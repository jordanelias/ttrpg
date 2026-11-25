"""B24.18 -- `contradicts(a, b)` is the pairing rule, exposed once (EVID_B "Exact edits" 2).

Two claims contradict when `_pair` marks one as disagreeing with the other on the cell `(subject, predicate)`: the same cell, a different value. The host
(`dossier.against`, `world_q.contradicted_tellers`) and `decision/options.py` read the one predicate; nothing restates `==`.

B24.19 -- `modules/social_contest/evidence.py::standing` is the one evidence rule (EVID_B edit 3): which exhibits still count, the relation read as data
(`Item.pairs`) from the host, the answering act's band (`Item.answered_band`) read and never regraded.
"""
from __future__ import annotations

import importlib
from dataclasses import replace

from ..decision import options as OP
from ..queries import person_q, world_q
from ..seam.wrappers import sigma
from ..data import verbs as _verbs
from ..state.carriers import Act, Claim, Said

CELL = "stores.level"                       # a cell predicate (`requires.CELL_STEMS`)


def _c(i: int, value, subject: str = "s1", predicate: str = CELL) -> Claim:
    return Claim(f"c{i}", "p_me", subject, predicate, value, 0, "firsthand", 5, "own")


def test_contradicts_is_the_pairing_rule():
    cases = [
        (_c(1, 3), _c(2, 4), True),                           # same cell, different value
        (_c(1, 3), _c(2, 3), False),                          # same cell, same value
        (_c(1, 3), _c(2, 4, predicate="stores.tier"), False),  # different predicate
        (_c(1, 3), _c(2, 4, subject="s2"), False),            # different subject
    ]
    checked = 0
    for a, b, want in cases:
        paired = person_q._pair([a], [b], lambda c: (c.subject, c.predicate), None)
        assert OP.contradicts(a, b) is want
        assert OP.contradicts(b, a) is want                   # symmetric
        assert (paired[1] == 1) is want                       # `_pair` and `contradicts` agree on the pair
        checked += 1
    assert checked == len(cases)
    assert OP.contradicts is person_q.contradicts             # one owner, re-bound by name


# ---- B24.19: `standing`, the one evidence rule inside the module (EVID_B edit 3) -------------------------------------------------------

def _it(iid, side, w=1.0, origin=None, pairs=(), cell=("s1", "stores.level", 3), band=None, **kw):
    from ..queries.inputs import Item
    return Item(iid, "record", w, side=side, cell=cell, origin=origin, pairs=tuple(pairs), answered_band=band, **kw)


def _ev():
    return importlib.import_module("modules.social_contest.evidence")            # by name, as the module's other tests do: `engine/` names no module by import


def _standing(presented, findings=(), cap=None):
    return _ev().standing(tuple(presented), tuple(findings), cap)


def test_corroboration_is_noisy_or_by_origin():
    """EVID_B gate 4: two items of one cell and value on one side, weights 0.5 and 0.5, from distinct origins are ONE item of 0.75; from one origin, 0.5
    (and the origin counted once however many items it filed); `evidence_cap` caps what the corroboration gains. FALSIFIER: an additive reading gives 1.0."""
    agree = (("b", "agrees"),)
    two = [_it("a", "for", 0.5, "o1", agree), _it("b", "for", 0.5, "o2", (("a", "agrees"),))]
    one = [replace(i, origin="o1") for i in two]
    got, struck, faults = _standing(two)
    assert [(i.id, i.weight) for i in got] == [("a", 0.75)] and struck == () and faults == ()
    assert [(i.id, i.weight) for i in _standing(one)[0]] == [("a", 0.5)]
    assert _standing(two, cap=0.6)[0][0].weight == 0.6                      # the cap limits the gain, it does not lower an item
    assert _standing(two, cap=0.1)[0][0].weight == 0.5
    lone = [_it("a", "for", 0.5, "o1"), _it("b", "for", 0.5, "o2")]         # same cell, nothing filed as agreeing: two items, each counted
    assert [i.weight for i in _standing(lone)[0]] == [0.5, 0.5]


