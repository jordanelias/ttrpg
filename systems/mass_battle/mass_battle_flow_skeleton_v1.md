# Mass battle — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/mass_battle/` · **Lane:** `MB` · **Contracts:** `mass_battle`
**Code roots traced:** `systems/mass_battle/sim/` (the canon engine plus the strategic adapter) ·
the calling chain through `systems/factions/sim/faction_action.py` and `engine/mc_v18.py`.
**Traced at:** `dcf38ef`

> **RETRACED 2026-08-24 — THERE IS ONE TREE NOW, AND THE TWO-TREE FRAME THIS DOCUMENT WAS BUILT ON
> IS GONE.** Until the mass-battle engine swap (`dcf38ef`) this subsystem held two disjoint
> codebases: TREE A, the 1,905-line `systems/mass_battle/sim/massbattle.py` that carried the
> campaign's only battle seam, and TREE B, the 11,342-line cell-scale engine living under
> `tests/sim/mass_battle/` and ruled canon by Jordan (J2, 2026-08-03) while being unreachable from
> the campaign. The swap deleted TREE A's engine and moved TREE B to `systems/mass_battle/sim/`, so
> the canon engine is now the one the campaign runs.
>
> **What survived is the ADAPTER, and it is a different thing from the engine.**
> `systems/mass_battle/sim/massbattle.py` is now 146 lines: `resolve_mass_battle`,
> `_faction_to_unit`, the garrison stub and the size-ratio → degree map. Those four existed only in
> TREE A and `systems/factions/sim/faction_action.py` imports the first by that exact path, so they
> were carried over field-for-field rather than deleted. §3 below is therefore split by ROLE —
> adapter, then engine — not by tree, and the old TREE A per-tick steps are gone because the code
> they described is gone. §7 records which of this document's gaps the swap CLOSED, because a gap
> that has been closed by deletion is not a gap and leaving it here would be the exact drift this
> format exists to prevent.

## 1. Entry points

