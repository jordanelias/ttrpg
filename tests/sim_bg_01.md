# SIM-BG-01 — Board Game Mode Simulation
## Date: 2026-04-02
## Mode: G5 (Full Turn Sequence, 3-Player) + D (Edge Cases) + J (Cognitive Load)
## Status: COMPLETE

### 7-Dimension Tag
Test ID: SIM-BG-01
Mechanics: BG turn sequence, Domain Actions, Seasonal Accounting, Clocks, Unit Cohesion, Parliamentary Manoeuvre
Mode: BG | Temporal: PRES
Tracks: Theocracy Counter (TC), Rendering Stability (RS), Institutional Pressure (IP), Public Instability (PI), faction stats
Factions: Crown (P1), Church (P2), Hafenmark (P3), Varfell/Guilds/Niflhel/Restoration Movement (NPC)
NPCs: Generic Crown, Generic Church, Generic Hafenmark, Generic Varfell, Generic Guilds, Generic Niflhel, Generic Restoration Movement
Archetypes: Military (Crown), Religious (Church), Economic (Hafenmark)

### Provisional Assumptions
[PROVISIONAL ASSUMPTION: ED-001 unresolved — simulating Domain Action economy. Card-Hand system not yet designed.]
[PROVISIONAL ASSUMPTION: ED-004 unresolved — NPC AI behavior assumed from faction archetype (primary stat action).]
[PROVISIONAL ASSUMPTION: Null Season Card Season 1 (Event deck not in params).]

### Params Gaps Identified and Resolved
PG-01: Order tokens per faction (=5), placement order rule — resolved via PP-169 (compilation B4)
PG-02: Full Phase 1-6 season structure — resolved via PP-169 (compilation B4)
PG-04: Unit Muster Ob table — resolved via PP-169 (compilation B6)
PG-05: Faction capital territory assignments — resolved via PP-169 (compilation B3)
PG-07: Parliamentary Manoeuvre Partial result — resolved via PP-170 (confirmed absent in spec; explicit "no effect" ruling added)
PG-03: Full Accounting Phase Steps 1-12 — UNRESOLVED (B8 not read; out of scope this run)
PG-06: Mandate recovery mechanism — UNRESOLVED; flagged ED-066
PG-08: Event deck contents — UNRESOLVED; out of scope

### Season 1 Simulation (Mode G5)

Starting State:
Crown: M5 I5 W4 Mil4 Sta4 | Church: M5 I6 W5 Mil4 Sta5 | Hafenmark: M4 I4 W5 Mil3 Sta4
Clocks: TC28 RS72 IP20 PI5

Phase 4 Resolution (most likely outcomes at median pools, TN7):
- Church Thread Op T5 (6D Ob2): E[net]=1.8, P(>=2)=70%. Most likely: Success. RS 72->71. Thread Debt placed.
- Crown Govern T1 capital (5D Ob1): E[net]=1.5, P(>=1)=91%, P(>=2)=69%. Most likely: Overwhelming. T1 Prosperity 4->5.
- Crown Muster T1 (4D Ob1): E[net]=1.2, P(>=1)=80%. Most likely: Success. Light Infantry queued (deploys S2). T1 Prosperity 5->4.
- Church Govern T3 capital (5D Ob1): E[net]=1.5. Most likely: Overwhelming. T3 Prosperity 4->5. TC 28->29.
- Hafenmark Trade T6 (5D Ob2): E[net]=1.5, P(>=2)=69%. Most likely: Overwhelming. Hafenmark W 5->7 (CEILING HIT — F-01).
- Hafenmark Govern T6 (4D Ob3): E[net]=1.2, P(>=3)=25%. Most likely: Partial. Control gained, T6 Prosperity 5->4.
- Hafenmark Parliamentary Manoeuvre (4D Ob2): E[net]=1.2, P(>=2)=50%. Most likely: Partial. No effect (PP-170).
- Crown Decree (5D Ob2): E[net]=1.5, P(>=2)=69%. Most likely: Overwhelming. Church Mandate 5->4.

End of Season 1:
Crown: M5 I5 W4 Mil4 Sta4 | Church: M4 I6 W5 Mil4 Sta5 | Hafenmark: M4 I4 W7 Mil3 Sta4
Clocks: TC29 RS71 IP20 PI5

### Findings

| ID | Type | Severity | Description | Resolution |
|----|------|----------|-------------|------------|
| F-01 | Design gap | P2 | Hafenmark Wealth ceiling hit S1 on Overwhelming Trade T6. No Wealth sink mechanic for excess above 5. Trade dead action S2+ without Wealth expenditure. | ED-064 |
| F-02 | Balance note | P3 | Crown-Church rivalry load-bearing. NPC Crown leaves TC advancement uncontested. | ED-004 (existing) |
| F-03 | Cognitive load | P1 | Novice planning ~12 min/player. 3-player = 36 min/season = 432-576 min total campaign. Not viable. | ED-065 |
| F-04 | Cognitive load | P2 | Phase 5 Accounting (13+ steps, 8/10 load) has no reference card protocol. Table stall risk. | PP-169 partial |
| F-05 | Design note | P3 | Crown Decree Ob escalation hard wall at consecutive S4 (Ob5 vs 5D). Works as designed; forces seasonal inaction. | Note only |
| F-06 | Data conflict | P1 | TC starting value conflict: params=28 (P-32 canonical), compilation B1=15 (STALE). Compilation not updated post-P-32. | No params change needed; compilation sync blocked by ED-001 |
| F-07 | Spec gap | P2 | Parliamentary Manoeuvre Partial undefined in B5 spec. | PP-170 |
| F-08 | Spec gap | P2 | Mandate recovery mechanism undefined in BG spec. | ED-066 |

### Mode J Cognitive Load Summary
Domain Actions phase (experienced): 6/10. Novice: 10+/10.
Planning time novice: ~12 min/player. Experienced: ~2.75 min/player. Expert: ~90 sec/player.
Threshold breach: P1 (novice >5 min per resolution phase per simulator spec).
Reference cards mandatory; insufficient alone to fix novice onboarding.
