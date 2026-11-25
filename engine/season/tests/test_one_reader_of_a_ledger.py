"""B09.06 -- ONE COMPARATOR WEIGHS EVERY BELIEF (`weigh_confidence`: control `False` at B09.06, shipped `True` since B09.08).

A person's belief about a cell is what `LedgerReader` answers. Today `epistemic.belief_contradicts` reads it WEIGHED
(`decision/options.py::teller_weight`: a firsthand claim weighs 1.0 whatever its age, a told one `told_weight ** hops *
relation * record`), while `said_of` and `decision/sheet.py::chronicle` read it PLAIN (newest, then most confident), so one
person acts on one belief and says and shows another. The weight the comparator uses also discards how sure he still is:
a sighting nine seasons old weighs as much as one made this season.

B09.06 lands the control and the weight's new factor, `present_confidence(c) / confidence_default`, behind the fixture
`weigh_confidence`; at `False` (the control and the revert) every weight is today's. B09.07 re-points `said_of` and the sheet
at the one comparator, and gives the stage reader (`world_q.current_stage`) the parameter, which no caller supplies yet
(the reader is dormant); B09.08 ships `True`.

  test_weigh_confidence_false_reproduces_today                     reads the `False` arm (`FX_OFF`), and asserts `True` ships
  test_said_of_sheet_and_belief_contradicts_agree_on_every_cell    planted ledger, the SHIPPED fixtures
  test_said_of_sheet_and_belief_agree_on_every_row_of_a_realm      a seeded realm: every (holder, subject) row, counts printed
  test_stale_sighting_falls_to_enough_tellers                      SHIPPED fixtures
  test_fresh_sighting_holds_against_one_teller                     SHIPPED fixtures

The planted tests fail for the right reason, not for want of an instrument: each plants a ledger whose answer depends on
how sure the holder still is, and at `weigh_confidence = False` the comparator gives a sighting full weight at any age (so
the stale sighting never falls, and `said_of` / the sheet, still plain, name the newest told value). Their control, in
the same file: the `False` arm (`FX_OFF`) is asserted in the first test to be today's weights and to differ from the shipped
arm, so a switch that did nothing would fail it.
"""
from __future__ import annotations

import inspect

from ..data.fixtures import DEFAULT_FIXTURES
from ..decision import options as OP
from ..decision.sheet import chronicle
from ..queries.person_q import LedgerReader, said_of
from ..state.carriers import Claim, Person, interior_of

FX = DEFAULT_FIXTURES                      # the SHIPPED fixtures: `weigh_confidence` True since B09.08
FX_ON = FX.sweep("weigh_confidence", True)  # the shipped arm, named (equal to `FX`)
FX_OFF = FX.sweep("weigh_confidence", False)  # the control, and the revert: today's weights
FULL = FX.get("confidence_default")
DECAY = FX.claim_decay()
CELL = "stores.level"                      # a cell predicate (`requires.CELL_STEMS`): told claims on it PAIR with a sighting
ME = "p_me"


