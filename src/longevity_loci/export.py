"""RM1: the curated rows projected onto just-dna-format 0.8's module tables, `variants.csv` and `studies.csv`, with a
sidecar `quote_sources.csv` saying where each provenance quote was read. docs/FORMATS.md ("Export") is its prose.

A pure function of `rows/` and `corpus/`: nothing is read from the article cache. Every exported row is parsed by
0.8's own `VariantRow` / `StudyRow` before it is written, so a cell the format refuses is caught here, reported and
withheld, never written for the compiler to find. What the format has no place for is reported by reason, with a
count (`Gap`); nothing is dropped silently."""

from __future__ import annotations

import csv
import io
import re
from collections import Counter
from collections.abc import Callable
from dataclasses import dataclass, field
from enum import StrEnum
from pathlib import Path

import yaml
# Two of the compiler's own checks, called rather than restated beside it (private names: the pin is <0.9).
from just_dna_compiler.compiler.allele_checks import _check_p_value_num
from just_dna_compiler.compiler.table_checks import _distinct_study_rows
from just_dna_format.spec import StudyRow, VariantRow
from pydantic import ValidationError

from longevity_loci.check import Note, load_corpus
from longevity_loci.models import (
    Direction,
    PhenotypeClass,
    Row,
    StatSignificance,
    Study,
    StudyDesign,
    Tier,
    Variant,
)

# The reference example's own headers (docs/format08_reference/longevity_studies), then the
# module seat's ask (docs/ROADMAP.md RM1) where 0.8 has a column for it, in the template's order. Never
# chrom/start/ref/alts (the enricher resolves them), weight (the module authors none), curator/method (spec defaults).
VARIANT_COLUMNS: tuple[str, ...] = (
    "rsid", "genotype", "state", "direction", "conclusion", "gene", "trait_efo_id",
    "negatives", "priority", "phenotype", "category", "stat_significance", "effect_size", "effect_measure",
    "effect_allele", "flags", "requires_callable", "acmg_sf", "actionability",
)
STUDY_COLUMNS: tuple[str, ...] = (
    "rsid", "pmid", "doi", "proxy_rsid", "phenotype_class", "trait_efo_id", "effect_allele", "effect_size",
    "effect_measure", "effect_unit", "p_value", "p_value_num", "sample_size", "sample_unit", "n_cases", "age_min",
    "age_max", "age_of", "stratum", "stratum_level", "ancestry", "population", "study_design", "statistical_test",
    "conclusion", "provenance_quote", "curator", "stat_significance",
)
QUOTE_COLUMNS: tuple[str, ...] = ("rsid", "pmid", "doi", "note", "quote_id", "reading", "depth", "quote_absent")

# The reference example's rule: the variant carries lifespan, each study its own outcome's trait.
VARIANT_TRAIT = "OBA_VT0005372"
STUDY_TRAIT: dict[PhenotypeClass, str] = {  # as the reference example's studies.csv writes each class
    PhenotypeClass.HEALTHSPAN: "EFO_0009762",
    PhenotypeClass.PARENTAL_LIFESPAN: "EFO_0007796",
    PhenotypeClass.EXTREME_SURVIVAL_CC: "OBA_VT0005372",
    PhenotypeClass.OWN_SURVIVAL: "OBA_VT0005372",
}
PRIORITY: dict[Tier, str] = {Tier.A: "high", Tier.B: "medium", Tier.C: "low", Tier.D: "low"}
# Tokens 0.8 computes downstream (tradeoff, the European-only flag, causal and effector confidences, the LD pair):
# never authored into the module.
COMPUTED_EXACT = frozenset({"tradeoff", "eur_only_evidence"})
COMPUTED_PREFIXES = ("causal:", "effector:", "ld_proxy_of:")
COX = frozenset({StudyDesign.PARENTAL_LIFESPAN_COX, StudyDesign.OWN_SURVIVAL_COX, StudyDesign.HEALTHSPAN_COX})
PERCENTILE = {StudyDesign.PERCENTILE_CC_P90: "90th", StudyDesign.PERCENTILE_CC_P99: "99th"}
NOMINAL_TEST = "nominal replication look-up (p < 0.05 in the discovery's direction), not genome-wide; D11/D13"
DERIVED_UNIT = "crude odds ratio derived from the printed allele frequencies, not printed by the source"
DERIVED = re.compile(r"\bderived here\b")  # the curator's own words for an effect computed, not printed (D25.10)
SIDE = {Direction.PROTECTIVE: "longer-lived", Direction.RISK: "shorter-lived"}


