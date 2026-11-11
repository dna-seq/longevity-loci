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
