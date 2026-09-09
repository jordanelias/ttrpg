"""`season.decision` -- AX-2's island: what a PERSON forms, wants and can afford, with no
`World` in scope. Layer 10, precedent `epistemic.py`.

EXTRACTED, step 7 of the decomposition (a PURE MOVE but for one call site, named below).
`04_CODE_ARCHITECTURE.md` SA.2 names this module `decision/` and types it: *"owns: nothing.
Returns `Scene[]`. may read: `PersonInterior`, `View`, `Sensation`, `budget`, `Question[]`, the
table's declarations. token: none."* SA.3 row 2 is why the split is BY MODULE and not by first
parameter: *"in one class, a person-side function calls a resolver-side one with no import to
scan."* SE.1 is sharper still: *"`decision/` is a directory from its first commit. The isolation
scan matches by path, so a `choose` drafted inside `loop/` and moved later would have been green
while violating AX-2."* (`04_CODE_ARCHITECTURE.md:1046`) -- which is exactly why this file exists
as a flat module rather than as a claim, and why this step adds an AST test rather than trusting
this docstring.

WHAT MOVED HERE, all as a pure line-slice of `shape.py` at HEAD `d4858c27`:
  * `Query.budget`, `Query.opening_set`, `Query.assemble`, `Query.entrenchment` -- the four
    PERSON-SIDE statics, now MODULE FUNCTIONS. Their eleven WORLD-side siblings did not move with
    them: they were already bindings to `season.queries.world_q` (step 5), and every call site
    renames to `world_q.<name>` directly (see `shape.py`'s breadcrumb). `class Query` itself is
    DELETED -- it survived as a call-site facade for exactly one step. ⚠ THE FIRST DRAFT OF THIS
    SENTENCE ATTRIBUTED A QUOTATION TO `04_CODE_ARCHITECTURE.md` §A.3 ROW 2 THAT IS NOT IN THAT
    DOCUMENT, OR ANYWHERE UNDER `architecture/`. The words quoted ("the class survives one more
    step only as the call-site facade; it goes at step 7") were `shape.py`'s OWN step-5 breadcrumb
    -- this repository quoting itself and crediting the spec. §A.3 row 2 actually reads: *"one
    `Query` class holding both families | two modules; the second cannot import the first | T-f.
    In one class, a person-side function calls a resolver-side one with no import to scan."* That
    row licenses the SPLIT and says nothing about a facade or a step number. Falsifier:
    `rg -n "call-site facade" architecture/` returns nothing.
  * Seventeen top-level names: `align`, `stance_toward`, `urgency`, `make_chooser`,
    `person_side_eligible`, `containing_rung_of`, `store_kind_of`, `_derive_operand`,
    `_REFERENT_OPERANDS` (with its preceding comment block), `operands_for`, `agreement`,
    `standing_of`, `_payload_of`, `pack_scenes`, `aggregate_questions`, `view_ids`,
    `body_band_penalty`.

WHAT DID NOT MOVE HERE, against an earlier plan's placement: `sense()` stays in `shape.py` today
and moves to `loop/driver.py` at step 9, not here -- `04_CODE_ARCHITECTURE.md:116` is explicit
that `sense()` is *"called by the loop, never by the decision"*, and SA.2's `decision/` row lists
four members with no `sense` among them. Filing it here would put a `World`-taking function inside
the one module `AX-2` forbids from naming `World` at all. The alignment table's LOADER
(`_load_alignment`/`ALIGNMENT_SWEEP`/`alignment_at`) also stays out -- it has lived in
`season.data.verbs` since step 3; only the per-call READER (`align`, below) is decision-side.

THE ONE DECLARED EDIT INSIDE A MOVED BODY: `make_chooser`'s inner `choose()` called
`Query.opening_set(...)` because `opening_set` was, at the time, a sibling staticmethod on the same
class. It moves to this module in the SAME step as `opening_set` itself, so the bare name
`opening_set(...)` resolves in this module's own globals -- the only line in this file that is not
a byte-identical slice of `shape.py`.

THE REBIND HAZARD THIS STEP CLOSES. `shape.py`'s own breadcrumb (written at step 6, forward-looking)
warned that `ALIGNMENT`, `belief_contradicts` and `pack_scenes` are each rebound by the test suite
(and, for the latter two, by frozen `proposals/2026-09-04-degree-sweep/` snapshots) by assigning
`S.<name> = ...` -- a rebind that works only because the READER (`align`, `opening_set`,
`make_chooser`) resolves the name in the SAME module's globals at call time. Moving all three
readers here, in the same commit as the corresponding test/arm re-points (`decision.ALIGNMENT`,
`decision.belief_contradicts`, one alias in `sweep_core.py` for `pack_scenes`), is what keeps every
rebind live rather than turning it into a silent no-op on the facade's stale copy.

⚠ "EVERY" IS EXACT, AND THE FIRST DRAFT OF THIS COMMIT MADE IT FALSE WHILE ASSERTING IT. Two more
files rebind these names -- `arm7_flexibility.py` (`pack_scenes`, 6 sites) and `wd_acceptance.py`
(`belief_contradicts`, 5) -- and the plan, the step brief and the commit message all said "nothing
imports either, so they cannot fail the suite". That premise is false on disk: `sweep.py:19`
imports and runs `arm7_flexibility`, and six files import `wd_acceptance`. Both are re-pointed
here. An unrepointed arm does not fail; it reports every branch identical, which is a fabricated
null and worse than a failure (§0.1 pt 4).

AX-2, ENFORCED HERE FOR REAL: this module may not import `state.world`, `queries.*`, `loop.*`,
`seam`, `combat_seam` or `shape`, and may not name `World` anywhere -- not as an import, not as a
bare name, not as a string constant. `test_decision_module_never_names_world` (added this step,
`engine/season/tests/test_season_shape.py`) is an AST pass that checks exactly that, because
`04_CODE_ARCHITECTURE.md:1046`'s "isolation scan matches by path" describes a scan that, before
this test, did not exist for this module -- a directory boundary is a promise; this is the check.

Imported at the top of `shape.py` (`from . import decision` + a re-export block) so every bare use
of a moved name further down that file keeps resolving, and so `S.<name>` keeps resolving for the
harness and tests: a re-export, not a second definition.
"""

from __future__ import annotations

from typing import Any, Callable, Optional

from .data.rosters import (
    CONVICTION_AXES, PERSON_PREDICATES, QUESTION_AGGREGATION, SCENE_PACKING_RULES,
    VIEW_BUILDER_RULES,
)
from .data.verbs import ALIGNMENT, ALIGNMENT_DEFAULT_CELL, ELIGIBILITY_KINDS, VERB_TABLE
from .epistemic import belief_contradicts
from .gaps import Forbidden, InstrumentDefect, Unspecified
from .state.carriers import Act, Candidate, Claim, Person, Question, Scene, Sensation, View
from .trace_log import TRACE

