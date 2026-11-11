# Upstream ledger: the registry

`dna-seq/just-dna-registry`, tags `vX.Y.Z`: where the module is published, and whose test instance the module seat
rehearses each version on. Kept by the liaison seat (`docs/seats/LIAISON.md`); another seat that meets a symptom in
the registry sends it there rather than writing here. A defect goes into the registry's consumer inbox,
`docs/CONSUMER_SUGGESTIONS.md` in its clone, restated in its terms with an id from its ledger, appended and never
committed; then a message to `just-dna-registry/triage`.

Watched on the liaison's machine from a clone outside this repository (its line `registry` in the liaison state
file): `[seat.liaison.watch.registry]` says each new tag.

## Read mark

**None yet.** The module seat has not yet published or rehearsed on the registry. The release the module seat
first runs against becomes the mark. The latest tag when this ledger began (2026-11-05) was `v0.27.0`.
Tags since, unread (nothing here uses the registry yet): `v0.27.1`, `v0.28.0` to `v0.28.6`, `v0.29.0` (0.29.0: a namespace renames, its old name kept as an alias; 0.28.5: `GET /caches` names each lane's readers; 0.28.6: docstrings, S28); 0.28 is the registry on
the compiler's 0.8. On 2026-11-09 production still served registry 0.27.0, format 0.7.1, compiler 0.7.2, and the
test instance (the polygon) answered HTTP 502; still 502 on 2026-11-10 at about 20:24 UTC, from the module seat's `registry_health(target=test)` (mode and contract unknown), so no rehearsal yet; again 502 at the v0.28.5 tag, while production answered 0.27.0, format 0.7.1, contract compatible; already known upstream, nothing to file. **Back on 2026-11-11**: the polygon answers as registry 0.28.5, mode test, serving format 0.8.0, so against our 0.7.1 the contract does not match and every publish, validate, check and download refuses 409; reads work. A rehearsal waits on the plugin's 0.8 move; production (0.27.0, format 0.7.1) is the other half of what that move waits on. Both serving format 0.8 is what the plugin's move past `<0.8`
waits on.

## Backlog

None: nothing before the first release in use is read, since nothing here used it.

## What this repository uses

Nothing yet.

## Inbound verdicts

None yet.

## Our pieces that duplicate the registry's

None yet.

## Outbound

None yet.
