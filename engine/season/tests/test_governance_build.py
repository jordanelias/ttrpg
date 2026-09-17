"""The covering test file for the governance/settlements/decisions build programme.

WHY A SECOND FILE RATHER THAN A 11,187th LINE IN `test_season_shape.py`. `CLAUDE.md` §0.4
clause 2 -- *"mid-session, run only the file covering what you touched"* -- is only cheap when
that file is small. `test_season_shape.py` is the INSTRUMENT'S OWN adversarial test: its subject
is whether the tracer flatters the shape. The subject here is different -- whether an item of
`proposals/2026-09-17-governance-and-behaviour/01_THE_BUILD_ORDER.md` actually executes -- so the
two are not the same object, and §4's split test (*can a reader work with it*) answers the rest.

EVERY TEST HERE CARRIES ITS ITEM'S FALSIFIER ID from that build order's sheet (`LB-n`), and each
observes BOTH halves of its item's claim. A test that observes only the write is the half-wiring
this programme is full of.

Run: python -m pytest engine/season/tests/test_governance_build.py -q
"""

from __future__ import annotations

import pytest

from ..data.matrix import Step
from ..gaps import Forbidden
from ..data.cast import faction_leader
from ..harness.populated import build_realm
from ..loop.driver import SeasonDriver
from ..loop.predicates import in_holdings
from ..queries import world_q
from ..harness import probes as P
from ..decision import budget as _budget
from ..state.carriers import Proposition, Tenure, View


# ---------------------------------------------------------------------------
# ITEM 1 -- `@effect_for("commit")` is WRITTEN AND HELD, NOT SHIPPED. There is no test here.
#
# The effect ran, `resolvable_verbs()` went 18 -> 19, and four falsifiers passed -- and one
# populated season then measured `commitment.made: 0 / commitment.refused: 42`, because no
# question source in `questions_for` offers a Proposition as a referent and `commit`'s typed cell
# is `existence(of: subject, kind: Proposition)`. Landing it breached a CONTROL BOUND (not a
# golden) in `test_wd_a_fork_changes_a_later_decision_...`, whose own message names the breach:
# *"some FOURTH channel reaches `opening_set`, and every other figure in `W-D` is confounded."*
#
# The measurement, the reasoning and the re-scheduling (item 1 moves to PHASE 2, after item 7,
# with `commitment.made > 0` as its artifact) are in
# `proposals/2026-09-17-governance-and-behaviour/01_THE_BUILD_ORDER.md` §7.2. A test asserting a
# behaviour this branch does not ship would be the half-wiring this file exists to refuse.
# ---------------------------------------------------------------------------


# ---------------------------------------------------------------------------
# ITEM 16 -- `add_tenure`'s hold domain/codomain guard (⊕ R13) + the faction holds
# re-homed to persons. Falsifier LB-16.
# ---------------------------------------------------------------------------

def test_lb16_a_faction_can_no_longer_hold_a_rung():
    """⊕ R13's DOMAIN half. `holonic §15`: *"`hold` | Person → Office | Rung | Record |
    Proposition"* -- a faction is a `Proposition`, so it is not in the domain.

    THE SHAPE THIS REFUSES RAN FOR MONTHS AND LOOKED FINE. It is the exact construction
    `harness/populated.py` used for every province in canon's starting-control table."""
    w = P.tiny_world()
    w.propositions["fac_x"] = Proposition("fac_x", "HOLDS", "X", "is a faction", True, 0)
    with pytest.raises(Forbidden):
        w.add_tenure(Tenure("t_bad", "fac_x", "D", "hold", 0))


def test_lb16_a_hold_may_not_reach_a_site():
    """⊕ R13's CODOMAIN half, and `05_LEDGER_AND_BUILD.md`'s own row for it: *"a `hold` never
    reaches a `Site` | **NOTHING today**"*. `Site` is the one class `holonic §15`'s row excludes
    that the world actually holds, so it is the only codomain violation that can be constructed."""
    w = P.tiny_world()
    with pytest.raises(Forbidden):
        w.add_tenure(Tenure("t_site", "p_low", "site_harbour", "hold", 0))


