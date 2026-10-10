"""`season.loop.effects_governance` -- office/seat lifecycle: confer, establish, release, revoke,
convene, oblige, levy.

EXTRACTED from `effects.py` at the per-subsystem split (Phase 4). Holds every effect that opens or
closes a `hold`/`oblige` Tenure on an Office or Seat, schedules a sitting, or moves a levy into a
seat's own treasury -- the governance slice of the verb table. `_closing` (`release`/`revoke`'s one
shared write) stays local here rather than in `effects_shared.py`: nothing outside this file's own
pair of openers calls it. See `effects_shared.py` for `effect_for`, `_operand` and the other
cross-file helpers this file's effects call (`_exercised_office`, `_new_oblige_term`, `_shift`).
"""

from __future__ import annotations

from ..data.rosters import RELEASABLE_KINDS
from ..loop.predicates import office_described_by
from ..state.carriers import Tenure
from ..state.gate import NO_CHANGE, Change, Subject
from ..state.ids import H

from .effects_shared import _exercised_office, _new_oblige_term, _operand, _shift, effect_for

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
    refused.

    v9 IN-11 (#453 §10.4 step 2, R-3 (b)) -- A CLOSED `commit` EARNS `commitment.ended`, AND
    `repudiate` IS CUT. `release` was already the second closer of a `commit` (its domain), so the
    row that did nothing else is deleted and the vow-break stays witnessable here: WHOLE-ACT
    earning -- when any edge it closes is a `commit`, every edge earns every kind. A release that closes no `commit` names each edge earning
    `tenure.closed` only, exactly as before; one that closes a `commit` names every edge it closes
    earning the row's whole `emits:` (`earns=None`), because the fold unions only NAMED kinds
    (`loop/resolve.py::_apply_write`) -- a `commit` edge earning `None` beside a `hold` edge
    earning `tenure.closed` would publish `tenure.closed` alone and drop the vow-break, and an
    utterer who committed to his own Proposition holds both edges on it."""
    subj = _operand(a, "subject")
    edges = [t for t in w.tenures
             if (t.subject == a.actor and t.object == subj
                 and t.kind in RELEASABLE_KINDS and t.live)]
    earns = None if any(t.kind == "commit" for t in edges) else "tenure.closed"
    return _closing(w, edges, earns)


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


def _closing(w: "World", edges: list, earns: "str | None" = None) -> Change:
    """`release` and `revoke`'s one write: close these edges at this tick, each named as an `edge`
    subject earning `earns` -- `None`, every kind the row declares (`revoke`'s one,
    `tenure.closed`), unless the caller narrows it (`_eff_release`: `tenure.closed` alone when no
    `commit` closes). One body because it is one write; the two effects differ only in WHICH
    edges, which is the whole of each."""
    def perform() -> None:
        for t in edges:
            t.until = w.tick
    return Change(tuple(Subject.edge(t, earns) for t in edges), perform)


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
