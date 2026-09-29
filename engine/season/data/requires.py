"""`season.data.requires` -- the `requires` grammar, extracted from `shape.py` (step 3 of the
decomposition, a PURE MOVE: no behaviour changed, only where the code lives).

Owns the requirement grammar in full: the third truth value (`_Unknown`/`UNKNOWN`), the read
carrier (`Observation`) and its verdict (`Verdict`), the five typed forms `@requirement_form`
registers (`Existence`, `ScalarThreshold`, `ContainPath`, `Relation`, `OwnLedger`), the
conjunction `AllOf` and the cell wrapper `TypedRequires`, the one evaluator (`evaluate`) and the
one binding constructor pair (`binding_of`/`binding_from_act`), and the loader
(`_build_clause`/`build_typed_requires`) that turns a `verb_table.yaml` cell into a `Requirement`.

`04_CODE_ARCHITECTURE.md` §F.24a: *"`F.24` said 'assumed: a small typed predicate grammar' and
supplied none... The 32 `requires` cells in the executable chain are the specification, and
reading them yields SEVEN forms."* `rosters.yaml: requires_forms` is the closed roster of their
names -- a cell naming an eighth REFUSES AT LOAD.

⚠ `WorldReader` AND `LedgerReader` DO NOT LIVE HERE, DELIBERATELY. Adjudicated at the move: they
are READERS -- `queries/` territory at a later step -- and the grammar this module owns asks only
`reader.read(subject, predicate)` of whichever one a caller hands it, never anything about WHERE
the answer came from. Moving a reader in here would give the grammar an opinion about that, which
is exactly the coupling `WorldReader`'s own docstring argues against (the actor's-own-ledger
carve-out: *"the fold may ask the ACTOR'S OWN ledger ... and no other"*). `shape.py` still defines
both readers, and both import `UNKNOWN` back from here -- the one name a reader's `read()` needs
from the grammar it serves.

⚠ THE ORDERING CONSTRAINT THIS MODULE EXISTS TO SATISFY. `_build_clause` refuses any requirement
form `REQUIREMENT_TYPES` does not carry -- and `season.data.verbs._load_verb_table` calls it once
per row while loading `verb_table.yaml` -- so every `@requirement_form` decorator below MUST have
run, registering its class, before that loader executes. This is not a comment asking the next
session to get an order right: `season/data/verbs.py` imports from this module BEFORE it defines
`_load_verb_table`, and Python fully executes an imported module (top to bottom) before the
importing module's own subsequent top-level code runs -- so `season.data.verbs` cannot observe a
partially-registered grammar regardless of which of the two a caller imports first. Import order
replaces file position.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Optional

from ..gaps import Unspecified
from .rosters import RECORD_CONTENT, roster, roster_map

REQUIRES_FORMS = roster("requires_forms")
REQUIRES_OPERANDS = roster("requires_operands")
REQUIRES_FORM_NEEDS = roster_map("requires_forms", "needs")

def _check_writ_sourced_subset(writ_sourced: frozenset, operands: frozenset,
                               name: str = "writ_sourced_operands") -> None:
    """Plan position `15c`. `writ_sourced` is a SUBSET of `operands`, never a second vocabulary --
    refused if it names anything the closed operand roster does not, the same discipline
    `record_kinds` and `tenure_kinds` are cross-validated against each other by in
    `data/rosters.py`. Factored into a function -- BATCH-CLOSE FINDING, methodology-close Phase 1
    antagonist -- so a test can call it with a planted mismatch rather than only exercising the
    branch that never fires on today's data (§0.1 pt 3: a refusal that nothing can observe fail).
    `name` is the claim-sourced roster being checked: `writ_sourced_operands` since `15c`, and
    `shortfall_sourced_operands` since `19d` uses the same rule rather than a second copy of it."""
    if not writ_sourced <= operands:
        raise Unspecified(
            f"rosters.yaml: {name} names {sorted(writ_sourced - operands)}, "
            "not in requires_operands",
            f"rosters.yaml -- {name}",
            needs=f"every {name} member to also be a requires_operands member",
            law="a claim answers FOR an existing operand name; it does not coin a new one")


WRIT_SOURCED_OPERANDS = roster("writ_sourced_operands")
_check_writ_sourced_subset(frozenset(WRIT_SOURCED_OPERANDS), frozenset(REQUIRES_OPERANDS))
# Plan position `19d`. The operand names a SHORTFALL claim answers (`kind`, `amount`), and the
# predicate stem it is recorded under: `(rung, "<stem>:<kind>", units)`. MATTER writes the claim
# (`loop/matter.py`) and `decision/options.py::_from_shortfall_claim` reads it, so the stem
# lives here once and neither side spells it. The stem's collision checks (it may be neither a
# `requires` stem nor the content stem) sit below `REQUIRES_STEMS`, which they need.
SHORTFALL_SOURCED_OPERANDS = roster("shortfall_sourced_operands")
_check_writ_sourced_subset(frozenset(SHORTFALL_SOURCED_OPERANDS), frozenset(REQUIRES_OPERANDS),
                           "shortfall_sourced_operands")
SHORTFALL_PREDICATE = roster_map("shortfall_sourced_operands", "claim").get("predicate")

class _Unknown:
    """THE THIRD TRUTH VALUE, AND IT IS NOT `False`.

    An operand the binding does not supply, or a question the reader cannot answer, is UNKNOWN --
    *nobody knows*, which is a different fact from *it is false*. The distinction is the whole of
    §F1 clause 4: `opening_set` drops a Candidate only on a KNOWN-FALSE requirement, and *"absence
    of a belief is not a belief in the negative"*. Collapse UNKNOWN into False here and every
    person stops forming every candidate whose requirement they happen to hold no claim about.

    ⚠ IT IS FALSY, AND DELIBERATELY SO. The FOLD's polarity is §42.2's -- zero evidence goes to
    the verdict AGAINST the thing measured -- so an unevaluable precondition must REFUSE. Callers
    still test `is True` / `is False` rather than truthiness, because the two readings differ; the
    falsy `__bool__` is the safe default for a caller that forgets."""
    __slots__ = ()

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "UNKNOWN"

UNKNOWN = _Unknown()

@dataclass(frozen=True)
class Observation:
    """ONE READ, RECORDED. `(subject, predicate, value)` -- the same triple a `Claim` carries,
    which is not a coincidence: an Observation is what a Claim would be if the reader wrote one.

    ⚠ THE PREDICATE IS DERIVED FROM THE FORM, NEVER LOOKED UP IN A ROSTER. `f"stores:{kind}"`,
    `"condition"`, `f"contain.path:{to}"` -- the string falls out of the cell's own fields, so a
    verb cannot acquire a predicate nobody can produce, and the write side has a name to aim at."""
    subject: Any
    predicate: str
    value: Any

@dataclass(frozen=True)
class Verdict:
    """`True | False | UNKNOWN`, plus every read that produced it.

    `observed` is kept here AND is attached to every Event the act emits -- that is `W-B`
    (`H-122`), landed 2026-09-04. `W-A` refused to attach it because *"building the carrier before
    its reader exists is the dead-carrier defect `ID-13` refuses"*; the reader is
    `belief_contradicts`, which evaluates the SAME cell against `LedgerReader`, so the refusal is
    DISCHARGED rather than overridden and no second evaluator exists (§27.2). ⚠ THIS DOCSTRING
    SAID THE OPPOSITE UNTIL THE `W-B` ADVERSARIAL PASS READ IT: it still described attaching the
    field as the defect, in the file that had just attached it. A comment asserting the absence of
    a field the class above it carries is the *doctrine asserting an enforcement that does not
    exist* failure, one seam over."""
    value: Any
    observed: tuple = ()
    # ⚠ PLAN POSITION `19` -- WHICH NAMED CONJUNCT DECIDED A VERDICT THAT IS NOT `True`: the first
    # clause that read False, else the first that read UNKNOWN (`AllOf`'s own precedence: FALSE
    # dominates UNKNOWN). `None` for a True verdict, an unnamed clause, or a cell with no names --
    # every row before `19`. It is `04 §C.4`'s `(ok, failed_conjunct) = eval(row.requires, ...)`,
    # the second half of that tuple, and the fold reads it as `row.refusal_for(failed_conjunct)`
    # (`loop/resolve.py::_admits`). It is NOT on the Event: which conjunct refused is carried by the
    # refusal KIND the row keys to it, and `observed` already carries the reads.
    failed: Optional[str] = None

def _as_number(v):
    """A read coerced to a number, or UNKNOWN. A string is UNKNOWN rather than an error: a ledger
    claim may carry anything, and a comparison against a word is a question nobody can answer."""
    if v is UNKNOWN or v is None or isinstance(v, str):
        return UNKNOWN
    try:
        return float(v)
    except (TypeError, ValueError):
        return UNKNOWN

def _bound(binding: dict, name: str):
    return binding.get(name, UNKNOWN) if binding.get(name, UNKNOWN) is not None else UNKNOWN

COMPARATORS = {">=": lambda a, b: a >= b, "<=": lambda a, b: a <= b}

# THE SEAT AN ACT EXERCISES, AS A BINDING KEY (plan position `19`). Structural like `actor` -- the
# Act carries it (`Act.via`), the payload never does -- so it is NOT a `requires_operands` member and
# `binding_of` adds it beside the actor. One spelling for the writer (`binding_of`) and the one
# reader (`Basis.check`).
VIA = "via"

REQUIREMENT_TYPES: dict = {}

def requirement_form(name: str):
    """Bind a form NAME from `rosters.yaml` to the class that evaluates it. The roster is the
    closed grammar; this is the implementation, and a name in one and not the other raises."""
    def deco(cls):
        if name not in REQUIRES_FORMS:
            raise SystemExit(f"{name!r} is not in rosters.yaml's requires_forms roster")
        REQUIREMENT_TYPES[name] = cls
        # ⚠ THE FORM'S NAME, ON THE CLASS. `rosters.yaml` gives each form a `needs:` -- the closed
        # set of operands a cell OF THAT FORM MAY reference -- and `operands_for` reads it to
        # decide which operands a Candidate carries BEYOND the ones its own cell binds. Without
        # this the mapping would have to be re-derived by scanning `REQUIREMENT_TYPES` backwards,
        # which is the same declaration written twice.
        cls._form = name
        return cls
    return deco

class Requirement:
    # The form's name, stamped by `@requirement_form`. `AllOf` has none -- a conjunction is not a
    # form (`rosters.yaml`: "CONJUNCTION IS NOT AN EIGHTH FORM") -- and unions its clauses'.
    _form = ""

    def needs(self) -> frozenset:
        """The operand names a cell OF THIS FORM MAY reference -- `rosters.yaml`'s `needs:`.

        Wider than `operands()`, which is what THIS cell actually binds. The gap between them is
        where `operands_for` looks for the operands an act needs and its precondition does not:
        `transfer`'s cell binds one rung (`from`) and §E3 gives it TWO `Rung.stores` writes."""
        return frozenset(REQUIRES_FORM_NEEDS.get(self._form) or ())

    # ⚠ EVERY FORM DECLARES THE STEMS IT ASKS FOR, so `_build_clause` can close the predicate
    # vocabulary at LOAD without a second list to keep in step (§8). A form that reads a stem it
    # does not declare here would pass the load check and still read UNKNOWN forever -- so the
    # rule is: whatever `check()` passes to `_observe`, `stems()` names.
    def stems(self) -> tuple:
        return ()

    """One clause of a typed `requires:`. Subclasses ARE the seven forms; `evaluate` never
    branches on a form name, because the class IS the branch (`G2` -- forbid the shape, never
    enumerate the words)."""

    def operands(self) -> tuple:
        """Every operand name this clause reads. Checked at load against the form's `needs:`."""
        return ()

    def entity_operands(self) -> tuple:
        """The operand naming THE THING THE REQUIREMENT IS ABOUT -- what a Candidate's `subject`
        can bind, and nothing else. A Candidate is `(verb, subject, why)` and carries exactly one
        entity (`H-94`/`H-80`), so this is the only operand the person's reading can supply."""
        return ()

    def check(self, reader, binding: dict, observed: list):
        raise NotImplementedError

