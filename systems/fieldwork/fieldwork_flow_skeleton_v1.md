# Fieldwork — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/fieldwork/` · **Lane:** `FI` · **Contracts:** `fieldwork_knots` (only
contract-declared module in this subsystem; `fieldwork`/`investigation` have no
`module_contracts.yaml` entry — `references/module_contracts.yaml:373`)
**Code roots traced:** `systems/fieldwork/sim/fieldwork.py`, `systems/fieldwork/sim/investigation.py`,
`systems/fieldwork/sim/knots.py`, `systems/fieldwork/__init__.py`, plus importers found by grep across
`engine/`, `systems/`, `tests/`: `engine/cross_scale/scene_dispatch.py`, `engine/mc_v18.py`,
`engine/autoload/game_state.py`, `engine/autoload/scene_slate.py`, `engine/tests/test_knots_ed912.py`,
`engine/tests/test_world_population.py`, `engine/tests/test_pipeline_reach.py`,
`systems/threadwork/sim/opposing.py`, `tests/valoria/test_oi12_orphan_census.py`
**Traced at:** `654506799c637e83eae33377a7b0974317721b0a`

## 1. Entry points

| Callable | Anchor | Called-by |
|---|---|---|
| `run_fieldwork_scene(scene)` | `systems/fieldwork/sim/fieldwork.py:38 run_fieldwork_scene` | `engine/cross_scale/scene_dispatch.py:354` (`_resolve_slot`, `st == "fieldwork"` branch) — reachable only via a `SceneSlot` manually constructed by a test (`engine/tests/test_pipeline_reach.py:298`); no production caller ever queues `scene_type="fieldwork"` (§7) |
| `advance_disposition(target, delta)` | `systems/fieldwork/sim/fieldwork.py:46 advance_disposition` | `—` (no caller found anywhere in `engine/`, `systems/`, `tests/`) |
| `advance_evidence(case, delta)` | `systems/fieldwork/sim/fieldwork.py:54 advance_evidence` | `—` (no caller found) |
| `resolve_npe_response(npc_id, prompt, world)` | `systems/fieldwork/sim/investigation.py:30 resolve_npe_response` | `engine/cross_scale/scene_dispatch.py:356` (`_resolve_slot`, `st == "investigation"` branch) — same test-only reachability as `run_fieldwork_scene` above |
| `evaluate_dialogue_lattice(scene, choice)` | `systems/fieldwork/sim/investigation.py:38 evaluate_dialogue_lattice` | `—` (no caller found) |
| `apply_response_matrix(actor, target, action)` | `systems/fieldwork/sim/investigation.py:46 apply_response_matrix` | `—` (no caller found) |
| `form_knot(actor_a, actor_b, world, actor_a_obj, actor_b_obj, season, rng)` | `systems/fieldwork/sim/knots.py:172 form_knot` | `—` in production (`engine/mc_v18.py` records a `stubwire.stub_resolve` call under the literal name `'form_knot(world-gen|season-tick)'` at `engine/mc_v18.py:204-205` instead of calling this function — see §7). Called only from unit tests: `engine/tests/test_knots_ed912.py:55` |
| `sustain_knot(knot_id, strain_delta, source, world)` | `systems/fieldwork/sim/knots.py:250 sustain_knot` | `systems/threadwork/sim/opposing.py:238` (inside `resolve_opposing_operations`, `systems/threadwork/sim/opposing.py:96`) — but `resolve_opposing_operations` itself has no caller anywhere in the tree (§7); also called directly by unit tests |
| `check_knot_rupture(knot_id, trigger, world)` | `systems/fieldwork/sim/knots.py:275 check_knot_rupture` | `—` in production; unit tests only (`engine/tests/test_knots_ed912.py:87`, `engine/tests/test_knots_ed912.py:91`, `engine/tests/test_knots_ed912.py:97`, `engine/tests/test_knots_ed912.py:100`) |
| `apply_knot_loss(actor, knot_id, mode, world)` | `systems/fieldwork/sim/knots.py:315 apply_knot_loss` | `—` in production; unit tests only (`engine/tests/test_knots_ed912.py:106`, `engine/tests/test_knots_ed912.py:112`, `engine/tests/test_knots_ed912.py:115`, `engine/tests/test_knots_ed912.py:121`) |
| `get_knot(knot_id, world)` | `systems/fieldwork/sim/knots.py:372 get_knot` | `—` (no caller found) |
| `get_active_knots(world)` | `systems/fieldwork/sim/knots.py:376 get_active_knots` | `—` (no caller found) |
| `reset_knots(world)` | `systems/fieldwork/sim/knots.py:380 reset_knots` | test helper only: `engine/tests/test_knots_ed912.py:43`, `engine/tests/test_knots_ed912.py:54` |
| `Knot.from_dict(d)` | `systems/fieldwork/sim/knots.py:131 from_dict` | `engine/autoload/game_state.py:396` (world-snapshot deserialization) |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `scene` (fieldwork scene object) | `arg` | `_resolve_slot`'s `ctx.get("scene")` | `engine/cross_scale/scene_dispatch.py:354` |
| `npc_id`, `prompt`, `world` | `arg` | `_resolve_slot`'s `ctx.get("npc_id")`/`ctx.get("prompt")`/`world` | `engine/cross_scale/scene_dispatch.py:356` |
| `actor_a`, `actor_b`, `actor_a_obj`, `actor_b_obj` | `arg` | caller-supplied duck-typed actors (`.bonds`, `.spirit`, `.history_relationships`, `.ts`, `.disposition_with_<other>`) | `systems/fieldwork/sim/knots.py:172-192 form_knot` |
| `world.knots` / module-level `_knots` fallback | `world-state` | `_store(world)` router | `systems/fieldwork/sim/knots.py:158-163 _store` |
| `world.rng` (fallback: fresh `random.Random()`) | `world-state` | `form_knot`'s rng resolution | `systems/fieldwork/sim/knots.py:217-220` |
| dice pool roll | `key` | `engine.autoload.dice_engine.roll_pool` | `systems/fieldwork/sim/knots.py:45 import`, `:222 roll_pool` call |
| `KNOT_DISPOSITION_MIN`, `KNOT_BONDS_MIN`, `KNOT_TS_MIN_PARTY`, `KNOT_FORMATION_TN`, `KNOT_FORMATION_OB` | `param` | module-level constants | `systems/fieldwork/sim/knots.py:51-58` |
| `knot_id`, `strain_delta`, `source`, `world` | `arg` | `resolve_opposing_operations`'s locals (`a_knot_id`/`b_knot_id`, `knot_strain_delta`) | `systems/threadwork/sim/opposing.py:236-246` |
| `world.knots` snapshot dict (on load) | `file` | save/load snapshot restore | `engine/autoload/game_state.py:394-396` |

