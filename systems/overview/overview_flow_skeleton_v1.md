# Overview — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/overview/` · **Lane:** `IN` · **Contracts:** `peninsular_strain`, `territorial_piety`, `game_director` (all
**Code roots traced:** `engine/mc_v18.py`, `systems/overview/sim/season.py`, `systems/overview/sim/accounting.py`, `systems/overview/sim/{ci_track,ms_track,ip_track,rs_track}.py`, `engine/autoload/{game_state,season_manager,victory,scene_slate}.py`, `engine/cross_scale/{scene_dispatch,parliamentary_bridge,echo_transport,articulation}.py`, `engine/substrate/{stubwire,keys}.py`
**Traced at:** `6545067`

## 1. Entry points

| Callable | Anchor | Called by |
|---|---|---|
| `run_campaign(seed, max_seasons, params) -> CampaignResult` | `engine/mc_v18.py:212 run_campaign` | `engine/mc_v18.py:317` (direct caller — `run_batch`'s loop; `run_batch` itself is reached only from `__main__` at `engine/mc_v18.py:334`); no in-tree production subsystem calls it — invoked externally by `tools/trace_execution_phases.py:147`, and indirectly by the generated verification script in `tools/build_fork.py:353`; and tests |
| `run_batch(n, base_seed, params) -> BatchResult` | `engine/mc_v18.py:311 run_batch` | `engine/mc_v18.py:334 __main__`; no external-tooling call site — `tools/dashboard_data.py` and `systems/mass_battle/sim/massbattle.py` mention `run_batch` only in comments, not calls; live callers are tests and its own `__main__` block |
| `_faction_actions_callback(world)` | `engine/mc_v18.py:116 _faction_actions_callback` | `engine/mc_v18.py:267` (passed as `action_callback=` to `run_season`) |
| `run_season(world, action_callback=None) -> SeasonResult` | `systems/overview/sim/season.py:48 run_season` | `engine/mc_v18.py:267` |
| `run_accounting(world)` | `systems/overview/sim/accounting.py:95 run_accounting` | `systems/overview/sim/season.py:72` |
| `compute_seasonal_ci_delta(world, ...) -> dict` | `systems/overview/sim/ci_track.py:100 compute_seasonal_ci_delta` | `systems/overview/sim/ci_track.py:186` (via `apply_seasonal_ci`) |
| `apply_ci_delta(delta, source, world) -> float` | `systems/overview/sim/ci_track.py:170 apply_ci_delta` | `systems/overview/sim/ci_track.py:187` (via `apply_seasonal_ci`); `systems/factions/sim/excommunication.py:166-167` |
| `apply_seasonal_ci(world, **kwargs) -> dict` | `systems/overview/sim/ci_track.py:181 apply_seasonal_ci` | `systems/overview/sim/accounting.py:112` |
| `apply_ms_baseline_decay(world) -> int` | `systems/overview/sim/ms_track.py:59 apply_ms_baseline_decay` | `systems/overview/sim/accounting.py:117` |
| `apply_ms_delta(delta, source, world) -> int` | `systems/overview/sim/ms_track.py:73 apply_ms_delta` | `systems/threadwork/sim/opposing.py:239`; `systems/threadwork/sim/co_movement.py:143` — no call from `accounting.py`/`season.py` |
| `apply_ip_delta(delta, source, world)` | `systems/overview/sim/ip_track.py:29 apply_ip_delta` | — (uncalled outside tests; see §7) |
| `check_phased_occupation_threshold(world)` | `systems/overview/sim/ip_track.py:37 check_phased_occupation_threshold` | — (uncalled anywhere, incl. tests; see §7) |
| `apply_rs_delta(delta, source, world)` | `systems/overview/sim/rs_track.py:28 apply_rs_delta` | `engine/cross_scale/echo_transport.py:355` |
| `advance_season(world) -> SeasonResult` | `engine/autoload/season_manager.py:31 advance_season` | `systems/overview/sim/season.py:69` |
| `check_arc_boundary(season) -> bool` | `engine/autoload/season_manager.py:46 check_arc_boundary` | — declared entry point, zero callers (see §7); only a prose mention at `systems/factions/sim/treaty.py:127` |
| `create_world(seed=None) -> World` | `engine/autoload/game_state.py:234 create_world` | `engine/mc_v18.py:224 run_campaign` |
| `check_all_factions(world) -> list[VictoryResult]` | `engine/autoload/victory.py:103 check_all_factions` | `engine/mc_v18.py:270 run_campaign` |
| `reset()` (victory streak) | `engine/autoload/victory.py:47 reset` | `engine/mc_v18.py:225 run_campaign` |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `seed` | arg (optional — falls back to wall-clock time if omitted; see §3 S1.1) | caller | `engine/mc_v18.py:212 run_campaign` |
| `max_seasons` | arg (shadowed — never read; see §7) | caller | `engine/mc_v18.py:212 run_campaign` |
| `params` | arg (dict, optional overrides) | caller | `engine/mc_v18.py:213 run_campaign` |
| `DEFAULT_PARAMS` (`CAMPAIGN_SEASONS`, `VICTORY_THRESHOLD`) | param | module constant | `engine/mc_v18.py:42-54 DEFAULT_PARAMS` |
| `ECHO_TRANSPORT` | flag (params override, else env var, default `'1'`) | caller / environment | `engine/mc_v18.py:57-67 _echo_transport_on` |
| `DISPATCH_COMBAT_BRIDGE` | flag (params override, else env var, default `'0'`) | caller / environment | `engine/mc_v18.py:70-81 _dispatch_combat_bridge_on` |
| `action_callback` | arg (Callable) | caller (`mc_v18` supplies `_faction_actions_callback`) | `systems/overview/sim/season.py:48 run_season` |
| `STARTING_STATS`, `STARTING_OWNER`, `ACCORD_MAP`, `PT_MAP` | param | module constant | `engine/autoload/game_state.py:46-61` |
| `world.clocks` seed values (`CI`, `MS`, `IP`, `PI`, `Strain`, `Turmoil`) | world-state | `create_world` | `engine/autoload/game_state.py:266 create_world` |
| `SEASONS_PER_ARC` | param | module constant | `engine/autoload/season_manager.py:23` |
| `SEASONS_PER_YEAR` | param | module constant | `systems/overview/sim/ms_track.py:48` |
| `assert_attempted`/`assert_success`/`suppress_attempted`/`suppress_success` | arg (caller-driven CI Assert/Suppress outcome) | caller — not supplied by `accounting.run_accounting` | `systems/overview/sim/ci_track.py:100-104 compute_seasonal_ci_delta` |
| `world.factions[*].parliamentary`/`.territories` | world-state | `engine/autoload/game_state.py` | `engine/mc_v18.py:124-128 _faction_actions_callback` |
| `world.rng` | world-state | `create_world` | `engine/autoload/game_state.py:195 World` |
| `world.echo_scheduler` presence | registry | set by `run_campaign` | `engine/mc_v18.py:241-250` |
| `game_state.ALL_PLAYABLE_15` | param | module constant | `engine/mc_v18.py:282` |
| `world.factions[*].L` | world-state | `engine/autoload/game_state.py` | `engine/mc_v18.py:284` |
| `world.territories[*].owner` | world-state | `engine/autoload/game_state.py` | `engine/mc_v18.py:283` |

## 3. Flow

- **S1** `[gate]` Campaign init — `engine/mc_v18.py:212 run_campaign`
  - **S1.1** `[branch]` if `seed is None`: draw the seed from wall-clock time instead — the campaign's determinism seam `engine/mc_v18.py:215-216`
  - **S1.2** `world = game_state.create_world(seed)` `engine/mc_v18.py:224 create_world`
  - **S1.3** `[write]` `victory.reset()` `engine/mc_v18.py:225 reset`
  - **S1.4** `[write]` `scene_slate.clear()` `engine/mc_v18.py:226 clear`
  - **S1.5** `effective_params = DEFAULT_PARAMS` merged with `params` `engine/mc_v18.py:228-231`
  - **S1.6** `[branch]` `world.dispatch_combat_bridge = _dispatch_combat_bridge_on(...)` (default OFF) `engine/mc_v18.py:237`
  - **S1.7** `[branch][write]` if `ECHO_TRANSPORT` on (default ON): attach `world.echo_scheduler` / `world.key_log` / `world._echo_key_seq`, then `articulation.subscribe_all(world.echo_scheduler)` `engine/mc_v18.py:241-258`
- **S2** `[loop]` Season loop, up to `max_s` iterations — `engine/mc_v18.py:260` (for _ in range(max_s))
  - **S2.1** `[gate]` `if world.winner: break` `engine/mc_v18.py:261-262`
  - **S2.2** `run_season(world, action_callback=_faction_actions_callback)` (return value discarded — see §7) `engine/mc_v18.py:267`
    - **S2.2.1** `[write]` `advance_season(world)` — season/arc counters, per-arc/per-season faction flag resets `systems/overview/sim/season.py:69` → `engine/autoload/season_manager.py:33-45`
    - **S2.2.2** `action_callback(world)` i.e. `_faction_actions_callback` `systems/overview/sim/season.py:71` → `engine/mc_v18.py:116`
      - **S2.2.2.1** `[loop][branch]` for each faction: skip if not `parliamentary`, skip if no `territories`, else `faction_take_action(faction, world, rng)` (exceptions caught, logged, not re-raised) `engine/mc_v18.py:124-136`
      - **S2.2.2.2** `[emit]` `scene_dispatch.run_scene_phase(world, world.rng)`; `world.scenes_resolved` incremented by resolved count `engine/mc_v18.py:141-142`
      - **S2.2.2.3** `[branch][gate: world.echo_scheduler is not None]` `parliamentary_bridge.run_parliamentary_scene(world, world.rng)`; on `resolved` increments `world.scenes_resolved` `engine/mc_v18.py:148-152`
      - **S2.2.2.4** `[branch][gate: world.echo_scheduler is not None][write]` `_sched.accounting_boundary()` then `_sched.next_tick()` `engine/mc_v18.py:158-161`
      - **S2.2.2.5** `[gap]` `stubwire.stub_resolve(...)` for `generate_npc(world-gen|season-tick)` `engine/mc_v18.py:186-194`
      - **S2.2.2.6** `[gap]` `stubwire.stub_resolve(...)` for `form_knot(world-gen|season-tick)` `engine/mc_v18.py:204-209`
    - **S2.2.3** `run_accounting(world)` `systems/overview/sim/season.py:72` → `systems/overview/sim/accounting.py:95`
      - **S2.2.3.1** `[write]` `apply_seasonal_ci(world)` — every season `systems/overview/sim/accounting.py:112`
      - **S2.2.3.2** `[gate: world.season > 0 and world.season % SEASONS_PER_YEAR == 0][write]` `apply_ms_baseline_decay(world)` `systems/overview/sim/accounting.py:116-117`
      - **S2.2.3.3** `[write]` `check_insurgency_triggers(world)` — every season `systems/overview/sim/accounting.py:124`
      - **S2.2.3.4** `[loop][write]` `check_insurgency_promotion(ins_id, world)` for each existing insurgency `systems/overview/sim/accounting.py:131-132`
      - **S2.2.3.5** `[write]` `simulate_npc_actions(world)` `systems/overview/sim/accounting.py:138`
      - **S2.2.3.6** `[write]` `_probe_province_accord_drift(world)` — report-only telemetry, runs last `systems/overview/sim/accounting.py:142` (def at `:53-92`)
  - **S2.3** `[gate]` Victory check — `check_all_factions(world)` `engine/mc_v18.py:270`
    - **S2.3.1** `[loop][gate][write]` for each `VictoryResult` in the returned list: first with `won=True` sets `world.winner` and `break`s this inner results loop only — the season loop itself only exits at the *next* iteration's S2.1 gate, not here `engine/mc_v18.py:271-274`
- **S3** `[gate]` Fallback winner — `if not world.winner:` compute territory-count score per parliamentary faction and take the max `engine/mc_v18.py:277-286`
- **S4** `[emit]` Build and return `CampaignResult` (winner, season, surviving, battle_count, scenes_resolved, insurgencies_formed, npcs_generated, stub_hits, accord_drift_probe_hits, key_log_hash, keys_emitted, final_state) `engine/mc_v18.py:288-308`

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `CampaignResult` | dataclass (return) | caller (external tools/tests; no in-tree production consumer) | `engine/mc_v18.py:84-105` (def), `:292-308` (return site) |
| `BatchResult` | dataclass (return) | caller | `engine/mc_v18.py:108-113` (def), `:322-329` (return site) |
| `SeasonResult` | dataclass (return) | declared consumer is the caller of `run_season`; the sole production caller (`run_campaign`) discards it — see §7 | `systems/overview/sim/season.py:39-45` (def), `:73-78` (return); discarded at `engine/mc_v18.py:267` |
| `world.winner` | world-state (write) | `engine/mc_v18.py` fallback/return, `victory.check_all_factions` gate | `engine/mc_v18.py:273`, `:277` |
| `world.clocks['CI']` | world-state (write) | live season-loop readers: `systems/factions/sim/council_solmund.py` (Council Ob gate, reached via `faction_action.py`) and `systems/factions/sim/tribunal.py` (formal-tribunal prereq gate, reached via `excommunication.py` → `faction_action.py`); plus readers declared but currently unreached from any production call site (per `factions_flow_skeleton_v1.md`/`social_contest_flow_skeleton_v1.md`): `systems/factions/sim/mass_seizure.py` (×2) and `systems/social_contest/sim/parliamentary_stay.py` | `systems/overview/sim/ci_track.py:177` (write); `systems/factions/sim/council_solmund.py:32`; `systems/factions/sim/faction_action.py:323`; `systems/factions/sim/tribunal.py:83`; `systems/factions/sim/excommunication.py:119`; `systems/factions/sim/mass_seizure.py:173`; `systems/factions/sim/mass_seizure.py:241`; `systems/social_contest/sim/parliamentary_stay.py:59` |
| `world.clocks['MS']` | world-state (write) | readers exist in-tree but are declared-unreached from any production call site (per `threadwork_flow_skeleton_v1.md`, "none found"): `systems/threadwork/sim/co_movement.py`, `systems/threadwork/sim/opposing.py` | `systems/overview/sim/ms_track.py:69`, `systems/overview/sim/ms_track.py:89` (write); `systems/threadwork/sim/co_movement.py:139`; `systems/threadwork/sim/opposing.py:235` |
| `world.insurgencies`, `world.uncontrolled_streaks` | world-state (write) | `systems/world/sim/insurgency_pipeline.py` own readers; serialized via `game_state.serialize_world` | `systems/world/sim/insurgency_pipeline.py:57-96` |
| `world.npcs`, `world.npc_counter` | world-state (write) | `systems/world/sim/npe.py` own readers; `CampaignResult.npcs_generated` | `systems/world/sim/npe.py:99-115`; `engine/mc_v18.py:299` |
| `world.accord_drift_probe_hits` | world-state (write, additive telemetry) | `CampaignResult.accord_drift_probe_hits` | `systems/overview/sim/accounting.py:83-92`; `engine/mc_v18.py:304` |
| `world.key_log` / `world.echo_scheduler` | world-state (write) | `CampaignResult.key_log_hash`/`keys_emitted`; `engine/cross_scale/*` readers | `engine/mc_v18.py:243-249`; `:305-306` |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| `world.season`, `world.arc` | RW | `engine/autoload/season_manager.py` | `engine/autoload/season_manager.py:35-38` |
| `world.winner` | RW | `engine/mc_v18.py` (write), `engine/autoload/victory.py` (feeds decision) | `engine/mc_v18.py:261`, `engine/mc_v18.py:273`, `engine/mc_v18.py:277-286` |
| `world.clocks['CI']` | RW | `systems/overview/sim/ci_track.py` | `systems/overview/sim/ci_track.py:170-178` |
| `world.clocks['MS']` | RW | `systems/overview/sim/ms_track.py` | `systems/overview/sim/ms_track.py:59-91` |
| `world.clocks['IP']` | W (seed only) | `engine/autoload/game_state.py`; declared writer `ip_track.apply_ip_delta` is uncalled | `engine/autoload/game_state.py:246`; `systems/overview/sim/ip_track.py:29-34` |
| `world.clocks['PI']`, `world.clocks['Strain']` | W (seed only) | `engine/autoload/game_state.py`; no reader or writer anywhere else in the tree | `engine/autoload/game_state.py:246` |
| `world.clocks['Turmoil']` | W (seed only) / R | `engine/autoload/game_state.py` (seed); `engine/autoload/victory.py` (read as the PS victory gate); no writer anywhere — see §7 | `engine/autoload/game_state.py:246`; `engine/autoload/victory.py:73` |
| `world.insurgencies`, `world.uncontrolled_streaks` | RW | `systems/world/sim/insurgency_pipeline.py` | `systems/overview/sim/accounting.py:124`, `systems/overview/sim/accounting.py:131-132` |
| `world.npcs`, `world.npc_counter` | RW | `systems/world/sim/npe.py` | `systems/overview/sim/accounting.py:138` |
| `world.settlements` | R (drift probe) | `systems/settlements/sim/registry.py` (write-owner); written at world-gen | `systems/overview/sim/accounting.py:79-89`; `engine/autoload/game_state.py:259-260` |
| `world.territories[*].accord` | R (drift probe) | `engine/autoload/game_state.py` (write-owner is SE/FA-lane. The dominant in-loop path is `Territory.adjust_accord(...)`, NOT a bare `.accord =` assignment — a grep for the literal misses it: `systems/factions/sim/faction_action.py:502`, `systems/factions/sim/faction_action.py:513` (both `_try_conquest`), `systems/factions/sim/faction_action.py:566` (`_try_govern`), `systems/factions/sim/crown_initiative.py:102`, `systems/factions/sim/crown_initiative.py:110` (both `attempt_royal_progress`). The two direct `.accord =` sites are `systems/factions/sim/parliamentary_transfer.py:278` and `systems/factions/sim/mass_seizure.py:293` — accounting.py's own comment cites a stale line number for the former, see §7) | `systems/overview/sim/accounting.py:87-88` |
| `world.battle_count` | R | write-owner `systems/factions/sim/faction_action.py:515` | `engine/mc_v18.py:296` |
| `world.echo_scheduler`, `world.key_log`, `world._echo_key_seq` | W (init) | `engine/mc_v18.py`; read by `engine/cross_scale/*` | `engine/mc_v18.py:243-250` |
| `world.dispatch_combat_bridge` | W | `engine/mc_v18.py`; read by `engine/cross_scale/scene_dispatch.py` | `engine/mc_v18.py:237` |
| `world.scenes_resolved` | RW | `engine/mc_v18.py`, `engine/cross_scale/parliamentary_bridge.py` | `engine/mc_v18.py:142`, `engine/mc_v18.py:152`, `engine/mc_v18.py:297` |
| `world.accord_drift_probe_hits` | RW | `systems/overview/sim/accounting.py` (write), `engine/mc_v18.py` (read) | `systems/overview/sim/accounting.py:83-92`; `engine/mc_v18.py:304` |
| `Faction.senator_inward_used`, `.consul_used` | W | `engine/autoload/game_state.py:132 reset_seasonal` (called every season via `advance_season`) | `engine/autoload/game_state.py:133-135` |
| `Faction.council_used_this_arc`, `.parl_transfer_used_this_arc` | W | `engine/autoload/game_state.py:136 reset_arc` (called on arc boundary via `advance_season`) | `engine/autoload/game_state.py:137-140` |
| `scene_slate._queue` (module-level global, not `world`-scoped) | RW | `engine/autoload/scene_slate.py` | `engine/autoload/scene_slate.py:31`, `engine/autoload/scene_slate.py:34-59` |
| `stubwire.invocations` (module-level global counter) | RW | `engine/substrate/stubwire.py`; snapshotted per-campaign by `run_campaign` | `engine/mc_v18.py:222`, `engine/mc_v18.py:300` |
| `victory._qualifying_streak` (module-level global, not `world`-scoped) | RW | `engine/autoload/victory.py` — reset per campaign by `victory.reset()`, not by `create_world` | `engine/autoload/victory.py:44-49`, `engine/autoload/victory.py:79-84` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| up | `engine.autoload.game_state` | `create_world`, `serialize_world` | `engine/mc_v18.py:224`, `engine/mc_v18.py:307` |
| up | `engine.autoload.victory` | `reset`, `check_all_factions` | `engine/mc_v18.py:225`, `engine/mc_v18.py:270` |
| up | `engine.autoload.scene_slate` | `clear` | `engine/mc_v18.py:226` |
| up | `engine.autoload.season_manager` | `advance_season` | `systems/overview/sim/season.py:69` |
| up | `engine.substrate.stubwire` | `stub_resolve`, module counter `invocations` | `engine/mc_v18.py:186`, `engine/mc_v18.py:204`, `engine/mc_v18.py:222`; `systems/overview/sim/ip_track.py:30`, `systems/overview/sim/ip_track.py:38`; `systems/overview/sim/rs_track.py:29` |
| up | `engine.cross_scale.scene_dispatch` | `run_scene_phase` (personal-scale scene phase, part of the per-season action callback) | `engine/mc_v18.py:141` |
| up | `engine.cross_scale.parliamentary_bridge` | `run_parliamentary_scene` | `engine/mc_v18.py:150` |
| up | `engine.cross_scale.echo_transport` | `make_scheduler` (campaign init) | `engine/mc_v18.py:243-248` |
| up | `engine.cross_scale.articulation` | `subscribe_all` | `engine/mc_v18.py:258` |
| out | `systems.factions.sim.faction_action` | `faction_take_action(faction, world, rng)`, writes `world.battle_count` | `engine/mc_v18.py:130`; `systems/factions/sim/faction_action.py:197`, `systems/factions/sim/faction_action.py:515` |
| out | `systems.world.sim.insurgency_pipeline` | `check_insurgency_triggers`, `check_insurgency_promotion`, `get_insurgencies` | `systems/overview/sim/accounting.py:124`, `systems/overview/sim/accounting.py:131-132` |
| out | `systems.world.sim.npe` | `simulate_npc_actions` | `systems/overview/sim/accounting.py:138` |
| out | `systems.factions.sim.council_solmund` | reads `world.clocks['CI']` as the Council Ob gate; reached via `faction_action.py`'s dispatch, itself reached from the season loop | `systems/factions/sim/faction_action.py:323`; `systems/factions/sim/council_solmund.py:32` |
| out | `systems.factions.sim.tribunal` | reads `world.clocks['CI']` as the formal-tribunal prereq gate; reached via `excommunication.py` → `faction_action.py`'s dispatch, itself reached from the season loop | `systems/factions/sim/excommunication.py:119`; `systems/factions/sim/tribunal.py:83` |
| out (declared, unreached) | `systems.factions.sim.mass_seizure` | reads `world.clocks['CI']` as the declaration + resolution gates; zero production callers per `factions_flow_skeleton_v1.md` | `systems/factions/sim/mass_seizure.py:173`; `systems/factions/sim/mass_seizure.py:241` |
| out (declared, unreached) | `systems.social_contest.sim.parliamentary_stay` | reads `world.clocks['CI']` as the Stay availability gate; zero callers anywhere in the tree per `social_contest_flow_skeleton_v1.md` | `systems/social_contest/sim/parliamentary_stay.py:59` |
| out (declared, unreached) | `systems.threadwork.sim.co_movement` | reads `world.clocks['MS']` as its delta base; no production caller found per `threadwork_flow_skeleton_v1.md` | `systems/threadwork/sim/co_movement.py:139` |
| out (declared, unreached) | `systems.threadwork.sim.opposing` | reads `world.clocks['MS']` as its delta gate; no production caller found per `threadwork_flow_skeleton_v1.md` | `systems/threadwork/sim/opposing.py:235` |
| out | `systems.settlements.sim.registry` | `province_members`, `province_accord` (drift probe); `populate_from_geography` (world-gen) | `systems/overview/sim/accounting.py:85`, `systems/overview/sim/accounting.py:87`; `engine/autoload/game_state.py:259-260` |
| in | `systems.threadwork.sim.opposing` | calls `ms_track.apply_ms_delta` | `systems/threadwork/sim/opposing.py:236-239` |
| in | `systems.threadwork.sim.co_movement` | calls `ms_track.apply_ms_delta` | `systems/threadwork/sim/co_movement.py:140-143` |
| in | `systems.factions.sim.excommunication` | calls `ci_track.apply_ci_delta` | `systems/factions/sim/excommunication.py:164-167` |
| in | `engine.cross_scale.echo_transport` | calls `rs_track.apply_rs_delta`, gated on `world.echo_scheduler` + an explicit caller-declared `echo`/`scene_outcome` block | `engine/cross_scale/echo_transport.py:354-355` |

## 7. Traced gaps

| Gap | Evidence anchor |
|---|---|
| `DEFAULT_PARAMS['VICTORY_THRESHOLD'] = 11` is a documented DEAD param — the live victory gate is `engine/autoload/victory.py`'s own module-level `VICTORY_THRESHOLD = 15`; nothing in `season.py`/`accounting.py`/`victory.py` reads `effective_params['VICTORY_THRESHOLD']`. | `engine/mc_v18.py:42-54 DEFAULT_PARAMS`; `engine/autoload/victory.py:27 VICTORY_THRESHOLD` (the live constant, unconnected to the dict) |
| `run_campaign`'s `max_seasons` argument is a dead param of the same class — `effective_params` is seeded from `DEFAULT_PARAMS`, which always carries `CAMPAIGN_SEASONS`, so `effective_params.get('CAMPAIGN_SEASONS', max_seasons)`'s fallback to the `max_seasons` argument is unreachable; the only way to actually move the season count is `params={'CAMPAIGN_SEASONS': ...}`. | `engine/mc_v18.py:212 run_campaign` (signature); `engine/mc_v18.py:228-231` (shadowing site) |
| `CampaignResult.stub_hits`'s own field comment asserts "0 while no live call site is stub-wired yet" — stale: this skeleton's S2.2.2.5/S2.2.2.6 record two `stubwire.stub_resolve` call sites (`generate_npc`, `form_knot`) that run every season, so hits ARE live, not zero-by-construction. | `engine/mc_v18.py:93-96` (comment); `engine/mc_v18.py:186-194`, `engine/mc_v18.py:204-209` (the live stub-wired call sites) |
| `stubwire.stub_resolve` call for `generate_npc(world-gen|season-tick)` — no automatic NPC generation is wired anywhere in the season loop; the comment states no canonical trigger exists to cite (only `simulate_npc_actions`, the drift half, runs live). | `engine/mc_v18.py:186-194` |
| `stubwire.stub_resolve` call for `form_knot(world-gen|season-tick)` — no automatic Knot formation is wired anywhere in the season loop; the comment states the personal-scale prerequisite fields (Disposition, Bonds) do not exist on the aggregate `World`. | `engine/mc_v18.py:204-209` |
| `world.clocks['Turmoil']` is read as the Political-Stability victory gate (`ps = world.clocks.get('Turmoil', 0.0)`) but has **zero write sites** anywhere in the tree outside its `create_world` seed of `0.0` — the gate is therefore permanently satisfied (`ps_ok` always `True`) in every traced campaign. `references/module_contracts.yaml`'s own `peninsular_strain` module entry independently records the same finding ("Turmoil has NO tracker file anywhere ... verified: grep for a Turmoil writer finds none"). | `engine/autoload/game_state.py:246` (seed); `engine/autoload/victory.py:73` (read); `references/module_contracts.yaml:640-642` |
| `world.clocks['PI']` and `world.clocks['Strain']` are seeded at world creation and have no reader or writer anywhere else in the codebase (production or test). | `engine/autoload/game_state.py:246` |
| `systems/overview/sim/ip_track.py`'s two declared entry points (`apply_ip_delta`, `check_phased_occupation_threshold`) are both `stubwire.stub_resolve` typed no-ops (Pass 2l armature stub) with **zero production call sites**; `apply_ip_delta` is exercised only by a generic pipeline-reach test, `check_phased_occupation_threshold` by nothing at all. `systems/mass_battle/sim/altonian_reinforcements.py` names `ip_track` as a dependency in its module docstring but contains no actual call. | `systems/overview/sim/ip_track.py:29-42`; `engine/tests/test_pipeline_reach.py:756-757`; `systems/mass_battle/sim/altonian_reinforcements.py:9` (docstring-only reference) |
| `systems/overview/sim/rs_track.py`'s `apply_rs_delta` is itself a `stubwire.stub_resolve` typed no-op (RS has no live write path per its own module docstring), reachable only through `engine/cross_scale/echo_transport.py`'s violence-row Accord Echo leg, which requires `world.echo_scheduler` attached AND a caller-declared `ctx['echo']['scene_outcome']` — no live trigger in the campaign loop declares that field (per `echo_transport.py`'s own module docstring), so the call site is WIRED but DORMANT in any seeded campaign today. | `systems/overview/sim/rs_track.py:15-33`; `engine/cross_scale/echo_transport.py:348-355` |
| `engine/autoload/season_manager.py`'s declared entry point `check_arc_boundary(season)` has zero callers anywhere in the tree (production or test) — the only reference is a prose mention inside a comment in a peer module. | `engine/autoload/season_manager.py:48-50`; `systems/factions/sim/treaty.py:127` (comment, not a call) |
| `run_season`'s `SeasonResult` return value is discarded at its sole production call site (`run_campaign`); the composed step data (`season`, `arc`, `new_arc`, `accounting_run`) is computed every season and never consumed there. | `systems/overview/sim/season.py:73-78` (return); `engine/mc_v18.py:267` (call site, return unassigned) |
| `systems/overview/sim/__init__.py`'s module docstring describes `accounting` as a "13-step end-of-season cascade"; `accounting.run_accounting`'s own docstring and body enumerate exactly 6 steps (CI, MS year-end, insurgency triggers, insurgency promotion, NPC ecology, Accord-drift probe). | `systems/overview/sim/__init__.py:10`; `systems/overview/sim/accounting.py:98-108` |
| `accounting.py`'s module docstring carries a standing PRE-LPS-1/PORT-BLOCKING note: `run_accounting()` has no Mandate-aggregation or Treasury-accrual step — the ratified LPS-1 per-settlement L/PS → Mandate pipeline is unimplemented in the traced accounting flow. | `systems/overview/sim/accounting.py:11-13` |
| `DISPATCH_COMBAT_BRIDGE` defaults OFF (`os.environ.get('DISPATCH_COMBAT_BRIDGE', '0')`) — the S1.6 branch and its downstream `engine.cross_scale.scene_dispatch` combat-bridge leg take the unchanged legacy path in every default-configured campaign traced here. | `engine/mc_v18.py:70-81` |
| `accounting.py`'s module docstring cites parliamentary_transfer.py line 210 as the province-Accord write site feeding the drift probe's divergence; `systems/factions/sim/parliamentary_transfer.py:210` is that file's §1.3 last-territory-protection guard, not an Accord write — the actual write (`terr.accord = ACCORD_MAP[accord_level]`) is at `systems/factions/sim/parliamentary_transfer.py:278`. The mass_seizure.py half of the same citation resolves correctly. | `systems/overview/sim/accounting.py:31-32` (stale citation); `systems/factions/sim/parliamentary_transfer.py:210` (cited line, not a write) |
| `compute_seasonal_ci_delta`'s Step 3 (Assert) / Step 4 (Suppress) parameters (`assert_attempted`, `assert_success`, `suppress_attempted`, `suppress_success`) are never supplied by `accounting.run_accounting`'s call at `apply_seasonal_ci(world)` — those steps are always no-ops (`0`) in the traced season loop; the docstring states they are caller-driven faction actions resolved elsewhere, not invoked from this flow. | `systems/overview/sim/accounting.py:110-112`; `systems/overview/sim/ci_track.py:100-104`, `systems/overview/sim/ci_track.py:142-152` |
| `peninsular_strain`'s contract declares `env.crisis` among its emits, also emitted by `scenario_authoring`; no `consumes:` row anywhere in the file carries `env.crisis`, unlike its three sibling `env.*` types, which each have a `from:` consumer row — a dangling emit. Worse: none of `peninsular_strain`'s four declared emits (`env.crisis`, `env.disaster`, `env.peninsular_strain_shock`, `env.population_change`) is produced by any `.py` in `engine/`, `systems/`, or `tools/` — the only tree hits are a subscription-roster string, two code comments, and a dashboard label, not an emitter. | `references/module_contracts.yaml:649 env.crisis`; `references/module_contracts.yaml:952 env.crisis`; `engine/cross_scale/articulation.py:124` |
| `ms_track.py`'s module docstring still carries a `[DRIFT: accounting._ms_decay ...]` block claiming `accounting.py` inlines PP-255 baseline decay separately — stale. `accounting.py` has no `_ms_decay`; it imports `apply_ms_baseline_decay` and calls it, Year-End-cadence-gated. `references/module_contracts.yaml`'s `peninsular_strain` `state:` row already corrected this exact claim (2026-07-29) and recorded that `ms_track.py`'s own copy was left uncorrected, out of that file's scope. | `systems/overview/sim/ms_track.py:19-25`; `systems/overview/sim/accounting.py:43`; `systems/overview/sim/accounting.py:117` |
