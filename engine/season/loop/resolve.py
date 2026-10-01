"""`loop/resolve.py` -- RESOLVE -- barrier 3, the only writing step for acts. `04 §A.2`: owns every ACTS row, through the gate, and the ordered fold; token ACTS.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.resolve = resolve`, so `SeasonDriver.resolve` IS this
function and `inspect.getsource(SeasonDriver.resolve)` returns THIS SOURCE. Eight tests read a
step's body that way -- three of them `witness`'s, one of those a pure NEGATIVE assertion --
and a stub would fail two and silently vacate the third, which is why step 9 of the
decomposition (ED-IN-0203) refused to delegate. Step 5 established the technique when
`class Query` bound module functions as staticmethods.

⚠ **THE TOKEN IS HANDED IN BY THE DRIVER (G2).** `SeasonDriver.season` mints an ACTS `Token`
through `loop/driver.py::mint_token` and passes it as `token`, once per round. `resolve` threads
it to `_fold` and `_fold` to `_apply_write`, each taking it as the argument after `w`; every gate
write below presents it. This module constructs none and calls no minter --
`tests/test_g2_token.py` fails if it does.
"""

from __future__ import annotations

import random
from ..data import files
from ..gaps import InstrumentDefect
from ..data.rosters import STRATA

from typing import Optional
from ..data.matrix import Step, matrix_row
from ..data.requires import UNKNOWN, Verdict, binding_from_act, evaluate
from ..data.verbs import (COUNTERPARTY_CLAUSE, ELIGIBILITY_CLAUSE, NO_PRECONDITION, VERB_TABLE,
                          WRITE_CLAUSE, VerbRow)
from ..gaps import Forbidden, Unspecified
from ..loop.effects import EFFECTS
from ..loop.predicates import REQUIRES_PREDICATES
from ..loop.sides import sides_of
from .. import manifest
from ..queries.world_q import WorldReader, ceiling, occasioned_by
from ..seam import ContestError, Resolution, contest, degree_of
from ..state.carriers import Act, Event, StateChange
from ..state.gate import Change, NoOpReceipt, Subject, Token, seat_hold
from ..state.ids import draw_factory, H
from ..state.world import World
from ..trace_log import TRACE



# -- RESOLVE -- barrier 3 -- the ONLY writing step for acts (S27) -------

def _canonical_order(w: "World", acts: list) -> list:
    """S27/S32 rest 3: FIVE STRATA, then a CONTENT-DERIVED hash key within each -- extracted
    from `resolve()`'s own sort (M4, `ED-IN-0279` clause (a)) so `loop/encounter.py` can fold a
    SUBSET of a round's acts in the SAME canonical order, rather than re-deriving the rule or
    skipping it (§8: it lives once). No `self`: the ordering is a pure function of the world's
    seed/tick and the acts themselves, not of driver state."""
    return sorted(acts, key=lambda a: (stratum_of(a),
                                       H(w.world_seed, w.tick, a.actor, f"order:{a.verb}:{a.id}")))


def _survives(self, w: "World", a: Act) -> list:
    """S27.1: a predecessor act can remove the actor. `[]` if `a.actor` is still in `w.persons`
    -- the caller folds normally. Otherwise an `act.ineligible` Event (already registered in
    `self.act_of`) that the caller should emit INSTEAD of folding.

    Extracted from `resolve()`'s own loop (M4) so `loop/encounter.py` shares the one check: a
    predecessor's act can remove a person just as easily inside RESOLVE as inside an earlier act
    of the SAME round's ENCOUNTER pass, and the reading is the fold's own rather than borrowed
    (see the inline comment this replaced, still true of both callers)."""
    if a.actor in w.persons:
        return []
    TRACE.decision(f"{a.actor} does not survive to act", "S27.1",
                   chose="emit `act.ineligible`; a predecessor removed the actor",
                   alternatives=["fold it anyway (the seam then sees a dead claimant)",
                                 "drop it silently (its act id never resolves)"])
    gone = [Event(H(w.world_seed, w.tick, a.actor, f"act.ineligible:{a.id}"),
                  "act.ineligible", [], [a.id], w.tick)]
    for _e in gone:
        self.act_of[_e.id] = a
    return gone


def _contests_of(a: Act, row: "VerbRow | None") -> list:
    """Which prize (if any) `a` contests: `a.contests` if the act itself names one, else the
    verb row's own `contests:` cell. Extracted (M4 review pass, `/simplify` finding): `resolve()`'s
    own loop and `loop/encounter.py::encounter` each wrote this expression independently, the same
    duplication `_canonical_order`/`_survives` were extracted to end (§8). No `self`: a pure
    function of the act and its row, not of driver state."""
    return list(a.contests or ()) or ([row.contests] if row and row.contests else [])


def _eligible(self, w: "World", a: Act, row: "VerbRow") -> bool:
    """§E4: eligibility admits `own`, `remit:<act>`, `hold:<object>`, `presence:<rung>` -- and
    NEVER `capability`, which the table loader already refuses. The kinds are a DISJUNCTION:
    `transfer` is eligible by `own` OR `hold:<store>`."""
    for alt in row.eligibility:
        kind, _, raw = alt.partition(":")
        kind, raw = kind.strip(), raw.strip()
        placeholder = raw.startswith("<") and raw.endswith(">")
        arg = raw.strip("<>")
        if kind == "own":
            return True                       # every person may attempt their own acts
        if kind == "remit":
            # ⚠ ADMITS ON THE TENURE'S SNAPSHOT, NOT THE LIVE OFFICE (position `13e`,
            # 2026-09-26). Was `off = w.offices.get(t.object); if off and arg in
            # off.remit_acts` -- a second reading of the same fact `decision/options.py`
            # already read off `t.granted_acts`, and the two could disagree (`epistemic.py`'s
            # `_ch_post_remit` docstring names the gap). `t.granted_acts` is the grant the
            # holder actually has; an office hand-mutated after seating does not reach it,
            # and an `establish` re-stamp does (`13f`).
            #
            # ⚠ G3: THE SEAT EXERCISED, NOT ANY SEAT HELD. This scanned EVERY live `hold` the
            # actor owned and admitted if any granted the act. `04:332` -- *"purview is asked of
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
            # ⚠ THE ARGUMENT IS COMPARED, as it is person-side. It was parsed and discarded
            # here too, so `hold:<store>` admitted anyone holding ANY object -- an
            # over-admission, and `G4` makes that a defect of equal weight to an
            # over-refusal. A `<...>` argument is a KIND, not an id, so it cannot be matched
            # and this declines rather than guessing which store the act meant (`H-75`).
            mine = [t for t in w.tenures
                    if t.subject == a.actor and t.kind == "hold" and t.until is None]
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
            # ⚠ NOT `return True`, and ⚠ THE REASON WAS CORRECTED BY `W6`'s ADVERSARIAL
            # PASS: this said "the presence index is `H-33` and does not exist", and `W6`
            # built it. What still declines the branch is `H-75` -- the argument is a
            # PLACEHOLDER naming a kind of rung, not an id, so there is nothing to look up.
            # predicate cannot be evaluated — and admitting on an unevaluable predicate is a
            # SILENT FILL off the register (G1) at the opposite polarity to §42.2, which sends
            # zero evidence to the verdict AGAINST. It refuses, and says which hole.
            #
            # It does NOT raise, because eligibility is a DISJUNCTION: `work` is `own |
            # presence:<site>` and `own` already admits, so raising here would refuse acts the
            # design permits. This branch declines and the loop tries the next alternative.
            TRACE.note(f"`presence:` eligibility is unevaluable (H-33, the presence index); "
                       f"declining this alternative for {a.verb}", "H-33")
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
    sc = self.scenes.get(getattr(a, "scene", None) or "")
    if sc is None:
        return []
    return [c for c in occasioned_by(w, getattr(sc, "occasion", None)) if c != a.id]

