"""Plan position `24f` -- SUBSISTENCE IS TERRITORIAL. `workplans/2026-09-18-governance-settlement-
behaviour-plan_part2.md`, *"24f — SUBSISTENCE IS TERRITORIAL (`ED-IN-0255`, ruled 2026-09-18)"*; its
design step is `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md` §3.1 item 10.

⭐ THE RULING, verbatim: *"subsistence/starvation should largely be an abstract/governance issue, and we
can just have NPC synecdoches that just represent the overall population affected? i don't think
having lords and guild members etc worry about subsistence is worthwhile"*; *"it's a territorial
issue"*.

What the position built, each asked of the real builder, the real MATTER barrier and the real Queries:
  1. THE PRODUCER -- `engine/season/cohorts.yaml`, authored `weight > 1` rows, one per populated rung,
     read once by `harness/populated.py::build_realm` after the case-derived cast
     (`cohort_rows` checks the file; `seat_cohorts` seats it and checks each weight against
     `capacity`). `ED-WR-0011` option A: nothing mints a cohort at run time.
  2. THE EXEMPTION -- `world_q.subsistence_draw` feeds only `Person.is_cohort`. The individual at
     `weight == 1`, the ruling's *"lords and guild members"*, wants nothing, is never short, and
     MATTER never falls his body for dearth. Both landed in ONE commit: alone, the exemption empties
     the draw on every built world (the plan's own attack: *"DEAD ON ARRIVAL"*).

THE FALSIFIERS, each with the failure it would show:
  * the producer seats exactly the file's rows beside an unchanged cast, and REFUSES each shape a row
    cannot take -- a weight-1 row, a weight past `capacity`, an unknown or doubled rung, a field from
    `npcs.yaml`'s schema, an empty file. The ceiling is shown to READ the dwellings, not a copy;
  * `_part2`'s own falsifier, on the BUILT realm and not a probe crowd: under a non-zero `body_step`,
    an office-holder under a settlement in dearth keeps his body, and that settlement's cohort, in
    the same dearth, draws and its body falls. CONTROL: the shipped `body_step` moves no body;
  * THE REBUILT DRAIN GUARD (`test_w8`'s, retired 2026-09-18 with a pointer to rebuild it *"on the
    TERRITORIAL quantity"*): on the built realm, at least one cohort draws real stock, the record
    MATTER used names no individual, and the realm's matter is conserved across the draw exactly.

MUTATION-CHECKED at `24f`: deleting the `is_cohort` skip in `subsistence_draw` reddens five tests --
the eater set, the ceiling test's eater line, the falsifier (`p_npc_008`, seated under `set_s_018`,
falls 1000 -> 970), its control, and the drain guard. ⚠ AND ONE MUTATION IT DOES NOT CATCH, said
rather than implied: seating the cohorts BEFORE the cast's tie block leaves every test here green,
because on today's roster no NPC's tie reaches the `neighbour` tier from the last-sorted hearth, the
one place a settlement-homed cohort would enter the pool. The no-tie test pins the property; the
ORDER that guarantees it is argued at `build_realm`'s call site, not observed.
"""

from __future__ import annotations

import ast
from pathlib import Path

import pytest

from ..data.matrix import Step, WriteClass
from ..data.requires import SHORTFALL_PREDICATE
from ..epistemic import _ch_co_located
from ..gaps import Forbidden, ShapeGap
from ..harness import populated as POP
from ..harness import probes as P
from ..harness import register as REG
from ..harness.run_cases import load_cases
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.attribution import anchor_of
from ..state.carriers import Person, Rung, Site, Tenure
from ..state.ids import ROOT

WEIGHTS = P.DEFAULT_FIXTURES.get("subsistence_weight")
# v9 SE-01 (`24g`): THE LIVE ARMS ARE READ OFF `H-125`'s OWN `sweep:` ROW, NOT COPIED. The register is
# where the sweep is declared and `harness/register.py` is its one reader, so a re-swept row moves
# these tests with it. The shipped default is the CONTROL arm (`0`); every OTHER arm is a live arm,
# and the falsifier below runs at each of them -- never a new magnitude.
H125 = next(r for r in REG.load()["rows"] if r["id"] == "H-125")
CONTROL_ARM = P.DEFAULT_FIXTURES.get("body_step")
LIVE_ARMS = [arm for arm in H125["sweep"] if arm != CONTROL_ARM]


def _cohorts(w) -> dict:
    return {pid: p for pid, p in w.persons.items() if p.is_cohort}


