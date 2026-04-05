# VALORIA REPOSITORY FILE INDEX
## Last updated: 2026-04-03
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
| canon/editorial_ledger.yaml | ALL | CURRENT | Source of truth for editorial decisions. 186 items as of 2026-04-04. |
| canon/patch_register.yaml | ALL | CURRENT | All patches PP-001–PP-400. De-collided 2026-04-04 (104 renumbered entries). PP-086–092 filled 2026-04-02. |

---


> **Note (2026-04-04):** ALL compilation/v0.14 stage documents are OUTDATED. Design docs in designs/ and params files in references/ are canonical. See canonical_sources.yaml.

## COMPILATION v0.14 (current checkpoint)

| File | Systems | Status | Depends On | Referenced By |
|------|---------|--------|------------|---------------|
| compilation/v0.14/stage1_core_engine.md | ALL | OUTDATED | 00_philosophical_foundations | references/params_core.md |
| compilation/v0.14/stage2_characters.md | TTRPG/HYBRID | OUTDATED | stage1 | — |
| compilation/v0.14/stage3_thread_operations.md | TTRPG/HYBRID | STALE | designs/ttrpg/threadwork_redesign_v25.md | — |
| compilation/v0.14/stage4_southernmost.md | TTRPG/HYBRID | OUTDATED | stage3 | — |
| compilation/v0.14/stage5_clocks.md | ALL | OUTDATED | stage1 | mass_battle_v3 (Coherence ref) |
| compilation/v0.14/stage6_factions.md | TTRPG | STALE | — | references/params_factions.md (TTRPG col); NOTE: BG faction mechanics superseded by bg_v05 |
| compilation/v0.14/stage7_territories.md | ALL | OUTDATED | stage6 | — |
| compilation/v0.14/stage8_combat.md | ALL | OUTDATED | stage1, stage2 | references/params_combat.md, references/params_mass_combat.md; PP-086–092 applied 2026-04-02 |
| compilation/v0.14/stage9_social.md | TTRPG | STALE | — | NOTE: debate_system_redesign_v1.md is the operative design. stage9 is empty. |
| compilation/v0.14/stage10_advancement.md | TTRPG | OUTDATED | stage2 | — |
| compilation/v0.14/stage11_scale_transitions.md | HYBRID | OUTDATED | stage1–8 | references/params_scale_transitions.md; PP-089/PP-090 PENDING application |
| compilation/v0.14/stage12_campaign_modes.md | ALL | OUTDATED | stage1–11 | — |
| compilation/v0.14/stage13_npcs.md | ALL | OUTDATED | stage2, stage6 | GAP: Focus+Attunement values missing from Non-Player Character profiles (GAP-ARC31-SIM-01) |
| compilation/v0.14/stage14_gm_tools.md | ALL | OUTDATED | all stages | — |
| compilation/v0.14/stage15_spell_catalog.md | TTRPG | OUTDATED | stage3 | threadwork_redesign_v25 (W-series ops) |
| compilation/v0.14/stage16_reference.md | ALL | OUTDATED | all stages | — |
| compilation/v0.14/stage17_canon_guard.md | ALL | OUTDATED | 00_philosophical_foundations | — |
| compilation/v0.14/stage3_compilation_report.md | INFRA | OUTDATED | — | — |
| compilation/v0.14/stage_bg_board_game_mode.md | BG | STALE | designs/board_game/valoria_bg_v05_simulation_and_patches.md | NOTE: BG v05 is canonical for BG mode. This stage file is behind. ED-001 (Card-Hand) BLOCKER. |
| compilation/v0.14/valoria_ruleset_v0.14.md | ALL | CURRENT | all stages | — |

---

## DESIGNS — BOARD GAME

