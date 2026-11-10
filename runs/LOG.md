# Run log

One entry per batch job the runner submitted, newest first: who asked and for what (the rows or the sweep it
serves), its inputs (the PMID list, the corpus revision), the commit it ran, its job id, and its result or its
failure with the cause. A fetch counts only once `uv run loci check quotes` passed on it; exit 4 (quotes that could
not be checked) is unknown, never a pass. A rerun that reuses texts already in the article cache says so here.

Timestamps are ISO-8601 UTC.

## 6428266 ll-fetch-supp-zenin: completed, delivered, not yet counted

- **Asked by** the curator, 2026-11-10 (Zulip 639311757), for every seed locus: Zenin 2019's healthspan summary
  statistics fetched once, filtered to the seed's rsIDs.
- **Inputs:** `loci fetch-supp pmid-30729179 zenodo:1302861 --rows '\b(rs…)\b'`, the regex from the 228 unique
  rsIDs of `docs/longevitymap_v2/data/seed_variants.csv`, sorted. The deposit holds one file,
  `healthspan_summary.csv.gz` (236,731,248 bytes), so no `--only`. Nothing reused from the cache.
- **Ran:** 686bd9d, `scripts/ll-fetch-supp.sbatch`, 2 cores, lab account, submitted 2026-11-10T23:52Z.
- **Result:** COMPLETED, exit 0, 72 s, 367 MB peak memory, 2026-11-10T23:54Z. The cache file is
  `pmid-30729179.supp-healthspan_summary.csv.gz.rows-1102aade.txt`: the header and 190 data lines. They cover 189
  of the 228 seed rsIDs and no rsID outside the seed. `rs2440012` has two lines (alleles A and G against C), so a row
  that uses it has to pick its allele. The other 39 seed rsIDs are not in the deposit: rs2227341, rs2260227, rs3830412, rs6543176, rs7039467, rs7754015, rs8192284, rs12189947, rs35257605, rs35262860, rs41419545, rs59633341, rs73538174, rs75526165, rs75571981, rs75737809, rs76612380, rs76888380, rs77184423, rs77546126, rs79645902, rs112262188, rs114658003, rs116257533, rs117082375, rs117530284, rs117898573, rs138499810, rs138762279, rs145265196, rs147730555, rs184517867, rs189871470, rs199607933, rs199678370, rs200818241, rs373800184, rs528161076, rs1732444170.
- **Gate:** not passed yet. No note quotes this file so far, so `loci check quotes` has nothing of it to check. The
  run after the job exited 4: 66 quotes located and 32 unknown, all of them in the two database notes
  (`db-gwascatalog-2025.01.09`, `db-opentargets-26.09`), which have no text in the cache. Those are not part of this
  fetch. The fetch counts once a note that quotes this file passes the check.
