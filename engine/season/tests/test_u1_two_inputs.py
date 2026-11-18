"""B05.09 -- THE SKILL SCORE HAS NO ATTRIBUTE IN IT; THE POOL IS `pool_of`; A FIRST RANK IS NEVER A LOSS
(TWO Edit A, CAP B1, CORE Edit 9, U1 §11 U1-B step 1).

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * A FIRST RANK NEVER LOWERS A POOL (CORE Edit 9's gate): a person holding no `argue` key trains it, `capability.raised`
    is emitted, his `argue` pool is not lower than before, and a second training raises the rank. FALSIFIER: his pool after the
    first rank below `pool_default` (the `{key: 1}` replacing the default is exactly the loss the old never-minted rule
    existed to prevent); the planted failure here is `pool.score` as lane A shipped it, or a score that is the bare rank.
  * `faculty` IS `pool_of(score, addends, pool_add, pool_floor)` (A-6, D-U1-08): with `pool_add` and `pool_floor` set, the
    pool is the one rule's answer, and the `score` it hands over carries no attribute and no addend.
  * UNTRAINED `none`: a non-holder of a row saying `untrained: none` has NO score, `faculty` answers 0 (a roll refused as a
    held 0 was) and `raised_capability` mints his first rank.
  * COMBAT KEEPS `score + addends` (MAP §G edit 4): `combat_input`'s `faculties` is not `faculty`, so `pool_add` and
    `pool_floor` do not reach the fight twice.
"""
from __future__ import annotations

import dataclasses
from types import MappingProxyType

import pytest

from engine.dice_engine.sigma_leverage import pool_of
from engine.substrate import descriptors

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.verbs import VERB_CAPABILITY
from ..harness import probes as P
from ..loop import effects_combat as EC
from ..loop.driver import SeasonDriver
from ..seam.wrappers import combat, pool
from ..state.carriers import Act
from .test_in12_step9 import CARIN, _kinds, _npc088, _resolve

VERB = "argue"            # draws on the `argue` skill key (`VERB_CAPABILITY`); asserted below
KEY = "argue"


def _addends(w, p, verb):
    return sum(int(add(w, p, verb)) for add in pool.POOL_ADDENDS)


def _world(**fixtures):
    fx = DEFAULT_FIXTURES
    for name, value in fixtures.items():
        fx = fx.sweep(name, value)
    return P.tiny_world(fx)


def test_the_verb_draws_on_the_key_these_tests_assume():
    assert VERB_CAPABILITY[VERB] == KEY


def test_a_first_rank_never_lowers_a_pool():
    """CORE Edit 9's gate, driven through the real `train` effect: a person with no `argue` key trains it."""
    w, d = _npc088()
    pupil = next(pid for pid, p in sorted(w.persons.items()) if pid != CARIN and not p.capability)
    p = w.persons[pupil]
    p.attributes = {}                       # the subject is the skill: no sheet to lift the pool
    default = w.fixtures.get("pool_default")
    before = pool.faculty(w, p, VERB)
    assert KEY not in p.capability and before >= default
    first = _kinds(_resolve(w, d, Act(id="tr_first", actor=CARIN, verb="train", payload={"subject": pupil, "kind": KEY})))
    assert first == ["capability.raised"], first                        # (1) the first rank is minted, not refused
    assert p.capability == {KEY: 1}
    assert pool.faculty(w, p, VERB) >= before and pool.score(w, p, VERB) == default      # (2) the pool is not lower
    second = _kinds(_resolve(w, d, Act(id="tr_second", actor=CARIN, verb="train", payload={"subject": pupil, "kind": KEY})))
    assert second == ["capability.raised"] and p.capability == {KEY: 2}      # (3) a second training raises the rank
    assert pool.faculty(w, p, VERB) == before                           # the pool holds at the default until the rank passes it
    for n in range(3):                                                  # CONTROL: the rank passing the default DOES raise the pool
        _resolve(w, d, Act(id=f"tr_more{n}", actor=CARIN, verb="train", payload={"subject": pupil, "kind": KEY}))
    assert p.capability[KEY] == 5 and pool.faculty(w, p, VERB) == before + (5 - default)


