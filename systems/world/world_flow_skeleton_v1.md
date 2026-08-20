# World — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

[EDITORIAL: this file is a traced structural skeleton (code → anchors), not design prose — produced
per `systems/_architecture/subsystem_flow_skeletons_v1.md`; it ratifies nothing and moves no head.]

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/world/` · **Lane:** `WR` · **Contracts:** `miraculous_event` (the only one
of this subsystem's four sim modules with a `references/module_contracts.yaml` entry — see §7 gap 7)
**Code roots traced:** `systems/world/sim/` (`__init__.py`, `insurgency_pipeline.py`,
`miraculous_event.py`, `restoration_movement.py`, `npe.py` — 4 modules, not the 6 the assignment
anticipated; `find systems/world/sim -type f` returns exactly these 5 files incl. `__init__.py`),
`engine/autoload/game_state.py` (`create_world`, `World`/`Faction`/`Territory` dataclasses,
`serialize_world`, `restore_world`), plus every production importer found via repo-wide grep:
`engine/mc_v18.py`, `systems/overview/sim/season.py`, `systems/overview/sim/accounting.py`,
`systems/settlements/sim/registry.py`, `systems/settlements/sim/adjacency.py`,
`engine/substrate/canon_buckets.py`, `engine/substrate/stubwire.py`,
`systems/factions/sim/{parliamentary_transfer,mass_seizure,faction_action}.py` (Territory writers)
**Traced at:** `6545067`

## 1. Entry points

| Callable | Anchor | Called by |
|---|---|---|
| `create_world(seed)` | `engine/autoload/game_state.py:234 create_world` | `engine/mc_v18.py:224 run_campaign` |
| `serialize_world(world)` | `engine/autoload/game_state.py:284 serialize_world` | `engine/mc_v18.py:307 run_campaign` |
| `restore_world(snapshot)` | `engine/autoload/game_state.py:354 restore_world` | — (no production caller; only `engine/tests/test_world_population.py:82`) |
| `check_insurgency_triggers(world)` | `systems/world/sim/insurgency_pipeline.py:139 check_insurgency_triggers` | `systems/overview/sim/accounting.py:124 run_accounting` |
| `check_insurgency_promotion(insurgency_id, world)` | `systems/world/sim/insurgency_pipeline.py:199 check_insurgency_promotion` | `systems/overview/sim/accounting.py:132 run_accounting` |
| `get_insurgencies(world=None)` | `systems/world/sim/insurgency_pipeline.py:258 get_insurgencies` | `systems/overview/sim/accounting.py:131 run_accounting` |
| `reset_for_world(world=None)` | `systems/world/sim/insurgency_pipeline.py:263 reset_for_world` | — (test helper only) |
| `generate_npc(faction, role, world, ...)` | `systems/world/sim/npe.py:215 generate_npc` | — (no call site anywhere in production; see §7 gap 3) |
| `simulate_npc_actions(world)` | `systems/world/sim/npe.py:325 simulate_npc_actions` | `systems/overview/sim/accounting.py:138 run_accounting` |
| `get_npcs_in_territory(territory_id, world=None)` | `systems/world/sim/npe.py:375 get_npcs_in_territory` | — (no production caller found) |
| `reset_npcs(world=None)` | `systems/world/sim/npe.py:380 reset_npcs` | — (test helper only) |
| `trigger_miraculous_event(event_type, world)` | `systems/world/sim/miraculous_event.py:28 trigger_miraculous_event` | — (stub; only reached by `engine/tests/test_pipeline_reach.py:758` stub-wire probe) |
| `process_rm_pt_decay(world)` | `systems/world/sim/restoration_movement.py:30 process_rm_pt_decay` | — (stub; only reached by `engine/tests/test_pipeline_reach.py:759` stub-wire probe) |
| `check_rm_emergence_trigger(world)` | `systems/world/sim/restoration_movement.py:38 check_rm_emergence_trigger` | — (stub; not called anywhere, not even by a stub-wire probe) |
| `canonical_pt(continuous_pt)` | `engine/autoload/game_state.py:74 canonical_pt` | `systems/factions/sim/mass_seizure.py:256 resolve_mass_seizure`, `systems/overview/sim/ci_track.py:133 compute_seasonal_ci_delta` |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `seed: int \| None` | arg | caller of `create_world` | `engine/autoload/game_state.py:234 create_world` |
| `snapshot: dict` | arg | caller of `restore_world` | `engine/autoload/game_state.py:354 restore_world` |
| `STARTING_OWNER` / `STARTING_STATS` / `STARTING_ACCORD` / `STARTING_PT` / `STARTING_GARRISON` | registry | module-level starting-state tables | `engine/autoload/game_state.py:46-93` |
| `world.territories` (dict) | world-state | `World` dataclass | `engine/autoload/game_state.py:188 World.territories` |
| `Territory.accord` / `.pt` / `.prosperity` / `.owner` | world-state | `Territory` dataclass, read by `insurgency_pipeline`/`npe` | `systems/world/sim/insurgency_pipeline.py:228-239`, `systems/world/sim/npe.py:180-200` |
| `world.season` | world-state | `World.season` | `systems/world/sim/insurgency_pipeline.py:167`, `systems/world/sim/npe.py:369` |
| `world.rng` | world-state | `World.rng` | `systems/world/sim/npe.py:231 generate_npc`, `systems/world/sim/npe.py:333 simulate_npc_actions` |
| `world.insurgencies` / `world.uncontrolled_streaks` | world-state | `World` dataclass fields | `engine/autoload/game_state.py:187-188` |
| `world.npcs` / `world.npc_counter` | world-state | `World` dataclass fields | `engine/autoload/game_state.py:187-188` |
| `ADJACENCY` | registry | peer subsystem (settlements) | `systems/settlements/sim/adjacency.py:9`, consumed at `systems/world/sim/insurgency_pipeline.py:116` |
| `canonical_accord(float) -> int` | registry (leaf fn) | `engine.substrate.canon_buckets` | `engine/substrate/canon_buckets.py:38`, imported at `systems/world/sim/npe.py:44` |
| `event_type: str` | arg | caller of `trigger_miraculous_event` | `systems/world/sim/miraculous_event.py:28` |
| `insurgency_id: str` | arg | caller of `check_insurgency_promotion` | `systems/world/sim/insurgency_pipeline.py:199` |
| `faction`, `role`, `territory_id`, `rng` (optional overrides) | arg | caller of `generate_npc` | `systems/world/sim/npe.py:215-217` |

## 3. Flow

- **S1** `engine.mc_v18.run_campaign` calls `game_state.create_world(seed)` to build the
  starting `World`. `engine/mc_v18.py:224 run_campaign`
  - **S1.1** `[write]` Builds `Faction`/`Territory` maps from the `STARTING_*` module tables.
    `engine/autoload/game_state.py:238-255 create_world`
  - **S1.2** `[write]` Initializes `World.clocks` (CI/MS/IP/PI/Strain/Turmoil). `engine/autoload/game_state.py:266 create_world`
  - **S1.3** `[emit]` Down-seam: calls `systems.settlements.sim.registry.populate_from_geography(world)`
    to populate `world.settlements` before returning. `engine/autoload/game_state.py:279-280 create_world`
- **S2** `[loop]` `run_campaign` iterates seasons (`for _ in range(max_s)`), calling
  `season.run_season(world, action_callback=...)` each iteration until a winner is set or the season
  cap is reached. `engine/mc_v18.py:260-267 run_campaign`
  - **S2.1** `[gate]` `run_season` Step 1: `season_manager.advance_season(world)` (peer-owned;
    orchestrates when the world-subsystem steps below fire, does not itself touch this subsystem's
    state). `systems/overview/sim/season.py:69 run_season`
  - **S2.2** `[write]` `run_season` Step 3 hands off to `accounting.run_accounting(world)`, whose
    step 3 calls `check_insurgency_triggers(world)`. `systems/overview/sim/accounting.py:124 run_accounting`
    → `systems/world/sim/insurgency_pipeline.py:139 check_insurgency_triggers`
    - **S2.2.1** `[branch]` Finds contiguous-Uncontrolled-territory groups via BFS over `ADJACENCY`.
      `systems/world/sim/insurgency_pipeline.py:110-136 _contiguous_uncontrolled_groups`
    - **S2.2.2** `[write]` Increments each qualifying group's consecutive-season streak in
      `world.uncontrolled_streaks`. `systems/world/sim/insurgency_pipeline.py:156-158`
    - **S2.2.3** `[branch]` `[write]` A sustained streak with no existing unpromoted record creates
      an `InsurgencyRecord` in `world.insurgencies` and emits a `'formation'` event; otherwise
      emits `'streak_extended'`. `systems/world/sim/insurgency_pipeline.py:160-189`
    - **S2.2.4** `[write]` Streak entries for groups that broke up this season are deleted.
      `systems/world/sim/insurgency_pipeline.py:192-194`
  - **S2.3** `[write]` `run_accounting` step 4 iterates `get_insurgencies(world)` and calls
    `check_insurgency_promotion(ins_id, world)` for each. `systems/overview/sim/accounting.py:131-132 run_accounting`
    → `systems/world/sim/insurgency_pipeline.py:199 check_insurgency_promotion`
    - **S2.3.1** `[gate]` Checks `L`, territory count, and averaged `Accord` thresholds against the
      record; returns unpromoted with a reason on first failing gate.
      `systems/world/sim/insurgency_pipeline.py:212-234`
    - **S2.3.2** `[branch]` `[write]` Averaged `PT` across held territories selects
      `'extra-parliamentary'` vs `'parliamentary'`; sets `rec.promoted = True`.
      `systems/world/sim/insurgency_pipeline.py:236-248`
  - **S2.4** `[write]` `run_accounting` step 5 calls `simulate_npc_actions(world)`.
    `systems/overview/sim/accounting.py:138 run_accounting` → `systems/world/sim/npe.py:325 simulate_npc_actions`
    - **S2.4.1** `[loop]` Iterates all NPC pairs within each territory in `world.npcs`.
      `systems/world/sim/npe.py:339-344`
    - **S2.4.2** `[gate]` `[branch]` `[write]` Pairs sharing a worldview conviction and holding
      adjacent Stance on some issue roll a Volatility check; on pass, both NPCs' `stance` shift
      toward each other by one step on one shared issue. `systems/world/sim/npe.py:344-365`
- **S3** `[branch, default-off]` `trigger_miraculous_event` is a declared entry point never invoked
  anywhere in the traced season loop; its body is an unconditional `stubwire.stub_resolve` call —
  no gate, no computation. `systems/world/sim/miraculous_event.py:28-33` (§7 gap 1)
- **S4** `[branch, default-off]` `process_rm_pt_decay` / `check_rm_emergence_trigger` are declared
  entry points never invoked anywhere in the traced season loop; both bodies are unconditional
  `stubwire.stub_resolve` calls. `systems/world/sim/restoration_movement.py:30-43` (§7 gap 2)
- **S5** `[branch, default-off]` `generate_npc` is fully implemented but has no call site at
  world-gen (S1) or season-tick (S2); the absence is explicitly recorded, not silent, via a named
  `stubwire.stub_resolve('generate_npc(world-gen|season-tick)', ...)` call sitting where the call
  would otherwise be. `engine/mc_v18.py:186-194 _faction_actions_callback` (§7 gap 3)
- **S6** `[write]` At campaign end (winner found or season cap reached), `run_campaign` calls
  `game_state.serialize_world(world)` to build `CampaignResult.final_state`.
  `engine/mc_v18.py:307 run_campaign` → `engine/autoload/game_state.py:284 serialize_world`
  - **S6.1** `[gate, default-off]` `restore_world` exists as the inverse of S6 but is exercised only
    by its own round-trip test, never by a production caller. `engine/autoload/game_state.py:354 restore_world`

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `World` instance | world-state | `engine.mc_v18.run_campaign` and everything downstream in the season loop | `engine/autoload/game_state.py:234 create_world`, `engine/mc_v18.py:224` |
| `list[InsurgencyEvent]` | emit | discarded by caller (`accounting.py` comment: "Events list discarded here") | `systems/world/sim/insurgency_pipeline.py:96-99`, `systems/overview/sim/accounting.py:119-124` |
| `PromotionResult` | emit | discarded by caller's loop | `systems/world/sim/insurgency_pipeline.py:103-107`, `systems/overview/sim/accounting.py:131-132` |
| `world.insurgencies` / `world.uncontrolled_streaks` mutations | world-state | `serialize_world` → `CampaignResult.final_state`; `mc_v18.insurgencies_formed` telemetry | `engine/autoload/game_state.py:296-300`, `engine/mc_v18.py:298` |
| `list[NPCAction]` | emit | discarded by caller ("Actions list discarded here") | `systems/world/sim/npe.py:168-172`, `systems/overview/sim/accounting.py:134-138` |
| `world.npcs` / `world.npc_counter` mutations | world-state | `serialize_world` → `final_state`; `mc_v18.npcs_generated` telemetry | `engine/autoload/game_state.py:301-304`, `engine/mc_v18.py:299` |
| serialized snapshot `dict` | file/registry | `CampaignResult.final_state`; any save-game caller | `engine/autoload/game_state.py:264`, `engine/autoload/game_state.py:274`, `engine/mc_v18.py:307` |
| `StubResult` (from `stub_resolve`) | emit | `stubwire.invocations` cumulative counter → `mc_v18` `stub_hits` campaign telemetry | `engine/substrate/stubwire.py:51`, `engine/substrate/stubwire.py:54`, `systems/world/sim/miraculous_event.py:29`, `systems/world/sim/restoration_movement.py:31`, `systems/world/sim/restoration_movement.py:39` |
| `canonical_pt(continuous_pt) -> int` | registry (leaf fn) | production bucketing callers in factions and overview | `engine/autoload/game_state.py:74 canonical_pt`, `systems/factions/sim/mass_seizure.py:256 resolve_mass_seizure`, `systems/overview/sim/ci_track.py:133 compute_seasonal_ci_delta` |

## 5. State touched

| Field | R/W/RW | Owning module | Anchor |
|---|---|---|---|
| `World.territories` | W (created) | `engine.autoload.game_state` | `engine/autoload/game_state.py:244-255 create_world` |
| `World.territories` | R | `systems.world.sim.insurgency_pipeline` | `systems/world/sim/insurgency_pipeline.py:117` |
| `Territory.accord` | R | `systems.world.sim.insurgency_pipeline`, `systems.world.sim.npe` | `systems/world/sim/insurgency_pipeline.py:228-230`, `systems/world/sim/npe.py:189` |
| `Territory.pt` | R | `systems.world.sim.insurgency_pipeline` | `systems/world/sim/insurgency_pipeline.py:237-239` |
| `Territory.prosperity` | R | `systems.world.sim.npe` | `systems/world/sim/npe.py:200-203` |
| `Territory.owner` | R | `systems.world.sim.npe` | `systems/world/sim/npe.py:196` |
| `World.insurgencies` | RW | `systems.world.sim.insurgency_pipeline` | `systems/world/sim/insurgency_pipeline.py:59`, `systems/world/sim/insurgency_pipeline.py:168-172`, `systems/world/sim/insurgency_pipeline.py:247-248` |
| `World.uncontrolled_streaks` | RW | `systems.world.sim.insurgency_pipeline` | `systems/world/sim/insurgency_pipeline.py:65`, `systems/world/sim/insurgency_pipeline.py:158`, `systems/world/sim/insurgency_pipeline.py:192-194` |
| `World.npcs` | RW | `systems.world.sim.npe` | `systems/world/sim/npe.py:101`, `systems/world/sim/npe.py:320-321`, `systems/world/sim/npe.py:338` |
| `World.npc_counter` | RW | `systems.world.sim.npe` | `systems/world/sim/npe.py:108-109` |
| `World.season` | R | `systems.world.sim.insurgency_pipeline`, `systems.world.sim.npe` | `systems/world/sim/insurgency_pipeline.py:167`, `systems/world/sim/insurgency_pipeline.py:171`, `systems/world/sim/insurgency_pipeline.py:176`, `systems/world/sim/npe.py:369` |
| `World.rng` | R | `systems.world.sim.npe` | `systems/world/sim/npe.py:231`, `systems/world/sim/npe.py:333` |
| `World.clocks` | W (created) | `engine.autoload.game_state` | `engine/autoload/game_state.py:266 create_world` |
| `World.settlements` | W (created, via down-seam) | `engine.autoload.game_state` → `systems.settlements.sim.registry` | `engine/autoload/game_state.py:279-280 create_world` |
| `Territory.accord` | R | `systems.overview.sim.accounting` | `systems/overview/sim/accounting.py:88 _probe_province_accord_drift` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| down | `systems.settlements.sim.registry` | `create_world` calls `populate_from_geography(world)` to build `world.settlements` | `engine/autoload/game_state.py:259-260` |
| lateral | `systems.settlements.sim.adjacency` | `insurgency_pipeline` imports `ADJACENCY` for its contiguous-group BFS | `systems/world/sim/insurgency_pipeline.py:116` |
| up | `systems.overview.sim.accounting` | `run_accounting` calls `check_insurgency_triggers`/`check_insurgency_promotion`/`get_insurgencies`/`simulate_npc_actions` every season | `systems/overview/sim/accounting.py:45-50`, `systems/overview/sim/accounting.py:124`, `systems/overview/sim/accounting.py:131-132`, `systems/overview/sim/accounting.py:138` |
| up | `systems.overview.sim.season` | `run_season` composes `advance_season → action_callback → run_accounting`; this subsystem's per-season steps execute only inside that composition | `systems/overview/sim/season.py:69-72` |
| up | `engine.mc_v18` | `run_campaign` creates/serializes `World`, drives the season loop, records `insurgencies_formed`/`npcs_generated` telemetry, and explicitly defers `generate_npc`/`form_knot` via named `stubwire` calls | `engine/mc_v18.py:224`, `engine/mc_v18.py:260-267`, `engine/mc_v18.py:298-299`, `engine/mc_v18.py:307`, `engine/mc_v18.py:186-209` |
| lateral | `engine.substrate.canon_buckets` | `npe` imports `canonical_accord` (a cycle-break leaf) at module top level | `systems/world/sim/npe.py:44`, `engine/substrate/canon_buckets.py:38` |
| lateral | `engine.substrate.stubwire` | `miraculous_event` and `restoration_movement` route their entire unimplemented bodies through `stub_resolve` | `systems/world/sim/miraculous_event.py:17`, `systems/world/sim/miraculous_event.py:29`, `systems/world/sim/restoration_movement.py:19`, `systems/world/sim/restoration_movement.py:31`, `systems/world/sim/restoration_movement.py:39` |
| lateral | `systems.factions.sim` (`parliamentary_transfer`, `mass_seizure`, `faction_action`) | Write `Territory.owner`/`.accord` directly on the world-owned dataclass; this subsystem's own code only ever reads those fields | `systems/factions/sim/parliamentary_transfer.py:278`, `systems/factions/sim/parliamentary_transfer.py:293`, `systems/factions/sim/mass_seizure.py:290`, `systems/factions/sim/mass_seizure.py:293`, `systems/factions/sim/faction_action.py:488` |
| lateral | `systems.overview.sim.accounting` | `_probe_province_accord_drift` reads `Territory.accord` directly via `canonical_accord`, bypassing every world-owned sim module | `systems/overview/sim/accounting.py:88 _probe_province_accord_drift` |
| in | `engine.autoload.game_state` (`restore_world`) | Late-imports `systems.world.sim.insurgency_pipeline.InsurgencyRecord` and `systems.world.sim.npe.NPC` to reconstruct registries from a snapshot | `engine/autoload/game_state.py:371`, `engine/autoload/game_state.py:378` |
| lateral | `systems.fieldwork` (canon ownership only, no code edge) | `npe.py`'s own canon citation is a fieldwork design doc, not a world or npcs one — see §7 gap 6 | `systems/world/sim/npe.py:4`, `systems/fieldwork/investigation_systems_v30.md:53` |
| lateral | `systems.npcs` (no code, cross-reference only) | `npe.py` is the sole NPC-generation/drift implementation in the repo; `systems/npcs/` has no `sim/` directory — its own flow skeleton (`systems/npcs/npcs_flow_skeleton_v1.md`) traces this same code as its interior — see §7 gap 6 | `systems/world/sim/npe.py:1-24` (module docstring); confirmed by directory listing, no `systems/npcs/sim/` exists |

## 7. Traced gaps

| Gap | Evidence anchor |
|---|---|
| `trigger_miraculous_event` is a typed no-op stub with zero production callers; its declared "Dependencies" (`sim/autoload/dice_engine`, `systems/threadwork/sim/rendering`) are never imported anywhere in the file — the only import is `stubwire`. | `systems/world/sim/miraculous_event.py:7-33` |
| `process_rm_pt_decay` and `check_rm_emergence_trigger` are both typed no-op stubs with zero production callers; declared deps (`sim/autoload/game_state`, `systems/world/sim/insurgency_pipeline`) are never imported. `check_rm_emergence_trigger` isn't even reached by the OI-17 stub-wire probe test that covers `process_rm_pt_decay`. | `systems/world/sim/restoration_movement.py:8-43`; probe list at `engine/tests/test_pipeline_reach.py:758-759` covers only `process_rm_pt_decay` |
| `generate_npc` is fully implemented but has no call site anywhere in production code (world-gen or season-tick). `engine.mc_v18` records the absence explicitly via a named `stubwire.stub_resolve` call rather than invoking it, and the corresponding acceptance test is marked `xfail(strict=True)`, confirming `npc_counter` stays at 0 for a full seeded campaign. | `engine/mc_v18.py:186-194`; `engine/tests/test_pipeline_reach.py:596-599` |
| `restore_world` has no production caller anywhere in the traced tree — exercised only by its own round-trip test. | `engine/autoload/game_state.py:334`; `engine/tests/test_world_population.py:82` |
| Stale "no registry" docstrings: `insurgency_pipeline.py` and `npe.py` both open with an `[ASSUMPTION]` comment stating `game_state.World` has no insurgency/NPC registry and describing the fields as a pending schema migration. `World` has already carried `insurgencies`, `uncontrolled_streaks`, `npcs` and `npc_counter` since the 2026-05-19 migration, and both modules' own `_ins_store`/`_streak_store`/`_npc_store` helpers already route through them when a `world` is supplied — the comments were not updated after the migration landed. | `systems/world/sim/insurgency_pipeline.py:13-16` vs `engine/autoload/game_state.py:185-188`; `systems/world/sim/npe.py:10-15` vs `engine/autoload/game_state.py:187-188` |
| Homing mismatch: `npe.py`'s own canon citation is `systems/fieldwork/investigation_systems_v30.md` SYSTEM 1 (NPE) — a fieldwork design doc, not one under `systems/world/` or `systems/npcs/`. Its runtime home is `systems/world/sim/`, and its only production call site is wired through `systems/overview/sim/accounting.py`. `systems/npcs/` has no `sim/` directory and no code anywhere in the repo imports an NPC-generation module from it — `npe.py` is the sole implementation, split across three different "owners" (canon: fieldwork; location: world; conceptual subject: npcs). | `systems/world/sim/npe.py:1-24`; `ls systems/npcs/` (no `sim/` present); repo-wide grep finds no `systems.npcs.*` import anywhere |
| `references/module_contracts.yaml` registers only `miraculous_event` among this subsystem's four sim modules, despite `insurgency_pipeline.py`, `npe.py` and `restoration_movement.py` each declaring explicit "Entry points" in their own docstrings. | `references/module_contracts.yaml:922-937` (present entry) vs no `module: insurgency_pipeline\|npe\|restoration_movement` row anywhere in that file |
| `restoration_movement.py`'s cited canon sources (a `designs/audit/2026-05-14-balance-audit/...` file and `designs/provincial/restoration_movement_v30.md`) resolve to nothing in the current working tree — `designs/` was retired 2026-07-19 (`CLAUDE.md` §3) and no `restoration_movement`-named doc exists anywhere in the repo outside this one `.py` file. By contrast `insurgency_pipeline.py`'s own `[CANON-GATED]: ... cited but not yet authored` comment is now stale in the other direction — `systems/world/insurgency_pipeline_v30.md` exists on disk with `## Status: CANONICAL`. | `systems/world/sim/restoration_movement.py:4`, `systems/world/sim/restoration_movement.py:6` (no matching file found by repo-wide search); `systems/world/sim/insurgency_pipeline.py:18-21` vs `systems/world/insurgency_pipeline_v30.md:3` |
| **The contract coverage is inverted from the execution.** `miraculous_event` — this subsystem's one module with a `module_contracts.yaml` entry — never executes anywhere in the traced season loop (S3). The two modules that carry all of this subsystem's measured execution every season, `insurgency_pipeline` and `npe`, have no contract entry at all. | `references/execution_map.json:1121 executes`; `references/execution_trace.json:120 insurgency_pipeline`; `references/execution_trace.json:121 npe`; `references/module_contracts.yaml:922-937 miraculous_event` |
| `systems/world/` has no `CURRENT.md` head row, despite `systems/world/insurgency_pipeline_v30.md` existing on disk with `## Status: CANONICAL`. | `systems/_architecture/subsystem_flow_skeletons_v1.md:150 world` |
