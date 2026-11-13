# Workplan v12 — batches B22-mb-armies (from B22.24) and B26-fi-inquiry

## Status: PROPOSED (a body part of workplan v12, continuing the file before it in reading order; ratified only when Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05)

## Written against: working tree HEAD `8ce8d6a` (2026-11-12). Producer: author lane A33. Short names, words and paths as the file before it: `proposals/<file>` is under `proposals/2026-11-12-subsystem-audit-suite/proposals/`; "lap" is the season's pass, "round" a fight's (A-101).

---

## Batch B22-mb-armies (continued from B22.23; its block head and position table are in the file before this one)

### B22.24 — the unit row gains `raw`; the module steps the four organising ops by band · `14_VERBS_MILITARY_D` Edit 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md` §3 Edit 1; the 27-lane and 26-lane folds (A-59, A-69; `raw` is read by the field's obedience draw as the `unsteady` step, `26_MASS_BATTLE_maneuver_orders.md` §1); `04` §C.5 (one ladder).
- ADVANCES: none of its own (the module half of the order of battle).
- INSTRUCTION (`modules/mass_battle/armyrecord.py`; owner MB):
  1. The unit row gains `raw: bool` (default `False`; `validate` accepts its absence). `to_order_of_battle` passes it to `orderofbattle.UnitRow` (the source's `Subformation`, renamed by B16L), which lowers the built unit's Discipline by one, floor 1. `[ASSUMPTION; medium; Jordan to correct; revert: the field unread.]` One number, `raw_discipline_step` = 1: in the troop table (`references/troops.yaml`, landed by B17) — the source says "in the troop table when it lands …, in `config.py` until then"; the troop table is in the tree after B17, so it goes there.
  2. `options(q)` gains three booleans beside B22.18's two: `unformed` (trained troops of a kind with no unit and a free slot), `understrength` (the existing `unit_routs` test), `off_doctrine` (a unit whose role, posture, target or fall-back differs from its doctrine row's, or `facts.footing_wanted != record['footing']`). `unassigned` is the existing advisory.
  3. `step(record, op, facts)` for the four ops. `form`: one unit per kind in `trained` that has none, named `<kind>-<n>`, role from the doctrine (`presets.ROLE_OF` today). `assign`: every trained trooper into the units of its kind, filling the weakest first. `disband`: every unit under `UNIT_ROUT_FLOOR`. `order`: for each unit, the fields that differ from the doctrine row's; and `footing` set to `facts.footing_wanted`.
  4. `_apply` honours `args['band']` for the four. No module-exported `BANDS` tuple: the host passes the ladder's own value, a member of `engine/dice_engine/dice_engine.py::Degree`, which the module may import (the dice engine is a leaf a provider may read, D-U1-08), and compares to its members:
     | op | Overwhelming | Success | Partial | (Failure never reaches the module) |
     |---|---|---|---|---|
     | `form` | formed, `raw: False` | formed, `raw: False` | formed, `raw: True` | |
     | `assign` | all move; the body's `raw` cleared | all move | half move (rounded up); a body whose strength more than doubles turns `raw` | |
     | `disband` | removed; all to the pool | removed; all to the pool | removed; half to the pool, half discharged | |
     | `order` | set; `raw` cleared | set | `role` and `posture` set, the other fields left | |
  5. `order` accepts `footing` alone and `doctrine` alone, as it accepts `strategy` alone. MB's `standing_orders` ride the same op when that proposal lands; nothing here anticipates their shape.
