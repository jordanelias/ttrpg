"""`season.epistemic` — what a person can come to KNOW, and who comes to know it.

EXTRACTED, step 6 of the decomposition (a PURE MOVE but for one call site, named below). Two
halves that belong together because they are the two ends of one channel:

  * **what is knowable** — `belief_contradicts` (§F1 clause 4, the one place a person's OWN
    ledger can refuse a candidate), and the two functions that decide what a deposit is ABOUT
    (`act_refs`, `claim_subjects`).
  * **who learns it** — `_event_place`, the five `_ch_*` witness-channel predicates, the
    `CHANNEL_PREDICATES` table built from the roster, `live_channels` and `observers_for`.
  * **what they saw** — `R8.1`'s `Seen` struct, its `_term_*` readers and `seen_of` /
    `seen_subject`, which `loop/witness.py` deposits as the `seen` claim.

⚠ `CHANNEL_PREDICATES` IS BUILT BY A `globals()` LOOKUP, AND THAT IS WHY THE FIVE PREDICATES
COULD NOT BE LEFT BEHIND. The loop below asks this module's globals for `_ch_<name>` for every
channel in `rosters.yaml`, and RAISES on a channel with no predicate. Split the table from the
predicates and it raises at import — loud, which is the good case, and the reason this carve
moves the table, its loop and its `del` as one block rather than as three statements. It is the
package's second such lookup; `state/carriers.py` records the first.

⚠ NOTHING HERE READS `belief_contradicts`, AND THAT IS LOAD-BEARING RATHER THAN INCIDENTAL. Its
only bare-name caller is `opening_set`, which lives in `season.decision` since step 7 and resolves
the name in THAT module's globals at call time — so every rebind must name `decision`, and all of
them do: the suite's six sites and `wd_acceptance.py`'s five, the latter through `sweep_core.PS`.
**If a function here ever calls it directly, that reader would bind THIS module's copy and those
rebinds would become no-ops on it** — the same hazard, one module over.

⚠ THIS PARAGRAPH PREDICTED ITS OWN EXPIRY AND THEN OUTLIVED IT. Until step 7 it read *"its only
bare-name caller is `Query.opening_set`, still in `shape.py`"* and closed with *"plan §0 item 1's
hazard, which arrives for real at step 7"*. Step 7 arrived; `Query.opening_set` no longer exists;
three clauses went false at once, and the step that falsified them corrected four other
breadcrumbs and skipped this one — the file that had named itself as the tripwire. `shape.py`'s
own rule covers it: WRITE THE RULE, NOT THE ADDRESS. A ruling recorded as a location is a claim
that expires silently at the next move.

⚠ `04_CODE_ARCHITECTURE.md` §A.2 DOES NOT NAME AN `epistemic` MODULE, and this docstring says so
rather than implying otherwise. Its nine are `state/ data/ queries/ decision/ loop/ seam/
manifest/ port/ tests/`; the channel half of this file is what §A.2's `loop/witness` row calls
*"channel predicates"*, and the knowable half is read by `decision`. The decomposition plan's §1
table names `epistemic.py` at layer 9 and that is what this is. Whether it folds into
`loop/witness` when the driver lands at step 9 is that step's call, not this one — the same
disposition `queries/readers.py` carries.

⚠ ONE LINE IS NOT A BYTE-IDENTICAL MOVE, declared rather than buried: `Query.presence` in
`_ch_co_located` is `world_q.presence` here. Same function object — `shape.Query` binds it — but
a channel predicate reaches a world query through the module that owns it.
"""

from __future__ import annotations

from dataclasses import dataclass, fields as _dc_fields
from typing import Optional

from .data.requires import binding_of, evaluate
from .data.rosters import (
    CLAIM_SUBJECT_RULES, FAN_OUT_MODES, OBSERVATION_DEPOSIT, OBSERVATION_TERMS, TERMS_SUPPLIED_BY,
    WITNESS_CHANNELS, require_member)
from .data.verbs import NO_PRECONDITION, VERB_TABLE, VerbRow
from .gaps import Unspecified
from .state.attribution import anchor_of
from .queries import cache, world_q
from .queries.person_q import LedgerReader
from .state.carriers import Event, Person
from .state.world import World


def belief_contradicts(p: Person, row: "VerbRow", subject: str, operands: dict) -> bool:
    """§F1 clause 4 -- is `requires(verb)` KNOWN-FALSE from `p`'s OWN claims?

    ⚠ THE ASYMMETRY IS THE WHOLE POINT AND MUST NOT BE SOFTENED TO "requires holds". This returns
    True only when the person HOLDS A CLAIM THAT CONTRADICTS the requirement. Having no belief
    either way is NOT a contradiction, so the Candidate forms, the person acts on a false premise,
    and the fold refuses them -- which is §F1's "a person who *wrongly* believes the granary full
    still forms the Candidate ... That is T3 and L2 working."

    Jordan, 2026-09-02: *"we can't control how others perceive and interpret our words or
    actions"* and *"our understanding of all other words and actions is subjective and singular."*
    A filter on world truth would be `choose` reading the world; this reads one person's ledger.

    ⚠ `W-A`: IT ASKS THE VERB'S OWN TYPED CELL, NOT A ROSTER. The previous version filtered on
    `predicate in PERSON_PREDICATES and value is False` -- a MEMBERSHIP TEST standing in for a
    requirement, because the `requires:` column was prose and `H-72` recorded that the map from a
    requirement to a predicate did not exist. `H-116` then measured the consequence: over 4,800
    deposited claims the two vocabularies were DISJOINT and zero claims were falsy, so clause 4
    could not fire in any run and the candidate set was invariant with respect to everything that
    happened in the simulation. The predicate is DERIVED from the form now (`stores:grain`,
    `condition`, `contain.path:D`), so there is one namespace and the write side has a name to aim
    at. `H-116`'s other half -- WITNESS depositing claims in that namespace -- is not this item.

    ⚠ AN UNTYPED VERB IS NOT CONTRADICTED. `evaluate(None, ...)` is UNKNOWN, and UNKNOWN is not
    False: a person cannot know a requirement fails when nothing states what the requirement is.
    That polarity is the OPPOSITE of the fold's, deliberately -- §F1 filters on belief and §42.2
    governs the resolver -- and the same `Verdict` carries both readings.

    ⚠ `W-C`: IT READS THE CANDIDATE'S OWN OPERANDS, WHICH IS WHAT MAKES THIS THE SAME QUESTION
    THE FOLD ASKS. It used to call `binding_from`, which rebound `subject` onto whichever operand
    the cell called its entity -- so for `transfer` the person asked *does the RECEIVER hold the
    grain*, and §54 item 7 asks about the GIVER's hearth. The person was reading a different cell
    from the fold and getting a defensible-looking answer to the wrong question. `operands` is the
    same bag the Act will carry, passed through the same `binding_of`, so the two sides now differ
    only in WHAT THEY READ (one ledger, one world) and in POLARITY -- which is the difference
    that is supposed to be there."""
    if (row.requires or "").strip() in NO_PRECONDITION:
        return False
    return evaluate(row.requires_typed, LedgerReader(p.ledger),
                    binding_of(p.id, operands)).value is False


