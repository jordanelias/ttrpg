session_id: 2026-05-13_v15_v18_full_cycle
session_close: 2026-05-13
phase: sim-mb-06
status: closed
last_stage: v18-committed-5b7aafa_discipline_continuous_effective_size
next_action:
  skill: valoria-simulator
  task: D-4 pursuit damage; D-5 rout cascade; D-8 multi-turn battery band recalibration
blockers: []
commits: [651bf7d, 55952ac, f3d94ef, ef7e8ec, 5b7aafa]
notes: |
  ## Five commits — v15 through v18 + audit

  v15 (651bf7d) — G-1 stamina + G-2 rout hooks. Battery 11/13.
  v16 (55952ac) — continuous effective_size + LETHALITY_SCALE=0.10.
  v16 audit (f3d94ef) — 10 gaps identified (0 P1, 6 P2, 4 P3).
  v17 (ef7e8ec) — multi-turn orchestrator + between-turn rules + D-7 fix.
  v18 (5b7aafa) — discipline_check_phase at phase boundary (D-6).

  ## Architecture (confirmed by Jordan)

  4 zoom levels: Peninsula → Territory → Battlefield (25x21 per unit) → Scene.
  3-phase cap per engagement turn. 5-8 turns per battle.
  Time is absolute. 30% cumulative casualties for rout.
  Multi-turn compounding is correct behavior (strategic composition > tactics).
  Battery bands need recalibration for multi-turn model.

  ## Multi-turn results (n=80, v18)

  H1 Line/Line: 52.5% (mirror). H3 HS/Line: 75% (envelopment advantage).
  H5 RF/HS: 72.5% (depth advantage). H7 GL/Line: 51.2%.
  Loser casualties ~33% at rout. Winner ~24%. Ratio 1.4x.
  Battles resolve in ~2 turns.

  ## Remaining gaps (from v16 audit)

  D-4 pursuit damage: NOT YET — diverges winner/loser casualty ratio
  D-5 rout cascade: NOT YET — requires level-2 orchestrator
  D-8 battery bands: needs design decision — multi-turn amplifies advantages
  D-2 per-unit grid: architecture (later)
  D-3 multi-unit: architecture (later)
  D-10 pool sensitivity: accepted as-designed (generalship dominance axiom)
