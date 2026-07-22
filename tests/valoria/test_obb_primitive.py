"""Tests for the OBB (oriented bounding box) cell primitive added to
tests/sim/mass_battle/geometry.py (CellBox, obb_overlap, obb_front_reach_overlap).

This is a foundation-only addition for a future spatial-model upgrade
(circle -> box): nothing in the engine calls these functions yet, so there is
no behaviour-change risk to any existing code path. These tests exercise the
primitive in isolation.

All configs are generated from a FIXED seed list (random.Random(seed), not
module-level `random`/unseeded `random.random()`), so every assertion is
against deterministic, reproducible data -- no live randomness."""
import math
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))  # tests/sim on path

from mass_battle.geometry import CellBox, cellbox_from, obb_overlap, obb_front_reach_overlap  # noqa: E402

CELL_RADIUS = 0.5  # mirrors mass_battle.hierarchy.units.CELL_RADIUS (half the 1.0 lattice pitch)

SEEDS = [1, 2, 3, 4, 5, 17, 42, 1001]


def _random_box(rng, cr_range=(-3.0, 3.0)):
    cr = rng.uniform(*cr_range)
    cc = rng.uniform(*cr_range)
    w = rng.uniform(0.3, 2.0)
    d = rng.uniform(0.3, 2.0)
    heading = (rng.uniform(-1.0, 1.0), rng.uniform(-1.0, 1.0))
    reach = rng.uniform(0.0, 1.0)
    return CellBox(cr=cr, cc=cc, w=w, d=d, heading=heading, reach_front=reach)


# ─── SYMMETRY ─────────────────────────────────────────────────────────────

def test_overlap_symmetric_seeded():
    for seed in SEEDS:
        rng = random.Random(seed)
        a = _random_box(rng)
        b = _random_box(rng)
        assert obb_overlap(a, b) == obb_overlap(b, a), f"seed={seed} a={a} b={b}"


def test_front_reach_overlap_symmetric_seeded():
    for seed in SEEDS:
        rng = random.Random(seed)
        a = _random_box(rng)
        b = _random_box(rng)
        assert obb_front_reach_overlap(a, b) == obb_front_reach_overlap(b, a), f"seed={seed} a={a} b={b}"


def test_overlap_symmetric_close_boxes():
    # Bias toward small offsets so a meaningful fraction of seeded pairs actually
    # overlap (uniform over +-3.0 mostly yields far-apart, trivially-False pairs).
    for seed in SEEDS:
        rng = random.Random(seed)
        a = _random_box(rng, cr_range=(-1.0, 1.0))
        b = _random_box(rng, cr_range=(-1.0, 1.0))
        assert obb_overlap(a, b) == obb_overlap(b, a)
        assert obb_front_reach_overlap(a, b) == obb_front_reach_overlap(b, a)


# ─── SELF-OVERLAP ─────────────────────────────────────────────────────────

