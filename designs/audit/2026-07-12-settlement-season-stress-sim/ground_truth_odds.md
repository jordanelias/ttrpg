# Ground-truth resolver odds (computed from existing repo code)

Source: `skills/valoria-dice-model/valoria_dice.py` (dice_pool, exact convolution on its die model,
cross-checked vs its `outcome_probs` Monte-Carlo, Δ≤0.003) and `sim/autoload/sigma_leverage.py`
`p_success()` closed-form (d_sigma). NOT agent estimates — canonical engine math.

## A. dice_pool — P(success = net ≥ Ob).  Die: 1→−1, 10→+2, ≥TN→+1.

### TN 6
| pool | Ob1 | Ob2 | Ob3 | Ob4 |
|---|---|---|---|---|
| 3 | 76% | 50% | 24% | 7% |
| 4 | 83% | 62% | 38% | 17% |
| 5 | 87% | 71% | 50% | 29% |
| 6 | 90% | 78% | 60% | 40% |
| 7 | 92% | 83% | 68% | 50% |
| 8 | 94% | 86% | 74% | 59% |
| 9 | 95% | 89% | 80% | 66% |
| 10 | 96% | 92% | 84% | 72% |
| 11 | 97% | 93% | 87% | 77% |
| 12 | 98% | 95% | 90% | 82% |
| 13 | 98% | 96% | 92% | 85% |
| 14 | 98% | 97% | 93% | 88% |
| 15 | 99% | 97% | 95% | 90% |
| 16 | 99% | 98% | 96% | 92% |
| 17 | 99% | 98% | 97% | 93% |
| 18 | 99% | 99% | 97% | 95% |

### TN 7
| pool | Ob1 | Ob2 | Ob3 | Ob4 |
|---|---|---|---|---|
| 3 | 68% | 40% | 17% | 5% |
| 4 | 75% | 51% | 28% | 12% |
| 5 | 80% | 60% | 38% | 20% |
| 6 | 83% | 67% | 47% | 28% |
| 7 | 86% | 73% | 55% | 36% |
| 8 | 89% | 77% | 61% | 44% |
| 9 | 91% | 81% | 67% | 51% |
| 10 | 92% | 84% | 72% | 57% |
| 11 | 93% | 86% | 76% | 63% |
| 12 | 94% | 89% | 80% | 68% |
| 13 | 95% | 90% | 83% | 72% |
| 14 | 96% | 92% | 85% | 76% |
| 15 | 97% | 93% | 87% | 79% |
| 16 | 97% | 94% | 89% | 82% |
| 17 | 97% | 95% | 91% | 84% |
| 18 | 98% | 96% | 92% | 86% |

## B. d_sigma — domain-action / Directive.  P = p_success(base_Ob, pool, net_σ), TN7.
net_σ from advantage levels: minor .25 / moderate .5 / strong .75 / major 1.0 (negative = disadvantage).

### base_Ob 2
| pool | −2 disadv | neutral | +moderate | +major | major+minor |
|---|---|---|---|---|---|
| 3 | 14% | 28% | 46% | 62% | 71% |
| 5 | 31% | 50% | 69% | 81% | 87% |
| 7 | 46% | 65% | 81% | 89% | 94% |
| 9 | 57% | 75% | 87% | 94% | 96% |
| 12 | 70% | 84% | 93% | 97% | 98% |

### base_Ob 3
| pool | −2 disadv | neutral | +moderate | +major | major+minor |
|---|---|---|---|---|---|
| 3 | 4% | 10% | 21% | 34% | 44% |
| 5 | 15% | 29% | 47% | 62% | 72% |
| 7 | 28% | 46% | 65% | 78% | 85% |
| 9 | 41% | 60% | 77% | 87% | 92% |
| 12 | 57% | 74% | 87% | 94% | 96% |

### base_Ob 4
| pool | −2 disadv | neutral | +moderate | +major | major+minor |
|---|---|---|---|---|---|
| 3 | 1% | 2% | 6% | 13% | 19% |
| 5 | 5% | 13% | 26% | 40% | 51% |
| 7 | 15% | 29% | 47% | 62% | 72% |
| 9 | 26% | 43% | 62% | 76% | 84% |
| 12 | 42% | 61% | 78% | 88% | 92% |
