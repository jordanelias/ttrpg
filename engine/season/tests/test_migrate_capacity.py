"""Plan position `19c` -- MIGRATE, carrying `24d-ii`'s `capacity`, and the `travel_leg` ride-along.
`workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md` "19c — MIGRATE" and "24d-ii —
CAPACITY"; the ruling is `RULINGS.yaml` RR-2 (*"must be able to build hearths and accept people who
move settlements"*; *"migration is a verb persons take"*).

What the position built, each asked of the real fold, the real MATTER barrier and the real gate:
  * THE RIDE-ALONG: a `travel_leg` ends at the next MATTER (`loop/matter.py`'s travel pass), the
    `MAT` half of `(Person, travel_leg)`'s `steps: [MAT, RES]`, emitting `travel.ended`. Before it
    nothing emptied the list and `decision/budget.py` charged every past leg in every season.

THE FALSIFIERS (the plan's own), and the control each carries:
  * after N moves and the legs' end, `len(travel_leg)` is 0 -- and the budget penalty is back to 0.
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


def test_19c_a_migrate_from_chain_a_to_chain_b_changes_residence_and_a_move_does_not():
    """The plan's OBSERVABLE, on the governance spine's two disjoint chains: *a `migrate` from chain
    `a` to chain `b` changes residence; a `move` does not* -- and the plan's falsifier *a `move`
    leaves `residence` unchanged*, asserted on the SAME person, destination and world, so the verb is
    the only difference. The `move` re-homes presence and leaves the `reside` edge where it was; the
    `migrate` then re-homes residence, closing the old edge in the same write (exactly one live
    `reside` after, and the old one's `until` is this tick)."""
    from ..harness import governance_spine as G
    from ..queries import world_q
    w, d = _world(lambda: G.build(0))
    who, home, there = "lp_hearth_a", "lr_hearth_a", "lr_hearth_b"
    assert world_q.residence_of(w)[who] == world_q.home_of(w)[who] == home

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
    admitted -- so each refusal is its clause's and not the verb's."""
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
    ok = _fold(w, d, Act(id="ok", actor=who, verb="migrate", payload={"to": "lr_settlement_a"}))
    assert _kinds(ok) == ["residence.changed"], _kinds(ok)
