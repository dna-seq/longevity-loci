"""RM1's export, on the committed fixture (assets/) and on the curated rows (rows/, corpus/). Every expected value is
computed from the rows at run time; the exported cells are read back through 0.8's own models."""

from __future__ import annotations

import csv
import io
import shutil
from collections import Counter
from pathlib import Path

import pytest
from just_dna_format.spec import StudyRow, VariantRow
from typer.testing import CliRunner

from longevity_loci.check import load_corpus
from longevity_loci.cli import app
from longevity_loci.export import (
    COMPUTED_EXACT,
    COMPUTED_PREFIXES,
    NOMINAL_TEST,
    PRIORITY,
    STUDY_COLUMNS,
    VARIANT_COLUMNS,
    VARIANT_TRAIT,
    Export,
    Gap,
    cell,
    export,
    load_rows,
    render,
    write,
)
from longevity_loci.models import Direction, Row, StatSignificance, Tier

REPO = Path(__file__).resolve().parent.parent
ASSETS = REPO / "assets"
REFERENCE = REPO / "docs" / "format08_reference" / "longevity_studies"
TREES = {"fixture": (ASSETS / "rows", ASSETS / "corpus"), "rows": (REPO / "rows", REPO / "corpus")}


@pytest.fixture(scope="module", params=sorted(TREES))
def tree(request: pytest.FixtureRequest) -> tuple[list[Row], Export, dict]:
    rows, corpus = TREES[request.param]
    notes, _ = load_corpus(corpus)
    return load_rows(rows), export(rows, corpus), notes


@pytest.fixture(scope="module")
def real() -> tuple[list[Row], Export]:
    rows, corpus = TREES["rows"]
    return load_rows(rows), export(rows, corpus)


def header(path: Path) -> list[str]:
    return next(csv.reader(path.open(encoding="utf-8")))


def citation(note) -> str:
    return str(note.head.pmid) if note.head.pmid is not None else "NONE"


def gap_total(result: Export, reason: Gap) -> int:
    return sum(n for (r, _), n in result.gaps.items() if r is reason)


def test_headers_are_08s() -> None:
    """studies.csv is the reference example's header exactly; variants.csv opens with the reference's and adds only
    columns 0.8's VariantRow declares, never a coordinate the enricher resolves nor an authored weight."""
    for columns, name in ((STUDY_COLUMNS, "studies.csv"), (VARIANT_COLUMNS, "variants.csv")):
        ref = header(REFERENCE / name)
        assert list(columns[: len(ref)]) == ref, name
    assert set(VARIANT_COLUMNS) <= set(VariantRow.model_fields)
    assert set(STUDY_COLUMNS) <= set(StudyRow.model_fields)
    assert not {"chrom", "start", "ref", "alts", "weight", "curator", "method"} & set(VARIANT_COLUMNS)


def test_variants_partition_the_rows(tree) -> None:
    """Each (rsid, genotype) of a row is one variants.csv row (alleles sorted); a variant with no genotype states is
    reported, not written."""
    rows, result, _ = tree
    expected = {(v.rsid, "/".join(sorted(g.genotype.split("/")))) for r in rows for v in r.variants for g in v.genotypes}
    assert {(x["rsid"], x["genotype"]) for x in result.variants} == expected
    assert len(result.variants) == len(expected)
    bare = [v for r in rows for v in r.variants if not v.genotypes]
    assert gap_total(result, Gap.NO_GENOTYPES) == len(bare)
    assert {x["rsid"] for x in result.variants} | {v.rsid for v in bare} == {v.rsid for r in rows for v in r.variants}


def test_variant_cells(tree) -> None:
    rows, result, _ = tree
    by_rsid = {v.rsid: (r, v) for r in rows for v in r.variants}
    for x in result.variants:
        row, v = by_rsid[x["rsid"]]
        g = next(g for g in v.genotypes if "/".join(sorted(g.genotype.split("/"))) == x["genotype"])
        assert x["state"] == g.state.value and x["conclusion"] == " ".join(g.conclusion.split())
        assert x["trait_efo_id"] == VARIANT_TRAIT
        assert x["priority"] == PRIORITY[row.axes.tier.value]
        assert x["category"] == row.axes.mechanism.value.value
        flags = x["flags"].split(";")
        assert flags[0] == f"tier:{row.axes.tier.value.value}"
        assert not [t for t in flags if t in COMPUTED_EXACT or t.startswith(COMPUTED_PREFIXES)]
        assert (x["requires_callable"], x["acmg_sf"]) == ("false", "false")
        if row.axes.tier.value is Tier.D:
            assert x["state"] == "neutral"


def test_every_study_maps_back(tree) -> None:
    """The exported studies and the rows' studies are one multiset under (rsid, citation, class, P, allele, proxy,
    quote): nothing added, nothing lost."""
    rows, result, notes = tree
    from_rows = Counter(
        (s.rsid, citation(notes[s.note]), s.phenotype_class.value, s.p_value or "", cell(s.p_value_num),
         s.effect_allele or "", s.proxy_rsid or "", notes[s.note].quotes[s.quote].text if s.quote else "")
        for r in rows for s in r.studies
    )
    exported = Counter(
        (x["rsid"], x["pmid"], x["phenotype_class"], x["p_value"], x["p_value_num"], x["effect_allele"],
         x["proxy_rsid"], x["provenance_quote"])
        for x in result.studies
    )
    assert exported == from_rows
    assert sum(len(r.studies) for r in rows) == len(result.studies) == len(result.quotes)


