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

## Reading 2026-11-11, record

> [q18] [0] r2 0.533397 variation1 rs10798302 d_prime 0.987948 population_name 1000GENOMES:phase_3:EUR variation2 rs16847402

`ld-rs10798302-rs16847402.json`: r² 0.53, D′ 0.99 in 1000 Genomes EUR. For row 10.

> [q19] mappings[0] start 174018660 location 1:174018660-174018660 allele_string A/G/T coord_system chromosome end 174018660 ancestral_allele G assembly_name GRCh38 seq_region_name 1 strand 1

> [q20] populations[76] population 1000GENOMES:phase_3:EUR frequency 0.181908548707753 allele_count 183 allele G

> [q21] mappings[0] seq_region_name 1 allele_string T/C end 174745913 location 1:174745913-174745913 ancestral_allele T assembly_name GRCh38 coord_system chromosome start 174745913 strand 1

> [q22] populations[76] allele C frequency 0.108349900596421 population 1000GENOMES:phase_3:EUR allele_count 109

> [q23] most_severe_consequence intron_variant

rs10798302 at GRCh38 1:174,018,660, A/G (a rare T besides), intronic; G 0.18 in EUR. rs16847402 at 1:174,745,913,
T/C on the forward strand; C 0.11 in EUR. For row 10.

## Reading 2026-11-11, record

> [q24] populations[78] allele A allele_count 172 population 1000GENOMES:phase_3:EUR frequency 0.170974155069582

> [q25] mappings[0] seq_region_name 2 assembly_name GRCh38 ancestral_allele A end 628524 strand 1 start 628524 location 2:628524-628524 allele_string A/G/T coord_system chromosome

rs6744653 (`variation-rs6744653.json`): GRCh38 2:628,524, A/G (A the reference and ancestral); A 0.171 in 1000
Genomes Europeans. Intergenic. For row 11.

> [q26] populations[76] frequency 0.179920477137177 population 1000GENOMES:phase_3:EUR allele T allele_count 181

> [q27] mappings[0] end 630070 location 2:630070-630070 allele_string T/A/C/G strand 1 coord_system chromosome start 630070 seq_region_name 2 assembly_name GRCh38 ancestral_allele T

rs66906321: GRCh38 2:630,070, T/C in Europeans (T the reference), T 0.180. For row 11.

> [q28] [0] variation2 rs66906321 r2 0.886777 variation1 rs6744653 population_name 1000GENOMES:phase_3:EUR d_prime 0.971266

> [q29] [0] population_name 1000GENOMES:phase_3:EUR variation2 rs2867105 variation1 rs6744653 r2 0.857788 d_prime 0.935895

> [q30] [0] r2 0.765845 variation2 rs2867105 variation1 rs66906321 d_prime 0.893232 population_name 1000GENOMES:phase_3:EUR

Pairwise LD, 1000 Genomes EUR: rs6744653–rs66906321 r² 0.89 (D′ 0.97); rs6744653–rs2867105 r² 0.86 (D′ 0.94);
rs66906321–rs2867105 r² 0.77 (D′ 0.89). For row 11.

> [q31] populations[77] allele T population 1000GENOMES:phase_3:EUR frequency 0.173956262425447 allele_count 175

> [q32] mappings[0] allele_string T/A/G ancestral_allele G strand 1 assembly_name GRCh38 coord_system chromosome end 601905 start 601905 seq_region_name 2 location 2:601905-601905

rs2867105: GRCh38 2:601,905 (the same as GRCh37 here), T/G in Europeans, T 0.174. For row 11.

> [q33] populations[77] allele T population 1000GENOMES:phase_3:EUR frequency 0.190854870775348 allele_count 192

> [q34] mappings[0] location 2:619653-619653 end 619653 ancestral_allele C start 619653 seq_region_name 2 strand 1 allele_string C/G/T assembly_name GRCh38 coord_system chromosome

rs10153797: GRCh38 2:619,653, C/T, T 0.191. Its LD with rs6744653 (`ld-rs6744653-rs10153797.json`) came back empty.
For row 11.

> [q35] [0] variation1 rs6744653 variation2 rs4640417 r2 0.113930 d_prime 0.999965 population_name 1000GENOMES:phase_3:EUR

rs6744653–rs4640417: r² 0.11 (D′ 1.00). For row 11.

> [q36] populations[77] allele_count 648 allele A population 1000GENOMES:phase_3:EUR frequency 0.644135188866799

rs4640417 (`variation-rs4640417.json`): GRCh38 2:648,527, A/G in Europeans, A 0.64, G 0.36. For row 11.

> [q37] [0] d_prime 0.999990 r2 0.462307 population_name 1000GENOMES:phase_3:EUR variation2 rs4845625 variation1 rs2228145

