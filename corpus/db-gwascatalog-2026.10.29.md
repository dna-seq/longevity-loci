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

## Reading 2026-11-12, record

> [q475] page size 200 totalElements 0 totalPages 0 number 0

rs9536314 holds no association in the GWAS Catalog (q475): no genome-wide line for KL-VS on any trait. For row 73.

## Reading 2026-11-12, record

> [q476] _embedded.associations[0] association_id 35567723 risk_frequency 0.938 pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.016-0.034] beta 0.0251 unit increase p_value 3.0000000000000004e-08 accession_id GCST006696 pubmed_id 29227965 first_author Pilling LC ci_lower 0.016 ci_upper 0.034

> [q477] _embedded.associations[0].reported_trait[0] Parental longevity (mother's attained age)

> [q478] page size 200 totalElements 0 totalPages 0 number 0

rs61949650 holds one association in the GWAS Catalog (q476, q477): Pilling 2017's mothers' attained age
(GCST006696), risk frequency 0.938 (T), β 0.0251, P 3e-8, mapped to LGMNP1 and LINC00355. Nothing else, no disease;
rs12586026 holds none (q478). For row 74.

## Reading 2026-11-12, record

> [q479] page size 200 totalElements 0 totalPages 0 number 0

> [q480] page size 200 totalElements 0 totalPages 0 number 0

Neither of row 75's rsIDs holds a GWAS Catalog association (q479 rs35257605, q480 rs116257533). For row 75.

## Reading 2026-11-13, record

> [q481] page size 200 totalElements 3 totalPages 1 number 0

> [q482] _embedded.associations[1].reported_trait[0] Parental longevity (combined parental attained age, Martingale residuals)

rs61978928 holds three GWAS Catalog associations (q481), all Pilling 2017's parental longevity: the combined
attained age (q482, P 2e-8), both parents in the top 10 % (P 3e-7) and fathers' attained age (P 2e-7). No disease.
For row 76.

## Reading 2026-11-13, record

> [q483] _embedded.associations[0] association_id 80754844 risk_frequency 0.0045 pvalue_description pvalue_mantissa 1 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [NR] beta 5.7181206 unit increase p_value 1e-08 accession_id GCST012419 pubmed_id 33948810 first_author Gurinovich A

rs77184423 holds one GWAS Catalog association (q483): Gurinovich 2021's longevity (100 years and older), risk
frequency 0.0045, P 1e-8. Nothing else. For row 77.

## Reading 2026-11-13, record

> [q484] _embedded.associations[0] association_id 131476418 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0037-0.0077] beta 0.00567587 unit increase p_value 2e-08 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0037 ci_upper 0.0077

> [q485] _embedded.associations[0].snp_effect_allele[0] rs28455998-T

> [q486] _embedded.associations[1] association_id 93551897 risk_frequency NR pvalue_description pvalue_mantissa 1 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.025-0.049] beta 0.0369 unit increase p_value 1e-09 accession_id GCST90018988 pubmed_id 34594039 first_author Sakaue S ci_lower 0.025 ci_upper 0.049

> [q487] _embedded.associations[1].snp_effect_allele[0] rs28455998-A

> [q488] _embedded.associations[4] association_id 119068902 risk_frequency NR pvalue_description pvalue_mantissa 7 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range - or_per_copy_num 0.97 or_value 0.97 beta - p_value 7.000000000000001e-09 accession_id GCST90132302 pubmed_id 35915156 first_author Tcheandjieu C

> [q489] _embedded.associations[4].snp_effect_allele[0] rs3959554-A

> [q490] _embedded.associations[5] association_id 91631971 risk_frequency 0.5823 pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.012-0.026] beta 0.0189 unit decrease p_value 2e-08 accession_id GCST90020053 pubmed_id 34431594 first_author Atkins JL ci_lower 0.012 ci_upper 0.026

> [q491] _embedded.associations[5].snp_effect_allele[0] rs3959554-A

Row 78. At rs28455998 the catalog holds two associations: Rosoff's mvAge ("Aging"), T β +0.0057, P 2e-8 (q484,
q485), and agents acting on the renin-angiotensin system, A raising their use, β 0.0369, P 1e-9 (q486, q487), so T
with less use. At rs3959554: coronary artery disease, A OR 0.97, P 7e-9 (q488, q489), and Atkins' frailty index, A
lowering it, β 0.0189, P 2e-8 (q490, q491); the lead's T rides with A (db-ensembl-116#q598, q600), so T goes with
less coronary disease and less frailty. Height records at rs3959554 are not read. For row 78.

## Reading 2026-11-13, record

> [q492] _embedded.associations[1] association_id 35567970 risk_frequency 0.881 pvalue_description pvalue_mantissa 1 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.013-0.026] beta 0.0192 unit decrease p_value 1e-08 accession_id GCST006701 pubmed_id 29227965 first_author Pilling LC ci_lower 0.013 ci_upper 0.026

> [q493] _embedded.associations[1].snp_effect_allele[0] rs74011415-G

> [q494] _embedded.studies[0] initial_sample_size 415,311 British ancestry individuals replication_sample_size NA gxe false gxg false snp_count 11535925 imputed true pooled false accession_id GCST006701 full_summary_stats_available true user_requested true pubmed_id 29227965 platforms Affymetrix [11535925] (imputed) disease_trait Parental longevity (father's attained age) full_summary_stats http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST006001-GCST007000/GCST006701 terms_of_license https://www.ebi.ac.uk/about/terms-of-use/

Row 79. Pilling 2017's fathers' attained age at rs74011415 (q492, q493): G, β 0.0192 "decrease" (in the Martingale
residual), P 1e-8, GCST006701; the fathers' study's initial sample, 415,311 British-ancestry individuals (q494). The
catalog's other records at the lead and at rs4774495 are Pilling's combined parents (P 7e-6) and Wright's fathers'
meta-analysis (P 5e-8). For row 79.

## Reading 2026-11-13, record

> [q495] _embedded.associations[0] association_id 138725159 risk_frequency 0.5051 pvalue_description pvalue_mantissa 3 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0074-0.0144] beta 0.0109 unit decrease p_value 3.0000000000000004e-09 accession_id GCST90446645 pubmed_id 39375568 first_author Sidorenko J ci_lower 0.0074 ci_upper 0.0144

> [q496] _embedded.associations[0].snp_effect_allele[0] rs4783780-A

> [q497] _embedded.associations[2] association_id 62271331 risk_frequency 0.5333 pvalue_description pvalue_mantissa 1 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta - p_value 1e-08 accession_id GCST011100 pubmed_id 32678081 first_author Timmers PRHJ

> [q498] _embedded.associations[2].snp_effect_allele[0] rs4783780-A

Row 82. At rs4783780 the catalog holds three records: body mass index, A lowering it (β 0.0109 "decrease", P 3e-9;
q495, q496), metabolic syndrome (allele unreported), and Timmers 2020's multivariate ageing traits, A, P 1e-8 (q497,
q498). rs4784227 holds 34, mostly breast cancer, also systolic and pulse pressure and Parkinson's disease. For row 82.

## Reading 2026-11-13, record

> [q499] _embedded.studies[4] initial_sample_size 699,030 European ancestry individuals replication_sample_size NA gxe false gxg false snp_count 4999481 imputed true pooled true accession_id GCST90624049 full_summary_stats_available true pubmed_id 40759756 platforms Various - as reported in the original studies disease_trait Frailty (Factor 3 - Multimorbidity) full_summary_stats http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90624001-GCST90625000/GCST90624049 terms_of_license https://creativecommons.org/publicdomain/zero/1.0/

> [q500] _embedded.studies[6] initial_sample_size 559,200 European ancestry individuals replication_sample_size NA gxe false gxg false snp_count 5423783 imputed true pooled true accession_id GCST90624047 full_summary_stats_available true pubmed_id 40759756 platforms Various - as reported in the original studies disease_trait Frailty (Factor 1 - Limited Social Support) full_summary_stats http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90624001-GCST90625000/GCST90624047 terms_of_license https://creativecommons.org/publicdomain/zero/1.0/

Foote 2025's deposits in the catalog: GCST90624049, n 699,030, the multimorbidity factor (q499); GCST90624047, n 559,200,
limited social support (q500); each n matches its deposit's. For row 85.

## Reading 2026-11-13, record

> [q501] . initial_sample_size 9,618 European ancestry individuals replication_sample_size 19,796 European ancestry individuals gxe false gxg false imputed false pooled false accession_id GCST004045 full_summary_stats_available false user_requested false pubmed_id 27790247 platforms Affymetrix [NR] disease_trait Age-related diseases, mortality and associated endophenotypes full_summary_stats NA terms_of_license https://www.ebi.ac.uk/about/terms-of-use/

GCST004045 (PMID 27790247): initial sample 9,618 European-ancestry individuals, replication 19,796 (q501). For rows 84
and 83, where it holds a set near each lead. For row 84.

## Reading 2026-11-13, record

> [q502] _embedded.associations[8] association_id 24294446 risk_frequency 0.7294 pvalue_description pvalue_mantissa 3 pvalue_exponent -33 multi_snp_haplotype false snp_interaction false range [1.33-1.49] or_per_copy_num 1.4130281 or_value 1.4130281 beta - p_value 3e-33 accession_id GCST004785 pubmed_id 27723757 first_author Jin Y ci_lower 1.33 ci_upper 1.49

> [q503] _embedded.associations[8].snp_effect_allele[0] rs4268748-T

> [q504] _embedded.associations[11] association_id 13436761 risk_frequency 0.26 pvalue_description pvalue_mantissa 2 pvalue_exponent -44 multi_snp_haplotype false snp_interaction false range [1.28-1.39] or_per_copy_num 1.33 or_value 1.33 beta - p_value 2e-44 accession_id GCST003327 pubmed_id 26829030 first_author Asgari MM ci_lower 1.28 ci_upper 1.39

> [q505] _embedded.associations[11].snp_effect_allele[0] rs4268748-C

> [q506] _embedded.associations[6] association_id 98326415 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -61 multi_snp_haplotype false snp_interaction false range [1.22-1.28] or_per_copy_num 1.25 or_value 1.25 beta - p_value 2e-61 accession_id GCST90095184 pubmed_id 35449187 first_author Kim Y ci_lower 1.22 ci_upper 1.28

> [q507] _embedded.associations[6].snp_effect_allele[0] rs4268748-C

> [q508] _embedded.associations[7] association_id 62271335 risk_frequency 0.7067 pvalue_description pvalue_mantissa 7 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range - beta - p_value 7e-12 accession_id GCST011100 pubmed_id 32678081 first_author Timmers PRHJ

> [q509] _embedded.associations[7].reported_trait[0] Aging traits (healthspan, parental lifespan or longevity) (multivariate analysis)

