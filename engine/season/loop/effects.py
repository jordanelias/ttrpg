"""`season.loop.effects` — the resolver's BODY. One effect per verb that writes.

EXTRACTED, step 5 of the decomposition (a PURE MOVE). `EFFECTS`, its decorator, the ONE operand
reader (`_operand`) and the eleven `_eff_*` (ten until `release`, 2026-09-11) move together and
must: §8's *"THE OWNER OF THE RULE, AND
THREE EFFECTS HAD THEIR OWN COPY"* is about `_operand` specifically, and the decorator-filled
table has to be defined where the decorated functions are or it is empty when the fold reads it.

WHAT THIS MODULE IS AGAINST, which is the reason it exists at all (§27.2). The fold once took an
`effect` parameter — a CALLER-SUPPLIED LAMBDA that inspected `a.verb` and returned Events, and
every probe wrote its own. That is a resolver per caller, each free to disagree about what a verb
does. A verb-keyed effect registered here is one implementation for every caller, and a verb with
a `writes:` column and no effect REFUSES rather than silently writing nothing. Register row H-63.

⚠ NOTHING HERE TAKES A WRITE TOKEN, AND NO EFFECT CALLS `w.write`. The first version of this
docstring said every effect writes THROUGH `w.write(...)`, which is the exact inversion the old
`_eff_confer` docstring refuted -- *"AN EFFECT MUTATES AND RETURNS THE IDS IT TOUCHED; IT DOES NOT
CALL `w.write` … My first version did both, and the fold correctly refused."* Caught by a
read-only critic, and it is §47's failure exactly: a false claim of enforcement stops the next
reader checking.

⚠⚠ G4 (plan position 7): THE CONTRACT EVERY EFFECT HERE IS WRITTEN TO, AND IT CHANGED. An effect
no longer MUTATES and REPORTS; it DESCRIBES. It reads the world as its predecessors left it and
returns a `state/gate.py::Change` -- the SUBJECTS it will write, named BEFORE anything moves, and
the write (`apply`), which still goes through the store's own methods (`add_tenure`,
`remove_person`, `_grant_remit`), because those are the one owners of their rules. The fold hands
the `Change` to `World.write`, which reads every subject, applies, reads again, and mints a receipt
for each subject that MOVED and for no other; if none moved it raises `NoOpReceipt` and the fold
emits the row's refusal (`04 §C.2`, F9). So an effect says what it will write and THE GATE says
whether it did -- the bookkeeping several effects carried to avoid claiming a write that did not
happen (`establish`'s `moved`, `_grant_remit`'s return value read as an `earned` filter) is the
gate's now, once.

WHAT EACH EFFECT NAMES IS A DECISION, and each docstring below states its own. Two rules hold for
all twelve, and both exist to keep every hash that is not `work`'s where it was:

  1. AN EFFECT NAMES THE IDS IT USED TO REPORT, IN THE ORDER IT REPORTED THEM -- and where it
     used to decide by hand WHETHER to report one (`establish`'s office), it names it always and
     the gate decides. So the receipts a success Event carries are exactly the ones it carried,
     and `content_hash` folds each receipt. Naming MORE
     (`move`'s legs, `create_record`'s `hold`, `kill`'s cascade) would add receipts to Events that
     have always carried fewer and move hashes no no-op refusal explains. The unnamed Tenures are
     still SEEN -- F3 judges every Tenure written, and a no-op refusal puts them back.
  2. DECLINING IS `NO_CHANGE`. An effect that decides not to write (`transfer` to a non-rung, a
     `move` up no ladder, an `utter` over an existing Proposition) returns it, and the gate's
     `NoOpReceipt` is the refusal -- the same channel as an effect that ran and moved nothing.
"""

from __future__ import annotations

from dataclasses import asdict
from typing import Optional

from ..data.requires import REQUIRES_OPERANDS
from ..data.rosters import (
    DECLARED, FIELD_CASUALTY_MODELS, LOST, PURSUIT_AXES, FELLED, RECORD_CONTENT, RECORD_KIND_KEYS,
    RELEASABLE_KINDS, RUNG_KINDS, SITE_KINDS, UNOPPOSED, WOUND_HARM_MODELS, faction_prop_id,
    require_member,
)

from ..gaps import Forbidden, InstrumentDefect, Unspecified
from ..loop.predicates import office_described_by
from ..queries import faction_q
from ..queries.world_q import (
    RESIDE_KIND, ancestry, capacity, ceiling, docketed, faction_holding, hold_force,
    holder_faction_of, home_of, place_of, population, residence_of, share, upkeep_of, works_for,
    works_target,
)
from ..state.carriers import Proposition, Record, Rung, Site, Tenure, Term
from ..state.gate import NO_CHANGE, Change, Subject, may_renew
from ..state.ids import H
from ..state.world import rung_kind_ascends
from ..trace_log import TRACE

# ⚠ THE SCAR ACCUMULATOR'S PRECISION, AND IT EXISTS TO MAKE THE FOLD ORDER-INDEPENDENT.
# `scar` accumulates across acts, and incremental IEEE addition is NON-ASSOCIATIVE -- the control
# `results.json`'s A5 row already records on this tree is exactly it (five float deltas summed in
# two orders give 0.30000000000000004 vs 0.3; the same five as integers are identical), and A5's
# own conclusion is that *"a one-ulp difference at a band floor is A VERB THAT EXISTS IN ONE
# ORDERING AND NOT ANOTHER"*. Because `scar` reaches `repr(Person)` -> `_entity_digest` ->
# `content_hash`, a one-ulp divergence moves the hash too. `S27.3`'s answer elsewhere is
# sum-then-clamp-once, which needs the whole set at once and this write does not have it;
# rounding each accumulation to a fixed place buys the same property -- `round(a+b) == round(b+a)`
# -- for a per-act writer.
# [JUSTIFIED: a PRECISION, not a game value -- six places is far below any magnitude `scar_step` can take and exists only to keep accumulation associative; nothing in the model reads it as a quantity]
_SCAR_DP = 6  # ED-IN-0249 / H-128 -- the scar accumulator's precision, order-independence only


# ---------------------------------------------------------------------------
# THE EFFECTS. One per verb, OWNED BY THE RESOLVER.
#
# ⚠ PART E's `writes:` COLUMN NAMES THE CELL AND NEVER THE VALUE. `transfer` writes
# `(Rung, stores)` -- it does not say BY HOW MUCH, or that the giver's store goes DOWN. Without
# that the fold checks a precondition, emits, and changes nothing, so `transfer` twice from a
# one-unit larder succeeds twice: the scarcity §27.1 rests on never happens.
#
# THE DISTINCTION FROM THE `effect` PARAMETER W3 REMOVED IS THE WHOLE POINT, and it is §27.2's.
# A CALLER-supplied lambda is a second resolver: every caller may disagree about what a verb does,
# and each probe did. A VERB-KEYED effect registered here is the resolver's BODY -- one
# implementation, the same for every caller, and a verb with a `writes:` and no effect REFUSES
# rather than silently writing nothing.
#
# This gap is register row H-63.
# ---------------------------------------------------------------------------
EFFECTS: dict = {}


def effect_for(verb: str):
    def deco(fn):
        EFFECTS[verb] = fn
        return fn
    return deco


def _operand(a: "Act", name: str):
    """THE FOLD'S ONE READ OF A CARRIED OPERAND. A missing one RAISES.

    ⚠ AN ABSENT OPERAND AT RESOLVE IS AN `InstrumentDefect`, NOT A REFUSAL, AND THE DISTINCTION
    IS THE WHOLE OF `W-C`'s SECOND HALF. A refusal says *the world would not permit this*; a
    caller minting a `transfer` that names no receiver is saying nothing about the world at all.
    Filing it as a refusal would emit `emits_on_refusal`, `W-B` would deposit that at WITNESS, and
    every witness would end the season holding a belief about a granary the act never named --
    the instrument's own gap, laundered into the game as evidence. `operands_for` is what makes
    this unreachable from a COMPUTED act: a Candidate whose operands cannot be derived is never
    formed, so an act arriving here without one came from a hand-written call site.

    ⚠ IT IS THE OWNER OF THE RULE, AND THREE EFFECTS HAD THEIR OWN COPY. `_eff_move` raised on a
    missing `to` and `_eff_work` on a missing `site` -- both correct, both written twice -- while
    `_eff_transfer` DEFAULTED four operands (`from`/`to` to `""`, `kind` to `"grain"`, `amount` to
    `1`) and `_eff_confer` defaulted `to` to the actor, i.e. conferred an office on whoever
    happened to be acting when the act named nobody. Same situation, four verbs, three answers.
    §8: the rule lives once."""
    d = a.payload if isinstance(getattr(a, "payload", None), dict) else {}
    if d.get(name) is None:
        raise InstrumentDefect(
            f"a {a.verb!r} reached its effect with no {name!r} operand. The fold binds operands "
            f"from the act's payload and `operands_for` forms NO Candidate whose operands it "
            f"cannot derive, so an act minted without one is a CALLER defect and not a design "
            f"gap -- and fabricating a value here would name a thing nobody chose. Payload: "
            f"{sorted(d)}")
    return d[name]


# --- THE GOVERNANCE SLICE'S EFFECTS. `dispatch` needs none: Part E gives it `writes: []`, so an
# order is an EMISSION and nothing else, which is `L1` in one row -- a dispatch does not move a
# person, it tells one, and whether they go is their own act next season.

@effect_for("confer")
def _eff_confer(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """Seats an office: a new `hold` Tenure opens, and any prior holder's closes.

    ⚠ IT DOES NOT CALL `w.write`, AND IT NO LONGER MUTATES WHERE IT DECIDES. Before G4 the fold
    called it INSIDE the gate's `apply()` and it returned the ids it had touched; a nested
    `w.write` there was a write inside a write, which the fold refused (my first version did both).
    Now it returns a `Change` and the gate applies it.

    G4 -- WHAT IT NAMES: THE EDGES, EACH WITH THE KIND IT EARNS. Every live `hold` on the office
    (`tenure.closed`) and the new one (`tenure.opened`), opened-first as the old mapping reported
    them. Each is an `edge` subject, judged by G3's diff: a closed hold's `until` moves, the new
    hold appears. So conferring onto an UNHELD office names no closure and earns no
    `tenure.closed`, which the old per-kind mapping did by hand. It cannot be a no-op in practice
    -- the new hold always opens -- but if it were, it would refuse like any other.

    ⚠ G3 -- BOTH ITS WRITES ARE ON EDGES SOMEBODY ELSE OWNS, AND EACH IS DECLARED. The write gate's
    F3 clause (`state/gate.py::tenure_write_basis`) admits the conferee's new `hold` under the
    CONFERRAL basis -- `Act.via` names a seat the actor sits in whose purview reaches this seat,
    which declares a rostered conferral basis -- and the incumbent's closed `hold` under `T-o`, the
    seat's revocation basis exercised through the same `via` (or `T-m`, where the incumbent is the
    actor). Without them the gate raises `NotYours` and puts both edges back. `_req_confer` asks the
    same two predicates first, so the shipped fold refuses (and emits) before this ever runs."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    # ⚠ `to` WAS `d.get("to") or a.actor` -- a silent default that seated the ACTOR whenever the
    # act named nobody, which is the same class as `_eff_transfer`'s four and is deleted with
    # them. A conferral onto nobody is a malformed act, not a self-conferral.
    # ⚠ THIS CHANGE IS A DELIBERATE EXTRA AND NOT A PATH `H-94` MADE REACHABLE; RECLASSIFIED BY
    # THE `W-C` ADVERSARIAL PASS, because filing it as a consequence overstates what closing the
    # operand channel did. NO COMPUTED ACT CAN REACH THIS EFFECT: `confer` is untyped, `office`
    # is not in `rosters.yaml: requires_operands` so `operands_for` can never derive one, and
    # `_req_confer` returns False when the payload names none -- `corpus_run`'s own output lists
    # `confer` among the verbs "foldable but never even attempted". The improvement is real (a
    # silent self-conferral becomes a loud `InstrumentDefect`) and nothing measurable moved.
    obj, to = d.get("office"), _operand(a, "to")
    if not obj or obj not in w.offices:
        return NO_CHANGE
    closed = [t for t in w.tenures if t.kind == "hold" and t.object == obj and t.live]
    nt = Tenure(H(w.world_seed, w.tick, to, f"hold:{obj}"), to, obj, "hold", w.tick)

    def perform() -> None:
        for t in closed:
            t.until = w.tick
        w.add_tenure(nt)
    # ⚠ PER-KIND. Conferring onto an UNHELD office closes nothing, and returning a flat list made
    # the fold publish `tenure.closed` anyway -- a state change that did not happen, which is the
    # fabricated-`person.died` class committed inside the fix for it. Each subject now carries the
    # kind it earns, and a kind no moved subject earned is not emitted (`loop/resolve.py::_fold`).
    #
    # ⚠ `nt.id`, NOT `[obj, to]` -- KEPT AS THE TENURE'S OWN ID, DELIBERATELY, AFTER A REJECTED
    # ALTERNATIVE. A first version of this fix reported `[obj, to]` (the office and the new
    # holder) so a witness's claim would name something legible. It was wrong: `_apply_write`
    # mints a Receipt against THIS write pair's field (`Tenure.until`, `verb_table.yaml`'s first
    # `writes:` entry for `confer`) for every id an effect reports, so `[obj, to]` minted
    # `(off_dicastery, set, Act, until)` and `(p_mid, set, Act, until)` -- Receipts asserting that
    # an OFFICE and a PERSON each had a `Tenure.until` write, which did not happen to either; only
    # the new Tenure did. That is the ID-9 class of defect this file's other comments name --
    # "an Event reporting a state change that did not happen" -- one seam over, in the Receipt
    # rather than the Event. Found by an adversarial critique of the first version. The Receipt
    # must name what was ACTUALLY written; H-71's others-half is closed at the READER instead --
    # see `epistemic.claim_subjects`'s Tenure-lifecycle expansion, which turns a `tenure.opened`/
    # `tenure.closed` Receipt naming a Tenure into claims about the two entities that Tenure
    # connects, on the same read `_ch_document_key` already does. One reader rule serves `confer`,
    # `revoke` and `release` alike, rather than three effects each inventing their own legible id.
    return Change((Subject.edge(nt, "tenure.opened"),)
                  + tuple(Subject.edge(t, "tenure.closed") for t in closed), perform)


@effect_for("establish")
def _eff_establish(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """Founds an office, or changes an existing office's remit -- and in the SAME act re-stamps the
    grant on every live `hold` on it.

    `_req_establish` has already refused everything that would make the constructor raise, so the
    `Office` built here is the one it admitted; if it is built from an act that skipped the
    precondition, the constructor's raise is the backstop and is left loud. `None` (an operand
    missing) is `NO_CHANGE`, and the fold emits `establish.refused`.

    A NEW id: the office is stored as the precondition admitted it. (It carried `establishment` at
    its default until plan position `17a` deleted that field, its matrix row and this row's
    `writes:` entry together: who serves a seat is `world_q.establishment_of`, a Query over live
    `oblige` Tenures, which no `establish` writes.) An
    EXISTING id: `remit_acts` is rewritten in place and nothing else is touched (the precondition
    refused any other difference). It earns `remit.changed` only if the remit actually moved.

    G4 -- WHAT IT NAMES: THE OFFICE (whole, as the content hash sees it) earning `office.established`
    or `remit.changed`, then every live `hold` on it earning `tenure.payload_set` -- the order the
    old mapping reported. THE GATE NOW DECIDES WHAT THIS EFFECT USED TO DECIDE BY HAND: the old
    body compared the remits itself (`moved`) and read `_grant_remit`'s boolean to filter which
    holds it reported, two private answers to *did this write happen*. Both are the gate's before-
    and-after now: an equal remit leaves the office's digest where it was (no `remit.changed`), a
    hold already carrying this grant is not in the tenure diff (no `tenure.payload_set`), and an
    establish that moves neither is `NoOpReceipt` -> `establish.refused`, as it was.

    ⚠ THE RE-STAMP, AND WHY IT IS HERE AND ROUTED THROUGH `_grant_remit`. The grant on a `hold` is
    a SNAPSHOT (`Tenure.granted_acts`): a hand-mutation of `w.offices[x].remit_acts` reaches no
    sitting holder. The act that changes a remit re-stamps them, so the grant still changes only
    by an act while sitting holders are reached -- and a `hold` opened on this id before the office
    existed, which `_grant_remit` traced and stamped nothing for, gets its grant now. `force=True`
    is `_grant_remit`'s own overwrite, so the payload key keeps ONE writer (`CLAUDE.md` §8).
    `tenure.payload_set` is earned only by a Tenure whose payload was actually written, so an
    establish with no sitting holder -- or one whose holders already carry this grant -- does not
    publish it.

    ⚠ G3 -- THE RE-STAMP WRITES A SITTING HOLDER'S EDGE, AND IT IS DECLARED. A `hold` is its
    holder's (S15.1), so re-writing its grant is a Tenure write by a non-owner -- a fourth live one
    beside `revoke`, `confer` and `kill / wound`, which G3's plan text did not list. The gate admits
    it under the CONFERRAL basis (the seat exercised may fill this office, so it may re-grant it);
    `_req_establish`'s clause 5 asks that first. ⚠ *"or `T-m` for the actor's own `hold`"* STOOD
    HERE AND IS FALSE SINCE G3's OWN ANTAGONIST FIX: `T-m` never admits re-granting a seat-hold,
    not even the actor's own (`state/gate.py::tenure_write_basis`) -- a sole holder re-stamping
    his own seat is exactly the exploit that fix closed. Corrected at G4, which rewrote this body."""
    off = office_described_by(a)
    if off is None:
        return NO_CHANGE
    cur = w.offices.get(off.id)
    holds = [t for t in w.tenures if t.kind == "hold" and t.object == off.id and t.live]

    def perform() -> None:
        if cur is None:
            w.offices[off.id] = off
        else:
            cur.remit_acts = list(off.remit_acts)
        for t in holds:
            w._grant_remit(t, force=True)
    return Change(
        (Subject.entity("offices", off.id,
                        "office.established" if cur is None else "remit.changed"),)
        + tuple(Subject.edge(t, "tenure.payload_set") for t in holds), perform)


@effect_for("release")
def _eff_release(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """`04 §A.3` row 14's generic closer: the actor ends a live edge they own.

    THE MIRROR OF EVERY OPENER AT ONCE, which is the point -- `04 §A.3` row 14 replaces *four
    closing verbs missing* with one, so `oblige`, `commit`, `tie`, `knot`, `succeed` and `hold`
    all end here rather than growing an antonym apiece. `01_AXIOMS.md:1121-1136` refuses the
    per-verb framing by name: *"Asking which verb ends an `oblige` is the wrong question… one
    sentence rather than four verbs."*

    ⚠ **A PERSON CAN NOW RESIGN AN OFFICE, AND THAT WAS A `T-m` VIOLATION IN THE TABLE, NOT THE
    DESIGN.** `hold` was closable only by `revoke`, which is `remit:revoke` -- so a seat could be
    taken from someone and never laid down. `registers/handoffs/architecture_meta_HANDOFF_NEXT.md` §2a: *"The design
    says a person may resign; the verb table does not let them. Fix the table, and do not re-open
    the design."* `hold` is in the domain for exactly this reason.

    ⚠ NO `w.write` HERE, AND NOTHING TO RELEASE IS A REFUSAL, NOT A RAISE (§E2: *failure emits,
    never raises*). Before G4 an empty returned list was how the fold learned nothing was closed;
    now the `Change` names no edge, the gate finds nothing moved, and `NoOpReceipt` is what emits
    `release.refused` -- the same refusal, through the one channel every effect shares.

    G4 -- WHAT IT NAMES: each live releasable edge the actor owns on `subject`, as an `edge`
    subject; the whole of what it writes. A closure always moves `until` (live means `until is
    None`), so a release that finds an edge is never a no-op, and one that finds none always is.

    ⚠ G3: `T-m` BY CONSTRUCTION, CONFIRMED RATHER THAN ASSUMED. The scan below closes only edges
    whose `subject` is the actor, so every write it makes is the owner's own and the gate admits it
    with no seat (`via=None`). `test_g3_release_is_the_owners_discretion_and_the_owners_only`
    observes both halves: the release admitted, and a write by the same actor on another's edge
    refused."""
    subj = _operand(a, "subject")
    edges = [t for t in w.tenures
             if (t.subject == a.actor and t.object == subj
                 and t.kind in RELEASABLE_KINDS and t.live)]
    return _closing(w, edges)


@effect_for("revoke")
def _eff_revoke(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """Unseats an office: the live `hold` closes. The mirror of `confer`, which is why the two are
    the pair that proves the slice — one opens what the other closes, on the same row.

    G4 -- WHAT IT NAMES: every live `hold` on the office, as an `edge` subject -- exactly what it
    closes and what it always reported. An office nobody holds names nothing, and the gate's
    `NoOpReceipt` emits `revoke.refused` where the empty list used to.

    ⚠ G3: A `T-o` WRITE, AND `via` MUST BE PRESENT. The `hold` it closes is the incumbent's, so the
    write gate admits it only as `04 §C.2`'s third clause -- `Act.via` names a seat the actor sits
    in, and the target seat's revocation basis (ruling (3), `rung_above_same_faction`) admits THAT
    seat -- or `T-m` if the incumbent is the actor. A revocation with no seat is refused at the gate
    and the hold put back; `_req_revoke` asks the same `may_revoke` first. ⚠ F3 IS ASKED BEFORE F9,
    so a seatless revocation is `NotYours` -- never excused as a no-op."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    obj = d.get("office")
    return _closing(w, [t for t in w.tenures if t.kind == "hold" and t.object == obj and t.live])


