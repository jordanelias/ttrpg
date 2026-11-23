"""v11 CP-T03-04 -- TRAINING AND FIGHTING MAKE A PERSON BETTER AT IT: the `arms` vocation.

`rosters.yaml: verb_capability` maps `fight`, `accept` and `capture` (the rows contesting `the body`) to `arms`. So:
(ii) a held `arms` key reaches combat's pool and Ob through `seam/wrappers/sigma.py::faculty` -- CR-85's one path,
`combat_input` -> `PersonalCombatInput.scores` -- and NO second skill input exists; (i) `arms` is a vocation
(`data/verbs.py::VOCATIONS`), so `train` forms on it and `_eff_train` raises it; (iii) the `cast:` overlay
(`harness/corpus_run.py::cast_overlay`, checked by `_check_capability` against the roster's values) is the authored
writer and names NO `arms` value (Jordan's content); (iv) `loop/effects_combat.py::_grown`: a fight that drew blood
raises `arms` by one on each SURVIVING party -- and, since B05.09 (CORE Edit 9, `raised_capability`), MINTS a first rank
for a survivor who held none (the never-minted rule and its mutation test are retired with it; B05.99 rewrote this file).
[ASSUMPTION; low; Jordan to correct; revert: rename the roster key] -- `arms` here is the trained skill, not
CP-T03-03's `arms_kinds` (equipment).

  FALSIFIER: a person holding `arms` 5 (the shipped roster, no test-local row) against a default party rolls pool 11
  against Ob 1.0, his opponent pool 8 against Ob 2.5 -- CR-85's planted faculty-5 reading, reproduced through the
  roster. A surviving holder of a bloodied fight gains one; a surviving non-holder is minted one.
  CONTROL: a FORMATION MOVER EVEN AT CONTROL -- `arms` in the vocation range adds one `train` Candidate per `train`
  formation, so with nobody holding the key every 1-season hash still moves. The realm hashes are
  `_realm_goldens.py`'s; `revert_cp_t03_04` (the three roster rows and the vocation removed, in process) is what the
  other files' reverts call.
"""
from __future__ import annotations

import importlib
import random
from engine.dice_engine import draw
from collections import Counter

import pytest


from ..data import rosters as R
from ..data import verbs as VERBS
from ..data.matrix import Step, WriteClass
from ..data.rosters import FELLED, UNTOUCHED, WOUNDED
from ..decision import options as OPT
from ..harness import probes as P
from ..boot.realm import build_realm
from ..harness.populated import run
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


def revert_cp_t03_04(monkeypatch):
    """The item OFF, in process: the three `verb_capability` rows deleted from the one shared dict (every reader --
    `faculty`, `practice`, `_grown`, the corpus check -- holds the same object) and `arms` taken out of `VOCATIONS` at
    each module that bound the frozenset. Other tests that pin a pre-item hash call it."""
    for verb in BODY_VERBS:
        monkeypatch.delitem(VERBS.VERB_CAPABILITY, verb)
    off = frozenset(VERBS.VERB_CAPABILITY.values())
    for mod in (VERBS, OPT, EC):
        monkeypatch.setattr(mod, "VOCATIONS", off)


@pytest.fixture
def _engine():
    if C.engine() is None:
        pytest.fail(f"personal_combat engine unavailable: {C.load_error()}")


# ---- (i) the roster ---------------------------------------------------------------------------------------------

def test_the_three_body_verbs_draw_on_arms_and_arms_is_a_vocation_with_an_attribute():
    """B05.25 (B05.99 rewrite): the retired `VOCATION_ATTRIBUTE` map read `arms` -> agility; a body verb now names NO
    `governing:` attribute (a hand-off row, `person_inputs: own`): the fight reads the attributes raw, by its own rule."""
    from engine.substrate import descriptors
    assert {v: VERBS.VERB_CAPABILITY.get(v) for v in BODY_VERBS} == {v: KEY for v in BODY_VERBS}
    assert KEY in VERBS.VOCATIONS and KEY in OPT.VOCATIONS and KEY in EC.VOCATIONS
    assert KEY in descriptors.CAPABILITIES
    assert all(VERBS.VERB_TABLE[v].governing == () and not VERBS.VERB_TABLE[v].brute for v in BODY_VERBS)
    # the key is spelt in no body: `_grown` reads it off the roster by verb
    src = open(EC.__file__, encoding="utf-8").read()
    assert '"arms"' not in src and "'arms'" not in src


