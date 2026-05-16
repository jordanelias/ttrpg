# Phase 5 sim — Continuous engine prototype + Phase 4 comparison

**Date:** 2026-05-15
**Sim:** `tests/sim/phase5_continuous_engine_2026-05-15.py`
**Trigger:** Jordan 2026-05-15 — accepted Path 3 (full continuous engine) to replace discrete d10 dice with Normal-distribution sampling.

---

## TL;DR

**The continuous engine works and is mathematically equivalent to discrete, BUT it does not solve the Agi-dominance problem.** Conditional Fast vs Strong win rate is 97.5% continuous vs 97.8% discrete — essentially identical.

**Implication:** the dominance problem is NOT caused by the dice mechanism. It's caused by the **doubling formula** `(Attr × 2) + H + 3`. Moving to continuous mapping resolves probability-table edge cases and enables fractional modifiers, but Agi-dominance persists because the pool-size GAP between Fast (17D) and Strong (11D) is the structural driver, regardless of how individual dice are computed.

---

## Sim A — Distribution Equivalence

Validated continuous engine produces statistically equivalent outputs to discrete d10 at canonical pool sizes:

| Pool | Discrete μ | Continuous μ | Discrete σ | Continuous σ | Δμ | Δσ |
|---|---|---|---|---|---|---|
| 5 | 2.018 | 1.990 | 1.792 | 1.780 | −0.029 | −0.012 |
| 8 | 3.206 | 3.191 | 2.256 | 2.241 | −0.015 | −0.015 |
| 11 | 4.382 | 4.390 | 2.662 | 2.656 | +0.009 | −0.005 |
| 14 | 5.609 | 5.598 | 2.991 | 2.969 | −0.011 | −0.022 |
| 17 | 6.790 | 6.785 | 3.296 | 3.283 | −0.005 | −0.013 |

Max deviation: |Δμ| = 0.029, |Δσ| = 0.022. **EQUIVALENT** — both well under 0.1 sanity threshold.

**Conclusion: continuous engine is a clean drop-in replacement.** The Normal(0.4N, 0.8√N) parameterization at TN 7 reproduces the discrete distribution to within sampling noise.

(Note: per-die mean is 0.4 in continuous, not 0.3 as the Phase 4 sim assumed. The Phase 4 calculation had an error — the correct per-die expected value at TN 7 is 0.1×(−1) + 0.5×0 + 0.3×1 + 0.1×2 = 0.4. Phase 4 conditional win rates are still valid; the absolute mean was just slightly off-calibration.)

## Sim B — Phase 4 Re-run on Continuous Engine

Same matchups, same builds, continuous engine. Compare against Phase 4 discrete results:

| Matchup | Discrete A\|dec (Phase 4) | Continuous A\|dec (Phase 5) | Δ |
|---|---|---|---|
| Fast vs Strong | 98.6% | 97.2% | −1.4pp |
| Fast vs Tough | 3.5% | 4.2% | +0.7pp |
| Strong vs Tough | 0.4% | 0.2% | −0.2pp |
| Fast+Tough vs Strong | 100.0% | 100.0% | 0 |
| Fast+Tough vs Tough | 98.3% | 99.5% | +1.2pp |

**Differences are within sampling noise.** Continuous engine reproduces Phase 4 results.

### Build-investment ROI (continuous)

| Build | Pool | Cond Win% vs Strong | Δ vs Agi 3 |
|---|---|---|---|
| Agi 3, End 4 | 11D | 50.0% | (baseline) |
| Agi 4, End 4 | 13D | 80.0% | +30.0pp |
| Agi 5, End 4 | 15D | 91.4% | +41.4pp |
| Agi 6, End 4 | 17D | 97.4% | +47.4pp |
| Agi 7, End 4 | 19D | 99.2% | +49.2pp |

ROI curve nearly identical to Phase 4 discrete (which showed Agi 7 at 99.5%). The continuous engine doesn't change the *shape* of the dominance curve.

## Sim C — Head-to-head at N=5000

| Engine | A win | B win | Draw | A\|dec |
|---|---|---|---|---|
| Discrete d10 | 14.5% | 0.3% | 85.2% | **97.8%** |
| Continuous | 18.2% | 0.5% | 81.4% | **97.5%** |

Δ conditional = −0.3pp. Statistical noise.

**The two engines produce indistinguishable balance outcomes at canonical pool formulas.**

