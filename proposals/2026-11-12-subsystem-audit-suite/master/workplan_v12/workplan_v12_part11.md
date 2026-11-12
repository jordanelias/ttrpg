# Workplan v12 — part 11: batches B17-mb-scale, B09-memory

## Status: PROPOSED (a body part of workplan v12, drafted under `master/workplan_v12/`; unratified input to `methodology-execute`'s 0.1 stop until Jordan adopts v12, `V12_STRUCTURE_part3.md` §8; resolves nothing at runtime, CLAUDE.md §0.05; not canon)

## Written against: the working tree at `aa31fd2` (branch `ccr-62958c70-0kjhsw`), read 2026-11-12; author lane A11 of `master/workplan_v12/V12_STRUCTURE_part2.md` §4.2, with the errata of `V12_STRUCTURE_part4.md`. Every item is written against the tree as the batches before it will leave it; where a symbol named here does not exist at `aa31fd2`, the item says which batch makes it.

**What this part holds.** Two batches, in execution order: `B17-mb-scale` (MB: one survivor share and a drawn battle, a typed field outcome on one code path, the troop file and its exporter, no hidden inputs) and `B09-memory` (IN: what a person remembers of a refusal, a fade, a reason and a record). Each batch is one block with one close, in the form of `V12_STRUCTURE_part2.md` §5.2 and §5.3 as `_part4` amends it (a `.99` re-pin position last, E-1; a `## Readings` block before it, E-10; SERIAL EDGES written after the position table, E-11). A part cites another part's batch or item by handle only.

**Words.** `unified/U1_GLOSSARY.md`. A person's numbers are an attribute, a skill and its skill score, a martial skill, a derived score (A-98). Armies follow the MB lexicon (`unified/MB_LEXICON.md` and `_part3.md`): army, unit, army formation, unit formation, troops, troop type, kit; no size word; a battle ends **won**, **lost** or **drawn** (a *drawn battle*, never "a draw" as the noun, S-11). A *lap* is one pass of the season's scene budget; a *round* is one engagement of a fight (A-101); the riposte's code id is `finalblow_riposte`. Copied source text that uses a word a later ruling retired is corrected and the correction said.

**Paths.** A bare path is under `proposals/2026-11-12-subsystem-audit-suite/`; `U3` is `unified/U3_DEPENDENCY_ORDER.md`; `the intake` is `master/eval/V12_INTAKE.md`; `the lexicon` is `unified/MB_LEXICON_part3.md`. A path under `engine/`, `modules/`, `systems/`, `tools/`, `references/`, `registers/`, `tests/` is the repository's. Proposal files are under `proposals/2026-11-12-subsystem-audit-suite/proposals/`.

**Names changed before these batches land** (`V12_STRUCTURE_part2.md` §5.10). B17 lands after B16L, B16M, B03c, B13 and B04, so every B17 item carries a `NAMES:` line for the identifiers its copied text uses: from B16L `subformations` → `units`, `Subformation` → `UnitRow`, Record kind `order_of_battle` → `standing_order`, the unit-row key `stance` → `posture`, `STANCES` → `POSTURES`; from B16M the engine's `hierarchy.units.Unit` → `Army`, `Subunit` → `Unit`, `subunits` → `units`, `SUBUNIT_*` → `UNIT_*`, `.broken` → `.disordered`, `max_turns` → `max_ticks`, `MassBattleInput.subunits` → `units` and the fixture `field_subunits` → `field_units` (the lexicon L2-1); from B03c `harness/populated.py::build_realm` → `boot/realm.py`. B09 lands after B04: `Claim.round` → `Claim.lap`, `SeasonDriver.round` → `.lap`, `scenes_per_round` → `scenes_per_lap`.

---

## Batch B17-mb-scale · lane MB · wave W9 · step S9 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B17-mb-scale
IN-FLIGHT ROW: registers/handoffs/HANDOFF_MB.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B16L-mb-words
GATE: Batch B16M-mb-engine-words
GATE: Batch B05-one-roll
GATE: Batch B14-pc-outcome
REQUIREMENT: none — the scale, the field's typed outcome and the troop file that B19a, B19, B20, B22 and B31 read (`V12_STRUCTURE.md` §2.2); rulings served: A-3, A-57, A-58, A-67, A-68, A-70, A-81 (a battle ends won, lost or drawn and each band writes), A-1 (one code path), D-U1-11c (no hidden inputs). `IS-MB-05`'s integrated reading is quoted at the close (B17.13), not a requirement row
BATCH GATE (read once, on the closing tree; `PYTHONHASHSEED=0` on every seeded command):
  `python tools/export_troops.py --check` → exit 0; `python tools/export_engine_params.py --check` → exit 0 (its new `mass_battle_v1.json` section);
  `python tools/ci_golden_modes_check.py` → `[BYTE-EXACT OK]` in every mode, each digest equal to B16M's close (`reading @<sha>`) or, where B17.01 or B17.08 moved one, equal to the value B17.99 re-records (said in that item's commit body);
  `git grep -n "environ" modules/mass_battle` → nothing; `git grep -n "troop_type == '" modules/mass_battle` → nothing;
  `python -m pytest engine/season/tests/test_march.py engine/season/tests/test_mass_battle_module.py tests/valoria/test_export_troops.py tests/valoria/test_field_golden_pins.py tests/valoria/test_mass_battle_army_record.py tests/valoria/test_mass_battle_order_of_battle.py tests/valoria/test_mass_battle_role_instructions.py tests/valoria/test_frontage_conservation.py engine/season/tests/test_go07_canonical_digest.py -q` → all pass;
  `build_realm(s)` (`boot/realm.py`), one season, s = 0, 1, 2: seed 0's content hash equal to B16M's close reading (no field is fought there); seed 2's moved and re-recorded by B17.99 (`04_MB_headcount_grade_and_scale` gate 5); seed 1 equal unless the commit body of B17.01 names a field fought there;
  B17.13's reading (`IS-MB-05`): at seed 2 the realm's battle ends `field.won`, `field.lost` or `field.drawn`;
  `python -m engine.season.harness.register --check` → exit 0; `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line, quoted;
  the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (the batch touches `modules/mass_battle/`, `engine/season/` and a registry: the full gates, `-m mass_battle` first);
  the glossary rows each item names, read against the code it landed (`STAGES.md`, "The glossary always matches", rule 2);
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, and the batch's measured wall time; no conjunct is named, so no `reading:` record is written; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B17.99: the realm pins of `engine/season/tests/_realm_goldens.py` (B02's one pin file) that moved — seed 2's one-season pin at least — and `test_go07_canonical_digest.py`'s vectors if they moved, read against B16M's close (`reading @<sha>`), or against B07's merge where B07 merged first in S9 (`V12_STRUCTURE_part3.md` §7.4); the three field digests only if B17.01 or B17.08 moved them; the commit says "re-pin: every fought field (B17.01: one survivor share, the drawn band, the shipped `field_walls_dr` and `field_units`; B17.03: the per-cohort write on the army path)".
IDS: ED-MB 0; H 0 (the batch closes register rows and writes none: H-250, H-354, H-359, H-308 by B17.01; H-355, H-151, H-360 by B17.02)
DIALS AT CONTROL: none. The `mass_kg` seeds, the `strength` seeds and every `secondary: null` of `references/troops.yaml` (B17.10) are authored content, Jordan's (`04_MB_unit_loadout_and_weapon_in_hand_B` "Seeds", "Content for Jordan"), listed in the batch's PR body (D-19), not settings at control; the second weapon's cost lands in B31 (loadout_B stage 4).
UNDECIDED: (1) `04_MB_headcount_grade_and_scale`'s `Drawn` write names "losses and fatigue … for each (A-69; `27_MB_E`)": `27_MB_E` lands in B22, so B17.01 writes the shares on `body` and the re-homing and leaves the fatigue write to `27_MB_E` in B22 (the reading that changes less; the other: hold `Drawn` to B22, which leaves H-354 open five batches). (2) `04_MB_typed_outcome_and_one_path` §4 retires `core/exchange.py::derive_command` and moves `CMD_CHA_WEIGHT`/`CMD_COG_WEIGHT` "with the harness code", but at `aa31fd2` `derive_command` is called by `hierarchy/units.py` (`Unit` and `Officer` `__post_init__`), so it is live module code: B17.06 is a POINTER and the retirement waits for `CommandRecord` (`27_MB_A`, B19). (3) `U5b_MB_residue` sections whose dependency lands later are not items here (E-8, the dependency wins): §3 (B22, U3 §4.1 row 62), §4 item 1 (after B19, its own Lands line), §5 (`04_MB_playable_field_scenario` §F, B20), §9 R-29 (`FieldOutcome.report`, declared by `04_MB_manager_battle_one_resolver`, B20); §9 R-25 is carried by `26_MASS_BATTLE_movement_and_fatigue_as_data` §4 (B31); §2 R-38 is Layer 1 text (`architecture/meta/03_VERBS_AND_LOOPS.md`, `10_FACTIONS_AND_DEPLOYMENT.md`), not applied by a v12 item without Jordan's amendment (`unified/U2_LAYER1_CONFORMANCE.md` row 86: AMBIGUOUS, "not applied here"); §2 R-23 and §7 edit v11 plan cards, which v12's adoption deletes (`V12_STRUCTURE_part3.md` §8.1 step 4); §8 is cross-listed with no edit. The B20, B22 and B31 authors and H2 are owed these. (4) `04_MB_typed_outcome_and_one_path` §3 empties every `environ` read, which `tests/valoria/test_field_golden_pins.py`'s drift guard compares against: B17.12 re-points the guard at `config.DEFAULT` (§3's own sentence that `os.environ` is read only under `systems/mass_battle/sim/`), the reading that keeps gate 3 observable; the other is to stop B17.12. (5) `04_MB_typed_outcome_and_one_path` §2 moves `pursuit_damage`, `recall_check`, `feigned_retreat_recognized`, `feigned_retreat_check` and `resolve_feigned_retreat` to `systems/mass_battle/sim/multi.py`, but B19 (`16_PESSIMIST_MB_rout_has_two_exits`, `27_MB_A` 27A-5, `27_MB_C` 27C-1, MBA-04 step 5: "`freed_attacker_damage` and `run_multi_unit_battle` leave with the legacy harness … not converted", `pursuit_damage` converted) and B20 (`26_MASS_BATTLE_maneuver_orders`) edit those five in `orchestration.py` and give them a season caller: B17.05 leaves the five in place (the reading that changes less; the other moves them out and B19/B20 move them back). `between_turn_recovery` and `base_combat_pool` do move: B19's `16_PESSIMIST_MB_one_stamina_ledger` edits them where they then live, `systems/mass_battle/sim/multi.py` (owed to the B19 author as a `NAMES:` line). (6) `04_MB_unit_loadout_and_weapon_in_hand_B` and `04_MB_typed_outcome_and_one_path` §3 name "the troop file's header" and "an `orders.obey` step" as rows: where `references/troops.yaml` puts a header key is B17.10's and B17.12's reading of the source, not a further decision.
C(B17-mb-scale): this batch's entries; the plan's head parts; `unified/U1_GLOSSARY.md` rows *end state*, *unit*, *kit*, *troops, troop type, levy*, *power*;
  `modules/mass_battle/massbattle.py`; `modules/mass_battle/orderofbattle.py`; `modules/mass_battle/armyrecord.py`; `modules/mass_battle/battle_loop.py`; `modules/mass_battle/orchestration.py`; `modules/mass_battle/config.py`; `modules/mass_battle/hierarchy/units.py`; `modules/mass_battle/core/exchange.py`; `modules/mass_battle/percell.py`; `modules/mass_battle/equipment/` (`__init__.py`, `_base.py`, `weapons.py`, `armour.py`); `modules/mass_battle/troop_types/` (`registry.py`, `recruitment.py`, `presets.py`, NEW `table.py`); `modules/mass_battle/armies.py`;
  `engine/season/queries/inputs.py` (`MassBattleInput`); `engine/season/data/fixtures.py`; `engine/season/rosters.yaml` (`field_degree_bands`); `engine/season/verb_table.yaml` (`march`); `engine/season/seam/ladder.py` (`field_degree`); `engine/season/seam/wrappers/mass_battle.py` (`resolve`, `field_estimate`, `field_input`); `engine/season/loop/effects_combat.py` (`_eff_march`); `engine/season/loop/effects_migration.py` (`_relocate`); `engine/season/state/gate.py` (the `muster` basis); `engine/season/hole_register.yaml`; `engine/season/requirements.yaml` (the scales note);
  `references/troops.yaml` (NEW); `tools/export_troops.py` (NEW); `engine/engine_params/troops.json` (NEW); `tools/export_engine_params.py`; `engine/engine_params/mass_battle_v1.json` (NEW); `engine/engine_params/combat_engine_v1.json` (read only); `tools/export_battle_orders.py` (the exporter pattern, read only); `references/ci_checks_registry.yaml`; `tools/valoria_local.py`; `references/restructure_ledger.md`;
  `systems/mass_battle/sim/` (NEW `multi.py`, `role_edges_probe.py`, `extremes_probe.py`; `bat.py`, `engine.py`, `validators.py`, `workbench/trace.py`; DELETE `tactic_cards.py`, `altonian_reinforcements.py`); `registers/placeholder_names.yaml`; `registers/mechanics_index.yaml`; `registers/handoffs/HANDOFF_MB.md`; `proposals/2026-10-29-army-phase5-design.md`; `proposals/mass_battle_fighting_withdrawal_v1.md`;
  the tests named in the items; instruments: `tools/ci_golden_modes_check.py`, `harness/aperture.py`, `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`; `engine/season/tests/_realm_goldens.py` (B02);
  the closing SHAs of B00, B01, B02, B16L, B16M, B05, B14; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_MB.md`, the skill and `methodology-close`).
