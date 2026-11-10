# Curator — notes

The curator seat's working state, rewritten to the present before a reset (`docs/seats/CURATOR.md`).

## Now (2026-11-10)

- First locus done by hand: 46 LPA, tier A kept (060c9bd). Shown to the lead in `#longevity-loci > formats`
  (639271230) with six format questions: a cite for a database release (Open Targets, gnomAD), nominal replication
  read as `not_significant`, no design for "cases aged 90+", file names for seed loci whose names hold `/`,
  spaces or nothing (81, 103, ~30 more), duplicate seed loci (IL6R 8/157, HTT 25/158, TERT 132/133/153), and
  whether rows get a changelog line. None blocks the plain loci; 81 and 103 wait on the file-name answer.
- The lead's format answers landed (e466070, 06423f1, a970b44) and 46-LPA moved onto them (04cc507): a db note
  for Open Targets 26.09, Deelen's column nominal. Waiting on the person, through the lead: whether a replication
  look-up with P and direction but no effect size may support (§6.3); until then CHARGE-EU 90+ stays
  not_significant with the reason in its statistical_test. Also with the person: the duplicate seed loci
  (8/157, 25/158, 132/133/153), skipped until answered. Rows get no changelog line.
- The five-row pilot is running (below): 93 LDLR, 80 CHRNB4 and 57 CDKN2B-AS1 done; 71 ATXN2, 67 TTC12 next, then pause.
- The scout's queue: pmid-42928374 (FURIN, pleiotropy with mental disorders) waits for locus 81; read it then.

## Pilot (five rows, from 2026-11-10)

The person's word through the lead (639290086): five new rows in PROGRESS order, one commit and a `done:` each, what
breaks written here as it happens, then a pause. 46-LPA's CHARGE-EU 90+ moved to nominal under D13 first (4813c8a).

What broke, by row:

- 93 LDLR
  - Wright 2019's Table 3 (AncestryDNA, the one sample outside UK Biobank and LifeGen) prints P and a z-score effect
    but no effect allele. The alleles are in a figshare supplement only: Europe PMC lists no supplementary file and
    the plugin's `list_supplementary` answers `not_determinable` for G3 (DOI prefix 10.1534). Found by figshare's
    API, read with `fetch_supplementary` and a stdlib xlsx reader (no openpyxl in the environment).
  - The cache holds an article's text only, so supplement values cannot be quoted or checked: they sit in the note
    as prose under a `supplement` reading, and the study quotes the main-text table row.
  - Wright's Supplemental Tables 8 and 9 give opposite allele labels for one beta (S9's `effect_allele_anc` is the
    other allele); S8 agrees with the main text. This sets the direction at CHRNA3/5, ANRIL and ATXN2 too.
  - Wright's supplement writes rs6511720's allele as A, the reverse strand of a G/T SNP: kept as printed, said in
    `effect_unit`.
  - Wright's arm is a linear regression of parents' lifespan, not a Cox model; `study_design` has no other parental
    design, so `parental_lifespan_cox` with the difference in `statistical_test`. Its effect is a z-score, written as
    `beta`.
  - Wright's meta-analysis (genome-wide significant) contains UK Biobank and prints no allele or pooled effect: not a
    study row, cited from the tier only.
  - Mine: Open Targets lists 1,000+ credible sets per LDLR variant, so filtering the first page missed Timmers
    2020's set; query by study instead (`study(studyId){credibleSets}`), corrected before the commit.

- 80 CHRNB4
  - The new `ungrained` warning (a study's quote names neither its rsid nor its gene) does not look at
    `proxy_rsid`: a quote naming the proxy the study reported still warns. Joshi 2017's Table 2 rows warn by design:
    the flattened table puts the rsid and gene on lines above the cell row, so the row quote names neither, and a
    second quote (q6) binds the rsid.
  - The seed names the locus CHRNB4; every paper says CHRNA3/5. `gene` is the effector call, and at E3 (L2G CHRNA5
    0.29) one name overclaims: written `CHRNA5/CHRNA3`.
  - The outcome cells cannot say "tested genome-wide, no estimate read" (Zenin's healthspan GWAS has no credible
    set here): written `untested`, with the reason in the verdict.
  - Exceptional survival is mixed: parents both in the top 10% significant (Pilling, UK Biobank), own survival past
    90 null (CHARGE-EU 90+, P 0.95). One cell holds one sign: `+`, the null kept as a study and said in the verdict.

- 57 CDKN2B-AS1
  - Deelen 2019's Supplementary Data 1 is the per-variant look-up of every published lifespan locus in a sample
    with no UK Biobank data (OR and P at the 90th and 99th percentile), and it decides replication at ATXN2 and ZW10
    too. Like Wright's, it can only sit in a note as prose: a study row needs a quote or a `quote_absent` kind, and
    none of the four kinds says "in the supplement, which the cache cannot hold". Its sheet title and column header
    also disagree on the 90th percentile's controls (dead against all).
  - My error, corrected (9a24449): I had read Deelen's 928 UK Biobank cases as part of its discovery. They are
    validation only.
  - Coronary artery disease's EFO id (EFO_0001645) is obsolete, replaced by MONDO_0005010, and the `mediator:`
    token takes `EFO_` only: no mediator flag on this row.
  - The requirements give trade-off loci "no actionability label", but the format requires one: `descriptive`
    written as the nearest.
  - §6.2 says a locus label goes in `phenotype` at E3 or E4, and does not say what `gene` then holds: written as the
    top L2G gene (CDKN2B), the label "9p21 heart disease region" in `phenotype`.

## How a locus goes (what the first one taught)

- `uv run loci fetch PMID…` for a handful of papers; a batch goes to the runner seat with the PMIDs and the rows.
- The parental-lifespan GWAS (Joshi 2017, Pilling 2017, Timmers 2019) share UK Biobank and LifeGen, and Timmers
  2020 combines them with Zenin and Deelen: none replicates another. Tier A needs a look-up in a sample outside
  them (CHARGE-EU 90+ in Joshi 2017 Table 2; Deelen 2019's discovery cohorts, which hold no UK Biobank
  data: its UK Biobank set, 928 cases at the 99th percentile, is validation only; overlap with LifeGen not stated).
  Corrected 2026-11-10: the 928 had been read as part of Deelen's discovery, and 93-LDLR's verdict said so.
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
