# VALORIA — Videogame Mode Specification
## Date: 2026-04-17
## Status: CANONICAL — single-mode extraction reference for Godot implementation
## Scope: Resolves all TTRPG/BG/Hybrid mode-branching decisions into one videogame specification.
## Purpose: The Godot implementer reads this document to know which rules from each design doc apply. No reverse-engineering of three-mode tables required.
## Cross-references: Every system design doc in designs/. Architecture: valoria-game/docs/architecture.md.

---

## §0 — Design Principle

The videogame is a continuous experience at two simultaneous scales:

**Strategic scale** (formerly "Board Game"): Territory map, faction orders, card-hand economy, seasonal accounting, victory conditions, NPC faction AI. The player sees this as a strategic overview — peninsula map, faction stat bars, seasonal phase resolution. Time moves in seasons.

**Personal scale** (formerly "TTRPG"): Character actions, dice-pool resolution, combat, social contests, fieldwork, threadwork. The player sees this as scene-level gameplay — dialogue, investigation, combat encounters, Thread operations. Time moves in scenes within a season.

**The zoom system** connects them. The engine triggers mandatory Zoom In events (scale_transitions_v30 §4.3) that pull the player from strategic to personal scale. The player may also elect personal scenes from the Season Slate (player_agency_v30 §4). Domain Echo (scale_transitions_v30 §3.4) propagates personal-scale outcomes back to strategic scale. There is no mode switch — both scales run simultaneously, and the player navigates between them.

**There is no GM.** All resolution is engine-handled. All NPC behavior follows the AI priority trees (npc_behavior_v30 §8). All ambiguous rulings in the design docs that say "GM decides" must be resolved to deterministic rules or authored content before implementation.

---

## §1 — System-by-System Mode Collapse

### 1.1 Combat (combat_v30.md)

| Rule | Videogame Decision | Source |
|------|-------------------|--------|
| Pool-split offence/defence | **Use.** Core combat mechanic. | combat_v30 §1, §4 |
| Zone-based positioning | **Use.** No grid. Zones: Melee / Reach / Ranged / Out. | combat_v30 §4 |
| Wound/Stamina tracking | **Use.** Per-character. Engine tracks. | combat_v30 §7 |
| Weapon TN matrix | **Use.** Per weapon type × action. | combat_v30 §5 |
| "BG: Unit-based abstraction" | **Discard for personal combat.** Used only in mass battle (see §1.5). | — |
| Initiative (PP-232) | **Use.** Deterministic: higher Attunement + Weapon Speed acts first. | combat_v30 §3 |
| Three-mode framing table (§THREE-MODE) | **Discard.** The videogame has one combat system. Mass combat is a separate container. | — |

**Implementation:** CombatContainer + CombatLogic. VersusResolution mode. All personal attributes active.

### 1.2 Social Contest (social_contest_v30.md)

| Rule | Videogame Decision | Source |
|------|-------------------|--------|
| §§1–9 (TTRPG rules) | **Use in full.** Argue pool, exchange structure, Conviction Track, Composure, styles, preparation, Beliefs integration. | social_contest_v30 §1–§9 |
| §10 (BG Parliamentary Vote) | **Use as strategic-scale resolution.** When Parliament votes occur during seasonal phase, resolve via §10 rules. Player may Zoom In to argue personally (triggers §§1–9 via Hybrid §11). | social_contest_v30 §10 |
| §11 (Hybrid Contest) | **Use.** This IS the videogame's zoom-in contest: BG Parliamentary vote triggers personal-scale debate scene when player participates. | social_contest_v30 §11 |
| Adjudicator types | **Use.** Engine selects adjudicator type based on scene context (Forum, Court, Private, Expert, Panel). | social_contest_v30 §2 |

**Implementation:** DebateContainer + SocialContestLogic. OpposedSimultaneous mode.

### 1.3 Fieldwork (fieldwork_v30.md)

