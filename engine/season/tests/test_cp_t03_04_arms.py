"""v11 CP-T03-04 -- TRAINING AND FIGHTING MAKE A PERSON BETTER AT IT: the `arms` vocation.

`rosters.yaml: verb_capability` maps `fight`, `accept` and `capture` (the rows contesting `the body`) to `arms`. So:
(ii) a held `arms` key reaches combat's pool and Ob through `seam/wrappers/sigma.py::faculty` -- CR-85's one path,
`combat_input` -> `PersonalCombatInput.faculties` -- and NO second skill input exists; (i) `arms` is a vocation
(`data/verbs.py::VOCATIONS`), so `train` forms on it and `_eff_train` raises it; (iii) the `cast:` overlay
(`harness/corpus_run.py::cast_overlay`, checked by `_check_capability` against the roster's values) is the authored
writer and names NO `arms` value (Jordan's content); (iv) `loop/effects_combat.py::_grown`: a fight that drew blood
raises `arms` by one on each SURVIVING party who ALREADY holds it; nothing is minted.
[ASSUMPTION; low; Jordan to correct; revert: rename the roster key] -- `arms` here is the trained skill, not
CP-T03-03's `arms_kinds` (equipment).

  FALSIFIER: a person holding `arms` 5 (the shipped roster, no test-local row) against a default party rolls pool 11
  against Ob 1.0, his opponent pool 8 against Ob 2.5 -- CR-85's planted faculty-5 reading, reproduced through the
  roster. A surviving holder of a bloodied fight gains one; a non-holder gains none and nothing is minted.
  MUTATION (executed below): `_grown` minting for a non-holder turns the never-mint check red.
  CONTROL: a FORMATION MOVER EVEN AT CONTROL -- `arms` in the vocation range adds one `train` Candidate per `train`
  formation, so with nobody holding the key every 1-season hash still moves (POST_ITEM). The control CANNOT
  reproduce the pre-item hash with the item in place; `revert_cp_t03_04` (the three roster rows and the vocation
  removed, in process) reproduces all three.
"""
from __future__ import annotations

import importlib
import random
from collections import Counter

import pytest

from engine.substrate import pc_engine

from ..data import rosters as R
from ..data import verbs as VERBS
from ..data.matrix import Step, WriteClass
from ..data.rosters import FELLED, UNTOUCHED, WOUNDED
from ..decision import options as OPT
from ..harness import probes as P
from ..harness.populated import build_realm, run
from ..loop import effects_combat as EC
from ..loop.driver import SeasonDriver, mint_token
from ..loop.effects_shared import EFFECTS
from ..seam import Resolution, degree_of
from ..seam.wrappers import combat as C
from ..state.carriers import Act
from ._fresh_process import entry_target
from ._scar_helpers import party_state

KEY = "arms"
BODY_VERBS = ("fight", "accept", "capture")

#: 1-season hashes BEFORE this item (22ea6e13), and AFTER it with nobody holding the key (formation only).
#: `build_realm(0).content_hash()` is 7266f56bea4e3d75705f5e88eec1b2e1 before and after.
#: Seeds 1 and 2 of both are the post-B10-11b reading (`reading @4b334f2a`), re-recorded by the batch pin commit: PC-20 (1)
#: (the head-weighted strike impact, `K_STR_HEAD`) moves a one-season run that reaches `strike_impact`; seed 0 calls none.
#: Was, before that pin commit: PRE_ITEM 6e25b047... / fe9032ed...; POST_ITEM 07634b99... / 1cc4370d....
#: B10-13 batch pin commit: PRE_ITEM was 20accb03... / 597fac34... / a157d34a... (= CR-85's POST_ITEM, re-recorded with it);
#: POST_ITEM was b2dde1fc... / c58b1a7e... / 5518f31c....
#: B10-12 pin commit (CR-24 `field_winner_casualties: engine` and MB-07r's support cap, both shipped, move a one-season
#: realm that fights; control: both reverted reads the old pins): seed 2 PRE_ITEM was 355872c5... (= CR-85's POST_ITEM),
#: POST_ITEM was 6078a950....
PRE_ITEM = {0: "a63b960024babdcd2a1a37839e2d6cb0",
            1: "0cd4f72e0cb1eba8ce55b78bfbc8201f",
            2: "b8c1873362190843ad00860275961a7e"}
POST_ITEM = {0: "8b5e882b0a4d771d56e8472ef557f84f",
             1: "e9aad997765ecb589711613cfb194444",
             2: "1139c7dcac2b0dd2b2ff6cbacc27e55c"}


