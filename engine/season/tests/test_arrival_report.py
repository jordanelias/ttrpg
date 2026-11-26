"""B12a.16 (`07_SE_kernel_repairs` D, H-327): ARRIVING TEACHES THE TRAVELLER THE PLACE, behind the fixture `arrival_report` (`loop/matter.py`).

THE ARM. MATTER's `travel.ended` write is the arrival. At `arrival_report: on` it carries `observed=_arrival_report(...)`: at most two
`Observation`s about the rung the traveller now stands in -- `(rung, "stores:<default_store_kind>", units)` as `_stock_report` builds it,
and `(rung, "held_by", the holder's id)` read through `world_q.governing_hold` -- and WITNESS deposits them to the write's witnesses, the
traveller among them. `off` (shipped) is the control: the write carries nothing, as before the item (read once at B12a.16, not kept).

THE WORLD is `probes.tiny_world`: `p_low` lives in `Hh`, moves to `S` (which holds grain 40 and, planted by the holder test, a `hold`); `p_high`
stands in `S`; `p_mid` stays in `Hh`.

THE FALSIFIERS, each able to see what it excludes: the claim lands only in a co-located resident's ledger (the traveller's holds none);
every ledger in the world gets it (the stayer's does); the holder line is deposited with no holder, or without the hold's holder when there
is one. The `off` control (the write carries nothing; the base hash) was read once at B12a.16 and is not kept as a test.
"""

from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Act, Tenure

TRAVELLER, RESIDENT, STAYER = "p_low", "p_high", "p_mid"   # `Hh`, `S`, `Hh` at build
STORES = "stores:grain"


def _world(**fx):
    """`tiny_world` at the given arms, its tick-0 MATTER barrier run, and `p_low`'s `move` to `S` folded."""
    fixtures = DEFAULT_FIXTURES
    for name, value in fx.items():
        fixtures = fixtures.sweep(name, value)
    w = P.tiny_world(fixtures)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _arrive(w, d):
    """The move to `S` folded, then the next season's MATTER (it ends the leg: `travel.ended`) and WITNESS over its Events. Returns them."""
    out = d.resolve(mint_token(w, WriteClass.ACTS), [Act(id="m1", actor=TRAVELLER, verb="move", payload={"to": "S"})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    assert [e.kind for e in out] == ["travel.moved"], [e.kind for e in out]
    w.tick += 1
    events = d.matter(mint_token(w, WriteClass.MATTER), [])
    d.witness(mint_token(w, WriteClass.INTERIOR), events)
    return events


def _about(w, pid, subject, predicate):
    return [c for c in w.persons[pid].ledger if c.subject == subject and c.predicate == predicate]


def test_an_arrival_with_the_report_on_deposits_the_places_stores_to_the_traveller():
    w, d = _world(arrival_report="on")
    assert not _about(w, TRAVELLER, "S", STORES), "the traveller held a claim about S's stores before he arrived"
    events = _arrive(w, d)
    (ended,) = [e for e in events if e.kind == "travel.ended"]
    # the units are what `S` holds when the leg ends: the larder and yield passes run before the travel pass and nothing writes `stores` after it
    units = w.rungs["S"].stores["grain"]
    assert units != 40, "the world did not move S's stores, so the reading cannot tell the leg's end from the opening stock"
    assert [(o.subject, o.predicate, o.value) for o in ended.observed if o.predicate == STORES] == [("S", STORES, units)], ended.observed
    held = _about(w, TRAVELLER, "S", STORES)
    assert [c.value for c in held] == [units], [(c.subject, c.predicate, c.value) for c in w.persons[TRAVELLER].ledger]
    # the falsifier's arm: a claim in the co-located resident's ledger ALONE would pass the line above for the wrong reason, so the
    # control is the person who stood elsewhere, who learned nothing of S
    assert not _about(w, STAYER, "S", STORES), "the stayer in `Hh` learned S's stores from a journey he did not make"


def test_an_arrival_reports_who_holds_the_place_through_the_governing_hold():
    """`S` is held by `p_high` (planted: `tiny_world` holds only an office). The hold is read on the rung's own ancestry, so a traveller to `S`
    is told `(S, held_by, p_high)`; with no hold on `S` or above it the holder is `None`, which WITNESS never deposits (the stores line still is)."""
    w, d = _world(arrival_report="on")
    w.add_tenure(Tenure("t_hold_s", "p_high", "S", "hold", since=0))
    events = _arrive(w, d)
    (ended,) = [e for e in events if e.kind == "travel.ended"]
    assert [o.value for o in ended.observed if o.predicate == "held_by"] == ["p_high"], ended.observed
    assert [c.value for c in _about(w, TRAVELLER, "S", "held_by")] == ["p_high"]

    w2, d2 = _world(arrival_report="on")
    events = _arrive(w2, d2)
    (ended,) = [e for e in events if e.kind == "travel.ended"]
    assert [o.value for o in ended.observed if o.predicate == "held_by"] == [None], ended.observed
    assert not _about(w2, TRAVELLER, "S", "held_by")
    assert _about(w2, TRAVELLER, "S", STORES), "the stores line is deposited whether or not the place is held"
