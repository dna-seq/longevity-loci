# Module — notes

The module seat's whole working state, rewritten 2026-11-16 for the move to another chat organisation (the person:
"Make sure they commit all to notes, transcripts are not moving"). A fresh session carries on from this file, the
priming `docs/seats/MODULE.md`, `CLAUDE.md` and the base. The history of every build is in git (`git log --
docs/seats/MODULE_NOTES.md module/`); the last section keeps only what is still worth reading.

## Now (2026-11-16, evening)

- **Holding at the batch-seventeen rehearsal**, trunk 12c673f, commit 3ee0bbb. Version 2.0.0 of
  `test-longevity-loci/longevitymap` is on the registry's **test instance only** (the polygon,
  https://module-polygon.just-dna.life), published 2026-11-16T16:51:55Z, content_signature
  `sha256:aebf5e38c20414a8bd766e1c92950c4a838092bdeeda6b9d3526789c2d9a44d1`, equal locally and on the polygon.
- **What it holds**: 164 rows (A 15, B 73, C 41, D 35): the 161 seed loci in 156 rows plus the eight second
  signals 162 to 169. 489 variant rows, 679 studies, 6 haplotypes (APOE ε2, ε3, ε4), 12 diplotype results (six
  ε pairs, a lifespan and an Alzheimer's result each). 245 rsIDs resolved, none unresolved, no ref or allele
  mismatch.
- **Warnings, unchanged in kind since batch twelve**: 20 `vrs_id_unverifiable` lines (21 indel alleles, carried;
  no edit clears them), `module_not_closed`, one `dataset_currency` finding (ClinVar).
- **Since the rehearsal, nothing in `rows/` or `src/longevity_loci/export.py` changed** (checked at 1ffba5f): only
  the lead's quote-check code, a corpus note (Pisanu 2026, FURIN, telomere length not mvAge) and notes files. The
  rehearsal is current. The scout's queue is empty and every seed locus has a row (the curator, 640847775).
- **Nothing is unpushed** for this seat.

## Standing orders

- **The lead (639797615, repeated per batch): hold at the rehearsal. No production publish and no close without
  the person's word.** Re-export and re-rehearse after each curation batch the lead closes, not per row.
- **Production is the person's alone**, on their explicit word for that version. "Publish it" from a seat is not
  that word.
- **The production route, the person 2026-11-19 (desk #56, relayed by the lead 641719095)**: a pull request into
  just-dna-lite carrying the ready module, superseding the v1 port (1.2.0 stays frozen). The lead opens it with
  module/ at 3ee0bbb (the 12c673f rehearsal, signature aebf5e38), without published.json. This seat answered
  (641719261): no licence in the spec, not closed, the spec comment and provenance still call D1/D3 pending
  defaults; each waits on a word. The compiler trio 0.8.9 (RM449, our four mirrored indels) is on PyPI, not yet in
  the plugin's lock. The PR is just-dna-lite#37 (the lead, 641721970), our four points open in its "before
  publishing" list; the lead also wants studies.csv's analysis and conclusion text worded for a reader (it cites
  decision and quote ids raw), a plan item for the lead, the curator and this seat, not yet set.
- **The org move (the lead, 640874040)**: a ticket for this seat may arrive from genie's secretary (another
  organisation). Leave it unread until the lead says the person has given the go; do not run the org-move switch
  before. Done 2026-11-17: the move finished by the org-move tool and this seat punched in again in
  desk-antonkulaga from a handoff. The held-back ticket (640873673) was never read or used; its description could
  not be posted (the new account may not post in the old organisation's `embassy-review`), so it is moot.
- The registry token is never repeated, quoted or stored; it lives in the plugin's local state on this machine.

## Waits on whom

- **The person**:
  - production publish of 2.0.0;
  - closing the module (`close_module`);
  - a licence for `module_spec.yaml` (left out until they name one);
  - **how the app (just-dna-lite) shows the ε pairs and the 19 studies at rs429358/rs7412** (studies with no
    variants.csv row, kept in studies.parquet with no warning). Unchecked; this seat runs the app only on an ask.
    Say so in every rehearsal report.
- **The lead**: the next batch's close, which triggers the next rebuild. No batch is open now.
- **The registry**: v0.32.0 is tagged and on PyPI, not yet served (polygon 0.30.0, production 0.31.0). Under it,
  `curated` counts only a verified review by someone with no role on the namespace, so we cannot mark our own
  module curated; variant claims fold spellings and say `matched`.

## The rehearsal routine (each batch the lead closes)

1. `git pull --ff-only` (its "Cannot fast-forward to multiple branches" is harmless); `uv run loci check rows`.
2. `git status`: **no uncommitted row edits in the tree.** The clone is shared and the export reads the working
   tree, so a curator's uncommitted edit rides along (it happened once, at 7040f7d).
3. `JMC_TRACE=0 uv run loci export` (writes `module/`; since plugin v0.48.15 the trace hook also catches Bash writes, so
   without the variable this session leaves `module/logs/trace/*.jsonl`, tracked and shipped). Read its summary of what 0.8 has no place for, against the last
   build's; a moved count is a row change to name in the report.
4. Remove the previous build output (a `2.0.0` folder on the data volume, outside the repo).
5. `enrich_module` on `module/` (runs a few minutes in the background), then `compile_module` strict into that
   folder. Read `warnings_summary`, `carried`, `actionable`, `resolution_subjects`, `fully_resolved`.
6. `registry_delete_version` test-longevity-loci/longevitymap@2.0.0 on target test, then `registry_publish` (target
   test, a changelog continuing the last). The tool's returned receipt is stale: ignore it.
7. Verify by GET `https://module-polygon.just-dna.life/api/v1/modules/test-longevity-loci/longevitymap`:
   `versions[0].content_signature` must equal the local compile's; `artifact_digest` differs every time (the
   server recompiles with its own toolchain) and that is expected. `latest_manifest.published_at` is the time.
