# Scout — notes

The scout seat's whole working state, rewritten 2026-11-16 before the seats move to another chat organisation (the
person: "Make sure they commit all to notes, transcripts are not moving"). A fresh session carries on from this file,
`docs/seats/SCOUT.md` (the priming), `scout/SEARCHES.md` (every query, window and recall) and `scout/screened.md`
(every record read, with its verdict).

## In hand

Nothing is half run. Every sweep so far is committed and pushed (last scout commits 06b9d98 and d8e0a08, 2026-11-16).

## State of the work

- **Queue (`scout/queue.md`): no open entry.** The eight second-signal candidates (D25.6) were all taken by the
  curator as rows 162 to 169 under D39.14 (`second_signal_of`); each entry has a **Taken** line naming its row.
  pmid-42928374 (Pisanu 2026, FURIN at 81) is **Closed** with the curator's line (7741c02): its shared variant is with
  telomere length, not mvAge. Tiers of 162 to 169 were revised by the lead's batch-seventeen read (D40); the Taken
  lines say the tier at filing only, the rows say the current one.
- **Every seed locus has a row** (the curator, 2026-11-16, dashboard `--left` 0). So the scout's sweeps are now the
  only source of new work for the curator: a new paper on a row, or a second signal at a seed locus (D25.6).
- **Track E** (2025–2026 papers and preprints): swept 2026-11-10 (window 2026-10-20 → 2026-11-10) and rerun
  2026-11-14 (window 2026-10-27 → 2026-11-14): 14 new records, nothing queued; GWAS Catalog v2 queried, no new study.
- **Tracks A to D and F to K**: swept 2026-11-13 (window 2026-10-20 → 2026-11-13), no new locus. C-protect-2 and
  D-multimorbidity-2 replace their noisy first versions; S-seedgene (a watch on the seed genes) runs with every sweep.

## Next, in order

1. **Second pass over A to D and F to K, with S-seedgene**, `unattended`, waits until 2026-11-17 (UTC): window from
   2026-10-30 (about two weeks' overlap with the last) to the run date; same queries as in SEARCHES, a row per query
   in each track's Runs table, new records into `screened.md`, recall unchanged unless a query changes (a changed
   query is a new line with its reason).
2. **Next track E run** after that: rerun from about 2026-10-31; look for PPR1366192's full text or published version
   (cognitive superagers' exome, rare HLA-B and HLA-DRB1 missense, no variant named); check the twelve unpublished
   preprints again for a published version (Chang's is PMID 42987714, found 2026-11-14); read Alvarez Sirvent 2026
   (v2) and Salazar (v3), newer versions not yet read.
3. Open, `unattended`: bioRxiv's and medRxiv's own listings, left out of both E runs (Europe PMC's preprint index
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

## Org move (2026-11-16)

- The lead (640874040): a ticket for this seat may arrive from genie's secretary; **leave it unread and do not run the
  org-move switch until the lead says the person has given the go.** A held-back embassy DM from that secretary,
  640873745, arrived the same evening and is left unread on that instruction; once handled, its description (secrets
  cut out) goes to `#embassy-review` as its line says.

## Learned

- Kit: a pending plugin reload never blocks work; right after one the watchdog may say it "holds no Zulip account":
  retry with `sleep 10`. The `nothing` button, a reaction or an ack closes the wake, not the turn.
- `git pull --ff-only origin main` can fail here with "Cannot fast-forward to multiple branches"; `git fetch origin
  main` then `git merge --ff-only origin/main` works.
- Commit by path (`git commit --only -- <paths>`), never `-A`; the leak gate refuses machine paths in a commit.
- Quota: stop at 95 % of the binding window with `watchdog.py wait-quota scout`; the repository's pace is full forward.
- Daily line in `#longevity-loci>daily` at the first turn of a new day when scout work landed since the last one
  (last posted 2026-11-15; the queue bookkeeping of 2026-11-16 is owed a line on 2026-11-17).

## To file

Nothing.

- 2026-11-17: moved to the chat organisation desk-antonkulaga (bin/org-move.py).
