# Workplan v12 — part 44, continued: batch B98-dials, from B98.23

## Status: PROPOSED (the continuation of part 44's batch B98-dials; drafted under `master/workplan_v12/`; unratified until Jordan adopts v12; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

The batch block's head (the GATE lines, BATCH GATE, RE-PIN, IDS, UNDECIDED U1 to U9, the reads `HASH`, `FIX` and the control arm, C, COST, EST), its position table and items B98.01 to B98.22 are in `workplan_v12_part44.md`. Paths, words and reads as stated there.

---

### B98.23 — wear stays a rate: the draw has no pool or obstacle values · row 29; B12a.10; `09_WR_B_draws_not_thresholds` edit 1, gate (2) · BLOCKED (design: no value stated) · HASH EQUAL
- SOURCE: part 2 §4 row 29 (TARGETED there; corrected here, U9); B12a.10: "The two `[CALIBRATE]` rows are fixtures `wear_draw_pool` and `wear_draw_ob_step`, shipped `None` … with `wear_draw: True` and either `None`, the loop refuses with `Unspecified` naming the row (E-14 …; B98 sets them)"; `proposals/09_WR_B_draws_not_thresholds.md` edit 1 ("`[CALIBRATE: the wear pool and the obstacle's per-point size, joint calibration, OWED §B]`") and its Reconciled line (each such row "set by the one joint calibration of A-5/A-6/A-7/A-26/A-31 (`OWED_TO_UNIFICATION.md` §B last bullet), not here"). No source, and no batch's item, states a value or a sweep for either row (`grep -l wear_draw_pool` over the body parts finds B12a.10 and part 2 only).
- SETTINGS: `engine/season/data/fixtures.py` (`wear_draw` = `False`; `wear_draw_pool`, `wear_draw_ob_step` = `None`).
- TARGET, recorded for the owner: gate (2) at two seasons, "under `wear_draw: True`, two harbours of equal condition and kind diverge within four seasons at some seed, and the realm's mean wear over eight seasons at three seeds lies within the control's rate ± its own spread" (four and eight seasons in the source; A-114).
- INSTRUCTION: none; flip nothing (U9). OWNER OF THE VALUES: the joint calibration of A-5/A-6/A-7/A-26/A-31 for a draw with no person rolling (WR lane); no batch carries it.
- GATE: `FIX(wear_draw)` → `False`; `FIX(wear_draw_pool)`, `FIX(wear_draw_ob_step)` → `None` (R2). B99 QUOTES: wear as a rate; R-09's draws do not include it.
- DEPENDS ON: V12 Batch B12a, B12a.10. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.24 — endings stay reached by crossing: the draw has no pool or obstacle values · row 30; B12a.12; `09_WR_B_draws_not_thresholds` edit 3, gate (3) · BLOCKED (design: no value stated) · HASH EQUAL
- SOURCE: part 2 §4 row 30 (TARGETED there; corrected here, U9); B12a.12: "the two `[CALIBRATE]` rows as fixtures `ending_draw_pool_step` and `ending_draw_ob`, shipped `None`; with `ending_draw: True` and either `None`, `endings_reached` refuses with `Unspecified` naming the row"; edit 3: "`[CALIBRATE: both, joint calibration, OWED §B]`". No value or sweep is stated anywhere.
- SETTINGS: `engine/season/data/fixtures.py` (`ending_draw` = `False`; `ending_draw_pool_step`, `ending_draw_ob` = `None`).
- TARGET, recorded: gate (3), "a planted world meeting a holds row's condition reaches it at some seeds and not others over 200 seeds, and more often the longer the condition has stood" (a planted world, no season run).
- INSTRUCTION: none; flip nothing (U9). OWNER OF THE VALUES: as B98.23.
- GATE: `FIX(ending_draw)` → `False`; the two rows → `None` (R2). B99 QUOTES: endings reached by crossing.
- DEPENDS ON: V12 Batch B12a, B12a.12. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.25 — `arrival_report` stays off · row 31; B12a.16; `07_SE_kernel_repairs` D · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 31; B12a's `DIALS AT CONTROL` line (part 19): "no source names a setter or a calibration (`07_SE_kernel_repairs` D ships it off and names only its test) … `BLOCKED (design: no target reading)` unless B98's author reads D's test as the target". Read: D's test is the item's falsifier at ship, not a reading of the realm; taken as no target (U4's "changes less").
- SETTING: `engine/season/data/fixtures.py` (`arrival_report`) = `off` (B12a.16).
- INSTRUCTION: none. OWNER OF THE TARGET: the SE lane (a realm reading of what arriving teaches).
- GATE: `FIX(arrival_report)` → `'off'` (R2). B99 QUOTES: the value as left.
- DEPENDS ON: V12 Batch B12a, B12a.16. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.26 — `APPROACH_SIGMA_K` stays 0: a ruling on the coefficient is owed · row 32; B16.08; PB §7 step 3c, §11 · BLOCKED (design: no value stated) · HASH EQUAL
- SOURCE: part 2 §4 row 32 ("TARGETED, with a ruling on the coefficient"; corrected here, U9); B16.08 ("`APPROACH_SIGMA_K=0.0`, tagged `[SIM-CALIBRATE]`, its comment naming B98"); `proposals/03_PC_duel_round_and_approach_B.md` (PB) §7 row 3c: "at 0, byte-identical; at the chosen value the nine-cell arming mirror is level within the control band, mean rounds are monotone in the summed lean, and the undecided share is reported"; the D-40 reconciliation: "no coefficient is chosen before the calibration batch"; §11: "Step 3c: small build plus a calibration pass on the workbench and a ruling on its coefficient". PB names no candidate value.
- SETTING: `modules/combat/config.py` (`CFG['APPROACH_SIGMA_K']`) = 0.0, exported in `engine/engine_params/combat_engine_v1.json`.
- TARGET, recorded: PB §7 row 3c above, on `systems/combat/combat_engine_v1/workbench/approach_policy_probe.py`.
- INSTRUCTION: none; flip nothing. OWNER OF THE VALUE: Jordan's ruling (PB §11), on candidate values the PC lane's workbench pass proposes.
- GATE: `python -c "from modules.combat.config import CFG; print(CFG['APPROACH_SIGMA_K'])"` → `0.0`; `python tools/export_engine_params.py --check` → exit 0 (R2). B99 QUOTES: the value as left.
- DEPENDS ON: V12 Batch B16, B16.08. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.27 — a journey is priced by its route · row 33; B12b.02, B12b.04; CP-T10-01 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 33 ("TARGETED (direction only)"); B12b's `DIALS AT CONTROL` line (part 24): "CP-T10-01's paired arm (on against off, seeds 0–2, two seasons): executed `move`s to a place other than the mover's own rise, and acts per acting person are quoted (`master/eval/E1.md` CP-T10-01, 'Control') — the card states the direction, not a size"; CP-T10-01's entry (`master/eval/E1.md`): on the on arm `_relocate` appends `(dest, points, path)` to `Person.travel_leg` and "`budget.py:60` subtracts the sum of points × `budget_leg_penalty`"; `proposals/09_WR_B_weather_with_memory_and_the_year.md` edit 3 "does nothing until it flips".
- SETTING: `engine/season/data/fixtures.py` (`route_pricing`) = `"off"` (B12b.02). New value: `"on"` (a two-member switch, U9). `leg_unit` keeps its `[ASSUMPTION: 2.0]`.
- INSTRUCTION: read both arms, seeds 0 to 2, two seasons, in-process (`run(2, s, w=w)` with the sweep): executed `move`s to a place other than the mover's own rise, and acts per acting person, per seed. Rule: the direction the card's mechanism gives `[ASSUMPTION: on the on arm executed moves to another place fall and acts per acting person do not rise, at every seed — basis: a leg's points are subtracted from the budget (CP-T10-01, "Adds"); the card states no size]`. If it holds, `route_pricing` → `"on"`.
- FALSIFIER and CONTROL: `test_route_leg.py` (S-001 → S-002 prices 1 point). Control arm: `HASH(0, 2; route_pricing = "off")` equals B98.22's after-reading (that is, B98.21's).
- GATE: `python -m pytest engine/season/tests/test_route_leg.py -q` → pass; the two arms' figures per seed quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every world with a journey (a leg costs budget). EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `route_pricing` → `"off"`.
- DEPENDS ON: V12 Batch B12b, B12b.02, B12b.04, B12b.10.
- COST and TIER: calibration; `sonnet`, high; `opus` reads the direction. LANDS IT: B98's producer; `Item: B98.27`, `[skip ci]`.

