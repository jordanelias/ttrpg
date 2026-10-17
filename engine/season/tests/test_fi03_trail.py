"""v9 FI-03 (`ED-FI-0002`), with FI-02 (`SM-3`): THE TRAIL IS FOUND AND DEPOSITED -- design steps 1 and 2.

A covert act (`forge`) leaves its Event in the log; only the people a witness channel admits learn of it.
A graded inquiry that reaches a finding band asks the `inquiry` role what its Event uncovers
(`seam/contest.py::find_trail`, from `loop/resolve.py`'s per-act bookkeeping); the fieldwork module
(`modules/fieldwork/find.py`) decides how much, by band (`rosters.yaml: finding_terms`); WITNESS gives the
finder what a witness of the act would have held, masked to those terms (`loop/witness.py::_found_claims`).

THE WORLD (`trail_world`, shared with the step-3 EXIT tests): `tiny_world` with the Crown planted (its
Proposition and two members' `commit` edges, `test_information_cluster.py::_world`'s shape). Every act is
RESOLVED through `SeasonDriver.resolve` and WITNESSED through `SeasonDriver.witness`, and every one of
them is chooser-reachable or a precondition the fold checks -- nothing is planted into a ledger but the
forger's own hearing of his subject (the `own_ledger` cell `forge` asks, `_hear`'s precedent):
  tick 0 -- the FORGER (`p_other`, in `Hh`) forges a sheet on `p_mid`: `record.forged`. The INVESTIGATOR
            (`p_high`, in `S`) is admitted by no channel -- asserted, not assumed;
  tick 1 -- the forger `move`s to `S` and `give`s the Record to the investigator (`give` is typed
            `with`: the receiver must stand where the giver does, so the move is what makes the plant
            honest). THE TRAIL IS REACHABLE BY A `research` ONLY THROUGH THIS PLANT: the Record is
            minted into the forger's own hand; the seed-0 realm plants none (`record.given` 0);
  tick 2 -- the investigator's `research` on the Record, which the REAL CHOOSER PATH forms for him
            (`world_q.questions_for` -> `decision/options.py::opening_set`), resolved through
            `resolve()`. The act id is the one thing searched: a bounded, recorded sweep for the band a
            test needs, asserted so no test passes on the wrong band.
The ticks are advanced by hand between the stages so each stage's claims are told apart by `when`
(`questions_for`'s default `since`), which the step-3 contrast reads.

THE BANDS ARE READ OFF THE DATA, NEVER SPELT: a band whose `finding_terms` row shows `HAND_TERM` is a
"hand" band, one whose row shows terms but not it a "blind" band.

RED WHEN PLANTED (each run 2026-10-17 on the build tree, then restored): the hand mask in
`_found_claims` dropped (`HAND_TERM in terms or s != hand` -> `True`) -- `test_a_blind_band_...` goes RED;
`holds_trail`'s re-check in `_found_claims` dropped -- `test_two_finds_of_one_trail_in_one_round_...`
goes RED; `holds_trail` made to compare `when` with `emitted_at` (the design's first exclusion) --
`test_a_second_research_of_the_same_record_deposits_nothing` and the one-round test go RED.
"""
from __future__ import annotations

import dataclasses

import pytest

from ..data.matrix import Step, WriteClass
from ..data.rosters import FINDING_TERMS, faction_prop_id
from ..decision.choose import _payload_of
from ..decision.options import opening_set
from ..epistemic import SEEN_PREDICATE, trail_of
from ..gaps import Unspecified
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..loop.witness import HAND_TERM
from ..manifest import MODULE_ENTRIES, resolve as manifest_resolve
from ..queries import world_q
from ..queries.inputs import Findings
from ..seam import find_trail
from ..state.carriers import Act, Claim, Event, Proposition, Tenure, View