def _matter(w):
    """MATTER alone, through the real barrier and a real MATTER token."""
    d = SeasonDriver(w)
    w.step = Step.MATTER
    return d.matter(mint_token(w, WriteClass.MATTER), [])


def _want(weight: int) -> dict:
    """What a person of this weight eats a season, recomputed from the fixture rather than copied."""
    return {k: wt * weight for k, wt in sorted(WEIGHTS.items()) if wt * weight > 0}


@pytest.fixture(scope="module")
def realm():
    """`build_realm(0)`, UNTOUCHED -- read-only tests share it; a test that runs MATTER builds its
    own, because MATTER writes."""
    return POP.build_realm(0)


# ======================================================================================
# 1 -- THE PRODUCER: `cohorts.yaml`, seated at world-gen beside the cast
# ======================================================================================

def test_24f_the_realm_seats_exactly_the_authored_rows_beside_an_unchanged_cast(realm):
    rows = POP.cohort_rows()
    cohorts = _cohorts(realm)
    assert rows, "the file is empty; every assertion below would pass over nothing"
    assert set(cohorts) == {f"{POP.COHORT_PREFIX}{r['rung']}" for r in rows}, (
        "the world's cohorts are not the file's rows -- something minted one, or dropped one")
    lives = world_q.residence_of(realm)
    stands = world_q.home_of(realm)
    for r in rows:
        pid = f"{POP.COHORT_PREFIX}{r['rung']}"
        assert cohorts[pid].weight == r["weight"], f"{pid}: weight is not the authored one"
        assert lives[pid] == stands[pid] == r["rung"], (
            f"{pid} lives at {lives.get(pid)!r} and stands at {stands.get(pid)!r}, not at its row's "
            f"rung {r['rung']!r}")
    # THE CAST IS THE CORPUS'S, UNCHANGED: one person per NPC case, every one an individual.
    cast = {pid for pid, p in realm.persons.items() if not p.is_cohort}
    assert len(cast) == len(list(load_cases("NPC"))), (
        "the case-derived cast changed size when the cohorts were seated")
    assert all(realm.persons[pid].weight == 1 for pid in cast)
    # A COHORT HOLDS NOTHING AND BELONGS TO NOTHING: its only edges are the two the seeder mints.
    for t in realm.tenures:
        if t.subject in cohorts:
            assert t.kind in ("contain", world_q.RESIDE_KIND), (
                f"{t.subject} has a `{t.kind}` edge the producer never mints")


def test_24f_the_cohorts_are_seated_after_the_cast_so_no_want_or_tie_lands_on_one(realm):
    """THE SECOND SEED IS NOT AN EDIT TO THE FIRST. `build_realm`'s tie tiers pool over `contain`
    edges (`roof`, `neighbour`), so a cohort seated before them would become the subject of some
    NPC's want. Seated last, none can be."""
    cohorts = set(_cohorts(realm))
    assert cohorts, "no cohort was seated; this test would pass vacuously"
    about = {p.subject for p in realm.propositions.values()}
    assert not about & cohorts, f"a Proposition is about a cohort: {sorted(about & cohorts)}"
    named = {t.object for t in realm.tenures if t.subject not in cohorts}
    assert not named & cohorts, f"a cast member's edge names a cohort: {sorted(named & cohorts)}"


def test_24f_every_cohort_is_a_cohort_and_fits_its_rungs_capacity(realm):
    cohorts = _cohorts(realm)
    assert cohorts
    for pid, p in cohorts.items():
        rung = world_q.residence_of(realm)[pid]
        assert 1 < p.weight <= world_q.capacity(realm, rung), (
            f"{pid} at weight {p.weight} against capacity {world_q.capacity(realm, rung)}")


def _dwelling(w, sid, rung):
    w.sites[sid] = Site(sid, rung, world_q.DWELLING_KIND,
                        condition=w.fixtures.get("condition_scale"))


