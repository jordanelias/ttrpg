# VALORIA — GAME DEVELOPMENT SPECIFICATION
## Architecture, Engine, Pipeline, and Procedure
## Date: 2026-04-11
## Engine: Godot 4.x (GDScript)

---

# PART ONE: ORIENTATION

## 1.1 What Exists

A GitHub repository (`jordanelias/ttrpg`, branch `main`) containing the complete design documentation for a tabletop game called Valoria. Approximately 35 active design documents, 15 parameter/reference files, 10 canonical/amendment files, and supporting infrastructure. No game code. Pure mechanical specification — formulas, procedures, tables, edge-case rulings, patch history.

The documents describe a hybrid game: personal-scale RPG (one character in combat, social contests, metaphysical operations) interlocked with strategic-scale board game (one faction competing for territorial control). Two scales connected by a consequence propagation system. Three world clocks measuring existential threats — Mending Stability at zero is shared loss; the other two (Church Influence, Institutional Pressure) create escalating crises that reshape the game but are not automatically terminal.

## 1.2 What You Are Building

A Godot 4 video game implementing this hybrid structure. The architecture has four layers:

| Layer | Purpose | Godot Pattern |
|-------|---------|---------------|
| **Content** | What exists — all persistent world state | Autoload + Resources |
| **Conflict** | What happens — situation generation, scene selection | RefCounted logic |
| **Resolution** | How it plays out — containers + core engine | Scenes + RefCounted logic |
| **Progression** | What changes — consequences, accounting, new conditions | Tracker mutations + display |

The game loop: Content → Conflict → Resolution → Progression → Content (updated) → next season.

## 1.3 Guiding Principles

**Resources are data.** A Resource stores faction stats, character attributes, territory properties. It has no behavior. It is read by multiple systems and edited only through controlled mutation paths.

**Nodes are lifecycle.** A Node manages scene tree presence — instantiation, signal wiring, visual display, input handling, cleanup. Container scenes are Nodes. UI elements are Nodes.

**RefCounted is logic.** The dice engine, tracker registry, consequence router, situation generator, AI decision trees, and threadwork system are all RefCounted scripts. They have no scene tree presence. They are instantiated, called, and garbage-collected. They do not render anything.

**One autoload.** The Meta-Container is the single autoload. It holds all persistent state and provides a read-only query interface for lower layers. All state mutations flow through `Meta.receive_consequence()`.

**Call down, signal up.** Parent nodes call methods on children. Children emit signals to parents. No node reaches laterally to a sibling. No node reaches upward to its parent by reference.

**Containers do not know about each other.** The CombatContainer does not know the BoardContainer exists. The GameDirector knows about both and manages transitions between them.

---

# PART TWO: REPOSITORIES AND PROJECT STRUCTURE

## 2.1 Two Repositories

| Repository | Purpose | Relationship |
|-----------|---------|-------------|
| `jordanelias/ttrpg` | Design documentation (canonical source of truth) | Read-only reference. Never modified by the game project. |
| `jordanelias/valoria-game` (new) | Godot project (all game code, assets, tests) | Implements mechanics described in the design repo. |

The design repo has its own CI, editorial workflow, and patch management. The game repo has its own directory conventions, asset pipeline, and test suite. Mixing them creates workflow conflicts.

Clone both locally:
```bash
git clone https://github.com/jordanelias/ttrpg.git ~/projects/valoria-design
gh repo create jordanelias/valoria-game --private
git clone https://github.com/jordanelias/valoria-game.git ~/projects/valoria-game
```

## 2.2 What Lives Where

| Content | Location |
|---------|----------|
| Design documents (canonical) | `valoria-design/` (local clone of ttrpg repo) |
| Godot project | `valoria-game/` |
| Extraction worksheets | `valoria-game/docs/extraction/` |
| Conversion ledger | `valoria-game/docs/conversion_ledger.md` |
| Design doc snapshots (frozen at extraction SHA) | `valoria-game/docs/snapshots/` |
| Trigger catalogue | `valoria-game/docs/trigger_catalogue.md` |
| Architecture specification | `valoria-game/docs/architecture.md` |

## 2.3 Godot Project Structure