def revert_cp_t03_04(monkeypatch):
    """The item OFF, in process: the three `verb_capability` rows deleted from the one shared dict (every reader --
    `faculty`, `practice`, `_grown`, the corpus check -- holds the same object) and `arms` taken out of `VOCATIONS` at
    each module that bound the frozenset. Other tests that pin a pre-item hash call it."""
    for verb in BODY_VERBS:
        monkeypatch.delitem(R.VERB_CAPABILITY, verb)
    off = frozenset(R.VERB_CAPABILITY.values())
    for mod in (R, VERBS, OPT, EC):
        monkeypatch.setattr(mod, "VOCATIONS", off)


@pytest.fixture
def _engine():
    if C.engine() is None:
        pytest.skip(f"personal_combat engine unavailable: {C.load_error()}")


# ---- (i) the roster ---------------------------------------------------------------------------------------------

def test_the_three_body_verbs_draw_on_arms_and_arms_is_a_vocation_with_an_attribute():
    assert {v: R.VERB_CAPABILITY.get(v) for v in BODY_VERBS} == {v: KEY for v in BODY_VERBS}
    assert KEY in VERBS.VOCATIONS and KEY in OPT.VOCATIONS and KEY in EC.VOCATIONS
    assert R.VOCATION_ATTRIBUTE[KEY] == "attr.body.agility"
    # the key is spelt in no body: `_grown` reads it off the roster by verb
    src = open(EC.__file__, encoding="utf-8").read()
    assert '"arms"' not in src and "'arms'" not in src


def test_nobody_holds_arms_at_landing_in_the_realm_the_overlay_or_a_lifepath():
    """The commit body's count: 0 persons hold `arms` (no overlay value, no lifepath template names it), and no
    practice record can form in it (`practice` counts Success-or-better; a fight's bands are none of the ladder's)."""
    from ..harness.corpus_run import cast_overlay
    held, seen = 0, 0
    for seed in (0, 1, 2):
        for p in build_realm(seed).persons.values():
            seen += 1
            held += KEY in (p.capability or {})
    assert seen >= 3 * 80 and held == 0
    overlay = [e for entries in cast_overlay().values() for e in entries]
    assert overlay, "setup: the overlay is empty"
    assert [e for e in overlay if KEY in (e.get("capability") or {})] == []
    assert [lp for lp, keys in R.LIFEPATH_TEMPLATES.items() if KEY in keys] == []
    assert all(R.DEGREE_STEP.get(b, 0) == 0 for b in (FELLED, WOUNDED, UNTOUCHED))


# ---- (ii) the one input path ------------------------------------------------------------------------------------

def _spy(monkeypatch) -> Counter:
    core = pc_engine.load()[0].core
    seen, real = Counter(), core.resolve

    def spy(pool, net_sigma, rng, ob):
        seen[(pool, ob)] += 1
        return real(pool, net_sigma, rng, ob)
    monkeypatch.setattr(core, "resolve", spy)
    return seen


@pytest.mark.parametrize("verb", ["fight", "accept"])
def test_falsifier_arms_5_rolls_pool_11_and_is_attacked_at_ob_2_5_through_the_seam(verb, monkeypatch, _engine):
    w = build_realm(1)
    a, b = sorted(w.persons)[:2]
    w.persons[a].capability = {**(w.persons[a].capability or {}), KEY: 5}
    assert KEY not in (w.persons[b].capability or {})
    inp = C.combat_input(w, [a, b], verb)
    assert inp.faculties == (5, 2), inp.faculties
    mod, attr = entry_target("the body")[1].split(":", 1)
    entry = getattr(importlib.import_module(mod), attr)
    seen = _spy(monkeypatch)
    checked = 0
    for s in range(6):
        entry(inp, random.Random(s))
        checked += 1
    assert set(seen) == {(11, 1.0), (8, 2.5)}, dict(seen)
    assert checked == 6


def test_control_with_nobody_holding_arms_every_season_roll_still_reads_pool_8_against_ob_1(monkeypatch, _engine):
    """The item moves formation, not a roll: seed 1's season fights all roll CR-85's (8, 1.0)."""
    seen = _spy(monkeypatch)
    w = build_realm(1)
    run(1, 1, w=w)
    assert seen and set(seen) == {(8, 1.0)}, dict(seen)


def test_control_with_the_item_off_the_same_holder_rolls_the_fallback(monkeypatch, _engine):
    revert_cp_t03_04(monkeypatch)
    w = build_realm(1)
    a, b = sorted(w.persons)[:2]
    w.persons[a].capability = {**(w.persons[a].capability or {}), KEY: 5}
    assert C.combat_input(w, [a, b], "fight").faculties == (2, 2)


# ---- (i) train ----------------------------------------------------------------------------------------------------