rs4268748, row 86, 12 associations. Vitiligo (Jin 2016, GCST004785): T OR 1.41, P 3e-33 (q502, q503), so T, Zenin's
healthier allele, raises vitiligo. Squamous cell carcinoma (Asgari 2016, GCST003327): C OR 1.33, P 2e-44 (q504,
q505); actinic keratosis (Kim 2022, GCST90095184): C OR 1.25, P 2e-61 (q506, q507). Timmers 2020's multivariate
ageing traits (GCST011100): P 7e-12, no effect printed (q508, q509). The rest: melanoma in situ, seborrhoeic keratosis,
benign skin neoplasms, sebaceous gland disorders, skin colour saturation and skin ageing, the disease and skin-ageing
lines with C the higher where a direction is printed. For row 86.

## Reading 2026-11-13, record

> [q510] _embedded.associations[0] association_id 131476435 risk_frequency NR pvalue_description pvalue_mantissa 5 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range [0.0099-0.019] beta 0.014460757 unit increase p_value 5e-10 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0099 ci_upper 0.019

> [q511] _embedded.associations[1] association_id 27238781 risk_frequency 0.95 pvalue_description pvalue_mantissa 3 pvalue_exponent -7 multi_snp_haplotype false snp_interaction false range [0.047-0.101] beta 0.074 unit decrease p_value 3e-07 accession_id GCST005194 pubmed_id 29212778 first_author van der Harst P ci_lower 0.047 ci_upper 0.101

rs34891485 (row 87): two associations. Rosoff 2023's mvAge (q510), effect allele T, β 0.0145, P 5e-10; and van der
Harst 2017's coronary artery disease (q511), risk allele T at 0.95, β 0.074 "unit decrease", P 3e-7: T lowers coronary
disease, so C raises it. For row 87.

## Reading 2026-11-13, record

> [q512] _embedded.associations[0] association_id 131476569 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.0041-0.0086] beta 0.006339843 unit decrease p_value 2e-08 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0041 ci_upper 0.0086

rs940088 (row 88): one association, Rosoff 2023's mvAge, effect allele T, β 0.0063 "unit decrease", P 2e-8 (q512):
T lowers mvAge, so C is the healthier allele. For row 88.

## Reading 2026-11-13, record

> [q513] _embedded.associations[0] association_id 164772423 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -21 multi_snp_haplotype false snp_interaction false range [0.056-0.085] beta 0.0706692 increase p_value 2e-21 accession_id GCST90314246 pubmed_id 38412862 first_author Suhre K ci_lower 0.056 ci_upper 0.085

rs1046896 (row 89): eight associations, seven of them HbA1c (Wheeler, Soranzo, Chen, Hachiya, Wojcik and others; T
raising it, P down to 4e-64) and one protein ratio (q513); no lifespan or longevity record, not even Torres'. For row
89.

## Reading 2026-11-13, record

> [q514] _embedded.associations[0] association_id 35691782 risk_frequency 0.953 pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.017-0.036] beta 0.0264 unit decrease p_value 2e-08 accession_id GCST006698 pubmed_id 29227965 first_author Pilling LC ci_lower 0.017 ci_upper 0.036

rs28926173 (row 90): two associations, both Pilling 2017's parental longevity: the top-10 % analysis (GCST006698, G at
0.953, β 0.0264 "unit decrease", P 2e-8; q514) and parents' attained age (GCST006697, P 6e-6). For row 90.

## Reading 2026-11-14, record

> [q515] _embedded.associations[14] association_id 6188 risk_frequency 0.24 pvalue_description pvalue_mantissa 3 pvalue_exponent -15 multi_snp_haplotype false snp_interaction false range [0.04-0.06] beta 0.05 unit increase p_value 3.0000000000000002e-15 accession_id GCST000185 pubmed_id 18454148 first_author Loos RJ ci_lower 0.04 ci_upper 0.06

rs17782313 (row 91): 15 associations, none of a lifespan phenotype; body mass index and obesity with C the risk allele
(Loos 2008, P 3e-15, q515; Willer 2009; Meyre 2009), height, dietary pattern, metabolic syndrome, leg ulcer and nail
fungus. For row 91.

## Reading 2026-11-14, record

> [q516] _embedded.associations[0] association_id 80754836 risk_frequency 0.0019 pvalue_description pvalue_mantissa 3 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [NR] beta 5.9159646 unit increase p_value 3.0000000000000004e-09 accession_id GCST012419 pubmed_id 33948810 first_author Gurinovich A

rs77546126 holds one GWAS Catalog association (q516): Gurinovich 2021's longevity (100 years and older), G, risk
frequency 0.0019, P 3e-9, its "beta" the score Z. Nothing else. For row 92.

## Reading 2026-11-14, record

> [q517] _embedded.associations[0] association_id 47713512 risk_frequency 0.87 pvalue_description pvalue_mantissa 4 pvalue_exponent -7 multi_snp_haplotype false snp_interaction false range [1.08-1.22] or_per_copy_num 1.1494253 or_value 1.1494253 beta - p_value 4e-07 accession_id GCST008600 pubmed_id 31413261 first_author Deelen J ci_lower 1.08 ci_upper 1.22

rs62127362 holds one GWAS Catalog association (q517): Deelen 2019's trans-ethnic longevity (90th percentile,
GCST008600), G, OR 1.15 (1.08–1.22), P 4e-7, Table 4's line inverted. Nothing else. For row 94.

## Reading 2026-11-14, record

> [q518] _embedded.associations[16] association_id 35567974 risk_frequency 0.504 pvalue_description pvalue_mantissa 8 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0083-0.0169] beta 0.0126 unit decrease p_value 8e-09 accession_id GCST006701 pubmed_id 29227965 first_author Pilling LC ci_lower 0.0083 ci_upper 0.0169

> [q519] _embedded.associations[1] association_id 228354946 risk_frequency 0.5261 pvalue_description pvalue_mantissa 2 pvalue_exponent -21 multi_snp_haplotype false snp_interaction false range [0.062-0.096] beta 0.07926 unit decrease p_value 2e-21 accession_id GCST90476035 pubmed_id 39024449 first_author Verma A ci_lower 0.062 ci_upper 0.096

> [q520] _embedded.associations[2] association_id 228354425 risk_frequency 0.5258 pvalue_description pvalue_mantissa 3 pvalue_exponent -15 multi_snp_haplotype false snp_interaction false range [0.055-0.093] beta 0.07399 unit decrease p_value 3.0000000000000002e-15 accession_id GCST90476030 pubmed_id 39024449 first_author Verma A ci_lower 0.055 ci_upper 0.093

> [q521] _embedded.associations[7] association_id 228207286 risk_frequency 0.5518 pvalue_description pvalue_mantissa 1 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [0.021-0.037] beta 0.02907 unit increase p_value 1e-12 accession_id GCST90480701 pubmed_id 39024449 first_author Verma A ci_lower 0.021 ci_upper 0.037

rs12461964 holds 19 GWAS Catalog associations (row 95). Pilling's fathers' attained age, A, 8e-9 (q518). Lung
disease, A protective, all genome-wide: respiratory failure, insufficiency, arrest (PheCode 509), A "decrease", P 2e-21
(q519); obstructive chronic bronchitis, P 3e-15 (q520); chronic bronchitis, pneumonia, respiratory failure (509.1),
medication for chronic lung disease (P 6e-13 to 1e-19). Smoking: years smoked, A "increase", P 1e-12 (q521). Also
omega-3 and fatty-acid measures, glycine, alkaline phosphatase, BMI (MTAG, A lower, 5e-8), FEV1 and FEV1/FVC after
bronchodilator (A higher, 2e-7 and 5e-7). For row 95.

## Reading 2026-11-14, record

> [q522] _embedded.associations[2] association_id 35567984 risk_frequency 0.586 pvalue_description pvalue_mantissa 1 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range [0.01-0.0186] beta 0.0143 unit decrease p_value 1e-10 accession_id GCST006701 pubmed_id 29227965 first_author Pilling LC ci_lower 0.01 ci_upper 0.0186

> [q523] _embedded.associations[0] association_id 227736328 risk_frequency 0.449 pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [1.05-1.1] or_per_copy_num 1.072 or_value 1.072 beta - p_value 2e-08 accession_id GCST91000481 pubmed_id 39198834 first_author Park YJ ci_lower 1.05 ci_upper 1.1

rs6108784 holds three GWAS Catalog associations (row 97): Pilling's fathers' attained age, T, P 1e-10 (q522); blood
pressure as a metabolic-syndrome component, C, OR 1.072, P 2e-8 (q523); and a mean arterial pressure by depressive
symptoms interaction, no allele. For row 97.

## Reading 2026-11-14, record

> [q524] _embedded.associations[1] association_id 131476364 risk_frequency NR pvalue_description pvalue_mantissa 6 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range [0.0043-0.0082] beta 0.006251762 unit increase p_value 6e-10 accession_id GCST90321079 pubmed_id 37550455 first_author Rosoff DB ci_lower 0.0043 ci_upper 0.0082

rs159428 holds seven GWAS Catalog associations (row 98): Rosoff 2023's multivariate ageing factor, T "increase", P
6e-10 (q524); also fluid intelligence, cognitive performance, executive function, the cognitive part of educational
attainment, and an "Aging" record. Zenin's healthspan is not among them. For row 98.

## Reading 2026-11-14, record

> [q525] _embedded.associations[4] association_id 62271348 risk_frequency 0.4633 pvalue_description pvalue_mantissa 4 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta - p_value 4e-08 accession_id GCST011100 pubmed_id 32678081 first_author Timmers PRHJ

> [q526] _embedded.associations[4].snp_allele[0] rs_id rs159428 effect_allele T

Row 98: Timmers 2020's multivariate ageing GWAS (healthspan, parental lifespan and longevity; pubmed 32678081,
GCST011100) has rs159428 at P 4e-8 (q525), T the effect allele (q526), its direction not printed here; it pools
Zenin's healthspan with UK Biobank's parental lifespan, so multivariate and not independent (D18.3, D22.2). For row
98.

## Reading 2026-11-14, record

> [q527] _embedded.associations[10] association_id 35567988 risk_frequency 0.856 pvalue_description pvalue_mantissa 2 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.012-0.024] beta 0.0176 unit decrease p_value 2e-08 accession_id GCST006701 pubmed_id 29227965 first_author Pilling LC ci_lower 0.012 ci_upper 0.024

> [q528] _embedded.associations[2] association_id 102116220 risk_frequency 0.149 pvalue_description pvalue_mantissa 3 pvalue_exponent -64 multi_snp_haplotype false snp_interaction false range [0.034-0.043] beta 0.0382 unit increase p_value 3e-64 accession_id GCST90243987 pubmed_id 36477530 first_author Saunders GRB ci_lower 0.034 ci_upper 0.043

> [q529] _embedded.associations[2].snp_allele[0] rs_id rs2273500 effect_allele C

> [q530] _embedded.associations[5] association_id 93479859 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.064-0.125] beta 0.0947 unit increase p_value 2e-09 accession_id GCST90018807 pubmed_id 34594039 first_author Sakaue S ci_lower 0.064 ci_upper 0.125

> [q531] _embedded.associations[5].snp_allele[0] rs_id rs2273500 effect_allele C

