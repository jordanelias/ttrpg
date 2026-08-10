# _architecture — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/_architecture/` · **Lane:** `IN` · **Contracts:** `engine_clock` (declared in
`references/module_contracts.yaml`, `sim_module: none` — no code joined), `articulation_layer`
(`references/module_contracts.yaml`, `sim_module: engine/cross_scale/articulation.py`)
**Code roots traced:** `engine/substrate/`, `engine/cross_scale/`, plus the live call sites that
enter/exit them: `engine/mc_v18.py`, `engine/autoload/game_state.py`, `systems/factions/sim/faction_action.py`,
`systems/factions/sim/parliamentary_transfer.py`, `systems/overview/sim/rs_track.py`
**Traced at:** `6545067`

## 1. Entry points

| Callable | Anchor | Called-by |
|---|---|---|
| `TypeRegistry.load` | `engine/substrate/keys.py:213 load` | `engine/cross_scale/echo_transport.py:82` (inside `_registry`); also the cook-side caller `tools/export_key_types.py:63` (inside `build`) |
| `TypeRegistry.load_json` | `engine/substrate/keys.py:232 load_json` | `engine/substrate/keys.py:216` (internal dispatch inside `load`; no direct external caller anywhere in the tree) |
| `TypeRegistry.require` | `engine/substrate/keys.py:303 require` | `engine/substrate/keys.py:383 validate_payload` (internal) |
| `TypeRegistry.validate_payload` | `engine/substrate/keys.py:308 validate_payload` | `engine/substrate/keys.py:383` (inside `KeyLog._validate`, def at `:378`) |
| `TypeRegistry.apply_defaults` | `engine/substrate/keys.py:322 apply_defaults` | `engine/substrate/keys.py:566` (inside `_emit_at_depth`, def at `:555`) |
| `KeyLog.append` | `engine/substrate/keys.py:367 append` | `engine/substrate/keys.py:567` (inside `_emit_at_depth`; no caller appends directly — always reached via `TickScheduler.emit`) |
| `KeyLog.lookup` | `engine/substrate/keys.py:364 lookup` | `engine/substrate/keys.py:588` (inside `accounting_boundary`, def at `:581` — resolves the Key for every queued `_pending_apply` callable at the ACCOUNTING boundary, the hottest production path); also `engine/tests/test_accord_echo.py:311`, `engine/tests/test_echo_transport.py:89` |
| `KeyLog.serialize` | `engine/substrate/keys.py:453 serialize` | `engine/substrate/keys.py:460 content_hash` (internal) |
| `KeyLog.content_hash` | `engine/substrate/keys.py:459 content_hash` | `engine/mc_v18.py:305 key_log_hash` |
| `KeyLog.__len__` | `engine/substrate/keys.py:358 __len__` | `engine/mc_v18.py:306 keys_emitted` |
| `TickScheduler.subscribe` | `engine/substrate/keys.py:506 subscribe` | `engine/cross_scale/articulation.py:169` (inside `subscribe_all`, def at `:152`) |
| `TickScheduler.emit` | `engine/substrate/keys.py:510 emit` | `engine/cross_scale/echo_transport.py:343`, `:438`; `systems/factions/sim/faction_action.py:394`; `systems/factions/sim/parliamentary_transfer.py:176` |
| `TickScheduler.schedule_emission` | `engine/substrate/keys.py:525 schedule_emission` | — (no production caller anywhere in `engine/` or `systems/`; only `tests/valoria/test_key_substrate.py:331` etc.) |
| `TickScheduler.drain_tick` | `engine/substrate/keys.py:538 drain_tick` | — (no production caller; only `tests/valoria/test_key_substrate.py:336` etc.) |
| `TickScheduler.accounting_boundary` | `engine/substrate/keys.py:581 accounting_boundary` | `engine/mc_v18.py:160` |
| `TickScheduler.next_tick` | `engine/substrate/keys.py:593 next_tick` | `engine/mc_v18.py:161` |
| `canon_buckets.canonical_accord` | `engine/substrate/canon_buckets.py:38 canonical_accord` | `engine/autoload/game_state.py:33` (re-export); `systems/overview/sim/accounting.py:88`; `systems/world/sim/npe.py:189` |
| `stubwire.stub_resolve` | `engine/substrate/stubwire.py:54 stub_resolve` | `engine/cross_scale/articulation.py:141`; `engine/cross_scale/scene_dispatch.py:366`; `engine/mc_v18.py:186`; `systems/overview/sim/rs_track.py:29` (representative sample — dozens of call sites corpus-wide) |
| `domain_echo.compute_domain_echo` | `engine/cross_scale/domain_echo.py:79 compute_domain_echo` | `engine/cross_scale/echo_transport.py:409` (inside `emit_scene_echo`, def at `:360`) |
| `domain_echo.compute_accord_echo` | `engine/cross_scale/domain_echo.py:128 compute_accord_echo` | `engine/cross_scale/echo_transport.py:450` (inside `emit_scene_echo`, def at `:360`) |
| `domain_echo.compute_thread_echo` | `engine/cross_scale/domain_echo.py:186 compute_thread_echo` | — (zero callers anywhere in the corpus, including tests) |
| `handoff_rules.apply_handoff` | `engine/cross_scale/handoff_rules.py:92 apply_handoff` | `engine/cross_scale/scene_dispatch.py:188` (inside `_handoff_validity_check_pair`, def at `:163`) |
| `zoom_in_out.zoom_in` | `engine/cross_scale/zoom_in_out.py:72 zoom_in` | `engine/cross_scale/scene_dispatch.py:219 _resolve_slot` |
| `zoom_in_out.zoom_out` | `engine/cross_scale/zoom_in_out.py:99 zoom_out` | `engine/cross_scale/scene_dispatch.py:396` (inside `_resolve_slot`, def at `:216`) |
| `zoom_in_out.check_mandatory_triggers` | `engine/cross_scale/zoom_in_out.py:165 check_mandatory_triggers` | `engine/cross_scale/scene_dispatch.py:97` (inside `evaluate_triggers`, def at `:75`) |
| `echo_transport.classify_scene_outcome` | `engine/cross_scale/echo_transport.py:134 classify_scene_outcome` | `engine/cross_scale/echo_transport.py:448` (inside `emit_scene_echo`, def at `:360`; internal) |
| `echo_transport.make_scheduler` | `engine/cross_scale/echo_transport.py:173 make_scheduler` | `engine/mc_v18.py:243` |
| `echo_transport.emit_scene_echo` | `engine/cross_scale/echo_transport.py:360 emit_scene_echo` | `engine/cross_scale/scene_dispatch.py:392` (inside `_resolve_slot`); `engine/cross_scale/parliamentary_bridge.py:212` (inside `run_parliamentary_scene`, def at `:180`) |
| `scene_dispatch.evaluate_triggers` | `engine/cross_scale/scene_dispatch.py:75 evaluate_triggers` | `engine/cross_scale/scene_dispatch.py:103 queue_triggered_scenes` (internal) |
| `scene_dispatch.queue_triggered_scenes` | `engine/cross_scale/scene_dispatch.py:102 queue_triggered_scenes` | `engine/cross_scale/scene_dispatch.py:420` (inside `run_scene_phase`, def at `:416`; internal) |
| `scene_dispatch.dispatch_scenes` | `engine/cross_scale/scene_dispatch.py:401 dispatch_scenes` | `engine/cross_scale/scene_dispatch.py:421` (inside `run_scene_phase`, def at `:416`; internal) |
| `scene_dispatch.run_scene_phase` | `engine/cross_scale/scene_dispatch.py:416 run_scene_phase` | `engine/mc_v18.py:141` |
| `parliamentary_bridge.run_parliamentary_scene` | `engine/cross_scale/parliamentary_bridge.py:180 run_parliamentary_scene` | `engine/mc_v18.py:150` |
| `articulation.render_protagonist_lens` | `engine/cross_scale/articulation.py:35 render_protagonist_lens` | — (zero callers anywhere in the corpus, including tests) |
| `articulation.evaluate_articulation_triggers` | `engine/cross_scale/articulation.py:44 evaluate_articulation_triggers` | `engine/tests/test_pipeline_reach.py:773` (test-only probe; no production caller) |
| `articulation.generate_chronicle_entry` | `engine/cross_scale/articulation.py:53 generate_chronicle_entry` | — (zero callers anywhere in the corpus, including tests) |
| `articulation.subscribe_all` | `engine/cross_scale/articulation.py:152 subscribe_all` | `engine/mc_v18.py:258` |
| `combat_bridge.derive_parties` | `engine/cross_scale/combat_bridge.py:114 derive_parties` | `engine/cross_scale/scene_dispatch.py:234` (inside `_resolve_slot`; only reachable when `world.dispatch_combat_bridge` is True — default False, `engine/mc_v18.py:81`) |
| `combat_bridge.resolve` | `engine/cross_scale/combat_bridge.py:131 resolve` | `engine/cross_scale/scene_dispatch.py:238` (inside `_resolve_slot`; same default-off gate) |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `Key`/`Target`/`EmittedAt`/`Visibility` construction | key | Caller-built at each emit site (`echo_transport`, `faction_action`, `parliamentary_transfer`) | `engine/substrate/keys.py:138 Key` |
| Cooked Key-type registry (`key_types.json`) | file | `tools/export_key_types.py` cook of `systems/_architecture/key_type_registry_v30.md` | `engine/cross_scale/echo_transport.py:68-69 _REGISTRY_PATH` |
| `world` (GameState) | world-state | `engine/autoload/game_state.create_world`, called by `engine/mc_v18.py:224` | `engine/cross_scale/scene_dispatch.py:75 evaluate_triggers` (param) |
| `rng` | arg | `world.rng`, threaded by the caller | `engine/mc_v18.py:141` (`scene_dispatch.run_scene_phase(world, world.rng)`) |
| Scene `ctx` dict (incl. optional `ctx['echo']` block) | arg | `engine/autoload/scene_slate.queue_scene` payload, built by `scene_dispatch.evaluate_triggers`/callers | `engine/cross_scale/scene_dispatch.py:105 queue_triggered_scenes` |
| `ECHO_TRANSPORT` flag | flag | `effective_params` dict or `os.environ`, default ON | `engine/mc_v18.py:57-67 _echo_transport_on` |
| `DISPATCH_COMBAT_BRIDGE` flag | flag | `effective_params` dict or `os.environ`, default OFF | `engine/mc_v18.py:70-81 _dispatch_combat_bridge_on` |
| `ECHO_CASCADE_DEPTH_MAX` / `ECHO_EMISSIONS_PER_TICK_MAX` | param | `effective_params`, defaulted from `echo_transport` module constants | `engine/mc_v18.py:244-247` |
| `world.factions` (Faction stats, `MULTS`) | world-state | `engine.autoload.game_state` | `engine/cross_scale/echo_transport.py:56` (from engine.autoload.game_state import MULTS) |
| `world.settlements` | world-state | `systems.settlements.sim.registry` | `engine/cross_scale/echo_transport.py:58`, read at `:292-293` |
| `world.season` | world-state | `engine.autoload.game_state` | read by every emitter to build `EmittedAt.season_index` — `engine/cross_scale/echo_transport.py:308`, also `:413` |
| `echo['scope_met']` | key | `ctx['echo']` block (see above), defaults True | `engine/cross_scale/echo_transport.py:390` |
| `echo['degree']` | key | `ctx['echo']` block, falls back to `_derive_degree` when absent | `engine/cross_scale/echo_transport.py:389` |
| `echo['target_settlement']` | key | `ctx['echo']` block | `engine/cross_scale/echo_transport.py:291` |
| `VALORIA_STRICT_KEYS` env var | flag | `os.environ`, default off (swallow validation errors) | `systems/factions/sim/faction_action.py:396` |

