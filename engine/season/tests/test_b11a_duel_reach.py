"""B11 lane A -- COMPUTED PLAY REACHES THE DUEL: the chain `challenge` -> `accept` -> a fought scene, every link
formed by the person and resolved by the fold, nothing hand-built but the world.

The links, each at its owner (the commit body carries the measurements):
  (1) formation: `challenge` forms only on a `Disputant` (`world_q.disputes_held`: a man beside him whom he holds a
      dispute with, `person_q.holds_dispute`), and carries `individual` on both parties; `capture` declares `Person`;
      a `Record` row whose cell asks a sub-kind forms only on a document his own reading says is of it
      (`options.documents_known_as`).
  (2) the challenged hears it: a witnessing addressee reads the document put to him (`witness.addressee_reads`), and
      `world_q.challenges_heard` stamps the challenge on his question (`14_VERBS_PHYSICAL_A` A4).
  (3) `accept`'s `to` is the challenge's own `challenger` (`operand_bags`' document branch).
  (4) the chooser reads `challenge` as done against its subject (`rosters.yaml: opposed_without_prize`).
  (5) `fight` no longer forms on the duel context: a duel is `accept`'s.
FALSIFIER (below): a planted grievance on a hand-built world forms the challenge, the fold issues it, the challenged
forms `accept` against the challenger and the fold fights it -- a drawn scene whose band is one of the duel's typed
outcomes; with `revert_b11a` no `challenge` forms. The realm reading (challenges issued, accepts declared, duels
yielded, seeds 0-2) is the commit body's, not an assertion here.
"""
from __future__ import annotations

from dataclasses import replace

import pytest

from ..data import verbs as V
from ..data.requires import AllOf, TypedRequires
from ..data.verbs import VERB_TABLE
from ..decision import assemble
from ..decision import options as O
from ..data.matrix import WriteClass
from ..harness import probes as P
from ..harness.populated import build_realm, run
from ..loop import witness as WIT
from ..loop.driver import mint_token
from ..queries import world_q
from ..state.carriers import Claim
from .test_in10_record_operands import _acts, _resolve
from .test_in12_step9 import _world
from .test_pc10b_challenge_record import _run

A, B = "p_mid", "p_low"            # `tiny_world`: both stand at the hearth (`with` each other)
FAR = "p_high"                     # elsewhere

#: `build_realm(s)` then one season (`run(1, s, w=w)`), on this commit's tree; PRE is the parent tree's -- rebased (C3-A2):
#: the base of B01 (`8727d1d`), read there under PYTHONHASHSEED=0 (was `1424aa7`'s d4c83c8c... / d9f3be70... / 285fb92a...).
#: POST re-pinned in B01.02 to the rebased reach's own reading (B01.01's tree, PYTHONHASHSEED=0; was the branch's 2b1679bb... /
#: e6976ba8... / e92efc2a..., `1424aa7`'s world, discarded per C3-A2).
POST = {0: "b4619054a2e47cb87ae4a99da6c98f03", 1: "8b24ff0864bce9f4541f7864ad4de21d", 2: "37baa06098d392eaca4066e4df18aa40"}
PRE = {0: "5ab73af282d0779646c38839fbab85d8", 1: "aa58ef0b71c947ce5ff9f0a75ffd8ca6", 2: "a21ab6e12e356ccc4261bec1c93ca3b4"}


def revert_b11a(monkeypatch) -> None:
    """EVERY LINK OF B11 LANE A'S REACH AT ITS REVERT, for the life of one test. A test pinning a pre-lane hash calls
    it (with the earlier items' own reverts)."""
    row = VERB_TABLE["challenge"]
    req = row.requires_typed
    kept = tuple(c for c in req.requirement.clauses if getattr(c, "relation", None) != "individual")
    assert len(kept) == len(req.requirement.clauses) - 2
    monkeypatch.setitem(VERB_TABLE, "challenge", replace(row, referent_class="",
                                                         requires_typed=TypedRequires(AllOf(kept), req.names)))
    monkeypatch.setitem(VERB_TABLE, "capture", replace(VERB_TABLE["capture"], referent_class=""))
    monkeypatch.setattr(world_q, "disputes_held", lambda w, p: ())
    monkeypatch.setattr(world_q, "challenges_heard", lambda w, p, named=None: ())
    monkeypatch.setattr(O, "RECORD_SUBKINDS_BY_VERB", {})
    monkeypatch.setattr(O, "document_read", lambda p, rid: None)
    monkeypatch.setattr(O, "OPPOSED_WITHOUT_PRIZE", frozenset())
    if "fight" in O.VIOLENCE_CONTEXTS:       # an earlier item's revert (CR-87's) may have emptied the block: keep it so
        monkeypatch.setattr(O, "VIOLENCE_CONTEXTS", {**O.VIOLENCE_CONTEXTS,
                                                     "fight": ("war", "crime", "duel", "defence")})
    monkeypatch.setattr(WIT, "addressee_reads", lambda rec, pid: False)
    monkeypatch.setattr(O, "OWN_HOLD_DECLINES", O.OWN_HOLD_DECLINES - {"carry", "found", "build"})
    monkeypatch.setattr(O, "RECORD_SUBKINDS_HELD", frozenset())