rs2273500 holds 12 GWAS Catalog associations (row 99): Pilling's fathers' attained age, T, 2e-8 (q527); cigarettes
smoked per day, C "increase", P 3e-64 (q528, q529; and four more cigarettes-per-day records, P 2e-39 to 3e-20, C up or
T down); chronic obstructive pulmonary disease, C "increase", P 2e-9 (q530, q531); nicotine dependence (C, 8e-9),
problematic tobacco use (1e-16, no allele), Foote's unhealthy-lifestyle frailty factor (1e-10). T, the longer-lived
fathers' allele, goes with fewer cigarettes and less COPD. For row 99.

## Reading 2026-11-14, record

> [q532] _embedded.associations[7].reported_trait[0] How many years have you or did you smoke cigarettes? (inv-normal transformed)

> [q533] _embedded.associations[7].snp_allele[0] rs_id rs12461964 effect_allele A

Row 95: the trait and allele of q521's association (228207286): years smoked (q532), effect allele A (q533), so A
"increase" in q521 is A with more years smoked. For row 95.

## Reading 2026-11-14, record

> [q534] _embedded.associations[0] association_id 16533112 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [0.059-0.125] beta 0.092149 unit increase p_value 3.0000000000000004e-08 accession_id GCST003393 pubmed_id 27015805 first_author Pilling LC ci_lower 0.059 ci_upper 0.125

rs62227724 holds one GWAS Catalog association (q534): Pilling 2016's mother's age at death. Nothing else. For row 100.

## Reading 2026-11-14, record

> [q535] page size 200 totalElements 823 totalPages 5 number 0

> [q536] _embedded.associations[7] association_id 228335733 risk_frequency 0.9849 pvalue_description pvalue_mantissa 6 pvalue_exponent -29 multi_snp_haplotype false snp_interaction false range [0.2-0.29] beta 0.2466 unit increase p_value 5.999999999999999e-29 accession_id GCST90475936 pubmed_id 39024449 first_author Verma A ci_lower 0.2 ci_upper 0.29

> [q537] _embedded.associations[7].snp_effect_allele[0] rs11591147-G

> [q538] _embedded.associations[17] association_id 228258753 risk_frequency 0.985 pvalue_description pvalue_mantissa 4 pvalue_exponent -295 multi_snp_haplotype false snp_interaction false range [0.4-0.45] beta 0.4257 unit increase p_value 4e-295 accession_id GCST90475416 pubmed_id 39024449 first_author Verma A ci_lower 0.4 ci_upper 0.45

> [q539] _embedded.associations[25] association_id 136019575 risk_frequency NR pvalue_description pvalue_mantissa 8 pvalue_exponent -11 multi_snp_haplotype false snp_interaction false range - beta - p_value 8e-11 accession_id GCST90309362 pubmed_id 38965376 first_author Carey CE

> [q540] _embedded.associations[25].snp_effect_allele[0] rs11591147-?

rs11591147 (row 3): 823 associations over five pages (q535; all five read), lipids and lipoproteins, PCSK9 levels,
coronary disease, myocardial infarction, aortic stenosis, abdominal aortic aneurysm; none for lifespan, longevity or
death. Coronary atherosclerosis (Verma 2024, MVP): G the risk allele, β 0.25, P 6e-29 (q536, q537); LDL cholesterol
G +0.43, P 4e-295 (q538): T lowers LDL and coronary disease. One record names diabetes, a confirmatory factor of
Carey 2024, P 8e-11, with no allele stated (q539, q540): a trade-off not shown, left open. For row 3.

## Reading 2026-11-14, record

> [q541] page size 200 totalElements 0 totalPages 0 number 0

> [q542] _embedded.associations[5] association_id 49134689 risk_frequency 0.7944 pvalue_description pvalue_mantissa 8 pvalue_exponent -25 multi_snp_haplotype false snp_interaction false range [0.017-0.025] beta 0.0209 unit decrease p_value 8e-25 accession_id GCST009003 pubmed_id 30239722 first_author Pulit SL ci_lower 0.017 ci_upper 0.025

> [q543] _embedded.associations[5].snp_effect_allele[0] rs6944634-C

> [q544] _embedded.associations[3] association_id 101724539 risk_frequency 0.7797 pvalue_description pvalue_mantissa 9 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [0.027-0.048] beta 0.03753776 unit decrease p_value 9e-12 accession_id GCST90162626 pubmed_id 36376295 first_author Levin MG ci_lower 0.027 ci_upper 0.048

> [q545] _embedded.associations[3].snp_effect_allele[0] rs6944634-C

> [q546] _embedded.associations[1] association_id 143803083 risk_frequency 0.7813 pvalue_description pvalue_mantissa 3 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [0.015-0.026] beta 0.0205 unit decrease p_value 3e-12 accession_id GCST90455669 pubmed_id 39406924 first_author Major TJ ci_lower 0.015 ci_upper 0.026

> [q547] _embedded.associations[1].snp_effect_allele[0] rs6944634-C