def act_refs(a) -> list:
    """The ids an Act NAMES — the meta-architecture's `Act.refs`, read off what the tracer's Act
    already carries rather than added as a second home for it.

    ⚠ **THIS EXISTS BECAUSE A TELLING CHANGES NOTHING.** `tell` declares `writes: []` — correctly;
    it *"deposits at WITNESS, not here"* — so its Event's `changes[]` is empty, and a deposit that
    reads only the Event has nothing to be about. The one thing that knows what was told is the
    act, and `payload["subject"]` is where `pack_scenes` puts it and where `_req_tell` reads it."""
    if a is None:
        return []
    pay = getattr(a, "payload", None)
    subj = pay.get("subject") if isinstance(pay, dict) else (pay if isinstance(pay, str) else None)
    return [subj] if subj else []


def _tenure_by_id(w: "World", tid: str):
    """The Tenure with this id, or `None`. Linear, and deliberately not indexed -- the same
    precedent `state/attribution.py::_event_by_id` states for the log: a lookup that is not hot
    does not earn a second structure to keep in step with `w.tenures`. Not called on a hot path
    -- measured over a 44.6s / 143-case corpus run, this lookup is reached 52 times against
    39,932 `claim_subjects` calls total, 0.111s of the run (`ED-IN-0267`'s own measurement)."""
    for t in w.tenures:
        if t.id == tid:
            return t
    return None


def _hold_tenure_ends(w: "World", subject: str) -> tuple:
    """`H-71`'s office-shaped rule, factored so `claim_subjects` and `seen_subject` answer *what is
    this deposit really about* once rather than twice. If `subject` is a `hold` Tenure's own id --
    the edge, not what it connects -- this returns its `(holder, held)` pair; any other subject,
    including a non-`hold` Tenure id (`commit`/`oblige`/`succeed`/`tie`/`knot`), passes through
    unchanged, which is the safe default `claim_subjects` already documents for those kinds.

    ⚠ EXTRACTED FOR `R8.1`, NOT REWRITTEN BESIDE IT (found by adversarial review): the first `seen`
    writing left `seen_subject` depositing a `hold` Tenure's own opaque id -- unwitnessable, because
    no live Tenure has a Tenure's own id as its `object` (`questions_for`'s `mine`), so Q2 could
    never fire for exactly the office-conferral/revocation events `R8.4`'s last row names. One
    owner closes that gap for both callers at once."""
    t = _tenure_by_id(w, subject)
    if t is not None and t.kind == "hold":
        return (subject,) if t.subject == t.object else (t.subject, t.object)
    return (subject,)