def _closing(w: "World", edges: list) -> Change:
    """`release` and `revoke`'s one write: close these edges at this tick, each named as an `edge`
    subject earning every kind the row declares (`tenure.closed`, on both rows). One body because
    it is one write; the two effects differ only in WHICH edges, which is the whole of each."""
    def perform() -> None:
        for t in edges:
            t.until = w.tick
    return Change(tuple(Subject.edge(t) for t in edges), perform)


@effect_for("convene")
def _eff_convene(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """Schedules a sitting: a Date comes due, with a ConveningCondition attached — Part E's two
    writes, both done by this one effect because the fold calls it once for the row.

    ⚠ A DATE IS A DICT HERE, not a class: `w.dates` is read as `d.get("due_at")` / `d.get("fired")`
    at CALENDAR. The first version built a `Date(...)` that does not exist.

    ⚠ WHAT THE SITTING THEN DECIDES IS `H-32` AND IS NOT HERE. `convene` puts a date on the
    calendar and stops, which is `L5`: a clock may not produce an outcome. `W7` is the item that
    makes the sitting decide.

    G4 -- WHAT IT NAMES: THE DATE, whole. Its id is `H(seed, tick, actor, venue)`, so a SECOND
    identical convening by the same person at the same venue in the same season finds the date
    already due when it says and already attached -- it moves nothing, and is now
    `convene.refused` where it used to publish a second `date.scheduled` for a date that was
    scheduled once. A different `when` moves `due_at` and is a real reschedule. Measured before
    this position on `build_realm(0)`: no convening in four seasons repeats one, so no run moves.

    ⚠ THE VENUE RIDES `subject` NOW, NOT `venue` (plan position `18`/PROC-A, 2026-09-29; C-11,
    `21_RECONCILIATION.md:379`: *"subject already binds the rung"*). `w.dates[...]["venue"]` is
    the DATE'S own field name, unrelated to and unchanged by the act's payload key, and
    `corpus_run.py`'s hand-built dates still set it directly."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    when = int(d.get("when", w.tick + 1))
    venue = d.get("subject")
    did = H(w.world_seed, w.tick, a.actor, f"convene:{venue or '-'}")

    def perform() -> None:
        date = w.dates.setdefault(did, {"id": did, "venue": venue})
        date["due_at"] = when
        date["convening_attached"] = True
    return Change((Subject.entity("dates", did),), perform)


def _decline_ascent(msg: str) -> Change:
    """The shared §10-ladder refusal: `move`, `migrate` and `found` each require their
    destination/parent to ascend the containment ladder and decline identically when it does not
    -- one owner for the `chose`/`alternatives` pair rather than a third hand-copy of it
    (`/simplify`, BATCH-CLOSE Phase 2). Callers still build their own message, since what "not up
    the ladder" names differs (a destination for `move`/`migrate`, a parent rung for `found`)."""
    TRACE.decision(msg, "S10/E3", chose="change nothing, so the fold emits the refusal",
                   alternatives=["write the edge anyway (add_tenure raises and the season "
                                 "dies)", "let the precondition admit it and crash later"])
    return NO_CHANGE


@effect_for("move")
def _eff_move(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§D4 / #353 §15.1: travel is a TENURE ALTER, owned by the traveller as the Tenure's subject.
    The old leg closes and a new one opens; the destination rides on the payload where the act
    names one. ⚠ This is `H-63`: Part E's `writes:` names the three cells and never the values, so
    what a `move` DOES is stated here rather than in the table — one implementation owned by the
    resolver, which is the distinction §27.2 draws against a caller-supplied lambda.

    G4 -- WHAT IT NAMES: THE TRAVELLER, WHOLE -- and only the traveller, which is what it always
    reported. That is not an omission of the legs: a `contain` leg is owned by its subject and
    stored on the Person (S15.1), so the Person's digest -- the string the content hash folds for
    them -- carries the legs AND `travel_leg`, and a move moves it. Naming the two legs as well
    would put two receipts on every `travel.moved` that has always carried one, which moves a hash
    for a reason that is not a no-op. A traveller who is not a Person (a hand-built act; RESOLVE
    never folds one, `act.ineligible` stops it first) names an absent subject that stays absent,
    so the move is refused and the legs it opened are put back -- where before G4 it published
    `travel.moved` about a mover that does not exist."""
    dest = _operand(a, "to")
    # ⚠ THE GUARD MOVED TO `_operand` AND ITS HISTORY IS KEPT HERE, because the history is what
    # makes the guard's shape legible. Rev 1 fell through on a missing destination, closed every
    # live leg and STILL returned `[a.actor]`, so `_fold` saw a non-empty `changed` and published
    # `travel.moved` for a move that did not happen. Returning `[]` would be quieter and just as
    # wrong: the caller would report a no-op as a legitimate nothing. §42.2's polarity rule -- no
    # destination is a refusal, never a silent success. The version of this guard that lived here
    # was found to pass `needs=`/`law=` to `InstrumentDefect`, which takes no keywords, so it
    # would have raised `TypeError` if it had ever fired -- a guard that crashes instead of
    # reporting, unfired because the precondition refuses first. One owner is also one place for
    # that mistake to be made.
    # ⚠ A DESTINATION THE LADDER WILL NOT SEAT THE MOVER IN IS A BLOCKED TRAVEL, NOT A CRASH, and
    # this branch is `W-C`'s doing: once `move` carries a real `to`, a person can name any rung
    # their containment path reaches, and `contain.path` asks for a SHARED ANCESTOR -- which a
    # sibling has. So `move p_low -> p_mid` passed the precondition, `add_tenure` raised
    # `Forbidden` on the §10 ladder, and the season died. Declining here returns nothing changed,
    # so the fold emits `move`'s own `emits_on_refusal`. The rule itself is not re-implemented:
    # `World.contain_ascends` is the one owner and `add_tenure` still RAISES on it, because a
    # caller writing the edge directly is a bug where a person attempting the journey is not.
    if not w.contain_ascends(a.actor, dest):
        # ⚠ THE INSTANCE DETAIL SITS AFTER ` -> `, WHICH IS `report.py`'s CLUSTER KEY
        # (`d.what.split(" -> ")[0]`). Putting the actor and the destination in the prefix would
        # mint one register entry per pair and leave the label reading mid-sentence.
        return _decline_ascent(
            f"a move's destination is not up the §10 ladder -> {a.actor} into {dest!r}")
    # ⚠ PLAN POSITION `19c`: WHAT A `move` LEAVES BEHIND IS THE MOVER'S `reside` EDGE -- it is not
    # touched here, so a traveller still lives where he lived (`_eff_migrate`'s docstring).
    return Change((Subject.entity("persons", a.actor),), lambda: _relocate(w, a, dest))


def _relocate(w: "World", a: "Act", dest: str) -> None:
    """THE JOURNEY, `move`'s and `migrate`'s one body: the actor's live `contain` legs close, a new
    one opens to `dest`, and `dest` is appended to `Person.travel_leg` -- the movement in progress
    (`ARCHITECTURE_V2.md` §D4) that `loop/matter.py`'s travel pass ends at the next MATTER. Called
    inside an effect's `perform`, so the gate observes every edge it writes. Extracted UNCHANGED from
    `_eff_move` at plan position `19c` because `migrate` is a journey too (a settler travels to his new
    home and pays the same distance penalty the season he goes), and a second copy of *what a journey
    writes* would let the two verbs disagree about it (§8). The leg's id is `move`'s, byte for byte,
    so every run that only moves is unmoved by the extraction."""
    for t in w.tenures:
        if t.subject == a.actor and t.kind == "contain" and t.until is None:
            t.until = w.tick
    w.add_tenure(Tenure(H(w.world_seed, w.tick, a.actor, f"leg:{a.id}"),
                        a.actor, dest, "contain", since=w.tick))
    # ⚠ THE DECLARED WRITE, NOW ACTUALLY WRITTEN. `verb_table.yaml`'s `move` row names
    # `(Person, travel_leg)` as its FIRST write and rev 1 never touched the field, so
    # `Query.budget`'s distance penalty read `len(p.travel_leg)` == 0 in every run and the only
    # test of it set the field by hand. A declared write that no effect performs is a lie the
    # write matrix cannot catch, because the matrix gates writes that HAPPEN.
    mover = w.persons.get(a.actor)
    if mover is not None:
        mover.travel_leg = list(mover.travel_leg) + [dest]


@effect_for("migrate")
def _eff_migrate(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """`RULINGS.yaml` RR-2 -- *"must be able to build hearths and accept people who move
    settlements"*; *"migration is a verb persons take"*. The migrant makes the journey (`_relocate`,
    `move`'s own body) AND settles at its end: his live `reside` edge closes and a new one opens to the
    destination, in one write.

    ⚠⚠ THE PRESENCE/RESIDENCE SPLIT, DECIDED HERE (plan position `19c`; `CLAUDE.md` §0 step 5 -- part
    1 `§5` routes it to architecture, not to Jordan). The tree had ONE edge for where you are and where
    you live, and `move` re-homed it. The split keeps `contain` as PRESENCE and adds `reside` as
    RESIDENCE, and `move` is defined by what it leaves behind: the `reside` edge.
      * WHY `contain` STAYS PRESENCE. It is ratified: `04_CODE_ARCHITECTURE.md` §B, *"LOCATION: ... its
        contain edge is where they are"*, and `ARCHITECTURE_V2.md` §D4, *"A person's location IS their
        contain Tenure"*. Every presence consumer reads it -- WITNESS's co-location, `share`, the larder
        ladder, `place_of` -- and `move` has executed as a re-homing across the corpus since `W-C`.
        Making `contain` the residence instead (and `travel_leg` the presence) reverses two ratified
        sentences and re-reads every one of those consumers.
      * WHY A TENURE AND NOT A CLAIM. The plan offered *"a WITNESS-side deposit rule or a Tenure kind"*.
        The throttle decides it: RR-2's capacity bounds POPULATION, the fold must count the people who
        LIVE under a rung, and the fold reads the world, never a ledger (AX-2, bar the actor's own). A
        residence held only in ledgers cannot be counted; a population counted by presence would make
        the throttle bypassable by one `move`, which reaches the same `contain` edge unthrottled.
      * WHY A TENURE AND NOT A `Person` FIELD. A person's relation to a place is an edge (`04` §B names
        LOCATION by its edge; `ID-2`, one home per fact), owned by its subject and judged by the gate's
        F3 like every other; `Person.marks`, which once listed *residence*, was deleted for having no
        reader or writer (`ED-IN-0261`). NOT a flag on `contain` either: `Tenure.payload` is the remit
        grant's (`H-71`), and the home edge ENDS when its owner travels, so residence would be read off
        an ended edge.
      * WHY EVERY BUILDER MINTS ONE, rather than residence defaulting to presence for a person with no
        `reside`. With the default, every writer of `contain` would be a silent writer of residence
        (`CLAUDE.md` §0.1 pt 1), and the next effect that re-homes a person would re-home his house.
        So `world_q.residence_of` reads one edge kind and nothing else.
    `move`, `migrate` and MATTER then state the whole of the split: a `move` re-homes `contain` and
    leaves `reside`; a `migrate` re-homes both; neither is a return, and a leg ends at MATTER either way.

    G3 -- EVERY EDGE IS THE ACTOR'S OWN (`T-m`): the `contain` legs and the `reside` edges are the
    migrant's, as subject, so the gate admits all four writes with no seat and NO NEW BASIS -- checked
    against `tenure_write_basis`'s nine rather than assumed: the closures are the owner's discretion,
    and an opening whose subject is the actor is `T-m`'s own case (it excludes only a SEAT-hold).

    G4 -- WHAT IT NAMES: THE MIGRANT, WHOLE, `move`'s reason: both edges are stored on the Person, so
    his digest carries them and his `travel_leg`, and one receipt says a migration happened.

    DECLINES (`NO_CHANGE` -> the `write` clause's `migrate.refused`):
      * a destination the §10 ladder will not seat him in (`move`'s decline, the same owner);
      * a destination he ALREADY LIVES IN -- a migration that changes no residence is none, and
        re-opening the same residence under a new id would be a digest move F9 publishes as a
        migration (`H-140`'s shape, answered for this verb rather than left open);
      * A DESTINATION AT CAPACITY -- RR-2's throttle, and `capacity`'s first caller (plan `24d-ii`,
        which lands here). A NEWCOMER is refused where `population(dest) + his weight` would pass
        `capacity(dest)`; the refusal is the destination's, read at the destination only, as the
        plan instructs (*"throttled by `capacity` at the destination"*). A migrant who ALREADY lives
        under `dest` (settling from his hearth into its settlement) is no newcomer to it: he is in
        its population before and after, so the move grows nothing and nothing throttles it.
        REJECTED: checking every ancestor too -- a newcomer to a hearth is a newcomer to its
        settlement, but a settlement's room is its hearths' room summed, and refusing a hearth
        with space because the town above is crowded would make the throttle a second, coarser
        census the ruling did not ask for; and throttling a `move` -- presence fills no house.
    REJECTED: settling without travelling (no leg) -- a settler makes the journey a traveller makes,
    and the distance penalty is the journey's, so two verbs pricing one journey two ways would be the
    S defect (*calculations consistent in methodology*)."""
    dest = _operand(a, "to")
    if not w.contain_ascends(a.actor, dest):
        return _decline_ascent(
            f"a migration's destination is not up the §10 ladder -> {a.actor} into {dest!r}")
    residence = residence_of(w)
    home = residence.get(a.actor)
    if home == dest:
        TRACE.decision(f"a migration to where the migrant already lives -> {a.actor} into {dest!r}",
                       "19c", chose="change nothing, so the fold emits the refusal",
                       alternatives=["re-open the same residence under a new id (a digest move "
                                     "published as a migration)", "treat it as a move"])
        return NO_CHANGE
    migrant = w.persons.get(a.actor)
    if migrant is None:
        # Not a person: `act.ineligible` stops it before the fold, so only a hand-built act lands
        # here, and it has no weight to house -- `move`'s reading of the same case.
        return NO_CHANGE
    newcomer = home is None or dest not in ancestry(w, home)
    if newcomer and population(w, dest, residence) + migrant.weight > capacity(w, dest):
        TRACE.decision(f"a migration into a rung at capacity -> {a.actor} into {dest!r}",
                       "RR-2/24d-ii", chose="change nothing, so the fold emits the refusal",
                       alternatives=["admit him anyway (capacity bounds nothing)",
                                     "refuse at every ancestor as well (a second, coarser census)"])
        return NO_CHANGE
    settled = [t for t in w.tenures if t.subject == a.actor and t.kind == RESIDE_KIND and t.live]

    def perform() -> None:
        _relocate(w, a, dest)
        for t in settled:
            t.until = w.tick
        w.add_tenure(Tenure(H(w.world_seed, w.tick, a.actor, f"reside:{a.id}"),
                            a.actor, dest, "reside", since=w.tick))
    return Change((Subject.entity("persons", a.actor),), perform)


@effect_for("work")
def _eff_work(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """`work` alters `(Site, condition)` by the act's declared delta. The DELTA IS NOT APPLIED
    HERE -- §27.3 sums every delta across the fold and clamps ONCE, so applying it per act would
    make the clamp arrival-order dependent, which §32 forbids. The write goes through the gate so
    the class and Partition are checked; the value lands in the accumulator.

    ⚠⚠ G4 -- THE ONE EFFECT WHOSE WRITE IS NOT WHERE ITS CHANGE IS, AND WHERE F9 IS JUDGED FOR IT.
    The plan's pre-flight named the trap: a gate that compares the SITE either side of this act's
    write sees no change BY CONSTRUCTION -- the site moves later, in `resolve()`'s one write per
    cell -- so `work` would be refused forever. So the change is judged TWICE, at the two writes
    that exist, each by the same before-and-after and neither by a rule of its own:

      1. HERE, PER ACT: the act STAGES its delta on the accumulator (`World.stage`), and the
         subject is that staged cell (`Subject.staged`). It moves iff the delta is non-zero -- an
         alter by zero stages nothing -- so a `work` declaring no delta, or a delta of 0, is
         `NoOpReceipt` -> `work.unavailable` at its own write. That is `H-94`'s worked case:
         `site.worked` over a repair nobody declared. The receipt still names the SITE, which is
         what the success Event has always carried (hash-identical where a real delta is staged).
      2. AT THE ACCUMULATOR, PER SITE: `resolve()` writes the clamped sum once, naming the Site, and
         the gate compares the site's condition either side. A clamp that eats the whole sum -- a
         site already at `condition_scale` being worked up, or two deltas cancelling -- moves
         nothing, and EVERY act that staged on that site is refused with it: their provisional
         `site.worked` is replaced in place by `work.unavailable` (`_refuse_after_the_fact`).

    WHY NOT JUDGE ONLY AT (2), the plan's candidate: an act with no delta stages nothing, so the
    accumulator would never learn of it and its `site.worked` would stand beside a site another
    act moved. WHY NOT ONLY AT (1): a per-act delta cannot see the clamp. The staged cell is not a
    parallel mechanism -- it is a store the gate reads like any other, which is why the gate needed
    no branch for `work`.

    ⚠ THE DELTA IS READ FROM THE ACT'S OWN DECLARED CHANGES, ON ITS OWN SITE, AND NOWHERE ELSE.
    Before G4 the accumulator summed every integer delta on ANY success Event's `changes[]` for ANY
    site -- so an act of a verb whose row writes no `Site.condition` could move a site by riding a
    delta on its Event, a write the matrix never saw declared. Now only an act whose row writes
    `Site.condition` stages -- `work`, and since plan position `24e` `restore` -- and only on the site
    it names. The DECLARED delta is unreachable from a computed act (none carries one: `H-94`).

    ⚠⚠ PLAN POSITION `24e` -- *"`work` advances `stage` (and inherits G4's accumulator answer)"* --
    AND WHAT THAT MEANS HERE, READ AGAINST THE CONTENT OWNER. A computed `work` carries no declared
    delta, so before `24e` it staged nothing and every one was `work.unavailable` (`H-105`: *"a loop
    with one arm cut is a RATCHET wearing a loop's clothes"*). It now has a SECOND source, used only
    when the act declares none: THE WORKS NAMING THE SITE. When a live works plans this site's kind
    at this site's rung (`queries/world_q.py::works_for`), the act stages `_rise` -- the headroom to
    the works' `ceiling`, shared among those standing at the fabric -- through the SAME accumulator,
    judged at the same two writes. So the works ADVANCES: each ripened term lifts the ceiling, and
    labour raises the fabric toward it. ⚠ NOT A `stage` KEY ADVANCED ON THE RECORD, which r2 `04`
    §A.6.1 RULED out on three grounds, the third decisive (*"progress is the condition and permission
    to progress is the ceiling, so nothing needs counting"*): `subject_matter` has no matrix row, so
    moving a stage there is an ungated write, and it would be a second progress ladder beside
    `Site.condition`. The stage a works has reached IS its fabric's condition against its ceiling.
    ⚠ AND NOT A THIRD FORMULA: `_rise` is `restore`'s own (`_eff_restore`), one owner for one
    quantity (§0.06 S: *"calculations consistent in methodology"*). What separates the two verbs is
    their preconditions, not their arithmetic -- `work` asks that the site clear its floor, `restore`
    that the actor stand at it -- and that `work` advances ONLY a works: a site no works names
    stages nothing from here, which is the position's control (*"a `text` Record is NOT advanced
    by `work`"*: a text Record has no `plan`, so it can never be the works a site is named by).
    REJECTED: summing the declared delta AND the works' rise -- one act would then move a fabric by
    two magnitudes from two owners, and the hand-built channel (`H-94`) would stop meaning what the
    act declared."""
    # ⚠ NO FALLBACK. This read `or next((x for x in sorted(w.sites)), None)` -- the alphabetically
    # FIRST site in the world -- so a `work` with no site named one nobody chose. `_eff_move`
    # refused the identical situation and this did not; found by the W-A adversarial pass, which
    # noted the two are the same defect one verb along. `W-C` gave that answer ONE owner
    # (`_operand`) rather than two copies of it.
    site = _operand(a, "site")
    site_deltas = tuple(c.delta for c in (a.changes or ())
                        if c.subject == site and c.field == "condition" and isinstance(c.delta, int))
    delta = sum(site_deltas)
    fabric = w.sites.get(site)
    # `not site_deltas`, NOT `not delta`: the fallback is for an act that declares NO delta on this
    # site, not for one that declares an explicit `0` -- the two read alike through `sum(())`,
    # `sum((0,))`, so testing the summed value would also replace a hand-built act's declared `0`
    # with the works' rise, which is not what "the act declares none" (above) says.
    if not site_deltas and fabric is not None and works_for(w, fabric.rung, fabric.kind):
        delta = _rise(w, fabric)
    cell = Subject.staged("Site", site, "condition")
    return Change((cell,), lambda: w.stage(cell.ref[1], a.id, delta))


def _rise(w: "World", site) -> int:
    """HOW FAR ONE ACT RAISES A FABRIC -- the ONE owner of `restore`'s formula, which `work` also
    reads when it advances a works (plan position `24e`). `verb_table.yaml`'s `restore` row:
    `Δ = +(1 − condition) × f(degree) × share` (§54 item 7's mirror), in fixed point:

      * `(1 − condition)` IS THE HEADROOM TO THE CEILING, `ceiling(w, site) − condition` -- r2 `04`
        §A.6.5's units decision (`condition` is an int on `condition_scale`, S48), bounded by the
        works (`queries/world_q.py::ceiling`, the full scale where no works names the site). Floored
        at 0: a fabric above its ceiling is not raised, and is not lowered here either.
      * `× share` IS `queries/world_q.py::share`, `(1, n)` for `n` persons standing at the fabric --
        r2 §A.6.4's commons: at a harbour forty stand at, one act moves a fortieth of the headroom.
        Multiply first, divide last, so the fraction is exact to the int.
      * ⚠ `× f(degree)` IS NOT BUILT, AND THE REASON IS THE FOLD'S, NOT THE FORMULA'S. r2 §A.6.5 reads
        it off `res.degree` (*"the existing degree ladder, not a new one"*), but `restore` and `work`
        are UNCONTESTED -- no `contests:` -- and `_fold` hands every such act `resolution=None`
        (*"`None` on every uncontested act, which is honest: no contest graded it"*), so r2's own
        body would raise on `None.degree`. The term is therefore the IDENTITY: an act no contest
        graded is taken whole. REJECTED: a fixture factor (an invented number standing where the
        design says a degree goes) and routing `restore` through a contest (a prize no subsystem
        claims, `rosters.yaml: contest_subsystems`). `H-164` carries the term, and the sweep r2
        declares for `share`.

    So the pace of a works is its TERMS (the ceiling) and its COMMONS (the share), never a rate:
    one hand alone at a fabric raises it to its ceiling in one act, and then nobody can raise it
    further until another term ripens -- r2 §A.6.6's TERM-STALL, arithmetic and not a cooldown."""
    headroom = max(0, ceiling(w, site) - site.condition)
    if not headroom:
        return 0
    num, den = share(w, site)
    return (headroom * num) // den


@effect_for("restore")
def _eff_restore(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `24e` -- `restore` RAISES A FABRIC. The row was TYPED (`verb_table.yaml`, W3's
    cell: *the site exists and the actor is present at it*) and had NO EFFECT, so
    `resolvable_verbs()` excluded it: `★` measured it formed 46 times in a populated season and
    offered never. r2 `04` §A.6.2's moment 4, *"BUILD IT UP"*, and §A.6.5's body, built as
    specified but for the degree term (`_rise` says why that is the identity).

    `work`'s ACCUMULATOR SHAPE, EXACTLY (G4, `_eff_work`'s docstring): the act STAGES its delta on
    `(Site, condition)` through `World.stage`, named as a `staged` subject, and `resolve()` sums every
    act's delta on the site and clamps ONCE, under the works' ceiling -- so two hands at one fabric
    commute and neither's delta is applied alone. It is judged twice, as `work` is: a delta of 0 (a
    fabric already at its ceiling -- *"you cannot hurry mortar"*) stages nothing and is
    `NoOpReceipt` -> `restore.refused` at its own write; a sum the clamp eats is refused after the
    fact (`loop/resolve.py::_refuse_after_the_fact`), which reads the row's refusal and so needed
    no line for `restore`.

    BUILDING AND REPAIRING ARE ONE ACT AT DIFFERENT BANDS (r2 §A.6.3's table, and its RULED
    heading): at a fabric no works names the ceiling is the full scale, so this repairs wear; at a
    works' fabric it raises the first courses as far as the ripened terms allow. No works is needed
    to restore, and no office: `own` admits and presence binds in the precondition, so *"a rival may
    finish what somebody else began"* (r2 §A.6.7) with no special case anywhere.

    DECLINES: a site that does not exist (a hand-built act that skipped the precondition) is
    `NO_CHANGE` -> `restore.refused`."""
    sid = _operand(a, "site")
    site = w.sites.get(sid)
    if site is None:
        return NO_CHANGE
    delta = _rise(w, site)
    cell = Subject.staged("Site", sid, "condition")
    return Change((cell,), lambda: w.stage(cell.ref[1], a.id, delta))


def _works_named(w: "World", a: "Act") -> tuple:
    """`(works, plan, rung)` -- the works the act names (its `subject`), what it plans, and the RUNG
    it plans it at -- or `(None, None, None)` if the subject is no works, or its `at` names no rung.
    `found`'s and `build`'s one reading of their operand: each then asks whether the plan is a kind
    IT makes. The precondition has already asked that the works exists and that the actor holds it
    (`verb_table.yaml`'s typed cells); this reads what the works SAYS, which no cell can.

    ⚠ THE MADE THING'S ID IS DERIVED FROM THE WORKS, NOT FROM THE TARGET (`_made_by`), so ONE works
    makes ONE thing: a second `found`/`build` from the same works finds its id taken and declines.
    r2's `f"{at}:{plan}"` is not taken -- it would collide across two successive works for one
    target (a second dwelling at one hearth, after the first works ended) and refuse the second as
    already made."""
    rec = w.records.get(_operand(a, "subject"))
    plan, at = works_target(rec.kind, rec.subject_matter) if rec is not None else (None, None)
    if plan is None or at not in w.rungs:
        return (None, None, None)
    return (rec, plan, w.rungs[at])


def _made_by(rec, plan: str) -> str:
    """The id of what the works `rec` makes -- `<plan>:<works id>`, readable in a trace as *the
    hearth of works rec:…*, and one owner for `found` and `build` (see `_works_named`)."""
    return f"{plan}:{rec.id}"


@effect_for("found")
def _eff_found(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `24e` -- A WORKS IS FOUNDED: a Rung of the works' `plan` kind is minted and
    placed in the rung its `at` names by a `contain` edge through `World.add_tenure`, the one
    writer, which enforces strict ascent. `ARCH` F.20 -- *"the world only decays -- nothing is ever
    founded or built"* -- is this effect's reason to exist, and `(Rung, exists)` its first producer
    (`H-41`'s first cell).

    WHAT IT MAKES, each choice with the reading it rejects:
      * A RUNG OF WHATEVER KIND THE WORKS PLANS, not a `hearth` written here. The plan's `24e`
        speaks of *"minting a `hearth` Rung"*, which is its example: a kind in a body is a
        definition the roster owns (`test_jordan_no_definition_is_hardcoded_in_a_body`), and strict
        ascent -- not a literal -- is what decides which kinds may be founded under which. A hearth
        under a settlement, a community under a territory; never a duchy under a hearth.
      * ITS PARENT IS THE WORKS' `at`, the one rung id the works carries. The act carries only its
        `subject` (the works) -- a person-side act can name no second rung (`H-94`), and `at` is
        not and must not become a `requires_operands` member (r2 `02`: *"I do not coin a ninth
        operand"*); `15c`'s reader left `found` exactly this place to read it from.
      * EMPTY: no stores, no sites, no holder. A founded hearth has no dwelling until one is BUILT
        (`build`, plan `24e`: *"A founded hearth has no dwelling until one is BUILT"*), and no
        `hold` is minted on it -- who holds a founded place is not this position's, and a `hold`
        written here would be a claim of ownership nobody made (`H-166`).
      * NO CAPACITY REFUSAL (the plan's CORRECTION of 2026-09-25, verbatim in substance): `found`
        and `build` are how capacity GROWS, and refusing a `found` at a rung at capacity would
        deadlock -- a full rung could never add the housing that raises its own ceiling. `found`
        keeps only its own preconditions (well-formed operands, the maker's standing, strict
        ascent). The refusal for a full rung is `19c`'s `migrate`'s.

    DECLINES (`NO_CHANGE` -> `found.refused`), each a clause the grammar cannot spell: the subject is
    no works or its `at` is no rung (`_works_named`); the plan is not a `rung_kinds` member (a works
    to build a Site is `build`'s); the works has already founded (`_made_by`'s id is taken); and the
    plan does not strictly ascend into `at` -- declined HERE, on `_eff_move`'s precedent, because
    `add_tenure` RAISES on it and a person attempting a founding the ladder will not seat is a
    refusal, not a crash. The rule is not re-implemented: `rung_kind_ascends` is the one owner
    `World.contain_ascends` reads too.

    G3 -- THE EDGE IS NOBODY'S, AND ITS BASIS IS `founding` (`state/gate.py`, the NINTH): a `contain`
    whose subject is a Rung is in no person's store (S15.1), so `T-m` cannot admit it; the gate
    admits it because the SAME write brought its subject into existence and it is that subject's only
    parent -- the mirror of `cascade`. Without it the gate raises `NotYours` and puts the edge back.

    G4 -- WHAT IT NAMES: THE RUNG, whole, earning `rung.founded` -- it always moves (absent ->
    present). The `contain` edge rides on the Rung's receipt as `create_record`'s maker's `hold`
    rides on the Record's (r2 §A.7.1: *"the `contain` edge rides inside `(Rung, exists)`"*), F3
    still judges it, and a refused write puts it back. The row declares `Tenure.since` beside
    `Rung.exists` all the same (`establish`'s `Tenure.payload` precedent: the fold gates exactly the
    pairs a verb declares), so the edge's pair is checked for class, step and partition."""
    rec, plan, parent = _works_named(w, a)
    if rec is None or plan not in RUNG_KINDS:
        return NO_CHANGE
    rid = _made_by(rec, plan)
    if rid in w.rungs:
        return NO_CHANGE
    if not rung_kind_ascends(plan, parent.kind):
        return _decline_ascent(
            f"a founding does not ascend the §10 ladder -> a {plan} under the "
            f"{parent.kind} {parent.id!r}")
    rung = Rung(rid, plan)
    placed = Tenure(H(w.world_seed, w.tick, rid, f"contain:{parent.id}:{a.id}"), rid, parent.id,
                    "contain", since=w.tick)

    def perform() -> None:
        w.rungs[rid] = rung
        w.add_tenure(placed)
    return Change((Subject.entity("rungs", rid, "rung.founded"),), perform)


@effect_for("build")
def _eff_build(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `24e` -- A WORKS IS BUILT: a Site of the works' `plan` kind (a `site_kinds`
    member) stands at the rung its `at` names, AT CONDITION 0. `(Site, exists)`'s first producer
    (`H-41`'s third cell) and the other half of `ARCH` F.20: *"nothing is ever founded OR BUILT"*.
    The plan's `24e`: *"A founded hearth has no dwelling until one is BUILT ... at runtime a
    dwelling exists because someone built it, which is what makes `found`/`build` the throttle"*.

    ⚠ AT CONDITION 0, AND THAT IS r2 `04` §A.7.1's DECISION, NOT A DEFAULT: *"a fabric that appeared
    at full condition would make `restore` pointless and would be a built thing nobody built.
    Condition 0 with a rising ceiling is 'raising the first courses'"*. So `build` stakes the
    fabric and `restore`/`work` raise it, as far as the SAME works' ripened terms allow -- the works
    names every `<plan>` at `<at>` (`queries/world_q.py::works_for`), so the Site it builds is the
    Site its `ceiling` bounds, with no second matching rule. A Site's yield scales with its
    condition (`loop/matter.py`), so a new producer produces nothing until it is raised.

    NO CAPACITY REFUSAL: building a dwelling at a full rung is how the rung's capacity grows (the
    plan's correction of 2026-09-25; `found`'s docstring). And NO EDGE: `Site.rung` is a field of the
    Site (S12), written in the same construction -- there is no Tenure to judge, so no gate basis is
    asked beyond the matrix row's own.

    DECLINES (`NO_CHANGE` -> `build.refused`): the subject is no works or its `at` is no rung
    (`_works_named`, `found`'s one reading); the plan is not a `site_kinds` member (a works to found
    a Rung is `found`'s); the works has already built (`_made_by`'s id is taken). ⚠ `site_kinds`
    CARRIES `body`, WHICH ITS OWN NOTE SAYS *"IS NOT A SITE"*: a works planning a `body` would build
    one. Refusing it here would be a kind literal in a body standing in for a roster defect; it is
    `H-166`'s, and no computed act can declare a works to reach it.

    G4 -- WHAT IT NAMES: THE SITE, whole, earning `site.built`; it always moves (absent -> present)."""
    rec, plan, rung = _works_named(w, a)
    if rec is None or plan not in SITE_KINDS:
        return NO_CHANGE
    sid = _made_by(rec, plan)
    if sid in w.sites:
        return NO_CHANGE
    site = Site(sid, rung.id, plan, condition=0)
    return Change((Subject.entity("sites", sid, "site.built"),),
                  lambda: w.sites.__setitem__(sid, site))


@effect_for("create_record")
def _eff_create_record(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3: `create_record` writes `(Record, exists)` and `(Record, stages)`. `H-63` is why the
    VALUES are here and not in the table.

    ⚠ THE STAGES COME FROM THE ACT, NOT FROM A DEFAULT. #353 `:1043` (§54 item 14) makes the
    stage list ACT-DECLARED -- "the act DECLARES the stages and their terms" -- so an act that
    names none creates a record with none, and the instrument does not invent a ladder. That is
    what makes Carin's season the case `PLAN.md` §6.1 chose: a Record with act-declared stages is
    the largest ruled row in the corpus and nothing about it needs a default.

    G4 -- WHAT IT NAMES: THE RECORD, whole -- what it always reported; the maker's `hold` is not
    named (a second receipt on every `record.created` would move every hash that has one). A new
    id always moves (absent -> present). The one no-op is an act naming an id that ALREADY holds
    an identical Record: the Record does not move, the gate refuses, and the `hold` the write
    opened beside it is PUT BACK with the refusal -- so the maker does not end up holding a second
    edge on a record the act did not make. A differing Record on an existing id is still an
    overwrite, as it was; whether a Record id may be re-made at all is not this position's to
    decide (`utter` refuses the same case for a Proposition by immutability, S14).

    ⚠ PLAN POSITION `15`: THE MINT MOVED INTO `_mint_document`, UNCHANGED, SO `issue` AND
    `petition` SHARE IT. What this verb adds is only its own reading of the act: the kind the act
    declares (else `text`), the content the act carries verbatim, and the rung the act names (else
    the actor -- r2 `02` §A.4 records that default as a defect and leaves it to `place_of`'s owner).
    MEASURED, WITH A CONTROL: on the finished position with `petition` withheld from the option set,
    `headless.run(3, 0)` and `populated.run(2, 0)` hash byte-identically to the tree before it -- the
    Record, the `hold` and the `Change` are built exactly as they were, and the one hash move the
    position makes is `petition` entering `resolvable_verbs()`.

    ⚠ PLAN POSITION `24e`: THIS IS THE `works`' PRODUCER, AND IT DECLINES A SECOND LIVE WORKS ON ONE
    TARGET. r2 `04` §A.6.2's moment 1 -- *"DECLARE the works: `create_record` -- exists, RUNS"* -- so
    the kind needed no new verb: an act declaring `kind: works` and `subject_matter: {plan, at}`
    mints one, with the maker's `hold` that makes him its master. The one thing added is r2 §A.6.3's
    *"one works per target"*: `queries/world_q.py::ceiling` cannot say which of two works bounds a
    fabric, so a works whose `(plan, at)` a live works already plans is `NO_CHANGE` -- the refusal
    the fold emits for any declined mint (`act.refused`, this row declaring no kind of its own;
    `F.20b`). r2 put the guard on `found` as a `cardinality` conjunct; see `works_for` for why it
    lives at the producer instead. Every other kind, and a computed act (which carries no payload
    and so always mints `text`), reads exactly as before -- no world built before `24e` holds a
    works, so no hash moves."""
    d = a.payload if isinstance(a.payload, dict) else {}
    kind = d.get("kind") or "text"
    plan, at = works_target(kind, d.get("subject_matter"))      # (None, None) for any other kind
    if works_for(w, at, plan):
        return NO_CHANGE
    return _mint_document(w, a, kind, d.get("subject_matter"), d.get("rung") or a.actor)


def _content_of(a: "Act", kind: str) -> Optional[dict]:
    """WHAT A DOCUMENT OF `kind` SAYS, READ OFF THE ACT THAT MINTS IT -- `None` for a kind with no
    keys (`text`), which is what every Record minted before `record_kinds` already carries.

    ONE RULE FOR EVERY KEY, AND THE RULE IS DATA (`rosters.yaml: record_kinds.content`): a key is
    read from the act's operand of the same name unless `read_from` names another (`terms` is the
    act's `subject` -- what the document is ABOUT). A source that is a `requires_operands` member
    goes through `_operand`, so a missing one is the caller defect it is everywhere else in this
    file; a source that is NOT an operand (`at`, r2 `02` §A.6's place of discharge, which the closed
    vocabulary cannot carry) is read as declared and may be absent. Nothing here names a kind's
    keys: they come from the roster the constructor refuses against, so the two cannot disagree."""
    keys = RECORD_KIND_KEYS[kind]
    if not keys:
        return None
    read_from = RECORD_CONTENT.get("read_from") or {}
    d = a.payload if isinstance(getattr(a, "payload", None), dict) else {}
    out = {}
    for key in keys:
        src = read_from.get(key, key)
        out[key] = _operand(a, src) if src in REQUIRES_OPERANDS else d.get(src)
    return out


def _addressed(content):
    """`content` with its addressee key (`record_kinds.content.addressee`) as an id LIST. The one
    owner of that shape: the mint stores it, and `_eff_petition` reads it before minting."""
    addr = RECORD_CONTENT.get("addressee")
    if not isinstance(content, dict) or content.get(addr) is None:
        return content
    v = content[addr]
    return {**content, addr: list(v) if isinstance(v, (list, tuple)) else [v]}


def _mint_document(w: "World", a: "Act", kind: str, content, rung: str) -> Change:
    """THE ONE MINT: a `Record` of `kind` saying `content`, drawn up at `rung`, and the maker's
    `hold` on it -- `create_record`, `issue` and `petition` are three readings of an act onto this
    body, which is r2 `02` §A.6's *one function, three registrations* with the kind supplied by the
    verb that knows it rather than by a table beside the effects (`OPENERS-DERIVE`'s precedent: the
    construction is the single owner of what a verb makes).

    ⚠ THE ADDRESSEE KEY IS STORED AS AN ID LIST, whatever the act carried (`record_kinds.content.
    addressee`, r2 §A.9.1), so a petition to one person and a writ to five executors spell the
    same key one way. The kind's KEY SET is not checked here: `Record.__post_init__` refuses a wrong one
    (⊕L35), before anything is written, and a refusal written twice is two rules."""
    d = a.payload if isinstance(a.payload, dict) else {}
    rid = d.get("record") or f"rec:{a.id}"
    content = _addressed(content)
    stages = list(d.get("stages") or [])
    if not stages:
        # `H-80`, DECLARED AND SWEPT. The act SHOULD declare these (#353 §13.1) and a computed
        # act cannot: §F1's Candidate is `(verb, subject, why)` with no operand channel. Refusing
        # instead would make `(Record, stages)` -- a Part D row -- unreachable from any person's
        # decision, so the honest form is §G's declare-default-sweep rather than either an
        # invention or a blocker. Each stage is `(due_tick, label, the act that wound the clock)`.
        n = w.fixtures.get("record_stages_default")
        term = w.fixtures.get("record_stage_term")
        stages = [(w.tick + (i + 1) * term, f"stage{i + 1}", a.id) for i in range(n)]
    rec = Record(rid, rung, kind, subject_matter=content, stages=stages)
    # S13: possession is a `hold` Tenure owned by the holder, never a field on the Record. The
    # maker holds what they made until they part with it.
    held = Tenure(H(w.world_seed, w.tick, a.actor, f"hold:{rid}"),
                  a.actor, rid, "hold", since=w.tick)

    def perform() -> None:
        w.records[rid] = rec
        w.add_tenure(held)
    return Change((Subject.entity("records", rid),), perform)


def _seat_rung(w: "World", a: "Act") -> str:
    """WHERE A SEAT-BORNE DOCUMENT IS DRAWN UP: the rung of the seat the act exercises (r2 `03`
    §A.10 -- *a seat-borne act draws on the SEAT's rung, and that is `Act.via`'s job*). `Record.rung`
    is required, so the answer is decided here rather than defaulted: the seat named by `Act.via`.
    A seat with no rung (an office-cluster, `rung? = null`, S6.2) has no place to draw a document up
    in -- and a hand-built act may name no seat at all -- and only then does the mint fall back to
    `create_record`'s own reading of the act, the one existing default rather than a new one.

    ⚠ FACTORED AT PLAN POSITION `19` OUT OF `_eff_issue`, WHERE IT WAS THREE INLINE LINES, BECAUSE
    `_eff_open_case` DRAWS ITS CASE FILE UP THE SAME WAY (§8). For both, the fallback is now
    unreachable from an ADMITTED act: each row's `purview` conjunct (`data/requires.py::Basis`)
    refuses a rungless seat -- a cluster seat has purview nowhere -- so a seat that reaches the
    mint always has a rung. It stays for the hand-built act that skips the precondition."""
    seat = w.offices.get(a.via) if a.via else None
    d = a.payload if isinstance(a.payload, dict) else {}
    return seat.rung if seat is not None and seat.rung is not None else (d.get("rung") or a.actor)


@effect_for("issue")
def _eff_issue(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§37.1: a DISPENSATION IS A `Record` OF KIND `dispensation`, minted with the issuer's `hold`
    -- r2 `02` §A.3's schema `{terms, to, at}`: the OUGHT it carries (the act's `subject`), the
    executors it names (`to`), and where it is discharged (`at`, absent unless declared).

    ⚠ REACHABLE SINCE PLAN POSITION `19`, WHICH GAVE `issue` ITS EVALUABLE CELL -- the executor
    exists and is a person, and the issuing seat's purview reaches him (`verb_table.yaml`'s `issue`
    row). Until then this docstring said *"NOTHING REACHES THIS YET"*: the prose `requires:` had no
    predicate, the fold raised before any effect ran, and `resolvable_verbs()` excluded the verb.
    This body is UNCHANGED by `19` but for the rung, factored into `_seat_rung` (`_eff_open_case`
    draws up the same way): the thing `15` built it to mint is what the precondition now admits.

    ⚠ A COMPUTED `issue` IS ADDRESSED TO WHAT IT IS ABOUT -- `terms` and `to` both bind the
    question's one referent (`H-94`'s single-referent limit), so its `terms` names the executor
    himself: a writ to a man about that man. `petition`'s row records the identical limit for the
    identical reason, and `15c`'s held-writ `to` is what separates the two when a person holds one."""
    return _mint_document(w, a, "dispensation", _content_of(a, "dispensation"), _seat_rung(w, a))


@effect_for("open_case")
def _eff_open_case(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `19` -- A CASE IS OPENED: the matter goes on the docket, and a case file is
    drawn up at the opening seat's rung. The plan's `19`: *"`open_case` gains `writes:
    DocketItem.matter` and the world reader a `docket` branch: a proceeding with zero authored acts
    needs somebody to have put the matter before the room, and no step did that."* CALENDAR forms
    docket SLOTS (`matter: None`, `loop/calendar.py`) and nothing ever filled one; this is the act
    that puts a matter before a bench, and `determine`'s docket conjunct is the act that needs it.

    WHAT IT WRITES, IN ONE `apply`:
      * THE CASE FILE -- `_mint_document`, the one mint (`create_record`/`issue`/`petition`'s), so
        the row's `Record.exists`/`Record.stages` are written exactly as `create_record` writes them:
        the act's declared stages, else `H-80`'s default (*"its typed cell declares stages, as
        `create_record`'s does"*). Kind `text`, with no content: a `case` kind with its own keys is
        a `record_kinds` member with no reader yet (that roster's own note: a kind lands WITH the
        reader that needs it), and the matter is carried where it is read -- on the docket.
      * THE DOCKET ITEM -- `{"date": None, "matter": <subject>}`, `World.docket`'s own shape, with
        no date because no sitting was convened for it (`convene`'s dates fire VACANT in every
        computed world: nothing sets a date's holder, so CALENDAR never forms a slot to fill).

    G4 -- WHAT IT NAMES: THE CASE FILE, whole, as `create_record` names its Record; it always moves
    (a new id). ⚠ THE DOCKET APPEND IS NOT A NAMED SUBJECT AND CANNOT BE ONE: `Subject`'s three shapes
    are an entity in a `_STATE_COLLECTIONS` member, an edge, and a staged cell, and `docket` is a
    SEQUENCE (`World._STATE_SEQUENCES`), which the gate has no `get()` for. So the append rides on
    the Record's receipt, the way `create_record`'s maker's `hold` does -- and, like that hold, a
    refused write would NOT put it back (the gate restores Tenures only). Two declines therefore come
    FIRST, before anything is built: a matter ALREADY on the docket (`docketed`, the one owner --
    it is before the room already, and a second item would let it be determined twice), and an act
    naming a case-file id that already exists (the only way the mint could be a no-op).

    Where it is drawn up: `_seat_rung`, as `issue`. `via.scope`'s purview reaching the matter is the
    row's precondition (`Basis`, `purview`), asked before this runs."""
    matter = _operand(a, "subject")
    d = a.payload if isinstance(a.payload, dict) else {}
    if docketed(w, matter) or d.get("record") in w.records:
        return NO_CHANGE
    made = _mint_document(w, a, "text", None, _seat_rung(w, a))
    item = {"date": None, "matter": matter}

    def perform() -> None:
        made.apply()
        w.docket.append(item)
    return Change(made.subjects, perform)


@effect_for("determine")
def _eff_determine(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `19` -- A DETERMINATION DISPOSES OF A MATTER: it binds the party to the bench,
    and takes the matter off the docket. `21_RECONCILIATION.md:575`, the plan's corrected observable:
    *"a determination opens the disposal Tenure on its subject via the seat"*.

    THE DISPOSAL TENURE, AND WHY IT IS THIS ONE -- each choice named with the reading it rejects:
      * KIND `oblige`. `arrangements.yaml`'s one seeded `disposes:` that is a Tenure kind is
        `arbitration`'s `oblige`; the other two dispose a `Record`. C-1 (`21_RECONCILIATION.md:167`,
        RULED A there): *"who owns the Tenure a determiner opens: its SUBJECT ... exactly `confer`,
        which opens a `hold` whose subject is the conferee"*, and its price, stated: *"the subject
        may `release` what the finding opened (T-m) ... a convict can discharge his own penance"* --
        `oblige` is in `release`'s domain, so that price is paid as ruled. The kind is a LITERAL
        here because `data/verbs.py::_derive_openers_from_effects` reads a `Tenure(...)` site's kind
        off its string literal (`_eff_commit`'s docstring records what factoring it cost), and
        that derivation is what `data/arrangements.py::arrangements_without_a_disposal_opener`
        (C-1's load check, REPORTED) reads: `arbitration` leaves that report with this line.
        REJECTED: a `hold` on a seat -- `04 §B.7`'s *"conferral: ... determine by <judging seats>"*,
        a determination FILLING a seat -- because a computed act carries one referent and that
        reading needs two (whom, and which seat): `confer`'s 100% refusal at `★` is that trap.
      * OWNED BY THE SUBJECT, the party the matter names -- C-1's owner, and `_eff_oblige`'s edge
        shape exactly (`subject` a person, `object` a seat).
      * ON THE SEAT EXERCISED (`via`) -- *"via the seat"*: the party is bound to the bench that bound
        him, and so joins its `establishment_of` like any obligee. REJECTED: the seat that opened
        the case -- the docket item does not record it, and adding a key nobody else reads would be
        a field for one reader.
      * CARRYING `_eff_oblige`'s TERM (`oblige_term`, `H-159`), declared by THIS act (T-n: *"the
        opening act declares the terms"*), so a disposal lapses at MATTER like any unpaid service,
        citing the determination that wound it (AX-5). `None` (the control) opens it with none.
      * NO `degree`. The row wrote `Tenure.degree` and nothing ever did; an UNCONTESTED act carries
        no degree -- `loop/resolve.py::_fold`'s own rule, *"`None` on every uncontested act, which is
        honest: no contest graded it"*. A graded disposal is the CONTESTED determination
        (`04_VERBS.md` §B.2's degree-keyed row, PHASE 2 steps 13-15), `H-162`'s.

    AND IT TAKES THE MATTER OFF THE DOCKET: every item naming the party is written back to
    `matter: None` -- the row's `DocketItem.matter` -- so the slot a sitting formed survives and the
    matter leaves it. That is what makes a second determination of one matter in one fold REFUSE
    (the docket conjunct reads 0), §27.1's scarcity on a docket as `levy`'s is on a larder.

    TWO DECLINES (`NO_CHANGE` -> `determine.refused` on the `write` clause), both NEGATIONS the
    grammar cannot spell: the party already owes this seat a live `oblige` (one edge per person and
    seat -- `_req_oblige` clause 4's rule; a second would list him twice in `establishment_of`), and
    the party is the actor (a judge does not bind himself; `may_determine` refuses it too).

    G3 -- THE EDGE IS SOMEBODY ELSE'S, AND ITS BASIS IS `determination` (`state/gate.py::
    may_determine`, the EIGHTH): a judging seat the actor sits in, whose bench's ground holds the
    party's home. The row's `bench` conjunct asks that same function first, so the fold refuses (and
    emits) before this runs rather than meeting `NotYours` here. ⚠ The docket write is not a Tenure
    and the gate does not restore it: were the gate ever to refuse this write, the matter would be
    off the docket with no edge opened. The shared predicate is what keeps that unreachable.

    G4 -- WHAT IT NAMES: THE EDGE, which always moves (absent -> present)."""
    party, seat = _operand(a, "subject"), a.via
    if (seat is None or party == a.actor
            or any(t.kind == "oblige" and t.subject == party and t.object == seat and t.live
                   for t in w.tenures)):
        return NO_CHANGE
    nt = Tenure(H(w.world_seed, w.tick, party, f"oblige:{seat}:{a.id}"), party, seat, "oblige",
                since=w.tick, term=_new_oblige_term(w, a))
    items = docketed(w, party)

    def perform() -> None:
        w.add_tenure(nt)
        for item in items:
            item["matter"] = None
    return Change((Subject.edge(nt),), perform)


@effect_for("petition")
def _eff_petition(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§36.1 / #353 §26.3: A PETITION IS A `Record` OF KIND `petition`, minted with the
    petitioner's `hold` -- `{terms, to, from}`: what it is about (the act's `subject`), the person
    it is addressed to (`to`), and the place it rises from (`from`). Drawn up where it rises from,
    so `Record.rung` is a place and not the petitioner's id (the defect r2 `02` §A.4 measured on
    every `create_record`).

    ⚠ TWO-SIDED (`ED-IN-0210` ruling 2 -- *withdraw (petitioner) or deny (receiver)*): the row's
    typed cell makes both sides EXIST, `opening_set` never forms a Candidate addressed to its own
    petitioner (the row's `counterparty:`), and this body refuses the same case for a HAND-BUILT act,
    which no person-side rule stands in front of. The grammar has no negation, so it is decided
    here, and the fold emits `petition.refused` through the gate's no-op channel (`NO_CHANGE`) --
    how every effect in this file declines. ⚠ WHAT THIS DOES NOT BUILD: the two closers. Ruling 2's
    WITHDRAW and DENY both close `(Record, exists)`, whose one closer is `destroy_record` -- which
    declines on both its eligibility alternatives today (`H-75`), and which the receiver can only
    reach once `give` (position `16`) puts the petition in his hand. The fold makes both sides
    NAMEABLE on the document; neither side can yet end it."""
    content = _addressed(_content_of(a, "petition"))
    if a.actor in content[RECORD_CONTENT.get("addressee")]:
        return NO_CHANGE
    return _mint_document(w, a, "petition", content, _operand(a, "from"))


@effect_for("survey")
def _eff_survey(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `20-iii` -- THE INFORMATION CLUSTER (narrative #14 §F; `D1-a` of
    `proposals/2026-09-27-mc-v18-retirement-plan/PROPOSAL.md`: *"A Record whose `subject_matter` is a
    frozen `faction_q.resolve(...)` snapshot, commissioned by an act, read free by holders, forgeable
    and destructible"*). A SURVEY IS COMMISSIONED: a `Record` of kind `faction_q.SHEET_KIND` whose
    content is `faction_q.resolve`'s five-field view of one faction, RESOLVED AT THE MOMENT OF WRITING,
    minted through `_mint_document` -- the one mint -- with the surveyor's `hold`. Proposal 14
    (`proposals/2026-09-12-emergent-narrative-primitives-v2/01_THE_TEN.md`): *"a faction sheet is
    those Queries, resolved at the moment of writing and frozen into a `Record`"*; and the attack it
    survived, which is why an act is spent here and nowhere else: *"The cost belongs to COMMISSIONING
    ... Free to read, costly to obtain, stale by construction."*

    WHICH FACTION -- `world_q.faction_holding(w, subject)`, THE ONE OWNER OF *which faction does this
    cohere under*. It answers for a faction's own Proposition (itself, if the roster carries it) and
    for a person (the one faction he is committed to; `None` for none or for two, where canon states
    no precedence). So the literal reading -- survey the Crown -- and the reachable one -- survey the
    faction of the man you were asked about -- are ONE read, and no referent-to-faction rule is
    written here. REJECTED, each with its reason:
      * THE SUBJECT IS THE FACTION AND NOTHING ELSE (`commit`'s cell, `existence` of `subject`, kind
        `Proposition`). No computed act's referent is ever a Proposition -- `questions_for`'s clause
        1 admits a claim only if its subject is in the asker's `reach`, and `place_of` of a
        Proposition is `None` (BO-9/BO-10's gap; `commit` MEASURED refused 33 of 33 in one realm
        season, `python -m engine.season.harness.aperture`) -- so a survey would be formed on every
        referent and refused on every one: a fourth instance of `H-156`'s scene tax, and a
        mechanism that runs in no shipped world.
      * `holder_faction_of` FOR A RUNG (*who holds this valley*): a second derivation beside the
        first, for a document the position does not name. A rung referent declines.
      * `create_record` DECLARING `kind: faction_sheet` (`works`' route at `24e`). Three reasons,
        any one sufficient. (a) A sheet's content is RESOLVED, and `create_record` stores what the
        act carries VERBATIM (r2 `02` §A.4, *verbatim or not at all*): a sheet whose maker supplies
        its content is a forgery by construction, and teaching `create_record` to resolve for one
        kind is a kind-keyed branch changing what a generic verb means. (b) A COMPUTED
        `create_record` carries nothing -- the row is untyped, so `operands_for` returns `{}` -- and
        could never say WHICH faction; it mints `text`, as it does 46 times a realm season. (c)
        `issue`'s and `petition`'s precedent: one mint, the kind supplied by the verb that knows it
        (r2 `02` §A.6's *one function, several registrations*).

    WHAT IT WRITES -- `asdict(faction_q.resolve(...))`: a fresh mapping of fresh lists, so nothing
    done to the world afterwards reaches the document (and `loop/witness.py::content_value` freezes it
    again, as tuples, for a holder's ledger). The keys are `Faction`'s fields, which `faction_q.py`
    checks against `rosters.yaml: record_kinds` at import. No date is written into it: the
    document-side date proposal 14 asks for (*"dated"*) has no key -- `at` is a PLACE in every kind
    that has it -- and is `H-169`'s; a holder's belief carries its own `when`.
    WHERE IT IS DRAWN UP -- where the surveyor stands, `world_q.place_of(actor)`, the one owner of
    *the rung a thing is at* (`give`'s reading of the same person). ⚠ NOT `create_record`'s default,
    the actor's own id, which r2 `02` §A.4 records as a defect; that default is kept only for an actor
    standing nowhere, where there is no rung to name.

    DECLINES (`NO_CHANGE` -> `survey.refused`, the `write` clause): the subject coheres under no single
    faction -- a person committed to none or to two, a rung, a site, a document, an unrostered
    Proposition. The cell has already asked that the surveyor has heard of the subject (`own_ledger`).

    ⚠ WHAT THIS DOES NOT BUILD, each registered (`H-169`): proposal 14.1's bound -- *what the sheet
    can contain is bounded by who you have* (the seats you have filled) -- so every survey is
    complete and exact, and anyone may commission one; `forge` has no effect body, so no act makes a
    false sheet; `destroy_record` declines for every actor (`H-75`), so no act burns one.

    G3 -- THE `hold` IS THE SURVEYOR'S OWN, `T-m`, exactly `create_record`'s. G4 -- WHAT IT NAMES: THE
    RECORD, whole, earning `faction.surveyed`; a new id always moves (absent -> present)."""
    prop = faction_holding(w, _operand(a, "subject"))
    if prop is None:
        return NO_CHANGE
    sheet = asdict(faction_q.resolve(w, prop))
    return _mint_document(w, a, faction_q.SHEET_KIND, sheet, place_of(w, a.actor) or a.actor)


@effect_for("give")
def _eff_give(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """Plan position 16 (`H-84`): the actor's `hold` on the Record ENDS and the receiver's OPENS, in
    ONE write -- the first verb that moves a Record to another person.

    CLOSE, THEN OPEN, INSIDE ONE `apply`, AND THE ORDER IS THE GATE'S CONDITION RATHER THAN THIS
    BODY'S DISCIPLINE. The giver's close is `T-m`; the receiver's open is admitted only under the
    `handover` basis (`state/gate.py::tenure_write_basis`), which requires the actor to have ended
    their own live `hold` on the same object in the SAME write. So a `give` that forgot the release
    is `NotYours` with both edges put back -- `hold_force` never sees two holders -- and one that
    released in an earlier write finds no licence in this one.

    WHICH EDGE CLOSES: the ONE live `hold` on the Record, read through `hold_force` (the owner of
    *who holds this*, which raises on two rather than choosing), and only if it is the ACTOR's --
    `_eff_confer` closes every hold on its object because a conferral displaces the incumbent;
    a gift displaces nobody but the giver, and closing another person's edge here would be
    refused by the gate anyway. Anything else declines (`NO_CHANGE` -> `give.refused`). Whether the
    receiver may be given it at all (a person, not the giver, standing here) is `_req_give`'s, asked
    first; it is not asked twice.

    G4 -- WHAT IT NAMES: the two edges, OPENED FIRST as `_eff_confer` names them. Both are `edge`
    subjects the tenure diff judges, and both earn the row's one kind, `record.given`. The receipts
    therefore name TENURES, not the Record -- `_eff_confer`'s lesson on what a receipt may assert --
    and every reader that wants the Record goes through `epistemic._hold_tenure_ends`, which is
    `claim_subjects`' and `seen_subject`'s route and, since this position, WITNESS's deposit rule's.

    THE RECEIVER'S EDGE ID carries the act (`hold:<record>:<act>`): a Record handed A -> B -> A
    inside one tick would otherwise re-mint A's first `hold` id, and two Tenures sharing an id is
    what `World._tenure_changes` tolerates rather than wants."""
    rid, to = _operand(a, "subject"), _operand(a, "to")
    held = hold_force(w, rid) if rid in w.records else None
    if held is None or held.subject != a.actor:
        return NO_CHANGE
    nt = Tenure(H(w.world_seed, w.tick, to, f"hold:{rid}:{a.id}"), to, rid, "hold", since=w.tick)

    def perform() -> None:
        held.until = w.tick                # the giver's release, FIRST
        w.add_tenure(nt)                   # then the receiver's hold
    return Change((Subject.edge(nt), Subject.edge(held)), perform)


@effect_for("destroy_record")
def _eff_destroy_record(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3: writes `(Record, exists)`. The Record goes, and every `hold` on it ends -- S15.3's
    rule that a tenure dies THROUGH the death of what it is over, never beside it.

    G4 -- WHAT IT NAMES: THE RECORD, whose existence is the whole of the declared write; it always
    moves (present -> absent), so a destruction that finds its record is never a no-op and one that
    does not declines (`NO_CHANGE` -> `destroy.refused`, as the old `None` did). The closed holds
    are the cascade -- F3 admits each as `destroy's cascade` because this same write removed the
    id -- and are not named, as they were never reported."""
    d = a.payload if isinstance(a.payload, dict) else {}
    rid = d.get("record")
    if rid is None or rid not in w.records:
        return NO_CHANGE

    def perform() -> None:
        del w.records[rid]
        for t in w.tenures:
            if t.object == rid and t.live:
                t.until = w.tick
    return Change((Subject.entity("records", rid),), perform)


def _scar(w: "World", p, verb: str) -> None:
    """`(Person, scar[axis])` -- THE MORAL LAYER'S MISSING MOTION, §54 item 21.

    ⚠ THE FORM IS THE CHAIN'S OWN AMENDMENT, NOT THE SOURCE DOCUMENT'S, AND THE DIFFERENCE IS THE
    WHOLE REASON THIS SITS AT RESOLVE. `conviction_track_v1.md` §2 -- the mechanic's design home,
    quarantined and REFERENCE under §0.05 -- has an NPC *"accumulate Conviction Scars from
    WITNESSING morally-loading events"*. `holonic_ARCHITECTURE.md:1901` folds that in AMENDED and
    says why in as many words: *"the source says written at WITNESS, which breaks two things --
    the moral layer's WITNESS row is nothing, and a scar written there is an Event writing a
    `(Person, ...)` social row, which is L4. Lawful form: a `(Person, scar[axis])` row,
    `social: true`, written at RESOLVE in the ACTS class BY THE OUTCOME THAT NAMES THE PERSON."*
    S9.3 is the law underneath (*"WITNESS NEVER TOUCHES A BELIEF"*), so the design document's own
    trigger table is the one part of it that may not be implemented.

    ⚠ THE AXES COME FROM `ALIGNMENT`, WHICH ALREADY OWNS *which axes a verb engages*. §8: find the
    single-owner primitive and compose on it. A second table mapping outcome -> axis would be a
    second owner of the same claim, free to disagree with the one `choose` scores against -- and
    it would have to be AUTHORED, on a basis `STR-2` is about to replace. Reading `ALIGNMENT`
    keyed by the live axis roster means this survives that rename by never having known the old
    names. `axis` on L3's closed registry, as item 21 requires.

    ⚠ WHAT IS ASSUMED HERE AND IS NOT THE CHAIN'S, STATED SO IT CAN BE ATTACKED: that the depth of
    the moral wound is PROPORTIONAL to how strongly the verb engages the axis. Item 21 gives the
    row, the step, the class and the keying; it does not give a formula. The alternative -- a flat
    scar on every engaged axis -- is the arm a sweep would compare, and `scar_step` is where it
    would be run from.

    ⚠ AND WHO IS SCARRED IS THE SUBJECT, WHICH IS A READING OF *"the outcome that names the
    person"* AND NOT A CERTAINTY. The outcome of `kill / wound` names the person wounded, so the
    wound is theirs. The competing reading -- that the ACTOR carries the moral wound of having
    done it -- is at least as defensible on the mechanic's own *moral wound* framing, and nothing
    in item 21 settles it. Left as the open question rather than decided in silence."""
    step = w.fixtures.get("scar_step")
    if not step:
        # THE CONTROL ARM, AND IT RETURNS BEFORE TOUCHING THE CARRIER. A zero-depth scar written
        # as a 0.0 cell would still put a key on the field, and `_entity_digest` reprs every
        # field -- which is the difference between an arm that is inert and one that looks it.
        return None
    # ⚠⚠ `decision.align`, NOT A LOCAL `ALIGNMENT` READ, AND THE LOCAL READ WAS A REAL DEFECT
    # RATHER THAN A STYLE SLIP. This computed the cell inline off THIS module's own `ALIGNMENT`
    # binding. `align()` reads the binding in `decision/options.py`, which is the one the `H-66`
    # alignment sweep REBINDS (`decision.options.ALIGNMENT = alignment_at(point)`) -- so the
    # sweep moved `choose`'s scoring and could not move the scar at all. MEASURED before the
    # fix: under the `uniform` arm `align('kill / wound','sacred')` read 1.0 while `_scar`
    # still wrote 3.0 off the unrebound 0.3. The docstring above promises exactly what the inline read broke: no
    # second table free to disagree with the one `choose` scores against. One owner, §8, and the
    # sweep now reaches both readers.
    from ..decision import align
    # ⚠ SIGNED, AND THE `abs()` THAT STOOD HERE COLLAPSED A DISTINCTION THE READER NEEDS.
    # 17 of the 52 populated `ALIGNMENT` cells are NEGATIVE, so a verb that VIOLATES an axis and
    # one that UPHOLDS it cut an identical wound under `abs()`. It is invisible today only
    # because `kill / wound`'s one cell is `+0.3`; it bites the moment a negative-cell verb is
    # wired, and the scar's named reader -- the Conviction crisis -- is about the DIRECTION of
    # the wound. The magnitude keeps the cell's sign and `scar` is a signed accumulator.
    for axis in PURSUIT_AXES:
        weight = float(align(verb, axis))
        if weight:
            p.scar[axis] = round(p.scar.get(axis, 0.0) + step * weight, _SCAR_DP)
    # ⚠ SORTED ON WRITE, BECAUSE A DICT'S INSERTION ORDER REACHES `World.content_hash()`.
    # `_entity_digest` digests a dataclass as `repr(obj)`, and `repr` of a dict is
    # insertion-ordered -- so two people scarred by the same verbs in opposite ORDERS held equal
    # values and produced different digests. `_entity_digest` already `sorted()`s PLAIN dicts for
    # this exact reason (`world.py:141`), but a dict FIELD inside a dataclass never reaches that
    # branch. `A5`/`S32` assert the content hash is order-independent; that survived only while
    # this dict could hold one key. Re-inserting in sorted order makes the field carry its own
    # canonical form rather than relying on nobody scarring twice.
    if len(p.scar) > 1:
        p.scar = {k: p.scar[k] for k in sorted(p.scar)}


@effect_for("fight")  # RENAMED from "kill / wound", 2026-09-29 (plan `FIGHT-RENAME`) -- same
# effect, same body; only the `EFFECTS` dict key (and its `verb_table.yaml` row) moved.
def _eff_kill(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3: writes `(Person, body)`, `(Person, exists)` and `(Tenure, until)`.

    ⚠⚠ G4 -- WHAT IT NAMES, AND THE ONE EFFECT THAT NARROWS ITS SUBJECT TO A FIELD. The subject is
    the person wounded, read as PRESENCE and `body` (`fields=("body",)`) -- the two cells the
    band's own kinds name (`person.died` is existence, `body.changed` is body). THREE THINGS THE
    SAME WRITE DOES ARE DELIBERATELY NOT PART OF WHAT THE GATE JUDGES:
      * `scar`. It is written by the OUTCOME, whatever the body did -- the comment at `_scar`'s
        call below says why it was moved ahead of the magnitude model: so that sweeping `H-123`
        (`wound_harm_model`) does not also sweep whether `H-128`'s scar runs. Judging the whole
        Person would re-couple them the other way: at `scar_step > 0` the `none` arm -- `H-123`'s
        control, whose whole job is to emit the REFUSAL -- would start emitting `body.changed`
        for a body nothing touched, and the control would measure `scar_step`. So a wound that
        moves only the scar is refused, and the scar stands, exactly as the `none` arm always
        behaved. At the shipped `scar_step = 0` the two readings cannot differ.
      * the CASCADE (`remove_person`'s closures). A consequence of the existence change, which IS
        judged; F3 admits each closure as `destroy's cascade`; never reported, so never named. If
        existence did not move the cascade did not run.
      * the dead person's own `person`-kind rung, popped by the same owner -- the same reasoning.
    THE NEW NO-OP THIS MAKES VISIBLE: a `Wounded` outcome under `scene_fraction` whose fraction
    rounds back to the body it started from (`max(1, body * left // full)` at `body == 1`, or a
    scene that took no health) used to emit `body.changed` over an unchanged body and is now
    `kill.refused`. MEASURED BEFORE THIS POSITION on `build_realm(0)`, four seasons: every
    `kill / wound` that reached this effect moved its subject, so no run moves.

    ⚠ AND THE TWO `Unspecified` RAISES NOW COME BEFORE ANYTHING IS WRITTEN. The no-scene raise
    always did; the no-health-scale raise came AFTER `_scar` had written, so a season that died on
    it died with the scar already moved. Both are read while the `Change` is built, which touches
    nothing.

    ⚠ THE TENURE ENDS THROUGH THE DEATH, which is §15.3's rule and the reason this is ONE effect
    rather than three writes a caller sequences: "a plague that kills the praefect ends his
    tenure THROUGH THE DEATH; A STORM CANNOT TOUCH IT." A wound that does not kill writes only
    the band, so the same verb covers both -- which is why the table's row is `kill / wound`.

    ⚠ `W-E`, 2026-09-04. THE EFFECT NOW TAKES THE RESOLUTION, AND `harm` IS GONE. Register row
    `H-114` measured what the old signature cost: the effect could not honour the branch
    `writes_at` had just selected, and the payload's `harm` key was read with the person's ENTIRE
    body as its fallback -- so a fold at degree `Wounded` reached `p.body == 0`, passed
    `if p.body > 0`, and DELETED THE PERSON. Both halves are closed here, and the `W-C` carve-out
    that named `harm` as `W-E`'s to own is retired with its subject rather than widened.
    ⚠ THE OLD SPELLING IS DELIBERATELY NOT QUOTED IN THIS DOCSTRING. `W-C`'s guard
    (`test_wc_no_operand_is_defaulted_by_a_get_or_setdefault_in_shape_py_outside_eff_kill`) scans
    RAW SOURCE TEXT, so quoting the deleted line here would keep its carve-out "used" and leave
    an open licence on the name `harm` -- the exact staleness that test's own `used == EXEMPT`
    assertion exists to catch, satisfied by prose describing the defect rather than by the defect.
    Found while running that test against this change.

    WHERE THE MAGNITUDE COMES FROM NOW, AND WHY IT IS NOT INVENTED. JORDAN, 2026-09-04, VERBATIM:
    *"the combat engine determines the result there. your code just has to accept the result."*
    So the harm is not a number this file chooses: it is the LOSS THE SCENE ALREADY COMPUTED, on
    the engine's own `WoundTracker`, read as the fraction of the subject's health the fight left
    standing. No constant is introduced by the default arm -- a fraction needs none, which is
    exactly why it is the default and the other two arms are the sweep.

    THE THREE ARMS (`wound_harm_model`, registered at `H-123`, injected at `DEFAULT_FIXTURES`):
      `scene_fraction`  body <- body x health_remaining / health_full. The scene decides.
      `total`           any wound is lethal. ⚠ THIS IS THE CONTROL AND IT IS THE BEHAVIOUR THIS
                        FUNCTION HAD BEFORE `W-E` (`harm` defaulting to full body), so the arm
                        that shows what the degree is worth is the code as it stood.
      `none`            a wound writes nothing. The fold's own write-nothing guard then emits the
                        REFUSAL rather than the success -- the second control, and it isolates
                        "the band selected a different write set" from "the band changed a value".

    ⚠ AND THIS SUPERSEDES ONE HARNESS TECHNIQUE, WHICH IS SAID HERE SO ITS OUTPUT IS NOT
    MISREAD. `proposals/2026-09-04-degree-sweep/arm3_tree.py` injects a degree by monkeypatching
    `VerbRow.writes_at` / `emits_at` and then calls `_fold` bare. That reached the effect while
    the effect took no degree; it cannot now, because the degree travels on the `Resolution` the
    SEAM returns and a patched READER is invisible from here. Re-run after `W-E`, its `Felled` and
    `Wounded` nodes report REFUSED with the message below. That is the closure of `H-114` seen
    from the probe's side -- the probe measured a world in which the degree could not reach the
    effect -- and not a new defect.

    ⚠ A WOUND CANNOT KILL, AND THE FLOOR IS STRUCTURAL RATHER THAN NUMERIC. The `Wounded` band
    means the engine did NOT fell this person; a model that took their body to 0 would contradict
    the band it is implementing. `max(1, ...)` is `combat_seam.derive_party`'s own floor
    (*"a dying person still fights"*), followed rather than reinvented."""
    d = a.payload if isinstance(a.payload, dict) else {}
    who = d.get("subject")
    p = w.persons.get(who)
    if p is None:
        return NO_CHANGE
    # ⚠ NO SCENE, NO HARM -- AND THIS IS A REFUSAL TO INVENT, NOT A MISSING FEATURE. `kill / wound`
    # declares `contests: the body`, so the only lawful route into this effect is through the
    # seam; an act folded without one has no scene to read a severity off, and the pre-`W-E`
    # answer to that was to kill. `writes_at(None)` already refuses one line earlier for the same
    # reason, so this is the second gate on the same road rather than a new rule.
    if res is None or not isinstance(res.result, dict):
        raise Unspecified(
            f"`kill / wound` on {who!r} was folded with no scene to read a severity from",
            "S39.4/H-98",
            needs="a Resolution from `resolve()`'s seam branch -- the personal-combat scene",
            law="Jordan 2026-09-03 -- kill/wound degrees are taken directly from scene combat. A "
                "harm this function chose would be the number `H-114` measured: the old default "
                "was the person's whole body, so an act naming no harm killed")
    st = (res.result.get("wound_state") or {}).get(who) or {}
    model = w.fixtures.get("wound_harm_model")
    require_member(
        model,
        WOUND_HARM_MODELS,
        f"wound-harm model {model!r} is not in the roster",
        "H-123",
        law="`observers_for`'s precedent and its reason -- *an unrecognised mode silently "
            "falling back would make every measurement of this sweep read the control*")
    # ⚠⚠ THE SCAR RUNS BEFORE THE HARM-MODEL BRANCH, AND IT USED TO RUN AFTER IT -- WHICH
    # CONFOUNDED TWO INDEPENDENT SWEEPS. `wound_harm_model == "none"` returns early (it is
    # `H-123`'s control, the arm that isolates *the band selected a different write set* from
    # *the band changed a value*), so with the call below that `return` a `Wounded` outcome at
    # `scar_step=10` silently wrote NO scar while `verb_table.yaml` declared `Person.scar` for
    # that band unconditionally. Sweeping `H-123` therefore also swept whether `H-128`'s
    # mechanism ran at all, so neither row measured what it says it measures. The moral wound
    # is a consequence of the OUTCOME, not of how much body the scene took, so it belongs
    # ahead of the magnitude model entirely. (G4: it is still the first thing `perform` writes;
    # the magnitude below is COMPUTED first only because computing it writes nothing.)
    if res.degree == FELLED:
        # The scene says this person went down, and the table says that is the kill. The body
        # goes to 0 on every arm: the arms grade a WOUND, and a felling is not one.
        body = 0
    elif model == "none":
        body = None                             # the control arm: the body is not written
    elif model == "total":
        body = 0
    else:                                       # `scene_fraction`
        full = int(st.get("health_full") or 0)
        left = int(st.get("health_remaining") or 0)
        if full <= 0:
            raise Unspecified(
                f"the scene reports no health scale for {who!r} ({st!r})", "S39.4/H-123",
                needs="`health_full` on the subject's wound state",
                law="the magnitude is READ from the scene; a scene that carries none cannot be "
                    "read, and choosing a number here is what this arm exists not to do")
        body = max(1, p.body * max(0, left) // full)

    def perform() -> None:
        _scar(w, p, a.verb)
        if body is None:
            return
        p.body = body
        if p.body > 0:
            return
        # ⚠ `w.tenures`, NOT `p.tenures + w._unowned`, AND THAT IS A FIX `W-E`'s OWN TEST FOUND.
        # `p.tenures` is the tenures this person is the SUBJECT of (§15.1 -- a Tenure is owned by
        # its subject), so the old scan could not see an edge ANOTHER PERSON owns that names the
        # dead one as its OBJECT. Measured in `tiny_world`: `t10`, a live `tie` from `p_low` to
        # `p_mid`, survived `p_mid`'s death and then DANGLED, because `del w.persons[who]` had
        # already removed the person it pointed at. §15.3 is explicit that the tenure ends THROUGH
        # THE DEATH; this is the write the `Felled` branch declares (`Tenure.until`) actually
        # reaching every edge it names. `w.tenures` is owner-first over every person plus
        # `_unowned`, so it is a WIDENING of the same scan and not a second rule.
        # ⚠ THE CASCADE MOVED TO `World.remove_person` (item 3b) AND THE COMMENT ABOVE IS ITS
        # PROVENANCE. It is unchanged in behaviour — the same `w.tenures` scan, for the same `W-E`
        # reason — and it moved because MATTER is now a SECOND way to die (a body reaching 0 from
        # an empty larder), and two sites closing tenures by hand is how the two drift apart (§8).
        # ⚠ G3: THESE CLOSURES ARE `destroy's cascade`, AND THE GATE RECOGNISES THEM BY
        # OBSERVATION. They run inside this act's own gated write (the `(Person, body)` pair, the
        # first in the `Felled` band), `remove_person` takes `who` out of `w.persons` in the same
        # `apply()`, and the gate admits a closure of an edge naming an id THE SAME WRITE removed
        # -- and nothing else. A cascade that closed the edges and left the person standing would
        # be refused and put back.
        w.remove_person(who)
    return Change((Subject.entity("persons", who, fields=("body",)),), perform)


@effect_for("march")
def _eff_march(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3 (M4, `ED-IN-0279` clause (a)): writes `(Person, body)` and `(Person, stance)` -- ON
    THE LOSING SIDE ONLY, on either band. Jordan's ruling on clause (b): a loss writes *"casualties
    only, decrease in morale, and a grudge token"* and nothing else -- the ruling is silent on the
    winner because it was never asked, and this does not invent an answer for it.

    ⚠ `Won`/`Lost` NAME THE ATTACKER'S OWN OUTCOME (`seam/ladder.py::field_degree`), NOT WHICH
    SIDE THIS WRITE LANDS ON. `Won` means the DEFENDERS lost; `Lost` means the ATTACKER'S OWN
    claimants lost. Reading both sides off `res.result["parties"]` and picking the loser by
    `res.degree` is the whole of that translation. This is NOT `kill / wound`'s *"the band is
    read off the ACT'S SUBJECT, never off `the loser` as a fixed party"* correction reapplied --
    that correction was about a payload naming ONE person; a field battle genuinely has two
    candidate losing SIDES and `res.degree` already names which one.

    ⚠ THE MAGNITUDE IS READ FROM THE ENGINE, NOT INVENTED, ON `wound_harm_model`'s OWN PRECEDENT.
    `field_casualty_model` (`H-148`) names three arms: `scaled_by_degree` (the default -- each
    loser's body scales by the SAME survivor fraction the engine computed for their whole side,
    `attacker_size_pct`/`defender_size_pct`), `total` (every loser's body to 0 -- the control,
    re-running "losing costs everything" deliberately), `none` (body is not written at all -- the
    second control, isolating the write from the band). The default is settled by Jordan's
    2026-09-04 ruling on `wound_harm_model` -- *"the combat engine determines the result there"*
    -- applied to this magnitude too, not by a fresh measurement; `tools/balance_oracle.py` is
    `mc_v18`-only and cannot observe an `engine/season`-only mechanic (`rosters.yaml`'s
    `field_casualty_models` note).

    ⚠ THE STANCE ROWS FOLLOW THE SEEDED-LOYALTY SHAPE (`harness/data/cast.py`'s own
    `stance_from_loyalty`): a FIXED valence of `-1.0` (both are negative sentiments; the sign is
    not swept) and a WEIGHT that is (`field_morale_weight`/`field_grudge_weight`, `H-148`,
    swept `0`/`1`/`3`). The grudge targets the WINNING faction; the morale hit targets the
    LOSER'S OWN faction -- both re-derived from `a.via` (the office the act was exercised
    through, `exercised_seat`'s own field) and `world_q.holder_faction_of` on the target rung,
    exactly as `loop/sides.py::sides_of` derives them, because both are facts about the ACT and
    re-deriving them here is cheaper and safer than threading a third value through `Resolution`
    for one reader."""
    if res is None or not isinstance(res.result, dict):
        raise Unspecified(
            f"`march` on {_operand(a, 'subject')!r} was folded with no result to read a "
            f"casualty count from", "S39.4/H-98",
            needs="a Resolution from `resolve()`'s seam branch -- the mass_battle provider",
            law="M4 (`ED-IN-0279` clause (a)) -- the magnitude is READ from the engine's own "
                "survivor ratio, never invented here")
    if res.degree in (DECLARED, UNOPPOSED):
        return NO_CHANGE
    parties = res.result.get("parties") or {}
    attackers = list(parties.get("claimants") or [])
    defenders = list(parties.get("subject_members") or [])
    engine_result = res.result.get("result") or {}
    attacker_lost = res.degree == LOST
    losers = attackers if attacker_lost else defenders
    pct = engine_result.get("attacker_size_pct" if attacker_lost else "defender_size_pct")
    touched = [pid for pid in losers if pid in w.persons]
    if not touched:
        return NO_CHANGE
    model = w.fixtures.get("field_casualty_model")
    require_member(
        model, FIELD_CASUALTY_MODELS, f"field-casualty model {model!r} is not in the roster",
        "H-148", law="`wound_harm_model`'s own precedent -- an unrecognised mode silently "
        "falling back would make every measurement of this sweep read the control")
    target = _operand(a, "subject")
    office = w.offices.get(a.via)
    attacker_faction = (faction_prop_id(office.faction)
                        if office is not None and office.faction else None)
    defender_faction = holder_faction_of(w, target)
    winner_faction = defender_faction if attacker_lost else attacker_faction
    loser_faction = attacker_faction if attacker_lost else defender_faction
    if model == "none" and winner_faction is None and loser_faction is None:
        return NO_CHANGE
    morale_w = w.fixtures.get("field_morale_weight")
    grudge_w = w.fixtures.get("field_grudge_weight")

    def perform() -> None:
        for pid in touched:
            p = w.persons[pid]
            if model == "total":
                p.body = 0
            elif model == "scaled_by_degree":
                p.body = max(1, int(p.body * max(0.0, pct or 0.0)))
            # `none`: the control arm -- body is not written at all.
            rows = list(p.stance or [])
            if winner_faction:
                rows.append((winner_faction, -1.0, grudge_w))
            if loser_faction:
                rows.append((loser_faction, -1.0, morale_w))
            p.stance = rows
            # ⚠ `remove_person` ON THE `total` ARM'S OWN body==0, `_eff_kill`'s PRECEDENT
            # (`_eff_kill` above: "the body goes to 0 ... `w.remove_person(who)`" whenever a write
            # leaves `p.body <= 0`) -- found missing by `/code-review` on the M4 diff. Without it,
            # `total` left a living person recorded at body 0, a state no other path in this
            # engine produces (`_eff_kill` never does), and ED-IN-0279's own first row named
            # `Person.exists` on participants as the recommended option this omitted.
            # `scaled_by_degree` floors at 1 and never reaches this, on `wound_harm_model`'s own
            # precedent that a wound (never total) cannot kill.
            if p.body <= 0:
                w.remove_person(pid)
    fields = ("stance",) if model == "none" else ("body", "stance")
    return Change(tuple(Subject.entity("persons", pid, fields=fields) for pid in touched), perform)


@effect_for("utter")
def _eff_utter(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3: writes `(Proposition, exists)`. §14: a Proposition is IDENTITY-BEARING AND IMMUTABLE,
    fixed at utterance and never destroyed -- `Proposition` is a frozen dataclass, so that is
    structural here rather than asserted.

    G4 -- WHAT IT NAMES: THE PROPOSITION, whole; it always moves (absent -> present), because an
    id already uttered is declined before anything is built (`NO_CHANGE` -> `act.refused`, the
    fold's own kind, since the row declares no refusal -- as the old `None` produced)."""
    d = a.payload if isinstance(a.payload, dict) else {}
    pid = d.get("proposition") or f"prop:{a.id}"
    if pid in w.propositions:
        return NO_CHANGE                  # immutable: an utterance never overwrites one
    prop = Proposition(pid, d.get("mood") or "OUGHT", d.get("subject") or a.actor,
                       d.get("predicate") or "", d.get("value"), w.tick)
    return Change((Subject.entity("propositions", pid),),
                  lambda: w.propositions.__setitem__(pid, prop))


@effect_for("commit")
def _eff_commit(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3 `:426`: commits the actor to a Proposition -- a new `commit` Tenure opens, subject the
    actor, object the Proposition the act names (`Act.subject`, the row's typed precondition:
    *the Proposition exists, immutable, §14*). Plan position `7a`. `commit` is a `tenure_kinds`
    member (`rosters.yaml`) with no opener until this effect -- `tenure_kinds_without_an_opener()`
    reported it, and `resolvable_verbs()` (`loop/driver.py`) excluded the verb for want of one,
    per §E3's `writes: ["Tenure.since"]` with nothing to perform it.

    ⚠ THE BAREST OPENER IN THIS FILE: no seat, no closure, no per-kind branch. `commit` is
    `own`-eligible with `beneficiary: actor` and carries no `via`, so the edge it opens names the
    actor as its own subject and is admitted under `T-m` (`state/gate.py::tenure_write_basis`) --
    the same basis `_eff_confer`'s new `hold` and `_eff_release`'s closures stand on. Read
    `_eff_confer` above for the general shape (name the edge, defer the mint into the closure);
    its seat/incumbent-closure logic does not apply here, because nothing closes and no `via` is
    read.

    G4 -- WHAT IT NAMES: THE EDGE, whole -- the one write the row declares. It always moves
    (absent -> present: `add_tenure` mints a fresh Tenure, never overwrites one), so a `commit`
    that reaches this effect is never a no-op; the row's one refusal (the Proposition does not
    exist) is the typed precondition's, asked before this ever runs, and there is nothing left for
    the effect itself to decline.

    THE ID SALTS ON THE OBJECT AND THE ACT, `_eff_give`'s `f"hold:{rid}:{a.id}"` pattern (`H`'s
    `subject_id` slot is the new Tenure's own subject, its `purpose` is `f"{kind}:{object}:{act}"`)
    -- BATCH-CLOSE FINDING (methodology-close Phase 1, antagonist), corrected from the plain
    `f"commit:{prop_id}"` this shipped with: two different actors committing to the same
    Proposition already minted distinct ids (each one's `subject_id` is its own actor), but an
    actor who releases a `commit` and re-commits to the SAME Proposition within the same tick
    would otherwise mint the identical id as the now-closed one -- the same collision `_eff_give`'s
    own docstring names and salts against. `commit` has no `release`-then-reopen path reachable
    today (untyped, chooser-unreachable), but the fix is one token and costs nothing to carry.

    ⚠ BUILD-ORDER BO-9/BO-10 (`proposals/2026-09-17-governance-and-behaviour/01_THE_BUILD_ORDER.md`
    §7.2): the first build of this effect, before any question source offered a Proposition
    referent, measured `commitment.made : 0` / `commitment.refused : 42` on one populated season --
    a structural gap in `operands_for`/`questions_for`, not in this body, and HELD rather than
    shipped. Items 5/7/8 (here `15`, `15c`, `15b`) are what BO-10 named as opening that aperture;
    this effect is unchanged from the held draft, because the diagnosis put the gap upstream of it.

    ⚠ NOT FACTORED WITH `_eff_oblige` BELOW, THOUGH THE TWO BODIES ARE IDENTICAL BUT FOR ONE STRING
    -- BATCH-CLOSE FINDING (methodology-close Phase 2, REUSE/SIMPLIFICATION lenses), REVERTED after
    trying it: `_derive_openers_from_effects` (`data/verbs.py::OPENERS-DERIVE`) is an AST walk over
    THIS FILE's own source that reads which verb opens which `tenure_kinds` member off a STRING
    LITERAL at each `Tenure(...)` call site, by design (its docstring: *"every site today names
    `kind` as a STRING LITERAL"*). A shared helper taking `kind` as a parameter makes that literal
    disappear from this file's source, and the walker silently stopped seeing `commit`/`oblige` as
    openers at all (`test_obligees.py::test_17a_oblige_is_resolvable_and_takes_releases_route`
    caught it: `_OPENERS_FROM_EFFECTS.get("oblige")` went from `["oblige"]` to `[]`). The
    duplication is real and the fix is not -- this is `create_record`/`issue`/`petition`'s
    `_mint_document` in reverse: that helper is safe to share because all three name the SAME
    literal kind (`hold`) inside it; `commit` and `oblige` do not, so nothing here can be factored
    without either losing the literal or hand-editing the derived roster back into a second copy."""
    prop_id = _operand(a, "subject")
    nt = Tenure(H(w.world_seed, w.tick, a.actor, f"commit:{prop_id}:{a.id}"), a.actor, prop_id,
                "commit", since=w.tick)
    return Change((Subject.edge(nt),), lambda: w.add_tenure(nt))


@effect_for("oblige")
def _eff_oblige(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§E3 `oblige`: the actor takes a duty to a seat -- a new `oblige` Tenure opens, subject the
    actor, object the seat the act names (`Act.subject`). Plan position `17a` (r2 item 9, `03` §A.9:
    *"`@effect_for("oblige")`: mint the Tenure the row already declares"*). `oblige` is a
    `tenure_kinds` member with no opener until this effect, so `resolvable_verbs()` excluded it
    for want of one, per its `writes: ["Tenure.since"]` with nothing to perform it.

    ⚠ `_eff_commit`'s SHAPE, EXACTLY -- the barest opener: no seat EXERCISED (`oblige` is
    `own`-eligible, `via` is `None`), no closure, no per-kind branch. The edge names the actor as
    its own subject and is admitted under `T-m` (`state/gate.py::tenure_write_basis`). The id salts
    on the object AND the act, `f"oblige:{seat}:{a.id}"` (`_eff_give`'s pattern, and `_eff_commit`'s
    since the same antagonist pass) -- BATCH-CLOSE FINDING (methodology-close Phase 1), corrected
    from the plain `f"oblige:{seat}"` this shipped with: an actor who releases their `oblige` to a
    seat and re-obliges to the SAME seat within the same tick would otherwise mint the identical id
    as the now-closed one. `oblige` has no such path reachable today (untyped, chooser-
    unreachable), but the fix is one token.

    ⚠ IT WAS WRITTEN AND REVERTED ONCE (`ED-IN-0211`): it opened a Tenure to `einhir_texts`, a bare
    string naming no entity. What changed is not this body but that `_req_oblige` now asks first --
    the subject is a seat, its `binds` admits the joiner, the actor does not sit in it, and no live
    `oblige` from him to it -- so by the time this runs there is nothing left to decline, and the
    edge it opens always moves (absent -> present), never a no-op.

    WHAT THE EDGE IS FOR: `queries/world_q.py::establishment_of` reads it (the seat's members, `ARCH
    §B.7` call 2), and through that the obligee channel (`epistemic._ch_post_remit`) -- an obligee
    standing at the seat holds what the seat does `inferred`. `release` ends it (`04 §A.3` row 14).

    ⚠ NOT FACTORED WITH `_eff_commit` ABOVE -- see its docstring: the two are `Tenure(..., kind,
    ...)` calls whose `kind` differs, and `_derive_openers_from_effects` needs that string literal
    visible at THIS call site to derive the opener roster. Read there for what was tried.

    ⚠ PLAN POSITION `17b`: THE EDGE IS OPENED WITH A DECLARED TERM, AND THIS IS THE ACT THAT DECLARES
    IT. `T-n` (`01_AXIOMS.md:1240`): *"So the opening act declares the terms"*; the retirement plan's
    G2: *"`oblige` Tenures carry a term (T-n) the paying act renews; unpaid terms mature and shrink
    the office's establishment"*. `matures_at` is `w.tick + oblige_term` (the fixture is the
    declared stand-in for a term a computed act cannot yet carry -- `H-159`, `record_stage_term`'s
    shape), and `declared_by` is THIS act, so an unpaid lapse at MATTER cites the oblige that wound
    it. Only `oblige` is given one: `commit`, `tie` and the rest carry `term=None`, which `04 §B.8`
    makes lawful (`term?`) and which no MATTER branch matures. The fixture's control arm `None`
    opens the edge exactly as `17a` did, with no term. A service nobody pays for now ENDS -- which
    is `F.18`'s *"no economic pressure on any office"* answered, and `release` is still the obligee's
    own way out before then."""
    seat = _operand(a, "subject")
    nt = Tenure(H(w.world_seed, w.tick, a.actor, f"oblige:{seat}:{a.id}"), a.actor, seat, "oblige",
                since=w.tick, term=_new_oblige_term(w, a))
    return Change((Subject.edge(nt),), lambda: w.add_tenure(nt))


def _oblige_term(w: "World") -> Optional[int]:
    """THE LENGTH, IN SEASONS, OF THE TERM AN `oblige` IS DECLARED FOR -- and that a paying act winds
    it on by -- read ONCE for both of its readers (`_eff_oblige`, `_renewals`), with the refusal
    in the same place. `None` is `H-159`'s control arm: no term at all. Anything else must be a
    whole number of seasons, at least one: a term of `0` would mature in the season that declared
    it (MATTER has already run when RESOLVE opens the edge, so it lapses at the next barrier with
    no window to pay), and a renewal by `0` moves no clock and would be refused as no renewal at
    all -- a number that looks like a setting and behaves like a defect."""
    n = w.fixtures.get("oblige_term")
    if n is not None and (isinstance(n, bool) or not isinstance(n, int) or n < 1):
        raise Forbidden(
            f"fixture oblige_term is {n!r}", "T-n",
            needs="None (no term: H-159's control) or a whole number of seasons >= 1",
            law="04 §B.8 `term?` / T-n -- the opening act declares a term that MATTER matures at a "
                "later barrier; a term that cannot outlive its own season is not one")
    return n


def _new_oblige_term(w: "World", a: "Act") -> Optional["Term"]:
    """The `Term` an `oblige` edge OPENS with, for the two writers that mint one from scratch
    (`_eff_oblige`, `_eff_determine`) -- one owner for the `None if n is None else Term(...)`
    ternary rather than a second hand-copy of it (`/simplify`, BATCH-CLOSE Phase 2). `_renewals`
    winds an EXISTING term rather than minting one and is not one of these two."""
    n = _oblige_term(w)
    return None if n is None else Term(w.tick + n, a.id)


@effect_for("transfer")
def _eff_transfer(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """§54 item 7's mirror: the giver's store goes DOWN and the receiver's goes UP.

    ⚠ THE FIRST VERSION ONLY DECREMENTED, and §E3 says `transfer` writes `(Rung, stores)` **×2**,
    one per side. A one-sided transfer ANNIHILATES MATTER -- six grain left the world and arrived
    nowhere, in an economy where `yield` is the only source (#353 `:856`). The scarcity proof still
    passed, because it only watched the giver: a run can be right about the thing it looks at and
    wrong about the world.

    G4 -- WHAT IT NAMES: BOTH RUNGS, giver first, each whole -- the two `(Rung, stores)` writes and
    the two ids it always reported. Two no-ops become visible that the old contract reported as
    successes: a transfer of `amount` 0, and a transfer from a rung TO ITSELF (the decrement and
    the increment land on one store and cancel). Each moved nothing and is now `transfer.refused`.
    Neither is a transfer; both published `transfer.made` with two receipts. MEASURED BEFORE THIS
    POSITION on `build_realm(0)`, four seasons: no `transfer` reached this effect at all (every one
    refused at its precondition), so no run moves."""
    # ⚠ FOUR SILENT DEFAULTS STOOD HERE AND `W-C` DELETED ALL FOUR: `from`/`to` defaulted to
    # `""`, `kind` to `"grain"` and `amount` to `1`. Each was §0.05's literal-in-a-body, and
    # together they made an operand-less `transfer` a WELL-FORMED act about a granary nobody
    # named. They are `_operand` reads now, and their two open values are fixtures with a register
    # row and a sweep (`H-94`).
    src = w.rungs.get(_operand(a, "from"))
    dst = w.rungs.get(_operand(a, "to"))
    kind, amount = _operand(a, "kind"), _operand(a, "amount")
    # ⚠ A SIDE THAT IS NOT A RUNG MEANS THE TRANSFER DID NOT HAPPEN, and returning nothing is what
    # makes the fold emit the refusal. This branch became reachable FROM A COMPUTED ACT the moment
    # operands became real: a person names a receiver from their question's referents and may name
    # something that is no rung at all. The old shape moved the giver's side anyway, which is the
    # matter ANNIHILATION this effect's own docstring records -- grain leaving the world and
    # arriving nowhere. §42.2's polarity: an unperformable transfer refuses; it does not
    # half-happen.
    # ⚠ *"IT SURVIVED ONLY BECAUSE NO COMPUTED ACT EVER BOUND `from` TO BEGIN WITH"* STOOD HERE
    # AND IS FALSE; STRUCK BY THE `W-C` ADVERSARIAL PASS. No COMPUTED act bound `from` -- but
    # probe `F10` did, in its payload, and omitted `to`, so the old effect decremented `Hh` and
    # delivered nowhere: `F10` DESTROYED 6 GRAIN ON EVERY PROBE RUN, in an economy where `yield`
    # is the only source. Measured by weighing every rung across the probe's own season: total
    # store mass ends at 107 on the pre-`W-C` tree (`45a537c`) and at 113 here, and the difference
    # is exactly the 6. The path was reachable AND REACHED; only the computed path was closed, and
    # `F10`'s payload edit is a BUG FIX in a live probe rather than a signature accommodation.
    # `F10` now asserts conservation, because its old assertion set could not observe the failure
    # it was sitting on (§0.1 point 2).
    if src is None or dst is None:
        TRACE.decision(f"transfer names a side that is no rung -> from "
                       f"{_operand(a, 'from')!r} to {_operand(a, 'to')!r}", "E3/S27.1",
                       chose="change nothing, so the fold emits the refusal",
                       alternatives=["move the giver's side anyway (matter leaves the world)"])
        return NO_CHANGE

    renewed = _renewals(w, a, src.id, dst.id, amount)

    def perform() -> None:
        _shift(src, dst, kind, amount)
        for t, term in renewed:
            t.term = term
    # BOTH SIDES, because §E3 says `transfer` writes `(Rung, stores)` twice -- one per side -- and
    # a one-sided report would make the Event name half of what it did. The `if r is not None`
    # filter that stood here is gone with the branch above that made it necessary.
    # ⚠ PLAN POSITION `17b`: EACH SUBJECT NOW NAMES THE KIND IT EARNS. The row declares
    # `term.renewed` beside `transfer.made`, and a subject earning `None` earns EVERY declared kind
    # (`loop/resolve.py::_fold`) -- so left as they were, the two rungs would publish a renewal on
    # every transfer that renewed nothing, and one renewed edge would earn `term.renewed` ALONE and
    # silently drop `transfer.made`. Named per kind, an ordinary transfer emits exactly what it
    # always did. The renewed edges ride as `edge` subjects, judged by G3's diff (`renewal`).
    # ⚠ THEIR RECEIPTS CARRY THE FIRST PAIR'S FIELD, `stores`, not `term` -- the fold mints every
    # subject's receipt against the write pair the effect ran on (`_eff_confer`'s docstring has the
    # history; `establish`'s re-stamped holds carry `exists` the same way). A known limit of the
    # one-effect-per-act fold, not a claim that a Tenure's stores moved.
    return Change((Subject.entity("rungs", src.id, "transfer.made"),
                   Subject.entity("rungs", dst.id, "transfer.made"))
                  + tuple(Subject.edge(t, "term.renewed") for t, _ in renewed), perform)


def _shift(src, dst, kind: str, amount) -> None:
    """MATTER MOVES FROM ONE RUNG'S STORES TO ANOTHER'S, CONSERVED: `src` down by `amount` of `kind`,
    `dst` up by the same. The one body of every act that moves stores between two rungs -- `transfer`
    and, since plan position `19`, `levy` -- factored so the W3 audit's lesson is written once:
    *"six grain left the world and arrived nowhere"* was a transfer that decremented one side and
    forgot the other. Each store is copied before it is written, as `_eff_transfer` always did, so
    no other holder of the old dict sees it change. Called only from inside a `Change.apply`: the
    gate reads both rungs either side of it (G4)."""
    src.stores = dict(src.stores or {})
    src.stores[kind] = src.stores.get(kind, 0) - amount
    dst.stores = dict(dst.stores or {})
    dst.stores[kind] = dst.stores.get(kind, 0) + amount


def _exercised_office(w: "World", a: "Act") -> Optional["Office"]:
    """The Office an act's `via` names, or `None` -- the one-line resolution `_eff_levy` and
    `_renewals` both did inline (`/simplify`, BATCH-CLOSE Phase 2). NOT `_seat_rung`: that helper's
    fallback (a document's `payload.rung`, else the actor) is for a Record write, not for either of
    these two, which have their own reasons to want the bare Office or nothing."""
    return w.offices.get(a.via) if a.via else None


@effect_for("levy")
def _eff_levy(w: "World", a: "Act", res: "Resolution | None" = None) -> Change:
    """PLAN POSITION `19` -- A LEVY MOVES A RUNG'S STORES INTO THE LEVYING SEAT'S TREASURY. The row's
    `scale_note`, *"a levy moves a Rung's stores -- the rung IS the subject"*; the retirement plan's
    G2 names where it goes, *"treasury = `Rung.stores` at the office's own rung"* -- the rung of the
    seat the act exercises (`Act.via`), the same treasury `_renewals` pays upkeep OUT of. So a levy is
    `transfer`'s shape with both sides fixed by the act's seat and subject rather than by the actor's
    home: `_shift` moves `amount` of `kind` from the levied rung to the seat's rung, conserved.

    ⚠ `writes: [Rung.stores, Rung.stores]`, ONE PER SIDE, AND THAT IS A CHANGE TO THE ROW. It declared
    ONE, as `transfer` once did, and the W3 audit's lesson is that a one-sided write annihilates
    matter. The second pair is check-only (class, step, partition), like `transfer`'s.

    WHAT THE ROW'S PRECONDITION HAS ALREADY ASKED, SO THIS DOES NOT: the seat's purview reaches the
    levied rung (`Basis`, `purview` -- which also refuses a rungless seat, so a seat that gets here
    has a treasury), and the rung holds `stores(subject, kind) >= amount` (`transfer`'s own form-2
    cell). §27.1's scarcity is that second conjunct read against the world THIS fold has left: two
    levies on one larder, and the second finds it short and emits `levy.refused`.

    DECLINES (`NO_CHANGE` -> the row's `write` clause, `levy.refused`): a side that is no rung --
    the hand-built act that skipped the precondition, `_eff_transfer`'s branch -- and, through G4
    rather than a line here, a levy of a seat's own rung into itself (both sides one store: nothing
    moves, `NoOpReceipt`), or of `0`.

    G4 -- WHAT IT NAMES: BOTH RUNGS, levied first, each whole and each earning `levy.taken`, as
    `_eff_transfer` names its two. NOT a Tenure write, so F3 asks nothing of it: the seat's authority
    over the rung is the precondition's `purview` conjunct, and the gate never observes stores
    (`may_renew`'s docstring states the same split)."""
    # THE TREASURY IS THE SEAT'S RUNG AND NOTHING ELSE -- deliberately NOT `_seat_rung`, whose
    # fallback (`payload.rung`, else the actor) is where a DOCUMENT may be drawn up; matter levied
    # through no seat, or a rungless one, has no treasury to go to, and the actor's own person-rung
    # is not one.
    seat = _exercised_office(w, a)
    src = w.rungs.get(_operand(a, "subject"))
    dst = w.rungs.get(seat.rung) if seat is not None and seat.rung is not None else None
    kind, amount = _operand(a, "kind"), _operand(a, "amount")
    if src is None or dst is None:
        return NO_CHANGE
    return Change((Subject.entity("rungs", src.id), Subject.entity("rungs", dst.id)),
                  lambda: _shift(src, dst, kind, amount))


def _renewals(w: "World", a: "Act", src: str, dst: str, amount) -> list:
    """PLAN POSITION `17b` -- WHICH `oblige` TERMS A `transfer` RENEWS, as `[(edge, its new Term)]`.
    The whole of *"payment by `transfer` renewing `oblige` terms"* (the plan's Contradiction-1 box;
    the retirement plan's G2: *"treasury = `Rung.stores` at the office's own rung; payment = the
    existing `transfer` verb; `oblige` Tenures carry a term (T-n) the paying act renews"*), and
    `04 F.18`'s repair: *"A MATTER payment would be a fourth clock, so the repair is a verb."*

    A TRANSFER IS A PAYMENT OF UPKEEP WHEN, AND ONLY WHEN, all of these hold:
      1. it is exercised THROUGH A SEAT (`Act.via`) whose seated holder is the actor -- `may_renew`,
         the gate's own `renewal` test, asked here first so the effect never names an edge the gate
         would refuse (a `NotYours` would escape the fold and end the season);
      2. it is paid OUT OF THAT SEAT'S OWN RUNG -- *"what the post pays its establishment out of the
         office's stake"* (`holonic_ARCHITECTURE.md:428`). A holder paying from his own hearth is
         giving a gift, not keeping a seat; a seat with no rung has no treasury and cannot pay;
      3. matter actually MOVED: another rung, a positive amount. A transfer from a rung to itself
         cancels to nothing (G4 already refuses it as a no-op), and without this clause a seat whose
         obligee lives at the seat's own rung could renew a term by paying itself;
      4. the receiving rung is an obligee's HOME (`home_of`, the one owner of *where a person
         lives*) -- the larder upkeep fills.
    Then it renews, of that seat's live `oblige` edges carrying a term whose subject lives at the
    receiving rung, as many as the amount covers at `upkeep_of(seat)` apiece (`0`: all of them),
    SOONEST-MATURING FIRST, ties by edge id -- the man about to lapse is paid first, and the order
    is a rule, not an accident of the store. Each new term runs `oblige_term` seasons ON FROM WHERE
    THE OLD ONE STOOD (so paying early buys the next term; it is not lost), and is `declared_by`
    this act, so the next lapse -- if nobody pays again -- cites this payment as the last hand to
    wind the clock (AX-5).

    ⚠ NO ENTITY IS NAMED AND NO OUTCOME IS SCRIPTED. Embezzlement -- narrative #3, *"already runs"*
    (`proposals/2026-09-12-emergent-narrative-primitives-v2/01_THE_TEN.md` §3) -- is not a branch
    here: a steward who moves the treasury to his own hearth simply meets clause 4 for nobody, the
    terms he did not pay mature at MATTER, and the seat's `establishment_of` shrinks. That is the
    observable this position gives #3, and it falls out of the rule rather than being written.

    ⚠ ONE TERM PER OBLIGEE PER PAYMENT, and any excess is simply transferred. Buying several terms
    for one man with one large payment is a reading the fixture does not rule on, and taking it
    would make "how far ahead may a seat prepay" a second quantity with no row.

    ⚠ WHAT NO COMPUTED ACT CAN REACH TODAY, STATED RATHER THAN IMPLIED. Clause 1 needs `Act.via` on a
    `transfer`, and `decision/options.py::exercised_seat` sets `via` only for a `remit:` alternative
    -- `transfer` is `own | hold:<store>`, so every computed transfer carries `via=None` and renews
    nothing. And no computed act forms an `oblige` (its row is untyped, `17a`). So the mechanism is
    EXECUTED by hand-built acts (`tests/test_term_upkeep.py`) and by MATTER's maturation, which needs
    no act at all; a person CHOOSING to pay upkeep is `H-158`'s `unblocks:`, not this body's.

    The cheap refusals come first, so an ordinary transfer (no `via`) reaches no Query and moves no
    trace line."""
    seat = _exercised_office(w, a)
    if seat is None or seat.rung != src or src == dst or amount <= 0:
        return []
    if not may_renew(w, a.actor, a.via, seat):
        return []
    n = _oblige_term(w)
    if n is None:
        return []                         # `H-159`'s control: no term exists to renew
    homes = home_of(w)
    due = sorted((t for t in w.tenures
                  if t.kind == "oblige" and t.object == seat.id and t.live
                  and t.term is not None and homes.get(t.subject) == dst),
                 key=lambda t: (t.term.matures_at, t.id))
    each = upkeep_of(w, seat.id)
    covered = len(due) if each == 0 else min(len(due), amount // each)
    return [(t, Term(t.term.matures_at + n, a.id)) for t in due[:covered]]