rs113160991 (row 108): no catalog association (q541). Its CEU proxy rs6944634 (r² 1.00, db-ensembl-116#q733; C with
the lead's G, pmid-30642433#q367) holds six: C lowers body mass index (Pulit 2019, P 8e-25, q542-q543), heart failure
(Levin 2022, P 9e-12, q544-q545; G the risk allele in Enzan 2025, P 5e-9) and serum urate (Major 2024, P 3e-12,
q546-q547), and the parental lifespan line is Timmers'. The longer-lived allele is the leaner, lower-urate,
heart-failure-protective one. For row 108.

## Reading 2026-11-14, record

> [q548] page size 200 totalElements 8 totalPages 1 number 0

> [q549] _embedded.associations[2] association_id 16747 risk_frequency 0.032 pvalue_description pvalue_mantissa 1 pvalue_exponent -25 multi_snp_haplotype false snp_interaction false range [NR] or_per_copy_num 5.3 or_value 5.3 beta - p_value 1e-25 accession_id GCST000863 pubmed_id 21051598 first_author Pereyra F

> [q550] _embedded.associations[2].snp_effect_allele[0] rs2395029-G

> [q551] _embedded.associations[7] association_id 11648 risk_frequency 0.03 pvalue_description pvalue_mantissa 2 pvalue_exponent -26 multi_snp_haplotype false snp_interaction false range [3.10-5.30] or_per_copy_num 4.1 or_value 4.1 beta - p_value 2e-26 accession_id GCST000173 pubmed_id 18369459 first_author Liu Y ci_lower 3.1 ci_upper 5.3

> [q552] _embedded.associations[7].snp_effect_allele[0] rs2395029-C

> [q553] _embedded.associations[1] association_id 41435741 risk_frequency 0.4 pvalue_description pvalue_mantissa 6 pvalue_exponent -97 multi_snp_haplotype false snp_interaction false range [25.38-49.58] or_per_copy_num 35.48 or_value 35.48 beta - p_value 6e-97 accession_id GCST007606 pubmed_id 30661239 first_author Nicoletti P ci_lower 25.38 ci_upper 49.58

rs2395029 (row 130): eight associations (q548). G controls HIV-1 (OR 5.3, P 1e-25, q549-q550; and two more); an AIDS-progression record
names G (OR 3.47), its direction not in the line; psoriasis OR 4.1, P 2e-26, its allele printed C (q551-q552), the opposite strand's name, at a
risk frequency of 0.03, the rare allele's, so G by frequency (derived); flucloxacillin liver injury OR 35, P 6e-97, allele not stated (q553). For row 130.

## Reading 2026-11-14, record

> [q554] page size 200 totalElements 0 totalPages 0 number 0

rs2860197 (row 134): no catalog association under this rsID (q554); the breast cancer and healthspan records sit in
Open Targets' sets (db-opentargets-26.09#q1147). For row 134.

## Reading 2026-11-14, record

> [q555] page size 200 totalElements 4 totalPages 1 number 0

rs3135388 (row 135): four associations (q555): multiple sclerosis (two), oligoclonal bands in multiple sclerosis, and a
protein ratio; none for lifespan. For row 135.

## Reading 2026-11-14, record

> [q556] _embedded.associations[2] association_id 13359 risk_frequency 0.22 pvalue_description pvalue_mantissa 4 pvalue_exponent -225 multi_snp_haplotype false snp_interaction false range [2.46-3.07] or_per_copy_num 2.75 or_value 2.75 beta - p_value 4e-225 accession_id GCST000424 pubmed_id 19525953 first_author De Jager PL ci_lower 2.46 ci_upper 3.07

> [q557] _embedded.associations[2].snp_effect_allele[0] rs3135388-A

rs3135388 (row 135): multiple sclerosis, A the risk allele, OR 2.75 per copy, P 4e-225 (q556-q557; and OR 1.99, P
9e-81): G, the longer-lived allele of the discovery, is multiple sclerosis's non-risk allele, genome-wide (D30.6). For
row 135.

## Reading 2026-11-15, record

> [q558] page size 200 totalElements 1 totalPages 1 number 0

rs12143832 (row 1): one association (q558), Deelen 2019's longevity line itself; nothing else. For row 1.

## Reading 2026-11-15, record

> [q559] page size 200 totalElements 2 totalPages 1 number 0

rs2758603 (row 9): two associations (q559), Deelen's longevity at the 99th percentile and height. For row 9.

## Reading 2026-11-15, record

> [q560] _embedded.associations[2].reported_trait[0] Cigarettes smoked per day

> [q561] _embedded.associations[5].reported_trait[0] Chronic obstructive pulmonary disease

> [q562] _embedded.associations[11] association_id 12827494 risk_frequency 0.15 pvalue_description  pvalue_mantissa 8 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [NR] beta 0.058 unit increase p_value 8e-09 accession_id GCST003185 pubmed_id 26440539 first_author Hancock DB

> [q563] _embedded.associations[11].reported_trait[0] Nicotine dependence

rs2273500 (row 99) in the GWAS Catalog: association 2 is cigarettes smoked per day (q560; its P 3e-64 and allele C, q528,
q529), association 5 chronic obstructive pulmonary disease (q561; P 2e-9, allele C, q530, q531), and association 11
nicotine dependence, Hancock 2015, P 8e-9 (q562, q563). For row 99.

## Reading 2026-11-15, record

> [q564] _embedded.associations[0] association_id 47713591 risk_frequency 0.22 pvalue_description pvalue_mantissa 8 pvalue_exponent -7 multi_snp_haplotype false snp_interaction false range 1.12-1.30 or_per_copy_num 1.21 or_value 1.21 beta - p_value 8e-07 accession_id GCST008601 pubmed_id 31413261 first_author Deelen J ci_lower 1.12 ci_upper 1.3

> [q565] _embedded.associations[0].reported_trait[0] Longevity (age >99th survival percentile)

rs3830412 in the GWAS Catalog: one association, Deelen's 99th-percentile longevity (q564, q565), A, OR 1.21, P 8e-7.
For row 22.

## Reading 2026-11-15, record

> [q566] _embedded.associations[0] association_id 47713570 risk_frequency 0.84 pvalue_description pvalue_mantissa 2 pvalue_exponent -7 multi_snp_haplotype false snp_interaction false range [1.16-1.39] or_per_copy_num 1.2658228 or_value 1.2658228 beta - p_value 2e-07 accession_id GCST008601 pubmed_id 31413261 first_author Deelen J ci_lower 1.16 ci_upper 1.39

> [q567] _embedded.associations[0].reported_trait[0] Longevity (age >99th survival percentile)

rs138762279 in the GWAS Catalog: Deelen's 99th-percentile longevity alone (q566, q567), risk frequency 0.84, the
discovery cohorts' own. For row 34.

## Reading 2026-11-15, record

> [q568] page size 200 totalElements 0 totalPages 0 number 0

rs112262188 in the GWAS Catalog: no association (q568). For row 107.

## Reading 2026-11-15, record

> [q569] _embedded.associations[0] association_id 218960600 risk_frequency 0.013 pvalue_description pvalue_mantissa 2 pvalue_exponent -6 multi_snp_haplotype false snp_interaction false range - beta 2.241 unit increase p_value 2e-06 accession_id GCST90726611 pubmed_id 42176242 first_author Beccacece L

rs113181552 in the GWAS Catalog: Beccacece's Calabrian longevity line alone (q569), T, beta 2.241, P 2e-6. For row 109.

## Reading 2026-11-15, record

> [q570] page size 200 totalElements 0 totalPages 0 number 0

rs116362179 in the GWAS Catalog: no association (q570). For row 110.

## Reading 2026-11-15, record

> [q571] page size 200 totalElements 0 totalPages 0 number 0

rs12189947 in the GWAS Catalog: no association (q571); Hsieh 2026 is not yet curated there. For row 113.

## Reading 2026-11-15, record

> [q572] page size 200 totalElements 0 totalPages 0 number 0

rs1468966 in the GWAS Catalog: no association (q572). For row 119.

## Reading 2026-11-15, record

> [q573] page size 200 totalElements 0 totalPages 0 number 0

rs13963 in the GWAS Catalog: no association (q573); Tanisawa's exome-chip study is not curated there. For row 116.

## Reading 2026-11-15, record

> [q574] page size 200 totalElements 0 totalPages 0 number 0

rs145265196 in the GWAS Catalog: no association (q574). For row 118.

## Reading 2026-11-15, record

> [q575] page size 200 totalElements 0 totalPages 0 number 0

rs147730555 in the GWAS Catalog: no association (q575). For row 120.

## Reading 2026-11-15, record

> [q576] page size 200 totalElements 0 totalPages 0 number 0

rs149554120 in the GWAS Catalog: no association (q576). For row 121.

## Reading 2026-11-15, record

> [q577] page size 200 totalElements 0 totalPages 0 number 0

rs1732444170 and rs184517867 in the GWAS Catalog: no association (q577; the two answers are the same line). For rows
122 and 123.

## Reading 2026-11-15, record

> [q578] page size 200 totalElements 0 totalPages 0 number 0

rs189871470 (row 124): no association in the Catalog (q578). For row 124.

## Reading 2026-11-15, record

> [q579] page size 200 totalElements 0 totalPages 0 number 0

rs199607933 (row 125): no association in the Catalog (q579). For row 125.

## Reading 2026-11-15, record

> [q580] page size 200 totalElements 0 totalPages 0 number 0

rs199678370 (row 126): no association in the Catalog (q580). For row 126.

## Reading 2026-11-15, record

> [q581] page size 200 totalElements 0 totalPages 0 number 0

rs2730486 (row 131): no association in the Catalog (q581). For row 131.

## Reading 2026-11-15, record

> [q582] page size 200 totalElements 0 totalPages 0 number 0

rs3138136 (row 136): no association in the Catalog (q582). For row 136.

## Reading 2026-11-15, record

> [q583] page size 200 totalElements 0 totalPages 0 number 0

rs34459993 (row 137): no association in the Catalog (q583). For row 137.

## Reading 2026-11-16, record

> [q584] _embedded.associations[31] association_id 165236624 risk_frequency NR pvalue_description pvalue_mantissa 7 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta 0.01 unit increase p_value 7e-08 accession_id GCST90551885 pubmed_id 40021682 first_author Park J

> [q585] _embedded.associations[0] association_id 228360386 risk_frequency 0.9232 pvalue_description pvalue_mantissa 3 pvalue_exponent -24 multi_snp_haplotype false snp_interaction false range [1.1-1.54] beta 1.322 unit decrease p_value 2.9999999999999996e-24 accession_id GCST90476533 pubmed_id 39024449 first_author Verma A ci_lower 1.1 ci_upper 1.54

rs35705950 (row 138): the one lifespan association is Park 2025's men's GWAS (GCST90551885), T β 0.01 on reduced lifespan, P 7e-8, short of genome-wide (q584); the rest are lung and blood traits, among them idiopathic pulmonary fibrosis (EFO_0000768; G, the other allele, OR given as a decrease, P 3e-24, q585). For row 138.

## Reading 2026-11-16, record

> [q586] _embedded.associations[34] association_id 105680586 risk_frequency NR pvalue_description pvalue_mantissa 4 pvalue_exponent -14 multi_snp_haplotype false snp_interaction false range [0.87-0.92] or_per_copy_num 0.89 or_value 0.89 beta - p_value 4e-14 accession_id GCST90270935 pubmed_id 37198478 first_author Pairo-Castineira E ci_lower 0.87 ci_upper 0.92

> [q587] _embedded.associations[34].snp_effect_allele[0] rs35705950-T

> [q588] _embedded.associations[35] association_id 105680304 risk_frequency 0.11 pvalue_description pvalue_mantissa 4 pvalue_exponent -14 multi_snp_haplotype false snp_interaction false range [0.82-0.89] or_per_copy_num 0.86 or_value 0.86 beta - p_value 4e-14 accession_id GCST90270934 pubmed_id 37198478 first_author Pairo-Castineira E ci_lower 0.82 ci_upper 0.89

> [q589] _embedded.associations[35].snp_effect_allele[0] rs35705950-T

rs35705950 and COVID-19 (row 138): T OR 0.89 for hospitalisation, P 4e-14 (q586, q587), and 0.86 for critical illness, P 4e-14 (q588, q589), Pairo-Castineira 2023; T, the fibrosis and shorter-life allele, is the protective side, so G, the longer-lived, is the side with more severe COVID-19. A 'COVID-19 severity' line (GCST90274862) prints its effect allele as '?' and is set aside. For row 138.

## Reading 2026-11-16, record

> [q590] page size 200 totalElements 0 totalPages 0 number 0

rs41419545 (row 140): no association in the catalogue (q590). For row 140.

## Reading 2026-11-16, record

> [q591] page size 200 totalElements 0 totalPages 0 number 0

rs62502826 (row 147): no association in the catalogue. For row 147.

## Reading 2026-11-16, record

> [q592] page size 200 totalElements 0 totalPages 0 number 0

rs75526165 (row 150): no association in the catalogue. For row 150.

## Reading 2026-11-16, record

> [q593] page size 200 totalElements 0 totalPages 0 number 0

rs6543176 (row 148): no association in the catalogue. For row 148.

## Reading 2026-11-16, record

> [q594] page size 200 totalElements 0 totalPages 0 number 0

rs75571981 (row 151): no association in the catalogue. For row 151.

## Reading 2026-11-16, record

> [q595] _embedded.associations[1] association_id 218986576 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -6 multi_snp_haplotype false snp_interaction false range - or_per_copy_num 0.32 or_value 0.32 beta - p_value 3e-06 accession_id GCST90854193 pubmed_id 41949656 first_author Hsieh MS

> [q596] _embedded.associations[0] association_id 218986602 risk_frequency NR pvalue_description pvalue_mantissa 5 pvalue_exponent -6 multi_snp_haplotype false snp_interaction false range - or_per_copy_num 0.28 or_value 0.28 beta - p_value 4.9999999999999996e-06 accession_id GCST90854194 pubmed_id 41949656 first_author Hsieh MS

rs75737809 (row 152): Hsieh 2026's two lines, OR 0.32, P 3e-6 (q595) and 0.28, P 5e-6 (q596), the effect allele printed as '?'. For row 152.

## Reading 2026-11-16, record

> [q597] page size 200 totalElements 0 totalPages 0 number 0

rs7754015 (row 154): no association in the catalogue. For row 154.

## Reading 2026-11-16, record

> [q598] page size 200 totalElements 0 totalPages 0 number 0

rs79159347 (row 155): no association in the catalogue. For row 155.

## Reading 2026-11-16, record

> [q599] page size 200 totalElements 0 totalPages 0 number 0

rs79645902 (row 156): no association in the catalogue. For row 156.

## Reading 2026-11-16, record

> [q600] page size 200 totalElements 0 totalPages 0 number 0

rs117082375 (row 111): no association in the catalogue. For row 111.

## Reading 2026-11-16, record

> [q601] page size 200 totalElements 0 totalPages 0 number 0

rs373800184 (row 139): no association in the catalogue. For row 139.

## Reading 2026-11-16, record

> [q602] page size 200 totalElements 0 totalPages 0 number 0

rs61838431 (row 146): no association in the catalogue. For row 146.

## Reading 2026-11-16, record

> [q603] _embedded.associations[0] association_id 10076208 risk_frequency 0.75 pvalue_description pvalue_mantissa 5 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range 1.15–1.34 or_per_copy_num 1.24 or_value 1.24 beta - p_value 5e-08 accession_id GCST002599 pubmed_id 25199915 first_author Broer L

> [q604] _embedded.associations[0].snp_allele[0] rs_id rs1416280 effect_allele C

> [q605] _embedded.associations[0].reported_trait[0] Longevity (90 years and older)

rs1416280 (row 117): Broer 2015 (GCST002599), C the risk (effect) allele at 0.75, OR 1.24 (1.15–1.34) per C, P 5e-8 (q603, q604), for longevity at 90 and older (q605). For row 117.

## Reading 2026-11-16, record

> [q606] page size 200 totalElements 0 totalPages 0 number 0

rs200818241 (row 127): no association in the catalogue. For row 127.

## Reading 2026-11-16, record

> [q607] _embedded.associations[0] association_id 118863923 risk_frequency 0.334 pvalue_description pvalue_mantissa 2 pvalue_exponent -16 multi_snp_haplotype false snp_interaction false range [1.04-1.06] or_per_copy_num 1.05 or_value 1.05 beta - p_value 2e-16 accession_id GCST90274714 pubmed_id 37945903 first_author Wang A ci_lower 1.04 ci_upper 1.06

> [q608] _embedded.associations[0].reported_trait[0] Prostate cancer

> [q609] _embedded.associations[0].snp_effect_allele[0] rs9275160-A

> [q610] _embedded.associations[2] association_id 100841412 risk_frequency 0.383776 pvalue_description pvalue_mantissa 1 pvalue_exponent -19 multi_snp_haplotype false snp_interaction false range [0.2-0.32] beta 0.26096 unit decrease p_value 1e-19 accession_id GCST90162093 pubmed_id 36168886 first_author Thareja G ci_lower 0.2 ci_upper 0.32

> [q611] _embedded.associations[2].reported_trait[0] Complement C4 levels

> [q612] _embedded.associations[4] association_id 64607051 risk_frequency NR pvalue_description pvalue_mantissa 9 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [1.03-1.06] or_per_copy_num 1.044 or_value 1.044 beta - p_value 9e-08 accession_id GCST011049 pubmed_id 33398198 first_author Conti DV ci_lower 1.03 ci_upper 1.06

> [q613] _embedded.associations[4].reported_trait[0] Prostate cancer

> [q614] page size 200 totalElements 5 totalPages 1 number 0

rs9275160 (row 159): five associations, every one on A: prostate cancer (Wang, GCST90274714, OR 1.05, P 2e-16; q607, q608, q609; and GCST90274713), complement C4 levels (Thareja, β +0.26, P 1e-19; q610, q611), prostate cancer again (Conti, P 9e-8; q612, q613), and Atkins' frailty index (q614). For row 159.

## Reading 2026-11-16, record

> [q615] _embedded.associations[17] association_id 33527 risk_frequency 0.252 pvalue_description pvalue_mantissa 3 pvalue_exponent -31 multi_snp_haplotype false snp_interaction false range [0.081-0.113] beta 0.097 unit decrease p_value 3.0000000000000003e-31 accession_id GCST001936 pubmed_id 23535734 first_author Codd V ci_lower 0.081 ci_upper 0.113

> [q616] _embedded.associations[17].efo_traits[0] efo_id OBA_0003784 efo_trait chromosome, telomeric region length

> [q617] _embedded.associations[17].snp_effect_allele[0] rs10936599-T

> [q618] _embedded.associations[9] association_id 97278039 risk_frequency NR pvalue_description pvalue_mantissa 8 pvalue_exponent -95 multi_snp_haplotype false snp_interaction false range - beta - p_value 8e-95 accession_id GCST90103979 pubmed_id 35530816 first_author Taub MA

> [q619] _embedded.associations[9].efo_traits[0] efo_id OBA_0003784 efo_trait chromosome, telomeric region length

> [q620] _embedded.associations[9].snp_effect_allele[0] rs10936599-?

> [q621] _embedded.associations[3] association_id 227546727 risk_frequency 0.7312 pvalue_description pvalue_mantissa 1 pvalue_exponent -14 multi_snp_haplotype false snp_interaction false range [1.06062165939086-1.10432159730391] or_per_copy_num 1.082 or_value 1.082 beta - p_value 1e-14 accession_id GCST90726395 pubmed_id 42706231 first_author Prokunina-Olsson L ci_lower 1.0606216 ci_upper 1.1043216

> [q622] _embedded.associations[3].efo_traits[0] efo_id MONDO_0001187 efo_trait urinary bladder cancer

> [q623] _embedded.associations[3].snp_effect_allele[0] rs10936599-C

> [q624] _embedded.associations[11] association_id 91633807 risk_frequency 0.76 pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [NR] or_per_copy_num 1.16 or_value 1.16 beta - p_value 3.0000000000000004e-08 accession_id GCST012396 pubmed_id 33875642 first_author Duran-Lozano L

> [q625] _embedded.associations[11].efo_traits[0] efo_id MONDO_0009693 efo_trait plasma cell myeloma

> [q626] _embedded.associations[11].snp_effect_allele[0] rs10936599-C

> [q627] _embedded.associations[14] association_id 38323 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [1.17-1.35] or_per_copy_num 1.26 or_value 1.26 beta - p_value 2e-09 accession_id GCST002299 pubmed_id 24292274 first_author Speedy HE ci_lower 1.17 ci_upper 1.35

> [q628] _embedded.associations[14].efo_traits[0] efo_id MONDO_0004948 efo_trait B-cell chronic lymphocytic leukemia

> [q629] _embedded.associations[14].snp_effect_allele[0] rs10936599-C

> [q630] _embedded.associations[19] association_id 16561 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [1.04-1.10] or_per_copy_num 1.04 or_value 1.04 beta - p_value 3.0000000000000004e-08 accession_id GCST000843 pubmed_id 20972440 first_author Houlston RS ci_lower 1.04 ci_upper 1.1

> [q631] _embedded.associations[19].efo_traits[0] efo_id MONDO_0005575 efo_trait colorectal cancer

> [q632] _embedded.associations[19].snp_effect_allele[0] rs10936599-C

> [q633] _embedded.associations[10] association_id 97179339 risk_frequency 0.75 pvalue_description pvalue_mantissa 8 pvalue_exponent -19 multi_snp_haplotype false snp_interaction false range [0.056-0.088] beta 0.0719 unit increase p_value 8e-19 accession_id GCST90103971 pubmed_id 34813871 first_author Liyanage U ci_lower 0.056 ci_upper 0.088

> [q634] _embedded.associations[10].efo_traits[0] efo_id MONDO_0005012 efo_trait cutaneous melanoma

> [q635] _embedded.associations[10].snp_effect_allele[0] rs10936599-C

rs10936599 (row 23), 21 associations in the catalogue. Telomere length, trait OBA_0003784 ("chromosome, telomeric
region length"): Codd 2013 (GCST001936) T, β 0.097 decrease, P 3e-31, T at 0.252 (q615, q616, q617); Taub 2022
(GCST90103979) P 8e-95, the allele unrecorded (q618, q619, q620). Cancers on C, the longer-telomere allele:
bladder cancer OR 1.082, P 1e-14 (q621 to q623); multiple myeloma OR 1.16, P 3e-8 (q624 to q626); chronic
lymphocytic leukaemia OR 1.26, P 2e-9 (q627 to q629); colorectal cancer OR 1.04, P 3e-8 (q630 to q632);
cutaneous melanoma β 0.072 increase, P 8e-19 (q633 to q635). The other lines (eosinophils, uterine fibroids,
further cancers, some with the allele unrecorded or on a strand-ambiguous G or A) are named, not read. For row 23.

## Reading 2026-11-16, record

> [q636] _embedded.associations[32] association_id 97278059 risk_frequency NR pvalue_description pvalue_mantissa 5 pvalue_exponent -79 multi_snp_haplotype false snp_interaction false range - beta - p_value 5e-79 accession_id GCST90103979 pubmed_id 35530816 first_author Taub MA

> [q637] _embedded.associations[32].efo_traits[0] efo_id OBA_0003784 efo_trait chromosome, telomeric region length

> [q638] _embedded.associations[32].snp_effect_allele[0] rs2736100-?

> [q639] _embedded.associations[49] association_id 40037 risk_frequency NR pvalue_description pvalue_mantissa 4 pvalue_exponent -6 multi_snp_haplotype false snp_interaction false range [NR] beta 0.0808 unit increase p_value 4e-06 accession_id GCST002341 pubmed_id 24465473 first_author Liu Y

> [q640] _embedded.associations[49].efo_traits[0] efo_id OBA_0003784 efo_trait chromosome, telomeric region length

> [q641] _embedded.associations[49].snp_effect_allele[0] rs2736100-C

> [q642] _embedded.associations[55] association_id 18594 risk_frequency 0.41 pvalue_description pvalue_mantissa 1 pvalue_exponent -27 multi_snp_haplotype false snp_interaction false range [1.22-1.33] or_per_copy_num 1.27 or_value 1.27 beta - p_value 1e-27 accession_id GCST001140 pubmed_id 21725308 first_author Hu Z ci_lower 1.22 ci_upper 1.33

> [q643] _embedded.associations[55].efo_traits[0] efo_id MONDO_0005138 efo_trait lung carcinoma

> [q644] _embedded.associations[55].snp_effect_allele[0] rs2736100-C

> [q645] _embedded.associations[38] association_id 36787529 risk_frequency 0.59 pvalue_description pvalue_mantissa 2 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [1.18-1.35] or_per_copy_num 1.27 or_value 1.27 beta - p_value 2e-12 accession_id GCST007842 pubmed_id 30714141 first_author Chen H ci_lower 1.18 ci_upper 1.35

> [q646] _embedded.associations[38].efo_traits[0] efo_id MONDO_0021042 efo_trait glioma

> [q647] _embedded.associations[38].snp_effect_allele[0] rs2736100-C

> [q648] _embedded.associations[26] association_id 131719998 risk_frequency 0.500216 pvalue_description pvalue_mantissa 3 pvalue_exponent -13 multi_snp_haplotype false snp_interaction false range [1.15540075176731-1.28471050022817] or_per_copy_num 1.2183412 or_value 1.2183412 beta - p_value 3.0000000000000003e-13 accession_id GCST90102620 pubmed_id 35835912 first_author Kar SP ci_lower 1.1554008 ci_upper 1.2847105

> [q649] _embedded.associations[26].efo_traits[0] efo_id EFO_0010819 efo_trait clonal hematopoiesis

> [q650] _embedded.associations[26].snp_effect_allele[0] rs2736100-C

> [q651] _embedded.associations[43] association_id 21659000 risk_frequency 0.5 pvalue_description pvalue_mantissa 8 pvalue_exponent -20 multi_snp_haplotype false snp_interaction false range 1.22–1.37 or_per_copy_num 1.29 or_value 1.29 beta - p_value 8e-20 accession_id GCST004713 pubmed_id 28604732 first_author Wang Z

> [q652] _embedded.associations[43].efo_traits[0] efo_id MONDO_0010108 efo_trait testicular germ cell tumor

> [q653] _embedded.associations[43].snp_effect_allele[0] rs2736100-A

> [q654] _embedded.associations[62] association_id 11907 risk_frequency 0.41 pvalue_description pvalue_mantissa 3 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [1.61-2.78] or_per_copy_num 2.11 or_value 2.11 beta - p_value 3.0000000000000004e-08 accession_id GCST000238 pubmed_id 18835860 first_author Mushiroda T ci_lower 1.61 ci_upper 2.78

> [q655] _embedded.associations[62].efo_traits[0] efo_id EFO_0000768 efo_trait idiopathic pulmonary fibrosis

> [q656] _embedded.associations[62].snp_effect_allele[0] rs2736100-A

> [q657] _embedded.associations[50] association_id 30632 risk_frequency 0.49 pvalue_description pvalue_mantissa 2 pvalue_exponent -19 multi_snp_haplotype false snp_interaction false range [1.27-1.49] or_per_copy_num 1.37 or_value 1.37 beta - p_value 2e-19 accession_id GCST001968 pubmed_id 23583980 first_author Fingerlin TE ci_lower 1.27 ci_upper 1.49

> [q658] _embedded.associations[50].efo_traits[0] efo_id MONDO_0015925 efo_trait interstitial lung disease

> [q659] _embedded.associations[50].snp_effect_allele[0] rs2736100-A

> [q660] _embedded.associations[33] association_id 88923238 risk_frequency 0.4977 pvalue_description pvalue_mantissa 3 pvalue_exponent -11 multi_snp_haplotype false snp_interaction false range [0.14-0.26] beta 0.2024 unit decrease p_value 3e-11 accession_id GCST90014290 pubmed_id 34187551 first_author McCartney DL ci_lower 0.14 ci_upper 0.26

> [q661] _embedded.associations[33].efo_traits[0] efo_id EFO_0022597 efo_trait aging

> [q662] _embedded.associations[33].snp_effect_allele[0] rs2736100-A

rs2736100 (row 30), 63 associations. Telomere length (OBA_0003784): Taub 2022 (GCST90103979) P 5e-79, the allele
unrecorded (q636 to q638); Liu 2014 C increase 0.081, P 4e-6, sub-genome-wide (q639 to q641). On C, the
longer-telomere allele: lung carcinoma OR 1.27, P 1e-27 (q642 to q644); glioma 1.27, P 2e-12 (q645 to q647);
clonal haematopoiesis 1.22, P 3e-13 (q648 to q650). On A, the shorter: testicular germ cell tumour 1.29, P 8e-20
(q651 to q653); idiopathic pulmonary fibrosis 2.11, P 3e-8 (q654 to q656); interstitial lung disease 1.37,
P 2e-19 (q657 to q659). McCartney 2021's epigenetic ageing ("aging", EFO_0022597) A decrease 0.20, P 3e-11
(q660 to q662). Blood-cell counts, proteins and other lines named, not read. For row 30.

## Reading 2026-11-16, record

> [q663] _embedded.associations[0] association_id 88923244 risk_frequency 0.0532 pvalue_description pvalue_mantissa 4 pvalue_exponent -54 multi_snp_haplotype false snp_interaction false range [0.95-1.22] beta 1.0823 unit decrease p_value 4e-54 accession_id GCST90014290 pubmed_id 34187551 first_author McCartney DL ci_lower 0.95 ci_upper 1.22

> [q664] _embedded.associations[0].efo_traits[0] efo_id EFO_0022597 efo_trait aging

> [q665] _embedded.associations[0].reported_trait[0] Intrinsic epigenetic age acceleration

> [q666] _embedded.associations[0].snp_effect_allele[0] rs10949481-T

rs10949481 (row 105): one association, McCartney 2021 (GCST90014290), intrinsic epigenetic age acceleration, trait EFO_0022597 ("aging"): T, β 1.08 years decrease (0.95 to 1.22), P 4e-54, T at 0.053 (q663 to q666). For row 105.

## Reading 2026-11-16, record

> [q667] _embedded.associations[4] association_id 130459873 risk_frequency 0.90515 pvalue_description pvalue_mantissa 1 pvalue_exponent -109 multi_snp_haplotype false snp_interaction false range [0.12-0.15] beta 0.13704 unit decrease p_value 1e-109 accession_id GCST90268497 pubmed_id 37587338 first_author Gupta R ci_lower 0.12 ci_upper 0.15

> [q668] _embedded.associations[4].efo_traits[0] efo_id EFO_0006312 efo_trait mitochondrial DNA measurement

> [q669] _embedded.associations[4].reported_trait[0] Mitochondrial DNA copy number (adjusted)

> [q670] _embedded.associations[4].snp_effect_allele[0] rs11085147-C

> [q671] _embedded.associations[5] association_id 94038306 risk_frequency 0.0223642 pvalue_description pvalue_mantissa 2 pvalue_exponent -95 multi_snp_haplotype false snp_interaction false range [0.069-0.083] beta 0.0756 unit increase p_value 2e-95 accession_id GCST90026371 pubmed_id 35023831 first_author Chong M ci_lower 0.069 ci_upper 0.083

> [q672] _embedded.associations[5].efo_traits[0] efo_id EFO_0006312 efo_trait mitochondrial DNA measurement

> [q673] _embedded.associations[5].reported_trait[0] Mitochondrial DNA copy number

> [q674] _embedded.associations[5].snp_effect_allele[0] rs11085147-T

rs11085147 (row 106), six associations. Mitochondrial DNA copy number, trait EFO_0006312: Gupta 2023 (GCST90268497,
adjusted) C 0.137 SD decrease, P 1e-109, C at 0.905 (q667 to q670); Chong 2022 (GCST90026371, PMID 35023831, UK
Biobank) T 0.076 increase, P 2e-95 (q671 to q674); both T the higher copy number, both UK Biobank. The raw
copy-number line and three protein levels (MRPL58, GADD45GIP1, NGRN, T higher) named, not read. For row 106.

## Reading 2026-11-16, record

> [q675] _embedded.associations[0] association_id 97355947 risk_frequency 0.024 pvalue_description pvalue_mantissa 2 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [1.08-2.11] beta 1.5943 unit increase p_value 2e-09 accession_id GCST90104403 pubmed_id 34962275 first_author Lin WY ci_lower 1.08 ci_upper 2.11

> [q676] _embedded.associations[0].efo_traits[0] efo_id EFO_0000473 efo_trait epigenetic status

> [q677] _embedded.associations[0].reported_trait[0] DNA methylation GrimAge acceleration

> [q678] _embedded.associations[0].snp_effect_allele[0] rs117530284-A

rs117530284 (row 112): one association, Lin 2022 (GCST90104403), GrimAge acceleration, trait EFO_0000473 ("epigenetic status"): A +1.59 years (1.08 to 2.11), P 2e-9, A at 0.024 (q675 to q678). For row 112.

## Reading 2026-11-16, record

> [q679] _embedded.associations[1].efo_traits[0] efo_id EFO_0006312 efo_trait mitochondrial DNA measurement

> [q680] _embedded.associations[1] association_id 130459693 risk_frequency 0.58199 pvalue_description pvalue_mantissa 8 pvalue_exponent -96 multi_snp_haplotype false snp_interaction false range [0.067-0.081] beta 0.07441 unit decrease p_value 8e-96 accession_id GCST90268497 pubmed_id 37587338 first_author Gupta R ci_lower 0.067 ci_upper 0.081

> [q681] _embedded.associations[1].reported_trait[0] Mitochondrial DNA copy number (adjusted)

> [q682] _embedded.associations[1].snp_effect_allele[0] rs12247015-A

> [q683] _embedded.associations[2] association_id 94038205 risk_frequency 0.445288 pvalue_description pvalue_mantissa 1 pvalue_exponent -55 multi_snp_haplotype false snp_interaction false range [0.03-0.038] beta 0.0337 unit increase p_value 1e-55 accession_id GCST90026371 pubmed_id 35023831 first_author Chong M ci_lower 0.03 ci_upper 0.038

> [q684] _embedded.associations[2].reported_trait[0] Mitochondrial DNA copy number

> [q685] _embedded.associations[2].snp_effect_allele[0] rs12247015-G

rs12247015 (row 114), three associations, all mitochondrial DNA copy number, trait EFO_0006312 (q679): Gupta 2023's
adjusted GWAS (GCST90268497) A 0.074 decrease, P 8e-96, A at 0.582 (q680 to q682), the paper's Table 2 line; its
raw line (P 5e-66) named; Chong 2022 (GCST90026371, PMID 35023831, UK Biobank) G 0.034 increase, P 1e-55 (q683 to
q685): the same side, the same people. No other trait. For row 114.

## Reading 2026-11-16, record

> [q686] _embedded.associations[0] association_id 88923648 risk_frequency 0.8216 pvalue_description pvalue_mantissa 6 pvalue_exponent -25 multi_snp_haplotype false snp_interaction false range [1.09-1.6] beta 1.3482 unit decrease p_value 6.0000000000000005e-25 accession_id GCST90014294 pubmed_id 34187551 first_author McCartney DL ci_lower 1.09 ci_upper 1.6

> [q687] _embedded.associations[0].efo_traits[0] efo_id EFO_0022597 efo_trait aging

> [q688] _embedded.associations[0].reported_trait[0] DNA methylation GrimAge acceleration

> [q689] _embedded.associations[0].snp_effect_allele[0] rs2227341-G

rs2227341 (row 128), one association: McCartney 2021's GrimAge acceleration (GCST90014294), G at 0.82, 1.35 years decrease, P 6e-25 (q686, q688, q689), the paper's Table S4 line; trait as mapped (q687). No other trait. For row 128.

## Reading 2026-11-16, record

> [q690] . initial_sample_size 34,461 European ancestry individuals replication_sample_size NA gxe false gxg false snp_count 7567980 imputed true pooled false accession_id GCST90014290 full_summary_stats_available true user_requested false pubmed_id 34187551 platforms Affymetrix,Illumina [7567980] (imputed) disease_trait Intrinsic epigenetic age acceleration full_summary_stats http://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST90014001-GCST90015000/GCST90014290 terms_of_license https://creativecommons.org/publicdomain/zero/1.0/

> [q691] cohort[3] BLSA

> [q692] cohort[6] FHS

> [q693] cohort[9] InCHIANTI

> [q694] cohort[11] LBC21

> [q695] cohort[12] LBC36

> [q696] cohort[23] TwinsUK

GCST90014290, McCartney 2021's European IEAA GWAS: 34,461 European ancestry individuals (q690); among its 27 cohorts BLSA,
FHS, InCHIANTI, LBC21, LBC36 and TwinsUK (q691 to q696), five of Lu 2018's eight cohorts. For row 105.

## Reading 2026-11-16, record

> [q697] _embedded.associations[2].snp_effect_allele[0] rs9275160-A

rs9275160 (row 159): the complement C4 association's allele is A (q697); with q610's 'beta 0.26096 unit decrease', A lowers C4 levels (the Catalog stores |β| with a direction word), so the row's earlier 'A raises C4' was reversed (D38.9). For row 159.

## Reading 2026-11-16, record

> [q698] _embedded.associations[9] association_id 27364879 risk_frequency 0.36 pvalue_description pvalue_mantissa 1 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [0.46-0.81] beta 0.631 unit increase p_value 1e-12 accession_id GCST005287 pubmed_id 29374233 first_author Lu AT ci_lower 0.46 ci_upper 0.81

> [q699] _embedded.associations[9].efo_traits[0] efo_id EFO_0022597 efo_trait aging

> [q700] _embedded.associations[9].snp_effect_allele[0] rs2736099-A

> [q701] _embedded.associations[8] association_id 55275996 risk_frequency 0.3668 pvalue_description pvalue_mantissa 9 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range [0.25-0.49] beta 0.3726 unit increase p_value 9e-10 accession_id GCST009604 pubmed_id 31738745 first_author Gibson J ci_lower 0.25 ci_upper 0.49

> [q702] _embedded.associations[8].snp_effect_allele[0] rs2736099-A

> [q703] _embedded.associations[7] association_id 131085845 risk_frequency NR pvalue_description pvalue_mantissa 1 pvalue_exponent -23 multi_snp_haplotype false snp_interaction false range [0.073-0.108] beta 0.0902276 unit decrease p_value 1e-23 accession_id GCST90328132 pubmed_id 38182794 first_author Choquet H ci_lower 0.073 ci_upper 0.108

> [q704] _embedded.associations[7].efo_traits[0] efo_id MONDO_0020804 efo_trait basal cell carcinoma

> [q705] _embedded.associations[7].snp_effect_allele[0] rs2736099-G

> [q706] _embedded.associations[6] association_id 214159544 risk_frequency NR pvalue_description pvalue_mantissa 3 pvalue_exponent -13 multi_snp_haplotype false snp_interaction false range [1.3-1.56] or_per_copy_num 1.43 or_value 1.43 beta - p_value 3.0000000000000003e-13 accession_id GCST90435343 pubmed_id 39948438 first_author Wen S ci_lower 1.3 ci_upper 1.56

> [q707] _embedded.associations[6].reported_trait[0] Clonal hematopoiesis (TET2 mutation)

> [q708] _embedded.associations[6].snp_effect_allele[0] rs2736099-A

rs2736099 (row 132), ten associations. Lu 2018's IEAA (GCST005287), A +0.631, P 1e-12, A at 0.36, trait EFO_0022597
(q698 to q700); Gibson 2019's IEAA (GCST009604, PMID 31738745, paper unread) A +0.37, P 9e-10 (q701, q702). Basal
cell carcinoma (Choquet 2024, GCST90328132): G 0.090 decrease, P 1e-23, so A raises it (q703 to q705); clonal
haematopoiesis with TET2 mutation (Wen, GCST90435343): A, OR 1.43, P 3e-13 (q706 to q708). Blood cell fractions,
neutrophil-to-lymphocyte ratio and ICAM2 named, not read. For row 132.

## Reading 2026-11-16, record

> [q709] _embedded.associations[61] association_id 55993984 risk_frequency 0.59 pvalue_description pvalue_mantissa 3 pvalue_exponent -31 multi_snp_haplotype false snp_interaction false range [0.052-0.076] beta 0.064 unit decrease p_value 3.0000000000000003e-31 accession_id GCST009856 pubmed_id 32109421 first_author Li C ci_lower 0.052 ci_upper 0.076

> [q710] _embedded.associations[61].efo_traits[0] efo_id OBA_0003784 efo_trait chromosome, telomeric region length

> [q711] _embedded.associations[61].snp_effect_allele[0] rs2853677-A

> [q712] _embedded.associations[10] association_id 219075349 risk_frequency 0.61 pvalue_description pvalue_mantissa 1 pvalue_exponent -75 multi_snp_haplotype false snp_interaction false range [0.82-0.86] or_per_copy_num 0.84 or_value 0.84 beta - p_value 1e-75 accession_id GCST90482691 pubmed_id 42152146 first_author Zhu M ci_lower 0.82 ci_upper 0.86

> [q713] _embedded.associations[10].reported_trait[0] Lung cancer

> [q714] _embedded.associations[10].snp_effect_allele[0] rs2853677-A

> [q715] _embedded.associations[11] association_id 217875669 risk_frequency 0.5918 pvalue_description pvalue_mantissa 7 pvalue_exponent -12 multi_snp_haplotype false snp_interaction false range [0.91-0.95] or_per_copy_num 0.93 or_value 0.93 beta - p_value 7e-12 accession_id GCST90838662 pubmed_id 42000752 first_author Dai H ci_lower 0.91 ci_upper 0.95

> [q716] _embedded.associations[11].reported_trait[0] Renal cell carcinoma

> [q717] _embedded.associations[11].snp_effect_allele[0] rs2853677-A

> [q718] _embedded.associations[13] association_id 214160110 risk_frequency 0.578 pvalue_description pvalue_mantissa 1 pvalue_exponent -115 multi_snp_haplotype false snp_interaction false range [0.74-0.776] or_per_copy_num 0.758 or_value 0.758 beta - p_value 1e-115 accession_id GCST90435366 pubmed_id 39948438 first_author Wen S ci_lower 0.74 ci_upper 0.776

> [q719] _embedded.associations[13].reported_trait[0] Clonal hematopoiesis (DNMT3A mutation)

> [q720] _embedded.associations[13].snp_effect_allele[0] rs2853677-A

rs2853677 (row 133), 73 associations. Li 2020's leukocyte telomere length (A 0.064 decrease, P 3e-31, trait OBA_0003784;
q709 to q711). Lung cancer: A OR 0.84, P 1e-75 (q712 to q714), so G raises it; renal cell carcinoma: A OR 0.93, P
7e-12 (q715 to q717); clonal haematopoiesis with DNMT3A mutation: A OR 0.758, P 1e-115 (q718 to q720). Blood
cell traits, protein levels and the rest named, not read. For row 133.

## Reading 2026-11-16, record

> [q721] _embedded.associations[1] association_id 130459943 risk_frequency 0.9404 pvalue_description pvalue_mantissa 5 pvalue_exponent -48 multi_snp_haplotype false snp_interaction false range [0.094-0.123] beta 0.10863 unit increase p_value 5e-48 accession_id GCST90268497 pubmed_id 37587338 first_author Gupta R ci_lower 0.094 ci_upper 0.123

> [q722] _embedded.associations[1].efo_traits[0] efo_id EFO_0006312 efo_trait mitochondrial DNA measurement

> [q723] _embedded.associations[1].reported_trait[0] Mitochondrial DNA copy number (adjusted)

> [q724] _embedded.associations[1].snp_effect_allele[0] rs4148974-C

> [q725] _embedded.associations[0] association_id 130460500 risk_frequency 0.9404 pvalue_description pvalue_mantissa 5 pvalue_exponent -38 multi_snp_haplotype false snp_interaction false range [0.081-0.11] beta 0.095391 unit increase p_value 4.999999999999999e-38 accession_id GCST90268498 pubmed_id 37587338 first_author Gupta R ci_lower 0.081 ci_upper 0.11

> [q726] _embedded.associations[0].reported_trait[0] Mitochondrial DNA copy number (raw)

rs4148974 (row 141), two associations, both Gupta 2023's: adjusted mtDNA copy number, C β 0.10863 increase, P 5e-48
(GCST90268497, trait EFO_0006312; q721 to q724); raw copy number, C 0.0954, P 5e-38 (q725, q726). No disease line.
For row 141.

## Reading 2026-11-16, record

> [q727] _embedded.associations[0] association_id 227788359 risk_frequency 0.779553 pvalue_description pvalue_mantissa 8 pvalue_exponent -53 multi_snp_haplotype false snp_interaction false range [0.046072-0.059606] beta 0.052839 standard deviation unit increase p_value 8e-53 accession_id GCST91000685 pubmed_id 38789417 first_author Keener R ci_lower 0.046072 ci_upper 0.059606

> [q728] _embedded.associations[0].efo_traits[0] efo_id OBA_0003784 efo_trait chromosome, telomeric region length

> [q729] _embedded.associations[0].snp_effect_allele[0] rs4691895-C

> [q730] _embedded.associations[2] association_id 55993972 risk_frequency 0.78 pvalue_description pvalue_mantissa 2 pvalue_exponent -21 multi_snp_haplotype false snp_interaction false range [0.046-0.07] beta 0.058 unit increase p_value 2e-21 accession_id GCST009856 pubmed_id 32109421 first_author Li C ci_lower 0.046 ci_upper 0.07

> [q731] _embedded.associations[2].snp_effect_allele[0] rs4691895-C

rs4691895 (row 143), three associations, all telomere length: Keener 2024 (PMID 38789417, GCST91000685) C +0.0528 SD,
P 8e-53, C at 0.78 (q727 to q729; trait OBA_0003784); Li 2020 C +0.058, P 2e-21 (q730, q731); Taub 2022's line
(GCST90103979, P 3e-26) prints no allele. No disease line. For row 143.

## Reading 2026-11-16, record

> [q732] _embedded.associations[1] association_id 55993990 risk_frequency 0.29 pvalue_description pvalue_mantissa 1 pvalue_exponent -13 multi_snp_haplotype false snp_interaction false range [0.029-0.053] beta 0.041 unit decrease p_value 1e-13 accession_id GCST009856 pubmed_id 32109421 first_author Li C ci_lower 0.029 ci_upper 0.053

> [q733] _embedded.associations[1].efo_traits[0] efo_id OBA_0003784 efo_trait chromosome, telomeric region length

> [q734] _embedded.associations[1].snp_effect_allele[0] rs59294613-A

> [q735] _embedded.associations[2] association_id 24084515 risk_frequency NR pvalue_description pvalue_mantissa 8 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range [1.06-1.14] or_per_copy_num 1.0982976 or_value 1.0982976 beta - p_value 8e-08 accession_id GCST004710 pubmed_id 28598434 first_author Scelo G ci_lower 1.06 ci_upper 1.14

> [q736] _embedded.associations[2].efo_traits[0] efo_id MONDO_0005086 efo_trait renal cell carcinoma

> [q737] _embedded.associations[2].snp_effect_allele[0] rs59294613-?

rs59294613 (row 144), three associations: Li 2020's leukocyte telomere length, A 0.041 decrease, P 1e-13 (q732 to q734);
renal cell carcinoma (Scelo 2017, GCST004710), OR 1.098 (1.06 to 1.14), P 8e-8, short of genome-wide, the allele
not printed (q735 to q737); Taub 2022's telomere line (P 6e-25) prints no allele. For row 144.

## Reading 2026-11-16, record

> [q738] _embedded.associations[129] association_id 55993978 risk_frequency 0.33 pvalue_description pvalue_mantissa 5 pvalue_exponent -45 multi_snp_haplotype false snp_interaction false range [0.07-0.094] beta 0.082 unit increase p_value 5e-45 accession_id GCST009856 pubmed_id 32109421 first_author Li C ci_lower 0.07 ci_upper 0.094

> [q739] _embedded.associations[129].efo_traits[0] efo_id OBA_0003784 efo_trait chromosome, telomeric region length

> [q740] _embedded.associations[129].snp_effect_allele[0] rs7705526-A

> [q741] _embedded.associations[42] association_id 219075503 risk_frequency 0.37 pvalue_description pvalue_mantissa 9 pvalue_exponent -96 multi_snp_haplotype false snp_interaction false range [1.27-1.34] or_per_copy_num 1.31 or_value 1.31 beta - p_value 8.999999999999999e-96 accession_id GCST90482692 pubmed_id 42152146 first_author Zhu M ci_lower 1.27 ci_upper 1.34

> [q742] _embedded.associations[42].reported_trait[0] Lung adenocarcinoma

> [q743] _embedded.associations[42].snp_effect_allele[0] rs7705526-A

> [q744] _embedded.associations[48] association_id 214160008 risk_frequency 0.326 pvalue_description pvalue_mantissa 3 pvalue_exponent -127 multi_snp_haplotype false snp_interaction false range [1.24-1.29] or_per_copy_num 1.27 or_value 1.27 beta - p_value 3e-127 accession_id GCST90435365 pubmed_id 39948438 first_author Wen S ci_lower 1.24 ci_upper 1.29

> [q745] _embedded.associations[48].reported_trait[0] Clonal hematopoiesis (overall)

> [q746] _embedded.associations[48].snp_effect_allele[0] rs7705526-A

> [q747] _embedded.associations[151] association_id 21699537 risk_frequency 0.332078 pvalue_description pvalue_mantissa 6 pvalue_exponent -19 multi_snp_haplotype false snp_interaction false range [1.28830538018993-1.48465482476452] or_per_copy_num 1.3829999 or_value 1.3829999 beta - p_value 6e-19 accession_id GCST004479 pubmed_id 28346442 first_author Phelan CM ci_lower 1.2883054 ci_upper 1.4846548

> [q748] _embedded.associations[151].reported_trait[0] Serous borderline ovarian cancer

> [q749] _embedded.associations[151].snp_effect_allele[0] rs7705526-A

rs7705526 (row 153), 155 associations. Li 2020's leukocyte telomere length, A 0.082 increase, P 5e-45 (q738 to q740;
trait OBA_0003784). Lung adenocarcinoma (Zhu): A OR 1.31, P 9e-96 (q741 to q743); clonal haematopoiesis (Wen): A OR
1.27, P 3e-127 (q744 to q746); serous borderline ovarian cancer (Phelan): A OR 1.38, P 6e-19 (q747 to q749).
The rest (lung cancer, melanoma, basal cell carcinoma, blood counts, other telomere lines; some PC-scale lines label
the allele C) named, not read. For row 153.

