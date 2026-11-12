# A-100 / A-101 supersession pass: running record

## Status: RECORD (reference; resolves nothing at runtime, CLAUDE.md §0.05). Applies `MBA_DESIGN_part3.md` §8 (rows) and §7.0 (batches) and `master/pc_round/PC_ROUND_SPEC_part2.md` §6 (PCR-1..4) to the live documents. One round; its edits are not themselves audited.

Reconciled: 2026-11-12, A-100/A-101 supersession pass (MBA-nn / PCR-n). Each edited file carries the same line at its head. Rows are those of `MBA_DESIGN_part3.md` §8.1 to §8.3. Disposition marks in the target read `SUPERSEDED by A-100 (MBA-nn): ...`; the text stays readable as history. Paths are under `proposals/2026-11-12-subsystem-audit-suite/`; `P` = `proposals/`.

## Rows applied (§8.1: proposals and the instruction suite)

| row | file edited | result |
|---|---|---|
| `04_MB_cr12_linear_law` step 1 (STANDS, narrowed) | `P/04_MB_cr12_linear_law.md` | done: the bisect bullet struck as dropped; the two instrument bullets stand |
| same, steps 2–3 (SUPERSEDED, MBA-04) | same | done: both steps marked at their head, landing struck in `Depends on` and `Lands in batch` |
| same, gate (NARROWED) | same | done: carrier `EXPOSURE_BASE = 0` |
| partition edits 1–3 (SUPERSEDED, MBA-04) | `P/16_PESSIMIST_MB_partition_and_the_pair_rule.md` | done: marked at "The pair rule", the exact-edits table noted, `Lands in batch` amended |
| partition edit 4, gate rows 1–5 (STANDS) | same | no edit to the rule; edit 4 carries a one-line pointer to MBA-04 step 3 because its landing moved (the only STANDS row given a mark) |
| 27B-1, 27B-2 (SUPERSEDED, MBA-01/04) | `P/27_MB_B_unit_prowess_on_the_row.md` | done: §2, both table rows and `Lands in batch` |
| 27B-3 (NARROWED), 27B-4 and §3 (NARROWED / STANDS) | same | done: `skill` for `power`; readout of felling chances; §3 untouched |
| 27C-1, 27C-2 (STANDS); 27C-3 (STANDS, narrowed) | `P/27_MB_C_dynamic_strength_and_the_residual_chance.md` | done: head note only (27C-3 lands in MBA-04's re-record, (h) read on the contact draw) |
| `27_MB_A`, `27_MB_D`, `27_MB_E`, `26_..._calibration_targets`, `04_MB_unit_loadout_and_weapon_in_hand_B`, `04_MB_squad_grid_...`, the list of STANDS documents, `U5b_MB_residue`, `03_PC_*`, `29_DICE_*` | none | skipped: STANDS, add nothing (the extensions are the MBA items; U3 carries MBA-07 in B30) |
| `26_MASS_BATTLE_cell_scale_and_time` §1, §3 / §2 | `P/26_MASS_BATTLE_cell_scale_and_time.md` | done: §2 NARROWED (range bands, `shots_per_tick`) |
| rout files (STANDS, pursuit damage law NARROWED) | `P/26_MASS_BATTLE_rout_pursuit_and_giving_ground.md`, `P/16_PESSIMIST_MB_rout_has_two_exits.md` | done: head note and the pursuit lines (§3 bullet; steps 2–3) |
| `16_PESSIMIST_MB_one_stamina_ledger` (STANDS, narrowed) | `P/16_PESSIMIST_MB_one_stamina_ledger.md` | done: head note and the "read by" cell (`MB_STAM_SIGMA` leaves; share feeds `rounds_d`) |
| `U5b_MB_rulings_in_the_field` §1 row 1 (STANDS) / row 2 (SUPERSEDED); §2–§5 (STANDS); §6 row 4 (NARROWED) | `P/U5b_MB_rulings_in_the_field.md` | done: row 2 and row 4 marked in place, head note |
| IS-MB-01..05, IS-MB-B3, `IS_B1_PC_MB_DICE.md` IS-PC-01..04, IS-DICE-01 (STANDS) | none | skipped: STANDS |
| IS-MB-06 (SUPERSEDED), IS-MB-P6, IS-MB-B2 (NARROWED) | `master/instructions/IS_B1_PC_MB_DICE_part2.md` | done: item head, P2-1.1 rows, P2-3.1, P2-3.2 and P2-3.5 rows struck or marked |

## Rows skipped (§8.2 and files outside the lane)

| row | why |
|---|---|
| CR-12, ED-MB-0045, ED-1043, MB-07r, CP-T04-04/10, MB-08, CL-TROOP (`workplans/valoria_master_workplan_v11*.md`) | workplans are outside the files this pass was given (`proposals/`, `master/instructions/`, `unified/` ledgers, `master/CODEBASE_IMPROVEMENT_PROPOSAL*.md`); STAGES.md step 5 dispositions v11 positions |
| H-361, H-150, H-97, H-348 (`engine/season/hole_register.yaml`) | a registry; not to be edited by this pass |
| `master/CODEBASE_IMPROVEMENT_PROPOSAL.md`, `_part2.md` | read: no §8 row touches either (their only "pool" hits are `pool_default` and `pooled_report`) |
| `unified/DECISIONS_ANSWERED.md` | a ruling record; not edited |
| `unified/U3_CONFLICT_LEDGER.md`, `U1_OWNERS_AND_VOCABULARY.md`, `U4_*`, `OWED_TO_UNIFICATION.md`, `unified/work/*` | records of other lanes that name the superseded items; read as history, not rows of §8, not edited |

## Glossary and lexicon rows (§8.3 and the PCR "owed" rows)

| term | file edited | result |
|---|---|---|
| contact draw, felling chance, exposure, matchup row, range band | `unified/U1_GLOSSARY.md` §E; `unified/MB_LEXICON_part2.md` group E | done: new rows; *matchup row* also names the `stated` status of A-113 |
| power (retired as a troop stat) | `unified/MB_LEXICON.md` group D; `U1_GLOSSARY.md` §J | done: struck, `skill` replaces it |
| prowess | `unified/MB_LEXICON.md` group D | done (not a §8.3 row; follows 27B-1/2 SUPERSEDED): "where its pool is composed" corrected |
| duel round | `U1_GLOSSARY.md` §J, §K; `MB_LEXICON_part2.md` | done: also the contact draw's unit |
| round, exchange, lap | `U1_GLOSSARY.md` §D, §E, §K | checked, present from the A-101 round lane; *exchange* gains the contact-draw rejection |
| L2-1's `subunit_combat_pool` → `unit_combat_pool` | `unified/MB_LEXICON_part3.md` | done (not a §8 row; the function is deleted by MBA-04 step 4) |

## U3 (§7.0 batches, PCR-1..4)

`unified/U3_DEPENDENCY_ORDER.md`: B19a added (§1 item 18a, §1.2, §1.3, §2.1 row 17a, §2.2, §2.3); B19 re-listed and given B16 and B19a in `after`; MBA-07 in B30; MBA-09 in B31; PCR-1 (first in B15), PCR-2 and PCR-3 (B16) were already in §1 items 15 and 16 and are added to §1.2, §1.3, §2.1 and the census; PCR-4 stays an unscheduled candidate; §1.5 lists the items and the six new batch edges; §3.1 notes on four superseded nodes; census rows; §6.1 test files. Waves recomputed by script (it first reproduced the old waves and the old schedule exactly).

## Findings of this pass (for the orchestrator)

1. **The critical path grows by two waves, not one.** `MBA_DESIGN_part2.md` §5.3 lists the cascade as B20, B22, B23, B30, B31 and says B38 is one wave later. B32 follows B20 (U3 §2.1 row 31), so B32, B33, B35, B36, B38, B39, B40 move too: the last batch goes W17 to W19 and the critical path is 20 batches (was 18), through B15, B16, B19a, B19, B20, B32. U3 §2.2 states it; `MBA_DESIGN_part2.md` is not mine to edit.
2. **A two-way edge inside B19.** MBA-06 depends on MBA-04, and MBA-04 step 5 reads the `pursuit` row MBA-06 step 4 ships. U3 splits MBA-04 step 5 to land after MBA-06 (an [ASSUMPTION], reversible).
3. **A-113 answered J-MBA-01 while the design was being applied**: MBA-09 is no longer BLOCKED (stated rows). U3 and the glossary follow A-113; the A-100 design files already carry it.
4. **A-102's B03c** (inserted by another lane, wave "not recomputed") moves every batch downstream of B04 by two more waves; the combined figures (last batch W21, critical path 22, 23 steps) are in U3 §2.2 as a note, not in the tables.
5. Other sessions committed parts of these edits while the pass ran (`git log` shows `[design]` commits touching the same files); nothing here was committed by this pass.
