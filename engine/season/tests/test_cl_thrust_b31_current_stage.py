"""CL-THRUST B3.1 (batch B10-05 landing) -- `world_q.current_stage(w, p, ambition)`, READ PERSON-SIDE.

For each referent of an ambition (`goal_referents`), the FIRST stage of the ambition's `goal_stages` row
(`data/goals.py`, B2) whose `predicate` is not TRUE of that referent, evaluated by `data/requires.py::
evaluate` against `LedgerReader(p.ledger)` -- the person's own claims, never the world -- with
`subject := the referent` and `actor := p.id`. The return is `{referent: Stage}` (a referent that has passed
every stage absent) or `None`. Nothing calls it yet (R2, the stage's referents in the person's `need`
question, is B3.2): no behaviour moves and no stored carrier is written.

What each test proves, and the failure it can observe:

  (a) BELIEF, NOT TRUTH (the section's falsifier): a person whose ledger holds the stage-1 claim reads
      stage 2; one whose ledger lacks it reads stage 1 although the WORLD satisfies the cell (asserted by
      running the same cell against `WorldReader`). PLANTED FAILURE, RUN BOTH WAYS: the reader swapped for
      `WorldReader` inside the test (`test_a_reader_of_the_world_..._reads_the_lacking_person_one_stage_on`)
      and, by hand, in the source (`world_q.current_stage` reading `WorldReader(w, p.id)`), which reddens (a).
  (b) A COMPLETE SEQUENCE READS `None`, and a referent that has passed every stage is absent while its
      sibling is not (the per-referent reading, TL §3.1 R1: *"the first stage whose predicate is not TRUE
      for each referent"*).
  (c) AN UNKNOWN PREDICATE DOES NOT PASS A STAGE: the verdict is asserted to BE UNKNOWN (an empty ledger; an
      `own_ledger` cell, which `LedgerReader` never answers), so the case is the one it names; a claim that
      reads FALSE does not pass either.
  (d) `actor := p.id`: a relation cell is TRUE only on the claim `held_by:<the person himself>`.
  (e) CONTROL: with no `goal_stages` row `current_stage` is `None` for every shipped goal and for every
      ambition of the seed-0 realm (the loop asserts it checked at least the floor, `CLAUDE.md` §0.1 pt 2),
      and with a row planted on a shipped goal it is not -- so the control can observe the thing it excludes.
  (f) COMPUTED WHEN ASKED, STORED NOWHERE: the world's content hash and the person's ledger and tenures are
      unchanged by a call; a Proposition no goal names, and an id the world minted no Proposition for, read
      `None`.
"""
from __future__ import annotations

import copy
import dataclasses

import pytest

from ..data import goals
from ..data.requires import UNKNOWN, binding_of, build_typed_requires, evaluate
from ..harness import populated
from ..queries import world_q
from ..queries.person_q import LedgerReader
from ..state.carriers import Claim, Person, Proposition, Tenure
from ..state.world import World

SEAT = "off_king"
THRONE = "g_throne"          # a seat_holders goal that carries a stage row
RUNG = "g_rung"              # a rung goal that carries none
# Three stages, each a cell a person's own claims can answer (`LedgerReader.read` returns the value of the
# newest claim whose predicate is the cell's derived one: `exists:<kind>`, `held_by:<actor>`).
S1 = {"form": "existence", "of": "subject", "kind": "Person"}
S2 = {"form": "relation", "of": "subject", "relation": "held_by"}
S3 = {"form": "existence", "of": "subject", "kind": "Proposition"}


def _goal(gid, org, obj, **more):
    return {"id": gid, "org": org, "text": f"{gid}, as a predicate", "object": obj,
            "pursuits": {"stability": 1}, "source": "test_cl_thrust_b31", **more}


def _stage(sid, term, cell):
    return {"id": sid, "term": term, "predicate": copy.deepcopy(cell), "pursuits": {"honour": 1}}