## Reading 2026-11-16, record

> [q750] _embedded.associations[10] association_id 55993996 risk_frequency 0.86 pvalue_description pvalue_mantissa 5 pvalue_exponent -19 multi_snp_haplotype false snp_interaction false range [0.05-0.078] beta 0.064 unit decrease p_value 5e-19 accession_id GCST009856 pubmed_id 32109421 first_author Li C ci_lower 0.05 ci_upper 0.078

> [q751] _embedded.associations[10].efo_traits[0] efo_id OBA_0003784 efo_trait chromosome, telomeric region length

> [q752] _embedded.associations[10].snp_effect_allele[0] rs9419958-C

> [q753] _embedded.associations[14] association_id 25285 risk_frequency 0.1353 pvalue_description pvalue_mantissa 9 pvalue_exponent -11 multi_snp_haplotype false snp_interaction false range [0.057-0.108] beta 0.0829 unit increase p_value 9e-11 accession_id GCST001697 pubmed_id 23001564 first_author Mangino M ci_lower 0.057 ci_upper 0.108

> [q754] _embedded.associations[14].snp_effect_allele[0] rs9419958-T

> [q755] _embedded.associations[7] association_id 131087097 risk_frequency NR pvalue_description pvalue_mantissa 4 pvalue_exponent -10 multi_snp_haplotype false snp_interaction false range - or_per_copy_num 0.938 or_value 0.938 beta - p_value 4e-10 accession_id GCST90328134 pubmed_id 38182794 first_author Choquet H

