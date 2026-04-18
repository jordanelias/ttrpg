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

## SIM-POL — Faction Politics Simulation Debt (PP-660 / PP-661, DEFERRED)

Per user instruction 2026-04-17, simulation validation of PP-660 faction politics rank-ladder expansion is deferred. These items are tracked here for discoverability; no active simulation work is scheduled.

| ID | Description | Priority | Status |
|----|-------------|----------|--------|
| SIM-POL-R01 | 7-rank progression pacing — validate player from Std 0 can reach Std 5 by S14 and Std 7 by S20 under normal play | P1 | DEFERRED 2026-04-17 |
| SIM-POL-R02 | Caste modifier impact — confirm Southern Einhir rank-advancement gates do not create unwinnable game states | P1 | DEFERRED 2026-04-17 |
| SIM-POL-R03 | Baralta Crown Claim × rank interaction — confirm Hafenmark-to-Crown Recognition Ceremony does not create exploit paths for free Crown Std 5 | P2 | DEFERRED 2026-04-17 |
| SIM-POL-R04 | TC × rank interaction — confirm TC 100 Unification does not trivialize or over-constrain Church rank advancement | P2 | DEFERRED 2026-04-17 |
| SIM-POL-R05 | Generational Shift Disposition outcomes — confirm 5-tier outcome table does not produce degenerate paths (always +3 in 2 seasons) | P1 | DEFERRED 2026-04-17 |

Resume trigger: (a) user-initiated simulation review, or (b) patch to faction_politics_expanded_v1 that changes rank-advancement formulas.


## New Findings — sim_npc_player_batch4_2026-04-17

### P2 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| ALM-SIM-01 | Almstedt | Constitutional irregularity (40-season-old amendment insufficient supermajority): most potent undisclosed institutional information in the game | Open — ED-660 adjacent |
| HAEL-SIM-02 | Haelgrund | Archives are Thread-constituted live objects, not static records — Ministry maintaining a sense organ no one knows is attached to a body | Noted |
| ELS-SIM-02 | Elske | Diplomatic Exchange produced by 8-season relational investment, not tactical argument — relationship is the precondition | Confirmed |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Almstedt certification of thin precedent enables Baralta Grand Contest — enables while constraining | ALM-SIM-02 | ✓ |
| Voss bifurcated intelligence (formal quarterly vs. War Council true picture) creates strategic reserve unknown to Löwenritter | VOSS-SIM-01 | ✓ |
| Klapp fiscal framing of buffer wins College vote where theological framing would lose | KL-SIM-02 | ✓ |
| Stenskald equal-validity ruling makes Maret Uln's claim an Assembly vote, not a blocked path | STEN-SIM-01 | ✓ |
| Haelgrund's Protocol 3 compliance (administrative routine) produces Warden intelligence access without deliberate choice | HAEL-SIM-01 | ✓ |
| Ehrenwall's 8-season relationship investment with Elske produces IP −10, AER +1 | ELS-SIM-01 | ✓ |

### Cross-Simulation Findings

| Finding | Description |
|---------|-------------|
| CROSS-B4-01 | Gatekeepers govern through withholding — negative power is the mid-rank character's primary tool |
| CROSS-B4-02 | Institutional memory is catastrophic risk — each character carries a specific piece of dangerous knowledge |
| CROSS-B4-03 | Relationship is political infrastructure — genuine relationship produces disproportionate returns at crisis moments |


## New Findings — sim_npc_player_batch5_2026-04-17

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| REICH-SIM-01 | Reichard | Haushalt Competence 3 +2/season has no Wealth cap — unbounded resource generation over long campaigns | Resolved — ED-663 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Reichard bifurcated record-keeping (inquiry notes vs. War Council true picture) preserves institutional memory | REICH-SIM-02 | ✓ |
| Heljason counter-argument addendum: internal preparation without burdening principal | HELJ-SIM-01 | ✓ |
| Father Linder's mutual management with Thale: institutionally stable dual-service without deception | LIND-SIM-01 | ✓ |
| Jarnstal partial compliance with Baralta's Doctrine preserves strongest ecclesiastical immunity ground | JAR-SIM-02 | ✓ |
| Hann's genealogical research produces his own best counter-argument | HANN-SIM-01 | ✓ Correct structural irony |
| Maret Uln's win-win construction: indispensable to Vaynard's success and to post-elimination continuity | MULN-SIM-02 | ✓ |

### Cross-Simulation Findings

| Finding | Description |
|---------|-------------|
| CROSS-B5-01 | Advisor as bottleneck — inconvenient truths are managed not delivered; systemic, not individual failure |
| CROSS-B5-02 | Coalition logic is asymmetric — preventing a majority is more efficient than building one |
| CROSS-B5-03 | Long-horizon investment wins mid-range crises — every successful character here invested 2+ seasons ahead |


## New Findings — sim_alternate_branches_2026-04-17

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| ALT-C-01 | Branch C | Path B wins at S9 while other factions 15 seasons from their conditions — speed-run calibration issue | Open — ED-666 |
| ALT-I-01 | Branch I | Coup Counter can fire at S17 before Regency Establishment conditions exist — premature triggering gap | Open — ED-667 |

