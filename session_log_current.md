---
session_id: "2026-05-20-pass-2l-stub-infill-arc-COMPLETE-plus-serializers"
session_close: "2026-05-20T08:30:00Z"
phase: simulation + infrastructure
status: complete
last_stage: per_record_serializers_landed_307e86ca

prior_session_pointer: "2026-05-17-v18-phase-9-faction-unique-actions (7ea85723)"
current_head: "307e86ca per-record serializers for 14 World registries"

next_action:
  recommended: option_A_deferred_migration_batch
  option_A:
    skill: valoria-simulator
    task: "Deferred Migration Batch — 4 mc_v18-behavior-changing migrations as one commit. See deferred_migration_batch."
    files:
      - sim/provincial/massbattle.py
      - sim/mc_v18.py
      - sim/peninsular/accounting.py
      - sim/peninsular/ci_track.py
      - sim/peninsular/ms_track.py
      - sim/peninsular/season.py
      - tests/sim/v17-integration/m3_mass_battle.py
  option_B:
    skill: valoria-canon-authoring
    task: "Resolve 8 canon-gated stubs (requires Jordan input)."
    blocked_on: Jordan

arc_summary:
  description: "Closed Pass 2l stub-infill plan (6669592f → 307e86ca)."
  commits_this_arc: 18
  tier_status:
    tier_0: "10 verified + 1 partial / 14 (3 canon-gated reclassified)"
    tier_1: "6 modules / 7 stubs (1 canon-gated)"
    tier_2: "8 modules / 10 stubs (2 canon-gated)"
  ledger_entries: 104
  schema_migrations: 2
  world_registries_total: 14
  per_record_serializers: 9_dataclasses
  bug_fixed: "canonical PT/Accord bucketing (ec3727fc) — affected ci_track + npe + nascent mass_seizure"
  bug_filed_unfixed: "mc_v18 non-determinism (massbattle.py L630 + L1053) — 03ce9c79"

blockers:
  - "Deferred Migration Batch: 4 mc_v18-behavior-changing migrations. See deferred_migration_batch."
  - "8 canon-gated stubs need Jordan input. See canon_gated_stubs."
  - "knots TIER-DRIFT-001: implemented Option A. Jordan decision pending (A/B/C) — ED-841."
  - "threadwork §6.1 Ontological Status body EMPTY — header only. Filed as canon gap."

deferred_migration_batch:
  shared_blast_radius: mc_v18_baseline
  ordering:
    1: "Fix mc_v18 non-determinism FIRST (massbattle.py L630 roll_pool + L1053 volley_roll_pool → world.rng)"
    2: "Migrate accounting._ms_decay → ms_track.apply_ms_baseline_decay"
    3: "Migrate accounting._ci_generation → ci_track.apply_seasonal_ci (canon-accurate; large CI behavior shift)"
    4: "Migrate mc_v18 inline season → season.run_season"
  post_batch_required:
    - "Re-baseline mc_v18 batch (N=100, base_seed=0)"
    - "Update tests/sim/v17-integration/m3_mass_battle.py expected ranges"
    - "Document baseline shift in stub_infill_plan as new Amendment"
  diagnosis_references:
    mc_v18_ndet: "03ce9c79 + stub_infill_plan Amendment 2026-05-19c"
    accounting_drift: "T0-4 commit message edff2cb0; T0-6 same; T2-1 f145e4b6"

canon_gated_stubs:
  count: 8
  pass_2d_varfell:
    - sim/world/varfell_mandate_action.py
    - sim/world/varfell_territorial_acquisition.py
    - sim/world/restoration_movement.py
  pass_2e_hafenmark:
    - sim/world/charter_liberties.py
    - sim/world/hafenmark_equipment.py
    - sim/world/altonian_reinforcements.py
  pass_2f_church:
    - sim/world/home_sanctuary.py
    - sim/world/infrastructure_reclamation.py
  also_blocked_canon_holes:
    - "threadwork §6.1 body empty"
    - "knots TIER-DRIFT-001 (ED-841 pending)"
    - "Pass 2h treaty_expiration_v30.md body"
    - "Pass 2i insurgency_pipeline_v30.md body"
    - "npc_ai priority-stack contamination audit"

ed_open: 28
ledger_entries: 104

last_known_mc_v18_run:
  context: "run_batch(5, base_seed=42) at HEAD 307e86ca with random.seed(0) pin per ndet finding"
  battles_mean: 38.0
  win_share: {Crown: 40.0, Church: 0.0, Hafenmark: 0.0, Varfell: 60.0}
  note: "Without random.seed(0) pin, results vary between runs (filed unfixed)."

consumer_guidance:
  - "MUST use canonical_pt() / canonical_accord() helpers — NEVER int(t.pt) / int(t.accord)"
  - "Cyclic module pairs use late-imports inside function bodies (knots→coherence, knots→conviction, conviction↔beliefs)"
  - "Schema migration #2 (d2941cde) routes 8 stores through World fields. Always pass world to keep state per-world."
  - "Bootstrap is quick_bootstrap() in github_ops.py — returns (g, h, files, token). PI bootstrap_script text drift to print_status_block is stale."

drift_flags_at_handoff:
  - "PI bootstrap_script references g.print_status_block() not in github_ops.py. quick_bootstrap() returns tuple instead. PI text-only drift."
  - "accounting.py contains legacy duplicates of ci_track + ms_track + season — in-scope for deferred migration batch."
  - "tests/sim/v17-integration/m3_mass_battle.py expected ranges need re-baselining after deferred batch."

pending_followons_not_in_scope:
  - "Mending integration: CO_MOVEMENT_CARDS CM-16/17/18 (Mending-specific per §7.1) deferred."
  - "Combat Tier 2+: Feint multi-turn pool (PP-294), Rescue interception (PP-292), Stunt, group Fibonacci, Vitality-based wound thresholds (PP-269)."
  - "Tribunal.py audit (1 NotImplementedError despite mostly-implemented status)."
  - "Phase 7 Steps 4.3-4.9 (flanking, ripple, tiebreakers, phase hooks, collision, cleanup)."
---
