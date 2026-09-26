"""G1b -- attribution without `Event.subject`, AND THE FIELD IS NOW DELETED.

THE CONTROL THIS FILE OPENED WITH COMPARED THE ACCESSORS AGAINST THE FIELD, AND IT COULD ONLY
EXIST WHILE THE FIELD DID. It said so: *"When the field goes, [the equivalence test] is the test
that must be deleted with it, and its deletion is the moment the equivalence stops being
checkable. Anything relying on that equivalence should have its own falsifier by then."* The
field went in G1b's finish (plan position 4, 2026-09-26). The equivalence was measured ONE LAST
TIME ACROSS THE DELETION -- every logged Event of the populated realm, four headless runs and the
whole probe corpus, the pre-deletion field against the post-deletion `anchor_of`, keyed by Event
id: 0 disagreements, and one Event moved (A2's `sitting.decided`, onto the field's own answer;
see `state/attribution.py`). What replaces it here are the falsifiers that equivalence was
standing in for, each able to observe the failure G1b's plan names -- *"silently vacating the
actor channel"* -- without the field to compare against:

  1. THE PLANTED EVENT. An Event with no act, no change and `[ROOT]` anchors on NOTHING, and the
     witness deposits nothing for it -- under every fan-out arm -- beside a control that differs
     only in carrying a change and IS deposited. The negative half is the plan's own falsifier;
     the positive half is what stops it passing because WITNESS is broken.
  2. THE CORPUS COUNT. Every logged Event in the probe corpus anchors, over a population floor
     so an empty corpus cannot pass -- the population where the blocker class lived.
  3. THE LIVE RUNS, AGAINST INDEPENDENT RECORDS. `actor_of` against the id the fold MINTED FROM
     the actor; each tier-2 anchor against the gate's own mint ledger; each tier-3 crossing
     against `w.crossings`, which `_crossings` writes from its own argument.
"""
import dataclasses

import pytest

from engine.season.data.rosters import FAN_OUT_MODES
from engine.season.data.fixtures import DEFAULT_FIXTURES
from engine.season.harness import headless
from engine.season.harness import probes as P
from engine.season.state import world as world_mod
from engine.season.state.acts import ActStore
from engine.season.state.attribution import actor_of, anchor_of
from engine.season.state.carriers import Act, Event, StateChange
from engine.season.state.ids import H, ROOT


class _W:
    """The two attributes the accessors touch, and nothing else."""
    def __init__(self, acts=None):
        self.acts = acts or ActStore()
        self.log = []


def _ev(causes, changes=None):
    return Event(id="e1", kind="k", changes=changes or [], causes=list(causes), emitted_at=1)


# -- the field is gone --------------------------------------------------------------------

def test_event_has_no_subject_field_and_refuses_one():
    """`04:402`'s STRUCTURAL claim, *"No `actor`, no `target`, no `subject` on `Event` -- the
    fields do not exist"*, as an executed fact rather than a docstring. A dataclass refuses an
    undeclared keyword, so a constructor still passing `subject=` fails loudly -- the silent
    failure is the POSITIONAL one, which is why every positional `Event(...)` was shifted by hand."""
    names = {f.name for f in dataclasses.fields(Event)}
    assert not names & {"subject", "actor", "target"}, sorted(names)
    with pytest.raises(TypeError):
        Event(id="e", kind="k", subject="x", changes=[], causes=[ROOT], emitted_at=0)


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
    """A fold-emitted Event has both. The field it replaced held the ACTOR there, so this must."""
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
    cause = Event(id="e_prior", kind="condition.changed",
                  changes=[StateChange("site_harbour", "set", "MATTER", "condition")],
                  causes=[ROOT], emitted_at=1)
    w.log = [cause]
    crossing = Event(id="e_cross", kind="condition.band_crossed",
                     changes=[], causes=["e_prior"], emitted_at=1)
    assert anchor_of(w, crossing) == "site_harbour"


# ⚠ `test_tier_4_is_the_field_and_it_is_the_blocker` IS DELETED HERE, ON PURPOSE, AS ITS OWN
# DOCSTRING ASKED: *"Finishing G1b means giving this class an antecedent or a receipt and making
# tier 4 unreachable -- at which point this test is deleted ON PURPOSE."* Tier 4 was the field, the
# class (`plague.struck`, `causes=[ROOT]`, no change, no act) turned out to be apparatus only, and
# `harness/probes.py::about` gives it a change. What the deleted test pinned -- that such an Event
# still answered -- is now false by design, and the next test pins the replacement answer.

def test_an_event_reaching_no_tier_at_all_returns_None():
    """No act among its causes, no change naming anything, no antecedent that anchors: NOTHING
    in the Event says what it concerns, and with the field gone there is no fallback. `None`,
    and every reader must treat it as the absence it is -- which the next test executes."""
    w = _W()
    plague = Event(id="e_p", kind="plague.struck", changes=[], causes=[ROOT], emitted_at=1)
    assert actor_of(w, plague) is None
    assert anchor_of(w, plague) is None
    # and a ROOT-caused Event with a change naming what it is about still anchors -- the carrier
    # `harness/probes.py::about` gives every apparatus Event, so the None above is the change's
    # absence and nothing else.
    assert anchor_of(w, Event(id="e_q", kind="plague.struck", changes=[P.about("R")],
                              causes=[ROOT], emitted_at=1)) == "R"


