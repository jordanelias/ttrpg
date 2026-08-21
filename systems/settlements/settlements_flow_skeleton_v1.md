# Settlements — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/settlements/` · **Lane:** `SE` · **Contracts:** `settlement_layer`, `settlement_economy`
**Code roots traced:** `systems/settlements/sim/registry.py`, `systems/settlements/sim/settlement.py`, `systems/settlements/sim/ledger.py`, `systems/settlements/sim/adjacency.py`, `systems/settlements/sim/infrastructure.py`, `systems/settlements/sim/temperaments.py`, `engine/autoload/game_state.py`, `engine/mc_v18.py`, `engine/cross_scale/echo_transport.py`, `systems/overview/sim/accounting.py`, `systems/factions/sim/mass_seizure.py`, `systems/factions/sim/parliamentary_transfer.py`, `systems/factions/sim/faction_action.py`, `systems/world/sim/insurgency_pipeline.py`, `systems/factions/sim/varfell_territorial_acquisition.py`, `tools/sim_harness/adapters/pr119_governance/*.py`
**Traced at:** `654506799c637e83eae33377a7b0974317721b0a`

## 1. Entry points

| Callable | Anchor | Called-by |
|---|---|---|
| `populate_from_geography(world, path=None)` | `systems/settlements/sim/registry.py:215 populate_from_geography` | `engine/autoload/game_state.py:279 populate_from_geography` (inside `create_world`) |
| `register_settlement(s, world=None)` | `systems/settlements/sim/registry.py:171 register_settlement` | `systems/settlements/sim/registry.py:264 register_settlement` (only production call, from inside `populate_from_geography` itself); `tools/sim_harness/adapters/pr119_governance/pr119_integrated_campaign.py:112 register_settlement` (prototype harness, not wired to CI) |
| `get_settlement(sid, world=None)` | `systems/settlements/sim/registry.py:176 get_settlement` | `systems/settlements/sim/settlement.py:107 get_settlement` |
| `province_members(province_id, world=None)` | `systems/settlements/sim/registry.py:180 province_members` | `systems/settlements/sim/settlement.py:175 province_members`; `systems/overview/sim/accounting.py:85 province_members` |
| `province_accord(province_id, world=None)` | `systems/settlements/sim/registry.py:184 province_accord` | `systems/overview/sim/accounting.py:87 province_accord` (the only production caller — read-only probe); `tools/sim_harness/adapters/pr119_governance/pr119_integrated_campaign.py:222 province_accord` (prototype harness) |
| `province_effective_prosperity(province_id, world=None)` | `systems/settlements/sim/registry.py:193 province_effective_prosperity` | `—` (no production caller; `tools/sim_harness/adapters/pr119_governance/pr119_integrated_campaign.py:262 province_effective_prosperity` only) |
| `succeed_governor(sid, new_governor, world=None, season=0)` | `systems/settlements/sim/registry.py:198 succeed_governor` | `—` (no production caller; `tools/sim_harness/adapters/pr119_governance/pr119_promote_ready_oversight.py:84 succeed_governor` only) |
| `compute_settlement_state(settlement_id, world)` | `systems/settlements/sim/settlement.py:95 compute_settlement_state` | `—` (no importer anywhere in `engine/`, `systems/`, `tests/` — see §7) |
| `aggregate_to_province(province_id, world)` | `systems/settlements/sim/settlement.py:160 aggregate_to_province` | `—` (no importer anywhere — see §7) |
| `build_infrastructure(territory_id, infra_type, world=None)` | `systems/settlements/sim/infrastructure.py:139 build_infrastructure` | `—` (no importer found in `engine/`, `systems/`, `tests/`; `tools/sim_harness/adapters/pr119_governance/pr119_integrated_campaign.py:198-199 build_infrastructure` and `tools/sim_harness/adapters/pr119_governance/pr119_subnational_factions.py:98 build_infrastructure` (prototype harness, not wired to CI)) |
| `count_infrastructure(territory_id, infra_type, world=None)` | `systems/settlements/sim/infrastructure.py:185 count_infrastructure` | `systems/factions/sim/mass_seizure.py:158 count_infrastructure` |
| `seizure_ob_modifier(territory_id, world=None)` | `systems/settlements/sim/infrastructure.py:236 seizure_ob_modifier` | `systems/factions/sim/mass_seizure.py:258 seizure_ob_modifier` |
| `ADJACENCY` (module constant, dict lookup) | `systems/settlements/sim/adjacency.py:9 ADJACENCY` | `systems/factions/sim/faction_action.py:42 ADJACENCY` (used at `:119`, `:168`); `systems/world/sim/insurgency_pipeline.py:116 ADJACENCY` (used at `:133`) |
| `temperament_of(territory_id)` | `systems/settlements/sim/temperaments.py:97 temperament_of` | `—` (no importer; declared a dependency only in a docstring — see §7) |
| `temperament_modifiers(territory_id, action_type)` | `systems/settlements/sim/temperaments.py:105 temperament_modifiers` | `—` (no importer) |
| `apply_strain_shock(strain_delta, affected_territories, world=None)` | `systems/settlements/sim/temperaments.py:142 apply_strain_shock` | `—` (no importer) |
| `get_faction_aggregate(faction_name)` | `systems/settlements/sim/temperaments.py:163 get_faction_aggregate` | `—` (no importer) |
| `ledger_add` / `ledger_has` / `ledger_get` / `ledger_sweep` | `systems/settlements/sim/ledger.py:47`, `systems/settlements/sim/ledger.py:61`, `systems/settlements/sim/ledger.py:65`, `systems/settlements/sim/ledger.py:69` | Only via `Settlement.add_tag`/`has_tag`/`tags` (`systems/settlements/sim/registry.py:99-107`) and `succeed_governor`'s `ledger_sweep` call (`systems/settlements/sim/registry.py:206`) — itself uncalled in production; live tag-writers are only `tools/sim_harness/adapters/pr119_governance/*.py` |
| `serialize_world(world)` settlements branch | `engine/autoload/game_state.py:349 settlements` | `engine/mc_v18.py:315 serialize_world` (end of `run_campaign`) |
| `restore_world(snapshot)` settlements branch | `engine/autoload/game_state.py:438-440 settlements` | no production caller found (save/restore round-trip exercised only by `engine/tests/test_world_population.py`) |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `systems/settlements/valoria_geography_v30.yaml` (`settlements:` map — `type`, `stats`, `territory`, `controller`) | `file` | Repo-committed geography source, loaded once at world-gen | `systems/settlements/sim/registry.py:246-249 populate_from_geography` |
| `LEGAL_TYPES` | `param` | Module-level constant, validated against on load | `systems/settlements/sim/registry.py:45-48 LEGAL_TYPES` |
| `world` (`GameState`/`World`) | `world-state` | Caller-supplied on every registry/ledger/infrastructure/adjacency entry point | `systems/settlements/sim/registry.py:165 settlement_store` |
| `settlement_id` / `province_id` / `territory_id` / `sid` | `arg` | Caller-supplied key | e.g. `systems/settlements/sim/registry.py:176 get_settlement` |
| `echo_ctx['target_settlement']`, `echo['scene_outcome']` | `arg` | Optional fields on a scene's `echo` context block, read at the accord-echo seam | `engine/cross_scale/echo_transport.py:301 echo_ctx`, `:167 declared` |
| `world.echo_scheduler` (presence) | `flag` | Set on `world` in `run_campaign` when `ECHO_TRANSPORT` is on | `engine/mc_v18.py:251 world.echo_scheduler` |
| `ACCORD_MAP` / `STARTING_ACCORD` / `STARTING_OWNER` | `param` | `engine/autoload/game_state.py` module constants, used to build `Territory` objects (a separate, uncoordinated source from the geography YAML — see §7) | `engine/autoload/game_state.py:246-254 Territory` |
| `world.territories[tid].templar` | `world-state` | `Territory` dataclass field, read as a seed for infrastructure Axis-2 backward compat | `systems/settlements/sim/infrastructure.py:130-131 templar_seed` |