def test_an_off_rung_item_enters_at_half_and_a_same_origin_second_adds_less():
    """KERN_B check 3: an item off the rung tried enters the sitting's board at half weight (and `irrelevance` is recorded against its side); a second item of
    one origin on a hand-built board adds nothing where one of a distinct origin adds, so the sum of the board is the rule's and not the items'."""
    from ..queries.inputs import Choice
    from .test_sc_proceeding_module import P, _inp, _key, _p, _rite, _sit
    evidence = _ev()
    on, off = _it("i1", "for", 2.0, rung="fact"), _it("i2", "for", 2.0, rung="definition")
    a = _p("a", "for", items=(on, off))
    inp = _inp([a, _p("b", "against"), _p("j0", decides=True, precedence=1)], _rite(close="bench", admits=("record",), issues=("fact", "definition")))
    st, _ = P.exchange(inp, _sit(inp), a, Choice("present", None, "i1"), _key("rung", 0))
    st, _ = P.exchange(inp, st, a, Choice("present", None, "i2"), _key("rung", 1))
    assert [(i.id, i.weight) for i, _ in st.board] == [("i1", 2.0), ("i2", 1.0)] and st.faults == (("irrelevance", "for"),)
    first = [_it("x", "for", 0.8, "o1", (("y", "agrees"), ("z", "agrees")))]
    same = first + [_it("y", "for", 0.6, "o1", (("x", "agrees"),))]
    other = first + [_it("z", "for", 0.6, "o2", (("x", "agrees"),))]
    w = lambda b: sum(i.weight for i in evidence.standing(tuple(b), (), None)[0])
    assert w(first) == w(same) == 0.8 and w(other) > 0.8 and w(other) - w(first) < 0.6        # one origin adds nothing; a second origin adds less than its weight


def test_an_answer_of_the_same_value_strikes_nothing():
    """EVID_B falsifier: an answer that says what the item says is AGREEMENT (rule 3), whatever its band: neither counts, nothing is struck, nothing is owed."""
    for band in ("Failure", "Partial", "Success", "Overwhelming"):
        got, struck, faults = _standing([_it("a", "for", 1.0, "o1", (("b", "agrees"),), band=band), _it("b", "against", 1.0, "o2", (("a", "agrees"),))])
        assert (got, struck, faults) == ((), (), ()), band


def test_an_answer_acts_by_its_band_on_the_item_it_answers():
    """Rules 1 and 2, band by band, on the answering act's own band: contradiction (Failure stands, Partial halves it and its answer, Success strikes it,
    Overwhelming strikes it and charges its citer if he knew it false, else its origin) and forgery (Failure: the impeacher bears `failed_impeachment`; Partial
    halves; Success strikes it alone; Overwhelming strikes every item of its origin and records `forgery_found`). An item never answered is never struck."""
    def board(band, **kw):
        return [_it("t", "for", 1.0, "o1", (("r", "contradicts"),), band=band, **kw), _it("r", "against", 0.5, "o2", (("t", "contradicts"),)),
                _it("m", "for", 1.0, "o1", (), cell=("s2", "stores.level", 1))]
    ws = lambda b, f=(), **kw: {i.id: i.weight for i in _standing(board(b, **kw), f)[0]}
    assert ws(None) == ws("Failure") == {"t": 1.0, "r": 0.5, "m": 1.0}
    assert ws("Partial") == {"t": 0.5, "r": 0.25, "m": 1.0}
    assert _standing(board("Success"))[1:] == (("t",), ()) and _standing(board("Overwhelming"))[1:] == (("t",), (("discredited_source", "o1"),))
    assert _standing(board("Overwhelming", sincere=False))[2] == (("self_contradiction", "for"),)
    checked = 0
    for band, want in (("Failure", ((), (("failed_impeachment", "against"),))), ("Partial", ((), ())), ("Success", (("t",), ())),
                       ("Overwhelming", (("t", "m"), (("forgery_found", "for"),)))):
        _, struck, faults = _standing(board(band), findings=("t",))
        assert (struck, faults) == want, band
        checked += 1
    assert ws("Partial", ("t",)) == {"t": 0.5, "r": 0.5, "m": 1.0} and checked == 4         # a forgery's Partial halves the Record alone