### B98.28 — the territory yield scale stays empty and the tensions stay unbuilt · row 34; B12b.45, B12b.46; CL-EVENTS (4) · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 34; B12b's `DIALS AT CONTROL` line: "target: none stated (CL-EVENTS (4): 'the switch staying off'; its on-arm reading 'names no target')".
- SETTINGS: `engine/season/data/fixtures.py` (`territory_yield_scale`) = `()`; `boot/realm.py::build_realm` (`tensions=False`).
- INSTRUCTION: none. OWNER OF THE TARGET: CL-EVENTS (WR lane).
- GATE: `FIX(territory_yield_scale)` → `()`; `build_realm`'s `tensions` default → `False` (R2). B99 QUOTES: both as left.
- DEPENDS ON: V12 Batch B12b, B12b.45, B12b.46. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.29 — the year's spell is drawn · row 35; B12b.03; `09_WR_B_weather_with_memory_and_the_year` edit 1, gate (4), edit 2 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 35; B12b.03: "`season_spell_draw=(),        # R-27: the year's regional obstacle terms, equally likely; swept () (control) / (-1, 0, +1)  [ASSUMPTION; medium; Jordan to correct]`"; `proposals/09_WR_B_weather_with_memory_and_the_year.md` "The gate that shows it worked" (4): "under the live arm with spells, at three seeds over eight seasons, at least one territory reads `shortfall` in two consecutive seasons (a hard spell raising the obstacle for a year), using CR-73's reading, and the same territory does not do so at every seed (the draw did not collapse into a threshold)"; edit 2's mean-one reading (part 24's R1: "the calibration target is a mean of one"). Read at two seasons (eight in the source; A-114). The gate's `(0.6, 1.0, 1.4)` is the withdrawn multiplier form; B12b.03's `(-1, 0, +1)` is the reconciled one.
- SETTING: `engine/season/data/fixtures.py` (`season_spell_draw`) = `()`. New value: `(-1, 0, +1)` (B12b.03's swept arm, `[ASSUMPTION; medium; Jordan to correct]`, U7).
- INSTRUCTION: read gate (4) and the mean harvest factor at `(-1, 0, +1)`, seeds 0 to 2, two seasons, in-process; if gate (4) holds and the mean harvest factor per seed lies inside the control's seed-to-seed spread (R1's form, B12b.43's table its before-reading), `season_spell_draw` → `(-1, 0, +1)`.
- FALSIFIER and CONTROL: edit 2's falsifier ("the recorded mean harvest factor … departs from one by more than the control's own seed-to-seed spread, and the factors are nevertheless shipped"); gate (3) (the spell a function of `(seed, year, region)` only). Control arm: `HASH(0, 2; season_spell_draw = ())` equals B98.27's after-reading.
- GATE: `python -m pytest engine/season/tests/test_season_weather.py engine/season/tests/test_season_weather_per_territory.py -q` → pass; gate (4)'s territory per seed and the mean harvest factor per seed quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every seeded world (every territory's draw takes the year's spell). EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers; `test_season_weather.py`'s pins where the shipped arm moves them.
- REVERT: `season_spell_draw` → `()`.
- DEPENDS ON: V12 Batch B12b, B12b.03, B12b.43 (the drawn form live); CR-73's `shortfall` reading (B12b, PROPOSED).
- STOPS IF: two seasons fall inside one year of `rosters.yaml: seasons_of_year` so no second year's spell is drawn: gate (4)'s "two consecutive seasons" is then read inside the one year and said so.
- COST and TIER: calibration; `sonnet`, high; `opus` reads gate (4). LANDS IT: B98's producer; `Item: B98.29`, `[skip ci]`.

### B98.30 — the season's terms stay at 1.0 · row 36; B12b.01; CP-T10-03 · BLOCKED (content: the winter values are Jordan's) · HASH EQUAL
- SOURCE: part 2 §4 row 36; B12b's `DIALS AT CONTROL` line: "`season_terms` = 1.0 on every multiplier and `hardship` 0 (B12b.01's control); … CP-T10-03's winter values are `[ASSUMPTION; medium; Jordan to correct]`, no reading — … unless Jordan names the values".
- SETTINGS: `engine/season/rosters.yaml` / `data/fixtures.py` (`season_terms`, every multiplier 1.0; `hardship` 0), as B12b.01 placed them.
- INSTRUCTION: none. OWNER OF THE VALUES: Jordan (D-19); listed in the PR body.
- GATE: the `season_terms` multipliers and `hardship` read on the closing tree → 1.0 and 0 (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B12b, B12b.01. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.31 — shares, hunger loss and regrowth stay at control · rows 37 to 39; B12b.19, B12b.35, B12b.36, B12b.38 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 rows 37 to 39; B12b's `DIALS AT CONTROL` lines.
- SETTINGS, in `engine/season/data/fixtures.py`, each with its reason:
  (37) `amount_shares` = `["1000"]` (B12b.19): "flipped 'only after plan CP-T08-06 (`unrest`) or `U5d_SE_cohort_heavy_moves_and_caste.md` gives the largest share a consequence path'; CP-T08-06 is HELD, B12b.26; target: none stated for the realm".
  (38) `hunger_loss` = `per_cohort`, `famine_loss` = 0 (B12b.35, B12b.36): "a reading at CR-22's exit, not a pass condition" (`07_SE_population_census.md` §5).
  (39) `regrow_seasons` = 0 (B12b.38): "a reading, not a pass condition" (`07_SE_population_regrowth_B.md` §5).
- INSTRUCTION: none. OWNER OF THE TARGET: (37) CP-T08-06 when it unholds; (38), (39) the SE lane.
- GATE: `FIX(amount_shares)` → `['1000']`; `FIX(hunger_loss)` → `'per_cohort'`; `FIX(famine_loss)` → 0; `FIX(regrow_seasons)` → 0 (R2). B99 QUOTES: the four as left, with the realm count of `empty` settlements at B99's horizon (the reading `07_SE_population_census.md` §5 names).
- DEPENDS ON: V12 Batch B12b, B12b.19, B12b.35, B12b.36, B12b.38. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.