@requirement_form("existence")
@dataclass(frozen=True)
class Existence(Requirement):
    """§F.24a form 1 -- *existence over an edge kind*, read to cover an OBJECT of a named class
    as well. The widening is argued in `rosters.yaml: requires_forms`, and it is what makes
    §F.24a's own "closes 30 of 32 cells" true of `carry`, `commit` and `dispatch`."""
    of: str
    kind: str

    def operands(self) -> tuple:
        return (self.of,)

    def entity_operands(self) -> tuple:
        return (self.of,)


    def stems(self) -> tuple:
        return ("exists",)

    def check(self, reader, binding, observed):
        subj = _bound(binding, self.of)
        if subj is UNKNOWN:
            return UNKNOWN
        n = _as_number(_observe(reader, subj, f"exists:{self.kind}", observed))
        return UNKNOWN if n is UNKNOWN else n >= 1

@requirement_form("scalar_threshold")
@dataclass(frozen=True)
class ScalarThreshold(Requirement):
    """§F.24a form 2 -- *a computed scalar against a threshold*. `transfer`'s
    `stores(hearth(giver), kind) >= amount` and `work`'s `condition >= floor(verb)`.

    The threshold is EITHER an operand (`transfer`'s `amount`) or a SECOND READ on the same
    entity (`work`'s `floor`, which is `band_floors[site.kind]`'s minimum and lives in Fixtures,
    `H-08`). Exactly one, checked at load: a cell with both states two thresholds and a cell with
    neither states none."""
    of: str
    scalar: str
    comparator: str = ">="
    key: str = ""
    threshold: str = ""
    threshold_predicate: str = ""

    def __post_init__(self) -> None:
        if bool(self.threshold) == bool(self.threshold_predicate):
            raise SystemExit(
                f"a `scalar_threshold` cell needs exactly one of `threshold:` (an operand) and "
                f"`threshold_predicate:` (a second read); got {self.threshold!r} / "
                f"{self.threshold_predicate!r}")
        if self.comparator not in COMPARATORS:
            raise SystemExit(
                f"comparator {self.comparator!r} is not one of {sorted(COMPARATORS)}. §12.1's "
                "floor is inclusive; a strict comparator is a change to what a precondition can "
                "say and needs a ruling, not a table edit")

    def operands(self) -> tuple:
        return tuple(x for x in (self.of, self.key, self.threshold) if x)

    def entity_operands(self) -> tuple:
        return (self.of,)


    def stems(self) -> tuple:
        return (self.scalar, self.threshold_predicate) if self.threshold_predicate else (self.scalar,)

    def check(self, reader, binding, observed):
        subj = _bound(binding, self.of)
        if subj is UNKNOWN:
            return UNKNOWN
        pred = self.scalar
        if self.key:
            k = _bound(binding, self.key)
            if k is UNKNOWN:
                return UNKNOWN
            pred = f"{self.scalar}:{k}"
        lhs = _as_number(_observe(reader, subj, pred, observed))
        if lhs is UNKNOWN:
            return UNKNOWN
        rhs = (_as_number(_observe(reader, subj, self.threshold_predicate, observed))
               if self.threshold_predicate else _as_number(_bound(binding, self.threshold)))
        if rhs is UNKNOWN:
            return UNKNOWN
        return bool(COMPARATORS[self.comparator](lhs, rhs))