# -- FALSIFIER 1: the planted Event nothing anchors is witnessed by nobody ------------------

def _deposits_for(w, e) -> list:
    """The `claim.deposited` emissions WITNESS made FOR `e` -- every deposit site in
    `loop/witness.py` passes `causes=[e.id]`, so this is exact per Event, not a diff of totals."""
    return [x for x in w.log if x.kind == "claim.deposited" and e.id in x.causes]


# SORTED: the roster is a set, and an unordered parametrize collects in a per-process order that
# `pytest -n auto` refuses ("Different tests were collected between gw0 and gw1").
@pytest.mark.parametrize("mode", sorted(FAN_OUT_MODES))
def test_an_event_that_anchors_nowhere_is_deposited_to_nobody(mode):
    """THE PLAN'S FALSIFIER, RUN THROUGH A REAL SEASON: *"plant a probe Event with no changes and
    `[ROOT]`: `anchor_of` returns `None` AND the witness deposits nothing for it."*

    ⚠ OVER EVERY FAN-OUT ARM, AND `total` IS WHY. The channel predicates admit nobody for an
    anchorless Event on their own -- `_event_place` finds no place, `_ch_witness_key` no key, the
    document channel no change. `total` consults no predicate: it fans every Event to everyone,
    and before `claim_subjects` stopped depositing about `None` it minted `Claim(subject=None)`
    into all five ledgers of this world (measured). The arms are read from the roster, so a
    fourth arm is covered by existing.

    ⚠ THE CONTROL IS THE SAME KIND, IN THE SAME WORLD AND SEASON, DIFFERING ONLY IN CARRYING A
    CHANGE NAMING `R`. Without it, zero deposits would also be what a broken WITNESS reports --
    §0.1 pt 4, a number without a control."""
    w = P.tiny_world(DEFAULT_FIXTURES.sweep("fan_out_mode", mode))
    none = Event(H(w.world_seed, w.tick, "R", "planted:anchorless"), "plague.struck",
                 [], [ROOT], w.tick)
    some = P.Ev(w, "R", "plague.struck", "R", [ROOT])
    assert anchor_of(w, none) is None
    assert anchor_of(w, some) == "R"

    P._run(w, actorless=[none, some])
    assert none in w.log and some in w.log, "the planted Events never reached the log"

    assert _deposits_for(w, some), (
        f"[{mode}] the CONTROL Event, which anchors on `R`, was deposited to nobody -- WITNESS "
        "itself is not depositing, so the zero asserted below would observe nothing")
    assert not _deposits_for(w, none), (
        f"[{mode}] an Event NOTHING anchors was deposited {len(_deposits_for(w, none))} time(s). "
        "With `Event.subject` gone, a claim minted from it is about nothing -- an instrument gap "
        "becoming a belief, which `witness` refuses for UNKNOWN on the same ground")
    assert not [c for p in w.persons.values() for c in p.ledger if c.subject is None], (
        f"[{mode}] a claim with subject None reached a ledger")


# -- FALSIFIER 2: the probe corpus, where the blocker class lived ---------------------------

def test_every_logged_event_in_the_probe_corpus_anchors(monkeypatch):
    """⚠ THE POPULATION THAT MATTERS, AND THE COUNT ASSERTS THAT IT ASSERTED.

    `state/attribution.py` records the lesson: a first sweep over headless runs found the tiers
    sufficient and was THE WRONG POPULATION -- headless never crosses a band and builds no
    apparatus Event, so the class that blocked the deletion never appeared in it. The probe
    corpus is where `plague.struck` and every other hand-built Event live, so this runs every
    probe and reads every World it built. A probe that drops `about(...)` leaves its Event
    anchoring on nothing, and it lands here as a named Event rather than as a quiet channel.

    Probes REFUSE by design -- a GAP verdict is a raise -- so each is called for the Worlds it
    builds and its verdict is not this test's business (`run_cases.run_probe` owns that, and
    caches it, which is why this calls the probe function rather than the runner)."""
    worlds = []
    real_init = world_mod.World.__init__

    def _capturing_init(self, *a, **k):
        real_init(self, *a, **k)
        worlds.append(self)

    with monkeypatch.context() as m:
        m.setattr(world_mod.World, "__init__", _capturing_init)
        for spec in P.PROBES.values():
            try:
                spec["fn"]()
            except Exception:                               # noqa: BLE001 -- see docstring
                pass

    anchored, anonymous = 0, []
    crossings_checked = 0
    for w in worlds:
        by_id = {e.id: e for e in w.log}
        for e in w.log:
            if anchor_of(w, e) is None:
                anonymous.append((e.kind, e.id))
            else:
                anchored += 1
        # TIER 3 AGAINST AN INDEPENDENT RECORD: `_crossings` appends
        # `(subject_id, verb, before, after, ev.id)` from its OWN argument, so a crossing whose
        # anchor disagrees with the site it was emitted for is caught here, not merely counted.
        for sid, _verb, _was, _now, eid in w.crossings:
            assert anchor_of(w, by_id[eid]) == sid, (
                f"crossing {eid} was emitted for {sid!r} and anchors on "
                f"{anchor_of(w, by_id[eid])!r}")
            crossings_checked += 1

    assert not anonymous, (
        f"{len(anonymous)} logged probe Event(s) anchor on NOTHING: {anonymous[:5]} -- an "
        "emitter built an Event with no act, no change and no anchored antecedent. Give it "
        "`harness/probes.py::about(...)`, or it is witnessed by nobody")
    # [JUSTIFIED: A VACUITY FLOOR, not a game value -- measured 2026-09-26 at 10,559 logged Events over 111 Worlds (76 by act, 10,469 by change, 14 by cause); 5,000 is half that, and a corpus that stopped building Worlds or logging Events fails here instead of passing on an empty loop]
    assert anchored >= 5000, f"only {anchored} anchored Events -- this check is near-vacuous"
    # [JUSTIFIED: A VACUITY FLOOR -- measured 14 crossings in the corpus; the tier-3 check above is vacuous at 0, and this is the only population that reaches it]
    assert crossings_checked >= 10, f"only {crossings_checked} crossings checked"


