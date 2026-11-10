# Agent Guidelines — longevity-loci

The re-curation of the longevity annotation module from its evidence: a curated row per locus, each claim citing a note on an article; not the module's tooling, the compiler or the registry.

`AGENTS.md` is a symlink to this file. If the two ever differ, that is a bug —
`ln -sf CLAUDE.md AGENTS.md`.

---

## Read these first, in this order

Obligatory. Read them yourself. **Do not delegate a document you are about to judge a design
against**: a subagent returns a summary, and a summary of a rule drops the qualifier the decision
turned on. Delegation is for finding things, never for deciding them.

1. **docs/ROADMAP.md** — open work only, in order.
2. **docs/CHANGELOG.md** — what actually landed, newest first.
3. **docs/DECISIONS.md** — the calls settled with the maintainer, each with the alternative it
   rejected.

A charter, when the repository keeps one (a format or a schema, whose invariants outrank any plan),
goes first in this list and wins any conflict with a plan. A per-area reference goes last, read
when the task touches its area.

Everything below is self-contained: no rule here requires following a link to know what you must
not do. Links carry positive detail only.

**The `.claude/` layer is part of this repository's contract.** Its skills, agents, commands and
hooks are named here, each with a line saying what it is for, or they are found by accident. Where
a skill is the canonical copy of a procedure, this file says so in one line and does not restate it.
None existed when this file was written.

Sessions that take a standing role (a seat) all load this file; each seat's own priming lives under
`docs/seats/`, and the seats kit runs them.

---

## 1. When rules conflict: ask, never infer

When two rules conflict (this file against a sibling repository's, against the person's global
preferences, a rule against what the code does), stop and ask. Do not pick the one that looks
better, do not synthesise a compromise, do not silently follow the more specific file. A conflict
between two live rules is almost always a real difference in what the repositories are, and
inferring which applies here is the guess that produces a rule nobody agreed to.

1. **Survey first, ask second.** Read both rules whole and find out why each side holds its
   version. A question that does not carry the reason cannot be answered.
2. **One question per conflict, batched**, never dripped. Each gets two to four concrete options.
3. **Each option states its cost**: what breaks, what it forces elsewhere, which rule it
   contradicts.
4. **Recommend one, and say so.**
5. **Record the answer where it will be read again**: the rule into its section below, the reason
   into §8 in the maintainer's own words, the call into `docs/DECISIONS.md` with the alternative it
   rejected. An answer not written down gets asked again.

A conflict with the charter is not a question: the charter wins.

**Adopting this file is such a moment.** It was laid by the seats kit's `bin/init.py`, and the
sections marked "Not yet written" have more than one right answer. The questions to ask before the
first change: the build, run and test commands; the layout beyond `docs/`; the dependency tier the
code may carry; whether consumers report to this repository (then it keeps a consumer inbox,
which the kit's triage role runs) and which repositories it consumes; whether a `git pull` into it
can break a user's install (then a STOP banner goes at the very top of this file, with the
sentence to hand the person); the sibling repositories, read-only unless the task targets them.

---

## 2. Non-negotiables

Read the whole list before the first edit. The reason follows each rule, because a rule without its
reason gets argued away at 2 a.m.

- **Never claim a test would have caught a bug without running it against the buggy code** and
  watching it fail. A new test is checked by breaking the code it guards.
- **Never silently fall back when the primary input is missing.** Refuse, or say loudly what was
  substituted: the person cannot see that the source differs.
- **Never fill a value from the same source that checks it.** The check then compares a source with
  itself and agrees perfectly, and the value moves from honestly unverified to apparently verified.
  A lookup reports, the person decides, the check checks; a refusal a tool prints is kept verbatim.
- **Never collapse unknown into yes or no.** A check that could not run is not a check that passed;
  a timeout is not a negative answer. Unknown is said as unknown.
- **Never read a reproducible result as a correct one.** A digest match, a strict mode, a
  reproducible build say the bytes came out the same, not that they mean what was intended.
- **Never commit a placeholder path or a made-up example value.** It proves nothing and outlives
  the session that invented it.
- **Never commit large data.** Anything over about 5 MB that must travel goes through Git LFS; a
  large blob in history is very hard to remove afterwards.
- **Never track `.leak_words` or `.leak_allow`.** They name everything the leak gate protects
  (copy `.leak_words.template` to `.leak_words` and fill it; the kit's `bin/leak-gate.sh install`
  turns the gate on). Never commit with `--no-verify`.
- **Git: commit as you go**, one coherent block per commit: a behaviour with its test, doc and
  changelog line. No conventional-commit prefixes. Stage explicit paths, never `git add -A` or
  `git add .`: they sweep in secrets, editor swap files and junk. Local branches are free to create
  and switch. No push, tags, releases, branch deletion or history rewriting: those are the
  maintainer's, unless a seat's priming grants one in writing, by name. Never `git stash drop` or
  `git stash clear`, even on request.

---

## 3. Layout

