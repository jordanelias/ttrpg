"""v9 SC-02 `23` -- typed ids and the remaining loader invariants (`04_CODE_ARCHITECTURE.md` §B.1, §B.13).

GRADE, STATED AS THE ENTRY REQUIRES: CI runs NO type-checker, so the `SeatId` wrapper is a RUNTIME
grade. `Act.actor` cannot hold a `SeatId` because the fold REFUSES one (`04:222`, *"MECHANICAL -- tag
assertion in the fold"*), not because a checker would; under a checker it would also be structural,
and nothing here claims that.

WHAT EACH BLOCK OBSERVES:
  1. THE SEATID TEST. Written BEFORE `SeatId` existed (it failed at import: `ImportError: cannot
     import name 'SeatId' from engine.season.state.ids` -- red by absence), then made green. Its real
     observation is a typed `SeatId` passed as `Act.actor` being refused in the fold, on BOTH fold
     entries (`resolve` and `encounter` share `_survives`); the control is the same string as a plain
     `str` / a person, which is not refused by the tag.
  2. THE BYTE-IDENTITY CONTROL. The wrapper folds IDENTICAL strings: the seats in the realm are
     `SeatId`s, and `build_realm(0).content_hash()` is `BASE_HASHES[0]`, unchanged.
  3. ONE TEST PER LOADER INVARIANT: plant the violation, expect a `SystemExit` naming its row.
"""

from __future__ import annotations

import re

import pytest

from ..gaps import InstrumentDefect
from ..state.carriers import Act, Office
from ..state.ids import SeatId
from .test_u7_remit import DUKE, SEAT, _fold, _kinds, _world


# ======================================================================================
# 1 -- A `SeatId` AS `Act.actor` IS REFUSED IN THE FOLD (the plan's falsifier for `23`)
# ======================================================================================

def test_a_seat_id_passed_as_act_actor_is_refused_in_the_fold():
    """The act's actor is the seat's id, TYPED. The refusal is `InstrumentDefect` ("you called me
    wrong", `gaps.py`), not a `ShapeGap`: a seat acting is AX-1's violation, and a probe that provokes
    it must not be filed as a design GAP. Control, in the same world: the same verb by the holder, naming
    the seat through `via`, is folded (it reaches an Event), so the refusal is the tag's and not the
    act's. The store is untouched by the refused act's id (the act enters the store before the fold, so
    the assertion is on the Events: none was emitted for it)."""
    w, d = _world()
    seat = w.offices[SEAT].id
    assert isinstance(seat, SeatId), "the office id is a SeatId, or no real act could carry one"
    bad = Act(id="seat_acts", actor=seat, verb="open_case", via=None, payload={"subject": "p_mid"})
    n = len(w.log)
    with pytest.raises(InstrumentDefect) as refused:
        _fold(w, d, bad)
    assert "SeatId" in str(refused.value) and SEAT in str(refused.value), str(refused.value)
    assert len(w.log) == n, "the refused act left an Event in the log"
    # CONTROL: the person who holds the seat, naming it through `via`, folds.
    ok = Act(id="holder_acts", actor=DUKE, verb="open_case", via=SEAT, payload={"subject": "p_mid"})
    assert _kinds(_fold(w, d, ok)), "control: the holder's act emitted nothing at all"


def test_a_seat_id_actor_is_refused_by_the_check_both_fold_entries_share():
    """`resolve` and `loop/encounter.py` both open with `_survives`, so the one refusal serves two
    entries (asserted on the shared function; `encounter.py` is read below for that call). A plain-`str`
    actor naming the same string is NOT refused by the tag: it is simply not a person
    (`act.ineligible`), so the tag is what separates 'a seat tried to act' from 'nobody is there'."""
    from ..loop import encounter
    import inspect
    assert "self._survives(w, a)" in inspect.getsource(encounter), "encounter no longer shares the check"
    w, d = _world()
    seat_str = str(w.offices[SEAT].id)
    assert type(seat_str) is str and not isinstance(seat_str, SeatId)
    plain = Act(id="plain_ghost", actor=seat_str, verb="open_case", payload={"subject": "p_mid"})
    out = _fold(w, d, plain)
    assert _kinds(out) == ["act.ineligible"], _kinds(out)
    typed = Act(id="typed_ghost", actor=SeatId(seat_str), verb="open_case",
                payload={"subject": "p_mid"})
    with pytest.raises(InstrumentDefect):
        d._survives(w, typed)
    assert [e.kind for e in d._survives(w, plain)] == ["act.ineligible"], "control: the plain ghost"


