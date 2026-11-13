# Liaison — notes

The liaison seat's working state, rewritten to the present before a reset (`docs/seats/LIAISON.md`).

## Now (2026-11-05)

First seating, the seat-builder's handout:

0. Leak gate: on (the lead's notes, 2026-11-05).
1. Ledgers: begun. Plugin marked at v0.48.0 (the pin in `.claude/settings.json`), compiler at v0.7.3 (the lock's
   trio), registry unmarked (nothing here runs against it yet). All three first marks fast-forwarded.
2. Clones and watchers: no line existed in this machine's liaison state file, nor a clone; the compiler's and
   registry's liaisons run elsewhere. Cloned all three beside this clone, lines `plugin`, `compiler`,
   `registry` added; one `--tags` watcher each, and `nightly.py deps`.
3. Upward wake asked of the compiler's and registry's leads: see "Asked" below.
4. Hello to the compiler's and registry's liaisons: see "Asked" below.

Own machinery before the kit: none for this seat (no scripts, hooks or watchers of its own).

## Asked

- `just-dna-compiler/lead`, `just-dna-registry/lead` (agent-chat > seat tables, 2026-11-05): add
  `longevity-loci/liaison` to their triage seat's `wake_from`. Compiler: done, their a8262397. Registry: waiting.
- `just-dna-compiler/lead` (agent-chat > 0.8 integration, 2026-11-05): a longevity-loci block in
  `docs/INTEGRATION_0_8.md`'s per-consumer checklists. Taken, as a module-author consumer: meta.csv, the StudyRow
  columns, model_organisms, pmid NONE + doi, the new strict refusals, enrich --rederive, source_release. They asked every seat not to act on that guide
  until they post its finished commit. Posted at 5b1b73b8; read, filed as #6.
- `just-dna-compiler/liaison`, `just-dna-registry/liaison` (agent-chat > upstream, 2026-11-05): hello, what we stand
  on; told we ask them before mapping their 0.8 branches. A notice, no answer owed.
- `agents-kit/admin` (agent-chat > avatars, 2026-11-05): a picture for this seat. Done, set.
- `just-dna-registry/liaison` (agent-chat > upstream, 2026-11-05): offered its 0.8 map (M1-M11) to reuse; told we
  import nothing of the trio yet.

## Open

- Compiler 0.8 adopted 2026-11-12 (the mechanical half: floors `>=0.8.4,<0.9`, caps lifted, `uv lock`, suite). Nothing to
  recompile yet: the module is a scaffold. The module seat re-validates it under 0.8 (handoff).
- Kit at v0.1.200 for this seat on 2026-11-13 (the reload took). Watcher `upstream-index` (2b5553a, the builder's
  handoff on the person's word): the trio on PyPI, baselines 0.8.6 each; a `published` line starts the per-release
  step as a tag line does. The plugin at v0.48.9 (pin moved 2026-11-13; just-dna 0.8.5), loaded after `/reload-plugins`.
- The plugin's pin binds only once the person drops `just-dna` from their user-level settings (their answer,
  2026-11-06; still present 2026-11-09). Until then, at each plugin release: `claude plugin update
  just-module-creator@just-dna --scope project` after moving the pin.
- `docs/seats/LIAISON.md` says the plugin's repository runs no seats; since 2026-11-05 it runs four. A priming
  change (the skill `change-priming`), for the person: the filing route itself is unchanged (issues, no inbox).
- The compiler's 0.8, waited on (the person, 2026-11-05): read at the cut, `waits until` the tag; the branch's
  changelog commits come in by `watch.compiler-next`.
- The plugin's `QUOTING.md`: read, filed as #7 (done). The plugin is not yet seen loaded in a session.
