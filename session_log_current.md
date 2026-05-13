session_id: 2026-05-13_phase_structure_audit
session_close: 2026-05-13
phase: sim-mb-06
status: closed
last_stage: v14-committed-1cc27b2_phase_structure_wired_audit_complete
next_action:
  skill: valoria-simulator
  task: G-1+G-2 paired cycle — stamina mechanism + rout-at-casualty-threshold on phase-boundary hooks
blockers: []
commits: [c33aa93aee095df634f6c74f2d116bf6dc7dae6b, 1cc27b2cda822b80c98f6ad0fdd394fc1ef7cd75]
notes: |
  ## What landed this session
  
  v13 (c33aa93) — cross-side cell contention, strict speed-differential resolution.
    - resolve_cross_side_contention() in v13.py: speed-priority for moving-vs-moving
      same-cell contests; loser cells that moved this turn revert to pre-move snapshot.
    - Strict-speed-only (deviation from Jordan full spec, deferred until cavalry):
      size/random tiebreakers applied per contested position per turn produced battery
      noise in symmetric matchups (random tiebreak fires on every Line-vs-Line contest).
      Equal-speed contests stay co-located, resolved by combat — historically the
      hoplite phalanx mirror pattern.
    - Historical: Crécy/Agincourt timing (defenders pre-positioned), Leuctra oblique
      order (faster wing arrives first), hoplite equal-speed resolution via combat.
    - Battery: 12/13 (unchanged from v12; H5 RF/HS still 47.4%).
    - Mechanism fires substantially in asymmetric-speed matchups (H3 HS-Line 14/battle,
      H10 Line-HS 8/battle, H6 RF-Line 4/battle); correctly silent in equal-speed
      (H1, H5, H7).
  
  v14 (1cc27b2) — phase/tick structure wired into simulation.
    - TICKS_PER_PHASE = 6, locked per Jordan directive after research confirmed
      "three-hex charge would take about 5 minutes" (Operational Studies Group) plus
      1-2 ticks reform = 6 total. Hoplite phalanx exhaustion bound (~10-15 min sustained
      close combat) maps to same 6-tick frame for infantry (ephodos → krousis →
      doratismos → othismos → pararrhexis).
    - phase_boundary(unit_a, unit_b, phase_idx) fires every 6 ticks within run_battle.
      Six empty hook stubs in canonical order: stamina_check, morale_check_phase,
      rout_resolution, rally_check, reform_check, threadwork_check.
    - Zero combat-behavior change. Battery 12/13 unchanged.
    - run_battle return dict additive: 'phases' and 'tick_in_phase' added.
    - Depth-as-replacement design started this session was REVERTED before commit.
      Research showed depth's real role is stamina-replacement (rear ranks rotate
      forward to refresh exhausted front-rankers), not casualty-replacement. That
      belongs on the stamina_check hook in next cycle.
  
  Audit cycle complete:
    - tests/sim/instrument_battle.py — reusable instrumentation tool for tick-by-tick
      battle records (per-cell position/speed/facing/halted, volley pending, pre-pairs,
      target assignment, advance deltas, cross-side contention firings, post-movement
      contacts, full pool decomposition, dice result, per-unit deltas, ASCII grid).
    - tests/sim/audit_record_v14_h5.md — H5 RF vs HS seed 1000000 (outstanding tension).
    - tests/sim/audit_record_v14_h1.md — H1 Line vs Line seed 1000000 (control mirror).
    - tests/sim/audit_sim_mb_06_v14.md — consolidated audit + NERS analysis. Five
      top-level divergences identified, every existing mechanism + every proposed gap
      scored against project NERS criteria (Necessary/Elegant/Robust/Smooth), audited
      against both literal history AND acclaimed-videogame precedents (Total War
      Medieval II / Three Kingdoms, Field of Glory II, Battle Brothers, Bannerlord).
  
  ## Top-level findings (audit)
  
  1. Per-tick lethality ~5-10× too high (sim tick-scale = historical phase-scale).
  2. No rout-at-casualty-threshold; battles run to ~100% destruction (historical
     and genre-universal: rout at 5-15% casualties).
  3. No stamina/exhaustion (THE limiting factor historically; in every acclaimed game).
  4. No rest/recovery between contact periods.
  5. Front-row-faster-than-rear-rank infantry speed is historically backwards
     (oblique-order belongs at multi-unit timing layer, not per-row of one unit).
  
  ## Gap register
  
  G-1 stamina, G-2 rout-at-threshold — HIGH priority, full NERS pass. Paired.
  G-4 formation cohesion, G-5 per-cell nearest-attacker angle — MEDIUM.
  G-6 unit-pace speed (replace per-row) — MEDIUM-HIGH (strict NERS improvement).
  G-7 rally — MEDIUM, completes rout/rally arc.
  G-3 per-tick lethality recalibration — likely falls out of G-1+G-2; defer.
  G-8 reform after withdrawal — defer until G-1/G-2 wired.
  G-9 threadwork — needs design clarification from Jordan; scope unspecified.
  G-10 sarissa multi-rank projection — defer; subsumed by stamina.
  G-11 cavalry mechanism — HIGH priority; BLOCKED on battery scope.
  
  ## Next cycle plan
  
  G-1 + G-2 paired implementation on existing phase-boundary hooks.
    - Add stamina to Unit dataclass (init high, depletes per contact tick).
    - Expose accessor for pool calc (degrade pool if stamina low).
    - Populate stamina_check: apply tick-deltas at phase boundary.
    - Populate morale_check_phase: casualties + stamina vs discipline-modified threshold.
    - Populate rout_resolution: set routed=True on threshold failure; queue pursuit
      damage for next phase.
    - Verify on instrumented H5 (regenerate via instrument_battle.py) + full battery.
    - Expected: H5 → 50-65% as RF rotation advantage manifests. RF's 6-deep column
      sustains stamina via rotation; HS's wings (3-deep at max) exhaust; HS routs
      first at morale threshold.
  
  ## Per-mechanism NERS summary (audit)
  
  Pass on all four (keep): volley-before-melee, column-local targeting, phase structure.
  Concept right, implementation needs fix: per-cell octagon angle (G-5), support_engage_frac
    (revisit with stamina).
  Fails all four NERS axes (REPLACE): per-row variable speed → G-6 unit-pace.
  Light R, waiting on cavalry: cross-side speed-priority contention.
  Triggers calibrated wrong (recalibrate under G-2): discipline penalty thresholds,
    morale degradation thresholds.
