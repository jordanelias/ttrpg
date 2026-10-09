"""`decision/` -- the `opening_set` member of `04_CODE_ARCHITECTURE.md` §A.2:133, and its helpers.

⚠ **THE FILE IS `options.py` AND THE MEMBER IS `opening_set`, DELIBERATELY.** §A.2:133 names four
members; a module named `opening_set.py` beside a function named `opening_set` makes
`decision.opening_set` ambiguous -- `__init__.py`'s re-export shadows the submodule -- and the
rebind surface needs the MODULE by name. "Option set" is the tree's own existing phrase for what
this returns, so the filename is idiomatic rather than coined (`CLAUDE.md` §4).

`opening_set` and its operand machinery (`operands_for`, `_derive_operand`, `_REFERENT_OPERANDS`,
`containing_rung_of`, `store_kind_of`, `_from_content_claim`, `_from_shortfall_claim`), the
eligibility predicate, and the two agreement/standing readers.

⚠ `entrenchment` SITS HERE PROVISIONALLY AND L3 RE-ADJUDICATES IT. Three functions in the old
`decision.py` self-declared as person-side Queries via `TRACE.query(..., "person")`: `budget`,
`opening_set` and `entrenchment`. The first two are named by §A.2:133 as `decision/` MEMBERS and
therefore cannot move to `queries/person_q` -- which is why `ED-IN-0206` item (2) is wrong about
them. `entrenchment` is the only one of the three that §A.2:133 does not name, so it is the only
real `queries/person_q` candidate in this file, and L3 owns that call.

AX-2 binds every file under `decision/`: no `World`, as an import, a name, an attribute or a
string. Enforced BY PATH over this directory (`04:1046`).
"""

from __future__ import annotations

from typing import Any, Callable, Optional
from ..data.cast import STANCE_MAX
from ..data.pursuits import to_axes
from ..data.requires import (
    CELL_STEMS, SHORTFALL_PREDICATE, SHORTFALL_SOURCED_OPERANDS, WRIT_SOURCED_OPERANDS,
)
from ..data.rosters import PERSON_PREDICATES, PURSUIT_AXES, RECORD_CONTENT, require_member
# `align` is imported, never `ALIGNMENT`: the table's one binding is `data.verbs.ALIGNMENT`, which the
# `H-66` sweep rebinds, and `align` reads it there.
from ..data.verbs import ELIGIBILITY_KINDS, VERB_TABLE, align
from ..epistemic import belief_contradicts
from ..gaps import Forbidden
from ..queries.person_q import LedgerReader, crisis_weights, known_persons, regard, said_of
from ..state.carriers import Candidate, Claim, Person, Question, View
from ..trace_log import TRACE


