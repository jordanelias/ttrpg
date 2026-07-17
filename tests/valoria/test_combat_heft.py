"""CI-tier: continuous weapon heft (WS-2 req4; morphology-rearch Phase B6 de-leak).

core.heft_resp reads weapon_physics.heft() — striking mass x forward-balance, normalised so the 2H cut-thrust
anchor (longsword) reads 1.0. The binary wt{light,heavy} class this replaced is gone outright (there is no
category left to reproduce, so the old byte-identity test is retired, not loosened). These tests pin the
falsifiable acceptance ordering the plan specifies: spear < arming < longsword < greatsword, and greatsword
not collapsed onto longsword within the (former) heavy class.
"""
import os
import sys

ENGINE = os.path.join(os.path.dirname(__file__), '..', '..', 'systems', 'combat', 'combat_engine_v1')
sys.path.insert(0, ENGINE)

import pytest  # noqa: E402
pytest.importorskip("numpy")  # engine import chain needs numpy + the sim modules; skip in the lightweight validator job

import core  # noqa: E402
from combatant import WEAPONS  # noqa: E402

CFG = {}  # heft_resp no longer reads cfg (kept as a parameter for call-site compatibility only)


def test_falsifiable_heft_ordering():
    """The plan's own acceptance test: spear < arming < longsword < greatsword. A spear's mass is mostly in its
    long shaft (light head, low PoB_frac contribution to heft), while a greatsword's mass is concentrated in a
    heavy, forward-balanced blade — heft tracks striking mass x forward-balance, not raw weapon mass.
    [PHASE-C FLAG, 2026-07-08, U1/ED-PC-0010] the spear<arming term now FAILS: U1's JD-1 PoB recalibration
    correctly moves arming/longsword's balance back toward the hand (per the ratified 1H band, 6-14cm), which
    necessarily lowers their m_head*PoB_frac heft numerator — even at the band's ceiling, neither can reach
    spear's own (untouched) numerator (checked: max achievable ~0.103/0.097 vs spear's fixed 0.138). This is
    NOT a new defect — it is the SAME reach-class over-dominance already tracked in registers/handoffs/HANDOFF_PC.md
    ("SPEAR flat-dominance... its win is REACH, not tempo") surfacing through a second symptom. Fixing it
    means revisiting spear's own head/haft mass split (out of JD-1's scope — spear was not one of the flagged
    weapons) or the approach-side lever already identified for the win-rate anomaly, not a per-weapon fudge
    here. The arming<longsword<greatsword sub-ordering (the part U1 actually governs) still holds and is
    checked separately below. Deliberately left failing, not silently patched."""
    h = lambda n: core.heft_resp(WEAPONS[n], CFG)
    assert h('spear') < h('arming') < h('longsword') < h('greatsword')


def test_sword_heft_ordering_within_band():
    """The part of the falsifiable ordering U1 actually governs (arming < longsword < greatsword) holds
    independent of the spear anomaly flagged above."""
    h = lambda n: core.heft_resp(WEAPONS[n], CFG)
    assert h('arming') < h('longsword') < h('greatsword')


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
