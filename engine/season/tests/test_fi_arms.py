"""B11.03 -- the four arms of `audits/16_PESSIMIST_FI.md` §1.1 and §1.3, restated as fixture sweeps.

`run_arm(seed, seasons, arm)` builds the realm, applies the arm, plays the seasons through
`harness/aperture.py::instrumented_season` (the instrument that already counts per verb, the one
`measure_world` wraps) and returns the per-verb census (attempted, executed) and the `told_by` claim count.

  ship     -- nothing changed.
  draw1    -- the shipped world with only the chooser's draw seed changed (`boot/chooser.py::chooser(draw_seed=1)`).
  nod3     -- `interview`, `reconstruct` and `thread_read` out of the chooser's verb set.
  nochron  -- `CHANNEL_PREDICATES["chronicle"]` forced False, everything else shipped.

The arm is applied through `harness/probes.py::chooser`, the one name `instrumented_season` composes its chooser
from, so the measured season is the shipped one with the arm's single change. The test reports; it asserts no spread.
Later items of the batch (B11.04's reach table) read their readings against this file's `ship` and `nochron` rows.
"""

from __future__ import annotations

import pytest

from .. import epistemic as EP
from ..boot.realm import build_realm
from ..harness import aperture, probes as P
from ..loop.driver import resolvable_verbs

ARMS = ("ship", "draw1", "nod3", "nochron")
NOD3 = frozenset({"interview", "reconstruct", "thread_read"})


def run_arm(seed: int, seasons: int, arm: str) -> dict:
    """`{"attempted": {verb: n}, "executed": {verb: n}, "told_by": n}` for `arm` at (`seed`, `seasons`).
    The arm's one change is undone when the call returns, so arms never stack."""
    assert arm in ARMS, arm
    w = build_realm(seed)
    base = P.chooser
    with pytest.MonkeyPatch.context() as mp:
        if arm == "draw1":
            mp.setattr(P, "chooser", lambda w_, **kw: base(w_, draw_seed=1, **kw))
        elif arm == "nod3":
            mp.setattr(P, "chooser", lambda w_, verbs=None, **kw: base(
                w_, verbs=frozenset(resolvable_verbs() if verbs is None else verbs) - NOD3, **kw))
        elif arm == "nochron":
            mp.setitem(EP.CHANNEL_PREDICATES, "chronicle", lambda w_, e, pid: False)
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
    assert checked == 4
    assert {v for v in NOD3 if got["nod3"]["attempted"][v]} == set()   # the cut arm formed none of what it cut
