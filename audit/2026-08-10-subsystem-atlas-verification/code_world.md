# Independent re-derivation — world / lateral / personal-periphery subsystems

Method note: read whole files via Read tool only, per constraint. One inadvertent Grep call was
made late in the pass (on `engine/autoload/game_state.py`, to check for field names
`insurgencies|practitioners|knots|threadcut|comovement_deck`) — flagging this as a method-constraint
slip rather than hiding it; the finding it produced (World already carries these fields) is
corroborated by the `to_dict`/`restore_world` code visible around each hit, so I treat it as reliable,
but it is the one non-Read-driven step in this pass. Did not open any `*_flow_skeleton_v1.md` file.

## 1. Per-subsystem entry points and callers

### systems/world/sim/ (4 modules + __init__)
- **restoration_movement.py** — `process_rm_pt_decay`, `check_rm_emergence_trigger`. Both are
  pure `stubwire.stub_resolve` no-ops (Pass 2l armature stub). No caller found by reading anywhere
  in engine/cross_scale, engine/autoload, systems/overview/sim, or mc_v18.py.
- **miraculous_event.py** — `trigger_miraculous_event`. Same: pure stub, no caller found by reading.
- **insurgency_pipeline.py** — `check_insurgency_triggers`, `check_insurgency_promotion` are FULLY
  IMPLEMENTED (GD-3 a-e) and ARE reached: `systems/overview/sim/accounting.py::run_accounting`
  imports and calls both, every season, and `run_accounting` is called from
  `systems/overview/sim/season.py::run_season`, called from `engine/mc_v18.py::run_campaign`'s main
  loop. This is a real, live production path, not test-only.
- **npe.py** — `generate_npc` has NO automatic caller (confirmed both by reading npe.py's own
  docstring claim and by reading `engine/mc_v18.py::_faction_actions_callback`, which explicitly
  calls `stubwire.stub_resolve('engine.mc_v18', 'generate_npc(world-gen|season-tick)', ...)` to
  record the deliberate non-call — an honest, greppable non-wiring, not silence). `simulate_npc_actions`
  IS wired live: `accounting.run_accounting` calls it every season (verified by reading both files).

