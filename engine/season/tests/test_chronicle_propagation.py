"""B02.16 -- `harness/chronicle.py`'s propagation reading: how far the played world's state differs from the
same built world where nobody acts. These tests are the reading's two controls, both directions, and pin
no number from a realm run (the numbers move whenever the game does):

  (a) the null arm against itself reads zero in every column;
  (b) a planted consequence is seen -- the bodies hazard set to 1 for one seat-holder moves `persons` and
      `seat holds` in column 1, reads as a death in the tenure causes, and puts a `person.died` in column
      3's denominator.

If either fails the reading is void.
"""

from __future__ import annotations


from ..data.verbs import VERB_TABLE
from ..harness import chronicle as C
from ..harness import storybar as SB
from ..boot.realm import build_realm
from ..queries import world_q

SEED, SEASONS, CAP = 0, 2, 10


def _null_arm(base, plant=None):
    """One copy of `base` run `SEASONS` seasons with nobody acting. `plant`, when given, is the one change
    made to the copy before it runs."""
    w = SB.fork(base)
    if plant is not None:
        plant(w)
    return SB.drive(w.world_seed, SEASONS, "off", world=w, wrap_chooser=C.nobody_acts)[0]


def test_null_arm_against_itself_reads_zero_in_every_column():
    base = build_realm(SEED, CAP)
    first, again = _null_arm(base), _null_arm(base)
    assert len(first.log) > 0, "the null arm logged nothing; a zero below would be vacuous"
    moved = C.moved_by_persons(first, again)
    assert set(moved) == set(C.COMPONENTS) | {f"tenure.{c}" for c in C.TENURE_CAUSES}
    assert moved and not any(moved.values()), f"two copies of one null world differ: {moved}"
    assert C.answered_outside_writing(first, VERB_TABLE) == 0
    terminals = C.terminals_answered(first)
    assert set(terminals) == set(C.TERMINALS)
    assert sum(emitted for emitted, _ in terminals.values()) > 0, (
        "the null arm emitted no terminal Event (MATTER's `body.changed` is one); the zeros below saw nothing")
    assert not any(answered for _, answered in terminals.values()), (
        f"nobody acted and a terminal was still answered: {terminals}")


def test_planted_body_hazard_moves_persons_and_seat_holds(monkeypatch):
    base = build_realm(SEED, CAP)
    seats = sorted((t.subject, t.object) for t in base.tenures
                   if t.kind == "hold" and t.live and t.object in base.offices)
    assert seats, "nobody is seated on the realm; the plant below observes nothing"
    holder, office = seats[0]
    control = _null_arm(base)
    assert holder in control.persons and not C.terminals_answered(control)["person.died"][0], (
        "the control arm already lost the holder; the plant below would not be the cause")
    # `age_step` above 0 only lets MATTER's bodies pass run; the hazard itself is replaced by one that is
    # certain for the one holder and nothing for anyone else
    monkeypatch.setattr(world_q, "body_hazard", lambda w, pid: 1.0 if pid == holder else 0.0)
    planted = _null_arm(base, plant=lambda w: setattr(w, "fixtures", w.fixtures.sweep("age_step", 0.01)))
    assert holder not in planted.persons, "the plant did not kill the holder"

    moved = C.moved_by_persons(planted, control)
    assert moved["persons"] >= 1, moved
    assert moved["seat holds"] >= 1, moved
    assert moved["tenure.death"] >= 1, f"the seat his death emptied is not read as a death: {moved}"
    emitted, _answered = C.terminals_answered(planted)["person.died"]
    assert emitted >= 1, "the death is not in column 3's denominator"
    # the same call, planted against itself, reads zero: the reading moved because of the plant
    assert not any(C.moved_by_persons(planted, _null_arm(base, plant=lambda w: setattr(
        w, "fixtures", w.fixtures.sweep("age_step", 0.01)))).values())
