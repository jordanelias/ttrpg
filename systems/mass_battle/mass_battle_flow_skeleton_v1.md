# Mass battle — Flow Skeleton v1

## Status: REFERENCE — traced structure only (no design content, no infill)

> Skeleton: base logical flow only. No mechanics, no numbers, no prose infill.
> Every claim carries a `path:line symbol` anchor. Guard: `tests/valoria/test_flow_skeletons.py`.

**Subsystem:** `systems/mass_battle/` · **Lane:** `MB` · **Contracts:** `mass_battle`
**Code roots traced:** `systems/mass_battle/sim/` (5 modules — TREE A, retired-but-live-seam) ·
`tests/sim/mass_battle/` (28 modules — TREE B, canon per J2) · the calling chain through
`systems/factions/sim/faction_action.py` and `engine/mc_v18.py` · the seam guard
`tests/valoria/test_j2_mass_battle_seam.py`.
**Traced at:** `6545067`

> **Two disjoint trees, traced separately.** `systems/mass_battle/sim/` (TREE A) is the only
> code this subsystem owns under its own folder and is the campaign's sole faction-scale battle
> seam. `tests/sim/mass_battle/` (TREE B) is a *different* codebase living under `tests/`, ruled
> canon by Jordan (J2, 2026-08-03), unit/cell-scale, and — per Standing Rule 1 — traced here
> because "trace where the code is, not where the folder is." §3 below carries them as two
> top-level branches; §7 carries the disjointness itself.

## 1. Entry points

| Callable | Anchor | Called-by |
|---|---|---|
| **TREE A** (`systems/mass_battle/sim/`) | | |
| `resolve_mass_battle(faction_a, faction_b, terrain, world)` | `systems/mass_battle/sim/massbattle.py:1791 resolve_mass_battle` | `systems/factions/sim/faction_action.py:451 resolve_mass_battle` (import) → `:433` (call) |
| `run_battle(unit_a, unit_b, max_turns, rng)` | `systems/mass_battle/sim/massbattle.py:1127 run_battle` | (a) `systems/mass_battle/sim/massbattle.py:1831 run_battle` (from `resolve_mass_battle`); (b) `tests/valoria/test_mass_battle_systems_movement.py:51 run_battle` |
| `run_multi_turn_battle(unit_a, unit_b, shape_a, shape_b, anchor_map, max_battle_turns)` | `systems/mass_battle/sim/massbattle.py:1357 run_multi_turn_battle` | `—` (no caller found; see §7) |
| `run_multi_unit_battle(side_a, side_b, pairings, shapes_a, shapes_b, anchor_map, max_battle_turns)` | `systems/mass_battle/sim/massbattle.py:1526 run_multi_unit_battle` | `—` (no caller found; see §7) |
| **TREE B** (`tests/sim/mass_battle/`) | | |
| `orchestration.run_battle(unit_a, unit_b, max_turns)` | `tests/sim/mass_battle/orchestration.py:1742 run_battle` | (a) `tests/sim/mass_battle/engine.py:520 run_battle` (router branch); (b) `tests/valoria/test_deployment_geometry.py:183 run_battle` |
| `orchestration.run_multi_turn_battle(unit_a, unit_b, shape_a, shape_b, anchor_map, max_battle_turns)` | `tests/sim/mass_battle/orchestration.py:2357 run_multi_turn_battle` | (a) `tests/sim/mass_battle/engine.py:522 run_multi_turn_battle` (router branch); (b) `tests/valoria/test_deployment_geometry.py:107 run_multi_turn_battle` |
| `orchestration.run_multi_unit_battle(side_a, side_b, pairings, shapes_a, shapes_b, anchor_map, max_battle_turns)` | `tests/sim/mass_battle/orchestration.py:2558 run_multi_unit_battle` | (a) `tests/sim/mass_battle/engine.py:524 run_multi_unit_battle` (router branch); (b) `tests/valoria/test_reserve_commit.py:42 run_multi_unit_battle` |
| `engine.resolve_battle(*args, kind='multi', **kwargs)` | `tests/sim/mass_battle/engine.py:512 resolve_battle` | `tests/sim/mass_battle/workbench/trace.py:89 resolve_battle` (and `:92`) |
| `engine.build_unit` / `build_army` / `build_envelopment` / `build_refused_flank` | `tests/sim/mass_battle/engine.py:176 build_unit`, `:213 build_army`, `:355 build_envelopment`, `:452 build_refused_flank` | `tests/sim/mass_battle/bat.py:47 build_unit`, `:74 build_envelopment`, `:86 build_refused_flank`; `tests/sim/gauge_mb.py:162 build_army` |

