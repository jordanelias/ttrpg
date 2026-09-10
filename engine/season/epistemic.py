"""`season.epistemic` — what a person can come to KNOW, and who comes to know it.

EXTRACTED, step 6 of the decomposition (a PURE MOVE but for one call site, named below). Two
halves that belong together because they are the two ends of one channel:

  * **what is knowable** — `belief_contradicts` (§F1 clause 4, the one place a person's OWN
    ledger can refuse a candidate), and the two functions that decide what a deposit is ABOUT
    (`act_refs`, `claim_subjects`).
  * **who learns it** — `_event_place`, the five `_ch_*` witness-channel predicates, the
    `CHANNEL_PREDICATES` table built from the roster, and `observers_for`.

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

from typing import Optional

from .data.requires import binding_of, evaluate
from .data.rosters import CLAIM_SUBJECT_RULES, WITNESS_CHANNELS
from .data.verbs import NO_PRECONDITION, VERB_TABLE, VerbRow
from .gaps import Unspecified
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


def claim_subjects(e: "Event", rule: str, refs: Optional[list] = None) -> list:
    """`H-79`: what the claims deposited from one Event are ABOUT.

    `actor` is the incumbent — one claim, subject = the Event's own subject. `per_change` mints
    one per `StateChange`, subject = THE THING CHANGED, which is what makes §F1's Q2 clause
    "something they hold" reachable at all. `both` is the union.

    Order is deterministic and de-duplicated, because a person holding two identical claims about
    one Event would double-count in every eviction comparison."""
    if rule not in CLAIM_SUBJECT_RULES:
        raise Unspecified(
            f"claim-subject rule {rule!r} is not in the roster", "H-79",
            needs=f"one of {sorted(CLAIM_SUBJECT_RULES)}",
            law="#353 §20 types `Claim.subject` and never says what a WITNESS deposit's subject "
                "is; a rule outside the roster is a fourth answer nobody declared")
    out = [] if rule == "per_change" else [e.subject]
    if rule in ("per_change", "both"):
        for c in e.changes:
            if c.subject and c.subject not in out:
                out.append(c.subject)
        # ⚠ **AND WHAT THE ACT NAMED, WHICH IS THE HALF THAT WAS MISSING.** An Event that wrote
        # nothing has an empty `changes[]`, so every claim deposited from one was minted about
        # **the actor** — by the `or [e.subject]` fallback below, `e.subject` being the actor for
        # anything the fold emits. §F1's Q2 admits a claim whose subject is the holder or
        # something the holder holds, so *a claim about the actor can never raise a listener's
        # question*: the news arrived in a form nobody could act on. Measured before this line
        # existed: `R3` = 0 of 30 on the NPC lane, 0 of 59 on ARC.
        #
        # ⚠ **THE RULE IS ABOUT WRITE-NOTHING EVENTS, NOT ABOUT `tell`, AND SAYING OTHERWISE WAS
        # AN OVERCLAIM A CRITIC BROKE.** The first writing of this comment quoted Reading 07 §3 —
        # *"the `tell` chain is the only transport"* — as though this line served `tell` alone. It
        # does not: it fires for every verb with `writes: []` (`speak`, `comply`, `dispatch`,
        # `evade`/`defy`, `refract`, the investigation acts), for `contest.resolved`, and for
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
    return out or [e.subject]


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
    if e.subject in w.persons:
        for t in w.tenures:
            if t.kind == "contain" and t.subject == e.subject and t.live:
                return t.object
        return None
    if e.subject in w.sites:
        return getattr(w.sites[e.subject], "rung", None)
    if e.subject in w.rungs:
        return e.subject
    for t in w.tenures:
        if t.kind == "contain" and t.subject == e.subject and t.live:
            return t.object
    return None


def _ch_co_located(w, e, pid) -> bool:
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


def _ch_document_key(w, e, pid) -> bool:
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
    -- she holds no rung -- and FALSE OF THE MECHANISM. `_eff_transfer` returns `[src.id, dst.id]`,
    `_apply_write` turns those into `StateChange`s subjected to the RUNGS, and the fold puts them on
    the Event. EXECUTED on `tiny_world`: with `p_other` holding `S` and acting, and `p_low` holding
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
    starts from `e.subject`, the actor -- a `document_key`-only witness learns WHO ACTED. `R8.5`
    cites a ratified line pointing the other way (*"a document holder saw only that the document
    changed"*). ⚠ WHEN THIS DOCSTRING WAS FIRST WRITTEN, ON THE PROTOTYPE, IT SAID THAT LINE
    *"lives on unmerged PR #371, not in this tree"*. That is no longer true of THIS file: #371 was
    adopted and `engine/season/` is the tree, so the ratified line and the mechanism it constrains
    now sit in one place. The asymmetry is still `PHASE 1` step 3's `seen` claim to supply. Named
    here rather than built, and it is now REACHABLE rather than vacuous, which is a consequence of
    this repair and belongs in its record.
    """
    return any(t.kind == "hold" and t.subject == pid and t.object == c.subject and t.live
               for c in e.changes if c.subject
               for t in w.tenures)


def _ch_witness_key(w, e, pid) -> bool:
    if pid == e.subject:
        return True
    return any(t.kind == "knot" and t.live and pid in (t.subject, t.object)
               and e.subject in (t.subject, t.object) for t in w.tenures)


def _ch_post_remit(w, e, pid) -> bool:
    """⚠ THIS COULD NEVER RETURN `True`. It compared `t.object` -- AN OFFICE ID -- against a set of
    REMIT ACT NAMES, and fell back to `getattr(t, "remit", None)` on a `Tenure` that has no such
    field. So `off_duke` was tested against `{"issue"}` and `None` against `{"issue"}`, and a
    channel that admits nobody in every possible world was reported as one of five carrying a
    predicate.

    The correct lookup ALREADY LIVES ONCE, in `_eligible`: the tenure's object is an OFFICE, and
    the office carries `remit_acts`. Re-deriving it here was `CLAUDE.md` §8 broken one function
    apart, which is how it came out wrong. Found by the `W6` adversarial pass."""
    remits = {x.split(":", 1)[1] for r in VERB_TABLE.values() if e.kind in (r.emits or ())
              for x in (r.eligibility or ()) if x.startswith("remit:")}
    if not remits:
        return False
    for t in w.tenures:
        if t.subject == pid and t.kind == "hold" and t.live:
            off = w.offices.get(t.object)
            if off and remits & set(off.remit_acts):
                return True
    return False


def _ch_chronicle(w, e, pid) -> bool:
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


def observers_for(w: "World", e: "Event", mode: str, everyone: list) -> list:
    """Who witnesses this Event, under the fan-out mode `H-33` declares.

    `total` is the specified behaviour and the sweep's control. The other two arms are the hole's
    own sweep points. A mode outside the three REFUSES -- an unrecognised mode silently falling
    back to `total` would make every measurement of this sweep read the control."""
    if mode == "total":
        return list(everyone)
    if mode == "presence_only":
        live = ("co_located",)
    elif mode == "all_five":
        live = tuple(WITNESS_CHANNELS)     # the names live once, in `witness_channels`
    else:
        raise Unspecified(
            f"fan-out mode {mode!r} is not one of H-33's declared sweep points", "H-33",
            needs="total | presence_only | all_five",
            law="H-33's sweep is `total / presence-only / all five`. A mode outside it that fell "
                "back to `total` would make every reading of this sweep report the control")
    return [pid for pid in everyone
            if any(CHANNEL_PREDICATES[c](w, e, pid) for c in live if c in CHANNEL_PREDICATES)]
