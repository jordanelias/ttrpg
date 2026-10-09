"""`season.data.verbs` -- the verb table and the alignment table, extracted from `shape.py`
(step 3 of the decomposition, a PURE MOVE: no behaviour changed, only where the code lives).

Owns `VerbRow` and its loader (`_load_verb_table`/`VERB_TABLE`), the load-time constants a row is
checked against (`VERB_TABLE_YAML`, `ELIGIBILITY_KINDS`), `NO_PRECONDITION` (the "no cell" prose
sentinel both `requires` and `requires_typed` use), `rows_without_a_producer` (§7.2's report --
it reads `VERB_TABLE`, which is why it did not move with the write matrix in step 2), and the
alignment table in full: its loader (`_load_alignment`/`ALIGNMENT`), its immutable baseline
(`ALIGNMENT_DECLARED`, `ALIGNMENT_DEFAULT_CELL`), and its sweep (`ALIGNMENT_SWEEP`/
`alignment_at`).

`verb_table.yaml` is Part E's body, loaded once at import: *"#353 types `resolve : (Act[],
World) -> Event[]` and never says what any verb DOES... with no table, every act needed a
hand-written `effect` lambda, and A LAMBDA PER ACT IS A SECOND RESOLVER."*

`_load_verb_table` calls `season.data.requires.build_typed_requires` once per row -- see that
module's docstring for the ordering constraint this creates and how it is satisfied structurally
by THIS module's own import of `requires`, below, rather than by file position.

⚠ `align()` AND `align_kind()` LIVE HERE, BESIDE THE TABLE THEY READ (telling workplan T2). `align`
was in `shape.py`, then `decision.py`, then `decision/options.py`; each move carried the rebind
address with it, and the last one left a reader in `options.py` and the table here. Now the
`ALIGNMENT` binding and its only reader share this module, so the rebind that moves one moves
the other: the `H-66` sweep and the `H-146` tests rebind `data.verbs.ALIGNMENT`, and nothing
else binds the name. Every reader (`choose`'s score, `refuses`, `person_q._pursuits_violated_by`, `corpus_run`) calls
`align`; tests that import `ALIGNMENT` do so function-locally and read it live -- a copy imported
by name at module scope would be a stale snapshot.

⚠ `VERB_TABLE` IS ASSIGNED TWICE, VERBATIM, AND ONLY THE SECOND ASSIGNMENT EVER RUNS. The
forward declaration below (`VERB_TABLE: dict = {}`) carries a comment from a PRIOR layout of
`shape.py`, from before steps 1-2 extracted the write matrix and roster readers: at that time
real loading code sat physically between the forward declaration and the fill. It does not any
more -- the two lines are adjacent -- and nothing at IMPORT TIME reads `VERB_TABLE` in the gap:
checked directly, `_load_alignment`'s own read of it (`admitted = set(VERB_TABLE) | ...`) is inside a
function BODY, defined a few lines after the real fill but not CALLED (`ALIGNMENT =
_load_alignment()`) until further still -- by which point the real fill has long since run.
Preserved unchanged because this is a PURE MOVE and the forward declaration is otherwise
harmless -- a `dict` type hint on a name the next line immediately rebinds.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass, field, fields
from typing import Optional

from . import files
from ..gaps import Forbidden, InstrumentDefect, Unspecified
from .matrix import MATRIX, Step
from .requires import REQUIRES_OPERANDS, TypedRequires, build_typed_requires
from .rosters import (
    PURSUIT_AXES, PURSUITS, RELEASABLE_KINDS, RUNG_KINDS, STRATA, TENURE_KINDS, load_yaml,
    require_member, roster, roster_map,
    table,
    table_meta,
)

VERB_TABLE_YAML = files.VERB_TABLE_YAML

ELIGIBILITY_KINDS = roster("eligibility_kinds")

# The "no cell" prose sentinel `requires` and `requires_typed` use. Defined ABOVE the loader (it sat
# at the foot of this module until 2026-09-25) because loader invariant 4 now reads it at load.
NO_PRECONDITION = ("—", "-", "")

# Loader invariant 9's roster: the prizes `contest_subsystems` claims, read once at load.
_CONTEST_PRIZES = frozenset(roster_map("contest_subsystems", "prizes"))

BENEFICIARY_KINDS = roster("beneficiary_kinds")
# ⚠ WHICH BENEFICIARY KINDS NEED A CELL TO BIND -- READ FROM THE ROSTER, NEVER LISTED HERE.
# `beneficiary_kinds.carriage` classifies every member `structural` or `operand`:
#   structural -- the carrier is on the Candidate regardless of the row's `requires_typed`
#                 (`actor` is held unconditionally, `subject` is a field, `none` carries nothing);
#   operand    -- carried only where the row's own cell binds or admits it, so invariant 13's
#                 third check must verify carriability for it.
# ⚠⚠ THIS WAS A LITERAL TUPLE AND JORDAN'S OWN GUARD CAUGHT IT
# (`test_jordan_no_definition_is_hardcoded_in_a_body`). Two versions were wrong in the same
# direction: first `("to",)`, a hand-kept list of operand members; then a hardcoded structural
# set subtracted from the roster, which is the same definition written the other way round.
# Either one silently stops covering a member the moment `rosters.yaml` gains one -- which is
# precisely the edit that roster's own note invites. Now a new member with no `carriage:` entry
# REFUSES at load, so the check cannot fall behind the roster.
_BENEFICIARY_CARRIAGE = roster_map("beneficiary_kinds", "carriage")
_unclassified = set(BENEFICIARY_KINDS) - set(_BENEFICIARY_CARRIAGE)
if _unclassified:
    raise SystemExit(
        f"rosters.yaml: `beneficiary_kinds` carries {sorted(_unclassified)} with no `carriage:` "
        "entry. Every member must be classified `structural` or `operand`, because loader "
        "invariant 13's third check verifies carriability for the operand ones and would "
        "silently skip an unclassified member -- CAT-2's dead option 1 re-entering through the "
        "column, which that check exists to forbid.")
_OPERAND_BENEFICIARIES = tuple(
    sorted(k for k, v in _BENEFICIARY_CARRIAGE.items() if str(v).strip() == "operand"))

@dataclass(frozen=True)
class VerbRow:
    verb: str
    stratum: str
    eligibility: tuple        # a DISJUNCTION -- `transfer` is eligible by `remit:issue` OR `own`
    #                           OR `hold:<store>`
    requires: str
    writes: tuple          # ("Kind.field", ...) -- each MUST be a Part D row
    emits: tuple
    emits_on_refusal: tuple
    grade: str
    # ⚠ THE SCALE THE ACT REACHES — a `rung_kinds` member (Jordan, 2026-09-02: *"we also need
    # stratum that concern governance and management re different scales of factions/governing
    # bodies"*). It is a SEPARATE AXIS from `stratum`, crossed with it: the stratum says what KIND
    # of act this is and orders resolution; the scale says WHOSE BODY it reaches. Five strata x
    # eight scales covers the governance surface without multiplying strata.
    #
    # ⚠ AND THE SCALE LADDER ALREADY EXISTED — `rung_kinds`: person, hearth, community,
    # settlement, territory, province, duchy, realm. Minting a second roster for it would be §8
    # broken on the exact axis this column is about.
    #
    # ⚠ A FACTION IS NOT ONE OF THEM, AND THAT IS A RULING RATHER THAN AN OMISSION.
    # `ARCHITECTURE_V2.md:93` lists *"a **faction acting** as an actor"* in its REFUSAL table, at
    # `L1`, with three corpus cases that wanted it; `H-21` completes it — *"a faction's treasury is
    # matter at the rung or office that holds it"*. So a faction never acts: a PERSON HOLDING AN
    # OFFICE acts, and the scale is the rung that office reaches. Governance at faction scale is
    # `binding_decision x <rung>`, not a faction verb.
    #
    # ⚠ SAME NAME AS A RETIRED FIELD, AND THE COLLISION IS WORTH NAMING HERE RATHER THAN AT ITS
    # OWN SITE. `04_CODE_ARCHITECTURE.md` §A.3 row 4 (`04:173`) and §B.13 invariant 10 (`04:470`)
    # both say a `scale:` key is "deleted; the loader rejects the key" — but that row describes
    # THE CHAIN's `scale:` (a per-module/per-verb-row concept, retired at Stage 1/2, ID-13). This
    # field is a later, unrelated ruling under the same word (`CLAUDE.md` §4's exact hazard: one
    # spelling, two meanings, no shared context between the sessions that met each). It is not
    # rejected by 04's rows above; those rows are about a different, already-dead field. `04` is
    # ratified and this comment does not edit it (`CLAUDE.md` §0.05) — it names the ambiguity at
    # the site that would otherwise be misread, per the layer-conformance skill's B4.
    scale: str = "person"
    # ⚠ PART E'S `contests:` COLUMN, WHICH WAS TRANSCRIBED INTO A NOTE AND LOST.
    # `ARCHITECTURE_V2.md:394` declares it — *"`contests: <prize> | none` — if set, ROUTES TO THE
    # SEAM AT RESOLVE (§39)"* — and `:434` sets it on `kill / wound` (*"`contests: the body` → the
    # seam"*). The loader had no such field, so the routing landed in `requires_note`, which
    # nothing reads, and the fold executed a kill AS A DIRECT WRITE. Jordan, 2026-09-02:
    # *"that…would trigger the personal combat scene. you can't just kill or wound imo."* The
    # design agrees with him and the instrument was the thing disagreeing.
    contests: str = ""
    # ⚠ THE SIXTH COLUMN, ADDED 2026-09-03 (#358 rev.2 §C.4 / F6, loader invariant 12).
    # `writes` was a flat tuple applied UNCONDITIONALLY AFTER THE SEAM RESOLVED, so a LOST contest
    # wrote exactly what a won one did -- `kill / wound` killed on any degree, and `Event.degree`
    # was read by nothing anywhere. A resolution whose result is discarded is not a weak outcome
    # model; it is a contest that did not happen.
    #
    # A verb WITHOUT `contests:` keeps the flat tuple and this stays empty.
    # A verb WITH `contests:` declares `writes` as a MAP from degree, and `writes` holds the union
    # (so the load-time Part D check below still sees every pair it must validate).
    writes_by_degree: dict = field(default_factory=dict)
    # ⚠ AND SO IS `emits:`, FOR THE SAME REASON ONE FIELD DEEPER. A flat `emits` on a contested
    # verb reports ONE outcome for every band -- `kill / wound` emitted `person.died` whether the
    # target died, was wounded, or walked away untouched. That is ID-9's class (a success report
    # for something that did not happen) inside the epistemic layer, where every witness then
    # mints a claim from it.
    emits_by_degree: dict = field(default_factory=dict)
    # ⚠ THE SEVENTH COLUMN, ADDED BY `W-A` (2026-09-04). THE PROSE `requires` STAYS BESIDE IT AND
    # IS THE PROVENANCE -- each cell names the §E3 line it was transcribed from, so the derivation
    # can be checked rather than trusted. `None` means the column is NOT typed for this verb and
    # the fold falls back to `REQUIRES_PREDICATES`, which for a verb with no predicate is the
    # existing refusal naming what is missing.
    requires_typed: Optional["TypedRequires"] = None
    # Why a row carries `requires_typed: none`. Required BY THE LOADER on such a row: an untyped
    # cell with no reason is indistinguishable from one nobody got to.
    requires_typed_note: str = ""
    # ⚠ THE EIGHTH COLUMN, ADDED BY PHASE-6 ITEM `6d` (2026-09-17). WHO THE ACT IS TAKEN FOR THE
    # GOOD OF -- a `beneficiary_kinds` member, resolving to a carrier THE CANDIDATE ALREADY HOLDS.
    # `CAT-2`, closed at step 5: *"DECLARE IT -- and declare it as a STATIC COLUMN ON
    # `verb_table.yaml` ... NOT as a fifth field on `Candidate`."*
    #
    # ⚠ THE OTHER TWO OPTIONS ARE DEAD BY MEASUREMENT AND BY RULING, AND THE MEASUREMENT IS
    # RE-RUNNABLE HERE. Deriving the beneficiary from the operand binding fails because 24 of 38
    # verbs are UNTYPED and can carry no operand at all; only 12 admit `to`. Re-take it with
    # `requires_typed.operands() | ({"subject","to"} & requires_typed.needs())` over this table.
    # A post-hoc attribution modifier is dead by Jordan's own correction -- orientation is a
    # weight AT APPRAISAL, not a rescoring of what a win was worth.
    #
    # ⚠⚠ AND IT CANNOT BE DERIVED FROM `writes:` EITHER, WHICH IS WHY IT IS DECLARED RATHER THAN
    # COMPUTED. `kill / wound` writes `Person.body` and `Person.exists` ON THE SUBJECT and the
    # good does not accrue to the person felled: A WRITE CAN BE A HARM. A rule reading the write
    # column would name the victim as the beneficiary of their own killing. The write column is
    # EVIDENCE for each row -- every `beneficiary_note:` cites it -- and never the rule.
    #
    # ⚠ `none` IS A DECLARATION. The loader requires the column on every row, so a new verb
    # cannot arrive without one; an absent column would read as `false` for every verb, which is
    # the UNKNOWN/False collapse `operands_for` refuses one level down.
    beneficiary: str = ""
    # ⚠ THE NINTH COLUMN, ADDED AT PLAN POSITION `15` -- THE OTHER PARTY, NAMED BY THE OPERAND
    # THAT CARRIES THEM. `ED-IN-0210` ruling 1: *a real interaction has a COUNTERPARTY, an OBSTACLE
    # and a DEGREE*; ruling 2: `petition` is *the first in the set where a counterparty is
    # structurally required*. `decision/options.py::opening_set` reads it and forms no Candidate
    # whose counterparty is the person themselves -- the contested-verb rule beside it (`contests:`
    # makes `subject` the second claimant), generalised to a row that names its counterparty
    # directly. `""` is the declared absence; the loader requires a named operand to be one the
    # row's typed cell BINDS, so the Candidate always carries the thing compared -- or, on an
    # UNTYPED row (`oblige`; `give` until plan position `14` typed it), a `requires_operands` member
    # no Candidate can carry, which makes `opening_set` form none: a second party the grammar
    # cannot yet name. Plan position `14` asks the same column again IN THE FOLD
    # (`loop/resolve.py::_admits`, `COUNTERPARTY_CLAUSE`), for the hand-built act no person forms.
    counterparty: str = ""
    # ⚠ THE TENTH COLUMN'S SECOND SHAPE, ADDED AT PLAN POSITION `19` -- `04 §B.13` INVARIANT 4'S
    # PER-CONJUNCT HALF (F7): *"every failable clause has a refusal kind -- not only a verb with a
    # `requires`, but each CONJUNCT of it, and any eligibility alternative that can decline."* §C.4's
    # fold spells the reader: `emit(row.refusal_for(ELIGIBILITY))` and
    # `emit(row.refusal_for(failed_conjunct))`. A row may declare `emits_on_refusal:` as a MAPPING
    # from a FAILABLE CLAUSE to its kinds, and this holds it; `emits_on_refusal` above holds the
    # UNION, so every reader that asks *is this Event one of the row's refusals* (`corpus_run`,
    # `loop/driver.py`, `loop/deliberate.py`) is unchanged. `writes`/`writes_by_degree` is the
    # precedent, one column over. Empty = a flat row, whose every refusal emits the flat tuple exactly
    # as before `19` -- so no row that did not opt in moves by a byte.
    refusals_by_clause: dict = field(default_factory=dict)
    # ⚠ THE TWO DECLARED ABSENCES A DRIVER-CONSTRUCTION REFUSAL READS (plan position IN-41, `SM-9` +
    # `SM-11`). Each is the row SAYING WHY the fold cannot carry it, so `resolvable_verbs()` drops it
    # with a reason on record rather than without a word; `manifest/registry.py` refuses both
    # directions -- a gap with no note, and a note on a row that has no gap (for `effect_decline_note:`
    # a row that has an effect or writes nothing).
    #
    # `effect_decline_note:` -- the row WRITES and no `@effect_for` body exists, and here is why
    # (refusal (a), `check_effects`). It is one of THREE columns the retired `decline_note:` was split
    # into, because that one column declined an effect on some rows and a FORMATION on others
    # (`oblige`, `destroy_record` have effects; their notes say why no Candidate forms). The formation
    # half is `formation_decline_note:`, an annotation this loader ignores (its `*_note` rule) and no
    # gate reads -- a row whose effect EXISTS is resolvable, and why nobody forms it is a reader's fact.
    effect_decline_note: str = ""
    # `requires_decline_note:` -- the row has a precondition that NOTHING EVALUATES (no typed cell, no
    # `REQUIRES_PREDICATES` entry), and here is why (`check_preconditions`). The third column of the
    # split. NOT `requires_typed_note`, which says why the cell is untyped and stands on rows a
    # registered predicate DOES evaluate (`oblige`, `release`).
    requires_decline_note: str = ""

    def precondition_evaluable(self, predicates) -> bool:
        """Can the fold evaluate this row's precondition: none at all, a typed cell, or a
        `predicates` (`loop/predicates.py::REQUIRES_PREDICATES`) entry. The ONE answer
        `resolvable_verbs()`'s first gate and `check_preconditions` both read (`CLAUDE.md` §8);
        `loop/resolve.py::_admits` (which `_fold` calls) branches the same three ways. `predicates`
        is a parameter because this loader may not import `loop/`."""
        return (not self.has_precondition
                or self.requires_typed is not None
                or self.verb in predicates)

    @property
    def has_precondition(self) -> bool:
        """The row's `requires` cell names a precondition (it is not one of `NO_PRECONDITION`'s
        "no cell" spellings). The ONE spelling of that test for the two readers that sweep the whole
        table for it -- `precondition_evaluable` above and `manifest/registry.py::check_preconditions`
        (`CLAUDE.md` §8)."""
        return (self.requires or "").strip() not in NO_PRECONDITION

    def effect_carried(self, effects) -> bool:
        """Can the fold carry this row's effect: it writes nothing, so none is owed, or an
        `@effect_for` body exists in `effects` (`loop/effects.py`'s `EFFECTS`). The ONE answer
        `resolvable_verbs()`'s second gate and `manifest/registry.py::check_effects` both read
        (`CLAUDE.md` §8), as `precondition_evaluable` is for the first gate. `effects` is a
        parameter because this loader may not import `loop/`."""
        return not self.writes or self.verb in effects

    def refusal_for(self, clause: Optional[str]) -> tuple:
        """`04 §C.4`'s `row.refusal_for(clause)`: the kinds a refusal AT `clause` emits.

        A FLAT row answers its flat tuple for every clause, which is every row's behaviour before
        plan position `19`. A KEYED row answers the clause's own kinds -- and a clause it does not
        key RAISES, because the loader has already required a key for every clause that can fail
        (`ELIGIBILITY_CLAUSE` if an alternative can decline, each named conjunct, `WRITE_CLAUSE` if
        the row writes, `COUNTERPARTY_CLAUSE` if it names a second party). Reaching this with an
        unkeyed clause is therefore a FOLD defect -- a new
        refusal point nobody declared -- and emitting the union instead would publish kinds for
        conjuncts that did not fail, which is `ID-9` inside the scarcity channel."""
        if not self.refusals_by_clause:
            return self.emits_on_refusal
        if clause not in self.refusals_by_clause:
            raise InstrumentDefect(
                f"{self.verb!r} keys its refusals on {sorted(self.refusals_by_clause)} and was "
                f"refused at {clause!r}, which it does not key. The loader requires a kind for every "
                f"failable clause, so a clause arriving here unkeyed is a refusal point the fold "
                f"added without declaring it (04 §B.13 #4, F7)")
        return self.refusals_by_clause[clause]

    def eligibility_kinds(self) -> tuple:
        return tuple(a.split(":")[0].strip() for a in self.eligibility)

    def emits_at(self, degree: str | None) -> tuple:
        """WHAT THIS ACT REPORTS, GIVEN WHAT THE SEAM RETURNED. Same polarity as `writes_at`:
        an uncontested verb ignores the degree; a contested one with no degree, or with a degree
        it does not declare, RAISES rather than reporting the wrong outcome.

        ⚠ `H-115`: THESE TWO RAISES USED TO BE `SystemExit`, THE ONLY RUN-TIME REFUSALS IN
        `shape.py` OUTSIDE THE TYPED GAP TAXONOMY (which now lives in `season/gaps.py`). `SystemExit` derives from `BaseException`, so
        `corpus_run.run_case`'s `except (S.ShapeGap, S.Unspecified, S.Forbidden, S.NoProducer)`
        clause never catches it -- a one-case design gap escaped as a whole-corpus run
        termination, with no DESIGN-GAP row and no section citation. The load-time raises
        beside these (missing/malformed YAML, in the loader functions -- locate them by grepping for the
        load-time exit token itself, NOT from a line list, which rots on every edit and had
        already rotted before step 1) are CORRECTLY fatal and are UNCHANGED -- this file loads once, and a
        broken table should end the process. These four are not load-time; they fire per-act,
        mid-corpus, and belong in the taxonomy every other per-case refusal in the package uses."""
        if not self.emits_by_degree:
            return self.emits
        if degree is None:
            raise Unspecified(
                f"{self.verb!r} declares `contests: {self.contests}` and was folded with no "
                "degree, so there is no way to say WHICH outcome to report.",
                "S39/H-98",
                needs="a degree from the seam (contest()) before `emits_at` reads an outcome",
                law="#358 rev.2 §C.4 -- a contested verb's `emits` is degree-keyed; folding one "
                    "with no degree is the defect the column exists to make unwritable")
        if degree not in self.emits_by_degree:
            raise Unspecified(
                f"{self.verb!r} has no `emits` branch for degree {degree!r}. Declared: "
                f"{sorted(self.emits_by_degree)}.",
                "S39/H-98",
                needs=f"an `emits` branch for degree {degree!r}, or a resolver that returns only "
                      "a degree this verb declares",
                law="#358 rev.2 §C.4 -- an unlisted degree RAISES rather than reporting a "
                    "branch that did not happen")
        return tuple(self.emits_by_degree[degree])

    def writes_at(self, degree: str | None) -> tuple:
        """THE PAIRS THIS ACT ACTUALLY WRITES, GIVEN WHAT THE SEAM RETURNED.

        An uncontested verb ignores the degree entirely. A contested one looks the degree up, and
        an ABSENT degree RAISES rather than falling back to the union -- §42.2's polarity: zero
        evidence goes to the verdict AGAINST, never to a silent full write. `Failure: []` is
        lawful and means the act still EMITS having written nothing, which is what separates a
        LOSS from a REFUSAL.

        ⚠ `H-115`, SAME FIX AS `emits_at` ABOVE -- see that docstring. These two raised
        `SystemExit` and escaped `run_case`'s `ShapeGap` clause whole."""
        if not self.writes_by_degree:
            return self.writes
        if degree is None:
            raise Unspecified(
                f"{self.verb!r} declares `contests: {self.contests}` and was folded with no "
                "degree. A contested verb's writes are degree-keyed (#358 rev.2 §C.4); folding "
                "one without a degree is the defect that column exists to make unwritable.",
                "S39/H-98",
                needs="a degree from the seam (contest()) before `writes_at` selects a branch",
                law="#358 rev.2 §C.4 -- a contested verb's `writes` is degree-keyed; folding one "
                    "with no degree is the defect the column exists to make unwritable")
        if degree not in self.writes_by_degree:
            raise Unspecified(
                f"{self.verb!r} has no `writes` branch for degree {degree!r}. Declared: "
                f"{sorted(self.writes_by_degree)}. An unlisted degree RAISES rather than "
                "defaulting -- a missing branch is a hole, not a full write.",
                "S39/H-98",
                needs=f"a `writes` branch for degree {degree!r}, or a resolver that returns only "
                      "a degree this verb declares",
                law="#358 rev.2 §C.4 -- an unlisted degree RAISES rather than defaulting to the "
                    "union, which would write more than the contest actually resolved")
        return tuple(self.writes_by_degree[degree])

# Loader invariant 10's verb-row key set, DERIVED from `VerbRow` rather than listed: every field a
# YAML column fills (the two `*_by_degree` maps are built from `writes:`/`emits:`, and `19`'s
# `refusals_by_clause` from `emits_on_refusal:`, not read), plus `domain` (read for `release`,
# invariant 6) and `source` (every row's provenance column).
_VERB_ROW_KEYS = (frozenset(f.name for f in fields(VerbRow)
                            if not f.name.endswith(("_by_degree", "_by_clause")))
                  | {"domain", "source"})

# THE TWO FAILABLE CLAUSES THE FOLD OWNS, BESIDE A ROW'S OWN NAMED CONJUNCTS (plan position `19`) --
# the keys a keyed `emits_on_refusal:` uses for them. `ELIGIBILITY_CLAUSE` is `04 §C.4`'s own
# `refusal_for(ELIGIBILITY)`: no alternative of the row admitted the actor. `WRITE_CLAUSE` is F9's:
# the precondition held and the write moved nothing (`NoOpReceipt`, `state/gate.py`) -- an effect
# that DECLINED, which is a refusal the row must name like any other. Defined here, beside the loader
# that requires them, and imported by the fold (`loop/resolve.py`) that emits them.
ELIGIBILITY_CLAUSE = "eligibility"
WRITE_CLAUSE = "write"
# THE THIRD, PLAN POSITION `14` (U7-own): `ED-IN-0210` ruling 1's SECOND PARTY, ASKED ONCE, IN THE
# FOLD. A row naming a `counterparty:` operand is refused here when the act names nobody there or
# names the actor -- the `Tenure(X, X)` self-loop ruling 1 calls a fiat. `opening_set` already declines the
# same case person-side, so no computed act reaches it; this is the clause a HAND-BUILT act meets,
# and it replaces the per-effect copies (`_eff_petition`'s self-address decline) with one owner.
# Derived like the other two: a keyed row keys it iff it names a counterparty.
COUNTERPARTY_CLAUSE = "counterparty"


def _derive_openers_from_effects() -> dict:
    """LOADER INVARIANT 6'S SECOND HALF, DERIVED RATHER THAN HAND-COPIED (`OPENERS-DERIVE`,
    2026-09-29, `workplans/2026-09-28-the-plan-one-order-mc-v18-retired.md` §3.1 item 6).
    `rosters.yaml`'s `tenure_kinds` row used to carry an `openers:` mapping BY HAND, kept in sync
    by a human re-reading `loop/effects.py` -- correct the day it was transcribed (2026-09-25) and
    silently wrong the day a new opener effect landed with no matching edit here (`CLAUDE.md` §8's
    every-rule-lives-once hazard). The single owner of "which verb opens which kind" is the
    `Tenure(...)` construction itself, inside the function `@effect_for` registers for that verb:
    every site today names `kind` as a STRING LITERAL -- `Tenure(id, subject, object, kind, ...)`,
    positional, or a `kind=` keyword -- so an AST walk over `effects.py`'s own source (read as
    TEXT, never imported -- no `data` -> `loop` import edge) reads the identical fact the
    hand-written roster used to transcribe, with no second copy to fall behind.

    Returns EVERY tenure kind, including the ones no effect opens today -- an empty list, the same
    "declared means present" contract the hand-written roster kept -- because a kind with a
    `writes: Tenure.since` cell and no opener (`commit`, `oblige`, `succeed`, `tie`, `knot`) is a
    real, disclosed hole, not an absent declaration. MEASURED against the mapping it replaced: the
    two agree exactly (`hold: [confer, create_record]`, `contain: [move]`, the other five empty).

    ⚠ THE WALK FOLLOWS A REGISTERED EFFECT INTO THE MODULE'S OWN HELPERS (plan position `15`).
    `create_record`, `issue` and `petition` share ONE mint, `_mint_document`, and the `hold` it
    opens is constructed there rather than in any decorated body -- so a walk confined to the
    decorated function would have DROPPED `create_record` from `hold`'s openers the day the mint
    was shared, a derived fact going quietly wrong in the direction nobody reads. A call to a
    function defined at the top of the SAME FILE is walked as if inlined (transitively, each helper
    once); anything imported -- including a cross-file helper in a SIBLING `effects_*.py` -- is not
    this file's and is not walked. MEASURED after the change: `hold: [confer, create_record, issue,
    petition]`, every other kind unchanged.

    ⚠⚠ SEVEN FILES, NOT ONE, SINCE THE PHASE-4 PER-SUBSYSTEM SPLIT (2026-09-30). `effects.py` itself
    is now a thin aggregator -- no `@effect_for`, no `Tenure(...)` -- and every decorated function
    moved into one of its `effects_*.py` siblings (`files.effects_modules()`, discovered by name
    rather than hand-listed, `loop_modules`'s own lesson one split down). Each sibling is walked on
    its OWN parse tree, so `helpers` is per-file too: a decorated function's cross-file calls (to
    `effects_shared.py`'s `_operand`, `_decline_ascent`, `_new_oblige_term`, `_shift`,
    `_exercised_office`, `_oblige_term`) are not followed, because none of them construct a Tenure
    -- checked by hand against every shared helper's body, not assumed. Had one, a split confined to
    one file at a time would MISS it the same way a walk confined to `EFFECTS_PY` alone now misses
    everything; the day a shared helper is given a `Tenure(...)` call, this docstring's claim goes
    false and this function must walk `effects_shared.py` from every sibling that reaches it, not
    only from its own file."""
    openers: dict = {k: set() for k in TENURE_KINDS}

    for path in files.effects_modules():
        tree = ast.parse(path.read_text(encoding="utf-8"))
        helpers = {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}

        def _reached(fn, helpers=helpers) -> list:
            """`fn` and every module-level helper IN THIS SAME FILE it calls, transitively, each
            once. `helpers` is bound as a default argument so each closure keeps ITS OWN file's
            map rather than the loop variable's final value (the late-binding trap `/simplify`
            exists to catch)."""
            out, todo, seen = [], [fn], set()
            while todo:
                f = todo.pop()
                if f.name in seen:
                    continue
                seen.add(f.name)
                out.append(f)
                todo.extend(helpers[c.func.id] for c in ast.walk(f)
                            if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
                            and c.func.id in helpers)
            return out

        for node in ast.walk(tree):
            if not isinstance(node, ast.FunctionDef):
                continue
            verb = None
            for dec in node.decorator_list:
                if (isinstance(dec, ast.Call) and isinstance(dec.func, ast.Name)
                        and dec.func.id == "effect_for" and dec.args
                        and isinstance(dec.args[0], ast.Constant)):
                    verb = dec.args[0].value
            if verb is None:
                continue
            for call in (c for f in _reached(node) for c in ast.walk(f)):
                if not (isinstance(call, ast.Call) and isinstance(call.func, ast.Name)
                        and call.func.id == "Tenure"):
                    continue
                kind = None
                if len(call.args) > 3 and isinstance(call.args[3], ast.Constant):
                    kind = call.args[3].value
                else:
                    kind = next((kw.value.value for kw in call.keywords
                                if kw.arg == "kind" and isinstance(kw.value, ast.Constant)), None)
                if kind is not None:
                    openers.setdefault(kind, set()).add(verb)
    return {k: sorted(v) for k, v in openers.items()}


#: Computed ONCE, same discipline as `effects.py`'s own source not changing mid-process
#: (`_OFFICES_DOC`/`OFFICES_SEATS` in `rosters.py` cache their own derivation the same way).
#: Found uncached at the Phase-1 methodology close (2026-09-29, `/simplify`, EFFICIENCY and
#: SIMPLIFICATION lenses, convergent): all three call sites below re-read and re-parsed
#: `loop/effects.py` from scratch on every call, though the derivation "once instead of a second
#: copy" was the function's own whole premise -- the same discipline now applies to the
#: derivation's runtime cost, not only to the source file it replaces.
_OPENERS_FROM_EFFECTS = _derive_openers_from_effects()


def _load_verb_table() -> dict:
    import yaml as _y
    if not VERB_TABLE_YAML.exists():
        raise SystemExit(f"verb_table.yaml not found at {VERB_TABLE_YAML}")
    doc = load_yaml(VERB_TABLE_YAML.read_text())
    out = {}
    _release_domain: frozenset = frozenset()
    for r in doc["verbs"]:
        name = r["verb"]
        if name in out:
            raise SystemExit(f"verb_table.yaml: {name!r} appears more than once")
        # LOADER INVARIANT 10, VERB HALF (`04 §B.13 #10`, `04:470`): UNKNOWN KEYS ARE REJECTED.
        # A column is either one this loader reads or an annotation spelled `*_note`; anything else
        # is a column that silently does nothing, which is what `writes_grade:`, `writes_source:`,
        # `eligibility_substitution:`, `eligibility_sweep:` and `effect:` were until 2026-09-25.
        # ⚠ #10's OTHER CLAUSE -- *"a `scale:` key fails the load"* -- IS NOT ENFORCED, BECAUSE IT
        # IS ABOUT A DIFFERENT FIELD: the chain's retired per-module `scale:`, not the ruled
        # rung-kind column `VerbRow.scale` carries (see the comment on that field above).
        unknown = sorted(k for k in r if k not in _VERB_ROW_KEYS and not str(k).endswith("_note"))
        if unknown:
            raise SystemExit(
                f"verb_table.yaml: {name!r} carries unknown key(s) {unknown}. 04 §B.13 #10 -- a "
                f"row's keys are the ones this loader reads ({sorted(_VERB_ROW_KEYS)}) or an "
                "annotation spelled `*_note`; any other column is read by nothing.")
        # ⚠ `writes:` NOW TAKES TWO SHAPES (#358 rev.2 invariant 12). A mapping is degree-keyed;
        # a sequence is the flat form. The union feeds the Part D check below either way, so a
        # pair named in ANY branch is still validated against the matrix at load.
        raw_writes = r["writes"]
        by_degree: dict = {}
        if isinstance(raw_writes, dict):
            by_degree = {str(k): list(v or []) for k, v in raw_writes.items()}
            flat = tuple(dict.fromkeys(w for v in by_degree.values() for w in v))
        else:
            flat = tuple(raw_writes)
        raw_emits = r["emits"]
        emits_by_degree: dict = {}
        if isinstance(raw_emits, dict):
            emits_by_degree = {str(k): list(v or []) for k, v in raw_emits.items()}
            flat_emits = tuple(dict.fromkeys(e for v in emits_by_degree.values() for e in v))
        else:
            flat_emits = tuple(raw_emits)
        # ⚠ `emits_on_refusal:` TAKES TWO SHAPES TOO (plan position `19`, invariant 4's per-conjunct
        # half). A mapping is keyed by FAILABLE CLAUSE; a sequence is the flat form. The union is the
        # flat column either way, so every reader of *is this a refusal* sees the same kinds.
        raw_refusals = r["emits_on_refusal"]
        by_clause: dict = {}
        if isinstance(raw_refusals, dict):
            by_clause = {str(k): tuple(v or ()) for k, v in raw_refusals.items()}
            flat_refusals = tuple(dict.fromkeys(k for v in by_clause.values() for k in v))
        else:
            flat_refusals = tuple(raw_refusals)
        row = VerbRow(name, r["stratum"], tuple(r["eligibility"]), r["requires"],
                      flat, flat_emits,
                      flat_refusals, r["grade"],
                      str(r.get("scale") or "person").strip(),
                      str(r.get("contests") or "").strip(),
                      by_degree, emits_by_degree,
                      build_typed_requires(name, r.get("requires_typed")),
                      str(r.get("requires_typed_note") or "").strip(),
                      str(r.get("beneficiary") or "").strip(),
                      str(r.get("counterparty") or "").strip(),
                      refusals_by_clause=by_clause,
                      effect_decline_note=str(r.get("effect_decline_note") or "").strip(),
                      requires_decline_note=str(r.get("requires_decline_note") or "").strip())
        # THE COUNTERPARTY IS AN OPERAND THE ACT CARRIES, OR IT IS NOTHING. `opening_set` compares
        # it with the person; a name the typed cell does not BIND is absent from every Candidate,
        # so the comparison would pass silently and the rule would be a column nothing enforced.
        # ⚠ AN UNTYPED ROW MAY NAME ONE (`oblige`; `give` until `14`), AND IT MEANS SOMETHING ELSE
        # THERE: no cell binds it, so no Candidate carries it, and `opening_set` forms none -- the
        # row declares a second party the grammar cannot yet name, and a person does not mint an
        # act with that hole (`operands_for`'s rule, reached through the one column that says the
        # hole is there). The name must still be a `requires_operands` member, so a typo is refused
        # rather than silently making a verb unformable. A TYPED row keeps the stricter rule: a
        # counterparty its own cell does not bind is a typo, not a declaration.
        if row.counterparty and (
                row.counterparty not in REQUIRES_OPERANDS if row.requires_typed is None
                else row.counterparty not in row.requires_typed.operands()):
            raise SystemExit(
                f"verb_table.yaml: {name!r} names counterparty {row.counterparty!r}, which its "
                "`requires_typed:` cell does not bind (or, on an untyped row, which is no "
                "`requires_operands` member). A counterparty is compared with the person forming "
                "the Candidate, and only a bound operand is always carried.")
        # A row that declares `requires_typed: none` must SAY WHY. The three admissible reasons
        # are a well-formedness constraint on the Act (§F.24a: `issue`, `open_case` -- *"they
        # belong in the `Act` schema and are refused at construction"*), a `per act` cell, and an
        # operand the closed `requires_operands` roster has no name for. None of the three is
        # "nobody got to it", and a blank note cannot tell the two apart.
        if "requires_typed" in r and row.requires_typed is None and not row.requires_typed_note:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `requires_typed: none` and no "
                "`requires_typed_note:`. An untyped cell with no reason is indistinguishable "
                "from one nobody typed, which is the state W-A exists to end.")
        # LOADER INVARIANT 13 (`CAT-2`, phase-6 item `6d`). THE BENEFICIARY COLUMN, IN THREE
        # CHECKS -- and the third is the one that carries the ruling's content.
        #
        # (1) IT IS REQUIRED. A row without it is refused at load, so a verb cannot arrive
        #     carrying no declaration. `none` is how a row says the good accrues to no person the
        #     Candidate holds; a BLANK would say the same thing to `benefits_me` and nothing at
        #     all to a reader, which is the state `requires_typed_note` already exists to end.
        if "beneficiary" not in r:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares no `beneficiary:`. Every row must say who "
                f"the act is taken for the good of -- one of {sorted(BENEFICIARY_KINDS)}. "
                "`none` is the declaration for an act whose good accrues to a Record, an Office, "
                "a Site or a Rung; an ABSENT column would read as `false` for every verb, which "
                "is the UNKNOWN/False collapse `operands_for` refuses one level down.")
        # (2) IT IS ROSTERED. `beneficiary_kinds` is the closed set, in `rosters.yaml`, so a
        #     fifth carrier is a data edit argued for in the roster rather than a new string here.
        #     ⚠⚠ IT RAISES `SystemExit`, NOT `Unspecified`, AND THE FIRST VERSION HAD THAT
        #     BACKWARDS. This went through `require_member`, which raises `Unspecified` -- and
        #     this file's own `H-115` docstring codifies the opposite split: load-time refusals
        #     are CORRECTLY fatal `SystemExit`, while `Unspecified`/`ShapeGap`/`Forbidden`/
        #     `NoProducer` are the PER-ACT gap taxonomy. `corpus_run.run_case` catches that
        #     taxonomy, so a broken TABLE imported inside its try block was reported as ONE
        #     CASE's `status="DESIGN-GAP"` -- a whole-table defect attributed to a case, which is
        #     the mis-attribution `H-115` was raised to end, arriving through the new check.
        #     It was also invisible to `test_h115_...`, which counts `raise SystemExit` only.
        if row.beneficiary not in BENEFICIARY_KINDS:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `beneficiary: {row.beneficiary!r}`, which is "
                f"not in `beneficiary_kinds` ({sorted(BENEFICIARY_KINDS)}). CAT-2 -- the "
                "beneficiary resolves to a carrier a Candidate ALREADY holds (the actor, "
                "`subject`, or a named operand); a name outside the roster is a carrier nothing "
                "can resolve. Add it to rosters.yaml and argue for it there, never here.")
        # (3) AN OPERAND BENEFICIARY MUST BE CARRIABLE BY THIS ROW'S OWN CELL, AND THIS IS THE
        #     CHECK THAT KEEPS THE COLUMN HONEST. `CAT-2` killed option 1 -- derive the
        #     beneficiary from the operand binding -- by MEASURING that 24 of 38 verbs are
        #     untyped and can carry nothing whatever. A static column dodges that failure only
        #     while it declares carriers the row can actually hold: `beneficiary: to` on a verb
        #     whose cell never binds `to` is the same dead reference, moved into the column that
        #     was supposed to escape it, and it would resolve to `None` forever in silence.
        #     `actor` and `subject` are exempt BY CONSTRUCTION, not by leniency -- the first is
        #     structural on every Candidate (`operands_for` skips it for exactly that reason) and
        #     the second is a field on the carrier, so neither depends on a cell.
        if row.beneficiary in _OPERAND_BENEFICIARIES:
            req = row.requires_typed
            carriable = set()
            if req is not None:
                carriable = set(req.operands()) | set(req.needs())
            if row.beneficiary not in carriable:
                raise SystemExit(
                    f"verb_table.yaml: {name!r} declares `beneficiary: {row.beneficiary}` and its "
                    f"`requires_typed` cell neither binds nor admits that operand "
                    f"(carriable: {sorted(carriable) or 'nothing -- the row is UNTYPED'}). The "
                    "beneficiary would resolve to nothing for every candidate ever formed, which "
                    "is the dead reference CAT-2 measured option 1 dying of -- a static column "
                    "escapes it only while it names a carrier this row can hold.")
        if name == "release":
            _release_domain = frozenset(r.get("domain") or ())
        # The two keyed columns must agree on their band set, or a band writes with nothing to
        # report or reports with nothing written.
        if by_degree and emits_by_degree and set(by_degree) != set(emits_by_degree):
            raise SystemExit(
                f"verb_table.yaml: {name!r} keys `writes` on {sorted(by_degree)} and `emits` on "
                f"{sorted(emits_by_degree)}. A band in one and not the other is an outcome that "
                "either changes the world silently or reports a change it did not make.")
        # LOADER INVARIANT 12 (#358 rev.2 §B.13). The two shapes are NOT interchangeable, and
        # both directions are checked: a contested verb with a flat list is the `kill / wound`
        # defect, and an uncontested verb with a degree map is a verb claiming an outcome it
        # never resolves.
        if row.contests and not by_degree:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `contests: {row.contests}` and a FLAT "
                "`writes:`. Its writes must be keyed by Degree (#358 rev.2 §C.4) -- otherwise "
                "losing the contest writes exactly what winning it does, which is the defect "
                "that routes to the seam and then discards what the seam returned.")
        if by_degree and not row.contests:
            raise SystemExit(
                f"verb_table.yaml: {name!r} has a degree-keyed `writes:` and no `contests:`. "
                "Nothing resolves a degree for it, so no branch could ever be selected.")
        # ⚠ **INVARIANT 12 WAS ONE-SIDED AND THE OTHER SIDE IS THE SAME DEFECT.** The four checks
        # above read `writes:` only, so a row with a FLAT `writes:` (`[]` included), a DEGREE-KEYED
        # `emits:` and no `contests:` LOADED CLEAN and then raised `Unspecified` at the first act
        # that folded it -- `emits_at(None)` has nowhere to look. That is precisely what invariant
        # 12 exists to make unwritable, escaping through the column it did not read.
        # ⚠ FOUND BY BUILDING THE SIX INVESTIGATION ACTS (ED-FI-0009), WHOSE `writes:` IS `[]` BY
        # DESIGN -- a finding is a Claim minted at WITNESS, not a typed write -- so they are the
        # exact shape that slips through: keying their `emits:` on a Degree would have been
        # accepted at load and would have failed per-act, mid-corpus, as a design gap rather than
        # as the table defect it is. They ship with a FLAT `emits:` because nothing grades an
        # investigation act yet; this check is what makes that a decision rather than a habit.
        if emits_by_degree and not row.contests:
            raise SystemExit(
                f"verb_table.yaml: {name!r} has a degree-keyed `emits:` and no `contests:`. "
                "Nothing resolves a degree for it, so no branch could ever be reported -- and "
                "unlike the `writes:` case this used to load clean and raise at the first fold.")
        if row.contests and not emits_by_degree:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `contests: {row.contests}` and a FLAT "
                "`emits:`. Its emissions must be keyed by Degree for the same reason its writes "
                "are: a flat list reports the SAME outcome whichever way the contest went, which "
                "is `ID-9` -- a wound emitting `person.died`.")
        # EVERY `writes:` MUST BE A PART D ROW. Checked AT LOAD, not at the first act that uses
        # it: a verb naming an unmarked cell is a defect in the table, and finding it when some
        # case happens to exercise that verb makes it look like a defect in the case.
        for w in row.writes:
            kind, _, fld = w.partition(".")
            if (kind, fld) not in MATRIX:
                raise SystemExit(
                    f"verb_table.yaml: {name!r} writes ({kind}, {fld}), which is on no row of "
                    "write_matrix.yaml. §30: ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION. Rule "
                    "the Part D row first, then add the verb.")
        # §E4: eligibility is one of four kinds and NEVER `capability` -- asserted OVER THE TABLE,
        # not over the prose, which is §7.2's per-item rule for W3.
        for k in row.eligibility_kinds():
            if k == "capability":
                raise SystemExit(
                    f"verb_table.yaml: {name!r} is gated on `capability`. #353 §9.2 -- "
                    "'capability supplies dice and GATES NOTHING'. No verb exists only for "
                    "office-holders.")
            if k not in ELIGIBILITY_KINDS:
                raise SystemExit(
                    f"verb_table.yaml: {name!r} has eligibility kind {k!r}, which is not one of "
                    f"{ELIGIBILITY_KINDS}. §E4 admits exactly four and a fifth would be a new "
                    "way to make a verb unavailable -- which is a design change, not a table edit.")
        # The scale must be a rung kind, and `rung_kinds` owns which. An unrostered scale RAISES
        # rather than defaulting to `person`: a governance verb quietly filed at person scale is
        # the silent-wrong-answer shape this file refuses everywhere else.
        if row.scale not in RUNG_KINDS:
            raise SystemExit(f"verb_table.yaml: {name!r} has scale {row.scale!r}, which is not a "
                             f"`rung_kinds` member: {sorted(RUNG_KINDS)}")
        # The stratum must be one of the five, and the roster owns which five.
        if row.stratum not in STRATA:
            raise SystemExit(f"verb_table.yaml: {name!r} has stratum {row.stratum!r}, which is "
                             f"not one of rosters.yaml's {list(STRATA)}")
        # LOADER INVARIANT 9 (`04 §B.13 #9`, `04:469`): CONTEST PRIZES ⊆ THE SUBSYSTEM ROSTER. A
        # misspelled prize used to load clean, boot clean, and reach the seam's generic refusal at
        # first call naming no row (`manifest.registry.unclaimed_contest_prizes`'s docstring). The
        # roster, `contest_subsystems.prizes`, owns which prizes exist.
        if row.contests and row.contests not in _CONTEST_PRIZES:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `contests: {row.contests}`, which is not a "
                f"`contest_subsystems.prizes` key ({sorted(_CONTEST_PRIZES)}). 04 §B.13 #9 -- "
                "contest prizes are a SUBSET of the subsystem roster; an unclaimed prize resolves "
                "to no provider and the seam refuses generically, naming no row.")
        # LOADER INVARIANT 4 (`04 §B.13 #4`, F7, `04:461-464`): EVERY FAILABLE CLAUSE HAS A
        # REFUSAL KIND. A clause can fail if the row has a `requires` cell, or if any eligibility
        # alternative is other than `own` (which cannot decline). Such a row with an empty
        # `emits_on_refusal` would refuse by emitting a kind nobody declared.
        # ⚠ THE PER-CONJUNCT HALF OF F7 IS ENFORCED BELOW SINCE PLAN POSITION `19`, FOR A KEYED ROW.
        # It said *"NOT ENFORCED HERE ... that schema does not exist"* until `19` built the schema
        # for its first consumers (`levy`, `open_case`, `determine`, `issue`). A FLAT row is still
        # checked at row grain only (the block directly below): `restore`, `examine` and `surveil`
        # carry an `AllOf` of two and one flat kind, which is lawful -- a flat row DECLARES that all
        # its conjuncts refuse alike -- and moving them is not `19`'s.
        _failable = (row.has_precondition
                     or any(k != "own" for k in row.eligibility_kinds()))
        if _failable and not row.emits_on_refusal:
            raise SystemExit(
                f"verb_table.yaml: {name!r} has a failable clause (a `requires` cell, or an "
                f"eligibility other than `own`: {list(row.eligibility)}) and an empty "
                "`emits_on_refusal:`. 04 §B.13 #4 (F7) -- every failable clause has a refusal "
                "kind; a refusal with no declared kind is a fabricated emission.")
        # LOADER INVARIANT 4, PER-CONJUNCT HALF (plan position `19`; `04:465-468`, F7): A KEYED ROW
        # KEYS EXACTLY ITS FAILABLE CLAUSES. The clause set is DERIVED from the row, never listed:
        #   * `ELIGIBILITY_CLAUSE`  iff an eligibility alternative can decline (anything but `own`);
        #   * every NAMED top-level conjunct of its typed cell (`conjunct:`, `data/requires.py`) --
        #     and a keyed row with a precondition must be TYPED and name EVERY conjunct, because a
        #     predicate's conjuncts (`REQUIRES_PREDICATES`) live in `loop/`, which this loader may not
        #     import, so a keyed predicate row is a set of keys nothing here can check;
        #   * `WRITE_CLAUSE`         iff the row writes (an effect can decline, F9's `NoOpReceipt`);
        #   * `COUNTERPARTY_CLAUSE`  iff the row names a `counterparty:` (plan position `14`).
        # MISSING is a failable clause with no kind -- the fold would reach `refusal_for` and raise;
        # EXTRA is a kind for a clause that cannot fail, read by nothing (`ID-13`). A name on a FLAT
        # row is refused for the same reason: nothing keys it. A CONTESTED row may key its refusals
        # only to ONE kind: the seam's party gap (`loop/resolve.py::_party_gap_refusal`) is a refusal
        # point this schema has no clause for, and it emits the union. ONE refusal names every
        # defect found, so a table edit that breaks three things is told all three.
        _names = row.requires_typed.conjuncts() if row.requires_typed is not None else ()
        if by_clause or _names:
            _expected, _defects = set(_names), []
            if any(k != "own" for k in row.eligibility_kinds()):
                _expected.add(ELIGIBILITY_CLAUSE)
            if row.writes:
                _expected.add(WRITE_CLAUSE)
            if row.counterparty:
                _expected.add(COUNTERPARTY_CLAUSE)
            if not by_clause:
                _defects.append(f"names conjuncts {list(_names)} and keys no refusal to them")
            if row.has_precondition and (
                    row.requires_typed is None or not row.requires_typed.names
                    or None in row.requires_typed.names):
                _defects.append("keys its refusals, so its precondition must be a typed cell with "
                                "EVERY top-level conjunct named")
            # ⚠ NARROWED AT TELLING WORKPLAN `T4`: the party-gap refusal emits the UNION, which is
            # `ID-9` only if the union holds more than one kind -- a kind published for a conjunct
            # that did not fail. A contested row whose every key emits ONE kind (`tell`:
            # `news.untold` for `holds` and `hearer`) emits exactly that kind at the party gap too.
            if row.contests and len(row.emits_on_refusal) > 1:
                _defects.append("declares `contests:`, whose party-gap refusal no clause names, "
                                "and keys more than one refusal kind, so that refusal would emit "
                                "kinds for conjuncts that did not fail")
            _after_fold = set(_names) & {ELIGIBILITY_CLAUSE, WRITE_CLAUSE, COUNTERPARTY_CLAUSE}
            if _after_fold:
                _defects.append(f"names a conjunct after a fold clause ({sorted(_after_fold)})")
            _missing = sorted(_expected - set(by_clause)) if by_clause else []
            _extra = sorted(set(by_clause) - _expected)
            _empty = sorted(k for k, v in by_clause.items() if not v)
            if _missing:
                _defects.append(f"keys no refusal for the failable clause(s) {_missing}")
            if _extra:
                _defects.append(f"keys refusals for {_extra}, which is no failable clause of it")
            if _empty:
                _defects.append(f"keys an EMPTY refusal for {_empty}")
            if _defects:
                raise SystemExit(
                    f"verb_table.yaml: {name!r} " + "; ".join(_defects) + ". 04 §B.13 #4 (F7), "
                    "the per-conjunct half -- every failable clause has a refusal kind, and a key "
                    f"is a failable clause. Its failable clauses: {sorted(_expected)}.")
        out[name] = row
    # -----------------------------------------------------------------------
    # LOADER INVARIANT 6 (`04_CODE_ARCHITECTURE.md` PART D row 15, MECHANICAL at load):
    # *"`release` generic; the loader asserts its domain equals `tenure_kinds \ {contain}`"*.
    #
    # ⚠⚠ **IT RUNS AFTER THE LOOP, AND THAT IS THE WHOLE OF THE DIFFERENCE BETWEEN A CHECK AND A
    # CHECK THAT CAN OBSERVE ITS OWN SUBJECT'S ABSENCE.** The first writing sat INSIDE the row
    # loop behind `if name == "release"`, so deleting or renaming the row meant the check never
    # executed: the load succeeded and the vocabulary was open-without-close again, which is the
    # exact state row 15 grades MECHANICAL at load. §0.1 pt 2 applied one notch too narrowly — the
    # branch could see a wrong domain and not a missing verb. Found by the unit's own adversarial
    # pass. The tests would have caught the deletion (`len(VERB_TABLE) == 38`, the executed-set
    # pins), but the tests are not the load and the row's grade claims the load.
    #
    # ⚠ THE ASSERTION IS AGAINST THE ROSTER, WHICH IS WHY THE COLUMN IS DECLARED AND NOT DERIVED.
    # `contain` is excluded because it is the one Tenure kind whose subject may be a Rung (PART D
    # row 13) and whose end is a MOVE, not a release -- `_eff_move` closes the old leg and opens
    # the new one, so a releasable `contain` would let a person leave a place for nowhere. Every
    # other kind is an edge a person opened and must be able to end (T-m).
    #
    # This is the check `open-without-close in the vocabulary` names: add an eighth tenure kind to
    # `rosters.yaml` and forget its closer, and the load fails HERE rather than shipping a relation
    # nothing can end.
    #
    # ⚠ ROW 15's SECOND HALF -- `04:466-467`, *"every kind's OPENER set is declared too"* -- IS
    # BELOW, after this check: `_derive_openers_from_effects()`, an AST walk over
    # `loop/effects.py`'s own `Tenure(...)` construction sites (`OPENERS-DERIVE`, 2026-09-29;
    # `rosters.yaml`'s `tenure_kinds` row carried this mapping by hand before this and no longer
    # does). Declared-and-empty is REPORTED (`tenure_kinds_without_an_opener`), not refused.
    if "release" not in out:
        raise SystemExit(
            "verb_table.yaml: no `release` row. Loader invariant 6 (04 PART D row 15) is the "
            "check that `tenure_kinds \\ {contain}` all have a closer, and without the verb "
            "every one of them is an edge that can be opened and never ended -- the "
            "open-without-close state T-m refuses. Removing the verb is a design change and "
            "`registers/handoffs/architecture_meta_HANDOFF_NEXT.md` §2a rules against re-opening it.")
    # ⚠ `RELEASABLE_KINDS` AND NOT A SECOND `frozenset(TENURE_KINDS) - {"contain"}`. The
    # derivation lives once, in `data/rosters.py` beside the roster it reads; this is the
    # comparison against the verb table's DECLARED column, which is the whole point of the column.
    # The excluded kinds are READ OFF the derivation rather than spelled, so the message cannot go
    # stale when the exclusion grows (`contain`, and `reside` since plan position `19c`).
    if _release_domain != RELEASABLE_KINDS:
        raise SystemExit(
            f"verb_table.yaml: `release` declares domain {sorted(_release_domain)}, and "
            f"`tenure_kinds \\ {sorted(frozenset(TENURE_KINDS) - RELEASABLE_KINDS)}` is "
            f"{sorted(RELEASABLE_KINDS)}. Loader invariant 6 "
            "(04 PART D row 15) requires them equal: a kind in the roster and not in this "
            "domain is an edge that can be opened and never closed, and a kind here and "
            "not in the roster is a closer for a relation that does not exist.")
    # LOADER INVARIANT 6, SECOND HALF (`04 §B.13 #6`, `04:466-467`, `ID-14`): EVERY KIND'S OPENER
    # SET IS DECLARED. `_derive_openers_from_effects()` seeds every `TENURE_KINDS` member with an
    # empty list before it reads anything, so "a kind with no entry" is now impossible BY
    # CONSTRUCTION rather than checked -- the `set(_openers) != set(TENURE_KINDS)` refusal this
    # block carried before `OPENERS-DERIVE` (2026-09-29) tested a failure mode only a HAND-WRITTEN
    # roster could reach; deleted rather than kept unreachable (`CLAUDE.md` §0.1 pt 2 -- "an
    # assertion must be able to observe the failure it excludes"; 44 -> 43 `raise SystemExit`s
    # across the model set, `test_season_shape.py`'s own pinned count). What survives is the check
    # a derivation cannot rule out by construction: an opener naming a verb `verb_table.yaml` does
    # not have -- a typo or an orphaned `@effect_for` registration in `loop/effects.py`.
    _openers = _OPENERS_FROM_EFFECTS
    _stray = sorted((k, v) for k, vs in _openers.items() for v in (vs or []) if v not in out)
    if _stray:
        raise SystemExit(
            f"loop/effects.py: a `Tenure(...)` construction names opener(s) that are no verb: "
            f"{_stray}. 04 §B.13 #6 -- an opener is a row of verb_table.yaml.")
    # LOADER INVARIANT 2 (`04 §B.13 #2`, `04:459`): EVERY MATRIX ROW WITH `RES` HAS A PRODUCING
    # VERB -- or DECLARES that it has none, and why, in its `unproduced:` column. `04:1025` (PART
    # E step 2) records the literal invariant as unsatisfiable today; the column is what lets the
    # check run and stay honest in both directions: an undeclared orphan refuses, and so does a
    # declaration on a row some verb now writes, which would otherwise outlive its reason.
    _produced = _produced_pairs(out)
    for (kind, fld), mrow in MATRIX.items():
        if Step.RESOLVE not in mrow.steps:
            continue
        has_producer = f"{kind}.{fld}" in _produced
        if not has_producer and not mrow.unproduced:
            raise SystemExit(
                f"write_matrix.yaml ({kind}, {fld}) is written at RES and no verb writes it. "
                "04 §B.13 #2 -- a RES row has a producing verb, or declares `unproduced: \"<hole "
                "id or F-tag>: <reason>\"`.")
        if has_producer and mrow.unproduced:
            raise SystemExit(
                f"write_matrix.yaml ({kind}, {fld}) declares `unproduced:` and a verb writes it. "
                "04 §B.13 #2 -- the declaration is stale; delete it.")
    return out