def test_24f_the_ceiling_reads_the_dwellings_and_refuses_a_cohort_they_cannot_house():
    """CHECKED AGAINST `capacity`, NEVER DERIVED FROM IT -- and the check reads the Query, so it
    moves when the Sites do. `tiny_world` has no dwelling: every rung is at the floor, which houses
    one, so a cohort of two refuses; one dwelling under `S` still houses one; a second admits it."""
    w = P.tiny_world()
    row = [{"rung": "S", "weight": 2}]
    assert world_q.capacity(w, "S") < 2, "the fixture already houses two; nothing below can refuse"
    with pytest.raises(ShapeGap):
        POP.seat_cohorts(w, row)
    assert not _cohorts(w), "a refused row seated its cohort anyway"
    _dwelling(w, "s_hh_dwelling", "Hh")
    with pytest.raises(ShapeGap):
        POP.seat_cohorts(w, row)
    _dwelling(w, "s_s_dwelling", "S")
    (pid,) = POP.seat_cohorts(w, row)
    assert w.persons[pid].weight == 2 and world_q.residence_of(w)[pid] == "S"
    # AND IT IS NOW AN EATER, which is the whole point of seating it.
    assert set(world_q.subsistence_draw(w)) == {pid}


@pytest.mark.parametrize("text", [
    "cohorts: []\n",                                                  # nobody would eat
    "cohorts:\n- {rung: set_s_001, weight: 1}\n",                     # an individual, not a cohort
    "cohorts:\n- {rung: set_s_001, weight: true}\n",                  # YAML's `true` is not 1 < w
    "cohorts:\n- {rung: set_s_001, weight: 2.5}\n",                   # a weight is a whole number
    "cohorts:\n- {rung: set_s_001}\n",                                # no weight at all
    "cohorts:\n- {rung: set_s_001, weight: 2, case: NPC-001}\n",      # `npcs.yaml`'s schema
    "cohorts:\n- {rung: set_s_001, weight: 2}\n- {rung: set_s_001, weight: 3}\n",  # one per rung
])
def test_24f_the_reader_refuses_every_shape_a_cohort_row_cannot_take(text):
    with pytest.raises(ShapeGap):
        POP.cohort_rows(text)


def test_24f_a_row_naming_a_place_the_world_did_not_build_refuses():
    w = P.tiny_world()
    with pytest.raises(ShapeGap):
        POP.seat_cohorts(w, POP.cohort_rows("cohorts:\n- {rung: set_nowhere, weight: 2}\n"))


# ======================================================================================
# 2 -- THE EXEMPTION: only a cohort eats, and the draw is never empty on the built realm
# ======================================================================================

def test_24f_on_the_built_realm_the_eaters_are_exactly_the_cohorts_and_there_are_some(realm):
    """THE PRECONDITION THE PLAN DEMANDS (`_part2` 24f): *"its falsifier asserts the eater count on
    `build_realm(0)` is `>= 1`"*, so the exemption cannot silently empty the pass. And the other
    half: no individual is in the record at all."""
    record = world_q.subsistence_draw(realm)
    assert len(record) >= 1, "the exemption emptied the draw on the built realm"
    assert set(record) == set(_cohorts(realm)), (
        f"the eaters are not the cohorts: individuals {sorted(set(record) - set(_cohorts(realm)))}, "
        f"unfed cohorts {sorted(set(_cohorts(realm)) - set(record))}")
    # THE TERRITORIAL QUANTITY: the realm demands exactly its cohorts' weighted want, and a hearth
    # housing only named people demands nothing.
    total = sum(p.weight for p in _cohorts(realm).values())
    assert world_q.demanded(realm, "r_valoria") == _want(sum(
        p.weight for pid, p in _cohorts(realm).items()
        if "r_valoria" in world_q.ancestry(realm, world_q.residence_of(realm)[pid])))
    assert sum(sum(row[k][0] for k in row) for _h, row in record.values()) == \
        sum(_want(total).values())
    seated = {t.subject for t in realm.tenures
              if t.kind == "hold" and t.live and t.object in realm.offices}
    assert seated, "nobody is seated; the exemption's other half has no subject"
    seat_home = world_q.residence_of(realm)[sorted(seated)[0]]
    assert not [pid for pid in _cohorts(realm)
                if seat_home in world_q.ancestry(realm, world_q.residence_of(realm)[pid])]
    assert world_q.demanded(realm, seat_home) == {}, (
        f"{seat_home} houses only named people and still demands food")


def _holder_and_cohort_pairs(w) -> list:
    """`(office-holder, the cohort of the settlement he lives under, that settlement)` for every
    seated person whose residence sits under a settlement that has a cohort."""
    lives = world_q.residence_of(w)
    cohort_at = {lives[pid]: pid for pid in _cohorts(w)}
    seated = sorted({t.subject for t in w.tenures
                     if t.kind == "hold" and t.live and t.object in w.offices})
    out = []
    for pid in seated:
        for rung in world_q.ancestry(w, lives[pid]):
            if rung in cohort_at:
                out.append((pid, cohort_at[rung], rung))
                break
    return out


