# A-100 design, part 3: coding items, the supersession list, the evidence log

## Status: PROPOSED (part 3 of `master/mb_abstraction/MBA_DESIGN.md`; nothing here is applied; resolves nothing at runtime)

Item form: `master/INSTRUCTION_SUITE_ORDER.md:11`. Handles `MBA-nn`. Dependencies are marked EXISTS-IN-TREE / PROPOSED / MISSING. Lane tag MB unless said. Line numbers are at this read (§9).

---

## §7 · Coding instructions (v12 batch items)

### §7.0 The batches

| batch | lane | after | items | hash movers | wave (U3 §2.2, amended §5.3) |
|---|---|---|---|---|---|
| **B19a-mb-contact-instrument** (new) | MB, PC review | B14, B15, B16, B17 | MBA-01, MBA-02 (stage 1), MBA-03 | none (hash EQUAL: nothing in a field reads the table) | W11 |
| **B19-mb-field-calibration** (existing; amended) | MB | adds B16, B19a to its list | MBA-04, MBA-05, MBA-06 after `27_MB_A` and `16_PESSIMIST_MB_one_stamina_ledger.md` steps 1–2 and **in place of** `04_MB_cr12_linear_law.md` steps 2–3 and `16_PESSIMIST_MB_partition_and_the_pair_rule.md` edits 1–3; MBA-08 read last with `26_MASS_BATTLE_calibration_targets.md` and `27_MB_C` 27C-2/27C-3 | every fought field; one re-pin in the batch's last `Item:` commit, co-batched with 27C-3's | W12 |
| **B30-mb-nested** (existing) | MB | unchanged | MBA-07 after `04_MB_squad_grid_of_named_characters.md` | none (a test) | W14 |
| **B31-mb-loadout-economy** (existing) | MB | unchanged | MBA-09 (BLOCKED in part on J-MBA-01) | fields with missiles or the later rows, when unblocked | W13 |

Every item's glossary edit rides in its own commit (`STAGES.md`, "The glossary always matches", rule 2; the rows are §8.3).

### §7.1 Items

**Item: MBA-01 · the troop file carries the contact's data: the duel key of each arm, the men's skill, the contact header, an empty matchup table**

