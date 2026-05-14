session_id: 2026-05-13_v15_v20_emergent_morale
session_close: 2026-05-13
phase: sim-mb-06
status: closed
last_stage: v20-committed-ae5c716_emergent_morale_erosion
next_action:
  skill: valoria-simulator
  task: D-5 morale cascade; G-11 cavalry pursuit; multi-unit engagement; per-unit grid
blockers: []
commits: [651bf7d, 55952ac, f3d94ef, ef7e8ec, 5b7aafa, 7f726b8, 334a885, ae5c716]
notes: |
  ## Eight commits — v15 through v20

  v15 (651bf7d) — stamina + rout hooks. v16 (55952ac) — continuous effective_size.
  v16 audit (f3d94ef). v17 (ef7e8ec) — multi-turn orchestrator. v18 (5b7aafa) — discipline.
  v19 (7f726b8) — bottom-up TroopCount HP. v19 fix (334a885) — pursuit canonical.
  v20 (ae5c716) — emergent morale erosion formula.

  ## Key result: emergent morale erosion

  morale_erosion = damage_taken / (discipline * command)
  30% rout threshold FALLS OUT from: morale=6, dmg~3/tick, disc=5, cmd=4.
  erosion = 3/20 = 0.15/tick. 6.0/0.15 = 40 ticks. 40 * 0.75%/tick = 30%.
  No imposed thresholds. No morale floor. General's contribution in denominator.
  Higher command → slower erosion → later rout. Generalship dominance (T1) structural.

  ## Bottom-up audit findings

  Started with 15/24 imposed constants. v20 removed 3 morale thresholds +
  flat stamina drain, replacing with emergent formulas. Remaining imposed:
  STAMINA_MAX (100), STAMINA_DRAIN_PER_CONTACT_CELL (3), STAMINA_RECOVERY_PER_RESERVE_RANK (8),
  STAMINA_EXHAUSTED_POOL_PENALTY (-1), BETWEEN_TURN_STAMINA_RECOVERY (30),
  TICKS_PER_PHASE (6), BATTLEFIELD_SIZE (25), BUFFER_CELLS (5).
  All structural/tuning — no morale thresholds remain.

  ## Architecture confirmed

  4 zoom: Peninsula → Territory → Battlefield (25x21/unit) → Scene.
  3-phase cap/turn. HP = TroopCount = Size * BLOCK_SIZE. No LETHALITY_SCALE.
  Standard infantry cannot pursue (§A.12). Pursuit is level-2 + Fast units.
