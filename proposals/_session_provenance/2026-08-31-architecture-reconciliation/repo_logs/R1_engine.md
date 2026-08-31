# R1 — engine/ : what actually executes

Scope: `engine/` only (substrate, autoload, cross_scale, mc_v18, engine_params, tests). Read-only.
All citations file:line against the working tree at time of read (2026-08-31).

---

## 1. Inventory: every module, its LOC, its role in one line

### `engine/substrate/` — the Key substrate (leaf tier)
| file | LOC | role |
|---|---|---|
| `__init__.py` | 41 | re-exports the public Key API (`Key`, `KeyLog`, `TickScheduler`, `TypeRegistry`, etc.) |
| `keys.py` | 601 | `Key`/`Target`/`Visibility`/`EmittedAt` dataclasses, `TypeRegistry` (loads `key_types.json`), `KeyLog` (append-only, validates 8 invariants, hashes), `TickScheduler` (cascade-depth + emissions-per-tick termination guard, OF-7 deferred-apply, B1 no-sync-reentry) |
| `descriptors.py` | 211 | sole runtime reader of `descriptors.json`; exposes `ATTRIBUTES`, `FACTION_STATS`, `CONVICTIONS`, `faction_bounds()`, `assert_faction_roster_is_covered()`, `resolve_conviction()` |
| `composition.py` | 69 | resolves a declared ROLE name (from `composition.json`) to a `systems.*` callable by string import — keeps `systems` out of `engine`'s import graph |
| `canon_buckets.py` | 48 | `canonical_accord(float)->int` — a pure bucketing leaf, relocated here to break an import cycle |
| `stubwire.py` | 84 | `StubResult`/`stub_resolve()` — the single typed "explicitly not built" no-op primitive, counted by `mc_v18`'s `stub_hits` telemetry |
| `world_initial_state.py` | 56 | sole runtime reader of `world_initial_state.json` — territory/faction opening-position tables |

### `engine/autoload/` — the singleton-hub tier
| file | LOC | role |
|---|---|---|
| `dice_engine.py` | 299 | `roll_pool`, `continuous_engine_sample`, **`degree_from_net`** — THE single degree ladder for every scale of the game; `BandExtension` injection seam |
| `engine_clock.py` | 127 | `run_tick(world, action_callback)` — the temporal spine: SEASON_TICK -> ACTION -> ACCOUNTING_BOUNDARY, one owner of season advancement |
| `game_state.py` | 513 | `Faction`, `Territory`, `World` dataclasses; `create_world`, `serialize_world`, `restore_world`; owns `MULTS`, `ACCORD_MAP`, `PT_MAP` |
| `npc_ai.py` | 47 | `select_action`/`evaluate_priority_stack` — both **stub-wired** (`stubwire.stub_resolve`), not implemented |
| `scene_slate.py` | 59 | module-level `deque` priority queue of `SceneSlot` for personal-scale scenes |
| `season_manager.py` | 50 | `advance_season(world)->SeasonResult`; `SEASONS_PER_ARC=4` |
| `sigma_leverage.py` | 333 | sigma-leverage advantage layer atop `dice_engine` — `sigma_n`, `soft_cap`, `net_boost`, `p_success`, `level()`, `levels_to_net_sigma()` |
| `victory.py` | 110 | `check_peninsular_sovereignty` — the SOLE victory function (GD-1); `VICTORY_THRESHOLD=15` |

### `engine/cross_scale/` — scale-transition glue
| file | LOC | role |
|---|---|---|
| `articulation.py` | 170 | trigger->chronicle-entry stubs (render layer unbuilt); `subscribe_all(scheduler)` wires trigger callbacks |
| `combat_bridge.py` | 150 | the `PATH_SEAM_ALLOWED` bare-name `sys.path` seam into `systems/combat/combat_engine_v1/`; derives two `Combatant`s from faction `Mil`, calls `wrapper.fight()` |
| `domain_echo.py` | 216 | `compute_domain_echo`, `compute_accord_echo`, `compute_thread_echo` — degree-keyed, no-RNG pure functions mapping scene outcome -> stat delta |
| `echo_transport.py` | 474 | routes a resolved scene outcome through the Key substrate to a deferred faction/settlement write at accounting boundary; owns `KEY_TYPE_BY_SCENE` |
| `handoff_rules.py` | 232 | `apply_handoff(from_scale, to_scale, payload, world)` — rule registry, validity-only, does not execute mechanics |
| `parliamentary_bridge.py` | 193 | `run_parliamentary_scene(world, rng)` — per-season Section-10 vote + territory-transfer motion |
| `scene_dispatch.py` | 423 | `run_scene_phase(world, rng)` — evaluate triggers -> queue -> dispatch (combat/contest/fieldwork/investigation) -> zoom_out; the season's scene-resolution seam |
| `zoom_in_out.py` | 198 | `zoom_in`/`zoom_out`/`check_mandatory_triggers` — Zoom protocol dataclasses |

### `engine/mc_v18.py` — 348 LOC — the campaign driver (`run_campaign`, `run_batch`, `_faction_actions_callback`)

### `engine/tests/` — 16 files, seeded regression + parity suite (see Sec 5, Sec 7 below)

### `engine/engine_params/` — 10 generated artifacts (JSON/YAML), see Sec 6

---

## 2. THE KEY SUBSTRATE — reproduced precisely

**Key** (`engine/substrate/keys.py:126-158`, dataclass):
```
id: str
type: str
emitted_at: EmittedAt
source_actor: str | None = None
causes: list = []
targets: list = []            # list[Target]
scale_signature: list = []    # list[str]
symbolic_dimensions: dict = {}
visibility: Visibility = Visibility()
time_horizon: str = "immediate"
permanence: str = "transient"
payload: dict = {}
```
`.to_obj()` (keys.py:141-155) is the canonical serialization — sorted-key JSON, list order preserved (semantic).

**Target** (keys.py:83-97): `actor_id, role, impact_vector: dict[axis->signed magnitude], stat_deltas: dict[stat->delta]`.

**Roles** (keys.py:47): `("subject", "object", "witness", "beneficiary", "bystander")` — target roles.

**Axes** (keys.py:44): `("hierarchical", "sacred", "instrumental", "traditional")` — the canonical 4-axis Conviction set.

**Scales** (keys.py:50): `("personal", "settlement", "territory", "peninsula")`.