## 3. Flow

- S1. `engine.cross_scale.scene_dispatch._resolve_slot` receives a `SceneSlot` whose
  `scene_type` is `"fieldwork"` or `"investigation"`. `engine/cross_scale/scene_dispatch.py:344` (elif st in ("fieldwork", "investigation"))
  - S1.1 `[branch]` `st == "fieldwork"` → calls `run_fieldwork_scene(ctx.get("scene"))`.
    `engine/cross_scale/scene_dispatch.py:353-354`
  - S1.2 `[branch]` `st == "investigation"` → calls
    `resolve_npe_response(ctx.get("npc_id"), ctx.get("prompt"), world)`.
    `engine/cross_scale/scene_dispatch.py:355-356`
  - S1.3 `[emit]` Both branches return a `StubResult` from `engine.substrate.stubwire.stub_resolve`
    (module `systems.fieldwork.sim.fieldwork` or `systems.fieldwork.sim.investigation`); the
    dispatcher copies `stub.reason`/`stub.stub` onto its own `out` dict and returns immediately —
    no further scene-phase steps (echo transport, zoom-out) run for this slot.
    `systems/fieldwork/sim/fieldwork.py:38-43`, `systems/fieldwork/sim/investigation.py:30-35`,
    `engine/cross_scale/scene_dispatch.py:357-359`
