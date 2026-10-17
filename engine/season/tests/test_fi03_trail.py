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

STEP 3, THE EXIT TESTS (sections 5-7): the position's falsifier over the tree's existing response surface
(Q2 -> `opening_set`; no goal edit, no decision code), the entity-id closure in SC-01 step 16's form
(`_closure_scan.py`, the one walk), and one seed run twice in one process giving one hash.
RED WHEN PLANTED (2026-10-17, each run then restored; the test-side plants on a scratch copy of this file,
deleted): `fieldwork_input` projecting no trail item -- the found-trail half and both twice-hash tests go
RED; the control arm left unsuppressed (precondition dropped) -- `trail_qs == []` goes RED;
`trail_of` walking `faction.surveyed` beside `covert_kinds` -- the survey control goes RED at its
`trail_of` precondition; the survey's positive arm without the listing -- RED ("the control is vacuous");
`npcs.yaml` dropped from the union -- the plant's `npcs.yaml` case goes RED; the main twice-hash test
under the drop-after-1 counter -- RED (`[1, 0]`); the control without the counter -- RED (one hash);
the realm with the chooser's draw seeded one higher per call -- RED (two hashes); the realm with the
provider forced to uncover any other hand's forging -- RED ("the realm now reaches a find").
"""
from __future__ import annotations

import ast
import dataclasses
import functools
import inspect
from pathlib import Path

import pytest

from .. import epistemic
from ..data import files
from ..data.goals import goals
from ..data.matrix import Step, WriteClass
from ..data.rosters import COVERT_KINDS, FINDING_TERMS, faction_prop_id
from ..decision.choose import _payload_of
from ..decision.options import opening_set
from ..epistemic import SEEN_PREDICATE, trail_of
from ..gaps import Unspecified
from ..harness import populated as POP
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..loop.witness import HAND_TERM
from ..manifest import MODULE_ENTRIES, resolve as manifest_resolve
from ..manifest.providers import PROVIDERS
from ..queries import world_q
from ..queries.inputs import Findings
from ..seam import find_trail
from ..state.attribution import actor_of
from ..state.carriers import Act, Claim, Event, Proposition, Tenure, View
from ._closure_scan import branches_on_ids, game_code

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


def trail_world(verb="forge", kind="record.forged"):
    """THE WORLD, built through the fold to the moment the investigator holds the forged Record (tick 2).
    Returns `(w, d, rid)`. `verb`/`kind`: the tick-0 act that mints the Record and the one Event it must
    emit -- `forge` by default; step 3's structural control passes `survey` (`faction.surveyed`), which
    mints the same Record id (the id is the act's) into the same hand by the same body (`_mint_sheet`)."""
    w = P.tiny_world()
    w.propositions[FAC] = Proposition(FAC, "HOLDS", "Crown", "is a faction of this world", True, 0)
    for pid in (INVESTIGATOR, ABOUT):
        w.add_tenure(Tenure(f"t_commit_{pid}", pid, FAC, "commit", since=0))
    d = SeasonDriver(w)
    forger = w.persons[FORGER]
    forger.ledger.append(Claim(f"c_{FORGER}_{ABOUT}", FORGER, ABOUT, "exists:Person", 1, w.tick,
                               "firsthand", 1, "own"))
    out = step(w, d, Act(id=FORGE_ID, actor=FORGER, verb=verb, payload={"subject": ABOUT}))
    assert [e.kind for e in out] == [kind], [e.kind for e in out]
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


# ======================================================================================
# 5 -- STEP 3, THE POSITION'S FALSIFIER: a response forms only from a found trail
# ======================================================================================
# THE RESPONSE SURFACE IS THE TREE'S EXISTING Q2 ROUTE, nothing added for FI-03: a deposited claim the
# investigator's `reach` covers is a `claim_landed` question (`world_q.questions_for`), and
# `decision/options.py::opening_set` forms candidates on its referent. "His next deliberation" is the
# next tick: `questions_for`'s default `since` is `(tick - 1, 0)`, so at the find's own tick the
# `give`'s and the `move`'s claims about the forger (tick 1) are still new and would raise questions on
# him in EVERY arm; one tick on, only what the find deposited is new.

def after_research(n, cand, verb="forge", kind="record.forged"):
    """`trail_world(verb, kind)`, the investigator's `research(n, cand)` resolved and witnessed, then the
    tick advanced to his next deliberation. Returns `(w, rid, finding)`."""
    w, d, rid = trail_world(verb, kind)
    (finding,) = step(w, d, research(n, cand))
    w.tick += 1
    return w, rid, finding


def responses(w, kind="record.forged"):
    """What the investigator's next deliberation forms on the FORGER, through the real chooser path.
    Returns `(trail_qs, from_trail, on_him)`: the questions whose `about` claim is `(FORGER, kind)` --
    not merely a question naming him -- the candidates `opening_set` forms on him from those, and every
    candidate it forms on him from ANY question."""
    p = w.persons[INVESTIGATOR]
    by_id = {c.id: c for c in p.ledger}
    view = View(INVESTIGATOR, [], w.fixtures.get("view_k"))
    trail_qs, from_trail, on_him = [], [], []
    for q in world_q.questions_for(w, p):
        c = by_id.get(q.about)
        is_trail = c is not None and (c.subject, c.predicate) == (FORGER, kind)
        if is_trail:
            trail_qs.append((q, c))
        for cand in opening_set(p, view, q, w.fixtures):
            if cand.subject == FORGER:
                on_him.append(cand)
                if is_trail:
                    from_trail.append(cand)
    return trail_qs, from_trail, on_him


def test_a_found_trail_forms_a_response_on_the_forger_and_a_suppressed_one_forms_none(monkeypatch):
    """THE POSITION'S FALSIFIER (`_part6` FI-03): same seed, same forge, same research act, same roll.
    TRAIL FOUND: at his next deliberation `questions_for` holds a question whose `about` claim is the
    inferred `(forger, record.forged)` the find deposited, and `opening_set` forms >= 1 candidate on the
    forger FROM IT. TRAIL SUPPRESSED (`finding_terms` emptied, step 2's control): the band is drawn
    identically and deposits nothing, and no question is about the forger's deed, none names him, and no
    candidate forms on him from any question."""
    n, cand = find_band(HAND_BANDS)
    w, rid, finding = after_research(n, cand)
    assert finding.kind == "finding.made" and finding.degree in HAND_BANDS, (finding.kind, finding.degree)
    trail_qs, from_trail, on_him = responses(w)
    assert trail_qs, "the found trail raised no question about the forger's deed"
    assert all(c.source == "inferred" and c.doer is None for _, c in trail_qs), trail_qs
    assert from_trail, "the question about the forger's deed formed no candidate on him"

    for band in list(FINDING_TERMS):
        monkeypatch.delitem(FINDING_TERMS, band)
    w, rid, finding2 = after_research(n, cand)
    assert (finding2.kind, finding2.degree, finding2.id) == (finding.kind, finding.degree, finding.id)
    assert forged_claims(w, INVESTIGATOR) == [] and found_deposits(w, finding2.id) == [], (
        "the control deposited the trail: it is not suppressed")
    trail_qs, _, on_him = responses(w)
    assert trail_qs == [], trail_qs
    assert not [q.id for q in world_q.questions_for(w, w.persons[INVESTIGATOR]) if FORGER in q.referents]
    assert on_him == [], sorted({c.verb for c in on_him})


def test_a_research_on_a_surveyed_record_forms_no_response_on_its_maker(monkeypatch):
    """THE STRUCTURAL CONTROL: the same world with the Record minted by `survey` (`faction.surveyed`, a
    deed of the same man, not a `covert_kinds` member), handed over the same way, and the same `research`
    act drawing the same hand band: nothing is trail, nothing is deposited, and no candidate forms on the
    maker. In the realm every act executes and emits its Event (S19.4), so a trail is suppressed only at
    the container -- this control is the other half: an act whose kind the data does not list.
    ITS OWN POSITIVE ARM, so the negative cannot pass for a reason other than the list: `covert_kinds`
    widened to the survey's kind (monkeypatched on `epistemic`, the one reader), the same world, the same
    act -- a response on him forms."""
    n, cand = find_band(HAND_BANDS)
    survey = ("survey", "faction.surveyed")
    assert survey[1] not in COVERT_KINDS, sorted(COVERT_KINDS)
    w, d, rid = trail_world(*survey)
    made = next(e for e in w.log if e.kind == survey[1])
    assert actor_of(w, made) == FORGER, "the survey is not the maker's deed"
    assert not [c for c in w.persons[INVESTIGATOR].ledger if c.when == made.emitted_at], (
        "the investigator witnessed the survey")
    # The chooser forms a `research` on this Record here too (its `to` operand is derived from a different
    # question, so its payload differs); the act resolved below is the forge world's, verbatim.
    mine = chooser_research(w, rid)
    assert mine is not None and mine.subject == rid, "the chooser forms no research on the surveyed Record"
    assert trail_of(w, rid, INVESTIGATOR) == []

    w, rid, finding = after_research(n, cand, *survey)
    assert finding.kind == "finding.made" and finding.degree in HAND_BANDS, (finding.kind, finding.degree)
    assert found_deposits(w, finding.id) == []
    trail_qs, _, on_him = responses(w, survey[1])
    assert trail_qs == [] and on_him == [], (trail_qs, sorted({c.verb for c in on_him}))

    monkeypatch.setattr(epistemic, "COVERT_KINDS", COVERT_KINDS | {survey[1]})
    w, rid, finding = after_research(n, cand, *survey)
    assert finding.degree in HAND_BANDS, finding.degree
    trail_qs, from_trail, _ = responses(w, survey[1])
    assert trail_qs and from_trail, "listing the survey's kind formed no response: the control is vacuous"


# ======================================================================================
# 6 -- STEP 3, CLOSURE: no game code branches on an entity id (SC-01 step 16's form)
# ======================================================================================
# The walk and the scope are `_closure_scan.py`'s, shared with `test_sc01_the_bar.py` (arrangement
# ids). A STATIC scan for the reason SC-01 gives: a seeded run reaches a planted branch only if that
# entity happens to act, so a behavioural test passes over a branch it never executes.

@functools.lru_cache(maxsize=None)
def entity_ids() -> dict:
    """The ids a scripted branch would name, from their loaders, never spelt: `goals.yaml` (its reader),
    the persons `build_realm(0)` seats, and `npcs.yaml`'s cases (the harness's own reader of its own
    roster file, `populated._load(ROSTER)`)."""
    return {"goals.yaml": frozenset(g.id for g in goals()),
            "build_realm(0).persons": frozenset(POP.build_realm(0).persons),
            "npcs.yaml": frozenset(r["case"] for r in POP._load(POP.ROSTER).get("npcs") or ())}


def _union() -> frozenset:
    return frozenset().union(*entity_ids().values())


def _provider_and_entry_files() -> tuple:
    """The fieldwork container's two files, read off what is REGISTERED (the provider the `inquiry` row
    names, the entry its composition row resolved), not spelt as paths."""
    trail_world()                                   # constructs a driver: the registrar has run
    row = manifest_resolve("inquiry", "finding.made")
    prov = PROVIDERS[("inquiry", row["provider"])]
    entry = MODULE_ENTRIES[row["module_entry"]].fn
    return tuple(Path(inspect.getsourcefile(fn)).resolve() for fn in (prov, entry))


def test_no_game_code_branches_on_an_entity_id():
    """FI-03's SCRIPTING-DRIFT FALSIFIER: no game code special-cases a goal, a person or an NPC case by
    its id. SCOPE AND WHAT IS NOT SEEN: `_closure_scan.py`'s docstring. The floor (`>= 100` files) and the
    two fieldwork files' membership assert the sweep read the package and the container;
    `test_a_planted_branch_on_an_entity_id_in_the_real_provider_is_found` is the scan's own falsifier."""
    ids = entity_ids()
    assert all(ids.values()), {k: len(v) for k, v in ids.items()}
    paths = game_code()
    assert len(paths) >= 100, len(paths)
    scanned = {f.resolve() for f in paths}
    for must in _provider_and_entry_files():
        assert must in scanned, f"{must} is not scanned"
    union = _union()
    found = {str(f.relative_to(files.REPO_ROOT)): h
             for f in paths if (h := branches_on_ids(ast.parse(f.read_text(encoding="utf-8")), union))}
    assert not found, f"game code branches on an entity id (scripting drift): {found}"


@pytest.mark.parametrize("source", ["goals.yaml", "build_realm(0).persons", "npcs.yaml"])
def test_a_planted_branch_on_an_entity_id_in_the_real_provider_is_found(source):
    """The scan's own falsifier, on the real provider's source PARSED IN MEMORY (never written: other
    `-n auto` workers scan the tree): `seam/wrappers/fieldwork.py` scans clean, then with
    `if act.actor == "<id>": return Findings(())` as `find`'s first statement after its docstring, it is
    reported. One id from each source of the union, so dropping a source from it reddens its case."""
    eid = min(entity_ids()[source])
    path = _provider_and_entry_files()[0]
    tree = ast.parse(path.read_text(encoding="utf-8"))
    assert branches_on_ids(tree, _union()) == []
    (fn,) = [n for n in tree.body if isinstance(n, ast.FunctionDef) and n.name == "find"]
    fn.body.insert(1, ast.parse(f"if act.actor == {eid!r}:\n    return Findings(())\n").body[0])
    assert [v for _, v in branches_on_ids(tree, _union())] == [eid]


# ======================================================================================
# 7 -- STEP 3, ONE SEED, TWICE, ONE HASH
# ======================================================================================
# THE SUBJECT IS PINNED BY MEASUREMENT, NOT SWAPPED AT RUN TIME: `build_realm(0)` reaches no find in two
# seasons (no `record.given`, so no forged Record reaches another hand -- `trail_of`'s docstring), so the
# twice-identical test of the FIND runs `trail_world`; the realm's twice-identical run is a separate,
# separately named test of the LOOP, which asserts the absence it relies on.

def count_finds(monkeypatch, drop_after=None) -> list:
    """Wrap the registered `inquiry` provider (the entry every finding reaches, `seam.find_trail`) to
    record how many items each call's `Findings` held. `drop_after=N` is the CONTROL'S PLANT: a counter
    kept across calls (as module state would be) that returns `Findings(())` from call N + 1 on."""
    trail_world()                                   # the provider table is filled
    key = ("inquiry", manifest_resolve("inquiry", "finding.made")["provider"])
    real, seen = PROVIDERS[key], []

    def wrapped(w, a, e, *, module_entry=None):
        out = real(w, a, e, module_entry=module_entry)
        if drop_after is not None and len(seen) >= drop_after:
            out = Findings(())
        seen.append(len(out.found))
        return out
    monkeypatch.setitem(PROVIDERS, key, wrapped)
    return seen


def one_run(n, cand):
    """`trail_world` and the investigator's hand-band research; the world's content hash."""
    w, d, rid = trail_world()
    step(w, d, research(n, cand))
    return w.content_hash()


def test_one_seed_twice_in_one_process_gives_one_hash_and_each_run_finds(monkeypatch):
    """The EXIT's *one seed run twice in one process giving one hash*, over the find: the same world, the
    same act, twice -- equal `content_hash()`, and each run's provider handed back a non-empty `Findings`
    (so the equality is not two runs that never reached the entry)."""
    n, cand = find_band(HAND_BANDS)                 # before the counter: the sweep calls the provider too
    seen = count_finds(monkeypatch)
    first = one_run(n, cand)
    k = len(seen)
    second = one_run(n, cand)
    assert seen[:k] and any(seen[:k]) and any(seen[k:]), seen
    assert first == second, "the same seed and act hashed differently in one process"


def test_a_find_that_keeps_state_across_runs_splits_the_hash(monkeypatch):
    """THE CONTROL: the twice-identical check can see a find that is not a function of its input -- with
    a counter that drops items after the first call, the first run finds and the second does not, and
    the two hashes differ."""
    n, cand = find_band(HAND_BANDS)
    seen = count_finds(monkeypatch, drop_after=1)
    first, second = one_run(n, cand), one_run(n, cand)
    assert len(seen) == 2 and seen[0] > 0 and seen[1] == 0, seen
    assert first != second, "a find that drops items on its second run left the hash unmoved"


def test_the_realm_seed_twice_in_one_process_gives_one_hash_and_reaches_no_find():
    """THE LOOP'S DETERMINISM, NOT THE FIND'S: `build_realm(0)` for two seasons (`populated.run` one
    season at a time on one world, `test_season_weather`'s BASE_HASHES shape), twice in one process --
    equal `content_hash()`. IT REACHES NO FIND, asserted rather than assumed: its inquiries do draw finding
    bands (so the entry is called), and no finding deposits anything. If that ever stops holding, the
    realm reaches the trail and is a candidate subject for the find's twice-identical test above."""
    def realm():
        w = POP.build_realm(0)
        for _ in range(2):
            POP.run(seasons=1, seed=0, w=w)
        return w
    a, b = realm(), realm()
    assert a.content_hash() == b.content_hash(), "build_realm(0) twice in one process gave two hashes"
    finds = [e for e in a.log if e.kind == "finding.made" and FINDING_TERMS.get(e.degree)]
    assert finds, "the realm drew no finding band: the entry was never called"
    assert not [e.id for e in finds if found_deposits(a, e.id)], "the realm now reaches a find"
