"""A supplement in the cache (RM4): the fixture article's real Supplementary Data 1, fetched at run time into a
temporary cache (the file is the authors', never the repository's), rendered to text, and a quote read from it
located there and nowhere else."""

from __future__ import annotations

import hashlib
import io
import json
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