def _admits(self, w: "World", a: Act, row: "VerbRow") -> tuple:
    """§E2's FIRST TWO STEPS, FOR BOTH PATHS: eligibility, then `requires` against the world the
    predecessors left. Returns `(ok, refusal_kinds, verdict)`.

    ⚠⚠ THIS FUNCTION EXISTS BECAUSE THE CONTEST BRANCH SKIPPED BOTH OF THEM, and the defect was
    invisible while no contested verb could be chosen. §E2's order is *eligibility -> `requires`
    -> resolve*, and `resolve()` routed to the seam BEFORE `_fold` was entered -- so a contested
    act was carried into personal combat without its precondition ever being read. MEASURED the
    day `kill / wound` was admitted (`ED-IN-0261`, amended): 85 of 143 corpus cases became
    whole-case DESIGN-GAPs, 74 of them `PARTY-GAP` -- *claimant not a person: 'p_a' /
    'rec:cb377aad7694a2da'* -- because `opening_set` binds `subject` from the question's referent
    and a question's referent is usually a Record or a Rung. The row's own precondition says the
    subject is a living person and it was never asked.

    ⚠ THE FIX IS AN ORDERING, NOT A NEW RULE, which is why this is an extraction rather than a
    predicate: the eligibility test and the `requires` evaluation below are `_fold`'s, moved
    up so the two paths share ONE owner (§8). A `_fold`-local copy of them inside the contest
    branch would be the second resolver §27.2 forbids, arriving as a guard.

    ⚠ A REFUSED CONTESTED ACT EMITS AND IS WITNESSED. It does not raise and it is not dropped:
    `emits_on_refusal` is what a reader sees, the act still cost a scene, and the distinction
    between a LOSS (the contest ran and went against you) and a REFUSAL (it never ran) is the
    one the row's degree bands were built to keep."""
    # ⚠ PLAN POSITION `19`: EVERY REFUSAL BELOW IS `row.refusal_for(<clause>)` -- `04 §C.4`'s own
    # spelling, `emit(row.refusal_for(ELIGIBILITY))` / `emit(row.refusal_for(failed_conjunct))`.
    # On a FLAT row it is `row.emits_on_refusal`, byte for byte what these lines emitted before; on a
    # KEYED row (`data/verbs.py`, invariant 4's per-conjunct half) it is the failing clause's own kind,
    # so a refusal says WHICH clause refused -- the gap `★` measured on `confer`/`establish`/`revoke`,
    # whose refusals *"carry no conjunct"*.
    if not self._eligible(w, a, row):
        TRACE.decision(f"{a.actor} is not eligible for {a.verb}", "E4",
                       chose="emit the refusal", alternatives=["raise", "silently drop"])
        return (False, row.refusal_for(ELIGIBILITY_CLAUSE) or ("act.ineligible",),
                Verdict(UNKNOWN, ()))
    verdict = Verdict(UNKNOWN, ())
    if row.requires.strip() not in NO_PRECONDITION:
        if row.requires_typed is not None:
            # ⚠ THE TYPED CELL, AND `is True` RATHER THAN A TRUTH TEST. `evaluate` returns
            # three values, and UNKNOWN -- an operand the act does not carry, or a question
            # the world cannot answer -- must REFUSE. §42.2's polarity: zero evidence goes to
            # the verdict AGAINST the thing measured, so an unevaluable precondition is a
            # refusal and never a silent admission. That is the same polarity the untyped
            # branch below has always had, and the reason `work` (whose `_req_work` ended in
            # a bare `return True` for an act naming no site) now refuses instead.
            #
            # ⚠ `W-B`: THE VERDICT'S `observed` RIDES ON THE EVENT, AND THE REFUSAL'S READS
            # ARE THE INFORMATIVE ONES. This block used to say the reads were "deliberately
            # dropped here ... building the carrier before its reader exists is `ID-13`", and
            # the reader existed already: `belief_contradicts` evaluates the same cell against
            # `LedgerReader`, so a claim carrying `(subject, predicate, value)` is read by the
            # same code that produced the Observation. The carrier is no longer dead --
            # `SeasonDriver.witness` deposits it, gated on `observation_deposit_mode`.
            #
            # ⚠ ATTACHED TO SUCCESS AND REFUSAL ALIKE. A refusal's reads are WHY it refused --
            # `stores:grain -> 0` on an emptied hearth -- and it is the only read whose value
            # can make `belief_contradicts` fire, because `0 >= 1` is the one thing in this
            # grammar that evaluates False. Attaching only to the success would build the
            # channel and leave out the traffic.
            #
            # ⚠ POSITION `11a`: `S12.1`'s `floor` READ CAN RAISE HERE NOW, AND IT MUST BE CAUGHT
            # THE WAY `PARTY-GAP` ALREADY IS BELOW (`contest()`'s call, same file) -- NAMED,
            # NARROW, AND FALLING THROUGH TO THE ORDINARY REFUSAL. `WorldReader.read`'s `floor`
            # stem raises `Unspecified("S12.1", ...)` for a site KIND with no registered band
            # floors at all (`dwelling`/`garrison` ship `{}` ON PURPOSE, `24d-i`/M4) -- a real and
            # documented case, but before `11a` no Question's referent could ever BE a Site id
            # (Q1/Q3 were dead, Q2's admission test had no place clause), so `work`'s `site`
            # operand could never bind to a dwelling and this raise was unreachable. `reach`/
            # `place_of` (`queries/world_q.py`) make a claim about a co-located Site an ordinary
            # `claim_landed` question, so it is reachable now, and MEASURED: `p_npc_090` mints
            # `work` on `s_s_009_cottage_dwelling` in `build_realm(0)`'s very first season, which
            # crashed every populated-world test before this catch existed. This paragraph's own
            # polarity rule is what decides it: *"an unevaluable precondition is a refusal and
            # never a silent admission"* -- `no band floors for this kind` IS zero evidence, not a
            # software defect, so it resolves to `UNKNOWN` (refusal) rather than propagating.
            # `where == "S12.1"` is this ONE raise's own tag, so a FUTURE raise `WorldReader.read`
            # might grow for a different reason is not silently swallowed with it -- the same
            # discipline `PARTY-GAP`'s own catch states for `ENGINE-UNAVAILABLE`.
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
            ok = bool(pred(w, a))
        if not ok:
            TRACE.decision(f"{a.verb} by {a.actor}: precondition unmet", "E2/S27.1",
                           chose="emit the refusal -- scarcity falls out of the fold",
                           alternatives=["raise (no Event, no witness, no arc)"])
            # `verdict.failed` is the conjunct that decided it (`data/requires.py::evaluate`); a
            # predicate row and an unnamed cell carry `None`, which only a flat row reaches.
            return (False, row.refusal_for(verdict.failed) or ("act.refused",), verdict)
    # ⚠ PLAN POSITION `14` (U7-own): THE SECOND PARTY, ASKED HERE AND NOWHERE ELSE. `ED-IN-0210`
    # ruling 1 -- *a real interaction has a COUNTERPARTY*; a row naming its `counterparty:` operand
    # is refused when the act names nobody there, or names the actor (the `Tenure(X, X)` fiat). The
    # operand is read through `binding_from_act`, the one reader of an act's payload. ASKED AFTER
    # `requires`, so every refusal a row already keys to a conjunct keeps its attribution, and only
    # an act that passed its whole precondition reaches this. `opening_set` declines the same case
    # person-side, so no computed act is ever refused here; it replaces the per-effect copy
    # `_eff_petition` carried (a petition addressed to its petitioner).
    if row.counterparty:
        other = binding_from_act(a).get(row.counterparty)
        if other is None or other == a.actor:
            TRACE.decision(f"{a.verb} by {a.actor}: no second party on `{row.counterparty}`",
                           "ED-IN-0210", chose="emit the refusal",
                           alternatives=["admit a self-relation (a fiat)"])
            return (False, row.refusal_for(COUNTERPARTY_CLAUSE) or ("act.refused",), verdict)
    return (True, (), verdict)