def test_se01_the_sweep_has_a_control_and_at_least_one_live_arm():
    """THE PARAMETRIZATION BELOW CANNOT BE VACUOUS: `H-125` declares a control (the shipped default,
    `0`) and at least one live arm, and the shipped default IS one of the declared arms."""
    assert CONTROL_ARM == 0, "the shipped `body_step` is no longer the control; `H-125` disagrees"
    assert CONTROL_ARM in H125["sweep"], f"the shipped arm is not on `H-125`'s sweep {H125['sweep']}"
    assert LIVE_ARMS and all(isinstance(a, int) and a > 0 for a in LIVE_ARMS), LIVE_ARMS


@pytest.mark.parametrize("arm", LIVE_ARMS)
def test_24f_falsifier_in_dearth_the_office_holder_keeps_his_body_and_the_cohort_does_not(arm):
    """`_part2` 24f's FALSIFIER, verbatim: *"Under a non-zero `body_step` arm: a `weight == 1`
    office-holder at a rung in dearth keeps their body; a `weight > 1` cohort at the same rung draws
    and its body moves."* On the BUILT realm -- *"a guard that passes only on `probes.py:744` is the
    dead-on-arrival case above, passing"*. v9 SE-01 (`24g`) runs it at EVERY live arm of `H-125`'s
    sweep (read off the register), and asserts the fall is exactly `arm x shortfall` -- the live
    arm's whole arithmetic, `loop/matter.py`'s `lost = step * sum(short)`.

    THE DEARTH IS THE REALM'S OWN, NOT PLANTED. At build every larder is empty and MATTER draws
    before it takes the first yield (#353 §25's order), so the first draw finds no stock anywhere:
    every settlement's `demanded` exceeds its `delivered`. Nothing here empties a store."""
    w = POP.build_realm(0)
    w.fixtures = w.fixtures.sweep("body_step", arm)
    pairs = _holder_and_cohort_pairs(w)
    assert pairs, "no office-holder lives under a settlement with a cohort; the falsifier is vacuous"
    for _holder, _cohort, rung in pairs:
        need, got = world_q.demanded(w, rung), world_q.delivered(w, rung)
        assert need and any(need[k] > got.get(k, 0) for k in need), f"{rung} is not in dearth"
    before = {pid: p.body for pid, p in w.persons.items()}

    evs = _matter(w)

    fell = {c.subject for e in evs if e.kind == "body.changed" for c in e.changes}
    for holder, cohort, rung in pairs:
        assert w.persons[holder].body == before[holder], (
            f"{holder}, seated, under {rung} in dearth, lost body "
            f"({before[holder]} -> {w.persons[holder].body}): the lord is worrying about "
            "subsistence, which `ED-IN-0255` rules out")
        assert holder not in w._subsistence_shortfall
        assert w.persons[cohort].body < before[cohort], (
            f"{cohort}, the population of {rung}, is in the same dearth and its body did not move")
        assert w._subsistence_shortfall[cohort] == _want(w.persons[cohort].weight), (
            "the cohort's shortfall is not its whole weighted want on an empty ladder")
        lost = arm * sum(w._subsistence_shortfall[cohort].values())
        assert w.persons[cohort].body == max(0, before[cohort] - lost), (
            f"{cohort} fell {before[cohort]} -> {w.persons[cohort].body} at arm {arm}; the live "
            f"arm's arithmetic says {max(0, before[cohort] - lost)}")
    # NOT ONE INDIVIDUAL'S BODY MOVED, ANYWHERE; AND EVERY BODY THAT MOVED IS A COHORT'S.
    assert fell and fell <= set(_cohorts(w)), f"a body.changed about a non-cohort: {fell}"
    assert all(w.persons[pid].body == before[pid] for pid in w.persons if pid not in _cohorts(w))


def test_24f_control_at_the_shipped_body_step_no_body_moves_in_the_same_dearth():
    """THE PAIRED CONTROL: the same realm, the same first draw, the shipped `body_step` (`H-125`'s
    control arm). The cohorts are short and no body moves, so the fall above is `body_step`'s."""
    w = POP.build_realm(0)
    assert w.fixtures.get("body_step") == 0, "the shipped arm moved; `H-125` and this test disagree"
    before = {pid: p.body for pid, p in w.persons.items()}
    evs = _matter(w)
    assert set(w._subsistence_shortfall) == set(_cohorts(w)), "the dearth is not the same dearth"
    assert {pid: p.body for pid, p in w.persons.items()} == before
    # v9 SE-01: THE CONTROL ARM EMITS NOTHING (`loop/matter.py:255-258`'s fabricating-sweep defect,
    # one clock over): no body write, no death, and no band crossing anchored on any person.
    assert not [e for e in evs if e.kind in ("body.changed", "person.died")]
    crossed = [e for e in w.log if e.kind == "condition.band_crossed"
               and anchor_of(w, e) in w.persons]
    assert not crossed, f"the control arm published {len(crossed)} body crossing(s)"


