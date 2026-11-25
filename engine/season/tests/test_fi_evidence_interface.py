"""B24.22 (FI_05_B "What FI supplies" 1): what kind of proof a held claim is, read once, and whether it impeaches a document.

`person_q.proof_kind(c)` is DERIVED from the claim (its predicate), never declared; `person_q.impeaches(c, record_id)` is a covert deed claim
whose subject is the Record. Both read the one claim and no World. Both tests are game-state tests in the `season_loop` lane (this file's
tree): each runs the reader over the claims the fold deposits, the kinds the verb table emits.
"""

from __future__ import annotations

from fractions import Fraction

from ..data import verbs as _verbs
from ..data.matrix import WriteClass
from ..data.rosters import COVERT_KINDS, MATTERS
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import person_q
from ..state.carriers import Act, Claim, Event, Record, Said
from ..state.ids import H


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


def test_a_cites_payload_is_told_like_said():
    """B24.24 / E-3 (game-state, season_loop): a `speak` that cites is a telling. Hand-built (no computed act carries `cites` before B24.27), the act cites one held claim
    and one Record; at EVERY band the verb grades, `Failure` included (ADM: the room heard it said), each present hearer comes to hold one told copy of the claim with
    the citer on its chain and one `content:<kind>` claim of the Record, with the citer on its chain; the citer holds no copy of his own telling; an Event the verb's row
    does not emit, or that grades no band (the refusal kind), tells nothing; and an act citing nothing deposits no told claim."""
    emits = _verbs.VERB_TABLE["speak"].emits_by_degree
    assert set(emits) >= {"Failure", "Partial", "Success", "Overwhelming"}
    teller, hearer = "p_low", "p_mid"
    content = {"terms": "prop_x", "to": ("p_other",), "from": teller}
    checked = 0
    for band in ("Failure", "Partial", "Success", "Overwhelming"):
        w = P.tiny_world()
        w.records["r_doc"] = Record("r_doc", "Hh", "petition", subject_matter=content)
        held = Claim("c_held", teller, "Hh", "stores:grain", 8, 0, "firsthand", 41, "own")
        w.persons[teller].ledger.append(held)
        said = Said("Hh", "stores:grain", 8, 41)
        act = Act(id=f"a_cite_{band}", actor=teller, verb="speak",
                  payload={"subject": "Hh", "cites": ("c_held", "r_doc"), "cited": {"c_held": said}})
        w.acts.append(act)
        d = SeasonDriver(w)

        def fire(kind, degree, _w=w, _act=act, _d=d):
            ev = Event(H(_w.world_seed, _w.tick, teller, f"ev:{kind}:{_act.id}"), kind, [], [_act.id], _w.tick, degree, ())
            _w.log.append(ev)
            _d.act_of[ev.id] = _act
            _d.witness(mint_token(_w, WriteClass.INTERIOR), [ev])

        def told(pid, _w=w):
            return [c for c in _w.persons[pid].ledger if c.source == "told_by"]

        fire(sorted(_verbs.VERB_TABLE["speak"].emits_on_refusal)[0], None)     # a refusal grades no band: nothing was said
        fire("conviction.moved", band)                                          # not an Event the speak row emits
        assert not told(hearer), f"{band}: an Event that is no telling of the citing verb told something: {told(hearer)}"
        fire(emits[band][0], band)
        mine = told(hearer)
        claim = [c for c in mine if c.predicate == "stores:grain"]
        doc = [c for c in mine if c.subject == "r_doc"]
        assert len(claim) == 1 and claim[0].chain == (teller,) and claim[0].confidence == 41, (band, mine)
        assert (claim[0].value != 8) <= (band == "Partial"), f"{band}: the told value drifted at a band that is not Partial (the told channel's own grading): {claim[0].value}"
        assert len(doc) == 1 and doc[0].predicate == "content:petition" and doc[0].chain == (teller,), (band, mine)
        assert len({c.id for c in mine}) == len(mine) == 2, f"{band}: two claims one act passed on share an id"
        assert not told(teller), f"{band}: the citer holds a told copy of his own citation"
        checked += 1
    assert checked == 4

    w = P.tiny_world()
    w.persons[teller].ledger.append(Claim("c_held", teller, "Hh", "stores:grain", 8, 0, "firsthand", 41, "own"))
    act = Act(id="a_plain", actor=teller, verb="speak", payload={"subject": "Hh"})
    w.acts.append(act)
    d = SeasonDriver(w)
    ev = Event(H(w.world_seed, w.tick, teller, "ev:plain"), emits["Success"][0], [], [act.id], w.tick, "Success", ())
    w.log.append(ev)
    d.act_of[ev.id] = act
    d.witness(mint_token(w, WriteClass.INTERIOR), [ev])
    assert not [c for c in w.persons[hearer].ledger if c.source == "told_by"], "a speak that cites nothing deposited a told claim"


