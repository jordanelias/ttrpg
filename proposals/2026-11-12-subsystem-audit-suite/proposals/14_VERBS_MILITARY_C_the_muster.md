# VERBS · MILITARY · C — the muster: `recruit`, `discharge_troops`, and a commander who is a person

Reconciled: 2026-11-12, U5b closure (`unified/U5_FINDINGS_CLOSURE_U5b.md` Parts 3–4; `U5b_VERBS_military_physical_residue.md`) — (1) **Layer 1**: `recruit` and `discharge_troops` write one cell on every band, so they are task rows with **flat** `writes:` and `emits:` (residue §1, shape (a)): the `share` 1.0 / 1.0 / 0.5 is the roster `task_fraction`, read and not restated; `levy.shirked` and `discharge.balked` are the keyed `emits_on_refusal` clause `draw`; the roster is `graded_tasks`. (2) **A-5, A-6, A-7**: one sampler; the pool is the one pool rule on the commander's `command` score, the same capability row the field's obedience draw reads (A-59; `proposals/27_MB_*`, another lane's, which define it once). (3) **A-25**: `cohort_committed`, `footing_war` and `levy` are named levels for the roller. (4) Edit 7's `armies_at_build` is the **one** fixture for armies at build (`04_MB_playable_field_scenario.md`'s `army_presets` yields to it), and Edit 5's opportunity-key digest is the one such edit. (5) A-22 and A-23 bear on who may levy and whether a detained commander commands: both are read where the seat's act is formed (FA's; `06_FA_levy_through_the_seat_B.md`). A-15 (natural death on) makes Edit 6's successor and dispersal reachable in ordinary play. A-2: the roll is a Record a person holds.

Reconciled: 2026-11-12, wave-3 rewrite lane W3-4a — the head line applied to the body (`unified/work/R4_READ.md` §1.3, 7b.5; F-R4-01, F-R4-02): Edit 4's rows take shape (a) (flat columns; `levy.shirked`/`discharge.balked` the `draw` refusal clause) and the `room` conjunct leaves the typed cell (G-04's fallback: asked at formation and by the effect, refused under `write`; C3-R7); Edit 5's `graded_inquiries`/`verb_capability` lines become `graded_tasks` membership and the row's `capability: command` cell (D-U1-07, U1 capability architecture §5); the favourable modifiers are leverage levels (C3-C10, A-25) and the hostile ones are listed for U1 as non-members of OBS §2 (INCOMPLETE); Edit 6's `loop/matter.py` dispersal pass is **deleted**: an unheld army's present strength is computed when read and changed only by the next act on its Record (`unified/U3_CONFLICT_LEDGER.md` C3-L11, which decides R4's J-R4-3 by a third option; U3 governs over R4 7b.5's cohort-act default); the 27-lane fold's "a seat's modifier as whole dice" follows U1 D-U1-01 (an `office` level, never dice); A-81, A-30, U3 batch B22, R4 7b.0 block. U4d glossary lane (2026-11-12, `unified/U1_GLOSSARY.md` §H–§I, ledger `unified/work/U4D_RENAMES.md`): "subformation" → "unit" in prose (glossary *unit*; the Record key `subformations` keeps its name).

## Status: PROPOSED