```
valoria-game/
├── project.godot
├── .gitignore
│
├── docs/
│   ├── architecture.md
│   ├── conversion_ledger.md
│   ├── trigger_catalogue.md
│   ├── extraction/           # Per-document worksheets
│   └── snapshots/            # Frozen source docs at extraction SHA
│
├── autoload/
│   └── Meta.gd              # THE single autoload
│
├── resources/
│   ├── data_types/           # Resource class definitions (.gd)
│   │   ├── FactionData.gd
│   │   ├── CharacterData.gd
│   │   ├── TerritoryData.gd
│   │   ├── ... (sub-resources: HistoryData, KnotData, etc.)
│   │   ├── Consequence.gd
│   │   ├── SceneOption.gd
│   │   ├── SeasonSlate.gd
│   │   ├── TriggerCondition.gd
│   │   └── SaveData.gd
│   └── instances/            # Data instances (.tres files)
│       ├── factions/
│       ├── territories/
│       ├── characters/
│       │   ├── named/        # 13 hand-authored NPCs
│       │   └── templates/    # Officer/local NPC generation templates
│       ├── weapons/
│       ├── armour/
│       ├── action_cards/
│       ├── co_movement_cards/
│       ├── triggers/         # Conditional trigger definitions
│       └── tables/           # Lookup tables (calamity matrix, Ob tables, etc.)
│
├── systems/                  # RefCounted game logic (no scene tree presence)
│   ├── engine/
│   │   ├── CoreResolver.gd
│   │   ├── CoreEngine.gd
│   │   ├── ConsequenceRouter.gd
│   │   ├── RollContext.gd
│   │   ├── RollResult.gd
│   │   ├── PoolModifier.gd
│   │   ├── ObModifier.gd
│   │   └── TrackerBinding.gd
│   ├── trackers/
│   │   ├── Tracker.gd
│   │   ├── TrackerRegistry.gd
│   │   └── TrackerThreshold.gd
│   ├── resolution_modes/
│   │   ├── ResolutionMode.gd       # Base
│   │   ├── SoloResolution.gd
│   │   ├── OpposedSimultaneous.gd
│   │   ├── OpposedSequential.gd
│   │   ├── VersusResolution.gd
│   │   └── PhaseLockedSimultaneous.gd
│   ├── threadwork/
│   │   ├── ThreadworkSystem.gd
│   │   ├── CoMovementGenerator.gd
│   │   └── ThreadVisualHandler.gd   # Interface
│   ├── ai/
│   │   ├── FactionAI.gd            # Base
│   │   └── [per-faction AI scripts]
│   ├── npc/
│   │   ├── NPCGenerator.gd
│   │   └── [per-NPC trajectory scripts]
│   ├── situation/
│   │   ├── SituationGenerator.gd
│   │   └── SceneAvailabilityBuilder.gd
│   ├── registries/
│   │   ├── FactionRegistry.gd
│   │   ├── CharacterRegistry.gd
│   │   ├── SettingState.gd
│   │   └── NarrativeState.gd
│   └── util/
│       ├── Enums.gd
│       └── Constants.gd
│
├── scenes/                   # Godot scenes (.tscn) + scripts (.gd)
│   ├── director/
│   │   ├── GameDirector.tscn
│   │   └── GameDirector.gd
│   ├── containers/
│   │   ├── ContainerBase.gd       # Shared interface (script only)
│   │   ├── conflict/
│   │   │   ├── ConflictContainer.tscn
│   │   │   └── ConflictContainer.gd
│   │   ├── combat/
│   │   │   ├── CombatContainer.tscn
│   │   │   ├── CombatContainer.gd  # Node lifecycle, UI updates
│   │   │   └── CombatLogic.gd     # State machine, round resolution
│   │   ├── debate/
│   │   ├── narrative/
│   │   ├── battle/
│   │   └── board/
│   ├── ui/
│   │   ├── persistent/        # Always-visible (CanvasLayer)
│   │   ├── season_overview/
│   │   ├── combat_ui/
│   │   ├── debate_ui/
│   │   ├── board_ui/
│   │   ├── thread_ui/
│   │   ├── cascade/
│   │   ├── menus/
│   │   └── victory/
│   └── transitions/
│
├── shaders/
├── assets/
│   ├── sprites/
│   ├── portraits/
│   ├── backgrounds/
│   ├── ui/
│   ├── map/
│   └── audio/
├── dialogue/                 # Dialogic 2 timelines (if used)
└── tests/
```

Container scripts vs Logic scripts: the Container script (.gd attached to the .tscn root) handles Godot node lifecycle — `setup()`, `_ready()`, signal connections, UI node references, visual updates, `scene_completed` emission. The Logic script handles the game state machine — round phases, declaration/resolution sequencing, turn order, win/loss evaluation. The Container delegates to the Logic. The Logic emits game events. The Container translates those into UI updates and signals.

## 2.4 .gitignore

```gitignore
# Godot cache and imports
.godot/

# OS
.DS_Store
Thumbs.db

# IDE
.vscode/
*.swp
*.swo

# Build
build/
export/
export_presets.cfg
```

Note: `.tres` files are plain text. Track them normally in Git. Do not use LFS for `.tres`. Use LFS only for binary assets (`.png`, `.wav`, `.ogg`) if they become large enough to warrant it.

---

# PART THREE: THE FOUR-LAYER ARCHITECTURE

## 3.1 Layer 1 — Content (Meta-Container)

### Purpose

All persistent world state. Single source of truth. Read-only query interface for lower layers. All mutations through `receive_consequence()`.

### What It Holds

**Tracker Registry** — every numerical track in the game, indexed by `StringName` key (`scope:owner:id`). World clocks, personal stats, faction stats, territory tracks, NPC tracks, scene-scope tracks, unit stats. Approximately 50+ tracker types across all scopes.

**Faction Registry** — all faction data Resources. Starting stats, private tracks, card hands, unit rosters, diplomatic state. All factions registered at startup including those that activate mid-campaign (register dormant, activate on trigger event).

**Character Registry** — player character + named NPCs + generated officers/locals. Stat blocks, Histories, Knots, Beliefs, Thread state.

**Setting State** — territory data, adjacency graph, calamity radiation state (derived from MS), woven configuration registry (over-actualisation tracking), thread debt per territory, current season, year tracking.

**Narrative State** — NPC trajectory states (conditional, multi-season branching), queued scenes from prior seasons, event log, active Beliefs driving the personal arc.

### Tracker System

Every numerical track is a Tracker. The registry holds all trackers. Systems mutate trackers only through the registry.

```gdscript
class_name Tracker extends RefCounted

var key: StringName
var value: int
var min_value: int
var max_value: int            # -1 = unbounded
var thresholds: Array[TrackerThreshold] = []
var seasonal_cap: int = -1    # -1 = none; faction stats = 2
var seasonal_change: int = 0

func apply_change(delta: int, source: StringName) -> TrackerChangeResult:
    var result = TrackerChangeResult.new()
    result.old_value = value
    result.source = source

    if seasonal_cap > 0:
        var remaining = seasonal_cap - absi(seasonal_change)
        if remaining <= 0:
            result.capped = true
            result.new_value = value
            return result
        delta = clampi(delta, -remaining, remaining)

    var new_val = clampi(value + delta, min_value,
                         max_value if max_value >= 0 else 9999)
    var actual_delta = new_val - value
    value = new_val
    seasonal_change += actual_delta
    result.new_value = value
    result.actual_delta = actual_delta

    for t in thresholds:
        if _crossed(result.old_value, result.new_value, t):
            result.thresholds_crossed.append(t)
    return result
```

The seasonal ±2 cap is enforced here — the single choke point. All code paths that change faction stats (personal scene Domain Echoes, strategic phase orders, accounting formulas) flow through `tracker_registry.apply_change()`. No direct mutation of faction data fields.

### Consequence Processing

```gdscript
# In Meta.gd:
func receive_consequence(consequence: Consequence):
    var change_result = tracker_registry.apply_change(
        consequence.tracker_key, consequence.delta, consequence.source)
    _visual_queue.append(change_result.to_visual_entry())
    for threshold in change_result.thresholds_crossed:
        _process_threshold(threshold)
```

