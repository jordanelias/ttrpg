# VALORIA REPOSITORY FILE INDEX
## Last updated: 2026-04-13 (v30 complete)
## Purpose: Single-source map of every committed file → game system → status
## Maintained by: valoria-orchestrator skill (update on every commit that adds/modifies a file)
## Format: path | systems | type | status | depends_on | referenced_by
## Three-mode framing: ALL systems stated as TTRPG baseline → Hybrid → Board Game.
## TTRPG = source layer. Hybrid = bridge. Board Game = abstraction. designs/ = working layer. compilation/ = snapshot.

---

## v30 Baseline Applied (2026-04-13)
> All canonical design docs renamed to `_v30.md` suffix. 40 deprecated files moved to `deprecated/designs/`. See `references/design_registry.yaml` for full atomization registry.

## HOW TO USE

- **systems**: which game mode(s) the file primarily covers (ALL / TTRPG / BG / HYBRID / INFRA)
- **type**: CANON (immutable) | COMPILED (checkpoint) | DESIGN (proposal) | TEST (simulation) | SKILL | TOOL | REF (parameter/reference) | LOG
- **status**: CURRENT | STALE | SUPERSEDED | DEPRECATED
- **depends_on**: files this file's content relies on being correct
- **referenced_by**: files that cite or build on this file

---

## CANON (immutable — do not modify without explicit canon amendment)

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| canon/00_philosophical_foundations.md | ALL | CURRENT | Highest authority. Governs all design. |
| canon/01_foundations_amendment_self_rendering.md | ALL | CURRENT | Amendment to foundations |
| canon/02_canon_constraints.md | ALL | CURRENT | Mechanical constraints derived from foundations |
| canon/03_canonical_timeline.md | ALL | CURRENT | World timeline |
| canon/README.md | INFRA | CURRENT | — |
| canon/audit_threadwork_v24.md | TTRPG | CURRENT | Audit of v24 threadwork vs foundations |
| canon/audit_threadwork_v25.md | TTRPG | CURRENT | Audit of v25 threadwork vs foundations |
| canon/editorial_ledger.yaml | ALL | CURRENT | Source of truth for editorial decisions |
| canon/patch_register_active.yaml | ALL | CURRENT | All patches PP-001 onwards |

---

## COMPILATION v0.14 (DEPRECATED — all stages outdated as of 2026-04-09)

> **All compilation/v0.14 stage documents are DEPRECATED.** Design docs in designs/ and params files in references/ are canonical. See canonical_sources.yaml. Each stage file now has a DEPRECATED header naming its replacement.

| File | Systems | Status | Canonical Replacement |
|------|---------|--------|----------------------|
| compilation/v0.14/stage1_core_engine_deprecated.md | ALL | DEPRECATED | references/params_core.md |
| compilation/v0.14/stage2_characters_deprecated.md | TTRPG/HYBRID | DEPRECATED | references/params_core.md |
| compilation/v0.14/stage3_thread_operations_deprecated.md | TTRPG/HYBRID | DEPRECATED | designs/ttrpg/threadwork_v30.md |
| compilation/v0.14/stage3_compilation_report.md | INFRA | DEPRECATED | Process artifact |
| compilation/v0.14/stage4_southernmost_deprecated.md | TTRPG/HYBRID | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage5_clocks_deprecated.md | ALL | DEPRECATED | designs/systems/clock_registry_v30.md |
| compilation/v0.14/stage6_factions_deprecated.md | TTRPG | DEPRECATED | BG/Hybrid: bg_v05. TTRPG: no replacement — unverified |
| compilation/v0.14/stage7_territories_deprecated.md | ALL | DEPRECATED | designs/setting/geography_v30.md |
| compilation/v0.14/stage8_combat_deprecated.md | ALL | DEPRECATED | designs/combat/combat_v30.md |
| compilation/v0.14/stage9_social_deprecated.md | TTRPG | DEPRECATED | designs/contest/social_contest_v30.md |
| compilation/v0.14/stage10_advancement.md | TTRPG | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage11_scale_transitions_deprecated.md | HYBRID | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage12_campaign_modes_deprecated.md | ALL | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage13_npcs.md | ALL | DEPRECATED | designs/npcs/npc_roster_v30.md (partial) |
| compilation/v0.14/stage14_gm_tools.md | ALL | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage15_spell_catalog.md | TTRPG | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage16_reference.md | ALL | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage17_canon_guard.md | ALL | DEPRECATED | skills/valoria-canon-guard/SKILL.md |
| compilation/v0.14/stage_bg_board_game_mode_deprecated.md | BG | DEPRECATED | designs/board_game/board_game_v30.md |
| compilation/v0.14/valoria_ruleset_v0.14_deprecated.md | ALL | DEPRECATED | Compilation snapshot — all stages outdated |

