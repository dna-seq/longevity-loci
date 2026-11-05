# Formats

The research seats' files, and what `loci check` enforces of them. The models are
`src/longevity_loci/models.py`; this page is their prose. Field names and vocabularies are the requirements'
own (`docs/longevitymap_v2/longevitymap_v2_requirements.md`, §4.2, §4.5, §5.2, §6), so the module seat's
export to `variants.csv` and `studies.csv` is a projection, not a translation. A worked example of each is in
`assets/` (a test fixture, not curation).

## A row: `rows/<locus_id>-<locus_name>.yaml`

One per locus, named by the seed list's `locus_id` and `locus_name` (`docs/longevitymap_v2/data/seed_variants.csv`);
a v1 locus with no seed entry takes the next free id above the seed's. Fields:

- `locus_id`, `locus_name`; `verdict` (`kept`, `re-tiered`, `legacy`, `dropped`) and `verdict_reason`.
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
  `tradeoff`), and `genotypes` (each `genotype`, `state`, `conclusion`).
- `studies`: one per (rsid, study), §6.3's columns: `note` and `quote` (the provenance quote, by id),
  `phenotype_class` (§4.5), `study_design`, `population` (never empty), `stat_significance`, and where known
  `p_value` (as written), `p_value_num`, `effect_size` (with its `effect_measure`: `beta`, `HR`, `OR`; and
  `effect_unit`), `effect_allele`, `statistical_test`, `curator` (who located the quote). A study's rsid is one of
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
`mediator:EFO_…`; and, open as §4.2 leaves them, `mech:`, `context:`, `ancestry_specific:`, `also_in:`,
`hallmark:` with a lower-case name. Any other token is refused; a new one is added here and in the models.

A cite is `<note key>#<quote id>`: `pmid-31413261#q1`.

## A note: `corpus/<key>.md`

One per article; the key is `pmid-<PMID>`, or `doi-<DOI>` with `/` written as `_` for a preprint. Front matter:
`key`, `pmid` (or `doi`), `title`, `year`, `title_checked` (the date the title was matched against PubMed),
`depth` (the deepest of its readings: `abstract`, `full_text`, `supplement`). Then the readings, each under
`## Reading <YYYY-MM-DD>, <depth>`, oldest first; a later reading is added below, the earlier never rewritten.
A quote is one line, `> [q<n>] <the text, verbatim>`, never empty, its id unique in the note; prose around it
says what the article shows for which variant. A doi key is the doi with `/` as `_`.

## The article cache: `$LOCI_CACHE/<key>.txt`

The text of each article read, outside git, keyed as its note (the variable is set on the machine, never written
as a path in the repository). Plain UTF-8 text: a PDF is converted before it is cached. A full text never
enters a commit, a message or an issue.

## The checks

`uv run loci check rows` and `uv run loci check quotes`. Exit 0 all passed, 1 a failure, 2 an input missing
(a directory, the seed list, the cache), 4 nothing failed but something could not be checked, or there was
nothing to check.

- **rows**: each row parses into its model (closed vocabularies refused otherwise), is named for its locus as
  the seed list names it, and holds a locus no other row holds; each cite names a note in `corpus/` and a quote id that note holds (`no_note`, `no_quote`). An axis or flag
  citing nothing is `unsupported`, a warning listed with `-v`.
- **quotes**: each note's quotes are found in its cached text (`located`, `not_found`); a note with no cached
  text is `no_text`, unknown, neither a pass nor a failure, and named by note. "Verbatim" survives Unicode
  compatibility forms (ligatures; super- and subscripts are kept), typographic quotes and dashes, a minus sign
  read as a hyphen, soft hyphens, any run of whitespace, and a hyphen at a line break (ASCII, soft or Unicode)
  read both ways; case, words, digits and punctuation must match, and the quote starts and ends on a word
  boundary. A quote that is the article's title is refused, and one quote cited for two or more variants is
  listed as `shared_quote` (the plugin's `QUOTING.md`, rules 1 and 2; D10). Copy a quote from the cached text,
  never retype it: the plugin's own check runs on its own retrieved text.

Not checked yet: that a row's studies carry §6.3's required columns for tier A/B; that a scored locus lists
all three genotypes with the most common one neutral; the hard rules (R-TIER-1 to 4); and that a cited quote
bears on the claim it is cited for. A quote is a substring: one cut short so that it drops a "not" before it
is still located, so a quote is a whole sentence or table cell (§6.3), and that is the curator's to keep.
