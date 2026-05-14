session_id: 2026-05-13_v15_v20_bottom_up_emergent
session_close: 2026-05-13
phase: sim-mb-06
status: closed
last_stage: v20-committed-e15e3bc_emergent_morale_grid_fix
next_action:
  skill: valoria-simulator
  task: true simultaneous resolution (fix processing order bias); freed-attacker mechanic; multi-unit engagements; cavalry G-11
blockers: []
commits: [651bf7d, 55952ac, f3d94ef, ef7e8ec, 5b7aafa, 7f726b8, 334a885, ae5c716, e15e3bc]
notes: |
  ## Nine commits — v15 through v20 (5 sim versions, 1 audit, 3 fixes)

  Key milestone: emergent morale erosion formula.
    erosion = damage / (discipline * command)
    30% rout falls out from morale=6, dmg~3/tick, disc=5, cmd=4.
    No imposed thresholds. Generalship dominance (T1) structural.

  Bottom-up audit: reduced imposed constants from 15 to 8.
    Removed: LETHALITY_SCALE, MORALE_LOSS_PCT_THRESHOLD, MORALE_HEAVY_LOSS_PCT_THRESHOLD,
    ROUT_FLOOR_LOSS_PCT, STAMINA_DRAIN_PER_CONTACT_TICK, morale floor.
    Replaced with emergent formulas using canonical stats.

  Processing order bias found and partially fixed:
    Root cause: unit_a processed before unit_b in run_battle.
    Alternating order reduces mirror bias from 100/0 to 61/35.
    Full fix: true simultaneous resolution (calculate all, then apply all).

  Morale cascade (D-5) prototyped:
    Canonical Ob 1 discipline check — professionals resist 92%, levy fails 36%.
    Flat -1 morale on failure (canonical §A.12).
    Real line-breaking mechanism is freed-attacker (victorious unit joins adjacent fight), not morale check.

  T1 throughline validated: Cmd 7 vs 1 = 100% win in 1.4 turns. Cmd 6 vs 2 = 100% in 2.9 turns.
    Double impact: higher command = more dice + slower morale erosion.

  Remaining: true simultaneous resolution, freed-attacker, multi-unit, cavalry, per-unit grid.
