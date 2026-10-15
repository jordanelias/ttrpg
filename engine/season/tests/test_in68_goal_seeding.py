"""v9 IN-68 (`workplans/valoria_master_workplan_v9_part5.md`, A-32; ED-IN-0293 (8), (10)) -- GOALS REACH
PERSONS: `harness/populated.py::seed_goals` mints each `goals.yaml` row as an OUGHT Proposition at
world-gen and the org's persons `commit` to it.

Hand-built goals files are planted through `goals.GOALS_YAML` and the loader's `_CACHE`, as
`test_in66_goals_loader.py` and `test_in67_goal_referents.py` do, and the realm is the real one
(`build_realm(0)`: Crown's eleven members, the Inner Circle's two seats, the spymaster's one). What each
test proves, and the failure it can observe:

  (a) a FACTION goal reaches the faction's members AND its head (a head who is no member is planted by
      rebinding `cast.faction_leader`); a BODY goal the holders of the seats whose `Office.body` it is
      and nobody else in the faction; a SEAT goal its holder and no other holder (the same body's).
  (b) `establishes` takes the parent goal off every person of the child's org and `influences` leaves
      both; the child's own commits stand either way, and persons outside the child org keep the parent.
  (c) an `orientation` row mints no Proposition and no commit, and is counted.
  (d) the stance row is `cast.stance_from_loyalty` of the member's loyalty to the org's faction, signed
      by the goal's `stance` -- a Crown member below indifference inverts it; a faction with no template
      writes none; a `rung` or `deed_doers` referent is no person at seeding and writes none.
  (e) an unknown rung REFUSES (a known one mints); a goal id already a Proposition refuses; a cap that
      drops the person or the seats drops the goal, counted.
  (f) `goals=False` mints nothing though the file names goals, and the shipped (empty) file builds the
      same realm, hash and census as the control arm.
"""
from __future__ import annotations

import pytest
import yaml

from ..data import cast, goals
from ..data.rosters import faction_prop_id
from ..gaps import Forbidden, Unspecified
from ..harness import populated as P
from ..queries.world_q import members

CROWN = {"faction": "Crown"}
CIRCLE = {"body": "Inner Circle"}
SPY = {"seat": "off_spymaster"}
HEIR = "p_npc_031"
KING = "p_npc_020"
CIRCLE_HOLDERS = {"p_npc_036", "p_npc_037"}      # off_royal_marshal, off_lord_treasurer: Inner Circle
SPYMASTER = "p_npc_033"                          # Crown, no body


def _row(gid, org, obj, **kw):
    row = {"id": gid, "org": org, "text": f"{gid}, as a predicate", "object": obj,
           "pursuits": {"stability": 1}, "source": "test_in68"}
    row.update(kw)
    return row


def _heir(gid="g_heir", **kw):
    return _row(gid, CROWN, {"kind": "person", "case": "NPC-031"}, **kw)


def _king(gid="g_king", org=CIRCLE, **kw):
    return _row(gid, org, {"kind": "seat_holders", "seats": ["off_king"]}, **kw)


