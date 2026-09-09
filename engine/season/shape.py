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
from .queries import world_q  # noqa: F401 -- world-first Query renames call `world_q.<name>` directly (step 7: `class Query` is gone)
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
from .epistemic import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    CHANNEL_PREDICATES, _ch_chronicle, _ch_co_located, _ch_document_key, _ch_post_remit,
    _ch_witness_key, _event_place, act_refs, belief_contradicts, claim_subjects, observers_for,
)
from . import decision  # noqa: F401 -- `decision.<name>` is the person-side call-site spelling, step 7
from .decision import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    _REFERENT_OPERANDS, _derive_operand, _payload_of, aggregate_questions, agreement, align,
    assemble, body_band_penalty, budget, containing_rung_of, entrenchment, make_chooser,
    opening_set, operands_for, pack_scenes, person_side_eligible, stance_toward, standing_of,
    store_kind_of, urgency, view_ids,
)
from . import seam  # noqa: F401 -- `seam.<name>` is the S39 dispatch call-site spelling, step 8
from .seam import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    ContestError, Resolution, combat_degree, contest, contest_subsystem, degree_ladder,
    degree_of, ladder_error,
)
# ⚠ `_LADDER`/`_LADDER_ERROR` are DELIBERATELY NOT re-exported here: `degree_ladder()`
# rebinds them through `global`, and a facade import captures a snapshot at load rather than
# reading `seam`'s live copy -- exactly the hazard `registers/handoffs/HANDOFF_IN.md` names
# for this move. Reach them as `seam._LADDER` / `seam._LADDER_ERROR`, never `S._LADDER`.

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
# for the two-phase `VERB_TABLE` assignment and why it is preserved unchanged.
#
# ⚠ CORRECTED, step 7: this paragraph used to end "...and for why `align()` (below, unmoved)
# still sees a sweep's rebind of `S.ALIGNMENT`." `align()` is NOT below any more -- it moved to
# `decision.py` at step 7 (this step), together with the other three names the test suite rebinds
# by assignment (`belief_contradicts`, `pack_scenes`). It now reads `decision`'s own `ALIGNMENT`
# (imported from `.data.verbs`, same as here), and the rebind sites are re-pointed to
# `decision.ALIGNMENT` in the same commit -- see `decision.py`'s docstring for why moving the
# READER rather than leaving a facade copy is what keeps the rebind live instead of turning it
# into a silent no-op.
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
# S17 -- QUERY. EXTRACTED WHOLE, step 7 of the decomposition.
#
# `class Query` is GONE. Its eleven resolver-side members were already bindings to
# `season.queries.world_q` (step 5) and nothing more; every `Query.<name>` call site in the
# package now reads `world_q.<name>` directly -- there is no facade left to bind through. Its
# four person-side statics -- `budget`, `opening_set`, `assemble`, `entrenchment` -- are MODULE
# FUNCTIONS in `season.decision` now, dedented out of the class body with nothing else changed.
#
# ⚠ THE QUOTATION THAT STOOD HERE WAS ATTRIBUTED TO `04_CODE_ARCHITECTURE.md` §A.3 ROW 2 AND IS
# NOT IN IT. It read: *"the class survives one more step only as the call-site facade; it goes at
# step 7, when the four person-side statics below become `decision`'s module functions."* Those
# are THIS FILE'S OWN step-5 words, deleted by this very commit -- the repository quoted itself
# and credited the spec, which is the anti-fabrication failure §7 names, arriving through prose
# rather than through a number. §A.3 row 2 actually reads: *"one `Query` class holding both
# families | two modules; the second cannot import the first | T-f. In one class, a person-side
# function calls a resolver-side one with no import to scan."* That row licenses the SPLIT and is
# silent on facades and step numbers. Falsifier: `rg -n "call-site facade" architecture/` -> 0.
#
# SEVENTEEN MORE TOP-LEVEL NAMES MOVED WITH THEM, in the same commit, all to `season.decision`:
# `align`, `stance_toward`, `urgency`, `make_chooser`, `person_side_eligible`,
# `containing_rung_of`, `store_kind_of`, `_derive_operand`, `_REFERENT_OPERANDS` (with its
# preceding comment block), `operands_for`, `agreement`, `standing_of`, `_payload_of`,
# `pack_scenes`, `aggregate_questions`, `view_ids`, `body_band_penalty`. `sense()`, further below
# in this file (after `stratum_of`/`resolvable_verbs`/`as_scenes`, none of which move here either),
# did NOT move -- it goes to `loop/driver.py` at step 9, and
# `04_CODE_ARCHITECTURE.md:116` is explicit that `sense()` is "called by the loop, never by the
# decision", so it never belonged in this batch.
#
# Imported at the top of this file (`from . import decision` + a re-export block) so every bare
# use of a moved name further down this file keeps resolving, and so `S.<name>` keeps resolving
# for the harness and tests: a re-export, not a second definition. See `decision.py`'s own
# docstring for the one declared edit inside a moved body (`make_chooser`'s `Query.opening_set(`
# call, now a bare `opening_set(` since both functions live in the same module) and for how the
# three test/arm rebinds (`ALIGNMENT`, `belief_contradicts`, `pack_scenes`) are re-pointed in
# this same step.
# ===========================================================================