def opening_set(p: Person, v: View, q: Question, fx: "Fixtures") -> list[Candidate]:
    """§F1 -- COMPUTED FROM THE VERB TABLE. No `roster` parameter: that is `D2` entire.

    ⚠ WHAT CHANGED, AND WHY IT COULD NOT CHANGE BEFORE. Rev 2 took `roster: list[Candidate]`
    and returned it, and said so: "the PROPERTY S17 chose the type to protect -- an option set
    that is COMPUTED rather than an AUTHORED LIST -- is not [faithful], because `roster` is the
    caller's authored list." Its reason was real: §61 gave `q` no producer, so there was
    nothing to compute a set FROM. `questions_for()` is that producer, so the roster's excuse
    is gone and with it the roster.

        { Candidate(verb, subject, operands) :                   -- §F1's `why`: gone, `14`
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

    ⚠ **THIS PARAGRAPH DESCRIBES THE PRE-2026-09-18 BEHAVIOUR AND IS KEPT AS THE RECORD.**
    `H-71` IS CLOSED: `remit:` is now evaluated person-side off the `hold` Tenure's granted acts,
    and `presence:` is the only kind still declining unconditionally. What follows is why it could
    not be evaluated before, which is still the reason the hole existed.

    ⚠ ONE OF §F1'S FOUR ELIGIBILITY KINDS CANNOT BE EVALUATED HERE, and it declines rather
    than admitting. See `person_side_eligible`: `remit:` needs the OFFICE's remit, and #353
    §11.1 is explicit that "who holds an office is NOT a field on the office -- it is a `hold`
    Tenure, owned by the holder", which gives the person the TENURE and leaves the REMIT with
    the office. That is a genuine collision in §F1 and it is registered (`H-71`), not filled.
    It is not the `budget` case: there the data was the person's and merely stored in the
    wrong place, and no such relocation is available for a remit two holders share."""
    TRACE.query("opening_set", "person")
    out: list[Candidate] = []
    axis = fx.get("refusal_axis")
    tolerance = refusal_tolerance(p, axis)
    # `T3a`: clause 4's reader grades hearsay by its teller. A ledger holding no told claim weighs
    # 1.0 everywhere, which is the unweighted order exactly (tested), so it takes the plain reader.
    weigh = teller_weight(p, fx) if any(c.chain for c in p.ledger) else None
    for verb, row in sorted(VERB_TABLE.items()):
        if not person_side_eligible(p, row):
            continue
        if tolerance is not None and refuses(verb, axis, tolerance):
            TRACE.note(f"{p.id} refuses {verb!r}: its `{axis}` alignment exceeds their own "
                       f"projected weight {tolerance:+.3f} (ED-IN-0261)", "H-146")
            continue
        # `19`: the seat this row's act would exercise -- `exercised_seat`, the same untraced walk
        # `pack_scenes` names `Act.via` by -- for the belief test's `basis` conjunct below.
        seat = exercised_seat(p, row)
        # `T4`: only a NAMED own-ledger conjunct carries `said` (`tell`'s `holds`); `survey` and
        # `reconstruct` share the form unnamed and carry nothing (telling workplan, "From Batch 1").
        ledger_of = row.requires_typed.named_own_ledger_operands() if row.requires_typed else ()
        said_of_entity: dict = {}           # entity -> `said_of` (this row's own-ledger read, per entity)
        for subject in q.referents:
            # ⚠⚠ A CONTEST NEEDS TWO CLAIMANTS, AND A PERSON IS NOT THEIR OWN ADVERSARY.
            # `move`'s `contain_path` cell keeps the same shape of rule -- *"a node is not a path
            # to itself"* -- as the reader's own, and this is that rule one seam over. It reads
            # the ROW'S OWN COLUMN (`contests:`), never a verb name, so it holds for whatever
            # else declares a prize later.
            #
            # MEASURED, the day `kill / wound` was admitted to `resolvable_verbs()`
            # (`ED-IN-0261`, amended): `opening_set` offers every person THEMSELVES as a referent
            # for every verb -- 49.6% of all candidates in the one-season sweep name the actor as
            # their own subject -- so the commonest contested candidate in the corpus was a
            # person attacking himself. 47 of 143 cases died on `personal combat needs two
            # parties; got 1` for no other reason.
            #
            # ⚠ WHY IT DECLINES HERE RATHER THAN REFUSING IN THE FOLD, which is the opposite of
            # the choice clause 4 makes: clause 4 is EPISTEMIC -- a person who wrongly believes
            # the granary full SHOULD form the Candidate and learn otherwise -- and being alone
            # in a room is not a belief anyone can be wrong about. There is no world-read here
            # and no `World`: `p.id` against a referent the person already holds.
            # ⚠ ONLY WHERE THE ROW NAMES NO COUNTERPARTY (telling workplan `T4`, Decision 3). A row
            # that names its second side on its own operand contests against THAT (`tell`'s `to`),
            # so its `subject` is a topic and a person may tell somebody about themselves; the
            # counterparty rule below still declines the person as their own second side.
            if row.contests and not row.counterparty and subject == p.id:
                continue
            # ⚠ OPERANDS BEFORE THE BELIEF TEST, AND THE ORDER IS THE POINT. Clause 4 asks
            # whether the requirement is known-false ABOUT THIS BINDING, so the binding has to
            # exist first -- asking it of an unbound cell is what made the person read a
            # different granary from the fold.
            # `T4`: ONE CANDIDATE PER BAG -- one bag for every row but one whose `to` is a KNOWN
            # PERSON (`operand_bags`), which forms one per person the teller knows.
            for ops in operand_bags(p, row, q, subject, fx):
                # ⚠ AND A TWO-SIDED ACT NEEDS A SECOND SIDE (plan position `15`, `ED-IN-0210` ruling
                # 2). The rule above, one column over: a row naming its `counterparty:` operand forms
                # no Candidate whose counterparty is the person -- a petition to oneself is the
                # Tenure(X,X) fiat ruling 1 names. Declined HERE, not refused in the fold, for the
                # reason the contest rule gives: no read the fold makes can say *that is you*, so a
                # refusal teaches nothing -- MEASURED, it fed itself (the refusal's claim about the
                # petitioner raised the next question about them). Reads the row's column, never a
                # verb name, and the loader guarantees the operand is carried.
                # ⚠ AND A SECOND SIDE NOBODY CAN NAME IS NO SECOND SIDE (plan position 16). On a TYPED
                # row the loader guarantees the counterparty is carried, so `None` cannot arise there.
                # On an UNTYPED row (`oblige`; `give` until plan position `14` typed it) nothing is
                # carried, and forming the Candidate would mint an act with no second party --
                # refused by the fold every time, for the instrument's reason. MEASURED before this
                # clause, the `give` row without it: 3 such acts in
                # `headless.run(3, 0)` and 41 in `populated.run(2, 0)`, every one `give.refused`, and
                # `release` dropped out of the corpus's executed set because they took its scenes --
                # position `15`'s *constant scene tax with nothing behind it*, the shape the petition
                # row's seat reading was refused for.
                if row.counterparty and ops.get(row.counterparty) in (None, p.id):
                    continue
                # `19`: THE SEAT THE ACT WILL BE EXERCISED THROUGH rides into the belief test as it rides
                # onto `Act.via` (`pack_scenes`), so a `basis` conjunct is asked of the same seat both
                # sides. `seat` is `exercised_seat`, read once per row above.
                # `T3a`: and the person reads their own ledger WEIGHING hearsay by its teller.
                if belief_contradicts(p, row, subject, ops, seat, weigh=weigh):
                    continue
                # WHAT THE TELLER WILL SAY IS DECIDED HERE, AT CHOOSE, AND RIDES THE ACT (`T1`,
                # `workplans/2026-10-01-telling-workplan.md`): a row whose typed cell holds a NAMED
                # `own_ledger` conjunct (`T4`; found by walking the form, never by a verb name)
                # passes on what the actor HOLDS about the clause's entity, copied out of their own
                # ledger now, so WITNESS reads the Act and never the teller's live ledger. Placed
                # after every decline so the copy is paid only for a Candidate that is formed;
                # `said` is not a `requires_operands` member, so `binding_of` drops it from both
                # readers' bindings.
                # ⚠ AND NOTHING TO SAY IS DECLINED (T1's deferral, decided at `T4`): a telling that
                # carries nothing passes nothing on, and the fold used to refuse it on `holds`
                # anyway -- a scene spent on a refusal the person could have known. Measured at T1:
                # 3 of 31 corpus candidates. Only the named conjunct declines; `survey` and
                # `reconstruct` carry no `said` and are untouched.
                if ledger_of:
                    # `said` depends on the entity alone, never on the hearer, so a subject's
                    # one telling is read once however many hearers it fans to.
                    entity = ops.get(ledger_of[0])
                    if entity not in said_of_entity:
                        said_of_entity[entity] = said_of(p.ledger, entity, fx)
                    said = said_of_entity[entity]
                    if said is None:
                        continue
                    ops = {**ops, "said": said}
                out.append(Candidate(verb, subject, operands=ops))
    return out


# ⚠ `project` LIVES HERE, NOT IN `choose.py`, AND THE REASON IS AN IMPORT CYCLE THAT EXECUTED.
# `ED-IN-0261`'s refusal gate (`H-146`) made `opening_set` call it, and it was reached by
# `from .choose import ...` inside a function body while `choose.py` imports this module at top
# level: `choose <-> options`, a real runtime cycle that
# `tests/valoria/test_import_cycle_game_state_npe.py` counted, because a deferred import hides a
# cycle from an instrument without removing it. It is defined ONCE, here, and `choose.py` imports
# it back -- the edge now runs one way only.
#
# `align` is NOT here any more: it moved to `data/verbs.py` beside `ALIGNMENT` (telling workplan T2),
# so the `H-66` rebind is `data.verbs.ALIGNMENT` and reaches `choose`'s score and this module's
# `refuses` gate through the one function. `project` is still recorded for the same move into
# `data/pursuits.to_axes`, its own docstring's stated single owner; not done here.


