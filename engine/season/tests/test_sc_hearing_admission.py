"""B24.25 -- a citing `speak` files its items by its OWN band (ADM "The resolution, decided", EVID_B edit 4).

The world is `governance_spine.build_hearing(seed)` -- a sitting due, a case file the docket item names, an accuser holding three Records -- and the act is the accuser's own `speak` on his accused's matter,
citing one held deed claim and one held Record, folded through the real fold (`_fold`: RESOLVE then ENCOUNTER) and witnessed. Each seed draws its own band. `_filing_run` is the one fold the tests read, so
a table the fold wrote is read by every assertion.

    Failure        `(tick, "excluded", side, ref, act)` for each item: no exhibit, no `proofs` level -- and the room still heard it said
    Partial        `(tick, "filed", side, rung, ref, weight x 1/2, origin, act)`
    Success        `filed` at the derived weight
    Overwhelming   `filed` at the derived weight, a ninth cell `True`: first heard

A game-state test in the `sc_season` lane: each observes what a real fold of a real `speak` wrote on the case file and what the case file's exhibits then bring to a roll.
"""
from __future__ import annotations

import functools
import importlib

import pytest

from engine.substrate import composition

from ..data import verbs as _verbs
from ..data.matrix import WriteClass
from ..harness import governance_spine as G
from ..loop.driver import SeasonDriver, mint_token
from ..queries import person_q, world_q
from ..queries.inputs import FILED_CELLS, FIRST_CELLS, is_filed, is_first
from ..seam.wrappers import sigma
from ..state.carriers import Act, Claim, Said
from .test_u7_remit import _fold

BANDS = ("Failure", "Partial", "Success", "Overwhelming")
SEEDS = 200
DEED = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)[0]            # a deed kind that is no pairing: a plain firsthand claim of a doing
OTHER_DEED = sorted(_verbs.DEED_KINDS - person_q.PAIRED_KINDS)[1]


def hearing(seed: int, arm: str = "ledger"):
    """`(world, driver, case file id)` of `build_hearing(seed)` at the `evidence_from` arm: the accuser holds the deed claim `c_deed` and three Records, and the accused's matter is docketed on a case file."""
    w = G.build_hearing(seed)
    w.fixtures = w.fixtures.sweep("evidence_from", arm)
    w.persons[G.ACCUSER].ledger.append(Claim("c_deed", G.ACCUSER, G.ACCUSED, DEED, True, 0, "firsthand", 100, "own"))
    return w, SeasonDriver(w), world_q.case_file_of(w, world_q.docketed(w, G.ACCUSED)[0])


def records_of(w, who: str) -> list:
    return [t.object for t in w.persons[who].tenures if t.kind == "hold" and t.live and t.object in w.records]


def cite(w, ids: tuple, key: str = "sp0", **extra) -> Act:
    """The accuser's `speak` on the accused's matter citing `ids`, each claim with the `Said` CHOOSE would have copied from his own ledger."""
    ledger = {c.id: c for c in w.persons[G.ACCUSER].ledger}
    said = {i: Said(c.subject, c.predicate, c.value, c.confidence, c.chain) for i, c in ledger.items() if i in ids}
    return Act(id=key, actor=G.ACCUSER, verb="speak", payload={"subject": G.ACCUSED, "cites": tuple(ids), "cited": said, **extra})


def fold_and_witness(w, d, act) -> list:
    """The act folded, its Events logged (`_fold`) and WITNESSED, as the loop does: what the room came to hold is in the ledgers after it."""
    out = _fold(w, d, act)
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return out


def hearers(w) -> list:
    """The people in the accuser's room but him: who heard the speech."""
    room = world_q.place_of(w, G.ACCUSER)
    return [p for p in w.persons if p != G.ACCUSER and world_q.place_of(w, p) == room]


