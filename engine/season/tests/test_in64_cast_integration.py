"""v9 IN-64 (`workplans/valoria_master_workplan_v9_part5.md`, ED-IN-0293 (1), (2), (4), (5)) -- THE
CAST, INTEGRATED: every cast Person holds the fifteen pursuits and a conviction on each concern.

The loaders refuse rather than fill (`data/cast.py`): `pursuits_of` refuses a registry row naming
fewer than the full roster, `conviction_of` refuses a row with no member of a concern, the concerns
read from `descriptor_registry.yaml: affiliation_roster.concerns` through the export -- never a set
typed in Python. A case with NO row still falls back to `seed_pursuits` (the normal authoring order).

FALSIFIERS, each executed below: a planted 14-pursuit row and a row without an `altonia` member are
refused by name; `export_descriptors.py --check` is red against an export the registry has moved
past; a case with no row is drawn, and on the shipped data nobody is; `test_13d_iii`'s declared-
exception test goes red on a realm with a third unauthored seat; the cast holds no identical
full profile in IN-62's `--persons` reading.
"""
from __future__ import annotations

import importlib.util
import pathlib

import pytest

from engine.season.data import cast
from engine.season.data.rosters import PURSUITS
from engine.season.gaps import Unspecified
from engine.season.harness import decision_spread as DS
from engine.season.harness import populated
from engine.substrate.descriptors import AFFILIATION_CONCERNS

from . import test_governance_build as GB

_REPO = pathlib.Path(__file__).resolve().parents[3]


def _real_row(cid: str = "NPC-005") -> dict:
    r = cast.row(cid)
    assert r is not None, f"{cid} has no registry row: the probe has nothing to plant on"
    return r


def _primary(r: dict) -> list:
    return [e for e in r["convictions"]["primary"] if isinstance(e, dict)]


# ------------------------------------------------------------------------------ the loaders

def test_in64_every_registry_row_loads_fifteen_pursuits_and_a_member_of_every_concern():
    """The shipped registry passes both refusals: every row's pursuits are the roster exactly, and
    every row holds a member of each concern (a 0 counts -- a considered rejection, IN-63)."""
    assert set(AFFILIATION_CONCERNS) == {"church", "einhir", "altonia"}, AFFILIATION_CONCERNS
    checked = 0
    for cid, r in sorted(cast._rows().items()):
        assert set(cast.pursuits_of(r)) == set(PURSUITS), cid
        held = cast.conviction_of(r)
        for concern, members in AFFILIATION_CONCERNS.items():
            assert any(m in held for m in members), (cid, concern)
        checked += 1
    assert checked >= 46, checked


def test_in64_a_row_naming_fourteen_pursuits_is_refused_by_name():
    r = _real_row()
    assert set(cast.pursuits_of(r)) == set(PURSUITS), "control: the real row loads"
    dropped = _primary(r)[-1]["conviction"]
    planted = {**r, "id": "NPC-PLANTED-14",
               "convictions": {**r["convictions"], "primary": _primary(r)[:-1]}}
    with pytest.raises(Unspecified) as red:
        cast.pursuits_of(planted)
    assert "NPC-PLANTED-14" in str(red.value) and "14 of the 15" in str(red.value), str(red.value)
    assert dropped in str(red.value), str(red.value)


def test_in64_a_row_without_an_altonia_member_is_refused_by_name():
    r = _real_row()
    cast.conviction_of(r)                                     # control: the real row loads
    altonia = set(AFFILIATION_CONCERNS["altonia"])
    assert altonia & set(r["affiliations"]), "the real row holds no altonia member to remove"
    planted = {**r, "id": "NPC-PLANTED-ALT",
               "affiliations": {k: v for k, v in r["affiliations"].items() if k not in altonia}}
    with pytest.raises(Unspecified) as red:
        cast.conviction_of(planted)
    assert "NPC-PLANTED-ALT" in str(red.value) and "altonia" in str(red.value), str(red.value)
    # Every concern refuses alike -- the check reads the grouping, it names no concern itself.
    refused = 0
    for concern, members in AFFILIATION_CONCERNS.items():
        bare = {**r, "affiliations": {k: v for k, v in r["affiliations"].items() if k not in members}}
        with pytest.raises(Unspecified):
            cast.conviction_of(bare)
        refused += 1
    assert refused == len(AFFILIATION_CONCERNS) >= 3


def test_in64_a_zero_satisfies_its_concern():
    """An opponent holds the pole at 0 (IN-63), and a 0 is a member present."""
    r = _real_row()
    zeroed = {**r, "affiliations": {**r["affiliations"],
                                    **{m: 0 for m in AFFILIATION_CONCERNS["altonia"]}}}
    held = cast.conviction_of(zeroed)
    assert all(held[m] == 0 for m in AFFILIATION_CONCERNS["altonia"]), held


def test_in64_no_row_is_not_refused_it_is_empty():
    assert cast.pursuits_of({}) == {} and cast.conviction_of({}) == {}


# ------------------------------------------------------------------------------ the export