**Permanence** (keys.py:52): `("transient", "persistent", "indelible")`. **Time horizon** (keys.py:53): `("immediate", "near", "far")`.

**Visibility** (keys.py:100-111): `public: bool = True`, `semi_public_observers: list`, `private_observers: list` — invariant 8 forces exactly one shape (public XOR exactly-one non-empty observer list).

**EmittedAt** (keys.py:114-121): `season_index: int`, `sub_step_index: int = -1` — sub_step_index is assigned by `KeyLog.append` (append order), never by the emitter.

**TypeRegistry** (keys.py:190-315): loads either the authored markdown (`systems/_architecture/key_type_registry_v30.md`, parsed by a tolerant line-based `_parse_entry`) or the cooked `engine/engine_params/key_types.json` — dispatched by file suffix (keys.py:207-217). **55 types**, pinned identical between the two representations by `test_key_substrate.py::test_json_and_markdown_registries_are_identical` (cited at keys.py:167). `require()`, `validate_payload()`, `apply_defaults()` are its public surface.

**KeyLog** (keys.py:319-419): append-only. `append()` runs `_validate()` (keys.py:355-406), enforcing all **8 numbered invariants**:
1. unique id (keys.py:357-358)
2. type registered + payload contract (359-360)
3. `causes[]` only cite already-logged keys (361-365)
4. cycle-freedom — holds by construction, not separately checked (367-369 comment)
5. season_index non-decreasing (370-374)
6. axis names subset-of AXES (375-381), roles subset-of ROLES (382-386)
7. `scale_signature` non-empty and subset-of SCALES (387-392)
8. exactly one visibility shape (393-402)
Plus `time_horizon`/`permanence` value checks (403-406).
`content_hash()` (keys.py:418-419) is `sha256(serialize())` — `serialize()` (keys.py:414-417) is newline-joined per-Key sorted-key JSON — the determinism surface cited throughout the corpus as "key_log_hash".

**TickScheduler** (keys.py:422-601): the emission/scheduling owner. Constructor **requires** `cascade_depth_max` and `emissions_per_tick_max` (no default — OF-CAP is an open fork, keys.py:428-437 docstring: "no fabricated constant enters the repo"). `emit()` (keys.py:460-471) is root emission (depth 0), raises `TerminationBreach` if called during a drain when `no_sync_reentry` is on. `schedule_emission()` (473-484) is the re-entrant path, enqueued at `depth+1`. `drain_tick()` (486-499) FIFO-drains the queue. `_emit_at_depth()` (501-524) is where a Key is actually validated+appended+applied (OF-7 deferred-apply logic at 517-521) and subscribers are synchronously notified (522-524). `accounting_boundary()` (527-536) runs all pending OF-7 applies in emission order. `next_tick()` (538-545) resets the per-tick counter and phase.

**Load-time invariants**: `TypeRegistry.load_json` (keys.py:229-256) additionally validates malformed type ids, non-dict entries, and a self-declared `type_count` against the actual roster size — parity checks the markdown path enforces structurally that the JSON path had to add explicitly (keys.py:242-247 comment names this a real historical gap).

---

## 3. THE TYPE INVENTORY — every Python class in `engine/`

| class | file:line | fields | who constructs it | who mutates it |
|---|---|---|---|---|
| `Target` | `substrate/keys.py:83` | actor_id, role, impact_vector, stat_deltas | emitters building a Key | none post-construction |
| `Visibility` | `substrate/keys.py:100` | public, semi_public_observers, private_observers | Key construction | none |
| `EmittedAt` | `substrate/keys.py:114` | season_index, sub_step_index | emitter (season_index) | `KeyLog.append` sets sub_step_index (keys.py:307) |
| `Key` | `substrate/keys.py:126` | id, type, emitted_at, source_actor, causes, targets, scale_signature, symbolic_dimensions, visibility, time_horizon, permanence, payload | any emitter (`echo_transport`, `articulation`, tests) | `TypeRegistry.apply_defaults` mutates scale_signature/permanence/time_horizon in place (keys.py:294-303) |
| `TypeRegistry` | `substrate/keys.py:190` | `types: dict` | `TypeRegistry.load`/`load_json` classmethods | none (read-only after load) |
| `KeyLog` | `substrate/keys.py:319` | registry, `_entries`, `_ids`, `_season_counters`, stat_vocabulary, stat_vocabulary_warnings | `echo_transport._registry()`-adjacent callers, tests | `append()` |
| `TickScheduler` | `substrate/keys.py:422` | log, caps, flags, subscriptions, `_queue`, `_pending_apply`, phase counters | `echo_transport.make_scheduler` (echo_transport.py:184) | `emit`/`schedule_emission`/`drain_tick`/`accounting_boundary`/`next_tick` |
| `KeyValidationError` / `TerminationBreach` | `substrate/keys.py:66/71` | exception subtypes | raised throughout `keys.py` | n/a |
| `StubResult` | `substrate/stubwire.py:39` (frozen) | module, io_contract, reason, `stub: bool` (init=False, always True) | `stub_resolve()` only | immutable |
| `Faction` | `autoload/game_state.py:109` | name, parliamentary, L, Sta, W, I, Mil, intel, territories, senator_inward_used, consul_used, peaceful, standing, excommunicated, council_used_this_arc, parl_transfer_used_this_arc | `create_world` (game_state.py:309), `restore_world` (441) | `.adjust()` (153), `.reset_seasonal()` (198), `.reset_arc()` (202); ~31 non-test call sites across `systems/factions`, `systems/overview` |
| `Territory` | `autoload/game_state.py:234` | tid, owner, accord, pt, garrison, prosperity, fort_level, templar, uncontrolled_since | `create_world` (316) | `.adjust_accord()`, `.adjust_pt()` (248-252) |
| `World` | `autoload/game_state.py:256` | factions, territories, clocks, season, arc, winner, battle_count, scenes_resolved, rng, **14 schema-migration registries** (practitioners, insurgencies, uncontrolled_streaks, npcs, npc_counter, treaties, convictions, beliefs, knots, knot_id_counter, territory_infrastructure, npc_drift_state, threadcut_beings, comovement_deck) + **settlements** | `create_world` | mutated throughout `mc_v18`, `engine_clock`, `cross_scale/*`; also carries **dynamically-attached** non-dataclass attrs: `echo_scheduler`, `key_log`, `_echo_key_seq`, `dispatch_combat_bridge` (set only when relevant flags are on — mc_v18.py:222-241) |
| `RollResult` | `autoload/dice_engine.py:163` | pool_size, tn, rolls, net, degree, ob | `roll_pool()` | none |
| `Degree` (Enum) | `autoload/dice_engine.py:27` | OVERWHELMING, SUCCESS, PARTIAL, FAILURE | n/a | n/a |
| `BandExtension` | `autoload/dice_engine.py:112` | `name`, `context_keys` (class attrs) | subsystem wrapper subclasses it | `may_overwhelm()`/`validate_context()` overridden by subclass |
| `SceneSlot` | `autoload/scene_slate.py:25` | scene_type, context, priority | `queue_scene()` | none |
| `SeasonResult` | `autoload/season_manager.py:23` | season, arc, new_arc | `advance_season()` | none |
| `VictoryResult` | `autoload/victory.py:26` | faction_id, won, held, qualifies_this_season, consecutive_qualifying, reason | `check_peninsular_sovereignty()` | none |
| `CampaignResult` | `mc_v18.py:91` | winner, season, surviving, battle_count, scenes_resolved, insurgencies_formed, npcs_generated, stub_hits, accord_drift_probe_hits, key_log_hash, keys_emitted, final_state | `run_campaign()` | none |
| `BatchResult` | `mc_v18.py:109` | n, win_share, all_winners, battles_mean | `run_batch()` | none |
| `HandoffResult` | `cross_scale/handoff_rules.py:73` | (validity result shape) | `apply_handoff()` | none |
| `ZoomInResult` / `ZoomOutResult` / `ZoomTrigger` | `cross_scale/zoom_in_out.py:48/56/64` | scene_ob_modifier / domain_echoes_queued / trigger_name+... | `zoom_in()`/`zoom_out()`/`check_mandatory_triggers()` | none |
| `DomainEchoResult` / `AccordEchoResult` / `ThreadEchoResult` | `cross_scale/domain_echo.py:51/61/71` | stat-delta shapes | `compute_domain_echo`/`compute_accord_echo`/`compute_thread_echo` | none |

