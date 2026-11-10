"""The checks, on the committed fixtures (assets/), against the real full text of their one article, fetched at run
time by `loci fetch`'s code into a temporary cache: the article's text is not ours, so it never lands in the
repository."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest
import yaml

from longevity_loci.check import FAILING, Kind, check_quotes, check_rows, load_note, load_seed, normalise, text_forms
from longevity_loci.fetch import Outcome, Source, fetch
from longevity_loci.models import Row, row_file

ASSETS = Path(__file__).resolve().parent.parent / "assets"
SEED = ASSETS.parent / "docs" / "longevitymap_v2" / "data" / "seed_variants.csv"


@pytest.fixture(scope="session")
def abstract(tmp_path_factory: pytest.TempPathFactory) -> str:
    """The article's open full text (the name is older than the fetch; it holds the abstract too)."""
    cache = tmp_path_factory.mktemp("fetch")
    got = fetch(31413261, cache)
    if got.outcome is Outcome.UNREACHABLE:
        pytest.skip(f"Europe PMC unreachable: {got.detail}")
    assert got.outcome is Outcome.FETCHED and got.source is Source.FULL_TEXT, got
    assert got.title == load_note(ASSETS / "corpus" / "pmid-31413261.md").head.title
    return (cache / "pmid-31413261.txt").read_text(encoding="utf-8")


@pytest.fixture()
def tree(tmp_path: Path) -> Path:
    shutil.copytree(ASSETS / "rows", tmp_path / "rows")
    shutil.copytree(ASSETS / "corpus", tmp_path / "corpus")
    (tmp_path / "cache").mkdir()
    return tmp_path


def kinds(findings) -> dict[Kind, int]:
    out: dict[Kind, int] = {}
    for f in findings:
        out[f.kind] = out.get(f.kind, 0) + 1
    return out


def fixture_cites() -> set[str]:
    row = Row.model_validate(yaml.safe_load((ASSETS / "rows" / "96-APOE.yaml").read_text()))
    return {c for _, c in row.cites()}


def test_rows_every_cite_resolves(tree: Path) -> None:
    findings = check_rows(tree / "rows", tree / "corpus")
    ok = {f.detail for f in findings if f.kind is Kind.OK}
    assert ok == fixture_cites()
    assert not [f for f in findings if f.passed is False]


def test_rows_missing_note_and_quote(tree: Path) -> None:
    row = tree / "rows" / "96-APOE.yaml"
    text = row.read_text()
    row.write_text(text.replace("tier: {value: A, cites: [pmid-31413261#q1, pmid-31413261#q2]}", "tier: {value: A, cites: [pmid-1#q1, pmid-31413261#q9]}"))
    found = {(f.kind, f.detail) for f in check_rows(tree / "rows", tree / "corpus")}
    assert (Kind.NO_NOTE, "pmid-1#q1") in found
    assert (Kind.NO_QUOTE, "pmid-31413261#q9") in found


def test_rows_misnamed_and_malformed(tree: Path) -> None:
    (tree / "rows" / "96-APOE.yaml").rename(tree / "rows" / "97-APOE.yaml")
    (tree / "rows" / "1-BAD.yaml").write_text("locus_id: 1\nlocus_name: BAD\nverdict: maybe\n")
    found = {(f.kind, f.path.name) for f in check_rows(tree / "rows", tree / "corpus")}
    assert (Kind.MISNAMED, "97-APOE.yaml") in found
    assert (Kind.MALFORMED, "1-BAD.yaml") in found


def test_quotes_located_in_real_abstract(tree: Path, abstract: str) -> None:
    (tree / "cache" / "pmid-31413261.txt").write_text(abstract)
    note = load_note(tree / "corpus" / "pmid-31413261.md")
    findings = check_quotes(tree / "corpus", tree / "cache")
    assert {f.where for f in findings if f.kind is Kind.LOCATED} == set(note.quotes)