Mechanical processing is synchronous and instant. Visual display is queued and consumed asynchronously by the PersistentUI.

### Consequence Timing

Two timing categories. Every consequence is classified at creation:

| Timing | When Applied | Examples | Why |
|--------|-------------|---------|-----|
| **Immediate** | During resolution, as it occurs | MS (PP-253: live, no buffer), Coherence, Health, Wounds, Stamina, Composure, Momentum | Subsequent rolls in the same conflict read these values for Ob/pool calculation |
| **Deferred** | At conflict conclusion, upstreamed | Domain Echoes (faction stat changes), narrative outcomes, NPC triggers, Belief evaluations | Conflict outcome may change their meaning; should be evaluated as a whole |

```gdscript
class_name Consequence extends RefCounted

enum Timing { IMMEDIATE, DEFERRED }

var tracker_key: StringName
var delta: int
var source: StringName
var timing: int

func is_immediate() -> bool:
    return timing == Timing.IMMEDIATE

static func classify(tracker_key: StringName) -> int:
    if tracker_key == &"world:global:rs":
        return Timing.IMMEDIATE
    if tracker_key.begins_with(&"personal:"):
        var tracker_id = tracker_key.get_slice(":", 2)
        if tracker_id in [&"coherence", &"certainty", &"health_damage",
                          &"wounds", &"stamina", &"composure", &"momentum"]:
            return Timing.IMMEDIATE
    return Timing.DEFERRED
```

## 3.2 Layer 2 — Conflict (Situation Generator)

### Purpose

Evaluates game state each season. Produces a SeasonSlate describing what conflicts are available or mandatory. Presents the slate to the player for scene selection and faction order placement.

### Process

1. **Evaluate NPC trajectory conditions** against current state. Fire any that trigger (e.g., Klapp discovery roll at scheduled season, Elske return condition met).
2. **Evaluate clock thresholds** from prior season's changes. Queue threshold events.
3. **Run AI faction decision-making.** Each AI selects orders from its priority tree. NPC-only orders (no player involvement) resolve immediately. Orders involving the player generate mandatory scene options.
4. **Build elective scene options** from player character's Beliefs, Knots, available investigation targets, and territory-based opportunities.
5. **Present SeasonSlate to player.** Mandatory scenes flagged. Elective scenes offered (player chooses 1–3). Faction order panel for card-hand play.
6. **Lock the season slate.** Conflicts set. Proceed to resolution.

### Implementation

The SituationGenerator is a RefCounted utility. The SeasonOverview is a Control scene (the game's signature screen — the player's strategic interface between seasons).

Trigger conditions are data-driven: each potential trigger is a TriggerCondition Resource with an associated evaluation Callable. The generator iterates registered triggers and filters by conditions. New triggers are added by creating Resource files, not modifying code.

## 3.3 Layer 3 — Resolution

### 3.3a Containers

Five scene container types plus a Conflict Container that wraps them and a Board Container for the strategic phase:

| Container | Scale | Purpose |
|-----------|-------|---------|
| **Conflict** | Wrapper | Hosts scene containers. Tracks data across scene transitions within a single conflict. Routes immediate consequences to Meta. Accumulates deferred consequences for upstream at conclusion. Evaluates Belief engagement for CP. |
| **Combat** | Personal | Pool-split offence/defence, priority resolution, reach system, wound/stamina tracking |
| **Debate** | Personal | Argument styles, Piety Track, Composure/strain, exchange resolution |
| **Narrative** | Personal | Dialogue, investigation, evidence gathering, event choices, skill checks |
| **Battle** | Relational | Mass combat 6-phase resolution, unit engagement, commander mechanics |
| **Board** | Territorial | Territory map, faction orders, card-hand economy, fog of war, AI resolution |

All scene containers implement a shared interface:

```gdscript
class_name ContainerBase extends Control

signal scene_completed(results: ContainerResult)
signal consequence_reported(consequence: Consequence)
signal zoom_in_requested(context: Dictionary)
signal scene_escalated(new_type: StringName, context: Dictionary)

var meta: Meta

func setup(context: Dictionary) -> void: pass
func create_snapshot() -> Resource: return null
func restore_snapshot(snapshot: Resource) -> void: pass
func get_partial_results() -> ContainerResult: return ContainerResult.new()
func apply_zoom_results(results: ContainerResult) -> void: pass
```

### The Conflict Container

The structural bridge between scene-level resolution and campaign-level progression.

```gdscript
class_name ConflictContainer extends Node

signal conflict_completed(result: ConflictResult)

var meta: Meta
var deferred_consequences: Array[Consequence] = []
var narrative_log: Array[Dictionary] = []
var active_scene: ContainerBase

func _on_scene_consequence(consequence: Consequence):
    if consequence.is_immediate():
        meta.receive_consequence(consequence)   # Pass through NOW
    else:
        deferred_consequences.append(consequence) # Accumulate
    narrative_log.append(consequence.to_log_entry())

func transition_to_scene(scene_type: StringName, context: Dictionary):
    if active_scene:
        deferred_consequences.append_array(active_scene.get_partial_results().consequences)
        active_scene.queue_free()
    var scene = _load_scene(scene_type)
    scene.meta = meta
    scene.setup(context)
    scene.consequence_reported.connect(_on_scene_consequence)
    scene.scene_completed.connect(_on_scene_completed)
    scene.scene_escalated.connect(_on_scene_escalated)
    add_child(scene)
    active_scene = scene

func _on_scene_escalated(new_type: StringName, context: Dictionary):
    transition_to_scene(new_type, context)  # Debate → Combat, Investigation → Debate

func _on_scene_completed(results: ContainerResult):
    deferred_consequences.append_array(results.consequences)
    active_scene.queue_free()
    active_scene = null
    var follow_up = _evaluate_follow_up(results)
    if follow_up:
        transition_to_scene(follow_up.scene_type, follow_up.context)
        return
    _conclude()

func _conclude():
    var result = ConflictResult.new()
    result.narrative_log = narrative_log
    result.cp_earned = _evaluate_belief_engagement(meta.characters.get_player(), narrative_log)
    result.domain_echoes = _evaluate_domain_echoes(deferred_consequences)
    result.deferred_consequences = deferred_consequences
    conflict_completed.emit(result)
```