> [q756] _embedded.associations[7].reported_trait[0] Basal cell carcinoma

> [q757] _embedded.associations[7].snp_effect_allele[0] rs9419958-C

> [q758] _embedded.associations[11] association_id 51191091 risk_frequency 0.13 pvalue_description pvalue_mantissa 1 pvalue_exponent -16 multi_snp_haplotype false snp_interaction false range [1.08-1.13] or_per_copy_num 1.1 or_value 1.1 beta - p_value 1e-16 accession_id GCST009158 pubmed_id 31649266 first_author Gallagher CS ci_lower 1.08 ci_upper 1.13

> [q759] _embedded.associations[11].reported_trait[0] Uterine fibroids

> [q760] _embedded.associations[11].snp_effect_allele[0] rs9419958-T

rs9419958 (row 160), 15 associations. Li 2020's leukocyte telomere length, C 0.064 decrease, P 5e-19 (q750 to q752;
trait OBA_0003784); Mangino 2012's telomere length, T +0.083, P 9e-11 (q753, q754; its sample unread). Basal cell
carcinoma (Choquet): C OR 0.938, P 4e-10, so T raises it (q755 to q757); uterine fibroids (Gallagher): T OR 1.1, P
1e-16 (q758 to q760). Platelet counts, PSA and FLT3LG levels named, not read. For row 160.