# ======================================================================================
# 3 -- THE REBUILT DRAIN GUARD: a cohort draws real stock on the built realm
# ======================================================================================

def test_24f_drain_guard_a_cohort_draws_stock_on_the_built_realm_and_matter_is_conserved(
        monkeypatch):
    """`test_w8`'s non-vacuity guard, retired 2026-09-18 because the drain it observed was a DUKE
    hauling grain, REBUILT ON THE TERRITORIAL QUANTITY as that retirement's own comment asks. It
    observes the draw MATTER actually ran: `subsistence_draw` is wrapped, not re-called, so the
    record asserted on is the one the barrier derived its writes from.

    Two MATTER barriers on `build_realm(0)`: the first takes the yield (its draw finds nothing, the
    dearth above), the second draws from that stock. The guard asserts it observed at least one
    cohort drawing (`take > 0`), that nobody else drew, and that the realm's matter after the second
    barrier is exactly `before - drawn + produced` -- so the draw moved real units out of real
    larders, not merely a number in a record."""
    w = POP.build_realm(0)
    _matter(w)
    w.tick += 1
    seen: list = []
    real = world_q.subsistence_draw

    def recording(w_):
        rec = real(w_)
        seen.append(rec)
        return rec

    monkeypatch.setattr(world_q, "subsistence_draw", recording)
    held_before = sum(sum((r.stores or {}).values()) for r in w.rungs.values())

    evs = _matter(w)

    assert len(seen) == 1, f"MATTER drew {len(seen)} times in one barrier"
    (record,) = seen
    drawing = {pid: sum(cell[1] for cell in row.values())
               for pid, (_h, row) in record.items() if any(cell[1] > 0 for cell in row.values())}
    assert len(drawing) >= 1, (
        "NO COHORT DREW on the built realm -- the territorial subsistence pass is inert, which is "
        "the dead-on-arrival case this guard exists for")
    assert set(record) <= set(_cohorts(w)), f"an individual drew: {sorted(set(record) - set(_cohorts(w)))}"
    # WHAT THIS BARRIER PRODUCED: the `yield` of every rung it emitted `yield.taken` about. A rung
    # that produced nothing this barrier keeps an older `yield`, so the field is read only where the
    # barrier wrote it. Nothing else in MATTER moves a store (a `transfer` or `levy` is RESOLVE's).
    took = {c.subject for e in evs if e.kind == "yield.taken" for c in e.changes}
    assert took, "no rung produced in the second barrier; the conservation check would be partial"
    produced = sum(sum((getattr(w.rungs[r], "yield") or {}).values()) for r in took)
    held_after = sum(sum((r.stores or {}).values()) for r in w.rungs.values())
    assert held_after == held_before - sum(drawing.values()) + produced, (
        f"matter is not conserved across the draw: {held_before} held, {sum(drawing.values())} "
        f"drawn, {produced} produced, {held_after} held after")
    # AND THE REALM IS IN SURPLUS ON ITS SECOND DRAW: every cohort is fed in full, so no larder ran
    # dry with a mouth unfed and no write carries a shortfall (`19d`'s record; its first draw found
    # no stock at all, which `loop/matter.py` states is silent).
    assert all(cell[1] == cell[0] for _p, (_h, row) in record.items() for cell in row.values()), (
        "a cohort went short on the realm's second draw -- the realm is no longer in surplus")
    assert not [o for e in evs for o in e.observed
                if str(o.predicate).partition(":")[0] == SHORTFALL_PREDICATE]


# ======================================================================================
# 4 -- v9 SE-01 (`24g`): the person-keyed crossing, P3's demand, and the carrier's owners
# ======================================================================================

