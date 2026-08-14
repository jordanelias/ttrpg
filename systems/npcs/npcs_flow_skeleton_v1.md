# NPCs — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

[EDITORIAL: this file is a traced structural skeleton (code-as-built, not design prose) — see
`systems/_architecture/subsystem_flow_skeletons_v1.md` for the format contract. `systems/npcs/`
itself holds only docs (zero `.py` files); every anchor below points at the code home the tracing
found elsewhere in the tree.]

**Subsystem:** `systems/npcs/` · **Lane:** `WR` · **Contracts:** `npc_behavior`, `npc_memory`
**Code roots traced:** `engine/autoload/npc_ai.py`, `systems/world/sim/npe.py`,
`systems/overview/sim/accounting.py`, `engine/mc_v18.py`, `engine/autoload/game_state.py`,
`engine/substrate/stubwire.py`, `engine/substrate/canon_buckets.py`
**Traced at:** `6545067`

## 1. Entry points

| Callable | Anchor | Called by |
|---|---|---|
| `generate_npc(faction, role, world, territory_id, rng)` | `systems/world/sim/npe.py:215 generate_npc` | `—` (no production call site; see §7 gap 1) |
| `simulate_npc_actions(world)` | `systems/world/sim/npe.py:325 simulate_npc_actions` | `systems/overview/sim/accounting.py:138 simulate_npc_actions` |
| `get_npcs_in_territory(territory_id, world)` | `systems/world/sim/npe.py:375 get_npcs_in_territory` | `—` (no caller found; see §7 gap 4) |
| `reset_npcs(world)` | `systems/world/sim/npe.py:380 reset_npcs` | `—` (test-helper docstring; no caller found) |
| `select_action(actor_id, world)` | `engine/autoload/npc_ai.py:33 select_action` | `—` (only reached by `engine/tests/test_pipeline_reach.py:763`, a stub-wired-check probe, not a production caller; see §7 gap 2) |
| `evaluate_priority_stack(actor_id, world)` | `engine/autoload/npc_ai.py:41 evaluate_priority_stack` | `—` (no caller found; see §7 gap 2) |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `world` (`World`) | arg | caller-supplied `GameState`/`World` | `systems/world/sim/npe.py:215 generate_npc` |
| `world.territories[tid].accord` / `.prosperity` / `.owner` | world-state | `Territory` fields read for ecology weighting | `systems/world/sim/npe.py:175-197 _ecology_weights` |
| `world.rng` | world-state | campaign RNG, falls back to a fresh `random.Random()` when absent | `systems/world/sim/npe.py:231-234 rng` |
| `faction`, `territory_id` | arg | optional caller overrides on `generate_npc` | `systems/world/sim/npe.py:215-217 generate_npc` |
| `role` | arg | accepted parameter on `generate_npc`, never read in the function body — docstring marks it reserved for future use | `systems/world/sim/npe.py:226-227 generate_npc` |
| `world.npcs` (per-territory NPC lists) | world-state | populated store `simulate_npc_actions` iterates | `systems/world/sim/npe.py:338 store` |
| `world.season` | world-state | stamped onto emitted `NPCAction.season` | `systems/world/sim/npe.py:369 NPCAction` |
| `actor_id`, `world` | arg | `npc_ai` entry-point signatures (unused inside the stub bodies) | `engine/autoload/npc_ai.py:33-46 select_action` |

## 3. Flow

- **S1** `[branch]` `generate_npc` resolves an `rng` — caller-supplied, else `world.rng`, else a
  fresh `random.Random()`. `systems/world/sim/npe.py:231-234 rng`
- **S2** `[branch]` If `territory_id` is `None`, one is drawn via `rng.choice(world.territories)`.
  `systems/world/sim/npe.py:236-237 territory_id`
- **S3** `_ecology_weights(world, territory_id)` computes prosperity/accord-derived weight
  modifiers for the territory, converting `Territory.accord` (continuous) through
  `canonical_accord` first. `systems/world/sim/npe.py:175-212 _ecology_weights`
  - **S3.1** `[gate]` `canonical_accord` buckets the continuous value via nearest-midpoint
    comparisons. `engine/substrate/canon_buckets.py:38-48 canonical_accord`
