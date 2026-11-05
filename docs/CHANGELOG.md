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
