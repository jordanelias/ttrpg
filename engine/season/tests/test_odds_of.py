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

from ..data.fixtures import DEFAULT_FIXTURES
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..seam import ladder
from ..seam.wrappers import sigma
from ..state.carriers import Act, Claim
from .test_sc01_obstacle_ceiling import _module

KEY = "copying"          # the capability key `tell` draws on (`VERB_CAPABILITY`); asserted below


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
    _assert_dealt(odds, inp)
    assert odds != (1.0, 0.0, 0.0, 0.0)


N_DEALT = 20_000


def _dealt_tally(inp, n=N_DEALT, seed=7) -> list:
    """`n` real rolls of the record `inp`, graded by the real ladder: the bands the fold would deal."""
    mod = _module()
    rng = random.Random(seed)
    tally = [0, 0, 0, 0]
    labels = {v: k for k, v in DEGREE_LABEL.items()}
    for _ in range(n):
        # dealt as the host deals it: the entry's margin, its fraction settled by the act's own draw
        # (CP-T01-06's per-pool cap composes a fractional obstacle here, so the fraction rule is live)
        margin = mod.roll(inp, rng)
        settled = settle_record(margin.net, inp.leverage, inp.pool, margin.ob, rng.random)
        band = labels[ladder.degree_of({**asdict(margin), "settled_margin": settled})]
        tally[DEGREE_ORDINAL[band]] += 1
    return tally


def _within_3se(odds, tally, n) -> None:
    """`odds` agree with a dealt `tally` of `n` rolls within three standard errors in every one of the four bands."""
    seen = 0
    for i, p in enumerate(odds):
        se = math.sqrt(max(p * (1 - p), 1e-12) / n)
        assert abs(tally[i] / n - p) <= 3 * se + 1e-9, (i, tally[i] / n, p)
        seen += 1
    assert seen == 4


def _assert_dealt(odds, inp, n=N_DEALT) -> None:
    """`odds` agree with `n` real rolls of `inp` within three standard errors in every one of the four bands."""
    _within_3se(odds, _dealt_tally(inp, n), n)


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


def test_mode_a_speak_into_a_bench_shows_the_odds_the_room_deals():
    """`speak` is heard by a bench (`heard_by: bench`): `_rolled_as` hands the fold's rung as the room, so the
    bench's `reception` of the speaker moves the obstacle, and `odds_of` shows THAT number: it agrees with real
    rolls of the record built WITH the room, and differs from the same act's odds without one.

    MUTATION (run, reverted): `_rolled_as`'s `heard_by == BENCH` branch returning `None` for the room -- the
    room-less odds are shown, the `!= roomless` assertion and the 3 SE agreement both red."""
    from .test_sc02_reception import (HEARER, PARTY, SPEAKER, _judging_world, _kind_with_lean, _claim as _deed,
                                      _lean, _open as _open_case, _fold as _fold_acts, _kinds)
    from ..queries import world_q
    w, d = _judging_world()
    kind = _kind_with_lean(w, +1)
    for i in range(math.ceil(1.0 / _lean(w, kind)) + 1):           # the bench's member favours the speaker
        w.persons[HEARER].ledger.append(_deed(f"fav{i}", HEARER, SPEAKER, kind))
    assert _kinds(_fold_acts(w, d, _open_case("oc"))) == ["case.opened"]
    room = world_q.place_of(w, SPEAKER)
    assert world_q.reception(w, SPEAKER, room) > 0.0, "the fixture's bench does not receive the speaker"
    act = Act(id="a:speak", actor=SPEAKER, verb="speak", payload={"subject": PARTY})
    odds = sigma.odds_of(w, act)
    with_room = sigma.contest_input(w, [SPEAKER, PARTY], verb="speak", subject=PARTY, room=room)
    roomless = sigma.contest_input(w, [SPEAKER, PARTY], verb="speak", subject=PARTY)
    assert with_room.reception != 0.0 and _module().obstacle(with_room) != _module().obstacle(roomless)
    assert odds is not None and odds == sigma._odds_of_input(with_room)
    assert odds != sigma._odds_of_input(roomless), "the bench's reception moved no odds"
    _assert_dealt(odds, with_room)


