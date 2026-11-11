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
- The compaction test ran (2026-11-11, 23:28Z): the session came back holding the seat and knowing the pilot;
  nothing woke it afterwards, so the lead wakes it after each row until kit #409 lands. Reported as 639308908.
- **Ten-row run** (the person via the lead, 639308791 and 639308811), from 6 CELSR2. Per row: commit, `done: <row>;
  compacting` to the lead, `watchdog.sh compact`, end the turn; the lead wakes the next. Stop at 80 % of the 7-day
  window or 95 % of the 5-hour window. After each tenth `done:`, re-measure the pacing and
  go on with the next ten, unless blocked or steered (the person, 2026-11-11, via the lead, 639316091: "After 10
  adjust pacing and go next 10 and so on unless blocked or I steer"; this replaces the earlier pause after ten). Rows done in this run: 6 CELSR2 (1 of 10); the corrections of 71 (d44fd4a) and 67 done; the E3 gene rule at 57 and 80 next, then 38 HLA-DQA1 by PROGRESS.
- **Before the next locus: the lead's corrections to 71 and 67**, one commit per row, from its handout (kept at
  `~/.local/state/agent-seat-blueprints/handouts/session-44d9cb42-a3f8-47e0-b7ab-a8dbd8338890/delivered/20261110T234346Z-review-71-67.md`;
  read it whole). In short: B stands at both because a powered non-replication in an independent sample
  (AncestryDNA) is red-flag heterogeneity, the lead's rule for both; rewrite each verdict_reason to that; Wright's
  studies become `parental_lifespan_linear`, quoted heterogeneity; 71: Pilling's proxy C is the risk allele
  (`direction: risk`), healthspan 0 from Zenin's SD15 quoted, autoimmune/CVD direction words quoted or dropped,
  per-copy parental months; 67: settle the E3 gene rule with the advisor (then apply at 57 too), age UNKNOWN or
  INFERRED, Pilling's fathers N about 415000, unquoted values quoted from the cached supplements or moved to prose,
  "parents" not "fathers".
- Tools: `uv run loci fetch-supp KEY LOCATOR` caches a supplement as text (RM4; quotable under a `supplement`
  reading); since 78c7675 it reads a `.gz` with `--rows REGEX`; before that 6's healthspan was left on a db note,
  `db-gwascatalog-2025.01.09`, read with the scratch `tbx.py URL.gz CHR START END RSID...` (a remote tabix
  region read). Open Targets' lifespan sets at a locus: `ot.py VARIANT` lists every set the variant is in; filter
  by trait (the four-study `otstudy.py` misses Pilling's fathers GCST006701 and Wright's GCST009450).
- **71 corrected** (2026-11-11), the lead's review applied. Tier B on red-flag heterogeneity alone: replication is
  met (LifeGen without UK Biobank, Timmers' Figure 2 source data, now cached as `pmid-30642433` q12/q14; Deelen's
  SD1 look-ups q9-q11), and AncestryDNA's powered null (heterogeneity P 2.6e-3, Wright S9 q17/q18) caps it. Rule,
  the lead's, for every row: **a powered non-replication in an independent sample is red-flag heterogeneity and
  caps the row at B.** Healthspan 0 now from Zenin SD15 (`pmid-30729179#q4`, fetched from Springer's ESM URL);
  autoimmune direction from Joshi q11 (rs3184504-T raises type 1 diabetes); cancer trade-off from Timmers q7, no
  "slightly"; per copy, parents about 1.7 months ("nearly two months"). Deelen and LifeGen share the Rotterdam
  Study (Timmers q13). eLife source data is at `https://cdn.elifesciences.org/articles/39856/elife-39856-figN-dataM-v2.xlsx`.
- **67 corrected** (2026-11-11), the lead's review applied. Tier B on red-flag heterogeneity alone: replication
  met (LifeGen fathers without UK Biobank, Timmers q15, P 0.016; Deelen SD1 q12, 90th OR 1.068, P 0.011), and
  AncestryDNA's null (Wright q11/q20, P 0.81, heterogeneity P 2.97e-4) caps it. New studies: the LifeGen replication;
  Deelen's own 90th/99th look-ups (replacing Timmers 2020's tabulation of the 90th); Wright's arm is now
  `parental_lifespan_linear`, N 309383, beta 0.0007895 with no allele (S9's allele column prints the other allele
  at 6 and 71; S8 has no row), no direction. Pilling's fathers' N left empty: Table 1's counts are not in the cached
  text. Age UNKNOWN. "parents" in the conclusions.
