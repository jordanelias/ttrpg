"""v11 CR-34, AS B24.11 LEFT IT -- A DECLARED ROW'S COMMITS ARE READ, AND GATE NOTHING (C-7, `ED-SC-0034`; H-161).

`determine` on a matter whose docket item names an arrangement row closing `declared` once carried a fifth conjunct, `vote` (the row's own `quorum:` of
live commits as a hard precondition). B24.11 deleted it: the count is the odds, not a gate. What stays here is the READING of the commits
(`world_q.declared_votes_by_member`, signed per member), which `sigma._present` turns into each seat's
starting track, and the control that the matter is no longer refused for want of them. The sitting those starts feed is `test_sc_hearing_ballots.py`'s.
`excommunication_deliberation` is the first declared row, `quorum: 2`.

The world is `test_u7_remit.py`'s (`probes.tiny_world`) with the Duke's seat ended and THREE Church seats at the duchy `D`, held by `p_high`, `p_low` and
`p_other`; the accused is `p_mid`, who lives in `Hh` under `D`.
"""

from __future__ import annotations

import pytest

from ..data import arrangements as A
from ..data.verbs import VERB_TABLE
from ..queries import world_q
from ..state.carriers import Office, Proposition, Tenure
from .test_u7_remit import JUDGE, PARTY, _determine, _fold, _kinds, _world

ROW = "excommunication_deliberation"
CHURCH = "Church of Solmund"
SEATS = {"off_cs1": "p_high", "off_cs2": "p_low", "off_cs3": "p_other"}       # seat -> holder
JUDGE_SEAT = "off_cs1"


def _church_world(row=ROW, **fx):
    """`tiny_world` with its Duke's hold ended and three Church seats on `D`; the accused `p_mid` docketed under `row`."""
    w, d = _world(**{**JUDGE, **fx})
    for t in list(w.tenures):
        if t.kind == "hold" and t.object == "off_duke":
            t.until = 0
    for n, (seat, who) in enumerate(SEATS.items()):
        off = Office(seat, "Dicastery", "D", ["issue", "determine"], faction=CHURCH)
        off.scope_rung = "D"
        w.offices[seat] = off
        w.add_tenure(Tenure(f"t_hold_{n}", who, seat, "hold", since=0))
    w.docket.append({"date": None, "matter": PARTY, world_q.DOCKET_ARRANGEMENT: row,
                     world_q.DOCKET_PETITION: None})
    return w, d


def _commit(w, who, prop_id, subject=PARTY, predicate="ban", mood="OUGHT", until=None, key=None):
    if prop_id not in w.propositions:
        w.propositions[prop_id] = Proposition(prop_id, mood, subject, predicate, True, 0)
    w.add_tenure(Tenure(key or f"cm_{who}_{prop_id}", who, prop_id, "commit", since=0, until=until))


def _vote_against(w, who, until=None):
    _commit(w, who, "prop_ban_mid", until=until)


def _determine_now(w, d, key="dt"):
    return _fold(w, d, _determine(key, via=JUDGE_SEAT, actor="p_high"))


def _row():
    return A.ARRANGEMENTS[ROW]


def _by_member(w):
    return world_q.declared_votes_by_member(w, PARTY, _row())


def _for_the_motion(w):
    """The members whose signed count is positive: how many distinct members vote for the motion."""
    return sum(1 for n in _by_member(w).values() if n > 0)


def test_the_bench_is_three_church_seat_holders_and_the_row_is_declared_at_two():
    """The setup's control: the bench the commits are read over is the three planted holders, the shipped row is `declared` with `quorum: 2`, and the
    `vote` conjunct is gone from `determine` (the keyed refusal with it)."""
    w, _ = _church_world()
    assert sorted(world_q.judging_set(w, "D", PARTY)) == sorted(SEATS.values())
    assert A.ARRANGEMENTS[ROW]["close"] == "declared" and A.ARRANGEMENTS[ROW]["quorum"] == 2
    assert "vote" not in VERB_TABLE["determine"].requires_typed.conjuncts()
    assert set(VERB_TABLE["determine"].requires_typed.conjuncts()) == {"party", "docket", "bench", "quorum"}


