"""B10.59 -- WHAT THE ACTOR CAN READ OFF HIMSELF IS DECLINED AT FORMATION (`decision/options.py::opening_set`, the K-3 branch
widened; `queries/person_q.py::OwnStateReader`).

The reader answers, of the person himself and from his own state alone: his Thread Sensitivity (the K-3 pair), whether he
holds an object (`held_by`: his own live `hold` Tenures), whether his own judgement scores a man's deeds against him
(`dispute`: `person_q.holds_dispute`) and whether he is an individual (`individual`, asked of the actor). A conjunct it
answers False declines the Candidate; a conjunct it cannot answer is UNKNOWN and the Candidate forms (clause 4's belief
polarity is untouched). Skill is never a requirement, so no stem for it is answered.

B10.60 adds `relation: individual` of `actor` to eight rows (`challenge` already carried it), so a cohort forms none of them
and the fold refuses a hand-built one.

GAME STATE, lane `season_loop` (`engine/season/tests/`). The roster test is B10.61's."""
from __future__ import annotations

from ..data.requires import REQUIRES_STEMS, UNKNOWN
from ..data.verbs import VERB_TABLE
from ..decision import assemble
from ..decision.options import opening_set
from ..harness import probes as P
from ..loop.driver import SeasonDriver
from ..queries.person_q import OwnStateReader
from ..state.carriers import Act, Claim, Question

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


# --- B10.60: a population does not take an individual's acts --------------------------------------------------------

#: item 5's set, each with the payload on which the CAST person is admitted at a hearth `Hh` in `tiny_world`.
_INDIVIDUAL_ROWS = {"challenge": {"subject": B}, "forge": {"subject": "Valorsmark"}, "sabotage": {"site": "site_harbour"},
                    "train": {"subject": B}, "create_record": {}, "conceal": {}, "interview": {"subject": B},
                    "surveil": {"subject": "Hh"}}


def _admitted(w, pid, verb):
    """`(ok, refusal kinds)` the fold's own admission gives `pid` a hand-built `verb` act on `_INDIVIDUAL_ROWS`'s payload."""
    d = SeasonDriver(w)
    ok, kinds, _verdict = d._admits(w, Act(f"act:{verb}:{pid}", pid, verb, payload=dict(_INDIVIDUAL_ROWS[verb])),
                                    VERB_TABLE[verb])
    return ok, tuple(kinds)


def _equipped(pid, w):
    """What the eight rows' OTHER conjuncts ask of `pid`: a deed claim his pursuits judge (`challenge`'s dispute) and a
    claim held on a faction (`forge`'s own-ledger cell). A cohort is handed the same, so the cast person and the
    cohort differ only in being one."""
    p = w.persons[pid]
    p.ledger.append(Claim(f"c_{pid}_deed", pid, B, "fight.declared", True, w.tick, "firsthand", 100, "own"))
    p.ledger.append(Claim(f"c_{pid}_seat", pid, "Valorsmark", "faction.head", "x", w.tick, "firsthand", 100, "own"))
    p.pursuits = {"liberty": 1.0}


def test_a_cohort_forms_none_of_the_individual_rows():
    """A cohort and a cast person handed the same act, at the same hearth with the same ledger, differ by exactly the
    rows carrying the actor's `individual` conjunct: the cast person is admitted on all eight, the cohort on none."""
    w = P.tiny_world()
    P.plant_cohort(w, "p_folk", "Hh")
    P.plant_cohort(w, "p_town", "S")                     # `sabotage` asks the actor at the site's own rung, `S`
    for pid in (A, "p_high", "p_folk", "p_town"):
        _equipped(pid, w)
    at_hearth = {v: (A, "p_folk") for v in _INDIVIDUAL_ROWS}
    at_hearth["sabotage"] = ("p_high", "p_town")
    admitted_cast = {v for v, (cast, _) in at_hearth.items() if _admitted(w, cast, v)[0]}
    admitted_cohort = {v for v, (_, cohort) in at_hearth.items() if _admitted(w, cohort, v)[0]}
    assert admitted_cast == set(_INDIVIDUAL_ROWS), set(_INDIVIDUAL_ROWS) - admitted_cast
    assert admitted_cohort == set(), admitted_cohort
    # and at formation (B10.59's reader): handed one question about a person, the two differ by exactly the rows
    # carrying the conjunct -- `challenge` is formed only on a `Disputant` referent, so it is not on this question
    q = Question("q:offer", "claim_landed", (B,), None, ((B, "Person"),))
    formed = {pid: {c.verb for c in opening_set(w.persons[pid], assemble(w.persons[pid], q, 12), q, w.fixtures)}
              for pid in (A, "p_folk")}
    rows = set(_INDIVIDUAL_ROWS) - {"challenge"}
    assert rows <= formed[A], rows - formed[A]
    assert not rows & formed["p_folk"], rows & formed["p_folk"]
    assert formed[A] - formed["p_folk"] == rows, (formed[A] - formed["p_folk"]) ^ rows
