"""[ED-MB-0041 Tier-2] The column view must be rebuilt from live cells, not frozen at spawn.

`col_grid` is built once, in `Unit.__post_init__`, from the spawn footprint. `sync_col_grid` used to
refresh only the `density` of the columns already in that list, so the column *membership* — and the
per-column `depth` — never changed. A body that wheeled or drifted laterally therefore occupied columns
its own grid did not contain, at which point `_fatigue_sigma` and `_defender_depth` both quietly
returned 0.0: no fatigue and no depth-based charge absorption, for exactly the units doing the
manoeuvring the model exists to represent.
"""
import os, sys
_SIM = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'sim'))
if _SIM not in sys.path:
    sys.path.insert(0, _SIM)

import pytest
from mass_battle.config import PER_CELL, STAMINA_MAX
from mass_battle.engine import build_army, SIDE_A_START_ROW
from mass_battle.percell import sync_col_grid, _fatigue_sigma, _defender_depth

pytestmark = pytest.mark.skipif(not PER_CELL, reason="column view only exists under PER_CELL")


def _unit(col=20):
    return build_army([{'shape': 'Line', 'troop_type': 'infantry', 'troops': 600.0,
                        'concentration': 100.0, 'starting_position': (SIDE_A_START_ROW, col)}],
                      'A', 'A')


def _shift(unit, dc):
    """Translate every cell laterally by `dc` columns, whichever coordinate source is live."""
    for a in unit.subunits:
        if hasattr(a, '_node_pos'):
            for cid, (r, c) in list(a._node_pos.items()):
                a._node_pos[cid] = (r, c + dc)
        else:
            for cid in list(a.cell_offsets_c):
                a.cell_offsets_c[cid] = a.cell_offsets_c.get(cid, 0) + dc
            for cid, _, _ in a.iter_cells():
                a.cell_offsets_c.setdefault(cid, dc)


def test_grid_membership_follows_the_cells():
    u = _unit()
    spawn_cols = {b.col for b in u.col_grid}
    assert spawn_cols, "a deployed unit must occupy some columns"

    _shift(u, 25)
    sync_col_grid(u)
    live_cols = {c for a in u.subunits for _pid, (r, c), _t in a.iter_cells()}
    grid_cols = {b.col for b in u.col_grid}

    assert grid_cols == live_cols, "the column view must be the live footprint, not the spawn one"
    assert not (grid_cols & spawn_cols), "this scenario is only meaningful if the body actually moved off"


def test_fatigue_and_depth_survive_a_lateral_shift():
    """The two mechanics that silently switched off. Both must still see the body after it moves."""
    u = _unit()
    _shift(u, 25)
    sync_col_grid(u)
    live_cols = {c for a in u.subunits for _pid, (r, c), _t in a.iter_cells()}
    contact = [(r, c) for a in u.subunits for _pid, (r, c), _t in a.iter_cells()]

    for b in u.col_grid:
        b.stamina = STAMINA_MAX / 2.0

    assert _fatigue_sigma(u, live_cols) < 0.0, \
        "a half-exhausted moved body must still register fatigue"
    assert _defender_depth(u, contact) > 0.0, \
        "a moved body must still present depth against a charge"


def test_depth_tracks_attrition_not_the_spawn_rank_count():
    u = _unit()
    before = {b.col: b.depth for b in u.col_grid}
    assert max(before.values()) > 1, "need a multi-rank formation for this test to mean anything"

    # Kill the rear ranks outright: drop every cell below the leading rank.
    for a in u.subunits:
        rows = sorted({cid[0] for cid in a.cell_troops})
        for cid in list(a.cell_troops):
            if cid[0] != rows[0]:
                del a.cell_troops[cid]
    sync_col_grid(u)

    assert all(b.depth == 1 for b in u.col_grid), \
        "a column ground down to one rank must not keep claiming its spawn depth"
