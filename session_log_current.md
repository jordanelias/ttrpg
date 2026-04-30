session_id: 2026-04-28-stress-test-political-dynamics
session_close: 2026-04-29
phase: simulation
status: closed
last_stage: >
  Three-batch NERS stress test against 12_development_specification.md (political dynamics).
  Commits (ttrpg):
    33100e7b — 13_stress_tests_extended.md (20 issues, 1 critical, 8 high)
    cac8142 — 14_ners_stress_tests.md (25 issues, 9 design-fail, 8 gaps)
    bb79d1a1 — 15_stress_tests_batch3.md (23 issues, 2 critical, 11 design-fail)
    [this close] — 16_session_close_observations.md (comprehensive context, priority order)
  Total: 68 issues across 50 unique test cases. All patchable; no architectural redesign required.
next_action:
  skill: editorial
  description: >
    IMMEDIATE (before implementation):
    (1) Define select_proposal() + domain_armature_alignment table [E-36-A — Critical]
    (2) Define max_scars = inner_circle_active_npc_count x 2 [E-48-A — Critical]
    (3) Define conviction_alignment_multiplier values in Procedure D [E-BOT-A — Critical]
    (4) Single-writer Opinion model: B/C produce Memories only; D consolidates [ST-32-A / E-HORIZ-A]
    (5) Decision: define symbolic_effects consumption OR cut 210-entry table [E-38-A/B]
    PENDING (Jordan decisions, unchanged from prior session):
    (6) Intelligence stat as 6th faction stat — unblocks Spy Ob, Varfell Path A
    (7) LICENSE decision (GOV-08)
    (8) 1.1 Knot Formation During Play
    (9) 1.2 Accord Propagation to Settlement Order
  priority: "Items 1-4 are spec edits with correct answers — no design decision needed. Item 5 is highest-stakes decision (400 authoring entries affected)."
blockers:
  - "select_proposal() — requires domain_armature_alignment authored table (Jordan sign-off)"
  - "symbolic_effects decision (keep + define consumption vs cut table)"
  - "Intelligence stat decision (Jordan, prior session)"
  - "LICENSE decision (Jordan, prior session)"
notes:
  - "Full issue register + priority order in 16_session_close_observations.md"
  - "canonical_sources.yaml at 4670/5000 tokens — approaching threshold"
  - "Class A (undefined values): 15 issues — authoring/spec completeness, no design decisions"
  - "Class B (unused fields): 8 issues — field/procedure misalignment, cut or implement"
  - "Class C (tie-breaking/edge cases): 6 issues — implementation-facing, low urgency"
  - "Class D (ordering/double-write): 5 issues — single-writer Opinion fix resolves core cluster"
