# The play surface — what an interface can bind to, and what it cannot yet

## Status: PROPOSED (2026-09-30) · design-only · ratifies nothing on merge · reference under `CLAUDE.md` §0.05
## Lane: IN, with PC, SC, FI · IDs: none allocated
## Read at HEAD `c8cc408`; realm figures from `python -m engine.season.harness.aperture` (seed 0).
## Suite: [README](README.md) · [01 the season loop](01_the_season_loop.md) · [02 against precedent](02_against_precedent.md) · **03 play surface** · [05 two modes](05_two_modes_of_one_bout.md) · [07 saying a weapon is good](07_saying_a_weapon_is_good.md)

**What this answers.** How much of the season loop and its subsystems is exposed in a form an interface
could bind to and actually play; which subsystem is closest; and the one constraint any interface must
keep.

---

## 1. Analysis

### 1.1 What exists

- **The choice seam.** `SeasonDriver.season(choose, …)` calls `choose(p, v, s, ask_budget)` for one
  person at a time, in a plain sequential loop, whenever that person has budget left and their inputs have
  changed or their queue is empty. A `choose` that hands one person's decision to an interface and
  everyone else's to `make_chooser` needs no engine change. DELIBERATE holds no write token, so a human
  choice reaches the world only as an act RESOLVE admits.
- **The menu.** `decision.options.opening_set(p, v, q, fx) → list[Candidate]` computes what this person
  can attempt now from `verb_table.yaml`; a `Candidate` carries `verb`, `subject`, `why` and `operands`.
- **The read side.** `queries/person_q.LedgerReader` answers from one person's own claims; `world_q`
  (presence, reach, members, holders, the questions a person faces) and `faction_q` answer world
  queries.
- **A world to point at.** `harness/populated.py::build_realm` builds the peninsula: at seed 0, 83
  persons, 24 of them seated, drawing on `npcs.yaml`, `offices.yaml`, `venues.yaml` and, since #444,
  `cohorts.yaml`.
- **A bout already recorded.** The combat seam captures the full trace of every fight and keeps one
  number from it ([05](05_two_modes_of_one_bout.md) §1.2).

### 1.2 What does not

- **No wire format.** Nothing in `engine/season/` outside the harness serialises a `World`, `Person` or
  `Event`; `World.content_hash()` is a digest, not a representation.
- **No supported record of a season.** `season()` returns counts and a hash; the events themselves sit
  in `w.log`, a driver internal.
- **No omniscient event log, by design.** An `Event` carries no actor, no target and no subject;
  attribution exists only as each witness's claim. An interface cannot show "who did what to whom" as
  fact — only what the player's character believes happened. The repository's own survey records that
  no game has a general channel for expressing interior state (`research/…_part2.md` §3.2, D6); this is a
  design problem to budget for, not a missing field.
- **No client.** `godot/skeleton/` covers one module, does not compile and extends a spine defined
  nowhere (`CLAUDE.md` §6); the Godot version itself awaits a ruling.

### 1.3 The one constraint

The design's epistemic contract: the engine owes a player *"the arithmetic of what your character
already holds, and nothing about the world they do not"* (quoted in
`references/what_valoria_is_and_what_runs.md` §1.1 from the code architecture, §C.11). A convenient
interface — a `World` dump rendered on screen — would break it on the first frame. Whatever an interface
reads must be a projection of one person's own holdings.

### 1.4 How ready each subsystem is

Ranked by how much of what a player would need to see already exists behind the verb:

| subsystem | what runs | what an interface would get | missing |
|---|---|---|---|
| **personal combat** | `fight` reaches `combat_engine_v1` through the seam; a real duel, deterministic from the world seed | a result, a wound state, and — if returned — a full trace | the seam runs the sim harness to a decision in one act; the trace is dropped; only `end` crosses from the person ([05](05_two_modes_of_one_bout.md), [09](09_the_character_sheet.md)) |
| **social contest** | `tell` contests *a standing* through the σ-leverage provider; the proceedings grammar (`arrangements.yaml`: thirteen keys, three seeded arrangements, all `disposal: bench`) and `world_q.judging_set` stage a hearing | a proceeding convened, a panel, one roll's margin | leverage is zero and most pools are the default ([01](01_the_season_loop.md) §1.2); no manoeuvre set exists; `systems/social_contest/sim/contest/` (fifteen modules) retires at `2-ii`, and the proceedings subsystem is partly built under plan position `22` (steps 6, 7, 9 and 10 done; the contest-resolution core, steps 11–16, open), while its proposal stays held back |
| **fieldwork** | five of the six investigation acts execute; each writes nothing and deposits a `finding.made` claim | "you examined the site; you now know X" | no graded outcome — `finding.none` means a failed precondition, never a failed attempt; `thread_read` cannot be attempted (untyped precondition); `knots.py`'s bond-strain model has no caller in the season loop; `interview` is a baseline awaiting the Dialogue Lattice (ED-FI-0004) |

Realm season, seed 0, findings made / none: examine 4 / 7, interview 5 / 13, research 3 / 30, surveil
9 / 11, reconstruct 20 / 6.

---

## 2. Recommendations

| # | recommendation | where | observable (falsifier) | cost | gate |
|---|---|---|---|---|---|
| **S-1** | A dispatching `choose`: one named person to an interface callback, everyone else to `make_chooser`. This is the whole single-player hook. | a harness or client module; no engine change | with the callback replaying `make_chooser`'s own pick, `content_hash` is equal (the control) | trivial | buildable now |
| **S-2** | A per-person projection as the boundary any client reads: that person's view, candidates, own claims, and the events they witnessed this season — never a `World`. | `queries/` | the projection for person *p* contains no claim *p* does not hold; a test plants a claim in another ledger and asserts it is absent | small | IN |
| **S-3** | Render the season as the character's journal of belief — subject, predicate, value, source, teller, confidence — not as a feed of fact. | client, over S-2 | a claim the character holds falsely appears as held, not corrected | design | IN, with the client |
| **S-4** | Return the combat trace the seam already captures ([05](05_two_modes_of_one_bout.md) M-1). | `seam/wrappers/combat.py` | `content_hash` unchanged | trivial | buildable now |
| **S-5** | A weapon card from contribution terms only ([07](07_saying_a_weapon_is_good.md) C-1). | `combat_engine_v1` | — | small | buildable now |
| **S-6** | Before any fieldwork interface: give the investigation acts a graded outcome (the fieldwork design grades them on four bands, and nothing resolves a band), and type `thread_read`'s precondition so it can be attempted. | `verb_table.yaml`, a resolver for the six | a failed attempt emits something other than a failed precondition; `thread_read` executes on the realm | medium | FI |
| **S-7** | Keep the client choice decoupled: build S-2 as the only thing a client reads, so the unresolved Godot version does not block interface work. | — | — | — | standing rule |

No new Jordan item. The Godot version is already his to rule.
