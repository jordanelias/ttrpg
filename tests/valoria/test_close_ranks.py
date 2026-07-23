"""ED-MB-0028 — cell-level closing-ranks lifecycle (Jordan directive 2026-07-23):
"as cells lose troops, unengaged troops from other cells fill them in to keep engaged cells at
prescribed density; coverage shrinks as minimums aren't met — the internal-subunit version of
rotating troops."

Verifies the foundational primitive Subunit.close_ranks(): leading ranks are refilled toward spawn
density from the rear, the rear depletes first, conservation holds, and it is inert when gated off.
"""
import os
import sys

import pytest

_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

from mass_battle.engine import build_army, SIDE_A_START_ROW  # noqa: E402
import mass_battle.hierarchy.units as HU  # noqa: E402


def _deep_subunit(width=3, depth=5, conc=100):
    spec = {'shape': 'Line', 'troop_type': 'infantry', 'unit_type': 'melee',
            'width': width, 'depth': depth, 'troops': width * depth * conc,
            'starting_position': (SIDE_A_START_ROW, 25)}
    return build_army([spec], 'A', 'A').subunits[0]


@pytest.fixture
def close_ranks_on():
    prev = HU.PC_CLOSE_RANKS
    HU.PC_CLOSE_RANKS = True
    yield
    HU.PC_CLOSE_RANKS = prev


def _front_hit(su, casualties):
    """Apply `casualties` evenly across the leading rank (orig_r == 0)."""
    front = [pid for pid in su.cell_troops if pid[0] == 0]
    per = casualties / len(front)
    for pid in front:
        su.cell_troops[pid] = max(0.0, su.cell_troops[pid] - per)


def test_default_gated_off():
    assert HU.PC_CLOSE_RANKS is False, "close-ranks must default OFF (byte-exact)"


def test_inert_when_off():
    su = _deep_subunit()
    _front_hit(su, 250)
    snapshot = dict(su.cell_troops)
    su.close_ranks()  # flag off -> no-op
    assert su.cell_troops == snapshot


def test_conservation(close_ranks_on):
    su = _deep_subunit()
    _front_hit(su, 250)
    before = sum(su.cell_troops.values())
    su.close_ranks()
    after = sum(su.cell_troops.values())
    assert abs(before - after) < 1e-6


def test_front_refilled_from_rear(close_ranks_on):
    su = _deep_subunit(width=3, depth=5)  # 1500 troops, 15 cells @100
    _front_hit(su, 250)                    # front rank down to ~16.7/cell
    su.close_ranks()
    # leading ranks restored to full prescribed density; the rearmost rank absorbed the loss
    for pid, t in su.cell_troops.items():
        if pid[0] == 0:
            assert t == pytest.approx(100.0), "front rank must be refilled to spawn density"
    rear_total = sum(t for pid, t in su.cell_troops.items() if pid[0] == max(p[0] for p in su.cell_troops))
    assert rear_total < 3 * 100.0, "the rear rank must have given up troops to the front"


def test_depth_spent_before_frontage(close_ranks_on):
    su = _deep_subunit(width=3, depth=5)
    _front_hit(su, 500)  # lose a third of the block
    su.close_ranks()
    live_by_rank = {}
    for pid, t in su.cell_troops.items():
        live_by_rank.setdefault(pid[0], 0.0)
        live_by_rank[pid[0]] += (t > 0.5)
    # front ranks stay fully manned (3 live cells); the rear ranks are the ones that thin out
    assert live_by_rank[0] == 3, "frontage must be preserved"
    assert live_by_rank[max(live_by_rank)] < 3, "depth (rear) must be spent first"


def test_shallow_cannot_sustain(close_ranks_on):
    # a 1-deep line has no reserve: close_ranks cannot refill it, so the front thins immediately
    su = _deep_subunit(width=6, depth=1)  # 600 troops, all front rank
    _front_hit(su, 300)
    su.close_ranks()
    front_avg = sum(su.cell_troops.values()) / len(su.cell_troops)
    assert front_avg == pytest.approx(50.0), "a shallow line has no depth to close ranks from"


def test_full_depletion_safe(close_ranks_on):
    su = _deep_subunit(width=2, depth=2)
    for pid in su.cell_troops:
        su.cell_troops[pid] = 0.0
    su.close_ranks()  # must not raise / divide-by-zero
    assert sum(su.cell_troops.values()) == 0.0