def _produced_pairs(table: dict) -> set:
    """Every `Kind.field` some verb writes, in any Degree branch (`VerbRow.writes` is the union).
    One owner for invariant 2 above and `rows_without_a_producer` below."""
    return {w for v in table.values() for w in v.writes}


def tenure_kinds_without_an_opener() -> list:
    """Loader invariant 6's second half, as a REPORT: the tenure kinds whose DERIVED opener set
    (`_derive_openers_from_effects()`, an AST walk over `loop/effects.py`) is empty -- relations no
    act can open today. Reported, not refused: an unopenable kind may be correct for now, and
    which of them are holes is a judgement `rosters.yaml`'s `tenure_kinds` row comment records
    (`commit`/`oblige`/`succeed`/`tie`/`knot` when `OPENERS-DERIVE` replaced the hand-written
    mapping with this function; `succeed`/`tie`/`knot` since `commit` gained its opener at plan
    position `7a` and `oblige` at `17a` -- computed, not read off the roster, so neither needed an
    edit here to leave the list)."""
    return sorted(k for k, vs in _OPENERS_FROM_EFFECTS.items() if not vs)

VERB_TABLE: dict = {}          # filled after STRATA loads, at the bottom of the roster block

VERB_TABLE = _load_verb_table()


def act_key(verb: str, subject, operands) -> str:
    """WHAT AN ACT'S ID IS OF, AFTER ITS VERB: `H(seed, tick, actor, f"act:{verb}:{act_key}")`.
    The subject, and -- for a row whose cell binds a known-person operand beside `subject`
    (`TypedRequires.known_person_operands`: `tell`'s `to`, and since plan position `14` `give`'s) --
    that operand too, as `subject>to`.

    ⚠ TELLING WORKPLAN `T4`, AND IT IS MEASURED NECESSITY: one topic now forms one `tell` per person
    the teller knows, so two acts in one deliberation shared `(actor, verb, subject)` and therefore
    one id, and `state/acts.py` refused the second (`act id ... is already in the store`) on the
    first realm season. Every row that binds no such operand answers its subject alone, so its ids
    are byte-identical to before. ONE OWNER for both minting sites: `decision/choose.py::pack_scenes` and
    `loop/deliberate.py::_qualify_by_round` (`04 PART D row 35`: purpose uniqueness is a
    convention, and this is where it is kept)."""
    key = "" if subject is None else str(subject)
    row = VERB_TABLE.get(verb)
    ops = operands if isinstance(operands, dict) else {}
    if row is not None and row.requires_typed is not None:
        for n in row.requires_typed.known_person_operands():
            if ops.get(n) is not None:
                key += f">{ops[n]}"
    return key


