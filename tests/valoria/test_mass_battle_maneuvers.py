"""Wires the mass-battle maneuver acceptance validators (envelop/sweep) into CI on BOTH movement
paths — the measurement instrument for the movement/pathing audit's fix plan (ED-1096/1097,
finding 1.4, fix-plan step 6).

Before this file: `validators.py`'s `Run:` docstring pinned only PER_CELL, leaving
FIELD_MOVEMENT/PC_NODE_COHESION at the ambient default. Since ED-1089 flipped that default ON,
every bare invocation of V-ENVELOP/V-SWEEP silently measured the DEAD node-path arm — the two
maneuver instructions ('envelop'/'sweep') are confirmed to exist only on the legacy grid path — so
past "Stage C.4 passed" / "the maneuver works" claims were true only of a path nothing runs by
default anymore. This file makes both arms explicit and checked:

  - test_*_grid: the LEGACY path, where the underlying mechanism is real. A genuine regression
    test — if this goes red, a real mechanic broke.
  - test_*_node: the LIVE default path Jordan actually watches (the workbench, traced battles).
    Marked xfail(strict=True) FOR NOW — it is expected to fail today (the maneuvers are confirmed
    unreachable there) and MUST start passing once fix-plan step 7 (the waypoint primitive) lands.
    strict=True means an unexpected PASS is itself a failure, so this file cannot silently rot into
    "xfail forever" once the fix ships — remove the marker at that point, not before.

Toggled via validators._set_movement_path, which mutates the already-imported module-level
FIELD_MOVEMENT/PC_NODE_COHESION on hierarchy.units and orchestration at runtime (not the
import-time env-var read bat.py relies on) — no subprocess isolation needed, but the toggles ARE
real process-wide globals, so every test here restores them in a `finally` to avoid leaking node/
grid state into whatever test runs next in the same pytest session."""
import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))  # tests/sim on path

from mass_battle import validators as _val  # noqa: E402
import mass_battle.hierarchy.units as _hu  # noqa: E402
import mass_battle.orchestration as _orch  # noqa: E402

# Lighter seed count than validators.py's own _SEEDS=20 default -- this is a CI acceptance gate
# (does the maneuver reach its goal at all), not the full aggregate-confidence battery a manual
# `python3 -m mass_battle.validators` run performs; keeps this file's runtime well inside
# tests/valoria's shared 5-minute CI budget (measured ~7s per path per validator locally).
_CI_SEEDS = 8


@pytest.fixture(autouse=True)
def _movement_toggles():
    # PER_CELL is a SEPARATE, additional gate the legacy advance_cells requires for 'envelop'/
    # 'sweep' to be reachable at all (hierarchy/units.py:897,925: `if PER_CELL and PC_ENVELOP_PATH
    # ...` / `if PER_CELL and PC_SWEEP ...`) -- distinct from FIELD_MOVEMENT/PC_NODE_COHESION
    # (which path), and read from the ambient process env at import time like they are, so it is
    # NOT set just by validators._set_movement_path('grid'). This test process's own pytest
    # environment does not set PER_CELL=1 (unlike validators.py's documented `Run:` line for a
    # manual script invocation), so force it here for the duration of every test in this file.
    saved = {(mod, name): getattr(mod, name) for mod in (_hu, _orch)
             for name in ('FIELD_MOVEMENT', 'PC_NODE_COHESION', 'PER_CELL')}
    _hu.PER_CELL = True
    try:
        yield
    finally:
        for (mod, name), val in saved.items():
            setattr(mod, name, val)


def test_envelop_reaches_rear_grid():
    """Regression: the legacy path's 'envelop' instruction still wraps a wide-placed detachment
    to the enemy's rear (V-ENVELOP, validators.py) -- this is the mechanism fix-plan step 7 will
    port to the live path, so it must keep working while that happens."""
    r = _val.v_envelop(path='grid')
    assert r.passed, f"V-ENVELOP (grid) regressed: measured={r.measured} expected={r.expected}"


def test_sweep_displaces_laterally_grid():
    """Regression: the legacy path's 'sweep' instruction still displaces a unit toward the enemy
    flank (V-SWEEP, validators.py)."""
    r = _val.v_sweep(path='grid')
    assert r.passed, f"V-SWEEP (grid) regressed: measured={r.measured} expected={r.expected}"


@pytest.mark.xfail(reason="movement audit finding 1.1-1.4 (ED-1096): 'envelop' is unreachable on "
                           "the default node path -- fix-plan step 7 (waypoint primitive) closes "
                           "this. Remove the xfail marker once it does, do not leave it stacked.",
                    strict=True)
def test_envelop_reaches_rear_node():
    """Acceptance target: V-ENVELOP on the LIVE default (node/field) path -- the path Jordan
    actually watches in the workbench. Currently fails (on==off, the instruction has zero effect)
    because _node_advance never reads Subunit.instructions at all."""
    r = _val.v_envelop(path='node', seeds=_CI_SEEDS)
    assert r.passed, f"V-ENVELOP (node) measured={r.measured} expected={r.expected}"


@pytest.mark.xfail(reason="movement audit finding 1.1-1.4 (ED-1096): 'sweep' is unreachable on "
                           "the default node path -- fix-plan step 7 (waypoint primitive) closes "
                           "this. Remove the xfail marker once it does, do not leave it stacked.",
                    strict=True)
def test_sweep_displaces_laterally_node():
    """Acceptance target: V-SWEEP on the LIVE default (node/field) path. Currently fails for the
    same reason as test_envelop_reaches_rear_node."""
    r = _val.v_sweep(path='node', seeds=_CI_SEEDS)
    assert r.passed, f"V-SWEEP (node) measured={r.measured} expected={r.expected}"