- **S4** `[branch]` Tier-1 archetype seed: faction affiliation is the caller override, else a
  weighted roll toward the controlling faction. `systems/world/sim/npe.py:243-246 npc_faction`
- **S5** `[loop]` Per active issue, a base Stance value is nudged by ecology weights.
  `systems/world/sim/npe.py:250-259 ACTIVE_ISSUES`
- **S6** Worldview conviction(s), compromise category, volatility and loyalty are derived from
  `rng` draws and ecology weights. `systems/world/sim/npe.py:262-276 CONVICTIONS`
- **S7** `[branch]` Tier-2 deviation roll (`rng.randint(1, DEVIATION_DIE_MAX)`); above threshold,
  `is_arc_vector` is set and one of four live axes (Stance / Worldview / Compromise / Volatility)
  is flipped to its opposite extreme; a fifth branch (hidden allegiance) computes but never
  applies — see §7 gap. `systems/world/sim/npe.py:279-305 dev_roll`
- **S8** `[write]` An `NPC` is constructed and appended to the territory's list in the resolved
  store (`world.npcs` when present, else the module-level fallback).
  `systems/world/sim/npe.py:307-321 _next_npc_id_val`
- **S9** `[emit]` `generate_npc` returns the constructed `NPC`. `systems/world/sim/npe.py:322 npc`
- **T1** `simulate_npc_actions` resolves `world.rng` (or a fresh `random.Random()`) and reads the
  NPC store. `systems/world/sim/npe.py:333-338 rng`
- **T2** `[loop]` For every same-territory NPC pair: `[gate]` skip unless worldviews share a
  conviction. `systems/world/sim/npe.py:341-345 npcs`
- **T3** `[gate]` `[loop]` Collect issues where the pair's Stance values are exactly adjacent
  (`abs(diff) == 1`); skip the pair if none. `systems/world/sim/npe.py:347-354 adj_pairs`
- **T4** `[gate]` Roll `d6` against the pair's average Volatility. `systems/world/sim/npe.py:356-357 avg_vol`
- **T5** `[write]` On pass, shift both NPCs' Stance on the first adjacent-issue pair toward each
  other by one step. `systems/world/sim/npe.py:358-365 issue`
- **T6** `[emit]` Append an `NPCAction(action_type='stance_drift', ...)` descriptor.
  `systems/world/sim/npe.py:366-371 NPCAction`
- **T7** `[emit]` Return the accumulated action list (discarded by its accounting caller — see §4).
  `systems/world/sim/npe.py:372 actions` / `systems/overview/sim/accounting.py:138 simulate_npc_actions`
