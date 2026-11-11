"""The research seats' first two checks: a row cites only quotes that exist in the corpus, and a note's quote is
found verbatim in its article's cached text. Each finding is a result with its kind, never a bare bool: a quote
that could not be checked (no cached text) is unknown, never a pass and never a failure."""

from __future__ import annotations

import csv
import glob
import logging
import re
import unicodedata
from collections import Counter
from dataclasses import dataclass, field
from datetime import date
from enum import StrEnum
from pathlib import Path

import yaml
from pydantic import ValidationError

from longevity_loci.models import (
    CITE, Depth, row_file, Direction, NoteHead, PhenotypeClass, Quote, Row, StatSignificance, State, StudyDesign, Tier,
)

log = logging.getLogger(__name__)

READING = re.compile(r"^## Reading (?P<date>\d{4}-\d{2}-\d{2}), (?P<depth>abstract|full_text|supplement|record)\s*$")
QUOTE_LINE = re.compile(r"^> \[(?P<qid>q\d+)\] (?P<text>.*)$")
DEPTH_ORDER = [Depth.ABSTRACT, Depth.FULL_TEXT, Depth.SUPPLEMENT, Depth.RECORD]


class Kind(StrEnum):
    OK = "ok"
    MALFORMED = "malformed"  # the file does not parse into its model
    MISNAMED = "misnamed"  # the file's name does not match what it holds
    DUPLICATE = "duplicate"  # two rows hold one locus_id
    NO_NOTE = "no_note"  # a cite names a note that is not in the corpus
    NO_QUOTE = "no_quote"  # a cite names a quote id its note does not hold
    UNSUPPORTED = "unsupported"  # an axis or flag cites nothing
    RULE = "rule"  # a row breaks one of the requirements' hard rules (§4.1, §6.3)
    INCOMPLETE = "incomplete"  # a scored variant's genotypes do not yet say what §6.2 asks (a warning)
    UNHARMONISED = "unharmonised"  # a variant's effect_allele is not the lifespan-increasing one (§6.2; a warning)
    UNGRAINED = "ungrained"  # a study's quote names neither its variant nor its gene (QUOTING.md rule 2; a warning)
    SHARED_QUOTE = "shared_quote"  # one quote cited for several variants: the plugin's QUOTING.md rule 2
    LOCATED = "located"
    NOT_FOUND = "not_found"  # the cached text is there and the quote is not in it
    NO_TEXT = "no_text"  # no cached text for the note: unknown, not checked


FAILING = frozenset({Kind.RULE, Kind.MALFORMED, Kind.MISNAMED, Kind.DUPLICATE, Kind.NO_NOTE, Kind.NO_QUOTE, Kind.NOT_FOUND})
UNKNOWN = frozenset({Kind.NO_TEXT})


@dataclass(frozen=True)
class Finding:
    kind: Kind
    path: Path
    where: str = ""
    detail: str = ""

    @property
    def passed(self) -> bool | None:
        """True a pass, False a failure, None not checked (or a warning that passes or fails nothing)."""
        if self.kind in FAILING:
            return False
        if self.kind in (Kind.OK, Kind.LOCATED):
            return True
        return None


@dataclass
class Note:
    path: Path
    head: NoteHead
    quotes: dict[str, Quote] = field(default_factory=dict)


def _front_matter(text: str) -> tuple[dict, list[str]]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("a note opens with a '---' front matter block")
    end = lines.index("---", 1)
    return yaml.safe_load("\n".join(lines[1:end])) or {}, lines[end + 1 :]


