"""B11 lane A -- PERSONS HOLD SCORES, AND THE SOCIAL ROLL'S OBSTACLE IS THE TASK'S DIFFICULTY PLUS ITS NAMED MODIFIERS.

  (3) `build_realm` seats `rosters.yaml: unauthored_attributes` under every person's authored `stats:` (`cast_attributes`
      ships on), so every person holds a score on every vocation's attribute.
  (4) one score, two roles (`10_DICE_one_score_two_roles.md`): `seam/wrappers/pool.py::score` is the base of a person's
      pool and the score his opponent's obstacle halves (`sigma.py::_opposition_of`), so `obstacle_default` never stands in
      for a person. `modules/social_contest/roll.py::obstacle_terms` composes Ob = the task's difficulty
      (`rosters.yaml: task_difficulty`, closed over the verbs the roll deals) + the opposing person's score / 2 (the
      2026-08-14 RULED term, one modifier, unchanged) - the room's terms + an examined document's forgery quality, under the
      ceiling, and names every term on the roll's record (`resolve`'s `ob_terms`). `interrogate`, `arrest` and `determine`
      name a vocation.
  CONTROL: `Fixtures obstacle_model: stand_in` composes the obstacle before this item, byte for byte (asserted over a grid of
  records here); `revert_b11a_scores` (the switch, the bundle off) reproduces the reach commit's realm hashes.
"""
from __future__ import annotations

import pytest

from ..data import rosters as R
from ..data import verbs as V
from ..data import cast
from ..data.fixtures import DEFAULT_FIXTURES
from ..gaps import Forbidden, Unspecified
from ..harness import populated
from ..harness import probes as P
from ..harness.populated import build_realm, run
from ..queries.inputs import SocialContestInput
from ..seam.wrappers import pool, sigma
from .test_sc01_obstacle_ceiling import _module


#: `build_realm(s)` then one season, this commit's tree; PRE is the reach commit's (`test_b11a_duel_reach.POST`).
#: Re-pinned in B01.02 on the rebased tree, PYTHONHASHSEED=0 (was the branch's 29a11c75... / 52e48937... / 5b948b83...,
#: `1424aa7`'s world, discarded per C3-A2).
POST = {0: "ad4dad1d9758e343329a7b9b90fbdb46", 1: "056bff314ba696f54e8ff21212057221", 2: "7f93eb2554768480d816c5fd040ffd9e"}


def revert_b11a_scores(monkeypatch) -> None:
    """THIS ITEM AT ITS REVERT, for the life of one test: the obstacle composed as before (`obstacle_model: stand_in`) and
    no attribute seated (the bundle and the cast's `stats:` read as empty, which `cast_attributes=False` writes). A test
    pinning an earlier hash calls it."""
    monkeypatch.setitem(DEFAULT_FIXTURES._v, "obstacle_model", "stand_in")
    # an earlier item's revert may have swept `populated`'s fixtures into a copy: switch that copy IN PLACE, so a later revert
    # in the same chain that edits the copy (or the original) keeps this switch
    monkeypatch.setitem(populated.DEFAULT_FIXTURES._v, "obstacle_model", "stand_in")
    monkeypatch.setattr(populated, "UNAUTHORED_ATTRIBUTES", {})
    monkeypatch.setattr(cast, "attributes_of", lambda r: {})
    for verb in ("interrogate", "arrest", "determine"):          # the three `verb_capability` rows (one dict, read by name)
        monkeypatch.delitem(R.VERB_CAPABILITY, verb)
    # and `VOCATIONS` re-read off what is left at each module that bound it (`test_cp_t03_04_arms.revert_cp_t03_04`'s list):
    # an earlier revert that took `arms`'s own rows out kept `arms` only because `arrest` still drew on it
    from ..decision import options as _OPT
    from ..loop import effects_combat as _EC
    left = frozenset(R.VERB_CAPABILITY.values())
    for mod in (R, V, _OPT, _EC):
        monkeypatch.setattr(mod, "VOCATIONS", left)


def _inp(**kw) -> SocialContestInput:
    base = dict(pool=2, opposition=None, obstacle_default=2.0, obstacle_ceiling=None, obstacle_refusal_multiple=2.0,
                leverage=0.0)
    base.update(kw)
    return SocialContestInput(**base)


def _legacy(inp) -> float:
    """The obstacle before this item, verbatim (its control)."""
    from engine.dice_engine.sigma_leverage import OB_MIN
    ob = float(inp.opposition) / 2.0 if inp.opposition is not None else float(inp.obstacle_default)
    room = float(inp.reception_gain) * float(inp.reception) + float(inp.proof_step) * float(inp.proofs)
    ob = max(ob - room, min(ob, float(OB_MIN))) if room > 0 else ob - room
    ob += float(inp.forgery_quality)
    if inp.obstacle_ceiling is None:
        return ob
    cap = float(inp.obstacle_ceiling)
    if inp.ceiling_per_pool and inp.pool >= 1:
        cap = _module()._chance_floor_cap(inp.pool, cap) or cap
    return min(ob, cap)


# ---- (3) the bundle --------------------------------------------------------------------------------------------