def test_train_raises_a_held_arms_and_mints_none():
    w = P.tiny_world()
    d = SeasonDriver(w)
    w.step, w.frozen = Step.RESOLVE, False
    holder, other = "p_low", "p_mid"
    w.persons[holder].capability = {KEY: 2}
    w.persons[other].capability = {}
    got = {}
    for pid in (holder, other):
        act = Act(id=f"tr_{pid}", actor=pid, verb="train", payload={"subject": pid, "kind": KEY})
        got[pid] = [e.kind for e in d._fold(w, mint_token(w, WriteClass.ACTS), act, None)]
    assert got == {holder: ["capability.raised"], other: ["train.refused"]}, got
    assert w.persons[holder].capability == {KEY: 3}
    assert KEY not in w.persons[other].capability


# ---- (iv) build-by-doing ------------------------------------------------------------------------------------------

ACTOR, SUBJECT = "p_low", "p_mid"
_BAND = {FELLED: dict(felled=True, wounds=2, left=0), WOUNDED: dict(wounds=1, left=5), UNTOUCHED: dict()}


def _fight(actor_band, subject_band, caps: dict, verb="fight"):
    """`ACTOR` fights `SUBJECT` through the real fold and gate (`test_cp_t03_00`'s harness), each party's
    `capability` set to `caps[pid]` first. Returns the world, the Events and each party's capability before."""
    w = P.tiny_world()
    for pid in (ACTOR, SUBJECT):
        w.persons[pid].capability = dict(caps.get(pid, {}))
    before = {pid: dict(w.persons[pid].capability) for pid in (ACTOR, SUBJECT)}
    d = SeasonDriver(w)
    w.step, w.frozen = Step.RESOLVE, False
    raw = {"wound_state": {SUBJECT: party_state(**_BAND[subject_band]), ACTOR: party_state(**_BAND[actor_band])}}
    res = Resolution(degree_of(raw, SUBJECT, w.fixtures), raw)
    act = Act(id="cp304", actor=ACTOR, verb=verb, payload={"subject": SUBJECT})
    return w, d._fold(w, mint_token(w, WriteClass.ACTS), act, res), before


def _raised(out) -> list:
    return sorted(c.subject for e in out if e.kind == "capability.raised" for c in e.changes)


def _never_minted(w, before) -> list:
    """THE NEVER-MINT CHECK: every party who held no `arms` before holds none after."""
    return [pid for pid in before if KEY not in before[pid] and pid in w.persons
            and KEY in (w.persons[pid].capability or {})]


def test_falsifier_a_surviving_holder_gains_one_and_a_non_holder_gains_none():
    w, out, before = _fight(WOUNDED, WOUNDED, {ACTOR: {KEY: 2}})
    assert w.persons[ACTOR].capability[KEY] == 3
    assert _never_minted(w, before) == [] and KEY not in w.persons[SUBJECT].capability
    assert _raised(out) == [ACTOR]
    assert "body.changed" in [e.kind for e in out]


def test_both_holders_grow_and_an_untouched_holder_beside_a_wounded_one_grows():
    w, out, _ = _fight(WOUNDED, WOUNDED, {ACTOR: {KEY: 2}, SUBJECT: {KEY: 4}})
    assert (w.persons[ACTOR].capability[KEY], w.persons[SUBJECT].capability[KEY]) == (3, 5)
    assert _raised(out) == sorted([ACTOR, SUBJECT])
    w, out, _ = _fight(UNTOUCHED, WOUNDED, {ACTOR: {KEY: 2}})
    assert w.persons[ACTOR].capability[KEY] == 3 and _raised(out) == [ACTOR]


def test_a_felled_holder_does_not_grow_and_his_surviving_holder_opponent_does():
    w, out, _ = _fight(FELLED, WOUNDED, {ACTOR: {KEY: 2}, SUBJECT: {KEY: 2}})
    assert ACTOR not in w.persons
    assert w.persons[SUBJECT].capability[KEY] == 3 and _raised(out) == [SUBJECT]


def test_an_untouched_fight_grows_nobody_and_still_reads_undecided():
    w, out, _ = _fight(UNTOUCHED, UNTOUCHED, {ACTOR: {KEY: 2}, SUBJECT: {KEY: 2}})
    assert [e.kind for e in out] == ["contest.undecided"]
    assert w.persons[ACTOR].capability[KEY] == w.persons[SUBJECT].capability[KEY] == 2


def test_control_non_holders_emit_no_capability_kind_and_no_body_subject_earns_it():
    w, out, before = _fight(WOUNDED, WOUNDED, {})
    assert _raised(out) == [] and "capability.raised" not in [e.kind for e in out]
    assert _never_minted(w, before) == []
    assert [e.kind for e in out] == ["body.changed"]


def test_mutation_a_minting_grown_turns_the_never_mint_check_red(monkeypatch):
    def minting(w, a, parties, bands, bodies):
        return {pid: {**(w.persons[pid].capability or {}), KEY: 1}
                for pid in dict.fromkeys(parties) if pid in w.persons and bodies.get(pid) != 0}
    monkeypatch.setattr(EC, "_grown", minting)
    w, out, before = _fight(WOUNDED, WOUNDED, {})
    assert _never_minted(w, before) == [ACTOR, SUBJECT]
    assert _raised(out) == [ACTOR, SUBJECT]


