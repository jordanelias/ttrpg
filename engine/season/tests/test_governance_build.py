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

import ast
import dataclasses

import pytest

from collections import Counter

from ..data import files
from ..data.matrix import MATRIX, Step
from ..data.rosters import CONFERRAL_BASES, REVOCATION_BASES, RUNG_KINDS, TITLE_DOMAINS, title_domain
from ..data.verbs import VERB_TABLE
from ..epistemic import CHANNEL_PREDICATES
from ..gaps import Forbidden, Unowned, Unspecified
from ..data.cast import faction_leader
from ..harness.populated import build_realm
from ..loop import predicates as _preds
from ..loop.driver import SeasonDriver, resolvable_verbs
from ..loop.predicates import in_holdings, office_described_by
from ..queries import world_q
from ..harness import probes as P
from ..decision import budget as _budget
from ..decision import operands_for, person_side_eligible
from ..state.carriers import (
    Act, Office, Person, Proposition, Rung, Tenure, View, matrix_rows_without_a_field,
    refuse_a_title_in_a_body,
)


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


# =================================================================================================
# LB-6d -- THE BENEFICIARY COLUMN (`CAT-2`, phase-6 item `6d`)
#
# What these assert, and the order matters: the column is DECLARED on every row (and the loader
# refuses a row without one), the declaration is CARRIABLE by the row that makes it, and the
# resolution RUNS on candidates the engine actually forms. The third is the one that could have
# been vacuous -- a column that resolves to nothing is CAT-2's dead option 1 relocated, and
# `benefits_me` would read 0.0 forever with every test green.
# =================================================================================================


def _verb_table_text() -> str:
    from ..data import files
    return files.VERB_TABLE_YAML.read_text()


def _load_with(table_text: str):
    """Reload the verb table from SUBSTITUTED text, pointing the loader at a TEMPORARY FILE.

    ⚠⚠ THIS USED TO WRITE THE TRACKED `engine/season/verb_table.yaml` AND RESTORE IT IN A
    `finally`, AND THAT WAS UNSAFE IN THE ONE CONFIGURATION CI ACTUALLY RUNS.
    `.github/workflows/valoria-ci.yml:351` runs `pytest engine/season/tests -q -n auto`, and
    xdist's default `--dist load` spreads one file's tests across workers. Two failures follow
    from writing the real path:
      * ANOTHER worker reading the table mid-arm (`test_season_shape.py` reads it directly in
        three places) sees a deliberately broken table and goes red for a reason unrelated to
        what it tests;
      * two `_load_with` calls OVERLAPPING leave the repo file corrupted for good — B snapshots
        A's broken arm as its `original`, A restores the real text, then B's `finally` writes
        A's broken arm back. A process killed between the write and the `finally` does the same
        with one worker.
    A test that can leave a tracked source file broken is not a strong test with a caveat; it is
    a test that edits the repository. The substituted table now lives in a `tmp` file and only
    the MODULE-LEVEL binding moves, so nothing outside this process can observe the arm and
    there is no path that mutates the working tree."""
    import importlib
    import tempfile
    from pathlib import Path
    from ..data import files, verbs as _verbs
    real = files.VERB_TABLE_YAML
    with tempfile.TemporaryDirectory() as d:
        arm = Path(d) / "verb_table.yaml"
        arm.write_text(table_text)
        files.VERB_TABLE_YAML = arm
        try:
            importlib.reload(_verbs)
        finally:
            files.VERB_TABLE_YAML = real
            importlib.reload(_verbs)


_LEVY_ROW = (
    '  - verb:        "levy"\n'
    '    scale:   "settlement"\n'
    '    scale_note: "a levy moves a Rung\'s stores -- the rung IS the subject"\n'
    '    stratum:     "uncontested_material"\n'
    '    eligibility: ["remit:issue", "presence:<rung>"]\n'
    '    beneficiary: "actor"\n'
)


def test_lb6d_every_verb_declares_a_rostered_beneficiary():
    """**LB-6d.** `CAT-2`: *"DECLARE IT -- and declare it as a STATIC COLUMN ON `verb_table.yaml`
    resolving to a carrier a Candidate ALREADY holds."* Every row, no exceptions, from the
    roster."""
    from ..data.verbs import BENEFICIARY_KINDS, VERB_TABLE

    # Same control as `test_season_shape.py`'s own `len(_load_verb_table()) == 38`: it is here so
    # that a table which SHRANK cannot let this census pass while examining a handful of rows.
    # [JUSTIFIED: the verb count is READ from verb_table.yaml, never chosen -- the control that stops this census passing over a loader that returned a subset]
    assert len(VERB_TABLE) == 38, "the verb count moved; this row's census is stale"
    undeclared = [v for v, r in VERB_TABLE.items() if not r.beneficiary]
    assert not undeclared, f"verbs with no `beneficiary:`: {undeclared}"
    off_roster = [(v, r.beneficiary) for v, r in VERB_TABLE.items()
                  if r.beneficiary not in BENEFICIARY_KINDS]
    assert not off_roster, f"beneficiaries outside `beneficiary_kinds`: {off_roster}"
    # ⚠ WHAT STOOD HERE WAS TAUTOLOGICAL AND CLAIMED NOT TO BE. It rebuilt `declared` with the
    # NEGATION of the `off_roster` predicate asserted empty one line above, so
    # `len(declared) == len(VERB_TABLE)` held unconditionally, and the empty-table case its
    # comment invoked is already excluded by the `== 38` assertion at the top. A comment claiming
    # a §0.1 pt 2 vacuity guard that the code does not provide is worse than no guard.
    # The real vacuity risk is the OTHER direction -- a census that examined rows carrying no
    # column at all -- so it is the DISTRIBUTION that is pinned, which a broken loader cannot fake.
    kinds = Counter(r.beneficiary for r in VERB_TABLE.values())
    assert set(kinds) <= set(BENEFICIARY_KINDS) and sum(kinds.values()) == len(VERB_TABLE)
    assert kinds["none"] < len(VERB_TABLE), (
        f"every row declares `none` ({kinds}) -- the column is present and says nothing, which "
        "this census would otherwise report as full coverage")


def test_lb6d_a_row_without_the_column_is_refused_at_load():
    """The column is REQUIRED, so a new verb cannot arrive carrying no declaration. An absent
    column would read as `benefits nobody` for that verb -- the UNKNOWN/False collapse."""
    src = _verb_table_text()
    dropped = src.replace(_LEVY_ROW, _LEVY_ROW.replace('    beneficiary: "actor"\n', ""), 1)
    assert dropped != src, "the substitution did not apply -- this test is asserting nothing"
    with pytest.raises(SystemExit, match="declares no `beneficiary:`"):
        _load_with(dropped)


def test_lb6d_an_off_roster_beneficiary_is_refused_at_load():
    """`beneficiary_kinds` is the closed set. A fifth carrier is argued for in `rosters.yaml`,
    never spelled into a cell.

    ⚠ IT EXPECTS `SystemExit`, AND IT EXPECTED `Unspecified` UNTIL 2026-09-18. The check went
    through `require_member`, which raises the PER-ACT gap type -- so a broken table imported
    inside `corpus_run.run_case`'s try block was caught there and reported as one case's
    DESIGN-GAP. `H-115`'s split is that load-time refusals are fatal `SystemExit`; this row is
    load-time, so it raises that now and this assertion follows it."""
    src = _verb_table_text()
    bogus = src.replace(_LEVY_ROW, _LEVY_ROW.replace('"actor"', '"treasury"'), 1)
    assert bogus != src, "the substitution did not apply -- this test is asserting nothing"
    with pytest.raises(SystemExit, match="not in `beneficiary_kinds`"):
        _load_with(bogus)


def test_lb6d_an_operand_beneficiary_the_row_cannot_carry_is_refused_at_load():
    """⚠ THE CHECK THAT KEEPS THE COLUMN HONEST, AND THE REASON `CAT-2` CLOSED THE WAY IT DID.

    Option 1 -- derive the beneficiary from the operand binding -- died on a measurement: 24 of 38
    verbs are UNTYPED and carry no operand at all. A static column escapes that only while it
    declares carriers the row can actually hold. `beneficiary: to` on an untyped verb is the SAME
    dead reference wearing the new column, and it would resolve to `None` for every candidate ever
    formed, silently, forever."""
    src = _verb_table_text()
    unbindable = src.replace(
        _LEVY_ROW, _LEVY_ROW.replace('beneficiary: "actor"', 'beneficiary: "to"'), 1)
    assert unbindable != src, "the substitution did not apply -- this test is asserting nothing"
    with pytest.raises(SystemExit, match="neither binds nor admits"):
        _load_with(unbindable)


def test_lb6d_kill_is_declared_to_benefit_the_actor_not_the_person_it_writes_on():
    """⚠ THE ROW THAT PROVES THE COLUMN CANNOT BE DERIVED FROM `writes:`.

    `kill / wound` writes `Person.body` and `Person.exists` ON THE SUBJECT. A rule reading the
    write column would name the victim as the beneficiary of their own killing, because A WRITE
    CAN BE A HARM. This is the falsifier for the claim that the declaration is load-bearing: if
    someone later derives this column, THIS is the assertion that goes red."""
    from ..data.verbs import VERB_TABLE

    row = VERB_TABLE["kill / wound"]
    assert "Person.body" in row.writes and "Person.exists" in row.writes, (
        "the row no longer writes on its subject, so this test's premise is gone")
    assert row.beneficiary == "actor", (
        "`kill / wound`'s beneficiary was derived from `writes:` and now names the victim")


def test_lb6d_none_and_an_unbound_carrier_are_different_answers():
    """`beneficiary_of` returns `None` twice over and the two are NOT the same claim. `none` is
    the verb's answer; an unbound carrier is a hole. The ROW discriminates them, which is why the
    resolver returns an id rather than a tri-state."""
    from ..data.verbs import VERB_TABLE
    from ..decision.choose import beneficiary_of, benefits_me
    from ..state.carriers import Candidate, Person

    p = Person(id="p1")
    declared_none = Candidate(verb="create_record", subject="rec1")
    assert VERB_TABLE["create_record"].beneficiary == "none"
    assert beneficiary_of(p, declared_none) is None

    hole = Candidate(verb="transfer", subject="r1", operands={})
    assert VERB_TABLE["transfer"].beneficiary == "to"
    assert beneficiary_of(p, hole) is None, "an unbound `to` resolved to something"

    bound = Candidate(verb="transfer", subject="r1", operands={"to": "p3"})
    assert beneficiary_of(p, bound) == "p3"
    assert benefits_me(p, bound) == 0.0
    assert benefits_me(p, Candidate(verb="levy", subject="r1")) == 1.0


