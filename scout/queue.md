# Queue

New papers bearing on a seed locus (`docs/longevitymap_v2/data/seed_variants.csv`; `rows/` holds none yet), for the
curator. Each entry: the locus, one line on why, the passage that says it (verbatim, with where and when it was
read), and every identifier the paper has. The curator takes it from here; the scout never tiers a row.

## Open

### pmid-42928374 — FES/FURIN (locus 81): pleiotropy with severe mental disorders

- **Paper:** Pisanu C, Nishioka M, et al. "Genome-wide analysis identifies pleiotropic genes shared between severe
  mental disorders and biomarkers of cellular aging." *Mol Psychiatry*, 2026 Oct 25 (online ahead of print).
  PMID 42928374, doi 10.1038/s41380-026-03946-0. Track E sweep, 2026-11-10 (E-core).
- **Why:** FURIN is named among nine genes carrying variants shared between "aging biomarkers" and all three
  disorders (bipolar disorder, MDD, schizophrenia). The biomarkers studied are mvAge (the multivariate longevity
  factor), brain-age gap, telomere length, mtDNA copy number and epigenetic age acceleration; the abstract does not
  say which of them FURIN's variant is shared with. If mvAge, this bears on the pleiotropy axis of the FES/FURIN row
  (track H counts rs6224 among the few lifespan leads with almost no disease footprint); if a clock or brain age,
  it is in a class track E keeps out of scoring.
- **Passage** (abstract, PubMed, https://pubmed.ncbi.nlm.nih.gov/42928374/, read 2026-11-10):
  > We identified several pleiotropic variants, with nine genes (AC068490.2, ASIC2, CNNM2, FURIN, GPM6A, HS6ST3, RP5-1043L13.1, SORCS3 and SP4) containing variants shared between aging biomarkers and all disorders.
- **Unknown:** which biomarker FURIN's variant is shared with; whether that variant is rs6224 or rs17514846 (the seed's
  variants), or in LD with them (the abstract names no rsID); whether the article is open access (a "© The
  Author(s)" line does not show a licence). Each is settled by the full text or its supplementary tables.

### rs13141210 at locus 28 RNU1-63P (4q13.2): a second mvAge signal, candidate row (D25.6)

- **Paper:** Rosoff DB et al. "Multivariate genome-wide analysis of aging-related traits identifies novel loci and new
  drug targets for healthy aging." *Nat Aging*, 2023 Aug. PMID 37550455, PMC10432278, doi 10.1038/s43587-023-00455-5
  (title checked against PubMed 2026-11-11). Corpus note `corpus/pmid-37550455.md`. From the curator, 2026-11-11.
- **Why:** a genome-wide mvAge lead 111 kb from row 28's lead rs28637671 at r² 0.095, so a separate signal; a seed
  rsID with no seed locus of its own. Row 28 names it in prose; D25.6 sends it here, to be curated after the seed list.
  The row's prose reads it as a possible B under D16 (LifeGen z about 4.4).
- **Passage** (Table 1, full text, Europe PMC, read by the curator 2026-11-11; `pmid-37550455#q28`):
  > rs13141210 4,67891641 C/T 0.50 −0.0058 (0.001) 1.46 × 10−8 RNU6-699P (intergenic) 0.55 Adult body size, cognitive performance, education, household income, lung cancer
- **Unknown:** its own tier; whether its tag rs10434248 (aging-GIP1, Timmers 2022) counts as a second multivariate
  scan or a shared input.

### rs16843603 (ADD1) at locus 25 HTT (4p16.3): a second mvAge signal, candidate row (D25.6)

- **Paper:** Rosoff 2023, as above (PMID 37550455). From the curator, 2026-11-11.
- **Why:** a genome-wide mvAge lead in an ADD1 intron, r² 0.095 to row 25's lead rs61348208, so a separate signal; a
  seed rsID with no seed locus of its own. Row 25 names it in prose; D25.6 sends it here.
- **Passage** (Supplementary table, MOESM3, read by the curator 2026-11-11; `pmid-37550455#q23`):
  > No (Frailty, Lifespan) rs16843603 11 4:2928577 4 2928577 7 rs16843603;rs2798287;rs11937729;rs1801058;rs113928896;rs71597207;rs34155847 C T 0.3052 4.1616324788e-10 -0.00705057367178 0.00112848149177 ADD1 0 intronic 3.773 5 4 4 2.83548326833141 4 0.585723327229924
- **Unknown:** its own tier; whether any lifespan study carries it outside mvAge's inputs (D16).

### rs114298671 (MSANTD1/RGS12) at locus 25 HTT (4p16.3): a third mvAge signal, candidate row (D25.6)

- **Paper:** Rosoff 2023, as above (PMID 37550455). From the curator, 2026-11-11.
- **Why:** a genome-wide mvAge lead near MSANTD1, novel in Rosoff, r² 0.08 to row 25's lead rs61348208, so a separate
  signal; a seed rsID with no seed locus of its own. Row 25 names it in prose; D25.6 sends it here.
- **Passage** (Supplementary table, MOESM3, read by the curator 2026-11-11; `pmid-37550455#q24`):
  > Yes rs114298671 11 4:3281869 4 3281869 2 rs114298671;rs71597207 A G 0.1223 1.56686856265e-08 0.00886760197706 0.00156835563347 MSANTD1 8403 intergenic 0.873 5 5 15 1.82958854405307 4 0.767064731931399
- **Unknown:** its own tier; whether any lifespan study carries it outside mvAge's inputs (D16); it shares a tag,
  rs71597207, with rs16843603's set above, so whether the two are wholly separate is unsettled here.

### rs3131621 (MICA … MICB / HCP5) at locus 37 HCP5 (6p21.33): the fathers' signal, candidate row (D25.6)

- **Paper:** Pilling LC et al. "Human longevity: 25 genetic loci associated in 389,166 UK biobank participants."
  *Aging (Albany NY)*, 2017. PMID 29227965. Replication: Wright KM et al., *G3*, 2019, PMID 31484785. Corpus notes
  `corpus/pmid-29227965.md`, `corpus/pmid-31484785.md`. From the curator, 2026-11-11.
- **Why:** Pilling's fathers' lead, 278 kb from row 37's lead rs3130507 (the mothers' signal), with no Ensembl CEU pair
  above the 0.05 floor (`db-ensembl-116#q247`, `q248`; the endpoint answers pairs megabases apart, `q242`): a
  separate signal, and the seed's
  second rsID at locus 37 with no locus of its own. Row 37 names it in prose; D25.6 sends it here. It has the stronger
  case of the two: replicated in AncestryDNA's fathers (P 7.7e-4, meta-analysis 8.9e-9, Wright's Table 3), LifeGen
  with UK Biobank P 1.9e-6, Timmers' LifeGen-without-UK-Biobank fathers one-sided P 0.093; the GWAS Catalog also lists
  rheumatoid arthritis or inflammatory bowel disease there (P 2e-13, `db-gwascatalog-2026.10.29#q234`, `q235`).