## 2. IN

| Input | Kind | Origin | Anchor |
|---|---|---|---|
| **TREE A** | | | |
| `faction_a` (attacker; has `.name`, `.Mil`) | arg | `systems/factions/sim/faction_action.py:454 faction_a` (the calling faction) | `systems/factions/sim/faction_action.py:453-458` |
| `faction_b` (defender, or `None`) | arg | `systems/factions/sim/faction_action.py:452 defender_faction` (`world.factions.get(t.owner)`) | `systems/factions/sim/faction_action.py:452` |
| `terrain` | arg | hardcoded `None` at the call site (deferred) | `systems/factions/sim/faction_action.py:456` |
| `world` (for `world.rng`) | world-state | `systems/factions/sim/faction_action.py:443 world` | `systems/mass_battle/sim/massbattle.py:1831 world.rng` |
| **TREE B** | | | |
| `unit_a`, `unit_b` (`Unit` dataclass instances) | arg | constructed by `engine.build_unit`/`build_army`/`build_envelopment`/`build_refused_flank` | `tests/sim/mass_battle/engine.py:176-509` |
| `shape_a`, `shape_b`, `anchor_map` | arg | caller-supplied deployment geometry | `tests/sim/mass_battle/orchestration.py:2357-2358 run_multi_turn_battle` |
| `pairings`, `shapes_a`, `shapes_b` | arg | caller-supplied multi-unit roster | `tests/sim/mass_battle/orchestration.py:2558-2559 run_multi_unit_battle` |
| `max_turns` / `max_battle_turns` | param (default) | function signature default | `tests/sim/mass_battle/orchestration.py:1742 run_battle`, `:2358 run_multi_turn_battle` |
| engine mode toggles read from `os.environ` at import time (`PER_CELL`, `LANCHESTER_ENABLED`, `REFORM_CHECK_ENABLED`, `PC_RESERVE_COMMIT`, and dozens more) | flag | env var, defaulted | `tests/sim/mass_battle/config.py:332 PER_CELL`, `tests/sim/mass_battle/config.py:400 LANCHESTER_ENABLED`, `tests/sim/mass_battle/orchestration.py:294 REFORM_CHECK_ENABLED`, `tests/sim/mass_battle/config.py:248 PC_RESERVE_COMMIT` |
| `CASCADING_ENABLED` | flag | hardcoded module constant, not env-read (see §7) | `tests/sim/mass_battle/config.py:143 CASCADING_ENABLED` |

## 3. Flow

### TREE A — `systems/mass_battle/sim/massbattle.py` (the live campaign seam)