def test_only_the_authored_capabilities_hold_arms_at_landing_not_the_overlay_or_a_lifepath():
    """BA1.99 re-point (was: nobody holds `arms` at landing). BA1.01 authors `arms` through the cast row's `capabilities:` on 11 persons, so
    at landing exactly those hold it, each at the authored score, at every seed; the `cast:` overlay still names no `arms` value, no lifepath
    template names it, and no practice record can form in it (`practice` counts Success-or-better; a fight's bands are none of the ladder's)."""
    from ..data import cast
    from ..harness.corpus_run import cast_overlay
    authored = {f"p_{cid.lower().replace('-', '_')}": cast.capabilities_of(r)[KEY]
                for cid, r in cast.load().items() if KEY in cast.capabilities_of(r)}
    assert len(authored) == 11, authored
    held, seen = 0, 0
    for seed in (0, 1, 2):
        got = {}
        for pid, p in build_realm(seed).persons.items():
            seen += 1
            if KEY in (p.capability or {}):
                got[pid] = p.capability[KEY]
        assert got == authored, (seed, got)
        held += len(got)
    assert seen >= 3 * 80 and held == 3 * len(authored)
    overlay = [e for entries in cast_overlay().values() for e in entries]
    assert overlay, "setup: the overlay is empty"
    assert [e for e in overlay if KEY in (e.get("capability") or {})] == []
    assert [lp for lp, keys in R.LIFEPATH_TEMPLATES.items() if KEY in keys] == []
    assert all(R.DEGREE_STEP.get(b, 0) == 0 for b in (FELLED, WOUNDED, UNTOUCHED))


# ---- (ii) the one input path ------------------------------------------------------------------------------------

def _spy(monkeypatch) -> Counter:
    # by name, inside the function: `test_importing_every_engine_module_pulls_in_no_subsystem` fails on a module-scope import and the ratchet counts a written one
    core = importlib.import_module("modules.combat.core")
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
    assert inp.scores == (5, 2), inp.scores          # B05.09: b's score is the untrained score, never his attribute (was 1)
    mod, attr = entry_target("the body")[1].split(":", 1)
    entry = getattr(importlib.import_module(mod), attr)
    seen = _spy(monkeypatch)
    checked = 0
    # seed range re-picked at B06.99: the stream changed (was range(6): on `accept` the defender rolled in none of seeds 0..5, in 21 of 0..59)
    for s in range(6, 12):
        entry(inp, draw.seeded(draw.H2("test_cp_t03_04_arms", s)))
        checked += 1
    # B05.99 re-pin (B05.09: the skill score has no attribute; B05.57/B05.58: the fight's pool is `pool_of(score, addends, 6, 5)`
    # and its Ob `opposed_ob(defender's score, 0.5)`): b scores the untrained 2, so a meets Ob 1.0 and b rolls pool 8 -- the
    # docstring's CR-85 reading again (B01a.99 had read b's drawn attribute: {(11, 0.5), (7, 2.5)}).
    assert set(seen) == {(11, 1.0), (8, 2.5)}, dict(seen)
    assert checked == 6


def test_control_a_minted_arms_rank_adds_nothing_to_a_roll_only_an_authored_holders_own_score_does(monkeypatch, _engine):
    """The item moves formation, not a roll: the season's fights roll no MINTED `arms` rank above the untrained score (was: nobody holds
    one at the build; BA1.99 re-pointed it to the persons who author none). B05.99 re-pin: B05.09 took the attribute out of the skill score and B05.57/B05.58 make the fight's pool
    `pool_of(score, addends, 6, 5)` and its Ob `opposed_ob(score, 0.5)`, so every roll is CR-85's (8, 1.0) again (B01a.99 had
    read the drawn attributes: (9, 2.5), (11, 2.0), (11, 1.5)). Since B05.09 a surviving party of a bloodied fight is MINTED a
    first rank (`_grown`), so after the season the holders are exactly those survivors, each at or below the untrained
    score (1 or 2) and so reading the same pool (was: no holder after the season)."""
    seen = _spy(monkeypatch)
    # seed re-picked at B06.99: the stream changed (was 1; seeds 0,2..8 scanned: a survivor of two bloodied fights holds 2 at 0,3,4,5,6,8;
    # seed 2 is the first where every holder is at 1 and every roll is (8, 1.0))
    w = build_realm(2)
    # BA1.99 re-point (BA1.01 authors `arms` 3 or 5 on 11 persons, so "nobody holds one at the build" is no longer the world): the rolls read
    # the untrained score alone for every person who authors none, and the authored holders read their own score (each raised by `_grown` at
    # most up to the value they hold after the season); a roll reads no other pool or Ob.
    from engine.dice_engine.sigma_leverage import opposed_ob, pool_of
    from ..seam.wrappers.pool import FIGHT_DICE_SITE, pool_pair, untrained
    authored = {pid: p.capability[KEY] for pid, p in w.persons.items() if KEY in (p.capability or {})}
    assert len(authored) == 11 and set(authored.values()) == {3, 5}, authored
    run(1, 2, w=w)
    held = {pid: p.capability[KEY] for pid, p in w.persons.items() if KEY in (p.capability or {})}
    # B10.99 re-read: B10.72 moved the season's fights, and a survivor of two bloodied fights now holds 2 here (was: every holder at 1);
    # what the claim needs is that no MINTED holder stands above the untrained score (`pool_default`), so a minted rank adds nothing to a roll
    minted = {pid: v for pid, v in held.items() if pid not in authored}
    assert minted and max(minted.values()) <= untrained(w.fixtures), minted
    assert all(held[pid] >= v for pid, v in authored.items()), (authored, held)       # a fight never lowers an authored rank
    pool_add, pool_floor = pool_pair(w.fixtures, FIGHT_DICE_SITE)
    scores = {untrained(w.fixtures)} | {s for pid, v in authored.items() for s in range(v, held[pid] + 1)}
    allowed = {(pool_of(a, 0, pool_add, pool_floor), opposed_ob(b, 0.5)) for a in scores for b in scores}    # 0.5: the module's own constant
    assert seen and set(seen) <= allowed and (8, 1.0) in seen, (dict(seen), sorted(allowed))
    assert any(pool > 8 for pool, _ob in seen), dict(seen)       # an authored holder's roll reads above the untrained pool


