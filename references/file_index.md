# VALORIA REPOSITORY FILE INDEX
## Last updated: 2026-04-09
## Purpose: Single-source map of every committed file → game system → status
## Maintained by: valoria-orchestrator skill (update on every commit that adds/modifies a file)
## Format: path | systems | type | status | depends_on | referenced_by
## Three-mode framing: ALL systems stated as TTRPG baseline → Hybrid → Board Game.
## TTRPG = source layer. Hybrid = bridge. Board Game = abstraction. designs/ = working layer. compilation/ = snapshot.

---

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
| canon/patch_register.yaml | ALL | CURRENT | All patches PP-001 onwards |

---

## COMPILATION v0.14 (DEPRECATED — all stages outdated as of 2026-04-09)

> **All compilation/v0.14 stage documents are DEPRECATED.** Design docs in designs/ and params files in references/ are canonical. See canonical_sources.yaml. Each stage file now has a DEPRECATED header naming its replacement.

| File | Systems | Status | Canonical Replacement |
|------|---------|--------|----------------------|
| compilation/v0.14/stage1_core_engine.md | ALL | DEPRECATED | references/params_core.md |
| compilation/v0.14/stage2_characters.md | TTRPG/HYBRID | DEPRECATED | references/params_core.md |
| compilation/v0.14/stage3_thread_operations.md | TTRPG/HYBRID | DEPRECATED | designs/ttrpg/threadwork_redesign_v25.md |
| compilation/v0.14/stage3_compilation_report.md | INFRA | DEPRECATED | Process artifact |
| compilation/v0.14/stage4_southernmost.md | TTRPG/HYBRID | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage5_clocks.md | ALL | DEPRECATED | designs/systems/clock_registry.md |
| compilation/v0.14/stage6_factions.md | TTRPG | DEPRECATED | BG/Hybrid: bg_v05. TTRPG: no replacement — unverified |
| compilation/v0.14/stage7_territories.md | ALL | DEPRECATED | designs/setting/geography_design.md |
| compilation/v0.14/stage8_combat.md | ALL | DEPRECATED | designs/combat/combat_design_v1.md |
| compilation/v0.14/stage9_social.md | TTRPG | DEPRECATED | designs/contest/social_contest_system_v2.md |
| compilation/v0.14/stage10_advancement.md | TTRPG | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage11_scale_transitions.md | HYBRID | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage12_campaign_modes.md | ALL | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage13_npcs.md | ALL | DEPRECATED | designs/npcs/npc_roster.md (partial) |
| compilation/v0.14/stage14_gm_tools.md | ALL | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage15_spell_catalog.md | TTRPG | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage16_reference.md | ALL | DEPRECATED | No design-layer replacement — unverified |
| compilation/v0.14/stage17_canon_guard.md | ALL | DEPRECATED | skills/valoria-canon-guard/SKILL.md |
| compilation/v0.14/stage_bg_board_game_mode.md | BG | DEPRECATED | designs/board_game/valoria_bg_v05_simulation_and_patches.md |
| compilation/v0.14/valoria_ruleset_v0.14.md | ALL | DEPRECATED | Compilation snapshot — all stages outdated |

---

## DESIGNS — BOARD GAME

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| **designs/board_game/valoria_bg_v05_simulation_and_patches.md** | **BG/HYBRID** | **CURRENT** | Canonical BG faction mechanics. P-12–P-32 applied. |
| designs/board_game/valoria_bg_v05_stress_test_report.md | BG/HYBRID | CURRENT | Source for ST-BG/MB/INT patches |
| designs/board_game/victory_architecture_v1.md | BG/ALL | CURRENT | Canonical victory conditions. PP-406–PP-427. |
| designs/board_game/faction_resolutions_2026_04_07.md | BG/ALL | CURRENT | PP-428 onwards. Active. |
| designs/board_game/varfell_path_b_redesign_ed311.md | BG | AWAITING REVIEW | ED-311 |
| designs/board_game/valoria_map_v2.svg | BG | CURRENT | Visual map |
| ~~19 superseded BG files~~ | — | DEPRECATED | Moved to deprecated/designs/board_game/ (2026-04-09) |

---

## DESIGNS — COMBAT

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| **designs/combat/combat_design_v1.md** | **ALL** | **CURRENT** | Canonical combat design. PP-086–092+. |

---

## DESIGNS — MASS COMBAT

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| **designs/mass_combat/mass_battle_v3.md** | **ALL** | **CURRENT** | Canonical mass battle spec. ST-MB patches. |

---

