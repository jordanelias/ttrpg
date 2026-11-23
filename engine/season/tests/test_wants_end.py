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
from ..decision.options import opening_set
from ..queries import world_q
from ..state.carriers import Claim, Person, Proposition, Tenure, View
from ..state.world import World
from .test_fi_referents import hears_of

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


def _claim(cid, subject, predicate, when=0) -> Claim:
    return Claim(cid, "p_o", subject, predicate, True, when, "firsthand", 100, "own")


def _world(ledger) -> World:
    """`p_o` is committed to the throne goal (the want), whose seat `p_a` holds; `p_o` holds `ledger`."""
    w = World(0)
    w.propositions[THRONE] = Proposition(THRONE, "OUGHT", "subj_" + THRONE, f"{THRONE} ought", True, 0)
    for pid in ("p_a", "p_o"):
        w.persons[pid] = Person(pid, pid)
    w.persons["p_a"].tenures.append(Tenure("t_hold_p_a", "p_a", SEAT, "hold", 0))
    w.persons["p_o"].tenures.append(Tenure("t_commit_p_o", "p_o", THRONE, "commit", 0))
    w.persons["p_o"].ledger = list(ledger)
    hears_of(w.persons["p_o"], SEAT, "p_a", when=-2)       # v12 B11.08: who holds the seat is the claims he holds of it, long known
    return w


def _needs(ledger) -> list:
    """The `need` questions `p_o` is asked, committed to the throne goal whose holder is `p_a`."""
    w = _world(ledger)
    assert world_q.aim_state(w, w.persons["p_o"], w.propositions[THRONE]) == "open", "the world does not hold it met"
    return [q for q in world_q.questions_for(w, w.persons["p_o"]) if q.source == "need"]


def test_a_believed_met_want_raises_no_need_question():
    both = [_claim("c1", "p_a", "exists:Person"), _claim("c2", "p_a", "held_by:p_o")]
    with goals.rows_replaced(goals.parse(_doc())):
        assert [q.id for q in _needs(both[:1])] == [f"q:need:{THRONE}"], "one stage passed: the want is still asked"
        assert _needs(both) == [], "both stages passed in his own ledger: he believes it met and is not asked"


def test_release_forms_on_his_own_commit_and_on_nobody_elses():
    """B10.72 (SITE): the `need` question names the seat's HOLDER (`p_a`), never the committed Proposition, so before the
    build `release` formed on `p_a` and could close nothing of `p_o`'s. A held `commit` is now a referent of `release`
    (`rosters.yaml: held_edge_sourced`): `p_o` is offered `release` on the throne goal he is committed to; `p_a`, who holds
    no commit to it, is not, on the very same question. PLANTED FAILURE: the roster line deleted reddens the first assertion."""
    w = _world([])

    def release_subjects(pid):
        p = w.persons[pid]
        return {c.subject for c in opening_set(p, View(p.id, [], w.fixtures.get("view_k"), q), q, w.fixtures)
                if c.verb == "release"}

    with goals.rows_replaced(goals.parse(_doc())):
        q = world_q.questions_for(w, w.persons["p_o"])[0]
        assert q.referents == ("p_a",), "the question names the seat's holder, not the want"
        assert THRONE in release_subjects("p_o"), "his own commit is offered for laying down"
        assert THRONE not in release_subjects("p_a"), "a commit he does not hold is not his to release"


def test_commitment_kept_reads_the_releasers_own_ledger():
    """B10.72 (U5a `CHAR` §3 (b)): was the want he laid down KEPT -- both stages' claims in HIS OWN ledger at the tick the edge
    closed (`Tenure.until`)? A claim missing, one that arrived after the closing tick, and a want with no stage row each read
    not kept; the same world with both claims in time reads kept. PLANTED FAILURE: dropping the `when <= until` filter reddens
    the third assertion; reading the world's seat (`p_a` does hold the throne's claims) instead of the ledger, the second."""
    both = lambda when2: [_claim("c1", "p_a", "exists:Person"), _claim("c2", "p_a", "held_by:p_o", when2)]
    with goals.rows_replaced(goals.parse(_doc())):
        def kept(ledger, until=5):
            w = _world(ledger)
            t = w.persons["p_o"].tenures[0]
            t.until = until
            return world_q.commitment_kept(w, t)

        assert kept(both(3)) is True, "both stages held true before it closed: kept"
        assert kept(both(3)[:1]) is False, "one stage never held: not kept"
        assert kept(both(9)) is False, "the second stage reached him after he had let it go: not kept"
    w = _world([])                      # no `goal_stages` row for this goal: no content a ledger can read
    t = w.persons["p_o"].tenures[0]
    t.until = 5
    assert world_q.commitment_kept(w, t) is False, "a want with no readable content is not read kept"