| Rule | Videogame Decision | Source |
|------|-------------------|--------|
| Exploration (Discovery Procedure §3.2) | **Use.** Player navigates POI nodes on territory map. | fieldwork_v30 §3 |
| Investigation (Evidence Track §4.1) | **Use.** Journal UI + Evidence Track progress bar. | fieldwork_v30 §4 |
| Socializing (Disposition + social actions §5) | **Use.** Dialogue system + Disposition meter per NPC. | fieldwork_v30 §5 |
| Survey action (§8.1, BG Consul Inward) | **Use as strategic-scale action.** Player assigns Survey as a faction Domain Action during strategic phase. Engine resolves via Influence pool vs Proximity-derived Ob. | fieldwork_v30 §8.1 |
| BG Social Interaction (§8.3) | **Discard.** Replaced by full personal-scale socializing (§5) accessible via Zoom In. | — |
| Hybrid Fieldwork Procedure (§9.1) | **Use.** This IS the videogame's fieldwork: strategic-phase Survey triggers personal-scale Discovery when player zooms in. | fieldwork_v30 §9 |
| Exposure system (§6) | **Use.** Per-territory Exposure meter. Cover-derived thresholds. | fieldwork_v30 §6 |
| Depth axis | **Authored per-POI.** No GM assignment. Each POI has a fixed Depth value. | fieldwork_v30 Godot column |
| Thread-Read as fieldwork (§4.5) | **Use.** TS ≥ 30 characters can Thread-Read POI for Evidence. Gated to Depth ≥ 4 (P1-16). | fieldwork_v30 §4.5 |

**Implementation:** NarrativeContainer (exploration/investigation). Dialogue system for socializing. Strategic-scale Survey via BoardContainer faction actions.

### 1.4 Threadwork (threadwork_v30.md)

| Rule | Videogame Decision | Source |
|------|-------------------|--------|
| Parts 1–4 (Operations, Coherence, Dissolution Residue, Recovery) | **Use in full.** All personal-scale Thread mechanics. | threadwork_v30 §§1–4 |
| Part 5 (Mending Stability) | **Use.** MS tracked globally. All drain/restoration per ms_budget.md. | threadwork_v30 §5, references/ms_budget.md |
| §5.4 (MS in Board Game) | **Use as strategic-scale MS tracking.** MS changes from strategic-phase Thread orders applied at Accounting. | threadwork_v30 §5.4 |
| §5.5 (MS in Hybrid) | **Use.** Both personal and strategic MS changes unified at Accounting. Seasonal cap ±10 net. | threadwork_v30 §5.5 |
| §7.1 (Board Game Thread Orders) | **Use as strategic-scale Thread actions.** Weave, Mend, Investigate, Harvest are faction-level Domain Actions during strategic phase. | threadwork_v30 §7.1 |
| §7.2 (Hybrid Mode) | **Use.** Coherence declaration rule (PP-198) governs who pays Coherence cost when personal-scale Thread ops affect the strategic layer. | threadwork_v30 §7.2 |
| §7.3 Mode Branching Table | **Collapse to single column.** See §2 below. | — |
| Co-Movement Cards (18) | **Use at strategic scale.** When a strategic-phase Thread order fires, draw a Co-Movement Card. When personal-scale Thread-Read fires during a scene, use Version C (auto-effects). | threadwork_v30 §7.1, §3.2 |
| Lock Chronic Drift | **Engine tracks.** Per-territory MS drift applied automatically at Accounting. | threadwork_v30 §3.3 |
| Coherence | **Use.** Per-practitioner track, 10→0. Engine tracks. | threadwork_v30 §3 |
| "GM tracks" entries | **Engine tracks.** All "Game Master tracks" items become engine-tracked state. | — |

**Implementation:** ThreadworkSystem (RefCounted logic). Personal-scale ops resolve in CombatContainer (P5 Leap) or NarrativeContainer (fieldwork Thread-Read). Strategic-scale ops resolve in BoardContainer faction actions.

### 1.5 Mass Battle (mass_battle_v30.md)

| Rule | Videogame Decision | Source |
|------|-------------------|--------|
| Part A (TTRPG Mass Battle) | **Use.** 6-phase turn structure, unit stats, formations, tactics, commander system. Engine resolves all phases. | mass_battle_v30 Part A |
| Part B (BG Battle Resolution) | **Use as auto-resolve option.** When a battle occurs and the player chooses not to Zoom In, resolve via Part B's simplified formula (Martial pool vs Battle Ob). | mass_battle_v30 Part B |
| §B.5 (Hybrid Handoff) | **Use.** This IS the videogame's battle zoom: strategic-phase battle triggers Part A when player zooms in, Part B when they don't. | mass_battle_v30 §B.5 |
| BG Unit Stats (§B.2) | **Use.** Pre-set on unit tokens. Strategic-scale view shows BG stats; zoomed battle shows full TTRPG stats. | mass_battle_v30 §B.2 |
| Thread in Mass Battle (§A.10) | **Use.** ×3 MS multiplier. Phase 4 timing. | mass_battle_v30 §A.10 |