def derived(w) -> tuple:
    """What `c_deed` and the first Record weigh BEFORE the band's share: the citer's own ledger's weight of the claim (`teller_weight`, `person_q.proof_weight` 1), and a Record's 1."""
    claim = next(c for c in w.persons[G.ACCUSER].ledger if c.id == "c_deed")
    return person_q.teller_weight(w.persons[G.ACCUSER], w.fixtures, w.tick)(claim) * float(person_q.proof_weight(claim)), 1.0


def _close_read(w) -> tuple:
    """`(lever, terms)` OF THE MATTER'S OWN CLOSE (B24's close, R1): the accuser's `determine` of the accused as the host builds it (`proceeding_input` on the docket's row), the board's leverage on
    its opening sitting (`proceeding._lever`: here the filed exhibits alone) and the obstacle terms of the presiding seat's draw at that leverage (`close_record`)."""
    P = importlib.import_module("modules.social_contest.proceeding")
    act = Act(id="t:close", actor=G.ACCUSER, verb="determine", via=G.ACCUSER_SEAT, payload={"subject": G.ACCUSED})
    row, form, _m, _i = world_q.proceeding_row(w, act)
    inp, _card = sigma.proceeding_input(w, [G.ACCUSER, G.ACCUSED], verb="determine", subject=G.ACCUSED, topic=G.ACCUSED, effort=0, row=row, form=form)
    lever = P._lever(inp, P.start(inp))
    return lever, dict(P.obstacle(P.close_record(inp, 0.0, lever)[1])[1])


@functools.lru_cache(maxsize=None)
def _filing_run(seed: int) -> dict:
    """ONE FILING SPEECH, `seed`'s: the band drawn, the stages it appended, the told claims each hearer then held about the accused, and what the case file's exhibits are at `case_file` with the levels
    they bring to the single roll (`roll.proof_levels`) and the obstacle terms it then reads, and the leverage they bring to the matter's own close (`_close_read`) with that close's terms."""
    w, d, case = hearing(seed, "case_file")
    before = len(w.records[case].stages)
    rec = records_of(w, G.ACCUSER)[0]
    roll = importlib.import_module("modules.social_contest.roll")
    read = lambda: sigma.contest_input(w, [G.ACCUSER, G.ACCUSED], verb="arrest", subject=G.ACCUSED, room=world_q.place_of(w, G.ACCUSER))
    bare = dict(roll.obstacle(read())[1])                                                      # the obstacle with nothing filed
    close_bare = _close_read(w)
    out = fold_and_witness(w, d, cite(w, ("c_deed", rec)))
    inp = read()
    told = {p: [c for c in w.persons[p].ledger if c.source == "told_by" and c.subject == G.ACCUSED and c.predicate == DEED] for p in hearers(w)}
    return dict(band=out[0].degree, kind=out[0].kind, changes=out[0].changes, stages=tuple(w.records[case].stages[before:]), derived=derived(w), rec=rec,
                exhibits=inp.exhibits, levels=composition.require(sigma.PROOF_LEVELS_ROLE)(inp), terms=dict(roll.obstacle(inp)[1]), bare=bare, told=told, proofs=inp.proofs,
                close=_close_read(w), close_bare=close_bare)


