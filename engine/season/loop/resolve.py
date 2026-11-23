"""`loop/resolve.py` -- RESOLVE -- barrier 3, the only writing step for acts, and THE FOLD (`04` T-k's one resolver: the fold lives here, once). `04 §A.2`: owns every ACTS row, through the gate, and the ordered fold; token ACTS.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.resolve = resolve`, so `SeasonDriver.resolve` IS this
function and `inspect.getsource(SeasonDriver.resolve)` returns THIS SOURCE, which the tests that
read a step's body rely on (ED-IN-0203 step 9).

⚠ **THE TOKEN IS HANDED IN BY THE DRIVER (G2).** `SeasonDriver.season` mints an ACTS `Token`
through `loop/driver.py::mint_token` and passes it as `token`, once per lap. `resolve` threads
it to `_fold` and `_fold` to `_apply_write`, each taking it as the argument after `w`; every gate
write below presents it. This module constructs none and calls no minter --
`tests/test_g2_token.py` fails if it does.
"""

from __future__ import annotations

import random
from dataclasses import replace
from ..gaps import InstrumentDefect
from ..data.rosters import (PERSON_DEMANDED, FOLD_INELIGIBLE, FOLD_REFUSED, armed_route_off, graded_route,
                            MARGIN_ENDING, SCAR_HOLDS, SCAR_SEASON_CAPS, SCAR_VINDICATIONS, STANDING_OCCASION_OPENED_BY, STRATA, UNROUTED_BAND,
                            require_member, task_share)

from typing import Any, Optional
from ..data.matrix import Step, matrix_row
from ..data.requires import UNKNOWN, Verdict, binding_from_act, evaluate
from ..data.verbs import (COUNTERPARTY_CLAUSE, DRAW_CLAUSE, ELIGIBILITY_CLAUSE, EVENT_KINDS, FORM_TASK,
                          VERB_TABLE, WRITE_CLAUSE, VerbRow)
from ..gaps import Forbidden, Unspecified
from ..loop.effects import EFFECTS
from ..loop.predicates import REQUIRES_PREDICATES
from ..loop.sides import _contests_of, sides_of     # `_contests_of` lives in sides.py (B10-08 close)
from .. import manifest
from ..epistemic import observers_for
from ..data.affiliations import engagement
from ..queries.person_q import (broken_by, confided_outside, conviction_after_crisis,
                                 elements_violated_by, pursuit_lean, upheld_by, _pursuits_upheld_by)
from engine.substrate.descriptors import AFFILIATION_CEILING
from ..queries.world_q import WorldReader, ceiling, demanded_person, occasioned_by
from ..seam import ContestError, ContestRefused, Resolution, contest, degree_of, find_trail, grade
from ..seam.ladder import is_margin_result
from ..state.carriers import Act, Event, StateChange, effort_of, subject_of
from ..state.gate import Change, NoOpReceipt, NotYours, Subject, Token, seat_hold
from ..state.containment import edges_of
from ..state.ids import SeatId, draw_factory, H
from ..state.world import World
from ..trace_log import TRACE



# -- RESOLVE -- barrier 3 -- the ONLY writing step for acts (S27) -------

def _canonical_order(w: "World", acts: list) -> list:
    """S27/S32 rest 3: FIVE STRATA, then a CONTENT-DERIVED hash key within each -- extracted
    from `resolve()`'s own sort (M4, `ED-IN-0279` clause (a)) so `loop/encounter.py` can fold a
    SUBSET of a lap's acts in the SAME canonical order, rather than re-deriving the rule or
    skipping it (§8: it lives once). No `self`: the ordering is a pure function of the world's
    seed/tick and the acts themselves, not of driver state."""
    return sorted(acts, key=lambda a: (stratum_of(a),
                                       H(w.world_seed, w.tick, a.actor, f"order:{a.verb}:{a.id}")))


def _survives(self, w: "World", a: Act) -> list:
    """S27.1: a predecessor act can remove the actor. `[]` if `a.actor` is still in `w.persons`
    -- the caller folds normally. Otherwise an `act.ineligible` Event (already registered in
    `self.act_of`) that the caller should emit INSTEAD of folding.

    Shared with `loop/encounter.py`: a predecessor's act can remove a person just as easily inside
    RESOLVE as inside an earlier act of the SAME lap's ENCOUNTER pass, and the reading is the
    fold's own rather than borrowed.

    ⚠ SC-02 `23`: THE TAG ASSERTION IS HERE, BECAUSE THIS IS THE ONE CHECK BOTH FOLD ENTRIES SHARE
    (`resolve` and `encounter` call it before anything else reads the actor). `04:222`, the Python
    column: *"STRUCTURAL under a checker; MECHANICAL at runtime"*, and `04:120` (AX-1), *"only a
    person acts; a seat enters through `Act.via`"*. It RAISES `InstrumentDefect` and does not emit
    `act.ineligible`: a seat that is not in `w.persons` would otherwise be indistinguishable from a
    person a predecessor removed, so the typed refusal is the only way to tell 'a seat tried to act' from
    'nobody is there'. The grade is RUNTIME -- CI runs no type-checker."""
    if isinstance(a.actor, SeatId):
        raise InstrumentDefect(
            f"act {a.id!r} ({a.verb}) names a SeatId as its actor: {str(a.actor)!r}. 04 §B.1 / AX-1 -- "
            "only a person acts; a seat enters through `Act.via`, and `Act.actor` is a PersonId.")
    if a.actor in w.persons:
        return []
    TRACE.decision(f"{a.actor} does not survive to act", "S27.1",
                   chose="emit `act.ineligible`; a predecessor removed the actor",
                   alternatives=["fold it anyway (the seam then sees a dead claimant)",
                                 "drop it silently (its act id never resolves)"])
    gone = _act_events(self, w, a, (FOLD_INELIGIBLE,))
    for _e in gone:
        self.act_of[_e.id] = a
    return gone


def _eligible(self, w: "World", a: Act, row: "VerbRow") -> bool:
    """§E4: eligibility admits `own`, `remit:<act>`, `hold:<object>`, `presence:<rung>` -- and
    NEVER `capability`, which the table loader already refuses. The kinds are a DISJUNCTION:
    `transfer` is eligible by `remit:issue` OR `own` OR `hold:<store>`."""
    for alt in row.eligibility:
        kind, _, raw = alt.partition(":")
        kind, raw = kind.strip(), raw.strip()
        placeholder = raw.startswith("<") and raw.endswith(">")
        arg = raw.strip("<>")
        if kind == "own":
            return True                       # every person may attempt their own acts
        if kind == "remit":
            # ⚠ ADMITS ON THE TENURE'S SNAPSHOT, NOT THE LIVE OFFICE (position `13e`).
            # `t.granted_acts` is the grant the holder actually has, the same fact
            # `decision/options.py` reads (`epistemic.py`'s `_ch_post_remit` docstring names the
            # gap a second reading would open); an office hand-mutated after seating does not
            # reach it, and an `establish` re-stamp does (`13f`).
            #
            # ⚠ G3: THE SEAT EXERCISED, NOT ANY SEAT HELD. `04:332` -- *"purview is asked of
            # the seat exercised, not the actor"* -- and `04:120`, *"a seat enters through
            # `Act.via`"*: a remit is a SEAT's, so a remit act is eligible only through the one
            # seat it names, which the actor must occupy (`seat_hold`, the gate's own test). An
            # act naming no seat (`via=None`) is the actor acting as themselves and has no remit
            # at all. `decision/choose.py` sets `via` person-side from the same grant, so a
            # COMPUTED act is admitted exactly as before; a hand-built one names its seat.
            t = seat_hold(w, a.actor, a.via)
            if t is not None and arg in t.granted_acts:
                return True
        elif kind == "hold":
            # ⚠ THE ARGUMENT IS COMPARED, as it is person-side: admitting anyone holding ANY
            # object is an over-admission, and `G4` makes that a defect of equal weight to an
            # over-refusal. A `<...>` argument is a KIND, not an id, so it cannot be matched
            # and this declines rather than guessing which store the act meant (`H-75`).
            mine = [t for t in edges_of(w, "hold", a.actor) if t.until is None]
            if not raw:
                if mine:
                    return True
            elif not placeholder:
                if any(t.object == arg for t in mine):
                    return True
            else:
                TRACE.note(f"`hold:<{arg}>` names an object KIND, not an id (H-75); "
                           f"{row.verb!r} declines rather than admitting on any held object")
        elif kind == "presence":
            # ⚠ NOT `return True`. What declines the branch is `H-75`: the argument is a
            # PLACEHOLDER naming a kind of rung, not an id, so there is nothing to look up -- and
            # admitting on an unevaluable predicate is a SILENT FILL off the register (G1) at the
            # opposite polarity to §42.2, which sends zero evidence to the verdict AGAINST. It
            # refuses, and says which hole.
            #
            # It does NOT raise, because eligibility is a DISJUNCTION: `work` is `own |
            # presence:<site>` and `own` already admits, so raising here would refuse acts the
            # design permits. This branch declines and the loop tries the next alternative.
            TRACE.note(f"`presence:` eligibility is unevaluable (H-75, its argument names a kind of rung, "
                       f"not an id); declining this alternative for {a.verb}", "H-75")
            continue
    return False

def _occasion_ids(self, w: "World", a: Act) -> list:
    """The antecedent Event ids for an act, via the Scene that carried it.

    ⚠ **AN ACT WITH NO SCENE HAS NO OCCASION, AND THAT IS NOT A DEFECT.** `as_scenes` still
    admits a bare `Act` as a one-interaction scene (the pre-`W17` accounting), and a
    hand-authored act in a test or a probe never went through DELIBERATE at all. Those
    genuinely have no question behind them, so they get nothing added and keep `[a.id]` —
    which is the honest answer, not a fallback.

    ⚠ **AND IT NEVER RETURNS THE ACT'S OWN EVENT.** The ids here are antecedents already in
    the log when the act folds; an Event cannot cause itself, and `causes[]` must name ids
    that exist."""
    sc = w.acts.scene_of(a.id)                    # B09.16: the Scene is kept beside its acts, not on the driver
    if sc is None:
        return []
    occ = getattr(sc, "occasion", None)
    # Batch B-I close (F1): AN ACT ON A CLASSED REFERENT ANSWERS THE STANDING OCCASION, NOT THE
    # QUESTION IT RODE ON. A vacancy, a seat told of or a writ held is stamped onto whatever
    # question the person answers (`queries/world_q.py::questions_for`, IN-53 D1), so that
    # question's own occasion -- a `claim_landed` question's originating Event -- is unrelated to
    # an act formed on the classed referent. Such an act gets `[ROOT]`, as a Q4 `need` does (plan
    # IN-53 step 3); one whose subject is ALSO a plain referent keeps the question's occasion.
    #
    # B09.12 (H-457): THE STANDING OCCASION HAS AN OPENING EVENT, AND THAT EVENT IS THE ACT'S REASON. The question's occasion
    # is still unrelated, but the vacancy, writ, wound or detention the act answers was opened by an Event the log holds: the
    # first kind `rosters.yaml: standing_occasion_opened_by` lists for the referent's class that was WRITTEN about it
    # (`World.last_emission_of`, the chaining primitive MATTER's clocks use). ONE id at most, so `causes[]` does not fan; none
    # where the log holds none (a seat vacant since the build). `standing_occasion_cause` False is the control: `[]`.
    subj = subject_of(a)
    if (subj and subj not in getattr(occ, "referents", ())
            and any(r == subj for r, _ in getattr(occ, "classes", ()))):
        if not w.fixtures.get("standing_occasion_cause"):
            return []
        cls = next(c for r, c in occ.classes if r == subj)
        for kind in STANDING_OCCASION_OPENED_BY.get(cls, ()):
            eid = w.last_emission_of(kind, subj, written=True)
            if eid is not None and eid != a.id:
                return [eid]
        return []
    return [c for c in occasioned_by(w, occ) if c != a.id]

