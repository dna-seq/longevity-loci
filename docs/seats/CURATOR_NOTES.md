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
  adjust pacing and go next 10 and so on unless blocked or I steer"; this replaces the earlier pause after ten). Rows done in this run: 6 CELSR2 (1 of 10), 38 HLA-DQA1 (2 of 10), 81 FES/FURIN (3 of 10), 103 (4 of 10), 2 PABPC4 (5 of 10), 4 LINC02796 (6 of 10), 5 FPGT / TNNI3K (7 of 10), 7 MAGI3 (8 of 10), 8 IL6R Asp358Ala with 157 (9 of 10); 10 RABGAP1L (10 of 10); second run: 11 LINC01875 (1 of 10), 12 KCNK3 (2 of 10), 13 PRKD3 (3 of 10), 14 LINC01122 (4 of 10), 15 AFF3 (5 of 10), 16 LRP1B (6 of 10), 17 CASP8 (7 of 10), 18 TMEM43 (8 of 10), 19 HMGB3P12 (9 of 10), 20 RNU1-96P (10 of 10); third run: 21 IP6K1 (1 of 10; held, then committed under D20), 24 NLGN1 (2 of 10), 25 HTT with 158 (3 of 10, after the colocalisation sweep), 26 GPR78 (4 of 10), 27 LINC02513 (5 of 10), 28 RNU1-63P (6 of 10), 29 MAML3 (7 of 10), the Timmers 2022 survival sweep (a correction, not counted), 30 TERT held on D4, 31 LINC02064 (8 of 10), 32 intergenic 5q14 (9 of 10), then the lead's review of 103, 8, 2, 10 with 5, 4 and 11 under D17/D18 (one commit each, not counted as rows); 6's healthspan re-cited to Zenin's cached file (597d9fb); 103 re-tiered B under D16 (5abae88); the Open Targets quotes re-quoted from cached records (f69c8d8); the corrections of 71 (d44fd4a) and 67 (3dd792c) done, the E3 gene rule at 57 (8d27300) and 80 (728d78d), 67's MANOVA study added under D15 (a519ae4); 38 corrected again at 103 (the AncestryDNA tag is shared); next 96 APOE waits on D2, so the seed tier B by locus_id.
