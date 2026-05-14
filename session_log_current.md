session_id: 2026-05-13_v15_v17_stamina_through_multiturn
session_close: 2026-05-13
phase: sim-mb-06
status: closed
last_stage: v17-committed-ef7e8ec_multi_turn_orchestrator
next_action:
  skill: valoria-simulator
  task: multi-turn battery band recalibration (design decision); pursuit/cascade (D-4/D-5); discipline with continuous effective_size (D-6)
blockers: []
commits: [651bf7d, 55952ac, f3d94ef, ef7e8ec]
notes: |
  ## Four commits this session

  v15 (651bf7d) — G-1 stamina + G-2 rout on phase-boundary hooks.
  v16 (55952ac) — G-3 continuous effective_size + lethality recalibration.
  v16 audit (f3d94ef) — formula validation + gap detection, 10 gaps, 0 P1.
  v17 (ef7e8ec) — multi-turn orchestrator + between-turn rules + D-7 morale separation.

  ## Architecture clarified (Jordan direction)

  4 zoom levels: Peninsula → Territory → Battlefield (25x21 per unit) → Scene.
  3-phase cap per engagement turn. 5-8 turns per battle.
  Time is absolute. Adjacent allies at one depth join. Auto-resolve available.
  30% cumulative casualties for rout (gameplay, not historical 10-15%).

  ## Key findings

  - Continuous effective_size: pool degrades proportionally. Works.
  - LETHALITY_SCALE=0.10: ~15% casualties per 3-phase turn. Correct for multi-turn.
  - Multi-turn compounding: geometric advantages amplify across turns.
    HS vs Line = 79%, RF vs HS = 74% at equal stats.
    This is CORRECT (strategic composition > tactical execution).
    Battery bands need recalibration for multi-turn model.
  - G-3 confirmed: lethality recalibration enables morale system to work as designed.
  - Throughline/NERS assessment completed. System sound at conception, over-specified
    at resolution (48-entry weapon matrix, 8 morale triggers). Streamlining recommended.

  ## Gap register (from v16 audit)

  D-1 multi-turn orchestrator: IMPLEMENTED (v17)
  D-7 morale separation: IMPLEMENTED (v17)
  D-9 between-turn rules: IMPLEMENTED (v17)
  D-4 pursuit damage: NOT YET
  D-5 rout cascade: NOT YET
  D-6 discipline with continuous eff_size: NOT YET
  D-8 multi-turn battery bands: need design decision from Jordan
  D-2 per-unit grid: architecture change (later)
  D-3 multi-unit engagements: architecture change (later)
