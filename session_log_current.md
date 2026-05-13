session_id: 2026-05-13_v15_stamina_rout
session_close: 2026-05-13
phase: sim-mb-06
status: closed
last_stage: v15-committed-651bf7d_stamina_rout_battery_11_of_13
next_action:
  skill: valoria-simulator
  task: G-3 lethality recalibration — prerequisite for meaningful rout rates; H7 GL geometric advantage reinforcement
blockers: []
commits: [651bf7dd3308a808b155afde3511677a8cc649f3]
notes: |
  ## What landed this session

  v15 (651bf7d) — G-1 stamina + G-2 rout on phase-boundary hooks.
    - Stamina: drain 16/contact-tick, recovery 8/reserve-rank at phase boundary.
      Pool penalty -1 die at exhaustion only (minimalist after 5 tuning iterations).
    - Rout: phase-boundary morale check for exhausted+damaged units (floor override
      at 20% casualties). Per-tick morale unchanged from v14.
    - Battery: 11/13 in-band (v14 at same seeds: 10/13).
      H5 RF-vs-HS FIXED (47.4 -> 50.2%). R3 Ranged mirror FIXED (44.0 -> 45.4%).
      H7 GL-vs-Line regressed (51.6 -> 49.4%, structural — GL shallow depth pays
      stamina cost vs Line depth).
    - Key finding: G-3 does NOT fall out of G-1+G-2 (contradicts audit prediction).
      Per-tick lethality (~3 HP/tick) kills units in 7-8 ticks; stamina differential
      needs 12+ ticks. Rout rate 0% — battles still end by HP death.

  ## Tuning iterations explored

  5 iterations tested: aggressive pool penalties (7/13), moderate (7/13), casualty-based
  morale triggers (7/13), stamina-gated triggers (4/13), minimalist pool-only (11/13).
  The -1 exhaustion penalty was the only tuning that improved H5 without destabilizing
  geometry-driven matchups.

  ## Gap register update

  G-1 stamina: IMPLEMENTED (v15). Mechanism live but effect limited by per-tick lethality.
  G-2 rout-at-threshold: PARTIALLY IMPLEMENTED (phase-boundary hooks live, 0% rout rate).
  G-3 lethality recalibration: CONFIRMED NEEDED (not falling out of G-1+G-2 as predicted).
  G-7 rally, G-8 reform, G-9 threadwork: hooks remain empty.
  H7 regression: GL geometric advantage needs reinforcement in a later cycle.