def opportunity_key(verb: str, subject, operands) -> Optional[tuple]:
    """WHAT MAKES TWO ACTS ONE OPPORTUNITY, FOR THE ONCE-PER-SEASON FILTER: `(verb, subject)`, plus
    the counterparty where the row names one -- `(verb, subject, <the operand its `counterparty:`
    column names>)`. `None` for an act that names no subject: it has no opportunity to be the same as,
    so it is never recorded and never filtered (`loop/deliberate.py::_drop_what_was_already_done`).

    ⚠ TELLING WORKPLAN `T4b`, A DEFECT JORDAN NAMED. `T4` made one `tell` Candidate per known present
    hearer, but the filter keyed `(verb, subject)`, so once a topic was told to B it could never be
    told to D that season -- and a person can obviously tell several hearers. The key is the GENERAL
    rule for a row that names a `counterparty:`, read off the ROW'S COLUMN and never a verb name; `tell`
    and, since plan position `14`, `give` are the rows where it changes anything TODAY (`give` is typed
    and formable, its subject the Record and its counterparty `to` the receiver, one Candidate per
    person the giver knows: `decision/options.py::operand_bags`). `petition` and `issue` always have
    `to` == `subject` (a computed Candidate's one referent), so their key is unchanged. Where the
    counterparty IS the subject (`determine`, `oblige`) it adds nothing and is left out, so those
    keys are byte-identical to before.

    ONE OWNER, BOTH SITES: `loop/driver.py` (writes a realised act) and `loop/deliberate.py`
    (reads it) both call this, so the key cannot be spelled two ways (`CLAUDE.md` §8). It sits beside
    `act_key`, which reads the same operands for the act's id, and needs no `World` or carrier."""
    if not subject:
        return None
    row = VERB_TABLE.get(verb)
    ops = operands if isinstance(operands, dict) else {}
    other = ops.get(row.counterparty) if row is not None and row.counterparty else None
    if other is None or other == subject:
        return (verb, subject)
    return (verb, subject, other)