def project(p: Person, scar_shift: float = 0.0) -> dict:
    """A person's thirteen conviction weights, in the four-axis basis. `U3` / R-06a.

    ⚠⚠ **§F2's `conviction[axis]` IS COMPUTED NOW, NOT LOOKED UP, AND THE FORMULA IS UNCHANGED IN
    SHAPE.** V2 §F2 spells `score(c) = Σ_axis conviction[axis] · alignment(c.verb, axis)` and that
    indexing only works if a person's convictions are KEYED BY AXIS — which is what
    `pursuit_axes` used to be forced to be, holding `Precedent` (a conviction) beside
    `self_preservation`, `suspicion` and `harm_borne` (three ad-hoc scalars) so the lookup had
    something to hit. `pursuit_axes`'s own note named the conflation and predicted the repair.
    So:

        conviction[axis]  :=  Σ_conv  p.pursuits[conv] · projection[conv][axis]

    and `Σ_axis` above is untouched. A person holds weights over the THIRTEEN; the projection is
    the only thing that knows about axes.

    ⚠ **THE MATRIX IS READ, NOT INVENTED** — `conviction_axis_matrix_v30.md` §2, with a per-cell
    rationale in its §3. That is the difference between this table and `alignment`, whose own note
    says of its cells *"a reason is not a citation"*. They multiply together, so which of the two
    is argued and which is cited is worth being able to see.

    ⚠ **A CONVICTION THE MATRIX DOES NOT LIST PROJECTS TO NOTHING, AND THAT IS THE SPARSE DEFAULT
    RATHER THAN A SILENT DROP.** `PROJECTION_DEFAULT_CELL` is the declared 0.0; the loader has
    already refused any conviction name outside the roster, so an unlisted pair here is a cell the
    data chose to leave sparse, not a typo that got through.

    ⚠ DELEGATED, NOT DUPLICATED. `data.pursuits.to_axes` is the one owner of *convictions → axes*,
    because a second caller appeared that does not have a `Person`: `data.cast.loyalty` projects a
    ROLE TEMPLATE's expected-conviction vector through the same 13×4. `to_axes` reads
    `data.verbs.PURSUIT_PROJECTION` at call time, so that is still the rebind that reaches here.

    ⚠ `scar_shift` is IN-08 H9's crisis reader (`Fixtures.scar_weight_shift`, `H-187`): the weights
    `to_axes` projects are `person_q.crisis_weights(p, scar_shift)` -- a pursuit whose scar count has
    reached threshold 2 gives weight to the others. `0`, the shipped control, hands `to_axes` the
    person's own `pursuits` untouched. Only `choose`'s score passes it; `refusal_tolerance` (dormant)
    reads the unshifted weight."""
    return to_axes(crisis_weights(p, scar_shift))


def refusal_tolerance(p: Person, axis: Optional[str]) -> Optional[float]:
    """`ED-IN-0261`'s deontological gate, the PERSON half: their projected weight on the gating
    axis, which IS the threshold (Jordan: *"the weighting is a threshold for certain actions"*).
    `None` when `refusal_axis` is unset -- the control arm, under which `opening_set` refuses
    nothing. The axis is whatever `Fixtures` names, checked against the live roster, never a
    literal here.

    ⚠ RUNS `project(p)` A SECOND TIME FOR THE SAME PERSON `choose()` PROJECTS FOR `score`, AND
    THIS IS KNOWN AND DEFERRED, NOT MISSED. Dormant today -- `refusal_axis` ships unset, and this
    line short-circuits above before `project` is ever called. Threading the caller's own
    projection through would need an optional parameter on `opening_set` itself, which breaks
    every test/harness spy pinned to its current four-parameter arity (measured: one such spy in
    `test_governance_build.py` alone); worth doing WITH `H6`, when the gate ships live and the
    cost stops being theoretical, not as a speculative widening now."""
    if axis is None:
        return None
    require_member(axis, PURSUIT_AXES, f"refusal axis {axis!r} is not on the pursuit_axes roster",
                   "H-146", law="ED-IN-0261 -- the gate reads a ROSTERED axis; an unrostered one "
                                "would raise `Unspecified` rather than project to a real weight")
    return project(p)[axis]


def refuses(verb: str, axis: str, tolerance: float) -> bool:
    """Does a person whose weight on `axis` is `tolerance` refuse `verb`? The PERSON-SIDE refusal
    `score` cannot express: it ranks, and at `choice_temperature` 0.1 a good enough outcome
    outranks any finite penalty (`ED-IN-0261`).

    Sign convention: the axis's NEG pole is the refusing one (`deontological` on
    `deontological/instrumental`), so a verb is refused when its alignment sits further toward the
    POS pole than the person's own weight. Only a verb the axis ENGAGES can be refused -- a zero
    cell, including the sparse default, is not one of the *"certain actions"* the ruling gates;
    the scar's `person_q.elements_violated_by` reads engagement the same way.

    Reads `data.verbs.align`, the one `choose`'s score reads too, so a rebind of
    `data.verbs.ALIGNMENT` moves the gate and the ranking together."""
    a = align(verb, axis)
    return bool(a) and a > tolerance


def person_side_eligible(p: Person, row: "VerbRow") -> bool:
    """§F1 clause 2, PERSON-SIDE. `own | remit | hold | presence`, NEVER `capability`.

    A DISJUNCTION: `transfer` is eligible by `own` OR `hold:<store>`, so one alternative admitting
    is enough and one alternative declining decides nothing.

    ⚠ **ONE OF THE FOUR KINDS DECLINES HERE — `remit:` NO LONGER DOES, AS OF 2026-09-18 (`13b`,
    `H-71`).** The bullet below is kept because it states WHY the hole existed and what closed it,
    but read it as history: the grant now rides on the `hold` Tenure (`World._grant_remit` writes
    it at `add_tenure`, `Tenure.granted_acts` owns the shape) and the body 45 lines down ADMITS on
    `arg in t.granted_acts`. An earlier version of this docstring still opened *"TWO OF THE FOUR
    KINDS DECLINE"* with the `remit:` bullet unmarked, so the function a reader opens to learn the
    rule stated the opposite of what it did.

    ⚠ THE DECLINING KIND NAMES ITS HOLE, and neither it nor any other branch admits on an
    unevaluable predicate -- that would be a silent fill off the register (`G1`) at the opposite
    polarity to §42.2, which sends zero evidence to the verdict AGAINST the thing measured. The
    resolver's `_eligible` still evaluates both, because it HAS a `World`; this is the person's
    reading, and the gap between the two readings is the finding.

      * ~~`remit:<act>`~~ **— CLOSED 2026-09-18, kept as the history of the hole.** It needed
        the OFFICE's `remit_acts`, which the person could not see. #353 §11.1: "who holds an
        office is NOT a field on the office -- it is a `hold` Tenure, owned by the holder", so
        the person owns the tenure and the office owns the remit. Unlike `budget`'s collision
        there is no relocation available: two holders of one office share one remit, so it is not
        the person's state to move. §F1 asserted this clause is person-side and did not say
        how; `13b` is the how — a SNAPSHOT of the office's remit is stamped onto the Tenure when
        the hold opens, so the person reads their own row and `choose` still receives no `World`.
      * `presence:<rung>` -- declined because the ARGUMENT IS A PLACEHOLDER naming a kind of
        rung rather than an id, which is `H-75`, and is the same reasoning the `hold:<store>`
        branch already carries one block below. ⚠ CORRECTED BY `W6`'s adversarial pass: this said
        *"`H-33`, the presence index, which does not exist"*, and `W6` BUILT it -- `_ch_co_located`
        reads it and `H-33` now carries a `site:`. The citation survived the thing it cited. The
        refusal itself is unchanged and correct; only its reason was stale."""
    return _admitted_through(p, row, trace=True)[0]