def test_lb6d_the_column_resolves_on_candidates_the_engine_actually_forms():
    """⚠⚠ THE ONE THAT IS NOT SATISFIABLE BY DECLARING ANYTHING (`CLAUDE.md` §0.2).

    Every test above reads the table or a hand-built Candidate. This one runs a season, takes
    every Candidate the deliberation ACTUALLY forms, and resolves each against its row. The
    failure it excludes is the one that matters: a column that declares carriers real candidates
    never hold resolves to `None` throughout, `benefits_me` reads 0.0 for everybody, and every
    other assertion in this block still passes.

    IT ASSERTS THAT IT ASSERTED (§0.1 pt 2) -- the examined count is asserted non-trivial, so a
    run that formed no candidates fails here instead of passing vacuously.

    ⚠ THE CONTROL ON ITS OWN HEADLINE, because a number without one is not a measurement (§0.1
    pt 4): roughly HALF of all candidates carry THE ACTOR AS THEIR OWN SUBJECT -- `opening_set`
    offers every person themselves as a referent for every verb. So the count of candidates
    reading `benefits_me == 1.0` is inflated by the aperture's shape and must not be read as
    *"persons are self-interested two thirds of the time"*. That is a property of the candidate
    former, which this item does not touch and this test does not assert a bound on."""
    from ..data.verbs import VERB_TABLE
    from ..decision import choose as _choose
    from ..harness import populated

    seen: list = []
    inner = _choose.opening_set

    def spy(person, view, question, fx):
        cands = inner(person, view, question, fx)
        seen.extend((person, c) for c in cands)
        return cands

    _choose.opening_set = spy
    try:
        populated.run(seasons=1, seed=0)
    finally:
        _choose.opening_set = inner

    # A FLOOR, not a measurement. The season forms 5,345 candidates at this seed (§7.3e, re-taken
    # by `probe_execution_pass.py`), so this sits far below the observed figure and is deliberately
    # NOT pinned to 5,345 -- pinning it would reland every unrelated aperture change here as a
    # false failure, which is how a guard stops being read.
    # [JUSTIFIED: a floor far below the 5,345 measured at this seed, chosen only to fail a sweep that ran thinly or not at all -- the vacuous pass this test exists to exclude]
    assert len(seen) > 1000, (
        f"only {len(seen)} candidates were formed; this sweep cannot observe what it is for")

    # ⚠⚠ THIS ZERO IS STRUCTURAL, NOT MEASURED, AND THE ITEM PRESENTED IT AS ITS RESULT.
    # Traced end to end after the fact: `actor` -> `p.id`, never None. `subject` -> `c.subject`,
    # and `opening_set` only ever builds a Candidate from `q.referents`, so it is never falsy.
    # `to` is declared by ONE row (`transfer`) whose form lists `to` in `needs:`, and
    # `_derive_operand` answers `to` with `return subject` (`options.py:309`) -- so it cannot be
    # None either. `holes` is therefore 0 for reasons in the CODE, not in the data, and the
    # assertion below cannot fail while that holds. Kept because it is a real regression guard on
    # those three paths, but it is NOT evidence that the column was declared well, and the
    # records that read it that way are corrected. The measurement that would bear on THAT is the
    # coverage line beneath it: 10 of the 38 rows (every `remit:`-gated verb, `confer` among
    # them) form zero candidates, so their declarations are never exercised here at all.
    holes = [(p.id, c.verb) for p, c in seen
             if VERB_TABLE[c.verb].beneficiary != "none"
             and _choose.beneficiary_of(p, c) is None]
    assert not holes, (
        f"{len(holes)} candidates declare a beneficiary that did not resolve, e.g. {holes[:5]}. "
        "A declared carrier that never binds is CAT-2's dead option 1 inside the new column")

    resolved = sum(1 for p, c in seen if _choose.beneficiary_of(p, c) is not None)
    assert resolved > len(seen) // 4, (
        f"only {resolved} of {len(seen)} candidates resolve any beneficiary -- the column is "
        "declared but inert, which is the failure this test exists to see")

    # The term SPANS its codomain. A `benefits_me` that is constant across candidates is inert by
    # construction (`urgency`'s own note: "a term constant across candidates is INERT BY
    # CONSTRUCTION -- the dead-carrier complaint"), whatever `orient` later multiplies it by.
    values = {_choose.benefits_me(p, c) for p, c in seen}
    assert values == {0.0, 1.0}, f"`benefits_me` never varied across a season: {values}"

# LB-6e -- `(Person, scar[axis])`, THE MORAL LAYER'S MISSING MOTION (§54 item 21, `H-128`)
#
# `04 §F.20a`: *no verb writes any `Person` interior field at all*, so every interior consequence
# is inert and a person leaves a season morally identical to the one who entered it. This is the
# one interior row whose TRIGGER the chain actually specifies, so it is the one that can be built
# without inventing the condition.
#
# THE SHIPPED ARM IS `scar_step = 0` AND IS PINNED BELOW. Every other test here sets the fixture
# explicitly, so the behaviour is EXERCISED rather than merely present (`CLAUDE.md` §0.2).
# =================================================================================================


def _scar_bands(scar_step, ids=range(24)):
    """Fold `kill / wound` through the REAL road at a given `scar_step`, and report each band's
    scar. Deliberately `_we_bands`' shape (`test_season_shape.py`) rather than a new harness: the
    act id is the only thing that varies, because `combat_seam` seeds its RNG from it, so nothing
    about the WORLD is tuned to reach a band."""
    from ..data.matrix import Step as _Step
    from ..state.carriers import Act as _Act

    seen = {}
    for i in ids:
        w = P.tiny_world()
        w.step = _Step.RESOLVE
        w.fixtures = w.fixtures.sweep("scar_step", scar_step)
        d = SeasonDriver(w)
        act = _Act(id=f"scar{i}", actor="p_low", verb="kill / wound",
                   payload={"subject": "p_mid"})
        evs = d.resolve([act], w.fixtures.get("contest_max_depth"))
        deg = evs[0].degree if evs else None
        alive = "p_mid" in w.persons
        seen.setdefault(deg, dict(
            alive=alive,
            scar=(dict(w.persons["p_mid"].scar) if alive else None),
            kinds=sorted(e.kind for e in evs)))
    return seen


def test_lb6e_the_matrix_row_finally_has_a_field():
    """`formal_analysis.md` C3 measured it: *"`matrix_rows_without_a_field()['absent']` lists
    `(Person, scar)`"*. A Part D row naming a field that does not exist is a licence pointing at
    nothing."""
    from ..state.carriers import Person

    p = Person(id="p1")
    assert hasattr(p, "scar"), "`(Person, scar)` still names a field the carrier does not have"
    assert p.scar == {}, (
        "`scar` ships pre-seeded. It is keyed on the AXIS ROSTER, and `STR-2` rules those members "
        "change -- seeding them here would put a copy of a roster about to be replaced into a "
        "carrier (§0.05 clause 3)")


def test_lb6e_a_wound_scars_and_the_axes_come_from_the_alignment_table():
    """**LB-6e**, and it observes BOTH halves: that a scar is WRITTEN, and that its KEYS are the
    ones `ALIGNMENT` engages -- not a second table, and not a literal.

    §8: `ALIGNMENT` already owns *which axes a verb engages*, and `choose` scores against it. A
    second outcome->axis table would be a second owner of that claim, free to disagree with the
    one the decision layer reads."""
    from ..data.rosters import PURSUIT_AXES
    from ..data.verbs import ALIGNMENT, ALIGNMENT_DEFAULT_CELL
    from ..seam.wrappers import combat as C
    if C.engine() is None:                      # a NAMED gap, never a silent skip
        pytest.skip(f"personal_combat engine unavailable: {C.load_error()}")

    engaged = {ax for ax in PURSUIT_AXES
               if float(ALIGNMENT.get(ax, {}).get("kill / wound", ALIGNMENT_DEFAULT_CELL))}
    if not engaged:
        pytest.skip("`kill / wound` engages no axis in ALIGNMENT, so this item has nothing to key "
                    "a scar on -- a data state, reported rather than asserted around")

    seen = _scar_bands(scar_step=10)
    wounded = [v for k, v in seen.items() if k == "Wounded"]
    assert wounded, (
        f"the sweep reached bands {sorted(str(k) for k in seen)} and never `Wounded`, so this "
        "test asserted nothing about a scar")
    got = wounded[0]["scar"]
    assert got, "a wound at `scar_step=10` left no scar at all"
    assert set(got) <= set(PURSUIT_AXES), (
        f"scar is keyed on {sorted(set(got) - set(PURSUIT_AXES))}, which the axis roster does "
        "not carry -- the keys came from somewhere other than the roster")
    assert set(got) == engaged, (
        f"scar keys {sorted(got)} != the axes ALIGNMENT engages for this verb {sorted(engaged)}; "
        "a second owner of *which axes a verb engages* has appeared")
    assert all(v > 0 for v in got.values()), got