def _doc(*, with_row=True) -> dict:
    doc = {"goals": [
        _goal(THRONE, {"faction": "Crown"}, {"kind": "seat_holders", "seats": [SEAT]}, stance=1),
        _goal(RUNG, {"faction": "Hafenmark"}, {"kind": "rung", "rung": "terr_T9"}),
    ]}
    if with_row:
        doc["goal_stages"] = [{"id": "gs_throne", "for": [THRONE],
                               "stages": [_stage("s1", "short", S1), _stage("s2", "medium", S2),
                                          _stage("s3", "long", S3)]}]
    return doc


@pytest.fixture
def staged():
    """The hand-built goals the reader sees (the loader's own `parse`, swapped in by `rows_replaced`)."""
    with goals.rows_replaced(goals.parse(_doc())):
        yield


@pytest.fixture
def unstaged():
    with goals.rows_replaced(goals.parse(_doc(with_row=False))):
        yield


def _claim(cid, holder, subject, predicate, value=True) -> Claim:
    return Claim(cid, holder, subject, predicate, value, 0, "firsthand", 100, "own")


def _holds(pid, referent, *stages) -> list:
    """The claims whose presence passes the named stages (1, 2, 3) of `referent` for `pid`."""
    return [_claim(f"c_{pid}_{referent}_{n}", pid, referent, pred)
            for n, pred in ((1, "exists:Person"), (2, f"held_by:{pid}"), (3, "exists:Proposition"))
            if n in stages]


def _world(*observers, holders=("p_a",)):
    """A world where each observer (pid, ledger) is committed to the OUGHT `THRONE` and `holders` sit on the
    seat -- so `goal_referents` reads exactly `holders`, in order."""
    w = World(0)
    w.propositions[THRONE] = Proposition(THRONE, "OUGHT", "subj_" + THRONE, f"{THRONE} ought", True, 0)
    for pid in dict.fromkeys(list(holders) + [o for o, _ in observers]):
        w.persons[pid] = Person(pid, pid)
    for i, h in enumerate(holders):
        w.persons[h].tenures.append(Tenure(f"t_hold_{h}", h, SEAT, "hold", i))
    for pid, ledger in observers:
        w.persons[pid].tenures.append(Tenure(f"t_commit_{pid}", pid, THRONE, "commit", 0))
        w.persons[pid].ledger = list(ledger)
    return w


def _stage_ids(w, pid) -> "dict | None":
    cur = world_q.current_stage(w, w.persons[pid], THRONE)
    return None if cur is None else {r: s.id for r, s in cur.items()}


# ---------------------------------------------------------------------------------------------------
# (a) belief, not truth
# ---------------------------------------------------------------------------------------------------

def _belief_world():
    return _world(("p_hold", _holds("p_hold", "p_a", 1)), ("p_lack", []))


def test_a_ledger_holding_the_stage_one_claim_reads_stage_two_and_one_lacking_it_reads_stage_one(staged):
    w = _belief_world()
    assert THRONE in world_q.ambitions(w, w.persons["p_hold"]) and THRONE in world_q.ambitions(w, w.persons["p_lack"])
    assert world_q.goal_referents(w, w.persons["p_lack"], w.propositions[THRONE]) == ("p_a",)
    assert _stage_ids(w, "p_hold") == {"p_a": "s2"}
    assert _stage_ids(w, "p_lack") == {"p_a": "s1"}
    # THE WORLD SATISFIES STAGE 1 FOR THE LACKING PERSON: the same cell, asked of the world, is TRUE. This is
    # what makes his reading "stage 1" a belief and not an absence of fact.
    s1 = goals.goal(THRONE).stages.stages[0]
    ledger_v = evaluate(s1.predicate, LedgerReader(w.persons["p_lack"].ledger),
                        binding_of("p_lack", {"subject": "p_a"})).value
    world_v = evaluate(s1.predicate, world_q.WorldReader(w, "p_lack"),
                       binding_of("p_lack", {"subject": "p_a"})).value
    assert world_v is True and ledger_v is UNKNOWN, (world_v, ledger_v)


