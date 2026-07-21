# VALORIA — MECHANICAL TERMS INDEX
## Diagnostic Glossary: All Mechanical Terms by Silo + Cross-Silo Diagnostics

**Status:** PROPOSAL — diagnostic deliverable for vocabulary audit, not yet committed to canonical sources.
**Date:** 2026-05-08
**Disposition (RATIFIED 2026-07-08, ED-IN-0029 docket, OPT-AV-14):** permanent historical snapshot,
no live regeneration (its would-be regenerator is the dead `tools/valoria_collator.py`, CLAUDE.md §8).
Flagged as the best candidate among the six sampled secondary indices for a future re-platform as
live A17/A18 signal, if that work is ever prioritized — not done by this ruling.
**Purpose:** complete enumeration of mechanical terms organized into vocabulary-isolated silos, with diagnostic registers identifying cross-silo overlaps, attribute↔mechanic word-class violations, synonym candidates, orphan terms, and deprecated/superseded terms. Designed as a working tool for identifying overlap, duplication, and confusion across the system corpus.

---

## §0 — PURPOSE AND USE

### §0.1 What this file is

This is the **single-place enumeration** of every mechanical term in the Valoria corpus, organized by play-system silo. The intent is that **each system of play has its own vocabulary** — investigation terms differ from combat terms differ from debate terms — and **character/faction characteristics do not collide with mechanic words**.

### §0.2 How to use it

- **§1 PER-SILO ENUMERATION** — find a term by silo. Each silo lists every term it owns.
- **§2 CROSS-SILO OVERLAP MATRIX** — find terms that appear in two or more silos. Three classes: intentional polysemy (kept), accidental duplicates (rename), word-class violations (rename mandatory).
- **§3 ATTRIBUTE↔MECHANIC COLLISION REGISTER** — explicit audit against the rule that attribute words must not collide with mechanic words. The single-place verdict per term.
- **§4 SYNONYM REGISTER** — different words for the same concept; canonical winner marked.
- **§5 ORPHAN TERMS** — terms surfaced in design docs that haven't been routed to a silo yet.
- **§6 DEPRECATED / SUPERSEDED REGISTER** — retired terms; should not appear in active docs.

### §0.3 Sources

Built from 80 cached design files (~1.08 MB) including:
- All `references/` curated artifacts (glossary, alias_registry, values_master, censured_vocabulary, design_registry, proper_noun_registry, etc.)
- 17 canonical system docs from `references/canonical_sources.yaml` plus their auxiliary docs
- All `params/` parameter files, `params/bg/` strategic-mode files, `params/factions/` faction-specific files
- All `designs/scene/` (combat_v30, social_contest_v30, fieldwork_v30, investigation_systems_v30, conviction_track_v30, derived_stats_v30, miraculous_event_v30)
- All `systems/threadwork/`, `designs/personal/`, `systems/_architecture/`, `systems/articulation/`, `systems/settlements/`, `systems/world/`
- `canon/01_foundations_amendment_self_rendering.md`, `canon/02_foundations_amendment_leap_mechanism.md`

Algorithmic extraction surfaced 2,166 candidate terms with 131 cross-silo overlaps; this file presents the curated set with diagnostic verdicts.

### §0.4 Silo taxonomy (16 silos + 4 diagnostic registers)

| Silo | What it owns |
|------|--------------|
| §1 | Character attributes (entity properties — what a person *is*) |
| §2 | Faction attributes |
| §3 | Territory attributes |
| §4 | World / cosmological state |
| §5 | **Combat (all scales — personal + mass)** |
| §6 | Personal resolution: Social Contest (Debate) |
| §7 | Personal resolution: Threadwork |
| §8 | Personal resolution: Fieldwork (Exploration / Investigation / Socializing / Exposure) |
| §9 | **Piety & Church Influence** |
| ~~§10~~ | ~~Mass Combat~~ → **merged into §5** |
| §11 | Strategic resolution: Faction Layer / Domain Actions |
| §12 | Strategic resolution: Clocks (dedicated clock mechanics only) |
| §13 | Strategic resolution: Tensions Deck / Royal Assassination / Special |
| §14 | Strategic resolution: Victory Paths |
| §15 | Scale-bridging |
| §16A | Dice engine (system-agnostic resolution primitives) |
| §16B | Authoring / Infrastructure (meta — not in-game) |

Diagnostic registers:
| §  | Register |
|----|----------|
| §2-overlap | Cross-Silo Overlap Matrix |
| §3-collision | Attribute ↔ Mechanic Collision Register |
| §4-synonym | Synonym Register |
| §5-orphan | Orphan Terms |
| §6-deprecated | Deprecated / Superseded Register |

---

# PART ONE — PER-SILO ENUMERATION

## SILO 1 — CHARACTER ATTRIBUTES (entity properties — what a person *is*)

> **Word-class rule:** these are nouns naming what the actor possesses. They MUST NOT collide with mechanic verbs (Lock, Pull, Mend, Weave, etc.) or process nouns (Roll, Pool, Phase, Action). Collisions flagged in §X-overlap.

### 1.1 Core Attributes (1–7 scale, character-level)
| Term | Abbr | Range | Definition | Source |
|------|------|-------|------------|--------|
| Agility | — | 1–7 | Physical speed and coordination. Base for Combat Pool. | params/core.md, glossary §1 |
| Attunement | — | 1–7 | Sensitivity to people, environments, Thread-adjacent phenomena. | params/core.md |
| Cognition | — | 1–7 | Reasoning, memory, analysis. | params/core.md |
| Endurance | — | 1–7 | Physical resilience. Determines Health and Stamina base. | params/core.md |
| Presence | — | 1–7 | Social force and rhetorical gravity. Base for Debate pool. | params/core.md |
| Spirit | — | 1–7 | Internal coherence, resolve, Thread operation capacity. | params/core.md |
| Strength | — | 1–7 | Raw physical power. Weapon minimum requirement. | params/core.md |

### 1.2 Derived Character Stats
| Term | Abbr | Formula / Range | Definition | Source |
|------|------|-----------------|------------|--------|
| Health | (HP) | = Endurance | Wound track. Resets per wound. *HP not standalone.* | glossary §1 |
| Vitality | — | (PP-694) | Replaces Health terminology in combat_v30 ED-548/694. | combat_v30 §7 |
| Stamina | — | Endurance + History + 1 (armour-modified) | Combat resource. Degrades per round. | combat_v30 §7 |
| Coherence | — | 10→0 | Personal rendering stability for Thread practitioners. *What's broken* in a fractured practitioner. | threadwork §3 |
| Intelligibility | — | 10→0 | How legibly reality presents to a fractured practitioner. *What they perceive of the breakage.* | threadwork §3, fieldwork §1 |
| Composure | (COMP) | varies | Social endurance track. Rattled at ≤2; concession forced at 0. | contest §6 |
| Concentration | — | varies | Action-economy resource for sustained rhetorical positions. | contest, derived_stats §5.2 |
| Focus | — | 1–5+ | Contact duration in Thread operation rounds. | threadwork §2.3 |
| Truth | — | 0–5 | Per-character metaphysical stance (renamed from Certainty + consolidates the retired character "Piety Track"/religious-standing meter, ED-IN-0075). Solmund orthodoxy (5, Himmelenger pole) → Thread-truth acceptance (0, Edeyja pole). Engine-internal; players see qualitative bands. PCs only; named NPCs at GM discretion. Legacy abbr `CERT` retired. | conviction_track, glossary §1 |
| Momentum | — | 0–4 | Tactical resource. Earned on Overwhelming success or Belief achieved; spent for automatic successes (non-Thread only). | combat_v30 §1 |
| Thread Fatigue | — | resource | Replaces Contact Rounds (ED-694). | threadwork §2.3 |
| Bonds | — | 1–7 | Structural relationship capacity. Caps Disposition Track (PP-684). Companion formation requires Bonds ≥ 5. | derived_stats §10.1, params/core |
| Renown | — | 0+ | Player-governance-linked reputation track. Governance failures apply Renown penalties (cap −2/season). | derived_stats §10.3 |

### 1.3 Thread Practitioner Stats
| Term | Abbr | Range | Definition | Source |
|------|------|-------|------------|--------|
| Thread Sensitivity | TS | 0–100+ | Perception depth and operation eligibility. Determines accessible operation scale. | threadwork |
| Thread Pool Score | TPS | TS ÷ 10 (round down) | Bonus dice added to Thread operation pools. | threadwork |
| Thread Tension | TT | 0–100+ | Accumulated stress from Thread activity. **Inverse direction from Mending Stability on the same axis.** | threadwork §5 |
| Thread Depth | (TD) | REMOVED PP-166 | Phantom stat; not tracked. *Do not use.* | alias_registry |

### 1.4 Personal-scale narrative properties
| Term | Abbr | Definition | Source |
|------|------|------------|--------|
| Belief | — | Player-authored character conviction. Drives Momentum and Character Points. | glossary §7 |
| Inspiration | — | Named focus that grants bonus dice in relevant scenes. **Distinct from Belief and History per ED-779.** | glossary §7 |
| History | — | Skill-equivalent. Specific experiential knowledge granting bonus dice. Cap = Memory score. | glossary §7 |
| Character Point | CP | Advancement currency from Beliefs and session milestones. **CP = Character Points only [ED-136].** | glossary §7 |
| Knot | — | Significant relationship bond. Variants: Close · Regular · Distant. Lifecycle per ED-773. | glossary §7 |
| Bond / Bonded NPC | — | Tracked relationship in articulation layer; lower threshold than Knot. | articulation §2.3 |
| Recall | — | Cap on History entries. *Renamed from "Memory (score)" to disambiguate from debate genre "Memory" and per-NPC "Memory entry."* | glossary §7 |
| Memory entry | — | Per-NPC: Key reference + salience. (Renamed from "Memory record" per PP-687.) | key_substrate §4.3 |
| Conviction Scar | — | Belief-revision marker from social contest outcomes. | contest §6.2 |
| Self-Other orientation | — | Scalar [-1, +1]. **Separate axis from Convictions.** Captures whom an actor primarily benefits. | conviction_taxonomy §3 |
| Personal Convictions | — | NPC's vector across the 13-Conviction set. | conviction_taxonomy §1 |
| Effective Convictions | — | Personal + faction Cascade math (PP-686 §3.2). | faction_behavior §3.2 |
| ~~Cover (derived)~~ | — | ~~Concealment level vs detection.~~ *Moved to §8 Fieldwork — Cover is a fieldwork mechanic output, not a character attribute.* | fieldwork §6.1 |
| Disposition | — | NPC-attached attitude state toward another entity. Drives behaviour-tree branching. **Belongs in attribute silo when describing the NPC's state, but the Disposition Track also operates as a fieldwork mechanic — see §1.H.** | npc_behavior, fieldwork §5.1 |

### 1.5 The 13 Convictions (granular enumeration — PP-684 taxonomy)
Each is an attribute-vector value held by an actor. Period-grounded.

| # | Conviction | Definition | Period root |
|---|------------|------------|-------------|
| 1 | Faith | Devotion to ecclesiastical authority and theological order. | *fides, pietas* |
| 2 | Authority | Deference to and assertion of legitimate command. | *auctoritas, imperium* |
| 3 | Order | Procedural correctness; rule-following; institutional regularity. | *ordo* |
| 4 | Scholastic | Reasoned inquiry; learning; scholarly method. | *studium*, scholastic tradition |
| 5 | Utility | Effectiveness; results; instrumental judgment. | *utilitas, ragion di stato* |
| 6 | Equity | Fairness across station; relief of injustice. | *aequitas* |
| 7 | Liberty | Self-determination; freedom from imposed authority. | *libertas* |
| 8 | Precedent | Reverence for ancestral practice; *what has been done.* | customary law, *consuetudo* |
| 9 | Community | Belonging to immediate community; common life. | *communitas* |
| 10 | Identity | Membership in categorical group; tribe, lineage, faction. | *gens*, lineage-honor |
| 11 | Warden | Stewardship of dependent and vulnerable. | *cura* |
| 12 | Virtue | Cultivation of moral character. | Aristotelian *virtus* |
| 13 | Honor | Pledged oath; honor-code; reputation as binding. | chivalric, military code |

### 1.6 Conviction axis-space (4 axes × 13 Convictions)
| Axis | Positive pole | Negative pole |
|------|---------------|---------------|
| hierarchical | rank-bearing, status-asserting, deferential to position | egalitarian, status-effacing |
| sacred | numinous, ritually charged, oath-binding | secular, instrumental |
| instrumental | end-justifies-means, calculative, transactional | principled, deontological |
| traditional | precedent-respecting, conservative, ancestral | progressive, reformist |

> Class B 5th axis (communal-vs-categorical) deferred unless calibration requires.

