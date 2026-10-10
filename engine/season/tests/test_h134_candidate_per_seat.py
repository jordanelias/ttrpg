"""`H-134` (and `H-207` cause 3) -- A PERSON HOLDING TWO SEATS THAT BOTH GRANT AN ACT FORMS ONE
CANDIDATE PER SEAT, AND THE SEAT RIDES TO `Act.via`.

THE FALSIFIER (the plan's, §0.1 pt 3). `decision/options.py::exercised_seat` used to take the FIRST
live `hold` granting the act, so a holder of `off_mayor` (a Mayor at `S`, below the Duke) THEN
`off_crown` (a King at `R`, the rung directly above the Duke) revoked through `off_mayor` always --
and `state/gate.py::seated_on_the_rung_above` admits only the second. This file plants exactly that
holder and asserts the Candidate through the second seat is formed, is packed with
`Act.via == "off_crown"`, and is admitted by the same predicate (`may_revoke`) the fold's `_req_revoke`
and the write gate ask. The MUTATION is the first-hold-only walk restored in
`options.py::_granting_holds` -- the test goes red on it (recorded in the commit's receipt).

THE CONTROL. A holder of ONE seat forms Candidates carrying no seat key, mints the ids
`pack_scenes` minted before, and `Act.via` is `exercised_seat`'s -- pinned against a digest taken
from the PRE-CHANGE function at f9ce11b0 (`_CONTROL`), and counted (`checked >= N`, §0.1 pt 2) so a
loop that asserted nothing cannot pass.

NOT HERE, AND SAID: a computed `revoke` still carries no `office` operand (`H-207` causes 1/2/4), so
the fold's `_req_revoke` refuses it before the seat is asked; this file asks the seat test by
adding the `office` a computed act lacks, and does not claim the computed `revoke` executes.
"""
import hashlib

import pytest

from ..data.verbs import VERB_TABLE, opportunity_key
from ..decision.choose import pack_scenes
from ..decision.options import exercisable_seats, exercised_seat, opening_set
from ..gaps import Unspecified
from ..harness import probes as P
from ..loop import predicates as _preds
from ..state.acts import ActStore
from ..state.carriers import Act, Office, Person, Question, Tenure, View
from ..state.gate import may_revoke
from ..state.ids import H

_RUNG_ABOVE = "rung_above_same_faction"
_GRANTS = ["issue", "confer", "revoke"]          # fixture choice: a Mayor/King both granting these
TWO, ONE = "p_two", "p_one"
TARGET = "off_duke"


def _seat(w, pid, oid, post, rung):
    """An office built BEFORE its holder is seated, so the grant is stamped at seating
    (`World._grant_remit`)."""
    w.offices[oid] = Office(oid, post, rung, list(_GRANTS), faction="Crown",
                            conferral="appointed", revocation=_RUNG_ABOVE)
    w.add_tenure(Tenure(f"t_{oid}_{pid}", pid, oid, "hold", 0))


def _world():
    """`tiny_world` (R ⊃ D ⊃ S ⊃ Hh; `p_high` holds `off_duke`, a Crown Duke at `D`), plus
      * `p_two`, seated FIRST on `off_mayor` (a Mayor at `S` -- below the duchy, so NOT the rung above
        the Duke) and SECOND on `off_crown` (a King at `R` -- the rung directly above it);
      * `p_one`, seated on `off_mayor2` alone (the control: one seat, the same grants).
    Both seats grant issue/confer/revoke; the Duke's seat declares the rung-above revocation basis."""
    w = P.tiny_world()
    w.offices[TARGET].revocation = _RUNG_ABOVE
    for pid in (TWO, ONE):
        w.persons[pid] = Person(pid, pid)
    _seat(w, TWO, "off_mayor", "Mayor", "S")
    _seat(w, TWO, "off_crown", "King", "R")
    _seat(w, ONE, "off_mayor2", "Mayor", "S")
    return w


def _candidates(w, pid):
    q = Question("q_h134", "need", (TARGET, "Hh"), "Hh")
    p = w.persons[pid]
    return opening_set(p, View(p.id, [], 99, q), q, w.fixtures)


def _acts(w, pid, cands):
    mint = lambda who, verb, subj: H(w.world_seed, w.tick, who, f"act:{verb}:{subj}")
    scenes = pack_scenes(w.persons[pid], cands, 99, w.fixtures, mint)
    return [a for s in scenes for a in s.acts]


def _with_office(a):
    """The act a computed `revoke` would be if it carried the `office` it lacks (`H-207`)."""
    return Act(id=a.id, actor=a.actor, verb=a.verb, via=a.via,
               payload={**(a.payload or {}), "office": a.payload["subject"]})


