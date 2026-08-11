# Code-spine trace — engine/substrate, engine/cross_scale, engine/autoload, engine/mc_v18.py, systems/overview/sim

Method: every .py file in scope read whole with the Read tool, no grep/rg used. Independent
re-derivation; no `*_flow_skeleton_v1.md` opened.

## Files read (24 total)
- engine/substrate/__init__.py, canon_buckets.py, keys.py, stubwire.py
- engine/autoload/__init__.py, dice_engine.py, game_state.py, npc_ai.py, scene_slate.py,
  season_manager.py, sigma_leverage.py, victory.py
- engine/cross_scale/__init__.py, articulation.py, combat_bridge.py, domain_echo.py,
  echo_transport.py, handoff_rules.py, parliamentary_bridge.py, scene_dispatch.py, zoom_in_out.py
- engine/mc_v18.py
- systems/overview/sim/__init__.py, accounting.py, ci_track.py, ip_track.py, ms_track.py,
  rs_track.py, season.py

---

## 1. Campaign execution order (run_campaign, season by season)

`run_campaign(seed, max_seasons, params)` — engine/mc_v18.py:212-308

1. `game_state.create_world(seed)` (mc_v18.py:224) → `game_state.py:212-259`:
   builds Faction/Territory dicts from STARTING_* tables, seeds `world.clocks`
   (`CI=30.0, MS=60.0, IP=20.0, PI=0.0, Strain=0.0, Turmoil=0.0` — game_state.py:244),
   then late-imports `systems.settlements.sim.registry.populate_from_geography(world)`
   (game_state.py:257-258, out of scope but the call site is in scope).
2. `victory.reset()` (mc_v18.py:225) — clears the module-level `_qualifying_streak` dict.
3. `scene_slate.clear()` (mc_v18.py:226) — empties the module-level scene queue.
4. `effective_params = DEFAULT_PARAMS` merged with caller `params` (mc_v18.py:228-231).
5. `world.dispatch_combat_bridge = _dispatch_combat_bridge_on(effective_params)` (mc_v18.py:237) —
   default OFF (mc_v18.py:70-81, env var default `'0'`).
6. If `_echo_transport_on(effective_params)` (default ON, mc_v18.py:57-67, env var default `'1'`):
   build `world.echo_scheduler = echo_transport.make_scheduler(...)` (mc_v18.py:241-248),
   `world.key_log = world.echo_scheduler.log`, `world._echo_key_seq = 0`, then
   `articulation.subscribe_all(world.echo_scheduler)` (mc_v18.py:257-258) — registers 13
   stub-wire trigger callbacks (articulation.py:116-130, 152-170).