No class in `engine/` is a "carrier" in the proposed-design sense (see Sec 7) — every dataclass here is a **strategic aggregate stat container** (Faction/Territory/World) or a **transport/result value object** (Key, RollResult, the cross_scale Result dataclasses). None represents an individual human actor.

---

## 4. THE LOOP THAT ACTUALLY RUNS — mc_v18's phase order, step by step

`run_campaign(seed, max_seasons, params)` (`mc_v18.py:213-283`):

1. **Setup** (213-241): `create_world(seed)`, `victory.reset()`, `scene_slate.clear()`; decide `DISPATCH_COMBAT_BRIDGE` flag once, stash on `world` (222); decide `ECHO_TRANSPORT` flag, and if ON attach `world.echo_scheduler = echo_transport.make_scheduler(...)`, `world.key_log = ...log`, subscribe articulation triggers (225-241).
2. **Season loop**, up to `max_s` iterations (244-262): each iteration calls `composition.require('season_driver')(world, action_callback=_faction_actions_callback)` (257) — resolved by string to `systems.overview.sim.season:run_season`, which internally calls `engine_clock.run_tick`.
   - `engine_clock.run_tick(world, action_callback)` (`autoload/engine_clock.py:96-127`) composes, IN THIS ORDER:
     a. **SEASON_TICK** — `advance_season(world)` (season_manager.py:29-38): `world.season += 1`; if `season % 4 == 1` it's a new arc (`world.arc += 1`, `reset_arc()` on every faction); `reset_seasonal()` on every faction always.
     b. **ACTION** — `action_callback(world)` = `mc_v18._faction_actions_callback` (mc_v18.py:120-207): for each parliamentary faction holding territory, `composition.require('faction_action')(faction, world, world.rng)` (138, wrapped in try/except that prints to stderr on error, never swallows silently — 139-144); then `scene_dispatch.run_scene_phase(world, world.rng)` (149) which drains `scene_slate` and dispatches combat/contest/etc; then if `world.echo_scheduler` is set, `parliamentary_bridge.run_parliamentary_scene(world, world.rng)` (156-159); then two `stubwire.stub_resolve()` calls for `generate_npc` and `form_knot` — both explicitly NOT auto-triggered, honest deferrals (190-206).
     b'. **barrier**: `sched.accounting_boundary()` (engine_clock.py:122) if scheduler present — flips scheduler phase to ACCOUNTING and runs OF-7 deferred applies.
     c. **ACCOUNTING** — `composition.require('accounting')(world)` (engine_clock.py:123) -> `systems.overview.sim.accounting:run_accounting`.
     b''. **tick close**: `sched.next_tick()` (engine_clock.py:125) resets per-tick emission counter, returns scheduler to ACTION phase.
   - Barriers/writes: `accounting_boundary()` is the barrier that separates "deferred settlement-locus writes queued during ACTION" from "writes applied"; `next_tick()` is the barrier that resets the emission-cap window. **The per-tick emission cap spans BOTH phases** (engine_clock.py:113-116 comment) — resetting it before accounting (the pre-2026-08-27 bug) would have let a tick's total emissions exceed the cap unnoticed.
3. **Victory check** (mc_v18.py:263-267): `victory.check_all_factions(world)` each season; first `won=True` result sets `world.winner` and breaks the season loop.
4. **Fallback winner** (270-278) if no winner after `max_s` seasons: territory-count + L + territories-held score.
5. **Result assembly** (280-283): `CampaignResult` built from `world` state, `stubwire.invocations` delta, `key_log.content_hash()`/`len()` if a scheduler was attached.

`run_batch(n, base_seed, params)` (mc_v18.py:286-303) just loops `run_campaign` with `seed = base_seed + i` and aggregates win-share/battle-count.

---

## 5. DETERMINISM AS BUILT — RNG ownership, seeding, replay, hashing