def test_quotes_survive_pdf_extraction_forms(tree: Path, abstract: str) -> None:
    """Line breaks, hyphens split across a line (ASCII, soft, Unicode) and odd spaces are what a PDF's text adds."""
    pdfish = (abstract.replace("previous", "previ-\nous").replace("reports", "re\u00ad\nports")
              .replace("percentile", "percen\u2010\ntile").replace(" odds of", "\n odds\u00a0of")
              .replace("90th and", "90th\u2009and"))
    assert pdfish != abstract
    (tree / "cache" / "pmid-31413261.txt").write_text(pdfish)
    assert kinds(check_quotes(tree / "corpus", tree / "cache")) == {Kind.LOCATED: 2}


def test_quotes_must_start_and_end_at_word_boundaries(tree: Path, abstract: str) -> None:
    note = tree / "corpus" / "pmid-31413261.md"
    note.write_text(note.read_text() + "\n> [q3] onsistent with previous reports\n")
    (tree / "cache" / "pmid-31413261.txt").write_text(abstract)
    found = {f.where: f.kind for f in check_quotes(tree / "corpus", tree / "cache")}
    assert found == {"q1": Kind.LOCATED, "q2": Kind.LOCATED, "q3": Kind.NOT_FOUND}


@pytest.mark.parametrize(
    ("addition", "reason"),
    [
        ("> [q3] \"\"\n", "empty"),
        ("## Reading 2026-1-5, abstract\n", "reading heading"),
        ("## Reading 2020-01-01, abstract\n", "oldest first"),
        ("## Reading 2026-11-06, supplement\n", "deepest reading"),
        ("> continued on a second line\n", "one line"),
        ("> [q3] A meta-analysis of genome-wide association studies identifies multiple longevity genes.\n", "title"),
    ],
)
def test_note_malformed(tree: Path, addition: str, reason: str) -> None:
    note = tree / "corpus" / "pmid-31413261.md"
    text = note.read_text()
    if reason == "one line":
        text = text.replace("shows the opposite.\n", "shows the opposite.\n" + addition)
        assert addition in text
    else:
        text = text + "\n" + addition
    note.write_text(text)
    with pytest.raises(ValueError, match=reason):
        load_note(note)


def test_empty_and_missing_inputs_are_not_a_pass(tmp_path: Path) -> None:
    with pytest.raises(FileNotFoundError):
        check_rows(tmp_path / "nowhere", tmp_path / "nowhere")
    (tmp_path / "rows").mkdir()
    (tmp_path / "corpus").mkdir()
    assert check_rows(tmp_path / "rows", tmp_path / "corpus") == []


def test_rows_duplicate_locus_and_seed_name(tree: Path) -> None:
    text = (tree / "rows" / "96-APOE.yaml").read_text()
    (tree / "rows" / "96-APOC1.yaml").write_text(text.replace("locus_name: APOE", "locus_name: APOC1"))
    seed = load_seed(SEED)
    assert seed[96] == "APOE"
    found = {(f.kind, f.path.name) for f in check_rows(tree / "rows", tree / "corpus", seed)}
    assert (Kind.DUPLICATE, "96-APOE.yaml") in found
    assert (Kind.MISNAMED, "96-APOC1.yaml") in found


def test_one_signal_two_seed_ids(tree: Path) -> None:
    """D14 (the person, 2026-11-10, "2a"): two seed ids naming one signal are one row, under the lower id, the other
    folded in; a row for the folded id is then a duplicate, whichever file is read first, and the folded id is a
    seed locus."""
    seed = load_seed(SEED)
    assert 8 in seed and 157 in seed and "IL6R" in seed[8] and "IL6R" in seed[157]
    text = (tree / "rows" / "96-APOE.yaml").read_text()
    (tree / "rows" / "96-APOE.yaml").unlink()
    low = row_file(8, seed[8])
    folded = text.replace("locus_id: 96\nlocus_name: APOE\n", f"locus_id: 8\nlocus_name: {seed[8]}\nalso_loci: [157]\n")
    assert "also_loci: [157]" in folded
    (tree / "rows" / low).write_text(folded)

    def found() -> set[tuple[Kind, str, str]]:
        return {(f.kind, f.path.name, f.where) for f in check_rows(tree / "rows", tree / "corpus", seed) if f.kind in FAILING}

    assert found() == set()
    high = row_file(157, seed[157])
    (tree / "rows" / high).write_text(text.replace("locus_id: 96\nlocus_name: APOE\n", f"locus_id: 157\nlocus_name: {seed[157]}\n"))
    assert {k for k, _, _ in found()} == {Kind.DUPLICATE} and len(found()) == 1
    (tree / "rows" / high).unlink()
    (tree / "rows" / low).write_text(folded.replace("also_loci: [157]", "also_loci: [157, 9999]"))
    assert found() == {(Kind.MISNAMED, low, "also_loci")}
    (tree / "rows" / low).write_text(folded.replace("also_loci: [157]", "also_loci: [3]"))
    assert {k for k, _, _ in found()} == {Kind.MALFORMED}