## Reading 2026-11-16, record

> [q761] _embedded.associations[0] association_id 54151231 risk_frequency 0.16 pvalue_description pvalue_mantissa 4 pvalue_exponent -28 multi_snp_haplotype false snp_interaction false range NR beta 0.004 unit decrease p_value 4e-28 accession_id GCST009375 pubmed_id 28346444 first_author Wright DJ

> [q762] _embedded.associations[0].efo_traits[0] efo_id EFO_0007783 efo_trait mosaic loss of chromosome Y measurement

> [q763] _embedded.associations[0].snp_effect_allele[0] rs59633341-A

> [q764] page size 200 totalElements 1 totalPages 1 number 0

rs59633341 (row 145): one association (q764), Wright 2017's mosaic loss of chromosome Y, A 0.004 decrease, P 4e-28,
GCST009375 (q761, q763; trait EFO_0007783, q762). Thompson 2019's lines are not in the Catalog's record. For row 145.

## Reading 2026-11-16, record

> [q765] _embedded.associations[0] association_id 88923910 risk_frequency 0.8201 pvalue_description pvalue_mantissa 6 pvalue_exponent -69 multi_snp_haplotype false snp_interaction false range [2.88-3.61] beta 3.2457 unit decrease p_value 6e-69 accession_id GCST90014298 pubmed_id 34187551 first_author McCartney DL ci_lower 2.88 ci_upper 3.61