- **Single seeded stream**: `World.rng: random.Random` (`game_state.py:265`), constructed as `random.Random(seed)` in `create_world` (game_state.py:306) and stored on `World` (339). This is **the** campaign RNG; every subsystem receives it (or a value derived from it) rather than drawing from the global `random` module directly — with one documented, deliberate exception (`scene_dispatch.py:299`, see below).
- **Propagation**: `world.rng` is passed explicitly to `faction_action` (mc_v18.py:138), `scene_dispatch.run_scene_phase` (149), `parliamentary_bridge.run_parliamentary_scene` (158).
- **Sub-stream derivation, not reseeding**: `combat_bridge.resolve()` (combat_bridge.py:140) does `fight_rng = random.Random(rng.getrandbits(32))` — derives an independent `random.Random` from the caller's stream via one `getrandbits` draw, so combat's internal draw count can't perturb the campaign stream's future draws.
- **Documented exception — global-state save/restore**: `scene_dispatch.py:299-306` — the contest kernel resolves off the **global** `random` module (not an injectable rng), so this call site does `prev_random_state = random.getstate(); random.seed(rng.getrandbits(32)); ... finally: random.setstate(prev_random_state)`. Comment explicitly notes reseeding from a **derived** value rather than a fixed pin, because a fixed pin "already learned breaks batch reproducibility" (massbattle.py precedent cited inline).
- **Replay/hashing**: `KeyLog.content_hash()` = `sha256(serialize())`, `serialize()` = newline-joined sorted-key JSON per Key in log order (keys.py:414-419). `CampaignResult.key_log_hash`/`keys_emitted` surface this per campaign (mc_v18.py:281-282). Two campaigns with the same seed and same code path produce byte-identical `key_log_hash` — pinned by `test_parliamentary_bridge.py` (`_ON_KEYLOG_HASH`, cited in `engine_clock.py` docstring).
- **Seeded regression goldens**: `engine/tests/test_mc_v18_regression.py` pins `run_batch(n=2, base_seed=0)` output (`GOLDEN_WIN_SHARE`, `GOLDEN_WINNERS`, `GOLDEN_BATTLES_MEAN` — test_mc_v18_regression.py:126-129) and asserts determinism (`test_mc_v18_batch_is_deterministic`, line 132: two runs of the same seed must be `==`). `engine/tests/test_f7_smoke_oracle.py` pins `run_batch(n=8, base_seed=42)` (win-share `{Crown 37.5, Church 12.5, Hafenmark 12.5, Varfell 37.5}` per its docstring, lines 16-18) plus `scenes_resolved`/`insurgencies_formed`/`npcs_generated` telemetry and a wall-time ceiling.
- **No independent PRNG per subsystem**: everything traces to one `random.Random(seed)` at world creation; there is no per-actor or per-Key seed.

---

## 6. THE PARAM/CONSTANT SURFACE

**Read only (did not run the exporter — files already present and pre-generated; running `--build` would write to the repo, which the task disallows).**

### Typed, cooked JSON artifacts under `engine/engine_params/` (each `_generated` by a `tools/export_*.py`, blocking `--check` round-trip):

| file | schema_version | shape | generated from |
|---|---|---|---|
| `combat_engine_v1.json` | 2 | `sections` (2 top-level groups) | `systems/combat/combat_engine_v1/config.py` + `core.py` |
| `composition.json` | 2 | `roles` — 27 entries, `{role: {target, kind, needed_by}}` | `references/module_contracts.yaml#composition_roles` |
| `descriptors.json` | 1 | `attributes`, `conviction_roster`, `faction_stats`(6), `faction_field_map`(6), `settlement_stats`(6), `practitioner_stats`(2), `territory_stats`(1), `unimplemented`(0) | `references/descriptor_registry.yaml` |
| `game_constants.json` | 1 | `constants`(13), `owners`(13), `collisions`(4), `divergences`(2) | `sim_params.json` + `combat_engine_v1.json` |
| `key_types.json` | 1 | `types` — 55 entries, `type_count: 55` | `systems/_architecture/key_type_registry_v30.md` |
| `module_contracts.json` | 1 | `modules`(27), `emit_edge_count: 60`, `consume_edge_count: 82`, `wildcard_consumers`(2), `unattributable`(14) | `references/module_contracts.yaml` |
| `sim_params.json` | 2 | `params` — **415** entries (list), `citation_coverage` | AST-read literal constants from the sim reference code |
| `value_pointer_links.json` | 1 | `links`(131), `by_pointer`(30), `by_value`(122) | literal-token cross-match between values and pointers |
| `world_initial_state.json` | 1 | `territories`(16), `faction_starting_stats`(4) | `references/world_initial_state.yaml` |

### `sim_params.json` `citation_coverage` — measured directly, this session, from the file as it stands on disk:
```
{'cited': 166, 'total': 415, 'uncited': 249, 'of_which_assumption_grade': 11}
```
Matches the order of magnitude of the figure CLAUDE.md's Section 0.05 correction cites (415 total, 11 assumption-grade), but see item 1 in Section 11 below for a 1-off discrepancy on the uncited count (249 measured live vs "248" quoted in CLAUDE.md).

Example entries (`sim_params.json` `params[0]`, `params[1]`):
```
{"key": "engine.autoload.ACCORD_MAP", "name": "ACCORD_MAP", "value": {"0": 1.0, ...}, "kind": "table", "module": "engine.autoload", "file": "engine/autoload/game_state.py", "citation": None, "citation_grade": None}
{"key": "engine.autoload.MULTS", "name": "MULTS", "value": {...}, "kind": "table", ...}
```
So even the constants that live inside `engine/` itself (`ACCORD_MAP`, `MULTS`, `PT_MAP`) are picked up by the exporter as **uncited** table literals — they are typed/exported but not provenance-tracked.

### `params_tables.yaml` — the byte-frozen prose capture, NOT a mechanism (per CLAUDE.md Section 0.05):
`_generated` header (params_tables.yaml:1): "GENERATED by tools/export_params_constants.py from engine/params/**/*.md. NEVER hand-edit... Where a value here disagrees with code, THE CODE WINS." `file_count: 37`, `table_count: 258`, `row_count: 1367`. This is reference-only — `dice_engine.degree_from_net`'s own docstring (dice_engine.py:264-270) explicitly disclaims it: the capture still shows the pre-ruling degree ladder (`Net >= 2*Ob` Overwhelming), while the code implements the margin-based ladder Jordan ruled 2026-08-14. **Confirmed live**: the exporter (`tools/export_params_constants.py`) that produced this capture was itself retired with its source, so this file can no longer be regenerated — its own header's "NEVER hand-edit" is now absolute (matching the discipline `world_initial_state.py` and `descriptors.py` docstrings cite for their live siblings).

