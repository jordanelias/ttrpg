# VALORIA GLOSSARY
## Terms, Abbreviations, and Acronyms
## Last updated: 2026-04-30
## Authority: This file is the canonical reference for all term expansions project-wide.
## Maintained by: valoria-orchestrator skill (update on any commit that introduces a new term)

---

## VALORIA TARGET CONTEXT

Valoria is a videogame (Godot 4.6), not a tabletop product. Mode labels (TTRPG / BG / Hybrid) below are **mechanical layers of the videogame**, not separate deliverables: TTRPG = personal-scale resolution layer; BG = strategic layer; Hybrid = bridge / scale-transition mechanism. Names retained as design-source-of-truth from the multi-mode origin. There is no GM — the engine handles all resolution; the term `Game Master` in §9 is preserved as design-source vocabulary mapped to engine resolution authority in implementation.

---

## USAGE RULES

- All terms must be written in full in every document. Abbreviations may appear in parentheses immediately after the full term on first use per section: e.g. `Thread Sensitivity (TS)`.
- Subsequent uses in the same section: full term only.
- **Exceptions (abbreviation may stand alone):** `TN` (Target Number), `Ob` (Obstacle), `TTRPG`, `BG`.
- **`CI` is no longer used** — historically ambiguous between Church Influence (renamed to Church Influence / CI per ED-782) and Piety Track (CT). Use `CI` for the Church clock; write `Piety Track` in full elsewhere. Residual CI sweep completed for `npc_behavior_v30.md` 2026-04-30 (PP-691); incidental CI residuals in other docs are queued in `references/censured_vocabulary.yaml`.

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
| Health | HP* | = Endurance | Wound track. Resets per wound. *HP not standalone — write Health.* |
| Stamina | — | Endurance + History + 1 (armour-modified) | Combat resource. Degrades per round. |
| Coherence | — | 10→0 | Personal rendering stability for Thread practitioners. Starts at 10. **Coherence is what's broken** in a fractured practitioner. |
| Intelligibility | — | 10→0 | How legibly reality presents to a fractured practitioner. **Intelligibility is what they perceive of the breakage**. Non-practitioners sense wrongness at threshold. |
| Composure | — | varies | Social endurance track. Used in Debate. Rattled at ≤ 2; concession forced at 0. |
| Focus | — | 1–5+ | Contact duration in Thread operation rounds. |
| Certainty | CERT* | 0–5 | Cosmological worldview track (PP-551). Solmund orthodoxy (5) → Thread acceptance (0). All PCs have it; named NPCs at GM discretion; factions do not hold Certainty. *CERT not standalone — write Certainty.* |
| Momentum | — | 0–4 | Tactical resource. Gained on Overwhelming success or Belief achieved. Spent for automatic successes (non-Thread only). |

### Thread Practitioner Stats

| Full Term | Abbr | Range | Description |
|-----------|------|-------|-------------|
| Thread Sensitivity | TS | 0–100+ | Perception depth and operation eligibility. Determines accessible operation scale. |
| Thread Pool Score | TPS | = Thread Sensitivity ÷ 10 (round down) | Bonus dice added to Thread operation pools. |
| Thread Depth | TD | **REMOVED (PP-166)** | Former stat; phantom definition from prior design iteration. Not tracked. Not used. |
| Thread Tension | TT | 0–100+ | Accumulated stress on the rendered world from Thread activity. Faction and world-scale tracker. **TT and Mending Stability run in opposite directions on the same world-state axis** — TT accumulates stress, MS measures coherence remaining. |

---

## PART TWO — WORLD CLOCKS (SHARED TRACKS)

These are campaign-level trackers shared across all factions. All are event-driven (no automatic per-season advance except where noted).

