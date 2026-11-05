# Changelog

Newest first.

## Unreleased

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