def _admits(self, w: "World", a: Act, row: "VerbRow") -> tuple:
    """§E2's FIRST TWO STEPS, FOR BOTH PATHS: eligibility, then `requires` against the world the
    predecessors left. Returns `(ok, refusal_kinds, verdict)`.

    ⚠⚠ THIS FUNCTION EXISTS BECAUSE `resolve()` ROUTES A CONTESTED ACT TO THE SEAM BEFORE `_fold`
    IS ENTERED, and §E2's order is *eligibility -> `requires` -> resolve*. Without it a contested
    act is carried into personal combat without its precondition ever being read: `opening_set`
    binds `subject` from the question's referent, usually a Record or a Rung, so the seam answers
    `PARTY-GAP` (*claimant not a person*) though the row's own precondition says the subject is a
    living person.

    ⚠ AN ORDERING, NOT A NEW RULE: the eligibility test and the `requires` evaluation below are
    `_fold`'s, moved up so the two paths share ONE owner (§8). A `_fold`-local copy of them inside
    the contest branch would be the second resolver §27.2 forbids, arriving as a guard.

    ⚠ A REFUSED CONTESTED ACT EMITS AND IS WITNESSED. It does not raise and it is not dropped:
    `emits_on_refusal` is what a reader sees, the act still cost a scene, and the distinction
    between a LOSS (the contest ran and went against you) and a REFUSAL (it never ran) is the
    one the row's degree bands were built to keep."""
    # ⚠ PLAN POSITION `19`: EVERY REFUSAL BELOW IS `row.refusal_for(<clause>)` -- `04 §C.4`'s own
    # spelling, `emit(row.refusal_for(ELIGIBILITY))` / `emit(row.refusal_for(failed_conjunct))`.
    # On a FLAT row it is `row.emits_on_refusal`; on a KEYED row (`data/verbs.py`, invariant 4's
    # per-conjunct half) it is the failing clause's own kind, so a refusal says WHICH clause
    # refused.
    if not self._eligible(w, a, row):
        TRACE.decision(f"{a.actor} is not eligible for {a.verb}", "E4",
                       chose="emit the refusal", alternatives=["raise", "silently drop"])
        return (False, _demand_earned(w, a, row.refusal_for(ELIGIBILITY_CLAUSE), False)
                or (FOLD_INELIGIBLE,), Verdict(UNKNOWN, ()))
    verdict = Verdict(UNKNOWN, ())
    if row.has_precondition:
        if row.requires_typed is not None:
            # ⚠ THE TYPED CELL, AND `is True` RATHER THAN A TRUTH TEST. `evaluate` returns
            # three values, and UNKNOWN -- an operand the act does not carry, or a question
            # the world cannot answer -- must REFUSE. §42.2's polarity: zero evidence goes to
            # the verdict AGAINST the thing measured, so an unevaluable precondition is a
            # refusal and never a silent admission (the untyped branch below has the same polarity).
            #
            # ⚠ `W-B`: THE VERDICT'S `observed` RIDES ON THE EVENT, AND THE REFUSAL'S READS
            # ARE THE INFORMATIVE ONES. `belief_contradicts` evaluates the same cell against
            # `LedgerReader`, so a claim carrying `(subject, predicate, value)` is read by the
            # same code that produced the Observation; `SeasonDriver.witness` deposits it, gated on
            # `observation_deposit_mode`.
            #
            # ⚠ ATTACHED TO SUCCESS AND REFUSAL ALIKE. A refusal's reads are WHY it refused --
            # `stores:grain -> 0` on an emptied hearth -- and it is the only read whose value
            # can make `belief_contradicts` fire, because `0 >= 1` is the one thing in this
            # grammar that evaluates False. Attaching only to the success would build the
            # channel and leave out the traffic.
            #
            # ⚠ POSITION `11a`: `S12.1`'s `floor` READ CAN RAISE HERE, AND IT MUST BE CAUGHT THE
            # WAY `PARTY-GAP` ALREADY IS BELOW (`contest()`'s call, same file) -- NAMED, NARROW,
            # AND FALLING THROUGH TO THE ORDINARY REFUSAL. `WorldReader.read`'s `floor` stem raises
            # `Unspecified("S12.1", ...)` for a site KIND with no registered band floors at all
            # (`dwelling`/`garrison` ship `{}` ON PURPOSE, `24d-i`/M4), and `reach`/`place_of`
            # (`queries/world_q.py`) make a claim about a co-located Site an ordinary
            # `claim_landed` question, so `work`'s `site` operand can bind to a dwelling. This
            # paragraph's own polarity rule decides it: `no band floors for this kind` IS zero
            # evidence, not a software defect, so it resolves to `UNKNOWN` (refusal) rather than
            # propagating. `where == "S12.1"` is this ONE raise's own tag, so a FUTURE raise
            # `WorldReader.read` might grow for a different reason is not silently swallowed with
            # it -- the same discipline `PARTY-GAP`'s own catch states for `ENGINE-UNAVAILABLE`.
            try:
                verdict = evaluate(row.requires_typed, WorldReader(w, a.actor),
                                   binding_from_act(a))
            except Unspecified as e:
                if e.where != "S12.1":
                    raise
                verdict = Verdict(UNKNOWN, ())
            ok = verdict.value is True
        else:
            pred = REQUIRES_PREDICATES.get(a.verb)
            if pred is None:
                raise Unspecified(
                    f"{a.verb!r} has a precondition the fold cannot evaluate: "
                    f"{row.requires!r}",
                    "E2",
                    needs="a typed `requires_typed:` cell, a predicate in "
                          "REQUIRES_PREDICATES, or a `requires:` the table states "
                          "structurally rather than in prose",
                    law="§E2 -- `requires` is checked IN THE FOLD. Stated as prose it is the "
                        "same defect `resolve` had, one column along: a rule the code cannot "
                        "read")
            # B09.19: a predicate that declares `clauses=` answers `(ok, clause)` and a bare-bool one `ok`. The clause rides
            # `Verdict.failed`, no `observed` reads with it (WITNESS deposits nothing new from the read itself), so a KEYED
            # predicate row emits the kind of the clause that refused and a flat row is unchanged.
            answer = pred(w, a)
            if isinstance(answer, tuple):
                ok, failed = bool(answer[0]), answer[1]
                declared = getattr(pred, "clauses", None)    # None: a wrapper or stand-in that declared nothing
                if declared is not None and failed is not None and failed not in declared:
                    raise InstrumentDefect(
                        f"{a.verb!r}'s predicate refused at {failed!r}, which it does not declare "
                        f"({list(declared)}); a name a refusal carries is one `requires_predicate(clauses=)` owns")
                verdict = Verdict(UNKNOWN, (), failed)
            else:
                ok = bool(answer)
        if not ok:
            TRACE.decision(f"{a.verb} by {a.actor}: precondition unmet", "E2/S27.1",
                           chose="emit the refusal -- scarcity falls out of the fold",
                           alternatives=["raise (no Event, no witness, no arc)"])
            # `verdict.failed` is the conjunct that decided it (`data/requires.py::evaluate`) or the clause a
            # naming predicate refused at; an unnamed cell and a bare-bool predicate carry `None`, which only a flat row reaches.
            return (False, _demand_earned(w, a, row.refusal_for(verdict.failed), True)
                    or (FOLD_REFUSED,), verdict)
    # ⚠ PLAN POSITION `14` (U7-own): THE SECOND PARTY, ASKED HERE AND NOWHERE ELSE. `ED-IN-0210`
    # ruling 1 -- *a real interaction has a COUNTERPARTY*; a row naming its `counterparty:` operand
    # is refused when the act names nobody there, or names the actor (the `Tenure(X, X)` fiat). The
    # operand is read through `binding_from_act`, the one reader of an act's payload. ASKED AFTER
    # `requires`, so every refusal a row already keys to a conjunct keeps its attribution, and only
    # an act that passed its whole precondition reaches this. `opening_set` declines the same case
    # person-side, so no computed act is ever refused here; it replaces the per-effect copy
    # `_eff_petition` carried (a petition addressed to its petitioner).
    # IN-53 D2 (H-207): the self half is waived for a row declaring `counterparty_may_be_self`
    # (`confer`: a self-conferral writes `Tenure(actor, office)`, not a self-loop); one owner of the
    # test, `VerbRow.self_counterparty_refused`, which `opening_set` asks too.
    if row.counterparty:
        other = binding_from_act(a).get(row.counterparty)
        if row.self_counterparty_refused(other, a.actor):
            TRACE.decision(f"{a.verb} by {a.actor}: no second party on `{row.counterparty}`",
                           "ED-IN-0210", chose="emit the refusal",
                           alternatives=["admit a self-relation (a fiat)"])
            return (False, _demand_earned(w, a, row.refusal_for(COUNTERPARTY_CLAUSE), False)
                    or (FOLD_REFUSED,), verdict)
    return (True, (), verdict)


# `G6` (`H-197`): declared on `tell`'s told bands; kept only when `_confidence_broken` says so.
CONFIDENCE_BROKEN = "confidence.broken"

# B10.24: declared on every row `rosters.yaml: pursuit_axes.refusable` lists; kept only when `_scruple_overridden` says so.
SCRUPLE_OVERRIDDEN = "scruple.overridden"

# B09.11: the kind `(Person, scar)` declares (`write_matrix.yaml`), emitted by `_scar_witnesses` beside its write.
SCAR_TAKEN = "scar.taken"
# B10.07: the same row's kind for a count that falls by vindication (`Fixtures scar_vindication`, `H-468`) [ASSUMPTION: the kind's name].
SCAR_HEALED = "scar.healed"
HEALED = "healed"      # the tally's marker for a vindication taken this season: `(HEALED, pid, None)`, a shape no `(pid, e)` or `(pid,)` pair has

# v9 SE-01 (`24g`) / `H-51`: `PERSON_DEMANDED` (`data/rosters.py`) is declared on `dispatch`'s refusal; kept
# only when `_demand_earned` says so, and the loader's flat-row rule exempts exactly that kind.


def _demand_earned(w: "World", a: Act, kinds: tuple, at_precondition: bool) -> tuple:
    """P3 -- `person.demanded` IS EARNED BY THE ACT, NOT BY THE ROW: `CONFIDENCE_BROKEN`'s shape,
    applied to a refusal. A row that declares the kind (`dispatch`, `verb_table.yaml`'s
    `refusal_note:`) emits it only from its PRECONDITION refusal and only when the act's subject is
    an id the world does not hold (`world_q.demanded_person`, the one owner). An ineligible act
    demands nobody: it was refused before it asked anything of the world. Every other kind passes
    untouched, so a row that does not declare it moves by no byte.

    ⚠ THE FORCED CHOICE, AS AT `G6`: a keyed `emits_on_refusal:` would say WHICH clause refused, but
    keying needs a typed precondition (`data/verbs.py`, invariant 4's per-conjunct half), and typing
    `dispatch` would also hand its cell to the person side (`belief_contradicts`, `operands_for`), a
    formation change this position neither needs nor measured. And even keyed, `existence` of a
    `Person` cannot tell *names nothing* (a demand) from *names a building* -- one conjunct, two
    meanings."""
    if PERSON_DEMANDED not in kinds:
        return kinds
    keep = at_precondition and demanded_person(w, a) is not None
    return tuple(k for k in kinds if k != PERSON_DEMANDED or keep)


def _margin_ending(resolution: "Resolution | None") -> tuple:
    """SC-P1 (B05.18): `Event.ending` of a margin provider's act -- `((key, value), ...)` in `rosters.yaml: margin_endings`' order, read off the
    result the provider RETURNED (`seam/wrappers/sigma.py::resolve`), nothing recomputed here. `()` where the result is not a margin
    provider's: the same test `seam/ladder.py::degree_of` makes (a scene's `wound_state` and a field's `FIELD_FLAGS` come first; a
    `net`/`ob` pair is the margin), and where the result lacks a source the tuple names (a result a test planted, no dice dealt).
    `margin` is the result's real margin (today's key `settled_margin`: `net - ob`, quantised once at the ladder)."""
    r = resolution.result if resolution is not None else None
    if not is_margin_result(r):
        return ()
    src = tuple("settled_margin" if k == "margin" else k for k in MARGIN_ENDING)
    return tuple(zip(MARGIN_ENDING, (r[k] for k in src))) if all(k in r for k in src) else ()


def _refusal_degree(row: "VerbRow", degree):
    """B07.10: the band a REFUSAL Event carries. A task row (`draw_kinds` set) is drawn before its write is known, so a
    refusal after the draw is a precondition failed, not an outcome: `None`, as `_admits`'s and `_refuse_party_gap`'s refusals
    carry none. A contested row keeps its band (unchanged). The `draw` clause's `<verb>.failed` keeps its band (an outcome)."""
    return None if row.draw_kinds else degree


