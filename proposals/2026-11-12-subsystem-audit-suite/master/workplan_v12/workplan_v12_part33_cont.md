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
- DEPENDS ON: EXISTS-IN-TREE `engine/season/loop/effects_shared.py::occupying_faction` (`:149`), `::_seize_rung`.
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
- TESTS: in `test_resv_field_defender.py`, written before step 1 and read red: `test_a_captured_commander_is_not_mustered` (a hand-built world with one captured commander: `mustered` at his rung excludes him and the field's sides are built without his weight).
- FALSIFIER and CONTROL: a detained person's `body` scaled by a field he could not have stood in. Control: worlds with no detained member unchanged by step 1.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_resv_field_defender.py engine/season/tests/test_in12_raze.py -q` → green after the re-pin; the pinned-hash tests B02 owns → green on the re-pinned values.
- HASH MOVERS: fields in which a mustered member is detained (none in shipped play before B22.33); the re-pin covers the batch.
- DEPENDS ON: V12 B22.34; EXISTS-IN-TREE `engine/season/queries/world_q.py::mustered` (`:2132`), `::restrained` (`:1766`).
- GLOSSARY: none.
- COST and TIER: edit and the re-pin; `sonnet`, high.
- LANDS IT: B22's producer; `Item: B22.35`, the batch's last `Item:` commit (no `[skip ci]`: its push opens BATCH-CLOSE).

| STOP. Batch B22-mb-armies closes here |

