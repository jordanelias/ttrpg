# Valoria — Execution Map (boot → termination)

> **GENERATED** by `tools/build_execution_map.py`. Do not hand-edit.

**8 of 35 units execute today** (27 modules + 8 adapters). 56 Key types registered.

Every node below is annotated `RUNS` or `does not run`. Nodes that do not run are kept: for the fork they are the work-list, not noise.


## 1. Execution spine

- **`boot`** Boot — construct the world
  <sub>`engine/mc_v18.py` → `world = game_state.create_world(seed=seed)`</sub>
  <sub>Deterministic from `seed`. Builds factions, territories, clocks. Godot: this is the save/load entry point — strategy Stage 1 specifies save = initial conditions + Key log.</sub>
  - **`boot.victory_reset`** Reset victory state  — modules: `victory`
    <sub>`engine/mc_v18.py` → `victory.reset()`</sub>
  - **`boot.slate_clear`** Clear the scene slate
    <sub>`engine/mc_v18.py` → `scene_slate.clear()`</sub>
    <sub>Module-level queue; NOT per-world state.</sub>
  - **`boot.flags`** Resolve per-campaign flags
    <sub>`engine/mc_v18.py` → `world.dispatch_combat_bridge = _dispatch_combat_bridge_on(effective_params)`</sub>
    <sub>DISPATCH_COMBAT_BRIDGE decided ONCE and stashed on `world` (single owner).</sub>
  - **`boot.substrate`** Attach the Key substrate
    <sub>`engine/mc_v18.py` → `world.echo_scheduler = echo_transport.make_scheduler(`</sub>
    <sub>THE ORCHESTRATOR. TickScheduler + KeyLog. Its PRESENCE is the ECHO_TRANSPORT flag — absence means the byte-exact legacy path. `world.key_log` is the log.</sub>
  - **`boot.subscribe`** Subscribe articulation to the scheduler  — modules: `articulation` *(does not run)*
    <sub>`engine/mc_v18.py` → `_articulation.subscribe_all(world.echo_scheduler)`</sub>
    <sub>The only production TickScheduler subscriber wiring.</sub>
