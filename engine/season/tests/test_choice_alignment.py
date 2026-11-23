"""B10.56 (`02_CHAR_choice_alignment` edits 1-4) -- A CHOICE VALUE SCORED BY ALIGNMENT CELLS: `data/verbs.py::align_choice(key, value, axis)` beside `align`,
read by `decision/choose.py::score_terms`' `pursuit` for each `choice_sourced` key a candidate's operands carry. Lane: the season loop.

THE FALSIFIER: two persons of opposite weight on one axis ranking two `retreat_at` values of one `marshal` question the same way with a cell authored
on that axis (the term does not reach the score), or differently with no cell (the order is not content-blind where no cell is authored). The cell is
PLANTED here through the loader's own `choices=`; the shipped roster carries none (the cells are content for `BA1-cast-content`).
"""
from __future__ import annotations

from types import SimpleNamespace

from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import PURSUIT_AXES
from ..decision import choose as CH
from ..state.carriers import Candidate, Person

_AXIS = "grandiose_humble"
_SUBJECT = "p_choice_x"
_ROLE = V.CHOICE_RANGES["role"][0]
_EARLY, _LATE = V.CHOICE_RANGES["retreat_at"][1], V.CHOICE_RANGES["retreat_at"][2]   # two of the key's closed set, in its order


def _rank(p, weights, monkeypatch):
    """`make_ranker`'s real order of the two `marshal` forms (one per `retreat_at` value) for a person whose axis weights are `weights`; temperature 0."""
    forms = [Candidate("marshal", _SUBJECT, {"role": _ROLE, "retreat_at": v}) for v in (_EARLY, _LATE)]
    monkeypatch.setattr(CH, "opening_set", lambda person, view, question, fx: list(forms))
    monkeypatch.setattr(CH, "project", lambda person, shift=0.0: weights)
    fx = DEFAULT_FIXTURES.sweep("choice_temperature", 0).sweep("odds_weighting", "none")
    return [c.operands["retreat_at"] for c in CH.make_ranker(fx)(p, SimpleNamespace(question=object(), odds=None))]


def test_opposite_temperaments_rank_two_retreat_at_values_in_opposite_order(monkeypatch):
    assert _AXIS in PURSUIT_AXES
    plus = {ax: (1.0 if ax == _AXIS else 0.0) for ax in PURSUIT_AXES}
    minus = {ax: -w for ax, w in plus.items()}
    a, b = Person(id="p_choice_a", name="a"), Person(id="p_choice_b", name="b")

    bare = (_rank(a, plus, monkeypatch), _rank(b, minus, monkeypatch))
    assert bare[0] == bare[1] == [_EARLY, _LATE], bare          # no cell authored: the two persons rank alike (the shipped state)

    cell = {"retreat_at": {_EARLY: {_AXIS: 0.3}, _LATE: {_AXIS: -0.4}}}
    monkeypatch.setattr(V, "ALIGNMENT", V._load_alignment(choices=cell))
    assert V.align_choice("retreat_at", _EARLY, _AXIS) == 0.3
    ranked = (_rank(a, plus, monkeypatch), _rank(b, minus, monkeypatch))
    assert ranked == ([_EARLY, _LATE], [_LATE, _EARLY]), ranked  # one cell on one axis, opposite weights: opposite orders