| File | Systems | Status | Depends On | Notes |
|------|---------|--------|------------|-------|
| designs/board_game/bg_consolidated_synthesis.md | BG | SUPERSEDED | — | Superseded by bg_v05 |
| designs/board_game/bg_improvement_v1.md | BG | SUPERSEDED | — | — |
| designs/board_game/bg_improvement_v2.md | BG | SUPERSEDED | — | — |
| designs/board_game/bg_improvement_v3.md | BG | SUPERSEDED | — | — |
| designs/board_game/bg_improvement_v3_amendment2.md | BG | SUPERSEDED | — | — |
| designs/board_game/bg_improvement_v4.md | BG | SUPERSEDED | — | — |
| designs/board_game/bg_improvement_review.md | BG | SUPERSEDED | — | — |
| designs/board_game/bg_proposal_critical_review.md | BG | SUPERSEDED | — | — |
| designs/board_game/bg_synthesis.md | BG | SUPERSEDED | — | — |
| designs/board_game/bg_synthesis_amendment_1.md | BG | SUPERSEDED | — | — |
| designs/board_game/stage_bg_proposal.md | BG | SUPERSEDED | — | — |
| designs/board_game/stage_bg_proposal_v02.md | BG | SUPERSEDED | — | — |
| designs/board_game/valoria_bg_v01.md | BG | SUPERSEDED | — | — |
| designs/board_game/valoria_bg_v02.md | BG | SUPERSEDED | — | — |
| designs/board_game/valoria_bg_v02_sim_report.md | BG | SUPERSEDED | — | — |
| designs/board_game/valoria_bg_v03_part1.md | BG | SUPERSEDED | — | — |
| designs/board_game/valoria_bg_v03_part2.md | BG | SUPERSEDED | — | — |
| designs/board_game/valoria_bg_v03_part3.md | BG | SUPERSEDED | — | — |
| designs/board_game/valoria_bg_v04.md | BG | SUPERSEDED | — | — |
| **designs/board_game/valoria_bg_v05_simulation_and_patches.md** | **BG/HYBRID** | **CURRENT** | stage8, stage6, threadwork_v25 | **Canonical BG faction mechanics. P-12–P-32 applied. ST-BG/INT patches added 2026-04-02.** |
| designs/board_game/valoria_bg_v05_stress_test_report.md | BG/HYBRID | CURRENT | bg_v05 | Source for ST-BG-01–13, ST-MB-01–10, ST-INT-01–13 patches |

---

## DESIGNS — MASS COMBAT

| File | Systems | Status | Depends On | Notes |
|------|---------|--------|------------|-------|
| **designs/combat/combat_design_v1.md** | **ALL** | **CURRENT** | stage1, stage2, mass_battle_v3 | **NEW 2026-04-02. Working combat design with three-mode framing. Replaces stage8 as design-layer source. PP-086–092 incorporated.** |

| **designs/mass_combat/mass_battle_v3.md** | **ALL** | **CURRENT** | stage8_combat, threadwork_v25 | **Operative mass battle spec. ST-MB patches added 2026-04-02. ST-MB-02 (Coherence) CRITICAL GAP.** |

---

## DESIGNS — DEBATE

| File | Systems | Status | Depends On | Notes |
|------|---------|--------|------------|-------|
| designs/debate/debate_example_v1.md | TTRPG/HYBRID | CURRENT | debate_system_redesign_v1 | Example scenario |
| **designs/debate/debate_system_redesign_v1.md** | **TTRPG/HYBRID** | **CURRENT** | stage1, stage9 | **Operative debate spec. Part 6 (compiled mechanics) added 2026-04-02 from v1+v2 stress tests.** |
| designs/debate/debate_stress_test_v1.md | TTRPG | CURRENT | debate_system_redesign_v1 | Source for D-01–D-10, R-01–R-07 patches |
| designs/debate/debate_stress_test_v2.md | TTRPG | CURRENT | debate_system_redesign_v1 | Source for v2-P01–v2-P04 patches |

---

## DESIGNS — TTRPG (Threadwork)

