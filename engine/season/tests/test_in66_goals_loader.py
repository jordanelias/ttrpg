"""v9 IN-66 (`workplans/valoria_master_workplan_v9_part5.md`, A-31; ED-IN-0293 (8)) -- THE GOALS
CARRIER: `engine/season/goals.yaml`, its one loader `data/goals.py`, and the two closed rosters
`goal_object_kinds` and `goal_derivations`.

A loader that cannot refuse is absent (`CLAUDE.md` §0.1 pt 2). Every refusal the entry lists is
PLANTED here, each by ONE mutation of one valid base document, so each refusal is isolated from the
others; each must raise (`pytest.raises`) the tree's refusal type naming the row. The base is loaded
first (the control), and the parametrised list asserts it ran a floor's worth of plants.

Rung ids are NOT refused here (checked at seeding, IN-68, once rungs exist): `rung:` must be a name.
"""
from __future__ import annotations

import copy

import pytest
import yaml

from engine.season.data import files, goals
from engine.season.data.rosters import PURSUITS, roster, roster_map
from engine.season.gaps import Forbidden, Unspecified


def _row(gid, org, obj, **more):
    return {"id": gid, "org": org, "text": f"{gid}, as a predicate", "object": obj,
            "pursuits": {"stability": 1}, "source": "test_in66", **more}


def _base() -> dict:
    """A valid document: a faction -> faction derivation, a seat -> body -> faction chain, and every
    object kind and every `deed_doers` form once."""
    return {"goals": [
        _row("g_fac", {"faction": "Löwenritter"}, {"kind": "orientation"}),
        _row("g_body", {"body": "Riskbreakers"}, {"kind": "seat_holders", "seats": ["off_king"]},
             stance=1, derives={"from": "g_fac", "kind": "establishes"}),
        _row("g_seat", {"seat": "off_riskbreaker_covert"}, {"kind": "person", "case": "NPC-020"},
             stance=-1, derives={"from": "g_body", "kind": "influences"}),
        _row("g_fac2", {"faction": "Crown"}, {"kind": "deed_doers", "kinds": ["bond.formed"]},
             derives={"from": "g_fac", "kind": "influences"}),
        _row("g_against", {"faction": "Varfell"}, {"kind": "deed_doers", "against": "g_body"}),
        _row("g_engage", {"faction": "Church of Solmund"},
             {"kind": "deed_doers", "engaging": "einhir_restoration"}),
        _row("g_rung", {"faction": "Hafenmark"}, {"kind": "rung", "rung": "terr_T9"}),
    ]}


def _mutated(gid, mutate) -> dict:
    """`_base()` with ONE goal row changed by `mutate(row)`; the only edit made."""
    doc = _base()
    mutate(next(r for r in doc["goals"] if r["id"] == gid))
    return doc


def _set(key, value):
    return lambda r: r.__setitem__(key, value)


def _in_object(key, value):
    return lambda r: r["object"].__setitem__(key, value)


def _drop(key):
    return lambda r: r.pop(key)


def _reseat(org, parent, kind="influences"):
    """Move a row to `org` and derive it from `parent`: the one edit that plants an ancestry plant on
    a row of its own, so no derivation cycle can be what refuses it."""
    return lambda r: r.update(org=org, derives={"from": parent, "kind": kind})


# ------------------------------------------------------------------------------ the control

def test_in66_a_valid_hand_built_document_loads():
    got = goals.parse(_base())
    assert [g.id for g in got] == [r["id"] for r in _base()["goals"]]
    by = {g.id: g for g in got}
    assert (by["g_fac2"].org_kind, by["g_fac2"].derives_from) == ("faction", "g_fac"), \
        "a faction -> faction derivation loads (authored content; the oath makes it subordinate)"
    chain = [by["g_seat"], by[by["g_seat"].derives_from], by[by[by["g_seat"].derives_from].derives_from]]
    assert [g.org_kind for g in chain] == ["seat", "body", "faction"], "the seat -> body -> faction chain"
    assert by["g_body"].stance == 1 and by["g_seat"].stance == -1 and by["g_fac"].stance is None
    assert by["g_rung"].object["rung"] == "terr_T9", "a rung id is kept as a name, not checked"
    assert {g.object["kind"] for g in got} == set(roster("goal_object_kinds")), \
        "the base exercises every rostered object kind"
    forms = set(roster_map("goal_object_kinds", "forms")["deed_doers"])
    assert len(forms) == 3 and {f for g in got if g.object["kind"] == "deed_doers"
                                for f in forms if f in g.object} == forms, \
        "the base exercises every rostered deed_doers form"


def test_in66_a_seat_goal_may_derive_from_its_factions_goal_directly():
    """A seat's ancestors are its body AND its faction; the entry's chain is a chain, not a ladder
    a goal must climb one rung at a time. [ASSUMPTION; the entry says only 'not its ancestor']"""
    doc = _mutated("g_seat", _set("derives", {"from": "g_fac", "kind": "influences"}))
    assert goals.parse(doc)


