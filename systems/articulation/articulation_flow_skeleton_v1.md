# Articulation — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/articulation/` · **Lane:** `IN` · **Contracts:** `articulation_layer`
**Code roots traced:** `engine/cross_scale/articulation.py`, `engine/cross_scale/__init__.py`,
`engine/mc_v18.py`, `engine/substrate/keys.py`, `engine/substrate/stubwire.py`,
`engine/substrate/__init__.py`, `engine/cross_scale/echo_transport.py`,
`engine/cross_scale/scene_dispatch.py`, `engine/cross_scale/zoom_in_out.py`,
`tests/valoria/test_articulation_subscriber.py`, `engine/tests/test_pipeline_reach.py`,
`tools/build_execution_map.py`, `references/module_contracts.yaml`
**Traced at:** `6545067`

`systems/articulation/` itself holds no `.py` — only `articulation_layer_v30.md` and
`_identifier_census.yaml`. Its code lives at `engine/cross_scale/articulation.py`
(`references/module_contracts.yaml:966` `sim_module`), per standing rule 1.

## 1. Entry points

| Callable | Anchor | Called by |
|---|---|---|
| `render_protagonist_lens(actor_id, world)` | `engine/cross_scale/articulation.py:35 render_protagonist_lens` | — (no call site found anywhere in the tree outside its own definition/docstring) |
| `evaluate_articulation_triggers(world)` | `engine/cross_scale/articulation.py:44 evaluate_articulation_triggers` | `engine/tests/test_pipeline_reach.py:762 evaluate_articulation_triggers` — a stub-conversion regression probe only; see §7 |
| `generate_chronicle_entry(event, world)` | `engine/cross_scale/articulation.py:53 generate_chronicle_entry` | — (no call site found anywhere in the tree outside its own definition/docstring) |
| `subscribe_all(scheduler)` | `engine/cross_scale/articulation.py:152 subscribe_all` | `engine/mc_v18.py:258 subscribe_all` (production); `engine/tests/test_pipeline_reach.py:649 subscribe_all` and `:681 run_campaign` (test reach probes); `tests/valoria/test_articulation_subscriber.py:233 subscribe_all` (unit tests) |
| `_make_trigger_callback(type_id)` | `engine/cross_scale/articulation.py:133 _make_trigger_callback` | `engine/cross_scale/articulation.py:169 _make_trigger_callback` (inside `subscribe_all`'s loop) |
| `_on_key(key, scheduler)` (closure returned by `_make_trigger_callback`) | `engine/cross_scale/articulation.py:140 _on_key` | `engine/substrate/keys.py:577 callback` — `TickScheduler._emit_at_depth`'s subscriber-dispatch loop |

## 2. IN

| Input | kind | origin | anchor |
|---|---|---|---|
| `world` (GameState) | world-state | `engine.mc_v18.run_campaign` | `engine/cross_scale/articulation.py:44 evaluate_articulation_triggers` |
| `actor_id` | arg | caller (no live caller — §7) | `engine/cross_scale/articulation.py:35 render_protagonist_lens` |
| `event` | arg | caller (no live caller — §7) | `engine/cross_scale/articulation.py:53 generate_chronicle_entry` |
| `scheduler` (`TickScheduler`) | arg | `world.echo_scheduler`, built by `echo_transport.make_scheduler` | `engine/mc_v18.py:258 subscribe_all` |
| `ECHO_TRANSPORT` (params/env flag; default ON) | flag | `effective_params` / `os.environ` | `engine/mc_v18.py:57-67 _echo_transport_on` (definition; call site `engine/mc_v18.py:241 _echo_transport_on`) |
| `_TRIGGER_TYPE_IDS` (13-entry roster) | param | hardcoded tuple in this module | `engine/cross_scale/articulation.py:116 _TRIGGER_TYPE_IDS` |
| `key` (`Key`, the emitted object passed to the callback) | key | `TickScheduler._emit_at_depth`'s subscription loop | `engine/substrate/keys.py:577 callback` |

## 3. Flow

- **S1** `[gate]` Campaign boot resolves the `ECHO_TRANSPORT` flag (params override, else env var,
  default `'1'`). Resolution logic: `engine/mc_v18.py:57-67 _echo_transport_on`; called at
  `engine/mc_v18.py:241 _echo_transport_on`
  - **S1.1** `[branch]` If ON: attach `world.echo_scheduler = echo_transport.make_scheduler(...)`.
    `engine/mc_v18.py:243 make_scheduler`
  - **S1.2** `[write]` `subscribe_all(world.echo_scheduler)` runs once at boot, inside the same
    `if _echo_transport_on(...)` branch. `engine/mc_v18.py:258 subscribe_all`
    - **S1.2.1** `[loop]` For each of the 13 `_TRIGGER_TYPE_IDS`, register one closure via
      `scheduler.subscribe(type_id, _make_trigger_callback(type_id))`, mutating
      `scheduler.subscriptions`. `engine/cross_scale/articulation.py:168-169 subscribe_all`
- **S2** `[gate]` For a callback to ever fire, some production code must call
  `scheduler.emit`/`schedule_emission` with a `Key` whose `.type` matches one of the 13 ids.
  `engine/substrate/keys.py:510 emit`
  - **S2.1** `[branch]` The only production module that constructs and emits real `Key` objects
    anywhere in `engine/` is `echo_transport.py`; it maps `scene_type -> key type` for exactly
    two families (`"contest"`, `"combat"`) and separately builds one `scene.accord_echo` Key.
    `engine/cross_scale/echo_transport.py:107-110 KEY_TYPE_BY_SCENE`,
    `engine/cross_scale/echo_transport.py:319-321 Key`
  - **S2.2** `[gate]` Both paths require the calling scene's `ctx['echo']` block to already carry
    explicit fields (`actor_faction`/`most_relevant_stat` for the §5.2 leg;
    `echo['scene_outcome']` for the accord-echo leg) — neither is populated by any live
    `scene_dispatch.py` caller under default flags. `engine/cross_scale/scene_dispatch.py:55`
    (`DISPATCH_COMBAT_BRIDGE off (today's default) this stays empty`),
    `engine/cross_scale/echo_transport.py:34-37` (no live producer declares `scene_outcome`)
- **S3** `[emit]` When a matching `Key` IS emitted, `TickScheduler._emit_at_depth` logs it, then
  synchronously calls every callback registered for `key.type`.
  `engine/substrate/keys.py:576-577 callback`
- **S4** `[emit]` The fired callback (`_on_key`) ignores the `Key`'s contents and returns a typed
  no-op via `stubwire.stub_resolve` — no state is read from or written to `world` or the `Key`.
  `engine/cross_scale/articulation.py:141 stub_resolve`
- **S5** `[write]` `stubwire.invocations` (a process-cumulative module-global counter) increments
  by one per firing. `engine/substrate/stubwire.py:66 invocations`
- **S6** `[emit]` At campaign end, `run_campaign` reads the pre/post delta of that counter into
  `CampaignResult.stub_hits`. `engine/mc_v18.py:300 stub_hits`

No step above reaches `render_protagonist_lens`, `generate_chronicle_entry`, or
`evaluate_articulation_triggers` in production — see §7.

## 4. OUT

| Output | kind | consumer | anchor |
|---|---|---|---|
| `StubResult` (frozen, `stub=True`) | return value, discarded by the caller | `TickScheduler._emit_at_depth`'s `callback(key, self)` call does not capture the return value | `engine/cross_scale/articulation.py:141 stub_resolve`, `engine/substrate/keys.py:577 callback` |
| `stubwire.invocations` delta | telemetry counter | `CampaignResult.stub_hits` | `engine/mc_v18.py:300 stub_hits` |
| `scheduler.subscriptions[type_id]` list entries | registration side-effect | `engine.substrate.keys.TickScheduler` (owning instance, held on `world.echo_scheduler`) | `engine/cross_scale/articulation.py:169 subscribe_all`, `engine/substrate/keys.py:507 subscribe` |

No `Key`, world-state field, or rendered artifact is ever produced by this module — see §7.

## 5. State touched

| Field | R/W | owning module | anchor |
|---|---|---|---|
| `world.echo_scheduler` | R | `engine.mc_v18` / `engine.cross_scale.echo_transport` | `engine/mc_v18.py:258 subscribe_all` |
| `TickScheduler.subscriptions` | W (append-only, via `.subscribe`) | `engine.substrate.keys` | `engine/substrate/keys.py:507 subscribe` |
| `stubwire.invocations` | W | `engine.substrate.stubwire` | `engine/substrate/stubwire.py:66 invocations` |

Articulation owns no field of its own on `world`, `GameState`, or any faction/territory/NPC
record — it reads the scheduler handed to it and writes only into that scheduler's subscription
list and the shared stub counter. `render_protagonist_lens`/`generate_chronicle_entry` declare
`LensState`/`ChronicleEntry` return types in the docstring but construct neither.
`engine/cross_scale/articulation.py:13-15`

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| `in` | `engine.mc_v18` (campaign driver) | Calls `subscribe_all` once per campaign, inside the `ECHO_TRANSPORT`-on boot branch | `engine/mc_v18.py:257-258` |
| `out` | `engine.mc_v18` (campaign driver) | Telemetry only: the campaign reads the `stubwire.invocations` delta this subsystem's fired callbacks contribute to, into `CampaignResult.stub_hits`. No state crosses — the counter is the entire payload | `engine/mc_v18.py:300 stub_hits` |
| `out` | `engine.substrate.keys.TickScheduler` | `subscribe_all` registers callbacks via the substrate's `.subscribe`; callbacks are later invoked by the substrate's own emission path | `engine/cross_scale/articulation.py:169 subscribe_all`, `engine/substrate/keys.py:576-577 callback` |
| `lateral` | `engine.cross_scale.echo_transport` | The sole production module that ever constructs a `Key` of a type articulation subscribes to (`scene.combat_resolved`, `scene.accord_echo`) | `engine/cross_scale/echo_transport.py:97-100`, `:309-311` |
| `lateral` | `engine.cross_scale.scene_dispatch` | Gates whether `echo_transport` ever receives a populated `ctx['echo']` to build a Key from (default: it does not) | `engine/cross_scale/scene_dispatch.py:55` |

## 7. Traced gaps

| Gap | Evidence anchor |
|---|---|
| **Tier 1 render layer is entirely uncalled.** `render_protagonist_lens` is a stub with zero callers anywhere in the tree — production or test — beyond its own definition/docstring listing. | `engine/cross_scale/articulation.py:35-41`; whole-repo grep for the symbol name finds no call site |
| **Tier 3 chronicle layer is entirely uncalled.** `generate_chronicle_entry` is likewise never invoked. | `engine/cross_scale/articulation.py:53-59`; whole-repo grep for the symbol name finds no call site |
| **Tier 2's own trigger-evaluation function is never invoked by production code either.** `evaluate_articulation_triggers`'s only caller in the tree is a stub-conversion regression probe that asserts it is *still* stub-wired, not a consumer of its output; `engine/mc_v18.py`'s season loop never calls it. | `engine/tests/test_pipeline_reach.py:749-762 _OI17_FULL_MODULE_ENTRYPOINTS` / `:767 test_oi17_full_module_conversions_are_stub_wired` |
| **10 of the 13 subscribed trigger type_ids have zero production emitter anywhere in `.py` code.** (`state.scar_acquired`, `state.coup_attempted`, `state.succession`, `mechanical.mission_shift`, `da.covert_betrayal`, `meta.knot_formed`, `meta.knot_ruptured`, `env.peninsular_strain_shock`, `meta.cascade_cluster_event`, `state.belief_revised`.) Nothing outside the roster constant itself and the test fixture constructs a `Key` of these types, so the corresponding callbacks can never fire in a real campaign. | `engine/cross_scale/articulation.py:117-126 _TRIGGER_TYPE_IDS`; whole-repo grep for each literal type string as a Python value returns only `tests/valoria/test_articulation_subscriber.py` |
| **`scene.combat_felled` is subscribed but has no emission path at all.** `echo_transport.py`'s `KEY_TYPE_BY_SCENE` maps only `"contest"` and `"combat"` scene types (to `scene.contest_resolved`/`scene.combat_resolved`) — no code path builds a `scene.combat_felled` Key. | `engine/cross_scale/echo_transport.py:107-110 KEY_TYPE_BY_SCENE` |
| **`scene.combat_resolved`'s one live emission path is behind a default-off flag.** Reaching it requires `DISPATCH_COMBAT_BRIDGE=1` (default `'0'`); the reach test for this path is an `xfail` under the default. | `engine/mc_v18.py:71-81 _dispatch_combat_bridge_on`, `engine/cross_scale/scene_dispatch.py:55`, `engine/tests/test_pipeline_reach.py:693-695 test_combat_pair_key_reaches_articulation_subscriber_under_flag_on` |
| **`scene.accord_echo`'s one live emission path is organically dormant.** It requires a caller-declared `echo['scene_outcome']`, which no live `scene_dispatch.py`/`parliamentary_bridge.py` caller sets today. | `engine/cross_scale/echo_transport.py:34-37` |
| **Net: `subscribe_all` wires all 13 callbacks at every default campaign boot, but under default flags none of the 13 can ever fire in a live campaign** — the whole Tier-2 trigger flow is structurally present and dormant, not partially reachable. | Composite of the four rows above; `engine/mc_v18.py:241-258` (default-flag boot path) |
| **Declared vs. actual `consumes` contract diverges.** `module_contracts.yaml` declares articulation as a universal wildcard reader of the Key stream (`{type: "*", from: engine}`); the actual code subscribes to exactly the 13 explicit ids in `_TRIGGER_TYPE_IDS` and nothing else — no wildcard subscription exists in this module. | `references/module_contracts.yaml:972-974`; `engine/cross_scale/articulation.py:116-130 _TRIGGER_TYPE_IDS` |
| **`subscribe_all` is non-idempotent by construction and unguarded.** A second call on the same scheduler double-registers every callback (`TickScheduler.subscribe` is purely additive); nothing in code enforces the "call exactly once per scheduler lifetime" contract — it is stated only in the docstring. | `engine/cross_scale/articulation.py:163-166 subscribe_all` docstring, `engine/substrate/keys.py:506-507 subscribe` |
