"""B21.60 -- a seat is held by an individual (`16_PESSIMIST_FA_B` edit 1, G1; R-04 who may sit).

`state/gate.py::may_sit` is the one predicate: the person exists and is not a cohort. `confer`'s and `succeed`'s preconditions and
the write gate's `conferral` and `claim` clauses all ask it, so a cohort is refused at the fold (`confer.refused`) where the gate
would raise. Later positions of the item chain (B21.61 to B21.63) add their arms to this file.
"""
from __future__ import annotations

import pytest

from ..data.matrix import WriteClass
from ..data.verbs import VERB_TABLE
from ..harness import probes as P
from ..loop.driver import mint_token
from ..loop.sides import seat_named_by, sides_of
from .. import manifest
from ..seam.wrappers import sigma
from ..state.carriers import Act, Office
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


CHURCH_SEAT = "off_confessor"


def _church_world():
    """`_gov_world` plus `off_confessor`, an unheld seat of the Church at `S` (the King's `off_crown` is Crown's)."""
    w, d = _gov_world()
    w.offices[CHURCH_SEAT] = Office(CHURCH_SEAT, "Confessor", "S", ["issue"], faction="Church of Solmund", conferral="appointed",
                                    revocation=w.offices[SEAT].revocation)
    assert w.offices[VIA].faction != w.offices[CHURCH_SEAT].faction and w.offices[VIA].faction == w.offices[SEAT].faction, "fixture"
    return w, d


def _confer_on(w, d, seat, to, aid):
    act = Act(id=aid, actor=CONFERRER, verb="confer", payload={"office": seat, "to": to}, via=VIA)
    return [e.kind for e in d.resolve(mint_token(w, WriteClass.ACTS), [act],
                                      contest_max_depth=w.fixtures.get("contest_max_depth"))]


def _confer_terms(w, seat, to):
    """The obstacle terms of the roll the fold would deal for the King conferring `seat` on `to`: the fold's own derivation (`sides_of`,
    `seat_named_by`, the prize row's hearing) into `sigma.contest_input`, composed by the registered obstacle owner."""
    act = Act(id="elig_terms", actor=CONFERRER, verb="confer", payload={"office": seat, "to": to}, via=VIA)
    prize = VERB_TABLE["confer"].contests
    parties, subject, rung = sides_of(w, act, to, prize)
    row = manifest.resolve("contest", prize)
    inp = sigma.contest_input(w, parties, verb="confer", subject=subject, room=rung, via=VIA, heard_by=row["heard_by"],
                              seat=seat_named_by(w, act, prize))
    return dict(sigma._composed_terms(inp))


def test_cross_chain_term_reads_zero_at_control():
    """A `confer` across factions composes an obstacle that lists no `cross_chain` term at `cross_chain_step` 0 (the control, shipped: the
    obstacle of every `confer` is the one it had) and one step at 1; a `confer` inside one chain lists none at either."""
    w, _ = _church_world()
    shipped = w.fixtures
    assert shipped.get("cross_chain_step") == 0, "the shipped step is the control"
    assert "cross_chain" not in _confer_terms(w, CHURCH_SEAT, INDIVIDUAL), "a term listed at the control"
    w.fixtures = shipped.sweep("cross_chain_step", 1)
    across, within = _confer_terms(w, CHURCH_SEAT, INDIVIDUAL), _confer_terms(w, SEAT, INDIVIDUAL)
    assert across["cross_chain"] == 1.0, across
    assert "cross_chain" not in within, "a conferral inside one chain was priced"
    assert {k: v for k, v in across.items() if k != "cross_chain"} == within, "the step moved a term other than its own"


def test_self_conferral_across_chains_refused():
    """G2: the King (`off_crown`, a Crown seat) confers an unheld seat of another faction (`off_confessor`, the Church's) on
    HIMSELF: `confer.refused`, nothing opened. CONTROL: he confers a seat of his own chain (`off_reeve`, Crown) on himself --
    admitted as today -- and the same Church seat on another person is admitted too (the rule is about the conferrer's own chain)."""
    w, d = _church_world()
    kinds = _confer_on(w, d, CHURCH_SEAT, CONFERRER, "elig_self_across")
    assert "confer.refused" in kinds and "tenure.opened" not in kinds, kinds
    assert _hold(w, CHURCH_SEAT) is None, "he seated himself across chains"
    kinds = _confer_on(w, d, CHURCH_SEAT, INDIVIDUAL, "elig_other_across")
    assert "tenure.opened" in kinds and _hold(w, CHURCH_SEAT).subject == INDIVIDUAL, kinds
    kinds = _confer_on(w, d, SEAT, CONFERRER, "elig_self_within")
    assert "tenure.opened" in kinds and "confer.refused" not in kinds, kinds
    assert _hold(w, SEAT).subject == CONFERRER, "the control: a self-conferral inside one chain was not admitted"