- **S0.1** `[gate]` the campaign action roll: the mass-battle path is reached only if `roll < cum_conquest` selects Conquest for this faction's turn, ahead of `_try_conquest`. `systems/factions/sim/faction_action.py:250`
- **S0.2** `[gate]` `_try_conquest` no-ops (`return _NOOP`, no battle) if the faction has no reachable `targets`. `systems/factions/sim/faction_action.py:443-444`. The former `faction.Mil >= CONQUEST_MIN_MIL` half of this gate was DELETED 2026-08-14 (Jordan ruling), so low-Military factions now reach the battle engine rather than being filtered before it.
- **S1** `[gate]` `resolve_mass_battle` constructs `unit_a` from `faction_a` via `_faction_to_unit`; if `faction_b` is `None`, constructs `unit_b` from a synthetic `_GarrisonStub`, else from `faction_b`. `systems/mass_battle/sim/massbattle.py:1817-1822 _faction_to_unit`
- **S2** `[emit]` calls `run_battle(unit_a, unit_b, max_turns, rng=world.rng)` — single-encounter, no multi-turn/multi-unit orchestration invoked from this path. `systems/mass_battle/sim/massbattle.py:1831 run_battle`
  - **S2.1** `[loop]` per-tick loop, `t` in `1..max_turns`: `[gate]` break if either unit already routed. `systems/mass_battle/sim/massbattle.py:1141-1143`
  - **S2.2** `[emit]` `volley_phase(unit_a, unit_b, rng=rng)` — ranged damage accumulated, not yet applied. `systems/mass_battle/sim/massbattle.py:1148 volley_phase`
  - **S2.3** pre-movement contact detection (`find_contacts`) halts atoms already touching the enemy before they advance. `systems/mass_battle/sim/massbattle.py:1152 find_contacts`
  - **S2.4** `assign_targets(unit_a, unit_b)` then per-atom `advance_cells` / `halt_before_enemy`. `systems/mass_battle/sim/massbattle.py:1174 assign_targets`, `:1189 advance_cells`, `:1196-1197 halt_before_enemy`
  - **S2.5** `resolve_cross_side_contention(unit_a, unit_b)` resolves cells two sides both moved into. `systems/mass_battle/sim/massbattle.py:1204 resolve_cross_side_contention`
  - **S2.6** post-movement `find_contacts` recomputes engagement `pairs`. `systems/mass_battle/sim/massbattle.py:1209 find_contacts`
  - **S2.7** `[write]` per-tick stamina drain proportional to cells in contact, both units. `systems/mass_battle/sim/massbattle.py:1211-1222`
  - **S2.8** `[branch]` engagement resolution: `resolve_engagements_cascading` if `CASCADING_ENABLED` else `resolve_engagements` (`CASCADING_ENABLED` is a hardcoded module constant, not env-gated — see §7). `systems/mass_battle/sim/massbattle.py:1223-1225`
  - **S2.9** `[write]` volley + engagement damage applied simultaneously to `unit_a.hp`/`unit_b.hp`, then `recalc_size()` on both. `systems/mass_battle/sim/massbattle.py:1274-1277`
  - **S2.10** `check_drift()` on non-routed, non-broken units. `systems/mass_battle/sim/massbattle.py:1283-1285`
  - **S2.11** `[gate]` morale erosion from total damage; `command <= 0` forces `morale = 0.0` (instant-rout path); otherwise `morale -= erosion`. `systems/mass_battle/sim/massbattle.py:1290-1299`
  - **S2.12** `[gate]` rout check: `morale <= 0` sets `routed = True`. `systems/mass_battle/sim/massbattle.py:1302-1303`
  - **S2.13** `[branch]` every `TICKS_PER_PHASE` ticks: `current_phase += 1` then `phase_boundary(unit_a, unit_b, current_phase)`. `systems/mass_battle/sim/massbattle.py:1306-1308`
    - **S2.13.1** `phase_boundary` fixed call order: `stamina_check` → `discipline_check_phase` → `morale_check_phase` → `rout_resolution` → `rally_check` → `reform_check` → `threadwork_check`. `systems/mass_battle/sim/massbattle.py:308-314`
    - **S2.13.2** `[gate]` `rally_check`, `reform_check`, `threadwork_check` are all empty hooks (`pass`) in this tree — no effect. `systems/mass_battle/sim/massbattle.py:293-303`
  - **S2.14** loop end: `winner` derived from final `routed` flags; returns a result dict. `systems/mass_battle/sim/massbattle.py:1310-1318 run_battle`
- **S3** `[branch]` `resolve_mass_battle` computes `a_size_pct`/`b_size_pct` from `effective_size`/`size_max`, derives `attacker_wins`, then maps to one of four `degree` strings via nested threshold checks. `systems/mass_battle/sim/massbattle.py:1833-1844`
- **S4** returns `{attacker_wins, degree, attacker_size_pct, defender_size_pct}`. `systems/mass_battle/sim/massbattle.py:1846-1851`

Continuing in the caller (`_try_conquest`, outside this subsystem's own folder but the only place
the return value is consumed):

- **S5** `[emit]` `_emit_battle_concluded` builds and emits a `scene.battle_concluded` Key — additive only (no `apply=`), silently no-ops if `world.echo_scheduler` is absent. `systems/factions/sim/faction_action.py:479 _emit_battle_concluded`, body at `:321-397`
- **S6** `[branch]` `if battle['attacker_wins']`: territory ownership transfer, loser `L` penalty, then `[branch]` Terms (`degree == 'Success'`) vs Storm (otherwise) settlement-side fork, then `world.battle_count += 1`. `systems/factions/sim/faction_action.py:481-517`

