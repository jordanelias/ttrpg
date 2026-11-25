"""B24.18 -- `contradicts(a, b)` is the pairing rule, exposed once (EVID_B "Exact edits" 2).

Two claims contradict when `_pair` marks one as disagreeing with the other on the cell `(subject, predicate)`: the same cell, a different value. The host
(`dossier.against`, `world_q.contradicted_tellers`) and `decision/options.py` read the one predicate; nothing restates `==`.

B24.19 -- `modules/social_contest/evidence.py::standing` is the one evidence rule (EVID_B edit 3): which exhibits still count, the relation read as data
(`Item.pairs`) from the host, the answering act's band (`Item.answered_band`) read and never regraded.
"""
from __future__ import annotations

import importlib
from dataclasses import replace

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


# ---- B24.19: `standing`, the one evidence rule inside the module (EVID_B edit 3) -------------------------------------------------------

def _it(iid, side, w=1.0, origin=None, pairs=(), cell=("s1", "stores.level", 3), band=None, **kw):
    from ..queries.inputs import Item
    return Item(iid, "record", w, side=side, cell=cell, origin=origin, pairs=tuple(pairs), answered_band=band, **kw)


def _ev():
    return importlib.import_module("modules.social_contest.evidence")            # by name, as the module's other tests do: `engine/` names no module by import


def _standing(presented, findings=(), cap=None):
    return _ev().standing(tuple(presented), tuple(findings), cap)


def test_corroboration_is_noisy_or_by_origin():
    """EVID_B gate 4: two items of one cell and value on one side, weights 0.5 and 0.5, from distinct origins are ONE item of 0.75; from one origin, 0.5
    (and the origin counted once however many items it filed); `evidence_cap` caps what the corroboration gains. FALSIFIER: an additive reading gives 1.0."""
    agree = (("b", "agrees"),)
    two = [_it("a", "for", 0.5, "o1", agree), _it("b", "for", 0.5, "o2", (("a", "agrees"),))]
    one = [replace(i, origin="o1") for i in two]
    got, struck, faults = _standing(two)
    assert [(i.id, i.weight) for i in got] == [("a", 0.75)] and struck == () and faults == ()
    assert [(i.id, i.weight) for i in _standing(one)[0]] == [("a", 0.5)]
    assert _standing(two, cap=0.6)[0][0].weight == 0.6                      # the cap limits the gain, it does not lower an item
    assert _standing(two, cap=0.1)[0][0].weight == 0.5
    lone = [_it("a", "for", 0.5, "o1"), _it("b", "for", 0.5, "o2")]         # same cell, nothing filed as agreeing: two items, each counted
    assert [i.weight for i in _standing(lone)[0]] == [0.5, 0.5]


def test_an_off_rung_item_enters_at_half_and_a_same_origin_second_adds_less():
    """KERN_B check 3: an item off the rung tried enters the sitting's board at half weight (and `irrelevance` is recorded against its side); a second item of
    one origin on a hand-built board adds nothing where one of a distinct origin adds, so the sum of the board is the rule's and not the items'."""
    from ..queries.inputs import Choice
    from .test_sc_proceeding_module import P, _inp, _key, _p, _rite, _sit
    evidence = _ev()
    on, off = _it("i1", "for", 2.0, rung="fact"), _it("i2", "for", 2.0, rung="definition")
    a = _p("a", "for", items=(on, off))
    inp = _inp([a, _p("b", "against"), _p("j0", decides=True, precedence=1)], _rite(close="bench", admits=("record",), issues=("fact", "definition")))
    st, _ = P.exchange(inp, _sit(inp), a, Choice("present", None, "i1"), _key("rung", 0))
    st, _ = P.exchange(inp, st, a, Choice("present", None, "i2"), _key("rung", 1))
    assert [(i.id, i.weight) for i, _ in st.board] == [("i1", 2.0), ("i2", 1.0)] and st.faults == (("irrelevance", "for"),)
    first = [_it("x", "for", 0.8, "o1", (("y", "agrees"), ("z", "agrees")))]
    same = first + [_it("y", "for", 0.6, "o1", (("x", "agrees"),))]
    other = first + [_it("z", "for", 0.6, "o2", (("x", "agrees"),))]
    w = lambda b: sum(i.weight for i in evidence.standing(tuple(b), (), None)[0])
    assert w(first) == w(same) == 0.8 and w(other) > 0.8 and w(other) - w(first) < 0.6        # one origin adds nothing; a second origin adds less than its weight