def load_note(path: Path) -> Note:
    """A note: its front matter, then readings (`## Reading YYYY-MM-DD, <depth>`, oldest first), each holding
    one-line `> [qN] text` quotes."""
    head_raw, body = _front_matter(path.read_text(encoding="utf-8"))
    note = Note(path=path, head=NoteHead.model_validate(head_raw))
    reading: date | None = None
    deepest: Depth | None = None
    after_quote = False
    for n, line in enumerate(body, start=1):
        if line.startswith("## Reading"):
            m = READING.match(line)
            if m is None:
                raise ValueError(f"body line {n}: a reading heading is '## Reading YYYY-MM-DD, <depth>': {line!r}")
            day = date.fromisoformat(m["date"])
            if reading is not None and day < reading:
                raise ValueError(f"body line {n}: readings go oldest first; {day} follows {reading}")
            reading, depth = day, Depth(m["depth"])
            if deepest is None or DEPTH_ORDER.index(depth) > DEPTH_ORDER.index(deepest):
                deepest = depth
            after_quote = False
        elif m := QUOTE_LINE.match(line):
            if reading is None:
                raise ValueError(f"quote {m['qid']} stands before any reading heading")
            if m["qid"] in note.quotes:
                raise ValueError(f"quote id {m['qid']} is used twice")
            if not normalise(m["text"]).strip('"').strip():
                raise ValueError(f"quote {m['qid']} is empty")
            if note.head.title and normalise(m["text"]).strip('"').strip().casefold() == normalise(note.head.title).casefold():
                raise ValueError(f"quote {m['qid']} is the article's title, which locates nothing (QUOTING.md rule 1)")
            note.quotes[m["qid"]] = Quote(qid=m["qid"], text=m["text"].strip(), reading=reading, depth=depth)
            after_quote = True
        elif line.startswith(">") and after_quote:
            raise ValueError(f"body line {n}: a quote is one line; a quote's continuation is not checked")
        else:
            after_quote = False
    if deepest is not None and note.head.depth != deepest:
        raise ValueError(f"depth is {note.head.depth.value}; the deepest reading is {deepest.value}")
    return note


def _files(directory: Path, pattern: str, label: str) -> list[Path]:
    if not directory.is_dir():
        raise FileNotFoundError(f"no {label} directory: {directory}")
    return sorted(directory.glob(pattern))


def load_corpus(corpus: Path) -> tuple[dict[str, Note], list[Finding]]:
    notes: dict[str, Note] = {}
    findings: list[Finding] = []
    for path in _files(corpus, "*.md", "corpus"):
        try:
            note = load_note(path)
        except (ValidationError, ValueError, yaml.YAMLError) as e:
            findings.append(Finding(Kind.MALFORMED, path, detail=str(e).replace("\n", " ")[:240]))
            continue
        if path.stem != note.head.key:
            findings.append(Finding(Kind.MISNAMED, path, detail=f"holds {note.head.key}"))
            continue
        notes[note.head.key] = note
    return notes, findings


def load_seed(seed: Path) -> dict[int, str]:
    """The seed list's locus ids and names (docs/longevitymap_v2/data/seed_variants.csv)."""
    with seed.open(encoding="utf-8") as f:
        return {int(r["locus_id"]): r["locus_name"] for r in csv.DictReader(f) if r["locus_id"]}


R_TIER_1_PMID = "pmid-22279548"  # §4.1 R-TIER-1: a row whose only support it is, is tier D
SCORED = frozenset({Tier.A, Tier.B})
# §6.3: required on every study supporting a tier A/B variant (pmid or doi is the note itself)
REQUIRED_AB = ("p_value", "p_value_num", "effect_size", "effect_measure", "effect_allele")
# D13, the person 2026-11-10 ("1a"): a nominal replication look-up supports with its allele, direction and p alone
REQUIRED_NOMINAL = ("p_value", "p_value_num", "effect_allele")
# D15, D20: a multivariate test, or a meta-analysis that prints no pooled effect, (a MANOVA across healthspan, lifespan and longevity) has a P and no single effect size
GENOME_WIDE = 5e-8
SUGGESTIVE_P = 1e-5
NOMINAL_P = 0.05  # §4.1: a replication counts at p < 0.05


