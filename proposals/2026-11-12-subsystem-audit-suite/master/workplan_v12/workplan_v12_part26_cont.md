# Workplan v12 — part 26, continued: Batch B19-mb-field-calibration, first half (B19.17 to B19.27)

## Status: PROPOSED (the continuation of `workplan_v12_part26.md`, split at an item boundary for the 120 KB cap, `V12_STRUCTURE_part4.md` E-12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

The batch block's head, its position table and B19.01 to B19.16 are in `workplan_v12_part26.md`. Words, paths and the tree read (`8c087bc`) are that file's.

---

### B19.17 — a unit formation and the scale of a cell, at the control arm · `04_MB_cell_hierarchy_as_data` §1–§2 · BUILD · HASH EQUAL (at `arm: cap`)
- SOURCE: `proposals/04_MB_cell_hierarchy_as_data.md` "The resolution, decided" §1 (words), §2 (the unit's formation), "Exact edits" rows 1–4 (their §2 parts), "Gate" 1–4, "Tests (W3-1)", "Falsifier"; the second `Folded:` line (the sourced depth seeds); `MB_LEXICON_part3.md` D-15, S-7 (`ranks`, `files` → `depth`, `width`); carries R-30, R-32 of `audits/04_MB_audit_addendum_B.md` §B6; rulings A-2, A-59 (2), (3); closes F-MB-20, F-MB-22.
- ADVANCES: R-04.c5 (ii) (a fought field on a cell battlefield with depth), through the flip B19.23.
- INSTRUCTION (copied, with S-7 applied to the column names):
  1. Troop file header, `references/troops.yaml`:
     ```yaml
     deployment:
       cell_troops: 16        # troops a cell at deployment. SEED: the tier table's density at 400 troops (25 cells)
       arm: cap               # grid | cap.  `cap` is today's packing and the control arm (flipped to grid at B19.23)
     ```
  2. Troop row: `depth` (was `ranks`, S-7; seeds, "the sourced depths, **2 for sword and spear foot, 4 for pike, 2 for horse**, and 2 for missile troops `[ASSUMPTION: missile depth not established in the sourced note — basis: the lowest sourced foot depth]`"). Unit row on the army Record (both optional): `depth`, `width` (was `ranks`, `files`), in cells.
  3. "Rule, in `orderofbattle._spec_for` and the two headcount constructors (one function, three callers):"
     ```
     depth = unit.depth or troop.depth
     width = unit.width or max(1, round(troops / (depth * deployment.cell_troops)))
     spec  = dict(width=width, depth=depth)          # footprint_for's explicit-grid arm, which exists today
     ```
     "Under `arm: cap` the constructors pass the cap as now." `footprint_for`'s explicit arm "ignores the floor and cap by design".
  4. Exact edits for §2: `references/troops.yaml`, `tools/export_troops.py` (`deployment`; `depth` on each troop row); `orderofbattle.py` (`UnitRow` gains `depth`, `width`; `_spec_for` computes the grid; `_rows_of` already takes `width`, `depth`); `massbattle.py` ("`_weighted_unit`, `_person_unit` call the same grid function in place of `concentration=float(CELL_CAP)`"); `armyrecord.py` ("`order` accepts ... `ranks`, `files`, validated against the exported sets; `to_order_of_battle` carries them", as `depth`, `width`); `engine/season/rosters.yaml: record_kinds.values.army` ("the unit row's key set gains" them; the pin test follows).
  5. First step (the source's W3-1 note): write `systems/mass_battle/sim/cells_probe.py` ("per army preset: cells per unit and ranks per block") and `systems/mass_battle/sim/pike_probe.py` ("n fields of a pike line and a heavy-infantry line at one seed set; count identical results"), each printing its reading.
- WHERE: `references/troops.yaml` (`deployment.cell_troops`, `deployment.arm`; troop rows' `depth`); `tools/export_troops.py`; `engine/engine_params/troops.json` (re-derived); `modules/mass_battle/troop_types/table.py` (reads the columns); `modules/mass_battle/orderofbattle.py` (`UnitRow.depth`, `.width`, `_spec_for`); `modules/mass_battle/massbattle.py` (`_weighted_unit`, `_person_unit`); `modules/mass_battle/armyrecord.py` (`order`, `validate`, `to_order_of_battle`); `engine/season/rosters.yaml` (`record_kinds.values.army`); NEW `systems/mass_battle/sim/cells_probe.py`, `pike_probe.py`; `tests/valoria/test_mass_battle_order_of_battle.py`; `tests/valoria/test_mass_battle_army_record.py` (the key-set pin).
- TESTS: `tests/valoria/test_mass_battle_order_of_battle.py::test_depth_is_a_lever` (gate 4: "two equal heavy-infantry bodies, one at `depth: 2`, one at `depth: 6`, n 200 against the same-run control: the win counts or the loss shares differ beyond the control's spread, in either direction; the result is recorded, not targeted", `assert checked >= 200`; it builds both on the grid rule explicitly, so it is green here and does not wait for the flip); the key-set pin in `test_mass_battle_army_record.py` follows.
- FALSIFIER and CONTROL: "a field whose result under `arm: cap` differs from today's". Control: gate 1, `arm: cap`: digests equal; `cells_probe.py` "prints today's counts (heavy infantry 2 cells, crossbow 1, cavalry 2, levy 1 for the weight-20 preset)".
- GATE: `python tools/export_troops.py --check` → exit 0; `python systems/mass_battle/sim/cells_probe.py` → heavy infantry 2, crossbow 1, cavalry 2, levy 1 (the weight-20 preset, `arm: cap`); `python -m pytest tests/valoria/test_mass_battle_order_of_battle.py tests/valoria/test_mass_battle_army_record.py tests/valoria/test_field_golden_pins.py -q` → pass (the pins as B19.12 left them, EXPECTED RED UNTIL B19.99 where B19.12 moved them); the seed-0 field hash equal to B19.15's.
- HASH MOVERS: none under `cap` ("none under `cap`").
- DEPENDS ON: V12 Batch B17 (`references/troops.yaml`, `tools/export_troops.py`, `troop_types/table.py`, `04_MB_headcount_grade_and_scale`); V12 B19.15; EXISTS-IN-TREE `geometry.py::footprint_for` (`:101`), `orderofbattle.py::_spec_for` (`:142`), `::_rows_of` (`:172`), `massbattle.py::_weighted_unit` (`:257`), `::_person_unit` (`:312`), `armyrecord.py::order` (`:203`), `::to_order_of_battle` (`:256`); `_spec_span` named by the source is in the tree (`modules/mass_battle/armies.py::_spec_span`, imported by `orderofbattle.py`; corrected by check lane K6: the item's earlier text said `grep: none`) and is not needed (`_rows_of` takes both).
- GLOSSARY: *unit formation* (§J): owner column → `references/troops.yaml` troop row `depth` and the unit row's `depth`, `width` (lexicon D-15); "ranks", "files" refused for the columns. *cell*: `deployment.cell_troops` the owner of a cell's men at deployment.
- NAMES: `Subformation` → `UnitRow`; Record key `subformations` → `units`; `stance` Record key → `posture` (B16L); `Subunit` → `Unit` (B16M; "`Subunit.width`, `depth`" in the source); `ranks` → `depth`, `files` → `width` (S-7, the suite's own rename, applied here).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B19's producer; `Item: B19.17`, `[skip ci]`.

### B19.18 — the army formation as rows; a unit's post · `04_MB_cell_hierarchy_as_data` §3 · BUILD · HASH EQUAL (at `line`)
- SOURCE: the same file, §3, "Exact edits" (the §3 parts and the `systems/mass_battle/sim/engine.py` row), "Gate" 5, "Tests (W3-1)"; `MB_LEXICON_part3.md` D-4 and S-6 (post `front` → `centre`), D-1 (subformation); `26_MASS_BATTLE_cell_scale_and_time.md` / U1 glossary *approach* (`approach_rows` → `opening_rows`); carries R-33; A-1, A-59 (3).
- ADVANCES: R-04.c4 (placement decides a field; `27_MB_C` gate 3 reads it in the second half).
- INSTRUCTION (copied, with S-6 applied):
  1. Troop file section:
     ```yaml
     formations:
       line:                       # today's rule, transcribed: the control
         opening_rows: 3           # the opening distance (was `approach_rows`; replaces `orderofbattle.py:67 _APPROACH_ROWS`)
         posts:
           centre:  {rank_line: 0, across: centre}
           rear:    {rank_line: 1, across: centre}     # one clear row behind the centre's depth
           left:    {rank_line: 0, across: left}
           right:   {rank_line: 0, across: right}
           reserve: {rank_line: 2, across: centre}
         default_post: {melee: centre, missile: rear, mounted: [left, right]}   # alternating, as now
       envelopment:                       # the harness's build_envelopment, as a row
         opening_rows: 3
         posts: {centre: {rank_line: 0, across: centre}, left: {rank_line: 0, across: wide_left}, right: {rank_line: 0, across: wide_right}, ...}
       refused_flank: { ... }             # the harness's build_refused_flank, as a row
     ```
     The `envelopment` and `refused_flank` rows' remaining posts are transcribed from `systems/mass_battle/sim/engine.py::build_envelopment` (`:127`) and `::build_refused_flank` (`:224`) so that gate 5's "the harness's own envelopment builder produces the same starting cells" holds (the source's "..." is that transcription).
  2. "`OrderOfBattle.formation: str = 'line'`; the Record's `strategy` key carries it." "Unit row: `post` (the formation post: `centre`, `rear`, `left`, `right`, `reserve`), default by the troop's class."
  3. "`orderofbattle._place` becomes the reader of a formation row: it places each line by the depth of the line in front of it, and each post across the field, exactly as it does now for the one rule. It still degrades to one centred line when a layout does not fit." `_APPROACH_ROWS` becomes the `line` row's `opening_rows` (B19.21 makes it a rule).
  4. "The timed release that makes an envelopment an envelopment (wings hold, then wheel) is not part of the formation row. It is a standing order on the wing units (`signal:` or `tick:`)."
  5. `armyrecord.order` accepts `post`, "validated against the exported sets; `to_order_of_battle` carries" it; `rosters.yaml: record_kinds.values.army` gains `post`; `systems/mass_battle/sim/engine.py`: "`build_envelopment`, `build_refused_flank` become thin callers of the formation rows, so the harness and the season deploy by one rule".
- WHERE: `references/troops.yaml` (`formations`); `tools/export_troops.py`; `engine/engine_params/troops.json`; `modules/mass_battle/orderofbattle.py` (`OrderOfBattle.formation`, `UnitRow.post`, `_place`, `_APPROACH_ROWS`); `modules/mass_battle/armyrecord.py` (`order`, `validate`, `to_order_of_battle`); `engine/season/rosters.yaml` (`record_kinds.values.army`); `systems/mass_battle/sim/engine.py` (`build_envelopment`, `build_refused_flank`); `tests/valoria/test_mass_battle_order_of_battle.py`.
- TESTS (written first, read red): `tests/valoria/test_mass_battle_order_of_battle.py::test_a_left_post_starts_left_of_the_front` ("a unit posted `left` in `line` starts left of the centre line's left edge"; the name keeps the source's) and `::test_envelopment_row_equals_the_harness_builder` ("an army with `formation: envelopment` starts with both wings wide of the centre, and the harness's own envelopment builder produces the same starting cells").
- FALSIFIER and CONTROL: "a formation whose season deployment differs from the harness's for the same row". Control: `formation: line` and no posts reproduce today's placement: the seed-0 field hash equal to B19.17's.
- GATE: `python -m pytest tests/valoria/test_mass_battle_order_of_battle.py tests/valoria/test_mass_battle_army_record.py -q` → pass; `python tools/export_troops.py --check` → exit 0; the seed-0 field hash equal to B19.17's.
- HASH MOVERS: none at `line` with default posts.
- DEPENDS ON: V12 B19.17; EXISTS-IN-TREE `orderofbattle.py::_place` (`:180`), `_APPROACH_ROWS` (`:67`), `OrderOfBattle` (`:98`), `systems/mass_battle/sim/engine.py::build_envelopment`, `::build_refused_flank`, `armyrecord.py::new` (`:43`, the `strategy` key).
- GLOSSARY: rows *post* (owner column → `references/troops.yaml: formations.<name>.posts`; the proposed `front` is now `centre`, S-6 closed), *army formation* (owner → `formations`), *approach* (the MB "opening distance" owner → `formations.<name>.opening_rows`), in this commit.
- NAMES: `Subformation` → `UnitRow`; `subformations` → `units` (B16L); post `front` → `centre` (S-6); "general" → commander (S-1).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B19's producer; `Item: B19.18`, `[skip ci]`.

### B19.19 — the read that names a subformation · `MB_LEXICON_part3.md` L1-6 · BUILD · HASH EQUAL
- SOURCE: `unified/MB_LEXICON_part3.md` §4 L1 table row L1-6, D-1; `V12_STRUCTURE.md` §2.2 B19 row ("L1-6 after that file's §3"); A-59, A-94.
- ADVANCES: A-59's word in code (no row).
- INSTRUCTION (copied): "add the read **`orderofbattle.subformations(oob) -> tuple[(post, tuple[unit name, ...]), ...]`** — only after `04_MB_cell_hierarchy_as_data.md` §3 lands the `post` column (B19)". A subformation is "a group of units at one post of the army formation, fighting by one set of tactics, led by the officer its units name when one man leads them all"; "a subformation is **read** over unit rows (A-2: a unit is a row; nothing new is stored)". Where the units at one post name different officers it is still one subformation (D-1's `[ASSUMPTION, reversible]`). Add it to `__all__`.
- WHERE: `modules/mass_battle/orderofbattle.py` (`subformations`, `__all__`); `tests/valoria/test_mass_battle_order_of_battle.py`.
- TESTS: `tests/valoria/test_mass_battle_order_of_battle.py::test_subformations_group_units_by_post` `[ASSUMPTION: test name; the item creates it, E-3]`: an order of battle with two units at `left` and one at `centre` reads `(('centre', (…,)), ('left', (…, …)))` in post order; red before.
- FALSIFIER and CONTROL: a subformation that is stored rather than read (a new field on `OrderOfBattle`). Control: the hash equal to B19.18's.
- GATE: `python -m pytest tests/valoria/test_mass_battle_order_of_battle.py -q` → pass; `git grep -n -w "subformations" -- modules/mass_battle` → only the new read and its `__all__` entry.
- HASH MOVERS: none.
- DEPENDS ON: V12 B19.18 (`UnitRow.post`); V12 Batch B16L (L1-1, L1-2 freed the name).
- GLOSSARY: row *subformation* (§J): owner column → `orderofbattle.subformations` (L1's glossary line, STAGES rule 2).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B19's producer; `Item: B19.19`, `[skip ci]`.

### B19.20 — the scale written once · `26_MASS_BATTLE_cell_scale_and_time` §1 · BUILD · HASH EQUAL
- SOURCE: `proposals/26_MASS_BATTLE_cell_scale_and_time.md` "The resolution, decided" §1, "Exact edits" row 1 (its §1 part), "Gate" 1, "Falsifier"; MBA §8.1 (§1 STANDS); carries S-1.
- ADVANCES: none (a stated scale; read by the report only).
- INSTRUCTION (copied): `references/troops.yaml`, in the `deployment` header B19.17 adds:
  ```yaml
  deployment:
    cell_troops: 16          # that proposal's seed; this is why
    scale:                   # what the numbers stand for. Read by the report; by no resolver.
      cell_m: 4              # 16 men at about 3 ft of front and of depth each: four files by four ranks (MV F1)
      tick_s: 4              # one cell at an ordinary marching pace (MV M3; snippet tier: a seed)
      bout_ticks: 18         # ROUTE_BUDGET_TICKS; a bout is one clash, about seventy seconds
      bout_minutes: 30       # a bout and the stand-off before the next, as the report tells it
    max_bouts: 1             # the control: today's field. Seed for the flip: 6
  ```
  "The 50 m tile and 5-minute turn are not adopted." `tools/export_troops.py` carries `scale` and `max_bouts` into `troops.json`. No resolver reads `scale` (the falsifier).
- WHERE: `references/troops.yaml` (`deployment.scale`, `deployment.max_bouts`); `tools/export_troops.py`; `engine/engine_params/troops.json`.
- TESTS: `tests/valoria/test_export_troops.py::test_no_resolver_reads_the_scale` `[ASSUMPTION: test name; the item creates it, E-3]`: a grep of `modules/mass_battle` for `scale']`/`.scale` reads of the troop header finds none outside the report; green.
- FALSIFIER and CONTROL: "a resolver constant that reads `scale`". Control: the hash equal to B19.19's.
- GATE: `python tools/export_troops.py --check` → exit 0; `python -m pytest tests/valoria/test_export_troops.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B19.17 (the `deployment` header); EXISTS-IN-TREE `config.ROUTE_BUDGET_TICKS`.
- GLOSSARY: rows *field tick*, *bout*, *battle* (the clock table, §K): owner columns → `troops.yaml: deployment.scale.tick_s`, `.bout_ticks`, `deployment.max_bouts`.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B19's producer; `Item: B19.20`, `[skip ci]`.

### B19.21 — per-arm missile ranges and the opening-distance rule, at control · `26_MASS_BATTLE_cell_scale_and_time` §2 · BUILD · HASH EQUAL
- SOURCE: the same file, §2 (NARROWED by MBA-05: the ranges are kept and are what the range bands divide), "Exact edits" rows 1–2, "Gate" 1–4, "Tests (W3-1)"; carries B-9, R-5.
- ADVANCES: R-04.c4 (a missile phase before contact), through the flips B19.24, B19.25.
- INSTRUCTION (the data and the rule, each shipped at its control; the flips are B19.24 and B19.25, "each flip ... its own commit"):
  1. `arms.<key>.range`: a second column of values the flip selects, copied:
     | arm | range, cells | ground | tier |
     |---|---|---|---|
     | `javelin` | `[1, 6]` | 20–25 m for the heaviest javelins | `[T]` ACOUP |
     | `bow`, `crossbow` | `[2, 40]` | about 200 m; some say 300 for the longbow | `[T]` W-CRE |
     | `sling`, `siege` | `[2, 8]` | **not established**; today's value kept | — |
     "`[2, 8]` for every arm stays as the control arm." Shipped here at `[2, 8]` for every arm, with the sourced values written beside each as `range_stated` `[ASSUMPTION: the two values sit in one row so the flip is one key — basis: the source's "each flip its own commit"]`.
  2. "`formations.<name>.opening_rows` ... becomes a rule with a floor: the longest `range[1]` among the missile arms on either side, capped so both lines fit the field, floor 3. Two armies with no missiles start three rows apart as now." Shipped as `opening_rows: 3` with the rule implemented behind the value `auto` (`orderofbattle._place`: "reads the approach rule; `_APPROACH_ROWS` becomes the floor's default").
  3. "`volleys` per arm (`…_B.md`) stays 10 for both until Jordan sets it." "A volley is a tick's worth" is NARROWED by MBA-05 (the second half: `shots_per_tick`); not edited here.
- WHERE: `references/troops.yaml` (`arms.<key>.range`, `range_stated`; `formations.<name>.opening_rows`); `tools/export_troops.py`; `engine/engine_params/troops.json`; `modules/mass_battle/orderofbattle.py` (`_place`: the `auto` rule); `tests/valoria/test_mass_battle_ammo.py`.
- TESTS (written here, read at the flips): `tests/valoria/test_mass_battle_ammo.py::test_bows_shoot_before_contact` (gate 2: "Bows at `[2, 40]` against foot, n 200: volley events before first contact are above zero in every field; with the control ranges they are at most two ticks' worth"; it sets the stated ranges in-process, so it is green here), `::test_javelin_range_is_six` (gate 4: "A javelin body does not shoot at an enemy seven cells off; a bow body does"; in-process), `::test_a_body_in_contact_does_not_volley` (gate 3: "An archer body with no switch order: its volley count after its first tick in contact is zero (with the contact rule of `…_B.md` as amended)"); `tests/valoria/test_mass_battle_order_of_battle.py::test_opening_rows_auto_is_the_longest_missile_range_with_a_floor` `[ASSUMPTION: test name; the item creates it, E-3]`.
- FALSIFIER and CONTROL: "shooting through a melee by the body being fought". Control: gate 1, "every range `[2, 8]`, approach 3: `tools/ci_golden_modes_check.py` digests equal" (as B19.12 left them: the seed-0 field hash equal to B19.20's).
- GATE: `python -m pytest tests/valoria/test_mass_battle_ammo.py tests/valoria/test_mass_battle_order_of_battle.py -q` → pass; `python tools/export_troops.py --check` → exit 0; the seed-0 field hash equal to B19.20's.
- HASH MOVERS: none at control.
- DEPENDS ON: V12 B19.18 (`formations`), B19.20; V12 Batch B17 (`arms.<key>.range`, `volleys`, `volleys_spent`, the contact rule, `04_MB_unit_loadout_and_weapon_in_hand_B.md` §2); EXISTS-IN-TREE `orderofbattle.py::_place`, `_APPROACH_ROWS`.
- GLOSSARY: row *approach*: the MB opening distance's owner → `formations.<name>.opening_rows` with `auto` (one sentence: "the opening distance: how many rows apart two armies start").
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B19's producer; `Item: B19.21`, `[skip ci]`.

### B19.22 — a battle is bouts with lulls: the bout loop inside `resolve_field`, at one bout · `26_MASS_BATTLE_cell_scale_and_time` §3 · BUILD · HASH EQUAL (at `max_bouts: 1`)
- SOURCE: the same file, §3 (Reconciled W3-1, 7b-15 Option A; `hol` §44.3), "Exact edits" rows 3–6, "Gate" 1, 5, 6, "Tests (W3-1)", "Falsifier"; U3 §4.1 row 65 (the lull's `CommanderAction` LATER, B20); D-U1-11e (`bouts` is this file's `FieldOutcome` field); A-1, A-3, A-9, A-30; carries R-6.
- ADVANCES: R-04.c4 (fewer drawn fields once flipped, B19.26); A-3's end state read at the last bout.
- INSTRUCTION (copied, S-1 and S-10 applied):
  1. "A field scene is **one** call of the one entry, `massbattle.resolve_field`, which loops over at most `max_bouts` bouts (an input field). A later bout is fought when the one before ended drawn and neither commander withdrew. The loop carries three things in its own frame from bout to bout: each part's surviving troops, each part's stamina (a share in [0, 1] at the boundary, U1 §3), each part's morale. Nothing else is state, and nothing is held on the wrapper; every draw of a bout is keyed `(field, bout, tick, unit, purpose)` (A-30)."
  2. "`modules/mass_battle/massbattle.py::resolve_field` gains `max_bouts` (from `MassBattleInput`) and the bout loop: run a bout, read its end state, on drawn and no withdrawal open a lull window (the decider's `CommanderAction` set plus `relieve`, `reform`, `commit`), build the next bout from the carried troops, stamina and morale held in the loop's frame, stop at a decision or at `max_bouts`." In B19 the lull window applies **standing orders only**: the decider's `CommanderAction` and the three lull rows are `04_MB_manager_battle_one_resolver.md` §4 and `26_MASS_BATTLE_maneuver_orders.md` (B20; U3 §4.1 row 65: "until then the lull applies standing orders only"). "Rested columns recover in the lull by the column ledger's existing between-turn rule."
  3. "`engine/season/queries/inputs.py::MassBattleInput`: `entry_stamina`, entry troops and entry morale may be given per part (the per-side form of `16_PESSIMIST_MB_one_stamina_ledger.md` is the one-part case)" — here the field `max_bouts: int = 1` is added; the per-part entry fields are declared with `entry_stamina` itself in B31 (step 3 of the ledger file; Patched: P-10: step 3 is now B19.28, earlier in this batch), since `entry_stamina` does not exist before it `[ASSUMPTION: the per-part form lands with the field it widens — basis: D-U1-11e, each field lands with its proposal]`; the bout loop carries the parts in its frame without an input field.
  4. "`engine/season/seam/wrappers/mass_battle.py::resolve` calls the entry once and reads one band; forwards `host.decide` as the `decide` parameter (no loop, no state)." `FieldOutcome` gains `bouts: int` (D-U1-11e). The scene's end state is A-3's, read at the last bout: won, lost, or drawn when the bouts run out. "One resolver (ruling A-1): every bout is the same bout function inside the one entry." "`run_multi_turn_battle` is not revived."
  5. Not here: "`report` is per bout; a duration line is `bouts x bout_minutes`" (B19.27, BLOCKED: `report` is B20's).
- WHERE: `modules/mass_battle/massbattle.py` (`resolve_field`: the bout loop); `engine/season/queries/inputs.py` (`MassBattleInput.max_bouts`; `FieldOutcome.bouts`); `engine/season/seam/wrappers/mass_battle.py` (`resolve`, `field_input`: `max_bouts` from the troop file's `deployment.max_bouts`); `engine/season/tests/test_mass_battle_module.py`.
- TESTS (`engine/season/tests/test_mass_battle_module.py`, written first): `::test_the_wrapper_calls_the_entry_once` (green here); `::test_a_bout_1_decision_equals_the_one_bout_run` (gate 5's last clause: "a field decided in bout 1 is field-for-field equal to the one-bout run"; green here); `::test_max_bouts_lowers_the_drawn_share` (gate 5: "`max_bouts: 6` on an even field, seeds 0 to 199 against the same seeds at 1: the share of fields ending `Drawn` falls; no field calls the entry more than six times"; sets 6 in-process, green here); `::test_six_bout_replay_from_interventions_is_equal` (gate 6) needs `FieldOutcome.interventions` (B20) and is written in B20's item `[the arm moved, §5.8]`.
- FALSIFIER and CONTROL: "A second battle loop anywhere under `modules/` beyond the bout loop inside `resolve_field`; a loop or carried state on the wrapper; a bout whose input carries anything but troops, stamina and morale." Control: gate 1, `max_bouts: 1`: digests equal; the seed-0 field hash equal to B19.21's.
- GATE: `python -m pytest engine/season/tests/test_mass_battle_module.py tests/valoria/test_army_battle.py -q` → pass; `git grep -n "for .* in range(.*max_bouts" -- modules engine/season/seam` → the one loop in `massbattle.py`; the seed-0 field hash and `python -m engine.season.harness.aperture 1 --seeds 0` realm hash (`HASH READING`) equal to B19.21's (`FieldOutcome` is a module outcome; a field that `_eff_march` folds is unchanged at one bout).
- HASH MOVERS: none at `max_bouts: 1`.
- DEPENDS ON: V12 Batch B17 (`FieldOutcome`, `04_MB_typed_outcome_and_one_path`; `resolve_field` as the one entry); V12 B19.08 (the one stamina ledger the loop carries), B19.21; V12 Batch B20 for the lull's `CommanderAction` (`04_MB_manager_battle_one_resolver.md` §4; LATER) and `interventions`; EXISTS-IN-TREE `massbattle.py::resolve_field` (`:473`), `seam/wrappers/mass_battle.py::resolve`, `::field_input`.
- GLOSSARY: rows *bout* and *lull* (§J): owner columns → `massbattle.resolve_field` (the bout loop) and `deployment.max_bouts`; "engagement" for a bout refused (S-10).
- NAMES: `GeneralAction` → `CommanderAction` (S-1); "season round" → season (the source's own Reconciled line); `max_turns` → `max_ticks` (B16M) where the bout calls `run_battle`; `harness/populated.py::build_realm` → `boot/realm.py` (B03c) in any probe.
- COST and TIER: small build; `sonnet`, `high`; the drawn-share reading `haiku` read by `opus` (the source).
- LANDS IT: B19's producer; `Item: B19.22`, `[skip ci]`.

### B19.23 — flip: `deployment.arm: grid` · `04_MB_cell_hierarchy_as_data` (the flip) · BUILD · HASH MOVER(behaviour)
- SOURCE: `04_MB_cell_hierarchy_as_data.md` Reconciled (1) ("the `arm: grid` flip is a step of the one field calibration batch and lands **after** the pair rule changes"), "Gate" 2, 3, 6, "Falsifier", "Hash movers"; UMR §6 row 4 ("the partition row is read **before** the grid arm").
- ADVANCES: R-04.c5 (ii) (a field fought on blocks with depth); R-04.c4.
- INSTRUCTION: `references/troops.yaml: deployment.arm: cap` → `grid` (revert: `cap`); re-export. "After this change a preset army is some forty to sixty cells in blocks two to four ranks deep (the sourced seeds)". Gate 6: "The law instrument and the gauge are re-read after the flip, because they and the season then fight the same bodies; their readings are reported, not gated."
- WHERE: `references/troops.yaml` (`deployment.arm`); `engine/engine_params/troops.json`.
- TESTS: none new; `test_depth_is_a_lever` (B19.17) re-read on the shipped arm.
- FALSIFIER and CONTROL: "After the flip, a season-built foot unit of 200 or more troops in one rank"; "any gate above read as a balance target". Control: `arm: cap` (B19.22's reading).
- GATE: `python systems/mass_battle/sim/cells_probe.py` → "for the weight-20 preset army, blocks of at least two ranks [depth] for every foot unit (the sourced seeds) and an army of at least thirty cells" (gate 2); `python systems/mass_battle/sim/pike_probe.py` → "the count of fields identical between a pike line and a heavy-infantry line is below 200 of 200 (today 440 of 440)" (gate 3); `PYTHONHASHSEED=0 python -m systems.mass_battle.sim.lanchester_signature` and `python tests/sim/gauge_mb.py --results` → re-read and printed in the commit body (gate 6, reported); `python -m pytest tests/valoria/test_mass_battle_partition.py -q -m mass_battle` → pass on the grid; the seed-0 field hash moved, recorded.
- HASH MOVERS: "the `arm: grid` flip (every army field)". Declared; `B19.99`'s re-pin.
- DEPENDS ON: V12 B19.12 (the partition row read before the grid arm), B19.17, B19.22.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high` (effort set explicitly, CLAUDE.md §10; R2c, K6 F16); the flip's readings `haiku` (`valoria-measure`), `high`, read by `opus`, `high` (the source).
- LANDS IT: B19's producer; `Item: B19.23`, `[skip ci]`.

### B19.24 — flip: the per-arm ranges · `26_MASS_BATTLE_cell_scale_and_time` §2 (flip 1) · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, §2, "Gate" 2, 4, "Hash movers" ("each flip (`range`, `opening_rows: auto`, `max_bouts: 6`) its own commit").
- ADVANCES: R-04.c4 (shooting before contact).
- INSTRUCTION: every arm's `range` takes its `range_stated` value (B19.21's table: `javelin` `[1, 6]`, `bow` and `crossbow` `[2, 40]`, `sling` and `siege` `[2, 8]`); revert: `[2, 8]` for every arm. Re-export. MBA-05 (the second half) reads these ranges through the range bands.
- WHERE: `references/troops.yaml` (`arms.<key>.range`); `engine/engine_params/troops.json`.
- TESTS: B19.21's three `test_mass_battle_ammo.py` tests re-read on the shipped values.
- FALSIFIER and CONTROL: a javelin body shooting at seven cells; volleys before contact at zero with bows on the field. Control: B19.23's reading at `[2, 8]`.
- GATE: `python -m pytest tests/valoria/test_mass_battle_ammo.py -q` → pass; `python tools/export_troops.py --check` → exit 0; the seed-0 field hash moved, recorded.
- HASH MOVERS: every army field with a missile arm. Declared; `B19.99`.
- DEPENDS ON: V12 B19.21, B19.23.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high` (effort set explicitly, CLAUDE.md §10; R2c, K6 F16).
- LANDS IT: B19's producer; `Item: B19.24`, `[skip ci]`.

### B19.25 — flip: `opening_rows: auto` · `26_MASS_BATTLE_cell_scale_and_time` §2 (flip 2) · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, §2 (the opening rule), "Hash movers"; `04_MB_cell_hierarchy_as_data.md` "Conflicts" (`ED-MB-0080`'s stress finding bears on `opening_rows`).
- ADVANCES: R-04.c4 ("An army facing bows starts in range and must cross it").
- INSTRUCTION: `formations.<name>.opening_rows: 3` → `auto` for `line`, `envelopment`, `refused_flank` (revert: 3). Re-export.
- WHERE: `references/troops.yaml` (`formations.<name>.opening_rows`); `engine/engine_params/troops.json`.
- TESTS: `test_opening_rows_auto_is_the_longest_missile_range_with_a_floor` (B19.21) re-read on the shipped value.
- FALSIFIER and CONTROL: two armies with no missiles starting more than three rows apart. Control: B19.24's reading.
- GATE: `python -m pytest tests/valoria/test_mass_battle_order_of_battle.py tests/valoria/test_mass_battle_ammo.py -q` → pass; the seed-0 field hash moved (where a missile arm fights), recorded.
- HASH MOVERS: every army field with a missile arm on either side. Declared; `B19.99`.
- DEPENDS ON: V12 B19.21, B19.24.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high` (effort set explicitly, CLAUDE.md §10; R2c, K6 F16).
- LANDS IT: B19's producer; `Item: B19.25`, `[skip ci]`.

### B19.26 — flip: `max_bouts: 6` · `26_MASS_BATTLE_cell_scale_and_time` §3 (flip 3) · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, §1 (`max_bouts: 1 # the control ... Seed for the flip: 6`), §3, "Gate" 5, "Hash movers".
- ADVANCES: R-04.c4 (fewer drawn fields: "Cut the bouts and the field is a draw machine or an attrition machine").
- INSTRUCTION: `deployment.max_bouts: 1` → `6` (revert: 1). Re-export. Until B20 the lull applies standing orders only (B19.22).
- WHERE: `references/troops.yaml` (`deployment.max_bouts`); `engine/engine_params/troops.json`.
- TESTS: `test_max_bouts_lowers_the_drawn_share` and `test_a_bout_1_decision_equals_the_one_bout_run` (B19.22) re-read on the shipped value.
- FALSIFIER and CONTROL: the drawn share not falling; a field calling the entry more than six times. Control: B19.25's reading at `max_bouts: 1`.
- GATE: `python -m pytest engine/season/tests/test_mass_battle_module.py -q` → pass; `PYTHONHASHSEED=0 python -m engine.season.harness.aperture 1 --seeds 0 1 2` → `field.won`, `field.lost`, `field.drawn` per seed quoted beside B19.25's (`reading @<sha>`); the seed-0 field hash moved, recorded.
- HASH MOVERS: every army field that is drawn after one bout. Declared; `B19.99`.
- DEPENDS ON: V12 B19.22, B19.25.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high` (effort set explicitly, CLAUDE.md §10; R2c, K6 F16); the drawn-share reading `haiku`, `high`, read by `opus`, `high`.
- LANDS IT: B19's producer; `Item: B19.26`, `[skip ci]`.

### B19.27 — the report's named draws and the per-bout report · 27_MB_C 27C-1 (the report half) with `26_MASS_BATTLE_cell_scale_and_time` §3 (`report` per bout) · POINTER (to B20.23; lane D4, E-8)
- What it points at (E-5): 27C-1's report half ("`_grade` collects [the draw trace events] into `report.draws`"; `_eff_march` writes the draws that changed the end state as `draw:<kind>` Observations on the band Event) and cell scale's per-bout `report` with its duration line. Its one dependency, `FieldOutcome.report`, is declared by V12 B20.05 (`04_MB_manager_battle_one_resolver.md` §6 via SCN §D, D-U1-11e); B20 (S16) lands after B19 (S15), so the item joins B20 as **B20.23** (E-8: the dependency wins), where its INSTRUCTION, TESTS and GATE are written.
- Targets: `modules/mass_battle/massbattle.py::_grade`; `engine/season/queries/inputs.py::FieldReport.draws`; `engine/season/loop/effects_combat.py::_eff_march`; `engine/season/rosters.yaml: observation_terms`. GATE: B20.23's (`test_report_draws_lists_every_named_draw_that_fired`; 27_MB_C gate 6). No commit in B19.

---

SERIAL EDGES (this half, read off the position table; E-11):
  within the batch: B19.01 first (U3: "T-rows written first as the batch's tests"; every later reading is taken on its block); B19.02 → B19.03 → B19.04 → B19.05 (the record, its defaults and data, the carriers, then the draw that reads them) → B19.06 (the `obey` site exists); B19.08 → B19.28 (Patched: P-10: step 3 after step 2; `references/troops.yaml`'s `fatigue` block B19.28 → B22.03 → B31.06); B19.07 → B19.08 (the redefined `agg_stamina` is what step 2 reports) → B19.12 (`rounds_d` reads the one column share); B19.09 → B19.12 (the repaired instrument reads the contact draw's exponent, MBA §4.2); B19.10 → B19.11 → B19.12 (the seam, the pure function, the call site) → B19.13 (`exposure_d` exists) → B19.14 (no reader of the deleted constants remains) → B19.15 (the last pool reader is gone); B19.12 → B19.23 (UMR §6 row 4: the partition row is read before the grid arm); B19.17 → B19.18 → B19.19 (L1-6 needs `post`); B19.17 → B19.20 (the `deployment` header) → B19.21 (`formations` from B19.18 too) → B19.22 (B19.08's ledger carried by the loop); flips last, one commit each, in the source's order: B19.23 → B19.24 → B19.25 → B19.26; B19.27 BLOCKED to B20; the second half (B19.51 onward) follows B19.26; `B19.99` re-pins every mover of this half.
  with other batches, by file (U3 §5.1 rows, `→` landing order): `tests/sim/gauge_mb.py` B19 only (B19.01, then 27C-2 and MBA-08 in the second half); `systems/mass_battle/sim/lanchester_signature.py` B19 only (B19.09, B19.12, then 27C-3 (h)); `modules/mass_battle/core/exchange.py` B19 only (B19.07, B19.12; `derive_command`'s retirement in the second half); `modules/mass_battle/orchestration.py` B17 → B19 → B20; `modules/mass_battle/config.py` B17 → B19 → B31; `percell.py` B17 → B19 → B31; `references/troops.yaml`, `tools/export_troops.py` B17 → B19a → B19 → B20; `modules/mass_battle/troop_types/table.py` B17 → B19a → B19 → B31; `orderofbattle.py` B17 → B19 → B20; `armyrecord.py` B19 → B20; `massbattle.py` B17 → B19 → B20; `battle_loop.py` B17 → B19 → B20; `hierarchy/units.py` B17 → B19 → B20; `core/contact.py` B19 → B20; `engine/season/queries/inputs.py` B17 → B19 → B22; `seam/wrappers/mass_battle.py` B17 → B19 → B20; `engine/season/rosters.yaml` B18 → B19 → B21 (different top-level key from B18, §7.3); `battle_orders.json` B19 → B20; `sim_params.json` B19 → B24; `systems/mass_battle/sim/engine.py` B19 (B19.14's row, B19.18's builders).
FILE CENSUS (this half; NEW files): `modules/mass_battle/core/contact_draw.py`, `core/volley.py` (B19.10; callers: `orchestration.py`); `systems/mass_battle/sim/cells_probe.py`, `pike_probe.py` (B19.17; callers: B19.23's gate, named here; the accretion pass keeps them only if this plan's later gates name them, else deletes them at the close); `tests/valoria/test_mass_battle_entry_stamina.py` (B19.07), `test_mass_battle_contact_draw.py` (B19.11), `test_mass_battle_partition.py` (B19.12).

The last item this part wrote: B19.27. The second half begins at B19.51.