def claim_subjects(w: "World", e: "Event", rule: str, refs: Optional[list] = None) -> list:
    """`H-79`: what the claims deposited from one Event are ABOUT.

    `actor` is the incumbent — one claim, subject = the Event's anchor (`anchor_of`; it was the
    Event's own `subject` field until G1b deleted it). `per_change` mints
    one per `StateChange`, subject = THE THING CHANGED, which is what makes §F1's Q2 clause
    "something they hold" reachable at all. `both` is the union.

    Order is deterministic and de-duplicated, because a person holding two identical claims about
    one Event would double-count in every eviction comparison."""
    require_member(
        rule,
        CLAIM_SUBJECT_RULES,
        f"claim-subject rule {rule!r} is not in the roster",
        "H-79",
        law="#353 §20 types `Claim.subject` and never says what a WITNESS deposit's subject "
            "is; a rule outside the roster is a fourth answer nobody declared")
    # G1b. `anchor_of` REPLACES `e.subject`, and it is the same value by measurement rather
    # than by intention -- 1,428 events over 5 seeds, 0 disagreements (`state/attribution.py`).
    # What it adds is that the two senses the field conflated are now separable: an act-caused
    # Event anchors on its ACTOR, a MATTER write on the THING WRITTEN, and a reader no longer has
    # to infer which it received from whether the id happens to name a person.
    anchor = anchor_of(w, e)
    out = [] if rule == "per_change" else [anchor]

    def _add(entity: str) -> None:
        if entity not in out:
            out.append(entity)

    if rule in ("per_change", "both"):
        for c in e.changes:
            if not c.subject:
                continue
            # ⚠ H-71's OTHERS HALF -- A `hold` TENURE'S RECEIPT NAMES THE EDGE, NOT WHAT IT
            # CONNECTS, AND A WITNESS CANNOT ACT ON AN EDGE'S OWN ID. `_eff_confer`/`_eff_revoke`/
            # `_eff_release` report the Tenure's own hash id as touched -- correctly, because that
            # is what the gate actually wrote (the Receipt's honesty is what a rejected earlier
            # fix broke, by reporting the office and the holder in the Tenure's place). Expanding
            # here, at the READER, keeps that honesty and still makes the fact legible: a claim
            # about a `hold` that opened or closed is really a claim about its SUBJECT (who) and
            # its OBJECT (what they hold).
            #
            # ⚠⚠ SCOPED TO `t.kind == "hold"`, NOT TO THE EVENT KIND -- A FIRST VERSION KEYED ON
            # `e.kind in ("tenure.opened", "tenure.closed")` AND THAT WAS WRONG, FOUND BY
            # ADVERSARIAL REVIEW. Both kinds are shared by every Tenure closer: `_eff_release`
            # ends ANY of `RELEASABLE_KINDS` (`hold, commit, oblige, succeed, tie, knot`,
            # `data/rosters.py`) through the ONE generic `tenure.closed` emit
            # (`verb_table.yaml`'s `release` row), so keying on the event kind admitted every one
            # of those, not just offices -- a `release` of a person's `commit` Tenure to an OUGHT
            # Proposition would have expanded into `(person, ...)` and `(proposition, ...)` and
            # broadcast both to every witness under the shipped `all_five` default, which is a
            # moral/ambition fact nobody ruled witnessable and the exact class of unmediated
            # deposit `AX-7`'s falsifier names. Keying on the TENURE'S OWN KIND is the correct cut
            # -- H-71 is about OFFICES, offices are held through `hold` Tenures, and `hold` is
            # already `_ch_document_key`'s own restriction for reading a live Tenure by its two
            # ends (`epistemic.py`, `_ch_document_key`: `t.kind == "hold" and t.subject == pid and
            # t.object == c.subject`) -- a search rather than an expansion, and keyed on the OBJECT
            # rather than the Tenure's own id, so it is a related read on the same restriction
            # rather than the identical operation. A `commit`/`oblige`/`succeed`/`tie`/`knot`
            # closure still deposits the Tenure's own opaque id, unchanged from before this row --
            # the safe default, and correct: nobody has ruled those witnessable in this form.
            for s in _hold_tenure_ends(w, c.subject):
                _add(s)
        # ⚠ **AND WHAT THE ACT NAMED, WHICH IS THE HALF THAT WAS MISSING.** An Event that wrote
        # nothing has an empty `changes[]`, so every claim deposited from one was minted about
        # **the actor** — by the `or [anchor]` fallback below (it read `or [e.subject]` until G1b
        # deleted the field), the anchor being the actor for anything the fold emits. §F1's Q2 admits a claim whose subject is the holder or
        # something the holder holds, so *a claim about the actor can never raise a listener's
        # question*: the news arrived in a form nobody could act on. Measured before this line
        # existed: `R3` = 0 of 30 on the NPC lane, 0 of 59 on ARC.
        #
        # ⚠ **THE RULE IS ABOUT WRITE-NOTHING EVENTS, NOT ABOUT `tell`, AND SAYING OTHERWISE WAS
        # AN OVERCLAIM A CRITIC BROKE.** The first writing of this comment quoted Reading 07 §3 —
        # *"the `tell` chain is the only transport"* — as though this line served `tell` alone. It
        # does not: it fires for every verb with `writes: []` (`speak`, `comply`, `dispatch`,
        # `evade`/`defy`, `construe`, the investigation acts), for `contest.resolved`, and for
        # every refusal. That is **correct and it is a different carrier**: Reading 07 §5 names
        # three, and the first is PRESENCE — *you were there*. A speech changes nothing and is
        # still witnessed, and what a witness learns is what was spoken ABOUT. Transport is what
        # reaches somebody who was NOT there, and that is still `tell` alone.
        #
        # ⚠ **AND THE CASCADE IS WORTH NAMING, BECAUSE IT EXPLAINS THE MEASUREMENT.** `speak` has
        # no precondition; `_req_tell` requires the teller to hold a claim on the subject. So a
        # witnessed speech about a proposition deposits the very claim `tell` needs, and `tell`
        # then executes *because* `speak` seeded it. The propagation this closes runs through
        # both, not through `tell` by itself.
        #
        # ⚠ **REFUSALS PROPAGATE TOO, AND THAT IS A DESIGN QUESTION NOBODY HAS RULED** — a
        # `news.untold` deposits a claim about the subject that was not told about. Registered as
        # `H-111` rather than decided here.
        # ⚠ `actor` STAYS THE DECLARED INCUMBENT and is untouched — it is the roster's control
        # arm, and this adds nothing to it.
        #
        # ⚠ **AND ONLY WHERE `changes[]` SUPPLIED NOTHING, WHICH IS NARROWER THAN THE FIRST
        # WRITING AND THE SUITE IS WHY.** Adding the act's referents to EVERY deposit inflated the
        # ledger enough that `H-40`'s decay sweep stopped being observable: the cap evicts on
        # `(confidence, recency)`, so the extra claims pushed the decayed ones out and all three
        # arms reported a minimum confidence of 100 — *"the rate is inert and this sweep is
        # measuring nothing"*, which is `ID-10` produced by a fix rather than by a bug. The
        # rationale only ever justified the empty case: an Event that wrote nothing has nothing
        # for `per_change` to find, and that is exactly where a telling lands.
        # ⚠ THE TEST IS ON `changes[]`, NOT ON `out`. Under the `both` rule `out` already holds
        # the actor, so testing the accumulator would have skipped every telling — which is the
        # case this exists for, and the first writing of this line did exactly that.
        #
        # ⚠ **AND IT REPLACES THE ACTOR RATHER THAN JOINING IT, WHICH IS BOTH THE CORRECT READING
        # AND THE ONE THAT DOES NOT PERTURB THE LEDGER.** A claim minted from a telling is about
        # WHAT WAS TOLD; the teller is not the news. Adding it as a second claim was measured and
        # rejected: it mints one extra claim per telling, the cap evicts on `(confidence,
        # recency)`, and `H-40`'s decay sweep then reported a minimum confidence of 100 in all
        # three arms — the rate made inert by a fix, which is the `ID-10` defect class arriving
        # from the direction nobody watches. One claim per witnessed Event either way, so the
        # eviction pressure this sweep measures against is unchanged.
        if not any(c.subject for c in e.changes) and any(refs or ()):
            out = [r for r in (refs or ()) if r]
    # ⚠ G1b: AN EVENT NOTHING ANCHORS IS DEPOSITED ABOUT NOTHING, NOT ABOUT `None`. With
    # `Event.subject` deleted, `anchor_of` answers `None` for an Event with no act, no change and
    # no anchored antecedent. The channel predicates already admit nobody for one, but the `total`
    # arm fans every Event to everyone, and without this line it minted `Claim(subject=None)` into
    # every ledger -- measured, 5 of 5 in `tiny_world`. `witness`'s own precedent decides it: a
    # read the instrument cannot answer (`UNKNOWN`) is NOT deposited, because the instrument's gap
    # would become a belief. No production emitter reaches this (every logged Event in the probe
    # corpus, headless and the populated realm anchors); `test_g1b_attribution.py` plants one.
    return [s for s in (out or [anchor]) if s is not None]


# ---------------------------------------------------------------------------
# `W6` -- THE FIVE WITNESS CHANNEL PREDICATES. `H-33`.
#
# ⚠ WHY THIS IS AN INJECTION AND NOT A READING. #353 §20 NAMES the five channels and gives none
# of them a predicate; `S61` states the consequence in terms -- *"WITNESS AS SPECIFIED FANS EVERY
# EVENT TO EVERY PERSON. Nothing said in private is private. A wrapper does not fix this and must
# not be presented as fixing it."* `H-33` is graded `assumption` for that reason and its sweep is
# `total / presence-only / all five`. `total` is the default AND the control, because the control
# has to be the design as written.
#
# ⚠ AND EVERY PREDICATE IS COMPUTED FROM WORLD STATE. §19.3 removes `target` from the Event and
# says why: *"observers are computed at WITNESS from presence; THE EMITTER DECLARES NO
# RECIPIENT."* A channel that needed the emitter to name someone would be a different design.
#
# ⚠ WHY THIS BECAME URGENT RATHER THAN OPTIONAL. `PLAN.md` §1.4 hole 16: `D22` (MATTER emits per
# write) and `H-33` (fan-out total) are *"individually fine and JOINTLY FATAL"*, and `W4` made
# that real -- events per run went 207 -> 896 -> 3389 over two, three and four seasons, ledgers
# pinned at the `L = 200` cap, and the test suite stopped finishing. The plan predicted it as an
# argument; it arrived as a measurement.
# ---------------------------------------------------------------------------

