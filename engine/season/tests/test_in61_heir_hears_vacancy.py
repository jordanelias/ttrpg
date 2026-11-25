"""CR-26 -- THE HEIR HEARS THE VACANCY (IN-61's design-first check (4), EXECUTED AS A TEST).

The occasion: when the throne (`off_king`) loses its holder, the holder of `off_heir` (`successions`'
key, IN-61) is handed a question set at the next DELIBERATE that names `off_king` as a CLASSED referent
of class `Office` -- the pair `row.referent_class: Office` forms on. H-230 measured that he was not
(20 question sets over four seasons, none) and named two limits, since repaired: CP-T02-01 (a death
names the seats it empties as a `tenure.closed` claim carrying the Office id) and CP-T02-02 (a realm
seat's id is its `offices.yaml` row id, so the throne is `off_king`).

THE CHAIN, FOUR LINKS, AND WHICH ONE A RED NAMES (`_failing_link`):
  (i)   the claim about the seat is NOT DEPOSITED in the heir's ledger at WITNESS;
  (ii)  it is deposited and EVICTED before he deliberates;
  (iii) it is in his ledger at DELIBERATE and `world_q.seats_named` / `_stamped` do not stamp it;
  (iv)  it is stamped, and the question he answers (`aggregate_questions` under the shipped
        `question_aggregation_rule`, `first`) carries no `Office` class pair for `off_king`.

TWO KINDS OF ARM, AND THEY ARE NOT THE SAME CLAIM:
  * the SEEDED arm (`build_realm(s)`, s = 0-2, four seasons) is a READING, and it lives in
    `harness/heir_hears.py` (`python -m engine.season.harness.heir_hears --seeds 0 1 2 --seasons 4`): which
    seed, which season, or none. It was a test here that passed with "none" and cost about 220 CPU-seconds
    of the suite; the plan (V2) says a reading is a harness reader.
  * the PLANTED arms (a death of the throne-holder at MATTER's death write; a `release` of the throne by
    its holder through the real fold) must pass whatever the seeds do, and they are this file's tests. A
    planted arm passing alone does NOT make `succeed` executed in computed play: that is the seeded
    reading's, a residue if it is none.

FALSIFIER: `World.seat_holds` returning nothing (CP-T02-01's emission helper off) turns the planted
death red at link (i). CONTROL: the same arm before the death (the throne held), and the stubbed arm
itself, carry 0 classed `off_king` referents -- the pre-CP-T02-01 reading (H-230's base: 20 sets, none).
"""
from __future__ import annotations

import pytest

from ..data.matrix import Step, WriteClass
from ..harness.heir_hears import HEIR_SEAT, THRONE
from ..harness.heir_hears import HeirSpy as _HeirSpy      # the names stay: `test_in61_succession.py`
from ..harness.heir_hears import holder as _holder        # imports `_holder` and `_one_season` from here
from ..harness.heir_hears import one_season as _one_season
from ..harness.heir_hears import reading as _reading
from ..boot.realm import build_realm
from ..loop.driver import SeasonDriver, mint_token
from ..loop.matter import _die
from ..queries import world_q
from ..queries.person_q import vacant_named
from ..state.carriers import Act
from ._seat_at_success import seat_at_success  # noqa: F401  (the fixture; its reason is in its module)


def _failing_link(deposited_at_witness, readings):
    """The first link of the chain that breaks, or `None` when the heir hears the vacancy. `readings` are
    the heir's question sets at the DELIBERATE barriers that followed (each a `_reading`)."""
    if not deposited_at_witness:
        return "(i) the claim about the seat is not deposited"
    if not readings:
        return "(ii) the heir never deliberated (no question set was handed to him)"
    if not any(r["in_ledger"] for r in readings):
        return "(ii) the claim was evicted before he deliberated"
    if not any(r["seats_named"] and r["stamped"] for r in readings):
        return "(iii) seats_named does not stamp the seat on his question"
    if not any(r["answered"] for r in readings):
        return "(iv) no Office class pair for the seat reaches the question he answers under `first`"
    return None


# --- THE SEEDED ARM: A READING, NOT A TEST -------------------------------------------------------
# `python -m engine.season.harness.heir_hears --seeds 0 1 2 --seasons 4` prints which seed and season
# vacates the throne under a living heir, and whether he hears it. It was a test of three four-season
# realms that passed with "none" by design (about 220 CPU-seconds of the suite); the plan's V2 says a
# reading is a harness reader, and the plan (CR-26) already said the seeded arm is "never asserted".

# --- THE PLANTED ARMS ----------------------------------------------------------------------------

