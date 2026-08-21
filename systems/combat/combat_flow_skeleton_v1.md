# Combat — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/combat/` · **Lane:** `PC` · **Contracts:** `personal_combat`
**Code roots traced:** `systems/combat/combat_engine_v1/{wrapper,combat_systems,core,combatant,config,contact,tradition,traditions,ability_primitives,weapons,weapon_physics,geometry,vocabulary,capabilities,state_graph}.py`, `systems/combat/combat_engine_v1/workbench/{balance,server,trace,armour_participation,build_levers}.py`, `systems/combat/sim/combat.py`, `engine/cross_scale/combat_bridge.py`, `engine/cross_scale/scene_dispatch.py`, `engine/mc_v18.py`, `engine/cross_scale/echo_transport.py`
**Traced at:** `6545067`

## 1. Entry points

| Callable | Anchor | Called by |
|---|---|---|
| `wrapper.fight(A, B, cfg=None, rng=None, max_bouts=12) -> int` | `systems/combat/combat_engine_v1/wrapper.py:465 fight` | `engine/cross_scale/combat_bridge.py:141 resolve` (campaign seam, flag-gated — §7); `systems/combat/combat_engine_v1/workbench/balance.py:65`, `systems/combat/combat_engine_v1/workbench/server.py:77`, `systems/combat/combat_engine_v1/workbench/trace.py:23`, `systems/combat/combat_engine_v1/workbench/armour_participation.py:78`, `systems/combat/combat_engine_v1/workbench/armour_participation.py:145`, `systems/combat/combat_engine_v1/workbench/build_levers.py:73` (offline balance/trace harnesses, CLI-invoked); `tests/valoria/test_combat_invariants.py` |
| `wrapper.engagement(A, B, first, cfg, rng, prev_closed=False)` | `systems/combat/combat_engine_v1/wrapper.py:47 engagement` | `wrapper.fight:480` only — internal, not an outside-callable entry |
| `combat_bridge.derive_parties(ctx, world)` | `engine/cross_scale/combat_bridge.py:114 derive_parties` | `engine/cross_scale/scene_dispatch.py:234 derive_parties` |
| `combat_bridge.resolve(a, b, rng)` | `engine/cross_scale/combat_bridge.py:131 resolve` | `engine/cross_scale/scene_dispatch.py:238 resolve` |
| `systems.combat.sim.combat.resolve_combat_round(participants, scene=None, rng=None)` (DEPRECATED engine) | `systems/combat/sim/combat.py:268 resolve_combat_round` | `engine/cross_scale/scene_dispatch.py:274 resolve_combat_round` (flag-off default branch) |
| `systems.combat.sim.combat.resolve_action(actor, target, action_type, scene=None, rng=None)` | `systems/combat/sim/combat.py:189 resolve_action` | `resolve_combat_round:293` only |
| `combat_engine_v1/workbench/balance.py` CLI (`weapon_matchup_table`, `attribute_parity_table`, `run_all`, …) | `systems/combat/combat_engine_v1/workbench/balance.py:222` (if __name__) | Jordan/operator, direct invocation (CLAUDE.md §9 routing table) |
| `combat_engine_v1/workbench/server.py:main` | `systems/combat/combat_engine_v1/workbench/server.py:134 main` | direct invocation (local trace/Monte-Carlo HTTP workbench) |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `A`, `B` (`Combatant` objects) | arg | caller-constructed | `systems/combat/combat_engine_v1/wrapper.py:465 fight` |
| `cfg` (defaults to module-level `CFG`) | param | `systems/combat/combat_engine_v1/config.py:2 CFG` (in-code literal dict, not file-read) | `systems/combat/combat_engine_v1/wrapper.py:467` (cfg=cfg or CFG) |
| `rng` (`random.Random`) | arg | caller-supplied or freshly constructed | `systems/combat/combat_engine_v1/wrapper.py:467` (rng=rng or random.Random()) |
| `max_bouts` | arg | caller-supplied, default 12 | `systems/combat/combat_engine_v1/wrapper.py:465` (max_bouts=12) |
| `Combatant.__init__` attribute overrides (`weapon`, `armor`, `tradition`, `strength`, `agi`, `end`, `cog`, `att`, `spirit`, `focus`, `history`, `disp`, `skills`, `equipped`) | arg | caller-constructed, else class defaults | `systems/combat/combat_engine_v1/combatant.py:93 Combatant.__init__` |
| `WEAPONS`, `GEOMETRY`, `HALFSWORD_FORM/BASE` (weapon data registry) | registry | `systems/combat/combat_engine_v1/weapons.py:74 WEAPONS` | `systems/combat/combat_engine_v1/combatant.py:7` (from weapons import) |
| `TRADITIONS`, `ADJACENT`, `ABILITIES`, `TRADITION_KIT` (tradition/ability registries) | registry | `systems/combat/combat_engine_v1/traditions.py:18 TRADITIONS`, `ability_primitives.py` | `systems/combat/combat_engine_v1/tradition.py:13-19` facade re-export |
| `ctx['factions'] = (fid_a, fid_b)` | arg | queued scene context (never populated live — §7) | `engine/cross_scale/combat_bridge.py:121 derive_parties` |
| `world.factions[fid].Mil` | world-state | strategic `World.factions` (aggregate faction stats) | `engine/cross_scale/combat_bridge.py:109` (history=max(1, round(f.Mil))) |
| `world.dispatch_combat_bridge` | flag | decided once per campaign by `mc_v18.run_campaign`, default OFF | `engine/mc_v18.py:78 _dispatch_combat_bridge_on`, `engine/mc_v18.py:237` |
| `wrapper._TRACE` callable | flag | workbench trace/branch-explorer seam, `None` by default | `systems/combat/combat_engine_v1/wrapper.py:16` (_TRACE = None) |

