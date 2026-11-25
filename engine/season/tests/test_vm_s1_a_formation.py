"""v12 B11.69 (`14_VERBS_SOCIAL1_A_formation` edits 3-5): A PERSON FORMS ONLY WHAT CAN BE DONE -- on a person he believes is with him, and `covenant` only on a Proposition.

Lane: the engine's formation (`decision/options.py::opening_set`), hand-built worlds (game-state: it observes which Candidates a person forms).

  * the `with` conjunct is read by conjunct, never by verb (`VerbRow.with_operands`): a row asking its `to` to be with the actor (`argue`) forms no
    act to a person his OWN ledger does not place with him, and a row asking its `subject` to be (`train`) forms none on him, under the arm
    `telling_hearers: seen_since_move`; the control arm `known` forms both (no bag dropped); a firsthand sighting places him there again;
  * `covenant` is classed `Proposition` (`argue`'s and `commit`'s class): it forms on the Proposition he has heard and on no person.
The realm readings (`aperture 2 s`, the hash) are commit-body readings, never assertions here.
"""
from __future__ import annotations

from engine.season.data.verbs import VERB_TABLE
from engine.season.epistemic import SEEN_PREDICATE, Seen
from engine.season.state.carriers import Claim

from .test_cr28_propositions_heard import HEARD, _question, _utter_witnessed
from .test_in53_vacancy_need import _formed, _know
from .test_works_founding import ABSENT, PRESENT, _world


def _argues_to(w, pid, to):
    return [c for c in _formed(w, pid, _question(w, pid)) if c.verb == "argue" and (c.operands or {}).get("to") == to]


def _on_subject(w, pid, subject):
    """The Candidates on `subject` of a row whose cell asks its `subject` to be with the actor (read off the cell, never a verb name)."""
    return [c for c in _formed(w, pid, _question(w, pid))
            if c.subject == subject and "subject" in VERB_TABLE[c.verb].with_operands()]


def _sighting(w, pid, who, cid="c_saw"):
    w.persons[pid].ledger.append(Claim(cid, pid, who, SEEN_PREDICATE, Seen(stratum="speech", who=who), 0, "firsthand", 100, "own", 0))


def test_a_person_placed_elsewhere_forms_no_argue_to_him():
    w, _ = _world(telling_hearers="seen_since_move")
    _utter_witnessed(w, PRESENT)
    _know(w, PRESENT, ABSENT)                       # he knows ABSENT exists; no firsthand sighting places him here
    assert _argues_to(w, PRESENT, ABSENT) == []
    control, _ = _world(telling_hearers="known")    # the control arm: every known person is offered, no bag dropped
    _utter_witnessed(control, PRESENT)
    _know(control, PRESENT, ABSENT)
    assert _argues_to(control, PRESENT, ABSENT), "the control forms no argue: the planted failure above cannot see a removal"


def test_a_person_placed_with_him_forms_it():
    w, _ = _world(telling_hearers="seen_since_move")
    _utter_witnessed(w, PRESENT)
    _know(w, PRESENT, ABSENT)
    assert _argues_to(w, PRESENT, ABSENT) == []
    _sighting(w, PRESENT, ABSENT)                   # his newest firsthand claim places ABSENT with him
    assert _argues_to(w, PRESENT, ABSENT)


def test_a_row_asking_its_subject_to_be_with_him_forms_on_nobody_he_believes_elsewhere():
    w, _ = _world(telling_hearers="seen_since_move")
    _know(w, PRESENT, ABSENT)
    # `train`'s, `tend`'s, `fight`'s ... cell is `with` of `subject`: the question carries ABSENT as a referent through `exists:Person`
    control, _ = _world(telling_hearers="known")
    _know(control, PRESENT, ABSENT)
    seen_by_control = _on_subject(control, PRESENT, ABSENT)
    assert seen_by_control, "the control arm forms nothing on him: the arm under test cannot show a removal"
    assert _on_subject(w, PRESENT, ABSENT) == []
    _sighting(w, PRESENT, ABSENT)
    assert {c.verb for c in _on_subject(w, PRESENT, ABSENT)} == {c.verb for c in seen_by_control}


def test_covenant_forms_only_on_a_proposition():
    w, _ = _world()
    _utter_witnessed(w, PRESENT)
    _know(w, PRESENT, ABSENT)
    covenants = [c for c in _formed(w, PRESENT, _question(w, PRESENT)) if c.verb == "covenant"]
    assert covenants and {c.subject for c in covenants} == {HEARD}, covenants
    assert VERB_TABLE["covenant"].referent_class == "Proposition"
