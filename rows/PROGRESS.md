# Curation progress

The curator's order of work. Strongest evidence first: the tier-A loci decide what the scored core is and are
the ones a reader sees first, so they set the pattern every later row follows; the tiers below come in the order
their seed tier ranks them, and v1's remaining rsIDs last, since most of them land as legacy rows.

The seed tier is `docs/longevitymap_v2/data/seed_variants.csv`'s, read at each locus's lead (`is_locus_lead`): a
mechanical consensus of the research tracks, to be confirmed or overturned by the papers, never copied into a row.
161 loci: 11 A, 82 B, 39 C, 1 D, 4 X, 24 with no seed tier.

## Done

- 46 LPA (lead rs10455872), tier A kept: the first locus, by hand, shown to the lead as the format's first row.
- 93 LDLR (lead rs142158911), tier A kept: the pilot's first row.
- 80 CHRNB4 (lead rs8042849, the papers' CHRNA3/5), tier A kept: the pilot's second row.
- 57 CDKN2B-AS1 (lead rs1556516), tier A kept, a trade-off with its net direction resolved: the pilot's third row.
- 71 ATXN2 (lead rs11065979, the SH2B3 block), tier B (seed A): weak replication outside UK Biobank; a trade-off.
- 67 TTC12 (lead rs61905747, the papers' ZW10), tier B (seed A): genome-wide only in fathers; null in AncestryDNA.
- 6 CELSR2 (lead rs646776, the SORT1 lipid locus), tier A kept: Pilling 2017 replicated in AncestryDNA; the ten-row run's first.
- 38 HLA-DQA1 (lead rs34967069, the HLA class II region), tier B (seed A): genome-wide, no independent replication of its own (the AncestryDNA mothers' tag is shared with 103).
- 81 FES/FURIN (lead rs6224, Pilling's rs17514846 its proxy), tier A kept: replicated in LifeGen without UK Biobank; effector FES by L2G.
- 103 (lead rs1049053, Zenin 2019's HLA-DQB1 healthspan SNP), tier C (seed A): genome-wide in healthspan only, its replication failed (power about 0.8); its lifespan results are row 38's signal through LD (D17.1).
- 2 PABPC4 (lead rs3768321, Rosoff 2023's mvAge), tier C (seed B): genome-wide only in the multivariate factor; lifespan P 0.071, so it cannot score (D16); Wright's nearby mothers' SNP not a tag (CEU r² 0.09); Deelen null (P 0.052).
- 4 LINC02796 (lead rs2613508, the NEGR1 obesity locus), tier B kept: genome-wide only in mvAge, with a nominal lifespan study (P 5.3e-4) that lets it score (D16); effector NEGR1 by L2G; modifiable through weight (D18.2); Deelen's 90th percentile nominal (P 0.036, an mvAge input), so exceptional survival +.
- 5 FPGT / TNNI3K (lead rs146254978, a 2 % variant), tier B kept: genome-wide only in Pilling 2017's parents' age-at-death analysis (P 4.6e-8), the rare C protective; not in Open Targets (C4/E4, no gene).
- 7 MAGI3 (lead rs1230666, the PTPN22 autoimmune region), tier B kept: genome-wide only in Timmers 2019's million lives (P 6.4e-9), null in the longevity look-ups; C1 by PICS PIP 0.64, E3 (no gene).
- 8 IL6R Asp358Ala (lead rs2228145, with 157's rs8192284 folded in), tier C (seed B): nominal only at the variant (Timmers 0.0034, AncestryDNA fathers 0.0017 by genomic control, Zenin 0.017), WHI null; the seed's B was MR-only (R-TIER-4); the locus's lifespan peak is the suggestive rs4845625 (3.7e-6, r² 0.46), whose shadow the variant's signal may be; harmonised to C; a trade-off (atopy); E1 IL6R, C4 (D17.2).
- 10 RABGAP1L (lead rs10798302, rs16847402 the same signal at r² 0.53), tier C (seed B): suggestive at Wright 2019's own genomic-control P (1.5e-6; raw 1.7e-8) in its current-age GWAS (VIABILITY_AF, confirmation only), not the parental meta-analysis the seed names; Timmers P 0.19 same side; Deelen nominal at the weak proxy only; C4, no gene.
- 11 LINC01875 (lead rs6744653, the TMEM18 obesity locus), tier B kept (A's first criterion fails at the lead, D18.3), a trade-off (heel bone density): genome-wide only at proxies (rs66906321 in Timmers' summary statistics, 2.3e-8, unreported by the paper; mvAge 4e-8), replicated at a third SNP in AncestryDNA fathers (genomic-control P 2.2e-3); the lead itself 5.8e-8; C4, no gene.
- 12 KCNK3 (lead rs1275922), tier A (seed B), on §4.1's letter: genome-wide in Timmers 2019 (6.0e-9), replicated only by Deelen 2019's 90th percentile (P 0.013, same allele; 99th 0.089; Timmers' Figure 4 look-up 0.16); AncestryDNA's nearest SNP not a tag (CEU r² 0.06); the Rotterdam overlap and Figure 4's sources inside Deelen stated, A held by D19.1; descriptive (the A raises calcium-channel-blocker use, hypertension and BMI, not mainly weight); no trade-off; C2, E2 KCNK3.
- 13 PRKD3 (lead rs577106756, a 0.1 % intron variant), tier B kept: genome-wide only in Park 2025's men (own survival, P 3.2e-8; not in the whole cohort); FinnGen null the other way (P 0.55, power not stated); healthspan uninformative; mech:cancer from the authors' same-sample PheWAS; men only; C4/E4, no gene.
- 14 LINC01122 (lead rs980183, Rosoff 2023's mvAge), tier B kept: genome-wide only in mvAge (P 1.8e-9), with a nominal lifespan study (Timmers, A, P 2.3e-5) that lets it score (D16); Deelen null; the longer-life A lowers type 2 diabetes, glucose and BMI; descriptive; C2 at its floor (PIP 0.107), E4, no gene.

## In hand

A ten-row run, on the person's word (2026-11-11, via the lead, 639308811: "go with next 10 measurement on
andjusted scenario, remeasure"), from 6 CELSR2 in the order below: one commit, a `done:` and a compaction per row,
stopping at 80 % of the 7-day window. After each ten: the pacing re-measured, then the next ten, unless blocked or
steered (the person, 2026-11-11, via the lead, 639316091: "After 10 adjust pacing and go next 10 and so on unless
blocked or I steer").

## Next: seed tier A (11)

In this order, and why:

1. 46 LPA: one clear lead, three genotypes, no trade-off, a single anchor (Timmers 2019) with independent support.
2. 93 LDLR, 80 CHRNB4 (CHRNA3/5), 57 CDKN2B-AS1, 71 ATXN2 (SH2B3), 67 TTC12 (ZW10/USP28): the other
   parental-lifespan loci of Timmers 2019's Table 1; CDKN2B-AS1 and ATXN2 are trade-offs, and come after the
   plain loci have set the pattern.
3. 6 CELSR2, 38 HLA-DQA1: single-track "A" calls the requirements (§12) ask the curator to confirm.
4. 81 FES/FURIN, 103 (no name): the seed's name does not make a file name (a `/`; none at all); asked of the lead.
5. 96 APOE last: waits on D2 (a diplotype inside v2), and its proxies are `ld_proxy_of` under it.

## Then: seed tier B (82), C (39), D (1), X (4), untiered (24)

By `locus_id` within each tier, as the seed lists them. Known before reaching them:

- 8 `IL6R Asp358Ala` (rs2228145) and 157 `IL6R (p.Asp358Ala)` (rs8192284) name one variant (rs8192284 is merged
  into rs2228145 in dbSNP, to be checked at curation); 25 and 158 are both HTT; 132, 133 and 153 are all TERT.
  Two seed loci for one signal become one row under the lower id, the others in its `also_loci` (D14).
- Many seed names hold a space, a `/` or brackets (`PCSK9 R46L`, `5q33.3 (EBF1 region)`, `KL (KL-VS`, ...); 44, 75,
  110, 134, 154 have none. docs/FORMATS.md now settles their file names (each run outside `[A-Za-z0-9._-]` one `_`;
  an unnamed locus `<locus_id>.yaml`): 5's is `5-FPGT_TNNI3K.yaml`.

## Last: v1's remaining rsIDs

v1's 528 rsIDs less those the seed list holds, as legacy rows (R-LEGACY-1), unless one qualifies for A/B on
modern evidence. Their depth waits on D6.

## What the requirements' open decisions (§11) block

None is asked until a locus needs it.

| Decision | Blocks |
|---|---|
| D1 weights | no row: a row carries no weight; the module seat's export |
| D2 APOE ownership | 96 APOE and its proxies (rs2075650, rs4420638, rs769449, rs405509, rs449647, ...) |
| D3 name and version | no row |
| D4 biological-ageing markers | the `ageing_markers` loci: TERT (132, 133, 153), TERC (23), LRRC34/TERC (104), POT1, NAF1, STN1/OBFC1 and the clock and LOY loci: whether they get rows at all |
| D5 mortality PGS | no row (the module's `pgs.csv`) |
| D6 legacy layer depth | v1's remaining rsIDs, and whether Build 3's 2,339 non-significant entries are ever read |
| D7 ancestry-specific loci | IL6 rs2069837, BMPER, BET1L, CLEC3B (116), the Taiwanese and CLHLS loci: their view, not their tier |