@pytest.mark.parametrize(
    ("old", "new"),
    [
        ("pleiotropy: {values: []", "pleiotropy: {values: [tradoff]"),
        ("context: {values: []", "context: {values: [sex_specific:z]"),
        ("actionability: {label: descriptive", "actionability: {label: descriptive, who: self"),
        ("population: European", "population: ''"),
        ("  - rsid: rs429358\n    note:", "  - rsid: rs1\n    note:"),
        ("pleiotropy: {values: []", "pleiotropy: {values: [tradeoff]"),
        ("ancestry: [EUR]", "ancestry: [European]"),
        ("    quote: q2\n", ""),
        ("    quote: q2\n", "    quote: q2\n    quote_absent: unchecked\n"),
        ("    sample_unit: individuals\n", "    sample_unit: individuals\n    curator: AI\n"),
        ("n_cases: 11262", "n_cases: 99999"),
        ("    effect_measure: OR\n", ""),
        ("sample_unit: individuals", "sample_unit: individuals\n    stratum: sex"),
        ("sample_unit: individuals", "sample_unit: individuals\n    age_min: 90"),
        ("sample_unit: individuals", "sample_unit: individuals\n    age_min: 90\n    age_max: 60\n    age_of: participant"),
    ],
)
def test_row_refused(tree: Path, old: str, new: str) -> None:
    row = tree / "rows" / "96-APOE.yaml"
    text = row.read_text()
    assert old in text
    row.write_text(text.replace(old, new))
    assert {f.kind for f in check_rows(tree / "rows", tree / "corpus")} >= {Kind.MALFORMED}


def test_one_quote_for_two_variants_is_flagged(tree: Path) -> None:
    row = tree / "rows" / "96-APOE.yaml"
    text = row.read_text()
    study = text[text.index("  - rsid: rs429358\n    note:"):]
    row.write_text(text + study.replace("rsid: rs429358", "rsid: rs7412", 1))
    shared = [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.SHARED_QUOTE]
    assert [(f.where, f.detail) for f in shared] == [("pmid-31413261#q2", "rs429358, rs7412")]


def test_study_carries_08_fields(tree: Path) -> None:
    row = Row.model_validate(yaml.safe_load((tree / "rows" / "96-APOE.yaml").read_text()))
    s = row.studies[0]
    assert (s.ancestry, s.sample_unit.value) == (["EUR"], "individuals")
    assert s.n_cases is not None and s.sample_size is not None and s.n_cases < s.sample_size


def test_outcome_cells_read_as_the_requirements_write_them(tree: Path) -> None:
    row = tree / "rows" / "96-APOE.yaml"
    row.write_text(row.read_text().replace("healthspan: untested, lifespan: untested", "healthspan: 0, lifespan: '-'"))
    parsed = Row.model_validate(yaml.safe_load(row.read_text()))
    assert (parsed.axes.outcome.healthspan.value, parsed.axes.outcome.lifespan.value) == ("0", "\u2212")


def test_quotes_one_word_changed_is_not_found(tree: Path, abstract: str) -> None:
    assert "lower odds" in abstract
    (tree / "cache" / "pmid-31413261.txt").write_text(abstract.replace("lower odds", "higher odds"))
    found = {f.where: f.kind for f in check_quotes(tree / "corpus", tree / "cache")}
    assert found == {"q1": Kind.NOT_FOUND, "q2": Kind.LOCATED}


def test_quotes_no_cached_text_is_unknown(tree: Path) -> None:
    findings = check_quotes(tree / "corpus", tree / "cache")
    assert kinds(findings) == {Kind.NO_TEXT: 2}
    assert all(f.passed is None for f in findings)


