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
