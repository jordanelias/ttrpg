# The season loop — how it runs, what it rolls, and where it stands

## Status: PROPOSED (2026-09-30) · design-only · ratifies nothing on merge · reference under `CLAUDE.md` §0.05
## Lane: IN · IDs: none allocated
## Read and run at HEAD `c8cc408` (after #444). Instruments: `python -m engine.season.harness.register --requirements`, `python -m engine.season.harness.aperture`.
## Suite: [README](README.md) · **01 the season loop** · [02 against precedent](02_against_precedent.md) · [03 play surface](03_play_surface.md)

**What this answers.** How `engine/season/` — the game code, Layer 2 — turns one season, in plain terms;
why a seeded season replays exactly even though fights and contests roll dice; and what the loop does
and does not do as of #444.

---

## 1. Analysis

### 1.1 One season, in order

`SeasonDriver.season()` (`loop/driver.py`) runs seven steps across four barriers:

1. **CALENDAR** — dates that have come due fire; a held seat gets a docket item. Decides nothing.
2. **MATTER** — the world moves by itself, once a season: wear and decay, sites **yield** stores
   (harbours grain and salt, seams ore and timber — `matter.py`), cohorts **eat** them, a drained larder
   emits a shortfall others can witness, and memory fades. The world then **freezes**.
3. **Rounds** — `scene_budget` of them (5 by default; `scenes_per_round` 1). Each round:
   - **DELIBERATE** — for each person in turn, a view of their *own* claims and the questions they face
     become a set of candidate acts. `choose` is asked when the person has budget left and something
     they can see has changed, or their queue is empty; otherwise the next scene they already chose is
     released. This step holds **no write token** and cannot change the world.
   - **RESOLVE** — the only step that writes acts. Acts are sorted into a canonical order (stratum, then
     a content hash), checked against the world their predecessors left, and folded through each verb's
     effect. Failure *emits* an event rather than raising: the second person at an emptied granary gets a
     different event.
   - **ENCOUNTER** — fights the contests RESOLVE declared and deferred (a march's field battle).
   - **WITNESS** — every event reaches those present to observe it or those later told, and each
     deposits a claim in **their own** ledger. Nobody knows anything they did not witness or hear.
4. **CENSUS** — reserved for demand-driven individuation; writes nothing today.

Then `w.tick += 1`. The return value is `{acts, events, rounds, deposits, hash}` — counts and a content
hash — while every event is appended to `w.log` as it happens.

Four barriers each mint one write token, and `write_matrix.yaml` says which step may write which field of
which record. DELIBERATE, being a pure map over a frozen world, gets none.

### 1.2 Why a seeded season replays exactly

Every id is a hash of `(world seed, tick, subject, purpose)` (`state/ids.py::H`, blake2b). Every random
draw comes from a generator seeded the same way: `draw_factory` returns
`random.Random(int(H(seed, tick, subject, purpose), 16))`, with `purpose` unique per draw
(`roll:<prize>:<act id>`). A σ-leverage contest receives that generator from the driver and threads it
down to `dice_engine.roll_pool`'s `rng.randint(1, 10)`; the personal-combat provider seeds its own from
the same world seed with a different purpose string, by design, so existing fight results did not have to
be re-recorded. Either way, the dice are probabilistic *in the fiction* and a hash lookup *in the code*:
the same seed gives the same season, byte for byte (`tools/m1_acceptance.py` row 2). A deferred contest
does not roll twice: `_contest` returns before building its generator when the prize's step is not the
step now running.

One honest qualifier: σ-leverage contests currently roll with **zero leverage**. `sigma.py` sets
`lev = 0.0` *"until something supplies leverage"*, and `_pool_of` falls to `pool_default` for everyone
whose capability is unset ([09](09_the_character_sheet.md) §1.2) — so a social contest today varies by
seed and fixture, not by person.

### 1.3 What #444 added, and what it did not

| area | now | still not |
|---|---|---|
| verbs with effects | 26 of 44 (13 new: restore, found, build, oblige, levy, issue, open_case, determine, petition, survey, give, commit, migrate) | carry, exchange, forge, repudiate, succeed, tie/knot have writes and no effect; none is ever formed |
| economy | MATTER yields stores; cohorts eat; shortfalls are witnessed | no coin anywhere; no verb produces goods; `exchange` has no effect; the shipped realm runs ~35× surplus |
| founding | `found` writes a Rung, `build` a Site | only hand-built acts reach them: they need a `works` Record, and no computed act mints one (aperture: found 14 attempted / 0 executed; build 15 / 0) |
| factions | `faction_q` answers membership, holdings, purview, superiors, subordinates, war — as queries, storing nothing | `head` is empty and `at_war` false in every buildable world; only `resolve` has a non-test caller |
| population | 37 weight-2 cohorts, one per settlement | they eat, count and migrate; `capability` and `pursuits` have no season writer, `scar`'s writer is inert at its default step (`scar_step = 0`), and `stance` is written only by `march` |

### 1.4 Against the nine requirements

`register --requirements`: **met 1 · partial 5 · not met 3.** Met: R-03 (a season ticks scene by scene).
Partial: R-04 (decisions at differing scales — flipped at plan position `20-ii` on 2026-09-30; the corpus
now runs at duchy, person, realm and settlement, but nothing acts *as* a faction), R-06, R-07, R-08, R-09.
Not met: R-01 (decisions propagate), R-02 (decisions affect later decisions), R-05 (every verb built).

`aperture` on the populated realm (seed 0): 34 verbs resolvable; 83 persons, 24 seated; executed zero
times in a season — build, found, commit, confer, determine, establish, issue, levy, migrate, revoke,
work; `give` and `oblige` are never formed.

---

## 2. Recommendations

| # | recommendation | where | observable (falsifier) | cost | gate |
|---|---|---|---|---|---|
| **L-1** | A supported read of what a season did, per person and in order — the events already in `w.log` and the claims each person deposited — so an interface need not reach into driver internals. See [03](03_play_surface.md) S-2. | `queries/` | the read's output for a seeded season equals `w.log` filtered by witness; `content_hash` unchanged | small | IN |
| **L-2** | Correct `deliberate.py`'s *"WorkerThreadPool over persons"* comment: the map is sequential and `_in_parallel_map` is a write guard. It matters because a blocking human `choose` depends on it ([03](03_play_surface.md) S-1). | `loop/deliberate.py:114` | — | trivial | buildable now |
| **L-3** | Name the zero-leverage state where a designer will see it: a σ-leverage contest's advantage has no producer. When one is chosen (position, office, a claim held), it enters as the μ-shift the resolution kernel already owns — never as an obstacle change. | `seam/wrappers/sigma.py` | a contest between a person with and without the chosen source differs in net over N seeds | small once chosen | IN, with SC |
| **L-4** | Make the founding chain reachable by computed play, or say plainly that the settlement builder runs only from authored acts: no computed `create_record` mints a `works` Record. | the plan's Phase 2, already in progress | aperture: `found` and `build` executed > 0 on the populated realm | — | the plan |

L-4 is observation, not a new work item: the plan's Phase 2 owns the founding chain and is in progress.
