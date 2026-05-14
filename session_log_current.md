session_id: 2026-05-13_v15_v20_emergent_mass_combat
session_close: 2026-05-13
phase: sim-mb-06
status: closed
last_stage: v20-committed-0f0a7b7_general_death_throughline_audit
next_action:
  skill: valoria-simulator
  task: D-5 morale cascade (§A.12); side-A grid bias fix; G-11 cavalry + pursuit
blockers: []
commits: [651bf7d, 55952ac, f3d94ef, ef7e8ec, 5b7aafa, 7f726b8, 334a885, ae5c716, 19434f6, 0f0a7b7]
notes: |
  ## Ten commits — v15 through v20 (6 sim versions + audit + fixes)

  Progression: imposed thresholds → emergent mechanics.
  Key formula: morale_erosion = damage / (discipline × command).
  30% rout emerges from canonical stats without any imposed threshold.
  HP = TroopCount = Size × BLOCK_SIZE. No LETHALITY_SCALE.

  ## Throughlines verified
  T1 Generalship: FULLY EMERGENT (Command in pool + morale denominator)
  T2 Cascade: PARTIAL (chain exists, D-5 morale cascade missing)
  T3 Combined arms: PARTIAL (formations work, cavalry/ranged need work)
  T6 Scale-invariant: VALIDATED (same dice engine at personal + mass scale)

  ## Meta-throughlines confirmed
  M1 General IS the army (Command=0 → instant rout)
  M2 Degradation one-directional (HP/disc/stam/morale all decrease)
  M3 Strategic composition > tactics (multi-turn compounding)

  ## Remaining imposed constants
  Stamina: MAX=100, DRAIN_PER_CELL=1, RECOVERY_PER_RANK=8, EXHAUSTED_PENALTY=-1
  Structure: TICKS_PER_PHASE=6, BLOCK_SIZE=100, BETWEEN_TURN_RECOVERY=30

  ## Known issues
  - Side-A bias 1.6%/turn in mirror matchups (grid/movement asymmetry)
  - Contact-fraction scaling needs per-unit grid to be accurate
  - Ranged combat broken at TroopCount HP scale
  - No morale cascade (D-5), no cavalry (G-11), no multi-unit (D-3)
