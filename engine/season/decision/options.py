"""`decision/` -- the `opening_set` member of `04_CODE_ARCHITECTURE.md` §A.2:133, and its helpers.

⚠ **THE FILE IS `options.py` AND THE MEMBER IS `opening_set`, DELIBERATELY.** §A.2:133 names four
members; a module named `opening_set.py` beside a function named `opening_set` makes
`decision.opening_set` ambiguous -- `__init__.py`'s re-export shadows the submodule -- and the
rebind surface needs the MODULE by name. "Option set" is the tree's own existing phrase for what
this returns, so the filename is idiomatic rather than coined (`CLAUDE.md` §4).

`opening_set` and its operand machinery (`operands_for`, `_derive_operand`, `_REFERENT_OPERANDS`,
`containing_rung_of`, `store_kind_of`), the eligibility predicate, and the two agreement/standing
readers.

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

from typing import Optional
from ..data.rosters import PERSON_PREDICATES
from ..data.verbs import ELIGIBILITY_KINDS, VERB_TABLE
from ..epistemic import belief_contradicts
from ..gaps import Forbidden
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