Scenes can escalate (debate → combat via Register Shift). Scenes can trigger follow-up scenes (investigation discovers something → confrontation). The Conflict Container manages these transitions. The full arc is evaluated at conclusion for CP and Domain Echo scope.

### Zoom Manager

Stack-based container transitions. Outer container suspends (snapshot state, disable processing, dim visually). Inner container activates. On completion, inner frees, outer restores. Maximum stack depth: 3 (Board → Battle → Combat).

```gdscript
func _on_zoom_in(context: Dictionary):
    var frame = ZoomFrame.new()
    frame.container = active_container
    frame.snapshot = active_container.create_snapshot()
    zoom_stack.push_back(frame)
    active_container.process_mode = Node.PROCESS_MODE_DISABLED
    active_container.modulate.a = 0.3

    var inner = _load_container(context.scene_type, context)
    container_host.add_child(inner)
    var prev = active_container
    active_container = inner
    await inner.scene_completed

    inner.queue_free()
    var frame_out = zoom_stack.pop_back()
    prev.process_mode = Node.PROCESS_MODE_INHERIT
    prev.modulate.a = 1.0
    prev.restore_snapshot(frame_out.snapshot)
    active_container = prev
    prev.apply_zoom_results(inner.get_results())
```

### 3.3b Core Engine

Every mechanical interaction flows through a three-stage pipeline:

**Stage 1 — Context Assembly.** The calling system builds a `RollContext`: pool (base + sourced modifiers), TN (with overrides), Ob (base + sourced modifiers), resolution mode, and tracker bindings (which trackers are affected and how each degree maps to a change).

Every modifier is sourced and traceable:

```gdscript
class_name PoolModifier extends RefCounted
var source: StringName    # "history_einhir_scholar"
var delta: int            # +6
var reason: String        # "Einhir Scholar History (3 pts + 3)"

class_name ObModifier extends RefCounted
var source: StringName    # "wounds"
var delta: int            # +2
var reason: String        # "Wounds (2): +2 Ob"
```

The roll context includes modifiers from current world state: MS-dependent Thread Ob modifier (read live from Meta), Coherence-dependent Ob and pool penalties, wound penalties, over-actualisation, thread debt, sequential failure penalties. These are queried from Meta at context assembly time — they reflect the world as it is right now, including any changes from prior operations in the same contact window.

**Stage 2 — Resolution Branching.** Five resolution modes:

| Mode | When | Mechanic |
|------|------|----------|
| **Solo** | One actor vs fixed Ob | Thread Leap, faction orders, investigation checks |
| **Opposed Simultaneous** | Both sides roll, compare | Board game battles, social contest exchanges |
| **Opposed Sequential** | Priority-ordered, each sees prior results | Personal combat rounds, board game order tiers |
| **Versus** | Attacker offence vs defender defence | Melee pool-split |
| **Phase-Locked Simultaneous** | All resolve independently, consequences at sync point | Mass combat Phase 6 (all damage applies at once) |

Each mode is a concrete class extending `ResolutionMode`. Adding a new mode means adding one script.

**Dice Engine.** Two variants determined by action category:

TTRPG dice (personal-scale rolls): d10, success on faces ≥ TN (Standard TN 7), face 10 = +1 success + bonus die that chains indefinitely, face 1 = −1 success. Net can be negative.

Board game dice (strategic-scale rolls): d10, non-exploding, success on 7–9 (+1), face 10 = +2, face 1 = −1.

Degree determination (both variants): Overwhelming requires net ≥ 2×Ob AND net ≥ 3. Success requires net ≥ Ob. Partial requires net > 0 but < Ob. Failure is net ≤ 0. Ob floor is 1 (nothing below 1). Pool floor is 1D.

**Stage 3 — Consequence Routing.** The engine iterates the roll context's tracker bindings. For each binding, it calls the degree-specific handler (a Callable), receives a TrackerChange, and applies it through the tracker registry. The registry enforces bounds and seasonal caps. Threshold crossings fire automatically. Immediate consequences are reported to Meta. The full chain: degree → binding handler → tracker change → threshold check → consequence report.

### Threadwork System

A cross-cutting service, not a container. Any container can invoke it. The same mechanical pipeline resolves Thread operations regardless of whether the practitioner is in personal combat, mass combat, investigation, or executing a faction strategic order.

The pipeline: eligibility check → environmental modifier query (MS-dependent Ob, territory thread debt, Coherence state) → Leap resolution → contact window (Focus − 1 operation rounds) → per-operation resolution with co-movement (three auto-effects always, per P-01) → consequence reporting.

**The Feedback Loop.** Within a single contact window, MS and Coherence changes from each operation feed back into the next operation's modifiers. The system recalculates MS Ob modifier and Coherence Ob modifier after each operation by querying Meta's live values. This produces the canonical compounding spiral: low Coherence increases Thread Ob → harder operations produce worse MS outcomes on Failure → worse MS further modifies Thread Ob.

MS changes from Thread operations apply immediately (PP-253). They are not batched. When the ThreadworkSystem produces an MS consequence, it is classified as IMMEDIATE and the Conflict Container forwards it to Meta at once. The Cascade display later shows what happened, but the state already changed.

**Visual representation** is per-container. Each container optionally implements a ThreadVisualHandler interface (show Leap transition, show operation result, show co-movement, show Coherence change). The ThreadworkSystem produces mechanical results. The container translates them into visuals appropriate to its context (full shader overlay in combat, simplified indicator in mass battle, territory highlight on the board).

## 3.4 Layer 4 — Progression

### During Resolution (Immediate)

MS, Coherence, Health, Wounds, Stamina, Composure, Momentum — applied through tracker registry as they occur. Threshold events fire on crossing.

### At Conflict Conclusion (Deferred)

