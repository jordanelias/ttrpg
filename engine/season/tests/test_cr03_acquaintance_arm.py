"""CR-03 (B10-09 close two) -- ACQUAINTANCE: HALF THE PERSONS KNOW NO ONE FOR FOUR SEASONS. A MEASUREMENT
and ONE HAND-BUILT ARM. NOTHING IN THE SHIPPED TREE CHANGES: no acquaintance route is enabled in the
shipped realm, `build_realm` is untouched, and so is every world hash. The arm's builder step lives in THIS
file and runs on a world this file builds.

HOW THE KNOWN SET FORMS (`queries/person_q.py::known_persons`: a truthy `exists:Person` reading, a `seen`
claim's `who`, a told claim's `chain[-1]`; nothing else). READ AT THE BASE COMMIT with the reference reader
(`proposals/2026-10-24-master-workplan-v10/ctl/acquaintance_probe.py`, `PYTHONHASHSEED=0`, four seasons,
the shipped realm, arm `off`; each run's exit and its five rows were read back from its log):

    persons who know nobody / persons alive       build    s1      s2      s3      s4
        seed 0                                    83/83    38/76   30/76   29/75   30/74
        seed 1                                    83/83    37/81   30/78   29/77   32/75
        seed 2                                    83/83    35/81   26/76   29/75   28/73

    median / max persons known at s4: 1 / 7 on every seed. Told claims (source three) in all ledgers at
    s4: 0, 0, 4.

HOW MANY PERSONS GET EACH SOURCE (a one-off reader over the same drive, seeds 0 / 1 / 2, persons with at
least one OTHER person named by the source, at s1 / s2 / s3 / s4): an `exists:Person` reading
28/30/25/21, 35/32/30/27, 36/37/29/25; a `seen` claim 27/36/36/33, 33/37/37/32, 34/38/37/35; a told
claim 0/1/0/0, 0/0/0/0, 4/5/0/4. At build all three are 0.

The plan recorded 83 of 83 at build (REPRODUCED on all three seeds) and 40 of 80 after four seasons at seed
0; the base reads 30 of 74. A different figure is recorded, not forced: the plan's figure was taken on an
earlier tree. Either way, 38 to 43 per cent of the living persons (28 to 32 of 73 to 75) still know no one
after four seasons, and at build every one of them does not: the realm starts with no acquaintance, and what
the four seasons add is `seen` claims and `exists` readings, each for about half the persons; the third
source, a told claim, is rare.

THE ARM AT REALM SCALE (a one-off reader, not a test: the shipped realm built at seeds 0-2, the step below
applied to it after the build, the 46 `concerns` rows of `npcs.yaml`): 83 of 83 know no one in the control,
37 of 83 in the arm (the 46 persons with a row know exactly one person; the 37 with none stay blocked).
`tell` forms for 0 persons in the control and 46 in the arm, the same on all three seeds. `argue` forms for
0 in both. The shipped drive, route off, forms `tell` for 38 to 50 persons at the season ends.

WHAT THE BLOCK COSTS. `tell` forms one Candidate per person the teller knows (`to`), `argue` and `give`,
`covenant` and `issue` the same (`VerbRow.known_person_operands`); a person who knows nobody forms none of
them, whatever else he holds. `argue` is blocked twice over in the realm: no question there names a
Proposition (`verb_table.yaml`'s `argue` `referent_class_note`: formed for 0/0/0 persons), so the route
below cannot make it form in PLAY and the arm hands the classed question over by hand, the way the
existing hand-built tests do.

THE ARM: ONE LAWFUL ROUTE, THE HOME'S FIRST. `npcs.yaml`'s `concerns` rows, which
`harness/populated.py` already writes as an OUGHT Proposition about the person concerned and a `commit`
Tenure from the person concerned-about-him. The new builder step (`seed_acquaintance_from_concerns`
below) reads the same rows (`case`, `concerns`) and writes the committer's OWN `exists:Person` reading of
the person concerned about -- the first of `known_persons`' three sources, so no roster of acquaintances
is kept (AX-2), no world read is made, and `tie` (how a person was CHOSEN, `npcs.yaml:25`) is not a source.
It reads the ROWS and not the `commit` Tenures: the same kind carries a faction's creed and an
organization's goal, which are membership and not a concern.

WHAT THE ARM SHOWS (this file's tests):
  * CONTROL (route off, the shipped build's shape): nobody knows anybody; `tell` and `argue` form for
    nobody, on every question the person is delivered and on a Proposition question handed to him.
  * ARM (route on): the four persons with a concern row each know exactly one person; `tell` forms for
    each, addressed to that person, and `argue` forms for each on his own OUGHT, addressed to that person.
    The fifth person, with no row, stays blocked in the arm too -- the route is only as wide as the rows.
  * THAT THE ARM RAN is read off the ARTIFACT, not an exit code: the arm's ledgers differ from the
    control's by exactly four `exists:Person` claims, one per committer, and by nothing else.

THE ASK FOR THE CLOSE NOTE (not a ledger row): should the realm START with acquaintances? That is a dense
social graph against a sparse one, and it changes what the game is. Wiring this route into `build_realm`
is a declared hash mover and is NOT done here.

[ASSUMPTION; medium; Jordan to correct; revert: use `seen` claims for co-located persons at CENSUS as the
first arm -- delete this file's builder step and write that one instead.] A concern row is an ACQUAINTANCE:
the committer knows OF the person he is concerned about, which is the weakest reading of a concern and the
one `exists:Person` carries (existence, not relation or opinion).
"""

