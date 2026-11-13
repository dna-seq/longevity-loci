# Searches

The scout's ledger (`docs/seats/SCOUT.md`): per track, each query as run, its sources, the window it covered, how
many hits and how many were new. A later sweep reruns the same query from the last window's end; a changed query is
a new line with its reason. The tracks are `docs/longevitymap_v2/evidence/`, A to K.

**Where the tracks stand.** None of the eleven syntheses records its query strings: track E names its PubMed
queries ("core", "clock", "somatic-mosaicism", "targeted mtDNA/long-read/ancestry/replication/review") with counts,
the others name none. Every query below is therefore **new**, written by the scout on 2026-11-10, and not a
reconstruction of what a track ran. "Covered to" is the date a synthesis states for its own searches; where it states
none, it is unknown.

How a query runs: PubMed through E-utilities by **entry date** (`datetype=edat`), so a paper published earlier but
indexed late is still caught; Europe PMC's preprint index (`SRC:PPR`) by **first index date** (`FIRST_IDATE`). Each
window overlaps the last by about two weeks. A hit is new when neither its PMID nor its DOI appears in any track's
evidence or candidate CSV, in the seed list, or in `scout/screened.md`.

The literal requests, so a run can be rebuilt without the script:

- PubMed: `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=pubmed&term=<query>&datetype=edat&mindate=YYYY/MM/DD&maxdate=YYYY/MM/DD&retmax=500&retmode=json`,
  then `esummary.fcgi?db=pubmed&id=<ids>&retmode=json` for titles and DOIs.
- Europe PMC: `https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=(<query>) AND (FIRST_IDATE:[YYYY-MM-DD TO YYYY-MM-DD])&format=json&pageSize=500&resultType=lite&cursorMark=*`,
  paged by `nextCursorMark`.

**Recall check.** A query is tested by running it without dates, restricted to the PMIDs of its track's evidence CSV
(`AND (<pmid>[uid] OR …)`), and recorded as k of n. A query with poor recall is changed as a new line with its reason.

## Track E — 2025–2026 papers and preprints

Covered to 2026-11-03 by the track itself (bioRxiv/medRxiv from 2025-01-01, PubMed 2025–2026, Europe PMC's preprint
index). Its direct bioRxiv listing stopped at April 2026 (49,792 of 130,451 records); Europe PMC's preprint index
covered the gap.

### Queries (new, 2026-11-10)

- **E-core**, PubMed: `(longevity[tiab] OR lifespan[tiab] OR "life span"[tiab] OR centenarian*[tiab] OR nonagenarian*[tiab] OR "parental lifespan"[tiab] OR healthspan[tiab] OR "extreme longevity"[tiab] OR "exceptional longevity"[tiab]) AND (GWAS[tiab] OR "genome-wide"[tiab] OR variant*[tiab] OR polymorphism*[tiab] OR allele*[tiab] OR exome[tiab] OR "whole-genome"[tiab] OR polygenic[tiab] OR haplotype*[tiab] OR "Mendelian randomization"[tiab])`
- **E-survival**, PubMed: `("all-cause mortality"[tiab] OR survival[tiab]) AND ("genome-wide association"[tiab] OR GWAS[tiab]) AND (lifespan[tiab] OR longevity[tiab] OR "age at death"[tiab])`
- **E-somatic**, PubMed: `("clonal hematopoiesis"[tiab] OR "clonal haematopoiesis"[tiab] OR "mosaic chromosomal"[tiab] OR "loss of Y"[tiab]) AND (germline[tiab] OR inherited[tiab] OR GWAS[tiab]) AND (mortality[tiab] OR lifespan[tiab] OR longevity[tiab])`
- **E-clock**, PubMed: `("biological age"[tiab] OR "epigenetic clock"[tiab] OR "proteomic age"[tiab] OR "aging clock"[tiab]) AND (GWAS[tiab] OR "genome-wide"[tiab] OR loci[tiab])`
- **E-preprint**, Europe PMC: `(longevity OR lifespan OR centenarian OR "parental lifespan" OR healthspan) AND (GWAS OR "genome-wide" OR variant OR polymorphism OR exome OR "whole-genome" OR polygenic) AND SRC:PPR`

