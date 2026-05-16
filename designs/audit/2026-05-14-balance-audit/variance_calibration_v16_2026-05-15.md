# Phase 1a — Variance Calibration Report
**Date:** 2026-05-15
**Deliverable:** `designs/audit/2026-05-14-balance-audit/variance_calibration_v16_2026-05-15.md`

## §1 Objective

Configure v15 quasibinomial to match v12c VFIVE degree distribution within 2pp across all game-relevant matchups, per integration plan v3 §5 Phase 1a.

## §2 VFIVE Specification

**Source:** `mc_v4.py` line 33
```
VFIVE = [-1, 0, 0, 0, 0, 0, 1, 1, 1, 2]
```

Per-die distribution: P(-1)=0.1, P(0)=0.5, P(1)=0.3, P(2)=0.1.
Mean = 0.4/die, Variance = 0.64/die, Range = [-1, +2]/die.

Sum of n dice: integer-valued, range [-n, 2n], computed exactly via PMF convolution.

**Degree thresholds** (`mc_v4.py` lines 38-41):
- Failure: net ≤ -1
- Partial: net = 0
- Success: 1 ≤ net ≤ 2
- Overwhelming: net ≥ 3

## §3 Quasibinomial Specification

**Source:** `mc_v15.py` lines 30-40

```python
mean = pool * p_hit
var = dispersion * pool * p_hit * (1 - p_hit)
sd = sqrt(var)
successes = gauss(mean, sd)  # clamped to [0, pool]
```

**Degree thresholds** (`mc_v15.py` lines 42-49): equivalent at integer boundaries.

**Plan-derived params** (integration plan v3 §3.2): p_hit=0.4, φ=2.67 (matching VFIVE mean and variance per die).

## §4 Results — Plan-Derived Parameters (p=0.4, φ=2.67)

### §4.1 Four-matchup comparison (plan §5 Phase 1a step 1-3)

| Pool | Ob | Degree | VFIVE (exact) | QB clamped | Δ |
|---|---|---|---|---|---|
| 4 | 4 | Failure | 88.14% | 93.31% | +5.17pp ⚠ |
| 4 | 4 | Partial | 8.07% | 6.69% | -1.38pp |
| 4 | 4 | Success | 3.66% | 0.00% | -3.66pp ⚠ |
| 4 | 2 | Failure | 48.82% | 59.86% | +11.04pp ⚠ |
| 4 | 2 | Partial | 23.24% | 21.04% | -2.20pp ⚠ |
| 4 | 2 | Success | 24.15% | 19.09% | -5.06pp ⚠ |
| 4 | 2 | Overwhelming | 3.79% | 0.00% | -3.79pp ⚠ |
| 5 | 3 | Failure | 62.00% | 71.18% | +9.18pp ⚠ |
| 5 | 3 | Partial | 18.20% | 15.63% | -2.57pp ⚠ |
| 5 | 3 | Success | 17.04% | 13.19% | -3.85pp ⚠ |
| 6 | 4 | Failure | 71.86% | 79.27% | +7.41pp ⚠ |
| 6 | 4 | Partial | 13.95% | 11.48% | -2.47pp ⚠ |
| 6 | 4 | Success | 12.16% | 9.24% | -2.91pp ⚠ |

**Max deviation: 11.04pp.** Far exceeds 2pp threshold.

### §4.2 Signed quasibinomial (plan step 5 — remove floor clamp)

Removing the [0, pool] clamp does not help: max deviation still 11.04pp at p=0.4 φ=2.67. The mismatch is distribution shape, not clamping.

## §5 Results — Optimized Parameters

### §5.1 Narrow optimization (4 matchups only)

Optimizer found p=0.4950, φ=2.5238 achieving max 1.69pp across the 4 plan matchups (signed QB). This is within 2pp.

### §5.2 Wide-range verification (26 matchups, pool 2-8, Ob 1-6)

The same parameters fail at pool 2 Ob 1 (8.36pp) and pool 8 Ob 4 (5.38pp).

Re-optimization over all 26 matchups: best achievable is p=0.5089, φ=2.4997 at **7.36pp** max deviation.

### §5.3 Failure modes

Two structural causes prevent any quasibinomial from matching VFIVE:

**1. Small-pool discreteness.** At pool 2-3, VFIVE sums are highly discrete (pool 2: only 7 possible values from -2 to +4). No continuous Gaussian can match a 7-point PMF within 2pp across all degree bins.

