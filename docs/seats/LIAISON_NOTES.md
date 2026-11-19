# Liaison — notes

The liaison seat's working state, rewritten to the present before a reset (`docs/seats/LIAISON.md`). Written whole on
2026-11-16 for the chat organisation move (the person: "Make sure they commit all to notes, transcripts are not
moving"), so a fresh session can carry on from this file and the three ledgers alone.

## Now (2026-11-16)

Nothing in hand. Every upstream release up to today is read and, where it moves our use, taken:

- **Plugin** `dna-seq/just-module-creator`: pinned and installed at **v0.48.15** (2026-11-19) (`.claude/settings.json`),
  ledger `docs/UPSTREAM_PLUGIN.md`, read mark v0.48.15.
- **Compiler trio**: `uv.lock` holds enricher **0.8.8**, compiler and format **0.8.6**; floors `>=0.8.8` / `>=0.8.6`,
  caps `<0.9`; polars and duckdb capped `<2`. Ledger `docs/UPSTREAM_COMPILER.md`, read mark v0.8.9. Suite 146 passed
  at the last move (a7bfed4).
- **Registry** `dna-seq/just-dna-registry`: read mark **v0.34.0** (2026-11-18), ledger `docs/UPSTREAM_REGISTRY.md`.
  Nothing here imports it; the plugin's server does. On 2026-11-16 the polygon served 0.30.0 (format 0.8.4) and
  production 0.31.0 (format 0.8.6), both compatible with our 0.8.6 client.
- **Kit**: this clone's pin (`.claude/settings.local.json`, untracked) moved to **v0.1.252** on 2026-11-19 (v0.1.251, v0.1.250, v0.1.249 and v0.1.248 earlier that day, v0.1.247 on 2026-11-18, v0.1.244, v0.1.243, v0.1.242, v0.1.240, v0.1.236, v0.1.235 and v0.1.234 earlier that day; v0.1.232 and v0.1.231 on 2026-11-17, v0.1.227 on 2026-11-16) by
  `move-to-tag.py --take`, on the lead's ask for the org move (rule 24 needs v0.1.226 or later; the machine's
  marketplace record already named v0.1.227, so v0.1.226 would have taken it back). The other seats of this clone
  move their own seats. Since the move, this seat keeps the clone's kit pin at the newest release (the lead asked it
  through the move; no tooling seat here), by `move-to-tag.py --take`, then posts in `#longevity-loci>move`.

## Routines (how this seat does its work)

Kit copy: `K=~/.claude/plugins/cache/agent-seat-blueprints/seats/<pinned version>`;
`W="sh $K/bin/py.sh $K/classes/base/watchdog.py"`.

- **A plugin tag** (watcher `plugin`): read `git diff vA..vB -- docs/CHANGELOG.md` in the clone
  the plugin's clone (its line `plugin` in the liaison state file); move the ref in `.claude/settings.json`; `timeout 300 claude plugin
  update just-module-creator@just-dna --scope project`; in `~/.claude/plugins/cache/just-dna/just-module-creator/<ver>`
  run `UV_LINK_MODE=copy uv sync --no-dev --reinstall -q` (the MCP start race leaves a broken `.venv` otherwise) and
  check the import with `uv run --no-dev python -c "import just_module_creator.server"`. If the plugin's `uv.lock`
  moved the trio, polars or duckdb: raise our floors to match, `uv lock`, `uv sync`, `nice -n 15 uv run pytest -q`.
  Then the ledger's inbound verdict (what is a lever for which seat, what breaks), the changelog line, commit, push,
  tell the module seat (and curator/lead where it names them) in `#longevity-loci>module`, `$W reload`.
- **A compiler or registry tag** (watchers `compiler`, `registry`; `upstream-index` says PyPI final releases of the
  trio): read the changelog diff in the compiler's or registry's clone (lines `compiler`, `registry`)
  (`git fetch --tags` first), write the inbound verdict and move the read mark. **Our lock follows the plugin's lock,
  never an upstream tag alone** (the plugin's server shares this machine's enricher cache, and a polars or duckdb
  difference changes artifact bytes).
- **Instances**: the plugin's `registry_health(target=test|prod)` says which registry version and format each serves.
- **Weekly deps bump**: watcher `nightly` (`nightly.py deps`), while the person is away.
- **Daily line**: `$W send liaison '#longevity-loci>daily' "..."`, at most 150 characters, only on a day with landed
  work (last: 2026-11-16).
- **Commits**: `git commit -q -m "...\n\nSeat: liaison\n\nCo-Authored-By: ..." --only -- <paths>` (`-m` before
  `--only --`), then `git pull -q --ff-only; git push -q origin main`. Ledger edits by a short script asserting each
  replaced string occurs once.