- **10 RABGAP1L** (2026-11-11), tier C re-tiered (seed B); briefly blocked on a `study_design` value, which the lead
  added as `current_age_quantitative` (8187cb8; the study written as a row, not prose). Both seed rsIDs
  (rs10798302 lead, rs16847402; r² 0.53, D′ 0.99, cached as db-ensembl-116 `ld-rs10798302-rs16847402.json`) come
  from Wright 2019's S8 `Male_Female.AGE`: a quantitative GWAS of AncestryDNA customers' own current age (n 482,068,
  λ 1.374, LDSC intercept 1.04, S Table 3), not the parental meta-analysis the seed names; neither is in S9. Raw P
  1.7e-8 (the catalog's 2e-8, GCST009448), genomic control 1.5e-6; the paper names only APOE and MAP2K6 from it.
  Class VIABILITY_AF (§4.5, confirmation only), so tier C either way; the AncestryDNA fathers 1886-1940 result (G,
  raw P 7.5e-4) is the same customers, not a replication; Timmers sumstats P 0.19 same side, Zenin null. Wright's G
  at rs16847402 (Ensembl T/C) is the forward C, by complement (derived). Open Targets 26.09: count 0 for both in
  the seven lifespan studies plus GCST009448 (whose three sets are 11p11, 8p12 WRN, APOE): C4, no gene. Cached,
  quoted. Rules settled: a current-age GWAS is VIABILITY_AF / current_age_quantitative, confirmation only, so never A/B
  alone; Wright's S8 keeps the raw P as the study's P, the genomic-control P beside it in statistical_test; the
  AncestryDNA parental result is not a replication of the same customers' age GWAS; mechanism with membership-only
  records (no allele) is general_ageing with the traits named, never a direction; the seed's second SNP at r² 0.53 is
  named in the header and verdict, not scored.
- **38 HLA-DQA1** (2026-11-11), tier B (seed A), advisor-checked. Lead rs34967069 (Timmers 2019 Table 1, q16). Rules
  settled: in a multi-signal region (MHC), a seed rsID with no quoted r² to the lead is named in the verdict, never a
  `proxy_rsid` (frequency bounds on r² move with the frequency source and are not written as findings); Joshi's
  rs34831921 and Pilling's rs28383322 stay unscored. Open Targets 26.09 resolves neither rsID and has no lifespan set
  in the MHC: C4/E4, no flag (nothing to cite), `gene: ""`. Timmers 2019's Figure 4 source data is cached
  (`fetch-supp`, q17): its R2 column repeats Freq1 and its rsID/Proxy headers are swapped, so no r² is read from it.
  Wright's S8/S9 hold clumped "representative" SNPs only: a lead's absence there is not a null. Age MIDLIFE INFERRED
  (Joshi q9, at his SNP). Seed trade-off (hypothesised) not recorded.
- **103** (2026-11-11), tier B re-tiered (seed A); first written C, moved to B the same day under D16 (the lead,
  639325686). Healthspan genome-wide (Zenin, P 1.4e-11, its own signal: LD shadow from 38's lead 2.9 vs z 6.9),
  not replicated (P 0.146 in unrelated UK Biobank others). D16: a co-occurring lifespan signal is a scoring-class
  lifespan study at p < 0.05, same allele and direction; Timmers 1.4e-4 (summary statistics, pmid-30642433#q23)
  is one, so healthspan scores and the single-study clause gives B. AncestryDNA mothers 3.3e-4 at rs3135006, r²
  0.80 to rs1049053 (Ensembl 116, cached by RM3: `corpus/db-ensembl-116.md`). Both lifespan results are shared
  with 38 (r² 0.32 between the leads; shadow 3.3 vs z 3.8) and unconditioned: kept as a caveat in the verdict.
  D16 also: no HEALTHSPAN_ONLY token (C keeps a locus out of scoring); a C row keeps directional genotype states
  (only R-TIER-1 forces neutral). It decides 35 IRF4, 66 TYR, 86 DEF8 and the mvAge-only loci (2 PABPC4 the
  first: C, its lifespan P 0.071). Phase from frequencies plus r² is written as derived, never as a record.
  Mechanism general_ageing from Zenin's multimorbidity line (q11).
- **8 IL6R Asp358Ala** (2026-11-11), tier C re-tiered (seed B), 157 folded in (D14: rs8192284 merged into
  rs2228145, db-ensembl-116#q7-q8; the file `8-IL6R_Asp358Ala.yaml`, `also_loci: [157]`). Nothing genome-wide at the
  variant; R-TIER-4 keeps Rosa 2019's cis-MR (34 instruments, none the variant) out of A/B: annotation, linked to C
  through the catalog's sIL6R record (derived). Nominal and one-sided: Timmers sumstats 0.0034, Wright AncestryDNA
  fathers 0.0011 (raw P, as at 38/103; mothers 0.0051) at rs7518199 (r² 0.93, phase by frequency), Zenin 0.017; WHI
  survival to 90 null (OR 1.00 CC vs AA, abstract), too wide to contradict, so C not D. C here is a judgement, no C
  clause fitting the lead literally (not suggestive; the replication is independent, not same-group). WHI's survival
  to 90 (52 % reached it) is OWN_SURVIVAL, not EXTREME_SURVIVAL_CC (§4.5: ≥90th/99th percentile, centenarians), so
  exceptional survival stays untested. Wright S9's columns are meta P, n, AncestryDNA P, β, SE, UK Biobank P, β, SE
  (misread once at this row, fixed in the follow-up). Rules settled: the first coding lead is effector E1 with `gene` named
  (§4.2's coding clause, Ensembl's and Open Targets' missense consequence); causal level read from longevity sets
  only, and a cached `credibleSets(studyIds, variantIds)` count 0 is the citable C4 (the filter matches members, not
  only leads, checked at MAGI3); a trade-off read from stated catalog alleles is `tradeoff` with `negatives`;
  drug-target loci get `mr:drug_target_proxy` and genotype text that names no treatment (R-VOICE-4). Pilling's
  rs6689306 (suggestive, r² 0.40, A with A by D′) named, not scored. For the lead: §5.2's example "IL6R rs2228145
  (B)" conflicts with R-TIER-4, and R-RARE-2's "never above tier B" with R-TIER-4's "never A/B" (PCSK9 R46L); and
  whether R-CAUSAL's "marks a region" unless C1 lets a C4 coding lead's text say what the variant does to the protein
  (here "dampens interleukin-6", quoted at pmid-39579785#q1): kept, asked.
- **7 MAGI3** (2026-11-11), tier B kept, advisor-checked. Lead rs1230666 (Timmers 2019 Table 1, q29; P 6.4e-9, new
  there, so no LifeGen-only result: the sumstats' "--" is direction only). Rules settled: C level by §4.2's PIP
  threshold even from a PICS set (0.64 in the lifespan set, C1), with the method and the in-set coding candidates
  (rs2476601, rs6679677 at r² 0.67, PIP 0.02) said in the verdict, and C1 never turning the genotype text from
  "region" to a gene; whether §4.2 should treat LD-only PICS as SuSiE is a question for the lead (not blocking).
  Timmers 2020's GCST011100 association has no effect size in any cached source: prose, not a directed study (D15).
  The GWAS Catalog's disease records are cited through the catalog note only (their PMIDs are not
  literature_search results); every stated allele read before a trade-off is judged; one with a self-contradicting or missing allele leaves it open ("none detected", never "none"). Age UNKNOWN:
  Timmers 2019's age-band section names only APOE, CHRNA3/5, CDKN2B-AS1 and ABO.
- **5 FPGT / TNNI3K** (2026-11-11), tier B kept, advisor-checked. Lead rs146254978 (Pilling 2017 Table 2, q15),
  genome-wide only in the parents' age-at-death analysis (n 208,118, P 4.6e-8; attained age 0.021). Rules settled:
  Pilling's age-at-death β is on summed z-scored ages (q17), positive = longer life, the opposite of the Martingale
  sign the note's header gives; calibrated at BEND3 rs1627804 against Timmers (q18, pmid-30642433#q28), never from
  the GWAS Catalog's reading of the same table. A variant Open Targets does not know is C4/E4 with no flag and
  `gene: ""`; its mechanism `general_ageing` is written as unassessed, never inferred from a gene's name; pleiotropy
  left empty (unsupported) rather than `broad`. A top-10 % P with no direction is not an outcome cell: exceptional
  survival `untested` (Pilling's workbooks: PMC serves HTML to a script). The study P is the paper's 4.6E-08, not
  the catalog's rounded 5e-8. New database note `db-gwascatalog-2026.10.29` (REST API v2, `associations?rs_id=`,
  release from `/api/v2/metadata`); the old `2025.01.09` note no longer has a citing row.
- **2 PABPC4** (2026-11-11), tier C re-tiered (seed B) (B since the D25.13 sweep), the first mvAge-only locus. Rosoff 2023 Table 1: rs3768321
  G +0.0079, P 6.46e-10, novel (no input GWAS genome-wide within 1 Mb), Q P 0.02. Lifespan: Timmers sumstats P 0.071
  (G longer, "--"), not p < 0.05, so D16 gives C; healthspan suggestive (Zenin sumstats 1.8e-7). Wright S8/S9: no
  clumped SNP at it (nearest 135 kb, P ~1e-3, LD not read). Open Targets 26.09 (cached, RM3): mvAge's set
  (GCST90321079) PIP 0.17 C2, L2G PABPC4 0.23 E3, gene ""; the same variant is HDL's (PIP 1.00) and triglycerides'
  (0.90) fine-mapped variant, the anchor for mechanism metabolism. Genotypes: common G/G neutral, T carriers risk
  (C rows keep directional states, D16). Seed-B loci whose seed source is Rosoff alone (4 LINC02796 and others in
  Table 1) go the same way unless a lifespan study reaches p < 0.05.
- **4 LINC02796** (2026-11-11), tier B kept (seed B), the first mvAge-only locus D16 lets score. Rosoff Table 1
  (q8): rs2613508 C +0.0077, P 7.77e-9, Q P 0.60. Lifespan: Timmers sumstats P 5.3e-4, C longer, "--": the
  co-occurring study, so the single-study clause gives B. Healthspan Zenin 3.3e-4, same side. Wright S8/S9 and
  Deelen SD1: nothing within 0.5 Mb. Open Targets 26.09: mvAge set abc062e8… led by rs2613508, PIP 0.048 of 75
  (C3), L2G NEGR1 0.56 (E2), gene NEGR1; BMI set (GCST009001) lead rs1993709 r² 0.99, G with T by frequency
  (derived), so T raises BMI: mechanism metabolism, pleiotropy mech:adiposity + broad. Open Targets ids here are
  REF_ALT as the record has them (1_72367899_C_T), not the seed's guess: a variant query on the wrong order returns
  null.
- **38 corrected** (2026-11-11), the lead's review (handout 20261111T004405Z-review-38) applied; superseded at
  103: B on the single-study clause, the AncestryDNA tag being shared with 103 (r² 0.80 to its lead). Was B for
  §4.1's tag clause: Wright S8 (AncestryDNA mothers 1886-1940) has rs3135006 (A = dbSNP's minor T, other strand) at
  P 3.3e-4, S9 meta P 3.1e-5, het 0.32 (q23, q24); added as a nominal proxy study. Rules learned: search Wright S8/S9
  by position near a lead, not only by rsID; an r² the lead review gives is checked against Ensembl's 1000 Genomes LD
  (`rest.ensembl.org/ld/human/pairwise/A/B?population_name=1000GENOMES:phase_3:EUR`) and cited in prose until RM3
  caches LD records (rs34831921 r² 0.97 EUR, rs3135006 0.38, D′ 1; rs3135006/rs3129720 CEU 1.0). No power claim
  without a quote. Genotype text says "linked to" where no quote gives a direction. Age DIRECT_WEAK (Joshi q9 at a
  SNP of r² ≈ 1). Exceptional survival kept 0: CHARGE P 0.003 at the tag is outweighed by the larger combined
  samples (Timmers Fig 4 at the tag, Deelen at the lead). The "25 signals" line had no quote and is gone.
- **81 FES/FURIN** (2026-11-11), tier A kept, advisor-checked. Lead rs6224 (Timmers 2019 Table 1, q18; PIP 0.22,
  C2); rs17514846 (Pilling) r² 0.92 from Open Targets' GCST009890 set, a proxy. Replication: Figure 2 source data
  sample b, P 0.013, the same pattern as 67 and 71. Effector E2 FES by L2G alone (FURIN 0.15; SMR names both, and SMR
  is not a colocalisation). Wright's S9 has nearby clumped SNPs (rs4702, rs2677737) with no r² to the lead: named,
  not scored, no heterogeneity. No mediator flag: Pilling's blood-pressure sentence is about the gene, not the SNP.
  Timmers 2020's cached text has no row for this locus; its MV P from Open Targets is not used. Scout's
  pmid-42928374 (gene-level FURIN pleiotropy) left queued, not cited.
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
- **21 IP6K1** (2026-11-11), tier A re-tiered (seed B), committed under D20 after a hold; the lead answered (a) at 639377669 and will read it adversarially. The lead's point, checked first: Timmers' "-+" at the lead is not an opposite effect but an unstable LifeGen sign (rs9855505, r² 1.00, reads "--"; 23 of 57 SNPs at P < 0.005 with the lead's frequency disagree): LifeGen does not replicate, at power about 0.4 from its SE at other loci (q19, q14), so not red-flag under 71/67 (put to the lead); Timmers rows for 3:49.75-49.90 Mb cached as `rows-c9881a08`). Rosoff's mvAge cited in the tier only. The lead's adversarial read (639380875): A holds under D21; corrected in one commit: power recomputed from UK Biobank's backed-out β (about −0.0176; one-sided 0.6 to 0.7, heterogeneity P about 0.055), genotypes per §6.2 (A/G the reference, G/G protective, A/A risk), PROTECT dropped, the meta row's METAL sample-size scheme, per-dataset genomic control and separate parental meta-analyses quoted (Wright q56-q58), AncestryDNA's GC P in the verdict, the direction order said as this reading's, the uncached Open Targets anxiety and QTL sets dropped. Rosoff's MOESM3 (Supplementary Tables 1-50) fetched without a 403 on 2026-11-11 (`pmid-37550455.supp-43587_2023_455_MOESM3_ESM.xlsx`). The hold, as it stood:
- **24 NLGN1** (2026-11-11), tier B kept. Rosoff's MOESM3 now fetches (it 403'd for row 21), so mvAge is a study row
  from Supplementary Tables 6, 7 and 10 (`pmid-37550455` q15-q20; ST07's input columns are recoded, so each input's
  direction is read from its own source). Frailty genome-wide at the locus (Atkins, by the catalog record at rs583514
  and Rosoff's look-up) is healthspan-class and Wright's viability result confirms only, so B (the lead's D23,
  2026-11-11, option (a)); modifiable through weight (D18.2) on the set leads' betas phased by frequency (Harris 2024's
  two sets dissent); no PROTECT token at 45/55 (as at 21); E1 NLGN1.
- **25 HTT** (2026-11-11), with 158 folded in (D14; rs82334 r² 0.66, the lead's shadow by z). Tier A (seed B): Timmers
  2019 genome-wide, replicated by Timmers 2022's FinnGen and Biobank Japan look-up (Supplementary Table 6 in MOESM1,
  the abstract alone says "independent"; rs362273 r² 0.67 EUR, 0.76 EAS, P 0.001 one-sided) and Deelen's 99th
  percentile (P 0.0093; 90th 0.19). The survival look-up is written `meta_analysis` with OWN_SURVIVAL; frailty
  (Atkins) `meta_analysis` with HEALTHSPAN, there being no frailty design. Atkins' P 3e-7 at rs61348208 carries a
  chromosome-3 label (RBM6) and is not read. E2 HTT on the one set holding the lead; mvAge's set (same signal,
  MSANTD1 L2G 0.55) would make it E3; told to the lead as a default. The seed's ADD1 (rs16843603) and MSANTD1
  (rs114298671) are separate signals (r² < 0.1); ADD1 looks like a B candidate under D16 (mvAge 4e-10, lifespan
  2.6e-7, FinnGen/BBJ P 0.042), no seed locus of its own.
  Corrected after the advisor's read: Timmers' set holds rs16843836 and rs82334 too (a credibleSets listing shows only
  25 locus rows; query a set's own `locus(variantIds:...)` for a PIP); phases shown by frequency and r² ceilings, never
  by direction; Timmers' Figure 4 look-up added with its D21 numbers; the conclusions say the SNP is not the
  Huntington's repeat. Owed: Timmers 2019's age-band source data (the seed's K_timmers2019_age_bands.csv) for the
  Table 1 rows (7, 12, 25).
- **The lead's batch-4 review** (2026-11-11; handout 20261111T113229Z-review-batch4, D25), one commit per row before
  row 33: 26 (80b7691, 00753fd) D held, genotypes neutral (D25.2), "flat or opposite", age_of parent with Deelen's
  parental definition (q81), the literature search recorded; 25 (295d2f9, 67b3d6c) A held, E3 with mvAge's set
  counted (D25.4), both calibrations stated (D25.3; mean-factor heterogeneity P 0.37 by my arithmetic, factor fixed),
  East Asian phase shown from frequencies; 29 (47b2a8b) general_ageing (D25.7); 31 (03d4ef5) Gurinovich's main text
  read, independence of Deelen shown as far as both papers go, but held at C and B put to the lead: §6.3 wants an
  effect size NECS does not print, and `check rows` lifts R-TIER-2 only on a second genome-wide study (D22.2 says a
  scoring-class replication). Scout got rs13141210 (28), ADD1 rs16843603 and, on its question, MSANTD1 rs114298671
  (25) (737f930, b3ccb2a). Lessons: `loci fetch-supp` renders a publisher PDF but not PMC's HTML or XML (file for the
  tooling seat, unattended); a PDF cached as `supp-` is read at depth `supplement`, and its quotes must avoid
  hyphenated line breaks and glued superscripts ("aFor"); a GRCh37 Ensembl record fetched under db-ensembl-116 passes
  the release check made against the main server, so say the server in the note (also to file); the fix helper's
  whitespace pattern eats indentation and newlines on a one-line field, so edit such lines with sed.
- **40 ABCC10** (2026-11-11), tier B kept (D18.3), row 39's shape: an mvAge lead with an independent nominal AncestryDNA replication at a tag (fathers, rs1214759), holding after Wright's genomic control. Lessons: Timmers' 1.2e-7 is `suggestive` (the check's band is 5e-8 to 1e-5), not `nominal`; a FinnGen null is calibrated within FinnGen against Timmers' self-scale β: APOE's factor (about 0.99 there) flags it, and D25.12's second factor is a mean over leads that hold up within FinnGen, never Figure 4's 0.42 (advisor), so unknown here; Wright S9's counted allele confirmed three ways (S8 prints A, the UK arm against LifeGen, Deelen's sign); Wright's mothers' lines 150 kb away are another signal (r² ≤ 0.16). The reference genotype first rested on 1000 Genomes EUR's pooled 0.35, within a standard error of the 1/3 crossover; every large sample (gnomAD NFE, LifeGen, Deelen, FinnGen, CEU) puts C/C first, so C/C (advisor): near the crossover, read the large samples. Trade-off first written on eGFR (the longer-life C lowers it); the kidney's disease endpoints (acute renal failure at the lead, three chronic sets at neighbours on T's haplotype) run with T, so no trade-off, preventable as row 27, put to the lead. Anchor Open Targets' beta sign on a SuSiE-inf set, not a PICS one (PICS copies the catalog's beta).
- **41 PRDM13** (2026-11-11), tier D from B, row 19's paper and row 26's shape. A discovery whose own allele frequency is wrong by two orders of magnitude: NECS's controls 0.0004 against gnomAD NFE 0.097, the LGP with no carrier against gnomAD ASJ 0.13. Lessons: when a summary-statistics file lacks a SNP, look for an indel at the same spot (Deelen's 6:100051298:ID, the deletion rs66927770 with its anchor base; Ensembl's region overlap listing shows dbSNP's joint CG>A record); FinnGen types SNP and deletion together. A 7-digit position regex (`996[0-9]{4}`) silently matches 9.96 Mb, not 99.6 Mb: count the digits. A positional regex for Zenin's deposit must not assume the delimiter (`\b100053621\b` works; `,6,…,` and `\t6\t…\t` returned nothing), and an empty result needs a positive control in the same regex before it reads as absent (advisor). Merged rsIDs (Ensembl's synonyms) go in the rsID regex too. A proxy leaning the discovery's way is kept out of `studies` when it is not counted: a study entry is how a counted replication is written. `unsupported` grows by one per row, the empty age-of-action cites. Where a red flag's scale is uncertain, state the smallest factor at which power and heterogeneity still flag (here 0.055) instead of two calibrations not at hand (advisor). Proxies at r² 0.6 leaning the discovery's way are named, not counted, below the 0.8 used elsewhere; put to the lead. Open Targets `variant null` was retried by study (GCST012419's five sets) and under the deletion's id before C4/E4.
- **42 BEND3** (2026-11-11), tier B kept, row 5's shape (same Pilling analysis). Lessons: Timmers' Figure 2 source data's discovery column for a Pilling lead is the attained-age result, not the analysis that made it genome-wide; say which β the power is computed against. Wright's Table 9 label was a strand complement again (A for a T/C SNP): orient it by the UK Biobank arm against Timmers' line for the same SNP. With D′ 1 the nesting of a weak tag can be read from r² and the frequencies (only one nesting fits), derived, not phased. FinnGen under APOE's factor alone settles "no flag" when power is under 0.8: the uncomputed second factor cannot raise one. A `fetch-supp` of FinnGen's suffix-less `.gz` needs `--name …tsv.gz` (refused otherwise). The catalog's `snp_effect_allele` on an association with no estimate gives no direction. No PROTECT token where no disease is known at the locus (row 21's reading). Semantic Scholar was rate-limited: five services answered. `unsupported` grew by two here: the empty age-of-action cites and the empty pleiotropy cites (as at row 5; `check rows -v` lists them). Open Targets was retried by Pilling's two studies (GCST006702, six sets; GCST006698, two), none at 6q21 (advisor). A 99th-percentile APOE factor borrowed from the 90th's ε4 line is said so.
- **43 FOXO3** (2026-11-11), tier B kept, row 27's shape (Timmers 2020's multivariate locus with Timmers 2019 co-occurring). Lessons: a famous candidate locus can still lack a genome-wide GWAS result; Broer's 1.85e-10 is a look-up pooled with the published candidate samples (Deelen's table prints 10,574 cases against the GWAS's 6,036), and Timmers 2020 says FOXO3 was never genome-wide; put to the lead (A alternative). Read all of a variant's Open Targets sets (214 here; the first 100 missed the frailty set). Phase two SNPs from frequencies and r²: opposite coupling caps r² at p1·p2/((1−p1)(1−p2)) for the minor alleles. A Timmers 2020 harm line (macular degeneration) is a quoted trade-off at the locus; the row needs `negatives` when it carries `tradeoff`. The multivariate signal colocalises with lower FOXO3 in blood, so conclusions never say G raises FOXO3. After the advisor's read: grep the GWAS Catalog at a set's lead too, not only at the row's SNP (rs6911407 at r² 0.98 carried Wright's AncestryDNA replication and the cognition direction); a variant block takes its effect and significance from one study, or says it is split; a harm quoted at a weaker tag is worded as a nearby marker's; an abstract's run-together headings ("ConclusionsWe") and a reference number glued to a word ("consortium7") break the quote check's word boundary. Owed to the lead: the A question (Broer's pooled P with AncestryDNA) and the healthspan cell under Foote's cognition factor.
- **D25.13 sweep** (2026-11-11; the lead, 639502812 and 639505086), one commit. Found by scanning every row's study entries and verdicts for a same-side P of 0.05 to 0.10 (the scratch scan's two regexes), not from recall: it added 10, 11, 12, 27, 29, 33, 67 and 71 to the six the lead named; the lead was told before they were folded in (639506970). Tier moves 2, 17, 18 C to B; 18's rests on Liu's printed P (D17.3) and a weak European replication beside Deelen's powered null, put to the lead as the raise to attack. 27's and 71's AncestryDNA fathers (0.0496, 0.0498) pass by a hair; 93's mothers now quoted from S9 (q79, q80). Lessons: halve only a printed two-sided P, on the discovery's side, at the lead or the tag already read; a value already one-sided (Timmers 2022's FinnGen/BBJ, Timmers 2019's longevity look-up) stays; keep the printed P as not_significant and give the one-sided value in the test text; a raise moves `verdict`, the outcome cells and the genotype texts' certainty words too. After the advisor's read: the first scan's regex missed second values ("P 0.21 and 0.061") and statistical_test strings, so scan the whole text for a bare 0.0[5-9] and read each hit (it added 36's healthspan cell); Wright's Table 9 AncestryDNA P is raw (its legend), while the paper calls on genomic-control P (S Table 3's λ: mothers 1.113, fathers 1.182, quoted q82 to q84), so a raw one-sided pass near 0.05 can vanish after correction (27, 71, 39's fathers); `check rows` exiting 0 on 18 at B does not mean R-TIER-2 was met: Liu's entry is `meta_analysis`, so the rule never fires on it.
- **39 ILRUN** (2026-11-11), tier B kept (D18.3), with an independent nominal replication in AncestryDNA's mothers at a tag. A trade-off by D18.1's letter (the longer-life A raises LDL and apolipoprotein B) put to the lead as the row's judgement call: the same haplotype has less heart failure and thrombosis, so the harm is a risk factor against diseases running the other way. Lessons: a database release (FinnGen) cannot be a study entry, cite it from an axis; a tradeoff locus needs `negatives` on the variant; Open Targets' plain `colocalisation` returns GWAS partners only, so query `studyTypes:[eqtl,...]` for QTLs; the GWAS Catalog's GCST90501xxx NMR lines print the opposite sign to Open Targets' sets for the same accessions, so they are not read for direction; Wright's S9 counted allele is anchored by the UK Biobank arm's sign against Timmers (row 15's method), FinnGen's tag agreeing. After the advisor's read, D25.13 as amended (it holds back to every row) applied at once: Deelen's 0.070 and 0.055 are one-sided 0.035 and 0.027, so exceptional survival is +; row 14's 0.060 joins the retro sweep. The proxy block was checked past the ±250 kb window from its edge SNP (rs112563428): it ends inside.
- **37 HCP5** (2026-11-11), tier B kept; after D25.13 (the lead, 2026-11-11) without replication_failed: a replication's P is read one-sided in the discovery's direction, and replication_failed marks a sample that fails, not one that replicates at a smaller effect even with a red-flag heterogeneity. Lessons: the pairwise LD endpoint answers pairs megabases apart (db-ensembl-116#q242, 2.7 Mb), so an empty pair with both SNPs in the panel reads as r² below 0.05 whatever the distance; the window listing reaches only 250 kb either side. A Wright S9 tag closer than Table 3's lead can change the numbers (rs3130467 r² 0.95 against rs1265159 0.83): grep S9 for every r² ≥ 0.8 proxy, not only the named lead. Wright's printed heterogeneity P (METAL) differs from one computed from the two arms' betas (0.040 against 0.11): state both. Check a Catalog trait's study ancestry before carrying it by a CEU r² (the six psoriasis lines were Egyptian, Taiwanese, Chinese or unreported). Cache every proxy record a row's prose counts (`fetch-supp` per rsID), never curl output. Timmers 2019's Figure 5 source data (age and sex bands, moderators; `elife-39856-fig5-data1/2-v2.xlsx`, now cached) print an allele suffix that is neither consistently the lengthening allele nor the other one: read the moderator P values and band contrasts, never the suffix's direction. The owed sweep of Figure 5's loci against the curated rows is done (see its PROGRESS line; the lead: "schedule it as you did Timmers 2022's"). Lessons from it: read a band's shape within a locus only (Beta and Z disagree in sign at some loci), never a class from the fathers' 90-120 band, never sex_specific on a nominal moderator that fails the paper's FDR; a null moderator alone is not constancy. Unrowed Figure 5 loci: ABO, 13q21.31, IGF2R, POM121C, HP, GBX2/ASB18, ZC3HC1, FOXO3A rs3800231 (for 43), APOE (for 96). rs3131621 queued for the scout (D25.6).
- **33, 35, 36 and the corrections to 31, 17** (2026-11-11). 31 ended B (D25.10, Deelen's nominal look-up lifts
  R-TIER-2). 33 5q33.3 B kept, A put to the lead (Timmers' parents as a smaller-effect replication). 35 IRF4 written
  A on D16, ruled B (D25.11: healthspan replicating healthspan in UK Biobank counts nothing toward A; a scoring-class
  replication outside UK Biobank is needed); every skin_sun row is modifiable, act_screen:skin, so 17 moved too.
  36 COX11P1 B, replication_failed: Park's own FinnGen look-up fails with power 0.97 under an APOE factor scaled
  within FinnGen; D25.12: MUC5B alone is not D25.3's mean, and a colocalisation alone is E2 (D24's rival check said
  unrun). Lessons: Park 2025's deposit (GCST90551884) swaps its allele columns, every β and frequency belonging to
  `other_allele` (APOE's ε4 at 0.84), so directions come from the paper; Zenin's deposit gives raw P (divide Z by
  √1.053); a triallelic lead gets no LD pair from Ensembl, so use a tag; FinnGen r11's PheWeb API shows null for a
  non-significant endpoint, so read the full file (`--name x.tsv.gz`, a suffix-less `.gz` is refused). To file with
  the tooling seat at idle: fetch-supp cannot render PMC HTML or XML; the suffix-less `.gz` refusal; the grch37
  release check reads the main server.
- **32 intergenic 5q14** (2026-11-11), tier C (seed B), row 16's sister from Chang 2022, D16 as there. The allele is not East Asian only: gnomAD Finns 0.023 and admixed Americans 0.028 carry it as often, non-Finnish Europeans 0.0008, so the European look-ups hold no line for it; the FIN-window SNPs at r² 0.74 run at 1 % in LifeGen and Zenin and do not tag it there. The replication arm is separate people of the same cohort and team, already inside the meta P: not a replication on its own (row 18's dataset-inside-the-meta precedent; D19.1 is about overlap, not this), settled by the lead as D25.9 (an arm inside the pooled P replicates nothing); row 16 reworded to match. Advisor: grepping row-filtered cache files is no search; run literature_search on the rsID and record it. Open Targets' one-variant PICS set: C1 by construction (row 19's wording); L2G XRCC4 0.85 with no colocalisation, E2 under D24, the first E2 on a one-variant set. Note depth for database records is `record`, not `database` (check quotes refuses it). A quote ending against a reference numeral ("frequency14") is not found: end it a word earlier.
- **31 LINC02064** (2026-11-11), tier C (seed B), B and D put to the lead. 30 TERT skipped: the requirements' `ageing_markers` names rs2736100 itself, so it waits on D4 with 23 (now in PROGRESS's D4 line). Row 19's paper (Gurinovich 2021), a common SNP this time. Deelen's 99th percentile is a scoring-class replication leaning the discovery's way (rs694966 P 0.0119), but independence is unknown: Deelen's cohort list (pmid-31413261#q80) has no NECS, yet holds LLFS and the Longevity Gene Project, and NECS's controls are in the unread main text (fetch_fulltext on PMC8190315 retrieved nothing). LifeGen and Zenin read at the well-imputed proxies, not only at the lead (advisor): the lead imputes at info 0.82 with A 0.39, its proxies at 0.995 with 0.31. Power by Timmers' own APOE conversion (pmid-30642433#q91), with NECS's rs429358 row against LifeGen's (factor about 9.4, crude odds ratios, derived). Zenin's `--rows` regex is `\b(...)\b`, not `^(...)\t` (its file is a CSV; a tab regex matches nothing). Gurinovich's Supplement Table 1 lists every SNP past 5e-8, so proxies missing there are informative (advisor's second pass): an r² 1.0 proxy carries the lead's Z, so a lead alone just past the cut rests on its own imputed calls. D22.3's exception is proxies leaning in the flat look-up itself (row 18's LifeGen), not a lean in another study: C here is by analogy, D the alternative. Lesson: read a look-up at the lead's well-imputed proxies as well as at the lead before resting a red flag on it.
- **29 MAML3** (2026-11-11), tier B kept, with a counted independent replication (FinnGen and Biobank Japan, via Timmers 2022's aging-GIP1 lead at r² 0.96), held at B by D18.3 because both genome-wide results are multivariate; row 25 was A on the same look-up only through Timmers 2019's genome-wide hit. Open Targets' `credibleSets` beta is the set lead's, not the queried variant's: read no direction from it without phasing the lead. Page all sets (`page:{index:0,size:100}`) before a trade-off or mechanism call; the first query returns 25. Mechanism smoking_lungs by row 14's rule (the lead leads three smoking sets), general_ageing the alternative put to the lead. Wright S9's printed allele checked on this locus at rs6840907 (S8 prints the counted allele, LifeGen agrees). Timmers 2022's MOESM6 prints NA for MAML3 (no fine-mapping). The owed sweep of Timmers 2022's survival look-up (MOESM1 Supplementary Table 6, all 23 leads) is done (see the sweep line in PROGRESS): 21 and 4 have new study rows, 28, 7, 15 and 67 prose. Its "Freq1 (BBJ)" column does not match 1000 Genomes JPT (TRAIP 0.50 against 0.76, NEGR1 0.20 against 0.029) and tracks Supplementary Table 4's discovery frequency within 0.02, yet prints 0.00 where Japan does not vary; what it holds is unknown: quote it as printed, never as Japan's frequency. Japan's share of a look-up's information is estimated from the two FinnGen-only rows (N 218,396, 15,152 deaths) by deaths × 2pq (advisor's second pass: NEGR1 about 30 %, not "Finnish only"); check East Asian frequencies in 1000 Genomes before writing ancestry [EUR, EAS]. Lesson: when a paper is first used for one row, sweep its whole look-up table against the curated rows then, not later.
- **28 RNU1-63P** (2026-11-11), tier B kept, on the seed's lead rs28637671 alone. mvAge only (1.95e-8, T healthier), D16 by LifeGen (T, P 5.8e-4); the lead is not rs13141210's shadow (r² 0.095 bounds z at about 1.4 against 3.44). Open Targets has no record of the variant under either allele order (`variant null` for T_G and G_T): C4/E4. Wright's only candidate tag is rs1481245 (r² 0.51, a weak proxy as row 10's 0.53), AncestryDNA fathers raw P 0.016, A with the lead's T. Ensembl's LD endpoints have a 0.05 r² floor that a lower `r2=` does not lift (window listing's least value 0.050020); a pair the endpoint returns empty, both SNPs in the panel, reads as r² < 0.05, cited from the window listing. The seed's rs13141210 is a separate signal with a stronger case (lifespan 9e-6, AncestryDNA at r² 0.94 tags, its own mvAge set in Open Targets): kept out of this row's axes as row 25 kept ADD1, and its own row put to the lead. Advisor's second pass: "no other trait" checked at the lead's 54 proxies (r² ≥ 0.8; the catalog one by one, Open Targets' search on the top ones): one sub-threshold record only; rs1481245's paracetamol sets are rs13109040's (r² 0.39); the proxy bounded both ways (lead predicts z 2.5; rs13141210's tags could give 1.6 of 2.4); rs13141210's tags' direction left unread (phase undetermined at 50/50). Lesson: when the lead has no record, run the trait search over its proxies before writing "no other trait".
- **27 LINC02513** (2026-11-11), tier B kept. Row 20's shape (Timmers 2020 MANOVA plus mvAge, D16 by LifeGen P 0.0016). Rosoff's Supplementary Table 6 prints the alleles A G with G's beta; Table 7 (effect allele first) and the catalog's rs17499404-G anchor the direction. Open Targets has no mvAge or Timmers 2020 set on 4p14 although the catalog names the SNP top hit of both (study-sets probes, q413-q414): C4/E4 stands by the longevity-set rule; KLF3 (L2G about 0.75 on the blood-pressure-coloc frailty and lymphocyte sets) in prose only. Foote 2025 frailty (PMID 40759756, title-checked) is genome-wide at rs2291433 (r² 0.996): healthspan +, cited from Open Targets' set, no pmid note. Wright S9 found by region (grep by position, not rsID): rs2291433's AncestryDNA arm, counted allele derived as at row 15. Deelen's position-only rows are ungrained in `check rows` (as row 20's q39/q40); kept. Age UNKNOWN as at 67 (q2 is collective), not MIDLIFE as 46/93. Reference genotype the heterozygote at 54/46 (as 21, 24), not row 20's homozygote. Advisor's second pass: Wright S9's stronger nearby SNPs read for LD (r² 0.29-0.40, not proxies); Foote's factor 3 read (defined partly by mean arterial pressure, Pan-UK Biobank inputs; new note pmid-40759756), so it is the blood-pressure signal, not separate healthspan evidence; lymphocyte phased (A raises it); asked the lead whether a healthspan-class set (Foote) counts under the causal set rule. Lesson: read a factor's definition before calling a multivariate frailty set healthspan evidence.
- **26 GPR78** (2026-11-11). Tier D (seed B), a default put to the lead with B as the alternative. Deelen 2019's
  genome-wide 90th percentile hit (rs7676745 A, OR 0.67, P 4.3e-8) has a powered null in its own UK Biobank
  validation (parental 90th percentile OR 0.98, P 0.67; power about 1.00, heterogeneity P about 3e-6, or 0.0004 at half
  the effect), and LifeGen and both rare neighbours lean the other way: D22.3's flat European look-up and §4.1's
  USP42/TMTC2 example (Sebastiani 2017's genome-wide hits, null in Timmers' parental data at their published
  effects, Figure 2 source data). The 71/67 rule's "caps at B" and Deelen's caveat on phenotype and imputation panels
  read the other way; D22.3 applies by analogy only (written for a cross-ancestry null); the first D row, so asked.
  Format gap: R-TIER-1 pairs D with neutral genotypes, but the check allows all-neutral only for `contested`. Genotype states
  kept from the discovery (G/G neutral, A risk), since D is research view only; exceptional survival filed 0, not +.
  Deelen's parental longevity line is filed EXTREME_SURVIVAL_CC with `percentile_case_control_p90` (no parental
  class has a 90th percentile cut). Learned: a quote ending in "." fails when the cache runs the next word on with no
  space ("sets.Table 3"): the checker wants a non-word character after the quote, so drop the final full stop. Deelen's
  90th percentile summary statistics are GCST008598, the 99th GCST008599. Open Targets has no record of rs7676745.