7. **Season loop**, up to `max_s` iterations, breaking early if `world.winner` is set
   (mc_v18.py:260-274). Each iteration is `run_season(world, action_callback=_faction_actions_callback)`
   (systems/overview/sim/season.py:48-78), which composes exactly 3 steps in order:
   1. **`season_manager.advance_season(world)`** (season.py:69 → season_manager.py:31-43):
      `world.season += 1`; if `season % 4 == 1` it's a new arc → `world.arc += 1` and every
      faction's `reset_arc()` runs (clears `council_used_this_arc`,
      `parl_transfer_used_this_arc`); every faction's `reset_seasonal()` always runs
      (clears `senator_inward_used`, `consul_used`).
   2. **`action_callback(world)` = `_faction_actions_callback`** (mc_v18.py:116-209):
      a. For each faction that is `parliamentary` AND holds `≥1` territory:
         `faction_take_action(faction, world, world.rng)` (out-of-scope module), errors caught
         and printed to stderr, never re-raised (mc_v18.py:124-136).
      b. `scene_dispatch.run_scene_phase(world, world.rng)` (mc_v18.py:141) →
         `queue_triggered_scenes` (only the **Stability Crisis** trigger,
         `Faction.Sta <= 2` → emergency-council contest, is field-evaluable —
         scene_dispatch.py:75-99) then `dispatch_scenes` (drains scene_slate,
         resolves each queued scene, runs echo_transport + zoom_out).
         `world.scenes_resolved` incremented by the resolved count (mc_v18.py:142).
      c. If `world.echo_scheduler` is set: `parliamentary_bridge.run_parliamentary_scene(world, world.rng)`
         (mc_v18.py:148-152) — derives a two-pole §10 vote every season from aggregate state
         (lowest-Stability proposer vs highest-Mandate establishment,
         parliamentary_bridge.py:82-97), runs it, composes a winner Domain Echo, and
         independently attempts the OI-04 CB-gated territory-transfer motion
         (parliamentary_bridge.py:165-177, 215-217) regardless of vote outcome.
      d. If `world.echo_scheduler` is set: `sched.accounting_boundary()` then `sched.next_tick()`
         (mc_v18.py:158-161) — runs every OF-7 deferred `apply` queued this season, in
         emission order, then resets the per-tick counter.
      e. Two `stubwire.stub_resolve` no-op calls, self-documented as deliberate non-fabrication:
         `generate_npc(world-gen|season-tick)` (mc_v18.py:186-194) and
         `form_knot(world-gen|season-tick)` (mc_v18.py:204-209) — neither is ever wired to a
         real generator anywhere in the traced spine.
   3. **`accounting.run_accounting(world)`** (season.py:72 → accounting.py:95-142), in this
      fixed order:
      1. `apply_seasonal_ci(world)` (accounting.py:112) — PP-412 5-step CI calc, every season.
      2. `if world.season > 0 and world.season % 4 == 0: apply_ms_baseline_decay(world)`
         (accounting.py:116-117) — Year-End only.
      3. `check_insurgency_triggers(world)` (accounting.py:124) — GD-3 emergence, every season.
      4. `for each insurgency: check_insurgency_promotion(...)` (accounting.py:131-132).
      5. `simulate_npc_actions(world)` (accounting.py:138) — NPE stance drift, every season.
      6. `_probe_province_accord_drift(world)` (accounting.py:142) — report-only telemetry,
         never writes state, runs last.
   - After the 3 steps, `victory.check_all_factions(world)` (mc_v18.py:270-274): first
     faction whose `check_peninsular_sovereignty` returns `won=True` sets `world.winner` and
     breaks the season loop.
8. If no `world.winner` after the loop: fallback winner by
   `held*10 + faction.L + len(territories)` among parliamentary factions (mc_v18.py:277-286).
9. `surviving = count of factions with >=1 territory` (mc_v18.py:288).
10. `CampaignResult` built, including `game_state.serialize_world(world)` (mc_v18.py:292-308).

---

## 2. Single Key-substrate mutation path (in order)

(engine/substrate/keys.py TickScheduler/KeyLog, exercised via engine/cross_scale/echo_transport.py
and engine/cross_scale/parliamentary_bridge.py)

1. Caller constructs a `Key(...)` dataclass (fields: id, type, emitted_at, causes, targets,
   scale_signature, symbolic_dimensions, visibility, time_horizon, permanence, payload) —
   e.g. echo_transport.py:309-323, echo_transport.py:416-428.
2. Caller calls `sched.emit(key, apply=callable)` (keys.py:510-523) — root emission at
   `cascade_depth=0`. (A callback reacting to an already-emitted Key inside a drain must instead
   call `schedule_emission`, keys.py:525-536 — B1/OF-B1 no-sync-reentry guard, keys.py:518-522,
   raises `TerminationBreach` if violated. Nothing in the traced spine actually exercises
   `schedule_emission` — no subscriber callback in scope ever emits a new Key; every
   `_TRIGGER_TYPE_IDS` callback in articulation.py is a stub-wire no-op that returns immediately,
   articulation.py:140-149.)
3. `_emit_at_depth` (keys.py:555-578): checks `cascade_depth_max` and `emissions_per_tick_max`
   caps, raising `TerminationBreach` if either is exceeded (keys.py:556-565).
