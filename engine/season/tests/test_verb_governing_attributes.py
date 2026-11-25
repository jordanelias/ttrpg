"""B05.25 -- THE VERB ROW NAMES ITS ATTRIBUTES, ITS AUTHORITY OR ITS SUBSYSTEM; THE POOL IS THE ATTRIBUTES' MEAN PLUS THE SKILL
RANK; A BRUTE VERB NEVER ROLLS (`2026-11-13-verb-governing-attributes` §0, §2, §4; B05.24's sentence).

THE RULE UNDER TEST: a verb names one to three attributes (`governing:`), his governing score for it is the mean of his scores
in them (an attribute he does not hold reads at `pool_default`), to the nearest tenth, a half up, a FRACTIONAL number; his rank in
the verb's skill is added; that plus the base, never below the floor, is the dice (`pool.faculty`). A verb that is a brute
function (`brute: seat | own | counterparty`) names none and never rolls; a verb that hands its act to a module that reads the
person by its own rule (the prize's `person_inputs: own`) names none either.

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * EVERY ROW TAKES EXACTLY ONE KIND, AND A POOL-PRIZE ROW TAKES (b): the loop asserts it asserted (`checked == len(VERB_TABLE)`).
    FALSIFIER: a row with none of the three loads (the plant in `test_a_row_naming_none_is_refused_at_load`).
  * A BRUTE ROW NEVER ROLLS: planted with `governing:` or a `difficulty:` cell it is refused, naming the
    verb; and the realm's own brute acts, folded twice from one state, are one outcome with no `roll:` stream minted and
    `pool.faculty` and `pool.score` patched to raise. CONTROL: a rolled act under the same counter DOES mint a `roll:` stream.
  * THE MEAN: `governing_mean([2, 3]) == 2.5` (a whole-number rounding, 3, or half-to-even, 2, fails), `[2, 2, 3] -> 2.3`,
    `[2, 3, 3] -> 2.7`, `[5] -> 5.0`, over every input the rule admits, against an exact `Fraction` reference.
  * THE POOL IS FRACTIONAL AND REACHES THE DICE UNROUNDED: `faculty == 2.5` and the `SocialContestInput` carries `2.5`.
  * AN UNHELD ATTRIBUTE READS `pool_default`; A FIRST RANK ADDS A DIE.
"""
from __future__ import annotations

import copy
import dataclasses
from fractions import Fraction
from itertools import product
from math import floor
from types import SimpleNamespace

import pytest

from engine.dice_engine import sigma_leverage as SL
from engine.substrate import descriptors

from ..data import verbs as VERBS
from ..data.rosters import GRADED_TASKS, roster_map
from ..data.verbs import BRUTE_KINDS, VERB_TABLE
from ..gaps import Unspecified
from ..harness import probes as P
from ..loop import resolve as RESOLVE
from ..loop.driver import SeasonDriver, mint_token
from ..data.matrix import Step, WriteClass
from ..seam.wrappers import pool, sigma
from ..state.carriers import Act, Record
from .test_g3_not_yours import _gov_world

PRIZES = roster_map("contest_subsystems", "prizes")
ACUITY, PERCEPTION, FOCUS = "attr.mind.acuity", "attr.mind.perception", "attr.mind.focus"


def _exempt(row, prizes=PRIZES) -> bool:
    return bool(row.contests) and (prizes.get(row.contests) or {}).get("person_inputs") == "own"


def _kinds_of(row, prizes=PRIZES) -> list:
    """(a) brute, (b) governing, (c) an exempt prize, (d) proceeds (B24p.16: a verb that opens a proceeding)."""
    return [k for k, held in (("a", bool(row.brute)), ("b", bool(row.governing)), ("c", _exempt(row, prizes)), ("d", bool(row.proceeds))) if held]


def _check(rows=None, prizes=None):
    return VERBS._check_governing_attributes(
        dict(VERB_TABLE) if rows is None else rows,
        PRIZES if prizes is None else prizes)


