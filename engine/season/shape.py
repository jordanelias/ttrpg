"""PR #353's idealized code shape (`ARCHITECTURE.md`), implemented faithfully enough to RUN.

REVISION 2. Revision 1 was attacked by a read-only antagonist that never saw its reasoning,
and the fidelity claim did not survive. Every correction below is recorded rather than
quietly applied, because the correction record is what makes the rest readable.

SCOPE (ARCHITECTURE.md S0.1, and Jordan 2026-09-01): the ONLY admissible source is the design
chain PR #337 -> now. Nothing under engine/, no subsystem sim/, and no decision ratified
before #337 is authority. Where ARCHITECTURE.md differs from #350/#351, ARCHITECTURE.md wins.

WHAT REVISION 2 RETRACTS
  1. THE PARTITION WAS INVENTED. Rev 1 declared twelve `social:` rows. ARCHITECTURE.md
     supplies exactly ONE (`(Tenure, until) = false`, S15.3) and S30.1 declares two MISSING.
     Rev 1's invented rows included `(Person, convictions)` and `(Person, beliefs)` -- the
     precise keys the in-chain #351 instrument marks DELIBERATELY ABSENT and pins with a
     regression test, because adding them turns a real gap into a PASS. Rev 2 carries only
     rows that are IN-CHAIN or DERIVABLE FROM S30's matrix by construction, each tagged with
     its provenance, and refuses everything else.
  2. `witness()` PASSED A FALSE DRIVER. It declared `driver="Act"` for a deposit caused by an
     Event, which is the one site where the gate would otherwise have fired.
  3. THE GATE WAS OPT-IN. `record_kind`/`fieldname` were optional, so omitting two kwargs
     silenced L4 entirely -- and CENSUS passed an `apply` that mutated nothing, recorded as
     admitted. S30.2 calls exactly that "worse than no gate".
  4. `contest()` WAS THE SECOND RESOLVER. It hardcoded a band with no margin, guarded the
     demote-only veto with dead code, and named THE MOST RECENT UNRELATED EVENT as its cause.
     S27.2 is the design's highest-value refusal and rev 1 broke it inside the seam.
  5. THE BUDGET WAS AN ENGINE TRUNCATION. S26 types `budget : (Person, View) -> int` with NO
     World; rev 1 gave it a World, so `choose` could not ask its own budget and the engine
     silently discarded the tail. That is "an engine deciding a person's options", which is L1.
  6. THREE CONSTANTS SAT IN BODIES -- a wear rate uniform across every site kind (the silent
     default S42.2.1 names by name), a `//60`, and `confidence=1`.
  7. `sense()` RETURNED A CONSTANT ZERO for `standing`, the one scalar S18.2 defines and no
     section computes.
  8. THE GAP TAXONOMY SPLIT ONE CONDITION ACROSS TWO KINDS (an unmarked cell raised Forbidden
     in one place and Unspecified in another).
  9. NINE MECHANISMS WERE CLAIMED MECHANICAL AND WERE CONVENTIONAL. Named at their sites.
 10. THIRTEEN THINGS THE SPEC REQUIRES WERE ABSENT -- the log content hash, sum-then-clamp-once,
     the five strata, the Ob>2xPool gate, L5's crossing emission, T5's carry chain, T6's
     dispensation, `hold` 1-per-object cardinality, S15.3's causation rule, the presence index
     and five witness channels, the boot manifest, the View `K` cap, and S54 item 7's
     `transfer` precondition on which S54.1's close rule explicitly depends.

FIDELITY RULES -- what makes a gap a finding rather than an artifact of this file:
  1. Where ARCHITECTURE.md SPECIFIES a mechanism, implement it as specified.
  2. Where it NAMES a mechanism and does not specify it, raise `Unspecified`. S42.2.1: "the
     honest behaviour is to REFUSE, not to pick a plausible number."
  3. Where the shape structurally FORBIDS what a case needs, raise `Forbidden`, naming the law.
  4. Where no step produces a change a case needs, raise `NoProducer`.
  5. Where two in-chain documents specify incompatible things, raise `Collision`.
  6. THE LAWS ARE ENFORCED BY CONSTRUCTION. Where a law is only a convention, the code SAYS SO
     at the site -- S34: "overstating this column is the failure mode"; S47: "a false claim of
     enforcement is worse than none, because it stops the next reader from checking."
"""

from __future__ import annotations

import enum
import hashlib
import sys
from dataclasses import dataclass, field, fields as dc_fields
from typing import Any, Callable, Optional

from .data import files
from .gaps import (
    Collision, Forbidden, Ineligible, InstrumentDefect, NoProducer, ShapeGap, Ungraded,  # noqa: F401
    Unowned, Unspecified, expect_refusal,
)
from .state.ids import H, ROOT
from .trace_log import TRACE


# ===========================================================================
# S48 -- FIXED POINT; W8 -- THE MATTER ECONOMY. BOTH EXTRACTED, step 3 of the decomposition.
#
# `Fixtures`, `_load_matter_tables`, `WEAR_RATES`/`BAND_FLOORS`/`SUBSISTENCE_WEIGHTS`/
# `SITE_YIELD`, and `DEFAULT_FIXTURES` all now live in `season.data.fixtures`, in that same
# order (`_load_matter_tables` sits between the class and the baseline instance there too --
# `DEFAULT_FIXTURES` reads three of its values off `rosters.yaml` and cannot be built before they
# load; see that module's docstring). Imported here so every bare use of these names further down
# this file keeps resolving, and so `S.<name>` keeps resolving for the harness and tests: this is
# a re-export, not a second definition.
# ===========================================================================

# ===========================================================================
# S23/S30 -- THE WRITE MATRIX; THE ROSTERS -- BOTH EXTRACTED, step 2 of the decomposition.
#
# `Step`, `WriteClass`, `MatrixRow`, `MATRIX` and everything that loads `write_matrix.yaml` now
# live in `season.data.matrix`. Every roster/table reader and everything that loads
# `rosters.yaml` -- `roster`, `table`, `office_faction`, `title_domain`/`title_rank`, and the
# roster constants below -- now live in `season.data.rosters`. Both are imported here so every
# bare use of these names further down this file keeps resolving, and so `S.<name>` keeps
# resolving for the harness and tests: this is a re-export, not a second definition.
#
# TWO THINGS STAYED AT STEP 2, BOTH ADJUDICATED AT THAT MOVE, AND BOTH HAVE SINCE LEFT -- the
# sentence is kept in its corrected form because BOTH RULINGS STILL HOLD; only the addresses
# moved. `MATRIX_REFUSAL_LAW` goes WITH ITS ONLY READER, the gate in `World`, and is therefore in
# `season.state.world` since step 4; it is a loop over a fix, not a definition, and filing it with
# the matrix would invite editing it as one. `rows_without_a_producer` goes WITH `VERB_TABLE`,
# which it reads, and is therefore in `season.data.verbs` since step 3.
#
# ⚠ THIS PARAGRAPH SAID "STAYS ... IN `shape.py`" AND WENT FALSE WITHOUT ANYTHING CHANGING ITS
# MIND, TWICE -- at step 3 and again at step 4, the second time in the same commit that moved the
# thing. Nothing catches it: the file still exists and every gate stays green. WRITE THE RULE, NOT
# THE ADDRESS. A ruling recorded as a location is a claim that expires silently at the next move.
# ===========================================================================

from .data.matrix import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    ASSUMPTIONS_USED, MATRIX, MATRIX_RETIRED, MatrixRow, PARTITION_ASSUMED, STEP_CLASS, Step,
    WRITE_MATRIX_YAML, WriteClass, _STEP_CLASS, _STEP_OF, assume_partition_row, matrix_row,
    partition_lookup,
)
from .data.rosters import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    BODY_FACTION, BODY_FUNCTION, CLAIM_SOURCES, CLAIM_SUBJECT_RULES, COMBAT_BANDS,
    CONVICTION_AXES, FACTIONS, FELLED, OBSERVATION_DEPOSIT_MODES, PERSON_PREDICATES,
    QUESTION_AGGREGATION, QUESTION_SOURCES, REMIT_ACTS, ROLE_TEMPLATE_OF, ROSTERS_YAML,
    RUNG_KINDS, SCENE_PACKING_RULES, STRATA, TENURE_KINDS, TITLE_DOMAINS, UNTOUCHED,
    VIEW_BUILDER_RULES, WITNESS_CHANNELS, WOUND_HARM_MODELS, WOUNDED, _ROSTERS, _TABLES,
    load_yaml, office_faction, roster, roster_map, table, table_meta, title_domain, title_rank,
)
from .data.requires import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    REQUIRES_FORMS, REQUIRES_OPERANDS, REQUIRES_FORM_NEEDS, _Unknown, UNKNOWN, Observation,
    Verdict, _as_number, _bound, COMPARATORS, REQUIREMENT_TYPES, requirement_form, Requirement,
    Existence, ScalarThreshold, ContainPath, Relation, OwnLedger, AllOf, TypedRequires, _observe,
    evaluate, binding_of, binding_from_act, REQUIRES_STEMS, LEDGER_DERIVED_STEMS,
    _require_known_stem, _build_clause, build_typed_requires,
)
from .data.verbs import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    VERB_TABLE_YAML, ELIGIBILITY_KINDS, VerbRow, _load_verb_table, VERB_TABLE, _load_alignment,
    ALIGNMENT, ALIGNMENT_DECLARED, ALIGNMENT_DEFAULT_CELL, rows_without_a_producer,
    ALIGNMENT_SWEEP, alignment_at, NO_PRECONDITION,
)
from .data.fixtures import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    Fixtures, _load_matter_tables, WEAR_RATES, BAND_FLOORS, SUBSISTENCE_WEIGHTS, SITE_YIELD,
    DEFAULT_FIXTURES,
)
from .state.carriers import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    Act, Candidate, Claim, Event, Office, Person, Proposition, Question, Record, Rung, Scene,
    Sensation, Site, StateChange, Tenure, View, matrix_rows_without_a_field,
)
from .state.world import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    MATRIX_REFUSAL_LAW, World, _TenureView, _entity_digest,
)
from .queries import world_q  # noqa: F401 -- `Query` binds its eleven functions as staticmethods
from .queries.readers import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    LedgerReader, WorldReader,
)
from .queries.world_q import occasioned_by, questions_for  # noqa: F401 -- re-exported, as above
from .loop.effects import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    EFFECTS, _eff_confer, _eff_convene, _eff_create_record, _eff_destroy_record, _eff_kill,
    _eff_move, _eff_revoke, _eff_transfer, _eff_utter, _eff_work, _operand, effect_for,
)
from .loop.predicates import (  # noqa: F401 -- re-exported, as above
    REQUIRES_PREDICATES, _req_confer, _req_convene, _req_dispatch, _req_revoke,
    highest_title_rank, in_holdings, requires_predicate, titles_held, under_purview,
)

