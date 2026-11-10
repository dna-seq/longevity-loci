# Changelog

Newest first.

## Unreleased

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
