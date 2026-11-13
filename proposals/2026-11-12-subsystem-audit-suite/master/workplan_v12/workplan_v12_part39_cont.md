# Workplan v12 — part 39, continued: batch B31-mb-loadout-economy

## Status: PROPOSED (the continuation of `workplan_v12_part39.md`, author lane A39; same status, same paths and words as that file's head; resolves nothing at runtime, CLAUDE.md §0.05)

---

## Batch B31-mb-loadout-economy · lane MB · wave W18 · step S19 · HASH MOVER, one re-pin
INVOCATION: /methodology-execute Batch B31-mb-loadout-economy
IN-FLIGHT ROW: registers/handoffs/HANDOFF_MB.md, Open table
GATE: Batch B00-ids
GATE: Batch B01-laneA
GATE: Batch B02-tests
GATE: Batch B16L-mb-words
GATE: Batch B17-mb-scale
GATE: Batch B18-pc-content
GATE: Batch B19-mb-field-calibration
GATE: Batch B20-mb-orders          (added by this part: `04_MB_unit_loadout_and_weapon_in_hand_B` stages 3–4 depend on `04_MB_manager_battle_one_resolver.md` §2, B20; §2.1's list lacks it; UNDECIDED (1))
GATE: Batch B22-mb-armies          (added by this part: `04_MB_campaign_party_economy` depends on `27_MB_E` (B22, the `assigned`/`absent` write); §2.1's list lacks it; UNDECIDED (1))
REQUIREMENT: none — rulings A-69 (armies carry fatigue back), A-78, A-113 (stated matchup rows), A-59 (2) (a unit's prowess from its own row), A-2 (a unit is a row); `IS_A_NINE_part2.md` §12's M5 lists B31 (none moves; all nine re-read at B40)
BATCH GATE (read once, on the closing tree, `PYTHONHASHSEED=0` on every seeded command; no command past two seasons, A-114):
  `python tools/export_troops.py --check` → exit 0; `python tools/export_mb_contact.py --check` → exit 0 (B19a); `python tools/export_sim_params.py --check` → exit 0 (the four stamina and speed constants leave `sim_params.json`);
  `python tools/ci_golden_modes_check.py` → every digest equal to B30's close at the controls (B31.02 to B31.16, `reading @<sha>`), then moved by B31.17 to B31.20 as declared and re-recorded by B31.99;
  `python tools/calibrate_mb_contact.py --trust` → seven `ok` lines; `--spot 20` → twenty `inside` lines (MBA-09's gate, "as MBA-02");
  `python -m pytest tests/valoria/test_export_troops.py tests/valoria/test_field_golden_pins.py tests/valoria/test_mass_battle_ammo.py tests/valoria/test_mass_battle_order_of_battle.py tests/valoria/test_mass_battle_terrain.py tests/valoria/test_mass_battle_maneuvers.py tests/valoria/test_mass_battle_role_instructions.py tests/valoria/test_mass_battle_entry_stamina.py tests/valoria/test_mass_battle_army_record.py tests/valoria/test_mass_battle_matchups.py tests/valoria/test_army_battle.py engine/season/tests/test_mass_battle_module.py engine/season/tests/test_march.py -q` → all pass;
  `git grep -n "MB_CAVALRY_SPEED_MULT\|MB_ENVELOP_SPEED_MULT\|MB_STAMINA_DRAIN\|MB_STAMINA_REST\|_SEASON_FORCE_POWER\|_UNIT_POWER\|_UNIT_DISCIPLINE" modules/ engine/` → nothing; `grep -n "troop_type == '" modules/mass_battle` → nothing;
  the realm content hash of `build_realm(s)` after one and two seasons, s = 0, 1, 2 → moved only by the declared flips (B31.17 to B31.19) and MBA-09's rows (B31.20) where a field is fought, recorded by the re-pin; the executed-verb tallies equal to B30's close (`reading @<sha>`) through B31.16;
  `python -m engine.season.harness.register --check` → exit 0; `--requirements` → nine lines; `python tools/m1_acceptance.py --summary` → its verdict line quoted; the suites `python tools/tests_for_diff.py --base <batch-start-sha>` names (engine core and registries are touched: the full gates);
  the glossary rows each item names, read against the code it landed;
  the close's commit body records `register --requirements` (nine lines), `m1_acceptance --summary`'s verdict line, the `BUILT OUT`, `ENGINES` and `NULL SCENES` lines before (`reading @<sha>`) and after, every seed value the batch landed (for Jordan, D-19), and the batch's measured wall time; no conjunct is named, so no `reading:` record is written; `status:` is not edited (`IS-A-12`).
RE-PIN: once, in B31.99: `tools/ci_golden_modes_check.py`'s digests, `tests/valoria/test_field_golden_pins.py`'s pins, every `engine/tests/` golden with a field, and the realm pins in `engine/season/tests/_realm_goldens.py`, read against B30's close (`reading @<sha>`); the commit says "re-pin: the three movement flips (B31.17 terrain pace, B31.18 fast-move drain, B31.19 entry shares) and the stated matchup rows (B31.20); every other item at its control, read equal".
IDS: ED-MB 0; H 0
DIALS AT CONTROL:
  `references/troops.yaml: veterancy.arm` = `off` (and `veterancy.ob` unset); set by B98; target: none stated (`04_MB_campaign_party_economy` gate 3 is "a reading of mechanism, not a balance target"; `ob` has no value in any source) → B98 writes it `BLOCKED (design: no target reading)`;
  `troops.<kind>.upkeep` = 0 on every row (so `arrears` is never written); set by: none in v12 ("Who pays, and how, is not designed here": FA's and SE's payment path, no proposal named) → B98 `BLOCKED (FA/SE: the payment path and the `arrears` write)`;
  `troops.<kind>.secondary` = null on every row; set by: a content pass (Jordan: which troops carry a second weapon; `04_MB_unit_loadout_and_weapon_in_hand_B` "Content for Jordan"); target: none stated;
  the drill step (a cohort's `arms` skill score as a step on its unit's skill) = absent; set by: the build B31.01's design schedules (no batch; `IS-MB-B2`); target: a calibration against `26_MASS_BATTLE_calibration_targets` (the design names it);
  `terrain.<row>.pace`, `fatigue.fast_move_drain`, `fatigue.entry.*` ship at control in B31.05, B31.06 and are set by this batch's own flips B31.17 to B31.19 (the source: "three flips, each its own commit").
C(B31-mb-loadout-economy): this batch's entries; the plan's head parts; `references/troops.yaml`; `tools/export_troops.py`; `engine/engine_params/troops.json`; `engine/engine_params/mb_contact.json`; `tools/export_mb_contact.py` (B19a); `tools/calibrate_mb_contact.py` (B19a, run only); `references/mb_contact/duel_grid.json` (read);
  `modules/mass_battle/troop_types/table.py` (B17, B19a, B19); `modules/mass_battle/hierarchy/units.py` (`_ORDER_SAFE_FIELDS`, `_ORDER_TRIGGER_KINDS`, `_node_advance`, `rekey_cells`, `check_drift`, `eff_power`, `eff_discipline`); `modules/mass_battle/percell.py` (`update_stamina`); `modules/mass_battle/orchestration.py` (`volley_phase`, `between_turn_recovery`, `resolve_engagements`); `modules/mass_battle/core/volley.py`, `core/contact_draw.py`, `core/contact_table.py` (B19, B19a); `modules/mass_battle/massbattle.py` (`resolve_field`, `_weighted_unit`, `_person_unit`); `modules/mass_battle/orderofbattle.py` (`_spec_for`, `build_unit`, `UnitRow`); `modules/mass_battle/armyrecord.py` (`apply`, `assign`, `to_order_of_battle`); `modules/mass_battle/config.py`; `modules/mass_battle/terrain.py`; `modules/mass_battle/geometry.py`;
  `engine/season/seam/wrappers/mass_battle.py` (`field_input`, `_order_of_battle`); `engine/season/queries/inputs.py` (`MassBattleInput`, `FieldOutcome`); `engine/season/loop/effects_combat.py` (`_eff_march`); `engine/season/rosters.yaml` (`record_kinds.values.army`); `engine/season/verb_table.yaml` (`march`); `engine/season/write_matrix.yaml` (`(Record, subject_matter)`); `engine/substrate/combat_kit.py` (`carry_demand_of`, B18); `engine/engine_params/combat_engine_v1.json` (read);
  the tests named in the items; instruments: `tools/ci_golden_modes_check.py`, `tools/export_sim_params.py`, `tests/sim/gauge_mb.py --results` (B19's MBA-08), `register`, `tools/m1_acceptance.py`, `tools/tests_for_diff.py`; `engine/season/tests/_realm_goldens.py` (B02);
  read whole by B31.20 only: `master/mb_abstraction/MBA_DESIGN_part2.md` §3.2 (the matchup roster and the row schema); by B31.01 only: `proposals/14_VERBS_MILITARY_B_train.md` §1 item 3;
  the closing SHAs of B00, B01, B02, B16L, B17, B18, B19, B20, B22; the permanent surface (CLAUDE.md, `CURRENT.md`, `HANDOFF.md`, `registers/handoffs/HANDOFF_MB.md`, the skill and `methodology-close`).
UNDECIDED:
  (1) Two gates added beyond §2.1's after-list (B20, B22), each read off a source's `Depends on:` line; neither makes a cycle (no batch but B98 and B99 follows B31); H2 adds both edges or strikes the two GATE lines.
  (2) **A back edge, for H2:** B22.03 (part 33) reads `MassBattleInput.entry_stamina` and `fatigue.lull_recover`, which U3 and `16_PESSIMIST_MB_one_stamina_ledger` place in B31 (step 3; `26_MASS_BATTLE_movement_and_fatigue_as_data` §3). B22's author assumed step 3 lands in B19. B31.06 and B31.07 are written to land only what the tree does not already hold (each opens with a check); recommended: B19's author (A26/A27) carries step 3 and the `fatigue.lull_recover` row, and these two items become the remainder. (Patched: P-10: done — B19.28 lands step 3's field and write and the `lull_recover` row; B31.06 adds the other rows to that block and B31.07 the three writers, each after its presence check.)
  (3) The A-69 record write `16_PESSIMIST_MB_one_stamina_ledger` places in B31 is carried by B22.03 and B22.04 (`last_field`, written under `recuperation: on`): B31.09 is a POINTER that adds only the source's named test.
  (4) The carry factors' carrier and form (B31.03): `03_PC_loadout_and_carry` item 4 says "on the unit row's input"; no source names the field or the map from shortfall to the two factors. Taken: a `carry` field on the order of battle's unit row, and the PC lane's two forms (fatigue `ACT_WEIGHT / D_WT × short`, step `1 / (1 + CARRY_CLOSE_K × short)`) read as multipliers; both `[ASSUMPTION]`.
  (5) MBA-01 renamed the troop column `power` to `skill` (B19a) and MBA-04 deleted the alias (B19); copied text that says `power` for the troop's quality is corrected to `skill` and the correction said (§5.11; MBA §8.3 retires `power` as a troop stat); the economy header's `power_per_step` is written `skill_per_step` for the same reason.
  (6) `26_MASS_BATTLE_movement_and_fatigue_as_data` §4 says "Hash movers: none at the controls", yet `check_drift` paying `reform_ticks` changes a drifting body's fight with no control arm: B31.08 declares MOVER(behaviour) and records EQUAL if the digests read equal.
  (7) The three movement flips (B31.17 to B31.19) are placed after the hash-EQUAL economy and prowess items (§5.9: EQUAL items first where the source's order allows; nothing in B31.10 to B31.16 reads a flipped value).
  (8) MBA-09 (2) (A-113): which rows ship `status: stated`. Taken: every one of the 25 non-★ rows (each involves a class personal combat does not carry: horse, pike, missile or crew) and the `missile.felling_per_hit` table; the ★ rows keep the status B19's MBA-08 left them at. `tools/calibrate_mb_contact.py --missile` (MBA-02 stage 2) is not built: A-113 rules personal combat is not taught the equipment.
  (9) Grouping (E-13): `04_MB_campaign_party_economy`'s six-step order is four items (steps 1–3 one: data and the one read; 4; 5; 6); `26_MASS_BATTLE_movement_and_fatigue_as_data`'s sections are one item each, the flips one each.
SERIAL EDGES: within the batch: B31.01 first (a design item at the batch's open, D-18); `references/troops.yaml` and `tools/export_troops.py` and `troop_types/table.py`: B31.03 → B31.04 → B31.05 → B31.06 → B31.08 → B31.10 → B31.14 → B31.15 → B31.17 → B31.18 → B31.19 → B31.20; `hierarchy/units.py`: B31.02 (`in_hand`, triggers) → B31.03 (the step factor in `_node_advance`) → B31.04 (pace in `_node_advance`) → B31.05 (terrain pace) → B31.08 (`reform`, `check_drift`) → B31.14 (`eff_power` raises); `percell.update_stamina`: B31.03 (carry factor) → B31.06 (fast-move term); `seam/wrappers/mass_battle.py::field_input`: B31.03 → B31.07 (entry writers) → B31.13 (unfed step); `queries/inputs.py::MassBattleInput`: B31.07; `loop/effects_combat.py::_eff_march`: B31.11 (the veterancy draw); `armyrecord.py`: B31.10 → B31.12 (dilution); `orderofbattle.py::_spec_for`: B31.10 → B31.14; B31.02 → B31.08 (the reform pays the switch's rule); B31.03, B31.04 → B31.15 (the readout reads the carry factor B31.03 hands in and the pace B31.04 lands).
  With other batches, by file (U3 §5.1, `→` is landing order): `references/troops.yaml`, `tools/export_troops.py`, `engine/engine_params/troops.json`, `modules/mass_battle/troop_types/table.py` B17 → B19a → B19 → B31 (A-100); `percell.py` B17 → B19 → B31; `massbattle.py` B17 → B19 → B20 → B31; `armyrecord.py` B19 → B20 → B22 → B31; `orderofbattle.py` B17 → B19 → B20 → B22 → B31 → B32; `modules/mass_battle/config.py` B17 → B19 → B31; `loop/effects_combat.py` B04 → B12 → B14 → B16 → B17 → B19 → B20 → B22 → B23 → B31; `engine/season/rosters.yaml` (hot) … → B30 → B31 → B32 …; `engine/season/seam/wrappers/mass_battle.py` B17 → B19 → B20 → B22 → B31 `[ASSUMPTION: this file's batch list is read from the B22 part and the sources, not from U3 §5.1's row]`.
PARALLEL: S19 with B33-inst-economy-hands (FA) and B36-wr-story-instruments (WR). Shared files: `engine/season/rosters.yaml` with B33 (B31 edits only `record_kinds.values.army`; different key), `engine/season/verb_table.yaml` with B33 and B36 if B31.09 adds `march`'s write (different rows): kept by hand at merge (§7.3). All three move pins: B31 merges first in the step (§2.1's order, §7.4).
COST: small builds, three declared flips, one content item; producer `valoria-author` on `sonnet`, `high`; B31.01 (design) and B31.20 (the stated rows and their history checks) on `opus`; the close's terminal critique `opus`; `--trust`/`--spot` supervised on `haiku`.
EST: 13 h [estimate: §2.4's formula over 21 positions, 0.4 h × 21 + 2.5 h + 2 h for the instrument reading (MBA-09's `--trust`, `--spot`), E-15]

| pos | item | source | state | hash | gates on |
|---|---|---|---|---|---|
| B31.01 | the drill step's design | `IS-MB-B2`; `27_MB_B` INCOMPLETE item 2 | DESIGN-FIRST | EQUAL | Batch B19 |
| B31.02 | the weapon in hand, two order triggers, the switch's tick | `04_MB_unit_loadout_and_weapon_in_hand_B` stage 3 | BUILD | EQUAL | Batch B19, Batch B20 |
| B31.03 | what a unit carries costs it stamina and speed | `04_MB_unit_loadout_and_weapon_in_hand_B` stage 4 | BUILD | EQUAL | B31.02; Batch B18 |
| B31.04 | pace on the troop row; the envelop pace on the order | `26_MASS_BATTLE_movement_and_fatigue_as_data` §1 | BUILD | EQUAL | B31.03 |
| B31.05 | ground slows horse: the terrain pace column, at control | `26_MASS_BATTLE_movement_and_fatigue_as_data` §2 | BUILD | EQUAL | B31.04 |
| B31.06 | the fatigue rows; the fast-move term at 0 | `26_MASS_BATTLE_movement_and_fatigue_as_data` §3 (rows) | BUILD | EQUAL | B31.03 |
| B31.07 | a field may be entered tired; who writes the share | `16_PESSIMIST_MB_one_stamina_ledger` step 3; `26_MASS_BATTLE_movement_and_fatigue_as_data` §3 (`entry`) | BUILD | EQUAL | B31.06; Batch B22 |
| B31.08 | changing formation out of contact, for a price | `26_MASS_BATTLE_movement_and_fatigue_as_data` §4 | BUILD | MOVER(behaviour) (declared, UNDECIDED (6)) | B31.02 |
| B31.09 | the stamina a unit ended with is recorded on its row | `16_PESSIMIST_MB_one_stamina_ledger` (the A-69 write) | POINTER | EQUAL | B31.07; Batch B22 |
| B31.10 | veterancy and upkeep as columns; read where a unit is built | `04_MB_campaign_party_economy` steps (1)–(3) | BUILD | EQUAL | B31.06; Batch B22 |
| B31.11 | a unit that stood may learn: the veterancy draw | `04_MB_campaign_party_economy` step (4); `U5b_MB_rulings_in_the_field` §5 | BUILD | EQUAL | B31.10 |
| B31.12 | recruits dilute experience | `04_MB_campaign_party_economy` step (5) | BUILD | EQUAL | B31.10 |
| B31.13 | an unfed side starts one morale lower | `04_MB_campaign_party_economy` step (6) | BUILD | EQUAL | B31.07 |
| B31.14 | the unmustered body is a troop row; no stat lent by the side | `27_MB_B` 27B-3 | BUILD | EQUAL | B31.10 |
| B31.15 | a unit's readout | `27_MB_B` 27B-4 | BUILD | EQUAL | B31.14, B31.03, B31.04 |
| B31.16 | — (pointer: `IS-PC-P2`, `03_PC_loadout_and_carry` items 4 and 6 are B31.02 and B31.03) | `IS-PC-P2` | POINTER | — | B31.03 |
| B31.17 | flip: ground slows horse | `26_MASS_BATTLE_movement_and_fatigue_as_data` §2 (the seeds) | BUILD | MOVER(behaviour) | B31.05, B31.15 |
| B31.18 | flip: moving fast tires | `26_MASS_BATTLE_movement_and_fatigue_as_data` §3 (`fast_move_drain`) | BUILD | MOVER(behaviour) | B31.17 |
| B31.19 | flip: a hard march, a second field and a short ration tire a side | `26_MASS_BATTLE_movement_and_fatigue_as_data` §3 (`entry`) | BUILD | MOVER(behaviour) | B31.18 |
| B31.20 | the other 25 matchup rows, stated, checked against history and banded to the derived rows | MBA-09 | CONTENT | MOVER(behaviour) | B31.19; Batch B19 |
| B31.99 | re-pin and close readings | E-1 | BUILD | MOVER (the re-pin) | B31.01 to B31.20 |

Not in this batch, and where each is: `04_MB_unit_loadout_and_weapon_in_hand_B` stages 1–2 (B17); `16_PESSIMIST_MB_one_stamina_ledger` steps 1–2 (B19); `27_MB_B` 27B-1, 27B-2 (SUPERSEDED by MBA-04, MBA §8.1) and §2's pool arithmetic (SUPERSEDED); `IS-MB-06` (SUPERSEDED by MBA-04, D-15); MBA-02 stage 2 `--missile` (not built: A-113); the payment path and the `arrears` write (FA, SE: "their proposals", none named; a DIAL above); `04_MB_campaign_party_economy` §3 (named and not built: march speed against carried weight, companions, prisoners and ransom, an upgrade tree); `U5b_MB_rulings_in_the_field` §1 (B05), §2 (B23), §3 (B30), §4 and §6 (B19).

### B31.01 — the drill step's design · `IS-MB-B2` · DESIGN-FIRST · HASH EQUAL
- SOURCE: `master/instructions/IS_B1_PC_MB_DICE_part2.md` "Blocked items" row `IS-MB-B2` ("MB lane, design-first, B31"; NARROWED by A-100: "a drill step is a step on the unit's `skill`; `power` is retired as a troop stat"); `proposals/27_MB_B_unit_prowess_on_the_row.md` "INCOMPLETE" item 2; `unified/U4_DOCUMENT_STATUS.md` §3.4 (27_MB_B: DESIGN, SITE); `proposals/14_VERBS_MILITARY_B_train.md` §1 item 3 (hands the read to MB); D-18; closes `IS-MB-B2`'s design half.
- ADVANCES: none of the nine; A-59 (2) (a drilled cohort's quality reaches its unit).
- INSTRUCTION: write ONE design file, no code, `proposals/2026-11-12-mb-drill-step.md` `[ASSUMPTION: the file name — basis: B10.51's precedent; CLAUDE.md §3: new design work goes to `proposals/`]`, `## Status: PROPOSED`, stating each with a falsifier and a control: (1) the size of the step (a cohort person's skill score in `arms`, `14_VERBS_MILITARY_B` §1 item 3, as a step on its unit's troop `skill`); (2) its cap; (3) the host-side read in `seam/wrappers/mass_battle.py::_order_of_battle` (the source's `_order_of_battle`), and that the module receives the step on the unit row and reads no person; (4) how the size is chosen: "a calibration against `26_MASS_BATTLE_calibration_targets`" (`IS-MB-B2`), with the reading rule and its control ("no step: a cohort's skill does not reach unit prowess; that is the control arm"). It also states that the step does not multiply prowess (`27_MB_B` §2's surviving prohibitions).
- WHERE: NEW `proposals/2026-11-12-mb-drill-step.md`. No file under `modules/` or `engine/`.
- TESTS: none (a design).
- FALSIFIER and CONTROL (stated in the file): two units of one troop row, one drawn from a drilled cohort, read differently through the contact draw (`contact_casualties`) only by the step and not at all with the step at 0. Control: the step at 0 reproduces the base digests.
- GATE: `test -f proposals/2026-11-12-mb-drill-step.md` → exit 0; `grep -c '^## Status: PROPOSED' proposals/2026-11-12-mb-drill-step.md` → 1; the file states (1) to (4) each with a falsifier and a control (read by the batch's `ners` critic); `git diff --stat <batch-start-sha> -- modules engine` shows no change made by this commit.
- HASH MOVERS: none. Its build, unscheduled, is a declared mover of every field with a drilled cohort.
- DEPENDS ON: V12 Batch B19 (MBA-01's `skill` column; MBA-04's `ContactVector`); V12 Batch B22 (`14_VERBS_MILITARY_B` `train`, the cohort's `arms` rank).
- GLOSSARY: none in this commit (the design names a new term with its ordinary-English reading; its build adds the row). The word is "drill", not "training", where it means a unit's practice (the glossary's *train* is a person's verb).
- COST and TIER: design; `opus`, `high`; critic `ners` on `opus`.
- LANDS IT: B31's `valoria-author` producer, `isolation: worktree`; `Item: B31.01`, `[skip ci]`; at the batch's open. Its approval is the batch PR's merge (ED-1094); its build is listed for Jordan in the PR body as unscheduled.

### B31.02 — the weapon in hand, two order triggers, the switch's tick · `04_MB_unit_loadout_and_weapon_in_hand_B` stage 3 · BUILD · HASH EQUAL
- SOURCE: `proposals/04_MB_unit_loadout_and_weapon_in_hand_B.md` §4 ("The weapon in hand"), its `Folded:` (audit 26) item (1) and (2), "Stages and gates" row 3, "Tests (W3-1)" stage 3, "Falsifier"; rulings A-2, A-59, A-100 (MBA §3.1: "A missile troop that is reached fights with its sidearm … or switches by a standing order (`volleys_spent`)"); ED-MB-0001 (read as "per the weapon in hand", the brief's later statement); closes R-35 of `audits/04_MB_audit_addendum_B.md`, `IS-PC-P2` (with B31.03).
- ADVANCES: none of the nine; a weapon decision reaches a field (A-59 (2)).
- INSTRUCTION (copied, with the corrections said):
  1. "`Subunit.in_hand: str = 'primary'`, in `hierarchy/units.py::_ORDER_SAFE_FIELDS`. `unit_type`, reach and support depth are read from the arm in hand." Correction (A-100): the contact draw reads the `duel_key` of the arm in hand (MBA-01), or the missile arm's `sidearm` when a missile arm is in hand hand to hand; `RANGED_MELEE_SIGMA` was deleted by MBA-04 step 7, so "the missile handicap" is that sidearm.
  2. "A change is an `Order` behaviour, so a standing order carries it (`04_MB_manager_battle_one_resolver.md`): for example `(enemy_range:2, {in_hand: secondary})`." `switch` is an order "and take[s] effect through the obedience draw (`27_MB_A`)".
  3. "**The switch costs a tick:** on the tick the order fires, the unit's pair pools are 0 and its brace latch resets. A body with a missile weapon in hand does not volley once it has switched". Correction (A-100, MBA-04 step 4): "pair pools are 0" is written as "the body contributes `m = 0` fighting men to its contact vector on that tick".
  4. "Two trigger kinds are added to `_ORDER_TRIGGER_KINDS`, not one: `flanked` (contact on a flank or rear arc, which the engine computes per pair) and **`volleys_spent`** (ammunition at zero)."
  5. "**No default order is invented by the builder.** … a body with no such order keeps its primary in hand and pays for it." "The switch is one-way within an engagement unless a later order switches back; the tick is paid each time."
  6. Audit 26's fold (1): "**A body itself in melee contact does not volley**, whichever weapon is in hand; a body not in contact may shoot into a melee". Open `orchestration.py::volley_phase` and `core/volley.py` (B19's MBA-05: "the no-volley-in-contact rule unchanged") and record in the commit body whether the rule holds at this tree; add it in `volley_phase` only if a reached body still volleys.
- WHERE: `modules/mass_battle/hierarchy/units.py` (`Unit.in_hand`, `_ORDER_SAFE_FIELDS`, `_ORDER_TRIGGER_KINDS`, the trigger evaluation, the switch tick); `modules/mass_battle/orchestration.py` (`volley_phase`; `resolve_engagements`' vector builder reads the arm in hand); `modules/mass_battle/core/volley.py` (only if step 6 finds the rule absent); `tests/valoria/test_mass_battle_ammo.py`.
- TESTS: `tests/valoria/test_mass_battle_ammo.py::test_switch_stops_volleys_and_costs_a_tick` and `::test_reached_archers_with_no_order_stop_volleying` (named, W3-1), written first and read red.
- FALSIFIER and CONTROL: "a reached missile body that still volleys after switching"; "any result that moves with every `secondary` null". Control: `python tools/ci_golden_modes_check.py` digests equal with every `secondary` null.
- GATE: the row's gate, copied: "digests equal with every `secondary` null; archers with `secondary: arming` and the order `(enemy_range:2, {in_hand: secondary})`: volley events stop at the order's tick, one tick with no melee from that body, then melee without the missile handicap"; and "a reached archer body with no order: zero volley events after its first tick in contact". `python -m pytest tests/valoria/test_mass_battle_ammo.py -q` → pass; `python tools/ci_golden_modes_check.py` → digests equal to B30's close.
- HASH MOVERS: none ("none at stages 1–3 with every `secondary` null").
- DEPENDS ON: EXISTS-IN-TREE `hierarchy/units.py::_ORDER_SAFE_FIELDS`, `::_ORDER_TRIGGER_KINDS`, `orchestration.py::volley_phase`; V12 Batch B17 (stages 1–2: `references/troops.yaml`'s `primary`, `secondary`); V12 Batch B19a, B19 (MBA-01 `duel_key`, `sidearm`; MBA-04, MBA-05; `27_MB_A`'s obedience draw); V12 Batch B20 (`04_MB_manager_battle_one_resolver.md` §2: standing orders on the unit row).
- GLOSSARY: *weapon in hand* (row exists for the duel's `form`, A-101's round): its owner column adds `Unit.in_hand` (mass battle; one state name with the duel's, `…_B.md` NERS S).
- NAMES: `Subunit` → `Unit` (B16M); `subunits` → `units` (B16M); the army is `Army` (B16M); "body" (a unit) → unit (S-8; K9 added: the item's copied text says "body" for a unit).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.02`, `[skip ci]`.

### B31.03 — what a unit carries costs it stamina and speed · `04_MB_unit_loadout_and_weapon_in_hand_B` stage 4 · BUILD · HASH EQUAL
- SOURCE: the same file, §3 (`strength` and its seed rule), §5, its first `Reconciled:` items (1), (2) (the factors act on the column ledger only), "Stages and gates" rows 4 and "4, after arrangement", "Tests (W3-1)" stage 4; `proposals/03_PC_loadout_and_carry.md` items 2–4 (`carry_demand_of`, "the ONE body"; the host hands the shortfall "as `(fatigue_factor, step_factor)` per in-hand state … on the unit row's input"); D-U1-11d; closes R-36, `IS-PC-P2`.
- ADVANCES: none of the nine; Jordan's stated trade (versatility against tiring and slowness) has a carrier.
- INSTRUCTION:
  1. Copied (§5): "the host evaluates the carry demand for each unit in both states and hands the module `(fatigue_factor, step_factor)` per state; the module multiplies the per-clash drain, divides the rest recovery, and multiplies the step." "The caller is the host, `seam/wrappers/mass_battle.py::field_input` (and the army constructors' input builders); `modules/mass_battle/` neither imports nor copies it." Masses: "An arm's mass lives in personal combat's typed export when its key is in that roster, and here (`mass_kg`) only when it is not."
  2. The form (UNDECIDED (4), `[ASSUMPTION: carrier and map — basis: `03_PC_loadout_and_carry` items 3 and 4]`): per state (`primary` in hand; `secondary` in hand), `short = max(0, carry_demand_of(masses_not_in_hand, armour) − strength)`; `fatigue_factor = 1 + ACT_WEIGHT / D_WT × short`; `step_factor = 1 / (1 + CARRY_CLOSE_K × short)` (the PC lane's constants, read from the export's `cfg`). The two pairs ride on the unit's row of the order of battle the host builds (`UnitRow.carry: ((f_primary, s_primary), (f_secondary, s_secondary))`, default `((1.0, 1.0), (1.0, 1.0))`).
  3. Module reads: `percell.update_stamina` multiplies the per-clash `drain` by the in-hand state's `fatigue_factor` and divides the rest by it; `Unit._node_advance` multiplies the step by `step_factor` (the column ledger only: "the subunit drain in `battle_loop` and `STAMINA_RECOVERY_PER_RESERVE_RANK` … have no successor").
  4. `strength` on every troop row by the seed rule, if B17 did not ship it: "the smallest whole number at or above the demand of the row's own armour, so that a type carrying only its primary pays nothing, as today."
- WHERE: `engine/season/seam/wrappers/mass_battle.py` (`field_input`, `_order_of_battle`: the factors); `modules/mass_battle/orderofbattle.py` (`UnitRow.carry`); `modules/mass_battle/percell.py` (`update_stamina`); `modules/mass_battle/hierarchy/units.py` (`_node_advance`); `references/troops.yaml` (`strength`, if absent); `tools/export_troops.py`, `engine/engine_params/troops.json` (re-derived); `tests/valoria/test_mass_battle_order_of_battle.py`.
- TESTS: `tests/valoria/test_mass_battle_order_of_battle.py::test_the_factor_handed_in_equals_carry_demand_of` (named): "the factor handed in equals the leaf evaluated on the same masses, asserted by calling it". Written first, read red.
- FALSIFIER and CONTROL: "a carried second weapon that changes nothing at any `strength`"; "a second roster or a second carry rule under `modules/mass_battle/`". Control: every `secondary` null → every factor 1.0 → digests equal.
- GATE: row 4, copied: "with a `secondary` and `strength` at the seed: stamina at tick 7 and first-contact tick differ from the same body without it; at a raised `strength` they do not; over 72 ticks the carrying side recovers more slowly out of contact"; row "4, after arrangement": "a pike body four ranks deep with `secondary: arming` and a `flanked` switch order, against the same body with no secondary, flanked by cavalry: the switching body's share lost differs beyond the same-run control at n 200; against a frontal charge it does not win more than the control" (a module reading on `resolve_field`, `assert checked >= 200`, quoted in the commit body). `python -m pytest tests/valoria/test_mass_battle_order_of_battle.py -q` → pass; `python tools/ci_golden_modes_check.py` → digests equal; `python tools/export_troops.py --check` → exit 0.
- HASH MOVERS: none at landing ("stage 4 only rows naming a second weapon"; none does).
- DEPENDS ON: V12 Batch B18 (`03_PC_loadout_and_carry`: `engine/substrate/combat_kit.py::carry_demand_of`, the export's `mass`); V12 Batch B19 (`04_MB_cell_hierarchy_as_data`, the arrangement; `16_PESSIMIST_MB_one_stamina_ledger` steps 1–2, the one column ledger); V12 B31.02; EXISTS-IN-TREE `percell.py::update_stamina`, `units.py::_node_advance`, `combat_kit.py`.
- GLOSSARY: *carry demand* (row exists, PC's): owner column `combat_kit.carry_demand_of` for persons and units alike.
- NAMES: `Subformation` → `UnitRow` (B16L); `Subunit._node_advance` → `Unit._node_advance` (B16M); "body" (a unit) → unit (S-8; K9 added: the item's copied text says "body" for a unit).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.03`, `[skip ci]`.

### B31.04 — pace on the troop row; the envelop pace on the order · `26_MASS_BATTLE_movement_and_fatigue_as_data` §1 · BUILD · HASH EQUAL
- SOURCE: `proposals/26_MASS_BATTLE_movement_and_fatigue_as_data.md` §1, "Exact edits", "Gate" 1, "Tests (W3-1)"; rulings A-59 (pace is a term a unit brings from its own row); `04_MB_unit_loadout_and_weapon_in_hand_B` `Folded:` (5); closes M-1 of `audits/26_MASS_BATTLE_HISTORICAL_ADJUDICATION.md`.
- ADVANCES: none of the nine.
- INSTRUCTION (copied): "`references/troops.yaml: troops.<kind>.pace`, cells a tick at base. Seeds reproduce today": every foot kind 1 ("Control and seed are the same."); `cavalry`, `light_cavalry`, `mounted_archers` 3 ("Today's constant, in range"); `knights_templar` 1 ("today's behaviour (it is not in `MOUNTED_TYPES`)"). "`MB_CAVALRY_SPEED_MULT` is deleted; the four sites read the row. The envelop multiplier becomes `orders.envelop_pace: 2`, one datum beside the order vocabulary, because it is a property of the order, not of a troop." `config.py`: delete `MB_CAVALRY_SPEED_MULT`, `MB_ENVELOP_SPEED_MULT`. Every site is found by `git grep -n "MB_CAVALRY_SPEED_MULT\|MB_ENVELOP_SPEED_MULT" modules/` at the item's open (this read finds five uses of the cavalry constant in `hierarchy/units.py`, the source names four; each reads the row). `troop_types/table.py` exposes `pace_for(kind)`; `tools/export_troops.py` carries the column; `python tools/export_sim_params.py --build` drops the two constants.
- WHERE: `references/troops.yaml` (`troops.*.pace`, `orders.envelop_pace`); `tools/export_troops.py`; `engine/engine_params/troops.json`; `modules/mass_battle/troop_types/table.py` (`pace_for`, the `orders` block); `modules/mass_battle/hierarchy/units.py` (every site); `modules/mass_battle/config.py`; `engine/engine_params/sim_params.json` (re-derived).
- TESTS: `tests/valoria/test_export_troops.py` (the round trip) and `tests/valoria/test_field_golden_pins.py` (gate 1); none new.
- FALSIFIER and CONTROL: "A pace that still depends on the spelling of a troop type's name". Control: digests equal.
- GATE: "Every new value at its control: `tools/export_troops.py --check` passes and `tools/ci_golden_modes_check.py` digests are equal"; `git grep -n "MB_CAVALRY_SPEED_MULT\|MB_ENVELOP_SPEED_MULT" modules/ engine/` → nothing; `python tools/export_sim_params.py --check` → exit 0.
- HASH MOVERS: none ("Sections 1 and the transcribed fatigue rows: edit, hash-equal").
- DEPENDS ON: V12 Batch B17 (the troop file, its loader and exporter); EXISTS-IN-TREE `config.py::MB_CAVALRY_SPEED_MULT`, `::MB_ENVELOP_SPEED_MULT`, `units.py::_node_advance`; V12 B31.03.
- GLOSSARY: *pace* (new row): "how many cells a unit moves in a tick at its ordinary speed, as a marching pace is"; owner `troops.yaml: troops.<kind>.pace`.
- NAMES: "body" (a unit) → unit (S-8; K9 added: the item's copied text says "body" for a unit).
- COST and TIER: edit (mechanical); `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.04`, `[skip ci]`.

### B31.05 — ground slows horse: the terrain pace column, at control · `26_MASS_BATTLE_movement_and_fatigue_as_data` §2 · BUILD · HASH EQUAL
- SOURCE: the same file, §2, "Exact edits" (`massbattle.py::resolve_field`), "Gate" 2; closes M-2.
- ADVANCES: none of the nine.
- INSTRUCTION (copied): "A `pace` column on the six terrain rows (`modules/mass_battle/terrain.py` today; the troop file's `terrain` section when that file lands), by class" — shipped at the control, every cell 1.0 ("Control arm: every cell 1.0"); the seeds (`forest_broken` mounted 0.6, `uphill` mounted 0.25; `narrow_pass`, `river_crossing`, `walls` "**not established**; no multiplier invented") are B31.17. "The multiplier applies to the body's step before the posture modifier, at the one place the step is formed (`units.py::_node_advance`; the continuous-speed arm accumulates the fraction as it already does for discipline)." "`massbattle.py::resolve_field` passes the field's terrain row to the units for pace, as it passes it for dice." The column lives in the troop file's `terrain` section `[ASSUMPTION: the troop file holds the section at this tree — basis: "when that file lands" (B17); if `terrain.py` still holds the rows, the column goes there]`.
- WHERE: `references/troops.yaml` (`terrain.<row>.pace`, or `modules/mass_battle/terrain.py`); `tools/export_troops.py`; `engine/engine_params/troops.json`; `modules/mass_battle/troop_types/table.py`; `modules/mass_battle/hierarchy/units.py` (`_node_advance`, the continuous arm); `modules/mass_battle/massbattle.py` (`resolve_field`); `tests/valoria/test_mass_battle_terrain.py`.
- TESTS: `tests/valoria/test_mass_battle_terrain.py::test_horse_pace_by_ground` (named; gate 2), written now with the seeds set in the test, read red before the edit.
- FALSIFIER and CONTROL: "horse at three times foot on `uphill`" (with the seeds set). Control: every cell 1.0 → digests equal.
- GATE: `python -m pytest tests/valoria/test_mass_battle_terrain.py -q` → pass (gate 2, seeds set in the test: "on `open_flat` the horse arrives in a third of the ticks; on `forest_broken` in about half to two-thirds; on `uphill` after the foot"); `python tools/ci_golden_modes_check.py` → digests equal; `python tools/export_troops.py --check` → exit 0.
- HASH MOVERS: none at the control.
- DEPENDS ON: V12 B31.04; EXISTS-IN-TREE `modules/mass_battle/terrain.py` (`OPEN_FLAT`, `FOREST_BROKEN`, the six rows), `massbattle.py::resolve_field`.
- GLOSSARY: none (*pace* from B31.04).
- NAMES: "body" (a unit) → unit (S-8; K9 added: the item's copied text says "body" for a unit).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.05`, `[skip ci]`.

### B31.06 — the fatigue rows; the fast-move term at 0 · `26_MASS_BATTLE_movement_and_fatigue_as_data` §3 (rows) · BUILD · HASH EQUAL
- SOURCE: the same file, §3, "Exact edits" (`config.py`, `percell.py`), "Gate" 1, 3; `16_PESSIMIST_MB_one_stamina_ledger` `Folded:` (audit 26) amendment (3); D-U1-11c ("the four constants deleted from `config.py` in the same commit that adds their rows"); A-69 (the head's `Folded:` (1)).
- ADVANCES: none of the nine.
- INSTRUCTION:
  1. Open `references/troops.yaml` and record whether a `fatigue:` block exists (B22.03 wrote `fatigue: {carry: off, carry_laps: 0}`) and whether it holds `lull_recover` (B22.03 reads it; UNDECIDED (2)). Add only the missing keys; never a second block.
  2. Copied (the rows):
     ```yaml
     fatigue:
       clash_drain: 12          # MB_STAMINA_DRAIN, per clash a column fights           (today)
       rest: 5                  # MB_STAMINA_REST, per tick a column is out of contact   (today)
       fast_move_drain: 0       # per tick a column moves above its row's pace. CONTROL 0. Seed for the flip: 2
       lull_recover: 30         # BETWEEN_TURN_STAMINA_RECOVERY (orchestration.py), per lull (today)
       entry:                   # share of full stamina a side starts with. CONTROL: all 1.0
         march_partial: 1.0
         second_field: 1.0
         unfed: 1.0
     ```
     The `entry` values ship at their control 1.0 here (the source's block shows the seeds 0.7, which are B31.19's flip); "the lowest product is floored at 0.3 so no side arrives unable to stand (a seed)" is the loader's floor. Keys B22.03 wrote (`carry`, `carry_laps`) stay.
  3. `config.py`: delete `MB_STAMINA_DRAIN`, `MB_STAMINA_REST` ("their values now rows"); `orchestration.py::BETWEEN_TURN_STAMINA_RECOVERY` reads `fatigue.lull_recover`. `percell.update_stamina` reads the rows, and gains the fast-move term: a column that moved above its row's `pace` this tick loses `fast_move_drain` (0: nothing).
  4. `troop_types/table.py` exposes the `fatigue` block; `tools/export_troops.py` carries it; `python tools/export_sim_params.py --build`.
- WHERE: `references/troops.yaml` (`fatigue`); `tools/export_troops.py`; `engine/engine_params/troops.json`; `modules/mass_battle/troop_types/table.py`; `modules/mass_battle/config.py`; `modules/mass_battle/orchestration.py` (`BETWEEN_TURN_STAMINA_RECOVERY`); `modules/mass_battle/percell.py` (`update_stamina`); `engine/engine_params/sim_params.json` (re-derived); `tests/valoria/test_mass_battle_maneuvers.py`.
- TESTS: `tests/valoria/test_mass_battle_maneuvers.py::test_fast_move_drain_tires_the_wing` (named; gate 3), written now with `fast_move_drain: 2` set in the test, read red before step 3.
- FALSIFIER and CONTROL: "stamina unchanged by a bout of double-pace movement at a non-zero drain". Control: every value at control → digests equal.
- GATE: `python -m pytest tests/valoria/test_mass_battle_maneuvers.py -q` → pass ("an enveloping wing's columns read lower stamina at first contact than the same wing at the control"); `python tools/ci_golden_modes_check.py` → digests equal; `python tools/export_troops.py --check`, `python tools/export_sim_params.py --check` → exit 0; `git grep -n "MB_STAMINA_DRAIN\|MB_STAMINA_REST" modules/ engine/` → nothing.
- HASH MOVERS: none at the control.
- DEPENDS ON: V12 B31.03, B31.04; V12 Batch B19 (the one column ledger, `16_PESSIMIST_MB_one_stamina_ledger` steps 1–2); V12 Batch B22 (B22.03's `fatigue` block); EXISTS-IN-TREE `config.py::MB_STAMINA_DRAIN`, `::MB_STAMINA_REST`, `orchestration.py::BETWEEN_TURN_STAMINA_RECOVERY`, `percell.py::update_stamina`.
- GLOSSARY: *stamina* (row exists; U1 §3: a share in [0, 1] at every typed boundary): unchanged.
- COST and TIER: edit and small build; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.06`, `[skip ci]`.

### B31.07 — a field may be entered tired; who writes the share · `16_PESSIMIST_MB_one_stamina_ledger` step 3; `26_MASS_BATTLE_movement_and_fatigue_as_data` §3 (`entry`) · BUILD · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_MB_one_stamina_ledger.md` "Step 3", "Gate", "Falsifier"; `proposals/26_MASS_BATTLE_movement_and_fatigue_as_data.md` §3 (`entry`, its three writers) and "Exact edits" (`field_input`); rulings A-69; U1 §3; closes F-PES-MB-06's step 3, M-7.
- ADVANCES: none of the nine; A-69 (fatigue reaches the field).
- INSTRUCTION:
  1. At the item's open: `grep -n entry_stamina engine/season/queries/inputs.py modules/mass_battle/massbattle.py`. If present (UNDECIDED (2)), step 2 is a POINTER to the landing commit (`git log -S entry_stamina --oneline`), named in the commit body; else build it.
  2. Copied (step 3): "`engine/season/queries/inputs.py::MassBattleInput` — new field `entry_stamina: tuple[float, float] = (1.0, 1.0)`, each side's share of full stamina at the start, in `[0, 1]`"; "`modules/mass_battle/massbattle.py::resolve_field` — after each `Unit` is built: `for b in unit.col_grid: b.stamina = STAMINA_MAX * share`; at `1.0` nothing is written"; "The `PER_CELL` off arm has no column grid; there `entry_stamina` other than `(1.0, 1.0)` is refused loudly rather than ignored." "`entry_stamina` may be given per part" (the audit-26 fold (2)) where B22.03 already passes a per-part value.
  3. Copied (`26_…` §3, `field_input`): "forms `entry_stamina` from the three facts (a share in [0, 1], U1 §3)": "the march's band (an army that arrives spent, `14_VERBS_MILITARY_A_movement.md`'s `Partial`), a second field in one season round, and a short ration" — "Each value multiplies; the lowest product is floored at 0.3"; "The three writers are the only writers; each reads a fact its owner already has (the march's band; the count of fields this round; the ration debit)". Under B22.03's A-69 record, the second-field writer is replaced by the recorded `stamina_left` plus one lull where a record exists (`27_MB_E` §4). At this item every `entry` value is 1.0, so every product is 1.0.
- WHERE: `engine/season/queries/inputs.py` (`MassBattleInput.entry_stamina`, if absent); `modules/mass_battle/massbattle.py` (`resolve_field`, if absent); `engine/season/seam/wrappers/mass_battle.py` (`field_input`); NEW `tests/valoria/test_mass_battle_entry_stamina.py` (if absent); `engine/season/tests/test_mass_battle_module.py`.
- TESTS: in `tests/valoria/test_mass_battle_entry_stamina.py` (named by the source), written first and read red: `test_entry_stamina_half_loses_more` ("a mirror field, n 100 seeds, friction pinned off for the test; `entry_stamina (0.5, 1.0)` loses more often than `(1.0, 1.0)` by more than the sampling band", `assert checked >= 100`), `test_default_equals_omitted`, `test_returned_stamina_below_100_after_a_fought_field`; `engine/season/tests/test_mass_battle_module.py::test_entry_stamina_lowers_the_tired_side` (`26_…` gate 4, written with `entry.march_partial: 0.7` set in the test). A test already landed is kept, not duplicated.
- FALSIFIER and CONTROL: "A field whose result is unchanged by `entry_stamina` 0.1 against 1.0 on one side". Control: "`(1.0, 1.0)` equals the field with the argument omitted, field for field"; the realm content hash at seed 0, one season, equal to B31.06's reading (`MassBattleInput` is not a `World` carrier: no encoding move).
- GATE: `python -m pytest tests/valoria/test_mass_battle_entry_stamina.py engine/season/tests/test_mass_battle_module.py -q` → pass; `python tools/ci_golden_modes_check.py` → digests equal.
- HASH MOVERS: none ("step 3 none at its default").
- DEPENDS ON: V12 B31.06 (the `entry` rows); V12 Batch B22 (B22.03: `FieldOutcome.stamina_left`, `last_field`, `field_input`'s per-part reading; `14_VERBS_MILITARY_A`'s march band, B22.08; B22.16's ration debit); EXISTS-IN-TREE `engine/season/queries/inputs.py::MassBattleInput`, `seam/wrappers/mass_battle.py::field_input`, `massbattle.py::resolve_field`, `config.py::STAMINA_MAX`.
- GLOSSARY: *entry stamina* (new row, if absent): "the share of full stamina a side starts a field with".
- NAMES: the copied "a second field in one season round" and "the count of fields this round" mean the lap (B04, `PCR-4`; A-101): the code counts fields per lap.
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.07`, `[skip ci]`.

### B31.08 — changing formation out of contact, for a price · `26_MASS_BATTLE_movement_and_fatigue_as_data` §4 · BUILD · HASH MOVER(behaviour) (declared)
- SOURCE: the same file, §4, "Exact edits" (`hierarchy/units.py`), "Gate" 5, "Tests (W3-1)"; A-59 (`reform` is an order through the obedience draw, `27_MB_A`); closes M-5 and F-MB-18 (`audits/04_MB_audit.md`).
- ADVANCES: none of the nine.
- INSTRUCTION (copied): "`shape`, `ranks` and `files` join `_ORDER_SAFE_FIELDS` as one behaviour key, `reform: {shape, ranks, files}`, applied through `rekey_cells` (after F-MB-18's repair: the three morale maps re-seeded from the body's aggregate)" — the repair is this item's (the source's exact edits: "`rekey_cells` repair"). "**Eligibility:** the body has no cell in contact on the tick the order fires. In contact the order stays pending." "**Cost:** `reform_ticks` during which the body's pair pools are 0, it does not volley, and its brace latch is down: the weapon switch's rule (`…_B.md` §4), for longer. Datum `orders.reform_ticks` by Discipline: 1 at Discipline 4 or more, 2 below." "in the lull between bouts … a reform costs no ticks." "`check_drift` stays, and pays the same cost: a body that loses its shape for want of Discipline is disordered for `reform_ticks`, not instantly re-dressed." "a `_reforming_until` tick on the subunit, read where the switch tick is". Correction (A-100): "pair pools are 0" is "contributes `m = 0` fighting men", as B31.02.
- WHERE: `modules/mass_battle/hierarchy/units.py` (`_ORDER_SAFE_FIELDS`, `rekey_cells`, `check_drift`, `Unit._reforming_until`); `references/troops.yaml` (`orders.reform_ticks`); `tools/export_troops.py`; `engine/engine_params/troops.json`; `modules/mass_battle/troop_types/table.py`; `tests/valoria/test_mass_battle_role_instructions.py`.
- TESTS: `tests/valoria/test_mass_battle_role_instructions.py::test_reform_out_of_contact_only_and_costs_ticks` and `::test_stamina_left_is_a_share` (named), written first, read red.
- FALSIFIER and CONTROL: "a re-forming body that fights". Control: a body never ordered to reform and never drifting reads as before.
- GATE: gate 5, copied: "A body ordered to `reform` from `Line` to `Column` while out of contact: its shape changes, its cells' morale ids match its troop ids, and for `reform_ticks` it deals no damage; the same order given in contact does not fire until contact ends; charged during the reform, it loses more than the same body charged after it." `python -m pytest tests/valoria/test_mass_battle_role_instructions.py -q` → pass; `python tools/ci_golden_modes_check.py` → read and quoted: equal, or moved only where `check_drift` fires (UNDECIDED (6)).
- HASH MOVERS: fields in which a body drifts (`check_drift` now pays `reform_ticks`), if any: declared; B31's one re-pin.
- DEPENDS ON: V12 B31.02 (the switch tick); V12 Batch B19 (`27_MB_A` obedience; `04_MB_cell_hierarchy_as_data`: `ranks`, `files`); EXISTS-IN-TREE `units.py::rekey_cells`, `::check_drift`, `::_ORDER_SAFE_FIELDS`.
- GLOSSARY: *reform* (new row): "to change a unit's unit formation while out of contact, which costs it time"; the word *unit formation* names the arrangement (MB lexicon).
- NAMES: "the subunit" → the unit (`Unit`, B16M); "body" (a unit) → unit (S-8; K9 added: the item's copied text says "body" for a unit).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.08`, `[skip ci]`.

### B31.09 — the stamina a unit ended with is recorded on its row · `16_PESSIMIST_MB_one_stamina_ledger` (the A-69 write) · POINTER · HASH EQUAL
- SOURCE: `proposals/16_PESSIMIST_MB_one_stamina_ledger.md` "The one writer of the recorded stamina (A-69, A-2)", "Gate" (`test_marched_field_records_stamina_left_on_the_army_record`, "(B31)"); UNDECIDED (3).
- What the pointed items do: B22.03 and B22.04 (part 33) write each unit row's `last_field: (lap, stamina_left)` at RESOLVE in `_eff_march` through the army verbs' write path (`armyrecord.apply`), under `recuperation: on`, through the existing `(Record, subject_matter)` matrix row. This item adds only the source's named test and the row note it owes.
- INSTRUCTION: (1) `tests/valoria/test_mass_battle_entry_stamina.py::test_marched_field_records_stamina_left_on_the_army_record`: a marched field, `recuperation: on` set in the test, leaves each fighting unit row's recorded stamina equal to the part's `FieldOutcome.stamina_left`; read green (the write exists), red with B22.04's write reverted in a scratch copy. (2) If `engine/season/verb_table.yaml`'s `march` row does not declare `Record.subject_matter` in its `writes` at the bands that fought a field, add it, and name `march` in the `(Record, subject_matter)` row's `by:` note in `engine/season/write_matrix.yaml` (the source's `[ASSUMPTION: … verify the band set at landing]`).
- WHERE: `tests/valoria/test_mass_battle_entry_stamina.py`; `engine/season/verb_table.yaml` (`march`, if needed); `engine/season/write_matrix.yaml` (the `by:` note, if needed).
- GATE: `python -m pytest tests/valoria/test_mass_battle_entry_stamina.py -q` → pass; `python -m engine.season.harness.register --check` → exit 0.
- HASH MOVERS: none (a test and a declaration; the write was B22's).
- DEPENDS ON: V12 B22.03, B22.04; V12 B31.07.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.09`, `[skip ci]`.

### B31.10 — veterancy and upkeep as columns; read where a unit is built · `04_MB_campaign_party_economy` steps (1)–(3) · BUILD · HASH EQUAL
- SOURCE: `proposals/04_MB_campaign_party_economy.md` §1 (bullets one to three), §2 (`upkeep`, `arrears`), "Exact edits", "Implementation (test 9, W3-1)" order (1)–(3), "Gate" 1, 5; rulings A-2 (columns of the unit row), A-59 (`experience` is quality; `arrears` lowers steadiness), A-100 (quality is the troop `skill`, MBA-01, MBA §8.1: "experience as a skill step"); closes R-42 of `audits/04_MB_audit_addendum_B.md`.
- ADVANCES: none of the nine; A-59 (2), the Bannerlord referent's "upkept".
- INSTRUCTION (copied, with the corrections said):
  1. "Troop file header: `veterancy: {arm: off | steps, power_per_step: 1, max_steps: 2}`; `off` is the control. The values are the archived design's, transcribed as seeds." Written `veterancy: {arm: off, skill_per_step: 1, max_steps: 2, ob: null}` (UNDECIDED (5): `power` is retired as a troop stat; `ob` is the draw's obstacle B31.11 reads, "`veterancy.ob` in the troop file's header", which no source gives a value: shipped `null`, and the loader refuses `arm: steps` while `ob` is `null`). "Troop row: `upkeep` (whole units of the treasury's coin per hundred troops per season; seed 0 for every row, so nothing is charged at landing)."
  2. "Army Record, unit row: `experience: 0 | 1 | 2` (default 0)" and "an `arrears: int` on the unit row (seasons unpaid, written by the campaign side)": both optional and absent by default, read as 0 when absent (B22.02's precedent for `absent` and `last_field`, ladder step 4: so no Record's content moves at landing). `modules/mass_battle/armyrecord.py`: the unit row accepts both; `to_order_of_battle` carries both; `engine/season/rosters.yaml: record_kinds.values.army`: the unit row's key set gains them.
  3. "**Read:** `armyrecord.to_order_of_battle` hands each unit's `experience` on; `orderofbattle._spec_for` adds `power_per_step * experience` to the troop row's `power` for that unit. One addition, at the one place a unit's stats are assembled." Corrected: `skill_per_step * experience` added to the troop row's `skill`. "read at `_spec_for` as `discipline -= min(arrears, discipline - 1)` for a row whose `upkeep` is above 0."
- WHERE: `references/troops.yaml` (`veterancy`; `troops.*.upkeep`); `tools/export_troops.py`; `engine/engine_params/troops.json`; `modules/mass_battle/troop_types/table.py` (the header, the `steps`-without-`ob` refusal); `modules/mass_battle/armyrecord.py` (the unit row, `to_order_of_battle`); `modules/mass_battle/orderofbattle.py` (`UnitRow.experience`, `.arrears`; `_spec_for`); `engine/season/rosters.yaml` (`record_kinds.values.army`); `tests/valoria/test_mass_battle_order_of_battle.py`.
- TESTS: `tests/valoria/test_mass_battle_order_of_battle.py::test_arrears_lower_discipline_only_with_upkeep` (named; gate 5: "A unit row with `upkeep` above 0 and `arrears` 2 is built at `discipline - 2` (floor 1); the same troop row at `upkeep` 0 is not"), and `::test_experience_adds_one_skill_step_per_step` `[ASSUMPTION: test name; E-3]`, written first, read red.
- FALSIFIER and CONTROL: "arrears that lower a levy; any result that moves with the arm `off` and every `upkeep` 0". Control: gate 1, "`veterancy.arm: off`, every `upkeep` 0: `python3 tools/ci_golden_modes_check.py` digests equal; the season pins unchanged".
- GATE: `python -m pytest tests/valoria/test_mass_battle_order_of_battle.py tests/valoria/test_mass_battle_army_record.py -q` → pass; `python tools/ci_golden_modes_check.py` → digests equal; the realm content hash at seed 0, one season → equal to B31.09's reading; `python tools/export_troops.py --check` → exit 0.
- HASH MOVERS: none (keys absent by default; arm `off`; upkeep 0).
- DEPENDS ON: V12 Batch B17 (the troop file; `04_MB_typed_outcome_and_one_path`'s per-unit parts); V12 Batch B19a, B19 (MBA-01's `skill`); V12 Batch B22 (B22.02's unit-row precedent; `27_MB_E`); EXISTS-IN-TREE `armyrecord.py::to_order_of_battle`, `orderofbattle.py::_spec_for`.
- GLOSSARY: *experience* (new row, if absent): "how many fields a unit has stood through and learned from, up to two steps"; *arrears* (new row): "seasons a unit's troops went unpaid". *veterancy* (the header) uses the plain word.
- NAMES: `Subformation` → `UnitRow` (B16L); the troop column `power` → `skill` (MBA-01); `power_per_step` → `skill_per_step` (this item).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.10`, `[skip ci]`.

### B31.11 — a unit that stood may learn: the veterancy draw · `04_MB_campaign_party_economy` step (4); `U5b_MB_rulings_in_the_field` §5 · BUILD · HASH EQUAL
- SOURCE: `proposals/04_MB_campaign_party_economy.md` §1 ("**Write:**", as reconciled by the standing rule), "Gate" 2, 3; `proposals/U5b_MB_rulings_in_the_field.md` §5 (items 1, 2, "Gate", "Falsifier", "Movers"), "Tests (W3-1)" §5; rulings A-30 (keyed), A-5 (the one sampler), A-69 (losses on the row); `audits/14_VERBS_MILITARY.md` §0.5 (the standing rule).
- ADVANCES: none of the nine; a veteran unit is worth protecting.
- INSTRUCTION (copied): `engine/season/loop/effects_combat.py::_eff_march`, "on a band that is not `Lost` for the unit's side, for each unit whose part in `FieldOutcome.parts` (a) lost troops and (b) did not rout": "one draw on the one sampler, keyed `H(seed, tick, unit, "veterancy")` (A-30): pool the pool rule on the unit officer's `command` score (the commander's where the unit has none; the untrained default where neither), obstacle `veterancy.ob` in the troop file's header plus one per step already held. Success or better: `experience += 1` to the cap. Partial or Failure: unchanged. A unit destroyed is reset" — "A unit whose part is destroyed (share 0) is reset to 0" — "through the army verbs' one write path (`armyrecord.apply`)". "Condition (a) is the Field of Glory rule … and keeps the write from being a clock." Only under `veterancy.arm: steps`; at `off` nothing is drawn and nothing written. Conditions (a), (b) and the reset read `assigned` after `27_MB_E`'s loss write (A-69, the economy's `Folded:` (2)).
- WHERE: `engine/season/loop/effects_combat.py` (`_eff_march`); `modules/mass_battle/armyrecord.py` (the `apply` command that sets `experience`); `tests/valoria/test_mass_battle_army_record.py`.
- TESTS: `tests/valoria/test_mass_battle_army_record.py::test_veterancy_draw_some_gain_some_do_not` (named by `U5b_MB_rulings_in_the_field`; "200 seeds, `assert checked >= 200`"), `::test_experience_rises_only_for_a_unit_that_lost_and_stood`, `::test_a_destroyed_unit_resets_experience` (named by the economy file), each with `arm: steps` and an `ob` set in the test; written first, read red.
- FALSIFIER and CONTROL: "A gain in every eligible unit" (`U5b` §5); "Experience gained by a unit that took no losses, or kept by one that was destroyed". Control: arm `off` → digests and the realm hash unchanged.
- GATE: §5's gate, copied: "The economy proposal's gate 2 with 200 seeds of one field: some eligible units gain and some do not; an untouched reserve never gains." `python -m pytest tests/valoria/test_mass_battle_army_record.py -q` → pass. The economy's gate 3 ("the same army with its line at `experience` 2 wins more than at 0, beyond the control's spread", n 200, a module reading) is read and quoted in the commit body.
- HASH MOVERS: none at `off` ("Movers. None at `off`").
- DEPENDS ON: V12 B31.10; V12 Batch B05 (the one sampler, the pool rule); V12 Batch B06 (the keyed draw); V12 Batch B19 (`27_MB_A`: the officer's and commander's `command`); V12 Batch B22 (B22.04's loss write); EXISTS-IN-TREE `loop/effects_combat.py::_eff_march`, `armyrecord.py::apply`.
- GLOSSARY: none (*experience* from B31.10).
- COST and TIER: small build; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.11`, `[skip ci]`.

### B31.12 — recruits dilute experience · `04_MB_campaign_party_economy` step (5) · BUILD · HASH EQUAL
- SOURCE: the same file, §1 ("**Dilution, so that recruits matter:**"), "Gate" 4; the `Folded:` (2) (men returning from `absent` do not dilute).
- ADVANCES: none of the nine.
- INSTRUCTION (copied): "`assign_troops` into a unit with `experience > 0` lowers it by one step when the troops added exceed half the unit's strength after the assignment. One rule, in `armyrecord.assign`. (The archived design keeps the higher of two merged units; that makes experience free to launder, so the lower-on-majority rule is proposed instead and marked as a departure.)" "men returning from `absent` are the unit's own and do not dilute its `experience`" (`27_MB_E` §2, §3).
- WHERE: `modules/mass_battle/armyrecord.py` (`assign`); `tests/valoria/test_mass_battle_army_record.py`.
- TESTS: `tests/valoria/test_mass_battle_army_record.py::test_assigning_more_than_half_lowers_experience_one_step` (named), written first, read red.
- FALSIFIER and CONTROL: gate 4: "`assign_troops` adding more than half a unit's strength lowers `experience` by one; adding less does not". Control: every unit at `experience` 0 → the realm hash unchanged.
- GATE: `python -m pytest tests/valoria/test_mass_battle_army_record.py -q` → pass.
- HASH MOVERS: none (no unit holds experience at landing).
- DEPENDS ON: V12 B31.10; EXISTS-IN-TREE `armyrecord.py::assign`; V12 Batch B22 (B22.05's return from `absent`).
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.12`, `[skip ci]`.

### B31.13 — an unfed side starts one morale lower · `04_MB_campaign_party_economy` step (6) · BUILD · HASH EQUAL
- SOURCE: the same file, §2 (the supply bullet), "Gate" 6, "Tests" gate 6; `field_provisioning` (`H-241`).
- ADVANCES: none of the nine.
- INSTRUCTION (copied): "Supply stays SE's: when `field_provisioning` is on and the stores bound a side's fielded troops, that side's morale-start drops by one (the stance row that already feeds it), so 'unfed' has its consequence without a second supply model. One line in `seam/wrappers/mass_battle.py::field_input`." `field_provisioning` ships off (`H-241`), so the line changes nothing at landing.
- WHERE: `engine/season/seam/wrappers/mass_battle.py` (`field_input`); `engine/season/tests/test_march.py`.
- TESTS: `engine/season/tests/test_march.py::test_unfed_side_starts_one_morale_lower` (named), with `field_provisioning` on in the test; written first, read red.
- FALSIFIER and CONTROL: a bounded side whose morale-start is unchanged with provisioning on. Control: provisioning off → the realm hash unchanged.
- GATE: gate 6, copied: "With `field_provisioning` on and stores bounding one side, that side's morale-start is one lower than in the same field with full stores." `python -m pytest engine/season/tests/test_march.py -q` → pass.
- HASH MOVERS: none (the fixture ships off).
- DEPENDS ON: EXISTS-IN-TREE `seam/wrappers/mass_battle.py::field_input`, `::_fed`, `::provision_input`; V12 B31.07.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.13`, `[skip ci]`.

### B31.14 — the unmustered body is a troop row; no stat lent by the side · `27_MB_B` 27B-3 · BUILD · HASH EQUAL
- SOURCE: `proposals/27_MB_B_unit_prowess_on_the_row.md` §3, "Exact edits", "Gate" 1, 3, the batch-item row 27B-3 (NARROWED by A-100: "the row carries `skill`, not `power`; the constructor edits and the five literals' deletion stand"), "Tests"; `unified/U4_DOCUMENT_STATUS.md` §3.4 (SITE); rulings A-59 (2), A-2; U3 §4.1 row 80.
- ADVANCES: none of the nine; a unit's quality comes from its own row.
- INSTRUCTION:
  1. SITE (§5.7): open `modules/mass_battle/hierarchy/units.py` and `core/contact_draw.py` (B19) and record in the commit body which attribute of a unit the contact vector reads as its men's skill after MBA-04 (`power` kept as the attribute name, or `skill`); steps 2–4 write that one.
  2. Copied: "The troop file gains the row `infantry`, 'an unmustered body', carrying today's literals transcribed (`power: 4`, `discipline: 5`; its morale still comes from the side's stance rows), and the constructor reads it." Written `skill: 4, discipline: 5` (MBA-01 step 2).
  3. Copied: "The season's constructors (`orderofbattle.build_unit`, `massbattle._weighted_unit`, `_person_unit`) give every `Subunit` its own `power`, `discipline` and `morale` from its troop row. `Unit.power` and `Unit.discipline` are not set by the season, and `eff_power` / `eff_discipline` raise, on a season-built unit, where they would have inherited. The inheritance stays for the harness until that code leaves."
  4. Delete `_SEASON_FORCE_POWER` (`massbattle.py`), `_UNIT_POWER`, `_UNIT_DISCIPLINE` (`orderofbattle.py`); `_UNIT_COMMAND` and `_MVP_UNIT_COMMAND` are `27_MB_A` §2's (B19): if still present, leave them.
- WHERE: `references/troops.yaml` (`troops.infantry`); `tools/export_troops.py`; `engine/engine_params/troops.json`; `modules/mass_battle/massbattle.py` (`_weighted_unit`, `_person_unit`, `_SEASON_FORCE_POWER`); `modules/mass_battle/orderofbattle.py` (`build_unit`, `_UNIT_POWER`, `_UNIT_DISCIPLINE`); `modules/mass_battle/hierarchy/units.py` (`eff_power`, `eff_discipline`); `tests/valoria/test_mass_battle_order_of_battle.py`.
- TESTS (copied): "`test_a_season_built_unit_takes_no_power_from_its_side` (gate 3: build through each of the three constructors and assert `sub.power is not None`)"; "Changed: the test in that file that pins `_UNIT_POWER`, `_UNIT_COMMAND`, `_UNIT_DISCIPLINE` equal to `massbattle`'s literals pins instead that both constructors read the `infantry` row." Mid-batch: that file and `tests/valoria/test_army_battle.py`. (`test_two_units_of_one_army_differ_by_their_rows`, gate 2, reads B31.10's `experience` and is written here with `experience` 2 set on one unit.)
- FALSIFIER and CONTROL: "a constructor still passing `power=` to `Unit` (gate 3's test fails)"; "If any digest moves at 27B-1 to 27B-3, the move is a defect in the edit: stop." Control: "200 seeded headcount fields through `massbattle.resolve_field`: equal to the tree before, field for field."
- GATE: `python tools/ci_golden_modes_check.py` → digests unchanged; the 200 headcount fields equal field for field (`assert checked >= 200`); `git grep -n "_SEASON_FORCE_POWER\|_UNIT_POWER\|_UNIT_DISCIPLINE" modules/ engine/` → nothing; `python -m pytest tests/valoria/test_mass_battle_order_of_battle.py tests/valoria/test_army_battle.py -q` → pass. Gate 2, copied: "An army of two heavy-infantry units, one at `experience` 2: over 200 fields with its same-run control, the experienced unit's share lost differs from its sibling's beyond the control's spread. Swapping which unit holds the experience swaps the reading."
- HASH MOVERS: none.
- DEPENDS ON: V12 B31.10; V12 Batch B19 (MBA-04: the vector; `27_MB_A` §2); EXISTS-IN-TREE `massbattle.py::_weighted_unit`, `::_person_unit`, `::_SEASON_FORCE_POWER`, `orderofbattle.py::build_unit`, `::_UNIT_POWER`, `units.py::eff_power`, `::eff_discipline`.
- GLOSSARY: *prowess* (row exists: a unit's quality only, D-U1-11p): unchanged; the troop row `infantry` is "the unmustered body", plain words.
- NAMES: `Subunit` → `Unit`, `Unit` → `Army` (B16M); the troop column `power` → `skill` (MBA-01); "body" (a unit) → unit (S-8; K9 added: the item's copied text says "body" for a unit).
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.14`, `[skip ci]`.

### B31.15 — a unit's readout · `27_MB_B` 27B-4 · BUILD · HASH EQUAL
- SOURCE: the same file, §4 (NARROWED by A-100, MBA-01: "the readout shows the unit's felling chances against a reference opponent (from `mb_contact.json`), not quality dice; 'no function sums it over an army' stands"), batch-item row 27B-4, "Gate" 6 (narrowed).
- ADVANCES: none of the nine; the designer and the player can be shown what a unit is.
- INSTRUCTION: `modules/mass_battle/troop_types/table.py::readout(row) -> dict`, copied with A-100's narrowing: "steadiness, armour tier, reach class and support ranks of the arm in hand, pace, and the two carry factors, each computed by the function the resolver calls. It is a description of one unit. **No function sums it over an army**". In place of "quality dice": the unit's felling chances against a reference opponent, by `core/contact_table.py::felling_chance` (B19a) `[ASSUMPTION: the reference opponent — basis: none stated; taken as the `infantry` row (B31.14) at full stamina, an optional `against=` argument; UNDECIDED]`.
- WHERE: `modules/mass_battle/troop_types/table.py` (NEW `readout`); `tests/valoria/test_mass_battle_order_of_battle.py`.
- TESTS: `tests/valoria/test_mass_battle_order_of_battle.py::test_readout_felling_chance_equals_the_contact_table` `[ASSUMPTION: test name; E-3]` (gate 6, narrowed: the readout's felling chance equals `felling_chance` called on the same arguments, asserted by calling it; no caller of `readout` sums its values). Written first, read red.
- FALSIFIER and CONTROL: "A function returning one number for an army's strength." Control: no resolution caller (`git grep -n "readout(" modules/mass_battle` → the definition and tests only).
- GATE: `python -m pytest tests/valoria/test_mass_battle_order_of_battle.py -q` → pass; digests equal.
- HASH MOVERS: none ("no caller in resolution").
- DEPENDS ON: V12 B31.14, B31.03 (carry factors), B31.04 (pace); V12 Batch B19a (`core/contact_table.py::felling_chance`, `mb_contact.json`); V12 Batch B17 (`table.py`).
- GLOSSARY: *felling chance* (row exists, MBA §8.3): unchanged.
- COST and TIER: edit; `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.15`, `[skip ci]`.

### B31.16 — pointer: personal combat's carry items for a unit · `IS-PC-P2` · POINTER
- What the pointed items do: `IS-PC-P2` (`master/instructions/IS_B1_PC_MB_DICE.md` "Pointers") closes `03_PC_loadout_and_carry` items 4 and 6 ("design-first in MB") by naming `04_MB_unit_loadout_and_weapon_in_hand_B` stages 3–4: B31.02 (the weapon in hand and its switch) and B31.03 (the carry factors from `combat_kit.carry_demand_of`). Files: `hierarchy/units.py`, `percell.py`, `seam/wrappers/mass_battle.py`. Gate: B31.03's `test_the_factor_handed_in_equals_carry_demand_of`. No work of its own; no commit.

### B31.17 — flip: ground slows horse · `26_MASS_BATTLE_movement_and_fatigue_as_data` §2 (the seeds) · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, §2's table, "Hash movers" ("three flips, each its own commit"), "Gate" 2; D-19 (seeds landed, ratified at the merge, listed for Jordan).
- ADVANCES: none of the nine; "horse loses most of its speed advantage in broken ground and uphill".
- INSTRUCTION (copied): the terrain `pace` column's mounted cells: `forest_broken` **0.6** ("Kriegsspiel 1824: cavalry 250 of 400 paces in light forest (WG K1); Lost Battles: rough ground costs horse double (WG L4)"), `uphill` **0.25** ("Kriegsspiel: 100 of 400 paces up inclines (WG K1)"); every foot cell and `open_flat`, `narrow_pass`, `river_crossing`, `walls` stay 1.0 ("**not established**; no multiplier invented"). Each value carries `status: seed` and its source in a comment.
- WHERE: `references/troops.yaml` (`terrain.forest_broken.pace`, `terrain.uphill.pace`, mounted); `engine/engine_params/troops.json` (re-derived).
- TESTS: `tests/valoria/test_mass_battle_terrain.py::test_horse_pace_by_ground` (B31.05) now reads the shipped values, not the test's.
- FALSIFIER and CONTROL: "horse at three times foot on `uphill`". Control: the revert (every cell 1.0) reproduces B31.15's digests.
- GATE: `python -m pytest tests/valoria/test_mass_battle_terrain.py -q` → pass; `python tools/ci_golden_modes_check.py` → digests read and recorded (moved where a field is fought on those grounds); the realm content hash at seed 0, one season, read.
- HASH MOVERS: every fought field with a mounted body on `forest_broken` or `uphill`. Declared; B31.99's re-pin.
- EXPECTED RED UNTIL B31.99: `python tools/ci_golden_modes_check.py` where a field is fought on those grounds (exit 1 while its pinned digests differ from the moved ones this item's GATE reads), under `[skip ci]` (K9 added this line, as B30.10).
- DEPENDS ON: V12 B31.05.
- GLOSSARY: none.
- NAMES: "body" (a unit) → unit (S-8; K9 added: the item's copied text says "body" for a unit).
- COST and TIER: edit (a value); `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.17`, `[skip ci]`.

### B31.18 — flip: moving fast tires · `26_MASS_BATTLE_movement_and_fatigue_as_data` §3 (`fast_move_drain`) · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, §3 ("`fast_move_drain` is M-3's rule … The seed is a sixth of a clash, chosen so that an envelopment at double pace over a whole bout costs about as much as three clashes; it is Jordan's to set"), "Gate" 3; D-19.
- ADVANCES: none of the nine.
- INSTRUCTION: `references/troops.yaml: fatigue.fast_move_drain: 0` → `2` ("Seed for the flip: 2"), `status: seed`, its source in a comment.
- WHERE: `references/troops.yaml`; `engine/engine_params/troops.json` (re-derived).
- TESTS: `tests/valoria/test_mass_battle_maneuvers.py::test_fast_move_drain_tires_the_wing` (B31.06) reads the shipped value.
- FALSIFIER and CONTROL: "stamina unchanged by a bout of double-pace movement at a non-zero drain". Control: the revert reproduces B31.17's digests.
- GATE: gate 3, copied: "`fast_move_drain: 2`: an enveloping wing's columns read lower stamina at first contact than the same wing at the control, and the envelopment's win share against the same-run control is reported, not targeted" (quoted in the commit body); `python -m pytest tests/valoria/test_mass_battle_maneuvers.py -q` → pass.
- HASH MOVERS: every fought field with a body moving above its pace. Declared; B31.99's re-pin.
- DEPENDS ON: V12 B31.06, B31.17.
- GLOSSARY: none.
- NAMES: "body" (a unit) → unit (S-8; K9 added: the item's copied text says "body" for a unit).
- COST and TIER: edit (a value); `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.18`, `[skip ci]`.

### B31.19 — flip: a hard march, a second field and a short ration tire a side · `26_MASS_BATTLE_movement_and_fatigue_as_data` §3 (`entry`) · BUILD · HASH MOVER(behaviour)
- SOURCE: the same file, §3 (`entry`: `march_partial: 0.7`, `second_field: 0.7`, `unfed: 0.7`; "Every magnitude here but the three transcribed ones is a seed with no historical figure behind it"), its head's `Folded:` (1) (`second_field` is the fallback where a part has no record, A-69), "Gate" 4; D-19.
- ADVANCES: none of the nine; A-69 (a march's result reaches the field).
- INSTRUCTION: `references/troops.yaml: fatigue.entry`: `march_partial`, `second_field`, `unfed` → `0.7` each, `status: seed`; the product floored at 0.3 (B31.07).
- WHERE: `references/troops.yaml`; `engine/engine_params/troops.json` (re-derived).
- TESTS: `engine/season/tests/test_mass_battle_module.py::test_entry_stamina_lowers_the_tired_side` (B31.07) reads the shipped value.
- FALSIFIER and CONTROL: a side entering after a `Partial` march at full stamina. Control: the revert (all 1.0) reproduces B31.18's realm hash.
- GATE: gate 4, copied: "`entry.march_partial: 0.7`, mirror field, n 100, friction pinned off for the test: the tired side loses more often than at 1.0 by more than the sampling band" (`assert checked >= 100`); the realm content hash at seeds 0 to 2, one season, read and recorded.
- HASH MOVERS: every world in which a field is fought after a `Partial` march, a second field in one lap or a short ration. Declared; B31.99's re-pin.
- DEPENDS ON: V12 B31.07, B31.18.
- GLOSSARY: none.
- NAMES: "a second field in one season round" → in one lap (B04).
- COST and TIER: edit (values); `sonnet`, `high`.
- LANDS IT: B31's producer; `Item: B31.19`, `[skip ci]`.

### B31.20 — the other 25 matchup rows, stated, checked against history and banded to the derived rows · MBA-09 · CONTENT · HASH MOVER(behaviour)
- SOURCE: `master/mb_abstraction/MBA_DESIGN_part3.md` §7.1 "Item: MBA-09"; `MBA_DESIGN_part2.md` §3.2 (the classes, the situations, the row schema, the roster table, "How each row is derived"); rulings A-100, A-113 (Jordan: "stated rows checked against history and banded logically to derived results"); U3 §1 item 31 ("one re-pin in B31's last `Item:` commit"); UNDECIDED (8).
- ADVANCES: A-100 for missiles and horse, completing what MBA-05 and MBA-06 ship as seeds; A-113.
- INSTRUCTION (MBA-09's text, copied, with A-113's answer applied):
  1. "(1) the 25 rows of §3.2 not marked ★ … read as MBA-08 reads": the rows, by §3.2's roster (copied): `horse_shock` × `foot_pike` `marching`; `horse_shock` × `foot_pole` `marching`; `horse_shock` × `foot_short` `marching`; `horse_shock` × `foot_missile` `charge_flank_or_rear`, `in_cover`; `horse_shock` × {`horse_shock`, `horse_light`, `horse_missile`} × {`charge_front_unbraced`, `charge_flank_or_rear`}; `horse_light` × {`foot_missile`, `horse_missile`} × {`charge_front_unbraced`, `pursuit`}; `horse_light` × {`foot_pike`, `foot_pole`} `charge_front_braced` ("**refused** (no charge)"); `horse_missile` × each foot class `skirmish` ("evades: the kite"); `foot_missile` × {`foot_pole`, `foot_pike`} `skirmish` ("evades"); `foot_pike` × {`foot_short`, `foot_pole`} `charge_front_unbraced` ("the push of pike"). Each row in §3.2's schema: `{a, d, situation, closes: closes | draw | evades | refused, close_ob, first_tick: {exposure_a, exposure_d, levels_a, levels_d}, stand, status}`, its "why (source)" cell copied into a comment.
  2. "(2) … shields, pikes, horse with lance and missile weapons are NOT taught to personal combat now; their matchup and per-hit rows ship as **stated rows** at `status: stated` (printed so in the battle report, never presented as measured), each (a) **checked against history** … recorded as a named check with its citation; and (b) **banded logically to the derived results**: each stated row must lie inside the band its derived neighbours imply …, checked by a test over the table that reads the derived rows and fails when a stated row leaves its band (extend MBA-08's dominance reading to host it). A stated row moves to `status: derived` only if personal combat later learns the equipment (not scheduled)." The 25 rows and `contact.missile.felling_per_hit` ship `status: stated` (UNDECIDED (8)). The values are content (D-19): drafted by this item, each marked `[ASSUMPTION]` in a comment, listed in the PR body for Jordan.
  3. `modules/mass_battle/troop_types/table.py`: the `status` closed set gains `stated` (MBA-01's loader refuses a status outside its set); the battle report prints `stated` beside such a row (the report `B20`'s `04_MB_playable_field_scenario` prints `[ASSUMPTION: the printer is `harness/field_scene.py`'s report — basis: B20 builds it; read at landing]`).
- WHERE: `references/troops.yaml` (`matchups`: 25 rows; `contact.missile.felling_per_hit` status); `tools/export_troops.py`; `engine/engine_params/troops.json`; `engine/engine_params/mb_contact.json` (re-exported by `tools/export_mb_contact.py`); `modules/mass_battle/troop_types/table.py` (the `stated` status); `tests/sim/gauge_mb.py` (the dominance reading hosts the band check); `tests/valoria/test_mass_battle_matchups.py`. `tools/calibrate_mb_contact.py` and `references/mb_contact/duel_grid.json` are run and read, not edited (UNDECIDED (8)).
- TESTS: in `tests/valoria/test_mass_battle_matchups.py`, written before step 1 and read red: `test_every_stated_row_lies_inside_its_derived_band` and `test_stated_rows_agree_with_history` `[ASSUMPTION: test names; E-3]` — the history checks, copied as named assertions: "a braced pike block stops a frontal charge more often than not; horse ridden into stakes and arrows fails; a pike block without a screen is weak to archers; arrows bounce off shields"; the ordering relations: "a shielded line is no worse than the same line unshielded; a braced pike no worse than an unbraced pike against a charge; heavier armour no worse against the same missile"; and `test_a_status_outside_the_closed_set_is_refused` (`stated` accepted). MBA-06's tests (`test_t6_charge_ordering`, `test_light_horse_does_not_charge_a_set_wall`, `test_no_troop_name_in_the_charge`) run on the new rows.
- FALSIFIER and CONTROL: "as MBA-02 and MBA-06": "a braced pike block that a frontal horse charge beats more often than the horse beats unbraced levy (T-6 inverted)"; "a charge that reads a troop name"; a stated row printed as measured. Control: "the horse against itself".
- GATE: `python tools/calibrate_mb_contact.py --trust` → seven `ok` lines; `--spot 20` → twenty `inside` lines; `python -m pytest tests/valoria/test_mass_battle_matchups.py -q` → pass (n per MBA-06's tests, `assert checked >= …` as written there); `python tests/sim/gauge_mb.py --results` → the dominance report printed in the commit body with each stated row's band; `python tools/export_troops.py --check`, `python tools/export_mb_contact.py --check` → exit 0.
- HASH MOVERS: "fields with the rows; one re-pin in B31's last commit" (B31.99).
- DEPENDS ON: V12 Batch B19a (MBA-01 to MBA-03: the table, its schema, `calibrate_mb_contact.py`); V12 Batch B19 (MBA-04 to MBA-06, MBA-08: the ★ rows, `gauge_mb.py`'s dominance reading); V12 B31.10 ("the economy's cost columns", to read dominance against cost); J-MBA-01: answered by A-113.
- GLOSSARY: *matchup row* (row exists, MBA §8.3): its status set gains *stated*: "a row written from sources and logic, not measured, and printed as such".
- COST and TIER: content and small build; drafting and the history checks `opus`, `high`; the test and loader `sonnet`; the `--trust` and `--spot` runs `haiku`-supervised; a `--trust` failure read by `opus`.
- LANDS IT: B31's producer; `Item: B31.20`, `[skip ci]`.

### B31.99 — re-pin and close readings · E-1 · BUILD · HASH MOVER (the re-pin)
- SOURCE: `V12_STRUCTURE_part4.md` E-1, E-2; `V12_STRUCTURE_part2.md` §5.9, §5.12; U3 §1 item 31 ("one re-pin in B31's last `Item:` commit").
- ADVANCES: none of the nine (B31 names no conjunct; no `reading:` record is written).
- INSTRUCTION: (1) re-record, once: `tools/ci_golden_modes_check.py`'s digests, `tests/valoria/test_field_golden_pins.py`, every `engine/tests/` golden with a field, the realm pins in `engine/season/tests/_realm_goldens.py`, read against B30's close (`reading @<sha>`); the commit says "re-pin: B31.17 terrain pace, B31.18 fast-move drain, B31.19 entry shares, B31.20 stated matchup rows (and B31.08 where a body drifts); every other item at its control". (2) The commit body lists every seed value the batch landed (the arms' `mass_kg`, `strength`, the three flips, the 25 stated rows, the `infantry` row) for Jordan's correction (D-19), and the batch gate's readings and §5.12's record.
- WHERE: the pin files named in (1).
- TESTS: none new; the covering suites `tools/tests_for_diff.py --base <batch-start-sha>` names, once.
- FALSIFIER and CONTROL: a pin that moves at B31.02 to B31.16's tree against B30's close (diff the digests recorded at B31.16 against B30's close: equal, or only B31.08's drifting bodies); control: each flip's revert reproducing the item before it.
- GATE: the BATCH GATE above, read once.
- HASH MOVERS: the re-pin itself.
- DEPENDS ON: B31.01 to B31.20.
- GLOSSARY: none.
- COST and TIER: edit; `sonnet`, `high`; the close's terminal critique `opus`.
- LANDS IT: B31's producer; `Item: B31.99`, the batch's last `Item:` commit, without `[skip ci]`.

| STOP. Batch B31-mb-loadout-economy closes here |
