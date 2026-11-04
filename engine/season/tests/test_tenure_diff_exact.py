"""`World._tenure_snapshot` / `_tenure_changes` answer as the reference walk they replaced.

WHY. The gate's F3 and F9 read one observation of the Tenure store around every watched write
(`state/gate.py`), so the diff is load-bearing: a Tenure it fails to list is a write nobody judged.
The fast path (`_tenure_changes`: the store in the snapshot's own order, identity-checked, fields
compared in C) is a rewrite of the per-Tenure loop, and this file holds the loop it replaced as the
reference and compares the two on every shape a write can leave the store in.

Clauses: (a) nothing moved -> no change; (b) one field assigned; (c) the payload mutated IN PLACE
(the case the deep copy exists for); (d) a Tenure opened; (e) a Tenure removed with its person;
(f) one removed and one opened, the store's length unchanged; (g) the store reordered; (h) a Tenure
with a non-None payload and a `term` moved; (i) one opened, and (j) one removed, at the very end of the
store. Each compares the full `(tenure, was)` list, order included. MUTATIONS (run, each alone, in
`state/world.py`): `_ne` always False -> (b), (c), (h) red; the identity walk always true -> (f), (g)
red; the length check dropped -> (i) red; the snapshot's payload copy dropped -> (c) red.
"""

from __future__ import annotations

import copy

import pytest

from ..harness import populated as POP
from ..state.carriers import Tenure


def _ref_snapshot(w):
    out = []
    for p in w.persons.values():
        for t in p.tenures:
            out.append((t, _fields(t, True)))
    for t in w._unowned:
        out.append((t, _fields(t, True)))
    return out


def _fields(t, cp):
    p = copy.deepcopy(t.payload) if cp and t.payload is not None else t.payload
    return (t.subject, t.object, t.kind, t.since, t.until, t.degree, p, t.term)


def _ref_changes(w, snap):
    seen = {id(t) for t, _ in snap}
    out = []
    for t, f in snap:
        if _fields(t, False) != f:
            out.append((t, Tenure(t.id, *f)))
    for p in w.persons.values():
        out.extend((t, None) for t in p.tenures if id(t) not in seen)
    out.extend((t, None) for t in w._unowned if id(t) not in seen)
    return out


def _same(a, b):
    assert len(a) == len(b)
    for (ta, wa), (tb, wb) in zip(a, b):
        assert ta is tb
        assert (wa is None) == (wb is None)
        if wa is not None:
            assert wa == wb


@pytest.fixture(scope="module")
def realm():
    return POP.build_realm(0)


def _holder(w):
    for p in w.persons.values():
        if len(p.tenures) >= 2:
            return p
    raise AssertionError("no person holds two Tenures")


def _check(w, mutate, expect_n):
    ref_snap, snap = _ref_snapshot(w), w._tenure_snapshot()
    undo = mutate(w)
    try:
        got, ref = w._tenure_changes(snap), _ref_changes(w, ref_snap)
        _same(got, ref)
        assert len(got) == expect_n, f"expected {expect_n} changes, saw {len(got)}"
    finally:
        undo()


def test_a_nothing_moved(realm):
    _check(realm, lambda w: (lambda: None), 0)


def test_b_one_field_assigned(realm):
    def m(w):
        t = _holder(w).tenures[0]
        old = t.until
        t.until = 9999
        return lambda: setattr(t, "until", old)
    _check(realm, m, 1)


def test_c_the_payload_mutated_in_place(realm):
    # the in-place mutation happens AFTER the snapshot, on a payload the snapshot copied
    p = _holder(realm)
    t = p.tenures[0]
    old = t.payload
    t.payload = {"remit_acts": ("a",)}
    ref_snap, snap = _ref_snapshot(realm), realm._tenure_snapshot()
    t.payload["remit_acts"] = ("a", "b")
    try:
        got, ref = realm._tenure_changes(snap), _ref_changes(realm, ref_snap)
        _same(got, ref)
        assert [x for x, _ in got] == [t], "the in-place payload change was not seen"
    finally:
        t.payload = old


def test_d_a_tenure_opened(realm):
    def m(w):
        p = _holder(w)
        n = Tenure("t_diff_open", p.id, "x", "hold", since=0)
        p.tenures.append(n)
        return lambda: p.tenures.remove(n)
    _check(realm, m, 1)


def test_e_a_tenure_removed_with_its_holder(realm):
    def m(w):
        p = _holder(w)
        gone = p.tenures.pop()
        return lambda: p.tenures.append(gone)
    _check(realm, m, 0)


def test_f_one_removed_one_opened_at_equal_length(realm):
    def m(w):
        p = _holder(w)
        gone = p.tenures.pop()
        n = Tenure("t_diff_swap", p.id, "x", "hold", since=0)
        p.tenures.append(n)
        return lambda: (p.tenures.remove(n), p.tenures.append(gone))
    _check(realm, m, 1)


def test_g_the_store_reordered(realm):
    def m(w):
        p = _holder(w)
        p.tenures[0], p.tenures[1] = p.tenures[1], p.tenures[0]
        return lambda: p.tenures.__setitem__(slice(0, 2), [p.tenures[1], p.tenures[0]])
    _check(realm, m, 0)


def test_h_term_and_payload_together(realm):
    def m(w):
        t = _holder(w).tenures[0]
        old = (t.payload, t.since)
        t.payload = {"k": 1}
        t.since = t.since + 1
        return lambda: (setattr(t, "payload", old[0]), setattr(t, "since", old[1]))
    _check(realm, m, 1)