def _event_place(w: "World", e: "Event") -> Optional[str]:
    """The rung an Event happened at, derived from its subject.

    ⚠ A PERSON IS ASKED BEFORE A RUNG, AND THE ORDER IS THE WHOLE OF THIS FUNCTION'S CORRECTNESS.
    The first version tested `e.subject in w.rungs` FIRST — and `probes.py` gives every person a
    same-id `person`-kind Rung, so for a person-subject Event this returned the person's own rung
    and `Query.presence` then answered *"who is contained IN p_high"*, which is nobody. Under the
    `presence_only` arm that excluded THE SPEAKER AND EVERYONE STANDING IN THE ROOM, and `P15`
    read the resulting empty set as a channel predicate excluding people. It was a channel BROKEN
    CLOSED, and `P15`'s only assertion (`narrow < total`) could not tell the two apart — §0.1 pt 2.
    **THIS IS A REPEAT.** `witness`'s own rev-2 retraction records the identical conflation:
    *"because every person has a `person`-kind Rung, made almost every Event private to its own
    subject"*, and `PLAN.md` §D4 names it as a standing hazard. Found by the `W6` adversarial
    pass."""
    # G1b. THE LOOKUP ORDER IS UNCHANGED AND THE HAZARD NOTE ABOVE STILL BINDS -- only the
    # SOURCE of the id moved, from the overloaded field to `anchor_of`, which returns the same
    # value on every event measured. Person-before-rung remains the whole of this function's
    # correctness.
    anchor = anchor_of(w, e)
    if anchor is None:
        return None
    if anchor in w.persons:
        for t in w.tenures:
            if t.kind == "contain" and t.subject == anchor and t.live:
                return t.object
        return None
    if anchor in w.sites:
        return getattr(w.sites[anchor], "rung", None)
    if anchor in w.rungs:
        return anchor
    for t in w.tenures:
        if t.kind == "contain" and t.subject == anchor and t.live:
            return t.object
    return None


def _ch_co_located(w: "World", e, pid) -> bool:
    """⚠ READS THE BARRIER'S PRESENCE INDEX, WHICH IS WHAT MAKES THE CLAIM ABOUT IT TRUE. `W6`
    published *"the presence index this barrier has always built was UNUSED until this line"* while
    this function called `Query.presence` DIRECTLY, rebuilding the answer with a full `w.tenures`
    scan for every (event, person) pair. The index stayed unused and the claim was false — which is
    the failure `shape.py`'s own fidelity rule names: *a false claim of enforcement is worse than
    none, because it stops the next reader from checking.* It is also where the narrow arm's cost
    went. `cache_at_barrier` is safe here because the fan is built BEFORE `witness` enters its
    parallel map. Found by the `W6` adversarial pass."""
    place = _event_place(w, e)
    if place is None:
        return False
    index = cache.presence_index(w)
    return pid in index.get(place, ())


def _ch_document_key(w: "World", e, pid) -> bool:
    """⚠ THIS COULD NEVER FIRE ON AN ACT, AND THE REPAIR IS TO READ `changes[]` (`R8.4`).

    It tested `t.object == e.subject`. Every fold-emitted Event sets `subject = a.actor` on the one
    path every act-emission takes (`shape.py::SeasonDriver::_fold::ev`), and no `hold` Tenure takes
    a PERSON as object. So the equality could hold only where an Event's subject was ITSELF the
    held thing, which is
    `MATTER`/`CALENDAR` kinds alone: those carry no verb and no actor. **`R5`'s bureaucratic
    channel was unreachable on acts -- not underused, unreachable**, and `R5` names three of the
    five channels bureaucratic rather than memorial.

    ⚠ A `hold` IS NOT ONLY OVER A RECORD OR AN OFFICE, and an earlier writing of this docstring
    said so and was wrong. `hold` over a RUNG is built all over the tree (`probes.py:991,998`;
    Part E's own `hold:<store>` eligibility cell). `tenure_kinds` declares no object type at all.
    The load-bearing half survives the correction -- no `hold` takes a PERSON as object, which is
    what makes the old predicate unsatisfiable on an act -- but the enumeration was false and the
    repair's reach is wider than it claimed. Found by the adversarial pass.

    MEASURED before the repair, Carin's world at seed 0, two seasons, the `all_five` arm: the
    predicate returned True for **1** (event, person) pair -- on `term.matured`, whose subject IS
    the record. Not one act. ⚠ Count the predicate EXHAUSTIVELY, not through `observers_for`: that
    function's `any(...)` short-circuits per person, so once `co_located` matches, later channels
    are never called and every count taken through it under-reports.

    THE OPERAND IS `changes[]` AND NOTHING IS ADDED TO CARRY IT. `H-79` already established that an
    act names what it wrote there, and `claim_subjects` already reads it to say what a deposit is
    ABOUT; this asks the same primitive who was WATCHING. `PLAN.md` §8.1 forbids an `actor` or
    `target` field on `Event` and this needs neither.

    ⚠ WHY A REPLACEMENT AND NOT A UNION -- BY CONSTRUCTION, WITH ONE NAMED CARVE-OUT. The first
    writing of this paragraph rested the decision on ONE SEEDED RUN, which is the weaker argument
    and was available in the stronger form. Structurally: `write()` and `term.matured` both put
    their subject into `changes[0]`, so NEW is a superset of OLD wherever they fire at all; every
    fold-emitted Event and every refusal has a PERSON subject, where OLD never fired. **The one
    exception is `condition.band_crossed` (emitted in `shape.py::SeasonDriver::matter`), which
    carries `subject = <Site>` and `changes = []`** -- a person holding that Site would satisfy OLD
    and not NEW. No `hold` over a
    Site exists anywhere in the tree, so the union would admit nobody today; the carve-out is named
    rather than hidden, because a Site-hold is not forbidden and this line is what would break.
    Found by the adversarial pass, which was right that a measurement was standing in for a proof.

    ⚠ THE CHANNEL DOES REACH A NON-AUTHOR TODAY, AND AN EARLIER WRITING OF THIS DOCSTRING DENIED
    IT. It said *the channel still fires for nobody but the author*, which is true of Carin's world
    -- she holds no rung -- and FALSE OF THE MECHANISM. `_eff_transfer` names both rungs (G4: as
    the subjects of its `Change`, where it returned `[src.id, dst.id]`), the gate mints a receipt
    subjected to each RUNG that moved, and the fold puts them on the Event. EXECUTED on `tiny_world`: with `p_other` holding `S` and acting, and `p_low` holding
    the destination `Hh`, `transfer.made` carries `changes=['S','Hh']` and `document_key` returns
    True for `p_low` -- **a non-author, witnessing an act, through the bureaucratic channel**. That
    is `R5` reachable, which is what this repair was for, and it under-reported itself. Found by the
    adversarial pass; pinned by `test_r8_4_document_key_reaches_a_non_author_through_a_store`.

    ⚠ WHAT THIS DOES **NOT** FIX, STATED HERE SO IT IS NOT READ AS FIXED: `H-84`, and it is now
    narrower than the sentence above once made it sound. No verb in the resolvable vocabulary moves
    a RECORD to another person, so the only person holding a Record is still its maker. The STORE
    route above is open; the RECORD route is not, and `PHASE 1` step 1's own falsifier is written
    about Records. That is a PRODUCER hole with its own row and its own owner (*Part E -- the verb
    that would do it*), and `H-84` forbids in terms inventing a `give_record` here to make a case
    pass. Nothing was invented.

    ⚠ AND ONE INTERACTION THIS DOES NOT SETTLE, BECAUSE IT IS `PHASE 1` STEP 3's. A channel decides
    WHO witnesses, not WHAT they learn. Composed with the deposit layer as it stands -- `observers_for`
    discards which channel admitted a person, and `claim_subjects` under the default `both` rule
    starts from the Event's anchor, the actor -- a `document_key`-only witness learns WHO ACTED. `R8.5`
    cites a ratified line pointing the other way (*"a document holder saw only that the document
    changed"*). ⚠ WHEN THIS DOCSTRING WAS FIRST WRITTEN, ON THE PROTOTYPE, IT SAID THAT LINE
    *"lives on unmerged PR #371, not in this tree"*. That is no longer true of THIS file: #371 was
    adopted and `engine/season/` is the tree, so the ratified line and the mechanism it constrains
    now sit in one place. ⚠ THE `seen` CLAIM NOW SUPPLIES THE ASYMMETRY (`R8.1`, `seen_of` below):
    a `document_key`-only witness is shown no term at all -- *only that the document changed* --
    (`rosters.yaml: observation_terms.supplied_by`). The event-kind deposit above it is unchanged and still names
    the actor under `both`, so the attribution leak this paragraph describes survives on THAT
    claim; `seen` is added beside it, as `R8.1` rules, not in its place.
    """
    return any(t.kind == "hold" and t.subject == pid and t.object == c.subject and t.live
               for c in e.changes if c.subject
               for t in w.tenures)