Lands in batch: B22 (`unified/U3_DEPENDENCY_ORDER.md` §3.1), after `14_VERBS_MILITARY_A_movement.md`; `04_MB_playable_field_scenario.md` §E (armies at build) lands here (U3 §4.1 row 69) and `17_CENSUS_C1A_02` W2's gate for these rows rides here (row 38).
Depends on: `06_FA_levy_through_the_seat_B.md` (B21: `state/gate.py::may_levy`, `may_wage`, both MISSING in the tree today; `world_q.raisable_by` exists, `queries/world_q.py:2186`); `07_SE_campaign_supply_and_muster.md` (B22); `27_MB_A_command_and_the_obedience_draw.md` (B19: `command`'s definition); `27_MB_E_what_an_army_carries_back.md` (B22: the loss ledger the strength read uses); `18_DETERMINISM_task_draw_for_uncontested_verbs.md` items 2, 4 (B07); `05_SC_obstacle_difficulty_and_modifiers_B.md` (B05).
Lane: MB (module), FA (gate), season rows. Tier (R4 7b.0 (1)): `sonnet` producer, effort `high`, for Edits 1–5 and 7; Edit 6's read (a keyed graded draw that sets an army's strength) `opus`; one `opus` read of the dispersal and successor gates. Test file: `engine/season/tests/test_vm_mil_c_muster.py` (one function per §4 gate; the scratch probe `probe_army_s0.txt`'s death sequence is restated as the successor function, U3 §6.2's rule).
Standing (R4 7b.0 (4)): the pool is the one pool rule (`sigma_leverage.pool_of`, D-U1-08) on the commander's `command` skill score (A-6, A-59); Presence and Reason as levels (A-7); a wound a level against the roll (A-8); the muster seat helps only as the `office` level (D-U1-01). Draws: `H(w.world_seed, w.tick, <actor id>, "recruit.task")`, `"discharge_troops.task"`; the strength read's draw `H(w.world_seed, <army id>, "army.disperse", <season>)` (A-30). **A-81:** `levy.shirked` and `discharge.balked` are refusal Events witnessed by the commander and the cohort persons at the muster rung (a claim of it to each), and every army Event carries the `muster_room`/`surplus` Observations (Edit 5).

Folded: 2026-11-12 by `audits/27_MB_COMMAND_AND_DYNAMIC_STRENGTH.md` (rulings A-59 and A-69). Nothing here is deleted. (1) The `command` capability the Reconciled line's item (2) points to is defined in `27_MB_A_command_and_the_obedience_draw.md` §1: trained rank as the pool, Presence and Reason as levels, and the seat's modifier as the `office` level (U1 D-U1-01; *W3-4a: the earlier "whole dice on the commander's pool" is superseded*). (2) **A-69**: once a unit's losses are written on its row, what the army holds of a cohort is `assigned` plus the men absent injured or fled, who are alive and still the cohort's; `recruit`'s limit and `discharge_troops` count them so, and a levy cannot be raised twice over by losing a battle (`27_MB_E_what_an_army_carries_back.md` §2). The dispersal of Edit 6 and the flight of a routed unit are two different events with one result on the strength a reader sees (men off the strength, of whom some drift back unprompted and some desert, A-78; a muster at the cohort's home is taken to bring more back or sooner); both are computed when read and written by an act (C3-L11).

Grounded: 2026-11-12 by `audits/25_GROUNDING_ENGINE.md` (G-04) — a typed conjunct cannot be waived by a payload key (`data/requires.py:1027-1030`); the proposal's stated fallback for `room` is now the edit. `14_VERBS_MILITARY_D_the_order_of_battle.md:128` carries the same mark and takes the same answer.

Batch M-C of `audits/14_VERBS_MILITARY.md` (§1 S3, §3.1, §3.2, §5.3). Source: F-VM-02, F-VM-03,
F-VM-06; `audits/04_MB_audit.md` F-MB-03, F-MB-13, F-MB-16; `AUDIT_BRIEF.md` "Standing rule". It
**adopts** `06_FA_levy_through_the_seat_B.md` (who may levy) and builds on it; it carries the mechanism
proposal D's four rows share. The army Record and its rule stay ED-IN-0306's and the module's. Nothing
is ratified by being written.

## 1. What it changes in `engine/season/` at runtime

1. A person who holds an `army` Record forms `recruit` and `discharge_troops` on it through the one
   chooser, when the army has room to raise or men to spare. Nobody else forms them.