def _check_sparse_table(name: str, cells: dict, rows: "set|tuple", row_what: str,
                        cols: "set|tuple", col_what: str, row_law: str, col_law: str) -> dict:
    """THE THREE CHECKS A ROSTER-KEYED SPARSE TABLE NEEDS, IN ONE PLACE.

    `alignment` (axis x verb) and `pursuit_projection` (conviction x axis) are the same KIND of
    object — a mapping whose outer key names a roster member, whose inner keys name another
    roster's members, that may be sparse and may not be uniformly zero. Each check exists because
    the corresponding failure is SILENT: a cell on an unrostered outer key is never read and never
    reported; an inner key naming nothing is a weight on an option nobody can form; and an all-zero
    table makes the whole mechanism inert while passing every test, which is the dead-carrier defect
    #353 `:739-744` names.

    ⚠⚠ THE TWO LOADERS HAD THIS CHECK-FOR-CHECK, AND `_load_projection`'s DOCSTRING SAID SO — *"the
    exact shape `_load_alignment` uses one table over -- the rule lives once in kind, not in copy"*.
    Writing that down is not the same as doing it: §8 says the rule lives once, full stop, and a
    fourth check or a change to the all-zero test would otherwise have to be made twice to stay in
    step. The LAW STRINGS stay per-caller, because what a violation means differs by table."""
    for outer, row in cells.items():
        if outer not in rows:
            raise Forbidden(
                f"{name} names {row_what} {outer!r}, which is not in the roster", "rosters.yaml",
                needs=f"add it to the roster, or drop the row", law=row_law)
        unknown = sorted(set(row) - set(cols))
        if unknown:
            raise Forbidden(
                f"{name}[{outer}] names {len(unknown)} {col_what}(s) outside the roster: {unknown}",
                "rosters.yaml",
                needs="spell it as the roster spells it, or drop the cell", law=col_law)
    if not any(val for row in cells.values() for val in row.values()):
        raise Forbidden(
            f"the {name} table is all zeroes", "rosters.yaml",
            needs="a default with at least one non-zero weight",
            law="PLAN §W5 -- 'a zero matrix makes convictions inert, which is the dead-carrier "
                "defect #353 `:739-744` names, and it would pass every test while meaning nothing'")
    return cells