def test_self_overlap():
    a = CellBox(cr=2.0, cc=-1.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    assert obb_overlap(a, a) is True
    assert obb_front_reach_overlap(a, a) is True

    b = CellBox(cr=0.0, cc=0.0, w=0.7, d=1.4, heading=(0.3, -0.9), reach_front=0.2)
    assert obb_overlap(b, b) is True
    assert obb_front_reach_overlap(b, b) is True


# ─── SEPARATION (axis-aligned unit boxes) ──────────────────────────────────

def test_separation_axis_aligned_row():
    a = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    # > 1.0 apart along row axis: no overlap.
    far = CellBox(cr=1.2, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    assert obb_overlap(a, far) is False
    # < 1.0 apart: overlap.
    near = CellBox(cr=0.8, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    assert obb_overlap(a, near) is True
    # Exactly 1.0 apart: documented boundary -- strict `<`, so this is NOT
    # an overlap (faces touch but do not interpenetrate).
    touching = CellBox(cr=1.0, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    assert obb_overlap(a, touching) is False
    # Straddle the boundary explicitly on both sides.
    just_under = CellBox(cr=0.999, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    just_over = CellBox(cr=1.001, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    assert obb_overlap(a, just_under) is True
    assert obb_overlap(a, just_over) is False


def test_separation_axis_aligned_col():
    a = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    near = CellBox(cr=0.0, cc=0.9, w=1.0, d=1.0, heading=(-1.0, 0.0))
    far = CellBox(cr=0.0, cc=1.1, w=1.0, d=1.0, heading=(-1.0, 0.0))
    assert obb_overlap(a, near) is True
    assert obb_overlap(a, far) is False


# ─── TRANSLATION INVARIANCE ────────────────────────────────────────────────

def test_translation_invariance_seeded():
    shifts = [(0.0, 0.0), (5.0, -3.0), (-2.5, 2.5), (100.0, -100.0)]
    for seed in SEEDS:
        rng = random.Random(seed)
        a = _random_box(rng, cr_range=(-1.5, 1.5))
        b = _random_box(rng, cr_range=(-1.5, 1.5))
        base_overlap = obb_overlap(a, b)
        base_reach = obb_front_reach_overlap(a, b)
        for (sr, sc) in shifts:
            a2 = CellBox(cr=a.cr + sr, cc=a.cc + sc, w=a.w, d=a.d, heading=a.heading, reach_front=a.reach_front)
            b2 = CellBox(cr=b.cr + sr, cc=b.cc + sc, w=b.w, d=b.d, heading=b.heading, reach_front=b.reach_front)
            assert obb_overlap(a2, b2) == base_overlap, f"seed={seed} shift={(sr, sc)}"
            assert obb_front_reach_overlap(a2, b2) == base_reach, f"seed={seed} shift={(sr, sc)}"


# ─── ROTATION (hand-computed) ──────────────────────────────────────────────
# Box B rotated 45 deg (heading normalize((-1,-1))) is a unit square whose
# corners point exactly along the row/col axes at distance sqrt(0.5^2+0.5^2)
# = sqrt(2)/2 ~= 0.70710678 from its centre (a "diamond" in axis-aligned
# terms), vs an axis-aligned unit box's face reach of only 0.5 along the same
# direction. Placed along the row axis from an axis-aligned unit box A
# (centres offset by t, same column), the row-axis projections are:
#   A: [-0.5, 0.5]            (face-to-face reach along row axis)
#   B: [t - 0.70710678, t + 0.70710678]   (corner-to-corner reach)
# so the two separate on the row axis exactly when 0.5 <= t - 0.70710678,
# i.e. t >= 0.5 + sqrt(2)/2 ~= 1.20710678 (hand-derived; verified no other
# axis separates earlier for these two placements -- see report).

_SQRT2_2 = math.sqrt(2.0) / 2.0
_ROTATION_THRESHOLD = 0.5 + _SQRT2_2  # ~= 1.20710678


def test_rotation_45deg_overlap_hand_computed():
    a = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    b_rot = CellBox(cr=1.0, cc=0.0, w=1.0, d=1.0, heading=(-1.0, -1.0))  # well inside threshold
    assert obb_overlap(a, b_rot) is True


def test_rotation_45deg_separation_hand_computed():
    a = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    b_rot = CellBox(cr=1.3, cc=0.0, w=1.0, d=1.0, heading=(-1.0, -1.0))  # past the threshold
    assert obb_overlap(a, b_rot) is False
    assert _ROTATION_THRESHOLD < 1.3  # sanity check on the hand-derived threshold itself


def test_rotation_diagonal_corner_reaches_farther_than_axis_aligned():
    # At the SAME centre offset (t=1.05, just past an axis-aligned unit box's
    # own 1.0 face-to-face threshold), the axis-aligned pair no longer
    # overlaps, but the 45deg-rotated pair still does -- direct evidence the
    # rotated box's corner reaches farther along this line than an
    # axis-aligned face would.
    a = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    b_axis_aligned = CellBox(cr=1.05, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    b_rotated = CellBox(cr=1.05, cc=0.0, w=1.0, d=1.0, heading=(-1.0, -1.0))
    assert obb_overlap(a, b_axis_aligned) is False
    assert obb_overlap(a, b_rotated) is True


# ─── REDUCES TO CIRCLE (axis-aligned offsets only) ─────────────────────────

def test_reduces_to_circle_axis_aligned_offsets():
    a = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    # Purely row-axis and purely col-axis offsets: for an axis-aligned unit
    # box these are the ONLY offsets where the box's projection onto the
    # offset direction is a face (reach exactly CELL_RADIUS), matching the
    # circle model exactly. Diagonal offsets diverge (see comment below) and
    # are deliberately excluded here.
    offsets = [
        (0.0, 0.0), (0.3, 0.0), (0.5, 0.0), (0.9, 0.0), (0.99, 0.0),
        (1.0, 0.0), (1.01, 0.0), (1.5, 0.0),
        (0.0, 0.4), (0.0, 0.999), (0.0, 1.0), (0.0, 1.2),
        (-0.7, 0.0), (0.0, -0.95), (0.0, -1.05),
    ]
    for (dr, dc) in offsets:
        b = CellBox(cr=dr, cc=dc, w=1.0, d=1.0, heading=(-1.0, 0.0))
        circle_overlap = math.hypot(dr, dc) < 2 * CELL_RADIUS  # < 1.0
        assert obb_overlap(a, b) == circle_overlap, f"offset={(dr, dc)}"


def test_diagonal_offset_diverges_from_circle_as_documented():
    # Expected divergence: at a 45deg offset, the box corner reaches out to
    # sqrt(2)/2 ~= 0.7071 in EACH of row and col, so two axis-aligned unit
    # boxes offset diagonally by (0.75, 0.75) (centre distance ~1.0607,
    # outside the circle's 1.0 radius-sum) still have their *box* corners
    # overlapping, while the *circle* model says no overlap. This is the
    # documented, expected divergence -- box and circle agree only on
    # cardinal offsets.
    a = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0))
    b = CellBox(cr=0.75, cc=0.75, w=1.0, d=1.0, heading=(-1.0, 0.0))
    dist = math.hypot(0.75, 0.75)
    assert dist > 2 * CELL_RADIUS  # circle model: NOT overlapping
    assert obb_overlap(a, b) is True  # box model: corners DO overlap


# ─── DIRECTIONAL REACH (the key test) ──────────────────────────────────────

def test_directional_front_reach_engages_only_in_front():
    # a faces "north" (heading (-1, 0), row decreasing = forward), body is a
    # unit square (w=d=1), reach_front=0.3. a's plain front face (no reach)
    # is at row = -0.5; with reach it is at row = -0.8.
    a = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0), reach_front=0.3)

    # Target directly IN FRONT (lower row than a's front face -- a's "up-field"
    # direction is decreasing row, per the up-field/advance_dir=-1 convention):
    # placed so the gap between a's plain front face (-0.5) and the target's
    # near face is 0.15 -- inside reach_front (0.3) but nonzero (no body
    # overlap). target near face (toward a) = target.cr + 0.5 = -0.65
    # => target.cr = -1.15.
    target_front = CellBox(cr=-1.15, cc=0.0, w=1.0, d=1.0, heading=(1.0, 0.0), reach_front=0.0)
    assert obb_overlap(a, target_front) is False  # gap present: no body overlap
    assert obb_front_reach_overlap(a, target_front) is True  # but a's reach engages it

    # The SAME target placed directly BEHIND a (mirror row, same gap): a's
    # reach only extends its FRONT face, never its back, so this must NOT
    # engage via a's reach.
    target_behind = CellBox(cr=1.15, cc=0.0, w=1.0, d=1.0, heading=(1.0, 0.0), reach_front=0.0)
    assert obb_overlap(a, target_behind) is False
    assert obb_front_reach_overlap(a, target_behind) is False


def test_directional_reach_is_from_the_reaching_box_only():
    # Reach is a's own front-facing property: reversing a's heading (so it
    # now faces the target that was previously "behind" it) flips which
    # placement it can reach -- proof the asymmetry follows the reaching
    # box's own heading, not absolute row direction.
    a_facing_south = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(1.0, 0.0), reach_front=0.3)
    target_at_1_15 = CellBox(cr=1.15, cc=0.0, w=1.0, d=1.0, heading=(1.0, 0.0), reach_front=0.0)
    target_at_neg_1_15 = CellBox(cr=-1.15, cc=0.0, w=1.0, d=1.0, heading=(1.0, 0.0), reach_front=0.0)
    assert obb_front_reach_overlap(a_facing_south, target_at_1_15) is True
    assert obb_front_reach_overlap(a_facing_south, target_at_neg_1_15) is False


def test_reach_front_zero_collapses_to_plain_overlap():
    for seed in SEEDS:
        rng = random.Random(seed)
        a = _random_box(rng, cr_range=(-1.0, 1.0))
        b = _random_box(rng, cr_range=(-1.0, 1.0))
        a0 = CellBox(cr=a.cr, cc=a.cc, w=a.w, d=a.d, heading=a.heading, reach_front=0.0)
        b0 = CellBox(cr=b.cr, cc=b.cc, w=b.w, d=b.d, heading=b.heading, reach_front=0.0)
        assert obb_front_reach_overlap(a0, b0) == obb_overlap(a0, b0), f"seed={seed}"


def test_either_side_reach_can_trigger_engagement():
    # b reaches forward into a even though a has no reach at all -- the
    # engagement test must catch EITHER side's reach, not just a's.
    a = CellBox(cr=-1.15, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0), reach_front=0.0)
    b = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(-1.0, 0.0), reach_front=0.3)
    assert obb_overlap(a, b) is False
    assert obb_front_reach_overlap(a, b) is True
    assert obb_front_reach_overlap(b, a) is True  # symmetric