def _grievance(w, holder=A, about=B):
    """`holder` saw `about` declare a fight, and his own pursuits judge it against him (`test_cr87`'s dispute)."""
    p = w.persons[holder]
    p.ledger.append(Claim("c_b11a_deed", holder, about, "fight.declared", True, w.tick, "firsthand", 100, "own"))
    p.pursuits = {"liberty": 1.0}


def _formed(w, pid, verb):
    p = w.persons[pid]
    qs = world_q.questions_for(w, p)
    if not qs:
        return []
    q = qs[0]
    return [c for c in O.opening_set(p, assemble(p, q, 12), q, w.fixtures) if c.verb == verb]


# ---- (1) formation ---------------------------------------------------------------------------------------------

def test_the_rows_declare_their_classes_and_challenge_asks_individuals():
    assert VERB_TABLE["challenge"].referent_class == "Disputant"
    assert VERB_TABLE["capture"].referent_class == "Person"
    rels = [getattr(c, "relation", None) for c in VERB_TABLE["challenge"].requires_typed.requirement.clauses]
    assert rels.count("individual") == 2


def test_a_grievance_beside_him_is_stamped_and_forms_the_challenge_and_none_without_it():
    w, _ = _world()
    assert world_q.disputes_held(w, w.persons[A]) == ()
    assert not _formed(w, A, "challenge"), "CONTROL: no grievance, no challenge"
    _grievance(w)
    assert world_q.disputes_held(w, w.persons[A]) == (B,)
    assert [c.subject for c in _formed(w, A, "challenge")] == [B]


def test_a_grievance_against_a_man_elsewhere_is_not_stamped():
    w, _ = _world()
    _grievance(w, about=FAR)
    assert world_q.disputes_held(w, w.persons[A]) == ()


def test_the_subject_of_a_challenge_is_its_opponent_and_obliges_is_not():
    assert O.subject_is_opponent(VERB_TABLE["challenge"])
    assert not O.subject_is_opponent(VERB_TABLE["oblige"])


def test_the_import_refuses_an_opposed_row_whose_second_side_is_not_its_subject():
    with pytest.raises(Exception):
        V._load_opposed_without_prize(["tell"])


def test_the_violence_context_roster_lists_no_duel_for_fight():
    assert "duel" not in V.VIOLENCE_CONTEXTS["fight"]


# ---- (2)-(4) the chain, through formation and the fold ---------------------------------------------------------

def test_falsifier_the_chain_fires_from_a_planted_grievance_and_the_revert_forms_nothing(monkeypatch):
    w, d = _world()
    _grievance(w)
    (ch,) = _formed(w, A, "challenge")
    out = _resolve(w, d, *_acts(w, A, [ch]))
    assert [e.kind for e in out] == ["challenge.issued"], [e.kind for e in out]
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    (rid,) = [r for r, rec in w.records.items() if rec.kind == "challenge"]
    pb = w.persons[B]
    assert O.documents_known_as(pb).get(rid) == frozenset({"challenge"}), "the addressee read what was put to him"
    assert world_q.challenges_heard(w, pb) == (rid,)
    acc = _formed(w, B, "accept")
    assert [(c.subject, c.operands.get("to")) for c in acc] == [(rid, A)], "one Candidate, against the challenger"
    kinds = [e.kind for e in _run(w, d, *_acts(w, B, acc))]      # RESOLVE declares; ENCOUNTER fights (a draw)
    assert kinds and kinds[0] == "accept.declared", kinds
    assert set(kinds[1:]) & {"duel.yielded", "body.changed", "person.died", "contest.undecided"}, kinds
    # THE REVERT: the same world and grievance. On this two-man world the grievance's own question names B, so the
    # unclassed row still forms the challenge (the realm's measured gap is the question that does not); the chain
    # breaks at the challenged, who holds no reading of the challenge and is offered no `accept`.
    revert_b11a(monkeypatch)
    w2, d2 = _world()
    _grievance(w2)
    (ch2,) = [c for c in _formed(w2, A, "challenge") if c.subject == B]
    out2 = _resolve(w2, d2, *_acts(w2, A, [ch2]))
    d2.witness(mint_token(w2, WriteClass.INTERIOR), out2)
    assert O.documents_known_as(w2.persons[B]) == {}
    assert not _formed(w2, B, "accept")