def test_the_via_of_an_act_is_typed_as_a_seat():
    """`Act.via : SeatId?` (`04:423`): a bare string given as `via` is tagged at construction, and
    `None` stays `None`. The tag is the same string, so nothing keyed on it moves."""
    a = Act(id="a", actor=DUKE, verb="open_case", via=SEAT)
    assert isinstance(a.via, SeatId) and a.via == SEAT
    assert hash(a.via) == hash(SEAT) and f"{a.via}" == SEAT and repr(a.via) == repr(SEAT)
    assert Act(id="b", actor=DUKE, verb="open_case").via is None
    assert isinstance(Office(SEAT, "Duke", "D", ["issue"], faction="Crown").id, SeatId)


# ======================================================================================
# 2 -- THE BYTE-IDENTITY CONTROL: THE WRAPPER FOLDS IDENTICAL STRINGS
# ======================================================================================

def test_the_wrapper_leaves_the_content_hash_where_it_was():
    """`build_realm(0)` seats the whole governance ladder, so its offices are `SeatId`s; its
    `content_hash()` is `BASE_HASHES[0]`, pinned BEFORE the wrapper existed (`d3edd90a...`, the base
    commit). The 1- and 2-season pins are `test_season_weather.py::test_in21_control_draw_off_...`, which
    this change was run against. The string-level control beside it: the mint folds a `SeatId` exactly
    as the bare string, and the tag does not survive into an f-string."""
    from ..harness import populated as POP
    from ..state.ids import H
    from .test_season_weather import BASE_HASHES
    w = POP.build_realm(0)
    seats = [o.id for o in w.offices.values()]
    assert len(seats) >= 20 and all(isinstance(i, SeatId) for i in seats), "the realm's seats are untyped"
    assert w.content_hash() == BASE_HASHES[0], "the wrapper moved the corpus hash"
    s = str(seats[0])
    assert H(1, 2, SeatId(s), "p") == H(1, 2, s, "p") and f"{SeatId(s)}" == s
    assert type(f"{SeatId(s)}") is str and SeatId(s) == s and {SeatId(s): 1}[s] == 1


# ======================================================================================
# 3 -- LOADER INVARIANT 7: THE EVENT-KIND ROSTER IS DERIVED, THE FOLD'S THREE LITERALS ARE COLUMNS
# ======================================================================================
# Each test PLANTS the violation and expects a `SystemExit` naming its row. The control is the shipped
# data, which loaded to import this file.

import dataclasses  # noqa: E402

from ..data import rosters as _rosters  # noqa: E402
from ..data import verbs as _verbs      # noqa: E402
from ..data.matrix import MATRIX         # noqa: E402
from ..data.rosters import FOLD_KINDS, LOGGED_KINDS    # noqa: E402
from ..data.verbs import EVENT_KINDS, VERB_TABLE, derive_event_kinds  # noqa: E402
from ..loop import resolve as _resolve   # noqa: E402
from .test_u7_remit import _plant        # noqa: E402

THREE = tuple(sorted(FOLD_KINDS))      # read off the data; the floor below pins it at the three


def test_the_three_body_literal_kinds_are_declared_columns_and_in_the_derived_roster():
    """F.20b's three kinds, as the live fold emits them (`act.ineligible`, `act.refused`, and S27.4's
    `attempt.refused` -- `04` names `contest.resolved` for the third, which the live fold never emits)."""
    assert len(THREE) == 3, FOLD_KINDS
    assert set(FOLD_KINDS.values()) == {"act.ineligible", "act.refused", "attempt.refused"}
    assert set(FOLD_KINDS.values()) <= EVENT_KINDS
    # the roster is DERIVED: every verb-row column and every matrix `emits:` is a member
    for name, row in VERB_TABLE.items():
        for col in (row.emits, row.emits_on_refusal, *row.emits_by_degree.values(),
                    *row.refusals_by_clause.values()):
            assert set(col) <= EVENT_KINDS, (name, col)
    checked = 0
    for mrow in MATRIX.values():
        assert set(mrow.emits) <= EVENT_KINDS
        checked += len(mrow.emits)
    assert checked >= 20 and len(EVENT_KINDS) >= 100, (checked, len(EVENT_KINDS))


