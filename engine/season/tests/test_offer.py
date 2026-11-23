"""B10.59 -- WHAT THE ACTOR CAN READ OFF HIMSELF IS DECLINED AT FORMATION (`decision/options.py::opening_set`, the K-3 branch
widened; `queries/person_q.py::OwnStateReader`).

The reader answers, of the person himself and from his own state alone: his Thread Sensitivity (the K-3 pair), whether he
holds an object (`held_by`: his own live `hold` Tenures), whether his own judgement scores a man's deeds against him
(`dispute`: `person_q.holds_dispute`) and whether he is an individual (`individual`, asked of the actor). A conjunct it
answers False declines the Candidate; a conjunct it cannot answer is UNKNOWN and the Candidate forms (clause 4's belief
polarity is untouched). Skill is never a requirement, so no stem for it is answered.

GAME STATE, lane `season_loop` (`engine/season/tests/`). The cohort and roster tests are B10.60's and B10.61's."""
from __future__ import annotations

from ..data.requires import REQUIRES_STEMS, UNKNOWN
from ..data.verbs import VERB_TABLE
from ..decision import assemble
from ..decision.options import opening_set
from ..harness import probes as P
from ..queries.person_q import OwnStateReader
from ..state.carriers import Claim, Question

A, B = "p_mid", "p_low"            # `tiny_world`: both stand at the hearth


def _challenges_on(w, pid, referent):
    """`pid`'s `challenge` Candidates on one question that carries `referent` as a `Disputant` -- the stamp
    `world_q.disputes_held` would give a man he holds a grievance with, here hand-built so that it is carried WHETHER OR
    NOT the person holds one (the stamp's own filter is not what this observes)."""
    p = w.persons[pid]
    cls = VERB_TABLE["challenge"].referent_class
    q = Question(f"q:challenge:{referent}", "claim_landed", (referent,), None, ((referent, cls),))
    return [c for c in opening_set(p, assemble(p, q, 12), q, w.fixtures) if c.verb == "challenge"]


def test_a_person_with_no_dispute_forms_no_challenge_and_one_with_it_does():
    w = P.tiny_world()
    assert not _challenges_on(w, A, B), "he holds no dispute against his man and still formed the challenge"
    p = w.persons[A]
    p.ledger.append(Claim("c_offer_deed", A, B, "fight.declared", True, w.tick, "firsthand", 100, "own"))
    p.pursuits = {"liberty": 1.0}              # the deed is judged against its doer (`test_b11a_duel_reach._grievance`)
    assert [c.subject for c in _challenges_on(w, A, B)] == [B]


def test_the_reader_answers_what_a_person_holds_and_is_of_himself_and_nobody_elses():
    w = P.tiny_world()
    P.plant_cohort(w, "p_folk", "Hh")
    duke, folk = w.persons["p_high"], w.persons["p_folk"]
    # `held_by`: his own live `hold` Tenure, asked of the actor only
    assert OwnStateReader(duke, w.fixtures).read("off_duke", f"held_by:{duke.id}") is True
    assert OwnStateReader(w.persons[A], w.fixtures).read("off_duke", f"held_by:{A}") is False
    assert OwnStateReader(w.persons[A], w.fixtures).read("off_duke", f"held_by:{duke.id}") is UNKNOWN
    # `individual`: asked of the actor, a cohort is not one; of anybody else it is the world's
    assert OwnStateReader(duke, w.fixtures).read(duke.id, f"individual:{duke.id}") is True
    assert OwnStateReader(folk, w.fixtures).read(folk.id, f"individual:{folk.id}") is False
    assert OwnStateReader(duke, w.fixtures).read(folk.id, f"individual:{duke.id}") is UNKNOWN