### TREE B — `tests/sim/mass_battle/` (canon per J2; not reachable from the campaign — see §7)

- **S1** `[gate]` `engine.resolve_battle(*args, kind=..., **kwargs)` routes to one of three orchestrators by `kind` — `'single'` → `run_battle`, `'multi'` → `run_multi_turn_battle`, `'multi_unit'` → `run_multi_unit_battle` — a pure pass-through router, byte-exact to calling the target directly. `tests/sim/mass_battle/engine.py:512-525 resolve_battle`
- **S2** `orchestration.run_battle(unit_a, unit_b, max_turns)` — one engagement turn, phase-bounded by `TICKS_PER_PHASE`:
  - **S2.1** `[gate]` `assert (not FIELD_MOVEMENT) or PC_NODE_COHESION` — invalid mode combination fails loudly. `tests/sim/mass_battle/orchestration.py:1758-1759`
  - **S2.2** `_draw_friction_cev` drawn once per unit per battle (lazy, first-entry-only). `tests/sim/mass_battle/orchestration.py:1767-1768`
  - **S2.3** `[loop]` per tick `t` in `1..max_turns`: `[gate]` break if either unit routed. `tests/sim/mass_battle/orchestration.py:1777-1780`
  - **S2.4** `volley_phase(unit_a, unit_b)` — ranged damage accumulated. `tests/sim/mass_battle/orchestration.py:1784 volley_phase`
  - **S2.5** pre-movement contact halt via `find_contacts`. `tests/sim/mass_battle/orchestration.py:1788 find_contacts`
  - **S2.6** `check_orders` (both units) then `assign_targets`. `tests/sim/mass_battle/orchestration.py:1831-1833` (check_orders, assign_targets)
  - **S2.7** escort/formation-relative positioning pass (centroid caching, escort-engage latch). `tests/sim/mass_battle/orchestration.py:1840-1880`
  - **S2.8** `[write]` per-atom `advance_cells` for atoms with a target or an unengaged escort assignment, both sides. `tests/sim/mass_battle/orchestration.py:1911-1918`
  - **S2.9** `[branch]` `[gate]` `FIELD_MOVEMENT`-gated cross-side time-of-impact resolution (`resolve_toi_and_commit`) — a TREE-B-only branch with no TREE A counterpart. `tests/sim/mass_battle/orchestration.py:1934-1935`
  - **S2.10** `halt_before_enemy` on both sides' atoms. `tests/sim/mass_battle/orchestration.py:1937-1938`
  - **S2.11** `resolve_cross_side_contention(unit_a, unit_b)` resolves cells two sides both moved into. `tests/sim/mass_battle/orchestration.py:1945`
  - **S2.12** post-movement `find_contacts` → `pairs`, then per-atom stamina drain proportional to cells in contact. `tests/sim/mass_battle/orchestration.py:1950-1971`
  - **S2.13** `[branch]` `resolve_engagements_cascading` if `CASCADING_ENABLED` else `resolve_engagements`. `tests/sim/mass_battle/orchestration.py:1972-1974`
  - **S2.14** `[write]` volley + engagement damage applied simultaneously to `unit_a.hp`/`unit_b.hp`; `[branch]` `PER_CELL` on routes damage through the per-column grid (`distribute_casualties_cellwise`/`apply_to_subunit`) instead of the aggregate `distribute_casualties`. `tests/sim/mass_battle/orchestration.py:2064-2065`, `tests/sim/mass_battle/orchestration.py:2079-2122`
  - **S2.15** `recalc_size()` both units; `check_drift()` on non-routed/non-broken units. `tests/sim/mass_battle/orchestration.py:2123-2130`
  - **S2.16** `[gate]` `command <= 0` forces `set_morale(0.0)` (instant rout path). `tests/sim/mass_battle/orchestration.py:2141-2143`
  - **S2.17** `[gate]` subunit-level rout check (`eff_morale <= 0` or `troop_total() < SUBUNIT_ROUT_FLOOR`), then `derive_rout()` per unit. `tests/sim/mass_battle/orchestration.py:2153-2161`
  - **S2.18** `[branch]` every `TICKS_PER_PHASE` ticks: `phase_boundary(unit_a, unit_b, current_phase)`. `tests/sim/mass_battle/orchestration.py:2163-2166`
    - **S2.18.1** fixed call order: `stamina_check` → `discipline_check_phase` → `morale_check_phase` → `rout_resolution` → `rally_check` → `reform_check` → `threadwork_check`. `tests/sim/mass_battle/orchestration.py:339-345`
    - **S2.18.2** `[gate]` `rally_check` and `threadwork_check` are empty hooks (`pass`); `reform_check` is implemented and flag-gated on `REFORM_CHECK_ENABLED` (default ON). `tests/sim/mass_battle/orchestration.py:287-289`, `tests/sim/mass_battle/orchestration.py:296-330`, `tests/sim/mass_battle/orchestration.py:332-334`
  - **S2.19** loop end: `winner` from final `routed` flags; returns a result dict. `tests/sim/mass_battle/orchestration.py:2166-2176`
