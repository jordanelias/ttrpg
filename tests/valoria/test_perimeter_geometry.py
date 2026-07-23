"""Perimeter target-point / face-normal geometry primitive (Jordan ruling 2026-07-23).
Pure geometry — no engine state, no goldens. Validates the primitive against the real formation
footprints (CELL_PATTERN_FN) and Jordan's hand-drawing model."""
import math
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'sim'))

import pytest  # noqa: E402
from mass_battle.geometry import CELL_PATTERN_FN  # noqa: E402
from mass_battle.perimeter import (  # noqa: E402
    target_points, perimeter_faces, nearest_target, approach_alignment, _centroid, SHARP_TIP_DEG,
)


def _outward(cells, tp):
    """A target point's normal must point AWAY from the centroid (outward)."""
    cen = _centroid(cells)
    tip = (tp.pos[0] + tp.normal[0], tp.pos[1] + tp.normal[1])
    d_tip = (tip[0] - cen[0]) ** 2 + (tip[1] - cen[1]) ** 2
    d_pos = (tp.pos[0] - cen[0]) ** 2 + (tp.pos[1] - cen[1]) ** 2
    return d_tip > d_pos - 1e-9


def test_line_is_a_four_face_rectangle():
    """A Line footprint -> 4 perimeter faces, 4 major (face-mid) + 4 minor (corner) targets, all
    normals unit-length and outward — the exact model in Jordan's drawing."""
    cells = CELL_PATTERN_FN['Line'](3)
    faces = perimeter_faces(cells)
    assert len(faces) == 4, f"a Line/rectangle has 4 faces, got {len(faces)}"
    tps = target_points(cells)
    majors = [t for t in tps if t.kind == 'major']
    minors = [t for t in tps if t.kind == 'minor']
    assert len(majors) == 4 and len(minors) == 4
    for t in tps:
        assert math.isclose(math.hypot(*t.normal), 1.0, abs_tol=1e-9), "normals must be unit vectors"
        assert _outward(cells, t), f"{t.kind} normal must point outward"
    # a rectangle's corners are right angles (90deg) -> not sharp
    assert not any(t.sharp for t in minors), "rectangle corners (90deg) are not sharp tips"


def test_rectangle_face_normals_are_axis_aligned():
    """The 4 face normals of an axis-aligned rectangle point along +/-r and +/-c (perpendicular to
    each face), covering all four cardinal directions."""
    cells = CELL_PATTERN_FN['Line'](3)
    faces = perimeter_faces(cells)
    dirs = {(round(f.normal[0]), round(f.normal[1])) for f in faces}
    assert dirs == {(1, 0), (-1, 0), (0, 1), (0, -1)}, f"expected 4 cardinal face normals, got {dirs}"


def test_arrowhead_has_a_sharp_or_flagged_tip_geometry():
    """An Arrowhead (triangle) -> 3 faces; its ACUTE corners are flagged sharp (the pointed-formation
    exception), and at least one vertex is sharp (<= SHARP_TIP_DEG)."""
    cells = CELL_PATTERN_FN['Arrowhead'](5)   # deeper wedge -> sharper apex
    faces = perimeter_faces(cells)
    assert len(faces) == 3, f"an Arrowhead hull is a triangle (3 faces), got {len(faces)}"
    minors = [t for t in target_points(cells) if t.kind == 'minor']
    assert any(t.sharp for t in minors), "a wedge must flag at least one sharp (<=60deg) vertex"
    for t in target_points(cells):
        assert _outward(cells, t), "arrowhead normals must point outward"


def test_nearest_target_picks_the_faced_side():
    """An attacker due-north of a Line engages the NORTH face (its target point is the northmost);
    an attacker due-south engages the south face."""
    cells = CELL_PATTERN_FN['Line'](3)
    cen = _centroid(cells)
    north = (min(r for r, _c in cells) - 5, cen[1])   # well above the formation
    south = (max(r for r, _c in cells) + 5, cen[1])
    tn = nearest_target(cells, north)
    ts = nearest_target(cells, south)
    assert tn.pos[0] < cen[0], "north attacker should target the north (smaller-row) face"
    assert ts.pos[0] > cen[0], "south attacker should target the south (larger-row) face"
    # the engaged face's normal points toward the attacker
    assert tn.normal[0] < 0 and ts.normal[0] > 0


def test_approach_alignment_is_one_when_square_on():
    """A body approaching its nearest face ALONG the inward normal (square-on) scores ~1.0; a grazing
    (perpendicular-to-normal) approach scores ~0; a from-behind heading scores negative."""
    cells = CELL_PATTERN_FN['Line'](3)
    cen = _centroid(cells)
    north = (min(r for r, _c in cells) - 5, cen[1])
    # square-on: heading points south (into the north face) = inward normal direction
    square = approach_alignment(cells, north, attacker_heading=(1.0, 0.0))
    graze = approach_alignment(cells, north, attacker_heading=(0.0, 1.0))
    behind = approach_alignment(cells, north, attacker_heading=(-1.0, 0.0))
    assert square == pytest.approx(1.0, abs=1e-6), f"square-on approach should score 1.0, got {square}"
    assert abs(graze) < 1e-6, f"grazing approach should score ~0, got {graze}"
    assert behind == pytest.approx(-1.0, abs=1e-6), f"from-behind should score -1.0, got {behind}"


def test_degenerate_footprint_still_returns_a_target():
    """A tiny (< 3 cell) footprint has no enclosed face, but callers must still get a target point."""
    assert perimeter_faces([(0, 0)]) == []
    tps = target_points([(0, 0), (0, 1)])
    assert len(tps) == 1 and tps[0].kind == 'major'


def test_determinism():
    """The primitive consumes no RNG and is order-independent — same cells (any order) -> same targets."""
    cells = CELL_PATTERN_FN['Line'](3)
    a = target_points(cells)
    b = target_points(list(reversed(cells)))
    assert [(t.kind, t.pos, t.normal, t.sharp) for t in a] == [(t.kind, t.pos, t.normal, t.sharp) for t in b]
