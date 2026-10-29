"""Plan position `24e` -- WORKS & FOUNDING. `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`
"24e — WORKS & FOUNDING (P4)"; content owner r2 `proposals/2026-09-17-governance-and-holdings-r2/
04_MATTER_AND_WORKS.md` §A.6 and r2 item 12. Layer-1 gap answered: `architecture/meta/
04_CODE_ARCHITECTURE.md` F.20 -- *"the world only decays -- nothing is ever founded or built"*.

What the position built, each asked of the real fold, the real MATTER barrier and the real gate:
  * a `works` is a `Record` of kind `works` (`rosters.yaml: record_kinds`), `{plan, at}` -- *"a
    <plan> at <at>"* -- minted by the `create_record` that already ran, with its maker's `hold`;
    one live works per target, declined at that producer.
  * `queries/world_q.py::ceiling` -- the works' matured terms, counted off the log, bound how far its
    fabric may be raised; `share` divides a rise among those standing at the fabric.
  * `restore` has an effect (`_eff_restore`), and `work` advances a works (`_eff_work`), both through
    ONE rise (`_rise`) staged on G4's accumulator and clamped once under the ceiling.
  * `found` mints a Rung of the works' plan and its `contain` edge, admitted at the gate under a
    NINTH basis, `founding`; `build` mints a Site of the plan at condition 0.

THE FALSIFIERS (the plan's, as corrected 2026-09-25), and the control each carries:
  * a `text` Record is NOT advanced by `work` -- the same site, the same worker, the same fold; the
    only difference is the Record's kind.
  * a `found` then a `build` of a dwelling at a rung whose population fills its dwellings SUCCEEDS,
    and the dwelling count at that rung and at every ancestor rises by exactly one -- counted before
    and after, not read off the success Event.

The fixture is `probes.tiny_world`: `R` (realm) > `D` (duchy) > `S` (settlement) > `Hh` (hearth).
`site_harbour` (condition 900) and `site_seam` stand at `S`. `p_high` lives in `S` -- the one person
present at the harbour -- `p_low`, `p_mid`, `p_other` in `Hh`, `p_king` in `R`.
"""

from __future__ import annotations

import pytest

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import Step, WriteClass
from ..harness import probes as P
from ..loop.driver import SeasonDriver, mint_token
from ..queries import world_q
from ..state.carriers import Act

HARBOUR, SETTLEMENT, HEARTH = "site_harbour", "S", "Hh"
PRESENT, ABSENT = "p_high", "p_low"          # at `S`, the harbour's rung / at `Hh`, below it


def _world(**fx):
    """`tiny_world` at the given fixture arms, its tick-0 MATTER barrier run."""
    fixtures = DEFAULT_FIXTURES
    for name, value in fx.items():
        fixtures = fixtures.sweep(name, value)
    w = P.tiny_world(fixtures)
    d = SeasonDriver(w)
    d.matter(mint_token(w, WriteClass.MATTER), [])
    return w, d


def _fold(w, d, *acts):
    """One RESOLVE pass -- the staged clamp included -- its Events logged as `season` logs them."""
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


def _declare(w, d, key, plan, at, actor=ABSENT, terms=3, kind=world_q.WORKS_KIND):
    """`create_record` of a works planning a `plan` at `at`, its `terms` due one a season from the
    next -- the act declares its stages (§13.1), so the test does not lean on `H-80`'s default."""
    stages = [(w.tick + i + 1, f"term{i + 1}", key) for i in range(terms)]
    content = {"plan": plan, "at": at} if kind == world_q.WORKS_KIND else None
    return _fold(w, d, Act(id=key, actor=actor, verb="create_record",
                           payload={"record": key, "kind": kind, "subject_matter": content,
                                    "rung": at, "stages": stages}))


def _stock(w, rung, plan):
    """PLANTED: exactly the price of a `plan` (v9 IN-28, `rosters.yaml: works_cost`, read through the
    fixture), added to `rung`'s stores. `tiny_world` stocks grain only, so a works that BUILDS needs
    its timber planted, and each test says so where it does."""
    r = w.rungs[rung]
    r.stores = dict(r.stores or {})
    for kind, n in w.fixtures.get("works_cost")[plan].items():
        r.stores[kind] = r.stores.get(kind, 0) + n


def _ripen(w, d, n):
    """`n` MATTER barriers -- one declared term ripens at each, through the gate."""
    for _ in range(n):
        _season(w, d)


def _work(key, actor=ABSENT, site=HARBOUR):
    return Act(id=key, actor=actor, verb="work", payload={"site": site})


def _restore(key, actor=PRESENT, site=HARBOUR):
    return Act(id=key, actor=actor, verb="restore", payload={"site": site})


# ======================================================================================
# 1 -- A WORKS IS A RECORD, MINTED BY `create_record`, ONE LIVE PER TARGET
# ======================================================================================

def test_24e_a_works_is_a_record_minted_by_create_record_with_its_makers_hold():
    """r2 §A.6.2 moment 1: the `create_record` that already runs declares the works, and mints the
    maker's `hold` -- the edge that makes him its master and that MATTER asks before a term ripens."""
    w, d = _world()
    out = _declare(w, d, "wk", "harbour", SETTLEMENT)
    assert _kinds(out) == ["record.created"], _kinds(out)
    rec = w.records["wk"]
    assert rec.kind == world_q.WORKS_KIND and rec.subject_matter == {"plan": "harbour", "at": SETTLEMENT}
    assert world_q.hold_force(w, "wk").subject == ABSENT
    assert [r.id for r in world_q.works_for(w, SETTLEMENT, "harbour")] == ["wk"]


def test_24e_a_second_live_works_on_one_target_is_declined_and_a_dead_one_frees_it():
    """r2 §A.6.3's *one works per target*, kept at the producer: a second works planning the same
    thing at the same place is refused (the fold's `act.refused` -- `create_record` declares no kind
    of its own), because `ceiling` could not say which of two bounds the fabric. CONTROLS: another
    target mints; and once the first works' master lets it go (`release` of his own `hold`, T-m) it
    is no longer live, and the target is free."""
    w, d = _world()
    _declare(w, d, "wk1", "harbour", SETTLEMENT)
    second = _declare(w, d, "wk2", "harbour", SETTLEMENT, actor="p_mid")
    assert _kinds(second) == ["act.refused"] and "wk2" not in w.records, _kinds(second)
    other = _declare(w, d, "wk3", "seam", SETTLEMENT, actor="p_mid")
    assert _kinds(other) == ["record.created"] and "wk3" in w.records
    let_go = _fold(w, d, Act(id="rel", actor=ABSENT, verb="release", payload={"subject": "wk1"}))
    assert _kinds(let_go) == ["tenure.closed"], _kinds(let_go)
    assert world_q.works_for(w, SETTLEMENT, "harbour") == []
    again = _declare(w, d, "wk4", "harbour", SETTLEMENT, actor="p_mid")
    assert _kinds(again) == ["record.created"], _kinds(again)