def test_admission_follows_the_citing_band_over_200_seeds():
    """ADM's table, read off the case file after 200 real filing speeches (each seed its own draw): all four bands occur; per band the new stages are exactly the table's -- `excluded` at `Failure` and only
    there (no `filed`), the weight halved at `Partial` and only there, the first-heard cell at `Overwhelming` and only there -- and each stage names the speaker's side, the item and the act.
    FALSIFIER: a dispatch that files at every band, or that halves nothing, or that marks `first` at `Success`, reddens a row."""
    seen, checked = {}, 0
    for seed in range(SEEDS):
        r = _filing_run(seed)
        band, stages = r["band"], r["stages"]
        claim_w, rec_w = r["derived"]
        assert band in BANDS and len(stages) == 2, (seed, band, stages)
        seen[band] = seen.get(band, 0) + 1
        for st, ref, base in zip(stages, (Said(G.ACCUSED, DEED, True, 100), r["rec"]), (claim_w, rec_w)):
            assert st[0] == 1 and st[2] == "for", (seed, st)                                           # the tick and the speaker's side
            if band == "Failure":
                assert st[1] == "excluded" and len(st) == 5 and st[3] == ref and st[4] == "sp0" and not is_filed(st), (seed, st)
                continue
            assert is_filed(st) and st[1] == "filed" and st[3] == "fact" and st[4] == ref and st[7] == "sp0", (seed, st)
            assert st[5] == (base * 0.5 if band == "Partial" else base), (seed, band, st)             # the half is read for Partial, nowhere else
            assert len(st) == (FIRST_CELLS if band == "Overwhelming" else FILED_CELLS) and is_first(st) == (band == "Overwhelming"), (seed, band, st)
        checked += 1
    assert checked == SEEDS and set(seen) == set(BANDS), seen


def test_excluded_items_add_no_proofs_level():
    """ADM's falsifier: an excluded item changes nothing the roll reads. At `case_file` the exhibits of the matter after a `Failure` filing are NONE and the `proofs` levels (0, 0), the speaker's own ledger
    read for the matter by nothing (`proofs` 0.0); the same filing at `Partial` brings ONE level (half of 1.95) and at `Success` and `Overwhelming` TWO; and at every band the obstacle terms are the empty
    case file's, to the term (A-25: standing items are leverage, never an obstacle term). THE MATTER'S OWN CLOSE reads the same (B24's close, R1: `determine` proceeds, so it reads the file itself):
    its board leverage before the filing is 0.0 and after it is the same count of `proof_level` levels (none at `Failure`), its terms the empty file's.
    FALSIFIER: an `excluded` stage counted as an exhibit gives `Failure` the levels of `Success`; a close that reads no exhibit stays at 0.0 after every band."""
    from engine.dice_engine.sigma_leverage import levels_to_net_sigma
    levels, closes, checked = {}, {}, 0
    for seed in range(SEEDS):
        r = _filing_run(seed)
        levels.setdefault(r["band"], set()).add(r["levels"])
        closes.setdefault(r["band"], set()).add(r["close"][0])
        if r["band"] == "Failure":
            assert r["exhibits"] == () and r["levels"] == (0, 0) and r["proofs"] == 0.0, (seed, r["exhibits"])
        else:
            assert len(r["exhibits"]) == 2, seed
        assert r["terms"] == r["bare"], (seed, r["band"])
        assert r["close_bare"][0] == 0.0 and r["close"][1] == r["close_bare"][1], (seed, r["band"], r["close"], r["close_bare"])
        checked += 1
    assert checked == SEEDS and levels == {"Failure": {(0, 0)}, "Partial": {(1, 0)}, "Success": {(2, 0)}, "Overwhelming": {(2, 0)}}, levels
    lv = lambda n: levels_to_net_sigma(["minor"] * n, [])
    assert closes == {"Failure": {lv(0)}, "Partial": {lv(1)}, "Success": {lv(2)}, "Overwhelming": {lv(2)}}, closes


def test_partial_enters_at_half_weight():
    """ADM's second falsifier: if `Partial` and `Success` gave the same `proofs`, the half-weight cell is not read. The exhibits' total weight at `Partial` is half the derived weight of the two items
    (0.975 where `Success` brings 1.95), and the levels they bring differ (1 against 2)."""
    totals = {}
    for seed in range(SEEDS):
        r = _filing_run(seed)
        totals.setdefault(r["band"], set()).add(round(sum(i.weight for i in r["exhibits"]), 6))
    full = round(sum(_filing_run(0)["derived"]), 6)
    assert totals["Partial"] == {round(full / 2, 6)} and totals["Success"] == totals["Overwhelming"] == {full} and totals["Failure"] == {0}, totals


