"""CP-T01-05 -- `effort`: spend your scene on one roll.

An act may carry `effort` (0, 1 or 2) in its payload. It fills `1 + effort` of its scene's interaction
slots, and each slot of effort is one NAMED LEVEL (`effort_level`, a fixture) entering the social roll's
sigma term through the closed roster `rosters.yaml: advantage_sources`. Effort is a mu-shift in sigma units,
never a flat bonus on the net and never an Ob reduction (`resolution-diagnostic` section 2).

THE CLAIMS, AND WHAT WOULD SHOW EACH WRONG:
  * THE PLAY SURFACE PRICES AND BOUNDS BY SLOTS, NOT BY `len(acts)` AND NOT BY THE CALLER'S `extended` FLAG:
    (i) one effort-1 `tell` in a scene whose caller left `extended` False costs 2 scene actions; (ii) one
    effort-2 act plus one more is 4 slots against a bound of 3 and is refused; (iii) one effort-1 act plus
    one plain act is 3 slots, admitted, cost 2.
  * THE EFFORT REACHES THE ROLL AS A NAMED LEVEL: the record's leverage is `levels_to_net_sigma` of the
    roster's levels (0.5 at effort 1, `moderate`), and the boost the roll adds is `net_boost`'s, so it SCALES
    with the root of the pool (a flat bonus would add the same net at pool 2 and pool 4).
  * ONE ID, ONE DRAW: an effort act is one act, so it takes the draw keyed by its own id; its roll differs
    from the same act at effort 0 by the boost alone.
  * THE CONTROL: no effort is the shipped chooser's case; the channel sums to 0.0 and `slots == len(acts)`.
  * THE N-LINE (`argue`, Success-only writes): at pool 2 against Ob 2, one effort-2 act deals
    Success-or-better more often than three stacked acts of the same cost (three plain acts in a three-slot
    scene), dealt through the real fold on hand-minted ids. `surveil`, where Partial writes, is REPORTED and not
    claimed: there stacking matches or beats effort.
"""
from __future__ import annotations

import math
import random

import pytest

from engine.dice_engine.sigma_leverage import band_odds, levels_to_net_sigma, net_boost

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.rosters import roster
from ..gaps import Ungraded
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..seam import grade
from ..seam.wrappers import sigma
from ..state.carriers import Act, Scene
from . import test_in12_step9 as T9

TOP = ("Success", "Overwhelming")


def _spent_by_king(scenes_of):
    """Run one season of `p_king` choosing the scenes `scenes_of(w, p)` returns once; the scene actions spent."""
    w = P.tiny_world(DEFAULT_FIXTURES)
    w = P._one_pass(w)
    p = w.persons["p_king"]

    def choose(person, v, s, ask_budget):
        return scenes_of(w, p) if person.id == "p_king" else []

    d = SeasonDriver(w)
    d.season(P.once(choose), None)
    return d._spent.get("p_king", 0)


def _tell(w, p, key, **payload):
    return P.Act_(w, p, "tell", key=key, payload={"subject": "p_mid", "to": "p_mid", **payload})


# ---------------------------------------------------------------------------------------------
# THE PLAY SURFACE: slots price and bound a scene
# ---------------------------------------------------------------------------------------------

def test_i_one_effort_1_tell_costs_two_scene_actions_with_extended_left_false():
    ext = DEFAULT_FIXTURES.get("extended_scene_cost")
    assert ext == 2, "the arm reads 2 scene actions off the shipped extended cost"
    spent = _spent_by_king(lambda w, p: [Scene("s0", p.id, [_tell(w, p, "t0", effort=1)])])
    assert spent == 2, spent
    plain = _spent_by_king(lambda w, p: [Scene("s0", p.id, [_tell(w, p, "t0")])])
    assert plain == 1, plain                                  # the control: the same scene at effort 0


