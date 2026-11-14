"""`harness/corpus_run.py::told_redeposits_in` -- the corpus's `told_by` redeposit counter, on planted ledgers.

`test_season_shape.py` asserts the counter reads 0 over the seed-0 corpus; a zero is only evidence if the counter can
see a redeposit. These ledgers are planted so each clause has a fixed answer: a true redeposit (told after an own copy
of the same triple) is counted; a later firsthand sighting of a told claim is not; and the count does not depend on the
ledger's order, which is not arrival order once `state/ledgers.py::evict_over_cap` has sorted it by eviction key.
"""
from __future__ import annotations

from ..harness.corpus_run import told_redeposits_in
from ..state.carriers import Claim
from ..state.ledgers import evict_over_cap

TRIPLE = ("p_b", "body", 3)


def _claim(cid: str, source: str, when: int, confidence: int, rnd: int = 0, value=TRIPLE[2]) -> Claim:
    chain = ("p_c",) if source == "told_by" else ()
    return Claim(cid, "p_a", TRIPLE[0], TRIPLE[1], value, when, source, confidence, "own", rnd, chain=chain)


def test_a_telling_after_an_own_copy_is_counted():
    ledger = [_claim("own", "firsthand", 1, 5), _claim("told", "told_by", 2, 5)]
    assert told_redeposits_in(ledger) == 1


def test_a_later_firsthand_sighting_of_a_told_claim_is_not_counted():
    # B01a.99's case (EMG-C3): told at `when` 2, seen firsthand at 3 and at 5.
    ledger = [_claim("told", "told_by", 2, 5), _claim("own3", "firsthand", 3, 5),
              _claim("own5", "firsthand", 5, 5)]
    assert told_redeposits_in(ledger) == 0


def test_a_redeposit_is_counted_in_the_order_eviction_leaves_the_ledger():
    # Deposit order: own copy at `when` 1 (confidence 9), then the telling at `when` 2 (confidence 1).
    ledger = [_claim("own", "firsthand", 1, 9), _claim("told", "told_by", 2, 1)]
    assert told_redeposits_in(ledger) == 1
    # The ledger as the cap's sort leaves it (cap not reached, so nothing leaves): key 9*(1+1)=18 for the own
    # copy, 1*(2+1)=3 for the telling, so the telling now sits FIRST. The premise is asserted, not assumed.
    assert evict_over_cap(ledger, cap=len(ledger)) == []
    assert [c.id for c in ledger] == ["told", "own"]
    assert told_redeposits_in(ledger) == 1


def test_the_round_orders_deposits_within_a_tick_and_a_tie_counts():
    assert told_redeposits_in([_claim("told", "told_by", 2, 5, rnd=1), _claim("own", "firsthand", 2, 5, rnd=0)]) == 1
    assert told_redeposits_in([_claim("told", "told_by", 2, 5, rnd=0), _claim("own", "firsthand", 2, 5, rnd=1)]) == 0
    # No field orders two deposits of one `(when, round)`: the detector counts the tie.
    assert told_redeposits_in([_claim("told", "told_by", 2, 5), _claim("own", "firsthand", 2, 5)]) == 1


def test_a_different_value_or_a_told_copy_is_not_an_own_copy():
    # A contradicting value is the epistemic layer working, not a belief stored twice.
    assert told_redeposits_in([_claim("own", "firsthand", 1, 5, value=1), _claim("told", "told_by", 2, 5)]) == 0
    # Two tellings of one triple: neither is an untold copy (the counter counts against untold claims only).
    assert told_redeposits_in([_claim("t1", "told_by", 1, 5), _claim("t2", "told_by", 2, 5)]) == 0
