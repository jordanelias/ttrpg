# NERS Stress Test — ners_stress_01
## Date: 2026-05-08
## Runs: 300 (100 seeds × 3 perturbation levels)
## Max seasons per run: 60

---

## §1 Outcome Distribution

### Mild perturbation (n=100)
| Outcome | Count | Rate |
|---------|-------|------|
| Crown wins | 16 | 16% |
| Church wins | 1 | 1% |
| Hafenmark wins | 1 | 1% |
| Varfell wins | 15 | 15% |
| Partition/Church | 1 | — |
| Shared loss | 0 | 0% |
| Ongoing at s60 | 67 | 67% |
| Avg game length | 57.0 seasons | — |

### Moderate perturbation (n=100)
| Outcome | Count | Rate |
|---------|-------|------|
| Crown wins | 22 | 22% |
| Church wins | 7 | 7% |
| Hafenmark wins | 6 | 6% |
| Varfell wins | 9 | 9% |
| Partition/Church | 7 | — |
| Shared loss | 3 | 3% |
| Ongoing at s60 | 53 | 53% |
| Avg game length | 54.9 seasons | — |

### Extreme perturbation (n=100)
| Outcome | Count | Rate |
|---------|-------|------|
| Crown wins | 24 | 24% |
| Church wins | 11 | 11% |
| Hafenmark wins | 10 | 10% |
| Varfell wins | 11 | 11% |
| Partition/Church | 11 | — |
| Shared loss | 7 | 7% |
| Ongoing at s60 | 37 | 37% |
| Avg game length | 52.4 seasons | — |

---

## §2 NERS Aggregate Scores

Score range [0.0, 1.0] — higher is better. Flagged if < 0.6.

| Signal | Axis | Direction | Score | Flag |
|--------|------|-----------|-------|------|
| n_faction_viability | N | Top-down / Bottom-up | 0.96 | ✓ |
| n_clock_activity | N | Diagonal (cross-system) | 1.00 | ✓ |
| r_winner_diversity | R | Lateral (inter-faction) | 1.00 | ✓ |
| r_faction_interaction | R | Lateral (inter-faction) | 1.00 | ✓ |
| r_game_length | R | Horizontal (within-scale) | 0.69 | ✓ |
| s_clock_monotonicity | S | Diagonal (cross-system) | 1.00 | ✓ |
| s_turmoil_bounded | S | Horizontal (within-scale) | 1.00 | ✓ |
| e_stat_correlation | E | Top-down | 0.64 | ✓ |
| e_territory_correlation | E | Top-down | 0.69 | ✓ |

---

## §3 Mode D Findings

No P1 or P2 findings. All NERS signals ≥ 0.6 across 300 runs.
---

## §4 Winner Dominance Check (R — Lateral)

| Faction | Wins | Rate | Flag |
|---------|------|------|------|
| Crown | 62 | 20% | ✓ |
| Church | 19 | 6% | ✓ |
| Hafenmark | 17 | 5% | ✓ |
| Varfell | 35 | 11% | ✓ |

---

## §5 Coverage Matrix Update

| Module | Status | Smoke Tests | Batch Runs |
|--------|--------|-------------|------------|
| Module 1 — Randomization Layer | verified | 5/5 PASS | N/A |
| Module 2 — NERS Batch | verified | see §3 | 300 |