| Full Term | Abbr | Range | Mode | Start | Loss / Milestone Thresholds | Description |
|-----------|------|-------|------|-------|----------------------------|-------------|
| Mending Stability | MS | 100→0 | ALL | 60 (TTRPG) / 72 (BG) | 0 = The Rupture (campaign ends) | World coherence. Shared track. Degrades from Thread operations and seasonal effects. **Renamed from Rendering Stability (RS) per ED-731.** |
| Church Influence | CI | 0–100 | ALL | 0 (TTRPG) / 28 (BG) | 40 = Church Assertive · 55 = Institutional Reach · 60 = Mass Seizure available (probabilistic declaration P = ((CI−60)/40)^3.3 per season — supersession_register entry 250715f) · 65 = Church Dominant · 80 = Church Ascendant · 100 = Theocracy Unification Attempt | Church political dominance accumulation. Church-specific clock. Per `designs/provincial/ci_political_v30.md` §2.1 (canonical). **Renamed from "Church Influence" (CI) per ED-782.** Old 75 = Phase Transition / Territorial Seizure threshold REMOVED — Mass Seizure now probabilistic from CI ≥ 60. |
| Institutional Pressure | IP | 0–100 | ALL | 20 | 75/80 = Altonian Vanguard (BG) | Pressure from the Altonian Empire. Invasion threat tracker. |
| Public Instability | PI | 0–10 | BG | 5 | 0 = Parliament dissolved + Löwenritter coup | Parliamentary health tracker. Board Game mode only. |

**Old CI = Church Influence rename:** ED-782 retired the abbreviation. New content uses `CI`. Residual `CI` references in `npc_behavior_v30.md` (16 paragraphs) swept by PP-691. Other corpus residuals queued for cleanup; see `canon/supersession_register.yaml` and `references/censured_vocabulary.yaml`. **Do not introduce `CI` in new content.**

---

## PART THREE — DEBATE SYSTEM TERMS

| Full Term | Abbr | Range / Type | Description |
|-----------|------|--------------|-------------|
| Piety Track | CT* | 0–10 | Debate position tracker. Side A wins at ≥ 7; Side B wins at ≤ 3. Compromise zone: 4–6. Canonical doc: `designs/personal/conviction_track_v1.md` (promoted PP-681). |
| Concentration | — | varies | Debate resource spent to sustain rhetorical positions. |
| Doubt Marker | — | token | Applied on Obscuring loss in Diverge state. |
| Composure | — | varies | Social endurance (see Part One). Also the damage track in Debate exchanges. |
| Genre | — | Past / Present / Future | Debate argument type selection each exchange. |
| Orientation | — | Revealing / Obscuring | Debate stance selection each exchange. |
| Interaction Type | — | CLASH / AMPLIFY / CROSS / DIVERGE | Determined by Genre + Orientation match between orators. |

**\* CT NOTE:** `CT` is the preferred abbreviation for Piety Track. Even `CT` should not stand alone — write "Piety Track" in full.

---

## PART FOUR — FACTION STATS

Most stats below tracked on 1–7 scale (0 = collapse / inoperability for most stats); Standing is the exception (0–10, see note). Board Game mode only unless noted.

| Full Term | Abbr used in tables | Description |
|-----------|---------------------|-------------|
| Mandate | M | Institutional authority and political legitimacy. 0 = Collapse state. |
| Influence | I | Social and cultural reach. Cannot drop below 1 (faction remains extant). |
| Wealth | W | Economic capacity. 0 = cannot Trade or fund Wealth-requiring actions. |
| Military | Mil | Military power. 0 = cannot Muster. |
| Intel | Int | Intelligence capacity. |
| Stability | Sta | Internal coherence. 0 = Collapse trigger (P-15). |
| Standing | — | Reputation track. Range 0–10 (exception to 1–7 scale). No in-game benefit above 7; 10 is cosmetic maximum. |

**Note:** Single-letter column header abbreviations (M, I, W, Mil, Int, Sta) are acceptable in table headers where the table is preceded by a full-term legend. Do not use single-letter abbreviations in prose.

---

## PART FIVE — COMBAT TERMS

| Full Term | Abbr | Description |
|-----------|------|-------------|
| Combat Endurance | CE | Stamina resource tracking in extended combat. Sub-application of Stamina (Part One); not a separate stat track. |
| Command | — | Unit commander stat in mass battle. ⌈(Presence + Cognition) ÷ 2⌉. Caps both Size contribution to pool and Discipline contribution to Health. (PP-232) |
| Damage Resistance | DR | Armour mitigation value. In mass combat: component of Health per Size formula. |
| Size | — | Unit headcount stat (replaces Strength). At 0: unit destroyed. Pool contribution capped at Command. (PP-232) |
| Power | — | Unit offensive quality (replaces Combat Power, PP-232/PP-233). Damage per success = 1 + Power. Derived from unit type. |
| Discipline | — | Unit organisational integrity (replaces Cohesion, PP-232). Contribution to Health per Size capped at Command. |
| Health per Size | H | min(Discipline, Command) + DR. Used to derive Total Health and current Size. (PP-233) |
| Total Health | — | Size × H. Full Size always used regardless of Command cap. (PP-233) |