def exercised_seat(p: Person, row: "Optional[VerbRow]") -> Optional[str]:
    """G3 -- THE SEAT A COMPUTED ACT EXERCISES: the office id its `Act.via` carries, or `None`.

    `04 §B.9` gives `Act` a `via : SeatId?` and `04:332` asks purview of the seat exercised, so
    the act a person mints has to say which seat it is exercised through -- and only the person can
    say, because only the person's own Tenures are in scope here (AX-2). It is the seat through
    which `person_side_eligible` ADMITTED the verb, read by the SAME walk (`_admitted_through`) so
    the two cannot disagree: a `remit:` alternative admits through the first live `hold` whose grant
    carries the act, and that hold's object is the seat. An `own` or `hold` alternative admits the
    person AS THEMSELVES, and no seat is exercised -- `kill / wound`, `transfer`, `release` all mint
    with `via=None`. The fold's `_eligible` then admits the same act through the same seat, so
    making `via` required there moves no computed act (measured: `build_realm(0)`'s content hash
    over one season is unchanged by G3).

    ⚠ WHICH SEAT, WHEN SEVERAL GRANT THE ACT, IS THE FIRST IN THE PERSON'S OWN TENURE ORDER -- a
    fixed rule, not a choice, and a LIMIT stated rather than hidden: a person holding two seats that
    both grant `confer` always exercises the first, even where only the second has purview over
    the target. Choosing by purview would need the containment tree, which is not the person's
    state. ⚠ PURVIEW IS `confer`'S TEST AND NOT EVERY ACT'S: `revoke` asks the PARENT RUNG
    (`state/gate.py::seated_on_the_rung_above` -- `via`'s rung is the one directly above the
    target seat's, same faction), and asks no purview. ONE WORLD BUILDER SEATS SOMEONE TWICE TODAY
    (`H-134`): `build_realm` gives NPC-020 `off_npc_020` (the realm, built by the per-case loop) and
    the minted `off_duke_valorsmark`, both granting issue/confer/revoke/convene, and the loop's hold
    precedes the minted one in his tenure order, so all his computed acts go via the King seat and
    the Duke seat is never exercised. For `confer` that costs nothing while the realm seat's purview
    reaches. For `revoke` it is the WRONG SEAT outright: the six Crown seats at T1 marked
    `rung_above_same_faction` (`offices.yaml`) can be stripped only through `off_duke_valorsmark`,
    and `_granting_hold` below always picks `off_npc_020`. The refusal that follows is silent and is
    masked only because a computed `revoke` carries no `office` operand, so `_req_revoke`
    (`loop/predicates.py`) refuses before the seat is ever asked. Where that choice ever matters, it
    becomes a candidate per seat. Traces nothing: the admission it mirrors already traced. A verb
    on no row (`row is None` -- a hand-ranked candidate naming an invented verb) exercises nothing;
    the fold refuses the verb itself, and inventing a seat for it here would be a second answer."""
    if row is None:
        return None
    return _admitted_through(p, row, trace=False)[1]


def _granting_hold(p: Person, act: str):
    """The first live `hold` in the person's OWN store whose grant carries `act`, or `None` -- the
    one person-side reading of *which seat grants this* (`H-71` arm 2's snapshot)."""
    return next((t for t in p.tenures if t.kind == "hold" and t.live and act in t.granted_acts),
                None)


def _admitted_through(p: Person, row: "VerbRow", trace: bool) -> tuple:
    """`(admitted, seat)`: `person_side_eligible`'s walk over the row's DISJUNCTION, once, for both
    of its readers -- the FIRST alternative that admits decides, and `seat` is the office it admitted
    through (`None` unless that alternative was `remit:`). `trace=False` is `exercised_seat`'s
    reading of a verb the first reading already traced, so the trace records each decline once."""
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
            return (True, None)
        if kind == "hold":
            # ⚠ THE ARGUMENT IS COMPARED. It was parsed and thrown away, so `transfer`'s
            # `hold:<store>` and `destroy_record`'s `hold:<record>` admitted anyone holding ANY
            # office -- an OVER-admission, which `G4` makes a defect of equal weight to an
            # over-refusal. `<store>`/`<record>` are PLACEHOLDERS naming a kind of object, not
            # ids, so a placeholder cannot be matched against a Tenure's `object` and this
            # DECLINES rather than guessing which store the act meant: that binding is `H-75`.
            if not raw:                       # bare `hold` -- holding anything admits
                if any(t.kind == "hold" and t.live for t in p.tenures):
                    return (True, None)
            elif not placeholder:             # a literal object id
                if any(t.kind == "hold" and t.live and t.object == arg for t in p.tenures):
                    return (True, None)
            elif trace:
                TRACE.note(f"`hold:<{arg}>` names an object KIND, not an id (H-75); "
                           f"{row.verb!r} declines rather than admitting on any held object")
        # `remit` and `presence` decline: see the docstring. TRACE records the decline so the
        # count is measurable rather than inferred from a verb's absence.
        elif kind == "remit":
            # ⚠ `H-71` CLOSED HERE, arm 2. The grant rides on the Tenure: `World._grant_remit`
            # stamps the office's remit acts into the `hold` Tenure's `payload` at the ONE writer,
            # and `Tenure.granted_acts` owns the shape both sides read. So the holder's own state
            # answers this, `choose` still receives no `World`, and `AX-2` is untouched.
            # A placeholder is not matched, for the same reason `hold:<store>` refuses: `<act>`
            # names a KIND of act, not one, and admitting on it would be the over-admission `G4`
            # weighs equally with an over-refusal. Every live `remit:` cell in `verb_table.yaml`
            # is a literal (`remit:issue`, `remit:confer`), so this refuses nothing that exists.
            # G3: the hold that grants it IS the seat exercised -- returned, not just found.
            seat = _granting_hold(p, arg) if arg and not placeholder else None
            if seat is not None:
                return (True, seat.object)
            if not trace:
                continue
            if placeholder:
                TRACE.note(f"`remit:<{arg}>` names an ACT KIND, not an act (H-75); "
                           f"{row.verb!r} declines rather than admitting on any granted remit")
            elif not arg:
                TRACE.note(f"bare `remit` names no act; {row.verb!r} declines")
            else:
                TRACE.note(f"`remit:{arg}` not granted on any live `hold` this person holds; "
                           f"{row.verb!r} declines")
        elif kind == "presence" and trace:
            TRACE.note(f"`presence:` eligibility is unevaluable person-side (H-33, the presence "
                       f"index); {row.verb!r} declines rather than admitting")
    return (False, None)


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


