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

## Batch 6 Findings (sim_batch_6_2026-04-16) — ST-31 through ST-40

### New P1
| SIM6-01 | RM Founding mechanic missing from all docs | ED-620 |

### Resolved
| ED-612 | Guilds solo victory (Merchant Hegemony) designed and validated |
| ED-614 | Cardinal restoration conditions specified |

### New P2 EDs (621-627)
BG lobby cap, Varfell Parliamentary constraint, IP rate, Elske arc, Excommunication procedure, Accord/Order distinction, Guilds victory constraint fix.

### Confirmed Working
Guilds Merchant Hegemony (~S15-17), TC bonus equalising Parliament pools, Memory genre advantage, Thread collective op (72D Calamity reversal), Fort defense bonus, Elske pre-coup investment → Regency S17, double Priority 0 Zoom In choice, double longevity death cascade.


## Consolidation — sim sessions 2026-04-16

### Jordan Design Corrections Applied

| Correction | Impact |
|------------|--------|
| Guilds, Niflhel = spoiler/pressure factions; they do not win | ED-612, ED-627 closed as by-design |
| Löwenritter post-coup holds until new monarch faction takes over | ED-613 closed as by-design; §3.6 reframed |

### Propagations to victory_v30.md

| ED | Change | Section |
|----|--------|---------|
| ED-588 | RM holding: PT ≤ 3 (was ≤ 1). Uprising OW: T9 PT −2 added. | §3.5 |
| ED-590 | Church victory: Accord ≥ 3 in ≥ 3 non-capital territories. | §3.2 |
| — | Löwenritter design note: transitional faction, not conventional winner. | §3.6 |


## Batch 7 Summary (sim_batch_7_2026-04-16) — ST-41 through ST-50

### Resolved EDs
ED-589 (Presence marker mechanics), ED-586 (Constrained sub-arc), ED-587 (Stability Crisis Zoom In),
ED-617 (Grand Contest Recall fix), ED-621 (BG lobby cap), ED-622 (Varfell no-Senator note),
ED-626 (Accord/Order distinction), ED-623 (IP rate validated)

### New EDs
| ED-628 | Siege mechanic missing for playable factions | P2 |
| ED-629 | Partition needs Phase 1 declaration | P2 |
| ED-630 | RS Rupture needs Last Declaration scene spec | P2 |

### Batch 7 Confirmed Working
RM Presence markers (Strategy C canonical), Altonian invasion at S25 (revised IP),
Coalition rebuff IP reset, RS Critical Stability checks, HI chain 2-scene → Tribunal,
RM 30-season arc S8→S14→S15, Assert Mandate gate critical, Varfell Path C S14-15,
Intelligence Embargo coalition spoiler.