def test_a_cited_id_not_held_is_refused_before_the_draw():
    """B24.25 / FI_05_B E-1 (game-state, season_loop), on `build_hearing`'s real fold: a `speak` is refused BEFORE ANY DRAW -- the row's refusal kind, `Event.degree` None, nothing on the case file -- when it cites
    an id the speaker does not hold (a claim id nobody holds, another person's claim, a Record the other party holds), when the kind of what it cites is one the matter's row does not admit (`parliamentary_debate`
    admits no proof; a deed claim reads `testimony`, `person_q.proof_kind`), and when it answers a stage that is no filed stage or is his own side's. The control beside each is the same speech with a held,
    admitted cite and a stage of the other side: it draws a band and writes a stage. FALSIFIER: a refused speech that has a degree, or writes."""
    from ..queries import world_q
    from .test_sc_hearing_admission import DEED, G, cite, hearing, fold_and_witness, records_of
    refusal = _verbs.VERB_TABLE["speak"].emits_on_refusal
    checked = 0
    for seed in range(12):
        w, d, case = hearing(seed)
        w.persons[G.ACCUSED].ledger.append(Claim("c_theirs", G.ACCUSED, G.ACCUSER, DEED, True, 0, "firsthand", 100, "own"))
        n = len(w.records[case].stages)
        for ids in (("c_nobody",), ("c_theirs",), (records_of(w, G.ACCUSED)[0],), ("c_deed", records_of(w, G.ACCUSED)[1])):
            out = fold_and_witness(w, d, cite(w, ids, key=f"sp_{ids[-1]}"))
            assert tuple(e.kind for e in out) == refusal and out[0].degree is None and len(w.records[case].stages) == n, (seed, ids, [(e.kind, e.degree) for e in out])
        n_own = len(w.records[case].stages)
        w.records[case].stages.append((1, "filed", "for", "fact", Said(G.ACCUSED, "stores.level", 1, 5), 1.0, G.ACCUSER, "a0"))
        for places in ((0,), (99,), (n_own,)):                                                       # a clock stage, a place off the file, his own side's stage
            out = fold_and_witness(w, d, cite(w, (), key=f"sp_ans{places[0]}", answers=places))
            assert tuple(e.kind for e in out) == refusal and out[0].degree is None, (seed, places, [(e.kind, e.degree) for e in out])
        # the control: a held, admitted cite files; and a row that admits no proof refuses the same deed claim
        w2, d2, case2 = hearing(seed)
        out = fold_and_witness(w2, d2, cite(w2, ("c_deed",)))
        assert out[0].degree is not None and out[0].kind not in refusal and any(s[1] in ("filed", "excluded") for s in w2.records[case2].stages), (seed, out)
        w3, d3, case3 = hearing(seed)
        world_q.docketed(w3, G.ACCUSED)[0][world_q.DOCKET_ARRANGEMENT] = "parliamentary_debate"
        out3 = fold_and_witness(w3, d3, cite(w3, ("c_deed",)))
        assert tuple(e.kind for e in out3) == refusal and out3[0].degree is None and not any(s[1] in ("filed", "excluded") for s in w3.records[case3].stages), (seed, out3)
        checked += 1
    assert checked == 12
