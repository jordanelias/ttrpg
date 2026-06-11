# Sigma-Leverage Computation Results — 2026-06-11
Engine: canonical face rule, exact convolution (no Normal approx unless stated).

## T1 — P(Success-or-better), TN 7, by pool x Ob
| Pool | Ob1 | Ob2 | Ob3 | Ob5 | Ob8 | Ob13 | Ob16 | Ob20 |
|---|---|---|---|---|---|---|---|---|
| 5D | 79.8% | 60.0% | 38.0% | 8.3% | 0.1% | 0.0% | 0.0% | 0.0% |
| 6D | 83.5% | 67.0% | 47.0% | 14.2% | 0.6% | 0.0% | 0.0% | 0.0% |
| 7D | 86.4% | 72.6% | 54.7% | 20.8% | 1.5% | 0.0% | 0.0% | 0.0% |
| 8D | 88.7% | 77.2% | 61.4% | 27.8% | 3.1% | 0.0% | 0.0% | 0.0% |
| 9D | 90.5% | 80.9% | 67.1% | 34.8% | 5.4% | 0.0% | 0.0% | 0.0% |
| 10D | 92.1% | 83.9% | 72.0% | 41.5% | 8.5% | 0.1% | 0.0% | 0.0% |
| 12D | 94.4% | 88.5% | 79.6% | 53.7% | 16.4% | 0.3% | 0.0% | 0.0% |
| 14D | 95.9% | 91.8% | 85.1% | 63.8% | 26.0% | 1.2% | 0.1% | 0.0% |
| 17D | 97.5% | 94.9% | 90.6% | 75.5% | 41.1% | 4.4% | 0.5% | 0.0% |
| 22D | 98.8% | 97.7% | 95.6% | 87.5% | 63.2% | 16.2% | 3.9% | 0.3% |

## T2 — Sigma leverage (TN 7): effect of +1D vs +1 Ob on P(Success), and in sigma units
| Pool | P@Ob3 | +1D delta | +1Ob delta | +1D in sigma | +1Ob in sigma |
|---|---|---|---|---|---|
| 5D | 38.0% | +9.0pp | -18.2pp | 0.22sigma | 0.56sigma |
| 7D | 54.7% | +6.7pp | -18.5pp | 0.19sigma | 0.47sigma |
| 10D | 72.0% | +4.1pp | -14.8pp | 0.16sigma | 0.40sigma |
| 14D | 85.1% | +2.2pp | -9.4pp | 0.13sigma | 0.33sigma |
| 17D | 90.6% | +1.3pp | -6.4pp | 0.12sigma | 0.30sigma |

## T3 — TN shift (Binding ops TN 8 vs standard TN 7), P(Success) at Ob 3 and Ob 5
| Pool | TN7 Ob3 | TN8 Ob3 | TN7 Ob5 | TN8 Ob5 |
|---|---|---|---|---|
| 5D | 38.0% | 27.0% | 8.3% | 5.0% |
| 8D | 61.4% | 46.4% | 27.8% | 16.9% |
| 10D | 72.0% | 56.6% | 41.5% | 26.4% |
| 14D | 85.1% | 71.3% | 63.8% | 44.7% |
| 17D | 90.6% | 78.8% | 75.5% | 56.3% |

## T4 — Leap roll (TN 7): degree distribution, pools 2-12, Ob 2 (TS30-49) / Ob 1 (TS50+)
| Pool | Ob | Ovw | Succ | Part | Fail |
|---|---|---|---|---|---|
| 2D | 2 | 1% | 25% | 32% | 42% |
| 3D | 2 | 5% | 35% | 28% | 32% |
| 5D | 2 | 20% | 40% | 20% | 20% |
| 7D | 2 | 36% | 36% | 14% | 14% |
| 9D | 2 | 51% | 30% | 10% | 9% |
| 12D | 2 | 68% | 21% | 6% | 6% |
| 5D | 1 | 38% | 42% | 0% | 20% |
| 9D | 1 | 67% | 23% | 0% | 9% |
| 12D | 1 | 80% | 15% | 0% | 6% |