FAC = faction_prop_id("Crown")
FORGER, INVESTIGATOR, ABOUT = "p_other", "p_high", "p_mid"
FORGE_ID = "fi03_forge"
HAND_BANDS = frozenset(b for b, t in FINDING_TERMS.items() if HAND_TERM in t)
BLIND_BANDS = frozenset(b for b, t in FINDING_TERMS.items() if t and HAND_TERM not in t)
# [JUSTIFIED: a test-fixture search bound, not a game value -- the act ids tried for a band; asserted reached]
SWEEP = 60


def step(w, d, *acts):
    """RESOLVE then WITNESS one round of `acts` through the driver; the Events reach `w.log` between the
    two, as `SeasonDriver.season` puts them there. Returns the Events."""
    w.step = Step.RESOLVE
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), out)
    return out


def trail_world():
    """THE WORLD, built through the fold to the moment the investigator holds the forged Record (tick 2).
    Returns `(w, d, rid)`."""
    w = P.tiny_world()
    w.propositions[FAC] = Proposition(FAC, "HOLDS", "Crown", "is a faction of this world", True, 0)
    for pid in (INVESTIGATOR, ABOUT):
        w.add_tenure(Tenure(f"t_commit_{pid}", pid, FAC, "commit", since=0))
    d = SeasonDriver(w)
    forger = w.persons[FORGER]
    forger.ledger.append(Claim(f"c_{FORGER}_{ABOUT}", FORGER, ABOUT, "exists:Person", 1, w.tick,
                               "firsthand", 1, "own"))
    out = step(w, d, Act(id=FORGE_ID, actor=FORGER, verb="forge", payload={"subject": ABOUT}))
    assert [e.kind for e in out] == ["record.forged"], [e.kind for e in out]
    (rid,) = [c.subject for c in out[0].changes]
    w.tick += 1
    assert [e.kind for e in step(w, d, Act(id="fi03_move", actor=FORGER, verb="move",
                                           payload={"to": "S"}))] == ["travel.moved"]
    assert [e.kind for e in step(w, d, Act(id="fi03_give", actor=FORGER, verb="give",
                                           payload={"subject": rid, "to": INVESTIGATOR}))] == [
        "record.given"]
    assert world_q.hold_force(w, rid).subject == INVESTIGATOR
    w.tick += 1
    return w, d, rid


def forged_event(w):
    return next(e for e in w.log if e.kind == "record.forged")


def chooser_research(w, rid):
    """The `research` Candidate the real chooser path forms for the investigator on the Record -- the
    questions `questions_for` raises for him and the candidates `opening_set` forms on each. Refuses to
    return anything it did not find there."""
    p = w.persons[INVESTIGATOR]
    view = View(INVESTIGATOR, [], w.fixtures.get("view_k"))
    for q in world_q.questions_for(w, p):
        for c in opening_set(p, view, q, w.fixtures):
            if c.verb == "research" and c.subject == rid:
                return c
    return None


def research(n, cand):
    """The investigator's act from the chooser's Candidate -- its verb and payload (`_payload_of`, the
    chooser's own), with the searched id."""
    return Act(id=f"fi03_research_{n}", actor=INVESTIGATOR, verb=cand.verb, payload=_payload_of(cand))


def find_band(bands, *, skip=()):
    """`(n, w, d, rid, events)` for the first act id in `SWEEP` whose research draws a band in `bands`."""
    for n in range(SWEEP):
        if n in skip:
            continue
        w, d, rid = trail_world()
        cand = chooser_research(w, rid)
        w.step = Step.RESOLVE
        out = d.resolve(mint_token(w, WriteClass.ACTS), [research(n, cand)],
                        contest_max_depth=w.fixtures.get("contest_max_depth"))
        if out and out[0].degree in bands:
            return n, cand
    raise AssertionError(f"{SWEEP} act ids drew no band in {sorted(bands)}")


