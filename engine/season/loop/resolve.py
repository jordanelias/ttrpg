"""`loop/resolve.py` -- RESOLVE -- barrier 3, the only writing step for acts. `04 §A.2`: owns every ACTS row, through the gate, and the ordered fold; token ACTS.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.resolve = resolve`, so `SeasonDriver.resolve` IS this
function and `inspect.getsource(SeasonDriver.resolve)` returns THIS SOURCE. Eight tests read a
step's body that way -- three of them `witness`'s, one of those a pure NEGATIVE assertion --
and a stub would fail two and silently vacate the third, which is why step 9 of the
decomposition (ED-IN-0203) refused to delegate. Step 5 established the technique when
`class Query` bound module functions as staticmethods.

⚠ **THE TOKEN IS STILL A `WriteClass` PARAMETER AND THAT IS G2's, NOT THIS UNIT's.** `04 §A.3`
row 3 replaces the parameter with an unforgeable token type minted only by the driver; until
that lands, this step passes `WriteClass` exactly as it did inside the class. Unit L5
delivers the MODULE boundary `04 §A.2:134` requires; the write discipline is Arc 2.
"""

from __future__ import annotations
from ..data import files
from ..gaps import InstrumentDefect
from ..data.rosters import STRATA

from typing import Optional
from ..data.matrix import Step, WriteClass, matrix_row
from ..data.requires import UNKNOWN, Verdict, binding_from_act, evaluate
from ..data.verbs import NO_PRECONDITION, VERB_TABLE, VerbRow
from ..gaps import Forbidden, Unspecified
from ..loop.effects import EFFECTS
from ..loop.predicates import REQUIRES_PREDICATES
from ..queries.world_q import WorldReader, occasioned_by
from ..seam import ContestError, Resolution, contest, degree_of
from ..state.carriers import Act, Event, StateChange
from ..state.ids import H
from ..state.world import World
from ..trace_log import TRACE



# -- RESOLVE -- barrier 3 -- the ONLY writing step for acts (S27) -------
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
            for t in w.tenures:
                if t.subject == a.actor and t.kind == "hold" and t.until is None:
                    off = w.offices.get(t.object)
                    if off and arg in off.remit_acts:
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