def test_lb6e_the_zero_arm_writes_no_scar_and_reports_none():
    """THE SHIPPED ARM, PINNED. At `scar_step = 0` `_scar` returns BEFORE touching the carrier, so
    no key is added. A zero-valued cell would still be a key, which is the difference between an
    arm that is inert and one that merely looks it.

    ⚠ THIS PINS THE BEHAVIOUR, NOT THE WHOLE TREE, AND THE NARROWER NAME IS A CORRECTION. It was
    called `..._is_the_pre_item_tree_exactly` and that was FALSE: `World.content_hash` digests a
    dataclass as `repr(obj)`, so `Person` gaining a field moves every person's digest whatever its
    value (`ff5c5765f4d2` -> `ab77c30d273b`, measured against a clean `origin/main` worktree).
    `runs/TRACE.txt` IS byte-identical -- no behaviour changes -- and that is the claim this test
    can actually make. `H-128` carries the full accounting of the two-line re-record."""
    from ..seam.wrappers import combat as C
    if C.engine() is None:
        pytest.skip(f"personal_combat engine unavailable: {C.load_error()}")

    seen = _scar_bands(scar_step=0)
    assert seen, "the sweep folded nothing; this pin asserts nothing"
    scarred = {k: v["scar"] for k, v in seen.items() if v["alive"] and v["scar"]}
    assert not scarred, (
        f"the control arm wrote a scar: {scarred}. `scar_step=0` must reproduce the pre-item tree "
        "exactly, or this item moved a golden it claims not to have")
    # ⚠ THE ASSERTION THAT STOOD HERE COULD NOT FAIL, AND SAYING WHY IS THE REPAIR. It read
    # `assert "scar.taken" not in v["kinds"]` -- but `scar.taken` is in NO band's `emits:` in
    # `verb_table.yaml`, so `emits_at` can never return it, for any band, any fixture value and
    # any future edit short of adding the column. That is §0.1 pt 2 exactly: an absent test
    # wearing a present one's clothes, sitting inside this item's own control. What is actually
    # worth pinning is that the table has not GROWN the kind while the magnitude is still 0 --
    # which is a claim about the data, so it is asserted against the data.
    from ..data.verbs import VERB_TABLE
    row = VERB_TABLE["kill / wound"]
    declared = {k for band in row.emits_by_degree for k in row.emits_by_degree[band]}
    assert "scar.taken" not in declared, (
        "`scar.taken` has been added to this verb's `emits:` while `scar_step` still ships at 0, "
        "so every wound now reports a scar that was not written -- the `ID-9` defect the row's "
        f"own note refuses. Declared kinds: {sorted(declared)}")


def test_lb6e_a_verb_that_engages_no_axis_scars_nothing():
    """THE CONTROL ON THE MECHANISM, not on the magnitude (§0.1 pt 4). `_scar` keys off
    `ALIGNMENT`, so a verb with no engaged axis must leave no scar even at a large step. Without
    this, `_scar` could be scarring every axis unconditionally and the test above -- which only
    checks the keys it DOES find -- would not see it."""
    from ..data.rosters import PURSUIT_AXES
    from ..loop.effects import _scar
    from ..state.carriers import Person

    w = P.tiny_world()
    w.fixtures = w.fixtures.sweep("scar_step", 10)
    p = Person(id="p_test")
    _scar(w, p, "no_such_verb_engages_no_axis")
    assert p.scar == {}, (
        f"a verb engaging no axis still scarred {p.scar} -- `_scar` is not reading ALIGNMENT, it "
        "is writing every axis unconditionally")
    # AND THE POSITIVE ARM, so this is not a test that passes because `_scar` never writes.
    engaged = [ax for ax in PURSUIT_AXES if ALIGNMENT_OF("kill / wound", ax)]
    if engaged:
        q = Person(id="p_test2")
        _scar(w, q, "kill / wound")
        assert q.scar, "`_scar` wrote nothing for a verb that DOES engage an axis; the negative "\
                       "arm above proves nothing on its own"


def ALIGNMENT_OF(verb, axis):
    from ..data.verbs import ALIGNMENT, ALIGNMENT_DEFAULT_CELL
    return float(ALIGNMENT.get(axis, {}).get(verb, ALIGNMENT_DEFAULT_CELL))


# =================================================================================================
# PLAN POSITION `13f` -- `establish` HAS AN EFFECT.
# `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`, position `13f`, which is a
# later plan than this file's `LB-n` sheet; the tests carry the position id instead. Its FALSIFIER,
# observed in both halves: a planted `establish` on an EXISTING id changes a sitting holder's
# `granted_acts` and publishes a `tenure.payload_set` naming that holder's Tenure, while a
# hand-mutation of the office reaches nobody (`test_h71_the_grant_is_a_snapshot_not_a_mirror`,
# `test_season_shape.py`, is that half); and an `establish` naming no belonging, or an unknown one,
# emits `establish.refused`, constructs nothing and lets no exception escape the fold.
# =================================================================================================

def _establish_world():
    """`tiny_world`, unchanged. Its duke `p_high` holds `off_duke`, whose remit grants `confer` --
    the eligibility `establish` declares -- and `p_mid` holds no office."""
    w = P.tiny_world()
    d = SeasonDriver(w)
    d.matter([])
    return w, d


def _founding(**over) -> dict:
    """A well-formed `establish` payload for an office `tiny_world` does not have. `appointed` is
    one of the three conferral values `ED-IN-0256` rules, and since `13d-i` rostered them the
    basis test passes nothing else."""
    p = dict(office="off_reeve", post="Reeve", rung="S", remit=["issue", "dispatch"],
             faction="Crown", conferral="appointed")
    p.update(over)
    return p


def _establish(w, d, aid: str, payload, actor: str = "p_high") -> list:
    return d.resolve([Act(id=aid, actor=actor, verb="establish", payload=payload)],
                     contest_max_depth=w.fixtures.get("contest_max_depth"))


def _seat_reeve(w, remit):
    """An EXISTING office with a conferral basis and a sitting holder, seated through
    `add_tenure` so the holder's grant is the snapshot `_grant_remit` takes at seating. The
    payload carries a key of another writer's, so the re-stamp is seen to be key-scoped."""
    w.offices["off_reeve"] = Office("off_reeve", "Reeve", "S", list(remit),
                                    conferral="appointed", faction="Crown")
    w.add_tenure(Tenure("t_reeve", "p_mid", "off_reeve", "hold", 0, payload={"note": "kept"}))
    [t] = [t for t in w.tenures if t.id == "t_reeve"]
    return t


def test_13f_the_remit_row_is_keyed_on_the_field_the_office_has():
    """Instruction (1). Part D's `(Office, remit)` named a field `Office` does not have, so the gate
    licensed a cell nothing could write and `matrix_rows_without_a_field()` listed it. The ROW is
    renamed at its owner, to the field the constructor validates and every remit check reads."""
    fields = {f.name for f in dataclasses.fields(Office)}
    assert "remit_acts" in fields and "remit" not in fields, sorted(fields)
    assert ("Office", "remit_acts") in MATRIX and ("Office", "remit") not in MATRIX
    assert ("Office", "remit_acts") not in matrix_rows_without_a_field()["absent"]
    assert not [k for k in matrix_rows_without_a_field()["absent"] if k[0] == "Office"], (
        "an `Office` row still names a field the carrier does not have")
    assert "Office.remit_acts" in VERB_TABLE["establish"].writes
    assert "remit.changed" in MATRIX[("Office", "remit_acts")].emits


def test_13f_a_planted_establish_founds_the_office_and_grants_a_hold_opened_before_it():
    """THE CONCRETE CASE THE POSITION NAMES: a `hold` opened on an office id before the office
    exists gets no grant (`_grant_remit` traces and stamps nothing), and `establish` then creates
    the office. The act re-stamps that holder in the same act, and the person-side reader sees it."""
    w, d = _establish_world()
    w.add_tenure(Tenure("t_early", "p_mid", "off_reeve", "hold", 0))
    [t] = [t for t in w.tenures if t.id == "t_early"]
    mid = w.persons["p_mid"]
    assert "off_reeve" not in w.offices and t.granted_acts == (), "fixture: not the early-hold case"
    assert not person_side_eligible(mid, VERB_TABLE["dispatch"]), "fixture: p_mid can dispatch"

    out = _establish(w, d, "e_found", _founding())
    kinds = [e.kind for e in out]
    assert kinds == ["office.established", "tenure.payload_set"], kinds
    off = w.offices["off_reeve"]
    assert (off.post, off.rung, off.remit_acts, off.faction, off.conferral) == (
        "Reeve", "S", ["issue", "dispatch"], "Crown", "appointed"), off
    assert off.establishment == [], "the effect wrote `establishment`, which is `17a`'s to delete"
    assert t.granted_acts == ("issue", "dispatch"), (
        f"the early holder's grant is {t.granted_acts} -- the act did not re-stamp it")
    assert person_side_eligible(mid, VERB_TABLE["dispatch"]), (
        "the grant is on the Tenure and the person-side reader still refuses the remit verb")
    ps = next(e for e in out if e.kind == "tenure.payload_set")
    assert t.id in {c.subject for c in ps.changes}, [c.subject for c in ps.changes]


def test_13f_an_office_nobody_holds_publishes_no_payload_set():
    """`tenure.payload_set` is EARNED by a re-stamped holder, never published for one that is not
    there -- the fabricated-emission class `_fold`'s own comments name. The success is still
    published: the office was founded."""
    w, d = _establish_world()
    out = _establish(w, d, "e_bare", _founding())
    assert [e.kind for e in out] == ["office.established"], [e.kind for e in out]
    assert "off_reeve" in w.offices