def _realm(monkeypatch, tmp_path, *rows, **kw):
    """`build_realm(0, **kw)` over a hand-built goals file, planted through the loader's patch point."""
    path = tmp_path / "goals.yaml"
    path.write_text(yaml.safe_dump({"goals": list(rows)}, allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr(goals, "GOALS_YAML", path)
    monkeypatch.setattr(goals, "_CACHE", None)
    return P.build_realm(0, **kw)


def _committed(w, gid) -> set:
    return {t.subject for t in w.tenures if t.kind == "commit" and t.object == gid and t.live}


def _stance_of(w, pid) -> list:
    return list(w.persons[pid].stance)


def _expected(pid, faction, referent, sign):
    """The row a member of `faction` takes: the creed's own call on the member's loyalty, signed."""
    st = cast.stance_from_loyalty(cast.loyalty(cast.row("NPC-" + pid.rsplit("_", 1)[1]), faction))
    return None if st is None else (referent, sign * st[0], st[1])


# ---------------------------------------------------------------------------------------------------
# (a) who commits: faction -> members and head; body -> its seats' holders; seat -> its holder
# ---------------------------------------------------------------------------------------------------

def test_in68_a_faction_goal_reaches_its_members_and_its_head(monkeypatch, tmp_path):
    w = _realm(monkeypatch, tmp_path, _heir())
    crown = set(members(w, faction_prop_id("Crown")))
    prop = w.propositions["g_heir"]
    assert (prop.mood, prop.subject, prop.predicate, prop.value, prop.when) == \
        ("OUGHT", HEIR, "g_heir, as a predicate", "Crown", 0)
    assert len(crown) > 5 and _committed(w, "g_heir") == crown, "every member, and no one else"
    # the head who is no member: planted by rebinding the owner of "who heads this faction"
    real = cast.faction_leader
    monkeypatch.setattr(cast, "faction_leader", lambda f: "NPC-040" if f == "Crown" else real(f))
    w2 = P.build_realm(0)
    assert "p_npc_040" not in members(w2, faction_prop_id("Crown")), "control: the head is no member"
    assert _committed(w2, "g_heir") == set(members(w2, faction_prop_id("Crown"))) | {"p_npc_040"}


def test_in68_a_body_goal_reaches_the_holders_of_the_seats_in_the_body_and_no_one_else(
        monkeypatch, tmp_path):
    w = _realm(monkeypatch, tmp_path, _king())
    crown = set(members(w, faction_prop_id("Crown")))
    assert CIRCLE_HOLDERS <= crown and SPYMASTER in crown, "control: the faction holds more than the body"
    assert _committed(w, "g_king") == CIRCLE_HOLDERS
    prop = w.propositions["g_king"]
    assert prop.subject == "off_npc_020", "the first seat's OFFICE (offices.yaml's `off_king` is seated as this)"
    assert prop.value == "Inner Circle"


def test_in68_a_seat_goal_reaches_its_holder_and_not_another_holder_of_the_body(monkeypatch, tmp_path):
    w = _realm(monkeypatch, tmp_path,
               _row("g_spy", SPY, {"kind": "person", "case": "NPC-031"}),
               _row("g_marshal", {"seat": "off_royal_marshal"}, {"kind": "person", "case": "NPC-031"}))
    assert _committed(w, "g_spy") == {SPYMASTER}
    assert _committed(w, "g_marshal") == {"p_npc_036"}, "not the treasurer, who sits in the same body"
    assert w._goal_census["commits"] == 2


# ---------------------------------------------------------------------------------------------------
# (b) derives: establishes replaces, influences keeps both
# ---------------------------------------------------------------------------------------------------

def _derived(kind):
    return [_heir(), _king(derives={"from": "g_heir", "kind": kind})]


def test_in68_establishes_takes_the_parent_goal_off_the_child_orgs_members(monkeypatch, tmp_path):
    w = _realm(monkeypatch, tmp_path, *_derived("establishes"))
    crown = set(members(w, faction_prop_id("Crown")))
    assert _committed(w, "g_king") == CIRCLE_HOLDERS, "the child's own commits stand"
    assert not CIRCLE_HOLDERS & _committed(w, "g_heir"), "the child org's members do not commit to the parent"
    assert _committed(w, "g_heir") == crown - CIRCLE_HOLDERS, "and no one else loses it"
    assert SPYMASTER in _committed(w, "g_heir")


def test_in68_influences_leaves_the_child_orgs_members_committed_to_both(monkeypatch, tmp_path):
    w = _realm(monkeypatch, tmp_path, *_derived("influences"))
    crown = set(members(w, faction_prop_id("Crown")))
    assert _committed(w, "g_king") == CIRCLE_HOLDERS
    assert _committed(w, "g_heir") == crown, "the parent keeps every member"
    assert CIRCLE_HOLDERS <= _committed(w, "g_heir") & _committed(w, "g_king")


# ---------------------------------------------------------------------------------------------------
# (c) orientation mints nothing
# ---------------------------------------------------------------------------------------------------

def test_in68_an_orientation_row_mints_no_proposition_and_no_commit_and_is_counted(monkeypatch, tmp_path):
    base = P.build_realm(0, goals=False)
    w = _realm(monkeypatch, tmp_path, _row("g_calm", CROWN, {"kind": "orientation"}, stance=1))
    assert "g_calm" not in w.propositions and not _committed(w, "g_calm")
    assert len(w.propositions) == len(base.propositions), "an OUGHT about nobody is not a motive"
    assert sum(len(p.tenures) for p in w.persons.values()) == sum(len(p.tenures) for p in base.persons.values())
    assert w.content_hash() == base.content_hash(), "the world cannot tell the file from none"
    c = P.census(w)
    assert (c["goal_orientation"], c["goals"], c["goal_commits"], c["goal_stance_rows"]) == (1, 0, 0, 0)
    # an orientation CHILD still takes the parent off its org (`establishes` is about the org's persons)
    w2 = _realm(monkeypatch, tmp_path, _heir(),
                _row("g_calm", CIRCLE, {"kind": "orientation"}, derives={"from": "g_heir", "kind": "establishes"}))
    assert not CIRCLE_HOLDERS & _committed(w2, "g_heir") and "g_calm" not in w2.propositions


# ---------------------------------------------------------------------------------------------------
# (d) the stance row
# ---------------------------------------------------------------------------------------------------

def test_in68_the_stance_row_is_the_creeds_loyalty_rule_signed_by_the_goals_stance(monkeypatch, tmp_path):
    base = P.build_realm(0, goals=False)
    checked, opposed = 0, 0
    for sign in (1, -1):
        w = _realm(monkeypatch, tmp_path, _heir(stance=sign))
        for pid in sorted(_committed(w, "g_heir")):
            added = _stance_of(w, pid)[len(_stance_of(base, pid)):]
            assert _stance_of(w, pid)[:len(_stance_of(base, pid))] == _stance_of(base, pid), "the creed's rows stand"
            want = _expected(pid, "Crown", HEIR, sign)
            assert added == [want], (pid, added, want)
            checked += 1
            opposed += want[1] != sign
    assert checked == 2 * len(_committed(w, "g_heir")) and checked >= 20
    assert opposed >= 2, "control: a Crown member below indifference inverts the sign (once per sign)"
    assert P.census(w)["goal_stance_rows"] == len(_committed(w, "g_heir"))


def test_in68_a_faction_with_no_template_writes_no_stance_row_and_a_row_per_referent_holder(
        monkeypatch, tmp_path):
    w = _realm(monkeypatch, tmp_path,
               _row("g_guild", {"faction": "Guilds"}, {"kind": "person", "case": "NPC-031"}, stance=1),
               _king("g_throne", org=CROWN, stance=1))
    guild = _committed(w, "g_guild")
    assert guild and all(HEIR not in [r[0] for r in w.persons[p].stance] for p in guild), \
        "Guilds has no role template: nothing to be loyal to"
    # `seat_holders`' referent is the holder NOW: one row toward the king per Crown member
    rows = [(p, r) for p in _committed(w, "g_throne") for r in w.persons[p].stance if r[0] == KING]
    assert len({p for p, _ in rows}) == len(_committed(w, "g_throne"))
    assert {r for p, r in rows if p == "p_npc_036"} >= {_expected("p_npc_036", "Crown", KING, 1)}


def test_in68_a_rung_or_deed_referent_is_no_person_at_seeding_and_writes_no_stance_row(
        monkeypatch, tmp_path):
    w = _realm(monkeypatch, tmp_path,
               _row("g_place", CROWN, {"kind": "rung", "rung": "terr_T9"}, stance=1),
               _row("g_doers", CROWN, {"kind": "deed_doers", "kinds": ["person.died"]}, stance=-1))
    assert _committed(w, "g_place") == _committed(w, "g_doers") and len(_committed(w, "g_place")) > 5
    assert w.propositions["g_place"].subject == "terr_T9" and w.propositions["g_doers"].subject == "Crown"
    c = P.census(w)
    assert (c["goals"], c["goal_stance_rows"]) == (2, 0)
    assert c["goal_commits"] == 2 * len(_committed(w, "g_place"))


# ---------------------------------------------------------------------------------------------------
# (e) refusals and the cap
# ---------------------------------------------------------------------------------------------------

def test_in68_an_unknown_rung_refuses_and_a_known_one_mints(monkeypatch, tmp_path):
    with pytest.raises(Unspecified, match="g_nowhere"):
        _realm(monkeypatch, tmp_path, _row("g_nowhere", CROWN, {"kind": "rung", "rung": "terr_T999"}))
    w = _realm(monkeypatch, tmp_path, _row("g_somewhere", CROWN, {"kind": "rung", "rung": "terr_T9"}))
    assert "terr_T9" in w.rungs and w.propositions["g_somewhere"].subject == "terr_T9"


def test_in68_a_goal_id_that_is_already_a_proposition_refuses(monkeypatch, tmp_path):
    with pytest.raises(Forbidden, match="fac_crown"):
        _realm(monkeypatch, tmp_path, _row("fac_crown", CROWN, {"kind": "rung", "rung": "terr_T9"}))


def test_in68_a_cap_that_drops_the_person_or_the_seats_drops_the_goal_and_counts_it(monkeypatch, tmp_path):
    w = _realm(monkeypatch, tmp_path, _heir(), _king(), _row("g_spy", SPY, {"kind": "rung", "rung": "terr_T9"}),
               cap=10)
    assert HEIR not in w.persons and "off_npc_020" not in w.offices, "control: the cap dropped both"
    assert "g_heir" not in w.propositions and "g_king" not in w.propositions
    assert _committed(w, "g_spy") == {SPYMASTER}, "a goal whose referent the cap kept is seeded"
    c = P.census(w)
    assert (c["goal_dropped"], c["goals"]) == (2, 1)
    full = _realm(monkeypatch, tmp_path, _heir(), _king())    # control: the complete cast seeds both
    assert (P.census(full)["goal_dropped"], P.census(full)["goals"]) == (0, 2)


# ---------------------------------------------------------------------------------------------------
# (f) the control arm, and the shipped (empty) file
# ---------------------------------------------------------------------------------------------------

def test_in68_goals_false_mints_nothing_though_the_file_names_goals(monkeypatch, tmp_path):
    rows = [*_derived("establishes"), _heir("g_h2", stance=1)]
    on = _realm(monkeypatch, tmp_path, *rows)
    off = P.build_realm(0, goals=False)
    assert P.census(on)["goals"] == 3 and P.census(on)["goal_commits"] > 0
    assert on.content_hash() != off.content_hash(), "control: the hash observes a seeded goal"
    for gid in ("g_heir", "g_king", "g_h2"):
        assert gid in on.propositions and gid not in off.propositions and not _committed(off, gid)
    c = P.census(off)
    assert (c["goals"], c["goal_orientation"], c["goal_commits"], c["goal_stance_rows"], c["goal_dropped"]) \
        == (0, 0, 0, 0, 0)
    assert len(off.propositions) == len(on.propositions) - 3


def test_in68_the_shipped_empty_goals_file_builds_the_control_arms_realm(monkeypatch):
    assert goals.goals() == (), "control: the shipped file is empty"
    shipped, off = P.build_realm(0), P.build_realm(0, goals=False)
    assert shipped.content_hash() == off.content_hash()
    assert P.census(shipped) == P.census(off)
    assert P.census(shipped)["goals"] == 0 and "goal_commits" in P.census(shipped)


def test_in68_a_seat_holders_goal_reads_the_seat_a_loop_built_realm_built_it_as(monkeypatch, tmp_path):
    """(g) IN-67's reader on the REAL realm. `off_king` is `offices.yaml`'s id; NPC-020's seat is
    loop-built and keeps `off_npc_020`, so a reader matching the listed ids to `Tenure.object` names
    nobody. Seeding records the built Office ids in the Proposition's `scope`. MUTATION (run): seeding
    without the scope turns the first assert red; the control is a hand-built world with no scope, where
    the listed ids are the Office ids."""
    from ..queries import world_q
    w = _realm(monkeypatch, tmp_path, _king())
    seat = w._office_census["authored"]["off_king"]
    assert seat != "off_king" and "off_king" not in w.offices, "the premise: the authored id is no Office"
    prop = w.propositions["g_king"]
    assert prop.scope == (seat,)
    onlooker = w.persons[HEIR]
    assert world_q.goal_referents(w, onlooker, prop) == (KING,)
    # the referent FOLLOWS the hold: close the King's hold and nobody is named
    [h] = [t for t in w.tenures if t.kind == "hold" and t.live and t.object == seat]
    assert h.subject == KING
    h.until = 1
    assert not h.live and world_q.goal_referents(w, onlooker, prop) == ()
