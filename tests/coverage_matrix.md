# Valoria Simulation Coverage Matrix
## Single canonical source. Updated by sim-orchestrator after each test batch.
## 7 dimensions tracked per test: Mechanic | Mode | Temporal | Tracks | Factions | NPCs | Archetypes

| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|---------|-----------|------|----------|--------|----------|------|------------|--------|----------|
| SIM-X-01 | Personal Combat + W-24 (Coherent Strike) | C + B | Single scene | Health, Wounds, Stamina, Coherence, RS | None | Practitioner-fighter (Mira), Armoured Veteran (Kaspar) | Practitioner-combatant | Complete — Issues found |
| SIM-X-02 | Debate (v1 redesign) + W-41 (Conviction Anchor) | C + B | Single scene | Composure, Coherence, RS, Belief | Church | Practitioner-scholar (Vessa), Inquisitor (Aldric) | Asymmetric Debate | Complete — Issues found |
| SIM-X-03 | Mass Battle + W-30 (Cohesion Bolster) + W-33 (Rally the Broken) | C + B | 2 turns | Strength, Cohesion, Morale, Coherence, RS | Lowenritter, Rebel | Practitioner attached to unit (Solmund) | Thread-supported Mass Battle | Complete — Issues found |
| SIM-X-04 | Mass Battle + Personal Combat (General Duel, Stage 1/2 Death) | C + D | 3 turns | Strength, Cohesion, Morale, Health, Wounds, CR | Lowenritter, Rebellion | General-combatants (Harnak, Davan) | General Duel | Complete — No P1/P2 |

> Coverage data from pre-v3 batches (Batches 01-11, threadweaving series) is archived in
> `deprecated/sim_coverage_matrix_legacy.md`. Tests predated 7-dimension tagging and cannot
> be retroactively mapped without re-running scenarios.

## Cross-Mechanic Findings Summary (SIM-X batch)

| ID | Source | Severity | One-line |
|----|--------|----------|----------|
| F-04 | SIM-X-01 | P2 | W-24 near-costless if Leap protected (0 RS, 0 Coherence) |
| F-07 | SIM-X-01 | P2 | W-24 balance entirely depends on Leap vulnerability; no RS/Coherence gate |
| F-08 | SIM-X-02 | P2 | W-41 break-even requires 11+ exchanges — exceeds typical Debate length |
| F-09 | SIM-X-02 | P1 | W-41 doesn't address structural disadvantage in asymmetric debates |
| F-10 | SIM-X-02 | P2 | W-40 series exchange cost disproportionately high vs combat equivalent |
| F-11 | SIM-X-03 | P1 | W-33 cannot rescue CP≤2 units: Cohesion=2 insufficient when Strength is binding |
| F-12 | SIM-X-03 | P2 | W-30 Coherence cost limits sustained Thread support to ~10 mass battle ops |
| F-13 | SIM-X-03 | P2 | Weapon mismatch decisive at mass scale before Thread considered |
| F-14 | SIM-X-03 | P3 | W-30 Failure mode risks own unit −1 Cohesion (~8% at Ob4) |
| F-15–F-18 | SIM-X-04 | P3 | Mass battle/personal combat cross-mechanic interaction coherent; no P1/P2 |

## P1 Items Requiring Editorial Decision

| ID | Description | Proposed Fix | Status |
|----|-------------|-------------|--------|
| F-09 | W-41 (Conviction Anchor) ineffective in asymmetric debates | W-41 needs broader effect scope OR new mechanic for Thread/Debate integration | [EDITORIAL: pending] |
| F-11 | W-33 (Rally the Broken) broken for CP≤2 units | Restore Cohesion to min(3, prior value) OR add Strength restoration component | [EDITORIAL: pending] |