For dice mechanics — Target Number (TN) and Obstacle (Ob) — see Part Six.

---

## PART SIX — DICE ENGINE TERMS

| Full Term | Abbr | Description |
|-----------|------|-------------|
| Target Number | TN | **Exception — abbreviation permitted standalone.** The die face threshold for a success (6, 7, or 8 depending on context). |
| Obstacle | Ob | **Exception — abbreviation permitted standalone.** The number of net successes required for a Success result. |
| Expected Value | EV | Probability-weighted average outcome per die or pool. Used in simulation analysis. |
| Degree of Success | — | Outcome tier: Overwhelming / Success / Partial / Failure. |
| Overwhelming | — | Net successes ≥ 2× Ob AND ≥ 3 minimum (TTRPG, PP-232); ≥ Ob + 1 (BG, provisional). |
| Partial | — | Net successes > 0 but < Ob. |

---

## PART SEVEN — WORLD / NARRATIVE TERMS

| Full Term | Abbr | Description |
|-----------|------|-------------|
| Gap | — | A rupture in the rendered substrate. Severity scales: Micro-Gap, Standard Gap, Entrenched Gap, Catastrophic Gap. |
| Shifting Object | — | Pre-Gap substrate instability. Less severe than a Gap; addressable by Mending. |
| Locked Zone | — | Territory or object subjected to Forced Resolution Lock. |
| Monstrous Incursion | — | Entity manifestation triggered by low Mending Stability or severe Dissolution failure. |
| The Rupture | — | Campaign-ending event when Mending Stability reaches 0. |
| Knot | — | A significant relationship bond (Close / Regular / Distant). Mechanically tracked with strain. Lifecycle specified per ED-773. |
| Belief | — | Player-authored character conviction. Mechanical driver for Momentum and Character Points. Distinct from Inspiration (see below). |
| Inspiration | — | Named focus that grants bonus dice when engaged in relevant scenes. Distinct from Belief (which drives Momentum/CP) and History (which is experiential skill). Per ED-779. |
| History | — | Skill-equivalent. Specific experiential knowledge that grants bonus dice. Cap = Memory score. |
| Character Point | CP | Advancement currency earned through Beliefs and session milestones. **CP refers to Character Points only** (ED-136); see PART TWELVE collision entry. |
| Disposition | — | NPC-attached attitude state toward another entity (PC, faction, settlement). Drives behaviour-tree branching in NPC AI. Canonical in `designs/npcs/npc_behavior_v30.md`; no separate first-class doc. Heavy cascade-terminal (Mode D — 391 chains). |
| Domain Action | — | Faction-level strategic action resolved at scale-transition phase. Mechanically the unit of strategic-layer decision. Canonical in `designs/architecture/scale_transitions_v30.md` + `designs/provincial/faction_layer_v30.md`; no separate first-class doc. Heavy cascade-terminal (Mode D — 346 chains). |
| Domain Echo | — | Faction-level consequence triggered by decisive Debate outcomes. |
| Grievance Marker | — | Token placed on a faction after hostile covert action. Originally scoped to Niflhel hostile action; Niflhel-as-faction struck per ED-764, scope extended to any covert/hostile action. |
| Co-Movement Card | — | Strategic-layer mechanism for Thread co-movement; resolved on every Thread operation result. (BG layer — name reflects card-economy origin; engine implementation is automatic on Thread-operation-completion event.) |
| Einhir | — | Pre-colonial indigenous culture of the Southernmost territories. Cultural/political axis. |
| Arc | — | Narrative sequence — a bounded structural unit within the emergent campaign framework. Arcs are designed in batches (arcs_01-04, arcs_05-09, etc.) and tracked in designs/arcs/. See `designs/arcs/arc_expansion_v30.md`. |
| Zoom In | — | Scale transition from larger (faction/territorial) to smaller (personal/scene) scale. Mechanically implemented as a transition phase during Domain Action resolution. See `designs/architecture/scale_transitions_v30.md` §4. |
| Zoom Out | — | Scale transition from smaller (personal/scene) to larger (faction/territorial) scale. Reverse of Zoom In. |
| Cardinal | — | Title for a senior Church official with Great Influence in the Church of Solmund. Four-Cardinal Structure governs the Church hierarchy. See `designs/npcs/npc_roster_v30.md` for named Cardinals (Prudence, Justice, Gifts, Temperance). |