def test_the_score_is_the_larger_of_the_rank_and_the_untrained_score_and_reads_no_attribute():
    w = _world()
    p = w.persons["p_low"]
    default = w.fixtures.get("pool_default")
    p.attributes = {descriptors.capability(KEY).base: 7}                # the governing attribute, held at the ceiling
    p.capability = {}
    assert pool.score(w, p, VERB) == default                            # a non-holder: the untrained score, whatever he is
    p.capability = {KEY: 1}
    assert pool.score(w, p, VERB) == default                            # a first rank is never a loss
    p.capability = {KEY: default + 3}
    assert pool.score(w, p, VERB) == default + 3                        # a holder: the rank
    p.attributes = {}
    assert pool.score(w, p, VERB) == default + 3                        # the same with no attribute held


def test_the_opposition_reads_the_skill_score_not_the_pool(monkeypatch):
    """B05.11 (U1-B step 4; CAP B4): a subject with practice addends, a seat and a resisting attribute at the ceiling opposes
    at his skill SCORE: `opposition == his rank`, no base dice, no practice addend, no seat, no attribute -- while his own pool
    (`faculty`) carries the addend. FALSIFIER: `_opposition_of` returning `faculty` (the pool) or the larger of the attribute and
    the rank (lane A's `max`, which reads 7 here). CONTROL: the roller's pool reads the same addend, so the addend is live."""
    from ..data.verbs import VERB_CAPABILITY, VERB_TABLE
    from ..seam.wrappers import sigma
    verb = "tell"
    key = VERB_CAPABILITY[verb]
    w = _world()
    SeasonDriver(w)
    subject = w.persons["p_high"]                                       # holds `off_duke`, a seat
    assert any(t.kind == "hold" for t in subject.tenures), "the subject holds a seat"
    subject.capability = {key: 5}
    subject.attributes = {VERB_TABLE[verb].opposed_attribute: descriptors.ATTRIBUTE_CEILING}
    monkeypatch.setattr(pool, "POOL_ADDENDS", list(pool.POOL_ADDENDS))
    pool.register_pool_addend(lambda w_, who, v: 3 if who.id == subject.id else 0)
    assert pool.faculty(w, subject, verb) > pool.score(w, subject, verb) == 5      # the addend is in his pool, not his score
    assert sigma._opposition_of(w, subject.id, verb) == 5.0                        # his opposition is his rank
    assert sigma.contest_input(w, ["p_low", subject.id], verb=verb, subject=subject.id).opposition == 5.0
    subject.capability = {}
    assert sigma._opposition_of(w, subject.id, verb) == float(w.fixtures.get("pool_default"))   # no rank: the untrained score


def test_the_pool_is_pool_of_with_the_base_and_the_floor():
    """`faculty == pool_of(score, addends, pool_add, pool_floor)`: both fixtures reach the pool, and at control (0, 0) it is
    `score + addends` (the control the entry names)."""
    w = _world()
    p = w.persons["p_low"]
    p.capability = {KEY: 3}
    base = pool.score(w, p, VERB)
    add = _addends(w, p, VERB)
    assert pool.faculty(w, p, VERB) == base + add                        # control: pool_add 0, pool_floor 0
    for pa, pf in ((0, 5), (3, 0), (6, 5), (6, 0)):
        w2 = _world(pool_add=pa, pool_floor=pf)
        p2 = w2.persons["p_low"]
        p2.capability = {KEY: 3}
        assert pool.faculty(w2, p2, VERB) == pool_of(pool.score(w2, p2, VERB), _addends(w2, p2, VERB), pa, pf)
    w3 = _world(pool_add=0, pool_floor=5)
    p3 = w3.persons["p_low"]
    p3.capability = {KEY: 1}
    assert pool.faculty(w3, p3, VERB) == max(5, 2 + _addends(w3, p3, VERB))      # the floor lifts a small pool


def test_the_governing_attribute_is_the_held_one_else_none():
    w = _world()
    p = w.persons["p_low"]
    attr = descriptors.capability(KEY).base
    p.attributes = {attr: 6}
    assert pool.governing_attribute(p, VERB) == 6
    p.attributes = {}
    assert pool.governing_attribute(p, VERB) is None
    assert pool.governing_attribute(p, "lie") is None                   # a verb drawing on no skill names no attribute