## 3. Flow

**S1. World-gen registration** — `[write]`
`create_world()` builds `World.territories` from `STARTING_OWNER`/`STARTING_ACCORD`/`STARTING_PT` (`engine/autoload/game_state.py:223-234`), independently calls `populate_from_geography(world)` to build `World.settlements` from the geography YAML (`engine/autoload/game_state.py:279 populate_from_geography`), which for each sorted `sid` validates `type` against `LEGAL_TYPES` `[gate]` (`systems/settlements/sim/registry.py:254-257`), unpacks `stats` into `(prosperity, defense, order)` `[gate]` (`systems/settlements/sim/registry.py:258`), constructs a `Settlement` and registers it into `world.settlements` (`systems/settlements/sim/registry.py:259-264`).

**S2. Per-season faction/scene phase (no settlement write)**
`run_campaign`'s season loop calls `run_season` → `_faction_actions_callback` (`engine/mc_v18.py:264-267`, `engine/mc_v18.py:116`), which dispatches faction Domain Actions (`faction_take_action`, reads `ADJACENCY` for target/threat derivation — S2.1) and scene resolution (`scene_dispatch.run_scene_phase` — S2.2).

- **S2.1 Adjacency reads** `[branch]` — `faction_action._conquest_targets`/`_threat_signal` union `ADJACENCY.get(tid, set())` over a faction's held territories to find conquest targets / proximate military threats (`systems/factions/sim/faction_action.py:139`, `systems/factions/sim/faction_action.py:188`).
- **S2.2 Scene → Domain Echo → settlement write (deferred)** — when `world.echo_scheduler` is set, `echo_transport.emit_scene_echo` runs (`engine/cross_scale/echo_transport.py:360`):
  - S2.2.1 `[gate]` requires an explicit `echo` block with `actor_faction`/`most_relevant_stat`; else returns `{}` (`engine/cross_scale/echo_transport.py:379-387`).
  - S2.2.2 `[emit]` §5.2 Domain Echo fires a Faction-stat Key via `sched.emit` (`:409-438`) — does not touch settlements.
  - S2.2.3 `[branch][gate]` §5.5 Accord Echo: `classify_scene_outcome` trusts only an explicit caller-declared `echo['scene_outcome']` (`:448`, `:134-170`); no live producer sets this field (traced — see §7), so this branch does not fire in a seeded campaign.
  - S2.2.4 `[write][emit]` (reachable-but-dormant) `_apply_accord_echo` resolves `echo_ctx['target_settlement']` against `world.settlements` (`:291-293`); on a resolvable settlement it builds a `scene.accord_echo` Key with a `_apply` closure that writes `settlement.order` (clamped `STAT_MIN`/`STAT_MAX`) and queues it via `sched.emit(key, apply=_apply)` (`:309-343`) — the write does NOT land immediately.

