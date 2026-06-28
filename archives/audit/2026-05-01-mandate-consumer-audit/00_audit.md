<!-- [PROVISIONAL: 2026-05-01 — Mandate-consumer audit per faction_behavior_v30 §6.2 Stage 7] -->
<!-- STATUS: PROVISIONAL — Class B mechanical audit. Identifies Mandate reads across the corpus and classifies each as Legitimacy-leaning / Popular-Support-leaning / mode-neutral. Refactor recommendations per tier. -->
<!-- AUTHORITY: PP-686 v2 §4 (Mandate retention as derived); §6.2 Stage 7 -->

# Mandate-Consumer Audit (PP-686 v2 Phase B Stage 7)

## §1 Purpose

PP-686 v2 §4 retains `Mandate = round(0.5 × Legitimacy + 0.5 × Popular_Support)` as a derived value for backward compatibility. Existing consumers continue to function; refactor to read Legitimacy or Popular_Support directly is **opportunistic, not required**.

This audit:
1. Catalogs every Mandate read across the canonical corpus.
2. Classifies each read by dominant semantic (L-leaning / PS-leaning / mode-neutral / undecided).
3. Tiers files for refactor priority.
4. Establishes the no-refactor-required baseline.

## §2 Methodology

- **Corpus scanned:** 627 files across `params/`, `designs/`, `canon/`, `references/`. Excludes archive folders, audit folders, sims, tests.
- **Pattern:** literal `Mandate` (case-sensitive) word match per line.
- **Classification heuristic:**
  - **L (Legitimacy):** linguistic signals of institutional acceptance, formal authority, procedural legitimacy, ecclesiastical recognition, official decree, succession, treaty.
  - **PS (Popular Support):** linguistic signals of populace backing, rebellion, riot, mass support, public approval.
  - **BOTH:** both signal classes present in the same line; semantic genuinely combined.
  - **DERIVED (mode-neutral):** Mandate used as a generic 0–7 stat in pool/Ob/check formulas, starting values, ceilings/floors, ±1 modifiers — no semantic preference between L and PS.
  - **UNCLASSIFIED:** no decisive linguistic signal; treat as DERIVED unless designer review flags otherwise.

Heuristic is intentionally conservative — UNCLASSIFIED defaults to DERIVED (no refactor needed), so the heuristic biases against false-positive refactor flags.

## §3 Aggregate Statistics

- **Files with Mandate references:** 124 of 627 scanned (~20%).
- **Total Mandate-mentioning lines:** 530.
- **Classification distribution:**
  - L (Legitimacy-leaning): 124 lines (23%)
  - PS (Popular-Support-leaning): 4 lines (0%)
  - BOTH: 11 lines (2%)
  - DERIVED (mode-neutral): 175 lines (33%)
  - UNCLASSIFIED: 216 lines (40%)
- **Dominant-tier file counts:**
  - L-dominant: 46 files
  - PS-dominant: 1 files
  - BOTH-dominant: 3 files
  - DERIVED-dominant: 54 files
  - UNCLASSIFIED-dominant: 20 files

## §4 Conclusion: NO IMMEDIATE REFACTOR REQUIRED

DERIVED + UNCLASSIFIED + BOTH = 402 lines (75%) operate correctly via the §4 derivation `Mandate = round(0.5 × L + 0.5 × PS)`. They do not need refactor.

L-leaning lines (124, 23%) and PS-leaning lines (4) **also work via derivation**, but their semantic precision improves if eventually refactored to read L or PS directly. Refactor is opportunistic; recommended timing is "next time the file is touched for other reasons."

## §5 Tier 1 — L-Dominant Files (Opportunistic Refactor)

46 files where Mandate is read primarily for institutional / formal / legitimacy-bearing semantics. Refactor recommendation: when next editing the file, consider replacing `Mandate` reads with `Legitimacy` reads where the line carries L-semantic.

