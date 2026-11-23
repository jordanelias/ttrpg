"""B10.30 (`02_CHAR_goal_lean_on_its_own_question` edits 1-3) -- THE GOAL'S LEAN ON ITS OWN QUESTION: `decision/choose.py::score_terms`'
`aim`, the tuple's last element. Lane: the season loop.

THE FALSIFIER: two persons with identical pursuits, committed to two goals whose `pursuits:` point opposite ways, each handed
his goal's `need` question on one referent, rank one verb differently at `aim_gain` 1 and identically at 0; the same two handed
one `claim_landed` question rank alike at every gain. The realm-hash half (`aim_gain` 0: `build_realm(0)` one-season hash equal
to the tree before) is a reading recorded at the commit, not pinned here.
"""
from __future__ import annotations

from types import SimpleNamespace

import pytest

from ..data import goals as goals_data
from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.pursuits import to_axes
from ..data.rosters import PURSUIT_AXES
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..state.carriers import Candidate, Person, Question, Tenure

_SUBJECT = "p_goal_lean_x"        # the one referent: a person no one holds a stance on
_GAINS = (0.0, 0.5, 1.0, 2.0)     # `H-477`'s sweep


def _opposed():
    """`(goal a, goal b, verb va, verb vb)`: two goals whose projected leans order two verbs OPPOSITE ways by a clear margin,
    found by scanning the loaded tables with the data owners (`to_axes`, `align`), never `score_terms`."""
    goals, verbs = goals_data.goals(), sorted(VERB_TABLE)
    pull = {(g.id, v): sum(to_axes(g.pursuits)[ax] * V.align(v, ax) for ax in PURSUIT_AXES) for g in goals for v in verbs}
    for a in goals:
        for b in goals:
            for i, va in enumerate(verbs):
                for vb in verbs[i + 1:]:
                    if pull[(a.id, va)] - pull[(a.id, vb)] > 0.05 and pull[(b.id, va)] - pull[(b.id, vb)] < -0.05:
                        return a.id, b.id, va, vb
    raise AssertionError("no two goals lean two verbs opposite ways: the tables moved under this test")


def _person(pid, committed_to=(), ended=()):
    """A person with NO pursuits (so the pursuit term cannot part him from another) and a live `commit` to each of
    `committed_to`, an ended one to each of `ended`."""
    p = Person(id=pid, name=pid)
    for i, goal_id in enumerate(committed_to):
        p.tenures.append(Tenure(f"t_{pid}_{i}", pid, goal_id, "commit", 0))
    for i, goal_id in enumerate(ended):
        p.tenures.append(Tenure(f"te_{pid}_{i}", pid, goal_id, "commit", 0, until=1))
    return p


def _need(goal_id):
    return Question(f"q:need:{goal_id}", "need", (_SUBJECT,), goal_id)


def _claim_landed():
    return Question("q:claim:goal_lean", "claim_landed", (_SUBJECT,), "claim:goal_lean")


def _fx(gain):
    return DEFAULT_FIXTURES.sweep("choice_temperature", 0).sweep("aim_gain", gain)


def _rank(p, q, gain, verbs, monkeypatch):
    """`make_ranker`'s real order of `verbs` (one candidate each, on `_SUBJECT`) for `p` handed `q`, at `aim_gain` `gain`."""
    monkeypatch.setattr(CH, "opening_set", lambda person, view, question, fx: [Candidate(v, _SUBJECT) for v in verbs])
    return [c.verb for c in CH.make_ranker(_fx(gain))(p, SimpleNamespace(question=q, odds=None))]


def _aims(p, q, gain, verbs):
    """`score_terms`' `aim` element (the fourth: `risk` follows it, B10.31) for each of `verbs`, as the chooser scores them for `q`."""
    fx = _fx(gain)
    memo = CH.deliberation_memo(p, fx)
    return [CH.score_terms(p, Candidate(v, _SUBJECT), fx, memo, None, q)[3] for v in verbs]


def test_aim_is_zero_at_gain_zero():
    ga, gb, va, vb = _opposed()
    pa = _person("p_gl_a", [ga])
    zero, live = _aims(pa, _need(ga), 0.0, (va, vb)), _aims(pa, _need(ga), 1.0, (va, vb))
    assert zero == [0.0, 0.0] and all(str(x) == "0.0" for x in zero)       # exactly 0.0, no sign of zero
    assert any(x != 0.0 for x in live), "aim was 0 at gain 1 too: the zero above observed nothing"
    # a score is its terms' sum, and at the control `aim` adds nothing to it
    fx = _fx(0.0)
    memo = CH.deliberation_memo(pa, fx)
    t = CH.score_terms(pa, Candidate(va, _SUBJECT), fx, memo, None, _need(ga))
    assert CH.score_total(t) == t[0] + t[1] + t[2]


def test_two_goals_with_opposite_leans_rank_one_verb_differently_on_their_own_question(monkeypatch):
    ga, gb, va, vb = _opposed()
    pa, pb = _person("p_gl_a", [ga]), _person("p_gl_b", [gb])
    at_zero = (_rank(pa, _need(ga), 0.0, (va, vb), monkeypatch), _rank(pb, _need(gb), 0.0, (va, vb), monkeypatch))
    at_one = (_rank(pa, _need(ga), 1.0, (va, vb), monkeypatch), _rank(pb, _need(gb), 1.0, (va, vb), monkeypatch))
    assert at_zero[0] == at_zero[1], f"identical persons ranked apart with the gain at 0: {at_zero}"
    assert at_one[0] != at_one[1], f"opposite goals, their own questions, gain 1, one ranking: {at_one}"
    assert at_one[0][0] == va and at_one[1][0] == vb      # each takes the verb his own goal leans toward


def test_a_claim_landed_question_ranks_alike_at_every_gain(monkeypatch):
    ga, gb, va, vb = _opposed()
    pa, pb = _person("p_gl_a", [ga]), _person("p_gl_b", [gb])
    checked = 0
    for gain in _GAINS:
        ra = _rank(pa, _claim_landed(), gain, (va, vb), monkeypatch)
        rb = _rank(pb, _claim_landed(), gain, (va, vb), monkeypatch)
        assert ra == rb, (gain, ra, rb)
        assert _aims(pa, _claim_landed(), gain, (va, vb)) == [0.0, 0.0]
        checked += 1
    assert checked == len(_GAINS)


@pytest.mark.parametrize("how", ["no commit", "ended commit", "own want", "another goal's question"])
def test_aim_is_read_only_where_he_holds_a_live_commit_to_the_goal_the_question_raised(how):
    ga, gb, va, vb = _opposed()
    p, q = {"no commit": (_person("p_gl_n"), _need(ga)),
            "ended commit": (_person("p_gl_e", ended=[ga]), _need(ga)),
            "own want": (_person("p_gl_w", [ga]), Question("q:need:prop_p_gl_w", "need", (_SUBJECT,), "prop_p_gl_w")),
            "another goal's question": (_person("p_gl_o", [ga]), _need(gb))}[how]
    other = _aims(p, q, 2.0, (va, vb))
    held = _aims(_person("p_gl_h", [ga]), _need(ga), 2.0, (va, vb))
    assert any(x != 0.0 for x in held), "a live commit read aim 0: the control observed nothing"
    # `another goal's question`: he holds a commit, to a different goal, so the question's goal is not his: aim 0
    assert other == [0.0, 0.0], (how, other)
