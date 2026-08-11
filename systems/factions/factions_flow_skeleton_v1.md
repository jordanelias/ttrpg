# Factions — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/factions/` · **Lane:** `FA` · **Contracts:** `faction_state`, `npc_behavior` (partial), `ci_political`, `faction_politics`
**Code roots traced:** `systems/factions/sim/` (16 modules), `engine/autoload/game_state.py` (`Faction`/`Territory`/`World`), `engine/autoload/season_manager.py`, `engine/cross_scale/parliamentary_bridge.py`, `engine/mc_v18.py` (caller), plus one-hop peer touches into `systems/mass_battle/sim/massbattle.py`, `systems/social_contest/sim/parliamentary_vote.py`, `systems/settlements/sim/adjacency.py`, `systems/settlements/sim/infrastructure.py`, `systems/overview/sim/ci_track.py`, `engine/autoload/victory.py`, `engine/substrate/keys.py`, `engine/cross_scale/articulation.py`.
**Traced at:** `6545067`

## 1. Entry points

| Callable | Anchor | Called-by |
|---|---|---|
| `faction_take_action(faction, world, rng)` | `systems/factions/sim/faction_action.py:177 faction_take_action` | `engine/mc_v18.py:130 faction_take_action` (inside `_faction_actions_callback`) |
| `Faction.reset_arc()` | `engine/autoload/game_state.py:135 reset_arc` | `engine/autoload/season_manager.py:39 reset_arc` |
| `Faction.reset_seasonal()` | `engine/autoload/game_state.py:131 reset_seasonal` | `engine/autoload/season_manager.py:42 reset_seasonal` |
| `run_parliamentary_scene(world, rng)` | `engine/cross_scale/parliamentary_bridge.py:180 run_parliamentary_scene` | `engine/mc_v18.py:150 run_parliamentary_scene` (gated on `world.echo_scheduler`) |
| `propose_transfer(initiator, target_territory, mode, world, ...)` | `systems/factions/sim/parliamentary_transfer.py:182 propose_transfer` | `engine/cross_scale/parliamentary_bridge.py:173 propose_transfer` (via `_run_transfer_motion`) |
| `propose_censure(proposer, world, rng)` | `systems/factions/sim/parliamentary_action.py:96 propose_censure` | `systems/factions/sim/faction_action.py:266 propose_censure` |
| `TreatyRecord.from_dict(...)` | `systems/factions/sim/treaty.py:76-82 from_dict` (dataclass, module-level) | `engine/autoload/game_state.py:381 TreatyRecord` (`restore_world`, deserialization only) |
| `attempt_charter(world)` | `systems/factions/sim/charter_liberties.py:27 attempt_charter` | — (stub; only `engine/tests/test_pipeline_reach.py:750`) |
| `apply_hafenmark_equipment(faction_state)` | `systems/factions/sim/hafenmark_equipment.py:30 apply_hafenmark_equipment` | — (stub; only `engine/tests/test_pipeline_reach.py:755`) |
| `t9_invasion_modifier(world)` | `systems/factions/sim/home_sanctuary.py:29 t9_invasion_modifier` | — (stub; only `engine/tests/test_pipeline_reach.py:752`) |
| `check_sanctuary_active(world)` | `systems/factions/sim/home_sanctuary.py:37 check_sanctuary_active` | — (stub; zero callers anywhere, including tests) |
| `compute_reclamation_bonus(target_territory, world)` | `systems/factions/sim/infrastructure_reclamation.py:29 compute_reclamation_bonus` | — (stub; only `engine/tests/test_pipeline_reach.py:751`) |
| `attempt_mandate_action(world)` | `systems/factions/sim/varfell_mandate_action.py:40 attempt_mandate_action` | — (stub; only `engine/tests/test_pipeline_reach.py:753`) |
| `attempt_territorial_acquisition(target_territory, world)` | `systems/factions/sim/varfell_territorial_acquisition.py:42 attempt_territorial_acquisition` | — (stub; only `engine/tests/test_pipeline_reach.py:754`) |
| `attempt_mass_seizure_declaration(world, force_declare=False)` | `systems/factions/sim/mass_seizure.py:161 attempt_mass_seizure_declaration` | — (implemented, zero production callers) |
| `resolve_mass_seizure(world, rng=None)` | `systems/factions/sim/mass_seizure.py:222 resolve_mass_seizure` | — (implemented, zero production callers) |
| `propose_treaty(parties, terms, world=None)` | `systems/factions/sim/treaty.py:99 propose_treaty` | — (stubwired no-op via `stubwire.stub_resolve`, does not raise despite its own docstring — see §7; zero production callers) |
| `process_treaty_expirations(world, lapse_rate=...)` | `systems/factions/sim/treaty.py:121 process_treaty_expirations` | — (implemented, zero production callers) |
| `register_treaty(...)` | `systems/factions/sim/treaty.py:145 register_treaty` | — (zero callers anywhere, including tests) |
| `run_excommunication_tribunal(accused, church, world, rng, ...)` | `systems/factions/sim/tribunal.py:87 run_excommunication_tribunal` | `systems/factions/sim/excommunication.py:119 run_excommunication_tribunal` |
| `run_tribunal(accused, accusers, proceeding_type, world=None, rng=None)` | `systems/factions/sim/tribunal.py:143 run_tribunal` | — (stub; zero callers anywhere, including tests) |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| `faction` | arg | `world.factions.items()` loop | `engine/mc_v18.py:124 faction` |
| `world` | arg | passed through `season.run_season` → `action_callback` | `engine/mc_v18.py:130 world` |
| `rng` | arg | `world.rng` | `engine/mc_v18.py:130 world.rng` |
| `faction.parliamentary`, `faction.territories` | key (gate) | `Faction` dataclass | `engine/mc_v18.py:125-127 parliamentary` |
| `world.territories`, `ADJACENCY` | world-state | `systems/settlements/sim/adjacency.py` | `systems/factions/sim/faction_action.py:117-122 ADJACENCY` |
| `faction.Mil`, `.L`, `.I`, `.Sta`, `.W`, `.standing` | world-state | `Faction` dataclass fields | `engine/autoload/game_state.py:98-114 Faction` |
| `world.clocks['CI']` | world-state | overview-owned clock, read via `.get('CI', 0.0)` | `systems/factions/sim/council_solmund.py:32 CI` |
| `world.echo_scheduler` | flag | set by `engine/mc_v18.py:243`, read via `getattr` | `engine/cross_scale/parliamentary_bridge.py:190 echo_scheduler` |
| `world.casus_belli` | flag (optional, duck-typed) | absent by default; no populating writer found in this trace | `systems/factions/sim/parliamentary_transfer.py:110 casus_belli` |
| `BASE_W_UNIQUE/CONQUEST/MUSTER/GOVERN`, `CONQUEST_TARGET_COEF`, `CONQUEST_MILADV_COEF`, `LOW_ACCORD_SEED`, `MUSTER_WEALTH_COST`, `CONQUEST_MIN_MIL`, etc. | param | module-level constants | `systems/factions/sim/faction_action.py:47-84 BASE_W_UNIQUE` |
| `MULTS`, `ALL_PLAYABLE_15` | registry | `engine/autoload/game_state.py` | `systems/factions/sim/faction_action.py:34 MULTS` |