def _fold(self, w: "World", token: Token, a: Act,
          resolution: "Resolution | None" = None) -> list[Event]:
    """ONE act through the table: the SAME code for every act and every caller.

    ⚠ `resolution` IS WHAT THE SEAM RETURNED. It is
    `None` for every uncontested act, which is every act the corpus produces, and on that
    path nothing below changes: `writes_at(None)` and `emits_at(None)` on a verb with no
    degree map return the same flat tuples the fold has always applied. A CONTESTED act
    arrives here only from `resolve()`'s seam branch, carrying the band the subsystem's own
    result decided (`degree_of`)."""
    # OBSERVATION ONLY, AND DEDUPED BY ID: `w.acts`'s own `append` is deliberately idempotent on a
    # repeated id, because RESOLVE's own Declared fold and ENCOUNTER's real fold both call `_fold`
    # for the SAME deferred act, and `self.resolved` is a plain list with no such guard. A march
    # act (or any verb folding at two steps) would otherwise be recorded twice, inflating
    # `len(self.resolved)`, which `out["acts"]` reports.
    # ⚠ `self._resolved_ids` IS THE O(1) COMPANION, NOT A SECOND LIST SCAN: `resolved` is
    # cumulative and NEVER RESET across a campaign's seasons, so `any(r.id == a.id for r in
    # self.resolved)` would cost O(current length) on EVERY act's fold -- `ActStore._by_id`'s own
    # reason for existing.
    if a.id not in self._resolved_ids:
        self._resolved_ids.add(a.id)
        self.resolved.append(a)
    # G1a. AND THE STORE, which is NOT observation -- every Event this fold emits names `a.id`
    # in `causes[]`, and `state/log.py` refuses a cause that resolves to nothing. `resolve()`
    # already recorded it before its own refusal branches; this is idempotent on that same
    # object (see `ActStore.append`) and exists for the callers that enter `_fold` directly,
    # which is most of the `W-B` suite. Putting it at the entry point rather than trusting the
    # one caller is the difference between an invariant and a convention.
    w.acts.append(a)
    row = VERB_TABLE.get(a.verb)
    if row is None:
        # WHOSE GAP IS IT? `VERB_TABLE` is the owner, taken to carry every verb the design names
        # [ASSUMPTION; medium; Jordan to correct; revert: restore the prose read (`names_a_verb`,
        # `SOURCE_353_TEXT`, `_S353_CACHE`) and the two-way wording from the parent of the commit
        # trailed `Item: CR-45`, drop `test_cr45_*` and H-64's CR-45 sentence, re-record the golden],
        # so a verb on no row is the caller's invention (register row H-64). No prose is read to
        # decide it, and nothing here reports a verb the design names that the table omits.
        raise Unspecified(
            f"verb {a.verb!r} is on no row of the verb table", "S27/E2",
            needs=(f"NOTHING FROM THE DESIGN -- #353 does not name {a.verb!r} as a verb. "
                   "This is the CALLER'S invention and the gap is the caller's"),
            law="§E2 -- the resolver's body IS the table. A verb the table does not carry has "
                "no semantics, and inventing them at the call site is the second resolver "
                "§27.2 forbids. ⚠ CHARGED TO THE INSTRUMENT, NOT THE DESIGN (register row H-64)")

    # `W-B`. THE READS THIS ACT'S PRECONDITION MADE, ON EVERY EVENT THE ACT EMITS.
    # ⚠ DECLARED BEFORE `ev` AND REBOUND BY THE `requires` BLOCK BELOW, DELIBERATELY. `ev`
    # closes over the NAME, so it reads whatever `verdict` is bound to AT CALL TIME -- which
    # is `UNKNOWN, ()` for the ineligibility return above (eligibility reads tenures, not the
    # requirement, so it observed nothing) and the evaluated Verdict for every return after
    # it. The alternative -- passing `observed` as a parameter to all four `ev(...)` call
    # sites -- puts the same fact in four places, which is `§8` one seam over.
    verdict = Verdict(UNKNOWN, ())
    # `W-E`. `Event.degree` IS ASSIGNED HERE, on the one path every act-emission takes (§8),
    # rather than at the four `ev(...)` call sites. `None` on every uncontested act, which is
    # honest: no contest graded it.
    _degree = resolution.degree if resolution is not None else None

    def ev(kinds, changes=None):
        return _act_events(self, w, a, kinds, changes, _degree, verdict.observed)

    def refuse(kinds):
        # B07.10: a refusal is a precondition failed, never an outcome (04 §C.4), so a task act's refusal carries no band.
        return _act_events(self, w, a, kinds, None, _refusal_degree(row, _degree), verdict.observed)

    # §E2's first two steps, THROUGH THE ONE OWNER (`_admits`): `resolve()`'s contest branch never
    # enters this function, so written out here they would be skipped there.
    # ⚠ `verdict` IS REBOUND, and `ev` reads it at CALL time by closing over the NAME -- so a
    # refusal carries the reads that produced it and an ineligibility carries none, which is
    # honest (eligibility reads tenures, not the requirement).
    _ok, _refusal_kinds, verdict = self._admits(w, a, row)
    if not _ok:
        return refuse(_refusal_kinds)
    # B07.05 (18-A "The resolution, decided" 4, A-81): A LOST DRAW WRITES NOTHING AND EMITS THE ROW'S `draw` CLAUSE. A drawn
    # `task` row at a band whose share is zero (`task_share`, `rosters.yaml: task_fraction`; no band named here) folds to its
    # keyed `emits_on_refusal` clause `draw` (`<verb>.failed`), stamped with the band, before any effect runs: the act was
    # admitted and went against the actor, which is neither a refusal nor a no-op write. A row with no `draw` clause, and an
    # act with no degree (the arm `off`, a bookkeeping row), never reaches it.
    if _degree is not None and row.draw_kinds and task_share(_degree) == 0:
        return ev(row.refusal_for(DRAW_CLAUSE))

    # Each `writes:` through the gate. The gate is the only writer; the fold never assigns.
    changed: list = []
    # Which of `emits:` the effect actually earned. Empty means "all of them", which is the
    # contract every effect returning a plain list keeps.
    earned: set = set()
    # CP-T03-00: each receipt beside the kinds its subject earned (`()` = every kind, the plain-list
    # contract), so each kind's Event carries only its earners' changes (below).
    earners: dict = {}
    # CP-T03-02: what the effect hands the act's success Events beside its receipts -- each moved
    # subject's `observed` (by receipt identity) and the fight's `ending` (`_apply_write`).
    carried: dict = {}
    # SC-P1 (B05.18): a margin provider's contest leaves the roll that decided it on EVERY Event the act's loop below stamps,
    # the Failure band's included (`changed` empty there); a scene's own `ending` replaces it in `_apply_write` (never both:
    # a result is a scene's or a margin's). `()` for every act no margin graded.
    _roll = _margin_ending(resolution)
    if _roll:
        carried["ending"] = _roll
    # ⚠ `writes_at(degree)`, NOT `row.writes` (#358 rev.2 §C.4 / invariant 12). An UNCONTESTED verb
    # has no `writes_by_degree`, so this returns the flat tuple. The degree arrives on `resolution`
    # from `resolve()`'s seam branch, minted by `degree_of` from what the SUBSYSTEM returned. A
    # column no resolver consults is not a weak mechanism, it is one that does not exist (ID-13).
    #
    # ⚠ `writes_at(None)` on a contested verb RAISES (`Unspecified`, `H-115`) rather than falling
    # back to the union, so a caller that folds a contested act WITHOUT a resolution fails loudly
    # here instead of silently writing the full kill.
    # `test_h115_the_degree_branches_raise_unspecified_not_systemexit` is that path, executed.
    _pairs = row.writes_at(_degree) if row.writes else ()
    if _pairs:
        eff = EFFECTS.get(a.verb)
        if eff is None:
            raise Unspecified(
                f"{a.verb!r} writes {list(row.writes)} and Part E does not say WHAT VALUE",
                "E2/E3",
                needs="an entry in EFFECTS, or a `writes:` column that carries the value",
                law="§E3's `writes:` names the CELL and never the VALUE. A fold that writes "
                    "the cell without the value changes nothing, so a precondition on a "
                    "quantity the act never spends cannot bind twice -- and §27.1's scarcity "
                    "stops happening. Register row H-63")
        # ⚠ THE EFFECT RUNS ONCE PER ACT, NOT ONCE PER PAIR: `move` declares three, and running it
        # per pair would close and reopen the actor's containment three times and mint three
        # Tenures with the SAME id. Every pair is still GATED (class, Partition
        # and driver are checked for each), and the state change happens exactly once.
        # The alternative considered and rejected: gate all pairs dry, then apply. That
        # separates the check from the write, which is precisely what §30.2 forbids -- "the
        # gate APPLIES the write".
        try:
            for n, pair in enumerate(_pairs):
                kind, _, fld = pair.partition(".")
                # The effect runs ONCE, on the first pair: a verb writing three cells is ONE
                # operation, and running it per pair minted three Tenures for one `move`.
                made = self._apply_write(w, token, a, kind, fld, eff if n == 0 else None,
                                         earned=earned, resolution=resolution, earners=earners,
                                         carried=carried)
                changed.extend(c for c in made if c not in changed)
        # ⚠ AN EFFECT THAT TOUCHED NOTHING DID NOT DO THE THING, AND MUST NOT EMIT THE
        # SUCCESS. `kill / wound`'s effect returns early when its payload names no subject --
        # which is every computed act, since §F1's Candidate carries no operands (`H-80`) -- and
        # emitting `person.died` anyway would publish a fabricated death into every ledger.
        #
        # ⚠⚠ G4: THIS IS THE GATE'S JUDGMENT, CAUGHT HERE -- "CONVERTED AT THE FOLD BOUNDARY
        # INTO THE ROW'S REFUSAL KIND". The gate reads every subject the effect names before and
        # after the write and raises `NoOpReceipt` when none moved; an effect that declines
        # (`NO_CHANGE`) names none. A check on whether the effect REPORTED an id would be defeated
        # by an effect that reports its site and changes nothing (`work`, F9). The refusal's cause
        # is `[a.id]` PLUS the act's occasion ids, appended by `_act_events` like every Event an
        # act emits. The WRITE is refused too: the trace records it as refused (`F9`). A refused
        # first pair leaves the later pairs unchecked: a refused write authorizes nothing after it.
        except NoOpReceipt:
            TRACE.decision(f"{a.verb} wrote nothing", "E3",
                           chose="emit the refusal, not the success",
                           alternatives=["emit `emits:` anyway (publishes an event for a "
                                         "state change that did not happen)"])
            return refuse(_demand_earned(w, a, row.refusal_for(WRITE_CLAUSE), False) or (FOLD_REFUSED,))
        # ⚠ H-143 (B03.76): THE GATE'S REFUSAL EMITS TOO, `04 §C`'s row *"a refusal emits, never
        # raises"* (MECHANICAL). `NotYours` is F3's judgment that the write is not the actor's; a
        # precondition that admitted what the gate then refuses would end the season here, where
        # `NoOpReceipt` -- the same `Forbidden`, graded the same -- already becomes the row's refusal.
        # The Tenure store was put back before the raise (`World._restore_tenures`); an entity the
        # same `apply()` wrote KEEPS the write (H-130's class, pinned by `test_g3_not_yours.py`,
        # where the Office write stands beside `establish.refused`), so the refusal does NOT always
        # stand beside an unchanged world. A DIRECT `World.write` outside the fold still raises: the gate is the
        # backstop, and only the fold converts it. A refused first pair leaves the later pairs
        # unchecked, as above.
        except NotYours:
            TRACE.decision(f"{a.verb}: the gate refused the write", "C.4",
                           chose="emit the refusal, not raise",
                           alternatives=["raise NotYours (ends the season)"])
            return refuse(_demand_earned(w, a, row.refusal_for(WRITE_CLAUSE), False) or (FOLD_REFUSED,))
    # The act's proposed changes ride on the success Events -- §27.3's accumulator sums
    # them across the fold and clamps ONCE, which is order-independent as a fact.
    # ⚠ `[a.id]`, NOT `[ROOT]`. §19.4: "an Event with NO ANTECEDENT declares `causes: [ROOT]`" --
    # a campaign seed, a clock's first emission. AN EVENT EMITTED BY AN ACT HAS AN ANTECEDENT: the
    # act. `[ROOT]` here would make every Event antecedent-free so NO ARC WALKS ANYWHERE, and
    # #353 §19.4 says the design rests its narrative layer, audit trail and arc model on this edge.
    # `[ROOT]` is `[]` wearing a marker.
    #
    # THE RULE IS ALREADY IN THIS FILE, ONE SEAM OVER. `resolve`'s contest branch passes
    # `causes=[a.id]` and its comment records why the "the id must already be in the log"
    # reading is wrong: `w.log` holds Events, an Act is never appended to it, so that
    # predicate is PERMANENTLY FALSE and reading it strictly produces `[ROOT]` forever.
    # §39.2 line 2 says `causes[]` NAMES THE ACTS.
    # ⚠ ONLY THE KINDS THE EFFECT EARNED. An effect that returns a plain list earns all of
    # them, unchanged; one returning a mapping earns exactly the keys it filled. `confer`
    # declares `tenure.opened` AND `tenure.closed`, and conferring onto an unheld office
    # closes nothing -- publishing the second is a state change that did not happen.
    # ⚠ `emits_at(degree)`, NOT `row.emits` (`H-113`): a contested verb would otherwise report the
    # FLAT UNION of every band -- `kill / wound` emitting `person.died` whether the target died,
    # was wounded, or walked away untouched. That is `ID-9`'s class (a success report for
    # something that did not happen) inside the epistemic layer, where every witness then mints a
    # claim from it. The `earned` intersection still runs, against the band's own kinds.
    # B07.05: an act whose ARMED route was not taken (`armed_by:` set, its fixture `off`) was never drawn, and reads its
    # band-keyed `emits:` at `UNROUTED_BAND` -- the band an undrawn act reads, as `forge_quality_at` does -- with
    # `Event.degree` still `None` (`reconstruct` emits `finding.made` as before B07, so the arm-off control holds and the
    # revert is the one fixture value). Any other band-keyed row folded with no degree still raises (`H-115`).
    _undrawn = _degree is None and row.emits_by_degree and armed_route_off(a.verb, w.fixtures)
    _declared = row.emits_at(UNROUTED_BAND if _undrawn else _degree)
    # B10.24: `scruple.overridden` is the ACT's, not an effect's earning: it leaves the `earned` intersection and is emitted below, graded by no band.
    _gives_way = SCRUPLE_OVERRIDDEN in _declared and _scruple_overridden(w, a)
    _declared = tuple(k for k in _declared if k != SCRUPLE_OVERRIDDEN)
    kinds = tuple(k for k in _declared if k in earned) if earned else _declared
    # v9 IN-18 `G6` (`H-197`): `confidence.broken` IS EARNED BY THE ACT, NOT BY THE BAND -- declared on
    # `tell`'s told bands, emitted only when the act breaks a circle (`_confidence_broken`).
    # Outcome-specific earning in the generic fold is the FORCED choice: the data-driven alternative is a
    # conditional-emission column, and `04 §A.3` says of one more column "A seventh column has no such
    # argument available"; `tell` writes nothing, so no effect runs to earn the kind through `earned`.
    # The fold's own kinds are the declared column `rosters.yaml: fold_kinds` (`act.ineligible`, `act.refused`).
    kinds = tuple(k for k in kinds if k != CONFIDENCE_BROKEN or _confidence_broken(w, a, row))
    # Causes: the act and its occasion, both stamped by `_act_events` (IN-50).
    # ⚠ CP-T03-00 (`-08` AM-C-01), FOLD-WIDE: EACH KIND'S EVENT CARRIES ONLY THE CHANGES OF THE SUBJECTS
    # THAT EARNED IT -- a receipt whose subject named kinds rides only those kinds' Events; one whose
    # subject named none (`earns=None`, every kind) rides all of them, as do the act's own `changes`.
    # Every Event of one fold carrying EVERY receipt would make WITNESS's `both`/`per_change` deposit
    # mint each kind about every changed subject: a felled actor beside a wounded subject would have
    # put `(subject, person.died, True)` -- about a living man -- in every ledger, and IN-58's pairing
    # would have named the actor his killer (the ID-9 class). `world.py`'s MATTER emission already
    # carries per kind (CP-T02-01's `extra` loop); this is the same rule on the act's path. Where no
    # subject names a kind every Event carries every receipt.
    # CP-T03-02: AND EACH KIND'S EVENT CARRIES, AFTER THE PRECONDITION'S READS, THE `observed` OF THE RECEIPTS
    # RIDING IT (`Subject.observed`: a wounded party's `(pid, "body", v)` on `body.changed`), and every success
    # Event carries the fight's `ending` -- `()` and `()` on every act that is not `fight`/`accept` at Felled/Wounded
    # or `capture` at a band where an edge is opened (its Untouched band included), so those Events are
    # byte-identical to before. [ASSUMPTION; medium; Jordan to correct; revert: the field and
    # the Observation]
    _obs_of = carried.get("observed", {})
    _ending = carried.get("ending", ())
    out = []
    for k in kinds:
        riding = [r for r in changed if not earners.get(id(r)) or k in earners[id(r)]]
        extra = tuple(o for r in riding for o in _obs_of.get(id(r), ()))
        for e in ev((k,), list(a.changes) + riding):
            if extra or _ending:
                e = replace(e, observed=tuple(e.observed) + extra, ending=_ending)
            out.append(e)
    # IN-08 H3: THE SCAR, AFTER THE ACT'S EVENTS ARE FORMED, BY THE OUTCOME. `changed` is the
    # gate's own receipts for this act's writes, so it is empty on every path that is not a deed:
    # each refusal above returned early, and a band that declares no writes (`tell`'s `Failure`,
    # `fight`'s `Untouched`, `march`'s `Declared`) moved nothing. The scar is earned by an outcome
    # that MOVED, as a success kind is (G4's `earned`), and never by a band's name. A STAGED write
    # (`work`, `restore`) counts as moved at fold time; if the accumulator's clamp later replaces
    # the success Event (`_refuse_after_the_fact`), the scar already written stands -- a candidate
    # reading, rare in computed play, not a Jordan question.
    if changed:
        _scar_witnesses(w, token, a, out, self._scar_tally)
    if _gives_way:
        out.extend(_act_events(self, w, a, (SCRUPLE_OVERRIDDEN,), None, None, verdict.observed))
    return out