def test_the_bundle_is_closed_over_the_ten_attributes_and_refuses_otherwise():
    from engine.substrate.descriptors import ATTRIBUTES
    assert set(R.UNAUTHORED_ATTRIBUTES) == set(ATTRIBUTES)
    bad = dict(R.UNAUTHORED_ATTRIBUTES)
    bad.pop(next(iter(bad)))
    with pytest.raises(Unspecified):
        R._load_unauthored_attributes(bad)
    with pytest.raises(Unspecified):
        R._load_unauthored_attributes({**R.UNAUTHORED_ATTRIBUTES, "attr.body.strength": 99})


def test_every_realm_person_holds_every_attribute_and_an_authored_one_wins():
    w = build_realm(0)
    assert all(set(p.attributes) == set(R.UNAUTHORED_ATTRIBUTES) for p in w.persons.values())
    authored = [p for p in w.persons.values() if p.attributes != R.UNAUTHORED_ATTRIBUTES]
    assert authored, "no cast row's `stats:` reached a person over the bundle"


# ---- (4) one score, two roles -----------------------------------------------------------------------------------

def test_score_is_the_pool_without_its_addends():
    w = P.tiny_world()
    p = w.persons["p_mid"]
    for verb in ("tell", "argue", "interrogate", "fight"):
        assert pool.faculty(w, p, verb) == pool.score(w, p, verb) + sum(int(a(w, p, verb)) for a in pool.POOL_ADDENDS)


def test_a_person_opposes_with_the_score_he_rolls_and_the_control_reads_the_held_values():
    w = P.tiny_world()
    hearer = w.persons["p_low"]
    assert hearer.attributes in ({}, None) and not hearer.capability.get("copying")
    assert sigma._opposition_of(w, "p_low", "tell") == float(w.fixtures.get("pool_default"))
    w.fixtures = w.fixtures.sweep("obstacle_model", "stand_in")
    assert sigma._opposition_of(w, "p_low", "tell") is None, "CONTROL: a person holding nothing opposed at the stand-in"


def test_the_task_difficulty_is_closed_over_the_verbs_the_roll_deals():
    assert set(V.TASK_DIFFICULTY) == V.social_roll_verbs()
    assert {"interrogate", "arrest", "determine"} <= set(R.VERB_CAPABILITY)
    with pytest.raises(Forbidden):
        V._load_task_difficulty({k: v for k, v in V.TASK_DIFFICULTY.items() if k != "tell"})
    with pytest.raises(Forbidden):
        V._load_task_difficulty({**V.TASK_DIFFICULTY, "give": 1.0})


def test_the_obstacle_is_the_difficulty_plus_the_ruled_score_term_and_every_term_is_named():
    ob, terms = _module().obstacle_terms(_inp(difficulty=1.0, opposition=4.0))
    assert (ob, terms) == (3.0, {"difficulty": 1.0, "opposition": 2.0})
    ob, terms = _module().obstacle_terms(_inp(difficulty=2.0))
    assert (ob, terms) == (2.0, {"difficulty": 2.0}), "no person opposes: no score term and no stand-in"
    ob, terms = _module().obstacle_terms(_inp(difficulty=1.0, opposition=2.0, reception=1.0, reception_gain=0.5,
                                         forgery_quality=1.0, obstacle_ceiling=2.0))
    assert set(terms) == {"difficulty", "opposition", "room", "forgery", "ceiling"}
    assert ob == pytest.approx(sum(terms.values()), abs=1e-12)


def test_falsifier_a_higher_opposing_score_raises_the_obstacle_and_lowers_the_odds():
    from engine.dice_engine.sigma_leverage import record_odds
    obs = [_module().obstacle(_inp(difficulty=1.0, opposition=float(s))) for s in (1, 2, 4, 6)]
    assert obs == sorted(obs) and len(set(obs)) == 4
    fail = [record_odds(2, ob, 0.0)[0] for ob in obs]
    assert fail == sorted(fail) and fail[0] < fail[-1]


@pytest.mark.parametrize("opp", [None, 0.0, 1.0, 2.0, 3.0, 7.0])
@pytest.mark.parametrize("room", [(0.0, 0.0), (1.0, 0.5), (-1.0, 0.5)])
@pytest.mark.parametrize("ceil", [None, 2.0])
@pytest.mark.parametrize("fq", [0.0, 1.0])
def test_control_the_stand_in_arm_composes_the_old_obstacle_exactly(opp, room, ceil, fq):
    inp = _inp(opposition=opp, reception=room[0], reception_gain=room[1], obstacle_ceiling=ceil,
               forgery_quality=fq, ceiling_per_pool=True)
    assert _module().obstacle(inp) == _legacy(inp)           # exact, not approx: the control is byte-identity


# ---- the realm hash: mover, and the revert ---------------------------------------------------------------------

@pytest.mark.parametrize("seed", [0, 1, 2])
def test_hash_post_item_and_revert(seed, monkeypatch):
    from .test_b11a_duel_reach import POST as PRE
    w = build_realm(seed)
    run(1, seed, w=w)
    assert w.content_hash() == POST[seed] != PRE[seed]
    revert_b11a_scores(monkeypatch)
    w = build_realm(seed)
    run(1, seed, w=w)
    assert w.content_hash() == PRE[seed]