def test_se01_a_person_keyed_crossing_is_placed_at_the_person_s_parent():
    """P1's OTHER HALF, EXECUTED. A cohort's body crossing is anchored on the cohort (tier 3, through
    its own `body.changed`), and `place_of` -- the one owner `_ch_co_located` reads -- answers the
    cohort's `contain` PARENT, `parent_of(w, who)`, never the cohort's own same-id `person` rung
    (where `presence` is *nobody*). So a bystander standing in the same settlement is co-located
    with the crossing and a person standing elsewhere is not. Run at the live arm that crosses the
    first floor in one season (`H-125`'s cite: *"`67` crosses it in one"*), found rather than named.

    The bystander is PLANTED, because on the realm as built no named person's `contain` parent is
    a settlement that seats a cohort; a test-built person standing there is the observer the
    channel needs, and it eats nothing (weight 1)."""
    w = POP.build_realm(0)
    cohort = sorted(_cohorts(w))[0]
    at = world_q.parent_of(w, cohort)
    assert at is not None and at != cohort and at in w.rungs
    w.persons["p_se01_bystander"] = Person("p_se01_bystander", "a bystander")
    w.rungs["p_se01_bystander"] = Rung("p_se01_bystander", "person")
    w.add_tenure(Tenure("t_se01_bystander_in", "p_se01_bystander", at, "contain", 0))
    elsewhere = next(pid for pid in sorted(w.persons)
                     if not w.persons[pid].is_cohort and world_q.place_of(w, pid) not in (None, at))
    scale = w.fixtures.get("condition_scale")
    floor = w.fixtures.get("band_floors")["body"]["full_operations"]
    arm = next((a for a in sorted(LIVE_ARMS)
                if scale - a * sum(_want(w.persons[cohort].weight).values()) < floor), None)
    assert arm is not None, f"no live arm of {LIVE_ARMS} crosses a floor in one season"
    w.fixtures = w.fixtures.sweep("body_step", arm)

    _matter(w)

    mine = [e for e in w.log if e.kind == "condition.band_crossed" and anchor_of(w, e) == cohort]
    assert mine, f"{cohort} crossed no band at arm {arm}; the test observes nothing"
    for e in mine:
        assert world_q.place_of(w, anchor_of(w, e)) == at, "the crossing is not at the parent"
        assert _ch_co_located(w, e, "p_se01_bystander"), (
            "a person standing where the cohort stands did not see its crossing -- the `presence` "
            "branch is closed for a PERSON-keyed crossing")
        assert not _ch_co_located(w, e, elsewhere), f"{elsewhere}, elsewhere, saw it"


def _dispatching(w, subject, actor="p_high", via="off_duke"):
    """A chooser that issues ONE `dispatch` naming `subject`, in the first season only."""
    sent: list = []

    def choose(p, v, s, ask_budget):
        if p.id == actor and not sent:
            a = P.Act_(w, p, "dispatch", payload=subject if not isinstance(subject, str)
                       else {"subject": subject}, via=via)
            sent.append(a)
            return [a]
        return []
    return choose, sent


def test_se01_a_dispatch_to_a_clerk_nobody_individuated_demands_him_and_census_mints_him():
    """THE EXIT, VERBATIM: *"a `dispatch` to a non-existent clerk emits `person.demanded` and,
    next season, a Person exists whose `person.individuated` cites it"*. The demand is the act's
    own refusal (it cites the act); the individuation cites the demand; the Person stands where
    the order was given (`place_of` of the dispatcher), with its `person` rung, at weight 1, and he
    is still there a season later. (A repeated order is not run here: the chooser sends once.)"""
    w = P.tiny_world()
    assert "p_clerk" not in w.persons and w.class_of("p_clerk") is None
    choose, sent = _dispatching(w, "p_clerk")
    P._run(w, choose)
    (act,) = sent
    demanded = [e for e in w.log if e.kind == "person.demanded"]
    assert len(demanded) == 1, f"{len(demanded)} demands for one dispatch"
    (dem,) = demanded
    assert dem.causes[0] == act.id, "the demand does not cite the act that made it"
    assert [e.kind for e in w.log if act.id in e.causes[:1]] == ["dispatch.refused",
                                                                 "person.demanded"]
    born = [e for e in w.log if e.kind == "person.individuated"]
    assert len(born) == 1 and born[0].causes == [dem.id], (
        f"the individuation does not cite the demand: {[(e.kind, e.causes) for e in born]}")
    # NEXT SEASON, A PERSON EXISTS.
    assert "p_clerk" in w.persons and w.persons["p_clerk"].weight == 1
    assert w.rungs["p_clerk"].kind == "person"
    assert world_q.place_of(w, "p_clerk") == world_q.place_of(w, "p_high") == "S"
    P._run(w, choose)
    assert "p_clerk" in w.persons, "the individuated clerk did not survive his first season"
    assert len([e for e in w.log if e.kind == "person.individuated"]) == 1


