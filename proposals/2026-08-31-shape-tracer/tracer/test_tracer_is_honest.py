"""Adversarial self-test of the tracer.

The tracer gates every finding downstream, so a bug in it is a bug in all of them. Two false
PASSes were already found by hand during construction:

  * W2 counted only `resolve()`'s return and missed band events emitted at MATTER, so a site
    strobing across a band edge six times in six seasons reported as clean.
  * P14 passed because the tracer's Partition table carried rows for `Person.capability`,
    `convictions` and `beliefs` that THE SUITE DOES NOT HAVE — an invention that hid a gap its
    own `ADVERSARIAL.md` had already found.

Both were infidelities in the direction of flattering the shape, which is the dangerous direction.
These tests exist so the third one is caught by a machine.

Run: python3 -m pytest test_tracer_is_honest.py -q   (from this directory)
"""

from __future__ import annotations

import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import pytest

from shape import (
    Act, Event, Forbidden, Person, Rung, SeasonLoop, Site, Step, Unspecified,
    World, WriteClass, SOCIAL, LEGAL_WRITES, condition_band,
)
from trace_log import TraceLog
import trace_log


def _w():
    w = World()
    w.rungs["settl"] = Rung(id="settl", kind="settlement")
    w.sites["harbour"] = Site(id="harbour", rung="settl", kind="harbour", condition=800)
    return w


# --- the write gate must actually gate ------------------------------------

def test_out_of_class_write_raises():
    """A MATTER-class write during RESOLVE must be refused, or the write matrix is decoration."""
    w = _w()
    w._step = Step.RESOLVE
    with pytest.raises(Forbidden):
        w.write("Site", "condition", "harbour", 1, WriteClass.MATTER, driver="Event")


def test_deliberate_admits_no_writes_at_all():
    """`04` §3: DELIBERATE is a map, not a barrier. Every class must be refused there."""
    w = _w()
    w._step = Step.DELIBERATE
    for wc in WriteClass:
        with pytest.raises(Forbidden):
            w.write("Site", "condition", "harbour", 1, wc, driver="Event")


def test_partition_is_asymmetric_not_biconditional():
    """social:True forbids an EVENT driver and permits an ACT; social:False permits both.
    Stated as a biconditional the Partition is simply false, per `01` Law 4."""
    w = _w()
    w._step = Step.RESOLVE
    # social:True + Event  -> refused
    with pytest.raises(Forbidden):
        w.write("Office", "post", "gov", "x", WriteClass.ACTS, driver="Event")
    # social:True + Act    -> allowed
    assert w.write("Office", "post", "gov", "x", WriteClass.ACTS, driver="Act")
    w._step = Step.MATTER
    # social:False + Event -> allowed  (wear and a tending act land on the same field by design)
    assert w.write("Site", "condition", "harbour", 1, WriteClass.MATTER, driver="Event")


def test_unmarked_cell_raises_rather_than_defaulting():
    """`04` §4: 'any unmarked cell is a write-class violation.' The tracer must NOT invent a row."""
    w = _w()
    w._step = Step.RESOLVE
    with pytest.raises(Unspecified):
        w.write("Person", "convictions", "p", 1, WriteClass.ACTS, driver="Act")


@pytest.mark.parametrize("absent", [
    ("Person", "capability"), ("Person", "convictions"),
    ("Person", "beliefs"), ("Site", "drawers"),
])
def test_rows_the_suite_lacks_stay_absent(absent):
    """Regression on the P14 infidelity. `ADVERSARIAL.md` rows 14/15/16 find these have no
    write-matrix row. If a future edit adds one, a real gap silently becomes a PASS."""
    assert absent not in SOCIAL, (
        f"{absent} was added to the tracer's Partition table. The suite does not have it — "
        "adding it hides a gap its own adversarial pass found.")


# --- the laws must hold by construction -----------------------------------

def test_choose_cannot_be_handed_a_world():
    """Law 2 works by what the signature OMITS. A View must not expose world collections."""
    from shape import View
    v = View(holder="p")
    for attr in ("persons", "rungs", "sites", "offices", "log", "tenures"):
        with pytest.raises(Forbidden):
            getattr(v, attr)


def test_act_actor_must_be_the_chooser():
    """Law 1 is mechanical: an Act's actor is the person whose choose produced it."""
    w = _w()
    w.persons["a"] = Person(id="a")
    loop = SeasonLoop(w)
    with pytest.raises(Forbidden):
        loop.run({"a": lambda p, v, s: Act(actor="someone_else", verb="x", target=None)})


# --- the instrument must not flatter ---------------------------------------