def _scruple_overridden(w: "World", a: Act) -> bool:
    """B10.24: DID THE ACTOR DO WHAT HIS OWN SCRUPLE FORBADE HIM? True where the Scene the act was released in (`w.acts.scene_of`)
    keeps, in its `forgone`, the act's own `(verb, subject)` at a positive margin -- a candidate his scruple (`options.scruple`)
    marked and the chooser let stand, so he acted against it. `Scene.forgone` is the chooser's record, read here and nowhere else; an
    act with no Scene (a hand-built one) or a Scene that struck nothing is False. The Event is `confidence.broken`'s shape, EARNED BY
    THE ACT, NOT BY THE BAND, and for the same forced choice: the verb row declares the kind and the fold keeps it only on this."""
    sc = w.acts.scene_of(a.id)
    if sc is None:
        return False
    subject = subject_of(a)
    return any(v == a.verb and s == subject and m > 0.0 for v, s, m in sc.forgone)


def _confidence_broken(w: "World", a: Act, row: "VerbRow") -> bool:
    """`G6`: DOES THIS ACT TELL A CONFIDED CLAIM TO SOMEBODY OUTSIDE ITS CIRCLE?

    The act carries what it says (`payload["said"]`, fixed at CHOOSE by `said_of`) and its row names
    who it is said to (`counterparty:`, read on the payload). The circle is on the actor's own copy of
    the said claim, `Claim.visibility` -- a tuple when the claim reached the actor through a telling
    made in confidence (`loop/witness.py::_circle_of`), `"own"` otherwise. The copy is the claim in
    the actor's ledger with the said `(subject, predicate, value, chain)`, the four fields `said_of`
    copies out of it. True when such a copy holds a circle the addressee is not in.

    ⚠ THE ACTOR'S OWN LEDGER AND NO OTHER. `04 §B.2:250` says: *"The carve-out is exact and it is not
    a widening: the fold may ask the ACTOR'S OWN ledger, through the `PersonInterior` snapshot the act
    carries, and no other."* `04 §B.9:423` types the act `Act := ( id, actor, via?, verb, refs,
    payload, terms?, scene )`, which has no slot for a snapshot, and `Act` here has none either: a
    `PersonInterior` now exists (`state/carriers.py`) but `loop/deliberate.py` builds it for `decision/`
    at CHOOSE and no act carries it to RESOLVE, so the spec is still AMBIGUOUS between the two sections. PICKED: the live read of the
    ACTOR'S OWN ledger, `w.persons[a.actor].ledger`, the precedent `queries/world_q.py`'s `claim.held`
    stem sets for `tell`'s `holds` conjunct (`WorldReader` has no stem for this match), handed bare to
    `queries/person_q.py::confided_outside`, the match's one owner beside `said_of`. REASON: carrying
    the circle on `Said` from CHOOSE would change which copy is found when it is evicted between
    CHOOSE and RESOLVE, which is a behaviour change, so it is not done here. GRADE: CONVENTION -- a
    one-token swap to another person compiles and no scan sees it, so the graded property *"the ledger
    is never read by ANOTHER person"* is not STRUCTURAL by signature (`04 §0` F9). ⚠ READ AT RESOLVE,
    NOT CARRIED FROM CHOOSE: a copy evicted between the two is not found, and the retelling breaks
    nothing [ASSUMPTION; `Said` carries no circle]. ⚠ A retelling INSIDE the circle (back to the confider, or to the other party) breaks
    nothing; the original teller holds their own copy `own` and can never break their own confidence;
    a self-disclosure (§10 decision 3) is an ordinary telling. At the shipped `telling_privacy` 0 no
    claim holds a circle, so this is False for every act."""
    pay = a.payload if isinstance(a.payload, dict) else None
    said = pay.get("said") if pay is not None else None
    hearer = binding_from_act(a).get(row.counterparty)
    p = w.persons.get(a.actor)
    if said is None or hearer is None or p is None:
        return False
    return confided_outside(p.ledger, said, hearer)


def _most_violated(p, verb: str, broken: tuple, violated: tuple) -> str:
    """THE ONE ELEMENT A PERSON HOLDS MOST VIOLATED BY AN ACT OF `verb`, from `broken` (his `broken_by` answer): the largest
    weight x |lean|, ties by name (`scar_season_cap: person`). A pursuit weighs its held weight times `pursuit_lean`; an affiliation
    its intensity as a share of the scale's ceiling (so it sits on the pursuit weight's own [0, 1] range) times `|engagement|`.
    [ASSUMPTION; medium; Jordan to correct: the sources give "largest weight x |lean|" and not the affiliation's weight.]"""
    pursuits = violated[0]

    def size(e: str) -> float:
        if e in pursuits:
            return float(p.pursuits[e]) * abs(pursuit_lean(verb, e))
        return (float(p.conviction[e]) / AFFILIATION_CEILING) * abs(engagement(verb, e))
    return min(broken, key=lambda e: (-size(e), e))


def _most_upheld(p, verb: str, healable: tuple) -> str:
    """THE ONE PURSUIT AN ACT OF `verb` HONOURS MOST AMONG `healable`: the largest weight x `pursuit_lean`, ties by name (`_most_violated`'s
    rule on the other side), so a vindication takes its one count from the pursuit he lives for most that the act serves."""
    return min(healable, key=lambda e: (-(float(p.pursuits[e]) * pursuit_lean(verb, e)), e))