- **U1** `[gate]` `select_action` / `evaluate_priority_stack` unconditionally return
  `stubwire.stub_resolve(...)` — no branching, no world read, no NPC selected.
  `engine/autoload/npc_ai.py:33-46 select_action`

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `NPC` (return value) | arg | caller of `generate_npc` — no in-tree production caller (§7 gap 1) | `systems/world/sim/npe.py:322 npc` |
| `world.npcs[territory_id]` append | write | `world` (persisted via `game_state.serialize_world`/`restore_world`) | `systems/world/sim/npe.py:320-321 store` |
| `world.npc_counter` increment | write | `world` state; read back as `CampaignResult.npcs_generated` telemetry | `systems/world/sim/npe.py:107-109 _next_npc_id` / `engine/mc_v18.py:299 npcs_generated` |
| `list[NPCAction]` (return value) | arg | `systems/overview/sim/accounting.run_accounting`, which discards it by design | `systems/overview/sim/accounting.py:138 simulate_npc_actions` |
| Mutated `NPC.stance` values (in-place) | write | `world.npcs` store (same objects `get_npcs_in_territory` would read) | `systems/world/sim/npe.py:360-365 issue` |
| `StubResult(module, io_contract, reason)` | arg | caller of `select_action`/`evaluate_priority_stack` — none in production | `engine/autoload/npc_ai.py:34-38 select_action` |
| `stubwire.invocations` increment | write | `engine/substrate/stubwire.py` module counter, folded into `CampaignResult.stub_hits` | `engine/substrate/stubwire.py:65-66 invocations` |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| `World.npcs` | RW | `engine/autoload/game_state.py` (declared) / `systems/world/sim/npe.py` (read+written) | `engine/autoload/game_state.py:185 npcs` |
| `World.npc_counter` | RW | `engine/autoload/game_state.py` (declared) / `systems/world/sim/npe.py` (incremented) | `engine/autoload/game_state.py:186 npc_counter` |
| `Territory.accord` / `.prosperity` / `.owner` | R | `engine/autoload/game_state.py` (`Territory`) | `systems/world/sim/npe.py:175-197 _ecology_weights` |
| `World.rng` | R | `engine/autoload/game_state.py` | `systems/world/sim/npe.py:231 rng` / `systems/world/sim/npe.py:333 rng` |
| `World.season` | R | `engine/autoload/game_state.py` | `systems/world/sim/npe.py:369 NPCAction` |
| `_npcs_by_territory` / `_npc_counter` (module fallback) | RW | `systems/world/sim/npe.py` | `systems/world/sim/npe.py:95-96` |
| serialized `snapshot['npcs']` / `snapshot['npc_counter']` | W (serialize) / R (restore) | `engine/autoload/game_state.py` | `engine/autoload/game_state.py:301-304 npc_counter` / `engine/autoload/game_state.py:375-379 NPC` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| up | `engine/autoload/game_state` | `World.npcs`/`.npc_counter` registry fields owned by game_state, populated by npe | `engine/autoload/game_state.py:185-186 npcs` |
| lateral | `systems/overview/sim/accounting` | `simulate_npc_actions` called every season from `run_accounting` step 5 | `systems/overview/sim/accounting.py:50 simulate_npc_actions` / `systems/overview/sim/accounting.py:138 simulate_npc_actions` |
| lateral | `engine/mc_v18` | honest-deferral `stubwire.stub_resolve('generate_npc(world-gen|season-tick)', ...)` fired once per season instead of calling `generate_npc` | `engine/mc_v18.py:186-194 stub_resolve` |
| down | `engine/substrate/canon_buckets` | `_ecology_weights` imports `canonical_accord` as a no-deps leaf | `systems/world/sim/npe.py:44 canonical_accord` |
| down | `engine/substrate/stubwire` | `npc_ai.select_action`/`evaluate_priority_stack` route through `stub_resolve` | `engine/autoload/npc_ai.py:19 stubwire` / `engine/autoload/npc_ai.py:34 stub_resolve` / `engine/autoload/npc_ai.py:42 stub_resolve` |
| declared, unimplemented | `systems/factions` (npc_behavior contract's `consumes`/`emits` Key edges: `scene.gossip`, `scene.witness`, `state.opinion_revised`, etc.) | contract declares edges against a `sim_module: none` — see §7 gap 3 | `references/module_contracts.yaml:126 npc_behavior` / `references/module_contracts.yaml:162 npc_behavior` |

## 7. Traced gaps

| Gap | Evidence anchor |
|---|---|
| `generate_npc` has no world-gen or season-tick call site — `engine/mc_v18.py` fires a `stubwire.stub_resolve('generate_npc(world-gen|season-tick)', ...)` in its place every season, and a dedicated test pins `npcs_generated == 0` on a seeded campaign. Only `simulate_npc_actions` (the drift half) is wired. | `engine/mc_v18.py:186-194 stub_resolve` · `engine/tests/test_world_population.py:142-154 test_generate_npc_has_no_automatic_call_site_this_wave` · `engine/mc_v18.py:299 npcs_generated` |
| `engine/autoload/npc_ai.py`'s two declared entry points (`select_action`, `evaluate_priority_stack`) are unconditional `stubwire.stub_resolve` no-ops with no branching and no production caller anywhere in `engine/`, `systems/`, or `tests/` — the only reference outside the module itself is a test asserting the stub-wired shape, not a live call. | `engine/autoload/npc_ai.py:33-46 select_action` · `engine/tests/test_pipeline_reach.py:763 select_action` · `engine/tests/test_pipeline_reach.py:767-779 test_oi17_full_module_conversions_are_stub_wired` (grep confirms no other caller) |
| The `npc_behavior` module contract (`references/module_contracts.yaml`) declares a full `consumes`/`emits`/`state`/`gates` Key-flow shape (Procedures B/C/D/E — all four declared accounting phases, none implemented) against `sim_module: none` — explicitly re-verified (OI-54, ED-IN-0097) that `systems/npcs/` holds zero `.py` files. None of this declared flow exists in code; `npc_ai.py` was considered and explicitly rejected as an implementation because it is itself a stub shell. The companion `npc_memory` contract (consumes 4 of `npc_behavior`'s emit types) is `doc: null`, `sim_module: none`, with its own gap note stating a grep for `npc_memory*` returns nothing tree-wide — no npc-memory store exists in code at all. | `references/module_contracts.yaml:126-141 npc_behavior` (sim_module: none) · `references/module_contracts.yaml:230-247 npc_memory` (doc: null, sim_module: none, "find/grep for npc_memory* across the tree returns nothing") |
| `get_npcs_in_territory` and `reset_npcs` (`systems/world/sim/npe.py`) have no caller anywhere in `engine/`, `systems/`, or `tests/` other than their own definitions — `reset_npcs`'s own docstring calls it a "Test helper" but no test invokes it. | `systems/world/sim/npe.py:375-377 get_npcs_in_territory` · `systems/world/sim/npe.py:380-386 reset_npcs` (grep confirms no other reference) |
| `mechanics_index.yaml`'s `npc_ai_service` entry cites `systems/_architecture/complete_systems_reference.md#part-1` as its canon source and marks `test_status: contested`, flagging the priority-stack contents as possibly contaminated pending an audit — a doc↔code divergence the contract layer records but the code carries no trace of (the function bodies are pure stub calls, no priority-stack data structure exists). | `registers/mechanics_index.yaml:192-198 npc_ai_service` · `engine/autoload/npc_ai.py:6` · `engine/autoload/npc_ai.py:21-30` |
| Tier-2 deviation's `flip_choice == 2` branch (hidden allegiance) computes a local `hidden_allegiance` value that is never passed to the `NPC(...)` constructor — the constructor call has no `hidden_allegiance=` kwarg, so this branch is dead: every generated NPC keeps the dataclass default (`None`) regardless of the roll. | `systems/world/sim/npe.py:296-299 hidden_allegiance` · `systems/world/sim/npe.py:308-319 NPC` |
| `PIETY_HIGH`/`PIETY_LOW` are declared but never referenced in `_ecology_weights` or `generate_npc` — the code comment there states Territory has no piety field and prosperity is used as a proxy instead. | `systems/world/sim/npe.py:56-57 PIETY_HIGH` · `systems/world/sim/npe.py:198-199 _ecology_weights` |
| The `npc_behavior` contract's own `doc:` field was repointed (C-KEY-2, 2026-07-29) to a doc homed under `systems/factions/`, demoting `npc_behavior_v30.md` to a `sources:` citation — so this folder owns neither the code (`sim_module: none`) nor the doc of its own primary contract. `CURRENT.md`'s "NPC behaviour" row still heads at the demoted doc, so the currency authority and the contract layer disagree about this subsystem's head. | `references/module_contracts.yaml:129 npc_behavior` · `CURRENT.md:49 npc_behavior_v30` |
| Zero `mechanics_index.yaml` entries resolve into `systems/npcs/` — no mechanic cites any `systems/npcs/` path in `canon_sources` or `sim_module`; the conceptually-matching `npc_ai_service` entry is canon'd and sim'd elsewhere. | `registers/mechanics_index.yaml:192 npc_ai_service` |
| `npc_behavior` sits in an L2 contract-layer cycle with `faction_state`, `piety_track` and `social_contest`, and is itself an L2-layer cut-vertex. | `audit/2026-08-06-vector-audit/structure_audit/data/structure_metrics.json:338 npc_behavior` · `audit/2026-08-06-vector-audit/structure_audit/data/structure_metrics.json:333 npc_behavior` |
