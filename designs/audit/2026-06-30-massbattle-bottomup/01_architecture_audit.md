# Mass-Battle Engine — Architecture Audit

**Date:** 2026-06-30 · **Target:** `tests/sim/mass_battle/` (live engine) · **Directive (2):** audit the
code architecture against wrapper-vs-engine separation and proper module decomposition.

`[SELF-AUTHORED — bias note: engine is largely Claude-authored; verdict-first, no false balance. Line
numbers verified against the working tree at HEAD 955db15.]`

---

## 0. Verdict

The engine's **spatial substrate is genuinely bottom-up and well-grounded** (cells → Lanchester
linear/square → octagon facing → du-Picq fatigue/morale σ → per-subunit rout/stamina). The
architectural defects are real and concentrated in **three seams**:

1. **No true wrapper.** `engine.py` (74 L) is a namespace re-exporter (`from mass_battle.X import *`)
   plus a `MECHANICS` registry. It resolves nothing, adapts nothing, routes nothing.
2. **A god-file resolver.** `orchestration.py` (**2,899 L**) owns the data model *and* targeting
   physics *and* attrition-law authoring *and* volley *and* outcome resolution *and* the turn loop
   *and* post-battle I/O. The nominal "core resolver" `resolution.py` (121 L) holds only the σ head.
3. **Inert behavioral modules.** Troop types, formations, tactics, and strategy exist only as data
   dicts (`config.TROOP_TYPE_ROLES` L148, `ROLE_SPEC` L164) or shape-name `if`-switches
   (`geometry.cell_speed` L335), never as wired modules with interfaces.

The fix is a **full clean module split** that enforces *wrapper resolves nothing · core resolves only ·
every module wired*, built up from named atoms. The good news: the migration is ~⅓ done (the package
split exists; Lanchester and per-subunit substrate are landed), so this is completing a trajectory, not
a greenfield.

---

## 1. Current structural map (verified line ranges, `orchestration.py`)

| Concern (should not all live here) | Symbols | Lines |
|---|---|---|
| Phase-boundary hooks | `morale_check_phase`, `rout_resolution`, `discipline_check_phase` | 290 / 317 / 339 |
| **Data model** | `class Subunit`, `class Unit` | 534 / 1235 |
| **Command-pool derivation** | `derive_command`, `command_base_pool`, `subunit_combat_pool` | 1182 / 1194 / 1203 |
| **Targeting physics** | `assign_targets`, `resolve_cross_side_contention`, `find_contacts` | 1386 / 1419 / 1535 |
| **Attrition-law authoring** | `_lanchester_strength` | 1652 |
| **Outcome resolution** | `resolve_engagements`, `resolve_engagements_cascading` | 1670 / 1978 |
| **Ranged resolution** | `volley_phase` | 2087 |
| **Battle loops + I/O** | `run_battle`, `run_multi_turn_battle`, `run_multi_unit_battle` | 2178 / 2477 / 2636 |

Seven distinct responsibilities in one flat namespace. A test touching one mechanic loads all 2,899
lines; a toggle is a scattered module-level `PC_*`/`SIGMA_*`/`MORALE_*` constant read at import.

`engine.py` (L6–10) re-exports the five modules and (L29–65) registers 29 mechanics with
`{fn, toggle, source, status}`. The registry is the seed of a real public surface but performs no
wrapper duty (no adapter, no router, no I/O contract).

---

## 2. Principle-by-principle assessment

### P1 — The wrapper must not conflate duties with engines

**FAIL.** There is no wrapper layer. The faction→unit construction lives in the *gauge*
(`gauge_mb.make_unit`/`make_mixed_unit`) and in `Subunit.of_type` (orch L638); battle-type routing is
three separate top-level entry points (`run_battle` / `run_multi_turn_battle` / `run_multi_unit_battle`);
I/O is inlined in those loops. The "wrapper" (`engine.py`) only forwards names.

**Target:** `engine.py` becomes the wrapper with exactly three non-resolution duties — (1) faction→unit
**adapter** (`build_side(roster, granularity)` drawing stats from `troop_types`, layout from
`formations`, posture from `doctrine`); (2) battle-type **router** (`resolve_battle(sides, kind)`
replacing the three entry points); (3) **I/O** (result dataclasses, the `MECHANICS` registry, trace
plumbing).

### P2 — The core engine is for resolving only

**FAIL.** Resolution is split across `resolution.py` (σ head) **and** `orchestration.py`
(`resolve_engagements` L1670, `_lanchester_strength` L1652, `volley_phase` L2087, phase hooks L290–339)
**and** `percell.py` (casualty distribution). Worse, the resolver *authors* the attrition law
(`_lanchester_strength` reads module-level `K_LINEAR` directly, orch L1652 → config L125) and *knows
troop concepts* (volley density, charge). A resolver should apply injected laws and compose injected
modifiers, knowing nothing of "charge" or "formation".

**Target:** a `core/` package — `exchange.py` (roll → degree → σ head → casualty magnitude),
`attrition.py` (Lanchester **application** with coeffs injected), `state.py` (the **sole** site that
mutates morale/discipline/rout), `contact.py` (the contact-event dataclass). Interface:
`core.resolve_exchange(contact, atk_state, dfn_state, laws, mods) → ExchangeResult` — `laws` and `mods`
are injected by their owning modules; the core never reaches up the DAG.

### P3 — Distinct modules for troop types, formations, tactics, strategies, cells, unit/subunit

**FAIL (data-only) / PARTIAL (cells).** Inventory of the would-be modules:

