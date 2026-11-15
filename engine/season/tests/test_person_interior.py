"""B03.58 -- the chooser receives a frozen copy of the person (`04` §B.2 row 2, §C.3).

DELIBERATE hands `choose` a `PersonInterior` (`state/carriers.py::interior_of`), not the stored `Person`, so a
callback -- a playable host's own, or a test's -- cannot change the person it is deciding for by assigning to it.
"""
import pytest

from engine.season.harness import probes as P
from engine.season.loop.driver import SeasonDriver


def test_a_callback_cannot_assign_a_skill_score():
    """A callback's `p.capability["argue"] = 9` raises at the assignment. Before B03.58 the callback was handed
    the stored `Person` and the assignment succeeded: the world's person held a score the fold never wrote."""
    w = P.tiny_world()
    called = []

    def callback(p, v, s, ask_budget):
        called.append(p.id)
        p.capability["argue"] = 9           # the assignment under test
        return []

    with pytest.raises(TypeError):
        SeasonDriver(w).season(callback, question=None,
                               contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert called, "the callback was never reached; the assignment was never tried"
    assert all("argue" not in p.capability for p in w.persons.values()), (
        "the stored person holds the assigned score")