def test_failure_still_deposits_the_told_copy():
    """ADM's third falsifier: the room heard it said even though the bench did not take it. At `Failure` the stages are `excluded`, and still a present hearer holds the told copy of the cited claim with the
    citer at the head of its chain (E-3: the told deposit fires at every band the told channel deposits at, whether or not the item was entered). FALSIFIER: no `Failure` run carries a told copy -- the
    deposit has been tied to admission."""
    deposited = {b: 0 for b in BANDS}
    for seed in range(SEEDS):
        r = _filing_run(seed)
        copies = [c for cs in r["told"].values() for c in cs]
        assert all(c.chain and c.chain[0] == G.ACCUSER for c in copies), (seed, copies)
        deposited[r["band"]] += bool(copies)
        if r["band"] == "Failure":
            assert all(st[1] == "excluded" for st in r["stages"]), seed
    assert deposited["Failure"] > 0 and all(deposited[b] > 0 for b in BANDS), deposited


def test_a_speak_citing_nothing_files_nothing():
    """The control (ADM, EVID_B gate 5), observed on the fold itself: a `speak` that cites nothing -- every computed one until B24.27 -- writes nothing on the case file and its Event carries no change, as it
    did when `speak.writes` was `[]`; it is answered by the band's OWN kind (not refused, `rosters.yaml: write_optional`), whichever band it drew. The realm's content hash at seeds 0 to 2 reads equal to B24.24's."""
    emits, seen, checked = _verbs.VERB_TABLE["speak"].emits_by_degree, set(), 0
    for seed in range(60):
        w, d, case = hearing(seed)
        before = list(w.records[case].stages)
        out = fold_and_witness(w, d, Act(id="sp0", actor=G.ACCUSER, verb="speak", payload={"subject": G.ACCUSED}))
        assert len(out) == 1 and out[0].kind == emits[out[0].degree][0] and not out[0].changes, (seed, [(e.kind, e.degree, e.changes) for e in out])
        assert list(w.records[case].stages) == before
        seen.add(out[0].degree)
        checked += 1
    assert checked == 60 and seen == set(BANDS)


# ---- B24.26: an answer to an item first heard faces `first_heard_ob` more (ADM edit 4; OBS §2 member 11) ------------------------------------------------------

def _sitting_terms(first_heard_ob: float) -> dict:
    """The `Margin.terms` of each move a sitting draws on the board, `{label: dict(terms)}`: the accuser's `i1` (heard first) and `i2` (not) are answered by the accused, `i1` is impugned, and the accuser
    answers the accused's `j1` and argues a point, at `first_heard_ob` as given."""
    from ..data.arrangements import GROUNDS
    from ..queries.inputs import Choice, Item
    from .test_sc_proceeding_module import P, _dials, _inp, _key, _p, _rite, _sit
    ground = next(g for g, r in GROUNDS.items() if r["reads"] != "item")
    cell = lambda n, v: (f"s{n}", "stores.level", v)
    i1 = Item("i1", "record", 1.0, origin="o1", cell=cell(1, 3), pairs=(("j1", "contradicts"),), first=True)
    i2 = Item("i2", "record", 1.0, origin="o2", cell=cell(2, 3), pairs=(("j2", "contradicts"),))
    j1 = Item("j1", "record", 1.0, origin="o3", cell=cell(1, 4), pairs=(("i1", "contradicts"),))
    j2 = Item("j2", "record", 1.0, origin="o4", cell=cell(2, 4), pairs=(("i2", "contradicts"),))
    a, b = _p("a", "for", items=(i1, i2)), _p("b", "against", items=(j1, j2))
    inp = _inp([a, b, _p("j0", decides=True, precedence=1)], _rite(close="bench", turns=8, admits=("record",)), dials=_dials(first_heard_ob=first_heard_ob))
    st = _sit(inp)
    for k, (who, item) in enumerate(((a, "i1"), (a, "i2"), (b, "j1"), (b, "j2"))):
        st, _ = P.exchange(inp, st, who, Choice("present", None, item), _key("fh", k))
    moves = {"answer_first": (b, Choice("answer", ground, "i1")), "answer_plain": (b, Choice("answer", ground, "i2")), "impugn_first": (b, Choice("impugn", ground, "i1")),
             "answer_by_first_side": (a, Choice("answer", ground, "j1")), "argue": (a, Choice("argue", ground, None, "raises"))}
    return {label: dict(P.exchange(inp, st, who, ch, _key("fh", 9))[1].terms) for label, (who, ch) in moves.items()}


