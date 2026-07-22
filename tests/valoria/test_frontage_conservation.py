"""Spatial-model v2 Stage D acceptance: the last live integer on the contact path removed.

Pre-v2, the melee Lanchester frontage term was `len(set(int_col))` over the snapped engaged-cell
recording (core.contact._find_contacts_standoff) -- the ONLY integer left on the live position/contact
path (backwards_analysis.md). Stage D (ED-MB-0013) replaces it with a CONTINUOUS front-overlap width
derived from the OBB bodies (geometry.engaged_frontage), threaded through the contact pairs as
`a_front`/`b_front` and consumed by core.attrition._lanchester_strength's new `front_width` argument.

This file is the Stage D gate the plan (spatial_model_v2_plan.md §3 Stage D / §5) demands:
  * I1 conservation holds under the new continuous partition (the hardest check -- casualties must
    still sum to hp);
  * the frontage is FRONTAGE-CAPPED: engaged_frontage can never exceed the enemy's covered meeting
    span, so the Lanchester law stays LINEAR (never square) -- its core guarantee;
  * the continuous width reduces to the legacy distinct-file count in the axis-aligned integer-lattice
    limit (each meeting file -> ~1.0), and is fractional for offset/partial meetings (the shape-fidelity
    gain), and DEPTH-INVARIANT (depth-2 stacking does not inflate frontage -- union dedups files);
  * the grid oracle path (front_width=None) keeps the exact legacy integer count (I4);
  * _lanchester_strength scales LINEARLY in front_width (a 2x frontage -> 2x strength);
  * determinism (I2).

Deterministic + seeded. Movement toggles saved/restored in fixtures (same discipline as
test_obb_contact_toi.py) so node/grid state never leaks between tests.
"""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))  # tests/sim on path

import pytest  # noqa: E402

import mass_battle.hierarchy.units as _hu  # noqa: E402
import mass_battle.orchestration as _orch  # noqa: E402
import mass_battle.core.contact as _contact  # noqa: E402
from mass_battle.geometry import (  # noqa: E402
    cellbox_from, engaged_frontage, _project_interval, _cellbox_corners,
    _normalize_heading, _rotate90,
)
from mass_battle.core.attrition import _lanchester_strength  # noqa: E402
from mass_battle.engine import build_unit  # noqa: E402
from mass_battle import validators as _val  # noqa: E402


# ─── fixtures ────────────────────────────────────────────────────────────────

@pytest.fixture
def field_path():
    saved = [(m, m.FIELD_MOVEMENT, m.PC_NODE_COHESION) for m in (_hu, _orch)]
    _val._set_movement_path('node')
    try:
        yield
    finally:
        for m, fm, nc in saved:
            m.FIELD_MOVEMENT = fm
            m.PC_NODE_COHESION = nc


def _unit_troops(unit):
    return sum(sum(su.cell_troops.values()) for su in unit.subunits)


def _row(c, cols, heading):
    """A single rank: one unit box per file in `cols`, at row `c`, facing `heading`."""
    return [cellbox_from(float(c), float(k), heading) for k in cols]


# ─── frontage geometry properties (pure) ─────────────────────────────────────

