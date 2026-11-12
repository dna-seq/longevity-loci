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

## Reading 2026-11-11, supplement

rs2228145 (IL6R p.Asp358Ala), for row 8: `associations?rs_id=rs2228145&size=50`, cached as
`associations-rs2228145.json`; rs8192284, its merged synonym, as `associations-rs8192284.json` (6 records, none
with a stated allele but one fibrinogen record).

> [q50] page size 50 totalElements 36 totalPages 1 number 0

36 associations for rs2228145, read in full: protein levels (IL6R, IL-6, OSMR, CFB), CRP, fibrinogen, blood counts,
lipids, allergic disease, atopic dermatitis, eczema, rheumatoid arthritis. None for lifespan, longevity, coronary
disease or aortic aneurysm. Those that settle a direction:

> [q35] _embedded.associations[7] association_id 162844628 risk_frequency 0.407474 pvalue_description pvalue_mantissa 1 pvalue_exponent -346 multi_snp_haplotype false snp_interaction false range [0.85-0.92] beta 0.8864 unit increase p_value 0.0 accession_id GCST90425952 pubmed_id 39528825 first_author Western D ci_lower 0.85 ci_upper 0.92

> [q36] _embedded.associations[7].reported_trait[0] Interleukin-6 receptor subunit alpha (analyte X4139.71) levels

> [q37] _embedded.associations[7].snp_allele[0] rs_id rs2228145 effect_allele C

Interleukin-6 receptor subunit alpha (SomaScan 4139-71; Western 2024, GCST90425952): β +0.89 per C, P below the floating-point floor (0.0). C raises circulating soluble IL6R, the protein readout of the variant.

> [q38] _embedded.associations[15] association_id 104522964 risk_frequency 0.6 pvalue_description pvalue_mantissa 2 pvalue_exponent -15 multi_snp_haplotype false snp_interaction false range [0.081-0.135] beta 0.108 unit increase p_value 2e-15 accession_id GCST90247165 pubmed_id 34648354 first_author Pietzner M ci_lower 0.081 ci_upper 0.135

> [q39] _embedded.associations[15].reported_trait[0] C-reactive protein levels

> [q40] _embedded.associations[15].snp_allele[0] rs_id rs2228145 effect_allele A

C-reactive protein (Pietzner 2021, GCST90247165): β +0.108 per A, P 2 × 10⁻¹⁵. A raises CRP, so C lowers it: less IL-6 signalling.

> [q41] _embedded.associations[35] association_id 41487 risk_frequency 0.6 pvalue_description pvalue_mantissa 4 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [1.05-1.10] or_per_copy_num 1.08 or_value 1.08 beta - p_value 4e-09 accession_id GCST002318 pubmed_id 24390342 first_author Okada Y ci_lower 1.05 ci_upper 1.1

> [q42] _embedded.associations[35].reported_trait[0] Rheumatoid arthritis

> [q43] _embedded.associations[35].snp_allele[0] rs_id rs2228145 effect_allele A

Rheumatoid arthritis (Okada 2014, GCST002318): OR 1.08 per A, P 4 × 10⁻⁹. A raises rheumatoid arthritis; C lowers it.

> [q44] _embedded.associations[23] association_id 55899097 risk_frequency 0.4108 pvalue_description pvalue_mantissa 1 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [1.03-1.051] or_per_copy_num 1.04 or_value 1.04 beta - p_value 1e-12 accession_id GCST009716 pubmed_id 31361310 first_author Johansson A ci_lower 1.03 ci_upper 1.051

> [q45] _embedded.associations[23].reported_trait[0] Allergic disease (asthma, hay fever or eczema)

> [q46] _embedded.associations[23].snp_allele[0] rs_id rs2228145 effect_allele C

Allergic disease, asthma, hay fever or eczema (Johansson 2019, GCST009716): OR 1.04 per C, P 1 × 10⁻¹².

> [q47] _embedded.associations[33] association_id 15815085 risk_frequency NR pvalue_description pvalue_mantissa 5 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range [1.05-1.11] or_per_copy_num 1.08 or_value 1.08 beta - p_value 5e-10 accession_id GCST003184 pubmed_id 26482879 first_author Paternoster L ci_lower 1.05 ci_upper 1.11

> [q48] _embedded.associations[33].reported_trait[0] Atopic dermatitis

> [q49] _embedded.associations[33].snp_allele[0] rs_id rs2228145 effect_allele C

Atopic dermatitis (Paternoster 2015, GCST003184): OR 1.08 per C, P 5 × 10⁻¹⁰.

The trade-off at this variant, from the stated alleles: C, the minor allele and the longer-life side (row 8), lowers
CRP and rheumatoid arthritis and raises allergic disease and atopic dermatitis. Every record with a stated allele is
consistent with that; the records with `?` (respiratory disease factor, venous thromboembolism, white cell count, CRP
in Wojcik, eczema in Kichaev) state no allele.

## Reading 2026-11-11, record

> [q51] _embedded.associations[0] association_id 55479467 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0099-0.0204] beta 0.01511 unit increase p_value 2e-08 accession_id GCST009448 pubmed_id 31484785 first_author Wright KM ci_lower 0.0099 ci_upper 0.0204

> [q52] _embedded.associations[0].reported_trait[0] Longevity

> [q53] _embedded.associations[0].snp_allele[0] rs_id rs10798302 effect_allele G

> [q54] page size 50 totalElements 1 totalPages 1 number 0

`associations-rs10798302.json`: one association, Wright 2019's GCST009448, reported as "Longevity": beta 0.0151 per
G, P 2 × 10⁻⁸, the raw P of the current-age GWAS (pmid-31484785#q28), not its genomic-control 1.5 × 10⁻⁶. No other
trait. For row 10.

> [q55] _embedded.associations[0] association_id 55479486 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.012-0.025] beta 0.01856 unit increase p_value 2e-08 accession_id GCST009448 pubmed_id 31484785 first_author Wright KM ci_lower 0.012 ci_upper 0.025

> [q56] page size 50 totalElements 1 totalPages 1 number 0

`associations-rs16847402.json`: the same study's one record, beta 0.0186, P 2 × 10⁻⁸ (raw). For row 10.

## Reading 2026-11-11, record

> [q57] _embedded.associations[0] association_id 56008494 risk_frequency 0.174 pvalue_description pvalue_mantissa 6 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.018-0.038] beta 0.0277 unit increase p_value 6.000000000000001e-08 accession_id GCST009890 pubmed_id 30642433 first_author Timmers PR ci_lower 0.018 ci_upper 0.038

> [q58] _embedded.associations[0].snp_allele[0] rs_id rs6744653 effect_allele A

rs6744653 (`associations-rs6744653.json`), its one association: Timmers 2019, GCST009890, parental lifespan, A,
beta 0.0277, P 6 × 10⁻⁸. For row 11.

> [q59] _embedded.associations[5] association_id 131476496 risk_frequency NR pvalue_description pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0048-0.0101] beta 0.00747789 unit increase p_value 4e-08 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0048 ci_upper 0.0101

> [q60] _embedded.associations[5].snp_allele[0] rs_id rs66906321 effect_allele T

rs66906321 (`associations-rs66906321.json`, nine associations): Rosoff 2023's mvAge (GCST90321079, "Aging"), T,
beta +0.0075, P 4 × 10⁻⁸: T on the healthier-ageing side. Rosoff's cached text does not list the SNP (its Table 1
holds novel leads only), so this record is the only cached source of the value. For row 11.

> [q61] _embedded.associations[7] association_id 36609274 risk_frequency 0.813524 pvalue_description pvalue_mantissa 1 pvalue_exponent -34 multi_snp_haplotype false snp_interaction false range [1.21-1.29] or_per_copy_num 1.25 or_value 1.25 beta - p_value 1e-34 accession_id GCST007241 pubmed_id 30677029 first_author Riveros-McKay F ci_lower 1.21 ci_upper 1.29

> [q62] _embedded.associations[7].snp_allele[0] rs_id rs66906321 effect_allele C

Extreme obesity (Riveros-McKay 2019): C, frequency 0.81, OR 1.25 (1.21 to 1.29), P 1 × 10⁻³⁴. So T, the
lifespan-raising allele, goes with less extreme obesity. For row 11.

> [q63] _embedded.associations[8] association_id 35964026 risk_frequency 0.178119 pvalue_description pvalue_mantissa 5 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range [0.01-0.02] beta 0.015077 unit decrease p_value 5e-10 accession_id GCST006979 pubmed_id 30598549 first_author Morris JA ci_lower 0.01 ci_upper 0.02

> [q64] _embedded.associations[8].snp_allele[0] rs_id rs66906321 effect_allele T

Heel bone mineral density (Morris 2019): T, frequency 0.18, beta 0.0151 decrease, P 5 × 10⁻¹⁰. T lowers heel bone
density. For row 11.

> [q65] _embedded.associations[6] association_id 106058670 risk_frequency NR pvalue_description pvalue_mantissa 1 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta - p_value 1e-08 accession_id GCST90274732 pubmed_id 36929942 first_author Lindstrom S

> [q66] _embedded.associations[6].snp_allele[0] rs_id rs66906321 effect_allele T

Cancer (pleiotropy, Lindstrom 2023): T, P 1 × 10⁻⁸, no beta or direction. For row 11.

> [q67] _embedded.associations[3] association_id 138938323 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -23 multi_snp_haplotype false snp_interaction false range - beta - p_value 2e-23 accession_id GCST90278622 pubmed_id 38116116 first_author Chen CY

> [q68] _embedded.associations[3].snp_allele[0] rs_id rs66906321 effect_allele ?

> [q69] page size 50 totalElements 9 totalPages 1 number 0

Body mass index (Chen 2024), P 2 × 10⁻²³, with no allele ("?"); the record's weight, waist and body-fat associations
state none either. Four of the nine records give no allele. For row 11.

> [q70] _embedded.associations[0].efo_traits[0] efo_id OBA_VT0005372 efo_trait life span determination trait

The catalog maps Wright 2019's age record at rs10798302 to life span (OBA_VT0005372). For row 10.

> [q71] page size 50 totalElements 8 totalPages 1 number 0

> [q72] _embedded.associations[2] association_id 227578446 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range [0.059-0.113] beta 0.086 unit decrease p_value 3e-10 accession_id GCST90998896 pubmed_id 42521668 first_author Bright U ci_lower 0.059 ci_upper 0.113

> [q73] _embedded.associations[2].snp_allele[0] rs_id rs1993709 effect_allele A

> [q74] _embedded.associations[6].snp_allele[0] rs_id rs1993709 effect_allele ?

> [q75] page size 50 totalElements 1 totalPages 1 number 0

Row 4's trade-off check (D18.1): rs2613508 has one record, mvAge's (`associations-rs2613508.json`); its BMI lead
rs1993709 has eight (`associations-rs1993709.json`). A at rs1993709, the allele riding with rs2613508's longer-life C
(db-opentargets-26.09#q46-q52), lowers BMI and waist-hip ratio and, in Bright's fibromyalgia GWAS, fibromyalgia (beta
0.086 decrease, P 3 × 10⁻¹⁰); G is the early-onset extreme obesity risk allele. Four records state no allele (two
fibromyalgia MTAG records, extreme obesity, neuroticism, q74). No record ties the longer-life allele to a harm; none
detected is not none. For row 4.

## rs1275922 (KCNK3) and its proxies, for row 12

`associations-rs1275922.json` (page size 50 totalElements 3 totalPages 1 number 0), `associations-rs11126666.json` (page size 50 totalElements 10 totalPages 1 number 0, r² 0.99 to the lead,
db-ensembl-116#q42), `associations-rs1731248.json` (page size 50 totalElements 1 totalPages 1 number 0, r² 0.97 in Timmers' credible set,
db-opentargets-26.09#q103); `associations-rs1731247.json` holds none.

> [q76] _embedded.associations[0] association_id 131476339 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0047-0.0093] beta 0.006999004 unit decrease p_value 3.0000000000000004e-09 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0047 ci_upper 0.0093

> [q77] _embedded.associations[0].reported_trait[0] Aging

> [q78] _embedded.associations[0].snp_allele[0] rs_id rs1275922 effect_allele A

> [q79] _embedded.associations[1] association_id 62271257 risk_frequency 0.74 pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta - p_value 2e-08 accession_id GCST011100 pubmed_id 32678081 first_author Timmers PRHJ

> [q80] _embedded.associations[1].reported_trait[0] Aging traits (healthspan, parental lifespan or longevity) (multivariate analysis)

> [q81] _embedded.associations[1].snp_allele[0] rs_id rs1275922 effect_allele G

> [q82] _embedded.associations[2] association_id 56008433 risk_frequency 0.74 pvalue_description pvalue_mantissa 6 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.17-0.34] beta 0.2579 years increase p_value 6.000000000000001e-09 accession_id GCST009890 pubmed_id 30642433 first_author Timmers PR ci_lower 0.17 ci_upper 0.34

> [q83] _embedded.associations[2].reported_trait[0] Parental lifespan

> [q84] _embedded.associations[2].snp_allele[0] rs_id rs1275922 effect_allele G

> [q85] _embedded.associations[1] association_id 104107644 risk_frequency NR pvalue_description pvalue_mantissa 8 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0064-0.0126] beta 0.0095 unit decrease p_value 8e-09 accession_id GCST90255621 pubmed_id 36581621 first_author Huang J ci_lower 0.0064 ci_upper 0.0126

> [q86] _embedded.associations[1].reported_trait[0] Body mass index

> [q87] _embedded.associations[1].snp_allele[0] rs_id rs11126666 effect_allele G

> [q88] _embedded.associations[3] association_id 49100549 risk_frequency 0.28 pvalue_description pvalue_mantissa 1 pvalue_exponent -13 multi_snp_haplotype false snp_interaction false range [0.013-0.025] beta 0.019 unit increase p_value 1e-13 accession_id GCST004904 pubmed_id 28892062 first_author Akiyama M ci_lower 0.013 ci_upper 0.025

> [q89] _embedded.associations[3].reported_trait[0] Body mass index

> [q90] _embedded.associations[3].snp_allele[0] rs_id rs11126666 effect_allele A

> [q91] _embedded.associations[4] association_id 45606655 risk_frequency 0.255998 pvalue_description pvalue_mantissa 7 pvalue_exponent -31 multi_snp_haplotype false snp_interaction false range [0.088-0.124] beta 0.106201254 unit increase p_value 7.000000000000001e-31 accession_id GCST007929 pubmed_id 31015401 first_author Wu Y ci_lower 0.088 ci_upper 0.124