def _vacant_readings(spy):
    """The heir's question sets handed him while the throne was still vacant. B21.16: any holder of a listed title may claim, so the
    throne can be held again before the season's last deliberation (the realm's five claimants all form the claim at once); the chain
    this file reads is the vacancy reaching the heir, which a set after a claim cannot show."""
    sets = [s for s in spy.sets if not s["throne_held"]]
    assert sets, "fixture: the throne was held at every deliberation"
    return [s["reading"] for s in sets]


def _plant(monkeypatch, route, seed=0):
    """A seeded world, the throne-holder's seat emptied by `route` through the real write and the real
    WITNESS, then the heir's NEXT DELIBERATE (a real season) with the question sets recorded.
    Returns `(deposited_at_witness, control_reading, spy)`."""
    w = build_realm(seed)
    king, heir_id = _holder(w, THRONE), _holder(w, HEIR_SEAT)
    assert king and heir_id and king != heir_id, "fixture: no distinct throne-holder and heir"
    heir = w.persons[heir_id]
    d = SeasonDriver(w)
    # throne held, before anything. v12 B11.08: the realm starts with the seat news (`seed_seat_news`), so the heir already holds the throne as HELD: links (i)-(iii) read true
    # before the death, and `_reading`'s "stamped" and "answered" mean he has HEARD IT VACANT, so they read false here and are the control beside `vacant`.
    control = {**_reading(w, heir, world_q.questions_for(w, heir, None)), "vacant": vacant_named(heir.ledger, THRONE)}
    assert not (control["stamped"] or control["answered"] or control["vacant"]), f"control: the throne reads vacant to the heir while held: {control}"
    if route == "death":
        w.step = Step.MATTER
        w._emitted_by_write = []
        _die(w, mint_token(w, WriteClass.MATTER), king)
        events = list(w._emitted_by_write)
        assert king not in w.persons, "the planted death did not happen"
    elif route == "release":
        w.step = Step.RESOLVE
        w.frozen = False
        events = d.resolve(mint_token(w, WriteClass.ACTS),
                           [Act(id="cr26_rel", actor=king, verb="release", payload={"subject": THRONE})],
                           contest_max_depth=w.fixtures.get("contest_max_depth"))
        assert king in w.persons, "a release is not a death"
    else:
        raise AssertionError(route)
    assert _holder(w, THRONE) is None, f"the {route} did not vacate the throne: {[e.kind for e in events]}"
    assert heir_id in w.persons and _holder(w, HEIR_SEAT) == heir_id, "the heir does not live and sit"
    w.log.extend(events)
    w.step = Step.WITNESS
    d.witness(mint_token(w, WriteClass.INTERIOR), events)
    deposited = vacant_named(w.persons[heir_id].ledger, THRONE) and any(
        c.subject == THRONE and c.predicate == "tenure.closed" for c in w.persons[heir_id].ledger)
    spy = _HeirSpy(heir_id)
    spy.install(monkeypatch)
    _one_season(w, d)
    return deposited, control, spy, [e.kind for e in events]


def test_planted_death_of_the_throne_holder_reaches_the_heir_as_a_classed_office_referent(monkeypatch):
    deposited, control, spy, kinds = _plant(monkeypatch, "death")
    assert "tenure.closed" in kinds, f"the death named no seat: {kinds}"
    assert not control["vacant"], f"control: the heir already heard the throne empty: {control}"
    readings = _vacant_readings(spy)
    link = _failing_link(deposited, readings)
    assert link is None, f"IN-61 STAYS STOPPED -- first failing link: {link}; readings {readings}"
    assert any(r["answered"] for r in readings)


def test_planted_release_of_the_throne_reaches_the_heir_as_a_classed_office_referent(monkeypatch):
    """The `release` route IN-61's GATE names: the throne vacated by its holder's own `release` (T-m),
    through the real fold. No death, no `person.died`: the seat reaches the heir by `release`'s own
    `tenure.closed` (the closed edge's id, which WITNESS expands to the seat)."""
    deposited, control, spy, kinds = _plant(monkeypatch, "release")
    assert not control["vacant"], f"control: the heir already heard the throne empty: {control}"
    assert "person.died" not in kinds, kinds
    readings = _vacant_readings(spy)
    link = _failing_link(deposited, readings)
    assert link is None, f"the release route fails -- first failing link: {link}; readings {readings}"


# --- B21.15: THE TWO ROYAL SEATS ARE TITLES THE THRONE CONFERS ---------------------------------