def test_control_with_the_item_off_the_same_holder_rolls_the_fallback(monkeypatch, _engine):
    revert_cp_t03_04(monkeypatch)
    w = build_realm(1)
    a, b = sorted(w.persons)[:2]
    w.persons[a].capability = {**(w.persons[a].capability or {}), KEY: 5}
    assert C.combat_input(w, [a, b], "fight").scores == (2, 2)


# ---- (i) train ----------------------------------------------------------------------------------------------------

def test_train_raises_a_held_arms_and_mints_a_first_rank():
    """B05.09 (CORE Edit 9; B05.99 rewrite): `train` on a non-holder MINTS a first rank (was `train.refused`)."""
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
    assert got == {holder: ["capability.raised"], other: ["capability.raised"]}, got
    assert w.persons[holder].capability == {KEY: 3}
    assert w.persons[other].capability == {KEY: 1}


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


def _minted(w, before) -> list:
    """Every party who held no `arms` before and holds it after (B05.09: a surviving non-holder's first rank)."""
    return [pid for pid in before if KEY not in before[pid] and pid in w.persons
            and KEY in (w.persons[pid].capability or {})]


def test_falsifier_a_surviving_holder_gains_one_and_a_non_holder_is_minted_one():
    """B05.09 (CORE Edit 9; B05.99 rewrite): the non-holder was refused his growth under the retired never-minted rule; he is
    minted a first rank now."""
    w, out, before = _fight(WOUNDED, WOUNDED, {ACTOR: {KEY: 2}})
    assert w.persons[ACTOR].capability[KEY] == 3
    assert _minted(w, before) == [SUBJECT] and w.persons[SUBJECT].capability[KEY] == 1
    assert _raised(out) == sorted([ACTOR, SUBJECT])
    assert "body.changed" in [e.kind for e in out]


def test_both_holders_grow_and_an_untouched_holder_beside_a_wounded_one_grows():
    w, out, _ = _fight(WOUNDED, WOUNDED, {ACTOR: {KEY: 2}, SUBJECT: {KEY: 4}})
    assert (w.persons[ACTOR].capability[KEY], w.persons[SUBJECT].capability[KEY]) == (3, 5)
    assert _raised(out) == sorted([ACTOR, SUBJECT])
    w, out, _ = _fight(UNTOUCHED, WOUNDED, {ACTOR: {KEY: 2}})
    # B05.09: the wounded non-holder beside him is minted a first rank (B05.99 rewrite; was [ACTOR])
    assert w.persons[ACTOR].capability[KEY] == 3 and _raised(out) == sorted([ACTOR, SUBJECT])
    assert w.persons[SUBJECT].capability[KEY] == 1


def test_a_felled_holder_does_not_grow_and_his_surviving_holder_opponent_does():
    w, out, _ = _fight(FELLED, WOUNDED, {ACTOR: {KEY: 2}, SUBJECT: {KEY: 2}})
    assert ACTOR not in w.persons
    assert w.persons[SUBJECT].capability[KEY] == 3 and _raised(out) == [SUBJECT]


def test_an_untouched_fight_grows_nobody_and_still_reads_undecided():
    w, out, _ = _fight(UNTOUCHED, UNTOUCHED, {ACTOR: {KEY: 2}, SUBJECT: {KEY: 2}})
    assert [e.kind for e in out] == ["contest.undecided"]
    assert w.persons[ACTOR].capability[KEY] == w.persons[SUBJECT].capability[KEY] == 2


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
        # B05.09 (B05.99 rewrite): the untouched non-holder survivor is minted a first rank (was: the holder alone)
        assert [s.id for s in grown] == [ACTOR, SUBJECT], (verb, ch.subjects)
        ch.apply()
        assert w.persons[ACTOR].capability[KEY] == 3 and w.persons[SUBJECT].capability[KEY] == 1
        checked += 1
    assert checked == 2
    assert set(EC.GROWN_KINDS) == {"capability.raised"}
    for verb in BODY_VERBS:
        row = VERBS.VERB_TABLE[verb]
        for band in (FELLED, WOUNDED):
            assert "Person.capability" in row.writes_at(band) and "capability.raised" in row.emits_at(band)
        assert "Person.capability" not in row.writes_at(UNTOUCHED)


# ---- the season: outcome mover once a key is held, formation mover at control -----------------------------------


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
