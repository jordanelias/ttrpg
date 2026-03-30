# Valoria Simulation Coverage Matrix
## Single canonical source. Updated by sim-orchestrator after each test batch.
## 7 dimensions tracked per test: Mechanic | Mode | Temporal | Tracks | Factions | NPCs | Archetypes

| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|---------|-----------|------|----------|--------|----------|------|------------|--------|----------|
| SIM-X-01 | Personal Combat + W-24 | C+B | Single scene | Health, Wounds, Stamina, Coherence, RS | None | Mira, Kaspar | Practitioner-combatant | Complete |
| SIM-X-02 | Debate + W-41 | C+B | Single scene | Composure, Coherence, RS, Belief | Church | Vessa, Aldric | Asymmetric Debate | Complete |
| SIM-X-03 | Mass Battle + W-30 + W-33 | C+B | 2 turns | Size, Cohesion, Morale, Coherence, RS | Lowenritter, Rebel | Solmund | Thread-supported Mass Battle | Complete |
| SIM-X-04 | Mass Battle + Personal Combat (General Duel) | C+D | 3 turns | Size, Cohesion, Morale, Health, Wounds, CR | Lowenritter, Rebellion | Harnak, Davan | General Duel | Complete |
| SIM-X-05 | Grand Debate + W-41 + W-42 + Audience | C+B | 5 exchanges | Composure, Coherence, RS, TC, Knots | Church, Hafenmark | Baralta, Himlensendt, Klapp | Institutional Grand Debate | Complete |
| SIM-X-06 | Personal Combat + Wound −1D + CE arc | C+D | 4 rounds | Health, Wounds, Stamina, CE | Lowenritter, Church | Ehrenwall, Haelmund, Vald, Maret | Named NPC duel + Inquisitor arc | Complete |
| SIM-X-07 | Mass Battle + W-30 + P-31 + General Duel + Stage 1/2 | C+D | 3 turns | Size, Cohesion, Morale, Coherence, RS, CR, Coup Counter | Lowenritter, Church | Ehrenwall (killed), Jarnstal, Maret | Named-NPC mass battle + Thread + deadlock | Complete |
| SIM-X-08 | Seasonal Accounting cascade | D+E | 1 season | All faction stats, TC, RS, Knots | All | Baralta, Klapp, Ehrenwall (dead), Vald | Full cascade | Complete |
| SIM-X-09 | Social (Vaynard/Almud) + Discovery Event + Domain Echo + Zoom | C+B | 1 scene | Composure, TS, TK, TC, IP | Crown, Varfell, Church | Vaynard, Almud, Klapp | Social → Thread → Faction zoom | Complete |
| SIM-X-10 | Sovereign Authority Doctrine + Olafsson Evidence Chain + TC cascade | C+B | 1 season | TC, Church Stability, Mandate, Baralta penalty | Church, Hafenmark | Baralta, Himlensendt, Olafsson | Domain Action chain + clock cascade | Complete |
| SIM-X-11 | Maret infiltration → Thread Diagnosis → Domain Echo → Inquisitor advance | C+B | 1 scene | TK, TC, CE, Coherence, RS, Investigation stages | Church, Varfell | Maret, Klapp, Vald | Personal→Thread→Faction zoom sequence | Complete |
| SIM-X-12 | 3-season full cascade | D+E | 3 seasons | All clocks, all faction stats, all NPC states | All | All named | Full cascade accounting | Complete |

> Pre-v3 batch coverage archived in `deprecated/sim_coverage_matrix_legacy.md`.

## P1 Findings — Editorial Decisions Required

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-11 | X-03 | W-33 broken for Size≤2 units: Cohesion=2 insufficient when Size is binding constraint | PENDING |
| F-27 | X-07 | Mass battle deadlock (HeavyCut vs HeavyArmour): no stalemate resolution rule | PENDING |
| F-30/F-33 | X-07/08 | Coup Counter: no successor rule on Grandmaster death | PENDING |
| F-43 | X-10 | Two Domain Actions can drop TC by 4+ in one season; no seasonal cap on TC | PENDING |
| F-45 | X-10 | Church Stability brake: does it suppress RS-driven cross-clock TC increase? | PENDING |
| F-52 | X-12 | No Stability recovery mechanic for externally damaged faction Stability | PENDING |

## Rules Gaps (No Patch Needed — GM Ruling Acceptable)

| ID | Source | Description |
|----|--------|-------------|
| F-38 | X-09 | Discovery Event mid-Debate: no interrupt rule; conservative ruling taken |
| F-41 | X-09 | No formal Impression rule for NPC TS-perception events during social scenes |
| F-48 | X-11 | CE track has no upper-ceiling distinction beyond Trajectory at CE 3 |

## Terminology Correction Applied

All prior SIM-X-01 through X-08 references to "Strength" as mass battle headcount stat corrected to **Size** in this index. Source files retain original text; correction is notional for tracking purposes only.
