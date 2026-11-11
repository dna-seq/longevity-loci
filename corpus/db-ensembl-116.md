---
key: db-ensembl-116
database: ensembl
release: "116"
url: https://rest.ensembl.org
accessed: 2026-11-11
depth: record
---

Ensembl release 116 (the REST API's `/info/data`), read through its REST API: pairwise linkage disequilibrium
(`/ld/human/pairwise`) in 1000 Genomes phase 3 Europeans (EUR), and variant records with population frequencies
(`/variation/human`). Each quote is a line of the record as `loci fetch-supp` cached it. The pairwise answer gives
r² and D′ but not which alleles travel together; where the phase is stated below it is derived from the
frequencies and the r², and says so.

## Reading 2026-11-11, record

> [q1] [0] variation2 rs3135006 variation1 rs1049053 r2 0.800109 d_prime 0.987217 population_name 1000GENOMES:phase_3:EUR

rs1049053 (row 103's lead, Zenin 2019's healthspan SNP) and rs3135006 (Wright 2019's AncestryDNA SNP): r² 0.80,
D′ 0.99 in EUR. rs3135006 is a close proxy of rs1049053.

> [q2] [0] population_name 1000GENOMES:phase_3:EUR r2 0.800109 variation1 rs1049053 variation2 rs3129720 d_prime 0.987217

rs1049053 and rs3129720 (the tag Timmers 2019's longevity look-up used for row 38): r² 0.80, D′ 0.99, the same
as q1.

> [q3] [0] variation1 rs1049053 r2 0.315028 variation2 rs34967069 population_name 1000GENOMES:phase_3:EUR d_prime 0.999998

rs1049053 and rs34967069 (row 38's lead): r² 0.32, D′ 1.0. The two leads are not proxies of each other.

> [q4] [0] variation2 rs9275245 population_name 1000GENOMES:phase_3:EUR d_prime 0.982821 variation1 rs1049053 r2 0.392049

rs1049053 and rs9275245 (a clumped SNP of Wright 2019's mothers' meta-analysis): r² 0.39, D′ 0.98. Named, not
scored.

> [q5] populations[86] allele C allele_count 248 population 1000GENOMES:phase_3:EUR frequency 0.246520874751491

> [q6] populations[77] allele_count 213 frequency 0.211729622266402 allele T population 1000GENOMES:phase_3:EUR

The minor alleles in EUR: C at rs1049053 (0.25), T at rs3135006 (0.21). An r² of 0.80 between a 0.25 and a 0.21
allele is possible only when the two minor alleles travel together (with the minor allele of one paired to the
major allele of the other, r² could not exceed about 0.09). So C at rs1049053 rides with T at rs3135006: derived
from q1, q5 and q6, not a record of its own. For row 103.

## Reading 2026-11-11, supplement

Row 8 (IL6R p.Asp358Ala): the seed's rs2228145 (locus 8) and rs8192284 (locus 157), and the lifespan SNPs near them.

> [q7] name rs2228145

> [q8] synonyms[28] rs8192284

Asked for rs8192284, Ensembl 116 answers with the record of rs2228145 and lists rs8192284 among its synonyms: dbSNP
merged rs8192284 into rs2228145. One variant, so seed loci 8 and 157 are one row (D14). The IL6R MR Consortium
calls it the same way (pmid-22421340#q1).

> [q9] most_severe_consequence missense_variant

> [q10] mappings[0] assembly_name GRCh38 seq_region_name 1 ancestral_allele A location 1:154454494-154454494 allele_string A/C/T end 154454494 coord_system chromosome strand 1 start 154454494

rs2228145 is a missense variant (IL6R p.Asp358Ala), at GRCh38 1:154,454,494, A/C (and a rare T). Coding: effector E1
by §4.2's first clause.

> [q11] [0] population_name 1000GENOMES:phase_3:EUR d_prime 0.999999 r2 0.941835 variation2 rs7529229 variation1 rs2228145

rs7529229, the IL6R MR Consortium's and the CHD studies' instrument: r² 0.94 to rs2228145 in 1000 Genomes EUR.

> [q12] [0] population_name 1000GENOMES:phase_3:EUR d_prime 0.982314 variation1 rs2228145 variation2 rs7518199 r2 0.932349

rs7518199, Wright 2019's clumped SNP for AncestryDNA fathers (pmid-31484785#q25): r² 0.93.

> [q13] [0] r2 0.332493 variation2 rs12568083 variation1 rs2228145 population_name 1000GENOMES:phase_3:EUR d_prime 0.929192

rs12568083, Wright 2019's clumped SNP for AncestryDNA mothers: r² 0.33. Not a proxy; not read.

> [q14] [0] d_prime 0.952959 variation2 rs6689306 variation1 rs2228145 population_name 1000GENOMES:phase_3:EUR r2 0.404919

rs6689306, Pilling 2017's suggestive IL6R SNP (pmid-29227965#q20): r² 0.40, D′ 0.95.

> [q15] populations[100] population 1000GENOMES:phase_3:EUR allele C frequency 0.36779324055666 allele_count 370

> [q16] populations[100] allele C population 1000GENOMES:phase_3:EUR frequency 0.359840954274354 allele_count 362

> [q17] populations[76] allele_count 445 allele A population 1000GENOMES:phase_3:EUR frequency 0.44234592445328

1000 Genomes EUR frequencies: C at rs7518199 0.368, C at rs2228145 0.360, A at rs6689306 0.442. Phase from these
and the r² above is derived, never a record: rs7518199-C with rs2228145-C (r² 0.93 is possible only with the minor
alleles together); rs6689306-A with rs2228145-A (pmid-29227965#q20).
