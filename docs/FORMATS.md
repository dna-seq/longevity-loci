# Formats

The research seats' files, and what `loci check` enforces of them. The models are
`src/longevity_loci/models.py`; this page is their prose. Field names and vocabularies are the requirements'
own (`docs/longevitymap_v2/longevitymap_v2_requirements.md`, §4.2, §4.5, §5.2, §6), so the module seat's
export to `variants.csv` and `studies.csv` is a projection, not a translation. A worked example of each is in
`assets/` (a test fixture, not curation).

## A row: `rows/<locus_id>-<locus_name>.yaml`

One per locus, named by the seed list's `locus_id` and `locus_name` (`docs/longevitymap_v2/data/seed_variants.csv`).
The row's `locus_name` is the seed's exactly; in the file name each run of characters outside `[A-Za-z0-9._-]`
becomes one `_` and the ends lose theirs (`81-FES_FURIN.yaml`, `73-KL_KL-VS.yaml`), and a locus the seed leaves
unnamed is `<locus_id>.yaml` (`models.row_file`);
a v1 locus with no seed entry takes the next free id above the seed's. Fields:

- `locus_id`, `locus_name`; `also_loci`, the other seed ids that name the same signal (IL6R 8 and 157), folded into
  this row, which is filed under the lowest of them (D14); `verdict` (`kept`, `re-tiered`, `legacy`, `dropped`) and `verdict_reason`.
- `axes`, the seven of the requirements' summary, each with the quotes it rests on in `cites`:
  - `tier`: `value` A to D (§4.1);
  - `mechanism`: `value`, a §5.2 `category` key (`other` refused);
  - `pleiotropy`: `values`, §4.2 tokens (`mech:<area>`, `broad`, `tradeoff`, ...);
  - `age_of_action`: `value` (`LIFELONG`, `MIDLIFE`, `LATE`, `AGE_INVERTING`, `EARLY_LIFE`, `UNKNOWN`) and
    `confidence` (`DIRECT`, `DIRECT_WEAK`, `INFERRED`, `UNKNOWN`);
  - `outcome`: `healthspan`, `lifespan`, `exceptional_survival`, each `"+"`, `0`, `"−"` or `untested` (never
    read as no effect). The minus is §4.2's U+2212; a typed `"-"` is read as it. Quote `+` and `-` in YAML;
  - `actionability`: `label` (`preventable`, `modifiable`, `descriptive`), `what` (`act_test:lpa`, ...), `who`
    (`act_who:self` or `act_who:doctor`);
  - `context`: `values` (`sex_specific:f`, `eur_only_evidence`, `ancestry_specific:<pop>`, ...).
- `flags`: §4.2's other tokens, one per entry, `token` plus `cites` (`causal:C2`, `effector:E1`,
  `PROTECT:PRESENCE`, `animal:genage_mouse`, `ld_proxy_of:rs…`).
- `variants`: per rsid, `gene` (the effector call), `phenotype` (at most six words), `trait_efo_id`,
  `effect_allele`, `effect_size`, `effect_measure`, `stat_significance` (from the anchor study), `direction`
  (`protective`, `risk`, `contested`, `unknown`), `negatives` (required on every variant when pleiotropy holds
  `tradeoff`), and `genotypes` (each `genotype`, `state`, `conclusion`; an indel's genotypes in its VCF
  alleles, as `T/T`, `T/TC`, `TC/TC`, D26.9).
- `studies`: one per (rsid, study), §6.3's columns: `note` and `quote` (the provenance quote, by id; or no
  `quote` and a `quote_absent` saying why: `not_found` read and nothing supports the row, `unchecked` only the
  abstract could be read, `other_claim` the article does not make the claim cited for (the row goes to a
  decision), `licence_unclear`),
  `phenotype_class` (§4.5), `study_design` (`parental_lifespan_linear` beside `_cox` for a linear model of
  parents' lifespan; `current_age_quantitative` for genotype regressed on participants' current age, a cross-sectional
  viability design, §4.5's confirmation-only class; `own_death_case_control` for deceased against living in a
  biobank, a binary endpoint), `population` (never empty), `stat_significance`, and where known
  `p_value` (as written), `p_value_num`, `p_one_sided` (only where the tier reads a one-sided P the article prints
  two-sided: half of `p_value_num`, in the discovery's direction, D26.13), `effect_size` (with its `effect_measure`: `beta`, `HR`, `OR`; and
  `effect_unit`), `effect_allele`, `direction` (the effect allele's, as the study reports it), `statistical_test`, `curator` (who located the quote: a name or a model id; `ai`, `true` and the like are
  refused). A study's rsid is one of
  the row's variants.
