"""B11.70 (`08_FI_03` §1 with `08_FI_07` §1): THE INQUIRY WORLD -- `harness/scenarios.py::inquiry_world`.

The world is a premise folded through the season loop's own steps (a forging, a move, a handover) with no claim planted in
the investigator's ledger: his case is a goal whose `deed_doers` referents are his suspects, empty until his OWN ledger names
someone. `test_every_inquiry_world_run_ends_by_a_predicate` is B11.76's (it needs the ending).
"""
from __future__ import annotations

from ..data import goals as goals_data
from ..harness import scenarios as S
from ..queries import world_q
from ..state.carriers import Claim


def test_inquiry_world_builds_its_six_parts_and_seeds_one_case_goal():
    """The six persons and the bench exist; the sheet was forged, handed on and is held by the holder; the witness saw the
    handover and not the forging; the investigator holds one goal whose object is `deed_doers` and whose referents are
    empty at build. FALSIFIER: a builder that authors an outcome (a claim naming the forger in the investigator's ledger)
    fails the last two asserts; the control below is the same read once his ledger does name the forger."""
    w = S.inquiry_world(0)
    assert set(S.INQUIRY_CAST) <= set(w.persons) and len(S.INQUIRY_CAST) == 6
    assert world_q.judging_set(w, S.TOWN) == ["p_bench_a", "p_bench_b", "p_investigator"]
    forged = [e for e in w.log if e.kind == "record.forged"]
    given = [e for e in w.log if e.kind == "record.given"]
    assert len(forged) == len(given) == 1, "the sheet was forged and handed on once"
    (rid,) = [c.subject for c in forged[0].changes]
    assert world_q.hold_force(w, rid).subject == "p_holder"
    ledger = lambda pid: w.persons[pid].ledger
    assert any(c.predicate == "record.given" for c in ledger("p_witness")), "the witness was at the handover"
    assert not any(c.predicate == "record.forged" for c in ledger("p_witness")), "and not at the forging"
    assert any(c.predicate == "record.forged" for c in ledger("p_forger")), "the forger holds his own deed"
    inv = w.persons["p_investigator"]
    mine = [t.object for t in w.tenures if t.kind == "commit" and t.subject == inv.id and t.object in w.propositions
            and goals_data.goal(t.object) is not None]
    assert mine == [S.CASE_GOAL], "the investigator holds exactly one goal"
    goal = goals_data.goal(S.CASE_GOAL)
    assert goal.object["kind"] == "deed_doers" and set(goal.object["kinds"]) >= {"record.forged"}
    assert not [c for c in inv.ledger if c.predicate in goal.object["kinds"]], "the investigator's ledger holds a covert deed at build"
    assert not [c for c in inv.ledger if c.subject == rid], "and nothing of the sheet"
    prop = w.propositions[S.CASE_GOAL]
    assert world_q.goal_referents(w, inv, prop) == ()
    # CONTROL: the reader sees a name once his own ledger holds one, wrongly or rightly.
    inv.ledger.append(Claim("c_ctl", inv.id, "p_forger", "record.forged", True, w.tick, "told", 1, "own"))
    assert world_q.goal_referents(w, inv, prop) == ("p_forger",)
    assert S.inquiry_world(0).content_hash() == S.inquiry_world(0).content_hash()
