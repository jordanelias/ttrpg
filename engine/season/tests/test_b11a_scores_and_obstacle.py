"""B11 lane A -- PERSONS HOLD SCORES, AND THE SOCIAL ROLL'S OBSTACLE IS THE TASK'S DIFFICULTY PLUS ITS NAMED MODIFIERS.
(B05.14 re-grounds the obstacle half on the one form: `test_obstacle_form.py` owns the form's claims; what stays here is lane A's
PERSON half and the rising-obstacle case, read on the new composer.)

  (3) `build_realm` seats the sheet `state/carriers.py::generated_attributes` draws (B01a.01; B01 seated `pool_default` on
      every key) under every person's authored `stats:` (`cast_attributes` ships on), so every person holds a score on
      every vocation's attribute. Its tests moved to `test_b01a_generated_attributes.py`.
  (4) one score, two roles (`10_DICE_one_score_two_roles.md`): `seam/wrappers/pool.py::score` is the base of a person's
      pool and the skill score his opponent's obstacle reads (`sigma.py::_opposition_of`), which the opposing ATTRIBUTE joins
      (`_opposing`, B05.14, A-137). `modules/social_contest/roll.py::obstacle` composes the obstacle -- the even line + the act's
      `difficulty:` level + `opposed_ob(opposition)` - the room's terms + an examined document's forgery quality, under the
      ceiling and over the floor -- and names every term on the roll's record (`Margin.terms`, `resolve`'s `terms`). `interrogate`,
      `arrest` and `determine` name a vocation.
  CONTROL (B05.14): the stand-in arm (`Fixtures obstacle_model`, a grid of records against `_legacy`) is gone with the arm; its
  replacement is `test_obstacle_form.py::test_step_1a_composes_todays_obstacle_at_control`. `revert_b11a_scores` (no attribute
  seated) is what other files' reverts call. The realm hashes are `_realm_goldens.py`'s.
"""
from __future__ import annotations

from engine.dice_engine.sigma_leverage import even_line, opposed_ob, pool_of, record_odds

from ..data import verbs as V
from ..data import cast
from ..boot import realm as boot_realm
from ..data.fixtures import DEFAULT_FIXTURES
from ..harness import probes as P
from ..queries import person_q
from ..queries.inputs import SocialContestInput
from ..seam.wrappers import pool, sigma
from ..state.carriers import Claim
from .test_sc01_obstacle_ceiling import _module


def revert_b11a_scores(monkeypatch) -> None:
    """THIS ITEM AT ITS REVERT, for the life of one test: no attribute seated (`generated_attribute_range` None and the cast's
    `stats:` read as empty, which `cast_attributes=False` writes). A test pinning an earlier hash calls it. (B05.14: the obstacle's
    `stand_in` arm it once also switched to is deleted with `Fixtures obstacle_model`.)"""
    # the `None` point of `generated_attribute_range` is the earlier no-seating world (B01a.01, H-856)
    monkeypatch.setitem(DEFAULT_FIXTURES._v, "generated_attribute_range", None)
    monkeypatch.setitem(boot_realm.DEFAULT_FIXTURES._v, "generated_attribute_range", None)
    monkeypatch.setattr(cast, "attributes_of", lambda r: {})
    for verb in ("interrogate", "arrest", "determine"):          # the three `verb_capability` rows (one dict, read by name)
        monkeypatch.delitem(V.VERB_CAPABILITY, verb)
    # and `VOCATIONS` re-read off what is left at each module that bound it (`test_cp_t03_04_arms.revert_cp_t03_04`'s list):
    # an earlier revert that took `arms`'s own rows out kept `arms` only because `arrest` still drew on it
    from ..decision import options as _OPT
    from ..loop import effects_combat as _EC
    left = frozenset(V.VERB_CAPABILITY.values())
    for mod in (V, _OPT, _EC):
        monkeypatch.setattr(mod, "VOCATIONS", left)


def _inp(**kw) -> SocialContestInput:
    base = dict(pool=2, opposition=None, obstacle_ceiling=None, obstacle_refusal_multiple=2.0, leverage=0.0,
                difficulty=1.0, pool_default=2, pool_add=0, opposition_rate=0.5)
    base.update(kw)
    return SocialContestInput(**base)