@requirement_form("contain_path")
@dataclass(frozen=True)
class ContainPath(Requirement):
    """§F.24a form 3 -- *path existence in the containment tree*. `move`'s whole cell (§E3 `:408`).

    ⚠ THE ENTITY IS THE DESTINATION, NOT THE ORIGIN. The origin is the actor and is bound from the
    act; a Candidate's `subject` names WHERE, which is the operand a person could hold a belief
    about (*there is no road from here to there*)."""
    of: str
    to: str

    def operands(self) -> tuple:
        return (self.of, self.to)

    def entity_operands(self) -> tuple:
        return (self.to,)


    def stems(self) -> tuple:
        return ("contain.path",)

    def check(self, reader, binding, observed):
        origin, dest = _bound(binding, self.of), _bound(binding, self.to)
        if origin is UNKNOWN or dest is UNKNOWN:
            return UNKNOWN
        v = _observe(reader, origin, f"contain.path:{dest}", observed)
        return UNKNOWN if v is UNKNOWN else bool(v)

@requirement_form("relation")
@dataclass(frozen=True)
class Relation(Requirement):
    """§F.24a form 5 -- *a relation between actor and subject*. `succeed`'s *the actor holds the
    office or estate whose heir is being designated*, and `restore`'s *the actor is present at
    it*. The relation NAME is the cell's; a relation the reader cannot answer is UNKNOWN, so an
    unimplemented one refuses rather than admitting."""
    of: str
    relation: str

    def operands(self) -> tuple:
        return (self.of, "actor")

    def entity_operands(self) -> tuple:
        return (self.of,)


    def stems(self) -> tuple:
        return (self.relation,)

    def check(self, reader, binding, observed):
        subj, actor = _bound(binding, self.of), _bound(binding, "actor")
        if subj is UNKNOWN or actor is UNKNOWN:
            return UNKNOWN
        v = _observe(reader, subj, f"{self.relation}:{actor}", observed)
        return UNKNOWN if v is UNKNOWN else bool(v)

