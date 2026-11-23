"""B10.27 (CHAR resolve-and-temper edits 1, 5): `queries/person_q.py::decisiveness`, the length of a person's
projected pursuit vector, and the line `decision/sheet.py::DevelopmentSheet` shows it on. Lane: the season loop.

THE FALSIFIER: `decisiveness` differing from the length of `projected_axes` for a hand-built person, at shift 0 or
at a scar shift; or the sheet's line differing from the reader's value for the person the space was handed."""
from __future__ import annotations

import math

from ..boot.realm import build_realm
from ..decision.sheet import creation_sheet, development_space, seat, take_ranked
from ..decision import make_chooser
from ..harness.play_surface import dispatching_chooser
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import person_q as PQ
from ..state.carriers import Person
from ..state.ids import H, draw_factory


def _person(pursuits, scar=None):
    p = Person(id="p_b1027", name="p_b1027")
    p.pursuits = dict(pursuits)
    p.scar = dict(scar or {})
    return p


def _length(v) -> float:
    acc = 0.0
    for a in sorted(v):
        acc += v[a] ** 2
    return math.sqrt(acc)


def test_decisiveness_is_the_projected_vector_length():
    held = PQ.SCAR_WEIGHT_SHIFT_AT
    arms = [({}, {}, 0.0), (dict(virtue=1.0), {}, 0.0), (dict(virtue=1.0, wealth=1.0), {}, 0.0),
            (dict(virtue=1.0, wealth=1.0), {}, 0.5), (dict(virtue=1.0, wealth=1.0), {"virtue": held}, 0.5)]
    got = []
    for pursuits, scar, shift in arms:
        p = _person(pursuits, scar)
        d = PQ.decisiveness(p, shift)
        assert d == _length(PQ.projected_axes(p, shift))
        got.append(d)
    assert len(got) == len(arms)
    assert got[0] == 0.0 and got[1] > 0.0          # no pursuit points nowhere; one points somewhere
    assert got[3] == got[2]                         # a shift with no scar at the threshold moves nothing
    assert got[4] != got[2]                         # one scar at the threshold does move the length


def test_the_development_sheet_shows_the_readers_decisiveness():
    w = build_realm(0)
    pid = sorted(w.persons)[0]
    p = w.persons[pid]
    w.fixtures = w.fixtures.sweep("scar_weight_shift", 0.5)
    held = [e for e, v in p.pursuits.items() if float(v) > 0]
    assert len(held) >= 2, "the first realm person holds one pursuit: no heir for the shift to reach"
    p.scar = {held[0]: PQ.SCAR_WEIGHT_SHIFT_AT}
    seen = []

    def pick(sheet):
        seen.append((sheet.decisiveness, PQ.decisiveness(p, 0.5), PQ.decisiveness(p, 0.0)))
        return take_ranked(sheet)

    mint = lambda who, verb, subj: H(w.world_seed, w.tick, who, f"act:{verb}:{subj}")
    draw = draw_factory(w.world_seed, lambda: w.tick)
    auto = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(), draw=draw)
    space = development_space(w.fixtures, mint, pick, verbs=resolvable_verbs(), draw=draw)
    choose = dispatching_chooser(auto, seat(creation_sheet(w.persons.values()), pid, space))
    SeasonDriver(w).season(choose, None, contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert seen, "the seated person was never deliberated for"
    assert seen[0][0] == seen[0][1] and seen[0][0] != seen[0][2]
