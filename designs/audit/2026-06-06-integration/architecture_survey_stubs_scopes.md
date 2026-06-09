# Architecture Survey — Modularity / Keys / Requirements Confirmation + Missing-Stub/Scope Map

**Status:** Audit / architecture survey. Class-C findings, Jordan-vetoable.
**Date:** 2026-06-06. **Scope:** the `sim/` engine (72 modules) and its supporting tooling, surveyed against the corrected target (single peninsula-control victory by elimination/diplomatic subjugation + the dynamic substrate: card-driven actions, worldly events, domain echoes, real faction-state → mass battle).
**Method:** full module inventory + status scan; AST layering graph (prior Stage-3 survey); schema + keying + determinism read; scope-vocabulary read from the live hook code.

`[READ:]` full `sim/` tree (72 modules, status-grouped) · sim/autoload/game_state.py (schema, registries, keying, serialization, hash-seed fixes) · valoria_hooks.py (TASK_REQUIRED_FILES, COMMIT_FORMAT) · github_ops.py (SESSION_SCOPES) · module headers for treaty / domain_echo / tactic_cards / miraculous_event / varfell_* (impl-vs-stub).

---

## §A — MODULAR ARCHITECTURE — CONFIRMED (sound, localized smells)

Yes, the engine is modular and the layering is correct.

- **Scale-layered with a shared spine.** `autoload/` (spine: game_state, dice_engine, season_manager, scene_slate, victory, registry) → scale layers (`personal/`, `provincial/`, `territory/`, `peninsular/`, `thread/`, `world/`) → `cross_scale/` (bridge) → `mc_v18` (driver). AST import direction is correct: scale layers depend on the spine, the bridge depends on what it connects, the driver orchestrates; no leaf-depends-on-driver inversion.
- **Repo separation** holds: `ttrpg` (design + this sim) vs `valoria-game` (Godot implementation).
- **Registry pattern**: per-subsystem state lives on `World` as keyed registries with a `_store(world)` router and module-level fallback — modular, with the deliberate trade-off below (§C).

Localized smells (carried from the Stage-3 survey, none architecture-breaking):
- **Spine inversion** — `game_state` lazy-imports 9 leaf modules in `from_dict` (import-safe; docstring "root primitive — none" is drift). Low–med.
- **`massbattle.py` = 1905L god module** (bare port of a 2143L monolith). Med — the one module that should be decomposed.
- **Status hygiene** — 32/72 stub + 28 untagged: over half the package is provisional or status-unclear (see §D).

Verdict: **modular — pass.** The structure is the right shape for the Godot target; the work is filling and wiring, not re-architecting.

---

## §B — KEYS — CONFIRMED (consistent + deterministic post-fix)

- **Entity keys:** `factions: dict[str→Faction]` keyed by name (`'Crown'…`); `territories: dict[str→Territory]` keyed by `tid` (`'T1'…'T17'`); `clocks: dict[str→float]` keyed by clock name.
- **Registry keys (heterogeneous but consistent per registry):** `actor_id` (practitioners, convictions, beliefs), `insurgency_id`, `knot_id`, `being_id`, `territory_id` (npcs, infrastructure, drift), `frozenset[tid]` (uncontrolled_streaks), `frozenset[parties]` (treaties).
- **ID schemes:** `ED-NNN` (editorial), `PP-NNN` (patches), `T`-IDs (territories), `S-001…S-037` (settlements). The editorial ledger keys on `ED-<int>` (the jsonl gate flags a handful of non-standard `PP-NPC-*` ids — pre-existing data hygiene, not structural).
- **Determinism — the load-bearing key fact, and it is handled.** String-keyed *sets* iterate in `PYTHONHASHSEED`-dependent order, which previously produced cross-process variance in `run_batch`. Fixed (2026-05-20): `Faction.territories` set→list (insertion-ordered), conquest adjacency `sorted()` before `rng.choice`, and `frozenset` registry keys serialized as sorted-lists for deterministic round-trip. Combined with the `world.rng` threading through the battle engine, batches are now byte-identical at a given seed.