## DESIGNS — CONTEST (Social/Debate)

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| **designs/contest/social_contest_system_v2.md** | **ALL** | **CURRENT** | Canonical social contest. PP-234. Supersedes debate_system_redesign_v1. |
| ~~designs/debate/*~~ | — | DEPRECATED | Moved to deprecated/ (2026-04-09). Superseded by contest system. |

---

## DESIGNS — TTRPG (Threadwork & Mechanics)

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| **designs/ttrpg/threadwork_redesign_v25.md** | **TTRPG/HYBRID/BG** | **CURRENT** | Canonical threadwork spec. |
| designs/ttrpg/threadwork_philosophical_reference.md | TTRPG | REFERENCE | Extracted from threadwork v25 Part 1 |
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
| designs/ttrpg/SUPERSEDED.md | INFRA | CURRENT | Notice file for Phase 1 artifacts |

---

## DESIGNS — HYBRID

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/hybrid/hybrid_gaps_resolved.md | HYBRID | PROPAGATION-PENDING | 17 gaps resolved. Not yet in stage11 or bg_v05. |

---

## DESIGNS — CONVICTION TRACK

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/conviction_track/opus_design_proposal.md | BG/ALL | WORKING | PP-406–PP-418 design proposal. NOT committed as patches. |

---

## DESIGNS — SETTING

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/setting/geography_design.md | ALL | CURRENT | Canonical geography. 17 territories. |
| designs/setting/calamity_radiation.md | ALL | CURRENT | Calamity radiation framework. |
| designs/setting/adjacency_map.jsx | ALL | CURRENT | Visual adjacency tool |

---

## DESIGNS — SYSTEMS

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/systems/clock_registry.md | ALL | CURRENT | Unified clock/track registry. PP-496. |

---

## DESIGNS — NPCs

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/npcs/npc_roster.md | ALL | CURRENT | 13-character roster. ED-358. |

---

## DESIGNS — WORLDBUILDING

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/worldbuilding/worldbuilding_integration_v3.md | ALL | CURRENT | Latest worldbuilding integration |
| designs/worldbuilding/worldbuilding_v3_canon_audit.md | ALL | CURRENT | Audit of v3 |
| designs/worldbuilding/editorial_comprehensive_review.md | ALL | CURRENT | Comprehensive editorial review |
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
| designs/gm_ref_cp14/gm_reference_workplan.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_01_04_rebuilt.md | ALL | CURRENT | Campaign arcs 1–4 |
| designs/gm_ref_cp14/arcs/arcs_05_08_rebuilt.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_09_11_elske_baralta.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_12_15_faction_transitions.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_16_19_faction_domain_echoes.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_20_23_branching.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_24_27_branching.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_28_30_coherence_zero.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/arcs_31_35_hybrid_systems.md | HYBRID | CURRENT | Arcs 32, 34, 35 NOT YET SIMULATED. |
| designs/gm_ref_cp14/arcs/valoria_emergent_arcs_experimental.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/valoria_emergent_campaign_arcs.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d01–d10 | ALL | CURRENT | All 10 dashboard files |
| designs/gm_ref_cp14/flowcharts/flowchart_templar_crossing.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/zoom_in_out_reference_card.md | ALL | CURRENT | — |

---

| designs/npcs/npc_roster_caste_annotations.md | ALL | CURRENT | Caste-axis impact on all 13 roster NPCs |
| designs/npcs/ed_403_406_407_resolutions.md | ALL | CURRENT | RM split, Ehrenwall assessment, consecration crisis |

## DESIGNS — MECHANICS
| designs/mechanics/baralta_crown_claim_mechanic.md | BG/HYBRID | CURRENT | Crown Succession Contest, Stake Claim DA, consecration crisis BG expression |
| designs/npcs/lenneth_threadwork_design.md | ALL | CURRENT | Lenneth stat block, TS development, Cultural Revival Track, threadwork at ruler diamond decision points |

## GM REFERENCE (gm_ref/)

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| gm_ref/arcs_01_04_nongreedy.md | ALL | CURRENT | Batch 01 arcs |
| gm_ref/arcs_05_09_batch02.md | ALL | CURRENT | Batch 02 arcs |
| gm_ref/arcs_10_18_consolidated.md | ALL | CURRENT | Batch 03 consolidated |
| ~~4 deprecated arc revision files~~ | — | DEPRECATED | Moved to deprecated/gm_ref/ (2026-04-09) |
| ~~gm_ref/debate_ref_card_v1.md~~ | — | DEPRECATED | Moved to deprecated/ — superseded by contest system |

---

## REFERENCES (parameter files)

| File | Systems | Status | Source Document |
|------|---------|--------|----------------|
| references/params_core.md | ALL | CURRENT | stage1 (legacy source) |
| references/params_combat.md | ALL | CURRENT | combat_design_v1.md |
| references/params_mass_combat.md | ALL | CURRENT | mass_battle_v3.md |
| references/params_factions.md | ALL | CURRENT | stage6 (TTRPG) + bg_v05 (BG) |
| references/params_board_game.md | BG | CURRENT | bg_v05 |
| references/params_contest.md | ALL | CURRENT | social_contest_system_v2.md |
| references/params_threadwork.md | TTRPG/HYBRID | CURRENT | threadwork_redesign_v25.md |
| references/params_scale_transitions.md | HYBRID | CURRENT | stage11 (legacy source) |
| references/params_core_history.md | ALL | CURRENT | Patch history |
| references/params_combat_history.md | ALL | CURRENT | Patch history |
| references/params_mass_combat_history.md | ALL | CURRENT | Patch history |
| references/params_board_game_history.md | BG | CURRENT | Patch history |
| references/params_threadwork_history.md | TTRPG/HYBRID | CURRENT | Patch history |
| references/glossary.md | ALL | CURRENT | Term expansion reference |
| references/canonical_sources.yaml | ALL | CURRENT | System authority map |
| references/file_index.md | ALL | CURRENT | This file |
| references/arc_register.md | ALL | CURRENT | 73 arcs + 7 collisions. Principal/secondary/tertiary. All NPCs mapped. v7. |
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
| tools/github_ops.py | GitHub operations | CURRENT |
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
| designs/hybrid/hybrid_gaps_resolved.md | 17 hybrid gaps | stage11, bg_v05 §B.5 |
| designs/ttrpg/mechanical_tasks_and_patches.md | R-65/R-66 blocked by ED-047 | stage15, stage5 |

---

*Index maintained by valoria-orchestrator. Update this file in the same commit as any file that changes its status, system classification, or dependency relationships.*
