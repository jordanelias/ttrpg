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

from ..data.rosters import COVER_KEY, COVER_KIND

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
    a = causing_act(w, e)
    return a.actor if a is not None else None


def causing_act(w, e: "Event"):
    """THE ACT THAT CAUSED THIS EVENT, or `None` -- `actor_of`'s first-match rule, returning the
    whole `Act` rather than its actor. `actor_of` reads it here, so the rule lives once (§8).

    Plan position `17a`: the obligee channel (`epistemic._ch_post_remit`) asks which SEAT an act was
    exercised through -- `Act.via`, `04 §B.9`'s *"a seat enters through `Act.via`"* -- and a person
    id cannot carry that. `None` is the same real answer it is for `actor_of`: nobody acted."""
    for c in e.causes:
        a = w.acts.get(c)
        if a is not None:
            return a
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
        # v9 IN-12 step 10 (#453 §9.3; K-19): TIER 1's ONE ALTERNATIVE ANSWER -- an actor holding a
        # LIVE COVER is anchored on the cover's id, the alias (`live_cover`). Nothing about who ACTED
        # changes: `actor_of` and `causing_act` still answer him, so `seen.who` (`epistemic._term_who`,
        # which reads the act) still names him to those present; what moves is what the Event is ABOUT
        # for every reader of the anchor -- the deposits' subject (`epistemic.claim_subjects`), the
        # knot-partner channel (`epistemic._ch_witness_key`, `pid == anchor`), `World._last_by_anchor`
        # and `trail_of`'s deeds-BY side. `world_q.event_place` places an act-caused Event by its
        # actor and not by this anchor, so where the Event happened does not move.
        return _cover_for(w, e, who) or who
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
        prior = event_by_id(w, c)
        if prior is not None and prior is not e:
            got = anchor_of(w, prior)
            if got is not None:
                return got
    # NO TIER 4. It read `Event.subject`, and G1b deleted the field once the only class that
    # needed it -- `plague.struck` and its kin, `causes=[ROOT]` with no change and no act -- was
    # shown to be apparatus and given a change of its own (module header). An Event arriving
    # here has no channel left that names what it concerns, and `None` says so.
    return None


def _cover_for(w, e: "Event", who: str) -> Optional[str]:
    """THE COVER `anchor_of` ANSWERS FOR AN ACT-CAUSED EVENT, or `None`. For a LOGGED Event, the cover
    its actor held WHEN IT WAS LOGGED (`World._covers_logged`, written by `World._on_logged` through
    `cover_at_logging`) -- never re-read, so a logged Event's anchor does not move when the cover later
    lapses, leaves his hand, or a second one is taken (`_on_logged`'s invariant, which
    `test_in56_last_emission_index.py` holds the index to). For an Event not yet logged (a reader
    inside RESOLVE, before the round's Events are appended), the live read (`live_cover`).

    ⚠ WHEN "LOGGED" IS [ASSUMPTION; medium; Jordan to correct; revert: the act's own moment, which
    needs the fold to record it]: the driver appends a round's Events after the round's whole fold
    (`loop/driver.py`), so a cover taken in a round covers every act of its taker logged with it, those
    resolved before the `conceal` in that round included, and `cover.assumed` itself anchors on the
    alias. A hand-built world without the log or the map reads live."""
    log = getattr(w, "log", None)
    has_id = getattr(log, "has_id", None)
    if has_id is not None and has_id(e.id):
        covers = getattr(w, "_covers_logged", None)
        return covers.get(e.id) if covers else None
    return live_cover(w, who)


def cover_at_logging(w, e: "Event") -> Optional[str]:
    """The live cover of the act's actor as the Event is logged -- `World._on_logged`'s one question
    of this module before it indexes the anchor; `None` for an Event no act caused."""
    return live_cover(w, actor_of(w, e))