def test_a_sitting_strikes_an_answered_item_by_the_rule_over_the_bands_drawn():
    """The sitting decides nothing about an answer: it grades the margin on the ladder, files the band on the item, and the board is `standing` over the items
    shown. Over 40 keys every band occurs; the item is struck at Success and Overwhelming only, and halved (its weight now) at Partial."""
    from ..data.arrangements import GROUNDS
    from ..queries.inputs import Choice
    from .test_sc_proceeding_module import P, _inp, _key, _p, _rite, _sit
    ground = next(g for g, r in GROUNDS.items() if r["reads"] != "item")
    i1, j1 = _it("i1", None, 1.0, "o1", (("j1", "contradicts"),)), _it("j1", None, 1.0, "o2", (("i1", "contradicts"),), cell=("s1", "stores.level", 4))
    a, b = _p("a", "for", items=(i1,)), _p("b", "against", items=(j1,))
    inp = _inp([a, b, _p("j0", decides=True, precedence=1)], _rite(close="bench", admits=("record",)))
    seen = {}
    for k in range(40):
        st, _ = P.exchange(inp, _sit(inp), a, Choice("present", None, "i1"), _key("ans", k))
        st, _ = P.exchange(inp, st, b, Choice("present", None, "j1"), _key("ans", k + 100))
        st, beat = P.exchange(inp, st, b, Choice("answer", ground, "i1"), _key("ans", k + 200))
        held, struck, _faults = _standing([i for i, _ in st.board])
        band = {i.id: i.answered_band for i, _ in st.board}["i1"]
        assert [(i.id, s) for i, s in st.board] == [("i1", "struck" if "i1" in struck else "answered"), ("j1", "stands")]    # the board is the rule's reading
        assert beat.struck == tuple(struck) and ("i1" in struck) == (band in ("Success", "Overwhelming"))
        seen[band] = {i.id: i.weight for i in held}.get("i1")
    assert set(seen) == {"Failure", "Partial", "Success", "Overwhelming"} and seen["Partial"] == 0.5 and seen["Failure"] == 1.0 and seen["Success"] is None


# ---- B24.20: the roll adds the standing items as `proofs` levels (EVID_B edit 5a) -----------------------------------------------------

def _roll_rec(exhibits=(), **kw):
    from ..queries.inputs import SocialContestInput
    base = dict(pool=2, opposition=8.0, obstacle_ceiling=None, obstacle_refusal_multiple=float("inf"), leverage=0.0, difficulty=0.0, pool_default=4,
                pool_add=0, opposition_rate=0.5, exhibits=tuple(exhibits), proof_level="minor", side="for")
    base.update(kw)
    return SocialContestInput(**base)


def test_a_struck_item_adds_no_proofs_level():
    """KERN_B check 4's companion and EVID_B's falsifier, on the roll's closed form: pool 2 against a score of 8 has different odds with 0 and 4 standing items
    (the levels are applied) and the SAME obstacle and terms (A-25: nothing favourable is subtracted); a struck item adds no level (an Overwhelming answer
    strikes it, a Failure leaves it standing); the same weight standing for the other side counts against the roller, one level for one level."""
    from engine.dice_engine.sigma_leverage import band_odds, net_boost
    roll = importlib.import_module("modules.social_contest.roll")

    def odds(rec):
        return band_odds(rec.pool, roll.obstacle(rec)[0], net_boost(roll.leverage(rec), rec.pool))
    four = [_it(f"f{i}", "for", 1.0, f"o{i}", cell=("s1", "stores.level", i)) for i in range(4)]
    none, held = _roll_rec(), _roll_rec(four)
    assert roll.obstacle(none) == roll.obstacle(held)                         # the obstacle is the empty case file's, to the term
    assert roll.proof_levels(none) == (0, 0) and roll.proof_levels(held) == (4, 0)
    assert odds(none) != odds(held) and roll.leverage(held) == 4 * 0.25 and roll.leverage(none) == 0.0
    foe = [_it("g", "against", 1.0, "og", cell=("s1", "stores.level", 9))]
    assert roll.proof_levels(_roll_rec(four + foe)) == (4, 1) and roll.leverage(_roll_rec(four + foe)) == 3 * 0.25
    answered = lambda band: [replace(four[0], pairs=(("g", "contradicts"),), answered_band=band), _it("g", "against", 1.0, "og", (("f0", "contradicts"),)), *four[1:]]
    struck, stood = roll.proof_levels(_roll_rec(answered("Overwhelming"))), roll.proof_levels(_roll_rec(answered("Failure")))
    assert struck == (3, 1) and stood == (4, 1)                              # the struck one adds none; the answered-and-failed one stands
    assert roll.leverage(_roll_rec(four, proof_level=None)) == 0.0            # `proof_level` None is the control arm: no level, the counts still reported