> [q92] _embedded.associations[4].reported_trait[0] Medication use (calcium channel blockers)

> [q93] _embedded.associations[4].snp_allele[0] rs_id rs11126666 effect_allele A

> [q94] _embedded.associations[6] association_id 35037989 risk_frequency NR pvalue_description pvalue_mantissa 5 pvalue_exponent -11 multi_snp_haplotype false snp_interaction false range [NR] beta 0.019 unit decrease p_value 4.9999999999999995e-11 accession_id GCST006368 pubmed_id 30108127 first_author Hoffmann TJ

> [q95] _embedded.associations[6].reported_trait[0] Body mass index

> [q96] _embedded.associations[6].snp_allele[0] rs_id rs11126666 effect_allele G

> [q97] _embedded.associations[7] association_id 12223330 risk_frequency 0.283 pvalue_description pvalue_mantissa 1 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.014-0.027] beta 0.02 kg/m2 increase p_value 1e-09 accession_id GCST002783 pubmed_id 25673413 first_author Locke AE ci_lower 0.014 ci_upper 0.027

> [q98] _embedded.associations[7].reported_trait[0] Body mass index

> [q99] _embedded.associations[7].snp_allele[0] rs_id rs11126666 effect_allele A

> [q100] _embedded.associations[0] association_id 117768508 risk_frequency 0.28753 pvalue_description pvalue_mantissa 5 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.872-0.934] or_per_copy_num 0.902 or_value 0.902 beta - p_value 5e-09 accession_id GCST90246081 pubmed_id 37601966 first_author Walters RG ci_lower 0.872 ci_upper 0.934

> [q101] _embedded.associations[0].reported_trait[0] ICD10 I10: Essential (primary) hypertension

> [q102] _embedded.associations[0].snp_allele[0] rs_id rs1731248 effect_allele C

At the lead (q76-q84): Rosoff 2023's mvAge, A lowers the factor (P 3 × 10⁻⁹), so G is on the healthier-ageing side;
Timmers 2020's multivariate test (P 2 × 10⁻⁸, G named, no effect size); Timmers 2019 (G, +0.26 years). At rs11126666,
whose G pairs with the lead's G (Timmers 2019's own proxy table, pmid-30642433#q48; Pilling's G,
pmid-29227965#q21): G lowers BMI (q85-q87, q94-q96) and A raises it (q88-q90, q97-q99); A raises the use of calcium
channel blockers (q91-q93, P 7 × 10⁻³¹). So the lifespan-shortening A goes with higher BMI and more use of calcium
channel blockers; nothing records harm on the G side among these. The other five records at rs11126666 (angiotensin
receptor blocker response, height, Pilling 2017's parental longevity, two more BMI) were read and add no harm to G. At rs1731248 (q100-q102) C lowers
essential hypertension (OR 0.90, P 5 × 10⁻⁹). C travels with the lead's G (db-opentargets-26.09#q110, q111), and its
risk frequency here (0.29) is the East Asian one, not the European (0.73): an East Asian sample, by frequency. So the
lifespan-raising G goes with less hypertension, in line with A's calcium-channel-blocker record; not a trade-off.

## rs577106756 (PRKD3), for row 13

> [q103] _embedded.associations[0] association_id 165236618 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta 0.09 unit increase p_value 3.0000000000000004e-08 accession_id GCST90551885 pubmed_id 40021682 first_author Park J

> [q104] _embedded.associations[0].reported_trait[0] Lifespan

> [q105] _embedded.associations[0].snp_allele[0] rs_id rs577106756 effect_allele A

> [q106] page size 50 totalElements 1 totalPages 1 number 0

The catalog's one association for rs577106756: Park 2025's men (GCST90551885), "Lifespan", A, β 0.09 "unit
increase", P 3 × 10⁻⁸. The catalog's "increase" is in Park's Martingale residual, which rises with death: the
paper's text (pmid-40021682#q5) says A reduces lifespan. No other trait is recorded for the variant.

## rs980183 (LINC01122), for row 14

> [q107] _embedded.associations[9] association_id 131476574 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0043-0.0084] beta 0.006344008 unit decrease p_value 2e-09 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0043 ci_upper 0.0084

> [q108] _embedded.associations[9].snp_allele[0] rs_id rs980183 effect_allele G

Rosoff 2023's mvAge: G lowers the factor (P 2 × 10⁻⁹), the paper's Table 1 (pmid-37550455#q10).

> [q109] _embedded.associations[11] association_id 62203733 risk_frequency 0.3942 pvalue_description pvalue_mantissa 1 pvalue_exponent -14 multi_snp_haplotype false snp_interaction false range [0.027-0.046] beta 0.0363 unit increase p_value 1e-14 accession_id GCST010555 pubmed_id 32541925 first_author Vujkovic M ci_lower 0.027 ci_upper 0.046

> [q110] _embedded.associations[11].reported_trait[0] Type 2 diabetes

> [q111] _embedded.associations[11].snp_allele[0] rs_id rs980183 effect_allele G

Vujkovic 2020 (the Million Veteran Program): G raises type 2 diabetes risk (β 0.036, P 1 × 10⁻¹⁴, G frequency 0.39).

> [q112] _embedded.associations[0] association_id 228177455 risk_frequency 0.3507 pvalue_description pvalue_mantissa 4 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [0.015-0.027] beta 0.02116 unit increase p_value 4e-12 accession_id GCST90479626 pubmed_id 39024449 first_author Verma A ci_lower 0.015 ci_upper 0.027

> [q113] _embedded.associations[0].reported_trait[0] Glucose (fasting status unknown, mean, inv-norm transformed)

> [q114] _embedded.associations[0].snp_allele[0] rs_id rs980183 effect_allele G

Verma 2024: G raises blood glucose (P 4 × 10⁻¹²).

> [q115] _embedded.associations[10] association_id 93540565 risk_frequency NR pvalue_description pvalue_mantissa 1 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0081-0.0167] beta 0.0124 unit decrease p_value 1e-08 accession_id GCST90018975 pubmed_id 34594039 first_author Sakaue S ci_lower 0.0081 ci_upper 0.0167

> [q116] _embedded.associations[10].reported_trait[0] Triglycerides

> [q117] _embedded.associations[10].snp_allele[0] rs_id rs980183 effect_allele A

Sakaue 2021: A lowers triglycerides (P 1 × 10⁻⁸). At the lead itself the longer-life A lowers type 2 diabetes,
glucose and triglycerides; nine NMR lipid-ratio records (Zoodsma 2025) state A and a tiny percentage. No record at
rs980183 puts harm on A.

## rs78438918 (AFF3), for row 15

> [q118] _embedded.associations[0] association_id 131476527 risk_frequency NR pvalue_description pvalue_mantissa 1 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0052-0.0105] beta 0.007838645 unit decrease p_value 1e-08 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0052 ci_upper 0.0105

> [q119] _embedded.associations[0].snp_allele[0] rs_id rs78438918 effect_allele A

Rosoff 2023's mvAge (GCST90321079): A, β 0.0078 "decrease", P 1 × 10⁻⁸; the paper's Table 1 (pmid-37550455#q11).

> [q120] page size 50 totalElements 1 totalPages 1 number 0

The only association the catalog holds at rs78438918.

## rs117898573 (LRP1B), for row 16

> [q121] _embedded.associations[0] association_id 100037586 risk_frequency 0.029 pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.58-1.2] beta 0.889 unit increase p_value 3.0000000000000004e-08 accession_id GCST90132317 pubmed_id 35927272 first_author Chang X ci_lower 0.58 ci_upper 1.2

> [q122] _embedded.associations[0].snp_allele[0] rs_id rs117898573 effect_allele T

> [q123] page size 50 totalElements 1 totalPages 1 number 0

The catalog's only association at rs117898573: Chang 2022's healthy ageing (GCST90132317), T, P 3 × 10⁻⁸; its
"beta 0.889 unit increase" is the log of the paper's OR 2.433 (pmid-35927272#q2).

## rs10197246 (CASP8 / FLACC1), for row 17

> [q124] _embedded.associations[0] association_id 228297633 risk_frequency 0.2775 pvalue_description pvalue_mantissa 7 pvalue_exponent -32 multi_snp_haplotype false snp_interaction false range [0.078-0.113] beta 0.09548 unit increase p_value 7.000000000000001e-32 accession_id GCST90479794 pubmed_id 39024449 first_author Verma A ci_lower 0.078 ci_upper 0.113

> [q125] _embedded.associations[0].snp_allele[0] rs_id rs10197246 effect_allele T

> [q126] _embedded.associations[1] association_id 228262050 risk_frequency 0.2803 pvalue_description pvalue_mantissa 9 pvalue_exponent -39 multi_snp_haplotype false snp_interaction false range [0.081-0.112] beta 0.09654 unit increase p_value 8.999999999999999e-39 accession_id GCST90475577 pubmed_id 39024449 first_author Verma A ci_lower 0.081 ci_upper 0.112

> [q127] _embedded.associations[2] association_id 131610113 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -6 multi_snp_haplotype false snp_interaction false range [0.045-0.111] beta 0.0780425 unit increase p_value 3e-06 accession_id GCST90428116 pubmed_id 38538606 first_author Harris BHL ci_lower 0.045 ci_upper 0.111

> [q128] _embedded.associations[2].snp_allele[0] rs_id rs10197246 effect_allele C

> [q129] page size 50 totalElements 3 totalPages 1 number 0

The catalog's three associations at rs10197246: Verma et al.'s skin melanoma in two analyses (GCST90479794, P 7 ×
10⁻³²; GCST90475577, P 9 × 10⁻³⁹), T the risk allele; Harris et al.'s breast cancer (GCST90428116, P 3 × 10⁻⁶), C
listed. Zenin's healthspan result is not in this record.

> [q130] _embedded.associations[0] association_id 103236660 risk_frequency 0.389 pvalue_description pvalue_mantissa 3 pvalue_exponent -85 multi_snp_haplotype false snp_interaction false range [0.011-0.014] beta 0.0124 unit increase p_value 2.9999999999999996e-85 accession_id GCST90245848 pubmed_id 36224396 first_author Yengo L ci_lower 0.011 ci_upper 0.014

> [q131] _embedded.associations[0].snp_effect_allele[0] rs1043943-T

> [q132] _embedded.associations[1] association_id 80430607 risk_frequency NR pvalue_description pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.09-0.203] beta 0.1464 unit increase p_value 4e-08 accession_id GCST012210 pubmed_id 33657282 first_author Liu X ci_lower 0.09 ci_upper 0.203

> [q133] _embedded.associations[1].snp_effect_allele[0] rs1043943-T

> [q134] page size 50 totalElements 2 totalPages 1 number 0

The catalog's two associations at rs1043943 (row 18): Yengo et al.'s height (GCST90245848), T +0.0124, P 3 × 10⁻⁸⁵;
Liu et al.'s longevity (GCST012210), T β 0.1464 (CI 0.09 to 0.203), P 4 × 10⁻⁸ (the paper's 3.59 × 10⁻⁸ rounded).

> [q135] _embedded.associations[0] association_id 80754840 risk_frequency 0.0065 pvalue_description pvalue_mantissa 4 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [NR] beta 5.8755207 unit increase p_value 4e-09 accession_id GCST012419 pubmed_id 33948810 first_author Gurinovich A

> [q136] _embedded.associations[0].reported_trait[0] Longevity (100 years and older)

> [q137] _embedded.associations[0].snp_effect_allele[0] rs78043944-A

> [q138] page size 50 totalElements 1 totalPages 1 number 0

The catalog's one association at rs78043944 (row 19): Gurinovich's centenarian GWAS (GCST012419), A, P 4 × 10⁻⁹.
Its "beta 5.8755207 unit increase" is the paper's score Z (pmid-33948810#q4, 5.875520619), not an effect size, and
its risk frequency 0.0065 is the controls' frequency of A. No other trait is recorded for the variant.

> [q139] . initial_sample_size 1,320 European ancestry cases, 2,899 European ancestry controls replication_sample_size 312 Ashkenazi Jewish ancestry cases, 638 Ashkenazi Jewish ancestry controls gxe false gxg false snp_count 9039731 imputed true pooled false accession_id GCST012419 full_summary_stats_available false user_requested false pubmed_id 33948810 platforms Illumina [9039731] (imputed) disease_trait Longevity (100 years and older) full_summary_stats NA terms_of_license https://www.ebi.ac.uk/about/terms-of-use/