- **Passage** (Table 2, full text, read by the curator 2026-11-11; not yet quoted in the note):
  > rs3131621 6 31425499 A G 8.9E-08 1.9E-02 4.8E-01 3.5E-05 3.6E-08 0.629 −0.0124 0.0022 MICA … MICB
- **Unknown:** its own tier (Deelen 2019 flat: 90th OR 1.0004, P 0.99, a flag under the APOE factor only, so none,
  by the curator's reading); its gene (Open Targets 26.09 has no record of it).

### rs15285 (LPL 3′ UTR) at locus 52 LPL (8p21.3): Wright's fathers' signal, candidate row (D25.6)

- **Paper:** Wright KM et al. "A Prospective Analysis of Genetic Variants Associated with Human Lifespan." *G3*, 2019.
  PMID 31484785. Corpus note `corpus/pmid-31484785.md` (q91 to q93). From the curator, 2026-11-11.
- **Why:** the seed's second rsID at locus 52, 11 kb from row 52's lead rs268 (LPL Asn318Ser) and a separate signal:
  r² below 0.05 from the two frequencies (`db-ensembl-116#q364`), and Aragam 2022's coronary disease
  fine-mapping holds rs268 alone in one set and rs15285 in another (`db-opentargets-26.09#q671`, `q678`). It carries
  LPL's only lifespan-class genome-wide result: Wright's fathers' meta-analysis P 8.5e-10, T (0.29 in Europeans)
  longer-lived, heterogeneity P 0.83; the AncestryDNA arm (P 2.4e-5, 1.0e-4 after genomic control) is inside the pooled
  P. Row 52 names it in prose; D25.6 sends it here. T tags rs13702 (r² 0.98) and partly rs328 (0.33).
- **Passage** (Table 3, full text, quoted as `pmid-31484785#q91`):
  > LPL	rs15285	8	19824667	8.46e-10	2.44e-05	0.012	0.003	1.20e-07	0.013	0.002
- **Unknown:** its own tier. Nothing outside Wright replicates it nominally: Timmers 2019 P 3.5e-5 (holds UK
  Biobank), Deelen's 90th one-sided 0.065, FinnGen death one-sided 0.16 (APOE factor power 0.66, no red flag), so B by
  the curator's reading; Wright's PICS set is flat (PIP 0.066 of 25, C3), L2G LPL 0.98.

### rs11780471 (3.6 kb upstream of EPHX2) at locus 53 EPHX2 (8p21.1): Wright's fathers' signal, candidate row (D25.6)

- **Paper:** Wright KM et al. "A Prospective Analysis of Genetic Variants Associated with Human Lifespan." *G3*, 2019.
  PMID 31484785. Corpus note `corpus/pmid-31484785.md` (q99). From the curator, 2026-11-11.
- **Why:** 97 kb from row 53's lead rs7844965 and tagging it only at r² 0.13, D′ 0.66 in CEU (`db-ensembl-116#q373`):
  genome-wide in Wright's fathers' meta-analysis, P 3.2e-8 (AncestryDNA 1.8e-5, UK Biobank 1.6e-5, heterogeneity P
  0.68), A (0.065) longer-lived. Wright's Table 3 lists one EPHX2..CLU locus, so whether this is a second signal is
  untested (no conditional analysis read). It is a known smoking locus: A lowers smoking initiation (P 5e-110,
  `db-gwascatalog-2026.10.29#q347`) and lung cancer (P 2e-8, `q351`), upstream of EPHX2 (`db-ensembl-116#q374`).
  Row 53 names it in prose; none of its evidence is cited there.
- **Passage** (Supplemental Table 9, quoted as `pmid-31484785#q99`):
  > FatherMetal_Lifespan+AttainedAge	8	27344719	rs11780471	3.239e-08	697000	1.759e-05	0.02224	0.005181	1.6e-05	0.0193807	0.00447518	0.6758	G
- **Unknown:** its independence from rs7844965 (a conditional test or a fine-mapping with two sets); Timmers 2019 P
  2.3e-6, Deelen's 90th P 0.33 and 99th 0.10 (A's side), read in the cached windows, not quoted.