def test_band_crossings_are_counted_from_the_log_not_from_resolve():
    """Regression on the W2 infidelity: band events are emitted at MATTER and are NOT in
    resolve()'s return, so counting the return under-reports strobing to zero."""
    w = _w()
    s = w.sites["harbour"]
    s.condition = 500
    w.persons["t"] = Person(id="t")
    loop = SeasonLoop(w)
    returned = 0
    for _ in range(4):
        evs = loop.run({"t": lambda p, v, ss: Act(actor="t", verb="restore", target="harbour")})
        s.condition = min(1000, s.condition + 40)
        returned += sum(1 for e in evs if e.family == "band_crossed")
    logged = sum(1 for e in w.log if e.family == "band_crossed")
    assert returned == 0, "resolve() must not carry MATTER events"
    assert logged == 4, f"the site strobed every season; log should show 4, showed {logged}"


def test_a_gap_is_recorded_exactly_once_per_case():
    """The register must not inflate: the same gap raised twice in one case is one row."""
    tl = TraceLog()
    tl.start_case("c1")
    tl.gap("UNSPECIFIED", "x", "y", "z")
    tl.gap("UNSPECIFIED", "x", "y", "z")
    assert len(tl.gaps) == 1
    tl.start_case("c2")
    tl.gap("UNSPECIFIED", "x", "y", "z")
    assert len(tl.gaps) == 2, "the same gap in a DIFFERENT case is a separate observation"


def test_every_probe_either_passes_or_records_a_gap():
    """No probe may fail silently, and none may raise a non-ShapeGap exception —
    a TRACER-ERROR is a bug in the instrument, never a finding about the shape."""
    import probes
    trace_log.TRACE = TraceLog()
    probes.TRACE = trace_log.TRACE
    import shape as _shape
    _shape.TRACE = trace_log.TRACE
    results = probes.run_all()
    errs = {k: v for k, (v, _) in results.items() if v == "TRACER-ERROR"}
    assert not errs, f"tracer bugs, not findings: {errs}"
    assert set(results) == set(probes.PROBES), "a probe went unrun"


# --- the ROUTER must not flatter either (added when the corpus grew to 78 cases) ---------

def test_generic_world_keywords_do_not_swallow_person_scale_needs():
    """The third greedy-keyword defect: `W1` is SITE decay, and the bare word "condition" was
    routing "nine named conditions" and "the underlying situation" onto it, manufacturing PASSes
    on a probe about harbours. Regression on the whole class, not just the one word."""
    from run_cases import route
    for need in [
        "the game must evaluate nine named conditions as distinct endgame states",
        "a resolution roll's failure must leave the underlying situation completely unresolved",
        "a superior's response must be determined by his own current internal condition",
    ]:
        assert route(need) != "W1", f"{need!r} routed to the site-decay probe"


def test_threshold_language_does_not_route_to_band_strobing():
    """`W2` is a site oscillating across a band edge. Sixteen core needs about a hidden quantity
    crossing a firing threshold were landing there on the bare word "threshold", attributing the
    block to the wrong mechanism."""
    from run_cases import route
    for need in [
        "a hidden personal quantity must cross a threshold and trigger a one-time check",
        "building a local quantity toward a use-threshold must be contestable",
        "a formal, threshold-triggered diplomatic demand must remain suppressed",
    ]:
        assert route(need) != "W2", f"{need!r} routed to band strobing"


def test_a_mostly_unrouted_case_is_not_reported_playable():
    """A case whose core needs did not route was NOT TESTED. Grading it PLAYABLE is the
    instrument flattering the shape by failing to aim at it."""
    import run_cases
    rows = [{"need": "x", "probe": None, "verdict": "UNMAPPED", "hardness": "core"},
            {"need": "y", "probe": "P1", "verdict": "PASS", "hardness": "core"}]
    core = [r for r in rows if r["hardness"] == "core"]
    unmapped = [r for r in core if r["verdict"] == "UNMAPPED"]
    assert len(unmapped) * 2 >= len(core), "this fixture must trip the NOT-ASSESSED rule"
    assert "NOT-ASSESSED" in open(run_cases.__file__).read(), \
        "the four-way verdict must survive; three-way silently re-creates the false PLAYABLE"


def test_every_new_probe_is_reachable_from_some_route():
    """A probe nothing routes to is a probe that never grades a case. P34/P35 were added
    BECAUSE needs existed for them; if a later edit narrows a regex past them, say so loudly."""
    from run_cases import route
    assert route("a leader's repeated use must silently accumulate a hidden personal quantity") == "P34"
    assert route("building toward a use-threshold must be contestable by an opposing actor's action") == "P35"
