"""B34.01 step 2 (GO-B §3, branch 1, "test first") -- THE DOER HOLDS HIS OWN ACT'S OUTCOME.

`p_npc_001` at `build_realm(0)` does one `research` act on a Record in his own place; the act ends `finding.none` (a Failure, which
`rosters.yaml: undeposited_kinds` keeps from making an EVENT-KIND claim: the hardest case, since only the actor's own observation reads
reach his ledger). After the WITNESS barrier his ledger must hold a claim with `doer == p_npc_001` that WITNESS deposited on that act's Event
(a `claim.deposited` caused by it). If this passes on the tree nothing is added: `account` (B34.03) already reads it. If it fails, branch 2
(the self-deposit rule at `loop/witness.py::witness`) is a declared hash mover and is the orchestrator's decision, not this file's.

The act ids are swept (60 at most) until one draws `Failure`: the draw is keyed on the act id and the world seed, so the id is the sample.
"""
from __future__ import annotations

from ..boot.realm import build_realm
from ..harness.scenarios import step
from ..loop.driver import SeasonDriver
from ..queries.world_q import place_of
from ..state.carriers import Act, Record

DOER = "p_npc_001"
REC = "rec_own_outcome"
# [JUSTIFIED: a test-fixture search bound, not a game value -- the act ids tried for a `Failure` draw; asserted reached]
SWEEP = 60


def test_the_doer_holds_his_own_acts_outcome():
    for n in range(SWEEP):
        w = build_realm(0)
        w.records[REC] = Record(REC, place_of(w, DOER), "text")
        d = SeasonDriver(w)
        (e,) = step(w, d, Act(id=f"a_own_outcome_{n}", actor=DOER, verb="research", payload={"subject": REC}))
        if e.kind == "finding.none":
            break
    else:
        raise AssertionError(f"{SWEEP} act ids drew no `finding.none`: the test observed no failed research")
    assert e.degree == "Failure", (e.kind, e.degree)
    deposited = {c.subject for x in w.log if x.kind == "claim.deposited" and e.id in x.causes for c in x.changes}
    assert deposited, "WITNESS deposited nothing for the act's Event: the doer's ledger cannot hold its outcome"
    mine = [c for c in w.persons[DOER].ledger if c.id in deposited and c.doer == DOER]
    assert mine, ("the doer holds no claim of his own on the act's Event; the deposits it made went to "
                  f"{sorted({x.holder for p in w.persons.values() for x in p.ledger if x.id in deposited})}")


OTHER = "p_npc_005"     # at another place than DOER (asserted below), so his act is not one DOER stood at


def test_every_resolved_act_has_an_own_account_row():
    """GATE 3 (B34.03): every act the seated person resolved has an `own=True` `AccountRow` -- a claim `account` reads from his own ledger with
    `doer == him` that WITNESS deposited on the act's Event -- and a planted act of another person yields none for him. Two acts of his (a record
    each) and one of `OTHER`'s are resolved in one world; the control is `OTHER`'s own account, which does hold the own row of the act planted
    (so the plant resolved)."""
    from ..decision.sheet import account
    w = build_realm(0)
    assert place_of(w, DOER) != place_of(w, OTHER)
    d = SeasonDriver(w)
    mine, theirs = [], []
    for rid, who, into in ((REC, DOER, mine), (REC + "_2", DOER, mine), (REC + "_other", OTHER, theirs)):
        w.records[rid] = Record(rid, place_of(w, who), "text")
        (e,) = step(w, d, Act(id=f"a_acct_{rid}", actor=who, verb="research", payload={"subject": rid}))
        into.append({c.subject for x in w.log if x.kind == "claim.deposited" and e.id in x.causes for c in x.changes})

    def held(pid, ids):
        return [r for r in account(w.persons[pid], (0, 0)) if r.own and r.claim.id in ids]
    assert all(ids and held(DOER, ids) for ids in mine), "an act he resolved has no own=True row"
    assert theirs[0] and held(OTHER, theirs[0]), "control: the planted act of OTHER has no own row for its doer"
    assert not held(DOER, theirs[0]), "another person's act gave him an own=True row"
    # his ledger holds claims that are not the echo of his deed (the build's, landed at tick -2), so a reader that marked every row `own` reads red here
    assert {r.claim.id for r in account(w.persons[DOER], (-2, 0)) if r.own} == {c.id for c in w.persons[DOER].ledger if c.doer == DOER}
    assert any(c.doer != DOER for c in w.persons[DOER].ledger), "his ledger holds nothing that is not his own deed: the equality above observed nothing"
