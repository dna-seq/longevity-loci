# Scout — notes

The scout seat's whole working state, rewritten 2026-11-16 before the seats move to another chat organisation (the
person: "Make sure they commit all to notes, transcripts are not moving"). A fresh session carries on from this file,
`docs/seats/SCOUT.md` (the priming), `scout/SEARCHES.md` (every query, window and recall) and `scout/screened.md`
(every record read, with its verdict).

## In hand

- **Backfill sweep, 2023-01-01 → 2026-10-20** (the lead, #longevity-loci>scout 641384225, for the person; decided,
  `urgent`, started 2026-11-17): every current query (E set, A–D, F–K, S-seedgene), Europe PMC preprints over the same
  window, bioRxiv's and medRxiv's own listings from 2026-04. Queue (a) any genome-wide lifespan, longevity, healthspan
  or age-at-death locus not a seed locus, (b) any paper on an existing row that no row cites. Also a one-line verdict on
  the nine pre-2023 GWAS Catalog ids and on Atanur 2026 (pmid 42880286). Reply there with records, new, queued.
  Widened by the person (lead, 641384713) to **2015-01-01 → 2026-10-20**, counts per window (2015-01-01 → 2017-06-24,
  2017-06-25 → 2022-12-31, 2023-01-01 → 2026-10-20). State 2026-11-17: fetched (26,979 PubMed hits, 21,127 distinct,
  20,823 not already screened or cited; 1,632 new Europe PMC preprints); abstracts classified by rule (human, a
  longevity or ageing-marker term, a genetic design, a row rsID or gene); 2,743 flagged records out to reader agents at
  abstract level and 2,770 longevity-genetic records at title level; the rest dropped by rule, counted by reason.
  The nine Catalog ids: no genome-wide lifespan association under the four EFO terms (Lunetta 2007's one line at
  1e-8 is age at menopause). Atanur 2026: abstract silent on age at death, Catalog study with no association: unknown.
  If the scratch is lost, rerun from the queries in SEARCHES.md; nothing committed rests on it yet.

## State of the work

- **Queue (`scout/queue.md`): no open entry.** Alvarez Sirvent 2026 (HLA-II fine-mapping, a preprint, Europe PMC
  PPR1306907), queued 2026-11-17 for rows 135 and 38, was closed by the curator the same day at abstract depth (0b389c2).
  The eight second-signal candidates (D25.6) were all taken by the
  curator as rows 162 to 169 under D39.14 (`second_signal_of`); each entry has a **Taken** line naming its row.
  pmid-42928374 (Pisanu 2026, FURIN at 81) is **Closed** with the curator's line (7741c02): its shared variant is with
  telomere length, not mvAge. Tiers of 162 to 169 were revised by the lead's batch-seventeen read (D40); the Taken
  lines say the tier at filing only, the rows say the current one.
- **Every seed locus has a row** (the curator, 2026-11-16, dashboard `--left` 0). So the scout's sweeps are now the
  only source of new work for the curator: a new paper on a row, or a second signal at a seed locus (D25.6).
- **Track E** (2025–2026 papers and preprints): swept 2026-11-10, rerun 2026-11-14 and 2026-11-17 (window 2026-10-31 →
  2026-11-17: 8 new records; the preprint version check queued Alvarez Sirvent 2026 v2 for row 135).
- **Tracks A to D and F to K**: swept 2026-11-13 (window 2026-10-20 → 2026-11-13) and again 2026-11-17 (window
  2026-10-30 → 2026-11-17: 37 new records, nothing queued, the GWAS Catalog unchanged), no new locus. C-protect-2 and
  D-multimorbidity-2 replace their noisy first versions; S-seedgene (a watch on the seed genes) runs with every sweep.

## Next, in order

1. **Next track E run**, `unattended`, waits until about 2026-11-24, with the third pass over A to D and F to K (from
   about 2026-11-03). Look again for PPR1366192's published version (cognitive superagers' exome, HLA-B and HLA-DRB1
   missense, no variant named) and the twelve unpublished preprints' (Chang's is PMID 42987714). **Watch Alvarez Sirvent
   2026** (doi 10.64898/2026.08.24.26361177) for a published version or an open full text: then tell the curator, who
   re-reads rows 135 and 38.
2. Open, `unattended`: bioRxiv's and medRxiv's own listings, left out of every E run (Europe PMC's preprint index
   stood in). The bioRxiv API is `https://api.biorxiv.org/details/{server}/{interval}`.

## How a sweep is run (the scripts were scratch, not committed: rewrite them from this)

- **PubMed**: E-utilities `esearch` by entry date (`datetype=edat`, `mindate`, `maxdate`, `retmax=500`), sent by
  **POST**: S-seedgene and other long queries get 414 on GET. Then `esummary` for titles. Python via `uv run python`,
  `-I` for anything reading fetched files; every request through the proxy (env vars set in `~/.bashrc`).
- **Recall check**: each query ANDed with the track CSV's PMIDs as `(<pmid>[uid] OR …)` with no date limit, recorded
  as k of n. The CSVs are `docs/longevitymap_v2/evidence/*_evidence.csv` (never edited by the scout).
- **Europe PMC preprints**: `SRC:PPR AND FIRST_IDATE:[lo TO hi]`, cursorMark paging; a published version found by
  `TITLE:(...) NOT SRC:PPR`, Crossref's relation fields, and the bioRxiv API's `published` field.
- **GWAS Catalog**: REST **v2** only (v1 answers 410), `/studies?efo_id=` for EFO_0007796, OBA_VT0005372,
  EFO_0009762 and EFO_0005056, pages of at most 500; compare the PMIDs against all PMIDs already screened or cited.
- **Dedupe**: union the query outputs by PMID (and preprint id), drop those already in `screened.md`, then screen
  the rest at title or abstract level; one row per record with its verdict.
- A PMID is never taken from memory: only from a search result, its title checked.

## Waits on others

- Nothing. Full-text batch fetches go to the runner seat as a PMID list (the runner, 2026-11-10); none is owed.

## Org move

- 2026-11-17: the seats moved to the chat organisation desk-antonkulaga (the lead's commit acb4b4e); this seat is
  punched in there. The old organisation's held-back message (640873745) was never read and its
  ticket not used: the move came through another session's handoff.

## Learned

- Kit: a pending plugin reload never blocks work; right after one the watchdog may say it "holds no Zulip account":
  retry with `sleep 10`. The `nothing` button, a reaction or an ack closes the wake, not the turn.
- `git pull --ff-only origin main` can fail here with "Cannot fast-forward to multiple branches"; `git fetch origin
  main` then `git merge --ff-only origin/main` works.
- Commit by path (`git commit --only -- <paths>`), never `-A`; the leak gate refuses machine paths in a commit.
- Quota: stop at 95 % of the binding window with `watchdog.py wait-quota scout`; the repository's pace is full forward.
- Daily line in `#longevity-loci>daily` at the first turn of a new day when scout work landed since the last one
  (last posted 2026-11-17).

## To file

Nothing.