def _own(i: int, subject: str, value, when: int, confidence: int = FULL) -> Claim:
    """A claim of his own: firsthand, empty chain, so `teller_weight` weighs it 1.0 at the control (`FX_OFF`)."""
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
    assert FX_OFF.get("weigh_confidence") is False                  # the control arm, the revert
    assert FX.get("weigh_confidence") is True                       # the SHIPPED value (B09.08); the readings below are `FX_OFF`'s
    tick = 6
    # a sighting made at season 2 at 100 (present 80 at tick 6), one at 60 made at season 0 (present 30), and a told claim
    own_a, own_b = _own(1, "r_a", 5, when=2), _own(2, "r_b", 6, when=0, confidence=60)
    told = _told(3, "r_a", 8, when=6, teller="p_t1")
    p = _person(own_a, own_b, told)
    weigh = OP.teller_weight(p, FX_OFF, tick)

    # TODAY'S RULE, restated: 1.0 for a claim nobody told, else told_weight ** hops * relation * record (clamped to 1.0)
    for c in (own_a, own_b):
        assert weigh(c) == 1.0, c.id                                # however faded: today it reads no confidence
        checked += 1
    relation = 1.0 + FX_OFF.get("rank_gain") * OP.rank(p, "p_t1") + FX_OFF.get("regard_gain") * max(
        -1.0, min(1.0, OP.regard(p, "p_t1", FX_OFF) / OP.STANCE_MAX))
    today_told = min(1.0, max(0.0, FX_OFF.get("told_weight") ** told.hops * relation * OP.record(p, "p_t1", FX_OFF, tick)))
    assert weigh(told) == today_told
    assert 0.0 < today_told < 1.0                                   # a told claim does not hit a clamp: the product is observed
    checked += 1

    # `ledger_weigh`: today's condition at False -- the closure for any told claim, `None` for a ledger of the person's own
    assert OP.ledger_weigh(p, FX_OFF, tick) is not None
    assert OP.ledger_weigh(_person(own_a, own_b), FX_OFF, tick) is None, "a faded sighting alone must not take the weighed reader at False"
    assert OP.ledger_weigh(_person(_own(4, "r_c", 1, when=tick)), FX_OFF, tick) is None
    checked += 3

    # THE CONTROL THAT STOPS THIS PASSING VACUOUSLY: the switch is observable. At True (shipped) the same sightings weigh their
    # present confidence share (80/100 and 30/100) and a faded ledger of the person's own takes the closure.
    weigh_on = OP.teller_weight(p, FX, tick)                        # the SHIPPED arm
    assert OP.teller_weight(p, FX_ON, tick)(own_a) == weigh_on(own_a)
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
    # THE SOURCE'S c0 = 80: read four seasons on (present 60), the sighting holds against one teller and falls to a NUMBER of
    # tellers this run prints (each teller contradicts the sighting and earns `record` < 1, so the number is read, not assumed).
    held80 = {n: _belief(_stale_against(n, c0=80, tick=4), FX, 4, "r_x") for n in range(1, 31)}
    assert held80[1] == 10, "c0 = 80: the sighting holds against one teller"
    falls_at = next((n for n, v in held80.items() if v == 99), None)
    print(f"B09.08 stale sighting c0=80 (read at tick 4): holds against 1 teller, falls to {falls_at} tellers")
    assert falls_at is not None and falls_at > 1, "c0 = 80: it falls to a number of tellers, more than one"
    assert all(v == 99 for n, v in held80.items() if n >= falls_at), "and stays fallen with more tellers"
    # a sighting made nine seasons ago, deposited at 100 and so at 55 now, still holds against one teller and falls to
    # enough of them
    held = {n: _belief(_stale_against(n, c0=100), FX, 9, "r_x") for n in (1, 30)}
    assert held[1] == 10, "control: one teller does not move a sighting he is still more than half sure of"
    assert held[30] == 99, "enough tellers must move it"
    # THE CONTROL: at False the sighting weighs 1.0 whatever its age, so thirty tellers do not move it and the c0 = 5 one holds
    assert _belief(_stale_against(30, c0=100), FX_OFF, 9, "r_x") == 10
    assert _belief(_stale_against(1, c0=5), FX_OFF, 9, "r_x") == 10


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


def test_said_of_sheet_and_belief_agree_on_every_row_of_a_realm():
    """THE FALSIFIER ON A SEEDED REALM (seed 1, three seasons -- the source's hearer): every (holder, subject) where a person
    holds two different values for one cell, `said_of`, the sheet and `LedgerReader.read` give ONE value. A subject he holds a
    `seen` claim on is outside the rows: `said_of` passes a sighting on only when it is all he holds (R8.1), by design.
    ⚠ THIS REALM CANNOT SEE THE FAILURE ON ITS OWN: the plain `said_of` reads the same value on every row here (the count is
    printed), so the disagreement the planted ledgers observe is not one this seed's rows hold. It is the source's committed
    reading of the two columns, kept as the regression, and the planted-ledger test is the one that fails when a reader drifts."""
    from collections import defaultdict
    from ..boot.realm import build_realm
    from ..harness.populated import run
    from ..data.rosters import ABSENT_PREDICATE
    from ..queries.person_q import SEEN_PREDICATE

    w = build_realm(1)
    run(3, 1, w=w)
    fx, tick = w.fixtures, w.tick
    assert fx.get("weigh_confidence") is True
    rows = equal = plain_differs = 0
    for _pid, p in sorted(w.persons.items()):
        held = defaultdict(set)
        for c in p.ledger:
            held[(c.subject, c.predicate)].add(repr(c.value))
        # a subject he holds a `seen` claim on, or his own `absent` claim on (B11.83: `said_of` never offers it, by design), is outside the rows
        seen = {c.subject for c in p.ledger if c.predicate in (SEEN_PREDICATE, ABSENT_PREDICATE)}
        subjects = {s for (s, _pr), v in held.items() if len(v) > 1} - seen
        if not subjects:
            continue
        me = interior_of(p, tick, fx.claim_decay())
        beliefs = dict(chronicle(me, fx).beliefs)
        weigh = OP.ledger_weigh(p, fx, tick)
        reader = LedgerReader(p.ledger, weigh, tick=tick, decay=fx.claim_decay())
        for subject in subjects:
            said = said_of(p.ledger, subject, fx, tick=tick, weigh=weigh)
            shown = beliefs[subject]
            belief = reader.read(subject, said.predicate)
            rows += 1
            equal += said.value == shown.value == belief
            plain = said_of(p.ledger, subject, fx, tick=tick)          # the pre-B09.07 plain reader: the failure this test can see
            plain_differs += plain.value != belief
    print(f"B09.08 realm seed 1, 3 seasons: {equal} / {rows} rows equal across said_of, sheet, belief_contradicts' reader "
          f"({plain_differs} rows the plain said_of would have read differently)")
    assert rows >= 3, rows                                             # measured 3 at the B11 close (B11.83 leaves three of the nine out); the loop must have asserted something (CLAUDE.md 0.1 pt 2)
    assert equal == rows, f"{rows - equal} rows disagree"
