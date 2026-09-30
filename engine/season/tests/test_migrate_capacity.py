"""Plan position `19c` -- MIGRATE, carrying `24d-ii`'s `capacity`, and the `travel_leg` ride-along.
`workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md` "19c — MIGRATE" and "24d-ii —
CAPACITY"; the ruling is `RULINGS.yaml` RR-2 (*"must be able to build hearths and accept people who
move settlements"*; *"migration is a verb persons take"*).

What the position built, each asked of the real fold, the real MATTER barrier and the real gate:
  * THE RIDE-ALONG: a `travel_leg` ends at the next MATTER (`loop/matter.py`'s travel pass), the
    `MAT` half of `(Person, travel_leg)`'s `steps: [MAT, RES]`, emitting `travel.ended`. Before it
    nothing emptied the list and `decision/budget.py` charged every past leg in every season.
  * THE SPLIT: `contain` is where a person IS; `reside` (a Tenure kind, one live per person, minted
    by every builder) is where he LIVES. `move` re-homes the first and leaves the second; `migrate`
    makes the same journey and re-homes both (`loop/effects.py::_eff_migrate` argues the carrier).
  * `24d-ii`'s `capacity` -- `max(floor, the dwelling Sites at the rung and below)`, the floor on
    `rosters.yaml: capacity_floor` (`H-167`) -- landed with its first caller, `migrate`'s throttle:
    a NEWCOMER whose weight would take `population` past `capacity` is refused.

THE FALSIFIERS (the plan's own), and the control each carries:
  * after N moves and the legs' end, `len(travel_leg)` is 0 -- and the budget penalty is back to 0;
  * a `migrate` from chain `a` to chain `b` of the spine changes residence; a `move` does not;
  * a `migrate` into a rung at capacity refuses -- and the same act is admitted once a dwelling is
    BUILT there (RR-2's lever), while a `move` into the full rung is never refused;
  * a rung with no dwelling reads exactly the floor, never 0 (and the sweep reaches it); one more
    dwelling raises its capacity and every ancestor's by one; `capacity(` has a caller outside tests.
Every one was mutation-checked at the build (the throttle removed, the floor dropped, the count cut
to the rung's own Sites, the newcomer rule removed, population counted by presence): each went red.
"""

from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import WriteClass
from ..decision import budget
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..state.carriers import Act

TRAVELLER, STAYER = "p_low", "p_mid"          # both in `Hh` at build; only the first travels


