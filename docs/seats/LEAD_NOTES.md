# Lead — notes

The lead seat's working state, rewritten to the present before a reset (`docs/seats/LEAD.md`, "Before a reset").

## Now (2026-11-05)

First seating, the seat-builder's handout:

1. Leak gate: done. The list is metabonet's, on the person's word (2026-11-05: "Take stopwodrs list from
   metabonet"), replacing a longer one the lead drafted.
2. Rules: done, 3e7ed57.
3. Groundwork: done, 3b38d74 (just-dna-lite at 050bf9f). The person told, so its folder there can become a pointer.
4. Cluster: done, differently from the handout. The machine file's `job_prefix` is one value (metabonet's `mn-`)
   and outranks the repository, so this clone sets `JOB_PREFIX=ll-` and `LOCI_CACHE` in its untracked
   `.claude/settings.local.json` env. The digest line read through that setting is not yet seen at a session
   start (checked with the variable inline). Nodes watcher alive.
5. Formats and checks: done, 8496cca; a critic's read is in flight, its fixes additive.
6. Inputs (v1.2.0's tables, HAGR Build 3 with its licence): open, unattended.
7. Trust register: asked the person.
8. Pin: nothing to move.

## To file (unattended, at the next idle turn)

- Kit: `[slurm] job_prefix` in the machine file is one value for every repository on the machine and wins over
  the repository's; a second repository on one cluster cannot have its own prefix without an env override.
- Liaison: the module-creator plugin is not installed on the lead's machine; `QUOTING.md` (D9) is unread.
- Kit: the kit's pin lives in `.claude/settings.local.json` (untracked), so another clone does not inherit it.

## Open

- Avatar request to the admin seat; the `first seating:` line to the builder, once the items above have states.