def _ch_witness_key(w: "World", e, pid) -> bool:
    # G1b. The witness key is the Event's anchor -- the actor where one acted, the written thing
    # otherwise. Same value as the field it replaces; see `state/attribution.py` for the control.
    anchor = anchor_of(w, e)
    if anchor is None:
        return False
    if pid == anchor:
        return True
    return any(t.kind == "knot" and t.live and pid in (t.subject, t.object)
               and anchor in (t.subject, t.object) for t in w.tenures)


def _ch_post_remit(w: "World", e, pid) -> bool:
    """⚠ THIS COULD NEVER RETURN `True`. It compared `t.object` -- AN OFFICE ID -- against a set of
    REMIT ACT NAMES, and fell back to `getattr(t, "remit", None)` on a `Tenure` that has no such
    field. So `off_duke` was tested against `{"issue"}` and `None` against `{"issue"}`, and a
    channel that admits nobody in every possible world was reported as one of five carrying a
    predicate.

    ⚠⚠ THIS PARAGRAPH SAID *"the correct lookup ALREADY LIVES ONCE, in `_eligible`"*, AND THAT
    BECAME FALSE ON 2026-09-18 — in the commit that closed `H-71`, which did not come back and
    amend it. ~~There are now THREE readings of *does this holder have this remit* over TWO
    stores: this site and `loop/resolve.py:56` read the live `w.offices[...].remit_acts`, while
    `decision/options.py` reads the SNAPSHOT on the `hold` Tenure (`Tenure.granted_acts`, written
    by `World._grant_remit` at `add_tenure`). They agree today and are not guaranteed to: a hold
    opened BEFORE its office exists gets an empty snapshot and is never revisited, so the person
    side refuses while both world-side readings admit; and any future write to `Office.remit_acts`
    is a silent no-op person-side — §0.1 pt 1's read/write asymmetry, with no guard shipped.~~
    **CLOSED 2026-09-26, position `13e`.** The three readings are now ONE STORE, though still
    three call sites that each ask it independently (this site, `loop/resolve.py`'s `_eligible`,
    and `decision/options.py`) — a further §8 move a later reader may make, not claimed here: this
    site and `_eligible` both admit on `t.granted_acts` (`remits & set(t.granted_acts)` here,
    `arg in t.granted_acts` there) — the same store `decision/options.py` already read — and the
    `w.offices.get(t.object)` lookup that made each a live-world reading is deleted from both. The
    read/write asymmetry this paragraph named is gone with it: the only readers of
    `Office.remit_acts` left in `engine/season/`'s non-test code are `_grant_remit`,
    `Office.__post_init__` and `_eff_establish` (an AST scan in `test_governance_build.py`'s `13e`
    section pins that set over the package, excluding `tests/`).

    ~~⚠ THE CONSOLIDATION IS SCHEDULED, NOT FORGOTTEN: position `13e` of
    `workplans/2026-09-18-governance-settlement-behaviour-plan.md` routes this site and `_eligible`
    onto `t.granted_acts`; `13f` gates it, because whether a remit change reaches SITTING holders
    (snapshot) or only future ones (mirror) is undecided and arrives with `establish`'s effect.~~
    **DONE 2026-09-26.** `13f` (2026-09-25) landed first and settled the gating question —
    `establish` re-stamps every live `hold` on the office it writes, so a remit change reaches
    sitting holders by an ACT and not by a hand-mutation — and `13e` then routed both readings
    above onto the snapshot that decision established. THREE structurally independent read-only
    review lanes had rediscovered this separately before either position landed, which was §10's
    rank-by-independent-rediscovery signal rather than three copies of one opinion. The original
    W6 finding above stands; it is the §8 lesson this file then had to relearn.

    Found by the `W6` adversarial pass."""
    remits = {x.split(":", 1)[1] for r in VERB_TABLE.values() if e.kind in (r.emits or ())
              for x in (r.eligibility or ()) if x.startswith("remit:")}
    if not remits:
        return False
    for t in w.tenures:
        if t.subject == pid and t.kind == "hold" and t.live:
            if remits & set(t.granted_acts):
                return True
    return False


