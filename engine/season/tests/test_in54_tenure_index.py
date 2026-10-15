"""IN-54 -- the object-side Tenure index (`queries/cache.py::tenure_index`) and the two channel
predicates that read it, `epistemic._ch_document_key` and `epistemic._ch_witness_key`.

What each clause observes, and what it is the falsifier of:

  (a) `test_the_index_answers_every_call_as_a_live_scan_does` -- over `populated.build_realm(0)`'s
      first two seasons, EVERY call either predicate receives is also put to the scan the predicate
      used to be (copied below, the oracle), and the two answers are equal. It asserts it checked
      (>= `MIN_CHECKS`) and that the answers were not all `False` (a comparison of two constants).
  (b) `test_a_planted_stale_index_entry_fails_the_per_call_comparison` -- the same comparison, handed
      an index with one entry the live store does not have, reports a disagreement.
  (c) `test_a_planted_change_to_a_channel_predicate_changes_the_fan_list` -- the control: the fan
      list `[(pid, event, channel)]` the comparison is about can be seen to move when a predicate
      moves.
  (d) `test_a_tenure_written_between_two_asks_is_seen_after_a_discard` -- the index is a
      PER-BARRIER cache, valid because every barrier calls `discard_caches()` first. A Tenure opened,
      closed and reopened between two asks is NOT seen without a discard (the cached answer comes
      back -- which shows the discard is what the design relies on) and IS seen after one; a knot
      likewise.

⚠ WHAT (a) CANNOT SEE, MEASURED: over the realm's two seasons no call has a CLOSED `hold` on the Event's
changed thing, so deleting the `t.live` clause from the index build leaves (a) green. The liveness
clause is observed by (d) alone, which closes and reopens an edge. Both are needed.
"""

from __future__ import annotations

import pytest

from .. import epistemic as EP
from ..harness import populated as POP
from ..harness import probes as P
from ..queries import cache
from ..state.attribution import anchor_of
from ..state.carriers import Event, Tenure
from ..state.ids import ROOT

MIN_CHECKS = 1000


# -- THE ORACLES: the two scans these predicates were, verbatim ----------------------------------
def scan_document_key(w, e, pid) -> bool:
    return any(t.kind == "hold" and t.subject == pid and t.object == c.subject and t.live
               for c in e.changes if c.subject
               for t in w.tenures)


def scan_witness_key(w, e, pid) -> bool:
    anchor = anchor_of(w, e)
    if anchor is None:
        return False
    if pid == anchor:
        return True
    return any(t.kind == "knot" and t.live and pid in (t.subject, t.object)
               and anchor in (t.subject, t.object) for t in w.tenures)


ORACLES = {"document_key": scan_document_key, "witness_key": scan_witness_key}


def disagreements(w, e, pid) -> list:
    """Every predicate whose INDEX answer differs from its live scan, for this (event, person)."""
    out = []
    for name, scan in ORACLES.items():
        got = EP.CHANNEL_PREDICATES[name](w, e, pid)
        want = scan(w, e, pid)
        if got != want:
            out.append((name, e.id, pid, got, want))
    return out


class _Run:
    pass


@pytest.fixture(scope="module")
def realm_run():
    """Two seasons of seed 0, with both predicates wrapped so each call is compared to its scan."""
    run = _Run()
    run.checks = {"document_key": 0, "witness_key": 0}
    run.true = {"document_key": 0, "witness_key": 0}
    run.mismatches = []
    originals = {n: EP.CHANNEL_PREDICATES[n] for n in ORACLES}

    def wrap(name):
        index_fn, scan = originals[name], ORACLES[name]

        def wrapped(w, e, pid):
            got = index_fn(w, e, pid)
            want = scan(w, e, pid)
            run.checks[name] += 1
            run.true[name] += bool(got)
            if got != want:
                run.mismatches.append((name, e.id, pid, got, want))
            return got
        return wrapped

    run.builds = 0
    build = cache._build_tenure_index

    def counted_build(w):
        run.builds += 1
        return build(w)

    for n in ORACLES:
        EP.CHANNEL_PREDICATES[n] = wrap(n)
    cache._build_tenure_index = counted_build
    try:
        w = POP.build_realm(0)
        POP.run(seasons=2, seed=0, w=w)
    finally:
        EP.CHANNEL_PREDICATES.update(originals)
        cache._build_tenure_index = build
    run.w = w
    return run