def _claim_by_id(p: Person, claim_id) -> Optional["Claim"]:
    """THE ONE CLAIM IN `p`'S OWN LEDGER WITH THIS ID, or `None`. `store_kind_of` and
    `_from_content_claim` (both below) each look a claim up by `q.about` before reading its
    predicate -- this is that lookup, factored once so it is not two loops over `p.ledger` written
    the same way. §20's constraint (a person's own ledger, never the world) lives at the call
    site, not here: this takes the ledger it is handed."""
    for c in p.ledger:
        if c.id == claim_id:
            return c
    return None


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
    c = _claim_by_id(p, q.about)
    if c is None:
        return None
    # `stores` is `transfer`'s own `scalar:`, and `f"{scalar}:{key}"` is how `Observation`
    # derives the predicate -- so this reads the namespace the cell writes rather than a
    # second vocabulary. A claim about anything else names no matter kind.
    stem, sep, arg = str(c.predicate).partition(":")
    return arg if sep and arg and stem == "stores" else None


def _from_content_claim(p: Person, q: "Question", name: str):
    """AN OPERAND READ OFF A HELD (or merely witnessed) WRIT -- position `15c`, r2
    `02_THE_WRIT_AND_THE_WORD.md` §A.13: *"the operands are the WRIT's, not the fixtures'."*
    Modelled on `store_kind_of`, one paragraph above: both read a claim by `q.about`, never by
    the referent, because a document's content is what the PERSON HOLDING IT believes, and
    `AX-2` puts a belief nowhere else (§20) -- `subject`/the referent is a different fact and
    stays on its own branch below.

    `None` when `q.about` names no claim in `p`'s own ledger, the claim's predicate does not
    start `content:`, or its value has no key `name`. ⚠ THAT LAST CASE IS THE LIVE ONE FOR TWO
    OF THE THREE CALLERS. `record_kinds`'s two schemas actually built (`15`) are
    `dispensation: [terms, to, at]` and `petition: [terms, to, from]` -- so a call for `to`
    resolves (both kinds address someone), and a call for `kind`/`amount` declines EVERY TIME
    today, because neither schema carries either key; the caller's existing fixture/referent
    fallback runs exactly as it does for a person naming no writ at all. That is a fact about
    today's two live schemas, not a limit of this function -- a later kind that does carry
    `kind`/`amount` needs no change here.

    ⚠ A SINGLETON LIST COLLAPSES TO ITS ONE ID; ANY OTHER COUNT DECLINES. `to`'s writ-side type
    is `[PersonId|OfficeId]` (r2 §A.3) -- a LIST, because a document may address several people
    -- but every operand this vocabulary has ever carried is a SCALAR (`_derive_operand`'s own
    `to`/`subject`/`site` branches, `_eff_transfer`'s single `w.rungs.get(...)`). FOUND BY
    RUNNING THE POPULATED CORPUS, not reasoned in advance (`CLAUDE.md` §0.1 pt 3): the first
    writing of this function returned the raw tuple, and 173 `petition`/`transfer` Candidates
    formed carrying it verbatim -- each one UNABLE TO EVER RESOLVE, because `w.persons`/
    `w.rungs` key on strings and a tuple matches nothing there, EVEN WHEN the sole named
    addressee genuinely exists. That is the instrument inventing a NEW way to refuse an act for
    a reason that is not there (§42.2's polarity), on top of the ones the design already has.
    Naming WHICH of several addressees a scalar operand means is a choice nobody has ruled --
    `ID-13`'s `floor` precedent -- so more than one, or none, declines exactly as an unreadable
    floor does; exactly one is not a choice at all, so it is not held back."""
    if q is None or not q.about:
        return None
    c = _claim_by_id(p, q.about)
    if c is None:
        return None
    stem, sep, _ = str(c.predicate).partition(":")
    if not sep or stem != RECORD_CONTENT.get("predicate") or c.value is None:
        return None
    v = dict(c.value).get(name)
    if isinstance(v, tuple):
        return v[0] if len(v) == 1 else None
    return v


