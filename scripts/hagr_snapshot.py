"""Snapshot HAGR LongevityMap's live entry pages (entry.php?id=1..N) into one CSV, to compare the live database
with Build 3's download and with v1's sqlite. An id past the last real entry returns an empty template, so an
entry is real only when its Identifier field is filled. Polite: three workers, a pause between requests.

    uv run python scripts/hagr_snapshot.py OUT.csv --last 3476
"""

from __future__ import annotations

import csv
import html
import logging
import re
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import typer

URL = "https://genomics.senescence.info/longevity/entry.php?id={i}"
FIELDS = ["Longevity Association", "Population", "Study Design", "Conclusions", "Identifier", "HGNC symbol",
          "Cytogenetic Location", "Gender", "Reference", "PubMed"]
log = logging.getLogger("hagr_snapshot")


def fetch(i: int) -> dict[str, str]:
    for attempt in range(3):
        try:
            with urllib.request.urlopen(URL.format(i=i), timeout=40) as r:
                text = r.read().decode("utf-8", errors="replace")
            break
        except (urllib.error.URLError, TimeoutError) as e:
            err = str(e)
            time.sleep(3 * (attempt + 1))
    else:
        return {"id": str(i), "status": f"fetch_error: {err}"}
    text = re.sub(r"<script.*?</script>", "", text, flags=re.S)
    # a tag opens with a letter, / or !: a "<70" in the text is not one
    parts = [p for p in (html.unescape(x).strip() for x in re.split(r"<[A-Za-z/!][^>]*>", text)) if p]
    rec = {"id": str(i)}
    for f in FIELDS:
        if f in parts:
            k = parts.index(f)
            nxt = parts[k + 1] if k + 1 < len(parts) else ""
            rec[f] = "" if nxt in FIELDS else nxt
    rec["pmids"] = ";".join(sorted(set(re.findall(r"pubmed[^\"']*?(\d{6,9})", text, flags=re.I)), key=int))
    rec["status"] = "entry" if rec.get("Identifier") else "empty"
    time.sleep(0.3)
    return rec


def main(out: Path, last: int = typer.Option(..., help="the last id to read"), workers: int = 3) -> None:
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(message)s")
    with ThreadPoolExecutor(workers) as ex:
        rows = list(ex.map(fetch, range(1, last + 1)))
    cols = ["id", "status", *FIELDS, "pmids"]
    with out.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        w.writerows(rows)
    counts: dict[str, int] = {}
    for r in rows:
        key = r["status"].split(":")[0]
        counts[key] = counts.get(key, 0) + 1
    log.info("wrote %s: %s", out, counts)


if __name__ == "__main__":
    typer.run(main)