- **S3** `orchestration.run_multi_turn_battle(unit_a, unit_b, shape_a, shape_b, anchor_map, max_battle_turns)`:
  - **S3.1** `[loop]` per `battle_turn` in `1..max_battle_turns`: `reset_positions` both units, then call `run_battle(unit_a, unit_b)` (persistent unit state across turns). `tests/sim/mass_battle/orchestration.py:2368-2374`
  - **S3.2** `[gate]` break if either unit routed after the turn; else `between_turn_recovery` both units. `tests/sim/mass_battle/orchestration.py:2393-2398`
  - **S3.3** loop end: winner derived from routed flags; returns a result dict with per-turn `log`. `tests/sim/mass_battle/orchestration.py:2400-2414`
- **S4** `orchestration.run_multi_unit_battle(side_a, side_b, pairings, shapes_a, shapes_b, anchor_map, max_battle_turns)`:
  - **S4.1** `[branch]` `[gate]` `PC_RESERVE_COMMIT`: pairs whose unit is in Reserve are benched out of `active_pairs` at start. `tests/sim/mass_battle/orchestration.py:2587-2591`
  - **S4.2** `[loop]` per `battle_turn`: reserve-commit check (benched pairs re-activate at their commit turn). `tests/sim/mass_battle/orchestration.py:2606-2611`
  - **S4.3** pursuit-phase resolution for units already pursuing a routed enemy (`recall_check` gate, else `pursuit_damage`). `tests/sim/mass_battle/orchestration.py:2616-2651`
  - **S4.4** `[loop]` each active pair: `reset_positions` then `run_battle(ua, ub)`. `tests/sim/mass_battle/orchestration.py:2655-2670`
  - **S4.5** freed-attacker bonus damage against an adjacent enemy, from units freed on a previous turn. `tests/sim/mass_battle/orchestration.py:2674-2719`
  - **S4.6** `[gate]` newly-routed detection this turn. `tests/sim/mass_battle/orchestration.py:2722-2730`
  - **S4.7** morale-cascade + rout-contagion applied to adjacent friendly units of each newly-routed unit (`discipline_check_cascade` gate, then `cascade_morale_hit`). `tests/sim/mass_battle/orchestration.py:2732-2774`
  - **S4.8** `[branch]` victor of a resolved pair becomes a pursuer (`Fast` speed) or a freed attacker (otherwise). `tests/sim/mass_battle/orchestration.py:2778-2807`
  - **S4.9** `[gate]` termination: mutual rout, or no active pairs/pursuit/reserve remaining → break; else `between_turn_recovery` on all non-routed units. `tests/sim/mass_battle/orchestration.py:2824-2840`
  - **S4.10** loop end: winner by surviving-unit count; returns a result dict with per-turn `log` and per-unit casualties. `tests/sim/mass_battle/orchestration.py:2842-2862`

## 4. OUT