- Recorded now for just-dna-format 0.8's `studies.csv` (issue #6), all optional: `ancestry` (`AFR`, `AMR`, `EAS`,
  `EUR`, `SAS`, a list, beside the free-text `population`); an age band `age_min`, `age_max` (years, either open)
  with `age_of` (`participant` or `parent`) required once a bound is given; `sample_size` with `sample_unit`
  (`individuals` or `lives`) and `n_cases` (not above the sample); `stratum` and `stratum_level`, both or neither;
  `proxy_rsid`, the variant the study reported when the row's rsid is its lead.

`tradeoff` and `eur_only_evidence` are curation here. In 0.8 the compiler computes both (from `meta.csv` and from
the studies' `ancestry`) and refuses them authored, so the export never writes them into the module; where the
curator's token and 0.8's computed value disagree, that is a finding for the curator.

The tokens (pleiotropy, context, actionability's `what`, `flags`) are §4.2's, closed where it closes them:
`broad`, `tradeoff`, `nonadditive`, `mr:drug_target_proxy`, `ancestry_tag`, `age_dependent`, `eur_only_evidence`,
`legacy_longevitymap`, `replication_failed`, `preprint`, `pleiotropic`, `conditional`; `causal:C1`–`C4`,
`effector:E1`–`E4`, `ap:weak|moderate|strong`, `sex_specific:m|f`, `PROTECT:ABSENCE_OF_RISK|PRESENCE|BUFFERING`,
`animal:genage_mouse|mouse_qtl|worm_rnai`, `animal_dir:concordant|discordant|nonmonotone`,
`act_test:lpa|ldl|bp|hba1c`, `act_screen:skin`, `act_behaviour:smoking|weight`, `ld_proxy_of:rs…`,
`mediator:EFO_…` or `mediator:MONDO_…` (where OLS retires an EFO disease id for MONDO's); and, open as §4.2 leaves them, `mech:`, `context:`, `ancestry_specific:`, `also_in:`,
`hallmark:` with a lower-case name. Any other token is refused; a new one is added here and in the models.

A cite is `<note key>#<quote id>`: `pmid-31413261#q1`.

## A note: `corpus/<key>.md`

One per article; the key is `pmid-<PMID>`, or `doi-<DOI>` with `/` written as `_` for a preprint. Front matter:
`key`, `pmid` (or `doi`), `title`, `year`, `title_checked` (the date the title was matched against PubMed),
`depth` (the deepest of its readings: `abstract`, `full_text`, `supplement`). Then the readings, each under
`## Reading <YYYY-MM-DD>, <depth>`, oldest first; a later reading is added below, the earlier never rewritten.
A quote is one line, `> [q<n>] <the text, verbatim>`, never empty, its id unique in the note; prose around it
says what the article shows for which variant. A doi key is the doi with `/` as `_`.

A fact read from a database release (Open Targets' fine-mapping and locus-to-gene scores, gnomAD's frequencies)
has a note of its own, `corpus/db-<database>-<release>.md` (`db-opentargets-26.09`), cited from an axis or a flag
like any note (`db-opentargets-26.09#q1`), never as a study's `note`: a study is an article's analysis. Its front
matter: `key`, `database`, `release`, `url` (where the record was read), `accessed` (the day), `depth: record`; no
pmid, doi, title or title_checked. Its readings are `## Reading <YYYY-MM-DD>, record`, each quote copied from the record as the cache holds it (D12).

A record is cached by `uv run loci fetch-supp db-<database>-<release> <locator> --name <file>.json` (RM3): the
locator a URL (Ensembl's REST API, a GWAS Catalog summary-statistics file with `--rows`), or `opentargets:<GraphQL
query>`, which is posted to Open Targets' API. Where the database states its release (Open Targets'
`meta.dataVersion`, Ensembl's `info/data`), it is asked first, and a release other than the key's is refused: a
later release is a different source. A JSON answer is cached one object a line: the object's path, then its scalar
fields as `key value` pairs (`data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.0694`),
nested objects and lists on lines of their own. A quote under a `record` reading is located in the note's cached
records. A record is never pasted into the cache by hand: the check would then compare the curator's copy with
itself.

## The article cache: `$LOCI_CACHE/<key>.txt`

The text of each article read, outside git, keyed as its note (the variable is set on the machine, never written
as a path in the repository). Plain UTF-8 text: a PDF is converted before it is cached. `uv run loci fetch PMID…`
fills it from Europe PMC: the open-access full text where there is one (JATS flattened, a table cell ending in a
tab), else the abstract; a sidecar `<key>.source.json` says which, from where, when, and the text's sha256. A
full text Europe PMC does not serve falls back to the abstract; a busy or failing service (408, 429, 5xx, a reset)
does not, so a transient fault never replaces a cached full text. Exit 0 fetched, 1 no record, no text, a refused
request or a malformed answer, 3 the service did not answer (retry). A full text never
enters a commit, a message or an issue.

An article's other files go beside it: `uv run loci fetch-supp <key> <locator> [--only REGEX]`, the locator a file's
URL (a GitHub file page is read as its raw file), `zenodo:<record>` or `figshare:<article>` (every file of the
deposit, or those whose name matches `--only`). Each file is rendered to text as `<key>.supp-<file name>.txt`, its kind read from its contents where it
is a zip (a publisher's OpenDocument spreadsheet served under an .xlsx name): a workbook (xlsx or ods) one line per row, cells tab-separated, each sheet opened by `## sheet: <name>`; csv and tsv the same; a PDF
its text, page by page, each opened by `## page <n>`; a Word or OpenDocument text its paragraphs, a table row a line with its cells
tab-separated; code and plain text as they are; a zip archive each member it
can render, opened by `## file: <name>`; a gzip the file inside it. `--rows REGEX` keeps only the lines the
expression finds and each table's header, streaming a gzip rather than unpacking it, for a deposit too big to
cache whole (a GWAS's summary statistics); its cache name gains `.rows-<8 hex of the filter>`. Its sidecar `<key>.supp-<file name>.source.json` gives the locator, the
URL, the filter, the day, and the sha256 of the file read and of the text written. A file with no text (an image, a binary
.xls or .doc) is refused and nothing is written: a figure's caption is in the article's text, and its values are
in a data deposit when the authors gave one. Exit 0 all fetched, 1 a file refused or none found, 3 a service did
not answer (retry).

## Export: the module's tables (RM1)

`uv run loci export [OUTDIR]` (default `module/`) projects `rows/` onto just-dna-format 0.8's `variants.csv` and
`studies.csv`, and writes `quote_sources.csv` beside them (`src/longevity_loci/export.py`). It reads `rows/` and
`corpus/` only, never the article cache. Every row it writes is parsed by 0.8's own `VariantRow` or `StudyRow`
first; a refusal is reported and the row withheld. Output is sorted by rsid (by number), then genotype or
citation, then every cell, so two runs give the same bytes. Exit 0 written, 1 a row or note that does not parse or
a cite the corpus lacks (nothing written), 2 an input missing.

The columns are the reference example's headers (`docs/format08_reference/longevity_studies/`), then the module
seat's ask where 0.8 has a column for it: on `variants.csv` negatives, priority, phenotype, category,
stat_significance, effect_size, effect_measure, effect_allele, flags, requires_callable, acmg_sf, actionability; on
`studies.csv` stat_significance. Never chrom, start, ref or alts (the enricher resolves them), weight, nor the
spec's defaults (curator, method on a variant).

- **variants.csv**, one row per (lead rsid, genotype), the genotype's alleles sorted as 0.8 requires; the
  genotype's state and conclusion; `direction` the genotype's state, as the reference example writes it and as 0.8
  reads it (per row: a row's direction stands in for its state), so the variant's own direction, which is the
  effect allele's, is carried by `effect_allele` and never lands on a risk or neutral genotype's row (a contested or
  unknown variant keeps its own on every row); the variant's other cells, `trait_efo_id` OBA_VT0005372 on every variant (the
  reference example's rule; the row's own trait is reported), `priority` high for tier A, medium for B, low for C
  and D, `category` the mechanism axis, `actionability` its label, `requires_callable` and `acmg_sf` false.
  `flags` is `tier:X`, then the pleiotropy, context and actionability tokens, then the row's flags, `;`-joined.
  A tier D row is exported like any other: its states are neutral and its flag `tier:D`.
- **studies.csv**, one row per (lead rsid, study): `pmid` from the note, or `NONE` with the note's `doi` for a
  preprint; `proxy_rsid` and the proxy's own `effect_allele` as the study holds them; `trait_efo_id` from the
  phenotype class as the reference example writes it (HEALTHSPAN EFO_0009762, PARENTAL_LIFESPAN EFO_0007796,
  EXTREME_SURVIVAL_CC and OWN_SURVIVAL OBA_VT0005372; another class is left empty and reported);
  `provenance_quote` the quote's verbatim text from `corpus/<key>.md`. A percentile design (p90, p99) opens
  `statistical_test` with its percentile, since 0.8 has no cell for it and only `statistical_test` tells the two
  apart. A Cox model's age-band row leaves `n_cases` empty: its deaths are events, not cases. An effect the curator
  derived (`effect_unit` saying "derived here") writes the unit "crude odds ratio derived from the printed allele
  frequencies, not printed by the source". A study cannot rest on a `db-` note (the model refuses it, D12), so none
  is exported as one.
- **quote_sources.csv**, one row per exported study: rsid, pmid, doi, the note, the quote id, the reading's date
  and depth, or the `quote_absent` reason. It lets the module's README explain the plugin's `quotes_found` zeros:
  the plugin looks in Europe PMC's body text only (issue #7, point 3), and a quote read at depth `supplement` is
  not there. The cache sidecar's source is not recorded in a note's fields (only in its prose), so it is not
  written.

Never written as authored values, because 0.8 computes them downstream: `tradeoff`, `eur_only_evidence`, the
`causal:` and `effector:` confidences and the `ld_proxy_of:` pair. Where the curator's token and 0.8's computed
value disagree, that is a finding for the curator.

**What 0.8 has no place for**, reported by the command by reason and with a count, never dropped silently:
`age_of_action` and `outcome` (no column; 0.8 derives the outcome strip from `phenotype_class`), a study's
`p_one_sided` (written into `statistical_test`), and two that are wishes for the format, filed with
just-dna-compiler's triage by the liaison, not losses hidden here:

- **`nominal` (S147; the compiler's RM434).** 0.8's `stat_significance` stops at significant, suggestive,
  not_significant and unknown, and the format's maintainers read none of them as a threshold: `significant` is the
  defensible reading for a replication that passed its own test, where `not_significant` would tell a reader the
  look-up failed. So a nominal study is written `significant`, its `p_value` and
  `p_value_num` exactly as held, and its `statistical_test` says "nominal replication look-up (p < 0.05 in the
  discovery's direction), not genome-wide; D11/D13" (after the percentile, where there is one). Never `unknown`
  for a known P. A nominal variant (8-IL6R today) leaves `stat_significance` empty: a variant row has no
  `statistical_test` to say it is not genome-wide.
- **A study's direction (S148; the compiler's RM435, an `effect_direction` column, increase or decrease, due in a
  minor release).** Until it ships, 0.8 has no study-level direction beside `effect_allele`. Where a study has an
  effect size, the direction stands in its sign, read with `effect_allele` and `effect_unit` (a hazard's sign
  convention, "positive = earlier", is said only in `effect_unit`). Where it has allele, direction and P but no effect size
  (D13, D15, D20), `conclusion` says "<allele> on the longer-lived side" (or the shorter-lived), `effect_size` empty.

The export also names, without changing either value, a study whose `p_value` and `p_value_num` disagree by more
than 1 % (the compiler's check, an error under strict), and two analyses of one article that no narrowing cell
tells apart (the compiler's duplicate rule). Both are the curator's to settle.

## The checks

`uv run loci check rows` and `uv run loci check quotes`. Exit 0 all passed, 1 a failure, 2 an input missing
(a directory, the seed list, the cache), 4 nothing failed but something could not be checked, or there was
nothing to check.

- **rows**: each row parses into its model (closed vocabularies refused otherwise), is named for its locus as
  the seed list names it, and holds loci (its own and its `also_loci`, each a seed locus) no other row holds; each cite names a note in `corpus/` and a quote id that note holds (`no_note`, `no_quote`). An axis or flag
  citing nothing is `unsupported`, a warning listed with `-v`.
- **quotes**: each note's quotes are found in its cached text (`located`, `not_found`): a quote under an
  `abstract` or `full_text` reading in `<key>.txt`, one under a `supplement` reading in the article's supplements
  (`<key>.supp-*.txt`) or the article, the file it was located in named. A quote whose text is not cached is
  `no_text`, unknown, neither a pass nor a failure, and named by note. "Verbatim" survives Unicode
  compatibility forms (ligatures; super- and subscripts are kept), typographic quotes and dashes, a minus sign
  read as a hyphen, soft hyphens, any run of whitespace, and a hyphen at a line break (ASCII, soft or Unicode)
  read both ways; case, words, digits and punctuation must match, and the quote starts and ends on a word
  boundary. A quote that is the article's title is refused, and one quote cited for two or more variants is
  listed as `shared_quote`, a variant whose `direction` is `risk` (not harmonised to the lifespan-increasing
  allele, §6.2, D17) as `unharmonised`, and a study whose quote names neither its rsid nor its gene as `ungrained`
  (the plugin's `QUOTING.md`, rules 1 and 2; D10; both warnings). Copy a quote from the cached text,
  never retype it: the plugin's own check runs on its own retrieved text.

- **rules**, inside `check rows`, from the row's own fields (`rule`, a failure). A study *supports* the row
  unless it is `not_significant`; a null study is kept and supports nothing (§6.3).
  - A study's `stat_significance` agrees with its `p_value_num`: `significant` below 5×10⁻⁸, `suggestive` from
    5×10⁻⁸ to 1×10⁻⁵, `nominal` from 1×10⁻⁵ to 0.05 (read on `p_one_sided` when the study has one, which must be
    half of `p_value_num` within 5 %). A nominal study supports: §4.1 counts a replication at
    p < 0.05, so the §6.3 fields below are asked of it too. `not_significant` has no band (D11).
  - R-TIER-1: a row whose only supporting studies are PMID 22279548 is tier D, neutral on every genotype.
  - A tier D row is neutral on every genotype (D25: not supported means no weight).
  - On a tier A or B row: a genome-wide significant study, not MR-only, not n = 1 genomes (R-TIER-4); not one
    unreplicated old-against-young case-control study, `centenarian_case_control` or
    `age_threshold_case_control` (R-TIER-2, D22; a percentile case-control design is not read as one; lifted by a supporting study of a replicating class, extreme survival, parental lifespan or own survival, in another note, a nominal look-up included, D22.2, D25.10); §6.3's `p_value`, `p_value_num`, `effect_size`, `effect_measure` and `effect_allele` on every supporting
    study, except that a `nominal` one (a replication look-up) or a `multivariate_healthspan_lifespan` one (D15), or a `meta_analysis` that prints no pooled effect
    (D20), needs only `p_value`, `p_value_num`,
    `effect_allele` and a `direction` other than `unknown` (or an `effect_size`) (D13); and, once a variant lists three genotypes, exactly one neutral, or every one neutral when its
    `direction` is `contested` (a trade-off with unresolved net direction, §6.2). Fewer than three genotypes is
    `incomplete`, a warning listed with `-v`: an APOE-style locus is scored as a diplotype (§6.4).

Not checked yet: R-TIER-3 (an ancestry banner, the consumer's) and R-TIER-1's "research view only" (the
module's), the tier A criteria a field cannot show (N, replication, heterogeneity), which genotype is the most common, and that a cited quote bears on the claim it is
cited for. A quote is a substring: one cut short so that it drops a "not" before it
is still located, so a quote is a whole sentence or table cell (§6.3), and that is the curator's to keep.
