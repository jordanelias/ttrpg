"""v9 FA-06 -- EVERY OTHER ORGANIZATION'S GOALS, AND THE COMPLETENESS REFUSAL AT SEEDING.

CARRIER: `engine/season/goals.yaml` (FA-05's nine rows plus FA-06's), the loader `data/goals.py` and the
seeding `harness/populated.py::seed_goals`, whose `complete` switch (`build_realm(goals_complete=)`, `True` by
default) refuses a world that seats an organization no row is about.

THE FALSIFIERS, each with the failure it would show:
  (a) the shipped file is COMPLETE: every faction with an authored head and every body with a seated
      member holds a row (`goals_missing(...) == []`), and the default build accepts it. CONTROL: the same
      reading over a file with one row deleted lists exactly that organization;
  (b) THE REFUSAL ITSELF: a body with a seated member and no goal -> `build_realm(0)` raises `Unspecified`
      naming the body; likewise a faction with an authored head. CONTROL: the same partial file builds under
      `goals_complete=False`, and the control arm (`goals=False`) never asks. MUTATION (run): `seed_goals`
      without its `if complete:` block turns (b) red and nothing else in this file;
  (c) the Nine Political Axes as data: the rival goals carry `stance -1` toward the rival head's seat, and a
      member of the faction takes a stance row against that head;
  (d) `establishes`: the Inquisitors hold the narrower heresy goal and not the Church's, every other Church
      member the Church's;
  (e) provenance: a row that names a quarantined design document carries the word "intent" and an
      [ASSUMPTION] tag (a reader's discipline made visible here, never a gate on the file).
"""
from __future__ import annotations

import pytest
import yaml

from ..data import cast, files, goals
from ..gaps import Unspecified
from ..harness import populated as P

CHURCH_HERESY = "goal_church_root_out_heresy"
INQ = "goal_inquisitors_find_heresy"
HAFEN_VS_CHURCH = "goal_hafenmark_church_influence_suppressed"
CHURCH_VS_RESTORATION = "goal_church_suppress_restoration"
QUARANTINED = ("faction_state_authoring_v30", "faction_canon_v30", "faction_behavior_v30", "worldbuilding_v30")


def _shipped_rows() -> list:
    return yaml.safe_load(files.GOALS_YAML.read_text(encoding="utf-8"))["goals"]


