"""`season.state.attribution` -- WHO ACTED, and WHAT THE EVENT IS ABOUT, without `Event.subject`.

`04:402` states the end position as STRUCTURAL: *"No `actor`, no `target`, no `subject` on
`Event` -- the fields do not exist"*, and `changes[]` carries the changed things individually.
**As of G1b (plan position 4, 2026-09-26) that claim is true of the code: the field is deleted.**
This module is what replaced it, and G1a is what made it possible: attribution reads `causes[]`
against the act store, and the changed thing reads `changes[]`, which now carries verified
receipts rather than assertions.

⚠ WHY THE FIELD HAS TO GO RATHER THAN BE TIDIED. `Event.subject` is OVERLOADED, and the two
senses are set by different emitters:

  * `loop/resolve.py` sets it to `a.actor`        -- THE ONE WHO ACTED
  * `state/world.py` and `loop/matter.py` set it  -- THE THING WRITTEN

Every reader then has to guess which it got. `epistemic._event_place` guesses by asking whether
the id is a person, a site or a rung, in an order its own docstring calls "the whole of this
function's correctness" -- because getting it wrong once made almost every Event private to its
own subject and `P15` could not tell a working channel from one broken closed. That hazard is a
consequence of the overload, not of the lookup.

THREE TIERS, IN ORDER. There were four, and the fourth was the field:

    1. the ACT channel   -- `causes[]` -> act store -> `actor`
    2. the CHANGE channel-- the first `changes[]` entry carrying a subject
    3. the CAUSE channel -- a consequence inherits the anchor of the Event that caused it
    (4. `Event.subject`  -- DELETED by G1b; an Event reaching none of 1-3 now anchors on `None`)

MEASURED, and the sequence of measurements matters more than any one of them. A first sweep of
1,428 events over 5 headless seeds found tiers 1-2 sufficient: 201 by act with 0 disagreements,
1,227 by change, 0 unrecovered. A wider sweep -- 3,411 events, 18 headless configurations --
agreed. **Both were the wrong population.** Running the PROBE CORPUS with tiers 1-2 only put 90
events through with no anchor at all and moved real behaviour: WITNESS deposits 9 -> 8, gate
writes 10,556 -> 10,477, four committed artifacts off byte-identity. Headless never crosses a
condition band, so the class that breaks this never appeared in it.

The two classes the corpus found:

  * `condition.band_crossed` -- `loop/matter.py` emits it with NO changes, caused by the PRIOR
    EVENT that wrote the condition. Tier 3 recovers it exactly: the crossing is about whatever
    its cause was about.
  * `plague.struck` -- `causes=[ROOT]`, no changes, no act, subject a rung. **Nothing in the
    Event held what it concerned** except the field, so tier 4 was the only thing that answered
    and this class was why the field could not go.

HOW THAT BLOCKER CLOSED, AND WHERE THE CLASS TURNED OUT TO LIVE. Every `causes=[ROOT]`-and-no-
`changes` Event in the tree was APPARATUS, never production: the fold's four emitters carry
`[a.id]` (tier 1), the gate's emission carries a minted receipt (tier 2), and MATTER's
`condition.band_crossed` names the write that crossed the floor (tier 3). The probe corpus's
`Ev()` -- `plague.struck` among its callers -- `probes.py`'s P15 speech and `corpus_run`'s
`planted_control` were the whole population, and each now carries a bare change naming what it
is about (`harness/probes.py::about`), which is tier 2. So the field went with no production
emitter changing, and one corpus Event MOVED IN THE RIGHT DIRECTION: A2's `sitting.decided`
(subject `D`, caused by a petition about `p_low`) had anchored on `p_low` through tier 3 while
the field said `D`; its own change now says `D`, the field's answer.

⚠ `None` IS NOW A REAL, REACHABLE ANSWER FROM `anchor_of`, AND IT MEANS "NOBODY CAN SAY WHAT
THIS IS ABOUT". Every reader treats it as the absence it is: `_event_place` returns no place,
`_ch_witness_key` admits nobody, `last_emission_of` matches nothing. That makes a regression
here SILENT -- an emitter that drops its change vacates its witness channel and nothing raises.
`engine/season/tests/test_g1b_attribution.py` is the instrument against it: it plants such an
Event and asserts the witness deposits nothing for it, and it asserts over the probe corpus and
live runs that every logged Event anchors, with a population floor so an empty log cannot pass.
"""
from typing import TYPE_CHECKING, Optional