# ---- B24.21: the host passes the case file's exhibits, with their relations (EVID_B edit 5) --------------------------------------------------

def test_the_sittings_board_and_the_rolls_exhibits_count_one_quantity_one_way():
    """B24.21 (c): the sitting's closing leverage (`proceeding._lever`) and the roll's (`roll.leverage`) price one board of standing weight with ONE rounding, half up, each side's weight
    counted in whole units on its own. On a board of 0.5 + 0.4 for and 0.4 against the roll counts (1, 0), and so must the sitting: the old truncation of the NET (0.5) read no level there.
    FALSIFIER: the sitting's lever 0 where the roll's is a level."""
    from .test_sc_proceeding_module import _inp, _p, _rite, _sit
    proceeding, roll = importlib.import_module("modules.social_contest.proceeding"), importlib.import_module("modules.social_contest.roll")
    checked = 0
    for weights in (((0.5, "for"), (0.4, "for"), (0.4, "against")), ((1.6, "for"), (0.6, "against")), ((0.4, "for"), (0.4, "against")), ((2.0, "for"), (1.0, "against"))):
        items = [_it(f"i{k}", side, w, f"o{k}", cell=("s1", "stores.level", k)) for k, (w, side) in enumerate(weights)]
        inp = _inp([_p("a", "for"), _p("b", "against"), _p("j0", decides=True, precedence=1)], _rite(close="bench"))
        lever = proceeding._lever(inp, _sit(inp, board=tuple((it, "stands") for it in items)))
        assert lever == roll.leverage(_roll_rec(items)), weights
        checked += 1
        if weights[0] == (0.5, "for"):
            assert lever == 0.25                                              # one level `minor`, where the net's truncation read none
    assert checked == 4


def _planted_case(w, matter, stages):
    """`matter` docketed under `arbitration`, its case file a Record holding `stages`."""
    from ..state.carriers import Record
    w.records["case1"] = Record("case1", "Hh", "text", stages=list(stages))
    w.docket.append({"date": None, "matter": matter, world_q.DOCKET_ARRANGEMENT: "arbitration", world_q.DOCKET_PETITION: None, world_q.DOCKET_CASE: "case1"})