@requirement_form("own_ledger")
@dataclass(frozen=True)
class OwnLedger(Requirement):
    """§F.24a form 6 -- *membership in the ACTOR'S OWN ledger*, and the form the cross-read missed.

    `tell`'s *the teller holds a claim on the subject* (§E3 `:417`). §B.2's corrected row (`F8`):
    *"the fold may ask the ACTOR'S OWN ledger ... and no other."* That carve-out is what licenses
    a resolver-side clause to read a ledger at all, and `WorldReader` makes it structural rather
    than promised -- it is constructed with one actor and can name no other person's claims.

    ⚠ IT READS WHETHER THE CLAIM IS HELD, NEVER WHETHER IT IS TRUE, which is the whole of `T3`.
    A liar and a mistaken witness both pass it, and the distortion lands at the receiver's
    WITNESS deposit -- `_req_tell`'s own docstring said so and this preserves it exactly."""
    of: str

    def operands(self) -> tuple:
        return (self.of,)

    def entity_operands(self) -> tuple:
        return (self.of,)


    def stems(self) -> tuple:
        return ("claim.held",)

    def check(self, reader, binding, observed):
        subj = _bound(binding, self.of)
        if subj is UNKNOWN:
            return UNKNOWN
        v = _observe(reader, subj, "claim.held", observed)
        return UNKNOWN if v is UNKNOWN else bool(v)

@requirement_form("basis")
@dataclass(frozen=True)
class Basis(Requirement):
    """§F.24a form 7 -- *a basis lookup on the exercised seat* (`04_CODE_ARCHITECTURE.md:1144`),
    IMPLEMENTED AT PLAN POSITION `19` (U7-remit). The form was in the closed roster from the start
    (`rosters.yaml: requires_forms`, `needs: [subject, from, to]`) with no class behind it, because
    its only live cells -- `confer`'s and `revoke`'s -- stayed on `REQUIRES_PREDICATES`; `_build_clause`
    refused any cell naming it (*"IN the grammar and has no implementation"*). So this is the
    grammar's own seventh form given its body, NOT a widening: no form, no operand and no combinator is
    added. What `19` adds to the vocabulary is two STEMS, below.

    WHY IT IS THE FORM `19` NEEDED. The plan's `19` gives four remit verbs *"a predicate reading
    `via.scope`"*, and three of them (`levy`, `issue`, `determine`) also need OPERANDS a computed act
    can carry -- `kind`/`amount`, the executor `to` -- which only a TYPED cell earns
    (`decision/options.py::operands_for` returns `{}` for an untyped row). A predicate beside a
    typed cell is two owners of one cell (`test_wa_one_owner_...`, `give`'s and `oblige`'s notes),
    so without this form the choice was *operands or the seat, never both* -- and `transfer`'s own
    form-2 cell, which the plan names for `levy`, could not be written at all.

    THE SEAT IS STRUCTURAL, NOT AN OPERAND -- the correction `04_VERBS.md`'s own determine row
    records (⑵: *"the conjunct binds `subject`; the actor is the acting person by construction and
    needs no operand"*). `Act.via` is to the binding what `Act.actor` is: carried by the Act itself,
    never by the payload, and put into the binding by `binding_of`'s `via=` (`04:120` AX-1, *"a seat
    enters through `Act.via`"*). `via` is NOT a `requires_operands` member and this form does not
    make it one -- coining it would be *"filling `H-94` by keyword argument"*. An act exercising NO
    seat binds no `via`, and the clause is UNKNOWN, which the fold refuses (§42.2): that is the
    plan's own falsifier for `19`, *"any of the five executing with `via=None`"*, made structural.

    THE PREDICATE CARRIES THE SEAT: `f"{basis}:{via}"`, the way `Relation` carries the actor
    (`held_by:<actor>`). So an Observation of it -- deposited at WITNESS like any other read (`W-B`)
    -- is an ABSOLUTE fact about one seat and one subject (*`off_duke`'s purview does not reach
    `R`*), never a seat-relative one a later reader would misapply to a different seat.

    `basis:` NAMES WHICH SEAT RULE IS ASKED, and the rule is the WRITE GATE'S OWN, never a copy
    (`state/gate.py` -- `_req_confer`/`may_fill`'s one-owner shape): `purview` is ruling (4),
    `purview_reaches` over the subject's place (`04:330`'s *"purview is asked of the seat exercised,
    never the actor"*); `bench` is `may_determine`, the `determination` basis's own predicate. Each is
    a `REQUIRES_STEMS` member, so a misspelt rule refuses at load rather than reading UNKNOWN forever.

    ⚠ OCCUPANCY IS ELIGIBILITY'S, NOT THIS FORM'S -- except where the gate's own predicate asks it.
    `purview` reads the seat's authority only; that the actor SITS in `via` is `_eligible`'s `remit:`
    branch (`seat_hold`), which every row using this form admits through. `levy`'s second
    alternative, `presence:<rung>`, declines unconditionally today (`H-75`); the day it admits, a
    `purview` read would have to ask `seat_hold` too, and this sentence is where that is written.
    `bench` does ask it, because `may_determine` is the gate's whole test and is taken whole.

    ⚠ PERSON-SIDE the seat is the one `decision/options.py::exercised_seat` names, passed to the same
    `binding_of` (`epistemic.belief_contradicts`), so §F1 clause 4 asks the cell the fold asks: a
    person who has watched `off_duke`'s levy of `R` refused holds `(R, purview:off_duke, False)` and
    stops forming it -- a belief, not a world read (`LedgerReader`)."""
    of: str
    basis: str

    def operands(self) -> tuple:
        return (self.of,)

    def entity_operands(self) -> tuple:
        return (self.of,)

    def stems(self) -> tuple:
        return (self.basis,)

    def check(self, reader, binding, observed):
        subj, seat = _bound(binding, self.of), _bound(binding, VIA)
        if subj is UNKNOWN or seat is UNKNOWN:
            return UNKNOWN
        v = _observe(reader, subj, f"{self.basis}:{seat}", observed)
        return UNKNOWN if v is UNKNOWN else bool(v)

