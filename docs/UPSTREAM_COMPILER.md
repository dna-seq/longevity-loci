# Upstream ledger: the compiler's packages

`just-dna-format`, `just-dna-compiler` and `just-dna-enricher`, released together from `dna-seq/just-dna-compiler`
with tags `vX.Y.Z` (the tag names the cut; each package carries its own version). Kept by the liaison seat
(`docs/seats/LIAISON.md`); another seat that meets a symptom in these packages sends it there rather than writing
here. A defect goes into the compiler's consumer inbox, `docs/CONSUMER_SUGGESTIONS.md` in its clone, restated in
its terms with the next `Sn` from its ledger, appended and never committed; then a mention of
`just-dna-compiler/triage` in `agent-chat` naming the `Sn` (its triage wakes on this seat since their a8262397).

Watched on the liaison's machine from a clone outside this repository (its line `compiler` in the liaison state
file): `[seat.liaison.watch.compiler]` says each new tag. The `0.8` branch closed at the cut (`edf2661c`) and its watcher
was retired; `main` takes the 0.8.x patches, which come as tags. The coming minor (`0.8`) is built on a branch of its own;
the compiler's liaison maps it, and is asked before this seat maps it again. The registry's liaison keeps an
adoption map of `0.8` (rows M1 to M11, in `docs/UPSTREAM_COMPILER.md` of `dna-seq/just-dna-registry`, read from the
compiler's `0.8` branch); reuse it at the cut, and tell that liaison where our use differs (its offer, 2026-11-05).

## Read mark

**`v0.8.4`** (tagged 2026-11-11, `36cbc20f`), patches on 0.8.0 read by their changelog headings and "After
upgrading" lines; read whole at our adoption. **In use: `v0.8.4`** since 2026-11-12, the trio at 0.8.4 in `uv.lock`,
adopted with the plugin's `v0.48.7`; 0.7.3 (enricher), 0.7.2 and 0.7.1 before it. The first mark, `v0.7.3` (3dd8c2a),
was fast-forwarded: no release before it was read.

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
- **Cut as 0.8.0** (2026-11-05, `edf2661c`; `main` at `e97339a3`): no behaviour change since `c90e6d98`. Tagged
  `v0.8.0` the same day. Read; not adopted: it waits on the plugin (its cap below 0.8), and our cap holds it out.

## 0.8.1 to 0.8.3, for the adoption

- `cache pull` with no `--only` now also fetches the Open Targets lane (~5.5 GB, RM408): at adoption pull
  `--only ensembl`, as the upgrade order says.
- Gene-metrics rows from the live gnomAD API are labelled `gnomad_api_constraint`, no longer `gnomad_v2.1.1_constraint`
  (RM417); the constraint snapshot is gnomAD 4.1.2 (RM410).
- `cache rebuild --dry-run` no longer writes (RM411); `--pin` is taken or refused (RM416).
- 0.8.3 (a patch, no recompile, no public name added): floors `>=0.8.3` across the trio; one `cache pull` or
  `cache prepare` moves a pulled lane to the hub's release (constraint 4.1.2, STRchive 2.28.0), and a STRchive pulled
  before it is moved aside first. A `verification.json` from 0.8.2 or earlier over edited bytes may carry stale
  records (RM423): re-run its checks at adoption. A `resolution.csv` row no table names now warns
  `derived_row_orphan` (RM422); `enrich` never removes it.
- 0.8.4 (a patch, no recompile; its release record shows no move on 22 reference modules): floors `>=0.8.4`. It
  carries RM428's fix (the GWAS pass asks for pages of 500, and asks a refused first page once more with no size)
  and three wording fixes (RM425 `effect_size` is the single strongest track, RM426, RM427). At adoption, run the
  GWAS pass (`just-dna-enricher gwas <spec-dir>`) on the module again: every pass run here on 0.7.3 filled nothing.

## Caps

- **`just-dna-enricher`, `just-dna-compiler`, `just-dna-format` `>=0.8.4,<0.9`** (2026-11-12): the plugin's
  `v0.48.7` range. The two caps below 0.8 that follow are lifted that day. The enricher cache on this machine held
  no lane (`cache status`: every lane absent), so nothing was moved aside; the first `cache pull --only ensembl`, or
  the plugin's `provision_caches`, writes the 0.8 lane fresh. The module is a header-only scaffold (no artifact, no
  `verification.json`, no GWAS sidecar), so the recompile, `enrich --rederive`, verification and GWAS re-run steps
  of the upgrade order have nothing to act on yet.
- *Lifted 2026-11-12:* **`just-dna-enricher<0.8`** (2026-11-05, the liaison's). 0.8.0 is cut (`edf2661c`) and goes to PyPI on the
  maintainer's publish; the weekly bump would then take it. Its enricher pulls the Ensembl lane from a new
  repository (`ensembl_variations_split`) into the same `<base>/ensembl_variations` directory, re-pulling a cache
  that names the old one, and a cache holding both releases resolves to nothing (§1.29, upgrade order step 3). The
  plugin's server, capped below 0.8, reads that directory on this machine. **Lift when** the plugin moves to 0.8;
  then the upgrade order is the guide's §2: floors, `uv lock`, `cache pull --only ensembl` once, recompile,
  `enrich --rederive` online, validate.
- *Lifted 2026-11-12:* **`just-dna-compiler<0.8`, `just-dna-format<0.8`** (2026-11-12, the liaison's). Enricher 0.7.3 does not cap
  them, and the weekly bump took both to 0.8.4 beside it, out of the plugin's 0.7.2 and 0.7.1. **Lift with** the
  enricher's cap.
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

- **RM428, the GWAS pass (2026-11-11, from the plugin's liaison, S143; severity high).** The GWAS Catalog retired
  its v1 API, so enricher 0.7.3, ours and the plugin's, gets HTTP 410 on every rsID; 0.8.3 and their main send
  `size=1000` to v2 `/associations`, which refuses above 500. No installable release has a working GWAS pass.
  For us: the module seat's `enrich_module` / `enrich_gwas_effects` returns no GWAS effects until a fix ships; an
  empty GWAS sidecar is not "no associations". Whether a 0.7.x patch is cut is RM428's ask 4, the compiler's
  person's call: declined (their desk #252, 2026-11-11), so no 0.7.x fix comes; the pass works again only from
  0.8.4 (on PyPI and tagged 2026-11-11, `36cbc20f`; RM428 closed there), i.e. with our 0.8 adoption. Nothing to file
  from here.

## Our pieces that duplicate the compiler's

None yet.

## Outbound

- **S130, S131** (2026-11-12, for the lead, from RM1's export to 0.8.4): format wishes. S130, `stat_significance`
  has no level for a replication at p < 0.05 (D11), or the description should name `p_value_num` as the field to
  read; S131, a study-level direction beside `effect_allele` for a study printing no effect size (D13). Meanwhile
  the export writes `not_significant` with the P kept and "nominal replication look-up (p < 0.05)" in
  `statistical_test`, and the direction in `conclusion`. Appended uncommitted; triage told in `agent-chat >
  upstream`. Open.