def _scar_witnesses(w: "World", token: Token, a: Act, events: list, tally: set) -> None:
    """IN-08 H3 -- `(Person, scar)` as `{pursuit: count}`: ONE COUNT PER OBSERVER PER VIOLATED
    PURSUIT, written AT RESOLVE BY THE ACT (`ED-IN-0261`'s scar model).

    ⚠ WHY HERE AND NOT AT WITNESS. L4 constrains WHO writes a `social: true` row -- only an act --
    and S9.3 forbids WITNESS to touch a belief (`state/world.py`'s `MATRIX_REFUSAL_LAW` refuses
    `(Person, scar)` at WITNESS). So the ACT writes it, here, through the gate, with the driver's
    ACTS token. WHO saw it is not private to WITNESS: `epistemic.observers_for` is the one owner of
    perception and is called here exactly as WITNESS calls it (`fan_out_mode`, everyone alive), so
    the scar follows the same channels the deposit does.

    ⚠ DECLARED DIVERGENCE (`ED-IN-0261`): RESOLVE's call can differ from WITNESS's on `co_located`,
    since a later act can move someone. The presence cache is a barrier cache, so it is DISCARDED
    before the call -- the scar reflects who stood there when THIS act happened, not when the
    first act of the lap was folded. (`presence` is the one barrier-cache key in the tree, and
    nothing else at RESOLVE reads it.)

    ⚠ THE VIOLATION PREDICATE IS A CANDIDATE READING, NOT A RULING: `person_q.elements_violated_by`
    (a sign test of the pursuit's projection against the verb's alignment, asked once per act and
    intersected with each person's holdings by `person_q.broken_by`). WHETHER THE ACTOR
    COUNTS is `scar_excludes_actor`, a swept `Fixtures` arm. B09.11: the write is recorded by one
    `scar.taken` Event, appended to the log and kept out of the list `resolve` returns (see the
    call below), so the receipts are in an Event and WITNESS deposits nothing about them; putting
    them on the act's own Event would deposit claims about every scarred observer. Its readers are
    listed once, on the field (`state/carriers.py`, `Person.scar`).

    IN-08 H11 -- THE SAME MECHANISM OVER THE AFFILIATION TABLE (J-5's C4). An element is a pursuit
    OR a held religious affiliation: the affiliation half of `person_q.elements_violated_by` (the
    verb's cell for that affiliation in `rosters.yaml: tables.affiliation_engagement` is negative)
    is asked beside the pursuit half, and the two answers are one list of elements written by this one write --
    same observers, same actor arm, same `changed` gate, same token. The two rosters cannot share a
    name (`data/affiliations.py::_load_engagement` refuses it), so a count is never merged across
    them. Its reader is the crisis at threshold 3 (H13, `_conviction_crisis` below, called after
    this write); H9's reader counts held pursuits only.

    B10.06 -- THE SEASON CAP (`Fixtures.scar_season_cap`, `H-465`; `None` the control, uncapped). `tally` is the driver's per-tick
    scratch (`SeasonDriver._scar_tally`, cleared where `w.draw` is, at the start of each `season()`): the (observer, element) pairs
    (`element`) or observers (`person`) already counted this season. Before the write, every pair in it is dropped, and at `person`
    each observer keeps the one element he holds most violated (`_most_violated`). It is a local of the driver's step, not world
    state; the count written is still `(Person, scar)`.

    B10.07 -- THE STOCK'S TWO ENDS (`02_CHAR_scar_is_a_wound`). Four fixtures, each at its control a no-op: `scar_hold` (`H-466`, `any`) and
    `scar_primary_mass` (`H-469`) say whose elements count (`primary`: his primary pursuits and the affiliations he stands for), `scar_lean_floor`
    (`H-467`, `0.0`) how far an act must lean against a pursuit to violate it, and `scar_vindication` (`H-468`, `off`): under `on`, an observer
    holding a count on a primary pursuit the act honours (lean above `+floor`) loses ONE of it, from the pursuit the act serves most (`_most_upheld`),
    never below 0 (a key at 0 is dropped), at most once per person per season (the tally's `(HEALED, pid, None)`, spent only by a count that fell)
    and BEFORE the act's own violations, in a write of its own that earns `scar.healed`. A pursuit is never both honoured and violated by one act.
    The vindication reads pursuits only: the affiliation table has a sign and no lean."""
    if not events:
        return
    # Which elements this verb violates is a property of the verb alone, asked once per act; whose
    # holdings it breaks is person-side and known before anyone is asked whether they saw it. When
    # it is nobody (a verb with no celled axis and no affiliation cell, or no one holding an element
    # it leans against) the presence index is not rebuilt for nothing.
    hold, mass = w.fixtures.get("scar_hold"), w.fixtures.get("scar_primary_mass")
    floor, vindicating = w.fixtures.get("scar_lean_floor"), w.fixtures.get("scar_vindication")
    require_member(vindicating, SCAR_VINDICATIONS, f"scar vindication {vindicating!r} is not in the roster", "H-468",
                   law="§G -- declare it, default it, sweep it; an unknown arm silently reading off would make the sweep report the control twice")
    require_member(hold, SCAR_HOLDS, f"scar hold {hold!r} is not in the roster", "H-466",
                   law="§G -- declare it, default it, sweep it; an unknown arm silently reading `any` would make the sweep report the control twice")
    violated = elements_violated_by(a.verb, floor)
    upheld = _pursuits_upheld_by(a.verb, floor) if vindicating == "on" else frozenset()
    if not any(violated) and not upheld:
        return
    everyone = list(w.persons)
    broken_of = {pid: broken_by(w.persons[pid], violated, hold, mass) for pid in everyone}
    # A person can be vindicated only on a primary pursuit the act honours that he already holds a count on.
    healable_of = {pid: tuple(e for e in upheld_by(w.persons[pid], upheld, hold, mass) if w.persons[pid].scar.get(e, 0) > 0)
                   for pid in everyone} if upheld else {}
    if not any(broken_of.values()) and not any(healable_of.values()):
        return
    mode = w.fixtures.get("fan_out_mode")
    exclude_actor = bool(w.fixtures.get("scar_excludes_actor"))
    w.discard_caches()
    # Only a person with something broken (or something to heal) can be scarred, so only they are asked whether they saw
    # it: `observers_for` judges each person alone and answers in the order it is given, so the
    # filtered list yields the same persons, in `everyone`'s order, as WITNESS's call would.
    candidates = [pid for pid in everyone
                  if (broken_of[pid] or healable_of.get(pid)) and not (exclude_actor and pid == a.actor)]
    seen = {pid for e in events for pid, _ch in observers_for(w, e, mode, candidates)}
    hits = [(pid, broken_of[pid]) for pid in candidates if pid in seen and broken_of[pid]]
    healed = {pid: _most_upheld(w.persons[pid], a.verb, healable_of[pid]) for pid in candidates
              if pid in seen and healable_of.get(pid) and (HEALED, pid, None) not in tally}
    if not hits and not healed:
        return
    cap = w.fixtures.get("scar_season_cap")
    spent: set = set()
    if cap is not None:
        require_member(cap, SCAR_SEASON_CAPS, f"scar season cap {cap!r} is not in the roster", "H-465",
                       law="§G -- declare it, default it, sweep it; an unknown arm silently reading uncapped "
                           "would make the sweep report the control twice")
        kept = []
        for pid, broken in hits:
            if cap == "person":
                if (pid,) in tally:
                    continue
                broken = (_most_violated(w.persons[pid], a.verb, broken, violated),)
                spent.add((pid,))
            else:
                broken = tuple(e for e in broken if (pid, e) not in tally)
                if not broken:
                    continue
                spent.update((pid, e) for e in broken)
            kept.append((pid, broken))
        hits = kept
        if not hits and not healed:
            return

    if healed:
        def mend() -> None:
            for pid, e in healed.items():
                counts = dict(w.persons[pid].scar)
                if counts[e] > 1:
                    counts[e] -= 1
                else:
                    del counts[e]                    # never below 0, and a spent count leaves no key behind
                w.persons[pid].scar = counts

        mended = w.write("scar", token, None, record_kind="Person", fieldname="scar", driver="Act",
                         actor=a.actor, via=a.via,
                         change=Change(tuple(Subject.entity("persons", pid, fields=("scar",), earns=SCAR_HEALED) for pid in healed), mend))
        tally.update((HEALED, pid, None) for pid in healed)
        mev = Event(id=H(w.world_seed, w.tick, a.actor, f"{SCAR_HEALED}:{a.id}"), kind=SCAR_HEALED,
                    changes=[r for _s, r in mended], causes=[a.id], emitted_at=w.tick)
        w.log.append(mev)
        TRACE.event(mev.id, mev.kind, mev.causes)
    if not hits:
        return

    def perform() -> None:
        for pid, broken in hits:
            p = w.persons[pid]
            counts = dict(p.scar)
            for e in broken:
                counts[e] = counts.get(e, 0) + 1
            # SORTED ON WRITE: the dict's iteration order is what a reader sees; the content hash
            # does not read it (GO-07 folds a mapping sorted by its encoded keys).
            p.scar = {k: counts[k] for k in sorted(counts)}

    got = w.write("scar", token, None, record_kind="Person", fieldname="scar", driver="Act",
                  actor=a.actor, via=a.via,
                  change=Change(tuple(Subject.entity("persons", pid, fields=("scar",), earns=SCAR_TAKEN)
                                      for pid, _b in hits), perform))
    tally |= spent
    # B09.11: THE SCAR IS RECORDED, ONE `scar.taken` EVENT PER WRITE, CARRYING EXACTLY THE RECEIPTS THE
    # GATE MINTED (one per scarred person, who is named by no other field: `Event` has no actor, target
    # or subject). It is appended to the LOG HERE and is NOT in the list `resolve` returns, so WITNESS
    # (which reads that list, as `claim.deposited` relies on) fans it to nobody: the deposit count per
    # season is the observer (`test_g4_no_op_receipt.py::test_scar_taken_event_deposits_no_claim`).
    # BUILT HERE, NOT BY `World.write`'s `emits=`: that path puts ONE fresh receipt on the write's own
    # kind's Event and the per-subject receipts only on a kind OTHER than `emits` (`extra`), so a write
    # whose every subject earns the row's one declared kind would leave its per-person receipts in no
    # Event -- which is the defect this closes. The kind is the row's declared one (`write_matrix.yaml`).
    # THE ID IS MINTED AS THE FOLD MINTS ITS OWN (`H(seed, tick, actor, "{kind}:{act}")`): one such Event
    # per act, so no draw ordinal is needed, and `actor_of` (which reads `causes`) agrees with the actor
    # the id was minted from (`test_g1b_attribution.py` re-derives it).
    ev = Event(id=H(w.world_seed, w.tick, a.actor, f"{SCAR_TAKEN}:{a.id}"), kind=SCAR_TAKEN,
               changes=[r for _s, r in got], causes=[a.id], emitted_at=w.tick)
    w.log.append(ev)
    TRACE.event(ev.id, ev.kind, ev.causes)
    _conviction_crisis(w, token, a, dict(hits))


def _conviction_crisis(w: "World", token: Token, a: Act, broken_of: dict) -> None:
    """IN-08 `12e` H13 -- THE CRISIS AT SCAR THRESHOLD 3 (G-Q6), the first writer of `(Person,
    conviction)`. Called only by `_scar_witnesses`, after its write, with the persons that write
    just counted: a crisis is reached only by a scar count moving, and a scar count moves only by an
    act's outcome that moved state (`_fold`'s `changed` gate). So the conviction write inherits every
    bound the scar has -- never from a refused act or a band that wrote nothing (`tell`'s `Failure`),
    and at RESOLVE (or ENCOUNTER, where `march` folds) with the driver's ACTS token; WITNESS's token
    is refused at the row (S9.3, `state/world.py`'s `MATRIX_REFUSAL_LAW`).

    WHAT THE CRISIS DOES is `queries/person_q.py::conviction_after_crisis` (fold, restabilise --
    not built -- or destroyed, rolling nothing); this function only asks it of each scarred person
    and writes the answers, once, through the gate. A person whose vector it leaves as it was is not
    named, so the gate's no-op refusal (F9) cannot fire on a crisis that changed nothing. Nothing is
    emitted, on the scar's precedent: `conviction.moved` is declared on the row and no reader
    consumes it, and an Event here would deposit claims about every observer at WITNESS.

    `broken_of` maps each scarred person, in the scar write's order, to the elements this act just
    scarred them on, and the crisis is asked only among those (`conviction_after_crisis(p,
    among=...)`): a person already at the threshold on one affiliation and scarred on a pursuit
    alone has no affiliation count that moved, so no crisis."""
    moved = []
    for pid, broken in broken_of.items():
        p = w.persons[pid]
        if not p.conviction:         # no affiliation held, so none can be in crisis
            continue
        after = conviction_after_crisis(p, among=frozenset(broken))
        if after != p.conviction:
            moved.append((pid, after))
    if not moved:
        return

    def perform() -> None:
        for pid, after in moved:
            w.persons[pid].conviction = after

    w.write("conviction", token, None, record_kind="Person", fieldname="conviction",
            driver="Act", actor=a.actor, via=a.via,
            change=Change(tuple(Subject.entity("persons", pid, fields=("conviction",))
                                for pid, _a in moved), perform))


