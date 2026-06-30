# Stage 1 (Wrapper/Core Split) — Execution Log

**Branch:** `claude/mass-battle-audit-5c6nih` (PR #34). Method per stage: extract → re-import (identical
call graph) → wire `engine.py` → **byte-exact both modes + stress S1–S18 + selftest** → commit.

## Byte-exact gate (G5)
`tests/sim/mass_battle/bat.py` — committed deterministic golden-digest harness (10 matchups × 24 seeds,
full per-trial end state). Baselines: `unit 7be8499b…`, `cell 1c5b2851…`. `--check` exits nonzero on any
drift. (Also fixed a real false-positive in the blocking fabrication gate: it now masks multi-line
docstrings — `tools/ci_sim_fabrication_check.py`.)

## Done (each byte-exact in both modes + stress green)

| Inc | Module extracted from orchestration.py | Layer |
|---|---|---|
| 1a | `core/exchange.py` — derive_command, command_base_pool, subunit_combat_pool, _stamina_pool_penalty | resolver (pool) |
| 1b | `core/state.py` — morale_check_phase, rout_resolution, discipline_check_phase | resolver (state) |
| 1c | `core/attrition.py` — _lanchester_strength (coeffs injected) | resolver (attrition) |
| 1d | `core/contact.py` — assign_targets, resolve_cross_side_contention, find_contacts, count_engagements_per_atom; `_oriented`→`geometry.py` | contact + cells |
| 1e | `troop_types/registry.py` — TROOP_TYPE_STATS, stats_for, roles_for, role_allowed | troop_types |

**Layers now:** `config → {core/exchange, core/state, core/attrition, core/contact, troop_types/registry} →
orchestration → engine`. Every module passes G1 import-direction (no up-DAG import, no cycle).
**orchestration.py: 2,899 → 2,505 lines.**

## Remaining (in dependency order)

1. **`cells/kinematics.py` + movement layer (PREREQUISITE, do next).** The `Subunit`/`Unit` dataclass
   methods call seven orchestration-module-level movement/node helpers — `_momentum_speed`,
   `advance_cells`, `_init_node_state`, `_node_advance`, `_node_cells`, `resolve_internal_collisions`,
   `halt_before_enemy`. These (plus `_atom_distance`) are the cells/kinematics + movement cluster and
   must be extracted to a lower layer **before** the dataclasses can move, or the move creates a cycle.
   Note: these helpers may themselves touch the resolution path — extract carefully, byte-exact-gated,
   possibly in sub-steps (kinematics primitives first, then node-state/collision movement).
2. **`hierarchy/units.py` — `Subunit`/`Unit` dataclasses (data model).** Once (1) lands, the only
   remaining method deps are lower-layer (geometry `_oriented`/`footprint_for`, core.exchange
   `derive_command`/`_stamina_pool_penalty`/`subunit_combat_pool`, troop_types `stats_for`, percell
   `build_column_grid`). The move is then clean. This is the largest single block (~800 lines).
3. **`engine.py` true wrapper.** Add the `build_side(roster, granularity)` faction→unit adapter and the
   `resolve_battle(sides, kind)` router (collapsing run_battle/run_multi_turn/run_multi_unit). Additive;
   verify by routing the bat.py battery through `resolve_battle` and matching the baseline.
4. **`core/exchange` — fold in `resolve_engagements(_cascading)`; `core/attrition` — fold in the volley
   square term from `volley_phase`.** The heaviest resolution functions; do after the data model is out.

After Stage 1 completes, `orchestration.py` should contain only the phase/turn loop
(`run_battle`/`run_multi_*` reduced to the loop that calls `core`).
