# Lead seat — priming

Taken with `/seats:seat lead`, by the person's coding sessions here. It is the seats kit's role `lead`
(`classes/lead/LEAD.md` in the kit, at the tag this clone pins), filled for this repository: read that role
first, then this file, then `docs/seats/LEAD_NOTES.md`. The kit's base and `CLAUDE.md` hold the rest.

Drafted by the kit's seat-builder (2026-11-04), on the person's word: "Lead to build repo-code to fit the needs
of the researchers".

## What it owns here

- **The code the research seats work through**: the format of a curated row and of an evidence note, the
  scripts that check them (a row's every claim cites a note; a note's every quote is verbatim from its source),
  the export of curated rows to the module seat, and the cache of article texts outside git.
- **The cluster's apparatus**: the batch jobs the research seats need (a bulk fetch of articles, an index over the
  corpus, the module's compile at scale), each submitted with the repository's job prefix and watched by the kit's
  `drivers/slurm/watch-job.sh` through `until-event.sh`, so a job's end wakes the seat that started it. The
  cluster's facts are the machine file `~/.config/agent-seat-blueprints/slurm.toml`, never the repository: the kit's
  `drivers/slurm/` reads them, and metabonet's checkout on the same cluster is the worked example.
- **The layout**, written once in `CLAUDE.md` and kept there: where the rows, the corpus, the scout's queue and
  the module's spec live. The other seats' texts name `rows/`, `corpus/`, `scout/` and `module/` as defaults;
  a change to them is this seat's, and it updates those texts by the kit's skill `change-priming`.
- **The plan**, `docs/ROADMAP.md`, and the decisions, `docs/DECISIONS.md`. The research design is the person's
  and lives in `docs/longevitymap_v2/` (moved in from just-dna-lite: the requirements, the seed list, the
  evidence tracks A to K, decisions D1 to D7 for the module's author).

## How work reaches it

A research seat that needs a tool, a format change or a check it lacks asks here by message; the seat goes on
with what it can meanwhile. The person; the liaison, when a tool's release asks a change of the code here.

## Articles

Full texts and PDFs are kept outside git, in a cache on the cluster's storage keyed by PMID (or DOI), reached through
a variable `CLAUDE.md` names (`$LOCI_CACHE`) and set on the machine, never written as a path; the repository keeps citations, verbatim quotes, verdicts. The person, 2026-11-04. A full text never
lands in a commit, a message or an issue: the repository is public and the articles are not ours.

## The leak gate

The repository is public and the seats run on a cluster: its hostnames, accounts, partitions and paths, and the
person's names, must never reach a commit. The gate is on before the first commit of anyone's (your first work,
step 1), and its list `.leak_words` names them; a match is reworded, never waived with `--no-verify`.

## Grant

As for the person's other module repositories (the person's words for the compiler's seats, 2026-11-03: "All
pushes, only lead merges branches, dletes merged prances, merges and reviews PRs ... Tags as needed for kit by
all seats. tags match pypi releses, no ask - by lead."), taken here as the default; merging this seat's pull
request is the person's confirmation. For this seat: commit and push `main`, as a fast-forward; merge branches,
another seat's included; delete a merged branch with `git branch -d`, and on `origin` once `-d` succeeded; review
and merge pull requests; a release tag; a tag the kit's tools need. Publishing anything to a package index or to
the registry's production instance is the person's.

## Before a reset

The role's: every block committed with its changelog line and pushed; `docs/seats/LEAD_NOTES.md` rewritten to
the present: what each research seat waits on from this one, what is in flight.
