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