Verdict: **keys — pass.** One forward note for the corrected victory model: factions are keyed by *name*, so "elimination" = removing the faction from `world.factions`; any code iterating factions (the action callback, fallback, the new elimination/subjugation victory check) must tolerate a faction being absent or flagged eliminated rather than assuming all four persist.

---

## §C — OTHER ENGINE / CODE-ARCHITECTURE REQUIREMENTS

- **Determinism:** confirmed (rng threaded end-to-end; byte-reproducible at seed; the hash-seed hazards fixed). Pass.
- **Serialization / persistence:** `serialize_world` / `restore_world` present, with frozenset-key encoding and lazy type-imports for subsystem dataclasses. Pass (the lazy imports are the §A spine-inversion smell, not a correctness fault).
- **Godot-implementability** (`design_doc_framing`): the strategic loop is pure engine logic with no presentation coupling, and the personal-scale scenes are the intended UX surface — the engine/UI separation supports the Godot port. The sim is the Python reference; `valoria-game` consumes it. Pass (not exercised here).
- **Type safety trade-off:** registry values are `Any`-typed to avoid import cycles (subsystem dataclasses live in their own modules; bidirectional typing would cycle). Consumers type-check at runtime. Acceptable, deliberate, documented — but it is why the spine reaches back into leaves for deserialization.

---

## §D — MISSING STUBS (gap map against the corrected target)

Surveyed against the corrected requirements. "Stub" = exists but unimplemented; "no module" = absent; "unwired" = implemented but not connected to the path that needs it. Worst-first.