def test_lb16_an_unresolvable_id_still_passes_so_rehoming_still_works():
    """THE CONTROL, AND IT IS THE ONE THAT KEEPS THE GUARD FROM BEING TOO WIDE.

    `_rehome` exists because a Tenure may be added BEFORE its subject is a person. A guard
    refusing every unknown id would refuse the store's own construction sequence, so `class_of`
    returns `None` for "not yet" and `_refuse_bad_hold` reads that as PERMITTED. Without this
    test the guard could tighten to `subject in w.persons` and every ordering-tolerant fixture in
    the tree would start raising -- which is a real regression wearing a stricter rule's clothes."""
    w = P.tiny_world()
    w.add_tenure(Tenure("t_early", "p_not_yet", "off_x", "hold", 0))
    assert w._unowned, "the plant did not land in _unowned; the guard refused an ordering it should tolerate"


def test_lb16_build_realm_has_no_faction_holds_and_holdings_is_satisfiable():
    """**LB-16**, and BOTH halves, because either alone is the half-wiring.

    Half one: `build_realm` builds with **0** faction-subject holds -- the artifact the build
    order names. Half two, which is the one that matters: `in_holdings` is TRUE for at least one
    (person, rung) pair, so a seat declaring `revocation: "holdings"` can finally execute to True.
    Before this item it was **false for every person over every rung in the world**, forever,
    while looking exactly like a working precondition.

    ⚠ IT ASSERTS THAT IT ASSERTED (`CLAUDE.md` §0.1 pt 2). A loop over candidate (person, rung)
    pairs that finds none is indistinguishable from a loop whose body never ran, and `LB-10c` is
    named in the build order as the live case of exactly that."""
    w = build_realm(0)

    holds = [t for t in w.tenures if t.kind == "hold"]
    assert holds, "no hold Tenures at all -- the fixture changed and this test is measuring nothing"
    faction_held = [t for t in holds if w.class_of(t.subject) != "Person"]
    assert faction_held == [], f"{len(faction_held)} holds still have a non-person subject"

    checked = 0
    true_pairs = []
    for pid in w.persons:
        for rid in w.rungs:
            checked += 1
            if in_holdings(w, pid, rid):
                true_pairs.append((pid, rid))
    # ⚠ THE FLOOR IS DERIVED, NOT A NUMBER. An earlier draft asserted `checked > 1000` — a
    # magnitude nobody chose, which `tools/ci_sim_fabrication_check.py` correctly refused. The
    # exact product is stronger AND literal-free: it observes that the loop ran to COMPLETION
    # rather than merely that it ran a lot, so a sweep truncated by an early `break` fails here.
    assert checked == len(w.persons) * len(w.rungs), (
        f"the sweep examined {checked} of {len(w.persons) * len(w.rungs)} pairs; it did not run "
        "to completion, so an empty result below would be indistinguishable from a skipped body")
    assert true_pairs, (
        "`in_holdings` is false for every person over every rung -- item 16 did not land, and "
        "every `revocation: \"holdings\"` basis refuses forever")