Added the same day, after the recall check below:

- **E-somatic-2**, PubMed, replaces E-somatic (which needed a germline term and caught 1 of track E's 37 PMIDs, none of
  its two clonal-haematopoiesis papers): `("clonal hematopoiesis"[tiab] OR "clonal haematopoiesis"[tiab] OR "mosaic chromosomal"[tiab] OR "loss of Y"[tiab]) AND (mortality[tiab] OR lifespan[tiab] OR longevity[tiab] OR inflammaging[tiab])`
- **E-heritability**, PubMed, new (E-core missed the heritability, pedigree and mtDNA papers): `(heritability[tiab] OR pedigree*[tiab] OR "polygenic"[tiab] OR mtDNA[tiab]) AND (lifespan[tiab] OR "life span"[tiab] OR longevity[tiab] OR mortality[tiab])`

**Recall on track E's evidence CSV** (37 PMIDs; 2026-11-10): E-core 29/37; E-survival 4/37; E-somatic 1/37; E-clock
2/37. E-core's misses: 40287427, 40499013, 40907250, 41610249, 41644533, 41670345, 42428085, 42660951. E-clock takes
40287427 and 42660951, E-somatic-2 takes 40499013 and 42428085, E-heritability takes 40907250, 41610249 and 41670345.
The set E-core + E-clock + E-somatic-2 + E-heritability finds 36/37; the one left out, 41644533, is a review.

E-core carries no species filter, on purpose (a `humans[mh]` filter drops papers not yet MeSH-indexed, which is most
of a three-week window); the screen removes non-human work by title and abstract.

### Runs

| Run | Window | Query | Hits | New | Queued |
|---|---|---|---|---|---|
| 2026-11-10 | 2026-10-20 → 2026-11-10 | E-core | 27 | 27 | 1 (pmid-42928374) |
| 2026-11-10 | 2026-10-20 → 2026-11-10 | E-survival | 1 (also in E-core) | 0 | 0 |
| 2026-11-10 | 2026-10-20 → 2026-11-10 | E-somatic | 1 | 1 | 0 |
| 2026-11-10 | 2026-10-20 → 2026-11-10 | E-clock | 3 | 3 | 0 |
| 2026-11-10 | 2026-10-20 → 2026-11-10 | E-preprint | 7 | 7 | 0 |
| 2026-11-10 | 2026-10-20 → 2026-11-10 | E-somatic-2 | 9 | 8 | 0 |
| 2026-11-10 | 2026-10-20 → 2026-11-10 | E-heritability | 28 | 20 | 0 |

66 unique records, listed with their verdicts in `scout/screened.md`; none was already in a track. **Not queried this
run:** the GWAS Catalog, and bioRxiv's and medRxiv's own listings (Europe PMC's preprint index stood in for both
servers). "No new locus" covers only the sources queried. Read at title level, and at abstract level where the title touched
human longevity genetics: 42986431 (review, CVD polygenic risk and lifespan; no locus), 42928381 (review,
cardiovascular resilience in centenarians; no locus), 42972028 (retinal mortality biomarker; its GWAS is a
biomarker-clock GWAS, a class track E excludes from scoring), 42928374 (queued: FURIN), and the preprint
PPR1359822 (doi 10.20944/preprints202611.0588.v1; KIR alleles in 86 Romanians aged 65–90; no controls named in the
abstract, no locus in the seed list). The clonal-haematopoiesis mortality papers from E-somatic-2 are somatic, which track E keeps out of germline
evidence. The rest are animal, plant, or non-genetic. No new locus at genome-wide significance in the sources queried.