# ⚠ TWO DEVIATIONS FROM THE DECOMPOSITION PLAN'S DECLARED IMPORT LIST, BOTH FOUND BY THE AST
# VERIFICATION THE PLAN ITSELF DEMANDED, NEITHER A JUDGMENT CALL:
#
# 1. `ELIGIBILITY_KINDS` IS IN `.data.verbs`, NOT `.data.rosters` -- the plan named the wrong
#    owner. `person_side_eligible()` reads it (`if kind not in ELIGIBILITY_KINDS`), and importing
#    it from `.data.rosters` as written raises `ImportError` at module load, immediately, for
#    every caller -- the loud failure mode, not the step-5 kind that hides until a byte-compare.
#    Verified against the actual definition site, which is `engine/season/data/verbs.py`'s
#    `ELIGIBILITY_KINDS = roster("eligibility_kinds")` -- located by `rg -n "^ELIGIBILITY_KINDS"`
#    and deliberately cited WITHOUT a line number, because the first draft of this comment said
#    `:55` and the assignment is at `:68`, in a file this same commit edits (CLAUDE.md §3: "a LINE
#    citation into a file being decomposed is wrong twice over"). It is *sourced* from the rosters file's
#    `eligibility_kinds` table but the module-level NAME lives in `verbs`, because `verbs.py` is
#    what checks a verb row's `eligible:` cell against it.
#
# 2. `Claim` IS ADDED to `.state.carriers`, absent from the plan's list. `agreement()`'s signature
#    reads `list[Claim]` twice, bare (not a forward-ref string) -- the same AST pass that confirmed
#    every other name below is needed found this one unimported. This is the step-5 `Forbidden`
#    lesson again: an annotation-only reference is still a reference, and `from __future__ import
#    annotations` makes a missing one a silent hole rather than an `ImportError`, since nothing in
#    this tree currently calls `typing.get_type_hints` on a season module. Fixed anyway rather than
#    left as a known dangling annotation.
#
# `Fixtures` and `VerbRow` are the converse case and are DELIBERATELY absent (the plan is right to
# omit them): every occurrence of either in the moved bodies is a QUOTED forward-reference string
# (`"Fixtures"`, `"VerbRow"`), never a bare name, never constructed, never the subject of
# `isinstance`. That is the same quoting the moved bodies used even inside `shape.py`, where both
# names WERE already resolvable -- so the quoting was never about deferred resolution, it is how
# this file's original author marked "an opaque handle whose class identity this function does not
# need". Importing them here would add two names AST proves are dead weight.


def budget(p: Person, v: View, k: int, fx: "Fixtures") -> int:
    """S26 / `H-28`: `budget : (Person, View) -> int`, PERSON-SIDE, NO WORLD. Returns SCENE
    ACTIONS, per Jordan's 2026-09-02 ruling.

    ⚠ REV 4 IS THE FIRST VERSION THAT READS ITS OWN ARGUMENTS. Rev 3's docstring disclosed,
    honestly, that it "RETURNS THE INJECTED FIXTURE AND IGNORES `p` AND `v`" -- functionally
    the FIELD S26.3 forbids. The reason it gave was a collision it called unresolved: S26
    types it with no `World`, S26.3 says it varies by office, condition and distance, and all
    three looked resolver-side.

    **They were never resolver-side; the STORE was in the wrong place.** #353 `:730` gives
    Person "every Tenure whose subject they are", so office-holding is the person's own state;
    `(Person, body)` and `(Person, travel_leg)` are Part D rows on Person. W5 moved the tenure
    store onto its subject (see `_TenureView`) and added the two fields, and the collision
    dissolved with no signature change. That is PLAN §3.3's SMALLER AMENDMENT, and taking it
    is what lets `:634`'s "the ONE non-decision function permitted a `World`" stay true --
    V2 §F3 took the larger one and made `budget` a second such function.

        budget = base + office_bonus x (own live `hold` Tenures)
                      - condition_penalty(own body band)
                      - distance_penalty(own travel legs)

    `condition_penalty` COUNTS BANDS on the `band_floors["body"]` table the site gate already
    uses -- `H-38` closed with "`Site.condition` is the model", so this spends that closure
    rather than inventing a second band scheme. Floor of 1: a wounded duke gets fewer scenes,
    and a dying one still gets one, because a budget of 0 would delete the person from the
    season silently rather than narrowing them (S26.3's triage is the point).

    `k` remains the injected base so the sweep site is unchanged. The two modifier magnitudes
    are fixtures (`H-70`); the DIRECTIONS are #353 `:912-913` and are not open.

    ⚠ `fx` IS NOT A WORLD, and the distinction is the one L2 actually draws. A `World` is other
    people's state -- persons, rungs, sites, the tenure store -- and reading it person-side is
    what L2 forbids. `Fixtures` is the PARAMS REGISTRY: flat numbers, no entity, identical for
    every person in the season, and #353 §22 assigns them to `params` precisely so they are
    not world state. `k` was already one of them, handed in by the driver; `fx` generalises
    that rather than widening it. The AST proof below tests for a `World` ANNOTATION, so it
    would catch a real regression here and correctly passes this."""
    TRACE.query("budget", "person")
    offices = sum(1 for t in p.tenures if t.kind == "hold" and t.live)
    b = k + offices * fx.get("budget_office_bonus")
    b -= body_band_penalty(p, fx)
    b -= len(p.travel_leg) * fx.get("budget_leg_penalty")
    return max(1, b)