def test_lb16_a_faction_with_no_authored_head_holds_nothing_and_it_is_counted():
    """THE COST OF THE RE-HOME, STATED RATHER THAN SWALLOWED.

    `Guilds` and `Schoenland` have no `leader:` in canon, so there is no person to re-home their
    provinces to and inventing one would put somebody canon does not name in charge of a
    territory. MEASURED: 16 provinces held before, **15 after**, and the one that drops is
    Schoenland's. The world reports it (`_unheld_for_want_of_a_head`) so an unheld province is a
    fact a reader can find rather than an arithmetic discrepancy they have to chase."""
    w = build_realm(0)
    assert hasattr(w, "_unheld_for_want_of_a_head")
    dropped = w._unheld_for_want_of_a_head
    assert dropped, (
        "nothing was dropped -- either canon grew the missing leaders, in which case delete this "
        "test, or the re-home silently invented a holder")
    assert all(fac for _, fac in dropped)
    # ⚠ THE ARITHMETIC IS A PARTITION, NOT A TOTAL. An earlier draft asserted `== 16` — the count
    # measured before the re-home, pinned into a test as a literal, which is the hard-coding
    # `tools/ci_sim_fabrication_check.py` exists to refuse and which would go stale the day canon
    # assigns one more province. The INVARIANT is what matters and it needs no number: the held
    # and the dropped are disjoint, and every drop is a faction canon genuinely gives no head.
    rung_holds = [t for t in w.tenures if t.kind == "hold" and w.class_of(t.object) == "Rung"]
    held_rungs = {t.object for t in rung_holds}
    dropped_rungs = {r for r, _ in dropped}
    assert held_rungs.isdisjoint(dropped_rungs), (
        f"a territory is both held and recorded as unheld: {held_rungs & dropped_rungs}")
    assert all(faction_leader(fac) is None for _, fac in dropped), (
        "a province was dropped for a faction that DOES have an authored head — the re-home "
        f"lost a holding it could have placed: {dropped}")


# ---------------------------------------------------------------------------
# ITEM 3a -- `nearest_store` and the per-eater draw. Falsifier LB-3a.
# ---------------------------------------------------------------------------

def _matter_once(w, *, keep_yield=False):
    """Run MATTER alone and return its Events.

    ⚠⚠ THE SITES ARE CLEARED UNLESS A CALLER ASKS OTHERWISE, AND THE FIRST WRITING OF THESE TESTS
    DID NOT DO THAT — every one of them failed, reporting a settlement that GAINED where a draw
    should have taken. The cause is `#353 §25`'s own barrier order: MATTER draws larders and THEN
    takes yield, in one call, so a bare `matter()` measures the NET of two steps and an assertion
    about the draw is reading a number the draw does not own.

    Removing the yield source is what makes the assertion observe the thing it names
    (`CLAUDE.md` §0.1 pt 2). The alternative — a paired no-eater control run, subtracting its
    yield — measures the same quantity at twice the runtime and puts a second run's arithmetic
    between the reader and the claim. `test_w8_matter_draws_before_it_produces_which_is_353s_
    stated_order` already owns the interaction of the two steps; these own the draw."""
    if not keep_yield:
        w.sites.clear()
    d = SeasonDriver(w)
    w.step = Step.MATTER
    return d.matter([])


def _eaters_at(w, rung_id):
    return [pid for pid, home in world_q.home_of(w).items() if home == rung_id]


def _heads(w, eaters):
    """Weight, not head count — `Person.weight` is the cohort multiplier."""
    return sum(w.persons[e].weight for e in eaters)


def decision_budget(w, pid):
    """What `decision.budget` gives this person right now — the READ side of `Person.body`."""
    p = w.persons[pid]
    return _budget(p, View(pid, [], w.fixtures.get("view_k")), w.fixtures.get("scene_budget"),
                   w.fixtures)


def _need(w, eaters):
    """Exactly what these eaters draw in one season, per kind, from the shipped weights.

    ⚠ EVERY LARDER IN THIS FILE IS STOCKED FROM THIS, never from a round number. A fixture stock
    of `40` is a magnitude nobody chose (and `tools/ci_sim_fabrication_check.py` refuses it), and
    it is the weaker assertion besides: *the settlement fell by the right amount* is satisfied by
    a range, while *the settlement is empty* is satisfied by one value."""
    return {k: wt * _heads(w, eaters) for k, wt in w.fixtures.get("subsistence_weight").items()}