- S2. `form_knot` — `[gate]` prerequisite chain, each a short-circuit return of `None`:
  - S2.1 `[gate]` caller must supply both `actor_a_obj`/`actor_b_obj`. `systems/fieldwork/sim/knots.py:181-182`
  - S2.2 `[gate]` `actor_a_obj.bonds >= KNOT_BONDS_MIN`. `systems/fieldwork/sim/knots.py:184-186`
  - S2.3 `[gate]` disposition (via `disposition_with_<actor_b>` or fallback `.disposition`)
    `>= KNOT_DISPOSITION_MIN`. `systems/fieldwork/sim/knots.py:188-192`
  - S2.4 `[gate]` at least one actor's `.ts >= KNOT_TS_MIN_PARTY`. `systems/fieldwork/sim/knots.py:194-197`
  - S2.5 `[gate]` `_count_knots_for_actor(actor_a, world) < floor(bonds_a/2)+1`.
    `systems/fieldwork/sim/knots.py:199-202`, count helper `systems/fieldwork/sim/knots.py:166-169`
  - S2.6 `[gate]` no existing active Knot already links `actor_a`/`actor_b`.
    `systems/fieldwork/sim/knots.py:204-210`
  - S2.7 `[loop]`/`[gate]` formation roll via `roll_pool(pool, tn=KNOT_FORMATION_TN, rng=rng)`; net
    result branches to `TIER_CLOSE`, `TIER_DISTANT`, or `None` (partial/failure).
    `systems/fieldwork/sim/knots.py:212-233`
  - S2.8 `[write]` on success, construct `Knot(...)` with an incrementing id (`world.knot_id_counter`
    if present, else module-level `_knot_id_counter`) and insert into `_store(world)`.
    `systems/fieldwork/sim/knots.py:235-247`
- S3. `sustain_knot` — `[gate]` knot-id/active checks, then `[write]` strain update clamped to the
  tier's `TIER_RANGE`; `[branch]` `strain >= RUPTURE_STRAIN` sets `knot.active = False` (`broke`).
  `systems/fieldwork/sim/knots.py:250-272`
- S4. `check_knot_rupture` — `[gate]` knot-id/active/known-trigger checks; `[branch]` Close-tier
  knot at `<= TEMPERED_STRAIN` absorbs the trigger once (`[write]` reset strain to 0), else
  `[write]` deactivates the knot and logs a rupture. `systems/fieldwork/sim/knots.py:275-312`
- S5. `apply_knot_loss` — `[branch]` on `mode`:
  - S5.1 `mode == 'break'`: `[write]` sets `composure_damage`/`disposition_set_to` on the returned
    consequences dict; `[branch]` Close-tier knot with positive strain additionally late-imports
    `systems.characters.sim.conviction.apply_conviction_scar` and calls it (`[lateral]`, wrapped in
    `try/except (ImportError, AttributeError): pass`). `systems/fieldwork/sim/knots.py:338-354`
  - S5.2 `mode == 'rupture'`: `[write]` sets `disposition_set_to`/`coherence_delta`; late-imports
    `systems.threadwork.sim.coherence.apply_coherence_delta` and calls it (`[lateral]`, same
    try/except guard). `systems/fieldwork/sim/knots.py:356-367`
