"""engine/autoload/engine_clock.py — the temporal spine: one tick, three phases, one owner.

Status: [live, 2026-08-27] — ED-IN-0199, plan Phase A1 (behaviour-neutral re-siting).

WHAT THIS OWNS — AND, PRECISELY, WHICH SECTION OF THE SPEC.
`systems/_architecture/reference/propagation_spec_v1.md` §O.1 states the tick model: "There is no
sub-season fixed timestep today. The season is the tick," composing exactly SEASON_TICK ->
ACTION -> ACCOUNTING_BOUNDARY, and "engine_clock owns this composition and is the only module
that may advance the season counter." That spec has been CANONICAL since 2026-07-02 and the
module it names did not exist. This is it.

⚠ This implements §O.1's PHASE ORDERING, and that is now ALL it implements.

WHAT THIS MODULE LOST, 2026-09-16 (ED-IN-0232, RULED by Jordan: *"anything key-based gets
retired"*). Until that ruling this seam carried two more lines — `accounting_boundary()` and
`next_tick()` on a Key scheduler fetched from `world` — and most of the reasoning that used to
stand here was about WHERE those two lines sat. It was a real argument about a real defect
(running both inside the ACTION phase deferred every accounting-phase apply a tick late), but
its whole subject retired with the Key substrate: there is no scheduler to fetch, no emission
queue to drain, and no phase for the scheduler to be in. The phase ORDER below is unchanged and
is still §O.1's; what is gone is the second reason for it.

FALSIFIER (CLAUDE.md §0.1 pt 3). The ordering claim is pinned by
`tests/valoria/test_engine_clock_phases.py`. The stronger output control that used to live
here — a seed-42 campaign compared field-by-field including `key_log_hash` — retired with the
fields it compared; what survives is the seeded campaign comparison itself, which moved to the
flag-OFF distribution the tree already asserted (see `engine/tests/test_f7_smoke_oracle.py`).

ONE NON-OUTPUT DIFFERENCE, stated so "output-identical" is not read as "identical".
`systems/overview/sim/season.py` no longer imports `run_accounting` at module level, so
`systems.overview.sim.accounting` and its transitive imports now load at the first `run_tick`
instead of at `season` import. Nothing in that closure draws RNG or mutates a world at import
time, so no campaign output moves — but the import TIMING genuinely changed, and a future
import-order-sensitive change should know that.

WHAT THIS IS NOT. It does NOT implement §4.1's `drain_emission_queue` seeding of accounting
emissions, the `cascade_depth` caps, or ORD-3 observer ordering — those are later phases and
two of them are blocked on rulings (R-4, R-11). This module is the SEAM, sited correctly, with
the composition the spec names. Growing it is a separate, non-neutral change.
"""
from __future__ import annotations

from engine.autoload.season_manager import advance_season
from engine.substrate import composition

#: §O.1's three phase names. Exported so callers and tests name the seam rather than
#: re-spelling the strings. These are the only phase constants in the tree now; the scheduler
#: that carried a second, internal set retired with the Key substrate (ED-IN-0232).
PHASE_SEASON_TICK = "season_tick"
PHASE_ACTION = "action"
PHASE_ACCOUNTING_BOUNDARY = "accounting_boundary"

PHASES = (PHASE_SEASON_TICK, PHASE_ACTION, PHASE_ACCOUNTING_BOUNDARY)


def run_tick(world, action_callback=None):
    """Run one season tick: SEASON_TICK -> ACTION -> ACCOUNTING_BOUNDARY.

    Returns `season_manager.SeasonResult`. `action_callback(world)` is the ACTION phase
    body and stays caller-supplied for the reason `season.run_season` already gave: the
    dispatch policy differs between the batch sim, an interactive Godot session, and a
    test injecting deterministic actions.

    The ordering below is §O.1's. The accounting boundary is no longer a call — with the Key
    scheduler retired (ED-IN-0232) nothing needs draining at it — so the boundary is now simply
    the point BETWEEN the action callback and accounting's body, which is where the spec puts it.

      * `run_accounting` is resolved by ROLE, not imported: `engine/` states what it needs
        and `references/module_contracts.yaml` states who provides it (see
        `engine/substrate/composition.py`). A direct import here would put `systems` back in
        `engine`'s import graph, which `tests/valoria/test_engine_does_not_import_systems.py`
        holds at zero.
    """
    result = advance_season(world)                       # --- SEASON_TICK ---

    if action_callback is not None:
        action_callback(world)                           # --- ACTION ---

    # --- ACCOUNTING_BOUNDARY opens ---
    composition.require('accounting')(world)             # --- tick closes ---

    return result
