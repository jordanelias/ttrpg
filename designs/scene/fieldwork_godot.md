# VALORIA — FIELDWORK SYSTEM v1.1 — §10 Godot Video Game Implementation
## Parent: designs/fieldwork/fieldwork_design_v1.md
## Status: DESIGN — canonical subsystem file. See parent for full cross-references.
## Mode applicability: Godot video game
## Godot validation: 2026-04-13 against jordanelias/valoria-game@main

---

## §10 GODOT VIDEO GAME IMPLEMENTATION

### §10.1 Exploration Map Architecture

Each territory is a navigable area containing POI nodes. POI nodes exist in the scene tree at authoring time but are conditionally visible based on the player-character's perception gates.

**Node structure (Godot):**
```
Territory (Node2D / Node3D)
├── NavigableArea
│   ├── PathGraph (navigation mesh or A* grid)
│   └── EnvironmentZones (Calamity radiation visual effects)
├── POI_Landmarks[] (always visible)
├── POI_Resources[] (visible if perception gate met)
├── POI_Secrets[] (visible if perception gate met)
├── POI_Remnants[] (visible if TS ≥ 10; rendering strain triggers on interact)
├── POI_Anomalies[] (visible if TS ≥ 30; environmental hazard zone)
└── POI_Breaches[] (visible if TS ≥ 50; existential encounter zone)
```

**Perception gate implementation:** Each POI node has an `is_perceivable(character)` method that checks the character's TS, Cognition, Certainty, and relevant Histories against the POI's depth requirements. POI nodes that fail the perception check are not rendered — they do not exist in the character's world.

**Conditional POI gates:** POIs gated by MS band, season, faction control, or prior discovery are evaluated dynamically. A Remnant that becomes perceivable when MS drops below 60 appears in-world at the moment MS crosses the threshold — the world changes because the substrate's intelligibility has changed.

### §10.2 Intelligibility Gradient Visualisation

The Intelligibility Gradient is the system's signature visual feature. The Godot implementation makes the character's rendering capacity visible — not as a filter over a single objective world, but as the character's genuine experiential reality.

**There is no neutral visual layer.** The Thread configuration constitutes a different experiential reality depending on how the observer's consciousness renders it. The Godot implementation uses different visual presentations for different characters, but this is not a "filter" — each visual is the world as that character genuinely inhabits it. The relationship between rendering and world is constitution/experience (Foundations §3.1), not appearance/reality.

| TS Range | Visual Presentation | Implementation |
|----------|---------------------|----------------|
| 0–9 | The world as settled consciousness renders it. Solid, consistent, complete. | Default scene rendering. No post-processing. |
| 10–29 | Something at the edges. Faint disturbance near Thread-adjacent sites. | Shader: subtle vertex displacement + chromatic aberration within POI activation radius. |
| 30–49 | The substrate's structure becomes part of the character's world. Thread filaments visible as a constitutive layer. | Shader: additive blend layer showing Thread mesh. Activated per-POI. |
| 50–69 | Full thread-sight. The substrate is experienced as a dimension of reality, not a hidden layer. | Shader: persistent overlay on all objects within Calamity zones. NPC aura indicators. |
| 70+ | The boundary of the intelligible. What lies beyond is not darkness or void — it is the rendering's dissolution, the edge of what consciousness can constitute. | Shader: dissolve effect at zone boundaries. Particle systems for surfeit-of-being eruptions. Audio: low-frequency rumble. |

**Certainty-dependent constitution:**

The same POI constitutes a different world for characters at different Certainty values. This is not interpretation or opinion — it is the world as given to that consciousness:

- **Certainty 5 (Orthodox):** Thread phenomena constitute a world where demonic intrusion is real. The visual language uses Church iconography — hellfire palette, sin-associated imagery. The character's rendering genuinely produces this world.
- **Certainty 3 (Questioning):** Thread phenomena constitute an ambiguous world. Undefined shimmer, neutral colour shifts. The character's rendering is uncertain — the world itself is uncertain.
- **Certainty 0 (Accepted):** Thread phenomena constitute a world where the substrate is natural. Calm, structural, the fabric of reality experienced directly. Beauty rather than horror.

### §10.3 Investigation Journal System

The Evidence Track maps to a **Journal** UI element:

```
Journal
├── Active Investigations[]
│   ├── Question (text)
│   ├── Evidence Track (progress bar: current / threshold)
│   ├── Clues[] (individual evidence items with reliability tags)
│   │   ├── ClueItem { text, source, reliability_tag, depth }
│   │   └── InertKnowledge { text, source, flagged: true }
│   └── Status (open / resolved / desperate_trail / blocked)
├── Resolved Investigations[]
└── Rumour Board (unverified items, no progress tracking)
```

**Inert Knowledge UI:** When a non-sensitive character receives Thread-verified evidence, the journal displays it with a distinctive visual treatment — grayed out, slightly blurred, with a tooltip: "Your character knows this was said, but cannot fully grasp its implications." The player can *read* the information (maintaining player agency) but the character cannot act on it mechanically (maintaining the epistemological barrier).

**Implementation note:** `systems/trackers/Tracker.gd` + `TrackerRegistry.gd` are structurally compatible with Evidence Track backing. A thin `fieldwork/EvidenceTrack.gd` wrapper over `Tracker.gd` is sufficient — no tracker architecture changes required.

### §10.4 Disposition and Dialogue

NPC Disposition drives the dialogue system:

**Disposition meter:** Visible on NPC portrait during interaction. Range −3 to +5 displayed as a segmented bar.