def _plant(monkeypatch, tmp_path, rows):
    path = tmp_path / "goals.yaml"
    path.write_text(yaml.safe_dump({"goals": list(rows)}, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr(goals, "GOALS_YAML", path)
    monkeypatch.setattr(goals, "_CACHE", None)


@pytest.fixture(scope="module")
def shipped():
    return P.build_realm(0)


def _committed(w, gid) -> set:
    return {t.subject for t in w.tenures if t.kind == "commit" and t.object == gid and t.live}


# ---------------------------------------------------------------------------------------------------
# (a) the shipped file is complete
# ---------------------------------------------------------------------------------------------------

def test_fa06_the_shipped_file_covers_every_seated_organization(shipped):
    assert P.goals_missing(shipped, goals.goals()) == []
    heads = [f for f in P.FACTIONS if cast.faction_leader(f) and f"p_{P._slug(cast.faction_leader(f))}" in shipped.persons]
    bodies = {o.body for o in shipped.offices.values() if o.body
              and any(t.kind == "hold" and t.live and t.object == oid for t in shipped.tenures
                      for oid in [o.id])}
    assert len(heads) >= 6 and len(bodies) >= 10, "control: the reading finds the organizations it should"
    have = {(g.org_kind, g.org) for g in goals.goals()}
    assert all(("faction", f) in have for f in heads) and all(("body", b) in have for b in bodies)
    c = P.census(shipped)
    assert (c["goals"], c["goal_orientation"], c["goal_dropped"]) == (12, 23, 0)


@pytest.mark.parametrize("gone, named", [
    ("goal_guild_masters_trade", "body 'Guild'"),
    ("goal_varfell_southernmost_dominion", "faction 'Varfell'"),
])
def test_fa06_the_reading_lists_exactly_the_organization_a_deleted_row_leaves_bare(
        monkeypatch, tmp_path, shipped, gone, named):
    rows = [r for r in _shipped_rows() if r["id"] != gone]
    if gone == "goal_varfell_southernmost_dominion":     # Varfell holds three rows; delete them all
        rows = [r for r in rows if r["org"] != {"faction": "Varfell"}]
    _plant(monkeypatch, tmp_path, rows)
    assert P.goals_missing(shipped, goals.goals()) == [named]


# ---------------------------------------------------------------------------------------------------
# (b) the refusal, at seeding
# ---------------------------------------------------------------------------------------------------

def test_fa06_a_body_with_a_seated_member_and_no_goal_refuses_seeding_naming_it(monkeypatch, tmp_path):
    rows = [r for r in _shipped_rows() if r["org"] != {"body": "Guild"}]
    assert len(rows) == len(_shipped_rows()) - 1, "control: exactly the Guild body's row is deleted"
    _plant(monkeypatch, tmp_path, rows)
    with pytest.raises(Unspecified) as exc:
        P.build_realm(0)
    assert "body 'Guild'" in exc.value.what and exc.value.what.count("body ") == 1 and "faction " not in exc.value.what
    # CONTROL: the same partial file builds when the switch is off, and the control arm never asks
    assert P.build_realm(0, goals_complete=False)._goal_census["goals"] > 0
    assert P.build_realm(0, goals=False)._goal_census["goals"] == 0


def test_fa06_a_faction_with_an_authored_head_and_no_goal_refuses_seeding_naming_it(monkeypatch, tmp_path):
    rows = [r for r in _shipped_rows() if r["org"] != {"faction": "Hafenmark"}]
    _plant(monkeypatch, tmp_path, rows)
    with pytest.raises(Unspecified) as exc:
        P.build_realm(0)
    assert "faction 'Hafenmark'" in exc.value.what and "body " not in exc.value.what
    # a bodyless, headless organization (Guilds' head is none) is asked for nothing at the faction level
    assert cast.faction_leader("Guilds") is None
    rows = [r for r in _shipped_rows() if r["org"] != {"faction": "Guilds"}]
    _plant(monkeypatch, tmp_path, rows)
    assert P.build_realm(0)._goal_census["goals"] > 0, "no authored head: no faction row is required"


def test_fa06_an_empty_file_refuses_and_names_every_seated_organization(monkeypatch, tmp_path, shipped):
    _plant(monkeypatch, tmp_path, [])
    with pytest.raises(Unspecified) as exc:
        P.build_realm(0)
    for name in ("faction 'Crown'", "faction 'Restoration Movement'", "body 'Riskbreakers'", "body 'Holy See'"):
        assert name in exc.value.what, name


# ---------------------------------------------------------------------------------------------------
# (c) rivals, the Nine Political Axes as data
# ---------------------------------------------------------------------------------------------------

def test_fa06_rival_goals_carry_stance_minus_one_toward_the_rival_heads_seat(shipped):
    byid = {g.id: g for g in goals.goals()}
    for gid, seat, org in ((HAFEN_VS_CHURCH, "off_confessor", "Hafenmark"),
                           (CHURCH_VS_RESTORATION, "off_restoration_leader", "Church of Solmund")):
        g = byid[gid]
        assert (g.org_kind, g.org, g.stance) == ("faction", org, -1), gid
        assert g.object == {"kind": "seat_holders", "seats": [seat]}, gid
    # a Hafenmark member takes a stance row against the Confessor (p_npc_021) and a Church member one
    # against the Restoration leader (p_npc_003): the creed's own call, negated
    assert any(ref == "p_npc_021" for p in shipped.persons.values() for ref, _, _ in p.stance
               if p.id in _committed(shipped, HAFEN_VS_CHURCH))
    assert any(ref == "p_npc_003" for p in shipped.persons.values() for ref, _, _ in p.stance
               if p.id in _committed(shipped, CHURCH_VS_RESTORATION))


# ---------------------------------------------------------------------------------------------------
# (d) `establishes`: the Inquisitors' goal replaces the Church's for them
# ---------------------------------------------------------------------------------------------------

def test_fa06_the_inquisitors_hold_the_narrower_heresy_goal_and_the_rest_of_the_church_the_broader(shipped):
    inquisitors = _committed(shipped, INQ)
    assert inquisitors == {"p_npc_004", "p_npc_038"}
    church = _committed(shipped, CHURCH_HERESY)
    assert church and not (church & inquisitors), "establishes: the parent is off the child org's persons"
    assert "p_npc_021" in church, "the Confessor, the Church's head, holds the broader goal"


# ---------------------------------------------------------------------------------------------------
# (e) provenance
# ---------------------------------------------------------------------------------------------------

def test_fa06_a_row_naming_a_quarantined_document_says_intent_and_tags_its_assumption():
    cited = [g for g in goals.goals() if any(q in g.source for q in QUARANTINED)]
    assert len(cited) >= 20, "control: FA-06's rows cite the sources"
    for g in cited:
        assert "intent" in g.source.lower(), g.id
        assert "ASSUMPTION" in g.source, g.id
        assert g.pursuits and g.text.strip(), g.id
