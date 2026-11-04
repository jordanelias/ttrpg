"""CR-26 -- THE HEIR HEARS THE VACANCY (IN-61's design-first check (4), EXECUTED AS A TEST).

The occasion: when the throne (`off_king`) loses its holder, the holder of `off_heir` (`successions`'
key, IN-61) is handed a question set at the next DELIBERATE that names `off_king` as a CLASSED referent
of class `Office` -- the pair `row.referent_class: Office` forms on. H-230 measured that he was not
(20 question sets over four seasons, none) and named two limits, since repaired: CP-T02-01 (a death
names the seats it empties as a `tenure.closed` claim carrying the Office id) and CP-T02-02 (a realm
seat's id is its `offices.yaml` row id, so the throne is `off_king`).

THE CHAIN, FOUR LINKS, AND WHICH ONE A RED NAMES (`_failing_link`):
  (i)   the claim about the seat is NOT DEPOSITED in the heir's ledger at WITNESS;
  (ii)  it is deposited and EVICTED before he deliberates;
  (iii) it is in his ledger at DELIBERATE and `world_q.seats_named` / `_stamped` do not stamp it;
  (iv)  it is stamped, and the question he answers (`aggregate_questions` under the shipped
        `question_aggregation_rule`, `first`) carries no `Office` class pair for `off_king`.

TWO KINDS OF ARM, AND THEY ARE NOT THE SAME CLAIM:
  * the SEEDED arm (`build_realm(s)`, s = 0-2, four seasons) is a READING, and it lives in
    `harness/heir_hears.py` (`python -m engine.season.harness.heir_hears --seeds 0 1 2 --seasons 4`): which
    seed, which season, or none. It was a test here that passed with "none" and cost about 220 CPU-seconds
    of the suite; the plan (V2) says a reading is a harness reader.
  * the PLANTED arms (a death of the throne-holder at MATTER's death write; a `release` of the throne by
    its holder through the real fold) must pass whatever the seeds do, and they are this file's tests. A
    planted arm passing alone does NOT make `succeed` executed in computed play: that is the seeded
    reading's, a residue if it is none.

FALSIFIER: `World.seat_holds` returning nothing (CP-T02-01's emission helper off) turns the planted
death red at link (i). CONTROL: the same arm before the death (the throne held), and the stubbed arm
itself, carry 0 classed `off_king` referents -- the pre-CP-T02-01 reading (H-230's base: 20 sets, none).
"""
from __future__ import annotations

import pytest

from ..data.matrix import Step, WriteClass
from ..harness.heir_hears import HEIR_SEAT, THRONE
from ..harness.heir_hears import HeirSpy as _HeirSpy      # the names stay: `test_in61_succession.py`
from ..harness.heir_hears import holder as _holder        # imports `_holder` and `_one_season` from here
from ..harness.heir_hears import one_season as _one_season
from ..harness.heir_hears import reading as _reading
from ..harness.populated import build_realm
from ..loop.driver import SeasonDriver, mint_token
from ..loop.matter import _die
from ..queries import world_q
from ..queries.person_q import ledger_names
from ..state.carriers import Act
from ..state.world import World


def _failing_link(deposited_at_witness, readings):
    """The first link of the chain that breaks, or `None` when the heir hears the vacancy. `readings` are
    the heir's question sets at the DELIBERATE barriers that followed (each a `_reading`)."""
    if not deposited_at_witness:
        return "(i) the claim about the seat is not deposited"
    if not readings:
        return "(ii) the heir never deliberated (no question set was handed to him)"
    if not any(r["in_ledger"] for r in readings):
        return "(ii) the claim was evicted before he deliberated"
    if not any(r["seats_named"] and r["stamped"] for r in readings):
        return "(iii) seats_named does not stamp the seat on his question"
    if not any(r["answered"] for r in readings):
        return "(iv) no Office class pair for the seat reaches the question he answers under `first`"
    return None


# --- THE SEEDED ARM: A READING, NOT A TEST -------------------------------------------------------
# `python -m engine.season.harness.heir_hears --seeds 0 1 2 --seasons 4` prints which seed and season
# vacates the throne under a living heir, and whether he hears it. It was a test of three four-season
# realms that passed with "none" by design (about 220 CPU-seconds of the suite); the plan's V2 says a
# reading is a harness reader, and the plan (CR-26) already said the seeded arm is "never asserted".

# --- THE PLANTED ARMS ----------------------------------------------------------------------------

