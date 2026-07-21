# sim reference — Valoria simulation armature (relocated)

> **RELOCATED 2026-07-21 (ED-IN-0071 P4 continuation — sim/ hollow-out).** The `sim/` tree is
> fully emptied. Its residual subpackages moved to their subsystem/engine homes: `sim/peninsular/`
> → `systems/overview/sim/`, `sim/personal/{conviction,beliefs,companion}` →
> `systems/characters/sim/`, `sim/personal/tribunal` + `sim/provincial/home_sanctuary` →
> `systems/factions/sim/`, `sim/tests/` → `engine/tests/`. The engine core (`substrate`,
> `autoload`, `cross_scale`, `mc_v18`) already lives in `engine/` (P3 Phase A). This doc is kept
> for orientation; the subpackage map below describes the pre-move layout — resolve live homes via
> `CURRENT.md` and `references/restructure_ledger.md`.

**Status:** scaffold (Pass 2l, 2026-05-17). All modules are stubs. **Stale caveat (see CLAUDE.md §7):**
this understates progress — many modules are real and `mc_v18.py` runs full campaigns.

## Not the same as tests/sim/ or tests/sim_framework/

Three directories collide on the word "sim" but are not duplicates — don't move content between them
without checking which one you actually mean:

- **`sim/`** (here) — the canonical Python Monte-Carlo reference implementation the GDScript port is
  built from. Its own regression tests live at `sim/tests/` (pytest, wired into CI — see CLAUDE.md §8).
- **`tests/sim/`** — unrelated to this package. It's *largely* a frozen archive of historical sim-*run*
  output (reports + one-off scripts from specific past simulation runs, e.g. `sim_mass_battle_SIM-MB-05.md`).
  This directory predates `sim/` — it held the prior monolithic `mc_v17.py` orchestrator that `sim/`
  replaced (see below). It's load-bearing for tooling: `ci_sim_fabrication_check.py`,
  `atomization_rules.yaml`, and `lane_assignments.yaml` all path-match on the literal `tests/sim/` prefix.
  ⚠️ **Not uniformly frozen (audit ED-IN-0074 D5):** `tests/sim/mass_battle/` is a **more-developed but
  disconnected** multi-unit battle engine (formations / collision / Lanchester, last advanced 2026-07-08),
  *not* run-output — and the wired `resolve_mass_battle` (`systems/mass_battle/sim/`) does not call it.
  Reconcile the two before porting the mass-battle slice; don't treat this subtree as dead history.
- **`tests/sim_framework/`** — a separate, earlier sim-harness attempt (its own `engine.py`/`state.py`),
  not consumed by `sim/` or by `mc_v18.py`.

## Purpose

Replaces the prior monolithic `tests/sim/v17-integration/mc_v17.py` orchestrator
with a modular armature mirroring `godot/scene_tree_architecture.md` 1:1.
Each canonical mechanical system has a dedicated module under one of the eight
subpackages.

The armature lets game-mechanic implementation proceed against a clean,
canon-aligned scaffold rather than continuing to grow a single Python file.
Maps directly to the Godot scene tree so that GDScript ports of each module
can be built from the Python reference implementation.

## Subpackage map

| Subpackage | Scope | Maps to Godot scene |
|---|---|---|
| `autoload/` | Global services — dice, state, season manager, victory check, mechanics registry | Godot Autoloads (DiceEngine, GameState, SeasonManager, VictoryManager, NPCAIManager, SceneSlateManager) |
| `personal/` | Character-scale: combat, contest, tribunal, parliamentary vote, fieldwork, investigation, conviction, beliefs, knots, companion | PersonalPhaseScene + subscenes |
| `thread/` | Thread layer: operations, collective, opposing, coherence, co-movement, rendering, threadcut | ThreadworkScene |
| `provincial/` | Mass battle + provincial-scale faction actions | StrategicPhaseScene + provincial subsystems |
| `territory/` | Settlement + infrastructure + adjacency + temperaments | SettlementMapScene |
| `peninsular/` | Strategic-scale world tracks (CI, RS, MS, IP) + season/accounting | PeninsulaMapScene + AccountingScene |
| `world/` | Background processes: Restoration Movement PT decay, miraculous events, insurgency pipeline, NPE | World-level autoload state |
| `cross_scale/` | Domain Echo, Zoom In/Out, Handoff Rules, Articulation Layer | Cross-scene message bus |

## Module conventions

See `sim/CONVENTIONS.md`. Every module declares:
1. Canon source doc (path under `designs/`)
2. Params source (path under `params/`)
3. Game Design constraints applicable (GD-1, GD-2, GD-3, …)
4. Dependencies on other sim modules
5. Public entry-point function signatures
6. Provisional / canonical / contested status flag

## Game Design constraints binding the armature

- **GD-1** (peninsula-only victory) — enforced in `sim/autoload/victory.py`. No
  other module produces game-end victory triggers. Faction-specific actions
  produce stat/territorial effects only.
- **GD-2** (deterministic threat response) — enforced in
  `sim/provincial/faction_action.py` mandatory-actions pass before stochastic
  candidate generation.
- **GD-3** (insurgency pipeline) — implemented in
  `sim/world/insurgency_pipeline.py`. Promoted-RM gets
  `parliamentary_status=extra` flag enforced in `sim/personal/parliamentary_vote.py`.

## Mechanics index

`registers/mechanics_index.yaml` (Pass 2j, pending) is the authoritative registry
mapping each mechanic to its `sim_module` path. Load via `sim/autoload/registry.py`.

## Status flags

Module docstring `Status:` field uses one of:
- `[PROVISIONAL — <reason>]` — stub or untested; canon source not yet fully
  consumed
- `[VERIFIED — N≥<n>]` — sim output validated against canonical expectation at
  the stated sample size
- `[CONTESTED — <reason>]` — implementation depends on canon claim that may be
  contaminated per Jordan diagnosis 2026-05-17; awaiting audit
- `[CANONICAL — N≥<n>, GD-<n>-compliant]` — verified at scale, GD-constraint-tested

All Pass 2l stubs ship as `[PROVISIONAL]`.

## What this scaffold does NOT do

- Author identity / flavor / world-building content (out of scope per Jordan
  directive 2026-05-17)
- Make claims about contested faction-identity traits (per contamination audit
  pending)
- Implement victory triggers beyond `peninsular_sovereignty()` (per GD-1)