**2. Range asymmetry.** VFIVE per-die range is [-1, +2] — maximum sum is 2×pool. Clamped quasibinomial maximum is pool. For pool 3 Ob 1: VFIVE has 5.2% Overwhelming (net ≥ 3 requires sum ≥ 4, achievable up to max 6), but clamped QB can never exceed net = pool - Ob = 2 → 0% Overwhelming. Even signed QB is structurally disadvantaged because the Gaussian tail has different shape from the true PMF tail.

## §6 Decision

Per plan §5 Phase 1a step 6: quasibinomial fundamentally cannot match VFIVE within 2pp across game-relevant matchups. **VFIVE sampling fallback required.**

## §7 VFIVE Sampling Fallback Design

### §7.1 Mechanism

Replace `quasibinomial_successes()` with `vfive_roll()` in v16:

```python
VFIVE = [-1, 0, 0, 0, 0, 0, 1, 1, 1, 2]  # [canonical: mc_v4.py line 33]

def vfive_roll(pool):
    """VFIVE sampling with probabilistic rounding for fractional pools.
    [canonical: integration_plan_v3 §5 Phase 1a step 6]
    
    Integer pool: sum of pool VFIVE dice.
    Fractional pool: floor(pool) dice + Bernoulli(frac) extra die.
    Example: pool=4.3 → 4 dice always + 5th die with 30% probability.
    """
    n = int(pool)
    frac = pool - n
    if frac > 0 and random.random() < frac:
        n += 1
    return sum(random.choice(VFIVE) for _ in range(max(1, n)))
```

### §7.2 Properties

- Integer pools: identical to v12c `roll_pool()`.
- Fractional pools: expected value = pool × 0.4 (same as VFIVE mean × expected dice count). Variance interpolates linearly between floor and ceil pools.
- Negative outcomes preserved: correctly models VFIVE's -1 face.
- Degree thresholds: use v4 integer thresholds (`resolve_degree` unchanged).

### §7.3 Fractional pool validation

v15 produces fractional pools in several places (e.g., `pool = church.I + ci / 10.0`). The probabilistic rounding preserves expected value:

```
E[vfive_roll(4.3)] = 0.7 × E[sum of 4 dice] + 0.3 × E[sum of 5 dice]
                   = 0.7 × 1.6 + 0.3 × 2.0
                   = 1.12 + 0.60 = 1.72
                   = 4.3 × 0.4 ✓
```

### §7.4 Scope of change in v16

1. Add `vfive_roll(pool)` function
2. Replace all `quasibinomial_successes(pool)` calls with `vfive_roll(pool)`
3. Keep `resolve_degree()` as v4 integer thresholds
4. All other v15 architecture unchanged

## §8 Blocking Decision

**Jordan Q4 (plan §9):** approve VFIVE sampling fallback in v15 architecture with probabilistic rounding for fractional pools?

Without approval, Phase 1b cannot proceed — dice distribution underpins all parameter sweep results.

## §9 Analytical Scripts

Phase 1a analysis code: `/home/claude/phase_1a_dice_calibration.py`
- Exact VFIVE PMF via convolution
- Quasibinomial analytical via normal CDF
- Monte Carlo validation (N=100,000)
- Exhaustive p/φ parameter search
- 26-matchup wide-range verification

All MC results validate against analytical within ±0.3pp (sampling noise at N=100k).


## §10 Jordan Decision — 2026-05-15

**Q4 resolved: Option B — keep quasibinomial.** VFIVE sampling fallback rejected. The game engine uses smooth quasibinomial distribution; VFIVE is legacy board-game heritage, not a constraint for the video game.

**Dice parameters for Phase 1b:** v15 defaults (p=0.5, φ=1.0). No dice code changes. Phase 1b parameter sweep compensates via game parameters (consent rate, treaty lapse, RM decay, victory threshold, plus restored mechanics: RM world process, Altonian Reinforcements).

**Implication:** v12c's balanced parameter values (consent 0.28, lapse 0.90, etc.) were tuned to VFIVE. They are starting points for the sweep, not transfer targets. The sweep grid may need to be wider than planned if v12c params don't converge on quasibinomial.

**Phase 1a status:** COMPLETE. Deliverable accepted with this addendum. Phase 1b unblocked on dice.