def _refuse_party_gap(self, w: "World", a: Act) -> list:
    """A contested or graded act refused AFTER admission (a party the seam cannot derive, a roll the
    provider refused, or a contest that reached its depth cap): the row's `emits_on_refusal`, `_contest`'s and `_grade`'s one body.

    ⚠ `or (FOLD_REFUSED,)` (`rosters.yaml: fold_kinds`), MATCHING EVERY SIBLING FALLBACK (`_admits`,
    `_fold`, `_refuse_after_the_fact`): a verb with an empty `emits_on_refusal:` (or a hand-built
    Act naming no real verb row at all) would otherwise produce ZERO Events here, a silent drop.

    ⚠ v9 IN-12 step 5 (#453 K-02, the party-gap fold edit): THE PARTY GAP IS THE COUNTERPARTY CLAUSE
    FAILING, so a row that KEYS `COUNTERPARTY_CLAUSE` emits `row.refusal_for(COUNTERPARTY_CLAUSE)` here
    and not its union -- which is what lets a contested keyed row carry two kinds (`arrest`), and the
    loader's contested-row rule narrows to rows that key no counterparty (`data/verbs.py`). Every row
    keying it before this edit (`determine`, `tell`; `issue` keys it too but is not contested, so it never reaches this body) keys ONE kind, equal to its union, so none moves.
    S27.4's refusal (a pool under 1D, `ContestRefused` `REFUSED`) reaches this body too and takes the
    counterparty kind [ASSUMPTION; medium; Jordan to correct; revert: the union, always]."""
    row = VERB_TABLE.get(a.verb)
    if row is None:
        declared = ()
    elif COUNTERPARTY_CLAUSE in row.refusals_by_clause:
        declared = row.refusal_for(COUNTERPARTY_CLAUSE)
    elif row.draw_kinds and WRITE_CLAUSE in row.refusals_by_clause:
        # B07.01 (UNDECIDED (11) (i)): a `task` row has nobody opposite, so no counterparty clause; its refused roll is an
        # act that did not take, its `write` key's kinds (the loader accepts its two refusal kinds on that ground).
        declared = row.refusal_for(WRITE_CLAUSE)
    else:
        declared = row.emits_on_refusal
    kinds = _demand_earned(w, a, declared, False) or (FOLD_REFUSED,)
    produced = _act_events(self, w, a, kinds)  # `_act_events` owns the id scheme (§8)
    for _e in produced:
        self.act_of[_e.id] = a
    return produced


def _contest(self, w: "World", token: Token, a: Act, contests: list,
             contest_max_depth: Optional[int], host: Optional[Any] = None) -> list:
    """S39.2, and M4's deferral fork (`ED-IN-0279` clause (a)). Extracted from `resolve()`'s own
    seam branch so RESOLVE and `loop/encounter.py` share the ONE body (§8) -- both call this for
    the same act, at different steps, and the STEP is what decides which of the two things it
    does.

    ⚠ ASSUMES `_admits` HAS ALREADY PASSED FOR `a`, AND NEVER RE-CHECKS IT. `resolve()`'s loop
    checks eligibility and `requires` once, before calling this, exactly as it always did; a
    caller reaching this function has already been admitted. ENCOUNTER's own selection is by the
    DECLARATION EVENT (`loop/encounter.py`), never by re-running this repo's own admission check
    against a world the whole lap has since moved -- `_fold`, below, still runs its OWN
    internal `_admits` when it applies the writes, which is pre-existing behaviour on every
    contested verb today and not something this function adds or removes.

    TWO THINGS THIS DOES, chosen by comparing `w.step` to the prize's OWN manifest row:

    - THE PRIZE ROW DECLARES A `step:` THAT IS NOT THE ONE RUNNING NOW (M4): fold at the row's
      own `declares:` band, writing nothing -- the loop's own deferral token (`Declared`,
      `field_degree_bands`). The real fight happens later, when this SAME function is called
      again with `w.step` at the declared step.
    - OTHERWISE (every prize before M4, and a deferred prize once its step arrives): dispatch to
      the seam and fold at the degree the subsystem's own result decides, exactly as `resolve()`
      always did.

    `host` (v10 REM-31, IN-46): the PLAYABLE host, passed by ENCOUNTER only (`loop/encounter.py`); RESOLVE's
    call passes none, so the driver can suspend nowhere but ENCOUNTER. Handed through `contest()` to the
    provider untouched; it enters neither the generator's purpose below nor the fold."""
    prize = manifest.resolve("contest", contests[0])
    if prize is not None and prize.get("step") and prize["step"] != w.step.value:
        return self._fold(w, token, a, Resolution(prize["declares"], {}))
    if contest_max_depth is None:
        raise Forbidden(
            "a contest was reached with no caller-supplied max_depth", "S39.3",
            law="S39.3 -- the depth cap has NO DEFAULT; a default is a number somebody made up "
                "and it will be cited later as though it were measured")
    # THE TARGET, AND WHICH SHAPE OF SIDES THE PRIZE NEEDS (M4). `sides_of` is the one place
    # that decides, dispatched on the PRIZE's own manifest module -- NEVER on `a.verb`, and
    # NEVER on what `_target` happens to look like: `_target` is `payload[row.opponent_operand()]`
    # (below), and a candidate's `subject` binding to a Rung id is not unique to `march`
    # (`tell`'s TOPIC can name a place, though its `_target` is now the hearer `to`), so a
    # shape-based dispatch on `_target` is unsafe -- see `sides_of`'s own docstring for the corpus
    # case that found this.
    # ⚠ THE OPPONENT IS THE ROW'S `counterparty:` OPERAND WHEN IT NAMES ONE, ELSE `subject`
    # (telling workplan `T4`, `ED-IN-0282`): `tell` contests against its HEARER (`to`), not its
    # topic. `fight` and `march` name no counterparty and read `subject` exactly as before.
    _row = VERB_TABLE.get(a.verb)
    _target = ((a.payload or {}).get(_row.opponent_operand() if _row is not None else "subject")
               if isinstance(a.payload, dict) else None)
    _parties, _subject, _rung = sides_of(w, a, _target, contests[0])
    # ⚠ A PARTY-GAP IS A REFUSAL HERE, NOT A RAISE (M4). `seam/contest.py`'s S39.1 -- *"claimant[]
    # is PERSONS, ALWAYS"* -- refuses an EMPTY list exactly as it would a wrong-shaped one
    # (`if not claimants: raise Forbidden(...)`), which every verb before M4 never triggered:
    # `sides_of`'s non-`mass_battle` branch always seeds `_parties` with `a.actor`, so it is
    # never empty. `march`'s army-muster branch genuinely CAN be -- an actor with no seat, or an
    # origin that musters nobody -- and that is `march`'s own eligibility/effects question
    # (`ED-IN-0279` clause (a)), not an instrument defect. Refusing it the same way `_admits`'s
    # ineligibility already does, rather than letting `contest()`'s hard raise escape a caller
    # that does not expect one.
    if not _parties:
        return _refuse_party_gap(self, w, a)
    # ⚠⚠ `U1`: THE DRIVER CONSTRUCTS THE GENERATOR, AND `04 §C.12`'s REJECTION 4 IS LOAD-BEARING.
    # `purpose` stays `roll:<prize>:<act id>`, provider-specific by design.
    # ⚠ AN `effort` ACT IS ONE ACT, SO IT IS ONE ID AND ONE DRAW (CP-T01-05): the effort is read off the act
    # at the `contest()` call below and reaches the roll as named levels; it spends slots, never a second draw.
    _rng = draw_factory(w.world_seed, lambda: w.tick)(a.actor, f"roll:{contests[0]}:{a.id}")
    # ⚠ A WRAPPER'S PARTY-GAP REACHES HERE TOO, AND IT IS THE SAME SHAPE OF GAP AS EMPTY
    # `_parties`. `sides_of`'s `holder_faction_of` is `None` for any Rung with no HELD ancestor
    # (`H-149` permits an unheld settlement as a march target; `boot/realm.py`'s `Uncontrolled`
    # provinces), which a wrapper reports as `status="PARTY-GAP"`. ⚠ SINCE v9 IN-13
    # `subject = None` NO LONGER REACHES THIS BRANCH: `mass_battle.py` answers it `Unopposed` (no
    # opposing faction), and an empty army is refused above, at the `_parties` check. The branch
    # stays for the other wrappers' shapes of missing party (`combat.py`, `sigma.py`, and
    # `mass_battle.py`'s no-rung). Read off the seam's result, not pre-checked on `_subject`
    # before the call, because PARTY-GAP is the WRAPPER's own vocabulary for every shape of
    # missing party (empty claimants, wrong-typed claimant, no subject, no rung) and a pre-check
    # here would have to re-enumerate all of them to stay in sync.
    r = contest(w, rung=_rung, prize=contests[0], claimants=_parties, depth=0,
                max_depth=contest_max_depth, causes=[a.id], verb=a.verb, subject=_subject,
                rng=_rng, effort=effort_of(a), host=host, via=a.via)
    if isinstance(r, ContestRefused):
        # `04 §A.2`'s typed refusal (`seam/contest.py::REFUSAL_STATUSES`): `PARTY-GAP` (a missing
        # party) and `REFUSED` (`sigma.py`'s S27.4, `Ob > 2x Pool`). `speak` is contested, so a
        # speaker whose pool is under 1D reaches this whenever a matter is docketed (the ceiling caps
        # the obstacle at 2); S27.4's rule is that the attempt is refused and the season spent --
        # never that the season aborts -- so it takes the verb's
        # refusal kind, the shape `PARTY-GAP` takes. `ENGINE-UNAVAILABLE` (a wrapper's subsystem
        # failed to import/compose) is NOT a refusal: the seam still raises it, loud on purpose, since
        # folding it into a graceful `march.refused` would hide an infrastructure failure behind a
        # plausible-looking game Event.
        return _refuse_party_gap(self, w, a)
    if isinstance(r, ContestError):
        # A depth-capped contest is a refusal like the one above: the act happened and the contest did not, so it
        # takes the row's refusal kind and never leaves the fold with no Event (`U5a_CORE_owed_edits` §B row 4).
        TRACE.note(f"contest returned {r}", "S39.3")
        return _refuse_party_gap(self, w, a)
    if not isinstance(r, dict):
        return r
    produced = self._fold(w, token, a, Resolution(degree_of(r, _target, w.fixtures), r))
    TRACE.decision(
        f"contest for {contests[0]!r} resolved", "S39/H-98",
        chose=f"read the degree off the scene and fold at it "
              f"({produced[0].degree if produced else '?'})",
        alternatives=["map winner -> person.died (S27.2: the second resolver)",
                      "record that it ran and write nothing (the pre-`W-E` behaviour: "
                      "a lost fight wrote exactly what a won one did)"])
    return produced


def _grade(self, w: "World", token: Token, a: Act, route: dict) -> list:
    """v9 FI-01 (`ED-FI-0009`, J-22 option (A)): AN INQUIRY, ROLLED AND FOLDED AT ITS DEGREE.

    `route` is the verb's `graded_tasks` row (`data/rosters.py::graded_route`); ASSUMES `_admits` HAS PASSED, as `_contest` does. The
    roll is `seam.grade`'s, the band `degree_of`'s (the one ladder), and the fold reports the band's
    `emits:` as for a contested act. A `ContestRefused` folds through `_refuse_party_gap`.

    ⚠ THE SUBJECT IS THE ACT'S `payload["subject"]`, WHICH A CHOOSER-FORMED ACT CARRIES AS THE QUESTION'S
    REFERENT (`research`: a Record, `surveil`: a Rung, a person-kind Rung shares its person's id). The
    provider reads opposition off a PERSON subject only (`sigma.py::_opposition_of`) and only where
    the verb's `capability:` column names a skill (`descriptors.CAPABILITIES`). The three inquiry verbs
    (`research`, `examine`, `surveil`) name `inquiry`, so a PERSON subject is opposed at his score on it and
    `opposed_ob(pool_default)` stands in only for a subject that is not a person (a Record, a Rung).
    ⚠ THE GENERATOR IS THE ACT'S OWN, `H(seed, tick, actor, "roll:<verb>:<act id>")` -- `_contest`'s
    shape with the verb where a prize would be (there is none), so adding a graded inquiry moves no
    other act's draw (`04 PART D row 35`)."""
    _subject = a.payload.get("subject") if isinstance(a.payload, dict) else None
    # B07.05 (18-A item 3, A-30): a `form: task` route draws on `H(seed, tick, actor, "task:" + a.id)`; an inquiry keeps
    # `roll:<verb>:<act id>` (the three carried inquiries' draws do not move). [ASSUMPTION: `reconstruct`, armed but
    # `form: inquiry`, takes the inquiry key -- basis: UNDECIDED (2) makes it an inquiry; 18-A's key names the task draw.]
    _purpose = f"task:{a.id}" if route.get("form") == FORM_TASK else f"roll:{a.verb}:{a.id}"
    _rng = draw_factory(w.world_seed, lambda: w.tick)(a.actor, _purpose)
    r = grade(w, [a.actor], [a.id], route, verb=a.verb, subject=_subject, rng=_rng,
              effort=effort_of(a))
    if isinstance(r, ContestRefused):
        return _refuse_party_gap(self, w, a)
    return self._fold(w, token, a, Resolution(degree_of(r, _subject, w.fixtures), r))