# ---- (3) the generated sheet: B01a.01's tests are `test_b01a_generated_attributes.py` -----------------------------

# ---- (4) one score, two roles -----------------------------------------------------------------------------------

def test_the_pool_is_the_governing_score_plus_the_rank_and_the_score_is_the_opposition_s():
    """B05.25 replaced "the score is the pool without its addends" (lane A's one score, two roles): the pool is
    `pool_of(governing score + rank, addends, pool_add, pool_floor)` and the skill score is the opposition's operand only."""
    w = P.tiny_world()
    p = w.persons["p_mid"]
    add, floor = w.fixtures.get("pool_add"), w.fixtures.get("pool_floor")
    checked = 0
    for verb in ("determine", "arrest", "research"):                # B05.25: `fight` is a subsystem's row and names no `governing:`, so `faculty` refuses it
        addends = sum(int(a(w, p, verb)) for a in pool.POOL_ADDENDS)
        assert pool.faculty(w, p, verb) == pool_of(pool.governing_score(w, p, verb) + pool.rank(p, verb), addends, add, floor)
        assert pool.faculty(w, p, verb) != pool.score(w, p, verb) + addends     # at the shipped base, not the old rule
        checked += 1
    assert checked == 3


def test_a_person_opposes_with_the_score_he_rolls():
    """B05.11: `_opposition_of` returns the skill score (no arm switch): a person holding nothing opposes at `pool_default`, a
    non-person subject opposes at nothing (the module's `opposed_ob(pool_default)` stands there). The record's `opposition` adds the
    resisting attribute (B05.14: `_opposing`)."""
    w = P.tiny_world()
    hearer = w.persons["p_low"]
    assert hearer.attributes in ({}, None) and not hearer.capability.get("arms")
    assert sigma._opposition_of(w, "p_low", "arrest") == float(w.fixtures.get("pool_default"))
    assert sigma._opposition_of(w, "site_harbour", "arrest") is None
    assert sigma._opposing(w, "site_harbour", "arrest") is None
    # score + the unheld attribute: the untrained score and (B05.16) the scale's mid-point; was 2 x pool_default
    assert sigma._opposing(w, "p_low", "arrest") == float(w.fixtures.get("pool_default")) + pool.attribute_midpoint() == 6.0


def test_every_verb_the_roll_deals_names_a_level_the_fixture_sizes():
    assert V.social_roll_verbs() and {"interrogate", "arrest", "determine"} <= set(V.VERB_CAPABILITY)
    sizes = DEFAULT_FIXTURES.get("difficulty_ob")
    assert {V.VERB_TABLE[v].difficulty for v in V.social_roll_verbs()} <= set(sizes)


def test_the_obstacle_is_the_form_and_every_term_is_named():
    ob, terms = _module().obstacle(_inp(difficulty=1.0, opposition=4.0))
    assert (ob, terms) == (3.0, (("even", 0.0), ("difficulty", 1.0), ("opposition", 2.0)))
    ob, terms = _module().obstacle(_inp(difficulty=2.0))
    assert (ob, terms) == (3.0, (("even", 0.0), ("difficulty", 2.0), ("opposition", 1.0))), "no person opposes: `opposed_ob(pool_default)`, never absent"
    ob, terms = _module().obstacle(_inp(difficulty=1.0, opposition=2.0, reception=1.0, reception_gain=0.5,
                                        forgery_quality=1.0, obstacle_ceiling=2.0))
    # B05.17: lane A's `room` step left the module (a favourable room is leverage, a hostile one the roster's `reception` term,
    # carried in `obstacle_operands`), so the record's `reception` no longer composes a step here; was [.., "room", ..]
    assert [n for n, _ in terms] == ["even", "difficulty", "opposition", "forgery", "ceiling"]
    assert ob == sum(v for _, v in terms) == 2.0


