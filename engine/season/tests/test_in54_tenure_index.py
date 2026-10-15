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
  (d) `test_a_tenure_written_between_two_calls_in_one_barrier_window_is_seen` -- the mid-RESOLVE
      case: no `discard_caches()` between the calls, a Tenure opened, closed and reopened between
      them, and a knot likewise; every answer follows.

⚠ WHAT (a) CANNOT SEE, MEASURED: over the realm's two seasons no call has a CLOSED `hold` on the Event's
changed thing, so deleting the `t.live` clause from the index build leaves (a) green. The liveness
clause is observed by (d) alone, which closes and reopens an edge. Both are needed.

`test_no_bare_tenure_list_surgery_outside_the_store` is the sweep over the half of the version the
field-assignment counter cannot see (CLAUDE.md §0.1 pt 1, `tests/valoria/test_morale_write_sweep.py`'s
shape): production code adds and removes Tenures through `World` only.
"""

from __future__ import annotations

import ast
import pathlib

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
    """The point of the index: one build per version, not one per (event, person). The comparison
    in (a) would pass as well for an index rebuilt on every call."""
    total = sum(realm_run.checks.values())
    assert realm_run.builds >= 1, "the build was never counted: the wrapper is not on the call path"
    assert realm_run.builds * 10 < total, (realm_run.builds, total)


# -- (b) ---------------------------------------------------------------------------------------
def test_a_planted_stale_index_entry_fails_the_per_call_comparison(realm_run):
    w = realm_run.w
    w.discard_caches()
    idx = cache.tenure_index(w)
    pid, obj = "p_stale_holder", "off_stale"
    assert pid not in idx.holds
    key = "tenures@%d.%d" % w.tenure_version()
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
def test_a_tenure_written_between_two_calls_in_one_barrier_window_is_seen():
    w = P.tiny_world()
    doc = Event(id="e_doc", kind="k", changes=[P.about("off_dicastery")], causes=[ROOT], emitted_at=1)
    kn = Event(id="e_kn", kind="k", changes=[P.about("p_other")], causes=[ROOT], emitted_at=1)
    doc_key, wit_key = EP.CHANNEL_PREDICATES["document_key"], EP.CHANNEL_PREDICATES["witness_key"]

    # the window opens: the index is built and cached; NO discard_caches() from here on
    assert not doc_key(w, doc, "p_mid") and not wit_key(w, kn, "p_mid")
    built = set(w._barrier_cache)

    hold = w.add_tenure(Tenure("t_in54_hold", "p_mid", "off_dicastery", "hold", since=0))
    assert doc_key(w, doc, "p_mid"), "an opened hold was not seen (structure counter)"
    hold.until = 3
    assert not doc_key(w, doc, "p_mid"), "a closed hold was still answered (field counter)"
    hold.until = None
    assert doc_key(w, doc, "p_mid"), "a reopened hold was not seen"

    knot = w.add_tenure(Tenure("t_in54_knot", "p_mid", "p_other", "knot", since=0))
    assert wit_key(w, kn, "p_mid") and not wit_key(w, kn, "p_low")
    knot.until = 3
    assert not wit_key(w, kn, "p_mid")
    assert set(w._barrier_cache) - built, "the index was never rebuilt -- the clause above is vacuous"

    for pid in w.persons:
        for e in (doc, kn):
            assert disagreements(w, e, pid) == []


def test_the_version_counts_a_field_assignment_and_leaves_the_hash_alone():
    w = P.tiny_world()
    h = w.content_hash()
    before = w.tenure_version()
    t = next(iter(w.tenures))
    t.until = t.until                       # an assignment of the same value still counts
    assert w.tenure_version() != before
    assert w.content_hash() == h
    before = w.tenure_version()
    w._tenure_structure += 1
    assert w.tenure_version() != before and w.content_hash() == h


def test_a_tenure_added_with_no_field_write_after_the_build_is_seen():
    """The STRUCTURE half of the version: a Tenure constructed (a field write, counted) BEFORE the
    index is built, then added, moves only `_tenure_structure`. A knot, not an office hold: a hold
    passes through `_grant_remit`, which writes `payload` and would move `Tenure.writes` anyway.
    MUTATION (run): delete `self._tenure_structure += 1` in `World.add_tenure` -> red."""
    w = P.tiny_world()
    kn = Event(id="e_kn", kind="k", changes=[P.about("p_other")], causes=[ROOT], emitted_at=1)
    wit_key = EP.CHANNEL_PREDICATES["witness_key"]
    t = Tenure("t_in54_late_knot", "p_mid", "p_other", "knot", since=0)
    assert not wit_key(w, kn, "p_mid")          # the index is built here, at the post-construction version
    writes = w.tenure_version()[0]
    w.add_tenure(t)
    assert w.tenure_version()[0] == writes, "add_tenure wrote a field: this no longer isolates the structure counter"
    assert wit_key(w, kn, "p_mid"), "a Tenure added after the build was not seen (structure counter)"


# -- the half of the version the field counter cannot see ------------------------------------------
_MUTATORS = {"append", "extend", "insert", "remove", "pop", "clear", "sort", "reverse"}
_STORES = {"tenures", "_unowned"}
# shrink-only: the harness probes that build a world and then edit it by hand (`state/world.py` is
# the store itself and is exempt as a whole).
_ALLOWED = {"harness/probes.py": 1}


def _list_surgery(src: str) -> int:
    n = 0
    for node in ast.walk(ast.parse(src)):
        if isinstance(node, (ast.Assign, ast.AugAssign)):
            targets = node.targets if isinstance(node, ast.Assign) else [node.target]
            n += sum(isinstance(t, ast.Attribute) and t.attr in _STORES for t in targets)
        elif (isinstance(node, ast.Call) and isinstance(node.func, ast.Attribute)
              and node.func.attr in _MUTATORS and isinstance(node.func.value, ast.Attribute)
              and node.func.value.attr in _STORES):
            n += 1
    return n


def test_no_bare_tenure_list_surgery_outside_the_store():
    root = pathlib.Path(__file__).resolve().parents[1]
    found = {}
    for path in sorted(root.rglob("*.py")):
        rel = path.relative_to(root).as_posix()
        if rel.startswith("tests/") or rel == "state/world.py":
            continue
        n = _list_surgery(path.read_text(encoding="utf-8"))
        if n:
            found[rel] = n
    assert found == _ALLOWED, found


def test_the_sweep_can_see_a_planted_surgery_site():
    assert _list_surgery("def f(p, t):\n    p.tenures.append(t)\n") == 1
    assert _list_surgery("def f(p):\n    p.tenures = []\n") == 1
    assert _list_surgery("def f(w, t):\n    w.add_tenure(t)\n") == 0