Gurinovich's study record (GCST012419): discovery 1,320 cases and 2,899 controls, both of European ancestry, HRC
imputed; replication 312 Ashkenazi cases and 638 controls (the abstract says 480 and about 800, pmid-33948810#q2).
The source of "European" for the NECS sample, the paper's own wording unread. For row 19.

> [q140] _embedded.associations[0].mapped_genes[0] HMGB3P12

> [q141] _embedded.associations[0].mapped_genes[1] VENTXP4

The catalog maps rs78043944 to HMGB3P12 and VENTXP4, where Supplement Table 1 names LINC00692 and LRRC3B. For row 19.

## rs2643826 (SLC4A7), for row 20

> [q142] page size 100 totalElements 63 totalPages 1 number 0

> [q143] _embedded.associations[1] association_id 228386698 risk_frequency 0.5532 pvalue_description pvalue_mantissa 1 pvalue_exponent -32 multi_snp_haplotype false snp_interaction false range [0.026-0.036] beta 0.03113 unit decrease p_value 1e-32 accession_id GCST90476403 pubmed_id 39024449 first_author Verma A ci_lower 0.026 ci_upper 0.036

> [q144] _embedded.associations[1].efo_traits[0] efo_id EFO_0006335 efo_trait systolic blood pressure

> [q145] _embedded.associations[1].snp_effect_allele[0] rs2643826-C

> [q146] _embedded.associations[2] association_id 228382287 risk_frequency 0.4703 pvalue_description pvalue_mantissa 4 pvalue_exponent -16 multi_snp_haplotype false snp_interaction false range [0.039-0.062] beta 0.05067 unit decrease p_value 4e-16 accession_id GCST90480128 pubmed_id 39024449 first_author Verma A ci_lower 0.039 ci_upper 0.062

> [q147] _embedded.associations[2].reported_trait[0] Hypertension (PheCode 401)

> [q148] _embedded.associations[2].snp_effect_allele[0] rs2643826-C

> [q149] _embedded.associations[34] association_id 131771500 risk_frequency NR pvalue_description pvalue_mantissa 6 pvalue_exponent -64 multi_snp_haplotype false snp_interaction false range [0.37-0.47] beta 0.4177 unit increase p_value 6e-64 accession_id GCST90310294 pubmed_id 38689001 first_author Keaton JM ci_lower 0.37 ci_upper 0.47

> [q150] _embedded.associations[34].snp_effect_allele[0] rs2643826-T

> [q151] _embedded.associations[16] association_id 191682993 risk_frequency 0.4404 pvalue_description pvalue_mantissa 4 pvalue_exponent -20 multi_snp_haplotype false snp_interaction false range [0.026-0.04] beta 0.0327 unit increase p_value 4e-20 accession_id GCST90624412 pubmed_id 40645996 first_author Yuan S ci_lower 0.026 ci_upper 0.04

> [q152] _embedded.associations[16].reported_trait[0] Atrial fibrillation

> [q153] _embedded.associations[16].snp_effect_allele[0] rs2643826-T

> [q154] _embedded.associations[12] association_id 228104257 risk_frequency 0.5532 pvalue_description pvalue_mantissa 5 pvalue_exponent -17 multi_snp_haplotype false snp_interaction false range [0.018-0.028] beta 0.02304 unit increase p_value 5.0000000000000005e-17 accession_id GCST90476338 pubmed_id 39024449 first_author Verma A ci_lower 0.018 ci_upper 0.028

> [q155] _embedded.associations[12].reported_trait[0] heart rate (HR, mean, inv-normal transformed)

> [q156] _embedded.associations[12].snp_effect_allele[0] rs2643826-C

> [q157] _embedded.associations[42] association_id 62271267 risk_frequency 0.5533 pvalue_description pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta - p_value 4e-08 accession_id GCST011100 pubmed_id 32678081 first_author Timmers PRHJ

> [q158] _embedded.associations[42].reported_trait[0] Aging traits (healthspan, parental lifespan or longevity) (multivariate analysis)

> [q159] _embedded.associations[42].snp_effect_allele[0] rs2643826-C

> [q160] _embedded.associations[35] association_id 131476408 risk_frequency NR pvalue_description pvalue_mantissa 1 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0043-0.0084] beta 0.006323946 unit increase p_value 1e-09 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0043 ci_upper 0.0084

> [q161] _embedded.associations[35].snp_effect_allele[0] rs2643826-C

> [q162] _embedded.associations[46] association_id 40932334 risk_frequency 0.4571 pvalue_description pvalue_mantissa 3 pvalue_exponent -29 multi_snp_haplotype false snp_interaction false range [0.34-0.48] beta 0.4106 mmHg increase p_value 2.9999999999999997e-29 accession_id GCST007267 pubmed_id 30578418 first_author Giri A ci_lower 0.34 ci_upper 0.48

> [q163] _embedded.associations[46].snp_effect_allele[0] rs2643826-C

The catalog holds 63 associations at rs2643826 (q142), nearly all blood pressure and its treatment. Their direction
is one: C lowers systolic pressure (Verma 2024, β −0.031 SD per C, P 1e-32, q143 to q145, EFO_0006335) and
hypertension (β −0.051, P 4e-16, q146 to q148); T raises systolic pressure by 0.42 mmHg (Keaton 2024, P 6e-64, q149,
q150) and atrial fibrillation (Yuan 2025, P 4e-20, q151 to q153). C raises heart rate slightly (+0.023 SD, P 5e-17,
q154 to q156). The ageing records: Timmers 2020's multivariate healthspan, parental lifespan and longevity, effect
allele C, P 4e-8, no β (q157 to q159), and Rosoff 2023's mvAge, C β +0.0063, P 1e-9 (q160, q161). One record runs
against the rest: Giri 2019's systolic pressure lists C with "0.4106 mmHg increase" at a risk frequency of 0.457
(q162, q163). It conflicts with every other record; whether its allele or its sign is wrong is unknown (0.457 fits T
in Europeans, db-ensembl-116#q92, or C in a mixed sample, as Verma's 0.47 at q146), so it is not read as a direction.

## rs9872864 and rs2271961 (IP6K1), for row 21

> [q164] page size 100 totalElements 2 totalPages 1 number 0

> [q165] _embedded.associations[1] association_id 47749032 risk_frequency NR pvalue_description pvalue_mantissa 7 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range - beta - p_value 7.000000000000001e-10 accession_id GCST009449 pubmed_id 31484785 first_author Wright KM

> [q166] _embedded.associations[1].snp_effect_allele[0] rs9872864-G

rs9872864 has two catalog records. Wright 2019's maternal lifespan (GCST009449): P 7 × 10⁻¹⁰, reported allele G,
no effect size. G is the allele the supplement shows lengthening mothers' lives (pmid-31484785#q52).

> [q167] _embedded.associations[0] association_id 165298819 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta 5.521 z score increase p_value 3.0000000000000004e-08 accession_id GCST90565218 pubmed_id 39192244 first_author Nogawa S

> [q168] _embedded.associations[0].snp_effect_allele[0] rs9872864-A

Nogawa 2024's dental caries: A, z 5.52 "increase", P 3 × 10⁻⁸. Not a disease of lifespan the row reads; stated only.

> [q169] page size 100 totalElements 3 totalPages 1 number 0

> [q170] _embedded.associations[1] association_id 131476397 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0041-0.0081] beta 0.006065845 unit increase p_value 3.0000000000000004e-09 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0041 ci_upper 0.0081

> [q171] _embedded.associations[1].snp_effect_allele[0] rs2271961-T

rs2271961 has three. Rosoff 2023's mvAge (GCST90321079): T, β +0.0061 (95 % CI 0.0041 to 0.0081) "unit increase",
P 3 × 10⁻⁹. On mvAge a higher value is healthier ageing (pmid-37550455#q2), so T is on the healthier side. Rosoff's
cached text does not list rs2271961; this record is the source, as at row 11.

> [q172] _embedded.associations[0] association_id 136813534 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range - beta 0.011 unit decrease p_value 2e-09 accession_id GCST90451690 pubmed_id 39294497 first_author Friligkou E

> [q173] _embedded.associations[0].snp_effect_allele[0] rs2271961-T

> [q174] _embedded.associations[2] association_id 47433890 risk_frequency 0.4957 pvalue_description pvalue_mantissa 9 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0052-0.011] beta 0.0081 unit increase p_value 9e-08 accession_id GCST008529 pubmed_id 31046077 first_author Zhong VW ci_lower 0.0052 ci_upper 0.011

> [q175] _embedded.associations[2].snp_effect_allele[0] rs2271961-C

Friligkou 2024's anxiety disorder: T, β 0.011 "unit decrease", P 2 × 10⁻⁹. Zhong 2019's tea consumption: C, β 0.0081
increase, P 9 × 10⁻⁸ (suggestive). Neither is read as a mechanism.

## Reading 2026-11-11, record

> [q176] _embedded.associations[0] association_id 131476466 risk_frequency NR pvalue_description pvalue_mantissa 7 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0039-0.0079] beta 0.005891484 unit increase p_value 7.000000000000001e-09 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0039 ci_upper 0.0079

> [q177] _embedded.associations[0].snp_effect_allele[0] rs472103-A

rs472103's one record: Rosoff 2023's mvAge (GCST90321079), A, β 0.0059 increase, P 7 × 10⁻⁹. For row 24.

> [q178] _embedded.associations[7] association_id 91631931 risk_frequency 0.4889 pvalue_description pvalue_mantissa 2 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.013-0.026] beta 0.0199 unit decrease p_value 2e-09 accession_id GCST90020053 pubmed_id 34431594 first_author Atkins JL ci_lower 0.013 ci_upper 0.026

> [q179] _embedded.associations[7].snp_effect_allele[0] rs583514-T

rs583514 (GRCh38 3:173,396,377; 26 kb from the lead, r² 0.86, db-ensembl-116#q113): Atkins 2021's frailty index
(GCST90020053, PMID 34431594), T, β 0.0199 decrease, P 2 × 10⁻⁹, risk frequency 0.489. T lowers frailty. T is the
lead's A by frequency (Timmers' file: T 0.487, A 0.466; only that phase fits r² 0.86; derived), and both lengthen
parents' lives there. For row 24.

> [q180] _embedded.associations[0] association_id 227881113 risk_frequency 0.433 pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.017-0.033] beta 0.025 unit decrease p_value 2e-08 accession_id GCST90854295 pubmed_id 42816531 first_author Saito K ci_lower 0.017 ci_upper 0.033

> [q181] _embedded.associations[0].snp_effect_allele[0] rs529200-G

rs529200's type 2 diabetes record from Saito (GCST90854295, PMID 42816531): G, β 0.025 "unit decrease", P 2 × 10⁻⁸.
Read as written, G lowers type 2 diabetes, so the lead's A (rs529200-A's partner, db-ensembl-116#q114, q115, derived)
would raise it: against Open Targets' set led by rs247975 (C raising it, db-opentargets-26.09#q256-q258). The catalog's
other type 2 diabetes record at rs529200 (Suzuki, GCST90492734) prints no β. One record dissents; not resolved here.
For row 24.

## Reading 2026-11-11, record

Row 25 (HTT). associations-rs61348208 (three records), associations-rs16843836 (one), associations-rs82334 (one).

> [q182] _embedded.associations[1] association_id 62271271 risk_frequency 0.3967 pvalue_description  pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta - p_value 3.0000000000000004e-08 accession_id GCST011100 pubmed_id 32678081 first_author Timmers PRHJ

> [q183] _embedded.associations[1].snp_effect_allele[0] rs61348208-T

Timmers 2020's multivariate analysis of healthspan, parental lifespan and longevity (GCST011100): rs61348208 T, P 3 ×
10⁻⁸, no effect size, the same UK Biobank and LifeGen samples as Timmers 2019. The third record at the lead is Salo's
lumbar disc herniation (GCST90837384), P 4 × 10⁻⁷, no allele: below genome-wide, not read.

> [q184] _embedded.associations[0] association_id 131476376 risk_frequency NR pvalue_description  pvalue_mantissa 7 pvalue_exponent -13 multi_snp_haplotype false snp_interaction false range [0.0058-0.0102] beta 0.008003949 unit decrease p_value 7e-13 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0058 ci_upper 0.0102

> [q185] _embedded.associations[0].snp_effect_allele[0] rs16843836-G

Rosoff 2023's mvAge at rs16843836: G, a decrease of 0.0080, P 7 × 10⁻¹³, matching Supplementary Table 6
(pmid-37550455#q21). For row 25.

Row 26 (GPR78). associations-rs7676745: one record.

> [q186] _embedded.associations[0] association_id 47713506 risk_frequency 0.96 pvalue_description  pvalue_mantissa 2 pvalue_exponent -7 multi_snp_haplotype false snp_interaction false range [1.28-1.72] or_per_copy_num 1.4925373 or_value 1.4925373 beta - p_value 2e-07 accession_id GCST008600 pubmed_id 31413261 first_author Deelen J ci_lower 1.28 ci_upper 1.72

> [q187] _embedded.associations[0].snp_effect_allele[0] rs7676745-G

> [q188] page size 50 totalElements 1 totalPages 1 number 0

The Catalog's only association for rs7676745 is Deelen 2019's trans-ethnic 90th percentile result (GCST008600,
P 2e-7, OR 1.49 per G, the inverse of Table 4's 0.67 per A; pmid-31413261#q62), not the European discovery's 4.3e-8.
No other trait is recorded for the variant. For row 26.

## Reading 2026-11-11, record

> [q189] _embedded.associations[3] association_id 131476387 risk_frequency NR pvalue_description pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0036-0.0077] beta 0.00564864 unit decrease p_value 4e-08 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB

> [q190] _embedded.associations[3].snp_effect_allele[0] rs17499404-G

> [q191] _embedded.associations[4] association_id 62271276 risk_frequency 0.5367 pvalue_description pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta - p_value 4e-08 accession_id GCST011100 pubmed_id 32678081 first_author Timmers PRHJ

> [q192] _embedded.associations[4].snp_effect_allele[0] rs17499404-A

> [q193] _embedded.associations[0].reported_trait[0] Blood cell traits latent factor 9 (white cell)

> [q194] page size 50 totalElements 5 totalPages 1 number 0

Row 27 (LINC02513). associations-rs17499404: five records. Rosoff 2023's mvAge (G "unit decrease", P 4e-8;
q189, q190) and Timmers 2020's multivariate scan (A, P 4e-8; q191, q192); Shi 2024's systolic (P 7e-18) and
diastolic (P 1e-12) pressure, allele unstated (their direction is read from Open Targets' sets led by the variant,
db-opentargets-26.09#q416-q421); a white-cell latent factor (Zhou 2025, P 6e-10, allele unstated; q193).

## Reading 2026-11-11, record

> [q195] _embedded.associations[0] association_id 131476424 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0041-0.0085] beta 0.006329202 unit increase p_value 2e-08 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB

> [q196] _embedded.associations[0].snp_effect_allele[0] rs28637671-T

> [q197] page size 50 totalElements 1 totalPages 1 number 0

Row 28. associations-rs28637671: one record, Rosoff 2023's mvAge (T "unit increase", P 2e-8; q195, q196, q197).
No other trait is recorded for the variant. rs13141210 (associations-rs13141210): mvAge (P 1e-8) and cigarettes per
day (Koskeridis 2022, MTAG, P 3e-11).

## Reading 2026-11-11, record

> [q198] _embedded.associations[0] association_id 217740303 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -6 multi_snp_haplotype false snp_interaction false range - beta - p_value 2e-06 accession_id GCST90837384 pubmed_id 39511132 first_author Salo V

> [q199] _embedded.associations[0].efo_traits[0] efo_id EFO_1002005 efo_trait lumbar disc herniation

Row 28. The 54 variants at r² 0.8 or more to rs28637671 (db-ensembl-116, `ldwin-rs28637671.json`), and rs1481245,
queried one by one (`associations-<rsID>.json`): 54 return no record (totalElements 0). rs28494793 (r² 0.93) has one,
Salo 2024's lumbar disc herniation, P 2e-6, allele unstated (q198, q199): short of genome-wide, so no trait is
recorded at the lead's proxies.

## Reading 2026-11-11, record

> [q200] association_id 131476445 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0039-0.008] beta 0.005953217 unit decrease p_value 2e-08 accession_id GCST90321079 pubmed_id 37550455

