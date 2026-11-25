"""B11.03 -- the cut arm of `audits/16_PESSIMIST_FI.md` §1.1, read against the shipped season.

`run_arm(seed, seasons, arm)` builds the realm, applies the arm, plays the seasons through
`harness/aperture.py::instrumented_season` (the instrument that already counts per verb, the one
`measure_world` wraps) and returns the per-verb census (attempted, executed) and the `told_by` claim count.

  ship     -- nothing changed.
  nod3     -- `interview`, `reconstruct` and `thread_read` out of the chooser's verb set.

The audit's other two arms (`draw1`, the chooser's draw seed changed; `nochron`, the public-record channel forced off) were run here and read by no assertion
and no other file, so they were dropped at the B11 close: a re-run nobody reads observes nothing. `harness/arms.py` is the n-seed instrument.

The arm is applied through `harness/probes.py::chooser`, the one name `instrumented_season` composes its chooser
from, so the measured season is the shipped one with the arm's single change. The test reports; it asserts no spread.
"""

from __future__ import annotations

import pytest

from ..boot.realm import build_realm
from ..harness import aperture, probes as P
from ..loop.driver import resolvable_verbs

ARMS = ("ship", "nod3")
NOD3 = frozenset({"interview", "reconstruct", "thread_read"})


def run_arm(seed: int, seasons: int, arm: str) -> dict:
    """`{"attempted": {verb: n}, "executed": {verb: n}, "told_by": n}` for `arm` at (`seed`, `seasons`).
    The arm's one change is undone when the call returns, so arms never stack."""
    assert arm in ARMS, arm
    w = build_realm(seed)
    base = P.chooser
    with pytest.MonkeyPatch.context() as mp:
        if arm == "nod3":
            mp.setattr(P, "chooser", lambda w_, verbs=None, **kw: base(
                w_, verbs=frozenset(resolvable_verbs() if verbs is None else verbs) - NOD3, **kw))
        m = aperture.instrumented_season(w, seasons)
    per_verb = lambda table: {v: sum(c.get(v, 0) for c in table.values()) for v in sorted(resolvable_verbs())}
    return {"attempted": per_verb(m["attempted"]), "executed": per_verb(m["executed"]),
            "told_by": sum(1 for p in w.persons.values() for c in p.ledger if c.source == "told_by")}


def test_arms_run_and_report():
    got = {arm: run_arm(0, 2, arm) for arm in ARMS}
    checked = 0
    keys = set(got["ship"]["attempted"])
    for arm, r in got.items():
        assert set(r["attempted"]) == keys == set(r["executed"]), arm
        assert all(r["executed"][v] <= r["attempted"][v] for v in keys), arm
        checked += 1
        print(f"ARM {arm:<8} told_by {r['told_by']:>6}  "
              + "  ".join(f"{v} {r['attempted'][v]}/{r['executed'][v]}" for v in ("march", "migrate")))
    assert checked == len(ARMS) == 2
    # THE CONTROL that lets the next line fail: the shipped season forms some of the three verbs, so "the cut arm formed none" is a cut and not an absence.
    assert {v for v in NOD3 if got["ship"]["attempted"][v]}, got["ship"]["attempted"]
    assert {v for v in NOD3 if got["nod3"]["attempted"][v]} == set()   # the cut arm formed none of what it cut