## 3. Flow

S1. **`fight(A, B, cfg, rng, max_bouts)`** — the multi-bout sim harness that runs to a decision (win-rate harness); the intended per-turn game call is **`engagement`** (S2), one engagement per game turn — see §7 for that entry point's reachability. `systems/combat/combat_engine_v1/wrapper.py:465 fight`.
  - S1.1 `[write]` Re-init both `WoundTracker`s and live state (`stamina`, `conc`, `initiative`, `poise`) via `_init_live`. `systems/combat/combat_engine_v1/wrapper.py:471-472`.
  - S1.2 `[emit]` `_emit('fight_start', …)`. `systems/combat/combat_engine_v1/wrapper.py:473`.
  - S1.3 `[loop]` For `turn` in `range(max_bouts)` (each iteration = one **engagement**, `systems/combat/combat_engine_v1/wrapper.py:477`):
    - S1.3.1 Coin-flip `first` aggressor. `systems/combat/combat_engine_v1/wrapper.py:478`.
    - S1.3.2 `[emit]` `_emit('turn_start', …)`. `systems/combat/combat_engine_v1/wrapper.py:479`.
    - S1.3.3 Call **S2 `engagement(...)`**, threading `prev_closed` forward. `systems/combat/combat_engine_v1/wrapper.py:480`.
    - S1.3.4 `[branch]` If a fighter was felled (`loser is not None`): set `result` (+1/-1 for A/B win) and `break`. `systems/combat/combat_engine_v1/wrapper.py:482-484`.
    - S1.3.5 `[write]` Else, per-bout stamina/concentration recovery for both fighters. `systems/combat/combat_engine_v1/wrapper.py:485-487`.
  - S1.4 `[branch][gate]` If `result != 0`, apply the symmetric `UPSET_FLOOR` upset-chance flip. `systems/combat/combat_engine_v1/wrapper.py:493-494`.
  - S1.5 `[emit]` `_emit('fight_result', …)`; return `result` (`+1`=A won, `-1`=B won, `0`=unresolved). `systems/combat/combat_engine_v1/wrapper.py:495-496`.

