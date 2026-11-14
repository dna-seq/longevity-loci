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

### rs61905747 (ZW10/TTC12), for row 67

Timmers 2020's multivariate set (43f2d00e), the only lifespan-class set in the window (q24's prose):

> [q285] data.credibleSet.colocalisation count 15

> [q286] data.credibleSet.colocalisation.rows[11] rightStudyType eqtl h4 0.9972065574855874 clpp 0.23815112477463007

> [q287] data.credibleSet.colocalisation.rows[11].otherStudyLocus isTransQtl false

> [q288] data.credibleSet.colocalisation.rows[11].otherStudyLocus.study.target approvedSymbol USP28

Fifteen QTL colocalisations, every one USP28's (expression and exon-level expression across GTEx v10, HipSci and
Geuvadis), two at H4 ≥ 0.8, both cis: GTEx v10 muscle (q286) and blood (0.997) gene expression; the other thirteen
at H4 0.04 to 0.58. No other gene colocalises, and no gene passes locus-to-gene (CLDN25 0.35, q27): colocalisation
alone, `effector:E2`, USP28, which Timmers 2020's SMR also names (pmid-32678081#q7).

### rs6224 (FES/FURIN), for row 81

The three lifespan-class sets holding the lead (`credibleSets-longevity8-15_90880313_G_T.json`): Timmers 2019's
(e95e1989), Pilling 2017's combined parents (0095b2a9) and Timmers 2020's (92b21d13). Timmers 2019's:

> [q289] data.credibleSet.colocalisation count 130

> [q290] data.credibleSet.colocalisation.rows[38] rightStudyType tuqtl h4 0.9952958338118982 clpp 0.1603052972733388

> [q291] data.credibleSet.colocalisation.rows[38].otherStudyLocus isTransQtl false

> [q292] data.credibleSet.colocalisation.rows[38].otherStudyLocus.study.target approvedSymbol FES

> [q293] data.credibleSet.colocalisation.rows[6] rightStudyType sqtl h4 0.9931848190271538 clpp 0.11703028162415956

> [q294] data.credibleSet.colocalisation.rows[6].otherStudyLocus isTransQtl false

> [q295] data.credibleSet.colocalisation.rows[6].otherStudyLocus.study.target approvedSymbol FURIN

At H4 ≥ 0.8, 120 cis colocalisations: FES 113 (expression, splicing, transcript usage, single-cell and one pQTL;
q290 a macrophage transcript-usage QTL) and FURIN 7 (q293 a GTEx tibial-nerve splicing QTL). The other two sets
hold the same partners, 130 each (FES 114 and 113, FURIN 8 and 7):

> [q296] data.credibleSet.colocalisation count 130

FURIN meets a criterion of its own (cis colocalisation) but holds under a tenth of the locus's colocalisations (7
of 120) and does not pass locus-to-gene (0.15 on this set, q35's prose), so it is no rival
under D24. FES passes locus-to-gene (0.97) and colocalises: `effector:E1`, FES.

### rs1556516 (9p21), continued, for row 57

The locus-to-gene scores of the other five sets, read after q278-q284 were written (D24 counts a rival that passes
locus-to-gene): CDKN2B tops each (each cached as `set-<first 8>-l2g`), 0.35 to 0.49 on four, and passes on Pilling 2017's combined-parents age-at-death
set (GCST006702, `set-e1251d1f-l2g`, led by rs1537373 and holding the lead):

> [q297] data.credibleSet.study id GCST006702 traitFromSource Parental longevity (combined parental age at death)

> [q298] data.credibleSet.l2GPredictions.rows[0] score 0.5308597087860107

> [q299] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol CDKN2B

> [q300] data.credibleSet.l2GPredictions.rows[1] score 0.22434711456298828

> [q301] data.credibleSet.l2GPredictions.rows[1].target approvedSymbol CDKN2A

On that set CDKN2B passes locus-to-gene (0.53, barely) and colocalises (the TwinsUK exon QTL, H4 0.964), and no
other gene passes either criterion: `effector:E1`, CDKN2B, by the letter on one set, the others at E2.

The highest of the other four, Pilling 2017's GCST006697 set (9215fe6d):

> [q302] data.credibleSet.l2GPredictions.rows[0] score 0.4910053312778473

### rs78438918 (AFF3), for row 15

Rosoff's mvAge set (63ebc186), the row's only lifespan-class set:

> [q303] data.credibleSet.colocalisation count 33

> [q304] data.credibleSet.colocalisation.rows[15] rightStudyType eqtl h4 0.9911823824469108 clpp 0.09257875016778748

> [q305] data.credibleSet.colocalisation.rows[15].otherStudyLocus isTransQtl false

> [q306] data.credibleSet.colocalisation.rows[15].otherStudyLocus.study.target approvedSymbol AFF3

> [q307] data.credibleSet.colocalisation.rows[30] rightStudyType eqtl h4 0.9746639712488064 clpp 0.03365484383727946

> [q308] data.credibleSet.colocalisation.rows[30].otherStudyLocus isTransQtl false

> [q309] data.credibleSet.colocalisation.rows[30].otherStudyLocus.study.target approvedSymbol ENSG00000230393

At H4 ≥ 0.8, 24 cis colocalisations: AFF3 18 (15 expression, 3 transcript usage; q304 GTEx caudate) and
ENSG00000230393, a gene without an approved symbol beside AFF3, 6 (expression, all exon-level; q307 GTEx testis).
AFF3 passes locus-to-gene (0.90, q136) and colocalises, E1 on its own; but ENSG00000230393 meets a criterion of its
own (cis colocalisation) and holds 6 of 24, at least a tenth, so under D24 the call is ambiguous: `effector:E3`, no
gene named (the lead's ruling on this row, 2026-11-11).

### rs11065979 (ATXN2/SH2B3), for row 71

The five lifespan-class sets holding the lead (`credibleSets-longevity8-12_111621753_C_T.json`): Timmers 2019's
(8a1b141e), Timmers 2020's (73d47418, the set behind q23's SH2B3 0.95), Pilling 2017's GCST006702 (82d18dcd), GCST009450
(d9840ebd) and Rosoff's mvAge (01b6835c). Timmers 2019's and Timmers 2020's:

> [q310] data.credibleSet.colocalisation count 443

> [q311] data.credibleSet.colocalisation.rows[158] rightStudyType eqtl h4 0.9685816794097922 clpp 0.027047107100935316

> [q312] data.credibleSet.colocalisation.rows[158].otherStudyLocus isTransQtl false

> [q313] data.credibleSet.colocalisation.rows[158].otherStudyLocus.study.target approvedSymbol ALDH2

> [q314] data.credibleSet.colocalisation count 330

> [q315] data.credibleSet.colocalisation.rows[73] rightStudyType eqtl h4 0.9894962321629834 clpp 0.07826537590308755

> [q316] data.credibleSet.colocalisation.rows[73].otherStudyLocus isTransQtl false

> [q317] data.credibleSet.colocalisation.rows[73].otherStudyLocus.study.target approvedSymbol ALDH2

Of the 443, 432 reach H4 ≥ 0.8 and all but one are trans (`isTransQtl true`; all 442 non-eQTL partners are
protein QTLs): the locus is a broad trans-pQTL hub. The one cis colocalisation is ALDH2's (a BLUEPRINT neutrophil
transcript, q311). The other four sets give the same: 330, 438, 409 and 144 QTL colocalisations, the cis one ALDH2's
on three (q315 on Timmers 2020's), none cis on mvAge's:

> [q318] data.credibleSet.colocalisation count 438

> [q319] data.credibleSet.colocalisation count 409

> [q320] data.credibleSet.colocalisation count 144

SH2B3 passes locus-to-gene (0.95, q23) but colocalises nowhere; ALDH2 meets a criterion of its own (cis
colocalisation) and holds every cis colocalisation: two genes, each on a different criterion, so under D24 the call
is ambiguous, `effector:E3`, no gene named (the lead's ruling on this row, 2026-11-11).

### rs646776 (CELSR2/PSRC1/SORT1), for row 6

Pilling 2017's fathers' set (1a658d9f), the row's only lifespan-class set (q29's prose):

> [q321] data.credibleSet.colocalisation count 153

> [q322] data.credibleSet.colocalisation.rows[97] rightStudyType eqtl h4 0.995913527601195 clpp 0.18801749224528802

> [q323] data.credibleSet.colocalisation.rows[97].otherStudyLocus isTransQtl false

> [q324] data.credibleSet.colocalisation.rows[97].otherStudyLocus.study.target approvedSymbol PSRC1

> [q325] data.credibleSet.colocalisation.rows[128] rightStudyType eqtl h4 0.9966203633591767 clpp 0.22160667286621008

> [q326] data.credibleSet.colocalisation.rows[128].otherStudyLocus isTransQtl false

> [q327] data.credibleSet.colocalisation.rows[128].otherStudyLocus.study.target approvedSymbol CELSR2

> [q328] data.credibleSet.colocalisation.rows[145] rightStudyType eqtl h4 0.995088419409183 clpp 0.15587794660913037

> [q329] data.credibleSet.colocalisation.rows[145].otherStudyLocus isTransQtl false

> [q330] data.credibleSet.colocalisation.rows[145].otherStudyLocus.study.target approvedSymbol SORT1

All 153 reach H4 ≥ 0.8; 39 are trans (protein QTLs), and of the 114 cis, PSRC1 holds 56 (expression), CELSR2 38
(expression and splicing), SORT1 16, ATXN7L2 2 and SYPL2 2. SORT1 (0.99) and CELSR2 (0.97) both pass
locus-to-gene (q30) and both colocalise, and PSRC1 colocalises most: under D24 the call is ambiguous,
`effector:E3`, no gene named (the lead's ruling on this row, 2026-11-11).

### The rows whose level stands: 2, 7, 19, 80, 20, 46 and 93

rs3768321 (PABPC4), row 2, Rosoff's mvAge set (0980823f; the row's only lifespan-class set):

> [q331] data.credibleSet.colocalisation count 296

> [q332] data.credibleSet.colocalisation.rows[38] rightStudyType sqtl h4 0.9953748047000629 clpp 0.16454838092960156

> [q333] data.credibleSet.colocalisation.rows[38].otherStudyLocus isTransQtl false

> [q334] data.credibleSet.colocalisation.rows[38].otherStudyLocus.study.target approvedSymbol PABPC4

> [q335] data.credibleSet.colocalisation.rows[119] rightStudyType eqtl h4 0.9561806999771456 clpp 0.019336944453125005

> [q336] data.credibleSet.colocalisation.rows[119].otherStudyLocus isTransQtl false

> [q337] data.credibleSet.colocalisation.rows[119].otherStudyLocus.study.target approvedSymbol MACF1

> [q338] data.credibleSet.colocalisation.rows[21] rightStudyType eqtl h4 0.9953748047000629 clpp 0.1682440409601266

> [q339] data.credibleSet.colocalisation.rows[21].otherStudyLocus isTransQtl false

> [q340] data.credibleSet.colocalisation.rows[21].otherStudyLocus.study.target approvedSymbol PABPC4-AS1

At H4 ≥ 0.8, 221 colocalisations, 220 cis: PABPC4 135 (splicing, expression, transcript usage), MACF1 38,
PABPC4-AS1 28, BMP8A 11, PPIEL 7, BMP8B 1. MACF1 and PABPC4-AS1 each meet a criterion of their own and hold more
than a tenth, and no gene passes locus-to-gene (PABPC4 0.23): ambiguous under D24, `effector:E3` stands.

rs1230666 (MAGI3/PTPN22), row 7, Timmers 2019's set (f53bfb83) and mvAge's (342a0b5f):

> [q341] data.credibleSet.colocalisation count 75

> [q342] data.credibleSet.colocalisation.rows[26] rightStudyType eqtl h4 0.9838425909855892 clpp 0.052902225186811994

> [q343] data.credibleSet.colocalisation.rows[26].otherStudyLocus isTransQtl false

> [q344] data.credibleSet.colocalisation.rows[26].otherStudyLocus.study.target approvedSymbol PHTF1

> [q345] data.credibleSet.colocalisation.rows[29] rightStudyType eqtl h4 0.9967581725800437 clpp 0.21289834114753012

> [q346] data.credibleSet.colocalisation.rows[29].otherStudyLocus isTransQtl false

> [q347] data.credibleSet.colocalisation.rows[29].otherStudyLocus.study.target approvedSymbol RHOC

> [q348] data.credibleSet.colocalisation count 75

Timmers 2019's: 24 at H4 ≥ 0.8, 6 trans protein QTLs, 18 cis: PHTF1 17, RHOC 1 (q345, a GTEx brain-cortex
transcript). mvAge's: 8 at H4 ≥ 0.8, 6 trans, 2 cis: PHTF1 1, RHOC 1. Over both sets RHOC holds 2 of 20, a tenth,
which D24 counts as a rival; no gene passes locus-to-gene (PHTF1 0.42, q62): `effector:E3` stands, at the edge.

rs78043944 (row 19), Gurinovich's own set (ab13a68d), with the QTL types named (q205 was the default query):

> [q349] data.credibleSet.colocalisation count 0

rs8042849 (CHRNB4/CHRNA5), row 80, Timmers 2019's set (8d0d0d1e):

> [q350] data.credibleSet.colocalisation count 47

> [q351] data.credibleSet.colocalisation.rows[12] rightStudyType eqtl h4 0.9977076684221937 clpp 0.2753931481442404

> [q352] data.credibleSet.colocalisation.rows[12].otherStudyLocus isTransQtl false

> [q353] data.credibleSet.colocalisation.rows[12].otherStudyLocus.study.target approvedSymbol PSMA4

> [q354] data.credibleSet.colocalisation.rows[13] rightStudyType eqtl h4 0.9784749800754303 clpp 0.039472056823559795

> [q355] data.credibleSet.colocalisation.rows[13].otherStudyLocus isTransQtl false

> [q356] data.credibleSet.colocalisation.rows[13].otherStudyLocus.study.target approvedSymbol CHRNA5

At H4 ≥ 0.8, 36, all cis: PSMA4 16, CHRNA5 14, ENSG00000261762 3, IREB2 2, CHRNA3 1. PSMA4 and CHRNA5 each hold
well over a tenth and neither passes locus-to-gene (CHRNA5 0.29, q14): ambiguous under D24, `effector:E3` stands.

rs2643826 (SLC4A7), row 20, mvAge's set (2971a8aa), with the QTL types named: none, as q217's prose read from the
GWAS partners.

> [q357] data.credibleSet.colocalisation count 0

rs10455872 (LPA), row 46, Timmers 2019's set (9a28de1c): six QTL colocalisations, all trans protein QTLs (CXCL13,
CCL27 and others), none of LPA:

> [q358] data.credibleSet.colocalisation count 6

rs6511720 (LDLR), row 93, the set of q9 (03c51795): four, three trans protein QTLs (PCSK9 among them) and one cis
KRI1 expression QTL at H4 0.61, below 0.8:

> [q359] data.credibleSet.colocalisation count 4

46 and 93 keep `effector:E2` on locus-to-gene alone (LPA 0.56, LDLR), with no cis colocalisation to add or to rival.

### Every lifespan-class set, the remaining rows

