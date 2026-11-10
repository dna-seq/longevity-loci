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
evidence or candidate CSV, nor in the seed list.

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

38 unique records; none was already in a track. Read at title level, and at abstract level where the title touched
human longevity genetics: 42986431 (review, CVD polygenic risk and lifespan; no locus), 42928381 (review,
cardiovascular resilience in centenarians; no locus), 42972028 (retinal mortality biomarker; its GWAS is a
biomarker-clock GWAS, a class track E excludes from scoring), 42928374 (queued: FURIN), and the preprint
PPR1359822 (doi 10.20944/preprints202611.0588.v1; KIR alleles in 86 Romanians aged 65–90; no controls named in the
abstract, no locus in the seed list). The rest are animal, plant, or non-genetic. No new locus at genome-wide
significance.

## Tracks A–D, F–K

Not yet swept. Their queries are to be written when each comes up, oldest first; every one is covered to an
unknown date or to 2026-11-03.

| Track | Subject | Covered to (as the synthesis states) |
|---|---|---|
| A | LongevityMap, HAGR, the v1 audit | 2026-11-03 (live site checked) |
| B | common-variant GWAS of longevity and lifespan | 2026-11-03 (GWAS Catalog v2 pulled) |
| C | rare and protective variants, centenarian sequencing | unknown (scope "2015–2026") |
| D | healthspan, ageing rate, heritability | unknown (scope "2018–2026") |
| F | reporting to three audiences | unknown |
| G | evaluating SNP-level associations | 2026-11-03 (titles checked) |
| H | pleiotropy and context | unknown |
| I | concepts and architecture | 2026-11-03 |
| J | model organisms | 2026-11-03 |
| K | definitions and age of action | unknown |