def _fold(self, w: "World", a: Act, resolution: "Resolution | None" = None) -> list[Event]:
    """ONE act through the table. This is what `effect` used to be, and the difference is
    that it is the SAME code for every act and every caller.

    ⚠ `resolution` IS WHAT THE SEAM RETURNED, AND IT IS THE PARAMETER `W-E` ADDED. It is
    `None` for every uncontested act, which is every act the corpus produces, and on that
    path nothing below changes: `writes_at(None)` and `emits_at(None)` on a verb with no
    degree map return the same flat tuples the fold has always applied. A CONTESTED act
    arrives here only from `resolve()`'s seam branch, carrying the band the subsystem's own
    result decided (`degree_of`)."""
    self.resolved.append(a)      # observation only -- decides nothing, see `resolved`
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
        return [Event(H(w.world_seed, w.tick, a.actor, f"{k}:{a.id}"),
                      k, a.actor, list(changes or []), list(causes), w.tick,
                      degree=_degree, observed=verdict.observed)
                for k in kinds]

    if not self._eligible(w, a, row):
        TRACE.decision(f"{a.actor} is not eligible for {a.verb}", "E4",
                       chose="emit the refusal", alternatives=["raise", "silently drop"])
        return ev(row.emits_on_refusal or ("act.ineligible",), [a.id])

    # `requires`, AGAINST THE WORLD THE PREDECESSORS LEFT -- which is the whole of §27.1.
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
            # ⚠ `W-B`: THE VERDICT'S `observed` NOW RIDES ON THE EVENT, AND THE REFUSAL'S
            # READS ARE THE INFORMATIVE ONES. This block used to say the reads were
            # "deliberately dropped here ... building the carrier before its reader exists is
            # `ID-13`", and the reader existed already: `belief_contradicts` evaluates the same
            # cell against `LedgerReader`, so a claim carrying `(subject, predicate, value)` is
            # read by the same code that produced the Observation. The carrier is no longer
            # dead -- `SeasonDriver.witness` deposits it, gated on `observation_deposit_mode`.
            #
            # ⚠ ATTACHED TO SUCCESS AND REFUSAL ALIKE. A refusal's reads are WHY it refused --
            # `stores:grain -> 0` on an emptied hearth -- and it is the only read whose value
            # can make `belief_contradicts` fire, because `0 >= 1` is the one thing in this
            # grammar that evaluates False. Attaching only to the success would build the
            # channel and leave out the traffic.
            verdict = evaluate(row.requires_typed, WorldReader(w, a.actor),
                               binding_from_act(a))
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
            return ev(row.emits_on_refusal or ("act.refused",), [a.id])

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
        for n, pair in enumerate(_pairs):
            kind, _, fld = pair.partition(".")
            # The effect runs ONCE, on the first pair: a verb writing three cells is ONE
            # operation, and running it per pair minted three Tenures for one `move`.
            made = self._apply_write(w, a, kind, fld, eff if n == 0 else None,
                                     earned=earned, resolution=resolution)
            changed.extend(c for c in made if c not in changed)
        # ⚠ AN EFFECT THAT TOUCHED NOTHING DID NOT DO THE THING, AND MUST NOT EMIT THE
        # SUCCESS. `kill / wound`'s effect returns early when its payload names no subject --
        # which is every computed act, since §F1's Candidate carries no operands (`H-80`) --
        # and the fold then emitted `person.died` ANYWAY. Artifact 2 published four fabricated
        # deaths across a four-season run, into every ledger, and `person.died` is one of the
        # three endings §6.3's own chain check accepts. Found by the `W9` adversarial pass.
        if eff is not None and not changed:
            TRACE.decision(f"{a.verb} wrote nothing", "E3",
                           chose="emit the refusal, not the success",
                           alternatives=["emit `emits:` anyway (publishes an event for a "
                                         "state change that did not happen)"])
            return ev(row.emits_on_refusal or ("act.refused",), [a.id])
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

def _apply_write(self, w: "World", a: Act, kind: str, fld: str, eff=None,
                 earned: Optional[set] = None,
                 resolution: "Resolution | None" = None) -> list:
    """The fold's write. It carries no per-verb behaviour -- the effect of a write is the
    matrix row's business, and what a verb writes is the verb table's.

    ⚠ IT NOW RETURNS THE `StateChange`s THE WRITE MADE, and that is what lets an Event say
    WHAT IT CHANGED. Before, an Event's `changes[]` was whatever the CALLER had put on the
    Act -- so a computed act, which is every act after `W5`, emitted an Event changing
    nothing. The fold knows what it wrote; an effect returns the ids it touched. Without this
    `H-79`'s `per_change` rule has nothing to read and §F1's Q2 clause "a claim whose subject
    is something they hold" stays unreachable, which is how the narrative substrate stayed
    empty through four revisions."""
    mrow = matrix_row(kind, fld)
    touched: list = []
    earned = earned if earned is not None else set()

    def apply():
        # ⚠ `W-E`: EVERY EFFECT TAKES THE RESOLUTION, AND UNIFORMLY. `H-114` measured the
        # alternative -- `_eff_kill` took no degree, so the effect that computes the VALUES
        # could not honour the branch `writes_at` had just selected, and a fold at degree
        # `Wounded` DELETED THE PERSON. One signature for all ten rather than an
        # inspect-the-callable dispatch: a fold that passes different arguments to different
        # effects has a second contract nobody declared.
        got = eff(w, a, resolution) if eff is not None else None
        # ⚠ AN EFFECT MAY EARN SOME OF ITS DECLARED KINDS AND NOT OTHERS. A list means *all*
        # of them (the original contract, unchanged); a MAPPING `{kind: [ids]}` names which.
        # Without this the fold emitted EVERY kind in `emits:` the moment anything changed --
        # so `confer` onto an unheld office published `tenure.closed` with nothing closed.
        # That is the fabricated-`person.died` class committed INSIDE the fix for it, and the
        # existing guard cannot see it because it is all-or-nothing per act. Found by the
        # governance-slice adversarial pass.
        if isinstance(got, dict):
            for k, ids in got.items():
                if ids:
                    earned.add(k)
                    touched.extend(ids)
        elif got:
            touched.extend(got)

    w.write(fld, mrow.write_class(Step.RESOLVE), apply,
            record_kind=kind, fieldname=fld, driver="Act")
    return [StateChange(t, "set", "Act", fld) for t in touched]