def test_normalise_keeps_words_and_case() -> None:
    assert normalise("signi\ufb01cant e\ufb00ect") == "significant effect"
    assert normalise("p < 10\u207b\u2078") != normalise("p < 10-8")
    assert normalise("ApoE “ε4” – x") == 'ApoE "ε4" - x'
    assert normalise("ApoE") != normalise("apoe")
    kept, joined = text_forms("genome-\nwide signif-\nicant")
    assert "genome-wide" in kept and "significant" in joined


def _row(tree: Path) -> Path:
    return tree / "rows" / "96-APOE.yaml"


@pytest.mark.parametrize(
    ("old", "new", "rule", "reason"),
    [
        ("stat_significance: significant\n    p_value: \"1.3 × 10−56\"\n    p_value_num: 1.3e-56",
         "stat_significance: suggestive\n    p_value: \"2e-6\"\n    p_value_num: 2.0e-6", "R-TIER-4", "no genome-wide"),
        ("p_value_num: 1.3e-56", "p_value_num: 0.2", "studies[0] rs429358", "not below 5e-8"),
        ("stat_significance: significant\n    p_value: \"1.3 × 10−56\"\n    p_value_num: 1.3e-56",
         "stat_significance: suggestive\n    p_value: \"0.01\"\n    p_value_num: 0.01", "studies[0] rs429358", "not in [5e-8"),
        ("    n_cases: 11262        # the abstract: 11,262 cases at the 90th percentile\n    sample_size: 36745",
         "    n_cases: 1\n    sample_size: 1", "R-TIER-4", "n = 1"),
        ("    p_value_num: 1.3e-56\n", "", "studies[0] rs429358", "p_value_num"),
        ("phenotype_class: EXTREME_SURVIVAL_CC", "phenotype_class: MR", "R-TIER-4", "MR-only"),
        ("study_design: percentile_case_control_p90", "study_design: centenarian_case_control", "R-TIER-2", "centenarian"),
        ("    effect_allele: C\n", "", "studies[0] rs429358", "effect_allele"),
        ("stat_significance: significant\n    p_value: \"1.3 × 10−56\"\n    p_value_num: 1.3e-56",
         "stat_significance: nominal\n    p_value: \"0.2\"\n    p_value_num: 0.2", "studies[0] rs429358", "not in [1e-5, 0.05)"),
        ("stat_significance: significant\n    p_value: \"1.3 × 10−56\"\n    p_value_num: 1.3e-56",
         "stat_significance: nominal\n    p_value: \"2e-6\"\n    p_value_num: 2.0e-6", "studies[0] rs429358", "not in [1e-5, 0.05)"),
    ],
)
def test_hard_rules(tree: Path, old: str, new: str, rule: str, reason: str) -> None:
    text = _row(tree).read_text()
    assert old in text
    _row(tree).write_text(text.replace(old, new))
    rules = [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.RULE]
    if not rule:
        assert rules == []
        return
    assert any(f.where == rule and reason in f.detail for f in rules), rules


def test_rules_quiet_on_the_fixture(tree: Path) -> None:
    kinds_seen = {f.kind for f in check_rows(tree / "rows", tree / "corpus")}
    assert Kind.RULE not in kinds_seen and Kind.INCOMPLETE in kinds_seen


def test_genotypes_one_neutral_unless_tradeoff(tree: Path) -> None:
    text = _row(tree).read_text()
    three = ("    genotypes:\n      - {genotype: TT, state: neutral, conclusion: x}\n"
             "      - {genotype: CT, state: risk, conclusion: x}\n      - {genotype: CC, state: risk, conclusion: x}\n")
    text = text.replace("    direction: risk\n", "    direction: risk\n" + three, 1)
    _row(tree).write_text(text)
    assert not [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.RULE]
    _row(tree).write_text(text.replace("state: risk, conclusion: x}\n      - {genotype: CC", "state: neutral, conclusion: x}\n      - {genotype: CC"))
    assert {f.where for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.RULE} == {"rs429358"}


def test_r_tier_1(tree: Path) -> None:
    note = tree / "corpus" / "pmid-22279548.md"
    note.write_text("---\nkey: pmid-22279548\npmid: 22279548\ntitle: x\nyear: 2012\ntitle_checked: 2026-11-05\n"
                    "depth: abstract\n---\n\n## Reading 2026-11-05, abstract\n\n> [q1] a passage\n")
    text = _row(tree).read_text().replace("note: pmid-31413261\n    quote: q2", "note: pmid-22279548\n    quote: q1")
    _row(tree).write_text(text)
    assert "R-TIER-1" in {f.where for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.RULE}