if TYPE_CHECKING:                       # pragma: no cover
    from .carriers import Event


def actor_of(w, e: "Event") -> Optional[str]:
    """WHO ACTED, or `None` for an Event no act caused.

    `None` IS A REAL ANSWER AND MUST NOT BE READ AS A GAP. MATTER's wear, the calendar's
    crossings and the clock's own emissions have no actor -- nobody did them -- and that is the
    distinction `Event.subject` could not express, because it held the written thing in exactly
    those cases and an actor everywhere else. A caller wanting "the one who did this" now gets
    nothing when nobody did it, instead of a rung id that reads like a person.

    THE FIRST CAUSE THAT RESOLVES TO AN ACT WINS. `causes[]` may name prior Events as well as
    acts (§39.2), and the order is the fold's: `resolve.py:309` puts `[a.id]` first and appends
    the occasion ids after it. Measured: 201 of 201 act-caused events agree with the field this
    replaces, so the first-match rule is the field's own rule rather than a new one.
    """
    for c in e.causes:
        a = w.acts.get(c)
        if a is not None:
            return a.actor
    return None


def anchor_of(w, e: "Event") -> Optional[str]:
    """WHAT THE EVENT IS ABOUT. Three tiers, in order; see the module header for the measurement.

    This is the function `Event.subject` was performing, with the overload made explicit instead
    of left for each reader to disentangle. It returns `None` for an Event that reaches none of
    the three tiers -- no act among its causes, no change naming anything, no antecedent that
    anchors -- and since the field is gone, that `None` is final: nothing else in the Event says
    what it concerns.
    """
    who = actor_of(w, e)
    if who is not None:
        return who
    for c in e.changes:
        # `changes[0].subject` in 1,058 of 1,058 measured, and no event spans two subjects --
        # but written as "the first change carrying a subject" rather than `e.changes[0].subject`
        # so that a future change with an empty leading subject degrades to the next one instead
        # of returning None and silently vacating the channel.
        if c.subject:
            return c.subject
    # TIER 3 -- A CONSEQUENCE INHERITS ITS CAUSE'S ANCHOR, and the corpus is why this tier
    # exists. `loop/matter.py` emits `condition.band_crossed` with NO changes, caused by the
    # PRIOR EVENT that wrote the condition; neither tier above reaches it, so the first two
    # tiers alone vacated the channel for every crossing in the corpus -- 90 events on one run,
    # deposits 9 -> 8, gate writes 10,556 -> 10,477. A headless sweep of 3,411 events reported
    # zero, because headless never crosses a band. That gap is the whole lesson of this tier:
    # the first measurement was of the wrong population.
    #
    # The reading is that a consequence is ABOUT whatever its cause was about -- the crossing
    # concerns the site whose condition moved -- and it reproduces the field exactly on that
    # population rather than approximating it.
    for c in e.causes:
        prior = _event_by_id(w, c)
        if prior is not None and prior is not e:
            got = anchor_of(w, prior)
            if got is not None:
                return got
    # NO TIER 4. It read `Event.subject`, and G1b deleted the field once the only class that
    # needed it -- `plague.struck` and its kin, `causes=[ROOT]` with no change and no act -- was
    # shown to be apparatus and given a change of its own (module header). An Event arriving
    # here has no channel left that names what it concerns, and `None` says so.
    return None


def _event_by_id(w, eid: str):
    """The logged Event with this id, or `None`. Linear, and deliberately not indexed: the log
    is small, this runs only on the tier-3 path, and an index would be a second structure to
    keep in step with `EventLog` for a lookup that is not hot."""
    for prior in getattr(w, "log", ()) or ():
        if prior.id == eid:
            return prior
    return None
