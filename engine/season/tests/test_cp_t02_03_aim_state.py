"""CP-T02-03 (B10-09; v10 AM-B-09) -- AN AMBITION CAN BE MET: `world_q.aim_state`, RUNG GOALS ONLY.

`aim_state(w, p, prop) -> "open" | "met"`; the `aim:` column of `rosters.yaml: goal_object_kinds` keeps its `rung`
row alone (`met` when the rung's `governing_hold` is held by a person committed to the goal's organization's
faction); Q4 (`questions_for`) forms no `need` for a `met` goal. What each test proves, and the failure it can
observe:

  (a) two hand-built worlds through the REAL Q4: a `rung` goal whose rung the org's member holds forms NO `need`; the
      same world with the rung lost (the hold ended; or held by a member of another faction) forms it. A rule that
      reads `open` always reddens the first (MUTATION, run below).
  (b) a kind with no row never reads `met`: the same holder on a `seat_holders` goal does not suppress its `need`.
  (c) MUTATION: the `aim:` column dropped from the roster, and the loader refuses (`Unspecified`, naming the column).
  (d) the shipped roster gives no kind but `rung` a row (the item's Must-not).
"""
from __future__ import annotations

import copy

import pytest
import yaml

from ..data import goals
from ..data import rosters
from ..data.rosters import roster_map
from ..gaps import Unspecified
from ..queries import world_q
from ..state.carriers import Person, Proposition, Tenure
from ..state.world import World

RUNG = "terr_T13"
SEAT = "off_king"
VARFELL = {"faction": "Varfell"}


def _row(gid, obj):
    return {"id": gid, "org": VARFELL, "text": f"{gid}, as a predicate", "object": obj,
            "pursuits": {"stability": 1}, "source": "test_cp_t02_03"}


