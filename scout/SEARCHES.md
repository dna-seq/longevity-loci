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

## Backfill, 2015-01-01 → 2026-10-20 (run 2026-11-17)

Asked by the lead for the person (#longevity-loci>scout, 2026-11-17): the window first set at 2023, then moved to
2015-01-01, the year of LongevityMap Build 3's newest PMID (Build 3 released 2017-06-24). Every current query (A–K,
the E set, S-seedgene, J-seedgene) by entry date in three windows, Europe PMC's preprint index (E-preprint) over the
same windows, and medRxiv's own listing from 2026-04-01. Every record with its verdict and its depth is in
`scout/backfill_2015_2026.tsv` (rule-dropped rows carry no title); `scout/screened.md` is not repeated there. PubMed
counts hits per query, before dedupe (a record found by two queries counts twice):

| Query | 2015-01-01 → 2017-06-24 | 2017-06-25 → 2022-12-31 | 2023-01-01 → 2026-10-20 |
|---|---|---|---|
| A-db | 24 | 86 | 190 |
| A-pgs | 7 | 93 | 196 |
| A-resource | 1 | 13 | 26 |
| B-gwas | 60 | 206 | 261 |
| C-mito | 153 | 459 | 477 |
| C-monogenic | 12 | 123 | 202 |
| C-protect-2 | 400 | 984 | 899 |
| C-rare | 121 | 280 | 317 |
| C-somatic-germline | 180 | 658 | 777 |
| D-clocks | 50 | 463 | 1103 |
| D-healthspan | 94 | 311 | 667 |
| D-multimorbidity-2 | 4 | 43 | 138 |
| E-clock | 15 | 99 | 151 |
| E-core | 573 | 1535 | 1538 |
| E-heritability | 289 | 913 | 1248 |
| E-preprint (Europe PMC) | 0 | 667 | 977 |
| E-somatic-2 | 7 | 144 | 249 |
| E-survival | 12 | 31 | 25 |
| F-reporting | 27 | 146 | 209 |
| G-finemap | 82 | 277 | 411 |
| H-pleiotropy | 96 | 235 | 223 |
| I-concepts | 337 | 877 | 908 |
| J-models | 352 | 907 | 880 |
| J-seedgene | 338 | 990 | 1252 |
| K-age | 32 | 107 | 148 |
| S-seedgene | 181 | 520 | 537 |
| **hits** | 3,447 | 11,167 | 14,009 |
| **distinct records** | 2,753 | 8,982 | 11,024 |
| known (cited by a row, in a track's CSV or in `screened.md`) | 43 | 120 | 162 |
| dropped by the fixed rule, not read | 2,025 | 6,606 | 8,195 |
| read (title or abstract) | 669 | 2,231 | 2,661 |
| queued | 16 | 25 | 6 |

The last four rows are after the rule fix of 2026-11-18 (below); the first count (c0a8726) had 2,041 / 6,666 / 8,235 dropped.

The 2017–2022 window's E-preprint row includes 2017-06-25 → 2022-12-31 only; Europe PMC's preprint index holds none
before mid-2017 for this query. Recall per query is unchanged from 2026-11-13 (recall has no date limit).

**How the records were read.**

1. **Abstracts.** All of them came from `efetch`, 21,056 of 21,127 PMIDs (the 71 without an abstract were read by
   title).
2. **The rule.** Each record was classed by rule, in this order:
   - a row's rsID in the abstract: flagged;
   - non-human (MeSH Animals without Humans, or a non-human organism in a record without MeSH): dropped;
   - genome-wide design plus a longevity term: flagged;
   - genome-wide design plus an ageing-marker term only: flagged;
   - a row's gene plus a longevity or marker term plus a genetic term: flagged;
   - no longevity or marker term: dropped;
   - no genetic term: dropped.

   The terms:
   - **longevity:** lifespan, longevity, centenarian, age at death, parental lifespan, healthspan, all-cause
     mortality, survival to an extreme age;
   - **marker:** telomere length, frailty, epigenetic clock or age, brain age, biological age, mtDNA copy number,
     loss of Y.

   What is left (longevity and genetic, with neither a genome-wide design nor a row gene) went to title reading.
3. **The rule fix, 2026-11-18** (the lead, D41: four of the eight calibration misses were faults, not scope).
   - **Zenin 2019 and Codd 2021 (telomere length).** Neither abstract says "genome-wide" or "GWAS", only "loci".
     The design test now also accepts loci or locus within a sentence of associated, identified, significant, novel
     or new, plus "association study", "genetic architecture", "summary statistics" and "SNP-based heritability".
   - **The mtDNA copy-number cohort (37255673).** Its MeSH has Animals and no Humans. MeSH no longer decides alone:
     a record is non-human only when it names a non-human organism, or carries animal-only MeSH, **and** has none of
     human, patient(s), participant(s), biobank, people, persons, centenarians, nonagenarians, women, men, adults,
     children, ancestry, population-based.
   - **The result.** All 22,759 records were classed again. 54 of the 58 row-cited papers now pass. The 4 still
     dropped are the three APOE or Klotho papers on Alzheimer's or cognition and the somatic scan, out of scope by the
     lead's word.
   - **The re-read.** 235 records the fix newly flagged, never read at abstract level before, were read to the end by
     two readers, by hand: 6 candidates, none new to the queue.
   - **The title batches.** The three title batches whose readers had set defaults by script (1,991 titles) were
     re-read title by title, by hand: 46 candidates.
   - **The scout's read.** The scout read every candidate not already decided: seven abstracts. Two were added to
     the queue (31585002 under row 96, 27714549 under row 73), and five fail the rule. The five are a genetic score
     with no row variant on its own (40598362), a review (30864497), an expression pilot with no outcome difference
     (31504207), candidate genes without a row (29300832), and Y haplogroups (35861954).
4. **Calibration** (the first rule). The rule was tested on the 58 row-cited PMIDs that fall in the windows: 50 are flagged. Of the
   8 dropped, 4 had no longevity or marker term (three APOE or Klotho papers on Alzheimer's or cognition, and the
   somatic-mutation scan), 3 were in the title-read class (Zenin 2019, a telomere-length paper, a mouse longevity
   GWAS), and 1 was misread as non-human (an mtDNA copy-number cohort).
5. **Readers.** 2,743 flagged records (abstract) and 2,770 title-class records went to 18 reader agents. They wrote one
   verdict per record and returned 308 candidates. Their depth varied:
   - some read whole abstracts;
   - some read the first 550–1,100 characters, and the rest only for doubtful records;
   - three of the four title readers set defaults by script and judged only their candidates one by one.

   The tsv says "abstract, reader" or "title, reader" for these. It is not a scout's verdict.
6. **The scout's own reading.**
   - Every CAND-A abstract (69) was read whole.
   - Every CAND-B was read by title and the reader's reason, and the queued ones by abstract.
   - Preprints and corrections were matched to their published versions through Europe PMC: 20 records turned out
     to be versions of papers already known (the "known by version" verdict).
   - PubMed indexes medRxiv preprints with PMIDs. 39132489 is the medRxiv version of Park 2025 (40021682), which
     rows cite.

**Queued** (`scout/queue.md`, 2026-11-17): the Catalog entry (thirteen non-seed lines, above); two loci outside every seed, at abstract depth, both needing the full text
for significance: rs1927465 between CYP26A1 and MYOF (Yashin 2018, LLFS, replicated in HRS) and Kashtanova 2026's WGS
of 3,703 adults aged 90+ (CFAP46, MYO18B, TBC1D28). Then 45 uncited papers on 18 rows (row 38 named beside 159; two added after the rule fix), one entry per row or group:
APOE 10 and a preprint, FOXO3 11, KL 6, ABO 2, LPA 2, CETP 2, IL6 3 (other promoter SNPs), the telomere-length rows 3, HLA-DQB1 2, and one
each for TFAM, CELSR2, EBF1, FTO, HTT, CDKN2B-AS1 and CHRNB4.

**The cut for rule (b).** The readers returned 239 CAND-B lines. 43 went to the queue (one more, a medRxiv preprint, came
from the listing). The rule was: the row's own variant or gene, against lifespan, longevity, survival to old age or
all-cause mortality, in a population or longevity cohort; or functional work on the row's exact variant. What was
cut, with its reason:

- ageing-marker associations (telomere length, clocks, brain age, frailty) at rows outside the marker section, and
  small telomere-length replications at the marker rows;
- disease-cohort mortality (dialysis, cancer, heart failure, Huntington's, Down syndrome);
- interaction-only and Mendelian-randomisation designs;
- cognition or dementia outcomes;
- frequency remarks without a test;
- corrections and preprints of known papers.

The lead asked for "any paper", so the cut is the scout's call. Every cut record is in the tsv with "CAND-B, not
queued".

**Checks on the readers.**

- **Sample.** An independent second reader took 100 records drawn at random (seed 20261117) from the 2,417 flagged
  records the readers rejected, and read each abstract whole. It found 0 misses and 5 borderline records, all
  telomere-length studies (37487414, 38789417, 41965821, 28447668, 40844718).
- **Alias rescan.** The gene pattern missed aliases: KL (two letters), FOXO3A, ApoE, IL-6, Lp(a), TOMM40, APOC1,
  SH2B3, CHRNA3/5, CDKN2A, 9p21, huntingtin. A rescan with them, plus a longevity and a genetic term, ran over every
  non-candidate record: 373 hits.
  - 266 had already been read at abstract level by a reader.
  - The 107 seen only by title or not at all were read by title. None ties a row variant to a lifespan, longevity
    or mortality outcome; they are Klotho and cognition papers, ApoE and brain studies, and mouse work.
  - One Klotho paper, 32444684, was added to row 73's entry.
- **Records without text.** Records with neither title nor abstract are "unknown" in the tsv, not a verdict.

**Read, not queued.** The judgement calls, with the reason for each:

- **Gene-level burden genes.** The exome PTV-burden genes for lifespan (Liu 2022, 37117740: BRCA2, BRCA1, TET2, PPM1D,
  LDLR, EML2, DEDD2) and Park 2025's (40021682: TET2, ATM, BRCA1, BRCA2, ASXL1, CKMT1B; SKAT-O C1orf52, IDH2, RLIM).
  - Both papers are already in track C's candidate CSV, marked "non-rsID / gene-level".
  - The CNV scans are the same non-SNP case: Danish nonagenarians' CNVs and mortality (26446717), Han Chinese
    long-lived CNVs (29883365).
  - No seed is gene-level. The lead decided 2026-11-18 (D41): no rows for gene-level, CHIP, SV or CNV hits; one is
    named in a row's prose only where a row exists.
- **Transcriptome and MR studies.**
  - Lifespan TWAS: TOMM40 and COASY, PPR1225305; haptoglobin, PPR185888.
  - Blood eQTL lifespan genes: 32358504.
  - MR on telomere length, clocks and frailty (533 records).
  - None is a variant at genome-wide significance.
- **Not genome-wide.** Candidate-gene longevity studies of genes without a row: BPIFB4, PLCG2 P522R, SIRT6, SMAD3,
  IGF1 coding variants, d3GHR, UCP2, SERPINE1 null (Amish), CCR5-Δ32, ERAP2. None was genome-wide.
- **Dementia-free survival.** Being dementia-free at 85 (42024100: MAL2, GCH1) is a dementia-resilience outcome, not
  lifespan or healthspan.
- **Ageing-marker GWAS.**
  - Clocks, telomere length, brain age, frailty and organ age, unless the abstract named a row's variant.
  - Japanese centenarians (PPR835001, CentPGS): no locus beyond APOE named; no published version found.

**The nine pre-2023 GWAS Catalog ids** (Track B, Runs). Their studies under the four EFO terms (EFO_0007796,
OBA_VT0005372, EFO_0009762, EFO_0005056) were listed with `/api/v2/studies?pubmed_id=` and their associations with
`/api/v2/associations?accession_id=`, 2026-11-17. None holds an association at P ≤ 5e-8 for lifespan, longevity,
healthspan or death:

- **17903295**, Framingham 100K: **corrected the same day.** The four-term listing showed only GCST000096, whose one
  line at 1e-8 is rs10496265 for age at menopause. Its other study, GCST000103 (morbidity-free survival, 558 people),
  is mapped outside the four terms and holds rs32566 and rs1412337 at 2e-9 each. Both are queued with the Catalog
  entry below. The first verdict, "no genome-wide line", was wrong for this id.
- **20834067, 21612516, 22533364**, small longevity scans: none genome-wide.
- **32772156**, SCZ and BD by parental lifespan: no associations listed.
- **32915819**, a German cohort's "Death": no associations listed.
- **34662886**, the UK Biobank phenome-wide parental-alive fields: no associations listed under these terms.
- **34737426**, the same, mother and father still alive: no associations listed under these terms.
- **35748965**, Finnish healthspan: 11 associations, none genome-wide.

Apart from 17903295's two lines, not a missed locus.

**The Catalog by position** (the lead's rule a, per locus rather than per paper):

- Every association at P ≤ 5e-8 in the 77 studies under the four terms (181 lines, plus GCST000103's two) was
  compared by GRCh38 position with the seed list (positions checked: rs429358 is 19:44,908,684 in both) and with
  the rows' stated positions.
- 149 lines sit at a seed or row rsID, 15 within 500 kb of a seed, and 6 carry no chromosome. Five of those six are
  Wright 2019's `im:` lines; read as positions, their numbers fall at seeds 80, 57 and 46, but that is inferred from
  the number alone.
- Thirteen lines are 1.2 Mb or more from any seed. Six are in no track and seven are in track B's
  `B_gwascatalog_gw_leads.csv` but were not seeded. All thirteen are queued as one entry for the curator and lead.
- Position checks on the two other new-locus entries: rs1927465 and Kashtanova's genes were compared by name only
  (the abstracts give no positions).

**Atanur 2026** (pmid 42880286, *Cell*, the structural-variant PheWAS of 467,152 UK Biobank genomes):

- The Catalog lists its "Age at death (structural variant analysis)" study, GCST90939774, with no association.
- The abstract (`loci fetch`, abstract only) does not mention age at death.
- So whether any structural variant reached significance for age at death is **unknown**, not none. Its
  supplementary tables settle it. Nothing to queue.

**medRxiv's own listing**, 2026-04-01 → 2026-11-17 (`https://api.biorxiv.org/details/medrxiv/2026-04-01/2026-11-17/<cursor>`):

- 14,210 records, 11,999 DOIs; 84 matched a longevity and a genetic term. They are in the tsv, `medrxiv` in the
  queries column.
- All 84 were read by title, and four by abstract. One was queued under row 96:
  10.64898/2026.06.18.26355781, ApoE ε4 against incident dementia or death in the Million Veteran Program.
- Alvarez Sirvent 2026 is the one already closed.
- 10.64898/2026.11.10.26365445 ("Enrichment of Rare Exonic Variants in Cognitive Superagers from Centenarian Families",
  posted 2026-11-12) is very likely PPR1366192's work. The two are not yet matched; matching them is the next E run's
  task.

**bioRxiv's own listing**, same interval: restarted 2026-11-17 in month chunks that each write a file. **Not
screened** at this commit, which leaves it unknown, not zero.

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
| 2026-11-14 | 2026-10-27 → 2026-11-14 | E-core | 26 | 6 | 0 |
| 2026-11-14 | 2026-10-27 → 2026-11-14 | E-survival | 0 | 0 | 0 |
| 2026-11-14 | 2026-10-27 → 2026-11-14 | E-clock | 8 | 2 | 0 |
| 2026-11-14 | 2026-10-27 → 2026-11-14 | E-somatic-2 | 9 | 2 | 0 |
| 2026-11-14 | 2026-10-27 → 2026-11-14 | E-heritability | 22 | 2 | 0 |
| 2026-11-14 | 2026-10-27 → 2026-11-14 | E-preprint | 7 | 2 | 0 |
| 2026-11-14 | 2026-10-27 → 2026-11-14 | S-seedgene | 9 | 0 | 0 |
| 2026-11-17 | 2026-10-31 → 2026-11-17 | E-core | 24 | 4 | 0 |
| 2026-11-17 | 2026-10-31 → 2026-11-17 | E-survival | 0 | 0 | 0 |
| 2026-11-17 | 2026-10-31 → 2026-11-17 | E-clock | 8 | 0 | 0 |
| 2026-11-17 | 2026-10-31 → 2026-11-17 | E-somatic-2 | 10 | 2 | 0 |
| 2026-11-17 | 2026-10-31 → 2026-11-17 | E-heritability | 15 | 1 | 0 |
| 2026-11-17 | 2026-10-31 → 2026-11-17 | E-preprint | 8 | 1 | 0 (1 queued from the version check below) |

66 unique records, listed with their verdicts in `scout/screened.md`; none was already in a track. **Not queried this
run:** the GWAS Catalog, and bioRxiv's and medRxiv's own listings (Europe PMC's preprint index stood in for both
servers). "No new locus" covers only the sources queried. Read at title level, and at abstract level where the title touched
human longevity genetics: 42986431 (review, CVD polygenic risk and lifespan; no locus), 42928381 (review,
cardiovascular resilience in centenarians; no locus), 42972028 (retinal mortality biomarker; its GWAS is a
biomarker-clock GWAS, a class track E excludes from scoring), 42928374 (queued: FURIN), and the preprint
PPR1359822 (doi 10.20944/preprints202611.0588.v1; KIR alleles in 86 Romanians aged 65–90; no controls named in the
abstract, no locus in the seed list). The clonal-haematopoiesis mortality papers from E-somatic-2 are somatic, which track E keeps out of germline
evidence. The rest are animal, plant, or non-genetic. No new locus at genome-wide significance in the sources queried.

The 2026-11-14 rerun overlaps the first by two weeks (window 2026-10-27 → 2026-11-14): 75 distinct records, 61 already
screened, 14 new, listed in `scout/screened.md`. Recall on track E's 37 PMIDs unchanged (E-core 29, E-somatic-2 5,
E-heritability 11, E-clock 2, E-survival 4; S-seedgene 17). The GWAS Catalog v2 was queried this run (the four EFO ids
of track B): no study beyond the nine pre-2023 ones named under Track B. bioRxiv's and medRxiv's own listings were again
left out; Europe PMC's preprint index stood in. Read at abstract level: PPR1366192 (doi 10.64898/2026.11.10.26365445,
whole-exome sequencing of 136 cognitive superagers; rare missense variants in HLA-B and HLA-DRB1, both seed genes, but
the phenotype is cognition, no single-variant or burden test was exome-wide significant, and the abstract names no
variant: noted for the next run, not queued) and PPR1362460 (rhesus macaques; out of scope). No new locus in the
sources queried.

**Track E's preprints, checked for a published version 2026-11-14** (the 13 rows of the evidence CSV with no PMID;
the CSV's own status reads "unpublished as of 2026-11-03"). Each was checked three ways: Crossref's relation fields
(is-preprint-of, has-version), the bioRxiv/medRxiv API's `published` field, and a Europe PMC title search outside
preprints (`TITLE:(first 12 words) NOT SRC:PPR`). One is published: Chang's clonal-haematopoiesis mortality preprint
(doi 10.64898/2026.05.28.26354392) is PMID 42987714, *JACC Adv* 2026 Nov 5, doi 10.1016/j.jacadv.2026.103440,
PMC13761253 (title checked against PubMed), found by Europe PMC only; medRxiv still says NA. It is somatic, so no seed
locus. The other twelve show no published version by any of the three (Sasaki's Research Square preprint was checked
by Crossref and Europe PMC only, since the bioRxiv API does not cover Research Square). Two have newer versions than
the CSV may have read: Alvarez Sirvent 2026 (HLA-II fine-mapping) is at v2 and Salazar (TMEM106B) at v3, per the
medRxiv API; neither version was read here.

**Track E rerun, 2026-11-17** (window 2026-10-31 → 2026-11-17; S-seedgene ran the same day over 2026-10-30 → 2026-11-17
with the other tracks). Recall on track E's 37 PMIDs as before (E-core 29, E-survival 4, E-clock 2, E-somatic-2 5,
E-heritability 11). 59 distinct records, 51 already screened, 8 new, none in scope (`scout/screened.md`). The GWAS
Catalog was queried the same day under track B, nothing new; bioRxiv's and medRxiv's own listings again left out.
**Preprints checked again** the same three ways: no new published version (Chang's stays the one), PPR1366192 still
a preprint (Europe PMC by DOI and title; medRxiv `published` NA). The newer versions read at abstract level through
the medRxiv API: Salazar (TMEM106B, v3 2026-08-17), not a seed locus, nothing to queue; Alvarez Sirvent 2025 (v1
only); **Alvarez Sirvent 2026 v2** (2026-10-09) names Hap-Y as HLA-DRB1*15:01, row 135's allele, which the row does not
cite: queued for the curator as a preprint, its centenarian result for Hap-Y unknown from the abstract.

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
| 2026-11-17 | 2026-10-30 → 2026-11-17 | A-resource | 0 | 0 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | A-db | 3 | 0 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | A-pgs | 4 | 1 | 0 |

The 2026-11-17 rows are the second pass, reported once under Tracks F–K, Runs.

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
| 2026-11-17 | 2026-10-30 → 2026-11-17 | B-gwas | 6 | 0 | 0 |
| 2026-11-17 | the whole Catalog list | B-catalog | 79 studies, 37 PubMed ids | 0 | 0 |

The 2026-11-17 rows are the second pass, reported once under Tracks F–K, Runs.

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
| 2026-11-17 | 2026-10-30 → 2026-11-17 | C-rare | 8 | 1 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | C-protect-2 | 9 | 5 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | C-mito | 10 | 2 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | C-monogenic | 6 | 3 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | C-somatic-germline | 9 | 3 | 0 |

The 2026-11-17 rows are the second pass, reported once under Tracks F–K, Runs.

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
| 2026-11-17 | 2026-10-30 → 2026-11-17 | D-healthspan | 7 | 1 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | D-clocks | 30 | 6 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | D-multimorbidity-2 | 4 | 1 | 0 |

The 2026-11-17 rows are the second pass, reported once under Tracks F–K, Runs.

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
| 2026-11-17 | 2026-10-30 → 2026-11-17 | S-seedgene | 7 | 0 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | F-reporting | 3 | 1 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | G-finemap | 10 | 3 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | H-pleiotropy | 4 | 0 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | I-concepts | 19 | 2 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | J-models | 12 | 1 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | J-seedgene | 18 | 7 | 0 |
| 2026-11-17 | 2026-10-30 → 2026-11-17 | K-age | 1 | 0 | 0 |

81 new records, in `scout/screened.md`, at title level: reviews, mechanistic and animal ageing work, and trait genetics
(Mendelian randomization and genomic SEM of vascular, adipose and bone ageing) with no longevity locus. One is noted
for track J and not queued: pmid 42995887, "STING deficiency extends median lifespan and mitigates age-related liver
pathology in mice"; STING is cGAS's partner and CGAS is a seed gene, but the paper tests no human variant. No new locus
in the sources queried.

**Second pass, 2026-11-17** (window 2026-10-30 → 2026-11-17, about two weeks' overlap with the first; every query
as written, C-protect-2 and D-multimorbidity-2 in place of their first versions). Each query's own recall on its
track's PMIDs is unchanged from 2026-11-13 (A-resource 5/53, A-db 3/53, A-pgs 12/53, B-gwas 32/55, C-rare 27/94,
C-protect-2 20/94, D-multimorbidity-2 6/60, and F to K as in the table above). 153 distinct records, 116 already
screened, 37 new, in `scout/screened.md` at title level: reviews, animal and mechanistic work, clinical genetics, and
four biological-age clocks. One human GWAS read at abstract level: pmid 43035561 (Suo X et al., *Neurol Sci*, 2026 Nov
16, doi 10.1007/s10072-026-09554-8), rs7315280 near TESC and hippocampal volume (meta P ≤ 1.37e-19 in UK Biobank and
ENIGMA); neither the variant nor the gene is in the seed list, and the trait is not longevity, so not queued. The GWAS
Catalog v2 (the four EFO ids of B-catalog) lists the same 79 studies under 37 PubMed ids, none new. H-pleiotropy,
K-age, B-gwas and S-seedgene brought nothing new. No new locus in the sources queried.

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