def test_h134_the_second_seat_forms_a_candidate_is_packed_via_it_and_the_fold_admits_it():
    w = _world()
    p, duke = w.persons[TWO], w.offices[TARGET]
    row = VERB_TABLE["revoke"]
    # The fixture says what it must: BOTH grant revoke, in this tenure order, and only the second
    # is the rung above the Duke -- so the first-hold walk could not have found the lawful seat.
    assert exercisable_seats(p, row) == ("off_mayor", "off_crown")
    assert exercised_seat(p, row) == "off_mayor"
    assert not may_revoke(w, TWO, "off_mayor", duke)
    assert may_revoke(w, TWO, "off_crown", duke)

    revokes = [c for c in _candidates(w, TWO) if c.verb == "revoke" and c.subject == TARGET]
    assert sorted(c.operands["via"] for c in revokes) == ["off_crown", "off_mayor"], revokes

    acts = [a for a in _acts(w, TWO, revokes)]
    assert sorted(a.via for a in acts) == ["off_crown", "off_mayor"]
    assert len({a.id for a in acts}) == 2, "two seats, one act id"
    admitted = [a.via for a in acts if _preds._req_revoke(w, _with_office(a))]
    assert admitted == ["off_crown"], admitted          # the SECOND seat, and only it
    by_seat = {a.via: a for a in acts}
    assert may_revoke(w, TWO, by_seat["off_crown"].via, duke)
    assert not may_revoke(w, TWO, by_seat["off_mayor"].via, duke)


def test_h134_a_transfer_gives_from_the_rung_of_the_seat_it_was_formed_for():
    """`from` is `treasury_of(seat)`, so the operand and `Act.via` agree for each Candidate (the
    reader that was `exercised_seat(p, row)` inside `_operands`)."""
    w = _world()
    ts = [c for c in _candidates(w, TWO) if c.verb == "transfer" and c.subject == "Hh"]
    assert {(c.operands["via"], c.operands["from"]) for c in ts} == {
        ("off_mayor", "S"), ("off_crown", "R")}, [c.operands for c in ts]
    acts = _acts(w, TWO, ts)
    assert {(a.via, a.payload["from"]) for a in acts} == {("off_mayor", "S"), ("off_crown", "R")}


def test_h134_two_seats_are_two_acts_ids_opportunities_and_the_store():
    w = _world()
    revokes = [c for c in _candidates(w, TWO) if c.verb == "revoke" and c.subject == TARGET]
    a1, a2 = _acts(w, TWO, revokes)
    assert a1.id != a2.id
    k1 = opportunity_key(a1.verb, TARGET, a1.payload)
    k2 = opportunity_key(a2.verb, TARGET, a2.payload)
    assert k1 != k2 and len(k1) == 4 and len(k2) == 4, (k1, k2)
    store = ActStore()
    store.append(a1)
    store.append(a2)                                    # no duplicate-id refusal
    # The necessity, observed: the same two acts under a seat-less id collide in the store.
    mint = lambda who, verb, subj: H(w.world_seed, w.tick, who, f"act:{verb}:{subj}")
    same = mint(TWO, "revoke", TARGET)
    s2 = ActStore()
    s2.append(Act(id=same, actor=TWO, verb="revoke", via="off_mayor", payload=a1.payload))
    with pytest.raises(Unspecified):
        s2.append(Act(id=same, actor=TWO, verb="revoke", via="off_crown", payload=a2.payload))


# --------------------------------------------------------------------------------------
# THE CONTROL: ONE SEAT IS BYTE-IDENTICAL TO THE FUNCTION BEFORE THE CHANGE
# --------------------------------------------------------------------------------------

# `(n candidates, n acts, sha256 of the repr of (candidates, acts))` for `p_one` -- captured by
# running `_control_reading` on the tree at f9ce11b0, BEFORE this change.
_CONTROL = (70, 70, "d9bebd8cdece6a438939510e295bb1bdb8062fd72bbac75821f76de7ec8d5484")


def _control_reading():
    w = _world()
    cands = _candidates(w, ONE)
    acts = _acts(w, ONE, cands)
    rep = (
        [(c.verb, c.subject, sorted((k, repr(v)) for k, v in c.operands.items())) for c in cands],
        [(a.id, a.via, sorted((k, repr(v)) for k, v in (a.payload or {}).items())) for a in acts],
    )
    return len(cands), len(acts), hashlib.sha256(repr(rep).encode()).hexdigest()


def test_h134_control_one_seat_forms_the_same_candidates_and_ids_as_before():
    w = _world()
    p = w.persons[ONE]
    for verb in ("revoke", "confer", "transfer"):
        assert exercisable_seats(p, VERB_TABLE[verb]) == ("off_mayor2",), verb
    cands = _candidates(w, ONE)
    carried = [c for c in cands if "via" in c.operands]
    assert carried == [], "a one-seat Candidate carries a seat key"
    acts = _acts(w, ONE, cands)
    mint = lambda who, verb, subj: H(w.world_seed, w.tick, who, f"act:{verb}:{subj}")
    checked = 0
    for a in acts:
        assert a.via == exercised_seat(p, VERB_TABLE[a.verb])
        assert a.id == mint(ONE, a.verb, a.payload["subject"]), a.verb
        assert "via" not in a.payload
        assert opportunity_key(a.verb, a.payload["subject"], a.payload) in {
            (a.verb, a.payload["subject"])}
        checked += 1
    assert checked >= 20 and any(a.via == "off_mayor2" for a in acts), checked
    assert _control_reading() == _CONTROL