8. `module/published.json`: set `deleted_at` on the last entry to the new published_at, append the new entry
   (target, canonical_id, namespace, name, version, owner `longevity-loci`, artifact_digest and content_signature
   from the registry, registry_url, published_at).
9. A line in this file; `git commit --only -- module/variants.csv module/studies.csv module/quote_sources.csv
   module/resolution.csv module/verification.json module/published.json module/haplotypes.csv
   module/diplotypes.csv docs/seats/MODULE_NOTES.md` (wait out `.git/index.lock` first), push.
10. Reply to the lead: counts, warnings and anything new, the content_signature, the app-display line.

**Trial builds** (rows landed, batch not closed): copy `module/` to the scratchpad, `uv run loci export DIR`,
enrich and compile there, note the result here. Never publish a trial. When the shared tree holds a
curator's uncommitted row, export from a worktree at the trunk head instead: in the clone's `.worktrees/`
(the kit's `bin/wt.sh NAME`), never in the scratchpad (base, kit #536), and removed once the trial is noted. They catch a strict refusal early (batch
eleven's was 101's proxy allele).

## What the projection does (settled, so not asked again)

- **Marker rows (D32, D37.12, D38, D39)**, the biological-ageing section: category `ageing_markers`, every genotype
  state neutral, direction `unknown` (the lead, 640645516: a marker row's direction speaks to longevity, where it
  is not known), weight null, `trait_efo_id` the marker's own (OBA_0003784 telomere length, EFO_0022597 epigenetic
  age acceleration, EFO_0006312 mtDNA copy number, EFO_0007783 loss of Y, EFO_0010602 brain age, EFO_0000473 on
  112), the tier a flag token. BIOMARKER studies carry the marker trait; lifespan and healthspan look-ups their own.
- **An empty gene is intended** (the lead, 640667466): the design names a gene only at effector E1 or E2
  (R-CAUSAL); 23 and 112 are E3, so `gene: ""`.