| File | Total | Breakdown |
|---|---:|---|
| `designs/architecture/campaign_modes_v30.md` | 3 | L:2 PS:0 BOTH:0 D:0 U:1 |
| `designs/arcs/emergent_campaign_arcs.md` | 8 | L:3 PS:0 BOTH:0 D:1 U:4 |
| `designs/npcs/npc_behavior_v30_infill.md` | 1 | L:1 PS:0 BOTH:0 D:0 U:0 |
| `designs/npcs/npc_foils_v30.md` | 6 | L:1 PS:0 BOTH:0 D:1 U:4 |
| `designs/provincial/baralta_crown_claim_v30.md` | 19 | L:7 PS:1 BOTH:0 D:2 U:9 |
| `designs/provincial/baralta_crown_claim_v30_infill.md` | 2 | L:1 PS:0 BOTH:0 D:0 U:1 |
| `designs/provincial/faction_behavior_v30.md` | 12 | L:3 PS:1 BOTH:2 D:1 U:5 |
| `designs/provincial/faction_layer_v30_infill.md` | 4 | L:2 PS:0 BOTH:0 D:2 U:0 |
| `designs/provincial/fail_forward_pp177.md` | 4 | L:1 PS:0 BOTH:0 D:0 U:3 |
| `designs/provincial/strategic_layer_v30_index.md` | 6 | L:2 PS:0 BOTH:0 D:2 U:2 |
| `designs/provincial/strategic_layer_v30_infill.md` | 3 | L:1 PS:0 BOTH:0 D:1 U:1 |
| `designs/ui/valoria_ui_ux_supplement_derived_settlement.md` | 1 | L:1 PS:0 BOTH:0 D:0 U:0 |
| `designs/world/worldbuilding_canon_audit_v30.md` | 8 | L:2 PS:0 BOTH:0 D:2 U:4 |
| `params/bg/ed_resolutions.md` | 9 | L:3 PS:0 BOTH:0 D:1 U:5 |
| `params/bg/institutions.md` | 21 | L:9 PS:0 BOTH:0 D:8 U:4 |
| `params/bg/npc_priority_trees.md` | 5 | L:2 PS:0 BOTH:0 D:0 U:3 |
| `params/bg/npcs_special.md` | 5 | L:3 PS:0 BOTH:0 D:1 U:1 |
| `params/bg/parliament.md` | 16 | L:5 PS:0 BOTH:0 D:4 U:7 |
| `params/bg/victory.md` | 8 | L:2 PS:0 BOTH:0 D:0 U:6 |
| `params/board_game.md` | 4 | L:1 PS:0 BOTH:0 D:1 U:2 |
| `params/factions_personal.md` | 13 | L:3 PS:0 BOTH:3 D:2 U:5 |
| `params/history/board_game.md` | 3 | L:1 PS:0 BOTH:0 D:0 U:2 |
| `params/scale_transitions.md` | 3 | L:1 PS:0 BOTH:0 D:1 U:1 |
| `references/alias_registry.yaml` | 2 | L:1 PS:0 BOTH:0 D:1 U:0 |
| `references/arcs/arc_register_clocks.md` | 2 | L:2 PS:0 BOTH:0 D:0 U:0 |
| `references/arcs/arc_register_factions.md` | 17 | L:6 PS:0 BOTH:0 D:3 U:8 |
| `references/arcs/arc_register_territory.md` | 5 | L:1 PS:0 BOTH:0 D:1 U:3 |
| `references/atoms_pending/2026-04-25/_consolidated/01_throughlines_meta.md` | 4 | L:2 PS:0 BOTH:0 D:1 U:1 |
| `references/atoms_pending/2026-04-25/_consolidated/03_threadwork_design.md` | 4 | L:1 PS:0 BOTH:0 D:1 U:2 |
| `references/atoms_pending/2026-04-25/_consolidated/06_mechanical_review_audit.md` | 5 | L:1 PS:0 BOTH:0 D:1 U:3 |
| `references/atoms_pending/2026-04-25/_consolidated/08_session_consolidation.md` | 1 | L:1 PS:0 BOTH:0 D:0 U:0 |
| `references/atoms_pending/2026-04-25/_reviews/05_v2_historicity_correction_review.md` | 1 | L:1 PS:0 BOTH:0 D:0 U:0 |
| `references/atoms_pending/2026-04-25/_reviews/06_mechanical_review_audit_review.md` | 2 | L:1 PS:0 BOTH:1 D:0 U:0 |
| `references/atoms_pending/2026-04-25/_reviews/10_session_log_index_review.md` | 2 | L:1 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/master_document_2026-04-25/15__2-3-critical-findings-beyond-audit-sim-revealed.md` | 2 | L:1 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/master_document_2026-04-25/49__8-9-faction-balance-simulation-work-remains-valid-.md` | 1 | L:1 PS:0 BOTH:0 D:0 U:0 |
| `references/atoms_pending/2026-04-25/valoria_master_analysis/08__section-8-synthesis-valoria-s-design-identity.md` | 2 | L:2 PS:0 BOTH:0 D:0 U:0 |
| `references/atoms_pending/2026-04-25/valoria_master_consolidation/13__4-5-rendering-strain-substrate-posture-cost.md` | 1 | L:1 PS:0 BOTH:0 D:0 U:0 |
| `references/atoms_pending/2026-04-25/valoria_master_consolidation/24__from-simulation-review-simulation-review-2026-04-1.md` | 1 | L:1 PS:0 BOTH:0 D:0 U:0 |
| `references/atoms_pending/2026-04-25/valoria_master_document/121__v-3-derived-stats-gap-07.md` | 1 | L:1 PS:0 BOTH:0 D:0 U:0 |
| `references/glossary.md` | 2 | L:1 PS:0 BOTH:0 D:1 U:0 |
| `references/propagation_map.md` | 1 | L:1 PS:0 BOTH:0 D:0 U:0 |
| `references/splits/params_board_game_split.yaml` | 4 | L:1 PS:0 BOTH:0 D:1 U:2 |
| `references/throughlines_meta_infill.md` | 3 | L:1 PS:0 BOTH:0 D:1 U:1 |
| `references/valoria_cross_conversation_review.md` | 1 | L:1 PS:0 BOTH:0 D:0 U:0 |
| `references/valoria_simulation_review.md` | 3 | L:2 PS:0 BOTH:0 D:0 U:1 |

