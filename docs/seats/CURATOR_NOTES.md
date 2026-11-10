# Curator — notes

The curator seat's working state, rewritten to the present before a reset (`docs/seats/CURATOR.md`).

## Now (2026-11-10)

- First locus done by hand: 46 LPA, tier A kept (060c9bd). Shown to the lead in `#longevity-loci > formats`
  (639271230) with six format questions: a cite for a database release (Open Targets, gnomAD), nominal replication
  read as `not_significant`, no design for "cases aged 90+", file names for seed loci whose names hold `/`,
  spaces or nothing (81, 103, ~30 more), duplicate seed loci (IL6R 8/157, HTT 25/158, TERT 132/133/153), and
  whether rows get a changelog line. None blocks the plain loci; 81 and 103 wait on the file-name answer.
- The lead's answers (639271512), its commit pending: a `corpus/db-<source>-<release>.md` note per database
  release; `stat_significance: nominal` (1e-5 to 0.05) supports; `age_threshold_case_control`; a file name is the
  seed name with each run outside `[A-Za-z0-9._-]` made `_`, an unnamed locus `<id>.yaml`; the duplicate seed loci
  go to the person, skipped until then; rows get no changelog line (`rows/PROGRESS.md` is the ledger). When it
  lands: move 46-LPA onto it (two nominal studies, the CHARGE design, a db note for Open Targets 26.09 and gnomAD).
- Next, unattended, by `rows/PROGRESS.md`: 93 LDLR, 80 CHRNB4, 57 CDKN2B-AS1, 71 ATXN2, 67 TTC12.
- The scout's queue: pmid-42928374 (FURIN, pleiotropy with mental disorders) waits for locus 81; read it then.

## How a locus goes (what the first one taught)

- `uv run loci fetch PMID…` for a handful of papers; a batch goes to the runner seat with the PMIDs and the rows.
- The parental-lifespan GWAS (Joshi 2017, Pilling 2017, Timmers 2019) share UK Biobank and LifeGen, and Timmers
  2020 combines them with Zenin and Deelen: none replicates another. Tier A needs a look-up in a sample outside
  them (CHARGE-EU 90+ in Joshi 2017 Table 2; Deelen 2019 cohorts, which include 928 UK Biobank cases).
- Effect sign conventions: Timmers years (+ longer), Joshi HR per a1 (> 1 shorter), Pilling Martingale (+ shorter),
  Zenin healthspan hazard (+ worse), Timmers 2020 −logHR and log-odds (+ better).
- Age bands and per-SNP replication of Timmers 2019 are eLife source-data supplements the cache does not hold.
- Every EFO id checked in OLS before it is written (EFO_0007796 parental longevity, EFO_0006925 lipoprotein A
  measurement).

## First seating (handout), what became of each item

1. Tools vs the kit: this seat had none of its own before the kit; the `loci` CLI is the lead's and kept.
2. Picture: a heron filing index cards, drawn by agents-kit/tooling (the admin seat is retired, #295), set.
3. Watchers: `watch.desk` and `watch.queue` started; `watch.brief` had not reported at punch-in.
4. Shared-channel backlog from before this account: read as information only.
5. First work: leak gate on in this clone (checked); PROGRESS.md written; the first locus done; §11's decisions
   mapped to the loci they block, none asked.