| File | Systems | Status | Depends On | Notes |
|------|---------|--------|------------|-------|
| **designs/ttrpg/threadwork_redesign_v25.md** | **TTRPG/HYBRID/BG** | **CURRENT** | 00_philosophical_foundations, stage3 | **Operative threadwork spec. Mode index added 2026-04-02. ST-TW patches added.** |
| designs/ttrpg/SUPERSEDED.md | INFRA | CURRENT | — | Marks older design files |
| designs/ttrpg/batch_a_designs.md | TTRPG | CURRENT | — | Design batch |
| designs/ttrpg/batch_ad_resolutions.md | TTRPG | CURRENT | — | — |
| designs/ttrpg/batch_bc_designs.md | TTRPG | CURRENT | — | — |
| designs/ttrpg/batch_d_designs.md | TTRPG | CURRENT | — | — |
| designs/ttrpg/batch_e_designs.md | TTRPG | CURRENT | — | — |
| designs/ttrpg/batch_f_designs.md | TTRPG | CURRENT | — | — |
| designs/ttrpg/church_territorial_seizure.md | TTRPG/BG | CURRENT | stage6, stage7 | — |
| designs/ttrpg/edeyja_npc.md | TTRPG | CURRENT | stage13 | — |
| designs/ttrpg/generation_tasks_gt01_gt02_gt03.md | TTRPG | CURRENT | — | — |
| designs/ttrpg/lowenritter_faction_card.md | BG | CURRENT | bg_v05 | — |
| designs/ttrpg/mechanical_tasks_and_patches.md | TTRPG | CURRENT | — | — |
| designs/ttrpg/succession_mechanic.md | ALL | CURRENT | stage6 | — |
| designs/ttrpg/valoria_emergent_scenarios.md | TTRPG | CURRENT | stage12 | — |
| designs/ttrpg/valoria_narrative_scenario_chains.md | TTRPG | CURRENT | stage12 | — |

---

## DESIGNS — HYBRID

| File | Systems | Status | Notes |
|------|---------|--------|-------|
| designs/hybrid/hybrid_gaps_resolved.md | HYBRID | CURRENT | Resolved hybrid design gaps |

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
| designs/gm_ref_cp14/arcs/arcs_31_35_hybrid_systems.md | HYBRID | CURRENT | Arcs 31–35 (generated 2026-04-01). Arcs 32, 34, 35 NOT YET SIMULATED. |
| designs/gm_ref_cp14/arcs/valoria_emergent_arcs_experimental.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/arcs/valoria_emergent_campaign_arcs.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d01_cascade_consequence_reference.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d02_seasonal_accounting_form.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d03_gm_dashboard.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d04_gap_escalation_table.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d05_coherence_band_track.md | TTRPG | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d06_thread_operation_resolution_card.md | TTRPG | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d07_npc_state_cards.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d08_knot_registry_template.md | TTRPG | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d09_comovement_matrix_skeleton.md | ALL | CURRENT | — |
| designs/gm_ref_cp14/dashboards/d10_framing_process_skeleton.md | ALL | CURRENT | — |

---

## REFERENCES (parameter files — extracted mechanical values for sim/audit use)

| File | Systems | Status | Source Document | Stale Flags |
|------|---------|--------|-----------------|-------------|
| references/params_core.md | ALL | CURRENT | stage1_core_engine.md | — |
| references/params_combat.md | ALL | CURRENT | stage8_combat.md | PP-086–092 applied to stage8; params_combat not yet synced |
| references/params_mass_combat.md | ALL | CURRENT | stage8 + mass_battle_v3 | ST-MB patches applied to mass_battle_v3; params not yet synced |
| references/params_factions.md | ALL | CURRENT | stage6 (TTRPG) + bg_v05 (BG) | — |
| references/params_board_game.md | BG | CURRENT | bg_v05_simulation_and_patches.md | ST-BG patches applied; params not yet synced |
| references/params_debate.md | TTRPG/HYBRID | CURRENT | debate_system_redesign_v1.md | Part 6 (compiled mechanics) added; params not yet synced |
| references/params_threadwork.md | TTRPG/HYBRID | CURRENT | threadwork_redesign_v25.md | ST-TW patches applied; params not yet synced |
| references/params_scale_transitions.md | HYBRID | CURRENT | stage11_scale_transitions.md | PP-089/PP-090 PENDING |
| references/glossary.md | ALL | CURRENT | — | Canonical term expansion reference. Update on every commit introducing a new term. |
| references/D10_INTEGRATION_GUIDE.md | ALL | CURRENT | — | — |
| references/d10_success_probabilities.json | ALL | CURRENT | — | — |

