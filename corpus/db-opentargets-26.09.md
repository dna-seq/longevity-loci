---
key: db-opentargets-26.09
database: opentargets
release: "26.09"
url: https://api.platform.opentargets.org/api/v4/graphql
accessed: 2026-11-10
depth: record
---

Open Targets Platform, release 26.09 (the API's `meta.dataVersion`), read through its GraphQL API. Each record
named in the prose is cached by `loci fetch-supp` (RM3) as `variant-<id>.json` or `credibleset-<studyLocusId>.json`,
one object a line, and each quote is that record's line as cached: a frequency line, or a credible-set member (its
PIP and r² to the set's lead, then the variant) or a locus-to-gene score (then its gene) as two lines joined. q1-q35
were first written as `field: value` before the records could be cached (D12), and re-quoted from the cached
records on 2026-11-11 with the same values.

## Reading 2026-11-10, record

Variant 6_160589086_A_G (rs10455872, LPA), `alleleFrequencies` (gnomAD, as Open Targets carries it; the frequency
is of the alternative allele G, the Lp(a)-raising one):

> [q1] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.06944975443343235

> [q2] data.variant.alleleFrequencies[5] populationName eas_adj alleleFrequency 0.000969743987587277

> [q3] data.variant.alleleFrequencies[9] populationName afr_adj alleleFrequency 0.012147599345713462

So G is about 7% in non-Finnish Europeans, 1% in Africans and 0.1% in East Asians: the tag does not carry Lp(a)
outside Europeans the way it does within (`ancestry_tag`).

Credible set 9a28de1c1982a3eb082610008a3fd828, study GCST009890 (Timmers 2019, "Parental lifespan"), PICS, four
variants, lead 6_160589086_A_G:

> [q4] data.credibleSet.locus.rows[0] posteriorProbability 0.3814318249801707 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 6_160589086_A_G

PIP 0.38: in a 95% credible set at 0.1 to 0.5, `causal:C2`. The other three members: 6_160576086_A_T 0.252,
6_160564494_G_A 0.227, 6_160584578_C_T (rs55730499) 0.139. The same lead holds PIP 0.40 in the multivariate study
GCST011100 (Timmers 2020), and rs55730499 leads Pilling 2017's set (GCST006697, SuSiE-inf) with rs10455872 at 0.32.

> [q5] data.credibleSet.l2GPredictions.rows[0] score 0.5594255924224854 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol LPA

The locus-to-gene score of LPA on that credible set (next PLG 0.341): L2G ≥ 0.5, `effector:E2`. E1 would also need a
cis-QTL colocalisation for LPA, not read here (the set has 1,391 colocalisations of every kind; not sorted).

Variant 19_11079858_G_A (rs142158911, LDLR), `alleleFrequencies`, of the alternative allele A (the lifespan-raising
one):

> [q6] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.11544578952019087

A is about 12% in non-Finnish Europeans, as Timmers 2019 has it (0.12). Other ancestries are not used: the African
figure (afr_adj 0.1875, exactly 3/16) is a sample too small to quote.

Credible set 03c517952394bc1997c99049d239a442, study GCST009890 (Timmers 2019, "Parental lifespan"), PICS, lead
19_11079858_G_A, about fifty members each with PIP under 0.04:

> [q7] data.credibleSet.locus.rows[0] posteriorProbability 0.035171205149789796 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 19_11079858_G_A

PIP 0.035: in the set, below 0.1, `causal:C3`. The signal is spread over a long LD block; no member stands out.

> [q8] data.credibleSet.locus.rows[33] posteriorProbability 0.01737606683859661 r2Overall 0.9559867534825262 is95CredibleSet true data.credibleSet.locus.rows[33].variant id 19_11091630_G_T

rs6511720 (19_11091630_G_T), Timmers 2020's, Pilling 2017's and Wright 2019's lead at LDLR, is in the same set at
r² 0.956 to the lead (PIP 0.017): the same signal, `ld_proxy_of:rs142158911`. Timmers 2020's multivariate study
GCST011100 has its own set here (6bf8fa2e5bdd96ea48ee4bc9856fdc7d, PICS, 49 members) led by rs6511720 at PIP 0.037,
so C3 either way; Pilling 2017's GCST006697 has no set in this window (rs6511720 was suggestive there).

> [q9] data.credibleSet.l2GPredictions.rows[0] score 0.9606614112854004 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol LDLR

The locus-to-gene score of LDLR on that set (the only gene in the top three above 0.5): `effector:E2`. E1 would need
a cis-QTL colocalisation for LDLR, not read here; Timmers 2020's eQTL colocalisation at this locus names KANK2, ILF3
and others, not LDLR.

Variant 15_78525587_C_T (rs8042849, CHRNA3/5), `alleleFrequencies`, of the alternative allele T (the
lifespan-raising one):

> [q10] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.6400883652430044

T is about 64% in non-Finnish Europeans (Timmers 2019: 0.65); 61% in African and 81% in East Asian gnomAD samples.

Credible set 8d0d0d1e11991d9ff9f5a5ea4fecf427, study GCST009890 (Timmers 2019), PICS, 30 members, lead
15_78525587_C_T:

> [q11] data.credibleSet.locus.rows[0] posteriorProbability 0.3505311365074509 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 15_78525587_C_T

PIP 0.35, `causal:C2`. GCST011100's set here (f3821132cc36ae09a8ac4cba08b1394b) has the same lead at 0.32.

> [q12] data.credibleSet.locus.rows[4] posteriorProbability 0.04564703281072673 r2Overall 0.9337735037407924 is95CredibleSet true data.credibleSet.locus.rows[4].variant id 15_78533838_G_A

rs931794 (Wright 2019's AncestryDNA lead), r² 0.93 to the lead; rs9788721 (Joshi's CHARGE proxy) is at 0.961.

> [q13] data.credibleSet.locus.rows[26] posteriorProbability 0.006751260807791553 r2Overall 0.8550959801809388 is95CredibleSet true data.credibleSet.locus.rows[26].variant id 15_78603787_A_G

rs1317286 (Pilling 2017's lead), r² 0.86 to the lead: `ld_proxy_of:rs8042849`. Pilling's own study GCST006697 holds
two sets here: rs1317286's (SuSiE-inf, 4b2a4542d121aa1e89555da4603a227a, with rs8042849 in it) and a second led by
rs578776 (c1d809ebe527dd273d44ff6759ceb60e, L2G CHRNA3 0.59), a secondary signal not scored here.

> [q14] data.credibleSet.l2GPredictions.rows[0] score 0.29093170166015625 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol CHRNA5

The locus-to-gene score of CHRNA5 on the Timmers 2019 set (next PSMA4 0.13,
CHRNA3 0.08): no gene reaches 0.5, `effector:E3`. The healthspan GWAS GCST007406 (Zenin 2019) has no credible set in
this window.

Variant 9_22100177_G_C (rs1556516, CDKN2B-AS1), `alleleFrequencies`, of the alternative allele C (the
lifespan-lowering one):

> [q15] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.5097071647419279

C is about 51% in non-Finnish Europeans, G 49%: the heterozygote is the most common genotype. C is 89% in African
and 67% in East Asian gnomAD samples.

Credible set 02462f216ce479d0c67d8b7bf734079f, study GCST009890 (Timmers 2019), PICS, 53 members, lead
9_22100177_G_C:

> [q16] data.credibleSet.locus.rows[0] posteriorProbability 0.05611117205107125 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 9_22100177_G_C

PIP 0.056, in the set below 0.1: `causal:C3`. The same block leads Timmers 2020's set (rs7859727, PIP 0.095),
Pilling 2017's (rs1556516, SuSiE-inf, PIP 0.17) and Zenin 2019's healthspan set GCST007406 (rs7859727, 0.11).

> [q17] data.credibleSet.locus.rows[2] posteriorProbability 0.03665730424019557 r2Overall 0.9843762746950737 is95CredibleSet true data.credibleSet.locus.rows[2].variant id 9_22103814_A_G

rs1333042 (Wright 2019's AncestryDNA lead), r² 0.98 to the lead; rs7859727 (Timmers 2020, Zenin 2019) is at
0.945: `ld_proxy_of:rs1556516`. Deelen 2019's CDKN2A/B discovery variant rs7039467 is in none of these sets.

> [q18] data.credibleSet.l2GPredictions.rows[0] score 0.3581562936306 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol CDKN2B

The locus-to-gene score of CDKN2B on the Timmers 2019 set (next CDKN2A 0.21, DMRTA1 0.12): below 0.5,
`effector:E3`. Timmers 2020 names CDKN2B as a cis-acting gene here by SMR and HEIDI, not by a colocalisation H4,
which §4.2's E2 asks for; Open Targets' own colocalisations were not read.

Variant 12_111621753_C_T (rs11065979, ATXN2/SH2B3), `alleleFrequencies`, of the alternative allele T (the
lifespan-lowering one):

> [q19] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.4454526645582715

> [q20] data.variant.alleleFrequencies[5] populationName eas_adj alleleFrequency 0.0017928286852589642

T is about 45% in non-Finnish Europeans and almost absent in East Asians (0.2%; 7.5% in African samples): the
lifespan-lowering haplotype is essentially European, and the locus has nothing to say outside Europe
(`ancestry_tag`). The SH2B3 missense rs3184504 (12_111446804_T_C, `mostSevereConsequence` missense_variant) shows
the same: its C allele is 51% in Europeans, 99.9% in East Asians.

Credible set 8a1b141eb70f7b60349f9bee88c3ec69, study GCST009890 (Timmers 2019), PICS, 21 members spread over about
1 Mb (to rs11066320 near PTPN11):

> [q21] data.credibleSet.locus.rows[0] posteriorProbability 0.3449911407808129 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 12_111621753_C_T

PIP 0.34, `causal:C2`. The missense rs3184504 is in the set at PIP 0.02 (r² 0.81); in Pilling 2017's SuSiE-inf
sets (GCST006697) it holds 0.15–0.16 against 0.23–0.25 for rs10774625 and rs7137828: not the C1 "coding with PIP ≥
0.2".

> [q22] data.credibleSet.locus.rows[10] posteriorProbability 0.0216267985568338 r2Overall 0.8130060667781549 is95CredibleSet true data.credibleSet.locus.rows[10].variant id 12_111494996_C_T

rs7137828 (Pilling 2017's lead), r² 0.81 to the lead; rs10774625 (Wright 2019's) 0.77: `ld_proxy_of:rs11065979`.

> [q23] data.credibleSet.l2GPredictions.rows[0] score 0.9505289196968079 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol SH2B3

The locus-to-gene score of SH2B3 on Timmers 2020's set here (GCST011100, 73d4741853bd7c0b6cf0d72356699b0b, lead
rs7137828); Pilling 2017's sets give SH2B3 0.95 and 0.96; Timmers 2019's broader set gives 0.41 (next ALDH2 0.17).
L2G ≥ 0.5 on the tighter sets, no colocalisation read: `effector:E2`, SH2B3.

Variant 11_113769120_A_C (rs61905747, ZW10/TTC12), `alleleFrequencies`, of the alternative allele C (the
lifespan-lowering one):

> [q24] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.17894225961114216

C is about 18% in non-Finnish Europeans (A 0.82, as Timmers 2020 has it); 16% in African, 0.2% in East Asian samples.

Credible set 43f2d00efd53bae3c0bbe0e9a8992e86, study GCST011100 (Timmers 2020, multivariate), PICS, 155 members,
lead 11_113769120_A_C. No credible set of GCST009890 or GCST006697 is in this window: the locus is genome-wide
significant only in the multivariate study and in Pilling 2017's fathers (not looked up here).

> [q25] data.credibleSet.locus.rows[0] posteriorProbability 0.30851682143588743 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 11_113769120_A_C

PIP 0.31, `causal:C2`.

> [q26] data.credibleSet.locus.rows[1] posteriorProbability 0.23982635310010916 r2Overall 0.9932439106381883 is95CredibleSet true data.credibleSet.locus.rows[1].variant id 11_113767455_T_C

rs17613838 (Wright 2019's), r² 0.99 to the lead: `ld_proxy_of:rs61905747`.

> [q27] data.credibleSet.l2GPredictions.rows[0] score 0.34978964924812317 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol CLDN25

The top locus-to-gene score (next ZW10 0.20): below 0.5, `effector:E3`. Timmers 2020's SMR names USP28, ANKK1 and
TTC12 (pmid-32678081#q7), none by colocalisation.

## Reading 2026-11-11, record

Variant 1_109275908_C_T (rs646776, CELSR2/PSRC1/SORT1), `alleleFrequencies`, of the alternative allele T (the
LDL-raising, lifespan-lowering one):

> [q28] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.7783743233702047

T is about 78% in non-Finnish Europeans, C 22%: T/T about 61%, C/T 34%, C/C 5%. T is 65% in African and 94% in East
Asian gnomAD samples.

Credible set 1a658d9fd8f8e98913ab45551589adde, study GCST006701 (Pilling 2017, fathers' attained age), SuSiE-inf,
ten members, lead 1_109274570_A_G (rs7528419, PIP 0.23; rs12740374 0.14):

> [q29] data.credibleSet.locus.rows[2] posteriorProbability 0.11315562079530557 r2Overall null is95CredibleSet true data.credibleSet.locus.rows[2].variant id 1_109275908_C_T

rs646776 holds PIP 0.11 in the set: `causal:C2`. rs602633 (Pilling's reported lead), rs4970836 (Timmers 2019's)
and rs599839 (Wright 2019's) are all members of the same set (PIP 0.054, 0.065 and 0.056): one signal,
`ld_proxy_of:rs646776`. Neither Timmers 2019's GCST009890, Timmers 2020's GCST011100, Pilling's combined
GCST006697 nor Zenin's healthspan GCST007406 has a set in this window. Many lipid, CAD and other sets cover the
same variants; none was used.

> [q30] data.credibleSet.l2GPredictions.rows[0] score 0.9894455075263977 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol SORT1

The locus-to-gene score of SORT1 on that set (next CELSR2 0.97, PSRC1 0.29). Both SORT1 and CELSR2 pass 0.5;
SORT1 is the top score, and no colocalisation was read: `effector:E2`, SORT1.

Credible set 09f4c8bb0fa06f0fbcc55b6e0cc7957b, study GCST009450 (Wright 2019's AncestryDNA-UK Biobank fathers'
meta-analysis), PICS, ten members, lead 1_109279544_G_A (rs599839):

> [q31] data.credibleSet.locus.rows[4] posteriorProbability 0.0802214037167139 r2Overall 0.940787220652168 is95CredibleSet true data.credibleSet.locus.rows[4].variant id 1_109275908_C_T

rs646776, r² 0.94 to Wright's lead rs599839 (PIP 0.080); rs602633 is at r² 0.94 too (PIP 0.078). L2G SORT1 0.99
on this set as well.

## Reading 2026-11-11, record

Variant 15_90880313_G_T (rs6224, FURIN/FES, an intron of FURIN and upstream of FES; noncoding), `alleleFrequencies`,
of the alternative allele T (the lifespan-lowering one):

> [q32] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.47384152497080306

T is about 47 % in non-Finnish Europeans, G 53 %: G/G about 28 %, G/T 50 %, T/T 22 %. T is 82 % in African and 14 % in
East Asian gnomAD samples.

Credible set e95e1989ec0d8799c17be4b6f837c2f1, study GCST009890 (Timmers 2019, "Parental lifespan"), PICS, nine
members, lead 15_90880313_G_T (beta −0.2507 per T):

> [q33] data.credibleSet.locus.rows[0] posteriorProbability 0.22429079929278053 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 15_90880313_G_T

rs6224 holds PIP 0.22: `causal:C2`. Timmers 2020's multivariate set (GCST011100) is led by rs6224 too (PIP 0.21), and
Pilling 2017's combined-parents set (GCST006697, SuSiE-inf) holds both rs17514846 (PIP 0.23, its lead) and rs6224
(0.20).

> [q34] data.credibleSet.locus.rows[8] posteriorProbability 0.06475078034972 r2Overall 0.9178175286358745 is95CredibleSet true data.credibleSet.locus.rows[8].variant id 15_90873320_C_A

rs17514846 (Pilling 2017's FURIN lead), r² 0.92 to rs6224 in that set (PIP 0.065): the same signal,
`ld_proxy_of:rs6224`.

> [q35] data.credibleSet.l2GPredictions.rows[0] score 0.9670971035957336 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol FES

The locus-to-gene score of FES on that set (FURIN 0.15), the only gene above 0.5, and no colocalisation was read:
`effector:E2`, FES. The variant lies in FURIN, and Timmers 2019's SMR names FURIN and FES both (pmid-30642433#q22).

## Reading 2026-11-11, record

Three credible sets led by 1_39570256_G_T (rs3768321, PABPC4; GRCh38), each cached whole by `loci fetch-supp` as
`credibleset-<studyLocusId>.json`. Open Targets' beta is per the variant id's second allele, T. For row 2.

> [q36] data.credibleSet studyLocusId 0980823f4152495c262627d9e13424aa finemappingMethod PICS pValueMantissa 6 pValueExponent -10 beta -0.007898258

> [q37] data.credibleSet.study id GCST90321079 traitFromSource Aging

The set of Rosoff 2023's mvAge ("Aging", GCST90321079; PICS), P 6 × 10⁻¹⁰, beta −0.0079 per T: the same result as
Rosoff's Table 1 (pmid-37550455#q1, +0.0079 per G).

> [q38] data.credibleSet.locus.rows[0] posteriorProbability 0.16832334222629408 is95CredibleSet true

rs3768321's PIP in that set: 0.17, in the 95 % set, the highest of its 100 members (the next 0.016):
`causal:C2`.

> [q39] data.credibleSet.l2GPredictions.rows[0] score 0.22739721834659576

The locus-to-gene score of PABPC4 on that set (next BMP8A 0.066): below 0.5 and no colocalisation read,
`effector:E3`, no gene named.

> [q40] data.credibleSet studyLocusId 0a6b39073b95a8a3d1f7e722abf30a8b finemappingMethod PICS pValueMantissa 4.7220001220703125 pValueExponent -68 beta -0.0387154

> [q41] data.credibleSet.study id GCST90497348 traitFromSource HDL cholesterol levels

> [q42] data.credibleSet.locus.rows[0] posteriorProbability 0.9999865928193756 is95CredibleSet true

HDL cholesterol (GCST90497348; PICS): P 4.7 × 10⁻⁶⁸, beta −0.039 per T, and rs3768321 the set's only member at PIP
1.00. T lowers HDL cholesterol.

> [q43] data.credibleSet studyLocusId 05a00e4b8b9355400615f04c5317bdef finemappingMethod PICS pValueMantissa 1.8359999656677246 pValueExponent -24 beta 0.0265928

> [q44] data.credibleSet.study id GCST90474428 traitFromSource Triglycerides levels (UKB data field 30870)

> [q45] data.credibleSet.locus.rows[0] posteriorProbability 0.9015747057939612 is95CredibleSet true

Triglycerides (GCST90474428, UK Biobank; PICS): P 1.8 × 10⁻²⁴, beta +0.027 per T, rs3768321 at PIP 0.90. T raises
triglycerides. So the lipid signal sits on the mvAge lead itself, T on the side of lower HDL, higher
triglycerides and worse ageing: the anchor of row 2's mechanism, a co-location of association, not a mediation
test.

## Reading 2026-11-11, record

rs2613508 (1_72367899_C_T, GRCh38; LINC02796 by the seed, NEGR1 region), for row 4: its variant record, the variant
record of the BMI set's lead rs1993709 (1_72372846_A_G), and two credible sets, cached by `loci fetch-supp`. Open
Targets' beta is per the variant id's second allele: T at rs2613508, G at rs1993709.

> [q46] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.8197380041212835

T's frequency in gnomAD's non-Finnish Europeans: 0.82, so C 0.18, as Rosoff's MAF (pmid-37550455#q8).

> [q47] data.credibleSet studyLocusId abc062e87620fc5eca41a2571c34057e finemappingMethod PICS pValueMantissa 8 pValueExponent -9 beta -0.007669109

> [q48] data.credibleSet.study id GCST90321079 traitFromSource Aging

The set of Rosoff 2023's mvAge ("Aging", GCST90321079; PICS), led by rs2613508 itself: P 8 × 10⁻⁹, beta −0.0077 per T,
Rosoff's Table 1 result (+0.0077 per C).

> [q49] data.credibleSet.locus.rows[0] posteriorProbability 0.04770664834894591 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 1_72367899_C_T

rs2613508's PIP in that set: 0.048, the highest of 75 members in the 95 % set, a long block of near-equal PIPs at
r² above 0.8 (the next 0.039): below 0.1, `causal:C3`.

> [q50] data.credibleSet.l2GPredictions.rows[0] score 0.5597900152206421 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol NEGR1

The locus-to-gene score of NEGR1 on that set, 0.56, the top gene: at 0.5 or above with no colocalisation read,
`effector:E2`, NEGR1.

> [q51] data.credibleSet studyLocusId 6e47d5bec330e6fe02b02c823df8040b finemappingMethod PICS pValueMantissa 1 pValueExponent -52 beta 0.0317

> [q52] data.credibleSet.study id GCST009001 traitFromSource Body mass index

> [q53] data.credibleSet.locus.rows[3] posteriorProbability 0.08410889445344838 r2Overall 0.9927827786782508 is95CredibleSet true data.credibleSet.locus.rows[3].variant id 1_72367899_C_T

Body mass index (GCST009001; PICS): P 1 × 10⁻⁵², beta +0.0317 per G at the lead rs1993709; rs2613508 is a member at PIP
0.084, r² 0.99 to the lead.

> [q54] data.credibleSet.l2GPredictions.rows[0] score 0.7448862195014954 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol NEGR1

NEGR1's locus-to-gene score on the BMI set, 0.74.

> [q55] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.8198093500838507

G's frequency at rs1993709 in the same population: 0.82, as T's at rs2613508 (q46); with r² 0.99 the two ride one
haplotype, G with T (phase derived from the frequencies, not read from a haplotype record). So T raises BMI, the side
of worse ageing in mvAge (q47): association on one haplotype, not a mediation test; the anchor of row 4's mechanism.

## Reading 2026-11-11, record

rs1230666 (1_113630788_A_G, GRCh38; MAGI3 by the seed, the PTPN22 region), for row 7: its variant record and two
credible sets, cached by `loci fetch-supp`. Open Targets' beta is per G, the id's second allele.

> [q56] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.8545842531272995

G's frequency in gnomAD's non-Finnish Europeans: 0.85, as Timmers 2019's 0.85 (pmid-30642433#q29).

> [q57] data.credibleSet studyLocusId f53bfb834cecc17a477fbb6d054e5404 finemappingMethod PICS pValueMantissa 6 pValueExponent -9 beta 0.3224

> [q58] data.credibleSet.study id GCST009890 traitFromSource Parental lifespan

Timmers 2019's parental lifespan set (GCST009890; PICS), led by rs1230666: P 6 × 10⁻⁹, beta 0.3224 years per G.

> [q59] data.credibleSet.locus.rows[0] posteriorProbability 0.6441357257784882 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 1_113630788_A_G data.credibleSet.locus.rows[0].variant.rsIds[0] rs1230666

rs1230666's PIP in that set: 0.64, at 0.5 or above: `causal:C1` by §4.2's threshold. PICS weighs members by LD with
the lead alone, so the lead is favoured when the block is long.

> [q60] data.credibleSet.locus.rows[1] posteriorProbability 0.017836708761464048 r2Overall 0.6753080834761617 is95CredibleSet true data.credibleSet.locus.rows[1].variant id 1_113834946_A_G data.credibleSet.locus.rows[1].variant.rsIds[0] rs2476601

> [q61] data.credibleSet.locus.rows[2] posteriorProbability 0.01766291421573972 r2Overall 0.6744933607140257 is95CredibleSet true data.credibleSet.locus.rows[2].variant id 1_113761186_C_A data.credibleSet.locus.rows[2].variant.rsIds[0] rs6679677

The next members, rs2476601 and rs6679677 (Timmers 2019's named variant, pmid-30642433#q31), at r² 0.68 and 0.67 to
the lead and PIP 0.018 each: the r² agrees with the paper's "r2 > 0.6".

> [q62] data.credibleSet.l2GPredictions.rows[0] score 0.41865965723991394 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol PHTF1

The top locus-to-gene score on that set: PHTF1, 0.42. Below 0.5, `effector:E3`; no gene named.

> [q63] data.credibleSet studyLocusId 342a0b5fa7ba1d5b86c1c50e484b4d2a finemappingMethod PICS pValueMantissa 2 pValueExponent -11 beta 0.010161293

> [q64] data.credibleSet.study id GCST90321079 traitFromSource Aging

> [q65] data.credibleSet.locus.rows[0] posteriorProbability 0.8624364813245581 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 1_113630788_A_G data.credibleSet.locus.rows[0].variant.rsIds[0] rs1230666

Rosoff 2023's mvAge set ("Aging", GCST90321079; PICS), led by rs1230666: P 2 × 10⁻¹¹, beta +0.0102 per G; PIP 0.86.

## Reading 2026-11-11, supplement

rs2228145 (IL6R p.Asp358Ala), for row 8. The variant record (`variant-1_154454494_A_C.json`):

> [q66] data.variant.rsIds[0] rs2228145

> [q67] data.variant.mostSevereConsequence label missense_variant

> [q68] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.4023276209195826

1_154454494_A_C is rs2228145, missense, its C allele (the alternative) at 0.40 in gnomAD non-Finnish Europeans.

`credibleSets(studyIds: [the seven lifespan, healthspan and longevity studies: GCST009890, GCST006697, GCST006702,
GCST011100, GCST009450, GCST007406, GCST90321079], variantIds: ["1_154454494_A_C"])`, cached as
`credibleSets-longevity-1_154454494_A_C.json`:

> [q69] data.credibleSets count 0

No credible set of any of those studies holds rs2228145: causal C4 for longevity, the level read from a longevity
set only. The filter matches a set's members, not only its lead: the same query for GCST009890 and rs2476601, a
non-lead member of Timmers 2019's MAGI3 set (q60), returns that set, led by rs1230666
(`credibleSets-control-GCST009890-1_113834946_A_G.json`):

> [q70] data.credibleSets count 1

> [q71] data.credibleSets.rows[0].variant.rsIds[0] rs1230666

All the variant's credible sets, of any study (`variant-credibleset-count-1_154454494_A_C.json`):

> [q72] data.variant.credibleSets count 286

286 sets in all, none from the seven studies above. For row 8.

## Reading 2026-11-11, record

> [q73] data.variant id 1_174018660_A_G

> [q74] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.18389232127096206

`variant-1_174018660_A_G.json`: rs10798302, intronic; G 0.184 in gnomAD non-Finnish Europeans. For row 10.

> [q75] data.credibleSets count 0

> [q76] data.credibleSets count 0

`credibleSets(studyIds, variantIds)` over the seven lifespan, healthspan and longevity studies plus Wright 2019's
current-age study GCST009448: no set holds rs10798302 (`credibleSets-longevity8-1_174018660_A_G.json`) or rs16847402
(`...-1_174745913_T_C.json`). For row 10.

> [q77] data.study.credibleSets count 3

> [q78] data.study.credibleSets.rows[0].variant.rsIds[0] rs4755737

> [q79] data.study.credibleSets.rows[1].variant.rsIds[0] rs11783562

> [q80] data.study.credibleSets.rows[2].variant.rsIds[0] rs769449

`study-GCST009448-sets.json`: Wright's current-age study has three credible sets (PICS), led by rs4755737 (11p11),
rs11783562 (8p12, near WRN) and rs769449 (APOE); none at 1q25. For row 10.

> [q81] data.variant.credibleSets count 26

> [q82] data.variant.credibleSets.rows[14].study id GCST90474379 traitFromSource IGF-1 levels (UKB data field 30770)

> [q83] data.variant.credibleSets.rows[14].variant id 1_174018660_A_G

> [q84] data.variant.credibleSets.rows[8].study id GCST90002378 traitFromSource White blood cell count

> [q85] data.variant.credibleSets.rows[1].study id GCST90627750 traitFromSource Hypothyroidism

> [q86] data.variant.credibleSets.rows[14] studyLocusId 99ab35c05be7fcbdac4f89d701522a52 pValueMantissa 1.7319999933242798 pValueExponent -18

`variant-crediblesets-1_174018660_A_G.json`: rs10798302 is in 26 sets of other traits. It leads one, IGF-1 levels in
UK Biobank (GCST90474379, P 1.7 × 10⁻¹⁸); it is a member, not the lead, of sets for white cell and neutrophil counts
(GCST90002378, P 6 × 10⁻¹⁶, and others), hypothyroidism (GCST90627750), IGF-1 in other studies, schizophrenia, and
expression of the gene ENSG00000152061 in blood cells and fat (the record names no symbol). Membership gives no allele or direction. For row 10.

## Reading 2026-11-11, record

> [q87] data.credibleSets count 0

> [q88] data.credibleSets count 0

No credible set of the eight lifespan, healthspan, longevity and current-age studies holds rs6744653
(`credibleSets-longevity8-2_628524_A_G.json`) or rs66906321 (`credibleSets-longevity8-2_630070_T_C.json`). For row 11.

> [q89] data.variant.credibleSets count 510

> [q90] data.variant.credibleSets.rows[2].study id GCST007241 traitFromSource Obesity (extreme)

> [q91] data.variant.credibleSets.rows[13].study id GCST002461 traitFromSource Body mass index

`variant-crediblesets-2_628524_A_G.json` (first 100 of 510 read): rs6744653 sits in 510 credible sets, nearly all of
body size and fat (extreme obesity, BMI, fat mass), with smoking, blood pressure, type 2 diabetes and lipids among the
rest. For row 11.

> [q92] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.8283593060864451

`variant-2_628524_A_G.json`: G 0.83 in gnomAD non-Finnish Europeans. For row 11.

> [q93] data.credibleSets count 0

> [q94] data variant null

rs1049053 (6:32,666,628 C/T): no credible set of the eight lifespan, healthspan, longevity and current-age studies
holds it (`credibleSets-longevity8-6_32666628_C_T.json`), and Open Targets 26.09 has no record of the variant at all
(`variant-6_32666628_C_T.json`). For row 103.

> [q95] data.credibleSet.l2GPredictions.rows[0] score 0.7735595107078552

> [q96] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol PABPC4

The locus-to-gene score of PABPC4 on the HDL cholesterol set led by rs3768321 (`credibleset-0a6b39073b95a8a3d1f7e722abf30a8b.json`,
q40-q42): 0.77, above 0.5, on a lipid trait's set, not the row's own claim (D17.2). For row 2.

## rs1275922 (KCNK3), for row 12

Variant 2_26710019_A_G. Of the eight lifespan studies (`credibleSets-longevity8-2_26710019_A_G.json`), it is in two
sets:

> [q97] data.credibleSets count 2

> [q98] data.credibleSet studyLocusId 197bf4ed7aa51f7f4f88306aceb01c7f finemappingMethod PICS pValueMantissa 6 pValueExponent -9 beta 0.2579

> [q99] data.credibleSet.study id GCST009890 traitFromSource Parental lifespan

> [q100] data.credibleSet.locus.rows[0] posteriorProbability 0.30925827312711746 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 2_26710019_A_G data.credibleSet.locus.rows[0].variant.rsIds[0] rs1275922

> [q101] data.credibleSet.locus.rows[1] posteriorProbability 0.1890451821492718 r2Overall 0.975536047142678 is95CredibleSet true data.credibleSet.locus.rows[1].variant id 2_26705229_A_G data.credibleSet.locus.rows[1].variant.rsIds[0] rs1731247

> [q102] data.credibleSet.locus.rows[2] posteriorProbability 0.1868541944383164 r2Overall 0.9745781541635675 is95CredibleSet true data.credibleSet.locus.rows[2].variant id 2_26705943_G_A data.credibleSet.locus.rows[2].variant.rsIds[0] rs11126666

> [q103] data.credibleSet.locus.rows[3] posteriorProbability 0.18111804250164912 r2Overall 0.9719652081828207 is95CredibleSet true data.credibleSet.locus.rows[3].variant id 2_26701955_A_C data.credibleSet.locus.rows[3].variant.rsIds[0] rs1731248

> [q104] data.credibleSet.l2GPredictions.rows[0] score 0.8477738499641418 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol KCNK3

Timmers 2019's parental-lifespan set (PICS, 11 members) is led by rs1275922 at PIP 0.31 (causal:C2), with three
variants at r² 0.97 to 0.98 sharing most of the rest (rs1731247 0.19, rs11126666 0.19, rs1731248 0.18): one signal,
its causal variant not resolved among four. Top locus-to-gene score KCNK3 0.85 (effector:E2; no colocalisation read).

> [q105] data.credibleSet studyLocusId e43a6d1483e391b7d4cad3e7667effd8 finemappingMethod PICS pValueMantissa 3 pValueExponent -9 beta 0.006999004

> [q106] data.credibleSet.study id GCST90321079 traitFromSource Aging

> [q107] data.credibleSet.locus.rows[0] posteriorProbability 0.31544213076152683 r2Overall 1 is95CredibleSet true data.credibleSet.locus.rows[0].variant id 2_26710019_A_G data.credibleSet.locus.rows[0].variant.rsIds[0] rs1275922

Rosoff 2023's mvAge set (GCST90321079, PICS) is led by rs1275922 at PIP 0.32, the same four-variant shape.

> [q108] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.7288516971586564

gnomAD non-Finnish Europeans: G (the alternate allele) 0.729.

> [q109] data.variant.alleleFrequencies[5] populationName eas_adj alleleFrequency 0.3146568437378829

gnomAD East Asians: rs1275922's G 0.315.

> [q110] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.7283868879472694

> [q111] data.variant.alleleFrequencies[5] populationName eas_adj alleleFrequency 0.3123543123543124

rs1731248 (variant 2_26701955_A_C): C, the alternate allele, 0.728 in non-Finnish Europeans and 0.312 in East
Asians, the lead's G frequencies (0.729, q108; 0.315, q109) in both; at EUR r² 0.97, D′ 0.98 (db-ensembl-116#q46)
C travels with the lead's G (derived from frequencies).

## rs577106756 (PRKD3), for row 13

> [q112] data.study id GCST90551885 traitFromSource Lifespan nSamples 180970

> [q113] data.credibleSets count 1

> [q114] data.credibleSets.rows[0].variant.rsIds[0] rs429358

Park 2025's men's GWAS is in Open Targets (`credibleSets-GCST90551885.json`, n 180,970) with one credible set, at
APOE's rs429358: none at PRKD3.

> [q115] data variant null

Nor does the platform know the variant (`variant-2_37257437_G_A.json`): no fine-mapping and no locus-to-gene score
for rs577106756 (causal C4, effector E4).

## rs980183 (LINC01122), for row 14

> [q116] data.variant.credibleSets count 270

Open Targets 26.09 holds rs980183 (2_59084401_G_A, alt A) in 270 credible sets. By the top P of each family, read
from all three pages: diabetes and glycaemia (type 2 diabetes to 3 × 10⁻³¹, HbA1c 3 × 10⁻²⁸, glucose 5 × 10⁻²⁸),
adiposity (fat mass 8 × 10⁻²⁶, BMI 1.5 × 10⁻²³, waist and hip), blood pressure (to 1.8 × 10⁻¹⁴, hypertension 2.4
× 10⁻¹⁵), NMR lipid ratios and triglycerides (to 1.4 × 10⁻¹³), CRP, ALT and cystatin C; no bone-density set. Most
are led by neighbours at r² about 0.97 (q54 of db-ensembl-116), whose alleles' phase to rs980183 is not read here.

> [q117] data.credibleSet studyLocusId eaf547c5ce79c2a061a043cf0d4e5684 finemappingMethod PICS pValueMantissa 2 pValueExponent -9 beta 0.006344008

> [q118] data.credibleSet.locus count 15

> [q119] data.credibleSet.locus.rows[0] posteriorProbability 0.10688954959474208 r2Overall 1 is95CredibleSet true

> [q120] data.credibleSet.locus.rows[1] posteriorProbability 0.06914659009560219 r2Overall 0.9811007837971086 is95CredibleSet true

> [q121] data.credibleSet.locus.rows[14] posteriorProbability 0.05614648010135342 r2Overall 0.9643256065982153 is95CredibleSet true

Rosoff 2023's mvAge set (GCST90321079, PICS): led by rs980183, P 2 × 10⁻⁹, β +0.0063 per A; 15 members, every one
in the 95 % set; the lead's PIP 0.107, the others 0.069 down to 0.056. C2 by the letter (PIP 0.1-0.5), at its
floor: one signal whose causal variant is not resolved. The set carries no locus-to-gene score (E4).

> [q122] data.credibleSet studyLocusId 5617c111367a6b3c00af0e1ce05041a6 finemappingMethod PICS pValueMantissa 1 pValueExponent -14 beta -0.0363

> [q123] data.credibleSet.study id GCST010555 traitFromSource Type 2 diabetes

> [q124] data.credibleSet.locus.rows[0] posteriorProbability 0.12952570780354172 r2Overall 1 is95CredibleSet true

Vujkovic 2020's type 2 diabetes set (GCST010555, PICS): led by rs980183, P 1 × 10⁻¹⁴, β −0.036 per A; the lead's
PIP 0.13, 15 members. A lowers type 2 diabetes. No locus-to-gene score.

> [q125] data.credibleSet studyLocusId 52184156cf864584518b8fd85fbd379a finemappingMethod SuSiE-inf pValueMantissa 9.101737976074219 pValueExponent -21 beta -0.014855347699468675

> [q126] data.credibleSet.study id GCST90013974 traitFromSource Body mass index (UKB data field 21001)

> [q127] data.credibleSet.variant.rsIds[0] rs6545714

> [q128] data.credibleSet.locus.rows[5] posteriorProbability 0.06618203494441346 r2Overall null is95CredibleSet true

> [q129] data.credibleSet.locus.rows[5].variant.rsIds[0] rs980183

A UK Biobank BMI set (GCST90013974, SuSiE-inf), led by rs6545714 (2_59080590_G_A, alt A), P 9 × 10⁻²¹, β −0.0149
per A; rs980183 is a member (PIP 0.066). rs6545714's A travels with rs980183's A (db-ensembl-116#q55, derived), so
the longer-life A goes with lower BMI. No locus-to-gene score.

## rs78438918 (AFF3, 2_100013653_A_G), for row 15

Open Targets gives β per alternate allele, here G: the mvAge set's +0.0078 is Rosoff's −0.0078 per A
(pmid-37550455#q11), which bears that reading out.

> [q130] data.variant.credibleSets count 19

Nineteen credible sets hold the lead: Rosoff's mvAge, three hand-grip-strength sets, a waist-hip ratio set, a
docosahexaenoic-acid ratio set, and thirteen expression or splicing sets (ten of them AFF3's, ENSG00000144218,
three ENSG00000230393's). No disease set holds it.

> [q131] data.credibleSet studyLocusId 63ebc186030598ff6170aee23778857e finemappingMethod PICS pValueMantissa 1 pValueExponent -8 beta 0.007838645

> [q132] data.credibleSet.study id GCST90321079 traitFromSource Aging

> [q133] data.credibleSet.locus count 44

> [q134] data.credibleSet.locus.rows[0] posteriorProbability 0.26396338020977966 r2Overall 1 is95CredibleSet true

> [q135] data.credibleSet.locus.rows[1] posteriorProbability 0.06137891285015807 r2Overall 0.8759564773546535 is95CredibleSet true

Rosoff 2023's mvAge set (PICS): led by rs78438918, P 1 × 10⁻⁸, β +0.0078 per G; 44 members; the lead's PIP 0.26,
the next 0.061. C2 (PIP 0.1-0.5): the lead is the likeliest of many, not resolved.

> [q136] data.credibleSet.l2GPredictions.rows[0] score 0.9018622040748596

> [q137] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol AFF3

Locus-to-gene on the mvAge set: AFF3 at 0.90 (E2).

> [q138] data.credibleSet studyLocusId c8ca52dba7eb1d7a05fa0ceb7d4c2701 finemappingMethod PICS pValueMantissa 4.585000038146973 pValueExponent -9 beta 0.0122074

> [q139] data.credibleSet.study id GCST90014019 traitFromSource Hand grip strength left (UKB data field 46)

> [q140] data.credibleSet.locus.rows[0] posteriorProbability 0.2798753662209768 r2Overall 1 is95CredibleSet true

> [q141] data.credibleSet.study id gtex-v10_ge_brain_cerebellum_ensg00000144218 traitFromSource ENSG00000144218

A UK Biobank hand-grip-strength set (GCST90014019, PICS), led by rs78438918 (PIP 0.28), P 4.6 × 10⁻⁹, β +0.0122
per G: G goes with a stronger grip. Locus-to-gene AFF3 at 0.87 (q145). And GTEx v10's cerebellum expression set
for AFF3 (q141, SuSiE), led by rs78438918 (PIP 0.14, q146), P 3 × 10⁻¹⁷, β +0.58 per G: G raises AFF3's expression
in the cerebellum.

> [q142] data.variant.credibleSets.rows[2] studyLocusId 435c0b6807d45058c1510fe1ff7e9e5f pValueMantissa 2.2450079917907715 pValueExponent -10 beta -0.007495712269800483

> [q143] data.variant.credibleSets.rows[2].study id GCST90692986 traitFromSource Waist-hip ratio

> [q144] data.variant.credibleSets.rows[2].variant id 2_100099129_C_T

A waist-hip ratio set led by a neighbour, 2_100099129_C_T, β −0.0075 per T; the lead is a member. The neighbour's
phase with G is not read, so the direction for G is unknown.

> [q145] data.credibleSet.l2GPredictions.rows[0] score 0.869569718837738

> [q146] data.credibleSet.locus.rows[0] posteriorProbability 0.13851348638621339 r2Overall null is95CredibleSet true

The grip set's locus-to-gene score (AFF3, 0.87), and the cerebellum AFF3 expression set's first member, the lead,
PIP 0.14 (SuSiE).

> [q147] data.credibleSet.locus.rows[7] posteriorProbability 0.04046131420255379 r2Overall 0.8313709706906519 is95CredibleSet true

> [q148] data.credibleSet.locus.rows[7].variant.rsIds[0] rs13032879

rs13032879, Wright 2019's fathers' SNP (pmid-31484785#q44), is a member of mvAge's 95 % credible set (PIP 0.040):
the same signal as the lead.

> [q149] data.variant.credibleSets.rows[17] studyLocusId f306c3f4920797759ffc31d6130fcb74 pValueMantissa 3.2836670875549316 pValueExponent -9 beta 0.008574912965415503

> [q150] data.variant.credibleSets.rows[17].study id GCST90692811 traitFromSource Hand grip strength left (UKB data field 46)

> [q151] data.variant.credibleSets.rows[17].variant id 2_100013653_A_G

A second grip-strength set led by the lead (GCST90692811), P 3.3 × 10⁻⁹, β +0.0086 per G.

> [q152] data.variant.credibleSets.rows[8] studyLocusId 8f24cd2a37077fd4d71b7e805e083f3a pValueMantissa 1.6492046117782593 pValueExponent -9 beta 0.008851918335459381

> [q153] data.variant.credibleSets.rows[8].variant id 2_99959842_C_T

The third grip set (GCST90691860), P 1.6 × 10⁻⁹, is led by a neighbour, 2_99959842_C_T, whose phase with G is not
read; it gives no direction for G.

## rs117898573 (LRP1B), for row 16

> [q154] data variant null

Open Targets 26.09 has no record of 2_142119915_C_T (`variant-sets-2_142119915_C_T.json`).

> [q155] data.study id GCST90132317 traitFromSource Healthy aging nSamples 7210

> [q156] data.credibleSets count 1

> [q157] data.credibleSets.rows[0].variant.rsIds[0] rs138499810

Chang 2022's study is in the platform (GCST90132317, n 7,210, the discovery arm) with one credible set, at the
chromosome 5 lead rs138499810: none at LRP1B. No fine-mapping and no locus-to-gene score for rs117898573 (causal C4,
effector E4).

## rs10197246 (CASP8 / FLACC1), for row 17

> [q158] data.variant.credibleSets count 81

> [q159] data.variant.credibleSets.rows[0] studyLocusId 00c38262c4439c76852867d7fb2beab3 pValueMantissa 1.4419573545455933 pValueExponent -9 beta -0.010883614063089686

> [q160] data.variant.credibleSets.rows[0].study id GCST007406 traitFromSource Healthspan

The variant (2_201340018_T_C, alternative allele C) is in 81 credible sets. It leads Zenin's healthspan set
(GCST007406), β −0.0109 for C, P 1.4 × 10⁻⁹.

> [q161] data.variant.credibleSets.rows[72] studyLocusId e60bc7e285ea1e1b42575a6df4cfb536 pValueMantissa 9.395000457763672 pValueExponent -39 beta -0.019308328170980823

> [q162] data.variant.credibleSets.rows[72].study id GCST90475577 traitFromSource Melanomas of skin, dx or hx (PheCode 172.1)

> [q163] data.variant.credibleSets.rows[58] studyLocusId ad82cd3dded0c69bf44a0456070fb139 pValueMantissa 1.0269999504089355 pValueExponent -24 beta -0.0234217779231829

> [q164] data.variant.credibleSets.rows[58].study id FINNGEN_R12_C3_CANCER_EXALLC traitFromSource Malignant neoplasm, excluding all cancers (controls excluding all cancers)

> [q165] data.variant.credibleSets.rows[30] studyLocusId 5ee8576cd8aa7946a468762e44a2003b pValueMantissa 2.48799991607666 pValueExponent -14 beta -0.0406445957458592

> [q166] data.variant.credibleSets.rows[30].study id FINNGEN_R12_C3_BREAST_EXALLC traitFromSource Malignant neoplasm of breast, excluding all cancers (controls excluding all cancers)

It also leads the sets of skin melanoma in UK Biobank (GCST90475577, C β −0.019, P 9.4 × 10⁻³⁹), FinnGen R12's all
malignant neoplasms (C −0.023, P 1.0 × 10⁻²⁴) and FinnGen's breast cancer (C −0.041, P 2.5 × 10⁻¹⁴): C lowers each, the
healthspan side. The other 77 sets include basal-cell and squamous-cell skin cancer, oesophageal squamous-cell
carcinoma, blood-cell counts and many CASP8 transcript and splicing QTLs (read, not each quoted).

> [q167] data.variant.credibleSets.rows[8] studyLocusId 271b549e92b548a38c493e105f9f66d9 pValueMantissa 1.2109999656677246 pValueExponent -63 beta -0.729308

> [q168] data.variant.credibleSets.rows[8].study id gtex-v10_tx_nerve_tibial_enst00000339403 traitFromSource ENST00000339403

The lead itself leads a CASP8 transcript QTL in tibial nerve (ENST00000339403, a CASP8 transcript; P 1.2 × 10⁻⁶³).

> [q169] data.credibleSet studyLocusId 00c38262c4439c76852867d7fb2beab3 finemappingMethod SuSiE-inf pValueMantissa 1.4419573545455933 pValueExponent -9 beta -0.010883614063089686

> [q170] data.credibleSet.locus.rows[0] posteriorProbability 0.12556739322186256 r2Overall null is95CredibleSet true

> [q171] data.credibleSet.locus.rows[10] posteriorProbability 0.025616056016237808 r2Overall null is95CredibleSet true

The healthspan set (SuSiE-inf): 11 variants in the 95 % set, rs10197246 the highest at PIP 0.126 (the 11th 0.026).
Causal C2 (in a set, PIP 0.1 to 0.5).

> [q172] data.credibleSet.l2GPredictions.rows[0] score 0.5551297664642334

> [q173] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol FLACC1

> [q174] data.credibleSet.l2GPredictions.rows[1] score 0.1901630461215973

> [q175] data.credibleSet.l2GPredictions.rows[1].target approvedSymbol CASP8

Locus-to-gene: FLACC1 0.555, CASP8 0.190.

> [q176] data.credibleSet.colocalisation count 235

> [q177] data.credibleSet.colocalisation.rows[111] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9887033787525517 clpp 0.07665679585887168 rightStudyType eqtl

> [q178] data.credibleSet.colocalisation.rows[111].otherStudyLocus.study.target approvedSymbol FLACC1

> [q179] data.credibleSet.colocalisation.rows[2] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9549020516130204 clpp 0.018997296365495152 rightStudyType eqtl

> [q180] data.credibleSet.colocalisation.rows[2].otherStudyLocus.study id brainseq_ge_brain_ensg00000064012 traitFromSource ENSG00000064012 studyType eqtl

> [q181] data.credibleSet.colocalisation.rows[2].otherStudyLocus.study.target approvedSymbol CASP8

QTL colocalisation of the healthspan set (`studyTypes` set to the QTL types; the default returned GWAS partners
only): 235 colocalisations over two pages (`coloc-qtl-…`, `coloc-qtl-p1-…`). At H4 ≥ 0.8, 217 are CASP8 (88 eQTL, 60
sQTL, 69 transcript-usage QTL, across GTEx and other panels), 7 FLACC1 eQTL (skin, adipose, breast, oesophagus,
cerebellum; q177, q178) and 1 TRAK2 exon QTL (counted from the cached pages, not each quoted). So FLACC1 meets E1 on
the letter (locus-to-gene ≥ 0.5 and a cis-QTL colocalisation) while CASP8 colocalises far more widely and holds the
lead's own strongest QTL (q167): two genes each meet a criterion, the ambiguity of E3. For row 17.

> [q182] data.credibleSet.colocalisation.rows[14] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9900413540286052 clpp 0.08529692544619219 rightStudyType gwas

> [q183] data.credibleSet.colocalisation.rows[14].otherStudyLocus.study id GCST90328132 traitFromSource Basal cell carcinoma studyType gwas

> [q184] data.credibleSet.colocalisation.rows[0] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9829808798018292 clpp 0.05076374646710202 rightStudyType gwas

> [q185] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study id GCST90692907 traitFromSource Facial ageing (UKB data field 1757) studyType gwas

> [q186] data.credibleSet.colocalisation.rows[78] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9863575327725644 clpp 0.06180410553167977 rightStudyType gwas

> [q187] data.credibleSet.colocalisation.rows[78].otherStudyLocus.study id GCST004988 traitFromSource Breast cancer studyType gwas

GWAS colocalisation of Zenin's healthspan set (the default query, `coloc-00c3…`: 112 partners, all GWAS): basal-cell
carcinoma (H4 0.99), facial ageing (0.98) and breast cancer (0.99), three of many skin-cancer, keratosis and other
cancer partners (read, not each quoted). The healthspan signal shares its variant with skin cancer and skin ageing
above all, and with breast cancer. For row 17.

> [q188] data.variant.credibleSets count 400

> [q189] data.variant.credibleSets.rows[20].study id gtex-v10_tx_testis_enst00000427795 studyType eqtl

> [q190] data.variant.credibleSets.rows[20].study.target approvedSymbol XPC

> [q191] data.variant.credibleSets.rows[20].variant id 3_14141910_T_C

> [q192] data.variant.credibleSets.rows[1].study id gtex-v10_exon_esophagus_gej_ensg00000154767_15_3_14147467_14147907 studyType eqtl

> [q193] data.variant.credibleSets.rows[1].variant id 3_14141910_T_C

rs1043943 (3_14141910_T_C, row 18) is in 400 credible sets, read in four pages of 100 (`variant-3_14141910_T_C-sets-p0`
to `p3`). By the sets' own study type and target, tallied, not each quoted: 321 are XPC's expression, splicing and
transcript-usage QTLs (144 eQTL, 115 sQTL, 62 tuQTL), 54 XPC-AS1's, 17 an unnamed gene's (ENSG00000268279), 3 others'
(LSM3, FAM194C), none TMEM43's; the lead itself tops 43 of XPC's (two quoted: a GTEx testis transcript of XPC,
P 1.4 × 10⁻⁵², and a GTEx oesophagus exon of XPC, P 8.7 × 10⁻⁶²).

> [q194] data.variant.credibleSets count 5

> [q195] data.variant.credibleSets.rows[1].study id GCST90475214 traitFromSource High blood pressure / hypertension

> [q196] data.variant.credibleSets.rows[1].variant id 3_14115290_G_T

> [q197] data.variant.credibleSets.rows[0].study id GCST90691788 traitFromSource Impedance of arm left (UKB data field 23110)

Only 5 of the 400 are GWAS sets (`variant-3_14141910_T_C-gwas`): arm impedance (three), hypertension and a
repeat-count trait, each led by another variant (hypertension by 3_14115290_G_T). No longevity, lifespan or
healthspan set holds the lead, so causal confidence for the row's claim is not assessable (D17.2) and there is no set
for L2G or colocalisation. For row 18.

> [q198] data.variant.credibleSets count 1

> [q199] data.variant.credibleSets.rows[0].study id GCST012419 traitFromSource Longevity (100 years and older) studyType gwas target null

> [q200] data.credibleSet studyLocusId ab13a68d63289f1922a881c2fcd8b7af finemappingMethod PICS confidence PICS fine-mapped credible set based on reported top hit credibleSetIndex null

> [q201] data.credibleSet.locus count 1

> [q202] data.credibleSet.locus.rows[0] posteriorProbability 1

> [q203] data.credibleSet.l2GPredictions.rows[0] score 0.4262925982475281

> [q204] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol LRRC3B

> [q205] data.credibleSet.colocalisation count 0

rs78043944 (3_26327009_G_A, row 19) is in one credible set, Gurinovich's own (GCST012419): PICS from the reported top
hit, one variant at posterior probability 1. A rare variant with no LD partners in the reference makes a one-variant
PICS set by construction, so the PIP restates the lead rather than resolving a locus. L2G's top gene LRRC3B, 0.43;
no colocalisation.

> [q206] data.variant.credibleSets.rows[0] studyLocusId ab13a68d63289f1922a881c2fcd8b7af pValueMantissa 4 pValueExponent -9 beta 5.8755207

The set's "beta 5.8755207" is the catalog's, so the paper's score Z again (db-gwascatalog-2026.10.29#q135). For row 19.

## rs2643826 (SLC4A7), for row 20

> [q207] data.variant.credibleSets count 142

> [q208] data.variant.credibleSets.rows[32] studyLocusId 2971a8aaede7e142cb445b09ec0974b1 pValueMantissa 1 pValueExponent -9 beta -0.006323946

> [q209] data.variant.credibleSets.rows[32].study id GCST90321079 traitFromSource Aging studyType gwas target null

> [q210] data.credibleSet finemappingMethod PICS confidence PICS fine-mapped credible set based on reported top hit

> [q211] data.credibleSet.locus count 3

> [q212] data.credibleSet.locus.rows[0] posteriorProbability 0.9262218562612249

> [q213] data.credibleSet.l2GPredictions.rows[0] score 0.5290349721908569

> [q214] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol SLC4A7

> [q215] data.credibleSet.l2GPredictions.rows[2] score 0.058627791702747345

> [q216] data.credibleSet.l2GPredictions.rows[2].target approvedSymbol NEK10

> [q217] data.credibleSet.colocalisation count 145

> [q218] data.credibleSet.colocalisation.rows[0] rightStudyType gwas h4 0.9999718769712762 clpp 0.9261894178685103

> [q219] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study id GCST90473520 traitFromSource ICD10 I10-I15: Hypertensive diseases studyType gwas target null

> [q220] data.variant.credibleSets.rows[5] studyLocusId 07c13f437ee1123b7664e1a1cdcefc49 pValueMantissa 1.4179999828338623 pValueExponent -22 beta 0.0486221465072313

> [q221] data.variant.credibleSets.rows[5].study id FINNGEN_R12_I9_HYPTENS traitFromSource Hypertension studyType gwas target null

> [q222] data.credibleSet finemappingMethod SuSie confidence SuSiE fine-mapped credible set with in-sample LD

> [q223] data.credibleSet.locus count 1

> [q224] data.credibleSet.locus.rows[0] posteriorProbability 0.995090075085926

> [q225] data.credibleSet.l2GPredictions.rows[0] score 0.5452383160591125

> [q226] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol SLC4A7

> [q227] data.variant.credibleSets.rows[76] studyLocusId 8017c5372316dc883cbd32b16e49c41a pValueMantissa 2.0840001106262207 pValueExponent -11 beta 0.00693494

> [q228] data.variant.credibleSets.rows[76].study id GCST90892633 traitFromSource Chronic kidney disease fast progression risk score (including urine markers) studyType gwas target null

rs2643826 (3_27521497_C_T) is in 142 credible sets (q207), all GWAS, nearly all blood pressure, hypertension and its
drugs; none is a QTL set. Rosoff's mvAge set (GCST90321079, q208, q209; β −0.0063 per T, the alternative allele, so
C raises the factor): PICS from the reported top hit, three variants, the lead at PIP 0.926 (q210 to q212); L2G
SLC4A7 0.529, NEK10 0.059 (q213 to q216); 145 colocalisations (q217), every one with another GWAS set (the second
page, `set-2971a8aa-coloc2`, holds the other 45), led by hypertensive disease at H4 1.00 (q218, q219); none with an
expression or other QTL set. FinnGen R12's hypertension set (q220, q221; β +0.049 per T): SuSiE with in-sample LD,
one variant, the lead at PIP 0.995 (q222 to q224); L2G SLC4A7 0.545 (q225, q226). The lead also leads a set for a chronic
kidney disease fast-progression risk score (GCST90892633), β +0.0069 per T (q227, q228): C on the lower-score side by Open Targets'
orientation, not checked against the study, which the catalog's 63 records do not hold. For row 20.

## rs9872864 and rs2271961 (IP6K1), for row 21

> [q229] data.variant.credibleSets count 538

> [q230] data.variant.credibleSets count 431

rs9872864 (3_49754590_A_G) lies in 538 credible sets, rs2271961 (3_49840680_T_C) in 431. Paging every set (a
reading, not cached as one file): two are of a scoring class, Wright 2019's mothers' set and Rosoff 2023's mvAge
set below, and each SNP is in both. The rest are GWAS of other traits and QTL sets. rs9872864 leads no other set.
rs2271961 leads one GWAS set of another trait, Friligkou 2024's anxiety disorder (PICS, P 2e-9; its catalog record
is db-gwascatalog-2026.10.29#q172), and GTEx expression, transcript and splicing sets for UBA7 and RNF123 (artery,
liver, brain, lung, thyroid, heart, testis); none of these is colocalised with a scoring set (q240).

> [q231] data.credibleSet finemappingMethod PICS confidence PICS fine-mapped credible set based on reported top hit

> [q232] data.credibleSet.study id GCST009449 traitFromSource Parental longevity (mother's age at death or mother's attained age)

> [q233] data.credibleSet.locus count 78

> [q234] data.credibleSet.locus.rows[0] posteriorProbability 0.02040303431189384

> [q235] data.credibleSet.locus.rows[56] posteriorProbability 0.011291352787322049

> [q236] data.credibleSet.locus.rows[56].variant id 3_49840680_T_C

Wright 2019's mothers' set (GCST009449): PICS from the reported top hit, 78 variants. rs9872864 leads it at
posterior 0.020; rs2271961 is in it at 0.011 (row 56 of the member list). The posteriors are flat, about 0.01 to 0.02
each: the set marks a region and picks no variant.

> [q237] data.credibleSet.l2GPredictions.rows[0] score 0.10563313961029053

> [q238] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol MST1R

> [q239] data.credibleSet.l2GPredictions.rows[4].target approvedSymbol IP6K1

L2G's top gene is MST1R at 0.11; IP6K1 is fifth at 0.064. No gene is near 0.5.

> [q240] data.credibleSet.colocalisation count 201

201 colocalisations for each of the two sets (this line is in both sets' files; three pages each read). All 201
are with GWAS sets, none with an expression, splicing or protein QTL. The GWAS partners at H4 ≥ 0.8 are blood
pressure and hypertension, intelligence and educational attainment, serum vitamin D, lung function (FEV1, peak
flow), HDL lipid fractions, pain and post-traumatic stress, among others. Colocalisation carries no direction.

> [q241] data.credibleSet.study id GCST90321079 traitFromSource Aging

> [q242] data.credibleSet.locus count 80

> [q243] data.credibleSet.locus.rows[0] posteriorProbability 0.02281116119543302

> [q244] data.credibleSet.locus.rows[31] posteriorProbability 0.01294394708269974

Rosoff 2023's mvAge set (GCST90321079): PICS from the reported top hit (the same method line as q231), 80 variants;
rs2271961 leads at 0.023, rs9872864 is in it at 0.013 (row 31).

> [q245] data.credibleSet.l2GPredictions.rows[0] score 0.19249854981899261

> [q246] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol GMPPB

Its L2G top gene is GMPPB at 0.19. No gene reaches 0.5 in either set.

## Reading 2026-11-11, record

The two IP6K1 scoring sets (a8824020, 97f2e5d9; row 21) re-queried for colocalisation with QTL sets, which the earlier
query (q240, GWAS partners only) did not return: Open Targets lists QTL partners only when `studyTypes` names them.

> [q247] data.credibleSet.colocalisation count 530

530 QTL colocalisations for each set (three pages of 200 read for each). At H4 ≥ 0.8, 484 and 485, spread over at
least a dozen genes: RNF123 311 each, UBA7 117, INKA1 16, CDHR4 8, GMPPB and MST1R 5, MST1 and RBM6 4, TRAIP 3,
IP6K1 2. Expression, transcript-usage and splicing QTLs, most from GTEx.

> [q248] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study.target approvedSymbol RNF123

> [q249] data.credibleSet.colocalisation.rows[2].otherStudyLocus.study.target approvedSymbol UBA7

The first rows: RNF123 (an oesophageal-mucosa expression QTL, H4 0.93) and UBA7. No single gene: effector E3 stands on
ambiguity, not on an absence of QTL colocalisation. For row 21.

## Reading 2026-11-11, record

NLGN1's lead rs472103 (3_173404702_A_C), row 24.

> [q250] data.variant.credibleSets count 180

180 credible sets hold the variant (two pages read): 179 GWAS and one expression QTL. The only one of a scoring class
is Rosoff's mvAge set (GCST90321079); no lifespan, longevity or healthspan GWAS set holds it. The rest are adiposity
and body composition (BMI ten, weight, waist, hip, fat mass and percentages), type 2 diabetes, reticulocyte
measures, lipoprotein and fatty-acid fractions, smoking initiation and insomnia.

> [q251] data.variant.credibleSets.rows[7] studyLocusId 05b358d81029716a026befb58c86a556 pValueMantissa 7 pValueExponent -17 beta 0.01618

> [q252] data.variant.credibleSets.rows[7].study id GCST90301650 traitFromSource Body mass index studyType gwas target null

> [q253] data.variant.credibleSets.rows[7].variant id 3_173396515_A_G

Hawkes's BMI set, led by rs529200 (3_173396515_A_G): β +0.0162 per G. G is the allele that rides with the lead's C
(db-ensembl-116#q114, q115, derived), so the lead's A lowers BMI. Of the 37 body-size and body-composition sets
(BMI, weight, waist, hip, fat and fat-free mass) led by rs529200, rs583514 or rs247975, each counting the allele that
rides with the lead's C by the same frequency reading, 32 give that allele the higher value, 3 print no β, and
Harris 2024's two (below) run the other way.

> [q254] data.variant.credibleSets.rows[56] studyLocusId 4c4290dfb79586288be204fcdc8ad9e3 pValueMantissa 3 pValueExponent -15 beta -0.0190525

> [q255] data.variant.credibleSets.rows[56].study id GCST90428119 traitFromSource Body mass index studyType gwas target null

Harris 2024's BMI set (GCST90428119): β −0.019 per G, the other way; its whole-body fat-mass set too. Against the
rest, not read further.

> [q256] data.variant.credibleSets.rows[66] studyLocusId 5648327c81f4793b9b1ac29e066ad5fd pValueMantissa 2 pValueExponent -11 beta 0.0254

> [q257] data.variant.credibleSets.rows[66].study id GCST010557 traitFromSource Type 2 diabetes studyType gwas target null

> [q258] data.variant.credibleSets.rows[66].variant id 3_173389653_T_C

A type 2 diabetes set led by rs247975 (3_173389653_T_C): β +0.025 per C, C riding with the lead's C (pmid-31484785
q59's reading): the lead's A goes with less type 2 diabetes too, not a trade-off.

> [q259] data.credibleSet finemappingMethod PICS confidence PICS fine-mapped credible set based on reported top hit

> [q260] data.credibleSet.locus count 16

> [q261] data.credibleSet.locus.rows[0] posteriorProbability 0.14131993002576904

> [q262] data.credibleSet.locus.rows[1] posteriorProbability 0.09462180972921529

Rosoff's mvAge set: PICS from the reported top hit, 16 variants; rs472103 leads at 0.141, the next at 0.095.

> [q263] data.credibleSet.l2GPredictions.rows[0] score 0.9233385324478149

> [q264] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol NLGN1

Locus-to-gene: NLGN1 at 0.92.

> [q265] data.credibleSet.colocalisation count 2

> [q266] data.credibleSet.colocalisation.rows[0] rightStudyType eqtl h4 0.9734951346983705 clpp 0.0324101844088943

> [q267] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study.target approvedSymbol NLGN1

Queried with the QTL study types: two QTL colocalisations, both NLGN1 expression (the gene, H4 0.975, and its
transcript ENST00000423427, H4 0.973; brain dorsolateral prefrontal cortex, CommonMind).

> [q268] data.credibleSet.colocalisation count 223

223 colocalisations with GWAS sets (three pages read), dominated at H4 ≥ 0.8 by BMI, weight, waist, hip and fat
mass, with type 2 diabetes, reticulocytes, lipoprotein fractions, smoking initiation and insomnia. Colocalisation
carries no direction.

## Reading 2026-11-11, record

The QTL colocalisation sweep. The colocalisations read before 2026-11-11 came from queries that named no `studyTypes`, and Open Targets then
returns GWAS partners only. Every row with a scoring credible set is re-read here with the QTL types named (eQTL,
sQTL, transcript-usage QTL, pQTL and their single-cell forms) and `isTransQtl` asked, each set cached as
`set-<first 8 of studyLocusId>-coloc-qtl[-pN]`. A gene is counted when a cis colocalisation (`isTransQtl false`)
reaches H4 ≥ 0.8, tallied from the cached pages, not each quoted; ambiguity is read by D24.

### rs1275922 (KCNK3), for row 12

> [q269] data.credibleSet.colocalisation count 6

> [q270] data.credibleSet.colocalisation.rows[1] rightStudyType eqtl h4 0.9964101021828494 clpp 0.20011817201137583

> [q271] data.credibleSet.colocalisation.rows[1].otherStudyLocus isTransQtl false

> [q272] data.credibleSet.colocalisation.rows[1].otherStudyLocus.study.target approvedSymbol KCNK3

Timmers 2019's set (197bf4ed): six QTL colocalisations, five at H4 ≥ 0.8, all cis and all KCNK3 (expression and
exon-level expression, GTEx v10), the best H4 0.996 in pancreas exon expression. Rosoff's mvAge set (e43a6d14) gives
the same five KCNK3 colocalisations:

> [q273] data.credibleSet.colocalisation count 6

KCNK3 is the top locus-to-gene gene (0.85, q104) and the only gene that colocalises: `effector:E1`, KCNK3.

### rs2613508 (NEGR1), for row 4

> [q274] data.credibleSet.colocalisation count 7

> [q275] data.credibleSet.colocalisation.rows[6] rightStudyType eqtl h4 0.9536593154699168 clpp 0.018212063210753512

> [q276] data.credibleSet.colocalisation.rows[6].otherStudyLocus isTransQtl false

> [q277] data.credibleSet.colocalisation.rows[6].otherStudyLocus.study.target approvedSymbol NEGR1

Rosoff's mvAge set (abc062e8): seven QTL colocalisations, six at H4 ≥ 0.8, all cis and all NEGR1 (five expression,
one splicing; q275 is HipSci's iPSC exon expression). NEGR1 is the top locus-to-gene gene (0.56, q50) and the only
gene that colocalises: `effector:E1`, NEGR1.

### rs1556516 (CDKN2B-AS1, 9p21), for row 57

The six lifespan-class sets holding the lead (`credibleSets-longevity8-9_22100177_G_C.json`): Timmers 2019's
(02462f21), Timmers 2020's (410c05db), Pilling 2017's combined parents (9215fe6d) and GCST006702 (e1251d1f), Rosoff's
mvAge (a21d3ccc) and Zenin's healthspan (afbd1892). Timmers 2019's:

> [q278] data.credibleSet.colocalisation count 3

> [q279] data.credibleSet.colocalisation.rows[1] rightStudyType eqtl h4 0.9489403556825597 clpp 0.016535715593562313

> [q280] data.credibleSet.colocalisation.rows[1].otherStudyLocus isTransQtl false

> [q281] data.credibleSet.colocalisation.rows[1].otherStudyLocus.study.target approvedSymbol CDKN2B

Three QTL colocalisations, all CDKN2B, one at H4 ≥ 0.8 (TwinsUK adipose exon expression, q279; the other two, brain
cortex expression and exon expression, below). Each of the other five sets holds one, the same TwinsUK CDKN2B exon
QTL, cis, at H4 0.937 to 0.964; Timmers 2020's:

> [q282] data.credibleSet.colocalisation count 1

> [q283] data.credibleSet.colocalisation.rows[0] rightStudyType eqtl h4 0.9368543387185756 clpp 0.013231475401459226

> [q284] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study.target approvedSymbol CDKN2B

CDKN2B is the only gene that colocalises, on every set; locus-to-gene is below 0.5 for every gene (CDKN2B 0.36,
q18), so colocalisation alone: `effector:E2`, CDKN2B. One adipose exon QTL carries it, a thin basis.