def test_quote_absent_with_its_reason(tree: Path) -> None:
    text = _row(tree).read_text().replace("    quote: q2\n", "    quote_absent: unchecked\n")
    _row(tree).write_text(text)
    findings = check_rows(tree / "rows", tree / "corpus")
    assert not [f for f in findings if f.passed is False]
    assert "studies[0] rs429358" not in {f.where for f in findings if f.kind is Kind.OK}


def test_quote_naming_neither_variant_nor_gene_is_flagged(tree: Path, abstract: str) -> None:
    sentence = "Gene-level association analysis reveals a role for tissue-specific expression of multiple genes in longevity."
    assert sentence in abstract
    note = tree / "corpus" / "pmid-31413261.md"
    note.write_text(note.read_text() + "\n> [q3] " + sentence + "\n")
    _row(tree).write_text(_row(tree).read_text().replace("    quote: q2\n", "    quote: q3\n"))
    flagged = [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.UNGRAINED]
    assert [f.where for f in flagged] == ["studies[0] rs429358"]


NULL_STUDY = """  - rsid: rs429358
    note: {note}
    quote_absent: not_found
    phenotype_class: PARENTAL_LIFESPAN
    study_design: parental_lifespan_cox
    population: European
    stat_significance: not_significant
"""


def test_a_null_study_supports_nothing(tree: Path) -> None:
    """§6.3's columns are asked of supporting studies only; a null study is kept as a row and needs none."""
    _row(tree).write_text(_row(tree).read_text() + NULL_STUDY.format(note="pmid-31413261"))
    assert not [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.RULE]


def _r_tier_1_note(tree: Path) -> None:
    (tree / "corpus" / "pmid-22279548.md").write_text(
        "---\nkey: pmid-22279548\npmid: 22279548\ntitle: x\nyear: 2012\ntitle_checked: 2026-11-05\n"
        "depth: abstract\n---\n\n## Reading 2026-11-05, abstract\n\n> [q1] a passage\n")


def test_r_tier_1_with_a_null_study_elsewhere(tree: Path) -> None:
    _r_tier_1_note(tree)
    text = _row(tree).read_text().replace("note: pmid-31413261\n    quote: q2", "note: pmid-22279548\n    quote: q1")
    _row(tree).write_text(text + NULL_STUDY.format(note="pmid-31413261"))
    found = [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.RULE and f.where == "R-TIER-1"]
    assert [f.detail for f in found] == ["only support is PMID 22279548, so tier D, not A"]


def test_r_tier_1_neutral_on_every_genotype(tree: Path) -> None:
    _r_tier_1_note(tree)
    text = _row(tree).read_text().replace("note: pmid-31413261\n    quote: q2", "note: pmid-22279548\n    quote: q1")
    text = text.replace("tier: {value: A,", "tier: {value: D,").replace(
        "    direction: risk\n", "    direction: risk\n    genotypes:\n      - {genotype: CC, state: risk, conclusion: x}\n", 1)
    _row(tree).write_text(text)
    found = [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.RULE]
    assert [(f.where, f.detail) for f in found] == [("R-TIER-1", "state neutral on every genotype: rs429358 CC")]


GENOTYPES = ("    genotypes:\n      - {{genotype: TT, state: {a}, conclusion: x}}\n"
             "      - {{genotype: CT, state: {b}, conclusion: x}}\n      - {{genotype: CC, state: {c}, conclusion: x}}\n")


@pytest.mark.parametrize(
    ("direction", "states", "fails"),
    [
        ("risk", ("neutral", "risk", "risk"), False),
        ("contested", ("neutral", "neutral", "neutral"), False),
        ("contested", ("neutral", "risk", "risk"), True),
        ("risk", ("neutral", "neutral", "risk"), True),
    ],
)
def test_genotype_states_by_direction(tree: Path, direction: str, states: tuple[str, str, str], fails: bool) -> None:
    g = GENOTYPES.format(a=states[0], b=states[1], c=states[2])
    text = _row(tree).read_text().replace("    direction: risk\n", f"    direction: {direction}\n" + g, 1)
    _row(tree).write_text(text)
    rules = [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.RULE]
    assert [f.where for f in rules] == (["rs429358"] if fails else [])


