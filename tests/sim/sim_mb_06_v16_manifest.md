# SIM-MB-06 v16 — Manifest

**Session:** 2026-05-13
**Iteration:** v15 → v16
**File:** `tests/sim/sim_mb_06_v16.py`

## Summary

v16 implements two architectural changes: **continuous effective_size** from TroopCount (G-3a) and **lethality recalibration** for multi-turn battles (G-3b). The sim now models one engagement turn (3 phases = 18 ticks) within a multi-turn battle structure.

## Architecture: 4-level zoom

1. **Peninsula** — faction-level grand strategy, all territories visible
2. **Territory** — terrain, army positioning, battle turns (5-8 per battle)
3. **Battlefield/engagement** — 25×21 grid PER UNIT, tactical combat. **The sim models this level.**
4. **Scene** — duels, thread operations, personal-scale encounters

Each battle turn at level 2 triggers up to 3 phases of engagement per unit pair at level 3. Adjacent ally units at one depth join (2v1, 2v2, 3v1). Auto-resolve available.

## Key changes

### G-3a: Continuous effective_size

`effective_size = hp / h_per_size` (float, not floored). Pool formula: `floor(min(effective_size, Command) + Command + penalties)`. A unit at 280/400 troops fights at effective_size 2.8 — pool degrades continuously as casualties mount, not in step-function drops at Size boundaries.

[canonical: derived_stats architecture (2026-04-19) — TroopCount as granular health pool. "Player sees: Heavy Infantry — 4,428 / 5,000 (Size 4)". Engine runs continuous effective_size internally.]

### G-3b: Lethality recalibration

`LETHALITY_SCALE = 0.10` applied to all combat damage. Calibrated so one 3-phase engagement turn produces ~15% casualties per side (~12% winner, ~17% loser). Rout occurs at ~30% cumulative casualties across 2-3 battle turns.

`max_turns` default changed to 18 (3-phase cap per engagement turn). [canonical: Jordan direction — "limit of three phases per simultaneous engagement per turn"]

### G-3c: Casualty-percentage morale triggers

Replace integer Size-based triggers (too coarse at Size 4). Per-tick morale at `loss_pct >= 0.30`: -2/tick. At `loss_pct >= 0.50`: -3/tick. Floor drops to 0 at 30% casualties. [canonical: Jordan direction — "30% rout threshold"]

## Multi-turn battle validation

Tested with multi-turn orchestration loop (stamina_recovery=30 between turns):

| Metric | Value | Target |
|---|---|---|
| Per-turn loser casualties | ~17% | 10-15% |
| Per-turn winner casualties | ~14% | — |
| Turns to rout | 2.1 | 2-3 |
| Loser cumulative at rout | ~33% | ~30% |
| Winner cumulative at rout | ~23% | — |
| Rout rate | 100% | high |
| H5 RF win rate (multi-turn) | 75.5% | 50-65% (needs tuning) |

## Constants

| Constant | Value | Source |
|---|---|---|
| `LETHALITY_SCALE` | 0.10 | Tuning — ~15% casualties per 3-phase turn |
| `MORALE_LOSS_PCT_THRESHOLD` | 0.30 | Jordan direction — 30% rout threshold |
| `MORALE_HEAVY_LOSS_PCT_THRESHOLD` | 0.50 | Tuning — accelerated morale collapse |
| `max_turns` (default) | 18 | Canonical — 3-phase engagement cap per turn |

All v15 stamina constants retained unchanged.

## Known issues

1. **H5 RF wins 75.5% in multi-turn** — above 50-65% target. RF's depth advantage stacks too hard across turns. Needs formation-specific tuning.
2. **H1 mirror asymmetric** (A 43%) — subunit position reset between turns introduces side bias. Multi-turn orchestration needs proper re-engagement positioning.
3. **Winner/loser casualty ratio 1.4x** — historical is 2-5x. Pursuit after rout and cascade from adjacent units breaking (level-2 mechanics) are not yet modeled.
4. **Per-turn casualties ~17%** — slightly above 10-15% target. LETHALITY_SCALE may need further reduction to 0.08.
5. **Single-engagement battery (H1-H13) not meaningful** at max_turns=18 — most matchups draw within one turn. Battery needs redesign for multi-turn model.
6. **Grid is shared** (both units on one surface) — should be per-unit 25×21 grids with boundary interaction.

## Carried forward

- Multi-turn battle orchestrator (level-2 loop with proper state persistence)
- Per-unit grid architecture (25×21 per unit, not shared)
- Multi-unit engagements (2v1, 3v1 from adjacent allies)
- Pursuit damage after rout (level-2 mechanic)
- Rout cascade to adjacent units (level-2 mechanic)
- Auto-resolve option
- Scene-level zoom (duels, thread) at level 4