# ======================================================================================
# 2 -- THE CEILING: RIPENED TERMS, COUNTED OFF THE LOG
# ======================================================================================

def test_24e_the_ceiling_rises_one_term_at_a_time_and_is_full_where_no_works_names_the_site():
    """`ceiling = scale x matured // declared`, the count read off `term.matured` Events (r2 §A.6.3
    DECIDED). Three terms: 0, 333, 666, 1000 across three barriers. CONTROL: the seam, which no
    works names, reads the full scale throughout; and a works on the harbour does not bound the seam."""
    w, d = _world()
    scale = w.fixtures.get("condition_scale")
    harbour, seam = w.sites[HARBOUR], w.sites["site_seam"]
    _declare(w, d, "wk", "harbour", SETTLEMENT)
    # A SECOND RECORD RIPENING ON THE SAME BARRIERS, so a count that forgot WHOSE term ripened
    # would read double: its `term.matured` Events must not lift the works' ceiling.
    _declare(w, d, "tx", None, None, actor="p_mid", kind="text")
    seen = [world_q.ceiling(w, harbour)]
    for _ in range(3):
        _season(w, d)
        seen.append(world_q.ceiling(w, harbour))
        assert world_q.ceiling(w, seam) == scale
    assert seen == [0, scale // 3, 2 * scale // 3, scale], seen
    assert world_q.matured_terms(w, "wk") == 3 == world_q.matured_terms(w, "tx")


def test_24e_the_share_is_one_over_the_persons_present_floored_at_one():
    """r2 `04` §A.6.4, RULED: `share = (1, n)`, `n` the persons standing at the fabric's rung, floored
    at one so a fabric nobody stands at is not divided by zero (v9 IN-07 E5: `settlements.fabric`'s
    share half). The probe moves the harbour's `rung` on a copy, so no world write is involved: the
    hearth holds three persons, the duchy none."""
    import dataclasses
    w, _d = _world()
    harbour = w.sites[HARBOUR]
    assert len(world_q.presence(w, "Hh")) == 3 and world_q.presence(w, "D") == []
    assert world_q.share(w, dataclasses.replace(harbour, rung="Hh")) == (1, 3)
    assert world_q.share(w, dataclasses.replace(harbour, rung="D")) == (1, 1)


def test_24e_a_works_whose_master_is_gone_bounds_nothing():
    """r2 §A.6.3: *a works with no master is not a bound* -- and MATTER stops ripening it
    (`loop/matter.py`: *a half-made copy STOPS*). The master dies -- MATTER's own death write, the
    cascade closing his `hold` (S15.3) -- so the harbour reads the full scale again, and the term
    due at that barrier does not ripen."""
    w, d = _world()
    _declare(w, d, "wk", "harbour", SETTLEMENT)
    assert world_q.ceiling(w, w.sites[HARBOUR]) == 0
    w.tick += 1
    w.step = Step.MATTER                     # MATTER's barrier: the one step that writes a death
    w.write("exists", mint_token(w, WriteClass.MATTER), lambda: w.remove_person(ABSENT),
            record_kind="Person", fieldname="exists", driver="Event",
            caused_person_exists=ABSENT, emits="person.died", subject=ABSENT, causes=["ROOT"])
    assert world_q.hold_force(w, "wk") is None
    assert world_q.ceiling(w, w.sites[HARBOUR]) == w.fixtures.get("condition_scale")
    d.matter(mint_token(w, WriteClass.MATTER), [])
    assert world_q.matured_terms(w, "wk") == 0


# ======================================================================================
# 3 -- `work` ADVANCES A WORKS; A TEXT RECORD IS NOT ADVANCED (THE PLAN'S CONTROL)
# ======================================================================================

@pytest.mark.parametrize("kind", [world_q.WORKS_KIND, "text"])
def test_24e_work_advances_a_works_and_a_text_record_is_not_advanced(kind):
    """THE PLAN'S FALSIFIER, BOTH ARMS FROM ONE BODY. The harbour at 500, two of three terms ripe
    (ceiling 666), one person standing at it: `work` by the maker raises it to exactly 666 --
    `(666 - 500) * 1 // 1`, the headroom over one share -- and emits `site.worked`. The SAME
    world with the Record declared `text` instead: the same act, the same site, and the harbour does
    not move -- `work.unavailable`, because no works names the site and the act declares no delta."""
    w, d = _world()
    scale = w.fixtures.get("condition_scale")
    _declare(w, d, "rec", "harbour", SETTLEMENT, kind=kind)
    _ripen(w, d, 2)
    harbour = w.sites[HARBOUR]
    harbour.condition = 500                  # planted: a fabric below its ceiling
    assert len(world_q.presence(w, SETTLEMENT)) == 1
    out = _fold(w, d, _work("wa"))
    if kind == world_q.WORKS_KIND:
        assert _kinds(out) == ["site.worked"], _kinds(out)
        assert harbour.condition == 2 * scale // 3 == 666, harbour.condition
    else:
        assert _kinds(out) == ["work.unavailable"], _kinds(out)
        assert harbour.condition == 500


def test_24e_work_on_a_site_of_another_kind_at_the_works_rung_is_not_advanced():
    """A works names a site by KIND at its rung (`works_for`): a harbour works does not advance the
    seam standing beside it. The seam at 100 (its floor, so `work`'s precondition admits) stays."""
    w, d = _world()
    _declare(w, d, "wk", "harbour", SETTLEMENT)
    _ripen(w, d, 3)
    seam = w.sites["site_seam"]
    seam.condition = 100
    out = _fold(w, d, _work("ws", site="site_seam"))
    assert _kinds(out) == ["work.unavailable"] and seam.condition == 100, (_kinds(out), seam.condition)


def test_24e_the_declared_delta_still_wins_and_the_ceiling_bounds_its_rise_but_never_cuts():
    """`H-94`'s hand-built channel is unchanged -- an act declaring its own delta stages exactly that
    -- and it now meets the ceiling at the clamp. The harbour at 900 under a works with no term ripe
    (ceiling 0): a declared +5 moves nothing (the rise is bounded) and the harbour is NOT dropped to
    the ceiling (`max(condition, ceiling)`; r2's bare `min(ceiling, ...)` would have taken it to 0).
    CONTROL: the same act with no works reaches 905."""
    from ..state.carriers import StateChange
    for with_works, expect, kinds in ((True, 900, ["work.unavailable"]), (False, 905, ["site.worked"])):
        w, d = _world()
        if with_works:
            _declare(w, d, "wk", "harbour", SETTLEMENT)
        harbour = w.sites[HARBOUR]
        harbour.condition = 900
        out = _fold(w, d, Act(id="wd", actor=ABSENT, verb="work", payload={"site": HARBOUR},
                              changes=[StateChange(HARBOUR, "alter", "Act", "condition", 5)]))
        assert _kinds(out) == kinds and harbour.condition == expect, (with_works, _kinds(out),
                                                                        harbour.condition)


# ======================================================================================
# 4 -- `restore`: BUILDING AND REPAIRING ARE ONE ACT AT DIFFERENT BANDS
# ======================================================================================

def test_24e_restore_repairs_a_fabric_no_works_names_to_full():
    """No works: the ceiling is the full scale, so `restore` by the one person standing at the
    harbour takes it from 500 to 1000 -- the whole headroom over one share. `site.restored`."""
    w, d = _world()
    harbour = w.sites[HARBOUR]
    harbour.condition = 500
    out = _fold(w, d, _restore("r1"))
    assert _kinds(out) == ["site.restored"], _kinds(out)
    assert harbour.condition == w.fixtures.get("condition_scale")


def test_24e_restore_needs_presence_and_is_refused_elsewhere():
    """The row's own cell -- *the actor is present at it* -- decides now that the effect exists:
    `p_low` lives in `Hh`, below the harbour's rung, and is refused; the harbour does not move."""
    w, d = _world()
    harbour = w.sites[HARBOUR]
    harbour.condition = 500
    out = _fold(w, d, _restore("r1", actor=ABSENT))
    assert _kinds(out) == ["restore.refused"] and harbour.condition == 500, _kinds(out)


def test_24e_restore_is_shared_among_those_standing_at_the_fabric_and_the_sum_commutes():
    """`share` is one over those present (r2 §A.6.4, the commons): with two standing at `S`, each
    stages half the headroom and the one clamp lands the whole of it. Folded in BOTH orders, the
    harbour ends at the same condition -- sum-then-clamp-once, S27.3."""
    ends = set()
    for order in ((PRESENT, "p_mid"), ("p_mid", PRESENT)):
        w, d = _world()
        t = next(t for t in w.tenures if t.subject == "p_mid" and t.kind == "contain" and t.live)
        t.object = SETTLEMENT                # planted: a second person standing at the harbour
        assert len(world_q.presence(w, SETTLEMENT)) == 2
        harbour = w.sites[HARBOUR]
        harbour.condition = 500
        out = _fold(w, d, *(_restore(f"r_{who}", actor=who) for who in order))
        assert _kinds(out) == ["site.restored", "site.restored"], _kinds(out)
        ends.add(harbour.condition)
    assert ends == {w.fixtures.get("condition_scale")}, ends
    # AND ONE HAND AMONG TWO MOVES HALF: the share is a fraction of the commons, not the whole.
    w, d = _world()
    next(t for t in w.tenures if t.subject == "p_mid" and t.kind == "contain" and t.live).object = SETTLEMENT
    w.sites[HARBOUR].condition = 500
    assert _kinds(_fold(w, d, _restore("r_one"))) == ["site.restored"]
    assert w.sites[HARBOUR].condition == 750, w.sites[HARBOUR].condition


def test_24e_restore_raises_a_works_fabric_to_its_ceiling_and_then_stalls():
    """r2 §A.6.6's TERM-STALL: the harbour at 200 under a works one of three terms ripe (ceiling
    333) -- `restore` raises it to 333 and no further; asked again in the same season it is
    `restore.refused` (*you cannot hurry mortar*). Another term ripens, and it rises to 666."""
    w, d = _world()
    _declare(w, d, "wk", "harbour", SETTLEMENT)
    _ripen(w, d, 1)
    harbour = w.sites[HARBOUR]
    harbour.condition = 200
    assert _kinds(_fold(w, d, _restore("r1"))) == ["site.restored"] and harbour.condition == 333
    assert _kinds(_fold(w, d, _restore("r2"))) == ["restore.refused"] and harbour.condition == 333
    _ripen(w, d, 1)
    harbour.condition = 333                  # planted back over the barrier's wear
    assert _kinds(_fold(w, d, _restore("r3"))) == ["site.restored"] and harbour.condition == 666


# ======================================================================================
# 5 -- `found`: A WORKS STAKES A PLACE, AND THE GATE ADMITS ITS EDGE AS A FOUNDING
# ======================================================================================

def _found(key, works, actor=ABSENT):
    return Act(id=key, actor=actor, verb="found", payload={"subject": works})


def _spy_bases(monkeypatch):
    """Every basis the real `tenure_write_basis` returns, observed rather than inferred."""
    from ..state import gate as G
    seen, real = [], G.tenure_write_basis

    def spy(*a, **k):
        b = real(*a, **k)
        seen.append((a[1].kind, a[1].subject, b))
        return b
    monkeypatch.setattr(G, "tenure_write_basis", spy)
    return seen


def test_24e_found_mints_one_rung_of_the_plan_under_its_at_and_census_shows_exactly_one_more(
        monkeypatch):
    """THE PLAN'S OBSERVABLE: *"`census` shows exactly one more rung after one `found`"* -- read off
    `harness/populated.census`, which counts rungs by kind FROM THE WORLD. The new rung is the works'
    plan kind, its one parent is the works' `at` (the ladder walks up through it to the realm), and
    its `contain` edge is admitted at the gate under `founding` and nothing else."""
    from ..harness.populated import census
    from ..state.gate import FOUNDING
    w, d = _world()
    _declare(w, d, "wk", "hearth", SETTLEMENT)
    before = census(w)["rungs"]
    seen = _spy_bases(monkeypatch)
    out = _fold(w, d, _found("f1", "wk"))
    assert _kinds(out) == ["rung.founded"], _kinds(out)
    after = census(w)["rungs"]
    assert after.get("hearth", 0) == before.get("hearth", 0) + 1, (before, after)
    assert sum(after.values()) == sum(before.values()) + 1, (before, after)
    new = next(r for r in w.rungs if r not in ("R", "D", "S", "Hh") and w.rungs[r].kind == "hearth")
    assert world_q.parent_of(w, new) == SETTLEMENT
    assert world_q.ancestry(w, new)[-1] == "R"
    assert new in world_q.descendants(w, "D")
    assert ("contain", new, FOUNDING) in seen, seen
    # v9 IN-28 (`H-166`): founded PAID FOR -- the hearth's stake moved out of the works' rung `S`
    # into it -- and HELD BY ITS FOUNDER. (It read *"founded empty, held by none"* before IN-28.)
    price = w.fixtures.get("works_cost")["hearth"]
    assert w.rungs[new].stores == price, w.rungs[new].stores
    assert world_q.hold_force(w, new).subject == ABSENT


@pytest.mark.parametrize("case", ["not_the_master", "a_text_record", "does_not_ascend",
                                  "same_kind", "plans_a_site", "founded_twice", "r2_nested_plan"])
def test_24e_found_is_refused_on_each_of_its_own_preconditions_and_makes_nothing(case):
    """EACH REFUSAL, AND NOTHING MADE ON ANY OF THEM: `found.refused` and the rung count unchanged.
    The maker's standing (another person does not hold the works), a well-formed operand (a `text`
    Record is no works), strict ascent (a duchy planned under a settlement -- and a hearth under a
    hearth: ascent is STRICT, an equal kind is not above), a plan that is not a rung kind (a
    dwelling is `build`'s), one works founding once -- and r2's nested `{as, kind}` plan, which is
    no plain kind, reads as no target and refuses rather than crashing a keyed lookup in RESOLVE."""
    w, d = _world()
    plan, key, actor = "hearth", "wk", ABSENT
    if case == "a_text_record":
        _declare(w, d, key, plan, SETTLEMENT, kind="text")
    elif case == "does_not_ascend":
        _declare(w, d, key, "duchy", SETTLEMENT)
    elif case == "same_kind":
        _declare(w, d, key, "hearth", HEARTH)
    elif case == "r2_nested_plan":
        _declare(w, d, key, {"as": "rung", "kind": plan}, SETTLEMENT)
    elif case == "plans_a_site":
        _declare(w, d, key, "dwelling", SETTLEMENT)
    else:
        _declare(w, d, key, plan, SETTLEMENT)
    if case == "not_the_master":
        actor = "p_mid"
    if case == "founded_twice":
        assert _kinds(_fold(w, d, _found("f0", key))) == ["rung.founded"]
    n = len(w.rungs)
    out = _fold(w, d, _found("f1", key, actor=actor))
    assert _kinds(out) == ["found.refused"], (case, _kinds(out))
    assert len(w.rungs) == n, case


def test_24e_the_founding_basis_admits_a_newborns_one_parent_and_nothing_else():
    """THE NINTH BASIS, ASKED DIRECTLY OF THE REAL `tenure_write_basis`, each admission with its refused
    twin one clause away: a `contain` opened for a rung the SAME write brought into existence is
    `founding`; the same edge when the rung was not born in this write is refused (no basis: a Rung
    is nobody's, so `T-m` cannot reach it); a second live parent for the newborn is refused; and an
    edge of another kind from the newborn is refused."""
    from ..state import gate as G
    from ..state.carriers import Rung, Tenure
    w, _d = _world()
    w.rungs["Hn"] = Rung("Hn", "hearth")
    t = w.add_tenure(Tenure("tn", "Hn", SETTLEMENT, "contain", since=w.tick))
    born = frozenset({"Hn"})
    assert G.tenure_write_basis(w, t, None, ABSENT, None, frozenset(), born=born) == G.FOUNDING
    assert G.tenure_write_basis(w, t, None, ABSENT, None, frozenset()) is None
    w.rungs["Hm"] = Rung("Hm", "hearth")          # a SECOND newborn, with no parent yet at all
    tie = w.add_tenure(Tenure("tt", "Hm", "Hh", "tie", since=w.tick))
    assert G.tenure_write_basis(w, tie, None, ABSENT, None, frozenset(),
                                born=frozenset({"Hm"})) is None
    w.add_tenure(Tenure("tn2", "Hn", "D", "contain", since=w.tick))
    assert G.tenure_write_basis(w, t, None, ABSENT, None, frozenset(), born=born) is None


# ======================================================================================
# 6 -- `build`, AND THE PLAN'S CORRECTED FALSIFIER: A FULL RUNG STILL GROWS
# ======================================================================================

def _build(key, works, actor=ABSENT):
    return Act(id=key, actor=actor, verb="build", payload={"subject": works})


def test_24e_build_stands_a_site_of_the_plan_at_condition_zero_and_once():
    """`build` makes the works' plan at its `at`, at CONDITION 0 (r2 §A.7.1: *"a fabric begins at
    NOTHING"*), and a works builds once. CONTROLS: a works planning a RUNG kind is `found`'s and
    `build` refuses it; a person who does not hold the works is refused."""
    w, d = _world()
    _declare(w, d, "wk", "harbour", HEARTH)
    _stock(w, HEARTH, "harbour")
    assert _kinds(_fold(w, d, _build("b0", "wk", actor="p_mid"))) == ["build.refused"]
    n = len(w.sites)
    out = _fold(w, d, _build("b1", "wk"))
    assert _kinds(out) == ["site.built"], _kinds(out)
    assert len(w.sites) == n + 1
    built = [s for s in w.sites.values() if s.rung == HEARTH and s.kind == "harbour"]
    assert len(built) == 1 and built[0].condition == 0, built
    assert _kinds(_fold(w, d, _build("b2", "wk"))) == ["build.refused"] and len(w.sites) == n + 1
    _declare(w, d, "wr", "hearth", SETTLEMENT, actor="p_mid")
    assert _kinds(_fold(w, d, _build("b3", "wr", actor="p_mid"))) == ["build.refused"]


def test_24e_a_found_then_a_build_at_a_full_rung_succeeds_and_every_ancestors_dwellings_rise_by_one(
        monkeypatch):
    """THE PLAN'S FALSIFIER, AS CORRECTED 2026-09-25 (the original was inverted): *"A `found` then a
    `build` of a `dwelling` at a rung whose population is at capacity SUCCEEDS, and that rung's
    dwelling count, and so every ancestor's count, rises by exactly one. Assert the count before and
    after, not only the success Event."* `S` is FULL: one dwelling (planted at `Hh`) under four
    residents (`p_high` at `S`, three at `Hh`), read through `world_q.population`/`capacity` since
    plan position `19c` landed both -- the plan: *"if the build lands with `19c`, read the rise
    through `capacity`"*, which this test asserted the day `capacity` did not exist and now does.
    ⚠ AND `found`/`build` NEVER CONSULT IT (the same message's second half, and `24d`'s reading of
    *"throttle"*: they are how capacity GROWS, and a full rung refusing them would stay full forever).
    Observed, not read off the source: both Queries are replaced by a raise for the two folds, at
    `world_q` and at the one module that imports them by name. The refusal for a full rung is
    `migrate`'s (`tests/test_migrate_capacity.py`). The founded hearth, with no dwelling yet, reads the
    FLOOR -- `24d-ii`'s *never 0* -- and building one lifts it no further than the floor already had."""
    # ⚠ `effects_founding`, NOT `effects`, SINCE THE PHASE-4 PER-SUBSYSTEM SPLIT (2026-09-30):
    # `found`/`build` moved to `effects_founding.py`, which never imports `capacity`/`population`
    # at all (neither call needs either), so `raising=False` -- the guard is now enforced
    # structurally (a bare reference to either name in that module would be a NameError, caught by
    # any test that exercises `found`/`build`) rather than by this patch alone; kept for the same
    # defence-in-depth `world_q`'s half still gives.
    from ..loop import effects_founding
    from ..state.carriers import Site
    w, d = _world()
    w.sites["dw_hh"] = Site("dw_hh", HEARTH, "dwelling", condition=w.fixtures.get("condition_scale"))
    floor = w.fixtures.get("capacity_floor")[world_q.DWELLING_KIND]
    assert world_q.population(w, SETTLEMENT) == 4 > world_q.capacity(w, SETTLEMENT) == 1
    chain = world_q.ancestry(w, SETTLEMENT)                       # S, D, R
    before = {r: world_q.capacity(w, r) for r in chain}

    def _consulted(*_a, **_k):
        raise AssertionError("`found`/`build` consulted the throttle they exist to lift")
    for mod in (world_q, effects_founding):
        for name in ("capacity", "population"):
            monkeypatch.setattr(mod, name, _consulted, raising=False)
    _declare(w, d, "wf", "hearth", SETTLEMENT)
    assert _kinds(_fold(w, d, _found("f1", "wf"))) == ["rung.founded"]
    hearth = next(r for r in world_q.descendants(w, SETTLEMENT) if r.endswith(":wf"))
    _declare(w, d, "wb", "dwelling", hearth)
    _stock(w, hearth, "dwelling")
    assert _kinds(_fold(w, d, _build("b1", "wb"))) == ["site.built"]
    monkeypatch.undo()
    after = {r: world_q.capacity(w, r) for r in chain}
    assert all(after[r] == before[r] + 1 for r in chain), (before, after)
    assert world_q.capacity(w, hearth) == max(floor, 1) and world_q.capacity(w, HEARTH) == 1


def test_24e_the_whole_lifecycle_runs_declare_ripen_found_build_move_in_and_raise():
    """r2 §A.6.2's four moments, end to end through the real fold and the real MATTER barrier: a
    works is DECLARED (`create_record`), its terms RIPEN (MATTER, through the gate), the plot is
    STAKED (`found`) and the fabric RAISED into being (`build`, at 0), and it is BUILT UP (`restore`
    by a person who moved in) -- exactly as far as the terms allow: two of three ripe, 666, and no
    further until the third ripens, then full."""
    w, d = _world()
    scale = w.fixtures.get("condition_scale")
    _declare(w, d, "wf", "hearth", SETTLEMENT)
    assert _kinds(_fold(w, d, _found("f1", "wf"))) == ["rung.founded"]
    hearth = next(r for r in world_q.descendants(w, SETTLEMENT) if r.endswith(":wf"))
    _declare(w, d, "wb", "dwelling", hearth, terms=3)
    _stock(w, hearth, "dwelling")
    assert _kinds(_fold(w, d, _build("b1", "wb"))) == ["site.built"]
    dwelling = next(s for s in w.sites.values() if s.rung == hearth)
    moved = _fold(w, d, Act(id="mv", actor=ABSENT, verb="move", payload={"to": hearth}))
    assert _kinds(moved) == ["travel.moved"] and ABSENT in world_q.presence(w, hearth), _kinds(moved)
    assert _kinds(_fold(w, d, _restore("r0", actor=ABSENT, site=dwelling.id))) == ["restore.refused"]
    _ripen(w, d, 2)
    assert _kinds(_fold(w, d, _restore("r1", actor=ABSENT, site=dwelling.id))) == ["site.restored"]
    assert dwelling.condition == 2 * scale // 3, dwelling.condition
    assert _kinds(_fold(w, d, _restore("r2", actor=ABSENT, site=dwelling.id))) == ["restore.refused"]
    _ripen(w, d, 1)
    assert _kinds(_fold(w, d, _restore("r3", actor=ABSENT, site=dwelling.id))) == ["site.restored"]
    assert dwelling.condition == scale


@pytest.mark.parametrize("verb", ["found", "build"])
def test_24e_a_works_whose_plan_or_at_is_no_plain_id_is_refused_not_a_crash(verb):
    """r2's nested `{as, kind}` plan and a list for `at` are no target (`works_target`): both verbs
    refuse, and neither reaches a keyed lookup that would raise `TypeError` inside RESOLVE --
    `site_kinds` is a frozenset and `w.rungs` a dict, so an unhashable plan or `at` would."""
    w, d = _world()
    kind = "dwelling" if verb == "build" else "hearth"
    _declare(w, d, "wp", {"as": "site" if verb == "build" else "rung", "kind": kind}, HEARTH)
    _declare(w, d, "wa", kind, [HEARTH], actor="p_mid")
    n = (len(w.rungs), len(w.sites))
    for key, works, actor in (("x1", "wp", ABSENT), ("x2", "wa", "p_mid")):
        out = _fold(w, d, Act(id=key, actor=actor, verb=verb, payload={"subject": works}))
        assert _kinds(out) == [f"{verb}.refused"], (works, _kinds(out))
    assert (len(w.rungs), len(w.sites)) == n


# ======================================================================================
# 7 -- v9 IN-45 `work`: THE WORKS CHANNEL, ATTACKED THROUGH THE REAL FORMATION (H-165 (2), (3))
# ======================================================================================
# The plan's candidate for H-165 limit 2 was a `rosters.yaml: record_sourced_operands` entry for a
# works, mapped onto the closed eight. These tests take the formation route the candidate would
# use: the maker's own `create_record`, WITNESS's content deposit, `questions_for`, `opening_set`,
# `pack_scenes` and the fold. No test here asserts anything about the seed-0 realm (v9 §0.5).
# What they show:
#   * `found` and `build` need NO operand channel. Once a works exists they form on it through
#     the question its maker is asked about it, and they execute. H-165 limit 3 is lifted by a works
#     EXISTING; what is missing in computed play is the PRODUCER, a computed `create_record` that
#     declares one (limit 2).
#   * `work` binds `site` to the question's referent. That referent is the Site when the question
#     is about the Site, and the works Record when the question is about the works. The candidate
#     entry cannot change this: a works' content keys are `{plan, at}`, a kind and a Rung id, and
#     `_content_answer` returns a key's value unchanged, so no works answers `site` with a Site.
# MUTATIONS, run at the build 2026-10-16. Each went RED, then was restored byte-exact and went GREEN:
#   * `_eff_create_record` minting `kind = "text"` for every act (the producer making no works,
#     which is computed play today) -> the first test's works arm and the second test went RED.
#   * `_eff_work`'s works branch disabled (`and works_for(...)` -> `and False`) -> the second
#     test's harbour arm went RED.

from ..decision import assemble as _assemble
from ..decision import options as _options
from ..decision.choose import pack_scenes as _pack
from ..state.ids import H as _H


def _formed_on(w, pid, referent, verbs, q=None):
    """The computed acts `pid` forms for `verbs` on a question naming `referent`. The question is
    `q` when given, else a `claim_landed` Question about nothing in his ledger, AS THE SPLICE DELIVERS
    IT (v10 REM-22): carrying its own referents of every stamped class (`world_q.own_referents_of_class`,
    through `_stamped`), because a row declaring `referent_class: Site` (`work`) forms on a classed
    referent alone. The acts come from the real `opening_set` and are packed by the real `pack_scenes`."""
    from ..data.rosters import OCCASION_ONLY_CLASSES
    from ..data.verbs import DECLARED_CLASSES
    from ..state.carriers import Question
    p = w.persons[pid]
    if q is None:
        q = Question(f"q:{referent}", "claim_landed", (referent,), None)
        q = world_q._stamped(q, world_q.own_referents_of_class(w, q, DECLARED_CLASSES - OCCASION_ONLY_CLASSES), w)
    cands = [c for c in _options.opening_set(p, _assemble(p, q, 12), q, w.fixtures) if c.verb in verbs]
    mint = lambda who, verb, subj: _H(w.world_seed, w.tick, who, f"act:{verb}:{subj}")
    return [a for s in _pack(p, cands, 99, w.fixtures, mint) for a in s.acts]


def _without_holding_class():
    """`opening_set`'s table with `found`'s and `build`'s `referent_class` BLANKED in-process (v10 REM-25,
    B10-05): the formation of the REM-24 tree (`f2381695`), which `test_in45_found_and_build_form_on_a_works_
    its_maker_is_asked_about_and_execute` was written against. THE UNIT AND THE REASON: the two rows declare
    `Record` and form on a Record-classed referent alone -- a held Record the question carries as that
    class -- so a question merely ABOUT the Record (a `claim_landed` question whose plain referent it is)
    forms neither; `test_rem25_found_and_build_form_on_the_works_the_maker_holds_...` below pins the shipped
    route."""
    import dataclasses
    from unittest import mock
    from ..data.verbs import VERB_TABLE
    from ..decision import options as _opts
    table = {**VERB_TABLE, **{v: dataclasses.replace(VERB_TABLE[v], referent_class="")
                              for v in ("found", "build")}}
    return mock.patch.object(_opts, "VERB_TABLE", table)


def _maker_declares_two_works(kind):
    """The setup of the two tests below: a hearth at `S` and a dwelling at `Hh` declared by the real
    `create_record`, WITNESS's deposit of each, the dwelling's timber planted, one season on."""
    w, d = _world()
    for key, plan, at in (("wh", "hearth", SETTLEMENT), ("wd", "dwelling", HEARTH)):
        d.witness(mint_token(w, WriteClass.INTERIOR), _declare(w, d, key, plan, at, kind=kind))
    _stock(w, HEARTH, "dwelling")            # the dwelling's timber (v9 IN-28); `S` stocks the stake
    _season(w, d)
    return w, d


@pytest.mark.parametrize("kind", [world_q.WORKS_KIND, "text"])
def test_rem25_found_and_build_form_on_the_works_the_maker_holds_and_a_text_forms_neither(kind):
    """THE SHIPPED ROUTE (v10 REM-25, B10-05): the same two Records, and the maker's delivered question (the
    head of `questions_for`) carries each he HOLDS as a `Record` -- `records_held_for_holding_rows`, kinds
    `HOLDING_RECORD_KINDS` -- so `found` and `build` form on both, and the real fold disposes exactly as
    the unclassed formation's did: `rung.founded` for the hearth under `found`, `site.built` for the
    dwelling under `build`, each verb's other works refused by its own effect. A question merely ABOUT a
    Record (a later question) carries no class and forms neither. THE CONTROL, the same body with the
    Records declared `text`: a text is no holding kind, no question carries a `Record` and neither verb
    forms for anyone on any question."""
    w, d = _maker_declares_two_works(kind)
    p = w.persons[ABSENT]
    qs = world_q.questions_for(w, p)
    head = qs[0]
    if kind != world_q.WORKS_KIND:
        assert not [r for q in qs for r, c in q.classes if c == "Record"], qs
        assert not [a for q in qs for a in _formed_on(w, ABSENT, "wh", ("found", "build"), q=q)]
        return
    assert {("wd", "Record"), ("wh", "Record")} <= set(head.classes), head
    acts = _formed_on(w, ABSENT, "wh", ("found", "build"), q=head)
    assert sorted((a.payload.get("subject"), a.verb) for a in acts) == [
        ("wd", "build"), ("wd", "found"), ("wh", "build"), ("wh", "found")], acts
    got = {}
    for key in ("wh", "wd"):
        for a in sorted((a for a in acts if a.payload.get("subject") == key),
                        key=lambda a: a.verb != "found"):
            got[(key, a.verb)] = _kinds(_fold(w, d, a))
    assert got == {("wh", "found"): ["rung.founded"], ("wh", "build"): ["build.refused"],
                   ("wd", "found"): ["found.refused"], ("wd", "build"): ["site.built"]}, got
    assert "hearth:wh" in w.rungs and w.sites["dwelling:wd"].condition == 0
    about = [q for q in qs[1:] if {"wh", "wd"} & set(q.referents)]
    assert about and not [a for q in about for a in _formed_on(w, ABSENT, "wh", ("found", "build"), q=q)]


@pytest.mark.parametrize("kind", [world_q.WORKS_KIND, "text"])
def test_in45_found_and_build_form_on_a_works_its_maker_is_asked_about_and_execute(kind):
    """THE MAKER IS ASKED ABOUT HIS WORKS AND `found`/`build` FORM ON IT. Two Records are declared
    by the real `create_record`: a hearth at `S` and a dwelling at `Hh`. WITNESS deposits each
    Record's content into the maker's own ledger, and the next season `questions_for` raises a
    question whose referent is the Record. `found` and `build` form on it, carrying
    `subject = the Record`, and the fold executes them: `rung.founded` for the hearth and
    `site.built` for the dwelling. Each verb's other works is refused by that verb's own effect.
    CONTROL, the same body with the Records declared `text`: the same questions form the same verbs,
    and every one is refused. The kind of the Record is the only difference between the arms.

    v10 REM-25 (B10-05): READ WITH `found`'S AND `build`'S `referent_class: Record` BLANKED IN-PROCESS
    (`_without_holding_class`) -- the formation of the REM-24 tree, which these assertions were written
    against; the shipped route (the held Record carried as a class by the head question) is the test above's.
    The assertions are unchanged and still execute: a question ABOUT the Record forms the two verbs on it, the
    fold executes the works arm and refuses the text arm."""
    w, d = _maker_declares_two_works(kind)
    p = w.persons[ABSENT]
    asked = {}
    for q in world_q.questions_for(w, p):
        for r in q.referents:
            asked.setdefault(r, q)
    assert {"wh", "wd"} <= set(asked), sorted(asked)          # the maker is asked about both
    got = {}
    with _without_holding_class():
        for key in ("wh", "wd"):
            acts = _formed_on(w, ABSENT, key, ("found", "build"), q=asked[key])
            assert sorted(a.verb for a in acts) == ["build", "found"], (key, acts)
            assert all(a.payload.get("subject") == key for a in acts), acts
            for a in acts:
                got[(key, a.verb)] = _kinds(_fold(w, d, a))
    if kind == world_q.WORKS_KIND:
        assert got == {("wh", "found"): ["rung.founded"], ("wh", "build"): ["build.refused"],
                       ("wd", "found"): ["found.refused"], ("wd", "build"): ["site.built"]}, got
        assert "hearth:wh" in w.rungs and w.sites["dwelling:wd"].condition == 0
    else:
        assert set(map(tuple, got.values())) == {("found.refused",), ("build.refused",)}, got


def test_in45_work_forms_on_what_the_question_names_and_never_reaches_the_site_a_works_names(
        monkeypatch):
    """`work`'s `site` IS THE QUESTION'S REFERENT, AND A WORKS CANNOT RE-AIM IT. The works plans a
    harbour at `S`, its term has ripened, and the harbour stands at 500.
      * A question naming the harbour forms `work` with `site = the harbour`. It executes:
        `site.worked`, 500 -> 1000.
      * CONTROL: a question naming the seam, which no works names, forms the same `work`. It is
        `work.unavailable` and the seam does not move.
      * THE GAP: the question the maker is actually asked is about the works Record. v10 REM-22
        (`work` declares `referent_class: Site`): the shipped `work` forms NOTHING on it, since the
        Record is not a Site. The formation the class removed is read with the row's column blanked
        in-process (the table as it stood before REM-22), which is where the two readings below
        are taken, unchanged: `work` binds `site` to the Record, which is no Site, and the act is
        `work.unavailable`.
      * THE CANDIDATE, PLANTED: `record_sourced_operands.works: {site: at}` is the one `site`
        mapping a works' keys allow, and the loader admits it. With it, `work` on that same question
        binds `site` to the Rung `S`, and the act is still `work.unavailable`. No mapping of
        `{plan, at}` onto the closed eight names a Site. (Read on the classless row as above: the
        shipped row never forms on the Record, so the mapping has nothing to re-aim.)"""
    w, d = _world()
    d.witness(mint_token(w, WriteClass.INTERIOR), _declare(w, d, "wk", "harbour", SETTLEMENT, terms=1))
    _ripen(w, d, 1)
    harbour, seam = w.sites[HARBOUR], w.sites["site_seam"]
    harbour.condition, seam.condition = 500, 500
    (on_harbour,) = _formed_on(w, ABSENT, HARBOUR, ("work",))
    assert on_harbour.payload["site"] == HARBOUR
    assert _kinds(_fold(w, d, on_harbour)) == ["site.worked"] and harbour.condition == 1000
    (on_seam,) = _formed_on(w, ABSENT, "site_seam", ("work",))
    assert _kinds(_fold(w, d, on_seam)) == ["work.unavailable"] and seam.condition == 500
    harbour.condition = 500
    # The question about the works' CONTENT claim. That claim is what the candidate reads
    # (`_from_content_claim`, by `q.about`).
    content = {c.id for c in w.persons[ABSENT].ledger
               if c.subject == "wk" and str(c.predicate).startswith("content:")}
    q = next(q for q in world_q.questions_for(w, w.persons[ABSENT], since=(0, 0))
             if q.referents == ("wk",) and q.about in content)
    assert _formed_on(w, ABSENT, "wk", ("work",), q=q) == []      # v10 REM-22: the class declines the Record
    import dataclasses
    classless = {**_options.VERB_TABLE,
                 "work": dataclasses.replace(_options.VERB_TABLE["work"], referent_class="")}
    monkeypatch.setattr(_options, "VERB_TABLE", classless)        # the row as it stood before REM-22
    (on_works,) = _formed_on(w, ABSENT, "wk", ("work",), q=q)
    assert on_works.payload["site"] == "wk"
    assert _kinds(_fold(w, d, on_works)) == ["work.unavailable"] and harbour.condition == 500
    from ..data.requires import REQUIRES_OPERANDS, RECORD_SOURCED_OPERANDS, _check_record_sourced
    from ..data.rosters import RECORD_KIND_KEYS
    planted = {**RECORD_SOURCED_OPERANDS, "works": {"site": "at"}}
    _check_record_sourced(planted, frozenset(REQUIRES_OPERANDS), RECORD_KIND_KEYS)   # admitted
    monkeypatch.setattr(_options, "RECORD_SOURCED_OPERANDS", planted)
    monkeypatch.setattr(_options, "_RECORD_ANSWERABLE",
                        frozenset(n for m in planted.values() for n in m))
    (planted_act,) = _formed_on(w, ABSENT, "wk", ("work",), q=q)
    assert planted_act.payload["site"] == SETTLEMENT and SETTLEMENT in w.rungs, planted_act
    from dataclasses import replace
    out = _fold(w, d, replace(planted_act, id=f"{planted_act.id}:planted"))   # one act per id (S27)
    assert _kinds(out) == ["work.unavailable"] and harbour.condition == 500, _kinds(out)


# ======================================================================================
# 8 -- v9 IN-28 (`H-166`): WHAT `found` AND `build` MAKE IS PAID FOR AND HELD
# ======================================================================================
# H-166's own design order: (1) a COST, (2) a HOLDER, (3) a CLOSER. (1) and (2) are built here. (3)
# is raze's (IN-12 step 11, B-R), not built here (`H-166`). The works exists by a hand-built `create_record`
# (where a works comes from in computed play is ED-IN-0297's open question, not this position's).
# Each test drives the real fold, the real MATTER barrier and the real gate.
# MUTATIONS, run at the build 2026-10-16. Each went RED, then was restored byte-exact and went GREEN:
#   * `_eff_found`'s `_shift` loop deleted (a founding that charges nothing) -> the first test RED.
#   * `_eff_build`'s debit loop deleted (a fabric built for free) -> the first test RED.
#   * `w.add_tenure(held)` deleted from `_eff_found` (a founded place nobody holds) -> the first
#     test RED.
#   * `_cost`'s shortfall clause emptied (`short = {}`) -> the second test RED on both verbs.


def _store(w, rung, kind):
    return (w.rungs[rung].stores or {}).get(kind, 0)


def test_in28_one_season_a_founded_place_is_paid_for_and_held_and_what_is_built_in_it_is_paid_for():
    """ONE SEEDED HAND-BUILT SEASON, EACH HALF OBSERVED ON THE WORLD, NOT ON THE SUCCESS EVENT.
    A works plans a hearth at `S` and is kept at `S`; its maker founds it. PAID: the stake
    (`works_cost` for a hearth) LEFT `S` and IS IN the new hearth, and the world's grain is unchanged
    (two-sided); the founding Event carries `S`'s receipt, so the cost was written THROUGH THE GATE.
    HELD: the founder holds the new hearth (`hold_force`, `in_holdings`). Then a works plans a
    dwelling in that hearth, its timber planted there: BUILT, the timber is CONSUMED (one-sided) and
    the stake is untouched, and the dwelling is held through its rung -- by the same founder, since a
    `hold` never reaches a Site. The season's MATTER barrier then runs, and the hold stands."""
    from ..state.gate import in_holdings
    w, d = _world()
    (kind, amount), = w.fixtures.get("works_cost")["hearth"].items()
    grain_before = sum((r.stores or {}).get(kind, 0) for r in w.rungs.values())
    s_before = _store(w, SETTLEMENT, kind)
    _declare(w, d, "wf", "hearth", SETTLEMENT)
    out = _fold(w, d, _found("f1", "wf"))
    assert _kinds(out) == ["rung.founded"], _kinds(out)
    hearth = next(r for r in world_q.descendants(w, SETTLEMENT) if r.endswith(":wf"))
    assert _store(w, SETTLEMENT, kind) == s_before - amount
    assert _store(w, hearth, kind) == amount
    assert sum((r.stores or {}).get(kind, 0) for r in w.rungs.values()) == grain_before
    assert {c.subject for c in out[0].changes} >= {hearth, SETTLEMENT}, out[0].changes
    assert world_q.hold_force(w, hearth).subject == ABSENT
    assert in_holdings(w, ABSENT, hearth)
    price = w.fixtures.get("works_cost")["dwelling"]
    _declare(w, d, "wb", "dwelling", hearth)
    _stock(w, hearth, "dwelling")
    held_before = dict(w.rungs[hearth].stores)
    assert _kinds(_fold(w, d, _build("b1", "wb"))) == ["site.built"]
    dwelling = w.sites["dwelling:wb"]
    assert {k: held_before[k] - _store(w, hearth, k) for k in price} == price
    assert _store(w, hearth, kind) == amount                  # the stake is not what a fabric costs
    assert world_q.hold_force(w, dwelling.rung).subject == ABSENT
    _season(w, d)
    assert world_q.hold_force(w, hearth).subject == ABSENT


def test_in28_a_founders_hold_stops_holder_faction_of_at_his_hearth_pinned_as_it_reads():
    """H-166 limit 2's CONSEQUENCE (B-K close, COR 5), PINNED AS IT READS TODAY -- not blessed and
    not changed. `world_q.holder_faction_of` returns at the FIRST held rung up the ancestry, so once
    `p_low` (committed to no faction) founds a hearth under `S`, which a Crown man holds, the hearth
    reads `None`: his hold is the nearest, and it coheres under nothing. (So a `survey`/`forge` of
    that hearth is refused, and `loop/sides.py`/`loop/effects_combat.py` read no side for it.)
    CONTROL, one change: the same founder committed to the Crown -> the hearth reads the Crown."""
    from ..data.rosters import faction_prop_id
    from ..state.carriers import Proposition, Tenure
    fac = faction_prop_id("Crown")
    for committed in (False, True):
        w, d = _world()
        w.propositions[fac] = Proposition(fac, "HOLDS", "Crown", "is a faction of this world",
                                          True, 0)
        w.add_tenure(Tenure("t_commit_p_mid", "p_mid", fac, "commit", since=0))
        w.add_tenure(Tenure("t_hold_S", "p_mid", SETTLEMENT, "hold", since=0))
        if committed:
            w.add_tenure(Tenure("t_commit_founder", ABSENT, fac, "commit", since=0))
        _declare(w, d, "wf", "hearth", SETTLEMENT)
        out = _fold(w, d, _found("f1", "wf"))
        assert "rung.founded" in _kinds(out), _kinds(out)
        hearth = next(r for r in world_q.descendants(w, SETTLEMENT) if r.endswith(":wf"))
        assert world_q.hold_force(w, hearth).subject == ABSENT
        assert world_q.holder_faction_of(w, SETTLEMENT) == fac          # the parent still answers
        assert world_q.holder_faction_of(w, hearth) == (fac if committed else None), committed


@pytest.mark.parametrize("verb", ["found", "build"])
def test_in28_a_works_whose_rung_cannot_pay_is_refused_and_nothing_is_made_or_spent(verb):
    """THE CAUSE CONTROLLED: the SAME world and the SAME act, and the price is the only thing that
    differs. At the shipped price the act executes; with the price swept one unit past what the
    works' rung holds, it is refused (`<verb>.refused`), nothing is made, and no store moves -- r2
    §A.6.6's MATTER-STALL, refused at the act rather than raising the place on credit."""
    plan = "hearth" if verb == "found" else "dwelling"
    made = (lambda w: w.rungs) if verb == "found" else (lambda w: w.sites)
    ran = 0
    for over in (False, True):
        w, d = _world()
        if verb == "build":
            _stock(w, SETTLEMENT, plan)
        cost = dict(w.fixtures.get("works_cost"))
        (kind, _amount), = cost[plan].items()
        if over:
            cost[plan] = {kind: _store(w, SETTLEMENT, kind) + 1}
            w.fixtures = w.fixtures.sweep("works_cost", cost)
        _declare(w, d, "wk", plan, SETTLEMENT)
        stores, n = {r: dict(x.stores or {}) for r, x in w.rungs.items()}, len(made(w))
        out = _fold(w, d, Act(id="x", actor=ABSENT, verb=verb, payload={"subject": "wk"}))
        if not over:
            assert _kinds(out) == [{"found": "rung.founded", "build": "site.built"}[verb]], _kinds(out)
        else:
            assert _kinds(out) == [f"{verb}.refused"], _kinds(out)
            assert len(made(w)) == n
            assert {r: dict(x.stores or {}) for r, x in w.rungs.items()} == stores
        ran += 1
    assert ran == 2


def test_in28_a_plan_with_no_price_is_refused_and_body_is_among_them():
    """A PLAN KIND WITH NO `works_cost` ROW CANNOT BE PAID FOR, so it is refused rather than raised
    free: `body` (in `site_kinds`, whose own note says it *"IS NOT A SITE"* -- `H-166` limit 4,
    refused by the roster and not by a kind literal) and `settlement` (a rung kind the ladder admits
    under a duchy; unpriced, SE-9(a)'s held question). CONTROL: a priced plan at the same rung, by
    the same maker, executes."""
    from ..data.rosters import SITE_KINDS
    w, d = _world()
    _stock(w, "D", "dwelling")
    cost = w.fixtures.get("works_cost")
    assert "body" in SITE_KINDS and "body" not in cost and "settlement" not in cost
    for key, plan, verb, want in (("wb", "body", "build", "build.refused"),
                                  ("ws", "settlement", "found", "found.refused"),
                                  ("wd", "dwelling", "build", "site.built")):
        _declare(w, d, key, plan, "D")
        out = _fold(w, d, Act(id=f"a:{key}", actor=ABSENT, verb=verb, payload={"subject": key}))
        assert _kinds(out) == [want], (plan, _kinds(out))