def test_two_genotypes_are_incomplete(tree: Path) -> None:
    g = "    genotypes:\n      - {genotype: TT, state: neutral, conclusion: x}\n      - {genotype: CT, state: risk, conclusion: x}\n"
    _row(tree).write_text(_row(tree).read_text().replace("    direction: risk\n", "    direction: risk\n" + g, 1))
    found = {(f.where, f.detail) for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.INCOMPLETE}
    assert ("rs429358", "2 of three genotypes") in found


def test_r_tier_1_silent_when_other_support_exists(tree: Path) -> None:
    _r_tier_1_note(tree)
    text = _row(tree).read_text()
    study = text[text.index("  - rsid: rs429358\n    note:"):]
    _row(tree).write_text(text + study.replace("note: pmid-31413261\n    quote: q2", "note: pmid-22279548\n    quote: q1"))
    assert "R-TIER-1" not in {f.where for f in check_rows(tree / "rows", tree / "corpus")}


def test_nominal_replication_supports(tree: Path) -> None:
    """§4.1 counts a replication at p < 0.05: a nominal study beside the genome-wide one supports the row, so the
    §6.3 fields are asked of it too, and its band is checked."""
    text = _row(tree).read_text()
    study = text[text.index("studies:\n") + len("studies:\n"):]
    nominal = (study.replace("stat_significance: significant", "stat_significance: nominal")
               .replace('p_value: "1.3 × 10−56"', 'p_value: "0.002"').replace("p_value_num: 1.3e-56", "p_value_num: 0.002")
               .replace("study_design: percentile_case_control_p90", "study_design: age_threshold_case_control"))
    assert "stat_significance: nominal" in nominal and "age_threshold_case_control" in nominal
    _row(tree).write_text(text + nominal)
    assert not [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.RULE]
    _row(tree).write_text(text + nominal.replace("    effect_allele: C\n", "", 1))
    rules = [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.RULE]
    assert [(f.where, "effect_allele" in f.detail) for f in rules] == [("studies[1] rs429358", True)]


def test_nominal_look_up_supports_on_allele_direction_and_p(tree: Path) -> None:
    """D13 (the person, 2026-11-10, "1a"): a nominal replication look-up that gives no effect size supports a tier
    A/B row on its allele, its direction and its p; without a direction it does not, and a genome-wide study still
    owes all five of §6.3's fields."""
    text = _row(tree).read_text()
    study = text[text.index("studies:\n") + len("studies:\n"):]
    assert "    effect_size: " in study and "    effect_measure: " in study
    bare = "".join(line for line in study.splitlines(keepends=True)
                   if not line.startswith(("    effect_size:", "    effect_measure:", "    effect_unit:")))
    nominal = (bare.replace("stat_significance: significant", "stat_significance: nominal")
               .replace('p_value: "1.3 × 10−56"', 'p_value: "0.002"').replace("p_value_num: 1.3e-56", "p_value_num: 0.002"))
    assert "stat_significance: nominal" in nominal and "p_value_num: 0.002" in nominal

    def rules() -> list[tuple[str, str]]:
        found = check_rows(tree / "rows", tree / "corpus")
        assert not [f for f in found if f.kind in FAILING and f.kind is not Kind.RULE]
        return [(f.where, f.detail) for f in found if f.kind is Kind.RULE]

    _row(tree).write_text(text + nominal.replace("    effect_allele: C\n", "    effect_allele: C\n    direction: risk\n", 1))
    assert rules() == []
    _row(tree).write_text(text + nominal)
    assert [(w, "direction" in d) for w, d in rules()] == [("studies[1] rs429358", True)]
    _row(tree).write_text(text + nominal.replace("    effect_allele: C\n", "    effect_allele: C\n    direction: unknown\n", 1))
    assert [(w, "direction" in d) for w, d in rules()] == [("studies[1] rs429358", True)]
    _row(tree).write_text(text + bare.replace("    effect_allele: C\n", "    effect_allele: C\n    direction: risk\n", 1))
    assert [(w, "effect_size" in d and "effect_measure" in d) for w, d in rules()] == [("studies[1] rs429358", True)]