- **The E3/E4 gene rule** (the advisor's read, settled by the requirements: line 65 "name a gene only at effector
  confidence E1/E2"; line 305 "A locus label goes in `phenotype` when the gene is E3/E4"): at E3/E4 `gene` is ""
  and the candidates go into verdict_reason. Tested: `gene: ""` passes `loci check rows`, and the module's
  `variants.csv` has `gene` optional. Applies to 67 (done), 57 (CDKN2B) and 80 (CHRNA5/CHRNA3), each its own commit.
- Format gap, for the lead: a `multivariate_healthspan_lifespan` study (Timmers 2020's MANOVA) has no effect size,
  and §6.3's check requires effect_size and effect_measure on every study supporting tier A/B, so 67 carries no
  multivariate study; its P 4e-10 is in the verdict prose only.
- Zenin's healthspan summary statistics for all 228 seed rsIDs are cached (runner job 6428266):
  `pmid-30729179.supp-healthspan_summary.csv.gz.rows-1102aade.txt`, 189 of 228 found. 6's db-gwascatalog cite can
  move to it when 6 is next touched.
- Rules settled on 6: a seed lead that sits in a lifespan credible set stays the lead even when no study reports
  it; a Bayes-factor P (Timmers' iGWAS) is never the study's P; age with no locus-own age bands is UNKNOWN.
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
  - Exceptional survival was mixed: parents both in the top 10% significant (Pilling, UK Biobank), own survival past
    90 null (CHARGE-EU 90+, P 0.95). First written `+`; moved to `0` once Deelen's supplement showed the 90th and
    99th percentiles null too (P 0.40, 0.58), three samples outside UK Biobank against one inside.

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

- 71 ATXN2
  - The first tier set below the seed's: B, not A. Outside UK Biobank and LifeGen, AncestryDNA's fathers show a
    quarter of the UK effect (P 0.10, heterogeneity P 2.6e-3) and Deelen's percentiles are nominal only. A judgement
    the lead and the person should see.
  - Deelen's two nominal look-ups are the row's only supporting studies outside UK Biobank, and their allele, OR and
    P exist only in Supplementary Data 1. Written as study rows quoting the main-text sentence that names ATXN2/BRAP
    among the nominal loci, with the values' source in `statistical_test`. The quote supports the claim; the numbers
    are unchecked. The cleaner fix is a supplement reading the cache can hold (the plugin reads xlsx; the cache
    could take a text rendering keyed `<key>.supp<N>.txt`): the lead's call.
  - Timmers 2019's credible set here spans about 1 Mb (21 members, to PTPN11), so its L2G (SH2B3 0.41) is diluted;
    the tighter sets of Timmers 2020 and Pilling give SH2B3 0.95. Cited from the tighter set.

- 67 TTC12
  - Tier B, the second below the seed: genome-wide only in Pilling's fathers and Timmers 2020's multivariate test;
    LifeGen's fathers replicate (no value in the text), AncestryDNA is null.
  - Timmers 2020's multivariate P (MANOVA) has no effect size, so the one genome-wide result that pools the three
    traits cannot be a supporting study; Timmers 2019's LifeGen-fathers replication has no value in the text (source
    data), so it is cited from the tier only.
  - `gene` at E3 again: the top L2G gene, CLDN25 at 0.35, reads oddly beside a locus the papers call ZW10 and the
    seed TTC12. The rule for `gene` below E2 wants deciding.
  - Pilling's single-parent analyses print no N; `sample_size` left empty.

Across the five: three kept at A (LDLR, CHRNA3/5, CDKN2B-AS1), two moved to B (ATXN2, ZW10). The deciding evidence
each time was a sample outside UK Biobank and LifeGen, and for four of the five its numbers sit in a supplement
(Wright's, Deelen's, Zenin's) the cache cannot hold. Not consistent yet: Deelen's supplement look-ups are study rows
at 71 and prose only at 93, 57, 67 and 80; to be made one way once the lead rules on supplements.

After the fifth row, the advisor's read (correction commit): mediator directions in conclusions that no quote
carried were softened (LDL at 93, smoking at 80, blood pressure and autoimmunity at 71); 71's healthspan went from
untested to 0 on Zenin's own look-up (its Supplementary Data 15); each row now says what became of the seed's other
rsIDs; 57's age cites dropped the Timmers 2019 decline it does not rest on. `loci check` reads none of these.
Rosoff 2023 (pmid-37550455, mvAge), cited by the seed at all five, was fetched and has no note: its text names no
pilot lead (values in its supplement), so it is unread for these rows.

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
