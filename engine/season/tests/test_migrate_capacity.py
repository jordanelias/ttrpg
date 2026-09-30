"""Plan position `19c` -- MIGRATE, carrying `24d-ii`'s `capacity`, and the `travel_leg` ride-along.
`workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md` "19c — MIGRATE" and "24d-ii —
CAPACITY"; the ruling is `RULINGS.yaml` RR-2 (*"must be able to build hearths and accept people who
move settlements"*; *"migration is a verb persons take"*).

What the position built, each asked of the real fold, the real MATTER barrier and the real gate:
  * THE RIDE-ALONG: a `travel_leg` ends at the next MATTER (`loop/matter.py`'s travel pass), the
    `MAT` half of `(Person, travel_leg)`'s `steps: [MAT, RES]`, emitting `travel.ended`. Before it
    nothing emptied the list and `decision/budget.py` charged every past leg in every season.

THE FALSIFIERS (the plan's own), and the control each carries:
  * after N moves and the legs' end, `len(travel_leg)` is 0 -- and the budget penalty is back to 0.
"""

from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..decision import budget
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Act

TRAVELLER, STAYER = "p_low", "p_mid"          # both in `Hh` at build; only the first travels


def _world(builder=P.tiny_world, **fx):
    """`builder()` at the given fixture arms, its tick-0 MATTER barrier run."""
    fixtures = DEFAULT_FIXTURES
    for name, value in fx.items():
        fixtures = fixtures.sweep(name, value)
    w = builder(fixtures) if builder is P.tiny_world else builder()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _fold(w, d, *acts):
    """One RESOLVE pass, its Events logged as `season` logs them."""
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _season(w, d):
    """The next season's MATTER barrier and nothing else: the tick advances, MATTER runs."""
    w.tick += 1
    return d.matter(mint_token(w, WriteClass.MATTER), [])


def _kinds(events):
    return [e.kind for e in events]


def _move(key, to, actor=TRAVELLER):
    return Act(id=key, actor=actor, verb="move", payload={"to": to})


# ======================================================================================
# 1 -- THE RIDE-ALONG: A LEG ENDS AT THE NEXT MATTER
# ======================================================================================

def test_19c_after_n_moves_the_legs_end_at_the_next_matter_and_the_penalty_returns_to_zero():
    """The plan's falsifier, *after N moves and the legs' end, `len(travel_leg)` is 0*, with the
    budget read BOTH sides of the end so the fix is observed where the defect bit (a write nobody
    reads would pass the length half alone -- `CLAUDE.md` §0.1 pt 1).

    Two moves in one season (`Hh` -> `S` -> `D`, each a strict ascent from a person-rung) lay two
    legs and cost two scenes; the next MATTER ends both in ONE write, emitting ONE `travel.ended`
    whose cause is the second move's `travel.moved` -- so the walk runs back to the act. CONTROLS:
    the person who never moved emits no `travel.ended` and keeps the full budget throughout; and the
    leg's end is not a return -- the traveller is still contained where the last leg took him."""
    w, d = _world()
    fx, k = w.fixtures, 5
    base = budget(w.persons[TRAVELLER], None, k, fx)
    assert base == budget(w.persons[STAYER], None, k, fx), "the two start unequal"
    first = _fold(w, d, _move("m1", "S"))
    second = _fold(w, d, _move("m2", "D"))
    assert _kinds(first) == _kinds(second) == ["travel.moved"], (_kinds(first), _kinds(second))
    traveller = w.persons[TRAVELLER]
    n = len(traveller.travel_leg)
    assert n == 2, traveller.travel_leg
    assert budget(traveller, None, k, fx) == base - n * fx.get("budget_leg_penalty") < base

    ended = [e for e in _season(w, d) if e.kind == "travel.ended"]
    assert traveller.travel_leg == [], traveller.travel_leg
    assert budget(traveller, None, k, fx) == base, "the distance penalty outlived its leg"
    assert len(ended) == 1, [e.kind for e in ended]
    assert ended[0].causes == [second[0].id], (ended[0].causes, second[0].id)
    assert budget(w.persons[STAYER], None, k, fx) == base
    home = next(t.object for t in traveller.tenures if t.kind == "contain" and t.live)
    assert home == "D", home

    # ... and a season with no move ends nothing: the pass is keyed on a leg, not on a person.
    assert not [e for e in _season(w, d) if e.kind == "travel.ended"]