def resolve(self, acts: list[Act],
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
    # ordering directly (`A37`).
    ordered = sorted(acts, key=lambda a: (stratum_of(a),
                                          H(w.world_seed, w.tick, a.actor, f"order:{a.verb}:{a.id}")))
    TRACE.decision(f"ordering {len(acts)} acts", "S27/S32",
                   chose="five strata, then a content-derived hash key over one global array",
                   alternatives=["completion order", "rank", "per-container sort (voids the fold)"])

    out: list[Event] = []
    pending: dict[str, list[int]] = {}     # S27.3 SUM-THEN-CLAMP-ONCE accumulator
    for a in ordered:
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
                             "attempt.refused", a.actor, [], [a.id], w.tick))
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
        _contests = list(a.contests or ()) or ([_row.contests] if _row and _row.contests else [])
        if _contests:
            if contest_max_depth is None:
                raise Forbidden("a contest was reached with no caller-supplied max_depth",
                                "S39.3", law="S39.3 -- the depth cap has NO DEFAULT; a default is a number somebody made up and it will be cited later as though it were measured")
            # S39.2 line 2: Events, into the same log, WITH causes[] NAMING THE ACTS.
            # ⚠ REV 3. Rev 2 wrote `[a.id] if any(e.id == a.id for e in w.log) else [ROOT]`.
            # `w.log` holds Events and an Act is never appended to it, so the predicate was
            # PERMANENTLY FALSE and every contest was called with [ROOT]. Retraction 4
            # replaced rev 1's fabricated cause with an unreachable branch rather than with
            # the rule. The act id is named directly.
            # ⚠ THE TARGET IS THE SECOND CLAIMANT, AND REV 1 NEVER PASSED IT, SO THE SEAM
            # JORDAN RULED FOR COULD NOT BE REACHED FROM THE FOLD AT ALL. `claimants=[a.actor]`
            # is one-claimant by construction; `combat_seam.resolve` refuses a party of one
            # (correctly -- a fight needs two), so every `kill / wound` driven through
            # `resolve()` raised `Unspecified: personal combat needs two parties; got 1`.
            # The only test of the seam called `contest()` DIRECTLY with two claimants, so
            # nothing observed the gap: the seam worked and the road to it did not.
            # Reproduce the old failure by deleting `_target`:
            #   d.resolve([Act("k","p_low","kill / wound",payload={"subject":"p_mid"})], 2)
            _target = (a.payload or {}).get("subject") if isinstance(a.payload, dict) else None
            _parties = [a.actor] + ([_target] if _target and _target != a.actor else [])
            r = contest(w, rung=(a.payload if isinstance(a.payload, str) else None) or "R",
                        prize=_contests[0],
                        claimants=_parties, depth=0, max_depth=contest_max_depth,
                        causes=[a.id])
            if isinstance(r, ContestError):
                TRACE.note(f"contest returned {r}", "S39.3")
                continue
            if not isinstance(r, dict):
                out.extend(r)
                continue
            # ⚠ THE SEAM RETURNS A SUBSYSTEM RESULT, NOT EVENTS, AND REV 1 EXTENDED THE
            # EVENT LIST WITH ITS KEYS. `out.extend(r)` over a dict yields the STRINGS
            # 'status', 'module', 'winner', ... so `resolve()` handed nine strings back to
            # `season()` as if they were Events. Invisible until now only because the road
            # to the seam was closed (the one-claimant bug above): the first act to reach
            # the seam is the first act to hit this.
            #
            # ⚠ `W-E`, 2026-09-04 -- THIS BRANCH USED TO `continue`, AND THAT WAS THE FIRST
            # OF THE THREE BROKEN LINKS. What stood here recorded THAT a contest ran, as a
            # `contest.resolved` Event with `changes=[]`, and threw the outcome away: a lost
            # fight and a won one produced the same Event, `Event.degree` was never assigned
            # by anything, and `emits_at` had no caller anywhere in the tracer (`H-113`).
            #
            # ⚠ AND WHAT IT REFUSED TO DO IS STILL REFUSED. The old comment's argument was
            # *"the subsystem returns a WINNER and a winner is not a degree; mapping one onto
            # the other is the second resolver S27.2 forbids"*. That argument is CORRECT and
            # is honoured: nothing here maps a winner. `degree_of` reads the band off the
            # SCENE -- the engine's own `WoundTracker`, on the Combatants the seam still
            # holds -- which is Jordan's 2026-09-03 ruling, *"kill/wound degrees should be
            # directly taken from scene combat"*, and 2026-09-04, *"the combat engine
            # determines the result there. your code just has to accept the result."*
            # `winner` is not read by anything below.
            #
            # ⚠ AND THE BAND IS READ OFF THE ACT'S **SUBJECT**, NOT OFF THE LOSER.
            # `kill / wound` writes on `payload["subject"]`, so reading the loser would kill
            # the target whenever the ACTOR was the one felled. `verb_table.yaml`'s
            # `writes_source:` cell said `wound_state[loser]` and is corrected there.
            #
            # ⚠ `contest.resolved` IS GONE AND ITS REMOVAL IS A CLOSURE, NOT A LOSS. It was
            # one of the three BODY LITERALS `README.md` records invariant 7 as refusing (a
            # kind emitted by the fold that no `emits:` column declares). The outcome is now
            # reported by the verb's OWN degree-keyed `emits:` -- `person.died` /
            # `body.changed` / `contest.undecided` -- which is where invariant 7 says a kind
            # is declared. Two body literals remain (`act.ineligible`, `act.refused`) and
            # they are not this item's.
            produced = self._fold(w, a, Resolution(degree_of(r, _target), r))
            TRACE.decision(
                f"contest for {_contests[0]!r} resolved", "S39/H-98",
                chose=f"read the degree off the scene and fold at it "
                      f"({produced[0].degree if produced else '?'})",
                alternatives=["map winner -> person.died (S27.2: the second resolver)",
                              "record that it ran and write nothing (the pre-`W-E` behaviour: "
                              "a lost fight wrote exactly what a won one did)"])
        else:
            # S27.1: CONTENTION IS AN ORDERED FOLD. Each act sees the world its predecessors
            # left. SEQUENCE, NOT SIMULTANEITY -- and NO ACT NEEDS TO KNOW ANOTHER EXISTED.
            produced = self._fold(w, a)
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
        for ch in (c for e in produced for c in e.changes):
            if ch.field and isinstance(ch.delta, int):
                pending.setdefault(f"{ch.subject}|{ch.field}", []).append(ch.delta)
        out.extend(produced)

    # S27.3 / S32 rest 4: SUM ALL DELTAS, CLAMP ONCE. Clamping may not depend on arrival
    # order. Integer addition is associative and commutative, so this is order-independent
    # AS A FACT, not as a claim (S32/S48).
    scale = w.fixtures.get("condition_scale")
    for key, deltas in pending.items():
        sid, fname = key.split("|", 1)
        if sid in w.sites and fname == "condition":
            site = w.sites[sid]
            total = sum(deltas)
            w.write("condition", WriteClass.ACTS,
                    lambda site=site, total=total: setattr(
                        site, "condition", max(0, min(scale, site.condition + total))),
                    record_kind="Site", fieldname="condition", driver="Act")
            TRACE.decision(f"clamping {sid}.condition", "S27.3",
                           chose=f"sum {deltas} = {total}, then clamp ONCE",
                           alternatives=["clamp per delta (arrival-order dependent)"])
    TRACE.step("RESOLVE", "leave")
    return out


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