def _plant(monkeypatch, tmp_path, *rows):
    path = tmp_path / "goals.yaml"
    path.write_text(yaml.safe_dump({"goals": list(rows)}, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr(goals, "GOALS_YAML", path)
    monkeypatch.setattr(goals, "_CACHE", None)


def _world(gid, *, holder_faction="fac_varfell", lost=False, obj=RUNG):
    """An observer committed to the OUGHT `gid`; `p_h` a member of `holder_faction` who holds `obj` (the hold ended
    at tick 1 when `lost`). The Proposition's id IS the goal's id (`data/goals.py`)."""
    w = World(0)
    w.propositions[gid] = Proposition(gid, "OUGHT", RUNG, f"{gid} ought", True, 0)
    obs, holder = Person("p_obs", "p_obs"), Person("p_h", "p_h")
    obs.tenures.append(Tenure("t_obs_commit", "p_obs", gid, "commit", 0))
    holder.tenures.append(Tenure("t_h_commit", "p_h", holder_faction, "commit", 0))
    holder.tenures.append(Tenure("t_h_hold", "p_h", obj, "hold", 0, 1 if lost else None))
    w.persons["p_obs"], w.persons["p_h"] = obs, holder
    return w, obs


def _need(w, obs) -> dict:
    return {q.about: q.referents for q in world_q.questions_for(w, obs) if q.source == "need"}


def _rung_goal(monkeypatch, tmp_path):
    _plant(monkeypatch, tmp_path, _row("g_rung", {"kind": "rung", "rung": RUNG}))


# ------------------------------------------------------------------------------------------------ (a)

def test_cp_t02_03_a_rung_its_org_holds_forms_no_need_and_the_same_world_with_it_lost_forms_it(
        monkeypatch, tmp_path):
    _rung_goal(monkeypatch, tmp_path)
    met, obs = _world("g_rung")
    assert world_q.aim_state(met, obs, met.propositions["g_rung"]) == "met"
    assert _need(met, obs) == {}, "the org's member holds the rung: the aim is met and asks for nothing"

    for lost, why in ((_world("g_rung", lost=True), "the hold ended"),
                      (_world("g_rung", holder_faction="fac_crown"), "held by another faction's member")):
        w, o = lost
        assert world_q.aim_state(w, o, w.propositions["g_rung"]) == "open", why
        assert _need(w, o) == {"g_rung": (RUNG,)}, f"{why}: the same goal forms its question again"


def test_cp_t02_03_mutation_an_aim_state_reading_open_always_reddens_the_met_world(monkeypatch, tmp_path):
    """The falsifier must be able to observe the failure it excludes: with the rule dead, (a)'s first assertion fails."""
    _rung_goal(monkeypatch, tmp_path)
    met, obs = _world("g_rung")
    monkeypatch.setattr(world_q, "aim_state", lambda w, p, prop: "open")
    with pytest.raises(AssertionError):
        assert _need(met, obs) == {}
    assert _need(met, obs) == {"g_rung": (RUNG,)}, "and it is the aim state alone that was suppressing it"


def test_cp_t02_03_a_holder_committed_to_two_factions_does_not_meet_it(monkeypatch, tmp_path):
    """A holder committed to the org's faction AND another reads `faction_holding` None: not met, not guessed."""
    _rung_goal(monkeypatch, tmp_path)
    w, obs = _world("g_rung")
    w.persons["p_h"].tenures.append(Tenure("t_h_commit2", "p_h", "fac_crown", "commit", 0))
    assert world_q.aim_state(w, obs, w.propositions["g_rung"]) == "open"
    assert set(_need(w, obs)) == {"g_rung"}


# ------------------------------------------------------------------------------------------------ (b)

def test_cp_t02_03_a_kind_with_no_row_is_never_met_though_its_seat_is_held_by_the_orgs_member(
        monkeypatch, tmp_path):
    _plant(monkeypatch, tmp_path, _row("g_king", {"kind": "seat_holders", "seats": [SEAT]}))
    w, obs = _world("g_king", obj=SEAT)
    assert world_q.aim_state(w, obs, w.propositions["g_king"]) == "open"
    assert _need(w, obs) == {"g_king": ("p_h",)}, "the throne's holder is a referent; no aim row, no suppression"
    w.propositions["o_plain"] = Proposition("o_plain", "OUGHT", "p_h", "a want", True, 0)
    assert world_q.aim_state(w, obs, w.propositions["o_plain"]) == "open", "a Proposition no goal names is open"


# ------------------------------------------------------------------------------------------------ (c)

def test_cp_t02_03_mutation_dropping_the_aim_column_makes_the_loader_refuse(monkeypatch):
    doc = {"goals": [_row("g_rung", {"kind": "rung", "rung": RUNG})]}
    assert [g.id for g in goals.parse(doc)] == ["g_rung"], "control: the shipped roster loads the row"
    row = copy.deepcopy(rosters._ROSTERS["goal_object_kinds"])
    del row["aim"]
    monkeypatch.setitem(rosters._ROSTERS, "goal_object_kinds", row)
    with pytest.raises(Unspecified, match="aim"):
        goals.parse(doc)


def test_cp_t02_03_the_loader_refuses_an_aim_row_for_no_kind(monkeypatch):
    row = copy.deepcopy(rosters._ROSTERS["goal_object_kinds"])
    row["aim"]["sixth_kind"] = "held_by_org_member"
    monkeypatch.setitem(rosters._ROSTERS, "goal_object_kinds", row)
    with pytest.raises(Unspecified, match="sixth_kind"):
        goals.parse({"goals": []})


def test_cp_t02_03_an_aim_row_naming_no_rule_refuses_when_asked(monkeypatch, tmp_path):
    _rung_goal(monkeypatch, tmp_path)
    row = copy.deepcopy(rosters._ROSTERS["goal_object_kinds"])
    row["aim"]["rung"] = "no_such_rule"
    monkeypatch.setitem(rosters._ROSTERS, "goal_object_kinds", row)
    w, obs = _world("g_rung")
    with pytest.raises(Unspecified, match="no_such_rule"):
        world_q.aim_state(w, obs, w.propositions["g_rung"])


# ------------------------------------------------------------------------------------------------ (d)

def test_cp_t02_03_the_shipped_roster_gives_rung_the_only_row():
    assert list(roster_map("goal_object_kinds", "aim")) == ["rung"]
