"""v10 CR-23 (M17 taken (a), `H-243`, [ASSUMPTION; medium; Jordan to correct; revert: `stock_report = off`]):
A LARDER'S STOCK REACHES THE SEATS OVER IT, AT ITS CROSSINGS.

`queries/world_q.py::requisitionable` is the one owner of the stocked test (`held > 0 and held >= amount`, the
fixtures' kind and amount); `larders_in_purview` routes through it. `loop/matter.py::_stock_report` puts
`Observation(rung, "stores:<default_store_kind>", units after)` on MATTER's last actorless `stores` write to a
rung in the barrier (the credit where the rung yields, else the debit) -- at `crossing` only when
`requisitionable` at the barrier's entry differs from after, at `season` on every such write, at `off` never.
WITNESS is unchanged: IN-22's seat route deposits the read to `world_q.governors_of`, so a governor who neither
stands at nor holds the larder learns its name, `larders_in_purview` stamps it, and `requisition` forms on it.

Hand-built worlds only (`probes.tiny_world`): the realm reading is `aperture 4 0`'s, recorded at CR-23's commit and
on `H-243`, not asserted here (v9 §0.5). THE HEARTH WORLD moves both of tiny_world's sites onto the hearth `Hh`
and empties its larder, so the hearth's first yield is a crossing and the Duke -- who stands at `S` and holds
`off_duke` on `D`, whose purview contains `Hh` -- is told of it only by the seat route.

MUTATIONS, run at the build (2026-10-30); each went RED, then was restored byte-exact and went GREEN:
  * `larders_in_purview` given back its own inline stocked test (`held > 0 and held >= amount`) instead of
    `requisitionable(w, r)` -> `test_cr23_a` RED (the patched owner no longer decides what is offered);
  * `_stock_report`'s `crossing` test dropped (report on every write) -> `test_cr23_a` and `test_cr23_b` RED (the
    stocked-before-and-after hearth reports under `crossing`, whatever the owner says);
  * the stock report removed from the credit write (`observed=` dropped there) -> `test_cr23_b`, `test_cr23_c` and
    `test_cr23_e` RED (no claim reaches the Duke; nothing is stamped; no requisition forms; `crossing` reads `off`).
"""
from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..data.requires import Observation
from ..gaps import Unspecified
from ..harness import probes as P
from ..loop import matter as _matter
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Claim
from .test_u7_remit import DUKE, SEAT, TREASURY, _computed_requisitions, _fold, _kinds

HEARTH = "Hh"
KIND = DEFAULT_FIXTURES.get("default_store_kind")


def _hearth_world(mode="crossing", hearth_stores=None):
    """`tiny_world` at `stock_report = mode`, both sites moved onto `Hh` (so it yields and `S` writes nothing)
    and `Hh`'s larder set to `hearth_stores` (empty by default) before the first MATTER barrier."""
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("stock_report", mode))
    for s in w.sites.values():
        s.rung = HEARTH
    w.rungs[HEARTH].stores = dict(hearth_stores or {})
    return w, SeasonDriver(w)


def _barrier(w, d):
    """One MATTER barrier and the WITNESS fan-out of its Events (round 0's, as `SeasonDriver.season` runs it)."""
    events = d.matter(mint_token(w, WriteClass.MATTER), [])
    d.witness(mint_token(w, WriteClass.INTERIOR), events)
    return events


def _reads_on(events, rung):
    """The `observed` of the `stores.changed` Events MATTER wrote on `rung`."""
    return [e.observed for e in events
            if e.kind == "stores.changed" and any(c.subject == rung for c in e.changes)]


def _stock_claims(p, rung):
    return [(c.predicate, c.value, c.source) for c in p.ledger
            if c.subject == rung and str(c.predicate).startswith("stores:")]