SERIAL EDGES: within the batch: B17.01 first (every later item reads the one share and the drawn band; U3 §1.2 B17 item 1) → B17.02 (R-12's sentence is deleted once the headcount write lands) and → B17.03 (`field_degree` re-pointed at the typed outcome) → B17.04 (the refusal sits beside the typed return) → B17.05 (`run_traced_battle` builds the typed input) → B17.07 (the feint's home is settled before its role leaves the menu) → B17.08 (the minimum is read from the cut role list) → B17.10 (the `roles` column is the cut list; `MIN_DISCIPLINE` is read before the header moves) → B17.11 (columns and `arms` exist) → B17.12 (§3 moves row values into the troop file and reads `export_troops.py --check`, U3 §1.2, U6 R-A) → B17.13 → B17.99. B17.06 has no edge (a POINTER); B17.09 has none inside the batch (test assertions only) and lands where its position puts it. Hash-EQUAL items come after the two behaviour movers B17.01 and B17.03 because the source orders the outcome's write before the moves (`04_MB_typed_outcome_and_one_path` "Implementation" (1) → (2)) and B17.01 heads U3's order; B17.08 is a declared mover placed where its input exists.
  With other batches, by file (U3 §5.1's batch lists, the lexicon's L1/L2 file lists, put in v12's landing order by `V12_STRUCTURE.md` §2.3's steps; U3's own rows are in handle order, which is not landing order here: B15, B16 and B12a–c land after B17): `massbattle.py` B16L → B16M → B17 → B19 → B20 → B31; `orderofbattle.py` B16L → B17 → B19 → B20 → (B22, B32 at S17) → B31; `orchestration.py`, `hierarchy/units.py` B16M → B17 → B19 → B20; `battle_loop.py` B16M → B17 → B15 → B19 → B20; `config.py` B16M → B17 → B19 → B31; `percell.py` B17 → B19 → B31; `troop_types/table.py`, `tools/export_troops.py` B17 → B19a → B19 → B31; `references/troops.yaml` B17 → B19a → B19 → B20 → B22 → B30 → B31; `seam/wrappers/mass_battle.py` B16M → B17 → B19 → B20 → B22 → (B23, B30 at S18) → B31; `seam/ladder.py` B17 → B23; `effects_combat.py` B04 → B14 → B17 → (B12a–c, B16) → B19 → B20 → B22 → B23 → B31; `queries/inputs.py` B05 → B14 → B17 → B15 → then U3's later batches in step order; `data/fixtures.py`, `rosters.yaml` B05 → (B07, B17 at S9) → B09 → …; `verb_table.yaml` B04 → (B07, B17 at S9) → B09 → …; `hole_register.yaml` B14 → B17 → B10 → …; `requirements.yaml` B03 → B17 → B09 → B11 → B26 (the scales note only). Hot files touched (`V12_STRUCTURE_part3.md` §7.3): `rosters.yaml` (`field_degree_bands`, `observation_terms`), `verb_table.yaml` (`march`), `fixtures.py` (three `field_*` keys), `inputs.py` (`MassBattleInput`, the three outcome records).
PARALLEL: S9 with B07-task-draw (IN). Shared files: `rosters.yaml` and `verb_table.yaml` (B07 edits the task-draw route rows and the loader's shapes; B17 the keys named above: different top-level keys, kept by hand at merge, §7.3); `fixtures.py` if B07 adds a fixture (a different key). Both are movers: B07 merges first (its row precedes B17's in `V12_STRUCTURE.md` §2.1); B17 rebases on B07's merge, takes B07's after-reading as its baseline (`reading @<sha>`) and re-pins once in B17.99 (§7.4). No file under `modules/mass_battle/` or `systems/mass_battle/` is B07's.
COST: edits and small builds, two wide mechanical moves (B17.05, B17.12); producer `valoria-author` on `sonnet`, `high`; the mechanical moves `haiku`-assisted (the source's tier); the close's terminal critique `opus`.
EST: 8 h [estimate: `V12_STRUCTURE.md` §2.4's per-commit formula over this batch's 14 positions (0.4 h × 14 + 2.5 h); §2.2's 5 h counted the five members, not the commits they order]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B17.01 | one survivor share, one scale, a drawn battle | `04_MB_headcount_grade_and_scale` | BUILD | MOVER(behaviour) | Batch B16M, Batch B05 |
| B17.02 | pointer, status-line and comment edits; three register rows | `U5b_MB_residue` §2 | BUILD | EQUAL | B17.01 |
| B17.03 | the field returns a frozen `FieldOutcome`; casualties per cohort | `04_MB_typed_outcome_and_one_path` §1 (its commit 1) | BUILD | MOVER(behaviour) | B17.01 |
| B17.04 | a side past the ceiling, or of nobody, never reaches the cell engine | `U5b_MB_residue` §6 | BUILD | EQUAL | B17.03 |
| B17.05 | one code path: the unreached loops move to the workbench; dead code deleted | `04_MB_typed_outcome_and_one_path` §2 (its commit 2) | BUILD | EQUAL | B17.03 |
| B17.06 | the first skill input waits for `CommandRecord` | `04_MB_typed_outcome_and_one_path` §4 | POINTER | — | — |
| B17.07 | one list of unit roles that leave the menu | `U5b_MB_residue` §1 with `04_MB_typed_outcome_and_one_path` §2 fifth bullet (its commit 4) | BUILD | EQUAL | B17.05 |
| B17.08 | `GappedLine`'s minimum Discipline lets its roles keep their shape | `U5b_MB_residue` §9 R-24 | BUILD | MOVER(behaviour) | B17.07 |
| B17.09 | conservation claims compared exactly | `U5b_MB_residue` §4 item 2 | BUILD | EQUAL | Batch B16M |
| B17.10 | the troop file, its exporter and its loader; the tables become reads | `04_MB_unit_loadout_and_weapon_in_hand_B` stage 1 | BUILD | EQUAL | B17.07, B17.08 |
| B17.11 | the four name tests become columns; reach derives from the arm | `04_MB_unit_loadout_and_weapon_in_hand_B` stage 2 | BUILD | EQUAL | B17.10 |
| B17.12 | no hidden inputs: the environment reads split between the troop file and an explicit `cfg` | `04_MB_typed_outcome_and_one_path` §3 (its commit 3) | BUILD | EQUAL | B17.10, B17.11 |
| B17.13 | the integrated reading of mass battle at this close | `IS-MB-05` | READING | — | B17.01 to B17.12 |
| B17.99 | re-pin and close readings | `V12_STRUCTURE_part4.md` E-1 | BUILD | MOVER (the re-pin) | B17.01 to B17.13 |

Not in this batch, and where each is: `04_MB_unit_loadout_and_weapon_in_hand` (SUPERSEDED in whole by `_B`, already marked at its Status line; no item, `V12_STRUCTURE_part2.md` §5.5); `04_MB_unit_loadout_and_weapon_in_hand_B` stages 3–4 (B31, U3 §4.1 row 61); `U5b_MB_residue` §3, §4 item 1, §5, §7, §8, §9 R-25 and R-29, §2 R-23 and R-38 (UNDECIDED (3) above); the `Drawn` write's fatigue (B22, `27_MB_E`; UNDECIDED (1)); a drawn defender's regard and grievance toward the aggressor (`U5d_FA_land_and_seats_pass_on_a_won_march`, B23, the FA reader `04_MB_headcount_grade_and_scale` names); `IS-MB-P3`, `-P4`, `-P5` (pointers of `IS_B1_PC_MB_DICE_part2.md` to this batch's members: carried by B17.01, B17.07 and B17.03, no item of their own).

### B17.01 — one survivor share, one scale, a drawn battle · 04_MB_headcount_grade_and_scale · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/04_MB_headcount_grade_and_scale.md` "The resolution, decided", "Exact edits", "Gate", "Tests (W3-1)", "Falsifier"; rulings A-3, A-57, A-58, A-67, A-68, A-70, A-80, A-81; closes F-MB-01, F-MB-02, F-MB-04 (`audits/04_MB_audit.md` R-01, R-02, R-03, R-16, R-18, R-19), H-250, H-354, H-359, H-308; `IS-MB-P3`.
- ADVANCES: none of the nine by itself; the scale every later MB batch reads (a realm force fights a battle that can be won, lost or drawn).
- INSTRUCTION ("Exact edits", copied; the struck `verdict` text of the source is not carried):
  1. `modules/mass_battle/massbattle.py` (owner of the grade and the headcount constructors):
     - `_grade(unit_a, unit_b)`: "delete the `by_troops` parameter and its `else` branch. Both shares are `unit.hp / max(1.0, unit.hp_max)`." `_grade` "returns each side's share and its `routed` / `conceded` flags, and **no** `verdict`; the rule below is evaluated by the host's `field_degree`":
        ```
        a_out = unit_a.routed or unit_conceded(unit_a)
        b_out = unit_b.routed or unit_conceded(unit_b)
        verdict = 'won'   if b_out and not a_out
                  'lost'  if a_out and not b_out
                  'drawn' otherwise            # both out, or neither out when the ticks ran down
        ```
       "The survivor-share tie-break (`a_size_pct > b_size_pct`) goes: a field in which neither side broke is drawn. The constants `OVERWHELMING_ATTACKER_MIN`, `OVERWHELMING_DEFENDER_MAX`, `PARTIAL_ATTACKER_MIN` and the four-way `degree` are deleted (no reader: `seam/ladder.py`)." `_run_and_grade` loses its `by_troops` argument with `_grade`'s.
     - "`_weighted_unit` and `_person_unit`: `troops = max(under_arms_cap(weight), _MIN_TROOPS)`; the `troops_per_weight` parameter is deleted. Both are built with `faction` `'A'` / `'B'` and placed by `orderofbattle._place` (one line each), so a headcount field starts `_APPROACH_ROWS` apart as an army field does. `_MVP_SUBUNIT_SHAPE['starting_position']` is deleted." `resolve_field`'s two calls of each drop `inp.troops_per_weight`.
     - "`_HEADCOUNT_LINE_TYPE` and `_oob_unit`'s `None` branch are unchanged (they already size by `under_arms_cap`)."
  2. `engine/season/queries/inputs.py`: "delete `MassBattleInput.troops_per_weight`" (and its docstring bullet).
  3. `engine/season/data/fixtures.py`: "delete `field_troops_per_weight` (and its sweep row); ship `field_walls_dr=3` (with CP-T04-05's scaling this is the archived table's +3 at a full garrison and proportionally less below; `None`, the flat row, stays in the sweep as the control); ship `field_subunits="person"`" (after B16M the key is `field_units`). Each shipped value keeps a `[JUSTIFIED: …]` tag on its line naming this item.
  4. `engine/season/hole_register.yaml`: "H-250 `default:` → closed, owner `recruitment.under_arms_cap`; H-354 closed by the `Drawn` band; H-359 `default:` → `person` shipped; H-308 → graded as shipped." (Edit each row's fields in place; no row is added.)
  5. `engine/season/rosters.yaml: field_degree_bands.values` gains `Drawn`, appended last after `Invested` (the roster's own note keeps the earlier positions; additions go at the end of their block, CIP part 2 §5 note 1). `engine/season/verb_table.yaml`: "`march` gains a `Drawn` row: writes `(Person, body)`, emits `field.drawn`. No arrival kind."
  6. `engine/season/seam/ladder.py::field_degree`: "reads the two sides' `routed` and `conceded` flags off the typed outcome and applies the rule above (`Won`, `Lost`, `Drawn`), after `unopposed` and `invested`." Until B17.03 lands the typed outcome, it reads the two flags off the result mapping `resolve` lifts (step 7); B17.03 re-points the read at `FieldOutcome` with no change of band.
  7. `engine/season/seam/wrappers/mass_battle.py::resolve`: "lifts the typed outcome's two sides in place of `attacker_wins`; `winner` is `claimants`, `other` or `[]`. `field_estimate` tallies four bands."
  8. `engine/season/loop/effects_combat.py::_eff_march`:
     - "the loser's write is capped as the winner's is: `min(1.0, max(0.0, mine))`" (the loser's `body` write; today `max(0.0, mine or 0.0)` uncapped);
     - "on `Drawn`: every member of both sides (or the drawn cohorts of a side that fought as an army) has `body` scaled by his own side's (or own part's) share, under `field_casualty_model` as the winners' write is today; no stance row; **each army returns immediately to its station** (the aggressor's to where the march began, A-67/A-68; the defender's to its own base, A-70), through `loop/effects_migration.py::_relocate` under the gate's `muster` basis (`state/gate.py`), in the same fold"; "the ration debit as on `Won` and `Lost`". The fatigue half of "losses and fatigue are written for each (A-69)" is `27_MB_E`'s write and lands in B22 (UNDECIDED (1)).
     - "every band names its durable write: `Won`/`Lost` the shares and `field.won`/`field.lost`; `Drawn` the shares, the re-homing and `field.drawn`, witnessed by those present" (A-81, A-80).
  9. Glossary: `unified/U1_GLOSSARY.md` row *end state* (§J): the owner column becomes a pointer to `seam/ladder.py::field_degree` and `rosters.yaml: field_degree_bands` (`Drawn`); the rejected "a draw" (noun) kept.
- WHERE: `modules/mass_battle/massbattle.py` (`_grade`, `_run_and_grade`, `_weighted_unit`, `_person_unit`, `_MVP_SUBUNIT_SHAPE`, the three constants, `resolve_field`); `engine/season/queries/inputs.py` (`MassBattleInput.troops_per_weight`); `engine/season/data/fixtures.py` (`field_troops_per_weight`, `field_walls_dr`, `field_units`); `engine/season/hole_register.yaml` (H-250, H-354, H-359, H-308); `engine/season/rosters.yaml` (`field_degree_bands`); `engine/season/verb_table.yaml` (`march`); `engine/season/seam/ladder.py` (`field_degree`); `engine/season/seam/wrappers/mass_battle.py` (`resolve`, `field_estimate`); `engine/season/loop/effects_combat.py` (`_eff_march`); `engine/season/tests/test_march.py`; `engine/season/tests/test_mass_battle_module.py`; `unified/U1_GLOSSARY.md` (*end state*).
- TESTS (written before the edit, read red where they assert the new behaviour): `engine/season/tests/test_march.py::test_a_drawn_field_returns_each_army_to_its_station`, `::test_a_drawn_field_writes_both_sides_losses` (gate 4: a hand-built stalemate folds `field.drawn`, both sides' bodies fall by their own shares, no `stance` row, each army at its station); `engine/season/tests/test_mass_battle_module.py::test_no_share_exceeds_one` (gate 1: `_weighted_unit` pairs, seeds 0 to 99, four size pairs: no share above 1.0; a side with no casualties reads exactly 1.0), `::test_realm_weight_pairs_vary_by_seed` (gate 2: weights 30 v 18, 20 v 6, 6 v 20 through `resolve_field`, seeds 0 to 59: the verdict varies by seed and the larger side's `won` share exceeds the smaller's; `assert checked >= 180`); gate 3 is the existing real-fold test `test_a_real_chooser_forms_and_folds_a_march_that_reaches_a_real_field_battle` `[ASSUMPTION: the source's "real-fold test" — basis: the one test in `test_march.py` whose name folds a real chooser's march to a field battle]`, read at the shipped fixtures with no scale override: a `field.won` for the unmodified Crown pair at some seed in 0 to 11 and a `field.lost` or `field.drawn` at another.
- FALSIFIER and CONTROL: "A fought field at the shipped fixtures whose loser's `body` rises, or whose untouched side's `body` falls; or twelve seeds of the unmodified realm pair that all fold one band." Control: `build_realm(0)`, one season, content hash equal to the previous close's reading (no field is fought there).
- GATE: `python -m pytest engine/season/tests/test_march.py engine/season/tests/test_mass_battle_module.py -q` → pass; the realm content hash after one season at seed 0 → equal to B16M's close reading; at seed 2 → moved (recorded in the commit body, re-pinned at B17.99); `python tools/ci_golden_modes_check.py` → read and recorded: equal, or the moved mode named in the commit body for B17.99 `[ASSUMPTION: the three `bat.py` modes do not run the headcount constructors — basis: `04_MB_typed_outcome_and_one_path` gate 3 and loadout_B stage 1 both expect the digests equal in this batch; `bat.py` not opened]`.
- EXPECTED RED UNTIL: B17.99 for the realm pin test of `_realm_goldens.py` at seed 2 (it stays under `[skip ci]`).
- HASH MOVERS: "every fought field; seed 2's one-season pin" (the source), with the shipped `field_walls_dr=3` and `field_units="person"`. Declared; B17's one re-pin in B17.99.
- DEPENDS ON: EXISTS-IN-TREE `modules/mass_battle/troop_types/recruitment.py::under_arms_cap`, `seam/ladder.py::field_degree`, `loop/effects_migration.py::_relocate`, the gate's `muster` basis (`state/gate.py`), `orderofbattle._place`, `_APPROACH_ROWS`; V12 Batch B16M (the names), Batch B05 (the one sampler for the module's dice, `U5b_MB_rulings_in_the_field` §1); the fatigue write V12 B22 (`27_MB_E`).
- GLOSSARY: *end state* (step 9).
- NAMES: `field_subunits` → `field_units`; `Subunit` → `Unit` and the engine's `Unit` → `Army` in any copied reference (B16M; `_MVP_SUBUNIT_SHAPE`, `_PersonSubunit` and `_weighted_unit`/`_person_unit` as B16M left them, the lexicon L2-1 (a) keeps the two builders' names); `build_realm` in `boot/realm.py` (B03c).
- COST and TIER: edit (one module file, one effect, four data rows); `sonnet`, `high`; MB review of the seam.
- LANDS IT: B17's `valoria-author` producer, `isolation: worktree`; `Item: B17.01`, `[skip ci]`.

### B17.02 — pointer, status-line and comment edits; three register rows · U5b_MB_residue §2 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5b_MB_residue.md` §2 (rows R-12, R-13, R-14, R-37 and the `hole_register.yaml` row); closes F-MB-25 (R-37, `U5_FINDINGS_CLOSURE_U5b.md`), R-12, R-13, R-14, H-355, H-151, H-360 (pointed).
- ADVANCES: none of the nine; reference surfaces that no longer say the opposite of the code.
- INSTRUCTION (each row's edit, copied; the rows not carried are UNDECIDED (3)):
  1. R-12, `registers/handoffs/HANDOFF_MB.md`: "a side under 100 troops … is not hurt" is deleted (B17.01 has landed: "true of the troops, false of the write until then").
  2. R-13, `proposals/2026-10-29-army-phase5-design.md`, M11: "one line: superseded by CR-24 (`field_winner_casualties: engine` shipped); the code governs".
  3. R-14, `engine/season/requirements.yaml`, the scales note: "reached via natural computed play" reworded to what the instrument reads: "`march` executes; a fought field does not (seeds 0 to 2: 0, 0, 1)" — the figures re-read at this tree by `python -m engine.season.harness.aperture 1 s`, s = 0, 1, 2, and the reading written instead of the source's if they differ, with its SHA. Only the note's text; no `status:` or `reading:` edited.
  4. R-37, `proposals/mass_battle_fighting_withdrawal_v1.md` Status: "reads 'BUILT, on by default' (`MB_YIELD_*` default `'1'`)"; `modules/mass_battle/orchestration.py::reform_check`'s docstring "states its flag's value (`REFORM_CHECK_ENABLED` defaults `'1'`)". The "melee sidearm" comment in `troop_types/registry.py` stays until `arms` lands (B17.11 removes it with `TROOP_TYPE_REACH`).
  5. `engine/season/hole_register.yaml`: "H-355: closed by A-57, A-58 and A-66 (the land may pass after an aggressor's win, by his own `seize`, C3-L12; a routed defender is re-homed). H-151: closed (its own `default:` says so). H-360: pointed at the per-part outcome" (the pointer names `FieldOutcome`'s `PartOutcome`, which B17.03 lands; the row's text is edited in this item and reads true from B17.03).
- WHERE: `registers/handoffs/HANDOFF_MB.md`; `proposals/2026-10-29-army-phase5-design.md`; `engine/season/requirements.yaml` (the scales note); `proposals/mass_battle_fighting_withdrawal_v1.md`; `modules/mass_battle/orchestration.py` (`reform_check` docstring); `engine/season/hole_register.yaml` (H-355, H-151, H-360).
- TESTS: none new.
- FALSIFIER and CONTROL: a surface that still says the opposite of the code (`grep -n "is not hurt" registers/handoffs/HANDOFF_MB.md` prints a line). Control: the realm content hash at seed 0, one season, equal to B17.01's reading.
- GATE: `python -m engine.season.harness.register --requirements` → loads, nine lines; `python -m engine.season.harness.register --check` → exit 0; `python tools/freshness_gate.py` → as CI runs it (report-only locally: its reading quoted).
- HASH MOVERS: none.
- DEPENDS ON: V12 B17.01; EXISTS-IN-TREE the four files and the three register rows.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B17's producer; `Item: B17.02`, `[skip ci]`.

### B17.03 — the field returns a frozen `FieldOutcome`; casualties per cohort · 04_MB_typed_outcome_and_one_path §1 (its commit 1) · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/04_MB_typed_outcome_and_one_path.md` "The resolution, decided" §1, "Implementation (test 9, W3-1)" order (1), "Gate" 4, "Falsifier"; rulings A-3, A-29, A-69 (control arm), D-U1-06, D-U1-11e; closes F-MB-05, F-MB-06 (R-04, R-05, R-08, R-09); `IS-MB-P5`.
- ADVANCES: none of the nine; one typed return on every provider (the seam row of `04`).
- INSTRUCTION ("§1", copied; `verdict` is withdrawn by A-3 and is not carried):
  1. `engine/season/queries/inputs.py`, beside `MassBattleInput`:
     ```
     @dataclass(frozen=True)
     class PartOutcome:
         id: str            # a member's person id (headcount `person` arm) or a cohort's (army path)
         share: int         # survivors on the body scale: round(condition_scale x hp_left / hp_start), 0..scale
         routed: bool

     @dataclass(frozen=True)
     class SideOutcome:
         share: int                 # the side's survivors, same scale
         routed: bool
         conceded: bool
         parts: tuple               # PartOutcome, in input order; () on the headcount `side` arm
         broke_first: Optional[str] # the part id that broke on its own account first, or None

     @dataclass(frozen=True)
     class FieldOutcome:
         # (Reconciled, A-3) no `verdict`: the host's `field_degree` reads the band off the two sides' flags
         ended: str                 # 'rout' | 'concession' | 'time'
         ticks: int                 # field ticks run (the engine's `run_battle` returns them as "turns")
         attacker: SideOutcome
         defender: SideOutcome
     ```
     "Shares are integers on the exported body scale (`condition_scale` arrives on the input), so the seam is the point where the engine's floats are quantised; quantised at the seam, not an integer-state commitment (A-29: declared floats now). `__post_init__` refuses an `ended` outside its set." "This file declares the base fields (`ended, ticks, attacker, defender`; the per-side and per-part records). The other fields of the one `FieldOutcome` land each with its own proposal and are declared nowhere else" (D-U1-11e).
  2. `modules/mass_battle/massbattle.py::resolve_field` returns a `FieldOutcome` on every arm (today a four-key `dict`, six on one arm). "Army path: a part is a cohort. Each unit's surviving fraction is applied to the troops each cohort assigned to it (`armyrecord`'s `assigned` rows, carried on `OrderOfBattle` as `drawn: ((unit, cohort, troops), ...)` in place of `drawn_from`), and summed per cohort. `broke_first` is read from the engine's own order of breaking: `battle_loop.run_battle` appends `(side, unit index)` to a list on its return value when it first sets `routed` on a unit while its army stands. `massbattle._PersonSubunit` and its property setter are deleted." (Corrected for the B16L/B16M names: "subformation" → unit, "subunit" → unit, the engine's "unit" → army.) The returned dict's `"turns"` key stays the engine's (B16M left it); `FieldOutcome.ticks` reads it.
  3. `engine/season/loop/effects_combat.py::_eff_march` "reads `outcome.attacker` / `.defender`: a person named in `parts` is scaled by his part's share, anyone else by the side's. `broke_observed` is written for both sides; it and the field's named draws (`draw:<name>`, `27_MB_C`) ride `Event.observed` as members of `rosters.yaml: observation_terms` (D-U1-06)" — `broke` joins `observation_terms` here if the roster does not hold it; the named draws join with `27_MB_C` (B19). `seam/ladder.py::field_degree` and `seam/wrappers/mass_battle.py::resolve` (B17.01 steps 6–7) read the two `SideOutcome`s.
  4. "With `recuperation: on` the per-unit loss is written to the unit's row by kind" is `27_MB_E` (B22); this item writes the per-cohort body share, which is the control arm A-69 keeps ("Folded" (3)).
- WHERE: `engine/season/queries/inputs.py` (`PartOutcome`, `SideOutcome`, `FieldOutcome`); `modules/mass_battle/massbattle.py` (`resolve_field`'s returns, `_PersonSubunit` deleted); `modules/mass_battle/battle_loop.py` (`run_battle`'s breaking order); `modules/mass_battle/orderofbattle.py` (`OrderOfBattle.drawn`); `modules/mass_battle/armyrecord.py` (`to_order_of_battle`'s `drawn`); `engine/season/loop/effects_combat.py` (`_eff_march`); `engine/season/seam/ladder.py` (`field_degree`); `engine/season/seam/wrappers/mass_battle.py` (`resolve`); `engine/season/rosters.yaml` (`observation_terms`); `engine/season/tests/test_mass_battle_module.py`; `tests/valoria/test_mass_battle_army_record.py`.
- TESTS (written before the edit, read red): `engine/season/tests/test_mass_battle_module.py::test_resolve_field_returns_a_frozen_field_outcome`, `::test_ended_outside_its_set_is_refused`; `tests/valoria/test_mass_battle_army_record.py::test_routed_and_holding_units_cut_their_own_cohorts` (gate 4: "a folded army field in which one unit routs and another holds leaves the cohorts that fed them with different bodies; a planted 'side share for every cohort' reddens it").
- FALSIFIER and CONTROL: "an army field whose reserve cohort is cut as deeply as its line." Control: the realm content hash at seeds 0 and 1, one season, equal to B17.01's reading (no natural season fights an army field); the planted side-share control reddens gate 4.
- GATE: `python -m pytest engine/season/tests/test_mass_battle_module.py tests/valoria/test_mass_battle_army_record.py engine/season/tests/test_march.py -q` → pass; `python tools/ci_golden_modes_check.py` → digests equal to B17.01's reading; the realm hash at seed 0, one season → equal to B17.01's.
- HASH MOVERS: "step (1) on the army path only (no natural season fights an army field)". Declared; B17's one re-pin in B17.99.
- DEPENDS ON: V12 B17.01 (the flags `field_degree` reads); EXISTS-IN-TREE `queries/inputs.py::MassBattleInput`, `battle_loop.run_battle`, `armyrecord` `assigned` rows, `OrderOfBattle.drawn_from`; V12 Batch B16L (`UnitRow`, `units`), Batch B16M.
- GLOSSARY: none (`FieldOutcome` is a type, not a new word; *end state* is B17.01's row).
- NAMES: `drawn: ((subformation, cohort, troops), ...)` → `((unit, cohort, troops), ...)`; `(side, subunit index)` → `(side, unit index)`; "while its unit stands" → "while its army stands" (B16L, B16M).
- COST and TIER: small build (the outcome record and per-cohort shares); `sonnet`, `high`.
- LANDS IT: B17's producer; `Item: B17.03`, `[skip ci]`.

### B17.04 — a side past the ceiling, or of nobody, never reaches the cell engine · U5b_MB_residue §6 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5b_MB_residue.md` §6 (`audits/16_PESSIMIST_MB.md` §3.3); closes the pessimist's extremes rows.
- ADVANCES: none of the nine; R's completeness at the extremes (a field never resolves a shape the module cannot hold).
- INSTRUCTION (copied):
  0. Write the scratch probe the source names as a file first: `systems/mass_battle/sim/extremes_probe.py` ("written first … expected output the three lines above": 0 a side and 1 a side never enter `run_battle`; 20,000 a side returns `SCALE-GAP`), run it, and record its before-reading in the commit body (red: today 20,000 a side resolves and one man a side reaches the engine).
  1. "`modules/mass_battle/massbattle.py::resolve_field`: a side past the module's stated ceiling (`MAX_TROOPS_PER_UNIT`) is refused with a typed result (`status="SCALE-GAP"`, on `PARTY-GAP`'s shape), not resolved. Today 20,000 a side resolves." (`PARTY-GAP`'s shape is the dict `seam/wrappers/mass_battle.py::resolve` returns, `dict(status=…, why=…)`; `SCALE-GAP` joins `seam/contest.py::REFUSAL_STATUSES` beside `PARTY-GAP` and `REFUSED` so the seam reads it as a refusal `[ASSUMPTION: the seam must recognise the new status as a refusal — basis: `REFUSAL_STATUSES` is the seam's one set of refused statuses; the source names the shape only]`.)
  2. "A field of nobody against nobody, or of two sides below the floor, is the host's `Unopposed` / `PARTY-GAP` branch and never reaches the cell engine (today the crash floor of one man a side resolves and the attacker 'loses'). After `04_MB_headcount_grade_and_scale.md` and the squad entry, the only sides that reach `resolve_field` are blocks."
- WHERE: `modules/mass_battle/massbattle.py` (`resolve_field`); `engine/season/seam/contest.py` (`REFUSAL_STATUSES`); `engine/season/seam/wrappers/mass_battle.py` (`resolve`, the floor test); NEW `systems/mass_battle/sim/extremes_probe.py`; `engine/season/tests/test_mass_battle_module.py`.
- TESTS (written before the edit, read red): `engine/season/tests/test_mass_battle_module.py::test_past_the_ceiling_returns_scale_gap`, `::test_empty_sides_never_reach_run_battle`.
- FALSIFIER and CONTROL: a side of 20,000 resolved, or one man a side entering `run_battle`. Control: the realm content hash at seed 0 and seed 2, one season, equal to B17.03's reading ("Movers. None in shipped play").
- GATE: `python systems/mass_battle/sim/extremes_probe.py` → the three expected lines; `python -m pytest engine/season/tests/test_mass_battle_module.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B17.01 (blocks are the only sides that reach `resolve_field`), B17.03 (the typed return beside which the refusal is a dict); EXISTS-IN-TREE `config.MAX_TROOPS_PER_UNIT`, `seam/contest.py::REFUSAL_STATUSES`.
- GLOSSARY: none.
- COST and TIER: small build; `sonnet`, `high`; the probe `haiku` (`valoria-measure`).
- LANDS IT: B17's producer; `Item: B17.04`, `[skip ci]`.

### B17.05 — one code path: the unreached loops move to the workbench; dead code deleted · 04_MB_typed_outcome_and_one_path §2 (its commit 2) · BUILD · HASH EQUAL
- SOURCE: `proposals/04_MB_typed_outcome_and_one_path.md` §2 (bullets 1–4, 6–7; the fifth is B17.07), "Implementation" order (2), "Gate" 1–3; rulings A-1 (Layer 1 §27.2 conformance, confirmed); closes F-MB-09, F-MB-10 (R-10, R-15, R-21).
- ADVANCES: none of the nine; one body of code for the season and the port.
- INSTRUCTION (§2, copied, with the cut UNDECIDED (5) states):
  1. "`run_multi_turn_battle`, `run_multi_unit_battle`, `between_turn_recovery`, `reset_morale_between_battles`, `reset_positions`, … `unit_in_reserve`, `freed_attacker_damage` and `Unit.base_combat_pool` move from `modules/mass_battle/` to `systems/mass_battle/sim/multi.py`, beside the harnesses that call them (`engine.py::resolve_battle`, `bat.py`, `validators.py`). They import the module; the module does not import them." `Unit.base_combat_pool` is the engine's `Army.base_combat_pool` after B16M; it moves as a function of the army taking the army as its argument, every caller in `multi.py`, `bat.py` and `validators.py` re-pointed. **Not moved (UNDECIDED (5))**: `pursuit_damage`, `recall_check`, `feigned_retreat_recognized`, `feigned_retreat_check`, `resolve_feigned_retreat` stay in `orchestration.py`, because B19 (`16_PESSIMIST_MB_rout_has_two_exits`, `27_MB_A` 27A-5, `27_MB_C` 27C-1, MBA-04 step 5) and B20 (`26_MASS_BATTLE_maneuver_orders`) edit them there and give them a season caller; `multi.py` imports them.
  2. "`systems/mass_battle/sim/workbench/trace.py::run_traced_battle` takes `kind='field'` as its default: it builds a `MassBattleInput` and calls `massbattle.resolve_field` under `resolution.tracing()`."
  3. "Deleted outright: `orchestration.threadwork_check`, `Subunit.halt_before_enemy` and their call sites (the archived integration spec ordered `halt_before_enemy` deleted in May 2026; it is still called twice a tick). `rally_check` is **kept as the commander's hook, not deleted** … until that lands it stays the no-op it is. Also deleted: `tactic_cards.py`; `altonian_reinforcements.py` (each with its `FORK:` row in `references/restructure_ledger.md`, and the pointers at `registers/placeholder_names.yaml` and in `registers/mechanics_index.yaml`)." The two files are `systems/mass_battle/sim/tactic_cards.py` and `systems/mass_battle/sim/altonian_reinforcements.py`; each row: `| \`systems/mass_battle/sim/<file>\` | \`FORK:<sha>\` | FORKED (<date>, workplan v12 B17.05: unreached by any season arm, \`04_MB_typed_outcome_and_one_path.md\` §2; \`<sha>\` is the last commit carrying the file) |`, read back as an exact row through `pathres.load_alias_map()` (CLAUDE.md §8). `orchestration.__all__` loses every moved and deleted name.
  4. "`massbattle.py`'s module docstring is cut to what the file is."
  5. "The provider's `resolver="dice_pool"` key is dropped from its three return shapes" (the `PARTY-GAP`, `Unopposed`/`Invested` and refusal dicts `seam/wrappers/mass_battle.py::resolve` returns; the `FieldOutcome` arm has none).
  6. Record in the commit body the reach probe of gate 1 (`audits/04_MB_audit.md` §12, re-run): every function left under `modules/mass_battle/` is entered by a season arm or by one of the four query rows, **except** the five of step 1's cut, each named with the batch that gives it a season caller (B19, B20).
- WHERE: `modules/mass_battle/orchestration.py` (the moved functions, `threadwork_check`, `__all__`); `modules/mass_battle/hierarchy/units.py` (`Unit.halt_before_enemy`, `Army.base_combat_pool`); `modules/mass_battle/massbattle.py` (docstring); `engine/season/seam/wrappers/mass_battle.py` (`resolve`'s return shapes); NEW `systems/mass_battle/sim/multi.py`; `systems/mass_battle/sim/engine.py`, `bat.py`, `validators.py` (imports); `systems/mass_battle/sim/workbench/trace.py` (`run_traced_battle`); DELETE `systems/mass_battle/sim/tactic_cards.py`, `systems/mass_battle/sim/altonian_reinforcements.py`; `references/restructure_ledger.md` (two `FORK:` rows); `registers/placeholder_names.yaml`; `registers/mechanics_index.yaml`.
- TESTS: none new; the covering files `tests/valoria/test_field_golden_pins.py` and every test `python tools/tests_for_diff.py` names for the moved files stay green (a test that imported a moved function from `modules/` imports it from `systems.mass_battle.sim.multi`).
- FALSIFIER and CONTROL: "A season arm that enters a function now under `systems/`." Control: `python tools/ci_golden_modes_check.py` digests equal to B17.04's reading ("the moves and the config object change no arithmetic", gate 3).
- GATE: `python tools/ci_golden_modes_check.py` → `[BYTE-EXACT OK]`, digests equal to B17.04's; `git grep -n "threadwork_check\|halt_before_enemy\|run_multi_turn_battle\|run_multi_unit_battle" modules engine` → nothing; `git grep -n "import.*systems" modules/mass_battle` → nothing; the realm hash at seed 0, one season → equal to B17.04's; `python -m pytest tests/valoria/test_field_golden_pins.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B17.03 (`run_traced_battle` builds the typed input and reads the typed outcome); EXISTS-IN-TREE every function named in step 1, `orchestration.rally_check`, `threadwork_check`; V12 Batch B16M (`Army`, `Unit`).
- GLOSSARY: none.
- NAMES: `Unit.base_combat_pool` → `Army.base_combat_pool`; `Subunit.halt_before_enemy` → `Unit.halt_before_enemy` (B16M).
- COST and TIER: edit, large and mechanical (moves, deletions); `sonnet`, `high`, "the moves `haiku`-assisted for the mechanical edits" (the source).
- LANDS IT: B17's producer; `Item: B17.05`, `[skip ci]`.

### B17.06 — the first skill input waits for `CommandRecord` · 04_MB_typed_outcome_and_one_path §4 · POINTER · —
- SOURCE: `proposals/04_MB_typed_outcome_and_one_path.md` §4 (Reconciled W3-1, D-U1-11g, U1 §4 M-23).
- What the pointed section does: the integer `MassBattleInput.command: tuple = (4, 4)` it once proposed is removed (it never entered the tree: `queries/inputs.py::MassBattleInput` holds no `command` at `aa31fd2`); the commander's and each officer's `command` skill reaches the field as `CommandRecord` (`27_MB_A_command_and_the_obedience_draw.md` §2, B19), and "the old integer and `core/exchange.py::derive_command` retire with it", `command_span` keeping its name.
- Target files and symbols: `modules/mass_battle/core/exchange.py::derive_command`, `config.CMD_CHA_WEIGHT`, `CMD_COG_WEIGHT`; their caller `hierarchy/units.py` (`Army`, `Officer` `__post_init__`).
- Where it lands: with `27_MB_A` in B19 (UNDECIDED (2)): `derive_command` is live module code at `aa31fd2`, so neither it nor the two weights move in B17.
- Gate: none here; B19's `27_MB_A` item reads `git grep -n derive_command modules` → nothing at its close.

### B17.07 — one list of unit roles that leave the menu · U5b_MB_residue §1 with 04_MB_typed_outcome_and_one_path §2 fifth bullet (its commit 4) · BUILD · HASH EQUAL
- SOURCE: `proposals/U5b_MB_residue.md` §1 (which "replaces the list in `04_MB_typed_outcome_and_one_path.md` §2 (its fifth bullet) and the list under F-PES-MB-08"); `04_MB_typed_outcome_and_one_path.md` "Implementation" order (4); closes R-10 (first audit), F-PES-MB-08; `IS-MB-P4`.
- ADVANCES: none of the nine; a menu offers no choice that cannot matter (a choice that matters, `IS_B1_PC_MB_DICE_part2.md` P2-1.0).
- INSTRUCTION (§1, copied):
  0. Write the scratch probe as a file first: `systems/mass_battle/sim/role_edges_probe.py` — "each unit role against no role, friction off, n 60, printing the count of identical fields; expected after the edit: no row at 60 of 60". Run it before the edit and record its rows in the commit body.
  1. The one list, decided:

     | role | off which menus | why | returns when |
     |---|---|---|---|
     | `Pursue` | every menu (cavalry, light cavalry, light infantry) | its instruction `pursue` maps to `None`; identical to no role in 60 of 60 | `16_PESSIMIST_MB_rout_has_two_exits.md` gives `pursue` its primitive (`may_pursue`) |
     | `Screen` | every menu | keyword `screen` has no primitive; identical in 60 of 60 | a primitive exists |
     | `Harass` | every menu | keyword `harass` has no primitive; its `GappedLine` shape is gone at tick 1 (F-MB-18) | a primitive exists and R-24 holds |
     | `Feint` | every menu | reached only through `resolve_feigned_retreat`, which no season path calls; identical in 60 of 60 | `26_MASS_BATTLE_maneuver_orders.md` reaches the feint |
     | `VolleyLine` | stays as a shape; its instruction tuple is emptied (`volley`, `loose`, `shoot_move` have no primitive) | identical in 60 of 60 for archers | — |
     | `Anvil` (heavy infantry against foot) | stays: it differs against horse (`brace_probe`) | recorded: inert against foot | — |
     | `Flanker`, `Shock` | stay: they are behaviours, not no-ops, and both lose (13 against 42; 16 against 41) | the addendum's F-MB-21 class; ride with `04_MB_manager_battle_one_resolver.md` §3's bar … and are read again after the pair rule changes | — |
  2. "Edits: `modules/mass_battle/config.py` (`TROOP_TYPE_ROLES`, `ROLE_SPEC`: the rows above; when the troop file lands they are the `roles` column of `references/troops.yaml`); the keywords `pin`, `loose`, `screen`, `pursue`, `volley`, `shoot_move`, `harass` leave `ROLE_SPEC`" (per `hierarchy/units.py::ROLE_INSTRUCTION_PRIMITIVES`' own table). "A role returns when a primitive exists for it."
- WHERE: `modules/mass_battle/config.py` (`TROOP_TYPE_ROLES`, `ROLE_SPEC`); NEW `systems/mass_battle/sim/role_edges_probe.py`; `tests/valoria/test_mass_battle_role_instructions.py`.
- TESTS (written before the edit, read red): `tests/valoria/test_mass_battle_role_instructions.py::test_no_menu_offers_a_role_without_a_primitive`. The file's existing `test_every_role_keyword_is_classified` stays green.
- FALSIFIER and CONTROL: "A menu row whose removal changes a field." Control: `python tools/ci_golden_modes_check.py` digests equal to B17.05's reading.
- GATE: `python systems/mass_battle/sim/role_edges_probe.py` → no role on any menu reads "identical in 60 of 60" against no role; `python tools/ci_golden_modes_check.py` → digests equal; `python -m pytest tests/valoria/test_mass_battle_role_instructions.py -q` → pass.
- HASH MOVERS: none ("no shipped person forms an army verb, so no season moves").
- DEPENDS ON: V12 B17.05 (`resolve_feigned_retreat`'s home settled); EXISTS-IN-TREE `config.TROOP_TYPE_ROLES`, `config.ROLE_SPEC`, `hierarchy/units.py::ROLE_INSTRUCTION_PRIMITIVES`.
- GLOSSARY: none (the glossary's *role* row already reads "unit role", qualified).
- COST and TIER: edit; `sonnet`, `high`; the probe run `haiku` (`valoria-measure`).
- LANDS IT: B17's producer; `Item: B17.07`, `[skip ci]`.

### B17.08 — `GappedLine`'s minimum Discipline lets its roles keep their shape · U5b_MB_residue §9 R-24 · BUILD · HASH MOVER(behaviour)
- SOURCE: `proposals/U5b_MB_residue.md` §9 row R-24; closes R-24 (first audit), F-MB-18.
- ADVANCES: none of the nine; a role a menu offers holds the shape it names.
- INSTRUCTION (R-24, copied; the source's first branch): "`modules/mass_battle/config.py::MIN_DISCIPLINE` (the troop file's header when it lands): `GappedLine`'s minimum is set to the Discipline of the lightest troop type whose menu offers a `GappedLine` role (2, per the audit's run), so `Skirmish` and `Kite` keep their shape past tick 1". At `aa31fd2` the row reads `"GappedLine": 5`; the item first reads, from `TROOP_TYPE_ROLES` and the troop stats, the lightest Discipline among types offering a `GappedLine` role after B17.07, records it in the commit body, and sets the value to it (the source expects 2). The source's other branch ("where a type is not meant to hold it, the role leaves that type's menu") is not taken: no type's menu is named for it.
- WHERE: `modules/mass_battle/config.py` (`MIN_DISCIPLINE`); `tests/valoria/test_mass_battle_role_instructions.py`.
- TESTS (E-3; the audit's one-tick probe restated as a named test, written before the edit, read red): `tests/valoria/test_mass_battle_role_instructions.py::test_every_gapped_line_role_keeps_its_shape_past_tick_one` `[ASSUMPTION: test name; the item creates it]`.
- FALSIFIER and CONTROL: a `GappedLine` role that reads another shape after tick 1 on a type that offers it. Control: the realm content hash at seeds 0 and 2, one season, equal to B17.07's reading (army fields only: "none in natural play").
- GATE: "the audit's one-tick probe: every `GappedLine` role still reads `GappedLine` after tick 1 on each type that offers it" (the test above → pass); `python tools/ci_golden_modes_check.py` → read: equal, or each moved mode named in the commit body and re-pinned at B17.99.
- HASH MOVERS: "R-24 … move[s] fields in which a body drifts (army fields only; none in natural play)": any workbench digest whose battery fields a `GappedLine` body. Declared; re-pinned in B17.99 if moved.
- DEPENDS ON: V12 B17.07 (the role list the minimum is read from); EXISTS-IN-TREE `config.MIN_DISCIPLINE`.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B17's producer; `Item: B17.08`, `[skip ci]`.

### B17.09 — conservation claims compared exactly · U5b_MB_residue §4 item 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/U5b_MB_residue.md` §4 item 2 (`audits/01_CORE_audit_addendum_C_tests.md` F-TEST-10 row 6, handed across by U5a); CLAUDE.md §0.1 pt 2.
- ADVANCES: none of the nine; an assertion that can observe the failure it excludes.
- INSTRUCTION:
  1. SITE (the source's `[UNVERIFIED: which of the 35]`): `git grep -n "approx" tests/valoria` over the mass-battle test files, and open each hit; list in the commit body every `approx` whose claim is a troop-count conservation (`tests/valoria/_conservation.py`, `test_frontage_conservation.py` first) and every one left as a sampled reading.
  2. "Each `approx` on a troop-count conservation becomes an exact comparison on the integer count, or on the float with the engine's own epsilon named at the site (`resolution.py`'s)". "Tolerances on win shares and other sampled readings stay." "No new test file and no CI row."
- WHERE: `tests/valoria/_conservation.py`; `tests/valoria/test_frontage_conservation.py`; the other files step 1 lists.
- TESTS: the edited assertions themselves.
- FALSIFIER and CONTROL: "With one troop removed in process inside `distribute_casualties`, the conservation tests fail." Control: unpatched, they pass.
- GATE: `python -m pytest tests/valoria/test_frontage_conservation.py <the files step 1 lists> -q` → pass; the same run with `modules.mass_battle.percell.distribute_casualties` monkeypatched in a scratch `conftest` (not committed) to drop one troop → the conservation tests fail; both readings in the commit body.
- HASH MOVERS: none.
- DEPENDS ON: EXISTS-IN-TREE `modules/mass_battle/percell.py::distribute_casualties`, `tests/valoria/_conservation.py`; V12 Batch B16M (the names the tests use).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, medium.
- LANDS IT: B17's producer; `Item: B17.09`, `[skip ci]`.

### B17.10 — the troop file, its exporter and its loader; the tables become reads · 04_MB_unit_loadout_and_weapon_in_hand_B stage 1 · BUILD · HASH EQUAL
- SOURCE: `proposals/04_MB_unit_loadout_and_weapon_in_hand_B.md` §1, §2, §3, "Stages and gates" row 1, "Tests (W3-1)" stage 1, "Call sites"; its Folded line (27_MB rulings: the `infantry` row); rulings A-2, A-59 (2); D-U1-11c, D-U1-11d; closes F-MB-22, F-MB-23, C-3 (R-35, R-36); U3 §6.3 names this item the only carrier of `references/troops.yaml`, `tools/export_troops.py` and `troop_types/table.py`.
- ADVANCES: none of the nine; a troop type is one row a designer edits.
- INSTRUCTION (§1–§3, copied):
  1. "Authored head: `references/troops.yaml` (owner MB). Export: `engine/engine_params/troops.json` by `tools/export_troops.py`, with the blocking `--check` round-trip the order vocabulary already has (`tools/export_battle_orders.py` → `battle_orders.json`)." Wired as that precedent is: a row in `references/ci_checks_registry.yaml` beside `tools/export_battle_orders.py`'s and a `('export_troops.py', ['--check'], True)` entry in `tools/valoria_local.py` (CLAUDE.md §0 step 4, precedent); the caller the accretion pass reads is `tests/valoria/test_export_troops.py::test_round_trip`.
  2. `arms` and `classes`, exactly:
     ```yaml
     arms:
       light_cut:   {class: non_pole, mass_kg: 1.2}
       heavy_cut:   {class: pole,     mass_kg: 2.0}
       heavy_blunt: {class: pole,     mass_kg: 1.5}
       spear:       {class: pole}                          # mass from personal combat's export (its key `spear`)
       arming:      {class: non_pole}                      # mass from personal combat's export (its key `arming`)
       pike:        {class: pike,     mass_kg: 3.5}
       bow:         {class: missile,  mass_kg: 2.0, range: [2, 8], volleys: 10}
       crossbow:    {class: missile,  mass_kg: 4.0, range: [2, 8], volleys: 10}
       sling:       {class: missile,  mass_kg: 0.8, range: [2, 8], volleys: 10}
       javelin:     {class: missile,  mass_kg: 2.5, range: [2, 8], volleys: 10}
       siege:       {class: missile,  mass_kg: 0.0, range: [2, 8], volleys: 10}   # crew-served: not carried
     classes:       # the ruled P-DEC-1 map (ED-MB-0014), authored once
       non_pole: {reach: 0.1, support_ranks: 1}
       pole:     {reach: 0.2, support_ranks: 2}
       pike:     {reach: 0.3, support_ranks: 3}
       missile:  {reach: 0.1, support_ranks: 1}      # a missile weapon used hand to hand: REACH_MELEE_DEFAULT
     ```
     "An arm's mass lives in personal combat's typed export when its key is in that roster, and here (`mass_kg`) only when it is not; the loader refuses both." "`range` and `volleys` are today's `VOLLEY_MIN_RANGE`, `VOLLEY_MAX_RANGE` and `MB_VOLLEYS_START`, transcribed." "Every `mass_kg` above is a seed at memory grade … Jordan's content" (PR body, D-19).
  3. `troops`: one row per troop type, "a transcription of today's constants", in the form of the source's `pike` row:
     ```yaml
     troops:
       pike:
         power: 4            # today's stat line, transcribed
         discipline: 4
         morale: 5
         strength: 3         # the score the carry demand is charged against (new; seed rule below)
         mounted: false      # speed, deployment on the flanks
         charge: 0           # charge penetration: 3 for today's `cavalry`, 0 otherwise
         wheel: false        # the fast enveloping wheel: today's `cavalry`, `light_cavalry`
         default_role: null  # `Kite` for today's `mounted_archers`
         cell_cap: 200       # densest troops a cell: 100 for the four horse types today
         ranks: 4            # the unit's default depth (04_MB_cell_hierarchy_as_data.md)
         primary: pike
         secondary: null     # an `arms` key, or null
         armour: medium      # none | light | medium | heavy
         roles: [ShieldWall, Hold, Anvil]
         training_site: barracks
         min_site_condition: 0.0
         upkeep: 0           # 04_MB_campaign_party_economy.md
     ```
     Every row's values are read from the twelve tables of "the problem" item 1 (`TROOP_TYPE_STATS`, `TROOP_TYPE_REACH`, `MOUNTED_TYPES` in `troop_types/registry.py`; `TROOP_TYPE_DENSITY_CAP`, `TROOP_TYPE_ROLES` (as B17.07 left it), `ROLE_SPEC` in `config.py`; `TROOP_LOADOUT`, `ARSENAL`, `ARMOURY` in `equipment/`; `TRAINING_SITE` in `troop_types/recruitment.py`; `ARM_SHARES`, `ROLE_OF` in `troop_types/presets.py`), every `secondary: null`. "**`strength` seed rule:** the smallest whole number at or above the demand of the row's own armour, so that a type carrying only its primary pays nothing, as today." "Knights templar keeps today's behaviour at landing (`mounted: false`, `cell_cap: 100`, lance class)." One more row (the Folded line): "`infantry`, the unmustered body of a side with no army Record, carrying the literals that side lends it today (`power: 4`, `discipline: 5`)". `ranks` is today's default depth where the tree has one, else 1 `[ASSUMPTION: `04_MB_cell_hierarchy_as_data.md` (B19) authors depth; at landing a unit is the depth the tree builds today — basis: loadout_B §5 "today's one-rank bodies"; nothing reads `ranks` before B19]`.
  4. "Reader: `modules/mass_battle/troop_types/table.py`, loaded once. It reads a data file and imports no `engine` code. It refuses, by name: an unknown column; a troop row naming an arm, armour tier, role or site kind that is not a member of its closed set; an arm whose mass is stated both here and in personal combat's export; a `secondary` equal to the `primary`. The third refusal reads `engine/engine_params/combat_engine_v1.json` (its `weapons` section) as a **data** dependency, never an import of `modules/combat/`."
  5. "Every table in 'the problem' item 1 becomes a function of this loader with its present name and signature (`stats_for`, `reach_for`, `is_mounted`, `cell_cap_for`, `roles_for`, `loadout_for`, `training_site_for`), so no call site changes at stage 1." The old tables are deleted where the function replaces them.
  6. Glossary: rows *kit* and *troops, troop type, levy* (§J): the owner columns become pointers to `references/troops.yaml` and `troop_types/table.py::loadout_for` / `stats_for`; the rejected words kept. Row *power*: unchanged (the column `power` is the tree's stat at landing; B19a and B19 retire it, A-100).
- WHERE: NEW `references/troops.yaml`; NEW `tools/export_troops.py`; NEW `engine/engine_params/troops.json` (re-derived by the tool, never by hand); NEW `modules/mass_battle/troop_types/table.py`; `modules/mass_battle/troop_types/registry.py`, `recruitment.py`, `presets.py`; `modules/mass_battle/config.py` (`TROOP_TYPE_DENSITY_CAP`, `TROOP_TYPE_ROLES`, `ROLE_SPEC`); `modules/mass_battle/equipment/__init__.py`, `weapons.py`, `armour.py`; `references/ci_checks_registry.yaml`; `tools/valoria_local.py`; NEW `tests/valoria/test_export_troops.py`; `unified/U1_GLOSSARY.md` (*kit*, *troops, troop type, levy*).
- TESTS (written before the edit, read red): `tests/valoria/test_export_troops.py::test_round_trip`, `::test_unknown_arm_key_refused_by_name`, `::test_mass_stated_twice_refused` (beside `test_engine_params_bridge.py`); `tests/valoria/test_field_golden_pins.py` for the digests.
- FALSIFIER and CONTROL: an unknown arm key or a twice-stated mass that loads; any digest that moves with every `secondary` null. Control: `python tools/ci_golden_modes_check.py` digests equal to B17.08's reading.
- GATE: "`tools/export_troops.py --check` passes; `python3 tools/ci_golden_modes_check.py` digests equal; an unknown arm key is refused by name; a mass stated twice is refused" → `python tools/export_troops.py --check` → exit 0; `python tools/ci_golden_modes_check.py` → `[BYTE-EXACT OK]`, equal; `python -m pytest tests/valoria/test_export_troops.py tests/valoria/test_field_golden_pins.py -q` → pass; the realm hash at seed 0, one season → equal to B17.08's.
- HASH MOVERS: none ("none at stages 1–3 with every `secondary` null").
- DEPENDS ON: V12 B17.07 (the `roles` column is the cut list), B17.08 (`MIN_DISCIPLINE` read before the header moves); EXISTS-IN-TREE `tools/export_battle_orders.py` (the pattern), `engine/engine_params/combat_engine_v1.json` `weapons`, the twelve tables; V12 Batch B13 (`combat_engine_v1.json` byte-identical after the package move), Batch B14 (`03_PC_weapon_records_in_the_export`: the export's weapon records).
- GLOSSARY: *kit*, *troops, troop type, levy* (step 6). "troop file": `references/troops.yaml`, the one authored table of troop types and arms, as a regiment's books are its file.
- COST and TIER: edit (mechanical, hash EQUAL); `sonnet`, `high`; "`haiku` for the transcription check" (the source).
- LANDS IT: B17's producer; `Item: B17.10`, `[skip ci]`.

### B17.11 — the four name tests become columns; reach derives from the arm · 04_MB_unit_loadout_and_weapon_in_hand_B stage 2 · BUILD · HASH EQUAL
- SOURCE: `proposals/04_MB_unit_loadout_and_weapon_in_hand_B.md` §2 (reach), §3 (the four name tests), "Stages and gates" row 2, "Tests" stage 2, "Falsifier"; `U5b_MB_residue.md` §2 R-37 (the "melee sidearm" comment); closes F-MB-22's name tests.
- ADVANCES: none of the nine; a designer adds a troop type with no code edit.
- INSTRUCTION (copied):
  1. "The four name tests become reads of `charge`, `wheel`, `default_role` and `mounted`" at the sites the source lists: `hierarchy/units.py` (charge; wheel), `orchestration.py` (recoil, two sites), `armies.py` and `orderofbattle.py` (stand-off) — each a `troop_type == '<name>'` test today, opened by symbol and replaced by the loader's column read.
  2. "**Reach and support depth are derived from the arm in hand**, not kept per troop type. The transcription is exact: across today's tables every weapon key is carried only by types of one reach (`light_cut` 0.1; `heavy_cut`, `heavy_blunt`, `spear` 0.2; `pike` 0.3; every missile type 0.1), so `TROOP_TYPE_REACH` and `support_ranks_for` can be deleted with no result moving." `reach_for` reads the primary arm's `class` row.
  3. R-37's last clause: "the 'melee sidearm' comment (`troop_types/registry.py`) goes when `arms` lands" — deleted with `TROOP_TYPE_REACH`.
- WHERE: `modules/mass_battle/hierarchy/units.py`; `modules/mass_battle/orchestration.py`; `modules/mass_battle/armies.py`; `modules/mass_battle/orderofbattle.py`; `modules/mass_battle/troop_types/registry.py` (`TROOP_TYPE_REACH`, `support_ranks_for`, the comment); `modules/mass_battle/troop_types/table.py` (`reach_for`); `tests/valoria/test_mass_battle_order_of_battle.py`.
- TESTS (written before the edit, read red): `tests/valoria/test_mass_battle_order_of_battle.py::test_a_new_row_charges_and_wheels_with_no_code_edit` ("a new row `cataphracts` with `mounted: true, charge: 3, wheel: true` charges, recoils and wheels with no code edit").
- FALSIFIER and CONTROL: "After stage 2, a troop behaviour that still depends on the spelling of a type's name (`grep -n "troop_type == '" modules/mass_battle` prints a line)." Control: digests equal to B17.10's reading.
- GATE: `git grep -n "troop_type == '" modules/mass_battle` → nothing; `python tools/ci_golden_modes_check.py` → digests equal; `python tools/export_troops.py --check` → exit 0; `python -m pytest tests/valoria/test_mass_battle_order_of_battle.py tests/valoria/test_export_troops.py -q` → pass.
- HASH MOVERS: none.
- DEPENDS ON: V12 B17.10 (the columns and `arms`); EXISTS-IN-TREE the six name-test sites, `TROOP_TYPE_REACH`, `support_ranks_for`.
- GLOSSARY: none.
- COST and TIER: edit (mechanical); `sonnet`, `high`.
- LANDS IT: B17's producer; `Item: B17.11`, `[skip ci]`.

### B17.12 — no hidden inputs: the environment reads split between the troop file and an explicit `cfg` · 04_MB_typed_outcome_and_one_path §3 (its commit 3) · BUILD · HASH EQUAL
- SOURCE: `proposals/04_MB_typed_outcome_and_one_path.md` §3, "Implementation" order (3), "Gate" 2–3, "Falsifier"; D-U1-11c (W3-1, 7b-13); `04` §C.12 rejection 4, `holonic_ARCHITECTURE.md` §47; closes F-MB-09's 91 environment reads.
- ADVANCES: none of the nine; every mechanism a field runs is stated in data or in an explicit argument (the port reads one config).
- INSTRUCTION (§3, copied):
  0. Count the reads at the item's open: `git grep -c "environ" modules/mass_battle` (the source measured 91: `config.py` 66, `hierarchy/units.py` 12, `orchestration.py` 11, `core/exchange.py` 2); record the per-file counts and each name in the commit body with its owner of step 1.
  1. "`modules/mass_battle/config.py`: every `os.environ.get(NAME, default)` becomes the default. Each of the 91 reads goes to one of two owners, never both: a column of a row a designer edits (a troop, an arm, a terrain, a formation, a doctrine, a fatigue rate, an `orders.obey` step) moves to `references/troops.yaml`, exported to `engine/engine_params/troops.json` by `tools/export_troops.py --check`; a global engine coefficient stays a literal in `config.py`, exported to `engine/engine_params/mass_battle_v1.json` by a section of `tools/export_engine_params.py --check`; the loader refuses a name present in both."
  2. "A frozen `EngineConfig` dataclass is the typed in-memory form of those literals (`config.DEFAULT`, the shipped instance), **passed to `resolve_field(inp, rng, *, cfg=None, troops_a=None, troops_b=None, decide=None, duel=None)` as an explicit `cfg` parameter**, as `fight(inp, rng, decide, cfg)` does in personal combat; there is no `config.active()` and no `config.using()` (no ambient selector: `04` §C.12 rejection 4, `hol` §47). `os.environ` is read only under `systems/mass_battle/sim/`, which builds a variant with `replace(DEFAULT, PER_CELL=False)` and passes it." The reads in `hierarchy/units.py`, `orchestration.py` and `core/exchange.py` become reads of the `cfg` threaded from `resolve_field` (or of the troop file for a row value). `decide` and `duel` are keyword parameters with default `None` that nothing passes yet (B20, B30).
  3. "`equipment/_base.py::Registry.override` and `remove` are deleted (no caller)."
  4. The pinned battles (UNDECIDED (4)): `systems/mass_battle/sim/bat.py` builds its `EngineConfig` from the environment variables `tools/ci_golden_modes_check.py` pins, through `replace(DEFAULT, …)`; `tests/valoria/test_field_golden_pins.py`'s drift guard compares each pin with the `config.DEFAULT` field of that name, not with a source-level `environ.get` default (§3's sentence "`os.environ` is read only under `systems/mass_battle/sim/`").
- WHERE: `modules/mass_battle/config.py` (`EngineConfig`, `DEFAULT`, every environment read); `modules/mass_battle/hierarchy/units.py`; `modules/mass_battle/orchestration.py`; `modules/mass_battle/core/exchange.py`; `modules/mass_battle/massbattle.py` (`resolve_field`'s signature); `modules/mass_battle/equipment/_base.py` (`Registry.override`, `remove`); `references/troops.yaml` (the row-shaped values); `tools/export_troops.py`; `engine/engine_params/troops.json` (re-derived); `tools/export_engine_params.py` (the `mass_battle_v1` section); NEW `engine/engine_params/mass_battle_v1.json` (re-derived); `systems/mass_battle/sim/bat.py`, `engine.py`, `validators.py`, `workbench/trace.py`, `multi.py` (each builds and passes its variant); `tests/valoria/test_field_golden_pins.py`.
- TESTS: `tests/valoria/test_field_golden_pins.py` (re-pointed, step 4) green; `tests/valoria/test_export_troops.py` gains `test_a_name_in_both_owners_is_refused` `[ASSUMPTION: test name; the item creates it — the source states the refusal, not its test]`, written before step 1 and read red.
- FALSIFIER and CONTROL: "a run whose outcome changes when an `MB_*` variable is exported" (run `ci_golden_modes_check.py` once with an `MB_*` variable exported in the shell outside its pins: digests unchanged). Control: digests equal to B17.11's reading ("the moves and the config object change no arithmetic").
- GATE: "`git grep -n "environ" modules/mass_battle` prints nothing" → nothing; `python tools/ci_golden_modes_check.py` → `[BYTE-EXACT OK]`, digests equal to B17.11's; `python tools/export_troops.py --check` → exit 0; `python tools/export_engine_params.py --check` → exit 0; `python -m pytest tests/valoria/test_field_golden_pins.py tests/valoria/test_export_troops.py tests/valoria/test_engine_params_bridge.py -q` → pass; the realm hash at seed 0, one season → equal to B17.11's.
- HASH MOVERS: none ("the rest EQUAL").
- DEPENDS ON: V12 B17.10, B17.11 (the troop file and its exporter, which §3's row values move into; U3 §1.2, U6 R-A); B17.05 (the harness code in `multi.py` that builds variants); EXISTS-IN-TREE `tools/export_engine_params.py`, `modules/combat`'s `fight(inp, rng, decide, cfg)` (after B13, `modules/combat/`), `equipment/_base.py::Registry`.
- GLOSSARY: none.
- COST and TIER: edit, large and mechanical (the config object); `sonnet`, `high` ("the record and config `sonnet`", the source).
- LANDS IT: B17's producer; `Item: B17.12`, `[skip ci]`.

## Readings (B17)

**Reading 1** (B17.13, `IS-MB-05`, `master/instructions/IS_B1_PC_MB_DICE_part2.md` "Item: IS-MB-05", copied byte for byte):
"at the close of B17, B20, B22 and B23 the last commit body quotes `python -m engine.season.harness.aperture 2 s`, s = 0, 1, 2: the `ENGINES` lines for `mass_battle.resolve_field`, `mass_battle.army`, `mass_battle.army_order`; the counts of `field.won`, `field.lost`, `field.drawn`, `field.unopposed`, `siege.pressed`; `attempted` and `executed` for `march`, `marshal`, `recruit`, `form_unit`, `assign_troops`, `order_unit`. Each reading names its SHA and is taken once."
Expected after B17 (its GATE): "at seed 2 the battle the realm fights is `field.won`, `field.lost` or `field.drawn` and no longer the artefact of the shipped scale". Falsifier's control: "before B17, `resolve_field` reads 0 in the first season at seed 0 (`master/HOLISTIC_AUDIT.md` §3)". Depends on CI-11's `ENGINES` block (B02). Run by `haiku`; read by the BATCH-CLOSE; quoted in B17.99's commit body.

### B17.99 — re-pin and close readings · V12_STRUCTURE_part4.md E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; `04_MB_headcount_grade_and_scale.md` gate 5 ("Seed 2's one-season pin is re-recorded, and the commit says so").
- ADVANCES: the batch's readings on one tree.
- INSTRUCTION:
  1. Re-record, once, every pin the batch moved: `engine/season/tests/_realm_goldens.py` (seed 2's one-season pin; any other seed whose reading moved, each named); `engine/season/tests/test_go07_canonical_digest.py`'s vectors where they moved; the `bat.py` field digests in `tools/ci_golden_modes_check.py` only where B17.01's or B17.08's commit body named a moved mode. The baseline is B16M's close (`reading @<sha>`), or B07's merge where B07 merged first in S9 (`V12_STRUCTURE_part3.md` §7.4). The commit says "re-pin: every fought field (B17.01; B17.03 on the army path; B17.08 where named)".
  2. Run Reading 1 (`aperture 2 s`, s = 0, 1, 2, `PYTHONHASHSEED=0`) and quote it.
  3. Take the batch gate's seeded readings (seeds 0 to 2, E-2) and the close record of the BATCH GATE line.
- WHERE: `engine/season/tests/_realm_goldens.py`; `engine/season/tests/test_go07_canonical_digest.py` (if moved); `tools/ci_golden_modes_check.py` (if a mode moved).
- TESTS: every test named in the BATCH GATE green after the re-pin.
- FALSIFIER and CONTROL: a pin moved that no item declared (then an item is wrong, not the pin). Control: seed 0's realm hash equal to B16M's close.
- GATE: the BATCH GATE.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: V12 B17.01 to B17.12.
- GLOSSARY: none.
- COST and TIER: reading and re-pin; `sonnet`, `high`; Reading 1 `haiku`.
- LANDS IT: B17's producer; `Item: B17.99`, the batch's last `Item:` commit (no `[skip ci]`).

| STOP. Batch B17-mb-scale closes here |