def _world(builder=P.tiny_world, **fx):
    """`builder()` at the given fixture arms, its tick-0 MATTER barrier run."""
    fixtures = DEFAULT_FIXTURES
    for name, value in fx.items():
        fixtures = fixtures.sweep(name, value)
    w = builder(fixtures) if builder is P.tiny_world else builder()
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _fold(w, d, *acts):
    """One RESOLVE pass, its Events logged as `season` logs them."""
    out = d.resolve(mint_token(w, WriteClass.ACTS), list(acts),
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    w.log.extend(out)
    return out


def _season(w, d):
    """The next season's MATTER barrier and nothing else: the tick advances, MATTER runs."""
    w.tick += 1
    return d.matter(mint_token(w, WriteClass.MATTER), [])


def _kinds(events):
    return [e.kind for e in events]


def _move(key, to, actor=TRAVELLER):
    return Act(id=key, actor=actor, verb="move", payload={"to": to})


# ======================================================================================
# 1 -- THE RIDE-ALONG: A LEG ENDS AT THE NEXT MATTER
# ======================================================================================

def test_19c_after_n_moves_the_legs_end_at_the_next_matter_and_the_penalty_returns_to_zero():
    """The plan's falsifier, *after N moves and the legs' end, `len(travel_leg)` is 0*, with the
    budget read BOTH sides of the end so the fix is observed where the defect bit (a write nobody
    reads would pass the length half alone -- `CLAUDE.md` §0.1 pt 1).

    Two moves in one season (`Hh` -> `S` -> `D`, each a strict ascent from a person-rung) lay two
    legs and cost two scenes; the next MATTER ends both in ONE write, emitting ONE `travel.ended`
    whose cause is the second move's `travel.moved` -- so the walk runs back to the act. CONTROLS:
    the person who never moved emits no `travel.ended` and keeps the full budget throughout; and the
    leg's end is not a return -- the traveller is still contained where the last leg took him."""
    w, d = _world()
    fx, k = w.fixtures, 5
    base = budget(w.persons[TRAVELLER], None, k, fx)
    assert base == budget(w.persons[STAYER], None, k, fx), "the two start unequal"
    first = _fold(w, d, _move("m1", "S"))
    second = _fold(w, d, _move("m2", "D"))
    assert _kinds(first) == _kinds(second) == ["travel.moved"], (_kinds(first), _kinds(second))
    traveller = w.persons[TRAVELLER]
    n = len(traveller.travel_leg)
    assert n == 2, traveller.travel_leg
    assert budget(traveller, None, k, fx) == base - n * fx.get("budget_leg_penalty") < base

    ended = [e for e in _season(w, d) if e.kind == "travel.ended"]
    assert traveller.travel_leg == [], traveller.travel_leg
    assert budget(traveller, None, k, fx) == base, "the distance penalty outlived its leg"
    assert len(ended) == 1, [e.kind for e in ended]
    assert ended[0].causes == [second[0].id], (ended[0].causes, second[0].id)
    assert budget(w.persons[STAYER], None, k, fx) == base
    home = next(t.object for t in traveller.tenures if t.kind == "contain" and t.live)
    assert home == "D", home

    # ... and a season with no move ends nothing: the pass is keyed on a leg, not on a person.
    assert not [e for e in _season(w, d) if e.kind == "travel.ended"]


# ======================================================================================
# 2 -- RESIDENCE: EVERY BUILDER MINTS IT, `move` LEAVES IT, `migrate` RE-HOMES IT
# ======================================================================================

def _live(w, pid, kind):
    return [t for t in w.tenures if t.subject == pid and t.kind == kind and t.live]


def test_19c_every_builder_houses_every_person_where_he_stands():
    """`world_q.residence_of` reads ONE edge kind and never falls back to presence (its docstring),
    so a builder that forgot to mint would leave its people of no fixed abode -- and a `population`
    of zero under every rung. Asserted over every builder the season engine ships, with the person
    count `>= 1` so an empty world cannot pass, and residence EQUAL to presence at build: the two
    diverge only when somebody travels."""
    from ..harness import corpus_run as C, governance_spine as G, headless as HL, populated
    from ..harness import run_cases as R, scarce
    from ..queries import world_q
    case = next(c for c in R.load_cases("NPC") if str(c.get("scale")) == "person")
    for name, w in (("tiny_world", P.tiny_world()), ("spine", G.build(0)),
                    ("realm", populated.build_realm(0)), ("headless", HL.build_world(0)),
                    ("scarce", scarce.build(0)), ("corpus", C.build_at(case, 0))):
        lives, stands = world_q.residence_of(w), world_q.home_of(w)
        assert len(w.persons) >= 1 and set(lives) == set(w.persons), (name, sorted(w.persons))
        assert lives == stands, (name, {p: (lives.get(p), stands.get(p)) for p in w.persons
                                        if lives.get(p) != stands.get(p)})


def _build_dwelling(w, d, at, by, key="wd"):
    """A dwelling STOOD at `at` by the real acts `24e` built -- `create_record` of a works planning a
    `dwelling` there (its maker's `hold` minted with it), then `build` by the works' holder -- so the
    capacity a test reads was raised the way RR-2 says it rises (*"`found` is the throttle"*: the
    lever that lifts the bound), not planted."""
    made = _fold(w, d, Act(id=key, actor=by, verb="create_record",
                           payload={"record": key, "kind": "works",
                                    "subject_matter": {"plan": "dwelling", "at": at}, "rung": at,
                                    "stages": [(w.tick + 1, "term1", key)]}))
    built = _fold(w, d, Act(id=f"{key}:b", actor=by, verb="build", payload={"subject": key}))
    assert _kinds(made) == ["record.created"] and _kinds(built) == ["site.built"], (
        _kinds(made), _kinds(built))


def test_19c_a_migrate_from_chain_a_to_chain_b_changes_residence_and_a_move_does_not():
    """The plan's OBSERVABLE, on the governance spine's two disjoint chains: *a `migrate` from chain
    `a` to chain `b` changes residence; a `move` does not* -- and the plan's falsifier *a `move`
    leaves `residence` unchanged*, asserted on the SAME person, destination and world, so the verb is
    the only difference. The `move` re-homes presence and leaves the `reside` edge where it was; the
    `migrate` then re-homes residence, closing the old edge in the same write (exactly one live
    `reside` after, and the old one's `until` is this tick). `lr_hearth_b` is given room first -- a
    second dwelling, BUILT (section 3 is the refusal without it)."""
    from ..harness import governance_spine as G
    from ..queries import world_q
    w, d = _world(lambda: G.build(0))
    who, home, there = "lp_hearth_a", "lr_hearth_a", "lr_hearth_b"
    assert world_q.residence_of(w)[who] == world_q.home_of(w)[who] == home
    _build_dwelling(w, d, there, by="lp_hearth_b")
    assert world_q.population(w, there) + 1 <= world_q.capacity(w, there) == 2

    moved = _fold(w, d, _move("mv", there, actor=who))
    assert _kinds(moved) == ["travel.moved"], _kinds(moved)
    assert world_q.home_of(w)[who] == there, "the move did not re-home presence"
    assert world_q.residence_of(w)[who] == home, "a `move` changed where he lives"

    settled = _fold(w, d, Act(id="mg", actor=who, verb="migrate", payload={"to": there}))
    assert _kinds(settled) == ["residence.changed"], _kinds(settled)
    assert world_q.residence_of(w)[who] == there and world_q.home_of(w)[who] == there
    live = _live(w, who, world_q.RESIDE_KIND)
    assert [t.object for t in live] == [there], live
    ended = [t for t in w.tenures if t.subject == who and t.kind == world_q.RESIDE_KIND
             and not t.live]
    assert [(t.object, t.until) for t in ended] == [(home, w.tick)], ended
    assert w.persons[who].travel_leg == [there, there], "a migration is a journey too"


def test_19c_a_migrate_declines_where_it_changes_no_residence_and_where_the_ladder_refuses():
    """The effect's two declines, each emitting the `write` clause's `migrate.refused` and writing
    nothing: a migrant who already lives at the destination (a migration that changes no residence
    is none -- `H-140`'s shape, answered for this verb), and a destination the §10 ladder will not
    seat him in (a sibling PERSON-rung, `move`'s own decline). And the `path` clause, which emits
    `move`'s `travel.blocked` because it is the same fact: a destination with no containment path.
    CONTROL: the same migrant, the same fold, a destination he does not live in and can reach, is
    admitted -- so each refusal is its clause's and not the verb's. The control is ALSO the throttle's
    newcomer rule: `lr_settlement_a` is over capacity (three live under it, one dwelling), and he is
    one of the three, so settling there grows nothing and nothing refuses it."""
    from ..harness import governance_spine as G
    from ..queries import world_q
    w, d = _world(lambda: G.build(0))
    who = "lp_hearth_a"
    before = (world_q.residence_of(w)[who], list(w.persons[who].travel_leg))
    for key, to, kind in (("same", "lr_hearth_a", "migrate.refused"),
                          ("sideways", "lp_hearth_b", "migrate.refused"),
                          ("nowhere", "ls_hearth_b_dwelling", "travel.blocked")):
        out = _fold(w, d, Act(id=key, actor=who, verb="migrate", payload={"to": to}))
        assert _kinds(out) == [kind], (key, _kinds(out))
        assert (world_q.residence_of(w)[who], list(w.persons[who].travel_leg)) == before, key
    town = "lr_settlement_a"
    assert world_q.population(w, town) == 3 > world_q.capacity(w, town) == 1
    ok = _fold(w, d, Act(id="ok", actor=who, verb="migrate", payload={"to": town}))
    assert _kinds(ok) == ["residence.changed"], _kinds(ok)
    assert world_q.population(w, town) == 3, "a settler already under the town changed its count"


# ======================================================================================
# 3 -- THE THROTTLE: A FULL RUNG REFUSES A NEWCOMER, AND BUILDING IS THE LEVER
# ======================================================================================

def test_19c_a_migrate_into_a_rung_at_capacity_refuses_and_a_built_dwelling_admits_it():
    """The plan's FALSIFIER, *a `migrate` into a rung at capacity refuses*, on the spine -- whose
    hearths carry one dwelling each (`24d-i`'s decision (4)), so the capacity half runs where the
    residence half does. `lr_hearth_b` houses one (`lp_hearth_b`) under one dwelling: FULL. A newcomer
    from chain `a` is refused with the `write` clause's kind, and nothing moves -- not his residence,
    not his presence, not his leg. Then RR-2's loop, closed: the hearth's own holder BUILDS a second
    dwelling (`24e`'s acts; `build` never consults capacity), the capacity rises by one, and the SAME
    act is admitted. CONTROL: a `move` into the full hearth is admitted before anything is built --
    presence fills no house, so the throttle is `migrate`'s alone."""
    from ..harness import governance_spine as G
    from ..queries import world_q
    w, d = _world(lambda: G.build(0))
    who, full = "lp_hearth_a", "lr_hearth_b"
    assert world_q.population(w, full) == world_q.capacity(w, full) == 1
    before = (world_q.residence_of(w)[who], world_q.home_of(w)[who], list(w.persons[who].travel_leg))
    refused = _fold(w, d, Act(id="mg1", actor=who, verb="migrate", payload={"to": full}))
    assert _kinds(refused) == ["migrate.refused"], _kinds(refused)
    assert (world_q.residence_of(w)[who], world_q.home_of(w)[who],
            list(w.persons[who].travel_leg)) == before

    visitor = _fold(w, d, _move("mv", full, actor="lp_settlement_a"))
    assert _kinds(visitor) == ["travel.moved"], "a full rung refused a visitor"
    assert world_q.population(w, full) == 1, "a visitor was counted as a resident"

    _build_dwelling(w, d, full, by="lp_hearth_b")
    assert world_q.capacity(w, full) == 2
    admitted = _fold(w, d, Act(id="mg2", actor=who, verb="migrate", payload={"to": full}))
    assert _kinds(admitted) == ["residence.changed"], _kinds(admitted)
    assert world_q.residence_of(w)[who] == full and world_q.population(w, full) == 2
    again = _fold(w, d, Act(id="mg3", actor="lp_community_a", verb="migrate", payload={"to": full}))
    assert _kinds(again) == ["migrate.refused"], "the second newcomer found room that was taken"


def test_19c_the_throttle_on_the_populated_realm_admits_an_empty_hearth_once():
    """The same falsifier on `populated.build_realm(0)`, the world the plan names for the capacity
    half: one dwelling per hearth, and most of the 211 hearths empty. A person migrating into an
    EMPTY hearth in another settlement is admitted (capacity 1, nobody living there); a second
    newcomer into the same hearth is refused (one lives there now, one dwelling); and a `move` there
    by the second is admitted and leaves his residence where it was."""
    from ..harness import populated
    from ..queries import world_q
    w, d = _world(lambda: populated.build_realm(0))
    lives = world_q.residence_of(w)
    first, second = sorted(lives)[:2]
    town_of = {p: world_q.ancestry(w, lives[p])[1] for p in (first, second)}
    empty = next(r for r, rung in sorted(w.rungs.items())
                 if rung.kind == "hearth" and world_q.population(w, r) == 0
                 and town_of[first] not in world_q.ancestry(w, r)
                 and town_of[second] not in world_q.ancestry(w, r))
    assert world_q.capacity(w, empty) == 1
    ok = _fold(w, d, Act(id="r1", actor=first, verb="migrate", payload={"to": empty}))
    assert _kinds(ok) == ["residence.changed"], _kinds(ok)
    no = _fold(w, d, Act(id="r2", actor=second, verb="migrate", payload={"to": empty}))
    assert _kinds(no) == ["migrate.refused"], _kinds(no)
    assert world_q.residence_of(w)[second] == lives[second]
    visit = _fold(w, d, _move("r3", empty, actor=second))
    assert _kinds(visit) == ["travel.moved"] and world_q.residence_of(w)[second] == lives[second]


# ======================================================================================
# 4 -- `capacity` (`24d-ii`): THE FLOOR, THE STEP, AND A CALLER
# ======================================================================================

def test_24d_ii_a_rung_with_no_dwelling_reads_exactly_the_floor_and_the_sweep_reaches_it():
    """`24d-ii`'s FALSIFIER: *a rung with zero dwellings returns exactly the floor, never 0* -- RR-2's
    stated reason for the floor. `tiny_world` stands no dwelling anywhere, so every rung's capacity
    IS the floor; and `H-167`'s three sweep arms are executed through `Fixtures.sweep`, so the floor is
    read through the fixture a sweep reaches (the `zero` arm is RR-2's refused reading, the control:
    a dwelling-less rung then houses nobody, and a newcomer is refused where the default admits)."""
    from ..queries import world_q
    for floor, expect in ((None, 1), (0, 0), (2, 2)):
        fx = {} if floor is None else {"capacity_floor": dict(DEFAULT_FIXTURES.get("capacity_floor"),
                                                              dwelling=floor)}
        w, d = _world(**fx)
        assert not [s for s in w.sites.values() if s.kind == world_q.DWELLING_KIND]
        for rung in ("Hh", "S", "D", "R"):
            assert world_q.capacity(w, rung) == expect, (floor, rung)
        # A hearth FOUNDED under `S` by `24e`'s acts: no dwelling, nobody living there. `p_king`
        # lives at `R`, above it, so he is a newcomer to it: the floor alone decides whether a
        # dwelling-less place can take anyone -- admitted at 1 and 2, refused at the control.
        made = _fold(w, d, Act(id="wf", actor="p_high", verb="create_record",
                               payload={"record": "wf", "kind": "works", "rung": "S",
                                        "subject_matter": {"plan": "hearth", "at": "S"},
                                        "stages": [(w.tick + 1, "term1", "wf")]}))
        founded = _fold(w, d, Act(id="f", actor="p_high", verb="found", payload={"subject": "wf"}))
        assert _kinds(made) == ["record.created"] and _kinds(founded) == ["rung.founded"]
        new = next(r for r in world_q.descendants(w, "S") if r.endswith(":wf"))
        assert world_q.capacity(w, new) == expect and world_q.population(w, new) == 0, floor
        out = _fold(w, d, Act(id="k", actor="p_king", verb="migrate", payload={"to": new}))
        want = "residence.changed" if expect >= 1 else "migrate.refused"
        assert _kinds(out) == [want], (floor, _kinds(out))


def test_24d_ii_one_more_dwelling_raises_capacity_at_the_rung_and_every_ancestor_by_one_step():
    """`24d-ii`'s FALSIFIER: *one more dwelling under a rung raises its capacity and every
    ancestor's by the same step* -- which is what makes the rung's OWN dwelling count (`descendants`
    excludes the rung; `capacity` unions it back in) and a count over the whole subtree. On the spine
    every rung of chain `b` holds `lr_hearth_b`'s dwelling, so each reads at least the floor by its
    Sites; one more BUILT at `lr_hearth_b` raises all seven of chain `b` and the realm by exactly one,
    and CONTROL -- chain `a`, which shares only the realm, does not move."""
    from ..harness import governance_spine as G
    from ..queries import world_q
    w, d = _world(lambda: G.build(0))
    chain_b = world_q.ancestry(w, "lr_hearth_b")
    chain_a = [r for r in world_q.ancestry(w, "lr_hearth_a") if r not in chain_b]
    assert len(chain_b) == 7 and len(chain_a) == 6, (chain_b, chain_a)
    before = {r: world_q.capacity(w, r) for r in chain_b + chain_a}
    _build_dwelling(w, d, "lr_hearth_b", by="lp_hearth_b")
    after = {r: world_q.capacity(w, r) for r in chain_b + chain_a}
    assert all(after[r] == before[r] + 1 for r in chain_b), (before, after)
    assert all(after[r] == before[r] for r in chain_a), (before, after)


def test_24d_ii_capacity_has_a_caller_outside_the_tests():
    """`24d-ii`'s third falsifier, *an AST check that `capacity(` has a caller outside `tests/`*
    (`ID-13`: a Query nobody calls is a declared row nobody reads). Parsed, not grepped, over every
    module of the season package except its tests and `world_q.py` itself (its own definition and
    docstring are not callers); and ANTI-VACUITY: the walk must reach `loop/effects.py`, the file the
    caller is in."""
    import ast
    from ..data import files
    callers, seen = [], set()
    for f in files.package_modules():
        if "tests" in f.parts or f.name == "world_q.py":
            continue
        seen.add(f.name)
        for node in ast.walk(ast.parse(f.read_text(encoding="utf-8"))):
            if isinstance(node, ast.Call) and (
                    (isinstance(node.func, ast.Name) and node.func.id == "capacity")
                    or (isinstance(node.func, ast.Attribute) and node.func.attr == "capacity")):
                callers.append(f.name)
    assert "effects.py" in seen, sorted(seen)
    assert "effects.py" in callers, f"`capacity` is called from nowhere outside the tests: {callers}"