def test_cr23_a_requisitionable_is_the_one_stocked_test(monkeypatch):
    """THE EXTRACTED PREDICATE. `larders_in_purview` offers exactly what `requisitionable` calls stocked, and
    MATTER's report crosses on the same predicate: patch the owner and both follow. A second, inline stocked
    test in `larders_in_purview` would keep offering the stocked larder under a patched-False owner, or keep
    refusing the empty one under a patched-True owner."""
    w, _ = _hearth_world(hearth_stores={KIND: 40})
    duke = w.persons[DUKE]
    duke.ledger.append(Claim("c_told_Hh", DUKE, HEARTH, "stores.changed", True, w.tick, "firsthand", 100,
                             "own"))
    assert world_q.requisitionable(w, HEARTH)
    assert world_q.larders_in_purview(w, duke) == (HEARTH,)           # anti-vacuity
    with monkeypatch.context() as m:
        m.setattr(world_q, "requisitionable", lambda w_, r, stores=None: False)
        assert world_q.larders_in_purview(w, duke) == ()
        w.rungs[HEARTH].stores = {}
        m.setattr(world_q, "requisitionable", lambda w_, r, stores=None: True)
        assert world_q.larders_in_purview(w, duke) == (HEARTH,)
    assert world_q.larders_in_purview(w, duke) == ()                  # the empty larder, the real owner
    # MATTER asks the same owner: an owner that calls nothing below 1000 stocked sees no crossing at the yield.
    w2, d2 = _hearth_world()
    with monkeypatch.context() as m:
        m.setattr(world_q, "requisitionable", lambda w_, r, stores=None: (
            (w_.rungs[r].stores if stores is None else stores) or {}).get(KIND, 0) >= 1000)
        events = _barrier(w2, d2)
    assert w2.rungs[HEARTH].stores.get(KIND, 0) > 0                   # anti-vacuity: the hearth did yield
    assert _reads_on(events, HEARTH) == [()]


@pytest.mark.parametrize("mode, before, reported", [
    ("crossing", {}, True),             # empty -> stocked: a crossing
    ("crossing", {KIND: 8}, False),      # stocked -> stocked: none
    ("season", {KIND: 8}, True),         # every last write
    ("off", {}, False),                  # never (the control)
])
def test_cr23_b_the_report_rides_the_last_write_with_the_level_it_leaves(mode, before, reported):
    """The yield's credit is the hearth's last write in the barrier, and the report is its one `stores:<kind>`
    read, valued at the units the write leaves."""
    w, d = _hearth_world(mode, before)
    events = d.matter(mint_token(w, WriteClass.MATTER), [])
    (seen,) = _reads_on(events, HEARTH)
    after = w.rungs[HEARTH].stores.get(KIND, 0)
    assert after > before.get(KIND, 0)                                 # anti-vacuity: it yielded
    assert seen == ((Observation(HEARTH, f"stores:{KIND}", after),) if reported else ()), seen


def test_cr23_b2_a_debit_that_empties_the_larder_reports_on_the_debit_after_the_shortfall():
    """No yield at the hearth (tiny_world's sites stay at `S`), and a cohort there eats it dry: the DEBIT is
    the last write, so the report rides it, after the shortfall it already carried (`19d`), valued 0. Under
    `off` the debit carries the shortfall alone, as before CR-23."""
    reads = {}
    for mode in ("crossing", "off"):
        w = P.tiny_world(DEFAULT_FIXTURES.sweep("stock_report", mode))
        w.persons["p_mid"].weight = 50                                 # a cohort: only a cohort eats (24f)
        assert world_q.requisitionable(w, HEARTH)                      # anti-vacuity: stocked at entry
        events = SeasonDriver(w).matter(mint_token(w, WriteClass.MATTER), [])
        assert w.rungs[HEARTH].stores.get(KIND, 0) == 0
        (reads[mode],) = _reads_on(events, HEARTH)
    shortfall = reads["off"]
    assert shortfall and all(o.predicate.startswith("shortfall:") for o in shortfall), shortfall
    assert reads["crossing"] == shortfall + (Observation(HEARTH, f"stores:{KIND}", 0),)