# -- FALSIFIER 3: live runs, against records the accessors do not read ---------------------

_FOLD_PURPOSES = ("{kind}:{act}", "act.ineligible:{act}", "refused:{act}")


# Four (seed, seasons) pairs, the same sample the field-equivalence control ran on. Nothing in
# the model reads them as quantities -- they select which runs are checked.
# [JUSTIFIED: SEEDS AND SEASON COUNTS, not game values -- the property behind them was measured at 3,411 events]
@pytest.mark.parametrize("seed,seasons", [(0, 1), (0, 2), (1, 3), (42, 2)])
def test_every_event_anchors_and_each_tier_agrees_with_an_independent_record(seed, seasons):
    """⚠ THE REWRITE OF `test_the_accessors_reproduce_the_field_exactly`, WHOSE CONTROL WAS THE
    FIELD. With the field gone, each tier is checked against a record the accessor does NOT read:

      * TIER 1 -- `actor_of` walks `causes[]` into the act store. The fold MINTED the Event's id
        from `a.actor` at emission (`H(seed, tick, a.actor, f"{kind}:{a.id}")`, or the
        refusal/ineligibility purposes, `loop/resolve.py`). So the id must re-derive from the
        actor the store returns: a store answering a different person breaks the hash.
      * TIER 2 -- in a LIVE run every anchoring change must be a receipt the gate actually
        minted (`Gate.issued`, identity). A production emitter anchoring through a hand-built
        change -- the transitional seam `harness/probes.py::about` uses on purpose -- is exactly
        the regression that looks fine and is not.
      * EVERY EVENT ANCHORS: `None` on a live run is a vacated channel, never an answer.

    Measured 2026-09-26: 100% on every clause over these four runs (544 Events) and over
    `populated.build_realm(0)` x 1 season (2,882 Events: 367 by act, 2,515 by receipt).
    """
    w = headless.run(seasons=seasons, seed=seed)["world"]
    log = list(w.log)
    # The smallest run in the parametrize above emits 39 events (seed 0 x 1 season, measured), so
    # this clears the real floor with room and still fails loudly if a change empties the log.
    # [JUSTIFIED: A VACUITY FLOOR, not a game value -- it guards §0.1 pt 2, it does not model anything]
    assert len(log) >= 20, f"only {len(log)} events — this control would be near-vacuous"

    anonymous = [(e.kind, e.id) for e in log if anchor_of(w, e) is None]
    assert not anonymous, f"{len(anonymous)} of {len(log)} live Events anchor on nothing: {anonymous[:5]}"

    by_act, by_receipt = 0, 0
    for e in log:
        who = actor_of(w, e)
        if who is not None:
            act_id = next(c for c in e.causes if w.acts.get(c) is not None)
            minted = {H(w.world_seed, e.emitted_at, who, p.format(kind=e.kind, act=act_id))
                      for p in _FOLD_PURPOSES}
            assert e.id in minted, (
                f"{e.kind} {e.id}: `actor_of` says {who!r}, but the fold did not mint this id "
                "from that actor -- the act channel attributes to someone the emitter did not")
            by_act += 1
            continue
        lead = next((c for c in e.changes if c.subject), None)
        if lead is not None:
            assert w.gate.issued(lead), (
                f"{e.kind} {e.id} anchors on {lead.subject!r} through a change the gate never "
                "minted -- a live emitter is leaning on the transitional seam")
            by_receipt += 1

    # and the actor channel specifically — the one the plan says fails silently
    assert by_act, "no event in this run was attributed to an act — the actor channel is dead"
    assert by_receipt, "no event anchored on a minted receipt — the change channel is dead"


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
