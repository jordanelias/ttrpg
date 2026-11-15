"""`decision/budget.py::budget` -- a seat buys no scene (C3-L8).

A person's scene budget is his establishment's base less the penalties of his own body and travel; a
held `hold` of any kind (a seat, a landholding, a book, a survey sheet) adds nothing to it. `04` §A.3 row
15 refuses an `office_bonus` in `budget` by name: a seat's capacity is its establishment, more named
persons each with their own budget.

`budget` is person-side and takes no `World`, so the instrument is a bare `Person` with Tenures planted
on its own store, the same way `test_season_shape.py::test_w5_budget_moves_with_the_persons_own_state_in_
the_ruled_directions` plants one.
"""

from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..decision import budget
from ..state.carriers import Person, Tenure, View


def _budget_of(p: Person) -> int:
    fx = DEFAULT_FIXTURES
    return budget(p, View(p.id, [], fx.get("view_k")), fx.get("scene_budget"), fx)


def test_a_seat_buys_no_scene():
    base = _budget_of(Person("p_none", "None"))

    held = Person("p_held", "Held")
    # Three live holds of three different kinds of object: a seat, a rung and a record.
    held.tenures = [Tenure("t_seat", "p_held", "off_x", "hold", since=0),
                    Tenure("t_rung", "p_held", "rung_x", "hold", since=0),
                    Tenure("t_rec", "p_held", "rec_x", "hold", since=0)]
    assert all(t.live for t in held.tenures), "the plant is not three LIVE holds"
    assert _budget_of(held) == base, (
        f"three live holds moved the budget {base} -> {_budget_of(held)}: a seat buys a scene")

    # Control: the same person with every hold closed, and a person who never held, read the same.
    for t in held.tenures:
        t.until = 1
    assert not any(t.live for t in held.tenures)
    assert _budget_of(held) == base == _budget_of(Person("p_none", "None")), (
        "a person with no live hold reads a different budget before and after holds")
