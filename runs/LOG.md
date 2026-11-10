# Run log

One entry per batch job the runner submitted, newest first: who asked and for what (the rows or the sweep it
serves), its inputs (the PMID list, the corpus revision), the commit it ran, its job id, and its result or its
failure with the cause. A fetch counts only once `uv run loci check quotes` passed on it; exit 4 (quotes that could
not be checked) is unknown, never a pass. A rerun that reuses texts already in the article cache says so here.

Timestamps are ISO-8601 UTC.

No jobs yet.
