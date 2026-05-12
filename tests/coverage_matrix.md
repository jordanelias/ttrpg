# Valoria Simulation Coverage Matrix
## Last updated: 2026-05-11 | SIM-MB-05A/B/C (Phase 2 complete)

| System | Last Sim | Scenarios | Findings | P1 Open | Status |
|--------|----------|-----------|----------|---------|--------|
| mass_combat (engagement) | SIM-MB-05A | Line vs Line + matrix | F-G lethality at 3.95t target met | — | ✓ ED-811 validated |
| mass_combat (volley) | SIM-MB-05C | TN6 vs TN7 composition sweep | F-I ranged dominance partial fix | ED-822 | ⚠ TN7 partial fix; ED-825 secondary measure |
| mass_combat (composition grid) | SIM-MB-05A | 5 shapes × 4 comps | — | — | ✓ ED-814 distribution validated |
| mass_combat (shapes) | SIM-MB-05A/B/C | 5×5 matrix + 4 H-variants | F-A,B,C all resolved; H-2 selected | — | ✓ ED-816 fully calibrated |
| mass_combat (drift cascade) | SIM-MB-05C | direct vs tiered alternatives | direct-to-Line selected over tiered | — | ✓ ED-817 validated |
| mass_combat (Discipline) | SIM-MB-05A | shape min-Disc tests | — | — | ✓ ED-815 reframing holds |
| mass_combat (combined attack) | SIM-MB-05A/C | vs 5 shapes; 3v1 test harness | F-D undercalibrated; F-J Fibonacci aggressive | ED-823 | ⚠ test harness needs rebuild |
| mass_combat (Horseshoe trigger) | SIM-MB-05C | 4 H-variants × 4 opponents | H-2 positional selected (54% mean) | — | ✓ ED-821 resolved → ED-816 |
| mass_combat (rally) | SIM-MB-04 | isolation | — | — | ✓ ED-802 formula verified |
| mass_combat (withdrawal) | SIM-MB-04 | conceptual | — | ED-813 | Phase 1 fix in workplan |
| mass_combat (stability) | SIM-MB-04 | S1,S2 | — | — | ✓ ED-808 correct |
| mass_combat (grid map) | SIM-MB-04 | 8x5 grid | — | — | Prototype validated |
| combat (personal) | SIM-MB-03 | — | — | — | See prior sims |
| social_contest | sim_d06 | — | — | — | See prior sims |
| thread | sim_thread_batch_08 | — | — | — | See prior sims |
| strategic | sim_bg_ff_01 | — | — | — | See prior sims |

## SIM-MB-05A/B/C Summary
- Date: 2026-05-11
- Scope: Phase 2 shape mechanics validation + exhaustive branch exploration
- Trials: 6000+ across three batteries
- EDs validated and closed: 811, 812, 814, 815, 816, 817, 821
- EDs raised and open: 822 (Volley TN partial fix; secondary measure as ED-825), 823 (combined attack calibration)
- Lethality: 3.95t mean, 0/600 one-turn kills
- Shape matrix: produces strategic rock-paper-scissors with Horseshoe H-2 trigger
- Volley TN7: partial fix for composition imbalance (+8pp pure-melee competitiveness)

## Next simulation priorities
1. **SIM-MB-06**: rebuild 3v1 combined attack test harness; validate ED-823 Fibonacci recalibration options
2. **Composition balance secondary measure**: test melee_pct Ob bonus / Volley pool cap / DR scaling (ED-825 candidate)
3. **Workplan Phase 3-6**: propagate ED-811..820 to mass_battle_v30.md and params files
4. **Then A3 SCHISM**: archetype 3 testing per parent workplan