def test_a_reader_of_the_world_instead_of_the_ledger_reads_the_lacking_person_one_stage_on(staged, monkeypatch):
    """THE PLANTED FAILURE (the section's): the person-side reader swapped for the world's. The lacking person
    then reads stage 2 -- the world's answer, a fact no channel delivered him -- and (a)'s assertion reddens.
    Run by hand against the source as well (`WorldReader(w, p.id)` in `current_stage`)."""
    w = _belief_world()
    want = {"p_hold": {"p_a": "s2"}, "p_lack": {"p_a": "s1"}}
    assert {pid: _stage_ids(w, pid) for pid in want} == want, "the control: the real reader reads belief"
    monkeypatch.setattr(world_q, "LedgerReader", lambda claims: world_q.WorldReader(w, "p_lack"))
    assert _stage_ids(w, "p_lack") == {"p_a": "s2"}, "the swapped reader answers from the world"
    assert _stage_ids(w, "p_lack") != want["p_lack"], "a world read is observable: (a) would redden"


# ---------------------------------------------------------------------------------------------------
# (b) complete sequences and the per-referent reading
# ---------------------------------------------------------------------------------------------------

def test_a_complete_sequence_reads_none_and_each_stage_is_reached_in_turn(staged):
    checked = 0
    for passed, want in ((), "s1"), ((1,), "s2"), ((1, 2), "s3"):
        w = _world(("p_o", _holds("p_o", "p_a", *passed)))
        assert _stage_ids(w, "p_o") == {"p_a": want}, passed
        checked += 1
    w = _world(("p_o", _holds("p_o", "p_a", 1, 2, 3)))
    assert world_q.current_stage(w, w.persons["p_o"], THRONE) is None
    checked += 1
    assert checked == 4


def test_the_first_unmet_stage_is_read_not_the_last_met_one(staged):
    """Stage 2 unmet but stage 3 held: the person is AT stage 2 (the first not TRUE), whatever he holds beyond."""
    w = _world(("p_o", _holds("p_o", "p_a", 1, 3)))
    assert _stage_ids(w, "p_o") == {"p_a": "s2"}
    w = _world(("p_o", _holds("p_o", "p_a", 3)))
    assert _stage_ids(w, "p_o") == {"p_a": "s1"}


def test_each_referent_is_read_on_its_own_and_a_passed_referent_is_absent(staged):
    checked = 0
    ledger = _holds("p_o", "p_a", 1) + _holds("p_o", "p_b", 1, 2, 3) + _holds("p_o", "p_c", 1, 2)
    w = _world(("p_o", ledger), holders=("p_a", "p_b", "p_c", "p_d"))
    assert world_q.goal_referents(w, w.persons["p_o"], w.propositions[THRONE]) == ("p_a", "p_b", "p_c", "p_d")
    cur = world_q.current_stage(w, w.persons["p_o"], THRONE)
    assert {r: s.id for r, s in cur.items()} == {"p_a": "s2", "p_c": "s3", "p_d": "s1"}, "p_b passed all"
    assert list(cur) == ["p_a", "p_c", "p_d"], "in the referents' order"
    checked += 1
    w = _world(("p_o", _holds("p_o", "p_a", 1, 2, 3) + _holds("p_o", "p_b", 1, 2, 3)), holders=("p_a", "p_b"))
    assert world_q.current_stage(w, w.persons["p_o"], THRONE) is None, "every referent passed every stage"
    checked += 1
    assert checked == 2
    # a vacant seat names nobody: nothing to read a stage of
    w = _world(("p_o", []), holders=())
    assert world_q.goal_referents(w, w.persons["p_o"], w.propositions[THRONE]) == ()
    assert world_q.current_stage(w, w.persons["p_o"], THRONE) is None


