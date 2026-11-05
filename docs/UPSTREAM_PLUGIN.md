# Upstream ledger: the module-creator plugin

`dna-seq/just-module-creator`, tags `vX.Y.Z`: the tools the module and curator seats build the annotation module
with. Kept by the liaison seat (`docs/seats/LIAISON.md`); another seat that meets a symptom in the plugin sends it
there rather than writing here. The plugin's repository runs no seats and keeps no consumer inbox: a defect goes
to its issues, through the kit's `report-to-kit --to dna-seq/just-module-creator`.

Watched on the liaison's machine from a clone outside this repository (its line `plugin` in the liaison state
file): `[seat.liaison.watch.plugin]` says each new tag.

## Read mark

**`v0.48.0`**: the tag `.claude/settings.json` pins the marketplace `just-dna` at (3dd8c2a, 2026-11-05), the
latest tag then. A first mark, fast-forwarded: no release before it was read, since nothing here used one. The
liaison moves the pin.

## Backlog

None: nothing before `v0.48.0` is read, since nothing here used it.

## What this repository uses

The plugin `just-module-creator@just-dna`, enabled for every clone (`.claude/settings.json`): its skills
(`find-evidence`, the module authoring guides) and its MCP server's literature and schema tools. Which of them the
module and curator seats call is filled in as they start; not yet seen loaded in a session.

## Inbound verdicts

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
