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
5. Formats and checks: done (8496cca, the critic's fixes 80eb769, 0.8's study fields 433a1d0 from issue #6,
   D10).
6. Inputs: done, `docs/INPUTS.md` (v1's sqlite, HAGR Build 3, a live snapshot; CC BY 3.0). v1.2.0's registry
   tables are the module seat's to fetch with the plugin.
7. Trust register: desk #200, default "later, at the module seat's first publish".
8. Pin: nothing to move.

## To file (unattended, at the next idle turn)

Nothing. Filed: kit #272 (job_prefix per machine), kit #273 (the kit pin in untracked settings). The plugin is
installed (v0.48.0), and `QUOTING.md` read into D10.

## Open

- Avatar asked of the admin seat (agent-chat, avatars); set it with `watchdog.py avatar lead --from ID` when the
  reply comes. The `first seating:` line sent to the builder.

## Plan

RM1 the export (after the compiler's 0.8 cut, the registry deploy and the plugin's release). RM2 landed
(9d42ccb, with `loci fetch`); a fresh auditor's read of it is the step before anything else of it ships. The plugin stays enabled for every seat, the person's call (2026-11-05: "3"), about 2.5k
tokens a session while its 81 tools stay deferred.