@dataclass(frozen=True)
class AllOf(Requirement):
    """CONJUNCTION, AND IT IS NOT AN EIGHTH FORM. `restore`'s cell is *the site exists AND the
    actor is present at it*; `confer`'s and `revoke`'s carry an `and` too. §F.24a enumerated the
    ATOMS -- the `and` was already in the cells it read.

    ⚠ THREE-VALUED, AND FALSE DOMINATES UNKNOWN. One known-false conjunct makes the conjunction
    known-false even if a sibling is unreadable, which is what lets §F1 clause 4 fire on a person
    who knows one half of a requirement fails. Collapsing to UNKNOWN there would drop the
    contradiction, which is the under-refusal `G4` weighs equally with an invention."""
    clauses: tuple

    def operands(self) -> tuple:
        return tuple(dict.fromkeys(o for c in self.clauses for o in c.operands()))

    def entity_operands(self) -> tuple:
        return tuple(dict.fromkeys(o for c in self.clauses for o in c.entity_operands()))

    def needs(self) -> frozenset:
        return frozenset().union(*(c.needs() for c in self.clauses)) if self.clauses else frozenset()

    def stems(self) -> tuple:
        return tuple(x for c in self.clauses for x in c.stems())

    def check(self, reader, binding, observed):
        return self.decide(reader, binding, observed)[0]

    def decide(self, reader, binding, observed) -> tuple:
        """`(value, index)` -- `check`'s verdict and the position of the clause that DECIDED it:
        the first False, else the first UNKNOWN, else `None` (True). Plan position `19`: the
        per-conjunct half of `04 §B.13` invariant 4 needs to know WHICH conjunct refused, and this
        is `check`'s own loop returning what it already knew -- one body, so the reads, their order
        and the short-circuit on False are exactly `check`'s (a second loop could observe
        differently and move every Event's `observed`)."""
        unknown_at = None
        for i, c in enumerate(self.clauses):
            r = c.check(reader, binding, observed)
            if r is False:
                return False, i
            if r is UNKNOWN and unknown_at is None:
                unknown_at = i
        return (True, None) if unknown_at is None else (UNKNOWN, unknown_at)

@dataclass(frozen=True)
class TypedRequires:
    """ONE `requires_typed:` CELL -- the clause tree, and nothing else.

    ⚠ `operand_defaults` WAS A FIELD HERE AND `W-C` DELETED IT, WHICH IS THE ONE-OWNER HALF OF
    `H-94`. It held `transfer`'s `{kind: grain, amount: 1}` -- the relocated form of
    `_req_transfer`'s two literals -- and it filled them INSIDE `evaluate`, i.e. at the FOLD, for
    an act whose payload carried neither. Two consequences, and the second is why it could not
    stay once operands became real: (1) the value had two homes, the cell and the person's
    derivation, free to disagree; (2) the fold would ADMIT a `transfer` on operands the cell had
    invented and `_eff_transfer` would then raise on the very same operands being absent from the
    payload -- a precondition and an effect reading different acts. The values moved to
    `DEFAULT_FIXTURES` (`default_store_kind`, `default_transfer_amount`), unchanged, where the
    person derives them and the act CARRIES them.

    ⚠ `names` (plan position `19`) -- THE CELL'S TOP-LEVEL CONJUNCTS, NAMED, one per clause of a
    top-level `all:` (or one for a single clause), `None` where a clause carries no `conjunct:`. They
    exist for ONE reader, the keyed `emits_on_refusal:` (`data/verbs.py`, loader invariant 4's
    per-conjunct half), which maps each name to the refusal kind that conjunct emits; the loader
    refuses a name on a row that keys nothing to it, so a name is never a dead label (`ID-13`)."""
    requirement: Requirement
    names: tuple = ()

    def conjuncts(self) -> tuple:
        """The named top-level conjuncts, in order, `None`s dropped."""
        return tuple(n for n in self.names if n is not None)

    def decide(self, reader, binding, observed) -> tuple:
        """`(value, failed)` -- the verdict and the NAME of the conjunct that decided a non-True one
        (`None` if True or unnamed). A top-level `AllOf` reports its deciding clause by position,
        which `names` turns into the name; a single clause decides alone. Nested conjunctions are
        one conjunct of their parent: only the top level is named."""
        req = self.requirement
        if isinstance(req, AllOf):
            value, i = req.decide(reader, binding, observed)
        else:
            value = req.check(reader, binding, observed)
            i = None if value is True else 0
        name = self.names[i] if i is not None and i < len(self.names) else None
        return value, name

    def operands(self) -> tuple:
        return self.requirement.operands()

    def entity_operands(self) -> tuple:
        return self.requirement.entity_operands()

    def needs(self) -> frozenset:
        return self.requirement.needs()

    def stems(self) -> tuple:
        """Delegated like every other accessor here, so the load-time stem closure sees a cell's
        stems whether it is asked of the wrapper or of the clause tree (§8: one owner)."""
        return self.requirement.stems()

    def check(self, reader, binding, observed):
        return self.requirement.check(reader, binding, observed)

def _observe(reader, subject, predicate: str, observed: list):
    v = reader.read(subject, predicate)
    observed.append(Observation(subject, predicate, v))
    return v

def evaluate(req: Optional[TypedRequires], reader, binding: dict) -> Verdict:
    """THE ONE EVALUATOR. `Verdict(value in {True, False, UNKNOWN}, observed)`.

    An UNTYPED verb is UNKNOWN to every reader -- not True, and not False. That is what makes
    `belief_contradicts` return *not contradicted* for one (§F1's asymmetry) while the fold still
    REFUSES one whose predicate is missing (§42.2's polarity). The same value, read with the two
    polarities the two sites actually have."""
    if req is None:
        return Verdict(UNKNOWN, ())
    # ⚠ THE BINDING IS THE CALLER'S AND THE CELL CONTRIBUTES NOTHING TO IT. Until `W-C` this
    # started from `req.operand_defaults`, so an operand the ACT did not carry was supplied HERE
    # -- under both readers, invisibly. An unsupplied operand is UNKNOWN now, and UNKNOWN refuses
    # in the fold and does not contradict for the person, which is the polarity pair the rest of
    # this block is built on.
    b = {k: v for k, v in (binding or {}).items() if v is not None}
    observed: list = []
    # `19`: `decide`, not `check` -- the same reads in the same order (`AllOf.check` IS `decide`'s
    # first half), plus the name of the conjunct that decided a refusal, for `refusal_for`.
    value, failed = req.decide(reader, b, observed)
    return Verdict(value, tuple(observed), failed)