> [q766] _embedded.associations[0].efo_traits[0] efo_id EFO_0022597 efo_trait aging

> [q767] _embedded.associations[0].reported_trait[0] DNA methylation PhenoAge acceleration

> [q768] _embedded.associations[0].snp_effect_allele[0] rs73538174-A

> [q769] page size 200 totalElements 1 totalPages 1 number 0

rs73538174 (row 149): one association (q769), McCartney 2021's DNA methylation PhenoAge acceleration, A (0.82) 3.2457
decrease, P 6e-69 (q765, q767, q768); trait EFO_0022597 (q766). For row 149.

## Reading 2026-11-16, record

> [q770] _embedded.associations[0] association_id 88923156 risk_frequency 0.2193 pvalue_description pvalue_mantissa 9 pvalue_exponent -22 multi_snp_haplotype false snp_interaction false range [0.28-0.42] beta 0.3481 unit decrease p_value 9e-22 accession_id GCST90014289 pubmed_id 34187551 first_author McCartney DL ci_lower 0.28 ci_upper 0.42

> [q771] _embedded.associations[0].efo_traits[0] efo_id EFO_0022597 efo_trait aging

> [q772] _embedded.associations[0].reported_trait[0] DNA methylation Hannum age acceleration

> [q773] _embedded.associations[0].snp_effect_allele[0] rs941997-T

> [q774] page size 200 totalElements 1 totalPages 1 number 0

rs941997 (row 161): one association (q774), McCartney 2021's DNA methylation Hannum age acceleration, T (0.22) 0.3481
decrease, P 9e-22 (q770, q772, q773); trait EFO_0022597 (q771). For row 161.

## Reading 2026-11-16, record

> [q775] _embedded.associations[4] association_id 222822470 risk_frequency 0.634 pvalue_description pvalue_mantissa 9 pvalue_exponent -36 multi_snp_haplotype false snp_interaction false range [0.22-0.3] beta 0.26036677 years decrease p_value 8.999999999999999e-36 accession_id GCST90965684 pubmed_id 41044200 first_author Jawinski P ci_lower 0.22 ci_upper 0.3

> [q776] _embedded.associations[4].efo_traits[0] efo_id EFO_0010602 efo_trait brain age measurement

> [q777] _embedded.associations[4].snp_effect_allele[0] rs13132853-A

> [q778] _embedded.associations[7] association_id 192523638 risk_frequency 0.355838 pvalue_description pvalue_mantissa 1 pvalue_exponent -14 multi_snp_haplotype false snp_interaction false range [0.14-0.24] beta 0.189136 unit increase p_value 1e-14 accession_id GCST90558034 pubmed_id 40795387 first_author Zhao X ci_lower 0.14 ci_upper 0.24

> [q779] _embedded.associations[7].snp_effect_allele[0] rs13132853-G

> [q780] _embedded.associations[9] association_id 118806015 risk_frequency NR pvalue_description pvalue_mantissa 2 pvalue_exponent -18 multi_snp_haplotype false snp_interaction false range - beta 0.23 unit increase p_value 2e-18 accession_id GCST90296682 pubmed_id 37165155 first_author Leonardsen EH

> [q781] _embedded.associations[9].snp_effect_allele[0] rs13132853-G

> [q782] _embedded.associations[0] association_id 228231249 risk_frequency 0.7383 pvalue_description pvalue_mantissa 4 pvalue_exponent -13 multi_snp_haplotype false snp_interaction false range [0.023-0.039] beta 0.03095 unit increase p_value 4e-13 accession_id GCST90479522 pubmed_id 39024449 first_author Verma A ci_lower 0.023 ci_upper 0.039

> [q783] _embedded.associations[0].efo_traits[0] efo_id EFO_0004340 efo_trait body mass index

> [q784] _embedded.associations[0].snp_effect_allele[0] rs13132853-A

> [q785] _embedded.associations[21] association_id 91777845 risk_frequency 0.64 pvalue_description pvalue_mantissa 1 pvalue_exponent -8 multi_snp_haplotype false snp_interaction false range - beta 0.009 % increase p_value 1e-08 accession_id GCST90020232 pubmed_id 33980691 first_author Martin S

> [q786] _embedded.associations[21].snp_effect_allele[0] rs13132853-A

> [q787] _embedded.associations[23] association_id 30568407 risk_frequency 0.6352 pvalue_description pvalue_mantissa 9 pvalue_exponent -9 multi_snp_haplotype false snp_interaction false range [0.0014-0.0026] beta 0.002 unit decrease p_value 9.000000000000001e-09 accession_id GCST005830 pubmed_id 29691431 first_author Tikkanen E ci_lower 0.0014 ci_upper 0.0026

> [q788] _embedded.associations[23].snp_effect_allele[0] rs13132853-A

> [q789] page size 200 totalElements 24 totalPages 1 number 0

rs13132853 (row 115), 24 associations (q789). Jawinski 2025's brain age gap (grey and white matter), A (0.634) 0.260
years decrease, P 9e-36 (q775, q777; trait EFO_0010602, q776). Two other brain-age GWASs put G on the older side:
Zhao's (PMID 40795387), G +0.189, P 1e-14 (q778, q779); Leonardsen's (PMID 37165155), G +0.23, P 2e-18 (q780,
q781); both papers unread, their samples' overlap with Jawinski's UK Biobank unread. A raises body mass index (+0.031,
P 4e-13; q782 to q784) and body fat percentage (P 1e-8; q785, q786) and lowers hand grip strength (P 9e-9;
q787, q788). Brain imaging, blood count and liver enzyme lines named, not read. For row 115.