from __future__ import annotations

from ..decision import assemble
from ..decision.options import opening_set
from ..harness import probes as P
from ..queries import world_q
from ..queries.person_q import KNOWN_PERSON_CLAIM, known_persons
from ..state.carriers import Claim, Proposition, Question, Tenure

RING = ("p_low", "p_mid", "p_high", "p_king")     # each carries a concern row about the next
STRANGER = "p_other"                              # carries none, as a person with no tie writes nothing
FAN = ("tell", "argue")


def seed_acquaintance_from_concerns(w, rows) -> list:
    """THE ARM'S ONE BUILDER STEP. `rows` is the authored concern rows as `(committer, concerned)` person
    ids -- `npcs.yaml`'s `case` and `concerns` cells through the same `p_<slug>` ids `populated.py` seats
    them under. Each committer's own ledger takes a truthy `exists:Person` reading of the person he is
    concerned about (`known_persons`' first source), when both are persons the world holds and they differ.
    Returns the claim ids written. It reads the rows and the persons and writes nothing but those claims.
    NOT the `commit` Tenures: the same Tenure kind also carries a faction's creed and an organization's goal
    (`populated.py`), which are membership and not a concern."""
    written = []
    for who, concerned in rows:
        if who in w.persons and concerned in w.persons and who != concerned:
            cid = f"c_acq_{who}_{concerned}"
            w.persons[who].ledger.append(Claim(
                cid, who, concerned, KNOWN_PERSON_CLAIM["predicate"], 1, 0, "firsthand", 100, "own"))
            written.append(cid)
    return written


def _world(route: bool):
    """A hand-built world: `tiny_world`'s five persons; the ring each carries `populated.py`'s concern write
    (an OUGHT Proposition about the next person, a `commit` Tenure to it); everyone holds one claim on the
    hearth `Hh` (so `tell` has something to say). `route` runs the builder step above on those rows."""
    w = P.tiny_world()
    for i, pid in enumerate(RING):
        about, prop = RING[(i + 1) % len(RING)], f"prop_{pid}"
        w.propositions[prop] = Proposition(prop, "OUGHT", about, "want", True, 0)
        w.add_tenure(Tenure(f"t_{prop}_commit", pid, prop, "commit", 0))
    for pid, p in w.persons.items():
        p.ledger.append(Claim(f"c_h_{pid}", pid, "Hh", "stores:grain", 8, 0, "firsthand", 37, "own"))
    rows = tuple((pid, RING[(i + 1) % len(RING)]) for i, pid in enumerate(RING))
    written = seed_acquaintance_from_concerns(w, rows) if route else []
    return w, written


