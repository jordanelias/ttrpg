"""B10.54 (`02_CHAR_voices_and_the_room` edits 1-4) -- A CHOICE READ BACK AS ITS SCORE PARTS, AND WHICH ARE HEARD:
`decision/score_parts.py`. Lane: the season loop.

THE FALSIFIER: (a) a `watch` that calls `score_parts` and `heard` on every deliberation moves `World.content_hash()` -- a voice is steering;
(b) the parts of a candidate do not sum to its `score_terms` -- a player would be shown reasons that did not decide. The realm half
runs ONE season here; the two-season reading is the commit's.
"""
from __future__ import annotations

import math

from engine.dice_engine.fmath import ltr_sum
from engine.substrate.descriptors import PURSUITS

from ..data import goals as goals_data
from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.pursuits import to_axes
from ..data.rosters import PURSUIT_AXES
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..decision import score_parts as SP
from ..state.carriers import Candidate, Claim, Person, Question, Tenure

_SUBJECT, _TO = "p_vc_subject", "p_vc_to"


def _person():
    """Fifteen pursuits at distinct weights (so no part is hidden by a tie), a stance on `_SUBJECT`, a live commit to the first goal."""
    goal = goals_data.goals()[0]
    p = Person(id="p_vc", name="p_vc", pursuits={e: 1.0 + 0.1 * i for i, e in enumerate(sorted(PURSUITS))}, stance=[(_SUBJECT, 3, 2), (_TO, 2, 4)])
    p.tenures.append(Tenure("t_vc", p.id, goal.id, "commit", 0))
    return p, Question(f"q:need:{goal.id}", "need", (_SUBJECT,), goal.id)


def _live():
    """Every term live: the shipped gains' controls swept ON, the believed-odds arm, a conferrer's fit."""
    return (DEFAULT_FIXTURES.sweep("aim_gain", 1.0).sweep("risk_gain", 1.0).sweep("confer_fit_weight", 1.0)
            .sweep("odds_weighting", "believed").sweep("scar_weight_shift", 0.0))


def _candidates():
    """One candidate per verb row; a row that seats a person (a `to` counterparty on an Office) is given a `to`."""
    seats = [v for v, r in VERB_TABLE.items() if r.referent_class == "Office" and r.counterparty == "to"]
    assert seats, "no row seats a person: the fit term is unobserved and the tables moved under this test"
    return [Candidate(v, "seat_vc" if v in seats else _SUBJECT, {"to": _TO} if v in seats else {}) for v in sorted(VERB_TABLE)]


def _odds(act, bands):
    return 0.4


def _scored(p, q, fx, c):
    memo = CH.deliberation_memo(p, fx)
    terms = CH.score_terms(p, c, fx, memo, _odds, q)
    return terms, SP.score_parts(p, c, fx, memo, _odds, q)


def test_score_parts_sum_to_the_score():
    p, q = _person()
    fx = _live()
    kinds, checked = set(), 0
    for c in _candidates():
        terms, parts = _scored(p, q, fx, c)
        kinds |= {x.kind for x in parts}
        total = math.fsum(terms)
        biggest = max((abs(x.pull) for x in parts), default=0.0)
        assert abs(math.fsum(x.pull for x in parts) - total) <= len(parts) * math.ulp(biggest) * 2, c.verb     # summation reorder: n ulp of the largest part (x2: the terms' own rounding)
        pulls = [abs(x.pull) for x in parts]
        assert pulls == sorted(pulls, reverse=True), c.verb
        owners = [x.owner for x in parts if x.kind == "pursuit"]
        assert len(owners) == len(set(owners)), c.verb                                           # each held pursuit once
        axes = {ax: V.align(c.verb, ax) for ax in PURSUIT_AXES}
        for e in p.pursuits:                                                                     # a held pursuit with a non-zero part is heard
            if ltr_sum(to_axes({e: p.pursuits[e]})[ax] * axes[ax] for ax in PURSUIT_AXES) != 0.0 and terms[0] != 0.0:
                assert e in owners, (c.verb, e)
        checked += 1
    assert checked == len(VERB_TABLE) and kinds == set(SP.ATTRIBUTED_TERMS), kinds          # every term was observed owning a part


def test_attributed_terms_equals_score_terms_length():
    p, q = _person()
    fx = _live()
    terms = CH.score_terms(p, _candidates()[0], fx, CH.deliberation_memo(p, fx), _odds, q)
    assert len(terms) == len(SP.ATTRIBUTED_TERMS) == len(CH.TERM_NAMES)
    assert SP.ATTRIBUTED_TERMS == CH.TERM_NAMES


def test_heard_names_who_carried_and_who_dissented_and_that_the_draw_departed():
    p, q = _person()
    fx = _live()
    seen_dissent = False
    for c in _candidates():
        terms, parts = _scored(p, q, fx, c)
        total = math.fsum(terms)
        if not parts or total == 0.0:
            continue
        sign = 1.0 if total > 0 else -1.0
        loud = SP.heard(parts, total, floor=0.0)
        carried = max((x for x in parts if x.pull * sign > 0), key=lambda x: abs(x.pull))
        assert loud[0] == carried
        against = [x for x in parts if x.pull * sign < 0]
        quiet = SP.heard(parts, total, floor=math.inf)                         # nothing reaches an infinite floor
        assert quiet == (carried,) and len(loud) <= 2
        if against:
            seen_dissent = True
            assert loud[1] == max(against, key=lambda x: abs(x.pull))
            near = abs(loud[1].pull)
            assert SP.heard(parts, total, floor=near / abs(total) * 0.99)[-1] == loud[1]         # a hair below its share: heard
            assert len(SP.heard(parts, total, floor=near / abs(total) * 1.01)) == 1      # a hair above: not
        drew = SP.heard(parts, total, drew_off=0.25)
        assert drew[-1].kind == "draw" and drew[-1].pull < 0 and SP.heard(parts, total) == SP.heard(parts, total, drew_off=None)
    assert seen_dissent, "no candidate had a part against its total: the dissent arm was never observed"


def test_a_pursuit_voice_cites_its_scar_count_and_the_newest_claim_it_scored():
    p, q = _person()
    e = sorted(PURSUITS)[0]
    axes = {ax: w for ax, w in to_axes({e: 1.0}).items() if w}
    scored = [k for k in sorted(V.DEED_KINDS) if any(V.align_kind(k, ax) for ax in axes)]
    unscored = [k for k in sorted(V.DEED_KINDS) if not any(V.align_kind(k, ax) for ax in axes)]
    assert scored and unscored, "the tables moved: no deed kind scores on this pursuit's axes, or all do"
    p.scar[e] = 2
    p.ledger += [Claim("c1", p.id, _SUBJECT, scored[0], True, 1, "firsthand", 100, "own"),
                 Claim("c2", p.id, _SUBJECT, scored[-1], True, 3, "firsthand", 100, "own"),
                 Claim("c3", p.id, _SUBJECT, unscored[0], True, 5, "firsthand", 100, "own")]       # newer, but not scored on `e`'s axes
    cite = SP.history(p, SP.ScorePart("pursuit", e, 0.5))
    assert cite.scar == 2 and cite.claim.id == "c2"
    assert SP.history(p, SP.ScorePart("pursuit", sorted(PURSUITS)[1], 0.5)).scar == 0
    assert SP.history(p, SP.ScorePart("stance", _SUBJECT, 0.5)) is None            # the stance voice's regard parts land with B10.55