@pytest.mark.parametrize("key", THREE)
def test_inv7_a_fold_kind_column_missing_refuses_the_load_naming_its_row(key):
    planted = {k: v for k, v in FOLD_KINDS.items() if k != key}
    with pytest.raises(SystemExit, match=rf"rosters\.yaml: `fold_kinds` misses \['{key}'\]"):
        _rosters.check_fold_kinds(planted)


def test_inv7_a_fold_kind_nothing_reads_and_a_malformed_kind_refuse_the_load():
    with pytest.raises(SystemExit, match=r"`fold_kinds` .*carries \['contest_resolved'\] that nothing reads"):
        _rosters.check_fold_kinds({**FOLD_KINDS, "contest_resolved": "contest.resolved"})
    with pytest.raises(SystemExit, match=r"`fold_kinds` .*malformed kind\(s\) for \['refused'\]"):
        _rosters.check_fold_kinds({**FOLD_KINDS, "refused": "actrefused"})
    assert _rosters.check_fold_kinds(dict(FOLD_KINDS)) == FOLD_KINDS, "control: the shipped roster"


def test_inv7_the_kinds_matter_logs_directly_are_a_declared_column_in_the_derived_roster():
    """`loop/matter.py` logs `standing.band_crossed` with no write behind it, so no matrix or verb row can
    declare it; it is the `logged_kinds` column (`rosters.yaml`), and the derived roster holds it. A
    drifted or malformed column refuses the load naming the row (PLANTED); dropping the column from the
    derivation leaves the kind outside `EVENT_KINDS` (the defect the B-P layer pass found)."""
    assert set(LOGGED_KINDS.values()) == {"standing.band_crossed"} and set(LOGGED_KINDS.values()) <= EVENT_KINDS
    with pytest.raises(SystemExit, match=r"`logged_kinds` keys \['standing_crossed', 'x'\]"):
        _rosters.check_logged_kinds({**LOGGED_KINDS, "x": "a.b"})
    with pytest.raises(SystemExit, match=r"malformed kind\(s\) for \['standing_crossed'\]"):
        _rosters.check_logged_kinds({"standing_crossed": "standingcrossed"})
    assert _rosters.check_logged_kinds(dict(LOGGED_KINDS)) == LOGGED_KINDS, "control: the shipped column"
    assert not set(LOGGED_KINDS.values()) <= derive_event_kinds(VERB_TABLE, MATRIX, FOLD_KINDS, {}), (
        "the kind is declared by another column; this test observes nothing")


def test_inv7_a_malformed_kind_in_an_emission_column_refuses_the_derivation_naming_the_row():
    for col, plant in (("emits", dict(emits=("tellmade",))),
                       ("emits_on_refusal", dict(emits_on_refusal=("",))),
                       ("emits[Success]", dict(emits_by_degree={"Success": ["a.b.c"]}))):
        table = dict(VERB_TABLE, tell=dataclasses.replace(VERB_TABLE["tell"], **plant))
        with pytest.raises(SystemExit,
                           match=rf"verb_table\.yaml: 'tell' declares Event kind .* in `{re.escape(col)}:`"):
            derive_event_kinds(table, MATRIX, FOLD_KINDS, LOGGED_KINDS)
    row = next(iter(MATRIX.values()))
    bad = {k: (dataclasses.replace(r, emits=("nodot",)) if r is row else r) for k, r in MATRIX.items()}
    with pytest.raises(SystemExit, match=r"write_matrix\.yaml \(.*\) declares Event kind 'nodot'"):
        derive_event_kinds(VERB_TABLE, bad, FOLD_KINDS, LOGGED_KINDS)
    assert derive_event_kinds(VERB_TABLE, MATRIX, FOLD_KINDS, LOGGED_KINDS) == EVENT_KINDS, "control"