| Module | Today | Verdict |
|---|---|---|
| troop types | `TROOP_TYPE_ROLES`/`ROLE_SPEC` dicts (config L148/164); `TROOP_TYPE_STATS`/`stats_for`/`of_type` (orch, ED-1018) | stats wired; **roles inert** |
| formations | `CELL_PATTERN_FN` + `*_cells` generators (geometry L9–80) | pattern-generators, not a `Formation` object; effects partly in hardcoded `cell_speed` |
| tactics | — | **absent**; 4 in-scope GAPs (feigned-retreat, ambush, hammer&anvil, skirmish) per `mb_engine_completeness_audit.md` |
| strategy/doctrine | only `Unit.stance` (orch L1253) | **absent**; Aggression/Cohesion unbuilt |
| cells | `_ColBlock` (percell L10), `build_column_grid` (percell L25), octagon (geometry) | **WIRED, genuinely bottom-up** |
| unit/subunit hierarchy | `Subunit`/`Unit` (orch L534/1235) | exists but **anatomical, not tactical** — subunit carries own stats (ED-1016/17/19) yet is inert in default mode; resolution operates on the unit pool |

**Target:** `troop_types/`, `formations/`, `tactics/`, `doctrine/`, `cells/`, `hierarchy/` — each a
behavioral module with an interface, emitting **cells + intents + injected mods**, never outcomes and
never flat σ.

### P4 — Granular, modular, bottom-up emergent from primitives

**PARTIAL.** Space is bottom-up (cells/Lanchester/du-Picq-σ/octagon); **time is top-down scripted**
(the phase loop in `run_battle` is an imperative sequence, not composed from sub-mechanics); and
formation effect partly lives in shape-name switches. The retirement of `SHAPE_OFF_MOD`/`SHAPE_DEF_MOD`
(config L58) is the proof-of-discipline that the rest must follow.

### P5 — Primitives grounded in evidentiary sources

**PARTIAL** — see `02_antipattern_census.md` / `03_provenance_ledger.md`. Laws are excellently grounded
(Lanchester, du Picq, cavalry bands); a cluster of *values* is asserted/calibrated.

### P6 — Emergent results validated top-down by historical data; multi-scale

**PARTIAL.** The gauge validates 11 bands top-down (good), but only at unit scale and only in `multi`
mode; the subunit layer is inert in default runs, so "unit vs subunit vs cell" is not exercised as a
first-class capability (see `04_validation_and_scale.md`).

---

## 3. Target architecture (the dependency DAG)

```
config + provenance
        │
        ├──► cells/{cell, geometry, kinematics}
        ├──► troop_types/{troop_atom, registry}
        │            │
        │            ▼
        └──► formations/formation ◄── cells
                     │
   ┌─────────────────┼───────────────────┐
   ▼                 ▼                    ▼
core/{contact,     doctrine/doctrine   (mods injected)
 exchange,             │
 attrition,            ▼
 state}            tactics/tactic
        └──────────────┬───────────────┘
                       ▼
              orchestration.py   (phase/turn loop ONLY — calls core)
                       ▼
                  engine.py      (WRAPPER — adapter + router + I/O)
                       ▼
                 gauge_mb.py / callers
```

No cycle. **The core depends on `cells` + `troop_types` but not on `formations`/`tactics`/`doctrine`** —
those feed it cells + mods + intents. This is the structural guarantee of "core resolves only": the
resolver sits *below* the strategic layers and cannot reach up to ask "what formation is this?".

**Atoms (DAG base):** `cell` (r,c + density + stamina + depth + facing), `troop-atom` (per-soldier
Power/DR/drill/lethality-per-degree), `contact-event`, `exchange`, `morale-state`, `velocity/momentum`.
**Composition:** `troop-atom + cell → subunit → unit → side/army`; `formation` = arrangement of cells;
`tactic` = a Command-run maneuver over units; `doctrine` = army posture conditioning tactics.

---

## 4. Migration map (what moves where) — for Stage 1

| From `orchestration.py` | To |
|---|---|
| `resolve_engagements`(_cascading) L1670/1978 | `core/exchange.py` |
| `_lanchester_strength` L1652 + volley square term (in `volley_phase` L2087) | `core/attrition.py` |
| phase hooks L290–339 (`morale_check_phase`, `rout_resolution`, `discipline_check_phase`) | `core/state.py` |
| `Subunit`/`Unit` L534/1235 (resolution methods stripped out) | `hierarchy/units.py` (data) |
| `assign_targets`/`find_contacts`/`resolve_cross_side_contention` L1386/1535/1419 | `cells/geometry.py` + `core/contact.py` |
| `derive_command`/`command_base_pool`/`subunit_combat_pool` L1182/1194/1203 | split: derivation → `troop_types`/`hierarchy`; pool assembly → `core/exchange` |
| `run_battle`/`run_multi_*` L2178/2477/2636 | wrapper `engine.resolve_battle(sides, kind)`; the per-turn loop stays in `orchestration.py` as the only thing it does |

**Reuse, don't rebuild:** `footprint_for` (geometry L122) is already the allocation→cells solver;
`_support_along_vector` (geometry L186) is the generative form of `SUPPORT_WEIGHTS`; `build_column_grid`
(percell L25) already derives frontage/depth from the live cell footprint; `Subunit.of_type` +
`TROOP_TYPE_STATS` (ED-1018) already wire troop-type stats; the `pc_formation_system.md` §7 mapping is
the formations/tactics/doctrine design.

---

## 5. Acceptance for the Stage-1 refactor (pre-stated, byte-exact)

A pure structure refactor with **zero behavior change**: `PER_CELL=0` reproduces the current engine
**byte-exact**; `PER_CELL=1` is **numerically identical** on all 11 gauge bands; the `MECHANICS`
self-test (`engine.mechanics_selftest`) stays green; no module imports up the DAG (enforced by an
import-direction check in G1). Any digest divergence is a refactor bug, not a tuning question.
