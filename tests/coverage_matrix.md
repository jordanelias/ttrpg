# Valoria Coverage Matrix
# Full historical findings: see tests/sim_batch_*_2026-04-16.md
# This file tracks open findings and recent confirmations only.

## Open Findings (all batches)

| ID | Source | Description | ED |
|----|--------|-------------|-----|
| SIM3-04 | NPC-03 | Arc state vs Priority 6 at Mandate < 3 | ED-586 |
| SIM3-07 | Zoom In | Stability Crisis Zoom In trigger absent | ED-587 |
| SIM4-01 | ST-14 | RM Phase 2 T9 holding condition unreachable | ED-588 |
| SIM4-02 | ST-14 | RM Presence marker mechanics undefined | ED-589 |
| SIM5-01 | ST-21 | No Parliamentary block on Tribune actions | ED-616 |
| SIM5-02 | ST-22 | Grand Contest Recall: once-per-source fix | ED-617 |
| SIM5-04 | ST-23 | Torben Conviction window: S1-8 formal def | ED-618 |
| SIM5-13 | ST-28 | 3-Obligation GM advisory cap | ED-619 |

## Active P1 EDs Requiring Design Action

| ED | Description |
|----|-------------|

## Resolved This Session (summary)

15 items resolved. See sim_batch archives for details.
Key: ED-588/589 (RM), ED-612 (Guilds), AUD-SET/VIC/NPC, SIM-DEBT-03/04,
ED-577-01-04, SIM-POL-R01-R05, ED-684, ED-590, ED-572, ED-545+.

## Recent Sims (2026-05-03)

| Sim | Scope | Result |
|-----|-------|--------|
| sim_telemetry_substrate_2026-05-03 (v2) | Phase 5a session 3.5 telemetry substrate (mandatory zoom-in frequency + SA-budget saturation, arc-driven correlation) | 4 personas × 100 campaigns × 40 seasons = 16k season-runs. v1 (independent triggers): 0% mandatory overflow across personas; mandatory p90 ~1.6. v2 (arc correlation: stability_crisis→revolt+succession, mass_battle→revolt, leader_removal→companion_arc, heresy→knot_crisis): mandatory overflow 0% Narrative/Normal, **0.4% Hard** (1 in 250 seasons under correlation); mandatory p90 lifts to 2.0 (+26%). Saturation unchanged: 96% Normal / 100% Hard / 36% Narrative. Per-system minutes use tabletop §12.3 placeholder durations — flagged [ASSUMPTION]. |


---

> **Historical batches archived.** All sim findings from 2026-04-17 to 2026-04-19 (inclusive) moved to `tests/coverage_matrix_archive_2026_04_19.md` per ED-786 archival sweep 2026-05-02. This active file tracks only unresolved findings, active P1 EDs, and the most-recent session summary.

## Vocabulary Sweep (2026-05-08)
All test/sim files updated: TC→CI, Peninsular Strain→Turmoil, Conviction Track→Piety Track, contest Initiative→First to Speak.

## Recent Sims (2026-05-08)

| Sim | Scope | Result |
|-----|-------|--------|
| ners_stress_01 (manifest) | NERS stress test — randomized starting conditions, all directions, Mode G | Module manifest committed. Module 1 (randomization layer) pending. Module 2 (NERS evaluation + batch) pending. |

### ners_stress_01 Module 1 (2026-05-08)
Module 1 randomization layer: 5 smoke tests PASS. Status: verified.

### ners_stress_01 Module 2 (2026-05-08)
NERS batch: 300 runs. No P1/P2 findings. All NERS signals >= 0.60. All 4 factions win. 52-67% ongoing at s60 — Tier A AI conservative strategy.
## Recent Sims (2026-05-09)

| Sim | Scope | Result |
|-----|-------|--------|
| combat_arch_residual_stress_01 (manifest) | Combat videogame architecture R1–R10 residual-risk sweep, Mode G + Mode A/B/D per module. Pressure-tests the 2026-05-01 EXPLORATORY composite stack residual risks (wound permanence, skill input in C, mass three-mode reframe, hero participation, wager stake range, Fibonacci cap, friendly fire, fieldwork-tempo shift, two-arch sufficiency, IP-gauge threshold). | Module 0 manifest committed. Modules R1–R10 pending. PP-684 collision resolved (4/18 set renumbered to PP-711..715 per fce5953); registry drift on combat/derived_stats design_doc fields documented. |