def _formed(w, pid, verb) -> list:
    """The `verb` Candidates `pid` forms, as `(subject, to)`: across every question `questions_for` delivers
    him (what play offers), and for `argue` also on a question naming his own OUGHT Proposition, classed as
    `questions_for` would stamp it (no question in the realm names one; see the docstring)."""
    p = w.persons[pid]
    qs = list(world_q.questions_for(w, p))
    prop = f"prop_{pid}"
    if prop in w.propositions:
        qs.append(Question(f"q:argue:{prop}", "need", (prop,), classes=((prop, w.class_of(prop)),)))
    out = []
    for q in qs:
        out += [(c.subject, c.operands.get("to")) for c in opening_set(p, assemble(p, q, 12), q, w.fixtures)
                if c.verb == verb]
    return out


def test_control_nobody_knows_anybody_and_tell_and_argue_form_for_nobody():
    """THE CONTROL, route off. Non-vacuous on three sides: every person holds a claim to tell (so the
    block is the empty known set and not an empty ledger), the ring's OUGHTs exist (so a Proposition
    question is real), and the arm below forms on the very same worlds once the one step runs."""
    w, written = _world(False)
    assert written == []
    assert all(w.persons[pid].ledger for pid in w.persons)
    assert all(known_persons(w.persons[pid].ledger, pid) == () for pid in w.persons)
    checked = 0
    for pid in w.persons:
        for verb in FAN:
            assert _formed(w, pid, verb) == [], (pid, verb)
            checked += 1
    assert checked == len(w.persons) * len(FAN)


def test_arm_the_concern_route_unblocks_tell_and_argue_for_the_persons_it_reaches():
    """THE ARM, route on. FALSIFIER: against the control above, `tell` and `argue` form for the four
    persons the rows reach and not for the fifth. Delete the builder step's `append` and the first
    assert (`written`) and every formation assert below it go red, which is the control's reading."""
    w, written = _world(True)
    assert sorted(written) == sorted(
        f"c_acq_{pid}_{RING[(i + 1) % len(RING)]}" for i, pid in enumerate(RING))
    reached = 0
    for i, pid in enumerate(RING):
        concern = RING[(i + 1) % len(RING)]
        assert known_persons(w.persons[pid].ledger, pid) == (concern,)
        told = _formed(w, pid, "tell")
        assert told and {to for _, to in told} == {concern}, (pid, told)
        argued = _formed(w, pid, "argue")
        assert argued == [(f"prop_{pid}", concern)], (pid, argued)
        reached += 1
    assert reached == len(RING)
    assert known_persons(w.persons[STRANGER].ledger, STRANGER) == ()
    assert _formed(w, STRANGER, "tell") == [] and _formed(w, STRANGER, "argue") == []


def test_the_arm_ran_the_artifact_differs_by_exactly_the_route_claims():
    """HOW THE ARM IS KNOWN TO HAVE RUN: a diff of the two worlds' ledgers, not a return code. They differ
    by exactly the four `exists:Person` claims the step reports, one per committer, each about the person
    its OUGHT is about, and by nothing else; and a world rebuilt with the step skipped is the control."""
    ctl, _ = _world(False)
    arm, written = _world(True)
    added = {}
    for pid in ctl.persons:
        before = {c.id for c in ctl.persons[pid].ledger}
        extra = [c for c in arm.persons[pid].ledger if c.id not in before]
        assert {c.id for c in ctl.persons[pid].ledger} <= {c.id for c in arm.persons[pid].ledger}
        added[pid] = extra
    new = [c for cs in added.values() for c in cs]
    assert sorted(c.id for c in new) == sorted(written) and len(new) == len(RING)
    assert all(c.predicate == KNOWN_PERSON_CLAIM["predicate"] and c.value for c in new)
    for i, pid in enumerate(RING):
        assert [c.subject for c in added[pid]] == [RING[(i + 1) % len(RING)]]
    assert added[STRANGER] == []
    again, _ = _world(False)
    assert all(known_persons(again.persons[pid].ledger, pid) == () for pid in again.persons)