@pytest.mark.parametrize(("locus_id", "file"), [
    (81, "81-FES_FURIN.yaml"), (73, "73-KL_KL-VS.yaml"), (3, "3-PCSK9_R46L.yaml"), (74, "74-intergenic.yaml"), (103, "103.yaml"),
])
def test_row_named_from_a_seed_name_a_path_cannot_hold(tree: Path, locus_id: int, file: str) -> None:
    """The row holds the seed's name exactly; its file name makes each run outside [A-Za-z0-9._-] one '_' (a slash
    would be a directory), and a locus the seed leaves unnamed is <id>.yaml."""
    seed = load_seed(SEED)
    name = seed[locus_id]
    text = _row(tree).read_text().replace("locus_id: 96", f"locus_id: {locus_id}").replace("locus_name: APOE", f"locus_name: {name!r}")
    _row(tree).unlink()
    (tree / "rows" / file).write_text(text)
    findings = check_rows(tree / "rows", tree / "corpus", seed)
    assert [f for f in findings if f.kind is Kind.MISNAMED] == []
    (tree / "rows" / file).rename(tree / "rows" / f"{locus_id}-{name}.yaml".replace("/", "_slash_"))
    assert [f.kind for f in check_rows(tree / "rows", tree / "corpus", seed) if f.kind is Kind.MISNAMED] == [Kind.MISNAMED]


DB_NOTE = """---
key: db-opentargets-26.09
database: opentargets
release: "26.09"
url: https://platform.opentargets.org/variant/19_44908684_T_C
accessed: 2026-11-10
depth: record
---

## Reading 2026-11-10, record

> [q1] {value}
"""


def _cite_db(tree: Path, value: str = "19_44908684_T_C") -> None:
    (tree / "corpus" / "db-opentargets-26.09.md").write_text(DB_NOTE.format(value=value))
    text = _row(tree).read_text()
    first_cites = text.index("cites: [")
    _row(tree).write_text(text[:first_cites] + "cites: [db-opentargets-26.09#q1, " + text[first_cites + len("cites: ["):])


def test_a_database_release_is_cited_and_its_quote_unknown(tree: Path) -> None:
    """A fact from a database release cites a note on that release; its quote is unknown to `check quotes` until a
    record of the release is cached, never a pass (D12)."""
    _cite_db(tree)
    rows = check_rows(tree / "rows", tree / "corpus")
    assert "db-opentargets-26.09#q1" in {f.detail for f in rows if f.kind is Kind.OK}
    assert not [f for f in rows if f.passed is False]
    quotes = [f for f in check_quotes(tree / "corpus", tree / "cache") if f.path.name == "db-opentargets-26.09.md"]
    assert [(f.kind, f.passed) for f in quotes] == [(Kind.NO_TEXT, None)]


@pytest.mark.parametrize(("old", "new", "says"), [
    ("release: \"26.09\"", "release: \"26.10\"", "does not name"),
    ("depth: record", "depth: full_text", "record"),
    ("url: https://platform.opentargets.org/variant/19_44908684_T_C\n", "", "url"),
    ("accessed: 2026-11-10\n", "pmid: 31413261\naccessed: 2026-11-10\n", "pmid"),
])
def test_a_database_note_refused(tree: Path, old: str, new: str, says: str) -> None:
    _cite_db(tree)
    note = tree / "corpus" / "db-opentargets-26.09.md"
    assert old in note.read_text()
    note.write_text(note.read_text().replace(old, new))
    bad = [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.MALFORMED]
    assert [f.path.name for f in bad] == ["db-opentargets-26.09.md"] and says in bad[0].detail, bad


def test_a_study_never_rests_on_a_database_note(tree: Path) -> None:
    _cite_db(tree)
    _row(tree).write_text(_row(tree).read_text().replace("note: pmid-31413261\n    quote: q2", "note: db-opentargets-26.09\n    quote: q1"))
    bad = [f for f in check_rows(tree / "rows", tree / "corpus") if f.kind is Kind.MALFORMED]
    assert [f.path.name for f in bad] == ["96-APOE.yaml"] and "article" in bad[0].detail
