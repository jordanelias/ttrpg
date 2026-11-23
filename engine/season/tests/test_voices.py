"""B10.54 (`02_CHAR_voices_and_the_room` edits 1-4) -- A CHOICE READ BACK AS ITS SCORE PARTS, AND WHICH ARE HEARD:
`decision/score_parts.py`; B10.55 (edit 5) -- THE ROOM A PERSON BELIEVES HE STOOD IN: `person_q.regard_parts`, `room_as_held`,
`chronicle.present_at`, `witness_regard`. Lane: the season loop.

THE FALSIFIER: (a) a `watch` that calls `score_parts` and `heard` on every deliberation moves `World.content_hash()` -- a voice is steering;
(b) the parts of a candidate do not sum to its `score_terms` -- a player would be shown reasons that did not decide. The realm half
runs ONE season here; the two-season reading is the commit's.
"""
from __future__ import annotations

import math

from engine.dice_engine.fmath import ltr_sum
from engine.substrate.descriptors import AFFILIATION_CONCERNS, HERITAGE_ENGAGES, PURSUITS

from ..boot.realm import seed_self_knowledge
from ..data import goals as goals_data
from ..data import verbs as V
from ..data.fixtures import DEFAULT_FIXTURES
from ..data.pursuits import to_axes
from ..data.affiliations import AFFILIATION_CEILING
from ..data.rosters import PURSUIT_AXES, REGARD_UNITS, SEEN_PREDICATE
from ..data.verbs import VERB_TABLE
from ..decision import choose as CH
from ..decision import score_parts as SP
from ..epistemic import Seen
from ..harness import chronicle
from ..harness import probes as P
from ..queries import person_q as PQ
from ..queries.cache import deposit_index
from ..state.carriers import Act, Candidate, Claim, Event, Person, Question, Tenure, interior_of

_SUBJECT, _TO = "p_vc_subject", "p_vc_to"


def _person():
    """Fifteen pursuits at distinct weights (so no part is hidden by a tie), a stance on `_SUBJECT`, a live commit to the first goal."""
    goal = goals_data.goals()[0]
    p = Person(id="p_vc", name="p_vc", pursuits={e: 1.0 + 0.1 * i for i, e in enumerate(sorted(PURSUITS))}, stance=[(_SUBJECT, 3, 2), (_TO, 2, 4)])
    p.tenures.append(Tenure("t_vc", p.id, goal.id, "commit", 0))
    w = P.tiny_world()
    w.persons[p.id] = p
    seed_self_knowledge(w)      # B10.65: he recognises every pursuit he holds, as the realm builds him
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


def _judging_person():
    """A person who regards `_SUBJECT` by every addend: a stance row, a firsthand deed claim, a told one, and a sighting that names a heritage
    whose concern he stands wholly for."""
    p, _ = _person()
    axis_w = PQ.projected_axes(p, 0.0)
    kinds = [k for k in sorted(V.DEED_KINDS) if k not in PQ.PAIRED_KINDS
             and PQ.deed_term(p, axis_w, Claim("k", p.id, _SUBJECT, k, True, 2, "firsthand", 100, "own")) != 0.0]
    assert len(kinds) >= 2, "the tables moved: fewer than two unpaired deed kinds score for this person"
    heritage = sorted(HERITAGE_ENGAGES)[0]
    for a in AFFILIATION_CONCERNS[HERITAGE_ENGAGES[heritage]]:
        p.conviction[a] = AFFILIATION_CEILING
    p.ledger += [Claim("d1", p.id, _SUBJECT, kinds[0], True, 2, "firsthand", 100, "own"),
                 Claim("d2", p.id, _SUBJECT, kinds[1], True, 2, "told_by", 100, "own", chain=(_TO,)),
                 Claim("s1", p.id, _SUBJECT, SEEN_PREDICATE, Seen(who=_SUBJECT, marks=(heritage,)), 2, "firsthand", 100, "own")]
    return p