class Gap(StrEnum):
    """What the export could not project as the row holds it, or changed on the way, by reason."""

    NO_GENOTYPES = "variant has no genotype states: no variants.csv row"
    VARIANT_TRAIT = "variant's trait_efo_id not written: the variant carries OBA_VT0005372 (the reference's rule)"
    VARIANT_NOMINAL = "variant stat_significance nominal written significant (0.8 has no nominal; the maintainers' RM434)"
    GENOTYPE_SORTED = "genotype's alleles written sorted, as 0.8 requires (the row holds them unsorted)"
    UNHARMONISED ="variant direction risk: effect_allele not harmonised to the lifespan-increasing allele (written)"
    AXIS_AGE = "axes.age_of_action: no 0.8 column"
    AXIS_OUTCOME = "axes.outcome: no 0.8 column (0.8 derives the outcome strip from phenotype_class)"
    COMPUTED_TOKEN = "computed token withheld from flags"
    STUDY_NOMINAL = "study nominal written significant, said not genome-wide in statistical_test (0.8 has no nominal; RM434)"
    ONE_SIDED = "study p_one_sided: no column, written into statistical_test"
    DIRECTION_IN_CONCLUSION = "study direction (no effect size) written into conclusion: no direction column"
    DIRECTION_BY_EFFECT = "study direction not written: no column; its effect_size and effect_allele carry the sign"
    DIRECTION_UNWRITTEN = "study direction not written: no column, and no effect size or allele to carry it"
    TRAIT_UNMAPPED = "study trait_efo_id empty: the reference example names no trait for its phenotype_class"
    DERIVED_EFFECT = "study effect derived, not printed: effect_unit says so in the lead's sentence"
    COX_BAND_CASES = "study n_cases withheld: a Cox model's age-band row counts events, not cases"
    PERCENTILE_TEST = "study percentile (p90, p99 design) written at the head of statistical_test: no percentile column"
    QUOTE_ABSENT = "study has no quote (quote_absent): provenance_quote empty"
    ORPHAN = "study's rsid has no variants.csv row"
    P_DISAGREE = "study p_value and p_value_num disagree beyond 1 % (0.8's check; strict validate refuses): written as held"
    DUPLICATE = "study not told apart from another analysis of its article (0.8's narrowing cells)"
    REFUSED = "row refused by 0.8's model: withheld"


class ExportError(Exception):
    """A real error: a row or note that does not parse, a study whose note or quote the corpus lacks."""


@dataclass
class Export:
    variants: list[dict[str, str]] = field(default_factory=list)
    studies: list[dict[str, str]] = field(default_factory=list)
    quotes: list[dict[str, str]] = field(default_factory=list)
    gaps: Counter[tuple[Gap, str]] = field(default_factory=Counter)  # (reason, detail) -> count

    def gap(self, reason: Gap, detail: str = "") -> None:
        self.gaps[(reason, detail)] += 1

    def by_reason(self) -> list[tuple[Gap, str, int]]:
        return [(r, d, n) for (r, d), n in sorted(self.gaps.items(), key=lambda kv: (list(Gap).index(kv[0][0]), kv[0][1]))]


