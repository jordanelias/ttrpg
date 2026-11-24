"""B21.60 -- a seat is held by an individual (`16_PESSIMIST_FA_B` edit 1, G1; R-04 who may sit).

`state/gate.py::may_sit` is the one predicate: the person exists and is not a cohort. `confer`'s and `succeed`'s preconditions and
the write gate's `conferral` and `claim` clauses all ask it, so a cohort is refused at the fold (`confer.refused`) where the gate
would raise. Later positions of the item chain (B21.61 to B21.63) add their arms to this file.
"""
from __future__ import annotations

import pytest

from ..data.matrix import WriteClass
from ..harness import probes as P
from ..loop.driver import mint_token
from ..state.carriers import Act
from ._seat_at_success import seat_at_success  # noqa: F401  (the fixture; its reason is in its module)
from .test_g3_not_yours import _gov_world, _hold

pytestmark = pytest.mark.usefixtures("seat_at_success")   # B21.14: a conferral is resisted by a draw; the write, not the draw, is this file's

SEAT, CONFERRER, VIA, INDIVIDUAL, COHORT = "off_reeve", "p_king", "off_crown", "p_mid", "c_crowd"


def _confer(w, d, to, aid):
    act = Act(id=aid, actor=CONFERRER, verb="confer", payload={"office": SEAT, "to": to}, via=VIA)
    return [e.kind for e in d.resolve(mint_token(w, WriteClass.ACTS), [act],
                                      contest_max_depth=w.fixtures.get("contest_max_depth"))]


def test_cohort_cannot_be_named_heir():
    """G1: the King confers a seat on a cohort (a person at `weight > 1`): `confer.refused`, nothing opened. CONTROL: the same
    act, same seat, same seat exercised, on an individual: `tenure.opened` and he holds it."""
    w, d = _gov_world()
    P.plant_cohort(w, COHORT, "S", weight=3)
    assert w.persons[COHORT].is_cohort and not w.persons[INDIVIDUAL].is_cohort, "fixture: no cohort beside an individual"
    kinds = _confer(w, d, COHORT, "elig_cohort")
    assert "confer.refused" in kinds and "tenure.opened" not in kinds, kinds
    assert _hold(w, SEAT) is None, "a cohort was seated"
    kinds = _confer(w, d, INDIVIDUAL, "elig_person")
    assert "tenure.opened" in kinds and "confer.refused" not in kinds, kinds
    assert _hold(w, SEAT).subject == INDIVIDUAL, "the control: an individual conferee was not admitted"