def test_the_stage_is_read_off_the_row_the_goal_is_for_and_the_stage_carries_its_own_pursuits(staged):
    w = _world(("p_o", _holds("p_o", "p_a", 1)))
    stage = world_q.current_stage(w, w.persons["p_o"], THRONE)["p_a"]
    assert stage is goals.goal(THRONE).stages.stages[1], "the loader's own Stage, not a copy"
    assert (stage.id, stage.term, stage.pursuits) == ("s2", "medium", {"honour": 1})


# ---------------------------------------------------------------------------------------------------
# (c) UNKNOWN is not TRUE
# ---------------------------------------------------------------------------------------------------

def test_an_unknown_predicate_does_not_pass_a_stage_and_neither_does_a_false_one():
    checked = 0
    own_ledger = {"form": "own_ledger", "of": "subject"}
    for name, cell, ledger, verdict in (
            # no claim on the cell's predicate: nobody knows
            ("empty ledger", S1, [], UNKNOWN),
            # a claim about the referent, but on another predicate: still nothing on THIS cell
            ("other predicate", S1, [_claim("c_x", "p_o", "p_a", "exists:Rung")], UNKNOWN),
            # `claim.held` is answered by no claim (WITNESS deposits none): the form reads UNKNOWN for all
            ("own_ledger", own_ledger, [_claim("c_y", "p_o", "p_a", "exists:Person")], UNKNOWN),
            # a claim that reads FALSE: a known no, equally not TRUE
            ("false claim", S1, [_claim("c_z", "p_o", "p_a", "exists:Person", 0)], False)):
        doc = _doc()
        doc["goal_stages"][0]["stages"][0]["predicate"] = copy.deepcopy(cell)
        with goals.rows_replaced(goals.parse(doc)):
            w = _world(("p_o", ledger))
            raw = evaluate(goals.goal(THRONE).stages.stages[0].predicate, LedgerReader(ledger),
                           binding_of("p_o", {"subject": "p_a"})).value
            assert raw is verdict, (name, raw)
            assert _stage_ids(w, "p_o") == {"p_a": "s1"}, name
        checked += 1
    assert checked == 4


# ---------------------------------------------------------------------------------------------------
# (d) actor := the person himself
# ---------------------------------------------------------------------------------------------------

def test_a_relation_cell_is_true_only_of_the_person_himself(staged):
    checked = 0
    for claim_holder, want in (("p_o", "s3"), ("p_other", "s2")):
        ledger = _holds("p_o", "p_a", 1) + [_claim("c_rel", "p_o", "p_a", f"held_by:{claim_holder}")]
        w = _world(("p_o", ledger))
        assert _stage_ids(w, "p_o") == {"p_a": want}, claim_holder
        checked += 1
    assert checked == 2


# ---------------------------------------------------------------------------------------------------
# (e) the control: no `goal_stages` row, no stage
# ---------------------------------------------------------------------------------------------------

def test_with_no_goal_stages_row_current_stage_is_none_for_every_ambition(unstaged):
    checked = 0
    w = _world(("p_o", _holds("p_o", "p_a", 1)))
    w.propositions[RUNG] = Proposition(RUNG, "OUGHT", "terr_T9", f"{RUNG} ought", True, 0)
    w.persons["p_o"].tenures.append(Tenure("t_commit_rung", "p_o", RUNG, "commit", 0))
    ambs = world_q.ambitions(w, w.persons["p_o"])
    assert set(ambs) == {THRONE, RUNG}
    for amb in ambs:
        assert world_q.goal_referents(w, w.persons["p_o"], w.propositions[amb]), "it has a referent to read"
        assert world_q.current_stage(w, w.persons["p_o"], amb) is None
        checked += 1
    assert checked == 2


