"""The two checks, on the committed fixtures (assets/), against the real abstract of their one article fetched at
run time into a temporary cache: the article's text is not ours, so it never lands in the repository."""

from __future__ import annotations

import json
import shutil
import urllib.error
import urllib.request
from pathlib import Path

import pytest
import yaml

from longevity_loci.models import Row
from longevity_loci.check import Kind, check_quotes, check_rows, load_note, load_seed, normalise, text_forms

ASSETS = Path(__file__).resolve().parent.parent / "assets"
SEED = ASSETS.parent / "docs" / "longevitymap_v2" / "data" / "seed_variants.csv"
EPMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:{pmid}%20AND%20SRC:MED&resultType=core&format=json"


@pytest.fixture(scope="session")
def abstract() -> str:
    url = EPMC.format(pmid=31413261)
    try:
        with urllib.request.urlopen(url, timeout=30) as r:
            hit = json.load(r)["resultList"]["result"]
    except (urllib.error.URLError, TimeoutError) as e:
        pytest.skip(f"Europe PMC unreachable: {e}")
    if not hit or not hit[0].get("abstractText"):
        pytest.skip("Europe PMC returned no abstract for 31413261")
    return hit[0]["abstractText"]


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
    row.write_text(text.replace("tier: {value: A, cites: [pmid-31413261#q1]}", "tier: {value: A, cites: [pmid-1#q1, pmid-31413261#q9]}"))
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
    assert kinds(check_quotes(tree / "corpus", tree / "cache")) == {Kind.LOCATED: 1}


def test_quotes_must_start_and_end_at_word_boundaries(tree: Path, abstract: str) -> None:
    note = tree / "corpus" / "pmid-31413261.md"
    note.write_text(note.read_text() + "\n> [q2] onsistent with previous reports\n")
    (tree / "cache" / "pmid-31413261.txt").write_text(abstract)
    found = {f.where: f.kind for f in check_quotes(tree / "corpus", tree / "cache")}
    assert found == {"q1": Kind.LOCATED, "q2": Kind.NOT_FOUND}


@pytest.mark.parametrize(
    ("addition", "reason"),
    [
        ("> [q2] \"\"\n", "empty"),
        ("## Reading 2026-1-5, abstract\n", "reading heading"),
        ("## Reading 2020-01-01, abstract\n", "oldest first"),
        ("## Reading 2026-11-06, full_text\n", "deepest reading"),
        ("> continued on a second line\n", "one line"),
    ],
)
def test_note_malformed(tree: Path, addition: str, reason: str) -> None:
    note = tree / "corpus" / "pmid-31413261.md"
    text = note.read_text()
    if reason == "one line":
        text = text.replace("shows the opposite.\n", "shows the opposite.\n" + addition)
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


@pytest.mark.parametrize(
    ("old", "new"),
    [
        ("pleiotropy: {values: []", "pleiotropy: {values: [tradoff]"),
        ("context: {values: []", "context: {values: [sex_specific:z]"),
        ("actionability: {label: descriptive", "actionability: {label: descriptive, who: self"),
        ("population: European", "population: ''"),
        ("  - rsid: rs429358\n    note:", "  - rsid: rs1\n    note:"),
        ("pleiotropy: {values: []", "pleiotropy: {values: [tradeoff]"),
    ],
)
def test_row_refused(tree: Path, old: str, new: str) -> None:
    row = tree / "rows" / "96-APOE.yaml"
    text = row.read_text()
    assert old in text
    row.write_text(text.replace(old, new))
    assert {f.kind for f in check_rows(tree / "rows", tree / "corpus")} >= {Kind.MALFORMED}


def test_outcome_cells_read_as_the_requirements_write_them(tree: Path) -> None:
    row = tree / "rows" / "96-APOE.yaml"
    row.write_text(row.read_text().replace("healthspan: untested, lifespan: untested", "healthspan: 0, lifespan: '-'"))
    parsed = Row.model_validate(yaml.safe_load(row.read_text()))
    assert (parsed.axes.outcome.healthspan.value, parsed.axes.outcome.lifespan.value) == ("0", "\u2212")


def test_quotes_one_word_changed_is_not_found(tree: Path, abstract: str) -> None:
    assert "lower odds" in abstract
    (tree / "cache" / "pmid-31413261.txt").write_text(abstract.replace("lower odds", "higher odds"))
    assert kinds(check_quotes(tree / "corpus", tree / "cache")) == {Kind.NOT_FOUND: 1}


def test_quotes_no_cached_text_is_unknown(tree: Path) -> None:
    findings = check_quotes(tree / "corpus", tree / "cache")
    assert kinds(findings) == {Kind.NO_TEXT: 1}
    assert all(f.passed is None for f in findings)


def test_normalise_keeps_words_and_case() -> None:
    assert normalise("signi\ufb01cant e\ufb00ect") == "significant effect"
    assert normalise("p < 10\u207b\u2078") != normalise("p < 10-8")
    assert normalise("ApoE “ε4” – x") == 'ApoE "ε4" - x'
    assert normalise("ApoE") != normalise("apoe")
    kept, joined = text_forms("genome-\nwide signif-\nicant")
    assert "genome-wide" in kept and "significant" in joined