def test_g3_queens_seat_confer_opens():
    """B21.15 (HAPPENINGS-B edit 1, G3): the Queen's and the Princess's seats, vacant, are refilled by a `confer` through a King's
    seat. Each row's `conferral` is read off the SHIPPED registry (`build_realm(0).offices`) onto a hand-built `_gov_world` (a realm
    costs about 0.6 s a seed, and the world is the one B21.14's band test draws on); then 40 world seeds are each drawn through
    the real `resolve`: never `confer.refused` (eligibility, the counterparty and the write admit the conferral; the band arms'
    strict `kinds ==` read every other refusal), and the seat opens at Overwhelming, Success or Partial, `appointment.resisted` at
    Failure with the seat still empty. FALSIFIER (run once, not kept): `conferral: null` on either row is refused at every seed --
    since B21.80 with `confer.no_basis`, the `basis` clause's kind, which the strict `kinds ==` arms read."""
    from collections import Counter

    from .test_g3_not_yours import _gov_world, _hold
    from ..state.carriers import Office

    shipped = build_realm(0).offices
    bands = {"off_widow_regent": Counter(), "off_princess": Counter()}
    checked = 0
    for seed in range(40):
        for seat in bands:
            row = shipped[seat]
            w, d = _gov_world()
            w.world_seed = seed
            w.offices[seat] = Office(seat, row.post, "R", [], faction="Crown", conferral=row.conferral,
                                     revocation=row.revocation)
            w.step = Step.RESOLVE
            out = d.resolve(mint_token(w, WriteClass.ACTS),
                            [Act(id=f"g3_{seat}_{seed}", actor="p_king", verb="confer", via="off_crown",
                                 payload={"subject": seat, "to": "p_low"})],
                            contest_max_depth=w.fixtures.get("contest_max_depth"))
            kinds = [e.kind for e in out]
            assert "confer.refused" not in kinds, (seed, seat, row.conferral, kinds)
            band = out[0].degree
            bands[seat][band] += 1
            if band == "Failure":
                assert kinds == ["appointment.resisted"] and _hold(w, seat) is None, (seed, seat, kinds)
            else:
                assert kinds == ["tenure.opened"], (seed, seat, band, kinds)
                h = _hold(w, seat)
                assert h is not None and h.subject == "p_low", (seed, seat, band, h)
            checked += 1
    assert checked >= 80, checked
    for seat, c in bands.items():
        assert c["Failure"] > 0 and sum(v for k, v in c.items() if k != "Failure") > 0, (seat, dict(c))


# --- B21.16: ANY LISTED TITLE MAY CLAIM THE THRONE (HAPPENINGS-B edits 2-3, G1, G2) -------------

# The five titles the throne's `successions` row lists (the entry's fixture, written here as the TEST's world, never read off the
# roster: a roster read would hand the red its own answer), and a holder each. `p_old_king` holds the throne and dies by `_die`.
_ROYAL_TITLES = {"off_heir": "p_mid", "off_widow_regent": "p_low", "off_princess": "p_other",
                 "off_duchess_hafenmark": "p_duchess", "off_duke_varfell": "p_high"}


def _royal_world(seed, dead):
    """A hand-built world (`test_g3_not_yours._gov_world`) holding the SHIPPED rows of the throne and its five titles
    (`SEAT_ROW_BY_ID`: conferral and remit as `offices.yaml` has them), each title held, the throne held by `p_old_king`, and the
    deaths in `dead` written through `_die` (the real MATTER death write, which empties the seats). Why not `build_realm`: it costs about 0.6 s a seed and a
    realm cannot be copied (`copy.deepcopy` leaves the log's `_act_ids` closure bound to the source world), so 40 seeds is 24 s."""
    from ..boot.realm import place_person
    from ..data.rosters import SEAT_ROW_BY_ID
    from ..state.carriers import Office, Tenure
    from .test_g3_not_yours import _gov_world
    w, d = _gov_world()
    w.world_seed = seed
    place_person(w, "p_duchess", "the Duchess of Hafenmark", "Hh")
    place_person(w, "p_old_king", "the old King", "R")
    for sid in (THRONE, *_ROYAL_TITLES):
        r = SEAT_ROW_BY_ID[sid]
        w.offices[sid] = Office(sid, r["post"], "R", list(r["remit_acts"]), faction="Crown", conferral=r.get("conferral"),
                                revocation=r.get("revocation"))
    w.add_tenure(Tenure("t_royal_throne", "p_old_king", THRONE, "hold", 0))
    for sid, pid in _ROYAL_TITLES.items():
        w.add_tenure(Tenure(f"t_royal_{sid}", pid, sid, "hold", 0))
    w.step = Step.MATTER
    w._emitted_by_write = []
    for who in dead:
        _die(w, mint_token(w, WriteClass.MATTER), who)
        assert who not in w.persons, who
    assert _holder(w, THRONE) is None, "the planted death did not vacate the throne"
    w.step = Step.RESOLVE
    return w, d


