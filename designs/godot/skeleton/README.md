# Valoria — Godot 4 Core Skeleton

The load-bearing reference code for the consolidated architecture
(`designs/godot/consolidated_architecture_v1.md`). This is the **core framework** — the
part that never changes to add content. Engines and modules are added as data + small
scripts on top of it.

> **Status:** reference skeleton. Port the Python reference (`sim/`) into the engine
> bodies; generate the `.tres` engine/module manifests from `references/module_contracts.yaml`.

## The three requirements → the three core pieces

| Requirement | File |
|---|---|
| **(1) Wrapper that organizes all systems** | `core/valoria_kernel.gd` (autoload) |
| **(2) Framework orchestrating all systems via a vectorized key-system, all directions** | `core/key_bus.gd` (autoload) + `core/key.gd` + `core/conviction_axis.gd` |
| **(3) Each system is a base engine that hosts many modules** | `core/base_engine.gd` + `core/engine_module.gd` |

Supporting: `core/key_type_registry.gd`, `core/mechanics_registry.gd`, `core/game_state.gd`.

## How it fits together

```
ValoriaKernel (boot, loop, zoom stack, save)
  ├─ loads KeyTypeRegistry  (data/key_types/*.tres)         — valid Key types
  ├─ loads MechanicsRegistry (data/engines/*.tres)          — discovers engines + modules
  └─ builds engines → each BaseEngine.setup() subscribes its consumed Key types on the KeyBus

gameplay:
  an engine/module resolves a container outcome → KeyBus.emit_key(Key)
  KeyBus.emit_key runs the SINGLE UPDATE RULE:
    validate → append to log → resolve observers (all directions) →
    each observer interprets via its 4-axis armature → subscribed engines consume →
    causal graph updated
  → the outcome is felt at every scale that the Key's targets/scale_signature/visibility reach.
```

## Autoload registration (`project.godot`)

```ini
[autoload]
GameState="*res://core/game_state.gd"
KeyTypeRegistry="*res://core/key_type_registry.gd"
MechanicsRegistry="*res://core/mechanics_registry.gd"
KeyBus="*res://core/key_bus.gd"
ValoriaKernel="*res://core/valoria_kernel.gd"
```

(Order matters: GameState and the registries before KeyBus; KeyBus before the Kernel.)

## Adding things — zero core edits

- **A new combat action / contest style / thread op** → a new `EngineModule` subclass
  (see `engines/combat/modules/strike_module.gd`) + its `.tres` manifest in the engine's
  folder. The engine dispatches to it by the Key types it declares it `consumes`.
- **A new engine** → a `BaseEngine` subclass (see `engines/combat/combat_engine.gd`) + an
  engine `.tres` manifest + a `mechanics_index.yaml` entry. The Kernel instantiates it from
  the registry.
- **A new Key type** → a `.tres` in `data/key_types/` + a registry entry.

## Worked example

`engines/combat/` shows the whole pattern: `CombatEngine` (a `BaseEngine`) hosts
`StrikeModule` (an `EngineModule`). Strike consumes `scene.combat_action.strike`, runs a
`DICE_POOL` resolver seeded per-Key (replay-deterministic), and emits `scene.combat_hit`
carrying a write-protected `health` delta as a `stat_delta` on the defender target — so the
wound rides the substrate, never a direct write (the F1 guard). When a fight ends,
`CombatEngine` emits `scene.combat_resolved`, which the bus delivers up to factions, sideways
to witnesses, and into NPC memory — automatically.

## Validate

```bash
godot --path . --check-only --script res://core/key_bus.gd --headless --quit
```

## Conformance

Each ported engine is checked against this shape by the Engine-Shape Conformance
methodology (wrapper / keys / scalars / vectors / plugins / evolvability) — the audit
layer that keeps every engine honest as the game grows.
