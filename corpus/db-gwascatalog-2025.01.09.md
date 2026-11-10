---
key: db-gwascatalog-2025.01.09
database: gwascatalog
release: "2025.01.09"
url: https://ftp.ebi.ac.uk/pub/databases/gwas/summary_statistics/GCST007001-GCST008000/GCST007406/harmonised/GCST007406.h.tsv.gz
accessed: 2026-11-11
depth: record
---

The GWAS Catalog's harmonised summary statistics for GCST007406 (Zenin 2019, healthspan, 300,447 UK Biobank
participants; the file's metadata last modified 2025-01-09, the release named here), read by region through its
tabix index. Zenin's own deposit (Zenodo 1302861, `healthspan_summary.csv.gz`, 237 MB) is gzipped, and `loci
fetch-supp` refuses a `.gz` file, so the record is not cached and `check quotes` reads these as unknown (D12).
Columns: chromosome, base_pair_location (GRCh38), effect_allele, other_allele, beta, standard_error,
effect_allele_frequency, p_value, variant_id, hm_coordinate_conversion, hm_code, rsid. The beta is on the log
hazard of the end of healthspan, so positive means an earlier end.

## Reading 2026-11-11, record

The 1p13.3 lipid locus, for row 6.

> [q1] 1 109275908 T C 0.0224 0.00582 0.78 0.000118699199285093 rs646776

rs646776: T, the LDL-raising and lifespan-lowering allele (0.78), β 0.0224 (SE 0.0058), P 1.2 × 10⁻⁴: T ends
healthspan earlier, C later. Nominal, on the lifespan side. rs602633 (G, β 0.0231, P 8.1 × 10⁻⁵), rs4970836 (A,
0.0237, 4.1 × 10⁻⁵), rs599839 (A, 0.0233, 5.2 × 10⁻⁵) and rs12740374 (T, −0.023, 8.0 × 10⁻⁵, T being the
minor, LDL-lowering allele there) agree. Not genome-wide; no credible set in Open Targets.
