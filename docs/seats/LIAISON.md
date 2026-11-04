# Liaison seat — priming

Taken with `/seats:seat liaison`. It is the seats kit's role `liaison` (`classes/liaison/LIAISON.md` in the kit, at
the tag this clone pins); read that first. This file adds the repository's facts. Its working state is
`docs/seats/LIAISON_NOTES.md`; it keeps one ledger per upstream, `docs/UPSTREAM_<NAME>.md`.

Seated on the person's word of 2026-11-04: "liaison seat to track bugs in our tooling for modules".

## Its upstreams

All three are the person's own, so a defect is filed, not drafted for the person:

1. **The module-creator plugin** (`dna-seq/just-module-creator`): the tools the module and curator seats work
   through. No consumer inbox: a defect is an issue there, through the kit's `report-to-kit --to
   dna-seq/just-module-creator` (this repository's `[repo] producers`). Its repository runs no seats.
2. **The compiler's packages** (`dna-seq/just-dna-compiler`: format, compiler, enricher): a defect goes into its
   consumer inbox, `docs/CONSUMER_SUGGESTIONS.md` in its clone, restated in its terms with an id from its ledger,
   appended and never committed; then a message to `just-dna-compiler/triage` naming the id. Its seats are seated.
3. **The registry** (`dna-seq/just-dna-registry`): the same way, its inbox and `just-dna-registry/triage`.

Ask the upstream's liaison in `agent-chat` before filing a defect in a library under both of you, as the role's
outbound step 2 says. The compiler's and the registry's next minors are built on branches of their own; their
liaisons already map them: ask them before mapping one yourself.

## Wired to the upstreams' seats

The kit's onboarding rule (the person, 2026-11-04): this seat may wake the compiler's and the registry's triage, and
their leads may wake it and this repository's lead. The upward half is a line in their seat tables, asked of their
leads in your first work.

## The dependency bump

This repository's Python lock, once the lead makes one: the kit's weekly job `deps`, as the role says.

## Grant

As in `docs/seats/LEAD.md`: commit and push `main`, as a fast-forward: its ledgers and its notes, a dependency cap
with its `uv lock`, and the dependency bump's mechanical fix. A tag the kit's tools need. Appending to an
upstream's consumer inbox, uncommitted; an issue on the plugin's repository. Nothing else.

## Before a reset

Each ledger's read mark current and committed; `LIAISON_NOTES.md` says what is half read and what each upstream
seat was last asked.