**S3. Action→Accounting boundary** `[gate]`
Still inside `_faction_actions_callback`, after the scene phase: `world.echo_scheduler.accounting_boundary()` applies every queued Key's deferred `apply` (including any queued S2.2.4 settlement-Order write), then `next_tick()` resets the per-tick emission counter (`engine/mc_v18.py:158-161`).

**S4. Season-end accounting** — `systems/overview/sim/accounting.py:95 run_accounting`, called from `run_season` (traced via `engine/mc_v18.py:264-267` comment; body at `systems/overview/sim/accounting.py:95-142`):
  1. `[step]` CI seasonal calc (`:112`) — no settlement touch.
  2. `[step][gate]` MS year-end decay (`:116-117`) — no settlement touch.
  3. `[step]` `check_insurgency_triggers` (`:124`) — reads `ADJACENCY` via `_contiguous_uncontrolled_groups` to group contiguous Uncontrolled territories `[loop]` (`systems/world/sim/insurgency_pipeline.py:116`, `systems/world/sim/insurgency_pipeline.py:133`).
  4. `[step]` `check_insurgency_promotion` per insurgency (`:131-132`) — no settlement touch.
  5. `[step]` `simulate_npc_actions` (`:138`) — no settlement touch.
  6. `[step][gate][emit]` `_probe_province_accord_drift(world)` (`:142`, body `:53-92`) — see S5.