def live_cover(w, actor: Optional[str]) -> Optional[str]:
    """v9 IN-12 step 10 (#453 §8.1 *Concealed identity*, §9.3; K-19): THE ID OF THE LIVE COVER `actor`
    HOLDS, or `None` -- `anchor_of`'s tier-1 cover read, its one owner.

    A COVER IS LIVE for `actor` when, all three: (1) he holds it -- a live `hold` among HIS OWN Tenures
    (S15: an edge is owned by its subject, so this reads his `Person.tenures`, never an index over every
    edge); (2) it is a `cover` (`COVER_KIND`) whose one key (`COVER_KEY`, `terms`) names HIM -- #453's
    *"where `terms == actor`"*: a cover handed to another hides nobody but the man it names, and only
    while that man holds it; (3) A STAGE IS UNMATURED (`_a_stage_unmatured`). Several at once answer the first by
    Record id, so the read is deterministic. A second cover is REACHABLE in computed play: `opening_set`
    declines it only through the holder's `content:cover` LEDGER claim (`held_document_declines`), which the
    ledger cap can evict and which two `conceal`s packed into one scene precede (MEASURED at B-Q's close:
    `build_realm(0)`, 2 seasons, one person holds two live covers).

    ⚠ A LIVE READ -- THE WORLD AS IT STANDS NOW. `anchor_of` asks it once per Event, as the Event is
    logged (`cover_at_logging`, kept in `World._covers_logged`), and never again for a logged Event:
    re-read later, the answer moves (the stages mature, the cover leaves his hand, he dies, a second
    is taken), and a logged Event's anchor must not (`_cover_for`).

    Cheap: an actor holding no `hold` on a cover returns at the second clause, no World-wide scan."""
    persons = getattr(w, "persons", None) or {}
    p = persons.get(actor) if actor is not None else None
    if p is None:
        return None
    found = []
    for t in p.tenures:
        if t.kind != "hold" or not t.live:
            continue
        rec = w.records.get(t.object)
        if rec is None or rec.kind != COVER_KIND:
            continue
        sm = rec.subject_matter if isinstance(rec.subject_matter, dict) else {}
        if sm.get(COVER_KEY) == actor and _a_stage_unmatured(w, rec):
            found.append(rec.id)
    return min(found) if found else None


def _a_stage_unmatured(w, rec) -> bool:
    """IS SOME DECLARED STAGE OF `rec` NOT YET RIPENED? -- `matured_terms`' count against the stage list,
    the log being the ruled carrier of *how many have ripened* (`matured_terms`' docstring). A Record
    with no stage has none unmatured. Two shortcuts, each EXACT rather than approximate, so the log is
    scanned only once every stage's tick has come: MATTER ripens a stage only AT its own due tick
    (`loop/matter.py`, `due != w.tick: continue`), so a stage due after now cannot have ripened; and
    `Record.matured` is set at every ripening (the same write), so a Record still `False` has ripened
    none."""
    stages = list(rec.stages or ())
    if not stages:
        return False
    if not rec.matured:
        return True
    if any(isinstance(st, tuple) and len(st) >= 3 and st[0] > w.tick for st in stages):
        return True
    return matured_terms(w, rec.id, stop=len(stages)) < len(stages)


def matured_terms(w, rid: str, stop: Optional[int] = None) -> int:
    """HOW MANY OF A RECORD'S DECLARED TERMS HAVE RIPENED -- counted off the log, r2 §A.6.3 DECIDED:
    *"the carrier for 'how many stages have ripened' is `w.log`"*. `Record.matured` is ONE bool for
    the whole Record (Jordan, 2026-09-10), so it cannot say how many.

    MATTER emits `term.matured` once PER RIPENING STAGE (`loop/matter.py`'s per-stage loop, through
    the gate on the `(Record, matured)` row, which declares exactly that kind), and the gate gives
    each emission a distinct id (`World.new_draw`), so N stages ripening in one tick are N Events.
    Matched on the MINTED RECEIPT's subject -- the Record the write named -- and NOT through
    `anchor_of`: tier 1 wins for an Event whose cause resolves to an act (a hand-built Record whose
    creating Event is not in the log falls back to the act that wound the clock), and that tier
    would answer the MAKER, not the Record (`H-129`'s shape). `matter.py`'s own `prior` lookup reads
    the receipt the same way.

    ⚠ MOVED HERE FROM `queries/world_q.py` AT v9 IN-12 step 10, UNCHANGED, which re-exports it for
    `ceiling`: `live_cover` (above) asks it from `anchor_of`, and `state/` imports nothing from
    `queries/` (`world_q` imports this module), so the one owner moved down rather than gaining a copy."""
    # `stop`: a caller that asks only whether the count REACHES a number (`_a_stage_unmatured`: every
    # declared stage) ends the scan there; the answer is `min(count, stop)`, which is all it reads.
    n = 0
    for e in w.log:
        if e.kind == "term.matured" and any(c.subject == rid for c in e.changes):
            n += 1
            if stop is not None and n >= stop:
                break
    return n


def event_by_id(w, eid: str):
    """The logged Event with this id, or `None`. Linear, and deliberately not indexed: the log
    is small, and an index would be a second structure to keep in step with `EventLog` for a lookup
    that is not hot. Callers: `anchor_of`'s tier-3 path, and since v9 FI-03
    `epistemic.trail_of` (once per covert kind per side of an inquiry's subject) and
    `loop/witness.py::_found_claims` (once per uncovered trail Event) -- both bounded by the
    findings, which are few -- and, since v9 SC-02 `22b` step 23, `world_q.standing_crossed` and
    `occasioned_by`, each behind `EventLog.has_id`'s O(1) guard."""
    for prior in getattr(w, "log", ()) or ():
        if prior.id == eid:
            return prior
    return None
