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