def test_inv7_the_fold_mints_no_kind_a_column_does_not_declare():
    """The F.20b defect at EXECUTION: `_act_events` refuses a kind outside the derived roster before the
    Event exists. Control, same world, same act: a declared kind is built."""
    w, d = _world()
    a = Act(id="ghost", actor=DUKE, verb="open_case")
    with pytest.raises(InstrumentDefect, match=r"would emit Event kind\(s\) \['thing\.happened'\]"):
        _resolve._act_events(d, w, a, ("thing.happened",))
    assert [e.kind for e in _resolve._act_events(d, w, a, ("act.refused",))] == ["act.refused"]


def test_inv7_the_fold_reads_each_literal_from_the_roster_not_from_its_body(monkeypatch):
    """OBSERVED, NOT GREPPED: point each of the three constants at a kind no column declares and drive
    the fold path that emits it. A body literal left behind would emit the old kind and raise nothing;
    reading the roster raises on the planted one. Three paths, three observations."""
    w, d = _world()
    # (1) `ineligible`: a predecessor removed the actor (S27.1)
    monkeypatch.setattr(_resolve, "FOLD_INELIGIBLE", "act.vanished")
    with pytest.raises(InstrumentDefect, match="act.vanished"):
        d._survives(w, Act(id="gone", actor="p_nobody", verb="open_case"))
    # (2) `refused`: the party-gap fallback of a hand-built act naming no verb row
    monkeypatch.setattr(_resolve, "FOLD_REFUSED", "act.declined")
    with pytest.raises(InstrumentDefect, match="act.declined"):
        _resolve._refuse_party_gap(d, w, Act(id="nowhere", actor=DUKE, verb="no_such_verb"))
    # (3) `attempt_refused`: S27.4's refusal of an attempt past the obstacle ceiling
    monkeypatch.setattr(_resolve, "FOLD_ATTEMPT_REFUSED", "attempt.spurned")
    over = Act(id="over", actor=DUKE, verb="open_case", obstacle=99, pool=1)
    with pytest.raises(InstrumentDefect, match="attempt.spurned"):
        _fold(w, d, over)
    monkeypatch.undo()
    again = Act(id="over2", actor=DUKE, verb="open_case", obstacle=99, pool=1)
    assert [e.kind for e in _fold(w, d, again)] == ["attempt.refused"], "control: the shipped kind"


# ======================================================================================
# 4 -- LOADER INVARIANT 4, THE FLAT HALF (S-8's residue)
# ======================================================================================

def test_inv4_a_flat_row_with_two_clauses_and_two_refusal_kinds_refuses_the_load(monkeypatch):
    """`confer` is FLAT with an eligibility, a counterparty and a write: a flat list is emitted whole at
    every refusal, so a second kind is published for a clause that did not fail (`ID-9`)."""
    assert not VERB_TABLE["confer"].refusals_by_clause, "fixture: confer must be a flat row"
    _plant(monkeypatch, "confer", lambda r: r["emits_on_refusal"].append("confer.also"))
    with pytest.raises(SystemExit, match=r"'confer' is a FLAT row with \d failable clause\(s\) and "
                                         r"declares 2 refusal kinds \['confer\.refused', 'confer\.also'\]"):
        _verbs._load_verb_table()


def test_inv4_a_contested_flat_row_with_two_refusal_kinds_refuses_at_the_party_gap(monkeypatch):
    """The party-gap refusal names no clause, so a contested flat row's second kind is the same defect
    even with one failable clause."""
    assert VERB_TABLE["fight"].contests and not VERB_TABLE["fight"].refusals_by_clause
    _plant(monkeypatch, "fight", lambda r: r["emits_on_refusal"].append("kill.also"))
    with pytest.raises(SystemExit, match=r"'fight' is a FLAT row .* and a contest/graded party gap"):
        _verbs._load_verb_table()