## T5 — Crisis arc end-state distribution (PP-194), by Close-Knot Bonds
Anchoring: 3 scenes, each Bonds TN7 Ob2; resolution pool = Bonds + successes, TN7 Ob3.
| Bonds | E[scenes won] | P(Coh4) | P(Coh3) | P(Coh1 retry) | P(NPC) |
|---|---|---|---|---|---|
| 1 | 0.30 | 0% | 2% | 43% | 55% |
| 2 | 0.78 | 0% | 15% | 50% | 35% |
| 3 | 1.20 | 2% | 28% | 46% | 25% |
| 4 | 1.54 | 5% | 38% | 39% | 18% |
| 5 | 1.80 | 10% | 43% | 33% | 14% |
| 6 | 2.01 | 16% | 45% | 27% | 11% |
| 7 | 2.18 | 22% | 45% | 23% | 9% |

## T6 — Discrete-exact vs continuous-Normal divergence at degree thresholds (TN 7)
Normal(0.4N, 0.8*sqrt(N)) as specified params/core Continuous Engine (no continuity correction stated).
| Pool | Ob | exact P(net>=Ob) | Normal P(net>=Ob) | abs diff | rel diff |
|---|---|---|---|---|---|
| 5D | 2 | 60.00% | 50.00% | 10.00pp | 17% |
| 5D | 3 | 38.00% | 28.81% | 9.20pp | 24% |
| 5D | 5 | 8.33% | 4.68% | 3.66pp | 44% |
| 5D | 8 | 0.13% | 0.04% | 0.09pp | 70% |
| 5D | 13 | 0.00% | 0.00% | 0.00pp | inf% |
| 7D | 2 | 72.61% | 64.73% | 7.89pp | 11% |
| 7D | 3 | 54.74% | 46.24% | 8.51pp | 16% |
| 7D | 5 | 20.83% | 14.93% | 5.89pp | 28% |
| 7D | 8 | 1.49% | 0.70% | 0.79pp | 53% |
| 7D | 13 | 0.00% | 0.00% | 0.00pp | 67% |
| 9D | 2 | 80.87% | 74.75% | 6.12pp | 8% |
| 9D | 3 | 67.12% | 59.87% | 7.25pp | 11% |
| 9D | 5 | 34.75% | 27.98% | 6.77pp | 19% |
| 9D | 8 | 5.43% | 3.34% | 2.09pp | 39% |
| 9D | 13 | 0.01% | 0.00% | 0.01pp | 69% |
| 12D | 2 | 88.54% | 84.38% | 4.16pp | 5% |
| 12D | 3 | 79.57% | 74.20% | 5.37pp | 7% |
| 12D | 5 | 53.65% | 47.12% | 6.53pp | 12% |
| 12D | 8 | 16.43% | 12.41% | 4.02pp | 24% |
| 12D | 13 | 0.33% | 0.15% | 0.18pp | 54% |
| 17D | 2 | 94.91% | 92.72% | 2.19pp | 2% |
| 17D | 3 | 90.61% | 87.53% | 3.08pp | 3% |
| 17D | 5 | 75.52% | 70.74% | 4.78pp | 6% |
| 17D | 8 | 41.08% | 35.80% | 5.28pp | 13% |
| 17D | 13 | 4.38% | 3.01% | 1.37pp | 31% |
| 22D | 2 | 97.66% | 96.50% | 1.16pp | 1% |
| 22D | 3 | 95.61% | 93.89% | 1.72pp | 2% |
| 22D | 5 | 87.53% | 84.44% | 3.09pp | 4% |
| 22D | 8 | 63.15% | 58.44% | 4.71pp | 7% |
| 22D | 13 | 16.17% | 13.15% | 3.02pp | 19% |

Worst absolute divergence: pool 5D Ob 2: exact 60.00% vs Normal 50.00%