def test_lb3a_a_hearth_with_no_larder_eats_from_its_settlement():
    """**LB-3a**, and it observes BOTH halves: the settlement's stores fall, AND the eaters are
    not short. Either alone is satisfiable by a half-wiring — a draw that takes nothing leaves
    nobody short only because nobody ate.

    THE DEFECT THIS CLOSES, measured on `build_realm(0)` before the change: **4,810 units, all of
    them at the 37 settlement rungs and none at the 211 hearths**, 46 persons in 26 hearths, and
    **0 rungs with both eaters and stores** — so the per-rung draw counted zero eaters wherever
    there was anything to eat, and the subsistence step was inert on the world that ships."""
    w = P.tiny_world()
    w.rungs["Hh"].stores = {}                      # the hearth's own larder is bare
    eaters = _eaters_at(w, "Hh") + _eaters_at(w, "S")
    assert _eaters_at(w, "Hh"), "nobody lives in the hearth; this test would pass vacuously"
    # ⚠ STOCKED TO EXACTLY WHAT THESE EATERS NEED, never to a comfortable round number. An earlier
    # draft wrote `{"grain": 40, "salt": 30}` — magnitudes nobody chose, which
    # `tools/ci_sim_fabrication_check.py` correctly refused. Exact stock is also a STRONGER test:
    # it pins the draw to the unit instead of asserting it landed somewhere below 40.
    need = _need(w, eaters)
    w.rungs["S"].stores = dict(need)

    _matter_once(w)

    for k in need:
        assert w.rungs["S"].stores[k] == 0, (
            f"{k}: settlement kept {w.rungs['S'].stores[k]} of exactly the {need[k]} its people "
            "needed. The hearth-dwellers did not reach up the ladder, or drew the wrong amount")
    assert not [e for e in eaters if e in w._subsistence_shortfall], (
        f"an eater is short beside a settlement stocked to their exact need: "
        f"{w._subsistence_shortfall}")


def test_lb3a_control_a_hearth_with_its_own_larder_eats_locally_and_unchanged():
    """THE PAIRED CONTROL, and it is what makes the walk a GENERALISATION rather than a change.

    `nearest_store` returns the rung ITSELF where that rung has stock, so a hearth with a larder
    feeds its own people exactly as the per-rung loop did. **If this arm moves, the walk is not a
    generalisation** — it is a new rule wearing one's clothes, and every reading of the populated
    world would then be confounded by a second change nobody asked for."""
    w = P.tiny_world()
    at_hh, at_s = _eaters_at(w, "Hh"), _eaters_at(w, "S")
    assert at_hh and at_s, "the fixture needs eaters at both rungs for the control to mean anything"
    # Each rung stocked to exactly ITS OWN eaters' need. If the walk reached past a stocked hearth,
    # or reached DOWN from the settlement, one of the two would end nonzero and the other short.
    w.rungs["Hh"].stores = dict(_need(w, at_hh))
    w.rungs["S"].stores = dict(_need(w, at_s))

    _matter_once(w)

    for k in _need(w, at_hh):
        assert w.rungs["Hh"].stores[k] == 0, (
            f"{k}: the hearth-dwellers did not eat locally from a larder they have")
        assert w.rungs["S"].stores[k] == 0, (
            f"{k}: the settlement fed somebody it should not have — the walk is reaching DOWN, "
            "or the hearth's own larder was skipped")
    assert not w._subsistence_shortfall.keys() & set(at_hh + at_s), (
        f"an eater is short where their own rung held exactly their need: "
        f"{w._subsistence_shortfall}")