def _fold(self, w: "World", token: Token, a: Act,
          resolution: "Resolution | None" = None) -> list[Event]:
    """ONE act through the table. This is what `effect` used to be, and the difference is
    that it is the SAME code for every act and every caller.

    ⚠ `resolution` IS WHAT THE SEAM RETURNED, AND IT IS THE PARAMETER `W-E` ADDED. It is
    `None` for every uncontested act, which is every act the corpus produces, and on that
    path nothing below changes: `writes_at(None)` and `emits_at(None)` on a verb with no
    degree map return the same flat tuples the fold has always applied. A CONTESTED act
    arrives here only from `resolve()`'s seam branch, carrying the band the subsystem's own
    result decided (`degree_of`)."""
    # OBSERVATION ONLY, AND DEDUPED BY ID (M4 review pass, `/code-review` finding). `w.acts`'s own
    # `append` is deliberately idempotent on a repeated id -- "the same act reached the store
    # twice by two entry points ... harmless, and deliberate" -- because RESOLVE's own Declared
    # fold and ENCOUNTER's real fold both call `_fold` for the SAME deferred act. `self.resolved`
    # is a plain list with no such guard, so a march act (or any future verb folding at two
    # steps) was recorded twice, inflating `len(self.resolved)` -- what `populated.py`'s own
    # `out["acts"]` reports -- for one act that reached resolution once. Guarding it the same way
    # `w.acts` already is closes the gap at its one owner rather than at every reader of the
    # count.
    # ⚠ `self._resolved_ids` IS THE O(1) COMPANION, NOT A SECOND LIST SCAN (M4 review pass,
    # `/simplify` efficiency finding). `resolved` is cumulative and NEVER RESET across a whole
    # campaign's many seasons, so `any(r.id == a.id for r in self.resolved)` costs O(current
    # length) on EVERY act's fold, not only march's -- O(N) per act over an N-act run,
    # `ActStore._by_id`'s own reason for existing, applied here the same way.
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
        # WHOSE GAP IS IT? Two different facts wear the same shape, and reporting them
        # alike is the mis-attribution G4 forbids: a verb #353 NAMES and Part E omits is a
        # HOLE IN THE SPECIFICATION (`utter`, `establish`, `exchange`, `succeed` were four,
        # and W3 filled them); a verb nobody names is THE CALLER'S INVENTION. The instrument
        # must not charge its own inventions to the design.
        named = not names_a_verb(a.verb)
        raise Unspecified(
            f"verb {a.verb!r} is on no row of the verb table", "S27/E2",
            needs=("a row in verb_table.yaml, ruled before it is added" if not named else
                   f"NOTHING FROM THE DESIGN -- #353 does not name {a.verb!r} as a verb. "
                   "This is the CALLER'S invention and the gap is the caller's"),
            law="§E2 -- the resolver's body IS the table. A verb the table does not carry has "
                "no semantics, and inventing them at the call site is the second resolver "
                "§27.2 forbids" + ("" if not named else
                ". ⚠ CHARGED TO THE INSTRUMENT, NOT THE DESIGN (register row H-64)"))

    # `W-B`. THE READS THIS ACT'S PRECONDITION MADE, ON EVERY EVENT THE ACT EMITS.
    # ⚠ DECLARED BEFORE `ev` AND REBOUND BY THE `requires` BLOCK BELOW, DELIBERATELY. `ev`
    # closes over the NAME, so it reads whatever `verdict` is bound to AT CALL TIME -- which
    # is `UNKNOWN, ()` for the ineligibility return above (eligibility reads tenures, not the
    # requirement, so it observed nothing) and the evaluated Verdict for every return after
    # it. The alternative -- passing `observed` as a parameter to all four `ev(...)` call
    # sites -- puts the same fact in four places, which is `§8` one seam over.
    verdict = Verdict(UNKNOWN, ())
    # `W-E`. THE THIRD BROKEN LINK: `Event.degree` was a declared field NOTHING EVER ASSIGNED
    # -- `ID-13`'s test applied to the epistemic layer's own outcome column. It is assigned
    # HERE, on the one path every act-emission takes (§8), rather than at the four `ev(...)`
    # call sites. `None` on every uncontested act, which is honest: no contest graded it.
    _degree = resolution.degree if resolution is not None else None

    def ev(kinds, causes, changes=None):
        return _act_events(w, a, kinds, causes, changes, _degree, verdict.observed)

    # §E2's first two steps, THROUGH THE ONE OWNER (`_admits`). They used to be written out
    # here, and writing them here is exactly what let `resolve()`'s contest branch skip them:
    # that branch never enters this function. `_admits`'s docstring carries the measurement.
    # ⚠ `verdict` IS REBOUND, and `ev` reads it at CALL time by closing over the NAME -- so a
    # refusal carries the reads that produced it and an ineligibility carries none, which is
    # honest (eligibility reads tenures, not the requirement).
    _ok, _refusal_kinds, verdict = self._admits(w, a, row)
    if not _ok:
        return ev(_refusal_kinds, [a.id])

    # Each `writes:` through the gate. The gate is the only writer; the fold never assigns.
    changed: list = []
    # Which of `emits:` the effect actually earned. Empty means "all of them", which is the
    # contract every effect returning a plain list keeps.
    earned: set = set()
    # ⚠ `writes_at(degree)`, NOT `row.writes` (#358 rev.2 §C.4 / invariant 12, 2026-09-03).
    # An UNCONTESTED verb has no `writes_by_degree`, so this returns the flat tuple and the
    # behaviour is identical -- the call is here so the new column HAS A READER. A column no
    # resolver consults is not a weak mechanism, it is one that does not exist (ID-13), and
    # this file already carries three instances of that defect found the hard way.
    #
    # ⚠ `W-E`, 2026-09-04. THIS LINE READ `_degree_for_writes = None  # the seam mints this
    # once H-98 rules the bands`, WITH A HARDCODED `None`, so `writes_at` was called for its
    # side effect of returning the flat tuple and no branch could ever be selected. That is
    # the first of the three links this item closed. The degree now arrives on `resolution`
    # from `resolve()`'s seam branch, minted by `degree_of` from what the SUBSYSTEM returned.
    #
    # ⚠ THE GUARD THE OLD COMMENT DESCRIBED IS STILL EXACTLY THE GUARD, and it is now the
    # reachable one rather than the hypothetical one: `writes_at(None)` on a contested verb
    # RAISES (`Unspecified`, `H-115`) rather than falling back to the union, so a caller that
    # folds a contested act WITHOUT a resolution fails loudly here instead of silently
    # writing the full kill. `test_h115_the_degree_branches_raise_unspecified_not_systemexit`
    # is that path, executed.
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
        # ⚠ THE EFFECT RUNS ONCE PER ACT, NOT ONCE PER PAIR. It ran per pair, so `move` --
        # which declares three -- closed and reopened the actor's containment three times and
        # minted three Tenures with the SAME id. Every pair is still GATED (class, Partition
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
                                         earned=earned, resolution=resolution)
                changed.extend(c for c in made if c not in changed)
        # ⚠ AN EFFECT THAT TOUCHED NOTHING DID NOT DO THE THING, AND MUST NOT EMIT THE
        # SUCCESS. `kill / wound`'s effect returns early when its payload names no subject --
        # which is every computed act, since §F1's Candidate carries no operands (`H-80`) --
        # and the fold then emitted `person.died` ANYWAY. Artifact 2 published four fabricated
        # deaths across a four-season run, into every ledger, and `person.died` is one of the
        # three endings §6.3's own chain check accepts. Found by the `W9` adversarial pass.
        #
        # ⚠⚠ G4: THIS IS NOW THE GATE'S JUDGMENT, CAUGHT HERE -- "CONVERTED AT THE FOLD BOUNDARY
        # INTO THE ROW'S REFUSAL KIND". It was `if eff is not None and not changed`, a check on
        # whether the effect REPORTED an id, which is exactly what `work` defeated: it reported its
        # site and changed nothing, so the check passed and `site.worked` shipped (F9). The gate
        # now reads every subject the effect names before and after the write and raises
        # `NoOpReceipt` when none moved; an effect that declines (`NO_CHANGE`) names none, so the
        # old falsy-return case lands here too, through one channel instead of two. The Event is
        # unchanged -- same kinds, same `[a.id]` cause, no changes -- so every refusal the old
        # check produced is byte-identical. What moved is that the WRITE is refused too: the trace
        # records it as refused (`F9`), where it used to record a write that changed nothing as
        # admitted. A refused first pair leaves the later pairs unchecked: a refused write
        # authorizes nothing after it.
        except NoOpReceipt:
            TRACE.decision(f"{a.verb} wrote nothing", "E3",
                           chose="emit the refusal, not the success",
                           alternatives=["emit `emits:` anyway (publishes an event for a "
                                         "state change that did not happen)"])
            return ev(row.refusal_for(WRITE_CLAUSE) or ("act.refused",), [a.id])
    # The act's proposed changes ride on the success Events -- §27.3's accumulator sums
    # them across the fold and clamps ONCE, which is order-independent as a fact.
    # ⚠ `[a.id]`, NOT `[ROOT]`, AND THIS WAS THE SUBSTRATE OF THE WHOLE NARRATIVE CLAIM.
    # §19.4: "an Event with NO ANTECEDENT declares `causes: [ROOT]`" — a campaign seed, a
    # clock's first emission. AN EVENT EMITTED BY AN ACT HAS AN ANTECEDENT: the act. Emitting
    # `[ROOT]` here made every Event in every season antecedent-free, so NO ARC WALKED
    # ANYWHERE — and #353 §19.4 says of exactly this: "the design rests its narrative layer,
    # audit trail and arc model on this edge -- 'the arc itself' -- and the measured state is
    # that the specified loop emits `causes=[]`, so the substrate of the entire
    # emergent-narrative claim is declared and never populated." `[ROOT]` is `[]` wearing a
    # marker.
    #
    # THE RULE IS ALREADY IN THIS FILE, ONE SEAM OVER. `resolve`'s contest branch passes
    # `causes=[a.id]` and its comment records why the "the id must already be in the log"
    # reading is wrong: `w.log` holds Events, an Act is never appended to it, so that
    # predicate is PERMANENTLY FALSE and reading it strictly produces `[ROOT]` forever.
    # §39.2 line 2 says `causes[]` NAMES THE ACTS. Found by running `headless.py`.
    # ⚠ ONLY THE KINDS THE EFFECT EARNED. An effect that returns a plain list earns all of
    # them, unchanged; one returning a mapping earns exactly the keys it filled. `confer`
    # declares `tenure.opened` AND `tenure.closed`, and conferring onto an unheld office
    # closes nothing -- publishing the second is a state change that did not happen.
    # ⚠ `W-E`, 2026-09-04: `emits_at(degree)`, NOT `row.emits`. THIS WAS THE SECOND BROKEN
    # LINK AND IT IS REGISTER ROW `H-113`: `VerbRow.emits_at` had ZERO CALLERS ANYWHERE IN
    # THE TRACER, verified by an independent read-only critic, so a contested verb reported
    # the FLAT UNION of every band -- `kill / wound` emitted `person.died` whether the target
    # died, was wounded, or walked away untouched. That is `ID-9`'s class (a success report
    # for something that did not happen) inside the epistemic layer, where every witness then
    # mints a claim from it. The `earned` intersection is UNCHANGED and still runs; it simply
    # intersects against the band's own kinds now instead of against all of them.
    _declared = row.emits_at(_degree)
    kinds = tuple(k for k in _declared if k in earned) if earned else _declared
    # ⚠ `[a.id]` ALONE WAS `N3`. §39.2 line 2 says `causes[]` NAMES THE ACTS, and that is
    # necessary and was treated as sufficient: an Event named the act that emitted it and
    # nothing named what occasioned the act, so the walk stopped dead at every decision and
    # `R3` — the only check the corpus failed — could never fire from a real run. The
    # occasion is on the Scene the act belongs to; `occasioned_by` turns it into the
    # antecedent Event ids. Adding them here rather than at the twelve `ev(...)` call sites
    # is `§8`: the rule lives once, on the one path every act-emission takes.
    return ev(kinds, [a.id] + self._occasion_ids(w, a), list(a.changes) + changed)