def test_the_case_file_is_the_proofs_of_a_docketed_matter_and_the_ledger_is_not():
    """B24.21 (EVID_B edit 5; falsifier: the proofs read BOTH from exhibits and from `world_q.proofs` for one matter). The speaker holds four ledger proofs against the party; the matter's case
    file holds five `filed` stages, a failed one (`excluded`) and a sitting's `entered`. At `evidence_from: case_file` the roll's `proofs` levels are the exhibits' alone -- two stand for the
    speaker (the third is the other side's identical claim as well, which counts for neither), one against him (a cell the other side put differently, unanswered so standing) -- and his ledger adds
    none; at `ledger` (the control) they are the ledger's and no exhibit is built; a matter with no case file reads the ledger at either arm. The obstacle is the same at both, to the term (A-25)."""
    from engine.dice_engine import draw
    from engine.dice_engine.sigma_leverage import levels_to_net_sigma
    from ..data import verbs as _verbs
    from ..state.carriers import Said
    from . import test_sc02_reception as R
    from .test_sc01_obstacle_ceiling import _module
    deed = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)[0]
    stages = [(1, "filed", "for", "fact", Said("s1", CELL, 3, 5), 1.0, "o1", "a1"),
              (1, "filed", "for", "fact", Said("s1", "stores.tier", 1, 5), 1.0, "o2", "a1"),
              (1, "filed", "for", "fact", Said(R.PARTY, deed, True, 5), 1.0, "o3", "a1"),
              (2, "filed", "against", "fact", Said("s1", CELL, 4, 5), 1.0, "o4", "a2"),          # the first's cell, a different value
              (2, "filed", "against", "fact", Said(R.PARTY, deed, True, 5), 1.0, "o5", "a2"),    # the third's own claim, from the other side
              (3, "excluded", "for", Said("s1", "stores.tier", 9, 5), "a3"), ("entered", "x")]

    def read(arm, case=True):
        w, _d = R._judging_world(evidence_from=arm)
        R._proofs(w, 4)
        if case:
            _planted_case(w, R.PARTY, stages)
        else:
            w.docket.append({"date": None, "matter": R.PARTY, world_q.DOCKET_ARRANGEMENT: "arbitration", world_q.DOCKET_PETITION: None, world_q.DOCKET_CASE: None})
        room = world_q.place_of(w, R.SPEAKER)
        inp = sigma.contest_input(w, [R.SPEAKER, R.PARTY], verb="arrest", subject=R.PARTY, room=room)
        out = sigma.resolve(w, [R.SPEAKER, R.PARTY], ["root"], R.PRIZE, verb="arrest", subject=R.PARTY, rng=draw.seeded(draw.H2("b24_21", 0)), rung=room)
        return inp, out, next((f, a) for n, f, a in out["levels"] if n == "proofs")
    ledger_inp, ledger_out, ledger = read("ledger")
    case_inp, case_out, case = read("case_file")
    bare_inp, _o, bare = read("case_file", case=False)
    assert ledger_inp.exhibits == () and ledger[0] > 0 and ledger[1] == 0                                    # the control: the ledger's proofs, no exhibit built
    assert case == (2, 1) and len(case_inp.exhibits) == 5 and case_inp.proofs == 0.0 < ledger_inp.proofs     # the case file's, and the ledger read for the matter by nothing
    assert bare_inp.exhibits == () and bare == ledger and bare_inp.proofs == ledger_inp.proofs               # a matter with no case file keeps the ledger at the case_file arm
    first, tier, own, foe, twin = case_inp.exhibits
    assert dict(first.pairs) == {foe.id: "contradicts"} and dict(tier.pairs) == {} and dict(own.pairs) == {twin.id: "agrees"} and dict(twin.pairs) == {own.id: "agrees"}
    assert (first.side, first.rung, first.weight, first.origin, first.cell) == ("for", "fact", 1.0, "o1", ("s1", CELL, 3)) and first.id == "case1#0"
    assert dict(_module().obstacle(ledger_inp)[1]) == dict(_module().obstacle(case_inp)[1]), "the exhibits are leverage, never an obstacle term"
    assert case_out["leverage"] - case_inp.leverage == levels_to_net_sigma(["minor"] * 2, ["minor"]) == 0.25    # what the roll applied is what the record names
    assert ledger_out["leverage"] == ledger_inp.leverage


# ---- B24.25: a citing `speak` files its items, and an answering one answers them (EVID_B edit 4; gates 1 to 3) ---------------------------------------------------

def _filing_world(seed, arm="case_file"):
    from .test_sc_hearing_admission import hearing
    return hearing(seed, arm)


def test_three_filed_items_give_three_proof_levels_and_no_obstacle_change():
    """EVID_B gate 1, on `build_hearing`: the accuser files two firsthand deed claims and a Record by ONE speech that grades `Success` or better (the seeds whose band does, read off the real fold): three `filed`
    stages; at close the roll's `proofs` levels are three for him and none against, and the obstacle terms equal those with nothing filed (A-25: items are leverage, never an obstacle term); each
    present hearer holds the told copies of the two claims with the accuser on the chain. FALSIFIER: an obstacle that moves with the filing, or two levels for three items."""
    from engine.dice_engine.sigma_leverage import levels_to_net_sigma
    from .test_sc_hearing_admission import DEED, G, OTHER_DEED, cite, fold_and_witness, hearers, records_of
    roll, checked = importlib.import_module("modules.social_contest.roll"), 0
    for seed in range(200):
        w, d, case = _filing_world(seed)
        w.persons[G.ACCUSER].ledger.append(Claim("c_deed2", G.ACCUSER, G.ACCUSED, OTHER_DEED, True, 0, "firsthand", 100, "own"))
        read = lambda: sigma.contest_input(w, [G.ACCUSER, G.ACCUSED], verb="arrest", subject=G.ACCUSED, room=world_q.place_of(w, G.ACCUSER))
        bare = dict(roll.obstacle(read())[1])
        out = fold_and_witness(w, d, cite(w, ("c_deed", "c_deed2", records_of(w, G.ACCUSER)[0])))
        if out[0].degree not in ("Success", "Overwhelming"):
            continue
        inp = read()
        assert len([s for s in w.records[case].stages if s[1] == "filed"]) == 3 and len(inp.exhibits) == 3, seed
        assert roll.proof_levels(inp) == (3, 0) and roll.leverage(inp) == levels_to_net_sigma(["minor"] * 3, []) and dict(roll.obstacle(inp)[1]) == bare, seed
        told = [c for p in hearers(w) for c in w.persons[p].ledger if c.source == "told_by" and c.predicate in (DEED, OTHER_DEED)]
        assert told and all(c.chain[0] == G.ACCUSER for c in told), (seed, told)
        checked += 1
    assert checked >= 20, checked