@pytest.mark.parametrize("subject, actor, via", [
    ("site_harbour", "p_high", "off_duke"),   # an id the world holds as a SITE: not a person
    ("S", "p_high", "off_duke"),              # an id the world holds as a RUNG
    ("p_mid", "p_high", "off_duke"),          # a person who exists: the order is GIVEN
    ("p_clerk", "p_low", None),               # an unheld id, but the actor holds no remit
    ({}, "p_high", "off_duke"),               # an order naming nobody (probe P9's payload shape)
])
def test_se01_control_a_dispatch_that_asks_for_no_absent_person_demands_nobody(subject, actor, via):
    """THE CONTROL ARMS OF THE DEMAND: every other way a dispatch ends emits no `person.demanded`
    and individuates nobody. The 14 refusals measured on the shipped realm (a dispatch naming a
    building, a site or a record) are the first two rows' case; an ineligible actor is refused
    before he asks the world anything."""
    w = P.tiny_world()
    persons = set(w.persons)
    choose, sent = _dispatching(w, subject, actor=actor, via=via)
    P._run(w, choose)
    assert sent, "the dispatch was never issued; the control observes nothing"
    assert not [e for e in w.log if e.kind in ("person.demanded", "person.individuated")]
    assert set(w.persons) == persons


def test_se01_control_a_date_the_world_already_holds_is_not_a_clerk_to_individuate():
    """B-F CLOSE: `class_of` has no `dates`, so a dispatch naming a convened date's id passed
    "unheld" and CENSUS would have minted a Person under it (and `place_of`, which checks persons
    first, would then have placed the date at the dispatcher's hearth)."""
    w = P.tiny_world()
    w.dates["d_se01_assembly"] = {"venue": "S"}
    assert w.class_of("d_se01_assembly") is None, "the control needs an id class_of cannot see"
    persons = set(w.persons)
    choose, sent = _dispatching(w, "d_se01_assembly")
    P._run(w, choose)
    assert sent, "the dispatch was never issued; the control observes nothing"
    assert not [e for e in w.log if e.kind in ("person.demanded", "person.individuated")]
    assert set(w.persons) == persons and "d_se01_assembly" not in w.rungs


def test_se01_control_a_person_who_died_is_not_a_clerk_to_individuate_again():
    """B-F CLOSE: `remove_person` pops the Person and its rung, so a dispatch to the dead id passed
    "unheld" and CENSUS would have re-minted him at full body with `person.died` already logged
    (the defect `World.remove_person` records as *the dead stayed referenceable*). The death is
    written through the real MATTER gate, as `loop/matter.py` writes it."""
    w = P.tiny_world()
    w.step = Step.MATTER
    w.write("exists", mint_token(w, WriteClass.MATTER), lambda: w.remove_person("p_other"),
            record_kind="Person", fieldname="exists", driver="Event", emits="person.died",
            subject="p_other", causes=[ROOT])
    assert "p_other" not in w.persons and w.class_of("p_other") is None
    assert [e.kind for e in w.log if e.kind == "person.died"], "the death was never logged"
    choose, sent = _dispatching(w, "p_other")
    P._run(w, choose)
    assert sent, "the dispatch was never issued; the control observes nothing"
    assert not [e for e in w.log if e.kind in ("person.demanded", "person.individuated")]
    assert "p_other" not in w.persons


# --------------------------------------------------------------------------------------
# THE CARRIED FALSIFIER: `Person.weight` / the envelope written by anything but CENSUS/MATTER
# fails; a stored aggregate where a Query is required fails.
# --------------------------------------------------------------------------------------

_SEASON = Path(__file__).resolve().parents[1]
_OWNED = {"weight": {"loop/census.py"},               # write_matrix.yaml: `weight` steps [CEN] only
          "envelope": {"loop/census.py", "loop/matter.py",
                       # WORLD-GEN, NOT A STEP: probe `W9` seeds its `tiny_world`'s envelope before
                       # any season runs, and then moves it through the gate at MATTER. Seeding a
                       # fixture world is the builder's (as `seat_cohorts` passes `weight=`).
                       # Shrink-only.
                       "harness/probes.py"}}


