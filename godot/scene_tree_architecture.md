# Phase 5.4 — Godot Scene Tree Architecture

> **⚠️ STALE / PARTIALLY SUPERSEDED (flagged 2026-06-30).** Dated 2026-04-18 — pre-`d+σ`, pre-LPS-2e.
> **Do not implement from this doc.** The governing Godot spec is
> `godot/godot_conversion_strategy_v1.md` (itself PROPOSED).
> Tracked by ED-1054.

# Date: 2026-04-18
# Maps UI/UX v4.1 §1.1 states to Godot scene tree

---

## Scene Tree

```
root (Node)
├── Autoloads (always loaded)
│   ├── DiceEngine          — pool resolution
│   ├── GameState           — all tracked state
│   ├── SeasonManager       — season loop, phase transitions
│   ├── SceneSlateManager   — scene generation + routing
│   ├── NPCAIManager        — priority trees, arc state machines
│   ├── VictoryManager      — condition checking
│   └── AudioManager        — music, SFX
│
├── UILayer (CanvasLayer, z=10 — persistent chrome)
│   ├── TopBar              — season counter, MS/CI/IP indicators, faction emblem
│   ├── NotificationQueue   — event popups, Scene Slate alerts
│   └── PauseMenu           — settings, save/load, quit
│
├── ModalLayer (CanvasLayer, z=20 — popups over everything)
│   ├── DialoguePanel       — NPC conversation, Belief reveal
│   ├── ContestPanel        — exchange UI, Piety Track display
│   └── ResultsPanel        — combat aftermath, contest outcome
│
└── MainScene (Node2D — swapped per game state)
    ├── MainMenuScene
    ├── CharacterCreationScene   — lifepath 4-stage wizard
    ├── BriefingScene            — season briefing, clock display
    ├── SceneSlateScene          — scene selection from generated slate
    ├── PersonalPhaseScene       — routes to subscenes:
    │   ├── FieldworkScene       — exploration, investigation, socializing
    │   ├── CombatScene          — round-by-round combat
    │   ├── ContestScene         — exchange-by-exchange contest
    │   ├── ThreadworkScene      — Leap, operations, Co-Movement
    │   ├── GovernanceScene      — settlement management
    │   └── CompanionScene       — companion interaction
    ├── StrategicPhaseScene      — faction AI resolution (animated map)
    ├── AccountingScene          — 13-step cascade (player watches results)
    ├── AftermathScene           — Conviction revision, Standing, Renown
    ├── PeninsulaMapScene        — territory overview (BG layer)
    │   └── SettlementMapScene   — province zoom (settlement nodes)
    └── EndgameScene             — victory/defeat summary
```

## Scene Transitions

| From | To | Trigger | Signal |
|------|-----|---------|--------|
| MainMenu | CharacterCreation | "New Game" | `game_started` |
| CharacterCreation | BriefingScene | Lifepath complete | `character_created` |
| Briefing | SceneSlate | Player ready | `briefing_acknowledged` |
| SceneSlate | PersonalPhase/* | Scene selected | `scene_selected(type)` |
| PersonalPhase/* | SceneSlate | Scene resolved | `scene_resolved` |
| SceneSlate | StrategicPhase | All actions used | `personal_phase_complete` |
| StrategicPhase | Accounting | AI turns done | `strategic_phase_complete` |
| Accounting | Aftermath | Cascade done | `accounting_complete` |
| Aftermath | Briefing | Next season | `season_complete` |
| Any | EndgameScene | Victory condition | `victory_achieved(faction)` |

## CanvasLayer Hierarchy
- z=0: MainScene (game world)
- z=10: UILayer (persistent HUD)
- z=20: ModalLayer (dialogue, contest, results)
- z=30: PauseMenu (above everything)

---

# Phase 5.5 — Cross-Repo Propagation Protocol
# Date: 2026-04-18

## Repos
- `jordanelias/ttrpg` — design source of truth (this repo)
- `jordanelias/valoria-game` — Godot implementation

## Protocol

### 1. Design → Implementation Tagging
Every ttrpg commit that affects Godot implementation includes:
```
[GODOT-IMPACT: system] description
```
Where `system` is one of: `dice`, `state`, `season`, `fieldwork`, `combat`, `contest`, `threadwork`, `mass_battle`, `npc_ai`, `settlement`, `victory`, `ui`.

### 2. Propagation Map Extension
`references/propagation_map.md` gains a "Cross-Repo Propagation" section:
```
## Cross-Repo Propagation (ttrpg → valoria-game)
| ttrpg Commit | System | Impact | valoria-game Status |
|-------------|--------|--------|-------------------|
| abc1234 | combat | Weapon TN changed | PENDING |
```

### 3. valoria-game Sync Tracking
`valoria-game` maintains `design_sync.md`:
```
# Design Sync Status
ttrpg_current_sha: abc1234def5678
last_sync_date: 2026-04-18
pending_impacts:
  - combat: weapon TN change (ttrpg abc1234)
```

### 4. Sync Verification
Before any valoria-game release:
1. Check `design_sync.md` → all pending impacts resolved
2. Run `init_validator.py` against current ttrpg params files
3. Flag any discrepancy between Godot resource values and design doc values

### 5. Conflict Resolution
If a Godot implementation discovers a design issue:
1. File ED item in ttrpg `canon/editorial_ledger.yaml`
2. Tag with `[GODOT-DISCOVERY]`
3. Resolve in ttrpg first, then propagate to valoria-game
Design docs are always authoritative. Implementation does not override design.
