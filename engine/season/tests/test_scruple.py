"""The deontological gate on ONE scale (B10.22): the person's side of it is his axis's SHARE of his projected vector
(`options.refusal_tolerance`), on ±1 as an alignment cell is, so a refusal tracks the man and not the size of the table.

Read on the built realm with no season. The cells the realm ships are content (`16_PESSIMIST_CHAR_B`), so the refusal
half is read on PLANTED persons whose vectors and cells are set here, never on the shipped `forge` cell."""

from __future__ import annotations

import math

import pytest

from ..boot.realm import build_realm
from ..data import verbs as data_verbs
from ..data.rosters import _ROSTERS, PURSUIT_AXES, refusable
from ..decision import options as _options
from .test_cr21_cells import _deontological_axis


@pytest.mark.parametrize("seed", (0, 1))
def test_share_not_projected_weight_is_the_tolerance(seed, monkeypatch):
    """Every cast tolerance is the axis's share of his projected vector and lies on ±1; and on planted persons a verb whose
    cell sits past the SHARE is refused while the raw weight would have said otherwise, in both directions."""
    w = build_realm(seed)
    axis = _deontological_axis()
    cast = [p for p in w.persons.values() if not p.is_cohort]
    assert len(cast) > 1
    for p in cast:
        v = _options.project(p)
        norm = math.sqrt(sum(x * x for x in v.values()))
        tol = _options.refusal_tolerance(p, axis)
        assert -1.0 <= tol <= 1.0, f"{p.id}: a tolerance of {tol:+.3f} lies off the cells' ±1 scale"
        assert tol == pytest.approx(v[axis] / norm if norm else 0.0, abs=1e-9)
    assert any(abs(_options.project(p)[axis]) < abs(_options.refusal_tolerance(p, axis)) for p in cast), (
        "no cast member's share differs from his raw weight, so the scale change observes nothing here")

    other = next(a for a in sorted(PURSUIT_AXES) if a != axis)
    mild, harsh = sorted(refusable(axis))[:2]
    monkeypatch.setitem(_ROSTERS["pursuit_axes"], "refusable", {axis: [mild, harsh]})
    monkeypatch.setattr(data_verbs, "ALIGNMENT", {axis: {mild: -0.5, harsh: 0.5}})
    p = cast[0]

    def planted(on_axis, off_axis):
        monkeypatch.setattr(data_verbs, "PURSUIT_PROJECTION", {"planted": {axis: on_axis, other: off_axis}})
        monkeypatch.setattr(p, "pursuits", {"planted": 1.0})
        tol = _options.refusal_tolerance(p, axis)
        return tol, {v for v in (mild, harsh) if _options.refuses(v, axis, tol)}

    # A man whose small vector points mostly down the axis: raw weight -0.2 (past `mild`'s -0.5 on the old scale: tolerated),
    # share -0.894 (below it: `mild` is past what he allows himself). `harsh` (+0.5) is past both.
    tol, refused = planted(-0.2, 0.1)
    assert tol == pytest.approx(-0.2 / math.hypot(0.2, 0.1))
    assert refused == {mild, harsh}
    # A man whose small vector lies wholly up the axis: raw weight +0.1 would refuse `harsh` (+0.5); his share is +1, so
    # nothing the cells reach lies past him.
    tol, refused = planted(0.1, 0.0)
    assert tol == pytest.approx(1.0)
    assert refused == set()
