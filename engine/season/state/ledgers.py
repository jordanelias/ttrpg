"""`state/ledgers` -- the eviction comparator, and the one function that applies it.

`04_CODE_ARCHITECTURE.md` §A.2:149 names this module as the owner of *"per-person packed claim
rows; the eviction comparator"*. This file holds the SECOND half: the comparator, which
`loop/witness.py`'s eviction closure calls.

⚠ THE STORE SPLIT IS NOT HERE. The first half -- claim rows in a sub-store of their own, with a
write token distinct from conviction state (`04:117`, AX-3) -- needs the G2 token-type rewrite,
which does not exist yet. Until it does, `Person.ledger` stays on the carrier and every eviction
still goes through `World.write(... "claim_ledger" ...)`, the gate that applies it (AX-4); this
module is called INSIDE that write, never instead of it.
"""
from __future__ import annotations


def present_confidence(confidence: int, when: int, tick: int, decay: int) -> int:
    """A claim's confidence at `tick`: what was deposited, less `decay` per season elapsed.

    THE SINGLE OWNER of how a claim fades. A claim stores the value it was deposited at and nothing ever
    writes it again; every reader of a held claim's confidence (`queries/person_q.py::LedgerReader`,
    `said_of`, `queries/world_q.py::reception`, `decision/questions.py`, and `evict_over_cap` below) asks
    here, with the `tick` it reads at and `Fixtures.claim_decay()`. It is `0` at the floor, never negative,
    and a `tick` at or before `when` has elapsed no season."""
    return max(0, confidence - decay * max(0, tick - when))


def eviction_key(confidence: float, recency: int) -> float:
    """S20/S34: EVICTION RANKS ON `confidence_live x recency` ONLY, NEVER SALIENCE -- a product,
    not a lexicographic `(confidence, when)` tuple, which is a different comparator and
    degenerates to insertion order under a constant confidence. Lowest is evicted first."""
    return confidence * (recency + 1)


def evict_over_cap(ledger: list, cap: int, tick: int = 0, decay: int = 0) -> list:
    """Sort `ledger` in place by `eviction_key(present_confidence(c.confidence, c.when, tick, decay), c.when)`
    -- the confidence a holder has the claim at NOW, not the one it was deposited at -- and pop from the front until
    `len(ledger) <= cap`. Returns the evicted claims, in eviction order. The sort is stable, so the
    list stays sorted after each pop -- the same claims leave as when each pop re-sorted first."""
    ledger.sort(key=lambda c: eviction_key(present_confidence(c.confidence, c.when, tick, decay), c.when))
    evicted = []
    while len(ledger) > cap:
        evicted.append(ledger.pop(0))
    return evicted
