"""B12b.45 (CL-EVENTS commit (3)) -- THE TENSIONS RECEIVER: `engine/season/tensions.yaml`, its one loader `data/tensions.py`, the closed roster
`rosters.yaml: tension_effects`, `Fixtures territory_yield_scale` read by `world_q.season_factor_of`, and `build_realm(tensions=True)`.

The B12b.45 tests PLANT their registry (`tensions.parse`, `tensions.cards_replaced`) and read the real realm; the B12b.46 tests at the foot read the
six shipped cards (`tensions.yaml`, `[ASSUMPTION]` content) as the realm draws them.

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
import yaml

from ..boot.realm import build_realm, draw_tension, seed_goals
from ..data import goals as goals_data
from ..data import tensions
from ..data.rosters import territory_rung_id
from ..decision import assemble
from ..decision.options import opening_set
from ..gaps import Forbidden, Unspecified
from ..harness.populated import run
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


# ---------------------------------------------------------------------------------------------------------------------------------------
# B12b.46 (CL-EVENTS commit (4)): THE SHIPPED DECK -- six `[ASSUMPTION]` cards in tensions.yaml, read here as the realm reads them.
# ---------------------------------------------------------------------------------------------------------------------------------------

SHIPPED = ("tension_royal_crisis", "tension_feldmark_famine", "tension_cardinal_independence", "tension_guild_fracture",
           "tension_einhir_incident", "tension_ministry_crisis")


def _object_of(w, goal) -> set:
    """WHAT A GOAL'S `object:` IS IN THIS WORLD, read from the World (never from `world_q.goal_referents`, the reader under test): a `rung`
    goal's rung; a `seat_holders` goal's live holders of its listed seats (persons, never a seat's id: `goal_referents`' contract)."""
    if goal.object["kind"] == "rung":
        return {goal.object["rung"]}
    seats = set(goal.object["seats"])
    return {t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object in seats and t.subject in w.persons}


def _formed_on_object(w, goal) -> int:
    """How many committed persons form, on the goal's OWN question (`q.about` is the goal), a candidate whose subject is the goal's object."""
    obj, n = _object_of(w, goal), 0
    for pid in sorted(t.subject for t in w.tenures if t.kind == "commit" and t.live and t.object == goal.id):
        p = w.persons[pid]
        n += any(c.subject in obj for q in world_q.questions_for(w, p) if q.about == goal.id
                 for c in opening_set(p, assemble(p, q, 12), q, w.fixtures))
    return n


def test_the_shipped_deck_seeds_at_six_seeds_and_a_committed_person_forms_a_candidate_on_its_goals_object():
    """Switch on, seeds 0-5, two seasons (A-114): every card of the shipped deck loads; the drawn card's goals are minted, committed to and its
    scales swept in; on the realm the first season deliberates over, at least one committed person forms on the goal's own question a candidate
    whose subject is the goal's object (counted per seed, so a vacuous loop fails); and the realm plays two seasons. The candidate is read at the
    opening, not after the run: a seat goal binds its holder at seeding, and the holder may be dead by the second season (seed 2's Comptroller
    falls in a duel in the first), which is the world playing, not the card failing."""
    assert tuple(c.id for c in tensions.cards()) == SHIPPED, "the six cards load from the shipped file"
    for seed in range(6):
        d = draw_tension(seed)
        w = build_realm(seed, tensions=True)
        assert dict(w.fixtures.get("territory_yield_scale")) == dict(d.yield_scale), (seed, d.card)
        for g in d.goals:
            assert g.id in w.propositions and any(t.kind == "commit" and t.live and t.object == g.id for t in w.tenures), (seed, g.id)
        checked = sum(_formed_on_object(w, g) > 0 for g in d.goals)
        assert checked >= 1, (seed, d.card, "no committed person formed a candidate on the goal's object")
        run(2, seed, w=w)
        assert w.tick == 2, (seed, w.tick)


def test_a_card_naming_a_seat_offices_lacks_is_refused_and_a_vacant_seat_seeds_its_goal_with_no_stance_row(monkeypatch, tmp_path):
    """PLANTED: a card whose `seat_holders` object names a seat absent from offices.yaml is refused when the realm draws it, naming the row; the
    shipped Ministry card seeded onto the realm with its seat built but vacant mints the goal and its commit and writes no stance row, where the
    same card with the seat held writes one (the control: the vacancy is what removed the row)."""
    absent = _goal("goal_plant_absent")
    absent["object"] = {"kind": "seat_holders", "seats": ["off_absent"]}
    path = tmp_path / "tensions.yaml"
    path.write_text(yaml.safe_dump({"tensions": [_card([{"kind": "goal", "goal": absent}])]}), encoding="utf-8")
    monkeypatch.setattr(tensions, "TENSIONS_YAML", path)
    with tensions.cards_replaced(None), pytest.raises(Unspecified, match=r"goal 'goal_plant_absent': seat 'off_absent' is not on offices"):
        build_realm(0, tensions=True)

    ministry = next(c for c in tensions.cards() if c.id == "tension_ministry_crisis")
    rows = tensions.resolve(ministry, lambda cid, i, options: options[0]).goals
    seat = rows[0].object["seats"][0]
    stance_rows = {}
    for arm in ("held", "vacant"):
        w = build_realm(0, goals=False)
        if arm == "vacant":
            for t in w.tenures:
                if t.kind == "hold" and t.live and t.object == seat:
                    t.until = w.tick
        cid_of = {pid: "NPC-" + pid.rsplit("_", 1)[1] for pid in w.persons if pid.startswith("p_npc_")}
        census = seed_goals(w, rows, w._office_census["authored"], cid_of, complete=False)
        assert rows[0].id in w.propositions and census["commits"] >= 1, arm
        stance_rows[arm] = census["stance_rows"]
    assert stance_rows["held"] >= 1 and stance_rows["vacant"] == 0, stance_rows
