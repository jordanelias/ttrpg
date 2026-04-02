# VALORIA GLOSSARY
## Terms, Abbreviations, and Acronyms
## Last updated: 2026-04-02
## Authority: This file is the canonical reference for all term expansions project-wide.
## Maintained by: valoria-orchestrator skill (update on any commit that introduces a new term)

---

## USAGE RULES

- All terms must be written in full in every document. Abbreviations may appear in parentheses immediately after the full term on first use per section: e.g. `Thread Sensitivity (TS)`.
- Subsequent uses in the same section: full term only.
- **Exceptions (abbreviation may stand alone):** `TN` (Target Number), `Ob` (Obstacle), `TTRPG`, `BG`.
- `TC` is a **collision abbreviation** — it has two distinct meanings depending on context. Do not use `TC` alone. Use the full term. See the TC entry below.

---

## PART ONE — GAME STATS AND ATTRIBUTES

### Core Attributes

| Full Term | Abbr | Range | Description |
|-----------|------|-------|-------------|
| Agility | — | 1–7 | Physical speed and coordination. Combat pool base. |
| Attunement | — | 1–7 | Sensitivity to people, environments, and Thread-adjacent phenomena. |
| Cognition | — | 1–7 | Reasoning, memory, analysis. |
| Endurance | — | 1–7 | Physical resilience. Determines Health and Stamina base. |
| Presence | — | 1–7 | Social force and rhetorical gravity. Debate pool base. |
| Spirit | — | 1–7 | Internal coherence, resolve, and Thread operation capacity. |
| Strength | — | 1–7 | Raw physical power. Weapon minimum requirement. |

### Derived Character Stats

| Full Term | Abbr | Formula / Range | Description |
|-----------|------|-----------------|-------------|
| Health | — | = Endurance | Wound track. Resets per wound. |
| Stamina | — | Endurance + History + 1 (armour-modified) | Combat resource. Degrades per round. |
| Coherence | — | 10→0 | Personal rendering stability for Thread practitioners. Starts at 10. |
| Intelligibility | — | 10→0 | How legibly reality presents to a fractured practitioner. Non-practitioners sense wrongness at threshold. |
| Composure | — | varies | Social endurance track. Used in Debate. Rattled at ≤ 2; concession forced at 0. |
| Focus | — | 1–5+ | Contact duration in Thread operation rounds. |
| Momentum | — | 0–4 | Tactical resource. Gained on Overwhelming success or Belief achieved. Spent for automatic successes (non-Thread only). |

### Thread Practitioner Stats

| Full Term | Abbr | Range | Description |
|-----------|------|-------|-------------|
| Thread Sensitivity | TS | 0–100+ | Perception depth and operation eligibility. Determines accessible operation scale. |
| Thread Pool Score | TPS | = Thread Sensitivity ÷ 10 (round down) | Bonus dice added to Thread operation pools. |
| Thread Depth | TD | **REMOVED (PP-166)** | Former stat; phantom definition from prior design iteration. Not tracked. Not used. |
| Thread Tension | TT | 0–100+ | Accumulated stress on the rendered world from Thread activity. Faction and world-scale tracker. |

---

## PART TWO — WORLD CLOCKS (SHARED TRACKS)

These are campaign-level trackers shared across all factions. All are event-driven (no automatic per-season advance except where noted).

| Full Term | Abbr | Range | Mode | Start | Loss Threshold | Description |
|-----------|------|-------|------|-------|----------------|-------------|
| Rendering Stability | RS | 100→0 | ALL | 60 (TTRPG) / 72 (BG) | 0 = The Rupture (campaign ends) | World coherence. Shared track. Degrades from Thread operations and seasonal effects. |
| Theocracy Counter | TC* | 0–100 | ALL | 0 (TTRPG) / 28 (BG) | 65 = Church Holy State (BG) | Church political dominance accumulation. Church-specific clock. Triggers territorial seizure at 60. |
| Institutional Pressure | IP | 0–100 | ALL | 20 | 75/80 = Altonian Vanguard (BG) | Pressure from the Altonian Empire. Invasion threat tracker. |
| Public Instability | PI | 0–10 | BG | 5 | 0 = Parliament dissolved + Löwenritter coup | Parliamentary health tracker. Board Game mode only. |

**\* TC COLLISION NOTE:** `TC` historically abbreviates both **Theocracy Counter** (this table) and **Conviction Track** (Debate system). These are distinct mechanics. Always use the full term. Never use the bare abbreviation `TC`.

---

## PART THREE — DEBATE SYSTEM TERMS

