"""The research seats' first two checks: a row cites only quotes that exist in the corpus, and a note's quote is
found verbatim in its article's cached text. Each finding is a result with its kind, never a bare bool: a quote
that could not be checked (no cached text) is unknown, never a pass and never a failure."""

from __future__ import annotations

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

from longevity_loci.models import CITE, NoteHead, Quote, Row

log = logging.getLogger(__name__)

READING = re.compile(r"^## Reading (?P<date>\d{4}-\d{2}-\d{2})\b")
QUOTE_LINE = re.compile(r"^> \[(?P<qid>q\d+)\] (?P<text>.+)$")
ROW_NAME = re.compile(r"^(?P<id>\d+)-(?P<name>.+)\.yaml$")


class Kind(StrEnum):
    OK = "ok"
    MALFORMED = "malformed"  # the file does not parse into its model
    MISNAMED = "misnamed"  # the file's name does not match what it holds
    NO_NOTE = "no_note"  # a cite names a note that is not in the corpus
    NO_QUOTE = "no_quote"  # a cite names a quote id its note does not hold
    UNSUPPORTED = "unsupported"  # an axis or flag cites nothing
    LOCATED = "located"
    NOT_FOUND = "not_found"  # the cached text is there and the quote is not in it
    NO_TEXT = "no_text"  # no cached text for the note: unknown, not checked


FAILING = frozenset({Kind.MALFORMED, Kind.MISNAMED, Kind.NO_NOTE, Kind.NO_QUOTE, Kind.NOT_FOUND})
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
    """A note: its front matter, then readings (`## Reading YYYY-MM-DD ...`), each holding `> [qN] text` lines."""
    head_raw, body = _front_matter(path.read_text(encoding="utf-8"))
    note = Note(path=path, head=NoteHead.model_validate(head_raw))
    reading: date | None = None
    for line in body:
        if m := READING.match(line):
            reading = date.fromisoformat(m["date"])
        elif m := QUOTE_LINE.match(line):
            if reading is None:
                raise ValueError(f"quote {m['qid']} stands before any '## Reading <date>' heading")
            if m["qid"] in note.quotes:
                raise ValueError(f"quote id {m['qid']} is used twice")
            note.quotes[m["qid"]] = Quote(qid=m["qid"], text=m["text"].strip(), reading=reading)
    return note


def load_corpus(corpus: Path) -> tuple[dict[str, Note], list[Finding]]:
    notes: dict[str, Note] = {}
    findings: list[Finding] = []
    for path in sorted(corpus.glob("*.md")):
        try:
            note = load_note(path)
        except (ValidationError, ValueError, yaml.YAMLError) as e:
            findings.append(Finding(Kind.MALFORMED, path, detail=str(e).splitlines()[0]))
            continue
        if path.stem != note.head.key:
            findings.append(Finding(Kind.MISNAMED, path, detail=f"holds {note.head.key}"))
            continue
        notes[note.head.key] = note
    return notes, findings


def check_rows(rows: Path, corpus: Path) -> list[Finding]:
    """Every row parses, is named for its locus, and cites only quotes its corpus holds."""
    notes, findings = load_corpus(corpus)
    for path in sorted(rows.glob("*.yaml")):
        try:
            row = Row.model_validate(yaml.safe_load(path.read_text(encoding="utf-8")))
        except (ValidationError, yaml.YAMLError) as e:
            findings.append(Finding(Kind.MALFORMED, path, detail=str(e).splitlines()[0]))
            continue
        if path.name != f"{row.locus_id}-{row.locus_name}.yaml":
            findings.append(Finding(Kind.MISNAMED, path, detail=f"holds {row.locus_id}-{row.locus_name}"))
        for name in type(row.axes).model_fields:
            if not getattr(row.axes, name).cites:
                findings.append(Finding(Kind.UNSUPPORTED, path, f"axes.{name}"))
        for f in row.flags:
            if not f.cites:
                findings.append(Finding(Kind.UNSUPPORTED, path, f"flag {f.token}"))
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
    return findings


_TRANSLATE = str.maketrans(
    {"‘": "'", "’": "'", "“": '"', "”": '"', "‐": "-", "‑": "-", "‒": "-",
     "–": "-", "—": "-", "−": "-", "­": None, " ": " "}
)


def normalise(text: str) -> str:
    """What "verbatim" survives: compatibility forms (ligatures, full-width), typographic quotes and dashes,
    soft hyphens, and any run of whitespace. Case, words and punctuation are kept as written."""
    text = unicodedata.normalize("NFKC", text).translate(_TRANSLATE)
    return re.sub(r"\s+", " ", text).strip()


def text_forms(text: str) -> tuple[str, str]:
    """The cached text with a hyphen at a line break kept (genome-wide) and joined (signif-icant)."""
    kept = normalise(re.sub(r"-[ \t]*\n[ \t]*", "-", text))
    joined = normalise(re.sub(r"-[ \t]*\n[ \t]*", "", text))
    return kept, joined


def check_quotes(corpus: Path, cache: Path) -> list[Finding]:
    """Every quote of every note is found in `<cache>/<key>.txt`; a note with no cached text is unknown."""
    notes, findings = load_corpus(corpus)
    for key, note in notes.items():
        cached = cache / f"{key}.txt"
        if not cached.is_file():
            findings += [Finding(Kind.NO_TEXT, note.path, q, str(cached.name)) for q in note.quotes]
            continue
        forms = text_forms(cached.read_text(encoding="utf-8", errors="strict"))
        for qid, quote in note.quotes.items():
            wanted = normalise(quote.text).strip('"')
            kind = Kind.LOCATED if any(wanted in f for f in forms) else Kind.NOT_FOUND
            findings.append(Finding(kind, note.path, qid, quote.text[:80]))
    return findings


def summary(findings: list[Finding]) -> Counter[Kind]:
    return Counter(f.kind for f in findings)
