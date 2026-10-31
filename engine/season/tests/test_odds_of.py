"""CP-T01-03 -- `seam/wrappers/sigma.py::odds_of`, the exact odds of the social roll an act would deal,
in two input modes, and `believed_input`, the person's own record.

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * MODE (a) IS THE DEALT NUMBER: 20,000 real `roll()` calls on the record the act's resolution builds,
    graded by the real ladder, agree with `odds_of` within three standard errors in every band; and the
    obstacle it grades against is the module's (replace `obstacle` and the odds follow it).
  * IT IS READ-ONLY: no World field changes, no rng is touched.
  * MODE (b) READS ONLY THE PERSON'S OWN LEDGER: a person who holds no claim on the opposition gets
    `None`, never a figure; one who holds a claim gets a tuple that differs from mode (a)'s where his
    belief differs from the true value, and equals it where it does not; `believed_input` takes no World.
  * A non-person subject needs no claim (the module's stand-in is known), a Record's forgery quality and
    a bench's reception are unknown to the believer unless he passes his own room.
"""
from __future__ import annotations

import inspect
import math
import random
from dataclasses import asdict

import pytest

from engine.dice_engine.dice_engine import DEGREE_LABEL, DEGREE_ORDINAL, Degree
from engine.dice_engine.sigma_leverage import band_odds, net_boost, settle_record
from engine.substrate import composition

from ..data.fixtures import DEFAULT_FIXTURES
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..seam import ladder
from ..seam.wrappers import sigma
from ..state.carriers import Act, Claim

KEY = "copying"          # the capability key `tell` draws on (`VERB_CAPABILITY`); asserted below


def _module():
    import importlib
    return importlib.import_module(composition.ROLES["social_contest.roll"]["target"].split(":", 1)[0])


def _world(*, mid=10, other=3):
    w = P.tiny_world(DEFAULT_FIXTURES)
    SeasonDriver(w)                                   # the registrar fills MODULE_ENTRIES
    # roster-exempt: TEST FIXTURE capabilities -- a strong and a weak hearer, and a speaker at pool 4.
    w.persons["p_mid"].capability = {KEY: mid}
    w.persons["p_other"].capability = {KEY: other}
    w.persons["p_low"].capability = {KEY: 4}
    return w


def _tell(to, actor="p_low"):
    return Act(id=f"a:{actor}:{to}", actor=actor, verb="tell", payload={"to": to})


def _claim(holder, subject, value, *, when=0, confidence=5):
    return Claim(id=f"c:{holder}:{subject}:{when}", holder=holder, subject=subject,
                 predicate=sigma.CAPABILITY_CLAIM + KEY, value=value, when=when,
                 source="told", confidence=confidence, visibility="own")


def test_the_verb_draws_on_the_key_these_tests_assume():
    from ..data.rosters import VERB_CAPABILITY
    assert VERB_CAPABILITY["tell"] == KEY


def test_mode_a_equals_the_dealt_distribution_within_three_standard_errors():
    w = _world()
    act = _tell("p_mid")
    odds = sigma.odds_of(w, act)
    assert odds is not None and math.isclose(sum(odds), 1.0, abs_tol=1e-12)
    # the record the resolution builds for this act, rolled for real
    inp = sigma.contest_input(w, ["p_low", "p_mid"], verb="tell", subject="p_mid")
    mod = _module()
    n = 20_000
    rng = random.Random(7)
    tally = [0, 0, 0, 0]
    labels = {v: k for k, v in DEGREE_LABEL.items()}
    for _ in range(n):
        # dealt as the host deals it: the entry's margin, its fraction settled by the act's own draw
        # (CP-T01-06's per-pool cap composes a fractional obstacle here, so the fraction rule is live)
        margin = mod.roll(inp, rng)
        settled = settle_record(margin.net, inp.leverage, inp.pool, margin.ob, rng.random)
        band = labels[ladder.degree_of({**asdict(margin), "settled_margin": settled})]
        tally[DEGREE_ORDINAL[band]] += 1
    seen = 0
    for i, p in enumerate(odds):
        se = math.sqrt(max(p * (1 - p), 1e-12) / n)
        assert abs(tally[i] / n - p) <= 3 * se + 1e-9, (i, tally[i] / n, p)
        seen += 1
    assert seen == 4 and odds != (1.0, 0.0, 0.0, 0.0)