def test_lb3a_the_root_larder_at_zero_feeds_nobody_and_raises_nothing():
    """A person under a realm that holds nothing goes hungry, and hunger is a fact about the
    world — not a `KeyError`, and not an `Unspecified`.

    `nearest_store` returns `None` at the root and the caller records a shortfall. Raising here
    would make an empty larder an instrument defect, and a season that dies on a bare world is a
    season nobody can run the starving case in."""
    w = P.tiny_world()
    for rid in ("R", "D", "S", "Hh"):
        w.rungs[rid].stores = {}

    evs = _matter_once(w)                      # must not raise

    assert w._subsistence_shortfall, "nobody is short on a world with no food anywhere"
    assert set(w._subsistence_shortfall) == set(world_q.home_of(w)), (
        "some eater is neither fed nor recorded short — the loop skipped them silently")
    assert not [e for e in evs if e.kind == "stores.changed"], (
        f"a store changed on a world that holds nothing: {[e.subject for e in evs]}")


def test_lb3a_a_cohort_eats_by_its_weight_and_not_by_its_head_count():
    """`Person.weight` IS THE COHORT MULTIPLIER AND THE OLD LOOP DROPPED IT.

    `state/carriers.py`: *"A COHORT IS A PERSON AT weight > 1"*. The per-rung draw was
    `wt * len(eaters)`, so two hundred people eat like one man. Every person in the shipped corpus
    is at weight 1 — which is exactly why this was invisible, and why a test has to plant the
    cohort rather than wait for the corpus to grow one."""
    w = P.tiny_world()
    w.rungs["Hh"].stores = {}
    eaters = _eaters_at(w, "Hh") + _eaters_at(w, "S")
    cohort = _eaters_at(w, "Hh")[0]
    w.persons[cohort].weight = len(eaters) + 1   # a cohort, distinguishable from any head count
    # Stocked to exactly the WEIGHTED need. A loop counting heads would draw strictly less and
    # leave a surplus, so the assertion below fails loudly rather than by a margin.
    need = _need(w, eaters)
    w.rungs["S"].stores = dict(need)

    _matter_once(w)

    assert w.rungs["S"].stores["grain"] == 0, (
        f"a cohort of {w.persons[cohort].weight} ate like one person: the settlement kept "
        f"{w.rungs['S'].stores['grain']} of the {need['grain']} its people needed by WEIGHT")


def test_lb3a_two_eaters_cannot_spend_the_same_unit():
    """SCARCITY BINDS, and it binds because `nearest_store` is given the caller's running view.

    The writes are deferred to the gate, so a loop reading `w.rungs[...].stores` directly would
    show every eater the FULL larder — the defect `loop/effects.py`'s own header names for
    `transfer` (*"`transfer` twice from a one-unit larder succeeds twice"*). With one grain
    between three eaters, exactly one grain may leave the larder and the rest must be short."""
    w = P.tiny_world()
    w.rungs["Hh"].stores = {"grain": 1}
    for rid in ("R", "D", "S"):
        w.rungs[rid].stores = {}
    eaters = _eaters_at(w, "Hh")
    assert len(eaters) > 1, "the fixture needs at least two eaters for this to mean anything"

    _matter_once(w)

    assert w.rungs["Hh"].stores["grain"] == 0, (
        f"the larder went to {w.rungs['Hh'].stores['grain']}; a deferred write let two eaters "
        "spend the same unit, or the draw took more than was there")
    # ⚠ SUMMED OVER THE HEARTH'S EATERS ONLY. The first writing summed every person in the world
    # and read 9 where it wanted 5, because `p_high` and `p_king` are ALSO short on this bare
    # fixture — a test that attributes other people's hunger to this larder.
    short_grain = sum(w._subsistence_shortfall.get(e, {}).get("grain", 0) for e in eaters)
    wt = w.fixtures.get("subsistence_weight")["grain"]
    want = wt * _heads(w, eaters)
    assert short_grain == want - 1, (
        f"shortfall {short_grain} != {want} wanted - 1 available; the arithmetic does not close")


# ---------------------------------------------------------------------------
# ITEM 3b -- the body write, the shared `_crossings`, `remove_person`.
# Falsifiers LB-3b and LB-3c.
# ---------------------------------------------------------------------------