def _untrained_none(monkeypatch, key):
    row = dataclasses.replace(descriptors.CAPABILITIES[key], untrained="none")
    monkeypatch.setattr(descriptors, "CAPABILITIES", MappingProxyType({**descriptors.CAPABILITIES, key: row}))


def test_untrained_none_gives_a_non_holder_no_score_and_a_refused_pool(monkeypatch):
    """The branch no shipped row reaches (B04.02's rows all say `default`): planted here, with the default row as its control."""
    w = _world(pool_floor=3)
    p = w.persons["p_low"]
    p.attributes = {}
    p.capability = {}
    assert pool.score(w, p, VERB) == w.fixtures.get("pool_default") and pool.faculty(w, p, VERB) >= 3      # control
    _untrained_none(monkeypatch, KEY)
    assert pool.score(w, p, VERB) is None
    assert pool.faculty(w, p, VERB) == 0                                # refused as a held 0 was: no floor lifts a refusal
    p.capability = {KEY: 1}
    assert pool.score(w, p, VERB) == w.fixtures.get("pool_default")     # the holder is scored (CORE Edit 9)
    p.capability = {}
    assert EC.raised_capability(p, KEY) == {KEY: 1}                     # and a non-holder of such a row is minted a first rank


def test_raised_capability_mints_a_first_rank_and_holds_the_ceiling():
    w = _world()
    p = w.persons["p_low"]
    p.capability = {"inquiry": 2}
    assert EC.raised_capability(p, KEY) == {"inquiry": 2, KEY: 1}       # a non-holder's first rank is 1
    ceiling = descriptors.capability(KEY).ceiling
    p.capability = {KEY: ceiling}
    assert EC.raised_capability(p, KEY) is None                         # the rank never passes the ceiling
    p.capability = {KEY: ceiling - 1}
    assert EC.raised_capability(p, KEY) == {KEY: ceiling}


def test_combat_receives_score_plus_addends_not_faculty():
    """MAP §G edit 4: with the base and the floor live, `faculty` applies them and the fight's `faculties` does not."""
    w = _world(pool_add=6, pool_floor=5)
    a, b = "p_low", "p_mid"
    for pid in (a, b):
        w.persons[pid].capability = {"arms": 3}
    inp = combat.combat_input(w, [a, b], "fight")
    for pid, got in zip((a, b), inp.faculties):
        p = w.persons[pid]
        assert got == pool.score(w, p, "fight") + _addends(w, p, "fight") == 3 + _addends(w, p, "fight")
        assert pool.faculty(w, p, "fight") >= 5 and pool.faculty(w, p, "fight") != got


# ---------------------------------------------------------------------------------------------------------------------
# B05.10 -- THE GOVERNING ATTRIBUTE IS DICE; THE OPPONENT'S ATTRIBUTE IS THE OPPOSITION; NEITHER IS A LEVEL.
# (CAP B3 and gate (3), as reconciled 2026-11-13 at B05.25: the roller's attributes are in his dice, averaged, so no `side: actor`
# `edge` row ships; the opponent's attribute is the verb row's `opposed_attribute:` and enters the opposition, never as levels.)
# FALSIFIER: a `side: actor` or `side: subject` `edge` row on `verb.base` shipped in `tables.capability_uses`, or a reader that
# turns an attribute into levels with none: `leverage` would then differ from 0.0 here with `attribute_level` at `minor`.
# ---------------------------------------------------------------------------------------------------------------------

def _argued(w, actor, subject):
    """The record the social roll deals for `actor` arguing at `subject`, and its obstacle's named terms."""
    from ..seam.wrappers import sigma
    inp = sigma.contest_input(w, [actor, subject], verb="tell", subject=subject)
    return inp, dict(sigma._composed_terms(inp))


