"""B24.01 (`IS-B2-SC-02`) -- THE DOCKET ITEM NAMES ITS CASE FILE.

`open_case` mints a `Record` (the case file) and docketed the matter without saying which Record; the item now
carries it under `world_q.DOCKET_CASE`, and `world_q.case_file_of` is the one reader (a carried petition is its own
case file, so the reader falls back to `DOCKET_PETITION`). Falsifier (`IS-B2-SC-02`): two items naming one case
file, or an item naming a Record nobody holds. Control: a slot CALENDAR formed names no case.
Declared MOVER: every world in which `open_case` executes gains the key (the content hash moves).
"""

from __future__ import annotations

import pytest

from ..queries import world_q
from .test_in45_carry import PARTY, PETITION, _carry, _filed
from .test_sc01_fired_slot import _convene, _next_season_calendar
from .test_u7_remit import _fold, _kinds, _open, _world


def test_an_opened_case_names_a_record_that_exists():
    """Every docket item after `open_case` -- one that fills a calendar slot, one appended where no slot
    holds the matter -- names a case file that is a Record the world keeps, on someone's `hold`, and no two
    items name one. (The realm's computed play opens no case at seeds 0 to 2: its docket is empty after a
    season, so a realm run has nothing to read and the worlds here are hand-built.)"""
    w, d = _world()
    did = _convene(w, d)
    _next_season_calendar(w, d)
    for key, subject in (("oc1", PARTY), ("oc2", "p_low")):
        assert _kinds(_fold(w, d, _open(key, subject=subject))) == ["case.opened"]
    held = {t.object for t in w.tenures if t.kind == "hold"}
    files, checked = [], 0
    for item in (i for i in w.docket if i["matter"] is not None):
        rid = world_q.case_file_of(w, item)
        assert rid in w.records, item
        assert rid in held, f"{rid} names a Record on no one's hold"
        files.append(rid)
        checked += 1
    assert checked >= 2, w.docket
    assert any(i["date"] == did and i["matter"] is not None for i in w.docket), "no case filled the slot"
    assert len(files) == len(set(files)), f"two docket items name one case file: {files}"


@pytest.mark.flat_fold
def test_a_carried_petition_is_its_own_case_file():
    """`carry` mints no case file: the petition it docketed is the file, so the item carries no `case` of its own."""
    w, d = _filed()
    out = _fold(w, d, _carry("c_yes"))
    assert _kinds(out) == ["petition.carried"], _kinds(out)
    item, = world_q.docketed(w, PARTY)
    assert item.get(world_q.DOCKET_CASE) is None, item
    assert world_q.case_file_of(w, item) == PETITION
    assert world_q.case_file_of(w, {**item, world_q.DOCKET_CASE: "rec:x"}) == "rec:x", "an opened case's own file outranks"


def test_a_slot_calendar_formed_names_no_case():
    """Control: the empty slot CALENDAR forms reads `None`; the case that fills it names the minted Record,
    the same key an appended item carries."""
    w, d = _world()
    did = _convene(w, d)
    _next_season_calendar(w, d)
    slot, = [i for i in w.docket if i["date"] == did]
    assert world_q.case_file_of(w, slot) is None
    assert _kinds(_fold(w, d, _open("oc"))) == ["case.opened"]
    filled, = [i for i in w.docket if i["date"] == did]
    assert world_q.case_file_of(w, filled) == "rec:oc" and "rec:oc" in w.records