def _starving_world(body_step=10):
    """`tiny_world` with every larder bare and no site to produce one — the empty-root arm.

    ⚠ `body_step` IS SET EXPLICITLY AND THE SHIPPED DEFAULT IS `0`. `H-125` parks the magnitude at
    the control arm because all 86 buildable corpus worlds hold zero stores, so any nonzero
    default starves 258 people in worlds that model a scene rather than an economy. The MECHANISM
    is exercised here at a live arm — which is what keeps it a built behaviour rather than a
    branch nothing reaches (§0.2) — and `test_lb3b_the_zero_arm_...` pins the shipped one."""
    w = P.tiny_world()
    for rid in ("R", "D", "S", "Hh"):
        w.rungs[rid].stores = {}
    w.sites.clear()
    w.fixtures = w.fixtures.sweep("body_step", body_step)
    return w


def test_lb3b_a_short_larder_falls_a_body_a_band_and_narrows_the_season():
    """**LB-3b**, and it asserts the crossing **AND** the budget drop, because either alone is
    half-wiring.

    ⚠ THIS IS THE READ/WRITE ASYMMETRY TEST (`CLAUDE.md` §0.1 pt 1). `decision.budget` reads
    `p.body` TODAY. A MATTER write that landed on a copy — or on a `Person` the rehome replaced —
    would fall a body that no reader ever sees, and a test asserting only *the body fell* would
    stay green through it. So the budget is asserted to move IN THE SAME SEASON the band is
    crossed: the band is what `body_band_penalty` counts, so the two are the same fact observed
    from the write side and from the read side."""
    w = _starving_world()
    fx, k = w.fixtures, w.fixtures.get("scene_budget")
    d = SeasonDriver(w)
    who = "p_low"
    start_body = w.persons[who].body
    start_budget = decision_budget(w, who)
    floor = max(f for f in fx.get("band_floors")["body"].values() if f <= start_body)

    crossed_at = None
    for season in range(1, 40):
        w.step = Step.MATTER
        evs = d.matter([])
        w.tick += 1
        if [e for e in evs if e.kind == "condition.band_crossed" and e.subject == who]:
            crossed_at = season
            break
    assert crossed_at is not None, (
        f"{who}'s body never crossed a band in 39 starving seasons; it is at "
        f"{w.persons[who].body} from {start_body}")
    assert w.persons[who].body < floor <= start_body, (
        f"the crossing fired without the body passing the {floor} floor")
    assert decision_budget(w, who) < start_budget, (
        f"the band was crossed and the budget did not move ({start_budget} -> "
        f"{decision_budget(w, who)}). The MATTER write landed somewhere `decision.budget` does "
        "not read — which is the read/write asymmetry this test exists for")


def test_lb3b_control_a_stocked_world_moves_no_body_and_no_budget():
    """THE CONTROL. Same fixture, same seed, larders full — bodies constant, budgets unchanged,
    and `_crossings` fires for SITES only.

    `CLAUDE.md` §0.1 pt 4: a number without a control is not a measurement. Without this arm, a
    body write that fired unconditionally — on the fed as well as the starving — would pass every
    assertion in the test above."""
    w = P.tiny_world()
    at = {rid: _eaters_at(w, rid) for rid in ("R", "D", "S", "Hh")}
    for rid, eaters in at.items():
        w.rungs[rid].stores = dict(_need(w, eaters)) if eaters else {}
    before_bodies = {pid: p.body for pid, p in w.persons.items()}
    before_budgets = {pid: decision_budget(w, pid) for pid in w.persons}

    d = SeasonDriver(w)
    w.step = Step.MATTER
    evs = d.matter([])

    assert {pid: p.body for pid, p in w.persons.items()} == before_bodies, (
        "a fed person's body moved")
    assert {pid: decision_budget(w, pid) for pid in w.persons} == before_budgets, (
        "a fed person's season narrowed")
    person_crossings = [e for e in evs if e.kind == "condition.band_crossed"
                        and e.subject in w.persons]
    assert not person_crossings, f"a fed person crossed a band: {person_crossings}"


