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


def test_the_opposition_keeps_the_attribute_read_through_the_parameter():
    """`score(..., attribute=)` is B01's parameter, kept until B05.11: the opposition's read only; the pool passes none."""
    w = _world()
    p = w.persons["p_low"]
    p.capability = {KEY: 3}
    seven = lambda person, verb: 7
    assert pool.score(w, p, VERB, attribute=seven) == 7                 # the larger of the attribute and the rank
    assert pool.score(w, p, VERB, attribute=lambda person, verb: 1) == 3
    assert pool.score(w, p, VERB, attribute=lambda person, verb: None) == 3
    assert pool.score(w, p, VERB) == 3                                  # the pool passes none


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