def test_13f_an_establish_on_an_existing_id_changes_the_remit_and_reaches_the_sitting_holder():
    """**THE POSITION'S FALSIFIER.** Both halves, in one world and in order, so neither can pass
    for the other's reason:

      * SNAPSHOT: a hand-mutation of `w.offices[x].remit_acts` does NOT reach the sitting holder;
      * MIRROR'S OBSERVABLE, BY AN ACT: a planted `establish` on the EXISTING id rewrites the
        remit in place, emits `remit.changed` and NOT `office.established`, changes the sitting
        holder's `granted_acts`, and publishes a `tenure.payload_set` naming that holder's Tenure.

    And the act that changes nothing is refused rather than reported: re-running it writes
    nothing, so the fold emits `establish.refused`."""
    w, d = _establish_world()
    t = _seat_reeve(w, ["issue"])
    mid = w.persons["p_mid"]
    assert t.granted_acts == ("issue",), f"fixture: seating stamped {t.granted_acts}"

    # SNAPSHOT: the hand-mutation reaches nobody.
    w.offices["off_reeve"].remit_acts = ["issue", "convene"]
    assert t.granted_acts == ("issue",), "a hand-mutation re-granted a sitting holder"
    assert not person_side_eligible(mid, VERB_TABLE["convene"])

    office = w.offices["off_reeve"]
    out = _establish(w, d, "e_remit", _founding(remit=["issue", "dispatch"]))
    kinds = [e.kind for e in out]
    assert kinds == ["remit.changed", "tenure.payload_set"], kinds
    assert w.offices["off_reeve"] is office, "the office was re-founded, not re-remitted in place"
    assert office.remit_acts == ["issue", "dispatch"], office.remit_acts
    assert t.granted_acts == ("issue", "dispatch"), (
        f"the sitting holder's grant is {t.granted_acts}: the act changed the office and did not "
        "reach the holder -- `_grant_remit(force=True)` is not being called, or is still a setdefault")
    assert t.payload.get("note") == "kept", "the re-stamp overwrote a key it does not own"
    assert person_side_eligible(mid, VERB_TABLE["dispatch"])
    assert not person_side_eligible(mid, VERB_TABLE["convene"]), (
        "the hand-mutation's `convene` survived -- the grant is the ACT's remit, not a union")
    ps = next(e for e in out if e.kind == "tenure.payload_set")
    assert t.id in {c.subject for c in ps.changes}, [c.subject for c in ps.changes]

    again = _establish(w, d, "e_again", _founding(remit=["issue", "dispatch"]))
    assert [e.kind for e in again] == ["establish.refused"], [e.kind for e in again]


@pytest.mark.parametrize("change", [
    dict(faction="Church of Solmund"),
    dict(post="Warden"),
    dict(rung="Hh"),
    dict(conferral="elected"),
    # ⚠ (`13d-i`) WAS `revocation="purview"`, r2's superseded value. Off the roster it now raises
    # in the constructor, so the act would refuse for THAT reason and this case would stop
    # observing a basis DIFFERENCE. The rostered value differs from the seat's `None` and constructs.
    dict(revocation="rung_above_same_faction"),
], ids=lambda c: next(iter(c)))
def test_13f_an_existing_id_refuses_any_change_but_the_remit(change):
    """Re-founding -- a different belonging, post, rung or basis on an id that exists -- is not a
    write `establish` declares, so it REFUSES and touches neither the office nor the holder. The
    control is in the same world: the same act without the change is admitted.

    ⚠ **ASSERTS THE OFFICE STILL CONSTRUCTS (added 2026-09-26, antagonist finding).** Without this,
    a future off-roster `change` value would refuse for the WRONG reason -- the constructor raising
    inside `office_described_by`, translated to `False` before clause 4's basis-difference check
    ever runs -- and this test would keep passing while testing nothing about re-founding. Each
    `change` here must still be a WELL-FORMED office, differing from the seated one by exactly the
    one declared field, or the case is not exercising what its `id` claims."""
    w, d = _establish_world()
    t = _seat_reeve(w, ["issue"])
    plain = _founding(remit=["issue", "dispatch"])
    assert _preds._req_establish(w, Act(id="ctl", actor="p_high", verb="establish",
                                        payload=plain)), "control: the unchanged act is refused"

    changed_payload = {**plain, **change}
    changed_act = Act(id="check_constructs", actor="p_high", verb="establish", payload=changed_payload)
    changed_office = office_described_by(changed_act)  # raises if this `change` is off-roster/malformed
    assert changed_office is not None, (
        f"{change}: the payload did not describe a constructible Office at all")

    out = _establish(w, d, "e_refound", changed_payload)
    assert [e.kind for e in out] == ["establish.refused"], [e.kind for e in out]
    assert w.offices["off_reeve"].remit_acts == ["issue"]
    assert t.granted_acts == ("issue",)


# `raises` marks the payloads the CONSTRUCTOR itself rejects, so each refusal below is shown to
# have intercepted a real raise rather than to have been a no-op nothing would have tripped.
@pytest.mark.parametrize("payload,raises", [
    ({}, False),
    (_founding(faction=None), True),                                   # belongs to nothing
    (_founding(faction="Nowhere Brotherhood"), True),                  # an unknown faction
    (_founding(faction=None, body="Office of Nothing"), True),         # an unknown body
    (_founding(body="Imperial Court", faction="Church of Solmund"), True),   # a mismatch
    (_founding(remit=["issue", "levy"]), True),                        # off `REMIT_ACTS`
    (_founding(post="Duke", faction=None, body="Imperial Court"), True),     # a title in a body
    (_founding(rung="nowhere"), False),                                # a rung the world lacks
    (_founding(conferral=None), False),                                # no conferral basis
    (_founding(office="p_low"), False),                                # an id a person holds
], ids=["empty", "no-belonging", "unknown-faction", "unknown-body", "mismatch", "off-roster-remit",
        "title-in-body", "unknown-rung", "no-basis", "person-id"])
