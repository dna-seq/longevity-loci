---
key: db-gnomad-4
database: gnomad
release: "4"
url: https://github.com/broadinstitute/gnomad-blog/blob/main/content/posts/2023-11-gnomad-v4-0.md
accessed: 2026-11-16
depth: record
---

gnomAD's own v4.0 release announcement, read from the source of its blog post in the Broad's public repository
(`broadinstitute/gnomad-blog`, `content/posts/2023-11-gnomad-v4-0.md`, cached by `loci fetch-supp` as a text file);
the page on gnomad.broadinstitute.org renders in the browser only. Each quote is a line as cached.

## Reading 2026-11-16, record

> [q1] Today, we are delighted to announce the release of gnomAD v4, which includes data from 807,162 total individuals. This release is nearly **5x** larger than the combined v2/v3 releases and consists of two callsets: exome sequencing data from 730,947 individuals, including 416,555 individuals from the [UK Biobank](https://www.ukbiobank.ac.uk/), and genome sequencing data from 76,215 individuals.

> [q2] However, the new inclusion of cohorts such as the UK Biobank means that the proportion of samples with European ancestry is higher than in previous releases.

gnomAD v4's exomes are 730,947 people, 416,555 of them UK Biobank's (q1, 57 %), and UK Biobank's inclusion raises the
European share (q2). The ancestry breakdown is an image in the post, so the non-Finnish European exome total is not
quoted; derived from Ensembl 116's exome line at rs41419545 (3,534 copies at 0.003178, db-ensembl-116#q901) it is about
1.11 million alleles, about 556,000 people. UK Biobank's 416,555 would be up to 75 % of that; how many of them fall
outside the non-Finnish European group is not printed. Ensembl 116's records do not name the gnomAD minor release
they read; the totals match v4's. For D35.6, rows 121 and 140.

## Reading 2026-11-16, record

> [q3] The 76,156 genomes from [gnomAD v3.1.2](https://gnomad.broadinstitute.org/news/2021-10-gnomad-v3-1-2-minor-release/) have been included in gnomAD v4.

> [q4] to ensure no overlap between the exomes and genomes

gnomAD v4's genomes are v3.1.2's 76,156 (q3), a 2021 release, before UK Biobank's exomes entered gnomAD, and kept
apart from the exomes in v4 (q4): so the genome frequencies (row 140's 0.334 %, db-ensembl-116#q902) are not UK
Biobank's people. For D35.6 shown on row 140, batch fourteen (D37).

## Reading 2026-11-19, record

> [q5] data.variant variant_id 18-50083001-C-T chrom 18 pos 50083001 ref C alt T exome null

> [q6] data.variant.genome.populations[27] id nfe ac 32 an 68036

> [q7] data.variant.genome.populations[24] id afr ac 5469 an 41550

> [q8] data.variant.genome.populations[21] id asj ac 0 an 3472

> [q9] data.variant.genome.populations[6] id fin ac 0 an 10620

> [q10] data.variant.genome ac 5775 an 152318

gnomAD v4's variant record for rs78441534, read through gnomAD's public API (dataset gnomad_r4) and cached by
`loci fetch-supp`, since Ensembl's REST service refused through the proxy on 2026-11-19 (503). GRCh38 18:50,083,001
C>T (q5), genomes only (no exome call). T in 32 of 68,036 non-Finnish European alleles (0.047 %, q6), 5,469 of 41,550
African (13.2 %, q7), none of 3,472 Ashkenazi (q8) or 10,620 Finnish (q9); 3.8 % over all genomes (q10). For row 175.

## Reading 2026-11-19, record

> [q11] data.variant.genome.populations[226] id 1kg:ceu ac 1 an 238

> [q12] data.variant.genome.populations[256] id 1kg:ibs ac 1 an 208

> [q13] data.variant.genome.populations[259] id 1kg:gbr ac 0 an 174

> [q14] data.variant.genome.populations[220] id 1kg:tsi ac 0 an 206

> [q15] data.variant.genome.populations[238] id 1kg:fin ac 0 an 196

The 1000 Genomes European samples in the same record (gnomAD's HGDP and 1000 Genomes subset): T in 1 of 238 CEU
alleles, 1 of 208 IBS, none of 174 GBR, 206 TSI or 196 FIN, 2 of 1,022 in all (0.2 %): rare, a second reference
agreeing with the non-Finnish European genomes (q6) and the NECS controls. For row 175.
