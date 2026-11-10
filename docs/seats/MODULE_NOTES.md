# Module — notes

The module seat's working state, rewritten to the present before a reset (`docs/seats/MODULE.md`).

## Now (2026-11-10)

First seated 2026-11-10. The seat-builder's first-seating handout is worked; its first work stands as below.

- **Version in progress: 2.0.0**, scaffolded in `module/` with the plugin (v0.48.5, format 0.7.1, compiler 0.7.2):
  `module_spec.yaml`, header-only `variants.csv`, `studies.csv`, `licensing.csv`. No rows, no loci yet.
- **Strict validation refuses the empty scaffold**, verbatim: "studies.csv is present but has no study rows.
  Grounding evidence is mandatory." That is the format's rule, not a defect: the module validates once the first
  curated locus lands. No stub row was added to turn it green.
- **The spec's hand-filled cells are the requirements' recommended defaults, not decisions**: D1 (`weighting:
  scale none`, order by priority), D3 (name `longevitymap`, title "Longevity genetics"), §6.2's `defaults:`. Each
  logged with `record_override` (`module/logs/authoring.log`). `license:` left out until the person names one.
- **Deferred table kinds**, added by `scaffold_module` when their turn comes: `haplotypes.csv` + `diplotypes.csv`
  (APOE, D2, after R-APOE-3's render check in just-dna-lite), `pgs.csv` (PGS000906, opened in the PGS Catalog at
  curation time). `licensing.csv` gets HAGR's row (CC BY 3.0, R-LEGACY-3) with the first increment.
- **Format version**: the scaffold's headers are 0.7.1's. RM1's export targets 0.8's columns; the module moves to
  0.8 when the plugin does (it waits on 0.8.0 on PyPI and both registry instances serving it). No 0.8 column is
  hand-added before then.

## v1.2.0, the legacy layer (registry prod, read 2026-11-10)

528 rsIDs, 1022 weight rows, 671 studies, 272 genes; categories antioxidant, genome_maintenance, heat-shock,
inflammation, insulin, lipids, mitochondria, mtor, other, renin-angiotensin, sirtuin, tumor-suppressor. Compiled
strict on compiler 0.7.0, fully resolved; no `weighting:`, no licence, no README, not closed; 126 literature rows,
0 quotes authored. Coverage gaps the compiler names: 307 sites lack the reference homozygote, 186 the hom-alt, 6 a
het. R-LEGACY-1 carries the 528 as tier C/D research-view rows, `flags: legacy_longevitymap`, no weight, neutral.

## Registry

- Polygon (test): HTTP 502 at 2026-11-10 ~20:24 UTC (`registry_health`: reachable false, mode null; unknown, not
  a pass). Known since 14:58 UTC; the registry's lead has asked the maintainer.
- No test token on this machine. Asked of the person; never read from a file, never minted by this seat.
- No rehearsal yet.

## Open

- Avatar: set 2026-11-10, a beaver stacking labelled blocks, drawn by agents-kit/tooling (639270008).
- Token for the polygon: the person's.
- `first seating:` report to the seat-builder: sent.
