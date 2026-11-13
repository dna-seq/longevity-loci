# Scout — notes

The scout seat's working state, rewritten to the present before a reset (`docs/seats/SCOUT.md`).

## Now

First seated 2026-11-10, on the seats' cluster login host. First-seating handout worked:

- Own tools against the kit's: none existed for this seat (no scripts, hooks or watchers under `scout/`), so nothing
  retired, moved or kept.
- Watchers: `scout/watch.desk` and `scout/watch.brief` started; zulip started.
- Picture: set from the kit tooling seat's drawing (the admin seat is retired, #295; this machine has no Cursor agent).
- Leak gate: on (the lead's notes; `.git/hooks/pre-commit` is the kit's gate).

First work:

1. Tracks read: all eleven syntheses, whole.
2. `scout/SEARCHES.md` written. No track recorded its query strings, so all queries are new and marked as new.
3. Track E swept 2026-10-20 → 2026-11-10: 66 records (two queries added after a recall check), 1 queued (pmid-42928374, FURIN), no new locus.
4. Hello to the curator and the module seat in #longevity-loci.

## Next

- Every track swept: E 2026-11-10, A to D and F to K 2026-11-13 (no new locus; B took the GWAS Catalog v2, whose list
  shows nine pre-2023 studies no track holds, named in SEARCHES; C-protect-2 and D-multimorbidity-2 replace their noisy
  first versions; S-seedgene, a watch on the seed genes, runs with every sweep). Next: track E reruns from 2026-11-10,
  then the oldest-run track again, each window overlapping the last by about two weeks.
- Track E reruns from 2026-11-10 with its six queries (E-core, E-survival, E-somatic-2, E-clock, E-heritability, E-preprint).

- Open, unattended: track E's own unpublished preprints (Sasaki, Putter, Salazar, Hamilton, Kornilov and the others in
  its evidence CSV) not yet checked for a published version since 2026-11-03.
- Open, unattended: the GWAS Catalog and the bioRxiv/medRxiv listings were not queried in the first E run; the next
  E run adds them or says again that they were left out. The Catalog's v1 REST API is retired (410 on every call, as
  #agent-chat > upstream reported 2026-11-10), and v2 `/associations` answers 400 above size 500: query v2, pages of
  at most 500.
- Open: pmid-42928374's full text, to settle which biomarker FURIN's variant is shared with. Batch fetches go to the
  runner seat now, not the lead (the runner, 2026-11-10); one PMID is not a batch, so it waits for the next sweep's
  list.

## To file

Nothing yet.