def test_capture_and_accept_grow_by_the_same_rule():
    """Each verb's EFFECT, called on a bloodied scene (capture's and accept's preconditions -- a seat, a held
    challenge -- are their own tests'): the grown party is named on `capability` earning its kind, and applying the
    Change raises him by one."""
    checked = 0
    for verb, operand in (("capture", "subject"), ("accept", "to")):
        w = P.tiny_world()
        w.persons[ACTOR].capability = {KEY: 2}
        w.persons[SUBJECT].capability = {}
        raw = {"wound_state": {SUBJECT: party_state(**_BAND[UNTOUCHED]), ACTOR: party_state(**_BAND[WOUNDED])}}
        res = Resolution(degree_of(raw, SUBJECT, w.fixtures), raw)
        ch = EFFECTS[verb](w, Act(id="cp304" + verb, actor=ACTOR, verb=verb, payload={operand: SUBJECT}), res)
        grown = [s for s in ch.subjects if "capability.raised" in s.kinds]
        assert [s.id for s in grown] == [ACTOR], (verb, ch.subjects)
        ch.apply()
        assert w.persons[ACTOR].capability[KEY] == 3 and KEY not in w.persons[SUBJECT].capability
        checked += 1
    assert checked == 2
    assert set(EC.GROWN_KINDS) == {"capability.raised"}
    for verb in BODY_VERBS:
        row = VERBS.VERB_TABLE[verb]
        for band in (FELLED, WOUNDED):
            assert "Person.capability" in row.writes_at(band) and "capability.raised" in row.emits_at(band)
        assert "Person.capability" not in row.writes_at(UNTOUCHED)


# ---- the season: outcome mover once a key is held, formation mover at control -----------------------------------

@pytest.mark.parametrize("seed", [0, 1, 2])
def test_control_formation_moves_every_hash_and_the_item_off_reproduces_the_pre_item_hash(seed, monkeypatch,
                                                                                         _engine):
    from .test_strife_credit import revert_cr79
    revert_cr79(monkeypatch)    # v11 CR-79 (the credit term, a later mover of the told deposit): reverted, so this pin reads its own item
    # v11 CP-T03-07 (`Person.body_ceiling`, a schema mover of every realm) is reverted in process on BOTH arms
    # (`test_cp_t03_07_body_ceiling.py::revert_cp_t03_07`, whose own control reproduces POST_ITEM), so both pins stand.
    from .test_cp_t03_07_body_ceiling import revert_cp_t03_07
    revert_cp_t03_07(monkeypatch)
    from .test_cp_t03_08_tend_on_the_wounded import revert_cp_t03_08
    revert_cp_t03_08(monkeypatch)   # v11 CP-T03-08 (`tend` forms on the wounded, a formation mover of every season), the same way
    from .test_b11a_duel_reach import revert_b11a
    revert_b11a(monkeypatch)   # B11 lane A (the duel chain's reach, a formation mover of every season), the same way
    from .test_b11a_scores_and_obstacle import revert_b11a_scores
    revert_b11a_scores(monkeypatch)   # B11 lane A (persons hold scores; the obstacle by task: a mover of the build and every season), the same way
    w = build_realm(seed)
    run(1, seed, w=w)
    assert w.content_hash() == POST_ITEM[seed] != PRE_ITEM[seed]
    revert_cp_t03_04(monkeypatch)
    w = build_realm(seed)
    run(1, seed, w=w)
    assert w.content_hash() == PRE_ITEM[seed]


def test_season_every_person_holding_arms_2_some_survivor_grows_at_the_encounter_step(_engine):
    """Every person in `build_realm(1)` planted at `arms` 2 (= `pool_default`, so no roll moves: pool 8, Ob 1.0):
    after one season at least one survivor holds 3 -- the write admitted at ENCOUNTER, where the season fights --
    and every value is 2 or more (nothing lowered, nothing minted)."""
    w = build_realm(1)
    for p in w.persons.values():
        p.capability = {**(p.capability or {}), KEY: 2}
    run(1, 1, w=w)
    vals = Counter(int(p.capability[KEY]) for p in w.persons.values())
    assert sum(vals.values()) >= 50
    assert min(vals) >= 2 and max(vals) >= 3, dict(vals)
    # `train` also raises a held key, so the growth is attributed: at least one `capability.raised` caused by a
    # body verb (measured at the build: one, by a `capture`; one more by a `train`).
    from ..queries.world_q import causing_act
    by = Counter(getattr(causing_act(w, e), "verb", None) for e in w.log if e.kind == "capability.raised")
    assert sum(by[v] for v in BODY_VERBS) >= 1, dict(by)
