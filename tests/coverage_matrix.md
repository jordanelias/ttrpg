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

| SIM-X-13 | FR-D-01 Dissolution + Past-Oriented Pulling (hypothetical TS 70) | C+B | Single scene | RS, Coherence retention, Temporal Disjunction, Certainty | None | Maret Uln, Haelmund (Disjunction witness) | Evidence erasure, PO-Pull prerequisites | Complete |
| SIM-X-14 | Mode 2 Monstrous Entity + W-06b + Vaynard Discovery + Domain Echo | C+D | Single scene | RS, Coherence, Certainty, TC, Locked Zone proximity | Varfell, Niflhel, Crown | Vaynard, Maret, Niflhel Envoy, Crown Diplomat | Political scene interrupted by entity | Complete |
| SIM-X-15 | Knot crisis (Klapp/Ansel) + Certainty + Inspiration attack + Call a Knot | C+D | 3 exchanges | Coherence, Certainty, Knot strain, Composure, Inspiration | Church | Klapp, Olafsson, Ansel | Practitioner under interrogation + Knot crisis | Complete |
| SIM-X-16 | Collective Weave (Maret anchor + Klapp helper) + Rendering Crisis | C+B | Single scene | Coherence retention (both), Certainty (Klapp→0), RS, Knots | Varfell | Maret, Klapp | First collective operation + Rendering Crisis | Complete |

> Pre-v3 batch coverage archived in `deprecated/sim_coverage_matrix_legacy.md`.

## P1 Findings — Editorial Decisions Required

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-11 | X-03 | W-33 broken for Size≤2 units: Cohesion=2 insufficient when Size is binding constraint | RESOLVED — ST-TW-02 applied to threadwork_redesign_v25.md |
| F-27 | X-07 | Mass battle deadlock (HeavyCut vs HeavyArmour): no stalemate resolution rule | PATCHED — Add to mass_battle_v3: at 3+ consecutive turns with 0 damage dealt, units with no tactical option may withdraw one zone (costs movement, does not trigger pursuit). |
| F-30/F-33 | X-07/08 | Coup Counter: no successor rule on Grandmaster death | PROVISIONAL — On Grandmaster death with Coup Counter ≥ 1: Löwenritter selects highest-CR surviving named officer as acting Grandmaster. Coup Counter resets to 0. Provisional pending user approval. |
| F-43 | X-10 | Two Domain Actions can drop TC by 4+ in one season; no seasonal cap on TC | PROVISIONAL — TC change cap: ±3 per season from Domain Actions (±5 from all sources combined). Provisional pending user approval. |
| F-45 | X-10 | Church Stability brake scope — suppresses Mandate-based TC only or all TC sources? | EDITORIAL — ED-049 added to ledger |
| F-52 | X-12 | No Stability recovery mechanic for externally damaged faction Stability | PROVISIONAL — Stability recovery: +1 Stability per season of no hostile Domain Actions targeting that faction + Stability ≤ 3 (slow natural recovery). Provisional pending user approval. |

## Rules Gaps (No Patch Needed — GM Ruling Acceptable)

| ID | Source | Description |
|----|--------|-------------|
| F-38 | X-09 | Discovery Event mid-Debate: no interrupt rule; conservative ruling taken |
| F-41 | X-09 | No formal Impression rule for NPC TS-perception events during social scenes |
| F-48 | X-11 | CE track has no upper-ceiling distinction beyond Trajectory at CE 3 |

## Terminology Correction Applied

All prior SIM-X-01 through X-08 references to "Strength" as mass battle headcount stat corrected to **Size** in this index. Source files retain original text; correction is notional for tracking purposes only.

## New P1 Findings (SIM-X-13 through X-16)

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-58 | X-14 | RS 22 is 2 points from Dormant (Leap-disabled) threshold — any failed Weaving crosses the line globally | Open — campaign awareness item |

## New P2 Findings (SIM-X-13 through X-16)

| ID | Source | Description |
|----|--------|-------------|
| F-54 | X-13 | Past-Oriented Pulling TS 70+ hard gate correctly blocks TS 50 — gate works as designed |
| F-55 | X-13 | PO-Pulling "+1 additional" Coherence cost = +1 Ob on retention roll sum — correctly maps under new system |
| F-62 | X-15 | Certainty (Spirit=3) depletes to 1 after 2 Leaps — one more Leap triggers Rendering Crisis for low-Spirit practitioners |
| F-63 | X-15 | Knot strain from Dissonant Coherence reaches crisis threshold near-inevitably without recovery; Conversion makes recovery unlikely — correct self-reinforcing arc |
| F-66 | X-16 | Rendering Crisis fires post-Leap, not during contact — no interrupt rule; crisis doesn't retroactively affect the operation |
| F-69 | X-16 | Territorial Weave success (−1 Ob territory-wide) may be disproportionately powerful at low RS when Thread operations are most precious |

