"""`fetch`'s handling of what Europe PMC answers. The network is stubbed (each case is an answer the service or a
proxy can give); the code under test, the sorting of answers and the writes to the cache, runs for real."""

from __future__ import annotations

import hashlib
import io
import json
import urllib.error
from pathlib import Path

import pytest

from longevity_loci import fetch as fetch_mod
from longevity_loci.fetch import Outcome, Source, fetch, jats_to_text

PMID = 31413261
HIT = {"pmcid": "PMC6694136", "isOpenAccess": "Y", "title": "A title.", "abstractText": "An <i>abstract</i> here."}
JATS = "<article><body><p>Full text.</p><table><tr><td>rs1</td><td>0.6</td></tr></table></body><back>refs</back></article>"


def search(hits: list[dict]) -> bytes:
    return json.dumps({"resultList": {"result": hits}}).encode()


def http(code: int) -> urllib.error.HTTPError:
    return urllib.error.HTTPError("u", code, "x", {}, io.BytesIO())  # type: ignore[arg-type]


def stub(monkeypatch: pytest.MonkeyPatch, search_answer: object, full_answer: object = None) -> None:
    def get(url: str, timeout: float) -> bytes:
        answer = full_answer if "fullTextXML" in url else search_answer
        if isinstance(answer, BaseException):
            raise answer
        assert isinstance(answer, bytes)
        return answer

    monkeypatch.setattr(fetch_mod, "_get", get)


def cached(cache: Path) -> tuple[str, dict]:
    return (cache / f"pmid-{PMID}.txt").read_text(), json.loads((cache / f"pmid-{PMID}.source.json").read_text())


def test_full_text_written_with_its_sidecar(monkeypatch: pytest.MonkeyPatch, tmp_path: Path) -> None:
    stub(monkeypatch, search([HIT]), JATS.encode())
    got = fetch(PMID, tmp_path)
    assert (got.outcome, got.source) == (Outcome.FETCHED, Source.FULL_TEXT)
    text, side = cached(tmp_path)
    assert text == jats_to_text(JATS) and "refs" not in text and "rs1\t0.6\t" in text
    assert side["sha256"] == hashlib.sha256(text.encode()).hexdigest() and side["source"] == "full_text"
    assert not list(tmp_path.glob("*.part"))


@pytest.mark.parametrize("full", [http(404), b"<article></article>"])
def test_no_full_text_falls_back_to_the_abstract(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, full: object) -> None:
    stub(monkeypatch, search([HIT]), full)
    got = fetch(PMID, tmp_path)
    assert (got.outcome, got.source) == (Outcome.FETCHED, Source.ABSTRACT)
    assert cached(tmp_path)[0] == "An abstract here."


@pytest.mark.parametrize("fault", [http(503), http(429), ConnectionResetError("reset"), TimeoutError()])
def test_a_transient_fault_keeps_the_cached_full_text(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, fault: BaseException) -> None:
    (tmp_path / f"pmid-{PMID}.txt").write_text("OLD FULL TEXT")
    stub(monkeypatch, search([HIT]), fault)
    assert fetch(PMID, tmp_path).outcome is Outcome.UNREACHABLE
    assert (tmp_path / f"pmid-{PMID}.txt").read_text() == "OLD FULL TEXT"


@pytest.mark.parametrize(
    ("answer", "outcome"),
    [
        (http(400), Outcome.REFUSED),
        (http(502), Outcome.UNREACHABLE),
        (ConnectionResetError("reset"), Outcome.UNREACHABLE),
        (b"<html>proxy login</html>", Outcome.MALFORMED),
        (b'{"version": "6.9"}', Outcome.MALFORMED),
        (search([]), Outcome.NOT_FOUND),
        (search([{"title": "x"}]), Outcome.NO_TEXT),
    ],
)
def test_search_answers(monkeypatch: pytest.MonkeyPatch, tmp_path: Path, answer: object, outcome: Outcome) -> None:
    stub(monkeypatch, answer)
    got = fetch(PMID, tmp_path)
    assert got.outcome is outcome and bool(got) is False
    assert list(tmp_path.iterdir()) == []