### Constants still living as bare Python literals inside `engine/` (not exported/typed as a schema, though captured by the AST scraper into sim_params.json):
- `engine/autoload/game_state.py:74` — `MULTS = {'L': 20, 'Sta': 10, 'W': 100, 'I': 15, 'Mil': 10, 'accord': 10, 'pt': 10}` — deliberately NOT moved to the registry yet (docstring at 57-73 explains why: spans two registry blocks, and 3 of 7 numbers have no cited provenance).
- `game_state.py:76-77` — `ACCORD_MAP`, `PT_MAP` (5-6 entry float tables).
- `dice_engine.py:171-172` — `_MU_PER_DIE = 0.40`, `_SIGMA_PER_DIE = 0.800` (cite `params/core.md Section Expected Value, TN 7`).
- `sigma_leverage.py:81-99` — `PER_DIE`, `TN_STANDARD=7`, `LEVEL_SIGMA` (4-entry dict), `M_MAX=1.5`, `SIGMA_N_COEFF=0.8`, `OB_MIN=1`.
- `victory.py:23-26` — `VICTORY_THRESHOLD=15`, `ACCORD_MIN=2.0`, `PS_MAX=6.0`, `SUSTAIN_SEASONS=2`.
- `season_manager.py:15` — `SEASONS_PER_ARC=4`.
- `echo_transport.py:96-97` — `DEFAULT_CASCADE_DEPTH_MAX=0`, `DEFAULT_EMISSIONS_PER_TICK_MAX=64`.

All of the above show up in `sim_params.json`'s AST-scraped 415-entry roster (confirmed for `ACCORD_MAP`/`MULTS` above) — so "typed export" and "still a Python literal" are **not mutually exclusive**: the exporter captures the literal's current value into a typed JSON snapshot, but the literal itself remains the single live owner code reads at runtime. The JSON is a report on the literal, not a replacement for it.

### Constants still inside `systems/`: outside this lane's tree, cited for completeness only, not independently re-derived here — CLAUDE.md's Section 0.05 correction states 415 numeric constants total in `sim_params.json`'s scope, "of which 248 uncited and 11 assumption-grade," and names `systems/` as "the migration backlog, not a filing problem."

---

## 7. RECONCILIATION TABLE (the heart of this task)

