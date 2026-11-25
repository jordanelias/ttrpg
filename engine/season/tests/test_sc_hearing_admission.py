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


@functools.lru_cache(maxsize=None)
def _filing_run(seed: int) -> dict:
    """ONE FILING SPEECH, `seed`'s: the band drawn, the stages it appended, the told claims each hearer then held about the accused, and what the case file's exhibits are at `case_file` with the levels
    they bring (`roll.proof_levels`) and the obstacle terms the roll then reads."""
    w, d, case = hearing(seed, "case_file")
    before = len(w.records[case].stages)
    rec = records_of(w, G.ACCUSER)[0]
    roll = importlib.import_module("modules.social_contest.roll")
    read = lambda: sigma.contest_input(w, [G.ACCUSER, G.ACCUSED], verb="arrest", subject=G.ACCUSED, room=world_q.place_of(w, G.ACCUSER))
    bare = dict(roll.obstacle(read())[1])                                                      # the obstacle with nothing filed
    out = fold_and_witness(w, d, cite(w, ("c_deed", rec)))
    inp = read()
    told = {p: [c for c in w.persons[p].ledger if c.source == "told_by" and c.subject == G.ACCUSED and c.predicate == DEED] for p in hearers(w)}
    return dict(band=out[0].degree, kind=out[0].kind, changes=out[0].changes, stages=tuple(w.records[case].stages[before:]), derived=derived(w), rec=rec,
                exhibits=inp.exhibits, levels=composition.require(sigma.PROOF_LEVELS_ROLE)(inp), terms=dict(roll.obstacle(inp)[1]), bare=bare, told=told, proofs=inp.proofs)


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
    case file's, to the term (A-25: standing items are leverage, never an obstacle term). FALSIFIER: an `excluded` stage counted as an exhibit gives `Failure` the levels of `Success`."""
    levels, checked = {}, 0
    for seed in range(SEEDS):
        r = _filing_run(seed)
        levels.setdefault(r["band"], set()).add(r["levels"])
        if r["band"] == "Failure":
            assert r["exhibits"] == () and r["levels"] == (0, 0) and r["proofs"] == 0.0, (seed, r["exhibits"])
        else:
            assert len(r["exhibits"]) == 2, seed
        assert r["terms"] == r["bare"], (seed, r["band"])
        checked += 1
    assert checked == SEEDS and levels == {"Failure": {(0, 0)}, "Partial": {(1, 0)}, "Success": {(2, 0)}, "Overwhelming": {(2, 0)}}, levels


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