### 1.7 Legacy / superseded character labels (DO NOT USE)
| Old label | Replaced by | Source |
|-----------|-------------|--------|
| Categorical Imperative | 13-Conviction taxonomy | PP-684 |
| Virtue | 13-Conviction taxonomy | PP-684 |
| Faith | 13-Conviction taxonomy | PP-684 |
| Scholastic | 13-Conviction taxonomy | PP-684 |
| Equity | 13-Conviction taxonomy | PP-684 |
| Honor | "Honor" (Conviction #13) | PP-684 |
| Reason (legacy tag) | replaced in PP-684 | PP-684 |
| Continuity (legacy tag) | replaced in PP-684 | PP-684 |

---
## SILO 2 — FACTION ATTRIBUTES (entity properties — what a faction *is*)

> **Word-class rule:** these are nouns naming what the faction possesses. They MUST NOT collide with mechanic verbs or process nouns. Note: **Mandate, Influence, Wealth, Military, Intel, Stability** all use English words also used colloquially as mechanics — collisions audited in §X-overlap.

### 2.1 Faction Core Stats (1–7 scale; Standing 0–10)
| Term | Abbr (table-only) | Range | Definition | Collapse | Source |
|------|-------------------|-------|------------|----------|--------|
| Mandate | M | 1–7 | Institutional authority and political legitimacy. | 0 = Collapse state | factions/stats_1_7_scale |
| Influence | I | 1–7 | Social and cultural reach. | Cannot drop below 1 | factions/stats_1_7_scale |
| Wealth | W | 1–7 | Economic capacity. | 0 = cannot Trade or fund Wealth-requiring actions | factions/stats_1_7_scale |
| Military | Mil | 1–7 | Military power; ceiling for unit quality. | 0 = cannot Muster | factions/stats_1_7_scale |
| Intel | Int | 1–7 | Intelligence capacity. | — | factions/stats_1_7_scale |
| Stability | Sta | 1–7 | Internal coherence. | 0 = Collapse trigger (P-15) | faction_layer §1 |
| Standing | — | 0–10 | Reputation track. **Exception to 1–7 scale.** No in-game benefit above 7; 10 is cosmetic max. | — | factions |

> Single-letter abbreviations permitted only in table headers following a full-term legend. Never alone in prose.

### 2.2 Derived faction values
| Term | Definition | Source |
|------|------------|--------|
| Political Pool | Pool used in parliamentary + negotiation contexts. *"Faction Pool" and "Mandate Pool" are deprecated aliases.* | ci_political §3.4 |
| CI Bonus Dice | Bonus to Church faction in political forums per CI threshold. | ci_political §3.2 |
| CI Obstacle Modifier | +1 Ob to actions opposing Church Domain Actions at CI ≥ 55. | ci_political §3.3 |
| Spiritual Weight (territory-attached, faction-relevant) | Repurposed from old PV; affects CI generation. | ci_political §1 |
| Popular Support (PS) | Per-**settlement** (not faction-level) outcome accumulator, 0-7, aggregated into faction Mandate (LPS-2e, Jordan 2026-05-30). **Corrected 2026-07-08 (ED-IN-0029 docket, OPT-AV-7)**: this row carried both the deprecated name "Public Support" and the superseded pre-LPS-2e faction-level-accumulator model — the real untracked residual the audit found (`name_collision_database.yaml`'s tracked citation pointed at a since-changed settlement_layer_v30.md line that no longer has the issue). | `settlement_layer_v30.md §1.8` |
| Legitimacy (L) | Per-settlement (0-7) faction trust currency, tracked alongside PS; aggregated into Mandate. | `settlement_layer_v30.md §1.8` |
| Income / Drain | Per-season resource flow (Wealth/Mandate/Influence/Military). | derived_stats §8.1 |
| Cascade resolution | Faction-Conviction cascade math; produces Effective Convictions. | faction_behavior §3.2 |
| Mission | Stated faction objective; alignment with Conviction profile. | faction_behavior §3.1 |
| Mission alignment | Conviction-profile fit between Mission and faction's effective Convictions. | faction_behavior §3.3 |
| Public Expectation | Populace's expected behaviour; gates outcome attribution. | faction_behavior §3.5 |
| Per-faction temperament | α (outcomes weight) + β (conduct weight); aggregated across territories. | territory_temperaments §3 |
| Faction-specific Negotiation Bonus | +X dice in negotiations of specified type. | faction_layer §4.1 |
| Casus Belli | Faction's triggering grievance for war declaration. | faction_layer §3.5 |

### 2.3 The seven player-facing factions (granular enumeration)
| Faction | Identity / role | Source |
|---------|----------------|--------|
| Crown | Royal political authority; capital at Valorsplatz (T1). Virtue-ethics framework (legacy). | victory §3.1 |
| Church of Solmund | Theocratic political-religious institution; cathedral at Himmelenger (T9). | victory §3.2 |
| Hafenmark | Constitutional/legalist faction; Gransol seat (T8). Categorical Imperative framework (legacy). | victory §3.3 |
| Varfell | Military-conqueror faction; Sigurdshelm seat (T12). Utility-driven framework (legacy); Reinhardt von Lohengramm parallel. | victory §3.4 |
| Restoration Movement (RM) | Cultural-revolution latent faction. Emerges from Varfell-RM relationship track. | victory §3.5 |
| Löwenritter | Conditional military regency faction; post-coup activation. Lions' Table seat. | victory §3.6 |
| Guilds | Mercantile / moral-relativist faction. Annika Feldhaus rep. | valoria_complete §1.3 |

> Niflhel **struck** as a player faction per CR-STRIKE-2026-04-19 (conflict_architecture). Toolkits redistributed to settlement-broker mechanics.

### 2.4 Subnational / role-bearing entities (faction-adjacent)
| Term | Definition | Source |
|------|------------|--------|
| Subnational faction | Faction operating at sub-territory (settlement) level. | settlement_layer §3.3 |
| Governor (assigned) | Settlement-level faction-appointed authority. | settlement_layer §3.2 |
| Local actor | Settlement-resident NPC with throughline weight. | settlement_layer §4.5 |
| Knights Templar | Church-only military order; conditional unit. | military_layer §1.8 |
| Faction Acquisition Toolkit | Faction-specific kit defining how it gains/loses territory. | victory §0.5 |
| Cardinal | Senior Church official. Four-Cardinal Structure (Prudence, Justice, Gifts, Temperance). | npc_roster |
| Tribune (Varfell) | Intel-revealing role. | victory §3.4 |
| Riskbreakers | Specialized identity-class; identity spec authored separately. | factions/riskbreakers_identity |

### 2.5 Faction internal-state mechanics
| Term | Definition | Source |
|------|------------|--------|
| Faction Collapse Exit Procedure | ED-675 process for dissolving a faction at Stability 0. | faction_layer §1.5 |
| Five Stability Triggers | (1) Territorial Occupation/Loss · (2) Unfavourable Treaty Terms · (3) Antagonistic Parliamentary Vote · (4) Major Subterfuge · (5) Failed Military Engagement: Significant Losses. | faction_layer §1.2 |
| Stability Recovery | Procedure for regaining Stability points. | faction_layer §1.3 |
| Accounting Stability Check | Per-season Stability check at Accounting phase. | faction_layer §1.4 |
| Faction-Specific Priorities | AI posture priority schemas per faction. | ci_political §6.2 |
| Posture Priority Framework | Generic AI posture mechanic. | ci_political §6.1 |
| Succession (faction) | Leadership-change procedure. Modes: routine · contested · emergency · imposed. | settlement_layer §7.2, faction_succession_split |
| Coup (attempted) | State transition Key type. | key_type_registry §5 |
| Demotion magnitude | Officer-level demotion sizing rule. | (referenced) |

### 2.6 Per-territory temperament values held BY a faction (aggregate)
| Temperament | α (outcomes) | β (conduct) | Period example |
|-------------|--------------|-------------|----------------|
| pragmatic | 0.7 | 0.3 | Florentine merchant class |
| traditional | 0.3 | 0.7 | Rural devout populace |
| balanced | 0.5 | 0.5 | Mixed urban populace |
| principled | 0.2 | 0.8 | Reformist enclaves |
| outcomes-only | 0.9 | 0.1 | Hardship populations under direct threat |

---
## SILO 3 — TERRITORY ATTRIBUTES (entity properties — what a territory *is*)

> **Word-class rule:** territory-property nouns. T-numbers (T1–T17) are IDs, not mechanics; they appear cross-silo only as references.

### 3.1 Territory state values
| Term | Abbr | Range | Definition | Source |
|------|------|-------|------------|--------|
| Provincial Value | PV | per-territory | Strategic worth toward Peninsular Sovereignty. | victory §1 |
| Piety Track (per-territory) | PT | 0–5 | Per-territory Solmund-orthodoxy track. 0 = Restoration pole, 5 = Piety pole. **PT ≡ Conviction Track per-territory per ED-644. Range is 0–5, NOT 0–10. See conviction_track_v30 §1.** | victory §2, conviction_track_v30 §1 |
| ~~Conviction Track (per-territory)~~ | ~~CV~~ | ~~0–10~~ | **MERGED — same track as Piety Track (PT) per ED-644 in conviction_track_v30. Abbreviation is PT, range is 0–5. "CV" and "0–10" were diagnostic errors in this index. Canonical name is Piety Track (PT).** | conviction_track_v30 §1 |
| Spiritual Weight (territory-attached) | — | per-territory | Repurposed PV for CI generation. | ci_political §1 |
| Temperament (per-territory) | — | 5-typology | One of: pragmatic · traditional · balanced · principled · outcomes-only. | territory_temperaments §2 |
| Accord (per-territory) | — | population commitment | Population alignment with controlling faction's project. | military_layer §4.1, peninsular_strain |
| Prosperity | — | gate | Economic state gating unit-quality availability. | military_layer §4.2 |
| Consecrated Status | — | binary state | Church-blessed territory state (PP-410). | conviction_track_v30 §1.4 |

### 3.2 The 17 provinces (granular enumeration)
| ID | Name | Faction | Region | Temperament | α/β | Notes |
|----|------|---------|--------|-------------|-----|-------|
| T1 | Valorsplatz | Crown | Eastern Lowlands / Capital | pragmatic | 0.7 / 0.3 | Crown capital + river-sea trade nexus |
| T2 | Kronmark | Crown | Eastern Lowlands / Heartland | traditional | 0.3 / 0.7 | Italian-coded farmland heartland |
| T3 | Lowenskyst | Crown | Northern Mountains / Border Fortress | balanced | 0.5 / 0.5 | NE Altonian-pass garrison |
| T4 | Grauwald | Varfell | Central Highlands / Highland Timber | traditional | 0.3 / 0.7 | Einhir heritage + highland tradition |
| T5 | Feldmark | Crown | Eastern Lowlands / Breadbasket | traditional | 0.3 / 0.7 | Crown breadbasket; agrarian populace |
| T6 | Stillhelm | Crown | Southern Approaches / S. Farmland | outcomes-only | 0.9 / 0.1 | Calamity-adjacent (southern Crown gate) |
| T7 | Rendstad | Hafenmark | Hafenmark Highlands / Timber Valley | traditional | 0.3 / 0.7 | Remote forested valley |
| T8 | Gransol | Hafenmark | Hafenmark Highlands / Constitutional Capital | pragmatic | 0.7 / 0.3 | Hafenmark constitutional seat |
| T9 | Himmelenger | Church | Mountain Ridge / Cathedral City | principled | 0.2 / 0.8 | Church seat / cathedral city |
| T10 | Spartfell | Hafenmark | Northern Mountains / Border Castle | balanced | 0.5 / 0.5 | NW Altonian-pass garrison |
| T11 | Halvardshelm | Varfell | Central Fjords | traditional | 0.3 / 0.7 | Fjord communities + Spartfell border |
| T12 | Sigurdshelm | Varfell | Western Fjords / Varfell Seat | balanced | 0.5 / 0.5 | Vaynard's court (urban administrative) |
| T13 | Oastad | Varfell | Southern Fjords | outcomes-only | 0.9 / 0.1 | Calamity-adjacent (Varfell southern gate to Askeheim) |
| T14 | Ehrenfeld | Crown | Central Plains / Military Hinge | balanced | 0.5 / 0.5 | Crown military hinge + Löwenritter HQ |
| T15 | Askeheim | Uncontrolled | Southernmost / Calamity Epicenter | outcomes-only | 0.9 / 0.1 | Calamity epicenter / frontier |
| T16 | Schoenland | Schoenland | Eastern Sea / Island Republic | pragmatic | 0.7 / 0.3 | Independent island republic |
| T17 | Halvarshelm | Hafenmark | Northern Mountains / Northern Mines | balanced | 0.5 / 0.5 | Iron/copper mining + Guilds |

### 3.3 Sub-territory level
| Term | Definition | Source |
|------|------------|--------|
| Settlement | Sub-territory governance node. **36 total** — see settlement_layer §2.1 registry. | settlement_layer §1, §2 |
| Settlement Type | Categorical typology of settlements (capacity tier). | settlement_layer §1.2 |
| Two-Tier Map | Province (T-level) ↔ Settlement (sub-T) cartography. | settlement_layer §1.1 |
| Settlement Stats | Per-settlement state (population, allegiance, infrastructure tier, etc.). | settlement_layer §1.3 |
| Institutional Facility Tiers | Capacity tiers for settlement-hosted institutions. | settlement_layer §1.4 |
| Facility Slot Capacity | Number of institutions a settlement can host per type. | settlement_layer §1.4.1 |
| Cross-Faction Wing Allocation | Multi-faction occupancy of a settlement's institution slots. | settlement_layer §1.4.4 |
| Capacity Pressure | Political mechanic from over-allocation. | settlement_layer §1.4.3 |
| Parish Social Services | Church-level settlement-resident services (historical_precedents §1.4). | settlement_layer §1.6 |
| Pastoral Assumption | Default ecclesiastical role of parish populace. | settlement_layer §1.7 |
| Settlement Registry | The 36-settlement enumeration (§2.1). | settlement_layer §2.1 |
| Two-Tier Authority Model | Faction-level + settlement-level dual governance. | settlement_layer §3.1 |
| Governor Assignment | Settlement governorship procedure. | settlement_layer §3.2 |
| Subnational Faction Visibility | UI/info layer surfacing local factions. | settlement_layer §4.2 |
| Settlement Events | Per-settlement scenario triggers. | settlement_layer §4.3 |
| Settlement POI Templates | Reusable settlement scene templates (Throughline T3). | settlement_layer §4.6 |
| Garrison | Defensive unit allocation per settlement. | settlement_layer §5.2 |
| Stature Ladder | Player progression scale (settlement → national). | settlement_layer §6.1 |

### 3.4 Geographic / regional groupings
| Term | Definition |
|------|------------|
| Eastern Lowlands | T1, T2, T5 |
| Northern Mountains | T3, T10, T17 |
| Hafenmark Highlands | T7, T8 |
| Central Highlands | T4 |
| Central Plains | T14 |
| Mountain Ridge | T9 |
| Central Fjords | T11 |
| Western Fjords | T12 |
| Southern Fjords | T13 |
| Southern Approaches | T6 |
| Southernmost | T15 (Askeheim) |
| Eastern Sea | T16 (Schoenland) |
| Einhir territories | Pre-colonial indigenous-culture geography (Southernmost). |
| March (layer) | Frontier territorial classification. | march_layer_v30 |

### 3.5 Cross-territory mechanical states
| Term | Definition | Source |
|------|------------|--------|
| Locked Zone | Territory under Forced Resolution Lock. | threadwork |
| Occupied territory | Faction holding a non-home territory by force. | faction_layer §2 |
| Fractional ownership | Multi-faction shared territorial control. | fractional_province_ownership_v30 |
| Adjacency | Inter-territory contact relation; underpins movement and combat range. | settlement_adjacency_v30 |
| Population (per-territory) | Demographic input for temperament weighting + Accord. | valoria_geography (referenced) |

---
## SILO 4 — WORLD / COSMOLOGICAL STATE (what the world *carries*)

> **Word-class rule:** these are world-state values and substrate-level concepts. They include shared world clocks (which also belong to the strategic/clocks silo) and pure-cosmology terms with no strategic-clock counterpart.

### 4.1 Shared world clocks (also enumerated in §K-Clocks)
| Term | Abbr | Range | Mode | Definition | Source |
|------|------|-------|------|------------|--------|
| Mending Stability | MS | 100→0 | ALL | World coherence track. Renamed from Rendering Stability per ED-731. **0 = The Rupture (campaign ends).** | threadwork §5, glossary §2 |
| Thread Tension | TT | 0–100+ | ALL | Faction/world-scale stress accumulator. **TT and MS run on opposite directions of the same world-state axis.** | threadwork |

### 4.2 Cosmological substrate (Foundations Amendments 1–4)
| Term | Definition | Source |
|------|------------|--------|
| Three-layer being-persistence | Foundational structure: (1) substrate, (2) rendered, (3) actor. | canon/01 Amendment 1 |
| Substrate | Underlying ontological layer. | canon/01 |
| Rendered (layer) | Actor-perceived rendition of substrate. | canon/01 |
| Actor (layer) | Conscious entity performing rendering. | canon/01 |
| Always-Already Self-Rendering | Foundational principle: rendering is performed by the actor's consciousness; no external GM. | canon/01 |
| Leap (the) | Entering Thread contact via rendering-suspension. Operations performed during suspension. | canon/02 Amendment 1 |
| Rendering Suspension | The Leap's structural target. | canon/02 |
| Knot Formation (during Leap) | Formation of relational lock during contact. | canon/02 Amendment 2 |
| Operation-Type Risk Taxonomy (3 layers) | Restorative · Manipulative · Destructive. Knot-profile-tag-bearing. | canon/02 Amendment 3 |
| Restorative operations | Operation-type class. | canon/02 |
| Manipulative operations | Operation-type class. | canon/02 |
| Destructive operations | Operation-type class. | canon/02 |
| Knot-Profile Tag | Mechanical marker on Knot recording op-type history. | canon/02 Amendment 6 |
| Coherence (cosmological) | What's broken in a fractured practitioner. *See §1.2 for stat form.* | canon/01 Amendment 3 |
| Coherence 0 outcomes | TS-gated outcomes when Coherence reaches 0 (4 bands — see §4.3). | canon/01 Amendment 4 |
| Einhir Catastrophe | Inversion of a Manipulative operation. | canon/02 Amendment 4 |
| Threadcut Beings | Beings cut from Thread substrate; observer-dependent rendering. | threadwork §6 |
| De-Actualisation | Mechanical class of substrate breakage. | threadwork §6.4 |
| Observer-Dependent Rendering | Rendering varies by observer's TS. | threadwork §6.2 |
| Observable Coherence Degradation | Public-facing signs of declining Coherence. | canon/01 Amendment 3 |

### 4.3 TS-gated Coherence-0 outcome bands
| TS band | Name | Outcome class |
|---------|------|---------------|
| 30–49 | Stirring | Ontological Freefall |
| 50–69 | Attuned | Relational Persistence |
| 70–89 | Sensitive | Structural Reconstitution |
| 90–100 | Resonant | Full Reconstitution and Reality Strain |

### 4.4 Substrate breakages and world-events
| Term | Definition | Source |
|------|------------|--------|
| Gap | Rupture in the rendered substrate. Severity tiers: Micro-Gap · Standard Gap · Entrenched Gap · Catastrophic Gap. | threadwork |
| Shifting Object | Pre-Gap substrate instability. Less severe than Gap; addressable by Mending. | threadwork |
| Locked Zone | Forced-Resolution-Locked territory or object. *See §1.G Threadwork mechanics for Lock op.* | threadwork |
| Monstrous Incursion | Entity manifestation triggered by low MS or severe Dissolution failure. | threadwork |
| The Rupture | Campaign-ending event when MS = 0. | threadwork |
| The Rupture Scene | Hybrid/TTRPG cinematic moment at MS=0 (ED-630). | victory §5.1 |
| Calamity (the) | World-scale rendering-side mechanism. | foundations canon |
| Calamity Drift | MS-linked PT erosion (PP-409). | conviction_track_v30 §1.3 |
| Calamity Radiation | Cross-territory effect of Calamity proximity (designs/world). | calamity_radiation (legacy doc) |

### 4.5 Solmund world-cosmology terms
| Term | Definition | Source |
|------|------------|--------|
| Solmund (the entity) | Cosmological figure. | solmund_v30 |
| Solmund (dissolution site) | Specific contested off-map location. | solmund_v30, ms_trajectory |
| Solmund Voice | Solmund's narrative-voice presence. | solmund_voice_v30 |
| Solmund Philosophy | Solmund's doctrinal/ethical position. | solmund_philosophy_v30 |
| Solmund Artifacts | Material objects of Solmund-cosmological significance. | solmund_artifacts_v30 |
| Miraculous Event | Cosmologically-charged rare event class. | miraculous_event_v30 |
| Baralta (the entity) | Cosmological/historical figure (extracted from miraculous_event §21). | baralta_v30 |
| Solmund Orthodoxy | Highest Truth value (5). World-religious orthodoxy. | conviction_track |
| Thread acceptance | Lowest Truth value (0). Worldview accepting Thread substrate. | conviction_track |

### 4.6 Peninsular-scale world state
| Term | Abbr | Definition | Source |
|------|------|------------|--------|
| Turmoil | — | Cross-cutting world-scale pressure system; T-07 throughline; Mode A hub. | peninsular_strain_v30 |
| Turmoil Counter | — | Strategic-layer counter for PS. | victory §0.3 |
| Peninsular Sovereignty | — | Universal victory condition. *See §N-Victory.* | victory §0 |
| MS Trajectory | — | Peninsula-wide MS values at specific historical dates (D-1, etc.). | ms_trajectory_v1 |
| Post-Calamity Era | — | World-state transition triggered at RS=0 (legacy term; now MS=0). | victory §5.1 |
| Phased Occupation Era | — | World-state transition at IP=100. | victory §5.2 |
| Anarchy Era | — | World-state transition: all factions dissolved. | victory §5.3 |

### 4.7 Substrate and Key vocabulary (universal substrate, PP-687)
| Term | Definition | Source |
|------|------------|--------|
| Key (substrate primitive) | Universal event-record. Replaces "EventImpact". | key_substrate §1 |
| Key Type | Subtype within a Key family. **37 total**, 7 families. | key_type_registry §9 |
| Causal Graph | Substrate-level provenance graph of Keys. | key_substrate §5 |
| Provenance | Per-Key causal-chain attribution. | key_substrate §5 |
| Salience (per-NPC) | NPC-perceived weight of a Key reference in memory. | key_substrate §4.5 |
| Memory Query API | Substrate API for per-NPC memory queries. | key_substrate §4.4 |
| Cycle detection | Substrate guarantee against causal loops. | key_substrate §4.6 |
| Replay determinism | Reproducibility guarantee. | key_substrate §6 |
| Lifecycle states (of Key) | Substrate Key-lifecycle classification. | key_substrate §4.8 |
| Visibility (Key) | Observer set for a Key emission. | key_substrate §4.2 |
| Sub-step ordering tiebreak | Determinism rule for simultaneous emissions. | key_substrate §4.7 |
| RNG seeding (per Key emission) | Determinism via per-Key RNG. | key_substrate §6.1 |

### 4.8 The 37 Key Types (granular enumeration — 7 families)
| Family | Subtype | Purpose |
|--------|---------|---------|
| scene_event | scene.dialogue | Spoken exchange recorded. |
| scene_event | scene.witness | Observation recorded. |
| scene_event | scene.gift | Object transfer recorded. |
| scene_event | scene.insult | Verbal hostility recorded. |
| scene_event | scene.threat | Coercive intent recorded. |
| scene_event | scene.interaction | (Class B, PP-687 Phase B Stage 1.) |
| scene_event | scene.gossip | (Class B, PP-687 Phase B Stage 1.) |
| da_outcome | da.public_governance | Open governance outcome. |
| da_outcome | da.covert_betrayal | Hidden hostile action outcome. |
| da_outcome | da.diplomatic_alliance | Pact outcome. |
| da_outcome | da.antinomian_action | Norm-breaking action outcome. |
| da_outcome | da.economic_intervention | Trade/economic outcome. |
| mechanical_event | mechanical.season_change | Season boundary tick. |
| mechanical_event | mechanical.accounting | Accounting-phase event. |
| mechanical_event | mechanical.cascade_resolution | Faction-Conviction cascade tick. |
| mechanical_event | mechanical.mission_shift | Faction Mission change. |
| mechanical_event | mechanical.scene_entered | Class B (Phase 5a session 3.5 telemetry). |
| mechanical_event | mechanical.scene_exited | Class B (Phase 5a session 3.5 telemetry). |
| mechanical_event | mechanical.scene_skipped | Class B (Phase 5a session 3.5 telemetry). |
| state_transition | state.scar_acquired | Conviction Scar acquired by NPC. |
| state_transition | state.standing_change | Standing track change. |
| state_transition | state.coup_attempted | Coup attempt registered. |
| state_transition | state.succession | Leadership succession. |
| state_transition | state.opinion_revised | Class B (PP-687 Phase B Stage 1). |
| state_transition | state.concern_resolved | Class B (PP-687 Phase B Stage 1). |
| state_transition | state.belief_revised | Class B (PP-688). |
| environmental | env.peninsular_strain_shock | PS pressure tick. |
| environmental | env.crisis | World-state crisis trigger. |
| environmental | env.disaster | Catastrophic world event. |
| environmental | env.population_change | Demographic shift. |
| scene_outcome | scene.contest_resolved | Social contest result. |
| scene_outcome | scene.battle_concluded | Battle result. |
| scene_outcome | scene.investigation_resolved | Investigation result. |
| system_meta | meta.knot_formed | New Knot tier (Class B per PP-687 §8). |
| system_meta | meta.knot_ruptured | Knot rupture (Class B, PP-688). |
| system_meta | meta.thread_woven | Weaving operation completion. |
| system_meta | meta.miraculous_event | Solmund-cosmological event tag. |
| system_meta | meta.legacy_event | Persistent legacy marker. |

### 4.9 Pre-colonial / cultural-layer
| Term | Definition |
|------|------------|
| Einhir | Pre-colonial indigenous culture of the Southernmost. |
| Valn | Pre-Altonian, ambiguous, possibly pre-Einhir entity (ED-728). |
| Altonia / Altonian Empire | Foreign empire to the east; invasion-pressure source. |
| Altonian Vanguard | Invasion event (IP 75/80 BG). |

---
## SILO 5 — PERSONAL RESOLUTION: COMBAT (combat-system mechanics)

> **Word-class rule:** mechanic verbs and process nouns specific to personal combat. MUST NOT collide with character-attribute words (Strength, Endurance) or faction-attribute words (Military, Mandate). Note: **Combat replaces Strength→Size and Combat Power→Power for unit-level vocabulary** to preserve attribute-vs-mechanic separation.

### 5.1 Pool / round / initiative
| Term | Definition | Source |
|------|------------|--------|
| Combat Pool | Dice pool for combat actions. | combat_v30 §1 |
| Round Structure | Turn ordering within a combat round. | combat_v30 §2 |
| Initiative | Round-start ordering rule (PP-232). | combat_v30 §3 |
| Three-Mode Framing | TTRPG / BG / Hybrid applicability frame. | combat_v30 |

### 5.2 Actions (combat verbs — granular)
| Action | Definition | Source |
|--------|------------|--------|
| Attack | Standard offensive action. | combat_v30 §4 |
| Defend | Standard defensive action. | combat_v30 §4 |
| Dodge | Movement-based defensive action. | combat_v30 §4 |
| Feint | Misleading offensive (Degree-table-resolved). | combat_v30 §4 |
| Disarm | Weapon-removal offensive (Degree-table-resolved). | combat_v30 §4 |
| Tie Up | Engagement-locking action. | combat_v30 §4 |
| Critical Hit | Special damage outcome. | combat_v30 §4 |
| Anti-Armour | DR-bypassing offensive class. | combat_v30 §4 |
| Rescue | Allied-extraction action. | combat_v30 §8 |

### 5.3 Weapon system
| Term | Definition | Source |
|------|------------|--------|
| Weapon TN Matrix | Per-weapon-class Target Number table. | combat_v30 §5 |
| Ranged Weapons | Distinct weapon category (ED-129). | combat_v30 §5 |
| Damage Resolution | PP-232 damage calculation procedure. | combat_v30 §5 |
| Reach Rules | Weapon-reach-band restrictions on engagement. | combat_v30 §5 |
| Environmental Factors (Ranged) | Environmental modifiers to ranged attacks. | combat_v30 §5 |
| Armour | Damage-mitigation gear (PP-232). | combat_v30 §6 |
| Damage Resistance | DR (also a faction-stat-adjacent value in mass combat). | combat_v30 §6 |
| Ranged DR | DR specific to ranged attacks. | combat_v30 §6 |

### 5.4 Wound / vitality / stamina
| Term | Definition | Source |
|------|------------|--------|
| Wound | Health/Vitality damage entry (ED-548, ED-694: Vitality replaces Health). | combat_v30 §7 |
| Wound Penalty | Pool penalty from accumulated Wounds (PP-232). | combat_v30 §7 |
| Vitality | Survival resource. (ED-694 — replaces Health term in combat_v30.) | derived_stats §4.1 |
| Stamina (combat use) | Action-economy resource per round. | combat_v30 §7, derived_stats §4.2 |
| Combat Endurance | CE — Stamina-resource sub-application in extended combat. | glossary §5 |

### 5.5 Group / mass-adjacent combat (TTRPG scale)
| Term | Definition | Source |
|------|------------|--------|
| Zone Collapse | Multi-engagement compression rule. | combat_v30 §8 |
| Fibonacci Group Bonus | Pool-bonus formula for group combatants. | combat_v30 §8 |
| Multi-Engagement | 3v2, 4v3, etc., engagement rules. | combat_v30 §8 |
| Mass Combat (TTRPG scale) | Smaller mass-action subset of full mass battle (§J). | combat_v30 §9 |
| Unit Stat Block (1–7) | TTRPG-scale unit stats. | combat_v30 §9 |
| Base Damage Formula (mass) | PP-086 mass-combat formula. | combat_v30 §9 |
| Formation Break Ob Stacking | PP-087 obstacle-stacking rule. | combat_v30 §9 |
| Siege Assault Linkage | PP-088 — connects siege actions to mass combat. | combat_v30 §9 |
| Artillery Bombard | PP-091 long-range bombardment. | combat_v30 §9 |
| Hybrid Phase Order | PP-089/090 phase-ordering for Hybrid mode. | combat_v30 §9 |
| Mode-Switch | Mid-combat mode transition rule. | combat_v30 §9 |

### 5.6 Thread integration
| Term | Definition | Source |
|------|------------|--------|
| Practitioner Interface (combat) | How a Thread practitioner enters combat scene. | combat_v30 §10.1 |
| Thread Perception in Combat | Thread-aware sensing during combat. | combat_v30 §10.2 |
| Cross-System Fire (from combat) | Combat outputs that drive other systems. | combat_v30 §10.3 |

### 5.7 Faction unit rosters (combat side)
| Term | Definition | Source |
|------|------------|--------|
| Faction Unit Roster | Faction-specific unit-template list (MT-01). | combat_v30 §11 |

### 5.8 Combat → world bridges
| Term | Definition | Source |
|------|------------|--------|
| Fieldwork Transitions (combat→fieldwork) | Combat-end handoff into fieldwork. | combat_v30 §11.5 |
| Combat Domain Echo | Strategic-layer consequence of combat outcomes. | combat_v30 §13.1 |
| Combat Reputation Cascade | Standing-track effect from notable combats. | combat_v30 §13.2 |
| Economic Actions in Settlements (Throughline T2) | Combat-economic linkage at settlement scale. | combat_v30 §13.1b |
| Settlement-Level Combat Consequences | Settlement-state effect of combats fought there. | combat_v30 §13.2b |
| Death Cascade | Cascading consequences when a named character dies in combat. | combat_v30 §13.3 |

### 5.9 Combat-system Degree table (uses dice-engine Degree but combat-specific applications)
| Term | Definition |
|------|------------|
| Degree Table (combat) | Combat-specific outcome bands for actions like Feint, Disarm. |

> **Important:** Combat uses the universal Degree of Success (Overwhelming/Success/Partial/Failure — see §R Dice Engine). The combat-specific "Degree Table" maps degree to combat-specific outcomes; the underlying degree primitives belong to the dice engine.

---
## SILO 6 — PERSONAL RESOLUTION: SOCIAL CONTEST (DEBATE)

> **Word-class rule:** rhetoric / argumentation mechanics. Note collisions: **Composure** is a character-attribute (§1) AND the debate damage track. **Equity / Precedent / Order** are Conviction labels (§1.5) AND debate stylistic/argument-class labels — flagged as INTENTIONAL polysemy in §X-overlap.

### 6.1 Setup / pool / structure
| Term | Definition | Source |
|------|------------|--------|
| Contest (the system) | Canonical name. Candidates considered: Contest · Contention · Proceeding (ED-136). Debate score tracked on **Persuasion Track** (0–10, renamed from "Conviction Track"). | contest §1 |
| Argue Pool | Dice pool for contest exchanges. | contest §3 |
| Argue Pool Construction | Procedure for assembling the pool. | contest §3 |
| Exchange Structure | Per-round structure of an exchange. | contest §4 |
| First to Speak | Speaker-order rule per round. *Renamed from "Initiative (contest)" to disambiguate from combat Initiative.* | contest §5 |
| Pre-Contest Preparation | Off-table rhetorical preparation. | contest §9.1 |
| Format Follows Context | Core principle (§1). | contest §1 |
| GM Setup (Before Contest Begins) | Setup procedure (also Engine Setup in implementation). | contest §2 |

### 6.2 Genre / Orientation / Interaction
| Term | Values / Type | Source |
|------|---------------|--------|
| Genre | Past · Present · Future | contest §4 |
| Orientation | Revealing · Obscuring | contest §4 |
| Interaction Type | Determined by Genre + Orientation match between orators. | contest §4 |
| **CLASH** (interaction) | Same Genre, opposite Orientation. | contest §4 |
| **AMPLIFY** (interaction) | Same Genre, same Orientation. | contest §4 |
| **CROSS** (interaction) | Different Genre, opposite Orientation. | contest §4 |
| **DIVERGE** (interaction) | Different Genre, same Orientation. | contest §4 |

### 6.3 Damage tracks / resources
| Term | Definition | Source |
|------|------------|--------|
| Composure (debate) | Social endurance damage track. Rattled at ≤2; concession at 0. **Cross-listed with §1.2 character stat.** | contest §6, derived_stats §5.1 |
| Concentration | Action-economy resource for sustained positions. | contest, derived_stats §5.2 |
| Doubt Marker | Token applied on Obscuring loss in Diverge state. | contest §4 |

### 6.4 Argument types (the four Pressure Point types — granular)
| Type | Definition | Maps to Contest Style |
|------|------------|----------------------|
| **Evidence** | Facts contradicting belief. | Citation (Precedent + Revealing) |
| **Consequence** | Outcomes the framework fails to explain. | Vision (Prospect + Revealing) |
| **Sanction** | Recognized binding authority. *Renamed from "Authority" to disambiguate from Conviction #2 per §3.2 rename action.* | Suppression (Precedent + Obscuring) |
| **Solidarity** | Relational obligation. *Renamed from "Loyalty" per params/contest.md canonical source.* | Any + Revealing (requires active Knot) |

### 6.5 Post-contest mechanics
| Term | Definition | Source |
|------|------------|--------|
| Obligations | Post-contest binding commitments (NEW §6.1). | contest §6.1 |
| Conviction Scar | Belief revision marker (NEW §6.2). | contest §6.2 |
| Conviction Scar Visibility | Player-facing surfacing of Scars. | contest §6.2 |
| Chain Contest | Unresolved-tension follow-up contest. | contest §6.3 |
| Asymmetric Proceeding | Non-balanced contest variant (e.g., trial). | contest §7 |
| Excommunication Tribunal | Specific asymmetric proceeding (ED-625). | contest §7.1 |
| Parliamentary Stay | Specific asymmetric proceeding (ED-631). | contest §10.1 |
| Forced Unmask | Reveal-forcing post-contest mechanic. | contest §9.6 |
| Multi-Party Contest — Coalition Structure | 3+ party contest rules. | contest §9.2 |
| Niflhel Social Toolkit | Mechanic kit (Niflhel-as-faction struck; toolkit retained for any covert/hostile action). | contest §9.7, fieldwork §5.8 |

### 6.6 Thread integration in contests
| Term | Definition | Source |
|------|------------|--------|
| Practitioner Weaving in Contests (R-65) | Weaving operation usable mid-contest. | contest §9.3 |
| Thread Operations Between Exchanges | Thread ops permitted between exchange turns. | contest §9.4 |
| Adjudicator Thread Response (ED-667) | Adjudicator's reaction to mid-contest Thread. | contest §9.4b |
| Beliefs Integration | Belief-driven argument bonuses. | contest §9.5 |

### 6.7 BG variants
| Term | Definition | Source |
|------|------------|--------|
| BG Parliamentary Vote | Strategic-layer voting analogue of contest. | contest §10 |
| BG Vote Setup | Setup procedure. | contest §10 |
| BG Vote Resolution | Resolution procedure. | contest §10 |
| Hybrid Contest | Hybrid-mode bridge format. | contest §11 |
| Grand Debate | Hybrid/TTRPG faction-layer extended contest. | faction_layer §4.2 |

### 6.8 Bridges out (debate → world)
| Term | Definition | Source |
|------|------------|--------|
| Debate → Domain Echo (PP-108) | Decisive contest outcome triggers strategic-layer Domain Echo. | scale_transitions §5.4 |
| Domain Echo (debate-class) | Faction-level consequence triggered by decisive debate outcome. | glossary §7 |

---
## SILO 7 — PERSONAL RESOLUTION: THREADWORK

> **Word-class rule:** Threadwork is the metaphysical-mechanical layer. Operation verbs (Weave, Pull, Lock, Mend, Dissolve) are deliberately distinctive — chosen to NOT collide with combat/debate/fieldwork verbs. Note: **Coherence** is a personal stat (§1) AND a cosmological term (§4). **Mending Stability** is a world clock (§4, §L) used by this system. Both intentional.

### 7.1 Operation prerequisites
| Term | Definition | Source |
|------|------------|--------|
| Approach Training | Pre-operation preparation; per-Approach skill. | threadwork §2.1 |
| Diagnosis | Mandatory pre-operation read. **No roll.** Required before Mending/Locking/Dissolution/POP. *§2.2 STRUCK ED-134/124, but term retained as gating concept.* | threadwork §2.2 |
| Eligibility (verify before rolling) | Pre-Leap eligibility check. | threadwork §2.3 |
| The First Leap (Event Scene) | First-Leap onboarding scene. | threadwork §2.3 |

### 7.2 The Leap
| Term | Definition | Source |
|------|------------|--------|
| Leap (the operation) | Entering Thread contact. **Full-round action; Priority 5.** Prerequisite for all Thread operations. | threadwork §2.3 |
| The Leap Roll | Dice resolution of Leap attempt. | threadwork §2.3 |
| Contact Duration | Length of operational window post-Leap. **ED-694: Thread Fatigue replaces Contact Rounds.** | threadwork §2.3 |
| Contact Rounds (legacy) | Old name for Contact Duration unit. **Use Thread Fatigue.** | threadwork (legacy) |
| Thread Fatigue | Action-economy resource for Thread operations. | derived_stats §6.1 |
| Thread Operation Visibility | Who perceives an active Thread operation. | threadwork §2.3 |
| Rendered-Level Thread Event Visibility (ED-677) | Who perceives operations at the rendered layer. | threadwork §2.3 |

### 7.3 Operation types (the 11 — granular)
| Op | Class | Definition | Prereq | Source |
|----|-------|------------|--------|--------|
| **Weaving** | restorative | Things Cohere. Stabilises threads, restores actualisation. | TS varies | threadwork §2.4 |
| **Pulling (Present-Oriented)** | manipulative | Things Open. De-actualises threads. | TS varies | threadwork §2.4 |
| **Past-Oriented Pulling** (POP) | manipulative | Pulling targeting historical thread configurations. | **TS 70+** | threadwork §2.4 |
| **Locking** | destructive | Forced Resolution; permanent stabilization of a thread configuration. | **TS 50+** | threadwork §2.4 |
| **Dissolution** | destructive | Forced Resolution; destruction of a thread configuration. | **TS 50+** | threadwork §2.4 |
| **Mending** | restorative | Substrate repair. Targets Gaps and Shifting Objects. | **TS 50+** | threadwork §2.4 |
| Diagnosis | (no-roll prereq) | Required pre-op read. | — | threadwork §2.2 |
| Leap | (gateway) | Contact entry. | — | threadwork §2.3 |
| Forced Resolution (FR) | umbrella | Collective term for Locking and Dissolution. **TN 8. No TPS added.** | — | threadwork §2.4 |
| Dissolution Residue | (residue mechanic) | Potency-rated bonus dice from prior Dissolution. **Costs −1 Coherence per use.** | — | threadwork §3.4 |
| Overweaving | (penalty state) | Multiple ops on same configuration in one contact window. **+1 Ob per op after first.** | — | threadwork |

### 7.4 Collective / opposing operations
| Term | Definition | Source |
|------|------------|--------|
| Collective Operations | Multi-practitioner cooperation. | threadwork §2.5 |
| Opposing Operations — Contested Intentionality | Two practitioners working in opposition (PP-632/PP-653). | threadwork §2.6 |
| Opposing Engagement Modifier | Pool modifier under opposition. | threadwork §2.6 |
| Resolution Table (opposing) | Outcome table for opposed ops. | threadwork §2.6 |
| Knot Strain | Knot damage from opposed ops. | threadwork §2.6 |
| Co-Movement (opposing) | Threadwork co-movement mechanic during opposition. | threadwork §2.6 |
| FR vs FR Both-Fail Scaling | Special outcome when both FR ops fail. | threadwork §2.6 |
| Sustained Opposition | Persistent counter-op state. | threadwork §2.6 |
| N-Way Opposing Operations | 3+ practitioner opposition rules. | threadwork §2.6 |
| Combat Timing (Thread integration) | When ops resolve relative to combat phases. | threadwork §2.6 |

### 7.5 Coherence track (10→0)
| Term | Definition | Source |
|------|------------|--------|
| What Coherence Measures | Personal rendering integrity. | threadwork §3.1 |
| Coherence Reduction | Sources of −Coherence. | threadwork §3.2 |
| Coherence Thresholds | Banded effects. | threadwork §3.3 |
| Recovery (Coherence) | Restoration procedures. | threadwork §3.5 |
| Fallout Tables | Outcome tables at low Coherence. | threadwork §3.6 |
| Rendering Crisis Resolution | Crisis-point procedure (PP-194 PROVISIONAL). | threadwork §3.7 |
| Rendering Crisis — Narrative Structure (ED-681) | Narrative-side resolution structure. | threadwork §3.7 |

### 7.6 Co-Movement (Version C)
| Term | Definition | Source |
|------|------------|--------|
| Co-Movement (the mechanic) | Why the actual effect is randomised. | threadwork §4.1–4.2 |
| Auto-Effect Tables | Per-result effect tables. | threadwork §4.3 |
| Co-Movement Cards 1–15 | **Canonical card list (ED-577).** | threadwork §4.3 |
| Co-Movement Card | Strategic-layer mechanism resolved on every Thread op result. *(BG-name reflecting card-economy origin; engine implementation is automatic event.)* | glossary §7 |
| History Resonance | History-stat-driven resonance bonus. | threadwork §4.4 |
| Flashback Anchoring | Mechanic for tying ops to past scenes. | threadwork §4.4 |
| Revised Co-Movement Card Deck (18 cards) | BG-mode 18-card variant. | threadwork §7.1 |

### 7.7 Mending Stability track (links to §4 / §L)
| Term | Definition | Source |
|------|------------|--------|
| What Rendering Stability Measures | (Legacy term — now Mending Stability per ED-731.) | threadwork §5.1 |
| Mending Stability Degradation Sources | Sources of MS reduction. | threadwork §5.2 |
| Mending Stability Thresholds | Banded effects. | threadwork §5.3 |
| MS in Board Game | BG-mode MS handling. | threadwork §5.4 |
| MS in Hybrid | Hybrid-mode MS handling. | threadwork §5.5 |
| Thread Revelation Curve | Per-season Thread visibility schedule (campaign_architecture §4). | threadwork §5.6 |
| Mass Battle MS Cost | Flat −1 per battle in which any Thread op occurs (campaign_architecture §3.1). PP-192 STRUCK and replaced. | values_master conflicts |
| Lock Chronic Drift | Per-season MS drain per active Lock by scale. PP-604 canonical. | threadwork |

### 7.8 Threadcut Beings (§6 of doc)
| Term | Definition | Source |
|------|------------|--------|
| Threadcut Beings | Beings cut from substrate. *Recontextualized per canon/01.* | threadwork §6 |
| Ontological Status | Threadcut metaphysical position. | threadwork §6.1 |
| Observer-Dependent Rendering | Rendering varies by observer's TS. | threadwork §6.2 |
| Rendering Beyond Observer Capacity | Mechanic when observer can't render. | threadwork §6.2 |
| Mechanical Distinctions (Threadcut) | Concrete mechanical differences. | threadwork §6.3 |
| De-Actualisation | Substrate-loss class. | threadwork §6.4 |

### 7.9 Cross-mode (BG / Hybrid)
| Term | Definition | Source |
|------|------------|--------|
| New Order: Mend (BG) | BG-only Domain Action: Mend. | threadwork §7.1 |
| Lock Chronic Drift (BG track) | BG-mode tracking of Lock drain. | threadwork §7.1 |

### 7.10 Settlement-level thread integration
| Term | Definition | Source |
|------|------------|--------|
| Settlement-level Thread Consequences (Throughline T1) | Per-settlement Thread effects. | threadwork (preamble), settlement_layer §4.4 |

---
## SILO 8 — PERSONAL RESOLUTION: FIELDWORK

> **Word-class rule:** Fieldwork is a meta-system spanning four sub-modes. Avoid colliding fieldwork's *Disposition* (NPC attitude) with combat's *Disposition* (none — clean), but DO note: **Disposition Track** appears in BOTH fieldwork (§5.1) AND as an NPC attribute. Different ontological registers for the same word; flagged.

### 8.1 Top-level fieldwork architecture
| Term | Definition | Source |
|------|------------|--------|
| Fieldwork (the system) | Umbrella for Exploration, Investigation, Socializing, Exposure. | fieldwork §0 |
| Intelligibility Gradient | Core principle: information-state degrades by depth. | fieldwork CORE |
| Depth Axis | Depth-of-engagement spectrum. | fieldwork §1 |
| Fieldwork Pool | Dice pool for fieldwork actions. | fieldwork §2 |
| Primary Attribute by Activity | Activity → driver attribute mapping. | fieldwork §2.1 |
| System Transition Rules | Within-fieldwork sub-mode transitions. | fieldwork §2.3 |
| Threadwork During Fieldwork | Thread ops mid-fieldwork. | fieldwork §2.4 |
| Domain Echo from Investigation | Investigation outcome → strategic echo. | fieldwork §2.5 |
| Knot-Mediated Remote Investigation | Knot-network remote-fieldwork mechanic. | fieldwork §2.6 |
| Non-Sensitive Partners and Dissonance | Non-practitioner companion handling. | fieldwork §2.7 |
| Threadcut Being Social Fieldwork | Special-case fieldwork against Threadcut entities. | fieldwork §2.8 |

### 8.2 Exploration sub-mode
| Term | Definition | Source |
|------|------------|--------|
| Exploration | Sub-mode for traversing unknown space. | fieldwork §3 |
| Point of Interest | POI — discoverable site. | fieldwork §3.1 |
| Discovery Procedure | Procedure for revealing POIs. | fieldwork §3.2 |
| Movement and Time | Movement-rate and time-cost rules. | fieldwork §3.3 |
| Rendering Strain at Depth 3+ | High-depth Coherence-cost mechanic. | fieldwork §3.4 |

### 8.3 Investigation sub-mode
| Term | Definition | Source |
|------|------------|--------|
| Investigation | Sub-mode for clue-gathering. | fieldwork §4 |
| Evidence Track | Per-case evidence accumulation. | fieldwork §4.1 |
| Investigation Actions | Investigation-specific verbs. | fieldwork §4.2 |
| Evidence Quality | Quality-grade per evidence. | fieldwork §4.3 |
| Epistemological Barrier | Maximum certainty achievable through Evidence alone. | fieldwork §4.3 |
| Desperate Trail | Fail-forward mechanic at zero evidence. | fieldwork §4.4 |
| Thread-Read | Perceptive-Leap mechanic for fast-track investigation. | fieldwork §4.5 |
| Contested Investigation | Two parties investigating same case. | fieldwork §4.6 |

### 8.4 Investigation systems (the four-system stack — separate canon)
| System | Definition | Source |
|--------|------------|--------|
| **NPC Population Engine (NPE)** | Per-territory population synthesis (System 1). | investigation_systems §System 1 |
| Territory Social Ecology | Per-territory NPC distribution and roles. | investigation_systems |
| NPC Genome Record | Per-NPC structured record. | investigation_systems |
| Two-Tier Generation | Named + procedural NPC generation. | investigation_systems |
| Persistence (NPE) | Memory model for NPCs. | investigation_systems |
| Named NPC Stance Triangles | Three-way relationship mappings. | npc_stance_triangles |
| **Investigation Interface** | Player-facing investigation tool (System 2). | investigation_systems §System 2 |
| Scene-as-Graph | Scene structured as node-graph for traversal. | investigation_systems |
| Traversal Economy | Cost rules for scene-graph traversal. | investigation_systems |
| Case Board | Investigation aggregation surface. | investigation_systems |
| Case Board Thread Layer | Thread-side overlay (ED-680). | investigation_systems |
| Temporal Dimension | Time-axis on scenes. | investigation_systems |
| Zoom In Triggers (investigation) | Conditions auto-zooming to scene scale. | investigation_systems, scale_transitions §4.3 |
| **Dialogue Lattice** | Dialogue-system architecture (System 3). | investigation_systems §System 3 |
| Gate Types | Dialogue gating-condition classes. | investigation_systems |
| Visibility Rules | What NPCs can/cannot say. | investigation_systems |
| Outcome Types (dialogue) | Categorisation of dialogue outcomes. | investigation_systems |
| Sincerity Gate | Detection of sincere vs deceptive responses. | fieldwork §5.3, investigation_systems |
| **Response Resolution Matrix** | Five-filter response chain (System 4). | investigation_systems §System 4 |
| Five-Filter Chain | Sequenced response-resolution filters. | investigation_systems |
| Bidirectionality | Mutual filtering between speaker and listener. | investigation_systems |
| Interdependency Matrix | Filter cross-dependencies. | investigation_systems |

### 8.5 Socializing sub-mode
| Term | Definition | Source |
|------|------------|--------|
| Socializing | Sub-mode for non-contest social interaction. | fieldwork §5 |
| Disposition Track | NPC attitude track toward an actor. **Bonded by Bonds attribute cap (per derived_stats §10.1).** | fieldwork §5.1 |
| Social Actions (Non-Contest) | Verbs available outside contest. | fieldwork §5.2 |
| Sincerity Gate | (See §8.4 — fieldwork-side application.) | fieldwork §5.3 |
| Information Gates | Information-availability gating per Disposition tier. | fieldwork §5.4 |
| Beliefs Integration (socializing) | Belief-driven social interaction effects. | fieldwork §5.5 |
| Knot Integration (socializing) | Knot-influence on social interaction. | fieldwork §5.6 |
| Contest Escalation | Boundary at which socializing becomes Contest. | fieldwork §5.7 |
| Negotiate Boundary | Shared boundary between Socializing and Contest. | fieldwork §5.7 |
| Niflhel Social Toolkit Extension | Toolkit for covert/hostile social action. | fieldwork §5.8 |
| NPC-Initiated Social Engagement | NPC-driven social scene opening. | fieldwork §5.9 |

### 8.6 Exposure sub-mode
| Term | Definition | Source |
|------|------------|--------|
| Exposure | Sub-mode for tracking detection-risk. | fieldwork §6 |
| Cover (derived value) | Concealment level. | fieldwork §6.1 |
| Exposure Track | Detection-risk accumulator. | fieldwork §6.2 |
| Exposure Sources | Things that raise Exposure. | fieldwork §6.3 |
| Exposure Reduction | Things that lower Exposure. | fieldwork §6.4 |
| Church Attention Pool | Church's investigative attention; tied to Exposure. | fieldwork §6.5 |

### 8.7 BG / Hybrid / Godot variants
| Term | Definition | Source |
|------|------------|--------|
| Survey (BG action) | Consul Inward variant — fieldwork as BG action. | fieldwork §8.1 |
| Hybrid Fieldwork Procedure | Hybrid-mode fieldwork integration. | fieldwork §9.1 |
| Hybrid Fieldwork Timing | Phase placement of fieldwork in Hybrid. | fieldwork §9.2 |
| Exploration Map Architecture | Godot exploration-system spec. | fieldwork §10.1 |
| Intelligibility Gradient Visualisation | UI for Depth-axis state. | fieldwork §10.2 |
| Investigation Journal System | Player-facing journal UI. | fieldwork §10.3 |
| Disposition and Dialogue (UI) | UI surface for Disposition states. | fieldwork §10.4 |
| Dice Visualisation | UI for dice-pool resolution. | fieldwork §10.5 |
| Season and Clock Integration (fieldwork) | Time-passing during fieldwork. | fieldwork §10.6 |

---
## SILO 9 — PIETY & CHURCH INFLUENCE

> **Word-class rule:** Piety Track (PT, per-territory, 0–5) is a *strategic-layer* track that takes its name from the *personal-layer* Conviction concept (§1.5). **This is intentional — population conviction = aggregated personal conviction at population scale.** The 13 individual Convictions (Faith, Authority, etc.) live in §1; the strategic track that scores Solmund-vs-Restoration orthodoxy lives here. *Note: "Conviction Track" and "CV" are legacy aliases per ED-644; canonical abbreviation is PT.*
>
> Note: this silo overlaps with §12-Clocks (PT is technically a per-territory clock) and with §14-Victory (PT drives Church victory paths).

### 9.1 Per-territory PT stat
| Term | Definition | Source |
|------|------------|--------|
| Piety Track (per-territory) | PT | Solmund-orthodoxy axis at population scale per territory. **0–5.** *Was "Conviction Track" — renamed per silo isolation directive. ED-644 confirms PT canonical.* | conviction_track_v30 §1 |
| Starting Values (PP-406) | Per-territory initial PT by faction-ownership and adjacency. | conviction_track_v30 §1.1 |
| Movement Rules (PP-408) | Procedure for PT change. | conviction_track_v30 §1.2 |
| Movement Actions | Specific CV-changing actions per faction. | conviction_track_v30 §1.2 |
| Calamity Drift (PP-409) | RS-linked (now MS-linked) PT erosion. | conviction_track_v30 §1.3 |
| Thread Operation PT Drift (ED-676) | Per-Thread-op PT erosion in territory. | conviction_track_v30 §1.3b |
| Consecrated Status (PP-410) | Church-blessed binary territory state. | conviction_track_v30 §1.4 |

### 9.2 Church Seizure mechanics
| Term | Definition | Source |
|------|------------|--------|
| Church Seizure Ob (PP-411) | Obstacle for Church-Seizure attempts. | conviction_track_v30 §2 |
| Ob Formula (Seizure) | Formula for Seizure Ob. | conviction_track_v30 §2 |
| Seizure Results | Outcome bands of a Seizure attempt. | conviction_track_v30 §2 |
| Mass Seizure | CI ≥ 60 probabilistic Seizure declaration. **Replaces gated 75-threshold Seizure.** | ci_political §2.2, conviction_track_v30 |

### 9.3 CI (Church Influence) generation — formerly TC (Theocracy Counter)
> **Terminology rename:** Theocracy Counter (TC) **renamed to Church Influence (CI)** per ED-782. TC remains in some legacy doc text; CI is canonical. **Per alias_registry: TC no longer used at term level.**

| Term | Definition | Source |
|------|------------|--------|
| CI Generation (PP-412) | CI accrual procedure. *(Heading in conviction_track_v30 §3 still says "TC Generation" — queued for fix.)* | conviction_track_v30 §3 |
| Seasonal CI Calculation | Per-season CI accrual procedure. | conviction_track_v30 §3 |
| Piety Domain Action (DISSOLVED) | Removed Domain Action; subsumed elsewhere. | conviction_track_v30 §3 |
| CI Pacing Analysis | Pacing characteristics of CI accumulation. | conviction_track_v30 §3 |

### 9.4 Church Victory paths (drive from Piety Track)
| Term | Definition | Source |
|------|------------|--------|
| Church Victory Conditions (PP-413) | ED-110 resolution. | conviction_track_v30 §4 |
| Primary Victory — Territorial Consolidation | CV-driven province count. | conviction_track_v30 §4.1 |
| Alternate Victory — Altonian Theocracy Path (PP-414) | Alt path using IP and Altonian invasion. | conviction_track_v30 §4.2 |
| Hollow Victory — Church + Hafenmark (PP-415) | Co-victory path. | conviction_track_v30 §4.3 |

### 9.5 Restoration Movement (RM) emergence
| Term | Definition | Source |
|------|------------|--------|
| RM Emergence as Latent Faction (PP-416) | Procedure for RM activation from Varfell. | conviction_track_v30 §5 |
| Varfell-RM Relationship Track | Varfell-side track gating RM emergence. | conviction_track_v30 §5.1 |
| Emergence Trigger | Threshold-based trigger for RM activation. | conviction_track_v30 §5.2 |
| Active RM — Stats and Actions | RM stats once activated. | conviction_track_v30 §5.3 |
| Suppression and Resolution (RM) | Mechanics for suppressing emerged RM. | conviction_track_v30 §5.4 |

### 9.6 Varfell Paths B & C
| Term | Definition | Source |
|------|------------|--------|
| Path B — Southernmost Dominion (PP-417 redesigned) | Varfell southern-conquest victory path. | conviction_track_v30 §6.1 |
| Path C — Thread Supremacy | **STRUCK PP-663, 2026-04-19.** | conviction_track_v30 §6.2 |
| Co-Victory Replacement — Varfell + RM (PP-418) | Replacement co-victory pairing. | conviction_track_v30 §7 |

### 9.7 Presentation layer (PT → player)
| Term | Definition | Source |
|------|------------|--------|
| Piety Track Presentation Layer | World→player surfacing of PT state. | conviction_track_v30 §11 |
| PT Change Environmental Events | Visible world-events from PT shifts. | conviction_track_v30 §11.1 |
| Church Attention Pool (player-facing) | Player-facing CI/Attention indicator. | conviction_track_v30 §11.2 |
| CI Milestone Presentation | Milestone-display schema. | conviction_track_v30 §11.3 |

---
## SILO 10 — STRATEGIC RESOLUTION: MASS COMBAT (Mass Battle)

> **Word-class rule:** unit-scale combat. Vocabulary deliberately renamed (PP-232) to avoid colliding with personal combat: **Strength→Size, Combat Power→Power, Cohesion→Discipline, CR→Command.** Vocabulary deliberately renamed (PP-233) for the core formula.

### 10.1 Battle scale and unit
| Term | Definition | Source |
|------|------------|--------|
| Mass Battle (the system) | TTRPG/Hybrid + BG-mode unit-scale combat. | mass_battle §A.1 |
| Battle Scale | Scale-classification for an engagement. | mass_battle §A.3 |
| Unit Stat Block (1–7) | Five canonical 1–7 unit stats below + DR. | mass_battle §A.4 |
| Weapon Effectiveness Reference | Cross-weapon-class table. | mass_battle §A.2 |

### 10.2 Unit stats (post-PP-232 renames — granular)
| Term | Replaces | Definition | Source |
|------|----------|------------|--------|
| **Size** | Strength (legacy) | Unit's troop count proxy. **At 0 = unit destroyed.** | mass_battle §A.4 |
| **Power** | Combat Power, CP (legacy) | Offensive stat. **Damage per success = 1 + Power.** | mass_battle §A.4 |
| **Discipline** | Cohesion (legacy) | Defensive coherence stat. | mass_battle §A.4 |
| **Command** | CR — Command Rating (legacy) | Officer/NCO leadership stat. **Formula: ceil((Presence + Cognition) / 2).** | mass_battle §A.5 |
| **Damage Resistance** | DR | Damage reduction stat. **Cross-listed with personal combat §5.3.** | mass_battle §A.4 |
| **Health per Size** | H | min(Discipline, Command) + DR. | alias_registry |
| **Total Health** | — | Size × H. | alias_registry |

### 10.3 Formation and turn structure
| Term | Definition | Source |
|------|------------|--------|
| Formation Type | One of four canonical formations. | mass_battle §A.6 |
| Battle Turn Structure | Per-turn phase order (Cascade Phases 1–6). | mass_battle §A.7 |
| Cascade Phase 1 — (initiation) | First cascade phase. | mass_battle §A.7 |
| Cascade Phase 6 — Engagement | Damage resolution phase (Volley + offensive Thread damage simultaneous). | mass_battle §A.7 |
| Tactics | Pre-battle tactical choice (with own card list in BG). | mass_battle §A.8 |
| Environmental Modifiers | Terrain, weather, etc. | mass_battle §A.9 |

### 10.4 Thread integration in Mass Battle
| Term | Definition | Source |
|------|------------|--------|
| Thread Operations in Mass Battle | Per-op rules at mass scale (ED-050: own phase between Manoeuvre and Engagement). | mass_battle §A.10 |

### 10.5 Special / contextual
| Term | Definition | Source |
|------|------------|--------|
| Southernmost rules | Special-rules envelope for Calamity-zone battles. | mass_battle §A.11 |
| Rout and Pursuit | Post-defeat unit-flight mechanics. | mass_battle §A.12 |
| Reinforcement (between battles) | Inter-battle unit recovery. | mass_battle §A.13 |
| Campaign Supply | Multi-battle supply mechanic (historical_precedents §1.3a). | mass_battle §A.14b |
| Levy Restriction | Levied-troop limitation (historical_precedents §1.3b). | mass_battle §A.14c |

### 10.6 BG-mode mass battle
| Term | Definition | Source |
|------|------------|--------|
| BG Unit Stats (pre-printed on tokens) | Token-level stat preprint. | mass_battle §B.2 |
| BG Battle Resolution | Margin-system resolution. | mass_battle §B.3 |
| Pool Formula | BG battle pool computation. | military_layer §2.1 |
| Battle Outcome (Margin System) | Outcome banding by net margin. | military_layer §2.2 |
| BG → TTRPG Handoff | Carry-over rules from BG battle to TTRPG aftermath. | military_layer §2.3 |
| Tactic Cards | BG-mode tactical card deck. | mass_battle §B.4 |
| Hybrid Handoff | BG ↔ Hybrid bridging rule. | mass_battle §B.5 |

### 10.7 Mass-combat → world bridges
| Term | Definition | Source |
|------|------------|--------|
| Post-Battle Consequence Scenes | Cinematic post-battle scenes. | mass_battle §D.1 |
| Named Unit Officers | Officer-NPC tracking on units. | mass_battle §D.2 |
| Player Morale Effect | Player-character morale impact post-battle. | mass_battle §D.3 |
| Army Morale (derived composite) | Army-level composite from Discipline, Casualties, Officer state. | mass_battle PART C, derived_stats §10.2 |

### 10.8 Battle Consequences (canonical — ED-542)
| Section | Definition | Source |
|---------|------------|--------|
| §E.1 Immediate Consequences | At battle resolution. | mass_battle §E.1 |
| §E.2 Accounting Consequences | Per-season accounting impact. | mass_battle §E.2 |
| §E.3 Exceptions | Edge-case carve-outs. | mass_battle §E.3 |
| §E.4 Cumulative Caps | Per-season capped totals. | mass_battle §E.4 |

### 10.9 Unit production / quality
| Term | Definition | Source |
|------|------------|--------|
| Unit Token | Minimal abstracted unit on the BG board. | military_layer §1.1 |
| Unit Type | Categorical unit class. | military_layer §1.2 |
| Military Stat → Unit Power Ceiling | Faction Military stat caps unit Power. | military_layer §1.3 |
| Muster Output | Units gained per Muster action. | military_layer §1.4 |
| Muster Prerequisites | Conditions for Muster eligibility. | military_layer §1.5 |
| Experience (units) | Persistent unit-level XP. | military_layer §1.6 |
| Wealth Zero Unit Degradation | Unit-quality decay at faction Wealth=0. | military_layer §1.7 |
| Knights Templar | Church-only unit type (ED-633). | military_layer §1.8 |
| Siege Action | New action category (ED-633). | military_layer §1.9 |

### 10.10 Cross-system notes (mass combat)
| Term | Definition | Source |
|------|------------|--------|
| Officer Capture | Three-Condition Gate trigger for Stability hits. | faction_layer §6.1 |
| Significant Loss | Trigger-5 stability event from battle losses. | faction_layer §6.2 |
| Three-Condition Gate (Trigger 5) | Three-clause spec for Stability hit. | faction_layer §6.2 |
| Ransom | Officer-recovery mechanic (ED-334/335). | faction_layer §6.3 |
| BG Mode Officer Fate | BG-only officer-handling (No Zoom In). | faction_layer §6.4 |

---
## SILO 11 — STRATEGIC RESOLUTION: FACTION LAYER / DOMAIN ACTIONS

> **Word-class rule:** strategic-layer faction-action vocabulary. Note: **Domain Action** (faction strategic action) and **Action** (general mechanic verb across all systems) are intentionally distinguished — *Domain Action* is always written in full when it means the strategic-layer instance.

### 11.1 Faction layer architecture
| Term | Definition | Source |
|------|------------|--------|
| Faction Layer | Strategic-layer system enclosing Stability, Treaty, Parliament, Domain Actions. | faction_layer §0 |
| Domain Action | Faction-level strategic action resolved at scale-transition phase. **Unit of strategic-layer decision.** | scale_transitions, faction_layer |
| Domain Echo | Faction-level consequence triggered by personal/scene-level decisive outcomes. | scale_transitions §5 |
| Grievance Marker | Tracked grievance state generated by Domain Echos. | glossary §7 |

### 11.2 Stability mechanics (cross-listed with §2 Faction Attributes)
> Five Stability Triggers and the Faction Collapse Exit Procedure ED-675 enumerated in §2.5; not repeated here.

| Term | Definition | Source |
|------|------------|--------|
| Stability (the system) | Redesigned faction-internal state subsystem. | faction_layer §1 |
| Stability Recovery | Procedure for regaining Stability points. | faction_layer §1.3 |
| Accounting Stability Check | Per-season check at Accounting phase. | faction_layer §1.4 |

### 11.3 Territorial Occupation
| Term | Definition | Source |
|------|------------|--------|
| Territorial Occupation | Faction-on-faction territory hold. | faction_layer §2 |
| Occupation Establishment | Procedure for establishing occupation. | faction_layer §2.2 |
| Occupation Effects | Concrete effects (income redirect, Stability hit, etc.). | faction_layer §2.3 |
| Occupation Duration | Duration rules and Control Transfer. | faction_layer §2.4 |
| Resistance Check | Per-season test for native uprising. | faction_layer §2.5 |
| Political Vacuum | Power-vacuum state (PP-500). | faction_layer §2.6 |
| Church Seizure (occupation-side integration) | How CI-Seizure interacts with occupation. | faction_layer §2.7 |

### 11.4 Treaty mechanics
| Term | Definition | Source |
|------|------------|--------|
| Treaty (the mechanic) | Bilateral or multilateral pact. | faction_layer §3 |
| Treaty Types | Categorical types of treaty. | faction_layer §3.1 |
| Initiating a Treaty | Initiation procedure. | faction_layer §3.2 |
| Negotiation Structure (Three Phases) | Phased negotiation procedure. | faction_layer §3.3 |
| Treaty Effects on Stability | Stability impact of treaty terms. | faction_layer §3.4 |
| Casus Belli | Justified war-trigger. | faction_layer §3.5 |

### 11.5 Negotiation mechanics (extended)
| Term | Definition | Source |
|------|------------|--------|
| Faction-Specific Negotiation Bonuses | Per-faction +X dice. | faction_layer §4.1 |
| Grand Debate | Hybrid/TTRPG-only contest format at faction layer. | faction_layer §4.2 |

### 11.6 Parliamentary mechanics
| Term | Definition | Source |
|------|------------|--------|
| Parliament (the mechanic) | Strategic-layer voting system. | faction_layer §5 |
| Phase Placement (Parliament) | Where votes occur in turn sequence. | faction_layer §5.2 |
| Vote Mechanics | Procedure for vote resolution. | faction_layer §5.3 |
| Parliamentary Action | A Domain-Action subtype usable in Parliament. | faction_layer §5.4 |
| Target Rebuttal | Voted-against faction's response procedure. | faction_layer §5.5 |
| CI Parliament Interaction | Church-Influence's effect on Parliament. | faction_layer §5.6 |
| Turmoil Parliament Interaction | PS-counter's effect on Parliament. | faction_layer §5.6b |
| Wealth Zero Consequence | Parliamentary effect of W=0. | faction_layer §5.7 |
| NPC Vote Behavior | Algorithmic NPC-faction vote logic. | faction_layer §5.8 |

### 11.7 BG / TTRPG / Hybrid mode variations (for the faction layer)
| Term | Definition | Source |
|------|------------|--------|
| Turn Sequence Integration Reference | Cross-mode turn-sequence reference. | faction_layer §7 |
| BG Mode (faction layer) | Pure-BG operation mode. | faction_layer §8.1 |
| TTRPG Mode (faction layer) | TTRPG-mode handling of faction layer. | faction_layer §8.2 |
| Hybrid Mode (faction layer) | Hybrid bridging. | faction_layer §8.3 |
| CI Formula (full) | Full sim-integration formula for CI. | faction_layer §9 |

### 11.8 BG-side faction actions enumeration
| Action | Definition | Source |
|--------|------------|--------|
| Govern | Stat-changing faction action (PP-174 / §4.2). | ci_political §4.2 |
| Trade | Wealth-economy action (§4.3). | ci_political §4.3 |
| Assert | TC-pumping action (§3.6). | military_layer §3.6 |
| Suppress | TC-attacking opponent's pump (§3.7). | military_layer §3.7 |
| Charity Advantage | Conditional Mandate-yield bonus (§3.4). | military_layer §3.4 |
| Templar Presence | Church-Mil action (§3.5). | military_layer §3.5 |
| Hafenmark Structural Suppression (Baralta) | Faction-specific structural suppression. | military_layer §3.8 |
| Conditional Passive (TC) | Passive-yield rule replaced PP-402 (Unconditional Passive). | military_layer §3.2 |
| Piety Yield (retained, refined) | Refined passive Piety mechanic. | military_layer §3.3 |
| Posture Priority Framework | AI-posture decision-tree. | ci_political §6.1 |

### 11.9 Card system / cooldown
| Term | Definition | Source |
|------|------------|--------|
| Card Hands | Per-faction action-card hand (PP-177). | ci_political §5.1 |
| Card → Action Mapping | Card-to-action lookup. | ci_political §5.2 |
| Cooldown Track | Per-action cooldown counter. | ci_political §5.3 |
| Renewal | Card-refresh mechanic. | ci_political §5.3 |

### 11.10 NPC-side faction logic
| Term | Definition | Source |
|------|------------|--------|
| NPC Priority Trees | Algorithmic action-prioritization for NPC factions. | params/bg/npc_priority_trees |
| NPC Vote Behavior | (See §11.6.) | faction_layer §5.8 |

---
## SILO 12 — STRATEGIC RESOLUTION: CLOCKS

> **Word-class rule:** clocks are world-or-faction-state numerical tracks. They are referenced *by* multiple play systems but their *definitions* live in this silo. **Piety Track (PT) is a per-territory clock but logically lives in §9 — see cross-silo overlap §2-overlap.**

### 12.1 World-state clocks (also cross-listed in §4)
| Term | Abbr | Range | Direction | Loss-state | Source |
|------|------|-------|-----------|------------|--------|
| Mending Stability | MS | 100→0 | down | 0 = The Rupture | threadwork §5 |
| Thread Tension | TT | 0–100+ | up | (no canonical cap) | threadwork |
| Turmoil Counter | — | counter | up | escalating PS shocks | victory §0.3, peninsular_strain_v30 |

### 12.2 Faction / political clocks
| Term | Abbr | Range | Direction | Mode | Definition | Source |
|------|------|-------|-----------|------|------------|--------|
| Church Influence | CI | 0–100 | up | ALL | Church faction's institutional reach. **Renamed from Theocracy Counter (TC) per ED-782.** | ci_political §2 |
| CI Milestone — Church Assertive | — | 40 | — | — | +1D on Assert and Seizure rolls. | ci_political |
| CI Milestone — Institutional Reach | — | 55 | — | — | Ob +1 to actions opposing Church Domain Actions. | ci_political |
| CI Milestone — Mass Seizure | — | 60 | — | — | Probabilistic Mass Seizure available; **P = ((CI-60)/40)^3.3** per season. | ci_political §2.2 |
| CI Milestone — Church Dominant | — | 65 | — | — | Secular factions need extra slot to oppose Church motions. | ci_political |
| CI Milestone — Church Ascendant | — | 80 | — | — | Seizure Ob -1 globally; PT drift. | ci_political |
| CI Milestone — Theocracy Unification Attempt | — | 100 | — | — | (See ci_political_v30 §2.2.) | ci_political §2.2 |
| Institutional Pressure | IP | 0–100 | up | ALL | Altonian-pressure / institutional-pressure track. **75/80 = Altonian Vanguard (BG).** | values_master |
| Public Instability | PI | 0–10 | down | BG | Public-confidence track. **0 = Parliament dissolved + Löwenritter coup.** | values_master |
| Cooldown Track | — | per-action | down | — | Per-action cooldown counter. | ci_political §5.3 |
| Piety Track (per-territory) | PT | 0–5 | both | ALL | Per-territory Solmund-orthodoxy track. **Same as "Conviction Track" per ED-644. Cross-listed §3.1, §9.** | conviction_track_v30 |

### 12.3 Faction-internal pseudo-clocks
| Term | Definition | Source |
|------|------------|--------|
| Stability (faction state) | Per-faction internal coherence (1–7); not strictly a clock but tracked as one. | faction_layer §1 |
| Standing | Per-faction reputation track (0–10). | factions/stats_1_7_scale |
| Popular Support (PS) | Per-**settlement** (0-7) outcome accumulator, aggregated into faction Mandate (LPS-2e). Corrected 2026-07-08 (ED-IN-0029, OPT-AV-7) — was "Public Support," faction-scale. | `settlement_layer_v30.md §1.8` |
| Legitimacy (L) | Per-settlement (0-7) trust currency, aggregated into Mandate. Corrected 2026-07-08 (same basis) — was faction-scale. | `settlement_layer_v30.md §1.8` |
| Church Attention Pool | Player-facing Church-detection track. | conviction_track_v30 §11.2, fieldwork §6.5 |
| Public Expectation | Populace's expected behaviour gating outcomes. | faction_behavior §3.5 |

### 12.4 Renewal / pacing mechanics (clock infrastructure)
| Term | Definition | Source |
|------|------------|--------|
| Card Renewal | Card-replenishment mechanic (PP-177). | ci_political §5 |
| Seasonal Cap | Per-season ceiling for CI generation. | ci_political §2.4 |
| Seasonal CI Calculation (legacy term — was "seasonal TC calc") | Per-season CI-accrual procedure. | conviction_track_v30 §3 |
| Accounting (phase) | Per-season faction-accounting tick. | faction_layer §1.4 |

### 12.5 Narrative-specific / deprecated clocks
| Term | Definition | Source |
|------|------------|--------|
| Torben Loyalty Clock | TLK — narrative-specific clock (range 10→0). **DEPRECATED — drain rate undefined (F72 gap).** | alias_registry |
| Elske Loyalty Track (ED-624) | Conditional Löwenritter-side track. | victory §3.6 |
| Varfell-RM Relationship Track | RM-emergence-gating track (cross-listed §I §9.5). | conviction_track_v30 §5.1 |

---
## SILO 13 — STRATEGIC RESOLUTION: TENSIONS DECK / ASSASSINATION / SPECIAL

> Strategic-layer auxiliary systems that don't fit the Domain-Action / Parliament / Treaty / Battle pattern. These are "special-event" mechanisms.

### 13.1 Tensions Deck (BG)
| Term | Definition | Source |
|------|------------|--------|
| Tensions Deck | BG-mode card deck of escalation events. | params/bg/tensions_deck |
| Tension Card | Individual deck entry. | tensions_deck |
| Tension Trigger | Condition that draws a Tension Card. | tensions_deck |
| Tension Effect | Per-card outcome. | tensions_deck |

### 13.2 Royal Assassination Fuse
| Term | Definition | Source |
|------|------------|--------|
| Royal Assassination Fuse | Specific BG escalation fuse for King-targeted assassination. | params/bg/royal_assassination |
| Fuse Trigger | Condition starting the Fuse countdown. | royal_assassination |
| Fuse Phases | Phased fuse-state progression. | royal_assassination |

### 13.3 Conflict architecture (top-level)
| Term | Definition | Source |
|------|------------|--------|
| Conflict Architecture (proposal) | Cross-system unification of conflict mechanics. | conflict_architecture_proposal |
| Niflhel Dissolution | Strike of Niflhel as faction; mechanic redistribution. | conflict_architecture, CR-STRIKE-2026-04-19 |
| Löwenritter Graduated Autonomy | Phased Löwenritter activation as faction. | conflict_architecture |

### 13.4 Stress patches (BG modular)
| Term | Definition | Source |
|------|------------|--------|
| Stress Patches | Modular BG-mode stress events. | params/bg/stress_patches |

---
## SILO 14 — STRATEGIC RESOLUTION: VICTORY PATHS

> All seven faction-specific paths to victory plus universal/co-victory architecture.

### 14.1 Universal architecture
| Term | Definition | Source |
|------|------------|--------|
| Universal Victory Condition — Peninsular Sovereignty | All-factions baseline win-state. | victory §0 |
| Peninsular Partition (Co-Victory — Alliance-Stalemate) | Multi-faction shared-win procedure (ED-304). | victory §0.1 |
| Accord System | Population-faction commitment dynamic. | victory §0.2, military_layer §4.1 |
| Turmoil Counter | World-pressure track gating victory triggers. | victory §0.3 |
| Battle Consequences | Cross-victory battle-outcome impact. | victory §0.4 |
| Faction Acquisition Toolkits | Per-faction kits for territorial gain/loss. | victory §0.5 |
| Provincial Value (PV) | Per-territory worth toward Peninsular Sovereignty. | victory §1 |
| Piety Track (PT) | Per-territory orthodoxy track (Solmund-side). | victory §2 |
| Starting Piety Track Values | Per-territory PT init (ED-677, PP-652). | victory §0.4 |

### 14.2 Faction strategies (granular)
| Faction | Path | Definition | Source |
|---------|------|------------|--------|
| Crown | Peninsula Sovereignty | Direct universal-condition path. | victory §3.1 |
| Crown | Strategic Milestone — Dominion | Mid-path milestone. | victory §3.1 |
| Church of Solmund | Solmundan Orthodoxy | Religious-supremacy path. | victory §3.2 |
| Church of Solmund | Mass Seizure Declaration | At CI=100. | victory §3.2 |
| Church of Solmund | Strategic Milestone — Altonian Theocracy Path | Alt path. | victory §3.2 |
| Church of Solmund | Partition — Church + Hafenmark | Co-victory pairing (ED-304). | victory §3.2 |
| Hafenmark | Dynastic Assertion (Primary) | Hafenmark primary path. | victory §3.3 |
| Hafenmark | Dynastic Assertion (Alternate, ED-307) | Baralta cadet branch. | victory §3.3 |
| Varfell | Path A — Intelligence Hegemony | (PP-663 revised; VTM row struck.) | victory §3.4 |
| Varfell | Path B — Southernmost Dominion | Southern-conquest path. | victory §3.4 |
| Varfell | Path C — Thread Supremacy | **STRUCK PP-663, 2026-04-19.** | victory §3.4 |
| Restoration Movement | Cultural Revolution (5 players, hardest mode) | Phase 1 + Phase 2. | victory §3.5 |
| Restoration Movement | Phase 1 — Cultural Majority | Threshold to unlock Phase 2. | victory §3.5 |
| Restoration Movement | Phase 2 — Cultural Uprising of T9 Himmelenger | Final-phase trigger. | victory §3.5 |
| Restoration Movement | RM Territory Control — Cultural Displacement | Gradual control mechanism. | victory §3.5 |
| Restoration Movement | Presence Marker Mechanics | Marker-token system (ED-589). | victory §3.5 |
| Löwenritter | Military Regency — Regency Establishment | Post-coup activation. | victory §3.6 |
| Löwenritter | Elske Loyalty Track | Loyalty-conditional clock (ED-624). | victory §3.6 |
| Löwenritter | Military Consolidation (Alternate) | Alt-victory path. | victory §3.6 |
| Löwenritter | Post-Coup Succession Rule (ED-674) | Succession after coup. | victory §3.6a |

### 14.3 Co-Victory and World-State Transitions
| Term | Definition | Source |
|------|------------|--------|
| Co-Victory Pairings | Allowed multi-faction shared wins. | victory §4 |
| Total Domination (ED-318) | Single-faction total-control alt. | victory §5 |
| World-State Transition | Mid-game state change altering victory landscape. | victory §5 |
| RS=0 → Post-Calamity Era | World-state transition (now MS=0). | victory §5.1 |
| IP=100 → Phased Occupation Era | Altonian-occupation triggered transition. | victory §5.2 |
| All Factions Dissolved → Anarchy Era | Total-collapse transition. | victory §5.3 |
| The Rupture Scene (ED-630) | Cinematic moment at MS=0. | victory §5.3 |
| Askeheim and RS (BALANCE-004) | Askeheim's role in MS pacing. | victory §6 |
| CI Generation and Church Seizure | Cross-link to CI track. | victory §7 |
| RM Founding Mechanic (ED-620) | RM-faction-creation rule. | victory §8 |
| Win Probability Assessment | Balance verification per faction (BALANCE-001). | victory §10 |

### 14.4 Hybrid integration
| Term | Definition | Source |
|------|------------|--------|
| PT State Transfer (Hybrid) | Carries PT across mode boundaries. | victory §9.1 |
| Victory Condition Check (Hybrid) | Trigger evaluation in Hybrid. | victory §9.2 |
| Hybrid Victory and P-32 | Hybrid-victory canonical patch. | victory §9.3 |
| Domain Echo Autonomous Resolution (ED-300) | Auto-resolve Echos in Hybrid. | victory §9.4 |

---
## SILO 15 — SCALE-BRIDGING (Personal ↔ Scene ↔ Faction ↔ Mass)

> Cross-system handoff vocabulary. These terms describe HOW resolution flows between scales — they're *bridge* mechanics, not in-system mechanics.

### 15.1 Three-mode architecture
| Term | Definition | Source |
|------|------------|--------|
| Three-Mode Architecture | TTRPG · Board Game · Hybrid. | scale_transitions §1 |
| Scale Table | Reference table of scales. | scale_transitions §2 |
| TTRPG (mode) | Tabletop RPG mode. | alias_registry |
| Board Game (BG, mode) | Pure board-game mode. | alias_registry |
| Hybrid (HYB, mode) | Combined mode. *HYB not permitted alone in prose.* | alias_registry |

### 15.2 The Eight Handoff Rules (granular)
| # | Handoff | Source |
|---|---------|--------|
| §3.1 | **Personal → Thread** — actor enters Thread contact via Leap | scale_transitions §3.1 |
| §3.2 | **Personal → Faction** — personal action triggers strategic-layer effect | scale_transitions §3.2 |
| §3.3 | **Personal → Scene (Contest)** — personal interaction escalates into a contest | scale_transitions §3.3 |
| §3.4 | **Scene → Faction (Domain Echo)** — decisive scene outcome triggers faction-layer effect | scale_transitions §3.4 |
| §3.5 | **Thread → Faction** — Thread op effects propagate to strategic layer | scale_transitions §3.5 |
| §3.6 | **Thread → Mass (Mass Battle Integration)** — Thread ops in Mass Battle | scale_transitions §3.6 |
| §3.7 | **Mass → Personal (General Duel)** — Mass-Battle resolution invokes personal duel | scale_transitions §3.7 |
| §3.8 | **Scene → Mass** — scene outcome alters mass-battle conditions | scale_transitions §3.8 |
| §3.9 | **Fieldwork ↔ All Systems** — fieldwork serves as cross-system connector | scale_transitions §3.9 |

### 15.3 Zoom In / Zoom Out
| Term | Definition | Source |
|------|------------|--------|
| Zoom In | Mode/scale shift down (BG → Hybrid → TTRPG). | scale_transitions §4.1 |
| Zoom Out | Mode/scale shift up (TTRPG → Hybrid → BG). | scale_transitions §4.2 |
| Zoom In Triggers (PP-556) | Conditions warranting Zoom In. | scale_transitions §4.3 |
| Arc-Specific Zoom In Triggers | Existing per-arc triggers. | scale_transitions §4.3.1 |
| Mandatory Zoom In Triggers | Cannot be declined. | scale_transitions §4.3.2 |
| World-State Zoom In Triggers | Scene Slate Priority 1 triggers. | scale_transitions §4.3.3 |
| "Where Were You?" — Retrospective Scene Generation | Mid-game retrospective scene insertion. | scale_transitions §4.4 |

### 15.4 Domain Echo (cross-listed §11)
| Term | Definition | Source |
|------|------------|--------|
| Domain Echo (the mechanic) | Faction-layer consequence from personal/scene-level outcomes. | scale_transitions §5 |
| Domain Echo Trigger | Conditions that fire an Echo. | scale_transitions §5.1 |
| Domain Echo Amount | Magnitude of an Echo. | scale_transitions §5.2 |
| Domain Echo Timing by Mode | When Echos resolve per mode. | scale_transitions §5.3 |
| Debate → Domain Echo (PP-108) | Decisive debate result → Echo. | scale_transitions §5.4 |
| Accord Domain Echo | Accord-derived Echo (peninsular_strain_v1). | scale_transitions §5.5 |
| Thread Domain Echo (ED-673) | Thread-op-derived Echo. | scale_transitions §5.6 |

### 15.5 Mode transition procedures
| Term | Definition | Source |
|------|------------|--------|
| TTRPG → BG (Session Boundary) | End-of-session mode shift. | scale_transitions §6.1 |
| BG → Hybrid (Mid-Game Zoom In) | Mid-game zoom-in into Hybrid. | scale_transitions §6.2 |
| Hybrid → TTRPG (Zoom Out) | Hybrid-to-TTRPG transition. | scale_transitions §6.3 |
| Coherence Initialization (PP-200) | Coherence values on mode entry. | scale_transitions §6.4 |
| Hybrid Coherence Cost (PP-198) | Coherence-cost rule for Hybrid mode. | scale_transitions §6.5 |

### 15.6 Sufficient Scope and Register Shift
| Term | Definition | Source |
|------|------------|--------|
| Sufficient Scope — Register Shift Trigger | Scope-threshold trigger for register shift. | scale_transitions §7 |
| Scope Shift Rules | Rules governing scope transitions. | scale_transitions §8 |
| PC Faction Embedding (ED-075) | PC's faction-affiliation in BG/Hybrid. | scale_transitions §9 |
| Thread Timing in Hybrid (PP-125, PP-260) | When Thread ops resolve in Hybrid. | scale_transitions §10 |
| Contested Figure System (ED-167, ED-168) | NPC-disposition tracking across modes. | scale_transitions §11 |

---
## SILO 16 — DICE ENGINE + AUTHORING/INFRASTRUCTURE

> Two related but distinct silos consolidated for compactness:
> **A — Dice Engine:** universal resolution primitives. These terms are NOT system-specific — every system (combat, debate, fieldwork, threadwork, mass combat) consumes them.
> **B — Authoring / Infrastructure:** meta-layer terms about the design process itself, not in-game.

---

## 16.A — DICE ENGINE (system-agnostic resolution primitives)

| Term | Abbr | Range / Values | Definition | Source |
|------|------|----------------|------------|--------|
| Target Number | TN | 6 / 7 / 8 | Per-die success threshold. **Standalone abbreviation permitted.** | params/core, alias_registry |
| Obstacle | Ob | integer | Net successes required for success. **Standalone abbreviation permitted.** | params/core |
| Pool | — | dice count | Pre-roll dice pool, system-specific composition. | params/core |
| Net Successes | — | integer | Successes minus opposing successes (in opposed). | params/core |
| Expected Value | EV | float | Statistical helper for design analysis. | params/core |
| Degree of Success | — | enum | Outcome banding for any roll. | params/core |
| **Overwhelming** (degree) | — | TTRPG: ≥ 2× Ob AND ≥ 3 min (PP-232); BG: ≥ Ob+1 (provisional) | Highest success band. | alias_registry |
| **Success** (degree) | — | net ≥ Ob | Standard success. | alias_registry |
| **Partial** (degree) | — | 0 < net < Ob | Mixed-result band. | alias_registry |
| **Failure** (degree) | — | net = 0 | No-success band. | alias_registry |
| Roll | — | (verb) | Generic dice action. | universal |
| Pool Composition Rules | — | per-system | Per-system rules on what dice belong in a pool. | params/core |

> Combat/Debate/Fieldwork all use these primitives but apply them via *system-specific* outcome tables (Combat Degree Table, Contest Composure resolution, Investigation Evidence Quality, etc.). The *primitives* are siloed here; the *applications* are siloed in their respective system silo.

---

## 16.B — AUTHORING / INFRASTRUCTURE (meta — not in-game)

| Term | Abbr | Definition | Source |
|------|------|------------|--------|
| Patch | PP-NNN, PP | Numbered design-patch identifier. **Standalone abbreviation permitted.** | alias_registry |
| Editorial Decision | ED-NNN, ED | Numbered editorial-decision identifier. **Standalone abbreviation permitted.** | alias_registry |
| Simulation Identifier | SIM-NNN | Numbered simulation-run identifier. | alias_registry |
| Simulation Debt | SIM-DEBT-NNN | Tracked simulation-coverage gap. | alias_registry |
| Game Master | GM | Tabletop facilitator role. **Engine-resolution model is canonical; GM-resolution is legacy.** | alias_registry |
| Engine Setup / Resolution | — | Canonical replacement for "GM setup / resolution." | (cross-cutting) |
| Player Character | PC | Player-controlled character. | alias_registry |
| Non-Player Character | NPC | Engine-controlled character. | alias_registry |
| Burning Wheel | BW | Design precedent (Burning Wheel RPG). | alias_registry |
| Behaviour Tree | — | NPC AI architecture model. | npc_behavior |
| Stage 10 (sim) | — | Specific simulation stage gate. | (cross-cutting) |
| Class A canonical | — | Highest-tier authority document. | (canonical_sources) |
| Class B canonical | — | Secondary-tier doc; can be modified by Class A. | (canonical_sources) |
| Throughline | T-NN | Cross-system narrative throughline tag. | throughlines_meta |
| Censured Vocabulary | — | Banned-token registry. | references/censured_vocabulary |
| Alias Registry | — | Canonical-name + alias mapping. | references/alias_registry |
| Glossary | — | Master mechanical-term glossary. | references/glossary |
| Values Master | — | All-numeric-values registry (~464 values). | references/values_master |
| Numeric Bounds Report | — | Pre-flight bounds-check on all numeric values. | references/numeric_bounds_report |
| Design Registry | — | Active-design-doc inventory. | references/design_registry |
| Proper Noun Registry | — | World-entity (people/places) registry. | references/proper_noun_registry |
| Canonical Sources | — | System → doc-path map. | references/canonical_sources |
| File Index Summary | — | Sparse repo-tree summary. | references/file_index_summary |
| Supersession Register | — | History of superseded design entries. | registers/supersession_register |
| Patch Register (in victory_v30) | — | Per-doc patch log. | victory §12 |
| Sign-off Block (PP-674 Vetting) | — | Stage-gate sign-off schema. | (PP-674) |
| Stage Gates | — | Sequential design-progression gates. | (cross-cutting) |

---

# PART TWO — DIAGNOSTIC REGISTERS

## §2 — CROSS-SILO OVERLAP MATRIX

> The vocabulary problem in three classes:
> - **INTENTIONAL POLYSEMY** — same word, different applications, by deliberate design (e.g., the same Conviction name appears at character AND faction scale because aggregation is the point).
> - **ACCIDENTAL DUPLICATE** — same word, different mechanics, by drift. Rename candidate.
> - **WORD-CLASS VIOLATION** — attribute-word used as mechanic-word, OR mechanic-word used as attribute-word. **This is the rule Jordan called out.** Rename mandatory.
>
> Words appearing in 4+ silos that are *generic English* (Roll, Pool, Action, Type, Value, Stat, Stage, Outcome, Failure, Success, Partial, Overwhelming, Degree) are dice-engine primitives and the polysemy is structural — flagged here for completeness only.

### §2.1 INTENTIONAL POLYSEMY (no rename needed)

| Word | Silos where it appears | Verdict + rationale |
|------|------------------------|----------------------|
| **Composure** | §1 character stat (derived) · §6 debate damage track · §16 (dice engine, indirectly) | INTENTIONAL — debate-system damage track *is* the character's Composure stat being attacked. Same noun, same referent. Glossary cross-lists it. **Keep.** |
| **Coherence** | §1 character stat · §4 cosmological state · §7 threadwork track | INTENTIONAL — Coherence is one concept (rendering integrity) examined at three scales (personal stat, cosmological substrate, in-operation track). **Keep.** |
| **Mending Stability (MS)** | §4 world-cosmological · §7 threadwork · §12 clocks · §14 victory | INTENTIONAL — MS is the canonical world-clock; every system that touches it cross-references the same value. **Keep.** |
| **Truth** | §1 character stat · §4 solmund-world | INTENTIONAL — Truth is the cosmology-orthodoxy stat; its definition is rooted in §4 even though it lives on the character sheet. **Keep.** |
| **~~Conviction Track / CV~~** | §9 (per-territory) · §12 clocks · §14 victory · §6 debate | **NO LONGER KEPT.** Renamed: territory = Piety Track (PT); contest = Persuasion Track. "Conviction" is a §1 attribute word — silo contamination. |
| **The 13 Conviction names** (Faith, Authority, Order, Scholastic, Utility, Equity, Liberty, Precedent, Community, Identity, Warden, Virtue, Honor) | §1 character attributes · §2 faction attributes (via faction Cascade) | INTENTIONAL — same Conviction set at personal and faction scale (per conviction_taxonomy §1). **Keep but FLAG for §3 collision audit:** a Conviction name appearing as a *mechanic verb* would be a violation. None currently do. |
| **Domain Echo** | §6 debate (bridge out) · §10 mass combat (bridge out) · §11 faction layer · §15 scale-bridging | INTENTIONAL — Domain Echo is the canonical *bridge mechanism*; every personal-scale system that can trigger it cross-references the same primitive. **Keep.** |
| **Knot** | §1 character (relationships) · §4 cosmological (Knot Formation during Leap) · §7 threadwork (Knot Strain) · §15 scale-bridging | INTENTIONAL — Knot is *one concept* (relational lock) treated at three depths: personal-relationship Knots, cosmological-Leap Knots, threadwork Knot-Strain. Glossary acknowledges. **Keep.** |
| **Disposition** | §1 character (NPC attribute) · §8 fieldwork (Disposition Track mechanic) | BORDERLINE INTENTIONAL — Disposition is a noun describing NPC state; the Track is the *mechanic* that operates on it. Different ontological registers. **Acceptable as-is per glossary note (PP-691) but worth a callout:** when used in mechanics writing, distinguish *NPC's disposition* (state) from *Disposition Track* (mechanic operating on it). |
| **Standing** | §2 faction attribute · §4 (state.standing_change Key type) | INTENTIONAL — Standing is a faction attribute; the Key type names the change-event, which is correct. **Keep.** |

### §2.2 ACCIDENTAL DUPLICATES (rename candidates — these are real bugs)

| Word | Silos / locations | Problem | Recommendation |
|------|-------------------|---------|----------------|
| **Cardinal** | §2 faction attributes (Church Cardinal NPC role) · NPC-roster terminology · BG strategic context (the Four-Cardinal Structure) | Two separate uses: (a) Church Cardinal as named NPC role, (b) Cardinal as cardinal-virtues structural-frame. Resolved if "Cardinal" is exclusively the NPC role and the structural frame is renamed (e.g., "Four-Virtue Structure"). **Recommend rename of structural frame.** |
| **Authority** | §1 (Conviction #2) · §6 (debate Pressure Point Type — **RENAMED to Sanction**) · §2 (faction-attribute parlance, adjacent to Mandate) | ~~Three uses, one deliberate (Conviction). Authority-as-Pressure-Point-type uses the Conviction's English root, but mechanically "Authority" the Pressure Point is *not* the Conviction.~~ **RESOLVED: Pressure Point renamed to "Sanction" in params/contest.md. Remaining uses (Conviction #2, faction-attribute parlance) are non-colliding.** |
| **Equity / Order / Precedent / Continuity / Honor** | §1 (Convictions #6/3/8/legacy/13) · debate argument-style classifiers (Citation = Precedent + Revealing; etc.) | The four Contest Style names (Citation/Vision/Suppression/Knot-required) **already use rename-from-Conviction** so this is mostly clean. But internally in contest §4 and faction_behavior §3.7, these Conviction labels are repeated for argumentation context with no clear Style mapping. **Audit recommendation:** every place a Conviction word appears in a mechanic context, add inline cross-reference to the §1 Conviction definition. |
| **Continuity** | §1 (LEGACY Conviction tag) · §2 (faction-attribute legacy framework) | LEGACY-only collision; both deprecated PP-684. **Continue using new 13-Conviction names; flag any active-doc "Continuity" references for sweep.** |
| **Categorical Imperative / Faith** | §1 (LEGACY) · §2 (faction-ethical-framework legacy) | Both replaced by 13-Conviction taxonomy. **Sweep all active docs.** |
| **TC** (abbreviation) | LEGACY: §12 clock for "Theocracy Counter" · §6 debate "Conviction Track" | RESOLVED at term level (TC no longer used; CI = Church Influence; CT = Conviction Track). **Corpus residuals exist** (npc_behavior swept; mass_battle, throughlines_meta_infill, npc_character_analyses queued). Continue sweep. |
| **CP** (abbreviation) | §1 (Character Points, current) · §10 (Combat Power, renamed to Power) | RESOLVED: ED-136 locks CP to Character Points; CP = Combat Power deprecated. **Sweep complete per alias_registry.** |
| **TD** (abbreviation) | §1 (Thread Depth, REMOVED PP-166) · Mermaid `flowchart TD` (top-down syntax) | RESOLVED: Thread Depth phantom; never appeared in docs. **No action needed.** |
| **COMP** (abbreviation) | §6 debate Composure · COMP general English | RESOLVED: write "Composure" in full; COMP not standalone. |

### §2.3 WORD-CLASS VIOLATIONS (the rule: attribute words ≠ mechanic words)

> **Jordan's stated rule:** "character and faction characteristics shouldn't have any overlap with mechanics in word choice." This section is the audit against that rule.

#### §2.3.1 CHARACTER-attribute words used as mechanic words
| Attribute word (§1) | Used as mechanic in | Verdict |
|---------------------|---------------------|---------|
| Strength | Combat min-requirement (mechanic). Mass-combat unit stat **renamed to Size** (PP-232). | RESOLVED for unit-level. **Personal-combat Strength used both as character stat AND as weapon-min-requirement** — borderline; arguably the mechanic *checks* the stat rather than *being* it. **Acceptable** (the character stat IS the mechanic's input). |
| Agility | Combat Pool driver. | OK — same pattern: stat → pool. |
| Endurance | Health, Stamina derivation. | OK — same pattern. |
| Presence | Argue Pool driver, Command formula input. | OK — same pattern. |
| Cognition | Command formula input, Investigation pool driver. | OK — same pattern. |
| Spirit | Thread Pool eligibility input. | OK — same pattern. |
| Attunement | Fieldwork pool driver. | OK — same pattern. |

> **Verdict on character attributes:** the 7 core attributes are used as *inputs to* mechanics, not *as* mechanics. This is the correct word-class separation. **No violations.**

#### §2.3.2 FACTION-attribute words used as mechanic words
| Attribute word (§2) | Used as mechanic in | Verdict |
|---------------------|---------------------|---------|
| **Mandate** | "Mandate Pool" appears in faction-Domain-Action contexts. Faction stat Mandate is the *driver* of the pool, but the pool name shares the noun. | BORDERLINE VIOLATION. **Recommend renaming the pool to "Faction Pool" (already used in some places) or "Political Pool" (used in ci_political §3.4, §7.2)** to avoid Mandate-the-stat being conflated with Mandate-the-pool. The alias_registry's `faction_pool` / `political_pool` is correct; ensure all use is collapsed to one. |
| **Influence** | Used as mechanical phrase "X exerts Influence" in some docs. | OK — verb-use of the noun, not a mechanic NAMED Influence. |
| **Wealth** | "Wealth Zero Consequence" — mechanic name. The mechanic is *about* the stat reaching 0 but the mechanic's name uses the stat noun. | OK — naming convention is fine; reads as "the consequence of Wealth being zero." |
| **Military** | "Military Layer" (a doc title), "Military Stat → Unit Power Ceiling" (a rule). The doc title and rule both use the stat noun. | BORDERLINE — Military as faction-stat is the driver; the doc and rule are *about* it. Acceptable. **However:** if the project ever names a generic "Military action" verb, that would be a violation. Currently there is none. |
| **Intel** | "Intel" the stat, "intelligence work" the activity. | OK — different word forms (noun vs activity-noun); not collision. |
| **Stability** | "Stability Triggers" — mechanic-naming uses the stat noun. | BORDERLINE — same pattern as Wealth Zero Consequence. Acceptable: mechanic is *about* Stability changing. **However:** "Stability Recovery," "Accounting Stability Check," "Stability Triggers" all mention Stability — verify these collectively don't overload the noun. Current usage is consistent. |
| **Standing** | "Standing change" Key type. | OK — naming convention. |

> **Verdict on faction attributes:** Mandate Pool / Faction Pool / Political Pool naming is the only real concern. **One soft violation; rename recommended.**

#### §2.3.3 TERRITORY-attribute words used as mechanic words
| Attribute word (§3) | Used as mechanic in | Verdict |
|---------------------|---------------------|---------|
| **Provincial Value (PV)** | Used as input to Spiritual Weight (which is repurposed PV). | OK — naming consistent. |
| **Piety Track (PT)** | The track and the attribute share name. | OK — same pattern as Stability. |
| **~~Conviction Track (CV)~~** | Renamed to Piety Track (PT). No longer polysemous. | **RESOLVED** |
| **Spiritual Weight** | Repurposed PV; used as CI generation input. | OK |
| **Temperament** | Per-territory attribute; used as input to populace-response computation. | OK |
| **Accord** | Per-territory attribute; "Accord Domain Echo" mechanic uses the noun. | OK — same pattern. |

> **Verdict on territory attributes:** clean. No violations.

### §2.4 GENERIC ENGLISH WORDS (structurally polysemous — for awareness only)

These words appear across many silos because they are dice-engine or natural-language primitives:

| Word | Silos | Note |
|------|-------|------|
| Action | §5, §6, §7, §8, §11 | Generic. **"Domain Action" is the strategic-layer specifier;** elsewhere "action" is just a verb. |
| Roll | §5, §6, §7, §8, §10, §16 | Dice primitive. |
| Pool | §5, §6, §7, §8, §10, §11, §16 | Dice primitive. |
| Stat | §1, §2, §3, §10 | Word-class category, not a mechanic. |
| Type | §4, §5, §6, §10, §15 | Used in compound names (Interaction Type, Formation Type, Key Type). |
| Outcome | §6, §11, §15 | Dice primitive. |
| Failure / Success / Partial / Overwhelming / Degree | §5, §6, §7, §8, §10, §16 | Dice-engine outcomes. **Universal — appears in every system.** |
| Pool | §5, §6, §7, §8, §10, §11 | Dice primitive. |
| Stage | §11, §13, §16 | Authoring meta or BG phase reference. |
| Phase | §10, §11 | BG turn-structure unit. |
| Value | §1, §2, §3, §4, §16 | Generic. |

---
## §3 — ATTRIBUTE ↔ MECHANIC COLLISION REGISTER

> Per Jordan's rule: **"character and faction characteristics shouldn't have any overlap with mechanics in word choice."**
>
> This register is the single-place audit. §2 surfaced the candidates; §3 makes the verdict explicit and lists rename actions.

### §3.1 The rule's three valid patterns
A character/faction/territory attribute word may appear in mechanic context if and only if it follows one of:
1. **Stat-as-input pattern** — the mechanic *consumes* the stat (e.g., "Combat Pool = Agility + Strength + dice"). The attribute is an *input*, not the mechanic's name.
2. **State-change-naming pattern** — the mechanic NAMED after the stat *changes the stat* (e.g., "Stability Recovery" recovers Stability; "Wealth Zero Consequence" triggers when Wealth = 0). The mechanic NAME is grammatical: the attribute is the SUBJECT or LOCATION of the change, not the verb.
3. **Aggregation-cross-scale pattern** — the same noun applies at multiple scales by deliberate design (e.g., Conviction at character + faction; Coherence at character + cosmological). Documented in §2.1.

Anything else is a violation requiring rename.

### §3.2 Active violations (rename required)

| Violation | Severity | Why it's a violation | Rename target |
|-----------|----------|----------------------|---------------|
| **"Mandate Pool"** as a strategic-layer pool name (when "Faction Pool" or "Political Pool" is also in use) | LOW | The faction stat *Mandate* drives a pool that shares its name. Pattern 2 (State-change-naming) doesn't apply because the pool is not *changing* Mandate, it's *spending dice driven by* Mandate. Risks reading "Mandate Pool" as "Mandate ATTRIBUTE = Mandate POOL." | Use **"Political Pool"** (already canonical in `ci_political_v30 §3.4, §7.2`). Verify all other docs collapse to single name. |
| **"~~Authority~~Sanction"** as Pressure Point Type (§6). *Renamed in params/contest.md this session.* | MEDIUM → **DONE** | The Conviction word was used as a debate-Pressure-Point-Type label. Pattern 1 (input) doesn't apply — the Pressure Point isn't checking the Conviction; it's a *style of argument.* | ~~Rename Pressure Point Type to **"Sanction"** or **"Authority Citation"**.~~ **DONE: renamed to Sanction in params/contest.md.** |
| **"Cardinal"** as NPC role AND structural frame ("Four-Cardinal Structure" of Church Convictions) | LOW | The named NPCs *are* called Cardinals (proper noun). The structural frame uses "Cardinal" generically (cardinal virtues). Risk: reader can't distinguish "the Cardinals voted" (NPCs) from "the Cardinal Structure determined" (frame). | Rename structural frame to **"Four-Virtue Structure"** or **"Quadrennial Frame"**. Reserve "Cardinal" for the NPC role. |

### §3.3 Borderline cases (audit to confirm, no rename yet)

| Term | Why borderline | Audit question |
|------|----------------|----------------|
| **"Stability Triggers"** | Names the trigger BY the stat it threatens (Pattern 2). Acceptable but the *Stability* noun appears in: Stability stat, Stability Triggers, Stability Recovery, Accounting Stability Check, Faction Collapse Exit Procedure (Stability=0). | Audit: is Stability ever *not* the subject of these mechanics? If yes, rename that case. Currently all five are about Stability changing. **CLEAN.** |
| **"Wealth Zero Consequence"** | Pattern 2. | Same audit. **CLEAN.** |
| **"Military Layer"** as a doc title | The doc is *about* the Military stat's strategic layer. Pattern 2-adjacent. | Audit: is the doc title ever shortened to just "Military"? If yes, that's a violation. **CLEAN per current usage.** |
| **"Disposition Track"** (§8 fieldwork) vs Disposition (NPC attribute) | Glossary acknowledges (PP-691). The mechanism is the *Track* (a clock-like construct); the attribute is *Disposition* (a state). | Audit: when prose says "Disposition" alone, does it mean the state or the Track? **Usage is currently consistent — state context vs mechanic context.** Worth a one-sentence glossary note. |
| **The 13 Conviction names appearing as debate Contest Style names** (Citation/Vision/Suppression/Knot-required) | The Style names ARE renamed from Convictions, so this is already mitigated. | Audit: anywhere a Conviction word appears in debate context outside the Style framework, ensure it's clearly the Conviction. **Mostly clean per spot-check; full text sweep recommended.** |

### §3.4 Compliant patterns (these pass the rule)

| Term | Pattern | Why compliant |
|------|---------|---------------|
| Combat Pool, Argue Pool, Fieldwork Pool, Thread Pool | Pattern 1 (stat-as-input) | Pool names use the *system* not the attribute. Drivers are attributes; pool names are not attributes. |
| Combat Endurance (CE) | Pattern 1 | Endurance is the stat; CE is the mechanic. Naming makes the role clear. |
| Health per Size (H), Total Health | Pattern 1 | Health/Size are mass-combat-renamed terms; the formulas use them as inputs. |
| ~~Conviction Track (CV)~~ → Piety Track (PT) | ~~Pattern 3~~ | **Renamed.** "Conviction" removed from track name — §1 attribute word. PT is scale-neutral name. |
| The 13 Convictions appearing at faction scale | Pattern 3 | Per faction_behavior §3.2 Cascade math. Documented intentional. |
| Coherence (personal stat + threadwork track + cosmological substrate) | Pattern 3 | Documented intentional in foundations canon. |

### §3.5 Summary of recommended rename actions

1. **Rename Mandate Pool → Political Pool** wherever it persists; verify consolidation. **Priority: low (cleanliness). STATUS: DONE — ci_political_v30 already canonical at "Political Pool" (§3.4). Only remaining occurrence is the comparison header §7.2, which is appropriate.**
2. **Rename Pressure Point "Authority" → Sanction** (or "Authority Citation"). **Priority: medium (real polysemy with Conviction). STATUS: DONE — renamed to "Sanction" in params/contest.md this session.**
3. **Rename "Four-Cardinal Structure" → Four-Virtue Structure** (or similar). **Priority: low. STATUS: OPEN — 12+ active files; requires dedicated sweep.**
4. **Audit sweep: any active-doc occurrence of "Categorical Imperative", "Faith", "Virtue", "Scholastic", "Equity", "Continuity (legacy)", "Reason (legacy)"** → replace with appropriate 13-Conviction names. **Priority: medium (legacy cleanup). STATUS: OPEN — 30+ active files affected; see corpus_fix_manifest.md.**
5. **Add inline cross-reference** anywhere a Conviction word appears in mechanic context to §1.5 definition. **Priority: low (documentation hygiene). STATUS: OPEN — requires full text sweep.**

---
## §4 — SYNONYM REGISTER (different words, same concept — unification candidates)

> Where the corpus uses two different words for the same mechanical concept, this register captures both with the canonical winner marked.

| Concept | Canonical | Aliases / Synonyms | Source |
|---------|-----------|---------------------|--------|
| World rendering-stability clock | **Mending Stability (MS)** | Rendering Stability (RS) | ED-731. Historical RS retained only in canon/02 annotations by intentional design. |
| Church-faction's institutional reach | **Church Influence (CI)** | Theocracy Counter (TC) | ED-782. TC retained in alias_registry collision_table; corpus residuals queued. |
| Mass-combat unit-size stat | **Size** | Strength (legacy) | PP-232. |
| Mass-combat offensive stat | **Power** | Combat Power (CP, legacy) | PP-232. ED-136 locks CP to Character Points. |
| Mass-combat defensive coherence stat | **Discipline** | Cohesion (legacy) | PP-232. |
| Mass-combat command stat | **Command** | Command Rating (CR, legacy) | PP-232. |
| Substrate event-record | **Key** | EventImpact (legacy) | PP-687. |
| Per-NPC remembered Key reference | **Memory entry** | Memory record, Memory schema (legacy) | PP-687. |
| Thread-contact action-economy resource | **Thread Fatigue** | Contact Rounds (legacy) | ED-694. |
| Wound-track survival resource (combat) | **Vitality** | Health (legacy in combat context) | ED-548 + ED-694. **Note:** Health is still used as the universal name (the personal stat); Vitality is the *combat-instance* of it. |
| Action-card faction-strategic system | **Card Hands** + **Card → Action Mapping** + **Cooldown Track** | Various legacy formulations of "card system" | PP-177 unified. |
| Faction-strategic ethical-framework modifier | **Mission + Cascade + Public Expectation triadic decomposition** | Ethical Framework Modifier (legacy) | PP-686 / SUPERSESSION-PP686-001. |
| Conviction taxonomy | **The 13 Convictions** (PP-684) | Categorical Imperative · Virtue · Faith · Scholastic · Equity · Honor · Reason (legacy) · Continuity (legacy) | PP-684. |
| Engine-resolution model | **Engine Setup / Resolution** | GM Setup / Resolution (legacy in always-already canon context) | canon/01 (consciousness-performed rendering). |
| TTRPG mode | **Tabletop Roleplaying Game (TTRPG)** | (none) | alias_registry. |
| Hybrid mode (full term) | **Hybrid (HYB)** | (none — HYB never standalone) | alias_registry. |
| BG mode | **Board Game (BG)** | (none) | alias_registry. |
| World-track for Solmund-orthodoxy at territory scale | **Piety Track (PT)** | Conviction Track (CT/CV — legacy abbreviation in some docs) | ED-644 explicitly confirms: "Conviction (PT) here is the same per-territory stat as Piety (PT)." Range is 0–5, NOT 0–10. PT is canonical. **RESOLVED — same track.** |
| ~~Per-territory Solmund-orthodoxy track~~ | ~~**Piety Track (PT)** vs **Conviction Track (CV)**~~ — ~~POTENTIAL DUPLICATION~~ | ~~If PT and CV are the same axis at the same scale, one is redundant.~~ | **RESOLVED per ED-644: they ARE the same track. PT is canonical. CV/CT are legacy abbreviations.** |
| Mass Seizure | **Mass Seizure** (probabilistic, CI ≥ 60) | Old "75-threshold Seizure" (gated, replaced) | ci_political §2.2 — replacement noted in supersession. |

> ~~**One open audit item:** `Piety Track (PT)` vs `Conviction Track (CV)` may be the same per-territory axis at the same scale, or they may be subtly different.~~ **RESOLVED:** ED-644 in conviction_track_v30 confirms PT ≡ CV. Same track, range 0–5, abbreviation PT. "CV" was a legacy abbreviation that drifted. See conviction_track_v30 §1 line 23.

---

## §5 — ORPHAN TERMS (present in design docs, not yet siloed)

> Terms surfaced during extraction that didn't fit cleanly into any silo. Each is a routing decision: which silo should adopt it, or is it a mis-extraction?

| Term | Where seen | Recommended silo | Confidence |
|------|------------|-------------------|------------|
| Companion (Companion Specification) | settlement_layer affects-list | §15 scale-bridging or §11 faction layer | LOW — needs companion_spec doc read |
| Throughline (T1, T2, T3, T7) | settlement_layer, fieldwork, threadwork preambles | §16 authoring/infrastructure | HIGH |
| Stage 6, Stage 6b, Stage 10 (sim) | conviction_taxonomy, articulation, key_substrate | §16 authoring/infrastructure | HIGH |
| Always-Already Self-Rendering | canon/01 | §4 cosmological (added) | DONE |
| 5-typology (temperament) | territory_temperaments §2 | §3 territory attributes (already added) | DONE |
| Class A / Class B canonical | most v30 docs | §16 authoring | HIGH |
| Class B 5th axis (Conviction extension) | conviction_taxonomy §2.2 | §1 character (already noted as deferred) | DONE |
| Co-files (cross-doc updates) | conviction_taxonomy header | §16 authoring | HIGH |
| Approach (Threadwork sub-skill) | threadwork §2.1 (Approach Training) | §7 threadwork (already covered) | DONE |
| Bonded NPC | articulation §2.3 | §1 character (added) | DONE |
| Bonds (attribute, "Bonds attribute cap") | derived_stats §10.1 | §1 character — **added to §1.2 this session** | DONE |
| Heroic Resource Slot | (legacy term in settlement_layer §6.1) | §1 or §2 | LOW (may be deprecated) |
| Stature (Ladder) | settlement_layer §6.1 | §3 territory or §16 (player-progression) | MEDIUM |
| Renown | derived_stats §10.3 (Renown ↔ Derived Value Bridge) | §1 character — **added to §1.2 this session** | DONE |
| Bond (vs Knot) | articulation §2.3 | §1 character — already added (Bond / Bonded NPC) | DONE |
| TroopCount | derived_stats §7 | §10 mass combat — derived value | MEDIUM (extend silo) |
| Settlement Combat Defense Feedback | derived_stats §10.4 | §3 territory or §10 combat | MEDIUM |
| Multiplier Tiers | derived_stats §3 | §16 (engine architecture) | MEDIUM |
| Concern queue / Memory salience indicator / Bonds register | articulation §2.1, §2.2, §2.3 | UI/protagonist-lens — separate sub-silo of §16 | LOW |
| Cross-faction Wing Allocation | settlement_layer §1.4.4 | §3 territory (already added) | DONE |
| Pastoral Assumption | settlement_layer §1.7 | §3 territory (already added) | DONE |
| Niflhel Operative (legacy) | conflict_architecture (Niflhel struck) | §X-deprecated | DONE (in §6) |

> **Routing-decision summary:** ~12 orphans need a silo; ~10 are already covered. ~~**Add Bonds attribute and Renown derived value to §1.2**~~ **DONE: Bonds and Renown added to §1.2 this session (verified via derived_stats_v30 §10.1 and §10.3).**

---

## §6 — DEPRECATED / SUPERSEDED REGISTER

> Terms that were retired. Listed for grep/search purposes — they should NOT appear in active docs.

### §6.1 Renamed (term-level RESOLVED)
| Old | New | Patch |
|-----|-----|-------|
| Theocracy Counter (TC) | Church Influence (CI) | ED-782 |
| Rendering Stability (RS) | Mending Stability (MS) | ED-731 |
| Combat Power (CP) | Power | PP-232 |
| Cohesion | Discipline | PP-232 |
| Strength (mass-combat unit) | Size | PP-232 |
| Command Rating (CR) | Command | PP-232 |
| EventImpact / EventImpact Matrix | Key (substrate) | PP-687 |
| Memory record / Memory schema | Memory entry | PP-687 |
| Contact Rounds | Thread Fatigue | ED-694 |
| Health (combat damage track) | Vitality | ED-548, ED-694 |
| Diagnosis (as separate operation) | Mandatory pre-op read; no roll | ED-134, ED-124 |
| GM resolution (in canon-context) | Engine resolution | canon/01 |

### §6.2 Removed (no replacement)
| Term | Status | Reference |
|------|--------|-----------|
| Thread Depth (TD) | REMOVED — phantom stat; never tracked | PP-166 |
| Piety Domain Action | DISSOLVED | conviction_track_v30 §3 |
| 75-threshold Seizure | REPLACED by Mass Seizure (CI ≥ 60 probabilistic) | ci_political §2 supersession |
| Path C — Thread Supremacy (Varfell) | STRUCK | PP-663 |
| Niflhel as faction | STRUCK; mechanic functions redistributed to settlement-broker | CR-STRIKE-2026-04-19, conflict_architecture |
| Vaynard Thread Mastery (VTM) | STRUCK | PP-663 |
| Cultural Reformation (PP-650) | STRUCK | PP-650 (replaced by PP-685) |
| Co-Movement Card (BG-only ten-card deck) | REPLACED by 18-card deck | threadwork §7.1 |

### §6.3 Deprecated abbreviations (legacy simulator codes)
| Abbreviation | Meaning | Status |
|--------------|---------|--------|
| TLK | Torben Loyalty Clock | DEPRECATED — drain rate undefined (F72 gap) |
| DD | Deniability Debt | DEPRECATED (Niflhel-tied; mechanic functions redistributed). Full term still appears in some docs as "Deniability Debt." |
| FSTAT | Faction Stats (collective) | DEPRECATED — was simulator category code, never an in-game term |

### §6.4 Legacy frameworks (replaced by 13-Conviction taxonomy)
| Legacy label | Replacement |
|---|---|
| Categorical Imperative | One of the 13 Convictions per faction; see conviction_migration_roster |
| Virtue | Virtue (Conviction #12) + Self-Other orientation |
| Faith | Faith (Conviction #1) + Authority (Conviction #2) |
| Scholastic | Scholastic (Conviction #4) |
| Equity | Equity (Conviction #6) |
| Honor | Honor (Conviction #13) |
| Reason (legacy tag) | (per migration roster — varies by character) |
| Continuity (legacy tag) | (per migration roster — varies by character) |
| Ethical Framework Modifier | Mission + Cascade + Public Expectation triadic decomposition (PP-686) |

---

# PART THREE — VERIFICATION + NEXT-STEP ACTIONS

## §V.1 Coverage verification

| Composite | Expected count | Enumerated in this file? |
|-----------|----------------|--------------------------|
| Core Attributes | 7 | YES — §1.1 |
| The 13 Convictions | 13 | YES — §1.5 |
| 4 Conviction axes | 4 | YES — §1.6 |
| Faction Core Stats | 7 | YES — §2.1 |
| Player factions | 7 | YES — §2.3 |
| Provinces (T1-T17) | 17 | YES — §3.2 |
| Settlements | 36 | REFERENCED — §3.3 (registry pointer; full enumeration in settlement_layer §2.1) |
| Temperaments | 5 | YES — §2.6 |
| Coherence-0 outcome bands | 4 | YES — §4.3 |
| Key families | 7 | YES — §4.7 |
| Key Types (total) | 37 | YES — §4.8 |
| Combat actions | 9 | YES — §5.2 |
| Interaction Types (CLASH/AMPLIFY/CROSS/DIVERGE) | 4 | YES — §6.2 |
| Pressure Point types | 4 | YES — §6.4 |
| Thread operation types | 11 | YES — §7.3 |
| Stability Triggers (faction) | 5 | YES — §2.5 |
| Eight Handoff Rules | 8 | YES — §15.2 |
| Articulation Triggers | 10 | (covered in §4 narratively; full enumeration in articulation_layer_v30 §3.1) |
| Mass-combat unit stats (post-PP-232) | 5 | YES — §10.2 |
| CI milestones (40/55/60/65/80/100) | 6 | YES — §12.2 |
| Faction Strategies (paths) | per faction × paths | YES — §14.2 |
| Co-Movement Cards | 15 (TTRPG) / 18 (BG) | YES — §7.6 |

## §V.2 Open audit items surfaced by this exercise

1. **Mandate Pool vs Political Pool consolidation** — ~~verify all docs collapse to *Political Pool*.~~ **RESOLVED: ci_political_v30 §3.4 already canonical at "Political Pool." No active canonical docs use "Mandate Pool" except ci_political §7.2 comparison header (appropriate).** (§3.2 violation, low severity.)
2. **Pressure Point "Authority"** — ~~rename recommended to disambiguate from Conviction.~~ **DONE: renamed to "Sanction" in params/contest.md this session. Also corrected "Loyalty" → "Solidarity" per canonical source.** (§3.2 violation, medium severity.)
3. **"Cardinal" as both NPC role and structural frame** — rename structural frame. **OPEN: 12+ active files use "Four-Cardinal Structure." Requires dedicated sweep cycle. See corpus_fix_manifest.md.** (§3.2 violation, low severity.)
4. **Piety Track (PT) vs Conviction Track (CV)** — ~~verify these are distinct or unify.~~ **RESOLVED: ED-644 in conviction_track_v30 explicitly confirms PT ≡ CV — same track, same abbreviation (PT), range 0–5. "CV" and "0–10" were index errors. §3.1, §4, §9 entries updated.** (§4 synonym register, closed.)
5. **Bonds attribute and Renown derived value** — ~~verify if first-class character properties; add to §1.2 if so.~~ **RESOLVED: both confirmed first-class. Bonds = structural relationship capacity (PP-684, derived_stats §10.1). Renown = governance-linked reputation track (derived_stats §10.3). Added to §1.2.** (§5 orphan, closed.)
6. **Conviction-name appearances in mechanic context** — full sweep recommended; add inline cross-references to §1.5 anywhere a Conviction word is used in a mechanic. **OPEN: requires text sweep of all contest, faction_behavior, and argument-style contexts.** (§3.3, §3.5 #5.)
7. **Legacy ethical-framework labels in active docs** — full sweep for Categorical Imperative, Virtue, Faith, Scholastic, Equity, Honor, "Reason (legacy)", "Continuity (legacy)" → replace per migration roster. **OPEN: 30+ active files affected across params/, systems/npcs/, designs/provincial/, designs/scene/, arcs/. See corpus_fix_manifest.md for full file list.** (§6.4.)
8. **Corpus residual sweep for TC** — ~~npc_behavior swept; remaining 5 paragraphs across throughlines_meta_infill, npc_character_analyses, mass_battle queued.~~ **PARTIALLY RESOLVED: mass_battle_v30 (1 TC→CI), npc_character_analyses_v30_infill (2 TC→CI) fixed this session. throughlines_meta_infill clean (0 hits). Remaining TC residuals exist in 40+ other files (mostly in references/, designs/audit/, and non-canonical docs). See corpus_fix_manifest.md.** (§6.1.)

## §V.3 Recommended commit path

This file is a **proposal**, ~~not yet committed~~. **Partially resolved this session (2026-05-07).** Suggested path:
1. ~~Review and accept the silo taxonomy.~~ **Pending Jordan review.**
2. ~~Ratify the §3 collision register's rename actions (Mandate Pool → Political Pool; Pressure Point Authority → Sanction; Four-Cardinal Structure → Four-Virtue Structure).~~ **Mandate Pool: already consolidated. Authority → Sanction: DONE (params/contest.md). Four-Cardinal: OPEN (sweep needed).**
3. ~~Adopt §4 synonym register as the canonical disambiguation table.~~ **PT vs CV GAP resolved. Register updated.**
4. ~~Schedule sweep cycles for §V.2 #6, #7, #8.~~ **#8 partially swept (3 TC→CI fixes). #6 and #7 require dedicated sessions. See corpus_fix_manifest.md.**
5. Commit this file at `references/mechanical_terms_index.md` as canonical diagnostic-glossary. **Committing this session with fixes applied.**

[GAP: ~~Bonds attribute, Renown~~ — RESOLVED: both added to §1.2 per derived_stats_v30 §10.1/§10.3]
[GAP: ~~PT vs CV duplication question~~ — RESOLVED per ED-644: same track, PT canonical, range 0–5]
[GAP: Four-Cardinal → Four-Virtue rename — 12+ active files, requires dedicated sweep cycle]
[GAP: Legacy ethical-framework labels — 30+ active files, requires dedicated sweep cycle per conviction_migration_roster_v30]
[GAP: TC residuals — ~40 non-canonical files remain; canonical files (mass_battle_v30, npc_character_analyses_v30_infill) fixed this session]
[ASSUMPTION: silos as defined cover all play-systems — basis: corpus walk of canonical_sources.yaml + designs/scene/ + canon/]
[CONFIDENCE: medium-high — diagnostic glossary is comprehensive; 5/8 audit items resolved or partially resolved; 3 remaining require dedicated sweep cycles]
[SELF-AUTHORED — bias risk: I produced this; an independent reviewer might add: (a) test the silo boundaries against actual play scenarios; (b) verify the Conviction-cross-scale claim in §2.1 with player-facing playtesting; (c) check whether the granular Conviction-axis vectors in §1.6 are stable enough to silo or if they're calibration-volatile.]