# ─── DEGENERATE INPUTS ──────────────────────────────────────────────────────

def test_zero_heading_defaults_up_field():
    a = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(0.0, 0.0))
    assert a.heading == (-1.0, 0.0)
    b = CellBox(cr=0.5, cc=0.0, w=1.0, d=1.0, heading=(0.0, 0.0))
    # Should not raise, and should behave as a normal axis-aligned box.
    assert obb_overlap(a, b) is True
    assert obb_front_reach_overlap(a, b) is True


def test_near_zero_heading_defaults_up_field():
    a = CellBox(cr=0.0, cc=0.0, w=1.0, d=1.0, heading=(1e-12, -1e-13))
    assert a.heading == (-1.0, 0.0)


def test_zero_width_or_depth_no_crash():
    a = CellBox(cr=0.0, cc=0.0, w=0.0, d=1.0, heading=(-1.0, 0.0))
    b = CellBox(cr=0.0, cc=0.0, w=1.0, d=0.0, heading=(-1.0, 0.0))
    c = CellBox(cr=0.0, cc=0.0, w=0.0, d=0.0, heading=(-1.0, 0.0))
    # A zero-width (or zero-depth) box degenerates to a line segment (or a
    # point, for both zero) -- no crash on any of these combinations.
    for x in (a, b, c):
        assert isinstance(obb_overlap(x, x), bool)
        assert isinstance(obb_front_reach_overlap(x, x), bool)
    # DOCUMENTED EDGE CASE: a degenerate (zero-area) box does NOT overlap
    # even itself. Its degenerate axis's projection interval collapses to a
    # single point ([k, k]), and the strict "touching counts as separated"
    # boundary rule (test_separation_axis_aligned_row) applies there too --
    # max <= min is trivially true for a single point compared with itself,
    # so that axis reports separation. This is a direct, consistent
    # consequence of picking strict `<` overlap semantics, not a special
    # case bolted on for zero extents.
    assert obb_overlap(a, a) is False
    assert obb_overlap(b, b) is False
    assert obb_overlap(c, c) is False
    # Two zero-width boxes offset only in the direction the zero-width axis
    # collapses (col, for an up-field-facing box) should not overlap (no
    # extent left to overlap with) -- same verdict as the coincident case
    # above, for the same reason.
    a_shifted = CellBox(cr=0.0, cc=0.5, w=0.0, d=1.0, heading=(-1.0, 0.0))
    assert obb_overlap(a, a_shifted) is False


