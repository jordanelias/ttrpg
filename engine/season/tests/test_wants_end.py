"""B10.71 -- a want a person BELIEVES met raises no standing `need` question.

THE BUILD (`world_q.questions_for`, Q4): the `need` question of an ambition is not raised while his OWN ledger reads every
stage of the goal's `goal_stages` row as passed (`current_stage` is `None` for a goal that has a row), beside the aim rule
that already skips a met rung goal (`aim_state`, CP-T02-03, observed by `test_cp_t02_03_aim_state.py`). A want with no stage
row has no content a ledger can read and is unchanged. A want he believes met that the world does not hold met is a false
belief at work, which the source intends.

  (a) BELIEF, NOT TRUTH: a holder whose ledger holds both stages' claims, on a goal whose aim reads `open`, is asked no
      `need` question; with one claim missing, the same world asks it. PLANTED FAILURE: the ledger reading dropped from
      `questions_for` reddens the first assertion.
"""
from __future__ import annotations

import copy

from ..data import goals
from ..queries import world_q
from ..state.carriers import Claim, Person, Proposition, Tenure
from ..state.world import World

SEAT = "off_king"
THRONE = "g_throne"
FIRST = {"form": "existence", "of": "subject", "kind": "Person"}
LAST = {"form": "relation", "of": "subject", "relation": "held_by"}


def _doc() -> dict:
    stages = [{"id": sid, "term": term, "predicate": copy.deepcopy(cell), "pursuits": {"honour": 1}}
              for sid, term, cell in (("s1", "short", FIRST), ("s2", "long", LAST))]
    return {"goals": [{"id": THRONE, "org": {"faction": "Valorsmark"}, "text": f"{THRONE}, as a predicate",
                       "object": {"kind": "seat_holders", "seats": [SEAT]}, "pursuits": {"stability": 1},
                       "source": "test_wants_end", "stance": 1}],
            "goal_stages": [{"id": "gs_throne", "for": [THRONE], "stages": stages}]}


def _claim(cid, subject, predicate) -> Claim:
    return Claim(cid, "p_o", subject, predicate, True, 0, "firsthand", 100, "own")


def _needs(ledger) -> list:
    """The `need` questions `p_o` is asked, committed to the throne goal whose holder is `p_a`."""
    w = World(0)
    w.propositions[THRONE] = Proposition(THRONE, "OUGHT", "subj_" + THRONE, f"{THRONE} ought", True, 0)
    for pid in ("p_a", "p_o"):
        w.persons[pid] = Person(pid, pid)
    w.persons["p_a"].tenures.append(Tenure("t_hold_p_a", "p_a", SEAT, "hold", 0))
    w.persons["p_o"].tenures.append(Tenure("t_commit_p_o", "p_o", THRONE, "commit", 0))
    w.persons["p_o"].ledger = list(ledger)
    assert world_q.aim_state(w, w.persons["p_o"], w.propositions[THRONE]) == "open", "the world does not hold it met"
    return [q for q in world_q.questions_for(w, w.persons["p_o"]) if q.source == "need"]


def test_a_believed_met_want_raises_no_need_question():
    both = [_claim("c1", "p_a", "exists:Person"), _claim("c2", "p_a", "held_by:p_o")]
    with goals.rows_replaced(goals.parse(_doc())):
        assert [q.id for q in _needs(both[:1])] == [f"q:need:{THRONE}"], "one stage passed: the want is still asked"
        assert _needs(both) == [], "both stages passed in his own ledger: he believes it met and is not asked"