def _bare_writes(src: str, rel: str) -> list:
    """Every assignment to `.weight`/`.envelope`, and every `setattr`/`__setattr__` naming one, in
    `src` -- the read/write asymmetry's WRITE side (`CLAUDE.md` §0.1 pt 1): a writer outside the
    owners would move the carrier the Queries read without passing the step that owns it."""
    out = []
    for n in ast.walk(ast.parse(src, rel)):
        targets = (n.targets if isinstance(n, ast.Assign)
                   else [n.target] if isinstance(n, (ast.AugAssign, ast.AnnAssign)) else [])
        for t in targets:
            if isinstance(t, ast.Attribute) and t.attr in _OWNED:
                out.append((rel, n.lineno, t.attr))
        if isinstance(n, ast.Call) and len(n.args) >= 2:
            f = n.func
            name = f.id if isinstance(f, ast.Name) else f.attr if isinstance(f, ast.Attribute) else ""
            a1 = n.args[1]
            if (name in ("setattr", "__setattr__") and isinstance(a1, ast.Constant)
                    and a1.value in _OWNED):
                out.append((rel, n.lineno, a1.value))
    return [x for x in out if x[0] not in _OWNED[x[2]]]


def test_se01_falsifier_no_module_but_census_or_matter_writes_weight_or_the_envelope():
    """THE SWEEP, AND ITS PLANTED FAILURE. Over every non-test module under `engine/season`, no
    bare write to `Person.weight` or `Rung.envelope` stands outside `loop/census.py` and
    `loop/matter.py`. A write planted in a THIRD module (`loop/resolve.py`) must be found, in both
    spellings -- otherwise the clean sweep would be the sweep that cannot see."""
    scanned = 0
    found = []
    for path in sorted(_SEASON.rglob("*.py")):
        rel = path.relative_to(_SEASON).as_posix()
        if rel.startswith("tests/"):
            continue
        scanned += 1
        found += _bare_writes(path.read_text(), rel)
    assert scanned >= 50, f"the sweep read {scanned} modules; it is not reading the tree"
    assert not found, f"a bare write outside CENSUS/MATTER: {found}"
    planted = ("def _eff(w, p, r):\n    p.weight = 40\n"
               "    setattr(r, 'envelope', [1])\n")
    assert _bare_writes(planted, "loop/resolve.py") == [
        ("loop/resolve.py", 2, "weight"), ("loop/resolve.py", 3, "envelope")]
    assert _bare_writes(planted, "loop/census.py") == [], "an owner's write was flagged"


@pytest.mark.parametrize("kind, field, value", [("Person", "weight", 40),
                                                ("Rung", "envelope", [1])])
def test_se01_falsifier_the_gate_refuses_weight_and_the_envelope_at_resolve(kind, field, value):
    """THE GATE HALF: a write of `(Person, weight)` or `(Rung, envelope)` at RESOLVE is FORBIDDEN by
    the write matrix (`weight` is `[CEN]`, `envelope` `[MAT, CEN]`), and the carrier is untouched.
    ⚠ THE TWO ARMS DIFFER IN THE STEP ALONE: the same MATTER token, driver, emission and subject, so
    only the matrix's step check can have refused the first (an ACTS token at RESOLVE would also be
    refused by the class check, and deleting the step check would leave that test green)."""
    w = P.tiny_world()
    rec = w.persons["p_mid"] if kind == "Person" else w.rungs["S"]
    was = getattr(rec, field)

    def write():
        w.write(field, mint_token(w, WriteClass.MATTER), lambda: setattr(rec, field, value),
                record_kind=kind, fieldname=field, driver="Event",
                emits=f"{field}.changed", subject=rec.id, causes=[ROOT])

    w.step = Step.RESOLVE
    with pytest.raises(Forbidden):
        write()
    assert getattr(rec, field) == was, "a refused write moved the carrier"
    w.step = Step.CENSUS
    write()
    assert getattr(rec, field) == value


def test_se01_falsifier_a_stored_aggregate_on_a_rung_is_refused(realm):
    """*"A stored aggregate where a Query is required fails"*: a settlement's population is
    `world_q.population`, a Query, and storing it on the Rung raises (S10.1 / L3) rather than
    standing beside the Query as a second answer that can go stale. (A refused write mutates
    nothing, so the module's shared read-only realm serves.)"""
    w = realm
    rung = world_q.parent_of(w, sorted(_cohorts(w))[0])
    assert world_q.population(w, rung) >= 1
    with pytest.raises(ShapeGap):
        w.rungs[rung].population = world_q.population(w, rung)
    assert not hasattr(w.rungs[rung], "population")