---

## DESIGNS — BOARD GAME

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| **designs/board_game/board_game_v30.md** | **BG/HYBRID** | **CURRENT** | Canonical BG faction mechanics. P-12–P-32 applied. |
| ~~designs/board_game/valoria_bg_v05_stress_test_report_deprecated.md~~ | — | DEPRECATED | Moved to deprecated/designs/board_game/ (2026-04-13) |
| designs/board_game/victory_v30.md | BG/ALL | CURRENT | Canonical victory conditions. PP-406–PP-427. |
| ~~designs/board_game/faction_resolutions_2026_04_07_deprecated.md~~ | — | DEPRECATED | Moved to deprecated/designs/board_game/ (2026-04-13) |
| designs/board_game/varfell_path_b_v30.md | BG | AWAITING REVIEW | ED-311 |
| designs/board_game/valoria_map_v2.svg | BG | CURRENT | Visual map |
| ~~19 superseded BG files~~ | — | DEPRECATED | Moved to deprecated/designs/board_game/ (2026-04-09) |

---

## DESIGNS — COMBAT

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| **designs/combat/combat_v30.md** | **ALL** | **CURRENT** | Canonical combat design. PP-086–092+. |

---

## DESIGNS — MASS COMBAT

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| **designs/mass_combat/mass_battle_v30.md** | **ALL** | **CURRENT** | Canonical mass battle spec. ST-MB patches. |

---