## T7 — Opposing operations, symmetric practitioners (both meet/partial/fail), TN 7
Engagement mod: +floor(opp TPS/2) min 1, both sides. Pool 5+2*TPS approx not used — direct pool/Ob input.
| Pool | Base Ob | Eng.mod | P(meet) | P(part) | P(fail) | P(Shifting Object: both meet) |
|---|---|---|---|---|---|---|
| 11D | 3 | +1 | 63% | 31% | 7% | 39% |
| 13D | 3 | +2 | 59% | 36% | 5% | 35% |
| 17D | 3 | +4 | 53% | 44% | 3% | 28% |
| 13D | 5 | +2 | 32% | 63% | 5% | 10% |
| 17D | 8 | +4 | 8% | 90% | 3% | 1% |

## T8 — Fatigue throughput (deterministic; ED-694): ops per contact by Spirit, Dissolution-only vs Pulling-only
Threshold = Spirit*5; Leap entry 3; Dissolution 10/rd; Pulling 5/rd; ops/session cap = Focus-1.
| Spirit | Threshold | Max Dissolution rounds | Max Pulling rounds |
|---|---|---|---|
| 2 | 10 | 0 | 1 |
| 3 | 15 | 1 | 2 |
| 4 | 20 | 1 | 3 |
| 5 | 25 | 2 | 4 |
| 6 | 30 | 2 | 5 |
| 7 | 35 | 3 | 6 |

## T9 — MS deterministic drift: seasons to Rupture from MS 60, no restoration
Baseline -1/yr (PP-255) = -0.25/season; plus op-load L RS/season net of self-closure.
| Net op load (RS/season) | Seasons to Rupture | Years |
|---|---|---|
| 0 | 240 | 60 |
| 0.5 | 80 | 20 |
| 1 | 48 | 12 |
| 2 | 27 | 7 |
| 3 | 18 | 5 |
| 5 | 11 | 3 |

## T10 — Continuity-corrected Normal (threshold at Ob−0.5): residual divergence
| Pool | Ob | exact | Normal(Ob−0.5) | abs diff |
|---|---|---|---|---|
| 5D | 2 | 60.00% | 61.01% | 1.01pp |
| 5D | 3 | 38.00% | 38.99% | 0.99pp |
| 5D | 5 | 8.33% | 8.11% | 0.22pp |
| 5D | 8 | 0.13% | 0.11% | 0.03pp |
| 7D | 2 | 72.61% | 73.05% | 0.43pp |
| 7D | 3 | 54.74% | 55.64% | 0.89pp |
| 7D | 5 | 20.83% | 21.09% | 0.27pp |
| 7D | 8 | 1.49% | 1.32% | 0.17pp |
| 9D | 2 | 80.87% | 80.92% | 0.05pp |
| 9D | 3 | 67.12% | 67.66% | 0.55pp |
| 9D | 5 | 34.75% | 35.38% | 0.63pp |
| 9D | 8 | 5.43% | 5.21% | 0.22pp |
| 12D | 2 | 88.54% | 88.31% | 0.23pp |
| 12D | 3 | 79.57% | 79.67% | 0.10pp |
| 12D | 5 | 53.65% | 54.31% | 0.66pp |
| 12D | 8 | 16.43% | 16.50% | 0.06pp |
| 17D | 2 | 94.91% | 94.60% | 0.31pp |
| 17D | 3 | 90.61% | 90.38% | 0.23pp |
| 17D | 5 | 75.52% | 75.72% | 0.20pp |
| 17D | 8 | 41.08% | 41.60% | 0.51pp |
| 22D | 2 | 97.66% | 97.41% | 0.25pp |
| 22D | 3 | 95.61% | 95.34% | 0.27pp |
| 22D | 5 | 87.53% | 87.41% | 0.12pp |
| 22D | 8 | 63.15% | 63.55% | 0.40pp |

Max residual with continuity correction: 1.01pp (vs 10.00pp uncorrected)