def opening_set(p: Person, v: View, q: Question, fx: "Fixtures") -> list[Candidate]:
    """§F1 -- COMPUTED FROM THE VERB TABLE. No `roster` parameter: that is `D2` entire.

    ⚠ WHAT CHANGED, AND WHY IT COULD NOT CHANGE BEFORE. Rev 2 took `roster: list[Candidate]`
    and returned it, and said so: "the PROPERTY S17 chose the type to protect -- an option set
    that is COMPUTED rather than an AUTHORED LIST -- is not [faithful], because `roster` is the
    caller's authored list." Its reason was real: §61 gave `q` no producer, so there was
    nothing to compute a set FROM. `questions_for()` is that producer, so the roster's excuse
    is gone and with it the roster.

        { Candidate(verb, subject, why, operands) :
            verb    in the verb table                            -- clause 1
          , eligibility(verb, p) holds                           -- clause 2
          , subject in referents(q)                              -- clause 3
          , requires(verb) not KNOWN-FALSE from p's OWN claims    -- clause 4
          , every operand requires(verb) names is DERIVABLE }     -- `W-C`, `H-94`

    ⚠ THE FIFTH LINE IS NOT A FIFTH CLAUSE OF §F1 AND MUST NOT BE READ AS ONE. Clauses 1-4
    are the design's; this is the instrument declining to MINT AN ACT WITH A HOLE. The
    difference matters because the two have opposite polarities: a clause of §F1 narrows what
    a person is willing to attempt, and this narrows what the person can COHERENTLY SAY. An
    act missing an operand is refused by the fold for the instrument's reason, and `W-B` will
    deposit that refusal as a belief -- so forming it would put a fabricated fact about a
    granary nobody named into every witness's ledger. `operands_for` traces every decline, so
    the count is measurable rather than inferred from a verb's absence.

    ⚠ `fx` IS THE FOURTH PARAMETER AND IT IS `budget`'s PRECEDENT, NOT A WIDENING. §F1 types
    this `opening_set(p, view, q)`. `Fixtures` is the PARAMS REGISTRY -- flat numbers, no
    entity, identical for every person in the season, assigned to `params` by #353 §22 -- and
    `Query.budget` already takes one for exactly this reason, with the argument written out
    there. Two of `transfer`'s operands (`kind`, `amount`) are values the design supplies NO
    number for, so they are fixtures with a register row and a sweep (`H-94`), and a person
    who cannot reach the registry cannot derive them. The alternative was to leave them in the
    verb table's `operand_defaults`, where the FOLD filled them under the person -- which is
    the two-owner defect this item deletes. What §F1's signature is protecting is that no
    AUTHORED OPTION LIST reaches here (`D2`); a params registry is not one, and the AST proof
    still sees no `World`.

    ⚠ CLAUSE 4 IS THE EPISTEMIC DESIGN AND IS NOT "requires holds". §F1: the person filters on
    WHAT THEY BELIEVE, "so a person who *wrongly* believes the granary full still forms the
    Candidate, acts, and gets `transfer.refused` from the fold. That is T3 and L2 working; a
    filter on world truth would be `choose` reading the world." Jordan, 2026-09-02: *"our
    understanding of all other words and actions is subjective and singular."* So the test is
    KNOWN-FALSE — a claim the person holds that contradicts the requirement — and NOT
    "unproven". Absence of a belief is not a belief in the negative.

    ⚠ ONE OF §F1'S FOUR ELIGIBILITY KINDS CANNOT BE EVALUATED HERE, and it declines rather
    than admitting. See `person_side_eligible`: `remit:` needs the OFFICE's remit, and #353
    §11.1 is explicit that "who holds an office is NOT a field on the office -- it is a `hold`
    Tenure, owned by the holder", which gives the person the TENURE and leaves the REMIT with
    the office. That is a genuine collision in §F1 and it is registered (`H-71`), not filled.
    It is not the `budget` case: there the data was the person's and merely stored in the
    wrong place, and no such relocation is available for a remit two holders share."""
    TRACE.query("opening_set", "person")
    out: list[Candidate] = []
    for verb, row in sorted(VERB_TABLE.items()):
        if not person_side_eligible(p, row):
            continue
        for subject in q.referents:
            # ⚠ OPERANDS BEFORE THE BELIEF TEST, AND THE ORDER IS THE POINT. Clause 4 asks
            # whether the requirement is known-false ABOUT THIS BINDING, so the binding has to
            # exist first -- asking it of an unbound cell is what made the person read a
            # different granary from the fold.
            ops = operands_for(p, row, q, subject, fx)
            if ops is None:
                continue
            if belief_contradicts(p, row, subject, ops):
                continue
            out.append(Candidate(verb, subject, why=q.source, operands=ops))
    return out


def assemble(p: Person, question: Any, k: int, rule: str = "recent") -> View:
    # ⚠ W5 REMOVED A `NoProducer` HERE, AND THE REMOVAL IS THE DISCHARGE OF §61, NOT A
    # SOFTENING OF IT. It read: "`assemble(person, question)` and `view(person, question)`
    # are UNSATISFIABLE; DELIBERATE HAS NO DECLARED ENTRY POINT." That was TRUE while nothing
    # produced `q`. `questions_for()` produces it from four sources, so `question is None` no
    # longer means "the design has no producer" -- it means THIS PERSON HAS NO QUESTION THIS
    # SEASON, which is an ordinary state (a quiet season, nothing due, no standing commit) and
    # not a hole. Such a person forms no candidates and does nothing, which is correct.
    # A WRONG TYPE STILL RAISES, below: silently accepting one would let a caller's leftover
    # string sit where a Question belongs and read as "no question", which is how a discharged
    # hole comes back as a silent no-op.
    if question is not None and not isinstance(question, Question):
        # `InstrumentDefect`, not `Forbidden`: a caller passing the wrong TYPE is a bug in the
        # caller, not a hole in #353, and filing it as a GAP would put it in the column that
        # measures the design. Same lesson as `_TenureView`.
        raise InstrumentDefect(
            f"assemble() was given a {type(question).__name__}, not a Question. Pass a "
            "Question from questions_for(), or None for a person with no question this "
            "season. §F1's `q` has a producer now (`H-04`); accepting any object here would "
            "make a stale injected fixture indistinguishable from an absent question.")
    return View(p.id, view_ids(p, question, k, rule), k, question)


