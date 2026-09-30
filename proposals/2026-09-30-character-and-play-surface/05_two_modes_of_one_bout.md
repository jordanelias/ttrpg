# Two modes of one bout — the grid and the duel

## Status: PROPOSED (2026-09-30) · design-only · ratifies nothing on merge · reference under `CLAUDE.md` §0.05
## Lane: PC, with IN at the seam · IDs: none allocated
## Measured at HEAD `c8cc408`.
## Suite: [README](README.md) · [04 the bout](04_the_bout.md) · **05 two modes** · [03 play surface](03_play_surface.md) · [08 mass battle](08_mass_battle_units.md)

**Jordan's intent, verbatim from the session this suite digests:** *"I want there to be a grid
map-based version where you choose to attack and then in fire emblem style you see the bout, but it's my
personal combat engine resolving there for a round — and then a duel version where you actually decide
at each step/beat."* This document says what the engine already provides for each, what it lacks, and
how to build both without a second resolver.

---

## 1. Analysis

### 1.1 The engine already names the right cadence; the season loop does not use it

`wrapper.fight()` carries the comment *"fight() is the multi-turn SIM harness (runs to a decision for
win-rates); the GAME calls one engagement per turn"* (`wrapper.py:477`). The season loop's `fight` verb
(renamed from `kill / wound` on 2026-09-29) reaches `engine/season/seam/wrappers/combat.py`, which calls
`wrapper.fight(A, B, rng=random.Random(seed))` — the harness, run to a decision inside one act. A player
has no point at which to decide anything.

Three details of that seam matter to both modes:

- **Parties.** Each `Combatant` is built from its `Person` with exactly one derived field, `end`, from
  `body_band_penalty`; strength, agility, cognition, tradition, techniques, weapon and armour are class
  defaults ([09](09_the_character_sheet.md) §1.3).
- **Seed.** The provider seeds itself from `H(world_seed, tick, a_id, f"contest:{prize}:{causes[0]}")`
  and deliberately ignores the driver's generator, so as not to re-record every existing fight result.
  A fight is exactly reproducible from the world seed either way.
- **What persists.** `effects_combat._eff_fight` writes `Person.body ← body × health_remaining ÷
  health_full` from the scene's wound tracker. `body` is the only carrier of what a fight did; wound
  count and wound interval are rebuilt from scratch at the next fight, although `combatant.py` records
  that canon wants wounds to persist between encounters until the session ends.

### 1.2 The bout is already recorded — and reduced to one number

`wrapper.py` has a trace hook, `_TRACE`, fired at **20** call sites across fourteen event kinds
(`fight_start, turn_start, engagement_start, approach, stophit, commit, read, mode, roll, outcome,
contact, separation, engagement_end, fight_result`). It draws no random number and mutates nothing, so
capturing it cannot change a result. The seam **already sets it** — `wrapper._TRACE = trace.append` for
the duration of the fight — and then returns `bouts = count(turn_start)`, discarding everything else.
The blow-by-blow a Fire Emblem-style bout screen would play is collected on every fight and dropped at
the return.

### 1.3 What a Fire Emblem or Final Fantasy Tactics clash is

A clash in either is a single formula evaluation: a hit check against evasion, sometimes a critical
check, attack minus defence, perhaps a second strike on a speed gap; Final Fantasy Tactics adds facing
and terrain to the hit check. Their depth lives on the grid — who stands where, who engages whom, in
what order — so the clash must be instant and repeatable dozens of times a map. `[UNVERIFIED: general
knowledge of these games' published mechanics]` This engine inverts the allocation: its depth is in
the clash ([04](04_the_bout.md) §1.5), which is right only if a player-visible fight is a weighty scene.

### 1.4 The Plan layer: decisions at engagement cadence, not beat cadence

`proposals/2026-07-26-personal-combat-player-agency-and-tradition-curriculum.md` (PROPOSED, nothing built)
sets three tiers: **T0 build** (weapon, armour, attributes, techniques — before the fight), **T1 plan**
(one set of intents per engagement), **T2 beat** (engine-only, "must stay closed"). Its six intents sit on
six of the nine moments ([04](04_the_bout.md) §1.3), and three rules bind any player input:

1. A plan is a prior, not a command — it reweights a gate the engine already rolls.
2. Intent is contested, never imposed — it resolves against the opponent's plan, the physics and the read.
3. Every intent is a trade with both ends wired — the cost lands in the same commit as the benefit.

Its own precondition (§9, finding D6) is that a second modulation layer built on a surface where weapon
choice spans ninety points will measure as inert, exactly as the tradition layer did. T2 was closed
because *"A human cannot meaningfully decide at that granularity"* in an engagement that runs in about
ten seconds of fiction. That argument is about cadence, and a deliberately slow duel scene is a
different cadence.

