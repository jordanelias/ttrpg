# Valoria Coverage Matrix
# Full historical findings: see tests/sim_batch_*_2026-04-16.md
# This file tracks open findings and recent confirmations only.

## Open Findings (all batches)

| ID | Source | Description | ED |
|----|--------|-------------|-----|
| SIM2-01 | ST-01 | 2x Senator Assert engine too fast | ED-572 (resolved) |
| SIM2-05 | ST-06 | Post-combat fieldwork when player fled undefined | ED-576 |
| SIM2-06 | ST-07 | Co-Movement Cards 1-15 not in canonical docs | ED-577 |
| SIM2-07 | ST-07 | TTRPG mass battle melee damage formula implicit | ED-578 |
| SIM2-10 | ST-03 | Social initiative deterministic vs combat rolled | ED-581 |
| SIM2-11 | ST-03 | Chain Contest Resistance-2 stall not documented | ED-582 |
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
| ED-588 | RM Phase 2 T9 PT ≤ 1 unreachable |
| ED-589 | RM Presence marker mechanics undefined |
| ED-612 | Guilds have no solo victory condition |

## Resolved This Session

| ED | Resolution |
|----|-----------|
| ED-590 | Church victory revised + validated: TC ≥ 65 + Accord ≥ 3 in ≥ 3 non-capitals |
| ED-572 | Assert → Pontifex-exclusive |
| ED-545/551/555/557/559/571/583 | See sim_batch_3 |
| ED-539/585 | See sim_batch_3/4 |

## Batch 5 Confirmed Working (ST-21 through ST-30)

Victory race convergence, Grand Contest CLASH-always, Torben Conviction emergence,
arc conditioner system (env/cross-NPC/obligation all fire clean), Depth 4-5 fieldwork,
co-victory hold phase robust, TS 30→70 trajectory, 3-Obligation cascade, Church victory
revised, all 6 tactic cards + counter-formations.

## Batch 6 Scope (ST-31 through ST-40)

Settlement mechanics, Guilds victory design, 6-faction Parliamentary sim,
Altonian Vanguard, RM Founding, Elske arc, Thread collective op,
Cardinal restoration, Baralta Arc C, longevity cascade.