## 3. Flow

**S0** `[gate][write]` Arc boundary: only when `new_arc` (season is the first of a new arc) does `Faction.reset_arc` clear arc-scoped flags on every faction — `engine/autoload/season_manager.py:34-39 new_arc`.

**S0.1** `[write]` Season boundary (ungated): `Faction.reset_seasonal` clears season-scoped flags on every faction, every season, regardless of the arc-boundary gate above — `engine/autoload/season_manager.py:40-42 reset_seasonal`.

**S1** `[loop][gate]` For each faction in `world.factions`: skip unless `faction.parliamentary` and `faction.territories` non-empty — `engine/mc_v18.py:124-128 parliamentary`.

**S2** `[emit-dispatch]` Call `faction_take_action(faction, world, world.rng)`, guarded per-faction by a try/except that logs to stderr rather than aborting the season — `engine/mc_v18.py:130-136 faction_take_action`.

  **S2.1** Compute four RNG-free state signals: conquest targets/mil-advantage, undergoverned share, threat — `systems/factions/sim/faction_action.py:192-196 targets`.

  **S2.2** `[gate]` Turn signals into per-bucket multipliers, re-weight the four base weights, renormalize to a probability vector — `systems/factions/sim/faction_action.py:199-212 conquest_mult`.

  **S2.3** `[gate]` Single draw `roll = rng.random()` against the cumulative thresholds — `systems/factions/sim/faction_action.py:220 roll`.

  **S2.4** `[branch]` `roll < cum_unique` → `_try_faction_unique` — `systems/factions/sim/faction_action.py:223-227 _try_faction_unique`.
    - **S2.4.1** `[branch]` Dispatch by `faction.name`: `Crown` → `crown_initiative.select_initiative_mode` then one of 3 modes; `Church` → priority chain Excommunication → Council → Absolution; any other name → immediate NOOP — `systems/factions/sim/faction_action.py:277-318 _faction_specific_unique`.
    - **S2.4.2** `[branch][gate]` If the faction-specific chain returned NOOP and `faction.parliamentary`, fall back to `parliamentary_action.propose_censure` — `systems/factions/sim/faction_action.py:264-268 propose_censure`.
    - **S2.4.3** `[branch]` If still NOOP, fall through to Conquest — `systems/factions/sim/faction_action.py:227` (fall through).

  **S2.5** `[branch]` `roll < cum_conquest` → `_try_conquest` — `systems/factions/sim/faction_action.py:230-233 _try_conquest`.
    - **S2.5.1** `[gate]` No-op unless a target exists and `faction.Mil >= CONQUEST_MIN_MIL` — `systems/factions/sim/faction_action.py:423 CONQUEST_MIN_MIL`.
    - **S2.5.2** `[lateral]` Resolve via `mass_battle.sim.massbattle.resolve_mass_battle` — `systems/factions/sim/faction_action.py:431-438 resolve_mass_battle`.
    - **S2.5.3** `[emit]` Emit `scene.battle_concluded` Key (log-only, no `apply=`) — `systems/factions/sim/faction_action.py:459 _emit_battle_concluded`.
    - **S2.5.4** `[branch][write]` On attacker win: transfer territory ownership, apply a loser Legitimacy penalty; then fork Terms (`deg == 'Success'`) vs Storm on Accord penalty and an `entry_terms_l_seed` proxy write — `systems/factions/sim/faction_action.py:461-497 attacker_wins`.

  **S2.6** `[branch][write]` `roll < cum_muster` → `_try_muster`: pay Wealth up front, roll `pool = Mil + floor(W / MUSTER_WEALTH_TO_POOL_DIV)`, apply Mil gain on success — `systems/factions/sim/faction_action.py:236-239 _try_muster`, `systems/factions/sim/faction_action.py:500-528 _try_muster`. Also reached by fall-through when S2.5's `_try_conquest` returns the `_NOOP` sentinel — since `cum_muster >= cum_conquest`, the same `roll` still satisfies this step's own condition, the analogous fall-through documented for the faction-unique slot at S2.4.3 — `systems/factions/sim/faction_action.py:230-239` (fall through), sentinel return at `systems/factions/sim/faction_action.py:423-424 _NOOP`.

  **S2.7** `[branch][write]` Unconditional terminal call — not gated on any threshold, reached whenever S2.4-S2.6 all failed to return a non-sentinel result → `_try_govern`: roll `pool = faction.I` against a fixed Ob, apply Accord gain or Stability loss — `systems/factions/sim/faction_action.py:242 _try_govern`, `systems/factions/sim/faction_action.py:531-550 _try_govern`. The three preceding branches at S2.4/S2.5/S2.6 are independent `if` statements, not `elif` — a roll landing in an early bucket whose branch returns the sentinel falls through every remaining bucket to this line, and the return here is itself not checked by the caller — see §7 for the compound cascade and its reachability.

  **S2.8** The dispatch-string return value of `faction_take_action` is not captured by the caller — `engine/mc_v18.py:130 faction_take_action` (call site discards the return).