---

## PART EIGHT — THREAD OPERATION TYPES

| Full Term | Abbr | Description |
|-----------|------|-------------|
| Weaving | — | Things Cohere. Stabilises threads, restores actualisation. |
| Pulling | — | Things Open. De-actualises threads. **Default sense is Present-Oriented**; see also Past-Oriented Pulling. |
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
| Simulation Identifier | SIM-NNN | ID format for simulation test outputs. E.g. SIM-D-01, SIM-X-08. |
| Patch | PP-NNN | Mechanical patch identifier. PP = patch prefix; NNN = sequential number. |
| Editorial Decision | ED-NNN | Editorial decision requiring user approval. Tracked in `canon/editorial_ledger.yaml`. |
| Simulation Debt | SIM-DEBT-NNN | Outstanding simulation recalibration needed after a mechanical change. |
| Game Master | GM | Design-source-of-truth role term. **In Valoria's videogame target there is no GM** — engine handles all resolution. The term persists in design corpus as legacy taxonomy; in implementation it maps to engine resolution authority (priority systems, scripted scene resolution, NPC AI orchestration). The bare-`GM` corpus sweep is queued; new content should use "engine" or write "Game Master" in full only when referring to the design-source taxonomic role. |
| Non-Player Character | NPC | A character not controlled by the player. In implementation: AI-driven entity with behaviour-tree decision logic per `designs/npcs/npc_behavior_v30.md`. |
| Player Character | PC | A character controlled by a player. |
| Burning Wheel | BW | Precedent game (Burning Wheel by Luke Crane). Referenced in cognitive load / precedent analysis. **Design-precedent term**; not an in-game mechanic. |
| Artificial Intelligence | AI | Behaviour-tree decision logic for NPC-controlled factions/characters. See `designs/npcs/npc_behavior_v30.md`. |

For Expected Value (EV) / Target Number (TN) / Obstacle (Ob) — see Part Six.

---

## PART TEN — GAME MODE LABELS (videogame mechanical layers)

| Full Term | Abbr | Notes |
|-----------|------|-------|
| Tabletop Roleplaying Game | TTRPG | **Exception — abbreviation permitted standalone.** Personal-scale resolution layer of the Valoria videogame. Source-of-truth name retained from multi-mode origin. |
| Board Game | BG | **Exception — abbreviation permitted standalone.** Strategic layer of the Valoria videogame. |
| Hybrid | HYB | Bridge mode / scale-transition mechanism. Write in full; do not use HYB alone. |

---

## PART ELEVEN — TOP-LEVEL SYSTEMS (non-stat, non-mechanic)

These are canonical-authority systems with their own design docs. Hub-centrality terms per Mode A / Mode C of `designs/audit/2026-04-30-terminology-vector-audit/`.