1. **Elimination / diplomatic-subjugation victory — NO MODULE + UNWIRED.** There is no faction-elimination terminal anywhere, and `victory.py` reads only territory/accord/PS — never `world.treaties`. `treaty.py` (157L) is *implemented* but disconnected from victory, so subjugation-by-treaty cannot win. This is the single largest gap: the canonical sole victory has no implementation. (Build the elimination/subjugation victory check; wire `treaties` + rival-elimination status; retire the GD-1 territorial proxy + the fallback.)
2. **Card economy — STUB (`provincial/tactic_cards.py`, 33L).** The deterministic+stochastic card-driven faction-action system is unbuilt; `faction_action.py` uses a hardcoded probability mix (`M7_ASSUMPTION_SIX`). (Build the card system; replace the probability placeholder.)
3. **Worldly events — STUB (`world/miraculous_event.py`, 21L; `world/restoration_movement.py`, 27L).** No event channel feeds faction stats. (Build the event system → stat effects.)
4. **Domain-echo → faction-stat wiring — IMPLEMENTED BUT UNWIRED (`cross_scale/domain_echo.py`, 208L).** The echo machinery exists; the season loop / scene seam does not apply echoes to faction stats (outcome→echo mapping unbuilt — prior integration audit). (Wire scene outcomes → domain echoes → faction-stat deltas.)
5. **Faction-state → mass-battle unit mapping — GAP.** `_faction_to_unit` collapses every faction to `power = round(Mil)` with constant troops/command/discipline/morale. The richer mapping (via `domain_echo` + accounting, the code's "Phase 7 Step 10") is unbuilt; `run_multi_unit_battle` exists but conquest uses single-encounter `run_battle`. (Build faction-state → unit-roster derivation so mass battles are fed by real state.)
6. **Varfell / Hafenmark faction-unique actions — STUBS, UNDISPATCHED (`varfell_mandate_action` 31L, `varfell_territorial_acquisition` 33L, `hafenmark_equipment` 22L).** `faction_action._try_faction_unique` returns `'invalid'` for both, and via the sequential-`if` cascade this is the dominant balance lever (their 30% slot falls through to Conquest). (Implement + dispatch, or change the cascade to `elif`.)
7. **Stub backlog (status hygiene).** 32 stubs total; beyond the above, the personal-scale resolvers `investigation` (31L) / `fieldwork` (33L) / `companion` (21L) and several provincial special actions (`charter_liberties`, `home_sanctuary`, `infrastructure_reclamation`, `altonian_reinforcements`) are armature stubs. Crown/Church unique actions (`crown_initiative` 295L, `excommunication` 214L, `absolution`, `council_solmund`) are *functional but PROVISIONAL-tagged* — they run, but aren't canonized. (Triage; canonize or retire.)

---

## §E — MISSING / FRAGMENTED SCOPES

The scope vocabulary is **three disjoint sets** (confirmed; matches the architecture's open item D6):
- **`TASK_REQUIRED_FILES`** (10): audit, canon_check, compilation, design, design_proposal, editorial, infrastructure, patch, propose_mechanic, simulation.
- **`COMMIT_FORMAT`** (11): editorial, patch, simulation, compilation, infrastructure, skill, cleanup, godot, phase, fix, bugfix.
- **`SESSION_SCOPES`** (per PI bootstrap): infrastructure, godot, editorial, design, simulation, audit, general.

Gaps:
- **No unified scope set** — the three overlap only partially (e.g. `canon_check`/`compilation`/`propose_mechanic`/`design_proposal` exist only in TASK; `skill`/`cleanup`/`phase`/`fix`/`bugfix` only in COMMIT; `general`/`audit`/`godot` only in SESSION+COMMIT). A single ~10-entry vocabulary is proposed (D6) but not landed.
- **`godot` (implementation) has no `TASK_REQUIRED_FILES` entry** — Godot-implementation work routes through `design`/`infrastructure` task gates rather than its own required-files set. A scope gap for the `valoria-game` side of the work.

---

## §F — SYNTHESIS

Architecture is **sound where Jordan asked to confirm it**: modular (correct scale-layering + spine + bridge), keys consistent and deterministic (post hash-seed fix), determinism and serialization in place, Godot-ready in shape. The defects are not architectural — they are **unbuilt and unwired components**, concentrated exactly where the corrected requirements need them:

- the **sole peninsula-control victory** (elimination/subjugation) has no implementation and `treaty` is unwired to it;
- the **dynamic substrate** — card economy (stub), worldly events (stub), domain-echo→stat wiring (unwired), faction-state→mass-battle mapping (gap) — is the set of channels that would make faction state evolve and let non-Mil identities (Hafenmark's wealth, Church's influence) matter;
- the **Varfell/Hafenmark unique-action stubs** both unbuild a feature and, through the `if`-cascade, set the current balance.

Build/wire order to reach the corrected target (subsumes the win-computation remediation):
1. Implement the single peninsula-control victory (elimination + treaty subjugation); retire the GD-1 proxy + fallback. (§D-1)
2. Wire the dynamic substrate so stats evolve: domain-echo→stat (§D-4), then card economy (§D-2), then worldly events (§D-3).
3. Feed mass battles real faction state (§D-5); decompose `massbattle` (§A) while doing so.
4. Implement + dispatch the Varfell/Hafenmark unique actions, or fix the cascade (§D-6).
5. Housekeeping: unify the scope vocabulary (§E / D6); triage the stub backlog and PROVISIONAL canonization (§D-7); fix the spine-inversion docstring drift (§A).

---

Citations:
  - sim/ (full tree, status-grouped)
  - sim/autoload/game_state.py
  - sim/autoload/victory.py
  - sim/provincial/{treaty,tactic_cards,faction_action,massbattle,varfell_territorial_acquisition}.py
  - sim/cross_scale/domain_echo.py
  - sim/world/miraculous_event.py
  - valoria_hooks.py (TASK_REQUIRED_FILES, COMMIT_FORMAT)
  - github_ops.py (SESSION_SCOPES)