def _apply_write(self, w: "World", token: Token, a: Act, kind: str, fld: str, eff=None,
                 earned: Optional[set] = None,
                 resolution: "Resolution | None" = None,
                 earners: Optional[dict] = None,
                 carried: Optional[dict] = None) -> list:
    """The fold's write. It carries no per-verb behaviour -- the effect of a write is the
    matrix row's business, and what a verb writes is the verb table's.

    ⚠ IT RETURNS THE `StateChange`s THE WRITE MADE, and that is what lets an Event say WHAT IT
    CHANGED: a computed act carries no `changes[]` of its own, and the fold knows what it wrote.
    `H-79`'s `per_change` rule and §F1's Q2 clause "a claim whose subject is something they hold"
    read it.

    G4: "what it wrote" is the GATE'S answer -- the receipts `World.write` minted for the
    subjects that moved, not the effect's report. An effect naming a subject that did
    not move gets no receipt for it; one naming nothing that moved raises `NoOpReceipt`, which
    `_fold` turns into the refusal.

    CR-06 (`H-137`): a Tenure the effect's OWN BODY changes, before it returns its `Change`, is
    refused as `NotYours` with the store put back, and so is an entity field it reassigned or an
    entity it added or removed (`effect_body_observed` states the bound: a value mutated in place
    escapes, so an effect still defers its mutation into `Change.apply`)."""
    # ⚠ G2: ASKED FOR ITS SIDE EFFECT ONLY. The class comes from the driver's token, so the row is
    # not otherwise read here -- but the call raises `Unspecified` for an absent row BEFORE
    # `World.write` is reached, and `World.write` would raise the same thing only after logging a
    # refused `TRACE.write` line (it keeps `runs/TRACE.txt` stable).
    matrix_row(kind, fld)
    earned = earned if earned is not None else set()
    # G2: THE DRIVER'S ACTS TOKEN, NOT `mrow.write_class(Step.RESOLVE)`: `World.write` computes
    # the same `STEP_CLASS[step]` from the same map, so S30.2's check could not fail for any fold
    # write. The token is a second source: a driver that handed RESOLVE a MATTER token is refused.
    # G3: WHO IS WRITING, AND THROUGH WHICH SEAT -- the gate's F3 clause asks both of every Tenure
    # the effect touches. `via` is `None` for an act exercising no seat, and then only the actor's
    # own edges (and a cascade the act itself caused) can be written.
    if eff is None:
        # A PAIR AFTER THE FIRST: gated for its class, step and partition, carrying NO change --
        # the effect already ran, once, on the first pair (`_fold` says why). A closure, so the
        # gate does not judge it for F9: it names nothing and mints nothing, and a check-only
        # write refused as a no-op would refuse every multi-cell verb on its second cell.
        w.write(fld, token, lambda: None,
                record_kind=kind, fieldname=fld, driver="Act", actor=a.actor, via=a.via)
        return []
    # ⚠ `W-E`: EVERY EFFECT TAKES THE RESOLUTION, AND UNIFORMLY (`H-114`): an effect that took no
    # degree could not honour the branch `writes_at` selected, and a fold at degree `Wounded`
    # would DELETE THE PERSON. One signature for all twelve rather than an inspect-the-callable dispatch: a fold
    # that passes different arguments to different effects has a second contract nobody declared.
    #
    # ⚠⚠ G4: THE EFFECT RUNS HERE, BEFORE THE WRITE, AND WRITES NOTHING -- IT RETURNS THE CHANGE.
    # `04 §C.2`'s signature is `gate.write(token, kind, field, id, change, ...)`: the change is an
    # ARGUMENT, computed by the caller and applied by the gate, so the gate can read a subject
    # before it moves. One consequence, stated: an effect's own refusal to be built (`_operand`'s
    # `InstrumentDefect`, `kill / wound`'s `Unspecified`) raises before the gate's class and
    # step checks rather than after them -- both are call-site defects and neither mutates.
    #
    # ⚠ CR-06 / `H-137`: THE EFFECT'S OWN BODY IS OBSERVED TOO, FOR TENURES AND ENTITY FIELDS.
    # `World.write` takes its snapshots only after this call returns, so a Tenure or an entity field
    # the body moved before handing back its `Change` was baked into them and judged by neither F3 nor
    # F9. `World.effect_body_observed` runs the effect inside its own snapshots and refuses what the
    # body moved (put back, then `not_yours`); its docstring states the bounds (a value mutated in
    # place escapes; anything moved is refused, lawful or not, since a body is not a write).
    change = w.effect_body_observed(lambda: eff(w, a, resolution), a.actor, a.via, kind, fld)
    got = w.write(fld, token, None, record_kind=kind, fieldname=fld, driver="Act",
                  actor=a.actor, via=a.via, change=change)
    # ⚠ AN EFFECT MAY EARN SOME OF ITS DECLARED KINDS AND NOT OTHERS. A subject that earns `None`
    # earns *all* of them (the original plain-list contract); a named kind earns only that one.
    # Otherwise the fold would emit EVERY kind in `emits:` the moment anything changed -- `confer`
    # onto an unheld office would publish `tenure.closed` with nothing closed. G4: a kind is
    # earned by a subject that MOVED, which the gate decides, not by one the effect listed.
    # CP-T02-01 / HR-1: a subject may name several kinds (`Subject.kinds`): a dead loser earns his
    # band's kind AND `person.died`, which one kind per subject could not say.
    # CP-T03-00: and, where the caller asks (`_fold`'s `earners`), WHICH kinds each receipt's subject
    # earned, keyed by the receipt's identity, so each kind's Event carries only its earners' changes.
    for s, _r in got:
        earned.update(s.kinds)
        if earners is not None:
            earners[id(_r)] = s.kinds
        # CP-T03-02: what a MOVED subject's write leaves it as (`Subject.observed`), keyed like `earners`.
        if carried is not None and s.observed:
            carried.setdefault("observed", {})[id(_r)] = s.observed
    # CP-T03-02: the fight's per-party ending (`Change.ending`), for the fold's success Events.
    if carried is not None and change.ending:
        carried["ending"] = change.ending
    # G1a -> G4. THE GATE MINTED THESE, INSIDE THE WRITE, FOR THE SUBJECTS THAT MOVED AND NO OTHER:
    # a receipt minted here for every id the effect REPORTED is how a no-op receipt
    # (`before == after`) comes to be admitted by the log.
    return [r for _s, r in got]

