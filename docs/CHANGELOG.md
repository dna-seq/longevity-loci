# Changelog

Newest first.

## Unreleased

- D30.10: a replication sample whose controls misfit the reference frequency at P < 0.01 is named, never counted, pass or fail (92 stays C).
- D30.9: a locus acts through weight only where its signal is shown to share the weight signal (88 stays general ageing).
- D30: batch nine's read. D29.18's test corrected (the meta with the AncestryDNA arm at z = 0 must pass the filter; sweep owed again); D17.1 reaches any nearby lifespan signal but never the anchor (87 contingent on a joint conditional); 103 re-read under D25.1; a nominal, uncontradicted, sub-suggestive locus is C; 77 stays C; PROTECT:ABSENCE_OF_RISK needs a genome-wide disease; v1 non-leads get legacy rows of their own.
- just-dna 0.8.5 (floors `>=0.8.5`), with the module-creator plugin's pin moved to `v0.48.9`, which locks the same; `remote_derive` reports its passes, and lane lookups carry their licence terms.
- D29.18–20: a Wright Table 9 AncestryDNA line counts as a replication only where the UK arm alone passes the table's filter (sweep owed); a genotype-model claim is tested whole (73 stays C); 74's sexes differ at P 2.9e-4.
- D29.15–17: 74 is B with replication_failed (D25.1's exception); `sex_specific` needs a test of the difference; a row is tiered on its lead's own evidence, so 75 is C on its suggestive repeat, the overfit line at the locus setting nothing.
- D29.14: a genotype-model claim (73 KL-VS, heterozygote advantage) is tiered, read and tested on its own model; per-allele lines are named, not scored.
- The module-creator plugin's pin moves to `v0.48.8` (registry lane lookups, `remote_derive`'s passes, gene hints for expression); nothing here changes.
- D29.11–13 (70 FGD6): a multivariate or healthspan discovery's red flag stays unknown even on a like-for-like comparison of two lifespan arms; a coronary colocalisation names heart_vessels; animal evidence is a flag, not a study.
- Pacing off, on the person's word (2026-11-12): the curator no longer stops at 95 % of the 5-hour or the 7-day window, and the dashboard counts against the whole window.
- D29.9–10: a quoted trade-off keeps a skin_sun row descriptive; a coding lead's E1 is not vetoed by another gene's QTL (66 TYR).
- RM1 done: the export validates and compiles strict on just-dna-format 0.8.4 (64 loci, 192 variant rows, 331 studies, every locus resolved), and the module seat's first rehearsal is on the registry's test instance as test-longevity-loci/longevitymap 2.0.0 (module 0fa5e77). Nothing on production.
- A variant may author its `locus` (chrom, start, ref, cited) where its rsID names several loci, and `loci export` writes it on the variant's rows and studies, so 0.8 verifies that locus instead of expanding onto all of them (D29.8; 47 AP5Z1).
- D29.7: consistent nominal look-ups across independent samples do not stand in for a genome-wide anchor (65 HSD17B12 is C).
- D29.3–6 from the adversarial read of rows 60 to 64: a proxy does not stand in where the lead is tested; an overfit discovery leaves exceptional survival untested; a printed P is read as printed; a heterogeneity P counts both errors.
- RM1 built: `loci export` projects the rows onto 0.8's `variants.csv` and `studies.csv` plus `quote_sources.csv`, each row parsed by 0.8's models, sorted and byte-reproducible; computed tokens never authored, `nominal` written `significant` and said not genome-wide in `statistical_test` (S147, the compiler's RM434), a bare study direction into `conclusion` until RM435's `effect_direction` ships (S148); what 0.8 cannot hold reported by reason (docs/FORMATS.md, "Export").
- just-dna 0.8 adopted: format, compiler and enricher `>=0.8.4,<0.9` (0.8.4 in the lock), with the module-creator plugin's pin moved to `v0.48.7`, whose server runs the same trio; polars and duckdb stay below 2. Suite unchanged.
- The curator's stop and the dashboard's cap move from 80 % to 95 % of the 7-day window, on the person's word (2026-11-12; 90 % for an hour first).
- D29.2: a footnote's allele outvoted by the paper's text, supplement and figure is overruled (64 BET1L, T longer-lived).
- D29.1: a database line the curator reads never replicates (D12), and a healthspan discovery's red flag is scaled from its own effect, so 63 TCF7L2 is B.
- D27 and D28 settle the sixth batch: the mean factor divides, a Genomic SEM factor is multivariate, a QC-flagged colocalisation is E3, red flags scaled from the discovery's own effect, a cell is `−` against the allele, a disease-informed Bayesian call counts for B only; 6 CELSR2 and 80 CHRNA3/5 leave A with `replication_failed`.
- Weekly dependency bump: typer 0.27.3 to 0.29.1, pydantic 2.14.3, click 8.5.1 and three small ones. `just-dna-compiler` and `just-dna-format` are now capped below 0.8, as the enricher is: the bump had taken them to 0.8.4 beside enricher 0.7.3.
- A study's `p_one_sided` holds the one-sided P the tier reads when the article prints two-sided; `check rows` reads the nominal band on it and asks it to be half the printed value (D26.13).
- D26 settles the fifth batch: P values after the paper's own genomic control, one-sided outcome cells, no flag on an uncomputable calibration, a genome-wide line the paper's own filter excludes as an overfit source (44, 41 D), a weaker discovery contradicted as D (45), 18 B with `replication_failed`; FORMATS writes indel genotypes in their VCF alleles.
- R-TIER-2 in `check rows` is lifted by a scoring-class study in another paper, a nominal look-up included, and no longer by a healthspan or multivariate one (D22.2, D25.10); it used to ask a second genome-wide study.
- `check rows` holds every tier D row neutral on every genotype, not only R-TIER-1's; D25 says when a tested discovery is D, how a red flag that converts scales is calibrated, and settles the fourth batch's questions.
- R-TIER-2 in `check rows` holds an age-threshold case-control (90+ against younger) as it holds a centenarian one; D21 fixes the red-flag line (power 0.8, heterogeneity P below 0.05), D22 what replicates and when a cross-ancestry null is tier D.
- A meta-analysis that prints no pooled effect supports a tier A/B row on its allele, direction and P (D20).
- `loci fetch-supp` reads OpenDocument spreadsheets and texts and Word documents, knowing an office file by its contents, not its name (Springer serves Gurinovich 2021's .ods as .xlsx).
- `study_design: own_death_case_control` (a biobank's deceased against its living); D19: a replication sharing a small, measured part of the discovery sample is independent, and a stratum's genome-wide hit is read at the paper's own threshold.
- `check rows` lists a variant not harmonised to the lifespan-increasing allele as `unharmonised`; D17 settles what the second batch's reviews found (a co-occurring lifespan study is the locus's own signal, causal confidence from the claim's own credible sets, genome-wide at the paper's own P, the anchor study's trait id).
- A curation dashboard in `#dashboards > longevity-loci curation` (the organisation's board channel, as genie keeps one): seed loci done, tiers, rows per hour and the weekly quota's burn as moving averages with a 3-hour half-life, and what is left before the 80% cap. `scripts/dashboard.py` writes it; the lead's watcher `dashboard` keeps it up to date every 10 minutes; the readings stay outside the repository.
- `study_design: current_age_quantitative`, for a GWAS of participants' current age (Wright 2019's AncestryDNA arm): cross-sectional viability, confirmation only (§4.5).
- A healthspan locus scores with a lifespan study at p < 0.05 on the same allele and direction beside it; with none it is tier C (D16).
- A database release's record is cached and its quotes checked (RM3): `loci fetch-supp db-<database>-<release> …` takes Open Targets' GraphQL (`opentargets:<query>`), Ensembl's REST (pairwise LD among it) or a summary-statistics file, refuses a release other than the key's where the database states one, and caches a JSON answer one object a line.
- A multivariate healthspan-lifespan test supports a tier A/B row on its allele, direction and P, having no single effect size (D15).
- `loci fetch-supp` reads a gzipped file, and `--rows REGEX` caches only the lines a row needs (with each table's header), so a summary-statistics deposit (Zenin 2019's 237 MB csv.gz) can back a quote.
- just-dna-format 0.8's longevity reference example and the compiler's longevitymap v2 shape audit, copied into `docs/format08_reference/`, with `docs/FORMAT08_REFERENCE.md` saying what they settle for the export and the rows.
- From the pilot (RM5): a study quote naming the proxy the study reported is grained; `mediator:` takes a MONDO id where OLS retired the EFO one; `study_design: parental_lifespan_linear` for a linear model of parents' lifespan.
- `loci fetch-supp`: an article's supplement tables, PDFs, code files and Zenodo or figshare deposits are cached as text beside the article, and `check quotes` locates a quote read at depth `supplement` in them; before, such a quote could only be prose (RM4).
- The curator compacts itself after each row, stops at 80% of the 7-day quota window, reads supplements, figures, code and data deposits as deep as a row needs, and settles the requirements' silent cells with the advisor; the lead reads a re-tiered row adversarially instead of asking the person.
- A row may fold in the other seed ids that name its signal (`also_loci`), filed under the lowest; a second row for one of them is a duplicate (D14).
- A nominal replication look-up supports a tier A/B row on its effect allele, its `direction` (a new study field) and its p, without an effect size; a genome-wide study still owes all five of §6.3's fields (D13).
- A database release can be cited: a `corpus/db-<database>-<release>.md` note, cited from an axis or a flag; its quotes are unknown to `check quotes` until a fetcher caches the record (D12).
- A row whose seed name holds a slash, a space or a bracket is filed under a file-safe name (`81-FES_FURIN.yaml`), and an unnamed locus as `<locus_id>.yaml`; the row keeps the seed's name.
- `stat_significance: nominal` (1×10⁻⁵ ≤ p < 0.05) supports a row, so a replication §4.1 counts is seen by the check; `study_design: age_threshold_case_control` for cases above an age (D11).
- `docs/seats/README.md` shows how work flows between the six seats, as a diagram, and which seats wait on the person.
- The runner seat is seated: `runs/LOG.md` (one entry per batch job) and `runs/STATUS.md` (what runs now) begin, empty; fetches for the scout and the curator now go to it.
- `module/` scaffolded for longevitymap 2.0.0 (plugin v0.48.5, format 0.7.1): the spec with the requirements' recommended defaults for D1 and D3, header-only variants, studies and licensing tables. Strict validation refuses it until the first curated study row lands.
- A runner seat (on the kit's `runner` role, a quiet seat) takes the repository's batch jobs on the cluster: fetches for the scout and the curator, later the index and the compile at scale, logged in `runs/`. The lead keeps to its own role: its `facts-to-rigger` duty and its cluster paragraph move to the runner, and so does the nodes watcher.
- The lead holds the runner's duty `facts-to-rigger`: cluster facts it finds go to the account's rigger the same turn, and a CPU burst over 16 cores is claimed with the rigger first.
- The scout is a quiet seat (`presence = false`): it sweeps whether the person is here or away. Its priming is written as five duties (sweep, query ledger, dedupe, queue, new loci), its work otherwise unchanged; bulk full texts for a sweep go to the lead as a batch fetch.
- The module-creator plugin's pin moved to v0.48.6 (`validate_module` reports carried warnings; the GWAS pass and a contract skew say they are upstream's).
- The module-creator plugin's pin moved to v0.48.5 (tool results name the plugin tool for an upstream CLI command; `registry_register` stops echoing a reused install-id).
- The module-creator plugin's pin moved to v0.48.4 (`fetch_fulltext` by DOI, `audit_module` names stale checks and orphaned derived rows).
- The module-creator plugin's pin moved to v0.48.2 (`fetch_fulltext` reaches PubMed for a PMCID Europe PMC lacks). The pin does not yet bind on the liaison's machine: see `docs/UPSTREAM_PLUGIN.md`.
- `just-dna-enricher` capped below 0.8 until the module-creator plugin moves to it: 0.8 moves the shared Ensembl cache the plugin's 0.7 enricher reads.
- `duckdb` and `polars` capped below 2, so the lock matches the module-creator plugin's (polars 1.44.2) and no 2.0 `.duckdb` reaches the shared enricher cache its 1.x reader crashes on.
- The module-creator plugin's pin moved to v0.48.1 (`remote_derive` and `remote_draft` send the registry token).
- The liaison's ledgers begin: `docs/UPSTREAM_PLUGIN.md` (read mark v0.48.0, the pinned plugin),
  `docs/UPSTREAM_COMPILER.md` (v0.7.3, the trio `uv.lock` installs) and `docs/UPSTREAM_REGISTRY.md` (no mark yet:
  nothing here runs against the registry). Each upstream's new tags are watched, and the weekly dependency bump of
  `uv.lock` is switched on, in the liaison's tables in `.blueprints.toml`.
- The repository's rules laid by the seats kit's `bin/init.py`: `CLAUDE.md` (with `AGENTS.md` linked to it), the
  roadmap, this changelog, the decisions, and the leak gate's `.leak_words.template`. The leak gate is on in the
  lead's clone (the list itself is machine-local and never tracked).
- The research groundwork moved in: `docs/longevitymap_v2/` (the requirements, the seed list, the evidence
  tracks A to K, decisions D1 to D7, the S14 audit with its scripts and evidence), copied unchanged from
  `dna-seq/just-dna-lite` at 050bf9f.
- The row and note formats (`docs/FORMATS.md`, decisions D8 and D9) and their checks: `uv run loci check rows`
  (every cite resolves to a note and a quote id) and `uv run loci check quotes` (every quote is found in the
  article's cached text, or said unknown when none is cached). Tested on a real abstract fetched at run time;
  each check broken on purpose and its test seen to fail. Not run yet on curated rows: none exist.
- The checks tightened after a critic's read of the formats: §4.2's tokens closed where the requirements close
  them, outcome cells read as §4.2 writes them, §6.2/§6.3's missing fields added (phenotype, trait_efo_id,
  p_value_num, age_band, curator), a study's rsid held to the row's variants, `negatives` required on a trade-off
  locus, rows held to the seed list's names and to one row per locus, a quote held to word boundaries and to one
  non-empty line, readings oldest first with their depth, and an empty or missing input no longer a pass.
- `just-dna-enricher` 0.7.3 a dependency (the project now needs Python 3.13, as it does), and the module-creator
  plugin enabled for every clone in `.claude/settings.json`, pinned at v0.48.0. The plugin is not yet seen loaded
  in a session: a session started after this commit shows it.
- The inputs fetched and recorded (`docs/INPUTS.md`): v1's `longevitymap.sqlite`, HAGR's Build 3 download and a
  snapshot of HAGR's live entry pages (`scripts/hagr_snapshot.py`), with digests and HAGR's CC BY 3.0 licence.
  The live site has not moved much since v1: 19 of v1's ids are now empty upstream, no text edits seen.
- A study records just-dna-format 0.8's fields now, optional (issue #6): `ancestry` codes, an age band with whose
  age it is, sample size and cases, a stratum, a proxy rsid, the effect's unit; an effect size needs its measure.
  The free-text `age_band` is gone, replaced by the band's bounds.
- The quote check set beside the plugin's `QUOTING.md` (D10): a title quoted as a passage is refused, one quote
  cited for several variants is listed (`shared_quote`).
- RM2 landed: `loci check rows` now checks the hard rules a row's fields can show (R-TIER-1, R-TIER-2, R-TIER-4,
  §6.3's required columns on a tier A/B row, one neutral genotype), and `loci fetch` fills the article cache
  from Europe PMC (open full text, else the abstract). The fixtures carry Deelen 2019's real Table 2 row.
- From the plugin's quoting rules (issue #7): a study may carry no quote with a `quote_absent` reason, a
  placeholder `curator` (`ai`, `true`) is refused, and a quote naming neither the study's variant nor its gene is
  listed as `ungrained`.
- The rules and the fetch, fixed after a fresh auditor's read of RM2: a null study supports nothing (R-TIER-1
  and §6.3's columns read supporting studies only), a resolved trade-off may have one neutral genotype (only a
  `contested` one is neutral throughout), `stat_significance` is held to `p_value_num`, n = 1 genomes are not tier
  A/B; `loci fetch` no longer turns a busy service into an abstract over a cached full text, sorts a refusal and a
  malformed answer from an outage, never writes an empty text, and writes atomically with the text's digest.