- **Filing upstream**: plugin defects go to its GitHub issues (`report-to-kit --to dna-seq/just-module-creator`);
  compiler and registry filings go whole to their triage seat (`just-dna-compiler/triage`,
  `just-dna-registry/triage`) by `bin/hand.sh`, after asking for the next id: their triages run on another machine,
  so an append to our clone of theirs never reaches them. Never edit or commit an upstream's repository.

## Waits on whom

- **The compiler's RM435** (`effect_direction` on the study row, our S148), on their 0.9 roadmap. When it ships: tell
  the lead the export can stop writing direction into `conclusion`.
- **Registry S145** (remote snapshots; its ask 4, a local Ensembl rsID index, is decided local-only in the compiler's
  0.9 RM431). Not in 0.32.0.
- **Compiler RM441** (with RM399; the registry's S156, which enricher release last changed a derivation): placed in
  compiler 0.10. Nothing for us to do; read at its tag.
- **The polygon and production serving registry 0.32**: then `registry_claims` folds spellings (S32) and the plugin's
  caveat on an empty claims answer lifts. Tell the lead and curator when seen.
- **The person: drop `just-dna` from their user-level `extraKnownMarketplaces`** (their answer, 2026-11-06; still
  present). Until then the project pin does not bind, and each plugin release needs the manual `claude plugin update`
  above. Theirs to do; never edit their settings on a peer's ask.
- **Production and the namespace word**: anything to production, and the namespace (`test-longevity-loci` on the
  polygon), wait on the person, through the lead and the module seat. Not this seat's.
- **#6** (open, ours): compiler 0.8 against our formats; the export's part stays with the lead.

## Learned

- **Curated status (registry S33, 0.32.0)**: only a `verified` highlighted review from someone with no role on the
  namespace counts, so no seat of ours can make our module curated. Told the lead and module seat (640785121).
- **APOE as diplotypes draws no warning by design** (compiler RM28): a study on a variant defined in haplotypes.csv
  is not `study_variant_orphan`. Our copied shape audit in `docs/format08_reference/` is stale on this; the lead
  updated FORMATS.md.
- **Other seats read stale clones of ours.** The compiler's liaison read our pyproject from a clone six days behind
  and reported caps below 0.8 (2026-11-16); answered with the current state, they confirmed. Answer such a report
  from `origin/main`, not from memory.
- **`watchdog.py daily liaison TEXT` only prints the last line**; post the daily with `send`.
- **`git pull --ff-only` once printed "no such ref was fetched"**: harmless; confirm with `git fetch` and `git status -sb`.
- **The kit's `move-to-tag.py` refuses a tag below the machine's marketplace record** (#517) and says the tag to take.
- Our own code's wishes (`loci check quotes`, `loci fetch-supp`) are the lead's, not an upstream's: this repository has
  no tooling seat, and the lead owns `src/longevity_loci`.

## Contacts

- Upstream seats: `just-module-creator/lead` and `/liaison`; `just-dna-compiler/lead`, `/triage`, `/pm`, `/liaison`;
  `just-dna-registry/lead`, `/triage`, `/liaison`. They talk in `#agent-chat > upstream`.
- Our seats: lead, module, curator, scout, runner, in `#longevity-loci`. The module seat is told of every plugin move.
- `just-dna-compiler/lead` added us to its triage's `wake_from` (their a8262397). The registry's: asked
  2026-11-05, unconfirmed.
- The compiler's `docs/INTEGRATION_0_8.md` has a longevity-loci block (module-author consumer); read at 5b1b73b8,
  filed as #6.

## Open

- **Try the compiler's unreleased 0.9 before its release** (their ask, relayed by the secretary 2026-11-19,
  641757343): the trio from git, `dna-seq/just-dna-compiler` branch `0.9` at `d9c578ae`, subdirectories `schema/`,
  `compiler/`, `enricher/` (versions still read 0.8.10, inside our `<0.9` cap). In a scratch environment, never our
  lock: run our suite and an enrich and compile of `module/` (offline and online), and report breaks in
  `#agent-chat` mentioning `desk-antonkulaga/secretary`. State: unattended, waits until the quota hold lifts (7-day
  at 98% on 2026-11-19).
- The priming's grant still names "appending to an upstream's consumer inbox, uncommitted", a route the compiler's
  and registry's triages replaced with `bin/hand.sh` (2026-11-12); the priming's upstream list says the new route
  (62c5ae4). The grant line is the person's text and is left as it is; it permits nothing the route now needs.
