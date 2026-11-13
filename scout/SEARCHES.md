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

## Tracks C–D, F–K

Not yet swept. Their queries below are **new**, written 2026-11-10, and **not yet run or recall-checked**; the
first run of each checks its recall on its track's CSV and may change them. All PubMed by entry date, as above.

| Track | Subject | Sources the synthesis names | Covered to (as it states) |
|---|---|---|---|
| A | LongevityMap, HAGR, the v1 audit | PubMed, HAGR site and Build 3, GWAS Catalog v2, Open Genes, HALL | 2026-11-03 (live site checked); swept 2026-11-13, above |
| B | common-variant GWAS of longevity and lifespan | PubMed, Crossref, GWAS Catalog v2, PGS Catalog | 2026-11-03 (Catalog pulled); swept 2026-11-13, above |
| C | rare and protective variants, centenarian sequencing | PubMed, Europe PMC, Crossref | unknown (scope "2015–2026") |
| D | healthspan, ageing rate, heritability | PubMed, Crossref, GWAS Catalog v2 REST | unknown (scope "2018–2026") |
| F | reporting to three audiences | PubMed, Crossref, product pages | unknown |
| G | evaluating SNP-level associations | PubMed, Open Targets 26.09 | 2026-11-03 (titles checked) |
| H | pleiotropy and context | PubMed, Open Targets | unknown |
| I | concepts and architecture | PubMed | 2026-11-03 |
| J | model organisms | PubMed, Europe PMC, GenAge Build 21, Open Genes API | 2026-11-03 |
| K | definitions and age of action | PubMed, Timmers 2019 source data | unknown |

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
