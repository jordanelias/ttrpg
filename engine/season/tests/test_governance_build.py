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

from ..gaps import Forbidden
from ..data.cast import faction_leader
from ..harness.populated import build_realm
from ..loop.predicates import in_holdings
from ..harness import probes as P
from ..state.carriers import Proposition, Tenure


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
