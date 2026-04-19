# Valoria Coverage Matrix
# Full historical findings: see tests/sim_batch_*_2026-04-16.md
# This file tracks open findings and recent confirmations only.

## Open Findings (all batches)

| ID | Source | Description | ED |
|----|--------|-------------|-----|
| SIM2-01 | ST-01 | 2x Senator Assert engine too fast | ED-572 (resolved) |
| SIM2-05 | ST-06 | Post-combat fieldwork when player fled undefined | Resolved — ED-576 |
| SIM2-06 | ST-07 | Co-Movement Cards 1-15 not in canonical docs | Resolved — ED-577 |
| SIM2-07 | ST-07 | TTRPG mass battle melee damage formula implicit | Resolved — ED-578 |
| SIM2-10 | ST-03 | Social initiative deterministic vs combat rolled | Resolved — ED-581 |
| SIM2-11 | ST-03 | Chain Contest Resistance-2 stall not documented | Resolved — ED-582 |
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

## Resolved This Session

| ED | Resolution |
|----|------------|
| ED-588 | PT ≤ 3 (revised from PT ≤ 1). Resolved in victory_v30 §3.5 (2026-04-16). |
| ED-589 | Presence marker mechanics defined: Community Organizing Domain Action, cap 5/territory, Church/Crown suppression rules. victory_v30 §3.5 updated. |
| ED-612 | Guilds intentionally have no solo victory condition. Guilds are an NPC faction/tool, not a protagonist faction. Confirmed in throughline analysis. |
| ED-577-01/02/03/04 | Co-Movement calibration — all 4 resolved, RS ±4.3 PASS |
| SIM-POL-R01-R05 | Faction politics simulation — all 5 items PASS (Standing reachability, Ministry decay, caste gating, branch differentiation, cross-faction balance) |
| ED-684 | Derived stats calibration — multipliers confirmed provisional (sim_derived_stats_calibration) |
| ED-590 | Church victory revised + validated: TC ≥ 65 + Accord ≥ 3 in ≥ 3 non-capitals |
| ED-572 | Assert → Pontifex-exclusive |
| ED-545/551/555/557/559/571/583 | See sim_batch_3 |
| ED-539/585 | See sim_batch_3/4 |

## Throughline Analysis + Propagation — 2026-04-17

Top-down audit across all 8 batches (ST-01 through ST-60).

### Robustness: ✓ working
Victory race convergence, TC/RS pyrrhic collision, Obligation cascade, Torben investment race, Calamity reversal gate, co-victory hold, Elske subversive strategy, Niflhel intelligence market

### Robustness: ✗ gaps addressed
IP rate too mild → revised (+3/battle, +2/season TC60+); No Parliamentary block on Excommunication → Parliamentary Stay added; Guilds solo victory resolved (ED-612)

### Elegance: ✓ working
TC Reform, Church Accord governance condition, Feigned Retreat dual utility, Excommunication fait accompli, Shield Wall/Wedge counter, Depth 5 non-investigative

### Elegance: ✗ gaps addressed
Grand Contest Recall → once-per-source rule; Accord/Order invisible → clarified; IP published wrong → corrected; BG lobby pre-determination → capped at 4-6

### Smoothness: ✓ working
Zoom In/Out (cleanest system), 5-step Cascade, collective co-movement fires once, three-faction bilateral sequential, mass battle tactic cards

### Smoothness: ✗ gaps addressed
Accord/Order co-fire sequence → Order 0 first, Accord 0 second; Partition silent win → Phase 1 declaration required; Siege mechanic absent → §1.9 added; Parliamentary Stay → §10.1 added

### Propagated
social_contest: Grand Contest Recall fix, BG lobby cap, Obligation 3-cap advisory, Parliamentary Stay §10.1
victory_v30: Rupture Scene + Last Declaration, RM Presence vs Phase 1 distinction, Partition Phase 1 declaration
peninsular_strain: IP rate +3/battle +2/season-TC60, Accord/Order distinction §2.4b, co-fire sequence
mass_battle: §E Battle Consequences (canonical consolidation from 4 source docs)
military_layer: §1.9 Siege Action mechanic
scale_transitions: Stability Crisis Zoom In trigger
npc_behavior: Constrained sub-arc state, Torben Conviction window S1-8


## New Findings — sim_npc_player_batch2_2026-04-16

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| JUS-SIM-02 | Cardinal Justice | Heresy Proceedings: authorization loop | ✓ Archived — ED-629 resolved 2026-04-17 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Vaynard Path B met at S9 from Season 1 hold — fastest single path | VAY-SIM-04 | ✓ |
| Vaynard S0 Assembly pre-garrisons T13 before Baralta can Proclaim | VAY-SIM-01 | ✓ Reinhard Principle |
| Intelligence auction: 2 major world events from S1 intel, zero Domain Actions | VAY-SIM-05 | ✓ Force multiplication |
| Baralta Sovereign Authority Doctrine = constitutional fortification | BAR-SIM-01 | ✓ |
| Almud institutional ambiguity as governance — Thread absorbed without public acknowledgment | ALM-SIM-03 | ✓ |
| Ehrenwall Counter fires from information failure (withholding RS data), not military failure | EHR-SIM-01 | ✓ Conviction correctly distinguishes |
| Justice winning Proceedings → shared loss conditions more likely | JUS-SIM-01 | ✓ Institutional winner / peninsula loser |
| Reinhard Principle generalizes to all faction leaders | CROSS-01 | ✓ Core strategic principle |
| Conviction = permanent Ob economy on aligned actions | CROSS-02 | ✓ |