- S6. `resolve_opposing_operations` (peer module, not fieldwork's own entry point) — `[branch]` on
  `a_knot_id`/`b_knot_id` presence, `[lateral]` late-imports `sustain_knot` and calls it once per
  supplied knot id, wrapped in `try/except (ImportError, AttributeError): pass`.
  `systems/threadwork/sim/opposing.py:236-249`. This step is unreachable in practice — see §7.

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `StubResult(module, io_contract, reason, stub=True)` | `key`-shaped no-op | `engine.cross_scale.scene_dispatch._resolve_slot`'s `out["reason"]`/`out["stub"]` | `systems/fieldwork/sim/fieldwork.py:39-43`, `engine/cross_scale/scene_dispatch.py:357-358` |
| `Knot | None` | `world-state` (inserted into `_store(world)`) | `_store(world)` (either `world.knots` or the module-level `_knots` dict) | `systems/fieldwork/sim/knots.py:246-247` |
| `KnotState(knot, broke, ruptured, strain_after, notes)` | `arg` return value | caller of `sustain_knot`/`check_knot_rupture` (only live caller: `opposing.py`, itself orphaned — §7) | `systems/fieldwork/sim/knots.py:250-272`, `:275-312` |
| consequences `dict` (`composure_damage`, `coherence_delta`, `disposition_set_to`, `wound`, `conviction_scar`) | `arg` return value | caller of `apply_knot_loss` (no live caller found — §7) | `systems/fieldwork/sim/knots.py:327-336` |
| `apply_conviction_scar(...)` call | `lateral` | `systems.characters.sim.conviction` | `systems/fieldwork/sim/knots.py:348-352` |
| `apply_coherence_delta(...)` call | `lateral` | `systems.threadwork.sim.coherence` | `systems/fieldwork/sim/knots.py:363-364` |
| `world.knots[k].to_dict()` | `world-state` (serialized) | save-snapshot writer | `engine/autoload/game_state.py:313-314` |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| `world.knots` (dict `knot_id -> Knot`) | RW | `engine.autoload.game_state` (`World` dataclass field); read/written by `systems.fieldwork.sim.knots` via `_store(world)` | field decl `engine/autoload/game_state.py:196`; router `systems/fieldwork/sim/knots.py:158-163` |
| `world.knot_id_counter` | RW | `engine.autoload.game_state` field; incremented in `form_knot` | field decl `engine/autoload/game_state.py:197`; increment `systems/fieldwork/sim/knots.py:236-238` |
| module-level `_knots` dict (fallback store, no `world` supplied) | RW | `systems.fieldwork.sim.knots` | `systems/fieldwork/sim/knots.py:154` |
| module-level `_knot_id_counter` (fallback counter) | RW | `systems.fieldwork.sim.knots` | `systems/fieldwork/sim/knots.py:155` |
| `Knot.strain`, `.active`, `.log` | W | `systems.fieldwork.sim.knots` (`sustain_knot`, `check_knot_rupture`) | `systems/fieldwork/sim/knots.py:265-271`, `:302-309` |
| `Knot.disposition` | W | `systems.fieldwork.sim.knots` (`form_knot`; set once at construction, never mutated after formation) | `systems/fieldwork/sim/knots.py:241-243 form_knot` |
| `engine.substrate.stubwire.invocations` (module-level counter) | W | `stub_resolve`, incremented on every fieldwork/investigation entry-point call | `engine/substrate/stubwire.py` (`stub_resolve`); call sites `systems/fieldwork/sim/fieldwork.py:39`, `systems/fieldwork/sim/fieldwork.py:47`, `systems/fieldwork/sim/fieldwork.py:55`, `systems/fieldwork/sim/investigation.py:31`, `systems/fieldwork/sim/investigation.py:39`, `systems/fieldwork/sim/investigation.py:47` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| `up` | `engine.cross_scale.scene_dispatch` | scene-type dispatch calls `run_fieldwork_scene`/`resolve_npe_response` (stub-wired) | `engine/cross_scale/scene_dispatch.py:344-359` |
| `up` | `engine.autoload.scene_slate` | declares `"fieldwork"` as an example `scene_type` string on `SceneSlot`; no production `queue_scene("fieldwork", ...)` call site exists (§7) | `engine/autoload/scene_slate.py:26`, `engine/autoload/scene_slate.py:34` |
| `up` | `engine.mc_v18` | season loop records a `stub_resolve` marker literally named `form_knot(world-gen|season-tick)` in place of calling `form_knot` | `engine/mc_v18.py:204-209` |
| `up` | `engine.autoload.game_state` | `World.knots`/`World.knot_id_counter` fields own the state `_store(world)` reads/writes; `Knot.from_dict` used on snapshot restore | `engine/autoload/game_state.py:196-197`, `engine/autoload/game_state.py:313-314`, `engine/autoload/game_state.py:394-397` |
| `lateral` | `engine.autoload.dice_engine` | `roll_pool` drives the §3.2 formation roll | `systems/fieldwork/sim/knots.py:45`, `systems/fieldwork/sim/knots.py:222` |
| `lateral` | `systems.threadwork.sim.opposing` | `resolve_opposing_operations` calls `sustain_knot` when knot ids are supplied (module itself orphaned — §7) | `systems/threadwork/sim/opposing.py:236-249` |
| `lateral` | `systems.threadwork.sim.coherence` | `apply_knot_loss` late-imports `apply_coherence_delta` on rupture | `systems/fieldwork/sim/knots.py:362-364` |
| `lateral` | `systems.characters.sim.conviction` | `apply_knot_loss` late-imports `apply_conviction_scar` on a high-strain Close break | `systems/fieldwork/sim/knots.py:346-352` |
| `down` | `engine.substrate.stubwire` | sole constructor for the stub-wired return values in `fieldwork.py`/`investigation.py` | `systems/fieldwork/sim/fieldwork.py:22`, `systems/fieldwork/sim/fieldwork.py:38-59`, `systems/fieldwork/sim/investigation.py:20`, `systems/fieldwork/sim/investigation.py:30-51` |

## 7. Traced gaps

| Gap | Evidence anchor |
|---|---|
| `run_fieldwork_scene`/`advance_disposition`/`advance_evidence` (fieldwork.py) and `resolve_npe_response`/`evaluate_dialogue_lattice`/`apply_response_matrix` (investigation.py) are all typed no-op stubs — every call returns `stubwire.StubResult`, never real behavior. | `systems/fieldwork/sim/fieldwork.py:38-59`, `systems/fieldwork/sim/investigation.py:30-51` |
| No production code path ever queues a `scene_type="fieldwork"` or `"investigation"` scene. `queue_triggered_scenes` (the sole caller of `scene_slate.queue_scene` in the whole tree — verified by grep, only call site) only ever fires `scene_type="contest"` for the "Stability Crisis" trigger; the other 7 canonical §4.3.2 triggers are explicitly deferred, not fabricated. The `("fieldwork", {})`/`("investigation", {})` branches in `_resolve_slot` are exercised only by a test that manually constructs a `SceneSlot` and calls `_resolve_slot` directly, bypassing `queue_triggered_scenes`/`evaluate_triggers` entirely — its own docstring states "today only 'contest' is ever organically queued, via Stability Crisis". | `engine/cross_scale/scene_dispatch.py:75-106` (`evaluate_triggers`/`queue_triggered_scenes`, only "Stability Crisis" → `scene_type: "contest"`); sole `queue_scene` call site `engine/cross_scale/scene_dispatch.py:105`; grep confirms no other `queue_scene(` call exists in `engine/`, `systems/`, `tests/`; test admission `engine/tests/test_pipeline_reach.py:283-298` |
| `form_knot` has NO auto-call anywhere in the season/campaign loop. `engine/mc_v18.py` deliberately records a `stubwire.stub_resolve` call under the literal string `'form_knot(world-gen|season-tick)'` as an "honest deferral" marker — this is not a call to `systems.fieldwork.sim.knots.form_knot`, just a stand-in name; `form_knot` itself is never imported by `engine/mc_v18.py` (grep confirms no `from systems.fieldwork.sim.knots import` or `knots.form_knot` in that file). `world.knots` is asserted to stay empty after a full seeded campaign. `form_knot`'s only real callers anywhere are unit tests. | `engine/mc_v18.py:196-209` (comment + `stub_resolve` call); `engine/tests/test_world_population.py:157-163` (`test_knots_stay_unpopulated_honest_deferral`, asserts `r.final_state.get('knots', {}) == {}`); only real caller `engine/tests/test_knots_ed912.py:55` |
| `systems.threadwork.sim.opposing.resolve_opposing_operations` — the only non-test caller of `sustain_knot` — is itself unreachable: grep across `engine/`, `systems/`, `tests/` finds no import of `systems.threadwork.sim.opposing` or call to `resolve_opposing_operations` anywhere outside its own file, and `tests/valoria/test_oi12_orphan_census.py` independently lists `systems/threadwork/sim/opposing.py` in its `_OI12_VERIFIED_ORPHAN_NO_CALLSITE` tuple (cross-checked against `structure_audit`'s import graph). So the knot-strain-on-opposing-operations path is dead on both ends: unreachable caller, real callee. | `systems/threadwork/sim/opposing.py:96 resolve_opposing_operations`, `:236-249` (the `sustain_knot` call); grep found zero external references; `tests/valoria/test_oi12_orphan_census.py:49` |
| `advance_disposition`, `advance_evidence` (fieldwork.py), `evaluate_dialogue_lattice`, `apply_response_matrix` (investigation.py), and `get_knot`, `get_active_knots` (knots.py) have no caller anywhere in `engine/`, `systems/`, or `tests/` — not even from a test. | grep of each symbol name across the repo returned only its own definition line in every case (see §1 rows) |
| `module_contracts.yaml` declares a contract only for `fieldwork_knots`; `fieldwork.py`'s own module docstring states this explicitly and cites its "Entry points" docstring block as the substitute io_contract source (no registry entry backs it). `investigation.py` has no contract entry either. | `references/module_contracts.yaml:373` (only `fieldwork_knots` row; grep for `module: fieldwork`/`module: investigation` finds nothing else); `systems/fieldwork/sim/fieldwork.py:29-35` |
| `RUPTURE_COHERENCE_LOSS` (the Coherence-on-rupture constant `apply_knot_loss` applies) is flagged `[UNVERIFIED post-ED-912]` in-code — retained provisionally, not a settled canonical value. Structural (not mechanical) implication: the `apply_knot_loss` → `apply_coherence_delta` lateral edge fires on a value the code itself marks unverified. | `systems/fieldwork/sim/knots.py:91-94`, `systems/fieldwork/sim/knots.py:360-361` |
| `RUPTURE_WOUND_DISSOLUTION` (declared for the FR-Dissolution rupture Wound consequence) is never referenced outside its own declaration. `apply_knot_loss`'s signature takes no `trigger` parameter that could condition Wound application, and the consequences dict's `'wound'` key is initialized to 0 and never reassigned in either the `'break'` or `'rupture'` branch — the FR-Dissolution Wound consequence is structurally unreachable. | declaration `systems/fieldwork/sim/knots.py:96`; signature `systems/fieldwork/sim/knots.py:315-316 apply_knot_loss`; unreassigned `'wound'` init `systems/fieldwork/sim/knots.py:334` |
| `COHERENCE_BAND_STRAIN_PACING` (a passive strain-accrual table) is declared and never read anywhere in the repo. | `systems/fieldwork/sim/knots.py:100-106` |
| **`apply_knot_loss` applies only 2 of its 4 declared consequence fields; the other 2 are written into the returned dict and applied to no actor object anywhere in the function.** The docstring claims the function "routes through coherence + conviction modules" — true for `coherence_delta` (routed to `threadwork.coherence.apply_coherence_delta`) and `conviction_scar` (routed to `characters.conviction.apply_conviction_scar` on a Close-tier positive-strain break), but `composure_damage` and `disposition_set_to` are set only on the local `consequences` dict, never written to `actor` or any object. Per this file's own §7 rows above, there is no production caller either — so both the routed and unrouted fields are currently unreachable in practice, but the asymmetry is a distinct, sharper defect than "no caller": even a hypothetical caller could not apply `composure_damage`/`disposition_set_to` without doing so itself outside this function. | docstring claim `systems/fieldwork/sim/knots.py:320`; `composure_damage` write-only `systems/fieldwork/sim/knots.py:340`; `disposition_set_to` write-only (break) `systems/fieldwork/sim/knots.py:342`, (rupture) `systems/fieldwork/sim/knots.py:359`; `conviction_scar` routed `systems/fieldwork/sim/knots.py:348-352`; `coherence_delta` routed `systems/fieldwork/sim/knots.py:363-365` |
