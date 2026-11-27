"""B34.12 (`16_PESSIMIST_GO` §4, gate 4): what a creation row marks. The seat-holder-from-ledger items of B34 (B34.23, B34.24) land their tests here."""
from __future__ import annotations

from ..boot.realm import build_realm
from ..decision.sheet import creation_sheet
from ..harness.play_surface import holdings_of


def test_creation_sheet_marks_cohorts_and_holdings():
    """`creation_sheet` at seed 0: a row's `cohort` is its person's `Person.is_cohort`, so as many rows are marked as the world seats cohorts, and
    the cohorts are neither all of the rows nor none. The holdings half of the gate (the Inquisitor's `("hold", "off_senior_inquisitor")`, a person
    with no seat showing no `hold`) is `test_season_shape.py::test_creation_sheet_shows_holdings_for_a_seat_holder`; here it is read again only
    to say the marked column and the held column are one row's, not two sheets."""
    w = build_realm(0)
    rows = creation_sheet(w.persons.values(), holdings_of(w))
    marked = sum(r.cohort for r in rows)
    assert marked == sum(p.is_cohort for p in w.persons.values())
    assert 0 < marked < len(rows), f"setup: {marked} of {len(rows)} rows are cohorts, so the column cannot show a difference"
    checked = 0
    for r in rows:
        assert r.cohort is w.persons[r.id].is_cohort, f"{r.id}: the row says cohort={r.cohort}, the person says {w.persons[r.id].is_cohort}"
        checked += 1
    assert checked == len(rows) == len(w.persons)
    # a cohort holds no seat (`state/gate.py`: a population is no officeholder), so a marked row shows no `hold`; the Inquisitor's row is no cohort
    assert not any(kind == "hold" for r in rows if r.cohort for kind, _ in r.holdings)
    inquisitor = next(r for r in rows if r.id == "p_npc_004")
    assert not inquisitor.cohort and ("hold", "off_senior_inquisitor") in inquisitor.holdings