4. `self.log.registry.apply_defaults(key)` (keys.py:566 → keys.py:322-333) — fills
   `scale_signature` / `permanence` / `time_horizon` defaults from the type registry entry when
   the emitter left them at dataclass defaults.
5. `self.log.append(key)` (keys.py:567 → keys.py:367-376): runs `_validate` (the 8 §2.3
   invariants, keys.py:378-434 — duplicate id, payload contract, causes-exist, season
   monotonicity, canonical axes, canonical scales, exactly-one-visibility-shape, valid
   time_horizon/permanence), then assigns `sub_step_index` as this season's next append-order
   counter (keys.py:371-373, SSI-1), records `id -> index`, and appends to `_entries`.
6. `_emitted_this_tick += 1` (keys.py:568).
7. If `apply` was supplied: under OF-7 (`defer_apply=True`, the ratified default) while phase is
   `ACTION`, the `(key.id, apply)` pair is queued into `_pending_apply` (keys.py:569-571) rather
   than applied now. (`defer_apply=False` or phase already `ACCOUNTING_BOUNDARY` would apply
   immediately, keys.py:572-573 — not exercised anywhere in the traced spine; every scheduler in
   scope is built via `echo_transport.make_scheduler`, which never overrides `defer_apply`.)
8. Synchronous subscriber notify (§4.1 step 5 subset): `for callback in
   self.subscriptions.get(key.type, []): callback(key, self)` (keys.py:576-577) — this is where
   articulation's 13 stub-wire trigger callbacks fire, when the emitted `key.type` matches one of
   `_TRIGGER_TYPE_IDS` (articulation.py:116-130).
9. Later the same season, `mc_v18._faction_actions_callback` calls
   `world.echo_scheduler.accounting_boundary()` (mc_v18.py:160 → keys.py:581-591): phase flips to
   `ACCOUNTING_BOUNDARY`, then every queued `(key_id, apply)` pair runs, in emission order,
   `apply(self.log.lookup(key_id))` — this is where the actual Faction.adjust / Settlement.order
   mutation happens (e.g. echo_transport.py:430-436, echo_transport.py:325-341).
10. `world.echo_scheduler.next_tick()` (mc_v18.py:161 → keys.py:593-601): resets
    `_emitted_this_tick` to 0 and phase back to `ACTION`; raises `TerminationBreach` if the queue
    is non-empty (should never happen — `drain_tick` is the only other queue-drain path and
    nothing in the traced spine calls `schedule_emission`/`drain_tick` at all).

Two live producers of step 1-2 exist in the traced spine:
- `echo_transport.emit_scene_echo` (echo_transport.py:360-455), called from
  `scene_dispatch._resolve_slot` (scene_dispatch.py:390-393) — fires only when `ctx['echo']` is
  populated. The only live populator in the traced spine is the **emergency_council** contest
  branch (scene_dispatch.py:334-343), reachable only via the Stability Crisis trigger.
- `parliamentary_bridge.run_parliamentary_scene` → `echo_transport.emit_scene_echo("contest", ...)`
  (parliamentary_bridge.py:207-213) — runs unconditionally every season once `echo_scheduler` is
  attached, whenever the vote resolves with a winner and degree in
  `{"Overwhelming","Success"}`.

---

## 3. Per-module entry points vs. what's actually called (in scope)

