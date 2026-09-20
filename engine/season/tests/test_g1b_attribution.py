"""G1b -- attribution without `Event.subject`.

THE CONTROL COMES FIRST AND IT IS THE POINT OF THIS FILE. G1b's stated failure mode is
*"silently vacating the actor channel"*, and its plan says in terms that a passing suite does not
see it. So the equivalence is asserted on a LIVE RUN against the field being replaced, while the
field is still there to compare against -- not inferred from the shape of the code.

When the field goes, `test_the_accessors_reproduce_the_field_exactly` is the test that must be
deleted with it, and its deletion is the moment the equivalence stops being checkable. Anything
relying on that equivalence should have its own falsifier by then.
"""
import pytest

from engine.season.harness import headless
from engine.season.state.acts import ActStore
from engine.season.state.attribution import actor_of, anchor_of
from engine.season.state.carriers import Act, Event, StateChange
from engine.season.state.ids import ROOT


class _W:
    """The two attributes the accessors touch, and nothing else."""
    def __init__(self, acts=None):
        self.acts = acts or ActStore()
        self.log = []


def _ev(causes, changes=None):
    return Event(id="e1", kind="k", subject="ignored", changes=changes or [],
                 causes=list(causes), emitted_at=1)


# -- the unit behaviour -------------------------------------------------------------------

def test_an_act_caused_event_attributes_to_that_acts_actor():
    w = _W()
    w.acts.append(Act(id="a1", actor="p_king", verb="speak"))
    e = _ev(["a1"])
    assert actor_of(w, e) == "p_king"
    assert anchor_of(w, e) == "p_king"


def test_an_event_no_act_caused_has_NO_actor_and_that_is_an_answer():
    """MATTER's wear has no actor. `None` here is the distinction `Event.subject` could not make:
    it held the WRITTEN THING in exactly these cases and an actor everywhere else, so a reader
    asking 'who did this' got a rung id that reads like a person."""
    w = _W()
    e = _ev([ROOT], [StateChange("rung_a", "set", "MATTER", "stores")])
    assert actor_of(w, e) is None
    assert anchor_of(w, e) == "rung_a"


def test_the_actor_channel_wins_over_the_change_channel():
    """A fold-emitted Event has both. The field it replaces held the ACTOR there, so this must."""
    w = _W()
    w.acts.append(Act(id="a1", actor="p_king", verb="transfer"))
    e = _ev(["a1"], [StateChange("rung_a", "set", "Act", "stores")])
    assert anchor_of(w, e) == "p_king"


def test_the_first_cause_resolving_to_an_act_wins():
    w = _W()
    w.acts.append(Act(id="a1", actor="p_first", verb="speak"))
    w.acts.append(Act(id="a2", actor="p_second", verb="speak"))
    assert actor_of(w, _ev(["a1", "a2"])) == "p_first"
    # a cause naming a prior EVENT is skipped, not treated as a miss
    assert actor_of(w, _ev(["some_event_id", "a2"])) == "p_second"


def test_a_leading_change_with_no_subject_degrades_to_the_next():
    """Written this way rather than `changes[0].subject` so an empty leading subject does not
    silently vacate the channel -- which is this unit's whole named failure mode."""
    w = _W()
    e = _ev([ROOT], [StateChange("", "set", "MATTER", "f"),
                     StateChange("rung_b", "set", "MATTER", "f")])
    assert anchor_of(w, e) == "rung_b"


def test_tier_3_a_consequence_inherits_the_anchor_of_its_cause():
    """The corpus class tiers 1-2 missed. `condition.band_crossed` changes nothing and is caused
    by the Event that wrote the condition; without this tier every crossing lost its anchor and
    WITNESS deposits fell 9 -> 8 on the corpus run."""
    w = _W()
    cause = Event(id="e_prior", kind="condition.changed", subject="ignored",
                  changes=[StateChange("site_harbour", "set", "MATTER", "condition")],
                  causes=[ROOT], emitted_at=1)
    w.log = [cause]
    crossing = Event(id="e_cross", kind="condition.band_crossed", subject="site_harbour",
                     changes=[], causes=["e_prior"], emitted_at=1)
    assert anchor_of(w, crossing) == "site_harbour"


