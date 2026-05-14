# Valoria Simulation Coverage Matrix

## sim_mb_06_v16 — G-3 continuous effective_size + lethality recalibration committed
- Date: 2026-05-13
- Scope: mass combat simulation v15→v16
- Mode: G (Incremental Build Protocol) — architectural change + lethality recalibration
- Status: committed
- Changes: continuous effective_size (float, not floored); LETHALITY_SCALE=0.10 for ~15%
  casualties per 3-phase engagement turn; casualty-percentage morale triggers at 30%/50%;
  max_turns default 18 (3-phase cap per engagement turn)
- Architecture: 4-level zoom (Peninsula → Territory → Battlefield → Scene).
  Sim models Battlefield level. Multi-turn battle: 5-8 turns × 3 phases per engagement.
  Per-unit 25×21 grid (not shared). Adjacent allies join at one depth.
- Findings: multi-turn rout at ~33% cumulative casualties after 2 turns.
  Winner casualties ~23%, loser ~33%. 100% rout rate.
  H5 RF wins 75.5% in multi-turn (above target — depth stacking).
  Per-turn battery not meaningful at max_turns=18 (most matchups draw).
  Winner/loser ratio 1.4x (historical 2-5x — needs pursuit/cascade).

## audit_sim_mb_06_v16 — formula validation + gap detection
- Date: 2026-05-13
- Scope: v16 audit (Mode A + Mode D)
- Status: committed
- Findings: 10 gaps (0 P1, 6 P2, 4 P3). Pool formula validated across boundary values.
  Phase-boundary morale check redundant with per-tick triggers (D-7).
  Multi-turn orchestrator is priority for v17 (D-1, D-9).

## sim_mb_06_v17 — multi-turn orchestrator + D-7 morale separation
- Date: 2026-05-13
- Scope: mass combat simulation v16→v17
- Mode: G — multi-turn battle loop, between-turn state rules, morale concern separation
- Status: committed
- Changes: run_multi_turn_battle orchestrator (D-1), between_turn_recovery (D-9),
  morale_check_phase separated from per-tick casualty triggers (D-7).
  Between turns: stamina +30, morale +0, HP persists, discipline persists.
- Multi-turn battery (n=100): geometric advantages compound across turns.
  H3 HS/Line 79%, H5 RF/HS 74% — higher than single-turn bands.
  Band recalibration needed for multi-turn model (design decision, not tuning).
- Winner casualties ~23%, loser ~33%. Ratio 1.4x. Battles resolve in ~2 turns.

## sim_mb_06_v18 — D-6 discipline with continuous effective_size
- Date: 2026-05-13
- Scope: mass combat simulation v17→v18
- Mode: G — D-6 fix: discipline degradation at phase boundary using cumulative loss
- Status: committed
- Changes: discipline_check_phase hook wired into phase_boundary (after stamina, before morale).
  Cumulative effective_size loss checked against DISCIPLINE_LOSS_THRESHOLD=1.0, asymmetric.
  Per-tick integer-Size discipline check removed (never fired at LETHALITY_SCALE=0.10).

## sim_mb_06_v19 — bottom-up TroopCount HP, no LETHALITY_SCALE
- Date: 2026-05-13
- Scope: mass combat simulation v18→v19
- Mode: G — bottom-up architectural change
- Status: committed
- Changes: HP = TroopCount = Size * BLOCK_SIZE (400 at Company scale).
  LETHALITY_SCALE removed entirely. Damage = soldier casualties from dice.
  Casualty rates emerge from pool/TN/DR mechanics: ~7% per 3-phase turn.
  4 turns to rout at ~31% cumulative. No tuning knobs.
- Multi-turn battery (n=80): H1 58.8%, H3 83.8%, H5 75.0%, H7 45.0%.
  Winner ~23%, loser ~31%. Ratio 1.4x. Battles 4 turns.

## v19 pursuit fix — Standard infantry cannot pursue per §A.12
- Date: 2026-05-13
- Scope: D-4 pursuit canonical compliance
- Changes: rout_resolution no longer applies pursuit damage from Standard infantry.
  Pursuit is a level-2 mechanic for Fast units only (canonical: §A.12).