| design object | exists in `engine/`? | what it's called there | file:line | same shape? | what would have to change |
|---|---|---|---|---|---|
| **Person** (incl. cohort = Person at weight>1) | **NO** | -- | -- | no | Nothing in `engine/` models an individual human actor with weight/identity. `Faction` is an aggregate (5-7 float stats), not a Person. `World.npcs: dict[territory_id -> list[NPC]]` (game_state.py:277) is the closest *slot*, but `NPC` itself lives in `systems/world/sim/npe.py` (outside this lane) and is late-imported by string (`composition.require('snapshot_state.npcs')`, game_state.py:469) — `engine/` never defines the class. A Person carrier would need a new dataclass at the substrate or autoload tier, plus a bridge from the aggregate `World.npcs` registry. |
| **Rung** | **NO**, but a shadow exists | `scale_signature` (list of `SCALES`) on every `Key`, plus informal "scale" vocabulary in `handoff_rules`/`zoom_in_out`/`scene_dispatch` (`SCALE_PERSONAL`, `SCALE_SCENE`, `SCALE_FACTION` constants) | `substrate/keys.py:50` (`SCALES`), `cross_scale/handoff_rules.py` (`SCALE_*` constants) | partial | `SCALES = ("personal", "settlement", "territory", "peninsula")` is a **flat enum of 4 strings**, not a composable container/tree object. The design's `Rung` is a first-class carrier (renamed from `Container`/`Node` specifically to avoid Godot collision); `engine/` has no such class — scale is a tag on a Key, not a thing Keys live inside. Would need a net-new type. |
| **Office** | **NO** | -- | -- | no | No concept of a role/seat distinct from the Faction holding it. `Faction.parliamentary: bool` (game_state.py:112) and the various `*_used_this_arc` flags gate *actions a faction may take*, not an office a Person occupies. Parliamentary machinery (`parliamentary_bridge.py`) operates directly on aggregate Faction stats, never through an Office intermediary. |
| **Site** | **NO** as a carrier, **YES** as an aggregate location | `Territory` (16 instances), `Settlement` (defined in `systems/settlements/sim/registry.py`, referenced via `World.settlements` registry, game_state.py:301) | `autoload/game_state.py:234` (`Territory`) | partial | `Territory` has 9 scalar fields (owner, accord, pt, garrison, prosperity, fort_level, templar, uncontrolled_since) — a strategic-layer stat bag, not an identity-bearing carrier in the design's sense (no Tenure edges attach to it beyond ad hoc string ids). Settlement is genuinely outside this lane (`systems/settlements/`). |
| **Tenure** (7 kinds incl. `hold`, `oblige`, `commit`) | **NO** | -- | -- | no | No edge type exists anywhere in `engine/`. Relationships are expressed as: (a) scalar dict membership (`Faction.territories: list[str]` — game_state.py:124 — a faction "holds" a territory only via list membership, no edge object, no kind, no provenance); (b) `Key.causes: list[str]` (keys.py:135) which is a **causal DAG edge between Keys**, not a relationship edge between carriers. Neither carries a `kind` enum. A Tenure substrate would be wholly new. |
| -- `hold` | NO | `Faction.territories` list membership | game_state.py:124 | no | as above |
| -- `oblige` | NO | -- | -- | no | closest analogue: nothing. Obligation/debt has no representation. |
| -- `commit` | NO | -- | -- | no | nothing |
| -- (4 other kinds, unnamed in task context) | NO | -- | -- | no | -- |
| **StateChange := (subject, mode, driver)** | **NO** as a unified triple, **partial** as two separate unrelated mechanisms | (1) `Key` (mode-like via `type`, no subject/driver partition); (2) `stubwire.StubResult` (marks "not built" rather than modeling a change) | `substrate/keys.py:126`, `substrate/stubwire.py:39` | no | `Key` carries `source_actor`/`targets[]`/`type`, but nothing partitions changes into mint/alter/efface, and nothing encodes "driver in Act|Event chosen by the subject" — Jordan's Partition is entirely absent. Every state write in `engine/` today is a direct field mutation (`Faction.adjust()`, `Territory.adjust_accord()`) that bypasses any Key/StateChange representation — the Key substrate is a **parallel observability/echo layer**, not the write path itself (see Section 9 below). |
| -- `mint` | NO | closest: nowhere. `World` object creation (`create_world`) is world-gen, not a per-entity mint event. | -- | no | -- |
| -- `alter` | **closest analogue exists** | `Faction.adjust()`, `Territory.adjust_accord/adjust_pt()` — direct mutation, clamped by registry bounds | game_state.py:153-196, 248-252 | partial (same *effect*, no *representation* as a typed StateChange) | These ARE the game's alter-events today, just not reified as objects — imperative method calls. A `StateChange(subject, mode='alter', driver=...)` object would need to wrap every one of these call sites (~31 non-test `.adjust()` sites alone). |
| -- `efface` | NO | nearest: `Territory.owner = None` (`is_uncontrolled()`, game_state.py:245-246) represents a territory losing its controller, but no generic "cease to exist" primitive exists for any carrier. | -- | no | -- |
| **Act** (`choose : (Person, View, Sensation) -> Act`) | **NO** | closest: `Action` type referenced only in unimplemented docstrings (`npc_ai.py` entry-point comments: "select_action(actor_id, world) -> Action") — `Action` is never actually defined anywhere in `engine/`. | `autoload/npc_ai.py:12` (docstring only) | no | `npc_ai.select_action`/`evaluate_priority_stack` are **both stub-wired** (npc_ai.py:31-46) — literally the only place `engine/` gestures at a "Person decides" primitive, and it returns a `StubResult`, never a real Act. No `View`/`Sensation` type exists at all. |
| **Event** (`resolve : (Act[], World) -> Event[]`) | **partial** | `Key` (as the emitted/logged record of something having happened) functions as an Event-like artifact, but nothing in `engine/` takes `Act[]` and produces `Key[]` through a pure `resolve` — the actual resolution paths (`faction_take_action`, `resolve_contest`, `wrapper.fight`) live in `systems/` and are called through `composition.require(...)`, each with its own bespoke signature — no uniform `resolve(Act[], World)->Event[]` signature exists anywhere. | `substrate/keys.py:126` (Key as Event-shadow) | no | Every subsystem resolver has its own ad hoc signature (Section 9 evidence below); unifying to `resolve(Act[], World)->Event[]` would be a rewrite of every `composition.json` role's callable signature, not an incremental change. |
| **Claim** (`witness : (Person, Event) -> Claim[]`, per-person, never a collection) | **NO** | -- | -- | no | `Key.visibility` (public/semi_public_observers/private_observers, keys.py:100-111) encodes *who may see* a Key, but nothing computes a per-witness `Claim` object — no function anywhere takes `(Person, Event)` and returns anything. `articulation.py`'s `render_protagonist_lens`/`generate_chronicle_entry` (cross_scale/articulation.py:35,53) are the nearest gesture at a witness-side render, and they are unimplemented stubs feeding the retired render layer. |
| **View** | **NO** | -- | -- | no | No type. `zoom_in_out.zoom_in()` returns a `ZoomInResult{scene_ob_modifier}` (zoom_in_out.py:48-54) — a single numeric modifier, not a per-person situational View. |
| **Sensation** | **NO** | -- | -- | no | No type anywhere in `engine/`. |
| **World** (resolve's second arg) | **YES, but shaped very differently** | `World` dataclass | `autoload/game_state.py:256-301` | partial | `engine/`'s `World` IS a single global mutable aggregate (factions/territories/clocks + 14 heterogeneous "Any-typed" registries, game_state.py:266-301 — explicitly documented as an accreted schema-migration pile, not a designed carrier index). If the design's `World` is meant as a clean index over the four carriers, `engine/`'s `World` would need a substantial internal rewrite, not just a rename. |
| **Query** (never stored, always recomputed) | **partial precedent exists, unnamed** | `canonical_accord()`/`canonical_pt()` (pure bucket functions, no storage) are Query-shaped; `descriptors.faction_bounds()` is Query-shaped (reads registry, computes, returns — never stores); by contrast `engine/`'s wider corpus term `Derived` means the **opposite** — a **stored** per-character value (see Section 8) | `substrate/canon_buckets.py:35-46`, `substrate/descriptors.py:98-108` | conceptually compatible, terminologically **colliding** with existing usage | The design's rename from `Derived`->`Query` is justified exactly by what Section 8 confirms: `engine/` and the wider corpus already use "Derived" for stored values, so re-using "Derived" for a never-stored recomputed category would collide with a live term of art. No code change required by this rename — it is purely a vocabulary fix that avoids a real, confirmed collision. |
| **choose** | **NO** | stub only (`npc_ai.select_action`) | `autoload/npc_ai.py:31` | no | see Act row |
| **resolve** | **NO uniform signature; many bespoke ones** | `composition.json`'s 27 roles, each a different signature | `engine_params/composition.json` | no | see Event row |
| **witness** | **NO** | -- | -- | no | see Claim row |
| **CALENDAR** (loop step 1) | **partial** | `season_manager.advance_season()` — arc/season counters and per-arc/per-season faction flag resets | `autoload/season_manager.py:29-38` | partial | Only resets faction flags; does not evaluate "what fires vs merely becomes reachable" per the design's step distinction — no convening-conditions concept exists. |
| **MATTER** (loop step 2, event barrier) | **NO clean match; scattered across ACCOUNTING** | `composition.require('accounting')(world)` -> `systems.overview.sim.accounting:run_accounting` (outside this lane) is the closest "world moves without a person choosing" phase, but it is not separated into its own barrier distinct from ACTION | `autoload/engine_clock.py:123` | partial | `engine/`'s loop has 3 phases (SEASON_TICK/ACTION/ACCOUNTING_BOUNDARY), not the design's 6 steps — MATTER's "the frozen world, and sense" concept has no engine-side analogue. |
| **DELIBERATE** (loop step 3) | **NO** | closest: `_faction_actions_callback`'s per-faction `composition.require('faction_action')` call (mc_v18.py:138) — but this is a **stochastic candidate-selection algorithm inside `systems/`**, not a `choose(Person, View, Sensation)->Act` call, and it operates on Factions, not Persons | `mc_v18.py:120-207` | no | Wholesale different mechanism: deterministic-mandatory-then-stochastic dispatch over aggregate factions, not per-person deliberation. |
| **RESOLVE** (loop step 4) | **YES, loosely** | `scene_dispatch._resolve_slot()` + `combat_bridge.resolve()` + `parliamentary_bridge.run_parliamentary_scene()` — genuinely a resolution phase that takes queued "acts" (scenes) and world state and produces outcomes | `cross_scale/scene_dispatch.py:217-395` | partial | Real resolution exists, dispatched per scene_type with bespoke per-type logic (combat/contest/fieldwork/investigation), not a uniform `resolve(Act[], World)->Event[]`. The design's "one roll, one obstacle" and "touch graph / conflict rule" have no engine-side analogue — `scene_dispatch` resolves scenes independently with no conflict/collision detection across concurrently-queued scenes. |
| **WITNESS** (loop step 5) | **NO** | nearest: `Key.visibility` block (who MAY see a Key) — but no step computes actual per-person Claims from it | `substrate/keys.py:100-111` | no | see Claim row above |
| **CENSUS** (loop step 6 — birth/death/demographic envelope) | **partial, and explicitly deferred** | `World.npc_counter`, `mc_v18`'s `stub_resolve('generate_npc', ...)` and `stub_resolve('form_knot', ...)` (mc_v18.py:190-206) — both **explicitly stub-wired, no automatic call site**; `victory.py`'s territory-count check is the only per-season "count something" pass | `mc_v18.py:190-206` | no (deliberately deferred, honestly, not fabricated) | The design's CENSUS (global pass, birth/death, de-individuation) has zero live analogue — `engine/` explicitly refuses to fabricate a generation trigger (mc_v18.py:198-201 comment cites "no canon head names an initial world-gen population nor a season-tick generation count... the honest move is to generate none automatically"). |

**Summary count**: of the ~22 design objects/signatures enumerated, **0 have a matching first-class type in `engine/`**. `Query`'s spirit (pure recompute, no storage) is already practiced (`canon_buckets`, `descriptors`), but the term "Derived" is taken by the opposite concept, confirming the rename is warranted. RESOLVE has the strongest partial precedent (real dispatch machinery exists). CENSUS/CALENDAR have weak partial precedents (season/arc bookkeeping exists but not the design's semantics). Person/Rung/Office/Tenure/Act/Claim/View/Sensation/choose/witness are **all absent** — a clean-sheet gap, not a refactor.