def _ch_chronicle(w: "World", e, pid) -> bool:
    """The matter-of-record channel: what a binding decision emits is public.

    ⚠ THIS DOES NOT READ `pid`, AND SAYING SO IS THE HONEST DESCRIPTION. It is an EVENT-KIND
    FILTER, not a per-person predicate: when it fires it fires for everyone alive, so it is
    `total` conditioned on kind. That is a defensible thing for a PUBLIC channel to be -- a matter
    of record is public to everyone by definition -- but the justification published with `W6` was
    that `chronicle` is *"deliberately not `everyone`"* and that this is what keeps `all_five`
    distinct from `total`. **That reasoning was wrong.** What keeps them distinct in the measured
    run is that `chronicle` matches NOBODY: the eight `binding_decision` verbs all have prose
    `requires:` and none is in `REQUIRES_PREDICATES`, so `resolvable_verbs()` excludes every one
    of them, and the MATTER/WITNESS kinds appear on no verb's `emits:` at all. The `any(...)` is
    over an empty generator for every Event the fold can currently produce.
    So the whole of `all_five - presence_only` is `document_key`. Recorded rather than papered
    over, and the register carries it as the reason `H-33`'s `all_five` arm is not yet a
    measurement of five channels. Found by the `W6` adversarial pass."""
    return any(r.stratum == "binding_decision" for r in VERB_TABLE.values()
               if e.kind in (r.emits or ()))


# ⚠ BUILT FROM THE ROSTER, NOT TYPED HERE. The first version was a dict literal mapping five
# channel names to five functions -- A ROSTER OF NAMES IN A PYTHON BODY, which is exactly what
# Jordan ruled against on 2026-09-02 (*"I do not want definitions etc to be hardcoded"*) and what
# `test_jordan_no_definition_is_hardcoded_in_a_body` exists to catch. It caught it. The names live
# once, in `rosters.yaml`; the functions are looked up by a derived name, so adding a channel is a
# data edit plus a function, and a channel with no function RAISES at import rather than silently
# never matching.
CHANNEL_PREDICATES = {}
for _c in sorted(WITNESS_CHANNELS):
    _fn = globals().get(f"_ch_{_c}")
    if _fn is None:
        raise Unspecified(
            f"channel {_c!r} is in the roster and has no `_ch_{_c}` predicate", "H-33",
            needs=f"define `_ch_{_c}(w, e, pid)`",
            law="a named channel with no predicate is the S61 debt wearing a roster entry -- an "
                "absent predicate must REFUSE, never quietly match nobody")
    CHANNEL_PREDICATES[_c] = _fn
del _c, _fn


def live_channels(mode: str) -> tuple:
    """Which channels are LIVE under a fan-out mode -- the one owner of that dispatch.

    ⚠ EXTRACTED FROM `observers_for` FOR `R8.1`, NOT WRITTEN BESIDE IT. The `seen` deposit asks
    *which channels admitted this witness* in order to know what they saw, and that is the same
    mode -> channel-set dispatch `observers_for` makes to decide WHETHER they saw. Two copies of it
    would drift the day a fourth arm lands (§8), so both callers ask here.

    `total` returns every channel, and neither caller consults them under that arm: `observers_for`
    admits everyone, and `seen_of` shows every witness every term (see there for why).

    ⚠ THE ARM NAMES ARE DATA (`rosters.yaml: fan_out_modes`), NOT LITERALS HERE. They were
    literals in the dispatch below until 2026-09-16 -- enforced, because the old `else` refused
    correctly, but not DEFINED where Jordan's 2026-09-02 ruling puts a definition. The two
    refusals below are DIFFERENT failures and that is the point: the first says a caller named an
    arm the sweep does not declare, the second says THE ROSTER GREW AND THIS FUNCTION DID NOT --
    the data/code drift a single combined check cannot see."""
    require_member(
        mode,
        FAN_OUT_MODES,
        f"fan-out mode {mode!r} is not one of H-33's declared sweep points",
        "H-33",
        law="H-33's sweep is declared in `rosters.yaml: fan_out_modes`. A mode outside it "
            "that fell back to `total` would make every reading of this sweep report the "
            "control")
    if mode in ("total", "all_five"):
        return tuple(WITNESS_CHANNELS)     # the names live once, in `witness_channels`
    if mode == "presence_only":
        return ("co_located",)
    raise Unspecified(
        f"fan-out mode {mode!r} is DECLARED in `fan_out_modes` and this function does not "
        f"dispatch it", "H-33",
        needs="give the new arm its channel selection here, beside the other three",
        law="`04 §B.13` ID-12 -- a declared row that reaches no code is the defect the "
            "loader's cross-validation exists to catch. A roster may grow; a dispatch that "
            "silently ignores the growth would run the new arm as whatever fell through")


def observers_for(w: "World", e: "Event", mode: str, everyone: list) -> list:
    """Who witnesses this Event, under the fan-out mode `H-33` declares.

    `total` is the specified behaviour and the sweep's control. The other two arms are the hole's
    own sweep points. A mode outside the three REFUSES -- an unrecognised mode silently falling
    back to `total` would make every measurement of this sweep read the control. The refusals and
    the mode -> channel dispatch live in `live_channels`, which the `seen` deposit shares."""
    live = live_channels(mode)
    if mode == "total":
        return list(everyone)
    return [pid for pid in everyone
            if any(CHANNEL_PREDICATES[c](w, e, pid) for c in live if c in CHANNEL_PREDICATES)]


