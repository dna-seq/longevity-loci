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
  adjust pacing and go next 10 and so on unless blocked or I steer"; this replaces the earlier pause after ten). Rows done in this run: 6 CELSR2 (1 of 10), 38 HLA-DQA1 (2 of 10), 81 FES/FURIN (3 of 10), 103 (4 of 10), 2 PABPC4 (5 of 10), 4 LINC02796 (6 of 10), 5 FPGT / TNNI3K (7 of 10), 7 MAGI3 (8 of 10), 8 IL6R Asp358Ala with 157 (9 of 10); 10 RABGAP1L (10 of 10); second run: 11 LINC01875 (1 of 10), then the lead's review of 103, 8, 2, 10 with 5, 4 and 11 under D17/D18 (one commit each, not counted as rows); 6's healthspan re-cited to Zenin's cached file (597d9fb); 103 re-tiered B under D16 (5abae88); the Open Targets quotes re-quoted from cached records (f69c8d8); the corrections of 71 (d44fd4a) and 67 (3dd792c) done, the E3 gene rule at 57 (8d27300) and 80 (728d78d), 67's MANOVA study added under D15 (a519ae4); 38 corrected again at 103 (the AncestryDNA tag is shared); next 96 APOE waits on D2, so the seed tier B by locus_id.
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
- **2 PABPC4** (2026-11-11), tier C re-tiered (seed B), the first mvAge-only locus. Rosoff 2023 Table 1: rs3768321
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
  (D17.3); rows 8, 11 and 103 still carry Wright's raw P on nominal results, asked of the lead; Deelen's summary statistics are keyed
  by GRCh37 chr:pos, so their study rows are `ungrained` (a warning) and the note ties the position to the rsID;
  an LD pair Ensembl does not return in EUR can be tried in CEU (a subset of EUR) and said so. Open (the
  advisor): no cached Ensembl LD record shows r² below 0.05, so an empty pair may mean "below a reporting floor"
  rather than unknown; until the endpoint's floor is read, rows 2 and 11 keep "unknown".
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
