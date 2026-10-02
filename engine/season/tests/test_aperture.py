"""Plan position `★` -- THE APERTURE RE-MEASUREMENT. `harness/aperture.py` is the populated-realm
formability-and-execution instrument the plan names as the gate's first step (*"the instrument does
not exist ... it is this gate's first step, not a separate position"*).

⚠ THESE TESTS PIN THE INSTRUMENT, NEVER ITS NUMBERS. What a populated season forms and executes is
the measurement, and it moves every time the game does; pinning it would be a golden nobody has
argued is correct (`CLAUDE.md` §0.1 pt 5, and `harness/populated.py`'s own *"THIS TABLE IS THE
BASELINE, NOT A REGRESSION CHECK"*). What is pinned is what makes the numbers mean anything:

  * THE CONTROL -- the measured arm ends in the same `content_hash()` and act count as
    `populated.run`, the owner, on a second world from the same seed. So the chooser/barrier
    watching observed the season without moving it, and the figures ARE `harness.populated 1`'s.
    `World.content_hash` folds every state collection and the log (`H-118`), which is what lets
    this equality observe a perturbation rather than merely the act count;
  * THE COUNTERFACTUAL IS HONEST -- re-aggregating a person's delivered questions under the shipped
    rule reproduces the question the real chooser received, at every deliberation, so the other
    rules' rows differ from it by the rule alone;
  * THE FUNNEL IS CLOSED -- no act reaches the fold for a verb the chooser never offered that
    person, so `attempted` is a subset of what this instrument watched being offered;
  * TWO READINGS OF "SEATED" AGREE -- `aperture.seats` against the builder's own `_office_census`.
"""

from __future__ import annotations

import pytest

from ..data.verbs import VERB_TABLE
from ..harness import aperture as A
from ..harness import governance_spine, populated


@pytest.fixture(scope="module")
def realm():
    return A.measure_world(populated.build_realm, 0, 1)


def test_aperture_the_measured_season_is_the_populated_season(realm):
    c = realm["control"]
    assert c["acts"] == realm["acts"], (
        f"populated.run resolved {c['acts']} acts and the instrumented season {realm['acts']}: the "
        "two arms are different experiments, so nothing the instrument reports is the populated "
        "season's. Check that `instrumented_season` still builds its driver and chooser exactly as "
        "`populated.run` does")
    assert c["hash"] == realm["hash"], (
        "the instrumented season ended in a different world than `populated.run` on the same seed "
        "-- the watching PERTURBED the run. `opening_set`/`assemble`/`aggregate_questions` must stay "
        "pure for this instrument to exist")


def test_aperture_the_counterfactual_rules_reproduce_the_real_call(realm):
    assert realm["per_rule"], "no deliberation was recorded -- the chooser wrapper never ran"
    n = {len(rows) for rows in realm["per_rule"].values()}
    assert len(n) == 1, f"the aggregation rules saw different deliberation counts: {n}"
    assert realm["rule_mismatch"] == 0, (
        f"{realm['rule_mismatch']} deliberation(s) where re-aggregating the delivered questions under "
        f"the shipped rule ({realm['shipped_rule']!r}) did not give the question the chooser "
        "received. The other rules' rows then differ by more than the rule")


def test_aperture_no_act_enters_the_fold_unoffered(realm):
    stray = sorted((pid, v) for pid, c in realm["attempted"].items() for v in c
                   if v not in realm["formed"].get(pid, ()) or v not in realm["foldable"])
    assert realm["attempted"], "no act was attributed -- `corpus_run.attribute` saw nothing"
    assert not stray, (
        f"acts reached the fold for verbs the chooser never offered their actor: {stray[:5]}. An "
        "act is entering by a route this instrument does not watch, so its funnel undercounts "
        "`formed`/`offered`; watch that route before reading the per-holder table")


def test_aperture_seats_agrees_with_the_builders_own_census():
    """SEATS, not persons: `build_realm` seats NPC-020 twice since `13d-iii` (the King and the Duke
    of Valorsmark), so the per-holder table has fewer keys than the census has seats -- the SUM of
    its lists is what must equal `seated`."""
    w = populated.build_realm(0)
    table = A.seats(w)
    seats = sum(len(offs) for offs in table.values())
    assert seats == w._office_census["seated"], (
        f"`aperture.seats` finds {seats} seats over {len(table)} persons and `build_realm` seated "
        f"{w._office_census['seated']}")
    assert len(table) < seats, "no person holds two seats: the sum and the key count are not told apart"


def test_aperture_the_spine_gives_the_per_holder_table_its_population():
    """`workplans/2026-09-18-governance-settlement-behaviour-plan.md` §3.8b: *"13 holders at 7
    distinct depths in one world, so 're-take it per holder' has a population rather than an
    anecdote"*. Asserted through the instrument's own readers, so a spine that stops seating or a
    `seat_depth` that stops walking shows here rather than as a short table."""
    m = A.measure_world(governance_spine.build, 0, 1)
    assert m["control"]["hash"] == m["hash"], "the instrument perturbed the spine season"
    assert len(m["seats"]) == len(governance_spine.spec()) == len(m["persons"]), (
        f"{len(m['seats'])} seated of {len(m['persons'])} persons over "
        f"{len(governance_spine.spec())} declared rungs -- every spine rung seats one holder")
    depths = [m["depth"][o] for offs in m["seats"].values() for o in offs]
    assert None not in depths, "a spine seat has no rung, so the table cannot say how deep it sits"
    # Every depth from the root down is populated: the table has a holder at each level, which is
    # the property the per-holder re-take needs. The COUNT of levels is the spine test's to pin.
    assert sorted(set(depths)) == list(range(max(depths) + 1)), sorted(set(depths))
    assert any(A.seat_gated(r) for r in VERB_TABLE.values()), (
        "no verb-table row is seat-gated; `seat_gated` parses nothing, so the per-holder funnel "
        "has no columns")
