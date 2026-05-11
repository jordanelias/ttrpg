# Valoria Simulation Coverage Matrix
## Last updated: 2026-05-11 | SIM-MB-04

This matrix tracks which mechanical systems have been simulated and at what coverage level.

| System | Last Sim | Scenarios | Findings | P1 Open | Status |
|--------|----------|-----------|----------|---------|--------|
| mass_combat (engagement) | SIM-MB-04 | S1,S2,S3 | FINDING-1,2,6 | ED-811,812 | ⚠ Lethality issue |
| mass_combat (volley) | SIM-MB-04 | S1,S2,S3 | FINDING-2 | ED-812 | ⚠ Over-tuned post-ED-800 |
| mass_combat (combined attack) | SIM-MB-04 | S2 | FINDING-4 | — | Blocked by ED-812 |
| mass_combat (rally) | SIM-MB-04 | isolation | — | — | ✓ Formula verified |
| mass_combat (withdrawal) | SIM-MB-04 | S2 | FINDING-7 | ED-813 | Phase gate ambiguous |
| mass_combat (stability) | SIM-MB-04 | S1,S2 | FINDING-8 | — | ✓ ED-808 correct |
| mass_combat (grid map) | SIM-MB-04 | S1,S2,S3 | FINDING-3 | — | Prototype working |
| mass_combat (discipline) | SIM-MB-04 | partial | — | — | No lethality to trigger |
| mass_combat (morale) | SIM-MB-04 | partial | — | — | No multi-turn battles in S1/S2 |
| combat (personal) | SIM-MB-03 | — | — | — | See prior sims |
| social_contest | sim_d06 | — | — | — | See prior sims |
| thread | sim_thread_batch_08 | — | — | — | See prior sims |
| strategic (BG) | sim_bg_ff_01 | — | — | — | See prior sims |

## SIM-MB-04 Summary
- Date: 2026-05-11
- Scope: mass_combat + grid_map prototype
- EDs tested: 800,801,802,804,805,806,807,808
- New EDs raised: 811 (engagement formula), 812 (volley lethality), 813 (withdrawal phase gate)
- Grid prototype: 8×5 confirmed viable for Godot tile system

## Next simulation priorities
1. **ED-811 resolution** — clarify engagement damage formula (Jordan ruling needed)
2. **ED-812 resolution** — recalibrate volley output post-ED-800 (Jordan ruling needed)
3. After 811+812: re-run S1/S2 for multi-turn battle validation
4. A3 SCHISM sim (CI, Seizure, Church) per workplan §9.1