def test_the_opponent_attribute_raises_the_opposition():
    """Two rollers differing only in a `governing` attribute read different pools and the same leverage (no level); two opponents
    differing only in the verb's `opposed_attribute` read different oppositions and the same pool. `attribute_level` is `minor`
    (live) in the test's fixtures: it changes nothing, since no row reads it at the social roll."""
    from ..data.verbs import VERB_TABLE
    from ..seam.wrappers import sigma
    verb = "tell"
    row = VERB_TABLE[verb]
    governing, opposed = row.governing[0], row.opposed_attribute
    assert governing and opposed and governing != opposed
    w = _world(attribute_level="minor")
    SeasonDriver(w)                                                          # the registrar fills the module entries
    lo, hi, other = w.persons["p_low"], w.persons["p_high"], w.persons["p_other"]
    for p in (lo, hi, other, w.persons["p_mid"]):
        p.capability, p.attributes = {}, {}
    lo.attributes, hi.attributes = {governing: 2}, {governing: 6}
    pools = [pool.faculty(w, p, verb) for p in (lo, hi)]
    assert pools[0] < pools[1], pools                                        # the governing attribute gives dice
    leverage = [sigma.contest_input(w, [p.id, "p_mid"], verb=verb, subject="p_mid").leverage for p in (lo, hi)]
    assert leverage == [0.0, 0.0], leverage                                  # and gives no level, with `attribute_level` live
    w.persons["p_mid"].attributes, other.attributes = {opposed: 3}, {opposed: 6}
    (a, ta), (b, tb) = _argued(w, "p_low", "p_mid"), _argued(w, "p_low", "p_other")
    assert a.pool == b.pool and a.leverage == b.leverage == 0.0              # the roller is unchanged
    assert b.opposition > a.opposition and tb["opposition"] > ta["opposition"]     # the opponent's attribute is harder to move
    default = w.fixtures.get("pool_default")
    assert a.opposition == 3 + default and b.opposition == 6 + default       # B05.14 (A-137): one point of the attribute, one point of the opposition, ON TOP of the skill score
    assert tb["opposition"] - ta["opposition"] == 0.5 * (6 - 3)              # and `opposition_rate` of each at the control
    # CONTROL: an opponent holding no `opposed_attribute` at all reads it at the mid-point (B05.16), above the held 3.
    w.persons["p_other"].attributes = {}
    mid = (descriptors.ATTRIBUTE_FLOOR + descriptors.ATTRIBUTE_CEILING) / 2
    assert _argued(w, "p_low", "p_other")[0].opposition == default + mid > a.opposition


def test_an_unauthored_person_reads_zero_attribute_levels():
    """B05.16 (CAP B9, U1 §4 "Unauthored attribute", §6; U1-B step 7): a person who holds NO value on an attribute (a hand-built world's
    person, `tiny_world`, no generic cast) reads the scale's MID-POINT `(ATTRIBUTE_FLOOR + ATTRIBUTE_CEILING) / 2` in the OPPOSITION,
    where the averaged dice side counts him at the untrained score. `governing_attribute` returns `None` for the key he does not hold
    (never a default), the opposition reads that `None` as the mid-point, and he is neither above nor below it: zero levels either
    way. FALSIFIER (CAP): an authored character is easier to oppose than an unauthored one: the unheld opponent reads `mid`, so a
    person authored BELOW the mid-point is the easier to move and one authored above is the harder, the unheld one reading
    exactly the person authored AT the mid-point. CONTROL: the held reads are what they were (`test_the_opponent_attribute_raises_the_opposition`)."""
    from ..data.verbs import VERB_TABLE
    from ..seam.wrappers import sigma
    verb = "tell"
    row = VERB_TABLE[verb]
    opposed, governing = row.opposed_attribute, row.governing[0]
    mid = (descriptors.ATTRIBUTE_FLOOR + descriptors.ATTRIBUTE_CEILING) / 2
    w = _world(attribute_level="minor")
    SeasonDriver(w)
    default = w.fixtures.get("pool_default")
    assert mid != default                                                    # the two readings differ here, so the test can tell them apart
    p, other = w.persons["p_other"], w.persons["p_mid"]
    p.capability, p.attributes = {}, {}
    assert pool.governing_attribute(p, verb) is None                         # no value held: None, not a default
    assert pool.opposing_attribute(w.fixtures, p, verb) == mid               # the opposition reads that None as the mid-point
    assert pool.opposing_attribute(w.fixtures, p, "forge") is None          # a row naming no `opposed_attribute` has none, held or not
    read = {}
    for label, held in (("below", mid - 1), ("at", mid), ("above", mid + 1), ("unheld", None)):
        p.attributes = {} if held is None else {opposed: held}
        read[label] = sigma.contest_input(w, [other.id], verb=verb, subject=p.id).opposition
    assert read["unheld"] == default + mid, read                             # his skill score plus the mid-point
    assert read["unheld"] == read["at"], read                                # unauthored IS the mid-point
    assert read["below"] < read["unheld"] < read["above"], read              # an authored character is easier or harder, not the unheld one
    p.attributes = {}
    other.attributes = {}
    assert sigma.contest_input(w, [p.id, other.id], verb=verb, subject=other.id).leverage == 0.0     # zero levels, `attribute_level` live
    other.attributes = {governing: descriptors.ATTRIBUTE_CEILING}
    assert sigma.contest_input(w, [p.id, other.id], verb=verb, subject=other.id).leverage == 0.0     # and an authored value gives none either
    p.attributes = {governing: 1}                                            # CONTROL: the dice side still counts an unheld attribute at the untrained score
    q = w.persons["p_low"]
    q.capability, q.attributes = {}, {}
    assert pool.governing_score(w, q, verb) == float(default) and mid != default


