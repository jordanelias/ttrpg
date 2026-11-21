"""B09.06 -- ONE COMPARATOR WEIGHS EVERY BELIEF, AT CONTROL (`weigh_confidence`, shipped `False` here).

A person's belief about a cell is what `LedgerReader` answers. Today `epistemic.belief_contradicts` reads it WEIGHED
(`decision/options.py::teller_weight`: a firsthand claim weighs 1.0 whatever its age, a told one `told_weight ** hops *
relation * record`), while `said_of` and `decision/sheet.py::chronicle` read it PLAIN (newest, then most confident), so one
person acts on one belief and says and shows another. The weight the comparator uses also discards how sure he still is:
a sighting nine seasons old weighs as much as one made this season.

B09.06 lands the control and the weight's new factor, `present_confidence(c) / confidence_default`, behind the fixture
`weigh_confidence`; at `False` (shipped until B09.08 flips it) every weight is today's. B09.07 re-points `said_of`, the sheet
and the stage reader at the one comparator; B09.08 ships `True`.

  green  test_weigh_confidence_false_reproduces_today
  red    test_said_of_sheet_and_belief_contradicts_agree_on_every_cell    } red until B09.08, by design (the plan's
  red    test_stale_sighting_falls_to_enough_tellers                      } EXPECTED RED, `[skip ci]`): each reads the
  red    test_fresh_sighting_holds_against_one_teller                     } SHIPPED fixtures, whose `weigh_confidence` is `False`

The three red tests fail for the right reason, not for want of an instrument: each plants a ledger whose answer depends on
how sure the holder still is, and at `weigh_confidence = False` the comparator gives a sighting full weight at any age (so
the stale sighting never falls, and `said_of` / the sheet, still plain, name the newest told value). Their controls, in
the same file: the `True` arm (`DEFAULT_FIXTURES.sweep("weigh_confidence", True)`) is asserted in the green test to move the
weights, so a switch that did nothing would fail it.
"""
from __future__ import annotations

import inspect

from ..data.fixtures import DEFAULT_FIXTURES
from ..decision import options as OP
from ..decision.sheet import chronicle
from ..queries.person_q import LedgerReader, said_of
from ..state.carriers import Claim, Person, interior_of

FX = DEFAULT_FIXTURES                      # the SHIPPED fixtures: `weigh_confidence` False until B09.08
FX_ON = FX.sweep("weigh_confidence", True)
FULL = FX.get("confidence_default")
DECAY = FX.claim_decay()
CELL = "stores.level"                      # a cell predicate (`requires.CELL_STEMS`): told claims on it PAIR with a sighting
ME = "p_me"


def _own(i: int, subject: str, value, when: int, confidence: int = FULL) -> Claim:
    """A claim of his own: firsthand, empty chain, so `teller_weight` weighs it 1.0 at the control."""
    return Claim(f"c{i}", ME, subject, CELL, value, when, "firsthand", confidence, "own")


def _told(i: int, subject: str, value, when: int, teller: str, confidence: int = FULL) -> Claim:
    """A claim a teller passed on: one hop, origin and teller the same person."""
    return Claim(f"c{i}", ME, subject, CELL, value, when, "told", confidence, "own", chain=(teller,))


def _person(*claims: Claim) -> Person:
    return Person(ME, ledger=list(claims))


def _reader(p: Person, fx, tick: int) -> LedgerReader:
    """THE COMPARATOR `epistemic.belief_contradicts` reads a ledger by: `LedgerReader` with `opening_set`'s `weigh`."""
    return LedgerReader(p.ledger, OP.ledger_weigh(p, fx, tick), tick=tick, decay=fx.claim_decay())


def _belief(p: Person, fx, tick: int, subject: str):
    return _reader(p, fx, tick).read(subject, CELL)


def _said_value(p: Person, fx, tick: int, subject: str):
    """What he would pass on. B09.07 gives `said_of` a `weigh=` keyword and `opening_set` passes `ledger_weigh(p, fx)`; this
    passes the same closure once the keyword exists, and is the plain call until then (the disagreement under test)."""
    kw = {"tick": tick}
    if "weigh" in inspect.signature(said_of).parameters:
        kw["weigh"] = OP.ledger_weigh(p, fx, tick)
    said = said_of(p.ledger, subject, fx, **kw)
    return None if said is None else said.value


def _sheet_value(p: Person, fx, tick: int, subject: str):
    """What his sheet shows. B09.07 gives `chronicle` an `fx` argument; passed once it exists, plain until then."""
    me = interior_of(p, tick, fx.claim_decay())
    chron = chronicle(me, fx) if "fx" in inspect.signature(chronicle).parameters else chronicle(me)
    held = dict(chron.beliefs)[subject]
    return None if held is None else held.value


def _stale_against(n: int, c0: int, tick: int = 9):
    """THE SOURCE'S p2d SHAPE: one sighting of `r_x` made at season 0 at `c0` (read at `tick`, so faded by `DECAY` a
    season), against the same newer value from `n` DISTINCT tellers at full confidence. Returns the person."""
    own = _own(0, "r_x", 10, when=0, confidence=c0)
    told = [_told(i, "r_x", 99, when=tick, teller=f"p_t{i}") for i in range(1, n + 1)]
    return _person(own, *told)