def _exporter():
    spec = importlib.util.spec_from_file_location("export_descriptors_in64",
                                                  _REPO / "tools" / "export_descriptors.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_in64_the_export_carries_concerns_and_check_is_red_against_a_stale_json(tmp_path, monkeypatch):
    """MUTATION, on a copy: the registry's `concerns` moved, the committed json not re-exported ->
    `--check` exits 1. CONTROL: the shipped registry against the shipped json exits 0."""
    ex = _exporter()
    assert ex.main(["--check"]) == 0, "control: the shipped export is not current"
    assert ex.build()["affiliation_roster"]["concerns"] == {
        c: list(ms) for c, ms in AFFILIATION_CONCERNS.items()}
    text = pathlib.Path(ex.SRC).read_text(encoding="utf-8")
    needle = "    altonia: [altonian_civics]\n"
    assert text.count(needle) == 1, "the registry's altonia concern line moved; re-aim the mutation"
    moved = tmp_path / "descriptor_registry.yaml"
    moved.write_text(text.replace(needle, "    altonia: [altonian_civics, thread_truth]\n"),
                     encoding="utf-8")
    monkeypatch.setattr(ex, "SRC", str(moved))
    assert ex.main(["--check"]) == 1, "--check stayed green against a json the registry moved past"


def test_in64_the_exporter_refuses_an_unrostered_or_twice_filed_member(tmp_path, monkeypatch):
    ex = _exporter()
    text = pathlib.Path(ex.SRC).read_text(encoding="utf-8")
    refused = 0
    for bad in ("    altonia: [altonian_theocracy]\n", "    altonia: [einhir_restoration]\n",
                "    altonia: []\n"):
        path = tmp_path / f"reg_{refused}.yaml"
        path.write_text(text.replace("    altonia: [altonian_civics]\n", bad), encoding="utf-8")
        monkeypatch.setattr(ex, "SRC", str(path))
        with pytest.raises(SystemExit):
            ex.build()
        refused += 1
    assert refused == 3


# ------------------------------------------------------------------------------ the built realm

@pytest.fixture(scope="module")
def _drawn():
    """The shipped realm, with every `seed_pursuits` call counted."""
    calls = []
    real = populated.seed_pursuits
    populated.seed_pursuits = lambda seed, cid, pid: calls.append(cid) or real(seed, cid, pid)
    try:
        w = populated.build_realm(0)
    finally:
        populated.seed_pursuits = real
    return w, calls


def test_in64_every_cast_person_holds_fifteen_pursuits_and_every_concern_and_none_is_drawn(_drawn):
    w, calls = _drawn
    assert calls == [], f"{len(calls)} cast person(s) fell back to the seed_pursuits draw: {calls}"
    checked = 0
    for pid, p in w.persons.items():
        if not pid.startswith("p_npc_"):
            continue
        assert set(p.pursuits) == set(PURSUITS), pid
        for concern, members in AFFILIATION_CONCERNS.items():
            assert any(m in p.conviction for m in members), (pid, concern)
        checked += 1
    assert checked >= 46, checked


def test_in64_the_cast_holds_no_identical_full_profile(_drawn):
    w, _calls = _drawn
    r = DS.read_persons(w)
    assert r["cast"] >= 46 and r["with_vector"] >= r["cast"], r
    assert r["identical_groups_cast"] == 0, r
    # IN-62's base (8372ed92) read 37 pairs above 0.99; the EXIT is "not above the base's".
    assert r["pairs_above"] <= 37, r["pairs_above"]


def test_in64_a_case_with_no_row_still_falls_back_to_seed_pursuits(monkeypatch):
    """A case added ahead of its registry row (the normal authoring order) is drawn, not refused.
    The probe hides one row -- a case no seat or leadership names, so nothing else needs the row."""
    from engine.season.data.rosters import roster_map
    leaders = set((roster_map("faction_leaders", "by_faction") or {}).values())
    cid = next(c for c in sorted(cast._rows())
               if c not in populated.OFFICES_BY_HOLDER and c not in leaders)
    pid = f"p_{cid.lower().replace('-', '_')}"
    calls = []
    real_draw, real_row = populated.seed_pursuits, cast.row
    monkeypatch.setattr(populated, "seed_pursuits",
                        lambda seed, c, p: calls.append((c, p)) or real_draw(seed, c, p))
    monkeypatch.setattr(cast, "row", lambda c: None if c == cid else real_row(c))
    w = populated.build_realm(0)
    assert calls == [(cid, pid)], calls
    assert w.persons[pid].pursuits == real_draw(0, cid, pid) and w.persons[pid].pursuits
    assert w.persons[pid].conviction == {}


def test_in64_a_third_unauthored_seat_turns_13d_iii_red(monkeypatch):
    """MUTATION: drop one Riskbreakers row -- its seat is still built by the loop from the registry
    cell, now with no row -> unauthored beside `off_npc_084`, and the declared-exception test is red.
    CONTROL: the same test on the shipped realm is green (it runs in `test_governance_build.py`)."""
    real = populated.OFFICES_SEATS
    row = next(r for r in real if r["id"] == "off_riskbreaker_doctrine")
    monkeypatch.setattr(populated, "OFFICES_SEATS", [r for r in real if r is not row])
    monkeypatch.setattr(populated, "OFFICES_BY_HOLDER",
                        {h: v for h, v in populated.OFFICES_BY_HOLDER.items() if h != row["holder"]})
    w = populated.build_realm(0)
    assert sorted(w._office_census["unauthored"]) == ["off_npc_080", "off_npc_084"], \
        w._office_census["unauthored"]
    with pytest.raises(AssertionError):
        GB.test_13d_iii_every_seat_the_realm_builds_has_a_rung_but_the_one_declared_exception(w)
