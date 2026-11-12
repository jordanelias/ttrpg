# MB · the squad of named characters on a formation grid: the scale below a mass battle, on the duel round

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Part 2) — A-4 and Layer 1 §44.3 folded; the grid, the row rule, the sheet, the outcome and the gates stand. (1) The squad's exchange loop and its per-person `DuelState`s cannot live in a wrapper (a wrapper holds no state, decides nothing and drives no clock, `architecture/holonic_ARCHITECTURE.md:1679-1686`; PC addendum F-PC-19). §3's host becomes a **registered entry**, `modules/mass_battle/squad.py::resolve_squad(inp: SquadInput, rng, *, duel, deciders=None) -> FieldOutcome`, reached by a sixth composition row; it holds the states in its own frame and calls the `duel` callable its adapter built (the `combat.round` role, nested at depth 1 under a cap of 1). `engine/season/seam/wrappers/squad.py` is not created; the scale rule stays in `seam/wrappers/mass_battle.py::resolve` as routing (`U5b_MB_rulings_in_the_field.md` §3). (2) It builds on `03_PC_duel_round_and_approach_B.md` (state in the calling loop's frame), not the first PC proposal. (3) A-3: the band is read by the host off the outcome, as for troops. (4) The three conflicts named at the foot are answered: the scale rule is routing between two entries of one module, not a second engine (A-1); the grid suspension's undecided case is one provider call with frame-local state (A-4) and the in-round consult is admitted by A-9; the carried `DuelState` never reaches the world, so the held seeded-damage step is not decided by it.

## Status: PROPOSED

Grounded: 2026-11-12 by `audits/24_GROUNDING_GAMES.md` (GM-01 to GM-03; GC-8, GC-9) — Ogre Battle is now sourced as a battle referent (`research/game_precedent_suite/grounding/ogre_battle.md`). Two notes added in place: the stated reason for not adopting "a member's row decides what it does" no longer holds, and "who can be reached" is not established as what the referents share. No edit of the proposal was changed; the choice between the two row rules is the MB lane's.

Lanes MB (the scale rule, the squad sheet, the host), PC (the round entry it calls), CHAR (the leader's
capability, the chooser's decider), IN (the seam). Carries R-41 of
`audits/04_MB_audit_addendum_B.md` §B6 and its §B4.6. Builds on `03_PC_duel_round_and_approach.md` §2 and
§5.1 (or its `_B` successor where one exists) and on the first MB audit's §15. Reference, not mechanism
(`CLAUDE.md` §0.05).

## What it changes in `engine/season/` at runtime

A field between two sides of named persons only (no cohort member, no army Record) stops being sent to
the cell engine as "two troops against three" and is resolved as a squad exchange: pairings of duel
rounds between the persons present. Every field the shipped realm can fight today is of this kind (first
audit §1.3: the seed-2 field is two persons against three), so this is a declared mover for those fields
and for nothing else. Until the PC round entry exists it changes nothing.

## The problem

- The realm's fields are two to six named persons a side at weight 1. `resolve_field` turns them into a
  headcount and the engine, calibrated for hundreds, returns a constant (first audit F-MB-01, F-MB-02).
  The first audit's R-01 makes that coherent (each person's weight becomes thirty troops); it does not
  make two named people an army, and it writes each of them a body share derived from anonymous troops
  they do not have.
- Jordan's referents for this scale are Ogre Battle and Unicorn Overlord: "small squads of named,
  distinct characters (classes, equipment, roles) placed on a formation grid, given standing tactical
  orders or priorities set in advance … and resolved automatically" (`AUDIT_BRIEF.md:311-315`). Unicorn
  Overlord is sourced (`research/game_precedent_suite/tutorials/T19_tactics_narrative.md:79-155`: up to
  five members, a leader whose effect applies to the squad, per-character Tactics as a priority list with
  up to two conditions, an outcome prediction, an automatic exchange). **Ogre Battle is not sourced as a
  battle referent anywhere in the tree**; what is said of it here is memory-grade and is marked.
  `[superseded 2026-11-12, audits/24_GROUNDING_GAMES.md GM-01 to GM-03: sourced since, in
  research/game_precedent_suite/grounding/ogre_battle.md (pages read in body): squads of five or fewer; the
  player picks one of four tactics per unit and does not control the fighters; a character's row, front or
  rear, decides which action he takes; a unit needs a living leader to take orders.]`
- Ratified Layer 1 already places this scale: "One scale down, unchanged: a squad is the members of a
  faction present at a rung, resolved once, every combatant a `Person`"
  (`architecture/meta/03_VERBS_AND_LOOPS.md:269-270`; `04_CODE_ARCHITECTURE.md:811`). A squad built as a
  mass-battle unit of cells would be the unit class that rule refuses.
- The PC lane has specified the resolver's half and named the missing owner: a squad exchange is "a set
  of pairings, each one duel round"; standing orders are rows of `(condition, approach)`; "its owner is
  the lane that owns squads and orders (MB…)"; "who is paired with whom is the squad host's policy, not
  combat's" (`03_PC_duel_round_and_approach.md` §5.1).

## The resolution, decided

### 1. The scale rule (one owner: the host adapter)

In `engine/season/seam/wrappers/mass_battle.py::resolve`, after the unopposed and invested branches:

```
a side is a SQUAD   iff  it has no order of battle and none of its members is a cohort
a field is a SQUAD FIELD iff both sides are squads
```

A squad field is resolved by the squad host (section 3). Any other field goes to `resolve_field` as now;
a squad facing troops fights as the persons it is, each a one-person body, by the first lane's `person`
arm. `Person.is_cohort` already separates the two for duels (CP-T03-01).

### 2. The squad sheet (data, held by persons, no new kind of thing)

A squad has no object. It is the side's members present, resolved once at the seam (the roster contract).
What a member brings is on the member:

| datum | where it lives | default |
|---|---|---|
| **place** on the grid: `front` or `rear`, and a file 1 to 3 | the standing-order Record the first lane keeps for `marshal` (a seat's `order_of_battle` Record gains `places: ((person, row, file), ...)`) | assigned in claimant order, front row first |
| **standing orders**: at most four rows of `(condition, response)` | the same Record, per person | `()`: fight the one opposite at the `normal` approach |
| **leader** | the acting person for the attackers; the holder of the target for the defenders | — |
| kit, attributes, skills, wounds | the person, read by `combat_input` as for any duel | — |

- `condition` is a closed set over the duel round's turn view, as the PC proposal fixes it (own wounds,
  opponent's wounds, round, measure closed), plus two the grid adds: `front_empty` (nobody stands before
  me) and `leader_down`.
- `response` is an approach (`aggressive`, `normal`, `defensive`), or a target word (`opposite`,
  `weakest`, `leader`), or `withdraw`.
- The grid is two rows of three files a side. **Seed, not a cited fact:** the corpus holds Unicorn
  Overlord's 2 x 3 at memory grade only (`T19:153`).

### 3. The host (pairing policy; no resolver of its own)

*(Reconciled, A-4 / Layer 1 §44.3:)* a registered entry, `modules/mass_battle/squad.py::resolve_squad`,
reached by its own composition row and handed a `duel` callable (the PC lane's `combat.round` role,
built by the adapter through `nested_entry`); it calls nothing else in any module. ~~New
`engine/season/seam/wrappers/squad.py`, called by the mass-battle provider for a squad field.~~

```
state: one DuelState per person (the PC proposal's record), held in this entry's loop frame for the length of the call
each exchange (at most FIELD_EXCHANGES, the troop file's header; seed 3, the engine's three phases):
    for each standing member, in initiative order (the round's own; the host adds none):
        target = his standing order's target word, resolved on the grid:
                 a front-row member may be struck by anyone;
                 a rear-row member may be struck only when his file's front place is empty,
                 or by a striker whose weapon in hand is a missile or pole weapon
        approach = his standing order's approach, or a played member's decider, or the chooser's
        pair (member, target) -> one combat.round call on their two DuelStates
    a member felled or yielded leaves the grid; his file's rear member is then exposed
the field ends when a side has no standing member, when a side's standing orders all say withdraw,
or at the exchange cap
```

- Outnumbering needs no rule: a member paired twice in one exchange fights two rounds on one carried
  state, the arithmetic the PC proposal already describes.
- The row rule is the whole of what "formation" means at this scale, and it is the one thing the
  referents share that a duel lacks: who can be reached. `[memory-grade: in Ogre Battle a member's row
  also decides what it does; not adopted, because nothing in the tree sources it]`
  `[Grounded 2026-11-12, audits/24_GROUNDING_GAMES.md GC-9. Two facts, no decision taken here (the choice is
  the MB lane's). (a) The reason given for not adopting it no longer holds: that a member's row decides his
  action is now sourced (grounding/ogre_battle.md row 5, a review read in body: "one they do when they are
  in the front row, and one for the rear row"). (b) "Who can be reached" is **not** established as what the
  referents share. In Ogre Battle, as sourced, whom a unit strikes is set by its tactic (Best, Strong, Weak,
  Leader), and a fan strategy page has spellcasters under the Leader tactic striking a leader who "usually"
  stands in the back row (grounding/ogre_battle.md rows 3, 4, 12; whether melee reaches the rear is not
  established). For Unicorn Overlord,
  "position influenc[es] their abilities and combat efficiency" is page-read; that the back row can be hit
  only by ranged or column attacks is one search snippet (grounding/unicorn_overlord.md). The reach rule
  above is therefore this proposal's own design, with snippet-grade precedent from one game.]`
- **The leader.** A leader adds nothing by rule. What he adds is a capability read through the capability
  surface the CHAR lane owns (a command capability, the first audit's §14), applied as the PC proposal
  applies any lever: a prior on gates the duel already rolls for his squad's members. Until that
  capability exists a leader is only the person whose fall fires `leader_down`.
- **Decider.** A played member is asked for his approach between exchanges through the same callable the
  duel uses; an unplayed one is served by his standing orders, or by the chooser. Delegated and commanded
  are the same rounds (the manager proposal's three conditions hold here unchanged: one entry, a decider
  that draws nothing, a recorded list of choices that replays exactly).
- **Prediction.** `field_estimate` on a squad field is samples of the same host on a private stream, as
  for a field of troops.

### 4. The outcome (one shape for both scales)

The host returns the first lane's `FieldOutcome` with the manager proposal's change (no `verdict`): each
side's `parts` are its persons, `share` is the person's remaining body on the body scale as the duel
round left it, `routed` is felled or yielded, `broke_first` the first to fall. `field_degree` reads the
band off it by the same rule as for troops (a side is out when none of its members stands or all have
withdrawn). `_eff_march` writes one way for both scales; the wounds a round deals are written as the
combat provider writes them. A fallen commander is named in the outcome, which is what a `capture` act
on `field.won` needs (first audit §5.5).

## Exact edits

| file (owner) | edit |
|---|---|
| `engine/season/seam/wrappers/mass_battle.py` (IN) | the scale rule; dispatch to the squad host |
| `modules/mass_battle/squad.py` (MB, new) *(Reconciled)*; `references/module_contracts.yaml` (a composition row `mass_battle.resolve_squad`); `engine/season/queries/inputs.py` (`SquadInput`) | the entry above; it is handed `duel`, which the adapter resolves by `composition.require('combat.round')` through `nested_entry` |
| `engine/season/rosters.yaml: record_kinds` (IN) | the standing-order Record's `subject_matter` gains `places` and per-person `standing_orders` |
| `references/troops.yaml: deployment` (MB) | `field_exchanges`, the grid's `rows` and `files` |
| `engine/engine_params/battle_orders.json` via `tools/export_battle_orders.py` (MB) | the squad's `conditions` and `responses` closed sets |
| `modules/combat/` (PC) | nothing beyond the PC proposal's round entry |
| `modules/mass_battle/` (MB) | the new `squad.py` only; the cell engine is untouched |

## Gate (execution artifacts)

1. `build_realm(2)`, one season, the field the shipped realm fights (two against three): the Event is a
   fought band; each of the five persons' `body` moves by what his own rounds did to him and by nothing
   else; no person's body equals his side's headcount over a constant (the first audit's F-MB-02 artefact
   is gone for this field).
2. Same seed, two sheets for one side (its leader `front` against `rear`): the persons hurt differ.
3. A rear-row member behind a standing front member is paired by no melee striker in any exchange
   (asserted on the trace, with a count of exchanges checked, so the loop cannot pass by not running).
4. Delegated against commanded: a decider that returns each member's standing-order response gives the
   same outcome and the same draw count as no decider.
5. `git grep -n "modules.combat" modules/mass_battle/squad.py engine/season/seam/wrappers/mass_battle.py`
   prints nothing (the role, not an import).
6. A side with one cohort member is not a squad: the field goes to `resolve_field`.

## Falsifier

A squad field whose result does not change when a member's kit, wounds or place changes; a rear member
struck through a standing front member by a sword; a squad exchange that draws from the cell engine; a
second duel resolver anywhere.

## NERS (definitions `CLAUDE.md` §0.06)

- **N.** Bottom-up: these fields exist today and are resolved by the wrong instrument. Top-down: two of
  Jordan's five referents are this scale. Lateral: it is the duel round, reused; diagonal: the same
  standing-orders, decider, report shape as the battle of troops. Cut it and named characters stay
  thirty anonymous spearmen each.
- **R.** Who stands where, who strikes whom and how hard are choices; persons' kits and skills matter;
  the world fights such fields with nobody watching, and a named person falls in them.
- **S.** One outcome shape and one grading rule across the two scales; pauses between exchanges as a duel
  pauses between rounds; no new resolver, so calculations are consistent by construction.
- **E, last.** One host file, one rule about rows, two closed sets. A player can see why the healer
  lived: she stood behind the shield.

## Cost class

Design-first for the row rule and the exchange cap (both seeds); small build after
`03_PC_duel_round_and_approach.md` steps 1 to 4. Blocked on that proposal and on nothing in
`modules/mass_battle/`.

## Conflicts with ruled or ratified items, named and not resolved

- **"One engine at every fidelity"** (2026-07-08) read as "every `march` goes to the cell engine": the
  scale rule contradicts that reading. Read as it is written, about the played and the delegated
  resolution of one contest, there is no conflict (first audit §15).
- **The ratified grid suspension** (REM-31, `proposals/2026-10-07-grid-mode-suspension.md`): it covers one
  provider call for one deferred act and lists "the grid map" as not decided. A squad field in which
  several members act between two rounds of one pair is that undecided case (PC proposal §6 item 1).
- **CR-85 §4 step 2** (held): a carried `DuelState` decides it in practice (PC proposal §6 item 3).
- `engine/season/requirements.yaml`'s combat scale row reads "grid-based map combat with units" as the
  cell field (an ASSUMPTION there). This proposal makes the other reading a second, separate thing; the
  row should say which it counts. CORE's.
