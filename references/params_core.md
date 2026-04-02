<!-- version: v0.14 | sources: stage1_core_engine.md | last_updated: 2026-03-26 -->
<!-- STALE CHECK: If current ruleset version ≠ v0.14, halt and flag before using. -->

# params_core.md — Core Dice Engine

## Die Rule (d10)
| Face | Effect |
|------|--------|
| 1 | −1 success |
| 2–6 | 0 |
| 7–9 | +1 success |
| 10 | +2 successes (no extra die) |

Net successes = sum of all contributions (may be negative).

## TN Values
| Mode | TN | When |
|------|----|------|
| Controlled | 6 | Prepared, unhurried, favourable |
| Standard | 7 | Default |
| Desperate | 8 | Duress, exhaustion, existential threat |

Thread operations: TN 7 standard; TN 8 for Forced Resolution and Past-Oriented Pulling.

## Obstacle Scale
| Ob | Difficulty |
|----|-----------|
| 1 | Routine |
| 2 | Moderate |
| 3 | Difficult |
| 5 | Entrenched |
| 8 | Structural |
| 10 | Foundational (cap; no stacking above 10) |

Ob minimum: 1. No modifier may reduce Ob below 1.

## Degrees of Success
| Degree | Condition |
|--------|-----------|
| Overwhelming | Net ≥ 2× Ob (+1 Momentum) |
| Success | Net ≥ Ob |
| Partial | Net > 0 but < Ob |
| Failure | Net ≤ 0 |

Ob 10 exception: Overwhelming unavailable. Partial requires net ≥ 5.

## Momentum
- Range: 0–4
- Gain: Overwhelming success OR Belief achieved
- Spend: 1 Momentum = 1 automatic success (non-Thread rolls only)
- Reset: start of each session

## Pool Minimum
No penalty may reduce a pool below 1D. Ob penalties still apply at 1D.

## Expected Value (per die)
| TN | E[net] per die |
|----|---------------|
| 6 | 0.40 |
| 7 | 0.30 |
| 8 | 0.20 |

## Quick Reference — P(≥N net), TN 7
| Pool | E[Net] | P(≥1) | P(≥2) | P(≥3) |
|------|--------|-------|-------|-------|
| 4D | 1.3 | ~80% | ~50% | ~25% |
| 6D | 2.0 | ~92% | ~70% | ~45% |
| 8D | 2.6 | ~97% | ~82% | ~60% |
| 10D | 3.3 | ~99% | ~90% | ~73% |
| 12D | 4.0 | ~99% | ~95% | ~83% |

Full multi-TN tables: references/tn_full_tables.md (generate via dice-model Task 8 if absent).