| Output | Kind | Consumer | Anchor |
|---|---|---|---|
| **TREE A** | | | |
| `{attacker_wins, degree, attacker_size_pct, defender_size_pct}` | dict (return) | `systems/factions/sim/faction_action.py:459 deg`, `:461 battle['attacker_wins']` | `systems/mass_battle/sim/massbattle.py:1846-1851` |
| `scene.battle_concluded` Key | emit (additive-only, no `apply=`) | `world.echo_scheduler` when attached; 4 declared consumers per `references/key_graph.json` per docstring (not independently re-verified here) | `systems/factions/sim/faction_action.py:414` (sched.emit(key)) |
| **TREE B** | | | |
| `{winner, turns, phases, tick_in_phase, a_stamina, b_stamina, a_hp_pct, b_hp_pct, a_morale, b_morale, truncated_groups, truncated_pairs, truncated_troops, max_groups}` | dict (return) | `run_multi_turn_battle` (`:2374`), `run_multi_unit_battle` (`:2666`), test callers | `tests/sim/mass_battle/orchestration.py:2166-2182` |
| `{winner, battle_turns, log, a_loss_final, b_loss_final}` | dict (return) | `tests/sim/gauge_mb.py`, `tests/valoria/test_deployment_geometry.py`, `test_friction_cev.py` | `tests/sim/mass_battle/orchestration.py:2408-2414` |
| `{winner, battle_turns, log, a_surviving, b_surviving, a_casualties, b_casualties}` | dict (return) | `tests/valoria/test_reserve_commit.py:42` | `tests/sim/mass_battle/orchestration.py:2852-2862` |
| trace events (`tick`/`melee`/`volley`/`positions`) | emit (opt-in via `start_trace(True)`) | `tests/sim/mass_battle/workbench/trace.py:78 get_trace`, served by `workbench/server.py`'s `/api/trace` | `tests/sim/mass_battle/orchestration.py:1779 trace_event` |
| `MECHANICS` registry (`mechanic -> {fn, toggle, source, status}`) | registry | self-test (asserts every entry resolves); audit tooling | `tests/sim/mass_battle/engine.py:38 MECHANICS` |

## 5. State touched

