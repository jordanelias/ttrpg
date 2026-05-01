---
session_id: 2026-04-30-architecture-session
session_open: 2026-05-01
phase: "Architectural design — PP-686 faction architecture, PP-687 universal Key substrate, PP-688 articulation layer (anticipated)"
status: open
last_stage: >
  COMMIT — five batched commits to designs/audit/2026-04-30-architecture-session/:
  16528352 (foundation: week audit + workplan v3 addendum),
  60e471e1 (PP-686 proposal + audit + sim v1/v2 + evaluations),
  eec6b01c (PP-687 proposal + audit + sim + evaluation),
  b2ef42fc (narrative articulation: arcs/story/three-tier/significance/cut-scene),
  de10d7aa (session-folder index README).
  All artifacts PROVISIONAL — pending Jordan ratification per each proposal's open-questions section.

session_arc:
  - "16528352518: foundation — week audit NERS (174:5 design:impl ratio; lateral peer-system flagged WEAKEST) + workplan v3 addendum (Phase 5a Godot-early addendum)"
  - "60e471e15: PP-686 — Mission/Cascade/Public Expectation/L+PS architecture replacing Ethical Framework Modifiers + Mandate. Sim v1 (7 scenarios; 5 calibration deltas C1-C5) + v2 with structured-concentration NPCs + Self-Other axis (10-item set C1-C10)"
  - "eec6b01cc: PP-687 — universal Key substrate. 19/5/0 NERS pre-sim, 22/2/0 post-sim. 6 scenarios all pass: 2,703 keys × 30 seasons in 144ms; determinism confirmed; cross-scale provenance walks correctly; cycle detection works"
  - "b2ef42fcf: narrative articulation layer (PP-688 anticipated). Three-tier: Tier 1 mud / Tier 2 trigger cut scenes / Tier 3 year-end omniscient chronicle. Significance fn (prominence × stakes × expectation × awareness, two tracks). Canonical Knot/Belief/Inspiration integration per fieldwork_socializing §5.5-5.6 + params/core.md"
  - "de10d7aa4: index README"

architectural_decisions_pending_ratification:
  - "PP-684 Conviction taxonomy revision: 12 entries (Faith/Authority/Order/Scholastic/Utility/Equity/Liberty/Precedent/Community/Identity/Warden/Virtue) with Honor provisional 13th; Self-Other orientation as separate axis [-1,+1]; cultural background templates"
  - "PP-685 Conviction migration roster (Reason/Autonomy/Continuity-tagged characters reassigned)"
  - "PP-686 faction architecture (4-piece: Mission/Cascade/Public Expectation/Legitimacy+Popular Support); 8 open questions §6"
  - "PP-687 universal Key substrate (typed event records as engine substrate); 10 open questions §9; 6 spec refinements per sim evaluation §4"
  - "PP-688 articulation layer (anticipated; not yet drafted as PP)"

calibration_set_C1_C10:
  - "C1: Cap Ob_modifier at ±2 (was ±3)"
  - "C2: Drop strictness reward path (saturates cap)"
  - "C3: drift_coef = 0.55-0.65 (sim showed 0.45 still under-responsive)"
  - "C4: Crisis-bypass rule: leader.scars >= 3 suspends cascade damping"
  - "C5: β-fidelity gating during negative outcomes (×0.5)"
  - "C6: Orphan NPC rule: α=1.0, contribute normally"
  - "C7: Self-Other orientation provisional formula (calibrate at Stage 10)"
  - "C8: NPC personal_convictions = primary (1-3 entries, 0.6-0.8) + cultural background (0.2-0.4)"
  - "C9: Codify aggregate as Standing-weighted normalized sum"
  - "C10: Cultural background templates as separate canonical authoring layer"