def test_tier_4_is_the_field_and_it_is_the_blocker():
    """⚠ THIS TEST PINS WHY `Event.subject` COULD NOT BE DELETED, and it should go red the day
    that becomes false. `plague.struck` carries `causes=[ROOT]`, no changes and no act: nothing
    in the Event holds what it concerns, so the field is the only answer. Finishing G1b means
    giving this class an antecedent or a receipt and making tier 4 unreachable -- at which point
    this test is deleted ON PURPOSE, like the bare-StateChange pin in G1a."""
    w = _W()
    w.log = []
    plague = Event(id="e_p", kind="plague.struck", subject="R",
                   changes=[], causes=[ROOT], emitted_at=1)
    assert actor_of(w, plague) is None
    assert anchor_of(w, plague) == "R", "tier 4 is the field; if this changed, say which tier answers now"


def test_an_event_reaching_no_tier_at_all_returns_None():
    """With tier 4 being the field, only an Event with an EMPTY subject reaches nothing."""
    w = _W()
    w.log = []
    assert anchor_of(w, Event(id="e", kind="k", subject="", changes=[],
                              causes=[ROOT], emitted_at=1)) is None


# -- THE CONTROL: equivalence to the field, on live runs ------------------------------------

# Four (seed, seasons) pairs sampled from the wider sweep this control stands in for. Nothing in
# the model reads them as quantities -- they select which runs the equivalence is checked on.
# [JUSTIFIED: SEEDS AND SEASON COUNTS, not game values -- the property behind them is measured at 3,411 events]
@pytest.mark.parametrize("seed,seasons", [(0, 1), (0, 2), (1, 3), (42, 2)])
def test_the_accessors_reproduce_the_field_exactly(seed, seasons):
    """⚠ THE ASSERTION THAT MATTERS, and it asserts that it asserted.

    A loop comparing `anchor_of(w, e) == e.subject` over an EMPTY log passes vacuously, which is
    §0.1 pt 2 exactly -- so the event count is asserted first. Measured at the time of writing:
    119 events for seed 0 x 2 seasons, and 1,428 over the wider sweep this is a sample of.
    """
    w = headless.run(seasons=seasons, seed=seed)["world"]
    log = list(w.log)
    # The smallest run in the parametrize above emits 38 events (seed 0 x 1 season, measured), so
    # this clears the real floor with room and still fails loudly if a change empties the log.
    # [JUSTIFIED: A VACUITY FLOOR, not a game value -- it guards §0.1 pt 2, it does not model anything]
    assert len(log) >= 20, f"only {len(log)} events — this control would be near-vacuous"

    mismatches = [(e.kind, e.subject, anchor_of(w, e)) for e in log
                  if anchor_of(w, e) != e.subject]
    assert not mismatches, (
        f"{len(mismatches)} of {len(log)} events where the replacement disagrees with the field "
        f"it replaces: {mismatches[:5]}")

    # and the actor channel specifically — the one the plan says fails silently
    act_caused = [e for e in log if actor_of(w, e) is not None]
    assert act_caused, "no event in this run was attributed to an act — the actor channel is dead"
    assert all(actor_of(w, e) == e.subject for e in act_caused)


def test_events_with_no_actor_are_a_real_population_not_an_empty_one():
    """The `None` branch has to be exercised by a real run, or `actor_of`'s second half is
    untested code asserting a distinction nothing reaches."""
    w = headless.run(seasons=2, seed=0)["world"]
    actorless = [e for e in w.log if actor_of(w, e) is None]
    # [JUSTIFIED: A POPULATION FLOOR, not a game value -- seed 0 x 2 seasons measured 99 actorless
    #  events, so 10 is an order of magnitude of headroom and still catches the case this exists
    #  for: the actor channel over-attributing until the None branch is never exercised.]
    assert len(actorless) >= 10, (
        f"only {len(actorless)} actorless events; the MATTER/clock population should be large "
        "and if it is not, the actor channel is over-attributing")