- **Done: the colocalisation sweep** (2026-11-11). Queries before then returned GWAS partners only (Open Targets lists
  QTL partners only when `studyTypes` names them). Re-read with the QTL types and `isTransQtl` (trans QTLs are not
  counted), 15 rows, not the 9 first listed: the E2 rows' "no colocalisation read" needed it too. A minor rival made
  the letter of row 17 drop clear calls; asked, the lead ruled D24 (a rival counts at a tenth of the cis
  colocalisations, or passing L2G). Moved: 12 E1 KCNK3, 4 E1 NEGR1, 57 E1 CDKN2B (L2G 0.53 on Pilling's set, read
  late, so two commits), 67 E2 USP28, 81 E1 FES; 6, 15, 71 to E3. Row 7 sits at the edge (RHOC 2 of 20 over two
  sets, told to the lead). A second pass (advisor) read every lifespan-class set of
  each lead (`credibleSets-longevity8-<variant>.json`): no level moved; row 80's CHRNA5 passes L2G on Pilling's set
  (0.75) beside PSMA4's equal colocalisation, so E3 stands, worded. Cache pattern: `set-<8>-coloc-qtl[-pN]`,
  `set-<8>-l2g`.
  Lead rs9872864, its proxy rs2271961 (Rosoff's mvAge SNP; r² 0.99, D′ 1, G with T). The anchor is Wright 2019's
  maternal meta-analysis, P 6.9e-10 (Table 3, S9), with Deelen's 90th percentile an independent replication (G, P
  0.020, no UK Biobank or AncestryDNA sample): A on §4.1's letter. But Wright prints no pooled effect, so it cannot
  be a study supporting A/B (§6.3, row 93's precedent), and the only genome-wide alternative, mvAge at rs2271961,
  exists only as the GWAS Catalog's record: Rosoff's text omits it, its summary statistics are not deposited
  (GCST90321079, `full_summary_stats_available` false), the publisher refuses a scripted fetch of MOESM3 (HTTP 403),
  and a db note cannot be a study's note. Asked the lead: a D15-style allowance for a meta-analysis that prints P and
  per-arm effects but no pooled one, or MOESM3 fetched by hand. Rejected meanwhile: a generic Rosoff quote, a pooled
  β computed here (the paper's METAL P does not match an inverse-variance pool), an effect-less Wright row, tier C.
  Other calls ride with it: A on §4.1's letter against B; PROTECT absence-of-risk on a 51/49 split; C3 and E3, no gene.
- **20 RNU1-96P** (2026-11-11), tier B kept, advisor-checked. Lead rs2643826 (SLC4A7), the D16 shape of rows 4, 14
  and 15 with Timmers 2020's MANOVA beside mvAge. First `preventable` with `act_test:bp`: the blood-pressure effect is
  at the lead itself (63 catalog records, one direction; Giri 2019's record runs against the rest, its allele or sign wrong, not read).
  Rosoff's "MAF" column is the minor allele's (T here), as at 15. Timmers 2020 q11 excepts SLC4A7 from the age trend,
  so age of action stays UNKNOWN (do not reuse q2 here). E2 SLC4A7 on L2G alone; Timmers' SMR names NEK10, put to
  the lead. Open Targets' FinnGen hypertension set (SuSiE, one variant, PIP 0.995) backs C1 beyond PICS.
- **19 HMGB3P12** (2026-11-11), tier C re-tiered (seed B), advisor-checked. Lead rs78043944, Gurinovich 2021's NECS
  centenarian SNP (pmid-33948810, Supplement Table 1; the main text not open in Europe PMC, abstract and both Springer
  supplements read). `fetch-supp` could not read the supplements (an .ods named .xlsx, a .docx); the lead fixed it at
  1192b5d within the hour. The paper prints a score Z, not a β: the GWAS Catalog's and Open Targets' "beta 5.8755" is
  that Z, so the variant has no effect size. A one-variant PICS set from the reported top hit gives PIP 1 by
  construction: C1 on §4.2's letter, said as meaningless, a sharper case of the open PICS question for the lead. The
  site's frequency differs by panel (1000 Genomes EUR 0.14, gnomAD 0.007): genotype text from gnomAD, which NECS
  controls and UK Biobank agree with. Deelen fetched for all six Gurinovich leads at once (`rows-76a0cab6`): only
  row 58's 9:38322516 is in the files; 31, 41, 77 and 92 are absent too. Rows 31, 41, 58, 77 and 92 quote Supplement
  Table 1 from the cached MOESM2 the same way; Supplement Table 2 holds the LGP results for 56 SNPs.
- **18 TMEM43** (2026-11-11), tier C re-tiered (seed B) (B since the D25.13 sweep), advisor-checked. Lead rs1043943, Liu 2021's Chinese
  longevity SNP (CLHLS; Table 1 q2, T, meta 3.59e-8). First use of **R-TIER-2** (an unreplicated old-against-young
  case-control caps at C): dataset 2 sits inside the genome-wide meta-analysis, so it is no replication (its earlier
  GWAS also supplied 11,893 of dataset 1's 27,656 chip SNPs, q5; this SNP's route unread). Table 1's rs1043943 row does not reconcile (β/SE gives 0.054 and 4.8e-7
  against the printed 0.016 and 3.59e-8; Table 2's sex strata pool to 3.5e-7); kept the printed P (D17.3), said in
  the row, sent to the lead. Europe is
  an informative null: common there (T 0.40), same LD to XPC's missense rs2228001 (r² 0.94 CEU and CHB), Deelen 90th
  CI excludes Liu's β. Timmers 0.057, Zenin healthspan 0.0035 (both T): neither lifts the cap. Open Targets: allele
  order is ref T/alt C here (`3_14141910_T_C`; the C_T id returns null), so check Ensembl's allele_string for the
  reference before querying. 400 sets, 321 XPC QTLs, no longevity set: C4/E4, XPC in prose only. Liu's supplements:
  Europe PMC lists them; its `supplementaryFiles` zip downloads slowly through the proxy (the first try cut by my own
  280 s timeout at 3.4 MB; run it in the background); S2 and S16 unread. Same paper's BMPER (rs17169634) meets R-TIER-2 too.
- **17 CASP8** (2026-11-11), tier C re-tiered (seed B) (B since the D25.13 sweep), advisor-checked. Lead rs10197246, Zenin 2019's healthspan
  SNP (Table 2 q28, C 3.67e-9 GC, replicated 2.43e-4 under 0.05/12). Supplementary Data 5 and 7 cached
  (`MOESM7`, `MOESM9`; MOESM number = SD number + 2, checked against the text's citations): SD7 shows the signal is
  cancer only (9.8e-18; all-but-cancer 0.97), parents' death 0.80, own death 0.67. Timmers 0.066 (q55), Deelen
  null (q35, q36): D16 gives C. Wright S8 has nominal SNPs at 85 and 118 kb whose LD Ensembl does not return; read
  as not tags from the frequency bound (max r² = p1(1-p2)/(p2(1-p1)), about 0.19), a rule worth reusing where LD
  is missing. First QTL colocalisation read: Open Targets' `colocalisation` returns GWAS partners only unless
  `studyTypes` names the QTL types. FLACC1 meets E1's letter (L2G 0.555 + 7 eQTL colocs), CASP8 has 217 QTL colocs
  and the lead's own top QTL: filed E3, no gene, as a call for the lead. Category skin_sun (skin cancers, keratoses,
  facial ageing dominate) with mech:cancer for breast, prostate, oesophagus: also a call.
- **16 LRP1B** (2026-11-11), tier C re-tiered (seed B), advisor-checked. Lead rs117898573, Chang 2022's
  Singapore Chinese healthy-ageing GWAS (1,618 healthy agers against 6,221 survivors who were not; T 0.029, OR 2.43,
  meta P 2.59e-8; same-cohort replication of 129 cases P 0.70, uninformative, not flagged replication_failed;
  lifestyle-adjusted 1.1e-7). Rules settled: a healthy-ageing composite among survivors is HEALTHSPAN (§4.5), so with
  no lifespan study it is C under D16; an East Asian variant absent from European data is untested there, never null
  (Timmers, Zenin, Deelen all checked); first `ancestry_specific:eas` context token, which replaces
  `eur_only_evidence`; a paper's gene-level "corroboration" from European haplotypes is not a replication. The study
  is `meta_analysis` for want of a healthspan case-control design value: asked of the lead. Open Targets knows no
  variant; Chang's study (GCST90132317) has one set, at chromosome 5: C4/E4, no gene. Seed locus 32 (rs138499810) is
  the same paper's other hit.
- **15 AFF3** (2026-11-11), tier B kept: mvAge genome-wide (rs78438918, A −0.0078, P 1.1e-8). Rosoff's Table 1 frequency
  column is the MAF ("EA/OA MAF"), not the effect allele's: here A is the effect allele and the major one, so G (0.17)
  is the longer-life allele; Timmers (A −0.020, 2.0e-4), Zenin (G, 0.0027) and Deelen (null, leaning G) agree.
  Wright's Supplemental Table 9 has two fathers' SNPs on the haplotype (rs13032879 r² 0.76, in mvAge's own set;
  rs4851244 r² 0.73): AncestryDNA arm raw P 0.0068 and 0.039; their labels (G, A) are complements of the major
  allele, so the counted allele is read from the UK Biobank arm's sign against Timmers (derived). Not in S8, so no
  genomic-control P is printed; the study is entered as nominal by the raw P, and the reading is put to the lead.
  Open Targets: 19 sets, no disease; mvAge PICS PIP 0.26 (C2), L2G AFF3 0.90 (E2); grip strength sets led by the lead
  (G stronger); AFF3 eQTL in the cerebellum (G up). Open Targets' β is per alternate allele (G here), confirmed by
  the mvAge set's sign against Rosoff's. pleiotropy coined `mech:muscle_strength` and `mech:cognition` (Rosoff's
  reading, through the catalog's LD partners only).
- **14 LINC01122** (2026-11-11), tier B kept, row 4's shape (D16): mvAge genome-wide (rs980183, G −0.0063, P 1.8e-9),
  Timmers nominal (A, 2.3e-5), Zenin nominal (0.033), Deelen 90th/99th null (0.18, 0.060), all mvAge inputs. Deelen's
  GWAS Catalog summary statistics (GCST008598, GCST008599, GRCh37 `chr:pos` ids) are fetched with `--rows`; the rows
  name no rsID, so `check rows` calls them ungrained (as at row 2): accepted. They had never been read for row 4:
  row 4's C is nominal at the 90th (P 0.036), so its exceptional survival is now +. Open Targets lists 270 sets at the
  variant: page it (`page:{index:N,size:100}`) before scanning traits. No L2G on any set read: E4, gene empty. Wright's
  four mothers' SNPs: no LD returned (EUR, CEU, floor off): unknown. Actionability descriptive (glycaemia as strong as
  adiposity, the lead leads the T2D and glucose sets); put to the lead with weight and act_test:hba1c as the
  alternatives.
- **13 PRKD3** (2026-11-11), tier B kept, a fragile one: Park 2025's men-only own-survival GWAS (180,970 men,
  21,059 dead), rs577106756 A (0.1 %, at the analysis's MAF floor, imputed) reduces lifespan, β 0.09 on the
  Martingale residual, P 3.2e-8; 5e-8 applied to each of three GWAS uncorrected; not genome-wide in the whole cohort.
  FinnGen "Death" P 0.55, A β −0.07, the other way (sign fixed by rs35705950's 0.034 = "increased death"); power not
  stated, so not the red flag. Not in Timmers' summary statistics nor Deelen SD1 (untested). Open Targets has Park's
  men's study (GCST90551885) with one set, at APOE, and no variant record: C4, E4, gene empty. Ensembl LD window no
  text (2 copies in EUR): no tag known. Park's PDFs and workbooks: Europe PMC serves none; the Supplementary
  Information PDF fetches from `static-content.springer.com/esm/art%3A10.1038%2Fs41467-025-57315-6/MediaObjects/`.
  The full text keeps formulas as LaTeX blobs inside sentences: quote the blob-free runs (split on
  `\documentclass...\end{document}`) and give the number in prose. FinnGen's study row uses `own_survival_cox` as
  the nearest design (a binary endpoint) and ancestry EUR (the vocabulary has no FIN). mech:cancer is the paper's
  PheWAS in the same UK Biobank deaths; filed general_ageing. The lead (639348338): hold 25 HTT's tier until the
  adversarial read of 12's raise to A reports; write the rest of 25 meanwhile.
- **D19 (2026-11-11, 292cab8) settles 12 and 13.** 12 stays A: a replication sharing a small, measured part of the
  discovery is independent; the row says the overlap. Timmers' Figure 4 sources (Broer 2015's CHARGE and Deelen 2014)
  are mostly inside Deelen 2019 (pmid-31413261#q28): not a second test. Timmers' Ps are uncorrected (no GC; LD-score
  intercept the check, pmid-30642433#q50). A Timmers self-effect in years is already doubled: parents differ by about
  half (12 and 93's texts fixed). 13 stays B, men only; FinnGen's Death is `own_death_case_control`. 25 HTT may go
  ahead under D19.1.
- **12 KCNK3** (2026-11-11), tier A, the first seed-B row raised to A; the call is put to the lead. Lead rs1275922
  (Timmers Table 1, 6.0e-9; Pilling's rs11126666 at r² 0.99 only 4.5e-6 in UK Biobank). The only replication outside
  UK Biobank is Deelen SD1's 90th percentile (OR 1.06 per G, P 0.013; 99th 0.089; I² 36 %); Timmers' Figure 4
  look-up at rs11126666 is 0.16 one-sided, in cohorts that probably overlap Deelen's. Read as A because the notes
  already count Deelen's discovery cohorts as an outside sample and §4.1 asks p < 0.05, same allele; no row before
  this one rested A on Deelen alone (71 had LifeGen without UK Biobank beside it). 25 HTT has the same shape. Wright:
  the mothers' rs2891519 (22 kb) is CEU r² 0.06, not a tag; the fathers' rs11126491 and rs4513249 return no LD in
  EUR or CEU, floor off: unknown. When EUR pairwise is empty, the CEU pairwise call resolved rs2891519 (as at row 2);
  Ensembl's window call (`ld-window50-rs1275922.json`, r² >= 0.1) lists the close members, but an SNP absent from it
  is not thereby below 0.1; window 500 returned HTTP 500. Fig. 4's "R2" column repeats Freq1 at several rows: not r².
  Trade-off checked at the lead, rs11126666 (G pairs with the lead's G in Timmers' proxy table) and rs1731248 (C with
  G by gnomAD frequencies in NFE and EAS; the catalog record's 0.29 is an East Asian sample): the A raises BMI and
  calcium-channel-blocker use, the G lowers hypertension; no harm on G. Descriptive, not D18.2's weight: the locus
  is not mainly a weight locus (Timmers: several risk factors; the strongest record is the blocker one); put to the
  lead with the options modifiable (weight) and preventable (blood pressure, but no measured BP effect cached). C2
  (PIP 0.31 of four at r² 0.97+), E2 KCNK3 (L2G 0.85).
- **11 LINC01875** (2026-11-11), tier B kept (the lead: A's first criterion fails, D18.3; rules 3 and 4 below overruled by D18.1-2 and D17.3). Lead
  rs6744653 (Timmers Table 2): CES P 5.8e-8, suggestive (BF P 7.0e-10 not counted). The seed's rs66906321 (r² 0.89)
  reaches 2.26e-8 in Timmers' summary statistics, unreported by the paper (Table 1 omits it, q42 calls TMEM18 genome-wide
  only by the Bayesian scan; no Methods filter explains it), and mvAge 4e-8 (catalog only). AncestryDNA replicates at
  rs2867105 (r² 0.86 to the lead; Wright's A the complement of T, derived): fathers 1886-1940 P 8.8e-4, mothers 0.058,
  heterogeneity 0.18 / 0.61. Longevity look-ups null (Timmers Fig. 4 0.41; Deelen 0.21, 0.061), healthspan null.
  C4/E4, no gene (TMEM18 by mapping only). Settled with the advisor: (1) every genome-wide and replicating value
  at a proxy, with no lifespan credible set to place the lead, reads as B's "reported SNP is a tag" clause, not A,
  though A's letter is met; (2) a Wright SNP near the lead is read by position (within 0.5 Mb), not by rsID only;
  a clumped SNP whose LD Ensembl does not return is unknown, named, never "nothing contradicts"; a low-r² SNP's side
  is read from D′ and frequencies (rs4640417: the lead's A on its longer-life A, derived). Mine, put to the lead:
  (3) a lifespan allele that lowers a quantitative trait (heel bone density) is not a trade-off: a trade-off needs a
  disease (it narrows the rule that a stated-allele catalog record is a trade-off); `descriptive`, not `modifiable`,
  for an obesity locus, as at row 4. With the advisor: (4) a
  deposited summary-statistics P below 5e-8 is the study's P even when the paper does not report the SNP, with the
  omission said in statistical_test. Overruled (the lead, 639341436): the paper's own call decides genome-wide at the
  lead (D17.3); a sumstats P at a proxy the paper never reports does not meet A's first criterion.
- **The lead's batch-2 review** (2026-11-11, handoff 20261111T024120Z-review-batch2.md; D17, D18), one commit per row:
  103 to C (replication_failed; lifespan 0 as 38's shadow; exceptional survival untested; C4/E4 cite Open Targets'
  absence of the variant); 8 rewritten (rs4845625 the lifespan peak, LD predicts z 3.1 vs 2.9; Rosa's lead instrument
  rs4129267 r² 1 with the variant, MR holds without it; harmonised to C, A/C neutral, A/A risk); 2 (rs17561720 CEU
  r² 0.09, not a tag; Deelen at the lead 0.052/0.19, exceptional survival 0); 10 (suggestive at Wright's GC P;
  Deelen rows added, the proxy nominal; exceptional survival +; OBA_VT0005372); 5 harmonised; 4 modifiable through
  weight; 11 a trade-off (heel BMD), descriptive. Rules learnt: Wright's significance call is by genomic control,
  so where Wright's P decides genome-wide (row 10) the study row carries the GC P, raw P in statistical_test
  (D17.3), and so do Wright's nominal rows (8, 11, 103; the lead, 639343982: one paper reads one way across rows); Deelen's summary statistics are keyed
  by GRCh37 chr:pos, so their study rows are `ungrained` (a warning) and the note ties the position to the rsID;
  an LD pair Ensembl does not return in EUR can be tried in CEU (a subset of EUR) and said so. Ensembl's LD
  endpoints drop pairs below an r² floor by default (the lead): an empty EUR pair is fetched again with `r2=0;d_prime=0`,
  and one still empty is unknown. Done 2026-11-11 for rs3768321-rs17561720 and rs6744653-rs10153797: both still
  empty, so both stay unknown (row 2 also has CEU r² 0.09). Deelen's chr:pos `ungrained` warnings stay (the lead).
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
  `variants.csv` has `gene` optional. Applied at 67, 57 (CDKN2B) and 80 (CHRNA5/CHRNA3), each its own commit. Side effect, told to the lead: the
  `ungrained` check grains a study's quote on the rsid or the row's `gene`, so with `gene` empty only the rsid grains.
- Format gap, for the lead: a `multivariate_healthspan_lifespan` study (Timmers 2020's MANOVA) has no effect size,
  and §6.3's check requires effect_size and effect_measure on every study supporting tier A/B, so 67 carries no
  multivariate study; its P 4e-10 is in the verdict prose only.
- Zenin's healthspan summary statistics for all 228 seed rsIDs are cached (runner job 6428266):
  `pmid-30729179.supp-healthspan_summary.csv.gz.rows-1102aade.txt`, 189 of 228 found. 6's db-gwascatalog cite moved
  to it (pmid-30729179#q16, 2026-11-11).
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
Rosoff 2023 (pmid-37550455, mvAge), cited by the seed at all five, was fetched and had no note: its text names no
pilot lead (values in its supplement), so it is unread for these rows. Noted at row 2 (2026-11-11): Table 1's novel
leads only; the supplementary tables (all 52 leads) are not cached.

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