# ===========================================================================
# THE `requires` GRAMMAR -- W-A. ONE DECLARATION, THREE READERS.
#
# EXTRACTED, step 3 of the decomposition (a PURE MOVE): the grammar itself -- `REQUIRES_FORMS`/
# `REQUIRES_OPERANDS`/`REQUIRES_FORM_NEEDS`, the third truth value (`_Unknown`/`UNKNOWN`),
# `Observation`, `Verdict`, the seven-form machinery (`requirement_form`, `Requirement` and its
# five `@requirement_form` classes including `OwnLedger`), the conjunction `AllOf`, the cell
# wrapper `TypedRequires`, the one evaluator (`evaluate`), the one binding pair (`binding_of`/
# `binding_from_act`), and the loader (`_build_clause`/`build_typed_requires`) -- now lives in
# `season.data.requires`. See that module's docstring for the ordering constraint the split
# creates (`_build_clause` needs every `@requirement_form` registered before `verb_table.yaml`
# loads) and how it is satisfied structurally rather than by file position.
#
# `04_CODE_ARCHITECTURE.md` §F.24a: *"`F.24` said 'assumed: a small typed predicate grammar' and
# supplied none... The 32 `requires` cells in the executable chain are the specification, and
# reading them yields SEVEN forms."*
#
# THE THREE READERS, and the reason this is worth doing at all:
#   1. THE FOLD (`SeasonDriver._fold`), through `WorldReader` -- §E2's `requires` against the
#      world the predecessors left.
#   2. THE PERSON (`belief_contradicts`), through `LedgerReader` -- §F1 clause 4, the SAME cell
#      asked of one person's OWN claims and of nothing else.
#   3. `resolvable_verbs()` -- *can the fold carry this verb through RESOLVE at all*.
#
# `WorldReader` AND `LedgerReader` STAY HERE, DELIBERATELY -- adjudicated at the move. They are
# READERS, `queries/` territory at a later step, and the grammar they serve asks only
# `reader.read(subject, predicate)`; moving a reader into the grammar module would give the
# grammar an opinion about where its answers come from. Both import `UNKNOWN` back from
# `season.data.requires` below; imported here so every bare use of the grammar's names further
# down this file keeps resolving, and so `S.<name>` keeps resolving for the harness and tests --
# this is a re-export, not a second definition.
# ===========================================================================

# ===========================================================================
# THE TWO READERS -- EXTRACTED, step 5 of the decomposition.
#
# `WorldReader` and `LedgerReader` now live in `season.queries.readers`. Step 3 left them here
# deliberately and said why: they are READERS, and the grammar they serve asks only
# `reader.read(subject, predicate)`, so filing a reader with the grammar would give the grammar an
# opinion about where its answers come from. It also said where they were going -- `queries/`, "at
# a later step" -- and this is that step.
#
# THE RULE, NOT THE ADDRESS (the correction step 4 had to make twice): a reader is filed by WHAT
# IT READS, not by who calls it. `WorldReader` reads the world and the ACTOR'S OWN ledger and
# nothing else; `LedgerReader` reads one person's claims and takes no `World` at all. Both answer
# `UNKNOWN` where they cannot resolve, which is the grammar's third truth value.
#
# Imported at the top of this file so every bare use further down keeps resolving, and so
# `S.WorldReader` keeps resolving for the harness and tests: a re-export, not a second definition.
# ===========================================================================
# `_require_known_stem`, `_build_clause` and `build_typed_requires` -- the loader that turns a
# `verb_table.yaml` cell into a `Requirement` -- now live in `season.data.requires` (step 3),
# imported back at the top of this file. `season.data.verbs._load_verb_table` calls
# `build_typed_requires` directly (it imports `season.data.requires` itself); this re-export
# exists only so `S.build_typed_requires` keeps resolving for the harness and tests.



# ===========================================================================
# PART E, LOADED FROM DATA -- W3. THE RESOLVER'S BODY.
#
# EXTRACTED, step 3 of the decomposition (a PURE MOVE): `VerbRow`, its loader
# (`_load_verb_table`/`VERB_TABLE`), the load-time constants a row checks against
# (`VERB_TABLE_YAML`, `ELIGIBILITY_KINDS`), and the alignment table's loader
# (`_load_alignment`/`ALIGNMENT`) now live in `season.data.verbs`. See that module's docstring
# for the two-phase `VERB_TABLE` assignment and why it is preserved unchanged, and for why
# `align()` (below, unmoved) still sees a sweep's rebind of `S.ALIGNMENT`.
#
# #353 types `resolve : (Act[], World) -> Event[]` and never says what any verb DOES. That is
# defect `D20`: with no table, every act needed a hand-written `effect` lambda, and A LAMBDA PER
# ACT IS A SECOND RESOLVER -- the thing §27.2 forbids. `verb_table.yaml` is the body.
#
# Imported here so every bare use of these names further down this file keeps resolving, and so
# `S.<name>` keeps resolving for the harness and tests: this is a re-export, not a second
# definition.
# ===========================================================================



# `_load_matter_tables` / `WEAR_RATES` / `BAND_FLOORS` / `SUBSISTENCE_WEIGHTS` / `SITE_YIELD` /
# `DEFAULT_FIXTURES` moved to `season.data.fixtures`, and `ALIGNMENT_DECLARED` /
# `ALIGNMENT_DEFAULT_CELL` moved to `season.data.verbs` (step 3, both imported back at the top of
# this file). `matrix_rows_without_a_field` moved to `season.state.carriers` at step 4, WITH the
# dataclasses it inspects via `globals()` -- it reads the module it is written in, so it travels
# with them or it silently reports every kind `unmodelled`.




# `rows_without_a_producer` moved to `season.data.verbs` (step 3) -- it reads `VERB_TABLE`, which
# moved with it in the same step, which is why it did not move with the write matrix in step 2.
# Imported back at the top of this file.



# ===========================================================================
# PART II -- THE PRIMITIVES
#
# EXTRACTED, step 4 of the decomposition (a PURE MOVE): the sixteen carriers -- `Tenure`,
# `StateChange`, `Event`, `Claim`, `Sensation`, `View`, `Question`, `Candidate`, `Scene`, `Act`,
# `Person`, `Site`, `Record`, `Proposition`, `Office`, `Rung` -- now live in
# `season.state.carriers`, together with `matrix_rows_without_a_field`, whose `globals()` lookup
# has to run in the module the classes are written in. See that module's docstring.
#
# Imported at the top of this file so every bare use of a carrier further down keeps resolving,
# and so `S.Person` keeps resolving for the harness and tests: this is a re-export, not a second
# definition.
# ===========================================================================


# ===========================================================================
# S45.1 -- DECLARE `World` FIRST
#
# EXTRACTED, step 4 of the decomposition (a PURE MOVE): `World`, the read-only tenure
# concatenation `_TenureView`, the per-entity digest `_entity_digest` that `content_hash` folds,
# and `MATRIX_REFUSAL_LAW` -- the table naming WHICH LAW refuses at each closed cell -- now live
# in `season.state.world`. See that module's docstring for why the refusal table travels with its
# reader rather than with the matrix, and for the read/write-asymmetry guard (§0.1 point 1) that
# `_TenureView` + `World.tenures` + `add_tenure` + `_rehome` form and that must stay whole.
#
# S45.1's ordering claim is now carried by the IMPORT rather than by file position, and it is
# stronger for it: `World` is defined in a module that imports the carriers and nothing above
# them, so nothing reading the world can be written before it -- `queries`, `decision` and `loop`
# are later steps and none of them may be imported there.
#
# Imported at the top of this file so every bare use of `World` further down keeps resolving, and
# so `S.World` keeps resolving for the harness and tests: a re-export, not a second definition.
# ===========================================================================


# ===========================================================================
# S17 -- QUERY. THE SIDE COLUMN IS THE ENFORCEMENT.
# ===========================================================================