# `ALIGNMENT_SWEEP` and `alignment_at` moved to `season.data.verbs` (step 3), imported back at
# the top of this file.
#
# ⚠ CORRECTED, step 7: this comment used to continue "`align()`, directly below, did NOT move --
# it is the per-call reader (`decision/` territory, a later step), not part of the table." That
# was true when it was written (step 3) and is false now: `align()` moved to `season.decision` in
# THIS step -- it was always going to (this sentence said so, naming `decision/` as its eventual
# home), and "a later step" has arrived. See the S17/QUERY breadcrumb above for the full list of
# what moved with it.


# `belief_contradicts` moved to `season.epistemic` (step 6) -- §F1 clause 4, the one place a
# person's OWN ledger can refuse a candidate. Imported back at the top of this file.
#
# ⚠ CORRECTED, step 7: this paragraph used to read "ITS ONE BARE-NAME CALLER IS `Query.opening_set`
# BELOW", present tense -- true when it was written (step 6), false now. Step 7 (this step) moved
# `opening_set` to `season.decision`, and `belief_contradicts`'s only in-package caller went with
# it, so the caller now resolves the name in `decision`'s OWN globals (imported unaliased from
# `.epistemic` at the top of that file), not this module's. `S.belief_contradicts` WAS rebound at
# EIGHT assignment lines in TWO files -- four in the suite's `test_wb_clause_four_fires_...`
# (:7069, :7080, :7097, :7107) and four in `proposals/2026-09-04-degree-sweep/wd_acceptance.py`
# (:283, :288, :401, :405); half of each set installs a wrapper and half restores the original.
# ⚠ AN EARLIER VERSION OF THIS COMMENT SAID "SIX SITES ... FOUR AND TWO", WHICH RECONCILED ON NO
# BASIS -- it mixed lines in one file with installs in the other.
# ⚠ AND `belief_contradicts` WAS NOT THE ONLY SUCH NAME: `ALIGNMENT` (4 lines, suite) and
# `pack_scenes` (8 lines, three degree-sweep arms) are rebound by the same mechanism, and
# `pack_scenes` was absent from the decomposition plan's own hazard list. **All three readers moved
# to `decision` in this same step, and the suite's four `test:7069`-family sites are re-pointed to
# `decision.belief_contradicts` in the same commit** -- closing, rather than merely predicting,
# the hazard the previous version of this comment described ("it will resolve the name in
# `decision`'s globals instead, and every one of those rebinds becomes a no-op on it"). That
# sentence was a forecast; this edit is the fix it forecast needing. ⚠ **NOT "SILENT", WHICH THIS
# COMMENT ALSO ONCE CLAIMED.** All three names are caught by an existing assertion: this one by the
# falsifier below, `ALIGNMENT` by `test:2376`'s uniform control, `pack_scenes` by the arms'
# `in_budget` consumer. ⚠ AND THERE IS NO SILENT RESIDUE, BECAUSE THE PREMISE THAT CREATED ONE WAS
# FALSE. What stood here said *"`wd_acceptance.py` and `arm7_flexibility.py` are imported by
# nothing, so they cannot fail the suite"* -- inherited from the decomposition plan's §2.3,
# repeated by the step brief and by the commit message, and refuted by one grep:
# `rg -n "import (arm7_flexibility|wd_acceptance)"` returns `sweep.py:19` (which RUNS arm7 at
# `:111`) and six importers of `wd_acceptance`. Both are re-pointed to `sweep_core.PS` in the same
# commit, so all three rebind families now reach the module their reader lives in.
# The falsifier is not vacuous:
# `test_wb_clause_four_fires_in_the_corpus_at_the_shipped_default_and_not_at_the_control`
# asserts `live` is non-empty and says in its own message *"or the deposit no longer reaches
# `belief_contradicts`"*.


