# 16 · PESSIMIST · PC · C — what the world keeps of a fight: the scene's shape, and the hand that killed

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` §1.5) — one consistency note; no edit changes. A-33 (news of a death travels by presence, trail and telling, apart from the seat's news): the `fell_to_hand` Observation rides the death's own Event, so the killer's name reaches exactly those the death reaches and no further; nothing here widens who learns of it. The scene's `shape` is also what a nested round returns to a field (`U5b_PC_rulings_in_the_fight.md` §1), so an officers' duel inside a battle is retold by the same five facts.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-5a. Rows applied: `R5_READ.md` §1 (AMBIGUOUS against `04` §C.6: an U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "fought scene" → "fight" (glossary *scene*); "typed record" → "dataclass" (glossary *record*).
Observation that names a doer reaches only channels that mint attribution) and §2 (A-33), U1 D-U1-06 (`observed` is the
one channel; every predicate here is a member of the closed roster `rosters.yaml: observation_terms`, which resolves the
`[name it at landing]`; `fell_to_hand` and `first_blood` are deposited only through channels whose
`observation_terms.supplied_by` includes `who`), D-U1-11a (the victor's `fight_endings` member is `prevailed`, not
`standing`), §7/§7b (gate row 5, test file, tier); U3 B14, §6.2 (`pS_season.py`, `pS2.py` are not in the repository).
Changed: the head paragraph's member name, edit 1's roster sentence, edit 2's variable name, the gate.

## Status: PROPOSED

Lands in batch: **B14** (PC), after `03_PC_typed_outcome_one_door.md` Part A and `03_PC_weapon_form_at_round_start.md`
(B14). Depends on: Part A's `CombatOutcome` and `fell_to`.

Source: `audits/16_PESSIMIST_PC.md` §3.3 (F-PES-PC-05, F-PES-PC-06). Extends, and does not restate,
`03_PC_typed_outcome_one_door.md` Part A (the typed `CombatOutcome`, its `DecisiveBeat`, the `fell_to`
Observation and the victor's member of `fight_endings`, `prevailed` by D-U1-11a). Reference only (`CLAUDE.md`
§0.05); not ratified by being written.

## What it changes in `engine/season/` at runtime (first)

Each fight's success Events carry up to five more `Observation`s (the scene's shape), and the
`person.died` Event of a felled *actor* carries one naming the standing party. `person_q.deed_doer`
reads that one before the `seen.who` pairing. **Declared hash mover for every log with a fight**
(`Event.observed` is hashed). No band, kind, carrier or store is added; nothing is kept between scenes.

## The problem (evidence)

`pS_season.py` S1, one `fight` at world seed 1003, through RESOLVE, ENCOUNTER and WITNESS:

- the scene: 8 turns, 14 exchanges, 5 wounds, 2 grapples (110 trace events); the winner ends on 12 of 40
  Health with three wounds;
- the log: `fight.declared`, `person.died`, `body.changed`; `ending = (('p_low', 'undecided'), ('p_mid',
  'felled'))`; no turn count, no blow, no reversal anywhere in the three Events;
- the trace is returned (`seam/wrappers/combat.py:422`) and read by nothing but `surrender_of`.

`pS2.py` S7, 100 `fight` scenes: 306 `person.died` claims are held afterwards; 106 name a living person
(the actor's anchor claim, `queries/person_q.py:259-262`). Where the actor is the one felled (148 of 300
scenes, S2), the only death claim names him, and no claim names the man who killed him: the stated limit
at `person_q.py:266-268`. Its frequency is one killing in two.

The typed-outcome proposal fixes the victor's word (`standing`) and keeps the killing blow (`fell_to`).
It keeps nothing of the fight before that blow (`turns` and `trace` are on the record and "folded
nowhere"), and `fell_to` carries the blow's source and weapon, not the hand.

## The resolution, decided (ladder step 4: the tree's own precedent)

The precedent is `CP-T04-01`'s `broke_observed` and the typed-outcome proposal's `fell_to`: an Event
has no payload, so a fact of the scene rides `Event.observed` as an `Observation(subject, predicate,
value)`. Two additions, both computed by the module from its own trace and returned on the typed record.

**1. The scene's shape.** `CombatOutcome` gains `shape: SceneShape`, built in `fight.py` from the trace
it already holds (a pure fold over `wound`, `turn_start`, `yield`; no new engine event):

```python
@dataclass(frozen=True)
class SceneShape:
    turns: int                 # turn_start count (today's `bouts`)
    blows: Mapping[str, int]   # wounding blows LANDED, by claimant id
    first_blood: Optional[str] # who landed the first wounding blow; None if none landed
    lead_changes: int          # times the party ahead on Health fraction changed
    nearest: Mapping[str, int] # each party's lowest Health remaining during the scene, in points