def resolve(self, token: Token, acts: list[Act],
            contest_max_depth: Optional[int] = None, scenes: Optional[dict] = None) -> list[Event]:
    w = self.w
    w.step = Step.RESOLVE
    w.frozen = False
    TRACE.step("RESOLVE", "enter"); TRACE.barrier(3, "RESOLVE")
    w.discard_caches()

    # S27: FIVE STRATA, then S32 rest 3's CONTENT-DERIVED canonicalization WITHIN each.
    # This sorts ONE GLOBAL ARRAY, which is exactly why RESOLVE DOES NOT PARTITION (S31).
    # ⚠ THE STRATUM COMES FROM THE VERB TABLE, NOT FROM THE ACT'S DEFAULT. `VerbRow.stratum` is a
    # NAME (`social`, `movement`) validated against the roster at load; `Act.stratum` is an INT
    # defaulting to 4, so without `stratum_of` mapping one onto the other every computed act
    # would resolve at 4 and §27's five-strata ordering would be INERT (`rosters.yaml` says of
    # that roster "ORDER IS SEMANTIC HERE... editing the order changes which acts see which
    # world"). An act that names its own stratum still wins, so a caller can test the ordering
    # directly (`A37`). `_canonical_order` is shared with `loop/encounter.py`.
    ordered = _canonical_order(w, acts)
    TRACE.decision(f"ordering {len(acts)} acts", "S27/S32",
                   chose="five strata, then a content-derived hash key over one global array",
                   alternatives=["completion order", "rank", "per-container sort (voids the fold)"])

    # B09.16: THE SCENES DELIBERATE RETURNED (`{scene id: Scene}`, release order) ARE KEPT BESIDE THEIR ACTS, HERE, BEFORE
    # ANY OF THEM IS APPENDED -- this step holds the ACTS token and the act store; DELIBERATE holds neither and stores
    # nothing. Added ahead of the sort's loop, in release order, so `ActStore.scenes()` is release order and every act
    # the loop below appends already answers `scene_of`. A bare-act caller (a test, a probe) passes none.
    for _sc in (scenes or {}).values():
        w.acts.add_scene(_sc)
    out: list[Event] = []
    # S27.3 SUM-THEN-CLAMP-ONCE accumulator. ⚠ G4: IT IS `World._staged` NOW, NOT A LOCAL HERE,
    # because an act's `work` WRITES to it through the gate (`_eff_work`'s docstring). Anything
    # staged before this pass came from a bare `_fold` outside any RESOLVE -- a test calling the
    # fold directly -- and belongs to no ordered fold, so it is discarded rather than applied.
    w.take_staged()
    for a in ordered:
        # G1a. THE ACT ENTERS THE STORE BEFORE IT IS FOLDED, and the order is the whole point:
        # every branch below emits `causes=[a.id]` plus the occasion ids (`_act_events`), INCLUDING the two refusal branches, so an
        # act recorded only on success would leave every refusal chain unresolvable -- which is
        # the case the act store's own header names. Appended once per act, here, rather than at
        # each of the five emission sites: `CLAUDE.md` §8, and five sites is five chances to
        # forget the one that refuses.
        w.acts.append(a)
        # ⚠⚠ S27.1: *each act sees the world its predecessors left.* A PREDECESSOR CAN REMOVE THE
        # ACTOR: acts are minted for everyone at DELIBERATE, resolved in stratum order at RESOLVE,
        # and a man felled in the third act of the season is not there for the ninth, so he does
        # not act. `_survives` is shared with `loop/encounter.py`.
        _gone = self._survives(w, a)
        if _gone:
            out.extend(_gone)
            continue
        # S39.2 line 1: loop -> subsystem, when an act contests something.
        #
        # ⚠ THE VERB'S COLUMN, NOT ONLY THE ACT'S FIELD. `ARCHITECTURE_V2.md:394` puts `contests:` on
        # the VERB ROW -- *"if set, routes to the seam at RESOLVE"* -- and `:434` sets it on
        # `kill / wound`; reading only `a.contests`, which no chooser sets, would send a kill down
        # the EFFECT path to write a death directly. Jordan, 2026-09-02: *"that…would trigger the
        # personal combat scene. you can't just kill or wound imo."*
        _row = VERB_TABLE.get(a.verb)
        _contests = _contests_of(a, _row)
        # v9 FI-01: an inquiry's `graded_tasks` route -- the second source of a degree, which the
        # loader refuses beside a `contests:` on the VERB ROW (one degree, one source); an act carrying its own
        # `contests` (`_contests_of`, hand-built acts only) takes the contest branch below and the route is unread.
        # B07.01 (18-A edit 6): `graded_route` -- a route carrying `armed_by: task_draw_arm` is taken only with the arm `on`;
        # `off` (the control) folds the act flat below, as before B07.
        _route = graded_route(a.verb, w.fixtures)
        if _contests or _route:
            # ⚠⚠ §E2's ORDER: ELIGIBILITY AND `requires` BEFORE THE SEAM, NOT AFTER IT. `_fold`, which
            # owns that check, is the branch this one is the alternative to, so a contested act's
            # precondition would otherwise never be read. `_admits` is the single owner (§8).
            #
            # ⚠ A REFUSAL HERE IS AN EVENT, NOT A RAISE. The act happened and was witnessed; what
            # did not happen is the contest. The row's `emits_on_refusal` -- `kill.refused`,
            # `speech.unheard`, every contested row's own -- is the kind, and `[a.id]` plus the occasion ids (`_act_events`) keeps the chain
            # resolvable exactly as the two refusal branches in `_fold` do.
            _ok, _refusal_kinds, _verdict = self._admits(w, a, _row) if _row else (True, (), None)
            if not _ok:
                produced = _act_events(self, w, a, _refusal_kinds,
                                       observed=_verdict.observed if _verdict else ())
                for _e in produced:
                    self.act_of[_e.id] = a
                out.extend(produced)
                continue
            # S39.2 line 2 onward: dispatch to the seam, or defer to ENCOUNTER, and fold at the
            # degree either one decides. Extracted to `_contest` (M4, `ED-IN-0279` clause (a))
            # so RESOLVE and `loop/encounter.py` share the one body -- see that function's own
            # docstring for the deferral fork and why it does not re-check `_admits`, just
            # confirmed above. `_contest` always returns a list -- a depth-capped
            # `ContestError` is folded to the row's refusal inside it, once, so this loop and
            # `loop/encounter.py`'s own do not each carry a second copy of that check.
            produced = (self._contest(w, token, a, _contests, contest_max_depth) if _contests
                        else self._grade(w, token, a, _route))
        else:
            # S27.1: CONTENTION IS AN ORDERED FOLD. Each act sees the world its predecessors
            # left. SEQUENCE, NOT SIMULTANEITY -- and NO ACT NEEDS TO KNOW ANOTHER EXISTED.
            produced = self._fold(w, token, a)
        # ⚠ `W-E`: THE TWO PATHS SHARE THE BOOKKEEPING BELOW (§8): duplicating those three loops
        # inside the contest branch would be a second copy of a rule that gets to disagree with
        # the first.
        # ⚠ WHICH ACT EMITTED WHICH EVENT, recorded once here rather than re-derived from the
        # id hash by every consumer. WITNESS needs it to answer *what is this deposit ABOUT*
        # for an Event that wrote nothing: an act that changes no state has an empty
        # `changes[]`, and the only thing that knows what it named is the act.
        # ⚠ **RESOLVER-SIDE AND CUMULATIVE ACROSS SEASONS — NOT season-local, and the
        # difference is load-bearing.** `resolved`, `act_of` and the Scene store (`w.acts`) are never reset by
        # `season()`, and `R3` REQUIRES that: a claim deposited at WITNESS in season *t* is
        # read at DELIBERATE in *t+1*, so the act that occasioned this one is a PREVIOUS
        # season's act and must still be reachable. A session that makes these three
        # season-local to tidy them blinds the propagation check silently — it would still
        # pass, on zero.
        for _e in produced:
            self.act_of[_e.id] = a
            # v9 FI-02 + FI-03 (`SM-3`, `ED-FI-0002`): WHAT THIS EVENT UNCOVERS, through the `inquiry`
            # role, dispatched by the Event's KIND (`seam.find_trail`; `rosters.yaml: inquiry_modules`)
            # for every Event THIS LOOP SEES (the fold's and `_contest`/`_grade`'s outputs; not an admit
            # refusal, not an after-the-fact replacement, not ENCOUNTER's) -- not from `_grade`, so no branch here names a verb, a
            # band or a kind: an unclaimed kind finds nothing, and an ungraded `finding.made` carries no
            # degree and `finding_terms` keys nothing for it -- the data decides. At RESOLVE, after the
            # act's fold, so the find reads the log as PREVIOUS laps left it (the log gains a lap's
            # Events only after RESOLVE returns, `loop/driver.py`). WITNESS deposits it.
            # ⚠ Reachable by a `research` only through a plant -- see `epistemic.trail_of`.
            # ⚠ LAYER 1 (`04` §A.2): see `seam/wrappers/fieldwork.py` (`self.findings` is a driver-held store).
            _found = find_trail(w, a, _e)
            if _found:
                self.findings[_e.id] = _found
        # ⚠ G4: NO LOOP FEEDS §27.3's ACCUMULATOR OFF THE SUCCESS EVENTS: it could not tell the
        # accumulator WHICH acts a site's total came from, which judging that total's write needs.
        # `_eff_work` stages its own delta through the gate instead (`World.stage`).
        out.extend(produced)

    # S27.3 / S32 rest 4: SUM ALL DELTAS, CLAMP ONCE. Clamping may not depend on arrival
    # order. Integer addition is associative and commutative, so this is order-independent
    # AS A FACT, not as a claim (S32/S48).
    #
    # ⚠⚠ G4: AND THIS IS WHERE F9 IS JUDGED FOR THE CHANGE `work` DEFERRED. The write names the
    # SITE and the gate compares its condition either side, so a sum the clamp eats entirely -- a
    # site at `condition_scale` worked up, deltas that cancel -- moves nothing and raises
    # `NoOpReceipt`. Every act that staged on the site then gets its refusal in place of its
    # provisional success (`_refuse_after_the_fact`): the site did not change, so no act changed
    # it. A site that is gone by now names an absent subject that stays absent, and refuses the
    # same way.
    scale = w.fixtures.get("condition_scale")
    for (rk, sid, fname), contribs in w.take_staged():
        if (rk, fname) != ("Site", "condition"):
            raise InstrumentDefect(
                f"a delta was staged on ({rk}, {fname}) of {sid!r}, and S27.3's accumulator "
                f"applies `(Site, condition)` only -- nothing here would ever land it")
        deltas = [d for _aid, d in contribs]
        total = sum(deltas)
        site = w.sites.get(sid)
        # ⚠ PLAN POSITION `24e`: THE UPPER BOUND IS THE WORKS' CEILING, NOT ONLY THE SCALE -- r2 `04`
        # §A.6.3, RULED: *"the ceiling is one more term in that one `min`"*, and `ceiling` returns the
        # scale when no works names the site. ⚠ `max(condition, ceiling)`, NOT r2's bare `ceiling`: the ceiling bounds
        # the RISE and never takes away what stands (a works declared on a standing fabric has 0 terms
        # ripe, ceiling 0, and r2's form would drop the fabric to 0 on the next staged delta).
        # Computed from the world BEFORE the sum, not from the deltas, so the clamp stays
        # order-independent AS A FACT (S32/S48): one bound per site, whatever order the acts staged in.
        hi = scale if site is None else min(scale, max(site.condition, ceiling(w, site)))

        def clamp_once(site=site, total=total, hi=hi) -> None:
            if site is not None:
                site.condition = max(0, min(hi, site.condition + total))
        try:
            w.write("condition", token, None,
                    record_kind="Site", fieldname="condition", driver="Act",
                    change=Change((Subject.entity("sites", sid),), clamp_once))
        except NoOpReceipt:
            TRACE.decision(f"the summed write to a site moved nothing -> {sid}.condition",
                           "S27.3/F9",
                           chose=f"refuse every act that staged on it ({len(contribs)})",
                           alternatives=["let each act's provisional success stand (a success "
                                         "Event for a write that did not happen: F9)"])
            _refuse_after_the_fact(self, w, out, [aid for aid, _d in contribs])
        except NotYours:
            # H-143 (B03.76): the gate's refusal of the summed write refuses the staged acts as a
            # no-op does -- `04 §C`'s "a refusal emits, never raises".
            TRACE.decision(f"the summed write to a site was refused by the gate -> {sid}.condition",
                           "C.4",
                           chose=f"refuse every act that staged on it ({len(contribs)})",
                           alternatives=["raise NotYours (ends the season)"])
            _refuse_after_the_fact(self, w, out, [aid for aid, _d in contribs])
        TRACE.decision(f"clamping {sid}.condition", "S27.3",
                       chose=f"sum {deltas} = {total}, then clamp ONCE",
                       alternatives=["clamp per delta (arrival-order dependent)"])
    TRACE.step("RESOLVE", "leave")
    return out


def _act_events(self, w: "World", a: Act, kinds, changes=None, degree=None,
                observed=()) -> list:
    """THE ONE SHAPE OF AN ACT'S EMISSION: one Event per kind, its id `H(seed, tick, actor,
    "<kind>:<act id>")`. `_fold`'s `ev` is this with the act's degree and verdict bound; the
    accumulator's after-the-fact refusal (G4) is this with the success Event's, so a `work`
    refused at the accumulator is byte-for-byte the Event it would have been refused as at its
    own write. Extracted rather than copied: two constructions of one id scheme is §8's defect.

    ⚠ **THE OCCASION IS APPENDED HERE, FOR EVERY EVENT THE ACT EMITS, REFUSAL OR SUCCESS** (IN-50).
    Every Event cites `[a.id]` and then `_occasion_ids`, the antecedent Events of the Scene that
    carried the act, de-duplicated and in that order. §39.2 line 2 says `causes[]` NAMES THE ACTS,
    which is necessary and not sufficient: an Event naming only the act that emitted it leaves the
    walk stopping dead at every decision, and `R3` could never fire from a real run (`N3`). A
    REFUSED act chosen from a scene another person's act-Event occasioned keeps the edge to that
    person. `self` is the driver, for `scenes`; an act with no scene has no occasion and cites
    its own id alone.

    ⚠ SC-02 `23`, LOADER INVARIANT 7 AT EXECUTION (`04 §B.13 #7`, `F.20b`): *"the log accepts no other
    kind"* -- the fold may mint only a kind the DERIVED roster (`data/verbs.py::EVENT_KINDS`, the
    union of every emission column and `rosters.yaml: fold_kinds`) holds. A kind outside it is a
    body literal come back, and
    it raises before the Event exists rather than reaching a log that would carry it. Scoped to the
    FOLD'S Events: a probe's hand-built Event is appended by the probe (`H-220`)."""
    if not EVENT_KINDS.issuperset(kinds):
        undeclared = sorted(k for k in kinds if k not in EVENT_KINDS)
        raise InstrumentDefect(
            f"act {a.id!r} ({a.verb}) would emit Event kind(s) {undeclared}, which no emission column "
            "declares. 04 §B.13 #7 / F.20b -- the Event-kind roster is derived from every emission "
            "column (verb rows' `emits`/`emits_on_refusal`, `write_matrix.yaml`, `rosters.yaml: "
            "fold_kinds`); a definition living as a literal in a body is what ID-12 refuses.")
    cited = list(dict.fromkeys([a.id, *self._occasion_ids(w, a)]))
    return [Event(H(w.world_seed, w.tick, a.actor, f"{k}:{a.id}"),
                  k, list(changes or []), list(cited), w.tick,
                  degree=degree, observed=observed)
            for k in kinds]


def _refuse_after_the_fact(self, w: "World", out: list, act_ids: list) -> None:
    """G4: REPLACE, IN PLACE, THE PROVISIONAL SUCCESS OF EVERY ACT WHOSE DEFERRED WRITE MOVED
    NOTHING, WITH THE ROW'S REFUSAL.

    `work`'s success is provisional by construction: `_fold` emits it when the act STAGES a
    non-zero delta, and only `resolve()`'s summed write says whether the site moved. When it did
    not, each staging act's Events -- contiguous in `out`, because `resolve` extends one act's
    at once -- are replaced where they stand by `emits_on_refusal`, carrying what a refusal at
    the act's own write would carry: `[a.id]` plus the act's occasion ids as cause (both through
    `_act_events`, IN-50), no changes, the same degree and the same precondition reads. `act_of`
    follows the replacement, so WITNESS attributes the refusal to the act and nothing keeps
    pointing at an Event that never entered the log."""
    for aid in dict.fromkeys(act_ids):
        at = [i for i, e in enumerate(out)
              if getattr(self.act_of.get(e.id), "id", None) == aid]
        if not at:
            continue
        if at != list(range(at[0], at[-1] + 1)):
            raise InstrumentDefect(
                f"act {aid!r}'s Events are not contiguous in RESOLVE's output ({at}); "
                f"`resolve` extends one act's Events at once, so something interleaved them")
        a = self.act_of[out[at[0]].id]
        row = VERB_TABLE.get(a.verb)
        first = out[at[0]]
        # `WRITE_CLAUSE` (plan position `19`): the accumulator's write moved nothing, which is F9's
        # refusal one step later -- the same clause a declining effect refuses at.
        refusal = _act_events(self, w,
                              a, _demand_earned(w, a, row.refusal_for(WRITE_CLAUSE), False) or (FOLD_REFUSED,),
                              degree=_refusal_degree(row, first.degree), observed=first.observed)
        for i in at:
            self.act_of.pop(out[i].id, None)
            # v9 FI-03: a find keyed on a replaced Event would outlive it (WITNESS pops by the ids it
            # is handed, and this one never enters the log), so it goes with the Event.
            self.findings.pop(out[i].id, None)
        out[at[0]:at[-1] + 1] = refusal
        for e in refusal:
            self.act_of[e.id] = a


# ---------------------------------------------------------------------------
# ⚠ `stratum_of` LIVES HERE FOR THE SAME REASON `sense` LIVES IN `deliberate.py`: RESOLVE is its
# only caller, and leaving it in `driver.py` would make this module import the driver that imports
# it back.
# ---------------------------------------------------------------------------

def stratum_of(a: "Act") -> int:
    """An Act's resolution stratum: its verb table row's, by index into the `strata` roster.

    `Act.stratum` is an int with a default, and a caller that sets it explicitly is taken at its
    word -- `A37` exercises the ordering that way. Everything else reads the table, which is
    where §27 actually puts the answer."""
    if a.stratum != Act.__dataclass_fields__["stratum"].default:
        return a.stratum
    row = VERB_TABLE.get(a.verb)
    if row is None or row.stratum not in STRATA:
        return a.stratum
    return STRATA.index(row.stratum)
