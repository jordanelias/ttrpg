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
  * the SEEDED arm (`build_realm(s)`, s = 0-2, four seasons) RECORDS its reading -- which seed, which
    season, or none -- and asserts only that it looked (`checked`). It passes with "none".
  * the PLANTED arms (a death of the throne-holder at MATTER's death write; a `release` of the throne by
    its holder through the real fold) must pass whatever the seeds do. A planted arm passing alone does
    NOT make `succeed` executed in computed play: that is the seeded reading's, a residue if it is none.

FALSIFIER: `World.seat_holds` returning nothing (CP-T02-01's emission helper off) turns the planted
death red at link (i). CONTROL: the same arm before the death (the throne held), and the stubbed arm
itself, carry 0 classed `off_king` referents -- the pre-CP-T02-01 reading (H-230's base: 20 sets, none).
"""
from __future__ import annotations

import pytest

from ..data.matrix import Step, WriteClass
from ..decision import make_chooser
from ..decision.questions import aggregate_questions
from ..harness.populated import build_realm
from ..loop import driver as DRV
from ..loop.driver import SeasonDriver, mint_token, resolvable_verbs
from ..loop.matter import _die
from ..queries import world_q
from ..queries.person_q import ledger_names
from ..state.carriers import Act
from ..state.ids import H, draw_factory
from ..state.world import World

THRONE, HEIR_SEAT = "off_king", "off_heir"
SEEDS, SEASONS = (0, 1, 2), 4


def _holder(w, seat):
    """The one live holder of `seat` (`None` when it is vacant): a live `hold` edge on it."""
    held = [t.subject for t in w.tenures if t.kind == "hold" and t.live and t.object == seat]
    assert len(held) <= 1, f"{seat} has {len(held)} live holders: {held}"
    return held[0] if held else None


def _classed(q):
    return ("off_king", "Office") in q.classes if q is not None else False


def _reading(w, heir, qs):
    """What the four links read at ONE question set handed to `heir` (the barrier-2 projection)."""
    rule = w.fixtures.get("question_aggregation_rule")
    answered = aggregate_questions(qs, rule) if qs else None
    return {"in_ledger": THRONE in ledger_names(heir.ledger),
            "seats_named": THRONE in world_q.seats_named(w, heir),
            "stamped": any(_classed(q) for q in qs),
            "answered": _classed(answered) and THRONE in answered.referents_for("Office")}


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


class _HeirSpy:
    """A spy on `loop.driver.questions_for` (the barrier-2 call site), recording every question set handed
    to the heir with the tick, whether the throne was held and whether he lived. `questions_for` is
    imported by name into `loop.driver`, which is why the spy names that module (its docstring says so)."""

    def __init__(self, heir_id):
        self.heir_id, self.sets = heir_id, []

    def install(self, monkeypatch):
        orig = DRV.questions_for

        def spy(w, p, since=None):
            out = orig(w, p, since)
            if p.id == self.heir_id:
                self.sets.append({"tick": w.tick, "throne_held": _holder(w, THRONE) is not None,
                                  "reading": _reading(w, p, out), "n": len(out)})
            return out
        monkeypatch.setattr(DRV, "questions_for", spy)


def _one_season(w, d):
    """One real season: MATTER, CALENDAR, the rounds of DELIBERATE, RESOLVE and WITNESS."""
    mint = lambda pid, verb, subj: H(w.world_seed, w.tick, pid, f"act:{verb}:{subj}")
    ch = make_chooser(w.fixtures, mint, verbs=resolvable_verbs(),
                      draw=draw_factory(w.world_seed, lambda: w.tick))
    return d.season(ch, question=None, contest_max_depth=w.fixtures.get("contest_max_depth"))


# --- THE SEEDED ARM ------------------------------------------------------------------------------

@pytest.fixture(scope="module")
def seeded():
    """`build_realm(s)` for s = 0-2, four seasons each, the heir's question sets recorded. The module's
    monkeypatch is hand-made (the fixture outlives a test's)."""
    mp = pytest.MonkeyPatch()
    rows = []
    try:
        for seed in SEEDS:
            w = build_realm(seed)
            heir_id = _holder(w, HEIR_SEAT)
            assert heir_id and _holder(w, THRONE) and heir_id != _holder(w, THRONE), "fixture moved"
            spy = _HeirSpy(heir_id)
            spy.install(mp)
            d = SeasonDriver(w)
            vacated = None
            for season in range(SEASONS):
                _one_season(w, d)
                if vacated is None and _holder(w, THRONE) is None:
                    vacated = {"season": season + 1, "heir_alive": heir_id in w.persons}
            mp.undo()
            rows.append({"seed": seed, "heir": heir_id, "sets": spy.sets, "vacated": vacated,
                         "ever_classed": [s["tick"] for s in spy.sets if s["reading"]["answered"]]})
    finally:
        mp.undo()
    return rows


def test_seeded_arm_records_which_seed_and_season_vacates_the_throne_under_a_living_heir(seeded):
    """RECORDS, does not assert, the reading; passes with 'none'. It asserts that it looked (§0.1 pt 2):
    every seed handed the heir a question set at every season's DELIBERATE, and what it checks is the
    sets it read. THE THRONE VACATED WHILE THE HEIR LIVES, then the heir hearing it at a later DELIBERATE
    is the PASS reading; a vacancy he did not hear is printed as UNHEARD, not hidden."""
    checked = sum(len(r["sets"]) for r in seeded)
    assert checked >= len(SEEDS) * SEASONS, f"the heir was handed only {checked} question sets"
    assert all(len({s["tick"] for s in r["sets"]}) >= SEASONS for r in seeded), "a seed skipped a season"
    hits = [(r["seed"], r["vacated"]["season"]) for r in seeded
            if r["vacated"] and r["vacated"]["heir_alive"] and any(
                s["reading"]["answered"] and not s["throne_held"] for s in r["sets"])]
    unheard = [(r["seed"], r["vacated"]["season"]) for r in seeded
               if r["vacated"] and r["vacated"]["heir_alive"] and (r["seed"], r["vacated"]["season"]) not in hits]
    vacated = [(r["seed"], r["vacated"]) for r in seeded if r["vacated"]]
    pre = sum(1 for r in seeded for s in r["sets"] if s["throne_held"] and s["reading"]["answered"])
    print(f"\nCR-26 SEEDED READING: seeds {list(SEEDS)} x {SEASONS} seasons, checked={checked} heir "
          f"question sets; throne vacated: {vacated or 'none'}; heard by a living heir: "
          f"{hits or 'none'}; vacated but UNHEARD: {unheard or 'none'}; "
          f"classed off_king while the throne was HELD: {pre} (control, expected 0)")
    # The control half is an assertion, not a record: with the throne held no set names it classed.
    assert pre == 0, "a set named the held throne as a classed referent: the control is not clean"


# --- THE PLANTED ARMS ----------------------------------------------------------------------------

def _plant(monkeypatch, route, seed=0):
    """A seeded world, the throne-holder's seat emptied by `route` through the real write and the real
    WITNESS, then the heir's NEXT DELIBERATE (a real season) with the question sets recorded.
    Returns `(deposited_at_witness, control_reading, spy)`."""
    w = build_realm(seed)
    king, heir_id = _holder(w, THRONE), _holder(w, HEIR_SEAT)
    assert king and heir_id and king != heir_id, "fixture: no distinct throne-holder and heir"
    heir = w.persons[heir_id]
    d = SeasonDriver(w)
    control = _reading(w, heir, world_q.questions_for(w, heir, None))    # throne held, before anything
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
    deposited = THRONE in ledger_names(w.persons[heir_id].ledger)
    spy = _HeirSpy(heir_id)
    spy.install(monkeypatch)
    _one_season(w, d)
    return deposited, control, spy, [e.kind for e in events]


def test_planted_death_of_the_throne_holder_reaches_the_heir_as_a_classed_office_referent(monkeypatch):
    deposited, control, spy, kinds = _plant(monkeypatch, "death")
    assert "tenure.closed" in kinds, f"the death named no seat: {kinds}"
    assert not any(control.values()), f"control: the heir already heard of the throne: {control}"
    readings = [s["reading"] for s in spy.sets]
    assert spy.sets and all(not s["throne_held"] for s in spy.sets), "fixture: the throne was held again"
    link = _failing_link(deposited, readings)
    assert link is None, f"IN-61 STAYS STOPPED -- first failing link: {link}; readings {readings}"
    assert any(r["answered"] for r in readings)


def test_planted_release_of_the_throne_reaches_the_heir_as_a_classed_office_referent(monkeypatch):
    """The `release` route IN-61's GATE names: the throne vacated by its holder's own `release` (T-m),
    through the real fold. No death, no `person.died`: the seat reaches the heir by `release`'s own
    `tenure.closed` (the closed edge's id, which WITNESS expands to the seat)."""
    deposited, control, spy, kinds = _plant(monkeypatch, "release")
    assert not any(control.values()), f"control: the heir already heard of the throne: {control}"
    assert "person.died" not in kinds, kinds
    readings = [s["reading"] for s in spy.sets]
    assert spy.sets and all(not s["throne_held"] for s in spy.sets), "fixture: the throne was held again"
    link = _failing_link(deposited, readings)
    assert link is None, f"the release route fails -- first failing link: {link}; readings {readings}"


def test_mutation_with_seat_holds_unread_the_planted_death_goes_red_at_link_i(monkeypatch):
    """THE FALSIFIER, run: CP-T02-01's emission helper off (`World.seat_holds` -> `[]`, so
    `death_subjects` names no seat while `remove_person` still closes the holds -- the pre-CP-T02-01
    death). The planted death then fails at link (i), and the heir's question sets carry 0 classed
    `off_king` referents: the control H-230 measured at the base."""
    monkeypatch.setattr(World, "seat_holds", lambda self, who: [])
    deposited, control, spy, kinds = _plant(monkeypatch, "death")
    assert "tenure.closed" not in kinds, f"the stub did not switch the emission off: {kinds}"
    readings = [s["reading"] for s in spy.sets]
    assert spy.sets, "the heir was handed no question set: the control observed nothing"
    link = _failing_link(deposited, readings)
    assert link is not None and link.startswith("(i)"), f"expected red at link (i), got: {link}"
    assert not any(r["stamped"] or r["answered"] for r in readings), readings
    assert sum(1 for s in spy.sets if s["reading"]["answered"]) == 0     # 0 classed off_king referents