def test_regard_parts_sum_to_regard():
    p = _judging_person()
    assert PQ.regard_parts(p, _SUBJECT).stored == PQ.regard(p, _SUBJECT) == PQ.stance_toward(p, _SUBJECT)       # no `fx`: the stored half exactly
    for unit in sorted(REGARD_UNITS):
        fx = DEFAULT_FIXTURES.sweep("regard_unit", unit)
        parts = PQ.regard_parts(p, _SUBJECT, fx)
        judged, told = (PQ.deeds_judged_steps if unit == "stance" else PQ.deeds_judged)(p, _SUBJECT, fx.get("scar_weight_shift"), fx.get("sworn_bond"),
                                                                                           fx.get("deed_counterparty"))
        assert parts.judged == fx.get("judged_gain") * judged and parts.told == fx.get("told_valence_gain") * told, unit
        assert parts.heritage == PQ.heritage_regard(p, _SUBJECT, fx), unit
        assert 0.0 not in (parts.stored, parts.judged, parts.told, parts.heritage), (unit, parts)           # every addend is observed carrying something
        assert PQ.regard(p, _SUBJECT, fx) == parts.stored + parts.judged + parts.told + parts.heritage, unit    # exactly, in the one addition order
        assert SP.history(p, SP.ScorePart("stance", _SUBJECT, 1.0), fx) == parts, unit


def test_room_as_held_names_only_what_the_actor_holds():
    w = P.tiny_world()
    actor, seen_by, unseen = "p_low", "p_mid", "p_other"
    w.acts.append(Act("a_vc", actor, "petition", payload={}))
    w.log.append(Event("ev_act", "petition.filed", [], ["a_vc"], 0))
    for pid in (actor, seen_by, unseen):                                    # each holds a claim deposited from the act's Event
        w.persons[pid].ledger.append(Claim(f"c_{pid}", pid, actor, "petition.filed", True, 0, "firsthand", 100, "own"))
        w.log.append(Event(f"ev_dep_{pid}", "claim.deposited", [P.apparatus_receipt(w, f"c_{pid}", "set", "Event")], ["ev_act"], 0))
    w.persons[unseen].stance.append((actor, -5, 5))                          # a witness the actor holds nothing of, and who holds him hostile
    w.persons[actor].ledger.append(Claim("c_saw", actor, "site_harbour", SEEN_PREDICATE, Seen(who=seen_by), 0, "firsthand", 100, "own"))
    deposited = deposit_index(w)["ev_act"]
    assert chronicle.present_at(w, "ev_act") == tuple(sorted((actor, seen_by, unseen)))        # world truth: all three stood there
    truth = dict(chronicle.witness_regard(w, "ev_act", DEFAULT_FIXTURES))       # the chronicle's reading: what each present person holds of him
    assert set(truth) == {seen_by, unseen} and truth[unseen]["stored"] == -25.0 and truth[seen_by]["stored"] == 0.0, truth
    room = dict(PQ.room_as_held(interior_of(w.persons[actor], 0, 0), "ev_act", DEFAULT_FIXTURES, deposited))
    assert set(room) == {seen_by} and room[seen_by]["seen"] == 1 and room[seen_by]["told"] == room[seen_by]["bond"] == 0, room   # he holds no claim of `unseen`
    w.persons[actor].ledger.append(Claim("c_told", actor, actor, "petition.filed", True, 1, "told_by", 100, "own", chain=(unseen,)))
    told = dict(PQ.room_as_held(interior_of(w.persons[actor], 0, 0), "ev_act", DEFAULT_FIXTURES, deposited))
    assert set(told) == {seen_by, unseen} and told[unseen]["told"] == 1, told         # the control: once he holds one, he names him
    assert PQ.room_as_held(interior_of(w.persons[actor], 0, 0), "ev_act", DEFAULT_FIXTURES, ()) == ()          # no claim of his is of that Event: no room
