"""`state/ledgers` -- the eviction comparator, and the one function that applies it.

`04_CODE_ARCHITECTURE.md` §A.2:149 names this module as the owner of *"per-person packed claim
rows; the eviction comparator"*. This file extracts the SECOND half (2026-09-25): the comparator
was inlined in `loop/witness.py`'s eviction closure. It is a PURE MOVE -- same key, same sort, same
pops, so the same claims leave the same ledgers in the same order.

⚠ THE STORE SPLIT IS NOT HERE. The first half -- claim rows in a sub-store of their own, with a
write token distinct from conviction state (`04:117`, AX-3) -- needs the G2 token-type rewrite,
which does not exist yet. Until it does, `Person.ledger` stays on the carrier and every eviction
still goes through `World.write(... "claim_ledger" ...)`, the gate that applies it (AX-4); this
module is called INSIDE that write, never instead of it.
"""
from __future__ import annotations


def eviction_key(confidence: float, recency: int) -> float:
    """S20/S34: EVICTION RANKS ON `confidence_live x recency` ONLY, NEVER SALIENCE -- a product,
    not a lexicographic `(confidence, when)` tuple, which is a different comparator and
    degenerates to insertion order under a constant confidence. Lowest is evicted first."""
    return confidence * (recency + 1)


def evict_over_cap(ledger: list, cap: int) -> list:
    """Sort `ledger` in place by `eviction_key(c.confidence, c.when)` and pop from the front until
    `len(ledger) <= cap`. Returns the evicted claims, in eviction order. The sort is stable, so the
    list stays sorted after each pop -- the same claims leave as when each pop re-sorted first."""
    ledger.sort(key=lambda c: eviction_key(c.confidence, c.when))
    evicted = []
    while len(ledger) > cap:
        evicted.append(ledger.pop(0))
    return evicted
