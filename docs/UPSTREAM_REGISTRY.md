# Upstream ledger: the registry

`dna-seq/just-dna-registry`, tags `vX.Y.Z`: where the module is published, and whose test instance the module seat
rehearses each version on. Kept by the liaison seat (`docs/seats/LIAISON.md`); another seat that meets a symptom in
the registry sends it there rather than writing here. A defect goes to the registry's consumer inbox, restated in its
terms. Its triage is not seated on this machine (2026-11-12), so an append to this machine's clone never reaches it:
send the section whole to `just-dna-registry/triage` by `bin/hand.sh`, after asking it for the next id, as the
compiler's triage asked of us.

Watched on the liaison's machine from a clone outside this repository (its line `registry` in the liaison state
file): `[seat.liaison.watch.registry]` says each new tag.

## Read mark

**`v0.31.1`** (2026-11-13, seen 2026-11-14), read whole (below); `v0.31.0` and `v0.30.1` the same day. Before it, **`v0.30.0`** (2026-11-12): the release the module seat first ran against, its first rehearsal on the polygon
(`test-longevity-loci/longevitymap@2.0.0`, our 0fa5e77; strict validate and compile green). Tags before it are
fast-forwarded past, read only by their changelog headings as listed below; nothing here used them.

History before the mark: the latest tag when this ledger began (2026-11-05) was `v0.27.0`. Tags read by heading,
not used: `v0.27.1`, `v0.28.0` to `v0.28.6`, `v0.29.0`, `v0.29.1` (0.29.1: floors format, compiler and enricher at
0.8.4; 0.29.0: a namespace renames, its old name kept as an alias; 0.28.5: `GET /caches` names each lane's
readers; 0.28.6: docstrings, S28); 0.30.0 (a caching proxy per snapshot lane and per derived-table pass, `GET
/lanes/{lane}`, `derived?passes=`, client calls optional and additive). The instances: on 2026-11-09 production
served registry 0.27.0 and format 0.7.1 and the polygon answered HTTP 502, still 502 on 2026-11-10; the polygon came
back on 2026-11-11 on format 0.8.0, then 0.29.1 on 0.8.4, refusing our 0.7.1 client with 409. On 2026-11-12
production answered 502 in the morning, and by the afternoon both instances served registry 0.30.0 and format
0.8.4, compatible with the plugin's v0.48.7 client.

## Backlog

None: nothing before the first release in use is read, since nothing here used it.

## What this repository uses

Through the plugin's registry tools (the module seat's): `registry_health`, publish, validate and check against the
polygon, under the namespace `test-longevity-loci` (the default; the person's word on it is open). Nothing goes
to production and the module is not closed without the person's word (the lead, 2026-11-12). Re-exported and
re-rehearsed once per curation batch.

## Inbound verdicts

- **`v0.31.1`** (2026-11-13). The operator's `registry upgrade` re-derives and publishes in one pass (a held
  result kept for `--accept-drift`), and Ctrl-C names what still runs. Client surface unchanged; nothing we call.
- **`v0.31.0`** (2026-11-13). Additive: client surface unchanged, three new calls (`variant_claims`,
  `gene_claims`, `list_modules(pgs_id=)`); server floors the trio at 0.8.6, a patch that moves nothing a caller
  reads (ours stays 0.8.5 with the plugin's server, `docs/UPSTREAM_COMPILER.md`). *A lever for the lead and the
  curator, once the plugin has a tool for it:* a variant-level catalog of what every published module says about
  one variant (`GET /variants?key=`, by rsID, VRS id or coordinates) or one gene, with a marker where two modules
  give the same allele, genotype and trait opposite directions, and a count of pairs it could not compare. A fact
  about two statements, never a verdict. Nothing to change here.
- **`v0.30.1`** (2026-11-13). Client surface unchanged; the server floors the trio at 0.8.5, as ours does. *For the
  module seat:* a `remote_derive` asking live passes (`offline=false`) now gets them, where 0.30.0 answered every
  live pass "skipped: offline" from the box's own switch; each live source stays gated by the operator.
  `registry upgrade`'s re-derivation reasons are the operator's, nothing we call. A keyed lane lookup answers every
  held lane whatever its terms (the 0.30 ruling, now in the API reference). Nothing to change here.

## Our pieces that duplicate the registry's

None yet.

## Outbound

None yet.
