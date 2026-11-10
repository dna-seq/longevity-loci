---
key: db-opentargets-26.09
database: opentargets
release: "26.09"
url: https://api.platform.opentargets.org/api/v4/graphql
accessed: 2026-11-10
depth: record
---

Open Targets Platform, release 26.09 (the API's `meta.dataVersion`), read through its GraphQL API. Each quote is a
value as the response gave it, as `field: value` on the record named in the prose; the record itself is not in
the cache (D12), so `check quotes` reads these as unknown until a fetcher caches it.

## Reading 2026-11-10, record

Variant 6_160589086_A_G (rs10455872, LPA), `alleleFrequencies` (gnomAD, as Open Targets carries it; the frequency
is of the alternative allele G, the Lp(a)-raising one):

> [q1] nfe_adj 0.06944975443343235

> [q2] eas_adj 0.000969743987587277

> [q3] afr_adj 0.012147599345713462

So G is about 7% in non-Finnish Europeans, 1% in Africans and 0.1% in East Asians: the tag does not carry Lp(a)
outside Europeans the way it does within (`ancestry_tag`).

Credible set 9a28de1c1982a3eb082610008a3fd828, study GCST009890 (Timmers 2019, "Parental lifespan"), PICS, four
variants, lead 6_160589086_A_G:

> [q4] 6_160589086_A_G posteriorProbability 0.3814318249801707

PIP 0.38: in a 95% credible set at 0.1 to 0.5, `causal:C2`. The other three members: 6_160576086_A_T 0.252,
6_160564494_G_A 0.227, 6_160584578_C_T (rs55730499) 0.139. The same lead holds PIP 0.40 in the multivariate study
GCST011100 (Timmers 2020), and rs55730499 leads Pilling 2017's set (GCST006697, SuSiE-inf) with rs10455872 at 0.32.

> [q5] LPA 0.5594255924224854

The locus-to-gene score of LPA on that credible set (next PLG 0.341): L2G ≥ 0.5, `effector:E2`. E1 would also need a
cis-QTL colocalisation for LPA, not read here (the set has 1,391 colocalisations of every kind; not sorted).

Variant 19_11079858_G_A (rs142158911, LDLR), `alleleFrequencies`, of the alternative allele A (the lifespan-raising
one):

> [q6] nfe_adj 0.11544578952019087

A is about 12% in non-Finnish Europeans, as Timmers 2019 has it (0.12). Other ancestries are not used: the African
figure (afr_adj 0.1875, exactly 3/16) is a sample too small to quote.

Credible set 03c517952394bc1997c99049d239a442, study GCST009890 (Timmers 2019, "Parental lifespan"), PICS, lead
19_11079858_G_A, about fifty members each with PIP under 0.04:

> [q7] 19_11079858_G_A posteriorProbability 0.035171205149789796

PIP 0.035: in the set, below 0.1, `causal:C3`. The signal is spread over a long LD block; no member stands out.

> [q8] 19_11091630_G_T r2Overall 0.9559867534825262

rs6511720 (19_11091630_G_T), Timmers 2020's, Pilling 2017's and Wright 2019's lead at LDLR, is in the same set at
r² 0.956 to the lead (PIP 0.017): the same signal, `ld_proxy_of:rs142158911`. Timmers 2020's multivariate study
GCST011100 has its own set here (6bf8fa2e5bdd96ea48ee4bc9856fdc7d, PICS, 49 members) led by rs6511720 at PIP 0.037,
so C3 either way; Pilling 2017's GCST006697 has no set in this window (rs6511720 was suggestive there).

> [q9] LDLR 0.9606614112854004

The locus-to-gene score of LDLR on that set (the only gene in the top three above 0.5): `effector:E2`. E1 would need
a cis-QTL colocalisation for LDLR, not read here; Timmers 2020's eQTL colocalisation at this locus names KANK2, ILF3
and others, not LDLR.

Variant 15_78525587_C_T (rs8042849, CHRNA3/5), `alleleFrequencies`, of the alternative allele T (the
lifespan-raising one):

> [q10] nfe_adj 0.6400883652430044

T is about 64% in non-Finnish Europeans (Timmers 2019: 0.65); 61% in African and 81% in East Asian gnomAD samples.

Credible set 8d0d0d1e11991d9ff9f5a5ea4fecf427, study GCST009890 (Timmers 2019), PICS, 30 members, lead
15_78525587_C_T:

> [q11] 15_78525587_C_T posteriorProbability 0.3505311365074509

PIP 0.35, `causal:C2`. GCST011100's set here (f3821132cc36ae09a8ac4cba08b1394b) has the same lead at 0.32.

> [q12] 15_78533838_G_A r2Overall 0.9337735037407924

rs931794 (Wright 2019's AncestryDNA lead), r² 0.93 to the lead; rs9788721 (Joshi's CHARGE proxy) is at 0.961.

> [q13] 15_78603787_A_G r2Overall 0.8550959801809388

rs1317286 (Pilling 2017's lead), r² 0.86 to the lead: `ld_proxy_of:rs8042849`. Pilling's own study GCST006697 holds
two sets here: rs1317286's (SuSiE-inf, 4b2a4542d121aa1e89555da4603a227a, with rs8042849 in it) and a second led by
rs578776 (c1d809ebe527dd273d44ff6759ceb60e, L2G CHRNA3 0.59), a secondary signal not scored here.

> [q14] CHRNA5 0.29093170166015625

The locus-to-gene score of CHRNA5 on the Timmers 2019 set (next PSMA4 0.13,
CHRNA3 0.08): no gene reaches 0.5, `effector:E3`. The healthspan GWAS GCST007406 (Zenin 2019) has no credible set in
this window.

Variant 9_22100177_G_C (rs1556516, CDKN2B-AS1), `alleleFrequencies`, of the alternative allele C (the
lifespan-lowering one):

> [q15] nfe_adj 0.5097071647419279

C is about 51% in non-Finnish Europeans, G 49%: the heterozygote is the most common genotype. C is 89% in African
and 67% in East Asian gnomAD samples.

Credible set 02462f216ce479d0c67d8b7bf734079f, study GCST009890 (Timmers 2019), PICS, 53 members, lead
9_22100177_G_C:

> [q16] 9_22100177_G_C posteriorProbability 0.05611117205107125

PIP 0.056, in the set below 0.1: `causal:C3`. The same block leads Timmers 2020's set (rs7859727, PIP 0.095),
Pilling 2017's (rs1556516, SuSiE-inf, PIP 0.17) and Zenin 2019's healthspan set GCST007406 (rs7859727, 0.11).

> [q17] 9_22103814_A_G r2Overall 0.9843762746950737

rs1333042 (Wright 2019's AncestryDNA lead), r² 0.98 to the lead; rs7859727 (Timmers 2020, Zenin 2019) is at
0.945: `ld_proxy_of:rs1556516`. Deelen 2019's CDKN2A/B discovery variant rs7039467 is in none of these sets.

> [q18] CDKN2B 0.3581562936306

The locus-to-gene score of CDKN2B on the Timmers 2019 set (next CDKN2A 0.21, DMRTA1 0.12): below 0.5,
`effector:E3`. Timmers 2020 names CDKN2B as a cis-acting gene here by SMR and HEIDI, not by a colocalisation H4,
which §4.2's E2 asks for; Open Targets' own colocalisations were not read.

Variant 12_111621753_C_T (rs11065979, ATXN2/SH2B3), `alleleFrequencies`, of the alternative allele T (the
lifespan-lowering one):

> [q19] nfe_adj 0.4454526645582715

> [q20] eas_adj 0.0017928286852589642

T is about 45% in non-Finnish Europeans and almost absent in East Asians (0.2%; 7.5% in African samples): the
lifespan-lowering haplotype is essentially European, and the locus has nothing to say outside Europe
(`ancestry_tag`). The SH2B3 missense rs3184504 (12_111446804_T_C, `mostSevereConsequence` missense_variant) shows
the same: its C allele is 51% in Europeans, 99.9% in East Asians.

Credible set 8a1b141eb70f7b60349f9bee88c3ec69, study GCST009890 (Timmers 2019), PICS, 21 members spread over about
1 Mb (to rs11066320 near PTPN11):

> [q21] 12_111621753_C_T posteriorProbability 0.3449911407808129

PIP 0.34, `causal:C2`. The missense rs3184504 is in the set at PIP 0.02 (r² 0.81); in Pilling 2017's SuSiE-inf
sets (GCST006697) it holds 0.15–0.16 against 0.23–0.25 for rs10774625 and rs7137828: not the C1 "coding with PIP ≥
0.2".

> [q22] 12_111494996_C_T r2Overall 0.8130060667781549

rs7137828 (Pilling 2017's lead), r² 0.81 to the lead; rs10774625 (Wright 2019's) 0.77: `ld_proxy_of:rs11065979`.

> [q23] SH2B3 0.9505289196968079

The locus-to-gene score of SH2B3 on Timmers 2020's set here (GCST011100, 73d4741853bd7c0b6cf0d72356699b0b, lead
rs7137828); Pilling 2017's sets give SH2B3 0.95 and 0.96; Timmers 2019's broader set gives 0.41 (next ALDH2 0.17).
L2G ≥ 0.5 on the tighter sets, no colocalisation read: `effector:E2`, SH2B3.