def test_inv4_the_earned_kind_is_the_only_exemption_and_it_is_one_constant_not_a_row_name(monkeypatch):
    """`dispatch` is flat with two clauses and two kinds and LOADS, because `person.demanded`
    (`data/rosters.py::PERSON_DEMANDED`, the kind the fold filters in `_demand_earned`) is exempt. Point
    the loader at another kind and the same row refuses -- so the exemption is that one constant,
    observed, and no verb is named in the code."""
    row = VERB_TABLE["dispatch"]
    assert not row.refusals_by_clause and len(row.emits_on_refusal) == 2, "fixture: dispatch is the case"
    monkeypatch.setattr(_verbs, "PERSON_DEMANDED", "ghost.kind")
    with pytest.raises(SystemExit,
                       match=r"'dispatch' is a FLAT row .*\['dispatch\.refused', 'person\.demanded'\]"):
        _verbs._load_verb_table()
    monkeypatch.undo()
    assert "dispatch" in _verbs._load_verb_table(), "control: the shipped constant loads the row"


def test_inv4_the_fold_earns_the_demanded_kind_at_every_refusal_site_not_only_three():
    """The loader exempts `person.demanded` from the flat-row refusal because the fold publishes it only
    when the act earns it: from the PRECONDITION refusal of an act naming nobody the world holds
    (`_demand_earned`). That has to hold at EVERY refusal site, or the exemption is a lie at the ones
    left whole. Observed at the party-gap and after-the-fact sites, which carry `dispatch`'s whole
    declared list: an act naming nobody, refused there, emits `dispatch.refused` ALONE (CONTROL: the
    precondition refusal of the same act still emits `person.demanded`)."""
    w, d = _world()
    row = VERB_TABLE["dispatch"]
    assert "person.demanded" in row.emits_on_refusal, "fixture: dispatch declares the kind"
    nobody = {"subject": "nobody_the_world_holds"}
    gap = _resolve._refuse_party_gap(d, w, Act(id="pg", actor=DUKE, verb="dispatch", payload=dict(nobody)))
    assert [e.kind for e in gap] == ["dispatch.refused"], [e.kind for e in gap]
    earned = _fold(w, d, Act(id="pc", actor=DUKE, verb="dispatch", payload=dict(nobody), via=SEAT))
    assert "person.demanded" in [e.kind for e in earned], "control: the precondition refusal earns it"
    # the loader's exemption and the fold's filter are one constant, read from one place
    assert _resolve.PERSON_DEMANDED is _rosters.PERSON_DEMANDED is _verbs.PERSON_DEMANDED


# ======================================================================================
# 5 -- THE `data/` LOADERS BEHIND ONE ENTRY; THE EFFECTS CORPUS IS ENUMERATED, NEVER LISTED
# ======================================================================================

def test_load_all_reaches_every_loader_and_the_driver_calls_it_first(monkeypatch):
    import pkgutil
    from .. import data
    from ..data import files, goals
    from ..loop import driver as _driver
    from ..loop.driver import SeasonDriver
    loaded = data.load_all()
    on_disk = sorted(i.name for i in pkgutil.iter_modules(data.__path__) if i.name != "files")
    assert list(loaded) == on_disk and len(loaded) >= 11, loaded      # discovered, with a floor
    assert {"rosters", "matrix", "verbs", "goals", "geography", "cast"} <= set(loaded)
    # a lazy loader's refusal is reachable from the one entry: plant a missing goals file
    monkeypatch.setattr(goals, "_CACHE", None)
    monkeypatch.setattr(goals, "GOALS_YAML", files.DATA_DIR / "no_such_goals.yaml")
    with pytest.raises(Exception, match="no_such_goals.yaml"):
        data.load_all()
    monkeypatch.undo()

    # and the driver is the caller: a sentinel raised from the entry surfaces from the constructor
    def boom():
        raise RuntimeError("load_all reached")
    w, _ = _world()
    monkeypatch.setattr(_driver, "load_all", boom)
    with pytest.raises(RuntimeError, match="load_all reached"):
        SeasonDriver(w)


def test_effects_corpus_is_enumerated_through_effects_modules_and_the_openers_read_it():
    """The opener derivation (`data/verbs.py::_derive_openers_from_effects`) reads
    `files.effects_modules()`: the discovered `effects*.py` set, floor 8 (the aggregator plus the seven
    siblings its docstring names), never a hand list."""
    import inspect
    from ..data import files
    mods = files.effects_modules()
    assert len(mods) >= 8 and all(p.name.startswith("effects") for p in mods), [p.name for p in mods]
    body = inspect.getsource(_verbs._derive_openers_from_effects)
    assert "effects_modules()" in body, "the openers walk a hand-listed corpus"
