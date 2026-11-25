"""B24.22 (FI_05_B "What FI supplies" 1): what kind of proof a held claim is, read once, and whether it impeaches a document.

`person_q.proof_kind(c)` is DERIVED from the claim (its predicate), never declared; `person_q.impeaches(c, record_id)` is a covert deed claim
whose subject is the Record. Both read the one claim and no World. Both tests are game-state tests in the `season_loop` lane (this file's
tree): each runs the reader over the claims the fold deposits, the kinds the verb table emits.
"""

from __future__ import annotations

from fractions import Fraction

from ..data import verbs as _verbs
from ..data.rosters import COVERT_KINDS, MATTERS
from ..queries import person_q
from ..state.carriers import Claim, Said


def _claim(predicate: str, *, subject: str = "p_x", value=True, chain: tuple = ()) -> Claim:
    return Claim("c_" + predicate, "p_h", subject, predicate, value, 0, "firsthand", 3, "own", chain=chain)


def test_proof_kind_follows_the_e1_table():
    """E-1: an untold deed claim and a chained one are `testimony` (the chain's discount is `teller_weight`'s, not a kind); a `confession.*` deed
    is `confession` unless it was withheld (B24.23); a claim that is no deed (a cell, a refusal kind, a false value) is no proof. Every kind it returns is a `matters` member."""
    deeds = sorted(_verbs.DEED_KINDS)
    confessions = [k for k in deeds if k.startswith("confession.")]
    plain = [k for k in deeds if not k.startswith("confession.")]
    assert confessions and plain
    for k in plain:
        assert person_q.proof_kind(_claim(k)) == "testimony" == person_q.proof_kind(_claim(k, chain=("p_a", "p_b"))), k
    for k in confessions:
        assert person_q.proof_kind(_claim(k)) == ("confession" if k != "confession.withheld" else None), k              # B24.23: a withheld one is no proof
    assert person_q.proof_kind(Said("p_x", plain[0], True, 3, ("p_a",))) == "testimony"                    # a told copy reads the same
    refusal = sorted(_verbs.REFUSAL_KINDS)[0]
    assert person_q.proof_kind(_claim(refusal)) is None and person_q.proof_kind(_claim(plain[0], value=False)) is None
    assert person_q.proof_kind(_claim("stance", value=0.4)) is None
    assert {person_q.proof_kind(_claim(k)) for k in deeds} - {None} <= set(MATTERS)       # None only for the withheld confession


def test_impeaches_reads_only_a_covert_deed_on_the_record():
    """E-5 item 2: a held deed claim whose subject is the cited Record and whose kind is a `covert_kinds` member impeaches it; the same kind
    on another subject, an overt deed on the Record, and a claim that is no deed do not."""
    rec = "rec_x"
    overt = sorted(_verbs.DEED_KINDS - set(COVERT_KINDS))
    assert COVERT_KINDS and overt
    for k in sorted(COVERT_KINDS):
        assert person_q.impeaches(_claim(k, subject=rec), rec), k
        assert not person_q.impeaches(_claim(k, subject="rec_other"), rec), k
        assert not person_q.impeaches(_claim(k, subject=rec, value=False), rec), k
    assert not any(person_q.impeaches(_claim(k, subject=rec), rec) for k in overt)
    assert person_q.impeaches(Said(rec, sorted(COVERT_KINDS)[0], True, 3), rec)                            # the told copy keeps its subject (E-5)


def test_a_withheld_confession_is_no_proof_and_a_full_one_is():
    """B24.23 (H-311): the exhibits the questioner holds against a prisoner are `attributed_deeds` of his, each `proof_weight`. One whose interrogation rolled
    Failure (`confession.withheld` on file) is worth 0, exactly a prisoner never questioned; Success and Overwhelming are worth 1 and Partial 0.5 (the
    `task_fraction` share of the band the `interrogate` row emits each kind at). Another deed of his stays a proof worth 1."""
    row = _verbs.VERB_TABLE["interrogate"]
    ledger_of = lambda *kinds: [_claim(k, subject="p_prisoner") for k in kinds]
    total = lambda ledger: sum(person_q.proof_weight(c) for c in person_q.attributed_deeds(ledger, "p_prisoner"))
    got = {b: total(ledger_of(*row.emits_by_degree[b])) for b in ("Overwhelming", "Success", "Partial", "Failure")}
    assert got == {"Overwhelming": 1, "Success": 1, "Partial": Fraction(1, 2), "Failure": 0}, got
    assert row.emits_by_degree["Failure"] == ["confession.withheld"] and total(ledger_of("confession.withheld")) == total([]) == 0
    other = sorted(_verbs.DEED_KINDS - set(person_q.CONFESSION_BAND))[0]
    assert total(ledger_of(other)) == 1 and person_q.proof_weight(_claim("stance", value=0.4)) == 0