> [q201] _embedded.associations[0].snp_effect_allele[0] rs36072649-T

> [q202] association_id 63950010 risk_frequency NR pvalue_description pvalue_mantissa 1 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [NR] or_per_copy_num 0.978 or_value 0.978 beta - p_value 1e-09 accession_id GCST011703 pubmed_id 33082346

> [q203] _embedded.associations[1].snp_effect_allele[0] rs36072649-A

> [q204] _embedded.associations[1].reported_trait[0] Smoking initiation

GWAS Catalog (2026-10-29), associations-rs36072649.json, two records. mvAge (Rosoff 2023, GCST90321079): T, β
0.00595 "unit decrease", P 2e-8 (q200, q201), anchoring T as the allele lowering the factor. Smoking initiation
(PMID 33082346, GCST011703): A, OR 0.978, P 1e-9 (q202-q204): the lead's A, the healthier-ageing allele, lowers
smoking initiation, at the lead itself. For row 29.

## Reading 2026-11-11, record

> [q205] _embedded.associations[0] association_id 80754852 risk_frequency 0.6394 pvalue_description pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [NR] beta 5.5010357 unit decrease p_value 4e-08 accession_id GCST012419 pubmed_id 33948810 first_author Gurinovich A

> [q206] _embedded.associations[0].reported_trait[0] Longevity (100 years and older)

> [q207] page size 50 totalElements 1 totalPages 1 number 0

rs649357: one association in the catalog (q207), Gurinovich 2021 (GCST012419), "Longevity (100 years and older)"
(q206), P 4e-8, risk frequency 0.6394 (NECS controls' C), "beta 5.5010357 unit decrease" (q205): the score Z, with
C the risk allele, as at row 19. Its 56 proxies at r² ≥ 0.8 (`associations-<rsID>.json`, queried one by one)
return no record (totalElements 0). No other trait is recorded on the haplotype. For row 31.

## Reading 2026-11-11, record

> [q208] range [0.76-1.54] beta 1.15 unit increase p_value 5e-09 accession_id GCST90132317 pubmed_id 35927272

> [q209] _embedded.associations[0].reported_trait[0] Healthy aging

> [q210] _embedded.associations[0].snp_effect_allele[0] rs138499810-T

> [q211] _links.self href https://www.ebi.ac.uk/gwas/rest/api/v2/associations?rs_id=rs138499810&page=0&size=50 page size 50 totalElements 1 totalPages 1 number 0

rs138499810 (`associations-rs138499810.json`): one record, Chang 2022's healthy ageing (q209), T (q210), P 5e-9,
"beta 1.15" with range 0.76 to 1.54 (q208), the only record (q211): the natural log of the paper's OR 3.158 and its CI (2.148 to 4.643), not
a separate estimate. No other trait on the variant. For row 32.

## Reading 2026-11-11, record

> [q212] _embedded.associations[1] association_id 40556 risk_frequency 0.352 pvalue_description  pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [1.06-1.74] or_per_copy_num 1.1 or_value 1.1 beta - p_value 2e-08 accession_id GCST002404 pubmed_id 24688116 first_author Deelen J ci_lower 1.06 ci_upper 1.74

> [q213] page size 100 totalElements 2 totalPages 1 number 0

rs2149954 (`associations-rs2149954.json`): two associations, both Deelen 2014 (q213): ≥85 (GCST002403, OR 1.07, P 4e-6)
and ≥90 (GCST002404, OR 1.1, P 2e-8, q212). The Catalog's CI 1.06 to 1.74 disagrees with the paper's 1.06 to 1.14
(pmid-24688116#q4); the paper is read. No other trait is recorded on this rsID; the blood-pressure results sit on
proxies (Deelen's rs9313772 and rs11953630) and in Open Targets' sets. For row 33.

## Reading 2026-11-11, record

> [q214] _embedded.associations[17] association_id 228300609 risk_frequency 0.8723 pvalue_description  pvalue_mantissa 1 pvalue_exponent -207 multi_snp_haplotype false snp_interaction false range [0.44-0.48] beta 0.461 unit decrease p_value 1e-207 accession_id GCST90479796 pubmed_id 39024449 first_author Verma A ci_lower 0.44 ci_upper 0.48

> [q215] _embedded.associations[17].reported_trait[0] Squamous cell carcinoma (PheCode 172.22)

> [q216] _embedded.associations[17].snp_effect_allele[0] rs12203592-C

> [q217] _embedded.associations[37] association_id 131476324 risk_frequency NR pvalue_description  pvalue_mantissa 7 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [0.0077-0.0139] beta 0.010844371 unit increase p_value 7e-12 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0077 ci_upper 0.0139

> [q218] _embedded.associations[37].snp_effect_allele[0] rs12203592-C

> [q219] _embedded.associations[72] association_id 62271280 risk_frequency 0.81 pvalue_description  pvalue_mantissa 8 pvalue_exponent -26 multi_snp_haplotype false snp_interaction false range - beta - p_value 8e-26 accession_id GCST011100 pubmed_id 32678081 first_author Timmers PRHJ

> [q220] _embedded.associations[25] association_id 18400 risk_frequency 0.19 pvalue_description  pvalue_mantissa 6 pvalue_exponent -15 multi_snp_haplotype false snp_interaction false range [1.34-1.63] or_per_copy_num 1.48 or_value 1.48 beta - p_value 6.0000000000000005e-15 accession_id GCST001116 pubmed_id 21685912 first_author Hoglinger GU ci_lower 1.34 ci_upper 1.63

> [q221] _embedded.associations[25].snp_effect_allele[0] rs12203592-?

rs12203592's 232 associations over three pages (`associations-rs12203592.json`, `-p1`, `-p2`). From the first file: Verma's UK Biobank
and Million Veteran phenome-wide skin cancer results put C on the lower side: squamous cell carcinoma β 0.461 "unit
decrease" per C, P 10⁻²⁰⁷ (q214 to q216), and the same shape for basal cell carcinoma, melanoma and skin cancer in the same
file (rows 15, 20, 22). From `-p1`: Rosoff 2023's mvAge, C "unit increase", 0.0108, P 7 × 10⁻¹² (q217, q218). Timmers 2020's
multivariate ageing GWAS: C at 0.81, P 8 × 10⁻²⁶, no beta or direction (q219). From `-p2`: Höglinger 2011's progressive
supranuclear palsy: OR 1.48 at P 6 × 10⁻¹⁵, the allele unstated (q220, q221; the frequency 0.19 would fit T, not
read as such). The Catalog holds no association from Zenin 2019 for this SNP. For row 35.

## Reading 2026-11-11, record

> [q222] _embedded.associations[46] association_id 104179443 risk_frequency 0.14065 pvalue_description  pvalue_mantissa 7 pvalue_exponent -40 multi_snp_haplotype false snp_interaction false range [0.39-0.53] beta 0.458651 unit increase p_value 6.9999999999999995e-40 accession_id GCST90255685 pubmed_id 36672889 first_author Farre X

> [q223] _embedded.associations[46].reported_trait[0] Freckles

> [q224] _embedded.associations[46].snp_effect_allele[0] rs12203592-T

In `associations-rs12203592-p1.json` (the second page): Farré's freckles, T "unit increase", β 0.459, P 7 × 10⁻⁴⁰
(q222 to q224). T goes with more freckling. For row 35.

## Reading 2026-11-11, record

> [q225] beta 0.004 unit increase p_value 3.0000000000000004e-08 accession_id GCST90551884 pubmed_id 40021682 first_author Park J

> [q226] _embedded.associations[1].snp_effect_allele[0] rs6902687-C

> [q227] _embedded.associations[0] association_id 191005407 risk_frequency NR pvalue_description  pvalue_mantissa 6 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range - beta - 

> [q228] _embedded.associations[0].reported_trait[0] Blood cell traits latent factor 2 (red cell)

The Catalog's two associations at rs6902687 (`associations-rs6902687.json`, totalElements 2): Park 2025's lifespan,
C, β 0.004 "increase", P 3e-8 (q225, q226); and Zhou 2025's blood-cell latent factor 2 (red cell), P 6e-10, effect
allele "?" (q227, q228). No other lifespan, longevity or healthspan study. For row 36.

## Reading 2026-11-11, record

> [q229] _embedded.associations[1] association_id 35567711 risk_frequency 0.72 pvalue_description  pvalue_mantissa 2 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range [0.011-0.02] beta 0.0155 unit decrease p_value 2e-10 accession_id GCST006696 pubmed_id 29227965 first_author Pilling LC

> [q230] _embedded.associations[1].snp_effect_allele[0] rs3130507-G

The Catalog's two associations at rs3130507 (`associations-rs3130507.json`, totalElements 2): Pilling 2017's mothers'
attained age, G, β 0.0155 "decrease" (the Martingale residual, so longer-lived), P 2 × 10⁻¹⁰ (q229, q230), and
Pilling's combined parents (P 4 × 10⁻⁶). No other trait at the lead itself. For row 37.

> [q231] _embedded.associations[0] association_id 45627116 risk_frequency NR pvalue_description  pvalue_mantissa 1 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range [1.62‐2.45] or_per_copy_num 2.0 or_value 2.0 beta - p_value 1e-10 accession_id GCST008096 pubmed_id 30921485 first_author Bejaoui Y

> [q232] _embedded.associations[0].reported_trait[0] Psoriasis

> [q233] _embedded.associations[0].snp_effect_allele[0] rs1265181-?

At rs1265181, r² 0.81 to row 37's lead in CEU (the window listing): psoriasis, OR 2.0, P 1 × 10⁻¹⁰, Bejaoui 2019, risk
allele not given (q231 to q233), in an Egyptian sample (q239). Of the lead's 71 proxies at r² ≥ 0.8, 14 have Catalog
records (each cached 2026-11-11, `associations-<rsid>.json`): psoriasis at six (rs6933647, rs3130455, rs3130467,
rs1265181, rs3130517, rs130076), every one in a sample that is not European or whose ancestry is not reported
(Bejaoui, Egypt; Yang, Taiwan; Zhang 2009, China; Lee's SNP-interaction lines, ancestry NR: the study records
`study-GCST008096`, `-GCST90435380`, `-GCST000321`, `-GCST007023`), so a CEU r² does not carry them to this signal and
no psoriasis link is read. The others: immune-protein levels (HMOX1, IL-12/LAG3, beta-2-microglobulin, IL-12B),
sarcoidosis, membranous nephropathy (q236 to q238), HIV set-point viral load, EBV copy number, hepatitis B vaccine
response, HDL cholesterol and waist-to-hip ratio, once or twice each. For row 37.

> [q234] _embedded.associations[0] association_id 165704410 risk_frequency NR pvalue_description  pvalue_mantissa 2 pvalue_exponent -13 multi_snp_haplotype false snp_interaction false range - beta - p_value 2e-13 accession_id GCST90302862 pubmed_id 37377963 first_author Wen YP

> [q235] _embedded.associations[0].reported_trait[0] Rheumatoid arthritis or inflammatory bowel disease

At the seed's other rsID rs3131621 (`associations-rs3131621.json`, totalElements 4): rheumatoid arthritis or
inflammatory bowel disease, P 2 × 10⁻¹³, allele "?" (q234, q235), beside Wright's fathers (P 9 × 10⁻⁹) and Pilling's
fathers and combined parents. For row 37's prose and the scout queue.

## Reading 2026-11-11, record

> [q236] _embedded.associations[1] association_id 10071455 risk_frequency 0.2191 pvalue_description  pvalue_mantissa 4 pvalue_exponent -37 multi_snp_haplotype false snp_interaction false range [NR] or_per_copy_num 2.42 or_value 2.42 beta - p_value 4e-37 accession_id GCST000984 pubmed_id 21323541 first_author Stanescu HC

> [q237] _embedded.associations[1].reported_trait[0] Idiopathic membranous nephropathy

> [q238] _embedded.associations[1].snp_effect_allele[0] rs1265159-T

> [q239] discovery_ancestry[0] 631 Greater Middle Eastern (Middle Eastern, North African or Persian) (Egypt)

> [q240] discovery_ancestry[0] 2894 European (France, Netherlands, U.K.)

At rs1265159, row 37's tag (r² 0.83, D′ 1, db-ensembl-116#q244): idiopathic membranous nephropathy, risk allele T
(0.219), OR 2.42, P 4 × 10⁻³⁷, Stanescu 2011 (q236 to q238), in a European sample from France, the Netherlands and
the UK (`study-GCST000984.json`, q240). Phase, derived: with T at about 0.22 and the lead's A at 0.28 (q247 of the
Ensembl note), D′ 1 and r² 0.83 fit only T on the A haplotype (r² about 0.86; the other phase gives at most 0.11). So
the nephropathy risk allele travels with the lead's shorter-lived A: the same side, no trade-off. q239 is Bejaoui
2019's psoriasis sample (`study-GCST008096.json`), Egyptian. For row 37.

## Reading 2026-11-11, record

> [q241] risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0069-0.0135] beta 0.010191999 unit increase p_value 2e-09 accession_id GCST90321079

> [q242] _embedded.associations[22].reported_trait[0] Aging

> [q243] _embedded.associations[22].snp_effect_allele[0] rs6907508-A

> [q244] risk_frequency 0.884473 pvalue_description pvalue_mantissa 2 pvalue_exponent -17 multi_snp_haplotype false snp_interaction false range [0.021-0.034] beta 0.0276231 unit increase p_value 2e-17 accession_id GCST010243

> [q245] _embedded.associations[28].reported_trait[0] Apolipoprotein B levels

> [q246] _embedded.associations[28].snp_effect_allele[0] rs6907508-A

> [q247] risk_frequency NR pvalue_description pvalue_mantissa 7 pvalue_exponent -21 multi_snp_haplotype false snp_interaction false range [0.027-0.041] beta 0.0339 unit decrease p_value 6.999999999999999e-21 accession_id GCST90018974

> [q248] _embedded.associations[24].reported_trait[0] Total cholesterol levels

> [q249] _embedded.associations[24].snp_effect_allele[0] rs6907508-G

> [q250] risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -24 multi_snp_haplotype false snp_interaction false range [0.03-0.03] beta 0.03 mmol/L increase p_value 2e-24 accession_id GCST90501278

> [q251] _embedded.associations[6].reported_trait[0] Total free cholesterol levels

> [q252] _embedded.associations[6].snp_effect_allele[0] rs6907508-G

> [q253] risk_frequency 0.1632 pvalue_description pvalue_mantissa 3 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range [0.0068-0.0129] beta 0.00984 unit increase p_value 3e-10 accession_id GCST90668013

> [q254] _embedded.associations[0].reported_trait[0] Heart failure (MTAG)

> [q255] _embedded.associations[0].snp_effect_allele[0] rs2492863-A

> [q256] risk_frequency 0.166 pvalue_description pvalue_mantissa 2 pvalue_exponent -11 multi_snp_haplotype false snp_interaction false range - beta 6.6832886 z-score increase p_value 2e-11 accession_id GCST90668077

> [q257] _embedded.associations[0].reported_trait[0] Heart failure (MTAG)

> [q258] _embedded.associations[0].snp_effect_allele[0] rs2814948-A

> [q259] risk_frequency 0.1342 pvalue_description pvalue_mantissa 5 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.034-0.068] beta 0.0507 unit increase p_value 5e-09 accession_id GCST90244158