def test_ii_one_effort_2_act_plus_one_more_is_refused_four_slots_against_three():
    cap = DEFAULT_FIXTURES.get("interactions_per_scene")
    assert cap == 3
    with pytest.raises(Ungraded) as refused:
        _spent_by_king(lambda w, p: [Scene("s0", p.id, [_tell(w, p, "t0", effort=2), _tell(w, p, "t1")])])
    assert "interactions" in str(refused.value), refused.value
    # the control, one clause away: the same two acts at effort 0 are two slots and are admitted
    assert _spent_by_king(lambda w, p: [Scene("s0", p.id, [_tell(w, p, "t0"), _tell(w, p, "t1")])]) == 2


def test_iii_one_effort_1_act_plus_one_plain_act_is_three_slots_admitted_at_cost_two():
    def scenes(w, p):
        sc = Scene("s0", p.id, [_tell(w, p, "t0", effort=1), _tell(w, p, "t1")])
        assert sc.slots == 3
        return [sc]
    assert _spent_by_king(scenes) == 2


def test_slots_equal_len_acts_when_no_act_carries_effort_and_cost_follows_the_slots():
    w = P.tiny_world(DEFAULT_FIXTURES)
    p = w.persons["p_king"]
    for n in (1, 2, 3):
        sc = Scene("s", p.id, [_tell(w, p, f"t{i}") for i in range(n)])
        assert sc.slots == len(sc.acts) == n
        assert sc.cost(2) == (2 if n > 1 else 1)
    # the price is derived from the slots (the scene carries no flag a caller could set)
    sc = Scene("s", p.id, [_tell(w, p, "t0", effort=1)])
    assert sc.cost(2) == 2
    assert Scene("s", p.id, [_tell(w, p, "t0"), _tell(w, p, "t1")]).cost(2) == 2
    assert Scene("s", p.id, [_tell(w, p, "t0")]).cost(2) == 1


# ---------------------------------------------------------------------------------------------
# THE ROLL: a named level, a mu-shift, one draw
# ---------------------------------------------------------------------------------------------

def _w():
    w = P.tiny_world(DEFAULT_FIXTURES)
    SeasonDriver(w)                                   # the registrar fills MODULE_ENTRIES
    return w


def test_the_roster_is_closed_and_every_member_has_its_function():
    assert set(roster("advantage_sources")) == {"effort"}
    assert set(sigma.ADVANTAGE_SOURCES) == set(roster("advantage_sources"))


def test_effort_reaches_the_record_as_a_named_level_and_odds_of_reads_it():
    w = _w()
    moderate = DEFAULT_FIXTURES.get("effort_level")
    assert moderate == "moderate"
    for e in (0, 1, 2):
        inp = sigma.contest_input(w, ["p_low"], verb="tell", subject="p_mid", effort=e)
        assert inp.leverage == levels_to_net_sigma([moderate] * e)
    assert sigma.contest_input(w, ["p_low"], verb="tell", subject="p_mid").leverage == 0.0
    act = Act(id="a1", actor="p_low", verb="tell", payload={"subject": "p_mid", "to": "p_mid", "effort": 1})
    got = sigma.odds_of(w, act)
    want = band_odds(2, 2.0, net_boost(0.5, 2))
    assert got == want, (got, want)
    assert round(sum(got[1:]) * 100, 2) == 43.46                       # Partial-or-better at effort 1
    two = sigma.odds_of(w, Act(id="a2", actor="p_low", verb="tell",
                               payload={"subject": "p_mid", "to": "p_mid", "effort": 2}))
    assert round(sum(two[1:]) * 100, 2) == 57.65 and round(sum(two[2:]) * 100, 2) == 25.79


def test_the_boost_scales_with_the_pool_it_is_not_a_flat_bonus():
    w = _w()
    nets = {}
    for pool in (2, 4):
        w.persons["p_low"].capability = {"copying": pool}
        w.persons["p_mid"].capability = {"copying": 4}
        base = sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell", subject="p_mid",
                             rng=random.Random(7))
        pushed = sigma.resolve(w, ["p_low"], ["c"], "a standing", verb="tell", subject="p_mid",
                               rng=random.Random(7), effort=1)
        assert base["pool"] == pushed["pool"] == pool and base["ob"] == pushed["ob"]
        nets[pool] = pushed["net"] - base["net"]
        assert math.isclose(nets[pool], net_boost(0.5, pool)), (pool, nets[pool])
        assert pushed["leverage"] == 0.5 and base["leverage"] == 0.0
    assert nets[4] > nets[2] and math.isclose(nets[4] / nets[2], math.sqrt(2)), nets