def test_accept_does_not_form_on_a_document_read_as_another_kind():
    w, _ = _world()
    p = w.persons[B]
    assert O.documents_known_as(p) == {}
    p.ledger.append(Claim("c_doc", B, "rec:x", "content:dispensation", (("terms", A), ("to", (B,)), ("at", None)),
                          0, "firsthand", 100, "own"))
    assert O.documents_known_as(p) == {"rec:x": frozenset({"dispensation"})}
    assert not V.RECORD_SUBKINDS_BY_VERB["accept"] & O.documents_known_as(p)["rec:x"]


def _reread_as(p, rid, kind):
    """`p`'s every reading of `rid` re-stemmed to `content:<kind>` (the value kept): the same document, read as `kind`."""
    n = 0
    for c in p.ledger:
        if c.subject == rid and c.predicate.startswith("content:"):
            c.predicate = f"content:{kind}"
            n += 1
    assert n, "the addressee held a reading to re-stem"


def test_falsifier_accept_forms_through_opening_set_only_on_a_document_read_as_a_challenge():
    """THE SUB-KIND FILTER, THROUGH `opening_set` (`decision/options.py`, the non-holding branch of
    `RECORD_SUBKINDS_BY_VERB`): the challenged holds a reading of a real challenge Record, so `challenges_heard` still
    puts it on his question, and `accept` forms on it only while his reading says it is a challenge. The same document
    read as `works` forms no `accept`. Seen RED with the filter deleted (`accept` formed on the misread document, against
    `p_mid`). `works` and not `dispensation`: a `dispensation` reading answers `accept`'s fan operand from the document
    (`rosters.yaml: record_sourced_operands`), so the operand bag declines it with or without the filter; a kind that
    sources no operand falls through to the bag per person known, where the filter is the only gate."""
    w, d = _world()
    _grievance(w)
    (ch,) = _formed(w, A, "challenge")
    d.witness(mint_token(w, WriteClass.INTERIOR), _resolve(w, d, *_acts(w, A, [ch])))
    (rid,) = [r for r, rec in w.records.items() if rec.kind == "challenge"]
    pb = w.persons[B]
    assert [c.subject for c in _formed(w, B, "accept")] == [rid], "CONTROL: read as a challenge, it forms"
    _reread_as(pb, rid, "works")
    assert O.documents_known_as(pb) == {rid: frozenset({"works"})}
    assert world_q.challenges_heard(w, pb) == (rid,), "the referent still reaches his question"
    assert not _formed(w, B, "accept"), "a document he reads as works is no challenge to him"


def test_falsifier_a_held_document_read_as_another_kind_declines_carry():
    """THE HOLDING BRANCH (`RECORD_SUBKINDS_HELD`, `carry` on a petition): the petitioner holds his filed petition and
    `carry` forms on it while he holds no reading of it (unknown forms) and while his reading says petition; the same
    held document read as a dispensation declines. Seen RED with the filter deleted (`carry` formed on the misread one)."""
    from .test_in45_carry import PETITION, PETITIONER, _carries, _filed
    w, _d = _filed()
    p = w.persons[PETITIONER]
    assert O.documents_known_as(p) == {}
    (q,) = world_q.questions_for(w, p)
    assert [c.subject for c in _carries(w, p, q)] == [PETITION], "CONTROL: unread, it forms"
    p.ledger.append(Claim("c_pet_read", PETITIONER, PETITION, "content:petition", (("terms", A), ("to", "p_high")),
                          0, "firsthand", 100, "own"))
    (q,) = world_q.questions_for(w, p)
    assert [c.subject for c in _carries(w, p, q)] == [PETITION], "CONTROL: read as a petition, it forms"
    _reread_as(p, PETITION, "dispensation")
    (q,) = world_q.questions_for(w, p)
    assert (PETITION, "Record") in q.classes, "the held document still reaches his question"
    assert _carries(w, p, q) == [], "a held document he reads as a dispensation is no petition to carry"


# ---- the realm hash: mover, and the revert ---------------------------------------------------------------------

@pytest.mark.parametrize("seed", [0, 1, 2])
def test_hash_post_lane_and_revert(seed, monkeypatch):
    # B11 lane A's second item (persons hold scores; the obstacle by task, a later mover of the build and every season) is
    # reverted in process, so POST still reads the reach alone.
    from .test_b11a_scores_and_obstacle import revert_b11a_scores
    revert_b11a_scores(monkeypatch)
    w = build_realm(seed)
    run(1, seed, w=w)
    assert w.content_hash() == POST[seed] != PRE[seed]
    revert_b11a(monkeypatch)
    w = build_realm(seed)
    run(1, seed, w=w)
    assert w.content_hash() == PRE[seed]
