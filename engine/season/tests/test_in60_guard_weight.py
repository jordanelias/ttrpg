"""v9 IN-60 (RS-26) -- THE SECURITY QUERY: `world_q.guard_weight`, THE SWORN WEIGHT PRESENT AT A RUNG.

`guard_weight(w, rung)` sums the `Person.weight` of the persons `presence` lists at the rung (exact) who
owe a live, sworn `oblige` to a seat HELD by a person ALSO present there -- the principal's own place.
Compute-on-demand, stored nowhere; a seat adds no modifier (`04` §B.7). Its reader is IN-59 (b)
(`admits_audience`'s guard limb); at IN-60 alone nothing called it, so the realm hashes did not move.

THE FALSIFIERS, on a hand-built world where the cause is controlled, each with its mutation:
  1. RECOMPUTE (T-a): end one swearer's `oblige` and the value falls by exactly his weight, with no
     other write. Mutation: memoise the first read -> red.
  2. THE REALM (`build_realm(0, guards=True)`): the King's home reads nonzero and each duke's home
     reads less -- `test_in36_foreign.py`'s guard tests, which read THIS Query (their local
     `_guard_weight` helper is retired for it, one owner).
  3. THE PRINCIPAL'S PLACE: an ordinary rung with one sworn resident and no principal present reads 0.
     Mutation: make the principal-presence clause a no-op (every held seat) -> red.
  4. STORED NOWHERE: no field, no write; checked on the diff, not by a test (`CLAUDE.md` §0.1 pt 5).

The fixture is `probes.tiny_world` (`R` > `D` > `S` > `Hh`; `p_high` holds `off_duke` and stands at
`S`; `p_low`, `p_mid`, `p_other` stand at `Hh`), with guard cohorts planted by `probes.plant_cohort`
and their `oblige` edges added by hand -- the same edge `build_realm(guards=True)` writes.
"""

from __future__ import annotations

from ..harness import probes as P
from ..queries import world_q
from ..state.carriers import DETERMINED_BY, Tenure

SEAT, PRINCIPAL = "off_duke", "p_high"   # roster-exempt: TEST FIXTURE ids (`tiny_world`'s)


def _world():
    return P.tiny_world()


def _swear(w, who, seat=SEAT, **kw) -> Tenure:
    """A live `oblige : who -> seat`, added by hand (the edge `populated.seat_guards` writes)."""
    return w.add_tenure(Tenure(f"t_ob_{who}_{seat}", who, seat, "oblige", 0, **kw))


def _guard(w, pid, rung, weight):
    P.plant_cohort(w, pid, rung, weight=weight)
    return _swear(w, pid)


def test_in60_a_sworn_cohort_at_the_principals_place_is_counted():
    w = _world()
    assert world_q.guard_weight(w, "S") == 0, "no one sworn: an unguarded place reads 0"
    _guard(w, "c_guard_a", "S", 3)
    assert world_q.guard_weight(w, "S") == 3


def test_in60_falsifier_1_ending_one_oath_drops_the_reading_with_no_other_write():
    w = _world()
    a = _guard(w, "c_guard_a", "S", 3)
    _guard(w, "c_guard_b", "S", 2)
    assert world_q.guard_weight(w, "S") == 5
    a.until = w.tick            # the ONE write: guard A's oath ends
    assert world_q.guard_weight(w, "S") == 2, "a stored value would not have moved (T-a)"


def test_in60_falsifier_3_a_sworn_resident_with_no_principal_present_reads_zero():
    """The inn case: a man sworn to the Duke lives at `Hh`, the Duke stands at `S`. Then the Duke comes
    to `Hh` (a positive control: the same rung reads > 0 once the principal is present, so the 0 is the
    principal clause, not a reader that sees nothing)."""
    w = _world()
    _guard(w, "c_guard_inn", "Hh", 4)
    assert world_q.guard_weight(w, "Hh") == 0
    assert world_q.guard_weight(w, "S") == 0, "the guard is not at the principal's place"
    w.add_tenure(Tenure("t_high_at_hh", PRINCIPAL, "Hh", "contain", 0))
    for t in w.tenures:
        if t.kind == "contain" and t.subject == PRINCIPAL and t.object == "S":
            t.until = w.tick
    assert world_q.guard_weight(w, "Hh") == 4


def test_in60_presence_is_the_exact_rung_and_a_person_counts_once_and_an_imposed_oblige_is_no_oath():
    """Three edges of the definition, one controlled world each; the loop asserts it asserted."""
    def below():                 # a guard at `Hh`, inside `S` where the principal stands: not counted at `S`
        w = _world()
        _guard(w, "c_guard_hh", "Hh", 3)
        return w, "S", 0

    def twice_sworn():           # sworn to two seats both held at `S`: counted once
        w = _world()
        w.offices["off_reeve"] = type(w.offices[SEAT])("off_reeve", "Reeve", "S", ["issue"], faction="Crown")
        P.plant_cohort(w, "c_guard_2", "S", weight=3)
        w.add_tenure(Tenure("t_king_at_s", "p_king", "S", "contain", 0))
        w.add_tenure(Tenure("t_king_reeve", "p_king", "off_reeve", "hold", 0))
        _swear(w, "c_guard_2")
        _swear(w, "c_guard_2", "off_reeve")
        return w, "S", 3

    def imposed():               # a sentence to serve the seat is not an oath (`Tenure.imposed`)
        w = _world()
        P.plant_cohort(w, "c_convict", "S", weight=3)
        _swear(w, "c_convict", payload={DETERMINED_BY: "off_duke"})
        return w, "S", 0

    checked = 0
    for build in (below, twice_sworn, imposed):
        w, rung, want = build()
        assert world_q.guard_weight(w, rung) == want, build.__name__
        checked += 1
    assert checked == 3
