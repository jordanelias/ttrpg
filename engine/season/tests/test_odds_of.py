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
from engine.dice_engine.sigma_leverage import band_odds, net_boost

from ..data.verbs import VERB_TABLE   # B05.14: the act's level (`TASK_DIFFICULTY` is deleted)
from ..data.fixtures import DEFAULT_FIXTURES
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from engine.substrate import composition
from ..queries import person_q
from ..seam import ladder
from ..seam.wrappers import pool, sigma
from ..state.carriers import Act, Claim
from .test_sc01_obstacle_ceiling import _module

KEY = "copying"          # the capability key `tell` draws on (`VERB_CAPABILITY`); asserted below
TASK_DIFFICULTY = {"tell": DEFAULT_FIXTURES.get("difficulty_ob")[VERB_TABLE["tell"].difficulty]}   # B05.14: `tell`'s level's size, where lane A's number was


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
                 predicate=person_q.CAPABILITY_CLAIM + KEY, value=value, when=when,
                 source="told", confidence=confidence, visibility="own")


def test_the_verb_draws_on_the_key_these_tests_assume():
    from ..data.verbs import VERB_CAPABILITY
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
        # dealt as the host deals it: the entry's real margin (`net - ob`), quantised once at the ladder (B05.02)
        margin = mod.roll(inp, rng)
        band = labels[ladder.degree_of({**asdict(margin), "settled_margin": margin.net - margin.ob})]
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
    assert before == band_odds(inp.pool, _module().obstacle(inp)[0], net_boost(inp.leverage, inp.pool))
    monkeypatch.setitem(composition._CACHE, "social_contest.obstacle", lambda i: (1.0, ()))   # the row the provider reads (B03.12)
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
    assert with_room.reception != 0.0 and _module().obstacle(with_room)[0] != _module().obstacle(roomless)[0]
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
    # (1) the pool below the 1D floor. B05.09: a held 0 now scores `max(pool_default, 0)`, so the pool of 0 is the one a skill
    # row saying `untrained: none` gives a non-holder (no score, `faculty` 0), planted on the key `tell` draws on.
    import dataclasses
    from types import MappingProxyType
    from engine.substrate import descriptors
    row = dataclasses.replace(descriptors.CAPABILITIES[KEY], untrained="none")
    monkeypatch.setattr(descriptors, "CAPABILITIES", MappingProxyType({**descriptors.CAPABILITIES, KEY: row}))
    w.persons["p_low"].capability = {}
    assert sigma.odds_of(w, act) is None
    refused = sigma.resolve(w, ["p_low", "p_mid"], ["root"], prize, **claim())
    assert refused["status"] == "REFUSED" and refused["why"] == "S27.4" and refused["pool"] == 0, refused
    w.persons["p_low"].capability = {KEY: 4}                          # (2) a pool that holds, an obstacle that does not
    assert sigma.odds_of(w, act) is not None
    monkeypatch.setattr(_module(), "obstacle", lambda i: (1000.0, ()))       # what `resolve` rolls against
    monkeypatch.setitem(composition._CACHE, "social_contest.obstacle", lambda i: (1000.0, ()))   # what `odds_of` reads (B03.12)
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
    act = _tell("p_other")                             # true opposition 3 -> obstacle `tell`'s difficulty + 1.5 (B11 lane A)
    true = sigma.odds_of(w, act)
    p.ledger.append(_claim("p_low", "p_other", 3))     # he believes the truth
    assert sigma.odds_of(w, act, believer=p) == true
    p.ledger.append(_claim("p_low", "p_other", 1, when=1))   # a later, wrong belief: obstacle difficulty + 0.5
    wrong = sigma.odds_of(w, act, believer=p)
    assert wrong is not None and wrong != true
    # B11 lane A: the obstacle is the task's difficulty (`rosters.yaml: task_difficulty`) plus the score term, re-pinned
    # from `band_odds(4, 0.5, 0.0)` (the score term alone, before the difficulty)
    assert wrong == band_odds(4, TASK_DIFFICULTY["tell"] + 0.5, 0.0)


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
    # a non-person subject: the task's difficulty is known to him (B11 lane A: no stand-in; was `obstacle_default`)
    inp = sigma.believed_input(p, "tell", "somewhere", fx, pool=4, person_subject=False)
    assert inp is not None and inp.opposition is None
    assert sigma._odds_of_input(inp) == band_odds(4, TASK_DIFFICULTY["tell"], 0.0)
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
    monkeypatch.setattr(pool, "POOL_ADDENDS", list(pool.POOL_ADDENDS))
    sigma.register_pool_addend(lambda w_, who, verb: 2 if who.id == "p_low" else 0)
    after = sigma.odds_of(w, act, believer=p)
    assert after == band_odds(6, TASK_DIFFICULTY["tell"] + 1.5, 0.0) == sigma.odds_of(w, act) and after != before   # B11 lane A: was band_odds(6, 1.5, 0.0)