---

## SKILLS

| File | Systems | Status | Uses Params? | Notes |
|------|---------|--------|--------------|-------|
| skills/valoria-orchestrator/SKILL.md | INFRA | CURRENT | No | Session management. Dir-based (canonical). |
| skills/valoria-orchestrator-SKILL.md | INFRA | STALE | No | Flat file — older stub. Use dir-based version. |
| skills/valoria-orchestrator/references/commit_convention.md | INFRA | CURRENT | — | — |
| skills/valoria-orchestrator/references/github_pat.md | INFRA | CURRENT | — | — |
| skills/valoria-orchestrator/references/model_routing_table.md | INFRA | CURRENT | — | — |
| skills/valoria-orchestrator/references/session_protocol.md | INFRA | CURRENT | — | — |
| skills/valoria-orchestrator/references/skill_registry.md | INFRA | CURRENT | — | — |
| skills/valoria-orchestrator/scripts/github_ops.py | INFRA | CURRENT | — | GraphQL batch reader added 2026-04-02 |
| skills/valoria-canon-guard-SKILL.md | INFRA | STALE | No | Flat file — use dir-based when available |
| skills/valoria-chunker-SKILL.md | INFRA | STALE | No | Flat file |
| skills/valoria-mechanic-audit-SKILL.md | INFRA | CURRENT | Yes (all params) | Correctly references params |
| skills/valoria-simulator-SKILL.md | INFRA | CURRENT | Yes (all params) | Correctly references params |
| skills/valoria-compiler-SKILL.md | INFRA | CURRENT | No | — |
| skills/valoria-editorial-register/SKILL.md | INFRA | CURRENT | No | Updated 2026-04-01 |
| skills/valoria-arc-generator/SKILL.md | INFRA | CURRENT | No | — |
| skills/valoria-combat-simulator/SKILL.md | INFRA | CURRENT | Own params | Uses references/combat_params.md (separate from main params) |
| skills/valoria-combat-simulator/references/combat_params.md | INFRA | CURRENT | — | Separate from references/params_combat.md |
| skills/valoria-dice-model/SKILL.md | INFRA | CURRENT | No | — |

---

## TESTS (simulation outputs)

| File | Systems | Patches Produced | Status |
|------|---------|-----------------|--------|
| tests/coverage_matrix.md | ALL | — | CURRENT |
| tests/sim_cascade_01.md | BG | — | CURRENT |
| tests/sim_combat_batch_11.md | ALL | PP-086–092 | CURRENT |
| tests/sim_mass_battle_batch_11.md | ALL | PP-086–092 (validated) | CURRENT |
| tests/sim_thread_batch_01–08.md | TTRPG | Various | CURRENT |
| tests/sim_ttrpg_batch_02–10.md | TTRPG | Various | CURRENT |
| tests/sim_ttrpg_batch_r01–r07.md | TTRPG | Various | CURRENT |
| tests/sim_ttrpg_batch_sonnet46.md | TTRPG | — | CURRENT |
| tests/sim_x_01_combat_thread.md | TTRPG | ST-TW-01,04 | CURRENT |
| tests/sim_x_02_debate_thread.md | TTRPG | — | CURRENT |
| tests/sim_x_03_massbattle_thread.md | ALL | ST-TW-02,03 | CURRENT |
| tests/sim_x_04_massbattle_personal.md | ALL | — | CURRENT |
| tests/sim_x_05_debate_thread_npcs.md | TTRPG | — | CURRENT |
| tests/sim_x_06_combat_wounds_npcs.md | TTRPG | F-23–25 (confirmed) | CURRENT |
| tests/sim_x_07_massbattle_npcs_thread.md | ALL | — | CURRENT |
| tests/sim_x_08_seasonal_cascade.md | ALL | — | CURRENT |
| tests/sim_x_09_vaynard_almud_zoom.md | TTRPG | — | CURRENT |
| tests/sim_x_10_doctrine_evidence_tc.md | ALL | — | CURRENT |
| tests/sim_x_11_maret_infiltration_zoom.md | TTRPG | — | CURRENT |
| tests/sim_x_12_three_season_cascade.md | ALL | — | CURRENT |
| tests/sim_x_13_pulling_dissolution.md | TTRPG | — | CURRENT |
| tests/sim_x_14_mode2_entity_political.md | ALL | — | CURRENT |
| tests/sim_x_15_knot_crisis_klapp.md | ALL | — | CURRENT |
| tests/sim_x_16_collective_weave.md | TTRPG | — | CURRENT |
| tests/simulation_report_arcs_31_33.md | HYBRID | PP-159–163 | CURRENT |