def test_lb3b_the_zero_arm_is_the_pre_item_tree_exactly():
    """`body_step = 0` IS THE CONTROL ARM OF THE SWEEP, and it must reproduce the day before this
    landed: nothing moves, nothing is emitted, nobody dies.

    A sweep arm that merely varies the magnitude cannot flip a verdict. This one can — it removes
    the cause rather than adjusting the result, which is the arm `harness/populated.py`'s own
    `creed_sweep` docstring calls the point of a control."""
    w = _starving_world(body_step=0)          # the SHIPPED arm, set explicitly
    assert P.DEFAULT_FIXTURES.get("body_step") == 0, (
        "the shipped `body_step` is no longer the control arm; `H-125` and this test disagree")
    before = {pid: p.body for pid, p in w.persons.items()}

    d = SeasonDriver(w)
    w.step = Step.MATTER
    evs = d.matter([])

    assert w._subsistence_shortfall, "nobody is short on a bare world; the arm proves nothing"
    assert {pid: p.body for pid, p in w.persons.items()} == before, (
        "a body moved at `body_step = 0` — the control arm is not the pre-item tree")
    assert not [e for e in evs if e.kind in ("body.changed", "person.died")], (
        f"the zero arm emitted a body event: {[e.kind for e in evs]}")


def test_lb3c_death_at_body_zero_closes_every_tenure_through_the_same_owner_as_kill():
    """**LB-3c.** A body reaching 0 at MATTER must end every live edge NAMING that person — the
    same cascade `kill / wound` runs at RESOLVE, through the same owner.

    ⚠ IT PLANTS THE EDGE `W-E` MEASURED DANGLING: a `tie` **another person owns** that names the
    dying one as its OBJECT. `p.tenures` is the edges this person is the SUBJECT of (§15.1), so a
    cascade scanning only that list cannot see it, and §15.3 is explicit that the tenure ends
    THROUGH the death. This is why `World.remove_person` scans `w.tenures`.

    ⚠ THE LITERAL FORM OF `LB-3c` IS NOT USED, AND THE REASON IS RECORDED RATHER THAN THE CHECK
    QUIETLY SOFTENED. `05_LEDGER_AND_BUILD.md` writes it as *"`grep -c "t.until = w.tick"
    engine/season` must be 1"*. That count is **5** on this tree and each of the five is a
    DIFFERENT closure — `confer` ending a prior hold, `release` ending what the actor owns,
    `revoke`, and so on — none of them the death cascade. Taking the grep literally would require
    deleting four legitimate per-verb closers. What the falsifier is ABOUT is that there is one
    DEATH cascade, and that is asserted directly below, on behaviour rather than on a line
    count."""
    w = _starving_world()
    w.add_tenure(Tenure("t_tie", "p_low", "p_mid", "tie", since=0))
    w.persons["p_mid"].body = 1

    d = SeasonDriver(w)
    w.step = Step.MATTER
    evs = d.matter([])

    assert "p_mid" not in w.persons, "a body reached 0 and the person is still in the world"
    assert [e.subject for e in evs if e.kind == "person.died"] == ["p_mid"]
    assert [t.live for t in w.tenures if t.id == "t_tie"] == [False], (
        "the `tie` another person OWNS, naming the dead one, survived the death and now dangles")
    assert not [t for t in w.tenures if t.live and "p_mid" in (t.subject, t.object)], (
        "a live edge still names a dead person")

    # ONE OWNER, asserted on the source: `_eff_kill` must not carry its own copy of the cascade.
    import inspect
    from ..loop import effects as _effects
    body = inspect.getsource(_effects._eff_kill)
    assert "remove_person" in body, "`_eff_kill` no longer routes through the one owner"
    assert "t.until = w.tick" not in body, (
        "`_eff_kill` has grown its own cascade again — two sites closing tenures by hand is how "
        "MATTER's death and RESOLVE's drift apart (§8)")
