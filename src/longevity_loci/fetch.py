"""The article cache: an article's text fetched from Europe PMC into `$LOCI_CACHE/<key>.txt`, with a sidecar
`<key>.source.json` saying what was fetched (the open-access full text, or the abstract only), when, and the
text's sha256, so a text and a sidecar that do not belong together are seen.

The text is the article's, not ours: it stays in the cache, never in the repository, a message or an issue."""

from __future__ import annotations

import hashlib
import html
import json
import logging
import os
import re
import urllib.error
import urllib.request
from dataclasses import dataclass
from datetime import UTC, datetime
from enum import StrEnum
from pathlib import Path

log = logging.getLogger(__name__)

SEARCH = "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:{pmid}%20AND%20SRC:MED&resultType=core&format=json"
FULLTEXT = "https://www.ebi.ac.uk/europepmc/webservices/rest/{pmcid}/fullTextXML"
RETRYABLE_HTTP = frozenset({408, 425, 429, 500, 502, 503, 504})


class Source(StrEnum):
    FULL_TEXT = "full_text"
    ABSTRACT = "abstract"


class Outcome(StrEnum):
    FETCHED = "fetched"
    NOT_FOUND = "not_found"  # Europe PMC holds no record of the PMID
    NO_TEXT = "no_text"  # a record, with neither an open full text nor an abstract
    UNREACHABLE = "unreachable"  # no answer, or a busy or failing service: retryable, says nothing of the article
    REFUSED = "refused"  # the service refused the request (a 4xx): not retryable as it stands
    MALFORMED = "malformed"  # an answer that is not what the service sends (a proxy's page, a changed schema)


@dataclass(frozen=True)
class Fetched:
    outcome: Outcome
    key: str
    source: Source | None = None
    title: str | None = None
    detail: str = ""

    def __bool__(self) -> bool:
        return self.outcome is Outcome.FETCHED


@dataclass(frozen=True)
class _Reply:
    outcome: Outcome | None  # None: the body is there
    body: bytes = b""
    status: int | None = None
    detail: str = ""


def jats_to_text(xml: str) -> str:
    """JATS as plain text: a table cell ends in a tab, a row, paragraph, title or section in a line break."""
    xml = re.sub(r"<(ref-list|back)\b.*?</\1>", "", xml, flags=re.S)
    xml = re.sub(r"</(td|th)>", "\t", xml)
    xml = re.sub(r"</(tr|p|title|sec|caption|label)>", "\n", xml)
    return html.unescape(re.sub(r"<[^>]+>", "", xml))


def _get(url: str, timeout: float, body: bytes | None = None) -> bytes:
    """A GET, or with `body` a POST of JSON (a GraphQL API that answers no GET)."""
    req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"} if body is not None else {})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()


def _request(url: str, timeout: float, body: bytes | None = None) -> _Reply:
    """One GET (or POST of `body`), its failure sorted by what the caller should do next."""
    try:
        return _Reply(None, _get(url, timeout) if body is None else _get(url, timeout, body))
    except urllib.error.HTTPError as e:
        kind = Outcome.UNREACHABLE if e.code in RETRYABLE_HTTP else Outcome.REFUSED
        return _Reply(kind, status=e.code, detail=f"HTTP {e.code} from {url}")
    except (OSError, TimeoutError) as e:  # URLError, a reset or a timeout while reading
        return _Reply(Outcome.UNREACHABLE, detail=f"{type(e).__name__}: {e}")


def _write(path: Path, text: str) -> None:
    tmp = path.with_name(path.name + ".part")
    tmp.write_text(text, encoding="utf-8")
    os.replace(tmp, path)


def fetch(pmid: int, cache: Path, timeout: float = 60) -> Fetched:
    """Fetch one article's text into the cache; the open full text when Europe PMC has one, else the abstract.
    A full text Europe PMC does not serve (404) falls back to the abstract; a busy or failing service does not,
    so a transient fault never replaces a cached full text by an abstract."""
    key = f"pmid-{pmid}"
    reply = _request(SEARCH.format(pmid=pmid), timeout)
    if reply.outcome is not None:
        return Fetched(reply.outcome, key, detail=reply.detail)
    try:
        hits = json.loads(reply.body.decode("utf-8"))["resultList"]["result"]
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as e:
        return Fetched(Outcome.MALFORMED, key, detail=f"search answer: {type(e).__name__}")
    if not hits:
        return Fetched(Outcome.NOT_FOUND, key)
    hit = hits[0]
    text, source, url = None, None, None
    pmcid = hit.get("pmcid")
    if pmcid and hit.get("isOpenAccess") == "Y":
        url = FULLTEXT.format(pmcid=pmcid)
        full = _request(url, timeout)
        if full.outcome is Outcome.UNREACHABLE:
            return Fetched(full.outcome, key, title=hit.get("title"), detail=full.detail)
        if full.outcome is None:
            body = jats_to_text(full.body.decode("utf-8", errors="replace"))
            if body.strip():
                text, source = body, Source.FULL_TEXT
        if text is None:
            log.info("%s: no full text from %s (%s); the abstract instead", key, pmcid, full.detail or "empty")
    abstract = html.unescape(re.sub(r"<[^>]+>", "", hit.get("abstractText") or ""))
    if text is None and abstract.strip():
        text, source, url = abstract, Source.ABSTRACT, SEARCH.format(pmid=pmid)
    if text is None or source is None:
        return Fetched(Outcome.NO_TEXT, key, title=hit.get("title"))
    sidecar = {"key": key, "pmid": pmid, "pmcid": pmcid, "source": source.value, "url": url,
               "title": hit.get("title"), "fetched": datetime.now(UTC).isoformat(timespec="seconds"),
               "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()}
    _write(cache / f"{key}.txt", text)
    _write(cache / f"{key}.source.json", json.dumps(sidecar, indent=2) + "\n")
    return Fetched(Outcome.FETCHED, key, source, hit.get("title"))
