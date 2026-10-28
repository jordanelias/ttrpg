"""v10 IN-18: `harness/obligee_report.py`, THE M0e READER (G5's trigger), on HAND-BUILT worlds.

The reader prints a figure and grades nothing (rule V2); what a realm run reads is NOT asserted here.
What is asserted is that the reader can SEE the thing it counts and that each clause of its definition
moves it: the same world reads 1 with `oblige` and 0 without it, 0 when the hearer is not the seat's
holder, 0 when the edge is not yet live at the tick of the telling, and 0 when its obligee test or
its seat-holder test is broken (the mutations, run in the tests below by patching the reader's own
helper, §0.1 pt 2).

The world is `probes.tiny_world` with the seat `off_duke` re-seated to `p_low`, who stands in `Hh`
with `p_mid` and `p_other` (a `tell` is refused unless the hearer stands with the teller, `hearer`),
so the obligee `p_mid` can tell the holder `p_low`.
"""

from __future__ import annotations

from ..data.matrix import Step, WriteClass
from ..harness import obligee_report as OR
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries.person_q import said_of
from ..seam import Resolution
from ..state.carriers import Act, Claim, Tenure

SEAT = "off_duke"
HOLDER, OBLIGEE, BYSTANDER = "p_low", "p_mid", "p_other"
TOPIC = "Hh"


def _world(obliged: bool = True, oblige_since: int = 0):
    w = P.tiny_world()
    for t in w.tenures:                       # re-seat: p_high leaves, p_low holds
        if t.kind == "hold" and t.object == SEAT:
            t.until = 0
    w.add_tenure(Tenure("t_hold_low", HOLDER, SEAT, "hold", since=0))
    if obliged:
        w.add_tenure(Tenure("t_oblige_mid", OBLIGEE, SEAT, "oblige", since=oblige_since))
    w.persons[OBLIGEE].ledger.append(
        Claim("c_held", OBLIGEE, TOPIC, "stores:grain", 8, 0, "firsthand", 37, "own"))
    return w


def _tell(w, to: str, actor: str = OBLIGEE, label: str = "x", lost: bool = False):
    """`actor` tells `to` what he holds on `TOPIC`, through the real fold: won (`news.told`) or `lost`
    (`news.untold`), logged and WITNESSED as the driver does it. Returns the Events."""
    kind = "news.untold" if lost else "news.told"
    d = SeasonDriver(w)
    w.step = Step.RESOLVE
    said = said_of(w.persons[actor].ledger, TOPIC, w.fixtures)
    a = Act(id=f"a_in18_{label}", actor=actor, verb="tell",
            payload={"subject": TOPIC, "to": to, "said": said})
    w.acts.append(a)
    out = d._fold(w, mint_token(w, WriteClass.ACTS), a, Resolution("Failure" if lost else "Success", {}))
    assert [e.kind for e in out] == [kind], [e.kind for e in out]
    w.log.extend(out)
    for e in out:
        d.act_of[e.id] = a
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return out


def test_in18_an_obligee_telling_his_seat_holder_reads_one_and_without_oblige_none():
    """THE FALSIFIER (the position's, G5 row): with the `oblige` edge the reader counts the telling
    (headline, attempted and heard); the SAME world and the SAME telling without the edge reads 0 on
    every line, while the telling itself is still seen (`tells_all == 1`) -- so the 0 is the missing
    duty and not a missing telling."""
    w = _world(obliged=True)
    _tell(w, HOLDER)
    r = OR.read_obligee_reports(w)
    assert (r.m0e, r.attempted, r.told_by, r.tells_all, r.tells_by_obligees) == (1, 1, 1, 1, 1), r.line()
    assert r.by_pair == {(OBLIGEE, SEAT, HOLDER): 1}
    assert (r.obligees, r.obligee_edges, r.edges_with_holder) == (1, 1, 1), r.line()

    w0 = _world(obliged=False)
    _tell(w0, HOLDER)
    r0 = OR.read_obligee_reports(w0)
    assert r0.tells_all == 1, "control: the telling was not made, so the 0 below proves nothing"
    assert (r0.m0e, r0.attempted, r0.told_by, r0.tells_by_obligees) == (0, 0, 0, 0), r0.line()


def test_in18_a_telling_to_anyone_but_the_seat_holder_is_not_a_report():
    """The hearer clause: the obligee tells the bystander (same rung, not the holder). It is an
    obligee's telling (`tells_by_obligees == 1`) and not a report (`m0e == 0`); the holder, standing
    there, overhears it, so the HEARD line still reads it -- which is why `m0e` is the headline."""
    w = _world(obliged=True)
    _tell(w, BYSTANDER)
    r = OR.read_obligee_reports(w)
    assert (r.tells_by_obligees, r.m0e, r.attempted) == (1, 0, 0), r.line()
    assert r.told_by == 1, "the holder overheard: the heard line is wider, as the module says"


def test_in18_a_lost_telling_is_attempted_and_is_not_a_report():
    """The told/untold clause, the branch the IN-18 verdict turns on: a `tell` the obligee LOST
    (`news.untold`, degree `Failure`) to his seat holder is an ATTEMPT (`attempted == 1`) and not a
    report (`m0e == 0`). Mutation: drop the `e.kind == TOLD` guard on `m0e` and it reads 1, which is
    G5's trigger firing on a telling nobody heard."""
    w = _world(obliged=True)
    _tell(w, HOLDER, label="lost", lost=True)
    r = OR.read_obligee_reports(w)
    assert (r.attempted, r.m0e, r.tells_all) == (1, 0, 0), r.line()
    assert sum(r.attempted_by.values()) == 1 and all(k[0] == "news.untold" for k in r.attempted_by)


def test_in18_an_edge_not_yet_live_at_the_telling_is_not_a_duty():
    """The tick window: an `oblige` opened at tick 5 does not make a tick-0 telling a report."""
    w = _world(obliged=True, oblige_since=5)
    _tell(w, HOLDER)
    r = OR.read_obligee_reports(w)
    assert r.tells_all == 1 and (r.m0e, r.told_by, r.tells_by_obligees) == (0, 0, 0), r.line()


def test_in18_the_reader_goes_red_when_its_obligee_or_seat_holder_test_is_broken(monkeypatch):
    """MUTATIONS (§0.1 pt 2): the reader must be able to see the failure it excludes. Break the
    liveness test (the window both the obligee and the holder are read through) and the world that
    reads 1 reads 0; the unbroken reader reads 1 again once restored."""
    w = _world(obliged=True)
    _tell(w, HOLDER)
    assert OR.read_obligee_reports(w).m0e == 1
    with monkeypatch.context() as m:
        m.setattr(OR, "_live_at", lambda t, tick: False)
        assert OR.read_obligee_reports(w).m0e == 0, "a broken window still counted"
    with monkeypatch.context() as m:       # only the HOLDER side broken: nobody holds the seat
        m.setattr(OR, "_live_at", lambda t, tick: t.kind != "hold")
        assert OR.read_obligee_reports(w).m0e == 0, "a seat with no holder still counted a report"
    with monkeypatch.context() as m:       # only the OBLIGEE side broken: nobody is obliged
        m.setattr(OR, "_live_at", lambda t, tick: t.kind != "oblige")
        assert OR.read_obligee_reports(w).m0e == 0, "an unobliged teller still counted"
    assert OR.read_obligee_reports(w).m0e == 1