---

## TOOLS

| tools/patch_propagation_checker.py | ALL | TOOL | CURRENT | canon/patch_register.yaml | references/params_*.md | Validates patches propagated to params headers |

| File | Purpose | Status |
|------|---------|--------|
| tools/coverage_matrix.py | Track simulation coverage | CURRENT |
| tools/find_references.py | Find cross-references between files | CURRENT |
| tools/github_ops.py | GitHub REST/GraphQL operations | CURRENT |
| tools/model_router.html | Model routing reference | CURRENT |
| tools/propagator.py | Propagate patches to dependent files | CURRENT |
| tools/verify_cuts.py | Verify patch cuts are applied | CURRENT |

---

## KNOWN STALE / SYNC GAPS

The following params files are behind their source documents after this session's patches:

| Params File | Source That Changed | What Changed |
|-------------|--------------------|--------------| 
| compilation/v0.14/stage8_combat.md | PP-089, PP-090 | PENDING — belong in stage11_scale_transitions.md |
| compilation/v0.14/stage3_thread_operations.md | threadwork_redesign_v25.md | Entire stage3 needs rewrite from v25 design |
| compilation/v0.14/stage9_social.md | debate_system_redesign_v1.md | Entire stage9 needs rewrite from Part 6 compiled spec |
| compilation/v0.14/stage_bg_board_game_mode.md | bg_v05_simulation_and_patches.md | ED-001 (Card-Hand) BLOCKER prevents full sync |

*Resolved 2026-04-02: params_combat, params_mass_combat, params_board_game, params_debate, params_threadwork — all synced with ST patch summaries.*

---

## DEPRECATED

Files in `deprecated/` are not in active use. Do not reference in new design work.

---

*Index maintained by valoria-orchestrator. Update this file in the same commit as any file that changes its status, system classification, or dependency relationships.*

---

## PROPAGATION-PENDING: APPROVED DECISIONS NOT YET IN WORKING FILES

These files contain confirmed design decisions that have not been propagated to the appropriate working design documents.

| File | Decisions Pending Propagation | Target Files |
|------|-------------------------------|--------------|
| designs/ttrpg/batch_ad_resolutions.md | G-053 (Approach Training 8CP), G-040 (Inspiration half-CP refund), G-054 (Circles single track confirmed), G-042 (No CP for faction founding), G-038 (Treaty betrayal table — **no home file yet**), G-044 (Altonian vassalage spec — **not yet designed**), Varfell collection transfer | threadwork_v25 (G-053), stage2/characters (G-040), faction design files (G-038, G-044) |
| designs/ttrpg/succession_mechanic.md | Almud succession mechanic — approved, no working design file | Needs: designs/ttrpg/political_mechanics.md or similar |
| designs/ttrpg/church_territorial_seizure.md | Theocracy Counter 80 per-territory roll — approved, integrates with G-050 | bg_v05 (Theocracy Counter 80 section already has this; verify parity) |
| designs/hybrid/hybrid_gaps_resolved.md | 17 hybrid gaps resolved — ready for integration | stage11_scale_transitions, bg_v05 §B.5, designs/hybrid/ |
| designs/ttrpg/generation_tasks_gt01_gt02_gt03.md | Status: "requires user review" — not integrated | Pending user review before any propagation |
| designs/ttrpg/mechanical_tasks_and_patches.md | R-54–R-68 applied to threadwork_v25 ✓; MT-01 applied to combat_design_v1 ✓; R-65/R-66 blocked by ED-047 | stage15_spell_catalog (R-55,56,59,60,62,63,64); stage5_clocks (R-68) |

