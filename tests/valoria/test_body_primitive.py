"""The cell body: a circle of radius CELL_RADIUS, one lattice pitch across (geometry.CellBody).

Jordan, 2026-11-01: "troops have geometry. they cannot overlap." The body is a circle because a circle is the one
shape two cells at the formation's own spacing cannot overlap at ANY relative rotation; facing does not change
the body, it only gives weapon reach its direction (reach extends the FRONT only) and orients the octagon
partition of the directions a cell is struck from (geometry.octagon_angle, not tested here).

Pure geometry, deterministic, seeded. Covers: overlap is strict and symmetric; tangent bodies (one pitch apart,
the lattice) do not overlap at ANY rotation (the property that replaced the unit square, which overlapped its own
neighbour by 0.079 at 10 degrees and 0.207 at 45); depth; reach is directional, front only, from the reaching
body only, and collapses to the plain overlap at zero reach; heading normalisation and its guards.
"""
import math
import os
import random
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))

import pytest  # noqa: E402

from modules.mass_battle.geometry import (  # noqa: E402
    CELL_RADIUS, CellBody, body_depth, body_overlap, cellbody_from, reach_reaches,
)

PITCH = 2 * CELL_RADIUS


def _rand_pair(rng):
    a = cellbody_from(rng.uniform(-3, 3), rng.uniform(-3, 3), (rng.uniform(-1, 1), rng.uniform(-1, 1)), rng.uniform(0, 1))
    b = cellbody_from(rng.uniform(-3, 3), rng.uniform(-3, 3), (rng.uniform(-1, 1), rng.uniform(-1, 1)), rng.uniform(0, 1))
    return a, b


def test_the_body_is_one_pitch_across():
    assert CELL_RADIUS == 0.5 and PITCH == 1.0


def test_overlap_and_reach_are_symmetric_seeded():
    rng = random.Random(20261101)
    checked = 0
    for _ in range(400):
        a, b = _rand_pair(rng)
        assert body_overlap(a, b) == body_overlap(b, a)
        assert reach_reaches(a, b) == reach_reaches(b, a)
        assert body_depth(a, b) == body_depth(b, a)
        checked += 1
    assert checked == 400


def test_overlap_is_strict_and_tangent_bodies_do_not_overlap():
    a = cellbody_from(0.0, 0.0, (1.0, 0.0))
    assert not body_overlap(a, cellbody_from(1.0, 0.0, (1.0, 0.0)))        # tangent along the heading
    assert not body_overlap(a, cellbody_from(0.0, 1.0, (1.0, 0.0)))        # tangent beside it
    assert body_overlap(a, cellbody_from(0.99, 0.0, (1.0, 0.0)))
    assert body_depth(a, cellbody_from(1.0, 0.0, (1.0, 0.0))) == 0.0
    assert math.isclose(body_depth(a, cellbody_from(0.75, 0.0, (1.0, 0.0))), 0.25, abs_tol=1e-12)
    assert a.cr == 0.0 and body_depth(a, a) == PITCH                       # a body fully on itself


def test_a_lattice_neighbour_never_overlaps_at_any_rotation():
    """The property the unit square lacked: two bodies one pitch apart, the second turned by ANY angle, never
    interpenetrate -- heading plays no part in the body."""
    checked = 0
    for deg in range(0, 360, 5):
        th = math.radians(deg)
        h = (math.cos(th), math.sin(th))
        for other in ((1.0, 0.0), (0.0, 1.0), (-1.0, 0.0), (0.0, -1.0)):
            a = cellbody_from(0.0, 0.0, (1.0, 0.0))
            b = cellbody_from(other[0], other[1], h)
            assert not body_overlap(a, b), (deg, other)
            assert body_depth(a, b) == 0.0
            checked += 1
    assert checked == 72 * 4