| Callable | Anchor | Called-by |
|---|---|---|
| **ADAPTER** (`systems/mass_battle/sim/massbattle.py`, 146 lines — strategic seam only) | | |
| `resolve_mass_battle(faction_a, faction_b, terrain, world)` | `systems/mass_battle/sim/massbattle.py:99 resolve_mass_battle` | `systems/factions/sim/faction_action.py:461 resolve_mass_battle` (import) → `:433` (call) |
| `_faction_to_unit(faction)` | `systems/mass_battle/sim/massbattle.py:63 _faction_to_unit` | `systems/mass_battle/sim/massbattle.py:115 _faction_to_unit` (and `:120`, `:122`) |
| **ENGINE** (`systems/mass_battle/sim/`, the canon cell-scale engine) | | |
| `orchestration.run_battle(unit_a, unit_b, max_turns)` | `systems/mass_battle/sim/orchestration.py:1749 run_battle` | (a) `systems/mass_battle/sim/engine.py:520 run_battle` (router branch); (b) `tests/valoria/test_deployment_geometry.py:183 run_battle` |
| `orchestration.run_multi_turn_battle(unit_a, unit_b, shape_a, shape_b, anchor_map, max_battle_turns)` | `systems/mass_battle/sim/orchestration.py:2364 run_multi_turn_battle` | (a) `systems/mass_battle/sim/engine.py:522 run_multi_turn_battle` (router branch); (b) `tests/valoria/test_deployment_geometry.py:107 run_multi_turn_battle` |
| `orchestration.run_multi_unit_battle(side_a, side_b, pairings, shapes_a, shapes_b, anchor_map, max_battle_turns)` | `systems/mass_battle/sim/orchestration.py:2565 run_multi_unit_battle` | (a) `systems/mass_battle/sim/engine.py:524 run_multi_unit_battle` (router branch); (b) `tests/valoria/test_reserve_commit.py:42 run_multi_unit_battle` |
| `engine.resolve_battle(*args, kind='multi', **kwargs)` | `systems/mass_battle/sim/engine.py:512 resolve_battle` | `systems/mass_battle/sim/workbench/trace.py:89 resolve_battle` (and `:92`) |
| `engine.build_unit` / `build_army` / `build_envelopment` / `build_refused_flank` | `systems/mass_battle/sim/engine.py:176 build_unit`, `:213 build_army`, `:355 build_envelopment`, `:452 build_refused_flank` | `systems/mass_battle/sim/bat.py:47 build_unit`, `:74 build_envelopment`, `:86 build_refused_flank`; `tests/sim/gauge_mb.py:162 build_army` |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| **ADAPTER** | | | |
| `faction_a` (attacker; has `.name`, `.Mil`) | arg | `systems/factions/sim/faction_action.py:464 faction_a` (the calling faction) | `systems/factions/sim/faction_action.py:463-468` |
| `faction_b` (defender, or `None`) | arg | `systems/factions/sim/faction_action.py:462 defender_faction` (`world.factions.get(t.owner)`) | `systems/factions/sim/faction_action.py:462` |
| `terrain` | arg | hardcoded `None` at the call site (deferred) | `systems/factions/sim/faction_action.py:466` |
| `world` (for `world.rng`) | world-state | `systems/factions/sim/faction_action.py:453 world` | `systems/mass_battle/sim/massbattle.py:124 rngsource` |
| **ENGINE** | | | |
| `unit_a`, `unit_b` (`Unit` dataclass instances) | arg | constructed by `engine.build_unit`/`build_army`/`build_envelopment`/`build_refused_flank` | `systems/mass_battle/sim/engine.py:176-509` |
| `shape_a`, `shape_b`, `anchor_map` | arg | caller-supplied deployment geometry | `systems/mass_battle/sim/orchestration.py:2364-2421 run_multi_turn_battle` |
| `pairings`, `shapes_a`, `shapes_b` | arg | caller-supplied multi-unit roster | `systems/mass_battle/sim/orchestration.py:2565-2869 run_multi_unit_battle` |
| `max_turns` / `max_battle_turns` | param (default) | function signature default | `systems/mass_battle/sim/orchestration.py:1749 run_battle`, `:2358 run_multi_turn_battle` |
| engine mode toggles read from `os.environ` at import time (`PER_CELL`, `LANCHESTER_ENABLED`, `REFORM_CHECK_ENABLED`, `PC_RESERVE_COMMIT`, and dozens more) | flag | env var, defaulted | `systems/mass_battle/sim/config.py:332 PER_CELL`, `systems/mass_battle/sim/config.py:400 LANCHESTER_ENABLED`, `systems/mass_battle/sim/orchestration.py:294 REFORM_CHECK_ENABLED`, `systems/mass_battle/sim/config.py:248 PC_RESERVE_COMMIT` |
| `CASCADING_ENABLED` | flag | hardcoded module constant, not env-read (see §7) | `systems/mass_battle/sim/config.py:143 CASCADING_ENABLED` |

## 3. Flow

### ADAPTER — `systems/mass_battle/sim/massbattle.py` (the live campaign seam)

> This branch used to carry TREE A's whole per-tick battle loop (steps S2.1–S2.14). That engine was
> DELETED by the 2026-08-24 swap, so those steps are gone rather than re-anchored: the flow they
> described is the one the ENGINE branch below describes, and it is now the flow the campaign
> actually runs. What remains here is the strategic seam and nothing else.