rs2228145 and rs4845625 (Timmers 2019's suggestive IL6R SNP): r² 0.46, D′ 1.00 in EUR. For row 8.

> [q38] [0] r2 0.094331 d_prime 0.317303 variation2 rs17561720 variation1 rs3768321 population_name 1000GENOMES:phase_3:CEU

> [q39] populations[76] frequency 0.192842942345924 population 1000GENOMES:phase_3:EUR allele T allele_count 194

> [q40] mappings[0] end 39705554 coord_system chromosome start 39705554 seq_region_name 1 location 1:39705554-39705554 allele_string C/A/T ancestral_allele C strand 1 assembly_name GRCh38

rs3768321 and rs17561720: Ensembl's 1000 Genomes EUR pair returned nothing (unknown), and its CEU pair, a subset of
EUR (Utah residents of northern and western European ancestry), gives r² 0.09, D′ 0.32. rs17561720 (1:39,705,554 in
GRCh38, C/A/T; T 0.19 in EUR) is not a proxy of rs3768321 in the panel that answers. For row 2.

> [q41] description RAB GTPase activating protein 1 like [Source:HGNC Symbol;Acc:HGNC:24663] end 174995308 seq_region_name 1 species homo_sapiens assembly_name GRCh38 display_name RABGAP1L

ENSG00000152061, the gene whose expression sets hold rs10798302 in Open Targets (db-opentargets-26.09#q86), is
RABGAP1L (1:174,159,339-174,995,308, GRCh38, protein coding). For row 10.

## rs1275922 (KCNK3), for row 12

> [q42] [0] variation1 rs1275922 r2 0.989960 variation2 rs11126666 d_prime 0.994968 population_name 1000GENOMES:phase_3:EUR

rs1275922 and rs11126666 (Pilling 2017's and Timmers' Figure 4 SNP) are one signal in 1000 Genomes EUR: r² 0.99.

> [q43] [0] d_prime 0.300056 population_name 1000GENOMES:phase_3:CEU variation1 rs1275922 variation2 rs2891519 r2 0.061131

rs2891519 (Wright 2019's AncestryDNA mothers' SNP, 22 kb away) is not a tag: CEU r² 0.06, D′ 0.30. The EUR pairwise
call is empty, with the r² floor off too.

> [q44] populations[76] population 1000GENOMES:phase_3:EUR allele_count 273 allele A frequency 0.271371769383698

> [q45] populations[83] allele_count 221 frequency 0.219681908548708 population 1000GENOMES:phase_3:EUR allele A

1000 Genomes EUR: rs1275922 A 0.27; rs2891519 A 0.22.

> [q46] [1] variation1 rs1275922 r2 0.969972 variation2 rs1731248 d_prime 0.984872 population_name 1000GENOMES:phase_3:EUR

Ensembl's LD window around rs1275922 (`ld-window50-rs1275922.json`, 1000 Genomes EUR, r² >= 0.1): rs1731248 at r²
0.97, D′ 0.98.

## rs577106756 (PRKD3), for row 13

> [q47] mappings[0] end 37257437 allele_string G/A seq_region_name 2 start 37257437 strand 1 location 2:37257437-37257437 assembly_name GRCh38 ancestral_allele G coord_system chromosome

rs577106756 at 2:37,257,437 (GRCh38), G/A, G ancestral; an intron variant.

> [q48] populations[56] allele A allele_count 2 frequency 0.00198807157057654 population 1000GENOMES:phase_3:EUR

> [q49] populations[11] frequency 0.001752 population gnomADg:nfe allele A allele_count 119

> [q50] populations[13] frequency 0.001703 population gnomADg:fin allele A allele_count 18

A is rare: 2 copies in 1000 Genomes EUR (0.002), 0.18 % in gnomAD's non-Finnish Europeans, 0.17 % in its Finns.
The LD window call (`ld-window50-rs577106756.json`, EUR, r² ≥ 0.1) rendered no text: with two copies in the panel
no tag is known, and that is unknown, not an absence of tags.

## rs980183 (LINC01122), for row 14

> [q51] mappings[0] assembly_name GRCh38 coord_system chromosome allele_string G/A/C strand 1 start 59084401 seq_region_name 2 ancestral_allele A end 59084401 location 2:59084401-59084401

rs980183 at 2:59,084,401 (GRCh38; 2:59,311,536 in GRCh37), G/A, A ancestral; an intron variant (of the LINC01122
transcript).

> [q52] populations[76] allele_count 619 frequency 0.615308151093439 population 1000GENOMES:phase_3:EUR allele A

> [q53] populations[77] population 1000GENOMES:phase_3:EUR frequency 0.384691848906561 allele_count 387 allele G

1000 Genomes EUR: A 0.62, G 0.38.

> [q54] [38] variation1 rs980183 variation2 rs6545714 r2 0.970730 d_prime 0.991491 population_name 1000GENOMES:phase_3:EUR

Ensembl's LD window (`ld-window500-rs980183.json`, EUR, r² ≥ 0.1): rs6545714, the lead of Open Targets' BMI set
(db-opentargets-26.09#q125), at r² 0.97, D′ 0.99.

> [q55] populations[79] allele A allele_count 622 frequency 0.618290258449304 population 1000GENOMES:phase_3:EUR

rs6545714's A is 0.62 in 1000 Genomes EUR, as rs980183's A is (q52): at r² 0.97 the two As travel together (derived
from the frequencies, not a phased call). Wright 2019's four AncestryDNA mothers' SNPs within 0.5 Mb (rs7593324,
rs10210385, rs1796435, rs13416859) are absent from the window and their pairwise calls render no text in EUR or CEU,
with the r² floor off: unknown, not read.

## rs78438918 (AFF3), for row 15

> [q56] mappings[0] seq_region_name 2 ancestral_allele A end 100013653 assembly_name GRCh38 strand 1 location 2:100013653-100013653 start 100013653 coord_system chromosome allele_string A/G

rs78438918 at 2:100,013,653 (GRCh38; 2:100,630,115 in GRCh37), A/G, A ancestral; an intron variant of AFF3.

> [q57] populations[76] allele G allele_count 167 population 1000GENOMES:phase_3:EUR frequency 0.166003976143141

1000 Genomes EUR: G 0.166, A 0.834. G/G about 3 in 100, A/G about 28, A/A about 70 (Hardy-Weinberg).

> [q58] [173] r2 0.756567 variation1 rs78438918 population_name 1000GENOMES:phase_3:EUR d_prime 0.882269 variation2 rs13032879

> [q59] [107] variation1 rs78438918 r2 0.730283 variation2 rs4851244 d_prime 0.909249 population_name 1000GENOMES:phase_3:EUR

Ensembl's LD window (`ld-window500-rs78438918.json`, EUR, r² ≥ 0.1): Wright 2019's fathers' SNPs rs13032879 (r²
0.76, D′ 0.88) and rs4851244 (r² 0.73, D′ 0.91).

> [q60] populations[76] frequency 0.169980119284294 population 1000GENOMES:phase_3:EUR allele T allele_count 171

> [q61] populations[76] allele_count 185 population 1000GENOMES:phase_3:EUR frequency 0.18389662027833 allele C

EUR: rs13032879 T 0.17, rs4851244 C 0.18, each the minor allele, as the lead's G (0.17) is. An r² above 0.7 between
two SNPs with minor alleles near 0.17 is only reachable with minor on minor, so each minor travels with G (derived
from the frequencies, not a phased call).

> [q62] . version 22 db_type core biotype protein_coding seq_region_name 2 start 99545419 end 100192469 assembly_name GRCh38 id ENSG00000144218 display_name AFF3 description ALF transcription elongation factor 3 [Source:HGNC Symbol;Acc:HGNC:6473] logic_name ensembl_havana_gene_homo_sapiens strand -1 canonical_transcript ENST00000672756.2 source ensembl_havana object_type Gene species homo_sapiens

ENSG00000144218 is AFF3, a protein-coding gene: the gene the eQTL sets of db-opentargets-26.09#q141 measure.

## rs117898573 (LRP1B), for row 16

> [q63] mappings[0] start 142119915 end 142119915 coord_system chromosome location 2:142119915-142119915 seq_region_name 2 strand 1 ancestral_allele C allele_string C/T assembly_name GRCh38

rs117898573 at 2:142,119,915 (GRCh38), C/T, ancestral C.

> [q64] populations[50] allele T population 1000GENOMES:phase_3:EAS frequency 0.0248015873015873 allele_count 25

> [q65] populations[45] frequency 0.0388349514563107 population 1000GENOMES:phase_3:CHB allele T allele_count 8

> [q66] populations[3] allele_count 96 frequency 0.0186 population gnomADg:eas allele T

East Asian frequencies of T: 1000 Genomes EAS 0.025 (CHB 0.039), gnomAD East Asian 0.019; Chang 2022's own 0.029.

> [q67] populations[53] population 1000GENOMES:phase_3:EUR allele C frequency 1 allele_count 1006

> [q68] populations[13] frequency 2.941e-05 allele T population gnomADg:nfe allele_count 2

Europeans: C in all 1,006 1000 Genomes EUR chromosomes, T 2.9 × 10⁻⁵ in gnomAD non-Finnish Europeans (2 alleles).
The variant is absent from European lifespan, healthspan and longevity data, so it is untested there, not null.

## rs10197246 (CASP8 / FLACC1), for row 17

> [q69] mappings[0] location 2:201340018-201340018 ancestral_allele C assembly_name GRCh38 start 201340018 strand 1 end 201340018 seq_region_name 2 allele_string T/A/C/G coord_system chromosome

rs10197246 at 2:201,340,018 (GRCh38; GRCh37 202,204,741), T/A/C/G as dbSNP lists it, an intron variant; the alleles
in the papers are C and T.

> [q70] populations[77] population 1000GENOMES:phase_3:EUR frequency 0.290258449304175 allele T allele_count 292

> [q71] populations[20] population gnomADg:nfe allele C allele_count 48964 frequency 0.7207

European frequencies: T 0.29 in 1000 Genomes EUR; C 0.72 in gnomAD non-Finnish Europeans (Zenin's 0.734). By
Hardy-Weinberg about 52 in 100 Europeans are C/C, 40 C/T and 8 T/T.

> [q72] populations[77] allele_count 73 frequency 0.0725646123260437 population 1000GENOMES:phase_3:EUR allele C

> [q73] populations[74] allele C population 1000GENOMES:phase_3:EUR frequency 0.0546719681908549 allele_count 55

> [q74] mappings[0] assembly_name GRCh38 allele_string T/A/C seq_region_name 2 end 201458233 coord_system chromosome strand 1 location 2:201458233-201458233 ancestral_allele T start 201458233

Wright 2019's two nearby S8 SNPs (pmid-31484785#q47, q48): rs3754935's C is 0.073 in 1000 Genomes EUR; rs1009276's C
(T/A/C on the forward strand, so Wright's G is the other strand's C) is 0.055. Between a 0.05 to 0.07 allele and the
lead's 0.29 the largest possible r² is p₁(1 − p₂) / (p₂(1 − p₁)), about 0.19 and 0.14: neither is a tag.

> [q75] . source Variants (including SNPs and indels) imported from dbSNP name rs1043943 ambiguity H var_class SNP most_severe_consequence 3_prime_UTR_variant minor_allele T MAF 0.310832

> [q76] populations[96] allele_count 403 allele T population 1000GENOMES:phase_3:EUR frequency 0.400596421471173

> [q77] populations[93] allele T allele_count 327 population 1000GENOMES:phase_3:EAS frequency 0.324404761904762

> [q78] populations[26] frequency 0.4027 population gnomADg:nfe allele_count 27378 allele T

> [q79] populations[21] allele T allele_count 1843 population gnomADg:eas frequency 0.357

> [q80] mappings[0] coord_system chromosome allele_string T/A/C location 3:14141910-14141910 start 14141910 strand 1 seq_region_name 3 end 14141910 ancestral_allele C assembly_name GRCh38

rs1043943 (row 18): a 3' UTR variant (of TMEM43), GRCh38 3:14,141,910, reference T (allele string T/A/C), ancestral C.
T is 0.40 in 1000 Genomes EUR and gnomAD non-Finnish Europeans, 0.32 in 1000 Genomes EAS and 0.36 in gnomAD East
Asians: common in both ancestries. By Hardy-Weinberg about 36 in 100 Europeans are C/C, 48 C/T and 16 T/T (EAS 46, 44,
10). Open Targets' variant id is therefore 3_14141910_T_C, and its betas are per C.

> [q81] [0] d_prime 0.999999 population_name 1000GENOMES:phase_3:CEU variation2 rs2228001 r2 0.938886 variation1 rs1043943

> [q82] [0] variation1 rs1043943 variation2 rs2228001 r2 0.939824 population_name 1000GENOMES:phase_3:CHB d_prime 0.999999

LD between rs1043943 and rs2228001 (XPC's missense variant, pmid-33657282#q7): r² 0.94, D' 1.0 in both 1000 Genomes CEU
and CHB. The lead tags XPC's missense variant as well in Europeans as in Chinese. For row 18.

> [q83] . source Variants (including SNPs and indels) imported from dbSNP ambiguity R var_class SNP MAF 0.206436 minor_allele A name rs78043944 most_severe_consequence intergenic_variant

> [q84] mappings[0] end 26327009 location 3:26327009-26327009 ancestral_allele null seq_region_name 3 start 26327009 strand 1 allele_string G/A coord_system chromosome assembly_name GRCh38

> [q85] populations[74] allele A population 1000GENOMES:phase_3:EUR allele_count 141 frequency 0.140159045725646

> [q86] populations[8] allele_count 343 frequency 0.00688 population gnomADg:nfe allele A

> [q87] populations[2] allele A population gnomADg:asj frequency 0.001702 allele_count 4

rs78043944 (row 19): intergenic, GRCh38 3:26,327,009, G/A. The frequencies of A disagree by twentyfold: 0.14 in 1000
Genomes EUR (CEU 0.18), 0.0069 in gnomAD non-Finnish Europeans and 0.0017 in gnomAD Ashkenazi Jews. NECS controls
(0.0065, pmid-33948810#q4) and Zenin's UK Biobank (0.0054) agree with gnomAD, so 1000 Genomes' call at this site is the
likely outlier; by gnomAD about 98.6 in 100 Europeans are G/G, 1.4 G/A, and A/A about 5 in 100,000. Open Targets'
id is 3_26327009_G_A. For row 19.

> [q88] populations[13] frequency 0.2643 allele_count 7865 population gnomADg:afr allele A

> [q89] populations[49] allele A allele_count 482 frequency 0.364599092284418 population 1000GENOMES:phase_3:AFR

A is common in Africans (gnomAD 0.26, 1000 Genomes AFR 0.36) and rare in Europeans (q86), so a small difference in
African ancestry between cases and controls would shift its frequency on its own. For row 19.

## rs2643826 (SLC4A7), for row 20

> [q90] . var_class SNP most_severe_consequence regulatory_region_variant name rs2643826 source Variants (including SNPs and indels) imported from dbSNP ambiguity Y minor_allele C MAF 0.463697

> [q91] mappings[0] allele_string C/T coord_system chromosome seq_region_name 3 assembly_name GRCh38 location 3:27521497-27521497 ancestral_allele T end 27521497 start 27521497 strand 1

> [q92] populations[2] frequency 0.555 allele C allele_count 37701 population gnomADg:nfe

> [q93] populations[75] population 1000GENOMES:phase_3:EUR allele C allele_count 551 frequency 0.547713717693837

> [q94] populations[73] allele C allele_count 688 frequency 0.682539682539683 population 1000GENOMES:phase_3:EAS

> [q95] populations[52] population 1000GENOMES:phase_3:AFR frequency 0.0264750378214826 allele C allele_count 35

rs2643826: a regulatory-region variant, GRCh38 3:27,521,497, C/T, T ancestral. C is the major allele in Europeans
(gnomAD non-Finnish 0.555, 1000 Genomes EUR 0.548) and East Asians (0.68), rare in Africans (0.026). By gnomAD's
European frequency about 31 in 100 Europeans are C/C, 49 C/T and 20 T/T. Open Targets' id is 3_27521497_C_T.

## rs9872864 and rs2271961 (IP6K1), for row 21

> [q96] . MAF 0.425432 source Variants (including SNPs and indels) imported from dbSNP minor_allele A name rs9872864 var_class SNP most_severe_consequence intron_variant ambiguity N

> [q97] mappings[0] location 3:49754590-49754590 seq_region_name 3 assembly_name GRCh38 start 49754590 end 49754590 ancestral_allele A strand 1 allele_string A/C/G/T coord_system chromosome

> [q98] populations[11] allele_count 34773 frequency 0.5117 allele G population gnomADg:nfe

> [q99] populations[77] population 1000GENOMES:phase_3:EAS frequency 0.160714285714286 allele_count 162 allele A

rs9872864: an intron variant, GRCh38 3:49,754,590, reference A, alternative G (Open Targets' 3_49754590_A_G). G is
0.512 in gnomAD's non-Finnish Europeans, A 0.488: G is the major allele by a hair. In East Asians A is 0.16 (1000
Genomes). By gnomAD's European frequency about 26 in 100 Europeans are G/G, 50 A/G and 24 A/A.

> [q105] populations[8] population gnomADg:afr allele A frequency 0.6264 allele_count 25914

A is the major allele in Africans (gnomAD 0.63).

> [q100] [0] variation1 rs9872864 r2 0.988107 variation2 rs2271961 d_prime 1.000000 population_name 1000GENOMES:phase_3:EUR

rs9872864 and rs2271961 are 86 kb apart and almost the same SNP in Europeans: r² 0.99, D′ 1.00 in 1000 Genomes
EUR. Which alleles travel together is derived from East Asian frequencies, where they are not near one half:
rs9872864's A is 0.161 there and rs2271961's C 0.166 (q99, q104), so A rides with C and G with T. Timmers' signs
agree (pmid-30642433#q59, q60).

> [q101] . minor_allele C most_severe_consequence intron_variant var_class SNP name rs2271961 source Variants (including SNPs and indels) imported from dbSNP ambiguity H MAF 0.417582

> [q102] mappings[0] strand 1 seq_region_name 3 end 49840680 ancestral_allele C assembly_name GRCh38 allele_string T/A/C coord_system chromosome start 49840680 location 3:49840680-49840680

> [q103] populations[33] allele T allele_count 34936 frequency 0.5138 population gnomADg:nfe

> [q104] populations[92] frequency 0.165674603174603 population 1000GENOMES:phase_3:EAS allele_count 167 allele C

rs2271961: an intron variant, GRCh38 3:49,840,680, reference T, alternative C (3_49840680_T_C). T is 0.514 in
gnomAD's non-Finnish Europeans; C is 0.166 in East Asians.

> [q106] [0] d_prime 1.000000 variation1 rs9872864 variation2 rs9855505 r2 1.000000 population_name 1000GENOMES:phase_3:EUR

> [q107] [0] population_name 1000GENOMES:phase_3:EUR d_prime 1.000000 variation2 rs12490656 r2 0.996021 variation1 rs9872864

rs9855505 (135 bp from the lead) is in perfect LD with rs9872864 in 1000 Genomes EUR (r² 1.00, D′ 1.00), and rs12490656
nearly (r² 0.996). Fetched to read Timmers' direction strings across the block (pmid-30642433#q61, q62). For row 21.

> [q108] [13] variation2 rs7560328 d_prime 0.937399 population_name 1000GENOMES:phase_3:EUR variation1 rs10197246 r2 0.572388

rs7560328, 40 kb from the CASP8 lead rs10197246, is r² 0.57, D′ 0.94 with it in 1000 Genomes EUR (the 500 kb window
already cached for row 17). For row 17's Deelen cluster (pmid-31413261#q46).

> [q109] [25] population_name 1000GENOMES:phase_3:EUR variation2 rs2607770 variation1 rs1043943 d_prime 1.000000 r2 1.000000

rs2607770 is in perfect LD with the TMEM43 lead rs1043943 in 1000 Genomes EUR (r² 1.0), one of 22 variants at r² ≥ 0.8
in the cached 500 kb window. For row 18's proxies in Timmers 2019 (pmid-30642433#q63, q64).

> [q110] populations[10] population gnomADg:nfe allele A allele_count 30664 frequency 0.4516

> [q111] populations[77] population 1000GENOMES:phase_3:EUR frequency 0.465208747514911 allele A allele_count 468

> [q112] [0] d_prime 0.971454 population_name 1000GENOMES:phase_3:EUR r2 0.925069 variation1 rs472103 variation2 rs247975

> [q113] [0] variation2 rs583514 r2 0.861476 variation1 rs472103 d_prime 0.991204 population_name 1000GENOMES:phase_3:EUR

> [q114] [0] variation1 rs472103 variation2 rs529200 r2 0.941602 d_prime 0.995852 population_name 1000GENOMES:phase_3:EUR

> [q115] populations[82] allele A allele_count 481 population 1000GENOMES:phase_3:EUR frequency 0.478131212723658

> [q116] mappings[0] seq_region_name 3 allele_string A/C/T coord_system chromosome assembly_name GRCh38 ancestral_allele C location 3:173404702-173404702 end 173404702 strand 1 start 173404702

> [q117] mappings[0] location 3:173389653-173389653 strand 1 coord_system chromosome assembly_name GRCh38 ancestral_allele C end 173389653 seq_region_name 3 allele_string T/C start 173389653

rs472103 (GRCh38 3:173,404,702; A/C/T, the reference A): A is 0.452 in gnomAD's non-Finnish Europeans and 0.465 in
1000 Genomes EUR, the minor allele, near even. Its proxies in 1000 Genomes EUR: rs247975 r² 0.93 (T/C on the forward
strand), rs583514 r² 0.86, rs529200 r² 0.94. rs529200's A is 0.478 in EUR; at frequencies 0.465 and 0.478 only A
with A fits r² 0.94 (A with G would cap r² near 0.80): rs529200-A rides with rs472103-A (derived). For row 24.

## Reading 2026-11-11, record

Linkage disequilibrium at 4p16.3, 1000 Genomes phase 3 (Ensembl REST, pairwise), for row 25.

> [q118] [0] d_prime 0.999996 population_name 1000GENOMES:phase_3:EUR r2 0.703834 variation2 rs16843836 variation1 rs61348208

> [q119] [0] d_prime 0.940373 variation1 rs61348208 variation2 rs82334 population_name 1000GENOMES:phase_3:EUR r2 0.663797

> [q120] [0] r2 0.095064 variation1 rs61348208 d_prime 0.370961 population_name 1000GENOMES:phase_3:EUR variation2 rs16843603

> [q121] [0] d_prime 0.965057 variation2 rs114298671 variation1 rs61348208 r2 0.082481 population_name 1000GENOMES:phase_3:EUR

> [q122] [0] d_prime 0.956065 r2 0.673733 variation2 rs362273 variation1 rs61348208 population_name 1000GENOMES:phase_3:EUR

> [q123] [0] d_prime 0.964900 population_name 1000GENOMES:phase_3:EAS variation2 rs362273 r2 0.760777 variation1 rs61348208

> [q124] [0] r2 0.981925 variation2 rs362273 variation1 rs82334 population_name 1000GENOMES:phase_3:EUR d_prime 1.000000

> [q125] [0] r2 0.910684 d_prime 0.985517 variation2 rs82334 variation1 rs16843836 population_name 1000GENOMES:phase_3:EUR

> [q126] [0] variation1 rs61348208 r2 0.425847 variation2 rs363096 population_name 1000GENOMES:phase_3:EUR d_prime 0.984722

> [q127] [0] d_prime 0.999986 population_name 1000GENOMES:phase_3:EUR variation1 rs61348208 r2 0.321684 variation2 rs11731237

rs61348208 to: rs16843836 r² 0.70 and rs82334 r² 0.66 (D′ 1.00, 0.94), the same signal by the shadow test
(pmid-30642433#q68, q69); rs16843603 (ADD1) r² 0.095 and rs114298671 (MSANTD1) r² 0.08, separate. Timmers 2022's
aging-GIP1 lead rs362273: r² 0.67 to rs61348208 in EUR and 0.76 in EAS, 0.98 to rs82334. rs16843836 to rs82334 r²
0.91. Wright 2019's clumped AncestryDNA SNPs in the window (fathers born 1886-1940, Supplemental Table 8; no mothers'
SNP there) are no tag: the nearest, rs363096 (r² 0.43) and rs11731237 (0.32), the rest under 0.19 (cached as
ld-rs61348208-<rsid>), so AncestryDNA is not read at the lead.

> [q128] [0] variation2 rs2285086 r2 0.834542 variation1 rs61348208 d_prime 1.000000 population_name 1000GENOMES:phase_3:EUR

rs2285086, 305 bp from the lead (Timmers 2019's Figure 4 look-up SNP, pmid-30642433#q72), r² 0.83, D′ 1.

The phase of each partner with the lead's T (0.39, pmid-30642433#q66), from frequency and r² alone. For alleles at
frequencies p and q, the r² ceiling is D_max² / (p(1−p)q(1−q)), with D_max = min(p(1−q), (1−p)q) when the two ride
together and min(pq, (1−p)(1−q)) when they are opposed. rs82334's C at 0.32 (pmid-34431594#q4): with T, ceiling 0.73;
against T, 0.30; observed 0.66 (q119), so C rides with T. rs362273's G at 0.32 (pmid-37118362#q8, the meta-analysis
frequency): the same ceilings, observed 0.67 (q122), so G rides with T. rs16843836's A at 0.31 (pmid-37550455#q21):
with T 0.70, against T 0.29, observed 0.70 (q118), so A with T. rs2285086's G at 0.427 (pmid-30642433#q72): with T
0.86, against T 0.48, observed 0.83, so G with T. Derived in Europeans; no East Asian frequency of the lead is cached,
so the East Asian phase is assumed the same, not shown. For row 25.

## Reading 2026-11-11, record

rs7676745 (GPR78), for row 26: its frequencies (variation-rs7676745) and its linkage disequilibrium with the two
rare neighbours in Deelen's and Timmers' summary statistics (ld-rs7676745-<rsid>), 1000 Genomes phase 3 EUR.

> [q129] [0] population_name 1000GENOMES:phase_3:EUR d_prime 0.679539 r2 0.450810 variation2 rs10022617 variation1 rs7676745

> [q130] [0] d_prime 0.715629 population_name 1000GENOMES:phase_3:EUR variation1 rs7676745 variation2 rs10009267 r2 0.475724

rs10022617 (r² 0.45, D′ 0.68) and rs10009267 (r² 0.48, D′ 0.72): weak tags of the lead, neither a proxy at r² 0.8.

> [q131] populations[64] allele_count 1008 allele G frequency 1 population 1000GENOMES:phase_3:EAS

> [q132] populations[67] allele A allele_count 44 population 1000GENOMES:phase_3:EUR frequency 0.0437375745526839

> [q133] mappings[0] assembly_name GRCh38 ancestral_allele G end 8563820 seq_region_name 4 strand 1 start 8563820 location 4:8563820-8563820 allele_string G/A coord_system chromosome

rs7676745 is 4:8,563,820 (GRCh38), G/A, G ancestral. A is 0.044 in 1000 Genomes Europeans (gnomAD non-Finnish
Europeans 0.046) and absent in East Asians (G 1, 1,008 chromosomes). Under Hardy-Weinberg in Europeans, G/G about 91
in 100, A/G about 8, A/A about 0.2. Phase of the neighbours, by frequency and r² ceilings (never by direction): with
the lead's A at 0.044 and rs10009267's C at 0.037 (pmid-30642433#q75), the coupled phase allows r² up to 0.83 and the
opposite phase at most 0.002, so the observed 0.48 puts C with A; rs10022617's G at 0.036 (q74 there) likewise
(0.83 against 0.002, observed 0.45), G with A. For row 26.

## Reading 2026-11-11, record

> [q134] populations[76] frequency 0.544731610337972 population 1000GENOMES:phase_3:EUR allele A allele_count 548

> [q135] populations[77] allele_count 458 allele G population 1000GENOMES:phase_3:EUR frequency 0.455268389662028

> [q136] populations[72] frequency 0.420634920634921 population 1000GENOMES:phase_3:EAS allele A allele_count 424

> [q137] mappings[0] start 38383858 strand 1 coord_system chromosome allele_string G/A/C location 4:38383858-38383858 end 38383858 ancestral_allele G assembly_name GRCh38 seq_region_name 4

> [q138] [0] r2 0.996000 variation1 rs17499404 d_prime 1.000000 population_name 1000GENOMES:phase_3:EUR variation2 rs2291435

> [q139] [0] population_name 1000GENOMES:phase_3:EUR variation2 rs13104866 variation1 rs17499404 r2 0.795930 d_prime 0.926672

> [q140] [0] r2 0.996000 variation2 rs2291433 variation1 rs17499404 d_prime 1.000000 population_name 1000GENOMES:phase_3:EUR

> [q141] populations[83] allele_count 459 allele T frequency 0.456262425447316 population 1000GENOMES:phase_3:EUR

> [q142] populations[84] allele_count 547 allele G frequency 0.543737574552684 population 1000GENOMES:phase_3:EUR

rs17499404 (LINC02513), for row 27: 4:38,383,858 (GRCh38), G/A, G ancestral. A is 0.545 in 1000 Genomes Europeans
(gnomAD non-Finnish 0.537, Finnish 0.41) and 0.42 in East Asians, so the variant is common everywhere. Under
Hardy-Weinberg in Europeans: A/A about 30 in 100, A/G about 50, G/G about 21. Linkage disequilibrium (EUR):
rs2291435 (Ehret 2016's blood-pressure SNP) r² 0.996; rs2291433 (the frailty set's lead, Wright's S9 SNP) r² 0.996;
rs13104866 (Hoffmann 2016's) r² 0.80. Phase of rs2291433, by frequency and r² ceilings: its G (0.544) against the
lead's A (0.545) allows r² up to about 1.0 coupled and 0.70 opposed, so the observed 0.996 puts G with A.

## Reading 2026-11-11, record

> [q143] [0] variation1 rs17499404 r2 0.398779 variation2 rs12646716 population_name 1000GENOMES:phase_3:EUR d_prime 0.770012

> [q144] [0] d_prime 0.625255 population_name 1000GENOMES:phase_3:EUR r2 0.317768 variation1 rs17499404 variation2 rs1487624

> [q145] [0] variation2 rs11732737 variation1 rs17499404 d_prime 0.594207 r2 0.285854 population_name 1000GENOMES:phase_3:EUR

> [q146] [0] variation2 rs7668402 population_name 1000GENOMES:phase_3:EUR d_prime 0.845158 variation1 rs17499404 r2 0.331253

> [q147] [0] variation1 rs17499404 r2 0.996000 variation2 rs6812640 d_prime 1.000000 population_name 1000GENOMES:phase_3:EUR

> [q148] populations[56] frequency 0.456262425447316 allele C population 1000GENOMES:phase_3:EUR allele_count 459

> [q149] populations[57] allele_count 547 population 1000GENOMES:phase_3:EUR allele G frequency 0.543737574552684

Row 27, second pass. Wright 2019's S9 SNPs within 20 kb of rs17499404 that are stronger in AncestryDNA than
rs2291433 (rs12646716, rs1487624, rs11732737, rs7668402) tag the lead weakly, r² 0.29 to 0.40 (q143-q146): none is a
proxy, so they are not scored at this lead. rs6812640, the lymphocyte set's lead, is r² 0.996 (q147); its G (0.544,
q149) against the lead's A (0.545) fits r² 0.996 only coupled (opposed at most about 0.70), so G rides with A.

## Reading 2026-11-11, record

> [q150] mappings[0] assembly_name GRCh38 ancestral_allele G allele_string T/G strand 1 seq_region_name 4 location 4:66914674-66914674 coord_system chromosome end 66914674 start 66914674

> [q151] populations[76] frequency 0.711729622266402 population 1000GENOMES:phase_3:EUR allele T allele_count 716

> [q152] populations[77] frequency 0.288270377733598 population 1000GENOMES:phase_3:EUR allele G allele_count 290

> [q153] populations[72] allele G population 1000GENOMES:phase_3:EAS frequency 0.056547619047619 allele_count 57

> [q154] [0] population_name 1000GENOMES:phase_3:EUR d_prime 0.481487 r2 0.094647 variation2 rs13141210 variation1 rs28637671

> [q155] [0] population_name 1000GENOMES:phase_3:EUR r2 0.511422 d_prime 0.992755 variation2 rs1481245 variation1 rs28637671

> [q156] [194] population_name 1000GENOMES:phase_3:EUR r2 0.050020 d_prime 0.784871 variation2 rs1471564 variation1 rs28637671

> [q157] populations[77] allele_count 441 population 1000GENOMES:phase_3:EUR allele G frequency 0.438369781312127

> [q158] populations[78] allele A population 1000GENOMES:phase_3:EUR frequency 0.561630218687873 allele_count 565

> [q159] [0] d_prime 0.950285 variation2 rs11947612 variation1 rs13141210 r2 0.531816 population_name 1000GENOMES:phase_3:EUR

> [q160] [0] population_name 1000GENOMES:phase_3:EUR variation1 rs13141210 variation2 rs923994 r2 0.241004 d_prime 0.935129

rs28637671 (RNU1-63P / RNU6-699P, 4q13.2), for row 28: 4:66,914,674 (GRCh38; 4:67,780,392 in GRCh37), T/G, G
ancestral (q150). T is 0.712 in 1000 Genomes Europeans (q151, q152; gnomAD non-Finnish 0.725), 0.94 in East Asians
(q153), 0.55 in Africans: common everywhere, G the minor allele. Under Hardy-Weinberg in Europeans: T/T about 51 in
100, T/G about 41, G/G about 8. Linkage disequilibrium (EUR): rs13141210, the locus's other mvAge SNP, r² 0.095
(D′ 0.48), a separate signal (q154). rs1481245 r² 0.51, D′ 0.99 (q155); phase by frequency and r² ceilings: its G
(0.44) and the lead's G (0.29) coupled allow r² up to about 0.52, opposed about 0.32 (with D′ near 1), so the observed
0.51 puts G with G and its A with the lead's T. The window listing around the lead (`ldwin-rs28637671.json`, ±100 kb,
r² floor requested 0.001) reports nothing below 0.050 (q156 its least value); the endpoint applies its own floor.
rs11947612 and rs923994 are absent from it although both are in the panel (q159, q160, read against rs13141210), and
the pairwise reads of the lead against them return nothing (`ld-` and `ld0-` files rendered to no text): their r² to
the lead is below 0.05. rs1481245's frequencies: q157, q158.

## Reading 2026-11-11, record

> [q161] [0] d_prime 0.987676 variation2 rs2164300 variation1 rs13141210 population_name 1000GENOMES:phase_3:EUR r2 0.937475

> [q162] [0] population_name 1000GENOMES:phase_3:EUR d_prime 1.000000 variation2 rs12506221 r2 0.856045 variation1 rs13141210

> [q163] [0] d_prime 0.973608 population_name 1000GENOMES:phase_3:EUR variation2 rs17799404 r2 0.385461 variation1 rs28637671

> [q164] [0] population_name 1000GENOMES:phase_3:EUR d_prime 0.982116 r2 0.257028 variation1 rs28637671 variation2 rs987811

> [q165] [0] variation2 rs12506243 d_prime 0.766629 population_name 1000GENOMES:phase_3:EUR variation1 rs28637671 r2 0.206245

> [q166] [0] population_name 1000GENOMES:phase_3:EUR r2 0.233302 variation2 rs1481245 variation1 rs13141210 d_prime 0.544549

> [q167] [159] population_name 1000GENOMES:phase_3:EUR variation2 rs28494793 variation1 rs28637671 r2 0.932821 d_prime 0.984887

> [q168] [337] d_prime 0.934429 r2 0.387545 variation2 rs13109040 variation1 rs28637671 population_name 1000GENOMES:phase_3:EUR

Row 28, after the advisor's read. rs13141210's tags in Wright's S9: rs2164300 r² 0.94 (q161), rs12506221 r² 0.86
(q162); at 0.50 against about 0.5 the frequency ceilings coupled and opposed are both near 1, so their phase to
rs13141210 is not read here. The lead's other Wright SNPs tag it weakly: rs17799404 r² 0.39 (q163), rs987811 0.26
(q164), rs12506243 0.21 (q165). rs1481245, the row's weak proxy, has r² 0.23 to rs13141210 (q166). The window listing
around the lead holds 54 variants at r² 0.8 or more (`ldwin-rs28637671.json`; rs6821811, rs56278947 and six others
at 1.0); rs28494793 (r² 0.93, q167) is the only one with a GWAS Catalog record (db-gwascatalog-2026.10.29#q198).
rs13109040 (r² 0.39, q168) leads Open Targets' paracetamol-use sets near the lead (db-opentargets-26.09#q441-q443).

## Reading 2026-11-11, record

> [q169] populations[76] population 1000GENOMES:phase_3:EUR frequency 0.365805168986084 allele_count 368 allele A

> [q170] [0] variation2 rs56172573 population_name 1000GENOMES:phase_3:EUR d_prime 0.991246 variation1 rs36072649 r2 0.961681

> [q171] [0] variation1 rs36072649 variation2 rs56172573 r2 0.908379 d_prime 1.000000 population_name 1000GENOMES:phase_3:EAS

> [q172] populations[75] allele C population 1000GENOMES:phase_3:EUR frequency 0.360834990059642 allele_count 363

> [q173] populations[73] population 1000GENOMES:phase_3:EAS frequency 0.307539682539683 allele_count 310 allele A

> [q174] populations[73] allele_count 331 population 1000GENOMES:phase_3:EAS allele C frequency 0.328373015873016

> [q175] [0] r2 0.698648 d_prime 0.955642 variation1 rs36072649 variation2 rs769673 population_name 1000GENOMES:phase_3:EUR

> [q176] populations[84] allele_count 308 allele A frequency 0.306163021868787 population 1000GENOMES:phase_3:EUR

Ensembl 116, row 29 (variation-rs36072649.json, variation-rs56172573.json, variation-rs769673.json,
ld-rs36072649-rs56172573.json and its -EAS, ld-rs36072649-rs769673.json, ldwin-rs36072649.json). rs36072649 (GRCh38
4:140,017,956 T/A): A 0.37 in 1000 Genomes EUR (q169), 0.31 in EAS (q173), the minor allele. rs56172573 (Timmers
2022's aging-GIP1 lead): r² 0.96 to the lead in EUR (q170), 0.91 in EAS (q171); its C 0.36 EUR (q172), 0.33 EAS
(q174) rides with the lead's A in both (the opposite phase caps r² near 0.3). rs769673, Wright's mothers' SNP: r² 0.70,
D′ 0.96 (q175), its A 0.31 (q176) with the lead's A. The 500 kb window listing (r² ≥ 0.05 shown) holds neither
rs6840907 (177 kb from the lead; ld-rs36072649-rs6840907.json renders to no text) nor rs4073315 (252 kb): below r²
0.05, not in the panel, or outside, unknown which; Wright's other SNPs here
(rs706333, rs10027416) lie about 0.4 Mb away, outside it, not read.

## Reading 2026-11-11, record

> [q177] [0] population_name 1000GENOMES:phase_3:EUR d_prime 1.000000 variation2 rs2815748 r2 0.993271 variation1 rs2613508

> [q178] [0] population_name 1000GENOMES:phase_3:EAS variation2 rs2815748 variation1 rs2613508 r2 1.000000 d_prime 1.000000

> [q179] populations[75] population 1000GENOMES:phase_3:EUR allele_count 181 allele G frequency 0.179920477137177

> [q180] populations[76] allele_count 180 frequency 0.178926441351889 population 1000GENOMES:phase_3:EUR allele C

> [q181] populations[89] population 1000GENOMES:phase_3:JPT allele_count 6 allele G frequency 0.0288461538461538

> [q182] [0] population_name 1000GENOMES:phase_3:EUR d_prime 0.999972 variation2 rs1230682 r2 0.243891 variation1 rs1230666

> [q183] populations[77] population 1000GENOMES:phase_3:EUR frequency 0.601391650099404 allele_count 605 allele A

> [q184] populations[67] allele_count 140 allele A population 1000GENOMES:phase_3:EUR frequency 0.139165009940358

> [q185] populations[65] allele_count 1008 allele G population 1000GENOMES:phase_3:EAS frequency 1

> [q186] [0] population_name 1000GENOMES:phase_3:EUR variation2 rs10434248 variation1 rs28637671 r2 0.125675 d_prime 0.510265

> [q187] [0] variation1 rs13141210 r2 0.838179 variation2 rs10434248 population_name 1000GENOMES:phase_3:EUR d_prime 0.995472

> [q188] [0] d_prime 0.999955 variation2 rs10434248 r2 0.153070 variation1 rs13141210 population_name 1000GENOMES:phase_3:EAS

> [q189] populations[72] allele A allele_count 562 frequency 0.557539682539683 population 1000GENOMES:phase_3:EAS

> [q190] populations[72] allele_count 163 allele T frequency 0.161706349206349 population 1000GENOMES:phase_3:EAS

> [q191] [0] variation2 rs61907878 r2 0.380013 variation1 rs61905747 population_name 1000GENOMES:phase_3:EUR d_prime 0.929761

> [q192] populations[69] allele T allele_count 73 population 1000GENOMES:phase_3:EUR frequency 0.0725646123260437

> [q193] populations[70] frequency 0.151093439363817 allele_count 152 population 1000GENOMES:phase_3:EUR allele C

> [q194] [0] variation2 rs7609078 r2 0.072160 variation1 rs78438918 population_name 1000GENOMES:phase_3:EUR d_prime 0.480088

> [q195] [0] population_name 1000GENOMES:phase_3:EAS d_prime 0.579490 variation1 rs78438918 r2 0.118876 variation2 rs7609078

> [q196] populations[110] allele T allele_count 159 frequency 0.764423076923077 population 1000GENOMES:phase_3:JPT

Ensembl 116, the sweep of Timmers 2022's survival look-up before row 30 (variation-rs2815748.json,
variation-rs2613508.json, variation-rs1230682.json, variation-rs1230666.json, variation-rs10434248.json,
variation-rs61907878.json, variation-rs61905747.json, variation-rs7609078.json, and the ld- files named by pair, -EAS
for East Asians). Row 4: rs2815748 r² 0.99 to rs2613508 in EUR (q177), 1.00 in EAS (q178); G 0.180 (q179) and C
0.179 (q180), so G rides with C; G 0.029 in JPT (q181). Row 7: rs1230682 r² 0.24, D′ 1.00 to rs1230666 (q182); A
0.60 (q183), the lead's A 0.14 (q184): at D′ 1 the lead's A lies on rs1230682's G (that phase gives r² 0.24, the
other about 0.02), so rs1230682's A always travels with the lead's G; the lead does not vary in EAS (q185). Row 28:
rs10434248 r² 0.13 to rs28637671 (q186), 0.84 to rs13141210 in EUR (q187), 0.15 in EAS (q188); in EAS A 0.56 (q189)
and T 0.16 (q190) at D′ 1 give r² 0.15 only with T inside A (the other phase about 0.24), so A rides with
rs13141210's T. Row 67: rs61907878 r² 0.38, D′ 0.93 to rs61905747 (q191); its T 0.073 (q192) inside the lead's C
0.151 (q193) gives about 0.4 at D′ 1 (the other phase about 0.01), so its C rides with the lead's A. Row 15: rs7609078
r² 0.07 EUR (q194), 0.12 EAS (q195), not the lead's signal. Row 21: rs2271961's T is 0.76 in JPT (q196).

## Reading 2026-11-11, record

> [q197] populations[77] population 1000GENOMES:phase_3:EUR frequency 0.290258449304175 allele A allele_count 292

> [q198] populations[3] population gnomADg:nfe allele_count 20521 allele A frequency 0.3024

> [q199] populations[73] allele A allele_count 676 frequency 0.670634920634921 population 1000GENOMES:phase_3:EAS

> [q200] mappings[0] location 5:29426329-29426329 ancestral_allele C assembly_name GRCh38 strand 1 start 29426329 end 29426329 allele_string A/C/T seq_region_name 5 coord_system chromosome

> [q201] [0] variation1 rs649357 r2 1.000000 variation2 rs694966 d_prime 1.000000 population_name 1000GENOMES:phase_3:EUR

> [q202] populations[78] frequency 0.290258449304175 population 1000GENOMES:phase_3:EUR allele_count 292 allele G

> [q203] [327] population_name 1000GENOMES:phase_3:EUR r2 0.990377 variation2 rs983077 variation1 rs649357 d_prime 1.000000

> [q204] [14] population_name 1000GENOMES:phase_3:EUR variation1 rs649357 variation2 rs631778 r2 1.000000 d_prime 1.000000

rs649357 (row 31's lead, GRCh38 5:29,426,329): A 0.29 in 1000 Genomes EUR (q197), 0.30 in gnomAD non-Finnish
Europeans (q198), 0.67 in EAS (q199), where it is the major allele. A triallelic site, A/C/T (q200), intergenic.
Its EUR proxies (window listing, `ldwin-rs649357.json`): rs694966 r² 1.0, D′ 1 (q201), its G 0.29 in EUR (q202), so
G travels with the lead's A; rs983077 r² 0.99 (q203); rs631778 r² 1.0 (q204). The window holds 56 SNPs at
r² ≥ 0.8. The lead's own imputed frequency runs high in UK Biobank and LifeGen (0.39 to 0.40) and in NECS's controls
(0.36), while its proxies sit at 0.31 in the same files. For row 31.

## Reading 2026-11-11, record

> [q205] mappings[0] allele_string C/A/G/T assembly_name GRCh38 coord_system chromosome ancestral_allele C end 82723979 location 5:82723979-82723979 strand 1 start 82723979 seq_region_name 5

> [q206] populations[57] allele_count 22 frequency 0.0218253968253968 population 1000GENOMES:phase_3:EAS allele T

> [q207] populations[14] population gnomADg:eas allele_count 115 frequency 0.02229 allele T

> [q208] populations[62] allele_count 6 frequency 0.0303030303030303 population 1000GENOMES:phase_3:FIN allele T

> [q209] populations[2] population gnomADg:fin frequency 0.02256 allele_count 238 allele T

> [q210] populations[7] frequency 0.0007798 allele_count 53 population gnomADg:nfe allele T

> [q211] populations[13] allele T frequency 0.02757 allele_count 421 population gnomADg:amr

> [q212] populations[60] population 1000GENOMES:phase_3:EUR frequency 0.00596421471172962 allele_count 6 allele T

> [q213] [2] d_prime 1.000000 population_name 1000GENOMES:phase_3:EAS variation2 rs191121907 r2 0.133786 variation1 rs138499810

> [q214] [0].transcript_consequences[2] transcript_id ENST00000835330 biotype lncRNA gene_id ENSG00000308603 strand -1 variant_allele T impact MODIFIER

rs138499810 (row 32's lead, GRCh38 5:82,723,979, a C/A/G/T site, q205; `variation-rs138499810.json`): T 0.022 in
1000 Genomes EAS (q206) and gnomAD East Asians (q207); 0.030 in 1000 Genomes Finns (q208) and 0.023 in gnomAD Finns
(q209); 0.0008 in gnomAD non-Finnish Europeans (q210), so near-absent outside Finland; 0.028 in gnomAD admixed Americans
(q211); 0.006 in 1000 Genomes EUR overall (q212), all from its FIN carriers (CEU and GBR carry none). So the allele is
not East Asian only: Finns and admixed Americans carry it as often, untested there. No East Asian proxy: in the EAS
window (`ldwin-rs138499810-EAS.json`, 500 kb, 33 SNPs listed at r² ≥ 0.001) the best is rs191121907 at r² 0.13 (q213).
The FIN window (`ldwin-rs138499810-FIN.json`, 99 Finns) lists rs531009177 at 0.79 and five SNPs at 0.74
(rs10942305, rs146787437, rs16899885, rs7734484, rs77791861), but these run at about 1 % in LifeGen and Zenin's mostly
British samples where the lead's T is 0.08 %, so they do not tag it there, and they are not proxies of the East Asian
signal (none reaches r² 0.14 in EAS). VEP: an intron of a lncRNA, ENSG00000308603 (q214). For row 32.

## Reading 2026-11-11, record

> [q215] populations[74] allele_count 389 allele T population 1000GENOMES:phase_3:EAS frequency 0.385912698412698

> [q216] populations[96] allele_count 342 allele G population 1000GENOMES:phase_3:EAS frequency 0.339285714285714

> [q217] populations[17] allele T allele_count 5669 population gnomADg:fin frequency 0.5377

> [q218] populations[25] population gnomADg:fin frequency 0.4636 allele G allele_count 4896

Population frequencies (var-rs61348208-pops.json, var-rs362273-pops.json). In 1000 Genomes East Asians, rs61348208
T 0.386 (q215) and rs362273 G 0.339 (q216). With G opposite T, r² could reach only about 0.32 (D at most 0.131 over
0.386 × 0.614 × 0.339 × 0.661); the EAS r² is 0.76 (q123), so G rides with T in East Asians, as in Europeans. In gnomAD
genomes' Finns, T 0.54 (q217) and G 0.46 (q218); there either phase allows r² near 0.7, so the phase in Finns is
assumed, not shown. For row 25.

## Reading 2026-11-11, record

> [q219] mappings[0] end 29427172 ancestral_allele A allele_string G/A/C location 5:29427172-29427172 strand 1 seq_region_name 5 coord_system chromosome start 29427172 assembly_name GRCh37

rs694966 on GRCh37 (grch37-var-rs694966.json, read from Ensembl's GRCh37 server, grch37.rest.ensembl.org; its data
release is that server's, which the key's release check, made against the main server, does not read): 5:29,427,172,
G/A/C, the position Deelen 2019's summary statistics print as 5:29427172 (pmid-31413261#q76). For row 31.

## Reading 2026-11-11, record

> [q220] mappings[0] assembly_name GRCh38 seq_region_name 5 allele_string C/T strand 1 end 158393594 coord_system chromosome start 158393594 location 5:158393594-158393594 ancestral_allele T

> [q221] populations[77] frequency 0.350894632206759 population 1000GENOMES:phase_3:EUR allele_count 353 allele T

> [q222] populations[13] allele T frequency 0.3707 population gnomADg:nfe allele_count 25161

> [q223] populations[72] allele C population 1000GENOMES:phase_3:EAS frequency 0.76984126984127 allele_count 776

> [q224] most_severe_consequence intron_variant name rs2149954 MAF 0.334576

rs2149954 (`variation-rs2149954.json`): GRCh38 5:158,393,594, C/T (q220); T 0.35 in 1000 Genomes Europeans (q221),
0.37 in gnomAD non-Finnish Europeans (q222), 0.23 in East Asians (C 0.77, q223); an intron variant by Ensembl's most
severe consequence (q224; Deelen's lincRNA, now LINC02227). Deelen's 157,753,180 is the hg18 position and LifeGen's and
Zenin's 157,820,602 the GRCh37 one, both tied by the rsID on their lines. For row 33.

## Reading 2026-11-11, record

> [q225] most_severe_consequence intron_variant

> [q226] mappings[0] location 6:396321-396321 end 396321 ancestral_allele C seq_region_name 6 start 396321 strand 1 allele_string C/G/T coord_system chromosome assembly_name GRCh38

> [q227] populations[73] allele T population 1000GENOMES:phase_3:EUR frequency 0.116302186878728 allele_count 117

> [q228] populations[23] allele_count 11449 frequency 0.1683 population gnomADg:nfe allele T

> [q229] populations[20] frequency 0.02597 allele_count 276 population gnomADg:fin allele T

> [q230] populations[1] allele_count 3 frequency 0.0005776 population gnomADg:eas allele T

> [q231] populations[7] frequency 0.03278 allele_count 1362 population gnomADg:afr allele T

rs12203592 (`variation-rs12203592.json`): an intron variant (q225) at GRCh38 6:396,321, the same coordinate as GRCh37's
(q226), C ancestral. T: 0.116 in 1000 Genomes Europeans (q227), 0.168 in gnomAD non-Finnish Europeans (q228), 0.026
in Finns (q229), 0.0006 in East Asians (q230), 0.033 in Africans (q231); 0.21 in the British samples (Zenin, Timmers).
T is commonest in north-west Europe; it is 0.078 in gnomAD's admixed Americans (q232), and in East and South Asians
almost everyone is C/C. For row 35.

## Reading 2026-11-11, record

> [q232] populations[5] frequency 0.07789 allele_count 1192 population gnomADg:amr allele T

> [q233] [0] r2 0.146242 variation1 rs12203592 d_prime 0.724712 population_name 1000GENOMES:phase_3:CEU variation2 rs11242982

rs12203592's T in gnomAD's admixed Americans, 0.078 (q232): about 15 in 100 carry a copy. Pairwise LD in 1000
Genomes CEU with the three Wright 2019 S9 SNPs near it (`ld-ceu-rs12203592-*.json`): rs11242982 r² 0.15, D′ 0.72
(q233); rs9378774 and rs1540767 return no pair (no text cached; Ensembl's floor), so neither is shown to tag the lead.
For row 35.

## Reading 2026-11-11, record

> [q234] location 6:28445714-28445714 seq_region_name 6 start 28445714 end 28445714 coord_system chromosome assembly_name GRCh38 strand 1 allele_string T/A/C ancestral_allele T

> [q235] populations[72] allele C population 1000GENOMES:phase_3:CEU frequency 0.313131313131313 allele_count 62

> [q236] populations[21] frequency 0.3108 population gnomADg:nfe allele C allele_count 21102

> [q237] populations[17] population gnomADg:fin allele C frequency 0.2174 allele_count 2279

> [q238] populations[4] allele C population gnomADg:eas frequency 0.1376 allele_count 713

> [q239] populations[14] frequency 0.4054 allele C population gnomADg:afr allele_count 16770

> [q240] populations[65] allele C frequency 0.146464646464646 allele_count 29 population 1000GENOMES:phase_3:CEU

rs6902687 (`variation-rs6902687.json`): GRCh38 6:28445714, T/A/C, ancestral T (q234). C 0.313 in 1000 Genomes CEU
(q235), 0.311 in gnomAD's non-Finnish Europeans (q236), 0.217 in Finns (q237), 0.138 in East Asians (q238), 0.405 in
Africans (q239); A is a rare third allele (0.0025 overall). rs1029328's C 0.146 in CEU (q240,
`variation-rs1029328.json`). Pairwise LD in CEU with the triallelic lead (`ld-ceu-rs6902687-*.json`) returns no pair at all, even for
rs13190937, which Park puts at R² > 0.99 (pmid-40021682#q21), so the lead's pairs are unknown, not zero. For row 36.

## Reading 2026-11-11, record

> [q241] [0] variation1 rs13190937 variation2 rs13215804 r2 1.000000 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000

> [q242] [0] variation2 rs3130507 r2 0.060778 variation1 rs13190937 d_prime 0.268403 population_name 1000GENOMES:phase_3:CEU

> [q243] [0] d_prime 0.941954 variation1 rs13190937 variation2 rs1029328 population_name 1000GENOMES:phase_3:CEU r2 0.333978

Pairwise LD in 1000 Genomes CEU with rs13190937 standing in for row 36's triallelic lead (Park's R² > 0.99 tag,
pmid-40021682#q21; `ld-ceu-rs13190937-*.json`): r² 1.0 to rs13215804, Park's other tag (q241), so the endpoint
answers at this site; r² 0.061 to row 37's lead rs3130507 (q242), a separate signal; r² 0.33 to Wright 2019's
rs1029328 (q243), not a tag. No pair returned for rs3131621 (row 37) or rs34967069 (row 38): unknown, not zero.
For row 36.

## Reading 2026-11-11, record

> [q244] [3148] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 r2 0.832000 variation2 rs1265159 variation1 rs3130507

> [q245] [1163] r2 0.951417 variation2 rs3130467 variation1 rs3130507 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000

> [q246] [2373] variation2 rs9265178 r2 0.050105 variation1 rs3130507 d_prime 0.411896 population_name 1000GENOMES:phase_3:CEU

The LD window around row 37's lead rs3130507 (`ld-window-ceu-rs3130507.json`, CEU, window 500 kb, r² ≥ 0.05; 71
variants at r² ≥ 0.8): Wright 2019's PSORS1C3 lead rs1265159 at r² 0.83, D′ 1 (q244), and rs3130467 at 0.95, D′ 1
(q245); the least value listed is 0.0501 (q246), the endpoint's floor. The seed's other rsID rs3131621 lies 278 kb
away, beyond the window's 250 kb on either side, so the listing does not reach it; the pairwise endpoint returns no
pair for the two (`ld-ceu-rs3130507-rs3131621.json`, no text).

> [q247] populations[65] allele_count 143 allele G population 1000GENOMES:phase_3:CEU frequency 0.722222222222222

> [q248] populations[64] allele A allele_count 131 frequency 0.661616161616162 population 1000GENOMES:phase_3:CEU

Both of row 37's seed SNPs are in the CEU panel: rs3130507 G 0.722 (q247), rs3131621 A 0.662 (q248). So the empty
pair reads as r² below the 0.05 floor (row 28's reading of an empty pair, q156). The pairwise endpoint is not limited
to the window's reach: it answered rs3130507 against row 36's rs13190937 (6:28.4 Mb, about 2.7 Mb away) with r² 0.061
(q242). So the earlier reading's "no pair returned for rs3131621 ... unknown, not zero" (row 36's tag against
rs3131621) also reads as r² below 0.05, both being in the panel. For row 37.

## Reading 2026-11-11, record

> [q249] [0] variation2 rs4970836 r2 0.903728 variation1 rs646776 population_name 1000GENOMES:phase_3:CEU d_prime 0.974359

Pairwise LD in 1000 Genomes CEU (`ld-rs646776-rs4970836.json`): Timmers 2019's CELSR2/PSRC1 SNP rs4970836 tags row
6's lead rs646776 at r² 0.90 (D′ 0.97), so Figure 5's bands for rs4970836 are read for row 6. For the Figure 5 sweep.

## Reading 2026-11-11, record

> [q250] mappings[0] location 6:34624313-34624313 seq_region_name 6 start 34624313 end 34624313 coord_system chromosome assembly_name GRCh38 strand 1 allele_string A/G ancestral_allele A

> [q251] populations[74] allele A population 1000GENOMES:phase_3:EUR frequency 0.898608349900596 allele_count 904

> [q252] populations[75] allele_count 102 frequency 0.101391650099404 allele G population 1000GENOMES:phase_3:EUR

> [q253] populations[75] population 1000GENOMES:phase_3:EUR frequency 0.13220675944334 allele_count 133 allele T

> [q254] populations[75] allele C allele_count 140 frequency 0.139165009940358 population 1000GENOMES:phase_3:EUR

> [q255] [495] population_name 1000GENOMES:phase_3:CEU d_prime 0.999997 r2 0.791662 variation2 rs9462007 variation1 rs6907508

> [q256] [176] variation2 rs9462014 r2 0.728448 variation1 rs6907508 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000

> [q257] [590] variation1 rs6907508 variation2 rs145294670 r2 1.000000 d_prime 1.000000 population_name 1000GENOMES:phase_3:CEU

> [q258] [24] d_prime 1.000000 population_name 1000GENOMES:phase_3:CEU variation1 rs6907508 variation2 rs3800461 r2 1.000000

> [q259] [66] d_prime 0.999998 population_name 1000GENOMES:phase_3:CEU variation1 rs6907508 variation2 rs2492863 r2 0.826920

> [q260] [315] variation1 rs6907508 r2 0.826920 variation2 rs2814948 d_prime 0.999998 population_name 1000GENOMES:phase_3:CEU

> [q261] [332] variation1 rs6907508 variation2 rs2814993 r2 0.826920 d_prime 0.999998 population_name 1000GENOMES:phase_3:CEU

rs6907508 at 6:34,624,313 (GRCh38; 6:34,592,090 in GRCh37), A/G, A ancestral (q250); A 0.899, G 0.101 in 1000 Genomes
EUR (q251, q252). Ensembl's CEU window (`ld-window-ceu-rs6907508.json`, ±250 kb, r² ≥ 0.05) holds 35 SNPs at r² ≥ 0.8.
Wright's tags: rs9462007 r² 0.79, D′ 1.00 (q255), its T 0.13 in EUR (q253); rs9462014 r² 0.73, D′ 1.00 (q256), its C
0.14 (q254). The proxies whose GWAS Catalog records row 39 reads: rs145294670 and rs3800461, r² 1.00 (q257, q258);
rs2492863, rs2814948 and rs2814993, r² 0.83, D′ 1.00 (q259 to q261). At D′ 1 a minor allele near the lead's 10 %
travels with the lead's minor G (derived, not phased).
The edge of the window: rs112563428 (r² 1.00, 208 kb from the lead) has its own CEU window cached
(`ld-window-ceu-rs112563428.json`, r² ≥ 0.8); it holds the lead and the same 35 SNPs, none further, so the block
ends inside the lead's window and the proxy sweep is whole.

## rs7742789 (ZNF318 / ABCC10), for row 40

> [q262] mappings[0] assembly_name GRCh38 seq_region_name 6 allele_string C/T strand 1 coord_system chromosome end 43378065 start 43378065 ancestral_allele C location 6:43378065-43378065

> [q263] populations[76] allele_count 350 frequency 0.347912524850895 population 1000GENOMES:phase_3:EUR allele T

> [q264] [180] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 r2 0.835820 variation2 rs1214759 variation1 rs7742789

> [q265] [350] population_name 1000GENOMES:phase_3:CEU variation2 rs7692 variation1 rs7742789 d_prime 0.999998 r2 0.867407

> [q266] [30] r2 0.561582 d_prime 0.999995 variation1 rs7742789 variation2 rs6919440 population_name 1000GENOMES:phase_3:CEU

rs7742789 at 6:43,378,065 (GRCh38; 6:43,345,803 in GRCh37), C/T, C ancestral (q262); T 0.35 in 1000 Genomes EUR
(q263), 0.31 in gnomAD non-Finnish Europeans and 0.72 in 1000 Genomes AFR (`variation-rs7742789.json`). Ensembl's CEU
window (`ld-window-ceu-rs7742789.json`, ±250 kb, r² ≥ 0.05) holds 15 SNPs at r² ≥ 0.8, the strongest rs7692,
rs58804120 and rs1563788 at 0.87 (q265). Wright's tag rs1214759: r² 0.84, D′ 1.00 (q264); its A (0.32) travels with
the lead's T (0.30 to 0.35) at D′ 1 (derived, not phased; both shorten life in LifeGen, pmid-30642433#q214, q215).
rs6919440, Wright's other fathers line, is at r² 0.56 (q266). For row 40.

## Reading 2026-11-11, record

> [q267] populations[14] frequency 0.3085 population gnomADg:nfe allele_count 20972 allele T

> [q268] [346] variation2 rs2270860 variation1 rs7742789 r2 0.755517 d_prime 0.922022 population_name 1000GENOMES:phase_3:CEU

> [q269] [68] population_name 1000GENOMES:phase_3:CEU r2 0.825704 d_prime 1.000000 variation2 rs6901866 variation1 rs7742789

> [q270] [250] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 r2 0.854320 variation1 rs7742789 variation2 rs7764523

Row 40's lead: T 0.31 in gnomAD non-Finnish Europeans (q267), against 0.35 in 1000 Genomes EUR (q263) and 0.32 in CEU;
the large samples agree with gnomAD (LifeGen 0.30, pmid-30642433#q214; Deelen 0.30, pmid-31413261#q97; Finns 0.29,
db-finngen-r11#q11). The kidney-disease sets' leads: rs2270860 r² 0.76, D′ 0.92 (q268); rs6901866 r² 0.83, D′ 1.00
(q269); rs7764523 r² 0.85, D′ 1.00 (q270). The lead's 15 proxies at r² ≥ 0.8 lie from 6:43,292,922 (rs6901866) to
6:43,386,693 (rs1214761) in GRCh38 (the catalog's locations), 85 kb before the lead to 9 kb after it, so the block
sits well inside the ±250 kb window and the proxy sweep is whole. For row 40.

## Reading 2026-11-11, record

> [q271] mappings[0] start 99603424 coord_system chromosome strand 1 allele_string G/A location 6:99603424-99603424 end 99603424 ancestral_allele G assembly_name GRCh38 seq_region_name 6

> [q272] populations[16] allele_count 6616 frequency 0.09731 allele A population gnomADg:nfe

> [q273] populations[19] frequency 0.1331 allele A population gnomADg:asj allele_count 462

> [q274] populations[77] allele_count 114 allele A population 1000GENOMES:phase_3:EUR frequency 0.113320079522863

> [q275] [205] variation1 rs114658003 variation2 rs66927770 r2 1.000000 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000

> [q276] [32] r2 0.605050 population_name 1000GENOMES:phase_3:CEU variation2 rs12660804 variation1 rs114658003 d_prime 0.999997

> [q277] mappings[0] end 99603423 allele_string C/- seq_region_name 6 start 99603423 strand 1 location 6:99603423-99603423 assembly_name GRCh38 ancestral_allele C coord_system chromosome

> [q278] populations[18] allele_count 6616 allele - population gnomADg:nfe frequency 0.09731

> [q279] [7] seq_region_name 6 consequence_type regulatory_region_variant start 99603423 id rs386704200 feature_type variation source dbSNP end 99603424 assembly_name GRCh38 strand 1 [7].alleles[0] CG [7].alleles[1] A

> [q280] populations[65] allele_count 16 frequency 0.0808080808080808 population 1000GENOMES:phase_3:CEU allele A

Row 41's lead rs114658003, GRCh38 6:99,603,424 G/A (q271; GRCh37 6:100,051,300). A is common: 0.097 in gnomAD's
non-Finnish Europeans (q272), 0.133 in Ashkenazi Jews (q273), 0.113 in 1000 Genomes EUR (q274), 0.081 in CEU (q280),
about 0.19 overall. Gurinovich's NECS controls, 0.0004 (pmid-33948810#q22), and the LGP's near 0 (pmid-33948810#q18)
are off by two orders of magnitude. The deletion rs66927770 sits one base before it (q277), with the very same allele
count, 6,616, in gnomAD's non-Finnish Europeans (q278) and r² 1.00, D′ 1.00 in CEU (q275); dbSNP also holds the two as
one record, rs386704200, CG>A (q279, from the region listing `overlap-6-99603424`). So in Europeans the deletion and
A travel together. That NECS's imputation split them, calling A without the deletion, is a candidate cause of the
miscall, derived, not shown: the HRC panel's site list is not read. In the CEU window nothing besides the deletion passes r² 0.8;
seven pass 0.6, all at r² 0.61 and D′ 1.00 (rs12660804, q276, and six more), whose minor alleles (about 0.05 to 0.07)
ride with A by r² and frequency (derived, not phased). For row 41.

## Reading 2026-11-11, record

> [q281] mappings[0] seq_region_name 6 location 6:107079224-107079224 coord_system chromosome end 107079224 start 107079224 assembly_name GRCh38 ancestral_allele C allele_string C/A/G/T strand 1

> [q282] populations[22] allele_count 21538 allele A population gnomADg:nfe frequency 0.317

> [q283] populations[78] frequency 0.314115308151093 population 1000GENOMES:phase_3:EUR allele A allele_count 316

> [q284] [68] r2 0.335381 population_name 1000GENOMES:phase_3:CEU variation1 rs1627804 variation2 rs9384641 d_prime 0.999979

> [q285] [51] variation2 rs1630395 variation1 rs1627804 r2 1.000000 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000

Row 42's lead rs1627804, intronic in BEND3, GRCh38 6:107,079,224 (q281; GRCh37 107,400,428), C ancestral and the
reference, A the alternative. A is 0.317 in gnomAD's non-Finnish Europeans (q282), 0.314 in 1000 Genomes EUR (q283),
0.28 in CEU, 0.43 in Finns, about 0.31 overall: C/C is the most common European genotype (about 47 in 100, C/A 43,
A/A 10, derived). The CEU window (±500 kb, r² ≥ 0.05; `ld-window-ceu-rs1627804`) holds eleven SNPs at r² ≥ 0.8, ten
at r² 1.00 (rs1630395, q285; rs61282127, rs311217 to rs311220, rs311224, rs1762716, rs1665909, rs1618476) and
rs36101665 at 0.98; five more at 0.75. Wright's fathers' tag rs9384641 has r² 0.34, D′ 1.00 (q284). For row 42.

## Reading 2026-11-11, record

> [q286] mappings[0] strand 1 end 108587315 ancestral_allele G assembly_name GRCh38 seq_region_name 6 coord_system chromosome allele_string G/T start 108587315 location 6:108587315-108587315

> [q287] populations[20] allele T allele_count 41573 population gnomADg:nfe frequency 0.6122

> [q288] populations[8] population gnomADg:eas frequency 0.3169 allele G allele_count 1631

> [q289] populations[21] allele_count 26337 allele G frequency 0.3878 population gnomADg:nfe

> [q290] [168] d_prime 0.968008 population_name 1000GENOMES:phase_3:CEU variation1 rs2802292 variation2 rs10457180 r2 0.626294

> [q291] [220] r2 0.403218 variation2 rs1159806 variation1 rs2802292 population_name 1000GENOMES:phase_3:CEU d_prime 0.679480

> [q292] [309] variation1 rs2802292 r2 0.602445 variation2 rs3800231 d_prime 0.937318 population_name 1000GENOMES:phase_3:CEU

Row 43's lead rs2802292, intronic in FOXO3, GRCh38 6:108,587,315 (q286; GRCh37 108,908,518), G ancestral and the
reference, T the alternative. G is 0.388 in gnomAD's non-Finnish Europeans (q289, T 0.612, q287), 0.43 in 1000
Genomes EUR, 0.35 in CEU, 0.317 in East Asians (q288): in Europeans G/T is the most common genotype (about 47 in 100,
T/T 37, G/G 15, derived), as LifeGen's 0.38, Deelen's 0.38 and FinnGen's 0.42 for G also give. The CEU window
(±500 kb; `ld-rs2802292.json`) puts rs2490272, rs2802288 and rs2253310 at r² 1.00 with it; Broer's second SNP
rs10457180 at 0.63 (q290); Timmers 2020's multivariate lead rs1159806 at 0.40, D′ 0.68 (q291); Flachsbart's
rs3800231 at 0.60 (q292). For row 43.

> [q293] [324] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 r2 0.978213 variation2 rs6911407 variation1 rs2802292

rs6911407 (GRCh38 6:108,545,828, C/A), 41 kb from the lead: r² 0.98, D′ 1.00 in CEU (q293). For row 43.

## Reading 2026-11-11, record

> [q294] mappings[0] seq_region_name 6 ancestral_allele C end 118368937 assembly_name GRCh38 strand 1 start 118368937 location 6:118368937-118368937 coord_system chromosome allele_string C/T

> [q295] populations[9] allele_count 2646 allele T population gnomADg:afr frequency 0.06374

> [q296] populations[15] frequency 0.0001618 population gnomADg:nfe allele_count 11 allele T

> [q297] populations[58] frequency 1 population 1000GENOMES:phase_3:EUR allele_count 1006 allele C

> [q298] populations[0] frequency 0.06113 population gnomADg:afr allele A allele_count 2538

> [q299] populations[6] frequency 0.0001471 population gnomADg:nfe allele A allele_count 10

> [q300] populations[16] allele_count 2980 frequency 0.07174 allele T population gnomADg:afr

> [q301] populations[7] allele_count 12 frequency 0.0001764 allele T population gnomADg:nfe

> [q302] populations[11] allele_count 1870 frequency 0.04707 population gnomADg:afr allele A

> [q303] populations[7] allele A population gnomADg:nfe frequency 8.88e-05 allele_count 6

Row 44's lead rs76888380 (`variation-rs76888380.json`), an intron variant by Open Targets' label, in 6q22.31 near PLN, GRCh38
6:118,368,937, C ancestral and the reference, T the alternative (q294). T is an African-ancestry allele: 0.064 in
gnomAD's African and African American genomes (q295), 0.00016 in non-Finnish Europeans (11 copies, q296), absent
in 1000 Genomes EUR (q297), Finns and East Asians (0 in gnomAD). Three of the variants that pass 5e-8 beside it in
Park's deposit (pmid-40021682#q44 to #q46), found by position (`overlap-6-*.json`) and read
(`variation-<rsid>.json`), show the same pattern: rs78528818's A 0.061 African, 0.00015 European (q298, q299);
rs73768654's T 0.072 and 0.00018 (q300, q301); rs73768634's A 0.047 and 0.00009 (q302, q303). One African haplotype,
carried by a few dozen of UK Biobank's European-ancestry participants (derived).

The records above are GRCh38; the deposits and Deelen's, Zenin's and LifeGen's files are GRCh37. The offset used
to place the lead and its neighbours in them (GRCh37 = GRCh38 + 321,163 here) is checked on a quoted variant:
rs9320648 at 118,690,014 in LifeGen (pmid-30642433#q225) and Zenin (pmid-30729179#q67), at 118,368,851 in FinnGen's
GRCh38 file (db-finngen-r11#q19). The three neighbours were found from the deposit's GRCh37 positions by that offset
(`overlap-6-*.json`), and their alleles match the deposit's variant ids. For row 44.

## Reading 2026-11-11, record

> [q304] mappings[0] location 6:126665850-126665850 start 126665850 allele_string A/C/G/T coord_system chromosome ancestral_allele G end 126665850 assembly_name GRCh38 seq_region_name 6 strand 1

> [q305] mappings[0] allele_string A/C/G/T assembly_name GRCh37 coord_system chromosome end 126986996 strand 1 ancestral_allele G seq_region_name 6 start 126986996 location 6:126986996-126986996

> [q306] allele_count 242 allele A frequency 0.240556660039761 population 1000GENOMES:phase_3:EUR

> [q307] allele_count 24 allele A frequency 0.0238095238095238 population 1000GENOMES:phase_3:EAS

> [q308] frequency 0.2511 population gnomADg:nfe allele_count 17060 allele A

> [q309] allele A allele_count 4476 population gnomADg:afr frequency 0.1079

rs1262476 (`variation-rs1262476.json`, `variation-grch37-rs1262476.json`): GRCh38 6:126,665,850 (q304), GRCh37
6:126,986,996 (q305), the position Deelen, LifeGen and Zenin print. The reference is A, the ancestral allele G. A
is 0.24 in 1000 Genomes Europeans (q306) and 0.25 in gnomAD's non-Finnish Europeans (q308), 0.024 in East Asians
(q307), and about 0.11 in gnomAD's African genomes (q309); 0.19 in Finns (gnomAD). G/G is the commonest
genotype in Europeans (about 0.57, derived). Its most severe consequence is intronic (q310). For row 45.

> [q310] most_severe_consequence intron_variant

## Reading 2026-11-11, record

> [q311] synonyms[3] rs528161076

> [q312] . name rs371933919 MAF 0.0370879 var_class indel source Variants (including SNPs and indels) imported from dbSNP most_severe_consequence intron_variant ambiguity null minor_allele CCCCCCCCC

> [q313] mappings[0] start 4787884 allele_string CCCCCCCC/CCCCC/CCCCCCC/CCCCCCCCC/CCCCCCCCCC seq_region_name 7 end 4787891 assembly_name GRCh38 ancestral_allele CCCCCCCC coord_system chromosome strand 1 location 7:4787884-4787891

> [q314] mappings[0] coord_system chromosome allele_string CCCCCCCC/CCCCC/CCCCCCC/CCCCCCCCC/CCCCCCCCCC assembly_name GRCh37 ancestral_allele CCCCCCCC end 4827522 strand 1 start 4827515 seq_region_name 7 location 7:4827515-4827522

> [q315] allele CCCCCCCCC allele_count 1874 frequency 0.02785 population gnomADg:nfe

> [q316] allele CCCCCCCCC allele_count 30 frequency 0.0298210735586481 population 1000GENOMES:phase_3:EUR

> [q317] allele_count 3664 allele CCCCCCCCC population gnomADg:afr frequency 0.09002

> [q318] allele CCCCCCCCC allele_count 3 population gnomADg:eas frequency 0.000591

> [q319] frequency 0.008954 population gnomADg:fin allele CCCCCCCCC allele_count 93

rs528161076, the seed's id, is now a synonym of rs371933919 (`variation-rs528161076.json` answers with rs371933919's
record, q311, q312): an insertion of one C in a run of eight, GRCh38 7:4,787,884 to 4,787,891 (q313), GRCh37
4,827,515 to 4,827,522 (q314); left-aligned, the T at 4,787,883 (GRCh38) or 4,827,514 (GRCh37) with TC as the
insertion, as Pilling (pmid-27015805#q13), FinnGen (db-finngen-r11#q22) and Open Targets
(db-opentargets-26.09#q604) write it. The insertion (nine Cs) is 0.028 in gnomAD's non-Finnish Europeans (q315),
0.030 in 1000 Genomes Europeans (q316), 0.090 in gnomAD's African genomes (q317), 0.0006 in East Asians (q318) and
0.009 in Finns (q319). The record's other synonyms include HGVS names (NM_002117 c.662A>G and the like) that this
reading does not explain; they are not read or used. Its most severe consequence is intronic (q312). For row 47.

## Reading 2026-11-11, record

> [q320] mappings[0] ancestral_allele A assembly_name GRCh38 coord_system chromosome strand 1 location 7:22728408-22728408 allele_string A/C/G seq_region_name 7 end 22728408 start 22728408

> [q321] location 7:22768027-22768027

> [q322] population 1000GENOMES:phase_3:EAS frequency 0.140873015873016 allele_count 142 allele G

> [q323] allele G allele_count 30 population 1000GENOMES:phase_3:CHS frequency 0.142857142857143

> [q324] population 1000GENOMES:phase_3:CHB frequency 0.160194174757282 allele G allele_count 33

> [q325] population 1000GENOMES:phase_3:EUR frequency 0.0894632206759443 allele G allele_count 90

> [q326] frequency 0.1701 population gnomADg:eas allele_count 881 allele G

> [q327] frequency 0.07344 population gnomADg:nfe allele_count 4995 allele G

rs2069837 (`variation-rs2069837.json`, and its GRCh37 record): GRCh38 7:22,728,408 (q320), GRCh37 7:22,768,027
(q321), A/G (C a third allele, not used), an IL6 intron. G is 0.141 in 1000 Genomes East Asians (q322), 0.143 in
southern Han Chinese (CHS, q323), 0.160 in northern Han (CHB, q324), 0.089 in Europeans (q325); gnomAD's East Asian
genomes 0.170 (q326), non-Finnish Europeans 0.073 (q327). Zeng's southern controls' 0.033 (pmid-26912274#q4) is about
a quarter of CHS's. For row 48.

## Reading 2026-11-11, record

> [q328] coord_system chromosome strand 1 allele_string A/G/T location 7:34054385-34054385 end 34054385 start 34054385 assembly_name GRCh38 seq_region_name 7 ancestral_allele G

> [q329] start 34093997 assembly_name GRCh37 location 7:34093997-34093997

> [q330] allele G population 1000GENOMES:phase_3:EAS frequency 0.0962301587301587 allele_count 97

> [q331] population 1000GENOMES:phase_3:CHS allele G frequency 0.0619047619047619 allele_count 13

> [q332] allele_count 25 frequency 0.121359223300971 population 1000GENOMES:phase_3:CHB allele G

> [q333] frequency 0.0984095427435388 allele G population 1000GENOMES:phase_3:EUR allele_count 99

> [q334] frequency 0.1021 population gnomADg:eas allele G allele_count 529

> [q335] frequency 0.08113 allele G population gnomADg:nfe allele_count 5518

> [q336] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation2 rs17169630 r2 1.000000 variation1 rs17169634

rs17169634 (`variation-rs17169634.json`, `variation-grch37-rs17169634.json`): GRCh38 7:34,054,385 (q328), GRCh37
7:34,093,997 (q329), A/G (T a third allele, not used), a BMPER intron. G is 0.096 in 1000 Genomes East Asians (q330),
0.062 in southern Han (CHS, q331), 0.121 in northern Han (CHB, q332), 0.098 in Europeans (q333); gnomAD genomes 0.102
East Asian (q334), 0.081 non-Finnish European (q335). So the allele is as common in Europe as in China. In CEU
(`ld-ceu-rs17169634.json`, 500 kb, r² ≥ 0.8) 16 variants tag it, every one at r² 1.0, among them rs17169630 (q336).
For row 49.

## Reading 2026-11-11, supplement

> [q337] mappings[0] start 114608796 location 7:114608796-114608796 allele_string A/G end 114608796 coord_system chromosome strand 1 ancestral_allele A assembly_name GRCh38 seq_region_name 7

> [q338] allele_count 23254 allele G population gnomADg:nfe frequency 0.3423

> [q339] allele_count 374 population 1000GENOMES:phase_3:EUR allele G frequency 0.371769383697813

> [q340] allele_count 20 frequency 0.0198412698412698 population 1000GENOMES:phase_3:EAS allele G

> [q341] frequency 0.262626262626263 allele G population 1000GENOMES:phase_3:FIN allele_count 52

> [q342] population_name 1000GENOMES:phase_3:CEU r2 1.000000 d_prime 1.000000 variation2 rs34526725 variation1 rs12705966

> [q343] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 r2 0.977926 variation2 rs2189012 variation1 rs12705966

> [q344] d_prime 0.711452 variation1 rs12705966 variation2 rs2396766 r2 0.211810 population_name 1000GENOMES:phase_3:CEU

Row 50's FOXP2 lead rs12705966 (`variation-rs12705966.json`, `ld-ceu-rs12705966.json`,
`ld-ceu-rs12705966-rs2396766.json`): GRCh38 7:114,608,796, A/G, A ancestral (q337). G is 0.34 in gnomAD non-Finnish
Europeans (q338), 0.37 in 1000 Genomes EUR (q339), 0.26 in FIN (q341) and 0.02 in EAS (q340). At gnomAD's 0.342:
A/A about 43 in 100, A/G 45, G/G 12 (derived). Nine CEU variants within 500 kb at r² ≥ 0.8: rs34526725 at 1.00 (q342),
six at 0.98 (rs2189012, q343, the ADHD proxy of pmid-37118362#q63, with rs7797335, rs1229760, rs1229761, rs1229762,
rs2045292), rs9969232 0.85 and rs4727799 0.83. Atkins' frailty lead rs2396766 is r² 0.21, D′ 0.71 (q344). For row 50.

## Reading 2026-11-11, supplement

> [q345] allele_string G/A coord_system chromosome seq_region_name 7 end 130045757 start 130045757 strand 1 assembly_name GRCh38 ancestral_allele G location 7:130045757-130045757

> [q346] allele A allele_count 26083 frequency 0.3844 population gnomADg:nfe

> [q347] allele_count 388 allele A frequency 0.385685884691849 population 1000GENOMES:phase_3:EUR

> [q348] allele A allele_count 433 frequency 0.429563492063492 population 1000GENOMES:phase_3:EAS

> [q349] population_name 1000GENOMES:phase_3:CEU variation2 rs11556924 variation1 rs56179563 r2 0.936464 d_prime 0.978125

> [q350] d_prime 0.999987 r2 0.404908 population_name 1000GENOMES:phase_3:CEU variation2 rs1464890 variation1 rs56179563

> [q351] d_prime 0.999973 population_name 1000GENOMES:phase_3:CEU variation1 rs56179563 variation2 rs2242487 r2 0.325833

> [q352] d_prime 0.999923 population_name 1000GENOMES:phase_3:CEU r2 0.216093 variation2 rs12706910 variation1 rs56179563

> [q353] variation1 rs56179563 variation2 rs13245505 r2 0.239573 d_prime 0.999952 population_name 1000GENOMES:phase_3:CEU

> [q354] most_severe_consequence missense_variant MAF null name rs11556924

> [q355] allele T allele_count 379 population 1000GENOMES:phase_3:EUR frequency 0.376739562624254

> [q356] allele C allele_count 958 frequency 0.950396825396825 population 1000GENOMES:phase_3:EAS

Row 51's ZC3HC1 lead rs56179563 (`variation-rs56179563.json`, `ld-ceu-rs56179563.json`, the pairwise files): GRCh38
7:130,045,757, G/A, G ancestral (q345); A, the lifespan-raising allele, at 0.384 in gnomAD non-Finnish Europeans,
0.386 in 1000 Genomes EUR (q346, q347) and 0.43 in EAS (q348). Genotypes in EUR by Hardy-Weinberg (derived): G/G
0.38, A/G 0.47, A/A 0.15, so A/G is the most common. The CEU window (r² ≥ 0.8, 500 kb) holds one SNP, rs11556924
(r² 0.94, D′ 0.98, q349; the pairwise call agrees), ZC3HC1's missense variant (q354), T at 0.377 in EUR (q355) but
C at 0.95 in EAS (q356): T is rare in East Asians while A is common, so the two do not travel together there (derived),
and the coding SNP's effects cannot be carried to East Asians through the lead. Wright's AncestryDNA SNPs tag the lead
weakly: rs1464890 r² 0.40 (q350), rs2242487 0.33 (q351), rs12706910 0.22 (q352), rs13245505 0.24 (q353), each at D′
1.00. For row 51.

## Reading 2026-11-11, supplement

> [q357] name rs268 MAF null var_class SNP source Variants (including SNPs and indels) imported from dbSNP most_severe_consequence missense_variant

rs268 (`variation-rs268.json`): a missense variant (the protein change is read from VEP, q367; Rosoff calls it exonic in
LPL, pmid-37550455#q47). For row 52.

> [q358] populations[33] frequency 0.01858 allele G population gnomADg:nfe allele_count 1264

gnomAD genomes, non-Finnish Europeans: G 0.0186, so A 0.981: A/A about 96 in 100, A/G about 4 in 100, G/G about 3
in 10,000 (derived, Hardy-Weinberg). For row 52.

> [q359] populations[85] population 1000GENOMES:phase_3:EUR allele G frequency 0.0139165009940358 allele_count 14

1000 Genomes EUR: G 0.0139 (14 copies). For row 52.

> [q360] populations[83] frequency 1 allele A population 1000GENOMES:phase_3:EAS allele_count 1008

1000 Genomes EAS: A fixed (G absent); gnomAD's African G is 0.003. The evidence and the variant are European. For
row 52.

> [q361] populations[78] frequency 0.00505050505050505 allele G population 1000GENOMES:phase_3:CEU allele_count 1

1000 Genomes CEU: one copy of G among 198, so pairwise LD with rs268 from CEU (or GBR, also one copy) rests on one
chromosome; the endpoint returned nothing for rs268 with rs15285 in CEU or GBR (`ld-rs268-rs15285`, `ld-gbr-…`),
which at its 0.05 floor reads as no LD above it, on that one copy; the EUR request (`ld-eur-…`) also returned
nothing, and whether EUR is a panel the endpoint serves is not known here, so that one is unknown, not a null. For row 52.

> [q362] most_severe_consequence 3_prime_UTR_variant name rs15285

rs15285 (`variation-rs15285.json`): LPL 3′ UTR. For row 52.

> [q363] populations[11] population gnomADg:nfe allele T frequency 0.292 allele_count 19840

gnomAD genomes non-Finnish Europeans: T 0.292. For row 52.

> [q364] populations[84] frequency 0.317097415506958 allele T population 1000GENOMES:phase_3:EUR allele_count 319

1000 Genomes EUR: T 0.317. With rs268's G at 0.014, the largest r² two alleles of these frequencies can have is
0.014 × 0.683 / (0.986 × 0.317), about 0.03; with gnomAD's 0.0186 and 0.292 (q358, q363), about 0.047 (both
derived): below 0.05 either way, whichever alleles pair: rs268 and rs15285 are separate
signals, as Open Targets' two separate coronary disease sets in one study also show (db-opentargets-26.09#q671,
q678). For row 52.

> [q365] [0] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation2 rs13702 r2 0.976479 variation1 rs15285

rs15285 tags rs13702, LPL's other 3′ UTR SNP, at r² 0.98 (CEU). For row 52.

> [q366] [0] variation2 rs328 r2 0.332365 variation1 rs15285 d_prime 0.999992 population_name 1000GENOMES:phase_3:CEU

and rs328, another LPL SNP, at r² 0.33, D′ 1.0 (CEU). For row 52.

## Reading 2026-11-11, supplement

> [q367] codons aAt/aGt variant_allele G sift_score 0.35 impact MODERATE amino_acids N/S polyphen_prediction benign gene_symbol LPL strand 1 cds_end 953 cdna_start 1141 sift_prediction tolerated protein_end 318 cds_start 953 polyphen_score 0.142 protein_start 318

Ensembl VEP for rs268 (`vep-rs268.json`), transcript ENST00000650287 (LPL, protein coding): codon aAt to aGt, amino
acids N/S at protein position 318, so G changes asparagine 318 to serine (Asn318Ser in this numbering, which counts
the signal peptide). SIFT calls it tolerated (0.35), PolyPhen benign (0.142): the predictors do not call it damaging,
and the row reads its effect from the association data, not from them. For row 52.

## Reading 2026-11-11, supplement

> [q368] [0].transcript_consequences[0] impact MODIFIER hgnc_id HGNC:4695 gene_symbol GULOP biotype unitary_pseudogene variant_allele A transcript_id ENST00000454030 gene_id ENSG00000234770 strand 1 gene_symbol_source HGNC

Ensembl VEP for rs7844965 (`vep-rs7844965.json`): its only transcript consequence is an intron of GULOP
(ENST00000454030), a unitary pseudogene, a modifier; no protein-coding gene's transcript holds it. For row 53.

> [q369] populations[5] frequency 0.2292 allele A population gnomADg:nfe allele_count 15577

gnomAD genomes, non-Finnish Europeans: A 0.229. For row 53.

> [q370] populations[76] allele_count 233 population 1000GENOMES:phase_3:EUR allele A frequency 0.231610337972167

1000 Genomes EUR: A 0.232. G/G about 59 in 100, A/G about 35, A/A about 5 (Hardy-Weinberg, derived). For row 53.

> [q371] populations[72] frequency 0.146825396825397 population 1000GENOMES:phase_3:EAS allele A allele_count 148

1000 Genomes EAS: A 0.147. Untested in East Asians. For row 53.

> [q372] [0] variation2 rs6558008 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation1 rs7844965 r2 0.968269

rs7844965 with rs6558008 in CEU: r² 0.97, D′ 1.00. One signal. For row 53.

> [q373] [0] population_name 1000GENOMES:phase_3:CEU d_prime 0.658662 variation2 rs11780471 r2 0.128361 variation1 rs7844965

rs7844965 with rs11780471 in CEU: r² 0.13, D′ 0.66. Not a proxy (pmid-31484785#q99). For row 53.

## Reading 2026-11-11, supplement

> [q374] [0].transcript_consequences[2] variant_allele A impact MODIFIER gene_symbol EPHX2 distance 3579 strand 1 biotype protein_coding hgnc_id HGNC:3402 gene_id ENSG00000120915 transcript_id ENST00000518328 gene_symbol_source HGNC

Ensembl VEP for rs11780471 (`vep-rs11780471.json`): upstream of EPHX2 (about 3.6 kb, every EPHX2 transcript), no
transcript holding it. For row 53.

## Reading 2026-11-12, record

> [q375] populations[75] frequency 0.521868787276342 allele_count 525 allele G population 1000GENOMES:phase_3:EUR

`var-rs11783562.json` (Ensembl's REST, GRCh38): G 0.52 in 1000 Genomes Europeans. For row 54.

> [q376] mappings[0] seq_region_name 8 allele_string T/A/G coord_system chromosome assembly_name GRCh38 ancestral_allele T location 8:30981030-30981030 end 30981030 start 30981030 strand 1

The site is triallelic in dbSNP (T/A/G), T ancestral; the studies here test T against G. G is the derived allele.
For row 54.

> [q377] populations[73] allele G allele_count 688 frequency 0.682539682539683 population 1000GENOMES:phase_3:EAS

G 0.68 in East Asians (0.04 in Africans). For row 54.

> [q378] . start 30994702 end 31033715 assembly_name GRCh38 version 13 db_type core biotype protein_coding seq_region_name 8 canonical_transcript ENST00000523392.2 strand -1 logic_name ensembl_havana_gene_homo_sapiens source ensembl_havana species homo_sapiens object_type Gene id ENSG00000172733 display_name PURG description purine rich element binding protein G [Source:HGNC Symbol;Acc:HGNC:17930]

`lookup-ENSG00000172733.json`: ENSG00000172733 is PURG (8:30,994,702-31,033,715, GRCh38, minus strand), 14 kb from the lead. For row 54.

## Reading 2026-11-12, supplement

`rs35262860` (variation, populations), `ld-rs35262860-ceu.json` (1000 Genomes CEU, r² ≥ 0.6 within 500 kb) and
`var-rs13279568.json`. For row 55.

> [q379] mappings[0] start 54566350 location 8:54566350-54566351 ancestral_allele CT strand 1 coord_system chromosome end 54566351 seq_region_name 8 allele_string CT/CTCT assembly_name GRCh38

rs35262860 is an insertion of CT, CT/CTCT at GRCh38 8:54,566,350 (Deelen's GCT/G at GRCh37 8:55,478,909, FinnGen's
G/GCT at 54,566,349, the same insertion left-aligned differently); ancestral CT, so the insertion is derived. For
row 55.

> [q380] populations[74] allele_count 379 population 1000GENOMES:phase_3:EUR frequency 0.376739562624254 allele CTCT

The insertion is 0.38 in 1000 Genomes Europeans (Deelen 0.39). For row 55.

> [q381] populations[70] allele CTCT frequency 0.0208333333333333 population 1000GENOMES:phase_3:EAS allele_count 21

0.02 in East Asians. For row 55.

> [q382] [16] r2 1.000000 variation1 rs35262860 d_prime 1.000000 population_name 1000GENOMES:phase_3:CEU variation2 rs13279568

rs13279568 is in perfect LD with the insertion in CEU (r² 1.0, D′ 1.0), as are rs13281601, rs7836982, rs4481575 and
rs13281365. For row 55.

> [q383] mappings[0] end 54566168 strand 1 start 54566168 assembly_name GRCh38 ancestral_allele G location 8:54566168-54566168 allele_string G/A coord_system chromosome seq_region_name 8

rs13279568 at GRCh38 8:54,566,168, G/A: Open Targets' key 8_54566168_G_A. For row 55.

> [q384] populations[12] allele CTCT population gnomADg:nfe frequency 0.3937 allele_count 26740

0.39 in gnomAD's non-Finnish Europeans. For row 55.

> [q385] . var_class indel ambiguity null minor_allele CTCT most_severe_consequence intron_variant MAF 0.20938 name rs35262860 source Variants (including SNPs and indels) imported from dbSNP

An intron variant (Ensembl's most severe consequence), the insertion the minor allele worldwide (0.21). For row 55.

`vep-rs35262860.json`: the insertion's consequences.

> [q386] [0].transcript_consequences[3] biotype protein_coding strand 1 impact MODIFIER transcript_id ENST00000636932 gene_symbol_source HGNC gene_id ENSG00000104237 hgnc_id HGNC:10263 variant_allele CT gene_symbol RP1

> [q387] [0].transcript_consequences[3].consequence_terms[0] intron_variant

An intron variant of RP1 (ENSG00000104237) on its protein-coding transcript ENST00000636932. For row 55.

## Reading 2026-11-12, record

> [q388] mappings[0] start 58925574 end 58925574 seq_region_name 8 allele_string A/G strand 1 location 8:58925574-58925574 coord_system chromosome ancestral_allele A assembly_name GRCh38

> [q389] populations[67] frequency 0.0467196819085487 population 1000GENOMES:phase_3:EUR allele_count 47 allele G

> [q390] populations[64] allele_count 1008 allele A frequency 1 population 1000GENOMES:phase_3:EAS

> [q391] populations[8] population gnomADg:nfe frequency 0.03641 allele G allele_count 2477

`var-rs13262617.json`: GRCh38 8:58,925,574, A/G, A ancestral, so G (the longer-lived allele) is derived. G 0.047 in
1000 Genomes Europeans, 0.036 in gnomAD's non-Finnish Europeans; absent in East Asians (A 1.0). For row 56.

> [q392] [13] r2 0.706884 variation1 rs13262617 d_prime 1.000000 population_name 1000GENOMES:phase_3:CEU variation2 rs79725344

> [q393] [51] population_name 1000GENOMES:phase_3:CEU d_prime 0.999999 variation2 rs13252116 r2 0.568062 variation1 rs13262617

> [q394] [9] variation2 rs7815098 d_prime 0.999999 population_name 1000GENOMES:phase_3:CEU variation1 rs13262617 r2 0.390206

`ld-rs13262617-ceu.json` (CEU, r² ≥ 0.3, 500 kb): the best tags reach r² 0.71 (rs79725344, rs10504278); rs13252116
0.57, rs7815098 0.39. No proxy above 0.8. For row 56.

> [q395] [0].transcript_consequences[0] gene_symbol_source HGNC strand -1 gene_id ENSG00000198846 transcript_id ENST00000361421 variant_allele G biotype protein_coding gene_symbol TOX impact MODIFIER hgnc_id HGNC:18988

> [q396] [0].transcript_consequences[0].consequence_terms[0] intron_variant

`vep-rs13262617.json`: an intron variant of TOX (ENSG00000198846), on the first listed transcript, ENST00000361421. For row
56.

> [q397] populations[78] allele_count 91 allele T frequency 0.0904572564612326 population 1000GENOMES:phase_3:EUR

> [q398] populations[67] frequency 0.0596421471172962 allele A population 1000GENOMES:phase_3:EUR allele_count 60

`var-rs7815098.json` and `var-rs13252116.json`, the two Wright 2019 fathers' tags of row 56's lead: rs7815098's minor T
0.090 in 1000 Genomes Europeans (C/A/T, C ancestral, GRCh38 8:58,927,549); rs13252116's minor A 0.060 (G/A, GRCh38
8:58,901,250). For row 56.


## Reading 2026-11-12, record

> [q399] mappings[0] strand 1 coord_system chromosome allele_string G/A/T location 9:38322519-38322519 end 38322519 start 38322519 assembly_name GRCh38 seq_region_name 9 ancestral_allele G

> [q400] populations[78] frequency 0.0606361829025845 allele T population 1000GENOMES:phase_3:EUR allele_count 61

> [q401] populations[23] frequency 0.05653 population gnomADg:nfe allele T allele_count 3844

> [q402] populations[19] population gnomADg:asj allele T frequency 0.04383 allele_count 152

> [q403] populations[74] population 1000GENOMES:phase_3:EAS allele T frequency 0.0932539682539683 allele_count 94

`var-rs10973748.json`: GRCh38 9:38,322,519, G/A/T, G ancestral, so T is derived. T 0.061 in 1000 Genomes Europeans,
0.057 in gnomAD non-Finnish Europeans, 0.044 in Ashkenazi Jews, 0.093 in East Asians. For row 58.

> [q404] [6] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation2 rs341466 r2 1.000000 variation1 rs10973748

> [q405] [4] variation1 rs10973748 r2 1.000000 variation2 rs341467 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000

> [q406] [7] variation2 rs10973750 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation1 rs10973748 r2 1.000000

`ld-rs10973748-ceu.json` (CEU, r² ≥ 0.3, 500 kb): nine tags, rs341466, rs341467, rs10973750 and rs10973749 at r²
1.0, rs12378970, rs10814677 and rs76830434 at 0.91, rs10973754 at 0.84, rs564198251 at 0.35. Wright 2019's nearby
nominal lines (rs4388534 at GRCh37 9:38,252,526, rs4878777 at 9:38,282,692; pmid-31484785 S Table 8) are not
among them, so not tags of the lead. For row 58.

> [q407] [0].intergenic_consequences[1] impact MODIFIER variant_allele T

`vep-rs10973748.json`: T is an intergenic variant (Open Targets: upstream of a gene). For row 58.

> [q408] populations[16] frequency 0.06362 allele C population gnomADg:nfe allele_count 4327

> [q409] populations[17] population gnomADg:nfe frequency 0.06339 allele_count 4311 allele A

> [q410] populations[18] allele G population gnomADg:nfe allele_count 3921 frequency 0.05764

`var-rs341466.json`, `var-rs341467.json`, `var-rs10973750.json`, the lead's CEU r² 1.0 tags (q404 to q406): in gnomAD
non-Finnish Europeans rs341466's C 0.064, rs341467's A 0.063, rs10973750's G 0.058 (1000 Genomes EUR 0.069, 0.069,
0.060), the alleles NECS codes (pmid-33948810#q24 to q26). For row 58.

## Reading 2026-11-12, supplement

> [q411] mappings[0] strand 1 assembly_name GRCh38 location 9:133266456-133266456 coord_system chromosome seq_region_name 9 allele_string T/C start 133266456 end 133266456 ancestral_allele C

rs2519093 on GRCh38 9:133,266,456, alleles T/C (T the reference), ancestral C: the lifespan-raising C is the ancestral,
common allele, T the derived. For row 59.

> [q412] populations[74] frequency 0.184890656063618 allele_count 186 population 1000GENOMES:phase_3:EUR allele T

> [q413] populations[75] allele C frequency 0.815109343936382 allele_count 820 population 1000GENOMES:phase_3:EUR

1000 Genomes Europeans: T 0.185, C 0.815. For row 59.

> [q414] populations[19] allele T population gnomADg:nfe allele_count 13281 frequency 0.1955

gnomAD non-Finnish Europeans: T 0.196. For row 59.

> [q415] populations[70] allele T population 1000GENOMES:phase_3:EAS allele_count 192 frequency 0.19047619047619

1000 Genomes East Asians: T 0.19, as in Europeans; untested there. For row 59.

> [q416] [29] population_name 1000GENOMES:phase_3:CEU d_prime 0.968500 variation1 rs2519093 variation2 rs651007 r2 0.937992

CEU r² 0.94 (D′ 0.97) to rs651007, Timmers' Figure 4 proxy. For row 59.

> [q417] [55] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 r2 1.000000 variation2 rs532436 variation1 rs2519093

CEU r² 1.0 to rs532436. Nine SNPs reach r² ≥ 0.8 (rs532436, rs600038, rs8176643, rs635634, rs115478735, rs651007,
rs649129, rs579459, rs495828), none in Wright 2019's tables. For row 59.

> [q418] [0].transcript_consequences[0] gene_symbol ABO variant_allele C hgnc_id HGNC:79 transcript_id ENST00000453660 gene_symbol_source HGNC gene_id ENSG00000175164 biotype protein_coding_CDS_not_defined strand -1 impact MODIFIER

VEP: an intron variant of ABO, no coding consequence. For row 59.

> [q419] [0] d_prime 0.999984 population_name 1000GENOMES:phase_3:CEU variation2 rs514659 r2 0.424208 variation1 rs2519093

CEU r² 0.42 (D′ 1.0) to Fortney's rs514659. For row 59.

## Reading 2026-11-12, supplement

> [q420] mappings[0] allele_string G/A coord_system chromosome seq_region_name 9 start 135376756 strand 1 end 135376756 location 9:135376756-135376756 ancestral_allele A assembly_name GRCh38

`var-rs75824829.json` (GRCh38): 9:135,376,756 G/A, A ancestral, so G is derived and A, the minor allele here, is the ancestral one. For row 60.

> [q421] populations[10] population gnomADg:nfe allele A allele_count 2855 frequency 0.04199

A 0.042 in gnomAD's non-Finnish Europeans. For row 60.

> [q422] populations[67] population 1000GENOMES:phase_3:EUR frequency 0.0337972166998012 allele A allele_count 34

A 0.034 in 1000 Genomes Europeans. For row 60.

> [q423] populations[17] population gnomADg:fin allele A allele_count 150 frequency 0.01413

A 0.014 in Finns, which lowers FinnGen's power. For row 60.

> [q424] populations[93] frequency 0.0521472392638037 allele A allele_count 51 population 1000GENOMES:phase_3:SAS

A 0.052 in South Asians; 0.0014 in gnomAD's East Asians and 0.0075 in its Africans (the file's lines). For row 60.

> [q425] [0] variation2 rs113450114 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation1 rs75824829 r2 0.489690

`ld-rs75824829-ceu.json`: the best proxy in 1000 Genomes CEU is rs113450114, r² 0.49 (D′ 1); next rs4841974, r² 0.41. No proxy reaches r² 0.5 in CEU. For row 60.

> [q426] [0] most_severe_consequence upstream_gene_variant id rs75824829 strand 1 allele_string G/A assembly_name GRCh38 input rs75824829 start 135376756 end 135376756 seq_region_name 9

VEP: no coding consequence. For row 60.

## Reading 2026-11-12, supplement

> [q427] [0].transcript_consequences[0] biotype lncRNA distance 1876 impact MODIFIER strand 1 transcript_id ENST00000741315 variant_allele A gene_id ENSG00000296725

VEP's nearest transcript: the lncRNA ENSG00000296725, 1.876 kb away (downstream, q426's other lines the same gene). For row 60.

> [q428] populations[2] population gnomADg:eas allele A allele_count 7 frequency 0.001355

A 0.0014 in gnomAD's East Asians: near absent. For row 60.

## Reading 2026-11-12, supplement

> [q429] mappings[0] start 11118452 location 10:11118452-11118452 allele_string C/T end 11118452 coord_system chromosome strand 1 ancestral_allele C assembly_name GRCh38 seq_region_name 10

rs547541271: GRCh38 10:11,118,452, C/T, C ancestral. For row 61.

> [q430] populations[17] allele_count 200 population gnomADg:nfe allele T frequency 0.002942

T in gnomAD's non-Finnish Europeans: 0.0029 (200 copies).

> [q431] populations[12] allele_count 2 frequency 0.0001886 allele T population gnomADg:fin

In Finns 0.00019 (2 copies).

> [q432] populations[57] allele_count 1006 frequency 1 population 1000GENOMES:phase_3:EUR allele C

1000 Genomes' Europeans carry no T (C at frequency 1), so Ensembl's CEU LD window has nothing to return (`ld-rs547541271-ceu.json` rendered to no text): no tag is known.

> [q433] populations[2] frequency 1 population gnomADg:eas allele C allele_count 5182

gnomAD's East Asians: C at frequency 1, T unseen.

> [q434] populations[9] population gnomADg:sas allele T frequency 0.001663 allele_count 8

South Asians: T 0.0017.

> [q435] [0] most_severe_consequence intron_variant input rs547541271 start 11118452 allele_string C/T assembly_name GRCh38 end 11118452 seq_region_name 10 id rs547541271 strand 1

> [q436] [0].transcript_consequences[0] impact MODIFIER variant_allele T strand 1 gene_symbol CELF2 biotype protein_coding gene_symbol_source HGNC gene_id ENSG00000048740 transcript_id ENST00000416382 hgnc_id HGNC:2550

VEP: an intron variant of CELF2 (ENSG00000048740), modifier.

> [q437] mappings[0] coord_system chromosome assembly_name GRCh37 seq_region_name 10 ancestral_allele C end 11160415 allele_string C/T strand 1 start 11160415 location 10:11160415-11160415

GRCh37 10:11,160,415, the position Park's deposits print.

> [q438] mappings[0] location 2:37484580-37484580 assembly_name GRCh37 start 37484580 coord_system chromosome seq_region_name 2 allele_string G/A end 37484580 strand 1 ancestral_allele G

rs577106756 at GRCh37 2:37,484,580 (from Ensembl's GRCh37 server, `grch37-var-rs577106756.json`), the position Park's deposits print. For row 13.

## Reading 2026-11-12, supplement

> [q439] mappings[0] end 90207407 ancestral_allele T assembly_name GRCh38 seq_region_name 10 strand 1 start 90207407 location 10:90207407-90207407 coord_system chromosome allele_string T/A/G

rs11186068 at GRCh38 10:90,207,407, T/A/G, T ancestral, so G derived; the position Beccacece's tables print. For row 62.

> [q440] populations[12] allele G allele_count 623 population gnomADg:nfe frequency 0.009167

G 0.92 % in gnomAD's non-Finnish Europeans ...

> [q441] populations[16] allele_count 52 allele G frequency 0.004898 population gnomADg:fin

... 0.49 % in its Finns ...

> [q442] populations[74] frequency 0.0119284294234592 population 1000GENOMES:phase_3:EUR allele G allele_count 12

... 1.2 % in 1000 Genomes' Europeans (12 copies) ...

> [q443] populations[106] allele_count 2 allele G frequency 0.00934579439252336 population 1000GENOMES:phase_3:TSI

... and 0.9 % (2 copies) in its Tuscans; Beccacece's discovery sample carries it at 3.3 %, cases and controls together (pmid-42176242#q7). For row 62.

> [q444] populations[20] allele_count 475 allele G population gnomADg:eas frequency 0.09205

G 9.2 % in gnomAD's East Asians ...

> [q445] populations[8] frequency 0.08607 population gnomADg:afr allele G allele_count 3572

... and 8.6 % in its Africans: common outside Europe, untested there. For row 62.

> [q446] mappings[0] coord_system chromosome allele_string T/A/G seq_region_name 10 strand 1 end 91967164 location 10:91967164-91967164 assembly_name GRCh37 ancestral_allele T start 91967164

GRCh37 10:91,967,164, the position LifeGen, Deelen, Zenin and Park print. For row 62.

> [q447] [0] input rs11186068 assembly_name GRCh38 allele_string T/A/G id rs11186068 most_severe_consequence intron_variant strand 1 seq_region_name 10 end 90207407 start 90207407

VEP: an intron variant ...

> [q448] [0].transcript_consequences[1] gene_symbol_source HGNC impact MODIFIER biotype lncRNA gene_id ENSG00000232229 variant_allele G gene_symbol LINC00865 transcript_id ENST00000664430 hgnc_id HGNC:45170 strand 1

... of LINC00865 (lncRNA), the G allele's consequence on transcript ENST00000664430. For row 62.

## Reading 2026-11-12, supplement

> [q449] mappings[0] start 112995025 end 112995025 location 10:112995025-112995025 allele_string T/C coord_system chromosome strand 1 ancestral_allele C seq_region_name 10 assembly_name GRCh38

rs35198068 at GRCh38 10:112,995,025, T/C; the ancestral allele is C on GRCh38 but T on GRCh37 (q454), so which is derived is not read. For row 63.

> [q450] populations[75] frequency 0.317097415506958 population 1000GENOMES:phase_3:EUR allele C allele_count 319

C 0.317 in 1000 Genomes' Europeans ... For row 63.

> [q451] populations[72] frequency 0.0228174603174603 allele C population 1000GENOMES:phase_3:EAS allele_count 23

... 0.023 in its East Asians ... For row 63.

> [q452] populations[51] frequency 0.305597579425113 population 1000GENOMES:phase_3:AFR allele C allele_count 404

... 0.31 in its Africans ... For row 63.

> [q453] populations[106] allele_count 293 frequency 0.29959100204499 population 1000GENOMES:phase_3:SAS allele C

... and 0.30 in its South Asians. For row 63.

> [q454] mappings[0] ancestral_allele T strand 1 end 114754784 coord_system chromosome allele_string T/C seq_region_name 10 start 114754784 location 10:114754784-114754784 assembly_name GRCh37

GRCh37 10:114,754,784, the position Zenin, LifeGen, Deelen, Park and mvAge print. For row 63.

> [q455] [0] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation1 rs35198068 r2 0.976689 variation2 rs34872471

rs35198068 and rs34872471 (Zenin's Table 2 SNP) in CEU: r² 0.977, D′ 1. For row 63.

> [q456] [0] population_name 1000GENOMES:phase_3:CEU variation2 rs7903146 variation1 rs35198068 d_prime 1.000000 r2 1.000000

rs35198068 and rs7903146 (the best-known TCF7L2 diabetes variant) in CEU: r² 1.00, D′ 1. For row 63.

> [q457] [0].transcript_consequences[0] hgnc_id HGNC:11641 impact MODIFIER transcript_id ENST00000277945 biotype protein_coding variant_allele C gene_id ENSG00000148737 strand 1 gene_symbol_source HGNC gene_symbol TCF7L2

VEP: an intron variant of TCF7L2 (ENST00000277945). For row 63.

## Reading 2026-11-12, supplement

> [q458] mappings[0] location 11:202785-202785 ancestral_allele C assembly_name GRCh38 strand 1 start 202785 end 202785 allele_string T/C coord_system chromosome seq_region_name 11

rs76612380 at GRCh38 11:202,785, T/C; C ancestral, so T, the common allele, is derived. Ensembl holds no 1000 Genomes
genotypes for it (only gnomAD, ALFA and GEM-J frequencies), so its pairwise LD queries return nothing, in CEU, CHB and
JPT alike (`ld-rs76612380-rs2280543-*`, `ld-rs76612380-rs79902640-CEU`): LD unknown, not absent. For row 64.

> [q459] mappings[0] strand 1 seq_region_name 11 allele_string T/C coord_system chromosome ancestral_allele C start 202785 assembly_name GRCh37 end 202785 location 11:202785-202785

The same position on GRCh37, the one BBJ (pmid-36737517#q9), Deelen, Park and LifeGen print. For row 64.

> [q460] populations[16] population gnomADg:eas frequency 0.08978 allele_count 413 allele C

C 0.090 in gnomAD's East Asians ... For row 64.

> [q461] populations[23] population gnomADg:nfe allele_count 1273 allele C frequency 0.01935

... 0.019 in its non-Finnish Europeans ... For row 64.

> [q462] populations[28] population gnomADg:fin allele_count 85 allele C frequency 0.008192

... 0.008 in its Finns ... For row 64.

> [q463] populations[19] population gnomADg:afr frequency 0.02439 allele C allele_count 947

... and 0.024 in its Africans. For row 64.

> [q464] [0].transcript_consequences[1] strand -1 impact MODIFIER variant_allele C gene_id ENSG00000177951 hgnc_id HGNC:19348 distance 139 gene_symbol BET1L gene_symbol_source HGNC biotype protein_coding transcript_id ENST00000325147

VEP: 139 bp downstream of BET1L (ENST00000325147); also downstream of CIMAP1A and upstream of RIC8A. For row 64.

> [q465] mappings[0] coord_system chromosome allele_string C/T location 11:203788-203788 start 203788 strand 1 seq_region_name 11 end 203788 ancestral_allele C assembly_name GRCh38

rs2280543, BBJ's genotyped proxy (pmid-36737517#q14), at GRCh38 11:203,788, C/T, 1 kb from the lead. For row 64.

> [q466] populations[104] allele T allele_count 20 frequency 0.0961538461538462 population 1000GENOMES:phase_3:JPT

rs2280543's T 0.096 in 1000 Genomes' Japanese: the minor allele, as the lead's C is. For row 64.

> [q467] populations[91] allele T allele_count 33 frequency 0.0328031809145129 population 1000GENOMES:phase_3:EUR

rs2280543's T 0.033 in 1000 Genomes' Europeans ... For row 64.

> [q468] populations[34] frequency 0.03826 population gnomADg:nfe allele_count 2603 allele T

... and 0.038 in gnomAD's non-Finnish Europeans, twice the lead's C (q461): in Europeans the proxy's r² with the lead
can be at most about 0.50 (derived from the two frequencies; at most 0.62 from FinnGen's, db-finngen-r11#q40, q42).
For row 64.

> [q469] [0] population_name 1000GENOMES:phase_3:CEU variation2 rs79902640 r2 1.000000 variation1 rs2280543 d_prime 1.000000

rs2280543 and rs79902640 (the BET1L eQTL's top variant, pmid-36737517) are one haplotype in CEU: r² 1.00. For row 64.

> [q470] [0] r2 1.000000 variation2 rs79902640 variation1 rs2280543 population_name 1000GENOMES:phase_3:JPT d_prime 1.000000

... and in JPT. For row 64.

> [q471] populations[49] allele_count 31 population 1000GENOMES:phase_3:EUR allele G frequency 0.0308151093439364

rs79902640's G 0.031 in Europeans, rs2280543's T's partner. For row 64.

## Reading 2026-11-12, supplement

> [q472] mappings[0] ancestral_allele G location 11:43770315-43770315 end 43770315 strand 1 seq_region_name 11 start 43770315 allele_string G/A coord_system chromosome assembly_name GRCh38

> [q473] mappings[0] seq_region_name 11 start 43791865 location 11:43791865-43791865 assembly_name GRCh37 allele_string G/A coord_system chromosome strand 1 end 43791865 ancestral_allele G

rs4755737 (`var-rs4755737`, `grch37-var-rs4755737`): G/A at 11:43,770,315 (GRCh38) and 11:43,791,865 (GRCh37); G
ancestral, A derived. For row 65.

> [q474] populations[19] population gnomADg:nfe frequency 0.4581 allele_count 31138 allele A

> [q475] populations[1] population gnomADg:eas frequency 0.3164 allele_count 1639 allele G

A at 0.46 in gnomAD's non-Finnish Europeans; G at 0.32 in its East Asians, so A 0.68 there (derived). For row 65.

> [q476] [0] variation1 rs4755737 r2 0.533305 variation2 rs4755202 population_name 1000GENOMES:phase_3:CEU d_prime 0.753007

`ld-rs4755737-rs4755202-CEU`: the seed's two rsIDs at r² 0.53, D′ 0.75 in CEU. The phase is not printed; both A
alleles are the age GWAS's older side (pmid-31484785#q107, q109). For row 65.

> [q477] [0].transcript_consequences[0] gene_symbol HSD17B12 gene_symbol_source HGNC strand 1 gene_id ENSG00000149084 variant_allele A biotype protein_coding transcript_id ENST00000278353 impact MODIFIER hgnc_id HGNC:18646

`vep-rs4755737`: intronic in HSD17B12 (most severe consequence intron variant). For row 65.

> [q478] mappings[0] end 43598388 seq_region_name 11 allele_string G/A/C/T start 43598388 strand 1 location 11:43598388-43598388 coord_system chromosome ancestral_allele G assembly_name GRCh38

rs4755202 at 11:43,598,388 (GRCh38), G/A/C/T with G ancestral; A is the allele every file here prints. For row 65.

> [q479] [0] d_prime 1.000000 r2 0.497652 population_name 1000GENOMES:phase_3:TSI variation2 rs74904474 variation1 rs11186068

`ld-rs11186068-rs74904474-TSI.json`: rs74904474 to the lead in 1000 Genomes Tuscans, r² 0.50, D′ 1; outside
Beccacece's r² ≥ 0.6 proxy list and Ensembl's CEU window at 0.6. At D′ 1 an r² that high requires the two minor
alleles on one haplotype, so rs74904474's A rides on the lead's G (derived). For row 62, prose.

## Reading 2026-11-12, supplement

> [q480] mappings[0] start 89284793 coord_system chromosome strand 1 end 89284793 location 11:89284793-89284793 allele_string G/A ancestral_allele G seq_region_name 11 assembly_name GRCh38

> [q481] mappings[0] coord_system chromosome end 89017961 strand 1 allele_string G/A assembly_name GRCh37 ancestral_allele G seq_region_name 11 start 89017961 location 11:89017961-89017961

`var-rs1126809`: G/A at GRCh38 11:89,284,793 (GRCh37 89,017,961), G ancestral. For row 66.

> [q482] populations[37] frequency 0.2791 allele A population gnomADg:nfe allele_count 18915

> [q483] populations[32] allele_count 1675 population gnomADg:fin allele A frequency 0.1587

> [q484] populations[93] allele A population 1000GENOMES:phase_3:EUR frequency 0.252485089463221 allele_count 254

> [q485] populations[91] frequency 0.999007936507937 allele G population 1000GENOMES:phase_3:EAS allele_count 1007

> [q486] populations[74] allele A population 1000GENOMES:phase_3:AFR frequency 0.00907715582450832 allele_count 12

> [q487] populations[121] frequency 0.0541922290388548 allele A population 1000GENOMES:phase_3:SAS allele_count 53

> [q488] populations[77] allele_count 87 allele A population 1000GENOMES:phase_3:AMR frequency 0.12536023054755

A, the derived allele: 0.28 in gnomAD's non-Finnish Europeans, 0.16 in Finns, 0.25 in 1000 Genomes Europeans, 0.13
in admixed Americans, 0.05 in South Asians, 0.01 in Africans; G 0.999 in East Asians. For row 66.

> [q489] [0].transcript_consequences[0] variant_allele A polyphen_prediction probably_damaging protein_end 402 biotype protein_coding cds_start 1205 cdna_start 1284 cdna_end 1284 impact MODERATE gene_symbol TYR polyphen_score 0.994 transcript_id ENST00000263321 hgnc_id HGNC:12442 strand 1 sift_score 0.01 gene_id ENSG00000077498 codons cGa/cAa cds_end 1205 sift_prediction deleterious amino_acids R/Q protein_start 402 gene_symbol_source HGNC

`vep-rs1126809`: A is a missense change in TYR (ENST00000263321), codon cGa/cAa, R402Q, PolyPhen probably damaging,
SIFT deleterious. For row 66.

> [q490] [0] variation1 rs1126809 variation2 rs574028 r2 0.346719 d_prime 0.953414 population_name 1000GENOMES:phase_3:CEU

> [q491] [0] population_name 1000GENOMES:phase_3:CEU d_prime 0.903105 variation2 rs4121744 r2 0.275540 variation1 rs1126809

> [q492] [0] population_name 1000GENOMES:phase_3:CEU r2 0.245226 variation1 rs1126809 variation2 rs10830204 d_prime 0.896152

The three AncestryDNA fathers' SNPs in Wright 2019's Supplemental Table 8 within 0.25 Mb of the lead (rs574028, 84
kb; rs4121744, 143 kb; rs10830204, 230 kb) tag it weakly in CEU: r² 0.35, 0.28, 0.25. Named, not scored. For row 66.

## Reading 2026-11-12, supplement

> [q493] mappings[0] allele_string G/A assembly_name GRCh38 coord_system chromosome location 11:119399248-119399248 end 119399248 ancestral_allele G start 119399248 seq_region_name 11 strand 1

> [q494] mappings[0] strand 1 coord_system chromosome allele_string G/A seq_region_name 11 assembly_name GRCh37 ancestral_allele null start 119269958 location 11:119269958-119269958 end 119269958

> [q495] populations[15] population gnomADg:nfe allele_count 262 frequency 0.003853 allele A

> [q496] populations[5] population gnomADg:eas allele_count 5192 frequency 1 allele G

rs139137459: GRCh38 11:119,399,248 G/A (GRCh37 119,269,958), G ancestral; A at 0.0039 in gnomAD genomes' non-Finnish
Europeans and absent from its East Asians (G 1, q496); 0.0018 in Finns. For row 68.

> [q497] populations[24] population gnomADg:nfe allele_count 554 allele G frequency 0.008146

> [q498] mappings[0] location 11:119419222-119419222 ancestral_allele A assembly_name GRCh38 strand 1 start 119419222 end 119419222 allele_string A/G seq_region_name 11 coord_system chromosome

> [q499] [0].transcript_consequences[0] biotype lncRNA gene_symbol_source HGNC impact MODIFIER gene_symbol USP2-AS1 transcript_id ENST00000498979 strand 1 hgnc_id HGNC:48673 variant_allele A gene_id ENSG00000245248

> [q500] populations[44] allele A population 1000GENOMES:phase_3:CEU frequency 0.0101010101010101 allele_count 2

> [q501] [0] variation1 rs139137459 variation2 rs151091095 r2 0.663265 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000

> [q502] [0] population_name 1000GENOMES:phase_3:GBR r2 1.000000 variation2 rs151091095 variation1 rs139137459 d_prime 1.000000

rs151091095, Timmers 2019's tag for the locus (pmid-30642433#q286): GRCh38 11:119,419,222 A/G, A ancestral, G 0.0081
in non-Finnish Europeans (q497). VEP puts rs139137459 in an intron of the lncRNA USP2-AS1 (q499). In 1000 Genomes'
CEU (A 0.010, two copies, q500) the pair's r² is 0.66, D′ 1; in GBR r² 1, D′ 1 (two copies of each): the rare
alleles ride together where they are seen, but on so few copies the European r² is fixed only by the frequencies'
bound, about 0.47. For row 68.

## Reading 2026-11-12, supplement

> [q503] mappings[0] allele_string A/T coord_system chromosome start 49569751 location 12:49569751-49569751 strand 1 ancestral_allele A assembly_name GRCh38 end 49569751 seq_region_name 12

> [q504] mappings[0] seq_region_name 12 ancestral_allele A assembly_name GRCh37 allele_string A/T strand 1 end 49963534 coord_system chromosome location 12:49963534-49963534 start 49963534

> [q505] populations[6] frequency 0.09258 population gnomADg:nfe allele_count 6043 allele T

> [q506] populations[13] allele_count 374 allele T population gnomADg:eas frequency 0.07351

> [q507] populations[3] allele T allele_count 953 frequency 0.09699 population gnomADg:fin

> [q508] [0] most_severe_consequence intron_variant start 49569751 allele_string A/T end 49569751 id rs55686423 strand 1 input rs55686423 assembly_name GRCh38 seq_region_name 12

rs55686423: GRCh38 12:49,569,751 A/T (GRCh37 49,963,534), A ancestral; T at 0.093 in gnomAD genomes' non-Finnish
Europeans (q505), 0.074 in East Asians (q506), 0.097 in Finns (q507); VEP's most severe consequence intronic (q508),
in PRPF40B and 1.6 kb from MCRS1. A/A about 82 in 100 Europeans, A/T 17, T/T 1 (derived). For row 69.

> [q509] mappings[0] seq_region_name 12 location 12:49591427-49591427 coord_system chromosome end 49591427 start 49591427 assembly_name GRCh38 allele_string G/A ancestral_allele A strand 1

> [q510] populations[15] allele_count 7511 population gnomADg:nfe allele A frequency 0.1105

> [q511] [0] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation2 rs11169081 variation1 rs55686423 r2 0.879121

> [q512] [0] d_prime 1.000000 population_name 1000GENOMES:phase_3:GBR r2 0.826886 variation2 rs11169081 variation1 rs55686423

> [q513] [0] d_prime 0.999999 variation2 rs7965658 r2 0.553324 variation1 rs55686423 population_name 1000GENOMES:phase_3:GBR

> [q514] [0] r2 0.200257 variation2 rs11169063 variation1 rs55686423 d_prime 0.662660 population_name 1000GENOMES:phase_3:CEU

> [q515] [0] d_prime 0.532366 population_name 1000GENOMES:phase_3:GBR r2 0.171550 variation1 rs55686423 variation2 rs6580707

rs11169081 (GRCh38 12:49,591,427 G/A, A ancestral; A 0.11 in non-Finnish Europeans, q510), 22 kb from the lead: r²
0.88 in CEU and 0.83 in GBR, D′ 1 (q511, q512), its minor A riding with the lead's minor T. Wright 2019's other
Table 9 lines nearby are weaker tags or none: rs7965658 r² 0.40 (CEU) to 0.55 (GBR, q513), rs11169063 0.20 (q514),
rs6580707 0.06 to 0.17 (q515). For row 69.

## Reading 2026-11-12, supplement

> [q516] [49] d_prime 1.000000 r2 0.824057 variation2 rs7977389 variation1 rs55686423 population_name 1000GENOMES:phase_3:EUR

> [q517] [189] population_name 1000GENOMES:phase_3:EUR d_prime 0.999999 r2 0.758732 variation2 rs17123764 variation1 rs55686423

> [q518] populations[5] allele_count 7487 allele C population gnomADg:nfe frequency 0.1101

> [q519] mappings[0] ancestral_allele C allele_string T/C/G strand 1 assembly_name GRCh38 coord_system chromosome end 49587939 start 49587939 seq_region_name 12 location 12:49587939-49587939

> [q520] populations[12] frequency 0.07636 allele T allele_count 5193 population gnomADg:nfe

Ensembl's LD window around rs55686423 in 1000 Genomes EUR at r² ≥ 0.5 (`ld-window-rs55686423-EUR`, 238 SNPs, about 50
at r² ≥ 0.8): rs7977389 (GRCh38 12:49,587,939, q519) at r² 0.82, D′ 1 (q516), its minor C (0.11 in non-Finnish
Europeans, q518) riding with the lead's minor T; rs17123764 at r² 0.76, D′ 1 (q517), its minor T (0.076, q520) with
the lead's T. Wright 2019's rs7303233, rs2272391 and rs7488270 are not in the window, so below r² 0.5. For row 69.

## Reading 2026-11-12, supplement

> [q521] mappings[0] coord_system chromosome allele_string T/A/G start 95187042 location 12:95187042-95187042 strand 1 seq_region_name 12 ancestral_allele T end 95187042 assembly_name GRCh38

> [q522] mappings[0] allele_string T/A/G seq_region_name 12 coord_system chromosome start 95580818 assembly_name GRCh37 location 12:95580818-95580818 ancestral_allele T strand 1 end 95580818

> [q523] populations[19] allele G allele_count 5064 population gnomADg:nfe frequency 0.07447

> [q524] populations[20] frequency 0.247 population gnomADg:eas allele G allele_count 1280

> [q525] populations[16] allele G allele_count 825 population gnomADg:fin frequency 0.07795

> [q526] . minor_allele G most_severe_consequence intron_variant var_class SNP ambiguity D name rs12830425 source Variants (including SNPs and indels) imported from dbSNP MAF 0.125392

rs12830425: GRCh38 12:95,187,042 (GRCh37 95,580,818), T/G, T ancestral (q521, q522); G at 0.074 in gnomAD genomes'
non-Finnish Europeans (q523), 0.25 in East Asians (q524), 0.078 in Finns (q525); intronic (q526). T/T about 86 in 100
Europeans, G/T 14, G/G 0.6 (derived). For row 70.

> [q527] [68] d_prime 0.963179 r2 0.894899 variation2 rs4762479 variation1 rs12830425 population_name 1000GENOMES:phase_3:EUR

> [q528] [83] d_prime 0.963179 r2 0.894899 variation1 rs12830425 variation2 rs11107896 population_name 1000GENOMES:phase_3:EUR

> [q529] [70] population_name 1000GENOMES:phase_3:EUR d_prime 0.963179 r2 0.894899 variation2 rs141526980 variation1 rs12830425

> [q530] [60] r2 0.894899 d_prime 0.963179 variation2 rs11107908 variation1 rs12830425 population_name 1000GENOMES:phase_3:EUR

> [q531] [90] variation2 rs34150274 variation1 rs12830425 d_prime 1.000000 r2 0.652864 population_name 1000GENOMES:phase_3:EUR

> [q532] [99] variation1 rs12830425 variation2 rs10859847 r2 0.982567 d_prime 1.000000 population_name 1000GENOMES:phase_3:EUR

> [q533] [62] population_name 1000GENOMES:phase_3:EUR variation2 rs11107900 variation1 rs12830425 r2 0.894899 d_prime 0.963179

> [q534] [61] population_name 1000GENOMES:phase_3:EUR r2 0.878523 d_prime 0.945705 variation1 rs12830425 variation2 rs11107904

> [q535] [94] population_name 1000GENOMES:phase_3:EUR variation1 rs12830425 variation2 rs11107928 r2 0.982295 d_prime 1.000000

> [q536] [15] population_name 1000GENOMES:phase_3:EUR d_prime 0.963179 r2 0.894899 variation2 rs11107903 variation1 rs12830425

> [q537] [0] variation1 rs12830425 r2 0.293028 variation2 rs4128507 d_prime 0.999996 population_name 1000GENOMES:phase_3:EUR

> [q538] populations[14] allele_count 4998 frequency 0.07349 population gnomADg:nfe allele C

> [q539] populations[21] allele_count 12330 allele C frequency 0.1813 population gnomADg:nfe

The lead's EUR window (1000 Genomes phase 3, r² ≥ 0.5, 113 SNPs). The leads of the other traits' credible sets that
hold the lead are in it (q527-q533, q536): rs4762479, rs11107896, rs141526980, rs11107908, rs11107900 and rs11107903
at r² 0.89 (D′ 0.96), rs10859847 at 0.98, rs34150274 at 0.65 (D′ 1); each set lead's minor allele, at about 0.07 in
non-Finnish Europeans (db-opentargets-26.09#q849-q856), rides with the lead's minor G. Wright 2019's tag rs11107904
r² 0.88, D′ 0.95 (q534), T/C with C at 0.073 (q538), so C rides with G; mvAge's best SNP in its FGD6 TWAS window,
rs11107928, r² 0.98 (q535); rs4128507 r² 0.29, D′ 1 (q537), C at 0.18 (q539), its C with G. For row 70.

## Reading 2026-11-12, supplement

> [q540] mappings[0] strand 1 seq_region_name 13 start 18865983 ancestral_allele C end 18865983 location 13:18865983-18865983 assembly_name GRCh38 coord_system chromosome allele_string C/A/G

> [q541] mappings[0] strand 1 ancestral_allele null end 19440123 coord_system chromosome seq_region_name 13 allele_string C/A/G location 13:19440123-19440123 assembly_name GRCh37 start 19440123

> [q542] populations[75] population 1000GENOMES:phase_3:EAS allele_count 96 frequency 0.0952380952380952 allele G

> [q543] populations[71] allele_count 21 frequency 0.1 population 1000GENOMES:phase_3:CHS allele G

> [q544] populations[70] allele_count 14 frequency 0.0679611650485437 population 1000GENOMES:phase_3:CHB allele G

> [q545] populations[80] frequency 0.201789264413519 allele_count 203 population 1000GENOMES:phase_3:EUR allele G

> [q546] populations[14] allele G population gnomADg:eas frequency 0.1108 allele_count 573

> [q547] [63] population_name 1000GENOMES:phase_3:EUR r2 0.945387 variation2 rs113946246 variation1 rs2440012 d_prime 0.981303

> [q548] [65] d_prime 1.000000 population_name 1000GENOMES:phase_3:EAS r2 0.988606 variation2 rs113946246 variation1 rs2440012

> [q549] . minor_allele null name rs2440012 MAF null most_severe_consequence intron_variant var_class SNP ambiguity V source Variants (including SNPs and indels) imported from dbSNP

> [q550] [0].transcript_consequences[3] variant_allele G gene_symbol_source HGNC gene_symbol ANKRD20A9P impact MODIFIER strand -1 hgnc_id HGNC:42023 gene_id ENSG00000206192 biotype transcribed_unprocessed_pseudogene transcript_id ENST00000457997

rs2440012: GRCh38 13:18,865,983 (the seed's position), GRCh37 13:19,440,123, C/A/G, C ancestral; intronic in the
pseudogene ANKRD20A9P (q549, q550). G at 0.095 in 1000 Genomes' East Asians (CHS 0.10, CHB 0.068) and 0.20 in
Europeans; gnomAD East Asians 0.11. Its best European tag in LifeGen, rs113946246 (13:19,429,318), is r² 0.945 (D′
0.98) in Europeans and 0.989 (D′ 1) in East Asians (q547, q548); its T at 0.82 (pmid-30642433#q294) against C at 0.80
here, so T rides with C, Zeng's longer-life allele. For row 72.

> [q551] populations[44] allele G frequency 0.09843 allele_count 1155 population ALFA:SAMN10492695

> [q552] populations[32] allele C allele_count 74 frequency 1 population ALFA:SAMN10492704

> [q553] populations[34] population ALFA:SAMN10492697 frequency 1 allele_count 60 allele C

rs2440012 in ALFA (dbSNP's frequencies; the sample labels are not in the cached record): SAMN10492695 has G 0.098 (C
0.90, A 0.0014), the numbers Liu 2021 gives for Europeans (pmid-33657282#q30); SAMN10492704 (74 alleles) and
SAMN10492697 (60) carry C only, and two others (86, 478 alleles) likewise. 1000 Genomes has G at 0.20 in Europeans and
0.095 in East Asians (q545, q542). The reference frequency depends on the source. For row 72.

## Reading 2026-11-12, record

> [q554] mappings[0] seq_region_name 13 allele_string T/A/G end 33054001 start 33054001 coord_system chromosome ancestral_allele T assembly_name GRCh38 location 13:33054001-33054001 strand 1

> [q555] mappings[0] start 33628138 location 13:33628138-33628138 assembly_name GRCh37 allele_string T/A/G seq_region_name 13 coord_system chromosome end 33628138 ancestral_allele T strand 1

> [q556] populations[95] allele G allele_count 195 frequency 0.193836978131213 population 1000GENOMES:phase_3:EUR

> [q557] populations[75] allele G allele_count 265 frequency 0.200453857791225 population 1000GENOMES:phase_3:AFR

> [q558] populations[91] frequency 1 population 1000GENOMES:phase_3:EAS allele_count 1008 allele T

> [q559] populations[18] allele_count 173893 allele G population gnomADe:nfe frequency 0.1565

> [q560] [27] r2 1.000000 variation2 rs9527025 variation1 rs9536314 population_name 1000GENOMES:phase_3:EUR d_prime 1.000000

> [q561] [0].transcript_consequences[1] cds_end 1054 hgnc_id HGNC:6344 variant_allele G transcript_id ENST00000380099 gene_symbol_source HGNC polyphen_score 1 polyphen_prediction probably_damaging codons Ttt/Gtt biotype protein_coding gene_symbol KL protein_end 352 cds_start 1054 cdna_end 1072 cdna_start 1072 amino_acids F/V gene_id ENSG00000133116 sift_score 0.02 sift_prediction deleterious protein_start 352 impact MODERATE strand 1

rs9536314 (row 73, KL-VS): GRCh38 13:33,054,001 (q554), GRCh37 13:33,628,138 (q555), T/A/G, T ancestral. G, the V352
allele of KL-VS, is 0.19 in 1000 Genomes Europeans (q556), 0.20 in Africans (q557), absent in East Asians (T at 1.0,
q558), 0.157 in gnomAD exomes' non-Finnish Europeans (q559). rs9527025 (C370S, KL-VS's other coding change) is in
complete LD with it in Europeans, r² 1.0, D′ 1.0 (q560), with ten other SNPs at r² 1.0 in the window. VEP: G is
Ttt/Gtt, a missense change at residue 352 of KL's canonical transcript ENST00000380099, PolyPhen probably damaging
(q561; its F/I line is the A allele). For row 73.

## Reading 2026-11-12, record

> [q562] mappings[0] seq_region_name 13 assembly_name GRCh38 ancestral_allele T coord_system chromosome strand 1 end 64262356 location 13:64262356-64262356 allele_string T/C start 64262356

> [q563] mappings[0] coord_system chromosome assembly_name GRCh37 ancestral_allele T seq_region_name 13 end 64836488 allele_string T/C strand 1 start 64836488 location 13:64836488-64836488

> [q564] populations[75] frequency 0.062624254473161 allele C population 1000GENOMES:phase_3:EUR allele_count 63

> [q565] populations[13] frequency 0.06415 allele C population gnomADg:nfe allele_count 4363

> [q566] [0] d_prime 1.000000 variation2 rs12586026 variation1 rs61949650 r2 1.000000 population_name 1000GENOMES:phase_3:CEU

> [q567] populations[76] frequency 0.0656063618290258 allele C allele_count 66 population 1000GENOMES:phase_3:EUR

> [q568] [0] start 64262356 end 64262356 seq_region_name 13 input rs61949650 allele_string T/C id rs61949650 strand 1 most_severe_consequence intergenic_variant assembly_name GRCh38

> [q569] populations[52] allele C population 1000GENOMES:phase_3:AFR frequency 0.118003025718608 allele_count 156

rs61949650 (row 74): GRCh38 13:64,262,356 (q562), GRCh37 13:64,836,488 (q563), T/C, T ancestral. C is 0.063 in 1000
Genomes Europeans (q564), 0.064 in gnomAD genomes' non-Finnish Europeans (q565), 0.12 in Africans (q569); 0.047 in
East Asians, 0.066 in South Asians. rs12586026, Wright's mothers' SNP 3.9 kb away, is in complete LD with it in CEU,
r² 1.0, D′ 1.0 (q566), its C at 0.066 in Europeans (q567), so C rides with C. VEP: intergenic (q568). The EUR window
at r² ≥ 0.5 holds 538 pairs. For row 74.

## Reading 2026-11-12, record

> [q570] mappings[0] assembly_name GRCh38 ancestral_allele TTTTTTTTTTTTT allele_string TTTTTTTTTTTTT/TTTTTTTTTTT/TTTTTTTTTTTT/TTTTTTTTTTTTTT/TTTTTTTTTTTTTTT/TTTTTTTTTTTTTTTT/TTTTTTTTTTTTTTTTT strand 1 seq_region_name 13 location 13:73649404-73649416 end 73649416 coord_system chromosome start 73649404

> [q571] mappings[0] end 74223553 ancestral_allele TTTTTTTTTTTTT strand 1 start 74223541 assembly_name GRCh37 location 13:74223541-74223553 allele_string TTTTTTTTTTTTT/TTTTTTTTTTT/TTTTTTTTTTTT/TTTTTTTTTTTTTT/TTTTTTTTTTTTTTT/TTTTTTTTTTTTTTTT/TTTTTTTTTTTTTTTTT seq_region_name 13 coord_system chromosome

> [q572] mappings[0] end 73757854 strand 1 start 73757854 assembly_name GRCh38 location 13:73757854-73757854 ancestral_allele G allele_string G/T seq_region_name 13 coord_system chromosome

> [q573] mappings[0] ancestral_allele G strand 1 end 74331991 coord_system chromosome assembly_name GRCh37 allele_string G/T location 13:74331991-74331991 start 74331991 seq_region_name 13

> [q574] populations[99] allele_count 400 allele TTTTTTTTTTTTTTT population 1000GENOMES:phase_3:EUR frequency 0.397614314115308

> [q575] populations[2] population gnomADg:nfe frequency 0.0001765 allele T allele_count 12

> [q576] populations[42] frequency 0.0642965204236006 allele T allele_count 85 population 1000GENOMES:phase_3:AFR

> [q577] populations[60] population 1000GENOMES:phase_3:EUR allele G allele_count 1006 frequency 1

> [q578] [0] id rs9573270 feature_type variation start 74212656 consequence_type intron_variant seq_region_name 13 source dbSNP strand 1 end 74212656 assembly_name GRCh37

rs35257605 (row 75's seed lead) is a poly-T repeat: GRCh38 13:73,649,404-73,649,416 (q570), GRCh37 13:74,223,541-553
(q571), 13 T ancestral, alleles of 11 to 17 T; the seed's C/CTT at 73,649,403 is the 15-T allele, 0.40 in 1000 Genomes
Europeans (q574), 0.43 in gnomAD genomes' non-Finnish Europeans. Ensembl's LD endpoint returns nothing for it (the
window query rendered no text), so its r² to any SNP is unknown. rs116257533: GRCh38 13:73,757,854 (q572), GRCh37
74,331,991 (q573), G/T, G ancestral; T is an African-ancestry allele, 0.064 in 1000 Genomes Africans (q576), absent in
Europeans there (q577), 0.00018 in gnomAD's non-Finnish Europeans (q575). Park's 13:74,212,656 is rs9573270 (q578),
intronic in KLF12 by position. For row 75.

## Reading 2026-11-12, record

> [q579] [0] seq_region_name 13 assembly_name GRCh37 strand 1 end 74331131 source dbSNP feature_type variation start 74331131 id rs78594190 consequence_type intron_variant

> [q580] populations[2] allele_count 12 frequency 0.0001764 population gnomADg:nfe allele G

> [q581] [0] d_prime 1.000000 population_name 1000GENOMES:phase_3:YRI variation1 rs116257533 variation2 rs78594190 r2 1.000000

Park's second passing line at row 75, GRCh37 13:74,331,131, is rs78594190 (q579): G at 0.00018 in gnomAD's non-Finnish
Europeans (q580), 0.065 in Africans, and in complete LD with rs116257533 in Yoruba, r² 1.0, D′ 1.0 (q581): one
African-ancestry haplotype. For row 75.

## Reading 2026-11-13, record

> [q582] mappings[0] assembly_name GRCh38 ancestral_allele T coord_system chromosome location 14:74855011-74855011 strand 1 start 74855011 allele_string T/C seq_region_name 14 end 74855011

> [q583] mappings[0] end 75321714 location 14:75321714-75321714 assembly_name GRCh37 ancestral_allele T start 75321714 seq_region_name 14 coord_system chromosome allele_string T/C strand 1

> [q584] populations[97] population 1000GENOMES:phase_3:EUR frequency 0.297216699801193 allele_count 299 allele C

> [q585] populations[92] allele_count 215 allele C population 1000GENOMES:phase_3:EAS frequency 0.213293650793651

> [q586] [0] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation2 rs929579 r2 0.971428 variation1 rs61978928

> [q587] populations[97] allele_count 318 allele T population 1000GENOMES:phase_3:EUR frequency 0.31610337972167

> [q588] [0] end 74855011 allele_string T/C strand 1 id rs61978928 start 74855011 most_severe_consequence 3_prime_UTR_variant seq_region_name 14 assembly_name GRCh38 input rs61978928

rs61978928 (row 76): GRCh38 14:74,855,011 (q582), GRCh37 14:75,321,714 (q583), T/C, T ancestral. C is 0.30 in 1000
Genomes Europeans (q584), 0.21 in East Asians (q585). rs929579, Wright's fathers' SNP 9 kb away, is at r² 0.97, D′ 1.0
in CEU (q586); its T is 0.32 in Europeans (q587), so its T rides with the lead's C. VEP: 3′ UTR of PROX2 (and YLPM1
transcripts) (q588). For row 76.

## Reading 2026-11-13, record

> [q589] mappings[0] ancestral_allele null seq_region_name 15 assembly_name GRCh38 start 29030729 coord_system chromosome strand 1 end 29030729 location 15:29030729-29030729 allele_string A/G

> [q590] mappings[0] ancestral_allele A strand 1 end 29322932 coord_system chromosome assembly_name GRCh37 allele_string A/G location 15:29322932-29322932 start 29322932 seq_region_name 15

> [q591] populations[55] frequency 0.115308151093439 population 1000GENOMES:phase_3:EUR allele G allele_count 116

> [q592] populations[31] frequency 0.427382753403933 allele G population 1000GENOMES:phase_3:AFR allele_count 565

> [q593] populations[7] allele G population ALFA:SAMN10492695 frequency 0.06404 allele_count 1162

> [q594] [0] assembly_name GRCh38 allele_string A/G seq_region_name 15 id rs77184423 most_severe_consequence intron_variant end 29030729 strand 1 input rs77184423 start 29030729

rs77184423 (row 77): GRCh38 15:29,030,729, where Ensembl's GRCh38 record prints the allele string as A alone (q589);
GRCh37 15:29,322,932, A/G, A ancestral (q590). G is 0.115 in 1000 Genomes Europeans (q591), 0.43 in Africans (q592),
0.24 in East Asians, and 0.064 in ALFA's Europeans (q593); the record carries no gnomAD frequency. VEP: intronic in
APBA2 (q594). NECS's controls carry G at 0.0045 (pmid-33948810#q33-q34) and Park's UK Biobank deposit at about
0.0008 (pmid-40021682#q79): the HRC-imputed samples see a rare allele where the sequenced panels see a common one,
so the frequency depends on the source (as at row 19). The EUR LD window at r² ≥ 0.5 holds 107 pairs. For row 77.

## Reading 2026-11-13, record

> [q595] mappings[0] strand 1 ancestral_allele A allele_string T/A assembly_name GRCh38 start 41138771 coord_system chromosome end 41138771 location 15:41138771-41138771 seq_region_name 15

> [q596] populations[77] frequency 0.503976143141153 allele T population 1000GENOMES:phase_3:EUR allele_count 507

> [q597] populations[64] allele T population 1000GENOMES:phase_3:CEU frequency 0.590909090909091 allele_count 117

> [q598] [4] population_name 1000GENOMES:phase_3:CEU d_prime 0.999997 variation2 rs3959554 variation1 rs28455998 r2 0.705928

> [q599] [9] population_name 1000GENOMES:phase_3:GBR d_prime 0.999998 variation1 rs28455998 variation2 rs3959554 r2 0.766987

> [q600] populations[65] frequency 0.671717171717172 population 1000GENOMES:phase_3:CEU allele_count 133 allele A

> [q601] populations[77] population 1000GENOMES:phase_3:EUR frequency 0.437375745526839 allele_count 440 allele G

> [q602] [4] variation1 rs28455998 variation2 rs11855102 r2 0.722033 d_prime 0.905420 population_name 1000GENOMES:phase_3:CEU

> [q603] populations[64] frequency 0.621212121212121 population 1000GENOMES:phase_3:CEU allele T allele_count 123

> [q604] [4] population_name 1000GENOMES:phase_3:CEU variation1 rs28455998 variation2 rs1678750 r2 0.979362 d_prime 1.000000

> [q605] populations[64] allele G allele_count 116 population 1000GENOMES:phase_3:CEU frequency 0.585858585858586

> [q606] [4] r2 0.897442 variation2 rs1869907 variation1 rs28455998 d_prime 0.957263 population_name 1000GENOMES:phase_3:CEU

> [q607] populations[65] allele T population 1000GENOMES:phase_3:CEU frequency 0.585858585858586 allele_count 116

Row 78. rs28455998 (q595): GRCh38 15:41,138,771, T/A, A ancestral, intergenic; T 0.504 in 1000 Genomes Europeans
(q596), 0.591 in CEU (q597). An A/T SNP near 50 %, so strand and phase are read from non-palindromic neighbours. Phase
from CEU, where the frequencies differ enough to decide (in GBR and pooled Europeans both phases fit). rs3959554,
Atkins' frailty SNP: r² 0.71 (CEU, D′ 1.00, q598), 0.77 (GBR, q599); A 0.672 in CEU (q600), G 0.437 in Europeans
(q601). With T at 0.591 and A at 0.672, r² 0.71 fits only T on A's haplotypes (the other phase caps r² near 0.34):
T rides with A (derived). rs11855102 (q602, q603): r² 0.72, D′ 0.91, T 0.621: T with T (the other phase caps r² near
0.42). rs1678750 (q604, q605): r² 0.98, D′ 1.00, G 0.586: G with T. rs1869907 (q606, q607): r² 0.90, T 0.586: T with T.
Ensembl returns no LD between the lead and Wright's Table 8 SNPs rs690136 and rs686038 (3 % variants). For row 78.

## Reading 2026-11-13, record

> [q608] mappings[0] assembly_name GRCh38 seq_region_name 15 allele_string G/A strand 1 coord_system chromosome end 47367997 start 47367997 ancestral_allele G location 15:47367997-47367997

> [q609] populations[76] allele A population 1000GENOMES:phase_3:EUR frequency 0.117296222664016 allele_count 118

> [q610] [0].transcript_consequences[1] biotype protein_coding hgnc_id HGNC:16770 gene_id ENSG00000137872 transcript_id ENST00000558014 gene_symbol_source HGNC variant_allele A impact MODIFIER gene_symbol SEMA6D strand 1

> [q611] [4] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation2 rs4774495 r2 1.000000 variation1 rs74011415

> [q612] [10] variation1 rs74011415 variation2 rs4774495 r2 1.000000 d_prime 1.000000 population_name 1000GENOMES:phase_3:GBR

> [q613] populations[79] allele_count 118 frequency 0.117296222664016 allele C population 1000GENOMES:phase_3:EUR

Row 79. rs74011415 (q608): GRCh38 15:47,367,997, G/A, G ancestral; A 0.117 in 1000 Genomes Europeans (q609); an intron
variant of SEMA6D's protein-coding transcripts (q610). rs4774495, Wright's SEMA6D lead: r² 1.00, D′ 1.00 in CEU (q611)
and GBR (q612); C 0.117 in Europeans (q613), so C rides with A and T with G. For row 79.

## Reading 2026-11-13, record

> [q614] [1] population_name 1000GENOMES:phase_3:CEU r2 0.174689 d_prime 0.787018 variation1 rs74011415 variation2 rs1378214

> [q615] [1] variation1 rs74011415 r2 0.161607 variation2 rs766132 d_prime 0.781812 population_name 1000GENOMES:phase_3:CEU

> [q616] [0] r2 0.150150 variation2 rs17358764 variation1 rs74011415 population_name 1000GENOMES:phase_3:CEU d_prime 0.836658

Row 79: Wright's three mothers' Table 9 SNPs near SEMA6D against the lead rs74011415, CEU r² 0.17 (rs1378214, q614),
0.15 (rs766132, q615) and 0.16 (rs17358764, q616); GBR 0.14 to 0.18. None tags the lead. For row 79.

## Reading 2026-11-13, record

> [q617] mappings[0] start 52537524 strand 1 end 52537524 ancestral_allele A location 16:52537524-52537524 assembly_name GRCh38 coord_system chromosome allele_string A/C seq_region_name 16

> [q618] populations[76] population 1000GENOMES:phase_3:EUR frequency 0.514910536779324 allele_count 518 allele A

> [q619] populations[64] population 1000GENOMES:phase_3:CEU allele_count 89 allele C frequency 0.44949494949495

> [q620] populations[77] allele_count 256 allele T frequency 0.254473161033797 population 1000GENOMES:phase_3:EUR

> [q621] populations[65] population 1000GENOMES:phase_3:CEU frequency 0.232323232323232 allele T allele_count 46

> [q622] [4] d_prime 0.947616 population_name 1000GENOMES:phase_3:CEU variation1 rs4783780 r2 0.332825 variation2 rs4784227

> [q623] [9] population_name 1000GENOMES:phase_3:GBR d_prime 0.941432 variation2 rs4784227 r2 0.317144 variation1 rs4783780

> [q624] [0] seq_region_name 16 start 52537524 end 52537524 assembly_name GRCh38 input rs4783780 strand 1 id rs4783780 most_severe_consequence intron_variant allele_string A/C

Row 82. rs4783780 (q617): GRCh38 16:52,537,524, A/C; A 0.515 in 1000 Genomes Europeans (q618), C 0.449 in CEU (q619);
an intron variant of TOX3 (q624). rs4784227: T 0.254 in Europeans (q620), 0.232 in CEU (q621). Between them r² 0.33,
D′ 0.95 in CEU (q622); 0.32, D′ 0.94 in GBR (q623). In CEU, T on C's haplotypes fits (r² up to 0.37), T on A's caps r²
near 0.25: T rides with C (derived). For row 82.

## Reading 2026-11-13, record

> [q625] [0].colocated_variants[0] id rs3112581 seq_region_name 16 allele_string A/C/G/T end 52537621 phenotype_or_disease 1 start 52537621 strand 1

> [q626] [4] r2 1.000000 variation2 rs3112581 variation1 rs4783780 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000

> [q627] populations[65] population 1000GENOMES:phase_3:CEU allele G frequency 0.44949494949495 allele_count 89

Row 82. 16_52537621_A_G is rs3112581 (q625), 97 bp from the lead; r² 1.00, D′ 1.00 with rs4783780 in CEU (q626; GBR the
same); its G at 0.449 in CEU (q627), the lead's C's frequency (q619): G rides with C. For row 82.

## Reading 2026-11-13, record

> [q628] populations[76] frequency 0.567594433399602 population 1000GENOMES:phase_3:EUR allele T allele_count 571

> [q629] populations[64] allele T allele_count 108 frequency 0.545454545454545 population 1000GENOMES:phase_3:CEU

> [q630] [2] d_prime 0.999998 population_name 1000GENOMES:phase_3:CEU variation2 rs10852521 r2 0.653151 variation1 rs1421085

> [q631] [7] d_prime 0.999996 population_name 1000GENOMES:phase_3:GBR variation2 rs10852521 r2 0.700406 variation1 rs1421085

> [q632] populations[66] population 1000GENOMES:phase_3:CEU frequency 0.439393939393939 allele_count 87 allele T

> [q633] mappings[0] start 53767042 end 53767042 seq_region_name 16 allele_string T/C strand 1 location 16:53767042-53767042 coord_system chromosome ancestral_allele T assembly_name GRCh38

> [q634] [0] start 53767042 most_severe_consequence intron_variant strand 1 id rs1421085 end 53767042 allele_string T/C input rs1421085 seq_region_name 16 assembly_name GRCh38

Row 83. rs1421085 (q633): GRCh38 16:53,767,042, T/C, an intron variant of FTO (q634); T 0.568 in 1000 Genomes Europeans
(q628), 0.545 in CEU (q629). rs10852521: r² 0.65, D′ 1.00 (CEU, q630); 0.70 (GBR, q631); its T 0.439 in CEU (q632).
With D′ 1, T on the lead's T haplotypes gives r² 0.65, T on C's would give 0.94: T rides with T (derived). For row 83.

## Reading 2026-11-13, record

> [q635] [1] population_name 1000GENOMES:phase_3:CEU variation1 rs1421085 variation2 rs7190492 r2 0.435892 d_prime 0.999993

Row 83: rs7190492, Wright's weaker AncestryDNA FTO line, is r² 0.44 to rs1421085 in CEU (q635). For row 83.

## Reading 2026-11-13, record

> [q636] populations[76] allele_count 294 frequency 0.292246520874752 population 1000GENOMES:phase_3:EUR allele A

> [q637] mappings[0] assembly_name GRCh38 allele_string C/A seq_region_name 16 coord_system chromosome end 56959412 strand 1 location 16:56959412-56959412 ancestral_allele C start 56959412

> [q638] [0] input rs3764261 assembly_name GRCh38 allele_string C/A strand 1 most_severe_consequence upstream_gene_variant id rs3764261 seq_region_name 16 end 56959412 start 56959412

> [q639] populations[101] allele_count 333 population 1000GENOMES:phase_3:EUR allele G frequency 0.331013916500994

Row 84. rs3764261 (q637): GRCh38 16:56,959,412, C/A, upstream of CETP (q638); A 0.292 in 1000 Genomes Europeans (q636).
rs5882, I405V: G (V) 0.331 in Europeans (q639). Ensembl returns no European LD between the two (below its reporting
floor), so they are separate signals. For row 84.

## Reading 2026-11-13, record

> [q640] [0].transcript_consequences[0] gene_symbol CETP impact MODERATE strand 1 polyphen_prediction benign protein_start 422 variant_allele A gene_symbol_source HGNC cdna_end 1294 sift_prediction tolerated hgnc_id HGNC:1869 cdna_start 1294 codons Gtc/Atc protein_end 422 cds_end 1264 transcript_id ENST00000200676 biotype protein_coding sift_score 1 amino_acids V/I cds_start 1264 gene_id ENSG00000087237 polyphen_score 0.003

rs5882 (row 84): CETP missense, codons Gtc/Atc (q640): the reference G codes valine, A isoleucine, so Barzilai's
405V is the G allele (p.422 in Ensembl's numbering, which counts the signal peptide). For row 84.

## Reading 2026-11-13, record

> [q641] mappings[0] start 72041694 coord_system chromosome end 72041694 location 16:72041694-72041694 seq_region_name 16 strand 1 allele_string A/T ancestral_allele A assembly_name GRCh38

> [q642] populations[77] allele T population 1000GENOMES:phase_3:EUR frequency 0.192842942345924 allele_count 194

> [q643] [2] d_prime 0.946112 r2 0.527366 population_name 1000GENOMES:phase_3:CEU variation2 rs9928413 variation1 rs12924886

> [q644] [2] r2 0.479718 d_prime 0.919644 variation1 rs12924886 variation2 rs17604662 population_name 1000GENOMES:phase_3:CEU

Row 85. rs12924886 (q641): GRCh38 16:72,041,694, A/T, A ancestral; T 0.193 in 1000 Genomes Europeans (q642); an intron
variant of a lncRNA near TXNL4B and HP. Wright's nearby Table 9 SNPs: rs9928413 r² 0.53 (q643), rs17604662 r² 0.48
(q644) in CEU. For row 85.

## Reading 2026-11-13, record

> [q645] [4] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 r2 0.955980 variation2 rs34042070 variation1 rs12924886

Row 85: rs34042070 r² 0.96, D′ 1.00 with rs12924886 in CEU (q645; 1.00 in GBR). Ensembl returns no CEU or GBR LD between
rs12924886 and Foote's rs7187129 (below its reporting floor): not a tag. For row 85.

## Reading 2026-11-13, record

> [q646] [4] r2 1.000000 variation1 rs1421085 population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation2 rs11642015

Row 83: rs11642015 r² 1.00, D′ 1.00 with rs1421085 in CEU (q646; GBR the same). For row 83.

## Reading 2026-11-13, record

> [q647] mappings[0] allele_string T/C coord_system chromosome location 16:89960104-89960104 start 89960104 strand 1 assembly_name GRCh38 ancestral_allele C end 89960104 seq_region_name 16

> [q648] populations[6] frequency 0.275 population gnomADg:nfe allele C allele_count 18693

> [q649] populations[80] population 1000GENOMES:phase_3:GBR frequency 0.307692307692308 allele_count 56 allele C

> [q650] [0].transcript_consequences[0] gene_symbol_source HGNC strand 1 transcript_id ENST00000268676 gene_id ENSG00000140995 variant_allele C gene_symbol DEF8 biotype protein_coding hgnc_id HGNC:25969 impact MODIFIER

> [q651] [0] population_name 1000GENOMES:phase_3:CEU r2 0.389348 variation2 rs4785759 variation1 rs4268748 d_prime 0.887536

> [q652] [0] population_name 1000GENOMES:phase_3:CEU variation2 rs9939542 variation1 rs4268748 r2 0.520343 d_prime 0.764047

> [q653] [0] r2 0.086201 variation1 rs4268748 d_prime 0.545100 population_name 1000GENOMES:phase_3:CEU variation2 rs1109334

Row 86. rs4268748 (q647): GRCh38 16:89,960,104, T/C; C 0.275 in gnomAD's non-Finnish Europeans (q648), 0.31 in GBR
(q649), common elsewhere too (0.28 in 1000 Genomes East Asians, 0.42 in Africans); an intron variant of DEF8 (q650),
in the MC1R region (Zenin names MC1R as the nearest gene, pmid-30729179#q121). Wright's viability SNPs: rs4785759 r² 0.39 (q651), rs9939542 0.52 (q652), rs1109334 0.09 (q653)
in CEU. For row 86.

## Reading 2026-11-13, record

> [q654] [0] name 1000GENOMES:phase_3:CEU description Utah residents with Northern and Western European ancestry size 99

Row 86. Phased in CEU (q654, 99 people, 198 haplotypes) from Ensembl's 1000 Genomes phase 3 genotype records for
rs4268748, rs9939542 and rs4785759 (each `genotype X|Y`, phased; counted from the listings): the lead's C rides with
rs9939542's C on 53 of its 62 haplotypes (T with A on 122 of 136), and with rs4785759's A on 59 of 62 (T with C on 100
of 136). For row 86.

## Reading 2026-11-13, record

> [q655] populations[31] population gnomADg:nfe allele C frequency 0.04915 allele_count 3343

> [q656] populations[87] frequency 0.0526838966202783 allele C population 1000GENOMES:phase_3:EUR allele_count 53

> [q657] populations[84] allele_count 1008 population 1000GENOMES:phase_3:EAS frequency 1 allele T

> [q658] [0].transcript_consequences[2] cds_end 226 protein_end 76 codons Acc/Gcc gene_id ENSG00000108771 amino_acids T/A cds_start 226 polyphen_score 0.015 sift_score 0.35 biotype protein_coding transcript_id ENST00000413196 gene_symbol_source HGNC variant_allele C protein_start 76 gene_symbol DHX58 strand -1 polyphen_prediction benign impact MODERATE sift_prediction tolerated cdna_start 601 hgnc_id HGNC:29517 cdna_end 601

> [q659] [0] population_name 1000GENOMES:phase_3:CEU r2 0.649944 variation2 rs12600570 variation1 rs34891485 d_prime 1.000000

> [q660] [0] variation2 rs11079033 d_prime 0.999999 population_name 1000GENOMES:phase_3:CEU variation1 rs34891485 r2 0.437410

rs34891485 (row 87): GRCh38 17:42,111,440 T/C, GRCh37 17:40,263,458. C, the minor allele, is 0.049 in gnomAD's
non-Finnish Europeans (q655) and 0.053 in 1000 Genomes Europeans (q656), absent in East Asians (q657). A missense
variant of DHX58 (q658): codons Acc/Gcc, threonine 76 to alanine (the gene is on the reverse strand, so the forward
strand's C is the alanine codon's G); SIFT tolerated, PolyPhen benign (0.015). LD in CEU: rs12600570 r² 0.65, D′ 1.00
(q659); rs11079033 r² 0.44 (q660). Phased in CEU (q654) from the 1000 Genomes genotype records of rs34891485 and
rs12600570 (`genotypes-*.json`, 198 haplotypes): (T, C) 173, (C, T) 17, (T, T) 8: the lead's C always rides with
rs12600570's T. For row 87.

## Reading 2026-11-13, record

> [q661] [0] d_prime 0.718209 variation1 rs34891485 variation2 rs76611716 population_name 1000GENOMES:phase_3:CEU r2 0.368623

> [q662] [0] d_prime 0.697817 population_name 1000GENOMES:phase_3:CEU variation1 rs34891485 variation2 rs1011157 r2 0.277680

Row 87, LD in CEU from rs34891485: to rs76611716, Timmers' peak 245 kb away, r² 0.37, D′ 0.72 (q661); to rs1011157,
Timmers' strongest line within 1 Mb (BECN1, 700 kb), r² 0.28, D′ 0.70 (q662). Rosoff's other independent SNPs at the
locus: rs12325861 r² 0.30, rs79677630 0.51, rs78645838 0.31 (`ld-ceu-rs34891485-*.json`); rs35118457 (58 bp away)
has no pair Ensembl reports. For row 87.

## Reading 2026-11-13, record

> [q663] populations[20] allele_count 21914 population gnomADg:nfe frequency 0.3224 allele C

> [q664] populations[77] allele C allele_count 288 population 1000GENOMES:phase_3:EUR frequency 0.286282306163022

> [q665] populations[72] allele C allele_count 50 population 1000GENOMES:phase_3:EAS frequency 0.0496031746031746

> [q666] [0] d_prime 1.000000 variation2 rs9899580 variation1 rs940088 population_name 1000GENOMES:phase_3:CEU r2 0.977926

> [q667] [0] population_name 1000GENOMES:phase_3:CEU d_prime 1.000000 variation1 rs940088 variation2 rs11655587 r2 0.840531

> [q668] [0] d_prime 0.832860 r2 0.649295 variation1 rs940088 variation2 rs11079849 population_name 1000GENOMES:phase_3:CEU

> [q669] [0] id rs940088 strand 1 end 49068486 assembly_name GRCh38 seq_region_name 17 allele_string T/C most_severe_consequence intergenic_variant input rs940088 start 49068486

rs940088 (row 88): GRCh38 17:49,068,486 T/C, GRCh37 17:47,145,848, intergenic (q669). C 0.32 in gnomAD's non-Finnish
Europeans (q663), 0.29 in 1000 Genomes Europeans (q664), 0.05 in East Asians (q665). LD in CEU: rs9899580 r² 0.98, D′
1.00 (q666); rs11655587, the lead of the BMI, heart-failure and ischaemic heart disease sets (GRCh38 17:49,063,432),
r² 0.84, D′ 1.00 (q667); rs11079849 r² 0.65 (q668). Phased in CEU (q654) from the 1000 Genomes genotype records: the
lead's C rides with rs9899580's G on 68 of 69 C haplotypes (T with T on all 129 T haplotypes), and with rs11655587's T
on all 69. For row 88.

## Reading 2026-11-13, record

> [q670] [0] r2 0.200733 variation1 rs76611716 population_name 1000GENOMES:phase_3:CEU d_prime 0.501555 variation2 rs1011157

Row 87: the two Timmers peaks near the lead, rs76611716 and rs1011157, r² 0.20, D′ 0.50 in CEU (q670). Their 1000
Genomes genotype records are cached beside the lead's (`genotypes-rs76611716.json`, `genotypes-rs1011157.json`). For
row 87.

## Reading 2026-11-13, record

> [q671] populations[23] allele T allele_count 21553 frequency 0.317 population gnomADg:nfe

> [q672] [0].transcript_consequences[0] transcript_id ENST00000269373 gene_symbol_source HGNC cdna_end 1466 cdna_start 1466 gene_id ENSG00000141560 hgnc_id HGNC:25700 variant_allele T gene_symbol FN3KRP biotype protein_coding impact MODIFIER strand 1

rs1046896 (row 89): GRCh38 17:82,727,657 C/T, GRCh37 17:80,685,533, in FN3KRP's 3′ UTR (q672); T 0.317 in gnomAD's
non-Finnish Europeans (q671). For row 89.

## Reading 2026-11-13, record

> [q673] populations[9] allele_count 3248 frequency 0.04775 population gnomADg:nfe allele A

> [q674] [0].transcript_consequences[0] strand -1 impact MODIFIER biotype protein_coding variant_allele A hgnc_id HGNC:6930 gene_symbol MC2R gene_id ENSG00000185231 transcript_id ENST00000327606 gene_symbol_source HGNC

rs28926173 (row 90): GRCh38 18:13,886,720 G/A, GRCh37 18:13,886,719, an intron of MC2R (q674); A 0.048 in gnomAD's
non-Finnish Europeans (q673). Ensembl reports no CEU LD pair from it to Wright's SNPs 300 to 500 kb away (rs1785171,
rs1785177, rs2567166, rs11659850, rs1648598, rs1785205). For row 90.

## Reading 2026-11-14, record

> [q675] populations[17] allele_count 15967 population gnomADg:nfe allele C frequency 0.2348

> [q676] [0] start 60183864 most_severe_consequence intergenic_variant strand 1 id rs17782313 end 60183864 allele_string T/A/C input rs17782313 seq_region_name 18 assembly_name GRCh38

> [q677] [0] variation2 rs476828 d_prime 1.000000 population_name 1000GENOMES:phase_3:CEU variation1 rs17782313 r2 0.974097

> [q678] [0] variation1 rs17782313 variation2 rs17066892 r2 0.090156 d_prime 0.308195 population_name 1000GENOMES:phase_3:CEU

rs17782313 (row 91): GRCh38 18:60,183,864 T/C, GRCh37 18:57,851,097, intergenic (q676), about 188 kb downstream of
MC4R; C 0.235 in gnomAD's non-Finnish Europeans (q675). LD in CEU: rs476828 r² 0.97 (q677); rs17066892, Deelen's
99th-percentile peak, r² 0.090 (q678). Ensembl reports no CEU pair from the lead to Wright's nearby lines (rs1379444,
rs35748167, rs650313, rs512279, rs9646627, 72 to 680 kb away) or to rs752720, rs1791329 and rs7228187. For row 91.

## Reading 2026-11-14, record

> [q679] mappings[0] seq_region_name 18 ancestral_allele null assembly_name GRCh38 end 73851283 strand 1 start 73851283 location 18:73851283-73851283 coord_system chromosome allele_string T/A/G

> [q680] populations[9] allele G allele_count 79 frequency 0.001456 population gnomADg:nfe

> [q681] populations[77] allele_count 93 allele G frequency 0.0924453280318091 population 1000GENOMES:phase_3:EUR

> [q682] populations[44] population ALFA:SAMN10492695 frequency 0.05477 allele G allele_count 1105

> [q683] populations[6] population gnomADg:asj frequency 0.01659 allele_count 41 allele G

> [q684] populations[3] population gnomADg:afr frequency 0.07373 allele_count 2438 allele G

> [q685] [0] id rs77546126 strand 1 assembly_name GRCh38 end 73851283 seq_region_name 18 allele_string T/A/G most_severe_consequence intron_variant input rs77546126 start 73851283

> [q686] populations[13] allele T allele_count 8460 frequency 1 population gnomADg:fin

rs77546126 (row 92): GRCh38 18:73,851,283, T/A/G (q679; the record holds no GRCh37 mapping, the paper's 71,518,518
is GRCh37, pmid-33948810#q37). G is 0.15 % in gnomAD's non-Finnish Europeans (q680; absent in its Finns, T at frequency 1, q686), 1.7 % in its
Ashkenazi Jews (q683), 7.4 % in its Africans (q684); 9.2 % in 1000 Genomes' Europeans (q681; CEU 0.11, GBR 0.08) and
5.5 % in ALFA's (q682). VEP: intronic in a lncRNA (q685), ENSG00000302257. NECS's controls (0.19 %,
pmid-33948810#q37) agree with gnomAD; 1000 Genomes and ALFA give a common allele, the frequency Deelen's two indels
beside it carry (pmid-31413261#q227-q230). The LGP's controls (0.006, pmid-33948810#q38) sit at about a third of
gnomAD's Ashkenazi 0.0166 (some 8 copies of 1,276 alleles where 21 are expected; derived). The pairwise LD endpoint
(1000 Genomes CEU) returned an empty list between the lead and each of Wright 2019's three nearest lines (rs12955729,
89 kb; rs17088751, 221 kb; rs11874029, 503 kb), so none tags it at the endpoint's threshold; the empty answers render
to no text and are not cached. For row 92.

## Reading 2026-11-14, record

> [q687] mappings[0] allele_string G/A/C coord_system chromosome start 32967573 location 19:32967573-32967573 strand 1 seq_region_name 19 assembly_name GRCh38 ancestral_allele G end 32967573

> [q688] populations[16] allele C allele_count 8205 frequency 0.1232 population gnomADg:nfe

> [q689] populations[77] frequency 0.116302186878728 population 1000GENOMES:phase_3:EUR allele_count 117 allele C

> [q690] populations[74] frequency 0.282738095238095 population 1000GENOMES:phase_3:EAS allele C allele_count 285

> [q691] [0].transcript_consequences[3] hgnc_id HGNC:25907 gene_id ENSG00000121289 transcript_id ENST00000305768 biotype protein_coding gene_symbol_source HGNC variant_allele C gene_symbol CEP89 impact MODIFIER strand -1

> [q692] [0] variation1 rs62127362 r2 0.054894 variation2 rs745961 population_name 1000GENOMES:phase_3:CEU d_prime 0.999835

rs62127362 (row 94): GRCh38 19:32,967,573, G/A/C, G ancestral (q687; Deelen's GRCh37 position 33,458,479). C is 0.12
in gnomAD's non-Finnish Europeans (q688) and 1000 Genomes' Europeans (q689), 0.28 in East Asians (q690), 0.09 in
Africans. VEP: intronic in CEP89 (q691; FAAP24 and RPL31P60 within 5 kb). LD to Wright's rs745961 in CEU r² 0.055
(q692). For row 94.