Domain Echoes (faction stat changes from personal actions), narrative outcomes, NPC triggers, CP awards. The Conflict Container packages these into a ConflictResult and the GameDirector forwards them to Meta.

### Domain Echo Scope Recognition

The tabletop game relies on GM judgment to recognise when a personal action has faction-level scope. The video game must implement this programmatically. At conflict conclusion, the Conflict Container evaluates whether the conflict's outcome qualifies as a Domain Action:

- Was a named faction representative the target?
- Did the outcome affect faction-level state (Mandate, Stability, territory control)?
- Was the action at Relational+ scale?

If yes, the Domain Echo is packaged with the appropriate faction stat changes and upstreamed.

### Cascade Display

An animated summary of the season's consequences. Not a processing step — all processing already occurred. The Cascade reads the visual queue from Meta and presents it: clock movements, territory changes, threshold events, faction stat changes. The player sees what their personal actions did to the world.

### Seasonal Accounting

Runs after Cascade display. Clock advancement formulas. Faction collapse checks (Stability 0 = eliminated). Victory condition evaluation (all factions, all paths, 2-consecutive-Accounting hold counter). Year-End accounting every 4th season (additional steps). Seasonal cap reset on all faction stat trackers.

### New Condition Generation

After accounting, state has changed. The SituationGenerator reads updated state when generating the next season's slate. The loop closes naturally.

## 3.5 Game Director

The root coordinator. Owns the season loop, container lifecycle, zoom stack.

```gdscript
extends Node

func _ready():
    _start_season()

func _start_season():
    Meta.advance_season()
    var slate = situation_gen.generate_slate(Meta)
    season_overview.display(slate)
    var choices = await season_overview.choices_confirmed
    await _run_conflicts(choices.scenes)
    await _run_strategic_phase(choices.orders, slate.ai_orders)
    await _run_cascade_display()
    Meta.run_accounting()
    var victor = Meta.check_victory()
    if victor:
        _show_victory(victor)
        return
    if Meta.get_rs() <= 0:
        _show_shared_loss("Mending Stability Rupture")
        return
    _start_season()

func _run_conflicts(scenes: Array[SceneOption]):
    for scene in scenes:
        var conflict = preload("ConflictContainer.tscn").instantiate()
        conflict.meta = Meta
        conflict.consequence_reported.connect(_on_immediate_consequence)
        conflict.zoom_in_requested.connect(_on_zoom_in)
        container_host.add_child(conflict)
        conflict.transition_to_scene(scene.scene_type, scene.to_context())
        active_container = conflict
        var result = await conflict.conflict_completed
        for c in result.deferred_consequences:
            Meta.receive_consequence(c)
        conflict.queue_free()

func _on_immediate_consequence(consequence: Consequence):
    Meta.receive_consequence(consequence)
    persistent_ui.flash_tracker(consequence)
```

Scene tree:
```
GameDirector (Node)
├── ContainerHost (Node)          ← active container lives here
├── PersistentUI (CanvasLayer)    ← always visible: clocks, notifications
├── SeasonOverview (CanvasLayer)  ← Layer 2 UI
└── TransitionEffects (CanvasLayer)
```

---

# PART FOUR: CHARACTERS

## 4.1 Player Character Options

**Create own character:** Attribute allocation (10 attributes from a point pool), History selection, Knot declaration, Belief writing. Thread Sensitivity 0 at creation. Faction assignment (determines which faction the player controls at strategic scale).

**Play as named NPC:** 13 named characters with pre-set stats, faction affiliation, relationships, narrative trajectory. Different NPCs produce structurally different games because their faction, Thread Sensitivity, and starting relationships differ.

Both paths produce a `CharacterData` Resource that the game treats identically from that point forward.

## 4.2 NPC Population

Three tiers:
- **Named NPCs (13):** Hand-authored full stat blocks with trajectory systems (multi-season branching arcs). The narrative spine of the game.
- **Faction officers (3–5 per faction):** Procedurally generated at game start from templates. Name, key stats, personality trait. Command military units, serve as opponents in Zoom In duels, and as targets for social contests. Persistent across the campaign.
- **Local NPCs (as needed):** Generated per scene. Minimal stats. Exist for one scene only.

All factions are registered at startup, including those that activate mid-campaign (e.g., Löwenritter enters via coup event). Their trackers exist but are dormant. Activation flips a flag and the faction begins participating in AI decisions and order resolution.

---

# PART FIVE: SAVE/LOAD

Save between seasons only. This avoids serializing mid-combat or mid-debate state.

Save point: after Layer 4 completes, before Layer 2 generates the next slate. All state is in Meta's registries and Resources.

Implementation: convert all registry state to Dictionaries via `serialize()`/`deserialize()` methods. Save as a `.tres` SaveData Resource. Use Dictionary serialization for persistence to avoid Godot's Resource nesting/reference-sharing edge cases. Use Resources at runtime for type safety and inspector editing.

```gdscript
func save_game(slot: String):
    var save = SaveData.new()
    save.tracker_states = Meta.tracker_registry.serialize()
    save.faction_data = Meta.factions.serialize()
    save.character_data = Meta.characters.serialize()
    save.setting_data = Meta.setting.serialize()
    save.narrative_data = Meta.narrative.serialize()
    ResourceSaver.save(save, "user://saves/%s.tres" % slot)
```

---

# PART SIX: ENVIRONMENT SETUP

## 6.1 Install Godot 4

Download Godot 4.3+ from https://godotengine.org/download. Standard build, not .NET (using GDScript, not C#). Extract and run once to verify.

## 6.2 Create the Godot Project

1. Open Godot. New Project.
2. Project path: your cloned `valoria-game/` repository.
3. Renderer: **Compatibility** (2D game, maximum platform support). Note: if the Thread Leap shader requires effects beyond Compatibility's capabilities, switch to Mobile renderer later. Test shaders early.
4. Create & Edit.

## 6.3 Initial Project Settings

**Display → Window:** 1920×1080, Stretch Mode canvas_items, Stretch Aspect expand.

**Autoload:** Do NOT register Meta.gd yet — it does not exist until Phase 0 creates it. Register it after Phase 0.

