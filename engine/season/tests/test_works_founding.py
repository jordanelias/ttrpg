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
    assert not w.rungs[new].stores and world_q.hold_force(w, new) is None   # founded empty, held by none


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


def _dwellings_under(w, rung):
    """The dwelling Sites at `rung` and at every rung below it -- `24d-ii`'s derivation (`capacity`'s
    count, before its floor), done here because `capacity` itself is `19c`'s and is not built."""
    under = {rung, *world_q.descendants(w, rung)}
    return sum(1 for s in w.sites.values() if s.kind == "dwelling" and s.rung in under)


def test_24e_build_stands_a_site_of_the_plan_at_condition_zero_and_once():
    """`build` makes the works' plan at its `at`, at CONDITION 0 (r2 §A.7.1: *"a fabric begins at
    NOTHING"*), and a works builds once. CONTROLS: a works planning a RUNG kind is `found`'s and
    `build` refuses it; a person who does not hold the works is refused."""
    w, d = _world()
    _declare(w, d, "wk", "harbour", HEARTH)
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


def test_24e_a_found_then_a_build_at_a_full_rung_succeeds_and_every_ancestors_dwellings_rise_by_one():
    """THE PLAN'S FALSIFIER, AS CORRECTED 2026-09-25 (the original was inverted): *"A `found` then a
    `build` of a `dwelling` at a rung whose population is at capacity SUCCEEDS, and that rung's
    dwelling count, and so every ancestor's count, rises by exactly one. Assert the count before and
    after, not only the success Event."* `S` is FULL by the only reading the tree can compute: one
    dwelling (planted at `Hh`) under four persons (`p_high` at `S`, three at `Hh`), every dwelling
    occupied. `capacity` is `19c`'s and is not built (asserted, so this test is re-read the day it
    lands -- the plan: *"if the build lands with `19c`, read the rise through `capacity`"*); so the
    count is `24d-ii`'s derivation, done by hand. The refusal for a full rung is `migrate`'s."""
    from ..state.carriers import Site
    assert not hasattr(world_q, "capacity"), (
        "`capacity` exists now (`19c`/`24d-ii`): read this rise through it, as the plan instructs, "
        "and assert that `found`/`build` never consult it")
    w, d = _world()
    w.sites["dw_hh"] = Site("dw_hh", HEARTH, "dwelling", condition=w.fixtures.get("condition_scale"))
    persons_under_s = [p for p in w.persons
                       if world_q.home_of(w).get(p) in {SETTLEMENT, *world_q.descendants(w, SETTLEMENT)}]
    assert len(persons_under_s) == 4 and _dwellings_under(w, SETTLEMENT) == 1, persons_under_s
    chain = world_q.ancestry(w, SETTLEMENT)                       # S, D, R
    before = {r: _dwellings_under(w, r) for r in chain}
    _declare(w, d, "wf", "hearth", SETTLEMENT)
    assert _kinds(_fold(w, d, _found("f1", "wf"))) == ["rung.founded"]
    hearth = next(r for r in world_q.descendants(w, SETTLEMENT) if r.endswith(":wf"))
    assert _dwellings_under(w, hearth) == 0                      # founded: no dwelling until BUILT
    _declare(w, d, "wb", "dwelling", hearth)
    assert _kinds(_fold(w, d, _build("b1", "wb"))) == ["site.built"]
    after = {r: _dwellings_under(w, r) for r in chain}
    assert all(after[r] == before[r] + 1 for r in chain), (before, after)
    assert _dwellings_under(w, hearth) == 1 and _dwellings_under(w, HEARTH) == 1


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