def _plant(monkeypatch, route, seed=0):
    """A seeded world, the throne-holder's seat emptied by `route` through the real write and the real
    WITNESS, then the heir's NEXT DELIBERATE (a real season) with the question sets recorded.
    Returns `(deposited_at_witness, control_reading, spy)`."""
    w = build_realm(seed)
    king, heir_id = _holder(w, THRONE), _holder(w, HEIR_SEAT)
    assert king and heir_id and king != heir_id, "fixture: no distinct throne-holder and heir"
    heir = w.persons[heir_id]
    d = SeasonDriver(w)
    control = _reading(w, heir, world_q.questions_for(w, heir, None))    # throne held, before anything
    if route == "death":
        w.step = Step.MATTER
        w._emitted_by_write = []
        _die(w, mint_token(w, WriteClass.MATTER), king)
        events = list(w._emitted_by_write)
        assert king not in w.persons, "the planted death did not happen"
    elif route == "release":
        w.step = Step.RESOLVE
        w.frozen = False
        events = d.resolve(mint_token(w, WriteClass.ACTS),
                           [Act(id="cr26_rel", actor=king, verb="release", payload={"subject": THRONE})],
                           contest_max_depth=w.fixtures.get("contest_max_depth"))
        assert king in w.persons, "a release is not a death"
    else:
        raise AssertionError(route)
    assert _holder(w, THRONE) is None, f"the {route} did not vacate the throne: {[e.kind for e in events]}"
    assert heir_id in w.persons and _holder(w, HEIR_SEAT) == heir_id, "the heir does not live and sit"
    w.log.extend(events)
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), events)
    deposited = THRONE in ledger_names(w.persons[heir_id].ledger)
    spy = _HeirSpy(heir_id)
    spy.install(monkeypatch)
    _one_season(w, d)
    return deposited, control, spy, [e.kind for e in events]


def test_planted_death_of_the_throne_holder_reaches_the_heir_as_a_classed_office_referent(monkeypatch):
    deposited, control, spy, kinds = _plant(monkeypatch, "death")
    assert "tenure.closed" in kinds, f"the death named no seat: {kinds}"
    assert not any(control.values()), f"control: the heir already heard of the throne: {control}"
    readings = [s["reading"] for s in spy.sets]
    assert spy.sets and all(not s["throne_held"] for s in spy.sets), "fixture: the throne was held again"
    link = _failing_link(deposited, readings)
    assert link is None, f"IN-61 STAYS STOPPED -- first failing link: {link}; readings {readings}"
    assert any(r["answered"] for r in readings)


def test_planted_release_of_the_throne_reaches_the_heir_as_a_classed_office_referent(monkeypatch):
    """The `release` route IN-61's GATE names: the throne vacated by its holder's own `release` (T-m),
    through the real fold. No death, no `person.died`: the seat reaches the heir by `release`'s own
    `tenure.closed` (the closed edge's id, which WITNESS expands to the seat)."""
    deposited, control, spy, kinds = _plant(monkeypatch, "release")
    assert not any(control.values()), f"control: the heir already heard of the throne: {control}"
    assert "person.died" not in kinds, kinds
    readings = [s["reading"] for s in spy.sets]
    assert spy.sets and all(not s["throne_held"] for s in spy.sets), "fixture: the throne was held again"
    link = _failing_link(deposited, readings)
    assert link is None, f"the release route fails -- first failing link: {link}; readings {readings}"


def test_mutation_with_seat_holds_unread_the_planted_death_goes_red_at_link_i(monkeypatch):
    """THE FALSIFIER, run: CP-T02-01's emission helper off (`World.seat_holds` -> `[]`, so
    `death_subjects` names no seat while `remove_person` still closes the holds -- the pre-CP-T02-01
    death). The planted death then fails at link (i), and the heir's question sets carry 0 classed
    `off_king` referents: the control H-230 measured at the base."""
    monkeypatch.setattr(World, "seat_holds", lambda self, who: [])
    deposited, control, spy, kinds = _plant(monkeypatch, "death")
    assert "tenure.closed" not in kinds, f"the stub did not switch the emission off: {kinds}"
    readings = [s["reading"] for s in spy.sets]
    assert spy.sets, "the heir was handed no question set: the control observed nothing"
    link = _failing_link(deposited, readings)
    assert link is not None and link.startswith("(i)"), f"expected red at link (i), got: {link}"
    assert not any(r["stamped"] or r["answered"] for r in readings), readings
    assert sum(1 for s in spy.sets if s["reading"]["answered"]) == 0     # 0 classed off_king referents