class Query:
    # ---- resolver-side: World FIRST, always -----------------------------
    #
    # EXTRACTED, step 5 of the decomposition: the eleven are MODULE FUNCTIONS in
    # `season.queries.world_q` now, and the lines below are BINDINGS to them, not copies --
    # `Query.parent_of is world_q.parent_of` is true, so there is exactly one owner of each rule
    # and EVERY `Query.<world-first>` call site resolves to the moved body unchanged — the property,
    # not a count. A bare "73" stood here and no instrument reproduced it (occurrences, matching lines
    # and actual calls all differ, as do `engine/season/` and the repo): the two-bases error §0.1 pt 5
    # already records once.
    #
    # `04_CODE_ARCHITECTURE.md` §A.3 row 2 is why the split is BY MODULE and not by first
    # parameter: *"in one class, a person-side function calls a resolver-side one with no import
    # to scan."* The class survives one more step only as the call-site facade; it goes at step 7,
    # when the four person-side statics below become `decision`'s module functions -- and
    # `decision` is the module that may not name `World` at all (AX-2).
    parent_of = staticmethod(world_q.parent_of)
    descendants = staticmethod(world_q.descendants)
    r1_aggregate = staticmethod(world_q.r1_aggregate)
    aggregate_guard = staticmethod(world_q.aggregate_guard)
    single_holder_counter = staticmethod(world_q.single_holder_counter)
    commit_count_guard = staticmethod(world_q.commit_count_guard)
    lateral = staticmethod(world_q.lateral)
    verbs = staticmethod(world_q.verbs)
    hold_force = staticmethod(world_q.hold_force)
    judging_set = staticmethod(world_q.judging_set)
    presence = staticmethod(world_q.presence)

    # ---- person-side: takes the ASKER; own interior only ----------------
    @staticmethod
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

    @staticmethod
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

    @staticmethod
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

    @staticmethod
    def entrenchment(p: Person, seasons_held: int, scale: int, span: int) -> int:
        TRACE.query("entrenchment", "person")
        return min(scale, (seasons_held * scale) // span)


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


def resolvable_verbs() -> frozenset:
    """The verbs the fold can actually carry through RESOLVE: no precondition, or a precondition
    some `REQUIRES_PREDICATES` entry evaluates.

    COMPUTED, NEVER LISTED. A caller narrowing an option set to these is not authoring a roster --
    it is asking the fold what it can execute, and the answer moves when `verb_table.yaml` or the
    predicate registry moves. W3 measured 12 of 32; this is that measurement as a function, so a
    probe can report both numbers instead of hardcoding either.

    THREE GATES: a precondition the fold can evaluate, an effect for whatever it writes, and NOT
    routing to a contest — a contesting verb's resolution is the seam's, and the seam does not
    return yet (`H-31`, `W7`)."""
    out = set()
    for v, row in VERB_TABLE.items():
        # ⚠ BOTH GATES, NOT JUST THE PRECONDITION. The first version checked `requires:` alone and
        # called `create_record` resolvable -- it has no precondition and no EFFECT, so the fold
        # admits it and then raises `Unspecified` on "Part E does not say WHAT VALUE". A caller
        # narrowing to "what the fold can execute" got a set the fold could not execute, and the
        # gap only surfaced when `W17`'s packing started attempting more verbs per season. Found
        # by running the corpus, not by reading it.
        # ⚠ `requires_typed` IS THE FIRST OF THE THREE, AND ONE OWNER IS WHY IT IS HERE. This
        # question -- *can the fold evaluate this precondition* -- is the same question `_fold`
        # asks two hundred lines down, and leaving it reading only `REQUIRES_PREDICATES` would
        # give the two sites different answers for every typed verb (§8: the rule lives once).
        gated = ((row.requires or "").strip() in NO_PRECONDITION
                 or row.requires_typed is not None
                 or v in REQUIRES_PREDICATES)
        effected = not row.writes or v in EFFECTS
        # ⚠ AND A THIRD GATE: A VERB THAT CONTESTS DOES NOT TAKE THE EFFECT PATH AT ALL.
        # `ARCHITECTURE_V2.md:394` — *"`contests: <prize>` — if set, ROUTES TO THE SEAM at
        # RESOLVE (§39)"* — so such a verb is executable only if the SEAM can return. It was
        # counted as executable only because the instrument read its own `EFFECTS` entry and never
        # read the column that says the effect is not the path. Jordan, 2026-09-02: *"you can't
        # just kill or wound imo."* Correct, and the design agreed at `:434` all along.
        #
        # ⚠ THE GATE'S OLD REASON IS NOW FALSE AND ITS NEW ONE IS NARROWER AND MEASURED. What
        # stood here said *"today `contest()` raises `Unspecified` at S39.4 before it returns
        # anything"*. That stopped being true for `the body` when the seam started CALLING
        # personal combat, and `W-E` (2026-09-04) closed the rest: the seam returns, `degree_of`
        # reads the band off the scene, and `_fold` executes all three branches. THE GATE STAYS,
        # ON A DIFFERENT AND CHECKABLE GROUND: a contested act needs a `subject` operand to name
        # the second claimant, and `operands_for` returns `{}` for an UNTYPED verb (`H-80`,
        # `H-94`) — `kill / wound`'s `requires` is `—`, so it is untyped. A computed
        # `kill / wound` would therefore reach the seam with ONE claimant, `combat_seam` would
        # return `PARTY-GAP`, and every case that produced one would become a whole-case
        # DESIGN-GAP. Admitting the verb here is `H-80`'s item, not this one, and the corpus
        # measures the difference: at the shipped fixtures no contested act arises from the loop,
        # which is why closing the seam moved ZERO bytes of the run artifacts.
        contested = bool(row.contests)
        if gated and effected and not contested:
            out.add(v)
    return frozenset(out)


# `ALIGNMENT_SWEEP` and `alignment_at` moved to `season.data.verbs` (step 3), imported back at
# the top of this file. `align()`, directly below, did NOT move -- it is the per-call reader
# (`decision/` territory, a later step), not part of the table.

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
        cands = Query.opening_set(p, v, q, fx)
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


# `questions_for` moved to `season.queries.world_q` (step 5). It takes a `World` FIRST and a
# `Person` second, which is what makes it a world query rather than a person-side one -- the
# distinction `test_w5_sense_is_still_the_only_world_taking_non_decision_function` checks by
# SIGNATURE, so it survives the move as a checkable property rather than as this sentence.
# Imported back at the top of this file.


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


# `occasioned_by` moved to `season.queries.world_q` (step 5) -- it takes a `World` first and asks
# it which acts a question is occasioned by. Imported back at the top of this file.


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
    index = w.cache_at_barrier("presence", lambda: {r: Query.presence(w, r) for r in w.rungs})
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


def as_scenes(produced: list, actor: str, w: "World") -> list:
    """Normalise what `choose` returned into Scenes. `W17`.

    ⚠ A BARE `Act` IS ONE SCENE CARRYING ONE INTERACTION, and that equivalence is what makes the
    scene container ADDITIVE rather than a rewrite: every caller written before the 2026-09-02
    ruling keeps its exact meaning, because one act per scene IS the pre-ruling accounting. A
    caller that wants the ruling's new freedom -- several interactions inside one budgeted scene
    -- returns Scenes instead. Mixing the two in one list is allowed and means what it looks
    like."""
    out = []
    for item in produced:
        if isinstance(item, Scene):
            out.append(item)
        elif isinstance(item, Act):
            out.append(Scene(H(w.world_seed, w.tick, actor, f"scene:{item.id}"), actor, [item]))
        else:
            raise InstrumentDefect(
                f"choose() returned a {type(item).__name__}; it must return Act or Scene "
                "objects. A bare Act is treated as a one-interaction scene (W17).")
    return out


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


def sense(p: Person, w: World, subsistence: Callable[[Person, World], int]) -> Sensation:
    """S18.2 / S26 -- the ONE non-decision function permitted a World, and the only bridge from
    world truth into `choose`.

    REV 3. It now RETURNS a Sensation, so `choose : (Person, View, Sensation) -> Act[]` is the
    signature actually exercised. Reading `.standing` raises where the design fails to supply
    it; `.subsistence` is computed by an INJECTED formula, because no in-chain document
    supplies one and S10.4 makes MatterKind an OPEN registry -- summing kinds as if fungible
    is a model choice this instrument may not make on the design's behalf (S42.2.1)."""
    TRACE.query("sense", "bridge")
    # BOTH scalars, as of W5. Rev 3 built a Sensation with one and let `.standing` raise; §18.2
    # says EXACTLY TWO, and `standing_of` computes the second person-side (`H-29`).
    return Sensation(subsistence(p, w), standing_of(p, w.fixtures))


# ⚠ `sense_subsistence_only(p, w, formula)` STOOD HERE AND W5 DELETED IT, on the evidence of its
# own proof. It was a SECOND non-decision function taking a `World` -- exactly what #353 `:634`
# permits only `sense()` to be -- and it had ZERO CALLERS anywhere in the tree. It survived
# because nothing checked SIGNATURES: the file's dead-code guard looks for switched-off rules
# (`if False`), not for unused functions, and every claim about "the ONE" was made in prose.
# `test_w5_sense_is_still_the_only_world_taking_non_decision_function` walks the AST for any
# person-side function annotated with a `World` and found this on its first run. Recovered at
# `git log -S sense_subsistence_only` if the injected-formula helper is ever wanted again.


# ===========================================================================
# PART III -- THE SEASON LOOP
# ===========================================================================

class ContestError:
    """S39.3/S53 -- GDScript HAS NO EXCEPTIONS and exceeding recursion depth is a CRASH, so the
    cap must produce a TYPED ERROR RESULT, CHECKED BY THE CALLER. Rev 1 returned `[]`, which is
    indistinguishable from a lawful no-event contest. This type is distinguishable."""

    def __init__(self, reason: str, depth: int, max_depth: int):
        self.reason, self.depth, self.max_depth = reason, depth, max_depth

    def __repr__(self) -> str:
        return f"ContestError({self.reason!r}, depth={self.depth}, max_depth={self.max_depth})"



# ===========================================================================
# THE FOLD -- W3. ONE `resolve`, READING `verb_table.yaml`.
#
# What was here: `resolve(acts, effect, ...)`, where `effect` was a CALLER-SUPPLIED LAMBDA that
# inspected `a.verb` and returned Events. Every probe wrote its own. That is defect `D20` and it
# is §27.2's "no second resolver" arriving as a PARAMETER rather than as a function -- a resolver
# per caller, each free to disagree with the others about what a verb does.
#
# THE FOLD, per §E2: eligibility -> `requires` AGAINST THE WORLD THE PREDECESSORS LEFT -> each
# `writes:` through `write()` -> `emits` or `emits_on_refusal`.
# ===========================================================================

# `REQUIRES_PREDICATES`, its `@requires_predicate` decorator, the four surviving predicates
# (`confer`, `revoke`, `dispatch`, `convene`) and the governance readers they use --
# `in_holdings`, `under_purview`, `titles_held`, `highest_title_rank` -- moved to
# `season.loop.predicates` (step 5), imported back at the top of this file. The registry travels
# with the functions it registers, which is the same rule step 3 applied to `REQUIREMENT_TYPES`.
#
# `W-A`'s retirement note travelled with them: the four that are GONE (`transfer`, `tell`, `move`,
# `work`) are typed cells in `verb_table.yaml` now, and
# `test_wa_one_owner_a_verb_has_a_typed_cell_or_a_predicate_and_never_both` is the guard that
# fails if a verb ever carries both. That guard reads `S.REQUIRES_PREDICATES` and is unmoved.


# Verbs the probe corpus uses that #353 does not name AS A VERB — checked, not assumed: the
# strings `take_seat`, `press_claim`, `raid` and `confer_authority` appear ZERO times in its 2,067
# lines, and `fight`/`refuse`/`do`/`act` appear only as ordinary English. They are the caller's
# inventions and the fold says so, rather than charging them to the design. Register row H-64.
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


_S353_CACHE: list = []


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

# `NO_PRECONDITION` moved to `season.data.verbs` (step 3), imported back at the top of this file.


# ===========================================================================
# THE EFFECTS -- EXTRACTED, step 5 of the decomposition (a PURE MOVE).
#
# `EFFECTS`, its `@effect_for` decorator, the ONE operand reader (`_operand`) and the ten `_eff_*`
# now live in `season.loop.effects`. They moved as one block and had to: §8's "THE OWNER OF THE
# RULE, AND THREE EFFECTS HAD THEIR OWN COPY" is about `_operand`, and a decorator-filled table
# must be defined where the decorated functions are or it is empty when the fold reads it.
#
# The fold below reads `EFFECTS` through the import at the top of this file, which is the SAME
# DICT OBJECT -- `S.EFFECTS is effects.EFFECTS`. A re-export, not a second definition.
# ===========================================================================


class SeasonDriver:
    """S23. Six steps, four barriers. DELIBERATE is a MAP, not a barrier; CENSUS SHARES
    WITNESS'S JOIN. S40.3/S44.3: NO CONTAINER GETS A CLOCK -- there is exactly one `season()`."""

    def __init__(self, w: World):
        self.w = w
        # OBSERVATION ONLY, and the distinction matters. Six probes used the removed `effect` hook
        # to record which acts reached RESOLVE and in what order. That is a thing to WATCH, not a
        # thing to DECIDE, and giving it back as a resolver parameter is how the second resolver
        # returns. This list is appended by the fold and read by nobody inside it.
        self.resolved: list[Act] = []
        # ⚠ RESOLVER-SIDE, AND CUMULATIVE — like `resolved`, which is also never reset. The
        # Scene is the budgeted unit and carries the `occasion`, so the fold can name what
        # occasioned an act. No person-side Query reaches it, exactly as none reaches `resolved`.
        # It is NOT season-local: see the note at the `_fold` call site for why R3 depends on
        # that, and do not "fix" it into one.
        self.scenes: dict = {}
        # Event id -> the Act that emitted it. See the note at the `_fold` call site.
        self.act_of: dict = {}

    # -- CALENDAR -- barrier 1 -- DECIDES NOTHING (S24) ----------------------
    def calendar(self) -> None:
        w = self.w
        w.step = Step.CALENDAR
        TRACE.step("CALENDAR", "enter"); TRACE.barrier(1, "CALENDAR")
        w.discard_caches()
        for did, d in list(w.dates.items()):
            if d.get("due_at") != w.tick:
                continue
            vacant = not d.get("holder")
            TRACE.decision(f"date {did} came due", "S24",
                           chose="fire-and-lapse" if vacant else "fire-as-sitting",
                           alternatives=["block until a holder exists", "defer to next season"])
            w.write("Date", WriteClass.CALENDAR, lambda d=d: d.__setitem__("fired", True),
                    record_kind="Date", fieldname="fired", driver="Event")
            if not vacant:
                w.write("DocketItem", WriteClass.CALENDAR,
                        lambda did=did: w.docket.append({"date": did, "matter": None}),
                        record_kind="DocketItem", fieldname="matter", driver="Event")
        TRACE.step("CALENDAR", "leave")

    # -- MATTER -- barrier 2 -- THE WORLD FREEZES AT ITS END (S25) -----------
    def matter(self, actorless: Optional[list[Event]] = None) -> list[Event]:
        w = self.w
        w.step = Step.MATTER
        TRACE.step("MATTER", "enter"); TRACE.barrier(2, "MATTER")
        w.discard_caches()
        emitted: list[Event] = []

        # S31.2: the EVENT CHANNEL and the DEATH CASCADE run SERIALLY, BEFORE the parallel
        # section, because both CROSS OWNERS (S31.1). S31.1 exception 3: an actorless event is
        # ONE Event spanning many rungs -- sharding it per rung BREAKS causes[], because ONE
        # CAUSE IS ONE ID.
        # ⚠ REV 5. This row previously read "serial: event channel, then death cascade; then
        # parallel over Sites and bodies" and was recorded 194 times -- describing TWO BRANCHES
        # THAT DO NOT EXIST IN THIS CODE. A decision register whose most frequent row names code
        # never written is worse than no register: it is the "every decision made" claim made
        # false at its highest-volume site.
        TRACE.decision("MATTER's cross-owner operations", "S31.1",
                       chose="serial: the actorless event channel; then parallel over Sites",
                       alternatives=["shard the event channel per rung (breaks causes[]: one cause is one id)"],
                       not_implemented=["the death cascade (S31.1 exception 2)",
                                        "bodies, larders, yield, travel (S25's other rows)"])
        for e in (actorless or []):
            w.log.append(e); emitted.append(e)
            TRACE.event(e.id, e.kind, e.causes)

        # -- TERM MATURATION (#353 `:491-492`) ------------------------------
        # "MATTER matures terms; each maturation is A PERSON'S PAST ACT RIPENING, with `causes[]`
        # pointing at the act that wound the clock." This is the second link of `PLAN.md` §6.3's
        # chain and the only mechanism in the design by which one season's act reaches into a
        # later one WITHOUT anybody acting again.
        #
        # ⚠ AND IT STOPS IF THE MAKER IS GONE, which #353 gives as the reason the lawful version
        # beats the clock-driven one: "a half-made copy now correctly STOPS if the copyist is
        # jailed, which the MATTER-driven version gets wrong: A COPY THAT FINISHES ITSELF." The
        # check is on the winder still existing, not on a clock.
        for rid in sorted(w.records):
            rec = w.records[rid]
            for n, st in enumerate(list(rec.stages)):
                if not (isinstance(st, tuple) and len(st) >= 3):
                    continue
                due, label, wound_by = st[0], st[1], st[2]
                if due != w.tick:
                    continue
                holder = next((t.subject for t in w.tenures
                               if t.object == rid and t.kind == "hold" and t.live), None)
                if holder is None or holder not in w.persons:
                    TRACE.note(f"{rid} stage {label!r} did not mature: its winder is gone "
                               "(#353 :496 -- a half-made copy STOPS rather than finishing itself)")
                    continue
                # `causes[]` names the EVENT that created the record where there is one, so the
                # chain WALKS; #353 says "the act that wound the clock" and the act's own
                # emission already names that act, so pointing at the emission preserves the
                # provenance and adds a link rather than restating one.
                prior = next((e.id for e in reversed(w.log)
                              if any(c.subject == rid for c in e.changes)), wound_by)
                ev = Event(H(w.world_seed, w.tick, rid, f"matured:{label}"),
                           "term.matured", rid,
                           [StateChange(rid, "set", "MATTER", "stages", label)],
                           [prior], w.tick)
                w.log.append(ev); emitted.append(ev)
                TRACE.event(ev.id, ev.kind, ev.causes)

        # -- CLAIM CONFIDENCE DECAY (`W4` / `H-40`) --------------------------
        # THE THIRD LICENSED CLOCK (#353 `:864`), and until now the only one of the three with no
        # implementation at all — Part D had no `Claim` row, so Part D was not total for a clock
        # #353 licenses. `W2` added the row; this is the other half.
        #
        # ⚠ L4 IS NOT VIOLATED AND THE REASON IS WORTH STATING: a Claim's confidence is
        # `social:false` in Part D, so the world may move it. What the world may NOT do is decide
        # anything with it — the decay emits and stops, exactly as a band crossing does.
        #
        # THE ANTECEDENT IS THE CLAIM'S OWN PREVIOUS DECAY, chaining to `[ROOT]` on the first one,
        # for the same reason wear does: a licensed clock's genuine first emission is the only
        # place `[ROOT]` belongs.
        decay = w.fixtures.claim_decay()
        for pid in sorted(w.persons):
            p_ = w.persons[pid]
            for c in list(p_.ledger):
                if c.confidence <= 0:
                    continue
                # The claim's own previous decay, else the deposit that created it. NEVER
                # `[ROOT]`: a claim is not a clock, it is a thing a witness deposited, and the
                # deposit has an Event. `[ROOT]` here would say the campaign seed caused it.
                prior = (w.last_emission_of("claim.decayed", c.id)
                         or w.last_emission_of("claim.deposited", c.id))
                if prior is None:
                    TRACE.note(f"{c.id} has no deposit Event to chain its decay to; skipped "
                               "rather than rooted at the campaign seed")
                    continue
                # ⚠ AN EFFECT THAT TOUCHED NOTHING DID NOT DO THE THING, AND MUST NOT EMIT THE
                # SUCCESS. That rule is already enforced twice in this file -- `_fold` applies it
                # to a verb whose effect wrote nothing, and `rosters.yaml`'s
                # `conditional_emission_rows` uses the same argument to exempt `(Record, ttl)`.
                # It was violated here, at `H-40`'s OWN DECLARED `0` SWEEP POINT: at
                # `claim_decay_per_season = 0` every claim still emitted `claim.decayed` every
                # season while `max(0, c.confidence - 0)` changed nothing, so the control arm of
                # the sweep published a decay that did not happen. A sweep point that fabricates
                # is worse than one that is unexecuted. Found by the `W4` adversarial pass.
                after = max(0, c.confidence - decay)
                if after == c.confidence:
                    continue
                w.write("confidence", WriteClass.MATTER,
                        lambda c=c, after=after: setattr(c, "confidence", after),
                        record_kind="Claim", fieldname="confidence", driver="Event",
                        emits="claim.decayed", subject=c.id, causes=[prior])

        # -- LARDERS, THEN YIELD (`W8`) -------------------------------------
        # #353 §25 fixes the ORDER and this code follows it rather than choosing one: *"Events
        # resolve FIRST, then bodies, larders, yield, travel, wear."* So a season's subsistence is
        # drawn against LAST season's stores and production replenishes afterwards, which is a
        # substantive difference — the reverse order would let a rung eat what it had not yet
        # produced, and no rung could ever run short. `test_w8_...order...` asserts it.
        #
        # ⚠ BODIES AND TRAVEL ARE STILL NOT BUILT. Naming them here would suggest otherwise; the
        # `not_implemented` list in this barrier's decision row is where they are recorded.
        weights = w.fixtures.get("subsistence_weight")
        factor = w.fixtures.get("season_factor")
        scale_ = w.fixtures.get("condition_scale")
        for rid in sorted(w.rungs):
            r = w.rungs[rid]
            eaters = Query.presence(w, rid)
            if eaters and weights:
                # `H-11`: *draw from the containing rung's stores, scaled by weight.* A kind with
                # no weight RAISES rather than drawing nothing (see `rosters.yaml`), so the loop
                # is over the WEIGHTS, which is the registry, not over whatever the larder holds.
                draw = {k: wt * len(eaters) for k, wt in weights.items()}
                have = dict(r.stores or {})
                after = {k: max(0, have.get(k, 0) - amt) for k, amt in draw.items()}
                short = {k: amt - (have.get(k, 0) - after[k]) for k, amt in draw.items()
                         if amt > have.get(k, 0)}
                if short:
                    # ⚠ A SHORTFALL EMITS NOTHING AND DECIDES NOTHING, on L5's rule: a threshold
                    # crossing *"MAY NEVER PRODUCE AN OUTCOME"*. Inventing starvation here would
                    # be the outcome L5 forbids, and it would be a social consequence written at
                    # MATTER, which is L4. It is recorded so a run can be read.
                    TRACE.note(f"{rid} could not meet subsistence for {len(eaters)} by {short} "
                               "-- recorded, not acted on (L5: a crossing produces no outcome)")
                if any(after[k] != have.get(k, 0) for k in after):
                    prior = w.last_emission_of("stores.changed", rid)
                    w.write("stores", WriteClass.MATTER,
                            lambda r=r, after=after: r.stores.update(after),
                            record_kind="Rung", fieldname="stores", driver="Event",
                            emits="stores.changed", subject=rid,
                            causes=[prior] if prior else [ROOT])
            # `yield` — #353 §25's *"only here"* row. The base is the SITE's, scaled by its
            # condition and then by `season_factor`, so a worn place produces less without a
            # second wear concept (`H-93`, and `rosters.yaml: site_yield` for why).
            produced: dict = {}
            # ⚠ THE SITE'S OWN `rung`, NOT THE RUNG'S `sites` LIST. The first version read
            # `r.sites`, and that list is a BACK-REFERENCE NOTHING MAINTAINS — it is empty for
            # every rung in the corpus, so the whole yield step was INERT and would have shipped
            # as an unreachable barrier stage. `Site.rung` is the maintained side (S12), and
            # reading the side that is actually written is the difference between a step that
            # runs and a step that merely exists (§0.2). Caught by `F10` failing for a different
            # reason and then looking at the fixture.
            for site in sorted(w.sites.values(), key=lambda x: x.id):
                if site.rung != rid:
                    continue
                for k, base in (SITE_YIELD.get(site.kind) or {}).items():
                    produced[k] = produced.get(k, 0) + int(
                        base * (max(0, site.condition) / scale_) * factor)
            produced = {k: v for k, v in produced.items() if v}
            if not produced:
                continue
            prior_y = w.last_emission_of("yield.taken", rid)
            w.write("yield", WriteClass.MATTER,
                    lambda r=r, produced=produced: object.__setattr__(r, "yield", dict(produced)),
                    record_kind="Rung", fieldname="yield", driver="Event",
                    emits="yield.taken", subject=rid,
                    causes=[prior_y] if prior_y else [ROOT])
            prior_s = w.last_emission_of("stores.changed", rid)
            credited = {k: (r.stores or {}).get(k, 0) + v for k, v in produced.items()}
            w.write("stores", WriteClass.MATTER,
                    lambda r=r, credited=credited: r.stores.update(credited),
                    record_kind="Rung", fieldname="stores", driver="Event",
                    emits="stores.changed", subject=rid,
                    causes=[prior_s] if prior_s else [ROOT])

        # S25: NO SOCIAL QUANTITY MOVES HERE. L4 at its sharpest.
        w._in_parallel_map = True
        scale = w.fixtures.get("condition_scale")
        floors_all = w.fixtures.get("band_floors")
        for s in w.sites.values():
            before = s.condition
            wear = w.fixtures.wear(s.kind)      # NO SILENT DEFAULT -- unregistered kind raises
            # `W4`. WEAR IS A LICENSED CLOCK, AND A CLOCK CHAINS TO ITSELF. `[ROOT]` is for the
            # campaign seed and a licensed clock's GENUINE FIRST emission (#353 `:682-685`); every
            # later tick of the same clock names the tick before it. So the number of `[ROOT]`
            # causes stops growing after season 1, which is `W4`'s stated proof and is asserted
            # rather than printed (`G3`). Handing every emission the root instead is what made the
            # `W9` artifact's entire log unwalkable.
            prior_wear = w.last_emission_of("condition.worn", s.id)
            _mark = len(w._emitted_by_write)
            w.write("condition", WriteClass.MATTER,
                    lambda s=s, wear=wear: setattr(s, "condition", max(0, s.condition - wear)),
                    record_kind="Site", fieldname="condition", driver="Event",
                    emits="condition.worn", subject=s.id,
                    causes=[prior_wear] if prior_wear else [ROOT])
            # ⚠ THE TAIL SINCE THIS WRITE, NOT THE WHOLE BUFFER. The first version CLEARED the
            # buffer before each site so `[-1]` would be this site's wear — which also threw away
            # every earlier emission of the barrier, and the barrier's emissions are what MATTER
            # must return so they can be witnessed. Marking the position keeps both.
            worn_ev = w._emitted_by_write[_mark] if len(w._emitted_by_write) > _mark else None
            # S12.1 / L5: A BAND EDGE CROSSING IS AN EMISSION, NOT A WRITE.
            #
            # ⚠ REV 3. Rev 2 appended a row for EVERY site EVERY season regardless of whether
            # any band was crossed, and NEVER CONSTRUCTED AN EVENT -- so nothing was
            # witnessable and nothing entered the log, while the probe that read it claimed
            # "L5 exactly... THE COUNTER COMPELS SOMEONE TO ACT". Half of L5 was missing and
            # the other half was a filter on "did the number change at all", which wear
            # guarantees. A crossing now fires only on a REAL band edge and EMITS.
            floors = floors_all.get(s.kind, {})
            for verb, floor in sorted(floors.items()):
                if before >= floor > s.condition:
                    # `W4`. THE CROSSING'S ANTECEDENT IS THE WEAR THAT CROSSED THE FLOOR, which is
                    # `H-12`'s whole purpose -- *"MATTER emits an Event per write SO CROSSINGS HAVE
                    # AN ANTECEDENT"*. It read `causes=[ROOT]`, so the one Event in this barrier
                    # that exists to be walked back from was rooted at the seed and walked nowhere.
                    ev = Event(
                        id=H(w.world_seed, w.tick, s.id, f"crossing:{verb}"),
                        kind="condition.band_crossed", subject=s.id, changes=[],
                        causes=[worn_ev.id] if worn_ev else [ROOT], emitted_at=w.tick)
                    w.log.append(ev); emitted.append(ev)
                    w.crossings.append((s.id, verb, before, s.condition, ev.id))
                    TRACE.event(ev.id, ev.kind, ev.causes)
                    TRACE.decision(f"{s.id} crossed the `{verb}` floor", "S12.1/S3-L5",
                                   chose="EMIT a witnessable Event; write no social row; produce no outcome",
                                   alternatives=["write the consequence directly (L5 forbids: a crossing MAY NEVER PRODUCE AN OUTCOME)",
                                                 "silently drop the verb from the set (then nobody can witness it)"])
        w._in_parallel_map = False
        # ⚠ THE EMISSIONS `write()` MADE ARE PART OF WHAT MATTER PRODUCED, AND LEAVING THEM OUT
        # MADE THEM UNWITNESSABLE. `emitted` is built by hand from explicit `append`s; `W4` moved
        # emission into `write()`, which appends to `w.log` and to this buffer but not to the list
        # `season()` hands to WITNESS. The measurable consequence: `condition.worn` and
        # `claim.decayed` were the ONLY kinds in the log that reached NO ledger — about a hundred
        # events a season that existed and that nobody could witness, in a design whose §61
        # fan-out is TOTAL. Found by measuring W6's starting state, not by reading.
        #
        # ⚠ AND `claim.deposited` IS DELIBERATELY NOT HERE. It is emitted during WITNESS, about a
        # person's own interior ledger. Fanning it would mean everyone learns what everyone else
        # remembers, AND it would close a loop — a deposit emits, the emission is witnessed, that
        # deposit emits — growing without bound. MATTER's barrier ends here; WITNESS's own
        # emissions are not MATTER's output.
        emitted.extend(w._emitted_by_write)
        w._emitted_by_write.clear()
        TRACE.step("MATTER", "leave")
        w.frozen = True     # S26.2 -- frozen from END OF MATTER to START OF RESOLVE
        return emitted

    # -- DELIBERATE -- a MAP, not a barrier (S26) ---------------------------
    def deliberate(self, choose: Callable[..., list[Act]], question: Any,
                   subsistence: Callable[[Person, World], int]) -> list[Act]:
        w = self.w
        if not w.frozen:
            raise Forbidden("DELIBERATE entered on an unfrozen world", "S26.2",
                            law="S26.2 -- the world is FROZEN from the end of MATTER to the start of RESOLVE. THIS IS WHAT MAKES THE MAP SAFE TO PARALLELISE")
        w.step = Step.DELIBERATE
        TRACE.step("DELIBERATE", "enter")
        # ⚠ CALLED HERE, NOT ONLY FROM THE `tenures` GETTER. `_rehome` exists so that a Tenure
        # added before its subject Person existed still reaches its owner, and its own docstring
        # names `budget` as what would otherwise read zero offices for a duke. But `budget`,
        # `person_side_eligible` and `questions_for` all read `p.tenures` DIRECTLY and this step
        # never touches `w.tenures`, so the guard did not cover the three functions it named --
        # it worked only if unrelated code happened to read the aggregate first. One call, at the
        # barrier, before any person-side read.
        w._rehome()
        acts: list[Act] = []
        k_view = w.fixtures.get("view_k")
        k_budget = w.fixtures.get("scene_budget")
        q_rule = w.fixtures.get("question_aggregation_rule")
        w._in_parallel_map = True       # S51: WorkerThreadPool over persons. The one that pays.
        for p in list(w.persons.values()):
            s = sense(p, w, subsistence)            # a Sensation, per S26's signature
            # §F1 / `H-04`. `q` HAS A PRODUCER NOW. Rev 3 took the question as an injected
            # parameter because §61 recorded that DELIBERATE HAD NO DECLARED ENTRY POINT; the
            # four sources are computed here, at the barrier, from the loop's own output.
            # An explicit `question` still overrides, so a probe can name the q it is testing.
            qs = questions_for(w, p)
            # `H-54`, DECLARED. This was `qs[0] if qs else None` — an `absent` hole filled inside
            # a subscript, with no row and no alternative (`G1`). `question_sources` is ORDERED,
            # so taking the first silently ruled that A DATE ALWAYS BEATS A NEED, which decides
            # what every NPC does first. The rule is data now; `first` is the incumbent kept as
            # the sweep's control.
            q_p = question if question is not None else aggregate_questions(qs, q_rule)
            v = Query.assemble(p, q_p, k_view)
            # S26.3: the PERSON asks their own budget. `choose` receives the QUERY, not the
            # answer -- rev 2 computed it in the engine and handed the number down, which is
            # the half of retraction 5 that never landed.
            ask_budget = lambda p=p, v=v: Query.budget(p, v, k_budget, w.fixtures)
            b = ask_budget()
            produced = choose(p, v, s, ask_budget)
            # `W17`. THE BUDGETED UNIT IS THE SCENE (Jordan, 2026-09-02), so the bound below
            # counts scenes and the interaction bound is a SEPARATE check. A bare `Act` is one
            # scene carrying one interaction -- which is exactly the pre-ruling semantics, so
            # every caller that returns Acts keeps its meaning and the change is additive.
            scenes = as_scenes(produced, p.id, w)
            spent = sum(sc.cost(w.fixtures.get("extended_scene_cost")) for sc in scenes)
            # S26.3: the engine does NOT truncate. Any cap applied here would be AN ENGINE
            # DECIDING A PERSON'S OPTIONS, which is L1. Over-budget is the CALLER'S defect.
            if spent > b:
                raise Forbidden(
                    f"{p.id} returned {len(scenes)} scenes costing {spent} against a budget of "
                    f"{b} scene actions", "S26.3",
                    needs="`choose` is bounded by budget(person, view) -- the PERSON chooses what to leave undone",
                    law="S26.3, re-stated in scenes per Jordan's 2026-09-02 ruling -- at one scene NOBODY EVER CHOOSES WHAT TO LEAVE UNDONE; the budget exists to create triage. An engine that silently discards the tail has made the choice instead of the person, which is L1. ⚠ THE UNIT MATTERS: eight INTERACTIONS across five scenes is LAWFUL and was refused before the ruling")
            # ⚠ A SEPARATE FAILURE, DELIBERATELY. `PLAN.md` `W17` item 3: the two propositions are
            # "a person returned more SCENES than `budget` allows" and "a scene carried more
            # interactions than the swept bound". Folding them into one check would make the
            # ruling's whole distinction unobservable.
            cap = w.fixtures.get("interactions_per_scene")
            if cap is not None:
                for sc in scenes:
                    if len(sc.acts) > cap:
                        # ⚠ `Ungraded`, NOT `Forbidden`. `Forbidden`'s own docstring is "a law
                        # forbids what the case requires", and this bound is a SWEPT HARNESS
                        # DEFAULT that Jordan explicitly did not rule. Filing it as `Forbidden`
                        # put a fixture's refusal in the column `PROBES.md` reports as "raised BY
                        # THE SHAPE ITSELF", i.e. charged a harness choice to the design. This
                        # file already uses `Ungraded` for exactly that polarity on numbers.
                        raise Ungraded(
                            f"scene {sc.id} carries {len(sc.acts)} interactions against a bound "
                            f"of {cap}", "S26.3",
                            needs="a scene carries 1-3 verb applications; the bound is swept, not constant",
                            law="`H-76`, `assumption`. `player_agency_v30.md` §6.3 -- 'A scene contains 1-3 mechanical interactions' -- which is CANONICAL but pre-#337, so under CLAUDE.md §0.05 it is REFERENCE and this is a swept default, not a rule of the design. Jordan ruled the UNIT and the NUMBER of scenes; he did not rule this")
            # ⚠ THE TRACE IS PER-SCENE, AND THE UNITS MUST NOT BE MIXED. It read
            # `TRACE.act(p.id, a.verb, b - i - 1)` where `b` is a SCENE budget and `i` enumerated
            # the FLATTENED interactions, so a lawful season published `budget_left=-10` — the
            # artifact stating that the engine had just accepted an overspend it did not. That is
            # the same defect the `act_budget` -> `scene_budget` rename was made to prevent, one
            # field along: a name is where the next reader learns what a number counts, and so is
            # a unit. `scene_left` is scenes; `interaction` is the position inside the scene.
            produced = []
            left = b
            for sc in scenes:
                left -= sc.cost(w.fixtures.get("extended_scene_cost"))
                # ⚠ THE SCENE IS REGISTERED AND THE ACT IS STAMPED WITH IT. Season-local, beside
                # `resolved`, and for the same reason: the fold needs to ask what occasioned an
                # act, and nothing else in the loop knows. Without this the Scene is built,
                # carries its occasion, and is dropped one line later — which is what `N3`
                # measured as *an act never cites its question*.
                self.scenes[sc.id] = sc
                for n, a in enumerate(sc.acts):
                    TRACE.scene_act(p.id, a.verb, left, n + 1, len(sc.acts))
                    a.scene = sc.id
                    produced.append(a)
            for i, a in enumerate(produced):
                # L1 -- THE PERSON IS THE ONLY ACTOR. ⚠ REV 4: `Act.actor` is a bare id and
                # nothing checked it, so `Act("x", "the_church", "excommunicate")` reached
                # `resolve` intact -- which means A6's and F3's "'The Church excommunicates' IS
                # NOT SPELLABLE" was FALSE, and both were labelled by="no-signature" on the
                # strength of it. It is spellable now only at the cost of this check.
                if a.actor != p.id:
                    raise Forbidden(
                        f"an Act returned by {p.id}'s choose() carries actor '{a.actor}'",
                        "S3-L1", needs="a named person, and the person deciding is that person",
                        law="L1 -- NO INSTITUTION ACTS, NO FACTION ACTS, NO THRESHOLD ACTS. An institution acts BY A NAMED PERSON AT A VENUE. Without this check the id is a free string and the law is a convention")
                acts.append(a)
        w._in_parallel_map = False
        TRACE.step("DELIBERATE", "leave")
        return acts

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

    # -- WITNESS -- barrier 4 -- THE JOIN (S28) -----------------------------
    def witness(self, events: list[Event]) -> int:
        w = self.w
        w.step = Step.WITNESS
        TRACE.step("WITNESS", "enter"); TRACE.barrier(4, "WITNESS")
        w.discard_caches()

        # S28 stage 1: FAN-OUT IS GLOBAL AND ONE PASS, computed from THE PRESENCE INDEX and the
        # five channels. No signals, no subscription table. DO NOT SHARD IT -- the design's
        # predecessor loop was retired precisely because its WITNESS was not global, which made
        # its parallelism claim UNSOUND rather than merely unproven.
        # ⚠ REV 3. Rev 2 keyed the observer set on the Event's subject rung and fell back to
        # THE SUBJECT ALONE when that was empty -- which, because every person has a
        # `person`-kind Rung, made almost every Event private to its own subject. That is a
        # SELF-WITNESS RULE THAT APPEARS NOWHERE IN THE CHAIN: the instrument invented the
        # privacy the design lacks, and then reported the design's privacy gap in a probe
        # that never touched the loop.
        #
        # S61 is explicit about the specified behaviour and this now implements it:
        #   "WITNESS AS SPECIFIED FANS EVERY EVENT TO EVERY PERSON. Nothing said in private
        #    is private. A wrapper does not fix this and must not be presented as fixing it."
        # The five channels are NAMED (S20) and NONE of their predicates is given, so there is
        # no predicate by which anyone could be EXCLUDED. The fan-out is therefore total.
        # Seeds the cache `_ch_co_located` reads. Before `W6`'s adversarial pass this was built
        # here and read NOWHERE -- the predicate rebuilt it per (event, person).
        w.cache_at_barrier("presence", lambda: {r: Query.presence(w, r) for r in w.rungs})
        everyone = list(w.persons)
        # `W6` / `H-33`. THE CHANNELS HAVE PREDICATES NOW, and the mode says which are live.
        # `total` is the specified behaviour and the sweep's control; the presence index this
        # barrier has always built was UNUSED until this line.
        mode = w.fixtures.get("fan_out_mode")
        fan: list[tuple[str, Event, str]] = [
            (pid, e, mode) for e in events for pid in observers_for(w, e, mode, everyone)]
        TRACE.decision(f"fan-out over {len(events)} events -> {len(fan)} deposits", "S28/S61",
                       chose=f"mode={mode} over {len(everyone)} persons "
                             f"({'#353 S61 as specified, and H-33 control' if mode == 'total' else 'H-33 arm; `all_five` is the ruled default since 2026-09-07, R7'})",
                       alternatives=[
                           "shard per rung (retired: made the parallelism claim unsound)",
                           "total (S61's specified behaviour, and H-33's control arm)",
                           f"the five channels {list(WITNESS_CHANNELS)}, each with the predicate "
                           "`rosters.yaml: witness_channel_predicates` injects"])

        # S28 stage 2: DEPOSIT IS PER-PERSON, into that person's OWN ledger and no other.
        cap = w.fixtures.get("ledger_cap")
        conf = w.fixtures.get("confidence_default")
        claim_rule = w.fixtures.get("claim_subject_rule")
        # `W-B` / `H-122`. WHO RECEIVES A CLAIM MINTED FROM WHAT THE FOLD READ. `none` is the
        # CONTROL -- the behaviour before `W-B`, so every measurement of this item has a baseline
        # (§0.1 point 4). Read here rather than inside the loop so the fixture is consulted once
        # per barrier and `Fixtures.reads` counts a barrier, not a deposit.
        obs_mode = w.fixtures.get("observation_deposit_mode")
        if obs_mode not in OBSERVATION_DEPOSIT_MODES:
            raise Unspecified(
                f"observation-deposit mode {obs_mode!r} is not in the roster", "H-122",
                needs=f"one of {sorted(OBSERVATION_DEPOSIT_MODES)}",
                law="`observers_for`'s precedent, and for its reason: *'an unrecognised mode "
                    "silently falling back would make every measurement of this sweep read the "
                    "control'*. Here the control is `none`, i.e. depositing nothing, so a silent "
                    "fallback would report `W-B` as having changed nothing")
        deposits = 0
        # ⚠ PASS-SCOPED, KEYED BY PERSON -- NOT PER (PERSON, EVENT), WHICH IS WHERE IT WAS BUILT
        # AND WHAT MADE THE DE-DUPLICATION BELOW A CLAIM THE CODE DID NOT DELIVER. `LedgerReader`
        # matches on `(subject, predicate)` and resolves on `(when, confidence)` with a STRICT `>`,
        # so two claims deposited in the SAME barrier with the same `confidence_default` tie on
        # both keys and the FIRST APPENDED wins -- which is the append-order dependence
        # `LedgerReader`'s own docstring says it exists to prevent (*"answering with the first
        # found would make the verdict depend on append order"*). A `seen_obs` created inside the
        # fan loop cannot see a collision across two Events, and `_eff_transfer` mutates
        # `Rung.stores` during RESOLVE, so two transfers on one rung in one season read 8 then 7
        # (`test_wb_two_reads_of_one_cell_in_one_barrier_deposit_exactly_one_claim` builds it).
        # MEASURED over the 86 corpus worlds (`W-B` adversarial pass, 2026-09-04): at `total`,
        # **651 surviving tied groups, 27 of them holding DIFFERENT values** -- e.g. `ARC-01`,
        # `p_a`, `('r_realm','stores:grain',when=4,conf=100)` holding `[168, 167, 167]`. At
        # `actor` it is 0, because one actor rarely acts twice on one rung in one season; the
        # defect is reachable in the shipped grammar and lives in the arm the row also measures.
        # ⚠ WHICH READ SURVIVES IS NOW STATED RATHER THAN LEFT TO A COMPARATOR IN ANOTHER CLASS.
        # Within one barrier every read is equally recent BY `when`, so `LedgerReader` cannot rank
        # them and something must: the first read the fan reaches -- i.e. the earliest Event in
        # RESOLVE order -- is kept, which is the answer `LedgerReader`'s strict `>` already gave.
        # This fix removes the TIE, not the answer.
        seen_obs_by_pid: dict = {}
        w._in_parallel_map = True
        for pid, e, channel in fan:
            p = w.persons.get(pid)
            if p is None:
                continue
            # S28: A KNOT DEPOSIT REUSES THE EVENT ID. Rev 1 wrote the rule and switched it off
            # with `if False`. This is the rule, on.
            via_knot = any(t.kind == "knot" and t.live and pid in (t.subject, t.object)
                           for t in w.tenures)
            src = "firsthand_via_knot" if via_knot else "firsthand"
            # `H-79`: WHAT A DEPOSIT IS ABOUT. #353 §20 types `Claim.subject` and never says what
            # it is for a WITNESS deposit; the instrument used `e.subject`, the ACTOR, which made
            # §F1's Q2 clause "a claim whose subject is SOMETHING THEY HOLD" unreachable and left
            # the narrative substrate empty. `changes[]` already names what an act touched, so
            # this reads the Event the design has rather than adding a field to it (§8.1).
            for n, subj in enumerate(claim_subjects(e, claim_rule, act_refs(self.act_of.get(e.id)))):
                cid = (e.id if via_knot and n == 0
                       else H(w.world_seed, w.tick, pid, f"claim:{e.id}:{n}"))
                c = Claim(cid, pid, subj, e.kind, True, w.tick, src, conf, "own")
                # `W4`. THE DEPOSIT EMITS, AND THAT IS WHAT GIVES A DECAY AN ANTECEDENT.
                # Part D declares `claim.deposited` on this row and NOTHING EMITTED IT, so a
                # claim entered the world uncaused — and every later `claim.decayed` would have
                # had to root at `[ROOT]`, which put 63 spurious roots in a 3-season run and made
                # `W4`'s own ROOT-count proof unsatisfiable. Chained to the witnessed Event, the
                # walk is `decayed -> ... -> deposited -> the act that was witnessed`, which is
                # what #353 §19.4 means by the substrate of the emergent-narrative claim.
                w.write("claim_ledger", WriteClass.INTERIOR,
                        lambda p=p, c=c: p.ledger.append(c),
                        record_kind="Person", fieldname="claim_ledger", driver="Event",
                        emits="claim.deposited", subject=c.id, causes=[e.id])
                TRACE.claim(pid, e.id, src)
                deposits += 1
            # `W-B`. THE SECOND DEPOSIT: ONE CLAIM PER READ THE FOLD MADE, IN THE `requires`
            # VOCABULARY. `Observation` is `(subject, predicate, value)` and so is `Claim`; its
            # own docstring says an Observation *"is what a Claim would be if the reader wrote
            # one"*, and this is the writer.
            #
            # ⚠ WHY THIS IS A SECOND LOOP AND NOT A RULE INSIDE `claim_subjects`. That function
            # answers *what is this deposit ABOUT* for the EVENT-KIND claim, and its
            # `actor`/`per_change`/`both` roster is `H-79`'s, already swept and already measured.
            # An observation-claim's subject is not a choice -- it is the entity the reader read,
            # and the Observation carries it. Overloading `H-79`'s rule would put two decisions on
            # one fixture, which is exactly the defect `H-121` was minted to repair.
            #
            # ⚠ AND THE PREDICATE IS NOT `e.kind`. That is the whole point. The event-kind claim
            # above carries `predicate = e.kind, value = True` -- `travel.blocked`, `act.refused`
            # -- and `belief_contradicts` evaluates `requires_typed` against `LedgerReader`, whose
            # vocabulary is `stores:<kind>` / `condition` / `contain.path:<to>` / `claim.held` /
            # `exists:<kind>` / a relation stem. The two vocabularies are DISJOINT, and `True` can
            # never make a comparator return False, so the belief channel was closed by a theorem
            # rather than by a bug (`H-116`, measured: 0 claims in the derived namespace over a
            # 3-season NPC-088 run before this line existed). These claims are in that namespace
            # by construction, because the Observation's predicate is derived from the cell.
            #
            # ⚠ UNKNOWN IS NOT DEPOSITED, AND THE REASON IS `H-94`'s. A read the world could not
            # answer is the INSTRUMENT'S GAP, and `operands_for` already refuses to mint an act
            # with a hole precisely so that *"the instrument's own gap would become a FALSE BELIEF
            # held by every witness, about a granary nobody named."* Depositing UNKNOWN would
            # reintroduce that from the other end. It is also inert-but-costly: `LedgerReader`
            # returns the stored value, `_as_number(UNKNOWN)` is UNKNOWN, and the clause returns
            # UNKNOWN -- so the claim can never contradict anything while still consuming a slot
            # the cap evicts somebody else for.
            #
            # ⚠ DE-DUPLICATED ON `(subject, predicate)`, WHICH IS THE KEY `LedgerReader.read`
            # MATCHES ON -- AND ACROSS THE WHOLE BARRIER, WHICH IS THE SCOPE THAT READER OPERATES
            # AT. Two claims a reader cannot tell apart are one belief stored twice, and
            # `claim_subjects` gives the same reason for its own de-duplication: a person holding
            # two identical claims would double-count in every eviction comparison. The set is
            # `seen_obs_by_pid` above; the first writing of this scoped it inside the fan loop, so
            # the sentence was true of one Event and false of the pass. See that comment for the
            # measurement.
            if obs_mode != "none" and (obs_mode == "total" or pid == e.subject):
                seen_obs = seen_obs_by_pid.setdefault(pid, set())
                # `e.observed`, NOT `getattr(e, "observed", ())`. The field is on `Event` now, so
                # a default here would be a guard for a case that cannot arise -- and it would
                # SWALLOW the one case worth failing on, an object that is not an Event reaching
                # this barrier. `content_hash`'s `getattr` is a different matter: it is the
                # forward-compatibility fold `W-B` was written against and predates the field.
                for o in e.observed:
                    if o.value is UNKNOWN or o.value is None:
                        continue
                    # ⚠ AND A READ COMPUTED FROM THE LEDGER IS NEVER DEPOSITED INTO IT. See
                    # `LEDGER_DERIVED_STEMS` for the measurement and for the alternative that was
                    # rejected. In one line: `WorldReader.read(X, "claim.held")` answers from
                    # LEDGER MEMBERSHIP, so storing `(X, "claim.held", False)` puts a claim about
                    # `X` in the ledger and makes that read True -- the deposit falsifies its own
                    # content, and the person then declines an act the fold would admit. This is
                    # the same prohibition as the UNKNOWN guard above, one predicate over: a
                    # deposit the instrument cannot stand behind is not deposited.
                    if str(o.predicate).partition(":")[0] in LEDGER_DERIVED_STEMS:
                        continue
                    key = (o.subject, o.predicate)
                    if key in seen_obs:
                        continue
                    seen_obs.add(key)
                    # `e.id` is in the digest, so the per-person counter need only separate
                    # two reads OF ONE EVENT; it spans the pass now and is still strictly
                    # increasing, so no two ids collide.
                    oc = Claim(H(w.world_seed, w.tick, pid, f"obs:{e.id}:{len(seen_obs)}"),
                               pid, o.subject, o.predicate, o.value, w.tick, src, conf, "own")
                    w.write("claim_ledger", WriteClass.INTERIOR,
                            lambda p=p, c=oc: p.ledger.append(c),
                            record_kind="Person", fieldname="claim_ledger", driver="Event",
                            emits="claim.deposited", subject=oc.id, causes=[e.id])
                    TRACE.claim(pid, e.id, src)
                    deposits += 1
            # ⚠ `while`, NOT `if`. THE CAP WAS NOT A CAP. One deposit can mint SEVERAL claims --
            # `claim_subjects` returns one per `StateChange` under the `per_change` rule -- and a
            # single `if` pops exactly one, so the ledger settled at 203 against `L = 200`. A cap
            # that is exceeded by however many subjects the last Event carried is not the bound
            # `H-09` declares, and every eviction measurement reads off it.
            while len(p.ledger) > cap:
                # S20/S34: EVICTION RANKS ON `confidence_live x recency` ONLY, NEVER SALIENCE.
                # Rev 1 sorted lexicographically on (confidence, when), which is a different
                # comparator and degenerated to insertion order under a constant confidence.
                # ⚠ THROUGH THE GATE. This sorted and popped `p.ledger` DIRECTLY — no `write()`
                # call, on the row `W4` had just made an emitting row. #353 `:1061-1064` is
                # explicit: *"either the gate applies the write, or direct assignment is made
                # impossible"*, and eviction was the second half of that sentence going
                # unenforced. The gate requires an emission only at MATTER, so an INTERIOR
                # eviction passes without one — which is correct here and is also a finding worth
                # naming rather than papering over: **a claim leaving a ledger is a real state
                # change that Part D gives no kind, so nobody can witness a forgetting.** That is
                # `(Person, claim_ledger)`'s version of `H-86` and is recorded on that row.
                # Found by the `W4` adversarial pass.
                p.ledger.sort(key=lambda c: c.confidence * (c.when + 1))
                w.write("claim_ledger", WriteClass.INTERIOR,
                        lambda p=p: p.ledger.pop(0),
                        record_kind="Person", fieldname="claim_ledger", driver="Event")
        w._in_parallel_map = False
        # S9.3/S28: WITNESS NEVER TOUCHES A BELIEF. Nothing above writes `beliefs` or
        # `convictions` -- and under rev 2's Partition both are MISSING rows, so an attempt would
        # raise rather than be caught by inspection.
        TRACE.step("WITNESS", "leave")
        return deposits

    # -- CENSUS -- shares WITNESS's join (S29) ------------------------------
    def census(self) -> None:
        w = self.w
        w.step = Step.CENSUS
        TRACE.step("CENSUS", "enter")
        TRACE.decision("individuation", "S29",
                       chose="demand-driven only; generated nobody",
                       alternatives=["a clock that generates (forbidden)",
                                     "a world-gen roster (S54 item 18 -- not a clock, not folded in)"])
        # S29: DEMAND-DRIVEN ONLY. Nothing generates without a demand and NO CLOCK GENERATES
        # ANYTHING -- so this step writes nothing here. Rev 1 called the gate with an `apply`
        # that mutated nothing, which S30.2 calls "worse than no gate"; the call is gone rather
        # than made cosmetic.
        TRACE.step("CENSUS", "leave")

    # -- one season --------------------------------------------------------
    def season(self, choose, question, subsistence,
               actorless: Optional[list[Event]] = None,
               contest_max_depth: Optional[int] = None) -> dict:
        w = self.w
        w.draw = 0                 # S33: the draw ordinal is per-TICK, so replay is exact
        self.calendar()
        matter_events = self.matter(actorless)
        acts = self.deliberate(choose, question, subsistence)
        events = self.resolve(acts, contest_max_depth)
        for e in events:
            w.log.append(e)                  # S19.5 -- ONE LOG, NOT TWO
            TRACE.event(e.id, e.kind, e.causes)
        deposits = self.witness(matter_events + events)
        self.census()
        w.tick += 1
        return dict(acts=len(acts), events=len(events) + len(matter_events),
                    deposits=deposits, hash=w.content_hash())


# ===========================================================================
# S39 -- THE SEAM
# ===========================================================================

def contest_subsystem(prize: Any) -> Optional[dict]:
    """Which subsystem owns a contest for this prize, from `rosters.yaml` crossed with
    `references/module_contracts.yaml`.

    Neither half is invented here: the PRIZE is what Part E's `contests:` column carries, and the
    SUBSYSTEM is a module the contracts file already declares with a doc and a resolver. Returns
    `None` for a prize no roster row claims -- which is a real answer, not a failure, and leaves
    the generic refusal below it intact."""
    name = roster_map("contest_subsystems", "prizes").get(str(prize))
    if name is None:
        return None
    import yaml as _y
    contracts = files.MODULE_CONTRACTS_YAML
    if not contracts.exists():
        return dict(module=name, resolver="unknown", doc="module_contracts.yaml not found")
    for m in (_y.safe_load(contracts.read_text()) or {}).get("modules") or []:
        if m.get("module") == name:
            # ⚠ THE PYTHON, NOT THE MARKDOWN. Jordan, 2026-09-02: *"we aren't using the .md or
            # anything for those systems. those are super outdated."* The contracts file carries
            # both a `doc:` (markdown) and a `sim_module:` (the live Python) for these three, and
            # the first version of this refusal printed the `doc:` — so it pointed a reader at a
            # file its owner calls superseded, which is the stale-pointer defect this chain keeps
            # finding in other people's work. `sim_module` first, and where the contract has none
            # the tree is asked directly rather than falling back to the markdown.
            where = m.get("sim_module") or ""
            if not where:
                guess = files.subsystem_sim_dir(name)
                where = (f"systems/{name}/sim/" if guess.is_dir()
                         else f"(no `sim_module:` in module_contracts.yaml; "
                              f"`doc:` is {m.get('doc')!r} and is out of date)")
            return dict(module=name, resolver=m.get("resolver") or "undeclared", doc=where)
    raise Unspecified(
        f"`contest_subsystems` maps {prize!r} to {name!r}, which is in no module contract", "S39",
        needs="a module named in references/module_contracts.yaml",
        law="the roster may only name a subsystem the contracts file declares -- otherwise the "
            "dispatch target is invented")


# ---------------------------------------------------------------------------
# S39.4 -- THE DEGREE. TWO SOURCES, BOTH ALREADY RULED, NEITHER RE-DERIVED HERE.
#
# ⚠ THIS BLOCK IS `W-E`, AND IT EXISTS BECAUSE A PARTIAL SUCCESS AND AN OVERWHELMING ONE WERE
# THE SAME EVENT. Three links were broken at once and each hid the next: `_fold` hardcoded
# `_degree_for_writes = None`; `emits_at` had ZERO callers anywhere in the tracer (`H-113`), so a
# contested verb reported the FLAT UNION of every band; and `Event.degree` was a field nothing
# ever assigned. Closing any one alone changes nothing observable.
#
# THE TWO SOURCES, AND WHY THIS FILE MAY NOT CHOOSE BETWEEN THEM:
#
#   1. THE LADDER, for a contest whose subsystem returns a MARGIN. `S39.4` -- one ladder for
#      every scale, four bands read off the margin -- and the tree OWNS it:
#      `engine/autoload/dice_engine.py::degree_from_net`, whose docstring reads *"THE degree
#      ladder. Single owner for every scale of the game (Jordan ruling, 2026-08-14)"*.
#      ⚠ IT IS IMPORTED AND CALLED, NOT MIRRORED. `S27.2` names a second resolver as its
#      highest-value refusal, and a band table copied into this file WOULD BE ONE -- it would go
#      on answering after the owner changed its mind, which is exactly what happened to
#      `params_tables.yaml`'s captured ladder (`CLAUDE.md` §5: the capture still shows the
#      PRE-RULING bands). The falsifier that this is a call and not a copy is
#      `test_we_the_ladder_is_the_trees_and_not_a_copy_of_it`, which monkeypatches
#      `degree_from_net` and requires every margin here to follow it.
#      ⚠ AND ITS OPERAND DOES NOT EXIST YET, WHICH IS SAID HERE RATHER THAN DISCOVERED LATER.
#      `degree_from_net` reads `net - ob`. NOTHING IN THIS TRACER PRODUCES A `net`: there is no
#      roll anywhere in `shape.py`, `Act.pool` / `Act.obstacle` are read only by `S27.4`'s
#      refusal gate, and no subsystem the seam can call returns one. So this branch is a READER
#      WITH NO PRODUCER today. It is written anyway, and recorded on `H-98` -- whose own `cite:` lists
#      *give the ladder a margin the subsystem can supply* as one of its three options -- because the
#      alternative is worse in a specific way: without it the shape of the missing thing is a
#      guess, and with it the gap is exactly *"no subsystem returns a margin"* -- which is one of
#      the three options `H-98`'s own `cite:` lists.
#
#   2. THE SCENE, for a contest that routes to personal combat. JORDAN, 2026-09-03, VERBATIM:
#      *"kill/wound degrees should be directly taken from scene combat, which is what actually
#      needs to be called when kill/wound is considered."* And again, 2026-09-04: *"the combat
#      engine determines the result there. your code just has to accept the result."*
#      So combat is EXEMPT from the ladder by ruling, and its bands are a READ of the
#      `WoundTracker` the engine computed -- `combat_seam.resolve`'s `wound_state`.
#
# ⚠ THE BAND IS READ OFF **THE ACT'S SUBJECT**, NOT OFF "THE LOSER", AND THAT CORRECTS THE TABLE.
# `verb_table.yaml`'s `writes_source:` cell says `wound_state[loser]`. `kill / wound` writes on
# `payload["subject"]` (`_eff_kill`), so reading the LOSER kills the wrong person whenever the
# ACTOR is the one felled: A attacks B, B fells A, `wound_state[A].felled` is True, and the fold
# would delete B. The subject is the person the writes land on, so the subject is the person
# whose state decides which branch of the writes applies. The table's cell is corrected there.
# ---------------------------------------------------------------------------

# ⚠ THE THREE BANDS AND THE HARM MODEL ARE DATA, NOT LITERALS HERE — `rosters.yaml:
# combat_degree_bands` / `wound_harm_models`, bound at import beside every other roster (Jordan
# 2026-09-02: definitions are not hardcoded). `verb_table.yaml` keys `writes:`/`emits:` on the
# same three strings, and `writes_at`'s own refusal prints BOTH SETS when they disagree, so drift
# between the reading and the table is loud at the first act that folds.
# ⚠ A FOURTH BAND (decisive vs narrow) HAS NO SOURCE IN THE DATA and is NOT invented -- that is
# the whole of what survives in `H-98` after the 2026-09-03 ruling.

_LADDER: Optional[tuple] = None
_LADDER_ERROR: str = ""


def degree_ladder() -> Optional[tuple]:
    """`(degree_from_net, DEGREE_LABEL)` from the tree's owner, or `None` with a NAMED reason.

    Deferred and by path, which is `combat_seam.engine()`'s shape and for its reason: the tracer
    still runs where the engine tree is absent, degrading to a named gap rather than an
    ImportError at import. The repo root carries no top-level modules, so putting it on
    `sys.path` shadows none of this directory's bare-name imports."""
    global _LADDER, _LADDER_ERROR
    if _LADDER is not None or _LADDER_ERROR:
        return _LADDER
    root = files.REPO_ROOT
    try:
        if str(root) not in sys.path:
            sys.path.insert(0, str(root))
        from engine.autoload.dice_engine import (  # noqa: E402
            DEGREE_LABEL as _L, degree_from_net as _d)
        _LADDER = (_d, _L)
        return _LADDER
    except Exception as e:                        # a real import failure is a NAMED gap
        _LADDER_ERROR = f"{type(e).__name__}: {e}"
        return None


def ladder_error() -> str:
    degree_ladder()
    return _LADDER_ERROR


@dataclass
class Resolution:
    """WHAT THE SEAM RETURNED, AS THE FOLD SEES IT. `None` for an uncontested verb, and that is
    the whole of the uncontested path's change: `writes_at(None)`/`emits_at(None)` on a verb with
    no degree map return the flat tuples they always did.

    Two fields and no third. `degree` is the token `verb_table.yaml` keys on; `result` is the
    subsystem's own return, kept whole so an effect can read a quantity the SCENE computed rather
    than one this file made up."""
    degree: str
    result: dict


def combat_degree(result: dict, subject: Optional[str]) -> str:
    """The band, READ off the scene the engine just fought (Jordan, 2026-09-03). Invents nothing:
    every quantity below is a field of the engine's own `WoundTracker`, on the Combatants
    `combat_seam` constructed and still holds after `wrapper.fight` collapsed them to an int.

    `felled` and `result == 0` are the SAME event from the engine's side -- `wrapper.fight` sets a
    non-zero result only on a felling -- so the three bands are: the subject went down; the
    subject is standing and bled; the subject is standing and untouched."""
    states = result.get("wound_state") or {}
    st = states.get(subject)
    if not subject or st is None or not st.get("available"):
        raise Unspecified(
            f"personal combat resolved and the scene carries no wound state for the act's "
            f"subject ({subject!r}); it has {sorted(states)}", "S39.4/H-98",
            needs="a `wound_state` entry for the person the act writes on",
            law="Jordan 2026-09-03 -- the degree is READ OFF THE SCENE. A subject the scene never "
                "fought has no band, and picking one would be the mapping that ruling removed")
    if st["felled"]:
        return FELLED
    return WOUNDED if st["wounds"] > 0 else UNTOUCHED


def degree_of(result: Any, subject: Optional[str] = None) -> str:
    """THE ONE PLACE A SUBSYSTEM'S RESULT BECOMES THE TOKEN `writes_at` / `emits_at` KEY ON.

    ⚠ IT DECIDES NOTHING. Each branch hands the question to whoever already owns it -- the scene
    for combat, `degree_from_net` for a margin -- and a result carrying NEITHER refuses by name.
    That refusal is the honest state of `mass_battle` and `social_contest`, which the seam
    resolves and does not call (Jordan, 2026-09-02: *"we don't NEED to worry about them at this
    point in time"*)."""
    if not isinstance(result, dict):
        raise Unspecified(
            f"a contest returned {type(result).__name__}, which carries no outcome to grade",
            "S39.4", needs="a subsystem result",
            law="S39.4 -- the degree is the SUBSYSTEM's, read off what it returned")
    if "wound_state" in result:
        return combat_degree(result, subject)
    if "net" in result and "ob" in result:
        lad = degree_ladder()
        if lad is None:
            raise Unspecified(
                f"a contest returned a margin and the tree's degree ladder is unavailable: "
                f"{ladder_error()}", "S39.4",
                needs="engine/autoload/dice_engine.py",
                law="S27.2 -- the ladder is imported from its single owner. A band table copied "
                    "into this file would be the second resolver, and would keep answering "
                    "after the owner changed its mind")
        degree_from_net, label = lad
        return label[degree_from_net(result["net"], result["ob"])]
    raise Unspecified(
        f"a contest for {result.get('prize', result.get('module'))!r} resolved and returned "
        f"neither a scene to read nor a margin to grade (keys: {sorted(result)})",
        "S39.4/H-98",
        needs="a `wound_state` (the scene), or a `net`/`ob` pair (the margin the one ladder reads)",
        law="S39.4 -- FOUR BANDS READ OFF THE MARGIN, and Jordan 2026-09-03 exempts combat by "
            "reading them off the scene instead. A subsystem returning neither cannot be graded, "
            "and grading it anyway is the second resolver S27.2 refuses")


def contest(w: World, rung: str, prize: Any, claimants: list[str],
            depth: int, max_depth: int, causes: list[str],
            extension: Optional[Callable[[str], bool]] = None):
    """S39. EVERY ARGUMENT IS LOAD-BEARING. Attaches at EXACTLY ONE PLACE -- RESOLVE.

    REV 2. Rev 1 was THE SECOND RESOLVER -- S27.2's highest-value refusal, broken inside the
    seam. It hardcoded `band = "Partial"` with no margin, no pool and no obstacle; it guarded
    the demote-only veto with dead code; and it named THE MOST RECENT UNRELATED EVENT as its
    cause, which is worse than [ROOT] because it produces a plausible, wrong arc graph THAT
    WALKS. S39.4's ladder reads off the MARGIN and no in-chain document supplies a margin
    model, so the honest behaviour is to REFUSE (S42.2.1)."""
    if not claimants:
        raise Forbidden("contest with no claimants", "S39.1",
                        law="S39.1 -- claimant[] is PERSONS, ALWAYS. Not factions, not units, not sides")
    if prize is None:
        raise Forbidden("contest with no prize", "S39.1",
                        law="S39.1 -- A CONTEST WITH NO PRIZE IS A FIGHT SCENE, AND THIS ENGINE HAS NO USE FOR ONE")
    if not causes:
        raise Forbidden("contest called with causes=[]", "S39.2",
                        law="S39.2 line 2 -- Events, into the same log, WITH causes[] NAMING THE ACTS")
    # ⚠ A CONTEST IS A DISPATCH TO A SUBSYSTEM, NOT A GENERIC ROLL. Jordan, 2026-09-02: *"a
    # contest seems like it can be a call for a different subsystem like personal combat, mass
    # battle or social contest."* All three ARE BUILT -- `references/module_contracts.yaml` gives
    # each a doc, a sim module and a declared resolver (`d_sigma` for personal combat, `dice_pool`
    # for the other two). So this seam was never missing a degree ladder it had to invent; it was
    # failing to CALL the engine that owns the prize.
    #
    # Wiring those engines is out of this chain's scope (Jordan ruled only this proposal chain is
    # in scope), so the refusal below NAMES the subsystem and its resolver instead of reporting one
    # undifferentiated hole. That turns "the degree ladder's margin model is absent" -- which reads
    # as a missing design -- into "this act belongs to `personal_combat`, whose resolver is
    # `d_sigma`, and nothing connects them", which is a wiring statement somebody can act on.
    if depth >= max_depth:
        TRACE.decision("contest depth cap reached", "S39.3",
                       chose="typed error result returned to the caller",
                       alternatives=["recurse (a CRASH in GDScript, not a catchable error)"])
        return ContestError("max_depth reached", depth, max_depth)
    # ⚠ THE DISPATCH RUNS **AFTER** THE DEPTH CHECK, AND IT DID NOT. Raising here first made
    # `ContestError("max_depth reached")` UNREACHABLE for every prize the roster claims — so
    # `H-87`'s registered cap was a number no branch could read and its three-point sweep was a
    # set of arms identical by construction. Found by the governance-slice adversarial pass.
    # ⚠ AND THE FIX IS A MOVE, NOT A SECOND CHECK. My first attempt added a duplicate cap test
    # twelve lines above this one — §8 broken in the act of fixing an ordering bug.
    _sub = contest_subsystem(prize)
    if _sub is not None:
        # ⚠ THE SEAM CALLS NOW. Jordan, 2026-09-02: *"kill / wound points towards a seam that
        # should be calling in the personal combat system."* This block used to resolve the
        # subsystem by name and then REFUSE — a pointer, not a call — on a scope note that ruling
        # overrides. `combat_seam` is the IN-side, built on `engine/cross_scale/combat_bridge.py`'s
        # precedent rather than a new pattern.
        if _sub["module"] == "personal_combat":
            from . import combat_seam
            out = combat_seam.resolve(w, claimants, causes, prize)
            if out.get("status") == "RESOLVED":
                TRACE.decision(f"contest for {prize!r} dispatched", "S39",
                               chose=f"called {out['module']} (resolver {out['resolver']})",
                               alternatives=["invent a degree ladder in the seam (S27.2: the "
                                             "second resolver)"])
                return out
            # A gap in the CALL is named as a gap in the call, never as a missing design.
            raise Unspecified(
                f"a contest for {prize!r} routes to `{out['module']}` and the call did not "
                f"complete: {out.get('why')}", "S39",
                needs=out.get("status"),
                law="the seam DISPATCHES (Jordan 2026-09-02). A party the seam cannot derive is "
                    "a gap in the derivation, not a hole in the subsystem, and `combat_bridge` "
                    "sets the rule: return the gap, never fabricate a side")
        raise Unspecified(
            f"a contest for {prize!r} belongs to the `{_sub['module']}` subsystem "
            f"(resolver: {_sub['resolver']}), and nothing connects the seam to it", "S39",
            needs=f"the seam to call {_sub['module']} ({_sub['doc']})",
            law="Jordan 2026-09-02 -- a contest is a call for a different subsystem. The three "
                "are declared in references/module_contracts.yaml WITH resolvers, so the seam's "
                "job is to DISPATCH; inventing a degree ladder here would be a second resolver, "
                "which S27.2 names as its highest-value refusal. `personal_combat` is CALLED "
                "above; mass_battle and social_contest still resolve to a name only")
    raise Unspecified(
        "the degree ladder's margin model",
        "S39.4",
        needs="a margin -- pool, obstacle, and the four band edges read off it",
        law="S39.4 -- ONE degree ladder for every scale, FOUR BANDS READ OFF THE MARGIN, never off the obstacle's size. No in-chain document supplies the margin model, and S27.2 refuses a second resolver, an auto-resolve formula and a fast path -- so a band computed here without a margin IS the second resolver",
    )
