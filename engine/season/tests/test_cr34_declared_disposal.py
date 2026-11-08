"""v11 CR-34 -- THE DECLARED DISPOSAL IS READ: A VOTE AT A SITTING COUNTS LIVE COMMITS (C-7, `ED-SC-0034`; H-161).

`determine` on a matter whose docket item names an arrangement row declaring `disposal: declared` gains one
conjunct, `vote`, in the `quorum` conjunct's shape: at least the row's OWN `quorum:` distinct members of the
bench (`judging_set`) hold a LIVE `commit` to an OUGHT Proposition whose subject is the party and whose predicate
names the kind the row `disposes:` (`ban`). `world_q.declared_votes` computes it when read and stores nothing.
`excommunication_deliberation` is the first declared row, `quorum: 2`. [ASSUMPTION; medium; Jordan to correct;
revert: any Proposition about the party; disposal bench on that row.]

REALM REACH IS 0 and this file does not claim otherwise: no computed `open_case` names an arrangement (H-80), so
the realm never meets a declared row; the evidence is the hand-built worlds below. The residue is the realm's own
-- a computed docket item that names an arrangement (a petition route reaching computed play, or `judging_set`'s
mapping) would make the clause live there. The seeded realm hash reading is in the item's receipt.

The world is `test_u7_remit.py`'s (`probes.tiny_world`) with the Duke's seat ended and THREE Church seats at the
duchy `D`, held by `p_high`, `p_low` and `p_other`; the accused is `p_mid`, who lives in `Hh` under `D`.

FALSIFIER: one bench member committed to an OUGHT about the accused naming `ban` -> `determine.refused` on the
`vote` clause; two -> admitted and the `ban` opens; one plus a member's commit to a faction creed whose subject is
the accused (the accused being his faction's leader) -> refused.
CONTROLS: (1) the second qualifying commit ENDED -> refused (live edges only); (2) a `legal_trial` matter in the
same world is admitted exactly as before; (3) at `quorum: 1` with the determiner himself committed, the result
equals the row read as `bench`. Each seen red with the mechanism removed, then restored (see the receipt).
"""

from __future__ import annotations

import pytest

from ..data import arrangements as A
from ..data.requires import UNKNOWN
from ..data.verbs import VERB_TABLE
from ..queries import world_q
from ..queries.world_q import WorldReader
from ..state.carriers import Office, Proposition, Tenure
from .test_u7_remit import DUKE, JUDGE, PARTY, _determine, _fold, _kinds, _world

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


def _bans(w):
    return [t for t in w.tenures if t.kind == "ban" and t.subject == PARTY and t.live]


def _reads(event):
    return {o.predicate: o.value for o in event.observed}


def test_the_bench_is_three_church_seat_holders_and_the_row_is_declared_at_two():
    """The setup's control: the bench the clause counts is the three planted holders, and the shipped row is
    `declared` with `quorum: 2` -- so the tests below fail on the clause and not on a bench that never formed."""
    w, _ = _church_world()
    assert sorted(world_q.judging_set(w, "D", PARTY)) == sorted(SEATS.values())
    assert A.ARRANGEMENTS[ROW]["disposal"] == "declared" and A.ARRANGEMENTS[ROW]["quorum"] == 2
    assert "vote" in VERB_TABLE["determine"].requires_typed.conjuncts()
    assert tuple(VERB_TABLE["determine"].refusal_for("vote")) == ("determine.refused",)


def test_one_vote_is_refused_on_the_vote_clause_two_open_the_ban():
    w, d = _church_world()
    _vote_against(w, "p_low")
    out = _determine_now(w, d, "dt1")
    assert _kinds(out) == ["determine.refused"], _kinds(out)
    assert _reads(out[0])["declared.votes"] == 1 and _reads(out[0])["declared.quorum"] == 2, _reads(out[0])
    assert _bans(w) == [] and world_q.docketed(w, PARTY), "a refused determination opened a ban or took the matter off"
    # The same world, one more member: admitted and the ban opens (so the refusal above was the clause's).
    _vote_against(w, "p_other")
    out = _determine_now(w, d, "dt2")
    assert _kinds(out) == ["matter.determined"] and out[0].degree in ("Overwhelming", "Success"), (
        _kinds(out), out[0].degree)
    assert len(_bans(w)) == 1 and not world_q.docketed(w, PARTY)