def test_in66_the_two_rosters_are_closed_and_hold_the_ruled_members():
    from engine.season.data import rosters
    kinds = roster("goal_object_kinds")
    # one membership per assert: spelling the five together would DUPLICATE the roster in a body,
    # which `test_season_shape.py::test_jordan_no_definition_is_hardcoded_in_a_body` refuses
    assert len(kinds) == 5
    for member in ("person", "seat_holders", "rung"):
        assert member in kinds, member
    assert "deed_doers" in kinds and "orientation" in kinds
    assert roster("goal_derivations") == {"establishes", "influences"}
    for name in ("goal_object_kinds", "goal_derivations"):
        assert rosters._ROSTERS[name]["open"] is False, name


def test_in66_the_shipped_goals_file_loads_through_the_one_loader(monkeypatch):
    """The file was empty until v9 FA-05 authored its first rows (`test_fa05_user_goals.py` reads them); what
    stays IN-66's is that the shipped file is the loader's own path and loads with no row refused."""
    assert files.GOALS_YAML.is_file() and goals.GOALS_YAML == files.GOALS_YAML
    raw = yaml.safe_load(files.GOALS_YAML.read_text(encoding="utf-8"))
    monkeypatch.setattr(goals, "_CACHE", None)
    assert len(goals.goals()) == len(raw["goals"]) and goals.goal("g_fac") is None