def check_rules(row: Row, path: Path) -> list[Finding]:
    """The requirements' hard rules a row's own fields can show (§4.1, §6.2, §6.3). A study *supports* the row
    unless it is `not_significant`; null studies are kept as rows and support nothing."""
    out: list[Finding] = []
    tier = row.axes.tier.value

    def rule(where: str, detail: str) -> None:
        out.append(Finding(Kind.RULE, path, where, detail))

    supporting = [s for s in row.studies if s.stat_significance is not StatSignificance.NOT_SIGNIFICANT]
    significant = [s for s in supporting if s.stat_significance is StatSignificance.SIGNIFICANT]
    for i, s in enumerate(row.studies):
        if s.p_value_num is None:
            continue
        if s.stat_significance is StatSignificance.SIGNIFICANT and s.p_value_num >= GENOME_WIDE:
            rule(f"studies[{i}] {s.rsid}", f"significant with p {s.p_value_num:g}, not below 5e-8")
        if s.stat_significance is StatSignificance.SUGGESTIVE and not GENOME_WIDE <= s.p_value_num < SUGGESTIVE_P:
            rule(f"studies[{i}] {s.rsid}", f"suggestive with p {s.p_value_num:g}, not in [5e-8, 1e-5)")
        if s.stat_significance is StatSignificance.NOMINAL and not SUGGESTIVE_P <= s.p_value_num < NOMINAL_P:
            rule(f"studies[{i}] {s.rsid}", f"nominal with p {s.p_value_num:g}, not in [1e-5, 0.05)")
    if supporting and {s.note for s in supporting} == {R_TIER_1_PMID}:
        if tier is not Tier.D:
            rule("R-TIER-1", f"only support is PMID 22279548, so tier D, not {tier.value}")
        moving = [f"{v.rsid} {g.genotype}" for v in row.variants for g in v.genotypes if g.state is not State.NEUTRAL]
        if moving:
            rule("R-TIER-1", f"state neutral on every genotype: {', '.join(moving)}")
    for v in row.variants:
        if v.direction is Direction.RISK:
            out.append(Finding(Kind.UNHARMONISED, path, v.rsid,
                               f"effect_allele {v.effect_allele} is the lifespan-lowering one; §6.2 harmonises to the other, so direction reads protective"))
    if tier in SCORED:
        if not significant:
            rule("R-TIER-4", f"tier {tier.value} with no genome-wide significant study")
        if significant and all(s.phenotype_class is PhenotypeClass.MR for s in significant):
            rule("R-TIER-4", f"tier {tier.value} on MR-only results")
        if significant and all(s.sample_size == 1 for s in significant):
            rule("R-TIER-4", f"tier {tier.value} on n = 1 genomes")
        if (significant and all(s.study_design is StudyDesign.CENTENARIAN_CC for s in significant)
                and len({s.note for s in significant}) < 2):
            rule("R-TIER-2", f"tier {tier.value} on one unreplicated centenarian study; caps at C")
        for i, s in enumerate(row.studies):
            if s.stat_significance is StatSignificance.NOT_SIGNIFICANT:
                continue
            if (s.stat_significance is StatSignificance.NOMINAL or s.study_design is StudyDesign.MULTIVARIATE
                    or (s.study_design is StudyDesign.META_ANALYSIS and s.effect_size is None)):
                missing = [c for c in REQUIRED_NOMINAL if getattr(s, c) is None]
                if s.effect_size is None and s.direction in (None, Direction.UNKNOWN):
                    missing.append("direction (or effect_size)")
            else:
                missing = [c for c in REQUIRED_AB if getattr(s, c) is None]
            if missing:
                rule(f"studies[{i}] {s.rsid}", f"§6.3 requires on a study supporting tier {tier.value}: {', '.join(missing)}")
        for v in row.variants:
            states = [g.state for g in v.genotypes]
            neutral = states.count(State.NEUTRAL)
            if len(states) < 3:
                out.append(Finding(Kind.INCOMPLETE, path, v.rsid, f"{len(states)} of three genotypes"))
            elif v.direction is Direction.CONTESTED and neutral != len(states):
                rule(v.rsid, "a trade-off with unresolved direction (contested) is neutral on every genotype")
            elif v.direction is not Direction.CONTESTED and neutral != 1:
                rule(v.rsid, f"one genotype, the most common, is neutral; {neutral} are")
    return out