### New SIM-DEBT

| ID | Description | Status |
|----|-------------|--------|
| SIM-B2-01 | Vaynard simultaneous 3-path Accounting conflict verification | OPEN |
| SIM-B2-02 | Ehrenwall moral ledger 30-season timing | OPEN |
| SIM-B2-03 | Justice-as-Confessor 10-season Church governance sim | OPEN |


## Editorial Approval — 2026-04-17

All open editorial items approved by Jordan. Propagated this batch:

| Item | Target | Status |
|------|--------|--------|
| ED-620 RM Founding Mechanic | victory_v30 §8 | Propagated |
| ED-624 Elske Loyalty Track | victory_v30 §3.6 | Propagated |
| ED-625 Excommunication Tribunal | social_contest §7.1 | Propagated |
| ED-616 Intelligence Embargo | tc_political_redesign §8 | Propagated |
| ED-591-609 Arc Expansion v1 | npc_behavior §5.2 reference note | Approved + noted |
| ED-634 Faction Politics expansion | faction_politics_expanded_v1 | Approved, propagation pending |


## ED-634 Propagation — 2026-04-17

Faction Politics rank-ladder expansion (PP-660). Propagated to:

| Target | Change |
|--------|--------|
| npc_behavior_v30 §1.2 | Community and Warden added to Conviction taxonomy |
| npc_behavior_v30 §3.3 | Caste-transgressive Scar risk modifier noted |
| npc_behavior_v30 §2.13 | Crown inner circle (Voss/Reichard/Thale/Linder/Kreutz) Stance Triangles |
| npc_behavior_v30 §2.14 | Hafenmark inner council (Heljason/Geirson) Stance Triangles |
| npc_behavior_v30 §2.15 | Varfell Jarl council (Holdar/Stenskald) Stance Triangles |
| player_agency_v30 §3.3 | Initiation Duty category added |
| Ledger | ED-634 resolved; sub-EDs 635-658 and SIM-POL-R01/02/05 registered |

Remaining open sub-EDs: ED-640/642/643/644/645/648/649/650/651/652/655/656/657/658, SIM-POL-R01/02/05. All P2 except ED-643 (Solmund propagation P1) and SIM-POL-R01/02/05 (P1 sim-debt).

## New Findings — sim_npc_player_batch3_2026-04-17

### Staleness Audit
- AER: **confirmed live** in board_game_v30. Modifies Altonian Vanguard deployment threshold. Prior simulation usage was correct.
- faction_politics_expanded_v1.md (PP-660, accepted 2026-04-17): canonical source for all sub-office ladders, named inner circle NPCs, Ministry expansion. Prior simulations pre-dated this document.

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| GAP-B3-01 | Multiple | Shadow Renown referenced across docs but no implementation specification | ✓ Archived — ED-632 resolved 2026-04-17 |
| — | Riskbreaker §2.2 | Deniability Debt referenced as "stage13 mechanic, retained" but not defined in canonical docs | Open — ED-633 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Spymaster: double-agent methodology (controlling compromised assets rather than severing them) | KOLT-SIM-01 | ✓ Correct intelligence model |
| Spymaster: 1-season verification delay produces actionable vs. speculative intelligence | KOLT-SIM-02 | ✓ Mechanically correct |
| Royal Guard dual-chain: Kreutz cannot transmit Counter information without chain breach | KREU-SIM-03 | ✓ Institutional blind spot confirmed |
| Guild Comptroller: Parliamentary Committee motions = cheapest Domain Action equivalents | FELD-SIM-02 | ✓ Free binding law from Scene action |
| Templar: converting military provocation into Parliamentary weapon through formal Protest | TEMP-SIM-01 | ✓ Defensive constraint as political tool |
| Riskbreaker: institutional activation (making institutions act without knowing they're directed) is highest-skill mission outcome | RB-SIM-01 | ✓ |
| Journeyman: victory depended entirely on Feldhaus's discretion — systemic, not personal | JOUR-SIM-01 | ✓ Honest statement about institutional power |

### Cross-Simulation Findings

| Finding | Description |
|---------|-------------|
| CROSS-B3-01 | Mid-rank characters experience the moral cost that faction leaders export |
| CROSS-B3-02 | Institutional blind spot is always one step up — constraints are positional, not systemic |
| CROSS-B3-03 | Shadow Renown lacks formal game support across three character types |

---