## DESIGNS — CONTEST (Social/Debate)

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| **designs/contest/social_contest_v30.md** | **ALL** | **CURRENT** | Canonical social contest. PP-234. Supersedes debate_system_redesign_v1. |
| ~~designs/debate/*~~ | — | DEPRECATED | Moved to deprecated/ (2026-04-09). Superseded by contest system. |

---

## DESIGNS — TTRPG (Threadwork & Mechanics)

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| **designs/ttrpg/threadwork_v30.md** | **TTRPG/HYBRID/BG** | **CURRENT** | Canonical threadwork spec. |
| designs/ttrpg/threadwork_philosophical_reference_v30.md | TTRPG | REFERENCE | Extracted from threadwork v25 Part 1 |
| designs/ttrpg/batch_a_designs.md | TTRPG | REFERENCE | Session 4 gap designs — check if gaps still open |
| designs/ttrpg/batch_ad_resolutions.md | TTRPG | PROPAGATION-PENDING | Approved decisions not yet in working files |
| designs/ttrpg/batch_bc_designs.md | TTRPG | REFERENCE | Session 4 military+political gap designs |
| designs/ttrpg/batch_d_designs.md | TTRPG | REFERENCE | Session 4 faction identity packages |
| designs/ttrpg/batch_e_designs.md | TTRPG | REFERENCE | Session 5 BG design briefs — mostly in bg_v05 |
| designs/ttrpg/batch_f_designs.md | TTRPG | REFERENCE | Session 5 hybrid+endgame |
| designs/ttrpg/church_territorial_seizure.md | TTRPG/BG | VERIFY | Approved. Check parity with bg_v05 TC 80. |
| designs/ttrpg/edeyja_npc.md | TTRPG | WORKING | Canonical NPC (ED-048 adjacent) |
| designs/ttrpg/generation_tasks_gt01_gt02_gt03.md | TTRPG | AWAITING REVIEW | Do not propagate without user sign-off |
| designs/ttrpg/lowenritter_faction_card.md | BG | WORKING | Verify parity with bg_v05 |
| designs/ttrpg/mechanical_tasks_and_patches.md | TTRPG | WORKING | R-54–R-68 applied |
| designs/ttrpg/succession_mechanic.md | ALL | PROPAGATION-PENDING | Approved. No home in working files yet. |
| designs/ttrpg/valoria_emergent_scenarios.md | TTRPG | WORKING | Emergent scenario map |
| designs/ttrpg/valoria_narrative_scenario_chains.md | TTRPG | WORKING | NPC arcs. Contains "Ceiral" references (ED-048). |
| designs/ttrpg/SUPERSEDED.md | INFRA | DEPRECATED → deprecated/designs/ttrpg/ | Notice file for Phase 1 artifacts |

---

## DESIGNS — HYBRID

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| **designs/hybrid/scale_transitions_v30.md** | **HYBRID/ALL** | **CURRENT** | Canonical scale transitions and mode bridging. Supersedes stage11. PP-594. |
| designs/hybrid/hybrid_gaps_v30.md | HYBRID | PROPAGATION-PENDING | 17 gaps resolved. Not yet in bg_v05. |

---

## DESIGNS — CONVICTION TRACK

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/conviction_track/conviction_track_v30.md | BG/ALL | WORKING | PP-406–PP-418 design proposal. NOT committed as patches. |

---

## DESIGNS — SETTING

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/setting/geography_v30.md | ALL | CURRENT | Canonical geography. 17 territories. |
| designs/setting/calamity_radiation_v30.md | ALL | CURRENT | Calamity radiation framework. |
| designs/setting/adjacency_map.jsx | ALL | CURRENT | Visual adjacency tool |

---

## DESIGNS — SYSTEMS

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/systems/clock_registry_v30.md | ALL | CURRENT | Unified clock/track registry. PP-496. |

---

## DESIGNS — NPCs

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/npcs/npc_roster_v30.md | ALL | CURRENT | 13-character roster. ED-358. |

---

## DESIGNS — WORLDBUILDING

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/worldbuilding/worldbuilding_v30.md | ALL | CURRENT | Latest worldbuilding integration |
| designs/worldbuilding/worldbuilding_canon_audit_v30.md | ALL | CURRENT | Audit of v3 |
| designs/worldbuilding/editorial_comprehensive_review.md | ALL | DEPRECATED | Comprehensive editorial review |
| ~~v1, v1_audit, v2~~ | — | DEPRECATED | Moved to deprecated/ (2026-04-09) |

---

## DESIGNS — COGNITIVE LOAD & META

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/cogload_moderate_target.md | ALL | CURRENT | Moderate ceiling target |
| designs/cogload_reduction_strategies.md | ALL | CURRENT | Moderate-Heavy ceiling |
| designs/companion_app_design_note.md | ALL | CURRENT | Companion app design note |
| designs/valoria_systematic_critique.md | ALL | CURRENT | Full systematic critique |
| designs/lir_ff_impact.md | BG | WORKING | PP-177. Status: "not yet committed" — verify. |

---

## DESIGNS — Game Master REFERENCE (CP14)

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/gm_ref_cp14/gm_reference_workplan.md | ALL | DEPRECATED | — |
| designs/gm_ref_cp14/arcs/arcs_01_04_rebuilt.md | ALL | DEPRECATED | Campaign arcs 1–4 |
| designs/gm_ref_cp14/arcs/arcs_05_08_rebuilt.md | ALL | DEPRECATED | — |
| designs/gm_ref_cp14/arcs/arcs_09_11_elske_baralta.md | ALL | DEPRECATED | — |
| designs/gm_ref_cp14/arcs/arcs_12_15_faction_transitions.md | ALL | DEPRECATED | — |
| designs/gm_ref_cp14/arcs/arcs_16_19_faction_domain_echoes.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_20_23_branching.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_24_27_branching.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_28_30_coherence_zero.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_31_35_hybrid_systems.md | HYBRID | CURRENT | Arcs 32, 34, 35 NOT YET SIMULATED. |
| designs/gm_ref_cp14/arcs/valoria_emergent_arcs_experimental.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/valoria_emergent_campaign_arcs.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d01–d10 | ALL | DEPRECATED | All 10 dashboard files |
| designs/gm_ref_cp14/flowcharts/flowchart_templar_crossing.md | ALL | DEPRECATED | — |
| designs/gm_ref_cp14/zoom_in_out_reference_card.md | ALL | DEPRECATED | — |

---

| designs/npcs/npc_roster_caste_annotations.md | ALL | DEPRECATED | Caste-axis impact on all 13 roster NPCs |
| designs/npcs/ed_403_406_407_resolutions.md | ALL | DEPRECATED | RM split, Ehrenwall assessment, consecration crisis |

## DESIGNS — MECHANICS
| designs/mechanics/baralta_crown_claim_v30.md | BG/HYBRID | CURRENT | Crown Succession Contest, Stake Claim DA, consecration crisis BG expression |
| designs/npcs/lenneth_threadwork_design.md | ALL | DEPRECATED | Lenneth stat block, TS development, Cultural Revival Track, threadwork at ruler diamond decision points |

## GM REFERENCE (gm_ref/)

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| gm_ref/arcs_01_04_nongreedy.md | ALL | CURRENT | Batch 01 arcs |
| gm_ref/arcs_05_09_batch02.md | ALL | CURRENT | Batch 02 arcs |
| gm_ref/arcs_10_18_consolidated.md | ALL | CURRENT | Batch 03 consolidated |
| gm_ref/arcs_36_40_interdependent.md | ALL | CURRENT | Emergent interdependent arcs batch 1 |
| gm_ref/arcs_41_45_interdependent.md | ALL | CURRENT | Emergent interdependent arcs batch 2 |
| ~~4 deprecated arc revision files~~ | — | DEPRECATED | Moved to deprecated/gm_ref/ (2026-04-09) |
| ~~gm_ref/debate_ref_card_v1.md~~ | — | DEPRECATED | Moved to deprecated/ — superseded by contest system |

---

## REFERENCES (parameter files)

| File | Systems | Status | Source Document |
|------|---------|--------|----------------|
| references/params_core.md | ALL | CURRENT | stage1 (legacy source) |
| references/params_combat.md | ALL | CURRENT | combat_v30.md |
| references/params_mass_combat.md | ALL | CURRENT | mass_battle_v30.md |
| references/params_factions.md | ALL | CURRENT | stage6 (TTRPG) + bg_v05 (BG) |
| references/params_board_game.md | BG | CURRENT | bg_v05 |
| references/params_contest.md | ALL | CURRENT | social_contest_v30.md |
| references/params_fieldwork.md | TTRPG/HYBRID/BG | CURRENT | fieldwork_v30.md |

| references/params_threadwork.md | TTRPG/HYBRID | CURRENT | threadwork_v30.md |
| references/params_scale_transitions.md | HYBRID | CURRENT | stage11 (legacy source) |
| references/params_core_history.md | ALL | CURRENT | Patch history |
| references/params_combat_history.md | ALL | CURRENT | Patch history |
| references/params_mass_combat_history.md | ALL | CURRENT | Patch history |
| references/params_board_game_history.md | BG | CURRENT | Patch history |
| references/params_threadwork_history.md | TTRPG/HYBRID | CURRENT | Patch history |
| references/glossary.md | ALL | CURRENT | Term expansion reference |
| references/design_registry.yaml | ALL | CURRENT | v30 design doc atomization map. Established 2026-04-13. |
| references/canonical_sources.yaml | ALL | CURRENT | System authority map |
| references/file_index.md | ALL | CURRENT | This file |
| references/arc_register.md | ALL | CURRENT | Arc system v8 (2026-04-13, PP-575). Vector format. 120+ arcs, 5 categories. Replaces v7. ED-401-405 open. |
| references/propagation_map.md | ALL | CURRENT | Cross-reference dependencies |
| references/effort-guide.md | INFRA | CURRENT | Effort calibration per skill |
| references/D10_INTEGRATION_GUIDE.md | ALL | CURRENT | — |
| references/d10_success_probabilities.json | ALL | CURRENT | — |
| references/sim_decision_protocols.md | ALL | CURRENT | — |
| ~~references/params_debate.md~~ | — | DEPRECATED | Moved to deprecated/ — superseded by params_contest.md |
| ~~references/params_debate_history.md~~ | — | DEPRECATED | Moved to deprecated/ |

---

## SKILLS (dir-based — canonical)

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| skills/valoria-orchestrator/SKILL.md | INFRA | CURRENT | Session management |
| skills/valoria-orchestrator/references/* | INFRA | CURRENT | Orchestrator reference files |
| skills/valoria-orchestrator/scripts/github_ops.py | INFRA | CURRENT | GraphQL batch reader |
| skills/valoria-canon-guard/SKILL.md | INFRA | CURRENT | Canon compliance |
| skills/valoria-chunker/SKILL.md | INFRA | CURRENT | Pre-process large docs |
| skills/valoria-mechanic-audit/SKILL.md | INFRA | CURRENT | Audit + consistency |
| skills/valoria-simulator/SKILL.md | INFRA | CURRENT | Simulation Modes A–M |
| skills/valoria-compiler/SKILL.md | INFRA | CURRENT | Compilation |
| skills/valoria-editorial-register/SKILL.md | INFRA | CURRENT | Editorial management |
| skills/valoria-arc-generator/SKILL.md | INFRA | CURRENT | Arc generation |
| skills/valoria-combat-simulator/SKILL.md + refs | INFRA | CURRENT | Combat simulation |
| skills/valoria-dice-model/SKILL.md + script | INFRA | CURRENT | Dice math |
| ~~6 flat skill files~~ | — | DEPRECATED | Moved to deprecated/skills/ (2026-04-09) |

---

## TESTS (all current)

| File | Systems | Status |
|------|---------|--------|
| tests/coverage_matrix.md | ALL | CURRENT |
| tests/sim_* (all simulation outputs) | Various | CURRENT |
| tests/stale_scan_bg_01.md | BG | CURRENT |
| tests/threadwork_decision_point_analysis.md | ALL | CURRENT | 8 threadwork decision points tested against arc register |
| tests/arc_branch_simulation.md | ALL | CURRENT | 7 key rolls simulated (Success/Failure branches, RS/TC/IP cascades) |
| tests/delay_vs_preclusion_evaluation.md | ALL | CURRENT | Roll failures reclassified: 6/7 are delays, 1 True Preclusion |

---

## TOOLS (all current)

| File | Purpose | Status |
|------|---------|--------|
| tools/broken_dependency_checker.py | Validate references | CURRENT |
| tools/coverage_matrix.py | Track simulation coverage | CURRENT |
| tools/editorial_review/valoria-editorial-review.jsx | Editorial review UI | CURRENT |
| tools/find_references.py | Cross-reference finder | CURRENT |
| tools/freshness_gate.py | Freshness validation | CURRENT |
| tools/model_router.html | Model routing reference | CURRENT |
| tools/patch_propagation_checker.py | Patch propagation | CURRENT |
| tools/propagator.py | Propagate patches | CURRENT |
| tools/verify_cuts.py | Verify patch cuts | CURRENT |

---

## INFRASTRUCTURE

| File | Status | Notes |
|------|--------|-------|
| .github/workflows/valoria-ci.yml | CURRENT | CI workflow |
| docs/freshness_gate_spec.md | CURRENT | Freshness gate spec |
| session_log_current.md | CURRENT | Active session log |
| session_log_archive.md | CURRENT | Archived sessions |

---

## DEPRECATED (deprecated/ directory)

All files in `deprecated/` are superseded and retained for audit trail only. Each has a DEPRECATED header naming its replacement. Do not reference in new design work.

Major groups moved 2026-04-09:
- 19 board game evolution files (bg_v01–v04, proposals, syntheses, improvements)
- 4 gm_ref arc revision files (superseded by arcs_10_18_consolidated.md)
- 4 debate system files + 2 debate params + 1 debate ref card (superseded by contest system)
- 3 worldbuilding v1/v2 files (superseded by v3)
- 5 root-level orphan files (workplan, gap register, patch proposals, scope map, project instructions)
- 6 flat skill files (superseded by dir-based versions)
- 1 qwen ruleset (non-authoritative)
- 1 empty `path` file (deleted)

---

## PROPAGATION-PENDING

| File | Decisions Pending | Target Files |
|------|-------------------|--------------|
| designs/ttrpg/batch_ad_resolutions.md | G-053, G-040, G-054, G-042, G-038, G-044, Varfell transfer | threadwork_v25, characters, faction files |
| designs/ttrpg/succession_mechanic.md | Almud succession mechanic | Needs political_mechanics.md or similar |
| designs/ttrpg/church_territorial_seizure.md | TC 80 per-territory roll | Verify parity with bg_v05 |
| designs/hybrid/hybrid_gaps_v30.md | 17 hybrid gaps | stage11, bg_v05 §B.5 |
| designs/ttrpg/mechanical_tasks_and_patches.md | R-65/R-66 blocked by ED-047 | stage15, stage5 |

---

*Index maintained by valoria-orchestrator. Update this file in the same commit as any file that changes its status, system classification, or dependency relationships.*

| designs/systems/npc_behavior_v30.md | NPC Behavior System design | 2026-04-13 | ACTIVE | Stance Triangles, Priority Trees, Arc Emergence |
| tests/audit_npc_behavior_system.md | NPC Behavior System audit | 2026-04-13 | COMPLETE | 15 findings |

## FIELDWORK SUBSYSTEM FILES (added 2026-04-13 — skeleton split)

| File | System | Status | Notes |
|------|--------|--------|-------|
| designs/fieldwork/fieldwork_v30.md | FIELDWORK | CURRENT | Master index + §1 Depth Axis + §2 Fieldwork Pool + §7 Derived Values. 224 lines (split from 856). |
| designs/fieldwork/fieldwork_exploration.md | FIELDWORK | CURRENT | §3 Exploration. 72 lines. |
| designs/fieldwork/fieldwork_investigation.md | FIELDWORK | CURRENT | §4 Investigation. 111 lines. |
| designs/fieldwork/fieldwork_socializing.md | FIELDWORK | CURRENT | §5 Socializing. 132 lines. |
| designs/fieldwork/fieldwork_exposure.md | FIELDWORK | CURRENT | §6 Exposure. 82 lines. |
| designs/fieldwork/fieldwork_bg.md | FIELDWORK/BG | CURRENT | §8 Board Game Mode. 47 lines. |
| designs/fieldwork/fieldwork_hybrid.md | FIELDWORK/HYBRID | CURRENT | §9 Hybrid Mode. 27 lines. |
| designs/fieldwork/fieldwork_godot.md | FIELDWORK/GODOT | CURRENT | §10 Godot + validation findings G10-F01–F07. 132 lines. |
| designs/fieldwork/fieldwork_summary.md | FIELDWORK | CURRENT | §11 Three-Mode Summary Table. 20 lines. |
| designs/fieldwork/fieldwork_editorial.md | FIELDWORK | CURRENT | §12 Open Items and Editorial Flags. 116 lines. |
| designs/fieldwork/fieldwork_rationale.md | FIELDWORK | CURRENT | §13 Design Rationale Index (NEW). 69 lines. Content file — no mechanical values. |


## NEW DOCS — v30 Skeleton/Infill (added 2026-04-13)

### Structure Note
Every v30 design doc now has a companion `_infill.md` file in the same directory.
Skeleton (`_v30.md`): tables, formulas, procedures, edge case rulings.
Infill (`_v30_infill.md`): prose, rationale, design history, examples.
Registry: `references/design_registry.yaml` tracks atomization status for all docs.

### Previously Unverified Systems — Now Unblocked
| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/ttrpg/factions_ttrpg_v30.md | TTRPG | CURRENT | From stage6. TTRPG faction mechanics. SIM-FAC verified. |
| designs/ttrpg/factions_ttrpg_v30_infill.md | TTRPG | CURRENT | Infill: prose/rationale |
| designs/setting/southernmost_v30.md | TTRPG/BG | CURRENT | From stage4. PP-643 (SIM-STH-E1) applied. SIM-STH verified. |
| designs/setting/southernmost_v30_infill.md | TTRPG/BG | CURRENT | Infill |
| designs/systems/campaign_modes_v30.md | ALL | CURRENT | From stage12. Procedural. |
| designs/systems/campaign_modes_v30_infill.md | ALL | CURRENT | Infill |

### New Params Files
| File | Systems | Status | Source |
|------|---------|--------|--------|
| references/params_factions_ttrpg.md | TTRPG | CURRENT | factions_ttrpg_v30.md |
| references/params_southernmost.md | TTRPG/BG | CURRENT | southernmost_v30.md + SIM-STH |
| references/params_campaign_modes.md | ALL | CURRENT | campaign_modes_v30.md |

### Skeleton/Infill Pairs (batch-created 2026-04-13)
All files below: skeleton at `_v30.md`, infill at `_v30_infill.md` in same directory.
| System | Skeleton | Infill Lines |
|--------|----------|-------------|
| threadwork | designs/ttrpg/threadwork_v30.md | 196 |
| combat | designs/combat/combat_v30.md | 86 |
| board_game | designs/board_game/board_game_v30.md | 94 |
| fieldwork | designs/fieldwork/fieldwork_v30.md | 85 |
| mass_battle | designs/mass_combat/mass_battle_v30.md | 7 |
| social_contest | designs/contest/social_contest_v30.md | 22 |
| scale_transitions | designs/hybrid/scale_transitions_v30.md | 20 |
| npc_behavior | designs/systems/npc_behavior_v30.md | 92 |
| worldbuilding | designs/worldbuilding/worldbuilding_v30.md | 25 |
| npc_roster | designs/npcs/npc_roster_v30.md | 78 |
| npc_foils | designs/npcs/npc_foils_v30.md | 91 |
| npc_character_analyses | designs/npcs/npc_character_analyses_v30.md | 85 |
| baralta_crown_claim | designs/mechanics/baralta_crown_claim_v30.md | 17 |
| conviction_track | designs/conviction_track/conviction_track_v30.md | 21 |
| geography | designs/setting/geography_v30.md | 17 |
| calamity_radiation | designs/setting/calamity_radiation_v30.md | 13 |
| character_histories | designs/characters/character_histories_v30.md | 71 |
| victory | designs/board_game/victory_v30.md | 17 |
| varfell_path_b | designs/board_game/varfell_path_b_v30.md | 8 |
| fieldwork_hybrid | designs/fieldwork/fieldwork_hybrid_v30.md | 2 |
| fieldwork_bg | designs/fieldwork/fieldwork_bg_v30.md | 4 |
| hybrid_gaps | designs/hybrid/hybrid_gaps_v30.md | 32 |
| southernmost | designs/setting/southernmost_v30.md | 35 |
| factions_ttrpg | designs/ttrpg/factions_ttrpg_v30.md | 64 |
| campaign_modes | designs/systems/campaign_modes_v30.md | 25 |

### Params History Files
| File | Status | Notes |
|------|--------|-------|
| references/params_factions_ttrpg_history.md | CURRENT | Patch history for params_factions_ttrpg.md |
| references/params_southernmost_history.md | CURRENT | Patch history incl PP-643 |
| references/params_campaign_modes_history.md | CURRENT | Patch history (procedural) |
