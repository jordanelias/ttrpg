"""B24.18 -- `contradicts(a, b)` is the pairing rule, exposed once (EVID_B "Exact edits" 2).

Two claims contradict when `_pair` marks one as disagreeing with the other on the cell `(subject, predicate)`: the same cell, a different value. The host
(`dossier.against`, `world_q.contradicted_tellers`) and `decision/options.py` read the one predicate; nothing restates `==`.
"""
from __future__ import annotations

from ..decision import options as OP
from ..queries import person_q
from ..state.carriers import Claim

CELL = "stores.level"                       # a cell predicate (`requires.CELL_STEMS`)


def _c(i: int, value, subject: str = "s1", predicate: str = CELL) -> Claim:
    return Claim(f"c{i}", "p_me", subject, predicate, value, 0, "firsthand", 5, "own")


def test_contradicts_is_the_pairing_rule():
    cases = [
        (_c(1, 3), _c(2, 4), True),                           # same cell, different value
        (_c(1, 3), _c(2, 3), False),                          # same cell, same value
        (_c(1, 3), _c(2, 4, predicate="stores.tier"), False),  # different predicate
        (_c(1, 3), _c(2, 4, subject="s2"), False),            # different subject
    ]
    checked = 0
    for a, b, want in cases:
        paired = person_q._pair([a], [b], lambda c: (c.subject, c.predicate), None)
        assert OP.contradicts(a, b) is want
        assert OP.contradicts(b, a) is want                   # symmetric
        assert (paired[1] == 1) is want                       # `_pair` and `contradicts` agree on the pair
        checked += 1
    assert checked == len(cases)
    assert OP.contradicts is person_q.contradicts             # one owner, re-bound by name