def binding_of(actor: str, operands: dict, via: Optional[str] = None) -> dict:
    """THE ONE BINDING. An actor, plus the operands something carries -- and BOTH READERS BUILD IT
    HERE, which is `W-C`'s whole point.

    ⚠ WHAT THIS REPLACED WAS TWO DIFFERENT DECISIONS WEARING ONE DECLARATION'S CLOTHES.
    `binding_from_act` did a LITERAL key match on the payload; `binding_from` (the person's side,
    now deleted) REBOUND the Candidate's `subject` onto whatever the requirement's entity operand
    happened to be called -- `from` for `transfer`, `to` for `move`, `site` for `restore`. So the
    person evaluated `stores(SUBJECT, kind)` and the fold evaluated `stores(<unbound>, kind)`:
    not the same cell asked twice, but a second, undeclared decision about WHOSE granary the
    requirement is about. The person's rebinding was also WRONG on its own terms -- §54 item 7
    says `hearth(GIVER)`, and the giver is the actor, never the referent.

    There is nothing left to rebind: `operands_for` derives every operand the cell names, the act
    CARRIES them, and both sides pass the same bag through here. `actor` is the one operand that
    is never carried, because it is structural on both sides -- `Act.actor` for the fold, `p.id`
    for the person -- and a copy of it on the payload would be a second home for a fact the Act
    already holds (`ID-2`).

    Operands outside `requires_operands` are dropped: a payload is also where `record`, `stages`,
    `venue` and `harm` ride, and the grammar's vocabulary is closed.

    ⚠ `via=` (plan position `19`) -- THE SEAT THE ACT EXERCISES, STRUCTURAL ON BOTH SIDES FOR THE
    REASON `actor` IS: `Act.via` for the fold (`binding_from_act`), `exercised_seat(p, row)` for the
    person (`epistemic.belief_contradicts`). It is read by one form, `Basis` (§F.24a form 7), and
    is added only when there is one, so a seatless act's binding is byte-for-byte what it was and a
    `basis` clause over it reads UNKNOWN. It is never taken from the payload: `via` is not an
    operand, and a payload key of that name would be dropped by the filter above like any other."""
    out = {"actor": actor,
           **{k: v for k, v in (operands or {}).items() if k in REQUIRES_OPERANDS}}
    if via is not None:
        out[VIA] = via
    return out

def binding_from_act(a) -> dict:
    """THE RESOLVER'S BINDING -- `Act.payload`, plus the actor.

    ⚠ IT WAS ALLOWED TO BE INCOMPLETE AND IT ALWAYS WAS; `W-C` CLOSED THAT AND DID NOT MAKE IT
    IMPOSSIBLE. `pack_scenes` used to put only the Candidate's `subject` on the payload, so
    `transfer` had no `kind`, `move` had no `to` and `work` had no `site`, and every one of those
    evaluated UNKNOWN and refused. A COMPUTED act now carries the operands its verb's cell names,
    because a Candidate that could not bind them was never formed. A HAND-BUILT act still binds
    whatever its author put on the payload, and an author who omits one still gets UNKNOWN and a
    refusal -- which is the polarity §42.2 wants and the reason this is not asserted here."""
    return binding_of(a.actor,
                      a.payload if isinstance(getattr(a, "payload", None), dict) else {},
                      getattr(a, "via", None))

# `WorldReader` and `LedgerReader` -- the two dispatchers `read()` on the stems below -- live in
# `shape.py`, not here (see this module's docstring). `REQUIRES_STEMS` is the closed vocabulary
# `_require_known_stem` (below) checks a cell's stems against at LOAD; `WorldReader.read`'s own
# `if stem ==` chain is a separate, hand-written dispatcher over the same names -- the two are not
# generated from one another, so a stem added here without a matching branch there still loads
# clean and reads UNKNOWN forever. `LEDGER_DERIVED_STEMS` is read at the WITNESS deposit site in
# `shape.py`, which imports it back from here.

# THE STEMS `WorldReader.read`/`LedgerReader.read` DISPATCH ON. The two readers below are the
# only consumers.
#
# ⚠ WHY THIS EXISTS: THE GRAMMAR CLOSED ON FORM AND OPERAND NAMES AND NOT ON THE STRINGS THAT
# ACTUALLY SELECT THE PREDICATE. Found by the W-A adversarial pass. `_build_clause` refused at load
# on an unrostered form, an unrostered operand, and an operand outside the form's `needs:` -- and
# validated NOTHING about `Existence.kind`, `ScalarThreshold.scalar`/`threshold_predicate` or
# `Relation.relation`. Those four strings are what `read` dispatches on, and an unrecognised one
# fell through to `return UNKNOWN` forever: `kind: Commit` for `commit`, or `relation: present-at`
# for `present_at`, LOADED CLEAN, evaluated UNKNOWN in every world, and the fold refused the verb
# everywhere -- reported as `H-94`'s honest operand famine. A typo and a design gap were
# indistinguishable, which is the silent-wrong-answer shape this file refuses everywhere else.
# roster-exempt: MECHANISM. These are the grammar's own predicate stems -- what a REQUIREMENT MAY
# ASK -- not the game's vocabulary; `rosters.yaml` says what the world contains.
# ⚠ PLAN POSITION `19` ADDED FOUR, EACH A QUESTION A REMIT VERB'S CELL ASKS AND NONE A NEW FORM:
# `purview` and `bench` are `Basis`'s (§F.24a form 7) two seat rules -- ruling (4)'s purview and the
# `determination` basis's bench, each the write gate's own predicate read early; `bench.size` and
# `quorum` are `determine`'s quorum conjunct, a `scalar_threshold` (form 2) of the bench's size
# against a SECOND READ, `work`'s `floor` shape, so no operand is added to `cardinality` (the
# widening `21_RECONCILIATION.md` A.1 struck). `WorldReader.read` answers all four.
REQUIRES_STEMS = frozenset({
    "exists", "stores", "condition", "floor", "contain.path", "held_by", "present_at",
    "claim.held", "rank", "purview", "bench", "bench.size", "quorum",
})

