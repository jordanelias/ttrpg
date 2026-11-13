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

### B98.32 — `management_orders` stays empty · row 40; B34.10; `IS-B3-GO-07` · BLOCKED (content: CL-MGMT's list, held) · HASH EQUAL
- SOURCE: part 2 §4 row 40; B34's `DIALS AT CONTROL` line (part 25_cont): "set by: none in v12 (the list is CL-MGMT's content, held …); target: none stated (A-104 names examples, not a list)"; part 2 §8 (CL-MGMT held).
- SETTING: `engine/season/rosters.yaml` (`management_orders`) = `[]` (B34.10).
- INSTRUCTION: none. OWNER: Jordan's list, through CL-MGMT when its trigger fires (part 2 §8); listed in the PR body.
- GATE: `management_orders` in `engine/season/rosters.yaml` → `[]` on the closing tree (R2). B99 QUOTES: no management order is offered; R-04's management conjunct reads at this.
- DEPENDS ON: V12 Batch B34, B34.10. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.33 — hands and spoilage stay at control · rows 41, 42; B12c.02, B12c.03; CP-T08-01, CP-T08-03 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 rows 41, 42; B12c's `DIALS AT CONTROL` line (part 28): `labour_mode` "CP-T08-01's control and falsifier are on/off readings, not a target"; `store_spoil` "shipped all 0 [ASSUMPTION; JQ-6's family]".
- SETTINGS: `engine/season/data/fixtures.py` (`labour_mode` = `off`, B12c.02; `store_spoil` = every rate 0, B12c.03).
- INSTRUCTION: none. OWNER OF THE TARGET: JQ-6's sweep (SE lane; no batch carries it).
- GATE: `FIX(labour_mode)` → `'off'`; `FIX(store_spoil)` → every rate 0 (R2). B99 QUOTES: both as left.
- DEPENDS ON: V12 Batch B12c, B12c.02, B12c.03. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.34 — prices stay at par: no computed `offer` · row 43; B12c.16, B12c.17 (HELD); CP-T08-05 · BLOCKED (carrier: no computed producer of `offer`) · HASH EQUAL
- SOURCE: part 2 §4 row 43 ("TARGETED, while B12c.17 is HELD: BLOCKED (carrier: no computed producer of `offer`)"); B12c.16 (shipped "at the card's control: every `price_base` equal and `price_horizon` 0 (par barter)"); CP-T08-05's reading: "across seeds a rung in dearth receives more grain by `exchange` than one in surplus, two seasons".
- SETTINGS: `engine/season/rosters.yaml` (`price_base`, every value equal); `engine/season/data/fixtures.py` (`price_horizon` = 0).
- INSTRUCTION: open B12c.17's row in the plan on `main`: if it is still HELD (its trigger, "a computed producer of an `offer` Record; H-165's shape", has not fired), flip nothing.
- STOPS IF: B12c.17 has landed (its trigger fired in a later batch): the position stops and is reported, because the priced values are CP-T08-05's and this plan copies none.
- GATE: `FIX(price_horizon)` → 0; `price_base` rows → equal (R2). B99 QUOTES: barter at par.
- DEPENDS ON: V12 Batch B12c, B12c.16, B12c.17. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.35 — `craft` stays withheld · row 44; B12c.25; CP-T08-04 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 44: "'read for scene crowding before it ships'; no figure".
- SETTING: `engine/season/data/fixtures.py` (`Fixtures.withheld_verbs` holds `craft`), B12c.25.
- INSTRUCTION: none. OWNER OF THE TARGET: the SE lane (a crowding figure).
- GATE: `FIX(withheld_verbs)` → contains `'craft'` (R2). B99 QUOTES: `craft` withheld; R-05's `BUILT OUT` reads it as not formed.
- DEPENDS ON: V12 Batch B12c, B12c.25. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.36 — the upkeep payment gets its question · row 45; B12c.18; CP-T08-08 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 45; B12c.18 ("The realm reading ('seed 1, six seasons, `term.renewed` > 0') is B98's, at two seasons (A-114)"); CP-T08-08 (`master/eval/E1.md`): "Realm reading: seed 1, six seasons, `term.renewed` > 0 (0 today, T08 §5c)"; "Control. `upkeep_lead: none` (the source off) reproduces today's hashes at seeds 0-2"; "Hash movers. On: seed 1 (the only seed with act-made obliges at two seasons) …".
- SETTING: `engine/season/data/fixtures.py` (`upkeep_lead`) = `none`. New value: a whole number of seasons; the card names none (U9): the probe takes `{1, 2}` (the leads a two-season run can see).
- INSTRUCTION: at each lead, seed 1, two seasons (six in the source; A-114), in-process: the count of `term.renewed` Events. Rule (U4): the smallest lead at which it is above 0. Neither: ship nothing; B99 reads the card's six-season reading at the shipped `none` (the source off) and quotes it.
- FALSIFIER and CONTROL: `test_upkeep_question.py` on `scarce.governed` (the card's falsifier and its mutation). Control arm: `HASH(0, 2; upkeep_lead = none)` equals B98.29's after-reading; and seed 1's control hash equal to its own pre-flip reading (the card's seed).
- GATE: `python -m pytest engine/season/tests/test_upkeep_question.py -q` → pass; `term.renewed` at seed 1 per lead quoted; `HASH(0, 2)` and the seed-1 hash recorded.
- HASH MOVERS: "On: seed 1 … and any later seed that forms obliges; every seed through the widened deposit" (the card; the deposit clause ships behind the same fixture, B12c.18's assumption). EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers at seed 1, and at every seed if the deposit moves them.
- REVERT: `upkeep_lead` → `none`.
- DEPENDS ON: V12 Batch B12c, B12c.18; Batch B33 (CP-T08-07, the stocked treasury, if it landed; B33.30 HELD otherwise: the reading may then be 0 for want of stock, and says so).
- COST and TIER: calibration; `sonnet`, high; `opus` reads the count. LANDS IT: B98's producer; `Item: B98.36`, `[skip ci]`.

### B98.37 — `effect_rate_gain` stays at 0 · row 46; B12c.26; `07_SE_capability_rate_B` §4 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 46 (no target stated).
- SETTING: `engine/season/data/fixtures.py` (`effect_rate_gain`) = 0 (B12c.26).
- INSTRUCTION: none. OWNER OF THE TARGET: the SE lane.
- GATE: `FIX(effect_rate_gain)` → 0 (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B12c, B12c.26. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.38 — `CARRY_CLOSE_K` stays 0: no value is stated · row 47; B18.07; `03_PC_loadout_and_carry` Gate 2 · BLOCKED (design: no value stated) · HASH EQUAL
- SOURCE: part 2 §4 row 47 (TARGETED there; corrected here, U9); B18.07 ("`close_rate` gains `CARRY_CLOSE_K` (in `CFG`, exported, 0 shipped)"; "one new `[SIM-CALIBRATE]` coefficient in `CFG`, 0 as the control"); the source states no value and no sweep.
- SETTING: `modules/combat/config.py` (`CFG['CARRY_CLOSE_K']`) = 0, exported in `engine/engine_params/combat_engine_v1.json`.
- TARGET, recorded: "Workbench, 1,000 fights per cell, disjoint-seed control: a Strength-4 spearman carrying an arming sword against the same spearman without one shows more stamina spent and a slower close; at Strength 7 the two are inside the control band."
- INSTRUCTION: none (U9). OWNER OF THE VALUE: the PC lane's workbench calibration (`systems/combat/combat_engine_v1/workbench/balance.py`), which no batch schedules.
- GATE: `python -c "from modules.combat.config import CFG; print(CFG['CARRY_CLOSE_K'])"` → 0 (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B18, B18.07. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.39 — an order is obeyed by a draw, if B19 did not ship it · row 48; B19.68; `27_MB_C` §4; MNV gate 1 · BUILD (flip, conditional) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 48 ("IN-BATCH (27C-3's commit if it ships arm R), else TARGETED"); part 26's `DIALS AT CONTROL` line ("`orders.obey.arm` = `off`; set by 27C-3's licensed commit only if it ships arm R …, else B98; target: 27_MB_C §4's criterion, arm R's readings 1, 2 and 4"); part 30's line ("target: MNV gate 1 ('the order is applied at tick 3 in some fields, at tick 4 in some, and later or never in some; `orders_fired` records which', n 200)"); B19.68 step 5 ("`orders.obey.arm`'s shipped value is recorded in this commit's body beside arm R's reading").
- CONDITION (U5): read B19.68's commit body on `main`. If it shipped arm R with `orders.obey.arm` on, record "set by B19.68 @<sha>"; POINTER, no commit. Otherwise run.
- SETTING: `orders.obey.arm` = `off` (the 27A-2 key, B19; its home as B19's UNDECIDED (1) took it: `modules/mass_battle/config.py`, exported to `battle_orders.json`). New value: `on`.
- INSTRUCTION: on this base, `PYTHONHASHSEED=0 python3 tests/sim/gauge_mb.py --arms --n 400` (B19.68's instrument, sized first, in the background) and read arm R's readings 1, 2 and 4 with the criterion's text as B19.68 copies it ("reading 1 holds in every scenario; in reading 2 the even field is side-fair and the smaller side at 2 : 1 wins a share above zero; and all five comparisons of reading 4 exceed their band"); and MNV gate 1 at n 200. If both hold, `orders.obey.arm` → `on`; re-derive the export with its tool.
- FALSIFIER and CONTROL: B19.68's ("a scenario whose win share is 0 or 1; an even field that is not side-fair; a choice of reading 4 inside its band"). Control arm: `python tools/ci_golden_modes_check.py` with the arm `off` → every digest equal to the previous position's tree; `HASH(2, 1)` (a fought field at seed 2, CIP part 2 §5 note 3) at `off` equal to its pre-flip reading.
- GATE: the arm-R table and MNV gate 1's tick distribution quoted; `python tools/export_sim_params.py --check` (or the battle-orders exporter's `--check`) → exit 0; `HASH(2, 1)` recorded.
- HASH MOVERS: every fought field. EXPECTED RED UNTIL B98.99: the combat and field goldens, `test_field_golden_pins.py`, the `_realm_goldens` readers at seed 2.
- REVERT: `orders.obey.arm` → `off`.
- DEPENDS ON: V12 Batch B19, B19.68; Batch B20 (MNV, `orders_fired`).
- COST and TIER: calibration; `sonnet`, high; `opus` applies the criterion to the table ("not delegated down"). LANDS IT: B98's producer; `Item: B98.39`, `[skip ci]` (if it runs).

### B98.40 — `orders.obey.in_contact` stays 0 · row 49; B19 (27A-2); `27_MB_A` §4 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 49; part 26's line: "('CONTROL. Flip seed 1. [shape from MV E4; no magnitude sourced]', 27_MB_A §4)".
- SETTING: `orders.obey.in_contact` = 0 (B19's `obey` block).
- INSTRUCTION: none. OWNER OF THE TARGET: the MB lane (a magnitude for obedience in contact).
- GATE: the `obey` block's `in_contact` read on the closing tree → 0 (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B19. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.41 — an elected seat keeps its conferral fallback · row 50; B21c.03; CR-35 (8); H-80 · BLOCKED (design: no computed route; H-80) · HASH EQUAL
- SOURCE: part 2 §4 row 50; part 25's `DIALS AT CONTROL` line: "`FILLED_BY["elected"]` keeps `CONFERRAL` if B21c.03 STOPS …; target: 'the elected narrowing waits until an election executes' (CR-35 (8)), which H-80 keeps unreachable".
- SETTING: `FILLED_BY["elected"]` (B21c.03's owner), only if B21c.03 stopped.
- INSTRUCTION: read B21c.03's commit or its STOPPED record: if it did not stop, this position records "not a member" and closes; else flip nothing.
- OWNER OF THE TARGET: an election that executes in computed play (H-80).
- GATE: `FILLED_BY["elected"]` read on the closing tree (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B21c, B21c.03. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.42 — the Church Influence bands and the untested triggers stay off: their reading is past two seasons · rows 51, 52; B21d.06 to B21d.09; CR-89, CR-90 · BLOCKED (A-114: target past two seasons) · HASH EQUAL
- SOURCE: part 2 §4 rows 51, 52 (HD-26; row 52 decided there); part 29's `DIALS AT CONTROL` lines: the CI band triggers' target "each flip kept only if CR-90's arm moves the reading in the ruled direction and the strife guard closes no terminal route" (CR-89's CONTROL); "CI starts at 28 with a season cap of ±5, so it reads at most 38 after two seasons and no CI band can be crossed in any seeded realm before season 3 (arithmetic on the shipped `[ASSUMPTION]` values, not a run)"; row 52: each Turmoil and goal-row trigger of B21d.07 to B21d.09 "whose flip CR-90's two-season arm does not support (equal arms)".
- SETTINGS: B21d.06's four Church Influence band switches (CI ≥ 40, 55, 60, 65 and 80) = off; the B21d.07 to B21d.09 switches each B21d's close left off (read their commit bodies).
- INSTRUCTION: none; flip nothing (`workplan_v12.md` §6).
- GATE: each switch read on the closing tree → off (R2).
- B99 QUOTES: CR-90's arm at B99's horizon (B99.01 step 6): the Church Influence reading per seed and whether any band is crossed, and each untested trigger's two arms; whether to flip on it is Jordan's.
- DEPENDS ON: V12 Batch B21d, B21d.06 to B21d.09. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.43 — three kinds of building stay unworn · row 53; B11F1; CR-106 · BLOCKED (design: no target reading) · HASH EQUAL
- SOURCE: part 2 §4 row 53; part 29_cont's line: "`wear_per_season` = 0 for `worship`, `templar_quarters`, `school` … (CR-106 gives no target)".
- SETTING: the three kinds' `wear_per_season` rows = 0 (B11F1's content rows).
- INSTRUCTION: none. OWNER OF THE TARGET: CR-106 (SE lane).
- GATE: the three rows read on the closing tree → 0 (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B11F1. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.44 — `window_responses` stays empty · row 54; B20 (`IS-MB-03` step 5) · BLOCKED (content: no authored row) · HASH EQUAL
- SOURCE: part 2 §4 row 54; part 30's line: "set by no batch (content: CHAR's cells, G-3); B98 lists it `BLOCKED (content: no authored row)`".
- SETTING: `window_responses` = empty (B20.19).
- INSTRUCTION: none. OWNER: the cast's content (CHAR's cells, G-3; Jordan), listed in the PR body.
- GATE: read on the closing tree → empty (R2). B99 QUOTES: an unplayed commander's window answer is the default; R-04.c5 (iii) reads at it.
- DEPENDS ON: V12 Batch B20, B20.19. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.45 — every doctrine's commander stays in reserve; the forward post is read, not shipped · row 55; B20.17; CHO gate 3 · BLOCKED (content: which doctrine rides forward) · HASH EQUAL
- SOURCE: part 2 §4 row 55 (TARGETED there; corrected here, U9); B20.17: "`doctrines.<name>.commander_post`: … seed `reserve` for every doctrine, which is the control"; `proposals/27_MB_D_the_commander_as_chooser.md` "Gate" 3: "The same commander posted forward against in reserve, n 400: forward, improvised orders are obeyed at once more often; forward, the share of fields in which his unit was struck is higher. Both differences beyond two standard errors". Gate 3 shows the post has a price and a gain; it does not say which doctrine takes which post.
- SETTING: `references/troops.yaml` (`doctrines.<name>.commander_post`) = `reserve` for every doctrine.
- INSTRUCTION: read gate 3 (`tests/valoria/test_mass_battle_officers.py::test_a_forward_post_buys_obedience_and_costs_exposure`, n 400) on this tree and quote it; flip nothing.
- OWNER: the doctrine rows are authored content (D-19; Jordan), listed in the PR body.
- GATE: the test → pass, its two differences quoted; `python tools/export_troops.py --check` → exit 0 (R2). B99 QUOTES: every commander in reserve.
- DEPENDS ON: V12 Batch B20, B20.17. COST and TIER: reading; `sonnet`, high. LANDS IT: no commit; B98.99's body.

### B98.46 — four obstacle steps of the word verbs leave 0 · row 56; B25.06, B25.13, B25.16, B25's `oblige` item; S2B §1, §2, §4; S2C §4; OBS §4 step 6+ · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 56; part 30_cont's line: "each 'with its step at control 0 first; equal at control; a declared mover when the step ships' (OBS §4 step 6+); set by B98; target: S2B's gate lines … and S2C §4's ('`news.told` / (`news.told` + `news.untold`) … stays below 1')"; `proposals/14_VERBS_SOCIAL2_B_a_word_with_content.md` "Gate": "`build_realm(s)`, s = 0, 1, 2, two seasons, `PYTHONHASHSEED=0`, on-arm against each fixture's control: … across the three seeds `proposition.believed` is emitted for some utterances and not for others (a fraction strictly between 0 and 1) …; §4: `oblige` formed > 0 at every seed, attempted ≥ 1; across seeds at least one `duty.taken` or `duty.probation` …; §2 … Over seeds 0–9 with the shipped odds, all four bands occur". S2B states no value: the sweep is the sibling `regard_step`'s, `0 / 0.5 / 1.0 / 2.0` (`13_SC_calibration` §3 step 3; U9, precedent).
- SETTINGS: `engine/season/data/fixtures.py` (`dissent_step`, `clarity_step`, `deference_step`, `establishment_step`) = 0. New values: each from `{0.5, 1.0, 2.0}`.
- INSTRUCTION: one value moved at a time, against its control (`13_SC_calibration` §3's rule): for each step in turn, the others at their chosen or control values, seeds 0 to 2 (0 to 9 for §2's bands), two seasons, in-process: the gate line that step's verb reads (`dissent` → §1's fraction and S2C §4's ratio; `clarity`, `deference` → §2's four bands; `establishment` → §4's `oblige` and `duty.*`). Rule (U4): per step, the smallest value at which its line holds and its line at 0 is not already the same (the step is not decoration); none: that step stays 0. One commit with the four values; each NUMBER row's text names its reading.
- FALSIFIER and CONTROL: S2B's falsifiers (`test_vm_s2_b_word.py`). Control arm: `HASH(0, 2; each step = 0)` equals B98.36's after-reading.
- GATE: `python -m pytest engine/season/tests/test_vm_s2_b_word.py engine/season/tests/test_vm_s2_c_case.py -q` → pass; the per-step table quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: "a declared mover when the step ships": every world with an `utter`, `tell`, `construe` or `oblige` drawn. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: the four steps → 0 (one commit).
- DEPENDS ON: V12 Batch B25, B25.06, B25.13, B25.16 and the `oblige` item; Batch B05 (OBS, the composer).
- COST and TIER: calibration; `sonnet`, high; `opus` reads each line. LANDS IT: B98's producer; `Item: B98.46`, `[skip ci]`.

### B98.47 — a tie weighs the teller, at IN-32's value · row 57; B25.20; S2D edit 4; FI08 §3 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 57 ("TARGETED at the 0.5 arm, else BLOCKED"); part 30_cont's line: "target: FI08 §3 / S2D gate ('`tied()` is called more than 0 times in a seeded realm and the `tie_gain` 0 and 0.5 arms hash differently'; 0.5 is IN-32's value, FI08 'The problem')".
- SETTING: `engine/season/data/fixtures.py` (`tie_gain`) = 0 (B25.20). New value: 0.5.
- INSTRUCTION: read the gate at 0.5, seeds 0 to 2, two seasons: the count of `tied()` calls (by the test file's counting wrapper) and `HASH(s, 2; tie_gain = 0.5)` against `HASH(s, 2; tie_gain = 0)`. If `tied()` is called and the hashes differ at some seed, `tie_gain` → 0.5.
- FALSIFIER and CONTROL: "`tie_gain` 0 must hash as the control" (S2D). Control arm: `HASH(0, 2; tie_gain = 0)` equals B98.46's after-reading.
- GATE: `python -m pytest engine/season/tests/test_knots_season_form.py engine/season/tests/test_vm_s2_d_tie.py -q` → pass; the calls and the two arms' hashes quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every world where a tied teller is weighed. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `tie_gain` → 0.
- DEPENDS ON: V12 Batch B25, B25.20; Batch B35 (the knot reader `tied()` reads, if it moved there).
- COST and TIER: calibration; `sonnet`, high. LANDS IT: B98's producer; `Item: B98.47`, `[skip ci]`.

### B98.48 — a sentence moves the hearers' regard · row 58; B27.04; SC_C "Gate" · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 58; part 31's line: "SC_C 'Gate': 'With `sentence_gain = 1`: regard for the convicted falls for every witness, by more for one given a positive stance toward the Duke and by less for one given a negative stance (three hearers planted at −25, 0, +25; the run prints three distinct values in that order)', swept 0 / 1 / 2, 'proposed first live value 1.0'".
- SETTING: `engine/season/data/fixtures.py` (`sentence_gain`) = 0.0 (B27.04). New value: 1.0 (the source's first live value; its gate reads at 1).
- INSTRUCTION: run `test_verdict_witnessed.py` at 1.0 (three planted hearers); if the three values print distinct and in order, `sentence_gain` → 1.0; its NUMBER row's text names the reading.
- FALSIFIER and CONTROL: B27.04's ("a planted hearer whose regard for the convicted does not move at `sentence_gain = 1`, or three hearers whose values are not in the stance order"). Control arm: `HASH(0, 2; sentence_gain = 0.0)` equals B98.47's after-reading.
- GATE: `PYTHONHASHSEED=0 python -m pytest engine/season/tests/test_verdict_witnessed.py -q` → pass; the three values quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every world where a sentence is witnessed. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers.
- REVERT: `sentence_gain` → 0.0.
- DEPENDS ON: V12 Batch B27, B27.03, B27.04. COST and TIER: calibration; `sonnet`, high. LANDS IT: B98's producer; `Item: B98.48`, `[skip ci]`.

### B98.49 — `docket_crossing_floors` stays empty · row 59; B27; TL §8 row B4.1 · BLOCKED (content: TL B6.n, held) · HASH EQUAL
- SOURCE: part 2 §4 row 59; part 31's line: "TL §8 row B4.1 names the control `()` only; the floors are authored with the ladders, TL B6.n, content held for Jordan".
- SETTING: `engine/season/data/fixtures.py` (`docket_crossing_floors`) = `()`.
- INSTRUCTION: none. OWNER: Jordan's ladders (TL B6.n, held, part 2 §8).
- GATE: `FIX(docket_crossing_floors)` → `()` (R2). B99 QUOTES: as left.
- DEPENDS ON: V12 Batch B27. COST and TIER: reading; `sonnet`, low. LANDS IT: no commit; B98.99's body.

### B98.50 — enmity can move a man to kill: the floor is set inside the realm's band · row 60; B37.13; `22_HAPPENINGS_C` · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 60; part 32's line: "target: `HAP_C`'s realm band at two seasons, seeds 0 to 7 ('fewer than one attempt per seed-season on average, and more than zero across the eight seeds'; four seasons in the source, A-114) and 'no death of a seat-holder in season 0'"; `proposals/22_HAPPENINGS_C_a_killing_is_a_crime_someone_commits.md` "Gate": "**Acceptance is a band, not a floor** … Zero means the context is dead and the floor is wrong; one a season means §1.2 of the audit has returned", and "Falsifier": "Set `enmity_floor` to admit every stance: the realm gate's upper bound fails".
- SETTING: `engine/season/data/fixtures.py` (`enmity_floor`) = a value no stance reaches (B37.13). New value: chosen by the probe from the realm's own values (U9): the values `held_against` takes over the persons who hold a dispute, at build, seeds 0 to 7, listed.
- INSTRUCTION: at each listed value (in order from the most hostile), seeds 0 to 7, two seasons, in-process: the count of `fight` formed under `enmity`, and seat-holders dead in season 0. Rule (U4): the most hostile value (the fewest admitted) at which the count is above 0 across the eight seeds, below one per seed-season on average, and no seat-holder dies in season 0. None: ship nothing.
- FALSIFIER and CONTROL: the source's falsifier above (read at the least hostile value: the upper bound fails). Control arm: `HASH(0, 2; enmity_floor = <the shipped unreachable value>)` equals B98.48's after-reading.
- GATE: `python -m pytest engine/season/tests/test_cr87_violence_contexts.py -q` → pass (`test_realm_band_between_zero_and_one_attempt_per_seed_season` at two seasons, `test_no_seat_holder_dies_in_season_zero`); the probe's table quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every world in which the context holds (a `fight` forms on enmity). EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers, the NPC-088 headless pin if it moves.
- REVERT: `enmity_floor` → the unreachable value.
- DEPENDS ON: V12 Batch B37, B37.13, B37.14.
- COST and TIER: calibration; `sonnet`, high; `opus` reads the band. LANDS IT: B98's producer; `Item: B98.50`, `[skip ci]`.

### B98.51 — the opener of an unexpected attack has an edge · row 61; B37.15; UPR §6 · BUILD (flip) · HASH MOVER(behaviour)
- SOURCE: part 2 §4 row 61 ("TARGETED, after row 60"); part 32's line: "`surprise_level` = None; set by B98, after `enmity_floor` (UPR §6 edit 3: 'shipped `None` until `22_HAPPENINGS_C` … gives an own-motive attack a context') …; target: UPR §6's gate, 'the opener's felled share is below the mirror control by more than the interval at `moderate`' (module scale, 6,000 fights, `opener_edge_probe.py`)"; `proposals/U5b_PC_rulings_in_the_fight.md` §6 row 3: "`surprise_level: None (control) | "minor" | "moderate"`, swept".
- SETTING: `engine/season/data/fixtures.py` (`surprise_level`) = `None`. New value: `"moderate"` (the source's reading arm).
- STOPS IF: B98.50 shipped nothing (no own-motive context holds): the source's condition is unmet; flip nothing and record.
- INSTRUCTION: `python systems/combat/combat_engine_v1/workbench/opener_edge_probe.py` at `moderate` (6,000 fights, in the background, sized first); if the opener's felled share is below the mirror control by more than the interval, `surprise_level` → `"moderate"`.
- FALSIFIER and CONTROL: UPR §6's ("An edge on a duel (`accept`) or on an arrest resisted; an edge that persists past the first exchange; a `surprise` event at the control arm"). Control arm: `HASH(0, 2; surprise_level = None)` equals B98.50's after-reading; `python tools/ci_golden_modes_check.py` → equal at `None`.
- GATE: `python -m pytest engine/season/tests/test_season_opener_edge.py -q` → pass; the probe's two shares and interval quoted; `HASH(0, 2)` recorded.
- HASH MOVERS: every season fight opened on an unexpected attack. EXPECTED RED UNTIL B98.99: the `_realm_goldens` readers if moved.
- REVERT: `surprise_level` → `None`.
- DEPENDS ON: V12 Batch B37, B37.15; V12 B98.50.
- COST and TIER: calibration; `sonnet`, high; the probe run may be `haiku`; `opus` reads it. LANDS IT: B98's producer; `Item: B98.51`, `[skip ci]`.