| Full Term | Abbr | Range / Type | Description |
|-----------|------|--------------|-------------|
| Conviction Track | CT* | 0–10 | Debate position tracker. Side A wins at ≥ 7; Side B wins at ≤ 3. Compromise zone: 4–6. |
| Concentration | — | varies | Debate resource spent to sustain rhetorical positions. |
| Doubt Marker | — | token | Applied on Obscuring loss in Diverge state. |
| Composure | — | varies | Social endurance (see Part One). Also the damage track in Debate exchanges. |
| Genre | — | Past / Present / Future | Debate argument type selection each exchange. |
| Orientation | — | Revealing / Obscuring | Debate stance selection each exchange. |
| Interaction Type | — | CLASH / AMPLIFY / CROSS / DIVERGE | Determined by Genre + Orientation match between orators. |

**\* CT NOTE:** `CT` is the preferred abbreviation for Conviction Track to avoid collision with Theocracy Counter. However, even `CT` should not be used alone — write "Conviction Track" in full.

---

## PART FOUR — FACTION STATS

All factions tracked on 1–7 scale (0 = collapse / inoperability for most stats). Board Game mode only unless noted.

| Full Term | Abbr used in tables | Description |
|-----------|---------------------|-------------|
| Mandate | M | Institutional authority and political legitimacy. 0 = Collapse state. |
| Influence | I | Social and cultural reach. Cannot drop below 1 (faction remains extant). |
| Wealth | W | Economic capacity. 0 = cannot Trade or fund Wealth-requiring actions. |
| Military | Mil | Military power. 0 = cannot Muster. |
| Intel | Int | Intelligence capacity. |
| Stability | Sta | Internal coherence. 0 = Collapse trigger (P-15). |
| Standing | — | 0–10 | Reputation track. No in-game benefit above 7; 10 is cosmetic maximum. |

**Note:** Single-letter column header abbreviations (M, I, W, Mil, Int, Sta) are acceptable in table headers where the table is preceded by a full-term legend. Do not use single-letter abbreviations in prose.

---

## PART FIVE — COMBAT TERMS

| Full Term | Abbr | Description |
|-----------|------|-------------|
| Combat Endurance | CE | Stamina resource tracking in extended combat. |
| Coherence Rating | CR | Unit-level cohesion stat in mass battle. Range varies by unit type. Replaced Thread Coherence as label in mass combat context (unrelated to personal Coherence stat). |
| Damage Resistance | DR | Armour mitigation value. Reduces damage received. |
| Target Number | TN | **Exception — abbreviation permitted standalone.** The die face threshold for a success (6, 7, or 8 depending on context). |
| Obstacle | Ob | **Exception — abbreviation permitted standalone.** The number of net successes required for a Success result. |

---

## PART SIX — DICE ENGINE TERMS

| Full Term | Abbr | Description |
|-----------|------|-------------|
| Target Number | TN | Permitted standalone. Threshold for a die to count as a success. |
| Obstacle | Ob | Permitted standalone. Required net successes for a Success result. |
| Expected Value | EV | Probability-weighted average outcome per die or pool. Used in simulation analysis. |
| Degree of Success | — | Outcome tier: Overwhelming / Success / Partial / Failure. |
| Overwhelming | — | Net successes ≥ 2× Ob (TTRPG); ≥ Ob + 1 (BG, provisional). |
| Partial | — | Net successes > 0 but < Ob. |

---

## PART SEVEN — WORLD / NARRATIVE TERMS

| Full Term | Abbr | Description |
|-----------|------|-------------|
| Gap | — | A rupture in the rendered substrate. Severity scales: Micro-Gap, Standard Gap, Entrenched Gap, Catastrophic Gap. |
| Shifting Object | — | Pre-Gap substrate instability. Less severe than a Gap; addressable by Mending. |
| Locked Zone | — | Territory or object subjected to Forced Resolution Lock. |
| Monstrous Incursion | — | Entity manifestation triggered by low Rendering Stability or severe Dissolution failure. |
| The Rupture | — | Campaign-ending event when Rendering Stability reaches 0. |
| Knot | — | A significant relationship bond (Close / Regular / Distant). Mechanically tracked with strain. |
| Belief | — | Player-authored character conviction. Mechanical driver for Momentum and Character Points. |
| Inspiration | — | Named focus that grants bonus dice when engaged in relevant scenes. |
| History | — | Skill-equivalent. Specific experiential knowledge that grants bonus dice. Cap = Memory score. |
| Character Point | CP | Advancement currency earned through Beliefs and session milestones. |
| Domain Echo | — | Faction-level consequence triggered by decisive Debate outcomes. |
| Grievance Marker | — | Token placed on a faction after hostile Niflhel action. |
| Co-Movement Card | — | Board Game mechanism for Thread co-movement; drawn on every Thread operation result. |
| Einhir | — | Pre-colonial indigenous culture of the Southernmost territories. Cultural/political axis. |

---

## PART EIGHT — THREAD OPERATION TYPES