### 1.5 There is no person-scale grid

No squad mechanic and no person-scale grid exist in code. Mass battle is a facing-aware cell field
(51 × 51; the facing octagon multiplies damage received — green 1.0, yellow 1.5, red 2.0). The
repository recorded a route in September: *"a squad is the persons present at a rung, every combatant a
Person; a cohort is a Person at weight > 1 … At weight 1 the same code is a squad game"*
(`references/what_valoria_is_and_what_runs.md` §2, row 7). Season-loop battles already fight on that field
through `resolve_field`, with troop count equal to the summed `Person.weight` of those present
([08](08_mass_battle_units.md) §1.5).

### 1.6 One engine, three fidelities — the shape that works

The repository's precedent research sets Football Manager, which resolves every fixture at three
fidelities of the same match engine calibrated so instant ≈ played, against Total War, whose
auto-resolve is a different algorithm and has diverged for twenty years
(`research/valoria_game_precedent_companion_v1_part2.md` K7, S3). Jordan's two modes plus what already
runs give exactly the first shape:

| fidelity | who sees it | what runs | player decides |
|---|---|---|---|
| **auto** | fights nobody is watching | `fight()` to a decision, one act (today's path) | nothing |
| **grid** | a skirmish on the map | one `engagement()` per attack, its trace played as the bout | whether and whom to attack; optionally one plan per engagement |
| **duel** | a named duel | the same state graph walked beat by beat | intents at the six player-facing moments, each beat they recur |

All three call `combat_engine_v1`. No second resolver exists at any fidelity.

---

## 2. Design

**Grid mode.** An attack command runs one `engagement()` between attacker and defender. Its trace is
the bout the player watches. Body is written back as now; the next engagement between the same pair
rebuilds both combatants from their persons. Whether finer wound state (count, interval) should survive
between engagements is §3 M-3.

**Duel mode.** The state graph advances one beat at a time. When a beat's node carries a player-facing
moment (measure, reopen, commit, mode, counter, contact), the player sets the intent for that beat under
the three rules. At the three closed moments — the read, entry to the bind, the length of a burst — the
engine resolves and the trace narrates. The read in particular stays closed: it is a contest between two
fighters' perceptions, and letting either player declare it would make it a choice.

---

## 3. Recommendations

| # | recommendation | where | observable (falsifier) | cost | gate |
|---|---|---|---|---|---|
| **M-1** | Return the trace the seam already captures, attached to the fight act's result, instead of reducing it to `bouts`. | `seam/wrappers/combat.py` | `World.content_hash()` equal before and after on a seeded season (the hook is side-effect-free); the returned trace is non-empty and its `turn_start` count equals `bouts` | trivial | buildable now |
| **M-2** | Add an engagement-cadence entry at the seam — one act, one `engagement()` — for player-present fights; keep `fight()` as the auto fidelity. | `seam/wrappers/combat.py`, `wrapper.engagement` | over N seeds, the distribution of outcomes after k engagements matches `fight()`'s in shape (a two-sample test), not only in mean — the precedent research's failure shape C | small | PC + IN |
| **M-3** | Decide where wound state lives between engagements: on the `Person` (count and interval as persisted state) or re-derived from `body` bands as now. Canon, per `combatant.py`, wants wounds to persist until the session ends. | `state/carriers.py::Person`, seam `derive_party` | a two-engagement grid fight leaves the defender with the wounds of the first | small | IN, with PC |
| **M-4** | Build the Plan layer only after its own §9 precondition holds: the lever surface must measurably matter first ([04](04_the_bout.md) B-1, B-3). | per the July proposal | its own acceptance gates | medium | after 04 B-1/B-3 |
| **M-5** | Specify duel mode as a cadence contract over the same graph: intents per beat at the six open moments; the three closed moments stay engine-resolved; the three rules unchanged. | a section added to the July proposal | a duel and a grid fight between the same builds, under neutral intents, produce the same outcome distribution | small | PC |
| **M-6** | Prototype the grid as mass battle at weight 1 before authoring a new grid. | `systems/mass_battle/sim/`, `seam/wrappers/mass_battle.py` | a weight-1 contact on the field calls `combat_engine_v1` for the clash | medium | MB + PC |

## 4. For Jordan

Two items survive the five tests in `CLAUDE.md` §0, because each option makes a materially different
game:

1. **Do fights nobody watches keep resolving to a decision inside one act, or span scenes as a grid fight
   does?** One act is simple and final; spanning scenes lets another character arrive, intervene or
   rescue within a season.
2. **Does duel mode open any of the three closed moments?** Recommended: no, for the read above all.
