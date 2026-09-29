"""Plan position `18a` -- FIELD DELETIONS. `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`
`18a`; content owner r2 item 14 (`proposals/2026-09-17-governance-and-holdings-r2/05_LEDGER_AND_BUILD.md`
§A.1.1(e)), corrected by `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md`'s contradiction 1.

THE LIST, re-derived against the tree rather than taken from either document's count. r2's thirteen,
less what is not deletion work:
  * `Tenure.payload` -- LIVE since `13b` (the remit grant; `Tenure.granted_acts`). r2's own exclusion.
  * `Office.upkeep` -- LIVE since `17b` (`world_q.upkeep_of`). Contradiction 1.
  * `Office.scope_rung` -- LIVE since `18` (`world_q.judging_set`'s containment test). Contradiction 1,
    as corrected; and Jordan's `RR-B` ruling (limb `B-1`) keeps `scope?` in the ratified `Seat :=`.
  * `Office.establishment` -- already gone (`17a`).
  * `Person.beliefs` -- already gone (2026-09-25, with its matrix row).
  * `Rung.sites` / `records` / `dates` -- KEPT: `04 §B.3`'s ratified `Rung :=` declares all three and no
    `RR-B` limb amends that line (see `Rung`'s own comment in `state/carriers.py`).
Deleted here, five: `Office.dates`, `Rung.stake`, `Rung.transmission`, `Rung.judging_set_rule`,
`Site.drawers`. Plus the Query `conferral_path`. `judging_set` had no stub left to delete: position `18`
replaced it with the real function under the same name, which r2 says to keep.

THE FALSIFIER, r2's own: *"`Tenure.granted_acts` still returns the grant for a seated holder after the
deletions -- the test that you did not delete the live field."*
"""

from __future__ import annotations

import dataclasses

import pytest

from ..data.matrix import _W2_LAW, MATRIX, MATRIX_RETIRED
from ..gaps import Forbidden
from ..harness import probes as P
from ..harness.populated import build_realm
from ..queries import world_q
from ..state.carriers import Office, Rung, Site, Tenure, matrix_rows_without_a_field

_GONE_FROM_RUNG = ("stake", "transmission", "judging_set_rule")


def _fields(cls) -> set:
    return {f.name for f in dataclasses.fields(cls)}


def test_18a_falsifier_granted_acts_still_returns_the_grant_for_every_seated_holder():
    """r2's falsifier, on the populated realm and on the probe world. Every live `hold` on an office
    carries the office's remit as its grant -- `_grant_remit` writes `Tenure.payload` at seating and
    `granted_acts` reads it back. Deleting `payload` (r2 row 17, the one the list must NOT take) would
    make every one of these `()`, which is what the non-empty count observes."""
    assert "payload" in _fields(Tenure)
    w = build_realm(seed=0)
    seated = [t for t in w.tenures if t.kind == "hold" and t.live and t.object in w.offices]
    assert seated, "fixture: no seated holder in build_realm(0)"
    granted = 0
    for t in seated:
        assert t.granted_acts == tuple(w.offices[t.object].remit_acts), (
            f"{t.subject} holds {t.object} with grant {t.granted_acts!r}, remit "
            f"{w.offices[t.object].remit_acts!r}")
        granted += bool(t.granted_acts)
    assert granted >= 1, "every seated holder's grant is empty -- the grant carrier is not being written"

    tw = P.tiny_world()
    [duke] = [t for t in tw.tenures if t.kind == "hold" and t.live and t.object == "off_duke"]
    assert duke.granted_acts and "determine" in duke.granted_acts, duke.granted_acts
    # AND THE GRANT STILL REACHES ITS READER: `judging_set` reads `granted_acts` and `scope_rung`
    # (kept, contradiction 1). Removing either would empty this bench.
    assert world_q.judging_set(tw, "D") == [duke.subject]


def test_18a_the_kept_fields_are_still_on_their_carriers():
    """The exclusions, each with a live reader or a ratified declaration -- asserted so an over-eager
    re-run of r2's list fails here, naming the field, before it fails somewhere less legible."""
    assert {"payload", "term"} <= _fields(Tenure)
    assert {"upkeep", "scope_rung"} <= _fields(Office)
    assert {"sites", "records", "dates"} <= Rung._DECLARED


def test_18a_the_deleted_fields_are_gone_and_a_caller_passing_one_is_refused():
    """`Office.dates` and `Site.drawers` are off their dataclasses. The three `Rung` fields are off
    `_DECLARED` AND out of `__init__` -- r2's ⊕ L40 coupling: `__init__` writes through
    `object.__setattr__`, which bypasses the whitelist, so a half-deletion would have kept writing a
    field `__setattr__` refuses. Both entry points must now refuse."""
    assert "dates" not in _fields(Office)
    assert "drawers" not in _fields(Site)
    assert "establishment" not in _fields(Office)     # `17a`'s, still gone
    r = Rung("r_18a", "hearth")
    checked = 0
    for name in _GONE_FROM_RUNG:
        assert name not in Rung._DECLARED and not hasattr(r, name), name
        with pytest.raises(Forbidden):
            Rung("r_18a_kw", "hearth", **{name: None})
        with pytest.raises(Forbidden):
            setattr(r, name, None)
        checked += 1
    assert checked == len(_GONE_FROM_RUNG)
    assert not hasattr(world_q, "conferral_path")


def test_18a_matrix_report_names_no_carrier_field_that_is_gone():
    """The OBSERVABLE (r2 `05:1254`): `matrix_rows_without_a_field()`. None of the deleted fields had a
    live matrix row -- `Rung.stake` and `Site.drawers` were retired at W2, the other three never had
    one -- so the report's `absent` list does not grow, and no `Office`/`Site`/`Rung` row names a
    field its carrier lacks. The two retired entries now say the FIELD went, not only the row: W2's
    generic `needs` ("add a producing verb") would be advice for the wrong defect."""
    report = matrix_rows_without_a_field()
    assert not [k for k in report["absent"] if k[0] in ("Office", "Site", "Rung")], report["absent"]
    for kind, fld in (("Rung", "stake"), ("Site", "drawers")):
        assert (kind, fld) not in MATRIX
        law, _needs = MATRIX_RETIRED[(kind, fld)]
        assert law != _W2_LAW, f"{kind}.{fld} still carries W2's row-only reason"
