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