**Implementation:** BattleContainer + BattleLogic. PhaseLockedSimultaneous mode (zoomed). SoloResolution (auto-resolve).

### 1.6 Scale Transitions (scale_transitions_v30.md)

| Rule | Videogame Decision | Source |
|------|-------------------|--------|
| §1 Three-Mode Architecture | **Collapse.** The videogame runs both scales simultaneously. No "TTRPG mode" vs "BG mode" — there is strategic scale and personal scale, with zoom between them. | — |
| §2 Scale Table | **Use.** Object → Personal → Relational → Territorial → Structural → Foundational. | scale_transitions_v30 §2 |
| §3 Domain Echo | **Use.** Engine evaluates Sufficient Scope after every personal scene and propagates consequences to strategic scale. | scale_transitions_v30 §3 |
| §4 Zoom In/Out | **Use.** Mandatory triggers (§4.3) + elective zoom from Season Slate. Stack-based container transitions (max depth 3). | scale_transitions_v30 §4 |
| §5 Domain Echo timing | **Use "Hybrid" column.** Domain Echo fires at Cascade Phase Accounting. | scale_transitions_v30 §5.3 |
| §6 Mode Transition Procedures | **Discard.** No session boundaries. No TTRPG→BG transition. The engine runs continuously. Zoom In/Out replaces mode transition. | — |
| §6.4 Coherence Initialization | **Use.** First activation = Coherence 10. Subsequent = carry forward. | scale_transitions_v30 §6.4 |
| §6.5 Coherence Cost (PP-198) | **Use.** Binary declaration at Phase 1 of Cascade Phase. | scale_transitions_v30 §6.5 |

**Implementation:** ZoomManager in GameDirector. Stack-based container transitions. ConsequenceRouter handles Domain Echo.

### 1.7 Faction Layer (faction_layer_v30.md)

| Rule | Videogame Decision | Source |
|------|-------------------|--------|
| Strategic-scale faction actions | **Use in full.** Card-hand economy, Domain Actions, seasonal accounting. | faction_layer_v30 §§1–6 |
| §4.2 Grand Debate (Hybrid/TTRPG Only) | **Use.** Grand Debate fires as a Zoom In event when conditions met. | faction_layer_v30 §4.2 |
| §6.4 BG Mode Officer Fate | **Use as auto-resolve.** When officer fate is resolved without player Zoom In. | faction_layer_v30 §6.4 |
| §8.1 BG Mode / §8.2 TTRPG Mode / §8.3 Hybrid Mode | **Use §8.3 (Hybrid).** This IS the videogame's treaty/diplomacy system. | faction_layer_v30 §8.3 |

### 1.8 NPC Behavior (npc_behavior_v30.md)

| Rule | Videogame Decision | Source |
|------|-------------------|--------|
| §§1–7 (TTRPG NPC systems) | **Use.** Convictions, Stance Triangles, arc trajectories, Disposition, companion behavior. Engine drives all NPC decisions. | npc_behavior_v30 §§1–7 |
| §8 (BG Faction Priority Trees) | **Use.** Strategic-scale NPC faction AI. Runs every season at Phase 4. | npc_behavior_v30 §8 |
| §9 (Hybrid Translation) | **Use.** This IS the videogame's NPC translation layer: strategic-phase faction AI decisions translate to personal-scale NPC behavior when the player zooms in (§9.1), and personal-scale NPC events translate back to faction state (§9.2). | npc_behavior_v30 §9 |
| "GM decides" NPC reactions | **Author deterministic rules.** Every NPC reaction currently left to GM must become a decision tree or authored response. | — |

### 1.9 Player Agency (player_agency_v30.md)

**No mode branching.** All rules apply to the videogame directly. Beliefs, Duties, Scene Slate, Standing progression — all implemented as engine systems.

### 1.10 Companion Specification (companion_specification_v30.md)

**No mode branching.** All rules apply directly. Companion AI follows the behavioral specification without GM mediation.

### 1.11 Settlement Layer (settlement_layer_v30.md)