**S3** `[emit]` Scene phase dispatch (peer subsystem, not traced further here) — `engine/mc_v18.py:141-142 run_scene_phase`.

**S4** `[gate]` If `world.echo_scheduler` is attached, call `parliamentary_bridge.run_parliamentary_scene(world, world.rng)` — `engine/mc_v18.py:148-152 run_parliamentary_scene`.

  **S4.1** Derive a two-pole motion from aggregate state: proposer = lowest-Stability eligible faction, establishment = highest-Mandate eligible faction — `engine/cross_scale/parliamentary_bridge.py:82-97 _derive_vote`.

  **S4.2** `[gate]` Fewer than 2 eligible factions → skip the vote (still attempts S4.6) — `engine/cross_scale/parliamentary_bridge.py:192-196` (fewer than two eligible).

  **S4.3** `[lateral]` Resolve via `systems.social_contest.sim.parliamentary_vote.run_parliamentary_vote` — `engine/cross_scale/parliamentary_bridge.py:199 run_parliamentary_vote`.

  **S4.4** `[branch]` Map vote band → (winning side, Domain-Echo degree); Committee/compromise → no echo — `engine/cross_scale/parliamentary_bridge.py:100-111 _winner_and_degree`, `engine/cross_scale/parliamentary_bridge.py:201-203 _winner_and_degree`.

  **S4.5** `[branch][emit]` On Success/Overwhelming, compose and emit a winner-side Domain Echo through `echo_transport.emit_scene_echo` — `engine/cross_scale/parliamentary_bridge.py:212 emit_scene_echo`.

  **S4.6** `[branch]` Independently (regardless of S4.1-S4.5 outcome) attempt the CB-gated Territory Transfer motion — `engine/cross_scale/parliamentary_bridge.py:217 _run_transfer_motion`.
    - **S4.6.1** Derive `(initiator, holder, mode)` candidates purely from `parliamentary_transfer`'s own CB tables, excluding arc-gated initiators and floor-protected holders — `engine/cross_scale/parliamentary_bridge.py:114-156 _derive_transfer`.
    - **S4.6.2** `[gate]` No candidate → return `None`, no side effects — `engine/cross_scale/parliamentary_bridge.py:169-171` (derived is None).
    - **S4.6.3** Call `parliamentary_transfer.propose_transfer(initiator, target_territory, mode, world, rng=rng)` — `engine/cross_scale/parliamentary_bridge.py:173 propose_transfer`.
      - **S4.6.3.1** `[gate]` Sequential blocks: mode validity, unknown initiator, GD-3 non-parliamentary, unheld target territory, self-transfer, last-territory floor, per-arc frequency — `systems/factions/sim/parliamentary_transfer.py:187-226 propose_transfer`.
      - **S4.6.3.2** `[gate]` CB availability filtered by mode; sets `parl_transfer_used_this_arc = True` on qualification — `systems/factions/sim/parliamentary_transfer.py:229-241 qualifying`.
      - **S4.6.3.3** `[lateral]` A second `run_parliamentary_vote` call determines a pool modifier — `systems/factions/sim/parliamentary_transfer.py:246-253 run_parliamentary_vote`.
      - **S4.6.3.4** `[gate]` Roll `pool = Proposer.I + mod` vs `Ob = Holder.L + PARL_MAJORITY_OB_BONUS` — `systems/factions/sim/parliamentary_transfer.py:257-260 roll_pool`.
      - **S4.6.3.5** `[branch][write][emit]` On Success/Overwhelming: move territory (`Faction.territories` and `Territory.owner`), set Accord, emit `da.public_governance` Key, and — Overwhelming only — additionally apply a holder Legitimacy penalty; on Partial: grant a retry CB, no transfer; on Failure: always a proposer Stability penalty, then by mode — Punishment applies a holder Standing penalty, Consensual applies no holder effect, and the default (adversarial/appeasement) branch instead GRANTS the holder Legitimacy — `systems/factions/sim/parliamentary_transfer.py:269-317 deg`.

