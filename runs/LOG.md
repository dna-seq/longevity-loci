# Run log

One entry per batch job the runner submitted, newest first: who asked and for what (the rows or the sweep it
serves), its inputs (the PMID list, the corpus revision), the commit it ran, its job id, and its result or its
failure with the cause. A fetch counts only once `uv run loci check quotes` passed on it; exit 4 (quotes that could
not be checked) is unknown, never a pass. A rerun that reuses texts already in the article cache says so here.

Timestamps are ISO-8601 UTC.

## 6428266 ll-fetch-supp-zenin: running

- **Asked by** the curator, 2026-11-10 (Zulip 639311757), for every seed locus: Zenin 2019's healthspan summary
  statistics fetched once, filtered to the seed's rsIDs.
- **Inputs:** `loci fetch-supp pmid-30729179 zenodo:1302861 --rows '\b(rs…)\b'`, the regex from the 228 unique
  rsIDs of `docs/longevitymap_v2/data/seed_variants.csv`, sorted. The deposit holds one file,
  `healthspan_summary.csv.gz` (236,731,248 bytes), so no `--only`. Nothing reused from the cache.
- **Ran:** 686bd9d, `scripts/ll-fetch-supp.sbatch`, 2 cores, lab account, submitted 2026-11-10T23:52Z.
- **Result:** pending.