## 3. Flow

**S0 — the substrate's single update rule** (`TickScheduler.emit()` → `_emit_at_depth`, invoked by
every emit site below; this is the emit→validate→append→observers path):

- S0.1 `[gate]` B1 no-sync-reentry: a subscriber that calls `emit()` (not `schedule_emission()`) while `_in_drain` is True raises `TerminationBreach` — structurally unreachable in production, since `_in_drain` is set only inside `drain_tick`, which has zero production callers (§7) — `engine/substrate/keys.py:518-523 emit`
- S0.2 `[gate]` cascade-depth cap and emissions-per-tick cap checked; raises `TerminationBreach` on breach — the cascade-depth cap is also structurally unreachable in production, since `emit()` always passes depth 0 (`:523`) while the caller-supplied default cap is 0 (§7); the emissions-per-tick cap is the only one of the two guards that is live — `engine/substrate/keys.py:556-565 _emit_at_depth`
- S0.3 `[write]` `TypeRegistry.apply_defaults` fills unset `scale_signature`/`permanence`/`time_horizon` from the type's registry entry — `engine/substrate/keys.py:566`
- S0.4 `[write]` `KeyLog.append` runs `_validate` (invariants 1 id-uniqueness, 2 payload-contract, 3 causes-exist, 5 season-monotonic, 6 axis-names, 7 scale-signature, 8 visibility-shape), then the default-off WARN-tier `stat_vocabulary` check (§7), then assigns `sub_step_index` as the per-season append counter — `engine/substrate/keys.py:367-376`, invariants at `engine/substrate/keys.py:378-434`, vocabulary check at `engine/substrate/keys.py:369-370`
- S0.5 `[branch]` if an `apply` callable was supplied: under OF-7 (`defer_apply` default True) and `_phase == ACTION`, queues `(key.id, apply)` to `_pending_apply`; otherwise applies inline immediately — `engine/substrate/keys.py:569-573`
- S0.6 `[emit]` synchronous subscriber notify: every callback registered for `key.type` runs with `(key, scheduler)` — `engine/substrate/keys.py:576-577`

