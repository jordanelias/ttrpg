"""Perimeter face / face-normal geometry primitive (Jordan ruling 2026-07-23).
Pure geometry — no engine state, no goldens. Validates the primitive against the real formation
footprints (CELL_PATTERN_FN) and Jordan's hand-drawing model."""
import math
import os
import sys


import pytest  # noqa: E402
from modules.mass_battle.geometry import CELL_PATTERN_FN  # noqa: E402
from modules.mass_battle.perimeter import perimeter_faces, _centroid  # noqa: E402


def _face_outward(cen, f):
    """A face's normal must point AWAY from the centroid (outward)."""
    tip = (f.mid[0] + f.normal[0], f.mid[1] + f.normal[1])
    d_tip = (tip[0] - cen[0]) ** 2 + (tip[1] - cen[1]) ** 2
    d_pos = (f.mid[0] - cen[0]) ** 2 + (f.mid[1] - cen[1]) ** 2
    return d_tip > d_pos - 1e-9


def test_line_is_a_four_face_rectangle():
    """A Line footprint -> 4 perimeter faces, every normal unit-length and outward — the exact model
    in Jordan's drawing."""
    cells = CELL_PATTERN_FN['Line'](3)
    faces = perimeter_faces(cells)
    assert len(faces) == 4, f"a Line/rectangle has 4 faces, got {len(faces)}"
    cen = _centroid(cells)
    for f in faces:
        assert math.isclose(math.hypot(*f.normal), 1.0, abs_tol=1e-9), "normals must be unit vectors"
        assert _face_outward(cen, f), "face normal must point outward"


def test_rectangle_face_normals_are_axis_aligned():
    """The 4 face normals of an axis-aligned rectangle point along +/-r and +/-c (perpendicular to
    each face), covering all four cardinal directions."""
    cells = CELL_PATTERN_FN['Line'](3)
    faces = perimeter_faces(cells)
    dirs = {(round(f.normal[0]), round(f.normal[1])) for f in faces}
    assert dirs == {(1, 0), (-1, 0), (0, 1), (0, -1)}, f"expected 4 cardinal face normals, got {dirs}"


def test_arrowhead_has_a_sharp_or_flagged_tip_geometry():
    """An Arrowhead (triangle) -> 3 faces (a wedge hull), every face normal outward."""
    cells = CELL_PATTERN_FN['Arrowhead'](5)   # deeper wedge -> sharper apex
    faces = perimeter_faces(cells)
    assert len(faces) == 3, f"an Arrowhead hull is a triangle (3 faces), got {len(faces)}"
    cen = _centroid(cells)
    for f in faces:
        assert _face_outward(cen, f), "arrowhead normals must point outward"


def test_degenerate_footprint_still_returns_a_target():
    """A tiny (< 3 cell) footprint has no enclosed face."""
    assert perimeter_faces([(0, 0)]) == []
    assert perimeter_faces([(0, 0), (0, 1)]) == []


def test_determinism():
    """The primitive consumes no RNG and is order-independent — same cells (any order) -> same faces."""
    cells = CELL_PATTERN_FN['Line'](3)
    assert perimeter_faces(cells) == perimeter_faces(list(reversed(cells)))