def _answered(seed, answer_to, planted, held, key="ans0"):
    """The accuser answers a stage the ACCUSED planted (an `against` item: the accused's own `speak` is refused today, so the answering side is the accuser's, which the rule treats alike): `planted` are
    the accused's stages appended before the answer, `held` the claims the accuser holds, `answer_to` the claims cited and the stage places answered. Returns `(world, case, events, items)`."""
    from .test_sc_hearing_admission import G, fold_and_witness
    w, d, case = _filing_world(seed)
    w.records[case].stages.extend(planted)
    w.persons[G.ACCUSER].ledger.extend(held)
    cites, places = answer_to
    ledger = {c.id: c for c in w.persons[G.ACCUSER].ledger}
    act = Act(id=key, actor=G.ACCUSER, verb="speak", payload={"subject": G.ACCUSED, "cites": cites, "answers": places,
                                                              "cited": {i: Said(ledger[i].subject, ledger[i].predicate, ledger[i].value, ledger[i].confidence, ledger[i].chain) for i in cites}})
    out = fold_and_witness(w, d, act)
    return w, case, out, sigma._exhibits_of(w, case)


def test_an_answer_strikes_by_its_band_in_a_share_strictly_between_0_and_1():
    """EVID_B gate 2 and FI_05_B (b), over 200 seeds of the real fold: the accused's filed claim `deed = True` (planted) is answered by the accuser's held `deed = False` (an `answers` act; the answered
    item stands at `Failure`, both halve at `Partial`, it is struck at `Success` and `Overwhelming`). All four bands occur; the struck share is strictly between 0 and 1; the answering speech's own item is
    EXCLUDED at `Failure` by the band that failed it (no exhibit), and the target's `answered_band` is the answering act's own `Event.degree`, read and never regraded. FALSIFIER: an answer that strikes at
    `Failure`, or at no band, or in every run."""
    from .test_sc_hearing_admission import DEED, G
    ev = _ev()
    planted = [(1, "filed", "against", "fact", Said(G.ACCUSED, DEED, True, 100), 1.0, G.ACCUSED, "a0")]
    seen, struck, checked = {}, 0, 0
    for seed in range(200):
        w, case, out, items = _answered(seed, (("c_deny",), (3,)), planted, [Claim("c_deny", G.ACCUSER, G.ACCUSED, DEED, False, 0, "firsthand", 100, "own")])
        band = out[0].degree
        target = items[0]
        assert target.answered_band == band and target.id == f"{case}#3", (seed, band, items)
        held, gone, _faults = ev.standing(tuple(items), (), 2.0)
        weights = {i.id: i.weight for i in held}
        if band == "Failure":
            assert len(items) == 1 and weights == {target.id: 1.0}, (seed, items)                  # the answer's item was excluded, the target stands whole
        elif band == "Partial":
            assert weights[target.id] == 0.5 and gone == (), (seed, weights)                       # both halved
        else:
            assert gone == (target.id,) and target.id not in weights, (seed, band, gone)
        seen[band] = seen.get(band, 0) + 1
        struck += bool(gone)
        checked += 1
    assert checked == 200 and set(seen) == {"Failure", "Partial", "Success", "Overwhelming"} and 0 < struck < 200, (seen, struck)