# ---------------------------------------------------------------------------
# `R8.1` -- THE `seen` CLAIM: WHAT A WITNESS SAW, EACH TERM INDEPENDENTLY UNKNOWABLE.
#
# Jordan: *"a way for someone to say 'I don't know the description of the person who did x' and
# 'someone looking like y did x'"* ... *"I saw this person doing y, but I don't know what y is"* ...
# *"they saw someone skulking around for no reason they could discern"*. The event-kind deposit in
# `loop/witness.py` hands every witness the engine's own verb token (`predicate = e.kind`) and no
# actor or motive slot at all -- perfect knowledge of WHAT, no capacity for WHO or WHY. The `seen`
# claim sits BESIDE it and the observation deposit, replacing neither.
#
# ⚠ ONE STRUCT, NOT ONE CLAIM PER TERM. `R8.2` records the per-term "sighting" shape and why
# adjudication broke it: a sighting id is neither a person id nor a Tenure object, so it can never
# raise `questions_for`'s Q2 and would sever the one live propagation route. *"The sighting term
# earns its own id at the commit that builds a recognition or inference producer, and not before."*
# Do not split this struct until that producer exists.
#
# ⚠ THE SUBJECT IS WHAT CARRIES IT, AND IT IS THE LOAD-BEARING HALF. `seen_subject` returns the
# changed thing, else the RUNG the Event happened at. Q2 fires on `c.subject in mine`, and a
# person's live `contain` Tenure has the RUNG as its object -- so a `seen` claim about a rung
# raises Q2 for every witness standing in it, through machinery that already existed.
#
# ⚠ WHAT THE STRUCT COSTS, STATED RATHER THAN DISCOVERED: per-term contestability. A second
# witness's `marks` cannot contradict a first witness's `who`, and a later inference must REPLACE
# the struct (`LedgerReader`'s newest-wins) rather than layer beneath it.
# ---------------------------------------------------------------------------

SEEN_PREDICATE = OBSERVATION_DEPOSIT.get("predicate")
if not isinstance(SEEN_PREDICATE, str) or not SEEN_PREDICATE:
    raise Unspecified(
        "`observation_terms.deposit.predicate` is absent or not a name", "R8",
        needs="name the predicate the `seen` claim is deposited under",
        law="Jordan 2026-09-02 -- a definition is data. A deposit with no declared predicate "
            "would have to spell one in a body")


@dataclass(frozen=True)
class Seen:
    """`R8.1`'s value -- `Claim.value` for a `seen` claim. Every term `None` where the channel
    withholds it; `marks=()` is *shown, and nothing describable*, which is not the same as `None`.

    FROZEN AND HASHABLE ON PURPOSE: `marks` is a tuple, so the struct can sit in the sets the
    corpus harness builds over `(subject, predicate, value)`, and the told channel's exact-triple
    guard compares it with `==`. ⚠ AND `==` IS WHOLE-VALUE, so `agreement()` would score two
    witnesses who agree on `who` and differ on `marks` as DISAGREEING -- `R8.3`'s stated price of
    deferring the per-term split. Today that price is not paid: `agreement` pairs only
    `person_predicates`, and `seen` is not one.

    The field names ARE `rosters.yaml: observation_terms` -- checked at import below."""
    stratum: Optional[str] = None
    marks: Optional[tuple] = None
    who: Optional[str] = None
    why: Optional[str] = None


if tuple(f.name for f in _dc_fields(Seen)) != tuple(OBSERVATION_TERMS):
    raise Unspecified(
        f"`Seen`'s fields {[f.name for f in _dc_fields(Seen)]} are not "
        f"`observation_terms` {list(OBSERVATION_TERMS)}", "R8",
        needs="edit the roster and the struct together; the roster is the definition",
        law="R8.1 -- the struct IS the roster. A term in one and not the other is either a term "
            "no witness can hold or a field nothing declares")


def _term_stratum(w: "World", e: "Event", act) -> Optional[str]:
    """The coarse WHAT -- the acted verb's stratum, never the verb TOKEN. Case 3's *doing something
    I can't name*. An actorless Event (MATTER, CALENDAR) has no verb and so no stratum.

    ⚠ NEVER THE TOKEN, NOT NEVER THE INFORMATION -- FOUND BY ADVERSARIAL REVIEW. `movement` has
    exactly one member, `move` (`data/verbs.py`'s table), so a witness shown `stratum="movement"`
    can infer the verb with certainty even though the string differs from it. The mitigation is
    that the event-kind claim beside this one already names `e.kind` under `both`/`per_change`
    (`claim_subjects`), so this term is not the leak's only source; it is not a leak this term
    closes for a bijective stratum, which R8.5's *"someone was doing something social"* example
    (a stratum with several members) does not have to contend with."""
    row = VERB_TABLE.get(getattr(act, "verb", None)) if act is not None else None
    return getattr(row, "stratum", None)


def _term_marks(w: "World", e: "Event", act) -> Optional[tuple]:
    """The actor's appearance. ⚠ CORRECTED post-port: `Person.marks` was DELETED 2026-09-24
    (`ED-IN-0261` item 1) as a zero-reader/zero-writer field — the same fact `R8.4` recorded
    while the field still existed. There is now no carrier at all, so this reads nothing rather
    than a deleted attribute; the value is unchanged (`()` for every actor), only the reason."""
    actor = w.persons.get(act.actor) if act is not None else None
    return () if actor is not None else None


def _term_who(w: "World", e: "Event", act) -> Optional[str]:
    """The actor. An actorless Event has nobody to see."""
    return act.actor if act is not None else None


def _term_why(w: "World", e: "Event", act) -> Optional[str]:
    """ALWAYS `None`, AND THAT IS A SCOPE DECISION, NOT AN IMPOSSIBILITY. `R8.4` says the engine
    *"forgets the motive before the act executes"*, and that overstates it: `Candidate.why` is
    dropped at `pack_scenes`, but the question that occasioned an act survives one hop away --
    `Act.scene` names the Scene, the driver's `scenes[...]` holds it, and `Scene.occasion.source`
    is the question source (the same lookup `loop/resolve.py`'s `_occasion_ids` makes). It is not
    on the Act, and these readers take `(w, e, act)` with no driver, so recovering it means
    passing the Scene in -- and deciding what a witness may infer of a motive is its own unit of
    work. No channel lists `why` in `supplied_by` today (`total` shows every term, and gets this
    `None`); the reader exists so the roster's term has a declared owner."""
    return None


# ⚠ BUILT FROM THE ROSTER, LIKE `CHANNEL_PREDICATES`: a term with no `_term_<name>` RAISES at
# import rather than silently reading `None`.
TERM_READERS = {}
for _t in OBSERVATION_TERMS:
    _fn = globals().get(f"_term_{_t}")
    if _fn is None:
        raise Unspecified(
            f"observation term {_t!r} is in the roster and has no `_term_{_t}` reader", "R8",
            needs=f"define `_term_{_t}(w, e, act)`",
            law="a term no reader can fill would be `None` for every witness forever, which is "
                "indistinguishable from a channel honestly withholding it")
    TERM_READERS[_t] = _fn
del _t, _fn