def check_rows(rows: Path, corpus: Path, seed: dict[int, str] | None = None) -> list[Finding]:
    """Every row parses, is named for its locus (the seed list's name, where the seed holds its id), holds loci
    (its own and those it folds in, `also_loci`) no other row holds, and cites only quotes its corpus holds."""
    notes, findings = load_corpus(corpus)
    stray = [p for p in _files(rows, "*", "rows") if p.suffix in (".yml", ".json")]
    findings += [Finding(Kind.MISNAMED, p, detail="a row is <locus_id>-<locus_name>.yaml") for p in stray]
    held: dict[int, Path] = {}
    quoted_for: dict[str, set[str]] = {}
    first_path: dict[str, Path] = {}
    for path in _files(rows, "*.yaml", "rows"):
        try:
            row = Row.model_validate(yaml.safe_load(path.read_text(encoding="utf-8")))
        except (ValidationError, yaml.YAMLError) as e:
            findings.append(Finding(Kind.MALFORMED, path, detail=str(e).replace("\n", " ")[:240]))
            continue
        if path.name != row_file(row.locus_id, row.locus_name):
            findings.append(Finding(Kind.MISNAMED, path, detail=f"holds locus {row.locus_id} {row.locus_name!r}, so {row_file(row.locus_id, row.locus_name)}"))
        if seed is not None and row.locus_id in seed and seed[row.locus_id] != row.locus_name:
            findings.append(Finding(Kind.MISNAMED, path, detail=f"the seed list names locus {row.locus_id} {seed[row.locus_id]}"))
        for locus in [row.locus_id, *row.also_loci]:
            if locus in held:
                findings.append(Finding(Kind.DUPLICATE, path, detail=f"locus {locus} is also {held[locus].name}"))
            held.setdefault(locus, path)
        if seed is not None:
            findings += [Finding(Kind.MISNAMED, path, "also_loci", f"the seed list holds no locus {i}")
                         for i in row.also_loci if i not in seed]
        findings += check_rules(row, path)
        for name in type(row.axes).model_fields:
            if not getattr(row.axes, name).cites:
                findings.append(Finding(Kind.UNSUPPORTED, path, f"axes.{name}"))
        for f in row.flags:
            if not f.cites:
                findings.append(Finding(Kind.UNSUPPORTED, path, f"flag {f.token}"))
        genes = {v.rsid: v.gene for v in row.variants}
        for i, s in enumerate(row.studies):
            if s.cite is None:
                continue
            quoted_for.setdefault(s.cite, set()).add(s.rsid)
            first_path.setdefault(s.cite, path)
            note = notes.get(s.note)
            quote = note.quotes.get(s.quote) if note else None
            if quote is not None:
                words = set(re.findall(r"[A-Za-z0-9]+", normalise(quote.text)))
                named = {s.rsid} | ({s.proxy_rsid} if s.proxy_rsid else set())  # the proxy is what the study reported
                if not named & words and not set(re.split(r"[^A-Za-z0-9]+", genes[s.rsid])) & words:
                    names = " / ".join(sorted(named))
                    findings.append(Finding(Kind.UNGRAINED, path, f"studies[{i}] {s.rsid}", f"{s.cite} names neither {names} nor {genes[s.rsid]}"))
        for where, cite in row.cites():
            m = CITE.match(cite)
            assert m is not None  # the model refused any other shape
            note = notes.get(m["note"])
            if note is None:
                findings.append(Finding(Kind.NO_NOTE, path, where, cite))
            elif m["quote"] not in note.quotes:
                findings.append(Finding(Kind.NO_QUOTE, path, where, cite))
            else:
                findings.append(Finding(Kind.OK, path, where, cite))
    for cite, rsids in sorted(quoted_for.items()):
        if len(rsids) > 1:
            findings.append(Finding(Kind.SHARED_QUOTE, first_path[cite], cite, ", ".join(sorted(rsids))))
    return findings