- **S0.1** `[gate]` the campaign action roll: the mass-battle path is reached only if `roll < cum_conquest` selects Conquest for this faction's turn, ahead of `_try_conquest`. `systems/factions/sim/faction_action.py:260`
- **S0.2** `[gate]` `_try_conquest` no-ops (`return _NOOP`, no battle) if the faction has no reachable `targets`. `systems/factions/sim/faction_action.py:453-454`. The former `faction.Mil >= CONQUEST_MIN_MIL` half of this gate was DELETED 2026-08-14 (Jordan ruling), so low-Military factions now reach the battle engine rather than being filtered before it.
- **S1** `resolve_mass_battle` constructs `unit_a` from `faction_a` via `_faction_to_unit`; `[branch]` if `faction_b` is `None`, constructs `unit_b` from a synthetic `_GarrisonStub` at `Mil=1.5`, else from `faction_b`. `systems/mass_battle/sim/massbattle.py:115-122 _faction_to_unit`
  - **S1.1** the constructed `Unit` is the pre-port adapter's minimum-viable default and is CARRIED OVER FIELD-FOR-FIELD: one `Line`/`infantry` subunit at `tier=2`, `command=4`, `discipline=5`, `morale=5`, `power=round(faction.Mil)`. `systems/mass_battle/sim/massbattle.py:63 _faction_to_unit`. It is a recorded `[GAP]`, not canon — see §7.
- **S2** `[emit]` `run_battle(unit_a, unit_b, max_turns=18)` — the canon engine's single-encounter orchestrator. Multi-turn and multi-unit orchestration exist in the engine and are NOT invoked from this path. `systems/mass_battle/sim/massbattle.py:126 run_battle`
  - **S2.1** `[gate]` the whole call is scoped by `rngsource.using(world.rng)`, so the engine's module-global `random` draws resolve against the campaign's seeded generator instead of the process-global one. Without this the seeded campaign goldens would be unpinnable rather than merely moved. `systems/mass_battle/sim/massbattle.py:124 rngsource`, `systems/mass_battle/sim/rngsource.py:1`
  - **S2.2** the per-tick flow itself is the ENGINE branch below, entered at `run_battle`. `systems/mass_battle/sim/orchestration.py:1749 run_battle`
- **S3** `[branch]` `resolve_mass_battle` computes `a_size_pct`/`b_size_pct` from `effective_size`/`size_max`, derives `attacker_wins`, then maps to one of four `degree` strings via nested threshold checks. `systems/mass_battle/sim/massbattle.py:128-139`
  - **S3.1** `[gap]` those thresholds are a bespoke post-hoc classification of survivor ratios, NOT the canonical margin-based degree ladder (`engine/autoload/dice_engine.py degree_from_net`). They were carried over verbatim so the engine swap stayed a single-variable experiment; reconciling the two ladders is open MB-lane work. `systems/mass_battle/sim/massbattle.py:46 OVERWHELMING_ATTACKER_MIN`
- **S4** returns `{attacker_wins, degree, attacker_size_pct, defender_size_pct}`. `systems/mass_battle/sim/massbattle.py:141-146`

Continuing in the caller (`_try_conquest`, outside this subsystem's own folder but the only place
the return value is consumed):

- **S5** `[emit]` `_emit_battle_concluded` builds and emits a `scene.battle_concluded` Key — additive only (no `apply=`), silently no-ops if `world.echo_scheduler` is absent. `systems/factions/sim/faction_action.py:489 _emit_battle_concluded`, body at `:321-397`
- **S6** `[branch]` `if battle['attacker_wins']`: territory ownership transfer, loser `L` penalty, then `[branch]` Terms (`degree == 'Success'`) vs Storm (otherwise) settlement-side fork, then `world.battle_count += 1`. `systems/factions/sim/faction_action.py:491-527`

### ENGINE — `systems/mass_battle/sim/` (the canon cell-scale engine; reached from S2 above)