def cell(v: object) -> str:
    """One CSV cell: empty for None, `true`/`false`, a float without a trailing `.0`, a list `;`-joined."""
    if v is None:
        return ""
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, float):
        return str(int(v)) if v.is_integer() and abs(v) < 1e15 else repr(v)
    if isinstance(v, (list, tuple)):
        return ";".join(cell(x) for x in v)
    return str(getattr(v, "value", v))


def _flags(row: Row, out: Export) -> str:
    tokens = [f"tier:{row.axes.tier.value.value}", *row.axes.pleiotropy.values, *row.axes.context.values,
              *row.axes.actionability.what]
    if row.axes.actionability.who is not None:
        tokens.append(row.axes.actionability.who.value)
    tokens += [f.token for f in row.flags]
    kept: list[str] = []
    for t in tokens:
        if t in COMPUTED_EXACT or t.startswith(COMPUTED_PREFIXES):
            out.gap(Gap.COMPUTED_TOKEN, t.split(":")[0])
        elif t not in kept:
            kept.append(t)
    return ";".join(kept)


def _variant_rows(row: Row, v: Variant, flags: str, out: Export) -> list[dict[str, str]]:
    if not v.genotypes:
        out.gap(Gap.NO_GENOTYPES)
        return []
    if v.trait_efo_id is not None and v.trait_efo_id != VARIANT_TRAIT:
        out.gap(Gap.VARIANT_TRAIT, v.trait_efo_id)
    if v.direction is Direction.RISK:
        out.gap(Gap.UNHARMONISED)
    sig = v.stat_significance
    if sig is StatSignificance.NOMINAL:
        out.gap(Gap.VARIANT_NOMINAL)
        sig = StatSignificance.SIGNIFICANT
    shared = {
        "rsid": v.rsid, "direction": v.direction, "gene": v.gene or None, "trait_efo_id": VARIANT_TRAIT,
        "negatives": v.negatives, "priority": PRIORITY[row.axes.tier.value], "phenotype": v.phenotype,
        "category": row.axes.mechanism.value, "stat_significance": sig, "effect_size": v.effect_size,
        "effect_measure": v.effect_measure, "effect_allele": v.effect_allele, "flags": flags,
        "requires_callable": False, "acmg_sf": False, "actionability": row.axes.actionability.label,
    }
    out_rows = []
    for g in v.genotypes:
        genotype = "/".join(sorted(g.genotype.split("/")))  # 0.8 reads an unphased genotype's alleles sorted
        if genotype != g.genotype:
            out.gap(Gap.GENOTYPE_SORTED, f"{v.rsid} {g.genotype}")
        values = {**shared, "genotype": genotype, "state": g.state, "conclusion": " ".join(g.conclusion.split())}
        out_rows.append({k: cell(x) for k, x in values.items()})
    return out_rows