def test_13f_an_unfoundable_establish_refuses_constructs_nothing_and_raises_nothing(payload, raises):
    """The fold's FIRST refusal path: the precondition returns False and the fold emits
    `emits_on_refusal`. Asserted on the Event -- the fold is called bare, so a raise escaping it
    fails this test as an error rather than passing silently."""
    w, d = _establish_world()
    before = dict(w.offices)
    act = Act(id="e_bad", actor="p_high", verb="establish", payload=payload)
    if raises:
        with pytest.raises((Unowned, Unspecified, Forbidden)):
            office_described_by(act)
    out = d.resolve([act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["establish.refused"], [e.kind for e in out]
    assert w.offices == before, f"an office was constructed: {sorted(set(w.offices) - set(before))}"


def test_13f_a_computed_establish_carries_no_operands_and_refuses():
    """The row is resolvable now and still untyped, so a COMPUTED `establish` forms with NO
    operands -- `operands_for` returns `{}` -- and must refuse until `15c` widens the operand
    vocabulary. What the chooser puts on its payload is the question's referent as `subject`, and
    that founds nothing."""
    row = VERB_TABLE["establish"]
    assert "establish" in resolvable_verbs()
    assert row.requires_typed is None
    w, d = _establish_world()
    duke = w.persons["p_high"]
    assert person_side_eligible(duke, row), "fixture: the duke cannot form `establish` at all"
    assert operands_for(duke, row, None, "p_low", w.fixtures) == {}
    out = _establish(w, d, "e_computed", {"subject": "p_low"})
    assert [e.kind for e in out] == ["establish.refused"], [e.kind for e in out]


def test_13f_confer_and_establish_ask_one_basis_test(monkeypatch):
    """Instruction (2): the basis test is FACTORED ONCE, so `13d-i` rewrites one function and both
    preconditions inherit it. Observed by behaviour, not by reading source: with the ONE function
    patched to refuse, both predicates refuse an act each admits unpatched. A predicate carrying
    its own copy of the test would go on admitting."""
    w, d = _establish_world()
    w.offices["off_dicastery"].conferral = "appointed"
    conf = Act(id="c_basis", actor="p_high", verb="confer",
               payload={"office": "off_dicastery", "to": "p_mid"})
    est = Act(id="e_basis", actor="p_high", verb="establish", payload=_founding())
    assert _preds._req_confer(w, conf) and _preds._req_establish(w, est), "control: not admitted"
    monkeypatch.setattr(_preds, "has_conferral_basis", lambda off: False)
    assert not _preds._req_confer(w, conf), "`_req_confer` does not ask the shared basis test"
    assert not _preds._req_establish(w, est), "`_req_establish` does not ask the shared basis test"


def test_13f_a_planted_establish_founds_an_office_by_body_not_only_by_faction():
    """`office_described_by`'s `body` branch, otherwise unexercised -- every other test in this
    section founds through `faction`. `Imperial Court` is a body that DERIVES to faction `Crown`
    (`data/rosters.py::office_faction`, `rosters.yaml:1096`), so the constructed `Office` carries
    both: the body as given, and the faction `office_faction` resolved it to."""
    w, d = _establish_world()
    out = _establish(w, d, "e_by_body", _founding(faction=None, body="Imperial Court"))
    assert [e.kind for e in out] == ["office.established"], [e.kind for e in out]
    off = w.offices["off_reeve"]
    assert (off.body, off.faction) == ("Imperial Court", "Crown"), (off.body, off.faction)


def test_13f_the_restamp_skips_a_non_hold_tenure_and_a_dead_hold_on_the_same_office():
    """The re-stamp's filter, `t.kind == "hold" and t.object == off.id and t.live`
    (`loop/effects.py`), is never exercised by the other tests: they seat exactly one live `hold`.
    Plants three tenures on the SAME office -- a live `hold` (re-stamped on every remit change), a
    `commit` naming the office as its object (a different kind, `add_tenure` never grants it), and
    a `hold` that is already closed at seating (`until` set, so `.live` is False from the start) --
    and asserts the re-stamp at `establish` time touches only the first.

    `add_tenure` calls `_grant_remit` for every `hold`, live or not -- the grant is a SNAPSHOT taken
    AT SEATING, not gated on liveness -- so the closed hold IS granted once, to the office's remit
    as it stood when it was seated. What this test isolates is `_eff_establish`'s re-stamp on a
    LATER remit change, which the `.live` filter excludes it from: its grant stays frozen."""
    w, d = _establish_world()
    t_live = _seat_reeve(w, ["issue"])
    w.add_tenure(Tenure("t_commit", "p_low", "off_reeve", "commit", 0))
    w.add_tenure(Tenure("t_dead", "p_low", "off_reeve", "hold", 0, until=1))
    [t_commit] = [t for t in w.tenures if t.id == "t_commit"]
    [t_dead] = [t for t in w.tenures if t.id == "t_dead"]
    assert t_commit.granted_acts == (), "fixture: a `commit` Tenure should never be granted"
    assert t_dead.granted_acts == ("issue",), (
        f"fixture: a `hold`, even dead on arrival, is granted the snapshot AT SEATING -- got "
        f"{t_dead.granted_acts}")

    out = _establish(w, d, "e_restamp_filter", _founding(remit=["issue", "dispatch"]))
    ps = next(e for e in out if e.kind == "tenure.payload_set")
    touched = {c.subject for c in ps.changes}
    # `t_live.id` is in there; `off_reeve` rides along too -- `_apply_write` unions every earned
    # kind's touched ids onto every Event this act produces (the pre-existing `Receipt.field`
    # imprecision `hole_register.yaml`'s `H-71` `source:` already names), not this filter's concern.
    assert t_live.id in touched, touched
    assert t_commit.id not in touched and t_dead.id not in touched, touched
    assert t_live.granted_acts == ("issue", "dispatch"), t_live.granted_acts
    assert t_commit.granted_acts == (), "a `commit` Tenure was re-stamped as though it were a `hold`"
    assert t_dead.granted_acts == ("issue",), (
        f"a CLOSED `hold`'s grant moved off its seating-time snapshot: {t_dead.granted_acts}")


# =================================================================================================
# PLAN POSITION `13e` -- ONE READING OF THE REMIT.
# `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`, position `13e`. Routes
# `loop/resolve.py`'s `_eligible` and `epistemic.py`'s `_ch_post_remit` off the live
# `w.offices[...].remit_acts` and onto the Tenure's own `t.granted_acts` -- the same store
# `decision/options.py` already read, closing the THREE-readings-over-two-stores gap
# `epistemic.py`'s `_ch_post_remit` docstring tracked. FALSIFIER, both arms in one world: a `hold`
# opened before its office exists, then the office HAND-CREATED (no act) -> the resolver now
# REFUSES the remit verb it admitted before this position; the same shape but the office FOUNDED
# BY `establish` -> the resolver ADMITS, because `13f`'s re-stamp reaches the sitting holder. AND
# an AST scan: no `Office.remit_acts` attribute read anywhere in the non-test package outside
# `_grant_remit`, `Office.__post_init__` and `_eff_establish`.
# =================================================================================================


def test_13e_hand_created_office_refuses_act_established_office_admits():
    """**THE POSITION'S FALSIFIER, BOTH ARMS, ONE WORLD.** Two holders, each seated on an office
    id BEFORE that office exists, so each Tenure's `granted_acts` snapshot opens at `()`:

      * `p_mid` on `off_hand` -- the office is then HAND-CREATED (`w.offices[x] = Office(...)`, no
        act). Pre-`13e`, `_eligible` read `w.offices.get(t.object)` live and admitted the moment
        the dict held the id, regardless of the Tenure's own grant. Post-`13e` it reads
        `t.granted_acts`, which a hand-mutation never reaches -- REFUSED.
      * `p_low` on `off_act` -- the office is then FOUNDED BY A PLANTED `establish`. `13f`'s
        effect re-stamps every live `hold` on the id it wrote, so `t.granted_acts` picks up the
        grant in the same act -- ADMITTED.

    Both arms exercise the RESOLVER (`_eligible`, `loop/resolve.py`), not `person_side_eligible`:
    the person-side reading (`decision/options.py`) already read `t.granted_acts` before this
    position and was never the bug -- `13f`'s own falsifier
    (`test_13f_a_planted_establish_founds_the_office_and_grants_a_hold_opened_before_it`) pins the
    ADMIT arm through that reading already. This pins the WORLD-side half `13e` closes, and its
    REFUSE arm is the one no earlier test observes: before this position the resolver admitted it."""
    w, d = _establish_world()
    w.add_tenure(Tenure("t_hand", "p_mid", "off_hand", "hold", 0))
    w.add_tenure(Tenure("t_act", "p_low", "off_act", "hold", 0))
    [t_hand] = [t for t in w.tenures if t.id == "t_hand"]
    [t_act] = [t for t in w.tenures if t.id == "t_act"]
    assert "off_hand" not in w.offices and "off_act" not in w.offices, "fixture: neither exists yet"
    early_holders = [t for t in (t_hand, t_act) if t.granted_acts == ()]
    assert len(early_holders) >= 1, (
        "fixture: no hold was opened before its office existed -- the falsifier is vacuous")

    dispatch = VERB_TABLE["dispatch"]

    # ARM 1 -- HAND-CREATED: no act, so no re-stamp reaches `t_hand`. REFUSE.
    w.offices["off_hand"] = Office("off_hand", "Reeve", "S", ["issue", "dispatch"],
                                    conferral="appointed", faction="Crown")
    assert t_hand.granted_acts == (), "a hand-mutation re-granted a sitting holder"
    act_hand = Act(id="a_hand", actor="p_mid", verb="dispatch", payload={})
    assert not d._eligible(w, act_hand, dispatch), (
        "the resolver admitted `p_mid`'s `dispatch` off a hand-created office -- `_eligible` is "
        "still reading `w.offices[...].remit_acts` live instead of `t.granted_acts`")
    assert not person_side_eligible(w.persons["p_mid"], dispatch), (
        "control: the person-side reading was already correct before this position")

    # ARM 2 -- FOUNDED BY ACT: `establish`'s effect re-stamps `t_act` in the same act. ADMIT.
    out = _establish(w, d, "e_act", _founding(office="off_act"))
    kinds = [e.kind for e in out]
    assert kinds == ["office.established", "tenure.payload_set"], kinds
    assert t_act.granted_acts == ("issue", "dispatch"), (
        f"the act did not reach the sitting holder: {t_act.granted_acts}")
    act_act = Act(id="a_act", actor="p_low", verb="dispatch", payload={})
    assert d._eligible(w, act_act, dispatch), (
        "the resolver refused `p_low`'s `dispatch` after a planted `establish` re-stamped the "
        "grant -- `13f`'s own falsifier and this position's complement")
    assert person_side_eligible(w.persons["p_low"], dispatch)


def test_13e_the_witness_channel_also_reads_the_snapshot_not_the_live_office():
    """`epistemic._ch_post_remit`'s HALF of this position's fix has no behavioural test elsewhere:
    `test_a_binding_decision_lights_the_two_witness_channels_that_needed_one`
    (`test_season_shape.py`) exercises `post_remit` on `off_duke`, whose remit already carries
    `confer` at seating -- it passes identically whether the channel reads `t.granted_acts` or the
    live office, because the two never disagree there. This test builds the disagreement: a holder
    whose OFFICE gains `confer` only AFTER seating (live-only, never in the snapshot), witnessing a
    REAL `confer` Event performed by someone else. Pre-`13e`, `_ch_post_remit` read `w.offices.get
    (t.object).remit_acts` live and would have wrongly admitted this holder as a remit-covering
    witness; post-`13e` it reads `t.granted_acts`, which the live-only grant never reached."""
    w, d = _establish_world()
    w.add_tenure(Tenure("t_hand", "p_mid", "off_hand", "hold", 0))
    [t_hand] = [t for t in w.tenures if t.id == "t_hand"]
    assert "off_hand" not in w.offices, "fixture: not seated yet"
    w.offices["off_hand"] = Office("off_hand", "Reeve", "S", ["issue", "dispatch", "confer"],
                                    conferral="appointed", faction="Crown")
    assert t_hand.granted_acts == (), (
        "a hand-created office re-granted a sitting holder -- fixture is not the snapshot case")

    w.offices["off_dicastery"].conferral = "appointed"      # rostered since `13d-i`
    out = d.resolve([Act(id="g_conf", actor="p_high", verb="confer",
                          payload={"office": "off_dicastery", "to": "p_low"})],
                    contest_max_depth=w.fixtures.get("contest_max_depth"))
    e = next((x for x in out if x.kind == "tenure.opened"), None)
    assert e is not None, f"fixture: confer did not open a Tenure: {[x.kind for x in out]}"

    assert CHANNEL_PREDICATES["post_remit"](w, e, "p_high"), (
        "control: the duke's own snapshot genuinely carries `confer` -- the channel should admit")
    assert not CHANNEL_PREDICATES["post_remit"](w, e, "p_mid"), (
        "`post_remit` admitted a witness whose OFFICE carries `confer` only live, never in their "
        "own Tenure's snapshot -- it is still reading `w.offices[...].remit_acts` instead of "
        "`t.granted_acts`")


def _remit_acts_attribute_reads_outside_allowlist() -> list:
    """Every `Attribute` node named `remit_acts` anywhere under the package's NON-TEST sources,
    outside `_grant_remit`, `Office.__post_init__` and `_eff_establish` -- the allow-list the
    position's own falsifier names. `tests/` is excluded on purpose: a fixture asserting
    `office.remit_acts == [...]` or hand-mutating one to build the SNAPSHOT-vs-mirror scenario is
    the test's job, not a consumer of the fact through the eligibility path this scan protects.
    A dict-key string (`t.payload["remit_acts"]`) is a `Subscript`/`Constant`, never an
    `Attribute`, so `Tenure.granted_acts`'s own storage never matches this scan by construction."""
    violations = []
    for path in sorted(files.PACKAGE_DIR.rglob("*.py")):
        rel = path.relative_to(files.PACKAGE_DIR)
        if rel.parts[0] == "tests":
            continue
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        allowed_spans = []
        for node in ast.walk(tree):
            if isinstance(node, ast.FunctionDef) and node.name in ("_grant_remit", "_eff_establish"):
                allowed_spans.append((node.lineno, node.end_lineno))
            elif isinstance(node, ast.ClassDef) and node.name == "Office":
                allowed_spans += [(sub.lineno, sub.end_lineno) for sub in node.body
                                   if isinstance(sub, ast.FunctionDef) and sub.name == "__post_init__"]
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute) and node.attr == "remit_acts":
                if not any(a <= node.lineno <= b for a, b in allowed_spans):
                    violations.append(f"{rel.as_posix()}:{node.lineno}")
    return violations


def test_13e_no_remit_acts_attribute_read_outside_the_three_allow_listed_sites():
    """**THE POSITION'S FALSIFIER, AST CLAUSE.** Before this position, `loop/resolve.py`'s
    `_eligible` and `epistemic.py`'s `_ch_post_remit` were a fourth and fifth reader of
    `Office.remit_acts`, beyond the three this scan allow-lists; this test observes their absence
    now that both read `t.granted_acts` instead. A fourth reader is PLANNED
    (`budget()` counting `t.granted_acts`, not `Office.remit_acts` -- not this position's job), so
    this pins the CURRENT set to catch a future regression back onto the office-side field rather
    than to block anything today."""
    violations = _remit_acts_attribute_reads_outside_allowlist()
    assert violations == [], (
        f"`Office.remit_acts` read as an attribute outside `_grant_remit`/`Office.__post_init__`/"
        f"`_eff_establish` at {violations} -- position `13e` consolidated every consumer onto "
        f"`Tenure.granted_acts`")


# =================================================================================================
# PLAN POSITION `13d-i` -- OFFICES AS DATA (items 1-4; item 5, `offices.yaml`, is a later unit).
# `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`, position `13d-i`. The two
# bases are rostered values (`rosters.yaml: conferral_bases`, `revocation_bases`) carrying
# `ED-IN-0256` rulings (2) and (3); `_req_confer` / `_req_establish` share a membership test and
# `_req_revoke` dispatches on the seat's declared basis, with no `is_title` branch (`H-109`).
# FALSIFIER `LB-10c`, re-pointed by ruling (3): a titled seat is revocable ONLY by the holder of a
# seat on the rung directly above it, in its faction -- every candidate iterated and counted.
# =================================================================================================

_RUNG_ABOVE = "rung_above_same_faction"       # `revocation_bases`' one member, ruling (3)


def _person(w, pid):
    """A bare person, placed the way `tiny_world` places its own."""
    w.persons[pid] = Person(pid, pid)
    w.rungs[pid] = Rung(pid, "person")
    w.add_tenure(Tenure(f"t_in_{pid}", pid, "Hh", "contain", 0))


def _seat_on(w, pid, oid, post, rung, faction, remit=("issue",)):
    """Seat `pid` on a new office, the office constructed FIRST so the grant is correct at seating."""
    if pid not in w.persons:
        _person(w, pid)
    w.offices[oid] = Office(oid, post, rung, list(remit), faction=faction)
    w.add_tenure(Tenure(f"t_{oid}", pid, oid, "hold", 0))


def _ladder_world():
    """`tiny_world` (R ⊃ D ⊃ S ⊃ Hh; `p_high` holds `off_duke`, a Crown `Duke` at `D`), plus a
    SIBLING duchy `D2` under `R` and a SECOND realm `R2` containing nothing of `R`'s. The duke's
    seat declares the rostered revocation basis."""
    w, d = _establish_world()
    w.rungs["D2"] = Rung("D2", "duchy")
    w.add_tenure(Tenure("t_d2_in_r", "D2", "R", "contain", 0))
    w.rungs["R2"] = Rung("R2", "realm")
    w.offices["off_duke"].revocation = _RUNG_ABOVE
    return w, d


def _may_revoke(w, actor, office) -> bool:
    return _preds._req_revoke(w, Act(id=f"r_{actor}_{office}", actor=actor, verb="revoke",
                                     payload={"office": office}))


def test_13d_i_lb10c_a_titled_seat_is_revocable_only_by_the_seat_above_in_its_faction():
    """**`LB-10c`, AS RULING (3) RE-POINTS IT.** r2 named it `..._revocable_only_by_a_holder_of_its_
    domain` and priced it on a three-conjunct `holdings` rule; both predate `ED-IN-0256`, so this
    asserts the ruling. The target is TITLED (`Duke`, on `titles.domains`), because that is the case
    the deleted `is_title` branch treated specially.

    Ten candidates, each isolating one way to be WRONG about "rung above of same faction" -- the
    faction, the rank, the rung, the land, the seat itself -- and EXACTLY ONE is admitted. The loop
    asserts it ran to completion (`CLAUDE.md` §0.1 pt 2).

    ⚠ **DOES NOT ISOLATE "PARENT" FROM "NEAREST SAME-FACTION ANCESTOR" (corrected 2026-09-26,
    found by an antagonist pass).** In THIS world the target's only ancestor at any distance is
    also its immediate parent (`R` sits directly above `D`), so a mutant that walked past an empty
    or foreign parent to find the nearest same-faction seat would still pass every candidate here.
    `test_13d_i_an_empty_parent_refuses_even_a_same_faction_grandparent` is the test that isolates
    it, with a chain long enough for the two readings to disagree."""
    w, _ = _ladder_world()
    assert title_domain(w.offices["off_duke"].post) == "duchy", "fixture: the target is not a title"
    _seat_on(w, "c_king", "off_king", "King", "R", "Crown")                  # above, same faction
    _seat_on(w, "c_rival_king", "off_rival_king", "King", "R", "Hafenmark")  # above, OTHER faction
    _seat_on(w, "c_far_king", "off_far_king", "King", "R2", "Crown")         # outranks, not above
    _seat_on(w, "c_peer_duke", "off_peer_duke", "Duke", "D2", "Crown")       # sibling rung
    _seat_on(w, "c_chancellor", "off_chancellor", "Chancellor", "D", "Crown")  # the SAME rung
    _seat_on(w, "c_mayor", "off_mayor", "Mayor", "S", "Crown")               # below
    _seat_on(w, "c_councillor", "off_privy", "Privy Councillor", None, "Crown")  # no rung at all
    _person(w, "c_landholder")
    w.add_tenure(Tenure("t_land_r", "c_landholder", "R", "hold", 0))         # HOLDS the rung above
    candidates = {
        "c_king": True, "c_rival_king": False, "c_far_king": False, "c_peer_duke": False,
        "c_chancellor": False, "c_mayor": False, "c_councillor": False, "c_landholder": False,
        "p_high": False,                                         # the target's own holder
        "p_other": False,                                        # holds nothing
    }
    assert in_holdings(w, "c_landholder", "R"), "fixture: the landholder does not hold the rung"
    checked, admitted = 0, []
    for pid, expected in candidates.items():
        got = _may_revoke(w, pid, "off_duke")
        assert got is expected, f"{pid}: `_req_revoke` answered {got}, ruling (3) says {expected}"
        checked += 1
        admitted += [pid] if got else []
    assert checked == len(candidates) and checked >= 10, f"the sweep checked {checked}"
    assert admitted == ["c_king"], admitted


def test_13d_i_the_seat_above_of_another_faction_refuses_though_it_meets_the_old_title_rule():
    """**THE DIFFERENT-FACTION CASE, BUILT TO SATISFY EVERYTHING THE DELETED RULE ASKED.** The
    rival King sits on the rung above the duchy (so the old containment purview held), OUTRANKS a
    duke (realm over duchy in `rung_kinds`), and HOLDS THE DUCHY (`in_holdings`) -- the 2026-09-02
    title rule's three conjuncts, all true. Ruling (3) refuses him on the one thing that differs:
    his faction. The control is his Crown twin in the same world, identical but for the faction."""
    w, _ = _ladder_world()
    for pid, oid, fac in (("c_rival_king", "off_rival_king", "Hafenmark"),
                          ("c_king", "off_king", "Crown")):
        _seat_on(w, pid, oid, "King", "R", fac)
        w.add_tenure(Tenure(f"t_land_d_{pid}", pid, "D", "hold", 0))
        assert in_holdings(w, pid, "D"), f"fixture: {pid} does not hold the duchy"
    assert RUNG_KINDS.index(w.rungs["R"].kind) > RUNG_KINDS.index(w.rungs["D"].kind)
    assert world_q.parent_of(w, "D") == "R", "fixture: the King's rung is not above the duchy"
    assert w.offices["off_rival_king"].faction != w.offices["off_duke"].faction
    assert not _may_revoke(w, "c_rival_king", "off_duke"), (
        "a higher-ranked seat of ANOTHER faction, on the rung above and holding the duchy, stripped "
        "the duke -- the rewrite is still the purview/holdings/rank conjunction")
    assert _may_revoke(w, "c_king", "off_duke"), "control: the same-faction twin is refused"


def test_13d_i_an_empty_parent_refuses_even_a_same_faction_grandparent():
    """**PINS "PARENT" AGAINST "NEAREST SAME-FACTION SEAT ABOVE."** Every other `13d-i` fixture
    seats someone at the target's immediate parent rung, so the two readings never disagree there
    -- an antagonist pass found this gap directly: with only those fixtures, a mutant that walks
    PAST an empty or foreign-faction parent to the nearest same-faction seat passes every existing
    test. This builds the one world where the readings diverge: `off_reeve_hh` sits at `Hh`, whose
    parent `S` holds NO seat at all, while its grandparent `D` holds `off_duke`, Crown -- the same
    faction. Under `seated_on_the_rung_above`'s own reading (the ADJACENT rung only), the duke's
    holder must REFUSE; under a nearest-same-faction-ancestor reading he would be admitted. Ruling
    (3)'s words are "rung above", not a walk -- that verb belongs to ruling (4)'s purview clause
    ("owner of highest rung in CHAIN of ownership"), a different mechanism this position does not
    build."""
    w, _ = _ladder_world()
    assert world_q.parent_of(w, "S") == "D" and world_q.parent_of(w, "Hh") == "S", (
        "fixture: the chain is not Hh -> S -> D as assumed")
    assert not any(t.kind == "hold" and t.object in w.rungs and w.rungs[t.object].kind == "S"
                   for t in w.tenures), "fixture: someone already sits at S"
    _seat_on(w, "p_reeve", "off_reeve_hh", "Reeve", "Hh", "Crown", remit=("issue",))
    w.offices["off_reeve_hh"].revocation = _RUNG_ABOVE
    assert w.offices["off_duke"].faction == w.offices["off_reeve_hh"].faction == "Crown", (
        "fixture: the duke and the reeve are not the same faction")
    assert not _may_revoke(w, "p_high", "off_reeve_hh"), (
        "the Crown duke, two rungs above an empty parent, revoked a Crown reeve -- "
        "seated_on_the_rung_above walked PAST the empty parent instead of refusing at it")


def test_13d_i_one_rule_at_every_depth_and_no_title_branch():
    """GENERAL OVER ANY SEAT AND ANY DEPTH (`CLAUDE.md` §0 -- never special-case). Three depths --
    a duchy under a realm, a settlement under a duchy, a hearth under a settlement -- and at the
    settlement a TITLED seat (`Mayor`) and an UNTITLED one (`Reeve`) side by side. Each is
    revocable by the seat on its parent rung and by nothing further up; the titled and untitled
    seats answer identically, which is `H-109` closed as a behaviour, not as a grep."""
    w, _ = _ladder_world()
    _seat_on(w, "c_king", "off_king", "King", "R", "Crown")
    _seat_on(w, "c_mayor", "off_mayor_s", "Mayor", "S", "Crown")
    _seat_on(w, "p_mid", "off_reeve_s", "Reeve", "S", "Crown")
    _seat_on(w, "p_low", "off_head_hh", "Family Head", "Hh", "Crown")
    for oid in ("off_mayor_s", "off_reeve_s", "off_head_hh"):
        w.offices[oid].revocation = _RUNG_ABOVE
    assert title_domain("Mayor") and title_domain("Reeve") is None, "fixture: titled/untitled pair"
    cases = [
        ("off_duke", "c_king", True), ("off_duke", "c_mayor", False),
        ("off_mayor_s", "p_high", True), ("off_mayor_s", "c_king", False),   # grandparent
        ("off_reeve_s", "p_high", True), ("off_reeve_s", "c_king", False),
        ("off_head_hh", "c_mayor", True), ("off_head_hh", "p_high", False),  # grandparent
    ]
    checked = 0
    for oid, pid, expected in cases:
        assert _may_revoke(w, pid, oid) is expected, (oid, pid, expected)
        checked += 1
    assert checked == len(cases) >= 8
    assert [_may_revoke(w, p, "off_mayor_s") for p in ("p_high", "c_king")] == \
        [_may_revoke(w, p, "off_reeve_s") for p in ("p_high", "c_king")], (
            "a titled and an untitled seat on the same rung answer differently -- an is_title branch")


def test_13d_i_the_revocation_basis_is_a_rostered_value_and_gates_the_rule():
    """The right revoker is refused unless the seat DECLARES a rostered basis: `None` (strippable by
    nobody, r2's `none`), r2's superseded `purview` (hand-mutated past the constructor), and the
    rostered value, in that order, on one seat and one actor. And the constructor refuses to build
    a seat declaring the off-roster value -- the `remit_acts` refusal's shape, one field along."""
    w, _ = _ladder_world()
    _seat_on(w, "c_king", "off_king", "King", "R", "Crown")
    seat = w.offices["off_duke"]
    seen = []
    for basis, expected in ((None, False), ("purview", False), (_RUNG_ABOVE, True)):
        seat.revocation = basis
        seen.append(_may_revoke(w, "c_king", "off_duke"))
        assert seen[-1] is expected, (basis, seen[-1])
    assert seen == [False, False, True], seen
    assert set(REVOCATION_BASES) == {_RUNG_ABOVE}, sorted(REVOCATION_BASES)
    with pytest.raises(Unspecified):
        Office("off_x", "Reeve", "S", [], faction="Crown", revocation="purview")
    assert Office("off_y", "Reeve", "S", [], faction="Crown", revocation=_RUNG_ABOVE).revocation


def test_13d_i_the_conferral_basis_is_roster_membership_not_a_nonempty_string():
    """**THE BEHAVIOUR CHANGE, STATED.** Before `13d-i` `has_conferral_basis` admitted any non-empty
    string -- including the free fixture string `test_season_shape.py` used, which is asserted
    REFUSED here. Now: every member of `conferral_bases` passes (all three iterated, not one
    sampled), an off-roster string and `None` refuse, through `has_conferral_basis` AND through
    `_req_confer` on an unheld office. The constructor refuses to BUILD the off-roster value, so
    that arm is reached by hand-mutation -- the predicate is tested on what it reads."""
    w, _ = _establish_world()
    off = w.offices["off_dicastery"]
    conf = Act(id="c_b", actor="p_high", verb="confer",
               payload={"office": "off_dicastery", "to": "p_mid"})
    checked = 0
    for basis in sorted(CONFERRAL_BASES):
        off.conferral = basis
        assert _preds.has_conferral_basis(off) and _preds._req_confer(w, conf), basis
        checked += 1
    assert checked == len(CONFERRAL_BASES) >= 3, checked
    for basis in (None, "something-not-on-the-roster", "the duke's remit (harness fixture)", ""):
        off.conferral = basis
        assert not _preds.has_conferral_basis(off), f"{basis!r} passed the basis test"
        assert not _preds._req_confer(w, conf), f"`_req_confer` admitted {basis!r}"
    with pytest.raises(Unspecified):
        Office("off_x", "Reeve", "S", [], faction="Crown", conferral="something-not-on-the-roster")


def test_13d_i_an_off_roster_conferral_on_establish_refuses_and_raises_nothing():
    """`13f`'s contract under the new test: `_req_establish` translates the constructor's new
    refusal to False, so an `establish` naming an off-roster basis emits `establish.refused`,
    constructs nothing, and lets no exception escape the fold. Every rostered basis founds."""
    w, d = _establish_world()
    act = Act(id="e_offroster", actor="p_high", verb="establish",
              payload=_founding(conferral="something-not-on-the-roster"))
    with pytest.raises(Unspecified):
        office_described_by(act)
    out = d.resolve([act], contest_max_depth=w.fixtures.get("contest_max_depth"))
    assert [e.kind for e in out] == ["establish.refused"], [e.kind for e in out]
    assert "off_reeve" not in w.offices
    founded = 0
    for i, basis in enumerate(sorted(CONFERRAL_BASES)):
        out = _establish(w, d, f"e_ok_{i}", _founding(office=f"off_reeve_{i}", conferral=basis))
        assert [e.kind for e in out] == ["office.established"], (basis, [e.kind for e in out])
        founded += 1
    assert founded == len(CONFERRAL_BASES) >= 3


def test_13d_i_the_title_in_a_body_refusal_is_rehomed_not_dropped():
    """Item (4), r2 `03` SC-5: *"deleting the title helpers loses no constructor invariant"*. The
    refusal is now a function of its own (`state/carriers.py::refuse_a_title_in_a_body`), which
    the constructor still calls and `offices.yaml`'s loader will. Asserted on BOTH routes, for EVERY
    title on the roster (counted), with the message naming the title AND the body; and the two
    non-cases -- a title with no body, a non-title in a body -- pass."""
    checked = 0
    for ttl in sorted(TITLE_DOMAINS):
        with pytest.raises(Forbidden) as direct:
            refuse_a_title_in_a_body("off_t", ttl, "Imperial Court")
        with pytest.raises(Forbidden) as built:
            Office("off_t", ttl, None, [], body="Imperial Court")
        for exc in (direct.value, built.value):
            assert repr(ttl) in str(exc) and "'Imperial Court'" in str(exc), str(exc)
        checked += 1
    assert checked == len(TITLE_DOMAINS) >= 11, checked
    refuse_a_title_in_a_body("off_t", "King", None)                  # a title held at a rung
    refuse_a_title_in_a_body("off_t", "Chancellor", "Imperial Court")  # an office in an organ
    assert Office("off_t", "Chancellor", None, [], body="Imperial Court").faction == "Crown"


def test_13d_i_revoke_executes_in_the_fold_for_the_seat_above_and_refuses_the_other_faction():
    """§0.2 -- DONE MEANS IT RUNS. Planted `revoke` acts through the resolver, both revokers seated
    with `revoke` in their grant so eligibility passes and the PREDICATE decides: the other
    faction's King first (`revoke.refused`; the duke's `hold` survives), then the Crown King
    (`tenure.closed`; it does not). Asserted on the Events."""
    w, d = _ladder_world()
    _seat_on(w, "c_rival_king", "off_rival_king", "King", "R", "Hafenmark", remit=("revoke",))
    _seat_on(w, "c_king", "off_king", "King", "R", "Crown", remit=("revoke",))
    held = lambda: [t for t in w.tenures if t.kind == "hold" and t.object == "off_duke" and t.live]
    assert held(), "fixture: nobody holds the duke's seat"

    def run(aid, actor):
        return [e.kind for e in d.resolve(
            [Act(id=aid, actor=actor, verb="revoke", payload={"office": "off_duke"})],
            contest_max_depth=w.fixtures.get("contest_max_depth"))]

    assert run("rv_rival", "c_rival_king") == ["revoke.refused"]
    assert held(), "the other faction's King closed the duke's hold"
    kinds = run("rv_king", "c_king")
    assert "tenure.closed" in kinds and "revoke.refused" not in kinds, kinds
    assert not held(), "the fold accepted the revocation and the duke's hold survived"


# =================================================================================================
# PLAN POSITION `24d-i` -- THE DWELLING SUBSTRATE (`ED-SE-0055`).
# `workplans/2026-09-18-governance-settlement-behaviour-plan_part2.md`, position `24d-i`. `dwelling`
# joins `site_kinds` with the two rows the loader forces, both at the CONTROL arm
# (`wear_per_season.dwelling: 0`, `band_floors.dwelling: {}`), and `build_realm` mints one dwelling
# Site per `hearth` rung. FALSIFIERS: exactly one dwelling on every hearth and none elsewhere, with
# a hearth floor so an empty world cannot pass; the loader's refusal, planted; and the control arm
# over one populated season, with no dwelling band crossing while the wear loop visited every one.
#
# ⚠ WHICH OTHER HEARTH BUILDERS MINT, AND WHY. The ruling names `build_realm` only; the rest is
# this position's architecture call (`CLAUDE.md` §0, step 5).
#   * `governance_spine.build` MINTS. The spine is the template the realm is fine-tuned FROM, and
#     `19c`'s `migrate` runs its observable on the spine's two disjoint chains. With a dwelling per
#     hearth, `capacity` counts 2 at the realm and 1 down each chain. Without, every rung reads the
#     floor. Cost: two Sites on a world no test runs a season on today.
#   * `corpus_run.build_at` DOES NOT. Every corpus world is ONE chain wide. Measured over every
#     buildable case, a corpus world has 0 or 1 hearth, so a dwelling there would be counted by
#     every rung of the chain alike, and `capacity` would still be one number per world. Minting
#     would buy no variation for `R-05` to score. It would still add a wear Event, co-located with
#     all three persons, to every hearth-scaled world.
#   * `probes.tiny_world` DOES NOT. It isolates mechanisms. A dwelling at `Hh` would sit with three
#     of its five persons and hand each a witnessed wear claim every season, in every probe and
#     every test built on it. It would also trip probe `F10`'s assert that `Hh` carries no Site;
#     that assert guards against PRODUCTION and would fire on a dwelling that produces nothing. A
#     probe that needs a dwelling plants one, as `site_odd` is planted.
#   * `headless.build_world` DOES NOT. The spec's list omits this fourth builder (`hearth_ostvik`).
#     It is Carin's single worked case and `m1_acceptance`'s probe world. A dwelling there would
#     add a wear claim to Carin's and the bailiff's ledgers, and nothing in either world reads
#     housing.
# =================================================================================================

def _dwellings(w):
    return [s for s in w.sites.values() if s.kind == "dwelling"]


def _hearths(w):
    return sorted(rid for rid, r in w.rungs.items() if r.kind == "hearth")


def _spine():
    from ..harness import governance_spine
    return governance_spine.build(0)


@pytest.mark.parametrize("build", [lambda: build_realm(0), _spine], ids=["build_realm", "spine"])
def test_24d_i_every_hearth_carries_exactly_one_dwelling_and_no_other_rung_carries_any(build):
    """FALSIFIER (a), on both builders that mint. Exactly one per hearth and none elsewhere is ONE
    comparison: the dwellings counted per rung must equal each hearth counted once. A dwelling on
    a settlement, a hearth with two, or a hearth with none all fail it."""
    w = build()
    hearths = _hearths(w)
    assert len(hearths) >= 1, "the world builds no hearth; everything below would pass vacuously"
    dw = _dwellings(w)
    per_rung = Counter(s.rung for s in dw)
    assert per_rung == Counter(hearths), (
        f"dwellings per rung != one per hearth. Off-hearth (first 10): "
        f"{sorted(set(per_rung) - set(hearths))[:10]}; hearths without exactly one (first 10): "
        f"{sorted(h for h in hearths if per_rung[h] != 1)[:10]}")
    scale = w.fixtures.get("condition_scale")
    checked = 0
    for s in dw:
        assert s.condition == scale, (
            f"{s.id} starts at {s.condition}, not at `condition_scale`, which is how the producing "
            "Sites are built")
        checked += 1
    assert checked == len(hearths) >= 1, checked


def test_24d_i_the_realm_mint_adds_sites_and_displaces_no_producing_site():
    """The OBSERVABLE's census, derived rather than pinned. The producing Sites are still one per
    producing kind per settlement, and the total is those plus one per hearth. A dwelling id that
    collided with a producing Site's would overwrite it, and the first count would drop."""
    from ..data.fixtures import SITE_YIELD
    w = build_realm(0)
    settlements = [r for r in w.rungs.values() if r.kind == "settlement"]
    producing = [k for k in sorted(SITE_YIELD) if SITE_YIELD[k]]
    assert settlements and producing, "fixture: no settlement or no producing kind"
    others = Counter(s.kind for s in w.sites.values() if s.kind != "dwelling")
    assert others == Counter({k: len(settlements) for k in producing}), others
    assert len(w.sites) == len(settlements) * len(producing) + len(_hearths(w)), len(w.sites)
    assert not [s.id for s in w.sites.values() if s.id in w.rungs], "a Site id shadows a rung id"


def test_24d_i_the_loader_refuses_dwelling_without_its_wear_or_floor_row(monkeypatch):
    """FALSIFIER (b), the loader's own refusal, planted and reverted by `monkeypatch`. The
    `dwelling` key is deleted from the loaded table the loader reads, and `_load_matter_tables`
    must raise `Ungraded` NAMING `dwelling`. That is the refusal for a kind with no row, and not
    some other failure. The unplanted arm must load, with the control-arm values."""
    from ..data import rosters as _R
    from ..data.fixtures import DEFAULT_FIXTURES, _load_matter_tables
    from ..gaps import Ungraded

    rates, floors, _w, _y = _load_matter_tables()
    assert rates["dwelling"] == 0 and floors["dwelling"] == {}, (rates, floors)
    assert DEFAULT_FIXTURES.wear("dwelling") == 0

    checked = 0
    for table, cell in (("wear_per_season", _R._ROSTERS["wear_per_season"]["rates"]),
                        ("band_floors", _R._TABLES["band_floors"]["cells"])):
        with monkeypatch.context() as m:
            m.delitem(cell, "dwelling")
            with pytest.raises(Ungraded) as got:
                _load_matter_tables()
            assert table in str(got.value) and "dwelling" in str(got.value), str(got.value)
        assert "dwelling" in cell, f"the plant on {table} was not reverted"
        checked += 1
    assert checked == 2, checked


def test_24d_i_the_control_arm_crosses_no_band_and_moves_no_question_in_one_season(monkeypatch):
    """FALSIFIER (c), and the `DONE·INERT` measurement it rests on, as a CONTROLLED comparison.

    TREATMENT is `build_realm(0)`. CONTROL is the same world with its dwellings deleted before the
    season. The control reproduces the pre-`24d-i` tree exactly: build hash and one-season hash
    were both byte-identical to the checkout before this change when measured.

    Treatment: no dwelling crossing reaches Q3, so no `band_crossed` Question comes from one, and
    every dwelling emits exactly one `condition.worn` and keeps its condition. The Events are what
    prove the wear loop visited them, so the zero is not an empty population.
    Treatment against control: the same Questions by id, the same resolved acts, every other
    non-deposit Event by id, and every control claim survives.

    ⚠ IT IS NOT SILENT, AND THIS POSITION IS NOT `DONE·INERT` BY THE PLAN'S TEST. CLAIMS MOVE. The
    wear Events are witnessed through `co_located`, so each resident of a hearth gets one
    firsthand `condition.worn` claim about that hearth's dwelling. This test pins the SHAPE of that
    movement, not its count. ⚠ It is a ONE-season identity. Measured beyond it: from season 2, the
    added claims displace others at `ledger_cap`, and by season 4 one resolved act differs."""
    from ..harness import populated
    from ..loop import deliberate

    def season(strip):
        w = build_realm(0)
        if strip:
            for s in _dwellings(w):
                del w.sites[s.id]
        dw = {s.id: s.rung for s in _dwellings(w)}
        qs = []
        inner = deliberate.questions_for

        def spy(w_, p, since=None):
            out = inner(w_, p, since)
            qs.extend(out)
            return out
        with monkeypatch.context() as m:
            m.setattr(deliberate, "questions_for", spy)
            out = populated.run(seasons=1, w=w)
        return w, dw, qs, out

    w, dw, qs, out = season(strip=False)
    scale = w.fixtures.get("condition_scale")
    assert len(dw) >= 1, "no dwelling was built; the zeros below would describe nothing"
    assert qs, "the questions_for spy saw no deliberation; the zero below would be unobserved"
    worn = Counter(e.subject for e in w.log if e.kind == "condition.worn" and e.subject in dw)
    assert worn == Counter(list(dw)), (
        f"the wear loop did not visit every dwelling exactly once: "
        f"{len(worn)} of {len(dw)} worn, {sum(worn.values())} Events")
    # ⚠ A `band_crossed` QUESTION NEVER NAMES A SITE, so "Questions naming a dwelling" is
    # attributed through Q3's ONLY input. `questions_for` builds one from each `w.crossings` tuple
    # `(site, use, ...)` as `Question(..., (use,), use)`: its referent is the site-USE, the floor's
    # key. A filter on dwelling ids over the Questions cannot fail. Measured with a planted
    # `wear 10` / `{planted_use: 995}`: 211 dwelling crossings and 460 `band_crossed` Questions
    # over two seasons, none carrying a dwelling id. No dwelling tuple means no dwelling Question.
    crossed = [c for c in w.crossings if c[0] in dw]
    assert crossed == [], f"{len(crossed)} dwelling crossings reach Q3 at the control arm"
    assert not [e for e in w.log if e.kind == "condition.band_crossed" and e.subject in dw]
    assert all(w.sites[sid].condition == scale for sid in dw), "a dwelling's condition moved at wear 0"
    assert not [q for q in qs if {q.about, *q.referents} & set(dw)], (
        "some question source now names a dwelling. `work` binds a referent as its `site`, and "
        "`world_q`'s `floor` read raises a bare `ValueError` on `band_floors.dwelling: {}`")

    cw, cdw, cqs, cout = season(strip=True)
    assert cdw == {}, "the control still has dwellings"
    # By Question ID, not only by source: the same questions, to the same people, about the same
    # things.
    assert sorted(q.id for q in qs) == sorted(q.id for q in cqs), (
        Counter(q.source for q in qs), Counter(q.source for q in cqs))
    assert (out["acts"], out["act_subjects"]) == (cout["acts"], cout["act_subjects"])
    # Every Event but the deposits is the control's, plus exactly the dwellings' own wear. The
    # deposits are excluded because their ids are not stable across arms; measured, every
    # `claim.deposited` id differs even where the claim id does not.
    other = lambda log: {e.id for e in log if e.kind != "claim.deposited"}
    worn_ids = {e.id for e in w.log if e.kind == "condition.worn" and e.subject in dw}
    assert other(w.log) - worn_ids == other(cw.log), (
        f"{len(other(w.log) - worn_ids ^ other(cw.log))} non-deposit Events differ between arms")

    claims = {c.id: c for p in w.persons.values() for c in p.ledger}
    control = {c.id for p in cw.persons.values() for c in p.ledger}
    assert control and control <= set(claims), (
        f"{len(control - set(claims))} control claims are gone from the treatment arm; the "
        "dwellings displaced something in season one")
    added = [claims[i] for i in set(claims) - control]
    at = {rung: sid for sid, rung in dw.items()}
    home = world_q.home_of(w)
    assert added, "no claim moved; if that is now true, `24d-i` IS `DONE·INERT` -- relabel it"
    for c in added:
        assert c.predicate == "condition.worn" and c.subject == at.get(home.get(c.holder)), (
            f"an added claim is not a resident's claim on their own hearth's dwelling: {c}")
