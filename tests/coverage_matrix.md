# Valoria Simulation Coverage Matrix
## Single canonical source. Updated by sim-orchestrator after each test batch.
## 7 dimensions tracked per test: Mechanic | Mode | Temporal | Tracks | Factions | NPCs | Archetypes

| Test ID | Mechanics | Mode | Temporal | Tracks | Factions | NPCs | Archetypes | Status | Findings |
|---------|-----------|------|----------|--------|----------|------|------------|--------|----------|
| SIM-X-01 | Personal Combat + W-24 (Coherent Strike) | C + B | Single scene | Health, Wounds, Stamina, Coherence, RS | None | Mira (practitioner-fighter), Kaspar (armoured veteran) | Practitioner-combatant | Complete — Issues found |
| SIM-X-02 | Debate (v1 redesign) + W-41 (Conviction Anchor) | C + B | Single scene | Composure, Coherence, RS, Belief | Church | Vessa (practitioner-scholar), Aldric (Inquisitor) | Asymmetric Debate | Complete — Issues found |
| SIM-X-03 | Mass Battle + W-30 + W-33 | C + B | 2 turns | Strength, Cohesion, Morale, Coherence, RS | Lowenritter, Rebel | Solmund (attached practitioner) | Thread-supported Mass Battle | Complete — Issues found |
| SIM-X-04 | Mass Battle + Personal Combat (General Duel, Stage 1/2) | C + D | 3 turns | Strength, Cohesion, Morale, Health, Wounds, CR | Lowenritter, Rebellion | Harnak (general), Davan (general) | General Duel | Complete — No P1/P2 |
| SIM-X-05 | Grand Debate + W-41 + W-42 + W-40 | C + B | Single scene (5 exchanges) | Composure, Coherence, RS, TC, Knot strain | Church, Hafenmark | Baralta, Himlensendt, Klapp (TS growth) | Institutional Grand Debate | Complete — Issues found |
| SIM-X-06 | Personal Combat (Ehrenwall vs Haelmund) + Inquisitor CE | C + D | Single scene (4 rounds) | Health, Wounds (−1D system), Stamina, CE | Lowenritter, Church | Ehrenwall, Haelmund, Inquisitor Vald, Maret Uln | Named NPC duel, Inquisitor arc | Complete — Issues found |
| SIM-X-07 | Mass Battle (Löwenritter vs Templars) + W-30 + P-31 + General duel + Stage 1/2 | C + D | 3 turns | Strength, Cohesion, Morale, Coherence, RS, CR, Coup Counter | Lowenritter, Church | Ehrenwall (killed), Jarnstal, Maret Uln | Named-NPC mass battle + Thread + deadlock | Complete — Issues found |
| SIM-X-08 | Seasonal Accounting — full cascade from X-05/06/07 | D + E | 1 season | Mandate, Influence, Military, Stability, TC, RS, Knots | All factions | Baralta, Klapp, Ehrenwall (dead), Vald | Full cascade accounting | Complete — Issues found |

> Coverage data from pre-v3 batches (Batches 01-11, threadweaving series) is archived in
> `deprecated/sim_coverage_matrix_legacy.md`. Tests predated 7-dimension tagging and cannot
> be retroactively mapped without re-running scenarios.

## Complete P1/P2 Findings Register (All SIM-X Batches)

| ID | Source | Severity | Description | Status |
|----|--------|----------|-------------|--------|
| F-04 | SIM-X-01 | P2 | W-24 near-costless if Leap protected (0 RS, 0 Coherence, +2 damage) | Open |
| F-07 | SIM-X-01 | P2 | W-24 balance entirely depends on Leap vulnerability; no RS/Coherence gate | Open |
| F-08 | SIM-X-02 | P2 | W-41 break-even requires 11+ exchanges — exceeds typical Debate length | Resolved — design feature (Inspiration-attack counter) |
| F-09 | SIM-X-02 | P1 | W-41 irrelevant in policy debates; narrow activation window (Inspiration attacks only) | Resolved — design feature, not bug |
| F-10 | SIM-X-02 | P2 | W-40 exchange cost disproportionate vs combat equivalent | Open |
| F-11 | SIM-X-03 | P1 | W-33 broken for CP≤2 units: Cohesion=2 insufficient when Strength is binding | EDITORIAL PENDING |
| F-12 | SIM-X-03 | P2 | W-30 Coherence cost limits sustained Thread support to ~10 mass battle ops | Open (by design — new retention roll makes this less acute) |
| F-13 | SIM-X-03 | P2 | Weapon mismatch decisive at mass scale before Thread considered | Design correct |
| F-19 | SIM-X-05 | P2 | 11D vs 8D pool gap makes Grand Debate structurally predetermined | Open |
| F-20 | SIM-X-05 | P2 | W-41 correctly scoped; irrelevant in policy debates — confirmed design feature | Resolved |
| F-21 | SIM-X-05 | P2 | High-Composure NPCs (11+) immune to Rattled in standard 5-exchange Grand Debates | Open |
| F-24 | SIM-X-06 | P2 | Range mismatch more fight-determining than pool differential or wounds | Design correct |
| F-26 | SIM-X-07 | P2 | Templar CP=5 exceeds Church Military=4 ceiling — CP corrected to 4 | Resolved (corrected in sim) |
| F-27 | SIM-X-07 | P1 | Mass battle deadlock (HeavyCut vs HeavyArmour): no stalemate resolution mechanism | EDITORIAL PENDING |
| F-30 | SIM-X-07 | P1 | No Coup Counter successor rule on Grandmaster death | EDITORIAL PENDING |
| F-32 | SIM-X-08 | P2 | Debate loss raises Doctrine action Ob4→Ob5, ~58%→~42% — material seasonal impact | Design correct (intended consequence) |
| F-36 | SIM-X-08 | P2 | Extended stalemate battles produce zero faction consequences | EDITORIAL PENDING |

## Editorial Decisions Required

| ID | Decision needed |
|----|----------------|
| F-11 | W-33 fix: restore Cohesion to min(3, prior value), or add Strength component |
| F-27 | Stalemate resolution: define turn limit, Morale decay rate, or attrition rule |
| F-30/F-33 | Coup Counter: define successor officer or let threat evaporate on death |
| F-36 | Stalemate consequences: passive Morale decay per turn for no-damage engagements? |