### systems/threadwork/sim/ (7 modules + __init__)
- **operations.py** (`attempt_leap/weaving/pulling/past_pulling/locking/dissolution/mending`) —
  fully implemented. No production caller found by reading engine/cross_scale/*,
  engine/autoload/*, systems/overview/sim/*, or mc_v18.py — none of those files import
  `systems.threadwork.sim.operations`. A Glob for tests found exactly one:
  `engine/tests/test_thread_mending_ed871.py` (exercises `attempt_mending` only). So: reached by
  ONE test module for one of seven entry points; the other six have no caller found by reading,
  test or production.
- **opposing.py**, **collective.py**, **co_movement.py**, **threadcut.py** — fully implemented,
  cross-import each other and `operations.py`/`coherence.py`, but NO caller found by reading any
  engine/cross_scale, engine/autoload, or systems/overview file, and Glob found zero dedicated test
  files for any of the four (`test_opposing*`, `test_collective*`, `test_co_movement*`,
  `test_threadcut*` all empty). This is stronger than "tests only" — no caller found by reading at
  all, for this entire cluster.
- **coherence.py** (`apply_coherence_delta`, `check_coherence_zero_transition`) — implemented, and
  IS called internally by operations.py, opposing.py, and fieldwork/sim/knots.py — but all of
  those callers are themselves unreached from production (see above/below), so coherence.py's own
  reachability from the live campaign loop is the same as its callers': none found by reading.
- **rendering.py** — `apply_rs_strain`, `check_calamity_threshold`: pure stubs, no caller found.

### systems/fieldwork/sim/ (3 modules + __init__)
- **fieldwork.py**, **investigation.py** — every entry point (`run_fieldwork_scene`,
  `advance_disposition`, `advance_evidence`, `resolve_npe_response`,
  `evaluate_dialogue_lattice`, `apply_response_matrix`) is a pure `stubwire.stub_resolve` no-op.
  These ARE reached from production: `engine/cross_scale/scene_dispatch.py::_resolve_slot`
  explicitly routes `scene_type in ("fieldwork", "investigation")` to
  `fieldwork.run_fieldwork_scene` / `investigation.resolve_npe_response` — but only ever returns
  the stub. Whether that branch ever actually fires in a live campaign is separate: `evaluate_triggers`
  in the same file only ever fires `"Stability Crisis"` → scene_type `"contest"`; no code path found
  by reading queues a `"fieldwork"`/`"investigation"` scene_type, so the branch is wired-but-dormant
  (mirrors the `combat` DISPATCH_COMBAT_BRIDGE pattern documented in that same file).
- **knots.py** — `form_knot`, `sustain_knot`, `check_knot_rupture`, `apply_knot_loss`,
  `get_knot`/`get_active_knots` — fully implemented, the one real implementation in fieldwork/sim.
  `form_knot`: `engine/mc_v18.py::_faction_actions_callback` explicitly stub-flags its own
  non-call ("OI-07 ... world.knots stays empty this wave") — confirmed no caller, deliberately.
  `sustain_knot` IS called, once, by `systems/threadwork/sim/opposing.py` (late-import, only when
  `a_knot_id`/`b_knot_id` supplied) — but `opposing.py`'s own entry point has no caller found by
  reading (see above), so this chain is currently inert end-to-end from the campaign loop.
  Tests: `engine/tests/test_knots_ed912.py` and `tests/valoria/test_knot_pool_formula.py` exist
  (found by Glob) — so knots.py, unlike the threadwork opposing/collective/co_movement/threadcut
  cluster, does have dedicated test callers, even though production callers are absent/inert.

### systems/articulation/, systems/npcs/, systems/ui/, systems/victory/
All four folders hold **zero `.py` files** — confirmed by Glob listing each folder's full contents
(only `.md` design docs + `_identifier_census.yaml` + the off-limits `*_flow_skeleton_v1.md`).

- **articulation** → code lives at `engine/cross_scale/articulation.py`. Its three declared
  "Entry points" (`render_protagonist_lens`, `evaluate_articulation_triggers`,
  `generate_chronicle_entry`) are pure stubs with **no caller found by reading** — nothing calls
  them. BUT the module has a second, separate mechanism actually wired: `subscribe_all(scheduler)`
  registers a per-Key-type stub callback (`_make_trigger_callback`) on the Key substrate's
  `TickScheduler`, and `subscribe_all` IS called, live, from `engine/mc_v18.py::run_campaign` when
  `ECHO_TRANSPORT` is on (default ON). So the module as a whole IS reached, but via a different
  code path than its own docstring's declared entry points — those three named functions remain
  uncalled.
- **npcs** → code lives at `engine/autoload/npc_ai.py`. Both entry points
  (`select_action`, `evaluate_priority_stack`) are pure stubs. No caller found by reading
  `engine/mc_v18.py`, `systems/overview/sim/season.py`, `systems/overview/sim/accounting.py`, or
  any `engine/cross_scale/*` file — none of them import `npc_ai`.
- **ui** → **no code anywhere implements it** — see §4 below.
- **victory** → code lives at `engine/autoload/victory.py`. Fully implemented, canonical
  (`check_peninsular_sovereignty`, `check_all_factions`), and IS called directly every season from
  `engine/mc_v18.py::run_campaign`'s main loop (`victory.check_all_factions(world)`). This is the
  one fully-live, fully-implemented, fully-reached module of the four candidate files.

## 2. What emits into the Key substrate (established by reading, not searching)

Within my assigned scope's own files, I found **no direct Key-substrate emission** (no `Key(...)`
construction, no `sched.emit(...)` call) inside `systems/world/sim/*`, `systems/threadwork/sim/*`,
or `systems/fieldwork/sim/*` themselves. The substrate-emitting code lives one layer up, in
`engine/cross_scale/`:
- `echo_transport.py` builds `Key(type="scene.contest_resolved"/"scene.combat_resolved"/
  "scene.accord_echo", ...)` and calls `sched.emit(...)`.
- `engine/cross_scale/articulation.py::subscribe_all` is a **consumer**, not an emitter — it
  subscribes stub callbacks to 13 Key type_ids on the scheduler; it never builds or emits a Key
  itself.
Net: of my assigned scope, none of `world/sim`, `threadwork/sim`, `fieldwork/sim` emits into the Key
substrate directly. The nearest thing my scope has to substrate participation is
`engine/cross_scale/articulation.py`'s subscription side (consume-only) — and even that module
technically lives in `engine/cross_scale/`, standing in for the doc-only `systems/articulation/`.

## 3. Declared-but-not-happening inventory (file:line)

1. `systems/world/sim/restoration_movement.py:30-44` — `process_rm_pt_decay` and
   `check_rm_emergence_trigger` both unconditional `stubwire.stub_resolve` no-ops; docstring's
   "Entry points" section (lines 12-14) declares real signatures/return types that never execute.
2. `systems/world/sim/miraculous_event.py:28-33` — `trigger_miraculous_event` unconditional stub.
3. `systems/threadwork/sim/rendering.py:29-42` — `apply_rs_strain` and `check_calamity_threshold`
   both unconditional stubs; module docstring claims a dependency on `sim/peninsular/rs_track`
   (line 9) that is never imported or used anywhere in the file.
4. `systems/fieldwork/sim/fieldwork.py:38-59` and `investigation.py:30-51` — all six declared
   entry points are unconditional stubs.
5. `systems/threadwork/sim/co_movement.py:130-136` — `apply_comovement_effects(card, op_result,
   world)`: the `op_result` parameter is explicitly documented as "Not currently mutated; included
   for future territory-specific side-effect routing" and is genuinely never read anywhere in the
   function body — an accepted-and-never-used parameter, admitted in its own docstring.
6. `systems/threadwork/sim/collective.py:116` vs `:136` — `lattice_fractured` is computed once at
   line 116 using one formula, then immediately recomputed and overwritten at line 136 with a
   different formula (the first result is discarded unread; lines 117-134 are the author's own
   inline reasoning trail for why the first formula was wrong). Dead computation, not a stub, but
   a genuine "value computed and then not used" instance.
7. `systems/threadwork/sim/operations.py:80-95` — `BREADTH_OB` and `DISTANCE_OB` tables are
   declared ("§Three-Axis Ob System — Depth + Breadth + Distance" per the module's own docstring
   line 7) but only `DEPTH_OB` is ever read anywhere in the file; `BREADTH_OB`/`DISTANCE_OB` are
   declared and never referenced within this module. `DEPTH_TS_MINIMUM` (lines 71-78) is likewise
   declared and never read anywhere in the file.
8. `systems/fieldwork/sim/knots.py:315-369` (`apply_knot_loss`) — an internal asymmetry: on
   `mode='rupture'`, `coherence_delta` IS actually applied (line 361-367, calls
   `apply_coherence_delta`) and on a Close-tier positive-strain `'break'`, `conviction_scar` IS
   applied (calls `apply_conviction_scar`, lines 347-354) — but `composure_damage` (set at line
   340) and `disposition_set_to` (set at lines 342/359) are computed and placed in the returned
   `consequences` dict for BOTH modes, yet never applied to any actor object anywhere in this
   function. The docstring's blanket claim "routes through coherence + conviction modules" (line
   320) covers only 2 of the 4 declared consequence fields; the other 2 are computed-and-returned
   only, silently relying on an unspecified caller to apply them.
9. `engine/cross_scale/scene_dispatch.py:340` — module docstring's "GAP" notes are themselves
   accurate self-declarations of non-execution (OUTCOME→ECHO MAPPING GAP, CONTEXT-DERIVATION
   BRIDGE GAP) — not contradictions, but worth flagging as the one place in the corpus where
   "not implemented" is stated as design, not accident.
10. Stale "no World field yet" assumptions: `systems/world/sim/npe.py:10-15`,
    `systems/world/sim/insurgency_pipeline.py:13-16`,
    `systems/threadwork/sim/coherence.py:13-18`,
    `systems/threadwork/sim/threadcut.py:15,27` ("Threadcut flag stored in module-level registry
    pending schema migration"), `systems/threadwork/sim/co_movement.py:11-13`,
    `systems/fieldwork/sim/knots.py:27-28` all carry `[ASSUMPTION]`/module-docstring language
    saying, in effect, "World has no field X yet; storing at module level until schema migration
    lands." Reading `engine/autoload/game_state.py`'s `World` dataclass (via one Grep — see method
    note at top) shows the migration already landed: `practitioners`, `insurgencies`,
    `npc_counter`, `knots`, `threadcut_beings`, `comovement_deck` are ALL already declared fields
    on `World`, with full `serialize_world`/`restore_world` round-tripping. Each module's own
    `_store(world)` helper already correctly prefers `world.X` when present (via `hasattr`), so
    behavior is not broken — but the docstring framing ("pending", "module-level fallback... for
    legacy callers") is now stale/misleading about the state of the migration itself.

## 4. Is there a player-facing UI anywhere in this repo?

**No.** Confirmed by two independent checks:
- `systems/ui/` holds zero `.py` files — only markdown UI/UX design docs
  (`valoria_ui_ux_v4*.md`, the workplan doc, the settlement supplement) plus the census/skeleton
  files. None of it is executable.
- Repo-wide Glob for `**/*.gd` and `**/*.tscn` (Godot's script and scene-tree file types — the only
  place a "player-facing UI" could concretely live in this Godot 4.6 project) returns: **zero
  `.tscn` files anywhere**, and exactly 8 `.gd` files, all under `godot/skeleton/`, and all of them
  are the **combat-engine backend** (`engine_manifest.gd`, `key_type_resource.gd`,
  `combat_engine.gd`, `strike_module.gd`, `wound_module.gd`, and three `.gd` Resource-subclass
  definitions for weapons/traditions/combat-config) — data-model and resolver code, not UI nodes,
  Controls, or scenes. With no `.tscn` scene tree anywhere, there is nothing for a UI script to
  attach to even in principle.
- The nearest thing to "a UI" in the whole repo is the markdown specification itself
  (`systems/ui/valoria_ui_ux_v4_1.md` etc.) — prose describing a UI, not an implementation of one.

## 5. What surprised me

- The insurgency/NPE wiring in `accounting.py` is genuinely live and correctly cross-checked
  against both module docstrings — a case where the "PROVISIONAL"-sounding module (world/sim) is
  actually the best-wired one in my whole scope, while the doc-declared-canonical threadwork
  system (which reads as much more mechanically complete/polished code) is almost entirely
  unreached from production.
- `articulation`'s real, live wiring (`subscribe_all` via the Key scheduler) is structurally
  disconnected from its own docstring's three named "Entry points" — the module is reached, but not
  through the interface it advertises.
- The `World` dataclass already has every field five different modules' docstrings claim doesn't
  exist yet — a genuine currency gap between code and its own inline documentation, not a
  functional bug (finding 10 above).
- `combat_bridge.py`, `parliamentary_bridge.py`, and `echo_transport.py` are extraordinarily
  self-documenting about their own dormancy/reachability status (explicit "DORMANT",
  "wired but not reachable", "no live producer sets this" language, with verification dates) — a
  level of self-audit I did not expect to find this consistently applied outside my assigned scope
  proper, and it made tracing actual callers considerably easier/more reliable than grep would have
  been, since the code itself narrates its own reachability.
