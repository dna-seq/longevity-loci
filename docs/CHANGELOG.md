# Changelog

Newest first.

## Unreleased

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
