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

**`v0.48.2`**, the tag `.claude/settings.json` pins (2026-11-06). The first mark, `v0.48.0` (3dd8c2a), was
fast-forwarded: no release before it was read.

**The pin does not bind on this machine.** The person's user settings declare the marketplace `just-dna` with no
ref, and that entry outranks the project's: the client refused `marketplace add 'dna-seq/just-module-creator#v0.48.2'
--scope project` ("its source doesn't match its extraKnownMarketplaces entry in user or managed settings"), and
`plugin update` installs `main`'s head. Seen 2026-11-06: the installed copy was 0.48.0 at `d0f710b` (not the tag)
while the pin named v0.48.1; updated, it is 0.48.2 at `1b622ff`, the tag plus one notes commit, the same code.
How to settle it is the person's (asked 2026-11-06).

## Backlog

None: nothing before `v0.48.0` is read, since nothing here used it.

## What this repository uses

The plugin `just-module-creator@just-dna`, enabled for every clone (`.claude/settings.json`): its skills
(`find-evidence`, the module authoring guides) and its MCP server's literature and schema tools. Which of them the
module and curator seats call is filled in as they start; not yet seen loaded in a session.

## Waiting on its move to 0.8

The plugin caps the compiler's trio below 0.8 until 0.8.0 is on PyPI and both registry instances serve it (read
from `/api/v1/version` on each); its lead will post in `agent-chat > upstream` when it plans the move, so we
switch with it (2026-11-05, their 6c5e4ad). State that day: 0.8.0 on PyPI; both instances (prod and test) serve
registry 0.27.0, format 0.7.1, compiler 0.7.2. Our caps (`docs/UPSTREAM_COMPILER.md`, "Caps") lift with it.

## Inbound verdicts

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