- **Advances:** A-100 (the data the contact draw reads), A-59 (2) (prowess is kit and troops, data on the row).
- **INSTRUCTION** (in order; `references/troops.yaml` and its loader exist after B17, `04_MB_unit_loadout_and_weapon_in_hand_B.md` §1):
  1. `references/troops.yaml: arms.<key>`: add `duel_key` (a key of personal combat's weapon export, or null) and `duel_key_status: exact | proxy | none`. Seeds: `light_cut: arming exact`, `heavy_cut: falchion proxy`, `heavy_blunt: mace exact`, `spear: spear exact`, `arming: arming exact`, `pike: spear proxy`, every missile arm `null none` with `sidearm: dagger`. [ASSUMPTION: these five — basis: nearest duel weapon by kind; content for Jordan's pass.]
  2. `troops.<type>`: rename the column `power` to `skill` (the men's martial skill on the duel's `faculty` scale, §1.7), values unchanged. Every reader of `power` in `modules/mass_battle/` reads it through `stats_for` (`troop_types/registry.py:78-85`) after B17's loader; the loader returns both keys during this batch (`power` an alias), and MBA-04 deletes the alias when the last pool reader goes.
  3. A header block `contact:` with `exposure: {base, posture_k, cover: {walls}}`, `levels: {intent_offense, intent_defense, terrain_die, charge_cap, morale_near_rout}` and `K: 6`, each value with `status: seed` and its source constant named in a comment (§1.3, §1.4 give the seeds); `missile: {bands: [0.25, 0.5], hit: {...}, shots_per_tick: {...}, felling_per_hit: {...}, profile: {foot: 1.0, mounted: 1.6}}`, all `status: seed`.
  4. `matchups: []`, shipped empty, with the loader's schema (§3.2).
  5. `modules/mass_battle/troop_types/table.py` (the loader B17 creates): reads the new columns; refuses, naming the row: an arm with neither `duel_key` nor `sidearm`; a `duel_key_status` outside its closed set; a `contact`/`missile` value with no `status`; a matchup row naming a class or situation outside the closed sets (§3.2's eight classes, seven situations) or a `closes` outside `closes | draw | evades | refused`. `tools/export_troops.py` carries the new columns into `engine/engine_params/troops.json`.
- **WHERE:** `references/troops.yaml`; `tools/export_troops.py`; `engine/engine_params/troops.json`; `modules/mass_battle/troop_types/table.py`; `tests/valoria/test_export_troops.py`.
- **FALSIFIER and control:** a seeded field moves at this item (it must not: nothing reads the new columns); control: `tools/ci_golden_modes_check.py`'s digests before and after.
- **GATE:** `python tools/export_troops.py --check` exits 0; `python -m pytest tests/valoria/test_export_troops.py -q` with new tests `test_every_arm_has_a_duel_key_or_a_sidearm`, `test_an_unstatused_contact_value_is_refused`, `test_a_matchup_row_outside_the_closed_sets_is_refused` (each written first and read red); `python tools/ci_golden_modes_check.py` digests unchanged.
- **Hash movers:** none. **Depends on:** `04_MB_unit_loadout_and_weapon_in_hand_B.md` stages 1–2 (PROPOSED, B17); personal combat's weapon export (`engine/engine_params/combat_engine_v1.json`, EXISTS-IN-TREE; its weapon records per `03_PC_weapon_records_in_the_export.md`, PROPOSED, B14).
- **Batch:** B19a, first. **Cost and tier:** edit; `sonnet`, `high`. **Lands it:** B19a's `valoria-author` producer, one `Item: MBA-01` commit, `[skip ci]`.

**Item: MBA-02 · the calibration instrument**

- **Advances:** A-100 (weapon-on-weapon and weapon-on-armour numbers from simulated personal combat).
- **INSTRUCTION:**
  1. New `tools/calibrate_mb_contact.py`, module docstring stating its role in one sentence ("runs the duel engine over a grid of matchups and writes the measured felling chances the mass-battle contact draw reads") and the same sentence as its `role:` line in `references/ci_checks_registry.yaml` (CLAUDE.md §4: coinage defined where invoked), with `blocking: false` and `notes: "an instrument, run by hand at a calibration pass; not a CI check"`.
  2. Loads the duel engine through `engine/substrate/pc_engine.py` (`pc_engine.load()`), never `modules/mass_battle`. The grid is read from `references/troops.yaml` (the fighter types are the distinct `(duel_key, armour, skill)` the troop rows can field, plus the §2.1 grid's levels) so a new troop type needs no edit here.
  3. Per cell: `random.Random(crc32(repr(cell_key)) % 100000)`; duels position-swapped in halves (the `balance.winrate` precedent, `systems/combat/combat_engine_v1/workbench/balance.py:56-75`); each duel read **per round from the round entry's typed result** (`master/pc_round/`, A-101; until it lands, the `engagement_end` and `wound` events, which is what the pilot read); accumulate per side `h_k` with Wilson intervals, the damage-taken quantiles, `felled_mortal` when the round result carries a mortal-wound band; the stop rule and the cap of §2.2.
  4. Sub-commands: `run OUT [--workers W] [--cells F]`; `--cell KEY N`; `--spot M` (re-run M cells chosen as every `len/M`-th in key order, each `h_1` inside its stored interval); `--trust` (§5.2's seven checks, stop on the first failure, print which).
  5. `--workers` uses `multiprocessing` with one RNG per cell (no shared stream), so the table does not depend on the worker count.
  6. **Stage 1 (B19a):** melee cells only. **Stage 2 (MBA-09, B31):** `--missile`, per-hit felling by `(missile head, armour)` through `core.damage` (`modules/combat/core.py:609`), once missile head records exist in personal combat's catalogue (MISSING; J-MBA-01).
  7. The first full run is made in this batch, launched in the background at the batch's start (`STAGES.md` efficiency rule 5) after two small runs size it; the measured table `references/mb_contact/duel_grid.json` is committed with the run's wall time, worker count and the `--trust` and `--spot 20` readings in the commit body (the time replaces §2.2's estimate).
- **WHERE:** `tools/calibrate_mb_contact.py`; `references/mb_contact/duel_grid.json`; `references/ci_checks_registry.yaml`.
- **FALSIFIER and control:** a measured table whose mirror cells disagree beyond their intervals (the instrument is biased by position); a table that differs when `--workers` changes. Controls: the mirror cells; `--workers 1` against `--workers 4` on 10 cells, byte-identical.
- **GATE:** `python tools/calibrate_mb_contact.py --trust` prints seven `ok` lines; `--spot 20` prints 20 `inside` lines; `--cell` on one pilot cell (`spear light 3 / arming light 3`) reproduces its stored row. Expected readings, from the pilot on today's engine (B15 will move them; the reading at B19a is the one recorded): mirror win shares within 0.03 of each other; mean rounds a mirror duel at least 2.
- **Hash movers:** none. **Depends on:** B14, B15, B16 (PROPOSED: §5.1); `master/pc_round/` (PROPOSED, in progress); `pc_engine.load` (EXISTS-IN-TREE, `modules/combat/fight.py:72`); MBA-01.
- **Batch:** B19a, second. **Cost and tier:** small build `sonnet`, `high`; the run `haiku`-supervised in the background; a `--trust` failure is read by `opus` (a judgment: is it the duel or the instrument). **Lands it:** B19a's producer.

**Item: MBA-03 · the exporter, its blocking `--check`, and the module's reader**

- **Advances:** CLAUDE.md §5 (a value the engine uses lives in a typed artifact behind an exporter with a blocking `--check`).
- **INSTRUCTION:**
  1. New `tools/export_mb_contact.py` on the `tools/export_battle_orders.py` pattern (`build()`, `main(argv)`, `--check` diffs and exits 1): builds `engine/engine_params/mb_contact.json` from `references/mb_contact/duel_grid.json` and `references/troops.yaml` (§2.3: per ordered pair of fighter types, `h[1..K]`, `beta`, flags; the `contact`, `missile` and `matchups` blocks with their status tags).
  2. `--check` also: (b) recomputes the duel-engine fingerprint (sha256 over `engine/engine_params/combat_engine_v1.json` and the sorted sources of `modules/combat/*.py`) and fails, printing `python tools/calibrate_mb_contact.py run …` as the remedy, when it differs from the table's; (c) refuses an arm whose `duel_key` the table lacks, and any pair of fighter types the troop file can field that has no cell.
  3. New `modules/mass_battle/core/contact_table.py`: loads `mb_contact.json` once (the `troop_types/table.py` precedent: a data file, no `engine` import, no `modules.combat` import); `felling_chance(arm_a, armour_d, skill_a, skill_d, rounds_d) -> float` (log-odds interpolation on skill and rounds), `beta(...)`, `status(...)`.
  4. `references/ci_checks_registry.yaml`: a row for the exporter, `blocking: true`, wired in `tools/valoria_local.py --staged` and proposed (not made) for the workflow's season job beside `export_battle_orders.py` (Jordan owns `.github/workflows/`; the registry note at `:312-318` is the precedent).
- **WHERE:** `tools/export_mb_contact.py`; `engine/engine_params/mb_contact.json`; `modules/mass_battle/core/contact_table.py`; `references/ci_checks_registry.yaml`; `tools/valoria_local.py`; new `tests/valoria/test_export_mb_contact.py`.
- **FALSIFIER and control:** a hand edit of `mb_contact.json` that `--check` passes; a changed `modules/combat/core.py` that `--check` passes. Controls: the committed pair passes.
- **GATE:** `tests/valoria/test_export_mb_contact.py::test_round_trip_is_clean`, `::test_a_hand_edit_fails_check`, `::test_a_changed_duel_engine_fails_check` (plants one byte in a copy of the fingerprinted sources, asserts exit 1 and the remedy line), `::test_a_troop_arm_without_a_cell_is_refused`, `::test_mass_battle_imports_no_combat` (subprocess import of `modules.mass_battle.core.contact_table`, asserting no path under `modules/combat` in `sys.modules`' files, the `test_importing_every_engine_module_pulls_in_no_subsystem` form), `::test_interpolation_hits_the_check_cells` (§2.5: at most one of twelve outside). `python tools/export_mb_contact.py --check` exits 0.
- **Hash movers:** none. **Depends on:** MBA-01, MBA-02. **Batch:** B19a, last (its close). **Cost and tier:** small build; `sonnet`. **Lands it:** B19a's producer; the close's one `opus` critique reads MBA-02's `--trust` output and this gate.

**Item: MBA-04 · the contact draw replaces the pool against an obstacle**

- **Advances:** A-100 (the exchange), A-60 (numbers through frontage, depth, endurance), A-59 (3) (no side-wide value), A-5, A-30.
- **INSTRUCTION** (in order):
  0. **ED-1043's trigger fires** (`workplans/valoria_master_workplan_v11_part10.md:189`: "a position edits `modules/mass_battle/orchestration.py` … that position's first commit extracts only the functions it touches, hash EQUAL"): first commit moves the melee pair's resolution out of `resolve_engagements` (`orchestration.py:1230-1378`), `pursuit_damage` (`:2057`) and `volley_phase` (`:1574-1688`) into `modules/mass_battle/core/contact_draw.py` and `core/volley.py`, unchanged; `tools/ci_golden_modes_check.py` digests equal.
  1. `core/contact_draw.py`: `ContactVector` (frozen dataclass, §1.1's fields); `contact_casualties(vec, table, z) -> float` implementing §1.3 steps 1–5 (levels in skill steps times `beta`; `q = 1 - (1 - h')^(r x m)`; `mu`, `var`; `clip`). Pure: no RNG inside, `z` passed in.
  2. `orchestration.resolve_engagements`: per pair and side, build the vector (`rounds_d` from the column stamina share; `support_a` from `_pair_engaged_troops` and `support_weight`; `exposure_d` from posture, `_octagon_cell_mods`' arc, the side count and cover, §1.4), draw `z` from the keyed draw owner with key `(field, bout, tick, pair, side, "contact")`, add `contact_casualties` to `dmg_a`/`dmg_b`; `MB_CELL_DAMAGE`'s allocation unchanged. Delete the melee pool, the sigma head's melee use, the opposed `compute_degree` lines and the `DAMAGE_BY_DEGREE` lines (`:1261-1368`).
  3. `core/attrition.py`: `_lanchester_strength` becomes `engaged_files(contact_cells, unit, front_width, shares)`, returning men in the front facing this contact, each contact cell counted at `1 / m` of the pairs it is in (`16_PESSIMIST_MB_partition_and_the_pair_rule.md` edit 4, which stands and is landed here).
  4. `core/exchange.py`: delete `subunit_combat_pool`, `pair_pool_contribution`, `command_base_pool`, `_stamina_pool_penalty`, `YIELD_POOL_MULT`; the routed/broken/disordered tests move to the vector's builder (a body with no fighting men contributes `m = 0`); `yield_active` becomes posture `retreat`. Keep `_pair_engaged_troops`, `derive_command`, `clamp_command`.
  5. `pursuit_damage`: the contact draw with the `pursuit` matchup row (the fleeing side's exposure at the rear arc, no answer from it); `freed_attacker_damage` and `run_multi_unit_battle` leave with the legacy harness (`04_MB_typed_outcome_and_one_path.md` §2), not converted.
  6. `percell.update_stamina`: the per-clash drain scaled by `exposure_d / EXPOSURE_BASE` (§1.4).
  7. `config.py`: delete `DAMAGE_BY_DEGREE`, `K_LINEAR`, `LANCHESTER_STRENGTH_REF`, `POOL_QUALITY_MODEL`, `POOL_QUALITY_SCALE`, `COMMAND_SIGMA_ENABLED`, `COMMAND_POOL_MULT`, `MB_STAM_SIGMA`, `RANGED_MELEE_SIGMA`, `MB_FRACTIONAL_POOL`, `PER_DIE_NET_EV` and their `__all__` entries; `CASUALTY_SCALE` stays only if a non-melee reader remains (grep at landing). `resolution.roll_pool*` and `_sigma_net_boost` stay only where a will check reads them, and move to the one sampler with `U5b_MB_rulings_in_the_field.md` §1 row 1 (B05). `python tools/export_sim_params.py --build` so `sim_params.json` drops the deleted constants.
  8. Delete the loader's `power` alias (MBA-01 step 2).
- **WHERE:** `modules/mass_battle/core/contact_draw.py` (new), `core/attrition.py`, `core/exchange.py`, `orchestration.py`, `percell.py`, `config.py`, `troop_types/table.py`; `engine/engine_params/sim_params.json`; `systems/mass_battle/sim/lanchester_signature.py` (the planted-collapse carrier, §4.2); new `tests/valoria/test_mass_battle_contact_draw.py`; `tests/valoria/test_mass_battle_partition.py` (the pair rule's gate file, re-pointed).
- **FALSIFIER and control:** (a) numbers leaking into the draw: two bodies of equal frontage and different depth produce different `mu` other than through `support_a` and endurance (test `test_depth_enters_only_through_support_and_endurance`); (b) a side term: any value read from the `Unit` that is not a field of the vector (test `test_the_vector_is_the_only_input`, by planting a `_friction` attribute and asserting no change); (c) the draw's mean differs from `mu` by more than 1% at `mu >= 5` over 20,000 draws (`test_contact_draw_mean_equals_mu_above_five`), with the bias below 5 printed (`test_clip_bias_is_reported_below_five`); (d) re-keying one contact changes another (`test_one_key_per_purpose`); (e) armour not monotone through `resolve_field` (`test_heavier_armour_loses_fewer_men`, n 200, `assert checked >= 200`). Controls: the same seed twice is one hash; the mirror field is side-fair (`systems/mass_battle/sim/mirror_probe.py`, below 1.5 standard deviations, `U5b_MB_rulings_in_the_field.md` §1).
- **GATE:** the five tests above and the pair rule's five rows (`test_partition_same_cells_inside_sampling_band`, `test_shape_one_rank_loses_more_than_wins`, `test_size_two_to_one_smaller_wins_some`, `test_flank_detachment_helps`, `test_no_certain_matchup_through_resolve_field`) green on the contact draw; `python -m systems.mass_battle.sim.lanchester_signature` (both `PER_CELL` arms): LINEAR on 27C-3 (h)'s condition, melee exponent at or below 1.4 with an identifiable fit, frontage control linear, NO-ANNIHILATION passing, the planted `EXPOSURE_BASE = 0` failing LINEAR; `grep -rn "DAMAGE_BY_DEGREE\|K_LINEAR\|POOL_QUALITY_SCALE\|subunit_combat_pool" modules/ engine/` prints nothing.
- **Hash movers:** every fought field; every `engine/tests/` golden with a field; `tools/ci_golden_modes_check.py`'s three digests. Declared; co-batched with `27_MB_C` 27C-3 and the other B19 movers; **one re-pin**, in B19's last `Item:` commit, said plainly as a re-pin.
- **Depends on:** MBA-01, MBA-03 (PROPOSED, B19a); the keyed draw owner (`11_GO_one_draw_owner.md`, PROPOSED, B06); the one stamina ledger's share (`16_PESSIMIST_MB_one_stamina_ledger.md` steps 1–2, PROPOSED, B19, earlier in the batch); `find_contacts`, `_octagon_cell_mods`, `support_weight`, `_pair_engaged_troops`, `MB_CELL_DAMAGE` (EXISTS-IN-TREE).
- **Batch:** B19, after `16_PESSIMIST_MB_one_stamina_ledger.md` steps 1–2, in the slot `U5b_MB_rulings_in_the_field.md` §6 row 4 gives CR-12 steps 1–3. **Cost and tier:** build with re-calibration; `opus` producer for step 2 (the vector's builder has judgment in it: which state is which field), `sonnet` for steps 0, 3–8. **Lands it:** B19's producer.

**Item: MBA-05 · the range-band missile model**

- **Advances:** A-100 layer (1).
- **INSTRUCTION:** `core/volley.py` (extracted in MBA-04 step 0): replace the pool, the `dr` subtraction and `K_SQUARE x eff_size` with §3.1 steps 1–5 (band from the per-arm range and `contact.missile.bands`; `shots_per_tick`; `hit[arm, band]`; `density_d` from `_volley_density_mult`, kept; `cover_d`; `profile_d`; `felling_per_hit[arm, armour, mounted]`; the keyed normal draw `(field, bout, tick, shooter, target, "volley")`). Ammunition, targeting orders and the no-volley-in-contact rule unchanged. `config.py`: delete `K_SQUARE`, `RANGED_DR_DEFAULT`, `VOLLEY_LETHALITY_SCALE` (grep their readers at landing). The per-arm ranges are `26_MASS_BATTLE_cell_scale_and_time.md` §2's, landed in the same batch.
- **WHERE:** `modules/mass_battle/core/volley.py`, `orchestration.py` (the call), `config.py`; `tests/valoria/test_mass_battle_ammo.py`.
- **FALSIFIER and control:** casualties per volley not falling from close to long band; not falling with the armour tier; a mounted target taking no more per hit than unarmoured foot of the same density. Control: the same body shooting at the same target at two distances in one band reads equal in distribution.
- **GATE:** `tests/valoria/test_mass_battle_ammo.py::test_volley_casualties_fall_with_the_band`, `::test_volley_felling_falls_with_the_armour_tier`, `::test_a_horse_takes_more_per_hit_than_unarmoured_foot` (T-6b), each n at least 400 with `assert checked >= 400`; the Lanchester SQUARE row at or above 1.6 with zero melee pairs (CR-12 step 1's repaired scenario).
- **Hash movers:** every field with a missile body; co-batched; the one re-pin. **Depends on:** MBA-01, MBA-04 step 0; `26_MASS_BATTLE_cell_scale_and_time.md` §2 (PROPOSED, B19). **Batch:** B19, after MBA-04. **Cost and tier:** small build; `sonnet`. **Lands it:** B19's producer.

**Item: MBA-06 · the ★ matchup rows and the charge on the contact draw**

- **Advances:** A-100 layer (2).
- **INSTRUCTION:**
  1. `troop_types/table.py`: `troop_class(type) -> str` from the arm class, `mounted` and `charge` columns (§3.2's eight classes; no name test); `matchup_row(a_cls, d_cls, situation) -> row | None`.
  2. `resolution.py`: `situation_of(attacker, defender, zone, t)` from the octagon zone, `_unit_braced`/`_subunit_braced`, `_brace_setup_ok`, momentum and formation state (all EXISTS-IN-TREE). `_charge_shock_sigma` (`:176-207`) returns, instead of a sigma, the charge's moral shock passed to the stand draw (`26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`), scaled by the row's `stand`; its preparedness product (`_disc_prep`, `_depth_prep`, `MB_SHOCK_*`) unchanged. `MB_CHARGE_RECOIL` becomes the row's `first_tick.exposure_a` times `_wall_prep`.
  3. `orchestration.resolve_engagements`: on a contact's first tick, read the row; `closes: draw` is a will check of the charging body on the one sampler with obstacle `close_ob` (a Failure: no contact this tick and the body halts, the H1 refusal); `evades`: the light body's kite on a draw (`MB_KITE_*`, unchanged); `refused`: no contact; then the row's first-tick exposure and levels enter the contact draw. `MB_RECOIL_CHARGER_GATE`'s literal `cavalry` test is deleted (the class replaces it).
  4. `references/troops.yaml: matchups`: the 10 ★ rows of §3.2 (the `pursuit` row among them, which MBA-04 step 5 reads), each `status: seed` with its source constant named, transcribed so the T-6 ordering reads as today; then MBA-08 reads them.
- **WHERE:** `modules/mass_battle/troop_types/table.py`, `resolution.py`, `orchestration.py`, `config.py`; `references/troops.yaml`; `tools/export_troops.py`; new `tests/valoria/test_mass_battle_matchups.py`.
- **FALSIFIER and control:** a charge that reads a troop name; a braced pike block that a frontal horse charge beats more often than the horse beats unbraced levy (T-6 inverted). Control: the horse against itself.
- **GATE:** `tests/valoria/test_mass_battle_matchups.py::test_t6_charge_ordering` (n 400 per arm, `assert checked >= 1200`), `::test_t6a_braced_pike_beats_a_frontal_charge_more_often_than_not`, `::test_t6c_a_horse_screen_helps_a_pike_block_under_bows`, `::test_no_troop_name_in_the_charge` (grep, asserted), `::test_light_horse_does_not_charge_a_set_wall`.
- **Hash movers:** every field with a mounted body; co-batched; the one re-pin. **Depends on:** MBA-04; `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md` with `16_PESSIMIST_MB_rout_has_two_exits.md` (PROPOSED, B19; the stand draw); `04_MB_unit_loadout_and_weapon_in_hand_B.md` §3's `charge`, `mounted` columns (PROPOSED, B17). **Batch:** B19, after the rout files. **Cost and tier:** small build `sonnet`; the row values read by `opus` at MBA-08. **Lands it:** B19's producer.

**Item: MBA-07 · the bridge: a squad of real duels against the contact draw on the same scene**

- **Advances:** A-100's "derived from personal combat" checked at the aggregation, not only per cell; the vertical direction of §6.2.
- **INSTRUCTION:** in `engine/season/tests/test_squad_field.py` (created by IS-MB-04, B30): a scene of eight foot against eight in one line (one kit each side, three kits: the mirror, arming against spear, light against heavy), resolved (a) as a squad through `modules/mass_battle/squad.py::resolve_squad` (real duel rounds per pair, `U5b_MB_rulings_in_the_field.md` §3) and (b) as two units of the same men through `resolve_field` on the contact draw at exposure 1 (one round a tick, the squad's own pace). Compare per side the share of men put out of the fight after a fixed number of rounds.
- **FALSIFIER and control:** the two shares differ beyond the sampling band in the mirror (then the aggregation, not the table, is wrong). Control: the squad against itself at two seeds.
- **GATE:** `::test_the_contact_draw_matches_the_squad_within_band` (n 200 scenes per kit, `assert checked >= 600`); the kits that differ are printed with their two shares (orderings must agree; magnitudes within the band or reported).
- **Hash movers:** none. **Depends on:** `04_MB_squad_grid_of_named_characters.md` and `U5b_MB_rulings_in_the_field.md` §3 (PROPOSED, B30); IS-MB-04 (PROPOSED, B30); MBA-04. **Batch:** B30, after IS-MB-04. **Cost and tier:** small build; `sonnet`; the reading `opus`. **Lands it:** B30's producer.

**Item: MBA-08 · the calibration read: exposure, the levels and the seeds, against the targets**

- **Advances:** §4.2's rows; A-77 (read with the multiplier's test).
- **INSTRUCTION:** after MBA-04 to MBA-06 and before 27C-3's commit, extend `tests/sim/gauge_mb.py --results` (`26_MASS_BATTLE_calibration_targets.md` §2) with T-2a, T-6a, T-6b, T-6c, T-11 and the dominance report (§6.3: every troop type's contact ratio against every other at equal men, fresh, per situation and at range; a type above 1 against all in all is printed). Set `EXPOSURE_BASE` once by T-1 and T-2 (one sweep of five values, n 400 each, sides swapped as control), never again in the same commit as a band; sweep each level and exposure factor one at a time against its control arm; record each `status` that moves from `seed` to `calibrated` with its reading.
- **WHERE:** `tests/sim/gauge_mb.py`; `references/troops.yaml` (`status` and values); `engine/engine_params/troops.json`, `mb_contact.json` (re-exported).
- **FALSIFIER and control:** a band edited in the commit that moves a constant into it (`26_MASS_BATTLE_calibration_targets.md`'s own falsifier); a `calibrated` status with no reading in the commit body.
- **GATE:** `python tests/sim/gauge_mb.py --results` printed in the commit body with n, band and control per row; T-2a: `EXPOSURE_BASE` under 1 and the reading of rounds per tick printed; T-8 ordering holds with no knob (it is the falsifier of the duel-derived fatigue); T-11 printed. `python tools/export_mb_contact.py --check` and `export_troops.py --check` exit 0.
- **Hash movers:** the values it sets; inside B19's one re-pin. **Depends on:** MBA-04 to MBA-06; `26_MASS_BATTLE_calibration_targets.md` (PROPOSED, B19). **Batch:** B19, read last, with 27C-2. **Cost and tier:** the runs `haiku` (`valoria-measure`), the reading `opus` (the batch's judgment node). **Lands it:** B19's producer; the reading in the close.

**Item: MBA-09 · what waits on the kit: missile per-hit felling derived, and the other matchup rows** (BLOCKED in part)

- **Advances:** A-100 for missiles and horse, completing what MBA-05 and MBA-06 ship as seeds.
- **INSTRUCTION:** (1) the 25 rows of §3.2 not marked ★, at `status: seed` then read as MBA-08 reads (unblocked; needs the economy's cost columns to read dominance against cost). (2) **ANSWERED (A-113, Jordan: "stated rows checked against history and banded logically to derived results"):** shields, pikes, horse with lance and missile weapons are NOT taught to personal combat now; their matchup and per-hit rows ship as **stated rows** at `status: stated` (printed so in the battle report, never presented as measured), each (a) **checked against history**: the row's direction and rough size must agree with what the sources support (a braced pike block stops a frontal charge more often than not; horse ridden into stakes and arrows fails; a pike block without a screen is weak to archers; arrows bounce off shields), recorded as a named check with its citation; and (b) **banded logically to the derived results**: each stated row must lie inside the band its derived neighbours imply (same armour tier and arm against the derived melee rows give the bounds; ordering relations hold: a shielded line is no worse than the same line unshielded; a braced pike no worse than an unbraced pike against a charge; heavier armour no worse against the same missile), checked by a test over the table that reads the derived rows and fails when a stated row leaves its band (extend MBA-08's dominance reading to host it). A stated row moves to `status: derived` only if personal combat later learns the equipment (not scheduled). The former wording follows for history: **BLOCKED on J-MBA-01:** when personal combat's catalogue carries missile head records, MBA-02 stage 2 derives `felling_per_hit`; when it carries a shield, a pike or a mounted fighter, the grid gains that axis and the corresponding matchup rows move to `status: derived` through MBA-07's bridge.
- **WHERE:** `references/troops.yaml`; `tools/calibrate_mb_contact.py`; `references/mb_contact/duel_grid.json`. **FALSIFIER and control:** as MBA-02 and MBA-06. **GATE:** as MBA-02 (`--trust`, `--spot`) and MBA-06's tests on the new rows. **Hash movers:** fields with the rows; one re-pin in B31's last commit. **Depends on:** J-MBA-01 (MISSING: Jordan's answer, then a PC-lane build); B31's economy (PROPOSED). **Batch:** B31, last. **Owner of the block:** Jordan, then the PC lane. **Cost and tier:** small build `sonnet`. **Lands it:** B31's producer.

### §7.2 Layer 1 conformance (`skills/layer-conformance` Lens B; `04` §A.2, `holonic_ARCHITECTURE.md` §43, §45–§47)

| item | typed input, typed outcome | holds no token | keeps no game state | calibration is data | grade |
|---|---|---|---|---|---|
| MBA-01 | the troop file is data read by the module's loader; no `World` | yes | yes | yes: `references/` head, `engine/engine_params/` export | CONFORMS |
| MBA-02 | a tool, not a module: reads the duel engine through the one path seam (`engine/substrate/pc_engine.py`) | n/a | writes only its output file | its product is data | CONFORMS (outside Layer 2) |
| MBA-03 | `contact_table.py` loads a data file once (precedent: `troop_types/table.py`, `04_MB_unit_loadout_and_weapon_in_hand_B.md` §1); imports no `modules.combat` (`§43`: a registry row, never an import), asserted by test | yes | the loaded table is immutable data, not game state | yes | CONFORMS |
| MBA-04 | `contact_casualties(ContactVector, table, z) -> float`: typed in, typed out, pure; the draw value is handed in from the one keyed owner, the module draws nothing of its own | yes | per-call frame only; column stamina stays in the battle loop's frame (`26_MASS_BATTLE_cell_scale_and_time.md` §3's rule) | yes | CONFORMS |
| MBA-05, MBA-06 | as MBA-04; the matchup row is data | yes | yes | yes | CONFORMS |
| MBA-07 | a test over two registered entries; `resolve_squad` calls the `duel` callable handed in (cap 1, A-72) | yes | yes | n/a | CONFORMS |
| MBA-08, MBA-09 | instruments and data | n/a | n/a | yes | CONFORMS |

**One AMBIGUOUS row, named (B4 disposition):** Layer 1 says a registered module "takes typed input" (`CLAUDE.md` §3 summarising `04` §A.2); a module that loads a data file at import is not handed that data on its input. The tree has decided this shape once (the troop table loader, `04_MB_unit_loadout_and_weapon_in_hand_B.md` §1, and today's `config.py` constants): data the module reads is not game state and not an input from the world. This design follows that precedent (ladder step 4). The alternative (the host loads `mb_contact.json` and hands it in on `MassBattleInput`) is equally conforming and costs one field; it is named here so v12's author can take it if B17 takes it for the troop table.

---

## §8 · The supersession list (a table, not an edit; a later pass applies it)

### §8.1 Proposals and the instruction suite

| document : section | disposition | reason |
|---|---|---|
| `04_MB_cr12_linear_law.md` step 1 (the instrument repair: volley standoff, the identifiable fit, the frontage control) | **STANDS** (narrowed) | the exponent check becomes the falsifier of the contact draw's construction (§4.2); the **bisect of LINEAR 77% to 52%** is dropped: its subject (the pool's drift) is retired |
| `04_MB_cr12_linear_law.md` steps 2–3 (`prowess`/base term; `REFERENCE_SIZE`; re-read `POOL_QUALITY_SCALE`) | **SUPERSEDED** by MBA-04 | there is no pool; numbers leave the melee by construction (A-60 met without `REFERENCE_SIZE`) |
| `04_MB_cr12_linear_law.md` gate (planted collapse carrier) | **NARROWED** | carrier becomes `EXPOSURE_BASE = 0` (§4.2) |
| `16_PESSIMIST_MB_partition_and_the_pair_rule.md` edits 1–3 (quality pool; each side paid by its own net × `PAY_PER_NET` × (1 + power); armour and walls as dice) | **SUPERSEDED** by MBA-04 (and §1.4's `cover`) | each side's casualties are the opponent's measured felling chance; armour is in the table; walls are cover |
| same, edit 4 (a contact cell's share `1/m`) and gate rows 1–5 | **STANDS** | landed in MBA-04 step 3; the five rows are MBA-04's gate |
| `27_MB_B_unit_prowess_on_the_row.md` 27B-1, 27B-2 (`prowess(atom)` returns the pool's base term) | **SUPERSEDED** by MBA-01/MBA-04 | prowess is the vector `(arm, armour, skill)` and has a value only against an opponent (A-59 (3)) |
| same, 27B-3 (`troops.infantry {power: 4, discipline: 5}`) | **NARROWED** | the row carries `skill` (MBA-01 step 2) |
| same, 27B-4 (`readout(row)`) and §3 (no baseline lent by the side) | **NARROWED** / **STANDS** | the readout shows the unit's felling chances against a reference opponent, not a pool; §3 stands |
| `27_MB_C_dynamic_strength_and_the_residual_chance.md` 27C-1, 27C-2 | **STANDS** | the named draws and the six-arm test; the contact and volley draws are reported aggregated per unit, not per tick |
| same, 27C-3 | **STANDS** (narrowed) | lands in the same re-record as MBA-04; its (h) is read on the contact draw |
| `27_MB_A_command_and_the_obedience_draw.md` | **STANDS** | A-59 (1); a will check keeps its obstacle |
| `27_MB_D`, `27_MB_E` | **STANDS** | `27_MB_E` gains `felled_mortal` as a recorded candidate for its dead share (§1.2), not a value |
| `26_MASS_BATTLE_calibration_targets.md` | **STANDS** (extended) | rows T-2a, T-6a–c, T-11 added by MBA-08; `MB_FRICTION_SIGMA` row as `27_MB_C` |
| `26_MASS_BATTLE_cell_scale_and_time.md` §1, §3 / §2 | **STANDS** / **NARROWED** | §2's per-arm ranges are read by range bands; "a volley is a tick's worth of shooting" becomes `shots_per_tick` |
| `26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`; `16_PESSIMIST_MB_rout_has_two_exits.md` | **STANDS**, except the pursuit damage law **NARROWED** | pursuit casualties are the contact draw under the `pursuit` row (MBA-04 step 5), one law |
| `16_PESSIMIST_MB_one_stamina_ledger.md` | **STANDS** (narrowed) | the ledger's share feeds `rounds_d`; `MB_STAM_SIGMA` leaves; drain scaled by exposure |
| `04_MB_unit_loadout_and_weapon_in_hand_B.md` | **STANDS** (extended) | `arms.duel_key`, `sidearm`, `troops.skill`, `contact`, `missile`, `matchups` (MBA-01) |
| `04_MB_unit_loadout_and_weapon_in_hand.md`, `04_MB_headcount_grade_and_scale.md`, `04_MB_typed_outcome_and_one_path.md`, `04_MB_cell_hierarchy_as_data.md`, `04_MB_manager_battle_one_resolver.md`, `04_MB_playable_field_scenario.md`, `04_MB_campaign_party_economy.md` (experience as a skill step), `26_MASS_BATTLE_aggression_and_land.md`, `26_MASS_BATTLE_maneuver_orders.md`, `26_MASS_BATTLE_movement_and_fatigue_as_data.md`, `14_VERBS_MILITARY_A`–`D` | **STANDS** | none reads the pool, the degree table or the side-wide value |
| `04_MB_squad_grid_of_named_characters.md` | **STANDS** (extended) | gains MBA-07's bridge gate |
| `U5b_MB_rulings_in_the_field.md` §1 row 1 (one sampler for the field's will checks) / row 2 (the pair's casualties `K_LINEAR × frontage × PAY_PER_NET × net × (1 + power)`) | **STANDS** / **SUPERSEDED** by MBA-04 | the contact has no pool and no net |
| same, §2–§5 | **STANDS** | |
| same, §6 row 4 (the field calibration batch's order) | **NARROWED** | CR-12 steps 2–3 and the pair rule's edits 1–3 are replaced by MBA-04 to MBA-06 in the same slot |
| `U5b_MB_residue.md` | **STANDS** | |
| `03_PC_*`, `U5b_PC_*`, `16_PESSIMIST_PC_A`–`D`, `18_DETERMINISM_no_certain_matchup.md`, `14_VERBS_PHYSICAL_A` | **STANDS** | they are the instrument's preconditions (§5.1) |
| `29_DICE_one_opposed_rule_form_and_tuning.md` | **STANDS** | fights and arguments; the field's contact has no obstacle and does not read it (§6.2 diagonal row) |
| `IS_B1_PC_MB_DICE_part2.md` IS-MB-01 to IS-MB-05 | **STANDS** | |
| same, IS-MB-06 (`prowess_of` arithmetic with two callers) | **SUPERSEDED** by MBA-04 | no pool arithmetic remains |
| same, IS-MB-P6 (the module keeps its own roller) | **NARROWED** | the contact and volley draws use the keyed draw's normal; the will checks use the one sampler (B05) |
| same, IS-MB-B2 (the drill step on `power`) | **NARROWED** | a drill step is a step on `skill` |
| same, IS-MB-B3 (`27_MB_E` shares) | **STANDS** | `felled_mortal` adds a candidate, not a value |
| `IS_B1_PC_MB_DICE.md` IS-PC-01 to IS-PC-04; IS-DICE-01 | **STANDS** | |

### §8.2 Workplan v11 positions and the hole register

| position or row (file : line) | disposition | reason |
|---|---|---|
| CR-12, melee attrition back to the linear law (`workplans/valoria_master_workplan_v11_part4.md:59`; `_part3.md:446`; `_part12.md:117`) | **SUPERSEDED** by MBA-04 (with CR-12's step 1 instrument repair carried as `04_MB_cr12_linear_law.md` step 1) | the law holds by construction; the exponent check is its falsifier |
| ED-MB-0045's owed item "melee attrition back to the locked linear law" (`_part10.md:111`, `:187`) | **SUPERSEDED** by MBA-04 | as CR-12; its CellTable owner and item 4 stay LEAVE |
| ED-1043, the god-file split, LEAVE with a trigger (`_part10.md:189`; `_part12.md:347`) | **STANDS**; its trigger fires at MBA-04 step 0 | MBA-04 edits `orchestration.py`; step 0 is the trigger's own form |
| MB-07r (`_part12.md:253`, CLOSED `aa6871b8`) | **retired with its constant** | `POOL_QUALITY_SCALE`'s recalibration; the constant is deleted |
| CP-T04-04, CP-T04-10, MB-08, CL-TROOP (`_part12.md:21`, `:49`, `:55`, `:254`) | **STANDS** | none touches the contact |
| H-361 (`engine/season/hole_register.yaml`, "a standing order's role moves the field against its orderer under the shipped friction") | **NARROWED** | re-read on the contact draw with the multiplier at zero (`27_MB_C` 27C-3 (k)); its text follows the reading |
| H-150 (garrison strength is defined and unreachable) | **STANDS** | a candidate reader is the contact draw's `cover` for a garrison (named, not built) |
| H-97 (which `Combatant` field a person's condition lands on) | **STANDS** | the instrument uses the default body; a person's condition reaches the field only through the nested duel |
| H-348 (the fighter left standing is recorded `undecided`) | **STANDS** | personal combat's |

### §8.3 Glossary and lexicon rows owed (`STAGES.md` rule 2; edited in the item's commit)

| term | row | owner after |
|---|---|---|
| **contact draw** | new: "the one draw that sets how many men one side of a contact loses in one field tick"; rejected: "exchange" (personal combat's phase), "melee roll" | `core/contact_draw.py::contact_casualties` |
| **felling chance** | new: "the chance one man is put out of the fight in one duel round against one opponent"; rejected: "hazard", "lethality" | `mb_contact.json` |
| **exposure** | new (Jordan's word, A-100): "how many duel rounds a front-rank man fights in one field tick" | `troops.yaml: contact.exposure` |
| **matchup row** | new: "a row of data saying how one class of troops meets another in one situation" | `troops.yaml: matchups` |
| **range band** | new: "a distance band in which a missile arm hits at a stated rate" | `troops.yaml: contact.missile.bands` |
| **power** (`MB_LEXICON.md:185`) | retired as a troop stat; "skill" (the men's martial skill) replaces it | `troops.yaml: troops.<type>.skill` |
| **duel round** | unchanged (A-101); the contact draw's unit | `master/pc_round/` |

---

## §9 · Evidence log, and what was not checked

### §9.1 Files opened at this read (the claims cite them)

`unified/DECISIONS_ANSWERED.md` (A-1 to A-101); `STAGES.md`; `master/INSTRUCTION_SUITE_ORDER.md`; `master/instructions/IS_B1_PC_MB_DICE_part2.md:1-155`; `unified/U3_DEPENDENCY_ORDER.md:406-506`; `unified/DECISIONS_FOR_JORDAN.md:1-40`; MB lexicon rows by search (`MB_LEXICON*.md`); glossary rows by search; proposals `04_MB_cr12_linear_law.md` (whole), `26_MASS_BATTLE_calibration_targets.md` (whole), `26_MASS_BATTLE_cell_scale_and_time.md` (whole), `U5b_MB_rulings_in_the_field.md:38-159`, `04_MB_unit_loadout_and_weapon_in_hand_B.md:52-186`, `16_PESSIMIST_MB_partition_and_the_pair_rule.md:82-160`, `27_MB_B` and `27_MB_C` headings and item tables; `research/historical/mass_battle_casualties_and_results_grounding.md:52-137`; MV and SQ rows by search; code: `modules/mass_battle/core/exchange.py`, `core/attrition.py`, `equipment/weapons.py`, `armour.py`, `_base.py`, `__init__.py`, `troop_types/registry.py`, `presets.py`, `config.py` (searched; `:280-389` read), `resolution.py:37-230`, `orchestration.py:1230-1381`, `:1574-1736`, `:2057-2085`, `:2170-2190`; `modules/combat/fight.py`, `wrapper.py:1-100`, `:483-625`, `combatant.py:20-209`, `attributes.py` (SPEC); `systems/combat/combat_engine_v1/workbench/balance.py:1-80`, `calibrate_generics.py:1-60`; `systems/mass_battle/sim/lanchester_signature.py:1-60`; `tools/export_battle_orders.py:1-40`; `architecture/meta/04_CODE_ARCHITECTURE.md:127-166`; `engine/season/hole_register.yaml` (searched); `workplans/valoria_master_workplan_v11*.md` (searched).

### §9.2 Probes run

- **E-1, the pilot** (§2.4): `pilot.py 5000` over four cells (the fourth a repeat of the first), 42.6 s; `pilot2.py 3000` over three skill cells, about 20 s. `PYTHONHASHSEED=0`. Outputs `…/scratchpad/pilot/out1.jsonl`, `out2.jsonl`.
- **E-2, the timing probe**: 20 mirror duels, 1.72 ms a duel (the first reading; 2.33 at 5,000).
- **E-3, the duel catalogue**: `sorted(WEAPONS)` from `modules/combat/weapons.py`: 54 keys, of which none is a pike, lance, bow, crossbow, sling, javelin or shield; a search of `weapons.py`, `config.py`, `core.py`, `combat_systems.py` for mount, horse, cavalry, shield, missile, ranged found only comments.

### §9.3 Not checked

- `master/pc_round/` did not exist at this read; the round's typed result is assumed to carry per round: each side's damage taken, whether each was felled, and (after B15/B16) the wound band. [ASSUMPTION: basis A-101's text and `wrapper.py`'s `engagement_end`/`wound` events.]
- The pilot ran on today's duel engine, before B15 and B16; every number in §2.4 will move and is a sizing reading only.
- The interpolation of skill in log-odds and the plateau at round 4 to 8 were read on the mirror only.
- `holonic_ARCHITECTURE.md` §43–§47 were located, not read in full; the Lens B grades rest on `04` §A.2 and the precedents named.
- The `14_VERBS_MILITARY_*`, `04_MB_manager_battle_one_resolver.md`, `04_MB_squad_grid_of_named_characters.md`, `27_MB_A`, `27_MB_D`, `27_MB_E`, `26_MASS_BATTLE_rout_*`, `16_PESSIMIST_MB_rout_*` and `_one_stamina_ledger` proposals were read by heading and by search for the pool, the degree table and `power`, not in full; a "STANDS" for them means no reader of what this design removes was found.
- The research gauge (`mass_battle_gauge_grounding.md`), wargame models and `research/game_precedent_suite/grounding/` were not opened.
- `tools/ci_golden_modes_check.py`, `tests/sim/gauge_mb.py` and the B06 draw owner's interface were not opened; their names and roles are taken from the proposals that cite them.
