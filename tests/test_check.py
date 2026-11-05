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
from longevity_loci.check import Kind, check_quotes, check_rows, load_note, normalise, text_forms

ASSETS = Path(__file__).resolve().parent.parent / "assets"
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
    """Line breaks, a hyphen split across a line, a soft hyphen and odd spaces are what a PDF's text adds."""
    pdfish = abstract.replace("previous reports", "previ-\nous re­ports").replace(" odds of", "\n odds of")
    pdfish = pdfish.replace("percentile", "percentiﬂe".replace("ﬂ", "l"))  # same word: control
    pdfish = pdfish.replace("rs429358", "rs429358").replace("Consistent", "Consiﬁstent".replace("ﬁ", ""))
    (tree / "cache" / "pmid-31413261.txt").write_text(pdfish)
    assert kinds(check_quotes(tree / "corpus", tree / "cache")) == {Kind.LOCATED: 1}


def test_quotes_one_word_changed_is_not_found(tree: Path, abstract: str) -> None:
    assert "lower odds" in abstract
    (tree / "cache" / "pmid-31413261.txt").write_text(abstract.replace("lower odds", "higher odds"))
    assert kinds(check_quotes(tree / "corpus", tree / "cache")) == {Kind.NOT_FOUND: 1}


def test_quotes_no_cached_text_is_unknown(tree: Path) -> None:
    findings = check_quotes(tree / "corpus", tree / "cache")
    assert kinds(findings) == {Kind.NO_TEXT: 1}
    assert all(f.passed is None for f in findings)


def test_normalise_keeps_words_and_case() -> None:
    assert normalise("ApoE “ε4” – x") == 'ApoE "ε4" - x'
    assert normalise("ApoE") != normalise("apoe")
    kept, joined = text_forms("genome-\nwide signif-\nicant")
    assert "genome-wide" in kept and "significant" in joined