## DESIGNS/ FILES — STATUS SUMMARY

| File | Status | Notes |
|------|--------|-------|
| designs/ttrpg/SUPERSEDED.md | INFRA | Marks superseded files |
| designs/ttrpg/batch_a_designs.md | REFERENCE | Session 4 gap designs — review if gaps are still open |
| designs/ttrpg/batch_bc_designs.md | REFERENCE | Session 4 military+political gap designs |
| designs/ttrpg/batch_d_designs.md | REFERENCE | Session 4 faction identity packages |
| designs/ttrpg/batch_e_designs.md | REFERENCE | Session 5 BG design briefs — mostly in bg_v05 |
| designs/ttrpg/batch_f_designs.md | REFERENCE | Session 5 hybrid+endgame — check against hybrid_gaps_resolved |
| designs/ttrpg/batch_ad_resolutions.md | PROPAGATION-PENDING | See table above |
| designs/ttrpg/generation_tasks_gt01_gt02_gt03.md | AWAITING USER REVIEW | Do not propagate without user sign-off |
| designs/ttrpg/edeyja_npc.md | WORKING | Canonical Non-Player Character (name working, ED-048 adjacent). In stage13. |
| designs/ttrpg/lowenritter_faction_card.md | WORKING | Approved. Verify parity with bg_v05 faction section. |
| designs/ttrpg/succession_mechanic.md | PROPAGATION-PENDING | Approved. No home in working design files yet. |
| designs/ttrpg/church_territorial_seizure.md | VERIFY | Approved. Check parity with bg_v05 Theocracy Counter 80 section. |
| designs/ttrpg/valoria_emergent_scenarios.md | WORKING | Emergent scenario map vs compiled ruleset. |
| designs/ttrpg/valoria_narrative_scenario_chains.md | WORKING | Non-Player Character arcs. Note: contains "Ceiral" references (ED-048). |
| designs/hybrid/hybrid_gaps_resolved.md | PROPAGATION-PENDING | 17 gaps resolved. Not yet integrated into stage11 or bg_v05. |
| designs/gm_ref_cp14/* | WORKING | All arc and dashboard files. Arcs 32,34,35 not yet simulated. |


## SKELETON-DEBT REGISTER (documents with non-skeleton content to clean up)

| File | Issue | Priority |
|------|-------|----------|
| ~~`designs/board_game/valoria_bg_v05_simulation_and_patches.md`~~ | DONE — v0.6 final committed 2026-04-02 (P-12–P-32 + ST-BG/INT all in-place) | ✓ |
| ~~`designs/ttrpg/threadwork_redesign_v25.md`~~ | DONE — v3.0 committed 2026-04-02. Part 1 → threadwork_philosophical_reference.md | ✓ |
| `compilation/v0.14/stage8_combat.md` | Part Eleven appended (PP-086–092). Apply in-place. Lower priority — compilation layer. | Low |
| `compilation/v0.14/stage11_scale_transitions.md` | §11.8 appended (PP-089/090). Apply in-place. | Low |


**Skeleton-debt fully cleared as of 2026-04-02.** All design and compilation documents apply patches in-place. No appendix sections remain in any working file.


**Skeleton-debt fully and definitively cleared as of 2026-04-02.** Zero appendix sections in any working document.

| designs/contest/social_contest_system_v2.md | ALL | DESIGN | CURRENT | canon/00_philosophical_foundations.md, canon/02_canon_constraints.md | references/params_contest.md | PP-234. Supersedes debate_system_redesign_v1 Part 6. |
| references/params_contest.md | ALL | REF | CURRENT | designs/contest/social_contest_system_v2.md | — | PP-234. Supersedes params_debate.md. |