### P2 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| ALT-J-01 | Branch J | Without warden cooperation, RS reaches ~21 at S30 — outside standard campaign window | Open — ED-668 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Almstedt deploys irregularity → forced supermajority → stronger Baralta victory (paradox) | ALT-A-01 | ✓ Constitutional stress-test produces better outcome |
| Voss's reserve makes Coup mechanically impossible without Ehrenwall violating Martial Honour Framework | ALT-B-01 | ✓ Military prep is Counter's check |
| Thale warning Almud produces strongest Crown outcome at highest personal cost | ALT-E-01 | ✓ Spymaster dilemma real |
| Klapp's publication produces Confessor endorsement via casting vote | ALT-D-01 | ✓ Church doctrinal transformation path confirmed |
| Heljason's refusal produces stronger legal brief than compliance | ALT-F-01 | ✓ Obstruction as highest-value advisor function |
| Haelgrund's report enters multi-faction intelligence chains; Niflhel pursues archives | ALT-G-01 | ✓ Silence vs disclosure has institutional cascade |
| Hann winning Assembly produces figurehead Sigurd + factional fragmentation | ALT-H-01 | ✓ Bloodline succession without governance produces POW-01 equivalent |

### Cross-Branch Findings

| Finding | Description |
|---------|-------------|
| CROSS-ALT-01 | Information timing is primary resource — who knows what, when controls outcomes more than military or TCV |
| CROSS-ALT-02 | Premature victory creates shallow worlds — mechanical win before narrative transformation produces stable but incomplete campaigns |
| CROSS-ALT-03 | Irreversible institutional precedent — published documents, legal records, disclosed intelligence cannot be recalled |


## New Findings — sim_mending_coherence_2026-04-17

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| MEND-SIM-01 | SIM 2 | OW Mending Coherence cost contradiction | ✓ Resolved — params_threadwork authoritative (0 all degrees); §3.2 corrected |
| MEND-SIM-02 | SIM 6 | ARC-S32 Coherence text wrong | ✓ Resolved — arc_register updated; fatigue mechanics substituted |
| MEND-SIM-03 | SIM 6 | ARC-S34 Edeyja Burnout primary path broken | ✓ Resolved — reframed as overwork/fatigue burnout; TE-15 terminal trigger preserved |

### P2 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| MEND-SIM-04 | SIM 3–4 | rs_budget.md recovery figures stale | ✓ Resolved — Scenario C updated; Conclusion corrected |
| MEND-SIM-05 | SIM 4 | wc_survival_spine.md Coherence row wrong | ✓ Resolved — resource tension table corrected |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Seasonal fatigue (+1 cumulative Ob, resets each season) throttles Mending effectively — self-correcting at negative E[RS] | MEND-SIM-01 | ✓ |
| WC3-is-singular-endgame conclusion holds; net −3.66/season at WC3 + community Mending survivable to Year 30 | MEND-SIM-04 | ✓ |
| Journeyman practitioners (Spirit 2, TS 50) have negative E[RS] at Field Ob 5; Relational-only targeting is correct | MEND-SIM-06 | ✓ |
| Old system caused permanent Severed equilibrium (Coh ~1, +2 Ob all ops) — new rule eliminates hidden impairment | MEND-SIM-02 | ✓ Design improvement confirmed |

### Cross-Simulation Findings

| Finding | Description |
|---------|-------------|
| CROSS-MEND-01 | Seasonal fatigue is the correct throttle — transparent to player, resets cleanly, no permanent impairment |
| CROSS-MEND-02 | ARC-S32 and ARC-S34 were built on Mending-as-Coherence-drain; both require text revision |
| CROSS-MEND-03 | Community Mending capacity is ~10x RS budget assumption; scenario narratives valid but net figures stale |


## New Findings — sim_alternate_branches2_2026-04-17

### P1 Findings

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| S-01 | Branch S | Ministry census records contain 150 seasons of undeclared Thread-sensitivity data | Open — ED-671 |

### Confirmed Working

| System | Source | Status |
|--------|--------|--------|
| Olafsson extra-territorial heresy designation as legal shadow outside Hafenmark | K-01 | ✓ |
| Baralta Arc B + Niflhel creates permanent constitutional precedent for criminal network | N-01 | ✓ |
| Unmanaged Arc C begins from absence of support not excess of exposure | Q-01 | ✓ Practitioner relationship structurally required |
| Almud Arc A reform prevents Counter advance via Ehrenwall moral ledger shift | T-01 | ✓ Reform path structurally prevents Coup |
| Haelgrund refusing synthesis → neutrality dataset more consequential than partisan dataset | S-01 | ✓ |
| Linder full RS report → Himlensendt sermon → offhand comment becomes public political theology | P-01 | ✓ |
| Stenskald conservative endorsement → Incapacity Assessment cascade at S28 | O-01 | ✓ |

### Cross-Branch Findings

| Finding | Description |
|---------|-------------|
| CROSS-B2-01 | Institutional neutrality is always political — no institutional act is without political consequence |
| CROSS-B2-02 | Most consequential actions are the smallest ones — addenda, single report decisions, synthesis refusals |
| CROSS-B2-03 | Reform path requires choosing uncertainty before being forced to — only path that permanently prevents the Coup |