def _load_projection() -> dict:
    """`tables.pursuit_projection`, the 15x7 that maps a person's pursuits into axis space
    (IN-08's cells commit).

    ⚠⚠ **THIS TABLE EXISTS BECAUSE `pursuit_axes` USED TO DO TWO JOBS AND COULD DO NEITHER
    WELL.** Before `U3` the roster held four names -- `Precedent`, `self_preservation`,
    `suspicion`, `harm_borne` -- one of which is a CONVICTION and three of which are ad-hoc
    scalars, and §F2's `conviction[axis]` looked a person's weight up in that one index set.
    `pursuit_axes`'s own note called the conflation out and predicted this repair: *"THIRTEEN
    convictions projecting onto FOUR axes through a 13x4 matrix ... It is the likeliest thing to
    change when `H-46` closes."* It changed here, and `H-46` did NOT close -- Jordan, 2026-09-02:
    *"convictions roster and axes etc may be modified in future."*

    THREE CHECKS, each for a failure that would otherwise be SILENT, and each the exact shape
    `_load_alignment` uses one table over -- the rule lives once in kind, not in copy:
      * a conviction outside the roster is a row nobody projects FROM;
      * an axis outside the roster is a column nobody scores WITH;
      * an all-zero matrix makes every person's convictions project to the zero vector, which is
        `uniform`'s control arm shipped as the default -- the dead-carrier defect, one table along.

    ⚠ IT DOES NOT CHECK THAT ALL 15 x 7 CELLS ARE PRESENT. Sparse is lawful here: an unlisted pair
    reads `default_cell`. What is checked is that every cell NAMED is nameable -- which is what
    makes a HALF-DONE ROSTER SWAP an `ImportError` rather than a plausible score: a row still keyed
    on a retired name, or a column on a retired axis, refuses here at module scope."""
    cells = table("pursuit_projection")
    return _check_sparse_table(
        "pursuit_projection", cells, PURSUITS, "pursuit", PURSUIT_AXES, "axis",
        row_law=("§F2 -- a person's pursuits are weights over the roster. A projection row for a "
                 "pursuit nobody can hold is read by nothing"),
        col_law=("references/descriptor_registry.yaml: axis_roster single-owns the seven names; an "
                 "eighth is one edit there and a refusal here, never two rosters drifting apart"))


