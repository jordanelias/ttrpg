# Phase 13 — Intermediating Layer Test (Reframing 2 Floor Analysis)

**Date:** 2026-05-17
**Sim:** `tests/sim/scripts/phase13_layers.py`
**Baseline:** Phase 10 best-stack (undoubled pool + 1/End Ob + Disarm + canonical stam + STR-strong)
**Tests:** Three intermediating layer candidates from planning_v0.md, each in isolation (M1/M2/M3 not included).

## Question

Does an intermediating layer between pool comparison and damage compress within-class Agi dominance from baseline 99% to target 60–70%? Tests structural defect identification from planning_v0.md.

## Layers tested

- **Layer A — Posture/Composure track.** Net successes drain opponent's Posture (Steady → Pressed → Reeling → Broken). Broken = Vulnerable for one round. Strike during Vulnerability deals direct HP at 2× damage modifier. POSTURE_NET_PER_STEP=1.0; POSTURE_RECOVERY_PER_BREATH=1.
- **Layer B — Advantage position track.** Single shared variable position (0–20, mid 10). Discrete exchange wins: 1 position toward winner per round (regardless of net magnitude). Position 0/20 = match decided.
- **Layer C — Stamina-primary.** Net successes drain opponent's Stamina at 2/net. HP damage only fires when net ≥ 3 OR target is Spent. Spent target takes 2.5× damage. Stamina-out triggers Spent state (not immediate loss).

## Results (N=2000 per matchup)

```
Matchup                                              none    A_post   B_pos   C_stam
Calibration: Strong vs Strong                       48.0%   24.8%   26.9%   41.4%
Calibration: Fast vs Fast                           47.4%   23.4%   25.1%   42.5%

Fast (Agi6) vs Strong (Agi3)   [within-class gap]   99.1%   36.3%   83.2%   87.7%
Fast vs Tough (Agi3 End6)      [End-investment]     76.3%   28.0%   20.9%   56.7%
Fast vs Mighty-light (STR7)    [F3 gap]             92.8%   36.7%   82.2%   77.7%
Fast vs Titan (heavy)          [cross-class]        13.5%   25.1%   18.0%   28.5%
Balanced (Agi5 STR5) vs Fast   [balanced build]      2.9%   10.1%    9.2%   17.2%
```

## Findings

### F1 — Layer A inverts within-class dominance

Within-class Fast-vs-Strong at 36.3% Fast (Strong wins ~64%). Layer A doesn't just compress Agi-dominance — it rebalances toward STR/End. STR-strong bonus dice (Strong STR 4 → +1 die on Strike) become more valuable per Strike when each Strike contributes to Posture damage, and Vulnerability hits fire at fixed multiplier. STR investment compounds; Agi pool advantage doesn't. This is a structural rebalancing, not a tuning issue.

**Implication:** Layer A doesn't preserve archetype hierarchy — Strong/Tough/Mighty become equally or more viable than Fast. May be a feature (cross-class diversity) or a bug (player-character viability of Agi-builds reduced) depending on design intent.

### F2 — Layer B mathematically floors dominance

Discrete-exchange-wins model converts linear pool-to-damage to binomial pool-to-win-frequency. Within-class Fast wins 83% (compressed from 99%). The compression is structural: pool advantage controls *probability* of winning a single exchange, not the *magnitude* of advantage in that exchange. Bounded effect; ~85% is approximate ceiling for this implementation.

**Implication:** Layer B is the cleanest mathematical compression. To hit 60-70% target, exchange-frequency advantage must be further reduced — possibly via tie-rate (close net successes produce no movement) or via Stamina-cost making sustained pressure expensive.

### F3 — Layer C compresses modestly

Within-class Fast wins 87.7% (compressed from 99%). Layer C's threshold-and-drain mechanism preserves most current dynamics; HP damage rare until target is Spent. Compression from 99 → 88 confirms scaling-defect identification: even partial removal of linear damage path produces measurable compression.

**Implication:** Layer C is the most conservative path. Easiest to implement (smallest deviation from current canon); least transformative.

