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


def test_the_word_enforce_does_not_manufacture_a_pass():
    """Fourth greedy-keyword defect, found by an independent read-only audit rather than by me:
    "a policy he ENFORCES" routed to A17 (winning vs enforcing are separate events) and came back
    PASS, so a report claimed the King was blocked on a probe his own case had passed. A false
    PASS is the dangerous direction and this one also corrupted a downstream change list."""
    from run_cases import route
    assert route("a leader's own long-held private doubt about a policy he enforces must be able "
                 "to persist for many seasons without forcing a decision") == "P19"
    assert route("an enforcer's valued professional trait must become a liability") != "A17"
    # the genuine A17 shape must still route
    assert route("a formal contest with a trackable winner must produce a ruling entirely "
                 "separate from its implementation") == "A17"


def test_an_action_budget_need_is_not_a_spiral():
    """`A5` is a self-reinforcing loop. The King's "unaddressed ones COMPOUNDING" landed there on
    the word "compound" when the need is an action budget — Jordan's stated player model is ~5
    scenes and so ~5 acts per season, and the shape gives exactly one."""
    from run_cases import route
    assert route("a single leader must be able to face several independent, ongoing pressure "
                 "sources in one season and only be able to substantively address a subset of "
                 "them, with the unaddressed ones compounding rather than pausing") == "P36"


def test_choose_returns_exactly_one_act_which_is_the_finding_p36_reports():
    """P36 must rest on an executed property of the shape, not on a reading of it."""
    w = _w()
    w.persons["k"] = Person(id="k")
    calls = []

    def once(p, v, s):
        calls.append(p)
        return Act(actor="k", verb="tell", target="settl")

    SeasonLoop(w).run({"k": once})
    assert len(calls) == 1, ("the shape calls choose once per person per season; if this ever "
                             "returns >1 the action-budget finding is obsolete and P36 must go")


# --- the OTHER direction. Four defects flattered the shape; the fifth damned it. ------------

RULED_ROWS = {
    # (record-kind, field): (social, the ruling that fixes it)
    ("Tenure", "until"): (False, "`02` §5.1: 'RULED: (Tenure, until) is social: false. Otherwise "
                                 "death cannot end a tenure and the entire succession mechanism "
                                 "has no producer.' Called the Partition's ONE DECLARED SEAM."),
    ("Site", "condition"): (False, "`04` §4 matrix: MATTER writes it via `wear`."),
    ("Person", "stance"): (True, "`04` §4 matrix: RESOLVE only, act-driven."),
    ("Office", "post"): (True, "`04` §4 matrix: conferral/revocation are acts."),
}


@pytest.mark.parametrize("key,expected", [(k, v) for k, v in RULED_ROWS.items()])
def test_rows_the_suite_HAS_RULED_are_present_and_correct(key, expected):
    """Instrument defect five, and the first to point the DAMNING way.

    `test_rows_the_suite_lacks_stay_absent` guards against INVENTING a row — the flattering
    direction, which is the one four earlier defects took. Nothing guarded against OMITTING a
    row the suite has explicitly ruled, and that omission is worse: it makes a closed seam look
    open. `A12` reported for hours that a dead king still holds the crown, because this table
    lacked `(Tenure, until)` and the probe wrote `(Tenure, hold)` instead. That is a defect in
    the tracer reported as a defect in the shape, and it was found by an audit, not by me.
    """
    social, ruling = expected
    assert key in SOCIAL, f"{key} is RULED and MISSING from the tracer's Partition table. {ruling}"
    assert SOCIAL[key] is social, f"{key} is ruled social={social}. {ruling}"


def test_the_declared_seam_is_bounded_by_causation_not_by_the_column():
    """`02` §5.1: what stops a storm vacating a praefecture is NOT the column — it is the rule
    that an actorless row may write `until` only on a (Person, exists) change the same row
    caused. If the column alone gated it, social:false would let any Event end any tenure."""
    w = _w()
    w.persons["p"] = Person(id="p")
    w._step = Step.MATTER
    w._died_this_row = {"p"}
    assert w.write("Tenure", "until", "p", 1, WriteClass.MATTER, driver="Event")
    w._died_this_row = set()
    with pytest.raises(Forbidden):
        w.write("Tenure", "until", "p", 1, WriteClass.MATTER, driver="Event")


def test_the_two_most_expensive_routes_are_not_substring_matches():
    """`A2` prices Law 1's central refusal and `A13` prices the question that goes to Jordan, so
    a loose regex on either is the most expensive mistake in the router. Bare `counter` matched
    inside "counter-productive"; bare `ambient` matched "ambient environmental quality", which
    is MATTER and already served."""
    from run_cases import route
    assert route("behaviour objectively counter-productive to his own interests") != "A2"
    assert route("an unrelated, ambient environmental quality degrades") != "A13"
    assert route("the ambient world-health quantity's pre-existing band") != "A13"
    # and the genuine cases must survive the narrowing
    assert route("a private, monotonically-increasing counter reaching its ceiling") == "A2"
    assert route("a background quantity tied to a population's cultural situation must drift "
                 "toward a pole purely from the absence of any faction acting") == "A13"


def test_the_endings_classification_is_committed_parseable_and_agrees_with_execution():
    """§3.3's 19-of-50 carries the whole "the corpus wants a summons, not a firing counter"
    argument, and it is an AGENT CLASSIFICATION OF PROSE — the weakest evidence in the suite.
    Two things make it usable, and this test pins both.

    1. It is reproducible: the rows are committed with their deciding phrases, so any call can
       be checked by hand. It used to live only in a session transcript.
    2. It INDEPENDENTLY REPRODUCES the executed number. The classifier counted 8 arcs closing at
       a threshold with nobody deciding, having seen only `ends_when` strings. The runner counts
       8 arc `core` needs blocked by A2, having seen only probes. Two instruments looking at
       different things and landing on 8 is worth more than either alone — and it only became
       true after the A2 route was narrowed off the bare substring `counter`.
    """
    import yaml, json, collections, os
    here = os.path.dirname(os.path.abspath(__file__))
    rows = yaml.safe_load(open(os.path.join(here, "..", "cases", "ENDINGS_CLASSIFIED.yaml")))
    assert len(rows) == 50
    labels = collections.Counter(r["label"] for r in rows)
    assert labels["THRESHOLD"] == 8
    assert sum(1 for r in rows if r["forced_by_threshold"] is True) == 19
    assert all(r.get("phrase") for r in rows), "every call must carry its deciding phrase"

    res = json.load(open(os.path.join(here, "..", "results.json")))
    a2 = sum(1 for cid, c in res["cases"].items()
             if c["lane"].startswith("ARC") and cid != "ARC-META-COLLISION"
             for r in c["rows"] if r["probe"] == "A2" and r["hardness"] == "core"
             and r["verdict"] not in ("PASS", "PARTIAL", "UNMAPPED"))
    assert a2 == labels["THRESHOLD"], (
        f"the two instruments have diverged: classifier says {labels['THRESHOLD']} arcs close at "
        f"a threshold, runner says A2 blocks {a2}. One of them has drifted and the convergence "
        "that licenses citing the classification is gone.")