S2. **`engagement(A, B, first, cfg, rng, prev_closed)`** — one exchange-bout inside a fight; returns `(felled Combatant | None, ended_closed)`. `systems/combat/combat_engine_v1/wrapper.py:47 engagement`.
  - S2.1 `[write]` Reset per-engagement transient geometry (`grip_position`, `lunge_depth`) — the open-measure reset. `systems/combat/combat_engine_v1/wrapper.py:59-60`.
  - S2.2 Derive `reach_base` for both fighters via `combat_systems.reach_base`; fix `longer`/`shorter` labels (tie broken by `rng`). `systems/combat/combat_engine_v1/wrapper.py:61-66`.
  - S2.3 `[gate][branch]` Determine `closed` (measure state) from `measure_gap` against a probabilistic band (`CLOSE_GAP_REF` ± `CLOSE_LATCH_BAND`). `systems/combat/combat_engine_v1/wrapper.py:77-80`.
  - S2.4 `[gate][branch]` Re-presentation gate: if `prev_closed` and the fresh state would be open, the longer weapon must win `represent_measure_p` or the engagement re-starts closed. `systems/combat/combat_engine_v1/wrapper.py:91-94`.
  - S2.5 `[write]` Reset both `initiative` to 0; draw independent uniform `ready` cadence phase per fighter. `systems/combat/combat_engine_v1/wrapper.py:97`, `systems/combat/combat_engine_v1/wrapper.py:110`.
  - S2.6 `[emit]` `_emit('engagement_start', …)`. `systems/combat/combat_engine_v1/wrapper.py:114-116`.
  - S2.7 `[loop]` `while beats < soft*3:` — the per-beat loop (soft cap `soft*3` beats). `systems/combat/combat_engine_v1/wrapper.py:117`.
    - S2.7.1 `[write]` Per-beat state update: initiative decay + disposition drift, poise regen, per-fighter `grip_position`/`range_avail`/`facing`/`lunge_depth` reset, `select_mode` (use-mode selection) + `selected_arm_magnitudes`, `reach_base` refresh #1. `systems/combat/combat_engine_v1/wrapper.py:122-141`.
    - S2.7.2 Compute per-fighter cadence `rate` (open: `weapon_tempo`; closed: `close_tempo`), then advance `ready` by `rate * tempo_pressure`. `systems/combat/combat_engine_v1/wrapper.py:142-149`.
    - S2.7.3 `[branch][gate]` If closed, `beats>1`, and a `reopen_moment` is pending: roll `reopen_prob`; on success the engagement **re-opens** (`closed=False`, `ready=_carry(...)`) and `continue`s the beat loop. `systems/combat/combat_engine_v1/wrapper.py:155-160`.
    - S2.7.4 `[branch][gate]` If closed and `beats>1`: proactive disengage attempt (`disengage_attempt_p`) — on a clean break (`disengage_clean_p`) the engagement re-opens and `continue`s; on a failed/read break the pursuer resolves a strike (`core.resolve` → `core.strike`) and may fell the withdrawer (`return`). `systems/combat/combat_engine_v1/wrapper.py:171-188`.
    - S2.7.5 `[branch]` **Approach phase** (`if not closed:`): stop-thrust roll (`core.resolve`/`core.strike`, may fell + arrest the closer), then `approach_step` advances `measure_gap`; `[gate]` `just_closed` transitions to closed (`ready=_carry(...)`). `systems/combat/combat_engine_v1/wrapper.py:190-227`.
      - S2.7.5a `[gate]` A nested `if not closed:` guard re-tests the (possibly just-updated) `closed` state: if still open, the stamina-collapse gate returns `None`; otherwise `continue`s to next beat. `systems/combat/combat_engine_v1/wrapper.py:228-230`.
      - S2.7.5b `[branch]` If `just_closed` set `closed=True` this same beat, the S2.7.5a guard evaluates false and both the stamina-collapse gate and the `continue` are skipped — the beat falls straight through into **S2.7.6** (closed exchange) without a separate iteration. `systems/combat/combat_engine_v1/wrapper.py:228`.
    - S2.7.6 `[gate]` **Closed exchange gate**: `actors = [c for c in (A,B) if ready[c]>=ACT_THRESHOLD]`; `continue` if empty. Pick `aggressor`/`defender` (both-ready ties broken by `rng`). `systems/combat/combat_engine_v1/wrapper.py:232-238`.
    - S2.7.7 `[write]` Half-sword auto-switch (`halfsword_target`) for both fighters, then re-select use-mode (`select_mode`) and re-derive `reach_base` (refresh #2) on the post-swap form. `systems/combat/combat_engine_v1/wrapper.py:241-252`.
    - S2.7.8 `[write]` Consume `aggressor`'s `ready`; roll `commit_depth`; `[branch][gate]` possible lunge (`lunge_quality`); pay stamina/tempo cost. `systems/combat/combat_engine_v1/wrapper.py:253-261`.
    - S2.7.9a Run the **read contest** (`read_contest`), selecting defender `mode` (`msig`) — this selection is an INPUT consumed by the σ-assembly in S2.7.9b, not the other way around. `systems/combat/combat_engine_v1/wrapper.py:282-286`.
    - S2.7.9b Assemble `net_sigma` from `defence_sigma` (fed the S2.7.9a-selected `msig[mode]`), `attack_sigma`, `armor_defeat_sigma`, `initiative_sigma` via `assemble_net_sigma`. `systems/combat/combat_engine_v1/wrapper.py:290-294`.
    - S2.7.10 `[branch][gate]` If defender won the read and the deep-commit gate holds (`systems/combat/combat_engine_v1/wrapper.py:299`): INDES initiative steal (`indes_steal_amount`) + possible `counter_select`. `systems/combat/combat_engine_v1/wrapper.py:298-303`.
    - S2.7.11 `[gate]` **The roll**: `pool = core.resolution_pool(aggressor.history)`; `deg, net = core.resolve(pool, net_sigma, rng)`. `systems/combat/combat_engine_v1/wrapper.py:304-305`.
    - S2.7.12 `[write]` Apply `overcommit_exposure` (initiative/poise loss) if positive. `systems/combat/combat_engine_v1/wrapper.py:309-313`.
    - S2.7.13 `[branch]` **Outcome mapping** on `deg` × defender `mode`: `fail`→riposte roll; `partial`→graze or bind; `success`→bind/riposte/hit (`core.strike`); `overwhelming`→hit or neutralize-miss. `systems/combat/combat_engine_v1/wrapper.py:319-331`.
    - S2.7.14 `[branch][gate]` If `counter_attempt`: `counter_success_prob` resolves the counter (voids the hit, riposte) or fails (cedes the steal, defender eats an undefended hit). `systems/combat/combat_engine_v1/wrapper.py:332-343`.
    - S2.7.15 `[branch]` **Displace-and-step-inside** gate (an `opening_created` precondition site): committed point-thrust exploited by `beat_aside`/`slip_inside`, gated on `read_win` + `DISPLACE_P`; may pull-back-graze and fells / sets `riposte`. `systems/combat/combat_engine_v1/wrapper.py:349-371`.
    - S2.7.16 `[branch]` Three more `opening_created`/`reopen_moment` precondition sites: over-committed shorter fighter, longer-weapon defensive win, freed-hand shove. `systems/combat/combat_engine_v1/wrapper.py:375-383`.
    - S2.7.17 `[branch][gate]` `if hit>0:` apply wound (`Combatant.apply_wound`), initiative/poise/stamina consequences, percussion stagger; `[gate]` return felled defender. `systems/combat/combat_engine_v1/wrapper.py:384-392`.
    - S2.7.18 `[branch][loop]` `if bind:` up to 3 extra sub-beats of bind resolution (`bind_sigma`, `bind_dominance_p`) — may strike/fell or flip to riposte; entering the bind is itself an `opening_created` precondition site. The bind sub-loop's `for _ in range(3): beats+=1` increments the **same** `beats` local that S2.7's outer `while beats < soft*3` condition checks (`beats` is initialized once at engagement start), so one bind pass can advance `beats` by 4 in a single outer-loop iteration — `beats` is not 1:1 with outer-loop iterations, and the wrapper's own comment at the contact-axis step immediately below (S2.7.20) confirms that step deliberately cannot re-enter this same mutation. `systems/combat/combat_engine_v1/wrapper.py:393-415`; shared counter init `systems/combat/combat_engine_v1/wrapper.py:111`; outer loop condition/increment `systems/combat/combat_engine_v1/wrapper.py:117`, `systems/combat/combat_engine_v1/wrapper.py:118`; bind sub-loop increment `systems/combat/combat_engine_v1/wrapper.py:404-405`; the "cannot re-enter" comment `systems/combat/combat_engine_v1/wrapper.py:431-432`.
    - S2.7.19 `[branch]` `if riposte:` if `sim` (simultaneous hit+riposte), first resolve a `disrupt_resist_p`-gated graze on the original aggressor (may fell); then, unconditionally, drain the (pre-flip) defender's `conc`; only then role-flip `aggressor, defender = defender, aggressor`. `systems/combat/combat_engine_v1/wrapper.py:416-426`.
    - S2.7.20 `[branch][gate]` **Contact axis** (grapple): `contact.grab_available` gated on `opening_created`; `contact.grab_outcome` resolves disarm/throw/pin/foot_pin/control, applying poise/initiative deltas. `systems/combat/combat_engine_v1/wrapper.py:433-448`.
    - S2.7.21 `[emit]` `_emit('outcome', …)`. `systems/combat/combat_engine_v1/wrapper.py:449-451`.
    - S2.7.22 `[gate]` **Turn/exchange separation checks**: stamina collapse → `return None`; `exchanges >= BURST_MAX` → `return None`; clean defence (no hit/riposte/bind) → `return None`. Otherwise the beat loop continues (a burst of exchanges). `systems/combat/combat_engine_v1/wrapper.py:460-462`.
  - S2.8 `[emit]` Loop exhaustion (`beat_exhaustion`) → `return None, closed`. `systems/combat/combat_engine_v1/wrapper.py:463`.

S3. **`core.resolve(pool, net_sigma, rng) -> (degree, net)`** — the shared dice-pool roll + degree band, delegated to `engine.autoload.sigma_leverage`. `systems/combat/combat_engine_v1/core.py:98 resolve`.

S4. **`core.strike(attacker, defender, deg, cfg, net=None, pool=None) -> damage`** — damage-number resolver consumed by every hit site in S2. `systems/combat/combat_engine_v1/core.py:569 strike`.

S5. **Campaign-seam dispatch** (outside `systems/combat/`, traced for the IN-side seam): `scene_dispatch._resolve_slot` on `st == "combat"`. `engine/cross_scale/scene_dispatch.py:224` (st == "combat").
  - S5.1 `[gate][branch]` `if getattr(world, "dispatch_combat_bridge", False):` — flag decided once per campaign by `mc_v18.run_campaign` (default OFF). `engine/cross_scale/scene_dispatch.py:232`, `engine/mc_v18.py:237`.
    - S5.1.1 **ON branch**: `combat_bridge.derive_parties(ctx, world)` → `[gate]` `None` on missing/unresolved `ctx['factions']` → deferred; else `combat_bridge.resolve(parts[0], parts[1], rng)` → **S1 `wrapper.fight`**. `engine/cross_scale/scene_dispatch.py:234-238`.
    - S5.1.2 `[write]` Sets `ctx["echo"]` (`actor_faction`/`target_faction`/`most_relevant_stat="Mil"`/`degree`) keyed off the bridge's `result` int. `engine/cross_scale/scene_dispatch.py:260-267`.
    - S5.1.3 **OFF branch (default)**: `[gate]` no `ctx['participants']` → deferred (`context-derivation gap`); else `systems.combat.sim.combat.resolve_combat_round(parts, ...)` — the DEPRECATED engine (S1 of the deprecated engine, `systems/combat/sim/combat.py:271`), byte-identical to the pre-bridge historical path. `engine/cross_scale/scene_dispatch.py:268-274`.
  - S5.2a `[branch][gate]` If `world.echo_scheduler` is attached (`ECHO_TRANSPORT` on, default ON): `echo_transport.emit_scene_echo("combat", ...)` is called — reached from **both** S5.1 sub-branches (bridge ON and deprecated-engine OFF/default alike), not gated on which one ran. `engine/cross_scale/scene_dispatch.py:390-392`.
    - S5.2b `[gate]` Inside `emit_scene_echo`: early-returns `{}` if `ctx["echo"]` (only set by S5.1.2, ON-branch only) or its derived `key_type` is absent. `engine/cross_scale/echo_transport.py:382`.
    - S5.2c `[branch][gate][emit]` Past that gate, a third, separate gate on the computed domain echo (`er.fires` plus a resolved faction/stat and a non-zero delta) decides whether a `scene.combat_resolved` **Key** is actually constructed and `sched.emit`ted into the substrate (deferred faction-stat apply at the accounting boundary). `engine/cross_scale/echo_transport.py:410-438`.
  - S5.3 **Never reached in the live campaign today** — see §7: no call site ever queues a `combat`-type scene, so `_resolve_slot`'s `st == "combat"` branch is dead code under the current season-loop trigger set regardless of the flag.

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `fight()` return `int` (`+1`\|`-1`\|`0`) | return value | `combat_bridge.resolve` (wraps into a result dict); workbench win-rate tallies; tests | `systems/combat/combat_engine_v1/wrapper.py:483-484`, `systems/combat/combat_engine_v1/wrapper.py:494-495` |
| `combat_bridge.resolve()` return dict (`result`, `winner`, `a_label`, `b_label`, `a_history`, `b_history`) | return value | `scene_dispatch._resolve_slot`'s `out["result"]` | `engine/cross_scale/combat_bridge.py:142-150` |
| `ctx["echo"]` block (ON-branch only) | write to caller-owned dict | `echo_transport.emit_scene_echo` | `engine/cross_scale/scene_dispatch.py:266-267` |
| `scene.combat_resolved` `Key` (substrate) | emit | `engine.substrate.TickScheduler` log; deferred `Faction.adjust(stat, delta)` apply at accounting boundary | `engine/cross_scale/echo_transport.py:416-438` |
| `resolve_combat_round()` return `RoundResult` (deprecated engine) | return value | `scene_dispatch._resolve_slot`'s `out["result"]` (OFF branch) | `engine/cross_scale/scene_dispatch.py:274-276` |
| `wrapper._emit(kind, **data)` trace events (`fight_start`, `turn_start`, `engagement_start`, `disengage`, `approach`, `stophit`, `commit`, `read`, `mode`, `roll`, `outcome`, `contact`, `separation`, `engagement_end`, `fight_result`) | emit (in-process callback) | `workbench/trace.py`'s `wrapper._TRACE` seam only when set; no-op (`_TRACE is None`) otherwise | `systems/combat/combat_engine_v1/wrapper.py:17-19`, `systems/combat/combat_engine_v1/workbench/trace.py:19-20` |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| `Combatant.stamina`, `.conc`, `.initiative`, `.poise` | RW | `combat_engine_v1/combatant.py` (declared); reset/mutated by `wrapper.py` | `systems/combat/combat_engine_v1/wrapper.py:21-26 _init_live` |
| `Combatant.wt` (`WoundTracker`: `cumulative_damage`, `wounds`, `felled`) | RW | `systems/combat/combat_engine_v1/combatant.py:50 WoundTracker` | `systems/combat/combat_engine_v1/wrapper.py:471` (A.wt.__init__(...)); `systems/combat/combat_engine_v1/combatant.py:154 apply_wound` |
| `Combatant.grip_position`, `.lunge_depth`, `.sel_*`, `.range_avail`, `.facing` | RW | `combat_engine_v1/combatant.py` (declared, per-beat derived); written by `wrapper.py` per beat | `systems/combat/combat_engine_v1/wrapper.py:133-141` |
| `Combatant.weapon` (half-sword form switch) | RW | `combatant.py` field; mutated by `wrapper.py` via `combat_systems.halfsword_target` | `systems/combat/combat_engine_v1/wrapper.py:241-242` |
| `world.factions[fid].Mil` (aggregate faction stat) | R | `engine/autoload/game_state.py` `Faction` | `engine/cross_scale/combat_bridge.py:109 f.Mil` |
| `world.factions[fid]` stat (via `.adjust`) | W (deferred, accounting boundary) | `engine/autoload/game_state.py` `Faction.adjust` | `engine/cross_scale/echo_transport.py:435-436` (f.adjust(...)) |
| `world.dispatch_combat_bridge` | W (once, campaign init) / R (per season) | `engine/mc_v18.py` | `engine/mc_v18.py:237`; read at `engine/cross_scale/scene_dispatch.py:232` |
| `world.echo_scheduler` / `world.key_log` | W (once, campaign init) / R (per scene) | `engine/mc_v18.py` / `engine/cross_scale/echo_transport.py` | `engine/mc_v18.py:243-249` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| up | `engine/cross_scale/combat_bridge.py` (IN lane) | consumes `wrapper.fight` + `combatant.Combatant` as-is via a sibling-directory `sys.path` insert + bare import (no `systems.combat.combat_engine_v1` package import exists) | `engine/cross_scale/combat_bridge.py:95-99 _load_engine` |
| up | `engine/cross_scale/scene_dispatch.py` (IN lane) | dispatches queued `combat`-type scenes to either the bridge (flag ON) or the deprecated `systems.combat.sim.combat` (flag OFF, default) | `engine/cross_scale/scene_dispatch.py:224-274` |
| up | `engine/mc_v18.py` (campaign driver) | decides+stashes `world.dispatch_combat_bridge` once per campaign; calls `scene_dispatch.run_scene_phase` every season | `engine/mc_v18.py:141`, `engine/mc_v18.py:237` |
| lateral | `engine/autoload/sigma_leverage.py` | `core.py` resolves its continuous dice-pool roll through the shared sigma-leverage kernel, not a private re-implementation | `systems/combat/combat_engine_v1/core.py:19` (from engine.autoload import sigma_leverage as SL) |
| out | `engine/cross_scale/echo_transport.py` (IN lane) | on the bridge ON-branch + `ECHO_TRANSPORT` on, converts `ctx["echo"]` into a `scene.combat_resolved` Key and a deferred `Faction.adjust` write — **combat_engine_v1 itself never touches this**, the seam is entirely on the IN side | `engine/cross_scale/echo_transport.py:99`, `engine/cross_scale/echo_transport.py:416-438` |
| out | `references/module_contracts.yaml` `personal_combat` module | declares `emits: scene.combat_hit / scene.combat_felled / scene.combat_resolved` as though the engine itself emits Keys — see §7 divergence | `references/module_contracts.yaml:1040-1043` |
| lateral (doc-only) | `godot/skeleton/engines/combat/` | GDScript illustration of the `combat.strike`/`combat.wound` module slice; not exercised by any Python flow traced here | `godot/godot_conversion_strategy_v1.md` (not re-anchored — GDScript tree, out of scope for a Python-code trace) |

## 7. Traced gaps

| Gap | Evidence |
|---|---|
| **`combat_engine_v1` neither emits nor consumes a substrate `Key`.** The `personal_combat` module contract declares `emits: scene.combat_hit / scene.combat_felled / scene.combat_resolved` and `consumes: scene.combat_strike / scene.combat_hit` as the engine's own I/O, but zero `.py` files under `combat_engine_v1/` reference `engine.substrate`, `Key(`, or `KeyLog` — the only grep hits are unrelated prose uses of the word "substrate" (initiative/tradition substrate). The one real `scene.combat_resolved` Key construction site lives entirely outside the subsystem, in `engine/cross_scale/echo_transport.py`. | `grep -rn "substrate\|KeyLog\|Key(" systems/combat/combat_engine_v1/*.py` → no substrate-API hits; `engine/cross_scale/echo_transport.py:416` (key = Key(); emits block at `references/module_contracts.yaml:1040-1043`; consumes block at `references/module_contracts.yaml:1037-1039` |
| **No live trigger ever queues a `combat`-type scene**, so the entire `st == "combat"` branch of `scene_dispatch._resolve_slot` — both the bridge (ON) and the deprecated engine (OFF, default) sub-branches — is unreachable from the season loop today, independent of `DISPATCH_COMBAT_BRIDGE`'s value. `evaluate_triggers` only ever fires a `"contest"` scene (Stability Crisis); the repo's only `scene_slate.queue_scene(...)` call site passes `ev["scene_type"]` from that fired-triggers list. | `engine/cross_scale/scene_dispatch.py:75-99 evaluate_triggers` (fires only `scene_type: "contest"`); `engine/cross_scale/scene_dispatch.py:105` (scene_slate.queue_scene(ev["scene_type"], ...)) (the only call site repo-wide — confirmed by `grep -rn "queue_scene(" .` returning just the definition + this one call); module docstrings at `engine/cross_scale/scene_dispatch.py:36-39` and `engine/cross_scale/combat_bridge.py:37-38` both independently assert the same absence |
| **`DISPATCH_COMBAT_BRIDGE` defaults OFF** (a default-off flag per §2 architecture rule 4). With it off, `scene_dispatch`'s combat branch calls the DEPRECATED `systems.combat.sim.combat.resolve_combat_round` (its own v30 pool/damage model, distinct from `combat_engine_v1`'s sigma-leverage model) rather than the canonical engine — moot in practice per the gap above, but the flag default is itself a traced absence. | `engine/mc_v18.py:78-89 _dispatch_combat_bridge_on` (`os.environ.get('DISPATCH_COMBAT_BRIDGE', '0') == '1'`) |
| `capabilities.py` and `state_graph.py` are present in `combat_engine_v1/` but are not imported by the live resolver spine (`wrapper.py` → `core.py`/`combat_systems.py`/`contact.py`/`tradition.py`). `capabilities.py`'s only production-code importer is `workbench/catalogue.py`; `state_graph.py` is imported only by `tests/valoria/test_combat_state_graph.py` and otherwise run standalone via its own `__main__` self-check — a declarative mirror of the traced control flow used for coverage verification, not part of the executed flow itself. | `grep -rln "import capabilities" systems/combat` → `workbench/catalogue.py` only; `grep -rln "import state_graph" systems tests` → `tests/valoria/test_combat_state_graph.py:15` only (the module does not import itself); `systems/combat/combat_engine_v1/state_graph.py:165` (`if __name__ == '__main__':`) |
| The intended per-turn game entry point, `wrapper.engagement`, has no outside caller — the only call site anywhere in the traced tree is `wrapper.fight` itself (the multi-bout sim harness, S1), which is internal to the same module. | `systems/combat/combat_engine_v1/wrapper.py:47 engagement` (called only at `systems/combat/combat_engine_v1/wrapper.py:480`); `systems/combat/combat_engine_v1/wrapper.py:477` (inline comment distinguishing the sim harness from the intended per-turn game call) |
| Deprecated engine `systems/combat/sim/combat.py`'s action set (`Feint`, `Disarm`, `Tie Up`, `Retrieve`, `Escape`, `Leap`, `Rescue`) is explicitly unimplemented — falls through to a `Failure` stub. Structural, not mechanical: no dispatch branch exists for these action types. | `systems/combat/sim/combat.py:90-97` (the declared action set, `ACTION_RESOLUTION_ORDER`); `systems/combat/sim/combat.py:263-268` (the "Action not implemented this tier" fallthrough — no action names appear at this anchor) |