**Main Scene:** Do NOT set yet. Set to `GameDirector.tscn` after Phase 4 creates it.

## 6.4 Install GDUnit4

Testing framework. Install via AssetLib in the Godot editor (search "GDUnit4") or clone into `addons/gdUnit4/`.

## 6.5 Install Dialogic 2 (Optional, Recommended)

Dialogue system for narrative scenes. Install via AssetLib. Not used until Phase 9 but installing now prevents later dependency conflicts.

---

# PART SEVEN: THE EXTRACTION PROCEDURE

## 7.1 Four Content Types in Design Documents

Every design document contains a mix of:

| Type | What It Is | Where It Goes |
|------|-----------|--------------|
| **Static data** | Numbers, tables, starting values | Resource files (.tres) |
| **System rules** | Formulas, procedures, conditional logic | GDScript in systems/ |
| **Trigger conditions** | Compound boolean conditions that drive situation generation | TriggerCondition Resources + registration |
| **Narrative content** | NPC dialogue, event text, argument text | Dialogue files, string tables (mostly written fresh) |

Trigger conditions are the category most easily missed. They are scattered across design documents as conditional sentences: "If CI ≥ 30 and a Thread operation occurred within 1 territory of T3 and no Heresy Investigation was opened this season, then..." These must be extracted into declarative data, not hardcoded into logic scripts.

## 7.2 Extraction Worksheet Template

One per source document. Saved in `docs/extraction/`.

```markdown
# Extraction Worksheet: [document name]
## Source: [path in ttrpg repo]
## SHA at extraction: [from canonical_sources.yaml]
## Lines: [count]
## Date: [date]
## Status: NOT STARTED / IN PROGRESS / COMPLETE

---

## STATIC DATA

| Item | Description | Target File | Extracted? |
|------|-------------|-------------|-----------|

## SYSTEM RULES

| Rule | Procedure (step-by-step) | Formula (if applicable) | Source Section | Interactions With | Target Script | Implemented? | Tested? |
|------|-------------------------|------------------------|---------------|-------------------|---------------|-------------|---------|

## TRIGGER CONDITIONS

| Trigger | Condition (full boolean) | Type | Target File | Extracted? |
|---------|------------------------|------|-------------|-----------|

## PATCHES AFFECTING THIS DOCUMENT

| Patch | What Changed | In params file? | In design doc? | In patch register? | Verified? |
|-------|-------------|-----------------|---------------|-------------------|-----------|

## EDGE CASES / OPEN QUESTIONS

| Question | Resolution | Source |
|----------|-----------|--------|

## CANONICAL WORKED EXAMPLES (→ test cases)

| Example | Location in Doc | Inputs | Expected Output | Test Written? | Passing? |
|---------|----------------|--------|-----------------|--------------|---------|
```

Note the SYSTEM RULES table separates "Procedure" from "Formula." A formula is a computation (one-line function). A procedure is a sequence of steps (state machine or multi-step method). Conflating them leads to under-extraction.

## 7.3 How to Read a Design Document

**Pass 1 — Structure map.** Skim the entire document. Note section headers. Identify tables (static data), procedures (system rules), inline patches (`> **P-NN:**` or `> **PP-NNN:**`), philosophical/narrative context (skip for extraction). For documents under 200 lines: 15 minutes. For documents over 500 lines: 45–60 minutes.

**Pass 2 — Data extraction.** Every table row. Every constant. Every starting value. Write into worksheet STATIC DATA. Note whether each value came from base text or a patch.

**Pass 3 — Rule extraction.** Every procedure, formula, conditional. For each rule, write: the formula or procedure in exact terms, what inputs it reads, what outputs it produces, what other rules it interacts with, what edge cases the document addresses, and which it leaves open. This is where you discover the questions.

**Pass 4 — Cross-reference.** Open the corresponding params file. Compare every value. If they disagree, the params file is authoritative for values (it has patches applied). Check `canon/patch_register.yaml` for pending or provisional patches. For any value, check three sources:
1. `references/params_*.md` (highest authority for values)
2. `designs/*/` canonical design doc (highest authority for procedures)
3. `canon/patch_register.yaml` (pending/provisional patches)

**Pass 5 — Worked examples.** Find dice rolls with specific face values and expected outcomes. These are acceptance tests. Record in worksheet.

## 7.4 Source Authority Rules