def test_first_heard_adds_the_term_to_the_answer_only():
    """ADM edit 4, both halves, on the real draw. INSIDE A SITTING: with `first_heard_ob` 2, the move that answers the item entered first (`Item.first`) names a `first_heard` term of exactly 2.0 in
    its obstacle, and no other roll does -- not an answer to an item not heard first, not an impugnment of the first-heard one, not the first side's answer to the other's item, not an argument; at the
    control (0) no roll names it. OUT OF A SITTING, over seeds: the accuser's `speak` that answers a `filed` stage with the first-heard mark is handed `first_heard` and its proceeding's roll names the term (2.0);
    the same speak answering a stage without the mark, and a speak that files a claim of its own against a standing first-marked stage and answers nothing, do not, and at 0 it is handed True and names nothing (hash equal at the control).
    FALSIFIER: the term on any roll but the answer to a first-heard item, or an answer to one that does not name it."""
    plain = _sitting_terms(2.0)
    assert plain["answer_first"].get("first_heard") == 2.0, plain["answer_first"]
    assert [m for m, t in plain.items() if "first_heard" in t] == ["answer_first"], plain
    control = _sitting_terms(0.0)
    assert not [m for m, t in control.items() if "first_heard" in t] and set(control["answer_first"]) == set(plain["answer_first"]) - {"first_heard"}, control      # the control lists nothing
    seen, checked = [], 0
    real = sigma._resolve_proceeding

    def spy(*a, **k):
        out = real(*a, **k)
        seen.append((k.get("first_heard"), dict(out.get("terms") or ())))
        return out

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(sigma, "_resolve_proceeding", spy)
        for seed in range(8):
            for ob, plant_first, answers in ((2.0, True, True), (2.0, False, True), (2.0, True, False), (0.0, True, True)):
                w, d, case = hearing(seed)
                w.fixtures = w.fixtures.sweep("first_heard_ob", ob)
                w.records[case].stages.append((1, "filed", "against", "fact", Said(G.ACCUSED, DEED, True, 100), 1.0, G.ACCUSED, "a0", *((True,) if plant_first else ())))
                w.persons[G.ACCUSER].ledger.append(Claim("c_deny", G.ACCUSER, G.ACCUSED, DEED, False, 0, "firsthand", 100, "own"))
                payload = {"subject": G.ACCUSED, "cites": ("c_deny",), "cited": {"c_deny": Said(G.ACCUSED, DEED, False, 100)}}
                if answers:
                    payload["answers"] = (len(w.records[case].stages) - 1,)
                else:                                                                                           # a plain filing of his own deed claim, with the first-marked stage standing against him
                    payload.update(cites=("c_deed",), cited={"c_deed": Said(G.ACCUSED, DEED, True, 100)})
                before = len(seen)
                out = fold_and_witness(w, d, Act(id="ans0", actor=G.ACCUSER, verb="speak", payload=payload))
                assert len(seen) == before + 1 and out, (seed, ob, plant_first, answers)
                handed, terms = seen[-1]
                assert handed is (plant_first and answers), (seed, ob, plant_first, answers, handed)          # the host's read of the stage's mark, and of whether the act answers it
                assert ("first_heard" in terms) is (plant_first and answers and ob > 0) and terms.get("first_heard", 2.0) == 2.0, (seed, ob, plant_first, answers, terms)
                checked += 1
    assert checked == 32 and any("first_heard" in t for _, t in seen) and any(h and "first_heard" not in t for h, t in seen)


