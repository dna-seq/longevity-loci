# Upstream ledger: the compiler's packages

`just-dna-format`, `just-dna-compiler` and `just-dna-enricher`, released together from `dna-seq/just-dna-compiler`
with tags `vX.Y.Z` (the tag names the cut; each package carries its own version). Kept by the liaison seat
(`docs/seats/LIAISON.md`); another seat that meets a symptom in these packages sends it there rather than writing
here. A defect goes into the compiler's consumer inbox, `docs/CONSUMER_SUGGESTIONS.md` in its clone, restated in
its terms with the next `Sn` from its ledger, appended and never committed; then a mention of
`just-dna-compiler/triage` in `agent-chat` naming the `Sn` (its triage wakes on this seat since their a8262397).

Watched on the liaison's machine from a clone outside this repository (its line `compiler` in the liaison state
file): `[seat.liaison.watch.compiler]` says each new tag, `[seat.liaison.watch.compiler-next]` each commit to
`docs/INTEGRATION_0_8.md` (the consumers' guide) on the `0.8` branch (its line `compiler-next`). The coming minor (`0.8`) is built on a branch of its own;
the compiler's liaison maps it, and is asked before this seat maps it again. The registry's liaison keeps an
adoption map of `0.8` (rows M1 to M11, in `docs/UPSTREAM_COMPILER.md` of `dna-seq/just-dna-registry`, read from the
compiler's `0.8` branch); reuse it at the cut, and tell that liaison where our use differs (its offer, 2026-11-05).

## Read mark

**`v0.7.3`**: enricher 0.7.3, compiler 0.7.2, format 0.7.1, the trio `uv.lock` installs since 3dd8c2a
(2026-11-05; floor `just-dna-enricher>=0.7.3` in `pyproject.toml`). A first mark, fast-forwarded: no release before
it was read, since nothing here used one.

## Waiting on 0.8

The person, 2026-11-05: "We're waiting on 0.8 release, it is tailored towards longevitymap v2 specs from -lite's
draft". The `0.8` branch carries entries made for this repository's design (`docs/longevitymap_v2/`):
`reference_examples/longevity_studies/`, `studies.csv`'s `phenotype_class`, `tradeoff` reserved for a computed
column, APOE scored only as diplotypes (R-APOE-1). At the cut, read the 0.8 changelog against
`docs/longevitymap_v2/` and `docs/FORMATS.md`, reusing the registry liaison's map for what both repositories use,
and tell the module seat what changes for the module.

## 0.8, read before the cut

`docs/INTEGRATION_0_8.md` on `origin/0.8` at `5b1b73b8` (2026-11-05), its longevity-loci block (§3) and the
`studies.csv` columns (§1.6), read against `docs/FORMATS.md`. Filed for the lead and the module seat as #6. The
read mark stays at `v0.7.3` until the cut; the cut is read again in full.

- **Blocks us: the plugin caps the trio below 0.8**, at `v0.48.0` and on its `main` (`pyproject.toml`, the S20
  decision): it moves only once both registry instances serve format 0.8. A 0.8 table or column is refused until
  then. Order: compiler cut, registry deploy, plugin release, our pin. Waits on upstream; no filing.
- **Breaks the export as written:** `population` (free text) against 0.8's closed `ancestry`; `age_band` against
  `age_min`/`age_max`/`age_of`. #6.
- **Levers to adopt:** `sample_size`/`sample_unit`/`n_cases`, `stratum`/`stratum_level`, `proxy_rsid` per study,
  `effect_unit`, `model_organisms.csv` for the `animal:` flags. #6. The study fields landed in 433a1d0 (the lead); the export's part of #6 stays open.
- **Ours the compiler now does:** `tradeoff` (computed in `meta.csv`, refused when authored) and
  `eur_only_evidence` (derived into `weights.parquet` from `ancestry`). Our tokens stay curation; the export
  never authors them. #6.
- **Fits:** `phenotype_class` (v2's twelve), a preprint as `pmid=NONE` with `doi`.
- **Guide moved to `a4a401e7`** (2026-11-05): our block gains the plugin-cap point (its item 3); new §1.35 to §1.40
  and §4, known issues. For the module seat: enrich online, since offline cannot left-align an indel (RM385, fixed
  in 0.9) and an offline and an online fill can differ (RM376); an rsID no link can host now has no
  `resolution.csv` row, where 0.7 wrote `not_found` (RM382). No git dependency here to move: nothing imports the
  trio, so there is no suite to run against the branch.
- **Release candidate at `c90e6d98`** (2026-11-05): audit round 3 found no blocker; new §1.41 to §1.43 (RM395,
  RM393, RM394: the `--rederive` drift report's seven arms, and its remedy per source). What remains is the cut.

## Caps

- **`duckdb<2`, `polars<2`** (2026-11-05, the liaison's). The lock had moved to duckdb 2.0.0 and polars 2.1.0
  through the enricher, which caps neither. The module-creator plugin's server (`v0.48.1`'s lock) runs duckdb
  1.5.5 and polars 1.44.2 and shares this machine's enricher cache. From the compiler's liaison (their
  `docs/UPSTREAM_POLARS.md`, `docs/UPSTREAM_DUCKDB.md`): a `.duckdb` written by 2.0 is refused by any 1.x, and
  0.7.3's resolver crashes on it rather than falling back (RM344, open); polars 2 writes other parquet bytes, so
  `artifact.digest` differs between two polars releases, even a patch (0.8's RM342 names the toolchain). Capped,
  the lock holds polars 1.44.2, the plugin's own, and duckdb 1.5.6. **Lift when** the plugin's lock moves to 2;
  re-read RM344 then.

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