def test_every_shipped_goal_and_every_ambition_of_the_realm_reads_none():
    shipped = goals.goals()
    assert all(g.stages is None for g in shipped), "the control: the shipped goals file carries no stages"
    checked = 0
    for g in shipped:
        w = World(0)
        w.propositions[g.id] = Proposition(g.id, "OUGHT", "subj_" + g.id, f"{g.id} ought", True, 0)
        p = Person("p_o", "p_o")
        p.tenures.append(Tenure("t_c", "p_o", g.id, "commit", 0))
        w.persons["p_o"] = p
        assert g.id in world_q.ambitions(w, p)
        assert world_q.current_stage(w, p, g.id) is None, g.id
        checked += 1
    assert checked == len(shipped) >= 30, "every shipped goal row (38 at the base reading)"
    # The same reading over a built realm: every ambition of every person (136 at the base reading, 12 of
    # the authored goals among them).
    w = populated.build_realm(0)
    before = w.content_hash()
    realm_checked = authored = 0
    for p in w.persons.values():
        for amb in world_q.ambitions(w, p):
            assert world_q.current_stage(w, p, amb) is None, (p.id, amb)
            realm_checked += 1
            authored += goals.goal(amb) is not None
    assert realm_checked >= 100 and authored >= 10, (realm_checked, authored)
    assert w.content_hash() == before, "asking stores nothing"


def test_the_control_can_observe_what_it_excludes_a_row_planted_on_a_shipped_goal_reads_a_stage():
    """The shipped control above is `None` because no row exists, not because the reader cannot return a
    stage: plant the row on a shipped goal whose referent is its subject (`rung`/`person`) and the same
    world reads one. The other kinds name their referents by a hold or a ledger (read above), so they are not
    planted here; the loop asserts how many it did plant (4 shipped rows are `rung`/`person` at the base)."""
    planted = 0
    row = _doc()["goal_stages"][0]["stages"]
    stages = goals.parse({"goals": [_goal("g_x", {"faction": "Crown"}, {"kind": "rung", "rung": "terr_T9"})],
                          "goal_stages": [{"id": "gs_x", "for": ["g_x"], "stages": row}]})[0].stages
    for g in goals.goals():
        if g.object["kind"] not in ("rung", "person"):
            continue
        with goals.rows_replaced(tuple(dataclasses.replace(x, stages=stages) if x.id == g.id else x
                                       for x in goals.goals())):
            w = World(0)
            w.propositions[g.id] = Proposition(g.id, "OUGHT", "subj_" + g.id, f"{g.id} ought", True, 0)
            p = Person("p_o", "p_o")
            p.tenures.append(Tenure("t_c", "p_o", g.id, "commit", 0))
            w.persons["p_o"] = p
            cur = world_q.current_stage(w, p, g.id)
            assert cur is not None and [s.id for s in cur.values()] == ["s1"], g.id
            assert list(cur) == ["subj_" + g.id]
        planted += 1
    assert planted >= 3, planted


# ---------------------------------------------------------------------------------------------------
# (f) computed when asked, stored nowhere
# ---------------------------------------------------------------------------------------------------

def test_asking_changes_nothing_and_an_id_with_no_goal_or_no_proposition_reads_none(staged):
    w = _world(("p_o", _holds("p_o", "p_a", 1)))
    p = w.persons["p_o"]
    snap = (w.content_hash(), list(p.ledger), [t.id for t in p.tenures], dict(vars(p)).keys())
    first = world_q.current_stage(w, p, THRONE)
    assert first == world_q.current_stage(w, p, THRONE) and first is not None
    assert (w.content_hash(), list(p.ledger), [t.id for t in p.tenures], dict(vars(p)).keys()) == snap
    checked = 0
    for amb in ("o_plain", "g_never_minted", RUNG):
        # `o_plain` names no goal; `g_never_minted` no Proposition of the world; RUNG is a goal without a row
        if amb == "o_plain":
            w.propositions[amb] = Proposition(amb, "OUGHT", "subj_o", "plain", True, 0)
        assert world_q.current_stage(w, p, amb) is None, amb
        checked += 1
    w2 = _world(("p_o", []))
    del w2.propositions[THRONE]
    assert goals.goal(THRONE).stages is not None
    assert world_q.current_stage(w2, w2.persons["p_o"], THRONE) is None, "no Proposition: no ambition"
    assert checked == 3