## Editorial Items (Open)

| ID | Source | Description |
|----|--------|-------------|
| F-70 | X-16 | Klapp Rendering Crisis: Belief revision content requires user input |
| F-45 | X-10 | Church Stability brake scope: suppresses only Mandate-based TC, or all TC sources? |
| F-52 | X-12 | Faction Stability recovery rate for externally damaged Stability — no rule defined |
| F-30 | X-07 | Coup Counter successor on Grandmaster death — no rule defined |
| F-27 | X-07 | Mass battle stalemate resolution — no rule defined |
| F-11 | X-03 | W-33 broken for CP≤2 units — EDITORIAL PENDING |
| F-43 | X-10 | Two Domain Actions can drop TC by 4+ in one season — no seasonal TC cap |
| SIM-D-01 | Debate: Argue/Read/CLASH/COMP/DIVERGE/TIE/Track/Composure/Concentration/Doubt/Regroup | TTRPG | CROSS | Composure, Concentration, Conviction Track | Generic (all factions modelled) | Generic archetypes | High-Pres orator, History-specialist, Low-social, Balanced social | Complete | F-D-01 (P1), F-D-02 (P2), F-D-03 (P2), F-D-04 (P2), F-D-06 (P2); SIM-DEBT-01 recalibrated |

| SIM-D-02 | Debate: Full scenario C+J — Himlensendt vs Baralta, 3-exchange Parliament, Diverge chain | TTRPG | PRESENT | TC, Composure, Concentration | Church, Hafenmark | Himlensendt, Baralta | Institutional authority, Legalist-constitutionalist | Complete | F-C-02 (P2 PP-100), F-C-04 (P1 ED-051), F-C-05 (P2 ED-052), F-C-06 (P1 cognitive load); SIM-DEBT-01 RESOLVED |

## SIM-DEBT Register

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| SIM-DEBT-01 | Debate system | RESOLVED. Mode C (SIM-D-02) confirmed: resistance dominates track movement; genre weight > pool size adjustments; 3-exchange Formal Debate → Compromise ~95%. CLASH strain calibration (2-3/exchange) analytically confirmed, scenario validation pending forced-CLASH run. | RESOLVED |
| AUD-TTRPG-01 | Modes A–G: Formula, Number Systems, Interaction Chains, Gap Detection, Core Principles, Playtest Burden, Cross-Mode | TTRPG | — | All tracks | All factions | All named NPCs | Full TTRPG mode | Complete | 11 P1s, 14 P2s, 4 P3s — see tests/aud_ttrpg_01.md |

## Provisional Decisions (from coverage matrix findings)

| Finding | Provisional Rule | Status |
|---------|-----------------|--------|
| F-27 | Mass battle stalemate: 3+ turns 0 damage → may withdraw one zone | Provisional — apply to mass_battle_v3 |
| F-30/F-33 | Coup Counter successor: highest-CR officer, Counter resets | Provisional — apply to designs/combat |
| F-43 | TC change cap: ±3/season Domain Actions, ±5 all sources | Provisional — apply to stage5_clocks or designs |
| F-52 | Stability recovery: +1/season with no hostile actions when Stability ≤ 3 | Provisional — apply to faction rules |


## New P1 Findings (SIM-D-01)

| ID | Source | Description | Status |
|----|--------|-------------|--------|
| F-D-01 | SIM-D-01 | DIVERGE+TIE: both score 0, different genres — Tie rule fires (any interaction type). | PP-097 PROVISIONAL |

## New P2 Findings (SIM-D-01)

| ID | Source | Description |
|----|--------|-------------|
| F-D-02 | SIM-D-01 | Regroup at Concentration=0: Spent ambiguous. PP-098: Regroup consumes Spent without penalty. |
| F-D-03 | SIM-D-01 | Obscuring in Divergence: orientation_weight undefined. PP-099: Doubt Marker rule applies. |
| F-D-04 | SIM-D-01 | Presence 1 cannot participate meaningfully in formal debate. Institutional gatekeeping implied. |
| F-D-06 | SIM-D-01 | Grand Debate + Corroboration: ~90 resolution steps. No GM reference card. Tooling gap. |
