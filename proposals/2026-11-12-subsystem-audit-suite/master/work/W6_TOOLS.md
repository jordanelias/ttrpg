# W6 · `tools/`: who calls each tool

## Status: WORK FILE (a script-built extract for `master/HOLISTIC_AUDIT.md`; reference; deleted when the stage closes)

## Read at: `4dc8a7b` (working tree, 2026-11-12).

Method: for each `tools/*.py`, is its file name written in `references/ci_checks_registry.yaml`, in `.github/workflows/valoria-ci.yml`, in `tools/valoria_local.py`, in `.claude/settings.json`; and how many other tracked files name its stem as a whole word (`tools/`, test files, `engine/`+`modules/` non-test, `skills/`+`.claude/`+`.github/`+`.githooks/`). **Name matching over-counts** for generic stems (`names`, `registry`, `pathres`) and counts a comment as a reference; a zero is reliable, a non-zero is a lead.

| tool | lines | in ci_checks_registry | in CI workflow | in valoria_local | in settings hooks | named by other tools | by tests | by engine/modules | by skills, commands, hooks |
|---|---|---|---|---|---|---|---|---|---|
| `broken_dependency_checker.py` | 515 | yes | yes | yes | - | 7 | 1 | 0 | 5 |
| `build_engine_atlas.py` | 594 | - | - | - | - | 1 | 2 | 0 | 0 |
| `build_identifier_census.py` | 555 | yes | yes | yes | - | 2 | 2 | 0 | 1 |
| `canon_coverage_check.py` | 260 | yes | yes | - | - | 1 | 0 | 0 | 1 |
| `ci_claim_provenance_check.py` | 345 | yes | yes | yes | - | 2 | 2 | 1 | 1 |
| `ci_co_file_checker.py` | 134 | yes | yes | yes | - | 6 | 1 | 0 | 1 |
| `ci_common.py` | 762 | yes | yes | - | - | 45 | 13 | 2 | 3 |
| `ci_design_prose_quarantine.py` | 118 | yes | yes | yes | - | 1 | 1 | 1 | 2 |
| `ci_editorial_checker.py` | 103 | yes | yes | yes | - | 5 | 0 | 0 | 2 |
| `ci_generation_consistency.py` | 120 | yes | yes | yes | - | 3 | 0 | 0 | 3 |
| `ci_golden_modes_check.py` | 189 | yes | yes | - | - | 0 | 4 | 2 | 1 |
| `ci_module_shape_check.py` | 136 | yes | yes | yes | - | 2 | 1 | 0 | 2 |
| `ci_names_consistency.py` | 144 | yes | yes | yes | - | 5 | 2 | 0 | 1 |
| `ci_naming_check.py` | 317 | yes | yes | yes | - | 6 | 2 | 0 | 2 |
| `ci_pp_frozen_check.py` | 147 | yes | yes | yes | - | 1 | 0 | 0 | 1 |
| `ci_quantity_vocabulary_check.py` | 186 | yes | yes | - | - | 3 | 1 | 0 | 4 |
| `ci_register_size_check.py` | 265 | yes | yes | yes | - | 4 | 0 | 0 | 2 |
| `ci_sim_fabrication_check.py` | 618 | yes | yes | yes | - | 5 | 4 | 5 | 3 |
| `ci_vacuous_assertion_check.py` | 295 | yes | yes | - | - | 0 | 0 | 0 | 1 |
| `ci_vetting_check.py` | 207 | yes | yes | yes | - | 4 | 0 | 0 | 1 |
| `compliance_check.py` | 238 | yes | yes | yes | - | 3 | 1 | 0 | 1 |
| `currency_consistency_check.py` | 539 | yes | yes | yes | - | 5 | 0 | 0 | 2 |
| `definitions_store.py` | 216 | - | - | - | - | 0 | 3 | 0 | 0 |
| `descriptor_registry.py` | 83 | - | - | - | - | 8 | 13 | 13 | 8 |
| `export_battle_orders.py` | 72 | yes | - | yes | - | 1 | 1 | 4 | 0 |
| `export_composition.py` | 270 | yes | yes | yes | - | 4 | 4 | 3 | 1 |
| `export_descriptors.py` | 312 | yes | yes | yes | - | 3 | 8 | 3 | 1 |
| `export_engine_params.py` | 187 | yes | yes | yes | - | 5 | 3 | 4 | 1 |
| `export_game_constants.py` | 266 | yes | yes | yes | - | 2 | 3 | 0 | 1 |
| `export_names.py` | 187 | yes | yes | - | - | 4 | 1 | 4 | 1 |
| `export_npc_roster.py` | 226 | yes | yes | yes | - | 1 | 1 | 4 | 1 |
| `export_sim_params.py` | 326 | - | - | - | - | 2 | 1 | 1 | 2 |
| `fold_ledger_to_latest.py` | 135 | yes | - | - | - | 2 | 0 | 0 | 0 |
| `freshness_gate.py` | 287 | yes | yes | yes | - | 4 | 0 | 0 | 2 |
| `gen_sigma_parity_goldens.py` | 190 | - | - | - | - | 1 | 2 | 1 | 0 |
| `hook_md_sweep_guard.py` | 131 | - | - | - | yes | 0 | 0 | 0 | 1 |
| `hook_naming_guard.py` | 55 | - | - | - | yes | 3 | 2 | 0 | 1 |
| `join_audit_workings.py` | 253 | - | - | - | - | 0 | 0 | 0 | 0 |
| `link_values_pointers.py` | 176 | - | - | - | - | 0 | 1 | 1 | 0 |
| `m1_acceptance.py` | 489 | yes | yes | - | - | 1 | 6 | 5 | 4 |
| `mechanics_index_gen.py` | 522 | yes | yes | - | - | 1 | 0 | 0 | 1 |
| `methodology_drive.py` | 155 | - | - | - | - | 0 | 0 | 0 | 1 |
| `names.py` | 164 | yes | yes | yes | - | 40 | 169 | 194 | 36 |
| `pathres.py` | 641 | - | - | - | - | 7 | 5 | 0 | 1 |
| `quantity_registry.py` | 257 | yes | - | - | - | 3 | 2 | 0 | 3 |
| `registry.py` | 425 | yes | - | yes | - | 19 | 41 | 72 | 18 |
| `session_provision.py` | 59 | - | - | - | - | 0 | 0 | 0 | 2 |
| `tag_normalizer.py` | 137 | - | - | - | - | 0 | 1 | 0 | 1 |
| `tests_for_diff.py` | 115 | - | - | - | - | 0 | 0 | 0 | 3 |
| `triage_work_items.py` | 272 | - | - | - | - | 2 | 0 | 0 | 0 |
| `validate_ed_citations.py` | 606 | yes | yes | yes | - | 7 | 0 | 1 | 2 |
| `valoria_local.py` | 232 | yes | yes | - | - | 5 | 0 | 0 | 5 |
| `verify_handoff_split.py` | 662 | - | - | - | - | 0 | 0 | 0 | 0 |
| `vocab_store.py` | 175 | - | - | - | - | 0 | 1 | 0 | 0 |