**Notable Tier 1 patterns:**
- Excommunication / Church doctrine actions read Mandate as ecclesiastical recognition → refactor to Legitimacy.
- Royal Decree / Crown formal authority reads → Legitimacy.
- Parliamentary / institutional procedural acts → Legitimacy.
- Faction inheritance, succession, treaty signing → Legitimacy.

## §6 Tier 2 — PS-Dominant Files

1 file where Mandate is read primarily as populace backing.

| File | Total | Breakdown |
|---|---:|---|
| `designs/arcs/gm_ref/arcs_05_09_index.md` | 1 | L:0 PS:1 BOTH:0 D:0 U:0 |

**Notable Tier 2 pattern:** populace-rebellion narrative arcs read Mandate as Popular Support; refactor when those arcs are revised.

## §7 Tier 3 — BOTH-Dominant Files

3 files where Mandate semantic is genuinely combined.

| File | Total | Breakdown |
|---|---:|---|
| `canon/patch_register_active.yaml` | 1 | L:0 PS:0 BOTH:1 D:0 U:0 |
| `designs/scene/conviction_track_v30_infill.md` | 1 | L:0 PS:0 BOTH:1 D:0 U:0 |
| `references/atoms_pending/2026-04-25/_reviews/08_session_consolidation_review.md` | 1 | L:0 PS:0 BOTH:1 D:0 U:0 |

**Recommendation:** keep on Mandate (derived); no refactor improves semantic clarity here.

## §8 Tier 4 — DERIVED-Dominant Files (No Refactor Required)

54 files where Mandate is used as a generic 0–7 stat in pool/Ob/check formulas, starting values, ceilings/floors, ±N modifiers. These reads operate correctly via §4 derivation indefinitely.