> [q260] _embedded.associations[1].reported_trait[0] Venous thromboembolism

> [q261] _embedded.associations[1].snp_effect_allele[0] rs145294670-A

> [q262] risk_frequency 0.11 pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [1.13-1.28] or_per_copy_num 1.2 or_value 1.2 beta - p_value 2e-08 accession_id GCST004146

> [q263] _embedded.associations[20].reported_trait[0] Chronic lymphocytic leukemia

> [q264] _embedded.associations[20].snp_effect_allele[0] rs3800461-C

> [q265] risk_frequency 0.1431 pvalue_description pvalue_mantissa 1 pvalue_exponent -11 multi_snp_haplotype false snp_interaction false range [0.044-0.078] beta 0.061 unit increase p_value 1e-11 accession_id GCST005196

> [q266] _embedded.associations[2].reported_trait[0] Coronary artery disease

> [q267] _embedded.associations[2].snp_effect_allele[0] rs2814993-A

> [q268] discovery_ancestry[0] 1366492 European (Finland, U.K., U.S.)

> [q269] discovery_ancestry[0] 762151 European (NR)

> [q270] discovery_ancestry[0] 1066917 European (Estonia, Finland, France, NR, Netherlands, Norway, Spain, U.K., U.S.)

> [q271] discovery_ancestry[0] 17691 European (Australia, NR, U.K., U.S.)

> [q272] discovery_ancestry[0] 250736 NR (NR, U.K.)

`associations-rs6907508.json` holds 42 associations. mvAge (GCST90321079): rs6907508-A, "unit increase", P 2e-9
(q241 to q243). Apolipoprotein B (GCST010243): A, risk frequency 0.88, "unit increase", P 2e-17 (q244 to q246); total
cholesterol (GCST90018974): G "unit decrease", P 7e-21 (q247 to q249): A raises both, as Open Targets' sets give
(db-opentargets-26.09). A sign conflict: the batch of NMR-metabolite lines GCST90501xxx prints G "increase" (total
free cholesterol, GCST90501278, q250 to q252; sphingomyelins, fatty acids, very small VLDL likewise), where Open
Targets' set for the same accession gives β −0.0324 per G with rs6907508 leading it, and every other record agrees
with Open Targets. Those lines are not read for direction.