| Field | R/W | Owning module | Anchor |
|---|---|---|---|
| **TREE A** | | | |
| `unit.hp` | RW | `systems/mass_battle/sim/units.py` (`Unit`) | write `systems/mass_battle/sim/massbattle.py:1274-1275`; read `:1834 effective_size` |
| `unit.morale` | RW | `systems/mass_battle/sim/units.py` (`Unit`) | write `systems/mass_battle/sim/massbattle.py:1295`, `systems/mass_battle/sim/massbattle.py:1299`, `systems/mass_battle/sim/massbattle.py:252` |
| `unit.routed` | RW | `systems/mass_battle/sim/units.py` (`Unit`) | write `systems/mass_battle/sim/massbattle.py:1303`, `systems/mass_battle/sim/massbattle.py:269`; read `:1836 attacker_wins` |
| `unit.stamina` | RW | `systems/mass_battle/sim/units.py` (`Unit`) | write `systems/mass_battle/sim/massbattle.py:1211-1222` |
| `unit.discipline` | W | `systems/mass_battle/sim/units.py` (`Unit`) | write `systems/mass_battle/sim/massbattle.py:289` |
| `world.rng` | R | caller (`GameState`, outside this subsystem) | `systems/mass_battle/sim/massbattle.py:1830` |
| `world.battle_count` | W | `systems/factions/sim/faction_action.py` (outside this subsystem's own folder — see §6) | `systems/factions/sim/faction_action.py:515` |
| **TREE B** | | | |
| `unit.hp` | RW | `tests/sim/mass_battle/hierarchy/units.py` (`Unit`) | write `tests/sim/mass_battle/orchestration.py:2064-2065` |
| `unit.morale` | RW | `tests/sim/mass_battle/hierarchy/units.py` (`Unit.set_morale`, `Unit.cascade_morale_hit`) | `tests/sim/mass_battle/hierarchy/units.py:2455` (set_morale, 2472 cascade_morale_hit) |
| `unit.routed` / `atom.routed` | RW | `tests/sim/mass_battle/hierarchy/units.py` (`Unit.derive_rout`) | `tests/sim/mass_battle/hierarchy/units.py:2438 derive_rout`; write site `tests/sim/mass_battle/orchestration.py:2153-2160` |
| `unit.stamina` | RW | `tests/sim/mass_battle/hierarchy/units.py` (`Subunit.drain_stamina`) | `tests/sim/mass_battle/hierarchy/units.py:709 drain_stamina` |
| `unit.col_grid` (per-column grid, `PER_CELL` only) | RW | `tests/sim/mass_battle/percell.py` | `tests/sim/mass_battle/orchestration.py:2119-2120 sync_col_grid` |

## 6. Seams

| Direction | Peer | Mechanism | Anchor |
|---|---|---|---|
| up | `engine/mc_v18.py` (campaign driver) | `run_campaign` → `run_season(action_callback=_faction_actions_callback)` | `engine/mc_v18.py:220 run_campaign`, `:267 run_season` |
| lateral | `systems/overview/sim/season.py` | `run_season`'s Step 2 invokes the passed `action_callback(world)` | `systems/overview/sim/season.py:70-71` (action_callback(world)) |
| lateral | `systems/factions/sim/faction_action.py` (FA lane) | `_faction_actions_callback` → `faction_take_action` → `_try_conquest` → `resolve_mass_battle` (TREE A) — the one live faction-scale battle call, reached only past the action-roll gate and the targets/Mil-floor gate (TREE A S0.1–S0.2) | `engine/mc_v18.py:130 faction_take_action`; `systems/factions/sim/faction_action.py:251 _try_conquest`, `:431-438 resolve_mass_battle` |
| down | `engine/substrate/keys.py` | `_try_conquest` emits `scene.battle_concluded` off the battle result, additive-only | `systems/factions/sim/faction_action.py:372` (from engine.substrate.keys import ..., :361 key =) |
| — | `systems/social_contest/sim/contest/wrapper.py` | comment-only reference ("Mirrors mass_battle.engine") — not an import, no runtime coupling | `systems/social_contest/sim/contest/wrapper.py:4`, `systems/social_contest/sim/contest/wrapper.py:290` |
| — (none found) | `engine/`, other `systems/*` | TREE B (`tests/sim/mass_battle/`) has zero `import` statements reaching `systems.` or `engine.` anywhere in its 28 modules | grep evidence, no anchor to cite (absence) — see §7 |

## 7. Traced gaps

| Gap | Evidence |
|---|---|
| **The two trees are disjoint and both alive for different reasons.** TREE A (`systems/mass_battle/sim/`) is retired per Jordan ruling J2 (2026-08-03) but carries the campaign's only faction-scale battle seam and cannot be deleted without breaking Military Conquest; TREE B (`tests/sim/mass_battle/`) is ruled canon by the same J2 but is unreachable from the campaign — feeding it a strategically-built unit raises `AttributeError: 'Subunit' object has no attribute 'cells_float'`. A later ruling (evacuation keep-set) re-pinned TREE A as `keep` one day after J2. | `systems/mass_battle/sim/__init__.py:1-11`; `tests/valoria/test_j2_mass_battle_seam.py:1-46` (full narrative), `:65-100 _canon_accepts_a_strategic_unit` (the measured `AttributeError`); `CURRENT.md:31` (2026-08-08 MB-lane stamp) |
| **TREE A's multi-turn/multi-unit orchestrators are dead code.** `run_multi_turn_battle` (line 1357) and `run_multi_unit_battle` (line 1526) have no caller anywhere in the repo — not `resolve_mass_battle` (which calls only single-encounter `run_battle`), not any test. `resolve_mass_battle`'s own docstring calls the single-encounter path a stand-in: "multi-unit orchestrator overkill for C2 scope." | grep for `run_multi_turn_battle`/`run_multi_unit_battle` scoped to TREE A across `tests/`, `systems/`, `engine/` returns zero call sites (only the TREE-B-scoped calls in `tests/valoria/test_reserve_commit.py`, `test_deployment_geometry.py`, `test_friction_cev.py`, which import `orchestration` from TREE B, not `massbattle` from TREE A); `systems/mass_battle/sim/massbattle.py:1823-1824` |
| **TREE A has two more never-wired modules.** `tactic_cards.py`'s `FACTION_TACTIC_CARD_POOL_MODIFIERS` is an empty dict, explicitly not referenced by `massbattle.py` ("ports without referencing this dict"), reserved pending a contamination audit. `altonian_reinforcements.py`'s `invoke_altonian_reinforcements` unconditionally raises `NotImplementedError`, and a dedicated guard test asserts it must keep doing so until MB's own migration plan converts it. | `systems/mass_battle/sim/tactic_cards.py:14-33`; `systems/mass_battle/sim/altonian_reinforcements.py:17-21`; `engine/tests/test_pipeline_reach.py:782-793 test_only_accepted_handoff_still_raises_unconditionally` |
| **`CASCADING_ENABLED` is a hardcoded `True` module constant in both trees, not an env-read flag** — despite TREE B's `config.py` being otherwise env-var-driven for its other toggles (§2), `CASCADING_ENABLED` there is still a bare `True` assignment. The `else resolve_engagements(...)` branch is therefore unreachable in either tree without a source edit. | `systems/mass_battle/sim/massbattle.py:84 CASCADING_ENABLED`; `tests/sim/mass_battle/config.py:143 CASCADING_ENABLED` |
| **The two trees disagree on the primary rout driver.** TREE A erodes morale every tick from accumulated damage (`erosion = total_dmg / (discipline*command)`, then `morale -= erosion`); TREE B removed that per-tick path by directive, leaving only the `command <= 0` instant-rout branch — TREE B rout instead comes from the phase-boundary `morale_check_phase` and the subunit floor check (S2.17/S2.18), not a per-tick erosion term. | `systems/mass_battle/sim/massbattle.py:1297-1299`; `tests/sim/mass_battle/orchestration.py:2135-2136` |
| **TREE A's `Unit`/`Subunit` split is a test-pinned circular import, not a clean layering.** `massbattle.py` imports `Subunit`/`Unit` from `units.py` at its own tail, after all its module-level constants/functions are already bound; `units.py` late-binds back to `massbattle` as `_mb` to reach those same constants/helpers at method-call time. The cycle is intentional and pinned by a dedicated regression test, not accidental debt. | `systems/mass_battle/sim/massbattle.py:1904 Unit`; `systems/mass_battle/sim/units.py:36 _mb`; `tests/valoria/test_import_cycle_game_state_npe.py:68` |
| **`rally_check` and `threadwork_check` are empty stub hooks in both trees**; TREE B additionally implements `reform_check` (TREE A's `reform_check` is also an empty stub). A default-off/never-executes flow that both trees' `phase_boundary` call unconditionally every phase. | `systems/mass_battle/sim/massbattle.py:293-303` (all three stubs); `tests/sim/mass_battle/orchestration.py:287-289`, `tests/sim/mass_battle/orchestration.py:332-334` (rally/threadwork stubs), `:296-330` (reform_check implemented, flag `REFORM_CHECK_ENABLED` default ON) |
| **Registries have not caught up to the J2 ruling.** `registers/mechanics_index.yaml`'s `mass_battle` entry still points `sim_module: systems/mass_battle/sim/massbattle.py` (TREE A) with no acknowledgement of TREE B. `references/module_contracts.yaml`'s `mass_battle` module entry deliberately omits `sim_module` at all (marked "undeclared", awaiting an MB-lane add). Neither registry names `tests/sim/mass_battle/` anywhere. | `registers/mechanics_index.yaml:484-507`; `references/module_contracts.yaml:584-610` |
| **TREE B never touches campaign world-state.** No file under `tests/sim/mass_battle/` references a `world` object, and none imports anything from `systems.` or `engine.` — confirming it operates purely on `Unit`/`Subunit` dataclasses with no faction/territory/season coupling. This is the structural half of why it cannot receive the strategic seam without an adapter. | grep for `\bworld\b` across `tests/sim/mass_battle/**/*.py` returns zero matches; grep for `^from systems\.` / `^import systems\.` / `^from engine\.` / `^import engine\.` across the same tree returns zero matches |
| **`_faction_to_unit`'s mapping is admittedly unspecified.** The strategic-faction → cell-based-`Unit` construction that would let TREE B receive the campaign's call has no canonical spec; `_faction_to_unit`'s own docstring says so, and `resolve_mass_battle`'s docstring separately flags terrain modifiers and the faction→unit mapping as deferred gaps. | `systems/mass_battle/sim/massbattle.py:1869-1872`, `:1812-1814` |