# ---- B24.43: an answering `speak` is priced as the sitting's `answer` is (EVID_B "The answer's odds") -----------------------------------------------------------

def test_an_answering_speak_meets_answer_ob():
    """B24.43 step 2, on the real fold, 8 seeds x 3 acts, at `answer_step` 0.25. The accuser's `speak` that ANSWERS a filed stage of the accused's (weight 3.0, answered by his held claim of the same cell) is handed
    the weight the stage holds over the answer (`world_q.answered_over`: 3.0 less the answer's own derived weight) and its roll's obstacle names `difficulty` at `answer_ob` (not the row's) and `answer` at
    `answer_step` x that weight; one that answers a stage the answer outweighs (0.5) is at `answer_ob` and names no `answer` term (nothing is owed over it); a plain citing speak of his own is handed `None`,
    keeps the row's difficulty and names no `answer`. FALSIFIER: an answering speak priced at the row's difficulty, or one that names no `answer` term over a heavier answered item, or a plain speak that names it."""
    seen, checked = [], 0
    real = sigma._resolve_proceeding

    def spy(*a, **k):
        out = real(*a, **k)
        seen.append((k.get("answered_over"), dict(out.get("terms") or ())))
        return out

    with pytest.MonkeyPatch.context() as mp:
        mp.setattr(sigma, "_resolve_proceeding", spy)
        for seed in range(8):
            for planted, kind in ((3.0, "answers"), (0.5, "answers"), (3.0, "plain")):
                w, d, case = hearing(seed)
                w.fixtures = w.fixtures.sweep("answer_step", 0.25)
                answer_ob, row_ob = w.fixtures.get("answer_ob"), sigma._difficulty_term(w.fixtures, {"verb": "speak"})["difficulty"]
                assert answer_ob != row_ob                                                                     # the two prices differ, so the one named is observable
                w.records[case].stages.append((1, "filed", "against", "fact", Said(G.ACCUSED, DEED, True, 100), planted, G.ACCUSED, "a0"))
                acc = w.persons[G.ACCUSER]
                acc.ledger.append(Claim("c_deny", G.ACCUSER, G.ACCUSED, DEED, False, 0, "firsthand", 100, "own"))
                payload = {"subject": G.ACCUSED, "cites": ("c_deny",), "cited": {"c_deny": Said(G.ACCUSED, DEED, False, 100)}}
                if kind == "answers":
                    payload["answers"] = (len(w.records[case].stages) - 1,)
                else:
                    payload.update(cites=("c_deed",), cited={"c_deed": Said(G.ACCUSED, DEED, True, 100)})
                deny = next(c for c in acc.ledger if c.id == "c_deny")
                assert person_q.proof_kind(person_q.cited_said(deny)) is None                                    # a denial is no deed: it files as testimony, at the weight his ledger gives the claim (`filings`)
                answer_w = person_q.teller_weight(acc, w.fixtures, w.tick)(deny)
                before = len(seen)
                out = fold_and_witness(w, d, Act(id="ans43", actor=G.ACCUSER, verb="speak", payload=payload))
                assert len(seen) == before + 1 and out, (seed, planted, kind)
                over, terms = seen[-1]
                if kind == "plain":
                    assert over is None and terms["difficulty"] == row_ob and "answer" not in terms, (seed, over, terms)
                else:
                    expect = max(0.0, planted - answer_w)
                    assert over == expect and terms["difficulty"] == answer_ob, (seed, planted, over, expect, terms)
                    assert (terms.get("answer") == 0.25 * expect) if expect else ("answer" not in terms), (seed, planted, terms)
                checked += 1
    assert checked == 24 and any("answer" in t for _, t in seen) and any(o == 0.0 for o, _ in seen), (checked, seen[:3])
