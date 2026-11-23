"""B10.57 (`IS-B2-CHAR-02` steps 1-5) -- ONE DECIDER FOR A CHOICE INSIDE A CONTEST: `decision/decider.py::make_decider(p, fx, draw, *, key, odds, bias, watch)` picks
one of a view's `legal` values by the alignment cells of `(key, value)` (B10.56) and the person's own axis weights, as a DRAW whose odds his interior sets. Lane: the
season loop. Planted persons, views and cells throughout (the shipped roster authors no choice cell, so no test reads it).
"""
from __future__ import annotations

from dataclasses import dataclass

from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import PURSUIT_AXES
from ..decision import choose as CH
from ..decision.decider import make_decider
from ..state.carriers import Person
from ..state.ids import draw_factory

_AXIS = "grandiose_humble"
_KEY = "retreat_at"
_A, _B, _C = V.CHOICE_RANGES[_KEY][:3]   # three of the key's closed set, in its order


@dataclass(frozen=True)
class _View:
    legal: tuple


def _scoped(base, n):
    """The wrapper's draw: `draw_factory`'s product bound to one scope, so `n` is the n-th decision of a scene."""
    return lambda pid, purpose: base(pid, f"test_role:scene:{n}:{purpose}")


def _weights(sign):
    return {ax: (float(sign) if ax == _AXIS else 0.0) for ax in PURSUIT_AXES}


def _plant(monkeypatch, sign, cell=None):
    """A person whose only weight is `sign` on `_AXIS`; `cell` (`{value: weight}`) authored on `_KEY` through the loader, else none."""
    monkeypatch.setattr(CH, "project", lambda person, shift=0.0, **read: _weights(sign))
    monkeypatch.setattr(V, "ALIGNMENT", V._load_alignment(choices={_KEY: {v: {_AXIS: w} for v, w in cell.items()}} if cell else None))
    return Person(id="p_decider", name="d")


def _picks(p, fx, legal, count, **kw):
    base = draw_factory(0, lambda: 0)
    return [make_decider(p, fx, _scoped(base, n), key=_KEY, **kw)(_View(legal)) for n in range(count)]


def test_with_no_cell_and_no_odds_every_legal_choice_is_drawn(monkeypatch):
    p = _plant(monkeypatch, 1)
    legal = (_A, _B, _C)
    picks = _picks(p, DEFAULT_FIXTURES, legal, 200)
    assert len(picks) >= 200 and all(x in legal for x in picks)
    assert set(picks) == set(legal), set(picks)          # a decider that always returns one value fails


def test_opposite_temperaments_pick_differently(monkeypatch):
    legal = (_A, _B)
    cell = {_A: 0.3, _B: -0.4}
    plus_bare, minus_bare = (_picks(_plant(monkeypatch, s), DEFAULT_FIXTURES, legal, 200) for s in (1, -1))
    assert plus_bare == minus_bare                          # no cell authored: the two persons draw alike on the same keyed draws
    plus, minus = (_picks(_plant(monkeypatch, s, cell), DEFAULT_FIXTURES, legal, 200) for s in (1, -1))
    assert plus.count(_A) > minus.count(_A) and plus.count(_B) < minus.count(_B), (plus.count(_A), minus.count(_A))
    assert plus.count(_A) > 100 > minus.count(_A)           # each leans toward the pole his weight takes


def test_a_single_legal_value_draws_nothing(monkeypatch):
    p = _plant(monkeypatch, 1, {_A: 0.3, _B: -0.4})
    def refuse(pid, purpose):
        raise AssertionError("a draw was taken on a single legal value")
    assert make_decider(p, DEFAULT_FIXTURES, refuse, key=_KEY)(_View((_B,))) == _B