- **S1** `[gate]` `engine.resolve_battle(*args, kind=..., **kwargs)` routes to one of three orchestrators by `kind` — `'single'` → `run_battle`, `'multi'` → `run_multi_turn_battle`, `'multi_unit'` → `run_multi_unit_battle` — a pure pass-through router, byte-exact to calling the target directly. `systems/mass_battle/sim/engine.py:512-525 resolve_battle`
- **S2** `orchestration.run_battle(unit_a, unit_b, max_turns)` — one engagement turn, phase-bounded by `TICKS_PER_PHASE`:
  - **S2.1** `[gate]` `assert (not FIELD_MOVEMENT) or PC_NODE_COHESION` — invalid mode combination fails loudly. `systems/mass_battle/sim/orchestration.py:1758-1759`
  - **S2.2** `_draw_friction_cev` drawn once per unit per battle (lazy, first-entry-only). `systems/mass_battle/sim/orchestration.py:1767-1768`
  - **S2.3** `[loop]` per tick `t` in `1..max_turns`: `[gate]` break if either unit routed. `systems/mass_battle/sim/orchestration.py:1777-1780`
  - **S2.4** `volley_phase(unit_a, unit_b)` — ranged damage accumulated. `systems/mass_battle/sim/orchestration.py:1564 volley_phase`
  - **S2.5** pre-movement contact halt via `find_contacts`. `systems/mass_battle/sim/orchestration.py:1795 find_contacts`
  - **S2.6** `check_orders` (both units) then `assign_targets`. `systems/mass_battle/sim/orchestration.py:1831-1833` (check_orders, assign_targets)
  - **S2.7** escort/formation-relative positioning pass (centroid caching, escort-engage latch). `systems/mass_battle/sim/orchestration.py:1840-1880`
  - **S2.8** `[write]` per-atom `advance_cells` for atoms with a target or an unengaged escort assignment, both sides. `systems/mass_battle/sim/orchestration.py:1911-1918`
  - **S2.9** `[branch]` `[gate]` `FIELD_MOVEMENT`-gated cross-side time-of-impact resolution (`resolve_toi_and_commit`) — a TREE-B-only branch with no TREE A counterpart. `systems/mass_battle/sim/orchestration.py:1934-1935`
  - **S2.10** `halt_before_enemy` on both sides' atoms. `systems/mass_battle/sim/orchestration.py:1937-1938`
  - **S2.11** `resolve_cross_side_contention(unit_a, unit_b)` resolves cells two sides both moved into. `systems/mass_battle/sim/orchestration.py:1945`
  - **S2.12** post-movement `find_contacts` → `pairs`, then per-atom stamina drain proportional to cells in contact. `systems/mass_battle/sim/orchestration.py:1950-1971`
  - **S2.13** `[branch]` `resolve_engagements_cascading` if `CASCADING_ENABLED` else `resolve_engagements`. `systems/mass_battle/sim/orchestration.py:1972-1974`
  - **S2.14** `[write]` volley + engagement damage applied simultaneously to `unit_a.hp`/`unit_b.hp`; `[branch]` `PER_CELL` on routes damage through the per-column grid (`distribute_casualties_cellwise`/`apply_to_subunit`) instead of the aggregate `distribute_casualties`. `systems/mass_battle/sim/orchestration.py:2064-2065`, `systems/mass_battle/sim/orchestration.py:2079-2122`
  - **S2.15** `recalc_size()` both units; `check_drift()` on non-routed/non-broken units. `systems/mass_battle/sim/orchestration.py:2123-2130`
  - **S2.16** `[gate]` `command <= 0` forces `set_morale(0.0)` (instant rout path). `systems/mass_battle/sim/orchestration.py:2141-2143`
  - **S2.17** `[gate]` subunit-level rout check (`eff_morale <= 0` or `troop_total() < SUBUNIT_ROUT_FLOOR`), then `derive_rout()` per unit. `systems/mass_battle/sim/orchestration.py:2153-2161`
  - **S2.18** `[branch]` every `TICKS_PER_PHASE` ticks: `phase_boundary(unit_a, unit_b, current_phase)`. `systems/mass_battle/sim/orchestration.py:2163-2166`
    - **S2.18.1** fixed call order: `stamina_check` → `discipline_check_phase` → `morale_check_phase` → `rout_resolution` → `rally_check` → `reform_check` → `threadwork_check`. `systems/mass_battle/sim/orchestration.py:339-345`
    - **S2.18.2** `[gate]` `rally_check` and `threadwork_check` are empty hooks (`pass`); `reform_check` is implemented and flag-gated on `REFORM_CHECK_ENABLED` (default ON). `systems/mass_battle/sim/orchestration.py:287-289`, `systems/mass_battle/sim/orchestration.py:296-330`, `systems/mass_battle/sim/orchestration.py:332-334`
  - **S2.19** loop end: `winner` from final `routed` flags; returns a result dict. `systems/mass_battle/sim/orchestration.py:2166-2176`