**No mode branching.** 36 settlements are data. Governance stats (Order, Prosperity, Defense) tracked by engine. Settlement scenes are Zoom In events from territory view.

---

## §2 — Unified Threadwork Mode Table

Replaces threadwork_v30 §7.3 three-column table.

| Rule | Videogame Implementation |
|------|-------------------------|
| Thread operations | **Personal scale:** Weaving, Pulling, Mending, Lock, Dissolution (full mechanics). **Strategic scale:** Weave, Mend, Investigate, Harvest (faction Domain Actions). Player may Zoom In to perform personal-scale ops during strategic phase (Coherence cost per PP-198). |
| Gap closure | **Personal:** Mending roll (Spirit×2 + History + TPS). **Strategic:** Mend order (faction action). Both resolve at Accounting. |
| Co-movement | **Personal:** Version C auto-effects (temporal + epistemic auto, actualized d6). **Strategic:** Draw Co-Movement Card. |
| Practitioner degradation | **Personal:** Coherence 10→0 tracked per character. **Strategic:** Not tracked for NPC faction practitioners (abstracted into faction Thread order outcomes). |
| World stability | **MS 100→0.** All changes unified at Accounting. Seasonal cap ±10 net (per threadwork_v30 §5.5). |
| Lock chronic drift | **Engine tracks.** Per-territory MS drift. Applied automatically at Accounting. No "GM tracks" — the engine IS the GM. |

---

## §3 — "GM Decides" Resolution Register

Every instance of "GM decides," "Game Master sets scope," "Game Master determines," or similar language in the design docs must be resolved to one of:

| Resolution Type | Description | Example |
|----------------|-------------|---------|
| **Authored** | Content is pre-authored per context (POI, NPC, location). | "Depth axis: GM-assigned" → POI has authored Depth value. |
| **Deterministic** | Formula or lookup table replaces GM judgment. | "GM sets Ob" → Ob = floor(stat/2) + modifier. |
| **AI-driven** | NPC behavior system makes the decision via priority tree. | "GM decides NPC reaction" → NPC Stance Triangle + Conviction determines reaction. |
| **Player choice** | Player explicitly chooses (where GM would have offered options). | "GM offers choice" → UI presents options with visible consequences. |
| **Default** | A single default behavior fires unless a specific condition overrides. | "GM may rule X" → X happens unless [condition], in which case Y. |

This register is not exhaustive here. Each design doc should be audited for "GM" references and resolved per the above types during Godot extraction.

---

## §4 — What Is Discarded

The following are formally abandoned and should not be implemented:

| Discarded | Reason |
|-----------|--------|
| TTRPG-only mode (standalone tabletop play) | No tabletop product. Personal-scale mechanics remain as the videogame's scene-level gameplay. |
| BG-only mode (standalone board game play) | No board game product. Strategic-scale mechanics remain as the videogame's territory-level gameplay. |
| Mode switching (TTRPG↔BG↔Hybrid transitions) | The videogame runs both scales continuously. Zoom In/Out replaces mode switching. |
| Session boundaries | Continuous play. Save/load replaces session management. |
| GM adjudication | Engine handles all resolution. NPC AI + authored content + deterministic rules. |
| GameMode enum in Godot | Strip. One mode. Starting values determined by difficulty/campaign setup. |
| Mode-split file naming (`_ttrpg.md`, `_bg.md`) | Deprecated. Historical only. |
| Physical component references (cards, tokens, dice, mats) | UI elements replace physical components. Card-hand economy → UI card panel. Territory map → interactive map. Dice → engine resolution with visual feedback. |

---

## §5 — Implementation Priority

For Godot extraction (Phase 1+ in conversion_ledger.md), read this document alongside the source design doc. For each system:

1. Check §1 above for which rules to extract.
2. For "Use" entries: extract the full mechanic from the source doc.
3. For "Use as strategic-scale" entries: extract into BoardContainer/faction action logic.
4. For "Use as auto-resolve" entries: extract the simplified formula for non-zoomed resolution.
5. For "Discard" entries: skip entirely.
6. For any "GM decides" language encountered: resolve per §3 before implementing.

---

*This document is the single mode-collapse reference. When a design doc has a three-mode table and this document specifies which column to use, this document governs. If a discrepancy is found between this document and a design doc's videogame-relevant rules, file an editorial item.*