---

## 8. THE `Derived` COLLISION — established as fact

`references/glossary.md:75-82`:
```
| Full Term | Abbr | Formula lives at | Description |
|-----------|------|-------------------|-------------|
| Health | HP* | params/core.md Section Derived Scores; derived_stats_v30.md Section 4.1 (authoritative) | Wound track. Resets per wound. |
| Stamina | -- | params/core.md Section Derived Scores | Combat resource. Degrades per round. |
| Coherence | -- | params/core.md Section Derived Scores | Personal rendering stability for Thread practitioners. Starts at 10. |
| Intelligibility | -- | (see Coherence -- same source) | How legibly reality presents to a fractured practitioner. |
| Composure | -- | params/core.md Section Derived Scores | Social endurance track. Used in Debate. |
| Focus | -- | references/descriptor_registry.yaml (attribute) | ... |
| Truth | -- | params/core.md Section Truth Track (PP-551) | ... |
| Momentum | -- | params/core.md Section Derived Scores | Tactical resource. Gained on Overwhelming success. |
```
`engine/engine_params/params_tables.yaml` contains the literal heading `## Derived Scores` (line 3114, and line 9136 duplicate) and `- section: Derived Values (CR3 -- three trackers; ED-1056)` (line 2806) -- the frozen prose capture of exactly this table.

**What `Derived` means in this repo today**: a category of **stored, per-character tracked values** (Health, Stamina, Coherence, Composure, Momentum, etc.) that are computed from an attribute formula but then **persist as a mutable tracked number on the character sheet** (e.g. "Resets per wound", "Degrades per round", "Gained on Overwhelming success or Belief achieved") -- i.e. exactly the *opposite* of the proposal's `Query`, which is "never stored, always recomputed." `grep -rn "Derived" engine/` returns **zero hits** in any `engine/*.py` source file (only in the frozen `params_tables.yaml` capture) -- so the term is not currently load-bearing on any executable code path in `engine/`, but it is a live, corpus-wide term of art (glossary + params tables + presumably `systems/` design docs outside this lane's scope) that the design's rename correctly avoids colliding with.

---

## 9. WHAT `engine/` ALREADY DOES THAT THE DESIGN CLAIMS IS MISSING -- duplication findings

1. **A composable, role-resolved dependency substrate already exists and solves exactly the problem a carrier/edge redesign would reopen.** `engine/substrate/composition.py` resolves 27 declared roles by string from `references/module_contracts.yaml`, with a blocking export-time round-trip check (composition.py:1-46). Any new design primitive that needs to call into `systems/` should route through this, not reinvent a lookup mechanism.

2. **A deterministic, hash-verifiable "event log" already exists.** `KeyLog`/`Key`/`TickScheduler` (Section 2 above) is -- in spirit -- an Event-emission and Event-log substrate with ordering guarantees (SSI, cascade-depth caps, deferred-apply at accounting boundary), content-hashed for replay verification. The design's `Event`/`resolve` primitives would likely want to sit ON TOP of this substrate rather than replace it -- `Key` already has `causes: list[str]` (a causal DAG, matching the design's implicit need for event provenance) and a `visibility` block (a first cut at "who witnesses this").

3. **A single degree-of-success ladder, ruled and enforced as the sole owner, already exists.** `dice_engine.degree_from_net` (dice_engine.py:242-296) is explicitly "THE degree ladder... single owner for every scale of the game" -- any design object that needs an obstacle/margin resolution should call this, not define a new one. It even has a formal extension seam (`BandExtension`) for per-subsystem variance without re-forking the ladder.

4. **Deferred-write / accounting-boundary semantics already exist and match the design's "four barriers, four write classes" framing closely.** `TickScheduler`'s OF-7 deferred-apply (a Key is logged live, its settlement-locus *effect* deferred to `accounting_boundary()`) is architecturally the same shape as the proposal's barrier-gated write classes. A StateChange/mint/alter/efface design should reconcile against this existing barrier rather than re-derive one from scratch.

5. **Explicit, typed "honest deferral" (not-yet-built) already has a single owner.** `stubwire.StubResult`/`stub_resolve()` (Section 1 above) is the established idiom for "this is a real gap, flagged, not fabricated" -- used 4+ times already in this lane alone (`npc_ai.py` x2, `mc_v18.py` x2, `scene_dispatch.py` multiple). Any newly-discovered gap in the design's coverage should be recorded this way, not via new prose.