**S5. Province-Accord drift PROBE (report-only, never writes)** — `systems/overview/sim/accounting.py:53 _probe_province_accord_drift`
  - S5.1 `[gate]` returns immediately if `world.settlements` or `world.territories` is falsy (`:79-82`).
  - S5.2 `[loop]` for each `territory_id, territory` in `world.territories.items()` (`:84`):
    - S5.2.1 `[gate]` skip if `province_members(tid, world)` is empty (`:85-86`).
    - S5.2.2 `[read]` `live_settlement_accord = registry.province_accord(tid, world)` — `floor(mean(settlement.order))` over real members (`:87`, `systems/settlements/sim/registry.py:184-190`).
    - S5.2.3 `[read]` `live_territory_accord = canonical_accord(territory.accord)` — Territory's own continuous field bucketed to the same 0-4 index space (`:88`, `engine/substrate/canon_buckets.py:36-43`).
    - S5.2.4 `[branch]` if the two values differ, increment `hits` (`:89-90`) — this loop body never writes `settlement.order` or `territory.accord`.
  - S5.3 `[write]` if `hits` is nonzero, set `world.accord_drift_probe_hits = hits` (`:91-92`) — a per-campaign dynamic attribute, not a `World` dataclass field.

**S6. Territory.accord direct writes (bypass settlements entirely)** `[write]`
Two production sites write `Territory.accord` directly, never going through `Settlement.order` or `registry.province_accord`:
  - `systems/factions/sim/parliamentary_transfer.py:278` (terr.accord = ACCORD_MAP[accord_level]).
  - `systems/factions/sim/mass_seizure.py:293` (t.accord = float(starting_accord)) (itself gated by `count_infrastructure`/`seizure_ob_modifier` reads from `systems/settlements/sim/infrastructure.py` at `:158,258`).

