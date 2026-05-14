# Audit: SIM-MB-06 v16

**Date:** 2026-05-13
**Scope:** v16 formula validation (Mode A) + gap detection (Mode D)
**Canonical sources fetched:** mass_battle_v30.md, params/mass_combat.md, sim_mb_06_v16.py

## A. Formula Validation

### A1. Pool formula: `floor(min(effective_size, Command) + Command + penalties)`

| effective_size | Command | Discipline | Stamina | Pool | Notes |
|---|---|---|---|---|---|
| 4.00 | 4 | 5 | 100 | 8 | Full unit, fresh |
| 2.80 | 4 | 5 | 100 | 6 | 30% casualties |
| 2.00 | 4 | 5 | 100 | 6 | 50% casualties |
| 0.50 | 4 | 5 | 100 | 4 | 87.5% casualties |
| 0.01 | 4 | 5 | 100 | 4 | Near-dead |
| 4.00 | 4 | 5 | 0 | 7 | Exhausted |
| 2.80 | 4 | 5 | 0 | 5 | 30% casualties + exhausted |
| 4.00 | 4 | 3 | 100 | 7 | Low discipline |
| 4.00 | 1 | 5 | 100 | 2 | Low command |
| 4.00 | 4 | 0 | 100 | 0 | Discipline broken |

**Finding (D-10):** Command term dominates pool. At eff_size 0.01, pool still 4 (half of maximum). A near-dead unit fights at half strength because the general is alive. This IS correct per design axiom "Generalship dominates" — but means casualties have limited combat effect until rout.

**Finding:** `max(1, ...)` floor means pool never goes below 1 (except broken). Verified no negative pools. ✓

### A2. Damage scaling

`LETHALITY_SCALE = 0.10` applied to engagement + volley damage. HP is now float. Fractional accumulation verified: hp=14.3 → eff_size=2.86, pool=6. ✓

### A3. Morale triggers

| Loss % | Trigger | Floor | Ticks to rout (from morale 6) |
|---|---|---|---|
| 0-29% | none | 1 | cannot rout |
| 30-49% | -2/tick | 0 | 3 ticks |
| 50%+ | -3/tick | 0 | 2 ticks |

**Finding:** Morale collapse is rapid once threshold is crossed. 3 ticks from trigger to rout means ~3% additional casualties between trigger and rout. Total at rout: ~33%.

### A4. Phase-boundary morale check (redundancy)

**Finding (D-7):** `morale_check_phase` fires -1 morale when exhausted AND casualties >= 30%. But per-tick triggers already fire -2/tick at 30%. The phase-boundary check is redundant — minor acceleration (one extra -1 per 6 ticks), not a distinct mechanism. Recommend: separate concerns. Per-tick = casualty pressure. Phase-boundary = exhaustion-only pressure (no casualty gate).

## D. Gap Detection

| ID | Severity | Gap | Description |
|---|---|---|---|
| D-1 | P2 | Multi-turn state persistence | No orchestrator persists state across engagement turns. Between-turn stamina recovery ad hoc (+30, not canonicalized). |
| D-2 | P2 | Per-unit grid architecture | Sim uses shared grid. Should be 25×21 per unit with boundary interaction. |
| D-3 | P2 | Multi-unit engagements | No 2v1, 2v2, 3v1. Adjacent allies at one depth should join. |
| D-4 | P2 | Pursuit damage after rout | Flat Power damage. Should model pursuit across turns: Fast chase, Standard/Slow cannot. Historical casualty ratios diverge here. |
| D-5 | P2 | Rout cascade to adjacent units | §A.12 morale cascade not modeled. Requires level-2 orchestrator. |
| D-6 | P3 | Discipline degradation with continuous effective_size | Integer Size rarely changes in one turn at scale 0.10. Discipline may never degrade. Consider continuous threshold. |
| D-7 | P3 | Redundant phase-boundary morale check | Per-tick casualty triggers + phase-boundary exhaustion check both fire at same conditions. Separate concerns. |
| D-8 | P3 | Battery redesign needed | Single-turn battery draws at max_turns=18. Need multi-turn battery. |
| D-9 | P2 | Between-turn recovery rules | Stamina, HP, morale inter-turn recovery not canonicalized. Discipline persists (PP-712). |
| D-10 | P3 | Pool sensitivity to casualties | Command term dominates. 87% casualties → pool still 4/8. Intentional (generalship axiom) but limits casualty impact on combat effectiveness. |

## Priority

**v17:** D-1 (multi-turn orchestrator) + D-9 (between-turn rules) + D-7 (separate morale concerns) + D-8 (multi-turn battery)

**v18:** D-4 (pursuit) + D-5 (rout cascade)

**Architecture (later):** D-2 (per-unit grid) + D-3 (multi-unit)

**Accept as-designed:** D-10 (Command dominance is the design axiom)