def test_a_commit_to_a_creed_whose_subject_is_the_accused_is_not_a_vote():
    """THE LOYAL-CREED HAZARD. The accused is his faction's leader, so a member's creed commit has HIM as its
    subject (`harness/populated.py`'s creed Propositions); its predicate is not the disposal's kind, so it is not
    a vote against him. One real vote plus one creed commit is one vote: refused."""
    w, d = _church_world()
    _vote_against(w, "p_low")
    _commit(w, "p_other", "fac_creed", predicate="carries the creed of")
    out = _determine_now(w, d)
    assert _kinds(out) == ["determine.refused"] and _reads(out[0])["declared.votes"] == 1, (_kinds(out), _reads(out[0]))
    assert _bans(w) == []


@pytest.mark.parametrize("shape", ["other_subject", "other_mood", "other_predicate"])
def test_a_commit_that_is_not_to_an_ought_about_the_party_naming_the_kind_is_not_a_vote(shape):
    """The three limbs of the rule, each on its own: a commit whose SUBJECT is somebody else, whose mood is not
    OUGHT, or whose predicate does not name the kind. Each stands in for the second vote beside one real one."""
    w, d = _church_world()
    _vote_against(w, "p_low")
    kw = {"other_subject": dict(subject="p_king"), "other_mood": dict(mood="HOLDS"),
          "other_predicate": dict(predicate="detain")}[shape]
    _commit(w, "p_other", f"prop_{shape}", **kw)
    out = _determine_now(w, d)
    assert _kinds(out) == ["determine.refused"] and _reads(out[0])["declared.votes"] == 1, (shape, _reads(out[0]))


def test_control_1_an_ended_second_commit_is_refused_live_edges_only():
    w, d = _church_world()
    _vote_against(w, "p_low")
    _vote_against(w, "p_other", until=0)
    out = _determine_now(w, d)
    assert _kinds(out) == ["determine.refused"] and _reads(out[0])["declared.votes"] == 1, _reads(out[0])
    assert _bans(w) == []


def test_two_commits_by_one_member_are_one_vote():
    """DISTINCT members: a member holding two live commits (two Propositions naming the kind) is one vote."""
    w, d = _church_world()
    _vote_against(w, "p_low")
    _commit(w, "p_low", "prop_ban_mid_again")
    out = _determine_now(w, d)
    assert _kinds(out) == ["determine.refused"] and _reads(out[0])["declared.votes"] == 1, _reads(out[0])


def test_a_commit_by_a_non_member_is_not_a_vote():
    """The bench is `judging_set`'s: a person holding no judging seat who commits to the same Proposition is no
    member and counts for nothing."""
    w, d = _church_world()
    _vote_against(w, "p_low")
    _vote_against(w, "p_king")
    out = _determine_now(w, d)
    assert _kinds(out) == ["determine.refused"] and _reads(out[0])["declared.votes"] == 1, _reads(out[0])


def test_control_2_a_bench_disposal_matter_in_the_same_world_is_admitted_as_before():
    """`legal_trial` (`disposal: bench`) in the same world, with NO commits at all: admitted. The `vote` conjunct
    reads 0 against 0 for it and refuses nothing."""
    assert A.ARRANGEMENTS["legal_trial"]["disposal"] == "bench"
    w, d = _church_world(row="legal_trial")
    out = _determine_now(w, d)
    assert _kinds(out) == ["matter.determined"], _kinds(out)
    reads = _reads(out[0])
    assert reads["declared.votes"] == 0 and reads["declared.quorum"] == 0, reads
    assert not world_q.docketed(w, PARTY)