def test_falsifier_a_higher_opposing_score_raises_the_obstacle_and_lowers_the_odds():
    """Scores 1, 2, 4, 6 give strictly rising obstacles and a strictly rising P(Failure) (kept from lane A's file, now on the one form)."""
    obs = [_module().obstacle(_inp(difficulty=1.0, opposition=float(s)))[0] for s in (1, 2, 4, 6)]
    assert all(a < b for a, b in zip(obs, obs[1:])), obs                 # strictly rising
    fail = [record_odds(2, ob, 0.0)[0] for ob in obs]
    assert all(a < b for a, b in zip(fail, fail[1:])), fail              # P(Failure) strictly rising, no step ties


def test_falsifier_a_believer_weighs_an_arrest_against_a_person_only_on_what_he_has_a_claim_on():
    """B24p.99: re-pointed from `lie` (which proceeds since B24p.19; no single-roll row names no vocation and an `opposed_attribute`) to `arrest`,
    the hearer holding no `arms` key: the roll opposes him at the untrained score on the skill half; the
    `opposed_attribute` half (`attr.body.strength`) is that person's own. The believer (`believed_input`, what the chooser weighs,
    `odds_weighting: believed`) holds no claim on it, so he CANNOT SAY (`None`, never a figure -- B05.14); with a claim equal to what the
    person holds, his record composes the SAME obstacle the roll is dealt. A non-person subject opposes at nothing, and that he knows."""
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("obstacle_ceiling", None))                  # uncapped: the cap is not this test's subject
    liar, hearer = w.persons["p_mid"], w.persons["p_low"]
    assert not hearer.capability.get(V.VERB_CAPABILITY["arrest"]), "the hearer holds no skill for the verb: the skill half is the untrained score"
    opposed = V.VERB_TABLE["arrest"].opposed_attribute
    hearer.attributes = {opposed: 6}
    fx = w.fixtures
    even, routine, rate = even_line(fx.get("pool_add")), fx.get("difficulty_ob")[V.VERB_TABLE["arrest"].difficulty], fx.get("opposition_rate")
    dealt = sigma._composed_obstacle(sigma.contest_input(w, [liar.id], verb="arrest", subject="p_low"))
    # B05.99 re-pin (B05.14's even line, B05.23's calibrated arm): even + difficulty + the rate x (his attribute + the untrained
    # score); was 1.0 + 0.5 x (4 + 2) at the control sizes
    assert dealt == even + routine + opposed_ob(6 + 2, rate), dealt
    kw = dict(pool=pool.faculty(w, liar, "arrest"), person_subject=True)
    # B05.62 ships `believed_prior: ordinary`: the believer with no claim takes the hearer for an ordinary person (the mid-point
    # attribute, the untrained score), so he composes a figure, and it is NOT the dealt one (the hearer holds 6, not 4)
    ordinary = sigma.believed_input(liar, "arrest", "p_low", w.fixtures, **kw)
    assert ordinary is not None and sigma._composed_obstacle(ordinary) == even + routine + opposed_ob(pool.attribute_midpoint() + 2, rate) != dealt
    shipped = w.fixtures
    w.fixtures = w.fixtures.sweep("believed_prior", "none")                     # the prior's control arm: B05.14's rule
    assert sigma.believed_input(liar, "arrest", "p_low", w.fixtures, **kw) is None          # FALSIFIER: a believer reading the dealt figure unasked
    # back at the shipped prior (with `regard_step` 1.0 shipped, the control arm answers None against any lone person, B05.21):
    # a held claim on the attribute is read instead of the ordinary person's
    w.fixtures = shipped
    liar.ledger.append(Claim(id="c0", holder=liar.id, subject="p_low", predicate=person_q.CAPABILITY_CLAIM + opposed, value=6,
                             when=0, source="told", confidence=5, visibility="own"))
    believed = sigma.believed_input(liar, "arrest", "p_low", w.fixtures, **kw)
    assert believed is not None and sigma._composed_obstacle(believed) == dealt
    nobody = sigma.believed_input(liar, "arrest", "site_harbour", w.fixtures, pool=kw["pool"], person_subject=False)
    # nobody opposite: the stand-in, `opposed_ob(pool_default)` (was 2.0 at the control sizes)
    assert nobody is not None and sigma._composed_obstacle(nobody) == even + routine + opposed_ob(fx.get("pool_default"), rate)