PURSUIT_PROJECTION = _load_projection()

# ⚠ NO `PROJECTION_DECLARED` HERE, AND ITS ABSENCE IS DELIBERATE. `ALIGNMENT_DECLARED` below
# exists because `ALIGNMENT` is REBOUND by `alignment_at()`'s sweep, so every arm must be
# built from an immutable baseline rather than from the previous arm. The projection has a
# declared `sweep:` on its row and NO `projection_at()` yet, so a frozen copy here would be a
# second 15x7 in memory that a reader assumes is wired to something because its sibling is.
# It comes back in the commit that adds the sweep, the way `ALIGNMENT_DECLARED` arrived with
# `ALIGNMENT_SWEEP`.
PROJECTION_DEFAULT_CELL = float(table_meta("pursuit_projection").get("default_cell", 0.0))


def _load_role_template_pursuits(rows: Optional[dict] = None) -> dict:
    """`tables.role_template_pursuits`, CHECKED AT LOAD, because its one read path cannot refuse.

    ⚠ THE VALIDATION STEP IN-08 OWES. `data/cast.py::loyalty` reads this table through
    `data/pursuits.py::to_axes`, which SKIPS a pursuit `PURSUIT_PROJECTION` has no row for -- the
    sparse default, correct for a person's map that `pursuit()` has already checked, and SILENT for
    this table, whose names nothing checks. A template still keyed on a retired name would project
    a plausible, smaller vector and `loyalty` would read it without a word. So the same three
    checks the two sibling tables get are run here, on the one owner of them
    (`_check_sparse_table`): an unrostered template, an unrostered pursuit, an all-zero table. `rows` is the table under test (default: the shipped one)."""
    return _check_sparse_table(
        "role_template_pursuits", table("role_template_pursuits") if rows is None else rows,
        roster("role_templates"),
        "role template", PURSUITS, "pursuit",
        row_law=("rosters.yaml: role_templates -- a template row nobody's faction can name is read "
                 "by nothing"),
        col_law=("references/descriptor_registry.yaml: pursuit_roster -- `to_axes` skips a pursuit "
                 "it has no projection row for, so a misspelt or retired name here would be a "
                 "silently smaller expectation vector, not an error"))