### F4 — All three layers show calibration draw issues

Layers A and B show calibration wins near 25%/25%, implying ~50% draws in symmetric matchups. Layer C is closer to ideal at 41-43% per side. Draw rates reflect that the layer mechanic + max_rounds=40 cap doesn't always produce decisive resolution in evenly-matched duels.

**Implication:** Tuning to hit 60-70% target is sensitive. None of the layers as currently tuned hit the target cleanly. The structural mechanisms are validated; the magnitudes need iteration.

### F5 — Cross-class (Fast vs Titan) results vary

Baseline: 13.5% Fast (heavy dominates 86%). Layers:
- A: 25.1% — moderate compression of heavy dominance
- B: 18.0% — Light still significantly disadvantaged
- C: 28.5% — moderate compression

None of the layers alone solve cross-class dominance the way M1 (Reach gate, Phase 11) does. Layers address pool-to-damage scaling, not weapon-class-vs-armor-class mismatch.

**Implication:** Cross-class balance requires separate mechanic (reach gate, weapon-keyed primary, or similar). Intermediating layer addresses within-class scaling only.

### F6 — Balanced builds remain non-viable across all layers

Phase 10 baseline: 2.9% Balanced vs Fast. Layers raise to 10–17%. Forced specialization persists. Layer addressing balanced-build viability would need to ALSO restore some advantage for moderate-attribute distribution — not addressed by any layer here.

## Three Readings

**Reading A — Layer is the right shape but tuning sensitive.** Phase 13 shows structural compression works in all three layers. Iteration on magnitudes (POSTURE_NET_PER_STEP, position win threshold, HP_DAMAGE_THRESHOLD) could land 60-70% target. Phase 14 would tune.

**Reading B — Layer alone is insufficient; needs companion mechanic.** Cross-class dominance (F5) and balanced-build non-viability (F6) persist across all layers. Intermediating layer addresses scaling; reach gate addresses range; weapon-keyed addresses archetype. Multiple mechanisms compose.

**Reading C — Layer is structurally incompatible with current d10 pool grammar at high pool magnitudes.** At Combat Pool 11–17D magnitudes, even bounded compression mechanisms leak — variance is too high relative to bound. Reform may need to attack pool magnitude (further undouble, halve baseline) rather than mediate output.

## Open canonical questions

1. Does Jordan accept Layer A's STR/End rebalancing as intentional or as defect?
2. Is Layer B's binomial floor acceptable design, or is mathematical compression too crude?
3. Layer C's modest compression (94→88) — is this sufficient given Reframing 2 already validated?
4. Should companion mechanisms (M1 reach gate, C2 weapon-keyed) layer with the chosen intermediating layer, or is layer alone sufficient?
5. Reading C suggests pool magnitudes themselves are the deeper defect. Worth testing baseline + halved Combat Pool magnitudes separately?

## Sim limitations

- Heuristic AI; "smart" strike-when-vulnerable rule applied but more sophisticated AI (pattern reads, predictive strikes) would shift results.
- Tuning is first-pass; magnitudes per layer untuned for target.
- Layer A AI Take Breath threshold at posture=3 is brittle; tuning to 2 changes results substantially.
- Layer C Spent state mechanic is binary; graduated stamina exhaustion (Tired/Winded/Spent) untested.
- max_rounds=40 cap; longer fights would reduce draw rates.

## Status

Three intermediating layer candidates tested in isolation. All three demonstrate structural compression of within-class Agi dominance from 99% baseline. None as currently tuned hit 60-70% target cleanly. Tuning sensitivity is high; structural effects are real.

Decision needed: Jordan to choose between Layer A (rebalancing toward STR/End), Layer B (binomial floor), Layer C (modest compression preserving current dynamics), or reject all layer-based approaches per Reading C.

## Related ledger entries

- ED-864 (combat C4 direction)
- ED-838 (Phase 8 Agi dominance baseline)
- ED-839 (Phase 10 reform baseline)
- planning_v0.md (root cause identification + Layer candidates)