6. **A registry-driven bound/clamp mechanism for stat mutation already exists** (`descriptors.faction_bounds()`, game_state.py:153-196) -- floor/ceiling per stat pulled from a cooked registry rather than hardcoded, with a load-time completeness check (`assert_faction_roster_is_covered`, descriptors.py:64-120) that halts import if the registry and the dataclass disagree. This is a working instance of "canon changes the registry, code enforces it" -- the design's `Query`/registry vocabulary should point at this as a precedent for how bound values ought to be sourced.

---

## 10. WHAT THE DESIGN NEEDS THAT `engine/` CANNOT DO -- the real gaps

1. **No individual-actor representation at all.** `World` holds only aggregate Faction/Territory stats plus loosely-typed dict registries (`npcs`, `convictions`, `knots`, etc.) whose *element types* live entirely in `systems/`, not `engine/`. A `Person` carrier (and cohort-as-weighted-Person) requires a net-new first-class type at the `engine/autoload` or `engine/substrate` tier -- nothing to build on here besides the dict-registry pattern itself (game_state.py:274-301).

2. **No relationship/edge type exists at all -- `Tenure` has zero precedent.** The two things that come closest (`Faction.territories: list[str]` list membership, and `Key.causes: list[str]` causal citation) are both **unkinded, untyped associations**, not a typed edge object with 7 kinds. This is the single largest structural gap: nothing in `engine/` models "X holds/obliges/commits to Y" as a first-class relationship.

3. **No unified Act/Event/Claim pipeline -- every subsystem resolver has its own bespoke signature.** Confirmed directly from `composition.json`'s 27 roles: `faction_action(faction, world, rng)`, `resolve_contest(built)` (implicit signature via `build_contest`/`resolve_contest` pair), `wrapper.fight(A, B, cfg, rng, max_bouts)`, `run_parliamentary_vote(motion, decls, world, rng)` -- no two share a signature, let alone the design's uniform `(Person,View,Sensation)->Act` / `(Act[],World)->Event[]` / `(Person,Event)->Claim[]` triple. Unifying these would touch essentially every subsystem entry point this lane composes over.

4. **`degree_from_net`'s ladder is fixed at TN 7, ruled immutable ("TN7 always. Never change TN anywhere ever." -- dice_engine.py:180-182, 2026-08-25).** Any design mechanism (e.g. a Query-derived obstacle) that implicitly assumed a variable TN would conflict with a hard, recent ruling -- must resolve difficulty entirely through Ob, never TN.

5. **No per-person View/Sensation assembly exists -- `zoom_in()` returns one global numeric modifier, not a per-actor situational snapshot.** `ZoomInResult{scene_ob_modifier: float}` (zoom_in_out.py:48-54) is the entire "context a scene sees" mechanism today; it is not keyed to a Person and carries no visibility/knowledge model.

6. **CENSUS-shaped generation (birth/death) is explicitly and deliberately UNBUILT, not merely unlinked.** `mc_v18.py:190-206`'s two `stub_resolve()` calls document that no canon source names a world-gen population count or a season-tick generation trigger -- this is a genuine content/design gap upstream of any engine change, not an engine limitation per se, but it means CENSUS has literally nothing to call into today.

7. **The campaign loop currently has 3 phases (SEASON_TICK/ACTION/ACCOUNTING_BOUNDARY), not the design's 6 steps (CALENDAR/MATTER/DELIBERATE/RESOLVE/WITNESS/CENSUS).** `engine_clock.run_tick`'s docstring is explicit that it implements only the phase *ordering*, not the full drain topology (`autoload/engine_clock.py:16-22`) -- WITNESS and CENSUS in particular have no phase-boundary home to attach to without extending `engine_clock` itself.

8. **`World.rng` is a single shared stream; the design's per-Person `choose` would need to reason about whether per-actor determinism/replay matters, and nothing in the current substrate supports keying an RNG sub-stream per Person** (only per-*resolver-call*, via the `getrandbits(32)`-derive pattern in `combat_bridge.py:140`). If the design wants reproducible-per-actor decisions independent of draw order among other actors, that pattern would need generalizing.

---

## 11. Claims to escalate

1. **A 1-off discrepancy between the live sim_params.json and CLAUDE.md's own quoted correction, worth flagging rather than silently reconciling.** Live-read `sim_params.json.citation_coverage` this session: `{'cited': 166, 'total': 415, 'uncited': 249, 'of_which_assumption_grade': 11}`. CLAUDE.md's Section 0.05 correction states "415, of which 248 uncited and 11 assumption-grade." 415-166=249, which matches the live file exactly, not 248. Either the file moved by one entry since that correction was written, or the correction's arithmetic was off by one. Recommend a one-line fix to CLAUDE.md's Section 0.05 bracket (248 -> 249), or an explanation for the mismatch -- flagging per the CLAUDE.md falsifier discipline (both sides stated) rather than silently reconciling it myself.

2. **Confirms exactly** the `engine/` Section 3 CLAUDE.md claim about the `PATH_SEAM_ALLOWED` bare-name seam: `tests/valoria/test_engine_does_not_import_systems.py:212` -- `PATH_SEAM_ALLOWED = {'cross_scale/combat_bridge.py'}`, matching `combat_bridge.py`'s own extensive docstring about the lazy, memoized `sys.path` insert. No contradiction found.

3. **Confirms** the `engine/` Section 0.05 claim about `descriptors.faction_bounds()` closing the 5-vs-6 gap and Legitimacy's floor-0/ceiling-7 ruling -- `Faction.adjust()`'s docstring (game_state.py:153-196) and `descriptors.py:98-172`'s docstrings are internally consistent with each other and with CLAUDE.md's account, including the still-unreachable `fac.intel` case (game_state.py:164-171, `MULTS` has no `'intel'` key -- confirmed, `MULTS` dict at game_state.py:74 indeed omits `intel`).

4. **No contradiction found** between `engine/`'s executable state and the proposal's own self-description -- `02_THE_SEASON_LOOP.md:3-5` and `01_ARCHITECTURE.md` both open with "Nothing here has executed... done means it runs, and none of this runs," which this sweep independently corroborates: grepping the proposal's vocabulary (Person, Rung, Office, Tenure, StateChange, mint/alter/efface, Query, choose/resolve/witness, CALENDAR/MATTER/DELIBERATE/RESOLVE/WITNESS/CENSUS) against `engine/` finds **zero live occurrences** of any of these exact terms as code identifiers (only informal shape-precedents, catalogued in Section 7/Section 9 above).
