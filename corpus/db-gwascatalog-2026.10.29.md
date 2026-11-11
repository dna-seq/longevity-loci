---
key: db-gwascatalog-2026.10.29
database: gwascatalog
release: "2026.10.29"
url: https://www.ebi.ac.uk/gwas/rest/api/v2/associations
accessed: 2026-11-11
depth: record
---

The GWAS Catalog's REST API 2.0, data release 2026-10-29 (its `metadata` endpoint's `data_release_date`). Each
record named here is cached by `loci fetch-supp` as `associations-<rsID>.json`, one object a line; each quote is a
line of it as cached. A catalog association is the catalog's own curation of a paper, not a second study.

## Reading 2026-11-11, record

rs146254978 (FPGT/TNNI3K), for row 5.

> [q1] _embedded.associations[0] association_id 35691731 risk_frequency 0.98 pvalue_description pvalue_mantissa 5 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.045-0.094] beta 0.0692 unit decrease p_value 5e-08 accession_id GCST006702 pubmed_id 29227965 first_author Pilling LC ci_lower 0.045 ci_upper 0.094

The catalog's one association for rs146254978: Pilling 2017 (GCST006702), P 5 × 10⁻⁸ as the catalog rounds it (the
paper gives 4.6 × 10⁻⁸, pmid-29227965#q15), risk frequency 0.98, "0.0692 unit decrease". The catalog reads the
paper's β as T lowering combined parental age at death, as pmid-29227965#q17 does.

> [q2] _embedded.associations[0].reported_trait[0] Parental longevity (combined parental age at death)

The reported trait: combined parental age at death.

> [q3] page size 20 totalElements 1 totalPages 1 number 0

The search returns one association in all: in this release the catalog records no other trait for rs146254978.

## Reading 2026-11-11, record

rs1230666 (MAGI3, the PTPN22 region), for row 7, cached as `associations-rs1230666.json` (the query adds
`&size=50`). Effect alleles as the catalog records them.

> [q4] _embedded.associations[0] association_id 227599930 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -72 multi_snp_haplotype false snp_interaction false range [0.21-0.27] beta 0.24 log odds ratio increase p_value 2e-72 accession_id GCST90998905 pubmed_id 42527560 first_author Bujnis MN ci_lower 0.21 ci_upper 0.27

> [q5] _embedded.associations[0].reported_trait[0] Hashimoto thyroiditis

> [q6] _embedded.associations[0].snp_allele[0] rs_id rs1230666 effect_allele A

Hashimoto thyroiditis: A raises the odds, P 2 × 10⁻⁷².

> [q7] _embedded.associations[5] association_id 165684131 risk_frequency 0.1447 pvalue_description pvalue_mantissa 9 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [0.026-0.046] beta 0.036 unit increase p_value 9e-12 accession_id GCST90455657 pubmed_id 40195560 first_author Lee DSM ci_lower 0.026 ci_upper 0.046

> [q8] _embedded.associations[5].reported_trait[0] Heart failure

> [q9] _embedded.associations[5].snp_allele[0] rs_id rs1230666 effect_allele A

Heart failure: A raises it, P 9 × 10⁻¹².

> [q10] _embedded.associations[6] association_id 131476329 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -11 multi_snp_haplotype false snp_interaction false range [0.0072-0.0131] beta 0.010161293 unit decrease p_value 2e-11 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0072 ci_upper 0.0131

> [q11] _embedded.associations[6].reported_trait[0] Aging

> [q12] _embedded.associations[6].snp_allele[0] rs_id rs1230666 effect_allele A

Rosoff 2023's mvAge (GCST90321079): A lowers the factor, P 2 × 10⁻¹¹, so G is on the healthier-ageing side.

> [q13] _embedded.associations[7] association_id 101976720 risk_frequency 0.152 pvalue_description pvalue_mantissa 5 pvalue_exponent -13 multi_snp_haplotype false snp_interaction false range [1.039-1.068] or_per_copy_num 1.053 or_value 1.053 beta - p_value 5e-13 accession_id GCST90132314 pubmed_id 36474045 first_author Aragam KG ci_lower 1.039 ci_upper 1.068

> [q14] _embedded.associations[7].reported_trait[0] Coronary artery disease

> [q15] _embedded.associations[7].snp_allele[0] rs_id rs1230666 effect_allele A

Coronary artery disease: A raises the odds (OR 1.053), P 5 × 10⁻¹³.

> [q16] _embedded.associations[11] association_id 41310595 risk_frequency 0.8721 pvalue_description pvalue_mantissa 4 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range [0.041-0.078] beta 0.0592 unit decrease p_value 4e-10 accession_id GCST004988 pubmed_id 29059683 first_author Michailidou K ci_lower 0.041 ci_upper 0.078