**S7. Campaign close — serialization** `[write]`
`run_campaign` calls `game_state.serialize_world(world)` (`engine/mc_v18.py:307`), which dict-serializes `world.settlements` via each `Settlement.to_dict()` (`engine/autoload/game_state.py:329-330`, `systems/settlements/sim/registry.py:112-133`) and carries `accord_drift_probe_hits` into `CampaignResult` (`engine/mc_v18.py:304`).

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `world.settlements: dict[sid, Settlement]` | `registry` | `serialize_world`, `province_members`/`province_accord` readers, `echo_transport._apply_accord_echo` | `engine/autoload/game_state.py:231 settlements` |
| `province_accord(...)` return (`int`) | `arg` | `_probe_province_accord_drift` only, in production | `systems/settlements/sim/registry.py:190 province_accord` |
| `world.accord_drift_probe_hits` (`int`) | `world-state` | `CampaignResult.accord_drift_probe_hits` | `engine/mc_v18.py:312 accord_drift_probe_hits` |
| `world.territory_infrastructure[tid]: InfrastructureState` | `registry` | `count_infrastructure`/`seizure_ob_modifier` readers (`mass_seizure.py`), `serialize_world`/`restore_world` | `engine/autoload/game_state.py:421-423 InfrastructureState` |
| `ADJACENCY[tid]: set[str]` | `key` | `faction_action._conquest_targets`/`_threat_signal`, `insurgency_pipeline._contiguous_uncontrolled_groups` | `systems/settlements/sim/adjacency.py:9 ADJACENCY` |
| Queued `scene.accord_echo` Key (`settlement.order` delta) | `key` | `TickScheduler` log, applied at `accounting_boundary()` — dormant in a seeded campaign (see §7) | `engine/cross_scale/echo_transport.py:319-333 key` |
| `CampaignResult.final_state['settlements']` | `arg` | `run_campaign` caller / any downstream telemetry reader | `engine/mc_v18.py:315 final_state` |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| `World.settlements` | `RW` | `engine/autoload/game_state.py` (declared), written by `registry.py` | `engine/autoload/game_state.py:231 settlements` |
| `World.territory_infrastructure` | `RW` | `engine/autoload/game_state.py` (declared), written by `infrastructure.py` | `engine/autoload/game_state.py:220 territory_infrastructure` |
| `World.npc_drift_state` | `RW` (declared only — no live writer other than the module fallback; see §7) | `engine/autoload/game_state.py` (declared) / `temperaments.py` (`_drift_store`) | `engine/autoload/game_state.py:221 npc_drift_state` |
| `World.accord_drift_probe_hits` | `W` (dynamic attribute, not a dataclass field) | `systems/overview/sim/accounting.py` | `systems/overview/sim/accounting.py:92 accord_drift_probe_hits` |
| `Settlement.order` | `RW` | `registry.py` (dataclass); written by `echo_transport._apply_accord_echo`'s deferred `_apply` (dormant, S2.2.4); read by `registry.province_accord` | `systems/settlements/sim/registry.py:65 order`, `engine/cross_scale/echo_transport.py:335-341` |
| `Settlement.prosperity` | `RW` | `registry.py` (dataclass); written only at `populate_from_geography`; read by `registry.province_effective_prosperity` (no production reader) | `systems/settlements/sim/registry.py:63 prosperity` |
| `Settlement.defense` | `RW` | `registry.py` (dataclass); written only at `populate_from_geography`; read only inside the orphaned `settlement.py` derivation path (no production reader) | `systems/settlements/sim/registry.py:64 defense` |
| `Settlement.governor_id` | `W` | `registry.succeed_governor` (no production caller) | `systems/settlements/sim/registry.py:205 governor_id` |
| `Settlement.legitimacy` / `.popular_support` | — | Declared, never read or written anywhere in `sim/` (module docstring's own PRE-LPS-1 note) | `systems/settlements/sim/registry.py:69-74 legitimacy` |
| `Settlement.ledger` (`list[LedgerTag]`) | `RW` | `ledger.py` primitives via `Settlement.add_tag`/`has_tag`/`tags`; only live writers are the `tools/sim_harness` prototype adapters | `systems/settlements/sim/registry.py:87 ledger` |
| `Territory.accord` | `RW` | `engine/autoload/game_state.py` (dataclass); written directly by `systems/factions/sim/parliamentary_transfer.py:278` and `systems/factions/sim/mass_seizure.py:293`, bypassing `Settlement.order` entirely; read (never written) by the S5 drift probe | `engine/autoload/game_state.py:167 accord` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| `up` | `engine/autoload/game_state.py` (World) | `world.settlements` / `world.territory_infrastructure` / `world.npc_drift_state` registries declared on `World`, populated/serialized by settlements-owned modules | `engine/autoload/game_state.py:200-211` |
| `up` | `systems/overview/sim/accounting.py` | Season-end `run_accounting` reads `registry.province_accord`/`province_members` for the report-only drift probe (never writes settlement or territory state) | `systems/overview/sim/accounting.py:85-92` |
| `lateral` | `engine/cross_scale/echo_transport.py` | Personal-scene Accord Echo resolves a target `Settlement` by id and writes `Settlement.order` through a deferred Key (`sched.emit`), reachable-but-dormant absent a `scene_outcome`-declaring caller | `engine/cross_scale/echo_transport.py:291-343` |
| `lateral` | `systems/factions/sim/mass_seizure.py` | Reads `count_infrastructure`/`seizure_ob_modifier` (Church infrastructure) for seizure Ob math, then writes `Territory.accord` directly (not through settlements) | `systems/factions/sim/mass_seizure.py:159`, `systems/factions/sim/mass_seizure.py:260`, `systems/factions/sim/mass_seizure.py:293` |
| `lateral` | `systems/factions/sim/parliamentary_transfer.py` | Writes `Territory.accord` directly on a successful transfer (not through settlements) | `systems/factions/sim/parliamentary_transfer.py:278` |
| `lateral` | `systems/factions/sim/faction_action.py` | Reads `ADJACENCY` for conquest-target and threat-signal derivation | `systems/factions/sim/faction_action.py:42`, `systems/factions/sim/faction_action.py:139`, `systems/factions/sim/faction_action.py:188` |
| `lateral` | `systems/world/sim/insurgency_pipeline.py` | Reads `ADJACENCY` to group contiguous Uncontrolled territories for GD-3 insurgency-emergence checks | `systems/world/sim/insurgency_pipeline.py:116`, `systems/world/sim/insurgency_pipeline.py:133` |
| `in` (declared, unwired) | `systems/factions/sim/varfell_territorial_acquisition.py` | Module docstring lists `systems/settlements/sim/temperaments` as a dependency; no actual `import` exists in the file (verified — see §7) | `systems/factions/sim/varfell_territorial_acquisition.py:18` (systems/settlements/sim/temperaments) |
| `out` (prototype, unwired) | `tools/sim_harness/adapters/pr119_governance/*.py` | Exercises `register_settlement`, `succeed_governor`, `province_accord`, `province_effective_prosperity`, and every `Settlement.add_tag`/`has_tag`/`tags` ledger call — none of these call sites are reachable from `engine/mc_v18.py`'s production campaign loop | `tools/sim_harness/adapters/pr119_governance/pr119_integrated_campaign.py:112`, `tools/sim_harness/adapters/pr119_governance/pr119_integrated_campaign.py:222`, `tools/sim_harness/adapters/pr119_governance/pr119_integrated_campaign.py:262` |

## 7. Traced gaps

| Gap | Evidence anchor |
|---|---|
| `compute_settlement_state`/`aggregate_to_province` (`settlement.py`) — the module's own declared §1.3 derived-value + province-aggregation entry points — have **zero importers** anywhere in `engine/`, `systems/`, `tests/`; pinned as a verified orphan by the OI-12 census (`_OI12_VERIFIED_ORPHAN_NO_CALLSITE`) | `systems/settlements/sim/settlement.py:95`, `systems/settlements/sim/settlement.py:160`; `tests/valoria/test_oi12_orphan_census.py:50 settlement.py` |
| `temperaments.py` — all four entry points (`temperament_of`, `temperament_modifiers`, `apply_strain_shock`, `get_faction_aggregate`) have **zero importers**; `varfell_territorial_acquisition.py` names it as a "Dependency" in its own docstring but the file contains no matching `import` statement (grep-verified, no hit); pinned as a verified orphan by the same OI-12 census row | `systems/settlements/sim/temperaments.py:97`, `systems/settlements/sim/temperaments.py:105`, `systems/settlements/sim/temperaments.py:142`, `systems/settlements/sim/temperaments.py:163`; `systems/factions/sim/varfell_territorial_acquisition.py:18-20`; `tests/valoria/test_oi12_orphan_census.py:51 temperaments.py` |
| **The `accord_drift_probe_hits` probe is report-only telemetry, not a reconciliation.** It compares `registry.province_accord` (settlement-Order floor-mean aggregate) against `Territory.accord` (bucketed via `canonical_accord`) per province and increments a counter on divergence — it never writes either value, never blocks/gates any other step, and the two write models it observes (`Settlement.order` via S2.2.4/dormant Echo vs. `Territory.accord` via the two writers cited below) remain permanently uncoordinated by design — the module's own docstring defers reconciliation to a separate SE-lane workstream (OI-37) | `systems/overview/sim/accounting.py:53-92`; `systems/factions/sim/parliamentary_transfer.py:278`; `systems/factions/sim/mass_seizure.py:293` |
| **Two independent, uncoordinated settlement-scale entities exist per province.** `World.territories` (T1-T17, built from `STARTING_OWNER`/`STARTING_ACCORD` module constants at world-gen) and `World.settlements` (37 settlements, built from `valoria_geography_v30.yaml` via `populate_from_geography`, keyed by settlement id `S-0xx` with a `province_id` pointing at a territory id) are populated from two different sources in the same `create_world()` call, with no code that cross-validates them beyond the report-only S5 probe | `engine/autoload/game_state.py:223-234` (Territory build); `engine/autoload/game_state.py:259-260` (settlements build); `systems/settlements/sim/registry.py:215-266 populate_from_geography` |
| **The Accord Echo settlement-write leg (S2.2.3/S2.2.4) is wired but organically dormant.** `classify_scene_outcome` only accepts an explicit caller-declared `echo['scene_outcome']`; no live producer in the campaign loop (`scene_dispatch.py`'s emergency_council/combat branches, `parliamentary_bridge.py`'s vote ctx) sets that key, so `_apply_accord_echo` never fires in a seeded campaign — confirmed by the module's own docstring and exercised only by direct unit tests | `engine/cross_scale/echo_transport.py:134-170`, `engine/cross_scale/echo_transport.py:360-455`; `engine/tests/test_accord_echo.py:8-11` |
| **The Ledger (durable governance memory) has no production writer.** `LedgerTag`/`ledger_add`/`ledger_sweep` and `Settlement.add_tag`/`has_tag`/`tags` are fully implemented, but the only call sites anywhere in the repo outside `ledger.py`/`registry.py` themselves are `tools/sim_harness/adapters/pr119_governance/*.py` (a prototype harness, not imported by `engine/`, `systems/*/sim/`, or any CI-run test) — `succeed_governor`, the one production entry point that would trigger `ledger_sweep`, itself has no production caller | `systems/settlements/sim/ledger.py:47-75`; `systems/settlements/sim/registry.py:198-207 succeed_governor`; `tools/sim_harness/adapters/pr119_governance/pr119_event_deck_engine.py:114` (representative `add_tag` call site) |
| `build_infrastructure` (the write-side Axis 1-4 constructor) has no importer in `engine/`, `systems/`, or `tests/` — only its read-side siblings (`count_infrastructure`, `seizure_ob_modifier`) are called in production; its only call sites anywhere are the `tools/sim_harness/adapters/pr119_governance` prototype harness (`pr119_integrated_campaign.py`, `pr119_subnational_factions.py`), not wired to CI | `systems/settlements/sim/infrastructure.py:139 build_infrastructure`; `tools/sim_harness/adapters/pr119_governance/pr119_integrated_campaign.py:198-199 build_infrastructure`; `tools/sim_harness/adapters/pr119_governance/pr119_subnational_factions.py:98 build_infrastructure` |
| The geography YAML's top-level `provinces:` block (per-province `fort_level`, `starting_pros`, `spiritual_weight`, `proximity_calamity`, `polygon`, `anchor`, `settlements:` list, `description`) is read by **no production code anywhere** — `populate_from_geography` reads only the `settlements:` map, never `data['provinces']`/`data.get('provinces')`, and a tree-wide grep for either form returns zero hits | `systems/settlements/valoria_geography_v30.yaml:18-31`; `systems/settlements/sim/registry.py:249 populate_from_geography` |
| `Settlement.legitimacy`/`Settlement.popular_support` are declared 0-7 fields with zero readers or writers anywhere in `sim/`, an inert schema stub per the module's own inline note (PRE-LPS-1, ED-FA-0004) | `systems/settlements/sim/registry.py:69-74` |
| `restore_world`'s `settlements` branch has no production caller — only exercised by `engine/tests/test_world_population.py`'s explicit serialize/restore round-trip | `engine/autoload/game_state.py:418-420`; `engine/tests/test_world_population.py:1-18` |
| **Two same-named, differently-keyed fields, both called `religious_building`.** `Settlement.religious_building` (`registry.py`) is touched only by the dataclass's own `to_dict`/`from_dict` — never set by `populate_from_geography`, never read by any logic — so it round-trips through serialization while being logically dead. The live field is a different store entirely: `InfrastructureState.religious_building`, written by `build_infrastructure` and read by `count_infrastructure`/`seizure_ob_modifier`. | `systems/settlements/sim/registry.py:81 religious_building`; `systems/settlements/sim/registry.py:123 religious_building`; `systems/settlements/sim/registry.py:148 religious_building`; `systems/settlements/sim/infrastructure.py:81 religious_building`; `systems/settlements/sim/infrastructure.py:160 religious_building`; `systems/settlements/sim/infrastructure.py:208 religious_building`; `systems/settlements/sim/infrastructure.py:246 religious_building` |
| **The `settlement_layer` contract's `executes:false` flag is correct for the file it names, but that file is the wrong one.** Its declared `sim_module` is `settlement.py`, the orphan this skeleton independently proves has zero importers; the live registry code (`registry.py`) that actually runs at boot and every `loop.s3` has no contract entry of its own. The contract pointing at the dead file while the live file goes uncontracted is the real defect. | `references/module_contracts.yaml:712-715 settlement_layer`; `systems/settlements/sim/settlement.py:95 compute_settlement_state`; `systems/settlements/sim/registry.py:215 populate_from_geography` |