def test_every_verb_row_names_its_attributes_or_its_authority_or_its_subsystem():
    checked = 0
    for verb, row in VERB_TABLE.items():
        kinds = _kinds_of(row)
        assert len(kinds) == 1, (verb, kinds)                                  # exactly one of (a), (b), (c), (d) (B24p.19: the five rows' `governing` is gone)
        if row.contests and PRIZES[row.contests].get("person_inputs") == "pool" and not row.proceeds:
            assert row.governing and not row.brute, verb                       # a pool-prize row takes (b), or (d) where it proceeds
            assert row.opposed_attribute in descriptors.ATTRIBUTES, verb       # and names who resists it
        if row.proceeds:
            assert not row.governing and row.opposed_attribute is None, verb   # a verb that proceeds pools nothing and names no resisting trait
        if row.brute:
            assert row.brute in BRUTE_KINDS and row.brute_note.strip(), verb
        if row.governing:
            assert 1 <= len(row.governing) <= 3 and len(set(row.governing)) == len(row.governing), verb
            assert set(row.governing) <= set(descriptors.ATTRIBUTES), verb
        checked += 1
    assert checked == len(VERB_TABLE) == 67, checked
    kinds = [k for r in VERB_TABLE.values() for k in _kinds_of(r)]
    assert (kinds.count("a"), kinds.count("b"), kinds.count("c"), kinds.count("d")) == (27, 30, 4, 6), kinds   # B24.08: `determine` moved from (b) to (d). The five that proceed pool nothing; B21.09 moved `establish` from (a) to (b) (it is drawn), B21.14 `confer`, `revoke`, `succeed`, B21.56 `issue`
    assert _check() is None                                                    # the shipped table passes the loader's own check


def test_a_brute_row_carrying_governing_or_a_difficulty_is_refused():
    give = VERB_TABLE["give"]
    assert give.brute == "own"
    _check()                                                                   # CONTROL: the unplanted table loads
    planted = {**VERB_TABLE, "give": dataclasses.replace(give, governing=(ACUITY,))}
    with pytest.raises(Unspecified, match="give"):
        _check(planted)
    with pytest.raises(Unspecified, match="give"):                             # a `difficulty:` cell (D-U1-04's column)
        _check({**VERB_TABLE, "give": dataclasses.replace(give, difficulty="routine")})
    with pytest.raises(Unspecified, match="give"):                             # a `contests:` prize
        _check({**VERB_TABLE, "give": dataclasses.replace(give, contests="a standing")})
    graded = {**GRADED_TASKS}
    assert "give" not in graded
    with pytest.raises(Unspecified, match="covenant"):                         # a `brute:` row carrying `opposed_attribute` (B21.56: was `issue`, now drawn)
        _check({**VERB_TABLE, "covenant": dataclasses.replace(VERB_TABLE["covenant"], opposed_attribute=ACUITY)})


def test_a_brute_verb_twice_on_one_state_is_one_outcome_and_no_draw(monkeypatch):
    """`convene` (B21.14: `confer` until it was drawn), `utter`, `transfer` and `dispatch`, hand-built, each resolved on two deep copies of one built world: the
    Event lists and `content_hash()` are equal, and no `roll:` stream is minted (the counter wraps `draw_factory`'s returned `draw`,
    the one stream every roll at `loop/resolve.py`'s two `"roll:..."` sites comes from) with `faculty` and `score` patched to raise.
    `engine/season/state/draw.py` does not exist; B06's keyed draw owner (`engine/dice_engine/draw.py`) re-points this counter."""
    real = RESOLVE.draw_factory
    purposes: list = []

    def counting(seed, tick_of):
        draw = real(seed, tick_of)

        def counted(actor, purpose):
            purposes.append(purpose)
            return draw(actor, purpose)
        return counted

    def boom(*a, **k):
        raise AssertionError("a brute act reached the pool reader")

    monkeypatch.setattr(RESOLVE, "draw_factory", counting)

    def twin(world_pair, act):
        a, b = copy.deepcopy(world_pair), copy.deepcopy(world_pair)
        runs = []
        for w, d in (a, b):
            ev = d.resolve(mint_token(w, WriteClass.ACTS), [copy.deepcopy(act)],
                           contest_max_depth=w.fixtures.get("contest_max_depth"))
            runs.append((ev, w.content_hash()))
        return runs

    gov = _gov_world()
    low_w = P.tiny_world()
    low = (low_w, SeasonDriver(low_w))
    cases = (
        # B21.14: `confer` is drawn (`contests: a seat`), so the seat-authorised brute case is `convene`
        (gov, Act(id="b_convene", actor="p_high", verb="convene", payload={"subject": "S"}, via="off_duke")),
        (low, Act(id="b_utter", actor="p_low", verb="utter")),
        (low, Act(id="b_transfer", actor="p_low", verb="transfer", payload={"from": "S", "to": "Hh", "kind": "grain", "amount": 3})),
        (gov, Act(id="b_dispatch", actor="p_high", verb="dispatch", via="off_duke", payload={"subject": "p_mid"})),
    )
    checked = 0
    for pair, act in cases:
        assert VERB_TABLE[act.verb].brute, act.verb
        monkeypatch.setattr(pool, "faculty", boom)
        monkeypatch.setattr(pool, "score", boom)
        monkeypatch.setattr(sigma, "faculty", boom)
        monkeypatch.setattr(sigma, "score", boom)
        purposes.clear()
        first, second = twin(pair, act)
        assert first[0] == second[0] and first[1] == second[1], act.verb       # one outcome from one state
        assert first[0], act.verb                                               # and it is an outcome, an Event at least
        assert not [p for p in purposes if str(p).startswith("roll:")], (act.verb, purposes)
        checked += 1
    assert checked >= 3, checked