def test_in66_the_lazy_reader_loads_a_file_through_its_patch_point(monkeypatch, tmp_path):
    path = tmp_path / "goals.yaml"
    path.write_text(yaml.safe_dump(_base(), allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr(goals, "GOALS_YAML", path)
    monkeypatch.setattr(goals, "_CACHE", None)
    assert [g.id for g in goals.goals()] == [r["id"] for r in _base()["goals"]]
    assert goals.goal("g_body").org == "Riskbreakers"


def test_in66_a_planted_violation_in_the_file_is_refused_through_the_reader_too(monkeypatch, tmp_path):
    path = tmp_path / "goals.yaml"
    path.write_text(yaml.safe_dump(_mutated("g_fac", _set("org", {"faction": "Atlantis"})),
                                   allow_unicode=True), encoding="utf-8")
    monkeypatch.setattr(goals, "GOALS_YAML", path)
    monkeypatch.setattr(goals, "_CACHE", None)
    with pytest.raises(Unspecified, match="g_fac"):
        goals.goals()
    assert goals._CACHE is None, "a refused file is not cached as if it had loaded"


def test_in66_a_missing_goals_file_is_refused_not_read_as_empty(monkeypatch, tmp_path):
    monkeypatch.setattr(goals, "GOALS_YAML", tmp_path / "absent.yaml")
    monkeypatch.setattr(goals, "_CACHE", None)
    with pytest.raises(Unspecified):
        goals.goals()


# ------------------------------------------------------------------------------ the plants
#
# (name, doc, refusal type, a fragment of the message naming what is wrong). The row id is asserted
# separately, for every plant: "naming the row".

_PLANTS = [
    # --- an unknown organization
    ("unknown faction", _mutated("g_fac", _set("org", {"faction": "Atlantis"})), Unspecified, "Atlantis"),
    ("unknown body", _mutated("g_body", _set("org", {"body": "Ministry of Nothing"})), Unspecified,
     "Ministry of Nothing"),
    ("unknown seat", _mutated("g_seat", _set("org", {"seat": "off_nobody"})), Unspecified, "off_nobody"),
    ("unknown org kind", _mutated("g_fac", _set("org", {"clan": "Löwenritter"})), Unspecified, "clan"),
    ("two organizations", _mutated("g_fac", _set("org", {"faction": "Crown", "body": "Riskbreakers"})),
     Unspecified, "exactly one"),
    ("no organization", _mutated("g_fac", _drop("org")), Unspecified, "exactly one"),
    # --- an unknown kind
    ("unknown object kind", _mutated("g_fac", _in_object("kind", "wish")), Unspecified, "wish"),
    ("unknown derivation kind",
     _mutated("g_body", _set("derives", {"from": "g_fac", "kind": "supersedes"})), Unspecified, "supersedes"),
    # --- an unknown referent: case id, seat id, affiliation, deed kind, goal id
    ("unknown case id", _mutated("g_seat", _in_object("case", "NPC-999")), Unspecified, "NPC-999"),
    ("unknown seat id in seat_holders", _mutated("g_body", _in_object("seats", ["off_king", "off_nobody"])),
     Unspecified, "off_nobody"),
    ("unknown affiliation", _mutated("g_engage", _in_object("engaging", "flat_earth")), Unspecified,
     "flat_earth"),
    ("unknown deed kind", _mutated("g_fac2", _in_object("kinds", ["bond.formed", "no.such_kind"])),
     Unspecified, "no.such_kind"),
    ("unknown goal id in against", _mutated("g_against", _in_object("against", "g_ghost")), Unspecified,
     "g_ghost"),
    ("deed_doers naming two forms", _mutated("g_fac2", _in_object("engaging", "einhir_restoration")),
     Unspecified, "forms"),
    ("deed_doers naming no form", _mutated("g_fac2", lambda r: r["object"].pop("kinds")),
     Unspecified, "forms"),
    ("seat_holders naming no seats", _mutated("g_body", _in_object("seats", [])), Unspecified, "seats"),
    ("person naming no case", _mutated("g_seat", lambda r: r["object"].pop("case")), Unspecified, "case"),
    ("rung naming no rung", _mutated("g_rung", lambda r: r["object"].pop("rung")), Unspecified, "rung"),
    # --- derives: dangling, cyclic
    ("dangling derives", _mutated("g_body", _set("derives", {"from": "g_ghost", "kind": "establishes"})),
     Unspecified, "g_ghost"),
    ("cyclic derives (two goals)", _mutated("g_fac", _set("derives", {"from": "g_fac2", "kind": "influences"})),
     Forbidden, "returns to"),
    ("cyclic derives (self)", _mutated("g_fac", _set("derives", {"from": "g_fac", "kind": "influences"})),
     Forbidden, "returns to"),
    # --- derives: the parent's org must be an ancestor (seat -> body -> faction)
    ("body deriving from another faction's goal",
     _mutated("g_body", _set("derives", {"from": "g_fac2", "kind": "establishes"})), Forbidden, "not above it"),
    ("seat deriving from another faction's goal",
     _mutated("g_seat", _set("derives", {"from": "g_fac2", "kind": "establishes"})), Forbidden, "not above it"),
    ("seat deriving from a seat goal (a sibling, not an ancestor)",
     _mutated("g_rung", _reseat({"seat": "off_riskbreaker_doctrine"}, "g_seat")), Forbidden, "not above it"),
    ("body deriving from a seat goal (a descendant)",
     _mutated("g_rung", _reseat({"body": "Riskbreakers"}, "g_seat")), Forbidden, "not above it"),
    ("body deriving from a body goal (a peer)",
     _mutated("g_rung", _reseat({"body": "Riskbreakers"}, "g_body")), Forbidden, "not above it"),
    ("faction deriving from a body goal",
     _mutated("g_fac2", _set("derives", {"from": "g_body", "kind": "influences"})), Forbidden, "not above it"),
    # --- stance
    ("stance 0", _mutated("g_body", _set("stance", 0)), Unspecified, "stance"),
    ("stance 2", _mutated("g_body", _set("stance", 2)), Unspecified, "stance"),
    ("stance a word", _mutated("g_body", _set("stance", "for")), Unspecified, "stance"),
    ("stance a bool", _mutated("g_body", _set("stance", True)), Unspecified, "stance"),
    # --- pursuits
    ("no pursuits key", _mutated("g_fac", _drop("pursuits")), Unspecified, "pursuits"),
    ("empty pursuits", _mutated("g_fac", _set("pursuits", {})), Unspecified, "pursuits"),
    ("unknown pursuit", _mutated("g_fac", _set("pursuits", {"stability": 1, "bloodlust": 1})), Unspecified,
     "bloodlust"),
    ("a pursuit weighing nothing", _mutated("g_fac", _set("pursuits", {"stability": 0})), Unspecified,
     "weighs"),
    # --- a duplicate id
    ("duplicate id", {"goals": _base()["goals"] + [copy.deepcopy(_base()["goals"][0])]}, Forbidden,
     "more than one"),
    # --- the row's own fields
    ("no text", _mutated("g_fac", _drop("text")), Unspecified, "text"),
    ("no source", _mutated("g_fac", _drop("source")), Unspecified, "source"),
    ("no object", _mutated("g_fac", _drop("object")), Unspecified, "object"),
    ("no goals list", {"goals": None}, Unspecified, "goals"),
]


def test_in66_the_plants_ran_a_floor_of_refusals_and_each_is_unique():
    assert len(_PLANTS) >= 38, len(_PLANTS)
    assert len({name for name, *_ in _PLANTS}) == len(_PLANTS)


@pytest.mark.parametrize("name,doc,cls,fragment", _PLANTS, ids=[p[0] for p in _PLANTS])
def test_in66_each_planted_violation_is_refused_by_name(name, doc, cls, fragment):
    # the plant is ONE mutation of the base: the base itself loads (the control), so the refusal
    # below can only be the mutation's.
    assert goals.parse(_base())
    with pytest.raises(cls) as red:
        goals.parse(doc)
    msg = str(red.value)
    assert fragment in msg, (name, msg)
    assert type(red.value) is cls, (name, type(red.value))
    # naming the row: the message carries the id of a goal row of the document
    if name != "no goals list":
        assert any(f"goal {r['id']!r}" in msg for r in doc["goals"]), (name, msg)


def test_in66_the_pursuit_roster_is_the_one_owners(monkeypatch):
    """The pursuit names are checked through `data/pursuits.py::pursuit`, the one owner, not a set
    typed in the loader: every rostered pursuit is accepted, so a roster edit reaches this loader."""
    doc = _mutated("g_fac", _set("pursuits", {p: 1 for p in sorted(PURSUITS)}))
    assert len(goals.parse(doc)[0].pursuits) == len(PURSUITS) >= 15