**S5** `[write]` Accounting boundary: apply deferred Key effects, advance the tick counter — `engine/mc_v18.py:158-161 accounting_boundary`.

**S6** `[gate]` After the season completes, `victory.check_all_factions` reads `Territory.owner` written in S2.5.4/S4.6.3.5 for territory-count scoring — `engine/mc_v18.py:268-269 check_all_factions`.

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| `Territory.owner` mutation | world-state write | `engine/autoload/victory.py` territory-count scoring | `engine/autoload/victory.py:65-66 owner` |
| `Faction.territories` mutation | world-state write | same victory check; also read back by `_conquest_targets`/`_undergoverned_share` next season | `systems/factions/sim/faction_action.py:470-471 territories.append` |
| `Faction.L/Sta/W/Mil/standing` mutation | world-state write | read by this subsystem's own next-season signals only (no cross-subsystem reader found) | `engine/autoload/game_state.py:124-129 adjust` |
| `world.battle_count` increment | world-state write | no reader found in this trace | `systems/factions/sim/faction_action.py:495 battle_count` |
| `scene.battle_concluded` Key | emit (log-only) | declared 4 consumers in `references/key_graph.json` per in-code comment, but no live subscriber found — see §7 | `systems/factions/sim/faction_action.py:459 _emit_battle_concluded` |
| `da.public_governance` Key | emit (log-only) | declared consumer `faction_layer` per in-code comment; no live subscriber found — see §7 | `systems/factions/sim/parliamentary_transfer.py:116-176 _emit_public_governance_transfer` |
| Domain Echo (`echo_transport.emit_scene_echo`) | emit (deferred write) | applied at the accounting boundary (S5) via the substrate | `engine/cross_scale/parliamentary_bridge.py:212 emit_scene_echo` |
| `faction_take_action` return string | return value | discarded by caller — see §7 | `engine/mc_v18.py:130 faction_take_action` |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| `Faction.L` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/faction_action.py:467 adjust` |
| `Faction.Sta` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/faction_action.py:548 adjust` |
| `Faction.W` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/faction_action.py:515-518 adjust` |
| `Faction.I` | R | `engine/autoload/game_state.py` | `systems/factions/sim/faction_action.py:540 faction.I` |
| `Faction.Mil` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/faction_action.py:524 adjust` |
| `Faction.standing` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/crown_initiative.py:97 standing` |
| `Faction.territories` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/faction_action.py:470-471 territories` |
| `Faction.parliamentary` | R | `engine/autoload/game_state.py` | `engine/mc_v18.py:125 parliamentary` |
| `Faction.excommunicated` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/excommunication.py:142 excommunicated` |
| `Faction.senator_inward_used` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/crown_initiative.py:78 senator_inward_used` |
| `Faction.council_used_this_arc` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/council_solmund.py:59 council_used_this_arc` |
| `Faction.parl_transfer_used_this_arc` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/parliamentary_transfer.py:241 parl_transfer_used_this_arc` |
| `Territory.owner` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/faction_action.py:468 owner` |
| `Territory.accord` | RW | `engine/autoload/game_state.py` | `systems/factions/sim/faction_action.py:482 adjust_accord` |
| `Territory.garrison` | W | `engine/autoload/game_state.py` | `systems/factions/sim/faction_action.py:472 garrison` |
| `Territory.entry_terms_l_seed` | W (dynamic, not a dataclass field) | none — see §7 | `systems/factions/sim/faction_action.py:489 entry_terms_l_seed` |
| `world.clocks['CI']` | RW | `engine/autoload/game_state.py` (field), `systems/overview/sim/ci_track.py` (writer) | `systems/factions/sim/excommunication.py:166-167 apply_ci_delta` |
| `world.battle_count` | W | `engine/autoload/game_state.py` | `systems/factions/sim/faction_action.py:495 battle_count` |
| `world.arc` | R | `engine/autoload/game_state.py` | `systems/factions/sim/parliamentary_transfer.py:225 world.arc` |
| `world.treaties` | RW (declared; live writers are all unreached production paths) | `engine/autoload/game_state.py` | `engine/autoload/game_state.py:187 treaties` |
| `world._battle_key_seq`, `world._parl_key_seq` | RW (dynamic attrs) | none (ad hoc counters) | `systems/factions/sim/faction_action.py:354-355 _battle_key_seq` |
| `world.casus_belli` | RW (optional, duck-typed; not a dataclass field) | none — see §7 | `systems/factions/sim/parliamentary_transfer.py:110 casus_belli` |
| `Faction.consul_used` | W | `engine/autoload/game_state.py` | `engine/autoload/game_state.py:133 consul_used` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| down | `settlements` | `ADJACENCY` map for conquest-target/threat derivation | `systems/factions/sim/faction_action.py:35 ADJACENCY` |
| down (declared, unreached) | `settlements` | `count_infrastructure`/`seizure_ob_modifier` imports in `mass_seizure.py` | `systems/factions/sim/mass_seizure.py:51-54 count_infrastructure` |
| lateral | `mass_battle` | `resolve_mass_battle(faction_a, faction_b, terrain, world)` for Conquest resolution | `systems/factions/sim/faction_action.py:431-438 resolve_mass_battle` |
| lateral | `social_contest` | `run_parliamentary_vote`/`Motion`/`VoteDeclaration` — Censure vote, Territory-Transfer vote, and the season's two-pole vote all wrap this resolver | `systems/factions/sim/parliamentary_action.py:40-44 run_parliamentary_vote` |
| lateral | `social_contest` | Excommunication Tribunal reuses `dice_engine` directly rather than a social_contest call — no edge (kept in-lane at `tribunal.py`) | `systems/factions/sim/tribunal.py:26 dice_engine` |
| lateral | `overview` | `ci_track.apply_ci_delta` for the §7.1 Excommunication CI escalation | `systems/factions/sim/excommunication.py:166-167 apply_ci_delta` |
| up/out | `overview`/victory | `Territory.owner` and `Faction.territories` writes are read by `victory.check_all_factions` for the territory-count win condition | `engine/autoload/victory.py:65-66 owner` |
| in | `overview` | `season_manager.advance_season` resets `Faction.reset_arc`/`reset_seasonal` before the action pass runs | `engine/autoload/season_manager.py:38-42 reset_arc` |
| in/out | `engine` substrate (Key log) | `scene.battle_concluded` / `da.public_governance` Key emission, gated on `world.echo_scheduler` | `systems/factions/sim/faction_action.py:348-350 echo_scheduler` |
| out | `engine` substrate (Key log) | `echo_transport.emit_scene_echo` composes a Domain Echo from the parliamentary vote outcome | `engine/cross_scale/parliamentary_bridge.py:212 emit_scene_echo` |

## 7. Traced gaps

| Gap | Evidence anchor |
|---|---|
| `faction_state`'s RESOLVER half (`mechanical.cascade_resolution` / `mechanical.mission_shift` accounting logic) has no implementation anywhere in the tree — confirmed, not merely repeated from the contract annotation, and restated at the precise scope the contract annotation overstated: `cascade_resolution` has zero Python implementation hits in `systems/` or `engine/` — its only occurrence in the tree at all is its own declaration in the key-types export, never consumed. `mission_shift` is likewise declared in the key-types export and is additionally consumed, but only as a subscription constant in `articulation.py`'s trigger-type-id tuple (a consumer registration, not resolver logic). No resolver exists for either type. | `references/module_contracts.yaml:67-70` (claim); `engine/engine_params/key_types.json:394 cascade_resolution` (declaration only, never consumed); `engine/engine_params/key_types.json:420 mission_shift` (declaration); `engine/cross_scale/articulation.py:120 mechanical.mission_shift` (sole consumption, list literal) |
| The docstring/module-header claim of "GD-2: mandatory threat-response before stochastic selection" does not match the code: there is no unconditional mandatory-action pass. `faction_take_action` computes RNG-free signals only to re-weight the probabilities of a single stochastic draw (`roll = rng.random()`); every branch, including the Church "priority chain," is reached only if that one roll lands in its (state-shifted) band. A faction with e.g. a live conquest opportunity is not guaranteed to act on it this season. The same false claim is propagated in three more places: the caller's own docstring, the Church excommunication module's header and a second inline mention, and generated tooling that inherited the caller's wording verbatim. | `systems/factions/sim/faction_action.py:180` (GD-2); `systems/factions/sim/faction_action.py:220 roll` (the only gate); `engine/mc_v18.py:119 _faction_actions_callback` (caller docstring); `systems/factions/sim/excommunication.py:8` (module header); `systems/factions/sim/excommunication.py:200 select_excommunication_target` (inline claim); `tools/build_execution_map.py:97` (generated execution-map note) |
| 6 of 16 `systems/factions/sim/` modules (`charter_liberties`, `hafenmark_equipment`, `home_sanctuary`, `infrastructure_reclamation`, `varfell_mandate_action`, `varfell_territorial_acquisition`) are pure `stubwire.stub_resolve` armature stubs with no real logic — declared entry points that resolve to a typed no-op, reachable only via `engine/tests/test_pipeline_reach.py`'s stub-wiring probe (`check_sanctuary_active`/`register_treaty` are not even probed there). Two whole faction identities (Varfell, Hafenmark) have zero faction-unique action in the live dispatch — `faction_action.py` routes both straight to the universal Parliamentary-Censure fallback. Separately, the module's own `__init__.py` roster is stale by two entries — it names only 14 modules, omitting `tribunal` and `home_sanctuary` — even though `home_sanctuary` is one of the six stubs counted here. | `systems/factions/sim/charter_liberties.py:27-32 stub_resolve`; `systems/factions/sim/faction_action.py:315-318` (no faction-specific unique action yet); `systems/factions/sim/__init__.py:1` (stale 14-module roster) |
| `mass_seizure.py` (Church's declared victory-adjacent action, full implementation, not a stub) and `treaty.py`'s `process_treaty_expirations`/`register_treaty` have zero production callers — verified independently in this trace (grep across `systems/`+`engine/` for each entry-point function name, excluding tests and self-module, returns nothing) and matches an in-repo measurement note that additionally confirms it by 40-seed instrumentation. `propose_treaty` is a stubwired no-op (no canonized non-Senator-Outward formation path) — it does not raise. | `systems/factions/sim/parliamentary_transfer.py:130-135 UNREACHABLE`; `systems/factions/sim/treaty.py:7-15` (IMPLEMENTATION STATUS) |
| `treaty.py`'s own docstring (module header and the `propose_treaty` entry-point summary) still declares the function "raises"/"still raises" with no canonized formation path, but the implementation was converted (OI-19, ED-IN-0091 plan §3 Wave 1) to a `stubwire.stub_resolve` typed no-op — it returns a `StubResult` and never raises. A code↔doc divergence, not a stale comment: the behavior a caller observes (silent no-op) is the opposite of what the docstring promises (an exception). | `systems/factions/sim/treaty.py:10` (docstring: "still raises"); `systems/factions/sim/treaty.py:27` (entry-point summary: "raises"); `systems/factions/sim/treaty.py:113-118 stub_resolve` (actual behavior) |
| `scene.battle_concluded` and `da.public_governance` are emitted into the Key log every Conquest / successful Territory Transfer, but no live subscriber consumes either type. `articulation.py`'s `_TRIGGER_TYPE_IDS` (the only Key-subscription callback registry found in this trace) lists 13 other types and neither of these two; the in-code comments citing "FOUR consumers" / "consumed by faction_layer" point at `references/key_graph.json` declarations, not runtime wiring. Both emissions are explicitly log-only (no `apply=`) so this is inert telemetry, not a silent behavior gap — but it is a declared-vs-wired divergence. | `systems/factions/sim/faction_action.py:459 _emit_battle_concluded`; `engine/cross_scale/articulation.py:116-130 _TRIGGER_TYPE_IDS` (neither type present) |
| `faction_take_action`'s return value (a dispatch-description string like `'Conquest:Success'`) is computed by every branch but discarded at the only call site — no logging, no telemetry counter, no test assertion reads it in production code. | `engine/mc_v18.py:130 faction_take_action` |
| `Territory.entry_terms_l_seed` is written as a bare dynamic attribute on a `Territory` dataclass instance that declares no such field — self-documented in the source as "a forward-compatible, golden-inert proxy... read by nothing yet." Confirmed: no read of `entry_terms_l_seed` found anywhere in `systems/` or `engine/`. | `systems/factions/sim/faction_action.py:486-489 entry_terms_l_seed`; `engine/autoload/game_state.py:141-151 Territory` (field not declared) |
| `world.casus_belli`, the optional duck-typed ledger `parliamentary_transfer._available_cb` reads to find non-Crown CB sources, has ZERO production writers, for two distinct reasons: the Crown-restoration source is appended only to `_available_cb`'s own LOCAL `sources` list, never to `world.casus_belli` itself; and `propose_transfer`'s Partial-outcome CB grant only extends the ledger when it is already a populated dict, so it cannot create the ledger either. Every `_MODE_CB` entry (`military`, `negotiated_agreement`, `excommunication`, `treaty_violation`, `crisis_stability`, etc., including the two sources reasoned about above) is therefore currently unreachable in a fresh campaign. | `systems/factions/sim/parliamentary_transfer.py:103-113 _available_cb`; `systems/factions/sim/parliamentary_transfer.py:109 sources` (local list, not the ledger); `systems/factions/sim/parliamentary_transfer.py:303-304 ledger` (gated on pre-existing dict); `systems/factions/sim/parliamentary_transfer.py:68-76 _MODE_CB` |
| **The unique→conquest→muster→govern dispatch is a compound cascade, not the one-step fall-throughs S2.4.3/S2.6 each individually record.** The three `if roll < cum_X:` blocks at S2.4/S2.5/S2.6 are independent, not `elif`; because the cumulative thresholds are non-decreasing, a roll landing in an early bucket whose branch returns the sentinel falls through every remaining bucket in turn to the S2.7 call, which is unconditional and whose return is never checked by its caller. `_try_govern` itself returns the same sentinel when the acting faction holds no territories, or when the rolled target territory is missing or its owner doesn't match the faction — so the top-level dispatch can surface the bare sentinel string as if it were a real outcome. This is a real, currently-unreachable latent defect: the caller gate skips any faction that is non-parliamentary or holds no territories, and both live territory-transfer sites keep `Faction.territories` and `Territory.owner` in sync on every transfer; the one write site that desyncs the two has zero production callers. Safety here lives in the caller-side gate, not a guard inside the resolver. | `systems/factions/sim/faction_action.py:87 _NOOP`; `systems/factions/sim/faction_action.py:223 _try_faction_unique`; `systems/factions/sim/faction_action.py:230 _try_conquest`; `systems/factions/sim/faction_action.py:236 _try_muster`; `systems/factions/sim/faction_action.py:242 _try_govern`; `systems/factions/sim/faction_action.py:534 territories`; `systems/factions/sim/faction_action.py:538 owner`; `engine/mc_v18.py:125 parliamentary`; `engine/mc_v18.py:127 territories`; `systems/factions/sim/mass_seizure.py:292 owner` |
| The L2 map declares `faction_state` as not executing, contradicted by the seeded execution trace, which records calls into this contract in every traced phase (boot, loop.s1, loop.s2.factions, loop.s2.parliament, loop.s3). | `references/execution_map.json:595 executes`; `references/execution_trace.json:33 faction_state`; `references/execution_trace.json:36 faction_state`; `references/execution_trace.json:39 faction_state`; `references/execution_trace.json:43 faction_state`; `references/execution_trace.json:49 faction_state` |
| `faction_action` is this subsystem's sole code-layer cut-vertex — removing it disconnects the import graph. | `audit/2026-08-06-vector-audit/structure_audit/data/structure_metrics.json:100 faction_action` |
| `faction_state` sits in an L2 contract-layer cycle with `npc_behavior`, `piety_track` and `social_contest`. | `audit/2026-08-06-vector-audit/structure_audit/data/structure_metrics.json:337 faction_state` |
| `coronation_renewal_prereq`'s docstring asserts Coronation is blocked when Crown is both excommunicated and the Church just attempted an excommunication this same season; the body implements no such check — it only tests whether `church` is present and parliamentary. | `systems/factions/sim/crown_initiative.py:193-208 coronation_renewal_prereq` |
| Mass-battle resolution for Conquest always passes a permanent placeholder for terrain, never a real value. | `systems/factions/sim/faction_action.py:436 terrain` |