### rs4784227 (TOX3/CASC16) at locus 82 CASC16 (16q12.1): Zenin's healthspan signal, candidate row (D25.6, D30.8)

- **Paper:** Zenin A et al. "Identification of 12 genetic loci associated with human healthspan." *Commun Biol*, 2019.
  PMID 30729179, PMC6353874, doi 10.1038/s42003-019-0290-0 (title checked against PubMed 2026-11-13). Corpus note
  `corpus/pmid-30729179.md` (q111, q112, q114). From the lead's batch-nine read, D30.8, 2026-11-13.
- **Why:** the seed's second rsID at locus 82, 28 kb from row 82's lead rs4783780 (r² 0.33, D′ 0.95 in CEU,
  `db-ensembl-116#q622`), and the TOX3/CASC16 breast-cancer variant. Genome-wide for healthspan in Zenin (T earlier,
  P 3.0e-8 after genomic control), cancer its only component (P 2.2e-10; parents' death P 0.10). Row 82 reads its
  lifespan Zs as the lead's shadow and Timmers 2020's set as colocalising with none of its breast-cancer sets, so a
  separate signal with no lifespan signal of its own once the lead is accounted for. D30.8 sends it here as a
  healthspan candidate.
- **Passage** (Table 2, full text, quoted as `pmid-30729179#q111`):
  > rs4784227 16 52,599,188 T C 0.24 0.032 3.02e-08 0.018 7.75e-02
- **Unknown:** its own tier; whether a healthspan signal carried by cancer alone counts for this module (D25.1, row
  86's shape, is the nearest precedent read here, not applied).

### rs6062322 (ZBTB46) at locus 99 CHRNA4 (20q13.33): a novel mvAge signal, candidate row (D25.6, D17.6)

- **Paper:** Rosoff 2023, as above (PMID 37550455). Corpus note `corpus/pmid-37550455.md` (q77, q78). From the
  curator, 2026-11-14 (#longevity-loci > curation, 640348417).
- **Why:** the seed's second rsID at locus 99, 455 kb from row 99's lead rs2273500 with no CEU LD pair at the
  endpoint's threshold, so another signal (D17.6); named in row 99, not scored there. Novel in Rosoff ("Yes"), mvAge
  P 3.3e-8 (T −0.0071, A the healthier allele by the curator's reading), frailty P 1.1e-5. Elsewhere in the corpus:
  Timmers 2019 A −0.0130, P 0.010 (`pmid-30642433#q356`); Zenin 2019 healthspan T −0.0228, P 2.6e-4
  (`pmid-30729179#q138`); FinnGen flat, P 0.56 (`db-finngen-r11#q74`).
- **Passage** (Supplementary table, MOESM3, quoted as `pmid-37550455#q77`):
  > Yes rs6062322 38 20:62441599 20 62441599 1 rs6062322 T A 0.1938 3.30263251677e-08 -0.00708049186358 0.0012816330016 ZBTB46:RP4-583P15.11 00:00:00 ncRNA_intronic 3.512 5 4 15 4.23399586645392 4 0.375263213896552
- **Unknown:** its own tier; whether any lifespan study carries it outside mvAge's inputs (D16: Timmers is an input).
  The allele each study favours is not reconciled here: the corpus notes read mvAge's A as healthier but Zenin's T
  −0.0228 on the healthspan hazard as T healthier (Zenin's positive β is an earlier end), and Rosoff's own healthspan
  column prints T +0.0228 (q78). Each sign convention needs checking before a direction is stated.