def found_deposits(w, finding_id):
    """Every `claim.deposited` the found deposit made for `finding_id`: caused by it AND by a trail Event."""
    return [e for e in w.log if e.kind == "claim.deposited" and len(e.causes) == 2
            and e.causes[0] == finding_id]


def forged_claims(w, pid):
    return [c for c in w.persons[pid].ledger if c.predicate == "record.forged"]


def found_seen(w, pid, rid):
    return [c for c in w.persons[pid].ledger
            if c.predicate == SEEN_PREDICATE and c.subject == rid and c.source == "inferred"]


# ======================================================================================
# 0 -- THE WORLD IS HONEST: no channel admits the investigator; the chooser forms the inquiry
# ======================================================================================

def test_the_investigator_witnessed_nothing_of_the_forgery_and_the_chooser_forms_his_research():
    """The two premises every test below rests on, each observed. (a) The forging reached the forger's
    co-located neighbour (`p_mid`, a `firsthand` anchor claim on the forger -- so the channel fan RAN and
    the investigator's absence is not a fan that admits nobody) and not the investigator, who holds no
    `record.forged` claim and no claim caused by the forging. (b) The investigator holds the Record, and
    `questions_for` -> `opening_set` forms his `research` on it: the inquiry is the chooser's, not hand-
    injected. (c) Before any inquiry the trail is there to be found: `trail_of` returns the forging."""
    w, d, rid = trail_world()
    f = forged_event(w)
    assert any(c.subject == FORGER and c.source == "firsthand" for c in forged_claims(w, ABOUT)), (
        "the forging reached no witness, so the investigator's absence below would be vacuous")
    assert forged_claims(w, INVESTIGATOR) == [], forged_claims(w, INVESTIGATOR)
    # The forging was the only act of its tick, so any claim he holds stamped then came from it.
    assert not [c for c in w.persons[INVESTIGATOR].ledger if c.when == f.emitted_at], (
        "the investigator holds a claim from the forging's tick")
    cand = chooser_research(w, rid)
    assert cand is not None, "the chooser forms no `research` on the planted Record"
    assert [e.id for e in trail_of(w, rid, INVESTIGATOR)] == [f.id]
    assert trail_of(w, rid, FORGER) == [], "a man's own act is not trail to him"


# ======================================================================================
# 1 -- A HAND BAND: the finder holds what a witness would have, from the `inferred` slot
# ======================================================================================

def test_a_hand_band_deposits_the_forgers_deed_and_the_control_deposits_nothing(monkeypatch):
    """A `research` drawing a hand band, resolved through `resolve()` and witnessed: the investigator now
    holds `(forger, record.forged, True)` and `(Record, record.forged, True)`, source `inferred`, not the
    doer; and a `seen` claim on the Record whose `who` is the forger. Each deposit's `claim.deposited`
    names the finding AND the forging -- the walk runs claim -> finding -> covert act.
    CONTROL, SAME SEED, SAME ACT, SAME ROLL: `finding_terms` emptied -- the band is drawn identically and
    the finding is deposited as before, and nothing of the trail lands."""
    n, cand = find_band(HAND_BANDS)
    w, d, rid = trail_world()
    out = step(w, d, research(n, cand))
    (finding,) = out
    assert finding.kind == "finding.made" and finding.degree in HAND_BANDS, (finding.kind, finding.degree)
    f = forged_event(w)
    held = {(c.subject, c.source, c.doer, c.value) for c in forged_claims(w, INVESTIGATOR)}
    assert held == {(FORGER, "inferred", None, True), (rid, "inferred", None, True)}, held
    (seen,) = found_seen(w, INVESTIGATOR, rid)
    assert seen.value.who == FORGER, seen.value
    deposits = found_deposits(w, finding.id)
    assert len(deposits) == 3 and all(e.causes == [finding.id, f.id] for e in deposits), deposits
    assert d.findings == {}, "WITNESS left a find on the driver"

    for band in list(FINDING_TERMS):
        monkeypatch.delitem(FINDING_TERMS, band)
    w, d, rid = trail_world()
    (finding2,) = step(w, d, research(n, cand))
    assert (finding2.kind, finding2.degree, finding2.id) == (finding.kind, finding.degree, finding.id)
    assert forged_claims(w, INVESTIGATOR) == [] and found_seen(w, INVESTIGATOR, rid) == []
    assert found_deposits(w, finding2.id) == []


