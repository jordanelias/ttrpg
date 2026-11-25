"""`season.state.attribution` -- WHO ACTED, and WHAT THE EVENT IS ABOUT, without `Event.subject`.

`04:402`: *"No `actor`, no `target`, no `subject` on `Event` -- the fields do not exist"*, and
`changes[]` carries the changed things individually. Attribution reads `causes[]` against the act
store, and the changed thing reads `changes[]`, which carries verified receipts rather than
assertions (`state/gate.py`).

⚠ `Event.subject` WOULD BE OVERLOADED, which is why no such field exists: the fold would set it to
`a.actor` (THE ONE WHO ACTED), `state/world.py` and `loop/matter.py` to THE THING WRITTEN, and every
reader would have to guess which it got (`epistemic._event_place` once guessed by asking whether the
id is a person, a site or a rung).

THREE TIERS, IN ORDER (`anchor_of`):

    1. the ACT channel   -- `causes[]` -> act store -> `actor`
    2. the CHANGE channel-- the first `changes[]` entry carrying a subject
    3. the CAUSE channel -- a consequence inherits the anchor of the Event that caused it

An Event reaching none of 1-3 anchors on `None`.

  * `condition.band_crossed` -- `loop/matter.py` emits it with NO changes, caused by the PRIOR
    EVENT that wrote the condition. Tier 3 recovers it exactly: the crossing is about whatever
    its cause was about.
  * Every `causes=[ROOT]`-and-no-`changes` Event in the tree is APPARATUS, never production: the
    fold's four emitters carry `[a.id]` (tier 1), the gate's emission carries a minted receipt
    (tier 2), and MATTER's `condition.band_crossed` names the write that crossed the floor
    (tier 3). The probe corpus's `Ev()`, `probes.py`'s P15 speech and `corpus_run`'s
    `planted_control` each carry a bare change naming what it is about
    (`harness/probes.py::about`), which is tier 2.

⚠ `None` IS A REAL, REACHABLE ANSWER FROM `anchor_of`, AND IT MEANS "NOBODY CAN SAY WHAT
THIS IS ABOUT". Every reader treats it as the absence it is: `_event_place` returns no place,
`_ch_witness_key` admits nobody, `last_emission_of` matches nothing. That makes a regression
here SILENT -- an emitter that drops its change vacates its witness channel and nothing raises.
`engine/season/tests/test_g1b_attribution.py` is the instrument against it: it plants such an
Event and asserts the witness deposits nothing for it, and it asserts over the probe corpus and
live runs that every logged Event anchors, with a population floor so an empty log cannot pass.
"""
from typing import TYPE_CHECKING, Optional

from ..data.rosters import COVER_AS, COVER_KEY, COVER_KIND

if TYPE_CHECKING:                       # pragma: no cover
    from .carriers import Event


def actor_of(w, e: "Event") -> Optional[str]:
    """WHO ACTED, or `None` for an Event no act caused.

    `None` IS A REAL ANSWER AND MUST NOT BE READ AS A GAP. MATTER's wear, the calendar's
    crossings and the clock's own emissions have no actor -- nobody did them -- and that is the
    distinction `Event.subject` could not express, because it held the written thing in exactly
    those cases and an actor everywhere else. A caller wanting "the one who did this" gets
    nothing when nobody did it, not a rung id that reads like a person.

    THE FIRST CAUSE THAT RESOLVES TO AN ACT WINS. `causes[]` may name prior Events as well as
    acts (§39.2), and the order is the fold's: `loop/resolve.py` puts `[a.id]` first and appends
    the occasion ids after it.
    """
    a = causing_act(w, e)
    return a.actor if a is not None else None


def causing_act(w, e: "Event"):
    """THE ACT THAT CAUSED THIS EVENT, or `None` -- `actor_of`'s first-match rule, returning the
    whole `Act` rather than its actor. `actor_of` reads it here, so the rule lives once (§8).

    The obligee channel (`epistemic._ch_post_remit`) asks which SEAT an act was
    exercised through -- `Act.via`, `04 §B.9`'s *"a seat enters through `Act.via`"* -- and a person
    id cannot carry that. `None` is the same real answer it is for `actor_of`: nobody acted."""
    for c in e.causes:
        a = w.acts.get(c)
        if a is not None:
            return a
    return None