| Full Term | Canonical doc | Description |
|-----------|---------------|-------------|
| Turmoil | `designs/provincial/peninsular_strain_v30.md` | Cross-cutting world-scale pressure system (T-07 throughline). Multi-graph hub (Mode A — top quintile in cite + mu + pp). |
| Conflict Architecture | `designs/architecture/conflict_architecture_proposal.md` | Architectural specification for conflict resolution across scales. Niflhel dissolution + Löwenritter graduated autonomy + Tensions Deck + Royal Assassination Fuse all anchored here. |
| Campaign Architecture | `designs/architecture/campaign_architecture_v30.md` | Architectural specification for campaign-scale structure: phase ordering, season cadence, scale-transition orchestration. |
| Victory | `designs/provincial/victory_v30.md` + `params/bg/victory.md` | Win-condition specification across factions. Faction-specific victory paths (Crown / Church / Hafenmark / Varfell / Löwenritter / RM / Guilds). |
| CI Political | `designs/provincial/ci_political_v30.md` | Church Influence political dynamics — milestones, seizure mechanics, Theocracy Unification spec. Renamed from `tc_political_redesign_v30` (same doc, CI = Church Influence's politically-active form per `references/canonical_sources.yaml` note). |

Other canonical / provisional systems (registration pending in alias_registry — see `references/canonical_sources.yaml` for authoritative system map): Settlement Adjacency, Fractional Province Ownership, Faction Succession Split, Tensions Deck, Royal Assassination Fuse, MS Trajectory, Approach Training, Wrong-Style Penalty, Heresy Investigation Lifecycle, Knot Lifecycle, Demotion Magnitude, Miraculous Event, Solmund Voice / Philosophy / Artifacts.

---

## PART TWELVE — COLLISION / DISAMBIGUATION TABLE

Terms whose abbreviations conflict with another term. Never use these abbreviations standalone.

| Abbreviation | Meaning A | Meaning B | Resolution |
|-------------|-----------|-----------|------------|
| CI | ~~Church Influence~~ (renamed CI per ED-782) | ~~Piety Track~~ (now CT) | **Do not use CI.** Write `CI` for Church Influence; `Piety Track` (or `CT` in technical contexts) for the debate tracker. |
| CP | Character Points (advancement currency) | ~~Combat Power~~ (renamed Power — PP-232) | CP = Character Points only [ED-136]. Use "Power" for the unit offensive stat. |
| TD | ~~Thread Depth~~ (REMOVED PP-166) | Top-Down (Mermaid flowchart directive) | Thread Depth is a phantom stat (REMOVED PP-166). `flowchart TD` is valid Mermaid syntax — not a game term. |
| COMP | Composure (Debate context) | Computation / Composition (general English) | Write "Composure" in game documents. |
| RS | ~~Rendering Stability~~ (renamed MS per ED-731) | — | Use Mending Stability (MS). RS appears only as historical annotation in `canon/02_foundations_amendment_leap_mechanism.md` per intentional retention. |

---

## PART THIRTEEN — DEPRECATED / RESOLVED ABBREVIATIONS

(Replaces former Part 12 "TERMS FLAGGED AS UNRESOLVED" — all entries previously flagged are now resolved per `references/alias_registry.yaml` `deprecated_abbreviations` block.)

| Abbreviation | Resolution | Status |
|-------------|------------|--------|
| CERT | Certainty (cosmological worldview track, 0–5; PP-551). See Part One. | RESOLVED — active stat |
| TLK | Torben Loyalty Clock (narrative-specific, 10→0; F72 gap). | DEPRECATED — historical only |
| DD | Deniability Debt (Niflhel Operative mechanic). Niflhel-as-faction struck per ED-764; mechanic survives as "Deniability Debt" full term where retained. | DEPRECATED — abbreviation not in active use |
| FSTAT | Faction Stats (collective shorthand for Mandate / Influence / Wealth / Military / Intel / Stability). | DEPRECATED — simulator code, never in-game term |
| CE (track code) | Combat Endurance (resolved). See Part Five. | RESOLVED — active stat |
| INT (track code) | Intel (`Int` faction stat). See Part Four. | RESOLVED — active stat |

For the canonical authority on deprecated abbreviations, see `references/alias_registry.yaml` `deprecated_abbreviations` and `legacy_renames` blocks.

---

## SIM-DEBT NOTE (PP-233)
DR contribution to Health per Size means heavily armoured units accumulate Health fast. H = min(Discipline,Command) + DR — heavy armour (DR 2) adds 40% more Health than unarmoured at equal Discipline. Interaction with armour-dependent Power modifiers needs simulation before values are treated as calibrated. Logged as SIM-DEBT-03.

---

## CHANGELOG

- **2026-04-30 (PP-691):** P0 propagation pass following terminology vector-audit. CI thresholds reconciled to ci_political_v30 §2.1 canonical (40 / 55 / 60 probabilistic / 65 / 80 / 100). Added Disposition + Domain Action (Mode D cascade sinks). Added new Part Eleven for top-level systems (Turmoil, Conflict Architecture, Campaign Architecture, Victory, CI Political — Mode A hubs). Old Part Twelve (UNRESOLVED) replaced by new Part Thirteen (DEPRECATED / RESOLVED) reflecting alias_registry deprecated_abbreviations. Old Part Eleven (collision table) renumbered to Part Twelve. Added VG-target preamble and Game Master engine-resolution note. RS legacy entry added to collision table. Coherence vs Intelligibility disambiguation. TT/MS opposite-direction note. CE relationship to Stamina clarified. Inspiration/Belief/History distinction added.
- 2026-04-24 (PP-678): Game Master full-phrase corpus sweep. Cardinal naming reconciled. Earlier glossary touchpoints.

*Glossary maintained by valoria-orchestrator. Update in the same commit as any file that introduces or retires a term.*