# ======================================================================================
# 2 -- A BLIND BAND: the thing, not the hand
# ======================================================================================

def test_a_blind_band_lands_the_claim_on_the_record_and_withholds_the_hand():
    """A band whose `finding_terms` row does not show `HAND_TERM`: the claim on the Record lands, none
    anchored on the forger does, and the `seen` claim's `who` is `None` -- an inference is less than a
    sight (`rosters.yaml: finding_terms`' note). A witness's anchor claim is not so masked, by design."""
    if not BLIND_BANDS:
        pytest.skip("finding_terms shows the hand at every band -- the ruled revert; nothing to withhold")
    n, cand = find_band(BLIND_BANDS)
    w, d, rid = trail_world()
    (finding,) = step(w, d, research(n, cand))
    assert finding.degree in BLIND_BANDS, finding.degree
    held = {c.subject for c in forged_claims(w, INVESTIGATOR)}
    assert held == {rid}, held
    (seen,) = found_seen(w, INVESTIGATOR, rid)
    assert getattr(seen.value, HAND_TERM) is None, seen.value
    assert seen.value.stratum is not None, "the blind band showed nothing at all -- the mask is wrong"


# ======================================================================================
# 3 -- WHAT HE ALREADY HOLDS IS NOT NEWS (R5: any subject, whatever its `when`)
# ======================================================================================

def test_a_second_research_of_the_same_record_deposits_nothing():
    """After a hand-band find, a second `research` of the same Record, a tick later, at a finding band:
    its finding deposits nothing of the trail -- the investigator already holds `(s, record.forged, True)`
    for a subject the deposit is about, and `when` is not compared (his claim is stamped at the find, two
    ticks after the forging, so the design's `when == emitted_at` exclusion would have re-deposited)."""
    n, cand = find_band(HAND_BANDS)
    w, d, rid = trail_world()
    step(w, d, research(n, cand))
    before = len(forged_claims(w, INVESTIGATOR))
    assert before == 2, before
    assert trail_of(w, rid, INVESTIGATOR) == [], "the trail is still news after it was found"
    w.tick += 1
    for m in range(SWEEP):
        out = step(w, d, research(f"again_{m}", cand))
        if out[0].degree in FINDING_TERMS:
            break
    else:
        raise AssertionError("no second research drew a finding band")
    assert found_deposits(w, out[0].id) == [], found_deposits(w, out[0].id)
    assert len(forged_claims(w, INVESTIGATOR)) == before


def test_two_finds_of_one_trail_in_one_round_deposit_it_once():
    """Two `research` acts of the same Record in ONE round both find the trail at RESOLVE (the log does
    not yet hold the first one's deposits), so the re-check at WITNESS (`_found_claims`' `holds_trail`) is
    what keeps one Event found once: the second finding deposits nothing."""
    picks = []
    for n in range(SWEEP):
        w, d, rid = trail_world()
        cand = chooser_research(w, rid)
        w.step = Step.RESOLVE
        out = d.resolve(mint_token(w, WriteClass.ACTS), [research(n, cand)],
                        contest_max_depth=w.fixtures.get("contest_max_depth"))
        if out[0].degree in HAND_BANDS:
            picks.append(n)
        if len(picks) == 2:
            break
    assert len(picks) == 2, f"{SWEEP} act ids drew fewer than two hand bands: {picks}"
    w, d, rid = trail_world()
    cand = chooser_research(w, rid)
    out = step(w, d, *(research(n, cand) for n in picks))
    finds = [e for e in out if e.kind == "finding.made"]
    assert len(finds) == 2, [(e.kind, e.degree) for e in out]
    per = sorted(len(found_deposits(w, e.id)) for e in finds)
    assert per == [0, 3], per
    assert len(forged_claims(w, INVESTIGATOR)) == 2