def _rebind_rows(monkeypatch, edit):
    """`capability_uses()` returns the shipped rows after `edit(rows)`, loaded by the real loader (no code edit)."""
    import copy
    from ..data import rosters
    rows = copy.deepcopy(list(rosters._TABLES["capability_uses"]["rows"]))
    edit(rows)
    monkeypatch.setattr(rosters, "_CAPABILITY_USES", rosters._load_capability_uses(rows, dict(DEFAULT_FIXTURES._v)))


def test_the_shipped_dice_row_names_the_pool_pair():
    from ..data import rosters
    dice = [r for r in rosters.capability_rows("social_roll") if r.role == "dice"]
    assert len(dice) == 1 and (dice[0].add, dice[0].floor) == ("pool_add", "pool_floor"), dice
    assert not [r for r in rosters.capability_rows("social_roll") if r.role == "edge"]      # no `edge` row ships (reconciled, B05.25)


def test_faculty_reads_its_pool_pair_from_the_social_roll_dice_row(monkeypatch):
    """MAP §G edit 4: `faculty` takes the fixture NAMES from the `social_roll` `dice` row. The shipped row names `pool_add` and
    `pool_floor`; swapping the two names in the row, with no code edit, swaps what the pool reads; a row naming neither reads 0
    and 0 whatever the fixtures hold (the control: at 0 and 0 the pool is `governing score + rank + addends`)."""
    w = _world(pool_add=3, pool_floor=0)
    p = w.persons["p_low"]
    p.attributes, p.capability = {}, {}
    plain = pool.governing_score(w, p, "tell") + pool.rank(p, "tell") + _addends(w, p, "tell")
    assert pool.faculty(w, p, "tell") == plain + 3                              # shipped: `add: pool_add`

    def swap(rows):
        i = next(i for i, r in enumerate(rows) if r["use"] == "social_roll" and r["role"] == "dice")
        rows[i] = dict(rows[i], add="pool_floor", floor="pool_add")
    _rebind_rows(monkeypatch, swap)
    assert pool.faculty(w, p, "tell") == max(3, plain)                          # swapped: the floor reads `pool_add`, the base reads `pool_floor` (0)
    assert pool.faculty(w, p, "tell") != plain + 3

    def bare(rows):
        i = next(i for i, r in enumerate(rows) if r["use"] == "social_roll" and r["role"] == "dice")
        rows[i] = {k: v for k, v in rows[i].items() if k not in ("add", "floor")}
    _rebind_rows(monkeypatch, bare)
    assert pool.faculty(w, p, "tell") == plain                                  # no names: 0 and 0, whatever the fixtures hold
