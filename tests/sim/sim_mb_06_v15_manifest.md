# SIM-MB-06 v15 — Manifest

**Session:** 2026-05-13
**Iteration:** v14 → v15
**Commit scope:** simulation
**File:** `tests/sim/sim_mb_06_v15.py`

## Summary

v15 implements **G-1 (stamina)** and **G-2 (rout-at-casualty-threshold)** on the phase-boundary hooks wired in v14. The implementation is minimalist: stamina affects combat pool only at exhaustion (-1 die), with phase-boundary morale checks for exhausted+damaged units. Per-tick morale logic is unchanged from v14.

**Primary outcome:** H5 (RF vs HS) enters target band (47.4% → 50.2%), fixing the only out-of-band test in v14's melee battery. One marginal regression: H7 (GL vs Line, 51.6% → 49.4%).

## Mechanisms

### G-1 Stamina

Unit-level stamina attribute (0-100). Three components:

1. **Per-tick drain:** -16 stamina per contact tick (both sides drain when contacts exist). Fresh units exhaust in 6.25 contact ticks without recovery.

2. **Phase-boundary recovery:** `STAMINA_RECOVERY_PER_RESERVE_RANK * (formation_depth - 1)` at each phase boundary. Formation depths at tier 3: RefusedFlank 7 rows (6 reserve, recovery 48), Line/Arrowhead 5 rows (4 reserve, recovery 32), Horseshoe 4 rows (3 reserve, recovery 24), GappedLine 3 rows (2 reserve, recovery 16).

3. **Pool penalty:** -1 die when exhausted (stamina = 0). No intermediate penalties. Deeper formations maintain full combat pool longer, dealing marginally more damage across the later ticks.

### G-2 Rout-at-casualty-threshold

Phase-boundary morale check for exhausted units:

- **`morale_check_phase`:** if exhausted AND casualty% >= 20%, morale floor drops to 0 and unit takes -1 morale (within canonical -3 cap).
- **`rout_resolution`:** if morale <= 0, unit routs. Pursuit damage = opponent Power as flat HP loss.
- **Per-tick morale:** unchanged from v14 (size thresholds, floor = 1).

## Constants

All stamina constants are tuning parameters — no canonical source specifies stamina values.

| Constant | Value | Rationale |
|---|---|---|
| `STAMINA_MAX` | 100 | Round number; percentage-style |
| `STAMINA_DRAIN_PER_CONTACT_TICK` | 16 | 6.25 ticks to exhaust without recovery |
| `STAMINA_RECOVERY_PER_RESERVE_RANK` | 8 | RF net -48/phase vs GL net -80/phase |
| `STAMINA_POOL_THRESHOLDS` | [(1, 0)] | No penalty while any stamina remains |
| `STAMINA_EXHAUSTED_POOL_PENALTY` | -1 | Minimal: ~2-3% shift without disrupting geometry |
| `ROUT_FLOOR_LOSS_PCT` | 0.20 | 20% casualties to lose floor (when exhausted) |
| `ROUT_EXHAUSTION_MORALE_HIT` | 1 | -1 morale/phase boundary when exhausted |
| `MORALE_PHASE_CAP` | 3 | [canonical: mass_battle_v30.md A.4] |

## Tuning history (5 iterations)

| # | Pool penalty | Morale | In-band | Issue |
|---|---|---|---|---|
| 1 | (80,0)(60,-1)(40,-2)(20,-3) exh=-4 | Casualty per-tick | 7/13 | Shallow formations crushed |
| 2 | (80,0)(50,-1)(20,-2) exh=-3 | stm<20 per-tick | 7/13 | GL still too penalized |
| 3 | Same | Casualty at 15%/35% | 7/13 | Casualty triggers dominate geometry |
| 4 | Same | Gated on stm<50 | 4/13 | Over-corrected; draws exploded |
| **5** | **(1,0) exh=-1** | **v14-identical per-tick** | **11/13** | **Best balance** |

## Battery (n=500, seed_base=1000000)

| Test | Matchup | v15 | v14 | Delta | Target | Status |
|------|---------|-----|-----|-------|--------|--------|
| H1 | Line vs Line | 51.8% | 51.6% | +0.2 | 45-55 | ✓ |
| H2 | Arrow vs Line | 55.2% | 54.4% | +0.8 | 50-65 | ✓ |
| H3 | HS vs Line | 62.2% | 61.6% | +0.6 | 50-65 | ✓ |
| H4 | HS vs Arrow | 47.0% | 48.2% | -1.2 | 40-60 | ✓ |
| **H5** | **RF vs HS** | **50.2%** | **47.4%** | **+2.8** | **50-65** | **FIXED** |
| H6 | RF vs Line | 58.2% | 56.8% | +1.4 | 45-60 | ✓ |
| **H7** | **GL vs Line** | **49.4%** | **51.6%** | **-2.2** | **50-65** | **← OUT** |
| H8 | GL vs Arrow | 48.0% | 49.6% | -1.6 | 45-60 | ✓ |
| H9 | Line vs Arrow | 48.0% | 48.2% | -0.2 | 35-50 | ✓ |
| H10 | Line vs HS | 39.2% | 37.6% | +1.6 | 35-50 | ✓ |
| H11 | Arrow vs HS | 55.6% | 51.0% | +4.6 | 40-60 | ✓ |
| R1 | Ranged vs Line | 22.2% | 22.0% | +0.2 | 30-50 | ← OUT (both) |
| R3 | Ranged mirror | 45.4% | 44.0% | +1.4 | 45-55 | **FIXED** |

**v14: 10/13 → v15: 11/13** (net +1)

**Rout rate: 0%.** Battles end by HP destruction. Phase-boundary morale fires but can't push morale to 0 before HP=0 at current lethality.

## Key design insight

**G-3 does NOT fall out of G-1+G-2** (contradicts audit prediction). Per-tick lethality (~3 HP/tick on 20 HP units) kills in 7-8 ticks. Stamina differential needs 12+ ticks (2+ phases). More aggressive penalties destabilize geometry. The minimalist -1 die works by subtly shifting damage rates across many ticks.

## Known issues

1. **H7 regression:** GL (3 rows) exhausts faster than Line (5 rows). Confirmed at n=2000: 50.2% → 47.6%. Fix: adjust GL geometric advantage in a later cycle.
2. **R1:** 22.2% — out at these seeds in both v14 and v15. Not a v15 regression.
3. **0% rout rate:** Requires G-3 (lethality reduction) to extend battles into phase 2+.

## Carried forward

- **G-3 lethality recalibration** — prerequisite for meaningful rout
- **H7 fix** — GL geometric advantage reinforcement
- **G-7 Rally** — `rally_check` hook empty
- **G-8 Reform** — `reform_check` hook empty
- **G-9 Threadwork** — `threadwork_check` hook empty
- **G-11 Cavalry** — charge cycle, Speed attribute, pursuit mechanics
