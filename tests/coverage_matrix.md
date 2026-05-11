# Valoria Simulation Coverage Matrix
## Last updated: 2026-05-11 | SIM-MB-05

| System | Last Sim | Scenarios | Findings | P1 Open | Status |
|--------|----------|-----------|----------|---------|--------|
| mass_combat (engagement) | SIM-MB-05 | Line vs Line + matrix | F-G lethality | — | ✓ ED-811 validated 3.95t avg |
| mass_combat (volley) | SIM-MB-05 | Composition sweep | F-I ranged dominance | ED-822 | ⚠ rebalance needed |
| mass_combat (composition grid) | SIM-MB-05 | 5 shapes × 4 comps | — | — | ✓ ED-814 distribution validated |
| mass_combat (shapes) | SIM-MB-05 | 5×5 matrix | F-A,B,C,H | ED-821 | ✓ ED-816 calibrated |
| mass_combat (drift cascade) | SIM-MB-05 | Disc threshold sweep | — | — | ✓ ED-817 validated |
| mass_combat (Discipline) | SIM-MB-05 | shape min-Disc tests | — | — | ✓ ED-815 reframing holds |
| mass_combat (combined attack) | SIM-MB-05 | vs 5 shapes | F-D too dominant | — | ⚠ defensive response needed |
| mass_combat (rally) | SIM-MB-04 | isolation | — | — | ✓ ED-802 formula verified |
| mass_combat (withdrawal) | SIM-MB-04 | conceptual | — | ED-813 | Phase 1 fix proposed |
| mass_combat (stability) | SIM-MB-04 | S1,S2 | — | — | ✓ ED-808 correct |
| mass_combat (grid map) | SIM-MB-04 | 8x5 grid | — | — | Prototype validated |
| combat (personal) | SIM-MB-03 | — | — | — | See prior sims |
| social_contest | sim_d06 | — | — | — | See prior sims |
| thread | sim_thread_batch_08 | — | — | — | See prior sims |
| strategic | sim_bg_ff_01 | — | — | — | See prior sims |

## SIM-MB-05 Summary
- Date: 2026-05-11
- Scope: Phase 2 shape mechanics validation
- EDs validated: 811,812,814,815,816,817 (post-Branch D/C adjustments)
- New EDs raised: 821 (Horseshoe targeting), 822 (Volley/Engagement composition balance)
- Mean battle length: 3.95t (target 3-6 ✓)
- One-turn kills: 0/600 trials
- Shape matrix: produces strategic rock-paper-scissors

## Next simulation priorities
1. **ED-821 resolution** — Horseshoe AI targeting / opponent-takes-bait mechanism
2. **ED-822 resolution** — Volley TN6→7 test, composition balance recalibration
3. After resolutions: SIM-MB-06 with all branches stable
4. Then Phase 5-6 propagation to canonical docs
5. Then A3 SCHISM
