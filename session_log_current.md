session_id: 2026-04-29-mass-battle-ners
session_close: 2026-04-29
phase: "2 — ongoing"
status: audit complete, patch proposals committed
last_stage: >
  mass battle NERS stress test (batches 1+2) + historical review + patch proposals
next_action:
  skill: editorial
  description: >
    JORDAN DECISIONS REQUIRED (see designs/audit/mass_battle_patch_proposals_2026-04-29.md):
    (1) DECISION-MB-01: PP-297 Stalemate Break canonical version — recommend Option A (design doc)
    (2) DECISION-MB-02: Muster initial Size §1.2 vs §1.4 — recommend Option C (defaults = target)
    (3) DECISION-MB-03: Morale reset between battles — recommend Option A (reset)
    (4) DECISION-MB-04: Discipline recovery between battles — recommend Option B (persist, Muster-only)
    (5) DECISION-MB-05: Rout contagion at Morale 0 — recommend Option A (brake, no rout until next turn)
    (6) DECISION-MB-06: Shadow Intel UX — recommend Option A (peek)
    (7) DECISION-MB-07: Siege formula — recommend Option A (pool = Military + 3 siege bonus)
    (8) DECISION-MB-08: Encirclement Morale cap — design addition, Jordan call
    AUTO-APPROVABLE (PP-PROP-MB-01 through 08): Jordan can approve batch.
    STANDING DECISIONS (still pending from prior session):
    (9) Intelligence stat restoration — see designs/audit/faction_stats_renaissance_review.md
    (10) LICENSE decision (GOV-08)
    (11) 1.1 Knot Formation During Play
    (12) 1.2 Accord Propagation
blockers:
  - "8 mass battle design decisions (Jordan)"
  - "8 auto-approvable patches awaiting approval (Jordan)"
  - "Intelligence stat decision (Jordan)"
  - "LICENSE decision (Jordan)"
notes:
  - "Stress test committed: designs/audit/mass_battle_stress_test_2026-04-29.md (13c11a9)"
  - "Patch proposals committed: designs/audit/mass_battle_patch_proposals_2026-04-29.md (1d9f864)"
  - "2 math failures found: MATH-FAIL-01 (siege calibration impossible), MATH-FAIL-02 (H fixed contradiction)"
  - "22 S/E/N/R findings across 2 batches + historical review"
  - "27 provisionals requiring resolution before Godot implementation"
  - "Historical review: system core is sound; 8 auto-approvable clarifications identified"
  - "canonical_sources.yaml at 4670/5000 tokens — approaching threshold"
