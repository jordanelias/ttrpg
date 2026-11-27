"""B10.27 (CHAR resolve-and-temper edits 1, 5): `queries/person_q.py::decisiveness`, the length of a person's
projected pursuit vector, and the line `decision/sheet.py::DevelopmentSheet` shows it on. Lane: the season loop.

THE FALSIFIER: `decisiveness` differing from the length of `projected_axes` for a hand-built person, at shift 0 or
at a scar shift; or the sheet's line differing from the reader's value for the person the space was handed.

B10.28 (CHAR resolve-and-temper edit 2): `decision/choose.py::temper`, the person's own factor on the choice
temperature, read from the uses row `choice_temper`. THE SIGN (CR-93, `B10.51`): `about_mid` RISES with the attribute,
so a temperature that FALLS with Focus (AR-23) is a NEGATIVE `temper_gain`; the shipped gain is the control, 0.
THE FALSIFIER: the low-Focus person departing from the score's top no more often than the high-Focus one at a
negative gain (the hook is not on the draw), or any person's temper differing from 1.0 at gain 0.

B10.29 (CHAR resolve-and-temper edit 4 with U5a §1): `harness/decision_spread.py --retest`, self-agreement and between-person
agreement of the sampled top over a stated number of draw ticks. THE FALSIFIER: self-agreement not moving with Focus at a
negative gain (the hook is not on the draw), or the realm's self-agreement at or below its between-person agreement at a swept gain."""
from __future__ import annotations

import math

from ..boot.realm import build_realm
from ..decision.sheet import creation_sheet, development_space, seat, take_ranked
from ..decision import make_chooser
from ..data.fixtures import DEFAULT_FIXTURES
from ..decision import choose as CH
from ..decision.choose import _sample_order, temper
from ..harness import decision_spread as DS
from ..harness.play_surface import dispatching_chooser
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..queries import person_q as PQ
from ..state.carriers import Candidate, Person
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
    pid = sorted(p for p, x in w.persons.items() if not x.is_cohort)[0]     # B21b.02: a guard cohort (`cohort_guard_*`) now sorts first and holds no pursuit
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


def _focused(focus, pid="p_b1028"):
    p = Person(id=pid, name=pid)
    p.attributes = {"attr.mind.focus": focus}
    return p


def test_temper_is_one_at_gain_zero():
    w = build_realm(0)
    shipped = w.fixtures
    live = shipped.sweep("temper_gain", -0.5)
    checked = 0
    for p in w.persons.values():
        if not (getattr(p, "attributes", None) or {}).get("attr.mind.focus"):
            continue
        assert temper(p, shipped) == 1.0, "the shipped gain is the control: every person's factor is exactly 1"
        assert temper(p, shipped.sweep("temper_gain", 0)) == 1.0
        checked += 1
    assert checked >= 20, "the realm seats Focus on its persons"
    assert temper(Person(id="p_none", name="p_none"), live) == 1.0   # a person holding no Focus reads no factor
    low, mid, high = (temper(_focused(f), live) for f in (1, 4, 7))
    assert low > mid == 1.0 > high > 0.0, "a negative gain makes the factor fall as Focus rises (AR-23)"


def test_low_focus_departs_from_the_score_top_more_often():
    w = build_realm(0)
    cands = [Candidate("v_a", "x"), Candidate("v_b", "x"), Candidate("v_c", "x")]
    scores = {id(cands[0]): 0.0, id(cands[1]): -0.03, id(cands[2]): -0.06}
    score = lambda c: scores[id(c)]
    low, high = _focused(1), _focused(7)           # the same id, so the same twenty draws, differing only in Focus

    def tops(fx, seed):
        draw = draw_factory(seed, lambda: 0)
        return [_sample_order(list(cands), score, p, fx, draw)[0] is not cands[0] for p in (low, high)]

    live = w.fixtures.sweep("temper_gain", -0.5)
    off = {"low": 0, "high": 0}
    checked = 0
    for seed in range(20):
        a, b = tops(live, seed)
        off["low"] += a
        off["high"] += b
        assert _sample_order(list(cands), score, low, w.fixtures, draw_factory(seed, lambda: 0)) == \
            _sample_order(list(cands), score, high, w.fixtures, draw_factory(seed, lambda: 0))
        checked += 1
    assert checked >= 20
    assert off["low"] > off["high"], f"the low-Focus person departs from the score's top more often: {off}"


_RETEST_TICKS = DS.RETEST_TICKS      # the source's own reading: 46 cast x 6 referents x 5 ticks' draws


def test_high_focus_agrees_with_himself_more():
    cands = [Candidate("v_a", "x"), Candidate("v_b", "x"), Candidate("v_c", "x")]
    scores = {id(cands[0]): 0.0, id(cands[1]): -0.03, id(cands[2]): -0.06}
    score = lambda c: scores[id(c)]
    low, high = _focused(1), _focused(7)           # the same id, so the same draws, differing only in Focus
    ticks = 40

    def self_agreement(p, fx):
        tops = DS.redraw_tops(list(cands), score, p, fx, seed=0, ticks=ticks)
        assert len(tops) == ticks
        return DS.agreement([(c.verb, c.subject) for c in tops])

    live = DEFAULT_FIXTURES.sweep("temper_gain", -0.5)
    (k_low, n_low), (k_high, n_high) = self_agreement(low, live), self_agreement(high, live)
    assert n_low == n_high == ticks * (ticks - 1) // 2 >= 700
    assert k_high > k_low, f"the high-Focus person takes the same first act on a redraw more often: {k_high} against {k_low} of {n_low}"
    assert self_agreement(low, DEFAULT_FIXTURES) == self_agreement(high, DEFAULT_FIXTURES), "at gain 0 Focus moves nothing"