def test_a_rolled_act_does_mint_a_roll_stream_under_the_same_counter(monkeypatch):
    """CONTROL for the brute-act test: the instrument sees a roll when there is one (an `examine` is a graded inquiry)."""
    real = RESOLVE.draw_factory
    purposes: list = []

    def counting(seed, tick_of):
        draw = real(seed, tick_of)
        return lambda actor, purpose: (purposes.append(purpose), draw(actor, purpose))[1]

    monkeypatch.setattr(RESOLVE, "draw_factory", counting)
    w = P.tiny_world()
    w.records["rec_b25"] = Record("rec_b25", "Hh", "text")
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    d.resolve(mint_token(w, WriteClass.ACTS), [Act(id="c_research", actor="p_low", verb="research", payload={"subject": "rec_b25"})],
              contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert any(str(p).startswith("roll:") for p in purposes), purposes


def test_a_row_naming_none_is_refused_at_load():
    for verb in ("give", "examine", "issue", "tell"):                      # one row of each kind (a), (b), (b with an opposition), (d)
        row = VERB_TABLE[verb]
        bare = dataclasses.replace(row, brute=None, brute_note="", governing=(), opposed_attribute=None, proceeds=())
        with pytest.raises(Unspecified, match=verb):
            _check({**VERB_TABLE, verb: bare})
    with pytest.raises(Unspecified, match="examine"):                           # more than one of (a), (b), (c)
        _check({**VERB_TABLE, "examine": dataclasses.replace(VERB_TABLE["examine"], brute="own", brute_note="x")})
    for bad in ((ACUITY, FOCUS, PERCEPTION, "attr.body.strength"), (ACUITY, ACUITY), ("attr.mind.nonesuch",)):
        with pytest.raises(Unspecified, match="issue"):                         # four attributes, a repeat, a key outside the ten
            _check({**VERB_TABLE, "issue": dataclasses.replace(VERB_TABLE["issue"], governing=bad)})
    with pytest.raises(Unspecified, match="issue"):                             # contested against a person with no opposed attribute
        _check({**VERB_TABLE, "issue": dataclasses.replace(VERB_TABLE["issue"], opposed_attribute=None)})
    with pytest.raises(Unspecified, match="covenant"):                          # `seat` where there is no `remit:` and no Office (B21.56: was `issue`)
        _check({**VERB_TABLE, "covenant": dataclasses.replace(VERB_TABLE["covenant"], eligibility=("own",), referent_class="")})
    with pytest.raises(Unspecified, match="a standing"):                        # a prize row with no `person_inputs`, or another value
        _check(prizes={**PRIZES, "a standing": {k: v for k, v in PRIZES["a standing"].items() if k != "person_inputs"}})
    with pytest.raises(Unspecified, match="a standing"):
        _check(prizes={**PRIZES, "a standing": {**PRIZES["a standing"], "person_inputs": "both"}})


def test_a_verb_is_exempt_only_by_its_prize():
    fight = VERB_TABLE["fight"]
    assert fight.contests == "the body" and not fight.governing and not fight.brute
    assert _kinds_of(fight) == ["c"]
    planted = {**PRIZES, "the body": {**PRIZES["the body"], "person_inputs": "pool"}}
    assert _kinds_of(fight, planted) == []                                      # names nothing, and no longer exempt
    with pytest.raises(Unspecified, match="fight"):
        _check(prizes=planted)
    with pytest.raises(Unspecified, match="arrest"):                            # a pool-prize row cannot be exempt either
        _check(prizes={**PRIZES, "a standing": {**PRIZES["a standing"], "person_inputs": "own"}})


def test_the_governing_score_is_the_mean_rounded_to_the_tenth():
    """A true half-tenth never occurs for integer scores with `n` of 1 to 3 (n=2 gives .0 or .5, n=3 gives .0, .3 or .7), so the
    rule's half-up clause is vacuous at this input; the reference is exact all the same."""
    assert SL.governing_mean([2, 3]) == 2.5 and isinstance(SL.governing_mean([2, 3]), float)
    assert SL.governing_mean([2, 2, 3]) == 2.3 and SL.governing_mean([2, 3, 3]) == 2.7 and SL.governing_mean([5]) == 5.0
    checked = 0
    for n in (1, 2, 3):
        for scores in product(range(1, 8), repeat=n):
            want = floor(Fraction(sum(scores), n) * 10 + Fraction(1, 2)) / 10
            got = SL.governing_mean(list(scores))
            assert got == want and isinstance(got, float), (scores, got, want)
            checked += 1
    assert checked == 7 + 7 ** 2 + 7 ** 3, checked
    for bad in ([], [1, 2, 3, 4], [-1], [3, -2]):
        with pytest.raises(ValueError):
            SL.governing_mean(bad)


def _person(w, **attrs):
    p = w.persons["p_low"]
    p.attributes = dict(attrs)
    p.capability = {}
    return p


def test_a_fractional_governing_score_reaches_the_dice_unrounded():
    w = P.tiny_world()
    verb = "examine"
    assert VERB_TABLE[verb].governing == (PERCEPTION, ACUITY)
    p = _person(w, **{PERCEPTION: 2, ACUITY: 3})
    assert pool.governing_score(w, p, verb) == 2.5
    # B05.99 re-pin (B05.23 ships the calibrated base and floor, pool_add 6, pool_floor 5): the shipped pool is 2.5 + 6
    assert (w.fixtures.get("pool_add"), w.fixtures.get("pool_floor")) == (6, 5)
    assert pool.faculty(w, p, verb) == 8.5
    inp = sigma.contest_input(w, [p.id], verb=verb, subject="site_harbour")
    assert inp.pool == 8.5 and isinstance(inp.pool, float)
    w.fixtures = w.fixtures.sweep("pool_add", 0).sweep("pool_floor", 0)          # the control arm: the governing score itself
    assert pool.faculty(w, p, verb) == 2.5
    inp = sigma.contest_input(w, [p.id], verb=verb, subject="site_harbour")
    assert inp.pool == 2.5 and isinstance(inp.pool, float)


def test_an_unheld_attribute_counts_at_the_untrained_score():
    w = P.tiny_world()
    default = w.fixtures.get("pool_default")
    verb = "examine"
    p = _person(w, **{ACUITY: 6})                                               # holds one of the row's two attributes
    assert pool.governing_score(w, p, verb) == SL.governing_mean([default, 6])
    p = _person(w)                                                              # holds none: the control, his pool is the default
    assert pool.governing_score(w, p, verb) == SL.governing_mean([default, default]) == float(default)
    # B05.99 re-pin (B05.23: pool_add 6 ships): the untrained man's pool is the default plus the base; at control, the default
    assert pool.faculty(w, p, verb) == default + w.fixtures.get("pool_add") == 8
    w.fixtures = w.fixtures.sweep("pool_add", 0).sweep("pool_floor", 0)
    assert pool.faculty(w, p, verb) == default


def test_a_first_rank_adds_a_die():
    w = P.tiny_world()
    verb = "examine"
    p = _person(w, **{PERCEPTION: 3, ACUITY: 4})
    before = pool.faculty(w, p, verb)
    assert pool.rank(p, verb) == 0
    p.capability = {VERBS.VERB_CAPABILITY[verb]: 1}
    assert pool.rank(p, verb) == 1
    assert pool.faculty(w, p, verb) == before + 1                                # a first rank adds one die, at pool_add 0, pool_floor 0
    p.capability = {VERBS.VERB_CAPABILITY[verb]: 3}
    assert pool.faculty(w, p, verb) == before + 3
    assert pool.rank(p, "move") == 0                                             # a verb naming no skill adds none
