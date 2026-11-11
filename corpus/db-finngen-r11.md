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