# -- (a) ---------------------------------------------------------------------------------------
def test_the_index_answers_every_call_as_a_live_scan_does(realm_run):
    assert not realm_run.mismatches, realm_run.mismatches[:5]
    for name, n in realm_run.checks.items():
        assert n >= MIN_CHECKS, f"{name}: only {n} calls were compared -- the comparison is a no-op"
        assert realm_run.true[name] > 0, f"{name}: every compared answer was False"


def test_the_index_is_built_far_less_often_than_it_is_asked(realm_run):
    """The point of the index: one build per barrier, not one per (event, person). The comparison
    in (a) would pass as well for an index rebuilt on every call."""
    total = sum(realm_run.checks.values())
    assert total >= MIN_CHECKS, f"only {total} asks were counted -- the ratio below is vacuous"
    assert realm_run.builds >= 1, "the build was never counted: the wrapper is not on the call path"
    assert realm_run.builds * 10 < total, (realm_run.builds, total)


# -- (b) ---------------------------------------------------------------------------------------
def test_a_planted_stale_index_entry_fails_the_per_call_comparison(realm_run):
    w = realm_run.w
    w.discard_caches()
    idx = cache.tenure_index(w)
    pid, obj = "p_stale_holder", "off_stale"
    assert pid not in idx.holds
    key = "tenures"
    e = Event(id="e_stale", kind="k", changes=[P.about(obj)], causes=[ROOT], emitted_at=1)
    assert disagreements(w, e, pid) == [], "fixture: the clean index already disagrees"
    w._barrier_cache[key] = cache.TenureIndex({**idx.holds, pid: frozenset({obj})}, idx.knots)
    try:
        assert [d[0] for d in disagreements(w, e, pid)] == ["document_key"]
    finally:
        w.discard_caches()
    assert disagreements(w, e, pid) == [], "the control did not restore"


# -- (c) ---------------------------------------------------------------------------------------
def test_a_planted_change_to_a_channel_predicate_changes_the_fan_list(realm_run, monkeypatch):
    w = realm_run.w
    events = list(w.log)[::10]
    everyone = list(w.persons)

    def fan():
        w.discard_caches()
        return [(pid, e.id, ch) for e in events
                for pid, ch in EP.observers_for(w, e, "all_five", everyone)]

    base = fan()
    assert base, "fixture: the sampled events fan to nobody"
    monkeypatch.setitem(EP.CHANNEL_PREDICATES, "witness_key", lambda w, e, pid: True)
    assert fan() != base, "a predicate that admits everybody left the fan list unchanged"
    monkeypatch.undo()
    assert fan() == base


# -- (d) ---------------------------------------------------------------------------------------
def test_a_tenure_written_between_two_asks_is_seen_after_a_discard():
    """The direct-caller contract `queries/cache.py` states: a Tenure write between two asks is seen
    after `w.discard_caches()`, and NOT without it. Each write is checked both ways -- the stale
    answer first, then the discarded one -- so the discard is shown to be the whole of what keeps
    the answer current. MUTATION (run): delete the `w.discard_caches()` calls below -> red."""
    w = P.tiny_world()
    doc = Event(id="e_doc", kind="k", changes=[P.about("off_dicastery")], causes=[ROOT], emitted_at=1)
    kn = Event(id="e_kn", kind="k", changes=[P.about("p_other")], causes=[ROOT], emitted_at=1)
    doc_key, wit_key = EP.CHANNEL_PREDICATES["document_key"], EP.CHANNEL_PREDICATES["witness_key"]

    def after_write(pred, e, pid, want):
        assert pred(w, e, pid) is (not want), "no discard yet: the cached answer should still stand"
        w.discard_caches()
        assert pred(w, e, pid) is want, "after discard_caches() the write was not seen"

    assert not doc_key(w, doc, "p_mid") and not wit_key(w, kn, "p_mid")   # the index is built here

    hold = w.add_tenure(Tenure("t_in54_hold", "p_mid", "off_dicastery", "hold", since=0))
    after_write(doc_key, doc, "p_mid", True)            # an opened hold
    hold.until = 3
    after_write(doc_key, doc, "p_mid", False)           # a closed hold (the `t.live` clause)
    hold.until = None
    after_write(doc_key, doc, "p_mid", True)            # a reopened hold

    knot = w.add_tenure(Tenure("t_in54_knot", "p_mid", "p_other", "knot", since=0))
    after_write(wit_key, kn, "p_mid", True)
    assert not wit_key(w, kn, "p_low")
    knot.until = 3
    after_write(wit_key, kn, "p_mid", False)

    w.discard_caches()
    for pid in w.persons:
        for e in (doc, kn):
            assert disagreements(w, e, pid) == []
