"""B10.14 -- the crisis reader's one composed signature, `queries/person_q.py::conviction_after_crisis(p, among, band, shared, reading)`.
Hand-built persons with planted creeds and scar counts; every expected conviction is stated here, not re-derived from the reader.

FALSIFIER: at the shared column the stronger creed is still the one folded, or `band=None` is no longer today's function.
"""
from __future__ import annotations

from ..queries import person_q as PQ
from ..state.carriers import Person
from ._scar_helpers import compatible_pairs, incompatible_pairs


def _person(conviction: dict, scar: dict) -> Person:
    return Person(id="p_crisis", conviction=dict(conviction), scar=dict(scar))


def test_off_reproduces_conviction_after_crisis():
    """`band=None`, `shared=False`, `reading="any"` is today's function on each of its branches, and its `scar_delta` is empty."""
    a, b = incompatible_pairs()[0]
    c, d = compatible_pairs()[0]
    checked = 0
    # FOLD: the stronger of two incompatible creeds in crisis is the one taken (today's `max`), its intensity going to the other, clamped.
    after, delta = PQ.conviction_after_crisis(_person({a: 4, b: 2}, {a: 3, b: 3}))
    assert (after, delta) == ({b: 5}, {})
    checked += 1
    # DESTROYED: nothing else is held.
    assert PQ.conviction_after_crisis(_person({a: 3}, {a: 3})) == ({}, {})
    checked += 1
    # RESTABILISE is not built: a compatible creed held beside it leaves the vector as it was.
    held = {c: 3, d: 2}
    assert PQ.conviction_after_crisis(_person(held, {c: 3})) == (held, {})
    checked += 1
    # `among` bounds the crisis to the creeds the act just scarred: a creed at the threshold that was not scarred is not in crisis.
    assert PQ.conviction_after_crisis(_person({a: 4, b: 2}, {a: 3}), among=frozenset({b})) == ({a: 4, b: 2}, {})
    checked += 1
    assert checked >= 4


def test_lowest_intensity_creed_is_the_one_in_crisis_for_shared_column():
    """Where the shared column scars every held creed alike, the lowest-intensity creed is the one in crisis and folds into the stronger."""
    a, b = incompatible_pairs()[0]
    held, scar = {a: 4, b: 2}, {a: 3, b: 3}
    shared, _ = PQ.conviction_after_crisis(_person(held, scar), shared=True)
    assert shared == {a: 5}, "the weaker creed must be the one that drops"
    # the control: a per-affiliation cell keeps the draft's direction (the stronger creed in crisis), the same person
    cell, _ = PQ.conviction_after_crisis(_person(held, scar), shared=False)
    assert cell == {b: 5}
    # a tie on intensity goes to the first by name under either selector
    tied, _ = PQ.conviction_after_crisis(_person({a: 3, b: 3}, {a: 3, b: 3}), shared=True)
    assert tied == {b: 5} and a < b


def test_each_band_writes_what_its_table_row_says():
    """`band=` reads `tables.crisis_bands`: the Overwhelming, Success, Partial and Failure rows each leave the creed in crisis, and its count, as written."""
    c, d = compatible_pairs()[0]
    a, b = incompatible_pairs()[0]
    held, scar = {c: 3, d: 2}, {c: 4}                    # a count of 4: `zero` (-4) and `threshold_less_one` (-2) differ
    got = {band: PQ.conviction_after_crisis(_person(held, scar), band=band) for band in PQ.CRISIS_BANDS}
    assert got["Overwhelming"] == ({c: 4, d: 2}, {c: -4})
    assert got["Success"] == (held, {c: -2})
    assert got["Partial"] == ({c: 2, d: 2}, {})
    assert got["Failure"] == ({c: 1, d: 2}, {})          # nothing incompatible held, something else held: -2
    assert PQ.conviction_after_crisis(_person({c: 5, d: 2}, scar), band="Overwhelming")[0] == {c: 5, d: 2}, "clamped at the ceiling"
    assert PQ.conviction_after_crisis(_person({c: 1, d: 2}, scar), band="Partial")[0] == {c: 0, d: 2}, "a held rejection, not a drop"
    assert PQ.conviction_after_crisis(_person({c: 1, d: 2}, scar), band="Failure")[0] == {c: 0, d: 2}, "floored at 0"
    assert PQ.conviction_after_crisis(_person({a: 3, b: 2}, {a: 3, b: 3}), band="Failure") == ({b: 5}, {}), "Failure folds first"
    assert PQ.conviction_after_crisis(_person({c: 3}, {c: 3}), band="Failure") == ({}, {}), "Failure destroys where nothing else is held"