def entrenchment(p: Person, seasons_held: int, scale: int, span: int) -> int:
    TRACE.query("entrenchment", "person")
    return min(scale, (seasons_held * scale) // span)


def align(verb: str, axis: str) -> float:
    """§F2's `alignment(c.verb, axis)`. Sparse: an unlisted pair reads the table's own declared
    `default_cell`, never a literal here."""
    return float(ALIGNMENT.get(axis, {}).get(verb, ALIGNMENT_DEFAULT_CELL))


def stance_toward(p: Person, referent: str) -> float:
    """§F2's second term, from `p`'s OWN stance rows. #353 `:333`: `(referent, valence -5..+5,
    weight 0..5)`. Valence times weight, summed over the rows naming this referent -- weight is
    what `:333` supplies it for, and dropping it would make a 5-weight conviction and a 0-weight
    one count alike."""
    total = 0.0
    for row in p.stance:
        if len(row) >= 3 and row[0] == referent:
            total += float(row[1]) * float(row[2])
    return total


def urgency(subsistence: int, fx: "Fixtures") -> float:
    """§F2's third term. NO IN-CHAIN FORMULA -- `H-73`, `assumption`, swept.

    ⚠ AND IT CANNOT CHANGE ANY DECISION, WHICH IS A DEFECT IN §F2 RATHER THAN IN THIS FUNCTION.
    §F2's score is

        score(c) = SIGMA_axis conviction[axis] * alignment(c.verb, axis)
                 + stance_toward(c.subject)
                 + urgency(sensation.subsistence)

    and the third term HAS NO `c` IN IT. It is added identically to every candidate, so it cannot
    move the ranking, cannot change which candidates survive `ask_budget()`, and cannot change the
    order they are returned in. `choose` returns "the top ask_budget() candidates, ORDERED by
    score", so a term constant across candidates is INERT BY CONSTRUCTION -- it is the dead-carrier
    shape #353 `:739-744` names, arriving in the scoring function instead of in a field.

    Kept and computed anyway, faithfully, because deleting it would hide the finding: the sweep
    (`H-73`) reports that NO verdict moves across three urgency scales, and that null result IS
    the measurement. `test_w5_f2_third_term_is_inert` is the falsifier."""
    return float(subsistence) / float(fx.get("condition_scale"))


def make_chooser(fx: "Fixtures", mint: Callable[[str, str, str], str],
                 verbs: Optional[frozenset] = None) -> Callable[..., list[Act]]:
    """§F2's decision policy as a FACTORY, so `choose(p, view, sensation, ask_budget)` keeps the
    FOUR-parameter signature §26 states while still reaching its params.

    `H-03` is the row: "grade: assumption. THE SHAPE IS RULED (§3 L1, §9, §26); only the weighting
    is open", so §G's discipline applies to the weights and not to this structure.

    Four properties, and each is checked by a test rather than asserted here:
      1. EVERY INPUT IS PERSON-SIDE -- `convictions`, `stance`, the View, the two Sensation
         scalars. No World, no resolver-side Query. L2 by parameter list.
      2. It CONSUMES `convictions` and `stance`, which #353 declares as fields and no formula in
         the chain reads -- a carrier nothing consumes is dead state (§22.1's own complaint).
      3. THE PERSON TRIAGES. `ask_budget()` is asked, not imposed; the engine never truncates.
      4. A lookup on one's own interior is indistinguishable from a deliberation at this
         boundary, and the design does not claim otherwise (§F2 property 4).

    ⚠ `mint` IS HERE BECAUSE §F2 TYPES `choose -> Act[]` AND GIVES THE PERSON NO WAY TO MINT ONE.
    An `Act` needs an id, and §33 derives every id from the world seed and the tick -- "unique per
    DRAW, not per operation" -- so a person-side function cannot produce one. That is a real gap
    between §F1's `-> Candidate[]` and §F2's `-> Act[]` and it is registered (`H-74`), not filled:
    the barrier passes a minter closed over the seed and tick, which are the CLOCK, not anybody's
    interior. Same shape as `fx`, and the AST proof still sees no `World`."""
    def choose(p: Person, v: View, s: Sensation, ask_budget) -> list[Act]:
        q = getattr(v, "question", None)
        if q is None:
            return []
        cands = opening_set(p, v, q, fx)
        if verbs is not None:
            cands = [c for c in cands if c.verb in verbs]
        u = urgency(s.subsistence, fx)
        def score(c: Candidate) -> float:
            return (sum(float(p.convictions.get(ax, 0.0)) * align(c.verb, ax)
                        for ax in CONVICTION_AXES)
                    + stance_toward(p, c.subject or "")
                    + u)
        # Deterministic: score DESC, then verb then subject, so a tie cannot depend on dict order.
        ranked = sorted(cands, key=lambda c: (-score(c), c.verb, c.subject or ""))
        # §26.3: the PERSON triages. The slice is the person's own choice of what to leave
        # undone, taken against a budget they ASKED for -- not an engine truncating a tail.
        # `W17`: the budgeted unit is the SCENE, so the slice is over scenes and each carries up
        # to `interactions_per_scene` of the ranked candidates. The default policy fills scenes
        # greedily in score order -- a person spends a scene on their best option and whatever
        # else it can carry, which is what "1-3 mechanical interactions" describes.
        return pack_scenes(p, ranked, ask_budget(), fx, mint, occasion=q)
    return choose


def person_side_eligible(p: Person, row: "VerbRow") -> bool:
    """§F1 clause 2, PERSON-SIDE. `own | remit | hold | presence`, NEVER `capability`.

    A DISJUNCTION: `transfer` is eligible by `own` OR `hold:<store>`, so one alternative admitting
    is enough and one alternative declining decides nothing.

    ⚠ TWO OF THE FOUR KINDS DECLINE HERE, EACH NAMING ITS HOLE, and neither admits on an
    unevaluable predicate -- that would be a silent fill off the register (`G1`) at the opposite
    polarity to §42.2, which sends zero evidence to the verdict AGAINST the thing measured. The
    resolver's `_eligible` still evaluates both, because it HAS a `World`; this is the person's
    reading, and the gap between the two readings is the finding.

      * `remit:<act>` -- `H-71`, NEW. Needs the OFFICE's `remit_acts`. #353 §11.1: "who holds an
        office is NOT a field on the office -- it is a `hold` Tenure, owned by the holder", so
        the person owns the tenure and the office owns the remit. Unlike `budget`'s collision
        there is no relocation available: two holders of one office share one remit, so it is not
        the person's state to move. §F1 asserts this clause is person-side and does not say how.
      * `presence:<rung>` -- declined because the ARGUMENT IS A PLACEHOLDER naming a kind of
        rung rather than an id, which is `H-75`, and is the same reasoning the `hold:<store>`
        branch already carries one block below. ⚠ CORRECTED BY `W6`'s adversarial pass: this said
        *"`H-33`, the presence index, which does not exist"*, and `W6` BUILT it -- `_ch_co_located`
        reads it and `H-33` now carries a `site:`. The citation survived the thing it cited. The
        refusal itself is unchanged and correct; only its reason was stale."""
    for alt in row.eligibility:
        kind, _, raw = alt.partition(":")
        kind, raw = kind.strip(), raw.strip()
        # A `<...>` argument is a PLACEHOLDER naming a KIND of object (`hold:<store>`), not an id.
        # Keeping the distinction is what lets the `hold` branch below refuse to guess.
        placeholder = raw.startswith("<") and raw.endswith(">")
        arg = raw.strip("<>")
        if kind not in ELIGIBILITY_KINDS:
            raise Forbidden(
                f"eligibility kind {kind!r} is not in the eligibility_kinds roster", "§E4",
                needs="one of the four; `capability` GATES NOTHING (#353 §9.2)",
                law="#353 §9.2 -- 'capability supplies dice and GATES NOTHING'. A fifth kind is a "
                    "new way to make a verb unavailable and needs a ruling, not a table edit")
        if kind == "own":
            return True
        if kind == "hold":
            # ⚠ THE ARGUMENT IS COMPARED. It was parsed and thrown away, so `transfer`'s
            # `hold:<store>` and `destroy_record`'s `hold:<record>` admitted anyone holding ANY
            # office -- an OVER-admission, which `G4` makes a defect of equal weight to an
            # over-refusal. `<store>`/`<record>` are PLACEHOLDERS naming a kind of object, not
            # ids, so a placeholder cannot be matched against a Tenure's `object` and this
            # DECLINES rather than guessing which store the act meant: that binding is `H-75`.
            if not raw:                       # bare `hold` -- holding anything admits
                if any(t.kind == "hold" and t.live for t in p.tenures):
                    return True
            elif not placeholder:             # a literal object id
                if any(t.kind == "hold" and t.live and t.object == arg for t in p.tenures):
                    return True
            else:
                TRACE.note(f"`hold:<{arg}>` names an object KIND, not an id (H-75); "
                           f"{row.verb!r} declines rather than admitting on any held object")
        # `remit` and `presence` decline: see the docstring. TRACE records the decline so the
        # count is measurable rather than inferred from a verb's absence.
        elif kind == "remit":
            TRACE.note(f"`remit:{arg}` is unevaluable person-side (H-71, the office's remit is "
                       f"not the holder's state); {row.verb!r} declines rather than admitting")
        elif kind == "presence":
            TRACE.note(f"`presence:` eligibility is unevaluable person-side (H-33, the presence "
                       f"index); {row.verb!r} declines rather than admitting")
    return False


def containing_rung_of(p: Person) -> Optional[str]:
    """WHERE THE ACTOR IS, READ OFF THE ACTOR: the object of their own live `contain` Tenure.

    A person's live `contain` Tenure. `W5` moved the tenure store onto the Person precisely so a
    person-side function could ask this without a World, and this is that move being spent rather
    than restated: #353 `:730` gives a Person "every Tenure whose subject they are", and where you
    are is one of them.

    ⚠ IT IS NOT A CHOICE, AND THAT IS WHY IT IS DERIVED RATHER THAN OFFERED. `H-94` asked where
    `transfer`'s operands come from and the answer differs per operand: where the actor is, is
    STATE (the actor is somewhere, and it is wherever they are), the receiver is the question's
    referent, and `kind`/`amount` are values the design does not supply at all. Only the third
    kind needs a fixture. Reading the first as a choice would invent an option the person does not
    have; reading it as a fixture would invent a place.

    ⚠ IT WAS CALLED `hearth_of` AND THE NAME ASSERTED SOMETHING THE CODE DOES NOT DO. RENAMED BY
    THE `W-C` ADVERSARIAL PASS, WHICH IS ALSO WHERE THE ASSUMPTION IS DECLARED. §54 item 7 writes
    `stores(hearth(giver), kind) >= amount` and supplies THE TOKEN AND NO DEFINITION
    (`ARCHITECTURE.md:1898`, `ARCHITECTURE_V2.md:418`) -- while `hearth` is SEPARATELY a member of
    `rosters.yaml: rung_kinds` (`person, hearth, community, settlement, territory, province,
    duchy, realm`; `ARCHITECTURE.md:376`). So the term has a second, narrower reading the document
    neither states nor excludes, and a function named for it was claiming the document had chosen.

      READING A (this one, SHIPPED): the actor's containing rung, WHATEVER ITS KIND.
      READING B (the alternative, NAMED so the choice is visible): walk up the containment ladder
        to the nearest rung whose `kind` is `hearth`.

    ⚠ MEASURED 2026-09-04, BOTH READINGS, OVER ALL 89 RUNNABLE CORPUS WORLDS, because a declared
    alternative nobody runs is the laundering §0.1 point 4 names. Reading B was built and folded.
      * CENSUS of what reading A returns, over all 267 corpus seatings (89 worlds x 3 persons):
        `hearth` 111 · `realm` 153 · `settlement` 3. So in 156 of 267 the shipped reading returns
        a rung that is NOT of kind `hearth` -- a majority, and the divergence is real, not
        theoretical.
      * `transfer` EXECUTED 702 -> 237, REFUSED 21 -> 0, and 0 -> 486 Candidates decline for want
        of `from`. The executed SET does not move (`transfer` still executes, in the 37
        person-scale worlds, which are the ones whose ladder HAS a hearth rung).
      * MOST OF THE DIVERGENCE IS THE WORLD BUILDER'S. `corpus_run.build_at` truncates the ladder
        at the case's own `scale:`, so a realm-scale case has no hearth rung to walk up to and
        seats its people directly in the realm; under a full ladder those 153 seatings would be
        hearths and the two readings would agree on them.
      * ⚠ BUT NOT ALL OF IT, AND THE REMAINDER IS NOT A DEFECT. A person may legitimately sit
        ABOVE a hearth in a hand-built world -- `tiny_world` seats the Duke in the settlement and
        the King in the realm, deliberately -- and there the two readings still differ. So this is
        not "a fixture bug that would vanish", and the closure below does not rest on pretending
        it is.

    ⚠ AND READING B IS REFUSED ON ARCHITECTURE (§0 test 5), NOT ON THE NUMBER. It is not
    person-side: `Rung.kind` and `Query.parent_of` are WORLD reads, and this function is exactly
    the site §F1's L2 keeps World-free -- a person knows WHICH rung contains them, because that
    Tenure is their own, and does not know WHAT KIND of rung it is, because kinds are the world's.
    Giving it a `World` turns
    `test_w5_sense_is_still_the_only_world_taking_non_decision_function` red, which is the
    falsifier for this paragraph rather than a claim about it. The remaining alternative -- let
    the FOLD compute `hearth(giver)`, which does have a World -- gives one operand two owners
    again, which is the divergence `W-C` closed.

    `None` for a person with no live containment -- a person nowhere cannot give from a store, and
    the Candidate is not formed. That is a REFUSAL and not a hole in the design: #353 seats every
    person on the ladder, so a person off it is a WORLD the case failed to build."""
    return next((t.object for t in p.tenures if t.kind == "contain" and t.live), None)


def store_kind_of(p: Person, q: "Question") -> Optional[str]:
    """The matter kind THE QUESTION IS ABOUT, from the person's own ledger. `None` if it says none.

    `q.about` is the originating object's id; for §F1's Q2 (`claim_landed`) that is a Claim in
    THIS person's ledger, and a claim whose predicate is `stores:<kind>` names a kind. The
    predicate is the one the grammar DERIVES (`f"{scalar}:{key}"`, `Observation`'s docstring), so
    this reads the same namespace `belief_contradicts` reads and the write side has a name to aim
    at -- which is `H-116`'s other half and is `W-B`, not this item.

    ⚠ PERSON-SIDE, AND THE LEDGER IS THE REASON IT CAN BE. §20: claims live in the holder's own
    ledger and nobody else may read it. Looking `q.about` up in the WORLD would make this a
    resolver read wearing a person's signature."""
    if q is None or not q.about:
        return None
    for c in p.ledger:
        if c.id != q.about:
            continue
        # `stores` is `transfer`'s own `scalar:`, and `f"{scalar}:{key}"` is how `Observation`
        # derives the predicate -- so this reads the namespace the cell writes rather than a
        # second vocabulary. A claim about anything else names no matter kind.
        stem, sep, arg = str(c.predicate).partition(":")
        return arg if sep and arg and stem == "stores" else None
    return None


def _derive_operand(p: Person, name: str, q: "Question", subject, fx: "Fixtures"):
    """ONE OPERAND, FROM THE PERSON'S OWN STATE. `None` means THIS PERSON CANNOT SUPPLY IT.

    ⚠ THE CHAIN IS NOT THE ROUTER `G2` FORBIDS, on `WorldReader.read`'s own precedent. It
    enumerates the CLOSED OPERAND VOCABULARY -- `rosters.yaml: requires_operands`, eight names,
    where an unrostered one already refuses at load -- and not verbs, entities or outcomes. There
    is no shape to forbid instead: each of the eight is a different question, and a per-verb table
    would be the special case `G2` is actually about.

    THE RULE IT IMPLEMENTS, stated once so the branches are readable as one decision rather than
    eight: AN OPERAND NAMING WHAT THE ACT IS ABOUT BINDS THE QUESTION'S REFERENT; AN OPERAND
    NAMING THE ACTOR'S OWN POSITION BINDS THE ACTOR'S OWN STATE; AN OPERAND THE DESIGN SUPPLIES NO
    VALUE FOR IS A FIXTURE. That is why `subject`, `to` and `site` all bind the referent and are
    not one name -- the cells name them differently because they mean different things TO THE
    VERB, and the person answers all three the same way, with the thing they were asked about.

    ⚠ THE REFERENT IS WORLD-SOURCED, AND THAT IS §F1'S OWN SHAPE RATHER THAN A WIDENING OF IT.
    Raised by the `W-C` adversarial pass and closed here rather than escalated, because it is
    answered: three of the four question sources read the world (`questions_for` Q1 from
    `w.dates`/`w.docket`, Q3 from `w.crossings`/`w.sites`, Q4 from `w.propositions`; only Q2 is
    ledger-sourced), and `W-C` promotes that referent from *which Candidate forms* to *an operand
    of the minted act*. §F1 states the derivation in terms -- `subject ∈ referents(q)`, "what the
    question is ABOUT" -- and puts the epistemic constraint in a DIFFERENT clause: `requires(verb)
    not KNOWN-false FROM p's OWN CLAIMS`, with its own warning that softening THAT clause is the
    breach. So the belief filter is on the requirement, never on the referent; and `to`/`site` are
    the referent under the two other names the closed operand vocabulary has for it, not a second
    channel.
    Two things make the promotion safe rather than merely licensed, and both are properties of
    code above rather than of this paragraph. (a) EVERY SOURCE IS ADDRESSED TO THE PERSON: Q1
    requires the Date's holder to be them or something they hold, Q2 reads their own ledger, Q3
    requires them to be PRESENT where the band crossed, Q4 is their own live `commit`. A person
    cannot be handed a referent they have no reach to. (b) THE REFERENT PROPOSES AND THE FOLD
    DISPOSES: naming a receiver is not moving matter to it. `_eff_transfer` returns nothing when a
    side is no rung and the fold emits `transfer.refused`; `move`'s `contain_path` cell reads
    UNKNOWN off the world and `contain_ascends` blocks a sibling. Measured over the corpus: 21 of
    723 transfers refused, 73 of 723 moves blocked -- so world-sourced ids do not DECIDE where
    matter goes, which was the sharp form of the objection.

    ⚠ AN OPERAND WITH NO BRANCH DECLINES, AND `floor` IS THE LIVE CASE. §12.1's floors are
    per-SITE-KIND (`band_floors`), and person-side there is no way to learn a site's kind without
    `w.sites` -- so a person cannot name the floor, and a cell binding `floor` as an OPERAND would
    form no Candidate and say so in the trace. No live cell does: `work` reads its floor as a
    SECOND READ on the site (`threshold_predicate`), which the world answers. Declining is
    therefore the honest branch AND the one with nothing dead behind it (`ID-13`) -- the
    alternative, `min` over every kind's floors, is a number nobody chose."""
    if name == "actor":
        return p.id
    # What the act is ABOUT -- three cell-side names for the one thing the person was asked about.
    if name == "subject":
        return subject
    if name == "to":
        return subject
    if name == "site":
        return subject
    # Where the ACTOR is. §54 item 7's `hearth(giver)`, READ AS the actor's containing rung of
    # any kind -- a declared assumption with a named alternative and a measurement, not a reading
    # the document supplies. See `containing_rung_of`, and register row `H-94`.
    if name == "from":
        return containing_rung_of(p)
    # Values the design states no number for. `H-94`, declared / defaulted / swept.
    if name == "kind":
        return store_kind_of(p, q) or fx.get("default_store_kind")
    if name == "amount":
        return fx.get("default_transfer_amount")
    return None


# ⚠ TWO NAMES, AND THEY ARE THE SAME FACT. `subject` is *what the act is about* and `to` is *the
# far end it is aimed at*; the person answers both with the referent they were asked about, so
# carrying both is one fact under the two names the closed vocabulary has for it -- not a second
# decision. A Candidate carries them BEYOND the operands its own cell binds, and the reason is in
# Part E's write column rather than in its `requires` column: `transfer` declares
# `writes: [Rung.stores, Rung.stores]` -- TWO rungs -- and its cell names ONE (`from`, the giver's
# hearth). The receiver is declared by the WRITE and asked for by no precondition, so a rule that
# carried only what the precondition binds would mint a transfer that cannot be performed.
# ⚠ `site` IS NOT IN THIS TUPLE AND THE OMISSION IS THE POINT. `subject` and `to` are POSITIONS in
# an act; `site` asserts a TYPE -- *this referent is a Site* -- and only a cell that actually reads
# it may make that assertion on the person's behalf. `existence`'s `needs:` admits `site`, so
# including it here would put a `site` on every `carry`.
# roster-exempt: MECHANISM, and under the guard's own threshold besides. These are two members of
# `rosters.yaml: requires_operands` singled out by the argument above -- the roster is still the
# declaration of WHAT AN OPERAND MAY BE; this names which two the person answers with the referent.
_REFERENT_OPERANDS = ("subject", "to")


def operands_for(p: Person, row: "VerbRow", q: "Question", subject,
                 fx: "Fixtures") -> Optional[dict]:
    """§F1'S MISSING CHANNEL: the operands a Candidate carries, DERIVED PERSON-SIDE. `None` means
    THIS PERSON CANNOT FORM THIS CANDIDATE.

    ⚠ THE RETURN OF `None` IS THE LOAD-BEARING HALF, NOT THE DICT. Never mint an act with a hole.
    An act missing an operand is refused by the fold for a reason that is about the INSTRUMENT
    rather than about the world, and once `W-B` attaches a Verdict's reads to its Event that
    refusal is deposited at WITNESS and becomes a belief every witness holds -- a FALSE one, about
    a granary that was never asked about. Refusing to form the Candidate keeps the instrument's
    own gap out of everybody's ledger, and `TRACE.note` makes it countable instead.

    ⚠ WHAT IS CARRIED: THE CELL'S OWN OPERANDS, PLUS `subject`/`to` WHERE THE FORM ADMITS THEM.
    The rule the item states is *a form whose `needs` cannot be bound forms no Candidate*, and
    `needs:` is read here as the CEILING on what may be carried rather than the FLOOR of what must
    bind. Both halves of that are load-bearing and neither is a softening:
      * as a FLOOR it declines on operands nobody asks about. `scalar_threshold`'s `needs:`
        includes `floor`, which no live cell binds as an operand (`work` reads its floor as a
        SECOND READ on the site, which the world answers) and which a person cannot derive at all
        -- §12.1's floors are per SITE KIND and a kind is a world read. So the floor reading
        refuses `transfer` and `work` for want of a value neither of them reads, which is a
        refusal for a reason that is not there.
      * as a CEILING it is exactly what keeps the two vocabularies apart. `existence`'s `needs:`
        admits `site` and `from`; carrying them would put a `site` on every `carry`, for no
        reader. And an UNTYPED verb carries NOTHING, which is what stops `kind` -- a MATTER kind
        here and a RECORD kind in `_eff_create_record` -- from arriving on a `create_record` and
        silently making every record a record of grain.

    ⚠ AN UNTYPED VERB IS NOT DECLINED. `{}` is the right answer for `speak`, `utter` and
    `create_record`: the grammar states no precondition for them, so there is nothing to bind, and
    refusing them would be reading "no cell" as "an unmet cell" -- the UNKNOWN/False collapse the
    whole of this block exists to refuse. Their effects want operands of their own (`stages` is
    `H-80`, `harm` is `W-E`); those are not in `requires_operands` and are not this item.

    ⚠ NO WORLD, AND THE GUARD ACTUALLY REACHES IT. The AST proof in
    `test_w5_sense_is_still_the_only_world_taking_non_decision_function` examines every function
    whose FIRST parameter is annotated `Person`, which is why `p` is first here and not `row`:
    `binding_from`'s docstring recorded that the same guard could not see IT, because its first
    parameter was a `TypedRequires`. A signature is where that gets fixed, not a sentence."""
    req = row.requires_typed
    if req is None:
        return {}
    bound = tuple(req.operands())
    admitted = req.needs()
    out: dict = {}
    for name in bound + tuple(n for n in _REFERENT_OPERANDS
                              if n in admitted and n not in bound):
        # `actor` is structural on both sides and is never carried; see `binding_of`.
        if name == "actor":
            continue
        v = _derive_operand(p, name, q, subject, fx)
        if v is None:
            if name not in bound:
                # An operand the CELL does not read cannot make the act malformed -- it is simply
                # not carried. Declining here would refuse a verb for want of a value nothing asks
                # for, which is the FLOOR reading this function's docstring rejects.
                continue
            TRACE.note(f"{row.verb!r} needs operand {name!r} and {p.id} cannot derive it "
                       f"person-side (H-94); NO Candidate is formed -- an act minted with a hole "
                       f"is refused for the instrument's reason and witnessed as a false belief",
                       "§F1/H-94")
            return None
        out[name] = v
    return out


def agreement(told: list[Claim], own: list[Claim]) -> tuple:
    """§F4's `agreement`, DEFINED -- and defined over TWO CLAIM SETS, not over claims and
    convictions. Returns `(agreements, disagreements, paired_predicates)`.

    ⚠ V2 §F4 IS WRONG IN A WAY #353 NAMES AS ITS WORST FAILURE MODE. It writes
    `agreement(claims in p's own ledger where subject == p and source == told_by, p's own
    convictions)` -- the claim ledger against the convictions. #353 §9.3 is a table whose whole
    purpose is to keep those apart: the ledger holds what is **TRUE**, convictions hold what is
    **RIGHT**, evidence moves the first and argument moves the second, and *"WITNESS NEVER TOUCHES
    A BELIEF... This is the single most dangerous collision in the design."* A formula that scores
    agreement between them makes evidence bear on the moral layer, which is the collision itself.
    PLAN `W5` says as much: *"H-29's default is not injectable as written."*

    THE CORRECTION IS SMALL AND STAYS INSIDE §F4'S OWN ARGUMENT. §18.2 says standing is "the gap
    between what everyone reads off you and what you hold", and §F4 reads "what you hold" as
    convictions. Read it instead as WHAT YOU HOLD TRUE -- your own firsthand claims about yourself
    -- and both sides are the epistemic layer, the collision is gone, and all three properties §F4
    wanted survive: computable person-side, WRONG-ABLE (a liar moves your standing, which is T3),
    and no cross-holder read, so §20 is untouched.

    Claims are paired BY PREDICATE, on the `person_predicates` roster -- PLAN `W5`'s "defined
    predicate vocabulary". Without one, "pairing by predicate" is pairing on a free string."""
    own_by = {c.predicate: c for c in own if c.predicate in PERSON_PREDICATES}
    agree = dis = 0
    for c in told:
        if c.predicate not in own_by:
            continue                    # nothing of your own to compare it against
        (agree, dis) = (agree + 1, dis) if c.value == own_by[c.predicate].value else (agree, dis + 1)
    return agree, dis, agree + dis


def standing_of(p: Person, fx: "Fixtures") -> int:
    """S18.2's second scalar, PERSON-SIDE, as a fixed-point int on `condition_scale` (S48).

        standing(p) = gap( told_by claims about p , p's own firsthand claims about p )

    0 means everyone reads you exactly as you read yourself; `condition_scale` is total mismatch.
    §18.2 calls it "the GAP", so it is computed as a gap and not silently inverted into a
    reputation score -- ⚠ the WORD "standing" ordinarily suggests the opposite polarity, and that
    tension is recorded rather than resolved, because resolving it would be picking a meaning the
    design did not state.

    ⚠ NO PAIRED PREDICATE RETURNS THE MAXIMUM GAP, NOT ZERO, and that is `H-29`'s swept default.
    Zero would mean "nobody has told you anything about yourself, therefore everyone agrees with
    you", which is §42.2's polarity rule run backwards -- zero evidence maps to the verdict
    AGAINST the thing measured, and the flattering reading is the one that rule exists to refuse.
    Raising instead would restore the blocker §F4 warns about: standing blocked 9 cases for a
    value nothing could produce."""
    scale = fx.get("condition_scale")
    told = [c for c in p.ledger if c.subject == p.id and c.source == "told_by"]
    own = [c for c in p.ledger if c.subject == p.id and c.source == "firsthand"]
    _agree, dis, paired = agreement(told, own)
    return scale if paired == 0 else (dis * scale) // paired


def _payload_of(c: "Candidate") -> Optional[dict]:
    """WHAT A COMPUTED ACT CARRIES: its subject, and the operands its verb's cell names.

    ⚠ `subject` STAYS EVEN WHEN NO CELL BINDS IT, because it is not only an operand. `act_refs`
    reads it to say what an act NAMES, `claim_subjects` reads it to say what a deposit is ABOUT,
    and `tell` -- whose `writes:` is empty by design -- has nothing else that knows what was told.
    Dropping it for a verb whose requirement happens not to mention `subject` would break the
    causal graph for the one verb the corpus most relies on."""
    d = dict(c.operands or {})
    if c.subject:
        d.setdefault("subject", c.subject)
    return d or None


def pack_scenes(p: Person, ranked: list, n_scenes: int, fx: "Fixtures", mint,
                occasion: Optional["Question"] = None) -> list:
    """`H-78`: WHICH interactions share one scene. `H-76` says how many; this says which.

    ⚠ THIS WAS A COMMENT IN `make_chooser` UNTIL THE `W17` ADVERSARIAL PASS READ IT -- "the
    default policy fills scenes greedily in score order", with no row, no alternative and no
    sweep. That is `H-53`'s defect one level up, and `H-53`'s own row names the shape: the
    instrument answering a WHICH question the specification left open, inside a slice.

    `greedy` is that behaviour declared and kept as the control. `one_per_scene` is the pre-ruling
    accounting. `by_subject` groups the interactions that share a subject, which is what
    `player_agency_v30.md` §6.3's "one scene opportunity pursued" describes -- an opportunity is
    an opportunity to do something ABOUT something."""
    rule = fx.get("scene_packing_rule")
    if rule not in SCENE_PACKING_RULES:
        raise Unspecified(
            f"scene-packing rule {rule!r} is not in the roster", "H-78",
            needs=f"one of {sorted(SCENE_PACKING_RULES)}",
            law="H-78 -- nothing in the chain says WHICH interactions share a scene, so a rule "
                "outside the roster is a fourth answer nobody declared")
    per = fx.get("interactions_per_scene")
    width = 1 if rule == "one_per_scene" else (len(ranked) if per is None else per)

    def scene(n: int, chunk: list) -> "Scene":
        # ⚠ `occasion=` IS NOT DECORATION. `choose` already holds the question — it refuses to
        # produce anything without one — and dropping it here is what left the act with no route
        # back to what raised it (`N3`).
        return Scene(mint(p.id, "scene", str(n)), p.id,
                     # ⚠ THE CANDIDATE'S SUBJECT REACHES THE ACT, AND IT USED NOT TO. This read
                     # `Act(mint(...), p.id, c.verb)` — three arguments — so `opening_set`
                     # computed a subject from the question's referents, `mint` folded it into the
                     # act's ID, and the act itself carried NOTHING. `_req_tell` reads
                     # `payload["subject"]` and got `None`, so `tell` was attempted and refused in
                     # every world in the corpus; `_eff_tell` had no target either.
                     #
                     # ⚠ THAT WAS HALF OF `H-94` AND `W-C` CLOSED THE OTHER HALF. The
                     # Candidate carries `operands` now, derived person-side from the actor's own
                     # Tenures, the question's referent and two fixtures, so
                     # `stores(hearth(giver), kind) >= amount` has a `from`, a `kind` and an
                     # `amount` -- and the act CARRIES them, which is what makes the fold bind
                     # what the person bound. The subject is written first and the operands over
                     # it, so a cell that binds the referent under its own name (`to`, `site`)
                     # cannot disagree with `subject` about which thing that is.
                     [Act(mint(p.id, c.verb, c.subject or ""), p.id, c.verb,
                          payload=_payload_of(c)) for c in chunk],
                     # `H-77`: a scene carrying more than one interaction is the EXTENDED one.
                     # This is what `extended` MEANS, and until W17's adversarial pass nothing
                     # ever set it -- so `Scene.cost` returned 1 unconditionally, H-77's sweep
                     # could not move any verdict, and the row passed R2 while being
                     # unexecutable. That is the laundering R2 exists to stop, in the row that
                     # was added the same day the rule was written.
                     extended=len(chunk) > 1, occasion=occasion)

    # ⚠ THE BOUND IS THE COST, NOT THE SCENE COUNT, and getting that wrong made the DEFAULT
    # chooser overspend by construction: once `extended` was actually set, five greedy scenes
    # cost ten against a budget of five and every season using `make_chooser` refused itself.
    # Found by running the corpus after `H-77` stopped being inert -- the row and the packer are
    # the same mechanism seen from two sides, and fixing one without the other is what broke it.
    ext = fx.get("extended_scene_cost")

    def take(chunks) -> list:
        out, left = [], n_scenes
        for chunk in chunks:
            if left <= 0:
                break
            # An extension the person cannot afford is taken as a PLAIN scene rather than
            # skipped: they still pursue the opportunity, with less in it. Skipping would be the
            # engine deciding what they leave undone, which is L1.
            if len(chunk) > 1 and ext > left:
                chunk = chunk[:1]
            cost = ext if len(chunk) > 1 else 1
            out.append(scene(len(out), chunk))
            left -= cost
        return out

    if rule == "by_subject":
        seen: dict = {}
        for c in ranked:
            seen.setdefault(c.subject or "", []).append(c)
        chunks = [seen[subj][start:start + width]
                  for subj in sorted(seen)
                  for start in range(0, len(seen[subj]), width)]
    else:
        chunks = [ranked[i:i + width] for i in range(0, len(ranked), width)]
    return take(chunks)


def aggregate_questions(qs: list, rule: str):
    """`H-54`: how many of a person's questions reach `assemble` in one season.

    #353 says NOTHING about this and the instrument answered it silently as `qs[0]` for four
    revisions. `first` preserves that answer as a declared, swept default; `all` and
    `one_per_source` are the alternatives the sweep compares it against. Returns ONE question,
    because `assemble(person, question)` takes one -- the rules differ in WHICH, and in how many
    are folded into it, which is exactly what is open."""
    if rule not in QUESTION_AGGREGATION:
        raise Unspecified(
            f"question-aggregation rule {rule!r} is not in the roster", "H-54",
            needs=f"one of {list(QUESTION_AGGREGATION)}",
            law="H-54 -- nothing in #353 says how many questions a person forms per season, so a "
                "rule outside the roster is a fourth answer nobody declared")
    if not qs:
        return None
    if rule == "first":
        return qs[0]
    if rule == "one_per_source":
        seen, keep = set(), []
        for q in qs:
            if q.source not in seen:
                seen.add(q.source); keep.append(q)
        qs = keep
    # `all` and `one_per_source` widen the REFERENTS rather than the question count, because
    # `assemble` takes one question. The person brings everything they are being asked about.
    refs = tuple(sorted({r for q in qs for r in q.referents}))
    return Question(f"q:agg:{rule}:{qs[0].id}", qs[0].source, refs, qs[0].about)


def view_ids(p: Person, q: Any, k: int, rule: str) -> list:
    """§18's "at most K claim ids from the holder's OWN ledger -- BUILT, not filtered". `H-53`.

    ⚠ #353 SUPPLIES K AND NEVER SUPPLIES WHICH K, and "built, not filtered" says what a View is
    NOT. `H-09` gives `K = 12`; nothing in the chain says which twelve of a 200-claim ledger a
    person brings to a question, and taking the last k -- which every revision before `W5` did
    silently -- is an invention. The rules are `rosters.yaml: view_builder_rules`, `recent` is the
    default because it is the incumbent and a sweep needs an honest control, NOT because it is
    argued for.

    PERSON-SIDE: it reads `p.ledger` and the question's own referents. No World."""
    if rule not in VIEW_BUILDER_RULES:
        raise Unspecified(
            f"view-builder rule {rule!r} is not in the view_builder_rules roster", "H-53",
            needs=f"one of {sorted(VIEW_BUILDER_RULES)}",
            law="§18 -- 'at most K ids ... BUILT, not filtered'. WHICH K is `H-53` and is open; "
                "a rule not on the roster is a fourth answer nobody declared")
    if rule == "highest_confidence":
        ranked = sorted(p.ledger, key=lambda c: (-c.confidence, c.id))
        return [c.id for c in ranked[:k]]
    if rule == "question_relevant":
        refs = set(getattr(q, "referents", ()) or ())
        near = [c for c in p.ledger if c.subject in refs]
        rest = [c for c in p.ledger if c.subject not in refs]
        # Relevant first, then the incumbent order for the remainder -- a person brings what the
        # question is about AND whatever else is freshest, rather than only the former.
        return [c.id for c in near[-k:]] + [c.id for c in rest[-(k - min(len(near), k)):]] \
            if k > len(near) else [c.id for c in near[-k:]]
    return [c.id for c in p.ledger][-k:]


def body_band_penalty(p: Person, fx: "Fixtures") -> int:
    """How many bands `p`'s body has fallen below the top, on `band_floors["body"]`.

    PERSON-SIDE: it reads `p.body` and a params table, never a World. `H-38` closed with *"the
    answer is YES -- `Site.condition` is the model"*, and this is that closure SPENT: the same
    floors table, the same "a band is a floor you are at or above" reading, one kind lower. A
    second band scheme would have been the invention `H-38` was closed to avoid.

    Returns 0 at full operations and rises by one per band crossed, so the order is FIXED and
    the narrowing is monotone -- which is the property `P32` names."""
    floors = fx.get("band_floors")["body"]
    # Descending, so "the top band" is unambiguous and the count is the number of floors passed.
    return sum(1 for f in sorted(floors.values(), reverse=True) if p.body < f)