def _study_row(s: Study, note: Note, out: Export) -> dict[str, str]:
    head = note.head
    tests: list[str] = []
    if s.study_design in PERCENTILE:  # 0.8 has no percentile cell: it leads statistical_test (the compiler's RM140)
        tests.append(f"cases at or beyond the {PERCENTILE[s.study_design]} survival percentile")
        out.gap(Gap.PERCENTILE_TEST)
    sig = s.stat_significance
    if sig is StatSignificance.NOMINAL:
        sig = StatSignificance.SIGNIFICANT
        tests.append(NOMINAL_TEST)
        out.gap(Gap.STUDY_NOMINAL)
    if s.p_one_sided is not None:
        tests.append(f"one-sided p {cell(s.p_one_sided)} in the discovery's direction (D26.13)")
        out.gap(Gap.ONE_SIDED)
    if s.statistical_test:
        tests.append(s.statistical_test)
    conclusion = None
    if s.direction is not None:
        if s.effect_size is None and s.effect_allele and s.direction in SIDE:
            conclusion = f"{s.effect_allele} on the {SIDE[s.direction]} side"
            out.gap(Gap.DIRECTION_IN_CONCLUSION)
        elif s.effect_size is not None and s.effect_allele:
            out.gap(Gap.DIRECTION_BY_EFFECT)
        else:
            out.gap(Gap.DIRECTION_UNWRITTEN, s.direction.value)
    unit = s.effect_unit
    if unit and DERIVED.search(unit):
        unit = DERIVED_UNIT
        out.gap(Gap.DERIVED_EFFECT)
    n_cases = s.n_cases
    if n_cases is not None and s.study_design in COX and (s.age_min is not None or s.age_max is not None):
        n_cases = None
        out.gap(Gap.COX_BAND_CASES)
    trait = STUDY_TRAIT.get(s.phenotype_class)
    if trait is None:
        out.gap(Gap.TRAIT_UNMAPPED, s.phenotype_class.value)
    quote = None
    if s.quote is None:
        out.gap(Gap.QUOTE_ABSENT, s.quote_absent.value if s.quote_absent else "")
    else:
        quote = note.quotes[s.quote].text
    values = {
        "rsid": s.rsid, "pmid": head.pmid if head.pmid is not None else "NONE",
        "doi": head.doi if head.pmid is None else None, "proxy_rsid": s.proxy_rsid,
        "phenotype_class": s.phenotype_class, "trait_efo_id": trait, "effect_allele": s.effect_allele,
        "effect_size": s.effect_size, "effect_measure": s.effect_measure, "effect_unit": unit,
        "p_value": s.p_value, "p_value_num": s.p_value_num, "sample_size": s.sample_size,
        "sample_unit": s.sample_unit, "n_cases": n_cases, "age_min": s.age_min, "age_max": s.age_max,
        "age_of": s.age_of, "stratum": s.stratum, "stratum_level": s.stratum_level, "ancestry": list(s.ancestry),
        "population": s.population, "study_design": s.study_design, "statistical_test": "; ".join(tests) or None,
        "conclusion": conclusion, "provenance_quote": quote, "curator": s.curator, "stat_significance": sig,
    }
    return {k: cell(x) for k, x in values.items()}


def _quote_row(s: Study, note: Note) -> dict[str, str]:
    q = note.quotes[s.quote] if s.quote is not None else None
    values = {
        "rsid": s.rsid, "pmid": note.head.pmid if note.head.pmid is not None else "NONE",
        "doi": note.head.doi if note.head.pmid is None else None, "note": note.head.key, "quote_id": s.quote,
        "reading": q.reading.isoformat() if q else None, "depth": q.depth if q else None,
        "quote_absent": s.quote_absent,
    }
    return {k: cell(x) for k, x in values.items()}


def _parsed(model: type[VariantRow] | type[StudyRow], values: dict[str, str], where: str, out: Export) -> object | None:
    """0.8's own model over the cells as the compiler would read them from the CSV; a refusal is a gap."""
    try:
        return model.model_validate({k: x for k, x in values.items() if x != ""})
    except ValidationError as e:
        first = e.errors()[0]
        out.gap(Gap.REFUSED, f"{model.__name__} {where}: {'.'.join(map(str, first['loc'])) or 'row'}: {first['msg']}")
        return None


def _rsid_key(rsid: str) -> tuple[int, str]:
    return (int(rsid[2:]) if rsid[2:].isdigit() else -1, rsid)


def _sort_key(columns: tuple[str, ...], second: str) -> Callable[[dict[str, str]], tuple]:
    def key(r: dict[str, str]) -> tuple:
        return (_rsid_key(r["rsid"]), r[second], tuple(r[c] for c in columns))
    return key


def load_rows(rows: Path) -> list[Row]:
    if not rows.is_dir():
        raise FileNotFoundError(f"no rows directory: {rows}")
    out: list[Row] = []
    for path in sorted(rows.glob("*.yaml")):
        try:
            out.append(Row.model_validate(yaml.safe_load(path.read_text(encoding="utf-8"))))
        except (ValidationError, yaml.YAMLError) as e:
            raise ExportError(f"{path}: does not parse (run `loci check rows`): {str(e).splitlines()[0]}") from e
    return out