def _claim_seasons(w, d, seasons, seed):
    """`seasons` rounds of the claim, each the real `resolve` over one `succeed` per living holder of a listed title while the throne
    is vacant (a Failure leaves it vacant and the claim forms again, `_eff_succeed`'s `writes_note`); the holder of the throne after.
    Who claims first within a round is the fold's canonical order, not this test's."""
    for season in range(seasons):
        claimants = sorted(t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object in _ROYAL_TITLES)
        if _holder(w, THRONE) is not None or not claimants:
            break
        w.step = Step.RESOLVE
        out = d.resolve(mint_token(w, WriteClass.ACTS),
                        [Act(id=f"b2116_{seed}_{season}_{p}", actor=p, verb="succeed", payload={"subject": THRONE})
                         for p in claimants], contest_max_depth=w.fixtures.get("contest_max_depth"))
        w.log.extend(out)
    return _holder(w, THRONE)


def test_g1_the_throne_is_held_by_the_heir_or_another_listed_title_not_always_the_heir():
    """B21.16 G1: THE KING DEAD, THE HEIR ALIVE, 40 world seeds, two seasons (the source reads four, A-114): the throne is held in
    most seeds, the heir holds it in some and not in all, and in at least one seed the holder of another listed title does.
    ⚠ DEPARTURE FROM THE SOURCE: it reads "the heir holds ... in MOST seeds". Nothing yet favours the heir over the other four
    (the claim's odds are BYZ-E's `favourable` term, edit 4's request, met in B32), so each claimant lands a band at the same rate
    and the heir, one of five, holds in about a fifth of the seeds; the test asserts what the code does and the receipt carries
    the clause. FALSIFIER (run once, not kept): `successions` reverted to the heir alone reads no other holder at any seed, so the
    last assertion fails."""
    held = {"heir": 0, "other": 0, "vacant": 0}
    checked = 0
    for seed in range(40):
        w, d = _royal_world(seed, dead=("p_old_king",))
        who = _claim_seasons(w, d, 2, seed)
        held["vacant" if who is None else "heir" if who == "p_mid" else "other"] += 1
        checked += 1
    assert checked == 40, checked
    assert held["vacant"] < checked // 2, held                     # the throne is held in most seeds
    assert 1 <= held["heir"] < checked, held                       # the heir in some, not in all
    assert held["other"] >= 1, held                                # another listed title's holder took it


def test_g2_both_dead_throne_claimable():
    """B21.16 G2: THE KING AND THE HEIR DEAD, 40 world seeds, two seasons: the throne is held at the end in at least one seed and
    vacant in at least one. Today (before edit 2): vacant at every seed. FALSIFIER (run once, not kept): `successions` reverted to
    the heir alone reads every seed vacant and the first assertion fails."""
    held = {"held": 0, "vacant": 0}
    checked = 0
    for seed in range(40):
        w, d = _royal_world(seed, dead=("p_old_king", "p_mid"))
        who = _claim_seasons(w, d, 2, seed)
        assert who != "p_mid", "the dead heir holds the throne"
        held["vacant" if who is None else "held"] += 1
        checked += 1
    assert checked == 40, checked
    assert held["held"] >= 1 and held["vacant"] >= 1, held


@pytest.mark.usefixtures("seat_at_success")       # the claim's write (which title closes), not its draw
def test_consort_claim_closes_her_seat_only_when_its_remit_is_empty():
    """B21.16 (R-16, the regent row's `remit_acts: []`): THE CONSORT'S CLAIM LAYS DOWN HER TITLE, because the seat exists to pass a
    seat -- `appointed`, no remit. CONTROL: with her old grant restored (`confer`, `revoke`...), the same claim at the same fold
    opens the throne and she KEEPS both (the seat has a use of its own, so the claim does not spend it). A duke who claims keeps
    his duchy (`off_duke_varfell`, `elected`, a remit of its own)."""
    def claim(w, d, who):
        out = d.resolve(mint_token(w, WriteClass.ACTS), [Act(id="b2116_claim", actor=who, verb="succeed", payload={"subject": THRONE})],
                        contest_max_depth=w.fixtures.get("contest_max_depth"))
        return [e.kind for e in out]

    for claimant, kept in (("p_low", False), ("p_high", True)):
        w, d = _royal_world(0, dead=("p_old_king", "p_mid"))
        seat = next(s for s, p in _ROYAL_TITLES.items() if p == claimant)
        assert "succession.refused" not in claim(w, d, claimant)
        assert _holder(w, THRONE) == claimant, "the claim did not seat him"
        assert (_holder(w, seat) == claimant) is kept, (claimant, seat)
    w, d = _royal_world(0, dead=("p_old_king", "p_mid"))
    w.offices["off_widow_regent"].remit_acts = ["issue", "confer", "revoke"]        # the control: the seat has a grant of its own
    claim(w, d, "p_low")
    assert _holder(w, THRONE) == "p_low" and _holder(w, "off_widow_regent") == "p_low", "the control spent a seat with a remit"