- **`loop`** Season loop — `for _ in range(max_s)`
  <sub>`engine/mc_v18.py` → `for _ in range(max_s):`</sub>
  <sub>Breaks on `world.winner`.</sub>
  - **`loop.s1`** Step 1 — advance_season  — modules: `engine_clock` *(does not run)*
    <sub>`systems/overview/sim/season.py` → `sr = advance_season(world)`</sub>
    <sub>Season counter, arc boundary, per-arc + per-season faction flag resets. The temporal spine `engine_clock` is `doc: null` — ED-1051, the sole remaining T0 blocker.</sub>
  - **`loop.s2`** Step 2 — action_callback
    <sub>`systems/overview/sim/season.py` → `action_callback(world)`</sub>
    <sub>The injection point. mc_v18 passes `_faction_actions_callback`; **Godot passes its own to drive UI scene flow** (season.py's own docstring). This is the seam the port hangs on.</sub>
    - **`loop.s2.factions`** Faction actions, per parliamentary faction holding territory  — modules: `faction_state` *(does not run)*, `faction_politics` *(does not run)*
      <sub>`engine/mc_v18.py` → `faction_take_action(faction, world, world.rng)`</sub>
      <sub>GD-2 mandatory-actions precedence enforced inside. Errors print to stderr, never abort.</sub>
    - **`loop.s2.scenes`** Scene phase — the personal-scale seam  — modules: `social_contest`, `personal_combat` *(does not run)*, `fieldwork_knots` *(does not run)*, `threadwork` *(does not run)*
      <sub>`engine/cross_scale/scene_dispatch.py` → `def run_scene_phase`</sub>
      <sub>MEASURED 2026-08-03: a whole campaign dispatches 29 slots and ALL 29 are `contest`. `queue_triggered_scenes` is the only production caller of `queue_scene`, and `evaluate_triggers` can only emit scene_type=contest. No trigger produces combat.</sub>
    - **`loop.s2.parliament`** Parliamentary vote (flag-gated on the scheduler)  — modules: `social_contest`
      <sub>`engine/mc_v18.py` → `parliamentary_bridge.run_parliamentary_scene(world, world.rng)`</sub>
      <sub>Resolves on aggregate state; composes a winner Domain Echo.</sub>
    - **`loop.s2.boundary`** ACTION->ACCOUNTING boundary — deferred applies land
      <sub>`engine/mc_v18.py` → `_sched.accounting_boundary()`</sub>
      <sub>OF-7. Keys emitted during the scene phase were logged LIVE; their `apply` closures execute HERE. Then `next_tick()` resets the per-tick emission counter. This is the orchestration contract: emission is immediate, effect is deferred to a named boundary.</sub>
  - **`loop.s3`** Step 3 — run_accounting  — modules: `territorial_piety` *(does not run)*, `settlement_layer` *(does not run)*, `npc_behavior` *(does not run)*
    <sub>`systems/overview/sim/season.py` → `run_accounting(world)`</sub>
    <sub>CI seasonal calc (PP-412 5-step) + MS baseline decay (PP-255, year-end cadence). Also calls `simulate_npc_actions` every season.</sub>
  - **`loop.victory`** Victory check (GD-1)  — modules: `victory`
    <sub>`engine/mc_v18.py` → `results = victory.check_all_factions(world)`</sub>
    <sub>Sets `world.winner`, which breaks the loop on the NEXT iteration.</sub>
- **`term`** Termination
  <sub>`engine/mc_v18.py` → `if not world.winner:`</sub>
  - **`term.fallback`** Fallback winner by territory count  — modules: `victory`
    <sub>`engine/mc_v18.py` → `scores[fn] = held * 10 + f.L + len(f.territories)`</sub>
    <sub>Runs when the loop exhausts `max_s` with no victor.</sub>
  - **`term.result`** Emit CampaignResult
    <sub>`engine/mc_v18.py` → `return CampaignResult(`</sub>
    <sub>Carries `key_log_hash` + `keys_emitted` — the parity surface the Godot port compares against (strategy Stage 2: Key-log equality is the master parity check).</sub>

## 2. Modules — contract, keys, state, port

| module | scale | resolver | build | runs | godot | rank | keys in | keys out |
|---|---|---|---|---|---|---|---|---|
| `personal_combat` | personal | d_sigma | unwired | — | gd-ported | 0 | 2 | 3 |
| `mass_battle` | scene | dice_pool | live | ✅ | python-oracle | 1 | 0 | 1 |
| `social_contest` | scene | dice_pool | gated | ✅ | python-oracle | 1 | 1 | 4 |
| `victory` | provincial | state_reader | live | ✅ | python-oracle | 1 | 0 | 0 |
| `clock_registry` | provincial | manifest | design | — | python-oracle | 2 | 0 | 0 |
| `combat_bridge` |  |  | gated | ✅ | python-oracle | 2 | 0 | 0 |
| `domain_echo` |  |  | gated | ✅ | python-oracle | 2 | 0 | 0 |
| `echo_transport` |  |  | gated | ✅ | python-oracle | 2 | 0 | 0 |
| `faction_state` | provincial | deterministic_accounting | deferred | — | python-oracle | 2 | 25 | 3 |
| `parliamentary_bridge` |  |  | gated | ✅ | python-oracle | 2 | 0 | 0 |
| `scene_dispatch` |  |  | deferred | — | python-oracle | 2 | 0 | 0 |
| `territorial_piety` | territory | deterministic_accounting | deferred | — | python-oracle | 2 | 0 | 0 |
| `threadwork` | personal | dice_pool | unwired | — | python-oracle | 2 | 0 | 2 |
| `zoom_in_out` |  |  | gated | ✅ | python-oracle | 2 | 0 | 0 |
| `faction_politics` | provincial | deterministic_accounting | deferred | — | python-oracle | 3 | 0 | 4 |
| `handoff_rules` |  |  | unwired | — | python-oracle | 3 | 0 | 0 |
| `piety_track` | personal | deterministic_accounting | deferred | — | python-oracle | 3 | 9 | 1 |
| `settlement_layer` | territory | deterministic_accounting | design | — | python-oracle | 3 | 2 | 1 |
| `articulation` |  |  | stub | — | no-oracle | 8 | 0 | 0 |
| `articulation_layer` | personal | armature_dot_product | stub | — | no-oracle | 8 | 1 | 0 |
| `audit` | scene | state_reader | deferred | — | no-oracle | 8 | 3 | 0 |
| `ci_political` | provincial | deterministic_accounting | deferred | — | no-oracle | 8 | 0 | 0 |
| `domain_actions` | provincial | d_sigma | design | — | no-oracle | 8 | 0 | 6 |
| `engine_clock` | provincial | clock_advance | design | — | no-oracle | 8 | 0 | 2 |
| `fieldwork_knots` | personal | dice_pool | stub | — | no-oracle | 8 | 1 | 4 |
| `game_director` | scene | manifest | deferred | — | no-oracle | 8 | 0 | 3 |
| `miraculous_event` | personal | state_reader | stub | — | no-oracle | 8 | 0 | 1 |
| `npc_behavior` | personal | deterministic_accounting | design | — | no-oracle | 8 | 31 | 11 |
| `npc_memory` | personal | state_reader | design | — | no-oracle | 8 | 4 | 0 |
| `peninsular_strain` | peninsula | deterministic_accounting | deferred | — | no-oracle | 8 | 0 | 4 |
| `scenario_authoring` | peninsula | manifest | design | — | no-oracle | 8 | 0 | 2 |
| `scene_slate` | scene | manifest | deferred | — | no-oracle | 8 | 0 | 8 |
| `scene_timer` | scene | state_reader | deferred | — | no-oracle | 8 | 3 | 0 |
| `campaign_architecture` | provincial | none | design | — | retire | 9 | 0 | 0 |
| `settlement_economy` | settlement | deterministic_accounting | design | — | retire | 9 | 2 | 0 |

## 3. Keys — producers, consumers, and the dead ends

**47 of 56 key types have both a producer and a consumer.** A type with no producer cannot fire; one with no consumer means nothing reacts. Both are kept below and marked — for the fork they are the work-list.

| key type | producers | consumers | required payload | gap |
|---|---|---|---|---|
| `*` | — | articulation_layer, fieldwork_knots | — | **no producer** |
| `da.antinomian_action` | domain_actions | articulation_layer, faction_state, npc_behavior, piety_track | faction_id, description | ok |
| `da.covert_betrayal` | domain_actions | articulation_layer, faction_state, npc_behavior, piety_track | faction_id, target_actor, target_faction, exposed | ok |
| `da.diplomatic_alliance` | domain_actions | articulation_layer, faction_state | faction_id, counterparty_faction, terms | ok |
| `da.economic_intervention` | domain_actions | articulation_layer, faction_state, settlement_economy | faction_id, target_territories, intervention_type | ok |
| `da.public_governance` | domain_actions | articulation_layer, faction_state, npc_behavior | faction_id, mission_alignment, outcome | ok |
| `env.crisis` | peninsular_strain, scenario_authoring | — | crisis_type, affected_territories | **no consumer** |
| `env.disaster` | peninsular_strain, scenario_authoring | articulation_layer, faction_state, settlement_layer | disaster_type, affected_territories | ok |
| `env.peninsular_strain_shock` | peninsular_strain | articulation_layer, faction_state, npc_behavior, settlement_layer | strain_delta, causes, affected_territories | ok |
| `env.population_change` | peninsular_strain, settlement_layer | faction_state, settlement_economy | territory_id, delta, cause | ok |
| `mechanical.accounting` | engine_clock | articulation_layer, faction_state | season_index, factions_processed | ok |
| `mechanical.cascade_resolution` | faction_state | articulation_layer, faction_state, npc_behavior | faction_id, prior_aggregate, new_aggregate, cascade_fidelity_change, triggered_by | ok |
| `mechanical.era_transition` | victory | — | to_era, trigger_stat | **no consumer** |
| `mechanical.mission_shift` | faction_state | articulation_layer, faction_state, npc_behavior | faction_id, prior_mission, new_mission, trigger | ok |
| `mechanical.project_advanced` | npc_behavior | articulation_layer, npc_behavior | project_id, progress_before, progress_after, project_domain | ok |
| `mechanical.scene_entered` | game_director, scene_slate | articulation_layer, audit, scene_timer | scene_id, system_id, scope, sa_cost_estimated, slate_priority, season_n, parent_scene_id, stack_depth_after | ok |
| `mechanical.scene_exited` | game_director | articulation_layer, audit, scene_timer | scene_id, sa_cost_actual, outcome_class, ended_by, sufficient_scope | ok |
| `mechanical.scene_skipped` | game_director | audit, scene_timer | scene_id, system_id, scope, slate_priority, season_n, reason | ok |
| `mechanical.season_change` | engine_clock | — | season_index, new_season | **no consumer** |
| `mechanical.second_calamity` | victory | — | seasons_sustained_at_or_below_5 | **no consumer** |
| `mechanical.settlement_captured` | settlement_layer | — | settlement_id, territory_id, capturing_faction_id, prior_controlling_faction_id | **no consumer** |
| `mechanical.theocracy_unification_declared` | ci_political, territorial_piety | — | ci_value, mass_seizure_targets | **no consumer** |
| `meta.cascade_cluster_event` | articulation_layer | articulation_layer | cluster_pair, similarity, cluster_type, sustained_seasons | ok |
| `meta.knot_formed` | fieldwork_knots | articulation_layer, npc_behavior | participants, tier | ok |
| `meta.knot_ruptured` | fieldwork_knots | articulation_layer, npc_behavior, piety_track | knot_id, participants, cause | ok |
| `meta.legacy_event` | — | — | originating_system, legacy_payload | **no producer** · **no consumer** |
| `meta.miraculous_event` | miraculous_event | articulation_layer, faction_state, npc_behavior | event_type, center_actor, witnessed_by | ok |
| `meta.thread_woven` | threadwork | articulation_layer, npc_behavior, piety_track | thread_id, operating_npc, operation_type | ok |
| `scene.accord_echo` | echo_transport | articulation_layer | scene_outcome, target_settlement | ok |
| `scene.battle_concluded` | mass_battle | articulation_layer, faction_state, npc_behavior, piety_track | battle_id, victor, casualties_per_side, territorial_outcome | ok |
| `scene.combat_felled` | personal_combat | articulation_layer, faction_state, npc_behavior | actor_id | ok |
| `scene.combat_hit` | personal_combat | personal_combat | — | ok |
| `scene.combat_resolved` | personal_combat | articulation_layer, faction_state, npc_behavior | scene_id, outcome, participants | ok |
| `scene.combat_strike` | player_input, scene_slate | personal_combat | attacker, defender | ok |
| `scene.contest_resolved` | social_contest | articulation_layer, faction_state, npc_behavior | scene_id, outcome, participants | ok |
| `scene.dialogue` | npc_behavior, scene_slate, social_contest | articulation_layer, faction_state, npc_behavior, piety_track | exchange_count, initiator_id, topic | ok |
| `scene.displacement` | npc_behavior | articulation_layer, npc_behavior | observer_id, displaced_relation | ok |
| `scene.draft_da` | domain_actions | articulation_layer, npc_behavior | action_type, actor_id | ok |
| `scene.gift` | fieldwork_knots, scene_slate | articulation_layer, faction_state, npc_behavior | giver_id, receiver_id, gift_type | ok |
| `scene.gossip` | npc_behavior | articulation_layer, npc_memory | principals, cumulative_drift, origin_interaction_key | ok |
| `scene.insult` | scene_slate, social_contest | articulation_layer, faction_state, npc_behavior, piety_track | source_actor, target_id | ok |
| `scene.interaction` | npc_behavior | articulation_layer, npc_memory | interaction_type, drift_a_to_b, drift_b_to_a | ok |
| `scene.investigation_resolved` | faction_politics, scene_slate | articulation_layer, faction_state, npc_behavior | scene_id, subject_id, finding | ok |
| `scene.thread_operation` | threadwork | articulation_layer, npc_behavior | operation, operator_id | ok |
| `scene.threat` | scene_slate, social_contest | articulation_layer, faction_state, npc_behavior, piety_track | threatener, threatened, demand | ok |
| `scene.witness` | npc_behavior, scene_slate | articulation_layer, npc_behavior, piety_track | observed_key_id, witness_actor | ok |
| `state.belief_revised` | fieldwork_knots, npc_behavior | articulation_layer, npc_behavior | npc_id, prior_belief, new_belief | ok |
| `state.concern_resolved` | npc_behavior | articulation_layer, npc_memory | concern_tag, affect | ok |
| `state.coup_attempted` | faction_politics | articulation_layer, faction_state, npc_behavior | faction_id, challenger_id, incumbent_id, outcome | ok |
| `state.opinion_revised` | npc_behavior | articulation_layer, npc_memory, social_contest | opinion_subject, affect_axis_before, affect_axis_after, confidence_before, confidence_after | ok |
| `state.project_completed` | npc_behavior | articulation_layer, npc_behavior | project_id, project_domain, completion_effect, supporters, obstructors, goal_short | ok |
| `state.project_failed` | npc_behavior | articulation_layer, npc_behavior | project_id, failure_mode, seasons_stalled | ok |
| `state.scar_acquired` | piety_track | articulation_layer, faction_state, npc_behavior | npc_id, conviction, scar_count_before, scar_count_after, triggering_event_key | ok |
| `state.settlement_revolt` | settlement_layer | — | settlement_id, territory_id, governor_expelled | **no consumer** |
| `state.standing_change` | faction_politics, faction_state | articulation_layer, faction_state, npc_behavior | npc_id, standing_before, standing_after, trigger | ok |
| `state.succession` | faction_politics | articulation_layer, faction_state, npc_behavior | faction_id, prior_leader_id, new_leader_id, succession_mode | ok |

## 4. Centralization — owned state per module

The scalars each module's contract declares it OWNS. A scalar appearing under two owners is the centralization defect the fork exists to remove, so ownership travels with the node rather than living in a separate register.

**37 owned scalars across 35 units; 1 claimed by more than one owner.**

| scalar | claimed by |
|---|---|
| `CI (Church Influence)` | ci_political, territorial_piety |