---

## Finding: continuous engine doesn't solve dominance — doubling does

This is the operationally important result. **The hypothesis that continuous mapping would naturally resolve Agi-dominance via the absence of probability saturation is wrong.**

### Why my earlier reasoning was incomplete

I argued earlier that "continuous mapping removes the saturation problem because there's no threshold to saturate against." That's true at the level of P(≥1 success) — that probability stops saturating. But what determines combat outcomes isn't just "did you get at least 1 success" — it's the **contested margin**: your net successes minus opponent's defensive net successes.

For Fast (17D pool) vs Strong (11D pool), the expected pool gap is:
- Discrete: E[Fast net] − E[Strong net] = 6.8 − 4.4 = 2.4 net successes
- Continuous: same, 6.8 − 4.4 = 2.4

The 2.4-success expected margin is the same in both engines. Continuous didn't reduce it — it can't, because the formula determines the means.

### What the continuous engine DOES buy you

Even though it doesn't solve dominance, the change isn't wasted:

1. **Fractional Ob and TN work natively.** Decision D's question about weapon condition (+0.25 Ob style) can now be implemented with real mechanical effect.
2. **No probability-table edge cases.** Foundational Thread (Ob 12+) no longer becomes structurally Overwhelming-inaccessible. The continuous engine handles high-Ob smoothly.
3. **Continuous degree resolution.** Outcome magnitude is a real number, surfacing as a UI gauge instead of a degree table lookup.
4. **Simpler probability computation.** No discrete summation tables needed; engine code uses Normal sampling.
5. **Fractional modifiers throughout** (cover quality, weapon condition, terrain, etc.).

These are genuine wins. The continuous engine is worth adopting **for these reasons** — just not as a fix for the dominance problem.

### What ACTUALLY solves dominance

The structural driver is the doubling. Three options to address it:

**Option 1 — Drop doubling.** `Pool = Attr + H + 3` produces 4D–14D range. Fast (Agi 6) gets 11D; Strong (Agi 3) gets 8D. Gap: 3D, or 1.2 expected successes. Dominance would compress sharply.

**Option 2 — Pool cap.** Keep doubling; cap effective pool at e.g. 14D. Agi 5+ all get the same effective pool. Closes the gap at the top but preserves attribute scaling at low/mid range.

**Option 3 — Re-ratify PP-717 D2 softcap.** `min(Agi, 4) × 2 + max(0, Agi-4) + H + 3`. Same effect as Option 2 at the formula layer.

**Recommendation:** **Option 1 + continuous engine.** Drop the doubling AND adopt continuous mapping. The doubling solves dominance (pool range compresses to 4D–14D). The continuous engine solves probability-table edge cases AND enables fractional modifiers. Together they resolve more issues than either alone, with no overlap in what they fix.

Alternative: continuous engine + Option 2 (cap), if you want to keep doubled pool feel (big numbers, talent-dominant).

---

## Recommended next decisions

### Decision E — Adopt continuous engine?

Phase 5 validates this is mathematically equivalent and works in code. Adoption commits you to:
- Re-deriving canonical Ob values (mostly straightforward; they map cleanly)
- Re-deriving degree thresholds for continuous magnitude
- Re-running all sim infrastructure against continuous engine
- Documenting the engine change in `params/core.md`

### Decision F — Drop doubling, OR add pool cap, OR re-ratify softcap?

Tied to Decision E. Three paths for fixing dominance:
- **Drop doubling** (`Attr + H + 3`): smaller pools, talent-and-training equal weight, no cap needed
- **Pool cap** (`min(Attr×2 + H + 3, 14)`): keep big pools, hard ceiling
- **Re-ratify softcap** (`min(Attr,4)×2 + max(0,Attr-4) + H + 3`): the v22-v27 ratified path

---

## Sim limitations

Same as Phase 4 — strike-only, no Feint/ED/Distance/Init, 50/50 fixed split, single weapon × armour. The continuous engine doesn't fix these limitations; that's a separate sim cycle to run with full v9 chassis once mechanical decisions are made.

---

## Status

Phase 5 sim complete. **Key finding: continuous engine is viable and clean, but doesn't solve dominance alone.** Jordan to decide:
1. Adopt continuous engine (independently valuable)
2. Pick a dominance solution (doubling drop / pool cap / softcap re-ratify)
3. Possibly both
