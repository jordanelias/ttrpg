"""B12b.45 (CL-EVENTS commit (3)) -- THE TENSIONS RECEIVER: `engine/season/tensions.yaml`, its one loader `data/tensions.py`, the closed roster
`rosters.yaml: tension_effects`, `Fixtures territory_yield_scale` read by `world_q.season_factor_of`, and `build_realm(tensions=True)`.

The file ships `tensions: []`, so every test below PLANTS its registry (`tensions.parse`, `tensions.cards_replaced`) and reads the real realm.

THE FALSIFIERS, each with the failure it would show:
  * FOUR REFUSALS, each by its own message and one mutation of one valid card: (i) a `fires_at` key, (ii) an effect kind off the roster, (iii) a goal
    row `data/goals.py::parse` rejects, refused with goals' own law string (one validator, not a second), (iv) a goal id `goals.yaml` already carries;
  * KEYED: the same seed twice draws the same card and the same `choose_one` picks, seeds 0-5 do not all pick alike, and a card with no effects is the
    realm it was (`content_hash`);
  * MINTED: the card's goal Propositions exist and at least one person commits to each (the count checked is asserted, so an empty loop fails);
  * SCALED: a scaled territory's factor is its unscaled factor times the scale, an unscaled territory's is untouched -- on the drawn arm and on the
    control arm, where `season_factors_by_rung` once read ONE factor for every rung.
"""
from __future__ import annotations

import copy

import pytest

from ..boot.realm import build_realm, draw_tension
from ..data import goals as goals_data
from ..data import tensions
from ..data.rosters import territory_rung_id
from ..gaps import Forbidden, Unspecified
from ..queries import world_q


def _goal(gid: str = "goal_plant", **more) -> dict:
    return {"id": gid, "org": {"faction": {"choose_one": ["Varfell", "Hafenmark"]}}, "text": "the plant holds",
            "object": {"kind": "seat_holders", "seats": [{"choose_one": ["off_king", "off_heir", "off_widow_regent"]}]},
            "stance": -1, "pursuits": {"stability": 1}, "source": "test_tensions [ASSUMPTION]", **more}


def _card(effects, cid: str = "tension_plant", **more) -> dict:
    return {"id": cid, "text": "a planted strain", "source": "test_tensions [ASSUMPTION]", "effects": effects, **more}


def _plant() -> dict:
    """A valid card: one goal row with two `choose_one` lists and one scale on T4."""
    return _card([{"kind": "goal", "goal": _goal()}, {"kind": "yield_scale", "territory": "T4", "scale": 0.75}])


def _load(card: dict) -> tuple:
    return tensions.parse({"tensions": [card]})


def _built(seed: int, card: dict, **kw):
    with tensions.cards_replaced(_load(card)):
        return build_realm(seed, tensions=True, **kw)


def test_the_loader_refuses_a_firing_key_a_foreign_effect_a_goal_goals_refuses_and_a_colliding_id():
    assert len(_load(_plant())) == 1, "control: the unmutated card loads"
    fires = {**_plant(), "fires_at": 3}
    with pytest.raises(Forbidden, match=r"tension 'tension_plant'.*fires_at"):                        # (i)
        _load(fires)
    foreign = _card([{"kind": "curse", "goal": _goal()}])
    with pytest.raises(Unspecified, match=r"tension 'tension_plant': effect kind 'curse' is not rostered"):  # (ii)
        _load(foreign)
    bare = _goal()
    bare["pursuits"] = {}
    with pytest.raises(Unspecified, match=r"carries no `pursuits:`") as own:                           # (iii)
        _load(_card([{"kind": "goal", "goal": bare}]))
    assert own.value.law == goals_data._LAW, "the refusal is goals' own, not a second validator's"
    taken = next(iter(goals_data.goals())).id
    with pytest.raises(Forbidden, match=r"more than one row carries this id") as dup:                  # (iv)
        _load(_card([{"kind": "goal", "goal": _goal(taken)}]))
    assert taken in str(dup.value)


def test_the_same_seed_draws_the_same_picks_and_seeds_do_not_all_pick_alike():
    card = _plant()
    with tensions.cards_replaced(_load(card)):
        drawn = [draw_tension(s) for s in range(6)]
        again = [draw_tension(s) for s in range(6)]
    assert drawn == again, "a draw is a function of the seed"
    picks = {(d.goals[0].org, tuple(d.goals[0].object["seats"])) for d in drawn}
    assert len(picks) >= 2, picks                                                                      # the lists are not constants
    assert {d.card for d in drawn} == {"tension_plant"}
    empty = _card([])
    assert _built(0, empty).content_hash() == build_realm(0).content_hash(), "an effectless card is the identity"
    assert _built(1, card).content_hash() == _built(1, card).content_hash()


def test_the_cards_goals_are_minted_and_at_least_one_person_commits_to_each():
    checked = 0
    for seed in range(6):
        w = _built(seed, _plant())
        with tensions.cards_replaced(_load(_plant())):
            d = draw_tension(seed)
        for g in d.goals:
            committed = [t for t in w.tenures if t.kind == "commit" and t.object == g.id]
            assert g.id in w.propositions and committed, (seed, g.id)
            checked += 1
    assert checked == 6, "the loop checked one goal row at each of six seeds"
    assert "goal_plant" not in build_realm(0).propositions, "the switch off mints nothing"


def test_a_scaled_territory_reads_base_times_scale_and_an_unscaled_one_its_base():
    t4, t1 = territory_rung_id("T4"), territory_rung_id("T1")
    plain = build_realm(0)
    scaled = _built(0, _plant())
    assert dict(scaled.fixtures.get("territory_yield_scale")) == {t4: 0.75}
    assert plain.fixtures.get("territory_yield_scale") == (), "the shared default is never mutated"
    for arm in ("drawn", "control"):
        for w in (plain, scaled):
            if arm == "control":
                w.fixtures = w.fixtures.sweep("season_factor_draw", ())
        for tick in range(4):
            plain.tick = scaled.tick = tick
            base = world_q.season_factor_of(plain, t4)
            assert world_q.season_factor_of(scaled, t4) == base * 0.75, (arm, tick)
            assert world_q.season_factor_of(scaled, t1) == world_q.season_factor_of(plain, t1), (arm, tick)
        assert world_q.season_factor_of(scaled, None) == world_q.season_factor_of(plain, None), "no territory reads 1.0"
        by_rung_p, by_rung_s = dict(world_q.season_factors_by_rung(plain)), dict(world_q.season_factors_by_rung(scaled))
        under = [r for r in by_rung_s if world_q.enclosing_territory(scaled, r) == t4]
        assert under and all(by_rung_s[r] == by_rung_p[r] * 0.75 for r in under), arm
        assert all(by_rung_s[r] == by_rung_p[r] for r in by_rung_s if r not in under), arm