def test_overlap_is_translation_invariant_seeded():
    rng = random.Random(7)
    for _ in range(100):
        a, b = _rand_pair(rng)
        dr, dc = rng.uniform(-9, 9), rng.uniform(-9, 9)
        a2 = cellbody_from(a.cr + dr, a.cc + dc, a.heading, a.reach_front)
        b2 = cellbody_from(b.cr + dr, b.cc + dc, b.heading, b.reach_front)
        assert body_overlap(a, b) == body_overlap(a2, b2)
        assert math.isclose(body_depth(a, b), body_depth(a2, b2), abs_tol=1e-9)


def test_body_overlap_ignores_reach_and_heading():
    a = cellbody_from(0.0, 0.0, (1.0, 0.0), reach_front=0.9)
    b = cellbody_from(1.3, 0.0, (0.0, 1.0))
    assert not body_overlap(a, b)                       # reach is a weapon, not a body
    assert not body_overlap(cellbody_from(0.0, 0.0, (0.0, 1.0)), b)


def test_front_reach_engages_only_in_front():
    reach = 0.3
    a = cellbody_from(0.0, 0.0, (1.0, 0.0), reach_front=reach)           # faces +row
    ahead = cellbody_from(PITCH + 0.2, 0.0, (-1.0, 0.0))                 # a gap of 0.2 in front
    behind = cellbody_from(-(PITCH + 0.2), 0.0, (1.0, 0.0))              # the same gap behind
    assert not body_overlap(a, ahead) and not body_overlap(a, behind)
    assert reach_reaches(a, ahead)
    assert not reach_reaches(a, behind)                                  # reach never extends the back


def test_reach_is_the_reaching_bodys_own_and_either_side_can_trigger():
    long_ = cellbody_from(0.0, 0.0, (1.0, 0.0), reach_front=0.5)
    short = cellbody_from(PITCH + 0.4, 0.0, (-1.0, 0.0), reach_front=0.0)
    assert reach_reaches(long_, short) and reach_reaches(short, long_)   # the long weapon reaches first
    blind = cellbody_from(0.0, 0.0, (-1.0, 0.0), reach_front=0.5)        # same weapon, faced away
    assert not reach_reaches(blind, short)


def test_reach_beside_the_front_does_not_engage():
    a = cellbody_from(0.0, 0.0, (1.0, 0.0), reach_front=0.5)
    side = cellbody_from(0.0, PITCH + 0.2, (1.0, 0.0))                   # beside, not ahead
    assert not reach_reaches(a, side)


def test_zero_reach_collapses_to_plain_overlap_seeded():
    rng = random.Random(11)
    for _ in range(300):
        a, b = _rand_pair(rng)
        a0 = cellbody_from(a.cr, a.cc, a.heading)
        b0 = cellbody_from(b.cr, b.cc, b.heading)
        assert reach_reaches(a0, b0) == body_overlap(a0, b0)


def test_zero_and_near_zero_heading_default_up_field():
    assert CellBody(0.0, 0.0, heading=(0.0, 0.0)).heading == (-1.0, 0.0)
    assert CellBody(0.0, 0.0, heading=(1e-12, -1e-12)).heading == (-1.0, 0.0)


def test_non_finite_heading_is_guarded():
    for bad in ((float('nan'), 0.0), (float('inf'), 1.0)):
        assert CellBody(0.0, 0.0, heading=bad).heading == (-1.0, 0.0)


def test_heading_is_normalised_and_helper_matches_constructor():
    b = cellbody_from(1.0, 2.0, (3.0, 4.0), reach_front=0.1)
    assert math.isclose(math.hypot(*b.heading), 1.0, abs_tol=1e-12)
    assert b == CellBody(1.0, 2.0, heading=(3.0, 4.0), reach_front=0.1)


def test_determinism_repeated_calls():
    rng = random.Random(5)
    pairs = [_rand_pair(rng) for _ in range(50)]
    first = [(body_overlap(a, b), reach_reaches(a, b), body_depth(a, b)) for a, b in pairs]
    assert first == [(body_overlap(a, b), reach_reaches(a, b), body_depth(a, b)) for a, b in pairs]