next_action:
  skill: editorial
  description: >
    PRIMARY (after Jordan ratification of architecture session):
    1. Resolve PP-687 §10.1 spec refinements inline (cycle detection, Memory query API, sub-step ordering, determinism enumeration, axis-count caveat, partial-migration bootstrap)
    2. Revise PP-686 spec to reference PP-687 (resolves audit P1-3, P2-1, P2-3, lateral weakness)
    3. Apply C1-C10 calibration deltas to PP-686 v3 spec
    4. Author full PP-687 Key type registry (~25-30 types)
    5. Author Conviction → axis matrix (12 × 4 = 48 entries) with calibration rationale
    6. Draft PP-688 articulation layer formally (Tier 1 UI lens / Tier 2 trigger ruleset / Tier 3 chronicle generator + significance function + canonical Knot/Belief/Inspiration integration)
    7. Add to canon/patch_register_active.yaml: PP-684, PP-685, PP-686, PP-687, PP-688 with full vetting blocks per PP-674 framework

    PRIOR SESSION CARRY-FORWARD (from terminology-vector-audit session):
    - Phase 1 of ecosystem workplan v2 (schemas + advisory two-layer validator)
    - PP-689 SHA followup
    - P1 backlog (Wager / Thread Revelation / Convictions / Pressure Points / Cohesion sweep / bare GM sweep)
    - Gameplay-design directive (workplan §B1 flagged infrastructure-to-gameplay imbalance)

blockers:
  - "All 5 commits this session land artifacts as PROVISIONAL — Jordan must review and ratify each PP's open questions before implementation"
  - "PP-687 ratifies before PP-686 implementation (sequencing dependency; PP-686 spec consumes PP-687)"
  - "Workplan v2 Phase 1 still gates the broader infrastructure work; this session opened a parallel architectural track"

session_artifacts: designs/audit/2026-04-30-architecture-session/
  - 00_index.md
  - 01_week_audit_NERS.md
  - 02_workplan_v3_addendum.md
  - 03_PP-686_proposal.md
  - 04_PP-686_audit_NERS.md
  - 05_PP-686_simulation_evaluation.md
  - 06_PP-686_sim_v2_evaluation.md
  - 07_PP-687_proposal.md
  - 08_PP-687_audit_NERS.md
  - 09_PP-687_simulation_evaluation.md
  - 10_emergent_arcs_engagement_NERS.md
  - 11_story_vs_happenings_analysis.md
  - 12_three_tier_articulation_reframe.md
  - 13_significance_function_omniscient_voice.md
  - 14_significance_canonical_integration.md
  - 15_accounting_cut_scene_snippet.md
  - sims/pp686_sim.py + pp686_sim_output.txt
  - sims/pp686_sim_v2.py + pp686_sim_v2_output.txt
  - sims/pp687_sim.py + pp687_sim_output.txt

notes:
  - "All proposals PROVISIONAL pending Jordan ratification; do not add to patch_register_active.yaml until §6 / §9 / §10 open questions resolved."
  - "Sim verification ledger (/home/claude/sim_verification_ledger.json) carries 28 distinct numeric values used across PP-686 + PP-687 sims; all cited to provisional proposal documents per sim_fabrication_check hook."
  - "Conviction taxonomy revision (PP-684): 12 entries confirmed during conversation; Honor flagged provisional 13th; Greed explicitly NOT a Conviction (Self-Other orientation axis instead)."
  - "PP-686 sim showed: honest defeat (ΔL +0.76, ΔPS -1.79 v2), successful tyrant (L-PS divergence 2.79), succession dynamics (Cesare cascade fid 0.904 → 0.631), all reproduce dramatic patterns Jordan named."
  - "PP-687 sim showed: 18,724 keys/sec; replay determinism confirmed; CAUSAL_GRAPH walks sub-millisecond; Memory grows to ~1000 entries/NPC at 30 seasons (indexing strategy needed for queries)."
  - "Articulation reframe: real-time arc detection rejected; year-end Accounting as omniscient retrospective is canonical framing. Cut scenes are punctuation form (Tier 2 + Tier 3)."
  - "Significance function reads canonical Knot (fieldwork_socializing §5.6), Belief (§5.5), Inspiration (params/core.md L128) mechanics directly; does not invent parallels."