_TRANSLATE = str.maketrans(
    {"\u2018": "'", "\u2019": "'", "\u201c": '"', "\u201d": '"', "\u2010": "-", "\u2011": "-", "\u2012": "-",
     "\u2013": "-", "\u2014": "-", "\u2212": "-", "\u00ad": None, "\u00a0": " "}
)
_BREAK = re.compile(r"[-\u00ad\u2010\u2011][ \t]*\n[ \t]*")


def _nfkc_keeping_scripts(text: str) -> str:
    """NFKC (ligatures, full-width forms, odd spaces), except super- and subscripts: 10⁸ is not 108."""
    return "".join(
        c if unicodedata.decomposition(c).startswith(("<super>", "<sub>")) else unicodedata.normalize("NFKC", c)
        for c in text
    )


def normalise(text: str) -> str:
    """What "verbatim" survives: compatibility forms (ligatures, full-width), typographic quotes and dashes,
    soft hyphens, and any run of whitespace. Case, words, digits, super- and subscripts and punctuation are kept
    as written; a minus sign (U+2212) reads as a hyphen, as PDFs and typed notes mix the two."""
    text = _nfkc_keeping_scripts(text).translate(_TRANSLATE)
    return re.sub(r"\s+", " ", text).strip()


def text_forms(text: str) -> tuple[str, str]:
    """The cached text with a hyphen at a line break kept (genome-wide) and joined (signif-icant); an ASCII hyphen,
    a soft hyphen or a Unicode hyphen at the break are all read both ways."""
    kept = normalise(_BREAK.sub("-", text))
    joined = normalise(_BREAK.sub("", text))
    return kept, joined


def located(quote: str, forms: tuple[str, ...]) -> bool:
    """The quote occurs in a form of the text, starting and ending at a word boundary: a quote may not begin or end
    inside a word."""
    wanted = normalise(quote).strip('"').strip()
    pattern = re.compile(r"(?<!\w)" + re.escape(wanted) + r"(?!\w)")
    return any(pattern.search(f) for f in forms)


def check_quotes(corpus: Path, cache: Path) -> list[Finding]:
    """Every quote of every note is found in its cached text: `<cache>/<key>.txt` for a quote read in the article,
    the article's and its supplements' (`<key>.supp-*.txt`, RM4) for one read in a supplement, and a database
    record's cached answers (the same names under a `db-` key, RM3) for one read in a record. A quote whose text is
    not cached is unknown; a located supplement quote names the file it was found in."""
    notes, findings = load_corpus(corpus)
    for key, note in notes.items():
        article = cache / f"{key}.txt"
        supps = sorted(cache.glob(f"{glob.escape(key)}.supp-*.txt"))
        texts = {p.name: text_forms(p.read_text(encoding="utf-8", errors="strict")) for p in [article, *supps] if p.is_file()}
        for qid, quote in note.quotes.items():
            if quote.depth in (Depth.SUPPLEMENT, Depth.RECORD):  # a supplement's or a database record's files
                where = [n for n in texts if n != article.name] + ([article.name] if article.name in texts else [])
                wanted = f"{key}.supp-*.txt"
                if not supps:
                    findings.append(Finding(Kind.NO_TEXT, note.path, qid, wanted))
                    continue
            else:
                where, wanted = ([article.name] if article.name in texts else []), article.name
                if not where:
                    findings.append(Finding(Kind.NO_TEXT, note.path, qid, wanted))
                    continue
            found = next((n for n in where if located(quote.text, texts[n])), None)
            if found is None:
                findings.append(Finding(Kind.NOT_FOUND, note.path, qid, quote.text[:80]))
            else:
                detail = quote.text[:80] if found == article.name else f"in {found}: {quote.text[:80]}"
                findings.append(Finding(Kind.LOCATED, note.path, qid, detail))
    return findings


def summary(findings: list[Finding]) -> Counter[Kind]:
    return Counter(f.kind for f in findings)