def test_cellbox_from_helper_matches_constructor():
    box_direct = CellBox(cr=1.0, cc=2.0, w=0.8, d=1.2, heading=(0.0, 1.0), reach_front=0.1)
    box_helper = cellbox_from(1.0, 2.0, (0.0, 1.0), w=0.8, d=1.2, reach_front=0.1)
    assert box_direct == box_helper


# ─── DETERMINISM ────────────────────────────────────────────────────────────

def test_determinism_repeated_calls():
    for seed in SEEDS:
        rng = random.Random(seed)
        a = _random_box(rng)
        b = _random_box(rng)
        r1 = obb_overlap(a, b)
        r2 = obb_overlap(a, b)
        r3 = obb_front_reach_overlap(a, b)
        r4 = obb_front_reach_overlap(a, b)
        assert r1 == r2
        assert r3 == r4


def test_non_finite_heading_guarded():
    """[antagonist reconcile] NaN/inf heading must not propagate NaN axes into SAT (would return
    garbage overlaps). It guards to the default up-field heading, same as the zero-vector case."""
    import math
    from mass_battle.geometry import CellBox, obb_overlap
    for bad in [(float('nan'), 0.0), (float('inf'), 0.0), (0.0, float('nan')), (float('inf'), float('inf'))]:
        box = CellBox(cr=0.0, cc=0.0, heading=bad)
        assert all(math.isfinite(x) for x in box.heading), f"heading {bad} not sanitized -> {box.heading}"
        # a box must overlap itself and a coincident box (no NaN-poisoned separation)
        assert obb_overlap(box, box) is True
        assert obb_overlap(box, CellBox(cr=0.0, cc=0.0, heading=(-1.0, 0.0))) is True