# THE STEMS WHOSE VALUE IS COMPUTED **FROM THE HOLDER'S OWN LEDGER** -- and which therefore MAY
# NOT BE DEPOSITED INTO IT. `WorldReader.read`'s `claim.held` branch answers
# `any(c.subject == subject for c in p.ledger)`, so a WITNESS deposit of
# `Observation(X, "claim.held", False)` appends a Claim whose `subject` IS `X` and makes that same
# read return True from the barrier that stored it. **The belief is false the moment it becomes
# readable, and it is made false by the act of recording it.**
#
# ⚠ THIS IS A CLOSURE PROPERTY OF THE GRAMMAR, NOT A SPECIAL CASE ON A VALUE OR AN ENTITY. The
# rule quantifies over PREDICATES THAT READ THE STORE THEY WOULD BE WRITTEN INTO; `claim.held` is
# the only member today because `OwnLedger` is the only form that reads a ledger. It is the THIRD
# principled exclusion at the deposit site and it has the same shape as the other two -- UNKNOWN
# (the instrument's gap must not become a belief) and duplicates (one belief, stored once).
#
# ⚠ MEASURED BEFORE EXCLUDING, seed 0, NPC-088 at `actor`, 8 seasons (`W-B` adversarial pass,
# 2026-09-04): at end of season 0 `LedgerReader(p_a).read('r_hearth','claim.held')` is **False**
# while `WorldReader(w,'p_a').read('r_hearth','claim.held')` is **True** -- the two readers
# disagreeing about the SAME person's SAME ledger, which is the one thing `belief_contradicts`'
# docstring says cannot happen (*"the same cell asked of two readers, differing only in WHAT THEY
# READ and in POLARITY"*). The person then declines `tell` for a season on a belief the fold
# would have admitted. It is not permanent: the block is per-SUBJECT and the claim is EVICTED by
# the ledger cap at season 2, after which `tell` runs again -- so the belief is corrected by
# FORGETTING rather than by anything the world did, which is a worse property than a wrong belief,
# not a milder one.
#
# ⚠ THE ALTERNATIVE WAS BUILT IN ARGUMENT AND REJECTED, and is recorded so it is not re-derived:
# make `LedgerReader` answer `claim.held` FROM MEMBERSHIP too, so the readers agree. That fails
# three ways -- the deposited Claim's `value` would then be written and never read (`ID-13`'s dead
# carrier, exactly what `W-A` refused to build), `any(c.subject == ...)` would live in two classes
# (§8: never re-implement a rule), and the belief store would become incapable of being wrong for
# form 6, which is the `T3` property `OwnLedger`'s own docstring exists to preserve.
# roster-exempt: MECHANISM, as `REQUIRES_STEMS` above -- this is a property of the GRAMMAR'S
# predicates (which of them read the ledger), not vocabulary the world contains.
LEDGER_DERIVED_STEMS = frozenset({"claim.held"})


def _check_shortfall_stem(stem, requires_stems: frozenset, content_stem) -> None:
    """Plan position `19d`. THE SHORTFALL CLAIM'S STEM MUST MEAN ONE THING, so it may be neither a
    stem the `requires` grammar reads nor the `content:` stem. The first collision would have
    `LedgerReader` answer the claim as a belief about a store LEVEL, and `belief_contradicts` would
    then decline a transfer on a number that was never a level. The second would have
    `_from_content_claim` read a shortfall as a document. `record_kinds`/`tenure_kinds`' overlap
    refusal (`data/rosters.py`) is the precedent: one stem, one reading. An absent or non-string
    stem refuses too, because the writer would otherwise spell `None:grain`. Factored into a
    function so the test can plant each collision (§0.1 pt 3)."""
    if not isinstance(stem, str) or not stem or ":" in stem:
        raise Unspecified(
            f"rosters.yaml: shortfall_sourced_operands.claim.predicate is {stem!r}",
            "rosters.yaml -- shortfall_sourced_operands",
            needs="a bare predicate stem (a word with no `:`)",
            law="the claim is `<stem>:<kind>`; a stem that is absent or already holds a `:` "
                "cannot be split back into the kind the reader needs")
    if stem in requires_stems or stem == content_stem:
        raise Unspecified(
            f"rosters.yaml: shortfall_sourced_operands.claim.predicate {stem!r} is already a "
            f"stem another reader answers", "rosters.yaml -- shortfall_sourced_operands",
            needs="a stem no `requires` form reads and that is not the content stem",
            law="one stem, one reading -- a shared word is two questions spelled one way")


_check_shortfall_stem(SHORTFALL_PREDICATE, REQUIRES_STEMS, RECORD_CONTENT.get("predicate"))

# THE KEY A TOP-LEVEL `requires_typed:` CLAUSE IS NAMED BY (plan position `19`), so a keyed
# `emits_on_refusal:` can say which refusal kind that conjunct emits. One spelling for the builder
# above and the verb loader (`data/verbs.py`), which checks the names against the keys.
CONJUNCT_KEY = "conjunct"


def _require_known_stem(stem: str, where: str) -> None:
    """A predicate stem outside `REQUIRES_STEMS` REFUSES AT LOAD rather than reading UNKNOWN
    forever. The three sibling closure checks below already do this for forms and operands; this
    is the fourth, and its absence made a typo indistinguishable from a design gap."""
    if stem not in REQUIRES_STEMS:
        raise SystemExit(
            f"verb_table.yaml: {where} names predicate stem {stem!r}, which no reader dispatches "
            f"on. Declared stems: {sorted(REQUIRES_STEMS)}. An unknown stem would evaluate "
            f"UNKNOWN in every world and refuse the verb everywhere, which is indistinguishable "
            f"from an honest operand gap.")