def test_a_witness_of_the_forgery_finds_nothing_new():
    """`trail_of` excludes what the inquirer already holds as a witness: `p_mid` was in the room when the
    Record was forged, so to him the forging is not trail."""
    w, d, rid = trail_world()
    assert forged_claims(w, ABOUT), "the fixture: the neighbour witnessed the forging"
    assert trail_of(w, rid, ABOUT) == []


# ======================================================================================
# 4 -- THE DISPATCH: the data decides, at both points
# ======================================================================================

def test_find_trail_dispatches_by_kind_and_band_and_nothing_else():
    """`seam.find_trail` on a planted Event of each shape, for the investigator's research: a kind no
    `inquiry_modules` row claims (the failing band's `finding.none`) finds nothing; an UNGRADED
    `finding.made` (no degree -- `interview`'s) reaches the row and finds nothing, because `finding_terms`
    keys the degree; a hand-band `finding.made` finds the forging."""
    w, d, rid = trail_world()
    cand = chooser_research(w, rid)
    a = research("dispatch", cand)
    w.acts.append(a)
    assert manifest_resolve("inquiry", "finding.none") is None
    band = sorted(HAND_BANDS)[0]
    for kind, degree, want in (("finding.none", None, ()), ("finding.made", None, ()),
                               ("finding.made", band, (forged_event(w).id,))):
        e = Event(f"ev_{kind}_{degree}", kind, [], [a.id], w.tick, degree=degree)
        assert tuple(fid for fid, _ in find_trail(w, a, e)) == want, (kind, degree)


def test_the_adapter_refuses_a_module_return_that_is_not_findings(monkeypatch):
    """Design falsifier (iv): the module entry returning anything but `Findings` raises, naming the entry
    -- a software defect, never read as nothing found."""
    w, d, rid = trail_world()
    cand = chooser_research(w, rid)
    a = research("refuse", cand)
    w.acts.append(a)
    role = manifest_resolve("inquiry", "finding.made")["module_entry"]
    monkeypatch.setitem(MODULE_ENTRIES, role,
                        dataclasses.replace(MODULE_ENTRIES[role], fn=lambda inp: {"found": ()}))
    e = Event("ev_refuse", "finding.made", [], [a.id], w.tick, degree=sorted(HAND_BANDS)[0])
    with pytest.raises(Unspecified, match=role):
        find_trail(w, a, e)


def test_the_module_is_pure_and_orders_by_emission():
    """`modules/fieldwork/find.py::find` on records alone: a band with terms uncovers every item in
    `(emitted_at, event_id)` order with those terms; a band with none, and no band, uncover nothing.
    Reached by STRING, as the host reaches it -- the entry the registrar resolved from its composition
    row at driver construction -- so this file names no module code by import."""
    from ..queries.inputs import FieldworkInput, TrailItem
    trail_world()                                   # constructs a driver: the registrar has run
    find = MODULE_ENTRIES[manifest_resolve("inquiry", "finding.made")["module_entry"]].fn
    items = (TrailItem("b", "record.forged", 3), TrailItem("a", "record.forged", 3),
             TrailItem("c", "record.forged", 1))
    band = sorted(HAND_BANDS)[0]
    got = find(FieldworkInput(band, items, dict(FINDING_TERMS)))
    assert isinstance(got, Findings)
    assert got.found == tuple((i, FINDING_TERMS[band]) for i in ("c", "a", "b")), got
    assert find(FieldworkInput(None, items, dict(FINDING_TERMS))) == Findings(())
    assert find(FieldworkInput(band, items, {})) == Findings(())