ROLE_TEMPLATE_PURSUITS = _load_role_template_pursuits()


def _derive_kind_verb() -> tuple:
    """`(KIND_VERB, EMITTED_KINDS)`, derived from every row's `emits:` and `emits_on_refusal:`.

    `EMITTED_KINDS` is every event kind some verb row can emit, success or refusal. `KIND_VERB`
    maps a kind to its verb ONLY where exactly one row emits it: a kind several rows emit names no
    single verb, so it maps to nothing rather than to whichever row happened to sort first. Both
    are read off the table once at load -- no kind or verb is listed here."""
    emitters: dict = {}
    for verb, row in VERB_TABLE.items():
        for kind in set(row.emits) | set(row.emits_on_refusal):
            emitters.setdefault(kind, set()).add(verb)
    kind_verb = {k: next(iter(vs)) for k, vs in emitters.items() if len(vs) == 1}
    return kind_verb, frozenset(emitters)


KIND_VERB, EMITTED_KINDS = _derive_kind_verb()

# Every kind some row emits ON REFUSAL (`emits_on_refusal:`), read off the table as `EMITTED_KINDS`
# is. A refusal reports an act that did not happen, so its claim is no deed
# (`queries/person_q.py::is_deed`).
REFUSAL_KINDS = frozenset(k for r in VERB_TABLE.values() for k in r.emits_on_refusal)

# Every kind a DEED claim can carry: emitted, and by no row on refusal (`is_deed`'s set).
DEED_KINDS = EMITTED_KINDS - REFUSAL_KINDS

# An authored alignment cell for an EVENT KIND rather than a verb is keyed `deed:<kind>` in the same
# axis row. Admitted only where `<kind>` is in `EMITTED_KINDS` (`_load_alignment`): a deed key for a
# kind no verb emits is a weight on an event nobody can see. None is authored today.
DEED_PREFIX = "deed:"


_DENSITY_LAW = ("IN-08 (`workplans/valoria_master_workplan_v9_part5.md`) -- every table verb carries "
                "a cell on each axis, or is listed in the declared `uncelled:` set with its reason; "
                "a verb nobody considered is not the same claim as a verb considered and left at "
                "zero, and only the first is refused")