def _contest(self, w: "World", token: Token, a: Act, contests: list,
             contest_max_depth: Optional[int]) -> list:
    """S39.2, and M4's deferral fork (`ED-IN-0279` clause (a)). Extracted from `resolve()`'s own
    seam branch so RESOLVE and `loop/encounter.py` share the ONE body (§8) -- both call this for
    the same act, at different steps, and the STEP is what decides which of the two things it
    does.

    ⚠ ASSUMES `_admits` HAS ALREADY PASSED FOR `a`, AND NEVER RE-CHECKS IT. `resolve()`'s loop
    checks eligibility and `requires` once, before calling this, exactly as it always did; a
    caller reaching this function has already been admitted. ENCOUNTER's own selection is by the
    DECLARATION EVENT (`loop/encounter.py`), never by re-running this repo's own admission check
    against a world the whole round has since moved -- `_fold`, below, still runs its OWN
    internal `_admits` when it applies the writes, which is pre-existing behaviour on every
    contested verb today and not something this function adds or removes.

    TWO THINGS THIS DOES, chosen by comparing `w.step` to the prize's OWN manifest row:

    - THE PRIZE ROW DECLARES A `step:` THAT IS NOT THE ONE RUNNING NOW (M4): fold at the row's
      own `declares:` band, writing nothing -- the loop's own deferral token (`Declared`,
      `field_degree_bands`). The real fight happens later, when this SAME function is called
      again with `w.step` at the declared step.
    - OTHERWISE (every prize before M4, and a deferred prize once its step arrives): dispatch to
      the seam and fold at the degree the subsystem's own result decides, exactly as `resolve()`
      always did."""
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
    # NEVER on what `_target` happens to look like: `_target` is `payload[row.counterparty or
    # "subject"]` (below), and a candidate's `subject` binding to a Rung id is not unique to `march`
    # (`tell`'s TOPIC can name a place, though its `_target` is now the hearer `to`), so a
    # shape-based dispatch on `_target` is unsafe -- see `sides_of`'s own docstring for the corpus
    # case that found this.
    # ⚠ THE OPPONENT IS THE ROW'S `counterparty:` OPERAND WHEN IT NAMES ONE, ELSE `subject`
    # (telling workplan `T4`, `ED-IN-0282`): `tell` contests against its HEARER (`to`), not its
    # topic. `fight` and `march` name no counterparty and read `subject` exactly as before.
    _row = VERB_TABLE.get(a.verb)
    _target = ((a.payload or {}).get((_row.counterparty if _row is not None else "") or "subject")
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
    # that does not expect one, is what `_ten_seasons`-style tests (no `corpus_run.run_case`
    # exception wrapper around them) found the hard way.
    def _party_gap_refusal() -> list:
        # ⚠ `or ("act.refused",)`, MATCHING EVERY SIBLING FALLBACK (`_admits`, `_fold`,
        # `_refuse_after_the_fact`) -- found missing in the M4 review pass's own correctional
        # round: a verb with an empty `emits_on_refusal:` (or a hand-built Act naming no real
        # verb row at all) produced ZERO Events here, a silent drop, where every other refusal
        # path in this module already falls back.
        row = VERB_TABLE.get(a.verb)
        kinds = (row.emits_on_refusal if row is not None else ()) or ("act.refused",)
        produced = _act_events(w, a, kinds, [a.id])  # `_act_events` owns the id scheme (§8)
        for _e in produced:
            self.act_of[_e.id] = a
        return produced
    if not _parties:
        return _party_gap_refusal()
    # ⚠⚠ `U1`: THE DRIVER CONSTRUCTS THE GENERATOR, AND `04 §C.12`'s REJECTION 4 IS LOAD-BEARING.
    # `purpose` stays `roll:<prize>:<act id>`, provider-specific by design -- see `resolve()`'s
    # own history (`git log` on this file) for the fuller account of why.
    _rng = draw_factory(w.world_seed, lambda: w.tick)(a.actor, f"roll:{contests[0]}:{a.id}")
    # ⚠ `subject IS None` REACHES HERE TOO, AND IT IS THE SAME SHAPE OF GAP AS EMPTY `_parties`
    # (M4, found by `valoria-critic`'s adversarial pass, not anticipated in the build). `sides_of`
    # returns `subject = holder_faction_of(w, target)`, `None` for any Rung with no HELD ancestor
    # -- `H-149` permits an unheld settlement as a march target, and the corpus has several
    # (`populated.py`'s `Uncontrolled` provinces). Every wrapper (`combat.py`, `sigma.py`,
    # `mass_battle.py`) reports that shape as `status="PARTY-GAP"`, and `seam/contest.py` raises
    # `Unspecified(needs="PARTY-GAP", ...)` for ANY non-RESOLVED status -- uncaught here before
    # this fix, so a march on an unheld target crashed the whole season. Caught by `needs`, not by
    # pre-checking `_subject` before the call, because PARTY-GAP is the WRAPPER's own vocabulary
    # for every shape of missing party (empty claimants, wrong-typed claimant, no subject, no
    # rung) and a pre-check here would have to re-enumerate all of them to stay in sync.
    try:
        r = contest(w, rung=_rung, prize=contests[0], claimants=_parties, depth=0,
                    max_depth=contest_max_depth, causes=[a.id], verb=a.verb, subject=_subject,
                    rng=_rng)
    except Unspecified as e:
        # ⚠ ONLY `PARTY-GAP` IS CAUGHT, DELIBERATELY (M4 review pass, `/simplify` altitude
        # finding, corrected once more by a second correctional pass). `ENGINE-UNAVAILABLE`
        # (a wrapper's subsystem failed to import/compose) is a software defect and stays
        # uncaught and loud on purpose -- swallowing it into a graceful `march.refused` would
        # hide a real infrastructure failure behind a plausible-looking game Event.
        # ⚠⚠ `sigma.py`'s own `REFUSED` (S27.4, `Ob > 2x Pool`) is NOT a software defect -- it is
        # a normal game refusal, and mischaracterizing it as one was this comment's own first
        # writing. It is PRE-EXISTING: `tell` already reaches an uncaught `Unspecified` on it
        # today, unrelated to march, and this fix neither created nor closes that gap -- widening
        # the catch to cover it is a `social_contest`-lane decision, outside what this pass may
        # decide. `e.needs` is a free-text field elsewhere in this codebase
        # (`manifest/registry.py`, `harness/probes.py`), matched by string rather than a typed
        # exception subclass, because `seam/contest.py` forwards a wrapper's raw `status` value
        # verbatim only at this one raise site -- a real but separate seam-contract gap, not
        # widened here.
        if e.needs == "PARTY-GAP":
            return _party_gap_refusal()
        raise
    if isinstance(r, ContestError):
        TRACE.note(f"contest returned {r}", "S39.3")
        return []
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


def _apply_write(self, w: "World", token: Token, a: Act, kind: str, fld: str, eff=None,
                 earned: Optional[set] = None,
                 resolution: "Resolution | None" = None) -> list:
    """The fold's write. It carries no per-verb behaviour -- the effect of a write is the
    matrix row's business, and what a verb writes is the verb table's.

    ⚠ IT NOW RETURNS THE `StateChange`s THE WRITE MADE, and that is what lets an Event say
    WHAT IT CHANGED. Before, an Event's `changes[]` was whatever the CALLER had put on the
    Act -- so a computed act, which is every act after `W5`, emitted an Event changing
    nothing. The fold knows what it wrote. Without this `H-79`'s `per_change` rule has nothing
    to read and §F1's Q2 clause "a claim whose subject is something they hold" stays
    unreachable, which is how the narrative substrate stayed empty through four revisions.

    G4: "what it wrote" is now the GATE'S answer -- the receipts `World.write` minted for the
    subjects that moved -- where it was the effect's report. An effect naming a subject that did
    not move gets no receipt for it; one naming nothing that moved raises `NoOpReceipt`, which
    `_fold` turns into the refusal."""
    # ⚠ G2: ASKED FOR ITS SIDE EFFECT ONLY. This was `mrow = matrix_row(kind, fld)` and `mrow` fed
    # the class below. The class now comes from the driver's token, so the row is no longer read
    # here -- but the call still raises `Unspecified` for an absent row BEFORE `World.write` is
    # reached, and `World.write` would raise the same thing only after logging a refused
    # `TRACE.write` line. Kept so a signature move does not also move `runs/TRACE.txt`.
    matrix_row(kind, fld)
    earned = earned if earned is not None else set()
    # G2: THE DRIVER'S ACTS TOKEN, NOT `mrow.write_class(Step.RESOLVE)`. The old expression was the
    # one non-literal class in the tree, and it was CIRCULAR -- `World.write` computes the same
    # `STEP_CLASS[step]` from the same map, so S30.2's check could not fail for any fold write
    # (`test_w3_the_write_class_check_still_refuses_a_wrong_class` named that limit). The token is
    # a second source: a driver that handed RESOLVE a MATTER token would now be refused.
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
    # ⚠ `W-E`: EVERY EFFECT TAKES THE RESOLUTION, AND UNIFORMLY. `H-114` measured the
    # alternative -- `_eff_kill` took no degree, so the effect that computes the VALUES could not
    # honour the branch `writes_at` had just selected, and a fold at degree `Wounded` DELETED THE
    # PERSON. One signature for all twelve rather than an inspect-the-callable dispatch: a fold
    # that passes different arguments to different effects has a second contract nobody declared.
    #
    # ⚠⚠ G4: THE EFFECT RUNS HERE, BEFORE THE WRITE, AND WRITES NOTHING -- IT RETURNS THE CHANGE.
    # `04 §C.2`'s signature is `gate.write(token, kind, field, id, change, ...)`: the change is an
    # ARGUMENT, computed by the caller and applied by the gate. Before G4 the effect ran INSIDE
    # the gate's `apply()` and reported ids after the fact, so the gate could not read a subject
    # before it moved. One consequence, stated: an effect's own refusal to be built (`_operand`'s
    # `InstrumentDefect`, `kill / wound`'s `Unspecified`) now raises before the gate's class and
    # step checks rather than after them -- both are call-site defects and neither mutates.
    change = eff(w, a, resolution)
    got = w.write(fld, token, None, record_kind=kind, fieldname=fld, driver="Act",
                  actor=a.actor, via=a.via, change=change)
    # ⚠ AN EFFECT MAY EARN SOME OF ITS DECLARED KINDS AND NOT OTHERS. A subject that earns `None`
    # earns *all* of them (the original plain-list contract); a named kind earns only that one.
    # Without this the fold emitted EVERY kind in `emits:` the moment anything changed -- so
    # `confer` onto an unheld office published `tenure.closed` with nothing closed. That is the
    # fabricated-`person.died` class committed INSIDE the fix for it. Found by the
    # governance-slice adversarial pass. G4: a kind is earned by a subject that MOVED, which the
    # gate decides, not by one the effect listed.
    for s, _r in got:
        if s.earns:
            earned.add(s.earns)
    # G1a -> G4. THE GATE MINTED THESE, INSIDE THE WRITE, FOR THE SUBJECTS THAT MOVED AND NO OTHER.
    # They were minted here, after `w.write` returned, for every id the effect REPORTED -- which is
    # how a no-op receipt (`before == after`) came to be issued by the gate and admitted by the log.
    return [r for _s, r in got]

def resolve(self, token: Token, acts: list[Act],
            contest_max_depth: Optional[int] = None) -> list[Event]:
    w = self.w
    w.step = Step.RESOLVE
    w.frozen = False
    TRACE.step("RESOLVE", "enter"); TRACE.barrier(3, "RESOLVE")
    w.discard_caches()

    # S27: FIVE STRATA, then S32 rest 3's CONTENT-DERIVED canonicalization WITHIN each.
    # This sorts ONE GLOBAL ARRAY, which is exactly why RESOLVE DOES NOT PARTITION (S31).
    # ⚠ THE STRATUM COMES FROM THE VERB TABLE, NOT FROM THE ACT'S DEFAULT. `VerbRow.stratum`
    # is a NAME (`social`, `movement`) validated against the roster at load; `Act.stratum` is
    # an INT defaulting to 4, and NOTHING MAPPED ONE ONTO THE OTHER -- so every computed act
    # resolved at 4 whatever its verb, and §27's five-strata ordering was INERT. `rosters.yaml`
    # says of that roster "ORDER IS SEMANTIC HERE... editing the order changes which acts see
    # which world", which described a column no resolver read. Found by the `W9` adversarial
    # pass. An act that names its own stratum still wins, so a caller can still test the
    # ordering directly (`A37`). Extracted to `_canonical_order` (M4) so `loop/encounter.py`
    # can fold a subset of a round's acts in the same order without a second copy of the rule.
    ordered = _canonical_order(w, acts)
    TRACE.decision(f"ordering {len(acts)} acts", "S27/S32",
                   chose="five strata, then a content-derived hash key over one global array",
                   alternatives=["completion order", "rank", "per-container sort (voids the fold)"])

    out: list[Event] = []
    # S27.3 SUM-THEN-CLAMP-ONCE accumulator. ⚠ G4: IT IS `World._staged` NOW, NOT A LOCAL HERE,
    # because an act's `work` WRITES to it through the gate (`_eff_work`'s docstring). Anything
    # staged before this pass came from a bare `_fold` outside any RESOLVE -- a test calling the
    # fold directly -- and belongs to no ordered fold, so it is discarded rather than applied.
    w.take_staged()
    for a in ordered:
        # G1a. THE ACT ENTERS THE STORE BEFORE IT IS FOLDED, and the order is the whole point:
        # every branch below emits `causes=[a.id]`, INCLUDING the two refusal branches, so an
        # act recorded only on success would leave every refusal chain unresolvable -- which is
        # the case the act store's own header names. Appended once per act, here, rather than at
        # each of the five emission sites: `CLAUDE.md` §8, and five sites is five chances to
        # forget the one that refuses.
        w.acts.append(a)
        # ⚠⚠ S27.1 SAID SO ALL ALONG: *each act sees the world its predecessors left.* A
        # PREDECESSOR CAN REMOVE THE ACTOR, and until a person could be killed inside the fold
        # nothing ever tested what the successor does. The answer is that he does not act: acts
        # are minted for everyone at DELIBERATE, resolved in stratum order at RESOLVE, and a man
        # felled in the third act of the season is not there for the ninth. Extracted to
        # `_survives` (M4) so `loop/encounter.py` shares the one check.
        _gone = self._survives(w, a)
        if _gone:
            out.extend(_gone)
            continue
        # S27.4: an attempt at Ob > 2 x Pool is REFUSED, and the season is spent. An
        # uncontested attempt routes to a GATE, never to an Ob = 0 roll.
        mult = w.fixtures.get("obstacle_refusal_multiple")
        if a.obstacle is not None and a.obstacle > mult * max(a.pool or 0, 0):
            # ⚠ `[a.id]`, NOT `[ROOT]`. A REFUSED ATTEMPT HAS AN ANTECEDENT — THE ATTEMPT.
            # This read `[ROOT]`, and the rule against it is stated TWICE in this file within
            # sixteen lines: the contest branch below passes `causes=[a.id]`, and `_fold`
            # carries a paragraph saying `[ROOT]` in an act-caused emission is "`[]` wearing a
            # marker". The rule was written on both sides of this line and violated between
            # them. It made `W4`'s headline claim — *"`[ROOT]` only for the seed and a licensed
            # clock's genuine first emission"* — FALSE OF THE DESIGN while true of the fixture,
            # because `Act.obstacle` defaults to `None` and the computed chooser never sets
            # one, so no test could reach it. Found by the `W4` adversarial pass.
            out.append(Event(H(w.world_seed, w.tick, a.actor, f"refused:{a.id}"),
                             "attempt.refused", [], [a.id], w.tick))
            TRACE.decision(f"{a.actor} attempted Ob={a.obstacle} against Pool={a.pool}",
                           "S27.4", chose="refuse; the season is spent",
                           alternatives=["roll it anyway", "route to an Ob=0 roll"])
            continue
        # S39.2 line 1: loop -> subsystem, when an act contests something.
        #
        # ⚠ THE VERB'S COLUMN, NOT ONLY THE ACT'S FIELD, AND THAT IS WHY THE SEAM NEVER FIRED.
        # `ARCHITECTURE_V2.md:394` puts `contests:` on the VERB ROW — *"if set, routes to the
        # seam at RESOLVE"* — and `:434` sets it on `kill / wound`. This read only `a.contests`,
        # which no chooser sets, so a kill took the EFFECT path and wrote a death directly.
        # Jordan, 2026-09-02: *"that…would trigger the personal combat scene. you can't just
        # kill or wound imo."* The design said so at `:434` and the instrument did not read it.
        _row = VERB_TABLE.get(a.verb)
        _contests = _contests_of(a, _row)
        if _contests:
            # ⚠⚠ §E2's ORDER, RESTORED: ELIGIBILITY AND `requires` BEFORE THE SEAM, NOT AFTER IT.
            # This branch used to route straight into personal combat, so a contested act's
            # precondition was never read -- `_fold`, which owns that check, is the branch this
            # one is the alternative to. The defect could not be seen while no contested verb was
            # choosable; admitting `kill / wound` made it 85 whole-case DESIGN-GAPs in one run.
            # `_admits` carries the measurement and is the single owner (§8).
            #
            # ⚠ A REFUSAL HERE IS AN EVENT, NOT A RAISE. The act happened and was witnessed; what
            # did not happen is the contest. `emits_on_refusal` -- `kill.refused` on the one row
            # that reaches this today -- is the kind, and `causes=[a.id]` keeps the chain
            # resolvable exactly as the two refusal branches in `_fold` do.
            _ok, _refusal_kinds, _verdict = self._admits(w, a, _row) if _row else (True, (), None)
            if not _ok:
                produced = [Event(H(w.world_seed, w.tick, a.actor, f"{k}:{a.id}"),
                                  k, [], [a.id], w.tick,
                                  observed=_verdict.observed if _verdict else ())
                            for k in _refusal_kinds]
                for _e in produced:
                    self.act_of[_e.id] = a
                out.extend(produced)
                continue
            # S39.2 line 2 onward: dispatch to the seam, or defer to ENCOUNTER, and fold at the
            # degree either one decides. Extracted to `_contest` (M4, `ED-IN-0279` clause (a))
            # so RESOLVE and `loop/encounter.py` share the one body -- see that function's own
            # docstring for the deferral fork and why it does not re-check `_admits`, just
            # confirmed above. `_contest` always returns a list -- a depth-capped
            # `ContestError` is converted to `[]` inside it, once, so this loop and
            # `loop/encounter.py`'s own do not each carry a second copy of that check.
            produced = self._contest(w, token, a, _contests, contest_max_depth)
        else:
            # S27.1: CONTENTION IS AN ORDERED FOLD. Each act sees the world its predecessors
            # left. SEQUENCE, NOT SIMULTANEITY -- and NO ACT NEEDS TO KNOW ANOTHER EXISTED.
            produced = self._fold(w, token, a)
        # ⚠ `W-E`: THE TWO PATHS SHARE THE BOOKKEEPING BELOW, AND THAT IS §8 RATHER THAN
        # TIDINESS. The contest branch used to `continue` past all of it, so a contested act's
        # Events were never entered in `act_of` and its deltas never reached §27.3's
        # accumulator. The moment the seam started returning something the fold could write,
        # duplicating those three loops inside the branch would have been the second copy of
        # a rule that gets to disagree with the first.
        # ⚠ WHICH ACT EMITTED WHICH EVENT, recorded once here rather than re-derived from the
        # id hash by every consumer. WITNESS needs it to answer *what is this deposit ABOUT*
        # for an Event that wrote nothing: an act that changes no state has an empty
        # `changes[]`, and the only thing that knows what it named is the act.
        # ⚠ **RESOLVER-SIDE AND CUMULATIVE ACROSS SEASONS — NOT season-local, and the
        # difference is load-bearing.** `resolved`, `scenes` and `act_of` are never reset by
        # `season()`, and `R3` REQUIRES that: a claim deposited at WITNESS in season *t* is
        # read at DELIBERATE in *t+1*, so the act that occasioned this one is a PREVIOUS
        # season's act and must still be reachable. A session that makes these three
        # season-local to tidy them blinds the propagation check silently — it would still
        # pass, on zero.
        for _e in produced:
            self.act_of[_e.id] = a
        # ⚠ G4: THE `for ch in e.changes: if isinstance(ch.delta, int): pending[...]` LOOP THAT
        # STOOD HERE IS GONE. It fed §27.3's accumulator off the success EVENTS, so any verb whose
        # act rode an integer delta on its `changes[]` moved a site whose `Site.condition` its
        # row never declared -- and it could not tell the accumulator WHICH acts a site's total
        # came from, which is what judging that total's write needs. `_eff_work` stages its own
        # delta through the gate instead (`World.stage`).
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
    # same way -- where the old loop skipped it silently and left every `site.worked` standing.
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
        # scale when no works names the site, so the bound is unchanged for every site in every world
        # built before `24e`. ⚠ `max(condition, ceiling)`, NOT r2's bare `ceiling`: the ceiling bounds
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
        TRACE.decision(f"clamping {sid}.condition", "S27.3",
                       chose=f"sum {deltas} = {total}, then clamp ONCE",
                       alternatives=["clamp per delta (arrival-order dependent)"])
    TRACE.step("RESOLVE", "leave")
    return out


def _act_events(w: "World", a: Act, kinds, causes, changes=None, degree=None,
                observed=()) -> list:
    """THE ONE SHAPE OF AN ACT'S EMISSION: one Event per kind, its id `H(seed, tick, actor,
    "<kind>:<act id>")`. `_fold`'s `ev` is this with the act's degree and verdict bound; the
    accumulator's after-the-fact refusal (G4) is this with the success Event's, so a `work`
    refused at the accumulator is byte-for-byte the Event it would have been refused as at its
    own write. Extracted rather than copied: two constructions of one id scheme is §8's defect."""
    return [Event(H(w.world_seed, w.tick, a.actor, f"{k}:{a.id}"),
                  k, list(changes or []), list(causes), w.tick,
                  degree=degree, observed=observed)
            for k in kinds]


def _refuse_after_the_fact(self, w: "World", out: list, act_ids: list) -> None:
    """G4: REPLACE, IN PLACE, THE PROVISIONAL SUCCESS OF EVERY ACT WHOSE DEFERRED WRITE MOVED
    NOTHING, WITH THE ROW'S REFUSAL.

    `work`'s success is provisional by construction: `_fold` emits it when the act STAGES a
    non-zero delta, and only `resolve()`'s summed write says whether the site moved. When it did
    not, each staging act's Events -- contiguous in `out`, because `resolve` extends one act's
    at once -- are replaced where they stand by `emits_on_refusal`, carrying what a refusal at
    the act's own write would carry: `[a.id]` alone as cause, no changes, the same degree and the
    same precondition reads. `act_of` follows the replacement, so WITNESS attributes the refusal
    to the act and nothing keeps pointing at an Event that never entered the log."""
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
        refusal = _act_events(w, a, row.refusal_for(WRITE_CLAUSE) or ("act.refused",), [a.id],
                              degree=first.degree, observed=first.observed)
        for i in at:
            self.act_of.pop(out[i].id, None)
        out[at[0]:at[-1] + 1] = refusal
        for e in refusal:
            self.act_of[e.id] = a


# ---------------------------------------------------------------------------
# ⚠ `names_a_verb` AND `stratum_of` LIVE HERE FOR THE SAME REASON `sense` LIVES IN `deliberate.py`:
# RESOLVE is their only caller, and leaving them in `driver.py` made this module import the driver
# that imports it back -- a cycle the tree's own count test caught on the first cut.
# ---------------------------------------------------------------------------

def names_a_verb(verb: str) -> bool:
    """Does #353 mention this word AT ALL? Asked of the source, never of a list.

    ⚠ THE FIRST VERSION WAS A HARDCODED LIST OF EIGHT, and the probe corpus invents at least
    fifteen — `v4`, `v0`, `buy_grain`, `petition2`, `report_truthfully`, `leverage`, `purge` were
    all missing from it. So HALF the gaps the fold reported were billed to the SPECIFICATION,
    telling a reader that #353 owes a row for `purge`. That is the mis-attribution the branch
    below exists to prevent, committed by the mechanism meant to prevent it. A list of names is a
    router and routers miss (`G2`); the property is cheap and cannot be spelled around.

    ⚠ IT TESTS MENTION, NOT VERBHOOD, and the weaker claim is the honest one. A backtick test was
    tried first and is wrong: #353 writes `confer` and `transfer` in backticks but `move` and
    `utter` bare, so the stricter property called two verbs it DOES name inventions. The
    consequence of the weaker test is over-attribution to the design in one direction only — a
    word #353 uses in ordinary English (`act`, `do`) reads as named — which is the SAFE direction:
    it never tells a reader the design owes a row for `purge`.

    ⚠ `speak` and `forge` occur ZERO times in #353. V2's Part E added them and declared them
    `assumption`, which V2 §1.2 says in as many words. They are declared additions, not silent
    inventions, and the table is where that declaration lives."""
    import re as _re
    return bool(_re.search(r"\b" + _re.escape(verb) + r"\b", SOURCE_353_TEXT()))


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


_S353_CACHE: list = []

# ---------------------------------------------------------------------------
# ⚠ `SOURCE_353_TEXT` (and its cache) MOVED HERE AT L5's SECOND CUT, for the same reason `sense` sits
# in `deliberate.py`: `names_a_verb` is its only reader and lives here, so leaving it in `driver.py`
# left `resolve <-> driver` cycling. The tree's cycle-count test named it twice -- once for
# `deliberate` and once for this -- which is the argument for a count over a roster: it kept naming
# what was left rather than passing on the half that was fixed.
# ---------------------------------------------------------------------------

def SOURCE_353_TEXT() -> str:
    if not _S353_CACHE:
        f = files.SOURCE_353_MD
        if not f.exists():
            # ⚠ THIS USED TO BE `else ""`, AND IT WAS A FAIL-OPEN IN THE WORST DIRECTION.
            # `names_a_verb` regex-searches this text; over an empty string EVERY verb reads as
            # NOT named by the design, so every gap the fold reports is billed to the
            # SPECIFICATION. That is the exact mis-attribution `names_a_verb`'s own docstring
            # says it exists to prevent ("telling a reader that #353 owes a row for `purge`"),
            # and it fired silently — measured before the fix: with the source absent,
            # `names_a_verb("move")` returned False for a verb #353 genuinely names.
            # An absent source is an INSTRUMENT problem, not a design gap, so it raises the
            # kind that is deliberately NOT a `ShapeGap` and cannot reach the design-gap column.
            raise InstrumentDefect(
                f"the #353 design source is not at {f}, where `season.data.files` anchors it. "
                "SOURCE_353_TEXT() has no honest answer without it: `names_a_verb` regex-searches "
                "this text, so an empty string makes EVERY verb read as not-named-by-the-design "
                "and bills every reported gap to the specification. Restore the file, or "
                "re-anchor files.SOURCE_353_MD.")
        _S353_CACHE.append(f.read_text())
    return _S353_CACHE[0]
