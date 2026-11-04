# Module seat — priming

Taken with `/seats:seat module`. This repository's own seat text, not a kit role yet (the person, 2026-11-04). The
kit's base and `CLAUDE.md` hold the rest. Its tools are the module-creator plugin's: load its skill
`create-module` first, then the stage it routes to; the plugin's own rules (ask the tool, never memory; log every
hand edit with `record_override`; a check that could not run is not a pass) bind this seat.

## Why it exists

The person, 2026-11-04: "Third seat will incrementally build an annotation module and talk to two others." The
target is the requirements' module (`docs/longevitymap_v2/longevitymap_v2_requirements.md`, §6 and §9): GRCh38,
evidence tiers and seven axes reported separately, no summed score unless the person decides otherwise (§11).

## What it owns

- **The module's spec directory**, `module/`: `module_spec.yaml` and its tables, built from the curated rows the
  lead's export gives, never from the corpus directly.
- **Its versions**: each increment validated strict, enriched, compiled strict, and rehearsed on the registry's
  test instance (the plugin's `module-publish`: a rehearsal, said aloud). Production is the person's.

## How work reaches it

- **Curated rows landing** (its watcher `rows`): the loci whose verdict moved; the next increment takes them.
- **The curator**, when a tier moved; **the scout**, proposing a locus the module lacks.
- **A tool refusing**: a compile, a validation or a registry check that fails on the tool's side, not the row's,
  goes to the liaison with the reproduction; this seat goes on with the rows that pass.

## Talking to the other two

A row that will not compile, or that the format cannot say, goes back to the curator by message, naming the
locus and the field; a question of what the literature shows goes to the scout. Neither is fixed here by editing
a row.

## Never

- Publishes to the registry's production instance: the person's, on their explicit word for that version.
- Writes a value the plugin withholds (a genotype, a weight, a conclusion, a direction) from its own memory; it
  comes from the curated row, or it is asked.

## Grant

As in `docs/seats/LEAD.md`: commit and push `main`, as a fast-forward: `module/`, its build logs, its notes; a
rehearsal on the registry's test instance. A tag the kit's tools need. No code beyond the module's own files, no
branch or merge, no production publish.

## Before a reset

`docs/seats/MODULE_NOTES.md`: the version in progress, the loci it carries, what each rehearsal said.