- **APOE (D33, desk #307)**: ε pairs in haplotypes.csv and diplotypes.csv; rs429358 and rs7412 have no variants.csv
  row ("variant has no genotype states", 2), and their 19 studies stay in studies.parquet with no warning (0.8's
  documented behaviour, RM28). A diplotype row has no pmid link; its grounding is its conclusion text.
- **second_signal_of and also_loci** have no 0.8 column; since c3b59df the export counts them by seed id (second
  signals at 25 ×2, 28, 37, 52, 53, 82, 99; also_loci 102, 104, 142, 157, 158). Each second signal reads as a locus
  of its own in the module. No flag token for now (the lead, 640736678).
- **Unharmonised variant directions** are written as the row holds them (3 now: 66's rs1126809, 86's rs4268748,
  169's rs4784227 after D40.1). APOE's rs429358 also says risk but has no genotype rows.
- Nominal studies are written `significant` with "not genome-wide" in `statistical_test` (RM434: the authors'
  verdict at their own threshold); one-sided P, percentile designs and derived effects go into
  `statistical_test` or `effect_unit` text; a study direction without an effect size goes into `conclusion`.
- Multi-allelic indels (rs35257605's poly-T, rs371933919, rs3830412) expand to several loci on enrich; their VRS
  ids are minted upstream and carried unverified.

## Toolchain and registry

- Plugin `just-module-creator` pinned by the liaison at v0.48.13 (96ad6e1, 2026-11-17; enricher 0.8.7, format and
  compiler 0.8.6). New in it: `registry_publish` refuses a spec whose module_spec.yaml names another name or version
  than the publish (ours: longevitymap 2.0.0, matching); the log check reads every shipped `logs/` file. The
  liaison moves the pin; this seat reloads. The kit (seats) is at v0.1.232.
- **v0.48.14 (enricher 0.8.8), pinned 62c3d19, 2026-11-18; reload queued.** The shared enricher cache's ClinVar
  moved to clinvar_2026-11-15 (3d73d49), so the next enrich may differ from 12c673f's for that alone: name it in
  the report, not as a row change. Publish needs the rehearsal name equal to module.name (ours matches). A
  provenance hook writes module/logs/trace/*.jsonl when a session hand-edits a module CSV; it is tracked and
  would publish. loci export does not trigger it; never hand-edit module/, and check git status for logs/trace.
- Plugin caches live on the data volume (`remember_setting JUST_DNA_PIPELINES_CACHE_DIR`, user config); the
  Ensembl lane (about 15 GB) is there. `$HOME` is the small volume.
- Polygon account `longevity-loci`, namespace `test-longevity-loci` claimed there. Production's existing
  longevitymap 1.2.1 is under `just-dna-seq`; the namespace for a production 2.0.0 is the person's call with the
  publish (asked 2026-11-12, not answered).
- The name `longevitymap` is not test-prefixed, so the operator's sweep keeps it: always delete before republishing.
- Enrich's GWAS pass: an empty GWAS result is unknown, never "no associations".

## Learned

- A green strict compile is determinism, not correctness: read the warnings and the export's summary every time.
- The shared clone's working tree is the export's input: check `git status` before a real export.
- The publish tool's receipt is stale and its "different artifact_digest" note is the server's recompile; the
  check is the content_signature.
- The polars `is_in` deprecation in scratch scripts: use `.implode()`.
- A progress commit saying a batch's corrections are done is the curator's done; still check `git status` before
  a real rebuild.

## Build history (rehearsals on the test instance; content_signature equal local and polygon each time)

| Batch | Trunk | Variant rows | Studies | Signature |
|---|---|---|---|---|
| first | 17e7770 | 192 | 331 | |
| 8 | 2d16f3d | 216 | 370 | |
| 9 | dfb21f9 | 249 | 427 | |
| 10 | 571e5b1 | 279 | 465 | |
| 11 | 1e0cc6f | 303 | 496 | 0fb54bbf |
| 12 | ca028a8 | 336 | 529 | 68e345d2 |
| 96 APOE | 7040f7d | 342 | 554 | 688ef9e7 |
| 13 | efb975f | 360 | 571 | 0abd2bde |
| 14 | 3b2c3f1 | 408 | 615 | cc75b113 |
| 15 | c483cf3 | 429 | 634 | da319d43 |
| 16 (seed complete) | ed22ea4 | 465 | 652 | 35d1122a |
| 17 (second signals) | 12c673f | 489 | 679 | aebf5e38 |

The APOE probe `test_apoe_probe@0.0.1` was published and deleted (desk #307 settled). The legacy v1.2.0 on
production (528 rsIDs, 671 studies, compiled on 0.7.0) is R-LEGACY-1's research-view layer, not built into 2.0.0.

- 2026-11-17: moved to the chat organisation desk-antonkulaga (bin/org-move.py).

- 2026-11-18, trial at 3b7c46b (the backfill read: row 170 CYP26A1-MYOF, the first locus outside the seed, at C;
  73 KL's replication_failed; notes on 18 rows): strict green, never published. variants 492, studies 682,
  haplotypes 6, diplotypes 12; 246 resolved, none unresolved, no ref or allele mismatch. Warnings as at 12c673f
  (20 indel VRS lines, no new indel; not closed; ClinVar currency). Export summary unchanged but for row 170's
  counts. Next block in curation: the GWAS Catalog's 13 lines as rows on 170's pattern; the rebuild waits for the
  lead's close.

- 2026-11-18, trial at 717de08 (rows 171 MYL2-VHRT, 172 SRRM3-POR, 173 B3GLCT; plugin v0.48.14, enricher 0.8.8,
  ClinVar 2026-11-15 in the cache): strict green, never published. Exported from a clean worktree, since the
  shared tree held the curator's unparsed, uncommitted 174. variants 501, studies 689, haplotypes 6, diplotypes
  12; 249 resolved, none unresolved, no ref or allele mismatch, 8 VRS minted. Warnings as before (20 indel VRS
  lines, not closed, one dataset_currency). second_signal_of now counts 71 (171). content_signature cef8e5fc.

- 2026-11-19, RM6 re-export for just-dna-lite#37 (the lead, 641725979): the 2.0.0 content (rows and corpus as at
  12c673f, in a worktree) exported with c6586ae's reader text, JMC_TRACE=0. Only studies.csv changed (3,183 decision
  and quote id tokens before, none after); variants 489, studies 679, haplotypes 6, diplotypes 12. The first compile
  warned verification_stale (the attestation was over the old bytes); re-enriched to attest: resolution, licensing
  and provenance unchanged byte for byte, verification.json now enricher 0.8.8 with ClinVar 2026-11-15 as the
  superseding release, and its witness check says nothing_to_check (recorded rows are compared only under
  --rederive; 0.8.6 had compared one). Strict green, warnings as usual (20 indel VRS, not closed, one
  dataset_currency), 245 resolved. content_signature c76726fd (was aebf5e38, the text alone). Not published.
- 2026-11-19, the second RM6 re-export (the lead, 641728864): rows and corpus as at 12c673f plus the curator's nine
  reader edits of 72f7810 (applied cleanly), export code d9eb9b6 (row numbers as locus names, the punctuation an id
  left closed), JMC_TRACE=0, re-enriched to attest. Only studies.csv and verification.json move; no id tokens left.
  variants 489, studies 679, haplotypes 6, diplotypes 12; strict green, warnings as usual. content_signature
  2b3f2e01. Not published.
