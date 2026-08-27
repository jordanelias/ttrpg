"""engine/autoload/engine_clock.py — the temporal spine: one tick, three phases, one owner.

Status: [live, 2026-08-27] — ED-IN-0199, plan Phase A1 (behaviour-neutral re-siting).

WHAT THIS OWNS — AND, PRECISELY, WHICH SECTION OF THE SPEC.
`systems/_architecture/propagation_spec_v1.md` §O.1 states the tick model: "There is no
sub-season fixed timestep today. The season is the tick," composing exactly SEASON_TICK ->
ACTION -> ACCOUNTING_BOUNDARY, and "engine_clock owns this composition and is the only module
that may advance the season counter." That spec has been CANONICAL since 2026-07-02 and the
module it names did not exist. This is it.

⚠ This implements §O.1's PHASE ORDERING. It does NOT implement §4.1's drain topology, and the
difference is worth naming here rather than leaving a reader to find it: §4.1's `run_tick`
pseudocode seeds accounting's emissions into the same `drain_emission_queue` as the action
phase's, and its own note says an "earlier draft called `run_accounting(state)` RAW, outside
the drain. That was unbounded." Line 103 below calls it raw. That is deliberate and bounded
for now — accounting emits nothing, so there is nothing to drain — but it means the shape
here is the one §4.1 rejects, and closing that is Phase E work, not a footnote to this one.

THE DEFECT THE RE-SITING FIXES, stated precisely because it is currently INERT and a reader
should not be misled into thinking a live bug was fixed. Before this module, the two clock
calls lived at the tail of `mc_v18._faction_actions_callback` (mc_v18.py:162-169 at 3d04568):

    _sched.accounting_boundary()   # enter ACCOUNTING_BOUNDARY, run OF-7 deferred applies
    _sched.next_tick()             # reset per-tick emission count, return to ACTION phase

`_faction_actions_callback` is the ACTION phase's body. Both calls therefore ran INSIDE the
action phase, before `run_accounting` had been reached at all, and `next_tick()` returned the
scheduler to `_PHASE_ACTION` for the whole of accounting. The consequence is exact and it is
in `engine/substrate/keys.py:_emit_at_depth`: an emission carrying an `apply` is deferred when
`self._phase == _PHASE_ACTION`. So any Key accounting emitted with a settlement-locus effect
would have been queued to the NEXT season's boundary rather than applied at this one — an
off-by-one-tick on every accounting-phase deferred apply, and a silent one.

WHY IT IS INERT TODAY, AND WHY THAT IS THE REASON TO MOVE IT NOW RATHER THAN LATER.
`systems/overview/sim/accounting.py` holds no scheduler reference and emits no Keys (verified
by grep at 3d04568: no `emit`, no `sched`, no `Key`). Its six steps are direct state writes.
So the misplacement costs nothing at this commit and the move is provably output-identical —
which is exactly the window in which to make it. The first accounting-phase emitter to land
would have inherited the defect, and its symptom (a settlement effect landing one season late)
is the kind that reads as a balance question rather than a phase bug.

FALSIFIER (CLAUDE.md §0.1 pt 3). `tests/valoria/test_engine_clock_phases.py` pins the phase
the scheduler is in at each seam, and fails against the pre-move tree. The output control is
separate and stronger: five seeded campaigns plus both pinned batches, compared field-by-field
including `key_log_hash`, must be byte-identical — recorded in the commit message. `keys_emitted`
is 164-229 per campaign, so the KeyLog hash is a live signal here, not a vacuous one.
The IN-TREE, re-runnable form of that control is `engine/tests/test_parliamentary_bridge.py`,
which pins `_ON_KEYLOG_HASH` / `_ON_KEYS_EMITTED` / `_ON_SCENES_RESOLVED` for a seed-42
ECHO_TRANSPORT-on campaign and runs in the `sim-regression` CI job. Cite that rather than the
commit message when someone asks whether this moved output.

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
#: re-spelling the strings; the scheduler's own internal phase constants live in
#: `engine/substrate/keys.py` and are deliberately NOT re-exported here — one owner each.
PHASE_SEASON_TICK = "season_tick"
PHASE_ACTION = "action"
PHASE_ACCOUNTING_BOUNDARY = "accounting_boundary"

PHASES = (PHASE_SEASON_TICK, PHASE_ACTION, PHASE_ACCOUNTING_BOUNDARY)


def scheduler_of(world):
    """The tick-scoped scheduler, or None when ECHO_TRANSPORT is off.

    `getattr` rather than an attribute access because `world.echo_scheduler` is set
    dynamically by `mc_v18.run_campaign` only under the flag — it is not a `World`
    dataclass field, and a world built by a test or by Godot may not carry one.
    """
    return getattr(world, "echo_scheduler", None)


def run_tick(world, action_callback=None):
    """Run one season tick: SEASON_TICK -> ACTION -> ACCOUNTING_BOUNDARY.

    Returns `season_manager.SeasonResult`. `action_callback(world)` is the ACTION phase
    body and stays caller-supplied for the reason `season.run_season` already gave: the
    dispatch policy differs between the batch sim, an interactive Godot session, and a
    test injecting deterministic actions.

    The ordering below is §O.1's, and each of the three scheduler-adjacent lines is placed
    where the spec puts it rather than where it happened to be:

      * `accounting_boundary()` runs AFTER the action phase closes and BEFORE accounting's
        body, because it IS the boundary — it drains the OF-7 deferred applies the action
        phase queued, and flips the scheduler to `_PHASE_ACCOUNTING` so that anything
        accounting emits applies immediately instead of deferring another tick.
      * `run_accounting` is resolved by ROLE, not imported: `engine/` states what it needs
        and `references/module_contracts.yaml` states who provides it (see
        `engine/substrate/composition.py`). A direct import here would put `systems` back in
        `engine`'s import graph, which `tests/valoria/test_engine_does_not_import_systems.py`
        holds at zero.
      * `next_tick()` runs LAST, closing the tick, because the per-tick emission counter must
        span BOTH phases — §4.1's note that "Level B's cap applies tick-wide, both phases."
        Resetting it before accounting (the pre-move behaviour) would have let a tick's total
        emissions exceed `emissions_per_tick_max` without tripping the guard.
    """
    result = advance_season(world)                       # --- SEASON_TICK ---

    if action_callback is not None:
        action_callback(world)                           # --- ACTION ---

    sched = scheduler_of(world)
    if sched is not None:
        sched.accounting_boundary()                      # --- ACCOUNTING_BOUNDARY opens ---
    composition.require('accounting')(world)
    if sched is not None:
        sched.next_tick()                                # --- tick closes ---

    return result