def test_weigh_confidence_false_reproduces_today():
    checked = 0
    assert FX.get("weigh_confidence") is False                      # the shipped value at B09.06 (B09.08 flips it)
    tick = 6
    # a sighting made at season 2 at 100 (present 80 at tick 6), one at 60 made at season 0 (present 30), and a told claim
    own_a, own_b = _own(1, "r_a", 5, when=2), _own(2, "r_b", 6, when=0, confidence=60)
    told = _told(3, "r_a", 8, when=6, teller="p_t1")
    p = _person(own_a, own_b, told)
    weigh = OP.teller_weight(p, FX, tick)

    # TODAY'S RULE, restated: 1.0 for a claim nobody told, else told_weight ** hops * relation * record (clamped to 1.0)
    for c in (own_a, own_b):
        assert weigh(c) == 1.0, c.id                                # however faded: today it reads no confidence
        checked += 1
    relation = 1.0 + FX.get("rank_gain") * OP.rank(p, "p_t1") + FX.get("regard_gain") * max(
        -1.0, min(1.0, OP.regard(p, "p_t1", FX) / OP.STANCE_MAX))
    today_told = min(1.0, max(0.0, FX.get("told_weight") ** told.hops * relation * OP.record(p, "p_t1", FX, tick)))
    assert weigh(told) == today_told
    assert 0.0 < today_told < 1.0                                   # a told claim does not hit a clamp: the product is observed
    checked += 1

    # `ledger_weigh`: today's condition at False -- the closure for any told claim, `None` for a ledger of the person's own
    assert OP.ledger_weigh(p, FX, tick) is not None
    assert OP.ledger_weigh(_person(own_a, own_b), FX, tick) is None, "a faded sighting alone must not take the weighed reader at False"
    assert OP.ledger_weigh(_person(_own(4, "r_c", 1, when=tick)), FX, tick) is None
    checked += 3

    # THE CONTROL THAT STOPS THIS PASSING VACUOUSLY: the switch is observable. At True the same sightings weigh their
    # present confidence share (80/100 and 30/100) and a faded ledger of the person's own takes the closure.
    weigh_on = OP.teller_weight(p, FX_ON, tick)
    assert weigh_on(own_a) == 0.8 and weigh_on(own_b) == 0.3
    assert weigh_on(told) == today_told                             # the told claim was deposited at full confidence
    assert OP.ledger_weigh(_person(own_a, own_b), FX_ON, tick) is not None
    assert OP.ledger_weigh(_person(_own(4, "r_c", 1, when=tick)), FX_ON, tick) is None    # fresh and full: the plain reader, as before
    checked += 5
    assert checked >= 11


def test_said_of_sheet_and_belief_contradicts_agree_on_every_cell():
    """THE FALSIFIER AS A PLANTED LEDGER: every (holder, cell) on which `said_of`, the sheet and `belief_contradicts`'
    comparator give different values. Two cells, each answered one way by the plain reader (the newest, a told claim) and
    the other by the weighed: a STALE sighting the teller outweighs, and a RECENT one a single teller does not."""
    tick = 4
    p = _person(
        _own(1, "r_stale", 10, when=0, confidence=20),             # present 0 at tick 4: he is no longer sure
        _told(2, "r_stale", 99, when=tick, teller="p_t1"),
        _own(3, "r_recent", 7, when=3),                            # present 95: he is still sure
        _told(4, "r_recent", 8, when=tick, teller="p_t1"))
    expected = {"r_stale": 99, "r_recent": 7}                      # the belief a person who weighs how sure he is holds
    checked = 0
    for subject, want in expected.items():
        belief = _belief(p, FX, tick, subject)
        said = _said_value(p, FX, tick, subject)
        shown = _sheet_value(p, FX, tick, subject)
        assert said == shown == belief, (subject, "said", said, "sheet", shown, "belief_contradicts' reader", belief)
        assert belief == want, (subject, belief, want)             # agreeing on the old answer is not agreement on this one
        checked += 1
    assert checked == 2


def test_stale_sighting_falls_to_enough_tellers():
    # a sighting made nine seasons ago at confidence 5: one credible teller outweighs it (the source: "at c0 = 5 it falls to one")
    assert _belief(_stale_against(1, c0=5), FX, 9, "r_x") == 99, "a sighting he is no longer sure of must fall to one teller"
    # a sighting made nine seasons ago, deposited at 100 and so at 55 now, still holds against one teller and falls to
    # enough of them: each teller contradicts the sighting and so earns `record` < 1, which is why it is many and not two
    held = {n: _belief(_stale_against(n, c0=100), FX_ON, 9, "r_x") for n in (1, 30)}
    assert held[1] == 10, "control: one teller does not move a sighting he is still more than half sure of"
    assert held[30] == 99, "enough tellers must move it"
    # and under the SHIPPED fixtures the same ledgers read the same way (red while `weigh_confidence` is False: the
    # sighting weighs 1.0 whatever its age, and the noisy-OR over tellers never reaches 1.0)
    assert _belief(_stale_against(30, c0=100), FX, 9, "r_x") == 99


def test_fresh_sighting_holds_against_one_teller():
    tick = 5
    fresh = _own(1, "r_x", 10, when=4)                              # one season old: present 95
    one = _person(fresh, _told(2, "r_x", 99, when=tick, teller="p_t1"))
    weigh = OP.teller_weight(one, FX, tick)
    assert _belief(one, FX, tick, "r_x") == 10, "a recent sighting holds against one newer teller"
    # ...because it weighs how sure he still is, which is more than a teller's word and less than certainty
    teller_w = weigh(one.ledger[1])
    assert 0.0 < teller_w < 0.95
    assert weigh(fresh) == 0.95, "a sighting weighs its present confidence share (red while `weigh_confidence` is False: it weighs 1.0)"