- For **mechanical values** (numbers, ranges, caps, formulas): the params file wins.
- For **procedures** (step sequences, resolution order, timing): the design doc wins.
- If a **provisional patch** exists: implement the provisional value but mark it `[PROVISIONAL]` in code with a comment referencing the patch ID.
- **Never extract from compilation stages** (compilation/v0.14/*). These are all deprecated. Use design docs and params files.
- Check `references/canonical_sources.yaml` to confirm which document is canonical for each system. Do not extract from a superseded source.

## 7.5 What Not to Extract

- GM guidance sections (become AI logic, not player-facing content)
- Cognitive load analysis (the video game eliminates cognitive load by automating tracking — these docs are historical)
- Compilation stages (deprecated — superseded by design docs)
- Philosophical framing (governs design decisions but does not contain implementable mechanics — reference for visual/narrative design, not GDScript)
- Stress test reports (findings already applied as patches)
- Batch design files (session-specific gap designs — check if gaps are resolved in canonical design docs first; if so, skip the batch file)

---

# PART EIGHT: IMPLEMENTATION PHASES

## Phase 0 — Foundation (1–2 weeks)

No design documents. Build the engine skeleton from the architecture specification.

**Create:** Enums, Constants, Tracker, TrackerRegistry, TrackerThreshold, CoreResolver (both dice variants), RollContext, RollResult, PoolModifier, ObModifier, TrackerBinding, CoreEngine, ConsequenceRouter, Consequence, all five resolution modes, Meta.gd skeleton (registries, `receive_consequence()`), FactionData.gd class, CharacterData.gd class, TerritoryData.gd class.

**Test:** `test_dice_engine.gd` — pool floor, Ob floor, exploding 10s chain, all degree cases (including Ob 20 exception, Overwhelming floor of 3 net), BG dice variant, Momentum gain on Overwhelming, negative net. `test_tracker_registry.gd` — register tracker, apply change, bounds enforcement, seasonal cap, threshold crossing detection.

**After Phase 0:** Register `autoload/Meta.gd` as autoload named "Meta" in Project Settings → Autoload.

## Phase 1 — Core Data Extraction (3–5 days)

**Extract from:** `references/params_core.md` (161 lines)

Static data: TN value table, Ob scale, degree table, attribute list and ranges, derived score formulas, Momentum rules, MS baseline decay rate, Certainty track rules, Reach terminology.

System rules: Momentum auto-success interaction (add to roll, 1 can cancel), MS baseline decay timing.

**Cross-reference:** `references/params_core_history.md` for patch history.

**Test:** Derived score formulas match params_core.

## Phase 2 — Combat Container (2–3 weeks)

**Extract from:** `designs/combat/combat_design_v1.md` (433 lines) + `references/params_combat.md` (285 lines)

Note: personal combat uses pool-split Versus resolution mode (attacker offence pool vs defender defence pool, margin determines hit/damage). It does not use a lookup matrix for hit determination. TN is always 7 (Standard) unless conditions push to 6 or 8. Weapon reach (Short/Long/Ranged) creates advantage/disadvantage. Armour provides damage reduction.

The Leap is a Priority 5 action during combat — when implementing combat, include the hook for Thread operations but do not implement Thread mechanics yet. Reserve Priority 5 as a "call Threadwork System here" placeholder.

Static data: priority table (8 tiers), weapon stats (from params_combat), armour stats, reach interaction rules.

System rules: pool-split allocation (total = Combat Pool, divide freely, min 0 either side), simultaneous declaration → sequential resolution by priority (higher Agility first within priority, ties simultaneous), Versus resolution (attacker offence vs defender defence), damage formula (margin + weapon power − armour reduction), wound threshold (every Health points of accumulated damage = 1 Wound), incapacitation (wounds ≥ ceil(Health/2)), wound Ob penalty (+1 Ob per Wound to all rolls).

**Create:** CombatContainer.tscn + .gd, CombatLogic.gd, PoolSplitSlider, basic combat AI.

**Test:** Pool split bounds, priority ordering, damage calculation, wound thresholds, incapacitation. Any worked examples from combat_design_v1.

## Phase 3 — World Data Extraction (1 week)

**Extract from:** `designs/setting/geography_design.md` (138 lines), `references/params_factions.md` (565 lines), `designs/setting/calamity_radiation.md` (158 lines), `designs/systems/clock_registry.md` (80 lines)

Create all territory, faction, and clock data resources. Register all world-scope and faction-scope trackers in Meta.

All factions registered at startup including dormant ones (with `is_active` flag).

**Test:** All trackers registered with correct initial values. Seasonal cap enforcement. Clock threshold detection. Faction collapse at Stability 0.

## Phase 4 — Game Loop Skeleton (2 weeks)

No new design documents. Build the game director and conflict container.

**Create:** GameDirector.tscn + .gd, ContainerBase.gd, ConflictContainer.tscn + .gd, PersistentUI (ClockDisplay, NotificationFeed), CascadeDisplay (simple text log), SeasonOverview (skeleton: hard-coded single combat scene), Accounting method in Meta.

Wire: season start → overview (auto-confirm) → conflict container → combat → cascade display → accounting → next season.

**After Phase 4:** Set `GameDirector.tscn` as Main Scene in Project Settings → Application → Run.

**>>> FIRST PLAYABLE <<<** One combat encounter per season. World state changes. Clocks advance. Nothing else works.

**Test:** `test_integration.gd` — full season cycle. Consequences flow through ConflictContainer → cascade → accounting → season advances.

## Phase 5 — Threadwork (5–7 weeks)

**The largest extraction.** Extract per operation type, not per document.

**Sources:** `designs/ttrpg/threadwork_redesign_v25.md` (876 lines), `references/params_threadwork.md` (637 lines), `compilation/v0.14/stage11_scale_transitions.md` (137 lines) for scale table and Coherence auto-costs.

**Sub-extractions:**

5a. **The Leap** (1 week) — Eligibility, pool (Spirit + Attunement + History + TPS), TN 7, Ob by TS tier (this Ob formula is unique to the Leap — operations use the scale table Ob instead), degree outcomes, contact duration = Focus.

5b. **Weaving** (1 week) — Pool, scale Ob table, MS consequences (scale-dependent), Coherence auto-cost, over-actualisation at Relational+, overweaving penalty.

5c. **Pulling** (1 week) — Ob by actualization level, duration ladder, Past-Oriented Pulling (TS 70+, MS ≤ 60, TN 8, halved pool for Foundational, fortification Ob addition).

5d. **Mending** (3 days) — Ob by Gap severity, threadcut interference.

5e. **Co-Movement** (1 week) — Three auto-effects on every operation (P-01). Version C for personal phase (deterministic + d6). Card deck (18 cards) for strategic phase. Both produce all three dimensions.

5f. **Combat integration** (3 days) — Wire Priority 5 in CombatLogic to ThreadworkSystem. Thread overlay activation. Immediate MS/Coherence consequences flow through ConflictContainer to Meta. Subsequent combat rounds see updated Ob.

5g. **Coherence track** (3 days) — 10→0 with threshold effects (Dissonant/Fragmented/Fractured/Severed/Crisis). TS-gated branching at 0. Certainty interaction (Coherence 0 → Certainty −1).

5h. **Feedback loop verification** (2 days) — Integration test: Weave drops MS below threshold mid-contact → next operation in same window has updated Ob → Coherence cost from first op applies Ob penalty to second op. Verify the compounding spiral works.

## Phase 6 — Debate Container (3–4 weeks)

**Extract from:** `designs/contest/social_contest_system_v2.md` (404 lines), `references/params_contest.md`

Argument styles, interaction types, Piety Track, Composure/strain, exchange resolution (OpposedSimultaneous mode), contest end conditions, Bond-based corroboration, Domain Echo scope recognition for debate outcomes, Register Shift (scene escalation to combat).

## Phase 7 — Board Game (8–12 weeks)

**The second largest extraction.** Four source documents totaling ~3,200 lines.

**Sources:** `designs/board_game/valoria_bg_v05_simulation_and_patches.md` (734 lines), `references/params_board_game.md` (1,616 lines), `designs/board_game/victory_architecture_v1.md` (472 lines), `designs/board_game/faction_resolutions_2026_04_07.md` (388 lines)

Sub-extractions: card-hand action economy → territory control and Conviction Value → fog of war → faction AI priority trees (one per faction) → battle resolution (OpposedSimultaneous, compare net) → Church seizure mechanics → victory conditions (all factions, all paths, including multi-step mechanics like Crown Treaty which is a substantial subsystem) → strategic-phase Thread orders (Co-Movement Card deck, BG dice variant).

Note: strategic-phase faction Thread orders use BG dice (non-exploding), not TTRPG dice. The RollContext's `action_category` must be set to `FACTION` for these rolls so the CoreResolver uses the correct dice variant.

## Phase 8 — Situation Generator + Full Season Overview (4–5 weeks)

**Sources:** `designs/hybrid/hybrid_gaps_resolved.md` (177 lines), `designs/npcs/npc_roster.md` (450 lines)

Full SituationGenerator, NPC trajectory logic (5 key NPCs for MVP), scene availability builder, full Season Overview UI (map preview, scene selector, order panel), trigger condition registration.

**>>> MVP COMPLETE <<<** Full season loop with combat, debate, Thread, strategic board, fog of war, AI factions, NPC trajectories, victory conditions.

## Phase 9+ — Post-MVP

Mass combat (715 + 535 lines of source). Narrative container + Dialogic integration. Character creation screen. NPC selection screen. Tutorial. Full NPC roster. Alternate victory paths. Southernmost expedition. Content writing (dialogue, argument texts, event descriptions — ~154,000 words).

---

# PART NINE: DAILY WORKFLOW

```
1. Open conversion ledger. Find current phase, next unextracted item.
2. Open extraction worksheet for current document.
3. Open source document (local clone or GitHub).
4. Extract: create Resources, implement rules, write tests.
5a. Run tests for current system. Fix failures.
5b. Run FULL test suite. If any previously passing test fails,
    the new code introduced a regression. Fix before proceeding.
6. Update extraction worksheet (Extracted/Implemented/Tested columns).
7. Update conversion ledger.
8. Commit with source reference:
   [phase/system] description — source doc §section, patch refs
9. Push.
```

---

# PART TEN: VERIFICATION

## 10.1 Three Verification Criteria

**Data verification.** Every value in `.tres` files matches the canonical params file. Open both. Compare field by field.

**Rule verification.** Every formula in GDScript matches the canonical design doc. Write tests with known inputs and hand-calculated expected outputs.

**Worked example verification.** Every canonical worked example (dice rolls with specific face values and expected outcomes from bg_v05, threadwork_v25, combat_design_v1, social_contest_v2) passes as a test case with deterministic dice. This is the gold standard. If a worked example fails, either your implementation or your understanding is wrong.

## 10.2 Canonical Examples Test File

`tests/test_canonical_examples.gd` — one test per worked example. Uses mocked/seeded RNG to produce deterministic dice faces. Tests the full pipeline: context assembly → resolution → consequence routing → tracker changes.

There are approximately 15–20 worked examples across the canonical documents. These are your acceptance tests. The conversion is not complete until all pass.

## 10.3 When You Get Stuck

1. Check the params file (authoritative for values, patches applied).
2. Check `canon/patch_register.yaml` (search by keyword for affecting patches).
3. Check `canon/editorial_ledger.yaml` (some ambiguities are known and unresolved).
4. If the ambiguity is structural: implement the most mechanically defensible interpretation, mark `[PROVISIONAL: ED-NNN]` in code, note in extraction worksheet, and move on.

---

# PART ELEVEN: QUICK REFERENCE

| If you need... | Look in... |
|----------------|-----------|
| A mechanical formula or value | `references/params_*.md` in design repo |
| A procedure or resolution sequence | `designs/*/` canonical design doc in design repo |
| Which doc is canonical for a system | `references/canonical_sources.yaml` in design repo |
| Whether a patch exists | `canon/patch_register.yaml` in design repo |
| Patch history for a system | `references/params_*_history.md` in design repo |
| An open editorial decision | `canon/editorial_ledger.yaml` in design repo |
| The architecture specification | `docs/architecture.md` in game repo |
| What has been extracted | `docs/conversion_ledger.md` in game repo |
| Extraction status of one doc | `docs/extraction/[name].md` in game repo |
| All trigger conditions | `docs/trigger_catalogue.md` in game repo |
| Project settings | `project.godot` in game repo root |
| The single autoload | `autoload/Meta.gd` |
| Resource class definitions | `resources/data_types/*.gd` |
| Resource data instances | `resources/instances/**/*.tres` |
| Game logic (no scene tree) | `systems/**/*.gd` |
| Scenes and scripts | `scenes/**/*.tscn` + `*.gd` |
| Tests | `tests/*.gd` |

---

# PART TWELVE: TIMELINE SUMMARY

| Phase | Duration (Solo) | Milestone |
|-------|----------------|-----------|
| 0: Foundation | 1–2 weeks | Engine skeleton, tracker system, dice resolver |
| 1: Core data | 3–5 days | Attributes, derived scores, TN/Ob/degree rules |
| 2: Combat | 2–3 weeks | First container, pool-split, priority resolution |
| 3: World data | 1 week | Territories, factions, clocks registered |
| 4: Game loop | 2 weeks | **First Playable** — one combat/season, clocks advance |
| 5: Threadwork | 5–7 weeks | Leap, Weave, Pull, Mend, co-movement, feedback loop |
| 6: Debate | 3–4 weeks | Social contest system, Piety Track |
| 7: Board game | 8–12 weeks | Strategic map, AI factions, orders, victory |
| 8: Situation gen | 4–5 weeks | **MVP** — full season loop, all systems, NPC arcs |
| 9+: Post-MVP | Open | Mass combat, narrative, content, polish |
| **Total to MVP** | **~28–38 weeks** | |
