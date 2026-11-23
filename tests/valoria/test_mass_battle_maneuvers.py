"""Wires the mass-battle maneuver acceptance validators (envelop/sweep) into CI on BOTH movement
paths — the measurement instrument for the movement/pathing audit's fix plan (ED-1096/1097,
finding 1.4, fix-plan step 6).

Before this file: `validators.py`'s `Run:` docstring pinned only PER_CELL, leaving
FIELD_MOVEMENT/MB_NODE_COHESION at the ambient default. Since ED-1089 flipped that default ON,
every bare invocation of V-ENVELOP/V-SWEEP silently measured the DEAD node-path arm — the two
maneuver instructions ('envelop'/'sweep') were confirmed (this session) to exist only on the
legacy grid path — so past "Stage C.4 passed" / "the maneuver works" claims were true only of a
path nothing runs by default anymore. This file makes both arms explicit and checked:

  - test_*_grid: the LEGACY path, where the underlying mechanism is real. A genuine regression
    test — if this goes red, a real mechanic broke.
  - test_*_node: the LIVE default path Jordan actually watches (the workbench, traced battles).
    Landed RED first (xfail(strict=True), commit 50247b1) as the acceptance target for fix-plan
    step 7 (the waypoint primitive, hierarchy/units.py Unit._resolve_maneuver_goal). Step 7
    landed the same session and both flipped GREEN for real (not just "no longer erroring" --
    verified the xfail was hiding a real bug in v_envelop/v_sweep's own seeds/turns forwarding
    before trusting the green). Now real regression tests, same standing as the grid arm.

Toggled via validators._set_movement_path, which mutates the already-imported module-level
FIELD_MOVEMENT/MB_NODE_COHESION on hierarchy.units and orchestration at runtime (not the
import-time env-var read bat.py relies on) — no subprocess isolation needed, but the toggles ARE
real process-wide globals, so every test here restores them in a `finally` to avoid leaking node/
grid state into whatever test runs next in the same pytest session."""
import os
import sys


import pytest  # noqa: E402

from systems.mass_battle.sim import validators as _val  # noqa: E402
import modules.mass_battle.hierarchy.units as _hu  # noqa: E402
import modules.mass_battle.orchestration as _orch  # noqa: E402

# Lighter seed count than validators.py's own _SEEDS=20 default -- this is a CI acceptance gate
# (does the maneuver reach its goal at all), not the full aggregate-confidence battery a manual
# `python3 -m systems.mass_battle.sim.validators` run performs; keeps this file's runtime well inside
# tests/valoria's shared 5-minute CI budget (measured ~7s per path per validator locally).
_CI_SEEDS = 8


@pytest.fixture(autouse=True)
def _movement_toggles():
    # PER_CELL is a SEPARATE, additional gate the legacy advance_cells requires for 'envelop'/
    # 'sweep' to be reachable at all (hierarchy/units.py:897,925: `if PER_CELL and MB_ENVELOP_PATH
    # ...` / `if PER_CELL and MB_SWEEP ...`) -- distinct from FIELD_MOVEMENT/MB_NODE_COHESION
    # (which path), and read from the ambient process env at import time like they are, so it is
    # NOT set just by validators._set_movement_path('grid'). This test process's own pytest
    # environment does not set PER_CELL=1 (unlike validators.py's documented `Run:` line for a
    # manual script invocation), so force it here for the duration of every test in this file.
    #
    # [2026-07-02 adversarial-review finding, ED-MB-0001] MB_ENVELOP_PATH/MB_SWEEP were missing from
    # this save/restore set even though every test here (via v_envelop/v_sweep's on/off comparison)
    # mutates hierarchy.units' copies directly and always leaves them at False when a test function
    # returns (the off-arm runs last) -- contradicting this docstring's own claim to restore
    # everything. Added here so a future in-process test added later in this suite that constructs
    # a Unit with an 'envelop'/'sweep' instruction doesn't silently inherit a disabled maneuver
    # from whatever ran before it in the same pytest session -- exactly the class of silent-failure
    # this whole audit exists to catch.
    saved = {(mod, name): getattr(mod, name) for mod in (_hu, _orch)
             for name in ('FIELD_MOVEMENT', 'MB_NODE_COHESION', 'PER_CELL', 'MB_ENVELOP_PATH', 'MB_SWEEP')}
    _hu.PER_CELL = True
    try:
        yield
    finally:
        for (mod, name), val in saved.items():
            setattr(mod, name, val)


def test_envelop_reaches_rear_grid():
    """Regression: the legacy path's 'envelop' instruction still wraps a wide-placed detachment
    to the enemy's rear (V-ENVELOP, validators.py) -- the mechanism fix-plan step 7 ported to the
    live path, so this must keep working alongside it."""
    r = _val.v_envelop(path='grid')
    assert r.passed, f"V-ENVELOP (grid) regressed: measured={r.measured} expected={r.expected}"


def test_sweep_displaces_laterally_grid():
    """Regression: the legacy path's 'sweep' instruction still displaces a unit toward the enemy
    flank (V-SWEEP, validators.py)."""
    r = _val.v_sweep(path='grid')
    assert r.passed, f"V-SWEEP (grid) regressed: measured={r.measured} expected={r.expected}"


def test_sweep_displaces_laterally_node():
    """Acceptance: V-SWEEP on the LIVE default (node/field) path -- Unit._resolve_maneuver_goal/
    _sweep_goal (fix-plan step 7), same mechanism as the retired test_envelop_reaches_rear_node."""
    r = _val.v_sweep(path='node', seeds=_CI_SEEDS)
    assert r.passed, f"V-SWEEP (node) measured={r.measured} expected={r.expected}"
