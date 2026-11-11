"""A supplement in the cache (RM4): the fixture article's real Supplementary Data 1, fetched at run time into a
temporary cache (the file is the authors', never the repository's), rendered to text, and a quote read from it
located there and nowhere else."""

from __future__ import annotations

import gzip
import hashlib
import io
import json
import re
import shutil
import zipfile
from pathlib import Path

import openpyxl
import pytest

from longevity_loci.check import Kind, check_quotes
from longevity_loci.fetch import Outcome
from longevity_loci.supp import Unrenderable, cache_name, fetch_supplement, render

ASSETS = Path(__file__).resolve().parent.parent / "assets"
KEY = "pmid-31413261"  # the fixture note's article, Deelen 2019
DEELEN_SD1 = ("https://static-content.springer.com/esm/art%3A10.1038%2Fs41467-019-11558-2/MediaObjects/"
              "41467_2019_11558_MOESM2_ESM.xlsx")


@pytest.fixture(scope="session")
def deelen(tmp_path_factory: pytest.TempPathFactory) -> Path:
    cache = tmp_path_factory.mktemp("supp")
    got = fetch_supplement(KEY, DEELEN_SD1, cache)
    if got.outcome is Outcome.UNREACHABLE or any(f.outcome is Outcome.UNREACHABLE for f in got.files):
        pytest.skip(f"the publisher's file server unreachable: {got.detail or got.files}")
    assert got, got
    [cached] = got.files
    assert cached.path is not None and cached.path.name == cache_name(KEY, "41467_2019_11558_MOESM2_ESM.xlsx")
    return cached.path


def test_supplement_cached_with_its_sidecar(deelen: Path) -> None:
    text = deelen.read_text(encoding="utf-8")
    side = json.loads(deelen.with_name(deelen.name.removesuffix(".txt") + ".source.json").read_text())
    assert side["key"] == KEY and side["url"] == DEELEN_SD1
    assert side["sha256"] == hashlib.sha256(text.encode("utf-8")).hexdigest()
    assert text.startswith("## sheet: ")
    assert "rs11065979" in text and "ATXN2/BRAP" in text


def _row_quote(text: str, rsid: str, cells: int) -> str:
    """A run of cells from the table row holding `rsid`, as a curator copies it from the cache."""
    line = next(line for line in text.splitlines() if f"\t{rsid}\t" in line)
    parts = line.split("\t")
    i = parts.index(rsid)
    return "\t".join(parts[i : i + cells])


def _tree(tmp_path: Path, supp: Path | None, quote: str) -> Path:
    shutil.copytree(ASSETS / "corpus", tmp_path / "corpus")
    note = tmp_path / "corpus" / f"{KEY}.md"
    text = note.read_text().replace("depth: full_text", "depth: supplement")
    note.write_text(text + f"\n## Reading 2026-11-11, supplement\n\n> [q9] {quote}\n")
    (tmp_path / "cache").mkdir()
    if supp is not None:
        shutil.copy(supp, tmp_path / "cache" / supp.name)
    return tmp_path


def test_a_supplement_quote_is_located_in_the_supplement(tmp_path: Path, deelen: Path) -> None:
    quote = _row_quote(deelen.read_text(encoding="utf-8"), "rs11065979", 6).replace("\t", " ")
    assert quote.startswith("rs11065979 12 ")
    tree = _tree(tmp_path, deelen, quote)
    got = {f.where: f for f in check_quotes(tree / "corpus", tree / "cache")}
    assert got["q9"].kind is Kind.LOCATED and deelen.name in got["q9"].detail
    # the article's own quotes have no article text here: unknown, never looked for in the supplement
    assert {got[q].kind for q in ("q1", "q2")} == {Kind.NO_TEXT}


def test_a_supplement_quote_with_no_supplement_cached_is_unknown(tmp_path: Path, deelen: Path) -> None:
    quote = _row_quote(deelen.read_text(encoding="utf-8"), "rs11065979", 6).replace("\t", " ")
    tree = _tree(tmp_path, None, quote)
    got = {f.where: f.kind for f in check_quotes(tree / "corpus", tree / "cache")}
    assert got["q9"] is Kind.NO_TEXT


def test_a_supplement_quote_one_cell_changed_is_not_found(tmp_path: Path, deelen: Path) -> None:
    quote = _row_quote(deelen.read_text(encoding="utf-8"), "rs11065979", 6).replace("\t", " ")
    wrong = quote.replace("rs11065979 12 ", "rs11065979 11 ", 1)
    assert wrong != quote
    tree = _tree(tmp_path, deelen, wrong)
    got = {f.where: f.kind for f in check_quotes(tree / "corpus", tree / "cache")}
    assert got["q9"] is Kind.NOT_FOUND


def test_render_kinds() -> None:
    book = openpyxl.Workbook()
    book.active.title = "S1"
    rows = [["SNP", "EA", "P"], ["rs1", "A", 0.002], [None, None, None], ["rs2", "G", None]]
    for r in rows:
        book.active.append(r)
    buf = io.BytesIO()
    book.save(buf)
    assert render("t.xlsx", buf.getvalue()) == "## sheet: S1\nSNP\tEA\tP\nrs1\tA\t0.002\nrs2\tG\n"
    assert render("t.csv", b"SNP,EA\nrs1,A\n") == render("t.tsv", b"SNP\tEA\nrs1\tA\n") == "SNP\tEA\nrs1\tA\n"
    assert render("run.R", b"fit <- lm(y ~ x)\n") == "fit <- lm(y ~ x)\n"
    arc = io.BytesIO()
    with zipfile.ZipFile(arc, "w") as z:
        z.writestr("b/fig1.png", b"\x89PNG")
        z.writestr("a/table.csv", "SNP,EA\nrs1,A\n")
    out = render("deposit.zip", arc.getvalue())
    assert out.index("## file: a/table.csv\nSNP\tEA\nrs1\tA\n") < out.index("## file: b/fig1.png\n(not rendered")
    with pytest.raises(Unrenderable):
        render("figure.png", b"\x89PNG")