def test_mode_a_research_on_a_forged_record_shows_the_odds_the_forgery_deals():
    """An inquiry has no prize and examines its subject: `_rolled_as` names the `graded_inquiries` route and
    the Record's `forgery_quality` enters the obstacle. Built at the SHIPPED arm (`trail_world`'s `fixtures`
    argument; its default sweeps `ceiling_per_pool` off, where the quality cannot raise the obstacle).
    FALSIFIER: the same investigator, the same Record with its quality set to 0, has other odds.

    MUTATION (run, reverted): the inquiry branch returning `examined=None` -- the Record's quality is
    dropped, the odds equal the unforged ones, and both assertions red."""
    from .test_fi03_trail import INVESTIGATOR, trail_world
    w, d, rid = trail_world(fixtures=DEFAULT_FIXTURES)
    assert w.fixtures.get("ceiling_per_pool") is True and w.records[rid].forgery_quality > 0
    act = Act(id="a:res", actor=INVESTIGATOR, verb="research", payload={"subject": rid})
    odds = sigma.odds_of(w, act)
    inp = sigma.contest_input(w, [INVESTIGATOR], verb="research", subject=rid, examined=rid)
    assert inp.forgery_quality > 0 and odds is not None and odds == sigma._odds_of_input(inp)
    _assert_dealt(odds, inp)
    w.records[rid].forgery_quality = 0                                # the control: a true document
    assert sigma.odds_of(w, act) != odds, "the forgery's quality moved no odds"


def test_mode_a_has_no_odds_where_s27_4_refuses_and_resolve_refuses_the_same_pair(monkeypatch):
    """S27.4: an obstacle above `obstacle_refusal_multiple` x pool deals no dice, so there is no distribution:
    `odds_of` is `None` and `resolve` returns REFUSED on the same pair. Two planted pairs (a pool of 0 against
    the stand-in obstacle; a pool of 4 against an obstacle the module composes at 1000), with the unrefused
    pair beside them as the control (a tuple, and RESOLVED).

    MUTATION (run, reverted): `_odds_of_input`'s early return deleted -- `record_odds` is asked for the
    refused pair and both planted cases red."""
    from ..data.verbs import VERB_TABLE
    w = _world()
    act = _tell("p_mid")
    prize = VERB_TABLE["tell"].contests
    claim = lambda: dict(verb="tell", subject="p_mid", rng=random.Random(3))
    control = sigma.resolve(w, ["p_low", "p_mid"], ["root"], prize, **claim())
    assert control["status"] == "RESOLVED" and sigma.odds_of(w, act) is not None
    w.persons["p_low"].capability = {KEY: 0}                          # (1) the pool below the 1D floor
    assert sigma.odds_of(w, act) is None
    refused = sigma.resolve(w, ["p_low", "p_mid"], ["root"], prize, **claim())
    assert refused["status"] == "REFUSED" and refused["why"] == "S27.4" and refused["pool"] == 0, refused
    w.persons["p_low"].capability = {KEY: 4}                          # (2) a pool that holds, an obstacle that does not
    assert sigma.odds_of(w, act) is not None
    monkeypatch.setattr(_module(), "obstacle", lambda i: 1000.0)
    assert sigma.odds_of(w, act) is None
    over = sigma.resolve(w, ["p_low", "p_mid"], ["root"], prize, **claim())
    assert over["status"] == "REFUSED" and over["pool"] == 4 and over["ob"] == 1000.0, over


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
    inp = sigma.believed_input(p, "tell", "somewhere", fx, pool=4, person_subject=False)
    assert inp is not None and inp.opposition is None
    assert sigma._odds_of_input(inp) == band_odds(4, fx.get("obstacle_default"), 0.0)
    # an examined Record's forgery quality, and a bench's terms, are unknown unless he supplies them
    assert sigma.believed_input(p, "tell", "r1", fx, pool=4, person_subject=False, examined_record=True) is None
    assert sigma.believed_input(p, "tell", "x", fx, pool=4, person_subject=False, heard=True) is None
    room = sigma.believed_input(p, "tell", "x", fx, pool=4, person_subject=False, heard=True,
                                room={"reception": 1.0, "proofs": 0.0})
    assert room is not None and room.reception == 1.0


def test_mode_b_pool_is_faculty_and_an_addend_moves_it(monkeypatch):
    """The believer's own pool is `faculty(w, believer, verb)`, the one reader: a registered addend moves
    mode (b) as it moves mode (a), while his belief about the opposition still comes from his ledger."""
    w = _world()
    p = w.persons["p_low"]
    p.ledger.append(_claim("p_low", "p_other", 3))
    act = _tell("p_other")
    before = sigma.odds_of(w, act, believer=p)
    assert before == sigma.odds_of(w, act)
    monkeypatch.setattr(sigma, "POOL_ADDENDS", list(sigma.POOL_ADDENDS))
    sigma.register_pool_addend(lambda w_, who, verb: 2 if who.id == "p_low" else 0)
    after = sigma.odds_of(w, act, believer=p)
    assert after == band_odds(6, 1.5, 0.0) == sigma.odds_of(w, act) and after != before


def test_mode_b_is_only_the_actors_own_odds():
    w = _world()
    other = w.persons["p_mid"]
    other.ledger.append(_claim("p_mid", "p_other", 3))
    assert sigma.odds_of(w, _tell("p_other", actor="p_low"), believer=other) is None
