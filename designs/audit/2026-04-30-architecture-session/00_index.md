# 2026-04-30 Architecture Session

**Scope:** PP-686 faction architecture + PP-687 universal Key substrate + narrative articulation layer (PP-688 anticipated).
**Status:** All artifacts PROVISIONAL — pending Jordan ratification per each proposal's open-questions section.

## Foundation

- `01_week_audit_NERS.md` — week-of audit, NERS all directions, identifies lateral peer-system integration as project's weakest direction.
- `02_workplan_v3_addendum.md` — Phase 5 split into 5a (early Godot scene, 5 sessions) + 5b (full prep). Addendum to workplan v3, NOT supersession.

## PP-686 Faction Architecture

- `03_PP-686_proposal.md` — Mission, Cascade, Public Expectation, Legitimacy + Popular Support. Class A new subsystem replacing Ethical Framework Modifiers + Mandate-as-single-scalar.
- `04_PP-686_audit_NERS.md` — comprehensive NERS, all directions. 3 P1-CRITICAL gaps; 5 P2 gaps; lateral direction WEAKEST.
- `05_PP-686_simulation_evaluation.md` — sim v1 evaluation; 7 scenarios. Architecture validated; 5 calibration deltas identified (C1–C5).
- `06_PP-686_sim_v2_evaluation.md` — sim v2 with structured-concentration NPCs + Self-Other axis + calibration deltas. 10-item calibration set C1–C10.
- `sims/pp686_sim.py`, `pp686_sim_v2.py` — reference implementations.
- `sims/pp686_sim_output.txt`, `pp686_sim_v2_output.txt` — execution traces.

## PP-687 Universal Key Substrate

- `07_PP-687_proposal.md` — typed event records as engine substrate. Class A foundational architecture. Supersedes doc 08 EventImpact and bespoke per-system event handling.
- `08_PP-687_audit_NERS.md` — comprehensive NERS. 19 STRONG / 5 MODERATE / 0 WEAK pre-sim. Diagonal and Lateral both go from PP-686's WEAK → STRONG.
- `09_PP-687_simulation_evaluation.md` — 6 scenarios; performance + determinism + cross-scale provenance + observer resolution + PP-686 integration + cycle detection. 22 STRONG / 2 MODERATE post-sim.
- `sims/pp687_sim.py` — reference implementation.
- `sims/pp687_sim_output.txt` — execution trace (2,703 keys × 30 seasons in 144ms; determinism confirmed).

## Narrative Articulation Layer (PP-688 anticipated)

- `10_emergent_arcs_engagement_NERS.md` — NERS evaluating whether the architectural stack produces emergent arcs and player engagement.
- `11_story_vs_happenings_analysis.md` — honest assessment that substrate alone produces happenings, not story; ~10–15% coherent-story frequency without articulation layer.
- `12_three_tier_articulation_reframe.md` — Tier 1 mud / Tier 2 trigger cut scenes / Tier 3 year-end omniscient chronicle. Replaces real-time arc-detection with temporal articulation at year-end Accounting boundaries.
- `13_significance_function_omniscient_voice.md` — significance function (prominence × stakes × expectation × awareness, two tracks: universal + protagonist).
- `14_significance_canonical_integration.md` — significance function reads canonical Knot/Belief/Inspiration mechanics directly per `fieldwork_socializing.md` §5.5–5.6 and `params/core.md`. Replaces generic substitutes from §13.
- `15_accounting_cut_scene_snippet.md` — illustrative six-cut-scene set demonstrating Tier 3 omniscient retrospective voice for the Crown's Third Year (Almud).

## Sequencing Recommendation

1. PP-687 ratifies first (substrate)
2. PP-686 spec revised to reference PP-687 (resolves audit P1-3, P2-1, P2-3, lateral weakness)
3. PP-688 (Articulation Layer) drafts and ratifies
4. PP-684 (Conviction taxonomy 12 + Self-Other axis) and PP-685 (migration roster) ratify in parallel
5. Implementation cascade per workplan v3 addendum

## Key Decisions Pending Jordan

- PP-686 §6 open questions (8 items)
- PP-687 §9 open questions (10 items)
- Calibration set C1–C10 from sim v2 evaluation
- Crisis-bypass rule (cascade damping suspended when leader.scars ≥ 3)
- Cumulative narrative weight tracking schema for actors