| Full Term | Abbr | Description |
|-----------|------|-------------|
| Weaving | — | Things Cohere. Stabilises threads, restores actualisation. |
| Pulling | — | Things Open. De-actualises threads; Present-Oriented and Past-Oriented variants. |
| Past-Oriented Pulling | POP | Pulling operation targeting historical thread configurations. Requires Thread Sensitivity 70+. |
| Locking | — | Forced Resolution; stabilises a thread configuration permanently. Requires Thread Sensitivity 50+. |
| Dissolution | — | Forced Resolution; destroys a thread configuration. Requires Thread Sensitivity 50+. |
| Mending | — | Substrate repair. Targets Gaps and Shifting Objects. Requires Thread Sensitivity 50+. |
| Diagnosis | — | Mandatory pre-operation read. No roll. Required before Mending, Locking, Dissolution, Past-Oriented Pulling. |
| Leap | — | Entering Thread contact. Prerequisite for all Thread operations. Full-round action (Priority 5). |
| Forced Resolution | FR | Collective term for Locking and Dissolution operations. TN 8. No Thread Pool Score added. |
| Dissolution Residue | — | Potency-rated bonus dice source from prior Dissolution. Costs −1 Coherence per use. |
| Overweaving | — | Penalty state from multiple operations on same configuration in one contact window. +1 Ob per op after first. |

---

## PART NINE — SIMULATION / INFRASTRUCTURE TERMS

| Full Term | Abbr | Description |
|-----------|------|-------------|
| Target Number | TN | Permitted standalone. |
| Obstacle | Ob | Permitted standalone. |
| Simulation Identifier | SIM-NNN | ID format for simulation test outputs. E.g. SIM-D-01, SIM-X-08. |
| Patch | PP-NNN | Mechanical patch identifier. PP = patch prefix; NNN = sequential number. |
| Editorial Decision | ED-NNN | Editorial decision requiring user approval. Tracked in canon/editorial_ledger.yaml. |
| Simulation Debt | SIM-DEBT-NNN | Outstanding simulation recalibration needed after a mechanical change. |
| Game Master | GM | The person running the game (TTRPG/Hybrid mode). |
| Non-Player Character | NPC | A character controlled by the Game Master, not a player. |
| Player Character | PC | A character controlled by a player. |
| Expected Value | EV | Average result of a probability distribution. Used in simulation analysis. |
| Burning Wheel | BW | Precedent game (Burning Wheel by Luke Crane). Referenced in cognitive load / precedent analysis. |
| Artificial Intelligence | AI | Non-Player Character decision logic in Board Game mode (NPC faction behaviour trees). |
| Hybrid | HYB | The Hybrid game mode bridging TTRPG and Board Game. "Hybrid" preferred; "HYB" not for standalone use. |

---

## PART TEN — GAME MODE LABELS

| Full Term | Abbr | Notes |
|-----------|------|-------|
| Tabletop Roleplaying Game | TTRPG | **Exception — abbreviation permitted standalone.** The baseline game mode. |
| Board Game | BG | **Exception — abbreviation permitted standalone.** The strategic abstraction mode. |
| Hybrid | HYB | Bridge mode. Write in full; do not use HYB alone. |

---

## PART ELEVEN — COLLISION / DISAMBIGUATION TABLE

Terms whose abbreviations conflict with another term. Never use these abbreviations standalone.

| Abbreviation | Meaning A | Meaning B | Resolution |
|-------------|-----------|-----------|------------|
| TC | Theocracy Counter (Church faction clock, 0–100) | Conviction Track (Debate position tracker, 0–10) | Write full term always. |
| TD | Thread Depth | Top-Down (Mermaid flowchart directive) | Thread Depth is a phantom stat (REMOVED PP-166). `flowchart TD` is valid Mermaid syntax — not a game term. |
| COMP | Composure (Debate context) | Computation / Composition (general English) | Write "Composure" in game documents. |

---

## PART TWELVE — TERMS FLAGGED AS UNRESOLVED

The following abbreviations appeared in skill files but could not be confirmed against any design document. They are removed from all tracking lists pending definition.

| Abbreviation | Suspected Meaning | Status |
|-------------|-------------------|--------|
| CERT | Unknown — possibly "Certainty" (a character track referenced in batch_d_designs) | [GAP: full name unconfirmed] |
| TLK | Unknown — possibly "Talk" or a social action abbreviation | [GAP: full name unconfirmed] |
| DD | Unknown — possibly "Domain Dice" or a date format artefact | [GAP: full name unconfirmed] |
| CE (track code) | Listed as track code in old simulator header; "Combat Endurance" expansion assumed | [GAP: confirm or replace] |
| FSTAT | Unknown — possibly "Faction Stat" | [GAP: full name unconfirmed] |
| INT (track code) | Listed as track code in old simulator header; possibly "Intel" faction stat | [GAP: confirm or replace] |

---

*Glossary maintained by valoria-orchestrator. Update in the same commit as any file that introduces or retires a term.*