def test_an_impeachment_strikes_origin_wide_only_at_overwhelming():
    """EVID_B gate 3 and FI_05_B (c): the accused's filed Record (a forgery) counts like any Record until answered (`standing` holds it whole, weight 1); the examiner, holding the finding
    `(record, record.forged, True)`, answers it by an `answers` speech that cites the finding: over 200 seeds all four bands occur, and the Record is struck in a share strictly between 0 and 1 --
    `Failure` it stands and its impeacher bears `failed_impeachment`, `Partial` it is halved, `Success` it alone is struck, `Overwhelming` it and every item of its origin are struck and `forgery_found`
    is recorded against the side that filed it. FALSIFIER: an origin-wide strike at `Success`."""
    from .test_sc_hearing_admission import G, records_of
    ev = _ev()
    seen, struck, checked = {}, 0, 0
    for seed in range(200):
        w0, _d0, _c0 = _filing_world(seed)
        rec = records_of(w0, G.ACCUSED)[0]
        planted = [(1, "filed", "against", "fact", rec, 1.0, "o_forger", "a0"), (1, "filed", "against", "fact", Said(G.ACCUSED, CELL, 3, 100), 1.0, "o_forger", "a0")]
        w, case, out, items = _answered(seed, (("c_found",), (3,)), planted, [Claim("c_found", G.ACCUSER, rec, "record.forged", True, 0, "firsthand", 100, "own")])
        band, record = out[0].degree, items[0]
        assert record.forged_found and record.answered_band == band and not items[1].forged_found, (seed, items)
        before, _g, _f = ev.standing(tuple(replace(i, answered_band=None, forged_found=False) for i in items), (), 2.0)
        assert {i.id: i.weight for i in before if i.side == "against"} == {record.id: 1.0, items[1].id: 1.0}, seed       # a forgery counts, as a true Record does, until it is answered
        held, gone, faults = ev.standing(tuple(items), (record.id,), 2.0)
        if band == "Failure":
            assert gone == () and ("failed_impeachment", "for") in faults, (seed, gone, faults)
        elif band == "Partial":
            assert gone == () and {i.id: i.weight for i in held}[record.id] == 0.5, (seed, gone)
        elif band == "Success":
            assert gone == (record.id,), (seed, gone)                                              # the Record alone
        else:
            assert set(gone) == {record.id, items[1].id} and ("forgery_found", "against") in faults, (seed, gone, faults)
        seen[band] = seen.get(band, 0) + 1
        struck += bool(gone)
        checked += 1
    assert checked == 200 and set(seen) == {"Failure", "Partial", "Success", "Overwhelming"} and 0 < struck < 200, (seen, struck)


def test_a_same_side_contradicting_cite_is_refused_at_filing():
    """EVID_B rule 2's filing refusal: a `speak` whose cite contradicts an item already standing for the citer's OWN side is refused BEFORE THE DRAW -- the row's refusal kind, no band, no stage -- and so is
    one that cites two claims that contradict each other. The same cell with the same value is no contradiction (it is agreement) and files; the other side's contradicting item is an answer, not a refusal.
    FALSIFIER: the refused speech draws a band or writes a stage."""
    from .test_sc_hearing_admission import DEED, G, cite, fold_and_witness
    refusal = _verbs.VERB_TABLE["speak"].emits_on_refusal
    planted = (1, "filed", "for", "fact", Said(G.ACCUSED, DEED, True, 100), 1.0, G.ACCUSER, "a0")
    checked = 0
    for seed in range(20):
        w, d, case = _filing_world(seed)
        w.records[case].stages.append(planted)
        w.persons[G.ACCUSER].ledger.append(Claim("c_no", G.ACCUSER, G.ACCUSED, DEED, False, 0, "firsthand", 100, "own"))
        n = len(w.records[case].stages)
        out = fold_and_witness(w, d, cite(w, ("c_no",)))
        assert tuple(e.kind for e in out) == refusal and out[0].degree is None and len(w.records[case].stages) == n, (seed, out)
        w2, d2, case2 = _filing_world(seed)                                                          # two cites that contradict one another
        w2.persons[G.ACCUSER].ledger.append(Claim("c_no", G.ACCUSER, G.ACCUSED, DEED, False, 0, "firsthand", 100, "own"))
        out2 = fold_and_witness(w2, d2, cite(w2, ("c_deed", "c_no")))
        assert tuple(e.kind for e in out2) == refusal and out2[0].degree is None, (seed, out2)
        w3, d3, case3 = _filing_world(seed)                                                          # the same cell and value agrees: not refused
        w3.records[case3].stages.append(planted)
        out3 = fold_and_witness(w3, d3, cite(w3, ("c_deed",)))
        assert out3[0].degree is not None and out3[0].kind not in refusal, (seed, out3)
        checked += 1
    assert checked == 20