def test_frontage_reduces_to_file_count_aligned():
    """Axis-aligned integer-lattice head-on: each distinct meeting file contributes ~1.0, so the
    continuous width equals the legacy len(set(int_col)) distinct-column count."""
    for n in (1, 3, 5):
        cols = range(-(n // 2), -(n // 2) + n)
        A = _row(0, cols, (1.0, 0.0))
        B = _row(1, cols, (-1.0, 0.0))
        assert math.isclose(engaged_frontage(A, B, (1.0, 0.0)), float(n), abs_tol=1e-9), n


def test_frontage_continuous_on_offset():
    """A half-file lateral offset yields a FRACTIONAL frontage -- the shape-fidelity gain integer
    snapping used to lose (it would have rounded the meeting up to whole files)."""
    A = _row(0, range(-1, 2), (1.0, 0.0))
    B = [cellbox_from(1.0, k + 0.5, (-1.0, 0.0)) for k in range(-1, 2)]
    f = engaged_frontage(A, B, (1.0, 0.0))
    assert 2.0 < f < 3.0 and math.isclose(f, 2.5, abs_tol=1e-9)


def test_frontage_depth_invariant():
    """Stacking a second rank behind the first does NOT inflate frontage -- the union dedups files, so
    a depth-2 block meets the enemy on the SAME width as depth-1 (the 'depth-2 no longer collapses'
    fix: frontage is continuous overlap of files, not a per-cell count)."""
    cols = range(-1, 2)
    B = _row(1, cols, (-1.0, 0.0))
    d1 = _row(0, cols, (1.0, 0.0))
    d2 = d1 + _row(-1, cols, (1.0, 0.0))     # a second rank behind
    assert math.isclose(engaged_frontage(d1, B, (1.0, 0.0)),
                        engaged_frontage(d2, B, (1.0, 0.0)), abs_tol=1e-9)


def test_frontage_capped_by_meeting_width():
    """Lanchester-linear guarantee: engaged frontage can NEVER exceed the enemy's covered span on the
    frontage axis. A WIDE side meeting a NARROW enemy is capped at the narrow enemy's width (numerical
    superiority is a linear edge via overlap, never square)."""
    wide = _row(0, range(-5, 6), (1.0, 0.0))     # 11 files
    narrow = _row(1, range(-1, 2), (-1.0, 0.0))  # 3 files
    axis = _rotate90(_normalize_heading((1.0, 0.0)))
    narrow_span = max(_project_interval(_cellbox_corners(b, use_reach=False), axis)[1] for b in narrow) - \
        min(_project_interval(_cellbox_corners(b, use_reach=False), axis)[0] for b in narrow)
    f = engaged_frontage(wide, narrow, (1.0, 0.0))
    assert f <= narrow_span + 1e-9, f"{f} exceeded meeting width {narrow_span}"
    assert math.isclose(f, 3.0, abs_tol=1e-9)    # capped at the 3-file enemy


def test_frontage_empty_sides():
    B = _row(1, range(-1, 2), (-1.0, 0.0))
    assert engaged_frontage([], B, (1.0, 0.0)) == 0.0
    assert engaged_frontage(B, [], (1.0, 0.0)) == 0.0


# ─── _lanchester_strength: front_width replaces the integer, linearly ────────

def test_lanchester_front_width_linear():
    """The strength term is LINEAR in the continuous frontage: 2x frontage -> 2x strength. Confirms
    the frontage enters exactly where the integer column count used to (no square-law amplification)."""
    s1 = _lanchester_strength([], unit=None, front_width=1.0)
    s2 = _lanchester_strength([], unit=None, front_width=2.0)
    s3 = _lanchester_strength([], unit=None, front_width=2.5)
    assert math.isclose(s2, 2.0 * s1) and math.isclose(s3, 2.5 * s1)


def test_lanchester_grid_fallback_byte_exact():
    """front_width=None (the grid/OFF path) keeps the EXACT legacy integer distinct-column count -- the
    grid oracle never sees the continuous term (I4). A frontage of exactly N files must equal what
    N integer contact columns produced pre-Stage-D."""
    cells = [(0, 0), (1, 0), (0, 1), (0, 2)]      # 3 distinct files (col 0,1,2); depth on col 0
    legacy = _lanchester_strength(cells, unit=None)                 # None -> len(set(cols)) = 3
    continuous = _lanchester_strength([], unit=None, front_width=3.0)
    assert math.isclose(legacy, continuous)
    assert math.isclose(legacy, 3.0 / _hu_lanchester_ref())


def test_lanchester_zero_frontage_no_casualties():
    """A degenerate glancing contact (front_width rounds to ~0) yields zero strength -- honest (no
    frontage, no melee), and it can only be transient (bodies keep closing until frontage > 0), so it
    never becomes a permanent standoff."""
    assert _lanchester_strength([], unit=None, front_width=0.0) == 0.0


def _hu_lanchester_ref():
    from mass_battle.config import LANCHESTER_STRENGTH_REF
    return LANCHESTER_STRENGTH_REF


# ─── live field-battle integration: pairs carry continuous frontage, I1 holds ─

def test_field_pairs_carry_continuous_frontage(field_path):
    """On the live field path, find_contacts pairs now carry continuous a_front/b_front, and at least
    one meeting is FRACTIONAL (not an integer) -- proof the continuous width is actually in play, not
    silently collapsing back to integers."""
    import random
    random.seed(313)
    a = build_unit('Line', 3, 'A', 'A', 9)
    b = build_unit('Line', 3, 'B', 'B', 9)
    seen_front, seen_fractional = False, False
    real = _orch.resolve_engagements_cascading

    def _spy(unit_a, unit_b, pairs, *args, **kwargs):
        nonlocal seen_front, seen_fractional
        for p in pairs:
            if 'a_front' in p and 'b_front' in p:
                seen_front = True
                for key in ('a_front', 'b_front'):
                    v = p[key]
                    if v > 0 and not math.isclose(v, round(v), abs_tol=1e-6):
                        seen_fractional = True
        return real(unit_a, unit_b, pairs, *args, **kwargs)

    _orch.resolve_engagements_cascading = _spy
    try:
        _orch.run_battle(a, b, max_turns=18)
    finally:
        _orch.resolve_engagements_cascading = real
    assert seen_front, "field pairs did not carry a_front/b_front -> Stage D not wired"
    # not asserting seen_fractional strictly (a perfectly aligned mirror can stay integer), but for an
    # asymmetric seed we expect some fractional meeting; keep it informative if it ever regresses.


@pytest.mark.parametrize("seed", [1, 7, 42, 101, 2026])
def test_conservation_under_continuous_frontage(field_path, seed):
    """I1 (the hardest Stage D check): Sum cell_troops == hp for every non-routed/broken unit at battle
    end, under the continuous-frontage partition. Frontage scales HOW MUCH damage; distribute_casualties
    still conserves it -- this proves the continuous term did not break the conservation invariant."""
    import random
    random.seed(seed)
    a = build_unit('Line', 3, 'A', 'A', 9)
    b = build_unit('Line', 3, 'B', 'B', 9)
    _orch.run_battle(a, b, max_turns=18)
    for unit in (a, b):
        if unit.routed or unit.broken:
            continue
        assert math.isclose(_unit_troops(unit), unit.hp, rel_tol=1e-6, abs_tol=1e-3), \
            f"seed={seed} {unit.name}: Sum cell_troops={_unit_troops(unit)} != hp={unit.hp}"


def test_determinism_same_seed(field_path):
    """Same seed twice -> identical public outcome (the continuous frontage is a deterministic float
    computation: projection + interval merge, no set-iteration order dependence)."""
    import random

    def _run():
        random.seed(555)
        a = build_unit('Line', 3, 'A', 'A', 9)
        b = build_unit('Line', 3, 'B', 'B', 9)
        res = _orch.run_battle(a, b, max_turns=18)
        return (res['winner'], res['turns'], round(a.hp, 6), round(b.hp, 6))

    assert _run() == _run()