def test_mode_a_grades_against_the_modules_obstacle_and_follows_it(monkeypatch):
    w = _world()
    act = _tell("p_mid")
    before = sigma.odds_of(w, act)
    inp = sigma.contest_input(w, ["p_low", "p_mid"], verb="tell", subject="p_mid")
    assert before == band_odds(inp.pool, _module().obstacle(inp), net_boost(inp.leverage, inp.pool))
    monkeypatch.setattr(_module(), "obstacle", lambda i: 1.0)
    moved = sigma.odds_of(w, act)
    assert moved == band_odds(inp.pool, 1.0, 0.0) and moved != before


def test_mode_a_is_read_only():
    w = _world()
    act = _tell("p_mid")
    h = w.content_hash()
    sigma.odds_of(w, act)
    sigma.odds_of(w, act, believer=w.persons["p_low"])
    assert w.content_hash() == h


def test_an_act_the_social_roll_does_not_deal_has_no_odds():
    w = _world()
    assert sigma.odds_of(w, Act(id="a:x", actor="p_low", verb="no_such_verb")) is None
    assert sigma.odds_of(w, Act(id="a:y", actor="not_a_person", verb="tell",
                                payload={"to": "p_mid"})) is None


# ---- mode (b) -----------------------------------------------------------------------------------

def test_mode_b_with_no_claim_on_the_opposition_is_none_never_a_figure():
    w = _world()
    p = w.persons["p_low"]
    assert p.ledger == []
    assert sigma.odds_of(w, _tell("p_mid"), believer=p) is None
    # a claim about somebody else is no claim on THIS opposition
    p.ledger.append(_claim("p_low", "p_other", 3))
    assert sigma.odds_of(w, _tell("p_mid"), believer=p) is None


def test_mode_b_with_a_claim_differs_from_mode_a_where_the_belief_differs_and_equals_it_where_not():
    w = _world()
    p = w.persons["p_low"]
    act = _tell("p_other")                             # true opposition 3 -> obstacle 1.5
    true = sigma.odds_of(w, act)
    p.ledger.append(_claim("p_low", "p_other", 3))     # he believes the truth
    assert sigma.odds_of(w, act, believer=p) == true
    p.ledger.append(_claim("p_low", "p_other", 1, when=1))   # a later, wrong belief: obstacle 0.5
    wrong = sigma.odds_of(w, act, believer=p)
    assert wrong is not None and wrong != true
    assert wrong == band_odds(4, 0.5, 0.0)


def test_mode_b_takes_the_latest_then_the_most_confident_claim():
    w = _world()
    p = w.persons["p_low"]
    act = _tell("p_other")
    p.ledger += [_claim("p_low", "p_other", 6, when=0, confidence=9), _claim("p_low", "p_other", 3, when=1, confidence=1)]
    assert sigma.odds_of(w, act, believer=p) == sigma.odds_of(w, act)


def test_mode_b_reads_the_ledger_and_not_the_world():
    assert "w" not in inspect.signature(sigma.believed_input).parameters
    w = _world()
    p = w.persons["p_low"]
    p.ledger.append(_claim("p_low", "p_other", 3))
    # the true state moves; the believer's answer does not
    act = _tell("p_other")
    before = sigma.odds_of(w, act, believer=p)
    w.persons["p_other"].capability = {KEY: 1}
    assert sigma.odds_of(w, act, believer=p) == before
    assert sigma.odds_of(w, act) != before


def test_mode_b_for_a_non_person_subject_needs_no_claim_and_a_record_or_room_is_unknown():
    w = _world()
    p = w.persons["p_low"]
    fx = w.fixtures
    # a non-person subject: the module's stand-in obstacle is known to him
    inp = sigma.believed_input(p, "tell", "somewhere", fx, person_subject=False)
    assert inp is not None and inp.opposition is None
    assert sigma._odds_of_input(inp) == band_odds(4, fx.get("obstacle_default"), 0.0)
    # an examined Record's forgery quality, and a bench's terms, are unknown unless he supplies them
    assert sigma.believed_input(p, "tell", "r1", fx, person_subject=False, examined_record=True) is None
    assert sigma.believed_input(p, "tell", "x", fx, person_subject=False, heard=True) is None
    room = sigma.believed_input(p, "tell", "x", fx, person_subject=False, heard=True,
                                room={"reception": 1.0, "proofs": 0.0})
    assert room is not None and room.reception == 1.0


def test_mode_b_is_only_the_actors_own_odds():
    w = _world()
    other = w.persons["p_mid"]
    other.ledger.append(_claim("p_mid", "p_other", 3))
    assert sigma.odds_of(w, _tell("p_other", actor="p_low"), believer=other) is None