> [q17] _embedded.associations[11].reported_trait[0] Breast cancer

> [q18] _embedded.associations[11].snp_allele[0] rs_id rs1230666 effect_allele G

Breast cancer: G, the common allele, lowers it ("unit decrease"), P 4 × 10⁻¹⁰.

> [q19] _embedded.associations[13] association_id 41864 risk_frequency 0.16 pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.014-0.039] beta 0.0269 unit increase p_value 2e-08 accession_id GCST002373 pubmed_id 24586183 first_author Medici M ci_lower 0.014 ci_upper 0.039

> [q20] _embedded.associations[13].reported_trait[0] Thyroid peroxidase antibody levels

> [q21] _embedded.associations[13].snp_allele[0] rs_id rs1230666 effect_allele A

Thyroid peroxidase antibody levels: A raises them, P 2 × 10⁻⁸.

> [q22] page size 50 totalElements 14 totalPages 1 number 0

Fourteen associations in all. Those read further for row 7:

> [q23] _embedded.associations[8] association_id 77342205 risk_frequency 0.166789 pvalue_description pvalue_mantissa 3 pvalue_exponent -7 multi_snp_haplotype false snp_interaction false range [1.04-1.09] or_per_copy_num 1.06 or_value 1.06 beta - p_value 3e-07 accession_id GCST011365 pubmed_id 33532862 first_author Hartiala JA ci_lower 1.04 ci_upper 1.09

> [q24] _embedded.associations[8].reported_trait[0] Myocardial infarction

> [q25] _embedded.associations[8].snp_allele[0] rs_id rs1230666 effect_allele G

Myocardial infarction (GCST011365): the record names G as the effect allele with OR 1.06, yet its risk frequency
0.167 is A's frequency, not G's (q56 of db-opentargets-26.09: G 0.85). The record disagrees with itself: unresolved,
read neither as support nor as a counterexample.

> [q26] _embedded.associations[1] association_id 214467339 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -7 multi_snp_haplotype false snp_interaction false range - or_per_copy_num 1.0598 or_value 1.0598 beta - p_value 3e-07 accession_id GCST90432175 pubmed_id 38072966 first_author Al-Ali AK

> [q27] _embedded.associations[1].reported_trait[0] Myocardial infarction

> [q28] _embedded.associations[1].snp_allele[0] rs_id rs1230666 effect_allele ?

Myocardial infarction (GCST90432175): OR 1.06, P 3 × 10⁻⁷, no allele stated (`?`): no direction.

> [q29] _embedded.associations[3] association_id 193104754 risk_frequency NR pvalue_description pvalue_mantissa 5 pvalue_exponent -7 multi_snp_haplotype false snp_interaction false range [0.75-0.88] or_per_copy_num 0.81 or_value 0.81 beta - p_value 5e-07 accession_id GCST90624742 pubmed_id 40883272 first_author Guler M ci_lower 0.75 ci_upper 0.88

> [q30] _embedded.associations[3].reported_trait[0] Hodgkin's lymphoma

> [q31] _embedded.associations[3].snp_allele[0] rs_id rs1230666 effect_allele ?

Hodgkin's lymphoma (GCST90624742): OR 0.81, P 5 × 10⁻⁷, no allele stated (`?`): no direction, and an effect of
that size could run either way.

> [q32] _embedded.associations[9] association_id 62271253 risk_frequency 0.8533 pvalue_description pvalue_mantissa 2 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range - beta - p_value 2e-09 accession_id GCST011100 pubmed_id 32678081 first_author Timmers PRHJ

> [q33] _embedded.associations[9].reported_trait[0] Aging traits (healthspan, parental lifespan or longevity) (multivariate analysis)

> [q34] _embedded.associations[9].snp_allele[0] rs_id rs1230666 effect_allele G

Timmers 2020's multivariate ageing traits (GCST011100): P 2 × 10⁻⁹, G named as the effect allele with no effect
size (Open Targets' set has none either): an allele label, not a direction.

Among the records whose allele is stated and consistent, every one puts A, the minor allele that shortens life, on the
side of more disease (thyroid autoimmunity, coronary disease, heart failure), and G on the side of less breast cancer:
no trade-off detected among them. Three records leave it open: the self-contradicting myocardial infarction record
(q23–q25) and the two with no allele (q26–q31). Rosoff's mvAge direction (q10) rests on the catalog's curation alone:
Open Targets carries the same 0.010161293, most likely the same upstream record, not a second check.