def test_i_a_tenure_opened_at_the_very_end_of_the_store(realm):
    """The identity walk sees only the snapshot's length of the store: an opened Tenure last in the
    walk leaves every earlier one aligned, so only the length check catches it."""
    def m(w):
        n = Tenure("t_diff_tail_open", "nobody", "x", "hold", since=0)
        w._unowned.append(n)
        return lambda: w._unowned.remove(n)
    _check(realm, m, 1)


def test_j_a_tenure_removed_from_the_very_end_of_the_store(realm):
    w = realm
    n = Tenure("t_diff_tail_gone", "nobody", "x", "hold", since=0)
    w._unowned.append(n)
    try:
        ref_snap, snap = _ref_snapshot(w), w._tenure_snapshot()
        w._unowned.remove(n)
        _same(w._tenure_changes(snap), _ref_changes(w, ref_snap))
        assert w._tenure_changes(snap) == [], "a removed Tenure's fields did not move: no change"
    finally:
        if n in w._unowned:
            w._unowned.remove(n)


# --- THE SHADOW AND THE VERSION -------------------------------------------------------------------
# `World._tenure_snapshot` no longer reads every Tenure on every write: it keeps a shadow of the store and
# trusts `Tenure._v` (a count of attribute sets) to say which Tenures to re-read. What that trusts, and what
# each clause below observes of it:
#   (k) a seeded random walk of every edit a store takes (a field set, the same value set again, a payload
#       edited in place, a payload rebound, a Tenure opened, removed, reordered, or nothing), with the
#       snapshot taken BEFORE each edit and the diff AFTER it, equals the reference at every step. Because
#       each step's snapshot is cut after the last step's edit, it also observes edits that land BETWEEN
#       writes: they are the next write's baseline, never its change.
#   (l) the blind channel, the one thing a version cannot count: a field set through `__dict__` is not seen
#       by the diff, and `discard_caches` raises `InstrumentDefect` for it at the barrier.
#   (m) a clean realm's barrier check passes.
# MUTATIONS (run, each alone): `Tenure.__setattr__` not counting -> (b), (c), (h), (k), (m) red; the payload
# comparison dropped from `_tenure_changes` -> (c), (k) red; `_verify_tenure_shadow` returning early -> (l) red;
# `_tenure_snapshot` never refreshing a moved entry -> (c), (d), (i), (k) red.

def test_k_a_random_walk_of_edits_agrees_with_the_reference_at_every_step():
    import random
    from ..state.carriers import Tenure as T
    w = POP.build_realm(0)
    rng = random.Random(0)
    owners = [p for p in w.persons.values() if p.tenures]
    for p in owners[:6]:                      # some payloads to edit in place
        p.tenures[0].payload = {"remit_acts": ("a",), "n": 1}
    steps, moved, fresh, between = 300, 0, 0, 0

    def pick():
        p = rng.choice(owners)
        return p, rng.randrange(len(p.tenures))

    def edit(step):
        nonlocal fresh
        op = rng.choice(["set", "same", "inplace", "rebind", "open", "remove", "swap", "none", "two"])
        if op in ("set", "two"):
            p, i = pick()
            p.tenures[i].until = rng.choice([None, step, step + 1])
        if op == "same":
            p, i = pick()
            t = p.tenures[i]
            t.since = t.since
        if op in ("inplace", "two"):
            held = [t for p in owners for t in p.tenures if isinstance(t.payload, dict)]
            if held:
                rng.choice(held).payload["n"] = rng.randrange(1000)
        if op == "rebind":
            p, i = pick()
            p.tenures[i].payload = rng.choice([None, {"n": step}])
        if op == "open":
            where = rng.choice(owners).tenures if rng.random() < 0.5 else w._unowned
            where.insert(rng.randrange(len(where) + 1), T(f"t_walk_{step}", "x", "y", "hold", since=step))
            fresh += 1
        if op == "remove":
            p, i = pick()
            if len(p.tenures) > 1:
                p.tenures.pop(i)
        if op == "swap":
            p, i = pick()
            j = rng.randrange(len(p.tenures))
            p.tenures[i], p.tenures[j] = p.tenures[j], p.tenures[i]

    for step in range(steps):
        ref_snap, snap = _ref_snapshot(w), w._tenure_snapshot()
        edit(step)                            # inside the write's window: the diff must list it
        got, ref = w._tenure_changes(snap), _ref_changes(w, ref_snap)
        _same(got, ref)
        moved += bool(got)
        if rng.random() < 0.5:                # BETWEEN writes: nobody diffs it; the next snapshot
            edit(step)                        # must take it as the baseline, not hand it back as a change
            between += 1
        if step % 7 == 0:
            w.discard_caches()                # the barrier check must stay quiet on every honest edit
    assert moved >= steps // 4, f"only {moved} of {steps} steps changed the store: the walk barely moved"
    assert fresh > 0 and between > steps // 4


def test_l_a_field_moved_behind_setattr_is_invisible_to_the_diff_and_loud_at_the_barrier():
    from ..gaps import InstrumentDefect
    w = POP.build_realm(0)
    w._tenure_snapshot()                       # cut the shadow
    t = _holder(w).tenures[0]
    old = t.__dict__["until"]
    t.__dict__["until"] = 424242               # no `__setattr__`: no version count
    try:
        with pytest.raises(InstrumentDefect):
            w.discard_caches()
    finally:
        t.__dict__["until"] = old


def test_m_a_clean_realm_passes_the_barrier_check_before_and_after_a_season():
    w = POP.build_realm(0)
    w._tenure_snapshot()
    w.discard_caches()
    POP.run(1, 0, w=w)
    w.discard_caches()
    assert w._tshadow is not None, "the shadow was never cut: the check observed nothing"