The sets of the eight lifespan-class studies holding each lead (`credibleSets-longevity8-<variant>.json`), so that
no row rests on one set where it has more; each set's QTL colocalisations (`set-<8>-coloc-qtl`) and locus-to-gene
scores (`set-<8>-l2g`) are cached. Rows 2, 4, 15 and 20 have one such set each, the one read above (mvAge's), and
row 19 none. The others:

Row 46 (rs10455872): six sets (Timmers 2019's, Timmers 2020's, Pilling's two, Zenin's healthspan, mvAge's), each
with the same six trans protein QTLs and no cis colocalisation; LPA passes locus-to-gene on every one (0.56 to 0.67).
Zenin's:

> [q360] data.credibleSet.study id GCST007406 traitFromSource Healthspan

> [q361] data.credibleSet.l2GPredictions.rows[0] score 0.6650680303573608

> [q362] data.credibleSet.colocalisation count 6

Row 93 (rs6511720): four sets (Timmers 2019's, Timmers 2020's, GCST009450's, mvAge's), each with three trans protein
QTLs and no cis colocalisation at H4 ≥ 0.8; LDLR passes locus-to-gene on every one (0.96). mvAge's:

> [q363] data.credibleSet.l2GPredictions.rows[0] score 0.9613806009292603

> [q364] data.credibleSet.colocalisation count 4

So 46 and 93 keep `effector:E2` on locus-to-gene alone, with no rival.

Row 80 (rs8042849): five sets. On each, PSMA4 (14 to 16) and CHRNA5 (14) hold the cis colocalisations at H4 ≥ 0.8,
with CHRNA3 (1 to 5), IREB2 and ENSG00000261762 fewer. CHRNA5 passes locus-to-gene on Pilling 2017's
combined-parents age-at-death set (0.75; 0.17 to 0.43 on the other four) and so meets E1 there by the letter, but
PSMA4 colocalises as often: a rival under D24, `effector:E3` stands.

> [q365] data.credibleSet.study id GCST006702 traitFromSource Parental longevity (combined parental age at death)

> [q366] data.credibleSet.l2GPredictions.rows[0] score 0.748673677444458

> [q367] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol CHRNA5

> [q368] data.credibleSet.colocalisation count 47

Row 6 (rs646776): of the eight studies only GCST009450 holds the lead (09f4c8bb; Pilling's fathers' GCST006701 set,
read above, is outside the eight), with the same partners: 111 cis at H4 ≥ 0.8, PSRC1 55, CELSR2 37, SORT1 15;
SORT1 0.99 and CELSR2 0.87 by locus-to-gene. E3 stands.

> [q369] data.credibleSet.colocalisation count 153

Row 67 (rs61905747): mvAge's set (b4aa6d2c) beside Timmers 2020's, the same fifteen USP28 colocalisations (two at H4 ≥
0.8) and the same locus-to-gene (CLDN25 0.35). E2 USP28 stands.

> [q370] data.credibleSet.colocalisation count 15

## Reading 2026-11-11, record

Row 25 (HTT, rs61348208). The lifespan-class credible sets holding the lead (credibleSets-longevity8-4_3087837_C_T),
mvAge's lead rs16843836 (…-4_3111610_G_A) and Atkins' rs82334 (…-4_3223644_A_C); then each set's locus-to-gene and
its QTL colocalisations (cis only, H4 ≥ 0.8, D24), and the GWAS colocalisations of Timmers' set.

### The sets

> [q371] data.credibleSets.rows[0] studyLocusId 0818ea59a9a46aca027bfbba5eb497b7 finemappingMethod PICS

> [q372] data.credibleSets.rows[0].locus count 70

> [q373] data.credibleSets.rows[0].locus.rows[0] posteriorProbability 0.1082559275924237

> [q374] data.credibleSets.rows[0].locus.rows[1] posteriorProbability 0.02896975667294271

> [q375] data.credibleSets.rows[1] studyLocusId 0e5bde677354457e3a8c7a15e5ad6db3 finemappingMethod PICS

> [q376] data.credibleSets.rows[1].locus count 39

> [q377] data.credibleSets.rows[1].locus.rows[0] posteriorProbability 0.06437204866041868

> [q378] data.credibleSets.rows[1].locus.rows[17] posteriorProbability 0.025358859835719

Of the eight lifespan-class studies, one set holds rs61348208: Timmers 2019's (GCST009890, 0818ea59, PICS), 70
variants, the lead first at PIP 0.108, the next 0.029. mvAge's set (GCST90321079, 0e5bde67, PICS, 39 variants) is led
by rs16843836 at 0.064 and holds rs82334 (0.025), not rs61348208. The queries by variant return Timmers' set for
rs16843836 and rs82334 as well (each count 2); the listing above shows only the first 25 of its 70 variants, and the
set's own locus filtered to the two (set-0818ea59-locus-htt-proxies) gives their PIPs:

> [q408] data.credibleSet.locus.rows[0] posteriorProbability 0.003401829497442979

> [q409] data.credibleSet.locus.rows[1] posteriorProbability 0.0025415823557971566

rs16843836 0.0034 and rs82334 0.0025 in Timmers' set. So Timmers' set holds all three; mvAge's holds rs16843836 and
rs82334 (158's own variant), not rs61348208. The lead sits at C2 by 0.008 in a flat set: the causal variant is not
resolved.

### Locus-to-gene

> [q379] data.credibleSet.l2GPredictions.rows[0] score 0.1745876967906952

> [q380] data.credibleSet.l2GPredictions.rows[1] score 0.16904586553573608

> [q381] data.credibleSet.l2GPredictions.rows[0] score 0.5475932359695435

> [q382] data.credibleSet.l2GPredictions.rows[1] score 0.4425610899925232

Timmers' set (set-0818ea59-l2g): MSANTD1 0.17, HTT 0.17; no gene passes 0.5. mvAge's set (set-0e5bde67-l2g): MSANTD1
0.55, HTT 0.44, RGS12 0.13; MSANTD1 passes.

### QTL colocalisations
#### set 0818ea59
> [q383] data.credibleSet.colocalisation count 55

> [q384] data.credibleSet.colocalisation.rows[0] rightStudyType eqtl h4 0.9591710381281714 clpp 0.020761397319080756

> [q385] data.credibleSet.colocalisation.rows[0].otherStudyLocus isTransQtl false

> [q386] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study.target approvedSymbol HTT

> [q387] data.credibleSet.colocalisation.rows[17] rightStudyType eqtl h4 0.9617852572180127 clpp 0.022166383735073656

> [q388] data.credibleSet.colocalisation.rows[17].otherStudyLocus isTransQtl false

> [q389] data.credibleSet.colocalisation.rows[17].otherStudyLocus.study.target approvedSymbol HTT-AS

#### set 0e5bde67
> [q390] data.credibleSet.colocalisation count 29

> [q391] data.credibleSet.colocalisation.rows[10] rightStudyType sqtl h4 0.9677233946542065 clpp 0.026681861585689796

> [q392] data.credibleSet.colocalisation.rows[10].otherStudyLocus isTransQtl false

> [q393] data.credibleSet.colocalisation.rows[10].otherStudyLocus.study.target approvedSymbol HTT

> [q394] data.credibleSet.colocalisation.rows[19] rightStudyType eqtl h4 0.9611859648334469 clpp 0.021959257731845417

> [q395] data.credibleSet.colocalisation.rows[19].otherStudyLocus isTransQtl false

> [q396] data.credibleSet.colocalisation.rows[19].otherStudyLocus.study.target approvedSymbol RGS12

> [q397] data.credibleSet.colocalisation.rows[12] rightStudyType eqtl h4 0.9670476431524524 clpp 0.02596799408688351

> [q398] data.credibleSet.colocalisation.rows[12].otherStudyLocus isTransQtl false

> [q399] data.credibleSet.colocalisation.rows[12].otherStudyLocus.study.target approvedSymbol MSANTD1

Timmers' set: 55 colocalisations, 40 at H4 ≥ 0.8, all cis: HTT 37 (eQTL 19, transcript 14, splice 4; max H4 0.96,
GTEx muscle), HTT-AS 3 (eQTL; 0.96), 3 of 40, under a tenth. mvAge's set: 29, 18 at H4 ≥ 0.8, all cis: HTT 13 (splice
7, transcript 3, eQTL 3), RGS12 4, MSANTD1 1.

Under D24, counting the sets that hold the lead (Timmers' alone): HTT colocalises, no gene passes L2G and HTT-AS holds
under a tenth, so HTT at E2 by colocalisation alone. Counting mvAge's set too (the same signal, r² 0.70, holding
158's own variant rs82334 but not the lead): MSANTD1 passes L2G there (0.55), which D24 makes ambiguous, E3. Row 25
is committed at E2 by the sweep's rule of the sets that hold the lead; with 158 folded in, which sets are the row's
is put to the lead.

### GWAS colocalisations of Timmers' set

> [q400] data.credibleSet.colocalisation count 100

> [q401] data.credibleSet.colocalisation.rows[10] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.953257397009372 clpp 0.018106825660253813 rightStudyType gwas

> [q402] data.credibleSet.colocalisation.rows[10].otherStudyLocus.study id GCST008059 traitFromSource Estimated glomerular filtration rate studyType gwas

> [q403] data.credibleSet.colocalisation.rows[25] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9534143518041933 clpp 0.018252438710154115 rightStudyType gwas

> [q404] data.credibleSet.colocalisation.rows[25].otherStudyLocus.study id GCST007342 traitFromSource Depression studyType gwas

> [q405] data.credibleSet.colocalisation.rows[0] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9421081552268675 clpp 0.014502214494512744 rightStudyType gwas

> [q406] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study id GCST90476457 traitFromSource white blood cell count (WBC, minimum, inv-norm transformed) studyType gwas

> [q407] data.credibleSet.colocalisation.rows[23].otherStudyLocus.study id GCST009858 traitFromSource Waist-to-hip ratio adjusted for BMI studyType gwas

(coloc-0818ea59…, eCAVIAR, 100 rows.) The set colocalises at H4 above 0.9 with white-cell and neutrophil counts,
lipid fractions in VLDL and HDL, eGFR (0.95), depression and major depression (0.95), waist-hip ratio adjusted for BMI
(0.91) and aspartate aminotransferase; frailty at 0.68. No direction is given; Timmers 2022's look-ups give some
(pmid-37118362#q9-q13). No disease of the heart, vessels or cancer leads it.

## rs7676745 (GPR78), for row 26

> [q410] data.credibleSets count 0

> [q411] data variant null

rs7676745 (4_8563820_G_A): no credible set of the eight lifespan, healthspan, longevity and current-age studies
holds it (`credibleSets-longevity8-4_8563820_G_A.json`), and Open Targets 26.09 has no record of the variant at all
(`variant-4_8563820_G_A.json`), so no locus-to-gene score or colocalisation: causal C4, effector E4. For row 26.

## Reading 2026-11-11, record

> [q412] data.meta.dataVersion year 26 month 09 data.credibleSets count 0

> [q413] data.study.credibleSets count 26

> [q414] data.study.credibleSets count 16

> [q415] data.variant.credibleSets count 103

> [q416] data.variant.credibleSets.rows[85] studyLocusId d9b910e8399daa17a3ff4c661f7db5db pValueMantissa 7 pValueExponent -18 beta -0.0166947 finemappingMethod PICS

> [q417] data.variant.credibleSets.rows[85].study id GCST90435415 traitFromSource Systolic blood pressure studyType gwas

> [q418] data.variant.credibleSets.rows[85].variant id 4_38383858_G_A

> [q419] data.variant.credibleSets.rows[8] studyLocusId 1b218179e5f97ae2ed4412930f03f923 pValueMantissa 1 pValueExponent -12 beta -0.0148223 finemappingMethod PICS

> [q420] data.variant.credibleSets.rows[8].study id GCST90435414 traitFromSource Diastolic blood pressure studyType gwas

> [q421] data.variant.credibleSets.rows[8].variant id 4_38383858_G_A

> [q422] data.credibleSet studyLocusId 594361228de1ed40760b004fe16d5198 finemappingMethod PICS confidence PICS fine-mapped credible set extracted from summary statistics pValueMantissa 3.321000099182129 pValueExponent -15 beta -0.0133237035996555

> [q423] data.credibleSet.variant id 4_38385454_T_G

> [q424] data.credibleSet.study id GCST90624049 traitFromSource Frailty (Factor 3 - Multimorbidity) pubmedId 40759756 publicationFirstAuthor Foote IF publicationDate 2025-08-04 nSamples 699030

> [q425] data.credibleSet.locus.rows[0] posteriorProbability 0.04307645512305034 r2Overall 0.9853064400822061

> [q426] data.credibleSet studyLocusId e3b10dba8389e17b4dbbbf76fca189b4 finemappingMethod SuSiE-inf confidence SuSiE fine-mapped credible set with out-of-sample LD pValueMantissa 4.064330101013184 pValueExponent -111 beta 0.012162147718968522

> [q427] data.credibleSet.study id GCST90691825 traitFromSource Lymphocyte percentage (UKB data field 30180) pubmedId 40968291 publicationFirstAuthor Karczewski KJ publicationDate 2025-09-18 nSamples 407282

> [q428] data.credibleSet.locus.rows[0] posteriorProbability 0.024664941272447127 r2Overall null

> [q429] data.credibleSet.colocalisation.rows[19] h4 0.9920087358110032 clpp 0.10170623637098505 colocalisationMethod COLOC_PIP_ECAVIAR

> [q430] data.credibleSet.colocalisation.rows[19].otherStudyLocus.study id GCST90310196 traitFromSource Systolic blood pressure (UKB data field 4080, 93, 6153 ,6177) studyType gwas

> [q431] data.credibleSet.l2GPredictions.rows[0] score 0.757474958896637 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol KLF3

> [q432] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.5372196385471243

> [q433] data.variant.alleleFrequencies[4] populationName fin_adj alleleFrequency 0.41058221126493455

rs17499404 (LINC02513, 4_38383858_G_A), for row 27. No credible set of the eight lifespan, healthspan, longevity
and current-age studies holds it (q412, `credibleSets-longevity8-4_38383858_G_A.json`). Checked because the GWAS
Catalog names it the top hit of both mvAge (GCST90321079) and Timmers 2020 (GCST011100): mvAge's 26 sets have none on
4p14 (its chromosome-4 sets lead at 4:3.11 Mb and 4:67.0 Mb; q413, `study-sets-GCST90321079.json`), and Timmers
2020's 16 sets have none on chromosome 4 (q414, `study-sets-GCST011100.json`). So causal C4 and effector E4 by the
longevity-set rule. The variant sits in 103 other sets (q415), nearly all blood pressure and hypertension. Two are
led by the variant itself, Shi 2024's (PICS): systolic pressure β −0.0167 per A, P 7 × 10⁻¹⁸ (q416-q418), and
diastolic β −0.0148 per A, P 1 × 10⁻¹² (q419-q421): A lowers blood pressure. Foote 2025's frailty multimorbidity
factor (GCST90624049, PMID 40759756, title-checked; n 699,030, its overlap with UK Biobank not read; PICS) is
led by rs2291433 (r² 0.985 here, 0.996 in 1000 Genomes; its G is the lead's A by phase, db-ensembl-116#q140-q142):
β −0.0133 per G, P 3 × 10⁻¹⁵, G less frail (q422-q425), genome-wide and healthspan-class (D23); the lead's PIP in it
is 0.043. Lymphocyte percentage (Karczewski 2025, GCST90691825; SuSiE-inf) is the locus's strongest set, P 4 × 10⁻¹¹¹,
led by rs6812640 (the lead's PIP 0.025, q426-q428), and it colocalises with the blood-pressure sets (systolic, H4
0.99, q429-q430), so blood pressure and the lymphocyte share one signal; its direction is not phased here.
Locus-to-gene on these sets is KLF3's (0.76 on the frailty set, q431; 0.75 on the lymphocyte set), not a longevity
set's, so it is named in prose only. A frequencies: q432, q433.

## Reading 2026-11-11, record

> [q434] data.credibleSet.locus.rows[0] posteriorProbability 0.07998751711179886

> [q435] data.credibleSet.l2GPredictions.rows[0] score 0.759643018245697 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol KLF3

> [q436] data.credibleSet.l2GPredictions.rows[0] score 0.7475316524505615 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol KLF3

Row 27, second pass. Shi 2024's systolic set led by rs17499404 (`credibleSet-d9b910e8399daa17a3ff4c661f7db5db.json`,
q416-q418): the lead's PIP 0.080 (q434), locus-to-gene KLF3 0.76 (q435); the lymphocyte set's KLF3 0.75 (q436). The
lymphocyte set's β +0.0122 is per rs6812640's G, which rides with the lead's A (db-ensembl-116#q147-q149): A raises
the lymphocyte percentage. Not a lifespan-class set, so KLF3 stays in prose (C4/E4 by the longevity-set rule).

## Reading 2026-11-11, record

> [q437] data variant null

> [q438] data.study.credibleSets.rows[7].variant id 4_67025923_C_T

> [q439] data.variant.credibleSets.rows[11] studyLocusId b259a8c151c1cc7b64f298d055f9966e pValueMantissa 1 pValueExponent -8 beta 0.005833901 finemappingMethod PICS

> [q440] data.variant.credibleSets.rows[11].study id GCST90321079 traitFromSource Aging studyType gwas

Row 28. rs28637671 has no record in Open Targets 26.09 under either allele order (q437: `variant-4_66914674_T_G.json`
and `variant-4_66914674_G_T.json` both return null), so no credible set of any study can hold it, and the
lifespan-class query returns none (`credibleSets-longevity8-4_66914674_T_G.json`, count 0). mvAge's set near it
(q413's listing, `study-sets-GCST90321079.json`) is led by rs13141210 (4_67025923_C_T, q438), a separate signal
(r² 0.095, db-ensembl-116#q154). So causal C4 and effector E4 for row 28, no gene. rs13141210 (for the question on its
own row): 17 sets, mvAge's among them (PICS, P 1e-8, q439, q440), the rest body fat and BMI, education, smoking,
COPD, HDL (`variant-4_67025923_C_T.json`).

## Reading 2026-11-11, record

> [q441] data.variant.credibleSets count 3

> [q442] data.variant.credibleSets.rows[0].study id GCST90692213 traitFromSource Medication for pain relief constipation heartburn - Paracetamol (UKB data field 6154) studyType gwas

> [q443] data.variant.credibleSets.rows[0].variant id 4_66855581_G_A

Row 28. Open Targets' search finds none of the lead's top proxies (rs6821811, rs56278947, rs34238324, rs28494793;
`search-<rsID>.json`, total 0). rs1481245 (4_66898102_A_G, the row's weak proxy) sits in three sets, all of UK
Biobank's paracetamol use (P 7e-10, SuSiE-inf), led by 4_66855581_G_A, rs13109040 (q441-q443), which has r² 0.39 to
the lead (db-ensembl-116#q168): not the lead's trait.

## Reading 2026-11-11, record

> [q444] data.variant id 4_140017956_T_A referenceAllele T alternateAllele A

> [q445] data.variant.credibleSets count 69

> [q446] data.meta.dataVersion year 26 month 09 data.credibleSets count 0

> [q447] data.variant.credibleSets.rows[21] studyLocusId 418745616c7c015f1ffe9ec798b288ca studyId GCST010557 pValueMantissa 2 pValueExponent -12 beta -0.0294 finemappingMethod PICS

> [q448] data.variant.credibleSets.rows[21].study traitFromSource Type 2 diabetes projectId GCST

> [q449] data.variant.credibleSets.rows[21].l2GPredictions.rows[0] score 0.7906950116157532

> [q450] data.variant.credibleSets.rows[21].l2GPredictions.rows[0].target approvedSymbol MAML3

> [q451] data.variant.credibleSets.rows[7] studyLocusId 148b669e5a11b7724aa5076cbd549dfd studyId GCST90399695 pValueMantissa 3.3310000896453857 pValueExponent -9 beta -0.036968 finemappingMethod PICS

> [q452] data.variant.credibleSets.rows[7].study traitFromSource Chronic obstructive pulmonary disease projectId GCST

> [q453] data.variant.credibleSets.rows[13] studyLocusId 2dbfd89e29bfc5e0b97446f5e0e2548e studyId GCST90475936 pValueMantissa 4.1539998054504395 pValueExponent -9 beta -0.008313254052470851 finemappingMethod SuSiE-inf

> [q454] data.variant.credibleSets.rows[13].study traitFromSource Coronary atherosclerosis (PheCode 411.4) projectId GCST

> [q455] data.variant.credibleSets.rows[13].l2GPredictions.rows[0] score 0.8399028778076172

> [q456] data.variant.credibleSets.rows[13].l2GPredictions.rows[0].target approvedSymbol MAML3

> [q457] data.variant.credibleSets.rows[22] studyLocusId 46fd207de84ba20ecd47f7693f32d90e studyId GCST007085 pValueMantissa 7 pValueExponent -10 beta null finemappingMethod PICS

> [q458] data.variant.credibleSets.rows[22].study traitFromSource Smoking status projectId GCST

> [q459] data.variant.credibleSets.rows[8] studyLocusId 17a8dee23ebd2b5743ffcc6aeb7303bf studyId FINNGEN_R12_F5_DEPRESSION_DYSTHYMIA pValueMantissa 9.326000213623047 pValueExponent -11 beta -0.00290903219040857 finemappingMethod SuSie

> [q460] data.variant.credibleSets.rows[8].study traitFromSource Depression or dysthymia projectId FINNGEN_R12

Open Targets Platform 26.09, row 29 (variant-4_140017956_T_A.json; credibleSets-longevity8-4_140017956_T_A.json).
rs36072649 is 4_140017956_T_A (q444), alternate A, and sits in 69 credible sets (q445; the first 25 rows returned):
type 2 diabetes (Vujkovic 2020, P 2e-12, q447, q448), COPD (P 3e-9, q451, q452), coronary atherosclerosis (P 4e-9,
q453, q454), smoking status (P 7e-10, q457, q458), FinnGen depression or dysthymia (P 9e-11, q459, q460), and lipid
fractions, visceral fat, lean mass, white cells, pain and intervertebral disc disorder among the rest. A set's beta is
its lead variant's, not necessarily this one's, so no direction is read from them. Locus-to-gene names MAML3 in every
one of the 25 returned, 0.67 to 0.85 (q449, q450 at 0.79; q455, q456 at 0.84), the next gene at 0.15 or less. None of
the eight lifespan, healthspan, longevity and current-age studies has a credible set holding the variant (q446), and
mvAge's 26 sets (q413) include none on 4q31 (study-sets-GCST90321079.json, leads listed by position).

## Reading 2026-11-11, record

> [q461] data.variant.credibleSets.rows[14] studyId GCST90691922 pValueMantissa 3.651437520980835 pValueExponent -9

> [q462] data.variant.credibleSets.rows[14].study traitFromSource Smoking status, ever vs never

> [q463] data.variant.credibleSets.rows[14].variant id 4_140017956_T_A

> [q464] data.variant.credibleSets.rows[29] studyId GCST90041844 pValueMantissa 4.730323314666748 pValueExponent -11

> [q465] data.variant.credibleSets.rows[29].study traitFromSource Maternal smoking around birth (UKB data field 1787)

> [q466] data.variant.credibleSets.rows[29].variant id 4_140017956_T_A

> [q467] data.variant.credibleSets.rows[56] studyId GCST011703 pValueMantissa 1 pValueExponent -9

> [q468] data.variant.credibleSets.rows[56].study traitFromSource Smoking initiation

> [q469] data.variant.credibleSets.rows[56].variant id 4_140017956_T_A

All 69 of rs36072649's credible sets (variant-sets-4_140017956_T_A.json: study, trait, lead variant, top
locus-to-gene), row 29. The variant leads three, all smoking: smoking status, ever against never (P 3.7e-9, q461-q463),
maternal smoking around birth (P 4.7e-11, q464-q466) and smoking initiation (GCST011703, P 1e-9, q467-q469; the GWAS
Catalog prints its A lowering it, db-gwascatalog-2026.10.29#q202, q203). The other 66 are led by nearby variants:
smoking (status, initiation, cessation, age at start, lifetime), type 2 diabetes and glucose (five studies),
COPD and airway obstruction, coronary atherosclerosis and ischaemic heart disease, depression, pain (back, neck,
chest, intensity), intervertebral disc disorder, visceral fat, lean mass, walking pace, CRP, white cells, monocytes,
platelet volume, potassium, cannabis use disorder, codeine use, reflux, and NMR lipid fractions (17 sets led by one
variant, 4_139953606_G_A). Locus-to-gene names MAML3 first in all 69 (0.66 to 0.87). No direction is read from them
(a set's beta is its lead's).

## Reading 2026-11-11, record

> [q470] data variant null

rs649357 (5_29426329_A_C, and C_A): Open Targets 26.09 has no record of the variant under either order
(`variant-sets-5_29426329_A_C.json`, `variant-sets-5_29426329_C_A.json`), nor of its r² 1.0 proxies rs694966
(5_29427065, both orders) and rs631778 (5_29426240, both orders); the rsID search finds only unrelated variants on
chromosome 15 (`search-rs649357.json`). No credible set, no locus-to-gene score: C4, E4. For row 31.

## Reading 2026-11-11, record

> [q471] data.variant id 5_82723979_C_T referenceAllele C alternateAllele T

> [q472] data.variant.alleleFrequencies[4] populationName fin_adj alleleFrequency 0.02256351915054987

> [q473] data.variant.alleleFrequencies[5] populationName eas_adj alleleFrequency 0.022286821705426358

> [q474] data.variant.credibleSets.rows[0] studyLocusId fe4f273ec43162aadef2040274173b4c studyId GCST90132317 pValueMantissa 5 pValueExponent -9 beta 1.15 finemappingMethod PICS

> [q475] data.variant.credibleSets.rows[0].locus.rows[0] posteriorProbability 1

> [q476] data.variant.credibleSets.rows[0].l2GPredictions.rows[0] score 0.8485983610153198

> [q477] data.variant.credibleSets.rows[0].l2GPredictions.rows[0].target approvedSymbol XRCC4

> [q478] data.variant.credibleSets.rows[0].l2GPredictions.rows[1] score 0.4570446312427521

> [q479] data.variant.credibleSets.rows[0].l2GPredictions.rows[1].target approvedSymbol TMEM167A

> [q480] data.credibleSet studyLocusId fe4f273ec43162aadef2040274173b4c

> [q481] data.credibleSet.colocalisation count 0

rs138499810 (`variant-sets-5_82723979_C_T.json`; C reference, T alternate, q471): T 0.023 in gnomAD Finns (q472)
and 0.022 in East Asians (q473). One credible set, Chang 2022's healthy ageing (GCST90132317, the set q155-q157 found
for row 16), PICS from the reported top hit (q474), the lead alone at PIP 1 (q475): a one-variant set, PIP 1 by
construction, the lead having no East Asian proxy above r² 0.13 (db-ensembl-116#q213). Causal C1 on §4.2's letter,
said as meaningless, as at row 19. Locus-to-gene: XRCC4 0.85 (q476, q477), TMEM167A 0.46 (q478, q479), ATG10 0.23,
RPS23 0.19. The set (`coloc-fe4f273ec43162aadef2040274173b4c.json`, q480) has no colocalisation of any kind (q481),
so no rival meets an E1/E2 criterion (D24): effector E2, XRCC4, the model's call on a one-variant set (its features
not read). For row 32.

## Reading 2026-11-11, record

> [q482] data.variant id 5_158393594_C_T referenceAllele C alternateAllele T

> [q483] data.variant.credibleSets count 115

> [q484] data.variant.credibleSets.rows[0] studyLocusId 05ca6e630be02b1364089c7e74c5a572 studyId GCST90624049 pValueMantissa 2.9830000400543213 pValueExponent -21 beta -0.0165470532670251 finemappingMethod PICS

> [q485] data.variant.credibleSets.rows[0].study traitFromSource Frailty (Factor 3 - Multimorbidity) projectId GCST

> [q486] data.variant.credibleSets.rows[0].locus.rows[15] posteriorProbability 0.025860334056678598

> [q487] data.variant.credibleSets.rows[2] studyLocusId 0fb0f8ae928509457ea183ae7f2de7f2 studyId GCST90473522 pValueMantissa 4.302999973297119 pValueExponent -34 beta -0.0577575 finemappingMethod PICS

> [q488] data.variant.credibleSets.rows[2].study traitFromSource ICD10 I10: Essential (primary) hypertension projectId GCST

> [q489] data.variant.credibleSets.rows[2].locus.rows[15] posteriorProbability 0.02101027189424359

> [q490] data.variant.credibleSets.rows[0].l2GPredictions.rows[0].target approvedSymbol EBF1

> [q491] data.variant.credibleSets.rows[55].l2GPredictions.rows[0].target approvedSymbol CLINT1

rs2149954 (`variant-sets-5_158393594_C_T.json` and its second page `variant-sets-p1-...`; C reference, T alternate,
q482): 115 credible sets (q483). I read every set's trait: blood pressure, hypertension, antihypertensive and
other blood-pressure medication, pulse and mean arterial pressure, heart rate, cardiovascular disease, coronary
artery disease (MTAG), atrial fibrillation, hair pattern, birth weight, platelet count, haemoglobin, prolonged
pregnancy, prostate hyperplasia, one T-cell expression QTL, and one frailty factor; none is lifespan, longevity or
survival. The frailty set is Foote 2025's multimorbidity factor (q484, q485), healthspan-class (D23), the lead's PIP 0.026
(q486). Essential hypertension (q487, q488), PIP 0.021 (q489). The beta and P on a set's line are its own lead
variant's, not rs2149954's (q492-q495), so they give no direction for T. The lead's PIP, where it shows among the 25
members the query returns (the member lists stop at 25, a page cap), is 0.007 to 0.098; in about a quarter of the
sets it lies past them. Locus-to-gene names EBF1 at about 0.4 to 0.6 in most sets (q490) and CLINT1 in some pulse-pressure sets
(0.93, q491). No lifespan-class set, so causal C4 and effector E4. For row 33.

## Reading 2026-11-11, record

> [q492] data.credibleSet.variant id 5_158397473_A_G

> [q493] data.credibleSet.study traitFromSource Frailty (Factor 3 - Multimorbidity) publicationFirstAuthor Foote IF publicationDate 2025-08-04 pubmedId 40759756

> [q494] data.credibleSet.locus.rows[0] posteriorProbability 0.025860334056678598 beta null standardError 0.11642424669468565 pValueMantissa null pValueExponent null r2Overall 0.943438451706887

> [q495] data.credibleSet.variant id 5_158397175_T_C

The lead's own entries in two of its sets (`member-<studyLocusId>-5_158393594_C_T.json`). Foote 2025's frailty
multimorbidity set (q493) is led by 5_158397473_A_G (q492); rs2149954 is a member at PIP 0.026, r² 0.94 to the lead,
with no beta or P of its own (q494). The essential hypertension set is led by 5_158397175_T_C (q495), the same shape.
So the betas on the variant's set list (q484, q487) are the set leads', and T's direction in these sets is not given
here. For row 33.

## Reading 2026-11-11, record

> [q496] data.variant.credibleSets count 381

> [q497] data.variant.credibleSets.rows[6] studyLocusId 3ebe7ef9958b5c249ce68244b0d819a2 studyId GCST007406 pValueMantissa 1.0615816116333008 pValueExponent -26 beta 0.01967712413041147 finemappingMethod SuSiE-inf

> [q498] data.variant.credibleSets.rows[6].study traitFromSource Healthspan projectId GCST

> [q499] data.variant.credibleSets.rows[6].locus.rows[0] posteriorProbability 0.9999999048994158

> [q500] data.variant.credibleSets.rows[6].locus.rows[0].variant id 6_396321_C_T

> [q501] data.variant.credibleSets.rows[6].l2GPredictions.rows[0] score 0.7911879420280457

> [q502] data.variant.credibleSets.rows[6].l2GPredictions.rows[0].target approvedSymbol IRF4

> [q503] data.variant.credibleSets.rows[6].l2GPredictions.rows[1] score 0.08313760906457901

> [q504] data.variant.credibleSets.rows[47] studyLocusId 5dbb0989eb97176d6a089f577c677b49 studyId GCST011100 pValueMantissa 8 pValueExponent -26 beta null finemappingMethod PICS

> [q505] data.variant.credibleSets.rows[47].locus.rows[0] posteriorProbability 0.9998945966579305

> [q506] data.variant.credibleSets.rows[79] studyLocusId b3e76002e23675c703039d2cbfa74279 studyId GCST90321079 pValueMantissa 7 pValueExponent -12 beta -0.010844371 finemappingMethod PICS

> [q507] data.variant.credibleSets.rows[79].locus.rows[0] posteriorProbability 0.9865442874839144

> [q508] data.credibleSet.colocalisation count 114

> [q509] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study id gtex-v10_txrev_blood_ensg00000137265_grp_2_contained_enst00000468485 traitFromSource ENSG00000137265.grp_2.contained.ENST00000468485 studyType tuqtl

> [q510] data.credibleSet.colocalisation.rows[17].otherStudyLocus.study id UKB_PPP_EUR_KIT_P10721_OID20370_v1 traitFromSource KIT:P10721:OID20370:v1 studyType pqtl

> [q511] data.variant.credibleSets.rows[18] studyLocusId 0c291e9253c39a7a0aeda93784455da2 studyId GCST005897 pValueMantissa 1 pValueExponent -581 beta 0.545 finemappingMethod PICS

> [q512] data.variant.credibleSets.rows[18].study traitFromSource Low tan response projectId GCST

> [q513] data.variant.credibleSets.rows[87].study traitFromSource Non-melanoma skin cancer projectId GCST

> [q514] data.variant.credibleSets.rows[87].locus.rows[0] posteriorProbability 0.9934044343969347

> [q515] data.variant.credibleSets.rows[20].study traitFromSource Skin cancer projectId GCST

rs12203592 (6_396321_C_T) is in 381 credible sets (q496; four pages, `variant-sets-6_396321_C_T.json` and `-p1` to
`-p3`). Three are the row's own claim's (D17.2): in the first file, Zenin's healthspan (GCST007406), SuSiE-inf, the variant alone at PIP
1.00 and itself the set's lead (q497 to q500), so the set's beta 0.0197 per T is the variant's own, on Open Targets'
scale; in the first file too, Timmers 2020's multivariate ageing set (GCST011100), PICS, PIP 1.00, no beta (q504, q505); in `-p2`, Rosoff 2023's
mvAge set (GCST90321079), PICS, PIP 0.99, T −0.0108 (q506, q507). Locus-to-gene: IRF4 0.79 on the healthspan set,
DUSP22 next at 0.08 (q501 to q503); 0.80 and 0.85 on the other two (the files). The rest are pigmentation, tanning
(Low tan response, PIP 1.00, T beta 0.545 as the set's lead, q511, q512; first file), skin cancers (non-melanoma skin cancer PIP 0.99, q513, q514; skin cancer,
q515; squamous cell, keratinocyte, melanoma), blood cell counts, retinal-image embeddings, facial ageing, puberty
timing and IRF4's own QTLs.

QTL colocalisation of the healthspan set (`coloc-qtl-3ebe7ef9958b5c249ce68244b0d819a2.json`; the two multivariate
sets give the same list): 114, all at H4 ≥ 0.8 (q508). 109 are IRF4 (60 eQTL, 18 sQTL, 31 transcript-usage QTL, e.g.
q509); one each are UK Biobank pQTLs of KIT (q510), GPNMB, JCHAIN, CD5L and DSG4, each 1 of 114, under
D24's tenth. IRF4: L2G ≥ 0.5 plus cis-QTL colocalisation, E1. For row 35.

## Reading 2026-11-11, record

> [q516] data variant null

Open Targets 26.09 has no record of row 36's lead: `variant(variantId:...)` answers null for 6_28445714_C_T and
6_28445714_T_C (`variant-6_28445714_C_T.json`, `variant-6_28445714_T_C.json`, q516), and the platform's search
finds none of rs6902687, rs13190937, rs13215804 or rs111859903 (Park 2025's R² > 0.99 set, pmid-40021682#q21;
the four queries cached no text), where the same search finds rs12203592 (`search-rs12203592.json`). So no credible
set holds the lead or its tags, Park 2025's whole-cohort study among them: no fine-mapping and no locus-to-gene
score. For row 36.

## Reading 2026-11-11, record

> [q517] data.variant id 6_34624313_A_G referenceAllele A alternateAllele G

> [q518] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.12261263647332332

> [q519] data.credibleSet studyLocusId 7e1f477e0f108539522b218bd7b3c80a finemappingMethod PICS confidence PICS fine-mapped credible set based on reported top hit pValueMantissa 2 pValueExponent -9 beta -0.010191999

> [q520] data.credibleSet.study id GCST90321079 traitFromSource Aging pubmedId 37550455 publicationFirstAuthor Rosoff DB nSamples 1559001

> [q521] data.credibleSet.locus count 96 data.credibleSet.locus.rows[0] posteriorProbability 0.08530487814389447 data.credibleSet.locus.rows[0].variant id 6_34624313_A_G data.credibleSet.locus.rows[0].variant.rsIds[0] rs6907508

> [q522] data.credibleSet.locus.rows[1] posteriorProbability 0.05538970539646245 data.credibleSet.locus.rows[1].variant id 6_34635914_G_A data.credibleSet.locus.rows[1].variant.rsIds[0] rs76967117

> [q523] data.credibleSet.l2GPredictions.rows[0] score 0.20016878843307495 data.credibleSet.l2GPredictions.rows[0].target approvedSymbol SNRPC data.credibleSet.l2GPredictions.rows[1] score 0.18480822443962097 data.credibleSet.l2GPredictions.rows[1].target approvedSymbol BLTP3A data.credibleSet.l2GPredictions.rows[2] score 0.11522052437067032 data.credibleSet.l2GPredictions.rows[2].target approvedSymbol SPDEF data.credibleSet.l2GPredictions.rows[3] score 0.09999772161245346 data.credibleSet.l2GPredictions.rows[3].target approvedSymbol ILRUN

> [q524] data.credibleSet.colocalisation count 107

> [q525] data.variant.credibleSets.rows[29] studyLocusId 4f6d0526ec59e6eee569c8d0d4b0ea05 studyId GCST010243 pValueMantissa 2 pValueExponent -17 beta -0.0276231 finemappingMethod PICS data.variant.credibleSets.rows[29].study traitFromSource Apolipoprotein B levels projectId GCST

> [q526] data.variant.credibleSets.rows[29].locus.rows[0] posteriorProbability 0.21578285989184492 data.variant.credibleSets.rows[29].locus.rows[0].variant id 6_34624313_A_G

> [q527] data.variant.credibleSets.rows[63] studyLocusId 5a60bc0384a9565c242b28f136007589 studyId GCST90498358 pValueMantissa 9.8149995803833 pValueExponent -21 beta -0.0302829 finemappingMethod PICS data.variant.credibleSets.rows[63].study traitFromSource LDL cholesterol levels projectId GCST

> [q528] data.variant.credibleSets.rows[63].locus.rows[0] posteriorProbability 0.2707859811441589 data.variant.credibleSets.rows[63].locus.rows[0].variant id 6_34624313_A_G

> [q529] data.variant.credibleSets.rows[86] studyLocusId f96477a844160cfc6683a4f2317db57a studyId GCST90500025 pValueMantissa 1.2710000276565552 pValueExponent -28 beta -0.035135 finemappingMethod PICS data.variant.credibleSets.rows[86].study traitFromSource Total cholesterol levels projectId GCST

> [q530] data.variant.credibleSets.rows[86].locus.rows[0] posteriorProbability 0.3758171221540299 data.variant.credibleSets.rows[86].locus.rows[0].variant id 6_34624313_A_G

> [q531] data.variant.credibleSets.rows[77] studyLocusId 5d5251807c839b6d8f87b9e36dd31a2d studyId GCST90301945 pValueMantissa 2.058000087738037 pValueExponent -22 beta -0.058150767 finemappingMethod PICS data.variant.credibleSets.rows[77].study traitFromSource Apolipoprotein A-I levels projectId GCST

> [q532] data.variant.credibleSets.rows[77].locus.rows[0] posteriorProbability 0.2965065448067371 data.variant.credibleSets.rows[77].locus.rows[0].variant id 6_34624313_A_G

> [q533] data.variant.credibleSets.rows[84] studyLocusId 42c9de93ca15dc9238a55ba7934c0dcc studyId GCST90501116 pValueMantissa 1.5850000381469727 pValueExponent -37 beta -0.0374 finemappingMethod PICS data.variant.credibleSets.rows[84].study traitFromSource Concentration of HDL particles projectId GCST

> [q534] data.variant.credibleSets.rows[84].locus.rows[0] posteriorProbability 0.45486306683152267 data.variant.credibleSets.rows[84].locus.rows[0].variant id 6_34624313_A_G

> [q535] data.variant.credibleSets.rows[90] studyLocusId 60709e73a030f085e7efae036434bf57 studyId GCST90691864 pValueMantissa 1.4616353511810303 pValueExponent -109 beta 0.03521005576394587 finemappingMethod SuSiE-inf data.variant.credibleSets.rows[90].study traitFromSource Standing height (UKB data field 50) projectId GCST

> [q536] data.variant.credibleSets.rows[90].locus.rows[0] posteriorProbability 0.44480924319016263 data.variant.credibleSets.rows[90].locus.rows[0].variant id 6_34624313_A_G

> [q537] data.variant.credibleSets.rows[54] studyLocusId a0d49183f92838c43af7d0c4e91c1ae8 studyId GCST90000025 pValueMantissa 1.8804374933242798 pValueExponent -42 beta 0.022691746978692525 finemappingMethod SuSiE-inf data.variant.credibleSets.rows[54].study traitFromSource Appendicular lean mass projectId GCST

> [q538] data.variant.credibleSets.rows[54].locus.rows[0] posteriorProbability 0.9972565652601071 data.variant.credibleSets.rows[54].locus.rows[0].variant id 6_34624313_A_G

> [q539] data.variant.credibleSets.rows[51] studyLocusId 57ceea19344795acec8306bacc5513d0 studyId GCST90428730 pValueMantissa 1 pValueExponent -26 beta -0.0085 finemappingMethod PICS data.variant.credibleSets.rows[51].study traitFromSource Gamma glutamyl transferase levels projectId GCST

> [q540] data.variant.credibleSets.rows[51].locus.rows[0] posteriorProbability 0.3541955400079486 data.variant.credibleSets.rows[51].locus.rows[0].variant id 6_34624313_A_G

> [q541] data.variant.credibleSets.rows[37] studyLocusId 5316b3cb0d9d4bcd0456fde470a9b880 studyId GCST008512 pValueMantissa 1 pValueExponent -8 beta 0.0217 finemappingMethod PICS data.variant.credibleSets.rows[37].study traitFromSource Multisite chronic pain projectId GCST

> [q542] data.variant.credibleSets.rows[37].locus.rows[0] posteriorProbability 0.07603128970978829 data.variant.credibleSets.rows[37].locus.rows[0].variant id 6_34624313_A_G

> [q543] data.variant.credibleSets.rows[90] studyLocusId fac4b284d88f543d03517ad32e17674c studyId GCST90501278 pValueMantissa 1.9950000047683716 pValueExponent -24 beta -0.0324 finemappingMethod PICS data.variant.credibleSets.rows[90].study traitFromSource Total free cholesterol levels projectId GCST

> [q544] data.variant.credibleSets.rows[90].locus.rows[0] posteriorProbability 0.32496341370742454 data.variant.credibleSets.rows[90].locus.rows[0].variant id 6_34624313_A_G

> [q545] data.credibleSet studyLocusId 34172f28b706dad5317e6211470cb256 finemappingMethod SuSiE-inf confidence SuSiE fine-mapped credible set with out-of-sample LD pValueMantissa 6.7989277839660645 pValueExponent -9 beta 0.006886937131206627

> [q546] data.credibleSet.study id GCST90707291 traitFromSource Hospital frailty risk score pubmedId 40764432 publicationFirstAuthor Mak JKL nSamples 500737

> [q547] data.credibleSet.locus.rows[41] posteriorProbability 0.011161286304012271 data.credibleSet.locus.rows[41].variant id 6_34624313_A_G data.credibleSet.locus.rows[41].variant.rsIds[0] rs6907508

> [q548] data.credibleSet.colocalisation.rows[0] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9841501405697227 clpp 0.05292548051109325 rightStudyType eqtl data.credibleSet.colocalisation.rows[0].otherStudyLocus studyLocusId af0e8fa885784ef279f6769e77c4f1eb data.credibleSet.colocalisation.rows[0].otherStudyLocus.study id gtex-v10_exon_adipose_visceral_ensg00000196821_10_6_34587288_34590508 traitFromSource ENSG00000196821.10_6_34587288_34590508 studyType eqtl data.credibleSet.colocalisation.rows[0].otherStudyLocus.study.target approvedSymbol ILRUN

> [q549] data.credibleSet.colocalisation.rows[15] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9894577773097832 clpp 0.0797855124721133 rightStudyType eqtl data.credibleSet.colocalisation.rows[15].otherStudyLocus studyLocusId d29e0b9bc38d196080a5acb2a76573fe data.credibleSet.colocalisation.rows[15].otherStudyLocus.study id gtex-v10_exon_brain_anterior_cingulate_cortex_ensg00000272288_7_6_34696317_34696722 traitFromSource ENSG00000272288.7_6_34696317_34696722 studyType eqtl data.credibleSet.colocalisation.rows[15].otherStudyLocus.study.target approvedSymbol ILRUN-AS1

Open Targets 26.09 resolves rs6907508 to 6_34624313_A_G, alternate allele G (q517), G 0.12 in gnomAD's non-Finnish
Europeans (q518), and places it in 705 credible sets (`variant-sets-p0` to `p7`). A set's β is per its own lead's
alternate allele; read here only for sets rs6907508 leads, where it is per G.

mvAge's set (GCST90321079, Rosoff 2023, PICS on the reported top hit; `credibleSet-7e1f477e…`): P 2e-9, β −0.0102 per
G (q519, q520); 96 members, rs6907508 first at PIP 0.085 (q521), the next at 0.055 (q522): in the set, PIP under 0.1,
causal C3. Locus-to-gene (q523): SNRPC 0.20, BLTP3A 0.18, SPDEF 0.12, ILRUN 0.10; none passes 0.5. Its QTL
colocalisations (`coloc-qtl-7e1f477e…`, eQTL, sQTL, tuQTL and pQTL types): 107 (q524), 102 of them at H4 ≥ 0.8, counted
from the cached rows (derived): ILRUN 86 (GTEx and others, expression and exon-level, q548), ILRUN-AS1 8 (q549),
BLTP3A 4, and one each for SPDEF and three UKB-PPP plasma proteins (MEGF10, APOF, CA14). Whether those three are cis
or trans, ILRUN-AS1's 8 of 102 is under D24's tenth and no rival passes L2G, so the call is ILRUN by colocalisation
alone: E2. Its 1,095 GWAS colocalisations (`coloc-…`, six pages) are led by GGT, height, lipids and apolipoproteins
(H4 0.97 to 0.99).

Sets rs6907508 leads, β per G (it tops each): apolipoprotein B (GCST010243) −0.0276, P 2e-17, PIP 0.22 (q525, q526);
LDL cholesterol (GCST90498358) −0.0303, P 1e-20, PIP 0.27 (q527, q528); total cholesterol (GCST90500025)
−0.0351, P 1e-28, PIP 0.38 (q529, q530); total free cholesterol (GCST90501278) −0.0324, P 2e-24, PIP 0.33
(q543, q544); apolipoprotein A-I (GCST90301945) −0.058, P 2e-22, PIP 0.30 (q531, q532); HDL particle
concentration (GCST90501116) −0.0374, P 2e-37, PIP 0.45 (q533, q534); standing height (GCST90691864, SuSiE-inf)
+0.0352, P 1.5e-109, PIP 0.44 (q535, q536); appendicular lean mass (GCST90000025, SuSiE-inf) +0.0227, P 2e-42,
PIP 0.997 (q537, q538); GGT (GCST90428730) −0.0085, P 1e-26, PIP 0.35 (q539, q540); multisite chronic pain
(GCST008512) +0.0217, P 1e-8, PIP 0.076 (q541, q542). So G, the shorter-lived allele, lowers both the atherogenic
(apolipoprotein B, LDL) and the HDL side, and goes with a taller, leaner-massed body; A raises LDL and apolipoprotein B.
The lean-mass PIP is for that trait, not for ageing. Hospital frailty (GCST90707291, Mak 2025, SuSiE-inf) has a set led
by rs56930444 (r² 0.83 to the lead, db-ensembl-116 window), P 7e-9, the lead in it at PIP 0.011 (q545 to q547):
a healthspan-class set the tier does not rest on (D25.5), named only. Coronary atherosclerosis, heart-failure and
hypertension sets hold the lead behind neighbours whose phase is not read; their β is not read for rs6907508.

## rs7742789 (ZNF318 / ABCC10), for row 40

> [q550] data.variant id 6_43378065_C_T referenceAllele C alternateAllele T

> [q551] data.variant.credibleSets count 172

> [q552] data.credibleSets count 0

> [q553] data.variant.credibleSets.rows[62] studyLocusId 6805e8f39784dc232c8891e7466c1620 studyId GCST90692779 pValueMantissa 6.255704879760742 pValueExponent -45 beta -0.022134224217095277 finemappingMethod SuSiE-inf data.variant.credibleSets.rows[62].study traitFromSource Cystatin C levels projectId GCST

> [q554] data.variant.credibleSets.rows[62].locus.rows[0] posteriorProbability 0.9980822499497782 data.variant.credibleSets.rows[62].locus.rows[0].variant id 6_43378065_C_T

> [q555] data.variant.credibleSets.rows[24] studyLocusId b7251b695a2943b12a30605624eec88b studyId GCST90428446 pValueMantissa 1.081796646118164 pValueExponent -51 beta 0.02238207120711087 finemappingMethod SuSiE-inf data.variant.credibleSets.rows[24].study traitFromSource Estimated glomerular filtration rate (creatinine, cystatin c) projectId GCST

> [q556] data.variant.credibleSets.rows[42] studyLocusId d7fa97ad2d7d44d5d9397c002066b4ce studyId GCST90319636 pValueMantissa 1.577418565750122 pValueExponent -11 beta -0.013927392846856389 finemappingMethod SuSiE-inf data.variant.credibleSets.rows[42].study traitFromSource Serum creatinine levels projectId GCST

> [q557] data.variant.credibleSets.rows[58] studyLocusId ee4e91f695a70b54d3d627fcc8a58d20 studyId GCST90476119 pValueMantissa 1.5499999523162842 pValueExponent -13 beta 0.011116510880298955 finemappingMethod SuSiE-inf data.variant.credibleSets.rows[58].study traitFromSource Acute renal failure (PheCode 585.1) projectId GCST

> [q558] data.variant.credibleSets.rows[82] studyLocusId 84c29e8e3611bb831174ffdc9c510815 studyId GCST90472780 pValueMantissa 8.958096504211426 pValueExponent -14 beta 0.012872463718314851 finemappingMethod SuSiE-inf data.variant.credibleSets.rows[82].study traitFromSource Systolic blood pressure projectId GCST

> [q559] data.variant.credibleSets.rows[39] studyLocusId cd98a61308a0950ee0b3436d887b10e9 studyId GCST90310296 pValueMantissa 9.40381908416748 pValueExponent -26 beta 0.009938326766106162 finemappingMethod SuSiE-inf data.variant.credibleSets.rows[39].study traitFromSource Pulse pressure projectId GCST

> [q560] data.variant.credibleSets.rows[23] studyLocusId b4f175edf3feb2c69a5bcf9ce0cfe8df studyId GCST90455657 pValueMantissa 8.036999702453613 pValueExponent -16 beta 0.0307 finemappingMethod PICS data.variant.credibleSets.rows[23].study traitFromSource Heart failure projectId GCST

> [q561] data.variant.credibleSets.rows[17] studyLocusId aeb466aeee96d10873e5ec2672765617 studyId GCST90475929 pValueMantissa 5.729000091552734 pValueExponent -9 beta 0.008332736185187383 finemappingMethod SuSiE-inf data.variant.credibleSets.rows[17].study traitFromSource Ischemic heart disease (PheCode 411) projectId GCST

> [q562] data.variant.credibleSets.rows[68] studyLocusId f9836bcc7e66f5b81206ca0541e02713 studyId GCST90624411 pValueMantissa 9.454999923706055 pValueExponent -12 beta 0.024 finemappingMethod PICS data.variant.credibleSets.rows[68].study traitFromSource Atrial fibrillation projectId GCST

> [q563] data.variant.credibleSets.rows[25] studyLocusId 312754c4cb5bb479dd80e2262f6c65fa studyId GCST90435354 pValueMantissa 2.0031023025512695 pValueExponent -9 beta 0.009172607488527402 finemappingMethod SuSiE-inf data.variant.credibleSets.rows[25].study traitFromSource Clonal hematopoiesis (DNMT3A mutation) projectId GCST

> [q564] data.variant.credibleSets.rows[16] studyLocusId 23ede60ead5c87b6bc315565b1f08f38 studyId GCST90475480 pValueMantissa 1.7639963626861572 pValueExponent -35 beta -0.03466723776087834 finemappingMethod SuSiE-inf data.variant.credibleSets.rows[16].study traitFromSource magnesium (Mg, mean, inv-norm transformed) projectId GCST

rs7742789 is 6_43378065_C_T, alt T (q550); `beta` is per T at the sets it leads (anchored on two SuSiE-inf sets
against the catalog, below, q557, q564). 172 credible sets hold it (q551;
`variant-sets-p0/p1-6_43378065_C_T.json`), 34 of them led by it; none is a lifespan, healthspan, longevity or
current-age study: the eight such studies hold no set with it (q552, `credibleSets-longevity8-6_43378065_C_T.json`),
and mvAge's 26 sets (q413, re-cached as `study-sets-GCST90321079.json`) include none on 6p21.1. So causal C4,
effector E4. Per T at the lead (each its set's lead): cystatin C −0.022, P 6 × 10⁻⁴⁵, a one-variant set, PIP 0.998
(q553, q554); eGFR from creatinine and cystatin C +0.022, P 1 × 10⁻⁵¹, PIP 0.994 (q555); creatinine −0.014 (q556);
so T goes with better filtration and C, the longer-life allele, with lower eGFR. Yet T raises acute renal failure
(+0.011, P 1.5 × 10⁻¹³, q557), systolic blood pressure (+0.013, P 9 × 10⁻¹⁴, q558), pulse pressure (+0.0099, P 9 ×
10⁻²⁶, q559), heart failure (+0.031, P 8 × 10⁻¹⁶, q560), ischaemic heart disease (+0.0083, P 6 × 10⁻⁹, q561), atrial
fibrillation (+0.024, P 9 × 10⁻¹², q562) and clonal haematopoiesis with a DNMT3A mutation (+0.0092, P 2 × 10⁻⁹,
q563), and lowers serum magnesium (−0.035, P 2 × 10⁻³⁵, PIP 0.74, q564). Other sets it leads: urea and blood urea
nitrogen (lower per T), heart rate, actinic keratosis and skin cancer (higher per T), alanine and HSPG2. Locus-to-gene
on these sets favours TJAP1 (about 0.8 on the kidney and blood-pressure SuSiE sets) or CRIP3 (about 0.47 on the PICS
sets), ZNF318 at most 0.42; named only, since no lifespan-class set exists to read an effector from. For row 40.

## Reading 2026-11-11, record

The chronic kidney disease sets that hold row 40's lead behind a neighbour, from the same `variant-sets` files, and
those neighbours' records (`variant-<id>.json`). Each set's `beta` is its own lead's, per that lead's alt allele.

> [q565] data.variant.credibleSets.rows[13] studyLocusId 1c2163e9fb3b99ae0f05ecfbd65eb985 studyId GCST90480387 pValueMantissa 1.1100000143051147 pValueExponent -10 beta 0.09288312748005599 finemappingMethod PICS data.variant.credibleSets.rows[13].study traitFromSource Disorders resulting from impaired renal function (PheCode 588) projectId GCST

> [q566] data.variant.credibleSets.rows[13].locus.rows[0] posteriorProbability 0.2040435838211657 data.variant.credibleSets.rows[13].locus.rows[0].variant id 6_43302413_C_T

> [q567] data.variant.credibleSets.rows[36] studyLocusId cb14224a27965bd86942fcda346296f2 studyId GCST90480386 pValueMantissa 1.7200000286102295 pValueExponent -10 beta 0.10436101532474278 finemappingMethod PICS data.variant.credibleSets.rows[36].study traitFromSource Secondary hyperparathyroidism (of renal origin) (PheCode 588.2) projectId GCST

> [q568] data.variant.credibleSets.rows[36].locus.rows[0] posteriorProbability 0.1790021723616663 data.variant.credibleSets.rows[36].locus.rows[0].variant id 6_43292922_T_C

> [q569] data.variant.credibleSets.rows[41] studyLocusId cf5743aade133351609ca61d6447d6e0 studyId GCST90479971 pValueMantissa 3.259999990463257 pValueExponent -9 beta 0.07785343920486418 finemappingMethod PICS data.variant.credibleSets.rows[41].study traitFromSource Anemia in chronic kidney disease (PheCode 285.21) projectId GCST

> [q570] data.variant.credibleSets.rows[41].locus.rows[0] posteriorProbability 0.1569898902837356 data.variant.credibleSets.rows[41].locus.rows[0].variant id 6_43382057_G_A

> [q571] data.variant id 6_43302413_C_T referenceAllele C alternateAllele T data.variant.rsIds[0] rs2270860

> [q572] data.variant id 6_43292922_T_C referenceAllele T alternateAllele C data.variant.rsIds[0] rs6901866

> [q573] data.variant id 6_43382057_G_A referenceAllele G alternateAllele A data.variant.rsIds[0] rs7764523

Three MVP PheCode sets of chronic kidney disease hold rs7742789 at PIP about 0.04 (locus rows 10, 10 and 6): disorders
from impaired renal function, β +0.093 per T of its lead rs2270860, P 1.1 × 10⁻¹⁰ (q565, q566, q571); renal
secondary hyperparathyroidism, +0.104 per C of rs6901866, P 1.7 × 10⁻¹⁰ (q567, q568, q572); anaemia in chronic
kidney disease, +0.078 per A of rs7764523, P 3.3 × 10⁻⁹ (q569, q570, q573). Each lead's alt is the minor allele in
non-Finnish Europeans (0.30, 0.31, 0.33, as rs7742789's T is 0.31) and is in strong LD with the lead (r² 0.76 to
0.85, D′ 0.92 to 1.00, db-ensembl-116#q268 to q270), so each counted allele travels with T (derived, not phased; the
studies are multi-ancestry, Europeans the largest arm, db-gwascatalog-2026.10.29#q287 to q289). So the T haplotype
carries more chronic kidney disease as well as more acute renal failure (q557), though T itself goes with lower
cystatin C and creatinine and higher eGFR (q553 to q556): the biomarkers and the disease endpoints run opposite ways.
The sign of `beta` at the lead is anchored on two SuSiE-inf sets against the catalog's lines for the same
accessions: acute renal failure T +0.0111 (q557) against rs7742789-C "decrease" (db-gwascatalog-2026.10.29#q283,
q284), and magnesium T −0.0347 (q564) against C "increase" (q285, q286). For row 40.

## Reading 2026-11-11, record

> [q574] data.study.credibleSets count 5

Open Targets 26.09 holds no variant record for rs114658003 (variant `6_99603424_G_A`) or for the deletion beside it
(`6_99603422_GC_G`, FinnGen's form): both queries return "data variant null" (the same text as q411; cached as
`variant-rs114658003.json` and `variant-rs66927770.json`). Gurinovich's study GCST012419 has five PICS sets (q574),
led by rs78043944, rs77184423, rs429358, rs77546126 and rs10973748; none at 6q16. So no set holds the lead, and its
causal and effector confidence could not be assessed. For row 41.

## Reading 2026-11-11, record

> [q575] data.search total 0

> [q576] data.credibleSets count 0

> [q577] data.study.credibleSets count 6

> [q578] data.study.credibleSets count 2

Open Targets 26.09 holds no variant record for rs1627804 (`6_107079224_C_A`, "data variant null", the text of q411;
`variant-rs1627804.json`); a search for the rsID returns nothing (q575), as do searches for its proxies rs1630395,
rs1618476 and rs36101665. The eight lifespan-class studies' credible sets hold none at the lead
(`credibleSets-longevity8-6_107079224_C_A`, q576). Retried by Pilling's own studies: GCST006702 (age at death)
has six sets (q577), led at 12_111621753, 15_78557437, 19_44908684, 6_160576086, 6_160591981 and 9_22103342;
GCST006698 (top 10 %) two (q578), at 15_78557437 and 19_44908684; none at 6q21. So causal and effector confidence could not be assessed. For row 42.

## Reading 2026-11-11, record

> [q579] data.search.hits[0] id 6_108587315_G_T

> [q580] data.variant.credibleSets count 214

> [q581] data.variant.credibleSets.rows[210].study traitFromSource Frailty (Factor 5 - Poorer Cognition) projectId GCST

> [q582] data.variant.credibleSets.rows[210].locus.rows[8] posteriorProbability 0.0654067970326906

> [q583] data.variant.credibleSets.rows[105] studyLocusId f317a9a62ba89aeeb528d653e7e35b46 studyId GCST011100 pValueMantissa 1 pValueExponent -8 beta null finemappingMethod PICS

> [q584] data.variant.credibleSets.rows[105].locus.rows[0] posteriorProbability 0.061890431235060155

> [q585] data.variant.credibleSets.rows[105].l2GPredictions.rows[0] score 0.41644757986068726

rs2802292 is `6_108587315_G_T` (q579). It sits in 214 credible sets (q580; all read, `variant-6_108587315_G_T-all.json`),
none of a lifespan-class study: they are adiposity (body mass index, weight, fat mass), cognition and education,
kidney function (eGFR, cystatin C), menarche and blood cells, its PIP about 0.06 to 0.11 in each, the sets' leads
other variants and locus-to-gene mostly FOXO3 (0.5 to 0.9). The one ageing-related set is Foote 2025's frailty
factor 5, "Poorer Cognition" (q581; GCST90624051, PICS, P 4.3 × 10⁻¹⁰, FOXO3 L2G 0.80), with the lead at PIP 0.065
(q582): healthspan-class (D23), and the cognition signal again. Timmers 2020's multivariate study GCST011100 has a
set at FOXO3 (q583; P 1e-8, PICS, 50 members) led by rs1159806 (`6_108685635_A_T`, PIP 0.062, q584), FOXO3 L2G 0.42
(q585), ARMC2 0.15; rs2802292 is not among its 50 members (`variant-6_108685635_A_T.json`). So the row's SNP is a tag
outside the locus's lifespan-class set: causal confidence C4. For row 43.

> [q586] data.variant.credibleSets.rows[210] studyLocusId fad2c221ec2a6886b210b7705006055c studyId GCST90624051 pValueMantissa 4.2820000648498535 pValueExponent -10 beta 0.015906992148477 finemappingMethod PICS

> [q587] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.3840483757062147

> [q588] data.variant.rsIds[0] rs6911407

Foote 2025's frailty factor 5 set (q586) is led by `6_108545828_C_A`, rs6911407 (q588), alt A at 0.384 in non-Finnish
Europeans (q587; `variant-6_108545828_C_A.json`), r² 0.98 with row 43's lead, A with G. Its beta, +0.0159, is read
as per alt allele A (the catalog prints no allele for it, db-gwascatalog-2026.10.29#q301, so the sign is Open Targets'
harmonisation, not the paper's), and Foote formats every input so that positive is the frailty-raising side
(pmid-40759756#q2): G's side scores higher on the poorer-cognition factor, as rs6911407-A's lower fluid intelligence
(db-gwascatalog-2026.10.29#q299) and Timmers 2020's "reduction in cognitive ability" (pmid-32678081#q23) also say.
For row 43.

## Reading 2026-11-11, record

> [q589] data.variant.credibleSets.rows[1] studyLocusId e2476c3f588e5c6ab56d35440181044a studyId GCST90551884 pValueMantissa 7.729002475738525 pValueExponent -9 beta -0.00879452480081629 finemappingMethod SuSiE-inf

> [q590] data.variant.credibleSets.rows[1].qualityControls[1] Study locus finemapped without in-sample LD reference

> [q591] data.variant.credibleSets.rows[1].locus.rows[0] posteriorProbability 0.11719316866899004

> [q592] data.variant.credibleSets.rows[1].l2GPredictions.rows[0].target approvedSymbol PLN

> [q593] data.variant.credibleSets.rows[1].l2GPredictions.rows[0] score 0.7674548029899597

> [q594] data.variant.credibleSets.rows[0] studyLocusId 217d1f0b0a39b481db78238a0fcb6cd0 studyId GCST90551886 pValueMantissa 3.3338894844055176 pValueExponent -9 beta -0.012437595155242075 finemappingMethod SuSiE-inf

> [q595] data.variant.credibleSets count 2

> [q596] data.variant.credibleSets.rows[0].locus.rows[24].variant id 6_118304954_C_A

> [q597] data.variant.credibleSets.rows[0].l2GPredictions.rows[0].target approvedSymbol CEP85L

Row 44's lead 6_118368937_C_T (`variant-6_118368937_C_T-all.json`, all sets read: two, q595). Park 2025's
whole-cohort deposit (GCST90551884, "Lifespan", n 393,833): a SuSiE-inf set of 21 variants led by rs76888380, P
7.7e-9, β −0.0088 (q589), its own PIP 0.117 (q591), next rs78528818 at 0.109; flagged for quality, fine-mapped
without an in-sample LD reference (q590); L2G PLN 0.77 (q592, q593), SLC35F1 0.20. The set's β is about 40 times
smaller than the deposit's |0.333| at the same variant (pmid-40021682#q43) and its allele is not stated: unreconciled,
read for nothing. Park's second deposit, GCST90551886 (n 212,863, the women by subtraction from the whole cohort and the men's q112): a 25-variant set led
by an insertion at 6:118,636,487, P 3.3e-9 (q594), which holds rs73768634 (q596), one of the rare haplotype's
variants; L2G CEP85L 0.27 (q597). No colocalisation is fetched for either; no other study, disease or QTL, holds
the lead.

> [q598] data.credibleSet.colocalisation count 0

Both sets' QTL colocalisations (`coloc-e2476c3f588e5c6ab56d35440181044a.json` for the whole cohort, q598;
`coloc-217d1f0b0a39b481db78238a0fcb6cd0.json` for the women, the same line): none, in any QTL type. PLN's 0.77 is
L2G alone; no rival gene passes L2G (SLC35F1 0.20) or colocalises (D24).

## Reading 2026-11-11, record

> [q599] data.variant id 6_126665850_A_G referenceAllele A alternateAllele G

> [q600] data.variant.credibleSets count 11

> [q601] data.variant.credibleSets.rows[2].study traitFromSource Attention deficit hyperactivity disorder or autism spectrum disorder or intelligence (pleiotropy) projectId GCST nSamples 371591 nCases 38564

> [q602] data.variant.credibleSets.rows[7].study traitFromSource Bone mineral density (paediatric, upper limb) projectId GCST nSamples 9416 nCases 0

> [q603] data.variant.credibleSets.rows[10].study traitFromSource Sitting height (UKB data field 20015) projectId GCST nSamples 419233 nCases 0

Row 45's lead rs1262476 (`variant-6_126665850_A_G-all.json`; under G>A Open Targets holds no record, as the reference
is A): eleven credible sets (q600), none of lifespan, longevity, healthspan or survival. It leads two PICS sets, Rao's
ADHD/autism/intelligence scan (PIP 0.24, q601) and Kemp's paediatric bone density (PIP 0.25, q602), and sits at PIP
0.03 to 0.15 in sets of leg and arm fat, BMI, femur-neck bone density, sitting height (q603), amlodipine
prescriptions and a HipSci exon QTL, most led by 6:126,727,085 and 6:126,727,464 (L2G CENPW 0.25 to 0.75, RSPO3
0.58 in the height set). With no lifespan-class set, causal and effector confidence are C4 and E4, and no gene is
named (D24). For row 45.

## Reading 2026-11-11, record

> [q604] data.variant id 7_4787883_T_TC referenceAllele T alternateAllele TC

> [q605] data.variant.credibleSets count 16

> [q606] rows[8] studyLocusId 8829a3930e365adaebaa57ef00943828 studyId lepik_2017_tx_blood_enst00000650310 pValueMantissa 2.4630000591278076 pValueExponent -10 beta -0.827584 finemappingMethod SuSie

Row 47's insertion (`variant-7_4787883_T_TC-all.json`; rs371933919): sixteen credible sets (q605), every one a
molecular QTL (ROSMAP, TwinsUK, GTEx v10, BLUEPRINT, Lepik 2017: transcript, exon and splice-junction usage of
ENSG00000242802, at nSamples 167 to 724). The insertion leads four of them, the largest a blood transcript QTL at
PIP 0.32 (q606). No GWAS set, so none of lifespan, longevity, healthspan or survival: causal and effector confidence
are C4 and E4, no gene named (D24). For row 47.

> [q607] data.variant id 7_4786560_G_A referenceAllele G alternateAllele A

> [q608] data.variant.credibleSets count 21

Pilling's proxy rs79109928 (`variant-7_4786560_G_A-all.json`): twenty-one credible sets (q608), again every one a
molecular QTL of ENSG00000242802's expression, transcripts and splicing (ROSMAP, GTEx v10, TwinsUK, BLUEPRINT,
OTAR3087_MAGE, Lepik 2017). No GWAS set holds the proxy either. For row 47.

## Reading 2026-11-11, record

> [q609] data.variant.credibleSets count 5

> [q610] data.variant.credibleSets.rows[3] studyLocusId a8e7e1b0de4e430e715dcc37275161e5 studyId GCST003425 pValueMantissa 2 pValueExponent -9 beta -0.49429628381477936 finemappingMethod PICS

> [q611] data.variant.credibleSets.rows[2] studyLocusId a3d504d458ec5b70dfbeba312867f5da studyId GCST008601 pValueMantissa 1 pValueExponent -8 beta -0.10536059565782314 finemappingMethod PICS

> [q612] data.variant.credibleSets.rows[3].locus.rows[0] posteriorProbability 0.5460920666096795

> [q613] data.variant.credibleSets.rows[2].locus.rows[0] posteriorProbability 0.9892568510538676

> [q614] data.variant.credibleSets.rows[3].l2GPredictions.rows[0] score 0.9051581025123596

> [q615] data.variant.credibleSets.rows[2].l2GPredictions.rows[0] score 0.8766800761222839

Row 48's IL6 lead (`variant-7_22728408_A_G-all.json`): five PICS credible sets (q609): critical COVID-19 (Gong,
GCST90105053, PIP 0.88), Takayasu arteritis (GCST006575, PIP 0.99), platelet count (the lead not its top member),
and two lifespan-class sets, Zeng's (q610; the lead's PIP 0.55, q612) and Deelen's trans-ethnic 99th percentile
(q611, which carries CLHLS, pmid-31413261#q127; PIP 0.99, q613). L2G names IL6 in both, 0.91 and 0.88 (q614, q615).
Both lifespan-class sets rest on CLHLS's genotypes, which D26.14 reads as an overfit source; the C1 they give is the
fine-mapping of that call.

> [q616] data.credibleSet.colocalisation count 3

> [q617] data.credibleSet.colocalisation.rows[0] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.8457248558956594 clpp 0.004981518632235571 betaRatioSignAverage 0

> [q618] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study id gtex-v10_ge_adipose_visceral_ensg00000179428 traitFromSource ENSG00000179428 studyType eqtl

> [q619] data.credibleSet.colocalisation.rows[2] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.7354906223769607 clpp 0.002531032214402276 betaRatioSignAverage 0

> [q620] data.credibleSet.colocalisation.rows[2].otherStudyLocus.study id gtex-v10_txrev_adipose_visceral_ensg00000136244_grp_1_upstream_enst00000404625 traitFromSource ENSG00000136244.grp_1.upstream.ENST00000404625 studyType tuqtl

> [q621] data.credibleSet.colocalisation count 0

The QTL colocalisations: Zeng's set (`coloc-a8e7e1b0de4e430e715dcc37275161e5.json`) has three (q616): IL6-AS1
(ENSG00000179428) expression in visceral adipose at H4 0.85 (q617, q618), the only one at 0.8 or more; the same gene in
subcutaneous adipose at 0.61; and an IL6 (ENSG00000136244) transcript-usage QTL in visceral adipose at 0.74 (q619,
q620), below 0.8. Deelen's trans-ethnic set has none (q621, `coloc-a3d504d458ec5b70dfbeba312867f5da.json`). Under D24
IL6-AS1 holds every cis colocalisation at H4 ≥ 0.8 (one of one) while IL6 passes L2G: E3, no gene named. The line is
eCAVIAR's, with clpp 0.005, the lowest of any colocalisation the rows have counted (earlier counted eCAVIAR lines run
from about 0.013 up, e.g. q177, q179); no rule sets a clpp floor, so it counts by the letter.

> [q622] data.variant.credibleSets.rows[2].study traitFromSource Longevity (age >99th survival percentile) projectId GCST nSamples 33444 nCases 5662

The 99th-percentile set's study has 5,662 cases (q622): Deelen's European 99th's 3,484 cases (as in rows 12 and 67)
plus Zeng's 2,178 centenarians (pmid-26912274#q2), so it is the trans-ethnic analysis carrying CLHLS (derived). For
row 48.

## Reading 2026-11-11, record

> [q623] data.variant.credibleSets count 6

> [q624] data.variant.credibleSets.rows[1] studyLocusId 34741810ca5197f07f78d981561229f0 studyId GCST012210 pValueMantissa 8 pValueExponent -15 beta 0.3084 finemappingMethod PICS

> [q625] data.variant.credibleSets.rows[1].locus.rows[0] posteriorProbability 0.1094118066419115

> [q626] data.variant.credibleSets.rows[1].locus.rows[0].variant id 7_34054385_A_G

> [q627] data.variant.credibleSets.rows[1].qualityControls[2] Study locus from curated top hit

> [q628] data.variant.credibleSets.rows[1].l2GPredictions.rows[0] score 0.9315248131752014

> [q629] data.variant.credibleSets.rows[1].l2GPredictions.rows[0].target approvedSymbol BMPER

> [q630] data.credibleSet.colocalisation count 4

> [q631] data.credibleSet.colocalisation.rows[0] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9798208240551841 clpp 0.04267495720797566 betaRatioSignAverage -1

> [q632] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study id gtex-v10_exon_brain_cerebellum_ensg00000164619_10_7_34153411_34153909 traitFromSource ENSG00000164619.10_7_34153411_34153909 studyType eqtl

> [q633] data.credibleSet.colocalisation.rows[3].otherStudyLocus.study id gtex-v10_ge_brain_cerebellum_ensg00000164619 traitFromSource ENSG00000164619 studyType eqtl

Row 49's BMPER lead (`variant-7_34054385_A_G-all.json`): six credible sets (q623), one lifespan-class, Liu 2021's
(GCST012210, PICS, from the curated top hit and without an in-sample LD reference, q624, q627). The lead's PIP there is
0.109 (q625, q626), the top of about 25 members, tied with 7_34054424_A_G: C2 by §4.2's letter. L2G names BMPER at
0.93 (q628, q629; BBS9 0.05). The other sets: a 71-person Delta-CEHC metabolite set and four GTEx cerebellar BMPER
(ENSG00000164619) expression and exon QTL sets. Liu's set has four colocalisations (q630,
`coloc-34741810ca5197f07f78d981561229f0.json`), all BMPER cerebellum or cerebellar-hemisphere eQTLs at H4 0.975 to
0.980 (eCAVIAR, clpp 0.035 to 0.043; q631 to q633): L2G ≥ 0.5 with a cis-QTL colocalisation, E1 BMPER. For row 49.

## Reading 2026-11-11, supplement

> [q634] data.variant.credibleSets count 34

> [q635] data.variant.credibleSets.rows[22] studyLocusId 99e9acb36832b3d0f43a6ffb2cbfbf32 studyId GCST90321079 pValueMantissa 9 pValueExponent -9 beta 0.006039821 finemappingMethod PICS

> [q636] data.variant.credibleSets.rows[22].study traitFromSource Aging projectId GCST nSamples 1559001 nCases 0

> [q637] data.variant.credibleSets.rows[22].locus.rows[0] posteriorProbability 0.14839243040180664

> [q638] data.variant.credibleSets.rows[22].locus.rows[0].variant id 7_114608796_A_G

> [q639] data.variant.credibleSets.rows[22].l2GPredictions.rows[0] score 0.9152749180793762

> [q640] data.variant.credibleSets.rows[22].l2GPredictions.rows[0].target approvedSymbol FOXP2

> [q641] data.variant.credibleSets.rows[25] studyLocusId a767ed5edba98399f7a2beec19cfec1a studyId GCST90275148 pValueMantissa 1.5869419574737549 pValueExponent -10 beta -0.025512637001286472 finemappingMethod SuSiE-inf

> [q642] data.variant.credibleSets.rows[25].study traitFromSource Attention deficit hyperactivity disorder (adjusted for sex) projectId GCST nSamples 58286 nCases 21738

> [q643] data.variant.credibleSets.rows[25].locus.rows[0].variant id 7_114608796_A_G

> [q644] data.variant.credibleSets.rows[7] studyLocusId 39ee17b887c65e4b6eec66cc3460c3dc studyId GCST90245879 pValueMantissa 6 pValueExponent -9 beta -0.017676765 finemappingMethod PICS

> [q645] data.variant.credibleSets.rows[7].study traitFromSource Genetically independent pain phenotypes (GIP1) projectId GCST nSamples 265000 nCases 0

> [q646] data.variant.credibleSets.rows[7].locus.rows[0].variant id 7_114608796_A_G

> [q647] data.credibleSet.colocalisation count 0

Row 50's FOXP2 lead (`variant-7_114608796_A_G-all.json`): 34 credible sets (q634). One is lifespan-class, Rosoff's
mvAge (GCST90321079, "Aging", PICS, from the curated top hit and without an in-sample LD reference, q635, q636): the lead
tops it at PIP 0.148 (q637, q638), C2 by §4.2's letter; L2G names FOXP2 at 0.92 (q639, q640; MDFIC 0.07). Its beta is
the alt G's, +0.0060, G healthier. QTL colocalisations for that set (`coloc-qtl-99e9acb36832b3d0f43a6ffb2cbfbf32.json`):
none, count 0 (q647). So L2G ≥ 0.5 alone: E2 FOXP2. The other 33 sets: ADHD (eight, the lead topping the ADuLT sets; in
GCST90275148 the lead's own β −0.0255 for G, PIP 0.196, q641 to q643), pain (seven, Tsepilov's pain factor led by the
lead, G −0.0177, PIP 0.151, q644 to q646; the rest led by neighbours), sleep duration (three), smoking initiation and
current smoking (three), substance use (three), education (two), IGF-1, diastolic pressure, chloride and chronic airway
obstruction, these led by other variants at PIP 0.08 to 0.75 with the lead at 0.003 to 0.085, so their betas are not
the lead's. Every set's L2G names FOXP2 (0.69 to 0.93). For row 50.

## Reading 2026-11-11, supplement

> [q648] data.variant.credibleSets count 279

> [q649] data.variant.credibleSets.rows[34] studyLocusId 21334332b750b2ccf8f92f70af11d35e studyId GCST90624049 pValueMantissa 8.90999984741211 pValueExponent -17 beta -0.0144044878093618 finemappingMethod PICS

> [q650] data.variant.credibleSets.rows[34].study traitFromSource Frailty (Factor 3 - Multimorbidity) projectId GCST nSamples 699030 nCases 0

> [q651] data.variant.credibleSets.rows[34].locus.rows[0] posteriorProbability 0.8231215958203267

> [q652] data.variant.credibleSets.rows[34].locus.rows[0].variant id 7_130045757_G_A

> [q653] data.variant.credibleSets.rows[34].locus.rows[1].variant id 7_130023656_C_T

> [q654] data.credibleSet.colocalisation.rows[211] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9953679542579715 clpp 0.17687840417967318 rightStudyType gwas

> [q655] data.credibleSet.colocalisation.rows[211].otherStudyLocus.study id GCST010479 traitFromSource Coronary artery disease studyType gwas

> [q656] data.credibleSet.colocalisation.rows[197].otherStudyLocus.study id GCST90692422 traitFromSource Essential hypertension (PheCode 401.1) studyType gwas

> [q657] data.credibleSet.colocalisation count 329

> [q658] data.credibleSet.colocalisation count 0

> [q659] data.variant.credibleSets.rows[34].l2GPredictions.rows[0] score 0.9346437454223633

> [q660] data.variant.credibleSets.rows[34].l2GPredictions.rows[0].target approvedSymbol ZC3HC1

> [q661] data.variant.credibleSets.rows[75] studyLocusId 4b165ac97182f6f6e4b9de39a29bd567 studyId GCST90479543 pValueMantissa 7.300000190734863 pValueExponent -17 beta -0.0648509723196163 finemappingMethod PICS

> [q662] data.variant.credibleSets.rows[75].study traitFromSource Coronary artery / coronary heart disease (including heart attack, angina) projectId GCST nSamples 404034 nCases 61575

> [q663] data.variant.credibleSets.rows[75].locus.rows[0].variant id 7_130045757_G_A

Row 51's ZC3HC1 lead (`variant-7_130045757_G_A-all.json`, `coloc-gwas-21334332.json`, `coloc-qtl-21334332.json`):
279 credible sets (q648), 263 of them holding only the lead and rs11556924; 42 led by the lead, 236 by
rs11556924, one by 7_130030572_T_C. The only one of the scoring classes is Foote 2025's frailty factor 3 (q649, q650; n 699,030, flagged
for quality control): the lead tops it, PIP 0.823 (q651, q652), rs11556924 the rest (q653, 0.177), β −0.0144 per A
(the set's lead is the row's lead, so the sign is read: A less frail, as the deposit, pmid-40759756#q6); L2G
ZC3HC1 0.93 (q659, q660), the only gene scored. No lifespan, longevity or own-survival set holds either SNP. That set
colocalises with 329 GWAS sets (q657), coronary artery disease (q654, q655, H4 0.995) and hypertension (q656) among
them; with only those two SNPs in nearly every set, H4 about 0.995 is what any pair of such sets gives, so it shows one shared
haplotype, not which trait carries the other. No QTL colocalisation (q658). The other sets are coronary disease,
blood pressure and hypertension, blood cell counts (platelets, eosinophils, basophils, red cells), kidney function,
height, SHBG and IGF-1; in Verma's coronary set led by the variant A lowers risk (β −0.065, q661 to q663).
For row 51.

## Reading 2026-11-11, supplement

> [q664] data.variant.credibleSets.rows[34].qualityControls[1] Study locus finemapped without in-sample LD reference

> [q665] data.variant.credibleSets.rows[17] studyLocusId 13205b25196a89e365230ab362780f31 studyId GCST010866 pValueMantissa 1 pValueExponent -17 beta -0.0509404 finemappingMethod PICS

> [q666] data.variant.credibleSets.rows[17].study traitFromSource Coronary artery disease projectId GCST nSamples 649058 nCases 121234

> [q667] data.variant.credibleSets.rows[17].locus.rows[0] posteriorProbability 0.8320779693578286

Row 51, the advisor's read: Foote's set was fine-mapped without in-sample LD (q664), one PICS set. Of the 279 sets at
the locus, rs11556924 leads 236 (q648), among them the coronary artery disease set of 121,234 cases (q665, q666),
where rs11556924 holds PIP 0.83 (q667; its variant is 7_130023656_C_T) and the lead the rest. Which SNP acts is open;
C1 stands on Foote's set by D17.2's letter. For row 51.

## Reading 2026-11-11, supplement

> [q668] data.variant.credibleSets count 507

rs268 (8_19956018_A_G) sits in 507 credible sets (`variant-8_19956018_A_G-all.json` and `-p2.json`, all 507 listed
by trait): lipid, lipoprotein and fatty-acid sets, and outside them only red-cell, reticulocyte and platelet measures,
disorders of lipoid metabolism, glycoprotein acetyls, eight plasma proteins (ANGPTL3, APOA1, APOC1, APOD, IL32, MENT, MFGE8, PLTP), a multi-trait
sex score and coronary artery disease (two sets); none of a lifespan, longevity, healthspan or multivariate-ageing
study (Rosoff's mvAge set is not among them). For row 52.

> [q669] data.variant.credibleSets.rows[205] studyLocusId 73f3f8e5f6cf89c6d89d762b11fdbeb2 studyId GCST005194 pValueMantissa 4.504735946655273 pValueExponent -8 beta 0.00985076963903044 finemappingMethod SuSiE-inf

van der Harst 2018's coronary artery disease (GCST005194, 34,541 cases), SuSiE-inf, β +0.0099 per G. For row 52.

> [q670] data.variant.credibleSets.rows[205].locus.rows[0] posteriorProbability 0.9956946186355491

rs268 holds PIP 0.996 in that set. For row 52.

> [q671] data.variant.credibleSets.rows[221] studyLocusId 7ad55d71e6c4e5efd4212d07e1f3d2fa studyId GCST90132314 pValueMantissa 4.098146915435791 pValueExponent -11 beta 0.005323644810909629 finemappingMethod SuSiE-inf

Aragam 2022's coronary artery disease (GCST90132314), β +0.0053 per G; a one-variant set. For row 52.

> [q672] data.variant.credibleSets.rows[221].locus.rows[0] posteriorProbability 0.9959441497517634

rs268, PIP 0.996: the coronary disease signal is the variant itself. Not scoring class, so it does not set causal
confidence (D17.2); it shows G raising coronary disease. For row 52.

> [q673] data.variant.credibleSets.rows[205].l2GPredictions.rows[0] score 0.992228090763092

L2G's top gene in the set, LPL at 0.99 (target on the next line). For row 52.

> [q674] data.variant.credibleSets count 579

rs15285 (8_19967156_C_T) sits in 579 sets (`-all` and `-p2`, read). For row 52.

> [q675] data.variant.credibleSets.rows[144] studyLocusId c7200f5a0479b12d13660dd8a755d99d studyId GCST009450 pValueMantissa 8 pValueExponent -10 beta null finemappingMethod PICS

Wright 2019's fathers' meta-analysis (GCST009450, n 699,000), PICS, P 8e-10. For row 52.

> [q676] data.variant.credibleSets.rows[144].locus.rows[0] posteriorProbability 0.06578173779206146

rs15285 tops it at PIP 0.066 of 25 members, a flat set (C3 for that signal); L2G LPL 0.98. For row 52.

> [q677] data.variant.credibleSets.rows[42] studyLocusId 16d195892c6b7755c759762abf7d5415 studyId GCST90132314 pValueMantissa 4.528810501098633 pValueExponent -16 beta -0.006063034055759036 finemappingMethod SuSiE-inf

Aragam 2022's coronary disease again (GCST90132314), a 25-member set: β −0.0061 per T. For row 52.

> [q678] data.variant.credibleSets.rows[42].locus.rows[5] posteriorProbability 0.027417425780295872

rs15285 at PIP 0.027 in it, and rs268 is not a member: one study, two coronary disease signals at LPL, rs268's set
(q671) and this one. For row 52.

## Reading 2026-11-11, supplement

> [q679] data.variant.credibleSets count 9

Open Targets 26.09, variant 8_27584547_G_A (rs7844965; `variant-8_27584547_G_A-all.json`): 9 credible sets, all
read (q680 to q703; the eQTL's own set q705 to q711). Two are lifespan-class (Pilling's, q680; Wright's fathers' meta, q687); none is healthspan or
multivariate. For row 53.

> [q680] data.variant.credibleSets.rows[1] studyLocusId 3e6a9cd086b2456f2effcaa96e20812d studyId GCST006697 pValueMantissa 7.7839131355285645 pValueExponent -9 beta -0.00866575786785378 finemappingMethod SuSiE-inf

Pilling 2017's combined parents' attained age (GCST006697), SuSiE-inf: P 7.8 × 10⁻⁹, β −0.0087 for alt A (Pilling's G
+0.0154, pmid-29227965#q24: the sign agrees, so the set's β is A's, the alt allele's). For row 53.

> [q681] data.variant.credibleSets.rows[1].study traitFromSource Parental longevity (combined parental attained age, Martingale residuals) projectId GCST nSamples 389166 nCases 0

Its study: Pilling's 389,166. For row 53.

> [q682] data.credibleSet.locus.rows[0] posteriorProbability 0.6603204145380442

Pilling's set (`set-3e6a9cd0.json`): rs7844965 holds posterior 0.66, the set's lead. The tier rests on this study,
so causal confidence is C1 (§4.2, PIP ≥ 0.5; D17.2). For row 53.

> [q683] data.credibleSet.locus.rows[1] posteriorProbability 0.22950681537282344

The set's second member holds 0.23 (q684): rs6558008, the window's smallest P in Timmers 2019
(pmid-30642433#q247), r² 0.97 to the lead. Which of the two acts is not settled. For row 53.

> [q684] data.credibleSet.locus.rows[1].variant.rsIds[0] rs6558008

It is rs6558008. For row 53.

> [q685] data.credibleSet.l2GPredictions.rows[0] score 0.22877295315265656

Locus-to-gene on Pilling's set: the top gene scores 0.23 (q686), CLU 0.09, SCARA3 0.06; none reaches 0.5. For row 53.

> [q686] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol CHRNA2

The top gene is CHRNA2. For row 53.

> [q687] data.variant.credibleSets.rows[6] studyLocusId 755010ed77d44199e9b0b145e834f4cc studyId GCST009450 pValueMantissa 6 pValueExponent -10 beta null finemappingMethod PICS

Wright's fathers' meta-analysis (GCST009450), PICS: P 6 × 10⁻¹⁰; it pools UK Biobank, Pilling's fathers. For row 53.

> [q688] data.variant.credibleSets.rows[6].locus.rows[0] posteriorProbability 0.42165557355481104

rs7844965 holds 0.42 there, the set's lead. For row 53.

> [q689] data.credibleSet.colocalisation count 2

Pilling's set colocalises with two QTLs (cis only, q690 to q693). For row 53.

> [q690] data.credibleSet.colocalisation.rows[0] rightStudyType eqtl h4 0.5164315849830894 clpp 0.0009752635847563811

The first: an eQTL at H4 0.52, under §4.2's 0.8. For row 53.

> [q691] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study.target approvedSymbol CHRNA2

CHRNA2's expression (one transcript, GTEx v10 cerebellum, q690). For row 53.

> [q692] data.credibleSet.colocalisation.rows[1] rightStudyType sceqtl h4 0.9841611466656495 clpp 0.05339663322275854

The second: a single-cell eQTL at H4 0.98, over 0.8. For row 53.

> [q693] data.credibleSet.colocalisation.rows[1].otherStudyLocus.study.target approvedSymbol GULOP

GULOP (ENSG00000234770), in enterocyte progenitor (OLFM4+) cells of the IBDverse study, cis. For row 53.

> [q694] data.credibleSet.colocalisation.rows[0] rightStudyType sceqtl h4 0.9855003246002719 clpp 0.05906239463285254

Wright's set colocalises once, with the same single-cell eQTL, H4 0.99. For row 53.

> [q695] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study.target approvedSymbol GULOP

GULOP again. So GULOP holds every colocalisation at H4 ≥ 0.8 on both lifespan-class sets (two of two) and CHRNA2
none: E2 by colocalisation alone, D24's rival test not met by CHRNA2 (L2G 0.23, H4 0.52). GULOP is a unitary
pseudogene (db-ensembl-116#q368), and the eQTL is one cell type of one study. For row 53.

> [q696] data.variant.credibleSets.rows[5] studyLocusId 6c6c4b171010fff1f6b074dfba31e6fa studyId GCST90692035 pValueMantissa 6.622216701507568 pValueExponent -13 beta 0.14918563722917957 finemappingMethod SuSiE-inf

A never-smoking set (GCST90692035), SuSiE-inf, P 6.6 × 10⁻¹³, β +0.149 for A; rs7844965 its only member (q697). For row 53.

> [q697] data.variant.credibleSets.rows[5].locus.rows[0] posteriorProbability 0.9999999999990195

Posterior about 1.0 to the lead. But the study is UK Biobank's African-ancestry subset, 6,532 people
(db-gwascatalog-2026.10.29#q344), and q703's East Asian subset of 2,649 gives P 1.3 × 10⁻¹³: P values of that size in
samples so small, for a SNP with no European smoking record in the Catalog (q341), are not read as evidence of a
smoking route. For row 53.

> [q698] data.variant.credibleSets.rows[7] studyLocusId 7ace9811283dfb31138c2e87d93a931a studyId GCST90243964 pValueMantissa 8 pValueExponent -12 beta -0.07472354619593642 finemappingMethod PICS

Lung cancer or family history of lung cancer (GCST90243964), PICS, P 8 × 10⁻¹², set led by rs6558008 (alt C,
β −0.075): C lowers it (db-gwascatalog-2026.10.29#q342), and C travels with the lead's A (pmid-30642433#q247). The
family-history part counts parents' lung cancer, close to the parental-lifespan phenotype itself. For row 53.

> [q699] data.variant.credibleSets.rows[7].study traitFromSource Lung cancer or family history of lung cancer projectId GCST nSamples 329946 nCases 29266

Its study: 329,946 people, 29,266 cases. For row 53.

> [q700] data.variant.credibleSets.rows[3] studyLocusId 6a8692efefd5ed062db6451bd9533e7e studyId GCST90475338 pValueMantissa 2.259000062942505 pValueExponent -11 beta -0.02082 finemappingMethod PICS

Hematocrit (maximum), PICS, P 2.3 × 10⁻¹¹, led by another SNP (rs7844965 posterior 0.16); a lower hematocrit with
the set lead's alt allele. For row 53.

> [q701] data.variant.credibleSets.rows[4] studyLocusId 6bef72a43e118458c27cabb475206a4d studyId GCST90475372 pValueMantissa 7.705067157745361 pValueExponent -9 beta -0.008492050348549666 finemappingMethod SuSiE-inf

Hemoglobin (maximum), SuSiE-inf, P 7.7 × 10⁻⁹, led by rs7844965 (posterior 0.38): A lowers hemoglobin, β −0.0085.
For row 53.

> [q702] data.variant.credibleSets.rows[8] studyLocusId b5ad4484442e73cd3a7e2a5dc0027f8b studyId GCST90476454 pValueMantissa 1.14058518409729 pValueExponent -15 beta -0.012008762237760203 finemappingMethod SuSiE-inf

White blood cell count, SuSiE-inf, P 1.1 × 10⁻¹⁵, led by another SNP (rs7844965 posterior 0.016). For row 53.

> [q703] data.variant.credibleSets.rows[0] studyLocusId 0e88fdf9c30f2058634130f8a8f6fd99 studyId GCST90692469 pValueMantissa 1.289778232574463 pValueExponent -13 beta 0.10554334405173751 finemappingMethod SuSiE-inf

A second never-smoking set (GCST90692469), P 1.3 × 10⁻¹³, rs7844965 at posterior 0.12; the East Asian subset of
2,649 (db-gwascatalog-2026.10.29#q345). For row 53.

## Reading 2026-11-11, supplement

> [q704] data.variant.credibleSets.rows[1].qualityControls[1] Study locus finemapped without in-sample LD reference

Pilling's set was fine-mapped without in-sample LD (as row 51's set was), so its 0.66 is that method's. For row 53.

> [q705] data.variant.credibleSets.rows[2] studyLocusId 615439975207128bcf1716ba919f3451 studyId OTAR2057_IBDverse_ge_Enterocytes_progenitor_crypt_OLFM4++_ENSG00000234770 pValueMantissa 1.6117099523544312 pValueExponent -9 beta -0.359968 finemappingMethod SuSie

The GULOP eQTL's own credible set (IBDverse, enterocyte progenitors, ENSG00000234770): P 1.6 × 10⁻⁹, SuSiE. For row 53.

> [q706] data.variant.credibleSets.rows[2].study traitFromSource ENSG00000234770 projectId OTAR2057_IBDverse nSamples 303 nCases null

It rests on 303 samples. For row 53.

> [q707] data.variant.credibleSets.rows[2].qualityControls[0] Study has quality control flag(s)

Open Targets flags the study's quality control. For row 53.

> [q708] data.variant.credibleSets.rows[2].locus.rows[0] posteriorProbability 0.5654238337902764

The eQTL set's lead holds 0.57 (q709). For row 53.

> [q709] data.variant.credibleSets.rows[2].locus.rows[0].variant id 8_27565545_G_C

It is 8_27565545_G_C, 19 kb from the lead. For row 53.

> [q710] data.variant.credibleSets.rows[2].locus.rows[4] posteriorProbability 0.057901134218701994

The row's lead holds 0.058 in the eQTL's set (q711), and the colocalisations' CLPP is about 0.05 (q692, q694):
H4 says the two signals share a variant, CLPP that the shared variant is not well placed. The E2 call stands on H4
by §4.2's letter, on a QC-flagged single-cell study of 303 samples whose set the lead does not lead. For row 53.

> [q711] data.variant.credibleSets.rows[2].locus.rows[4].variant id 8_27584547_G_A

The row's lead. For row 53.

## Reading 2026-11-12, record

> [q712] data.credibleSets.rows[0] studyLocusId 7d1d08292a3cb5c88db9c4c228ba94e7 finemappingMethod PICS

`credibleSets` over the eight studies (the seven lifespan, healthspan and longevity studies plus Wright 2019's
current-age study GCST009448, as at row 10, q75) for 8_30981030_T_G: one set, Wright's age study's, PICS. No
lifespan, longevity or healthspan study holds the lead. For row 54.

> [q713] data.study.credibleSets.rows[1] studyLocusId 7d1d08292a3cb5c88db9c4c228ba94e7 pValueMantissa 8 pValueExponent -9 finemappingMethod PICS

`study-GCST009448-sets.json` (q77): the set is built at P 8 × 10⁻⁹, the uncorrected P (pmid-31484785#q100); the
row reads the study at the genomic-control P, 8.7 × 10⁻⁷. For row 54.

> [q714] data.study.credibleSets.rows[1].locus count 29

The set holds 29 variants. For row 54.

> [q715] data.study.credibleSets.rows[1].locus.rows[0] posteriorProbability 0.0988035086190874

The lead's posterior probability, 0.0988, the set's highest, just under §4.2's 0.1: C3 (in a set, PIP < 0.1).
The rest spread from 0.053 down. For row 54.

> [q716] data.study.credibleSets.rows[1].l2GPredictions.rows[0] score 0.5907216668128967

> [q717] data.study.credibleSets.rows[1].l2GPredictions.rows[0].target approvedSymbol WRN

Locus-to-gene on this set: WRN 0.591, over §4.2's 0.5. For row 54.

> [q718] data.study.credibleSets.rows[1].l2GPredictions.rows[1] score 0.4991125166416168

> [q719] data.study.credibleSets.rows[1].l2GPredictions.rows[1].target approvedSymbol PURG

PURG 0.499, 0.001 under the bar, so not a rival by D24's letter. For row 54.

> [q720] data.study.credibleSets.rows[1].l2GPredictions.rows[2] score 0.24657242000102997

> [q721] data.study.credibleSets.rows[1].l2GPredictions.rows[2].target approvedSymbol TEX15

TEX15 0.247. The seed list's `l2g_top WRN:0.59` is this same record, not a second source. For row 54.

> [q722] data.credibleSet.colocalisation count 24

`coloc-7d1d08292a3cb5c88db9c4c228ba94e7.json`, the set's colocalisations: 24, every one with another GWAS
(`rightStudyType gwas` on all 24, counted), none with a QTL study, so no cis-QTL colocalisation for the effector
call. For row 54.

> [q723] data.credibleSet.colocalisation.rows[6] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9639209679470132 clpp 0.02370518614300261 rightStudyType gwas

> [q724] data.credibleSet.colocalisation.rows[6].otherStudyLocus.study id GCST006867 traitFromSource Type 2 diabetes studyType gwas

Type 2 diabetes, H4 0.96. For row 54.

> [q725] data.credibleSet.colocalisation.rows[8] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9727116469928901 clpp 0.03135062418361347 rightStudyType gwas

> [q726] data.credibleSet.colocalisation.rows[8].otherStudyLocus.study id GCST90239652 traitFromSource High density lipoprotein cholesterol levels studyType gwas

HDL cholesterol, H4 0.97. For row 54.

> [q727] data.credibleSet.colocalisation.rows[14].otherStudyLocus.study id GCST90476435 traitFromSource triglyceride (mean, inv-norm transformed) studyType gwas

Triglycerides (H4 0.98), with mixed hyperlipidaemia and HbA1c alongside. For row 54.

> [q728] data.credibleSet.colocalisation.rows[22].otherStudyLocus.study id GCST90179150 traitFromSource Body mass index (MTAG) studyType gwas

Body mass index (H4 0.94), with predicted visceral fat alongside. For row 54.

> [q729] data.credibleSet.colocalisation.rows[9].otherStudyLocus.study id GCST90131901 traitFromSource Insomnia studyType gwas

Insomnia (H4 0.98). For row 54.

> [q730] data.credibleSet.colocalisation.rows[16].otherStudyLocus.study id GCST005316 traitFromSource Intelligence (MTAG) studyType gwas

Intelligence (H4 0.95), with general cognitive ability (0.42) alongside. None of the records gives a beta, so no
direction for G on any of these traits is read. For row 54.

> [q731] data.variant.credibleSets count 19

`variant-8_30981030_T_G-all.json`, the lead's own sets: 19, all GWAS but one; they repeat the colocalising traits (type 2 diabetes, triglycerides, HDL, mixed hyperlipidaemia, visceral fat, metabolic syndrome, insomnia, intelligence, education) and Wright's "Longevity" set. For row 54.

> [q732] data.variant.credibleSets.rows[10] studyLocusId 972f2e986671f3cfe10753a837ee01d4 studyId gtex-v10_ge_brain_caudate_ensg00000172733 pValueMantissa 8.338000297546387 pValueExponent -9 beta -0.237478 finemappingMethod SuSie

The one expression set: GTEx v10 caudate (brain), ENSG00000172733, PURG (db-ensembl-116#q378), SuSiE, β −0.237. For row 54.

> [q733] data.variant.credibleSets.rows[10].qualityControls[0] Study has quality control flag(s)

> [q734] data.variant.credibleSets.rows[10].locus.rows[2] posteriorProbability 0.04463040832819606

The source flags that set for quality control, and the lead's probability in it is 0.045. A membership, not a colocalisation with the age set (q722: none with a QTL study), so it gives PURG no E1/E2 criterion (D24) and, unlike row 53's, no flagged colocalisation (D27.7). For row 54.

## Reading 2026-11-12, supplement

`variant-8_54566349_G_GCT-all.json` (row 55's insertion, keyed as FinnGen keys it, db-finngen-r11#q31) and
`variant-8_54566168_G_A-all.json` (its r² 1.0 proxy rs13279568, db-ensembl-116#q383): both answer the same.

> [q735] data variant null

Open Targets 26.09 holds no record of the insertion or of the proxy, so no credible set holds either: C4, E4. For
row 55.

## Reading 2026-11-12, record

`variant-8_58925574_A_G-all.json`: Open Targets 26.09 answers q735's text for rs13262617 too, and its variant
search (q575's text) finds nothing for rs13262617 nor for its best CEU tags rs79725344 and rs10504278 (r² 0.71,
db-ensembl-116#q392): no record, so no credible set holds the lead: C4, E4. For row 56.

## Reading 2026-11-12, record

> [q736] data.variant.credibleSets.rows[0] studyLocusId 06b8a7a353e4c3bffd5e0ebbe8a5970a studyId GCST012419 pValueMantissa 2 pValueExponent -9 beta 5.969329 finemappingMethod PICS

> [q737] data.variant.credibleSets.rows[0].locus.rows[0] posteriorProbability 0.3413763657877318

> [q738] data.variant.credibleSets.rows[0].qualityControls[1] Study locus finemapped without in-sample LD reference

> [q739] data.variant.credibleSets.rows[0].qualityControls[2] Study locus from curated top hit

> [q740] data.variant.credibleSets.rows[0].l2GPredictions.rows[0] score 0.47552305459976196

> [q741] data.variant.credibleSets.rows[0].l2GPredictions.rows[0].target approvedSymbol ALDH1B1

> [q742] data.credibleSet.colocalisation count 0

`variant-9_38322519_G_T-all.json`: rs10973748 is in one credible set, Gurinovich's NECS study's (PICS, 9 variants,
built from the GWAS Catalog's curated top hit without in-sample LD, the study QC-flagged), where its posterior
probability, the set's highest, is 0.341: C2. Locus-to-gene gives ALDH1B1 0.476, under 0.5, then IGFBPL1 0.133 and
SHB 0.091; `coloc-06b8a7a353e4c3bffd5e0ebbe8a5970a.json` finds no colocalisation (all study types). Assessed, no
criterion met: E3, no gene named. The variant search finds the same record (`search-rs10973748.json`, total 1,
9_38322519_G_T). For row 58.

## Reading 2026-11-12, supplement

> [q743] data.search.hits[0] id 9_133266456_T_C entity variant

The variant search: rs2519093 is 9_133266456_T_C. For row 59.

> [q744] data.variant.credibleSets count 510

The lead sits in 510 credible sets (`variant-9_133266456_T_C-all.json`, `-all-p2.json`, all read): proteins, lipids,
blood counts, thrombosis and coronary disease, most with ABO's locus-to-gene about 0.58; none from a lifespan,
longevity, healthspan or frailty study. For row 59.

> [q745] data.credibleSets count 107

Every set of eleven longevity studies (GCST009890, GCST006697, GCST006701, GCST006702, GCST011100, GCST009450,
GCST009448, GCST007406, GCST90321079, GCST008598, GCST008599: Timmers 2019 and 2020, Pilling 2017, Wright 2019, Zenin
2019, Rosoff's mvAge, Deelen 2019; `credibleSets-longevity11-all.json`): 107 sets, none on chromosome 9 between 130
and 136 Mb. For row 59.

> [q746] data.credibleSets count 426

Every set of Foote 2025's general frailty factor and six factors (`credibleSets-foote7-all.json`): 426, the nearest to
ABO at 9:136,626,337, 3.4 Mb away. For row 59.

## Reading 2026-11-12, supplement

> [q747] data.search total 0

Open Targets' search finds no record of rs75824829. For row 60.

> [q748] data variant null

Nor by its GRCh38 id 9_135376756_G_A: no credible set, no locus-to-gene, no colocalisation. For row 60.

## Reading 2026-11-12, supplement

> [q749] data.search total 0

Open Targets 26.09 finds no variant for rs547541271. For row 61.

> [q750] data variant null

Nor by its id 10_11118452_C_T: no fine-mapping, no locus-to-gene.

> [q751] data.study id GCST90551886 traitFromSource Lifespan nSamples 212863

> [q752] data.study.credibleSets count 17

Park's women's study holds 17 credible sets; none lies on chromosome 10 (derived, from the 17 lead ids).

## Reading 2026-11-12, supplement

> [q753] data.search total 0

Open Targets' search for rs11186068: nothing ...

> [q754] data variant null

... and no variant record at 10_90207407_T_G: no credible set, no locus-to-gene. For row 62.

## Reading 2026-11-12, supplement

> [q755] data.variant.credibleSets count 845

rs35198068 (10_112995025_T_C) lies in 845 credible sets, mostly diabetes, glycaemic and other traits. For row 63.

> [q756] data.credibleSet studyLocusId 32f4abfd01de830d55171b276aea34be finemappingMethod SuSiE-inf pValueMantissa 4.092370510101318 pValueExponent -30 beta 0.020915560333601382

Zenin 2019's healthspan set at TCF7L2: SuSiE-inf, P 4.1e-30 ... For row 63.

> [q757] data.credibleSet.study id GCST007406 traitFromSource Healthspan

... study GCST007406, healthspan. For row 63.

> [q758] data.credibleSet.locus.rows[0] posteriorProbability 0.4448656202625202 is95CredibleSet true

rs35198068 PIP 0.445 ... For row 63.

> [q759] data.credibleSet.locus.rows[1] posteriorProbability 0.432248193866332 is95CredibleSet true

... rs34872471 0.432 ... For row 63.

> [q760] data.credibleSet.locus.rows[2] posteriorProbability 0.1228130840805406 is95CredibleSet true

... rs7903146 0.123: the lead at PIP 0.1 to 0.5, `causal:C2`. For row 63.

> [q761] data.credibleSet.l2GPredictions.rows[0] score 0.9093946218490601

Locus-to-gene 0.909 ... For row 63.

> [q762] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol TCF7L2

... TCF7L2. For row 63.

> [q763] data.credibleSet.colocalisation count 0

No QTL colocalisation of the healthspan set (eQTL, pQTL, sQTL and their single-cell forms queried): L2G alone, `effector:E2`. For row 63.

> [q764] data.credibleSet studyLocusId f2b74ee748693bbb2d39ba97f8fddfe2 finemappingMethod PICS pValueMantissa 4 pValueExponent -28 beta null

Timmers 2020's multivariate set (GCST011100, PICS, P 4e-28) ... For row 63.

> [q765] data.credibleSet.locus.rows[0] posteriorProbability 0.4692622796271064 is95CredibleSet true

... led by rs35198068 at PIP 0.469; multivariate, named, not counted (D25.5, D27.6). For row 63.

> [q766] data.credibleSet studyLocusId a2b7c6567c8ba519ed1cd1170d2db39e finemappingMethod PICS pValueMantissa 5 pValueExponent -16 beta -0.008514585

mvAge's set (GCST90321079, PICS, P 5e-16) ... For row 63.

> [q767] data.credibleSet.locus.rows[0] posteriorProbability 0.33006469460849164 is95CredibleSet true

... rs35198068 at PIP 0.330; named, not counted. For row 63.

## Reading 2026-11-12, supplement

> [q768] data.credibleSet.colocalisation count 114

The positive control for q763's query: the same `studyTypes` QTL query on row 35's healthspan set (3ebe7ef9958b5c249ce68244b0d819a2, `control-3ebe7ef9958b5c249ce68244b0d819a2-qtlcoloc.json`) returns its 114 QTL colocalisations (q508), so q763's zero is an answer, not a query that cannot see QTLs. For row 63.

## Reading 2026-11-12, supplement

> [q769] data.variant.credibleSets count 25

rs76612380 (11_202785_T_C, `variant-11_202785_T_C`) lies in 25 credible sets ... For row 64.

> [q770] data.variant.credibleSets.rows[16].study id GCST90270909 traitFromSource Lifespan studyType gwas

... one of them a GWAS's, BBJ's survival study; the other 24 are QTL sets. For row 64.

> [q771] data.credibleSet studyLocusId 9f1743923df45578a9e95c019dde4cb4 finemappingMethod PICS pValueMantissa 6 pValueExponent -9 beta -0.08338160893905101

The study's one set (`study-setids-GCST90270909`, `set-9f1743923df45578a9e95c019dde4cb4`): PICS, from the Catalog's
P 6e-9, with beta −0.083, ln 0.92 copied from the Catalog's record (db-gwascatalog-2026.10.29#q417), whose allele is
"?" (q418): the sign settles nothing about the allele. For row 64.

> [q772] data.credibleSet.locus.rows[0] posteriorProbability 0.9442135664016534 is95CredibleSet true

The lead at PIP 0.944 ... For row 64.

> [q773] data.credibleSet.locus.rows[0].variant.rsIds[0] rs76612380

... rs76612380 ... For row 64.

> [q774] data.credibleSet.locus.rows[1] posteriorProbability 0.029435522870490914 is95CredibleSet true

... and rs112762297 at 0.029, the set's second member. PICS reads LD from a reference panel, and the lead has no 1000
Genomes genotypes in Ensembl (db-ensembl-116#q458): a PIP from a single summary P, not a fine-mapping of BBJ's data.
For row 64.

> [q775] data.credibleSet.l2GPredictions.rows[0] score 0.2408827841281891

Locus-to-gene's best, 0.24 ... For row 64.

> [q776] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol BET1L

... BET1L ... For row 64.

> [q777] data.credibleSet.l2GPredictions.rows[1] score 0.1485983282327652

... then 0.15 ... For row 64.

> [q778] data.credibleSet.l2GPredictions.rows[1].target approvedSymbol RIC8A

... RIC8A: no gene reaches 0.5. For row 64.

> [q779] data.credibleSet.colocalisation count 33

The set's QTL colocalisations (`set-9f1743923df45578a9e95c019dde4cb4-qtlcoloc`): 33, of which 25 at H4 ≥ 0.8: SIRT3
14, BET1L 7, PSMD13 2, PKP3 1 and ENSG00000288681 1 (counted from the file). For row 64.

> [q780] data.credibleSet.colocalisation.rows[7] h4 0.979526794873751 clpp 0.04223376379416853 rightStudyType eqtl colocalisationMethod COLOC_PIP_ECAVIAR

One of SIRT3's: H4 0.98 ... For row 64.

> [q781] data.credibleSet.colocalisation.rows[7].otherStudyLocus.study.target approvedSymbol SIRT3

... a SIRT3 transcript's eQTL in skeletal muscle (FUSION). For row 64.

> [q782] data.credibleSet.colocalisation.rows[26] h4 0.9985894833803172 clpp 0.3839486220254775 rightStudyType eqtl colocalisationMethod COLOC_PIP_ECAVIAR

One of BET1L's: H4 0.999 ... For row 64.

> [q783] data.credibleSet.colocalisation.rows[26].otherStudyLocus.study.target approvedSymbol BET1L

... BET1L's expression in transverse colon (GTEx v10). For row 64.

## Reading 2026-11-12, supplement

> [q784] data.credibleSets count 1

> [q785] data.credibleSets.rows[0].study id GCST009448

`credibleSets` over the eight studies (the seven lifespan, healthspan and longevity studies plus Wright 2019's
current-age study GCST009448, as at rows 10 and 54) for 11_43770315_G_A: one set, Wright's age study's. No lifespan,
longevity or healthspan study holds the lead. For row 65.

> [q786] data.credibleSets count 0

The same query for rs4755202 (11_43598388_G_A): no set. For row 65.

> [q787] data.study.credibleSets.rows[0] studyLocusId 96ea20cc681fbe3c5115f3cbbc7ec2fa pValueMantissa 4 pValueExponent -9 finemappingMethod PICS

> [q788] data.study.credibleSets.rows[0].locus count 69

> [q789] data.study.credibleSets.rows[0].locus.rows[0] posteriorProbability 0.12425352940751408

`study-GCST009448-sets.json` (q77, q78): the 11p11 set is built at P 4 × 10⁻⁹, the uncorrected P
(pmid-31484785#q107); the row reads the study at the genomic-control P, 4.8 × 10⁻⁷, so the set sets no causal or
effector level (D28.5). 69 variants by PICS; the lead's posterior probability 0.124 is the set's highest, the next
0.089, 0.087 and 0.080. For row 65.

> [q790] data.credibleSet.l2GPredictions.rows[0] score 0.45437049865722656

> [q791] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol HSD17B12

> [q792] data.credibleSet.l2GPredictions.rows[1] score 0.268466591835022

> [q793] data.credibleSet.l2GPredictions.rows[1].target approvedSymbol ALKBH3

`set-96ea20cc.json`: locus-to-gene on that set, HSD17B12 0.454 (under 0.5), ALKBH3 0.268, ACCS 0.125. The seed's
HSD17B12:0.45 is this record. For row 65, prose.

> [q794] data.credibleSet.colocalisation.rows[10].otherStudyLocus.study id GCST90691892 traitFromSource Diastolic blood pressure, combined automated + manual reading, adjusted by medication - raw studyType gwas

> [q795] data.credibleSet.colocalisation.rows[20].otherStudyLocus.study id GCST90692421 traitFromSource Hypertension (PheCode 401) studyType gwas

> [q796] data.credibleSet.colocalisation.rows[8].otherStudyLocus.study id GCST007982 traitFromSource Sleep duration studyType gwas

The set's 90 GWAS colocalisations: at H4 above 0.9, diastolic and systolic blood pressure, hypertension (H4 0.96)
and doctor-diagnosed high blood pressure, sleep duration (0.98 to 0.99), red cell distribution width, linoleic and
omega-6 fatty acid fractions and age at first sexual intercourse; body mass index and weight at 0.84. The rows
carry no allele, so no direction for A is read from them. For row 65.

> [q797] data.credibleSet.colocalisation count 43

> [q798] data.credibleSet.colocalisation.rows[1].otherStudyLocus.study.target approvedSymbol HSD17B12

`set-96ea20cc-qtlcoloc.json`: 43 QTL colocalisations; at H4 ≥ 0.8, HSD17B12 17 (expression and splicing, in adipose,
skin, artery, lymphoblastoid cells and others), ENSG00000246250 5, API5 1, ACCS 1 (counted from the file). HSD17B12
would lead by D24, with the unnamed ENSG00000246250 at 5 of 24 a rival; the set sets no level (D28.5), so this is
prose. For row 65.

> [q799] data.credibleSet.colocalisation.rows[48].otherStudyLocus.study id GCST90498300 traitFromSource Linoleic acid to total fatty acids percentage studyType gwas

> [q800] data.credibleSet.colocalisation.rows[56].otherStudyLocus.study id GCST90476361 traitFromSource red cell diameter width (RDW, mean, inv-norm transformed) studyType gwas

The same set's colocalisations with the linoleic acid fraction (H4 0.923) and red cell distribution width (H4 0.923),
past the same 0.9 cut as q794 to q796. For row 65.

> [q801] data.variant.credibleSets.rows[23].variant id 11_43770315_G_A

`variant-11_43770315_G_A-leads.json` (the lead's 39 sets, each with its own lead variant): rs4755737 leads two, Wright's
age set (row 23, beta 0.01207) and one splicing set of ENSG00000246250 (row 3). Every blood-pressure, hypertension and
sleep-duration set holding it is led by another variant, so their betas are not A's and give it no direction. For
row 65.

## Reading 2026-11-12, supplement

> [q802] data.credibleSets count 3

> [q803] data.credibleSets.rows[2] studyLocusId 99cf48a1a1b921fafabd9d843831b11f finemappingMethod SuSiE-inf

> [q804] data.credibleSets.rows[2].study id GCST007406

> [q805] data.credibleSets.rows[2].locus count 11

> [q806] data.credibleSets.rows[2].locus.rows[0] posteriorProbability 0.2083564277865569

> [q807] data.credibleSets.rows[2].locus.rows[0].variant id 11_89284793_G_A

`credibleSets-longevity8-11_89284793_G_A` (the eight lifespan-class studies, filtered by membership): three sets hold
rs1126809. Zenin 2019's healthspan (GCST007406), SuSiE-inf, 11 variants, the lead first at PIP 0.208. For row 66.

> [q808] data.credibleSets.rows[0] studyLocusId 1c9ebe5a0d72b917e8a3d0f4c95d090f finemappingMethod PICS

> [q809] data.credibleSets.rows[0].study id GCST011100

> [q810] data.credibleSets.rows[1] studyLocusId 5d7c205424ea4b06ca00e6c17b9bfdc1 finemappingMethod PICS

> [q811] data.credibleSets.rows[1].study id GCST90321079

The two others are PICS sets of the multivariate scans, Timmers 2020 (GCST011100, 58 variants, the lead 0.280) and
Rosoff's mvAge (GCST90321079, 80 variants, 0.143): named, not counted (D25.5, D27.6). For row 66.

> [q812] data.credibleSet.l2GPredictions.rows[0] score 0.8260523676872253

> [q813] data.credibleSet.l2GPredictions.rows[0].target approvedSymbol TYR

`set-99cf48a1` (Zenin's set): locus-to-gene TYR 0.826, the only gene listed. For row 66.

> [q814] data.credibleSet.colocalisation count 2

> [q815] data.credibleSet.colocalisation.rows[1] rightStudyType tuqtl h4 0.9815760469987316 clpp 0.046221027746727116

> [q816] data.credibleSet.colocalisation.rows[1].otherStudyLocus.study.target approvedSymbol NOX4

`set-99cf48a1-qtlcoloc`: two cis QTL colocalisations, both one NOX4 transcript-usage QTL in GTEx artery (aorta H4
0.98; tibial 0.78, under the cut). TYR has none. For row 66.

## Reading 2026-11-12, supplement

> [q817] data variant null

> [q818] data.credibleSets count 0

Open Targets 26.09 has no record of 11_119399248_G_A (rs139137459): no credible set, no locus-to-gene, no
colocalisation. For row 68.

## Reading 2026-11-12, supplement

> [q819] data.variant.credibleSets count 74

> [q820] data.variant.credibleSets.rows[40] studyLocusId 70d4a9c51b534e44d0e9b3fe1f55ab1c pValueMantissa 3.5360000133514404 pValueExponent -10 beta -1.20406

> [q821] data.variant.credibleSets.rows[40].study id schmiedel_2018_ge_th17_memory_ensg00000161791 traitFromSource ENSG00000161791 studyType eqtl

> [q822] data.variant.credibleSets.rows[1].study id GCST90472780 traitFromSource Systolic blood pressure studyType gwas

> [q823] data.variant.credibleSets.rows[1].locus.rows[0] posteriorProbability 0.005304472575683967

> [q824] data.credibleSets count 0

Open Targets 26.09, 12_49569751_A_T (rs55686423): 74 credible sets hold it (q819), none of the eight longevity
studies, mvAge's GCST90321079 among them (q824). It leads only two, T-cell expression sets for ENSG00000161791
(Schmiedel 2018, memory Th17 and Tfh; PIP 0.077 and 0.063, q820, q821); the rest are led by other variants, the
lead at a PIP of 0.001 to 0.09: blood pressure and hypertension (e.g. systolic pressure, PIP 0.005, q822, q823),
large-HDL lipids, lung function, seated height, ever smoked. No locus-to-gene was read. For row 69.

## Reading 2026-11-12, supplement

> [q825] data.variant.credibleSets.rows[2] studyLocusId 01b19cdfc22a89835a7b3d5c1ec3e672 pValueMantissa 4.132812976837158 pValueExponent -11 beta -0.010302969096309407

> [q826] data.variant.credibleSets.rows[2].variant id 12_49587939_T_C

> [q827] data.variant.credibleSets.rows[2].study id GCST90693004 traitFromSource Hypertension (PheCode 401) studyType gwas

A hypertension set (PheCode 401, GCST90693004) led by 12_49587939_T_C, rs7977389 (r² 0.82 to rs55686423,
db-ensembl-116#q516), P 4.1e-11, beta −0.0103 for the set lead's C: C lowers hypertension, as Hoffmann's T raises
systolic pressure (pmid-37550455#q61). For row 69.

## Reading 2026-11-12, supplement

> [q828] data.variant.credibleSets count 20

> [q829] data.variant.credibleSets.rows[2] studyLocusId 3dd6e3793b507c7764279f1f687ad661 pValueMantissa 8 pValueExponent -9 beta null

> [q830] data.variant.credibleSets.rows[2].study id GCST011100 traitFromSource Aging traits (healthspan, parental lifespan or longevity) (multivariate analysis) studyType gwas

> [q831] data.variant.credibleSets.rows[2].locus.rows[0] posteriorProbability 0.0581411253362301

> [q832] data.credibleSets count 1

> [q833] data.credibleSets.rows[0].locus count 77

> [q834] data.variant.credibleSets.rows[6] studyLocusId 5535a0a44a7e27172903ab2afac0c875 pValueMantissa 2.534301280975342 pValueExponent -10 beta -0.008063619220410271

> [q835] data.variant.credibleSets.rows[6].study id GCST005195 traitFromSource Coronary artery disease studyType gwas

> [q836] data.variant.credibleSets.rows[18] studyLocusId f960f14abcf37495761919be6ec864bb pValueMantissa 2.305000066757202 pValueExponent -12 beta -0.0914

> [q837] data.variant.credibleSets.rows[18].study id GCST90018877 traitFromSource Myocardial infarction studyType gwas

> [q838] data.variant.credibleSets.rows[10] studyLocusId 9a8a42e819268bf7a2f8495bd7d6af50 pValueMantissa 6.479000091552734 pValueExponent -13 beta -0.0877

> [q839] data.variant.credibleSets.rows[10].study id GCST90018793 traitFromSource Angina pectoris studyType gwas

> [q840] data.variant.credibleSets.rows[17] studyLocusId c16bb4f39f588ec579956439f2f1d171 pValueMantissa 3.7639999389648438 pValueExponent -16 beta 0.04367

> [q841] data.variant.credibleSets.rows[17].study id GCST90476299 traitFromSource platelet count (mean, inv-norm transformed) studyType gwas

> [q842] data.variant.credibleSets.rows[4] studyLocusId 507796de7faefc6d6fce36e1ca636ede pValueMantissa 7.645884990692139 pValueExponent -11 beta 0.010443520472435667

> [q843] data.variant.credibleSets.rows[4].study id GCST90476454 traitFromSource white blood cell count (WBC, mean, inv-norm transformed) studyType gwas

> [q844] data.variant.credibleSets.rows[14].study id fusion_exon_adipose_naive_ensg00000028203_19_12_95257154_95257181 traitFromSource ENSG00000028203.19_12_95257154_95257181 studyType eqtl

> [q845] data.t1 id ENSG00000028203 approvedSymbol VEZT

> [q846] data.cs.l2GPredictions.rows[0] score 0.320669561624527

> [q847] data.cs.l2GPredictions.rows[0].target approvedSymbol NR2C1 id ENSG00000120798

> [q848] data.cs.colocalisation count 36

> [q849] data.v1.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.07380160668569578

> [q850] data.v2.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.07213870892281404

> [q851] data.v3.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.0734982332155477

> [q852] data.v4.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.07353762903273241

> [q853] data.v5.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.07139513108614232

> [q854] data.v6.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.07555575158786168

> [q855] data.v7.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.07350517890772128

> [q856] data.v8.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.07355233361762198

> [q857] data.cs.colocalisation.rows[2] h4 0.9521904516823316 clpp 0.017664786398943345 colocalisationMethod COLOC_PIP_ECAVIAR rightStudyType gwas

> [q858] data.cs.colocalisation.rows[2].otherStudyLocus.study id GCST005194 traitFromSource Coronary artery disease studyType gwas

Open Targets 26.09, 12_95187042_T_G (rs12830425): 20 credible sets hold it (q828). Of the eight longevity studies,
one: Timmers 2020's multivariate GCST011100, a PICS set of 77 variants that the lead itself leads at a posterior of
0.058 (q829-q833). Its locus-to-gene: NR2C1 0.32 (q846, q847), VEZT 0.26, FGD6 0.20, NDUFA12 0.06; 36
colocalisations with other GWAS in a listing that names no study type (q848): coronary disease (e.g. GCST005194,
H4 0.95, q857, q858), platelet counts, angina, pulse pressure. That listing returns GWAS only; the QTL types,
queried by name, are a later reading (q859-q868). The other sets, led by other variants with the lead
at a posterior of 0.006 to 0.06, phased by the set leads' minor alleles (about 0.07, q849-q856) riding with G
(db-ensembl-116#q527-q536): G lowers coronary artery disease (GCST005195, rs4762479 T β −0.0081, P 2.5e-10; q834,
q835), myocardial infarction (rs11107896 A β −0.091, P 2.3e-12; q836, q837) and angina (rs141526980 TGA β −0.088, P
6.5e-13; q838, q839), and raises platelet count (rs10859847 G β +0.044, P 3.8e-16; q840, q841) and white-cell count
(rs11107900 T β +0.010, P 7.6e-11; q842, q843). Two adipose sets for ENSG00000028203, VEZT (q844, q845), are not
colocalised with the Timmers set. For row 70.

## Reading 2026-11-12, supplement

> [q859] data.credibleSet.colocalisation count 18

> [q860] data.credibleSet.colocalisation.rows[0] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9414616949407358 clpp 0.014300823113747797 betaRatioSignAverage 0

> [q861] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study id gtex-v10_ge_adipose_subcutaneous_ensg00000180263 traitFromSource ENSG00000180263 studyType eqtl

> [q862] data.credibleSet.colocalisation.rows[4] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.945488131345599 clpp 0.015535540383610777 betaRatioSignAverage 0

> [q863] data.credibleSet.colocalisation.rows[4].otherStudyLocus.study id gtex-v10_ge_artery_aorta_ensg00000180263 traitFromSource ENSG00000180263 studyType eqtl

> [q864] data.credibleSet.colocalisation.rows[2] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.9475215954755791 clpp 0.016854787900315388 betaRatioSignAverage 0

> [q865] data.credibleSet.colocalisation.rows[2].otherStudyLocus.study id gtex-v10_ge_fibroblast_ensg00000028203 traitFromSource ENSG00000028203 studyType eqtl

> [q866] data.credibleSet.colocalisation.rows[2].otherStudyLocus.study.target approvedSymbol VEZT

> [q867] data.credibleSet.colocalisation.rows[11] colocalisationMethod COLOC_PIP_ECAVIAR h4 0.929982093342927 clpp 0.011834526321304713 betaRatioSignAverage 0

> [q868] data.credibleSet.colocalisation.rows[11].otherStudyLocus.study.target approvedSymbol NDUFA12

> [q869] data.cs.colocalisation.rows[1] h4 0.9704183181920868 clpp 0.0286918036640765 colocalisationMethod COLOC_PIP_ECAVIAR rightStudyType gwas

> [q870] data.cs.colocalisation.rows[1].otherStudyLocus.study id GCST90476296 traitFromSource platelet count (maximum, inv-norm transformed) studyType gwas

Timmers 2020's set at FGD6 (3dd6e379…), queried with the QTL types named (the query of row 20): 18 QTL
colocalisations (q859), 13 at H4 ≥ 0.8. FGD6 holds 8 (expression in subcutaneous adipose, H4 0.94, q860, q861; aorta,
0.95, q862, q863; fibroblasts, lung and arterial exons), VEZT 4 (fibroblast expression, 0.95, q864-q866; three
adipose transcript and exon sets), NDUFA12 1 (a monocyte transcript, 0.93, q867, q868). The colocalisation sign field
is 0 throughout, so no direction is read. The GWAS-only listing of the same set (q848) has 36 rows; its platelet
colocalisation at H4 0.97 is GCST90476296, the maximum platelet count (q869, q870). For row 70.

## Reading 2026-11-12, supplement

> [q871] data variant null

> [q872] data.credibleSets count 1

> [q873] data.credibleSets.rows[0].variant id 7_22728408_A_G

Open Targets 26.09 has no record for rs2440012 (13_18865983_C_G, q871), and Zeng's study GCST003425 holds one
credible set, IL6's (q872, q873): none at ANKRD20A9P. No causal or effector level can be read. For row 72.

## Reading 2026-11-12, record

> [q874] data.variant.credibleSets count 1

> [q875] data.variant.credibleSets.rows[0] studyLocusId 359bfd7d6e7151cb2172ee4d61040301 pValueMantissa 2.196429967880249 pValueExponent -7 beta -0.549065

> [q876] data.variant.credibleSets.rows[0].study id OTAR2057_IBDverse_ge_Colon_ileum_Enterochromaffin_TPH1_CES1+_ENSG00000133116 traitFromSource ENSG00000133116 studyType sceqtl

> [q877] data.variant.credibleSets.rows[0].locus.rows[0] posteriorProbability 0.012101984836731734

> [q878] data.credibleSets count 0

13_33054001_T_G (rs9536314, row 73): one credible set holds it (q874), a single-cell eQTL for KL
(ENSG00000133116) in ileal enterochromaffin cells (q876), led by 13_33083565_A_C (q875), where KL-VS's posterior
probability is 0.012 (q877). No set of the nine longevity studies (Timmers 2019 and 2020, Deelen 2019, Zeng 2016 and
the rest of the list) holds it (q878). No longevity or disease fine-mapping places KL-VS. For row 73.

## Reading 2026-11-12, record

> [q879] data.variant.credibleSets count 3

> [q880] data.variant.credibleSets.rows[0].study id GCST90569461 traitFromSource Gut microbial network clusters (Salmon (at 1 year) x Any Breastfeeding (Duration) interaction studyType gwas

> [q881] data.variant.credibleSets.rows[1].study id GCST90094707 traitFromSource Black olive liking studyType gwas

> [q882] data.credibleSets count 0

13_64262356_T_C (rs61949650, row 74): three credible sets hold it (q879), two gut-microbial network clusters by
breastfeeding interaction (q880 and the third) and black olive liking (q881), none a disease or lifespan trait. No set
of the nine longevity studies holds it (q882), and Pilling's mothers' study (GCST006696) has no set here. No gene can
be named from fine-mapping. For row 74.

## Reading 2026-11-12, record

> [q883] data.variant.credibleSets.rows[0] studyLocusId f48ec086ca0759283f3639f69ce7b7f4 pValueMantissa 4.863107681274414 pValueExponent -6 beta 0.0067361257223389395 finemappingMethod SuSiE-inf confidence SuSiE fine-mapped credible set with out-of-sample LD

> [q884] data.variant.credibleSets.rows[0].locus.rows[0] posteriorProbability 0.07034168895832833

> [q885] data.variant.credibleSets.rows[1] studyLocusId e41c91dd508237f5894d4c0ec3c222ed pValueMantissa 4.503342151641846 pValueExponent -9 beta -0.008998080089636729 finemappingMethod SuSiE-inf confidence SuSiE fine-mapped credible set with out-of-sample LD

> [q886] data.variant.credibleSets.rows[1].locus.rows[0] posteriorProbability 0.5351966339430967

> [q887] data.variant.credibleSets.rows[0] studyLocusId 5c4802611db885c6019fcf286a2f038c pValueMantissa 6.60985803604126 pValueExponent -11 beta -0.013903108478312146 finemappingMethod SuSiE-inf confidence SuSiE fine-mapped credible set with out-of-sample LD

> [q888] data.variant.credibleSets.rows[0].study id GCST90551886 traitFromSource Lifespan studyType gwas

> [q889] data.variant.credibleSets.rows[0].qualityControls[1] Study locus finemapped without in-sample LD reference

> [q890] data.credibleSets count 0

Row 75. The seed's two rsIDs sit in different Open Targets sets of Park's deposits. 13_73649403_C_CTT (rs35257605)
is in one set of the whole cohort (GCST90551884), P 4.9e-6, PIP 0.070 (q883, q884): a sub-genome-wide set.
13_73757854_G_T (rs116257533) is in the whole cohort's set at P 4.5e-9, PIP 0.54 (q885, q886), and in the second sex
scan's (GCST90551886, the women by row 44's subtraction) at P 6.6e-11, PIP 0.59 (q887, q888). Every set is SuSiE-inf
with out-of-sample LD, its study QC-flagged and fine-mapped without an in-sample LD reference (q889). None of the
nine longevity studies holds either variant (q890, and the same for 13_73757854_G_T). For row 75.

## Reading 2026-11-13, record

> [q891] data.variant.credibleSets count 102

> [q892] data.credibleSets count 0

14_74855011_T_C (rs61978928, row 76): 102 credible sets hold it (q891), among them alanine and glutamine levels,
neuroticism and mood swings, monocyte and platelet counts, lung function and molecular QTLs for nearby genes, the lead's
posterior probability small in those read (0.005 to 0.03): a busy region, where it leads none of the sets read. No set
of the nine longevity studies holds it (q892). For row 76.

## Reading 2026-11-13, record

> [q893] data.variant.credibleSets.rows[0] studyLocusId 8861fe5a08727499d4db839b592501a0 pValueMantissa 1 pValueExponent -8 beta 5.7181206 finemappingMethod PICS

> [q894] data.variant.credibleSets.rows[0].locus.rows[0] posteriorProbability 1

> [q895] data.variant.credibleSets.rows[0].l2GPredictions.rows[0] score 0.4187757670879364

15_29030729_A_G (rs77184423, row 77): one credible set holds it, Gurinovich's PICS set (q893, P 1e-8), the lead
alone at posterior probability 1 (q894); locus-to-gene gives APBA2 0.42 (q895), GOLGA6L7 0.20. For row 77.

## Reading 2026-11-13, record

> [q896] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.002669717772692601

> [q897] data.variant.alleleFrequencies[9] populationName afr_adj alleleFrequency 0.18072326269098077

> [q898] data.variant.alleleFrequencies[6] populationName asj_adj alleleFrequency 0.0007686395080707148

Open Targets' gnomAD frequencies for 15_29030729_A_G (rs77184423, row 77): G 0.0027 in non-Finnish Europeans (q896),
0.18 in Africans (q897), 0.0008 in Ashkenazi Jews (q898). gnomAD sides with NECS's controls (0.0045) and Park's UK
Biobank (about 0.0008), against 1000 Genomes' Europeans (0.115) and ALFA's (0.064): the references disagree. For row 77.

## Reading 2026-11-13, record

> [q899] data.variant.credibleSets count 143

> [q900] data.variant.credibleSets.rows[26] studyLocusId 27c48045b34bcdc3da2f0f934d13586f pValueMantissa 1.0119999647140503 pValueExponent -9 beta 0.0369 finemappingMethod PICS

> [q901] data.variant.credibleSets.rows[26].study id GCST90018988 traitFromSource Medication use (agents acting on the renin-angiotensin system) studyType gwas

> [q902] data.variant.credibleSets.rows[26].locus.rows[0] posteriorProbability 0.0335034507688656

> [q903] data.variant.credibleSets.rows[14] studyLocusId 161050e7b38c034352dba93e1e4b38d4 pValueMantissa 4.359246253967285 pValueExponent -9 beta 0.008007924518550385 finemappingMethod SuSiE-inf

> [q904] data.variant.credibleSets.rows[14].variant id 15_41151726_A_G

> [q905] data.variant.credibleSets.rows[14].study id GCST90693007 traitFromSource Coronary atherosclerosis (PheCode 411.4) studyType gwas

> [q906] data.credibleSets count 0

15_41138771_T_A (rs28455998, row 78): 143 credible sets hold it (q899), 136 of GWAS, none of a lifespan, longevity,
frailty or ageing study (the nine longevity studies, q906: none; no trait of the 143 names ageing, frailty, survival
or lifespan). It leads one: GCST90018988's renin-angiotensin medication use (PICS, P 1e-9, alt A β +0.0369, q900, q901),
at posterior 0.034 (q902). Elsewhere it sits at 0.03 or less, in sets led by other variants, mostly blood pressure and
hypertension, also coronary disease, eGFR and creatinine, height, red-cell counts, brain white-matter imaging,
menopause and lung function. Atkins' rs3959554 (15_41151726_A_G) leads coronary atherosclerosis sets, G raising it
(β +0.0080, P 4.4e-9, q903 to q905). For row 78.

## Reading 2026-11-13, record

> [q907] data.variant.credibleSets count 2

> [q908] data.credibleSets count 0

> [q909] data.credibleSets count 0

15_47367997_G_A (rs74011415, row 79): two credible sets hold it (q907), each led by another variant with the lead at
posterior 0.005 or less: UK Biobank's age at completing education and FinnGen R12's ever-smoking (locus-to-gene SEMA6D
0.87 and 0.47 there). None of Pilling's five deposits (q908) nor the nine longevity studies (q909) has a set here. For
row 79.

## Reading 2026-11-13, record

> [q910] data.variant.credibleSets count 38

> [q911] data.variant.credibleSets.rows[33] studyLocusId f01a4deb921bfbb94532a95c6be245e0 pValueMantissa 1 pValueExponent -8 beta null finemappingMethod PICS

> [q912] data.variant.credibleSets.rows[33].study id GCST011100 traitFromSource Aging traits (healthspan, parental lifespan or longevity) (multivariate analysis) studyType gwas

> [q913] data.variant.credibleSets.rows[33].locus.rows[0] posteriorProbability 0.04251940095019988

> [q914] data.variant.credibleSets.rows[33].l2GPredictions.rows[0] score 0.8855655193328857

> [q915] data.credibleSet.colocalisation count 2

> [q916] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study.target approvedSymbol RBL2

> [q917] data.credibleSet.colocalisation.rows[1].otherStudyLocus.study.target approvedSymbol LINC03064

> [q918] data.credibleSet.colocalisation count 45

> [q919] data.credibleSet.colocalisation.rows[7] rightStudyType gwas h4 0.9645214645994986

> [q920] data.credibleSet.colocalisation.rows[7].otherStudyLocus.study id GCST90474606 traitFromSource Body mass index (BMI) (UKB data field 21001) studyType gwas

> [q921] data.variant.credibleSets.rows[9] studyLocusId 345f950946ddc3a331f1ebdba292eb27 pValueMantissa 6.517000198364258 pValueExponent -9 beta 0.0117586 finemappingMethod PICS

> [q922] data.variant.credibleSets.rows[9].study id GCST90474606 traitFromSource Body mass index (BMI) (UKB data field 21001) studyType gwas

16_52537524_A_C (rs4783780, row 82): 38 credible sets hold it (q910). It leads Timmers 2020's multivariate ageing set
(GCST011100, PICS, P 1e-8; q911, q912) at posterior 0.043, the top of 40 members (q913), locus-to-gene TOX3 0.886
(q914). Its QTL colocalisations are two cis eQTLs (q915): an RBL2 transcript in CD16 monocytes (H4 0.97, q916) and
LINC03064 in testis (H4 0.88, q917); none of TOX3. Its GWAS colocalisations, 45 (q918), are mostly body mass and fat
mass (H4 0.83 to 0.97; the lead's own BMI set at 0.96, q919, q920), also brain morphology, systolic pressure, type 2
diabetes (0.90) and cholelithiasis; none of rs4784227's breast-cancer sets (16_52565276_C_T), which lead the locus's
other sets at posteriors up to 1.0; one breast-cancer set of its own (q923 to q926). The lead's own BMI set (q921, q922): PICS, P 6.5e-9, alt C β +0.0118, so A lowers
BMI. For row 82.

## Reading 2026-11-13, record

> [q923] data.credibleSet.colocalisation.rows[36] rightStudyType gwas h4 0.9611826078715578

> [q924] data.credibleSet.colocalisation.rows[36].otherStudyLocus.study id GCST90429846 traitFromSource Breast cancer studyType gwas

> [q925] data.credibleSets.rows[0] studyLocusId 62c06ce518f6300e8e49ad4d0e64ff76 pValueMantissa 1.7654715776443481 pValueExponent -8 beta 0.11218163546316709 finemappingMethod SuSiE-inf

> [q926] data.credibleSets.rows[0].variant id 16_52537621_A_G

Row 82. Timmers 2020's set at rs4783780 colocalises with a breast-cancer set (GCST90429846, H4 0.96; q923, q924), led
by 16_52537621_A_G (rs3112581, db-ensembl-116#q625), SuSiE-inf, P 1.8e-8, alt G β +0.112 (q925, q926): G raises
breast cancer. G rides with the lead's C (db-ensembl-116#q626, q627). For row 82.

## Reading 2026-11-13, record

> [q927] data.variant.credibleSets count 1701

> [q928] data.credibleSets count 0

> [q929] data.variant.credibleSets.rows[73] studyLocusId 0b0f2f6002fe711db38d050f5bcd3fe7 pValueMantissa 2.4000000953674316 pValueExponent -277 beta 0.1195 finemappingMethod PICS

> [q930] data.variant.credibleSets.rows[73].study id GCST90479523 traitFromSource Body mass index (BMI, minimum, inv-normal transformed) studyType gwas

> [q931] data.variant.credibleSets.rows[73].locus.rows[0] posteriorProbability 0.8496191016524004

> [q932] data.variant.credibleSets.rows[123] studyLocusId 13e3b3e7e5cedc8a9514b476ea341f3c pValueMantissa 1.5499999523162842 pValueExponent -97 beta 0.11440126030997533 finemappingMethod PICS

> [q933] data.variant.credibleSets.rows[123].study id GCST90479892 traitFromSource Diabetes mellitus (PheCode 250) studyType gwas

> [q934] data.variant.credibleSets.rows[94] studyLocusId 0ef265c01c2d113ee98b805e9c705832 pValueMantissa 3.5899999141693115 pValueExponent -16 beta 0.04562517802627547 finemappingMethod PICS

> [q935] data.variant.credibleSets.rows[94].study id GCST90480134 traitFromSource Ischemic heart disease (PheCode 411) studyType gwas

> [q936] data.variant.credibleSets.rows[84] studyLocusId 0df6f38bbdd60c179774f54f569fa9a9 pValueMantissa 9.784317016601562 pValueExponent -43 beta -0.02129108981906212 finemappingMethod SuSiE-inf

> [q937] data.variant.credibleSets.rows[84].study id GCST90475416 traitFromSource low density lipoprotein cholesterol (LDLC, mean, inv-norm transformed) studyType gwas

16_53767042_T_C (rs1421085, row 83): 1,701 credible sets hold it (q927), none of the eleven longevity studies queried
(q928). Of the first 200 returned, it leads 46, among them BMI (PICS, P 2.4e-277, alt C β +0.12, posterior 0.85; q929
to q931), diabetes mellitus (C +0.114, P 1.5e-97, posterior 0.46; q932, q933), ischaemic heart disease (C +0.046, P
3.6e-16, posterior 0.06; q934, q935) and LDL cholesterol (C −0.021 on the inverse-normal scale, P 9.8e-43, posterior
0.09; q936, q937); also waist and hip, body composition, HbA1c, glucose, CRP, blood pressure and heart failure, C on
the higher side. So T goes with lower weight, less diabetes and heart disease, and slightly higher LDL. For row 83.

## Reading 2026-11-13, record

> [q938] data.variant.credibleSets.rows[57] studyLocusId 62e2ea7362adca771080be57eae5b1f7 pValueMantissa 2.117220878601074 pValueExponent -15 beta -0.02028992001349487 finemappingMethod SuSiE-inf

> [q939] data.variant.credibleSets.rows[57].study id GCST90454345 traitFromSource Breast cancer (luminal A) studyType gwas

> [q940] data.variant.credibleSets.rows[1] studyLocusId 794e210b5cf207b0f473efd18d731ea1 pValueMantissa 3.0280001163482666 pValueExponent -12 beta -0.0216958 finemappingMethod PICS

> [q941] data.variant.credibleSets.rows[1].study id GCST90500022 traitFromSource Total cholesterol levels studyType gwas

All 1,701 of rs1421085's credible sets read (nine pages), row 83: the lead tops 380. Among them about 40 lipid sets
(LDL, total cholesterol, IDL and very-small-VLDL fractions) in which C, the higher-BMI allele, lowers the lipid, e.g.
total cholesterol C −0.022, P 3.0e-12 (q940, q941), as LDL (q936, q937); and a breast-cancer set (luminal A,
GCST90454345, SuSiE-inf, P 2.1e-15) with C −0.020 (q938, q939): C lowers it, so T, the longer-lived allele, raises
breast cancer and LDL. Of 21 body-weight sets it tops, two run against the rest (UK Biobank weight, weight-to-muscle
ratio); a bone-density set prints no β. For row 83.

## Reading 2026-11-13, record

> [q942] data.variant.credibleSets count 1707

> [q943] data.credibleSets count 0

> [q944] data.variant.credibleSets.rows[116] studyLocusId 2f47e6b07bdfacbf3c5fca4f5049a3dc pValueMantissa 9.88131332397461 pValueExponent -323 beta 0.15793175706664966 finemappingMethod SuSiE-inf

> [q945] data.variant.credibleSets.rows[116].study id GCST90269503 traitFromSource HDL cholesterol levels (UKB data field 23406) studyType gwas

> [q946] data.variant.credibleSets.rows[116].locus.rows[0] posteriorProbability 0.9579272751503588

> [q947] data.variant.credibleSets.rows[57] studyLocusId 42aa19e9531cf6cf12dd6bdfb274f8f3 pValueMantissa 7 pValueExponent -9 beta 0.13976194237515863 finemappingMethod PICS

> [q948] data.variant.credibleSets.rows[57].study id GCST001100 traitFromSource Age-related macular degeneration studyType gwas

16_56959412_C_A (rs3764261, row 84): 1,707 credible sets hold it (q942), none of the eleven longevity studies queried
(q943); read over all nine pages, it tops 434, almost all lipid: HDL cholesterol in UK Biobank (SuSiE-inf, P 1e-322,
alt A β +0.158, posterior 0.96; q944 to q946), A raising HDL in every HDL-cholesterol-level set it tops, with the HDL
particle fractions up and VLDL and LDL fractions down. One disease set: age-related macular degeneration (GCST001100,
PICS, P 7e-9, A β +0.140; q947, q948): A, the longer-lived allele, raises it. No coronary set with a β is topped by
the lead. For row 84.

## Reading 2026-11-13, record

> [q949] data.variant.credibleSets.rows[172] studyLocusId 7372a87f9c3204045d3643fc81eb3782 pValueMantissa 7.96999979019165 pValueExponent -12 beta 0.09728212280655374 finemappingMethod PICS

> [q950] data.variant.credibleSets.rows[172].study id GCST90480048 traitFromSource Macular degeneration (senile) of retina NOS (PheCode 362.29) studyType gwas

> [q951] data.variant.credibleSets.rows[166] studyLocusId 92542fc5b3ac400e59313e1076f16659 pValueMantissa 7 pValueExponent -9 beta -0.034744173 finemappingMethod PICS

> [q952] data.variant.credibleSets.rows[166].study id GCST007931 traitFromSource Medication use (HMG CoA reductase inhibitors) studyType gwas

rs3764261, row 84, over all nine pages. Of the 434 sets the lead tops, 408 are lipid, fatty-acid or lipoprotein
traits; the other 26 are proteins (APOA1, APOC1 and others), vitamin D, metabolic syndrome (Kristiansson's, A +0.07,
on a scale the record does not name), statin use (A −0.035, P 7e-9, q951, q952), waist and a coronary-or-factor-VII
pleiotropy set with no β, and two macular-degeneration sets, both with A raising it: GCST001100 (q947, q948) and UK
Biobank's senile macular degeneration (PICS, P 8.0e-12, A β +0.097; q949, q950). Every macular-degeneration set at the
locus, whoever leads it, has its alt allele raising it. One HDL set runs against the rest: GCST009661 "Low
HDL-cholesterol levels", A +0.59 (a case-control set, its scale unnamed). For row 84.

## Reading 2026-11-13, record

> [q953] data.credibleSets.rows[0] studyLocusId fa1d4b7abd7e1a3b83d334570d408c87 finemappingMethod PICS pValueMantissa 1 pValueExponent -8

> [q954] data.credibleSets.rows[0].locus.rows[0] posteriorProbability 0.24263312943077164

> [q955] data.credibleSets.rows[0].l2GPredictions.rows[0] score 0.9654757976531982

> [q956] data.credibleSets.rows[0].l2GPredictions.rows[1] score 0.7052884697914124

> [q957] data.credibleSet.locus count 7

> [q958] data.credibleSet.colocalisation count 154

> [q959] data.variant.credibleSets count 945

16_72041694_A_T (rs12924886, row 85). Timmers 2019's parental-lifespan set (GCST009890, PICS, P 1e-8; q953), the
lead at posterior 0.243 (q954), the top of 7 members (q957); locus-to-gene HP 0.965 and HPR 0.705 (q955, q956). Its
QTL colocalisations, 154 (q958): of the cis ones at H4 ≥ 0.8, HP 58, HPR 55, TXNL4B 21, DHODH 9 (counted from the
listing). The lead is in 945 sets (q959) and tops 21, 14 of them lipid: alt T raises LDL, non-HDL cholesterol,
apolipoprotein B, triglycerides and mixed hyperlipidaemia (e.g. LDL β +0.025, P 2e-117), so A lowers them; the rest are
GALNT2 and plasma glycans, albumin, two eQTLs and Timmers' own set. No disease set is topped by the lead. For row 85.

## Reading 2026-11-13, record

> [q960] data.variant.credibleSets.rows[195] studyLocusId 6bca38782038a5874c10522b32f4124f pValueMantissa 2.161113977432251 pValueExponent -117 beta 0.025483377380416963 finemappingMethod SuSiE-inf

> [q961] data.variant.credibleSets.rows[195].study id GCST90019512 traitFromSource Low density lipoprotein cholesterol levels studyType gwas

rs12924886, row 85: the LDL-cholesterol set it tops (GCST90019512; q960, q961), alt T β +0.0255, P 2.2e-117: A lowers
LDL. For row 85.

## Reading 2026-11-13, record

> [q962] data.variant.credibleSets.rows[44] studyLocusId 45a189a11b74e29c1fe99a1eb20821d3 pValueMantissa 1.2970000505447388 pValueExponent -14 beta 0.04023775 finemappingMethod PICS

> [q963] data.variant.credibleSets.rows[44].variant id 16_72067626_C_G

> [q964] data.variant.credibleSets.rows[44].locus.rows[0] posteriorProbability 0.13235586485841558

> [q965] data.variant.rsIds[0] rs34042070

> [q966] data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.19903498190591074

> [q967] data.variant.rsIds[0] rs7187129

rs12924886, row 85. A coronary-artery-disease set holding the lead (GCST90132315, q962), led by 16_72067626_C_G
(q963), rs34042070 (q965), alt G β +0.040, P 1.3e-14, the lead at posterior 0.13 (q964). G is 0.199 in gnomAD's
non-Finnish Europeans (q966), the lead's T 0.193 (db-ensembl-116#q642), r² 0.96 (CEU) and 1.00 (GBR)
(db-ensembl-116#q645): G rides with T, so T raises coronary disease and A, the longer-lived allele, lowers it. Foote's
factor 3 set at 16q22 (db-opentargets-26.09, foote7 listing, P 1.7e-10) is led by 16_71827541_T_C, rs7187129 (q967),
214 kb from the lead. For row 85.

## Reading 2026-11-13, record

> [q968] data.variant.credibleSets.rows[105] studyLocusId 0e059c4548bde15553a0ee98505b3aa3 pValueMantissa 1 pValueExponent -149 beta null finemappingMethod PICS

> [q969] data.variant.credibleSets.rows[105].variant id 16_56956804_C_A

> [q970] data.variant.credibleSets.rows[105].study id GCST004045 traitFromSource Age-related diseases, mortality and associated endophenotypes studyType gwas

> [q971] data.variant.credibleSets.rows[105].locus.rows[0] posteriorProbability 0.07987396605649862

rs3764261, row 84: the one ageing-named set at CETP in all 1,707, GCST004045 "Age-related diseases, mortality and
associated endophenotypes" (q970; PICS, P 1e-149, no β, q968), led by 16_56956804_C_A (q969), the lead at posterior
0.08 (q971). Its study (db-gwascatalog-2026.10.29#q501): 9,618 European individuals, He 2016's pleiotropic analysis, whose
endophenotypes include lipids (pmid-27790247#q1), so at CETP it reads as the lipid signal. For row 84.

## Reading 2026-11-13, record

> [q972] data.variant.credibleSets.rows[31] studyLocusId 9b4a8900ab048fd09fd8005c8d40940f pValueMantissa 1.9739999771118164 pValueExponent -17 beta 0.0145988158018329 finemappingMethod PICS

> [q973] data.variant.credibleSets.rows[31].variant id 16_53768582_C_T

> [q974] data.variant.credibleSets.rows[31].study id GCST90624049 traitFromSource Frailty (Factor 3 - Multimorbidity) studyType gwas

> [q975] data.variant.credibleSets.rows[100].study id GCST90624052 traitFromSource Frailty (Factor 6 - Disability) studyType gwas

> [q976] data.variant.rsIds[0] rs11642015

rs1421085, row 83: two of its 1,701 sets are Foote's frailty factors, factor 3 (GCST90624049; PICS, P 2.0e-17; q972,
q974) and factor 6 (GCST90624052, P 3.0e-14; q975), both led by 16_53768582_C_T (q973), rs11642015 (q976), the lead
at posterior 0.039 and 0.034. Also a set of GCST004045 (age-related diseases, mortality and endophenotypes, 9,618
people; db-gwascatalog-2026.10.29#q501) led by another variant, the lead at posterior 0.009. For row 83.

## Reading 2026-11-13, record

> [q977] data.credibleSet.locus count 70

> [q978] data.credibleSet.l2GPredictions.rows[0] score 0.9860568046569824

> [q979] data.credibleSet.colocalisation count 2

Foote's factor 3 set at FTO (9b4a8900…), row 83: 70 members (q977), the lead rs1421085 at posterior 0.039
(q972's set); locus-to-gene FTO 0.986 (q978; RPGRIP1L 0.20 next); its two QTL colocalisations (q979) are trans pQTLs
(LEP, OBP2B), no cis one. For row 83.

## Reading 2026-11-13, record

> [q980] data.variant.credibleSets count 21

> [q981] data.credibleSets count 2

> [q982] data.credibleSets.rows[0] studyLocusId 27cc69b923af74dfbbe5b7bea000dc48 finemappingMethod SuSiE-inf pValueMantissa 3.9535210132598877 pValueExponent -13

> [q983] data.credibleSets.rows[0].study id GCST007406 traitFromSource Healthspan

> [q984] data.credibleSets.rows[0].locus.rows[0] posteriorProbability 0.37889356919904565

> [q985] data.credibleSets.rows[0].l2GPredictions.rows[0].target approvedSymbol DEF8

> [q986] data.credibleSets.rows[0].l2GPredictions.rows[0] score 0.8956615924835205

> [q987] data.credibleSets.rows[1] studyLocusId 399ed49d2e486524d35c9bad87d24b05 finemappingMethod PICS pValueMantissa 7 pValueExponent -12

> [q988] data.credibleSets.rows[1].locus.rows[0] posteriorProbability 0.8172746981464537

> [q989] data.credibleSet.locus count 4

> [q990] data.credibleSet.colocalisation count 6

> [q991] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study.target approvedSymbol RPL13

> [q992] data.credibleSet.colocalisation.rows[1].otherStudyLocus.study.target approvedSymbol DEF8

> [q993] data.credibleSet.colocalisation.rows[2].otherStudyLocus.study.target approvedSymbol DEF8

> [q994] data.credibleSet.colocalisation.rows[3].otherStudyLocus.study.target approvedSymbol SPG7

> [q995] data.credibleSet.colocalisation.rows[4].otherStudyLocus.study.target approvedSymbol DEF8

> [q996] data.credibleSet.colocalisation.rows[5].otherStudyLocus.study.target approvedSymbol DEF8

16_89960104_T_C (rs4268748, row 86). The lead is in 21 sets (q980), every one paged; of the eleven longevity studies
and Foote 2025's seven deposits two hold it (q981): Zenin's healthspan (GCST007406, SuSiE-inf, P 4e-13; q982, q983),
the lead at posterior 0.379 (q984), the top of 4 members (q989), locus-to-gene DEF8 0.896 (q985, q986); and Timmers
2020's multivariate set (GCST011100, PICS, P 7e-12; q987), the lead at 0.817 (q988), named, not counted (D25.5). The
healthspan set's QTL colocalisations, 6 (q990), all cis and at H4 ≥ 0.99: DEF8 4 (an exon eQTL in monocytes, a
fibroblast transcript and two fibroblast splicing QTLs), RPL13 1 (a cartilage transcript-usage QTL) and SPG7 1 (a
neuron transcript) (q991 to q996). The other 19 sets are skin traits (squamous cell carcinoma, actinic keratosis,
melanoma, seborrhoeic keratosis, benign skin neoplasm, sebaceous cyst, skin colour, skin ageing), vitiligo (alt C β
−0.35, so T raises it), age at first sex, number of children, a plasma metabolite and a DEF8 eQTL. For row 86.

## Reading 2026-11-13, record

> [q997] data.variant.credibleSets.rows[0] studyLocusId fbc1463eb33ab77768dc91a950f8587a pValueMantissa 5 pValueExponent -10 beta -0.014460757 finemappingMethod PICS

> [q998] data.variant.credibleSets.rows[0].study id GCST90321079 traitFromSource Aging studyType gwas

> [q999] data.variant.credibleSets.rows[0].locus.rows[0] posteriorProbability 0.8631273558437729

> [q1000] data.credibleSet.l2GPredictions.rows[0] score 0.7762042880058289

> [q1001] data.credibleSet.locus.rows[1] posteriorProbability 0.08293424571731994

> [q1002] data.credibleSet.colocalisation count 0

rs34891485 (row 87, variant 17_42111440_T_C): one credible set holds it, Rosoff 2023's mvAge (GCST90321079, q997,
q998), PICS, P 5e-10, β −0.0145 for C (T +0.0145), the lead at posterior 0.863 (q999), three variants in all, the
next rs78862468 at 0.083 (q1001). Locus-to-gene names one gene, DHX58, 0.776 (q1000); no QTL colocalisation (q1002).
For row 87.

## Reading 2026-11-13, record

> [q1003] data.variant.credibleSets count 66

> [q1004] data.variant.credibleSets.rows[18] studyLocusId 57327b4dfde0ffa125bd8352a8fff373 pValueMantissa 7.566999912261963 pValueExponent -21 beta -0.0215907 finemappingMethod PICS

> [q1005] data.variant.credibleSets.rows[18].study id GCST90302889 traitFromSource Body mass index studyType gwas

> [q1006] data.variant.credibleSets.rows[18].variant id 17_49063432_C_T

> [q1007] data.variant.credibleSets.rows[18].locus.rows[0] posteriorProbability 0.02716207440542874

> [q1008] data.variant.credibleSets.rows[4] studyLocusId 0b92b4b46cc85dd41d1a611d934028d7 pValueMantissa 1.2100000381469727 pValueExponent -10 beta -0.0253 finemappingMethod PICS

> [q1009] data.variant.credibleSets.rows[4].study id GCST90455657 traitFromSource Heart failure studyType gwas

> [q1010] data.variant.credibleSets.rows[16] studyLocusId 4d33b61434a047f93129e8f69289a3fc pValueMantissa 1.2799999713897705 pValueExponent -12 beta -0.040181789632831706 finemappingMethod PICS

> [q1011] data.variant.credibleSets.rows[16].study id GCST90480134 traitFromSource Ischemic heart disease (PheCode 411) studyType gwas

rs940088 (row 88, 17_49068486_T_C): 66 credible sets hold it (q1003), the lead topping none, its posterior at most 0.04
in any; none of a lifespan-class study, and no mvAge set. They are adiposity (BMI, waist, fat mass, visceral fat),
glycaemia and type 2 diabetes, coronary and ischaemic heart disease, heart failure, C-reactive protein, blood
pressure, insomnia, walking pace, intelligence and brain volumes. Seventeen are led by rs11655587 (17_49063432_C_T, r²
0.84 to the lead, its T riding with the lead's C, db-ensembl-116#q667): BMI, T −0.0216, P 7.6e-21, the lead at posterior
0.027 (q1004-q1007); heart failure, T −0.0253, P 1.2e-10 (q1008, q1009); ischaemic heart disease, T −0.040, P 1.3e-12
(q1010, q1011). So the lead's C goes with lower BMI and less heart disease. Locus-to-gene names IGF2BP1 in nearly all
(0.48 to 0.72), B4GALNT2 below 0.07. For row 88.

## Reading 2026-11-13, record

> [q1012] data.variant.credibleSets.rows[61] studyLocusId f5cb07efa96dfe126e7228c5fc6c8b2a pValueMantissa 2.260999917984009 pValueExponent -9 beta -0.06528333177349593 finemappingMethod PICS

> [q1013] data.variant.credibleSets.rows[61].study id GCST90668071 traitFromSource T2D (Phecode: 250.2) studyType gwas

> [q1014] data.variant.credibleSets.rows[21] studyLocusId 5f63d48aaee3368bcab80459b58274cf pValueMantissa 2.759999990463257 pValueExponent -9 beta -0.048790164169432056 finemappingMethod PICS

> [q1015] data.variant.credibleSets.rows[21].study id GCST90479543 traitFromSource Coronary artery / coronary heart disease (including heart attack, angina) studyType gwas

> [q1016] data.variant.credibleSets.rows[28] studyLocusId 844889cae8378689e9feadb0106b2f9d pValueMantissa 1.3580000400543213 pValueExponent -9 beta 0.020074740338067 finemappingMethod SuSie

> [q1017] data.variant.credibleSets.rows[28].study id FINNGEN_R12_FG_CVD traitFromSource Cardiovascular diseases (excluding rheumatic etc) studyType gwas

Row 88, the other set leads phased against rs940088 in CEU (1000 Genomes genotype records, `genotypes-*.json`;
haplotype counts derived): the lead's C rides with the alt allele of 17_49014058_C_T (rs9906944; 63 of 69 C
haplotypes), 17_49017679_G_A (rs11079852; 68), 17_49013423_C_T (rs11079849; 62), 17_49046061_T_C (rs4643373; 62),
17_49058513_G_A (rs68085814; 62), 17_49034385_T_C (rs144170248; 68) and 17_49016036_T_C (rs4794018; 68), as with
17_49063432_C_T (rs11655587; 69, q1004-q1011). Every disease or risk-factor β of those leads' sets is negative for
the alt allele: type 2 diabetes (rs9906944's T, −0.065, P 2.3e-9, q1012, q1013), coronary disease (rs11079849's T,
−0.049, P 2.8e-9, q1014, q1015), HbA1c, diabetic retinopathy, kidney failure, peripheral vascular disease, angina,
C-reactive protein, systolic blood pressure, insomnia, fat mass and waist; intelligence, walking pace and brain
volumes positive. So C, the healthier allele, sits on the less-disease side of each. One set runs the other way:
FinnGen R12's cardiovascular diseases, led by rs35929648 (17_48925181_A_G, 143 kb away), G +0.020, P 1.4e-9 (q1016,
q1017), L2G SNF8 and UBE2Z; G rides with C on 20 of 69 C haplotypes against 14 of 129 T haplotypes, r² about 0.05
(derived), the lead's posterior there 0.0009: a separate signal, named. rs9912906 (17_49027070_A_T, an HbA1c set)
has no genotype record Ensembl returns, so it is unphased. For row 88.

## Reading 2026-11-13, record

> [q1018] data.credibleSets.rows[1] studyLocusId e95e1989ec0d8799c17be4b6f837c2f1 pValueMantissa 1 pValueExponent -10 beta -0.2507 finemappingMethod PICS

> [q1019] data.credibleSets.rows[1].study id GCST009890 traitFromSource Parental lifespan

> [q1020] data.credibleSet.colocalisation count 172

> [q1021] data.credibleSet.colocalisation.rows[72] h4 0.9962746412955811 clpp 0.19973039274001583 betaRatioSignAverage -1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1022] data.credibleSet.colocalisation.rows[72].otherStudyLocus studyLocusId e2873de2f6b21c91287cb4cf7056e64d beta 0.04919270135702459 pValueMantissa 6.5159759521484375 pValueExponent -7

> [q1023] data.credibleSet.colocalisation.rows[72].otherStudyLocus.study id GCST90335164 traitFromSource Diastolic blood pressure (BMI unadjusted)

> [q1024] data.credibleSet.colocalisation.rows[147] h4 0.9927650488707778 clpp 0.1153920673041969 betaRatioSignAverage -1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1025] data.credibleSet.colocalisation.rows[147].otherStudyLocus.study id GCST90132314 traitFromSource Coronary artery disease

> [q1026] data.credibleSet.colocalisation.rows[130] h4 0.9928587892685564 clpp 0.11366000679130708 betaRatioSignAverage 1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1027] data.credibleSet.colocalisation.rows[130].otherStudyLocus studyLocusId 7015e215653ffb056cfeae06168d1e6e beta -0.00912999196619885 pValueMantissa 7.8286824226379395 pValueExponent -9

> [q1028] data.credibleSet.colocalisation.rows[130].otherStudyLocus.study id GCST90309345 traitFromSource Respiratory disease (confirmatory factor analysis Factor 11)

> [q1029] data.credibleSet.colocalisation.rows[43] h4 0.9916368711914341 clpp 0.09789427174436614 betaRatioSignAverage 1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1030] data.credibleSet.colocalisation.rows[43].otherStudyLocus.study id FINNGEN_R12_M13_ARTHROSIS_KNEE_PRIM_KNEESURG traitFromSource Gonarthrosis, primary, with knee surgery

> [q1031] data.credibleSet.colocalisation.rows[170] h4 0.9685400753084448 clpp 0.0276152691534785 betaRatioSignAverage 1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1032] data.credibleSet.colocalisation.rows[170].otherStudyLocus.study id GCST90309362 traitFromSource Diabetes (confirmatory factor analysis Factor 28)

Row 81 (rs6224, 15_90880313_G_T): Timmers 2019's parental-lifespan set, PICS, led by rs6224, T −0.2507 years (q1018,
q1019), so G the longer-lived. Its GWAS colocalisations (q1020): 172, 158 at H4 ≥ 0.8. Open Targets' sign column
(betaRatioSignAverage, the other trait's β over the lifespan β) puts G on the good side of blood pressure and
coronary disease: diastolic pressure at rs6224 itself, T +0.049 with sign −1, so G lowers it (q1021-q1023); coronary
artery disease, sign −1, so G lowers it (q1024, q1025); likewise pulse pressure, coronary atherosclerosis, left
ventricular mass, pre-eclampsia and hyperlipidaemia (sign −1). Some sets run against G, sign +1: a respiratory-disease
factor (confirmatory factor 11) at rs6224, T −0.0091, so G raises it on the factor's scale (q1026-q1028); FinnGen's
primary knee osteoarthritis with surgery (q1029, q1030); a diabetes factor (factor 28, q1031, q1032). Many sets carry
sign 0 (no direction): among them suicide attempt, smoking initiation, schizophrenia, opioid use disorder and
myocardial infarction. The spread is broad (lipids, blood cells, liver enzymes, brain morphology, body mass, birth
weight, psychiatric traits). For row 81.

## Reading 2026-11-13, record

> [q1033] data.variant.credibleSets.rows[14] studyLocusId d88600d9ec2827cd3e1d4f261900ebdf pValueMantissa 7.480000019073486 pValueExponent -9 beta -0.03246719013750137 finemappingMethod PICS

> [q1034] data.variant.credibleSets.rows[14].study id GCST90480543 traitFromSource Osteoarthrosis, localized, primary (PheCode 740.11) studyType gwas

> [q1035] data.variant.credibleSets.rows[61] studyLocusId 66f0ec25ca31ea8c6f6695c3e149a198 pValueMantissa 1.1699999570846558 pValueExponent -9 beta -0.028587456851912506 finemappingMethod PICS

> [q1036] data.variant.credibleSets.rows[61].study id GCST90479998 traitFromSource Obstructive sleep apnea (PheCode 327.32) studyType gwas

> [q1037] data.variant.credibleSets.rows[67] studyLocusId ca75f55e8b114efeb1567818e9efcff4 pValueMantissa 1.7039999961853027 pValueExponent -14 beta 0.011542275934448606 finemappingMethod SuSiE-inf

> [q1038] data.variant.credibleSets.rows[67].study id GCST90476116 traitFromSource Nephritis and nephropathy in diseases classified elsewhere (PheCode 580.31) studyType gwas

> [q1039] data.variant.credibleSets.rows[7] studyLocusId 7482a12b5716262320e9c6040e324af3 pValueMantissa 9.128999710083008 pValueExponent -11 beta 0.009473544407515895 finemappingMethod SuSiE-inf

> [q1040] data.variant.credibleSets.rows[7].study id GCST90475996 traitFromSource Peripheral vascular disease studyType gwas

> [q1041] data.variant.credibleSets.rows[3].study id GCST004044 traitFromSource Age-related diseases and mortality studyType gwas

Row 63 (rs35198068, 10_112995025_T_C), the owed sweep: all 845 credible sets read in nine pages of 100
(`variant-10_112995025_T_C.json` and `-p1` to `-p8`). The lead tops 99, all GWAS; the betas are for C, the diabetes
allele. Beyond the first page they add diabetes, HbA1c, glucose and diabetes-medication sets (C raising them), weight,
BMI, fat mass and LDL sets (C lowering them), and four disease sets the row had not named: localized primary
osteoarthrosis, C −0.032, P 7.5e-9, posterior 0.20 (q1033, q1034), and obstructive sleep apnoea, C −0.029, P 1.2e-9,
posterior 0.22 (q1035, q1036), both on T's side, the longer-lived allele, as the weight sets are; nephropathy, C
+0.012, P 1.7e-14, posterior 0.42 (q1037, q1038), and peripheral vascular disease, C +0.0095, P 9.1e-11 (q1039, q1040),
on C's. The longevity-class sets are the ones the row names (Zenin's healthspan, Timmers 2020, mvAge), plus Foote's
metabolic factor led by another variant (posterior 0.057) and He 2016's two age-related-disease sets (GCST004044 and
GCST004045, q1041), led by rs7903146's neighbour 10_112996282_A_T, the lead at posterior 0.05 and 0.03, with no β:
named, not counted (as at row 84). For row 63.

## Reading 2026-11-13, record

> [q1042] data.variant.credibleSets count 113

> [q1043] data.variant.credibleSets.rows[47] studyLocusId 5e3f875ef3531a8b15b58379476c8632 pValueMantissa 3.256999969482422 pValueExponent -115 beta 0.0315268 finemappingMethod PICS

> [q1044] data.variant.credibleSets.rows[47].study id GCST90256420 traitFromSource Glycated hemoglobin HbA1c levels studyType gwas

> [q1045] data.variant.credibleSets.rows[47].locus.rows[0] posteriorProbability 0.4898974222771357

> [q1046] data.variant.credibleSets.rows[47].l2GPredictions.rows[0] score 0.8729496598243713

rs1046896 (row 89, 17_82727657_C_T): 113 credible sets (q1042), none of a lifespan-class study. It tops five HbA1c sets,
T raising HbA1c (GCST90256420, +0.0315, P 3.3e-115, the lead at posterior 0.49, locus-to-gene FN3KRP 0.87; q1043-q1046),
and eight QTL sets. For row 89.

## Reading 2026-11-13, record

> [q1047] data variant null

Row 90: Open Targets 26.09 has no record of 18_13886720_G_A (q1047), so no credible set, locus-to-gene or
colocalisation. For row 90.

## Reading 2026-11-14, record

> [q1048] data.variant.credibleSets.rows[81] studyLocusId d2508d5e12142b3e8eb54b4167ef865d pValueMantissa 8.119000434875488 pValueExponent -11 beta 0.017619094552596 finemappingMethod PICS

> [q1049] data.variant.credibleSets.rows[81].study id GCST90624052 traitFromSource Frailty (Factor 6 - Disability) studyType gwas

> [q1050] data.variant.credibleSets.rows[81].locus.rows[0] posteriorProbability 0.03498049078820421

> [q1051] data.variant.credibleSets.rows[81].l2GPredictions.rows[0] score 0.6089618802070618

> [q1052] data.variant.credibleSets.rows[133] studyLocusId 8f846a1f014b7ca702f9d4e1caad2242 pValueMantissa 1.5199999809265137 pValueExponent -45 beta 0.0561 finemappingMethod PICS

> [q1053] data.variant.credibleSets.rows[133].study id GCST90309828 traitFromSource Body mass index (UKB data field 21001) studyType gwas

> [q1054] data.variant.credibleSets.rows[68] studyLocusId 7428dc232ed8038cf4f915d76e63d8ed pValueMantissa 1.2829999923706055 pValueExponent -10 beta 0.03282808 finemappingMethod PICS

> [q1055] data.variant.credibleSets.rows[68].study id GCST90132315 traitFromSource Coronary artery disease studyType gwas

> [q1056] data.credibleSet.colocalisation count 910

> [q1057] data.credibleSet.colocalisation.rows[51] rightStudyType gwas h4 0.968630786656337 clpp 0.02712301481793383 betaRatioSignAverage 1

> [q1058] data.credibleSet.colocalisation.rows[51].otherStudyLocus.study id GCST90132315 traitFromSource Coronary artery disease studyType gwas target null

> [q1059] data.credibleSet.colocalisation.rows[193] rightStudyType gwas h4 0.9555647457058117 clpp 0.01904860596858273 betaRatioSignAverage 1

> [q1060] data.credibleSet.colocalisation.rows[193].otherStudyLocus.study id GCST90029024 traitFromSource Type 2 diabetes studyType gwas target null

> [q1061] data.credibleSet.colocalisation.rows[26] rightStudyType gwas h4 0.9776971091273264 clpp 0.038034071418537985 betaRatioSignAverage 1

> [q1062] data.credibleSet.colocalisation.rows[26].otherStudyLocus.study id GCST90566412 traitFromSource Body mass index studyType gwas target null

> [q1063] data.credibleSet.colocalisation.rows[18] rightStudyType gwas h4 0.9703347791833433 clpp 0.02866110190255525 betaRatioSignAverage -1

> [q1064] data.credibleSet.colocalisation.rows[18].otherStudyLocus.study id GCST90691606 traitFromSource Worrier / anxious feelings (UKB data field 1980) studyType gwas target null

> [q1065] data.credibleSet.colocalisation count 0

Row 91 (18_60183864_T_C, rs17782313). The lead sits in 597 credible sets (all read, three pages of 200) and tops 43, mostly
body-composition, BMI and diet traits (also an HDL cholesteryl-ester ratio, height and nail fungus): in UK Biobank's BMI set (q1052, q1053) its alt C raises BMI, β +0.0561, P 1.5e-45,
posterior 0.15. Of the 43, four total-mass sets and one weight set print the other sign (the source's allele coding, not
resolved here; the colocalisations below carry the sign). No set of a lifespan study holds it; one ageing set does: Foote 2025's factor 6, disability (q1048 to q1050; led by rs476828, 18_60185354_T_C, alt C +0.0176 towards
frailty, P 8.1e-11, PICS; the lead at posterior 0.035). Foote's set:
locus-to-gene MC4R 0.609 (q1051), PMAIP1 0.081 next; no QTL colocalisation (q1065); 910 GWAS colocalisations (q1056,
all read, five pages), 647 at H4 ≥ 0.8, about 300 of them body-composition traits (86 BMI sets, 27 weight sets, and fat
and lean mass, impedance, waist and hip): BMI, H4 0.978, sign +1 (q1061, q1062), C raising BMI with frailty. Diseases colocalising, the
less-frail T on the lower-risk side in the sets that print a sign of +1: coronary artery disease (GCST90132315, H4 0.969, sign
+1, q1057, q1058; its own set, led by rs476828, C +0.0328, P 1.3e-10, q1054, q1055), type 2 diabetes (GCST90029024,
H4 0.956, +1, q1059, q1060; two other diabetes sets print −1, H4 0.969 and 0.949, and most print 0), heart failure, gout. Run the other way,
T raising them: HDL cholesterol, eGFR, SHBG, and self-reported worry and nervous feelings (worry H4 0.970, sign −1,
q1063, q1064). For row 91.

## Reading 2026-11-14, record

> [q1066] data.variant.credibleSets.rows[0] studyLocusId 15969b4dfb6b1acdb1ae723d6c64364a pValueMantissa 3 pValueExponent -9 beta 5.9159646 finemappingMethod PICS

> [q1067] data.variant.credibleSets.rows[0].locus.rows[0] posteriorProbability 1

> [q1068] data.variant.credibleSets.rows[0].l2GPredictions.rows[0] score 0.7555360794067383

> [q1069] data.variant.credibleSets.rows[0].l2GPredictions.rows[0].target approvedSymbol TIMM21

> [q1070] data.variant.credibleSets.rows[0].l2GPredictions.rows[1] score 0.34417304396629333

> [q1071] data.credibleSet.colocalisation count 0

18_73851283_T_G (rs77546126, row 92): one credible set holds it, Gurinovich's PICS set (q1066, P 3e-9), the lead
alone at posterior 1 (q1067), as at rows 19 and 77. Locus-to-gene: TIMM21 0.756 (q1068, q1069), FBXO15 0.344 (q1070),
CYB5A 0.217, C18orf63 0.054. The set has no colocalisation of any kind, GWAS or QTL (q1071). For row 92.

## Reading 2026-11-14, record

> [q1072] data.variant.credibleSets count 5

> [q1073] data.variant.credibleSets.rows[0].study id gtex-v10_ge_esophagus_mucosa_ensg00000121289 traitFromSource ENSG00000121289 studyType eqtl

> [q1074] data.variant.credibleSets.rows[3].study id gtex-v10_ge_fibroblast_ensg00000121289 traitFromSource ENSG00000121289 studyType eqtl

> [q1075] data.variant.credibleSets.rows[3].locus.rows[0] posteriorProbability 0.13942543490033024

19_32967573_G_C (rs62127362, row 94): five credible sets hold the lead (q1072), all molecular QTLs of CEP89
(ENSG00000121289) or its transcripts: GTEx oesophagus mucosa (q1073) and fibroblast (q1074) expression, HipSci iPSC
expression, transcript and transcript-usage sets; posterior 0.07 to 0.14 (fibroblast 0.14, q1075). No GWAS set, so no
lifespan-class set holds it, and no locus-to-gene or colocalisation is read for it. For row 94.

## Reading 2026-11-14, record

> [q1076] data.variant.credibleSets count 54

> [q1077] data.variant.credibleSets.rows[6] studyLocusId 14d169f285c37b4508bcf3d5ffcbef54 pValueMantissa 7.344662666320801 pValueExponent -9 beta 0.008471501279365589 finemappingMethod SuSiE-inf

> [q1078] data.variant.credibleSets.rows[6].study id GCST006701 traitFromSource Parental longevity (father's attained age) studyType gwas

> [q1079] data.variant.credibleSets.rows[6].locus.rows[0] posteriorProbability 0.5448193084618755

> [q1080] data.credibleSet.colocalisation count 124

> [q1081] data.credibleSet.colocalisation.rows[55] rightStudyType gwas h4 0.9973909284214304 clpp 0.2612128876727489 betaRatioSignAverage 1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1082] data.credibleSet.colocalisation.rows[55].otherStudyLocus.study id GCST90476035 traitFromSource Respiratory failure, insufficiency, arrest (PheCode 509) studyType gwas target null

> [q1083] data.credibleSet.colocalisation.rows[47] rightStudyType gwas h4 0.9961173706644707 clpp 0.1882205400267694 betaRatioSignAverage 0 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1084] data.credibleSet.colocalisation.rows[47].otherStudyLocus.study id GCST90479593 traitFromSource Chronic lung diseases including COPD, Emphysema and Bronchitis studyType gwas target null

> [q1085] data.credibleSet.colocalisation.rows[40] rightStudyType gwas h4 0.9987208553241945 clpp 0.41571759922217283 betaRatioSignAverage -1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1086] data.credibleSet.colocalisation.rows[40].otherStudyLocus.study id GCST009965 traitFromSource Cotinine levels in current smokers studyType gwas target null

> [q1087] data.credibleSet.colocalisation.rows[56] rightStudyType gwas h4 0.9979112142704848 clpp 0.3020887836515012 betaRatioSignAverage -1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1088] data.credibleSet.colocalisation.rows[56].otherStudyLocus.study id GCST90480701 traitFromSource How many years have you or did you smoke cigarettes? (inv-normal transformed) studyType gwas target null

> [q1089] data.credibleSet.colocalisation.rows[13] rightStudyType gwas h4 0.943536578891768 clpp 0.015229153231130098 betaRatioSignAverage 0 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1090] data.credibleSet.colocalisation.rows[13].otherStudyLocus.study id GCST90473255 traitFromSource ICD10 F17: Mental and behavioural disorders due to use of tobacco studyType gwas target null

> [q1091] data.credibleSet.colocalisation.rows[30] rightStudyType gwas h4 0.9941230859444651 clpp 0.1338317372474234 betaRatioSignAverage 1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1092] data.credibleSet.colocalisation.rows[30].otherStudyLocus.study id GCST90691579 traitFromSource LDL direct levels studyType gwas target null

> [q1093] data.credibleSet.colocalisation count 2

19_40835324_A_G (rs12461964, row 95): 54 credible sets hold it (q1076), one of a lifespan-class study: Pilling's
fathers' attained age (GCST006701; q1077, q1078; SuSiE-inf, P 7.3e-9, β +0.0085, so per G on the shorter-positive
scale), the lead at posterior 0.545 (q1079). The set has no locus-to-gene rows. It colocalises with 124 GWAS sets
(q1080), among them, at H4 0.94 to 0.999: respiratory failure (q1081, q1082; sign +1, G's way with shorter life),
chronic lung disease including COPD (q1083, q1084), cotinine in current smokers (q1085, q1086; −1), years smoked
(q1087, q1088; −1), tobacco use disorder (q1089, q1090), LDL direct (q1091, q1092; +1); also emphysema, chronic airway
obstruction, lung-disease medication, lung cancer in siblings, squamous lung carcinoma (+1 where signed), and many
lipid, fatty-acid and coffee sets. QTL colocalisations: two (q1093), both CYP2A6 splicing QTLs at H4 ≥ 0.8. So A,
the longer-lived fathers' allele, goes with less lung disease, more cotinine and more years smoked, and lower LDL.
For row 95.

## Reading 2026-11-14, record

> [q1094] data.credibleSet.colocalisation.rows[0] rightStudyType sqtl h4 0.8485514738354065 clpp 0.005189535153360986 betaRatioSignAverage 1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1095] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study.target approvedSymbol CYP2A6

Row 95: the first of the fathers' set's two QTL colocalisations, a GTEx liver splicing QTL of CYP2A6
(ENSG00000255974), H4 0.85 (q1094, q1095); the second, the same gene's liver transcript QTL, H4 0.88. All 124 GWAS
colocalisations (q1080) read by category and by betaRatioSignAverage (relative to the set's β, which
is +0.0085 per G in Open Targets' SuSiE-inf fit against the deposit's −0.0126 per A, the same direction, G shorter):
lipids and fatty acids 73 (24 signed +1, 4 signed −1, 45 unsigned); lung disease and function 20 (11 signed +1,
G's way with shorter life, 9 unsigned, none −1), among them respiratory failure, COPD, emphysema, chronic airway
obstruction, pneumonia and lung cancers; smoking 4 (cotinine and years smoked −1, so A raises them; tobacco use
disorder and smoking cessation unsigned); coffee 6, kidney function 6, other cancers 2, other 13. For row 95.

## Reading 2026-11-14, record

> [q1096] data.variant.credibleSets count 8

> [q1097] data.variant.credibleSets.rows[2] studyLocusId 542c7ae637fa8151e2615f830eb90340 pValueMantissa 1.0819727182388306 pValueExponent -10 beta 0.008991130964325567 finemappingMethod SuSiE-inf

> [q1098] data.variant.credibleSets.rows[2].study id GCST006701 traitFromSource Parental longevity (father's attained age) studyType gwas

> [q1099] data.variant.credibleSets.rows[2].locus.rows[0] posteriorProbability 0.7030831968444489

> [q1100] data.variant.credibleSets.rows[2].l2GPredictions.rows[0] score 0.48606178164482117

> [q1101] data.variant.credibleSets.rows[2].l2GPredictions.rows[0].target approvedSymbol JAG1

> [q1102] data.credibleSet.colocalisation count 31

> [q1103] data.credibleSet.colocalisation count 46

20_10983718_T_C (rs6108784, row 97): eight credible sets hold it (q1096), one of a lifespan-class study: Pilling's
fathers' attained age (q1097, q1098; SuSiE-inf, P 1.1e-10), the lead at posterior 0.70 (q1099). Locus-to-gene: JAG1
0.486 (q1100, q1101), under 0.5; SLX4IP 0.14. The set colocalises with 31 GWAS sets (q1102): blood pressure
(hypertension, pulse pressure, systolic and mean arterial pressure) and heel and total-body bone density, those signed
+1 (the C allele's way, with shorter fathers' lives), and blood urea nitrogen −1; and with 46 QTL sets (q1103),
every one signed −1 at H4 0.33 to 0.98: LINC02871 (ENSG00000125899) 29, the unnamed ENSG00000270777 17. For row 97.

## Reading 2026-11-14, record

> [q1104] data.credibleSet.colocalisation.rows[3] rightStudyType eqtl h4 0.9529969793400684 clpp 0.018351057086537184 betaRatioSignAverage -1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1105] data.credibleSet.colocalisation.rows[3].otherStudyLocus.study.target approvedSymbol LINC02871

> [q1106] data.credibleSet.colocalisation.rows[0] rightStudyType eqtl h4 0.9124580080396696 clpp 0.009310771926011705 betaRatioSignAverage -1 colocalisationMethod COLOC_PIP_ECAVIAR

> [q1107] data.credibleSet.colocalisation.rows[0].otherStudyLocus.study.target approvedSymbol ENSG00000270777

Row 97, the fathers' set's QTL colocalisations counted in full (all 46): at H4 ≥ 0.8, LINC02871 27 of 29 (one row,
q1104, q1105) and the unnamed ENSG00000270777 16 of 17 (q1106, q1107), all signed −1. ENSG00000270777 holds over a
tenth of the cis colocalisations, a rival under D24: E3. For row 97.

## Reading 2026-11-14, record

> [q1108] data.variant.credibleSets count 29

> [q1109] data.variant.credibleSets.rows[11] studyLocusId 633485c762f62d04fade634391c614d6 pValueMantissa 6 pValueExponent -10 beta -0.006251762 finemappingMethod PICS

> [q1110] data.variant.credibleSets.rows[11].study id GCST90321079 traitFromSource Aging studyType gwas

> [q1111] data.variant.credibleSets.rows[11].locus.rows[0] posteriorProbability 0.4827717686071306

20_32511508_T_C (rs159428, row 98): 29 credible sets hold it (q1108), none of a lifespan-class or healthspan study
(Zenin's healthspan has no set in Open Targets); Rosoff 2023's mvAge PICS set (GCST90321079, "Aging"; q1109, q1110),
the lead at posterior 0.48 (q1111), locus-to-gene under 0.06 for every gene. The others: triglyceride and cholesterol
ratios in lipoprotein subclasses, cognition and education, age at first sexual intercourse, papulosquamous disorders.
For row 98.
