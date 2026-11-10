# Module — notes

The module seat's working state, rewritten to the present before a reset (`docs/seats/MODULE.md`).

## Now (2026-11-10)

First seated 2026-11-10. The seat-builder's first-seating handout is worked; its first work stands as below.

**Sleeping (the person, 2026-11-10, forwarded by the lead, 639290114): "Module seat sleeps this time."** The
curator's first-five-rows run goes ahead without this seat. No build, no probe and no new projection until the
person or the lead wakes the seat; messages are read and let go meanwhile.

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

## The first curated row, read for the export (2026-11-10)

`rows/46-LPA.yaml` (060c9bd), tier A kept, one variant (rs10455872, three genotypes), seven studies. Not built into
`module/`: the module takes rows through the lead's export (RM1), never by hand. Read against 0.7.1 and sent to the
lead (639271942): studies.csv's key (variant, pmid) collides twice in LPA (probed in a scratch spec: "Duplicate
(variant, pmid): (rs10455872, 29030599)", a warning); the lead's new `nominal` has no 0.7.1 stat_significance
value; the proxy studies' alleles (T, C) belong to rs55730499 and must not land on rs10455872's row. Asked the
liaison whether 0.8 widens the study key.

## v1.2.0, the legacy layer (registry prod, read 2026-11-10)

528 rsIDs, 1022 weight rows, 671 studies, 272 genes; categories antioxidant, genome_maintenance, heat-shock,
inflammation, insulin, lipids, mitochondria, mtor, other, renin-angiotensin, sirtuin, tumor-suppressor. Compiled
strict on compiler 0.7.0, fully resolved; no `weighting:`, no licence, no README, not closed; 126 literature rows,
0 quotes authored. Coverage gaps the compiler names: 307 sites lack the reference homozygote, 186 the hom-alt, 6 a
het. R-LEGACY-1 carries the 528 as tier C/D research-view rows, `flags: legacy_longevitymap`, no weight, neutral.

## Registry

- Polygon (test): answers again by 2026-11-11 (the liaison, 639307944; ledgers 438d527): registry 0.28.5, mode
  test, serving format 0.8.0. The plugin's 0.7.1 gets 409 on every publish, validate, check and download; reads
  work. No rehearsal is possible until the plugin moves to 0.8, token or not (desk #251 updated so).
- Enrich's GWAS pass is broken in every installable enricher (compiler RM428, high): 0.7.3 gets 410 from the
  retired GWAS Catalog v1, 0.8.x sends a page size v2 refuses. An empty GWAS result from `enrich_module` is
  unknown, never "no associations".
- No test token on this machine. Asked of the person; never read from a file, never minted by this seat.
- No rehearsal yet.

## Open

- Avatar: set 2026-11-10, a beaver stacking labelled blocks, drawn by agents-kit/tooling (639270008).
- Token for the polygon: the person's; on the desk as #251 (filed 2026-11-10, unattended). Default on silence: build and check locally, no rehearsal, nothing registered.
- `first seating:` report to the seat-builder: sent.
- On waking: read `docs/format08_reference/` (just-dna-format 0.8's longevity reference example and the compiler's longevitymap v2 shape audit; the lead, 639310707). It notes Timmers 2019 contradicting itself on effect alleles (639310710), which bears on LPA and CELSR2.
