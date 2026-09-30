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

import pytest

from ..data.matrix import Step, WriteClass
from ..gaps import ShapeGap
from ..harness import populated as POP
from ..harness import probes as P
from ..harness.run_cases import load_cases
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Site

WEIGHTS = P.DEFAULT_FIXTURES.get("subsistence_weight")
# `H-125`'s sweep arms are `[0, 10, 67]` and `0` is the shipped control. The falsifier needs a body
# that CAN move, so it runs at the middle arm, the one `test_governance_build.py`'s starving world
# already uses -- never a new magnitude.
# [JUSTIFIED: an existing sweep arm of `H-125` (`body_step`), chosen so a body can move; not a new game value]
BODY_STEP_ARM = 10


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


def test_24f_falsifier_in_dearth_the_office_holder_keeps_his_body_and_the_cohort_does_not():
    """`_part2` 24f's FALSIFIER, verbatim: *"Under a non-zero `body_step` arm: a `weight == 1`
    office-holder at a rung in dearth keeps their body; a `weight > 1` cohort at the same rung draws
    and its body moves."* On the BUILT realm -- *"a guard that passes only on `probes.py:744` is the
    dead-on-arrival case above, passing"*.

    THE DEARTH IS THE REALM'S OWN, NOT PLANTED. At build every larder is empty and MATTER draws
    before it takes the first yield (#353 §25's order), so the first draw finds no stock anywhere:
    every settlement's `demanded` exceeds its `delivered`. Nothing here empties a store."""
    w = POP.build_realm(0)
    w.fixtures = w.fixtures.sweep("body_step", BODY_STEP_ARM)
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
    assert not [e for e in evs if e.kind in ("body.changed", "person.died")]


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