The proxy sweep over the 35 SNPs at r² ≥ 0.8 (Ensembl's CEU window, db-ensembl-116#q250 onward): 24 have records,
146 associations, most of them lipids, body size and liver enzymes. Read here, each on the minor allele that travels
with the lead's G (D′ 1, frequencies; derived), each study's ancestry from its cached record:
- heart failure (MTAG, boosted by heart-function traits; GCST90668013, European, q268):
  rs2492863-A, risk frequency 0.16, "increase", P 3e-10 (q253 to q255); and GCST90668077 (European, q269):
  rs2814948-A, 0.17, z 6.68, P 2e-11 (q256 to q258); both r² 0.83 (db-ensembl-116#q259, q260);
- venous thromboembolism (GCST90244158, European, 7,177 cases, q270): rs145294670-A, 0.13, β 0.0507
  "increase", P 5e-9 (q259 to q261), r² 1.00 (db-ensembl-116#q257);
- chronic lymphocytic leukaemia (GCST004146, European, 4,478 cases, q271): rs3800461-C, 0.11, OR 1.2,
  P 2e-8 (q262 to q264), r² 1.00 (db-ensembl-116#q258).
Coronary artery disease at rs2814993-A (0.14, "increase", P 1e-11, q265 to q267; r² 0.83) and at rs2814944 (r² 0.76)
comes from studies whose ancestry the catalog leaves unreported (GCST005196, q272; GCST005195 likewise):
not read, as at row 37. So the shorter-lived G's haplotype goes with more heart failure, thrombosis and CLL, and
with lower LDL and apolipoprotein B. For row 39.

## rs7742789 (ZNF318 / ABCC10), for row 40

> [q273] _embedded.associations[15] association_id 131476521 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0039-0.0082] beta 0.006035937 unit increase p_value 3.0000000000000004e-08 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB

> [q274] _embedded.associations[15].snp_effect_allele[0] rs7742789-C

> [q275] discovery_ancestry[0] 398696 European (U.K.)

> [q276] discovery_ancestry[3] 1893921 European (Canada, Denmark, Estonia, Germany, Iceland, Japan, Netherlands, Sweden, U.K., U.S.)

> [q277] discovery_ancestry[2] 2212177 European (Finland, Iceland, NR, Norway, Sweden, U.K., U.S.)

> [q278] discovery_ancestry[0] 322141 European (U.K.)

> [q279] discovery_ancestry[1] 400940 European (U.K.)

> [q280] discovery_ancestry[0] 406504 European (U.K.)

> [q281] discovery_ancestry[0] 417274 European (U.S.)

> [q282] discovery_ancestry[0] 425203 European (U.S.)

The catalog's 19 associations for rs7742789 (`associations-rs7742789.json`) include Rosoff 2023's mvAge line,
rs7742789-C "unit increase", P 3 × 10⁻⁸ (q273, q274), which anchors the counted allele, and no lifespan, longevity or
mortality study; nor do its 15 proxies at r² ≥ 0.8 (`associations-<rsID>.json`, 111 lines, most of them blood
pressure, then testosterone, urate, kidney function and platelets; the only other disease lines stroke,
cardiovascular disease, heart failure and atrial fibrillation). The studies of the Open Targets sets row 40 reads
(`study-<accession>.json`), each with a European arm: clonal haematopoiesis with a DNMT3A mutation GCST90435354
(398,696 Europeans, U.K., q275); heart failure GCST90455657 (multi-ancestry, 1,893,921 Europeans among them, q276);
atrial fibrillation GCST90624411 (multi-ancestry, 2,212,177 Europeans, q277); systolic blood pressure GCST90472780
(322,141, U.K., q278); cystatin C GCST90692779 (400,940 Europeans among U.K. samples, q279); eGFR from creatinine and
cystatin C GCST90428446 (406,504, U.K., q280); ischaemic heart disease GCST90475929 (417,274, U.S., q281); acute
renal failure GCST90476119 (425,203, U.S., q282). The variant's own sets, read at the lead, need no phasing.

## Reading 2026-11-11, record

Row 40's sign anchors and the kidney-disease studies (`associations-rs7742789.json`, `study-<accession>.json`).

> [q283] _embedded.associations[2] association_id 228333544 risk_frequency 0.695 pvalue_description pvalue_mantissa 2 pvalue_exponent -13 multi_snp_haplotype false snp_interaction false range [0.04-0.072] beta 0.05589 unit decrease p_value 2e-13 accession_id GCST90476119

> [q284] _embedded.associations[2].snp_effect_allele[0] rs7742789-C

> [q285] _embedded.associations[5] association_id 228262091 risk_frequency 0.6933 pvalue_description pvalue_mantissa 2 pvalue_exponent -35 multi_snp_haplotype false snp_interaction false range [0.046-0.064] beta 0.05486 unit increase p_value 2e-35 accession_id GCST90475480

> [q286] _embedded.associations[5].snp_effect_allele[0] rs7742789-C

> [q287] discovery_ancestry[0] 447143 European (U.S.)

> [q288] discovery_ancestry[0] 448588 European (U.S.)

> [q289] discovery_ancestry[0] 445574 European (U.S.)

Acute renal failure (GCST90476119): rs7742789-C "decrease", P 2 × 10⁻¹³ (q283, q284); serum magnesium (GCST90475480):
C "increase", P 2 × 10⁻³⁵ (q285, q286). Open Targets' SuSiE-inf sets for the same accessions give T the opposite
signs, so its `beta` there is per T. The three chronic kidney disease studies of MVP, each with African-American and
Hispanic arms beside the European: GCST90480387 (447,143 Europeans, q287), GCST90480386 (448,588, q288), GCST90479971
(445,574, q289). The proxies' lines row 40 names only (stroke, hypertension, testosterone, urate) were not checked for
ancestry; some are Japanese (Kanai 2018's blood pressure at rs16896398, a uric-acid line from 1KG-JEWEL7K). For row 40.

## Reading 2026-11-11, record

> [q290] _embedded.associations[0] association_id 80754848 risk_frequency 4.0E-4 pvalue_description pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [NR] beta 5.5104795 unit increase p_value 4e-08 accession_id GCST012419 pubmed_id 33948810 first_author Gurinovich A

> [q291] _embedded.associations[0].snp_effect_allele[0] rs114658003-A

> [q292] page size 100 totalElements 1 totalPages 1 number 0

rs114658003: one association in the catalog, Gurinovich 2021's (GCST012419, Longevity (100 years and older)),
A "increase", P 4 × 10⁻⁸ (q290, q291). Its "beta 5.5104795" is the paper's score Z (pmid-33948810#q22), and its
risk frequency 4.0E-4 is NECS's controls' A. No other trait is recorded (q292). For row 41.

## Reading 2026-11-11, record

> [q293] _embedded.associations[0].reported_trait[0] Parental longevity (both parents in top 10%)

> [q294] _embedded.associations[1] association_id 35691727 risk_frequency 0.684 pvalue_description  pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.013-0.027] beta 0.0197 unit increase p_value 4e-08 accession_id GCST006702 pubmed_id 29227965 first_author Pilling LC ci_lower 0.013 ci_upper 0.027

> [q295] page size 100 totalElements 2 totalPages 1 number 0

> [q296] page size 100 totalElements 0 totalPages 0 number 0

rs1627804: two associations, both Pilling 2017's (q295). Parents' age at death, C β +0.0197, P 4 × 10⁻⁸ (GCST006702,
q294), and both parents in the top 10 %, P 5 × 10⁻⁶ (GCST006698, q293), which records C as the effect allele but no
estimate ("beta -"), so the top-10 % result has no direction here. No other trait. Its eleven proxies at r² ≥ 0.8
(db-ensembl-116#q285 and the reading there) hold no association at all: each query returns q296's empty page (one
cached file per rsID, `associations-<rsid>.json`). For row 42.

## Reading 2026-11-11, record

> [q297] _embedded.associations[0].efo_traits[0] efo_id EFO_0007984 efo_trait platelet component distribution width

> [q298] page size 100 totalElements 1 totalPages 1 number 0

rs2802292: one association in the catalog (q298), platelet distribution width (q297; Vuckovic 2020, T, P 2 ×
10⁻²¹). No longevity or lifespan entry: Broer's pooled result is not catalogued at this SNP. For row 43.

## Reading 2026-11-11, record

> [q299] _embedded.associations[0] association_id 218978004 risk_frequency 0.367722 pvalue_description pvalue_mantissa 7 pvalue_exponent -14 multi_snp_haplotype false snp_interaction false range - beta 0.0250543 unit decrease p_value 7e-14 accession_id GCST90832687 pubmed_id 42092107 first_author Dong X

> [q300] _embedded.associations[3] association_id 55479331 risk_frequency NR pvalue_description pvalue_mantissa 6 pvalue_exponent -6 multi_snp_haplotype false snp_interaction false range [0.0055-0.0137] beta 0.009596 unit increase p_value 6e-06 accession_id GCST009448 pubmed_id 31484785 first_author Wright KM ci_lower 0.0055 ci_upper 0.0137

> [q301] _embedded.associations[1].snp_effect_allele[0] rs6911407-?

rs6911407 (r² 0.98 with row 43's lead, its A with G): four associations (`assoc-rs6911407.json`). Fluid
intelligence (Dong, GCST90832687), A, β 0.025 decrease, P 7 × 10⁻¹⁴ (q299): G's side has slightly lower fluid
intelligence. Longevity (Wright 2019's AncestryDNA, GCST009448), A, β 0.0096 increase, P 6 × 10⁻⁶ (q300). Foote
2025's frailty factor 5 ("Poorer Cognition", P 4 × 10⁻¹⁰) with no effect allele (q301), and a multi-trait sex score.
For row 43.

## Reading 2026-11-11, record

> [q302] page size 100 totalElements 0 totalPages 0 number 0

The catalog's associations for rs76888380 (`assoc-rs76888380.json`): none (q302). Park 2025 reported no 6q22.31
locus (pmid-40021682#q40), and the catalog holds nothing else at the variant.

## Reading 2026-11-11, record

> [q303] page size 100 totalElements 4 totalPages 1 number 0

> [q304] or_value 1.12 beta - p_value 1e-06 accession_id GCST008600 pubmed_id 31413261 first_author Deelen J

> [q305] _embedded.associations[1].snp_effect_allele[0] rs1262476-A

> [q306] beta 0.104 unit increase p_value 3.0000000000000004e-09 accession_id GCST002496 pubmed_id 24945404 first_author Kemp JP

> [q307] _embedded.associations[3].snp_effect_allele[0] rs1262476-G

> [q308] _embedded.associations[3].reported_trait[0] Bone mineral density (paediatric, upper limb)

> [q309] _embedded.associations[0].reported_trait[0] Attention deficit hyperactivity disorder or autism spectrum disorder or intelligence (pleiotropy)

> [q310] _embedded.associations[0].snp_effect_allele[0] rs1262476-?

The catalog's associations for rs1262476 (`assoc-rs1262476.json`): four (q303). Deelen 2019's trans-ethnic 90th
percentile record (GCST008600), A OR 1.12, P 1e-6 (q304, q305; pmid-31413261#q110). Kemp 2014's paediatric upper-limb
bone density (ALSPAC and Generation R, about 9,400 children; GCST002496), G β +0.104 (unit increase), P 3e-9 (q306 to q308), and a
second line at P 4e-8: so A, the longer-life allele, goes with lower bone density in children. Rao 2022's ADHD,
autism or intelligence pleiotropy scan (title-checked 2026-11-11: "Genetic Relationships between
Attention-Deficit/Hyperactivity Disorder, Autism Spectrum Disorder, and Intelligence."), P 9e-9, no allele (q309 to
q311). For row 45.

> [q311] accession_id GCST90134330 pubmed_id 35764056 first_author Rao S

> [q312] initial_sample_size 11,262 European ancestry cases, 2,178 East Asian ancestry cases, 177 African American cases, 25,483 European ancestry controls, 2,299 East Asian ancestry controls, 211 African American controls.

> [q313] full_summary_stats_available false

The catalog's study record for Deelen's trans-ethnic 90th percentile analysis (`study-GCST008600.json`): 11,262
European, 2,178 East Asian and 177 African American cases against 25,483, 2,299 and 211 controls (q312), so about
17 % of the cases are not European; no summary statistics deposited (q313; the FTP directory answers 404). For
row 45.

## Reading 2026-11-11, record

> [q314] risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.01-0.021] beta 0.01577 unit decrease p_value 3.0000000000000004e-08 accession_id GCST003395 pubmed_id 27015805

> [q315] snp_effect_allele[0] rs528161076-?

> [q316] totalElements 1 totalPages 1

> [q317] initial_sample_size 1,339 middle-aged British cases, 40,934 middle-aged British controls replication_sample_size NA

The catalog's one association for rs528161076 (`assoc-rs528161076.json`, q316): Pilling 2016's GCST003395, "Parental
extreme longevity (95 years and older)", P 3e-8, β 0.01577 "unit decrease" with the effect allele unrecorded (q315):
Supplementary Table 2's β per T (pmid-27015805#q13), its sign folded into the unit. The study record
(`study-GCST003395.json`): 1,339 British cases and 40,934 controls, no replication sample (q317). No other trait is
recorded for the variant. For row 47.

> [q318] page size 100 totalElements 0 totalPages 0 number 0

The same query under the surviving id rs371933919 (`assoc-rs371933919.json`) and under Pilling's proxy rs79109928
(`assoc-rs79109928.json`) each returns this line: no association under either. For row 47.

## Reading 2026-11-11, record

> [q319] _embedded.associations[0] association_id 80430573 risk_frequency NR

> [q320] _embedded.associations[0].snp_allele[0] rs_id rs17169634 effect_allele G

> [q321] _embedded.associations[1] association_id 42691 risk_frequency NR pvalue_description  pvalue_mantissa 1 pvalue_exponent -7

rs17169634's associations (`assoc-rs17169634`): Liu 2021 (GCST012210, β 0.3084 per G, P 8e-15), with no risk-allele
frequency (q319, q320); and Nelson 2014's (GCST002429, P 1e-7, q321), the Alzheimer's report Liu cites
(pmid-33657282#q18), its allele "?". For row 49.

## Reading 2026-11-11, supplement

> [q322] beta 0.006039821 unit decrease p_value 9.000000000000001e-09 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB

> [q323] beta 0.0334 unit increase p_value 1e-10 accession_id GCST90275136 pubmed_id 37689771 first_author Pedersen EM

> [q324] beta 0.017676765 unit increase p_value 6.000000000000001e-09 accession_id GCST90245879 pubmed_id 32587327 first_author Tsepilov YA

Row 50's FOXP2 lead (`assoc-rs12705966`): three associations. Rosoff's mvAge, rs12705966-A, decrease (q322); Pedersen's
ADHD (ADuLT model adjusted for sex), the allele printed "?" (q323); Tsepilov's genetically independent pain factor,
rs12705966-A, increase (q324), so G lowers it, as Open Targets' set has it (db-opentargets-26.09#q644). For row 50.

## Reading 2026-11-11, supplement

> [q325] beta 0.06497 unit increase p_value 7e-17 accession_id GCST90479543 pubmed_id 39024449 first_author Verma A

> [q326] p_value 9.000000000000001e-17 accession_id GCST90624049 pubmed_id 40759756 first_author Foote IF

> [q327] range [0.0083-0.0151] beta 0.011705069 unit decrease p_value 2e-11 accession_id GCST90449056 pubmed_id 39537608 first_author Koskeridis F

> [q328] or_per_copy_num 1.04 or_value 1.04 beta - p_value 3.0000000000000004e-08 accession_id GCST90837384 pubmed_id 39511132 first_author Salo V

> [q329] beta 0.05994 unit increase p_value 2e-39 accession_id GCST90475936 pubmed_id 39024449 first_author Verma A

> [q330] beta 0.0393 unit increase p_value 1e-15 accession_id GCST90475919 pubmed_id 39024449 first_author Verma A

Row 51's ZC3HC1 lead (`assoc-rs56179563`, 22 associations) and its proxy rs11556924 (`assoc-rs11556924`, pages 0 to
2, 141 associations). At the lead: Verma's coronary artery or heart disease, rs56179563-G, increase (q325, β
0.065); Foote's frailty factor 3, allele "?" (q326; the deposit gives G raising it, pmid-40759756#q6); Koskeridis's
systolic blood pressure, rs56179563-A, decrease (q327); the rest angina, heart failure, erectile dysfunction,
height (G lower), creatinine, blood cell counts (A raises platelets, eosinophils and basophils). At rs11556924, T
riding with A: Salo's lumbar disc herniation, rs11556924-T, OR 1.04 (1.02 to 1.05), P 3 × 10⁻⁸ (q328), the
longer-life allele raising a disease; C raises coronary atherosclerosis (q329) and hypertension (q330); T lowers HDL
cholesterol, IGF-1 and creatinine, raises eGFR, SHBG and testosterone; Timmers 2019's own line (T, P 4e-7). For row 51.

## Reading 2026-11-11, supplement

> [q331] discovery_ancestry[0] 829699 European (Estonia, Finland, U.K.)

Salo's lumbar disc herniation study (`study-GCST90837384`), the source of q328: European discovery, 80,724 cases and
748,975 controls from Estonia, Finland and the UK, so the trade-off at rs11556924 is read in Europeans, where T rides
with the lead's A (db-ensembl-116#q349, q355). No Open Targets set at the locus is of disc disease. For row 51.

## Reading 2026-11-11, supplement

> [q332] or_per_copy_num 0.876 or_value 0.876 beta - p_value 4e-11 accession_id GCST90132314 pubmed_id 36474045 first_author Aragam KG

rs268 (`assoc-rs268-p0` to `-p2`, 101 associations, all read), Aragam 2022's coronary artery disease: effect allele A
(the record's `snp_effect_allele`), OR 0.876 per copy (0.843 to 0.911), P 4e-11. A protects against coronary disease.
For row 52.

> [q333] beta 0.024401588 unit increase p_value 3.0000000000000004e-08 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB

Rosoff 2023's "aging" (mvAge): A, increase, P 3e-8 (pmid-37550455#q46). For row 52.

> [q334] beta 0.2466 unit increase p_value 6e-166 accession_id GCST90019523 pubmed_id 33462484 first_author Sinnott-Armstrong N

Sinnott-Armstrong 2021's triglycerides (UK Biobank): G raises triglycerides, 0.25 units, P 6e-166. For row 52.

> [q335] efo_id EFO_0004530 efo_trait triglyceride measurement

That record's trait: EFO_0004530, triglyceride measurement. For row 52.

> [q336] beta 0.12852937 unit increase p_value 5e-10 accession_id GCST007931 pubmed_id 31015401 first_author Wu Y

Wu 2019's statin use (UK Biobank): G raises it. For row 52.

> [q337] beta 0.2533705 unit decrease p_value 9e-65 accession_id GCST90728570 pubmed_id 41686896 first_author Du M

Du's MASLD (a multi-trait analysis): A, decrease, P 9e-65. No harm on A's side among the 101 records: A lowers
coronary disease, triglycerides and liver-fat disease and raises HDL; the blood-cell lines (haematocrit, cell
volume and width, platelets) are measures, not diseases; abdominal aortic aneurysm, metabolic syndrome and its
clusters print no allele. For row 52.

> [q338] p_value 8e-10 accession_id GCST009450 pubmed_id 31484785 first_author Wright KM

rs15285 (`assoc-rs15285-p0` to `-p4`, 205 associations), Wright 2019's fathers' longevity (GCST009450): P 8e-10,
allele printed G (Wright's S9 column, pmid-31484785#q93), no effect. For row 52.

> [q339] beta 0.052 unit decrease p_value 8e-14 accession_id GCST005194 pubmed_id 29212778 first_author van der Harst P

van der Harst 2018's coronary artery disease: T lowers it, P 8e-14. The second signal's; prose only. For row 52.

## Reading 2026-11-11, supplement

> [q340] beta 0.2972 unit decrease p_value 7e-220 accession_id GCST90019510 pubmed_id 33462484 first_author Sinnott-Armstrong N

Sinnott-Armstrong 2021's HDL cholesterol (UK Biobank, GCST90019510): G lowers HDL, P 7e-220 (the record's effect
allele rs268-G). For row 52.

## Reading 2026-11-11, supplement

> [q341] page size 50 totalElements 4 totalPages 1 number 0

GWAS Catalog associations for rs7844965 (`assoc-rs7844965-p0`, page 0 of 1): 4 records, all parental longevity
(Pilling's combined parents and fathers, Wright's fathers' meta and AncestryDNA fathers). No disease or risk-factor
record, so no harm is recorded on A's side here. For row 53.

> [q342] _embedded.associations[0] association_id 214209387 risk_frequency 0.23 pvalue_description  pvalue_mantissa 8 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [0.906-0.949] or_per_copy_num 0.928 or_value 0.928 beta - p_value 8e-12 accession_id GCST90243964 pubmed_id 35511172 first_author Gabriel AAG ci_lower 0.906 ci_upper 0.949

rs6558008 (`assoc-rs6558008-p0`, its only record, page 0 of 1): lung cancer or family history of lung cancer,
OR 0.928 (0.906 to 0.949) per copy, P 8 × 10⁻¹², risk frequency 0.23, GCST90243964. For row 53.

> [q343] _embedded.associations[0].snp_effect_allele[0] rs6558008-C

The allele is C, the minor one, which travels with the lead's A (pmid-30642433#q247): A's side has less lung
cancer, in the patient or the family. For row 53.

> [q344] initial_sample_size 4,595 African ancestry cases, 1,937 African ancestry controls

GCST90692035 (`study-GCST90692035`), never smoking in UK Biobank: 4,595 African-ancestry cases, 1,937 controls.
For row 53.

> [q345] initial_sample_size 1,970 East Asian ancestry cases, 679 East Asian ancestry controls

GCST90692469 (`study-GCST90692469`): 1,970 East Asian-ancestry cases, 679 controls. For row 53.

## Reading 2026-11-11, supplement

> [q346] _embedded.associations[0] association_id 104964846 risk_frequency NR pvalue_description  pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false

GWAS Catalog associations for rs11780471 (`assoc-rs11780471-p0`, page 0 of 1): six records, five on smoking
(q347 to q350) and one on lung cancer (q351). For row 53.

> [q347] _embedded.associations[1] association_id 102107907 risk_frequency 0.0606 pvalue_description  pvalue_mantissa 5 pvalue_exponent -110 multi_snp_haplotype false snp_interaction false

Smoking initiation (Saunders 2022, GCST90243985), P 5 × 10⁻¹¹⁰, A's β −0.038 (q348): A, the minor allele (0.06),
lowers smoking initiation. For row 53.

> [q348] _embedded.associations[1].snp_effect_allele[0] rs11780471-A

The allele is A. For row 53.

> [q349] _embedded.associations[3] association_id 41275855 risk_frequency 0.063121 pvalue_description  pvalue_mantissa 2 pvalue_exponent -13 multi_snp_haplotype false snp_interaction false

Smoking initiation, ever against never regular (Liu 2019, GCST007474), P 2 × 10⁻¹³, A lowers it (q350). For row 53.

> [q350] _embedded.associations[3].snp_effect_allele[0] rs11780471-A

A again. For row 53.

> [q351] _embedded.associations[5] association_id 22003071 risk_frequency 0.940381112 pvalue_description  pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false

Lung cancer (McKay 2017, GCST004748), P 2 × 10⁻⁸, OR 1.15 per G (q352): A, the longer-lived allele in Wright's
fathers (pmid-31484785#q99), goes with less lung cancer and less smoking. rs11780471 is a smoking locus; how much of
row 53's lead (r² 0.13) it explains is untested. For row 53.

> [q352] _embedded.associations[5].snp_effect_allele[0] rs11780471-G

The allele is G. For row 53.

## Reading 2026-11-12, record

> [q353] page size 50 totalElements 1 totalPages 1 number 0

`associations-rs11783562.json`: the catalog holds one association for the lead. For row 54.

> [q354] _embedded.associations[0] association_id 55479437 risk_frequency NR pvalue_description  pvalue_mantissa 8 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0078-0.0158] beta 0.01177 unit increase p_value 8e-09 accession_id GCST009448 pubmed_id 31484785 first_author Wright KM ci_lower 0.0078 ci_upper 0.0158

That one is Wright 2019's current-age study (GCST009448): β 0.01177, P 8 × 10⁻⁹, the uncorrected P (pmid-31484785#q100). No other lifespan-class study of this SNP in the catalog. For row 54.

> [q355] _embedded.associations[0].snp_effect_allele[0] rs11783562-C

Its effect allele is Wright's C, the complement of the forward G (db-ensembl-116#q376). For row 54.

## Reading 2026-11-12, supplement

`assoc-rs35262860-p0`: the catalog's associations for row 55's lead.

> [q356] _embedded.associations[0] association_id 47713526 risk_frequency 0.39 pvalue_description  pvalue_mantissa 6 pvalue_exponent -7 multi_snp_haplotype false snp_interaction false range 1.07-1.15 or_per_copy_num 1.11 or_value 1.11 beta - p_value 6e-07 accession_id GCST008600 pubmed_id 31413261 first_author Deelen J ci_lower 1.07 ci_upper 1.15

> [q357] _embedded.associations[0].snp_effect_allele[0] rs35262860-GCT

One association: Deelen 2019's trans-ethnic 90th percentile line (GCST008600), GCT OR 1.11 (1.07-1.15), P 6e-7
(the paper's Table 4 prints 5.6e-7, pmid-31413261#q145). No other trait. For row 55.

## Reading 2026-11-12, record

> [q358] _embedded.associations[0] association_id 35567961 risk_frequency 0.97 pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.023-0.049] beta 0.036 unit increase p_value 3.0000000000000004e-08 accession_id GCST006701 pubmed_id 29227965 first_author Pilling LC ci_lower 0.023 ci_upper 0.049

> [q359] _embedded.associations[0].snp_effect_allele[0] rs13262617-A

One association: Pilling 2017's fathers' attained age (GCST006701), A β 0.036 (0.023–0.049), P 3e-8. No other trait.
For row 56.

## Reading 2026-11-12, record

> [q360] _embedded.associations[0] association_id 80754832 risk_frequency 0.0312 pvalue_description  pvalue_mantissa 2 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [NR] beta 5.969329 unit increase p_value 2e-09 accession_id GCST012419 pubmed_id 33948810 first_author Gurinovich A

> [q361] _embedded.associations[0].snp_effect_allele[0] rs10973748-T

`assoc-rs10973748-p0`: one association, Gurinovich 2021's (GCST012419, longevity, 100 years and older), T, P 2e-9;
its "beta 5.969329" is the paper's score Z (pmid-33948810#q23) and the risk frequency 0.0312 the controls'. No other
trait. The eight CEU proxies at r² ≥ 0.8 (`assoc-rs341466-p0`, `-rs341467-`, `-rs10973750-`, `-rs10973749-`,
`-rs12378970-`, `-rs10814677-`, `-rs76830434-`, `-rs10973754-`) hold none (totalElements 0 each). For row 58.

## Reading 2026-11-12, supplement

> [q362] range [1.37-1.43] or_per_copy_num 1.4 or_value 1.4 beta - p_value 4e-169 accession_id GCST009030 pubmed_id 31420334 first_author Lindstrom S

> [q363] _embedded.associations[26].snp_effect_allele[0] rs2519093-T

Venous thromboembolism (Lindström 2019, page 7, association 26): T raises it, OR 1.40 (1.37-1.43), P 4e-169. For row 59.

> [q364] range [1.06- 1.11] or_per_copy_num 1.08 or_value 1.08 beta - p_value 1e-11 accession_id GCST003116 pubmed_id 26343387 first_author Nikpay M

> [q365] _embedded.associations[46].snp_effect_allele[0] rs2519093-T

Coronary artery disease (Nikpay 2015, page 7, association 46): T raises it, OR 1.08, P 1e-11. For row 59.

> [q366] range [1.07-1.11] or_per_copy_num 1.09 or_value 1.09 beta - p_value 5e-19 accession_id GCST011365 pubmed_id 33532862 first_author Hartiala JA

> [q367] _embedded.associations[49].snp_effect_allele[0] rs2519093-T

Myocardial infarction (Hartiala 2021, page 6, association 49): T raises it, OR 1.09, P 5e-19. For row 59.

> [q368] range [0.051-0.061] beta 0.0562 unit increase p_value 3e-100 accession_id GCST90018961 pubmed_id 34594039 first_author Sakaue S

> [q369] _embedded.associations[41].snp_effect_allele[0] rs2519093-T

LDL cholesterol (Sakaue 2021, page 6, association 41): T raises it, β 0.056, P 3e-100. For row 59.

> [q370] range [0.077-0.089] beta 0.0830219 unit decrease p_value 1e-180 accession_id GCST90002384 pubmed_id 32888494 first_author Vuckovic D

> [q371] _embedded.associations[10].snp_effect_allele[0] rs2519093-T

Haemoglobin (Vuckovic 2020, page 7, association 10): T lowers it, β 0.083, P 1e-180. For row 59.

> [q372] range [1.04-1.07] or_per_copy_num 1.05 or_value 1.05 beta - p_value 3e-16 accession_id GCST006409 pubmed_id 30013184 first_author Waage J

> [q373] _embedded.associations[5].snp_effect_allele[0] rs2519093-T

Allergic rhinitis (Waage 2018, page 0, association 5): T raises it, OR 1.05, P 3e-16. For row 59.

> [q374] totalElements 398

rs2519093's 398 associations (`assoc-rs2519093-p0` to `-p7`, all read): lipids and lipoproteins, blood cell counts,
hundreds of plasma proteins, venous thromboembolism, coronary disease and myocardial infarction (T the risk allele
throughout), allergy; no lifespan, longevity, healthspan or frailty line. Its nine r² ≥ 0.8 proxies hold 1,023 more
(`assoc-<rsID>-s200p*`, all pages), none of those traits. For row 59.

> [q375] range [0.094-0.157] beta 0.1255 unit increase p_value 6.0000000000000004e-18 accession_id GCST90480299 pubmed_id 39024449 first_author Verma A

> [q376] _embedded.associations[35].snp_effect_allele[0] rs115478735-A

Peptic ulcer (Verma 2024, `assoc-rs115478735-s200p0`, association 35): rs115478735's A raises it, β 0.126, P 6e-18.
rs115478735 is at CEU r² 0.97, D′ 1.0 to the lead (db-ensembl-116 `ld-rs2519093-ceu.json`, line 18), its A at 0.81
against the lead's C at 0.815, so A rides with C, the longer-life allele (derived). For row 59.

> [q377] range [0.042-0.073] beta 0.05748 unit increase p_value 1e-14 accession_id GCST90476073 pubmed_id 39024449 first_author Verma A

> [q378] _embedded.associations[4].snp_effect_allele[0] rs115478735-A

Diverticulosis and diverticulitis (Verma 2024, association 4): A, riding with C, raises it, β 0.057, P 1e-14. For row
59.

> [q379] range [0.039-0.075] beta 0.05737 unit increase p_value 3e-11 accession_id GCST90475731 pubmed_id 39024449 first_author Verma A

> [q380] _embedded.associations[17].snp_effect_allele[0] rs115478735-A

Gout and other crystal arthropathies (Verma 2024, association 17): A, riding with C, raises it, β 0.057, P 3e-11. For
row 59.

> [q381] range [0.044-0.083] beta 0.0632 unit increase p_value 1e-10 accession_id GCST90627740 pubmed_id 41644669 first_author White SL

> [q382] _embedded.associations[0].snp_effect_allele[0] rs635634-C

Benign nodular goiter (White, `assoc-rs635634-s200p0`, association 0): rs635634's C raises it, β 0.063, P 1e-10.
rs635634 is at CEU r² 0.97, D′ 1.0 to the lead; in Timmers' summary statistics its T (0.19) shortens life (β −0.0218,
P 1.3e-5, pmid-30642433 `rows-a6fe4f5f`), so C rides with the lead's C. These four lines, at proxies, are the trade-off
row 59 carries (D18.1): the longer-life side raises peptic ulcer, diverticular disease, gout and goitre, while T raises
thrombosis, coronary disease and LDL. For row 59.

## Reading 2026-11-12, supplement

> [q383] page size 50 totalElements 1 totalPages 1 number 0

`assoc-rs75824829-p0`: the catalog holds one association for the lead. For row 60.

> [q384] _embedded.associations[0] association_id 16533693 risk_frequency NR pvalue_description  pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0085-0.018] beta 0.01326 unit decrease p_value 4e-08 accession_id GCST003395 pubmed_id 27015805 first_author Pilling LC ci_lower 0.0085 ci_upper 0.018

Pilling 2016's GCST003395, P 4e-8, β 0.01326 "unit decrease", effect allele unrecorded; no replication sample (q317 for the study). For row 60.

> [q385] _embedded.associations[0].mapped_genes[0] LINC02907

The catalog maps it to LINC02907 (and PPP1R26-AS1), the seed's name. For row 60.

## Reading 2026-11-12, supplement

> [q386] page size 50 totalElements 1 totalPages 1 number 0

The Catalog holds one association for rs547541271. For row 61.

> [q387] _embedded.associations[0] association_id 165236637 risk_frequency NR pvalue_description  pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta 0.04 unit increase p_value 3.0000000000000004e-08 accession_id GCST90551886 pubmed_id 40021682 first_author Park J

Park's women's study (GCST90551886): P 3e-8, β 0.04 per unit increase.

> [q388] _embedded.associations[0].mapped_genes[0] CELF2

Mapped to CELF2.

## Reading 2026-11-12, supplement

> [q389] page size 50 totalElements 1 totalPages 1 number 0

The Catalog's associations for rs11186068 (`assoc-rs11186068-p0`): one. For row 62.

> [q390] _embedded.associations[0] association_id 218960570 risk_frequency 0.033 pvalue_description  pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta 1.728 unit increase p_value 3.0000000000000004e-08 accession_id GCST90726611 pubmed_id 42176242 first_author Beccacece L

Beccacece 2026's (GCST90726611): risk frequency 0.033, P 3e-8, beta 1.728. For row 62.

> [q391] _embedded.associations[0].mapped_genes[0] LINC00865

Mapped to LINC00865. For row 62.

> [q392] _embedded.associations[0].snp_effect_allele[0] rs11186068-G

The effect allele G. For row 62.

> [q393] initial_sample_size 299 Calabrian ancestry cases, 406 Calabrian ancestry controls replication_sample_size NA

The study record (`study-GCST90726611.json`): 299 Calabrian cases, 406 controls, no replication sample entered. For row 62.

> [q394] cohort[0] ECHA

The cohorts, ECHA ...

> [q395] cohort[1] GEHA

... and GEHA. For row 62.

## Reading 2026-11-12, supplement

> [q396] _embedded.associations[33] association_id 188118406 risk_frequency 0.29106134 pvalue_description  pvalue_mantissa 3 pvalue_exponent -41 multi_snp_haplotype false snp_interaction false range [0.28-0.38] beta 0.32841325 unit increase p_value 3e-41 accession_id GCST90468151 pubmed_id 39789286 first_author Loya H ci_lower 0.28 ci_upper 0.38

The Catalog's associations for rs35198068 (`assoc-rs35198068.json`): 58. Type 2 diabetes, P 3e-41, beta 0.328 increase ... For row 63.

> [q397] _embedded.associations[33].reported_trait[0] Type 2 diabetes

... (the reported trait) ... For row 63.

> [q398] _embedded.associations[33].snp_effect_allele[0] rs35198068-C

... for C: C is the diabetes risk allele, T the non-risk one. For row 63.

> [q399] _embedded.associations[20] association_id 228125396 risk_frequency 0.7066 pvalue_description  pvalue_mantissa 4 pvalue_exponent -89 multi_snp_haplotype false snp_interaction false range [0.054-0.066] beta 0.0604 unit increase p_value 4e-89 accession_id GCST90475159 pubmed_id 39024449 first_author Verma A ci_lower 0.054 ci_upper 0.066

Body mass index (minimum, inverse-normal), P 4e-89, beta 0.060 increase ... For row 63.

> [q400] _embedded.associations[20].reported_trait[0] Body mass index (BMI, minimum, inv-normal transformed)

... (the reported trait) ... For row 63.

> [q401] _embedded.associations[20].snp_effect_allele[0] rs35198068-T

... for T: the longer-life allele raises BMI. For row 63.

> [q402] _embedded.associations[25] association_id 228059042 risk_frequency 0.7066 pvalue_description  pvalue_mantissa 6 pvalue_exponent -36 multi_snp_haplotype false snp_interaction false range [0.029-0.039] beta 0.03383 unit increase p_value 5.9999999999999996e-36 accession_id GCST90475255 pubmed_id 39024449 first_author Verma A ci_lower 0.029 ci_upper 0.039

Diastolic blood pressure (mean), P 6e-36, beta 0.034 increase ... For row 63.

> [q403] _embedded.associations[25].reported_trait[0] diastolic blood pressure (DBP, mean, inv-normal transformed)

... (the reported trait) ... For row 63.

> [q404] _embedded.associations[25].snp_effect_allele[0] rs35198068-T

... for T. For row 63.

> [q405] _embedded.associations[3] association_id 228356771 risk_frequency 0.7067 pvalue_description  pvalue_mantissa 3 pvalue_exponent -23 multi_snp_haplotype false snp_interaction false range [0.032-0.051] beta 0.04147 unit increase p_value 3e-23 accession_id GCST90475762 pubmed_id 39024449 first_author Verma A ci_lower 0.032 ci_upper 0.051

At rs34872471 (`assoc-rs34872471.json`, 82 associations): obesity (PheCode 278.1), P 3e-23, beta 0.041 increase ... For row 63.

> [q406] _embedded.associations[3].reported_trait[0] Obesity (PheCode 278.1)

... (the reported trait) ... For row 63.

> [q407] _embedded.associations[3].snp_effect_allele[0] rs34872471-T

... for T: the longer-life allele raises obesity, a disease. For row 63.

> [q408] _embedded.associations[8] association_id 228334712 risk_frequency 0.7069 pvalue_description  pvalue_mantissa 5 pvalue_exponent -28 multi_snp_haplotype false snp_interaction false range [0.057-0.084] beta 0.07062 unit decrease p_value 5e-28 accession_id GCST90476123 pubmed_id 39024449 first_author Verma A ci_lower 0.057 ci_upper 0.084

Chronic renal failure (PheCode 585.3), P 5e-28, beta 0.071 decrease ... For row 63.

> [q409] _embedded.associations[8].reported_trait[0] Chronic renal failure [CKD] (PheCode 585.3)

... (the reported trait) ... For row 63.

> [q410] _embedded.associations[8].snp_effect_allele[0] rs34872471-T

... for T. For row 63.

> [q411] _embedded.associations[60] association_id 131101556 risk_frequency 0.291251 pvalue_description  pvalue_mantissa 3 pvalue_exponent -40 multi_snp_haplotype false snp_interaction false range [0.15-0.2] beta 0.173769 increase p_value 2.9999999999999998e-40 accession_id GCST90274723 pubmed_id 38409652 first_author Zhao C ci_lower 0.15 ci_upper 0.2

Cardiometabolic multimorbidity, P 3e-40, beta 0.174 increase (the seed's Zhao 2024, PMID 38409652, whose abstract names no SNP) ... For row 63.

> [q412] _embedded.associations[60].reported_trait[0] Cardiometabolic multimorbidity

... (the reported trait) ... For row 63.

> [q413] _embedded.associations[60].snp_effect_allele[0] rs34872471-C

... for C. For row 63.

> [q414] _embedded.associations[59] association_id 131774393 risk_frequency NR pvalue_description  pvalue_mantissa 3 pvalue_exponent -17 multi_snp_haplotype false snp_interaction false range [0.17-0.28] beta 0.2238 unit increase p_value 3e-17 accession_id GCST90310294 pubmed_id 38689001 first_author Keaton JM ci_lower 0.17 ci_upper 0.28

Systolic blood pressure, P 3e-17, beta 0.224 increase ... For row 63.

> [q415] _embedded.associations[59].reported_trait[0] Systolic blood pressure

... (the reported trait) ... For row 63.

> [q416] _embedded.associations[59].snp_effect_allele[0] rs34872471-C

... for C: blood pressure runs both ways at the locus (T raises diastolic, q402, C systolic). For row 63.

## Reading 2026-11-12, supplement

> [q417] _embedded.associations[0] association_id 105619373 risk_frequency NR pvalue_description  pvalue_mantissa 6 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.89-0.95] or_per_copy_num 0.92 or_value 0.92 beta - p_value 6.000000000000001e-09 accession_id GCST90270909 pubmed_id 36737517 first_author Akiyama M ci_lower 0.89 ci_upper 0.95

Akiyama 2023's association (GCST90270909, `assoc-rs76612380`): OR 0.92 (0.89–0.95), P 6e-9, risk frequency not
reported. For row 64.

> [q418] _embedded.associations[0].snp_effect_allele[0] rs76612380-?

The Catalog records no effect allele ("?"): its curators could not tell which allele the 0.92 counts, the question
pmid-36737517#q10 against q26 settles. Open Targets' PICS set copies this record's sign (db-opentargets-26.09#q771).
For row 64.

> [q425] _embedded.associations[0].mapped_genes[0] BET1L

Mapped to BET1L. A second line (GCST90270907, P 8e-7, the men) is the same paper's. For row 64.

> [q419] _embedded.associations[0] association_id 64573116 risk_frequency 0.101 pvalue_description  pvalue_mantissa 1 pvalue_exponent -14 multi_snp_haplotype false snp_interaction false range [0.18-0.3] beta 0.238 unit increase p_value 1e-14 accession_id GCST011021 pubmed_id 33199917 first_author Bakker MK ci_lower 0.18 ci_upper 0.3

Bakker 2020 (GCST011021, PMID 33199917), intracranial aneurysm at rs2280543: beta 0.238, increase, risk frequency
0.101 ... For row 64.

> [q421] _embedded.associations[0].snp_effect_allele[0] rs2280543-T

... for T, the minor allele, the lead's C haplotype: more aneurysm. For row 64.

> [q420] _embedded.associations[2] association_id 17787 risk_frequency 0.88 pvalue_description  pvalue_mantissa 4 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [1.17-1.64] or_per_copy_num 1.39 or_value 1.39 beta - p_value 4e-12 accession_id GCST001027 pubmed_id 21460842 first_author Cha PC ci_lower 1.17 ci_upper 1.64

Cha 2011 (GCST001027, PMID 21460842), uterine fibroids, Japanese: OR 1.39, P 4e-12, risk frequency 0.88 ... For row 64.

> [q422] _embedded.associations[2].snp_effect_allele[0] rs2280543-G

... for "G", the major allele at 0.88 printed on the other strand (rs2280543 is C/T, db-ensembl-116#q465): C, the
lead's T haplotype, more fibroids, as BBJ's own table has it (pmid-36737517#q32). For row 64.

## Reading 2026-11-12, supplement

> [q426] _embedded.associations[0] association_id 55479447 risk_frequency NR pvalue_description  pvalue_mantissa 4 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0081-0.0161] beta 0.01207 unit increase p_value 4e-09 accession_id GCST009448 pubmed_id 31484785 first_author Wright KM ci_lower 0.0081 ci_upper 0.0161

> [q427] _embedded.associations[0].snp_effect_allele[0] rs4755737-A

> [q428] _embedded.associations[0].reported_trait[0] Longevity

`assoc-rs4755737`: the catalog's one association for the lead (totalElements 1) is Wright 2019's age GWAS, filed as
"Longevity" at the uncorrected P (4e-9; pmid-31484785#q107), A, beta 0.0121. No blood-pressure or other trait line for
the lead. For row 65.

> [q429] _embedded.associations[0] association_id 55479432 risk_frequency NR pvalue_description  pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0075-0.0155] beta 0.01152 unit increase p_value 2e-08 accession_id GCST009448 pubmed_id 31484785 first_author Wright KM ci_lower 0.0075 ci_upper 0.0155

`assoc-rs4755202`: the seed's second rsID, the same study's one line, A. For row 65.

## Reading 2026-11-12, supplement

> [q430] _embedded.associations[14] association_id 228298365 risk_frequency 0.7756 pvalue_description pvalue_mantissa 5 pvalue_exponent -87 multi_snp_haplotype false snp_interaction false range [0.15-0.18] beta 0.1683 unit decrease p_value 5e-87 accession_id GCST90479794 pubmed_id 39024449 first_author Verma A ci_lower 0.15 ci_upper 0.18

> [q431] _embedded.associations[14].reported_trait[0] Melanomas of skin, dx or hx (PheCode 172.1)

> [q432] _embedded.associations[14].snp_effect_allele[0] rs1126809-G

> [q433] _embedded.associations[12] association_id 228300022 risk_frequency 0.7328 pvalue_description pvalue_mantissa 2 pvalue_exponent -57 multi_snp_haplotype false snp_interaction false range [0.15-0.18] beta 0.1623 unit decrease p_value 2e-57 accession_id GCST90479795 pubmed_id 39024449 first_author Verma A ci_lower 0.15 ci_upper 0.18

> [q434] _embedded.associations[12].reported_trait[0] Basal cell carcinoma (PheCode 172.21)

> [q435] _embedded.associations[12].snp_effect_allele[0] rs1126809-G

> [q436] _embedded.associations[10] association_id 228301017 risk_frequency 0.7751 pvalue_description pvalue_mantissa 1 pvalue_exponent -41 multi_snp_haplotype false snp_interaction false range [0.14-0.18] beta 0.164 unit decrease p_value 1e-41 accession_id GCST90479796 pubmed_id 39024449 first_author Verma A ci_lower 0.14 ci_upper 0.18

> [q437] _embedded.associations[10].reported_trait[0] Squamous cell carcinoma (PheCode 172.22)

> [q438] _embedded.associations[10].snp_effect_allele[0] rs1126809-G

> [q439] _embedded.associations[7] association_id 228317167 risk_frequency 0.7771 pvalue_description pvalue_mantissa 5 pvalue_exponent -100 multi_snp_haplotype false snp_interaction false range [0.14-0.16] beta 0.1505 unit decrease p_value 5e-100 accession_id GCST90480468 pubmed_id 39024449 first_author Verma A ci_lower 0.14 ci_upper 0.16

> [q440] _embedded.associations[7].reported_trait[0] Actinic keratosis (PheCode 702.1)

> [q441] _embedded.associations[7].snp_effect_allele[0] rs1126809-G

> [q442] _embedded.associations[83] association_id 30827831 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -172 multi_snp_haplotype false snp_interaction false range [0.16-0.35] beta 0.257 unit increase p_value 2e-172 accession_id GCST005897 pubmed_id 29739929 first_author Visconti A ci_lower 0.16 ci_upper 0.35

> [q443] _embedded.associations[83].reported_trait[0] Low tan response

> [q444] _embedded.associations[83].snp_effect_allele[0] rs1126809-A

> [q445] _embedded.associations[84] association_id 24294450 risk_frequency 0.7311 pvalue_description pvalue_mantissa 1 pvalue_exponent -43 multi_snp_haplotype false snp_interaction false range [1.41-1.59] or_per_copy_num 1.497006 or_value 1.497006 beta - p_value 1e-43 accession_id GCST004785 pubmed_id 27723757 first_author Jin Y ci_lower 1.41 ci_upper 1.59

> [q446] _embedded.associations[84].reported_trait[0] Vitiligo

> [q447] _embedded.associations[84].snp_effect_allele[0] rs1126809-G

> [q448] _embedded.associations[50] association_id 119452324 risk_frequency NR pvalue_description pvalue_mantissa 7 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.036-0.073] beta 0.0542 unit decrease p_value 7.000000000000001e-09 accession_id GCST90310211 pubmed_id 37386247 first_author Han X ci_lower 0.036 ci_upper 0.073

> [q449] _embedded.associations[50].reported_trait[0] Primary open angle glaucoma (multi-trait analysis)

> [q450] _embedded.associations[50].snp_effect_allele[0] rs1126809-A

> [q451] _embedded.associations[23] association_id 228271214 risk_frequency 0.7169 pvalue_description pvalue_mantissa 7 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [0.045-0.085] beta 0.06478 unit decrease p_value 7e-12 accession_id GCST90475851 pubmed_id 39024449 first_author Verma A ci_lower 0.045 ci_upper 0.085

> [q452] _embedded.associations[23].reported_trait[0] Macular degeneration, dry (PheCode 362.21)

> [q453] _embedded.associations[23].snp_effect_allele[0] rs1126809-G

> [q454] _embedded.associations[64] association_id 88930877 risk_frequency 29.21 pvalue_description pvalue_mantissa 2 pvalue_exponent -21 multi_snp_haplotype false snp_interaction false range [NR] or_per_copy_num 1.05 or_value 1.05 beta - p_value 2e-21 accession_id GCST012442 pubmed_id 34108613 first_author Ivarsdottir EV

> [q455] _embedded.associations[64].reported_trait[0] Age-related hearing impairment

> [q456] _embedded.associations[64].snp_effect_allele[0] rs1126809-A

> [q457] _embedded.associations[46] association_id 131476313 risk_frequency NR pvalue_description pvalue_mantissa 7 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0044-0.0089] beta 0.006619422 unit increase p_value 7.000000000000001e-09 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0044 ci_upper 0.0089

> [q458] _embedded.associations[46].reported_trait[0] Aging

> [q459] _embedded.associations[46].snp_effect_allele[0] rs1126809-G

> [q460] _embedded.associations[67] association_id 62271305 risk_frequency 0.7133 pvalue_description pvalue_mantissa 8 pvalue_exponent -13 multi_snp_haplotype false snp_interaction false range - beta - p_value 8e-13 accession_id GCST011100 pubmed_id 32678081 first_author Timmers PRHJ

> [q461] _embedded.associations[67].reported_trait[0] Aging traits (healthspan, parental lifespan or longevity) (multivariate analysis)

> [q462] _embedded.associations[67].snp_effect_allele[0] rs1126809-G

`assoc-rs1126809` (90 associations), read for row 66. Skin, from Verma 2024's PheCode GWAS (GCST90479794 and
its siblings, pubmed 39024449; the lines say "decrease" per G): G lowers melanoma of skin (β 0.168, P 5e-87, q430), basal cell carcinoma (P 2e-57, q433),
squamous cell carcinoma (P 1e-41, q436) and actinic keratosis (P 5e-100, q439); A raises a low tan response (P
2e-172, q442). Against G: G raises vitiligo (OR 1.50 per G, P 1e-43, Jin 2016, q445), and A lowers primary open-angle
glaucoma in a multi-trait analysis (β 0.054 "decrease", P 7e-9, q448), so G raises it. With G: G lowers dry macular
degeneration (P 7e-12, q451), and A raises age-related hearing impairment (OR 1.05, P 2e-21, q454). Ageing: Rosoff's
mvAge, G "increase" 0.0066, P 7e-9 (q457); Timmers 2020's multivariate scan, G, P 8e-13, no estimate (q460).

## Reading 2026-11-12, supplement

> [q463] _embedded.associations[0] association_id 35691766 risk_frequency 0.996 pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.059-0.122] beta 0.0906 unit decrease p_value 3.0000000000000004e-08 accession_id GCST006698 pubmed_id 29227965 first_author Pilling LC ci_lower 0.059 ci_upper 0.122

> [q464] _embedded.associations[0].reported_trait[0] Parental longevity (both parents in top 10%)

> [q465] _embedded.associations[0].snp_effect_allele[0] rs139137459-G

The GWAS Catalog's only association for rs139137459: Pilling 2017 (GCST006698), "Parental longevity (both parents
in top 10%)", G at 0.996, β 0.0906 "decrease" (CI 0.059-0.122), P 3e-8. For row 68.

## Reading 2026-11-12, supplement

> [q466] _embedded.associations[0] association_id 131476476 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0065-0.0136] beta 0.010027203 unit decrease p_value 3.0000000000000004e-08 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0065 ci_upper 0.0136

