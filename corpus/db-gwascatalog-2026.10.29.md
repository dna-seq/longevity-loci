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