def test_cr23_b3_a_rung_both_debited_and_yielding_reports_on_neither_write_when_it_ends_as_stocked_as_it_began():
    """THE DEBIT-AND-YIELD BRANCH (`loop/matter.py`: `if rid not in yielded:` on the debit). The hearth yields AND a
    cohort eats at it, so MATTER writes it twice -- the debit, then the credit, the credit being the LAST. The
    larder is stocked at the barrier's entry, drained to 0 by the debit and refilled by the credit, so under
    `crossing` it is stocked before and after and NEITHER write reports a `stores:<kind>` read. A debit that
    reported anyway would be judged at the mid-state and tell a seat a stocked larder is empty."""
    w, d = _hearth_world("crossing", {KIND: 8})
    w.persons["p_mid"].weight = 50                                     # a cohort: only a cohort eats (24f)
    assert world_q.requisitionable(w, HEARTH)                          # anti-vacuity: stocked at entry
    events = d.matter(mint_token(w, WriteClass.MATTER), [])
    reads = _reads_on(events, HEARTH)
    assert len(reads) == 2, reads                                      # anti-vacuity: the debit AND the credit
    assert world_q.requisitionable(w, HEARTH)                          # stocked at exit
    assert not [o for r in reads for o in r if str(o.predicate).startswith("stores:")], reads


def test_cr23_c_the_report_reaches_the_seat_and_a_computed_requisition_executes_with_via():
    """THE CHAIN, ALL COMPUTED. The Duke neither stands at nor holds the hearth; the crossing's read reaches him
    by the seat route (`inferred`), `larders_in_purview` stamps the hearth, the real formation makes a
    `requisition` of it through his seat, and the real fold takes the fixtures' amount into the treasury."""
    w, d = _hearth_world()
    _barrier(w, d)
    duke = w.persons[DUKE]
    level = w.rungs[HEARTH].stores[KIND]
    assert _stock_claims(duke, HEARTH) == [(f"stores:{KIND}", level, "inferred")]
    assert world_q.larders_in_purview(w, duke) == (HEARTH,)
    (lv,) = _computed_requisitions(w)
    assert lv.payload.get("subject") == HEARTH and lv.via == SEAT, (lv.payload, lv.via)
    amount = w.fixtures.get("default_transfer_amount")
    before_d = (w.rungs[TREASURY].stores or {}).get(KIND, 0)
    assert _kinds(_fold(w, d, lv)) == ["requisition.taken"]
    assert w.rungs[HEARTH].stores[KIND] == level - amount
    assert w.rungs[TREASURY].stores[KIND] == before_d + amount


@pytest.mark.parametrize("plant", ["no observation at the flip", "off"])
def test_cr23_d_planted_failure_without_the_report_the_seat_is_never_told(plant, monkeypatch):
    """PLANTED FAILURE: `observed=()` at the flip (the report returns nothing), and the `off` arm -- the Duke holds
    no read of the hearth, nothing is stamped, and no `requisition` forms: the tree before CR-23."""
    if plant == "off":
        w, d = _hearth_world("off")
    else:
        monkeypatch.setattr(_matter, "_stock_report", lambda *a, **k: ())
        w, d = _hearth_world()
    _barrier(w, d)
    duke = w.persons[DUKE]
    assert world_q.requisitionable(w, HEARTH)                          # anti-vacuity: a stocked larder
    assert _stock_claims(duke, HEARTH) == []
    assert world_q.larders_in_purview(w, duke) == ()
    assert [a.payload.get("subject") for a in _computed_requisitions(w)] == []


def test_cr23_e_off_is_the_control_and_an_unknown_arm_refuses(monkeypatch):
    """`off` is the tree before CR-23 exactly (the content hash after a barrier equals the report-suppressed
    crossing arm's), the shipped arm is `crossing`, and an arm outside `rosters.yaml: stock_reports` refuses
    rather than reading as `off`."""
    assert DEFAULT_FIXTURES.get("stock_report") == "crossing"
    assert "crossing" in _matter.STOCK_REPORTS and "off" in _matter.STOCK_REPORTS   # the shipped arm, the control
    w_off, d_off = _hearth_world("off")
    _barrier(w_off, d_off)
    with monkeypatch.context() as m:
        m.setattr(_matter, "_stock_report", lambda *a, **k: ())
        w_cut, d_cut = _hearth_world()
        _barrier(w_cut, d_cut)
    w_on, d_on = _hearth_world()
    _barrier(w_on, d_on)
    assert w_off.content_hash() == w_cut.content_hash() != w_on.content_hash()
    w_bad, d_bad = _hearth_world("sometimes")
    with pytest.raises(Unspecified):
        d_bad.matter(mint_token(w_bad, WriteClass.MATTER), [])