> [q467] _embedded.associations[0].snp_effect_allele[0] rs55686423-A

> [q468] _embedded.associations[1] association_id 102110877 risk_frequency 0.0897 pvalue_description pvalue_mantissa 1 pvalue_exponent -16 multi_snp_haplotype false snp_interaction false range [0.009-0.0144] beta 0.0117 unit decrease p_value 1e-16 accession_id GCST90243985 pubmed_id 36477530 first_author Saunders GRB ci_lower 0.009 ci_upper 0.0144

> [q469] _embedded.associations[1].reported_trait[0] Smoking initiation

> [q470] _embedded.associations[1].snp_effect_allele[0] rs55686423-T

The GWAS Catalog's two associations for rs55686423: Rosoff 2023's mvAge (GCST90321079), A, β 0.0100 "decrease", P
3e-8 (q466, q467); and Saunders 2022's smoking initiation (GCST90243985, PMID 36477530), T at 0.0897, β 0.0117
"decrease", P 1e-16 (q468-q470): T lowers the chance of ever having smoked regularly. For row 69.

## Reading 2026-11-12, supplement

> [q471] _embedded.associations[0] association_id 62271314 risk_frequency 0.0733 pvalue_description pvalue_mantissa 8 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range - beta - p_value 8e-09 accession_id GCST011100 pubmed_id 32678081 first_author Timmers PRHJ

> [q472] _embedded.associations[0].snp_effect_allele[0] rs12830425-G

> [q473] page size 200 totalElements 1 totalPages 1 number 0

The GWAS Catalog's one association for rs12830425 (q473): Timmers 2020's multivariate ageing traits (GCST011100),
G at 0.073, P 8e-9 (q471, q472). For row 70.

## Reading 2026-11-12, supplement

> [q474] _embedded.associations[0] association_id 16503376 risk_frequency NR pvalue_description pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [NR] or_per_copy_num 1.6611296 or_value 1.6611296 beta - p_value 4e-08 accession_id GCST003425 pubmed_id 26912274 first_author Zeng Y

GWAS Catalog, rs2440012: one association, Zeng 2016's (GCST003425), P 4e-8, OR 1.66 (per C, the inverse of 0.602).
No other trait. For row 72.