2. A command with no payload is carried out to the army's doctrine and footing by the module; a
   command with a payload is unchanged (the menu's).
3. A levy and a discharge are each one draw: how many answer, how many go.
4. A dead commander's roll is taken up by his successor; a leaderless army, and troops an army may no
   longer keep, thin by chance: their present strength is computed when read (C3-L11), and the next act
   on the Record writes it.
5. With `armies_at_build: off` (shipped) no `army` Record exists, so nothing forms and the realm,
   spine and corpus hashes are EQUAL but for one declared mover (Edit 3's kind narrowing).

## 2. The problem (evidence)

- `data/fixtures.py:1157`: the six army verbs are withheld; `rosters.yaml:2671-2680` gives the reason
  (the command is payload, no Candidate carries it). `aperture 2 0`: formed 0, the six `army.*` kinds
  never emitted.
- `harness/army_presets.py:12-20`: the unplayed commander's army is folded between seasons, outside
  DELIBERATE and outside anyone's budget, from a plan that "draws nothing"; nothing calls it.
- `probe_army_s0.txt` (`build_realm(0)`, hand-built acts through `SeasonDriver.resolve`): the verbs
  execute; a levy of 60 raises exactly 60; after the commander's death through the gate `army_of`
  is `None`, `other_army_records` still returns his army, and
  `armyrecord.cohort_claims` counts its 40 levy against the successor's new army
  (`queries/world_q.py:2198-2203` has no holder test where `army_of`, `:2278-2287`, has one).
- `armyrecord.py:303-311`: the cap is asked at `recruit` only; a cohort whose `weight` falls, or
  that leaves the faction's ground, keeps its men under arms.
- An army costs nothing to keep (`07_SE_campaign_supply_and_muster.md` §2), so `discharge_troops`
  has no motive; SE's three arms supply it and are cited, not redone.

## 3. Exact edits, by owner, in landing order

**Edit 1 — the module: doctrine step, footing, state** (`modules/mass_battle/armyrecord.py`;
owner MB, reviewed by it).

- `KEYS = ('faction', 'strategy', 'trained', 'subformations', 'doctrine', 'footing')`;
  `new(faction, strategy='line', doctrine=DEFAULT_DOCTRINE, footing='peace')`; `validate` accepts a
  record lacking the two new keys as carrying the defaults (no minted Record exists in any shipped
  world; `rosters.yaml: record_kinds.army` mirrors the six).
- `target(record, cohorts, full, others) -> {(cohort, troop_type): count}`: the doctrine's shares
  (`troop_types/presets.py::ARM_SHARES` today; `references/troops.yaml: doctrines` when MB's troop
  file lands) of each cohort's `under_arms_cap`, times the footing's share (`FOOTING_SHARE =
  {'peace': 0.25, 'war': 1.0}`, `[ASSUMPTION; medium; Jordan to correct; revert: 1.0 for both]`),
  each entry bounded by `recruit_limit`.
- `step(record, op, facts) -> ((op, args), ...)`: the primitive commands a payload-less `op` stands
  for. `recruit`: `target − by_type`, per cohort, positive entries. `discharge`: `by_type − target`,
  plus every trooper of a cohort absent from `facts.cohorts`, plus the excess over a cohort's
  present cap; unassigned first, then released from the largest unit.
- `_apply`: an op whose `args` carry no command key runs `step` and folds its commands in order;
  `args['share']` (the host's `rosters.yaml: task_fraction` value for the band, read through
  `loop/effects_shared.py::graded_amount`'s table and never restated) scales each count, rounding up.
- `options(q)` gains three keys beside `raise` and `advisories`: `muster_room` (bool: `step('recruit')`
  is non-empty), `surplus` (bool: `step('discharge')` is non-empty), and the three booleans proposal
  D reads. One function decides what the menu shows and what the cell asks.

**Edit 2 — `engine/season/queries/world_q.py`.**

```python
def army_state(w: World, rid: str, actor: str) -> dict:
    """The module's `options` for the army `rid` as `actor` may command it: `ArmyOptionsQuery(record,
    cohorts the actor may levy (state/gate.py::may_levy through his muster seat), full, others)`.
    The one reader the six army rows' third conjunct asks; `harness/military_menu.py::menu` calls it."""
```

`other_army_records` is unchanged (an unheld army's men are still under arms until they disperse or
are taken up; Edit 6). `data/requires.py: REQUIRES_STEMS` gains the relation stems `muster_room` and
`surplus`, asked `of: subject` and the actor (`room`'s shape), answered by `army_state`; neither is
world-only, so a refusal's read is deposited to the actor.

**Edit 3 — formation** (`engine/season/decision/options.py::opening_set`; mover).

- After `refs = row.referents_of(q)`: for a row whose class is `Record` and whose cell asks
  `existence` of a record sub-kind and `held_by` of `subject` (read off the cell,
  `data/verbs.py::_asks_subject_held`, never a verb name), keep only the referents whose
  `content:<kind>` claim in the person's own ledger is of an asked kind. New helper beside
  `held_record_claims`: `held_record_kinds(p) -> {record id: kind}` (the same read without the
  `record_sourced_operands` filter). **Declared mover** for `carry`, `comply`, `found`, `build`:
  REM-25's wrong-kind residue (2 / 3 / 2 refusals a season at seeds 0 to 2) stops.
- `[UNVERIFIED: that a minter's ledger receives `content:army` in season (WITNESS's fourth deposit,
  `loop/witness.py:823-846`, reads `newly_held`); the probe folds between seasons, where WITNESS does
  not run.]` If it does not, the mint's Event is added to `newly_held`'s sources; no other deposit
  is proposed.

**Edit 4 — the rows** (`engine/season/verb_table.yaml`). `recruit`, final text of the changed
columns (`discharge_troops` is the same with the substitutions listed under it):

```yaml
  - verb:        "recruit"
    stratum:     "uncontested_material"
    eligibility: ["remit:dispatch"]
    beneficiary: "none"
    referent_class: Record
    referent_class_note: "14-VM-C: FORMED ONLY ON AN `army` RECORD THE PERSON HOLDS -- `records_held_for_holding_rows` stamps it (`HOLDING_RECORD_KINDS` derives `army` off this cell), and `opening_set` keeps a held Record only where his own `content:` claim is of the asked kind. REVERT: delete this column; the row is hand-built only, as before."
    requires:    "the subject is an army record the actor holds, and the army may raise more men from cohorts his seat may levy"
    requires_typed:
      all:
        - form:      existence
          of:        subject
          kind:      army
          conjunct:  army
        - form:      relation
          of:        subject
          relation:  held_by
          conjunct:  command
    capability:  command          # U1 capability architecture §5; `27_MB_A` §1 defines it
    difficulty:  routine
    writes:      ["Record.subject_matter"]   # shape (a): one cell, the band scales the count
    writes_note: "14-VM-C: `armyrecord.apply` with `share` = `task_fraction[band]` (1, 1, 0.5); a failed draw writes nothing and emits `levy.shirked` (the `draw` refusal clause). A payload naming `cohort`, `troop_type`, `count` is one levy; none is the doctrine's step (`armyrecord.step`). The seat's right over the cohort is `state/gate.py::may_levy` (FA). [ASSUMPTION; medium; Jordan to correct; revert: the flat write without the draw.]"
    emits:       ["army.recruited"]
    emits_on_refusal:
      eligibility: ["recruit.unauthorized"]
      army:        ["recruit.refused"]
      command:     ["recruit.refused"]
      write:       ["recruit.refused"]
      draw:        ["levy.shirked"]
    refusal_note: "KEYED PER CLAUSE. `room` is not a typed conjunct (G-04): it is asked at formation (`belief_contradicts`) and by the effect for a payload-less act, and refused under `write`; its read `(army, muster_room:<actor>, False)` rides the Event and is deposited to the actor, so a commander at strength does not call the levy again until he learns otherwise (REM-29's limit applies and is `01_CORE_claim_fade_as_read.md`'s to lift). `write` also covers a payload the module refuses (an unknown kind, a count over the cap), or a cohort the seat may not levy."
    grade:       "assumption"
```

**The `room` conjunct binds a doctrine step.** A spoken command (a payload naming cohort, kind and
count) is bounded by the cap alone, in the effect, as now: a player may raise beyond his doctrine's
shares. `[GROUNDED, 25 G-04: it cannot. A typed clause is a `form` from the closed `requires_forms`
roster with that form's fields and nothing else (`data/requires.py:1027-1030`; the classes at `:292-558`);
no clause carries a waiver or a payload condition. So `room` is asked at formation (`belief_contradicts`) and by the effect for a payload-less act,
and its refusal key is `write`. Proposal D states the same for its four rows.]`

`discharge_troops`: the same row with `surplus` (asked as `room` is) for `muster_room`; flat `emits:
["army.discharged"]`; `draw: ["discharge.balked"]`; refusal kinds `discharge_troops.unauthorized` and
`discharge_troops.refused`.

**Edit 5 — the draw and the effects.**

- `rosters.yaml: graded_tasks.values` gains `recruit` and `discharge_troops` (shape (a)); the
  skill is each row's own `capability: command` cell (D-U1-07), not a `verb_capability` line;
  `army_verbs` is unchanged.
- Obstacle and leverage, through the one composer (`[ASSUMPTION; medium; Jordan to correct]` each):

  | verb | difficulty | obstacle terms | leverage (levels for the roller, A-25; C3-C10) |
  |---|---|---|---|
  | `recruit` | `routine` | `muster_difficulty` (by troop kind: a column of the troop table; until it lands, 1 for a kind with no training Site, 2 for one with, 3 where `TRAINING_SITE`'s floor is above 0) · `cohort_resents` (the cohort holds a negative stance row toward the faction; for a doctrine step, any cohort in the step) · `larder_short` · `half_under_arms` | `cohort_committed` · `footing_war` |
  | `discharge_troops` | `routine` | `arrears` (a live ration `shortfall` on the army's treasury) · `on_foreign_ground` | `levy` |

  **INCOMPLETE (blocked on U1, R4 7b.8):** the obstacle terms are not members of OBS §2's closed roster
  and the levels are not named sources of `advantage_sources`; U1 decides members, folds and sources
  (`cohort_resents` reads a stance row and may be the existing member `regard`; `larder_short` may be
  `stakes`, as for `migrate`). Until then each ships absent (0): the control is `routine`.
- `loop/effects_army.py`: `_eff_recruit(w, a, res)` and `_eff_discharge_troops(w, a, res)` are reached
  only on a won draw (a failed draw is the `draw` refusal, emitted with no write); they build `args` as
  now, adding `share` (`task_fraction[res.degree]`) and, when the payload names no command, `cohorts`
  (`may_levy`'s set with weights and sites). Every army Event carries `Observation(rid, "muster_room:<actor>", bool)` and
  `Observation(rid, "surplus:<actor>", bool)` read from `army_state` after the write, so the
  commander's belief follows his own acts.
- `data/verbs.py::act_key` and `opportunity_key`: for a verb in `ARMY_VERBS` whose operands carry a
  command key, the key gains a digest of the command (the choice suffix's shape), so the menu may
  give several spoken commands a season; a doctrine step carries none and is once a season
  (MB R-17's disposition, built).

**Edit 6 — the roll outlives its holder.**

- `loop/effects_information.py::_eff_create_record`, the `army` branch: where an unheld `army`
  Record of the minter's faction exists (lowest id), the effect opens the minter's `hold` on it and
  mints nothing (`record.taken_up`); `_army_mintable` admits it under the same conjuncts.
- *(W3-4a, C3-L11: the `loop/matter.py` pass is deleted.)* MATTER may not write an army's strength:
  `(Record, subject_matter)` is an ACTS row written at RESOLVE (`engine/season/write_matrix.yaml:353-359`),
  and a MATTER pass would be a fourth motion (`04` PART D 17; `holonic` §29). Instead, **computed when
  read** (the D-48 precedent): a new reader `queries/world_q.py::present_strength(w, rid) -> dict`
  returns the Record's `by_type` counts less, for an unheld `army` Record (and for troops a held one may
  no longer keep: `army_state(...)['surplus']` true for a cohort gone or shrunk), the dispersed share: for
  each season since it became unheld (or since the surplus arose), one keyed graded draw
  `H(w.world_seed, rid, "army.disperse", season)` at rate `Fixtures leaderless_dispersal` (swept;
  NUMBER row in `hole_register.yaml`), reading hold · half of the affected troops go home · all go,
  composed in season order. Every reader of an army's strength reads it: `army_state`,
  `other_army_records`' counts, `armyrecord.cohort_claims`' input, `seam/wrappers/mass_battle.py::
  _order_of_battle`. The **next act** on the Record (the successor's `record.taken_up`, or any army verb)
  writes the read value into `subject_matter` first, through `armyrecord.apply('discharge', ...)` inside
  that act's effect, and the read then starts from the written value (no `army.dispersed` Event and no
  MATTER write). An army nobody plays or holds therefore melts over seasons, by chance, and not at once.
  Order of edits: the reader, then its callers, then the write-through in `_eff_create_record`'s army
  branch and `loop/effects_army.py`'s effects. Hash: moves every reader of an unheld army's strength
  (none at `armies_at_build: off`).

**Edit 7 — fixtures** (`data/fixtures.py`).

- `armies_at_build: "off"` (shipped) | `"empty"` (each faction's first `may_wage` leader mints an
  empty army through the fold at build, `harness/populated.py`) | `"mustered"` (today's
  `army_presets.install`, kept as a world-gen arm and no longer the unplayed commander's only path).
- `withheld_verbs` drops `recruit` and `discharge_troops` in this batch and the other four in M-D.
  With `armies_at_build: off` no one holds an army, so nothing forms.

## 4. Gate and falsifier

- **Execution artifact.** `aperture 2 s`, s = 0 to 2, `armies_at_build: empty`: `army.recruited`
  emitted by an act that passed through DELIBERATE (the act store names a chooser round, not a
  hand-built id), at every seed; `recruit`'s refusals on `room` are not repeated by the same actor
  the next season. A hand-built run on `build_realm(0)`, 200 seeds of the draw, one levy of 60: all
  four bands occur; the counts on the roll are 60, 60, 30, 0 by band.
- **State sets the odds.** The same levy by a seat whose cohort holds a negative stance row toward
  the faction, against the same seat with none, n 200 each, same-run control: the share of
  `levy.shirked` is higher for the first beyond sampling error. A reading of mechanism, not balance.
- **The successor.** The probe's death sequence re-run: after the commander's death the next
  `may_wage` leader's mint emits `record.taken_up`, `army_of` returns the old id, and the cohort's
  room is 60 less the troops still on the roll (20 in the probe), not 0 and not 60.
- **Dispersal.** A leaderless army of 600 over 8 seasons at 50 seeds: `present_strength` at the end
  takes more than two values across seeds, and is 600 at some seed and below 600 at another; the
  Record's written `subject_matter` is unchanged until an act touches it. Falsifier (C3-L11): the read
  twice at one tick returns one value; a planted act after the read writes the share, and the next read
  adds nothing new.
- **Downstream read.** `seam/wrappers/mass_battle.py::_order_of_battle` returns an order of battle
  for a faction whose army an NPC raised and (proposal D) organised.
- **Control.** `armies_at_build: off`: hashes EQUAL to the base but for Edit 3's declared mover.
  `task_fraction` at its control arm (`1 / 1 / 1 / 0`) with the `draw` clause never firing (the rows
  out of `graded_tasks`): every levy raises its whole count (today's certainty).
- **Falsifier (planted).** `share` ignored in `_apply`: Partial raises 60. The `muster_room`
  Observation dropped: the same commander is refused on `room` in consecutive seasons.
  `may_levy` replaced by `raisable_by`: FA's seatless-member probe executes again.

## 5. What it does not do

It does not decide who goes to war or where (`march`'s formation on a defended enemy place is
PHYSICAL's and CHAR's). It writes no stores and no `weight` (J-C-2 stands; the cost is SE's three
arms). It does not add troop experience or upkeep (MB R-42). It does not lift the realm's
levy-only condition (SE's `training_endowment`).

## 6. NERS reading (E last)

- **N.** From above: armies exist because persons raised them. From below: a cohort is asked and
  answers. Laterally: `requisition`'s authority and the inquiry's roller. Diagonally: a field's
  grudge rows make the next levy harder, so a war has a memory. Remove it and force is a constant.
- **R.** Whom to call, how hard, and when to stand down are choices with a loser; a commander's
  `command` and his people's regard change what he fields; with no player, armies rise, shirk,
  balk and melt. Complete at the extremes: no seat, no levy; no commander, a slow dispersal.
- **S.** One state function for the menu and the cell; one cap; one journey of a trooper (raise,
  assign, release, discharge); the draw is the route every graded act uses.
- **E, against that.** Two record keys, two module functions, two readers (`army_state`,
  `present_strength`), two stems, one class column, one mint branch. "Call the levy; a loved lord gets his men" is a
  sentence a player can use.

## 7. Cost class

Small build across three owners (MB module, FA gate, the season rows). One declared mover at the
shipped fixtures (Edit 3); the rest move only under `armies_at_build`.
