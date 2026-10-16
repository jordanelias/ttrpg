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
from ..decision import options as _options
from ..decision.options import exercisable_seats, exercised_seat, opening_set
from ..loop.deliberate import _qualify_by_round
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

    acts = _acts(w, TWO, revokes)
    assert sorted(a.via for a in acts) == ["off_crown", "off_mayor"]
    assert len({a.id for a in acts}) == 2, "two seats, one act id"
    # The payload copy is a discriminator, never a second answer: it must equal `Act.via`.
    assert [a.payload["via"] for a in acts] == [a.via for a in acts]
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
    # The opportunity is the verb on the subject for the actor, whichever seat did it: the seat is in
    # the id and not in this key, so its shape cannot depend on how many seats the person holds.
    assert k1 == k2 == ("revoke", TARGET), (k1, k2)
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
# running `_control_reading` on the tree at f9ce11b0, BEFORE this change. RE-RECORDED AT IN-53
# (DECISION 2026-10-13 D1; was `(70, 70, "d9bebd8c...")`): exactly two Candidates leave, diffed
# against e716f10b -- `confer` on `Hh` and on `off_duke`, because `confer` now forms only on a
# referent the question carries as `Office` and this question carries none; no Candidate is added.
# RE-PINNED AT v9 IN-09: 68 -> 66. `comply` is typed and `referent_named`, so it no longer forms on
# a referent the person's own ledger does not name; it was formed on arbitrary referents before and
# then filtered out by `resolvable_verbs()`, so no behaviour moves (`aperture 4 0` other rows equal).
# RE-PINNED AT v9 IN-10 (#453 §10.1): 66 -> 64, exactly the two `issue` Candidates leave and no
# Candidate is added (per-verb count diffed: every other verb still 2). `issue` joined the
# known-person fan for `to` (its `terms` conjunct binds `subject`), and `p_one` knows nobody and
# holds nothing to say about the referent, so no writ forms -- where before both writs were
# addressed to what they were about.
# RE-PINNED AT v9 IN-45 `carry` (B-K), DIGEST ONLY: 64 -> 64, `c3cc3ff1...` -> `4351ecd2...`. The pin
# passed at fae9e623 (IN-10) and went red at c435a5ec. Attributed per verb by diffing the dumped
# Candidate and act lists at each commit:
#   * `forge` (c435a5ec, IN-45 `forge`) -- the WHOLE move. No Candidate or act id added or removed:
#     its two Candidates (`off_duke`, `Hh`), formed untyped with no operands before, now carry
#     `subject` (the row is typed with `survey`'s cell). The 64 act ids and payloads are unchanged.
#     CONTROL: HEAD's lists with `forge`'s `subject` operand stripped re-hash to `c3cc3ff1...`.
#   * `survey` + Rung (aa26c4fd) -- nothing: lists byte-identical to c435a5ec's.
#   * `carry` (IN-45, on aa26c4fd) -- nothing: its two Candidates were already formed with
#     `{subject, to}` at fae9e623 (formation reads the verb table, not `resolvable_verbs()`); the
#     lists are byte-identical to aa26c4fd's.
# RE-PINNED AT v9 IN-45 `migrate` (B-K, on 4cee0de5): 64 -> 62, `4351ecd2...` -> `b8163ec4...`.
# Exactly the two `migrate` Candidates leave (on `off_duke` and `Hh`, the question's plain
# referents) and none is added: `migrate` declares `referent_class: Rung` and forms only on a place
# `places_named` stamps, and `p_one`'s ledger names none. CONTROL: the same reading with `migrate`'s
# `referent_class` blanked in `VERB_TABLE` re-hashes to `(64, 64, "4351ecd2...")` exactly.
# RE-PINNED AT v9 IN-49 `levy` (B-K, on ccf16bc3): 62 -> 60, `b8163ec4...` -> `5abeea9b...`.
# Exactly the two `levy` Candidates leave (on `off_duke` and `Hh`, the question's plain referents)
# and none is added: `levy` declares `referent_class: Rung` and forms only on a `Rung`-classed
# referent, and this reading's question carries none. CONTROL: the same reading with `levy`'s
# `referent_class` blanked in `VERB_TABLE` and `world_q.larders_in_purview` stamping nothing
# re-hashes to `(62, 62, "b8163ec4...")` exactly.
# RE-PINNED AT v9 SC-01 step 12 (`speak`, B-N), DIGEST ONLY: 60 -> 60, `5abeea9b...` -> `4b486ad7...`.
# The pin passed at ffd753f6 and went red at 947747e0 (step 12). The dumped Candidate and act lists
# at ffd753f6 and at 801f733e differ in `speak` alone: its two Candidates (`Hh`, `off_duke`), formed
# with no operands before, now carry `{subject, to}` (the row is a typed cell over a `DocketItem`
# subject), and their two acts' payloads gain `to`. No Candidate or act id is added or removed.
# CONTROL: every other line of the two dumps is identical, and ffd753f6's reading re-hashes to
# `5abeea9b...` exactly.
_CONTROL = (60, 60, "4b486ad73f3c039d4761e22dfae85eaaa5db51011aaa6c2205016c9de60f0cc6")


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
        assert opportunity_key(a.verb, a.payload["subject"], a.payload) == (
            a.verb, a.payload["subject"])
        checked += 1
    assert checked >= 20 and any(a.via == "off_mayor2" for a in acts), checked
    assert _control_reading() == _CONTROL


def test_h134_the_belief_test_is_asked_of_the_seat_each_candidate_is_formed_for(monkeypatch):
    """`opening_set` hands `belief_contradicts` the seat the Candidate is formed for, the same one
    that rides to `Act.via`. The fixture's ledger is empty, so the real test cannot contradict
    whichever seat it receives; a recorder (returning False, so every Candidate forms) observes the
    seat instead. A first-seat slip at that call reddens this and nothing else in the file."""
    rec = []

    def fake(p, row, subject, ops, seat, weigh=None):
        rec.append((row.verb, seat))
        return False

    monkeypatch.setattr(_options, "belief_contradicts", fake)
    w = _world()
    cands = _candidates(w, TWO)
    checked = 0
    for verb in {c.verb for c in cands if "via" in c.operands}:
        asked = [s for v, s in rec if v == verb]
        formed = [c.operands["via"] for c in cands if c.verb == verb and "via" in c.operands]
        assert asked == formed, (verb, asked, formed)
        assert set(asked) == {"off_mayor", "off_crown"}, (verb, asked)
        checked += 1
    assert checked >= 3, checked


def test_h134_two_seats_stay_two_act_ids_after_the_round_requalifies_them():
    """`_qualify_by_round` re-mints every id from the PAYLOAD on a re-deliberation (round >= 1), where
    no Candidate is in sight; the seat in the payload is what keeps the two seats' ids apart there."""
    w = _world()
    revokes = [c for c in _candidates(w, TWO) if c.verb == "revoke" and c.subject == TARGET]
    mint = lambda who, verb, subj: H(w.world_seed, w.tick, who, f"act:{verb}:{subj}")
    scenes = pack_scenes(w.persons[TWO], revokes, 99, w.fixtures, mint)
    before = {a.id for s in scenes for a in s.acts}
    assert len(before) == 2
    _qualify_by_round(scenes, w, 1)
    after = {a.id for s in scenes for a in s.acts}
    assert len(after) == 2 and not (after & before), (before, after)