def anchor_of(w, e: "Event") -> Optional[str]:
    """WHAT THE EVENT IS ABOUT. Three tiers, in order; see the module header.

    It returns `None` for an Event that reaches none of
    the three tiers -- no act among its causes, no change naming anything, no antecedent that
    anchors -- and that `None` is final: nothing else in the Event says
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
        # Written as "the first change carrying a subject" rather than `e.changes[0].subject`
        # so that a future change with an empty leading subject degrades to the next one instead
        # of returning None and silently vacating the channel.
        if c.subject:
            return c.subject
    # TIER 3 -- A CONSEQUENCE INHERITS ITS CAUSE'S ANCHOR. `loop/matter.py` emits
    # `condition.band_crossed` with NO changes, caused by the PRIOR EVENT that wrote the condition;
    # neither tier above reaches it.
    #
    # The reading is that a consequence is ABOUT whatever its cause was about -- the crossing
    # concerns the site whose condition moved.
    for c in e.causes:
        prior = event_by_id(w, c)
        if prior is not None and prior is not e:
            got = anchor_of(w, prior)
            if got is not None:
                return got
    # NO TIER 4: an Event arriving here has no channel left that names what it concerns, and
    # `None` says so.
    return None


def _cover_for(w, e: "Event", who: str) -> Optional[str]:
    """THE COVER `anchor_of` ANSWERS FOR AN ACT-CAUSED EVENT, or `None` -- the cover's id, or (B11.64) the PERSON whose name it
    borrows (`_cover_names`; `COVER_AS`), either one what the Event is ABOUT. For a LOGGED Event, the cover
    its actor held WHEN IT WAS LOGGED (`World._covers_logged`, written by `World._on_logged` through
    `cover_at_logging`) -- never re-read, so a logged Event's anchor does not move when the cover later
    lapses, leaves his hand, or a second one is taken (`_on_logged`'s invariant, which
    `test_in56_last_emission_index.py` holds the index to). For an Event not yet logged (a reader
    inside RESOLVE, before the lap's Events are appended), the live read (`live_cover`).

    ⚠ WHEN "LOGGED" IS [ASSUMPTION; medium; Jordan to correct; revert: the act's own moment, which
    needs the fold to record it]: the driver appends a lap's Events after the lap's whole fold
    (`loop/driver.py`), so a cover taken in a lap covers every act of its taker logged with it, those
    resolved before the `conceal` in that lap included, and `cover.assumed` itself anchors on the
    alias. A hand-built world without the log or the map reads live."""
    log = getattr(w, "log", None)
    has_id = getattr(log, "has_id", None)
    if has_id is not None and has_id(e.id):
        covers = getattr(w, "_covers_logged", None)
        return covers.get(e.id) if covers else None
    return _cover_names(w, live_cover(w, who))


def cover_at_logging(w, e: "Event") -> Optional[str]:
    """WHAT THE ACT'S ACTOR'S LIVE COVER MAKES OF HIM AS THE EVENT IS LOGGED -- `World._on_logged`'s one question
    of this module before it indexes the anchor; `None` for an Event no act caused or an actor with no cover.

    The answer is the anchor the cover gives (`_cover_names`): the NAME THE COVER BORROWS (`COVER_AS`, B11.64) when it names
    one, else the cover's own id. It is resolved HERE, once, and kept (`World._covers_logged`), so a logged Event's anchor never
    moves with the Record a cover is (`_cover_for`'s invariant): `actor_of`, `causing_act` and `seen.who` name the real hand
    whichever it is."""
    return _cover_names(w, live_cover(w, actor_of(w, e)))


def _cover_names(w, cover: Optional[str]) -> Optional[str]:
    """THE ANCHOR A COVER GIVES ITS HOLDER'S ACTS: the person it borrows the name of (`COVER_AS`), else its own id (the alias).
    `None` for no cover. The one owner of that choice, asked by `cover_at_logging` and by `_cover_for`'s live read."""
    rec = w.records.get(cover) if cover is not None else None
    sm = rec.subject_matter if rec is not None and isinstance(rec.subject_matter, dict) else {}
    return sm.get(COVER_AS) or cover


def live_cover(w, actor: Optional[str]) -> Optional[str]:
    """v9 IN-12 step 10 (#453 §8.1 *Concealed identity*, §9.3; K-19): THE ID OF THE LIVE COVER `actor`
    HOLDS, or `None` -- `anchor_of`'s tier-1 cover read, its one owner.

    A COVER IS LIVE for `actor` when, all three: (1) he holds it -- a live `hold` among HIS OWN Tenures
    (S15: an edge is owned by its subject, so this reads his `Person.tenures`, never an index over every
    edge); (2) it is a `cover` (`COVER_KIND`) whose one key (`COVER_KEY`, `terms`) names HIM -- #453's
    *"where `terms == actor`"*: a cover handed to another hides nobody but the man it names, and only
    while that man holds it; (3) A STAGE IS UNMATURED (`a_stage_unmatured`). Several at once answer the first by
    Record id, so the read is deterministic. A second cover is REACHABLE in computed play: `opening_set`
    declines it only through the holder's `content:cover` LEDGER claim (`held_document_declines`), which the
    ledger cap can evict and which two `conceal`s packed into one scene precede.

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
        if sm.get(COVER_KEY) == actor and a_stage_unmatured(w, rec):
            found.append(rec.id)
    return min(found) if found else None


def a_stage_unmatured(w, rec) -> bool:
    """IS SOME DECLARED STAGE OF `rec` NOT YET RIPENED? -- `matured_terms`' count against the stage list,
    the log being the ruled carrier of *how many have ripened* (`matured_terms`' docstring). A Record
    with no stage has none unmatured. Two shortcuts, each EXACT rather than approximate, so the log is
    scanned only once every stage's tick has come: MATTER ripens a stage only once its due tick has come
    (`loop/matter.py`, `due > w.tick: continue`, v11 CR-55), so a stage due after now cannot have ripened; and
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

    ⚠ IT LIVES HERE, NOT IN `queries/world_q.py` (which re-exports it for
    `ceiling`): `live_cover` (above) asks it from `anchor_of`, and `state/` imports nothing from
    `queries/` (`world_q` imports this module), so the one owner moved down rather than gaining a copy."""
    # `stop`: a caller that asks only whether the count REACHES a number (`a_stage_unmatured`: every
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