```
rows/        a curated row per locus, <locus_id>-<locus_name>.yaml (the name made file-safe, docs/FORMATS.md);
             rows/PROGRESS.md the curator's order
corpus/      an evidence note per article, <key>.md (pmid-<PMID>, or doi-<DOI> for a preprint)
scout/       SEARCHES.md (the searches, by track) and queue.md (new papers waiting for a row)
module/      the module's spec directory (module_spec.yaml and its tables), the module seat's
runs/        the runner seat's LOG.md (one entry per batch job) and STATUS.md (what runs now, what is queued)
src/longevity_loci/   the formats' models and the checks (`loci`)
tests/       pytest, on the fixtures in assets/
assets/      fixtures that travel: one example row and one note
docs/        all markdown except this file and README.md; docs/FORMATS.md the row and note formats;
             docs/longevitymap_v2/ the research design, moved in from just-dna-lite unchanged
docs/seats/  the seats' primings and notes
```

**The article cache is outside git**, at `$LOCI_CACHE/<key>.txt`, the variable set on the machine and never
written as a path here. **Never commit an article's full text or PDF**, nor paste one into a message or an
issue: the repository is public and the articles are not ours. Notes keep citations, verbatim quotes and
verdicts only.

---

## 4. Build, run, test

- `uv sync`: the environment (Python 3.13+, uv; never `uv pip install`). It carries `just-dna-enricher` (and through
  it `just-dna-compiler` and `just-dna-format`), the module toolchain's enrichment of rsIDs and coordinates.
- The module-creator plugin (`dna-seq/just-module-creator`, its marketplace `just-dna`) is enabled for every clone
  by `.claude/settings.json`, pinned at a tag: its skills (`find-evidence`, the module authoring guides) and its MCP
  server's literature and schema tools. The liaison moves the pin.
- `uv run pytest`: the tests; the quote tests fetch one real abstract from Europe PMC and skip offline.
- `uv run loci check rows`: every row parses, is named for its locus, cites only quotes the corpus holds.
- `uv run loci fetch PMID…`: an article's text into `$LOCI_CACHE` (Europe PMC's open full text, else the abstract).
- `uv run loci fetch-supp KEY LOCATOR`: an article's supplement, data deposit (`zenodo:ID`, `figshare:ID`) or code file
  into `$LOCI_CACHE` as text, beside the article's, where a quote read at depth `supplement` is checked.
- `uv run loci check quotes`: every note's quote is found verbatim in `$LOCI_CACHE`. Exit 0 passed, 1 a failure,
  2 no cache set, 4 some quotes could not be checked (unknown, not passed).

Batch work on the cluster (bulk fetches, indexes, the compile at scale) is submitted with this repository's job
prefix, which the machine's settings name, never this file.

**Run the commands yourself** rather than telling the person to run them, except where a command
needs an interactive terminal: then hand over the exact line.

---

## 5. Code and tests

- **A result that can be unknown says so.** Yes, no and unknown are three answers; when "no" has
  kinds (a refusal, a timeout, a crash, a malformed input), the answer carries which.
- **Ordering is load-bearing** wherever bytes are hashed, compared or shipped: never emit in the
  order of a set or a map without a stable sort.
- **Aggregate a warning raised in a loop**: by reason, once, with a count.
- **Timestamps are stored as ISO-8601 UTC** and shown in local time.
- **A deprecation warning in code you touched is a blocker**: the API moved; fix it, and the rule
  here, so the pattern does not return.
- **Internals are free to change; the contract is not.** The public API, the shape of what is
  written or sent and the command line change only on purpose, and with a version.
- **Tests run the real code path on real data** and compute the expected values from the fixture
  at run time. Never mock the transformation under test. Assert relationships (set equality, sums,
  round trips) over existence or counts, and cover the edges: empty, null, a boundary, malformed
  input.

---

## 6. Docs and their lifecycle

- **All markdown goes in `docs/`**, except this file and `README.md`. Every file under `docs/` is
  named in UPPER_SNAKE; directories stay lowercase.
- **`docs/` is the ground truth.** This file repeats from it only what orients a reader, and every
  prohibition lives here in full: a "don't" behind a link does not get read.
- **`docs/ROADMAP.md` holds open work only.** Done items leave it; the changelog says what landed.
- **`docs/CHANGELOG.md`** records what landed, newest first, in the same commit as the change,
  including a change made here to follow a repository this one consumes.
- **Update the affected docs in the same commit as the change**, never after.
- **Something that belongs to a repository this one consumes but does not own** is reported to
  that repository's inbox (its issues, or its consumer inbox), restated in its terms, never filed
  into its roadmap, and its repository is never edited or committed to. Our side of it goes into our
  changelog.
- **Before a pull request**, show `git diff <upstream>/main --stat HEAD` and
  `git log <upstream>/main..HEAD --oneline` and wait for approval. Files of one installation (local
  settings, local configs) stay out.
- **Prose is plain and honest.** Never describe a capability the repository does not have.

---

## 7. Self-correction

When outdated knowledge of an API causes a real failure, fix the code and the rule here (and the
affected `docs/`), so the next session does not repeat it. When the maintainer corrects a
preference, it goes into §8 in their words, with the reason.

## 8. Learned

Append-only, one line each: the maintainer's preferences in their own words, and the facts of this
machine and this project that reading the code does not reveal.

- `docs/longevitymap_v2/` keeps just-dna-lite's lowercase file names: moved in unchanged, so its links hold; it is
  exempt from the UPPER_SNAKE rule.