- **S3** `orchestration.run_multi_turn_battle(unit_a, unit_b, shape_a, shape_b, anchor_map, max_battle_turns)`:
  - **S3.1** `[loop]` per `battle_turn` in `1..max_battle_turns`: `reset_positions` both units, then call `run_battle(unit_a, unit_b)` (persistent unit state across turns). `systems/mass_battle/sim/orchestration.py:2368-2374`
  - **S3.2** `[gate]` break if either unit routed after the turn; else `between_turn_recovery` both units. `systems/mass_battle/sim/orchestration.py:2393-2398`
  - **S3.3** loop end: winner derived from routed flags; returns a result dict with per-turn `log`. `systems/mass_battle/sim/orchestration.py:2400-2414`
- **S4** `orchestration.run_multi_unit_battle(side_a, side_b, pairings, shapes_a, shapes_b, anchor_map, max_battle_turns)`:
  - **S4.1** `[branch]` `[gate]` `PC_RESERVE_COMMIT`: pairs whose unit is in Reserve are benched out of `active_pairs` at start. `systems/mass_battle/sim/orchestration.py:2587-2591`
  - **S4.2** `[loop]` per `battle_turn`: reserve-commit check (benched pairs re-activate at their commit turn). `systems/mass_battle/sim/orchestration.py:2606-2611`
  - **S4.3** pursuit-phase resolution for units already pursuing a routed enemy (`recall_check` gate, else `pursuit_damage`). `systems/mass_battle/sim/orchestration.py:2616-2651`
  - **S4.4** `[loop]` each active pair: `reset_positions` then `run_battle(ua, ub)`. `systems/mass_battle/sim/orchestration.py:2655-2670`
  - **S4.5** freed-attacker bonus damage against an adjacent enemy, from units freed on a previous turn. `systems/mass_battle/sim/orchestration.py:2674-2719`
  - **S4.6** `[gate]` newly-routed detection this turn. `systems/mass_battle/sim/orchestration.py:2722-2730`
  - **S4.7** morale-cascade + rout-contagion applied to adjacent friendly units of each newly-routed unit (`discipline_check_cascade` gate, then `cascade_morale_hit`). `systems/mass_battle/sim/orchestration.py:2732-2774`
  - **S4.8** `[branch]` victor of a resolved pair becomes a pursuer (`Fast` speed) or a freed attacker (otherwise). `systems/mass_battle/sim/orchestration.py:2778-2807`
  - **S4.9** `[gate]` termination: mutual rout, or no active pairs/pursuit/reserve remaining → break; else `between_turn_recovery` on all non-routed units. `systems/mass_battle/sim/orchestration.py:2824-2840`
  - **S4.10** loop end: winner by surviving-unit count; returns a result dict with per-turn `log` and per-unit casualties. `systems/mass_battle/sim/orchestration.py:2842-2862`

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| **ADAPTER** | | | |
| `{attacker_wins, degree, attacker_size_pct, defender_size_pct}` | dict (return) | `systems/factions/sim/faction_action.py:469 deg`, `:461 battle['attacker_wins']` | `systems/mass_battle/sim/massbattle.py:141-146` |
| `scene.battle_concluded` Key | emit (additive-only, no `apply=`) | `world.echo_scheduler` when attached; 4 declared consumers per `references/key_graph.json` per docstring (not independently re-verified here) | `systems/factions/sim/faction_action.py:424` (sched.emit(key)) |
| **ENGINE** | | | |
| `{winner, turns, phases, tick_in_phase, a_stamina, b_stamina, a_hp_pct, b_hp_pct, a_morale, b_morale, truncated_groups, truncated_pairs, truncated_troops, max_groups}` | dict (return) | `run_multi_turn_battle` (`:2374`), `run_multi_unit_battle` (`:2666`), test callers | `systems/mass_battle/sim/orchestration.py:2166-2182` |
| `{winner, battle_turns, log, a_loss_final, b_loss_final}` | dict (return) | `tests/sim/gauge_mb.py`, `tests/valoria/test_deployment_geometry.py`, `test_friction_cev.py` | `systems/mass_battle/sim/orchestration.py:2408-2414` |
| `{winner, battle_turns, log, a_surviving, b_surviving, a_casualties, b_casualties}` | dict (return) | `tests/valoria/test_reserve_commit.py:42` | `systems/mass_battle/sim/orchestration.py:2852-2862` |
| trace events (`tick`/`melee`/`volley`/`positions`) | emit (opt-in via `start_trace(True)`) | `systems/mass_battle/sim/workbench/trace.py:78 get_trace`, served by `workbench/server.py`'s `/api/trace` | `systems/mass_battle/sim/orchestration.py:1786 trace_event` |
| `MECHANICS` registry (`mechanic -> {fn, toggle, source, status}`) | registry | self-test (asserts every entry resolves); audit tooling | `systems/mass_battle/sim/engine.py:38 MECHANICS` |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| **ADAPTER** | | | |
| `unit.effective_size` / `unit.size_max` | R | `systems/mass_battle/sim/hierarchy/units.py` (`Unit`) | read `systems/mass_battle/sim/massbattle.py:128-129` |
| `unit.routed` | R | `systems/mass_battle/sim/hierarchy/units.py` (`Unit`) | read `systems/mass_battle/sim/massbattle.py:130` |
| `world.rng` | R | caller (`GameState`, outside this subsystem) | `systems/mass_battle/sim/massbattle.py:124 rngsource` |
| the engine's active RNG holder | RW | `systems/mass_battle/sim/rngsource.py` (this subsystem) | `systems/mass_battle/sim/rngsource.py:1` |
| `world.battle_count` | W | `systems/factions/sim/faction_action.py` (outside this subsystem's own folder — see §6) | `systems/factions/sim/faction_action.py:525` |
| **ENGINE** | | | |
| `unit.hp` | RW | `systems/mass_battle/sim/hierarchy/units.py` (`Unit`) | write `systems/mass_battle/sim/orchestration.py:2064-2065` |
| `unit.morale` | RW | `systems/mass_battle/sim/hierarchy/units.py` (`Unit.set_morale`, `Unit.cascade_morale_hit`) | `systems/mass_battle/sim/hierarchy/units.py:2467 set_morale` |
| `unit.routed` / `atom.routed` | RW | `systems/mass_battle/sim/hierarchy/units.py` (`Unit.derive_rout`) | `systems/mass_battle/sim/hierarchy/units.py:2450 derive_rout`; write site `systems/mass_battle/sim/orchestration.py:2154-2161` |
| `unit.stamina` | RW | `systems/mass_battle/sim/hierarchy/units.py` (`Subunit.drain_stamina`) | `systems/mass_battle/sim/hierarchy/units.py:710 drain_stamina` |
| `unit.col_grid` (per-column grid, `PER_CELL` only) | RW | `systems/mass_battle/sim/percell.py` | `systems/mass_battle/sim/orchestration.py:2126-2127 sync_col_grid` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| up | `engine/mc_v18.py` (campaign driver) | `run_campaign` → `run_season(action_callback=_faction_actions_callback)` | `engine/mc_v18.py:220 run_campaign`, `:267 run_season` |
| lateral | `systems/overview/sim/season.py` | `run_season`'s Step 2 invokes the passed `action_callback(world)` | `systems/overview/sim/season.py:70-71` (action_callback(world)) |
| lateral | `systems/factions/sim/faction_action.py` (FA lane) | `_faction_actions_callback` → `faction_take_action` → `_try_conquest` → `resolve_mass_battle` (the ADAPTER) — the one live faction-scale battle call, reached only past the action-roll gate and the targets gate (S0.1–S0.2), and from there into the canon engine | `engine/mc_v18.py:130 faction_take_action`; `systems/factions/sim/faction_action.py:261 _try_conquest`, `:431-438 resolve_mass_battle` |
| down | `engine/substrate/keys.py` | `_try_conquest` emits `scene.battle_concluded` off the battle result, additive-only | `systems/factions/sim/faction_action.py:382` (from engine.substrate.keys import ..., :361 key =) |
| — | `systems/social_contest/sim/contest/wrapper.py` | comment-only reference ("Mirrors mass_battle.engine") — not an import, no runtime coupling | `systems/social_contest/sim/contest/wrapper.py:4`, `systems/social_contest/sim/contest/wrapper.py:290` |
| — (none outward) | `engine/`, other `systems/*` | The ENGINE half imports nothing from `engine.` and nothing from another `systems/` subsystem: it operates on `Unit`/`Subunit` dataclasses alone. The coupling is one-directional and lives entirely in the ADAPTER, which is what let the engine be swapped underneath the campaign without touching a caller. | `systems/mass_battle/sim/massbattle.py:33-35 rngsource` (the adapter's only three imports, all in-subsystem) |

## 7. Traced gaps

> **SIX OF THIS SECTION'S ROWS WERE CLOSED BY DELETION on 2026-08-24 and are recorded below as
> closed rather than dropped silently.** All six were true statements about TREE A, and TREE A's
> engine no longer exists. A gap that no longer has a subject is not a gap; leaving it stated would
> make this document assert defects in code that cannot be read.

| Gap | Evidence |
|---|---|
| **`_faction_to_unit`'s mapping is unspecified, and this is the live one.** No canonical spec exists for turning a strategic faction into a cell-scale `Unit`. The adapter builds one `Line`/`infantry` subunit at `tier=2`, `command=4`, `discipline=5`, `morale=5`, `power=round(faction.Mil)` — the pre-port defaults, carried over field-for-field so the engine swap stayed single-variable. The canon engine can express troop types, equipment, formations, multi-subunit hierarchies and orders of battle; the campaign uses none of them, because what a faction's army IS at the strategic scale is an unanswered design question, not a wiring gap. | `systems/mass_battle/sim/massbattle.py:63 _faction_to_unit`; `systems/mass_battle/sim/massbattle.py:70-75` (the recorded `[GAP]`) |
| **The adapter's degree map is not the canonical degree ladder.** `resolve_mass_battle` classifies a finished battle by survivor-size ratio through three bespoke thresholds; the game's ladder (`degree_from_net`) is margin-based. Both are live, they disagree by construction, and nothing reconciles them. Carried over verbatim rather than fixed, so the swap measured the resolution model and nothing else. | `systems/mass_battle/sim/massbattle.py:46 OVERWHELMING_ATTACKER_MIN`; `systems/mass_battle/sim/massbattle.py:132-139` |
| **Multi-turn and multi-unit orchestration is unreached from the campaign.** The engine implements `run_multi_turn_battle` and `run_multi_unit_battle`; `resolve_mass_battle` calls only single-encounter `run_battle`. Their only callers are tests. This is now a DELIBERATE scope statement rather than dead code — the orchestrators are the canon engine's and are exercised — but the campaign does not reach them. | `systems/mass_battle/sim/massbattle.py:126 run_battle`; `systems/mass_battle/sim/orchestration.py:2364 run_multi_turn_battle`, `:2559 run_multi_unit_battle` |
| **Two never-wired modules survive the port.** `tactic_cards.py`'s `FACTION_TACTIC_CARD_POOL_MODIFIERS` is an empty dict reserving a name and import path; `altonian_reinforcements.py`'s `invoke_altonian_reinforcements` raises `NotImplementedError` unconditionally, and a guard test asserts it must keep doing so until MB's own migration converts it. | `systems/mass_battle/sim/tactic_cards.py:23`; `systems/mass_battle/sim/altonian_reinforcements.py:20-21 invoke_altonian_reinforcements`; `engine/tests/test_pipeline_reach.py:810-821 test_only_accepted_handoff_still_raises_unconditionally` |
| **`CASCADING_ENABLED` is a hardcoded `True` module constant, not an env-read flag** — despite `config.py` being otherwise env-var-driven for its toggles (§2). The `else resolve_engagements(...)` branch is therefore unreachable without a source edit. | `systems/mass_battle/sim/config.py:143 CASCADING_ENABLED` |
| **`rally_check` and `threadwork_check` are empty stub hooks** called unconditionally by `phase_boundary` every phase; `reform_check` is implemented and flag-gated on `REFORM_CHECK_ENABLED` (default ON). The Thread→Mass handoff `handoff_rules.py` describes has no execution path from the mass-battle side. | `systems/mass_battle/sim/orchestration.py:288-290 rally_check`, `:333-335 threadwork_check`, `:296-330 reform_check`; call site `systems/mass_battle/sim/orchestration.py:337 phase_boundary` |
| **Registries have not caught up.** `registers/mechanics_index.yaml`'s `mass_battle` entry points `sim_module: systems/mass_battle/sim/massbattle.py`, which is now the 146-line ADAPTER rather than the engine — the path is still correct as the subsystem's entry point and now UNDER-describes it. `references/module_contracts.yaml`'s `mass_battle` entry omits `sim_module` entirely (marked "undeclared", awaiting an MB-lane add), which is why this subsystem is absent from `references/execution_trace.json`'s by-unit attribution despite dominating the call profile. | `registers/mechanics_index.yaml:484-507`; `references/module_contracts.yaml:700-726` |

### Closed by the 2026-08-24 engine swap

| Was | Why it is closed |
|---|---|
| *"The two trees are disjoint and both alive for different reasons."* | There is one tree. TREE A's engine was deleted; the canon engine moved into `systems/mass_battle/sim/` and the campaign reaches it through the adapter. |
| *"TREE A's multi-turn/multi-unit orchestrators are dead code."* | Those functions were deleted with TREE A. The surviving orchestrators are the canon engine's and have test callers — restated as a scope row above, not a dead-code row. |
| *"The two trees disagree on the primary rout driver."* | There is no second tree to disagree with. Rout is whatever the canon engine does: phase-boundary `morale_check_phase` plus the subunit floor check, with no per-tick erosion term. |
| *"TREE A's `Unit`/`Subunit` split is a test-pinned circular import."* | `systems/mass_battle/sim/units.py` no longer exists and the tail-import cycle went with it. The adapter imports `Subunit`/`Unit` from `hierarchy/units.py` at the top of the file like any other module. |
| *"TREE B never touches campaign world-state"* (as a reason it could not receive the seam) | Still true of the engine, and no longer a blocker: the adapter is the thing that touches world-state, and it is the whole of the coupling. Restated as a §6 seam row. |
| *the J2 provenance banner that stood in this subsystem's `sim/__init__.py`* | That file is now empty. The J2 narrative it carried is in this document's header and in `references/restructure_ledger.md`. |