## Track A: LongevityMap, HAGR, the v1 audit

First swept 2026-11-13. Queries, all PubMed by entry date:

- **A-resource** (written 2026-11-10, unchanged): `(LongevityMap[tiab] OR "Human Ageing Genomic Resources"[tiab] OR HAGR[tiab] OR GenAge[tiab] OR "Open Genes"[tiab]) AND (database[tiab] OR resource[tiab] OR update[tiab])`
- **A-db** (new 2026-11-13, after the recall check): `(database[ti] OR resource[ti] OR atlas[ti] OR portal[ti]) AND (aging[ti] OR ageing[ti] OR longevity[ti] OR lifespan[ti])`
- **A-pgs** (new 2026-11-13, after the recall check): `("polygenic score*"[tiab] OR "polygenic risk"[tiab] OR "polygenic propensity"[tiab] OR "polygenic prediction"[tiab] OR "polygenic lifespan"[tiab] OR PRS[tiab]) AND (longevity[tiab] OR lifespan[tiab] OR "all-cause mortality"[tiab] OR "life expectancy"[tiab])`

Track A's GWAS and sequencing papers are B's, C's and E's subject, so their queries cover them and run in those
tracks' sweeps, not here.

### Recall

On track A's 53 PMIDs (`A_longevitymap_hagr_evidence.csv`), 2026-11-13: A-resource 5/53 (the resources only), A-db
3/53, A-pgs 12/53, B-gwas 32/53, C-rare 9/53, E-core 47/53. The set A-resource + A-db + A-pgs + B-gwas + C-rare +
E-core finds 52/53; the one left out, 35324888 (sparse polygenic scores across 813 UK Biobank traits), is not a
longevity paper by its title. Before A-db, HALL (37870433) was missed; before A-pgs, five of the nine polygenic-score
papers were.

### Runs

| Run | Window | Query | Hits | New | Queued |
|---|---|---|---|---|---|
| 2026-11-13 | 2026-10-20 → 2026-11-13 | A-resource | 0 | 0 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | A-db | 5 | 5 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | A-pgs | 4 | 1 (3 already screened in track E) | 0 |

