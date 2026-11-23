"""B10.58 (`IS-B2-CHAR-07`, A-108) -- A PERSON'S OWN MANNER OFFSET: `Person.manner_offset`, read once, by `person_q.projected_axes`,
on the three axes `rosters.yaml: manner_offset_axes` names. Lane: the season loop.

THE FALSIFIERS: two persons with identical pursuits and opposite offsets projecting alike (the offset is not read); an offset moving an axis
it was not set on; a person with no offset projecting other than his pursuits alone; and a manner offset on the refused axis reaching the
refusal gate's threshold (M37: no manner axis feeds the gate -- `proposals/2026-10-24-character-layers-v2.md` section 11.5).
"""
from __future__ import annotations

from ..data import rosters as R
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.pursuits import pursuit, to_axes
from ..decision.options import refusal_tolerance, refusable, refuses
from ..queries.person_q import projected_axes
from ..state.carriers import Person

_SWING = DEFAULT_FIXTURES.get("manner_offset_bound")        # a planted offset AT the bound, the largest one the loader admits (H-481)
_AXIS = "deontological_instrumental"        # the gate's axis (`refusal_axis`, None at the control since B10.32) and one of the three


def _person(pid, offset):
    p = Person(id=pid, name=pid)
    p.pursuits = {pursuit("honour"): 5.0}
    p.manner_offset = dict(offset)
    return p


def test_two_persons_with_identical_pursuits_differ_by_their_offsets():
    """Opposite offsets on the three named axes: the projections differ by exactly the offsets there and not at all on the other four, and
    a person holding none projects his pursuits alone."""
    three = sorted(R.MANNER_OFFSET_AXES)
    up = _person("p_up", {a: _SWING for a in three})
    down = _person("p_down", {a: -_SWING for a in three})
    bare = _person("p_bare", {})
    u, d, b = projected_axes(up), projected_axes(down), projected_axes(bare)
    assert b == to_axes(bare.pursuits), "a person with no offset must project his pursuits alone"
    checked = 0
    for ax in sorted(R.PURSUIT_AXES):
        if ax in three:
            assert u[ax] == b[ax] + _SWING and d[ax] == b[ax] - _SWING, ax
        else:
            assert u[ax] == d[ax] == b[ax], ax
        checked += 1
    assert checked == len(R.PURSUIT_AXES) and len(three) == 3


def test_a_manner_offset_does_not_move_the_refusal_threshold():
    """M37: two persons with identical pursuits and opposite offsets on the refused axis project differently on it, and hold the SAME
    refusal threshold and refuse the same verbs: the gate reads his pursuits alone."""
    up, down = _person("p_up", {_AXIS: _SWING}), _person("p_down", {_AXIS: -_SWING})
    assert projected_axes(up)[_AXIS] != projected_axes(down)[_AXIS]
    tol_up, tol_down = refusal_tolerance(up, _AXIS), refusal_tolerance(down, _AXIS)
    assert tol_up == tol_down == refusal_tolerance(_person("p_bare", {}), _AXIS)
    verbs = sorted(refusable(_AXIS))
    assert verbs, "the axis refuses nothing, so the gate was not asked"
    assert [refuses(v, _AXIS, tol_up) for v in verbs] == [refuses(v, _AXIS, tol_down) for v in verbs]