# ⚠ `supplied_by` IS KEYED ON EXACTLY THE FIVE CHANNELS AND NAMES ONLY DECLARED TERMS. A channel
# missing from it would show nothing by omission -- the silent-empty `rosters.yaml`'s header
# forbids -- and a term outside `observation_terms` would be a field `Seen` does not have.
if set(TERMS_SUPPLIED_BY) != set(WITNESS_CHANNELS):
    raise Unspecified(
        f"`observation_terms.supplied_by` keys {sorted(TERMS_SUPPLIED_BY)} are not the witness "
        f"channels {sorted(WITNESS_CHANNELS)}", "R8",
        needs="give every channel a row, `[]` if it shows nothing",
        law="R8.1 -- each term is None WHERE THE CHANNEL WITHHOLDS IT, which needs every channel "
            "to say what it shows")
for _c, _terms in TERMS_SUPPLIED_BY.items():
    if not isinstance(_terms, list) or not set(_terms) <= set(OBSERVATION_TERMS):
        raise Unspecified(
            f"`observation_terms.supplied_by.{_c}` is {_terms!r}, not a list of "
            f"{list(OBSERVATION_TERMS)}", "R8",
            needs="list only declared terms",
            law="R8.1 -- the struct's terms are closed")
del _c, _terms


def seen_subject(w: "World", e: "Event", pid: str, mode: str) -> Optional[str]:
    """`R8.1`: the changed thing when there is one, else the rung the Event happened at -- and
    where the Event changed SEVERAL things, the one THIS WITNESS holds.

    ⚠ PER-WITNESS, AND THE FIRST WRITING WAS NOT. It took the first non-empty `changes[]` subject
    for everyone, so a `transfer` (`changes = [src, dst]`) gave the DESTINATION'S holder a claim
    about the SOURCE -- a rung not in their live Tenure objects, on which Q2 can never fire. The
    channel that admitted them (`document_key`) admitted them BECAUSE they hold `dst`. So: the first
    changed thing among `pid`'s live Tenure objects (the same set `questions_for` calls `mine`,
    read the same way -- `w.persons[pid].tenures`, not a fresh scan of `w.tenures` filtered by
    subject, which is `O(fan size x |w.tenures|)` over a barrier's whole fan instead of the one
    person's own list), else the first changed thing, else the rung. Still one claim per
    (witness, event).

    ⚠ AND EACH CHANGED SUBJECT PASSES THROUGH `_hold_tenure_ends` FIRST, FOR THE SAME REASON
    `claim_subjects` ALREADY DOES (`H-71`). A `confer`/`revoke`/`release` on a `hold` Tenure
    reports the Tenure's OWN opaque id in `changes[]` -- correct as a Receipt, unwitnessable as a
    subject, since no live Tenure has a Tenure's id as its `object`. Found by adversarial review:
    the first `seen` writing deposited that raw id, so `R8.4`'s office-conferral case could never
    raise Q2 for anyone. Expanding here keeps one answer to *what is this deposit about* shared
    with `claim_subjects` rather than two that can drift (§8).

    ⚠ EXCEPT UNDER `total`, WHICH IS UNIFORM BY DEFINITION, NOT PER-WITNESS. `total` is `H-33`'s
    control arm -- *"fans every event to every person"* IDENTICALLY -- and `seen_of` already
    special-cases it for the same reason (every term shown to everyone). A per-witness subject
    would make two co-located witnesses hold different claims under the one arm designed to be
    the uniform baseline every other arm is measured against.

    ⚠⚠ **`test_r7_two_persons_hold_different_things_and_at_total_they_cannot` DOES NOT CATCH THIS,
    AND CLAIMING IT DID WAS A DEFECT §0.1 pt 2 NAMES** (found by adversarial review, not by
    running it). `_r7_witness_claims` keeps only claims whose predicate is a logged Event kind
    (`test_season_shape.py`), and `seen`'s predicate never is one, so every `seen` claim is
    filtered out of that comparison before it runs -- deleting this whole `if mode == "total"`
    branch passes that test unchanged. The real falsifier is
    `test_r8_the_total_arm_subjects_a_multi_change_event_uniformly` in `test_seen_claim.py`, added
    beside it, which exercises a `transfer`-shaped multi-change Event under `total` and asserts
    every co-located witness gets the identical subject -- the one case this branch exists for.
    So under `total`, every witness gets the SAME subject: the first changed thing (after the
    `hold`-Tenure expansion above), else the rung -- the pre-per-witness rule, deliberately not
    personalized here.

    `None` when the Event changed nothing and has no place; then nothing is deposited, because a
    claim about nothing raises no question and occupies a ledger slot the cap evicts somebody
    else for."""
    changed = []
    for c in e.changes:
        if not c.subject:
            continue
        for s in _hold_tenure_ends(w, c.subject):
            if s not in changed:
                changed.append(s)
    if changed:
        if mode == "total":
            return changed[0]
        mine = {t.object for t in w.persons[pid].tenures if t.live}
        return next((s for s in changed if s in mine), changed[0])
    return _event_place(w, e)


def seen_of(w: "World", e: "Event", act, pid: str, mode: str) -> Seen:
    """What `pid` SAW of `e`: the union of the terms shown by every live channel admitting them.

    ⚠ EVERY CHANNEL IS ASKED, NOT THE FIRST THAT MATCHES. `observers_for` short-circuits because it
    only needs WHETHER; this needs WHAT, and a co-located knot partner is shown more than either
    channel alone would show.

    ⚠ `total` SHOWS EVERY TERM TO EVERY WITNESS. That arm is `H-33`'s control -- *"fans every event
    to every person"*, the maximal-information design as written -- so gating it on the channel
    predicates would make it a fan-out of WHO with the narrow arms' filter on WHAT, and a
    comparison against it would no longer be against the control. (`why` still reads `None`: no
    reader supplies it, see `_term_why`.)

    ⚠ AN ALL-`None` STRUCT IS RETURNED, NOT DROPPED. *Something happened here and I know nothing
    about it* is information, and it is exactly `R8.5`'s document holder (*"saw only that the
    document changed"*). An actorless Event (MATTER, CALENDAR) also yields one: no verb, no actor.
    Whether to deposit is the caller's call, on the SUBJECT alone (`seen_subject`).

    ⚠ MUST BE CALLED BEFORE `witness` ENTERS ITS PARALLEL MAP. `_ch_co_located` reads
    `cache.presence_index`, and `World.cache_at_barrier` raises `Forbidden` inside the map whether
    or not the index is already built."""
    if mode == "total":
        shown = set(OBSERVATION_TERMS)
    else:
        admitted = [c for c in live_channels(mode) if CHANNEL_PREDICATES[c](w, e, pid)]
        shown = {t for c in admitted for t in TERMS_SUPPLIED_BY[c]}
    return Seen(**{t: (TERM_READERS[t](w, e, act) if t in shown else None)
                   for t in OBSERVATION_TERMS})