def test_the_inquiry_route_carries_effort_too():
    w = _w()
    route = {"provider": "social_contest", "module_entry": "social_contest.roll"}
    out = grade(w, ["p_low"], ["a"], route, verb="surveil", subject="Hh", rng=random.Random(3), effort=2)
    assert out["leverage"] == 1.0, out
    assert grade(w, ["p_low"], ["a"], route, verb="surveil", subject="Hh", rng=random.Random(3))["leverage"] == 0.0


# ---------------------------------------------------------------------------------------------
# THE N-LINE: argue, at the play surface, on hand-minted ids
# ---------------------------------------------------------------------------------------------

def _argue_top_rates(n):
    """`(effort-2 rate, stacked-3 rate)` of Success-or-better over `n` fresh worlds each, dealt through the
    real fold. The stacked arm is three hand-minted-id acts resolved in ONE pass (a three-slot scene's worth)."""
    effort_hits = stacked_hits = 0
    for i in range(n):
        w, d, pid, _ = T9._argue_world()
        act = Act(id=f"ar_e{i}", actor=T9.ARGUER, verb="argue",
                  payload={"subject": pid, "to": T9.HEARER, "effort": 2})
        out = T9._resolve(w, d, act)
        assert len(out) >= 1 and out[0].degree is not None, [(e.kind, e.degree) for e in out]
        effort_hits += out[0].degree in TOP
        w, d, pid, _ = T9._argue_world()
        acts = [T9._argue(pid, f"ar_s{i}_{j}") for j in range(3)]
        out = T9._resolve(w, d, *acts)
        degrees = [e.degree for e in out if e.kind.startswith("argument.")]    # one per act
        assert len(degrees) == 3, [(e.kind, e.degree) for e in out]
        stacked_hits += any(g in TOP for g in degrees)
    return effort_hits / n, stacked_hits / n


def test_argue_one_effort_2_act_beats_three_stacked_acts_on_success_or_better():
    w, _d, pid, _ = T9._argue_world()
    one = sigma.odds_of(w, Act(id="x", actor=T9.ARGUER, verb="argue",
                               payload={"subject": pid, "to": T9.HEARER, "effort": 2}))
    plain = sigma.odds_of(w, T9._argue(pid, "y"))
    p_effort = sum(one[2:])
    p_stacked = 1 - (1 - sum(plain[2:])) ** 3
    assert round(p_effort * 100, 1) == 25.8 and round(p_stacked * 100, 1) == 19.6
    n = 1200
    got_effort, got_stacked = _argue_top_rates(n)
    for got, want in ((got_effort, p_effort), (got_stacked, p_stacked)):
        se = math.sqrt(want * (1 - want) / n)
        assert abs(got - want) <= 3 * se, (got, want)           # the dealt rate is the shown rate
    assert got_effort > got_stacked, (got_effort, got_stacked)


def test_surveil_is_reported_not_claimed():
    """Partial writes at `surveil`, so stacked acts match or beat one effort-2 act on Partial-or-better."""
    effort2 = band_odds(2, 2.0, net_boost(levels_to_net_sigma(["moderate"] * 2), 2))
    plain = band_odds(2, 2.0)
    stacked_p = 1 - (1 - sum(plain[1:])) ** 3
    stacked_s = 1 - (1 - sum(plain[2:])) ** 3
    print(f"\n  surveil, pool 2 against Ob 2: effort 2 Partial+ {sum(effort2[1:]):.4f} / Success+ "
          f"{sum(effort2[2:]):.4f}; three stacked acts Partial+ {stacked_p:.4f} / Success+ {stacked_s:.4f}")
    assert stacked_p >= sum(effort2[1:]) - 0.05
    assert sum(effort2[2:]) > stacked_s
