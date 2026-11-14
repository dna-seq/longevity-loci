---
key: db-finngen-r11
database: finngen
release: "r11"
url: https://r11.finngen.fi
accessed: 2026-11-11
depth: record
---

FinnGen release 11, read from its public summary statistics (`finngen_R11_DEATH.gz`, the "Any death" endpoint,
GRCh38, cached by `loci fetch-supp` as `finngen_R11_DEATH.tsv.gz.rows-6560e735`, the rows of four variants) and its
PheWeb API (`/api/variant/...`, `/api/region/DEATH/...`). Each quote is a line as cached. `beta` is per `alt` allele on
the binary endpoint, positive more death (Park 2025 reads rs35705950's positive β as increased death,
pmid-40021682#q9). The PheWeb variant page prints the DEATH line with null values for row 36's two variants, and the
region endpoint omits them; the full file holds them.

## Reading 2026-11-11, record

> [q1] #chrom pos ref alt rsids nearest_genes pval mlogp beta sebeta af_alt af_alt_cases af_alt_controls

> [q2] 6 28445714 T C rs6902687 COX11P1 0.201707 0.695278 -0.0113305 0.00887483 0.22418 0.222456 0.224395

> [q3] 6 28443467 G A rs13190937 ZSCAN23 0.204952 0.688348 -0.0112498 0.00887511 0.224169 0.222447 0.224385

> [q4] 19 44908684 T C rs429358 APOE 1.25458e-27 26.9015 0.104773 0.00961906 0.181222 0.187179 0.180475

> [q5] 11 1219991 G T rs35705950 RP11-532E4.3 0.00597104 2.22395 0.034205 0.012441 0.102189 0.102593 0.102139

> [q6] n_case 50511 n_control 403222 n_sample NA phenocode DEATH

The DEATH file's header (q1). rs6902687, alt C (0.224 in Finns): β −0.0113 (SE 0.0089), P 0.20 (q2); its tag
rs13190937, alt A: β −0.0112 (SE 0.0089), P 0.20 (q3), Park 2025's printed value (pmid-40021682#q26). C leans to less
death, the other way from Park's UK Biobank discovery. Calibrations within FinnGen against Park's whole-cohort β
(pmid-40021682#q31, q32): APOE's rs429358 C β 0.1048 (SE 0.0096), P 1.3e-27 (q4), about 8.1 times Park's ε4 β;
MUC5B's rs35705950 T β 0.0342 (SE 0.0124), P 0.006 (q5), about 6.7 times Park's. The endpoint's 50,511 cases and
403,222 controls (q6, from the PheWeb variant page). For row 36.

## Reading 2026-11-11, record

The same file, cached again with the rows of rows 32 and 37 (`rows-d1ec483e`).

> [q7] 5 82723979 C T rs138499810 CTD-2218K11.2 0.374424 0.426636 0.02294 0.025827 0.0210922 0.0216309 0.0210247

> [q8] 6 31179699 G A rs3130507 POU5F1 0.160738 0.793882 0.0139185 0.00992341 0.167566 0.170584 0.167188

> [q9] 6 31457722 A G rs3131621 XXbac-BPG181B23.9 0.157887 0.801654 0.0113703 0.0080514 0.30421 0.308608 0.303659

Row 32's lead rs138499810 (q7): T 0.0211 in Finns, β +0.02294 (SE 0.02583), P 0.374, T toward more death, not
significant. Row 37's two seed SNPs: rs3130507 A β +0.0139 (SE 0.0099), P 0.16, so G, Pilling's longer-lived
mothers' allele, toward less death (q8); rs3131621 G β +0.0114 (SE 0.0081), P 0.16, so A, the longer-lived fathers'
allele, toward less death (q9). Neither significant.

## Reading 2026-11-11, record

> [q10] 6 34624313 A G rs6907508 ILRUN 0.110073 0.958319 0.0151637 0.00949 0.190708 0.189631 0.190843

The same DEATH file, cached again with row 39's rows (`rows-ac81c46d`; the header is q1). rs6907508, alt G (0.19 in
Finns): β +0.0152 (SE 0.0095), P 0.11, G toward more death, the side of the discovery's shorter-lived G; not
significant (one-sided 0.055, derived). Its tags rs9462007 and rs9462014 are in the same cached rows, the same signal,
not read separately.

## Reading 2026-11-11, record

The same DEATH file, cached again with row 40's rows (`rows-60700e76`; the header is q1, the counts q6).

> [q11] 6 43378065 C T rs7742789 RP5-895C5.4 0.828815 0.0815422 -0.00175461 0.0081149 0.294499 0.293681 0.294601

> [q12] 6 43385242 A G rs1214759 RP5-895C5.4 0.844638 0.0733294 0.00157441 0.00803419 0.694684 0.695409 0.694593

rs7742789, alt T (0.29 in Finns): β −0.0018 (SE 0.0081), P 0.83 (q11), T leaning very slightly toward less death,
the other way from the discovery; its tag rs1214759, alt G: β +0.0016, P 0.84 (q12), the same null. Calibrated
within FinnGen against Timmers' self-scale β (T −0.0224, pmid-30642433#q214), D25.3's two factors (derived): APOE's
(rs429358 C 0.1048 here, q4, against Timmers' 0.1056, pmid-30642433#q90; factor 0.99) predicts T +0.022, power about
0.86, heterogeneity P about 0.009: it flags. The second calibration, as D25.12 reads it for FinnGen, is a mean over
leads that hold up within FinnGen, which is not computed here, so whether this is a red flag is unknown. (Borrowing
Figure 4's mean, 0.42 of APOE's, pmid-30642433#q92, would predict +0.0093, power about 0.31, heterogeneity P about
0.18; that factor was derived for other scales and is not D25.12's.) For row 40.

## Reading 2026-11-11, record

> [q13] 6 99603422 GC G rs66927770 PRDM13 0.488506 0.31113 0.00687389 0.00992351 0.168428 0.169262 0.168324

> [q14] 6 99603424 G A rs114658003 PRDM13 0.488541 0.311099 0.00687335 0.00992352 0.168428 0.169261 0.168324

> [q15] 6 99605745 T C rs12660804 PRDM13 0.309973 0.508676 0.0126936 0.0125026 0.0976046 0.0990255 0.0974266

rs114658003, alt A (0.168 in Finns, 0.169 among the deceased and 0.168 among the others): β +0.0069 (SE 0.0099) on
death, P 0.49 (q14), A leaning toward more death, the other way from NECS (one-sided P in NECS's direction about 0.76,
derived). FinnGen holds the deletion rs66927770 beside it with the same frequency and statistics (q13), so it types
the two together. The r² 0.61 proxy's C, which rides with A: β +0.0127, P 0.31 (q15), the same lean. FinnGen's scale
differs from NECS's and D25.12's second factor is not computed, so it is not used for D21's flag. For row 41.

## Reading 2026-11-11, record

The DEATH file again, BEND3's window (`rows-610fc7c0`, GRCh38 6:107.00 to 107.10 Mb).

> [q16] 6 107079224 C A rs1627804 BEND3 0.639433 0.194205 -0.0035111 0.00749448 0.421722 0.420805 0.421837

> [q17] 6 107078153 T C rs9384641 BEND3 0.378934 0.421436 0.00675296 0.00767503 0.369487 0.373316 0.369007

rs1627804, alt A (0.42 in Finns, against 0.32 in non-Finnish Europeans): β −0.0035 (SE 0.0075) on death, P 0.64
(q16), A leaning slightly toward less death, the other way from the discovery (one-sided P in its direction about
0.68, derived). D21 under APOE's factor within FinnGen (0.99, row 40's reading): Timmers' A β −0.0157
(pmid-30642433#q28) predicts A +0.0155, one-sided power about 0.67, heterogeneity z 2.23, P about 0.026 (derived).
The power is under 0.8, so it is no red flag under that calibration, and a flag needs both (D25.3): no red flag,
whatever D25.12's uncomputed second factor gives. Wright's tag rs9384641, alt C: β +0.0068, P 0.38 (q17), C leaning
toward more death, the same reverse lean. For row 42.

## Reading 2026-11-11, record

> [q18] 6 108587315 G T rs2802292 FOXO3 0.360427 0.443183 0.00686455 0.00750592 0.579215 0.57931 0.579203

rs2802292, alt T (0.58 in Finns): β +0.0069 (SE 0.0075) on death, P 0.36, T leaning toward more death, so G toward
less, the discovery's side (one-sided P about 0.18, derived). D21 under APOE's factor within FinnGen (0.99): Timmers'
T β −0.0148 (pmid-30642433#q221) predicts T +0.0147 here, one-sided power about 0.62, heterogeneity z 0.92, P about
0.36 (derived): no red flag under that calibration, so none (D25.3). For row 43.

## Reading 2026-11-11, record

> [q19] 6	118368851	A	C	rs9320648	SLC35F1	0.53693	0.270082	-0.00458767	0.00742988	0.535374	0.534993	0.535421

> [q20] 6	118369099	C	CA	rs138527257	SLC35F1	0.179982	0.74477	0.0166488	0.012417	0.0982884	0.0990805	0.0981892

FinnGen r11's "Death" at row 44's lead (GRCh38 6:118,368,937; `finngen_R11_DEATH.tsv.gz` rows 6:118.2 to 118.4 Mb):
no line; the file runs from 118,368,851 (q19) to 118,369,099 (q20) across it, though it carries variants down to
an alternative frequency of 2.5e-5 nearby. T is absent in gnomAD's Finns (db-ensembl-116, row 44's reading).
Untested, not null.

## Reading 2026-11-11, supplement

> [q21] 6	126665850	A	G	rs1262476	VIM2P	0.284029	0.546637	0.00989393	0.00923535	0.798321	0.799601	0.798161

FinnGen r11's "Death" at row 45's lead (GRCh38 6:126,665,850; `finngen_R11_DEATH.tsv.gz`, `rows-b1d83c72`): G (alt,
0.80) β +0.0099 (SE 0.0092) on the log hazard of death, P 0.28; per A −0.0099, A's side longer-lived, one-sided
P 0.14 (derived). D21 under D25.3 (derived), Deelen's European 90th β +0.0913 (pmid-31413261#q115) carried to
Timmers' scale and into FinnGen by APOE's factor here (0.99, q4 against pmid-30642433#q90): by APOE's factor (4.84)
expected A −0.0187, one-sided power 0.65, heterogeneity P 0.39, no flag; by the loci's mean factor (0.4175) expected
−0.0447, power 1.00, heterogeneity P 0.015, a flag. A flag under one calibration only is no flag. For row 45.

## Reading 2026-11-11, supplement

> [q22] 7 4787883 T TC rs528161076,rs371933919 AP5Z1 0.380806 0.419296 0.0339197 0.0387029 0.00930656 0.00957644 0.00927275

FinnGen r11's death endpoint (`rows-ec9f8c12`, GRCh38) at row 47's AP5Z1 insertion itself, under both its rsIDs: TC
(0.0093 in Finns) log OR +0.034 for death, SE 0.039, P 0.38, so the long-lived parents' allele in Pilling leans to
more deaths here. FinnGen is independent of UK Biobank. Pilling's top-1 % effect carried by APOE's top-1 % factor (46,
pmid-27015805#q17 against pmid-30642433#q90) and into FinnGen (0.99, q4) predicts −0.72: power 1.00, heterogeneity P
3e-8. The flag holds at any factor of 6.2 or more; the loci's mean factor is not defined for this phenotype, so the
flag is unknown (D26.3). For row 47.

## Reading 2026-11-11, supplement

> [q23] 7	22728408	A	G	rs2069837	IL6	0.234042	0.630706	-0.0183747	0.0154408	0.0619421	0.060551	0.0621164

FinnGen r11's death endpoint (`rows-aade8c53`, GRCh38) at row 48's IL6 lead: G (0.062 in Finns) log OR −0.018 for
death (SE 0.015), P 0.23. G leans to fewer deaths, against Zeng's A; null. FinnGen is independent of CLHLS. For row
48.

## Reading 2026-11-11, supplement

> [q24] 7	34054385	A	G	rs17169634	BMPER	0.319216	0.495916	-0.0159799	0.0160429	0.0559885	0.0562301	0.0559582

BMPER's rs17169634 (GRCh38 7:34,054,385) in FinnGen R11's death endpoint: G −0.0160 on the log hazard of death (SE
0.0160), P 0.32; G at 0.056. G's side, one-sided 0.16 (derived): no pass. For row 49.

## Reading 2026-11-11, supplement

> [q25] 7	114608796	A	G	rs12705966	FOXP2	0.0348835	1.45738	0.0169712	0.00804434	0.313307	0.315377	0.313048

Row 50's FOXP2 lead in FinnGen R11's death endpoint (`rows-a231a0fe`, GRCh38 7:114,608,796): alt G (0.31) β +0.0170 (SE
0.0080) on the log odds of death, P 0.035: G, the allele mvAge and Timmers call healthier, goes with more deaths here,
nominal against them (one-sided P for G's side 0.98, derived). D21 under APOE's factor within FinnGen (0.99, row 40's
reading, q4 against pmid-30642433#q90): Timmers' G +0.0133 (pmid-30642433#q236) predicts G −0.0132, one-sided power
0.50, heterogeneity P about 9 × 10⁻⁴ with both SEs (derived); power is below 0.8, so no red flag under the larger factor, and Figure 4's
mean (0.4175 of APOE's) gives less (−0.0055, power 0.17, heterogeneity P 0.006). D25.12's within-FinnGen mean is not
computed and could only lower the power. FinnGen is independent of UK Biobank and LifeGen; most of Timmers 2022's
survival look-up at this SNP is these people (pmid-37118362#q58). For row 50.

## Reading 2026-11-11, supplement

> [q26] 7	130045757	G	A	rs56179563	ZC3HC1	0.460487	0.336783	-0.00574237	0.0077805	0.354038	0.354537	0.353976

Row 51's ZC3HC1 lead in FinnGen R11's death endpoint (`rows-a0540331`, GRCh38 7:130,045,757): alt A (0.35) β −0.0057
(SE 0.0078) on the log odds of death, P 0.46: A, Timmers' lifespan-raising allele, leans to fewer deaths, one-sided
0.23 (derived), no pass. D21 under APOE's factor within FinnGen (0.99, row 40's reading): Timmers' A +0.0211
(pmid-30642433#q239) predicts A −0.0209, one-sided power 0.85, heterogeneity P 0.084 with both SEs (derived); the
power bar is met but heterogeneity is not below 0.05, so no red flag. Figure 4's mean (0.4175 of APOE's) predicts
−0.0087, power 0.30, heterogeneity P 0.71. rs11556924 (alt T): β −0.0035 (SE 0.0079), P 0.66, the same side. For
row 51.

## Reading 2026-11-11, supplement

> [q27] 8	19956018	A	G	rs268	LPL	0.548986	0.260439	0.0148558	0.0247893	0.0225557	0.0231222	0.0224847

FinnGen R11's death endpoint (GRCh38), rs268: ref A, alt G, β +0.0149 per G (SE 0.0248), P 0.55, one-sided 0.27 on
A's side (derived); G 0.023 in Finland. The expected size, from Timmers' β (pmid-30642433#q244) under APOE's
within-FinnGen factor 0.99: −0.065 per A, power 0.84, heterogeneity P 0.080 with both SEs; under Figure 4's mean
factor power 0.29, P 0.63. Below D21's line (heterogeneity P not below 0.05), no red flag. For row 52.

> [q28] 8	19967156	C	T	rs15285	LPL	0.314307	0.502646	-0.00851573	0.00846305	0.257011	0.257894	0.2569

rs15285: ref C, alt T, β −0.0085 per T (SE 0.0085), P 0.31, one-sided 0.16 on T's side; under APOE's factor power
0.66, heterogeneity P 0.35. Not nominal; the second signal's, prose only. For row 52.

## Reading 2026-11-11, supplement

> [q29] 8	27584547	G	A	rs7844965	GULOP	0.0229652	1.63893	-0.0200234	0.0088053	0.23089	0.22783	0.231273

FinnGen R11 death endpoint (`rows-e90def79`), rs7844965 at 8:27,584,547 (GRCh38): alt A, β −0.0200 (SE 0.0088) on the
log odds of death, P 0.023, A 0.231; nearest gene GULOP. A goes with fewer deaths: one-sided P 0.011 (derived), a
nominal replication outside UK Biobank. Under D21 with APOE's factor within FinnGen (0.99, q4 over
pmid-30642433#q90) Pilling's +0.0303 expects A −0.030, power 0.96, heterogeneity P 0.33; the mean factor gives power
0.41, P 0.41: consistent, no flag. For row 53.

## Reading 2026-11-12, supplement

> [q30] 8	30981030	T	G	rs11783562	RP11-293D9.2	0.00102094	2.991	-0.0244255	0.00743616	0.525952	0.521527	0.526507

FinnGen R11 death endpoint (`rows-41171935`), rs11783562 at 8:30,981,030 (GRCh38): ref T, alt G, β −0.0244 (SE
0.0074) on the log odds of death, P 0.0010, G 0.526 (cases 0.522, controls 0.527); 50,511 deaths against 403,222
controls (q6). G goes with fewer deaths, one-sided P 0.0005 (derived): a nominal replication outside AncestryDNA and
UK Biobank, the row's one independent support. The PheWeb region endpoint gives the same line
(`death-8_30981030.json`). For row 54.

## Reading 2026-11-12, supplement

FinnGen r11's "Death" at row 55's insertion (GRCh38 8:54,566,349; `finngen_R11_DEATH.tsv.gz`, `rows-05b389a0`).

> [q31] 8	54566349	G	GCT	rs35262860,rs398112480	RP1	0.96925	0.0135643	0.000309972	0.00804093	0.311675	0.312967	0.311513

GCT (alt, 0.31) β +0.00031 (SE 0.0080) on the log hazard of death, P 0.97: flat, one-sided 0.52 against the
discovery (derived). D21 under D25.3 (derived), Deelen's 90th per insertion +0.1028 (pmid-31413261#q146) carried to
Timmers' scale and into FinnGen by APOE's factor here (0.99, q4 against pmid-30642433#q90): by APOE's factor
expected −0.0211, one-sided power 0.84, heterogeneity P 0.018; by the loci's mean factor −0.0505, power 1.00,
heterogeneity P 7e-5, or 0.003 counting the mean's SE. A red flag under both. No UK Biobank; overlap with Deelen's
Finnish cohort Vitality 90+ (pmid-31413261#q149) unknown, and any overlap would favour agreement. For row 55.

## Reading 2026-11-12, supplement

> [q32] 8 58925574 A G rs13262617 TOX 0.542774 0.265381 0.0122139 0.0200681 0.0361168 0.0355734 0.0361848

FinnGen R11 death endpoint (`rows-d05d9439`), rs13262617 at 8:58,925,574 (GRCh38): alt G (0.036), β +0.0122 (SE
0.0201) on the log hazard of death, P 0.54: G, the discovery's longer-lived allele, leans to more deaths (one-sided
0.73 against the discovery, derived). D21, Timmers' scale into FinnGen by APOE's factor (0.99, q4 over
pmid-30642433#q90) and the loci's mean factor (derived): from the fathers' 0.0824, APOE power 0.99, heterogeneity P
1.6e-4, mean power 0.52 (P 0.027), so no flag; from a both-parents 0.029 to 0.042 (pmid-30642433#q254), APOE power 0.42 to 0.66, no flag. No UK
Biobank. For row 56.

> [q33] 9	38322519	G	T	rs10973748	RP11-113O24.3	0.766757	0.115342	0.00478869	0.0161442	0.0551319	0.0572405	0.0548678

FinnGen R11 death endpoint (`rows-f70b6fb7`), rs10973748 at 9:38,322,519 (GRCh38): alt T 0.055, β +0.0048 (SE
0.0161), P 0.77: T, NECS's long-lived allele, leans to more deaths (one-sided 0.62 against, derived). D21 (derived),
NECS's log OR into Timmers' scale (pmid-30642433#q255) and into FinnGen by −0.99: under APOE's factor expects −0.070,
power 1.00, heterogeneity P 2e-4; at half, power 0.70, no flag. The mean factor enters twice, NECS into Timmers' scale
and Timmers' into FinnGen, and cancels: one conversion. A flag at full effect. For row 58.

## Reading 2026-11-12, supplement

> [q34] 9	133266456	T	C	rs977371848	ABO	0.434572	0.361938	-0.00719583	0.009209	0.797072	0.796916	0.797092

FinnGen R11 death endpoint (`rows-34c921c6`), GRCh38 9:133,266,456 T>C, row 59's lead rs2519093 by position and alleles
(the file names it rs977371848): alt C 0.80, β −0.0072 (SE 0.0092) on the log odds of death, so C with fewer deaths, P
0.43 (one-sided 0.22). D21 (derived), Timmers' β per C × −0.99: expects −0.022, power 0.78, heterogeneity P 0.15 under
APOE's factor; −0.0093, power 0.26, P 0.83 under the mean factor: no red flag. For row 59.

## Reading 2026-11-12, supplement

> [q35] 9	135376756	G	A	rs75824829	RP11-555H7.2	0.143128	0.844274	0.0443916	0.0303172	0.015967	0.0165589	0.0158929

FinnGen R11 death endpoint (`rows-1ce2da39`), rs75824829 at 9:135,376,756 (GRCh38): ref G, alt A, β +0.0444 (SE 0.0303) on the log odds of death, P 0.14, A 0.016 (cases 0.0166, controls 0.0159); 50,511 deaths (q6). A leans to more deaths, against Pilling's direction; independent of UK Biobank. For row 60.

## Reading 2026-11-12, supplement

> [q36] 10	11118452	C	T	rs547541271	CELF2	0.932537	0.030334	-0.0176491	0.208487	0.000314074	0.000333067	0.000311695

FinnGen R11's any-death endpoint at rs547541271 (GRCh38 10:11,118,452; `finngen_R11_DEATH.tsv.gz` rows 10:11.108 to
11.130 Mb): T log OR −0.0176 (SE 0.208), P 0.93, T 0.03 % (Park's own look-up, pmid-40021682#q38). D21 (derived):
like for like, Park's whole-cohort T +0.0147 (pmid-40021682#q54) under APOE's Park-to-FinnGen factor 8.1 (q4 against
pmid-40021682#q32) expects +0.12, power 0.14; the women's +0.0369, the generous bound, expects +0.30, power 0.42,
heterogeneity P 0.13; MUC5B's factor 6.7 gives less. 80 % power needs a factor of 14 on the women's effect. No
calibration raises a flag, so D25.3's mean factor is not needed: no red flag. For row 61.

## Reading 2026-11-12, supplement

> [q37] 2	37257437	G	A	rs577106756	PRKD3	0.54652	0.262394	-0.0660254	0.109498	0.00127138	0.00107412	0.00129609

FinnGen R11's any-death endpoint at rs577106756 (GRCh38 2:37,257,437; `finngen_R11_DEATH.tsv.gz`, the row filter
`^2\t37257437\t`): A log OR −0.066 (SE 0.109), P 0.55, A 0.13 % (Park's own look-up, pmid-40021682#q15). A is about
as common here as in UK Biobank. D21 (derived), like for like: Park's whole-cohort A +0.042 (SE 0.0095,
pmid-40021682#q61) under APOE's Park-to-FinnGen factor 8.1 (q4 against pmid-40021682#q32) expects +0.34, power 0.93,
heterogeneity P 0.002 (both standard errors; 0.0002 on FinnGen's alone); under MUC5B's 6.7 (q5 against
pmid-40021682#q31), +0.28, power 0.83, heterogeneity P 0.006. Both flag. D25.3's mean factor is unknown for this
look-up (D25.12: with PRKD3 and CELF2 left out, MUC5B alone is not a mean), so the flag is unknown and sets no token
(D26.3). The men's +0.088 would flag at any of these factors. For row 13.

## Reading 2026-11-12, supplement

> [q38] 10	90207407	T	G	rs11186068	LINC01374	0.377325	0.423284	0.0505537	0.0572629	0.00417764	0.00448483	0.00413916

FinnGen R11's any-death endpoint at rs11186068 (GRCh38 10:90,207,407; `finngen_R11_DEATH.tsv.gz`, the row filter `^10\t90207407\t`): G log OR +0.051 for death (SE 0.057), P 0.38, G 0.42 %: G leans to more deaths, against Beccacece's direction. For row 62.

## Reading 2026-11-12, supplement

> [q39] 10	112995025	T	C	rs35198068	TCF7L2	0.0346729	1.46001	0.0195382	0.00925035	0.202042	0.206557	0.201476

FinnGen R11's any-death endpoint (`rows-e785b41f`, the filter `^10\t11299[0-9]{4}\t`), rs35198068 at GRCh38 10:112,995,025: C (alt) log OR +0.0195 (SE 0.0093) for death, P 0.035, C at 0.202 (cases 0.2066, controls 0.2015). T lowers the odds of death, one-sided 0.017 (derived); independent of UK Biobank. rs34872471 and rs7903146 give the same (P 0.035, 0.031). From LifeGen's T +0.0060 (pmid-30642433#q276; APOE's factor to FinnGen 0.99, q4 against pmid-30642433#q90) the expected T log OR is about −0.006, so the observed −0.0195 passes; a ratio of APOE's lines from Zenin's healthspan scale (pmid-30729179#q89) would expect about −0.47, the curator's own conversion (D28.1). For row 63.

## Reading 2026-11-12, supplement

> [q40] 11 202785 T C rs76612380 BET1L 0.572436 0.242273 0.0201862 0.0357616 0.0135301 0.0135888 0.0135228

FinnGen R11's "Any death" file (`finngen_R11_DEATH.tsv.gz.rows-282537d8`; the region API omits the variant),
rs76612380: C at 1.35 %, log OR +0.020 (SE 0.036) for death, P 0.57: C leans to more death, one-sided 0.29 (derived).
For row 64.

> [q41] 11 202835 A G rs79902640 BET1L 0.240074 0.619654 0.0304517 0.0259207 0.0211529 0.0215727 0.0211003

rs79902640's G (2.1 %): +0.030 (SE 0.026), P 0.24. For row 64.

> [q42] 11 203788 C T rs2280543 BET1L,RP11-304M2.5 0.304043 0.517065 0.0262153 0.0255062 0.0216407 0.0220204 0.0215932

rs2280543's T (2.2 %): +0.026 (SE 0.026), P 0.30. All three lean the minor haplotype toward death. For row 64.

## Reading 2026-11-12, supplement

> [q43] 11	43770315	G	A	rs4755737	HSD17B12,RP11-472I20.4	0.0389171	1.40986	-0.0153214	0.00741936	0.491109	0.487459	0.491566

FinnGen R11's "Any death" file (`finngen_R11_DEATH.tsv.gz.rows-0afd56a6`), rs4755737: A at 49 %, log OR −0.0153
(SE 0.0074) for death, P 0.039: A with fewer deaths, one-sided 0.019 (derived). Outside AncestryDNA and UK Biobank.
rs4755202 reads the same way (A −0.0148, P 0.048). For row 65.

> [q44] 10	90237320	C	G	rs151047665	LINC01374	0.208513	0.680866	0.0755015	0.0600332	0.00379864	0.00411978	0.00375841

FinnGen R11's death endpoint (`rows-7a7d9270`) at rs151047665, a CEU proxy of row 62's lead: its rare G +0.076 log
OR for death (SE 0.060), P 0.21. FinnGen holds 20 of the lead's 21 CEU proxies (not rs111444455), and each puts the rare allele, the lead's G's
partner, on the side of more deaths, as at the lead (q38), none nominal (best P 0.21, this line); rs7093821's second alternative allele, T at 0.19 %, is another variant and leans the other way (P 0.37). For row 62, prose.

## Reading 2026-11-12, supplement

> [q45] 11 89284793 G A rs1126809 TYR 0.788052 0.103445 -0.00261329 0.00972061 0.177574 0.178381 0.177473

FinnGen R11's any-death endpoint (`rows-c74cfa48`), rs1126809 at GRCh38 11:89,284,793: A at 0.178, log OR −0.0026
(SE 0.0097) for death per A, P 0.79: flat, A's sign a hair to fewer deaths, against the healthspan direction. For row 66.

## Reading 2026-11-12, supplement

> [q46] 11 119399248 G A rs139137459 USP2-AS1 0.748855 0.125602 -0.0292033 0.0912176 0.00160096 0.00163094 0.0015972

FinnGen R11 DEATH (`rows-ce519916`), rs139137459 (GRCh38 11:119,399,248): alt A at 0.0016 (cases 0.00163, controls
0.00160), β −0.029 (SE 0.091), P 0.75: A on the fewer-deaths side, flat (one-sided 0.37, derived). For row 68.

## Reading 2026-11-12, supplement

> [q47] 12 49591427 G A rs11169081 FAM186B,PRPF40B 0.791737 0.101419 -0.00295224 0.0111804 0.125957 0.125066 0.126068

FinnGen R11 DEATH, read by position (`rows-63136947`): no line for rs55686423 (GRCh38 12:49,569,751; neither the
rsID filter, `rows-5155709c`, nor the position finds it, though T is 0.097 in gnomAD's Finns, db-ensembl-116#q507).
Its tag rs11169081 (GRCh38 12:49,591,427, r² 0.83-0.88 to the lead, db-ensembl-116#q511, q512): alt A at 0.126, β
−0.0030 (SE 0.011), P 0.79: A, which rides with the lead's T, on the fewer-deaths side, flat (one-sided 0.40,
derived). For row 69.

## Reading 2026-11-12, supplement

> [q48] 12 95187042 T G rs12830425 FGD6 0.283625 0.547256 -0.014635 0.0136493 0.0795774 0.0790604 0.0796422

FinnGen R11 DEATH (`rows-2aa4ffe6`), rs12830425 (GRCh38 12:95,187,042): alt G at 0.080, β −0.0146 (SE 0.0136), P
0.28: G on the fewer-deaths side, not nominal (one-sided 0.14, derived). For row 70.

## Reading 2026-11-12, supplement

> [q49] 13 18865983 C G rs2440012 ANKRD20A9P 0.758017 0.120321 -0.00292698 0.00950053 0.193636 0.195645 0.193384

FinnGen R11 DEATH, rs2440012 (GRCh38 13:18,865,983), alt G at 0.19: β −0.0029 (SE 0.0095), P 0.76; G on the
fewer-deaths side, flat, against Zeng's (one-sided for C 0.62, derived). A separate C/A line is not read. For row 72.

## Reading 2026-11-12, record

> [q50] 13 33054001 T G rs9536314 KL 0.530451 0.275355 0.00581862 0.00927538 0.198429 0.199372 0.19831

FinnGen R11 DEATH at rs9536314 (GRCh38 13:33,054,001), row 73: G (0.198) beta +0.0058 (SE 0.0093), P 0.53, G with
slightly more deaths, flat (q50). For row 73.

## Reading 2026-11-12, record

> [q51] 13 64262356 T C rs61949650 LINC00355 0.22351 0.650704 0.0203245 0.0166971 0.0520708 0.0523171 0.05204

FinnGen R11 DEATH at rs61949650 (GRCh38 13:64,262,356), row 74 (q51): C (0.0520) beta +0.020 (SE 0.017), P 0.22, C
with slightly more deaths, against the discovery's side, not significant; nearest gene LINC00355. For row 74.

## Reading 2026-11-12, record

> [q52] 13 73649403 C CTT rs573195248 LINC00393 0.262924 0.58017 0.00831401 0.00742649 0.464643 0.464286 0.464688

FinnGen R11 DEATH, row 75: at GRCh38 13:73,649,403 C/CTT (q52), labelled rs573195248, matched to the seed's
rs35257605 by position and alleles (the repeat's 15-T allele; CTT at 0.46 here against 0.43 in gnomAD's non-Finnish
Europeans): CTT beta +0.0083 (SE 0.0074), P 0.26, CTT with slightly more deaths, against Park's lean, flat.
rs116257533 has no line. For row 75.

## Reading 2026-11-13, record

> [q53] 14 74855011 T C rs61978928 PROX2,YLPM1 0.178852 0.747507 0.0103069 0.00766713 0.370724 0.373486 0.370379

FinnGen R11 DEATH at rs61978928 (GRCh38 14:74,855,011), row 76 (q53): C (0.37) β +0.0103 (SE 0.0077), P 0.18, C with
slightly more deaths, against the discovery, flat; nearest genes PROX2, YLPM1. For row 76.

## Reading 2026-11-13, supplement

> [q54] 15 41138771 T A rs28455998 RP11-129I12.3 0.452904 0.343994 -0.00580089 0.00772852 0.362903 0.362072 0.363008

> [q55] 15 41151726 A G rs3959554 RP11-129I12.3 0.635561 0.196843 -0.00377446 0.00796442 0.321189 0.320924 0.321222

FinnGen R11 death at row 78's lead (q54): alt A β −0.0058 (SE 0.0077) on the log odds of death, P 0.45, so T with
slightly more deaths, one-sided for T about 0.77 (derived): against, flat. At rs3959554 (q55): G −0.0038, P 0.64, the
same lean (G travels with the lead's A). For row 78.

## Reading 2026-11-13, supplement

> [q56] 15 47367997 G A rs74011415 CTD-2050N2.1,SEMA6D 0.870558 0.0602025 0.00157774 0.00968233 0.177342 0.176769 0.177414

FinnGen R11 death at row 79's lead (q56): alt A β +0.0016 (SE 0.0097) on the log odds of death, P 0.87, so G with
slightly fewer deaths, flat; A at 0.177 in FinnGen. For row 79.

## Reading 2026-11-13, supplement

> [q57] 16 52537524 A C rs4783780 TOX3 0.00579442 2.23699 0.0206528 0.00748508 0.422698 0.426368 0.422238

> [q58] 16 52565276 C T rs4784227 CASC16 0.0423253 1.3734 0.0173036 0.00852263 0.250958 0.253668 0.250619

FinnGen R11 death at row 82's locus. rs4783780 (q57): alt C β +0.0207 (SE 0.0075) on the log odds of death, P 0.0058,
so A with fewer deaths. rs4784227 (q58): alt T +0.0173 (SE 0.0085), P 0.042. A database line (D29.1). For row 82.

## Reading 2026-11-13, supplement

> [q59] 16 53767042 T C rs1421085 FTO 0.249221 0.603415 -0.00864473 0.00750252 0.418328 0.416157 0.4186

FinnGen R11 death at rs1421085 (q59): alt C β −0.0086 (SE 0.0075), P 0.25, so C with slightly fewer deaths: against
T, flat. For row 83.

## Reading 2026-11-13, supplement

> [q60] 16 56959412 C A rs3764261 CETP 0.0870342 1.06031 -0.0141105 0.00824573 0.278618 0.277925 0.278705

> [q61] 16 56982180 G A rs5882 CETP 0.280136 0.552631 -0.00824457 0.00763377 0.617217 0.614764 0.617524

FinnGen R11 death at CETP, row 84: rs3764261 (q60) alt A β −0.0141 (SE 0.0082), P 0.087, A with fewer deaths
(one-sided 0.044, derived); rs5882 (q61) alt A −0.0082, P 0.28. A database line (D29.1). For row 84.

## Reading 2026-11-13, supplement

> [q62] 16 72041694 A T rs12924886 TXNL4B 0.691484 0.160218 0.00370897 0.00934617 0.193543 0.19555 0.193292

FinnGen R11 death at rs12924886 (q62): alt T β +0.0037 (SE 0.0093), P 0.69: A with slightly fewer deaths, flat. For
row 85.

## Reading 2026-11-13, supplement

> [q63] 16 89960104 T C rs4268748 DEF8 0.781369 0.107144 0.00239805 0.00864049 0.245536 0.247054 0.245346

FinnGen R11 death at rs4268748 (q63): alt C β +0.0024 (SE 0.0086), P 0.78: flat. For row 86.

## Reading 2026-11-13, record

> [q64] 17 42111440 T C rs34891485 DHX58 0.481588 0.317324 -0.0106575 0.0151439 0.064675 0.0633611 0.0648396

FinnGen R11's death endpoint at rs34891485 (q64): alt C (0.065 in Finns) β −0.0107 (SE 0.0151), P 0.48: C with
slightly fewer deaths, so T leans to more, one-sided 0.24 against T (derived), flat. Against Timmers' T +0.0453
under APOE's within-FinnGen factor (0.99): power 0.91, heterogeneity P 0.0016; under the mean factor power 0.34, P
0.060: one calibration only, no D21 red flag (derived). For row 87.

## Reading 2026-11-13, record

> [q65] 17 49068486 T C rs940088 IGF2BP1 0.192983 0.71448 -0.0104175 0.00800237 0.31594 0.315412 0.316007

FinnGen R11's death endpoint at rs940088 (q65): alt C (0.316 in Finns) β −0.0104 (SE 0.0080), P 0.19: C with fewer
deaths, one-sided 0.096 C's way (derived), flat. Against Timmers' C +0.0171: APOE's within-FinnGen factor power 0.68,
heterogeneity P 0.47; the mean factor power 0.22: no flag. For row 88.

## Reading 2026-11-13, record

> [q66] 17 82727657 C T rs1046896 FN3KRP 0.947215 0.0235514 0.000558895 0.00844198 0.264542 0.263413 0.264683

FinnGen R11's death endpoint at rs1046896 (q66, row 89): alt T (0.26) β −0.0006 (SE 0.0084), P 0.95: flat. For row 89.

## Reading 2026-11-13, record

> [q67] 18 13886720 G A rs28926173 MC2R 0.852988 0.0690572 -0.00371042 0.020023 0.0356129 0.035228 0.0356611

FinnGen R11's death endpoint at rs28926173 (q67, row 90): alt A (0.036 in Finns) β −0.0037 (SE 0.020), P 0.85: flat.
For row 90.

## Reading 2026-11-14, record

> [q68] 18 60183864 T C rs17782313 RP11-795H16.2 0.240429 0.619014 0.0111587 0.00950553 0.184975 0.187216 0.184694

FinnGen R11's death endpoint at rs17782313 (q68, row 91): alt C (0.185 in Finns) β +0.0112 (SE 0.0095), P 0.24: C with
slightly more deaths, so T fewer, flat (one-sided 0.12). For row 91.

## Reading 2026-11-14, supplement

> [q69] 19 32967289 T C rs62127361 CEP89 0.896142 0.0476231 0.00176935 0.0135544 0.0818786 0.0818017 0.0818882

FinnGen R11's death endpoint, row 94: no line at rs62127362 (GRCh38 19:32,967,573), so its neighbour rs62127361 (284
bases away, r² 0.94 and D′ 1.00 in CEU, db-ensembl-116#q693) stands in (D29.3); its C, alt, is the minor allele with
the lead's C (Deelen's 90th prints it at 0.88 for T with the lead's effect, pmid-31413261#q232's neighbour 33,458,195).
Alt C (0.082 in Finns) β +0.0018 (SE 0.0136) on death, P 0.90: flat, G a hair towards fewer deaths (one-sided 0.45,
derived). Against Deelen's European 90th effect carried over as for Timmers (pmid-30642433#q348): APOE's factor
predicts G −0.032 on death, one-sided power 0.77, heterogeneity P 0.041; the mean factor −0.077, power 1.00, P 1.7e-4.
A flag under the mean factor only, so no flag (D25.3, as row 45's FinnGen), Timmers' β is already per self (D30.16), so this
expectation is the per-self one; the doubled restatement of 2026-11-14 (a flag under both) is withdrawn. A database
line sets no D (D30.12). Independent of Deelen
and UK Biobank. For row 94.

## Reading 2026-11-14, supplement

> [q70] 19 40835324 A G rs12461964 CTC-490E21.10,CTC-490E21.12 0.285696 0.544096 -0.00802801 0.0075196 0.547295 0.540404 0.548158

FinnGen R11's death endpoint at rs12461964 (q70, row 95): alt G (0.54 in Finns) β −0.0080 (SE 0.0075), P 0.29: G with
slightly fewer deaths, against A (one-sided 0.14 against A, derived). A sex-combined sample, so tested on
Pilling's both-parents effect (D28.2), at the factor Timmers' Figure 2 sheet uses for both-parents results (about
1.97; D30.16, correcting the fathers' 2.287 first used here): expected +0.0166 per A per self (SE 0.0044), one-sided
power 0.71, so no flag (D21). A database line sets no D (D30.12). All derived. For row 95.

## Reading 2026-11-14, supplement

> [q71] 20 10983718 T C rs6108784 RP11-103J8.1 0.539345 0.268133 0.00472896 0.00770436 0.365813 0.368304 0.365501

FinnGen R11's death endpoint at rs6108784 (q71, row 97): alt C (0.37 in Finns) +0.0047 (SE 0.0077), P 0.54 (corrected
2026-11-14: the first reading swapped the P and frequency columns): T with slightly fewer deaths, one-sided 0.27,
flat. Against Pilling's both-parents effect at Timmers' both-parents factor (about 1.97, D30.16: +0.0152 per T per
self): power 0.63, heterogeneity P 0.24, no flag; a database line sets no D either way. Derived. For row 97.

## Reading 2026-11-14, supplement

> [q72] 20 32511508 T C rs159428 NOL4L,RP5-1184F4.7 0.0110428 1.95692 0.0196161 0.0077188 0.636042 0.638093 0.635785

FinnGen R11's death endpoint at rs159428 (q72, row 98): alt C (0.64 in Finns) β +0.0196 (SE 0.0077), P 0.011: C with
more deaths, T with fewer, one-sided 0.0055 (derived); outside UK Biobank. A database release line: it never
replicates (D12, D30.12). For row 98.

## Reading 2026-11-14, supplement

> [q73] 20 63355597 T C rs2273500 CHRNA4 5.93458e-09 8.22661 0.0521067 0.00895521 0.217358 0.221944 0.216783

> [q74] 20 63810246 A T rs6062322 ZBTB46,ZBTB46-AS1 0.56219 0.250117 0.00563339 0.00971959 0.178265 0.178964 0.178177

FinnGen R11's death endpoint at rs2273500 (q73, row 99): alt C (0.22 in Finns) β +0.0521 (SE 0.0090), P 5.9e-9: C
with more deaths, T with fewer, genome-wide, outside UK Biobank. A database release line: it never replicates (D12,
D30.12), so it is named, not counted. rs6062322 (q74): flat, P 0.56. For row 99.
