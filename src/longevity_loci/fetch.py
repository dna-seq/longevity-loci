"""The article cache: an article's text fetched from Europe PMC into `$LOCI_CACHE/<key>.txt`, with a sidecar
`<key>.source.json` saying what was fetched (the open-access full text, or the abstract only) and when.

The text is the article's, not ours: it stays in the cache, never in the repository, a message or an issue."""

from __future__ import annotations

import html
import json
import logging
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


class Source(StrEnum):
    FULL_TEXT = "full_text"
    ABSTRACT = "abstract"


class Outcome(StrEnum):
    FETCHED = "fetched"
    NOT_FOUND = "not_found"  # Europe PMC holds no record of the PMID
    NO_TEXT = "no_text"  # a record, with neither an open full text nor an abstract
    UNREACHABLE = "unreachable"  # the service did not answer: retryable, says nothing of the article


@dataclass(frozen=True)
class Fetched:
    outcome: Outcome
    key: str
    source: Source | None = None
    title: str | None = None
    detail: str = ""

    def __bool__(self) -> bool:
        return self.outcome is Outcome.FETCHED


def jats_to_text(xml: str) -> str:
    """JATS as plain text: a table cell ends in a tab, a row, paragraph, title or section in a line break."""
    xml = re.sub(r"<(ref-list|back)\b.*?</\1>", "", xml, flags=re.S)
    xml = re.sub(r"</(td|th)>", "\t", xml)
    xml = re.sub(r"</(tr|p|title|sec|caption|label)>", "\n", xml)
    return html.unescape(re.sub(r"<[^>]+>", "", xml))


def _get(url: str, timeout: float) -> bytes:
    with urllib.request.urlopen(url, timeout=timeout) as r:
        return r.read()


def fetch(pmid: int, cache: Path, timeout: float = 60) -> Fetched:
    """Fetch one article's text into the cache; the open full text when Europe PMC has one, else the abstract."""
    key = f"pmid-{pmid}"
    try:
        hits = json.loads(_get(SEARCH.format(pmid=pmid), timeout))["resultList"]["result"]
    except (urllib.error.URLError, TimeoutError) as e:
        return Fetched(Outcome.UNREACHABLE, key, detail=str(e))
    if not hits:
        return Fetched(Outcome.NOT_FOUND, key)
    hit = hits[0]
    text, source, url = None, None, None
    pmcid = hit.get("pmcid")
    if pmcid and hit.get("isOpenAccess") == "Y":
        url = FULLTEXT.format(pmcid=pmcid)
        try:
            text, source = jats_to_text(_get(url, timeout).decode("utf-8")), Source.FULL_TEXT
        except urllib.error.HTTPError as e:
            log.info("%s: no full text from %s (%s); the abstract instead", key, pmcid, e.code)
        except (urllib.error.URLError, TimeoutError) as e:
            return Fetched(Outcome.UNREACHABLE, key, detail=str(e))
    if text is None and hit.get("abstractText"):
        text, source, url = html.unescape(re.sub(r"<[^>]+>", "", hit["abstractText"])), Source.ABSTRACT, SEARCH.format(pmid=pmid)
    if text is None:
        return Fetched(Outcome.NO_TEXT, key, title=hit.get("title"))
    (cache / f"{key}.txt").write_text(text, encoding="utf-8")
    sidecar = {"key": key, "pmid": pmid, "pmcid": pmcid, "source": source.value, "url": url,
               "title": hit.get("title"), "fetched": datetime.now(UTC).isoformat(timespec="seconds")}
    (cache / f"{key}.source.json").write_text(json.dumps(sidecar, indent=2) + "\n", encoding="utf-8")
    return Fetched(Outcome.FETCHED, key, source, hit.get("title"))