| File | Total | Breakdown |
|---|---:|---|
| `canon/editorial_ledger_index.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `canon/session_checkpoint.md` | 3 | L:0 PS:0 BOTH:0 D:2 U:1 |
| `designs/architecture/canonical_registry.md` | 4 | L:1 PS:0 BOTH:0 D:2 U:1 |
| `designs/architecture/complete_systems_reference.md` | 6 | L:2 PS:0 BOTH:0 D:3 U:1 |
| `designs/architecture/generational_transition_v30.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `designs/architecture/hybrid_gaps_v30.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `designs/architecture/session_a_spec_patches.md` | 2 | L:0 PS:0 BOTH:0 D:1 U:1 |
| `designs/arcs/arc_expansion_v30_index.md` | 2 | L:0 PS:0 BOTH:0 D:2 U:0 |
| `designs/npcs/npc_character_analyses_v30_infill.md` | 4 | L:0 PS:0 BOTH:0 D:1 U:3 |
| `designs/provincial/ci_political_v30_index.md` | 2 | L:0 PS:0 BOTH:0 D:2 U:0 |
| `designs/provincial/clock_registry_v30.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `designs/provincial/factions_personal_v30_infill.md` | 2 | L:0 PS:0 BOTH:0 D:1 U:1 |
| `designs/provincial/peninsular_strain_v30_index.md` | 2 | L:0 PS:0 BOTH:0 D:2 U:0 |
| `designs/scene/miraculous_event_v30.md` | 2 | L:0 PS:0 BOTH:0 D:1 U:1 |
| `designs/videogame/godot_architecture_specification.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `designs/world/solmund_master_document.md` | 3 | L:0 PS:0 BOTH:0 D:2 U:1 |
| `designs/world/southernmost_v30.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `params/bg/ci_seizure.md` | 12 | L:0 PS:0 BOTH:0 D:9 U:3 |
| `params/bg/core.md` | 12 | L:2 PS:1 BOTH:1 D:6 U:2 |
| `params/bg/faction_actions.md` | 30 | L:3 PS:0 BOTH:0 D:17 U:10 |
| `params/bg/ministry.md` | 24 | L:4 PS:0 BOTH:0 D:6 U:14 |
| `params/bg/phases.md` | 2 | L:0 PS:0 BOTH:0 D:1 U:1 |
| `params/bg/stress_patches.md` | 9 | L:0 PS:0 BOTH:0 D:1 U:8 |
| `params/bg/tracks.md` | 12 | L:4 PS:0 BOTH:1 D:5 U:2 |
| `params/factions/riskbreakers_identity.md` | 16 | L:3 PS:0 BOTH:0 D:5 U:8 |
| `params/factions/stats_1_7_scale.md` | 35 | L:9 PS:0 BOTH:0 D:10 U:16 |
| `params/threadwork_superseded.md` | 3 | L:0 PS:0 BOTH:0 D:1 U:2 |
| `references/arcs/arc_register_events.md` | 4 | L:0 PS:0 BOTH:0 D:1 U:3 |
| `references/atoms_pending/2026-04-25/_consolidated/02_solmund_cultural_guide.md` | 3 | L:0 PS:0 BOTH:0 D:2 U:1 |
| `references/atoms_pending/2026-04-25/_consolidated/04_faction_balance_three_modes.md` | 9 | L:2 PS:0 BOTH:0 D:3 U:4 |
| `references/atoms_pending/2026-04-25/_consolidated/05_v2_historicity_correction.md` | 2 | L:0 PS:0 BOTH:0 D:1 U:1 |
| `references/atoms_pending/2026-04-25/_consolidated/10_session_log_index.md` | 3 | L:0 PS:0 BOTH:0 D:3 U:0 |
| `references/atoms_pending/2026-04-25/_reviews/02_solmund_cultural_guide_review.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/atoms_pending/2026-04-25/_reviews/03_threadwork_design_review.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/atoms_pending/2026-04-25/_reviews/09_canon_rectification_pp675_ed783_review.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/atoms_pending/2026-04-25/master_document_2026-04-25/14__2-2-monte-carlo-simulation-results.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/atoms_pending/2026-04-25/master_document_2026-04-25/26__p1-essential-for-modes-to-feel-rich.md` | 2 | L:0 PS:0 BOTH:0 D:2 U:0 |
| `references/atoms_pending/2026-04-25/solmund_master_document/25__22-faction-response-pathways.md` | 2 | L:0 PS:0 BOTH:0 D:1 U:1 |
| `references/atoms_pending/2026-04-25/solmund_master_document/31__28-implementation-priorities.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/atoms_pending/2026-04-25/valoria_master_analysis/03__section-3-v2-factual-audit-findings-5-tiers.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/atoms_pending/2026-04-25/valoria_master_analysis/11__section-11-outstanding-design-decisions.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/atoms_pending/2026-04-25/valoria_master_document/114__iii-3-claims-that-survive-recalibration.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/atoms_pending/2026-04-25/valoria_master_document/56__9-7-peninsular-strain-0-10.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/atoms_pending/2026-04-25/valoria_session_2026-04-25_master/03__section-3-major-new-specs-authored.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/atoms_pending/2026-04-25/valoria_session_2026-04-25_master/04__section-4-stress-tests-run.md` | 2 | L:0 PS:0 BOTH:0 D:2 U:0 |
| `references/canonical_sources.yaml` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/numeric_bounds_report.yaml` | 11 | L:1 PS:0 BOTH:0 D:8 U:2 |
| `references/propagation_log.md` | 2 | L:0 PS:0 BOTH:0 D:1 U:1 |
| `references/throughlines_complete.md` | 4 | L:1 PS:0 BOTH:0 D:2 U:1 |
| `references/throughlines_meta_solmund_appendix.md` | 1 | L:0 PS:0 BOTH:0 D:1 U:0 |
| `references/valoria_canonical_definitive_r2.md` | 4 | L:1 PS:0 BOTH:0 D:2 U:1 |
| `references/valoria_complete_systems_r2.md` | 6 | L:2 PS:0 BOTH:0 D:3 U:1 |
| `references/valoria_interdoc_audit.md` | 2 | L:0 PS:0 BOTH:0 D:1 U:1 |
| `references/values_master.yaml` | 6 | L:0 PS:0 BOTH:0 D:4 U:2 |

**Recommendation:** no refactor. These files use Mandate as a generic stat; semantic precision is irrelevant.

## §9 Tier 5 — UNCLASSIFIED Files (Treat as DERIVED)

20 files with no decisive linguistic signal. Default treatment: DERIVED (no refactor needed). Designer review may reclassify into Tier 1, 2, 3, or 4.

| File | Total | Breakdown |
|---|---:|---|
| `canon/03_canonical_timeline.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `designs/architecture/early_game_ignition_analysis.md` | 5 | L:0 PS:0 BOTH:0 D:0 U:5 |
| `designs/npcs/companion_specification_v30.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `designs/npcs/npc_foils_v30_infill.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `designs/threadwork/threadwork_v30_infill.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `params/bg/clocks.md` | 2 | L:0 PS:0 BOTH:0 D:0 U:2 |
| `params/contest.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `params/threadwork.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/_reviews/04_faction_balance_three_modes_review.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/master_document_2026-04-25/28__p3-designer-hygiene-no-direct-player-impact.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/master_document_2026-04-25/38__phase-e-strategic-balance-refinement-p1-sim-valida.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/master_document_2026-04-25/40__phase-g-designer-hygiene-p3.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/valoria_master_analysis/06__section-6-holistic-system-level.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/valoria_master_consolidation/14__4-6-per-faction-thread-entry-points.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/valoria_master_document/100__19-4-meta-throughlines-emergent-structural-pattern.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/valoria_master_document/58__10-2-domain-echo-the-upward-pipe.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/valoria_master_document/68__13-2-faction-toolkits-not-alternate-endpoints.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |
| `references/atoms_pending/2026-04-25/valoria_master_document/88__16-7-npc-recruitment-pp-642.md` | 2 | L:0 PS:0 BOTH:0 D:0 U:2 |
| `references/proper_noun_triage_round2.yaml` | 3 | L:0 PS:0 BOTH:0 D:0 U:3 |
| `references/wc_survival_spine.md` | 1 | L:0 PS:0 BOTH:0 D:0 U:1 |

## §10 Per-File Refactor Order (Tier 1 + Tier 2)

Files for opportunistic refactor, sorted by descending Mandate-mention count (highest-impact first):

| Rank | File | L Lines | Total | Refactor Priority |
|---:|---|---:|---:|---|
| 1 | `params/bg/institutions.md` | 9 | 21 | high |
| 2 | `designs/provincial/baralta_crown_claim_v30.md` | 7 | 19 | high |
| 3 | `references/arcs/arc_register_factions.md` | 6 | 17 | high |
| 4 | `params/bg/parliament.md` | 5 | 16 | high |
| 5 | `designs/provincial/faction_behavior_v30.md` | 3 | 12 | medium |
| 6 | `designs/arcs/emergent_campaign_arcs.md` | 3 | 8 | medium |
| 7 | `params/bg/ed_resolutions.md` | 3 | 9 | medium |
| 8 | `params/bg/npcs_special.md` | 3 | 5 | medium |
| 9 | `params/factions_personal.md` | 3 | 13 | medium |
| 10 | `designs/architecture/campaign_modes_v30.md` | 2 | 3 | medium |
| 11 | `designs/provincial/faction_layer_v30_infill.md` | 2 | 4 | medium |
| 12 | `designs/provincial/strategic_layer_v30_index.md` | 2 | 6 | medium |
| 13 | `designs/world/worldbuilding_canon_audit_v30.md` | 2 | 8 | medium |
| 14 | `params/bg/npc_priority_trees.md` | 2 | 5 | medium |
| 15 | `params/bg/victory.md` | 2 | 8 | medium |
| 16 | `references/arcs/arc_register_clocks.md` | 2 | 2 | medium |
| 17 | `references/atoms_pending/2026-04-25/_consolidated/01_throughlines_meta.md` | 2 | 4 | medium |
| 18 | `references/atoms_pending/2026-04-25/valoria_master_analysis/08__section-8-synthesis-valoria-s-design-identity.md` | 2 | 2 | medium |
| 19 | `references/valoria_simulation_review.md` | 2 | 3 | medium |
| 20 | `designs/npcs/npc_behavior_v30_infill.md` | 1 | 1 | low |
| 21 | `designs/npcs/npc_foils_v30.md` | 1 | 6 | low |
| 22 | `designs/provincial/baralta_crown_claim_v30_infill.md` | 1 | 2 | low |
| 23 | `designs/provincial/fail_forward_pp177.md` | 1 | 4 | low |
| 24 | `designs/provincial/strategic_layer_v30_infill.md` | 1 | 3 | low |
| 25 | `designs/ui/valoria_ui_ux_supplement_derived_settlement.md` | 1 | 1 | low |

*(Top 25 of 47 total Tier 1+2 files)*

## §11 Stage 7 Sign-off

| Item | Status |
|---|---|
| Audit performed | YES |
| Total Mandate references catalogued | 530 |
| L-dominant files identified for opportunistic refactor | 46 |
| PS-dominant files identified | 1 |
| Files requiring no refactor (DERIVED-dominant + UNCLASSIFIED + BOTH) | 77 |
| Backward compatibility verified via §4 derivation | YES |
| Mandate retention canonical for backward compat | YES (per faction_behavior_v30 §4) |

**Stage 7 closed:** No immediate refactor required. Backward-compatibility path intact. Opportunistic refactor list available for Phase B continuation.

## §12 Open Items Carried Forward

- Per-line manual review of UNCLASSIFIED entries (deferred; default-DERIVED treatment is safe).
- Tier 1 refactor: opportunistic, executes when files are touched for other reasons.
- Phase B Stage 8 (Stage 10 sim verification) is unblocked by this audit; no consumer refactor blocks Stage 8.

---

**End audit. PROVISIONAL pending Stage 10 calibration.**