```

`loop/effects_combat.py::_eff_kill` puts on the act's success Events, for each party `p`:
`Observation(p, "blows_landed", shape.blows[p])`, and once per scene (subject the actor):
`Observation(actor, "fight_turns", shape.turns)`, `Observation(shape.first_blood, "first_blood", True)`
when not `None`, and `Observation(actor, "lead_changes", shape.lead_changes)`. Five facts, each one a
number or a name the scene already computed; a narrator, the chronicle and a played person's display
read them off the log. The predicates are members of `rosters.yaml: observation_terms` (`:1273`, the closed
roster `fell_to` also joins, D-U1-06); the loader refuses a predicate on `observed` that is not a member.
**Who may hold the names.** `first_blood` and `fell_to_hand` name a person as a doer: WITNESS deposits them only
through channels whose `observation_terms.supplied_by` includes `who` (`co_located`, `witness_key`), never through
`document_key`, `post_remit` or `chronicle` (`04` §C.6: attribution per channel). The counts (`blows_landed`,
`fight_turns`, `lead_changes`) name no doer and ride every channel the Event's other facts ride.

**2. The hand.** For a felled party who is the act's *actor*, `_eff_kill`'s Subject carries
`Observation(felled, "fell_to_hand", prevailing_party)`. `queries/person_q.py::deed_doer` reads a
`fell_to_hand` Observation on the claim's Event first and returns its value; the `seen.who` pairing
stands for every other case. This closes the stated limit at its site and guesses nothing: the fold
knows who the other claimant was.

Not taken: storing the trace (a second copy of scene state in the world; `04` §A.2 forbids a module's
state outliving the call) and a new Event kind per beat (the fold's kinds are the row's bands).

## Exact edits, by owner

| file | edit |
|---|---|
| `engine/season/queries/inputs.py` | `SceneShape` beside `CombatOutcome` (after `03_PC_typed_outcome_one_door.md` Part A lands) |
| `modules/combat/fight.py` | builds `SceneShape` from `trace`; no engine change |
| `engine/season/seam/wrappers/combat.py::resolve` | returns `shape=` beside `beat=` |
| `engine/season/loop/effects_combat.py::_eff_kill` (and `_eff_capture` through its base) | the Observations above |
| `engine/season/queries/person_q.py::deed_doer` | the `fell_to_hand` read, before the pairing; the `LIMIT, stated` note at `:266-268` restated as closed |
| `engine/season/harness/chronicle.py::lines` | where an act's Events carry `fight_turns`, the line appends `(n turns, first blood X, k lead changes)`; a render change only |

## Gate (execution artifacts)

The S1 and S7 probes were lane scratch (not in the repository). NEW `tests/valoria/test_combat_scene_shape.py` (beside
`test_combat_audit_pins.py`, which exists): `test_scene_shape_is_a_pure_fold_over_trace`,
`test_fell_to_hand_names_the_prevailing_party` (gate 2), `test_played_and_automated_scenes_carry_equal_observations`
(gate 4), `test_document_post_remit_and_chronicle_witnesses_hold_no_fell_to_hand` (gate 5). Command:
`python -m pytest tests/valoria/test_combat_scene_shape.py -q -m combat`. Readings:

1. The S1 reading (a fight at world seed 1003): the three Events of the seed-1003 fight carry `fight_turns 8`, `blows_landed`
   for both parties summing to 5, `first_blood` and `lead_changes`.
2. The S7 probe re-run over 100 fights: in every scene where the actor is felled, `deed_doer` on the
   bystander's `person.died` claim returns the standing party; before the change it returns `None` or
   the dead man.
3. Control: with the Observations withheld the pre-change hash returns.
4. A played `fight` and an automated one from equal choices carry equal Observations (the module
   computes them from the same trace).
5. A `document_key`, `post_remit` and `chronicle` witness of the death holds no `fell_to_hand` and no
   `first_blood` (the hand reaches only `who`-supplying channels).

## Falsifier

A fight whose Events let a reader recover neither its length nor who struck first; a death in
self-defence after which no witness can name the killer.

## NERS reading

- **N.** Bottom-up: the module computes it and the seam drops it. Top-down: R-01 (propagation) and R-07
  (memory) ask that a deed be something others can hold. Lateral: the field's `broke_observed` does this
  for a battle. Diagonal: regard and vengeance (CHAR's CP-T03-06) need the killer's name before they can
  weigh anything. Cut it and every fight is retold as its verdict.
- **R.** The half with no player: a chronicle line with a shape; the self-defence killer becomes
  knowable, so a grievance can form against him. Completeness: a scene with no blow carries
  `fight_turns` and nothing else.
- **S.** One channel (`observed`), the precedent's; no second store; equal across the two modes.
- **E, last.** One frozen record, five predicates, one read in `deed_doer`. High against what N and R
  found; it needs the dataclass first.

## Cost class

Edit, after `03_PC_typed_outcome_one_door.md` Part A. Tier: `sonnet`, effort `high`. Hash movers declared: every log
with a fight (`Event.observed` is hashed); one re-pin at B14's close. Lands it: B14, order the roster members →
`SceneShape` and the module fold → the seam's return → `_eff_kill`'s Observations → `deed_doer` → the chronicle line.