def test_a_matter_naming_no_arrangement_reads_zero_against_zero():
    """The computed docket's case (H-80: no arrangement named): the clause is vacuous, `0 >= 0`."""
    w, _ = _church_world(row=None)
    r = WorldReader(w, DUKE)
    assert r.read(PARTY, "declared.votes") == 0 and r.read(PARTY, "declared.quorum") == 0


@pytest.mark.parametrize("quorum", [1, 2, 3])
def test_the_rows_own_quorum_key_is_the_threshold_swept(quorum, monkeypatch):
    """H-161's sweep {1, 2, 3} on the row's own key: with exactly two votes, admitted at 1 and 2, refused at 3."""
    monkeypatch.setitem(A.ARRANGEMENTS[ROW], "quorum", quorum)
    w, d = _church_world()
    _vote_against(w, "p_low")
    _vote_against(w, "p_other")
    out = _determine_now(w, d)
    assert _kinds(out) == (["matter.determined"] if quorum <= 2 else ["determine.refused"]), (quorum, _kinds(out))
    assert _reads(out[0])["declared.quorum"] == quorum


def test_control_3_at_quorum_one_with_the_determiner_committed_the_result_equals_the_bench_reading(monkeypatch):
    """At `quorum: 1` the determiner's own live commit is the one vote, and the outcome is what the same matter
    gives when the row is read as `bench` (today's): a determination, one `ban`."""
    monkeypatch.setitem(A.ARRANGEMENTS[ROW], "quorum", 1)
    w, d = _church_world()
    _vote_against(w, "p_high")
    declared = _determine_now(w, d)
    declared_bans = len(_bans(w))
    monkeypatch.setitem(A.ARRANGEMENTS[ROW], "disposal", "bench")
    monkeypatch.setitem(A.ARRANGEMENTS[ROW], "quorum", None)
    w2, d2 = _church_world()
    _vote_against(w2, "p_high")
    bench = _determine_now(w2, d2)
    assert _kinds(declared) == _kinds(bench) == ["matter.determined"], (_kinds(declared), _kinds(bench))
    assert declared_bans == len(_bans(w2)) == 1
    assert declared[0].degree == bench[0].degree


def test_an_ambiguous_docket_is_refused_and_reads_unknown_not_a_guessed_row():
    """TWO docket items for one matter, one under the declared row (a hand-planted docket: `open_case` declines a
    matter already docketed). `declared_sitting` answers `UNKNOWN` rather than choosing the declared row, and
    `_eff_determine` declines it, so even with the quorum of votes in hand nothing opens. PLANTED FAILURE:
    `declared_sitting` returning the declared row whatever else the matter is docketed under -- the first
    assertion, red."""
    w, d = _church_world()
    _vote_against(w, "p_low")
    _vote_against(w, "p_other")                     # two live votes: the declared row alone would admit
    w.docket.append({"date": None, "matter": PARTY, world_q.DOCKET_ARRANGEMENT: None,
                     world_q.DOCKET_PETITION: None})
    assert world_q.docketed_under(w, PARTY) == {ROW, None}
    assert world_q.declared_sitting(w, PARTY) is UNKNOWN
    out = _determine_now(w, d)
    assert _kinds(out) == ["determine.refused"], _kinds(out)
    assert _bans(w) == [] and len(world_q.docketed(w, PARTY)) == 2, "a refused determination opened a ban or moved the docket"


def test_the_tally_is_stored_nowhere():
    """Computed when read: the count follows the edges. End a vote and the next read falls; nothing was kept."""
    w, _ = _church_world()
    r = WorldReader(w, DUKE)
    assert r.read(PARTY, "declared.votes") == 0
    _vote_against(w, "p_low")
    _vote_against(w, "p_other")
    assert r.read(PARTY, "declared.votes") == 2
    for t in w.tenures:
        if t.kind == "commit" and t.subject == "p_other":
            t.until = 0
    assert r.read(PARTY, "declared.votes") == 1