**Dialogue option gating:** Conversation options are filtered by current Disposition + character attributes. A Bond-focused dialogue option requiring Disposition +3 simply does not appear at Disposition +1. The player sees what their character could plausibly say in this relationship.

**Social action as dialogue choice:** Each dialogue node can trigger a social action roll. The player selects the approach (Read, Converse, Connect, Impress, Negotiate, Rumour), the game rolls the pool, and the result determines the conversation branch.

**NPC memory:** NPCs remember prior interactions. A failed social action at Disposition −1 that drops Disposition to −2 should be reflected in dialogue — the NPC references the prior misstep. This is not mechanical complexity; it is authored content gated by state.

**Implementation note:** `systems/npc/NPCSocialModifiers.gd` is compatible with Disposition backing. NPC memory requires `NarrativeState` persistence — see G10-F04 below.

### §10.5 Dice Visualisation

d10 pool rolls use a visual system consistent across all Valoria mechanics:

| Die Face | Visual | Colour |
|----------|--------|--------|
| 1 | Skull icon or down-arrow | Red |
| 2–6 | Neutral pip | Gray |
| 7–9 | Success checkmark | Blue |
| 10 | Double success + chain icon | Gold |

Net successes displayed prominently. Degree announced with audio cue and screen flash (Failure: dull red; Partial: amber; Success: blue; Overwhelming: gold pulse).

### §10.6 Season and Clock Integration

Fieldwork actions consume in-game time:
- Each exploration/investigation/social scene = 1 time unit.
- Each season has a budget of 4–6 time units (configurable; represents the available daylight/travel time).
- At season end: Accounting Phase fires automatically. Clocks advance. Faction actions resolve.

**Clock HUD:** MS, CI, IP displayed persistently. PI and faction-specific tracks available on faction screen. Exposure displayed per-territory on map overlay.

**Implementation note:** `systems/faction/FactionTurnSystem.gd` handles seasonal accounting. `systems/trackers/TrackerRegistry.gd` can back MS/CI/IP. Clock HUD is a new UI scene — see G10-F06 below.

---

## §10 VALIDATION FINDINGS (2026-04-13)

Technical validation against jordanelias/valoria-game@main repo structure.

| ID | §Ref | Priority | Finding | Implementation Path |
|----|------|----------|---------|---------------------|
| G10-F01 | §10.1 | P3 | POI system entirely absent. No `systems/fieldwork/` directory, no `POINode.gd`, no `FieldworkManager.gd`, no NavigableArea/PathGraph. Territory data exists at registry level (`SettingState.gd`) only. | New: `systems/fieldwork/POINode.gd`, `FieldworkManager.gd`, `POIRegistry.gd`. Extend `SettingState.gd` with POI lists per territory. |
| G10-F02 | §10.2 | P3 | No shaders implemented (`shaders/` is `.gitkeep`). Intelligibility Gradient visual layer has no code equivalent. Expected — POI system must precede shaders. | New: per-TS-band shader files in `shaders/`. Integrate with POI activation radius triggers. |
| G10-F03 | §10.3 | P2 | Journal UI not implemented. `systems/trackers/Tracker.gd` is structurally compatible with Evidence Track backing — no tracker architecture change needed. | New: `scenes/fieldwork/Journal.tscn`, `fieldwork/EvidenceTrack.gd` (thin wrapper over `Tracker.gd`). |
| G10-F04 | §10.4 | P2 | NPC memory (§10.4) blocked by two existing audit findings: A-02 (`NPCTrajectoryEvaluator` disconnected from season loop) and DA-03 (`NarrativeState.deserialize()` stub — state not persisted). Disposition infrastructure (`NPCSocialModifiers.gd`) is present. | Fix A-02 and DA-03 first. Then: `fieldwork/DispositionTrack.gd` per NPC, dialogue gating via `NPCSocialModifiers`. |
| G10-F05 | §10.5 | P3 | Dice visualisation not confirmed from directory listing. `assets/ui/` and `assets/audio/` directories exist. Not fieldwork-specific — core engine UI concern. | Verify `scenes/ui/` for existing dice roll UI. Dice visuals are shared across all resolution modes, not fieldwork-only. |
| G10-F06 | §10.6 | P2 | Clock HUD absent. Two existing bugs affect fieldwork season integration: B-03 (`Constants.RS_CRITICAL_THRESHOLD` missing — POI gates use MS bands) and A-05 (`NarrativeState.log_event()` hardcodes `season = 0`). | Fix B-03 and A-05 first. New: `scenes/ui/ClockHUD.tscn`. Wire to `TrackerRegistry` for MS/CI/IP. |
| G10-F07 | §4.5 | P3 | `systems/threadwork/` contains only `.gitkeep`; `ThreadworkSystem.gd` lives in `systems/engine/`. Thread-Read fieldwork integration (§4.5) requires threadwork-fieldwork coupling. Structural inconsistency with declared architecture. | Decision required: move `ThreadworkSystem.gd` to `systems/threadwork/` (preferred — consistent with directory architecture) or document engine placement as permanent. |

**Summary:** No fieldwork implementation exists. Infrastructure is compatible — tracker system, NPC social modifiers, faction turn system, and territory registries all support the §10 architecture without modification. Four existing audit findings (A-02, A-05, B-03, DA-03) directly block §10.4 and §10.6 integration. Recommended sequence: fix audit blockers → POI system → Journal UI → Clock HUD → Shaders.

**No changes required to fieldwork_design_v1.md §10 specification.** The design is internally consistent with Godot architecture. Gaps are implementation gaps, not design gaps.