def _from_shortfall_claim(p: Person, q: "Question", name: str):
    """AN OPERAND READ OFF A HELD SHORTFALL CLAIM. Plan position `19d`, the retirement plan's G3:
    *"wiring the existing `transfer` verb's operands from a shortfall claim"*. The claim is
    `(rung, "shortfall:<kind>", units)`. MATTER records it on the write of a larder its draw ran
    dry with a mouth unfed, as `demanded - delivered` over the rung's subtree
    (`queries/world_q.py`), and WITNESS deposits it into those who saw that write. So a person
    asked about it knows WHICH matter the place lacks and HOW MUCH. This reads the two:
      * `kind`   -- the predicate's argument (`store_kind_of`'s own move, one stem over);
      * `amount` -- the claim's value, when it is a positive whole number of units.
    Both are read by `q.about` from `p`'s OWN ledger, never by the referent, on
    `_from_content_claim`'s precedent (§20, `AX-2`).

    ⚠ `to` IS NOT READ HERE. For a `claim_landed` question the referent IS the claim's subject, so
    the referent rule already binds `to` to the drained rung (`rosters.yaml:
    shortfall_sourced_operands`' note). ⚠ `from` IS NOT READ HERE EITHER. The giver gives from where
    they stand (`containing_rung_of`), for r2 §A.13's reason: a claim about somewhere else must not
    reach into a larder the actor is not standing in.

    ⚠ `None` IS SILENT BY DESIGN. It means no claim by `q.about` in `p`'s own ledger, a predicate
    that is not `shortfall:<kind>`, or an amount that is not a positive whole number, and the caller
    falls through to `store_kind_of`/the fixtures exactly as before. A drifted retelling (`15b`'s
    `_told_value`) stays positive by construction: it preserves sign and never crosses zero. So a
    rumour can misstate how short a place is, and it can never turn the shortfall into a surplus.

    REJECTED SHAPES, each for a reason:
      * A `content:` WRIT CARRYING `kind`/`amount` (`15c`'s reader, a new record kind). The writ is
        a document someone ISSUES. Here nobody asks: the larder ran dry and a witness saw it.
        Minting a document for a fact nobody authored is the automatic promotion S36.1 forbids
        (probe `F19`'s law).
      * THE `stores:<kind>` OBSERVATION `store_kind_of` already reads. That is a store LEVEL. A
        level is not a lack: a larder at 30 is plenty for three mouths and a famine for thirty, and
        a person cannot know the mouths (`demanded` is a world read).
      * THE PER-PERSON SHORTFALL, as witnessed through item 3b's `body.changed`.
        (`World._subsistence_shortfall` is census-only and is no claim at all.) That claim is about
        a PERSON, so its referent is no rung and a transfer to it refuses (`_eff_transfer`: no
        rung, no transfer). It carries no kind or amount either (`value` is `True`). It is also the
        per-person scale `ED-IN-0255` ruled away from: *"i don't think having lords and guild
        members etc worry about subsistence is worthwhile"*, *"it's a territorial issue"*."""
    if q is None or not q.about:
        return None
    c = _claim_by_id(p, q.about)
    if c is None:
        return None
    stem, sep, kind = str(c.predicate).partition(":")
    if not sep or not kind or stem != SHORTFALL_PREDICATE:
        return None
    if name == "kind":
        return kind
    if name == "amount":
        v = c.value
        ok = isinstance(v, int) and not isinstance(v, bool) and v > 0
        return v if ok else None
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

    ⚠ POSITION `15c` ADDS A FOURTH READING, CHECKED FIRST FOR THREE OF THE EIGHT NAMES: AN OPERAND
    THE PERSON'S OWN HELD WRIT ANSWERS BINDS THE WRIT, not the referent and not the fixture.
    `to`/`kind`/`amount` -- the three of `transfer`'s own operands not already `from` (r2 §A.13:
    *"the executor's act is `transfer`, whose operands -- `from`, `to`, `kind`, `amount` -- are
    all in the closed eight"*) -- ask `_from_content_claim` first. `from` is DELIBERATELY EXCLUDED
    from this check: r2's own ruling keeps *where you are* off the writ (*"a writ that could name
    `from` would let a Duke's document reach into a larder the executor is not standing in"*), so
    it stays on `containing_rung_of` alone, below. `at` -- the writ's OWN place of discharge -- is
    also excluded here, and DELIBERATELY: `at` is not (and r2 rules it must not become, *"I do not
    coin a ninth operand"*) a member of `requires_operands`, so no typed cell can ever ask
    `operands_for` for it and `_derive_operand` is never called with `name == "at"` at all -- a
    branch here would be dead code no test could reach (`ID-13`). `13f`/`19`/`19b`/`found` are
    where a NEW verb cell earns `at` a roster place, if one ever needs to bind it directly; this
    position supplies the READER those positions build on, not the roster edit.

    ⚠ POSITION `19d` ADDS A FIFTH SOURCE, FOR TWO NAMES: `kind` and `amount` are read off a held
    SHORTFALL claim (`_from_shortfall_claim`), ahead of `store_kind_of` and the fixtures. `to` is
    not among them, because a shortfall claim's subject already IS the question's referent.

    ⚠ S5 (round-1 `01_THE_BUILD_ORDER.md`, row S5): this widening adds no fifth carrier.
    `beneficiary_kinds` (`rosters.yaml`) stays four members (`actor, subject, to, none`) --
    CAT-2 closed the beneficiary as a STATIC verb-table column resolving to a carrier the
    Candidate already holds, never a new operand name, so `benefits_me(c)` inherits nothing new
    to read from this branch.

    ⚠ THE REFERENT IS WORLD-SOURCED, AND THAT IS §F1'S OWN SHAPE RATHER THAN A WIDENING OF IT.
    Raised by the `W-C` adversarial pass and closed here rather than escalated, because it is
    answered: one of the two question sources reads the world directly (`questions_for` Q4 `need`
    from `w.propositions`); Q2 `claim_landed` is ledger-sourced -- `for c in p.ledger`, unchanged --
    but ADMITTED through `reach`/`place_of` (`queries/world_q.py`, position `11a`), which read
    world state (`w.tenures`, `w.offices`, `w.rungs`) to decide whether the person may be ASKED
    about a claim their own ledger already holds. ⚠ `date_due` and `band_crossed` -- the two other
    world-reading sources this paragraph used to name -- were folded out at `11a`: both MEASURED
    zero questions in every buildable world, and both fold into `claim_landed` rather than into a
    third route. `W-C` promotes that referent from *which Candidate forms* to *an operand of the
    minted act*. §F1 states the derivation in terms -- `subject ∈ referents(q)`, "what the
    question is ABOUT" -- and puts the epistemic constraint in a DIFFERENT clause: `requires(verb)
    not KNOWN-false FROM p's OWN CLAIMS`, with its own warning that softening THAT clause is the
    breach. So the belief filter is on the requirement, never on the referent; and `to`/`site` are
    the referent under the two other names the closed operand vocabulary has for it, not a second
    channel.
    Two things make the promotion safe rather than merely licensed, and both are properties of
    code above rather than of this paragraph. (a) EVERY SOURCE IS ADDRESSED TO THE PERSON: Q2
    reads their own ledger, filtered by `reach(w, p)` -- never another person's, and never widening
    who WITNESSED (`01` §A.4.4) -- and Q4 is their own live `commit`. A person cannot be handed a
    referent they have no reach to. (b) THE REFERENT PROPOSES AND THE FOLD DISPOSES: naming a
    receiver is not moving matter to it. `_eff_transfer` returns nothing when a
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
    # THE WRIT ANSWERS FIRST, for the names `rosters.yaml: writ_sourced_operands` declares (see
    # this function's own docstring for why `from`/`at` are not among them). A person naming no
    # writ at all, or one whose kind has no such key, falls straight through to the referent/
    # fixture below -- `_from_content_claim` returning `None` is silent by design, not a special
    # case of this one. BATCH-CLOSE FINDING (methodology-close Phase 1, CODE ARCHITECTURE lens):
    # this was a literal `("to", "kind", "amount")` tuple, caught by
    # `test_jordan_no_definition_is_hardcoded_in_a_body` -- moved to the roster rather than
    # exempted, since it names a real design fact (which operand names a writ may answer) with a
    # cited source, not a mechanism.
    if name in WRIT_SOURCED_OPERANDS:
        v = _from_content_claim(p, q, name)
        if v is not None:
            return v
    # AND A HELD SHORTFALL CLAIM ANSWERS NEXT (plan position `19d`), for the names
    # `rosters.yaml: shortfall_sourced_operands` declares (`kind`, `amount`). A question has one
    # `about`, and a claim is either a writ's or a shortfall's, never both, so the two readers
    # never compete for one operand and their order does not matter. Both come before
    # `store_kind_of` and the fixtures: a claim that NAMES the matter and the quantity outranks
    # a default that names neither.
    if name in SHORTFALL_SOURCED_OPERANDS:
        v = _from_shortfall_claim(p, q, name)
        if v is not None:
            return v
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
    parameter was a `TypedRequires`. A signature is where that gets fixed, not a sentence.

    ⚠ TELLING WORKPLAN `T4`: THE FIRST OF `operand_bags`, for the callers that ask for one bag. A
    row whose `to` is a known person has one bag per person known; this answers the first, or
    `None` for none."""
    bags = operand_bags(p, row, q, subject, fx)
    return bags[0] if bags else None


def operand_bags(p: Person, row: "VerbRow", q: "Question", subject,
                 fx: "Fixtures") -> list[dict]:
    """EVERY OPERAND BAG `p` CAN FORM FOR `row` ON `subject` -- `[]` when none (telling workplan
    `T4`, `ED-IN-0282`). One bag for every row whose operands all come from `_derive_operand`
    (`operands_for`'s rule, unchanged); for a row whose cell binds a known-person operand beside
    `subject` (`TypedRequires.known_person_operands`: `tell`'s `to`, and since plan position `14`
    `give`'s -- `petition` and `issue` bind `to` without `subject`, so `to` is what they are about
    and keeps the referent rule in `_derive_operand`), one bag PER PERSON `p` KNOWS (`queries/person_q.py::known_persons`, from `p`'s own claims,
    never the actor and never the topic), in that function's sorted order. Nobody known is no bag:
    a telling to nobody is an act with a hole (`operands_for`'s `None`), traced and not formed.

    ⚠ PERSON-SIDE AND WORLD-FREE, like `operands_for` -- `p` first for the AST guard's reason
    recorded there. WHETHER the person told is present is the fold's `hearer` conjunct; a known
    person who is elsewhere still gets a Candidate. THE TELLER DOES NOT LEARN IT FROM THE REFUSAL: the
    `with` read is observed, never deposited (batch-2 close `F1`), and `news.untold` is one kind for
    both conjuncts, so a refused telling to an absent hearer is retried whenever the teller
    re-deliberates -- a scene tax with nothing behind it. Recorded, with the measurement owed, at
    the telling workplan's T4b *As built* line. `give` (plan position `14`) shares the shape: its
    receiver is a known person and its `with` conjunct the fold's."""
    fan = row.requires_typed.known_person_operands() if row.requires_typed is not None else ()
    if not fan:
        ops = _operands(p, row, q, subject, fx, {})
        return [] if ops is None else [ops]
    people = known_persons(p.ledger, p.id, subject)
    if not people:
        TRACE.note(f"{row.verb!r} needs {list(fan)} from a person {p.id} knows, and they know "
                   f"nobody but {subject!r}; NO Candidate is formed (T4)", "§F1/H-94")
        return []
    out = []
    for who in people:
        ops = _operands(p, row, q, subject, fx, {n: who for n in fan})
        if ops is not None:
            out.append(ops)
    return out


def _operands(p: Person, row: "VerbRow", q: "Question", subject, fx: "Fixtures",
              given: dict) -> Optional[dict]:
    """`operands_for`'s body: the cell's own operands plus `subject`/`to` where the form admits
    them, each from `given` if it names it (`operand_bags`' known person) else `_derive_operand`;
    `None` for a bound operand nobody can supply. The rules are `operands_for`'s docstring's."""
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
        v = given[name] if name in given else _derive_operand(p, name, q, subject, fx)
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
    agree, dis = _pair(told, own, lambda c: c.predicate, PERSON_PREDICATES)
    return agree, dis, agree + dis


def _pair(told: list[Claim], own: list[Claim], key: Callable[[Claim], Any],
          admit=None) -> tuple:
    """THE ONE PAIRING STEP: each `told` claim against `own`'s belief at the same `key`, `(agree, dis)`.

    `agreement` pairs by predicate on the `person_predicates` roster (`admit`); `record` pairs by
    `(subject, predicate)` over the cell predicates (`admit=None`, filtered by `record`). Both call
    this, so how a told claim is matched to what the hearer holds, and what counts as agreeing
    (`==`, whole-value), lives once.

    ⚠ THE MATE IS THE CLAIM `LedgerReader` CALLS THE BELIEF, NOT THE LAST ONE LISTED. Where `own`
    holds several claims at one `key`, the one paired against is `LedgerReader._best`'s -- most
    recent, then most confident -- because list order is the EVICTION sort (`state/ledgers.py`:
    `confidence x (when + 1)`), not an order of belief, and a second ladder here would score a
    truthful told claim against a belief the person no longer holds. (This replaced a dict
    comprehension in which the last-listed claim at a key silently won.) A tie goes to the first
    listed, as `_best` has it."""
    by_key: dict = {}
    for c in own:
        if admit is None or key(c) in admit:
            by_key.setdefault(key(c), []).append(c)
    belief: dict = {}                   # key -> the claim `LedgerReader` would answer from
    agree = dis = 0
    for c in told:
        k = key(c)
        if k not in by_key:
            continue                    # nothing of your own to compare it against
        if k not in belief:
            belief[k] = LedgerReader(by_key[k]).belief_among()
        mate = belief[k]
        (agree, dis) = (agree + 1, dis) if c.value == mate.value else (agree, dis + 1)
    return agree, dis


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


def _clamp(x: float, lo: float, hi: float) -> float:
    return lo if x < lo else hi if x > hi else x


def rank(p: Person, teller: str) -> int:
    """`+1` if `p`'s own claims say `teller` outranks `p`, `-1` if outranked, `0` if they say
    neither. ALWAYS `0` TODAY, AND THAT IS A MEASURED ABSENCE, NOT A STUB'S GUESS.

    The ordering itself exists -- `offices.yaml: titles` maps each title to a rung kind, and
    *"rank is the ordinal in `rung_kinds`"* -- but a hearer can only rank a teller off claims
    the HEARER holds, and no writer in the tree deposits an `office` claim (the `person_predicates`
    member is a vocabulary word with no producer; MEASURED, `build_realm(0)` one season: zero
    `office` claims in any ledger), nor is an `office` claim's value typed as a title or a seat.
    Comparing values nobody writes, in a shape nobody declared, would be inventing the ruling."""
    # ABSENT: H-181 rank ordering  (an `absent` hole row, read by harness/register.py; nothing reads this marker)
    return 0


def _is_cell(c: Claim) -> bool:
    """Is `c` a claim on a CELL -- a slot that holds one value (`data/requires.py: CELL_STEMS`)?"""
    return str(c.predicate).partition(":")[0] in CELL_STEMS


def record(p: Person, teller: str, fx: "Fixtures") -> float:
    """A TELLER'S RECORD WITH `p`: how often what `teller` told `p` matched what `p` holds firsthand
    (telling workplan `T6`, `ED-IN-0282`; E5).

        record = 1 + record_gain * (agree - dis) / (agree + dis)        agree + dis > 0
               = 1.0                                                    agree + dis == 0

    A PAIR is one claim of `p`'s own ledger whose `Claim.teller` is `teller`, against `p`'s own
    firsthand claim (empty chain, source `firsthand`) on the SAME `(subject, predicate)` cell: it
    agrees if the values are `==`, else it disagrees. The pairing step is `_pair`, the one
    `agreement` uses; only the key (a cell, not a predicate) and the roster differ. It reads
    `p.ledger` and nothing else, so another person's claims cannot move it (`p` never reads a
    ledger it does not hold).

    ⚠ ONLY CELL PREDICATES PAIR (`_is_cell`, `data/requires.py: CELL_STEMS`), BOTH SIDES. A `seen`
    claim is not a cell -- each sighting is a distinct `Seen` value, so a told sighting would
    "disagree" with the very sighting it reports -- and an event-kind claim (`news.told` ...) is
    always `True`, so any pair of them agrees for free. The firsthand claim paired against is the
    one `LedgerReader` reads as the belief AMONG FIRSTHAND CLAIMS (`_pair`). A claim stores no time of
    observation, so a told claim that has itself since replaced that belief is still scored against
    the older firsthand one (recorded at `H-183`).

    ⚠ ZERO PAIRS IS NEUTRAL, 1.0 -- DELIBERATELY NOT `standing_of`'s POLARITY. `standing_of` maps
    zero pairs to the MAXIMUM gap because there the thing measured is a flattering reading, and
    no evidence must not flatter. Here the thing measured is a stranger's reliability, and copying
    that polarity would read every teller `p` has never been able to check as maximally unreliable,
    halving their word (at the shipped gain) before they have said anything wrong. A teller with no
    record is exactly as credible as `told_weight` and `relation` make them.

    ⚠ A TELLER'S OWN CONTRADICTION IS A PAIR, SO IT LOWERS THEIR RECORD: the claim being weighed is
    one of the pairs. That is intended -- a teller who contradicts what `p` saw is, by that, less
    credited on the next cell -- and it is also why `record_gain` 0 (the control) is the only arm on
    which a told claim's weight is independent of the firsthand claims it contradicts."""
    gain = fx.get("record_gain")
    told = [c for c in p.ledger if c.teller == teller and _is_cell(c)]
    own = [c for c in p.ledger if not c.chain and c.source == "firsthand" and _is_cell(c)]
    agree, dis = _pair(told, own, lambda c: (c.subject, c.predicate))
    # ABSENT: H-191 intent reconciliation  (an `absent` hole row, read by harness/register.py; nothing reads this marker)
    if agree + dis == 0:
        return 1.0
    return 1.0 + gain * (agree - dis) / (agree + dis)


def teller_weight(p: Person, fx: "Fixtures") -> Callable[[Claim], float]:
    """THE `weigh` CLOSURE `LedgerReader` RANKS `p`'S CLAIMS BY (telling workplan `T3a`,
    `ED-IN-0282`; the reader `H-157` recorded as missing for `Claim.teller`).

        weigh(c) = 1.0                                       if c.chain is empty
                 = clamp01(told_weight ** hops * relation * record)   otherwise
        hops     = len(c.chain)         teller = c.chain[-1]           (origin = c.chain[0])
        relation = 1 + rank_gain * rank(p, teller)
                     + regard_gain * clamp(regard(p, teller) / STANCE_MAX, -1, 1)
        record   = `record(p, teller, fx)`: 1.0 with no pair; else 1 + record_gain * balance (`T6`)

    `RULINGS.yaml` CAT-3, closed: store the teller and grade the claim WHEN READ, by the hearer's
    belief about their relation to the teller -- so a revised regard re-grades every claim that
    teller ever passed on, and nothing is frozen at deposit. `hops` is read off `Claim.chain` (`T3b`):
    a retelling is a longer chain, so it weighs `told_weight` less again, and the `relation` is the
    hearer's to the one who told THEM, the last hop. A claim with an empty chain -- firsthand,
    seen, inferred, or a `told_by` deposit through a channel with no speaking actor -- weighs 1.0.

    ⚠ THE FIXTURES ARE READ ON THE FIRST TOLD CLAIM, NOT AT BUILD. A ledger with no teller in it
    reads none of them, so a world with no telling reads exactly what it read before `T3a`.
    ⚠ AT THE CONTROL VALUES (`told_weight` 1.0, `rank_gain`, `regard_gain` and `record_gain` all
    0) EVERY CLAIM WEIGHS EXACTLY 1.0 and `LedgerReader` orders as it did before `T3a`.
    ⚠ THE ONE-HOP BOUND. `told_weight` x `relation` x `record` is clamped at 1.0, and a one-hop claim
    at the shipped 0.5 stays strictly below a firsthand claim's 1.0 only while `relation` x `record`
    stays below 2. At NEUTRAL regard a good record ALONE gives 0.5 x 1 x 1.5 = 0.75 (< 1); 1.0 needs
    `relation` x `record` >= 2, i.e. at the best record (1.5) `relation` >= 4/3 -- regard >= 2/3 of
    `STANCE_MAX` at the shipped `regard_gain`. A regarded teller whose earlier hearsay was confirmed
    can therefore tie a firsthand claim on support and win on `when`; `rank` reads 0 (`H-181`) so it
    adds nothing yet. `record` is not independent of what it weighs: see `record`'s last warning.
    ⚠ `relation` AND `record` EACH DEPEND ON THE TELLER ALONE AND ON `p`'s LEDGER, WHICH DOES NOT
    CHANGE INSIDE ONE `opening_set`, so each is computed ONCE PER TELLER."""
    gains: list = []
    relation_of: dict = {}      # `relation` depends on the teller alone: one stance scan per teller
    record_of: dict = {}        # `record` too: one ledger scan per teller

    def weigh(c: Claim) -> float:
        if not c.chain:
            return 1.0
        teller = c.teller
        if not gains:
            gains.extend((fx.get("told_weight"), fx.get("rank_gain"), fx.get("regard_gain")))
        told_weight, rank_gain, regard_gain = gains
        relation = relation_of.get(teller)
        if relation is None:
            relation = relation_of[teller] = (
                1.0
                + rank_gain * rank(p, teller)
                + regard_gain * _clamp(regard(p, teller) / STANCE_MAX, -1.0, 1.0))
        # ABSENT: H-180 stake  (an `absent` hole row, read by harness/register.py; nothing reads this marker)
        rec = record_of.get(teller)
        if rec is None:
            rec = record_of[teller] = record(p, teller, fx)
        return _clamp(told_weight ** c.hops * relation * rec, 0.0, 1.0)

    return weigh