def test_proxy_allele_is_the_studys(real) -> None:
    """A proxy study writes its own effect_allele (the proxy's), never the lead variant's. The rows state no proxy's
    alleles, so the membership half of the check is not runnable here: 0.8's compiler checks it after the enricher
    resolves the proxy."""
    rows, result = real
    proxies = Counter((s.rsid, s.proxy_rsid, s.effect_allele or "") for r in rows for s in r.studies if s.proxy_rsid)
    assert proxies, "the curated rows hold proxy studies"
    assert Counter((x["rsid"], x["proxy_rsid"], x["effect_allele"]) for x in result.studies if x["proxy_rsid"]) == proxies


def test_nominal_is_significant_and_said(real) -> None:
    """The lead's rule: a nominal study is written significant (a replication that passed its own test, the format maintainers' RM434), its P kept exactly, and statistical_test says
    it was a nominal look-up. Never `unknown` for a known P."""
    rows, result = real
    nominal = Counter((s.rsid, s.p_value or "", cell(s.p_value_num)) for r in rows for s in r.studies
                      if s.stat_significance is StatSignificance.NOMINAL)
    assert nominal
    written = [x for x in result.studies if NOMINAL_TEST in x["statistical_test"]]
    assert Counter((x["rsid"], x["p_value"], x["p_value_num"]) for x in written) == nominal
    assert {x["stat_significance"] for x in written} == {"significant"}
    assert gap_total(result, Gap.STUDY_NOMINAL) == sum(nominal.values())
    held = Counter(s.stat_significance.value for r in rows for s in r.studies if s.stat_significance is not StatSignificance.NOMINAL)
    others = Counter(x["stat_significance"] for x in result.studies if NOMINAL_TEST not in x["statistical_test"])
    assert others == held and "unknown" not in others


def test_direction_without_effect_goes_to_conclusion(real) -> None:
    """The lead's rule: a study with allele, direction and P but no effect size writes its direction into
    `conclusion`, effect_size empty; one with an effect size leaves conclusion empty (the sign is the effect's)."""
    rows, result = real
    side = {Direction.PROTECTIVE: "longer-lived", Direction.RISK: "shorter-lived"}
    expected = Counter((s.rsid, s.p_value or "", f"{s.effect_allele} on the {side[s.direction]} side")
                       for r in rows for s in r.studies
                       if s.effect_size is None and s.effect_allele and s.direction in side)
    assert expected
    got = Counter((x["rsid"], x["p_value"], x["conclusion"]) for x in result.studies if x["conclusion"])
    assert got == expected
    assert all(x["effect_size"] == "" for x in result.studies if x["conclusion"])
    assert gap_total(result, Gap.DIRECTION_IN_CONCLUSION) == sum(expected.values())


def test_every_cell_parses_in_08(tree) -> None:
    """Read back from the written CSV, every row is one 0.8's models accept."""
    _, result, _ = tree
    for text, model in ((render(result.variants, VARIANT_COLUMNS), VariantRow), (render(result.studies, STUDY_COLUMNS), StudyRow)):
        for r in csv.DictReader(io.StringIO(text)):
            model.model_validate({k: v for k, v in r.items() if v != ""})


def test_sorted_and_byte_identical(tmp_path: Path) -> None:
    """rsid (by number), then genotype or citation; two runs write the same bytes."""
    rows, corpus = TREES["rows"]
    for name in ("a", "b"):
        write(export(rows, corpus), tmp_path / name)
    for f in ("variants.csv", "studies.csv", "quote_sources.csv"):
        assert (tmp_path / "a" / f).read_bytes() == (tmp_path / "b" / f).read_bytes()
    for f, second in (("variants.csv", "genotype"), ("studies.csv", "pmid"), ("quote_sources.csv", "pmid")):
        got = [(int(r["rsid"][2:]), r[second]) for r in csv.DictReader((tmp_path / "a" / f).open(encoding="utf-8"))]
        assert got == sorted(got), f


def test_fixture_study_is_an_orphan_and_said(tmp_path: Path) -> None:
    """The fixture's variants hold no genotypes, so its one study cites an rsid variants.csv lacks: written, and
    reported; its quote is the note's verbatim text."""
    rows, corpus = TREES["fixture"]
    result = export(rows, corpus)
    notes, _ = load_corpus(corpus)
    (row,) = load_rows(rows)
    (s,) = row.studies
    assert result.variants == []
    assert [x["provenance_quote"] for x in result.studies] == [notes[s.note].quotes[s.quote].text]
    assert result.gaps[(Gap.ORPHAN, s.rsid)] == 1
    q = result.quotes[0]
    assert (q["note"], q["quote_id"], q["depth"]) == (s.note, s.quote, notes[s.note].quotes[s.quote].depth.value)


def test_cli_writes_and_refuses(tmp_path: Path) -> None:
    rows, corpus = TREES["fixture"]
    runner = CliRunner()
    ok = runner.invoke(app, ["export", str(tmp_path / "out"), "--rows", str(rows), "--corpus", str(corpus)])
    assert ok.exit_code == 0, ok.output
    assert Gap.NO_GENOTYPES.value in ok.output
    assert header(tmp_path / "out" / "studies.csv") == list(STUDY_COLUMNS)
    broken = tmp_path / "rows"
    shutil.copytree(rows, broken)
    path = next(broken.glob("*.yaml"))
    path.write_text(path.read_text().replace("quote: q2", "quote: q99"))
    bad = runner.invoke(app, ["export", str(tmp_path / "bad"), "--rows", str(broken), "--corpus", str(corpus)])
    assert bad.exit_code == 1 and not (tmp_path / "bad").exists()
    missing = runner.invoke(app, ["export", str(tmp_path / "x"), "--rows", str(tmp_path / "none"), "--corpus", str(corpus)])
    assert missing.exit_code == 2
