"""CI-tier: continuous weapon heft (WS-2 req4; morphology-rearch Phase B6 de-leak).

core.heft_resp reads weapon_physics.heft() — striking mass x forward-balance, normalised so the 2H cut-thrust
anchor (longsword) reads 1.0. The binary wt{light,heavy} class this replaced is gone outright (there is no
category left to reproduce, so the old byte-identity test is retired, not loosened). These tests pin the
falsifiable acceptance ordering the plan specifies: spear < arming < longsword < greatsword, and greatsword
not collapsed onto longsword within the (former) heavy class.
"""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'designs', 'scene', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import pytest  # noqa: E402
pytest.importorskip("numpy")  # engine import chain needs numpy + the sim modules; skip in the lightweight validator job

import core  # noqa: E402
from combatant import WEAPONS  # noqa: E402

CFG = {}  # heft_resp no longer reads cfg (kept as a parameter for call-site compatibility only)


def test_falsifiable_heft_ordering():
    """The plan's own acceptance test: spear < arming < longsword < greatsword. A spear's mass is mostly in its
    long shaft (light head, low PoB_frac contribution to heft), while a greatsword's mass is concentrated in a
    heavy, forward-balanced blade — heft tracks striking mass x forward-balance, not raw weapon mass."""
    h = lambda n: core.heft_resp(WEAPONS[n], CFG)
    assert h('spear') < h('arming') < h('longsword') < h('greatsword')


def test_greatsword_not_collapsed_onto_longsword():
    """The headline req-4 case: a heavy forward-balanced greatsword reads meaningfully heavier than a longsword,
    not just marginally — the within-class differentiation the binary wt class could never express."""
    h_ls = core.heft_resp(WEAPONS['longsword'], CFG)
    h_gs = core.heft_resp(WEAPONS['greatsword'], CFG)
    assert h_gs > h_ls * 1.5


def test_longsword_anchor_near_one():
    """heft() is normalised so the 2H cut-thrust anchor (longsword) reads ~1.0 by construction."""
    assert abs(core.heft_resp(WEAPONS['longsword'], CFG) - 1.0) < 1e-6


def test_heft_never_negative():
    """The heft response cannot go negative (a zero-mass-head degenerate weapon floors at 0, never penalises)."""
    for w in WEAPONS.values():
        assert core.heft_resp(w, CFG) >= 0.0