def _build_clause(verb: str, cell: dict) -> Requirement:
    if not isinstance(cell, dict):
        raise SystemExit(f"verb_table.yaml: {verb!r} `requires_typed:` clause is not a mapping: "
                         f"{cell!r}")
    # ⚠ `conjunct:` IS A TOP-LEVEL NAME ONLY (plan position `19`). `build_typed_requires` strips it
    # from each top-level clause before this runs; one arriving HERE sits inside a nested `all:`,
    # which is one conjunct of its parent and cannot have a refusal kind of its own. Refused rather
    # than ignored: a name nothing can key to is the dead label `ID-13` refuses.
    if CONJUNCT_KEY in cell:
        raise SystemExit(f"verb_table.yaml: {verb!r} names a `{CONJUNCT_KEY}:` inside a nested "
                         f"`all:` ({cell[CONJUNCT_KEY]!r}); only a top-level conjunct can be keyed "
                         "to a refusal kind")
    if "all" in cell:
        clauses = tuple(_build_clause(verb, c) for c in (cell["all"] or ()))
        if len(clauses) < 2:
            raise SystemExit(f"verb_table.yaml: {verb!r} has an `all:` with {len(clauses)} "
                             "clause(s); a conjunction of one is the clause itself")
        return AllOf(clauses)
    form = cell.get("form")
    if form not in REQUIRES_FORMS:
        raise SystemExit(
            f"verb_table.yaml: {verb!r} names requires form {form!r}, which is not in "
            f"rosters.yaml's requires_forms: {sorted(REQUIRES_FORMS)}. §F.24a derives SEVEN forms "
            "from the 32 live cells; an eighth is a new thing a precondition can ASK, which is a "
            "design change and not a table edit")
    cls = REQUIREMENT_TYPES.get(form)
    if cls is None:
        raise SystemExit(
            f"verb_table.yaml: {verb!r} uses form {form!r}, which is IN the grammar and has no "
            "implementation. `cardinality` and `basis` have no `own`-eligible cell -- their live "
            "cells are `confer` and `revoke`, which stay on REQUIRES_PREDICATES")
    try:
        req = cls(**{k: v for k, v in cell.items() if k != "form"})
    except TypeError as e:
        raise SystemExit(f"verb_table.yaml: {verb!r}'s {form!r} cell does not fit the form: {e}")
    allowed = set(REQUIRES_FORM_NEEDS.get(form) or ())
    for o in req.operands():
        if o not in REQUIRES_OPERANDS:
            raise SystemExit(
                f"verb_table.yaml: {verb!r} binds operand {o!r}, which is not in rosters.yaml's "
                f"requires_operands: {sorted(REQUIRES_OPERANDS)}. Coining an operand is filling "
                "`H-94` by keyword argument")
        if o not in allowed:
            raise SystemExit(
                f"verb_table.yaml: {verb!r}'s {form!r} cell binds {o!r}, which is not in that "
                f"form's `needs:` ({sorted(allowed)})")
    # ⚠ THE FOURTH CLOSURE CHECK, AND THE ONE THAT WAS MISSING. The three above close the FORM
    # and the OPERANDS; this closes the PREDICATE STEM, which is what the readers actually
    # dispatch on. Every stem a requirement can ask for is read off the requirement itself, so a
    # new form contributes its stems automatically rather than needing this list edited.
    for stem in req.stems():
        _require_known_stem(stem, f"{verb!r}'s {form!r} cell")
    return req

def build_typed_requires(verb: str, cell) -> Optional[TypedRequires]:
    """A `requires_typed:` cell into a `TypedRequires`, or `None` for an explicit `none`.

    `None` means THE COLUMN IS NOT TYPED FOR THIS VERB, and the verb stays on
    `REQUIRES_PREDICATES` -- which for a verb with no predicate is the fold's existing refusal,
    naming what is missing. It is never a silent success."""
    if cell is None:
        return None
    if isinstance(cell, str):
        if cell.strip().lower() == "none":
            return None
        raise SystemExit(f"verb_table.yaml: {verb!r} `requires_typed:` is the string {cell!r}; "
                         "the only string admitted is `none`, which must carry a "
                         "`requires_typed_note:` saying why")
    if not isinstance(cell, dict):
        raise SystemExit(f"verb_table.yaml: {verb!r} `requires_typed:` is not a mapping: {cell!r}")
    # ⚠ `operand_defaults:` IS NO LONGER A KEY AND A CELL CARRYING ONE MUST REFUSE, not be
    # ignored. `W-C` moved `transfer`'s two to `DEFAULT_FIXTURES`; dropping the key silently would
    # let a later table edit re-introduce a fold-side default that no longer has a reader, and it
    # would read as accepted. `_build_clause` raises on any key the form does not take, so the
    # refusal is already structural -- this comment is here so the next reader knows the absence
    # is a decision and not an oversight.
    # ⚠ PLAN POSITION `19`: EACH TOP-LEVEL CONJUNCT MAY CARRY A `conjunct:` NAME -- stripped here,
    # before the form is built (a form takes only its own fields), and kept on the cell as
    # `TypedRequires.names`, which is what a keyed `emits_on_refusal:` maps from. Whether every
    # conjunct is named, and every name keyed, is the VERB loader's check (`data/verbs.py`,
    # invariant 4's per-conjunct half), because only the row knows whether it keys its refusals.
    tops = cell["all"] if "all" in cell and isinstance(cell.get("all"), list) else [cell]
    names = tuple(c.get(CONJUNCT_KEY) if isinstance(c, dict) else None for c in tops)
    named = [n for n in names if n is not None]
    if (any(not isinstance(n, str) or not n.strip() for n in named)
            or len(set(named)) != len(named)):
        raise SystemExit(f"verb_table.yaml: {verb!r} names its conjuncts {list(names)}; each "
                         f"`{CONJUNCT_KEY}:` is a non-empty word, and no two alike -- a keyed "
                         "`emits_on_refusal:` maps each to ONE refusal kind")

    def strip(c):
        return {k: v for k, v in c.items() if k != CONJUNCT_KEY} if isinstance(c, dict) else c
    stripped = ({**cell, "all": [strip(c) for c in tops]} if "all" in cell and tops is cell["all"]
                else strip(cell))
    return TypedRequires(_build_clause(verb, stripped),
                         names if any(n is not None for n in names) else ())