- WHERE: `modules/mass_battle/armyrecord.py` (the unit row; `validate`; `to_order_of_battle`; `options`; `step`; `_apply`); `modules/mass_battle/orderofbattle.py` (`UnitRow`: the Discipline step); `references/troops.yaml` (`raw_discipline_step`); `engine/engine_params/troops.json` (re-exported).
- TESTS: in `tests/valoria/test_mass_battle_army_record.py`, written first and read red: `test_each_op_writes_the_record_its_band_names` (the table above, one case per cell); `test_a_raw_unit_is_built_one_discipline_lower_floor_one`.
- FALSIFIER and CONTROL: planted, `raw` not passed to `UnitRow` (read at B22.26's downstream gate); the `band` argument ignored: two record outcomes, not three. Control: realm hash at seeds 0 to 2 equal (no caller).
- GATE: `python -m pytest tests/valoria/test_mass_battle_army_record.py tests/valoria/test_mass_battle_order_of_battle.py -q` → green; `python tools/export_troops.py --check` → exit 0.
- HASH MOVERS: none.
- DEPENDS ON: V12 B22.23, B22.18 (`step`, the keys); V12 Batch B17 (`04_MB_headcount_grade_and_scale`; `references/troops.yaml`); EXISTS-IN-TREE `engine/dice_engine/dice_engine.py::Degree`, `modules/mass_battle/troop_types/presets.py::ROLE_OF`.
- GLOSSARY: row *raw* (new): "a unit newly formed or swollen past its drill, one step less steady"; owner the unit row's `raw` column.
- NAMES: `orderofbattle.Subformation` → `UnitRow`; `subformation_routs` → `unit_routs`; the order payload key `stance` → `posture` (B16L, L1-2, L1-1, L1-4); `SUBUNIT_ROUT_FLOOR` → `UNIT_ROUT_FLOOR` (B16M, L2-1).
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B22's producer, `isolation: worktree`; `Item: B22.24`, `[skip ci]`.

### B22.25 — four stems answered by the army's state · `14_VERBS_MILITARY_D` Edit 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md` §3 Edit 2.
- ADVANCES: none of its own.
- INSTRUCTION: `engine/season/data/requires.py`: `unformed`, `unassigned`, `understrength`, `off_doctrine`, relation stems of `subject` and the actor, answered by `world_q.army_state` (B22.19); none world-only. `footing_wanted` is `war` when `world_q.at_war` holds for the army's faction against any faction, else `peace`; with FA's `06_FA_war_lives_in_seats_B.md` that is a seat's word. The stems are asked at formation (`belief_contradicts`) and in the effect for a payload-less act, never as a typed conjunct (G-04; the source's "the `need` conjunct binds a doctrine step only").
- WHERE: `engine/season/data/requires.py` (`REQUIRES_STEMS`); `engine/season/queries/world_q.py` (`army_state` reports `footing_wanted`).
- TESTS: in NEW `engine/season/tests/test_vm_mil_d_order_of_battle.py` (one function per §4 gate), written first: `test_the_four_stems_read_army_state`; red before.
- FALSIFIER and CONTROL: planted, `off_doctrine` always true: a commander orders the same body every season (read at B22.26). Control: hashes equal.
- GATE: `python -m pytest engine/season/tests/test_vm_mil_d_order_of_battle.py -q` → green.
- HASH MOVERS: none.
- DEPENDS ON: V12 B22.24, B22.19; EXISTS-IN-TREE `engine/season/queries/world_q.py::at_war` `[ASSUMPTION: present — cited by the source]`; V12 `06_FA_war_lives_in_seats_B` edits 1–3 (Batch B21).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.25`, `[skip ci]`.

### B22.26 — `form_unit`, `assign_troops`, `disband_unit`, `order_unit` are task rows on `command` · `14_VERBS_MILITARY_D` Edits 3, 4, 5 · BUILD · HASH EQUAL
- SOURCE: `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md` §3 Edits 3, 4, 5; §4; "Standing" (A-5, A-6, A-7, A-8, A-25, A-30, A-59, A-81); D-36 (three organising verbs); G-04; the A-69/A-78 fold (`assign_troops` on a unit with fled men is the recall, B22.05).
- ADVANCES: R-05 (`form_unit`, `assign_troops`, `disband_unit`, `order_unit` built out, read at the batch gate after B22.33); `ENGINES`: `mass_battle.army`, `mass_battle.army_order`. One commit `[ASSUMPTION: the grouping — basis: as B22.21]`.
- INSTRUCTION:
  1. Edit 3 — `engine/season/verb_table.yaml`. Each row keeps its stratum, beneficiary and first two conjuncts, takes `recruit`'s class column and eligibility `["own"]` unchanged, and changes as follows (shape (a), flat columns; the `need` read is not a typed conjunct):
     ```yaml
       - verb:        "form_unit"
         referent_class: Record
         capability:  command
         difficulty:  routine
         requires_typed:
           all:
             - {form: existence, of: subject, kind: army, conjunct: army}
             - {form: relation,  of: subject, relation: held_by,  conjunct: command}
         writes: ["Record.subject_matter"]
         emits:  ["army.formed"]
         emits_on_refusal: {army: ["form_unit.refused"], command: ["form_unit.refused"], write: ["form_unit.refused"], draw: ["unit.unformed"]}

       - verb:        "assign_troops"
         referent_class: Record
         capability:  command
         difficulty:  routine
         requires_typed:
           all:
             - {form: existence, of: subject, kind: army, conjunct: army}
             - {form: relation,  of: subject, relation: held_by,    conjunct: command}
         writes: ["Record.subject_matter"]
         emits:  ["army.assigned"]
         emits_on_refusal: {army: ["assign_troops.refused"], command: ["assign_troops.refused"], write: ["assign_troops.refused"], draw: ["assign.balked"]}

       - verb:        "disband_unit"
         referent_class: Record
         capability:  command
         difficulty:  routine
         requires_typed:
           all:
             - {form: existence, of: subject, kind: army, conjunct: army}
             - {form: relation,  of: subject, relation: held_by,       conjunct: command}
         writes: ["Record.subject_matter"]
         emits:  ["army.disbanded"]          # a Partial's half sent home rides the Event as Observation `discharged` (a count)
         emits_on_refusal: {army: ["disband_unit.refused"], command: ["disband_unit.refused"], write: ["disband_unit.refused"], draw: ["unit.balked"]}

       - verb:        "order_unit"
         referent_class: Record
         capability:  command
         difficulty:  routine
         requires_typed:
           all:
             - {form: existence, of: subject, kind: army, conjunct: army}
             - {form: relation,  of: subject, relation: held_by,      conjunct: command}
         writes: ["Record.subject_matter"]
         emits:  ["army.ordered"]
         emits_on_refusal: {army: ["order_unit.refused"], command: ["order_unit.refused"], write: ["order_unit.refused"], draw: ["order.unheeded"]}
     ```
     The band still reaches the module as `args['band']` (B22.24's table): one cell, different contents, so shape (a). The `need` stems (B22.25) are asked at formation and in the effect for a payload-less act, refused under `write`.
  2. Edit 4 — `engine/season/rosters.yaml`: `graded_tasks.values` gains the four; the skill is each row's `capability: command` cell (D-U1-07), not a `verb_capability` line. Obstacle and leverage through the one composer (every number `[ASSUMPTION; medium; Jordan to correct]`):
     | verb | difficulty | obstacle terms | leverage (A-25; C3-C10) |
     |---|---|---|---|
     | `form_unit` | `routine` | `drill_difficulty` (by troop kind, troop table; until it lands, `recruit`'s stand-in) · `no_training_place` (no Site of the kind's training kind where the commander stands) | — |
     | `assign_troops` | `routine` | `influx_exceeds_body` · `body_raw` | — |
     | `disband_unit` | `routine` | `body_experienced` (a step, MB R-42's `experience`, 0 until it lands) · `arrears` | — |
     | `order_unit` | `routine` | `many_fields` (more than two fields change) · `body_raw` · `undisciplined` (Discipline 1) | `disciplined` (the kind's Discipline 4 or more) |
     Every term and the level ship absent until B22.01's design names them: the control is `routine`.
  3. Edit 5 — `engine/season/loop/effects_army.py`: `_apply(w, a, op, args, kind, res)` gains `res`; it is reached only on a won draw; it passes `args['band']` (the ladder's `Degree`) and, for a payload-less act, `facts` from `army_state`. Every Event carries the four state Observations (`unformed`, `unassigned`, `understrength`, `off_doctrine`) after the write.
  4. Draws: `H(w.world_seed, w.tick, <actor id>, "<verb>.task")` for the four rows (A-30). A-81: each failed draw is a refusal Event witnessed by the commander and the officers of the body named.
- WHERE: `engine/season/verb_table.yaml` (`form_unit`, `assign_troops`, `disband_unit`, `order_unit`); `engine/season/rosters.yaml` (`graded_tasks.values`; composer rows; `observation_terms`: `discharged` and the four state terms if absent); `engine/season/loop/effects_army.py` (`_apply`).
- TESTS: in `test_vm_mil_d_order_of_battle.py`, written first and read red: `test_each_of_the_four_has_four_bands` (one hand-built act of each on `build_realm(0)`, 200 seeds: all four bands occur for each; the record after each band is B22.24's table: a Partial `form` is `raw: True`; a Partial `disband` leaves the pool half the body's men; a Partial `order` changes `role` and `posture` only); `test_a_better_commander_makes_more_steady_bodies` (two commanders, `command` 5 and none, equal cohorts and doctrine, two seasons, 50 seeds — "three seasons in the source; A-114": the count of steady bodies with troops differs beyond sampling error); `test_a_raw_army_wins_less_often_and_not_never` (a field between two equal armies, one all `raw`, n 200 through `massbattle.resolve_field`: the raw army's win share is lower, and not 0).
- FALSIFIER and CONTROL: planted, `raw` not passed to `UnitRow`: the downstream test reads equal shares; `off_doctrine` always true: the act store shows a repeat with no change of record; the `band` argument ignored: two record outcomes, not three. Control: the four rows out of `graded_tasks` (no draw): each act is certain; `armies_at_build: off`: hashes EQUAL.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mil_d_order_of_battle.py tests/valoria/test_army_verbs.py -q` → green; the downstream field test read once by `opus` ("If it is 0 or equal, the `raw` step is mis-sized or unread"). The source's `aperture 3 s`, s = 0 to 2, `armies_at_build: empty` arm is read at two seasons ("three seasons in the source; A-114") after B22.27: all six `army.*` kinds leave the never-emitted list; at least one faction's army holds a unit with troops assigned by acts that passed through DELIBERATE; `_order_of_battle` returns an order of battle for it — moved to B22.27's GATE.
- HASH MOVERS: none at `armies_at_build: off`.
- DEPENDS ON: V12 B22.25; V12 Batch B07 (`graded_tasks`, the loader); V12 Batch B19 (`27_MB_A` §1, §3: `command`, the obedience draw), Batch B20 (`26_MASS_BATTLE_maneuver_orders`); EXISTS-IN-TREE `engine/season/loop/effects_army.py::_apply` `[ASSUMPTION: present — cited by the source's Edit 5]`. Cut edge (U3 §4.1 row 80, LATER): `27_MB_B_unit_prowess_on_the_row` (B31) ships with no behaviour at its control arm; the order of battle reads it when it lands.
- GLOSSARY: none new (*unit*, *order of battle* are MB lexicon D-2, D-14's).
- NAMES: as B22.24.
- COST and TIER: small build; `sonnet`, high; one `opus` read of the downstream field gate (the `raw` step's size is the judgment).
- LANDS IT: B22's producer; `Item: B22.26`, `[skip ci]`.

### B22.27 — the four leave the withheld list; the preset arm says what it draws · `14_VERBS_MILITARY_D` Edits 6, 7 · BUILD · HASH EQUAL
- SOURCE: `proposals/14_VERBS_MILITARY_D_the_order_of_battle.md` §3 Edits 6, 7; §4 execution artifact.
- ADVANCES: R-05 (with B22.33, the four verbs can form in the realm).
- INSTRUCTION:
  1. Edit 6 — `data/fixtures.py`: `withheld_verbs` drops `form_unit`, `assign_troops`, `disband_unit`, `order_unit`. `rosters.yaml: army_verbs`' note loses its "no person forms one" sentence.
  2. Edit 7 — `harness/army_presets.py::install` stays as the `armies_at_build: mustered` arm. Its docstring's "the plan is deterministic: it draws nothing" becomes false of the result (its folds now draw) and stays true of the plan; it says so.
- WHERE: `engine/season/data/fixtures.py` (`withheld_verbs`); `engine/season/rosters.yaml` (`army_verbs` note); `engine/season/harness/army_presets.py` (`install`'s docstring).
- TESTS: none new.
- FALSIFIER and CONTROL: a person forming an army verb at `armies_at_build: off`. Control: `off`: hashes EQUAL.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mil_d_order_of_battle.py -q` → green; the source's arm moved here, at two seasons: `aperture 2 s`, s = 0 to 2, `armies_at_build: empty` → all six `army.*` kinds leave the never-emitted list; at least one faction's army holds a unit with troops assigned by acts that passed through DELIBERATE; `seam/wrappers/mass_battle.py::_order_of_battle` returns an order of battle for it (`test_an_npc_raised_army_has_an_order_of_battle` in `test_vm_mil_d_order_of_battle.py`, written in this item; it is also `14_VERBS_MILITARY_C`'s downstream read). The arm "with PHYSICAL's `march` formation landed: one `field.won`, `field.lost` or `field.drawn` fought from such an army" is read at the batch gate (B22.R1).
- HASH MOVERS: none at `off`.
- DEPENDS ON: V12 B22.26; EXISTS-IN-TREE `engine/season/harness/army_presets.py::install`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B22's producer; `Item: B22.27`, `[skip ci]`.

### B22.28 — `occupying_faction` moves to its query owner · `14_VERBS_PHYSICAL_B` B2 (first row) · BUILD · HASH EQUAL
- SOURCE: `proposals/14_VERBS_PHYSICAL_B_field_and_ruin.md` B2 table row 1; "Order of landing" ("B2's move of `occupying_faction` first (no behaviour)").
- ADVANCES: none (a move; the licence owner B22.30 composes on).
- INSTRUCTION: `loop/effects_shared.py::occupying_faction` → `queries/world_q.py`: move `occupying_faction` verbatim. `effects_shared` imports and re-exports it (`_seize_rung` unchanged).
- WHERE: `engine/season/loop/effects_shared.py` (`occupying_faction`, removed; an import and re-export); `engine/season/queries/world_q.py` (`occupying_faction`).
- TESTS: none new; the covering files `engine/season/tests/test_in12_raze.py` and those `python tools/tests_for_diff.py` names stay green.
- FALSIFIER and CONTROL: any seeded hash moving. Control: realm, spine and corpus hashes at seeds 0 to 2 equal.
- GATE: `python -m pytest engine/season/tests/test_in12_raze.py -q` → green; `git grep -n "def occupying_faction" engine/season` → one line, in `queries/world_q.py`.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `engine/season/loop/effects_shared.py::occupying_faction` (`:149`), `engine/season/loop/effects_information.py::_seize_rung` (its caller; not in `effects_shared.py`), `engine/season/loop/effects_founding.py::_eff_raze` (the other caller).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B22's producer; `Item: B22.28`, `[skip ci]`.

### B22.29 — `march` forms only on a `Field`; one owner says who defends · `14_VERBS_PHYSICAL_B` B1 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_PHYSICAL_B_field_and_ruin.md` B1 (as rewritten by W3-4a: `field_defender` and `fields_in_reach` are `U5b_VERBS_military_physical_residue.md` §2 edits 1–3, carried in this table); "Order of landing"; Gate; Falsifier; `audits/14_VERBS_PHYSICAL.md` §5.7 (copied below); rulings A-58, A-74.
- ADVANCES: R-04, R-05 (`march` forms on places that can be fought for); declared: in every war-less world `march` stops forming (realm: 26 formations to 0).
- INSTRUCTION (one row per owner, as the source's table):
  1. `engine/season/queries/world_q.py`: add `field_defender(w, via, rung) -> Optional[str]`, **the one owner of who defends this ground against this seat**, with no war test: `None` unless `w.rungs[rung].kind in MARCH_TARGET_KINDS`; the holder faction when it is not the marcher's (`seat_faction(via)`) and no leave stands (`world_q.passage_granted`, U5d's decision 5; MISSING in the tree until B23, and read as "no leave" until then); when the holder is the marcher's own faction or has given leave, the faction mustered there that the marcher's faction is `at_war` with, if any (relief); else `None`. The title test reads the same predicate. Expose its first test as `is_field_kind(w, rung)`.
  2. Same file: add stamp term `fields_in_reach(w, p)`: Rungs among `p`'s ledger names (`ledger_names`, `places_named`' knowledge rule) for which some live `hold` of `p` on a seat granting `MUSTER_ACT` gets a non-`None` `field_defender`, **and** either a war `p` knows of puts the defender among his enemies (the knowledge test of `enemies_heard`, factored out into `_wars_known(w, p)` and shared by both) or (A-74) `p` holds a claim or grievance against the holder, once FA names the acts that count and gives them a reader (until then the second occasion reads nothing). Stamped under `Field`.
  3. `engine/season/rosters.yaml: referent_classes`: `values` gains `Field`; `occasion_only_classes` gains `Field`. Note: *"a Rung on which a seat of the asker may march (`world_q.fields_in_reach` over `field_defender`); occasion-only, so `places_named` never reaches `march`"*.
  4. `engine/season/data/verbs.py`: `FIELD_CLASS = "Field"` beside `DETAINEE_CLASS` and `ENEMY_CLASS`. `RUNG_REMIT_ACTS` loses `dispatch` (derived; `march` no longer declares `Rung`). That reverses REM-27's derived widening of `larders_in_purview`, and it is declared.
  5. `engine/season/verb_table.yaml`, row `march`: `referent_class: Field`. `referent_class_note`: *"14_VERBS_PHYSICAL_B B1: FORMED ONLY ON A `Field` (`world_q.fields_in_reach`, over the same `field_defender` `sides_of` reads). A person forms it only against a faction he knows he is at war with (or, A-74, holds a named claim or grievance against); a played or hand-built march onto land another holds is opposed by the holder whether or not a war exists, and is itself the aggression (A-58; residue §2 edit 3). REM-27's measured `fields_named` was unearned because `places_named` stamped the same Rungs under `Rung`; an occasion-only class removes that route. [ASSUMPTION; medium; revert: `referent_class: Rung` and REM-27's note]."* `requires_typed` is unchanged.
  6. `engine/season/loop/sides.py::sides_of`, the `mass_battle` branch: `subject = field_defender(w, a.via, target)`. The army is mustered as today, and `claimants = []` when the target's kind is outside the roster, through `is_field_kind`. Delete the inline kind check and its disclosure comment, replaced by one line citing the owner.
  7. `engine/season/decision/options.py`: `march` forms one Candidate per `march_postures` value carrying `posture`, on `vocation_sourced`'s shape (`rosters.yaml: payload_sourced: {march: posture}` is a new roster line, read where `VOCATION_SOURCED` is). A withheld posture is not formed.
- WHERE: `engine/season/queries/world_q.py` (NEW `field_defender`, `is_field_kind`, `fields_in_reach`, `_wars_known`; `enemies_heard` factored); `engine/season/rosters.yaml` (`referent_classes`, `occasion_only_classes`, NEW `payload_sourced`); `engine/season/data/verbs.py` (`FIELD_CLASS`; `RUNG_REMIT_ACTS` derivation); `engine/season/verb_table.yaml` (`march`); `engine/season/loop/sides.py` (`sides_of`); `engine/season/decision/options.py` (the posture fan); NEW `engine/season/tests/test_v14_march_on_a_field.py`; NEW `engine/season/tests/test_vm_phy_b_field_ruin.py`; NEW `engine/season/tests/test_resv_field_defender.py`.
- TESTS: written before the edit and read red:
  - NEW `engine/season/tests/test_v14_march_on_a_field.py` (`audits/14_VERBS_PHYSICAL.md` §5.7, copied): `build_realm(0)` with one WAR Proposition planted through the real fold (an `utter` and a `commit` by two seats granting `dispatch`, one per faction, each told of it), one season through `SeasonDriver.season`. Pass: a seated holder of `dispatch` of one faction forms `march` only on settlements and territories the other faction holds and that his ledger names; at least one is attempted, and its Event is a field band (`field.won`, `field.lost`, `siege.pressed` or `Drawn`), not `march.refused` on kind. **Draw assertion:** the same planted pair, seeds 0–29, produces both `field.won` and `field.lost` (or `Drawn`) for the larger side (`assert checked >= 30`). **Control:** the same world without the war forms no `march`.
  - NEW `engine/season/tests/test_resv_field_defender.py` (`U5b_VERBS_military_physical_residue` §2's gate, the parts that need no `passage_granted`): the same world **without** the war and with one hand-built `march` on the neighbour's defended settlement: the Event is a field band and not `field.unopposed`. (The covenant arm — "a hand-built march onto a rung whose holder has a live covenant with the marcher's seat arrives with no field" — needs `passage_granted` and is read in B23.)
  - NEW `engine/season/tests/test_vm_phy_b_field_ruin.py` ("one function per gate"): `test_march_formations_fall_to_zero_in_the_warless_realm` (`aperture 2 0` before and after: `march` formed 26 → 0; every remaining refusal reason named).
- FALSIFIER and CONTROL: planted, restore `referent_class: Rung`: formations on hearths and own places return, and `test_v14_march_on_a_field.py` fails on the formed set; a field that holds one verdict for one pair over 30 seeds means the field is still deterministic; a march on a defended neighbour folding `Unopposed`. Control: the war-less world forms no `march`.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_v14_march_on_a_field.py engine/season/tests/test_resv_field_defender.py engine/season/tests/test_vm_phy_b_field_ruin.py -q` → green. MB's gate 2 (`04_MB_headcount_grade_and_scale`, B17: a field verdict varies by seed) is green before the war-world draw assertion is quoted as a field.
- HASH MOVERS: every realm pin with a `march` formation (all of them at seed 0); `larders_in_purview`'s narrowing (declared; B22's one re-pin).
- DEPENDS ON: V12 B22.28; V12 CR-91's carrier (Batch B21b: a WAR Proposition, as occasion, A-103; B1's formation half "may land before CR-91 as a declared honest zero"); V12 `06_FA_remit_grant_by_row` (Batch B21); V12 `04_MB_headcount_grade_and_scale` (Batch B17: gate 2); V12 `U5b_VERBS_military_physical_residue` §1, `18_DETERMINISM_task_draw_for_uncontested_verbs` items 2, 4 (Batch B07); EXISTS-IN-TREE `engine/season/loop/sides.py::sides_of`, `engine/season/data/verbs.py::DETAINEE_CLASS`, `::ENEMY_CLASS`, `::RUNG_REMIT_ACTS`, `engine/season/queries/world_q.py::places_named`; MISSING `world_q.passage_granted` (owner: `U5d_FA_land_and_seats_pass_on_a_won_march` decision 5, Batch B23; read as "no leave" until then, as the source states).
- GLOSSARY: row *field* (MB lexicon D-18) gains the referent class `Field`: "a place a seat of the asker may march on and someone would defend"; owner `world_q.fields_in_reach`.
- NAMES: `VOCATION_SOURCED` → as B04 left it (see B22.13).
- COST and TIER: build; `sonnet`, high; one `opus` read of the field-verdict gate.
- LANDS IT: B22's producer; `Item: B22.29`, `[skip ci]`.

### B22.30 — `raze` forms only on a town its seat may ruin · `14_VERBS_PHYSICAL_B` B2 (the class) · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_PHYSICAL_B_field_and_ruin.md` B2 table row 2 (`towns_occupied`, `Occupied`) and the `raze` row's `referent_class`; `U5b_VERBS_military_physical_residue.md` §3 (`may_ruin`, its docstring, A-73); "Order of landing" ("then B2's class").
- ADVANCES: R-05 (`raze` forms only where it can be done).
- INSTRUCTION:
  1. `engine/season/queries/world_q.py`, the licence at its one owner, beside the moved `occupying_faction`:
     ```python
     def may_ruin(w, via, rid) -> bool:
         """The licence `raze` asks, for formation (`towns_occupied`) and for the effect, one owner: the
         seat's faction is mustered at `rid` AND EITHER it occupies it (`occupying_faction`) OR it holds it
         (`holder_faction_of(w, rid)` is the seat's faction) by a hold whose opening Event is a `rung.seized`
         caused by an act of a seat of that faction (A-73: "what he took, while it is in his hand"), read
         through `state/attribution.py::causing_act`. Resolver-side only: the stamp `towns_occupied` is
         computed in `queries/world_q.py`, never in `decision/` (`04` §B.9)."""
     ```
     Once he confers the place onward, or it passes from him, the holder arm closes for him.
  2. Same file: stamp term `towns_occupied(w, p)`: `RAZE_TARGET_KINDS` Rungs for which some seat `s` of `p` granting `MUSTER_ACT` has `may_ruin(w, s, rid)` true. Stamped under the new occasion-only class `Occupied` (`rosters.yaml: referent_classes` and `occasion_only_classes`, and `data/verbs.py` `OCCUPIED_CLASS = "Occupied"`, as for `Field`).
  3. `verb_table.yaml`, row `raze`: `referent_class: Occupied` with a note. The effect asks the same `may_ruin` (one licence owner) from B22.31.
- WHERE: `engine/season/queries/world_q.py` (NEW `may_ruin`, `towns_occupied`); `engine/season/rosters.yaml` (`referent_classes`, `occasion_only_classes`); `engine/season/data/verbs.py` (`OCCUPIED_CLASS`); `engine/season/verb_table.yaml` (`raze`: `referent_class`, note).
- TESTS: in `engine/season/tests/test_vm_phy_b_field_ruin.py`, written first: `test_raze_formations_fall_to_zero_in_the_warless_realm` (`aperture 2 0` before and after: `raze` formed 26 → 0); in `test_resv_field_defender.py`: `test_raze_does_not_form_on_an_inherited_town` (residue §3's falsifier: a hold not opened by a seizure). The seizure arm's gate (after `seize`, the victor's opening set holds `raze` on the town he took) needs B23's `seize_place`: read in B23.
- FALSIFIER and CONTROL: planted, drop `referent_class: Occupied`: `raze` forms on unoccupied places again. Control: the holder arm removed: after a seizure, `raze` does not form (today's reading).
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_phy_b_field_ruin.py engine/season/tests/test_resv_field_defender.py -q` → green.
- HASH MOVERS: every realm pin with a `raze` formation (all at seed 0; declared; B22's one re-pin).
- DEPENDS ON: V12 B22.29, B22.28; EXISTS-IN-TREE `engine/season/queries/world_q.py::holder_faction_of`, `engine/season/state/attribution.py::causing_act` `[ASSUMPTION: present — cited by the residue]`.
- GLOSSARY: none (the class name `Occupied` is a code name; prose says "a town his seat occupies or took").
- COST and TIER: small build; `opus` producer for `may_ruin` (the residue's tier: "§2 and §3 `opus` producer for `field_defender` and `may_ruin`"), `sonnet` for the rest.
- LANDS IT: B22's producer; `Item: B22.30`, `[skip ci]`.

### B22.31 — `raze` is one draw over four bands · `14_VERBS_PHYSICAL_B` B2 (the grading) · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_PHYSICAL_B_field_and_ruin.md` B2 rows 3–7; `audits/14_VERBS_PHYSICAL.md` §6.7 (copied below); `U5b_VERBS_military_physical_residue` §1 (shape (b)); rulings A-30, A-59, A-81; H-228.
- ADVANCES: R-05 (`raze` built out); R-09 (an outcome drawn).
- INSTRUCTION:
  1. `raze` is a contest row on the `a task` prize; the route roster keeps one name, `graded_tasks`. **Pool:** the one pool rule on the commander's `command` skill score (D-U1-08; A-59); the army's size against the town enters as named levels for the roller (a leverage source U1 names, shipped absent until B22.01's design names it). **Obstacle:** `difficulty: routine` plus the town's fabric as the OBS member `ruin` (member 27, reused). `obstacle_default` is not used.
  2. `verb_table.yaml`, row `raze`: `contests: "a task"`; `capability: command`; `difficulty: routine`. `writes:` degree-keyed: `Overwhelming` and `Success`: `["Rung.stores", "Rung.stores", "Site.exists", "Rung.exists"]`. `Partial`: `["Rung.stores", "Rung.stores", "Site.condition"]`. `Failure`: `[]`. `emits:` `Overwhelming`/`Success`: `["rung.razed", "site.razed"]`; `Partial`: `["site.damaged"]`; `Failure`: `["raze.resisted"]`. `emits_on_refusal: ["raze.refused"]`. `writes_note`: the cascade on `Rung.exists` is Layer 1 §B.8's, unchanged; `Site.exists` is the act's own declared write on Sites whose `rung` is the subject, not the cascade. `engine/season/write_matrix.yaml`, the `(Site, exists)` row's `emits:` cell (`site.built`) gains `site.razed` (`faction.surveyed`'s precedent).
  3. `loop/effects_founding.py::_eff_raze`: the licence is `may_ruin`. By band: move `raze_sack_share[band]` per mille of the Rung's `stores` to the exercised seat's rung (`_shift`, `requisition`'s two-sided shape). On Success and better, end each Site naming the Rung, then delete the Rung as today. On Partial, lower each Site's `condition` by `loop/effects_economy.py::_fall` (`sabotage`'s formula). `raze.resisted` is earned by the Rung on Failure (written nothing; `contest.undecided`'s shape).
  4. `data/fixtures.py`: `raze_sack_share: {Overwhelming: 1000, Success: 500, Partial: 250}` (per mille of the Rung's stores), swept, NUMBER row in `hole_register.yaml`, `[ASSUMPTION; medium]`.
  5. `data/verbs.py::KIND_VERB`: `raze.resisted` and `site.razed` map to `raze`. `site.damaged` already maps to `sabotage`; a second emitter makes it unmapped, which is lawful `[verify the map's rule at landing]` — the first INSTRUCTION step opens `KIND_VERB`'s rule and records it in the commit body.
  6. Draw: `H(w.world_seed, w.tick, <actor id>, "raze.task")` (A-30). A-81: `raze.resisted` is witnessed by the town's residents and the razing army's men present.
- WHERE: `engine/season/verb_table.yaml` (`raze`); `engine/season/write_matrix.yaml` (`(Site, exists)` `emits:`); `engine/season/loop/effects_founding.py` (`_eff_raze`); `engine/season/data/fixtures.py` (`raze_sack_share`); `engine/season/data/verbs.py` (`KIND_VERB`); `engine/season/rosters.yaml` (`graded_tasks` is not touched; the composer row for `raze`); `engine/season/hole_register.yaml` (one NUMBER row); NEW `engine/season/tests/test_v14_raze_after_occupation.py`.
- TESTS: NEW `engine/season/tests/test_v14_raze_after_occupation.py` (`audits/14_VERBS_PHYSICAL.md` §6.7, copied), written before the edit and read red: §5.7's war world with the march forced to `Won` by a fixture-planted army imbalance (MB presets). In the next season the victor's opening set holds `raze` on the occupied town **only**. If attempted at Success (fixture pool): `w.rungs` shrinks by one, every Site naming it is gone, and the seat's treasury `stores` rose by `raze_sack_share` of the town's prior `stores`. At Partial: the Rung stands and every Site's `condition` fell. At Failure: nothing moved, and `raze.resisted` is witnessed. **Draw assertion:** at the shipped pool, seeds 0–29 produce at least two different bands for the same occupation (`assert checked >= 30`). **Control:** with no occupation, the opening set holds no `raze`. `engine/season/tests/test_in12_raze.py`'s H-228 pin reddens on the Site half by design; it is re-pinned in B22's one re-pin (B22.35) — the source re-records it "in the same commit"; the plan's rule is one re-pin per batch (structure §5.9), so this item's covering run expects that one assertion red until B22.35.
- FALSIFIER and CONTROL: planted, drop `referent_class: Occupied` (B22.30): the test fails on the formed set. Control: no occupation, no `raze`.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_v14_raze_after_occupation.py engine/season/tests/test_vm_phy_b_field_ruin.py -q` → green; `test_in12_raze.py` → the H-228 pin red, the rest green. The raze-band gate read once by `opus`.
- HASH MOVERS: every realm pin with a `raze` attempt; `test_in12_raze.py`'s H-228 pin (declared; B22's one re-pin).
- EXPECTED RED UNTIL B22.35: `engine/season/tests/test_in12_raze.py`'s H-228 pin (the GATE above), under `[skip ci]`.
- DEPENDS ON: V12 B22.30; V12 `U5b_VERBS_military_physical_residue` §1, `U5c_VERBS_residue_and_governance_owner` §1 (Batch B07); EXISTS-IN-TREE `engine/season/loop/effects_founding.py::_eff_raze` `[ASSUMPTION: present — cited]`, `engine/season/loop/effects_economy.py::_fall`, `engine/season/write_matrix.yaml` row `(Site, exists)` (`:418-424`, cited by the source).
- GLOSSARY: none.
- IDS: H block slot 2 (`raze_sack_share`'s NUMBER row).
- COST and TIER: build; `opus` for the contested row and its terms (the source's tier), `sonnet` for the rest; one `opus` read of the raze-band gate.
- LANDS IT: B22's producer; `Item: B22.31`, `[skip ci]`.

### B22.32 — armies at build, doctrines as data, `marshal` fans its fall-back point only · `04_MB_playable_field_scenario` §E · BUILD · HASH EQUAL
- SOURCE: `proposals/04_MB_playable_field_scenario.md` §E (as its head line item (2) and W3-1 rewrote it); gates 4, 5, 7; U3 §4.1 rows 69, 70 (SPLIT: §E lands in B22); H-361.
- ADVANCES: R-04 (armies exist and choose), with B22.33 and B22.34.
- INSTRUCTION (the parts of §E that move nothing at `armies_at_build: off`; the two flips are B22.33 and B22.34; the opportunity-key digest is B22.21's, made once there; training Sites are B22.17's):
  1. `engine/season/boot/realm.py` (the source's `harness/populated.py::build_realm`): after the cast is seated, `army_presets.install(w)` when `Fixtures armies_at_build` is `mustered`.
  2. `modules/mass_battle/troop_types/presets.py::ROLE_OF['levy']`: `'Hold'` in place of `'Reserve'`: a levy line stands as a line. (Whether to restrict levy to its home territory is a design call for FA and is not made here.)
  3. The doctrine becomes data: `ARM_SHARES` moves to `references/troops.yaml: doctrines` (the one troop file, exported to `engine/engine_params/troops.json`), keyed by a doctrine name (`balanced` = today's 45/25/20; at least `foot`, `horse`, `missile` beside it — authored values, listed in the PR body for Jordan). The commander's `create_record` act names the doctrine; which one a given leader picks is the chooser's, on cells CHAR owns. `plan(q)` reads `q.doctrine`.
  4. `harness/army_presets.py::install` stays a world-gen arm; an unplayed commander forms the army verbs through the one chooser (B22.21, B22.26).
  5. `marshal` fans `retreat_at` only (three candidates, not forty-five); the role key leaves the standing order (H-361).
- WHERE: `engine/season/boot/realm.py` (the `install` call); `modules/mass_battle/troop_types/presets.py` (`ROLE_OF`, `ARM_SHARES` removed, `plan`); `references/troops.yaml` (`doctrines`); `engine/engine_params/troops.json` (re-exported); `tools/export_troops.py` (the `doctrines` section, if its schema lists sections); `engine/season/rosters.yaml` and `engine/season/decision/options.py` (`marshal`'s fan: `retreat_at` only).
- TESTS: in `tests/valoria/test_army_menu_presets.py`, written first and read red: `test_two_doctrines_raise_two_armies` (gate 5: two leaders naming different doctrines raise different armies from equal means).
- FALSIFIER and CONTROL: two doctrines that raise the same army. Control: `armies_at_build: off`: hashes EQUAL; `python tools/export_troops.py --check` round-trips.
- GATE: `python -m pytest tests/valoria/test_army_menu_presets.py engine/season/tests/test_cp_t04_02_marshal.py -q` → green; `python tools/export_troops.py --check` → exit 0.
- HASH MOVERS: none at `off` (`marshal` is withheld until B22.34).
- DEPENDS ON: V12 B22.27, B22.23; V12 Batch B17 (`references/troops.yaml`, `tools/export_troops.py`); V12 Batch B20 (`04_MB_playable_field_scenario` §A–§D, G; `field_scene.py`); EXISTS-IN-TREE `modules/mass_battle/troop_types/presets.py::ROLE_OF`, `::ARM_SHARES` `[ASSUMPTION: present — cited]`, `engine/season/harness/army_presets.py::install`.
- GLOSSARY: row *doctrine* (B22.18) becomes a pointer to `references/troops.yaml: doctrines`.
- NAMES: `harness/populated.py::build_realm` → `boot/realm.py` (B03c); `stance` → `posture` in the standing order's payload (B16L, L1-4).
- COST and TIER: small build plus a data edit outside the lane; `sonnet`.
- LANDS IT: B22's producer; `Item: B22.32`, `[skip ci]`.

### B22.33 — armies are mustered at realm build · `04_MB_playable_field_scenario` §E (the `armies_at_build` flip) · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/04_MB_playable_field_scenario.md` §E ("shipped `off`; the flip is its own commit"); "Hash movers: the `armies_at_build` flip and the `withheld_verbs` flip, each its own commit with the aperture reading"; gate 4.
- ADVANCES: R-04, R-05 (a seeded realm raises armies by persons' own acts); `ENGINES`: `mass_battle.army`, `mass_battle.army_order`.
- INSTRUCTION: `data/fixtures.py`: `armies_at_build` `"off"` → `"mustered"` `[ASSUMPTION: the flip's value — basis: §E's bullet installs the presets "when `Fixtures armies_at_build` is `mustered`", and the head line maps this file's `army_presets: on` to `mustered`]`. The commit carries the aperture reading.
- WHERE: `engine/season/data/fixtures.py` (`armies_at_build`).
- TESTS: none new.
- FALSIFIER and CONTROL: a realm with presets on that still fights no field in two seasons at three seeds ("then the missing piece is the march candidate"). Control: `armies_at_build: off` (the previous item's hash).
- GATE: `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2 → `army.recruited`, `army.formed`, `army.assigned` out of the never-emitted list; quoted in the commit body with the before-reading (`reading @<B22.32's sha>`).
- HASH MOVERS: every seeded realm, spine and corpus pin (an army Record at build; declared; B22's one re-pin).
- DEPENDS ON: V12 B22.32.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B22's producer; `Item: B22.33`, `[skip ci]`.

### B22.34 — `marshal` and `surrender` leave the withheld list · `04_MB_playable_field_scenario` §E (the `withheld_verbs` flip) · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/04_MB_playable_field_scenario.md` §E ("`withheld_verbs` loses the army verbs, `marshal` and `surrender` (a declared mover, with the aperture reading in its commit)"); `data/fixtures.py`'s own note ("`marshal` (CP-T04-02, `H-361`) and `surrender` (CP-T04-07) ship withheld so the season is EQUAL at shipped, each flip a separate declared mover").
- ADVANCES: R-05 (`marshal`, `surrender` can form; `order.marshaled` emitted).
- INSTRUCTION: `data/fixtures.py`: `withheld_verbs` drops `marshal` and `surrender` (the six army verbs left it in B22.23 and B22.27). `[ASSUMPTION: one commit for both — basis: §E names one `withheld_verbs` flip; the fixture's note says "each flip a separate declared mover", read as separate from the `armies_at_build` flip]`.
- WHERE: `engine/season/data/fixtures.py` (`withheld_verbs`).
- TESTS: none new.
- FALSIFIER and CONTROL: `order.marshaled` still never emitted after the flip. Control: the previous item's hash.
- GATE: `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2 → `order.marshaled` out of the never-emitted list; quoted in the commit body with the before-reading.
- HASH MOVERS: every seeded realm in which `marshal` or `surrender` forms (declared; B22's one re-pin).
- DEPENDS ON: V12 B22.33.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`.
- LANDS IT: B22's producer; `Item: B22.34`, `[skip ci]`.

### B22.35 — a detained man musters nowhere; the batch's one re-pin · `U5b_VERBS_military_physical_residue` §4 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/U5b_VERBS_military_physical_residue.md` §4 (`audits/25_GROUNDING_ENGINE.md` G-32; C3-R3); ruling A-23; U3 §4.1 row 26 (§4 lands in B22 with `14_VERBS_PHYSICAL_B`).
- ADVANCES: R-04 (a captured commander is not fielded); A-23.
- INSTRUCTION:
  1. `engine/season/queries/world_q.py::mustered`: a member for whom `restrained(w, pid)` is true is not counted. One conjunct at the one owner. (The seat-side check is FA's.)
  2. `loop/sides.py` and `seam/wrappers/mass_battle.py::_order_of_battle` read `mustered` and need no edit; an army whose holder is detained is fielded as a headcount line.
  3. **The re-pin.** In this commit, re-record every pin B22's declared movers moved (B22.06–B22.09, B22.12, B22.13, B22.20, B22.29–B22.31, B22.33, B22.34, and this item): the realm, spine and corpus pins at seeds 0 to 2 and the field goldens a moved field reaches, and `engine/season/tests/test_in12_raze.py`'s H-228 pin; the commit says "re-pin" plainly and quotes the before-reading (`reading @<the previous close's sha>`) and the after-reading. The last `Item:` commit also writes the named conjuncts' `reading:` records in `engine/season/requirements.yaml` (`IS-A-12`; `status:` not edited).
- WHERE: `engine/season/queries/world_q.py` (`mustered`); the pin files the movers reach (`engine/season/tests/_realm_goldens.py` and the golden files it owns, B02's one golden owner); `engine/season/tests/test_in12_raze.py` (H-228 pin); `engine/season/requirements.yaml` (`reading:` records).
- TESTS: in `test_resv_field_defender.py`, written before step 1 and read red: `test_a_captured_commander_is_not_mustered` (a hand-built world with one captured commander: `mustered` at his rung excludes him and the field's sides are built without his weight). (Patched: P-04) The arm of `14_VERBS_PHYSICAL_A` A2's gate that reads a mustered prisoner, moved here by B29's UNDECIDED (3) (§5.8: "the proposal's gate fails until it lands", `audits/14_VERBS_PHYSICAL.md` §2.4): in `engine/season/tests/test_vm_phy_a_custody.py` (B14.27's file, B29's gate), `test_a_man_captured_and_detained_musters_nowhere` `[ASSUMPTION: test name; the item creates it, E-3]` — the `capture` scene of B29's planted world (`test_v14_capture_after_resisted_arrest`'s shape: the arrest forced to Failure, a scene fought to a yield, `detain` to the warrant's issuing seat) followed by `mustered` at the captive's rung: he is not counted; read red before step 1.
- FALSIFIER and CONTROL: a detained person's `body` scaled by a field he could not have stood in. Control: worlds with no detained member unchanged by step 1.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_resv_field_defender.py engine/season/tests/test_in12_raze.py -q` → green after the re-pin; the pinned-hash tests B02 owns → green on the re-pinned values; (Patched: P-04) `python -m pytest engine/season/tests/test_vm_phy_a_custody.py -k musters_nowhere -q` → pass.
- HASH MOVERS: fields in which a mustered member is detained (none in shipped play before B22.33); the re-pin covers the batch.
- DEPENDS ON: V12 B22.34; EXISTS-IN-TREE `engine/season/queries/world_q.py::mustered` (`:2132`), `::restrained` (`:1766`); (Patched: P-04) V12 Batch B29 (`capture`, `detain` to the issuing seat; `test_vm_phy_a_custody.py`).
- GLOSSARY: none.
- COST and TIER: edit and the re-pin; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.35`, `[skip ci]` (the batch's last `Item:` push is B22.99, which takes step 3, the re-pin, with the GATE's "green after the re-pin" arms and HASH MOVERS' re-pin clause; repair lane R1, E-1).

## Readings (B22)

Written by repair lane R1 (K8 F2: the three READING rows had no block; E-10). Each text is copied byte for byte from the source the row names, line breaks kept; read once on the closing tree at B22.99 and quoted in its commit body with its SHA.

Reading 1 (B22.R1, `IS-MB-05`; `master/instructions/IS_B1_PC_MB_DICE_part2.md`, item IS-MB-05, its INSTRUCTION and GATE bullets):

- **INSTRUCTION:** at the close of B17, B20, B22 and B23 the last commit body quotes `python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2: the `ENGINES` lines for `mass_battle.resolve_field`, `mass_battle.army`, `mass_battle.army_order`; the counts of `field.won`, `field.lost`, `field.drawn`, `field.unopposed`, `siege.pressed`; `attempted` and `executed` for `march`, `marshal`, `recruit`, `form_unit`, `assign_troops`, `order_unit`. Each reading names its SHA and is taken once.
- **GATE:** expected after B17: at seed 2 the battle the realm fights is `field.won`, `field.lost` or `field.drawn` and no longer the artefact of the shipped scale; after B22: fought battles above 0 at every seed and the two army rows above 0 (the scenario proposal's gate 4); after B23: at least one `seize` following a `field.won`.

Reading 2 (B22.R2, `17_CENSUS_C1A_02` W2; `proposals/17_CENSUS_C1A_02_wires_and_corrections.md` §W2, the two census rows of this batch and the closing gate; the `_siege` row is INCOMPLETE in its source, no carrier):

| census row | effect(s) | corpus reading | proposal that names the verb |
|---|---|---|---|
| `loop/effects_army.py:34 _army`, `:45 _payload` | `recruit`, `form_unit`, `assign_troops`, `disband_unit`, `discharge_troops`, `order_unit` | never attempted | `14_VERBS_MILITARY_C_the_muster.md`, `14_VERBS_MILITARY_D_the_order_of_battle.md` |
| `loop/effects_combat.py:686 _siege` | `march` | never attempted | `14_VERBS_MILITARY_A_movement.md` |

**The gate these rows close on.** `python -m engine.season.harness.corpus_run`: each verb above appears
under `VERBS THAT EXECUTED`. Today's line reads 23 of 67 executed, 13 only refused, 30 never attempted.
[v12: run as `python -m engine.season.harness.corpus_run --seasons 2`, two seasons a case, D-17; the case's own span, to `MAX_SEASONS`, is B99's; the line's figures are the source's reading, not a target.]

Reading 3 (B22.R3, `IS-A-09` (1) and (2); `master/instructions/IS_A_NINE_part2.md`, item IS-A-09, "What this item still adds"):

(1) `IS-MB-02`'s gate line `march` with posture `besiege`
formed and executed is read through `IS-A-06`'s `BUILT OUT` block at B22's close (`aperture 2 --seeds 0 1 2`), and
`field.invested` is read in `EMITTED KINDS`; (2) the `march` row's built-out reading counts a besiege that wears
nothing but leaves its claim (`IS-MB-02` step 4) as a clean execution, not a refusal.

### B22.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1; B22.35 step 3, moved · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2, E-10 (the Readings block above); B22's RE-PIN, REQUIREMENT and BATCH GATE lines; B22.35 INSTRUCTION step 3, moved here by repair lane R1 (part 2 §11 C-01; K8 F1, F2).
- ADVANCES: R-04.c1 and the batch's `BUILT OUT` and `ENGINES` rows (its REQUIREMENT line), read on this tree; their conjuncts' `reading:` records written here (`IS-A-12`); no `status:` edited; M3 and M4 readings as the REQUIREMENT line names them.
- INSTRUCTION: (1) **The re-pin**: B22.35 step 3 as written there (every pin B22's declared movers moved: the realm, spine and corpus pins at seeds 0 to 2, the field goldens a moved field reaches, and `engine/season/tests/test_in12_raze.py`'s H-228 pin; "re-pin" said plainly, before and after quoted). (2) Readings 1 to 3 (the block above, B22.R1 to B22.R3), each read once on this tree and quoted in this commit's body with its SHA. (3) Every BATCH GATE line, the `HASH READING` at `<s>` = 0, 1, 2 before (`reading @<sha>`) and after, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before and after, and the batch's measured wall time, into this commit's body; the conjuncts' `reading:` records.
- WHERE: the pin files the movers reach (`engine/season/tests/_realm_goldens.py` and the golden files it owns, B02's one golden owner); `engine/season/tests/test_in12_raze.py` (the H-228 pin); `engine/season/requirements.yaml` (`reading:` records).
- TESTS: none new; after step 1 the pinned-hash tests B02 owns and `test_in12_raze.py` read green on the re-pinned values.
- FALSIFIER and CONTROL: a pin that moved and that no B22 item declared (B22.04 to B22.35's HASH MOVERS lines; then the re-pin stops and the batch is `STOPPED`). Control: the close B22 rebased on (B21b's or B20's, whichever merged last, `reading @<sha>`).
- GATE: the BATCH GATE above, every line, read once on this commit's tree; `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_resv_field_defender.py engine/season/tests/test_in12_raze.py -q` → green after the re-pin.
- HASH MOVERS: the batch's one re-pin, here and nowhere else.
- DEPENDS ON: V12 B22.01 to B22.35; the Readings B22.R1 to B22.R3.
- GLOSSARY: none.
- COST and TIER: a re-pin and the readings; `sonnet`, high; the readings read by `opus`.
- LANDS IT: B22's producer; `Item: B22.99`, the batch's last `Item:` push (no `[skip ci]`: its push opens BATCH-CLOSE).

| STOP. Batch B22-mb-armies closes here |

---

## Batch B26-fi-inquiry · lane FI · wave W17 · step S17 · HASH MOVER, one re-pin

INVOCATION: /methodology-execute Batch B26-fi-inquiry
IN-FLIGHT ROW: registers/handoffs/HANDOFF_FI.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B10-character
GATE: Batch B11-fi-readers
GATE: Batch B12c-material-verbs-and-valley
GATE: Batch B24-sc-hearing
GATE: Batch B25-fi-questioning
HASH READING: `PYTHONHASHSEED=0 python -c "import sys; from engine.season.boot.realm import build_realm; from engine.season.harness.populated import run; s, k = int(sys.argv[1]), int(sys.argv[2]); w = build_realm(s); run(k, s, w=w); print(w.content_hash())" <s> <k>` → the realm content hash at seed `<s>` after `<k>` seasons: `<k>` = 1, one season, unless the gate names two (never more before B99, D-17); `<k>` = 0 reads the build hash; per item `<s>` = 0 (a mover's reading, E-2), at `.99` `<s>` = 0, 1, 2; each value quoted `reading @<sha>`, the tree it was read on (`workplan_v12.md` §3.B, "the hash reading").
REQUIREMENT: `BUILT OUT`: `destroy_record`, `examine`, `seize` (a Record) → each built out (IS-A §12.2 row B26). Milestone: M3 (every verb).
BATCH GATE (read once, on the closing tree; every seeded command under `PYTHONHASHSEED=0`; two seasons at most, A-114):
  1. `python -m engine.season.harness.register --check` → each check's violation count (R2, G6 and any other that reports) does not rise from the reading taken at the batch's opening (quote both, `reading @<sha>`); `python -m engine.season.harness.register --requirements` → nine lines, recorded.
  2. `python tools/m1_acceptance.py --summary` → its verdict line, recorded.
  3. the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names → green.
  4. `python -m engine.season.harness.aperture 2 --seeds 0 1 2` → the `BUILT OUT` line reads built out for `destroy_record`, `examine`, and `seize` on a Record (IS-A-08: a verb not built out is a failed gate); for `create_record`, `forge`, `survey`, `research`, `reconstruct`, `surveil` (rows this batch re-draws) the `BUILT OUT` line quoted; `interview`, `reconstruct`, `thread_read` attempted 0 where B26.06 withholds them.
  5. `python -m engine.season.harness.aperture 2 0` and `2 1` → `examine` attempted above 0; `surveil` refusals on `present_at` and `exists:Rung` at 0; a `finding.made` from `surveil` deposits at least one claim other than "a finding was made" where any deed happened at the place (`14_VERBS_PHYSICAL_C` gate).
  6. The close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the named conjuncts' readings with their tree, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`, B25's close or B22's merge, whichever is later in the step's merge order) and after, and the batch's measured wall time; the last `Item:` commit writes the conjuncts' `reading:` records; `status:` is not edited (`IS-A-12`).
RE-PIN: every seeded realm, spine and corpus pin, re-recorded once in B26.99 (the batch's last `Item:` commit; moved from B26.17 by repair lane R1, E-1), said plainly as a re-pin; the before-reading is the previous close's after-reading (`reading @<sha>`); in step S17 B26 merges after B22 and rebases on B22's re-pin (§7.4 of the structure).
EXPECTED RED UNTIL B26.99 (under `[skip ci]`, E-1; one batch line, repair lane R1): the realm and corpus pins any mover item of this batch moves read red from its first mover (B26.01) to the re-pin; the files that pin them (`git grep -lE '"[0-9a-f]{32}"'` over the test trees and the golden files, those this batch names): `engine/season/tests/_realm_goldens.py` (B02's one pin file); `engine/season/tests/test_go07_canonical_digest.py` (its asserting test, `SHIPPED`/`CENSUS`).
IDS: ED-FI 0; H 2 (the NUMBER rows of B26.09 `forgery_quality_step` and B26.15 `surveil_watch_rate`; H-169's existing row is narrowed by B26.17, no new id)
DIALS AT CONTROL:
  - `data/fixtures.py: withheld_verbs` gains `thread_read` (and `interview`, `reconstruct` only if B26.06's check finds their products unlanded); set by: each row's product item, "in the same change that gives the row a graded band with a write" (`thread_read`: `14_VERBS_PHYSICAL_D` stage 2, B35); target: none stated (A-81's rule, not a reading).
  - `data/fixtures.py: press_level` ships `minor` (its control `None`; swept `None` / `minor` / `moderate`): not at control; listed for B98's table only as a swept value.
C(B26-fi-inquiry): this batch's entries; the plan's head parts; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_FI.md`, the skill, `methodology-close`);
  edited: `engine/season/verb_table.yaml`, `engine/season/rosters.yaml`, `engine/season/data/fixtures.py`, `engine/season/data/verbs.py`, `engine/season/data/rosters.py`, `engine/season/seam/wrappers/sigma.py`, `engine/season/loop/witness.py`, `engine/season/loop/resolve.py`,
  `engine/season/loop/effects_information.py`, `engine/season/queries/person_q.py`, `engine/season/queries/world_q.py`, `engine/season/decision/options.py`, `engine/season/epistemic.py`, `engine/season/hole_register.yaml`, `unified/U1_GLOSSARY.md`;
  tests: NEW `engine/season/tests/test_questioning.py`, `test_doubted_paper.py`, `test_withheld_inquiry_rows.py`, `test_vm_mat_d_paper.py`, `test_vm_mat_e_knowledge.py`, `test_vm_phy_c_looking.py`, `test_v14_examine_finds_the_saboteur.py`, `test_v14_surveil_witnesses_the_place.py`, `test_survey_bound.py`; existing `engine/season/tests/test_fi03_trail.py`, `test_information_cluster.py`;
  read only: `08_FI_03`'s `inquiry_world` harness (B11), `08_FI_05_evidence-interface_B`'s hearing fixture (B24), `epistemic.trail_of`, `epistemic.holds_trail`, `loop/witness.py::_told_value`, `::_found_claims`, `modules/fieldwork/find.py`, `engine/season/harness/aperture.py`;
  the closing SHAs of B00, B01, B02, B10, B11, B12c, B24, B25.
  Read whole (an item says so): `proposals/2026-11-12-subsystem-audit-suite/proposals/U1_obstacle_terms_military_physical.md` is not read here (B22's); `engine/season/hole_register.yaml` row H-169 is read whole by B26.16.
SERIAL EDGES:
  within the batch: B26.01 → B26.02 (`16_PESSIMIST_FI_B` lands "after `19_LACUNA_questioning…`, before `16_PESSIMIST_FI_D`") → B26.03 → B26.04 → B26.05 (its edits 1 → 2 → 3 → 4, one commit each) → B26.06 (`16_PESSIMIST_FI_D` after FI_B);
  B26.07 → B26.08 → B26.09 → B26.10 → B26.11 (`14_VERBS_MATERIAL_D` §7: `create_record` → `survey` → `forge` → `destroy_record` → `seize`, "the other four act on papers that say something") → B26.12 → B26.13 (`14_VERBS_MATERIAL_E` after `_D`; `research`, then `reconstruct`) → B26.14 → B26.15 (`14_VERBS_PHYSICAL_C` C1 then C2) → B26.16 → B26.17 (H-169: the design, then the build, at the tail; the build edits `_eff_survey` after B26.08).
  with other batches: `engine/season/queries/world_q.py`, `person_q.py`, `verb_table.yaml`, `rosters.yaml`, `fixtures.py`, `effects_information.py`, `options.py`, `sigma.py`, `data/verbs.py`: hot files (U3 §5.1), B25 → B26 → B27; `engine/season/loop/witness.py`: B25 → B26 → B28; `engine/season/loop/resolve.py`: B10 → B26 → B27; `engine/season/data/fixtures.py: withheld_verbs`: B22 (army verbs, `marshal`, `surrender` leave) and B26 (`destroy_record` leaves, the inquiry rows join) edit one tuple in one step — the coordinator merges B22 first and B26 rebases on it (one key, two batches: §7.3's rule).
PARALLEL: S17 with B11F2 (IN), B22 (MB), B28 (SC), B32 (FA), B37p (WR). Shared with B22: `rosters.yaml`, `verb_table.yaml`, `world_q.py`, `fixtures.py` (the same key, `withheld_verbs`: serialised as above), `effects_information.py` (B22's `_eff_create_record` army branch and B26's `account` branch: one function, two batches — serialised, B22 first), `data/verbs.py`, `sigma.py`, `options.py`. With B28: `witness.py`, `person_q.py`, `options.py`. Merge order: after B11F2 and B22, before B28, B32, B37p.
COST: build (six proposals, one intake entry; small builds and edits, five declared movers in `14_VERBS_MATERIAL_D` alone); producer `sonnet`, effort high; judgment nodes `opus`: B26.07 (the told deposit), B26.10 and B26.11 (the two contested rows), B26.13 (the 20-seed `reconstruct` table), B26.15 (the admission sweep), B26.16 (the design).
EST: 5 h [estimate: the structure's §2.4 formula; nothing timed]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B26.01 | questioning has an approach and a cost; the questioned learn they were asked | `19_LACUNA_questioning_has_an_approach_and_a_cost` | BUILD | MOVER(behaviour) | Batch B25 (CP-T06-05's item; `14_VERBS_SOCIAL2_C` §3), Batch B05 |
| B26.02 | one reader says which papers a person doubts | `16_PESSIMIST_FI_B` edit 1 | BUILD | EQUAL | B26.01; Batch B24, Batch B11 |
| B26.03 | a doubted paper's content answers no operand | `16_PESSIMIST_FI_B` edit 2 | BUILD | EQUAL | B26.02 |
| B26.04 | a name known only from a doubted paper is not a name heard | `16_PESSIMIST_FI_B` edit 3 | BUILD | EQUAL | B26.03 |
| B26.05 | an empty sheet key forms no bag | `16_PESSIMIST_FI_B` edit 4 | BUILD | MOVER(behaviour) | B26.04 |
| B26.06 | the inquiry rows with no product leave formation until they have one | `16_PESSIMIST_FI_D` edits 1, 3 | BUILD | MOVER(behaviour) | B26.05; Batch B11, Batch B25 |
| B26.07 | `create_record` writes an account, and its holder learns it with the writer on the chain | `14_VERBS_MATERIAL_D` §2 | BUILD | MOVER(behaviour) | B26.06; Batch B12c, Batch B07, Batch B10 |
| B26.08 | `survey` can come back thin | `14_VERBS_MATERIAL_D` §4 | BUILD | MOVER(behaviour) | B26.07 |
| B26.09 | `forge` is a false copy of a held paper | `14_VERBS_MATERIAL_D` §3 | BUILD | MOVER(behaviour) | B26.08 |
| B26.10 | `destroy_record` is released, on a paper that names its holder | `14_VERBS_MATERIAL_D` §5 | BUILD | MOVER(behaviour) | B26.09 |
| B26.11 | `seize` takes a warranted person's papers | `14_VERBS_MATERIAL_D` §6 (the Record half) | BUILD | MOVER(behaviour) | B26.10 |
| B26.12 | `research` teaches what it read | `14_VERBS_MATERIAL_E` §2 | BUILD | MOVER(behaviour) | B26.11; Batch B11 |
| B26.13 | `reconstruct` concludes | `14_VERBS_MATERIAL_E` §3 | BUILD | MOVER(behaviour) | B26.12 |
| B26.14 | `examine` forms where the person stands and can name a saboteur | `14_VERBS_PHYSICAL_C` C1 | BUILD | MOVER(behaviour) | B26.13; Batch B12c |
| B26.15 | `surveil` makes the watcher an observer, by a draw | `14_VERBS_PHYSICAL_C` C2 | BUILD | MOVER(behaviour) | B26.14 |
| B26.16 | what bounds a survey's content | H-169 (intake `:480`; E7 carry-forward `:183`) | DESIGN-FIRST | EQUAL | B26.15 |
| B26.17 | a survey is bounded by the seats whose remit covers the subject; the batch's one re-pin | H-169 | BUILD | MOVER(behaviour) | B26.16, B26.08 |
| B26.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1; B26.17 step 3, moved | BUILD | MOVER (the re-pin) | B26.17 |

**Placement and not carried.** H-169: no member or instruction item names its id (`grep -l H-169` over the six members and `master/instructions/`: none), and its text says neither "first" nor "last", so it is placed at the batch's tail in the intake's order (structure §5.6). `16_PESSIMIST_FI_D` edit 2 (R-05's `measured:` text): not carried — `IS-A-01` (B02) removes every row's `measured:` field ("`measured:` leaves"), so the edit has no target; the withheld rows are read through `IS-A-06`'s `BUILT OUT` block instead (see the receipt). `14_VERBS_MATERIAL_D` §6's Rung half (`seize_place`, `places_occupied`): B23's (U3 §4.1 row 82). `14_VERBS_MATERIAL_E` §4 steps 1 and 3 (FI-04 §1, §2 and FI-06): B11's items.

### B26.01 — questioning has an approach and a cost; the questioned learn they were asked · `19_LACUNA_questioning_has_an_approach_and_a_cost` · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/19_LACUNA_questioning_has_an_approach_and_a_cost.md` R-19-10, R-19-11, "Exact edits, by owner" 1–5, Gate, Falsifiers; rulings A-25; U1 ledger P-03, R-25, S-08; `unified/U4_DOCUMENT_STATUS.md` §3.4 (DEP-v11: CP-T06-05).
- ADVANCES: R-05 (`interview`, `interrogate` carry a choice that moves odds); R-08 (suspects react with no player present).
- INSTRUCTION:
  1. `engine/season/verb_table.yaml` — `interview`, `interrogate`: a payload key `questioning` declared in the row's `requires_note` as non-operand; `emits` unchanged.
  2. `engine/season/rosters.yaml: choice_sourced` — `questioning` for both rows, values `calm`, `press` (both formed as Candidate variants; default `calm`, the control). The key is `questioning`, not `approach` (the PC lane's key in the same roster).
  3. `engine/season/seam/wrappers/sigma.py` — the `approach` member of `ADVANTAGE_SOURCES` reads the act's `questioning` value and returns the `press_level` lists: at `press`, one `press_level` for the questioner in the engagement draw, and one `press_level` against the questioned person's answering `lie` (CP-T06-05's `tell` / `lie`); at `calm` no level. Nothing lowers an obstacle (A-25). At `press` the questioned person's regard of the questioner falls by one `regard` step (the stored half, `queries/person_q.py`'s regard writer).
  4. `engine/season/loop/witness.py` — the counterpart observation for `interview` / `interrogate`: every admitted act deposits to its subject one firsthand claim `(questioner, questioned_about, <the act's question subject>)` with the act's `when`, through WITNESS's existing observation deposit (`observation_deposit_mode`, at the counterpart); one predicate `questioned_about`, added to `rosters.yaml: person_predicates`. SITE (the source's `[UNVERIFIED]`): first read whether WITNESS's general presence deposit already gives the subject a `seen` of the act, and record it in the commit body (the gate's control reads it first).
  5. `engine/season/data/fixtures.py` — `press_level` (a `LEVEL_SIGMA` name; first value `minor`, sweep `None` / `minor` / `moderate`, control `None`). `press_ob` is not created.
- WHERE: `engine/season/verb_table.yaml` (`interview`, `interrogate`); `engine/season/rosters.yaml` (`choice_sourced`, `person_predicates`); `engine/season/seam/wrappers/sigma.py` (`ADVANTAGE_SOURCES`, `approach`); `engine/season/loop/witness.py` (the counterpart observation); `engine/season/data/fixtures.py` (`press_level`); NEW `engine/season/tests/test_questioning.py`.
- TESTS: NEW `engine/season/tests/test_questioning.py`, written before the edit and read red: `test_pressed_lies_succeed_less_but_above_zero`, `test_the_questioned_learn_they_were_asked`, `test_guilty_react_to_being_asked_and_innocent_do_not`, `test_press_lowers_regard_one_step_and_calm_does_not`, `test_press_lowers_no_obstacle` (the `terms` are equal across `calm` and `press`; only `levels` differ).
- FALSIFIER and CONTROL: `press` changes the lie's success share to 0 (a lock, not odds); an obstacle term differs between `calm` and `press` (A-25); guilty and innocent interviewees react identically. Control: `questioning` absent (`press_level` `None`) and the deposit off reproduce the base content hash.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_questioning.py -q` → five pass. On `inquiry_world(seed)`, seeds 0–199 (`assert checked >= 200`): a planted guilty interviewee questioned `press` lies successfully in a share strictly lower than questioned `calm`, and strictly above 0; after one admitted `interview`, the interviewee holds `(questioner, questioned_about, X)`; in the following season the share of guilty interviewees who fold `conceal`, `forge`, `lie` or `move` is above the same share with the deposit off, and the share of innocent ones is not; `press` lowers the interviewee's `regard` of the questioner by one step; `calm` leaves it.
- HASH MOVERS: wherever `interview` or `interrogate` folds (19 / 8 / 19 `interview` at `build_realm(0..2)`); declared; B26's one re-pin.
- DEPENDS ON: V12 CP-T06-05's item (Batch B25: the questioned person answers by his own act; the intake's B25 entry `:476`); V12 `14_VERBS_SOCIAL2_C_case_question_confession` §3 (Batch B25: the `interview` row); V12 `U5c_SC_one_obstacle_form` §3 (Batch B05: the `approach` source); V12 `08_FI_03_playable-inquiry` (Batch B11: `inquiry_world`); EXISTS-IN-TREE `engine/season/loop/witness.py` (`observation_deposit_mode`).
- GLOSSARY: row *approach* (U1 ledger S-08) gains the key `questioning` with its reading: "how hard a questioner presses: calm or press"; owner `rosters.yaml: choice_sourced`.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B26's producer, `isolation: worktree`; `Item: B26.01`, `[skip ci]`.

### B26.02 — one reader says which papers a person doubts · `16_PESSIMIST_FI_B` edit 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_FI_B_a_paper_is_about_something.md` "Edits, by owner" 1; "Gate"; closes F-PES-FI-03.
- ADVANCES: R-05 (`forge`, `research`: detection has a consequence).
- INSTRUCTION: `engine/season/queries/person_q.py`, one reader beside `ledger_names`: `doubted(claims) -> frozenset`: the subjects of held claims whose predicate is a `COVERT_KINDS` member (`data/rosters.py`) with a true value. Person-side, World-free; reads the holder's own ledger (AX-2). Kinds come from the roster, so a covert kind that does not write a Record adds ids no content claim has, and changes nothing.
- WHERE: `engine/season/queries/person_q.py` (NEW `doubted`); NEW `engine/season/tests/test_doubted_paper.py`.
- TESTS: NEW `engine/season/tests/test_doubted_paper.py` (the scratch probes `p3b_knows.py`, `p3_forgery.py` restated as named tests, U3 §6.2), written first: `test_holder_who_saw_the_forging_forms_no_candidate_off_the_sheet` (red until B26.03), `test_control_ledger_without_the_claims_forms_them` (green), `test_empty_sheet_key_forms_no_bag` (red until B26.05), `test_ledger_names_skips_a_doubted_paper` (red until B26.04); and `test_doubted_reads_covert_kind_claims` (green after this edit).
- FALSIFIER and CONTROL: a person who holds `(paper, record.forged, True)` whose `doubted` omits the paper. Control: the realm content hash at seeds 0 to 2 equal (no caller yet).
- GATE: `python -m pytest engine/season/tests/test_doubted_paper.py -q` → `test_doubted_reads_covert_kind_claims` and the control pass; the other three red (expected until B26.03–B26.05).
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `engine/season/queries/person_q.py::ledger_names`, `engine/season/data/rosters.py::COVERT_KINDS` `[ASSUMPTION: the name — basis: the source cites it; `rosters.yaml: covert_kinds` exists at :3333]`; V12 `08_FI_05_evidence-interface_B`, `19_LACUNA_admission_rides_the_citing_draw` (Batch B24), `18_DETERMINISM_notice_is_a_draw` (Batch B11) for what makes a holder know.
- GLOSSARY: row *doubted* (new): "a paper its holder knows is false"; owner `person_q.doubted`.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B26's producer; `Item: B26.02`, `[skip ci]`.

### B26.03 — a doubted paper's content answers no operand · `16_PESSIMIST_FI_B` edit 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_FI_B_a_paper_is_about_something.md` edit 2.
- ADVANCES: as B26.02.
- INSTRUCTION: `engine/season/decision/options.py::held_record_claims` and `::_from_content_claim`: a content claim whose subject is in `doubted(p.ledger)` is skipped (computed once per call).
- WHERE: `engine/season/decision/options.py` (`held_record_claims`, `_from_content_claim`).
- TESTS: `test_holder_who_saw_the_forging_forms_no_candidate_off_the_sheet` turns green (row 1 reads 0 candidates addressed off the sheet, row 2 (control) reads 19; row 4 reads 0).
- FALSIFIER and CONTROL: a candidate whose operand was read off a doubted paper's content. Control: the shipped realm's content hash at seeds 0 to 2 unchanged ("no holder doubts a held paper there").
- GATE: `python -m pytest engine/season/tests/test_doubted_paper.py -q` → that test and the control pass; `aperture 2 s`, s = 0 to 2, content hash equal to B26.02's reading.
- HASH MOVERS: none in shipped runs.
- DEPENDS ON: V12 B26.02; EXISTS-IN-TREE `engine/season/decision/options.py::held_record_claims` (`:979`), `::_from_content_claim` (`:913`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B26's producer; `Item: B26.03`, `[skip ci]`.

### B26.04 — a name known only from a doubted paper is not a name heard · `16_PESSIMIST_FI_B` edit 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_FI_B_a_paper_is_about_something.md` edit 3.
- ADVANCES: as B26.02.
- INSTRUCTION: `engine/season/queries/person_q.py::ledger_names`: its content branch skips the claims whose subject is in `doubted(claims)`, so a name he knows only from a paper he knows is false is not a name he has heard.
- WHERE: `engine/season/queries/person_q.py` (`ledger_names`).
- TESTS: `test_ledger_names_skips_a_doubted_paper` turns green.
- FALSIFIER and CONTROL: a name read off a doubted paper in `ledger_names`. Control: shipped hashes at seeds 0 to 2 unchanged.
- GATE: `python -m pytest engine/season/tests/test_doubted_paper.py -q` → four of five pass (`test_empty_sheet_key_forms_no_bag` red until B26.05); content hash at seeds 0 to 2 equal to B26.02's reading.
- HASH MOVERS: none in shipped runs.
- DEPENDS ON: V12 B26.03; EXISTS-IN-TREE `engine/season/queries/person_q.py::ledger_names` (`:1387`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B26's producer; `Item: B26.04`, `[skip ci]`.

### B26.05 — an empty sheet key forms no bag · `16_PESSIMIST_FI_B` edit 4 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/16_PESSIMIST_FI_B_a_paper_is_about_something.md` edit 4; "Cost class" ("edit 4 moves every world where a sheet key is empty (re-pinned once in B26)").
- ADVANCES: R-05 (12 and 16 candidates the fold must refuse stop forming).
- INSTRUCTION: `engine/season/decision/options.py`, the record-sourced operand derivation (`_derive_operand`'s `held=` channel): where `record_sourced_operands` maps the operand to a key and that key's value is `None` or an empty list, the bag is not formed. The one reader of the roster is `decision/options.py::_content_answer` and the answerable set `_RECORD_ANSWERABLE`; the fallback that binds the Record's own id is found before editing by `rg -n "_content_answer\|_RECORD_ANSWERABLE" engine/season/decision/options.py` and reading each call site: the edit is at the call site that substitutes the Record id when `_content_answer` returns `None` (record the site in the commit body).
- WHERE: `engine/season/decision/options.py` (the call site of `_content_answer` that substitutes the Record id).
- TESTS: `test_empty_sheet_key_forms_no_bag` turns green (on a surveyed genuine sheet whose `head` is `None`, 0 candidates with `to` equal to a Record id).
- FALSIFIER and CONTROL: a candidate whose `to` is the Record's own id. Control: worlds with no empty sheet key unchanged.
- GATE: `python -m pytest engine/season/tests/test_doubted_paper.py -q` → five pass; `report` / `delta HEAD` moving the realm (declared).
- HASH MOVERS: every world where a sheet key is empty (declared; B26's one re-pin).
- DEPENDS ON: V12 B26.04; EXISTS-IN-TREE `engine/season/decision/options.py::_content_answer` (`:948`), `::_RECORD_ANSWERABLE` (`:970`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B26's producer; `Item: B26.05`, `[skip ci]`.

### B26.06 — the inquiry rows with no product leave formation until they have one · `16_PESSIMIST_FI_D` edits 1, 3 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/16_PESSIMIST_FI_D_withhold_what_has_no_product.md` "Resolution, decided", "Edits, by owner" 1 and 3, "Gate"; ruling A-81 (consequence 2); F-PES-FI-05, F-PES-FI-11; `unified/U4_DOCUMENT_STATUS.md` §3.4 (DEP-v11: CP-T06-05, B10-15).
- ADVANCES: A-81 (157 still scenes leave a seeded realm at seed 0).
- INSTRUCTION:
  0. The source's own condition, read first: "The three rows ship withheld from formation until each has its product, and each product's own proposal removes its row from the list in the same change": `interview` when the person questioned answers by his own act (CP-T06-05, B25); `reconstruct` when it states a conclusion (`08_FI_03` §3 as amended by `19_LACUNA_conclusion_is_a_committed_assertion.md`, B11; and B26.13 here); `thread_read` when it reads a bond or a hazard (B10-15; `14_VERBS_PHYSICAL_D`, B35). For each row, open its `verb_table.yaml` entry at the batch's open: a row that already carries a graded band with a write is not added; record the reading per row in the commit body. `[UNDECIDED in the receipt: at B26's open CP-T06-05 (B25) and the conclusion (B11) have landed; whether they gave their rows "a graded band with a write" is read at the tree]`.
  1. `engine/season/data/fixtures.py`, `withheld_verbs`: the shipped tuple gains each of `"interview"`, `"reconstruct"`, `"thread_read"` that step 0 does not exclude. The sweep comment gains the arm without them as the control (today's behaviour).
  3. Each product item (B35's `14_VERBS_PHYSICAL_D` for `thread_read`, and any other that step 0 leaves withheld) removes its row from `withheld_verbs` in the same change that gives the row a graded band with a write (A-81); this item writes that sentence into the `withheld_verbs` comment beside each added member, naming its product.
- WHERE: `engine/season/data/fixtures.py` (`withheld_verbs` and its comment); NEW `engine/season/tests/test_withheld_inquiry_rows.py`.
- TESTS: NEW `engine/season/tests/test_withheld_inquiry_rows.py`, written first: `test_three_rows_form_no_candidate` (for each row added; red before), `test_hand_built_interview_and_reconstruct_still_execute` (green: the rows are not deleted; for each of the two that step 0 adds).
- FALSIFIER and CONTROL: after the edit, a seeded realm run in which an act the shipped arm carried out, caused (through `causes[]`) by one of the withheld rows' `finding.made` Events, has no counterpart. Control: the arm without the three (today's tuple).
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_withheld_inquiry_rows.py -q` → green; `python -m engine.season.harness.aperture` at seeds 0–2 → each withheld verb attempted 0 times; `report` / `delta HEAD` moving every seeded realm once (declared).
- HASH MOVERS: every seeded realm (157 of 1,394 acts at seed 0 over three seasons, the source's reading); declared; B26's one re-pin.
- DEPENDS ON: V12 B26.05; V12 CP-T06-05's item (Batch B25); V12 `08_FI_03` §3 and `19_LACUNA_conclusion_is_a_committed_assertion` (Batch B11); EXISTS-IN-TREE `engine/season/data/fixtures.py: withheld_verbs` (H-156; `marshal`'s precedent at `verb_table.yaml`'s "Ships WITHHELD" line).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, high.
- LANDS IT: B26's producer; `Item: B26.06`, `[skip ci]`.

### B26.07 — `create_record` writes an account, and its holder learns it with the writer on the chain · `14_VERBS_MATERIAL_D` §2 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MATERIAL_D_paper.md` §2, §7 (first: "the other four act on papers that say something"), §8 (`create_record`); "Standing" (A-6, A-7, A-8, A-30, A-81); G-02 (no `any:` combinator).
- ADVANCES: R-05; the arc sequence's first stage (238 of 238 `text` Records at seed 0 have no content today).
- INSTRUCTION:
  1. `rosters.yaml: record_kinds.values`: `account: [terms, said]`, with a note: *minted by a computed `create_record`; `terms` is the act's `subject` (`content.read_from`), `said` the `Said` the writer copied at CHOOSE; a `record_sourced_operands` kind mapping `subject: terms`*. `text: []` stays for a hand-built act.
  2. `verb_table.yaml`, `create_record`:
     ```yaml
       - verb:        "create_record"
         stratum:     "uncontested_material"
         eligibility: ["own"]
         beneficiary: "actor"
         capability:  copying
         difficulty:  plain
         requires:    "the writer holds a claim on what he writes about, and is one person"
         requires_typed:
           all:
             - {form: own_ledger, of: subject, conjunct: holds}
             - {form: relation, of: actor, relation: individual}
         writes:  ["Record.exists", "Record.stages"]   # shape (a): one Record; the band sets the drift of `said`
         emits:   ["record.created"]
         emits_on_refusal: {draw: ["record.spoiled"], <each derived clause>: ["record.refused"]}   # MAT_A §2 row 5 note
     ```
     A hand-built act that declares a `kind` and no `said` keeps today's untyped admission by a row flag `declared_kind_admits: true`, read by `_admits` (G-02: there is no `any:` combinator).
  3. `decision/options.py`: nothing new (the named `own_ledger` conjunct already makes `opening_set` copy `said_of` onto the Candidate and decline when there is nothing to say).
  4. `loop/effects_information.py::_eff_create_record`: a payload that declares no `kind` and carries `said` mints `account` with `{terms: subject, said: <the Said, drifted at Partial by the lossy-copy rule `loop/witness.py::_told_value` uses>}`; a declared kind mints as today; any kind at Failure returns `NO_CHANGE` under the Failure band's kind.
  5. `loop/witness.py`, the told channel: for a person who came to hold an `account` Record (the `newly_held` pairs the content deposit reads), also deposit the `Said` as a told claim: source `told_by`, chain = the chain the paper's own `said` content records + the writer the paper names, through the told channel's own guard, refraction and credit. The content deposit ("THE FOURTH DEPOSIT") carries **no attribution** by design, so the told claim is **not** added there; it is one more case in the told-channel block that follows it ("THE TOLD CHANNEL"), and its chain is read from the paper's content, never from the act store.
  6. `rosters.yaml: graded_tasks` gains `create_record`. Draw `H(w.world_seed, w.tick, <actor id>, "create_record.task")` (A-30). A-81: `record.spoiled` is a refusal Event witnessed by those present and, for a writer alone, his own firsthand claim `(self, create_record.failed, True)`.
- WHERE: `engine/season/rosters.yaml` (`record_kinds.values.account`; `record_sourced_operands`; `graded_tasks`); `engine/season/verb_table.yaml` (`create_record`); `engine/season/data/verbs.py` or `data/requires.py` (`declared_kind_admits`, read by `_admits`); `engine/season/loop/effects_information.py` (`_eff_create_record`); `engine/season/loop/witness.py` (the told-channel block); NEW `engine/season/tests/test_vm_mat_d_paper.py`.
- TESTS: NEW `engine/season/tests/test_vm_mat_d_paper.py` (one function per §8 gate; `mat_probe.py` is evidence, not a gate), written first and read red: `test_accounts_have_content_and_no_cohort_writes_one` (realm, seeds 0 to 2: `account` Records with content > 0 and none written by a cohort); `test_a_given_account_teaches_its_holder_with_the_writer_on_the_chain` (a two-hearth fixture: A writes an account of a deed, `give`s it to B; B's ledger holds the deed with A on the chain; B's candidate set on that subject differs from the control, the witness edit off); `test_faithful_and_drifted_accounts_both_occur` (seeds 0 to 19, `assert checked >= 20`).
- FALSIFIER and CONTROL: an account whose receiver holds nothing new. Planted failure: pin the degree at `Success`: no drifted account; the spread test goes red. Control: the witness edit off.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mat_d_paper.py -q` → the three pass; `test_information_cluster.py` → green. The spread read once by `opus`.
- HASH MOVERS: every seeded world (`create_record` is 231 of 1,529 resolved acts at seed 0); declared; B26's one re-pin.
- DEPENDS ON: V12 B26.06; V12 `14_VERBS_MATERIAL_A_mending` §2 (Batch B12c: `graded_amount`, the shapes); V12 `18_DETERMINISM_task_draw_for_uncontested_verbs` items 1, 2, 4 and `U5c_VERBS_residue_and_governance_owner` §1 (Batch B07); V12 `08_FI_01_claim-sourced-referents` edit 1, `08_FI_02_rumour-that-travels` (Batch B11); V12 `02_CHAR_offer_what_can_be_done` item 5 (Batch B10: the `individual` conjunct); EXISTS-IN-TREE `engine/season/queries/person_q.py::said_of`, `engine/season/loop/witness.py::_told_value`, `engine/season/loop/effects_information.py::_eff_create_record`.
- GLOSSARY: row *account* (new): "a paper that says what its writer held about something"; owner `rosters.yaml: record_kinds.values.account`.
- COST and TIER: small build; `sonnet`, high; the told deposit (step 5) `opus`.
- LANDS IT: B26's producer; `Item: B26.07`, `[skip ci]`.

### B26.08 — `survey` can come back thin · `14_VERBS_MATERIAL_D` §4 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MATERIAL_D_paper.md` §4, §8 (`survey`); H-169 limit (1) is B26.16–B26.17's.
- ADVANCES: R-05 (`survey` built out).
- INSTRUCTION:
  1. `queries/person_q.py`, new and World-free: `faction_named(ledger, subject) -> Optional[str]`, the one faction the holder's own claims give `subject`: a claim of a kind a `commit` opener emits pairing him with a faction Proposition, a holder `holders_named` gives a rung, or the Proposition itself; `None` for none or two.
  2. `rosters.yaml`: a line `own_faction_declines: [survey]` read in `opening_set` as `own_stance_declines` is (the referent is kept only where `faction_named` answers). When CHAR's single own-state decline lands this line folds into it.
  3. `verb_table.yaml`, `survey`:
     ```yaml
       - verb:        "survey"
         capability:  inquiry
         difficulty:  routine          # + `opposition` (SC-B) when his ledger names the faction's head
         requires_typed:
           all:
             - {form: own_ledger, of: subject}
             - {form: relation, of: actor, relation: individual}
         writes:  ["Record.exists"]                # shape (a): Partial is a thin sheet, the same cell
         emits:   ["faction.surveyed"]
         emits_on_refusal: {draw: ["survey.failed"], <each derived clause>: ["survey.refused"]}
     ```
  4. `_eff_survey`: at `Partial` the minted sheet keeps `proposition` and `head` and carries `members`, `holdings` and `seats` as empty lists (the key set is exact, so the keys stay). `graded_tasks` gains `survey`. Draw `H(w.world_seed, w.tick, <actor id>, "survey.task")`.
- WHERE: `engine/season/queries/person_q.py` (NEW `faction_named`); `engine/season/rosters.yaml` (`own_faction_declines`; `graded_tasks`); `engine/season/decision/options.py` (`opening_set` reads `own_faction_declines`); `engine/season/verb_table.yaml` (`survey`); `engine/season/loop/effects_information.py` (`_eff_survey`).
- TESTS: in `test_vm_mat_d_paper.py`, written first: `test_full_and_thin_sheets_both_occur_and_post_admission_refusals_are_stale_only` (realm: post-admission `survey.refused` 0 or stale only; full and thin sheets both occur); red before.
- FALSIFIER and CONTROL: a sheet with a non-empty list at `Partial`. Planted failure: pin the degree at `Success`: no thin sheet; the test goes red.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mat_d_paper.py engine/season/tests/test_information_cluster.py -q` → green.
- HASH MOVERS: every seeded world with a survey; declared; B26's one re-pin.
- DEPENDS ON: V12 B26.07; V12 `08_FI_01_claim-sourced-referents` edit 1 (Batch B11: `person_q.holders_named`); EXISTS-IN-TREE `engine/season/loop/effects_information.py::_eff_survey`, `engine/season/decision/options.py::opening_set`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B26's producer; `Item: B26.08`, `[skip ci]`.

### B26.09 — `forge` is a false copy of a held paper · `14_VERBS_MATERIAL_D` §3 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MATERIAL_D_paper.md` §3, §8 (`forge`); F-R4-09 (a quality step, not a second share table); H-169 limit (2) (built at v9 IN-45; this item replaces the body).
- ADVANCES: R-05 (`forge` built out).
- INSTRUCTION:
  1. `rosters.yaml`: `forgeable_kinds: [dispensation, petition, faction_sheet, account]`; `forged_key: {faction_sheet: head, dispensation: terms, petition: terms, account: terms}` (checked against `record_kinds`' key lists at import). `_FORGED_SHEET_KEY` becomes a read of this map.
  2. `queries/world_q.py`: `papers_held(w, p, kinds)`: Records on his own live holds of the given kinds; stamped as `Record.<kind>`.
  3. `verb_table.yaml`, `forge`:
     ```yaml
       - verb:        "forge"
         referent_class: Record        # a paper he holds (`papers_held` over `forgeable_kinds`)
         capability:  copying
         difficulty:  demanding
         counterparty_note: "`to` is whom the false paper names; no second side, so no `counterparty:`"
         requires:    "the forger holds the paper he copies, knows the person it will name, and is one person"
         requires_typed:
           all:
             - {form: existence, of: subject, kind: Record}
             - {form: relation,  of: subject, relation: held_by}
             - {form: existence, of: to, kind: Person}
             - {form: relation,  of: actor, relation: individual}
         writes:  ["Record.exists", "Record.forgery_quality"]   # shape (a): the band sets the quality
         emits:   ["record.forged"]
         emits_on_refusal: {draw: ["forge.failed"], <each derived clause>: ["forge.refused"]}
     ```
     Binding `to` beside `subject` puts `to` in `known_person_operands`, so `operand_bags` forms one Candidate per person the forger knows, himself included; bounded by `Fixtures forge_names` (the newest N known persons, shipped 3) `[ASSUMPTION; medium; Jordan to correct]`.
  4. `loop/effects_information.py::_eff_forge`: copy the exemplar's `subject_matter`, set `forged_key[kind]` to the act's `to`, mint the same kind through `_mint_document` with `forgery_quality` from the band; decline (`forge.refused`) where the exemplar is gone, its kind is not forgeable, or `to` already is the true value. `_mint_sheet`'s `forged=` arm is deleted; `survey` no longer shares a body with `forge`.
  5. `data/fixtures.py`: `forgery_quality_step=1`: Overwhelming `default_forgery_quality + step`, Success the default, Partial `max(1, default − step)`, with a NUMBER row in `hole_register.yaml`; `forge_names=3`. `rosters.yaml: graded_tasks` gains `forge`. Draw `H(w.world_seed, w.tick, <actor id>, "forge.task")`.
- WHERE: `engine/season/rosters.yaml` (`forgeable_kinds`, `forged_key`, `graded_tasks`); `engine/season/queries/world_q.py` (NEW `papers_held`); `engine/season/verb_table.yaml` (`forge`); `engine/season/loop/effects_information.py` (`_eff_forge`, `_mint_sheet`, `_FORGED_SHEET_KEY`); `engine/season/data/fixtures.py` (`forgery_quality_step`, `forge_names`); `engine/season/hole_register.yaml` (one NUMBER row).
- TESTS: in `test_vm_mat_d_paper.py`, written first and read red: `test_a_forged_writ_is_complied_with` (`08_FI_03`'s `inquiry_world`: a forged writ naming a third person, given to its addressee, is followed by a `comply` the control lacks); `test_a_planted_success_research_finds_the_forgery_and_a_higher_quality_resists` (a `research` at a planted `Success` deposits `(record, record.forged, True)`; one quality step higher, the same roll fails). The existing `tests`' forge assertions in `test_information_cluster.py` re-read; any that pin the `_mint_sheet` arm are updated in this commit and named.
- FALSIFIER and CONTROL: a forgery of a paper the forger never held. Control: the same world with the act not formed.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mat_d_paper.py engine/season/tests/test_information_cluster.py engine/season/tests/test_fi03_trail.py -q` → green.
- HASH MOVERS: every seeded world with a forgery; declared; B26's one re-pin.
- DEPENDS ON: V12 B26.08; V12 `08_FI_03_playable-inquiry` (Batch B11: `inquiry_world`); EXISTS-IN-TREE `engine/season/loop/effects_information.py::_eff_forge`, `::_mint_document`, `::_mint_sheet` `[ASSUMPTION: present — cited by the source and by H-169's row]`.
- GLOSSARY: none.
- IDS: H block slot 1 (`forgery_quality_step`'s NUMBER row).
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B26's producer; `Item: B26.09`, `[skip ci]`.

### B26.10 — `destroy_record` is released, on a paper that names its holder · `14_VERBS_MATERIAL_D` §5 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MATERIAL_D_paper.md` §5, §8 (`destroy_record`); H-156 option (b); H-75; H-169 limit (3); `04` §C.6 (covertness is presence).
- ADVANCES: R-05 (`destroy_record` built out: IS-A §12.2 row B26).
- INSTRUCTION:
  1. `data/fixtures.py`: `withheld_verbs` loses `destroy_record` (H-156 option (b); the member is the control arm).
  2. `rosters.yaml: referent_classes` gains `Damning`; `queries/world_q.py::papers_damning(w, p)`: the Records on his own live holds whose content, as his own content claim holds it, names him (`world_q.named`, the reader clause 3 of Q2 uses). `own_hold_declines`' line for this verb goes (the stamp is narrower).
  3. `verb_table.yaml`, `destroy_record`:
     ```yaml
       - verb:        "destroy_record"
         eligibility: ["own"]
         referent_class: Damning
         contests:    "a task"         # shape (b): Partial and Failure emit `destroy.seen`
         capability:  none
         capability_note: "burning a paper draws on no skill; the draw is whether it is seen"
         difficulty:  plain            # + `watch`: (persons present at his rung − 1) x Fixtures watch_step
         requires_typed:
           all:
             - {form: existence, of: subject, kind: Record}
             - {form: relation,  of: subject, relation: held_by}
             - {form: relation,  of: actor, relation: individual}
         writes:  {Overwhelming: ["Record.exists"], Success: ["Record.exists"], Partial: ["Record.exists"], Failure: []}
         emits:
           Overwhelming: ["record.destroyed"]
           Success:      ["record.destroyed"]
           Partial:      ["record.destroyed", "destroy.seen"]
           Failure:      ["destroy.seen"]
         emits_on_refusal: ["destroy.refused"]
     ```
     The §E3 placeholders `hold:<record>` and `presence` leave the eligibility list.
  4. `rosters.yaml: covert_kinds` gains `record.destroyed`, read by `epistemic.trail_of`. No masking rule exists or is added: a person co-located at the burning holds the attribution at every band; the clean/seen difference between bands is the `destroy.seen` deed. It is not a `graded_tasks` member (a contest row). A-81: `destroy.seen` names the actor and is deposited to those present.
- WHERE: `engine/season/data/fixtures.py` (`withheld_verbs`); `engine/season/rosters.yaml` (`referent_classes`, `covert_kinds`, `own_hold_declines`); `engine/season/queries/world_q.py` (NEW `papers_damning`); `engine/season/data/verbs.py` (the `Damning` class constant, as `DETAINEE_CLASS`); `engine/season/verb_table.yaml` (`destroy_record`).
- TESTS: in `test_vm_mat_d_paper.py`, written first: `test_a_destroyed_account_cannot_be_cited` (FI-05-B's hearing fixture: a destroyed one cannot be cited by anybody); `test_a_paper_is_not_destroyed_at_failure`; red before. `test_information_cluster.py`'s destroy tripwire ("the forge and destroy tests assert the two verbs still do not execute") is updated in this commit and named.
- FALSIFIER and CONTROL: a paper destroyed at `Failure`. Planted failure: pin the degree at `Success`: no `destroy.seen`. Control: `withheld_verbs` with `destroy_record` (the shipped arm).
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mat_d_paper.py engine/season/tests/test_information_cluster.py -q` → green.
- HASH MOVERS: every seeded world in which `destroy_record` forms; declared; B26's one re-pin.
- DEPENDS ON: V12 B26.09; V12 `08_FI_05_evidence-interface_B` (Batch B24: the hearing fixture); EXISTS-IN-TREE `engine/season/data/fixtures.py: withheld_verbs` (`destroy_record` first member, H-156), `engine/season/queries/world_q.py::named` `[ASSUMPTION: present — cited]`, `engine/season/epistemic.py::trail_of`.
- GLOSSARY: none (the class name `Damning` is a code name; prose: "a paper that names its holder").
- COST and TIER: small build; `opus` for the contested row (the source's tier), `sonnet` for the rest.
- LANDS IT: B26's producer; `Item: B26.10`, `[skip ci]`.

### B26.11 — `seize` takes a warranted person's papers · `14_VERBS_MATERIAL_D` §6 (the Record half) · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MATERIAL_D_paper.md` §6 (the Record half), §8 (`seize`); A-79, D-U1-02 (opposition through `opposed_ob`); G-03 (one `referent_class` per row); U3 §4.1 row 82 (the Rung half is B23's).
- ADVANCES: R-05 (`seize` on a Record built out: IS-A §12.2 row B26).
- INSTRUCTION:
  1. `queries/world_q.py`: `papers_warranted(w, p)`: for each person a `warrant_sourced` dispensation on his own live hold names, the Records `person_q.holders_named(p.ledger, record)` gives that person; stamped `Record`. (`places_occupied` and the `seize_place` row are B23's.)
  2. `decision/options.py::opening_set`: `seize` leaves `warrant_sourced`'s narrowing (the stamp is the narrowing); `arrest` keeps it.
  3. `loop/effects_information.py::_held_warrant_names`: true when a held warrant names the Record **or the person who holds it** (`hold_force`).
  4. `verb_table.yaml`, `seize`:
     ```yaml
       - verb:        "seize"
         referent_class: Record        # one class per row (G-03); the Rung half is a second row, B23
         contests:    "a task"         # shape (b): bands write different cells and emit different kinds
         capability:  none
         difficulty:  routine          # + `opposition` (the holder's skill score through `opposed_ob`, A-79, D-U1-02)
         writes:
           Overwhelming: ["Tenure.until", "Tenure.since"]
           Success:      ["Tenure.until", "Tenure.since"]
           Partial:      []
           Failure:      []
         emits:
           Overwhelming: ["record.seized"]
           Success:      ["record.seized"]
           Partial:      ["seize.resisted"]
           Failure:      ["seize.resisted"]
         emits_on_refusal: ["seize.refused"]   # a contested row keys one kind; the clause rides `observed`
     ```
     The tree's keyed refusal (`seize.unauthorized`, `seize.refused`) is flattened to one kind (`issue`'s precedent); the refusal's `observed` reads still name the failed clause. `seize` is a contest row, not a `graded_tasks` member.
  5. `_eff_seize` at Overwhelming carries, as `observed`, one `held_by` Observation per other Record the dispossessed person holds; at Partial one for the Record sought. The holder witnesses `seize.resisted` and is free to `give`, `conceal` or `destroy_record` the paper. A-81: `seize.resisted` names the actor and is deposited to those present and to the holder.
  6. (Patched: P-12) `rosters.yaml: contest_owed` (B07's roster of rows owed a `contests:` cell; its loader refuses a member that declares `contests:`): delete `seize` in this commit, which gives the row its `contests:` (B07's UNDECIDED (1); B23's author: "`seize` stays until B26"). If B07's roster lists `seize` under a carrying proposal other than `14_VERBS_MATERIAL_D`, the entry is still deleted here (the row gains its cell here) and the commit body says so.
- WHERE: `engine/season/queries/world_q.py` (NEW `papers_warranted`); `engine/season/decision/options.py` (`opening_set`'s `warrant_sourced` narrowing); `engine/season/loop/effects_information.py` (`_held_warrant_names`, `_eff_seize`); `engine/season/verb_table.yaml` (`seize`); `engine/season/rosters.yaml` (`contest_owed`: `seize` deleted, P-12).
- TESTS: in `test_vm_mat_d_paper.py`, written first and read red: `test_a_seized_account_is_cited_by_the_seizer` (FI-05-B's hearing); `test_a_warned_holder_destroys_after_a_partial_seizure` (at a planted `Partial` seizure the warned holder forms `destroy_record` the next lap and the control does not — source "the next round" → "the next lap", A-101); `test_no_seize_candidate_has_a_person_subject`.
- FALSIFIER and CONTROL: a `seize` Candidate whose subject is a person. Planted failure: pin the degree at `Success`: no resisted seizure.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mat_d_paper.py -q` → green; the spread of each gate read once by `opus`.
- HASH MOVERS: every seeded world in which `seize` forms on a Record; declared; B26's one re-pin.
- DEPENDS ON: V12 B26.10; V12 `08_FI_01_claim-sourced-referents` edit 1 (Batch B11: `person_q.holders_named`); V12 the opposition rule (`opposed_ob`, Batch B05); EXISTS-IN-TREE `engine/season/loop/effects_information.py::_held_warrant_names`, `::_eff_seize` `[ASSUMPTION: present — cited]`.
- GLOSSARY: none.
- COST and TIER: small build; `opus` for the contested row, `sonnet` for the rest.
- LANDS IT: B26's producer; `Item: B26.11`, `[skip ci]`.

### B26.12 — `research` teaches what it read · `14_VERBS_MATERIAL_E` §2 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MATERIAL_E_knowledge.md` §2, §4 step 2, §5 (`research`, A-81); C-24 (`observes:` flat; `finding_terms` owns the band); H-319.
- ADVANCES: R-05 (`research` built out); R-07 (an inquiry teaches).
- INSTRUCTION:
  1. `verb_table.yaml`, `research`:
     ```yaml
       - verb:        "research"
         stratum:     "uncontested_material"
         eligibility: ["own", "presence:<site>"]
         beneficiary: "actor"
         referent_class: Record
         capability:  inquiry
         difficulty:  demanding        # SC-B: reproduces today's obstacle of 2; + `subject` (the Record's forgery_quality)
         requires:    "the record consulted exists, the researcher is where it is, and he is one person"
         requires_typed:
           all:
             - {form: existence, of: subject, kind: Record}
             - {form: relation,  of: subject, relation: present_at}     # FI-04 §2
             - {form: relation,  of: actor, relation: individual}
         writes:      []
         observes:    [{read: content, of: subject}, {read: held_by, of: subject}]   # flat (C-24)
         # finding_terms (U5c_FI_residue.md §8): O and S deposit both reads; P deposits `content`, lossy; F none
         emits:
           Overwhelming: ["finding.made"]
           Success:      ["finding.made"]
           Partial:      ["finding.made"]
           Failure:      ["finding.none"]
         emits_on_refusal: ["inquiry.refused"]                          # FI-04 §1
     ```
  2. `engine/season/data/verbs.py`, `loop/resolve.py::_fold`: FI-03 §2's `observes:` column as written, a **flat** list; which of the row's reads a band deposits, and which band marks a read `lossy`, is `finding_terms`' (`U5c_FI_residue.md` §8), keyed by degree there, not on the row. (If B11 landed the column, this step is the `research` row's use of it only.)
  3. `loop/witness.py`: the Observation deposit (the second deposit) already lands an Event's observations in the actor's ledger; a `content:` read is deposited as the `content:<kind>` claim a holder would get, **without** a `hold`; at a band the row marks `lossy` the value passes through `_told_value`'s drift.
  4. `queries/world_q.py::questions_for`: `research` forms on bare `Record`; SOCIAL2-A's `_stamped` must keep the `(id, Record)` pair beside `(id, Record.<kind>)`.
  5. The `present_at` stem gains one Record branch through `place_of` (FI-04 §2's edit): if B11's FI-04 §2 has not landed it, it lands here first (MATERIAL_E §4 step 1), and the commit says which. The found deposit (`loop/witness.py::_found_claims`, `modules/fieldwork/find.py`) is unchanged.
  6. Draw `H(w.world_seed, w.tick, <actor id>, "research.task")`. A-81: a failed `research` leaves the searcher `(subject, research.failed, True)`, deposited to the actor only (`observation_deposit_mode: actor`), once `rosters.yaml: undeposited_kinds` is amended for inquiries (`U5c_FI_residue.md`'s edit, the FI rewrite lane's; if it has not landed, the A-81 arm of the gate reads its expected 0 at B26's close as not yet met and says so).
- WHERE: `engine/season/verb_table.yaml` (`research`); `engine/season/data/verbs.py` and `engine/season/loop/resolve.py` (`_fold`: the `observes:` column, if not landed); `engine/season/loop/witness.py` (the `content:` read without a `hold`); `engine/season/queries/world_q.py` (`questions_for`; the `present_at` stem's Record branch if not landed); `engine/season/rosters.yaml` (`finding_terms` rows for `research`); NEW `engine/season/tests/test_vm_mat_e_knowledge.py`.
- TESTS: NEW `engine/season/tests/test_vm_mat_e_knowledge.py` (one function per §5 gate, on FI-03's `inquiry_world`), written first and read red: `test_research_lowers_a_liars_record_after_success_and_drifts_at_partial` (a hearer's `record` of a liar reads 1.0 before his `research` of the contradicting account and below 1.0 after a `Success`; at a planted `Partial` he holds a drifted value; at `Failure` nothing; seeds 0 to 2); `test_no_research_by_someone_not_where_the_paper_is` (realm); `test_a_failed_research_leaves_the_searcher_his_claim` (A-81).
- FALSIFIER and CONTROL: a `content:` claim deposited with a `hold`. Control: `observes:` empty reads 1.0 throughout.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mat_e_knowledge.py engine/season/tests/test_fi03_trail.py -q` → green.
- HASH MOVERS: every seeded world with a `research` (71 / 95 / 67 attempted at seeds 0 / 1 / 2); declared; B26's one re-pin.
- DEPENDS ON: V12 B26.11; V12 `08_FI_03_playable-inquiry` §2, `08_FI_04_small-edits` §1–§2, `19_LACUNA_conclusion_is_a_committed_assertion` (Batch B11); V12 `U5c_FI_residue` §7–§8 (`finding_terms`; its batch as U3 places it); V12 `14_VERBS_MATERIAL_A_mending` (Batch B12c); V12 `U5c_SC_one_obstacle_form` §3 (Batch B05); EXISTS-IN-TREE `engine/season/loop/witness.py::_told_value`, `::_found_claims`, `engine/season/queries/world_q.py::questions_for`, `::place_of`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, high.
- LANDS IT: B26's producer; `Item: B26.12`, `[skip ci]`.

### B26.13 — `reconstruct` concludes · `14_VERBS_MATERIAL_E` §3 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_MATERIAL_E_knowledge.md` §3, §4 step 4, §5 (`reconstruct`); C-22 (an inquiry; the conclusion is a deposit; the Proposition is the maker's later `utter`); A-25 (`proofs` is leverage); H-218, H-315, K-37.
- ADVANCES: R-05 (`reconstruct` built out); R-07 (an inquiry reaches a bench through a conclusion).
- INSTRUCTION:
  1. *The value space.* `queries/person_q.py::deed_doer` over the actor's own ledger. New, World-free, beside `said_of`:
     ```python
     def concluded_of(ledger, subject, fx) -> "Optional[Concluded]":
         """What the holder would conclude about `subject`: the newest deed claim he holds whose counterparty or
         object is `subject` (`attributed_deeds` / `is_deed`), the doer `deed_doer` gives it (or None), and the
         number of independent chain roots among his claims of that deed. None where he holds no deed claim on
         it, or already holds a Proposition he uttered concluding on it. `Concluded(deed, doer, roots)`."""
     ```
  2. *It rides the act.* `opening_set` copies `concluded_of` onto the Candidate under `concluded`, as it copies `said`, and declines when it is `None`. The row's named `own_ledger` conjunct is the hook. Where the ledger offers several doers the fan is `choice_sourced` (`reconstruct: [concluded]`).
  3. *The roll.* It joins `graded_tasks` as an inquiry. Pool `inquiry`. Obstacle: difficulty `demanding`. Corroboration is leverage: the `proofs` source (`U5c_SC_one_obstacle_form.md` §3) gives one level per independent root beyond the first (`Concluded.roots − 1`), soft-capped with every other level.
  4. *The product.* `reconstruct` writes nothing. At a winning band WITNESS deposits the conclusion to its maker as his own firsthand claim (content `{deed, counterparty, doer}` at Overwhelming and Success, `{deed, counterparty}` at Partial; the reads `finding_terms` names per band); the HOLDS Proposition exists only when he later `utter`s it with `cites`. At Failure nothing is concluded (`finding.none`).
  5. *What it unlocks.* `rosters.yaml: terms_sourced` gains `petition: [<the conclusion's kind>]` so a petition forms from a held conclusion with its `terms` the named doer.
  6. `verb_table.yaml`, `reconstruct`:
     ```yaml
       - verb:        "reconstruct"
         stratum:     "uncontested_material"
         eligibility: ["own"]
         beneficiary: "actor"
         capability:  inquiry
         difficulty:  demanding        # + levels from the `proofs` source: one per independent root beyond the first
         requires:    "the actor holds a claim of a deed done to or about the subject, and is one person"
         requires_typed:
           all:
             - {form: own_ledger, of: subject, conjunct: holds}
             - {form: relation,  of: actor, relation: individual}
         writes:      []               # an inquiry (C-22): the conclusion is a deposit to its maker
         emits:
           Overwhelming: ["finding.made"]
           Success:      ["finding.made"]
           Partial:      ["finding.made"]
           Failure:      ["finding.none"]
         emits_on_refusal: ["inquiry.refused"]
     ```
     `rosters.yaml: graded_tasks` gains `reconstruct`; the route note's sentence that `reconstruct` "waits on a value space nothing supplies" is struck. Draw `H(w.world_seed, w.tick, <actor id>, "reconstruct.task")`.
  7. If B26.06 withheld `reconstruct`, this item removes it from `withheld_verbs` only where its winning bands' deposit is a durable write by the definition `IS-A-07` copied into B02 (`30_WR_D` §3's list); otherwise it stays withheld and the close says so (`16_PESSIMIST_FI_D` edit 3: the product's change removes the row "in the same change that gives the row a graded band with a write").
- WHERE: `engine/season/queries/person_q.py` (NEW `concluded_of`, `Concluded`); `engine/season/decision/options.py` (`opening_set`: the `concluded` copy and decline); `engine/season/rosters.yaml` (`choice_sourced`, `graded_tasks`, `terms_sourced`, the route note; `finding_terms` rows for `reconstruct`); `engine/season/verb_table.yaml` (`reconstruct`); `engine/season/loop/witness.py` (the conclusion deposit, if `finding_terms` does not already route it); `engine/season/data/fixtures.py` (`withheld_verbs`, step 7 only).
- TESTS: in `test_vm_mat_e_knowledge.py`, written first and read red: `test_reconstruct_deposits_a_conclusion_and_sometimes_a_wrong_name` (FI-03's §3 gate over 20 seeds, `assert checked >= 20`: a conclusion claim is deposited to its maker in more than zero folded acts; at least one run's conclusion names someone who is not the deed Event's actor and at least one names the actor); `test_a_petition_forms_from_a_held_conclusion`; `test_a_proposition_exists_only_after_the_makers_utter`; `test_two_roots_win_more_often_than_one_at_the_same_pool` (the `proofs` level).
- FALSIFIER and CONTROL: a conclusion naming a person the actor's ledger does not hold; a `reconstruct` formed on a subject he holds no deed claim about; all 20 runs name the true actor. Planted failure: compute `concluded_of` from the Event log instead of the ledger: FI-01's silent-change arm must move a candidate and go red.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_vm_mat_e_knowledge.py -q` → green; the 20-seed table read once by `opus` (whether a wrong name occurs).
- HASH MOVERS: every seeded world with a `reconstruct` (84 / 91 / 113 attempted at seeds 0 / 1 / 2) where B26.06 does not withhold it; declared; B26's one re-pin.
- DEPENDS ON: V12 B26.12; V12 `08_FI_06_testimony-names-a-hand` and `19_LACUNA_conclusion_is_a_committed_assertion` (Batch B11: the pairing travels; the one mint of a committed conclusion); EXISTS-IN-TREE `engine/season/queries/person_q.py::deed_doer` (`:250`), `::said_of` (`:1165`).
- GLOSSARY: row *conclusion* (U1 S-21) becomes a pointer to `person_q.concluded_of`.
- COST and TIER: small build; `sonnet`, high; one `opus` read of the 20-seed table.
- LANDS IT: B26's producer; `Item: B26.13`, `[skip ci]`.

### B26.14 — `examine` forms where the person stands and can name a saboteur · `14_VERBS_PHYSICAL_C` C1 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_PHYSICAL_C_looking.md` C1, "Order of landing"; `audits/14_VERBS_PHYSICAL.md` §7.7 (copied); REM-22.
- ADVANCES: R-05 (`examine` built out: IS-A §12.2 row B26).
- INSTRUCTION:
  1. `engine/season/queries/world_q.py`: stamp term `sites_here(w, p)`: Sites whose `rung` equals `place_of(w, p.id)`, sorted. Stamped in `_stamped` under `Site`.
  2. `engine/season/rosters.yaml: covert_kinds`: `values: ["record.forged", "site.damaged", "record.destroyed"]` (B26.10 added `record.destroyed`). Note: *"`site.damaged` (14_VERBS_PHYSICAL_C): a sabotage is a deed done TO a Site, which `examine` (a Site inquiry) can uncover through `trail_of`'s written side. [ASSUMPTION; medium; revert: drop the value]."* `_check_covert_kinds` accepts it (`sabotage` emits it).
  3. `engine/season/verb_table.yaml`, row `examine`: `observes:` per FI-03 §2 (the Site's `condition`; the `stores` of its rung). `referent_class_note`: append *"14_VERBS_PHYSICAL_C: `sites_here` stamps the Sites where he stands, so the row forms; REM-22's 'never attempted' closes."*
- WHERE: `engine/season/queries/world_q.py` (NEW `sites_here`; `_stamped`); `engine/season/rosters.yaml` (`covert_kinds`); `engine/season/verb_table.yaml` (`examine`); NEW `engine/season/tests/test_v14_examine_finds_the_saboteur.py`; NEW `engine/season/tests/test_vm_phy_c_looking.py`.
- TESTS: NEW `engine/season/tests/test_v14_examine_finds_the_saboteur.py` (`audits/14_VERBS_PHYSICAL.md` §7.7, copied), written first and read red: `build_realm(0)`; a person sabotages a Site through the real fold, unseen (`sabotage` executed with no co-present witness); an investigator stands at the same place. One season. Pass: the investigator forms `examine` on that Site; an executed `examine` at Success deposits a claim anchored on the saboteur with the `site.damaged` kind; at Partial it deposits the kind without the hand. **Control:** with `covert_kinds` at its shipped value, the same Success deposits no trail claim. NEW `engine/season/tests/test_vm_phy_c_looking.py`: `test_examine_is_attempted_above_zero` (`aperture 2 0` and `2 1`).
- FALSIFIER and CONTROL: planted, remove `sites_here` from `_stamped`: `examine` formations return to 0; ship `covert_kinds` unchanged: a Success finds no saboteur.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_v14_examine_finds_the_saboteur.py engine/season/tests/test_vm_phy_c_looking.py -q` → green.
- HASH MOVERS: every realm pin (`examine` 0 to some formations; Site rows such as `restore` and `sabotage` gain formations at the actor's place: H-163's shared-class cost); declared; B26's one re-pin.
- DEPENDS ON: V12 B26.13, B26.10; V12 `08_FI_03_playable-inquiry` §2 and `08_FI_04_small-edits` (Batch B11: `observes:`); V12 `14_VERBS_MATERIAL_A_mending` (Batch B12c: `sabotage` emits `site.damaged`); V12 `18_DETERMINISM_task_draw_for_uncontested_verbs` item 2 (Batch B07: `graded_tasks`); EXISTS-IN-TREE `engine/season/queries/world_q.py::place_of`, `::_stamped` `[ASSUMPTION: present — cited]`, `engine/season/rosters.yaml: covert_kinds` (`:3333`).
- GLOSSARY: none.
- COST and TIER: edit and a stamp; `sonnet`, effort medium.
- LANDS IT: B26's producer; `Item: B26.14`, `[skip ci]`.

### B26.15 — `surveil` makes the watcher an observer, by a draw · `14_VERBS_PHYSICAL_C` C2 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/14_VERBS_PHYSICAL_C_looking.md` C2, "Order of landing", Gate, Falsifier; `audits/14_VERBS_PHYSICAL.md` §8.7 (copied); A-30; `04` PART D 35 (a new draw must not move unrelated goldens); D-44, D-45; A-81.
- ADVANCES: R-05 (`surveil` built out); R-08 (watching has a risk; concealment has a counter).
- INSTRUCTION:
  1. `queries/world_q.py`: stamp term `place_here(w, p)`: `(place_of(w, p.id),)` or `()`, stamped under `Rung`.
  2. `rosters.yaml`: new roster `own_presence_declines` (`own_hold_declines`' shape): `values: [surveil]`. Read in `decision/options.py::opening_set` beside `OWN_HOLD_DECLINES`: keep `r` only if `r` is the object of one of `p`'s own live `contain` Tenures. Own state, no World.
  3. `verb_table.yaml`, row `surveil`: `referent_class: Rung`. `emits:` `Failure: ["finding.none", "watcher.seen"]` (both in its `draw` refusal clause, residue §1). `emits_note`: *"`watcher.seen` (14_VERBS_PHYSICAL_C C2): the Exposure half of canon carried as a deed anchored on the watcher and witnessed by those present (no aggregate on a Rung, 04:260)."* `observes:` per FI-03 §2.
  4. `rosters.yaml: witness_channels`: `values` gains `surveil`, placed **second**, after `co_located` and before `witness_key`; `claim_source:` gains `surveil: firsthand`; one note sentence naming this file and the revert (drop the value). The channel admits observer `q` to an Event `e` when `e`'s place is the subject Rung of a `finding.made` Event of verb `surveil` by `q` in the same season, or lies under that Rung (`causing_act` to read the verb and subject, resolver-side; no new state). Admission is a keyed draw at `surveil_watch_rate[band]`. The terms shown are `finding_terms[band]` (one mask).
  5. `engine/season/epistemic.py`: one function `_ch_surveil(w, e, pid) -> bool`, found by derived name into `CHANNEL_PREDICATES`; `observers_for` dispatches it from the roster with no verb literal. The draw is `H(w.world_seed, w.tick, e.id, f"surveil.watch:{pid}")` through the one draw owner (A-30), with a pinned golden in the test.
  6. `data/fixtures.py`: `surveil_watch_rate: {Overwhelming: 1.0, Success: 0.5, Partial: 0.25}`, `[ASSUMPTION: not decidable from the repository — basis: R4 7b.5; swept {0.25, 0.5, 1.0}, control 1.0 at every band (the band alone admits)]`, NUMBER row in `hole_register.yaml`.
- WHERE: `engine/season/queries/world_q.py` (NEW `place_here`); `engine/season/rosters.yaml` (NEW `own_presence_declines`; `witness_channels`); `engine/season/decision/options.py` (`opening_set`); `engine/season/verb_table.yaml` (`surveil`); `engine/season/epistemic.py` (NEW `_ch_surveil`); `engine/season/data/fixtures.py` (`surveil_watch_rate`); `engine/season/hole_register.yaml` (one NUMBER row); NEW `engine/season/tests/test_v14_surveil_witnesses_the_place.py`.
- TESTS: NEW `engine/season/tests/test_v14_surveil_witnesses_the_place.py` (`audits/14_VERBS_PHYSICAL.md` §8.7, copied; "round 1/2" there is the season's pass: laps, A-101), written first and read red: `build_realm(0)`; a watcher and a third person at one settlement. The watcher's `surveil` is forced to Success (fixture pool) in lap 1. The third person performs `give` at the same place in lap 2, with no co-location channel admitting the watcher (the test plants the watcher in a quarter under the settlement so the ordinary channel does not admit him). Pass: the watcher holds a claim of the `give` anchored on the giver. At Partial, the claim holds no hand. At Failure, the third person holds a `watcher.seen` claim anchored on the watcher. **Control:** without the surveil, the watcher holds no claim of the `give`. In `test_vm_phy_c_looking.py`: `test_surveil_refusals_on_presence_and_rung_are_zero`; `test_the_admission_draw_is_pinned` (its golden; `04` PART D 35); `test_at_rate_one_every_event_is_seen` (the control that the draw, not the band alone, admits).
- FALSIFIER and CONTROL: planted, remove the `surveil` channel from `witness_channels`: the Success case deposits nothing; set `surveil_watch_rate` to 1.0 in the probe and observe that every Event is seen.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_v14_surveil_witnesses_the_place.py engine/season/tests/test_vm_phy_c_looking.py -q` → green; `aperture 2 0` and `2 1`: `surveil` refusals on `present_at` and `exists:Rung` at 0. The admission sweep read once by `opus`.
- HASH MOVERS: every realm pin (`surveil` formations narrowed; the channel's admissions); declared; B26's one re-pin.
- DEPENDS ON: V12 B26.14; V12 `08_FI_03_playable-inquiry` §2 (Batch B11); EXISTS-IN-TREE `engine/season/rosters.yaml: witness_channels` (`:409`), `engine/season/epistemic.py::CHANNEL_PREDICATES`, `::observers_for`, `engine/season/data/rosters.py::WITNESS_CHANNELS`.
- GLOSSARY: none (*surveil* has a row).
- IDS: H block slot 2 (`surveil_watch_rate`'s NUMBER row).
- COST and TIER: small build (one witness channel); `sonnet`, high; one `opus` read of the admission sweep.
- LANDS IT: B26's producer; `Item: B26.15`, `[skip ci]`.

### B26.16 — what bounds a survey's content · H-169 · DESIGN-FIRST · HASH EQUAL
- SOURCE: the intake `:480` (H-169 · STILL-NEEDED · rows E3:595, E7:67 · settled: "register row governs (E7:67 STILL-NEEDED)"); its carry-forward block `master/eval/E7.md:183-186` (OWNER verbatim: `loop/effects_information.py` — `_eff_survey` (limits 1, 6) and `_eff_forge` (limit 2, built at v9 IN-45); `verb_table.yaml` — `destroy_record`'s eligibility (limit 3, `H-75`); `rosters.yaml` — `record_kinds.faction_sheet`, whose keys follow `faction_q.Faction` (limit 4), and `record_sourced_operands` (its `faction_sheet` row, limit 5)); `engine/season/hole_register.yaml` row H-169 (read whole by this item); `audits/08_FI_audit.md:521` ("design-first, unchanged"); D-18.
- ADVANCES: R-05, R-06 (a sheet whose scope is the seats one filled: "the missing motive for the entire personnel layer", proposal 14.1 as the row quotes it).
- INSTRUCTION: write the design stating (1) to (5) with falsifiers; no code. The carry-forward's INSTRUCTION: "design-first (the FI audit says 'unchanged'). Bound a survey's content by the seats whose remit covers the subject (the row's 14.1 form) rather than `faction_q.resolve` whole. Limits 2 and 3 are built." The row's 14.1 form: "*a set of people, never a visibility number* -- the seats whose remit covers the subject bound the compiler and the compiler's competence scales the error".
  1. The set: which seats' remits bound a survey of a faction, of a person, of a Rung (limit 6 is lifted: a Rung subject is answered by `holder_faction_of`).
  2. What a bounded sheet holds of `members`, `holdings`, `seats` when the compiler holds no covering seat, and how it composes with B26.08's thin `Partial` sheet (one sheet shape, not two).
  3. How "the compiler's competence scales the error": by the `survey` draw's band (B26.08) alone, or a further term — named, with its reader.
  4. Limits 4 (no date key) and 5 (members, holdings, seats read by nothing): whether this design takes them or leaves them on the row, said.
  5. The falsifier: a survey by a person with no remit over the subject returns the full sheet; the control: one with a covering seat returns the full one.
- WHERE: NEW `proposals/2026-11-12-subsystem-audit-suite/proposals/FI_survey_bound_by_remit.md` `[ASSUMPTION: the path — basis: CLAUDE.md §3, new design work goes to proposals/; the bound's data live where code reads them, never in this file]`.
- TESTS: none (a design).
- FALSIFIER and CONTROL: the design leaves (1) or (3) undecided. Control: nothing in `engine/` changes.
- GATE: `test -f <that file> && grep -c -E 'remit|members|holdings|seats' <that file>` → the file exists and states (1) to (5); `git diff --stat HEAD~1 -- engine modules references` → empty for this commit.
- HASH MOVERS: none.
- DEPENDS ON: V12 B26.08 (`survey`'s bands); EXISTS-IN-TREE `engine/season/loop/effects_information.py::_eff_survey`, `engine/season/queries/faction_q.py::resolve` `[ASSUMPTION: present — named by the row]`, `Office.remit`.
- GLOSSARY: none.
- COST and TIER: design; `opus` (the carry-forward's TIER), high; a `ners` critic. What the ladder cannot settle ends the run `STOPPED` for Jordan (D-18).
- LANDS IT: B26's producer; `Item: B26.16`, `[skip ci]`.

### B26.17 — a survey is bounded by the seats whose remit covers the subject; the batch's one re-pin · H-169 · BUILD · HASH MOVER(behaviour)
- SOURCE: the intake `:480`; `master/eval/E7.md:183-186` (GATE: "a survey by a person with no remit over the subject returns a bounded sheet; a control with a covering seat returns the full one. HASH: moves [ASSUMPTION]. TIER: opus."); B26.16's design.
- ADVANCES: R-05, R-06; narrows H-169 to the limits B26.16 leaves open.
- INSTRUCTION:
  1. `loop/effects_information.py::_eff_survey`: bound the sheet's content by the seats whose remit covers the subject, as B26.16's design states (its (1) and (2)), in place of `faction_q.resolve` whole. If B26.16's design is not merged when this item's turn comes, this item is HELD (D-18) and leaves for the held list at the expunge; the re-pin of step 3 then rides B26.15's commit instead, and the close says so.
  2. `engine/season/hole_register.yaml`, row H-169: limit (1) closed by this commit (with the SHA in the close), limits (2) and (3) recorded as built (B26.09, B26.10), what B26.16 leaves of (4) and (5) stated; nothing else of the row edited.
  3. **The re-pin.** In this commit, re-record every pin B26's declared movers moved (B26.01, B26.05–B26.15, and this item): the realm, spine and corpus pins at seeds 0 to 2, rebased on B22's merge (step S17's order); the commit says "re-pin" plainly and quotes the before-reading (`reading @<sha>`) and the after-reading. The last `Item:` commit also writes the named conjuncts' `reading:` records (`IS-A-12`; `status:` not edited).
- WHERE: `engine/season/loop/effects_information.py` (`_eff_survey`); `engine/season/hole_register.yaml` (H-169); the pin files the movers reach (B02's one golden owner, `engine/season/tests/_realm_goldens.py`); `engine/season/requirements.yaml` (`reading:` records); NEW `engine/season/tests/test_survey_bound.py`.
- TESTS: NEW `engine/season/tests/test_survey_bound.py`, written before step 1 and read red: `test_a_survey_without_a_covering_seat_is_bounded`; `test_a_survey_with_a_covering_seat_is_full` (the control; green at the base and after).
- FALSIFIER and CONTROL: a survey by a person with no remit over the subject returns the full sheet. Control: a compiler with a covering seat returns the full one.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_survey_bound.py engine/season/tests/test_information_cluster.py engine/season/tests/test_vm_mat_d_paper.py -q` → green after the re-pin; the pinned-hash tests B02 owns → green on the re-pinned values.
- HASH MOVERS: every seeded world with a survey by a person with no covering seat ("moves [ASSUMPTION]", the carry-forward's); the re-pin covers the batch.
- DEPENDS ON: V12 B26.16, B26.08; EXISTS-IN-TREE `engine/season/loop/effects_information.py::_eff_survey`, `engine/season/hole_register.yaml` row H-169 (`:3824`).
- GLOSSARY: none.
- COST and TIER: small build; `opus` (the carry-forward's TIER) for step 1, `sonnet` for the re-pin.
- LANDS IT: B26's producer; `Item: B26.17`, `[skip ci]` (the batch's last `Item:` push is B26.99, which takes step 3, the re-pin, and the GATE's "green after the re-pin" arms; step 1's HELD fallback no longer moves the re-pin to B26.15; repair lane R1, E-1).

### B26.99 — re-pin and close readings · `V12_STRUCTURE_part4.md` E-1; B26.17 step 3, moved · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; B26's RE-PIN, REQUIREMENT and BATCH GATE lines; B26.17 INSTRUCTION step 3, moved here by repair lane R1 (part 2 §11 C-01; K8 F1).
- ADVANCES: the `BUILT OUT` readings of B26's REQUIREMENT line (`destroy_record`, `examine`, `seize` a Record), read on this tree; their conjuncts' `reading:` records written here (`IS-A-12`); no `status:` edited.
- INSTRUCTION: (1) **The re-pin**: B26.17 step 3 as written there (every pin B26's declared movers moved, B26.01, B26.05 to B26.15 and B26.17: the realm, spine and corpus pins at seeds 0 to 2, rebased on B22's merge, step S17's order; "re-pin" said plainly, before and after quoted). If B26.17 is HELD (its step 1: B26.16's design unmerged), the re-pin is still made here, over the movers that landed. (2) Every BATCH GATE line, the `HASH READING` at `<s>` = 0, 1, 2 before (`reading @<sha>`) and after, the `BUILT OUT` lines before and after, and the batch's measured wall time, into this commit's body; the named conjuncts' `reading:` records.
- WHERE: the pin files the movers reach (B02's one golden owner, `engine/season/tests/_realm_goldens.py`); `engine/season/requirements.yaml` (`reading:` records).
- TESTS: none new; after step 1 the pinned-hash tests B02 owns read green on the re-pinned values.
- FALSIFIER and CONTROL: a pin that moved and that no B26 item declared (then the re-pin stops and the batch is `STOPPED`). Control: B22's merge readings (`reading @<sha>`), the base B26 rebased on.
- GATE: the BATCH GATE above, every line, read once on this commit's tree; `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_survey_bound.py engine/season/tests/test_information_cluster.py engine/season/tests/test_vm_mat_d_paper.py -q` → green after the re-pin (B26.17's files; `test_survey_bound.py` exists only if B26.17 landed).
- HASH MOVERS: the batch's one re-pin, here and nowhere else.
- DEPENDS ON: V12 B26.01 to B26.17.
- GLOSSARY: none.
- COST and TIER: a re-pin and the readings; `sonnet`, high.
- LANDS IT: B26's producer; `Item: B26.99`, the batch's last `Item:` push (no `[skip ci]`: its push opens BATCH-CLOSE).

| STOP. Batch B26-fi-inquiry closes here |


