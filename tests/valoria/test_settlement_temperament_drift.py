"""The drift store a write lands in is the store the read comes out of (ED-SE-0050).

THE DEFECT THIS PINS. `temperament_modifiers` read the drift store with a bare
`_drift_store()` — no `world` — while `apply_strain_shock` wrote it with
`_drift_store(world)`. `_drift_store(world=None)` returns `world.npc_drift_state`
when given a world and the module-global `_drift_state` otherwise, so in any
world-carrying campaign the write and the read addressed provably different dict
objects: every strain shock's accumulated drift landed somewhere the reader could
not reach, and `temperament_modifiers` returned `drift=0.0, drift_applied=False`
forever.

This is CLAUDE.md §0.1 point 1's read/write asymmetry class, and it was born
broken rather than broken by drift — the reader never had a `world` parameter to
pass. Both functions are currently campaign-unreachable (no importer: see
`systems/settlements/settlements_flow_skeleton_v1.md`), so this test is also the
first thing that has ever executed the pair together.

FALSIFIER. `test_a_world_write_is_visible_to_a_world_read` fails against the
pre-fix tree (reader hits the module global, sees 0.0) and passes after. The
remaining tests pin the fallback path so the fix does not quietly delete it.
"""
from __future__ import annotations

import pytest

from systems.settlements.sim import temperaments as T


class _World:
    """Minimal world carrying the registry field `_drift_store` looks for."""

    def __init__(self):
        self.npc_drift_state: dict[str, float] = {}


@pytest.fixture(autouse=True)
def _clean_module_store():
    """The module-global store is process-wide; isolate every test from it."""
    T.reset_drift()
    yield
    T.reset_drift()


def _drifted_territory() -> str:
    """A territory whose temperament is NOT already outcomes-only.

    Drift interpolates alpha toward the outcomes-only weights, so on a territory
    that is already outcomes-only the alpha shift is zero and the assertion below
    could pass for the wrong reason.
    """
    for tid, temp in T.TERRITORY_TEMPERAMENTS.items():
        if temp != "outcomes-only":
            return tid
    raise AssertionError("no non-outcomes-only territory in the roster")


def test_a_world_write_is_visible_to_a_world_read():
    """THE FALSIFIER. Pre-fix this fails: the read could not reach the world store."""
    w = _World()
    tid = _drifted_territory()

    written = T.apply_strain_shock(2.0, [tid], world=w)
    assert written[tid] > 0, "precondition: the shock must record positive drift"
    assert w.npc_drift_state[tid] == written[tid], "the write landed on the world store"

    mods = T.temperament_modifiers(tid, "faction_action", world=w)
    assert mods["drift"] == written[tid]
    assert mods["drift_applied"] is True


def test_drift_actually_moves_the_coefficients():
    """Not just plumbed through — the value has to reach the alpha/beta output.

    Guards against a fix that returns the right `drift` field while leaving the
    interpolation reading the old store.
    """
    w = _World()
    tid = _drifted_territory()

    before = T.temperament_modifiers(tid, "faction_action", world=w)
    T.apply_strain_shock(5.0, [tid], world=w)
    after = T.temperament_modifiers(tid, "faction_action", world=w)

    assert after["drift"] > before["drift"]
    assert after["alpha"] != before["alpha"], "drift must shift alpha toward outcomes-only"
    outcomes_alpha = T.TEMPERAMENT_WEIGHTS["outcomes-only"]["alpha"]
    assert abs(after["alpha"] - outcomes_alpha) < abs(before["alpha"] - outcomes_alpha)


def test_the_module_global_fallback_still_works():
    """The world=None path is a real path, not dead code — keep it covered."""
    tid = _drifted_territory()

    T.apply_strain_shock(2.0, [tid], world=None)
    mods = T.temperament_modifiers(tid, "faction_action")

    assert mods["drift"] > 0
    assert mods["drift_applied"] is True


def test_the_two_stores_stay_isolated_from_each_other():
    """They are SUPPOSED to be disjoint. The defect was the reader being unable to
    address the world store at all — not the stores being separate."""
    w = _World()
    tid = _drifted_territory()

    T.apply_strain_shock(2.0, [tid], world=w)

    assert T.temperament_modifiers(tid, "faction_action")["drift"] == 0.0
    assert T.temperament_modifiers(tid, "faction_action", world=w)["drift"] > 0.0


def test_two_worlds_do_not_share_drift():
    """The reason the world store exists: concurrent worlds must not interleave."""
    w1, w2 = _World(), _World()
    tid = _drifted_territory()

    T.apply_strain_shock(3.0, [tid], world=w1)

    assert T.temperament_modifiers(tid, "faction_action", world=w1)["drift"] > 0.0
    assert T.temperament_modifiers(tid, "faction_action", world=w2)["drift"] == 0.0
