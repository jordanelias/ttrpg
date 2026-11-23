"""B10.31 (`02_CHAR_what_an_act_risks` edits 1-5) -- WHAT AN ACT RISKS: `decision/choose.py::score_terms`' `risk`, the tuple's fifth element
(`(pursuit, stance, fit, aim, risk)`), on a candidate whose row contests a prize `rosters.yaml: bodily_prizes` lists. Lane: the season loop.

    risk = - risk_gain * exposed * (1 - chance) * (1 + body_band_penalty) * nerve

THE FALSIFIERS: a candidate whose row contests no bodily prize changing score at any gain (the term leaked); a wounded person ranking an exposed
act no lower than a whole one (the body does not reach the term); a low-Spirit person ranking an exposed act no lower than a high-Spirit one at a
non-zero `nerve_gain` (the uses row does not reach the term). The realm-hash half (`risk_gain` 0: `build_realm(0)` one-season hash equal to the
tree before) is a reading recorded at the commit, not pinned here.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from engine.substrate.descriptors import PURSUITS
from ..data import rosters as R
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..decision.budget import body_band_penalty
from ..state.carriers import Candidate, Person

_SUBJECT = "p_risk_x"            # the one referent: a person no one holds a stance on
_VERBS = sorted(VERB_TABLE)


def _fx(gain, nerve=0.0):
    """Temperature 0 (the score order alone) and the believed-odds factor off, so a chance is asked only by the risk term."""
    return (DEFAULT_FIXTURES.sweep("choice_temperature", 0).sweep("odds_weighting", "none")
            .sweep("risk_gain", gain).sweep("nerve_gain", nerve))


def _person(pid, body=1000, spirit=None):
    """A person holding one pursuit (so the field's scores spread across the verb table, which is what lets a drop in one term change a RANK)
    and, where given, a Spirit. Two persons built with the same arguments but one are identical but for it."""
    p = Person(id=pid, name=pid)
    p.pursuits = {PURSUITS[0]: 5.0}
    p.body = body
    if spirit is not None:
        p.attributes = {"attr.spirit.will": spirit}
    return p


def _bodily(verb):
    row = VERB_TABLE[verb]
    return bool(row.contests) and row.contests in CH.BODILY_PRIZES


def _rank(p, gain, monkeypatch, nerve=0.0):
    """`make_ranker`'s real order of one candidate per verb of the table, on `_SUBJECT`."""
    monkeypatch.setattr(CH, "opening_set", lambda person, view, question, fx: [Candidate(v, _SUBJECT) for v in _VERBS])
    return [c.verb for c in CH.make_ranker(_fx(gain, nerve))(p, SimpleNamespace(question=object(), odds=None))]


def _terms(p, verb, gain, nerve=0.0, odds=None):
    fx = _fx(gain, nerve)
    return CH.score_terms(p, Candidate(verb, _SUBJECT), fx, CH.deliberation_memo(p, fx), odds)


def test_risk_is_zero_at_gain_zero_and_the_chance_is_not_asked():
    exposed = [v for v in _VERBS if _bodily(v)]
    assert len(exposed) >= 2, "fewer than two rows contest a bodily prize: the tables moved under this test"
    asked = []

    def odds(act, bands):
        asked.append(act.verb)
        return 0.5

    p = _person("p_risk_a")
    for v in exposed:
        t = _terms(p, v, 0.0, odds=odds)
        assert len(t) == 5 and str(t[4]) == "0.0", (v, t)          # exactly 0.0, no sign of zero
        assert CH.score_total(t) == t[0] + t[1] + t[2]
    assert asked == [], "the believed chance was asked at risk_gain 0"
    live = [_terms(p, v, 1.0, odds=odds)[4] for v in exposed]
    assert all(x < 0.0 for x in live) and len(asked) == len(exposed), "risk was not live at gain 1: the zero above observed nothing"


def test_a_wounded_person_ranks_an_exposed_act_lower(monkeypatch):
    whole, hurt = _person("p_risk_w"), _person("p_risk_h", body=50)
    assert body_band_penalty(whole, _fx(1.0)) == 0 and body_band_penalty(hurt, _fx(1.0)) > 0
    rw, rh = _rank(whole, 1.0, monkeypatch), _rank(hurt, 1.0, monkeypatch)
    exposed = [v for v in rw if _bodily(v)]
    assert len(exposed) >= 2
    for v in exposed:
        assert rh.index(v) > rw.index(v), f"{v}: the wounded person did not rank it lower ({rw.index(v)} -> {rh.index(v)})"
    assert _rank(whole, 0.0, monkeypatch) == _rank(hurt, 0.0, monkeypatch), "at gain 0 the wound alone parted two ranks"
    for v in (u for u in rw if not VERB_TABLE[u].contests):
        assert rh.index(v) <= rw.index(v) and _terms(hurt, v, 1.0)[4] == 0.0     # a row that contests nothing carries no risk, and only moves up


@pytest.mark.parametrize("gain", (0.5, 1.0))
def test_an_uncontested_candidate_is_unchanged_at_any_gain(gain):
    p = _person("p_risk_u", body=50)
    checked = 0
    for v in _VERBS:
        if _bodily(v):
            continue
        assert _terms(p, v, gain) == _terms(p, v, 0.0), f"{v} contests no bodily prize and scored differently at risk_gain {gain}"
        checked += 1
    assert checked >= 20


def test_spirit_moves_exposed_acts_through_the_uses_row(monkeypatch):
    row = R.CapabilityUse(use="choice_exposure", role="judgement", key="attr.spirit.will", side="actor", gain="nerve_gain")
    shipped = R.capability_uses()
    low, high = _person("p_risk_lo", spirit=1), _person("p_risk_hi", spirit=7)
    exposed = [v for v in _VERBS if _bodily(v)]
    # no row ships: with none planted the two read alike whatever Spirit they hold
    assert [_terms(low, v, 1.0, -0.5)[4] for v in exposed] == [_terms(high, v, 1.0, -0.5)[4] for v in exposed]
    monkeypatch.setattr(R, "capability_uses", lambda: shipped + (row,))
    rl, rh = _rank(low, 1.0, monkeypatch, -0.5), _rank(high, 1.0, monkeypatch, -0.5)
    for v in exposed:
        assert rl.index(v) > rh.index(v), f"{v}: the low-Spirit person did not rank it lower ({rh.index(v)} vs {rl.index(v)})"
        assert _terms(low, v, 1.0, -0.5)[4] < _terms(high, v, 1.0, -0.5)[4] < 0.0
        assert _terms(low, v, 1.0, 0.0)[4] == _terms(high, v, 1.0, 0.0)[4]       # at nerve_gain 0 the row reads 1.0 for both
    assert all(_terms(low, v, 1.0, -0.5)[4] == 0.0 for v in _VERBS if not VERB_TABLE[v].contests)


def test_a_better_believed_chance_lowers_the_risk():
    p = _person("p_risk_c")
    verb = next(v for v in _VERBS if _bodily(v) and CH._writing_bands(Candidate(v, _SUBJECT)))
    asked = []

    def at(chance):
        def odds(act, bands):
            asked.append(tuple(bands))
            return chance
        return odds

    sure, even, doubtful, unknown = (_terms(p, verb, 1.0, odds=at(c))[4] for c in (1.0, 0.5, 0.1, None))
    assert sure == 0.0 and doubtful < even < sure, (sure, even, doubtful)
    assert unknown == even == _terms(p, verb, 1.0, odds=None)[4]    # an answer of `None`, and no query at all, read `risk_unknown_chance` (0.5)
    assert asked and set(asked) == {CH._writing_bands(Candidate(verb, _SUBJECT))}     # the one query, asked of the bands the row writes
