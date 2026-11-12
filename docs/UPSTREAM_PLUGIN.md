# Upstream ledger: the module-creator plugin

`dna-seq/just-module-creator`, tags `vX.Y.Z`: the tools the module and curator seats build the annotation module
with. Kept by the liaison seat (`docs/seats/LIAISON.md`); another seat that meets a symptom in the plugin sends it
there rather than writing here. The plugin's repository keeps no consumer inbox: a defect goes to its issues,
through the kit's `report-to-kit --to dna-seq/just-module-creator`. Since 2026-11-05 it runs seats (lead, pm,
tester, liaison); its lead wakes on this seat and may wake this seat and our lead (our cdd95d3), for a release or
a change to the tool surface we rely on.

Watched on the liaison's machine from a clone outside this repository (its line `plugin` in the liaison state
file): `[seat.liaison.watch.plugin]` says each new tag.

## Read mark

**`v0.48.8`**, the tag `.claude/settings.json` pins (2026-11-12). The first mark, `v0.48.0` (3dd8c2a), was
fast-forwarded: no release before it was read.

**The pin does not bind on this machine.** The person's user settings declare the marketplace `just-dna` with no
ref, and that entry outranks the project's: the client refused `marketplace add 'dna-seq/just-module-creator#v0.48.2'
--scope project` ("its source doesn't match its extraKnownMarketplaces entry in user or managed settings"), and
`plugin update` installs `main`'s head. Seen 2026-11-06: the installed copy was 0.48.0 at `d0f710b` (not the tag)
while the pin named v0.48.1; updated, it is 0.48.2 at `1b622ff`, the tag plus one notes commit, the same code.
The person's answer (2026-11-06): drop the user-level entry, so the repository's pin binds; theirs to do,
since it is their settings file. Still present on 2026-11-09, so the copy is updated by hand to the pinned
release: `claude plugin update just-module-creator@just-dna --scope project` installed 0.48.8 (2026-11-12), the
tag or main's head plus notes commits.

## Backlog

None: nothing before `v0.48.0` is read, since nothing here used it.

## What this repository uses

The plugin `just-module-creator@just-dna`, enabled for every clone (`.claude/settings.json`): its skills
(`find-evidence`, the module authoring guides) and its MCP server's literature and schema tools. Which of them the
module and curator seats call is filled in as they start; not yet seen loaded in a session.

## Its server on this machine

2026-11-09: after the update to 0.48.4 its MCP server did not connect (`ImportError: FastMCP server support is not
installed`). Ours, not the plugin's: the install's `.venv` held packages with files missing (`mcp/client/`,
`starlette.applications`) that their own RECORD lists; the 0.48.2 install was broken the same way, the 0.48.0
one whole. Likely several sessions starting `uv run` on a fresh `.venv` at once (the kit's #300, the MCP start
race). Repaired with `UV_LINK_MODE=copy uv sync --no-dev --reinstall` in the install directory. Routine after each
plugin update: that sync once, then the sessions reconnect (`watchdog.py reload --mcp`).

## Its move to 0.8 (done)

Done with `v0.48.7` (2026-11-12): the trio `>=0.8.4,<0.9`, `just-dna-registry>=0.29.1`, polars and duckdb still
`<2`. Our side moved the same day (`docs/UPSTREAM_COMPILER.md`, "Caps"). What follows is the state before it.


The plugin caps the compiler's trio below 0.8 until 0.8.0 is on PyPI and both registry instances serve it (read
from `/api/v1/version` on each); its lead will post in `agent-chat > upstream` when it plans the move, so we
switch with it (2026-11-05, their 6c5e4ad). State that day: 0.8.0 on PyPI; both instances (prod and test) serve
registry 0.27.0, format 0.7.1, compiler 0.7.2. Our caps (`docs/UPSTREAM_COMPILER.md`, "Caps") lift with it.

## Inbound verdicts

- **`v0.48.8`** (2026-11-12). Nothing breaks; toolchain unchanged (the trio 0.8.4, polars 1.44.2, duckdb 1.5.6).
  *For the module seat:* `registry_lane_lookup` reads one snapshot lane a registry holds, by key, without a
  download (registry 0.30); `remote_derive` takes 0.30's `passes`, `live` (off by default) and an interval, and
  returns `passes_report`; `enrich_expression_effects(rows=true)` names, under `no_gene_candidates`, the MANE genes
  within reach of a position whose rows author no gene (hints only, nothing written). Install synced by hand.
- **`v0.48.7`** (2026-11-12): **just-dna 0.8.** Its server runs format, compiler and enricher 0.8.4 (polars 1.44.2,
  duckdb 1.5.6), so our caps below 0.8 lift with it, and the 0.8 adoption's mechanical half is done here the same
  day. 0.48.6 and earlier get HTTP 409 from both registry instances once they serve 0.8. *For the module seat:* the
  GWAS pass works again (RM428), at one request a second, and `enrich_gwas_effects` names a refused page size;
  `validate_module` is the compile's own pre-flight (0.8 runs the resolution step) and 0.8's eleven new warning
  codes are in the symptom table; `enrich_module` names `allele_mismatches` (0.8 writes no `not_found` row);
  `fetch_fulltext` tells an outage from an absent copy (F133); `lookup_citation(doi=…)` no longer puts a PMID in
  `pmid`; `registry_rename_namespace` is new; `opentargets enrich`, `ld-pairs` and `clinvar-gkm lookup` have no
  tool yet. Install synced by hand; the import is clean on 0.8.4.
- **`v0.48.6`** (2026-11-11). Nothing breaks; toolchain unchanged (trio below 0.8, polars 1.44.2, duckdb 1.5.6).
  *For the module seat:* `validate_module` now returns `warnings_summary` and `carried`; `enrich_gwas_effects` says
  the GWAS Catalog retired v1 (410) and that retrying or editing will not help (F146; the compiler's RM428, its
  fix on their main as f0433de5, not yet released); `remote_derive` and `remote_draft` name a 409 contract skew as
  the instance's (F144), which the polygon on format 0.8.0 now gives. Install synced by hand; the import is clean.
- **`v0.48.5`** (2026-11-10). Nothing breaks for us. *For the module seat:* `validate_module`, `compile_module`
  and the drafters now add `on_this_surface`, the plugin tool that does what an upstream message's CLI command
  names (F132), and `top_expression_effects` explains `gene_not_at_locus` in its result (F140). `registry_register`
  no longer echoes a reused install-id (F126). Its weekly bump moved duckdb to 1.5.6, as our lock has; the trio
  caps are unchanged (below 0.8; enricher 0.7.3, compiler 0.7.2, format 0.7.1), polars 1.44.2. Its install's
  environment synced by hand after the update, the routine above; the import is clean.
- **`v0.48.3`, `v0.48.4`** (2026-11-08, -09). *Levers for the curator:* `fetch_fulltext(doi=…)` finds what a PMID
  would (F122), which covers our `doi-` notes; an empty `fetch_fulltext` with a known PMCID says to call again,
  since Europe PMC refuses some requests at random (F133). *For the module seat:* `audit_module` names recorded
  checks older than the last edit (F139), derived rows nothing authors any more (F137), and no longer decides on a
  stale attestation (F138); `check_pgx`, `draft_from_strchive` and the expression tools say what they did. Nothing
  breaks for us; caps unchanged (the trio below 0.8, polars 1.44.2, duckdb 1.5.5).
- **`v0.48.2`** (2026-11-06): `fetch_fulltext(pmid=…)` falls back to PubMed for the PMCID and DOI when Europe PMC
  lacks them (F31), a *lever* for the curator, who reads full texts through it; an empty open-access answer names
  the DOI asked (F50); the suite is hermetic (F119), and no longer reads a sibling checkout of just-dna-format.
  Caps unchanged (the trio below 0.8, polars 1.44.2, duckdb 1.5.5).
- **`v0.48.1`** (2026-11-05), one entry: `remote_derive` and `remote_draft` send the registry token, and refuse
  before uploading when none is found. *Nothing for us*: neither tool is called here yet. The tag also carries
  RM31's traceability design and F116's note, documents only (`CLAUDE.md`, `docs/ROADMAP.md`,
  `docs/just-dna-format-pending-fixes.md`), no code. Pin moved: a patch, nothing here depends on the old behaviour.
- **`skills/find-evidence/references/QUOTING.md` at `v0.48.0`**, read 2026-11-05 against D9 and `docs/FORMATS.md`,
  with the check it describes (just-dna-enricher 0.7.3's `quote_matches`, `literature.py:654-660`: whitespace
  collapsed and case folded, nothing else, against Europe PMC's body text). Filed as #7 for the lead and the
  curator. *Breaks an assumption:* a quote passing `loci check quotes` can score `quotes_found = 0` upstream (our
  typography forgiveness, our cache against their text, supplements). *Levers:* refuse a quote equal to the note's
  title; per-(pmid, rsid) grain; the four kinds of empty quote; a table row taken by regex; `curator` as an
  identity, never `ai`. *Fits:* `curator` per study row, readings by depth. Landed by the lead: fcbc03f, cba10a6; the
  text-source gap is RM1. #7 closed.

## Our pieces that duplicate the plugin's

None yet.

## Outbound

None yet.
