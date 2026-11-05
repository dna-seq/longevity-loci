# Upstream ledger: the compiler's packages

`just-dna-format`, `just-dna-compiler` and `just-dna-enricher`, released together from `dna-seq/just-dna-compiler`
with tags `vX.Y.Z` (the tag names the cut; each package carries its own version). Kept by the liaison seat
(`docs/seats/LIAISON.md`); another seat that meets a symptom in these packages sends it there rather than writing
here. A defect goes into the compiler's consumer inbox, `docs/CONSUMER_SUGGESTIONS.md` in its clone, restated in
its terms with an id from its ledger, appended and never committed; then a message to `just-dna-compiler/triage`.

Watched on the liaison's machine from a clone outside this repository (its line `compiler` in the liaison state
file): `[seat.liaison.watch.compiler]` says each new tag. The coming minor (`0.8`) is built on a branch of its own;
the compiler's liaison maps it, and is asked before this seat maps it again. The registry's liaison keeps an
adoption map of `0.8` (rows M1 to M11, in `docs/UPSTREAM_COMPILER.md` of `dna-seq/just-dna-registry`, read from the
compiler's `0.8` branch); reuse it at the cut, and tell that liaison where our use differs (its offer, 2026-11-05).

## Read mark

**`v0.7.3`**: enricher 0.7.3, compiler 0.7.2, format 0.7.1, the trio `uv.lock` installs since 3dd8c2a
(2026-11-05; floor `just-dna-enricher>=0.7.3` in `pyproject.toml`). A first mark, fast-forwarded: no release before
it was read, since nothing here used one.

## Backlog

None: nothing before `v0.7.3` is read, since nothing here used it.

## What this repository uses

A dependency only: `just-dna-enricher` (bringing the compiler and the format), the module toolchain's enrichment
of rsIDs and coordinates. No code under `src/` or `tests/` imports any of the three yet; the symbols are listed
here as the first import lands.

## Inbound verdicts

None yet.

## Our pieces that duplicate the compiler's

None yet.

## Outbound

None yet.