| Module | Declared entry points | Called from something else in scope? |
|---|---|---|
| substrate/keys.py | Key, KeyLog, TickScheduler, TypeRegistry | Yes — via echo_transport (make_scheduler, emit) |
| substrate/canon_buckets.py | canonical_accord | Yes — game_state.py:33 re-export; accounting.py:41,88 |
| substrate/stubwire.py | stub_resolve, reset_invocations | Yes — widely (npc_ai, rs_track, ip_track, articulation, scene_dispatch, mc_v18) |
| autoload/game_state.py | create_world, serialize_world, restore_world | Yes — mc_v18.py:224,307 |
| autoload/season_manager.py | advance_season, check_arc_boundary | advance_season: yes (season.py:69). **check_arc_boundary: NOT called anywhere in scope** (season.py re-derives the same `% 4 == 1` test itself only indirectly via advance_season; check_arc_boundary is a pure orphan within this spine). |
| autoload/dice_engine.py | roll_pool, continuous_engine_sample, degree_from_net | **NOT called anywhere in scope.** Only consumer in scope is sigma_leverage.py (itself unreached — see below). |
| autoload/npc_ai.py | select_action, evaluate_priority_stack | **NOT called anywhere in scope.** Both bodies are unconditional stub-wire no-ops (npc_ai.py:33-46) regardless. mc_v18's faction dispatch goes through `systems.factions.sim.faction_action.faction_take_action` (out of scope), never through this module, despite this module's own docstring naming faction_action as a dependency (npc_ai.py:10) — the dependency direction implied by the docstring does not match any call found. |
| autoload/scene_slate.py | queue_scene, next_scene, clear, pending_count | Yes — scene_dispatch.py (queue_scene, next_scene, pending_count); mc_v18.py:226 (clear) |
| autoload/sigma_leverage.py | sigma_n, soft_cap, eff_ob, net_boost, p_success, roll_net, degree, etc. | **NOT called anywhere in scope.** A fully-built module (312 lines) with zero callers within substrate/cross_scale/autoload/mc_v18/overview-sim. |
| autoload/victory.py | check_peninsular_sovereignty, check_all_factions, reset | Yes — mc_v18.py:225,270 |
| cross_scale/domain_echo.py | compute_domain_echo, compute_accord_echo, compute_thread_echo | compute_domain_echo, compute_accord_echo: yes (echo_transport.py:409,450). **compute_thread_echo: NOT called anywhere in scope** — a fully-implemented §5.6 Thread Echo rule table (domain_echo.py:186-216) with zero callers. |
| cross_scale/echo_transport.py | make_scheduler, emit_scene_echo, classify_scene_outcome | Yes — mc_v18.py:243 (make_scheduler); scene_dispatch.py:392, parliamentary_bridge.py:212 (emit_scene_echo) |
| cross_scale/scene_dispatch.py | evaluate_triggers, queue_triggered_scenes, dispatch_scenes, run_scene_phase | Yes — mc_v18.py:141 (run_scene_phase, which composes the rest) |
| cross_scale/handoff_rules.py | apply_handoff | Yes — scene_dispatch.py:188 (via `_handoff_validity_check_pair`), for `(Scene,Faction)` only (the only pair scene_dispatch derives — scene_dispatch.py:157-160). 6 of the 8 §3.x rules (`§3.1,§3.2,§3.3,§3.5,§3.6,§3.7,§3.8` — everything except `§3.4 Scene→Faction`) are **never reached with a matching key from anything in the traced spine.** |
| cross_scale/zoom_in_out.py | zoom_in, zoom_out, check_mandatory_triggers | zoom_in, zoom_out: yes (scene_dispatch.py:219,396). check_mandatory_triggers: yes (scene_dispatch.py:97, filtered down to non-"Stability Crisis" names only, which are then just reported as `deferred` and never acted on further). |
| cross_scale/articulation.py | render_protagonist_lens, evaluate_articulation_triggers, generate_chronicle_entry, subscribe_all | subscribe_all: yes (mc_v18.py:258). **render_protagonist_lens and evaluate_articulation_triggers are NOT called anywhere in scope** (generate_chronicle_entry likewise not called; all three are unconditional stub-wire no-ops regardless, articulation.py:35-59). |
| cross_scale/combat_bridge.py | derive_parties, resolve | Yes, but only reachable when `world.dispatch_combat_bridge` is True (default False, mc_v18.py:81) **AND** a `combat` scene is queued — and **nothing in the traced spine ever calls `queue_scene("combat", ...)`** (scene_dispatch.evaluate_triggers only ever fires the Stability Crisis **contest**, scene_dispatch.py:80-95). So combat_bridge is dead in every seeded campaign today, doubly so. |
| cross_scale/parliamentary_bridge.py | run_parliamentary_scene | Yes — mc_v18.py:150 (unconditional every season once echo_scheduler attached) |
| overview/sim/season.py | run_season | Yes — mc_v18.py:267 |
| overview/sim/accounting.py | run_accounting | Yes — season.py:72 |
| overview/sim/ci_track.py | compute_seasonal_ci_delta, apply_ci_delta, apply_seasonal_ci | apply_seasonal_ci: yes (accounting.py:112). compute_seasonal_ci_delta, apply_ci_delta are its own internal helpers (called by apply_seasonal_ci itself, ci_track.py:186-187) — no external caller of the two lower-level functions exists in scope. |
| overview/sim/ms_track.py | apply_ms_baseline_decay, apply_ms_delta | apply_ms_baseline_decay: yes (accounting.py:117). **apply_ms_delta: NOT called anywhere in scope** ("Thread operation / Restoration source" callers are out-of-scope or nonexistent). |
| overview/sim/rs_track.py | apply_rs_delta | Called once, from echo_transport.py:355 — but only on the §5.5 Accord-Echo "violence" leg, which (per echo_transport's own docstring, echo_transport.py:157-162) has **zero live producers** setting `echo['scene_outcome']=='violence'` anywhere in the traced spine — so this call site is present but organically unreached in any seeded campaign. The function itself is an unconditional stub-wire no-op regardless (rs_track.py:28-33). |
| overview/sim/ip_track.py | apply_ip_delta, check_phased_occupation_threshold | **NEITHER function is called anywhere in scope.** `world.clocks['IP']` is seeded at world creation (game_state.py:244) but nothing in the traced spine ever reads or writes it afterward — a fully dead world-track end to end within this scope. |

---

## 4. Declared-but-doesn't-happen (stubs / no-ops / dead flags / dead constants / stale comments)

1. **engine/autoload/npc_ai.py:33-46** — `select_action` and `evaluate_priority_stack` are
   unconditional stub-wire no-ops (never real logic), AND (per §3 table above) neither function
   is called by anything else read in this scope — a doubly-dead module relative to its own
   docstring's claimed dependency on `systems/factions/sim/faction_action` (npc_ai.py:10), which
   in the traced spine is the *actual* faction-dispatch caller (mc_v18.py:130) that bypasses
   npc_ai entirely.

2. **systems/overview/sim/ip_track.py:29-42** — both `apply_ip_delta` and
   `check_phased_occupation_threshold` are unconditional stub-wire no-ops, and (§3 table) neither
   is called anywhere in the traced spine, even though `world.clocks['IP']` is explicitly seeded
   to 20.0 at world creation (game_state.py:238-244, with an inline comment "Currently unread by
   live code (peninsular_strain is unbuilt)" — i.e. the code itself documents its own deadness).

3. **systems/overview/sim/ms_track.py:19-25** — the module's own docstring still asserts:
   `[DRIFT: accounting._ms_decay (sim/peninsular/accounting.py L36-39) ALSO implements PP-255
   baseline decay inline ... Migration ... is out of Tier 0 scope]`. Reading `accounting.py`
   whole (this pass) shows **no such inline function exists**: `accounting.py` imports
   `apply_ms_baseline_decay` directly from this very module (accounting.py:43) and calls it once,
   gated on year-end cadence (accounting.py:116-117) — there is no `_ms_decay` anywhere in
   accounting.py. This is the exact same defect class that `ci_track.py:18-33` explicitly
   documents having been corrected for CI on 2026-08-04 ("this note is kept as a corrected record
   because it was twice read as current state") — but `ms_track.py`'s sibling claim about MS was
   never similarly corrected. A comment contradicting the code it describes (in a sibling file),
   left stale.

4. **engine/mc_v18.py:42-53** — `DEFAULT_PARAMS['VICTORY_THRESHOLD'] = 11` is a parameter dict
   entry accepted and never read: the live gate is `engine/autoload/victory.py:27`'s own
   module-level `VICTORY_THRESHOLD = 15`, used directly at `victory.py:70`
   (`territory_count_ok = held >= VICTORY_THRESHOLD`) — the dict value never reaches it. The
   comment self-documents this and cites a tripwire test that asserts the value is unwired.
   Genuinely a declared-dead constant, verified dead by reading `victory.py` in full.

5. **engine/mc_v18.py:186-209** — two `stubwire.stub_resolve` calls every season declare that
   `generate_npc` and `form_knot` are NOT auto-invoked (by design, citing a no-fabrication
   rationale). Consequence, confirmed by reading `game_state.py`'s `World` dataclass
   (`knots: dict = field(default_factory=dict)`, game_state.py:196) and this trace: **nothing in
   the traced spine ever populates `world.knots`** — it stays permanently empty for the life of
   any campaign that only exercises this scope. (`world.npc_counter`/`world.npcs` CAN move via
   `simulate_npc_actions`'s drift half, accounting.py:138, but never via generation within scope.)

5b (surprise, not a stub). **engine/cross_scale/combat_bridge.py is unreachable from any seeded
   campaign today for TWO independent reasons simultaneously**: (a) `DISPATCH_COMBAT_BRIDGE`
   defaults OFF (mc_v18.py:70-81), and (b) even with the flag ON, nothing in the traced spine
   ever calls `queue_scene("combat", ...)` — `scene_dispatch.evaluate_triggers` (scene_dispatch.py:75-99)
   only ever fires the Stability Crisis trigger, which queues a **contest**, never a combat scene.
   `combat_bridge.py`'s own docstring (line 37-38) already asserts the second fact ("verified: no
   `queue_scene("combat", ...)` call site exists anywhere in the tree") — confirmed independently
   by reading the whole spine, not by trusting that assertion.

---

## 5. Surprises

- The whole Key/Echo substrate (engine/substrate/keys.py) — the most heavily-engineered,
  most-commented file in scope — has exactly **two live producers** reachable in any seeded
  campaign: the emergency-council contest branch of scene_dispatch (gated on the single evaluable
  Stability Crisis trigger) and parliamentary_bridge's per-season vote. Every other declared Key
  producer path in scope (combat's echo block, the §5.5 "violence"/"territorial_transfer"/
  "governance"/"destabilisation" Accord-Echo legs other than what an emergency-council/vote
  outcome can classify) is wired but organically dormant, confirmed by echo_transport.py's own
  extensive dormancy documentation and independently re-derived here by tracing every caller.
- `TickScheduler.schedule_emission` / `drain_tick` (the B1 re-entrant, cascade-depth>0 path,
  keys.py:525-553) are never exercised by anything in the traced spine — every emission in scope
  is a root emission (`cascade_depth=0`) via `sched.emit`. The re-entrancy guard machinery is
  fully built and fully unreached within this scope.
- `engine/autoload/dice_engine.py` and `engine/autoload/sigma_leverage.py` are two complete,
  clean, well-tested-looking root primitives (roll_pool, continuous_engine_sample, soft_cap,
  p_success, etc.) with **zero callers anywhere in this entire scope** — not stubs, just
  unreached from this vantage point (presumably consumed by combat/contest resolvers outside
  scope, e.g. systems/social_contest, systems/combat — neither read in this pass).
- `domain_echo.compute_thread_echo` (§5.6 Thread Echo, a fully-implemented rule table,
  domain_echo.py:186-216) has no caller anywhere in scope — the Thread scale-transition leg of
  the cross-scale architecture is entirely unwired from the campaign loop as traced here.
- Of the 8 canonical §3.x handoff rules in handoff_rules.py, only `§3.4 Scene→Faction` is ever
  actually looked up with a live `(from_scale, to_scale)` pair by anything in scope
  (scene_dispatch.py:157-160) — the other 7 rules are fully implemented, dispatchable, and
  reachable in principle via `apply_handoff` directly, but nothing in the traced call graph ever
  constructs a call with their scale pairs.