def test_a_declared_determine_with_no_commit_at_all_is_admitted_and_sat():
    """The count is no longer a gate: with NO bench member committed to anything, the declared matter is formed and heard (it was refused on `vote` before B24.11), and
    the sitting's draw decides it -- a determination or an undetermined matter, never `determine.refused`. The one-seed observation; the seeds are `test_sc_hearing_ballots`'s."""
    w, d = _church_world()
    assert _by_member(w) == {}
    out = _determine_now(w, d)
    assert _kinds(out)[0] in ("matter.determined", "matter.undetermined"), _kinds(out)


def test_a_commit_is_read_per_member_signed_for_the_motion_or_against_it():
    """One live commit to an OUGHT about the accused naming `ban` is `+1` for the member; the same Proposition's NEGATION (`value` false) is `-1`; a member with neither is
    absent; the members for the motion are those read positive."""
    w, _ = _church_world()
    _vote_against(w, "p_low")
    w.propositions["prop_spare"] = Proposition("prop_spare", "OUGHT", PARTY, "ban", False, 0)
    _commit(w, "p_other", "prop_spare")
    assert _by_member(w) == {"p_low": 1, "p_other": -1}
    assert _for_the_motion(w) == 1


def test_a_commit_to_a_creed_whose_subject_is_the_accused_is_no_commit_on_the_motion():
    """THE LOYAL-CREED HAZARD. The accused is his faction's leader, so a member's creed commit has HIM as its subject (`harness/populated.py`'s creed
    Propositions); its predicate is not the disposal's kind, so it is no commit on the motion."""
    w, _ = _church_world()
    _vote_against(w, "p_low")
    _commit(w, "p_other", "fac_creed", predicate="carries the creed of")
    assert _by_member(w) == {"p_low": 1}


@pytest.mark.parametrize("shape", ["other_subject", "other_mood", "other_predicate"])
def test_a_commit_that_is_not_to_an_ought_about_the_party_naming_the_kind_is_not_read(shape):
    """The three limbs of the rule, each on its own: a commit whose SUBJECT is somebody else, whose mood is not OUGHT, or whose predicate does not name the kind."""
    w, _ = _church_world()
    _vote_against(w, "p_low")
    kw = {"other_subject": dict(subject="p_king"), "other_mood": dict(mood="HOLDS"),
          "other_predicate": dict(predicate="detain")}[shape]
    _commit(w, "p_other", f"prop_{shape}", **kw)
    assert _by_member(w) == {"p_low": 1}, shape


def test_an_ended_commit_is_no_commit_and_a_non_member_has_none():
    """Live edges only (`ambitions`), and the bench is `judging_set`'s: an ended commit and a commit by a person holding no judging seat read for nothing."""
    w, _ = _church_world()
    _vote_against(w, "p_low")
    _vote_against(w, "p_other", until=0)
    _vote_against(w, "p_king")
    assert _by_member(w) == {"p_low": 1}


def test_two_commits_by_one_member_are_two_levels_and_one_member():
    """A seat's track starts at one level a COMMIT: a member holding two live commits on the motion reads `2`, and is one member for the motion."""
    w, _ = _church_world()
    _vote_against(w, "p_low")
    _commit(w, "p_low", "prop_ban_mid_again")
    assert _by_member(w) == {"p_low": 2} and _for_the_motion(w) == 1


def test_a_matter_with_no_place_has_no_bench():
    w, _ = _church_world()
    assert world_q.declared_votes_by_member(w, "nobody_anywhere", _row()) == {}


def test_the_reading_is_stored_nowhere():
    """Computed when read: the readings follow the edges. End a commit and the next read falls; nothing was kept."""
    w, _ = _church_world()
    assert _by_member(w) == {}
    _vote_against(w, "p_low")
    _vote_against(w, "p_other")
    assert _by_member(w) == {"p_low": 1, "p_other": 1}
    for t in w.tenures:
        if t.kind == "commit" and t.subject == "p_other":
            t.until = 0
    assert _by_member(w) == {"p_low": 1}