def test_an_unrenderable_file_writes_nothing(tmp_path: Path) -> None:
    got = fetch_supplement(KEY, "not a locator", tmp_path)
    assert got.outcome is Outcome.REFUSED and not got
    got = fetch_supplement("pmid-x", DEELEN_SD1, tmp_path)
    assert got.outcome is Outcome.REFUSED
    assert list(tmp_path.iterdir()) == []


def test_gzip_and_a_row_filter() -> None:
    """A summary-statistics deposit (Zenin 2019's is a 237 MB csv.gz) is cached as its header and the variants a row
    needs: streamed, never decompressed whole."""
    table = b"SNP\tA1\tbeta\tp\nrs1\tA\t0.1\t0.5\nrs3184504\tT\t-0.007\t0.128\nrs2\tG\t0.2\t0.9\n"
    packed = gzip.compress(table)
    assert render("stats.tsv.gz", packed) == render("stats.tsv", table)
    assert render("stats.tsv.gz", packed, rows=r"\brs3184504\b") == "SNP\tA1\tbeta\tp\nrs3184504\tT\t-0.007\t0.128\n"
    assert render("stats.tsv.gz", packed, rows=r"\brs999\b") == "SNP\tA1\tbeta\tp\n"
    assert cache_name(KEY, "stats.tsv.gz") != cache_name(KEY, "stats.tsv.gz", r"rs1") != cache_name(KEY, "stats.tsv.gz", r"rs2")


def test_a_filtered_supplement_keeps_each_sheet_header_and_the_row(tmp_path: Path, deelen: Path) -> None:
    full = deelen.read_text(encoding="utf-8")
    got = fetch_supplement(KEY, DEELEN_SD1, tmp_path, rows=r"\trs11065979\t")
    if not got and any(f.outcome is Outcome.UNREACHABLE for f in got.files):
        pytest.skip("the publisher's file server unreachable")
    [cached] = got.files
    lines = cached.path.read_text(encoding="utf-8").splitlines(keepends=True)
    sheets = [l for l in full.splitlines(keepends=True) if l.startswith("## sheet: ")]
    assert [l for l in lines if l.startswith("## sheet: ")] == sheets
    hits = [l for l in full.splitlines(keepends=True) if "\trs11065979\t" in l]
    assert hits and all(h in lines for h in hits)
    assert set(lines) <= set(full.splitlines(keepends=True))  # nothing written that the full rendering lacks
    side = json.loads(cached.path.with_name(cached.path.name.removesuffix(".txt") + ".source.json").read_text())
    assert side["rows"] == r"\trs11065979\t"


def test_a_json_record_is_one_object_a_line() -> None:
    record = {"data": {"variant": {"id": "6_160589086_A_G", "rsIds": ["rs10455872"],
                                   "alleleFrequencies": [{"populationName": "nfe_adj", "alleleFrequency": 0.0694},
                                                         {"populationName": "eas_adj", "alleleFrequency": None}]}}}
    assert render("variant.json", json.dumps(record).encode()) == (
        "data.variant id 6_160589086_A_G\n"
        "data.variant.rsIds[0] rs10455872\n"
        "data.variant.alleleFrequencies[0] populationName nfe_adj alleleFrequency 0.0694\n"
        "data.variant.alleleFrequencies[1] populationName eas_adj alleleFrequency null\n")


def test_a_database_record_is_refused_under_another_release(tmp_path: Path) -> None:
    """RM3: Ensembl states its release; a db note naming another is refused before anything is fetched, and one
    naming the current release is cached, and a record-depth quote from it is located."""
    probe = fetch_supplement("db-ensembl-1", "https://rest.ensembl.org/info/data?content-type=application/json",
                             tmp_path, name="info.json")
    if probe.outcome is Outcome.REFUSED and "could not be read" in probe.detail:
        pytest.skip(f"Ensembl unreachable: {probe.detail}")
    assert probe.outcome is Outcome.REFUSED and "not 1" in probe.detail, probe
    assert list(tmp_path.iterdir()) == []
    current = re.search(r"serves release (\d+)", probe.detail)[1]
    key = f"db-ensembl-{current}"
    (tmp_path / "c").mkdir()
    got = fetch_supplement(key, "https://rest.ensembl.org/info/data?content-type=application/json", tmp_path / "c",
                           name="info.json")
    assert got, got
    [cached] = got.files
    line = next(l for l in cached.path.read_text().splitlines() if l.startswith("releases[0] "))
    assert line == f"releases[0] {current}"
    corpus = tmp_path / "corpus"
    corpus.mkdir()
    (corpus / f"{key}.md").write_text(
        f"---\nkey: {key}\ndatabase: ensembl\nrelease: \"{current}\"\nurl: https://rest.ensembl.org/info/data\n"
        f"accessed: 2026-11-11\ndepth: record\n---\n\n## Reading 2026-11-11, record\n\n> [q1] {line}\n")
    found = {f.where: f for f in check_quotes(corpus, tmp_path / "c")}
    assert found["q1"].kind is Kind.LOCATED and cached.path.name in found["q1"].detail