def test_an_answer_of_the_same_value_strikes_nothing():
    """EVID_B falsifier: an answer that says what the item says is AGREEMENT (rule 3), whatever its band: neither counts, nothing is struck, nothing is owed."""
    for band in ("Failure", "Partial", "Success", "Overwhelming"):
        got, struck, faults = _standing([_it("a", "for", 1.0, "o1", (("b", "agrees"),), band=band), _it("b", "against", 1.0, "o2", (("a", "agrees"),))])
        assert (got, struck, faults) == ((), (), ()), band


def test_an_answer_acts_by_its_band_on_the_item_it_answers():
    """Rules 1 and 2, band by band, on the answering act's own band: contradiction (Failure stands, Partial halves it and its answer, Success strikes it,
    Overwhelming strikes it and charges its citer if he knew it false, else its origin) and forgery (Failure: the impeacher bears `failed_impeachment`; Partial
    halves; Success strikes it alone; Overwhelming strikes every item of its origin and records `forgery_found`). An item never answered is never struck."""
    def board(band, **kw):
        return [_it("t", "for", 1.0, "o1", (("r", "contradicts"),), band=band, **kw), _it("r", "against", 0.5, "o2", (("t", "contradicts"),)),
                _it("m", "for", 1.0, "o1", (), cell=("s2", "stores.level", 1))]
    ws = lambda b, f=(), **kw: {i.id: i.weight for i in _standing(board(b, **kw), f)[0]}
    assert ws(None) == ws("Failure") == {"t": 1.0, "r": 0.5, "m": 1.0}
    assert ws("Partial") == {"t": 0.5, "r": 0.25, "m": 1.0}
    assert _standing(board("Success"))[1:] == (("t",), ()) and _standing(board("Overwhelming"))[1:] == (("t",), (("discredited_source", "o1"),))
    assert _standing(board("Overwhelming", sincere=False))[2] == (("self_contradiction", "for"),)
    checked = 0
    for band, want in (("Failure", ((), (("failed_impeachment", "against"),))), ("Partial", ((), ())), ("Success", (("t",), ())),
                       ("Overwhelming", (("t", "m"), (("forgery_found", "for"),)))):
        _, struck, faults = _standing(board(band), findings=("t",))
        assert (struck, faults) == want, band
        checked += 1
    assert ws("Partial", ("t",)) == {"t": 0.5, "r": 0.5, "m": 1.0} and checked == 4         # a forgery's Partial halves the Record alone


def test_a_sitting_strikes_an_answered_item_by_the_rule_over_the_bands_drawn():
    """The sitting decides nothing about an answer: it grades the margin on the ladder, files the band on the item, and the board is `standing` over the items
    shown. Over 40 keys every band occurs; the item is struck at Success and Overwhelming only, and halved (its weight now) at Partial."""
    from ..data.arrangements import GROUNDS
    from ..queries.inputs import Choice
    from .test_sc_proceeding_module import P, _inp, _key, _p, _rite, _sit
    ground = next(g for g, r in GROUNDS.items() if r["reads"] != "item")
    i1, j1 = _it("i1", None, 1.0, "o1", (("j1", "contradicts"),)), _it("j1", None, 1.0, "o2", (("i1", "contradicts"),), cell=("s1", "stores.level", 4))
    a, b = _p("a", "for", items=(i1,)), _p("b", "against", items=(j1,))
    inp = _inp([a, b, _p("j0", decides=True, precedence=1)], _rite(close="bench", admits=("record",)))
    seen = {}
    for k in range(40):
        st, _ = P.exchange(inp, _sit(inp), a, Choice("present", None, "i1"), _key("ans", k))
        st, _ = P.exchange(inp, st, b, Choice("present", None, "j1"), _key("ans", k + 100))
        st, beat = P.exchange(inp, st, b, Choice("answer", ground, "i1"), _key("ans", k + 200))
        held, struck, _faults = _standing([i for i, _ in st.board])
        band = {i.id: i.answered_band for i, _ in st.board}["i1"]
        assert [(i.id, s) for i, s in st.board] == [("i1", "struck" if "i1" in struck else "answered"), ("j1", "stands")]    # the board is the rule's reading
        assert beat.struck == tuple(struck) and ("i1" in struck) == (band in ("Success", "Overwhelming"))
        seen[band] = {i.id: i.weight for i in held}.get("i1")
    assert set(seen) == {"Failure", "Partial", "Success", "Overwhelming"} and seen["Partial"] == 0.5 and seen["Failure"] == 1.0 and seen["Success"] is None