def export(rows: Path, corpus: Path) -> Export:
    """The projection, in memory. Raises ExportError on a real error; everything else is a counted Gap."""
    notes, findings = load_corpus(corpus)
    if findings:
        raise ExportError("; ".join(f"{f.path.name}: {f.detail}" for f in findings))
    out = Export()
    loaded = load_rows(rows)
    exported_rsids: set[str] = set()
    for row in loaded:
        out.gap(Gap.AXIS_AGE)
        out.gap(Gap.AXIS_OUTCOME)
        flags = _flags(row, out)
        for v in row.variants:
            for values in _variant_rows(row, v, flags, out):
                if _parsed(VariantRow, values, f"{v.rsid} {values['genotype']}", out) is not None:
                    out.variants.append(values)
                    exported_rsids.add(v.rsid)
    for row in loaded:
        for s in row.studies:
            note = notes.get(s.note)
            if note is None or (s.quote is not None and s.quote not in note.quotes):
                raise ExportError(f"locus {row.locus_id} study {s.rsid}: {s.cite or s.note} is not in the corpus (run `loci check rows`)")
            values = _study_row(s, note, out)
            if _parsed(StudyRow, values, f"{s.rsid} {s.note}", out) is None:
                continue
            if s.rsid not in exported_rsids:
                out.gap(Gap.ORPHAN, s.rsid)
            out.studies.append(values)
            out.quotes.append(_quote_row(s, note))
    out.variants.sort(key=_sort_key(VARIANT_COLUMNS, "genotype"))
    out.studies.sort(key=_sort_key(STUDY_COLUMNS, "pmid"))
    out.quotes.sort(key=_sort_key(QUOTE_COLUMNS, "pmid"))
    _compiler_checks(out)
    return out


def _compiler_checks(out: Export) -> None:
    """Two of the compiler's checks on studies.csv, reported here as gaps so the export names them before validate
    does: the duplicate rule (`_distinct_study_rows`: two rows under one (rsid, citation) are two claims only when
    some narrowing cell is stated in both and differs), and p_value against p_value_num (within 1 %). Neither value
    is changed: the row holds both, and which is right is the curator's to settle."""
    seen: dict[tuple[str, str], list[StudyRow]] = {}
    every: list[StudyRow] = []
    for values in out.studies:
        parsed = StudyRow.model_validate({k: x for k, x in values.items() if x != ""})
        siblings = seen.setdefault((values["rsid"], values["pmid"] + values["doi"]), [])
        if any(not _distinct_study_rows(parsed, sib) for sib in siblings):
            out.gap(Gap.DUPLICATE, f"{values['rsid']} {values['pmid'] if values['pmid'] != 'NONE' else values['doi']}")
        siblings.append(parsed)
        every.append(parsed)
    _, disagree = _check_p_value_num(every, strict=False)
    for message in disagree:
        out.gap(Gap.P_DISAGREE, str(message).split(":")[0])


def render(rows: list[dict[str, str]], columns: tuple[str, ...]) -> str:
    buf = io.StringIO()
    w = csv.DictWriter(buf, fieldnames=list(columns), lineterminator="\n")
    w.writeheader()
    w.writerows(rows)
    return buf.getvalue()


def write(result: Export, outdir: Path) -> dict[str, int]:
    """Write the three files into `outdir`; returns rows written per file."""
    outdir.mkdir(parents=True, exist_ok=True)
    files = {
        "variants.csv": (result.variants, VARIANT_COLUMNS),
        "studies.csv": (result.studies, STUDY_COLUMNS),
        "quote_sources.csv": (result.quotes, QUOTE_COLUMNS),
    }
    for name, (rows, columns) in files.items():
        (outdir / name).write_text(render(rows, columns), encoding="utf-8")
    return {name: len(rows) for name, (rows, _) in files.items()}