Causal graph: `causes[]` is populated in exactly one place corpus-wide — `_apply_accord_echo` sets
`causes=[caused_by_key_id]` when the sibling domain-echo leg fired for the same scene resolution,
`[]` otherwise (never fabricated) — `engine/cross_scale/echo_transport.py:317`. Cycle-freedom (invariant 4)
holds by construction because the log is append-only and invariant 3 only allows citing already-logged
ids — `engine/substrate/keys.py:390-392` (comment) / `:384-389` (enforcement).

**Season-loop level** (`engine/mc_v18.py`, per campaign then per season):

- S1 `[gate]` `run_campaign` decides `DISPATCH_COMBAT_BRIDGE` once, stashes on `world` — `engine/mc_v18.py:237`
- S2 `[branch]` if `ECHO_TRANSPORT` on: `echo_transport.make_scheduler` builds `TypeRegistry.load` → `KeyLog` → `TickScheduler`, attached as `world.echo_scheduler`/`world.key_log` — `engine/mc_v18.py:241-249`, `engine/cross_scale/echo_transport.py:181-184`
- S2.1 `[write]` `articulation.subscribe_all` registers 13 Tier-2 trigger callbacks (§3.1 roster) on the scheduler — `engine/mc_v18.py:257-258`, `engine/cross_scale/articulation.py:168-170`
- S3 `[loop]` per season, `run_season` invokes `_faction_actions_callback` — `engine/mc_v18.py:267`, `:116`
  - S3.1 `[loop]` per parliamentary faction with territory: `faction_take_action`; may reach `_try_conquest` → `resolve_mass_battle` → `[emit]` `_emit_battle_concluded` (`sched.emit(key)`, no `apply=`, log-only) — `engine/mc_v18.py:124-136`; `systems/factions/sim/faction_action.py:429-459`, emit at `:394`
  - S3.2 `scene_dispatch.run_scene_phase(world, rng)` — `engine/mc_v18.py:141`
    - S3.2.1 `queue_triggered_scenes`: `evaluate_triggers` scans `world.factions` for the one field-evaluable §4.3.2 trigger (Stability Crisis), queues via `scene_slate.queue_scene` — `engine/cross_scale/scene_dispatch.py:75-99`, `:102-106`
    - S3.2.2 `[loop]` `dispatch_scenes` drains `scene_slate` one slot at a time — `engine/cross_scale/scene_dispatch.py:401-413`
      - S3.2.2.1 `zoom_in_out.zoom_in` validates entry phase, computes scene Ob modifier — `engine/cross_scale/scene_dispatch.py:219-220`
      - S3.2.2.2 `[branch]` resolver dispatch by `scene_type`: `combat` (bridge if `DISPATCH_COMBAT_BRIDGE` on, else deprecated `combat.resolve_combat_round`), `contest` (`social_contest.sim.contest.build_contest`/`resolve_contest`), `fieldwork`/`investigation` (stub-wired), else stub-wired total-mapping fallback — `engine/cross_scale/scene_dispatch.py:224-371`
      - S3.2.2.3 `[gate]` handoff validity check over `handoff_rules.apply_handoff` for the scene's derived `(Scene, Faction)` pair — `engine/cross_scale/scene_dispatch.py:381-384`, `engine/cross_scale/handoff_rules.py:92-232`
      - S3.2.2.4 `[branch]` if `world.echo_scheduler` present: `echo_transport.emit_scene_echo(scene_type, result, ctx, world)` — `engine/cross_scale/scene_dispatch.py:390-393`
        - S3.2.2.4.1 `[gate]` requires `ctx['echo']` block + a `KEY_TYPE_BY_SCENE` mapping — `engine/cross_scale/echo_transport.py:379-387`
        - S3.2.2.4.2 `domain_echo.compute_domain_echo` — `engine/cross_scale/echo_transport.py:409`
        - S3.2.2.4.3 `[emit][write]` if `er.fires`: builds a `scene.*_resolved` Key, `sched.emit(key, apply=...)` where `apply` adjusts Faction stat via `MULTS` (S0 above governs landing) — `engine/cross_scale/echo_transport.py:416-438`
        - S3.2.2.4.4 `[gate]` `scope_met` (read at `engine/cross_scale/echo_transport.py:390`, threaded into `compute_domain_echo` at S3.2.2.4.2) gates the entire Accord leg below — `engine/cross_scale/echo_transport.py:447`
        - S3.2.2.4.5 `[gate]` `classify_scene_outcome` requires an explicit caller-declared `echo['scene_outcome']` — `engine/cross_scale/echo_transport.py:448`, `engine/cross_scale/echo_transport.py:164-170`
        - S3.2.2.4.6 `[branch]` if classified: `domain_echo.compute_accord_echo` — `engine/cross_scale/echo_transport.py:450`
        - S3.2.2.4.7 `[emit][write]` if `ar.fires`: builds a `scene.accord_echo` Key (`causes` per S0's causal-graph note), `sched.emit(key, apply=...)` where `apply` writes `Settlement.order` — `engine/cross_scale/echo_transport.py:304-343`
        - S3.2.2.4.8 `[write]` if `ar.rs_delta`: calls `rs_track.apply_rs_delta` — `engine/cross_scale/echo_transport.py:354-355` (see §7 — this is itself a stub)
      - S3.2.2.5 `zoom_in_out.zoom_out` folds `accord_applied`/`other_echoes` into `ZoomOutResult.domain_echoes_queued` (`notes` receives unrelated entries — PC-incapacitation/Contested-Figure-wound/Phase-6 notices, not the echo dicts); performs no additional writes itself — `engine/cross_scale/scene_dispatch.py:396`, `engine/cross_scale/zoom_in_out.py:131-136`; recorded by the caller into `out["domain_echoes"]` at `engine/cross_scale/scene_dispatch.py:397`
  - S3.3 `[branch]` if `world.echo_scheduler` present: `parliamentary_bridge.run_parliamentary_scene` — `engine/mc_v18.py:148-152`
    - S3.3.1 `_derive_vote` picks proposer (lowest Stability)/establishment (highest Mandate) — `engine/cross_scale/parliamentary_bridge.py:82-97`
    - S3.3.2 `[branch]` if `_derive_vote` returns `None` (fewer than two eligible parliamentary factions): S3.3.3/.3.4 are skipped, jumping straight to S3.3.5 — `engine/cross_scale/parliamentary_bridge.py:192-196`
    - S3.3.3 `run_parliamentary_vote` (SC-lane) applies the loser Mandate penalty directly — not via a Key — `engine/cross_scale/parliamentary_bridge.py:199`
    - S3.3.4 `[branch][emit]` winner echo composed and routed through the SAME `emit_scene_echo` path as S3.2.2.4 — `engine/cross_scale/parliamentary_bridge.py:205-213`
    - S3.3.5 `[branch]` `_run_transfer_motion` → `parliamentary_transfer.propose_transfer` runs on BOTH the S3.3.2 no-vote branch and the normal path — `engine/cross_scale/parliamentary_bridge.py:194` (no-vote branch), `engine/cross_scale/parliamentary_bridge.py:217` (normal branch); on a successful transfer, `[emit]` `_emit_public_governance_transfer` (`sched.emit(key)`, no `apply=`, log-only) — `systems/factions/sim/parliamentary_transfer.py:294`, emit at `systems/factions/sim/parliamentary_transfer.py:176`
  - S3.4 `[write][gate]` `accounting_boundary()`: runs every queued `_pending_apply` callable in emission order — this is where the deferred Faction/Settlement writes from S3.2.2.4.3/.4.7 actually land; resets phase — `engine/mc_v18.py:158-160`, `engine/substrate/keys.py:581-591`
  - S3.5 `next_tick()`: raises `TerminationBreach` if the emission queue is non-empty, else resets the per-tick emission counter — `engine/mc_v18.py:161`, `engine/substrate/keys.py:593-601`
- S4 at campaign end: `KeyLog.content_hash()` / `len(KeyLog)` read into `CampaignResult` telemetry — `engine/mc_v18.py:305-306`

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `Faction.adjust(stat, delta)` call | write | `engine.autoload.game_state.Faction` | `engine/cross_scale/echo_transport.py:430-436` (`_apply` closure) |
| `Settlement.order` write | write | `systems.settlements.sim.registry.Settlement` | `engine/cross_scale/echo_transport.py:325-341` (`_apply` closure) |
| `rs_track.apply_rs_delta` call | write (never lands — see §7) | `systems.overview.sim.rs_track` | `engine/cross_scale/echo_transport.py:354-355`; stub body `systems/overview/sim/rs_track.py:28-33` |
| `scene.battle_concluded` / `da.public_governance` Keys | key (log-only, no `apply=`) | `KeyLog` (telemetry only — no live reader beyond counts) | `systems/factions/sim/faction_action.py:361-394`; `systems/factions/sim/parliamentary_transfer.py:162-176` |
| `CampaignResult.key_log_hash` / `.keys_emitted` / `.stub_hits` | telemetry | `engine.mc_v18.CampaignResult`, read by `run_batch`/callers | `engine/mc_v18.py:103-104`, `:300`, `:305-306` |
| `HandoffResult` (from `apply_handoff`) | value | `scene_dispatch._handoff_validity_check_pair`, folded into the per-slot `out` dict as `handoff_stub`/`handoff_reason` | `engine/cross_scale/scene_dispatch.py:188-195`, `:381-384` |
| `ZoomTrigger` list (from `check_mandatory_triggers`) | value | `scene_dispatch.evaluate_triggers` (filters the `deferred` trigger-name list) | `engine/cross_scale/zoom_in_out.py:165-198`, `engine/cross_scale/scene_dispatch.py:97-98` |
| `ZoomOutResult` (from `zoom_out`, incl. `.domain_echoes_queued`) | value | `scene_dispatch._resolve_slot`, folded into the per-slot `out["domain_echoes"]` | `engine/cross_scale/zoom_in_out.py:99-162`, `engine/cross_scale/scene_dispatch.py:396-397` |
| `StubResult` (from `stub_resolve`) | value | Whichever caller records `.stub`/`.reason` (e.g. `scene_dispatch`'s per-slot `out` dict); `mc_v18` only counts invocations, discards the value | `engine/substrate/stubwire.py:34-43` |

## 5. State touched

| Field | R/W/RW | Owning module | Anchor |
|---|---|---|---|
| `world.echo_scheduler` | RW | `engine.mc_v18` writes (attach); read throughout `engine/cross_scale/` as the ECHO_TRANSPORT gate | W: `engine/mc_v18.py:243`; R: `engine/cross_scale/scene_dispatch.py:390`, `engine/cross_scale/parliamentary_bridge.py:190`, `systems/factions/sim/faction_action.py:348`, `systems/factions/sim/parliamentary_transfer.py:153` |
| `world.key_log` | RW | `engine.mc_v18` | W: `engine/mc_v18.py:249`; R: `engine/mc_v18.py:290`, `engine/mc_v18.py:305-306` |
| `world._echo_key_seq` | RW | `engine.cross_scale.echo_transport` | `engine/cross_scale/echo_transport.py:306-307`, `engine/cross_scale/echo_transport.py:411-412` |
| `world.season` | R | `engine.autoload.game_state` (owned elsewhere; this subsystem only reads) | `engine/cross_scale/echo_transport.py:308`, `engine/cross_scale/echo_transport.py:413`; monotonicity invariant enforced at `engine/substrate/keys.py:395-398` |
| `world.dispatch_combat_bridge` | RW | `engine.mc_v18` writes; `scene_dispatch` reads | W: `engine/mc_v18.py:237`; R: `engine/cross_scale/scene_dispatch.py:232` |
| `world.scenes_resolved` | RW | `engine.mc_v18` (dataclass field owned by `engine.autoload.game_state`) | field: `engine/autoload/game_state.py:172`; RW: `engine/mc_v18.py:142`, `engine/mc_v18.py:152` |
| `world._battle_key_seq` | RW | `systems.factions.sim.faction_action` | `systems/factions/sim/faction_action.py:354-355` |
| `world._parl_key_seq` | RW | `systems.factions.sim.parliamentary_transfer` | `systems/factions/sim/parliamentary_transfer.py:159-160` |
| Faction stat (`L`/`Sta`/`W`/`I`/`Mil`, via `.adjust`) | W | `engine.autoload.game_state.Faction` | `engine/cross_scale/echo_transport.py:435-436` |
| `Settlement.order` | W | `systems.settlements.sim.registry` | `engine/cross_scale/echo_transport.py:335-341` |
| `TickScheduler.subscriptions` | RW | `engine.substrate.keys` (W: subscribe; R: notify) | W: `engine/cross_scale/articulation.py:169`; R: `engine/substrate/keys.py:576` |
| `TickScheduler._pending_apply` | RW | `engine.substrate.keys` (W: queue; R: drain at `accounting_boundary`) | W: `engine/substrate/keys.py:571`; R: `engine/substrate/keys.py:587-590` |
| `TickScheduler._queue` | RW | `engine.substrate.keys` (never reached in production — see §7) | W: `engine/substrate/keys.py:536`; R: `engine/substrate/keys.py:546` |
| `stubwire.invocations` | W | `engine.substrate.stubwire` (module-level counter this subsystem writes; derived output listed in §4 as `CampaignResult.stub_hits`) | `engine/substrate/stubwire.py:65-66` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| down | `engine.autoload.game_state` | Reads `Faction`/`World`/`MULTS`; writes via `Faction.adjust` | `engine/cross_scale/echo_transport.py:56` |
| down | `engine.autoload.scene_slate` | `queue_scene`/`pending_count`/`next_scene` | `engine/cross_scale/scene_dispatch.py:66`, `:105`, `:403-404` |
| down | `systems.settlements.sim.registry` | `Settlement.order` read/write, `STAT_MIN`/`STAT_MAX` bounds | `engine/cross_scale/echo_transport.py:58`, `:335` |
| down | `systems.overview.sim.rs_track` | `apply_rs_delta` (stub — see §7) | `engine/cross_scale/echo_transport.py:354` |
| lateral | `systems.social_contest.sim.contest` (SC) | `build_contest`/`resolve_contest` | `engine/cross_scale/scene_dispatch.py:287-299` |
| lateral | `systems.social_contest.sim.parliamentary_vote` (SC) | `run_parliamentary_vote` | `engine/cross_scale/parliamentary_bridge.py:65`, `:199` |
| lateral | `systems.factions.sim.parliamentary_transfer` (FA) | `propose_transfer` + CB-availability helpers | `engine/cross_scale/parliamentary_bridge.py:64`, `:173` |
| lateral | `systems.combat.sim.combat` (deprecated) / `combat_engine_v1` (PC) | `resolve_combat_round` / `wrapper.fight` | `engine/cross_scale/scene_dispatch.py:273-274`; `engine/cross_scale/combat_bridge.py:97-98`, `:141` |
| lateral | `systems.fieldwork.sim.fieldwork` / `investigation` (FI) | stub-wired resolvers | `engine/cross_scale/scene_dispatch.py:351-356` |
| in (up) | `systems.factions.sim.faction_action` (FA) | Direct `TickScheduler.emit` call into the substrate from outside `engine/cross_scale/` | `systems/factions/sim/faction_action.py:394` |
| in (up) | `systems.factions.sim.parliamentary_transfer` (FA) | Direct `TickScheduler.emit` call into the substrate from outside `engine/cross_scale/` | `systems/factions/sim/parliamentary_transfer.py:176` |
| up | `engine.mc_v18` | Top-level orchestrator: owns flag decisions and every season-loop call into this subsystem | `engine/mc_v18.py:141`, `:148-152`, `:158-161`, `:241-258` |

## 7. Traced gaps

| Gap | Evidence anchor |
|---|---|
| `engine/cross_scale/__init__.py` is docstring-only — no re-exports, no package-level wiring — unlike `engine/substrate/__init__.py`, which re-exports its full public API | `engine/cross_scale/__init__.py:1-11` (whole file); contrast `engine/substrate/__init__.py:26-41` |
| `TickScheduler.schedule_emission`/`drain_tick` (the B1 re-entrant/cascade-queue path) have ZERO production callers anywhere in `engine/` or `systems/` — every live emission in the corpus goes through `emit()` at cascade_depth 0; only `tests/valoria/test_key_substrate.py` exercises the queue | `engine/substrate/keys.py:525 schedule_emission`, `engine/substrate/keys.py:538 drain_tick`; corroborated by `DEFAULT_CASCADE_DEPTH_MAX = 0`, `engine/cross_scale/echo_transport.py:91` |
| Both S0 termination guards other than the emissions-per-tick cap are structurally unreachable in production: the cascade-depth cap (`_emit_at_depth`) can never trip because `emit()` always passes depth 0 while the caller-supplied default cap is 0; the B1 re-entry gate (`emit()`) can never trip because it requires `_in_drain`, set only inside `drain_tick`, which (row above) has zero production callers. The per-tick emissions cap is the only live termination guard. | `engine/substrate/keys.py:523 emit`, `engine/substrate/keys.py:556-560 _emit_at_depth`, `engine/substrate/keys.py:518-523 emit`, `engine/cross_scale/echo_transport.py:91` |
| `combat_bridge.derive_parties`/`resolve` are unreachable in production regardless of the `DISPATCH_COMBAT_BRIDGE` flag's value: `evaluate_triggers` only ever appends `scene_type: "contest"`, so no scene is ever queued with `scene_type == "combat"` for `_resolve_slot`'s combat branch (or `KEY_TYPE_BY_SCENE['combat']`/articulation's combat subscriptions) to reach | `engine/cross_scale/scene_dispatch.py:84-95 evaluate_triggers` |
| `KeyLog.append`'s WARN-tier `stat_vocabulary` check (`_check_stat_vocabulary`, candidate invariant 9) runs only when a caller supplies `stat_vocabulary` at construction; `make_scheduler` always constructs `KeyLog` with none, so the check is default-off corpus-wide | `engine/substrate/keys.py:369-370` (guard), `engine/substrate/keys.py:436-451 _check_stat_vocabulary`; `engine/cross_scale/echo_transport.py:181 make_scheduler` |
| `articulation.render_protagonist_lens` and `articulation.generate_chronicle_entry` have ZERO callers anywhere in the corpus, including tests | `engine/cross_scale/articulation.py:35-41`, `:53-59`; repo-wide grep for both names returns only their own def/docstring lines |
| `domain_echo.compute_thread_echo` (the §5.6 Thread Echo leg) has ZERO callers anywhere in the corpus, including tests | `engine/cross_scale/domain_echo.py:186-216`; repo-wide grep returns only its own def and its module-docstring listing at `:19` |
| `handoff_rules.apply_handoff` is production-reachable for exactly 1 of its 8 declared `(from_scale, to_scale)` pairs — `(Scene, Faction)` — via `_HANDOFF_SCALE_PAIR_BY_SCENE_TYPE`; the other 7 rules are exercised only by `tests/valoria/test_handoff_dispatch_validity.py`, never by a live dispatch call | `engine/cross_scale/scene_dispatch.py:157-160` (dict has exactly 2 entries, both mapping to `(SCALE_SCENE, SCALE_FACTION)`) |
| The §5.5 Accord Echo's RS component routes to `rs_track.apply_rs_delta`, itself a Pass-2l armature stub — the write described in `compute_accord_echo`'s violence-row notes never lands on any world field | `engine/cross_scale/echo_transport.py:354-355` call site; stub body `systems/overview/sim/rs_track.py:28-33` |
| The whole Accord-Echo branch (S3.2.2.4.4-.4.7) is organically DORMANT in any seeded campaign — no live producer ever sets `ctx['echo']['scene_outcome']`, so `classify_scene_outcome` always returns `None` in production | `engine/cross_scale/echo_transport.py:36-38`, `:157-162` (module's own recorded dormancy note, re-verified in-file) |
| `render_protagonist_lens`/`evaluate_articulation_triggers`/`generate_chronicle_entry` are all `stubwire.stub_resolve` typed no-ops (Pass-2l armature stubs), not implementations; of the three, only `evaluate_articulation_triggers` is reached at all, and only by a test probe, never production code | `engine/cross_scale/articulation.py:35-59`; probe at `engine/tests/test_pipeline_reach.py:762`, `:773` |
| `engine_clock` — the `module_contracts.yaml`-declared contract this scheduler notionally realizes — carries `sim_module: none`; no code was ever joined to `TickScheduler`/`KeyLog` under that contract name | `references/module_contracts.yaml:863-866` |
| `TypeRegistry.load_json` is never called directly by any production or test call site; it is reached exclusively through `TypeRegistry.load`'s suffix dispatch | `engine/substrate/keys.py:213-216`; repo-wide grep for `.load_json(` outside `keys.py` itself returns nothing |
| `faction_action.py`'s in-code claim carries two stale statements. (1) "THE FIRST KEY EMISSION OUTSIDE `echo_transport`" is stale as of this trace — a third non-`echo_transport` emitter now exists (`parliamentary_transfer.py`'s `_emit_public_governance_transfer`), not named by that comment. (2) The same span's measurement that `scene.accord_echo` was the substrate's sole live emitter at 13 keys/campaign cannot hold given this skeleton's own dormancy row above (the whole Accord-Echo branch is organically dormant, `classify_scene_outcome` always returns `None` in production) — the live per-campaign emitter is `scene.contest_resolved` via the domain-echo leg's `sched.emit` call | `systems/factions/sim/faction_action.py:324-327` (claim); `systems/factions/sim/parliamentary_transfer.py:116-176` (the uncounted emitter); `engine/cross_scale/echo_transport.py:438` (the actual live emitter) |
