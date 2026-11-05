# Formats

The research seats' files, and what `loci check` enforces of them. The models are
`src/longevity_loci/models.py`; this page is their prose. Field names and vocabularies are the requirements'
own (`docs/longevitymap_v2/longevitymap_v2_requirements.md`, §4.2, §4.5, §5.2, §6), so the module seat's
export to `variants.csv` and `studies.csv` is a projection, not a translation. A worked example of each is in
`assets/` (a test fixture, not curation).

## A row: `rows/<locus_id>-<locus_name>.yaml`

One per locus, named by the seed list's `locus_id` and `locus_name` (`docs/longevitymap_v2/data/seed_variants.csv`);
a v1 locus with no seed entry takes the next free id. Fields:

- `locus_id`, `locus_name`; `verdict` (`kept`, `re-tiered`, `legacy`, `dropped`) and `verdict_reason`.
- `axes`, the seven of the requirements' summary, each with the quotes it rests on in `cites`:
  - `tier`: `value` A to D (§4.1);
  - `mechanism`: `value`, a §5.2 `category` key (`other` refused);
  - `pleiotropy`: `values`, §4.2 tokens (`mech:<area>`, `broad`, `tradeoff`, ...);
  - `age_of_action`: `value` (`LIFELONG`, `MIDLIFE`, `LATE`, `AGE_INVERTING`, `EARLY_LIFE`, `UNKNOWN`) and
    `confidence` (`DIRECT`, `DIRECT_WEAK`, `INFERRED`, `UNKNOWN`);
  - `outcome`: `healthspan`, `lifespan`, `exceptional_survival`, each `+`, `0`, `-` or `untested` (never read
    as no effect);
  - `actionability`: `label` (`preventable`, `modifiable`, `descriptive`), `what` (`act_test:lpa`, ...), `who`;
  - `context`: `values` (`sex_specific:f`, `eur_only_evidence`, `ancestry_specific:<pop>`, ...).
- `flags`: §4.2's other tokens, one per entry, `token` plus `cites` (`causal:C2`, `effector:E1`,
  `PROTECT:PRESENCE`, `animal:genage_mouse`, `ld_proxy_of:rs…`).
- `variants`: per rsid, `gene` (the effector call), `effect_allele`, `direction` (`protective`, `risk`,
  `contested`, `unknown`), `negatives`, and `genotypes` (each `genotype`, `state`, `conclusion`).
- `studies`: one per (rsid, study), §6.3's columns: `note` and `quote` (the provenance quote, by id),
  `phenotype_class` (§4.5), `study_design`, `population`, `stat_significance`, and where known `p_value`,
  `effect_size`, `effect_measure` (`beta`, `HR`, `OR`), `effect_allele`, `statistical_test`.

A cite is `<note key>#<quote id>`: `pmid-31413261#q1`.

## A note: `corpus/<key>.md`

One per article; the key is `pmid-<PMID>`, or `doi-<DOI>` with `/` written as `_` for a preprint. Front matter:
`key`, `pmid` (or `doi`), `title`, `year`, `title_checked` (the date the title was matched against PubMed),
`depth` (the deepest reading so far: `abstract`, `full_text`, `supplement`). Then the readings, each under
`## Reading <YYYY-MM-DD>, <depth>`, oldest first; a later reading is added below, the earlier never rewritten.
A quote is one line, `> [q<n>] <the text, verbatim>`, its id unique in the note; prose around it says what
the article shows for which variant.

## The article cache: `$LOCI_CACHE/<key>.txt`

The text of each article read, outside git, keyed as its note (the variable is set on the machine, never written
as a path in the repository). Plain UTF-8 text: a PDF is converted before it is cached. A full text never
enters a commit, a message or an issue.

## The checks

`uv run loci check rows` and `uv run loci check quotes`. Exit 0 all passed, 1 a failure, 2 the cache is not
set, 4 nothing failed but something could not be checked.

- **rows**: each row parses into its model (closed vocabularies refused otherwise) and is named for its locus;
  each cite names a note in `corpus/` and a quote id that note holds (`no_note`, `no_quote`). An axis or flag
  citing nothing is `unsupported`, a warning listed with `-v`.
- **quotes**: each note's quotes are found in its cached text (`located`, `not_found`); a note with no cached
  text is `no_text`, unknown, neither a pass nor a failure. "Verbatim" survives Unicode compatibility forms
  (ligatures), typographic quotes and dashes, soft hyphens, any run of whitespace, and a hyphen at a line break
  read both ways; case, words and punctuation must match.

Not checked yet: that a row's studies carry §6.3's required columns for tier A/B, the hard rules (R-TIER-1 to
4), and that a cited quote bears on the claim it is cited for (that one is the curator's reading).
