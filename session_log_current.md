session_id: 2026-05-13_v15_v19_full_cycle
session_close: 2026-05-13
phase: sim-mb-06
status: closed
last_stage: v19-committed-334a885_bottom_up_troop_count_pursuit_fix
next_action:
  skill: valoria-simulator
  task: multi-turn battery band recalibration; D-5 morale cascade; cavalry (G-11) for pursuit
blockers: []
commits: [651bf7d, 55952ac, f3d94ef, ef7e8ec, 5b7aafa, 7f726b8, 334a885]
notes: |
  ## Seven commits — v15 through v19 + audit + fix

  v15 (651bf7d) — G-1 stamina + G-2 rout hooks.
  v16 (55952ac) — continuous effective_size + lethality recalibration.
  v16 audit (f3d94ef) — 10 gaps, 0 P1.
  v17 (ef7e8ec) — multi-turn orchestrator + between-turn rules.
  v18 (5b7aafa) — discipline with continuous effective_size.
  v19 (7f726b8) — bottom-up TroopCount HP, LETHALITY_SCALE removed.
  v19 fix (334a885) — pursuit: Standard infantry cannot pursue per §A.12.

  ## Key architectural outcome

  Bottom-up emergent approach achieved:
  - HP = TroopCount = Size * BLOCK_SIZE (400 at Company scale)
  - Damage = soldier casualties from dice (no scaling)
  - ~7% casualties per 3-phase turn (emergent from pool/TN/DR)
  - 4 turns to rout at ~31% cumulative (emergent)
  - 4 zoom levels confirmed: Peninsula → Territory → Battlefield → Scene
  - 3-phase cap per engagement turn, 5-8 turns per battle
  - Standard infantry cannot pursue (canonical §A.12)

  ## Remaining

  D-5 morale cascade (§A.12): rout triggers Disc check on friendly units
  D-8 battery bands: need recalibration for multi-turn model
  G-11 cavalry: Fast speed, pursuit mechanics, charge cycle
  D-2 per-unit grid (25x21): architecture change
  D-3 multi-unit engagements: 2v1, 3v1 etc
