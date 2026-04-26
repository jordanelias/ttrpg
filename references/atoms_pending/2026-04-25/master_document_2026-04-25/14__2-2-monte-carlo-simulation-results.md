---
atom_id: master_document_2026-04-25__14__2-2-monte-carlo-simulation-results
source_file: master_document_2026-04-25.md
source_section: "§2.2 Monte Carlo simulation results"
section_index: 14
total_sections: 50
line_count: 30
char_count: 1964
source_sha256: 312f97236be6f341
session_date: 2026-04-25
ingested: 2026-04-25
status: pending-prioritization
origin: session-master-upload
---

## §2.2 Monte Carlo simulation results

Built `sim_balance.py` — 750-line Python Monte Carlo simulator modeling 4 active factions (Crown/Church/Hafenmark/Varfell) across 17 territories, with d10 TN 7+ resolution, Burning Wheel-style outcome tiers, season-by-season action AI.

**Iteration history (37 iterations, ~50,000 total runs):**

| Stage | Win Rates (C/Ch/H/V) | Spread | Key Change |
|---|---|---:|---|
| I0 baseline | 88.7 / 0 / 0 / 0.3 | 88.4 pp | No Treaty consent gate |
| I3 | 61.3 / 0 / 0 / 0.7 | 60.6 pp | Anti-death-spiral floor added |
| I13 (best post-bug-fix) | 19.2 / 12.3 / 17.0 / 18.3 | 6.9 pp | 11-flag calibration |
| I33 (canonical Ob restored) | 15.1 / 6.2 / 15.3 / 6.9 | 9.1 pp | After fixing 2 sim bugs |

**Key sim-validated changes (ranked by leverage):**

1. **Tribune Compact** for Varfell (P0, audit §6.1) — Ob = M/2 + 2, gates Intel ≥ 5 + S ≥ 4
2. **Mass Seizure quadratic** declaration probability (P0) — replace `^3.3` with `^2.0`
3. **Crown all-3-rivals milestone** (P0) — revert PP-540's 2-of-3 softening
4. **Crown Treaty cession on Success+OW** (P0) — operationalizes `peninsular_strain §5.1`
5. **Church PV ≥ 10 + Accord ≥ 2 in 3 non-cap + Mass Seizure must fire** (P1)
6. **Hafenmark PV ≥ 12** (P1) — revert PP-541
7. **Hafenmark Diplomatic Token -1 Ob** (P1) — auto-applied, models `peninsular_strain §5.3`
8. **Sovereign Authority costs Diplomat-card** (P1, audit §6.3)
9. **Calamity Refugee penalty at MS ≤ 35** (P1, audit §6.4, BALANCE-005)
10. **Hafenmark Proclamation Wealth cost** (P0 for sim balance) — without it Hafenmark dominates
11. **Hafenmark PI ≥ 7 milestone** (P0 for sim balance) — was PI ≥ 5, trivially pre-met
12. **Church starting infrastructure pre-built** (P0 for sim balance) — Cathedral/Templar/Governor distribution per PT
13. **Crown Destabilize action** targeting lowest-Stab rival (P1)
14. **Mandate recovery passive** (P1) — factions not Mandate-attacked recover M slowly, capped at starting
