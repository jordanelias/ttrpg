"""B10.04 -- regard read as a share of the stance bound, times `Fixtures stance_scale`
(`decision/choose.py::stance_term`; `U5a_CHAR_owed_amendments` §2).

`stance_scale` ships at its control, `STANCE_MAX`: the term is today's exactly (the realm hash is the control, recorded in
the commit). The test below observes what the sweep (0.2, 0.4, 0.8) is for: a man's loyalty to one person makes an act done
against him rare in his choices, and not impossible.

FALSIFIER: no draw takes the act against him at any swept value (the gap is out of the draw's reach), or more than half
do (the relationship no longer restrains).
"""
from __future__ import annotations

import random

from ..data.pursuits import pursuit
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..decision.options import opening_set, subject_is_opponent
from ..harness import probes as P
from ..state.carriers import Question, View

A, B = "p_mid", "p_low"          # `probes.tiny_world`: both at the hearth `Hh`
DRAWS = 200
SWEPT = (0.2, 0.4, 0.8)


def _takes_the_act_against_him(v: float) -> tuple[int, int]:
    """`(takes, checked)` over `DRAWS` draws of one deliberation: `A`, with an authored stance of 10 toward `B`, answers one
    question about `B`; `takes` counts the draws whose first pick is an act the verb row treats as against its subject
    (`subject_is_opponent`, the sign `_stance_arm` reads under the shipped `declared` arm)."""
    w = P.tiny_world()
    p, fx = w.persons[A], w.fixtures.sweep("stance_scale", v)
    p.stance.append((B, 2, 5))                              # valence 2 x weight 5 = 10
    # [JUSTIFIED: the pull of his own pursuits toward the act against B -- `speak` is the one opponent row this question forms, and
    # its alignment is small on every axis, so a negative weight on `stewardship` (humble: speak -0.4 on `grandiose_humble`) is the
    # only plant that makes it his pursuits' top; one fixed value across the sweep, not tuned per swept value]
    p.pursuits = {pursuit("stewardship"): -2.0}
    q = Question("q:regard-unit", "need", (B,), B)
    cands = opening_set(p, View(A, [], fx.get("view_k"), q), q, fx)
    memo = CH.deliberation_memo(p, fx)
    scores = {id(c): CH.score_total(CH.score_terms(p, c, fx, memo, None)) for c in cands}
    ranked = CH.score_order(cands, scores)
    takes = checked = 0
    for s in range(DRAWS):
        def draw(pid, purpose, s=s):
            return random.Random(f"{s}|{pid}|{purpose}")
        top = CH._sample_order(ranked, lambda c: scores[id(c)], p, fx, draw)[0]
        checked += 1
        takes += subject_is_opponent(VERB_TABLE[top.verb]) and top.subject == B
    return takes, checked


def test_a_strong_loyalty_makes_acting_against_rare_not_impossible():
    got = {}
    for v in SWEPT:
        takes, checked = _takes_the_act_against_him(v)
        assert checked >= DRAWS, v
        assert takes < DRAWS / 2, f"at {v} {takes} of {checked}: the relationship no longer restrains"
        got[v] = takes
    assert max(got.values()) > 0, f"0 of {DRAWS} at every swept value: the gap is out of the draw's reach, {got}"
    assert got[0.2] >= got[0.4] >= got[0.8], f"a larger scale must not restrain less: {got}"