# `questions_for` moved to `season.queries.world_q` (step 5). It takes a `World` FIRST and a
# `Person` second, which is what makes it a world query rather than a person-side one -- the
# distinction `test_w5_sense_is_still_the_only_world_taking_non_decision_function` checks by
# SIGNATURE, so it survives the move as a checkable property rather than as this sentence.
# Imported back at the top of this file.


# `act_refs` and `claim_subjects` moved to `season.epistemic` (step 6) -- they decide what a
# deposit is ABOUT, which is the same question the channels answer from the other end. Imported
# back at the top of this file.


# `occasioned_by` moved to `season.queries.world_q` (step 5) -- it takes a `World` first and asks
# it which acts a question is occasioned by. Imported back at the top of this file.


# ===========================================================================
# `W6` -- THE FIVE WITNESS CHANNEL PREDICATES, AND WHO OBSERVES AN EVENT.
#
# EXTRACTED, step 6 of the decomposition: `_event_place`, the five `_ch_*`, the roster-built
# `CHANNEL_PREDICATES` table and `observers_for` now live in `season.epistemic`.
#
# THE TABLE, ITS LOOP AND ITS `del` MOVED AS ONE BLOCK, and had to: `CHANNEL_PREDICATES` is
# built by asking the DEFINING MODULE's `globals()` for `_ch_<name>` for every channel in
# `rosters.yaml`. Leave the five predicates behind and the loop raises at import -- loud, which
# is the good case, and the reason this is a block rather than three statements. It is the
# package's second `globals()` lookup; `state/carriers.py` records the first, and both travel
# with the definitions they read.
#
# Imported at the top of this file so every bare use further down keeps resolving, and so
# `S.CHANNEL_PREDICATES` keeps resolving for the harness and tests: a re-export, not a second
# definition.
# ===========================================================================






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

# ===========================================================================
# THE SEASON LOOP -- EXTRACTED, step 9 of the decomposition (a PURE MOVE).
#
# `SeasonDriver` and the five functions around it -- `stratum_of`, `resolvable_verbs`,
# `as_scenes`, `sense`, `names_a_verb` -- plus the #353 source reader (`_S353_CACHE` /
# `SOURCE_353_TEXT`) now live in `season.loop.driver`. Whole bodies, byte-identical: three tests
# read `SeasonDriver.witness`'s own source through `inspect.getsource`, and one of them is a
# NEGATIVE assertion, so a delegating stub here would fail two and silently vacate the third.
#
# ⚠ `loop/driver.py`, NOT `loop.py`: `season.loop` has been a PACKAGE since step 5, so a sibling
# module of that name would be shadowed.
#
# `sense()` went here rather than to `decision.py`. It takes a `World`, and `decision.py` may not
# name one (AX-2); `04_CODE_ARCHITECTURE.md:116` says `sense()` is *"called by the loop, never by
# the decision"*.
#
# WHAT IS LEFT IN THIS FILE IS NOW ONLY THE FACADE. Every name it exports is defined elsewhere
# and imported back, which is what makes step 10 a deletion rather than a carve.
# ===========================================================================
from .loop.driver import (  # noqa: F401 -- re-exported so `S.<name>` and every bare use resolve
    SOURCE_353_TEXT, SeasonDriver, _S353_CACHE, as_scenes, names_a_verb, resolvable_verbs,
    sense, stratum_of,
)