Six new records, listed with their verdicts in `scout/screened.md`, at title level: single-cell and glycoproteome
atlases (animal or tissue ageing), a Medicaid waiver study, a kidney-senescence bibliometric map, and a prostate
cancer screening model. None bears on a seed locus. The HAGR site still shows LongevityMap as "Build 3" (read
2026-11-13), so the source has not moved since the synthesis. **Not queried this run:** the Open Genes and HALL
sites, and the GWAS Catalog (B's run takes it). No new locus in the sources queried.

## Track B: common-variant GWAS of longevity and lifespan

First swept 2026-11-13. Queries:

- **B-gwas** (PubMed by entry date; written 2026-11-10, unchanged): `("genome-wide association"[tiab] OR GWAS[tiab] OR "genome-wide meta-analysis"[tiab]) AND (longevity[tiab] OR lifespan[tiab] OR "parental lifespan"[tiab] OR "parental longevity"[tiab] OR centenarian*[tiab] OR "age at death"[tiab] OR healthspan[tiab])`
- **B-catalog** (GWAS Catalog REST v2): every study under EFO_0007796 (parental longevity), OBA_VT0005372
  (longevity), EFO_0009762 (healthspan) and EFO_0005056 (age at death), from
  `https://www.ebi.ac.uk/gwas/rest/api/v2/studies?efo_id=<id>&size=200&page=<n>`. v2 gives no publication-date
  filter, so the whole list is pulled and each PubMed id checked against the tracks, the seed list and
  `scout/screened.md`.

### Recall

On track B's 55 PMIDs (`B_gwas_evidence.csv`), 2026-11-13: B-gwas 32/55, C-rare 10/55, E-core 51/55, A-pgs 15/55,
D-healthspan 14/55. Together they find 53/55. E-heritability finds a third, 41670345 (polygenic indices of 35 traits
and mortality). The one left, 35324888, is the 813-trait polygenic-score paper track A also holds. B-gwas alone misses
the healthy-ageing GWAS (35927272) and most of the polygenic-score papers.

### Runs

| Run | Window | Query | Hits | New | Queued |
|---|---|---|---|---|---|
| 2026-11-13 | 2026-10-20 → 2026-11-13 | B-gwas | 7 | 2 (5 already screened in tracks E and A) | 0 |
| 2026-11-13 | the whole Catalog list | B-catalog | 79 studies, 37 PubMed ids | 1 from 2026 (9 older ids not in any track) | 0 |

The two new B-gwas records: a maize nickel-transport GWAS, and a Lewy body disease GWAS (a disease, not longevity;
no locus to queue). The new Catalog record is pmid 42880286 (Atanur SS et al., "A phenome-wide structural variant map
from 467,152 UK Biobank genomes", *Cell*, 2026 Oct 15, doi 10.1016/j.cell.2026.09.035), study GCST90939774, "Age at
death (structural variant analysis)", 442,634 Europeans: the Catalog lists **no** association for it, so no locus
to queue; whether any structural variant came near genome-wide significance for age at death is unknown short of its
summary statistics. The nine older ids (2007–2022: 17903295, 20834067, 21612516, 22533364, 32772156, 32915819,
34662886, 34737426, 35748965) predate the tracks' window; they are the tracks' gaps, not new papers, and are listed
here for the curator rather than queued. No new locus in the sources queried.

## Track C: rare and protective variants, centenarian sequencing

First swept 2026-11-13. The synthesis states its scope as "2015–2026" and no date it covered to, so the window
below is the same as A's and B's; anything between its last search and 2026-10-20 is unknown, not covered. Queries,
all PubMed by entry date:

- **C-rare** (written 2026-11-10, unchanged): `(exome[tiab] OR "whole-genome sequencing"[tiab] OR "rare variant*"[tiab] OR "loss-of-function"[tiab] OR "protective variant*"[tiab]) AND (centenarian*[tiab] OR longevity[tiab] OR lifespan[tiab] OR "long-lived"[tiab] OR supercentenarian*[tiab])`
- **C-protect** (new 2026-11-13; run once, then replaced by C-protect-2 for its noise): `(protective[tiab] OR "loss-of-function"[tiab] OR resistance[tiab] OR resilience[tiab] OR deficiency[tiab] OR heterozygo*[tiab]) AND (Christchurch[tiab] OR APOE[tiab] OR ANGPTL3[tiab] OR APOC3[tiab] OR ASGR1[tiab] OR PCSK9[tiab] OR Klotho[tiab] OR "KL-VS"[tiab] OR Reelin[tiab] OR "Laron"[tiab] OR GHR[tiab])`
- **C-protect-2** (new 2026-11-13, for the next runs): C-protect `AND (carrier*[tiab] OR variant*[tiab] OR allele*[tiab] OR mutation*[tiab] OR heterozygo*[tiab] OR homozygo*[tiab]) NOT (mice[ti] OR mouse[ti] OR rat[ti] OR rats[ti])`. Recall 20/94 against C-protect's 21; hits in this window 18 against 50.
- **C-mito** (new 2026-11-13): `("mitochondrial DNA"[tiab] OR mtDNA[tiab] OR haplogroup*[tiab]) AND (longevity[tiab] OR lifespan[tiab] OR mortality[tiab] OR centenarian*[tiab] OR frailty[tiab] OR penetrance[tiab])`
- **C-monogenic** (new 2026-11-13): `("genotype-first"[tiab] OR penetrance[tiab] OR "pathogenic variant*"[tiab]) AND (mortality[tiab] OR survival[tiab] OR lifespan[tiab]) AND (exome[tiab] OR "whole-genome"[tiab] OR "whole genome"[tiab] OR biobank[tiab])`
- **C-somatic-germline** (new 2026-11-13): `("clonal hematopoiesis"[tiab] OR "clonal haematopoiesis"[tiab] OR "loss of Y"[tiab] OR "Y chromosome loss"[tiab] OR "mosaic chromosomal"[tiab] OR "telomere length"[tiab] OR "mtDNA mutation*"[tiab] OR "mtDNA copy"[tiab]) AND (GWAS[tiab] OR "genome-wide"[tiab] OR "whole genome*"[tiab] OR "whole-genome"[tiab] OR germline[tiab] OR inherited[tiab])`

### Recall

On track C's 94 PMIDs (`C_rare_protective_evidence.csv`), 2026-11-13, cumulative in this order: B-gwas 15, C-rare 33,
E-core 62, E-somatic-2 65, E-heritability 71, C-protect 82, C-mito 83, C-monogenic 85, C-somatic-germline 91. C-rare
alone finds 27/94: track C is mostly disease-protective variants (APOE Christchurch, ANGPTL3, APOC3, KL-VS), clonal
haematopoiesis and mtDNA, which name no longevity term. Left out: a single supercentenarian's clonal haematopoiesis
(33184493), an ancient polymorphic deletion's evolutionary history (34559564), and a mosaic-Y-loss GWAS (31748747,
"mosaic Y chromosome loss" matches none of the phrases).

### Runs

| Run | Window | Query | Hits | New | Queued |
|---|---|---|---|---|---|
| 2026-11-13 | 2026-10-20 → 2026-11-13 | C-rare | 10 | 7 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | C-protect | 50 | 50 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | C-mito | 14 | 5 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | C-monogenic | 5 | 5 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | C-somatic-germline | 15 | 13 | 0 |

80 new records, in `scout/screened.md`, at title level. Most are animal or mechanistic work (mouse APOE Christchurch,
Klotho reviews, atherosclerosis models). The human genetic ones are disease genetics with no longevity phenotype
(APOE ε4 and amyloid, PCSK9 variants and LDL uptake, lipid-gene SNPs and cardiovascular risk, ApoE in type 2
diabetes, monogenic disease reports) or germline studies of somatic traits (the Mount Sinai Million clonal
haematopoiesis landscape, 42990510; telomere-length Mendelian randomization papers). None bears on a seed locus as
longevity evidence. No new locus in the sources queried.

## Track D: healthspan, ageing rate, heritability

First swept 2026-11-13. The synthesis states its scope as "2018–2026" and no date it covered to, so anything
between its last search and 2026-10-20 is unknown, not covered. Queries, all PubMed by entry date:

- **D-healthspan** (written 2026-11-10, unchanged): `(healthspan[tiab] OR frailty[tiab] OR "intrinsic capacity"[tiab] OR "healthy aging"[tiab] OR "healthy ageing"[tiab] OR "telomere length"[tiab]) AND ("genome-wide"[tiab] OR GWAS[tiab] OR "Mendelian randomization"[tiab] OR heritability[tiab])`
- **D-clocks** (new 2026-11-13): `("age acceleration"[tiab] OR "brain age"[tiab] OR "organ age"[tiab] OR "organ aging"[tiab] OR "organ-specific aging"[tiab] OR "proteomic aging"[tiab] OR "proteomic clock"[tiab] OR "aging clock"[tiab] OR "biological age"[tiab] OR "epigenetic age"[tiab] OR "aging signatures"[tiab]) AND (GWAS[tiab] OR "genome-wide"[tiab] OR loci[tiab] OR "genetic architecture"[tiab] OR proteom*[tiab] OR mortality[tiab])`
- **D-multimorbidity** (new 2026-11-13; run once, then replaced by D-multimorbidity-2: "resilience" alone took in plant and livestock genomics): `(multimorbidity[tiab] OR resilience[tiab] OR "aging-related outcomes"[tiab] OR "intrinsic capacity"[tiab]) AND (GWAS[tiab] OR "genome-wide"[tiab] OR "Mendelian randomization"[tiab] OR polygenic[tiab])`
- **D-multimorbidity-2** (new 2026-11-13, for the next runs): `(multimorbidity[tiab] OR "cognitive resilience"[tiab] OR "resilience to"[tiab] OR "aging-related outcomes"[tiab] OR "intrinsic capacity"[tiab]) AND (GWAS[tiab] OR "genome-wide"[tiab] OR "Mendelian randomization"[tiab] OR polygenic[tiab]) AND (human*[tiab] OR participant*[tiab] OR individuals[tiab] OR adults[tiab] OR biobank[tiab])`. Recall 6/60 against 7; hits in this window 5 against 40.

Track D's germline studies of mosaic loss, mtDNA copy number and telomeres are also C-somatic-germline's (track C).

### Recall

On track D's 60 PMIDs (`D_healthspan_evidence.csv`), 2026-11-13, cumulative: A-pgs 6, B-gwas 19, D-healthspan 30,
E-core 35, E-heritability 39, E-clock 41, C-somatic-germline (with `mosaic[ti] OR "copy number"[tiab] OR
heteroplasmy[tiab]` added for this check) 44, D-clocks 54, D-multimorbidity 58. Left out: the two mosaic-Y-loss GWAS
(31748747, 28346444), whose abstracts pair "Y chromosome loss" with "genetic variants" or "predisposition", which the
germline clause does not name.

### Runs

| Run | Window | Query | Hits | New | Queued |
|---|---|---|---|---|---|
| 2026-11-13 | 2026-10-20 → 2026-11-13 | D-healthspan | 8 | 3 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | D-clocks | 43 | 36 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | D-multimorbidity | 40 | 37 | 0 |

76 new records, in `scout/screened.md`, at title level. D-clocks' are biological-age, clock and organ-age studies
and reviews, none with a germline locus (the track E rule keeps clock GWAS out of scoring in any case); D-multimorbidity's
are mostly plant and livestock genomics, plus a migraine GWAS and two Mendelian randomization papers. None bears on a
seed locus. No new locus in the sources queried.

## Tracks F–K

First swept 2026-11-13, each with the query written 2026-11-10 (in the table's list below, unchanged) over
2026-10-20 → 2026-11-13; for F, H and K the date the synthesis covered to is unknown, so the gap before 2026-10-20 is
unknown, not covered. Two queries are new:

- **S-seedgene** (new 2026-11-13, a watch across tracks, the scout's own aim): any of the 176 gene symbols named in
  `seed_variants.csv` (its `genes` column, free-text words, lncRNA and pseudogene names and variant labels dropped; the
  list is regenerated from the CSV at each run), in title or abstract, `AND (longevity[tiab] OR lifespan[tiab] OR "life span"[tiab] OR centenarian*[tiab] OR "age at death"[tiab] OR healthspan[tiab] OR "all-cause mortality"[tiab] OR pleiotrop*[tiab] OR "trade-off"[tiab] OR "phenome-wide"[tiab]) AND (variant*[tiab] OR allele*[tiab] OR polymorphism*[tiab] OR genotype*[tiab] OR carrier*[tiab] OR haplotype*[tiab])`. Too long for a GET: sent by POST.
- **J-seedgene** (new 2026-11-13): the same gene list `AND (lifespan[tiab] OR "life span"[tiab] OR longevity[tiab] OR aging[tiab] OR ageing[tiab]) AND (mice[tiab] OR mouse[tiab] OR "C. elegans"[tiab] OR "Caenorhabditis elegans"[tiab] OR Drosophila[tiab] OR yeast[tiab] OR zebrafish[tiab] OR knockout[tiab] OR transgenic[tiab])`. Noisy: short symbols (MAPT, CGAS) pull in mechanistic ageing work.

### Recall

On each track's PMIDs, 2026-11-13, the track's own query, then cumulative with B-gwas, A-pgs, E-core, D-healthspan
and E-heritability (and H-pleiotropy plus S-seedgene where named):

| Track | PMIDs | Own query | With the shared queries | With H-pleiotropy, S-seedgene / J-seedgene |
|---|---|---|---|---|
| F | 68 | 1 | 20 | not run |
| G | 87 | 0 | 25 | not run |
| H | 79 | 7 | 47 | 49 |
| I | 139 | 39 | 100 | not run |
| J | 94 | 14 | 43 | 48 (J-seedgene) |
| K | 70 | 9 | 50 | 53 |

Recall is low for F and G on purpose, not by accident: their evidence is the general literature on reporting
polygenic scores and direct-to-consumer tests (guidelines, position statements) and on fine-mapping, colocalisation
and effector-gene methods, none of it about longevity. A new paper there changes how a row is evaluated or reported,
not which loci there are, so the scout does not chase it; a seat that wants those fields watched asks for a query of
its own. H's and K's misses are disease-specific trade-off papers (APOE, PCSK9, IL6R, SH2B3, Klotho) and familial-
longevity scores; S-seedgene catches a few, and its recall is limited by the tracks citing disease phenotypes
(Alzheimer's, coronary disease) that its longevity clause leaves out. J's misses are model-organism papers naming a
gene with no lifespan word.

### Runs

| Run | Window | Query | Hits | New | Queued |
|---|---|---|---|---|---|
| 2026-11-13 | 2026-10-20 → 2026-11-13 | S-seedgene | 12 | 10 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | F-reporting | 2 | 2 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | G-finemap | 15 | 15 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | H-pleiotropy | 7 | 5 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | I-concepts | 26 | 18 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | J-models | 14 | 10 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | J-seedgene | 21 | 20 | 0 |
| 2026-11-13 | 2026-10-20 → 2026-11-13 | K-age | 2 | 1 | 0 |

81 new records, in `scout/screened.md`, at title level: reviews, mechanistic and animal ageing work, and trait genetics
(Mendelian randomization and genomic SEM of vascular, adipose and bone ageing) with no longevity locus. One is noted
for track J and not queued: pmid 42995887, "STING deficiency extends median lifespan and mitigates age-related liver
pathology in mice"; STING is cGAS's partner and CGAS is a seed gene, but the paper tests no human variant. No new locus
in the sources queried.

### The queries as written 2026-11-10

Written 2026-11-10 for tracks A–D and F–K; every one was run and recall-checked 2026-11-13 (each track's section
above says what changed). All PubMed by entry date, as above.

| Track | Subject | Sources the synthesis names | Covered to (as it states) |
|---|---|---|---|
| A | LongevityMap, HAGR, the v1 audit | PubMed, HAGR site and Build 3, GWAS Catalog v2, Open Genes, HALL | 2026-11-03 (live site checked); swept 2026-11-13, above |
| B | common-variant GWAS of longevity and lifespan | PubMed, Crossref, GWAS Catalog v2, PGS Catalog | 2026-11-03 (Catalog pulled); swept 2026-11-13, above |
| C | rare and protective variants, centenarian sequencing | PubMed, Europe PMC, Crossref | unknown (scope "2015–2026"); swept 2026-11-13, above |
| D | healthspan, ageing rate, heritability | PubMed, Crossref, GWAS Catalog v2 REST | unknown (scope "2018–2026"); swept 2026-11-13, above |
| F | reporting to three audiences | PubMed, Crossref, product pages | unknown; swept 2026-11-13, above |
| G | evaluating SNP-level associations | PubMed, Open Targets 26.09 | 2026-11-03 (titles checked); swept 2026-11-13, above |
| H | pleiotropy and context | PubMed, Open Targets | unknown; swept 2026-11-13, above |
| I | concepts and architecture | PubMed | 2026-11-03; swept 2026-11-13, above |
| J | model organisms | PubMed, Europe PMC, GenAge Build 21, Open Genes API | 2026-11-03; swept 2026-11-13, above |
| K | definitions and age of action | PubMed, Timmers 2019 source data | unknown; swept 2026-11-13, above |

- **A-resource**: `(LongevityMap[tiab] OR "Human Ageing Genomic Resources"[tiab] OR HAGR[tiab] OR GenAge[tiab] OR "Open Genes"[tiab]) AND (database[tiab] OR resource[tiab] OR update[tiab])`
- **B-gwas**: `("genome-wide association"[tiab] OR GWAS[tiab] OR "genome-wide meta-analysis"[tiab]) AND (longevity[tiab] OR lifespan[tiab] OR "parental lifespan"[tiab] OR "parental longevity"[tiab] OR centenarian*[tiab] OR "age at death"[tiab] OR healthspan[tiab])`;
  plus the GWAS Catalog's studies for EFO_0007796, OBA_VT0005372, EFO_0009762 and EFO_0005056, by publication date.
- **C-rare**: `(exome[tiab] OR "whole-genome sequencing"[tiab] OR "rare variant*"[tiab] OR "loss-of-function"[tiab] OR "protective variant*"[tiab]) AND (centenarian*[tiab] OR longevity[tiab] OR lifespan[tiab] OR "long-lived"[tiab] OR supercentenarian*[tiab])`
- **D-healthspan**: `(healthspan[tiab] OR frailty[tiab] OR "intrinsic capacity"[tiab] OR "healthy aging"[tiab] OR "healthy ageing"[tiab] OR "telomere length"[tiab]) AND ("genome-wide"[tiab] OR GWAS[tiab] OR "Mendelian randomization"[tiab] OR heritability[tiab])`
- **F-reporting**: `("polygenic score*"[tiab] OR "polygenic risk"[tiab] OR "genetic risk"[tiab] OR "direct-to-consumer"[tiab]) AND (report*[tiab] OR communicat*[tiab] OR understanding[tiab]) AND (longevity[tiab] OR lifespan[tiab] OR aging[tiab] OR ageing[tiab])`
- **G-finemap**: `("fine-mapping"[tiab] OR "credible set*"[tiab] OR colocali*[tiab] OR "effector gene*"[tiab] OR "locus-to-gene"[tiab]) AND (longevity[tiab] OR lifespan[tiab] OR aging[tiab] OR ageing[tiab])`
- **H-pleiotropy**: `(pleiotrop*[tiab] OR "antagonistic pleiotropy"[tiab] OR "phenome-wide"[tiab] OR PheWAS[tiab] OR "gene-environment"[tiab]) AND (longevity[tiab] OR lifespan[tiab] OR "parental lifespan"[tiab])`
- **I-concepts**: `(longevity[tiab] OR lifespan[tiab] OR centenarian*[tiab]) AND (genetic*[tiab] OR heritab*[tiab]) AND (review[pt] OR "meta-analysis"[pt] OR architecture[tiab] OR "familial longevity"[tiab])`
- **J-models**: `(mouse[tiab] OR mice[tiab] OR "knock-in"[tiab] OR "Caenorhabditis elegans"[tiab] OR Drosophila[tiab]) AND lifespan[tiab] AND (human[tiab] OR GWAS[tiab] OR "human allele"[tiab] OR humanized[tiab] OR humanised[tiab])`
- **K-age**: `(longevity[tiab] OR lifespan[tiab] OR mortality[tiab]) AND ("age-dependent"[tiab] OR "age-varying"[tiab] OR "age of onset"[tiab] OR "age-specific"[tiab] OR "age at death"[tiab]) AND (allele*[tiab] OR variant*[tiab] OR polygenic[tiab] OR GWAS[tiab])`
