# Personal-Combat Stress Matrix — Results
_N=200/position (×2 swapped), max_bouts=40, seed=20260623; mirror baseline = 54.8% win / 0.0% draw. Baseline: uniform-4, arming, light armour, tradition none._

> Read every cell as a **marginal vs the same-config baseline** (the @4 / ×1.0 / full-engine cell), not an absolute — the single-seed mirror sits at 54.8%, so the fair point is there, not 50.

## Block 1 — Attribute impact (win% vs uniform-4, swept 1→7)

| Attribute | @1 | @2 | @3 | @4 | @5 | @6 | @7 | swing(7−1) |
|---|--|--|--|--|--|--|--|--|
| **cog** | 6.8 | 10.0 | 21.8 | 54.8 | 77.8 | 86.8 | 92.0 | +85.2 |
| **history** | 8.0 | 12.5 | 28.2 | 54.8 | 76.5 | 90.2 | 92.0 | +84.0 |
| **strength** | 4.8 | 7.8 | 18.0 | 54.8 | 66.5 | 82.8 | 86.0 | +81.2 |
| **agi** | 14.5 | 19.0 | 26.0 | 54.8 | 76.0 | 86.5 | 92.2 | +77.7 |
| **end** | 7.8 | 16.0 | 25.0 | 54.8 | 62.5 | 74.2 | 81.5 | +73.7 |
| **att** | 16.2 | 22.2 | 28.5 | 54.8 | 70.2 | 81.0 | 86.2 | +70.0 |
| **spirit** | 25.8 | 31.5 | 37.0 | 54.8 | 58.0 | 65.0 | 67.0 | +41.2 |
| **focus** | 42.8 | 46.0 | 44.5 | 54.8 | 51.0 | 57.5 | 59.8 | +17.0 |
| **disp** | 47.8 | 51.5 | 49.2 | 54.8 | 49.8 | 47.5 | 46.8 | -1.0 |

## Block 2 — Derived-score leverage (one fighter's derived value ×0.5 / ×1.5, attributes equal)

| Derived score | ×0.5 win% | ×1.5 win% | spread | leverage |
|---|--|--|--|--|
| `reading` | 5.5 | 94.0 | +88.5 | ★★★ dominant |
| `reach_base` | 5.8 | 94.0 | +88.2 | ★★★ dominant |
| `weapon_tempo` | 11.2 | 77.2 | +66.0 | ★★★ dominant |
| `resolution_pool*` | 14.0 | 73.8 | +59.8 | ★★★ dominant |
| `stamina_max` | 23.0 | 71.0 | +48.0 | ★★ strong |
| `balance_eff` | 32.8 | 68.5 | +35.7 | ★★ strong |
| `health_full*` | 35.0 | 61.8 | +26.8 | ★★ strong |
| `conc_max` | 37.8 | 61.8 | +24.0 | ★ moderate |
| `reflex` | 41.8 | 59.5 | +17.7 | ★ moderate |
| `handling_penalty` | 50.8 | 49.5 | -1.3 | · minor |
| `initiative_sigma` | 52.2 | 49.5 | -2.7 | · minor |
| `leverage` | 56.8 | 46.8 | -10.0 | · minor |
| `legibility` | 58.2 | 45.2 | -13.0 | · minor |
| `str_demand` | 54.8 | 36.2 | -18.6 | · minor |

## Block 3 — State-graph component ablation (Δwin% vs full engine, by matchup)

_Full-engine panel baseline (A win%): mirror 54.8 · reach 86.8 · skill 92.0 · armour 44.0. Δ = ablated − full; large |Δ| = load-bearing, ~0 = inert in that matchup._

| Component (ablated) | mirror Δ | mirror draw Δ | reach Δ | skill Δ | armour Δ | max\|Δ\| |
|---|--|--|--|--|--|--|
| `burst` | -6.6 | +0.0 | +4.2 | +0.0 | -38.5 | 38.5 |
| `armour_defeat` | -4.0 | +0.0 | -1.0 | -0.5 | -23.8 | 23.8 |
| `standing_reach` | +0.0 | +0.0 | -22.3 | +0.0 | +2.5 | 22.3 |
| `single_counter` | -8.8 | +0.0 | -1.6 | +0.8 | -2.8 | 8.8 |
| `attacker_bias` | -7.8 | +0.0 | +2.0 | +1.0 | +1.2 | 7.8 |
| `indes_steal` | -7.3 | +0.0 | +1.0 | +0.0 | -5.2 | 7.3 |
| `riposte` | -3.0 | +0.0 | +1.7 | -2.2 | -7.2 | 7.2 |
| `legibility` | -7.0 | +0.0 | -3.6 | +0.0 | +1.5 | 7.0 |
| `commit_disc` | -7.0 | +0.0 | +0.0 | +0.2 | -1.5 | 7.0 |
| `stop_hit` | +0.0 | +0.0 | -5.0 | +0.0 | +6.8 | 6.8 |
| `handling` | -1.0 | +0.0 | +6.2 | +0.8 | -3.0 | 6.2 |
| `bind` | -4.0 | +0.0 | +3.0 | -0.2 | -6.0 | 6.0 |
| `overcommit` | -5.8 | +0.0 | +3.7 | +0.0 | -1.5 | 5.8 |
| `approach_displace` | +0.0 | +0.0 | +5.4 | +0.0 | +0.0 | 5.4 |
| `feint` | -5.3 | +0.0 | +2.2 | +0.2 | -5.2 | 5.3 |
| `wound_ob` | -4.3 | +0.0 | +2.2 | +1.5 | +5.2 | 5.2 |
| `initiative_edge` | -4.3 | +0.0 | +0.2 | +0.2 | -4.8 | 4.8 |
| `reach_reopen` | +0.0 | +0.0 | +4.0 | +0.0 | -1.0 | 4.0 |
| `tempo_fatigue` | -1.3 | +0.0 | -4.0 | +0.8 | +0.0 | 4.0 |
| `consistency_focus` | -1.8 | +0.0 | -0.8 | +2.2 | +0.0 | 2.2 |
| `mental_fatigue` | -2.0 | +0.0 | -1.8 | +0.0 | +1.0 | 2.0 |
| `poise_kuzushi` | -2.0 | +0.0 | +1.4 | +1.2 | +0.5 | 2.0 |
| `displace_inside` | +0.0 | +0.0 | +1.2 | +0.0 | +0.0 | 1.2 |
| `push_shove` | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | 0.0 |
| `oob` | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | 0.0 |
| `disrupt_focus` | +0.0 | +0.0 | +0.0 | +0.0 | +0.0 | 0.0 |