def test_mode_b_is_only_the_actors_own_odds():
    w = _world()
    other = w.persons["p_mid"]
    other.ledger.append(_claim("p_mid", "p_other", 3))
    assert sigma.odds_of(w, _tell("p_other", actor="p_low"), believer=other) is None


def _partial_or_better(odds):
    """The probability of any band above Failure (`odds` is `band_odds`'s tuple, Failure first)."""
    return sum(odds[1:])


def test_an_unauthored_hearer_is_not_harder_than_a_held_one():
    """B05.11 (TWO's falsifier, `10_DICE_one_score_two_roles.md` "The falsifier"): `odds_of` for a `tell` at an unauthored hearer
    equals the odds at a hearer holding the skill at `pool_default`, and a hearer holding it at a higher rank gives lower
    odds. The opposition is the opponent's skill SCORE: the resisting attribute (the verb row's `opposed_attribute`) is held at the
    ceiling by the unauthored hearer here and below the default by the held one, and neither moves it. FALSIFIER: lane A's
    `max(attribute, rank)` (the unauthored hearer opposes at 7 and the one holding the default at 2: the inversion TWO names)."""
    from engine.substrate import descriptors
    from ..data.verbs import VERB_TABLE
    w = _world()
    opposed = VERB_TABLE["tell"].opposed_attribute
    default = w.fixtures.get("pool_default")
    for pid, held, attr in (("p_mid", {}, descriptors.ATTRIBUTE_CEILING),      # unauthored, resolute
                            ("p_other", {KEY: default}, 1),                       # holds the skill at the untrained score, soft
                            ("p_king", {KEY: default + 3}, 1),                    # holds it higher, soft
                            ("p_high", {}, None)):                                # unauthored, no attributes held
        w.persons[pid].capability = dict(held)
        w.persons[pid].attributes = {} if attr is None else {opposed: attr}
    odds = {pid: sigma.odds_of(w, _tell(pid)) for pid in ("p_mid", "p_other", "p_king", "p_high")}
    assert all(o is not None for o in odds.values()), odds
    assert odds["p_mid"] == odds["p_other"] == odds["p_high"], odds              # the unauthored hearer is no harder than one at the default
    assert _partial_or_better(odds["p_king"]) < _partial_or_better(odds["p_other"]), odds   # a higher rank is harder to move


def test_raising_the_subjects_inquiry_score_lowers_partial_or_better_on_interrogate():
    """B05.11 (H-312's probe, which printed an unchanged tuple at every setting before): the `interrogate` row names `inquiry`
    and a resisting attribute; the subject's `inquiry` score alone moves the odds, the attribute (held at the ceiling) does not.
    CONTROL: the same subject at `pool_default` reads the unauthored subject's odds."""
    from engine.substrate import descriptors
    from ..data.verbs import VERB_CAPABILITY, VERB_TABLE
    w = _world()
    row = VERB_TABLE["interrogate"]
    assert VERB_CAPABILITY["interrogate"] == "inquiry" and row.opposed_attribute
    subject = w.persons["p_mid"]
    subject.attributes = {row.opposed_attribute: descriptors.ATTRIBUTE_CEILING}
    act = Act(id="a:p_low:p_mid", actor="p_low", verb="interrogate", payload={"subject": "p_mid"})
    seen = []
    for rank in (None, w.fixtures.get("pool_default"), 4, 7):
        subject.capability = {} if rank is None else {"inquiry": rank}
        seen.append(sigma.odds_of(w, act))
    assert all(o is not None for o in seen), seen
    assert seen[0] == seen[1], seen                                              # control: unauthored == the default
    moved = [_partial_or_better(o) for o in seen[1:]]
    assert moved[0] > moved[1] > moved[2], moved                                 # each step of the score lowers Partial-or-better


def test_score_reads_no_attribute():
    """B05.09 (TWO "Tests and lands"): the skill score the pool starts from has no attribute in it. A person holding the
    verb's attributes (governing and opposed) at the ceiling and no skill key scores the untrained score, `pool_default`; with a
    skill key below it, the same (a first rank is never a loss). B05.11 deleted the opposition's `attribute=` argument, so the
    attribute enters no score. FALSIFIER: lane A's `max(attribute, rank)` (the score of this person is 7)."""
    from engine.substrate import descriptors
    from ..data.verbs import VERB_TABLE
    w = _world()
    p = w.persons["p_low"]
    default = w.fixtures.get("pool_default")
    row = VERB_TABLE["tell"]
    p.attributes = {a: descriptors.ATTRIBUTE_CEILING for a in (*row.governing, row.opposed_attribute)}
    p.capability = {}
    assert pool.score(w, p, "tell") == default
    assert not hasattr(pool, "_opposing_attribute") and "attribute" not in inspect.signature(pool.score).parameters
    p.capability = {KEY: 1}
    # the pool (B05.25) is the governing mean, the rank and the addends: the attributes reach the dice there, and only there
    assert pool.score(w, p, "tell") == default and pool.faculty(w, p, "tell") == pool.governing_score(w, p, "tell") + 1 + sum(
        int(a(w, p, "tell")) for a in pool.POOL_ADDENDS)