def _check_alignment_density(cells: dict, uncelled: dict) -> None:
    """IN-08's DENSITY RULE, at load: each `VERB_TABLE` verb is either keyed on EVERY axis row
    (a number, or an explicit `null` -- "considered; no source, no lean") or named in `uncelled:`
    with a reason, and then keyed on NO axis.

    ⚠ WHY IT IS NEEDED, IN THE LOADER'S OWN WORDS: `_check_sparse_table` *"does not check that all
    ... cells are present"*, and that is right for the VALUES -- sparse is lawful. What it let
    through silently is a NEW VERB ROW that nobody celled: it scores 0.0 on every axis, which reads
    exactly like a verb considered and judged neutral. Every verb row added after IN-08 (IN-12's
    steps, IN-51, IN-32, PC-06 K-3) lands its cells or its `uncelled:` line, or this refuses,
    naming the verb and the axes it is missing."""
    if not isinstance(uncelled, dict):
        raise Forbidden(
            f"alignment `uncelled:` is a {type(uncelled).__name__}, not a mapping of verb -> reason",
            "rosters.yaml", needs="`uncelled: {<verb>: <reason>}`", law=_DENSITY_LAW)
    unknown = sorted(v for v in uncelled if v not in VERB_TABLE)
    if unknown:
        raise Forbidden(
            f"alignment `uncelled:` names {unknown}, which the verb table does not carry",
            "rosters.yaml", needs="spell it as `verb_table.yaml` does, or drop the line",
            law=_DENSITY_LAW)
    unreasoned = sorted(v for v, why in uncelled.items() if not str(why or "").strip())
    if unreasoned:
        raise Forbidden(
            f"alignment `uncelled:` gives no reason for {unreasoned}", "rosters.yaml",
            needs="a reason per verb -- the declaration IS the reason", law=_DENSITY_LAW)
    for verb in sorted(VERB_TABLE):
        keyed = [ax for ax in PURSUIT_AXES if verb in cells.get(ax, {})]
        if verb in uncelled:
            if keyed:
                raise Forbidden(
                    f"alignment: {verb!r} is declared `uncelled:` and is celled on {keyed}",
                    "rosters.yaml", needs="drop the cells or the `uncelled:` line", law=_DENSITY_LAW)
            continue
        if len(keyed) != len(PURSUIT_AXES):
            absent = sorted(ax for ax in PURSUIT_AXES if ax not in keyed)
            raise Forbidden(
                f"alignment: verb {verb!r} has no cell on axis(es) {absent} and is not in the "
                f"declared `uncelled:` set", "rosters.yaml",
                needs=f"a cell for {verb!r} on each of {absent} (`null` for no lean), or an "
                      f"`uncelled:` line naming it with its reason",
                law=_DENSITY_LAW)


def _load_alignment(cells: Optional[dict] = None, uncelled: Optional[dict] = None) -> dict:
    """§F2's `alignment(c.verb, axis)`, from `rosters.yaml`, with FOUR load-time checks.

    Each check exists because the corresponding failure would be SILENT. A cell naming a verb the
    table no longer carries is dead weight nothing reports; an axis outside the roster makes
    `axis_weight[axis]` unreachable; and an all-zero matrix -- PLAN §W5's named guardrail -- "would
    pass every test while meaning nothing", which is the dead-carrier defect #353 `:739-744`
    describes. The fourth is IN-08's density rule (`_check_alignment_density`). All four raise HERE
    rather than producing a plausible score later.

    A `deed:<kind>` key is admitted beside the verbs, for kinds in `EMITTED_KINDS` only (the same
    first check, one column wider). `cells` defaults to the roster table, and then `uncelled`
    defaults to the table's own `uncelled:` declaration and the density rule runs; a caller may
    pass another table to exercise the loader without touching the shipped one, and the density
    rule runs on it only if that caller passes an `uncelled` too.

    An explicit `null` cell is a considered zero: it satisfies the density rule and is DROPPED
    from the returned table, so every reader (`align`, the sweep, the scar) sees the sparse numeric
    table it always saw and reads `default_cell` for it."""
    if cells is None:
        cells = table("alignment")
        if uncelled is None:
            uncelled = table_meta("alignment").get("uncelled") or {}
    admitted = set(VERB_TABLE) | {DEED_PREFIX + k for k in EMITTED_KINDS}
    checked = _check_sparse_table(
        "alignment", cells, PURSUIT_AXES, "axis", admitted, "verb or `deed:<kind>`",
        row_law=("§F2 -- `axis_weight[axis] * alignment(verb, axis)` sums over the ROSTER. A cell "
                 "on an unrostered axis is never read and never reported"),
        col_law=("§E2 -- the verb table is the roster of verbs. A cell keyed on a verb that does "
                 "not exist is a weight on an option nobody can ever form; a `deed:` key for a "
                 "kind no verb emits is a weight on an event nobody can see"))
    if uncelled is not None:
        _check_alignment_density(checked, uncelled)
    return {ax: {k: v for k, v in row.items() if v is not None} for ax, row in checked.items()}

ALIGNMENT = _load_alignment()

# The immutable baseline. `ALIGNMENT` is REBOUND by a sweep; this is not, so every sweep point is
# built from the declared table rather than from the previous point (see `alignment_at`).
ALIGNMENT_DECLARED = {ax: dict(row) for ax, row in ALIGNMENT.items()}
ALIGNMENT_DEFAULT_CELL = float(table_meta("alignment").get("default_cell", 0.0))


def align(verb: str, axis: str) -> float:
    """§F2's `alignment(c.verb, axis)`. Sparse: an unlisted pair reads the table's own declared
    `default_cell`, never a literal here.

    ⚠ IT READS THIS MODULE'S `ALIGNMENT`, THE ONE BINDING. `alignment_at()`'s sweep rebinds
    `data.verbs.ALIGNMENT`, and `choose`'s score, the `H-146` refusal gate and the scar's
    `person_q._pursuits_violated_by` (via `elements_violated_by`) all call
    this function, so one rebind moves every reader. A second binding anywhere (a `from .verbs
    import ALIGNMENT` in a reader module) would be a stale snapshot the rebind never reaches."""
    return float(ALIGNMENT.get(axis, {}).get(verb, ALIGNMENT_DEFAULT_CELL))


def celled_verbs() -> frozenset:
    """The verbs with AT LEAST ONE CELLED AXIS: a non-zero cell in the live `ALIGNMENT` binding.

    ⚠ G-1 (2026-10-06, [medium; Jordan to correct]) IS ITS FIRST READER: R-06 and R-08 count only
    candidates whose verb has a celled axis, because a verb with none -- an `uncelled:` verb such as
    `tell`, or one whose every cell is a considered `null` -- scores 0.0 for every person by
    construction, and its candidates can neither discriminate nor be a tie the ranking failed to
    break. Read off `ALIGNMENT`, the binding the sweep rebinds, so under `uniform` every verb is
    celled -- the control arm's own answer."""
    return frozenset(v for row in ALIGNMENT.values() for v, val in row.items()
                     if val and not str(v).startswith(DEED_PREFIX))


def align_kind(kind: str, axis: str) -> float:
    """The alignment of an EVENT KIND on an axis: an authored `deed:<kind>` cell if one exists, else
    the alignment of the one verb that emits the kind (`KIND_VERB`), else 0.

    Read by `deeds_judged`/`deed_valence`; under `uniform` every deed key is celled 1.0. Placed
    beside `align` so the verb-keyed and kind-keyed readers share one table and one rebind."""
    cell = ALIGNMENT.get(axis, {}).get(DEED_PREFIX + kind)
    if cell is not None:
        return float(cell)
    verb = KIND_VERB.get(kind)
    if verb is None:
        return 0.0
    return align(verb, axis)


def rows_without_a_producer() -> dict:
    """Every `social: true` row that no verb writes — §7.2's rule for W2, as a REPORT.

    ⚠ IT IS A FLAG AND NOT A DELETE INSTRUCTION, and the W2 audit is why. W2 retired six rows on
    this rule; applied literally the same rule condemns `(Person, pursuits)`, which #353 §9.3
    REQUIRES ("moved by argument and consequence"). So a producerless row is one of two different
    things and the report cannot tell them apart:

      * A HOLE — the verb is missing. `(Person, pursuits)` has no verb because Part E carries
        no argument verb, which is a gap in Part E, not a reason to delete a row #353 mandates.
      * DEAD — nothing in the design produces it. That was the six.

    Distinguishing them is a judgement, so this reports and a human decides. What it MUST NOT do
    is what the first reading of the rule did: delete on sight. `emits:` was parsed and never read
    by anything until this function, so the column the retirement rested on was inert data."""
    produced = _produced_pairs(VERB_TABLE)
    out = {}
    for (kind, fld), row in MATRIX.items():
        if row.social is not True:
            continue                      # the world may write it; a verb is not required
        if f"{kind}.{fld}" not in produced:
            out[(kind, fld)] = row.emits
    return out

# From `rosters.yaml`, not a literal: the three points ARE a definition -- each names a claim
# the sweep compares -- so Jordan's no-hardcoding ruling reaches them. The guard caught this
# as a literal tuple and was right to; it is one of the few hits that was not mechanism.
ALIGNMENT_SWEEP = tuple(table_meta("alignment")["sweep"])

def alignment_at(point: str) -> dict:
    """`H-66`'s three sweep points. `rosters.yaml` declares the SET; this is the transform.

    ⚠ `uniform` IS THE CONTROL, and naming it so is the point. Every cell equal makes
    `SIGMA_axis conviction[axis] * alignment(verb, axis)` the same for every candidate, so
    convictions cannot discriminate at all -- a verdict that does NOT move between `declared` and
    `uniform` is a verdict the table was never deciding. §0.1 point 4: a number without a control
    is not a measurement, in EITHER direction.

    `sign_only` discards the magnitudes and keeps the signs, which separates "the table's
    DIRECTIONS are load-bearing" from "its INVENTED NUMBERS are". Since the numbers are declared
    invented, that separation is the one worth having."""
    require_member(
        point,
        ALIGNMENT_SWEEP,
        f"{point!r} is not an alignment sweep point",
        "H-66",
        law="§G -- declare it, default it, sweep it. A fourth point is a fourth claim")
    # ⚠ EVERY POINT IS BUILT FROM `ALIGNMENT_DECLARED`, NEVER FROM `ALIGNMENT`. A sweep works by
    # rebinding `ALIGNMENT`, so a transform reading the live global transforms whatever the last
    # point left: `alignment_at("sign_only")` after `uniform` returned sign(1.0) == 1.0 — i.e.
    # uniform again — and the sweep reported two arms as one. The baseline is captured at import
    # and never rebound, which is what makes the three points independent.
    if point == "declared":
        return {ax: dict(row) for ax, row in ALIGNMENT_DECLARED.items()}
    if point == "uniform":
        # ⚠ EVERY (verb, axis) PAIR, NOT EVERY LISTED CELL, and the difference is the whole
        # control. The first version returned `{v: 1.0 for v in row}`, which left UNLISTED pairs
        # falling through `align()` to `default_cell = 0.0` — so a verb absent from an axis still
        # scored differently from one present on it, convictions could still discriminate, and
        # `P31` passed under the "control". The test's own observability check caught it: a
        # control that the probe survives is not a control (§0.1 point 2).
        # The deed keys too: `align_kind` reads a `deed:<kind>` cell first, so under the control a
        # kind several rows emit (no `KIND_VERB`) reads 1.0 like every verb, not 0.0.
        return {ax: {**{v: 1.0 for v in VERB_TABLE},
                     **{DEED_PREFIX + k: 1.0 for k in EMITTED_KINDS}} for ax in PURSUIT_AXES}
    return {ax: {v: (1.0 if w > 0 else -1.0 if w < 0 else 0.0) for v, w in row.items()}
            for ax, row in ALIGNMENT_DECLARED.items()}

