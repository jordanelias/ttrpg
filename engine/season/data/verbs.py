"""`season.data.verbs` -- the verb table and the alignment table.

Owns `VerbRow` and its loader (`_load_verb_table`/`VERB_TABLE`), the load-time constants a row is
checked against (`VERB_TABLE_YAML`, `ELIGIBILITY_KINDS`), `NO_PRECONDITION` (the "no cell" prose
sentinel both `requires` and `requires_typed` use), `rows_without_a_producer` (§7.2's report,
which reads `VERB_TABLE`), and the alignment table in full: its loader
(`_load_alignment`/`ALIGNMENT`), its immutable baseline (`ALIGNMENT_DECLARED`,
`ALIGNMENT_DEFAULT_CELL`), and its sweep (`ALIGNMENT_SWEEP`/`alignment_at`).

`verb_table.yaml` is Part E's body, loaded once at import: *"#353 types `resolve : (Act[],
World) -> Event[]` and never says what any verb DOES... with no table, every act needed a
hand-written `effect` lambda, and A LAMBDA PER ACT IS A SECOND RESOLVER."*

`_load_verb_table` calls `season.data.requires.build_typed_requires` once per row -- see that
module's docstring for the ordering constraint this creates and how it is satisfied structurally
by THIS module's own import of `requires`, below, rather than by file position.

⚠ `align()` AND `align_kind()` LIVE HERE, BESIDE THE TABLE THEY READ. The `ALIGNMENT` binding and
its only reader share this module, so the rebind that moves one moves the other: the `H-66` sweep
and the `H-146` tests rebind `data.verbs.ALIGNMENT`, and nothing else binds the name. Every reader (`choose`'s score, `refuses`, `person_q._pursuits_violated_by`, `corpus_run`) calls
`align`; tests that import `ALIGNMENT` do so function-locally and read it live -- a copy imported
by name at module scope would be a stale snapshot.
"""

from __future__ import annotations

import ast
from dataclasses import dataclass, field, fields, replace
from typing import Optional

from . import files, rosters as _rosters
from ...substrate.descriptors import ATTRIBUTES, CAPABILITIES
from ..gaps import Forbidden, InstrumentDefect, Ungraded, Unspecified
from .arrangements import ARRANGEMENTS, _DISPOSES_LITERALS
from .matrix import MATRIX, Step
from .requires import (
    CELL_STEMS, KNOWN_PERSON_OPERANDS, RECORD_SOURCED_OPERANDS, REQUIRES_OPERANDS, VIA, AllOf, Existence, Relation,
    ScalarThreshold, TypedRequires, WITH_STEM, build_typed_requires,
)
from .rosters import (
    CONTEXT_KEY, COVERT_KINDS, DEGREE_BANDS, DIFFICULTY_LEVELS, LOOK_READS, DOMINANCE_KINDS, BOOKKEEPING_VERBS, CONTEST_OWED, FOLD_KINDS, LOGGED_KINDS, GRADED_TASKS, MARCH_POSTURE_KEY, MARCH_POSTURES, PROCEEDING_MOVES, ORDER_RETREAT_AT, ORDER_RETREAT_KEY, ORDER_ROLE_KEY, ORDER_ROLES, PERSON_DEMANDED, PROCLAIMED, PURSUIT_AXES, PURSUITS, READ_TO_ADDRESSEE, RECORD_KINDS, REFERENT_CLASSES, RELEASABLE_KINDS,
    RESTRAINT_KINDS, STANDING_OCCASION_OPENED_BY, STRIFE_KINDS,
    SCRUPLE_OVERRIDDEN, is_event_kind, refusing_pole,
    STRATA, TENURE_KINDS, THREAD_OPERATIONS, UNDEPOSITED_KINDS, load_yaml, require_member, roster,
    roster_map,
    table,
    table_meta,
)

VERB_TABLE_YAML = files.VERB_TABLE_YAML

ELIGIBILITY_KINDS = roster("eligibility_kinds")
REGARD_SIGNS = roster("regard_signs")          # B10.11: the closed set of a row's `regard_sign:` (`VerbRow.regard_sign`)

# The "no cell" prose sentinel `requires` and `requires_typed` use. Defined ABOVE the loader because
# loader invariant 4 reads it at load.
NO_PRECONDITION = ("—", "-", "")

# Loader invariant 9's roster: the prizes `contest_subsystems` claims, read once at load.
_PRIZES = roster_map("contest_subsystems", "prizes")
_CONTEST_PRIZES = frozenset(_PRIZES)

BENEFICIARY_KINDS = roster("beneficiary_kinds")
# ⚠ WHICH BENEFICIARY KINDS NEED A CELL TO BIND -- READ FROM THE ROSTER, NEVER LISTED HERE.
# `beneficiary_kinds.carriage` classifies every member `structural` or `operand`:
#   structural -- the carrier is on the Candidate regardless of the row's `requires_typed`
#                 (`actor` is held unconditionally, `subject` is a field, `none` carries nothing);
#   operand    -- carried only where the row's own cell binds or admits it, so invariant 13's
#                 third check must verify carriability for it.
# ⚠⚠ A hand-kept list of either half (`test_jordan_no_definition_is_hardcoded_in_a_body` (retired)) would
# silently stop covering a member the moment `rosters.yaml` gains one. A new member with no
# `carriage:` entry REFUSES at load, so the check cannot fall behind the roster.
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
class Look:
    """ONE THING A ROW'S ACT LOOKS AT (B11.71, `08_FI_03` §2, FRES §8): the operand it looks at (`of`, a `requires_operands` member the row's own
    cell binds) and the `rosters.yaml: look_reads` member it reads there (`read`). It names what is looked at and NEVER A BAND: which reads a
    band deposits is `rosters.yaml: finding_terms`'s, the one band-keyed table. `queries/world_q.py::WorldReader.look` answers it (`.looks` for a whole row)."""
    of: str
    read: str


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
    # ⚠ PART E'S `contests:` COLUMN. `ARCHITECTURE_V2.md:394` declares it — *"`contests: <prize> |
    # none` — if set, ROUTES TO THE SEAM AT RESOLVE (§39)"* — and `:434` sets it on `kill / wound`
    # (*"`contests: the body` → the seam"*). Jordan, 2026-09-02: *"that…would trigger the personal
    # combat scene. you can't just kill or wound imo."*
    contests: str = ""
    # ⚠ THE SIXTH COLUMN (#358 rev.2 §C.4 / F6, loader invariant 12). A flat `writes` is applied
    # UNCONDITIONALLY AFTER THE SEAM RESOLVED, so a LOST contest would write what a won one did.
    # A resolution whose result is discarded is not a weak outcome model; it is a contest that did
    # not happen.
    #
    # A verb WITHOUT `contests:` keeps the flat tuple and this stays empty.
    # A verb WITH `contests:` declares `writes` as a MAP from degree, and `writes` holds the union
    # (so the load-time Part D check below still sees every pair it must validate).
    writes_by_degree: dict = field(default_factory=dict)
    # ⚠ AND SO IS `emits:`, FOR THE SAME REASON ONE FIELD DEEPER. A flat `emits` on a contested
    # verb reports ONE outcome for every band, which is ID-9's class (a success report for
    # something that did not happen) inside the epistemic layer, where every witness then mints a
    # claim from it.
    emits_by_degree: dict = field(default_factory=dict)
    # ⚠ THE SEVENTH COLUMN (`W-A`). THE PROSE `requires` STAYS BESIDE IT AND
    # IS THE PROVENANCE -- each cell names the §E3 line it was transcribed from, so the derivation
    # can be checked rather than trusted. `None` means the column is NOT typed for this verb and
    # the fold falls back to `REQUIRES_PREDICATES`, which for a verb with no predicate is the
    # existing refusal naming what is missing.
    requires_typed: Optional["TypedRequires"] = None
    # Why a row carries `requires_typed: none`. Required BY THE LOADER on such a row: an untyped
    # cell with no reason is indistinguishable from one nobody got to.
    requires_typed_note: str = ""
    # ⚠ THE EIGHTH COLUMN. WHO THE ACT IS TAKEN FOR THE GOOD OF -- a `beneficiary_kinds` member,
    # resolving to a carrier THE CANDIDATE ALREADY HOLDS. `CAT-2`: *"DECLARE IT -- and declare it
    # as a STATIC COLUMN ON `verb_table.yaml` ... NOT as a fifth field on `Candidate`."*
    #
    # ⚠ DERIVING THE BENEFICIARY FROM THE OPERAND BINDING FAILS: most verbs are UNTYPED and can
    # carry no operand at all. A post-hoc attribution modifier is dead by Jordan's own
    # correction -- orientation is a weight AT APPRAISAL, not a rescoring of what a win was worth.
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
    # ⚠ THE NINTH COLUMN -- THE OTHER PARTY, NAMED BY THE OPERAND THAT CARRIES THEM. `ED-IN-0210` ruling 1: *a real interaction has a COUNTERPARTY, an OBSTACLE
    # and a DEGREE*; ruling 2: `petition` is *the first in the set where a counterparty is
    # structurally required*. `decision/options.py::opening_set` reads it and forms no Candidate
    # whose counterparty is the person themselves -- the contested-verb rule beside it (`contests:`
    # makes `subject` the second claimant), generalised to a row that names its counterparty
    # directly. `""` is the declared absence; the loader requires a named operand to be one the
    # row's typed cell BINDS, so the Candidate always carries the thing compared -- or, on an
    # UNTYPED row (`oblige`), a `requires_operands` member no Candidate can carry, which makes
    # `opening_set` form none: a second party the grammar cannot yet name. The same column is asked
    # again IN THE FOLD (`loop/resolve.py::_admits`, `COUNTERPARTY_CLAUSE`), for the hand-built act
    # no person forms.
    counterparty: str = ""
    # ⚠ THE TENTH COLUMN'S SECOND SHAPE -- `04 §B.13` INVARIANT 4'S PER-CONJUNCT HALF (F7): *"every failable clause has a refusal kind -- not only a verb with a
    # `requires`, but each CONJUNCT of it, and any eligibility alternative that can decline."* §C.4's
    # fold spells the reader: `emit(row.refusal_for(ELIGIBILITY))` and
    # `emit(row.refusal_for(failed_conjunct))`. A row may declare `emits_on_refusal:` as a MAPPING
    # from a FAILABLE CLAUSE to its kinds, and this holds it; `emits_on_refusal` above holds the
    # UNION, so every reader that asks *is this Event one of the row's refusals* (`corpus_run`,
    # `loop/driver.py`, `loop/deliberate.py`) is unchanged. `writes`/`writes_by_degree` is the
    # precedent, one column over. Empty = a flat row, whose every refusal emits the flat tuple.
    refusals_by_clause: dict = field(default_factory=dict)
    # ⚠ THE TWO DECLARED ABSENCES A DRIVER-CONSTRUCTION REFUSAL READS (`SM-9` + `SM-11`). Each is the row SAYING WHY the fold cannot carry it, so `resolvable_verbs()` drops it
    # with a reason on record rather than without a word; `manifest/registry.py` refuses both
    # directions -- a gap with no note, and a note on a row that has no gap (for `effect_decline_note:`
    # a row that has an effect or writes nothing).
    #
    # `effect_decline_note:` -- the row WRITES and no `@effect_for` body exists, and here is why
    # (refusal (a), `check_effects`). The formation half is `formation_decline_note:`, an annotation
    # this loader ignores (its `*_note` rule) and no gate reads -- a row whose effect EXISTS is
    # resolvable, and why nobody forms it is a reader's fact.
    effect_decline_note: str = ""
    # `requires_decline_note:` -- the row has a precondition that NOTHING EVALUATES (no typed cell, no
    # `REQUIRES_PREDICATES` entry), and here is why (`check_preconditions`). NOT `requires_typed_note`, which says why the cell is untyped and stands on rows a
    # registered predicate DOES evaluate (`oblige`, `release`).
    requires_decline_note: str = ""
    # IN-53 (H-207): THE REFERENT CLASS -- the carrier type (`Office`) a Candidate of this verb must
    # be ABOUT. `""` is the declared absence: the verb forms on the question's PLAIN referents. A named class must be a `rosters.yaml: referent_classes` value or the
    # load refuses; the verb then forms ONLY on referents the question carries as that class, and
    # never on its plain ones (`referents_of`, `Question.referents_for`): the class is a PARTITION
    # (DECISION 2026-10-13 D1), so a classed referent never reaches an undeclared row. It exists
    # because `opening_set` has no World (L2) and cannot ask what kind of thing a referent is:
    # `confer` formed on every rung, person, Record and Site a question named and was refused by
    # the fold on every one.
    referent_class: str = ""
    # IN-53 (H-207, DECISION 2026-10-13 D2): MAY THE COUNTERPARTY BE THE PERSON THEMSELF? `False`
    # (every row but one) keeps ED-IN-0210's counterparty clause as it was: no Candidate, and no
    # admitted act, whose counterparty is its actor. `True` (`confer`: the lord who assumes a vacant
    # seat) adds the person to the known persons the fan ranges over (`decision/options.py::
    # operand_bags`) and waives the self-exclusion at both counterparty sites (`opening_set`,
    # `loop/resolve.py::_admits`). The loader admits it only on a row whose counterparty a known
    # person fills (`known_person_operands`), the only rows the fan reaches.
    counterparty_may_be_self: bool = False
    # IN-10 (a) (H-203, DECISION 2026-10-13): MUST A CLASSED REFERENT BE ONE THE PERSON WAS TOLD OF?
    # `False` (every row but one): the row forms on every referent its class partition yields -- for
    # `confer`, the vacancies `world_q.vacancies` stamps, which no ledger names. `True` (`oblige`):
    # only on a referent the person's OWN LEDGER names (`queries/person_q.py::ledger_names`: a
    # deposit about it, or a held document whose `terms` it is -- #453 K-25), asked person-side in
    # `decision/options.py::opening_set` with no World (L2). The loader admits it only beside a
    # `referent_class:`; one class, two sources, and this column is which one a row may answer.
    referent_named: bool = False
    # v10 CP-T05-02 (iii) (AM-D-02): MAY THE SUBJECT BE THE PERSON THEMSELF? `False` (every row but one)
    # keeps `opening_set`'s self-subject decline: a person is not their own adversary on a row contested
    # against its subject (`decision/options.py::subject_is_opponent`). `True` (`speak`: a docketed party
    # answers to his own matter) waives that decline for the row declaring it, and for that row alone. NOT
    # `counterparty_may_be_self`, which waives the COUNTERPARTY operand's self-exclusion (`confer`). The
    # loader admits it only on a row `subject_is_opponent` reads as contested against its subject.
    subject_may_be_self: bool = False
    # B03.68 (`09_WR_threadwork_module` edit 3): WHICH THREAD OPERATION THE ROW PERFORMS, a `thread_operations`
    # member (`rosters.yaml`; leap, weave, pull, ...). `""` is the declared absence, every row today: the thread
    # rows that name an operation are B35's (CP-T07-03, -04, -11). The loader refuses a value outside the roster,
    # so a row naming a working the threadwork module does not have never loads.
    operation: str = ""
    # B04.03 (U1-A step 2): THE SKILL THE ROW TESTS -- a `descriptors.CAPABILITIES` id, or `none`, spelled. `""` is
    # the declared absence on a row that neither contests nor is graded (nothing there draws dice from a skill). The
    # loader requires it on every contested or graded row (no default by omission), refuses a value that is neither a
    # skill nor `none`, and refuses `none` with no `capability_note:` saying why nobody has a skill there.
    capability: str = ""
    # B05.25 (B05.24's row shape, `proposals/2026-11-13-verb-governing-attributes.md` §0): ONE KIND PER ROW. (a) `brute` --
    # `seat`, `own` or `counterparty`, with `brute_note` saying what authorises the act: it never rolls, it happens when its
    # gate is met and is refused at formation when it is not. (b) `governing` -- one to three `descriptors.ATTRIBUTES` keys,
    # averaged into his governing score for the verb (`pool.py::governing_score`), with `opposed_attribute` the one key a
    # person opposite resists it with, on a row contested against a person. (c) neither: the row's `contests:` prize says
    # `person_inputs: own` and the module it hands the act to reads the person by its own rule. `_check_governing_attributes`
    # refuses any other shape at import.
    governing: tuple = ()
    opposed_attribute: Optional[str] = None
    brute: Optional[str] = None
    brute_note: str = ""
    # B05.14 (SC-B Edit A; D-U1-04): HOW HARD THE ACT ITSELF IS -- a member of `rosters.yaml: difficulty_levels` (`Fixtures.difficulty_ob` sizes it),
    # on every row the social roll deals (a `contests:` prize its provider resolves, or a `graded_tasks` route to it) and on no other: the
    # loader refuses a rolled row with none and any other row with one (`social_rolled`). `None` is the declared absence, a row nothing rolls.
    difficulty: Optional[str] = None
    # B10.11 (`02_CHAR_scar_cap_and_regard_unit` Addendum; H-337, H-282): THE SIGN OF REGARD -- whether a person's liking for the act's subject pulls him
    # toward the act (+1), away from it (-1) or not at all (0); a `rosters.yaml: regard_signs` member, read by `decision/choose.py::_stance_arm`
    # under `stance_polarity: declared`. The loader fills the absence (`None`) with the sign the table read before the column: `-1` where
    # `opposed_to_subject(...)` (`contested_against_subject()` and the `opposed_without_prize` rows), else `+1`, so a row with no cell reads as it always did and every row carries a sign after the load.
    # ⚠ LAYER 1, NAMED AT THE SITE: a verb column meets `04` §B.13 (*a property of a roster member travels with the roster*) against §C.4 (*a
    # verb needing more columns is one the design has not finished thinking about*). The column is picked, as U1 §1 picks `capability:`,
    # because a loader default makes a missing value explicit and refusable (B4's third disposition); `04` is not edited.
    regard_sign: Optional[int] = None
    # B11.65 (`18_DETERMINISM_notice_is_a_draw` edit 1): IS THE ROW'S DEED DONE TO BE SEEN -- one that those present learn without a draw,
    # as a public act in ordinary speech is one done openly. A boolean, REQUIRED ON EVERY ROW and never derived from the verb's name: the
    # loader refuses a row that omits it or writes a non-boolean (a string, an integer, a null). Read by `epistemic.py::notice` (B11.66): a `public`
    # row's deed draws no notice for a person its precedence-head channel admits. ⚠ LAYER 1, NAMED AT THE SITE, as `regard_sign` above: `04` §B.13 inv. 10 admits the key once the loader knows it; `04` is not edited.
    public: bool = False
    # B11.71 (`08_FI_03` §2, FRES §8): WHAT AN ACT OF THIS ROW LOOKS AT BESIDE THE READS ITS OWN CELL MAKES -- a FLAT list of `Look`s (`observes:`), the
    # non-gating reads the fold takes and attaches to the act's Events as `Observation`s; WITNESS deposits the ones the Event's band lists in
    # `rosters.yaml: finding_terms` (the actor's own reads, as every observation). `()` is the declared absence (every row but three). ⚠ LAYER 1,
    # NAMED AT THE SITE, as `public` above: `04` §B.13 inv. 10 admits the key once the loader knows it; `04` is not edited.
    observes: tuple = ()
    # B24p.16 (RD §D.1; V2 p2 §M): HOW THE VERB PROCEEDS -- a verb that influences a person by words opens a proceeding, and its row says WHICH and in what
    # form (R3, R6). A tuple of `(when, row, form, move, item)` entries, the first whose `when` holds read (`world_q.proceeding_row`): `when` a tuple of
    # `(key, value)` pairs (`hearer`: `cohort`; `docketed`: `True`), empty for the fallback that closes every list; `row` an arrangement id, or `docket` (the
    # row the docket hears the matter under); `form` `full`, `abridged` or `auto`; `move` a `proceeding_moves` member that draws (`argue`); `item` `any`, or
    # `false` (the speaker is offered his own false items only, `person_q.false_items`: a `lie` is an `argue` on his own false word, V2 p2 §M).
    # `()` is the declared absence, every row but five; `seam/contest.py::contest` reads it (B24p.19) and the provider runs the proceeding for such a row, so
    # a row that proceeds names no `governing:` and no `opposed_attribute:` (refused by `_check_proceeds`).
    proceeds: tuple = ()
    # B21.07 (VB-A commit A1): THE TENURE KINDS THIS ROW CLOSES, its `domain:` column (`release`'s, asserted against `RELEASABLE_KINDS` below;
    # `pardon`'s `[detain, ban]`); `()` for a row that closes nothing. The loader already read the column for loader invariant 6 and kept it
    # nowhere; `OWN_EDGE_DECLINES` is its first reader after the load, so the row carries it rather than a second parse of the file.
    domain: tuple = ()

    def referents_of(self, q) -> tuple:
        """THE REFERENTS OF QUESTION `q` A CANDIDATE OF THIS VERB MAY BE FORMED ON: `q`'s plain
        referents when the row declares no `referent_class:`, else only those `q` carries as that
        class (`Question.referents_for`). The one owner of the partition; `opening_set` iterates it."""
        return q.referents_for(self.referent_class or None)

    def self_counterparty_refused(self, other, actor) -> bool:
        """IS `other`, ON THIS ROW'S COUNTERPARTY OPERAND, NO SECOND PARTY? Nobody (`None`) always;
        the actor himself unless the row declares `counterparty_may_be_self`. The one owner of the
        test `opening_set` (person-side) and `loop/resolve.py::_admits` (the fold) both ask."""
        return other is None or (other == actor and not self.counterparty_may_be_self)

    def opponent_operand(self) -> str:
        """THE PAYLOAD OPERAND AN ACT OF THIS ROW CONTESTS AGAINST: its `counterparty:` when the row names one, else
        `subject` (telling workplan `T4`, `ED-IN-0282`: `tell` contests against its hearer `to`; `fight` and `march`
        name none and read `subject`). The one owner of that rule, asked by `loop/resolve.py` (the fold's `_target`)
        and `decision/options.py::subject_is_opponent`."""
        return self.counterparty or "subject"

    def contested_against_subject(self) -> bool:
        """WHETHER AN ACT OF THIS ROW IS CONTESTED AGAINST ITS `subject`: it declares a prize (`contests:`) and its
        opponent operand is `subject`. The one owner of the test `decision/options.py::subject_is_opponent` and the
        loader's `subject_may_be_self` refusal both ask."""
        return bool(self.contests) and self.opponent_operand() == "subject"

    def opposed_to_subject(self, opposed_without_prize) -> bool:
        """WHETHER AN ACT OF THIS ROW IS DONE AGAINST ITS `subject`: it is contested against it, or it names no prize and is listed in
        `opposed_without_prize` (`rosters.yaml`, B11 lane A) with the subject for its second side. The one owner of the test
        `decision/options.py::subject_is_opponent` (the roster module-global it passes) and the loader's `regard_sign` default (the roster,
        read before the module-global exists) both ask."""
        return self.contested_against_subject() or (
            self.verb in opposed_without_prize and self.opponent_operand() == "subject")

    def with_operands(self) -> tuple:
        """THE `of:` OPERANDS OF THE ROW'S `relation: with` CONJUNCTS (v12 B11.69, `14_VERBS_SOCIAL1_A` edit 3): the operands the cell asks to
        be WITH the actor -- `to` for `tell`, `lie`, `give`, `argue`, `accept`; `subject` for `tend`, `train`, `challenge`, `fight`, `capture`. Read off the typed
        cell's TOP-LEVEL clauses (an `AllOf`'s, or the lone clause; a `with` nested under another conjunction is not seen, no shipped cell nests
        one) by the relation's stem, never a verb name; an untyped row has none. The ONE reader of that conjunct at formation: where the
        person is offered an act (`decision/options.py::opening_set`) and which bags he forms (`::_person_bags`) both ask it."""
        req = self.requires_typed
        if req is None:
            return ()
        top = req.requirement
        return tuple(dict.fromkeys(c.of for c in (top.clauses if isinstance(top, AllOf) else (top,))
                                   if isinstance(c, Relation) and c.relation == WITH_STEM))

    def known_person_operands(self) -> tuple:
        """THE OPERANDS A CANDIDATE OF THIS ROW TAKES FROM SOMEBODY THE PERSON KNOWS, one bag per
        person known (`decision/options.py::operand_bags`) -- the ONE owner, read by `operand_bags`
        and `act_key`.

        A TYPED row answers its cell's (`TypedRequires.known_person_operands`: `tell`'s and `give`'s
        `to`, beside a bound `subject`). An UNTYPED row carries nothing, EXCEPT the one second party
        it names that a known person can fill: its `counterparty:` where that is a
        `known_person_operands` member (IN-53: `confer`'s `to`, the conferee, beside the office as
        `subject`). Any other untyped counterparty (`oblige`'s `subject`) is filled by no known
        person -- no fan; since IN-10 (a) `oblige`'s seat is the classed referent the Candidate is
        formed on (`decision/options.py::_operands`). Read off the row's columns and the roster; no
        verb name."""
        if self.requires_typed is not None:
            return self.requires_typed.known_person_operands()
        return ((self.counterparty,)
                if self.counterparty and self.counterparty in KNOWN_PERSON_OPERANDS else ())

    def commanded_operand(self) -> Optional[str]:
        """THE OPERAND THIS ROW ORDERS -- the person the seat must command (B21.55, A-22) -- or `None` for a row that orders nobody.
        The ONE owner `decision/options.py::operand_bags` reads. A TYPED row answers its cell's: the operand of a `basis`
        conjunct under the `command` rule (`issue`'s `to`). An UNTYPED row, whose cell no clause can carry, answers `subject`
        when `rosters.yaml: command_declines` names it (`dispatch`, whose predicate asks the same rule in the fold). Read off the
        cell and the roster; no verb name."""
        if self.requires_typed is not None:
            ops = self.requires_typed.command_operands()
            return ops[0] if ops else None
        return "subject" if self.verb in COMMAND_DECLINES else None

    def precondition_evaluable(self, predicates) -> bool:
        """Can the fold evaluate this row's precondition: none at all, a typed cell, or a
        `predicates` (`loop/predicates.py::REQUIRES_PREDICATES`) entry. The ONE answer
        `resolvable_verbs()`'s first gate and `check_preconditions` both read (`CLAUDE.md` §8);
        `loop/resolve.py::_admits` (which `_fold` calls) branches the same three ways. `predicates`
        is a parameter because this loader may not import `loop/`.

        B09.19: A KEYED PREDICATE ROW IS ADMITTED ONLY WHEN ITS PREDICATE KEYS ARE EXACTLY THE CLAUSES THE PREDICATE DECLARES
        (`requires_predicate(clauses=)`), the loader's rule *a keyed row keys exactly its failable clauses* for the one kind of
        clause it cannot see. A key the predicate never answers is read by nothing (`ID-13`); a declared clause left unkeyed is
        a refusal the fold would reach `refusal_for` with and raise on. A FLAT row is unchanged."""
        if not self.has_precondition or self.requires_typed is not None:
            return True
        if self.verb not in predicates:
            return False
        if not self.refusals_by_clause:
            return True
        return self.predicate_keys() == frozenset(getattr(predicates[self.verb], "clauses", ()))

    def predicate_keys(self) -> frozenset:
        """The keys of a keyed untyped row that the fold does not own: the clauses its predicate must declare."""
        return frozenset(self.refusals_by_clause) - FOLD_CLAUSES

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

        A FLAT row answers its flat tuple for every clause. A KEYED row answers the clause's own kinds -- and a clause it does not
        key RAISES, because the loader has already required a key for every clause that can fail
        (`ELIGIBILITY_CLAUSE` if an alternative can decline, each named conjunct, `WRITE_CLAUSE` if
        the row writes, `COUNTERPARTY_CLAUSE` if it names a second party). Reaching this with an
        unkeyed clause is therefore a FOLD defect -- a new
        refusal point nobody declared -- and emitting the union instead would publish kinds for
        conjuncts that did not fail, which is `ID-9` inside the scarcity channel."""
        if not self.refusals_by_clause:
            return self.emits_on_refusal
        # B07.01: a keyed row whose precondition is unnamed (a `task` row keyed only because its `draw` clause must be,
        # whose cell's own-ledger conjunct may not be named without carrying `said`, `decision/options.py`) declares ONE
        # refusal kind, which the loader requires; the unnamed precondition's refusal is that kind, as on a flat row.
        if clause is None and len(self.emits_on_refusal) == 1:
            return self.emits_on_refusal
        if clause not in self.refusals_by_clause:
            raise InstrumentDefect(
                f"{self.verb!r} keys its refusals on {sorted(self.refusals_by_clause)} and was "
                f"refused at {clause!r}, which it does not key. The loader requires a kind for every "
                f"failable clause, so a clause arriving here unkeyed is a refusal point the fold "
                f"added without declaring it (04 §B.13 #4, F7)")
        return self.refusals_by_clause[clause]

    @property
    def party_gap_at_write(self) -> bool:
        """IS THIS ROW'S PARTY GAP REFUSED AT ITS `write` CLAUSE? True where nobody is opposite on the act's own face -- a row naming no
        `counterparty:` (a `task` row, B07.01, names none: its `draw` key, `draw_kinds`; so do `establish` and `revoke`, B21.81) -- and the row
        keys `write`: its party gap is an act that did not take, so it emits the `write` key's kinds, never the union. The ONE
        answer the loader's contested-row rule (`_load_verb_table`) and the fold (`loop/resolve.py::_refuse_party_gap`) read."""
        return not self.counterparty and WRITE_CLAUSE in self.refusals_by_clause

    @property
    def draw_kinds(self) -> tuple:
        """B07.01 (18-A item 4): the kinds a `task` row emits when its draw is lost -- its keyed `emits_on_refusal:` clause
        `draw` (`DRAW_CLAUSE`). A lost draw, not a refusal (04 §C.4: a refusal is a precondition failed), so these kinds are
        NOT in `emits_on_refusal` (the refusal union) and every reader of *is this a refusal* is unchanged; empty on every
        other row."""
        return tuple(self.refusals_by_clause.get(DRAW_CLAUSE, ()))

    def eligibility_kinds(self) -> tuple:
        return tuple(a.split(":")[0].strip() for a in self.eligibility)

    def emits_at(self, degree: str | None) -> tuple:
        """WHAT THIS ACT REPORTS, GIVEN WHAT THE SEAM RETURNED. Same polarity as `writes_at`:
        an uncontested verb ignores the degree; a contested one with no degree, or with a degree
        it does not declare, RAISES rather than reporting the wrong outcome.

        ⚠ `H-115`: THESE RAISES ARE TYPED GAPS (`season/gaps.py`), NOT `SystemExit`. `SystemExit`
        derives from `BaseException`, so `corpus_run.run_case`'s `except (S.ShapeGap, S.Unspecified,
        S.Forbidden, S.NoProducer)` clause would never catch it -- a one-case design gap would end
        the whole-corpus run. The load-time raises (missing/malformed YAML, in the loader
        functions) are correctly fatal: this file loads once, and a broken table should end the
        process. These fire per-act, mid-corpus, and belong in the taxonomy every other per-case
        refusal in the package uses."""
        if not self.emits_by_degree:
            return self.emits
        if degree is None:
            src = f"`contests: {self.contests}`" if self.contests else "a `graded_tasks` route"
            raise Unspecified(
                f"{self.verb!r} keys `emits:` by degree "
                f"({src}) "
                "and was folded with no degree, so there is no way to say WHICH outcome to report.",
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

        ⚠ `H-115`, SAME RULE AS `emits_at` ABOVE -- see that docstring."""
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
# YAML column fills (the two `*_by_degree` maps are built from `writes:`/`emits:`, and
# `refusals_by_clause` from `emits_on_refusal:`, not read), plus `domain` (read for `release`,
# invariant 6) and `source` (every row's provenance column).
_VERB_ROW_KEYS = (frozenset(f.name for f in fields(VerbRow)
                            if not f.name.endswith(("_by_degree", "_by_clause")))
                  | {"domain", "source"})

# THE TWO FAILABLE CLAUSES THE FOLD OWNS, BESIDE A ROW'S OWN NAMED CONJUNCTS --
# the keys a keyed `emits_on_refusal:` uses for them. `ELIGIBILITY_CLAUSE` is `04 §C.4`'s own
# `refusal_for(ELIGIBILITY)`: no alternative of the row admitted the actor. `WRITE_CLAUSE` is F9's:
# the precondition held and the write moved nothing (`NoOpReceipt`, `state/gate.py`) -- an effect
# that DECLINED, which is a refusal the row must name like any other. Defined here, beside the loader
# that requires them, and imported by the fold (`loop/resolve.py`) that emits them.
ELIGIBILITY_CLAUSE = "eligibility"
WRITE_CLAUSE = "write"
# THE THIRD: `ED-IN-0210` ruling 1's SECOND PARTY, ASKED ONCE, IN THE
# FOLD. A row naming a `counterparty:` operand is refused here when the act names nobody there or
# names the actor -- the `Tenure(X, X)` self-loop ruling 1 calls a fiat. `opening_set` already declines the
# same case person-side, so no computed act reaches it; this is the clause a HAND-BUILT act meets,
# and it replaces the per-effect copies (`_eff_petition`'s self-address decline) with one owner.
# Derived like the other two: a keyed row keys it iff it names a counterparty.
COUNTERPARTY_CLAUSE = "counterparty"
# B07.01 (18-A item 2, item 4): THE FOURTH KEY, AND NOT A REFUSAL -- a `form: task` row's lost draw. A row keys it iff its
# `graded_tasks` route is `form: task`; its kinds are the row's `draw_kinds`, kept out of the refusal union.
DRAW_CLAUSE = "draw"
# B09.19: THE FOUR THE FOLD OWNS. Any other key of a keyed UNTYPED row with a precondition is a clause its PREDICATE declared
# (`loop/predicates.py::requires_predicate(clauses=)`), which this loader may not import: `VerbRow.precondition_evaluable` checks
# those against the predicate table, and the loader below lets them through as keys it cannot judge.
FOLD_CLAUSES = frozenset({ELIGIBILITY_CLAUSE, WRITE_CLAUSE, COUNTERPARTY_CLAUSE, DRAW_CLAUSE})
# B07.01 (18-A item 2): THE TWO SHAPES OF A `graded_tasks` ROUTE. `inquiry` keys `emits:` by Degree and writes nothing (FI-01, as
# before); `task` carries a flat `writes:` and `emits:` and keys `emits_on_refusal:` with `DRAW_CLAUSE`. The loader branches on them.
FORM_INQUIRY = "inquiry"
FORM_TASK = "task"
ROUTE_FORMS = (FORM_INQUIRY, FORM_TASK)
# B07.01 (18-A item 1): the `Person` cells a `bookkeeping` row may not write without `brute:` (another's body or being) --
# `rosters.yaml: bookkeeping_forbidden_cells`, a closed set the refusal reads, so not spelled here (CLAUDE.md §0.05).
BOOKKEEPING_FORBIDDEN_CELLS = frozenset(roster("bookkeeping_forbidden_cells"))


def _effect_calls() -> list:
    """EVERY `Call` NODE EACH REGISTERED EFFECT REACHES, as `(verb, call)` -- the one walk over `files.effects_modules()` that
    `_derive_openers_from_effects` (which `Tenure(...)` a verb opens) and `_derive_minted_record_kinds` (which `Record` kind a verb
    mints, B21.17) both read, so the namespace and helper resolution described on the first live once. Source is read as TEXT,
    never imported (no `data` -> `loop` edge); a helper is walked as if inlined, transitively, each once."""
    calls: list = []
    # Every sibling is parsed FIRST, so a helper one file imports from another is walked in ITS OWN
    # file's namespace. `namespace[stem]` = the top-level functions of `stem` plus the ones it brings in
    # with `from .<sibling> import name` (level 1, a sibling stem), the import binding the name the
    # caller spells; `owner` maps a function node to its file's stem.
    trees = {path.stem: ast.parse(path.read_text(encoding="utf-8")) for path in files.effects_modules()}
    own = {stem: {n.name: n for n in tree.body if isinstance(n, ast.FunctionDef)}
           for stem, tree in trees.items()}
    namespace: dict = {}
    for stem, tree in trees.items():
        ns: dict = {}
        for n in tree.body:
            if isinstance(n, ast.ImportFrom) and n.level == 1 and n.module in own and n.module != stem:
                ns.update({al.asname or al.name: own[n.module][al.name]
                           for al in n.names if al.name in own[n.module]})
        ns.update(own[stem])           # a file's own definition shadows an import of the same name
        namespace[stem] = ns
    owner = {id(fn): stem for stem, fns in own.items() for fn in fns.values()}

    for stem, tree in trees.items():
        def _reached(fn) -> list:
            """`fn` and every helper it calls -- module-level in its own file, or imported from a
            sibling `effects_*.py` -- transitively, each once, each resolved in ITS OWN file's
            namespace (`namespace[owner[...]]`)."""
            out, todo, seen = [], [fn], set()
            while todo:
                f = todo.pop()
                if id(f) in seen:
                    continue
                seen.add(id(f))
                out.append(f)
                ns = namespace[owner.get(id(f), stem)]
                todo.extend(ns[c.func.id] for c in ast.walk(f)
                            if isinstance(c, ast.Call) and isinstance(c.func, ast.Name)
                            and c.func.id in ns)
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
                if isinstance(call, ast.Call):
                    calls.append((verb, call))
    return calls


def _derive_openers_from_effects() -> dict:
    """LOADER INVARIANT 6'S SECOND HALF, DERIVED RATHER THAN HAND-COPIED (`OPENERS-DERIVE`). The
    single owner of "which verb opens which kind" is the `Tenure(...)` construction itself, inside
    the function `@effect_for` registers for that verb (`CLAUDE.md` §8's every-rule-lives-once):
    every site names `kind` as a STRING LITERAL -- `Tenure(id, subject, object, kind, ...)`,
    positional, or a `kind=` keyword -- so an AST walk over the effect modules' own source (read as
    TEXT, never imported -- no `data` -> `loop` import edge) reads the fact with no second copy to
    fall behind.

    Returns EVERY tenure kind, including the ones no effect opens -- an empty list, the "declared
    means present" contract -- because a kind with a `writes: Tenure.since` cell and no opener
    (`commit`, `oblige`, `succeed`, `tie`, `knot`) is a real, disclosed hole, not an absent
    declaration. Run this function for the current set.

    ⚠ THE WALK FOLLOWS A REGISTERED EFFECT INTO THE MODULE'S OWN HELPERS. `create_record`, `issue`
    and `petition` share ONE mint, `_mint_document`, and the `hold` it opens is constructed there
    rather than in any decorated body -- so a walk confined to the decorated function would DROP
    `create_record` from `hold`'s openers, a derived fact going quietly wrong in the direction
    nobody reads. A call to a function defined at the top of the SAME FILE, or imported from a
    SIBLING `effects_*.py`, is walked as if inlined (transitively, each helper once).

    ⚠⚠ SEVERAL FILES, NOT ONE. `effects.py` is a thin aggregator -- no `@effect_for`, no
    `Tenure(...)` -- and every decorated function lives in one of its `effects_*.py` siblings
    (`files.effects_modules()`, discovered by name rather than hand-listed). Every sibling is
    parsed first and a decorated function's helpers are resolved through its OWN file's namespace:
    the top-level functions it defines plus the ones it imports from a sibling (`from .effects_x
    import name`), so a shared helper that constructs a Tenure is walked from every sibling that
    reaches it (v9 IN-13: `_relocate`, defined in `effects_migration.py`, opens `contain` for
    `march` in `effects_combat.py`). A call through anything but a bare name, or a `Tenure` whose
    `kind` is not a literal, is not read.
    """
    openers: dict = {k: set() for k in TENURE_KINDS}
    for verb, call in _effect_calls():
        if not (isinstance(call.func, ast.Name) and call.func.id == "Tenure"):
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


#: Computed ONCE: the effect modules' source does not change mid-process, and all three call sites
#: below read the same derivation (`_OFFICES_DOC`/`OFFICES_SEATS` in `rosters.py` cache theirs alike).
_OPENERS_FROM_EFFECTS = _derive_openers_from_effects()


def _record_kinds_answered(row: "VerbRow") -> Optional[frozenset]:
    """THE RECORD KINDS ONE ROW ANSWERS A HELD DOCUMENT OF (IN-09): for a row declaring
    `referent_class: Record`, the `kind` of every `existence` clause of `subject` in its typed cell
    (`comply`: `dispensation`); `None` for a row declaring any other class or none. The ONE owner:
    `_load_verb_table` refuses a `Record` row it leaves empty, and `_derive_record_referent_kinds`
    and `_derive_holding_record_kinds` union its sub-kinds (`_record_subkinds_answered`, v10 REM-2C) into
    the two sets the Record terms of
    `queries/world_q.py::questions_for` stamp by (`writs_held`; `records_held_for_holding_rows`, told
    apart by whether the row's cell asks `held_by` of `subject`)."""
    if row.referent_class != "Record":
        return None
    if row.requires_typed is None:
        return frozenset()
    req = row.requires_typed.requirement
    return frozenset(c.kind for c in (req.clauses if isinstance(req, AllOf) else (req,))
                     if isinstance(c, Existence) and c.of == "subject")


def _record_subkinds_answered(row: "VerbRow") -> frozenset:
    """THE RECORD SUB-KINDS ONE ROW ANSWERS (v10 REM-2C, B10-05, AM-A-11; M19 taken, [ASSUMPTION; medium;
    Jordan to correct]): `_record_kinds_answered` less the row's class itself, empty for a row declaring any
    other class or none. A clause asking `existence` of the COLLECTION (`research`: `kind: Record`, any
    document) names no sub-kind a standing occasion could stamp by -- every Record answers it -- so it is
    in neither derivation below; such a row forms on the question's own Records, which
    `queries/world_q.py::own_referents_of_class` stamps, and (the class being shared) on every Record the
    two standing occasions stamp.
    The ONE place that exclusion is written: both derivations read it."""
    return (_record_kinds_answered(row) or frozenset()) - {row.referent_class}


#: The authorisers of a brute verb (B05.24) and the ways a prize's module reads a person (B05.25): rosters, not lists here.
BRUTE_KINDS = roster("brute_kinds")
PERSON_INPUTS = roster("person_inputs_kinds")

#: The provider name the social roll's prize rows and inquiry routes carry (`rosters.yaml: contest_subsystems`,
#: `graded_tasks`; `seam/wrappers/sigma.py::_PROVIDER`).
SOCIAL_ROLL_PROVIDER = "social_contest"


def social_rolled(verb: str, row, prizes: dict) -> bool:
    """IS `row` ONE THE SOCIAL ROLL DEALS? Its `contests:` prize is resolved by the `social_contest` provider
    (`prizes` is `rosters.yaml: contest_subsystems.prizes`), or a `graded_tasks` route sends it there (armed or not: the row's shape does not depend on a fixture's value). THE ONE TEST: the loader's
    `difficulty:` refusal and `social_roll_verbs()` both ask it, and no verb is named."""
    if row.contests and (prizes.get(row.contests) or {}).get("provider") == SOCIAL_ROLL_PROVIDER:
        return True
    return (GRADED_TASKS.get(verb) or {}).get("provider") == SOCIAL_ROLL_PROVIDER


def _arm_default(name: str):
    """B07.01 (UNDECIDED (11) (iii)): the SHIPPED value of the `Fixtures` member a route's `armed_by:` names, or `None` where
    no such member is registered (the route check after the loop refuses it, naming the verb). Imported here, not at module
    level: `data/fixtures.py` reads `data/rosters.py` only, so this import closes no cycle."""
    from .fixtures import DEFAULT_FIXTURES
    try:
        return DEFAULT_FIXTURES.get(name)
    except Ungraded:
        return None


def _bookkeeping_cells_touched(row) -> list:
    """The cells of a `bookkeeping` row's `writes:` that move another's body, holding or stores (18-A item 1): a
    `BOOKKEEPING_FORBIDDEN_CELLS` member; a `Tenure` field where the edge is not the actor's own (`beneficiary:` other than
    `actor`) or is a seat's `hold` (an `Office` referent); `Rung.stores` (whose rung the loader cannot tell the actor
    holds). [ASSUMPTION: the two Tenure cases are read off `beneficiary:` and `referent_class: Office` -- basis: the
    loader holds no act, so whose Tenure a write touches is what the row declares of its edge.]"""
    return [w for w in row.writes
            if w in BOOKKEEPING_FORBIDDEN_CELLS or w == "Rung.stores"
            or (w.startswith("Tenure.") and (row.beneficiary != "actor" or row.referent_class == "Office"))]


def _check_resolution_classes(rows: dict) -> None:
    """B07.01 (18-A item 1; UNDECIDED (1), (10)): THREE RESOLUTION CLASSES, ONE PER WRITING ROW, DERIVED -- `contest` (the
    row has `contests:`), `task` (a `graded_tasks` route), `bookkeeping` (a `bookkeeping_verbs` member), and the fourth,
    `contest` owed to the lane named (`contest_owed`). A row that writes or emits a finding (a kind `rosters.yaml:
    inquiry_modules.findings` keys) and is in none, or any row in two, is refused naming it; so is a `contest_owed` member
    that declares `contests:` (its verb leaves the roster in that commit), a roster member that is no verb row, a
    `bookkeeping` row with no `why:`, and a `bookkeeping` row whose `writes:` touch another's body, holding or stores
    (`_bookkeeping_cells_touched`) unless it declares `brute:` (UNDECIDED (10): the loader's column for a write with no roll),
    or that emits a finding. The loader's refusal per data family (CLAUDE.md §0.05), not a tree-wide guard."""
    findings = frozenset(roster_map("inquiry_modules", "findings"))
    bad = [f"`{name}` names {v!r}, which is no verb row"
           for name, members in (("bookkeeping_verbs", BOOKKEEPING_VERBS), ("contest_owed", CONTEST_OWED))
           for v in members if v not in rows]
    bad += [f"`bookkeeping_verbs` {v!r} has no `why:` line" for v, r in BOOKKEEPING_VERBS.items()
            if not (isinstance(r, dict) and str(r.get("why") or "").strip())]
    bad += [f"`contest_owed` {v!r} names no carrying proposal" for v, p in CONTEST_OWED.items() if not str(p or "").strip()]
    for verb, row in rows.items():
        classes = [c for c, held in (("contest", bool(row.contests)), ("task", verb in GRADED_TASKS),
                                     ("bookkeeping", verb in BOOKKEEPING_VERBS), ("contest owed", verb in CONTEST_OWED)) if held]
        finds = sorted(findings & set(row.emits))
        if verb in CONTEST_OWED and row.contests:
            bad.append(f"{verb!r} is in `contest_owed` and declares `contests: {row.contests}`: delete it from the roster")
        elif len(classes) > 1:
            bad.append(f"{verb!r} is in {len(classes)} classes {classes}; a row is in exactly one")
        elif not classes and (row.writes or finds):
            bad.append(f"{verb!r} writes or emits a finding and is in no class (`contests:`, a `graded_tasks` route, "
                       "`bookkeeping_verbs`, `contest_owed`)")
        if verb in BOOKKEEPING_VERBS:
            touched = [] if row.brute else _bookkeeping_cells_touched(row)
            if touched or finds:
                bad.append(f"{verb!r} is `bookkeeping` and {'writes ' + str(touched) if touched else 'emits ' + str(finds)}"
                           f"{' with no `brute:`' if touched else ''}: bookkeeping moves no one else's body, holding or stores")
    if bad:
        raise SystemExit(
            "verb_table.yaml / rosters.yaml: " + "; ".join(bad) + ". 18-A item 1 (B07.01) -- every writing row is "
            "`contest`, `task` or `bookkeeping` (or owed a contest by its lane), derived from its row and the rosters.")


def _check_governing_attributes(rows: dict, prizes: dict) -> None:
    """B05.25: EVERY ROW IS ONE OF FOUR KINDS, OR THE LOAD REFUSES, NAMING EACH ROW THAT IS NOT (B24p.16 added (d), `proceeds`: a verb that opens a
    proceeding, whose dice are the proceeding's own). `rows` is `{verb: VerbRow}`,
    `prizes` is `rosters.yaml: contest_subsystems.prizes`. (a) `brute` (a member of `BRUTE_KINDS`, with a `brute_note`; `seat` only where the eligibility carries `remit:`
    or the referent class is `Office`); (b) `governing` (one to three distinct `descriptors.ATTRIBUTES` keys); (c) the exemption:
    the row's prize reads `person_inputs: own`. A brute row never rolls, so it also carries no `opposed_attribute`, no `contests:`
    prize, no `graded_tasks` route and no `difficulty:` cell; a row contested on a `pool` prize takes
    (b) and names the `opposed_attribute` of the person opposite; a prize row names its `person_inputs`. A row of kind (b) that
    nothing yet rolls (no prize, no route) is inert and is not refused: its draw is B07's."""
    bad = []
    for name, prize in prizes.items():
        if (prize or {}).get("person_inputs") not in PERSON_INPUTS:
            bad.append(f"prize {name!r}: `person_inputs` is {(prize or {}).get('person_inputs')!r}, not one of {sorted(PERSON_INPUTS)}")
    for verb, row in rows.items():
        inputs = (prizes.get(row.contests) or {}).get("person_inputs") if row.contests else None
        exempt = inputs == "own"
        taken = [k for k, held in (("brute", row.brute), ("governing", row.governing), ("exempt prize", exempt), ("proceeds", row.proceeds)) if held]
        if len(taken) != 1:
            bad.append(f"{verb!r} takes {taken or 'none'} of `brute`, `governing`, an exempt prize and `proceeds`; it takes exactly one")
        if row.brute:
            if row.brute not in BRUTE_KINDS:
                bad.append(f"{verb!r}: `brute: {row.brute}` is none of {sorted(BRUTE_KINDS)}")
            if not row.brute_note:
                bad.append(f"{verb!r}: `brute: {row.brute}` with no `brute_note:` saying what authorises it")
            if row.brute == "seat" and not (any(e.startswith("remit:") for e in row.eligibility) or row.referent_class == "Office"):
                bad.append(f"{verb!r}: `brute: seat` with no `remit:` eligibility and no Office referent")
            for what, present in (("governing", row.governing), ("opposed_attribute", row.opposed_attribute),
                                  ("a `contests:` prize", row.contests), ("a `graded_tasks` route", verb in GRADED_TASKS),
                                  ("a `difficulty:` cell", getattr(row, "difficulty", None) is not None)):
                if present:
                    bad.append(f"{verb!r} is brute and carries {what}: a brute verb never rolls")
        if len(row.governing) > 3 or len(set(row.governing)) != len(row.governing) or not set(row.governing) <= set(ATTRIBUTES):
            bad.append(f"{verb!r}: `governing: {list(row.governing)}` is not one to three distinct keys of the ten attributes")
        if row.opposed_attribute is not None and row.opposed_attribute not in ATTRIBUTES:
            bad.append(f"{verb!r}: `opposed_attribute: {row.opposed_attribute}` is no attribute key")
        if inputs == "pool" and not row.proceeds:        # a row that proceeds (B24p.19) pools nothing: the proceeding's own dice are the six attributes of the room
            if not row.governing:
                bad.append(f"{verb!r} is contested on a `pool` prize ({row.contests!r}) and names no `governing:`")
            if row.opposed_attribute is None:
                bad.append(f"{verb!r} is contested against a person on a `pool` prize ({row.contests!r}) and names no `opposed_attribute:`")
    if bad:
        raise Unspecified(
            "verb_table.yaml: " + "; ".join(bad), "verb_table.yaml: governing / brute / opposed_attribute",
            needs="each row exactly one of `brute:` (seat, own, counterparty, with a note), `governing:` (one to three of the ten "
                  "attributes; `opposed_attribute:` on a row contested on a `pool` prize) or an exempt prize (`person_inputs: own`)",
            law="B05.24 (ED-IN-0379), Jordan 2026-11-13 -- every verb's dice amount is set by the character's attributes, or it never rolls, or it "
                "is the subsystem's")


def _build_looks(verb: str, raw, row: "VerbRow") -> tuple:
    """B11.71: A ROW'S `observes:` COLUMN INTO `Look`s, or the load refuses naming the row. The column is a FLAT LIST of `{of: <operand>, read: <read>}`
    -- a mapping (a band-keyed one) or an entry that names a band is refused, since which reads a band deposits is `finding_terms`'s and a second
    band-keyed table beside it is the defect FRES §8 names. Each `of` is a `requires_operands` member the row's own cell BINDS (an operand the act
    never carries looks at nothing), each `read` a `look_reads` member, and no `read` is a stem the row's own cell asks: WITNESS tells a look from a
    gating read by the stem, so a stem on both sides would let a failed look pass for a gating read. A row that keys no `emits:` by degree has no band,
    and WITNESS deposits none of its looks (no `finding_terms` row for `None`). A function so a test can plant each refusal."""
    if raw is None:
        return ()
    if not isinstance(raw, list):
        raise SystemExit(f"verb_table.yaml: {verb!r} `observes:` is {type(raw).__name__}, not a flat list of `{{of, read}}` entries -- it names what is "
                         "looked at and never a band (`rosters.yaml: finding_terms` is the one band-keyed table)")
    cell = row.requires_typed
    out = []
    for entry in raw:
        if not isinstance(entry, dict) or set(entry) != {"of", "read"}:
            raise SystemExit(f"verb_table.yaml: {verb!r} `observes:` entry {entry!r} is not `{{of: <operand>, read: <read>}}`")
        of, read = entry["of"], entry["read"]
        if of in DEGREE_BANDS or read in DEGREE_BANDS:
            raise SystemExit(f"verb_table.yaml: {verb!r} `observes:` entry {entry!r} names a band; it names what is looked at, and "
                             "`rosters.yaml: finding_terms` says which reads a band deposits")
        if of not in REQUIRES_OPERANDS or cell is None or of not in cell.operands():
            raise SystemExit(f"verb_table.yaml: {verb!r} `observes:` looks at {of!r}, which its `requires_typed` cell does not bind "
                             f"(binds {sorted(cell.operands()) if cell is not None else 'nothing -- the row is untyped'}); the act would not carry it")
        if read not in LOOK_READS:
            raise SystemExit(f"verb_table.yaml: {verb!r} `observes:` reads {read!r}, which is not a `rosters.yaml: look_reads` member ({sorted(LOOK_READS)})")
        if read in cell.stems():
            raise SystemExit(f"verb_table.yaml: {verb!r} `observes:` reads {read!r}, a stem its own cell asks: a look is a NON-GATING read, and WITNESS "
                             "tells it from a gating one by the stem")
        out.append(Look(of, read))
    if len(set(out)) != len(out):
        raise SystemExit(f"verb_table.yaml: {verb!r} `observes:` lists a look twice")
    return tuple(out)


# B24p.16: THE KEYS OF ONE `proceeds:` ENTRY, AND THE SET EACH CELL IS A MEMBER OF. Read by `_proceeds_entries` (the normaliser) and `_check_proceeds`.
_PROCEEDS_KEYS = ("when", "row", "form", "move", "item")
_PROCEEDS_FORMS = ("full", "abridged", "auto")
_PROCEEDS_ITEMS = ("any", "false")
_PROCEEDS_WHEN = {"hearer": ("cohort",), "docketed": (True,)}      # a `when` key and the one value it may take
PROCEEDS_DOCKET = "docket"                                         # a `row` that is no arrangement id: the row the docket hears the matter under


def _proceeds_entries(verb: str, raw) -> tuple:
    """A ROW'S `proceeds:` CELL AS ITS ENTRIES (B24p.16): absent is `()`, a single mapping is ONE entry with an empty `when`, a list is its entries in order.
    Each is `(when, row, form, move, item)` -- `when` a tuple of `(key, value)` pairs, `move` defaulting to `argue`, `item` to `any` (YAML's `false` reads
    as the cell `false`); `row` and `form` stay `None` where the file names none, for `_check_proceeds` to refuse with the rest. A cell that is no mapping
    or list of mappings, or an entry key outside `_PROCEEDS_KEYS`, is refused here (invariant 10's rule for a column: a key read by nothing is a typo)."""
    if raw is None:
        return ()
    entries = [raw] if isinstance(raw, dict) else list(raw) if isinstance(raw, (list, tuple)) else None
    if entries is None or not all(isinstance(e, dict) for e in entries):
        raise Unspecified(f"verb_table.yaml: {verb!r} `proceeds:` is {raw!r}", "verb_table.yaml: proceeds",
                          needs="a mapping, or a list of mappings, each `{when?, row, form, move?, item?}`", law="B24p.16, RD §D.1")
    out = []
    for e in entries:
        stray = sorted(set(e) - set(_PROCEEDS_KEYS))
        if stray:
            raise Unspecified(f"verb_table.yaml: {verb!r} `proceeds:` names {stray}", "verb_table.yaml: proceeds",
                              needs=f"only {list(_PROCEEDS_KEYS)} in an entry", law="B24p.16, RD §D.1")
        when = e.get("when") or {}
        out.append((tuple(sorted(when.items())) if isinstance(when, dict) else when, e.get("row"), e.get("form"),
                    e.get("move", "argue"), "false" if e.get("item") is False else e.get("item", "any")))
    return tuple(out)


def _check_proceeds(rows: dict) -> None:
    """B24p.16: A `proceeds:` CELL IS ROUTING THE LOAD CAN CHECK, OR THE LOAD REFUSES, NAMING EACH ROW THAT IS NOT. `rows` is `{verb: VerbRow}`. A row refused:
    one that carries `proceeds` with `brute` (R7: a brute function opens nothing); an entry whose `row` is neither an arrangement id (`ARRANGEMENTS`) nor
    `docket`; whose `form` is outside `full`, `abridged`, `auto`; whose `move` is not a `PROCEEDING_MOVES` member that draws; whose `item` is outside `any`,
    `false`; whose `when` names a key outside `hearer` (value `cohort`) and `docketed` (value `True`); and a cell whose last entry's `when` is not empty
    (nothing then answers an act no `when` holds for); and one that carries `governing` or `opposed_attribute` beside it (B24p.19 deleted the five rows')."""
    bad = []
    for verb, row in rows.items():
        if not row.proceeds:
            continue
        if row.brute:
            bad.append(f"{verb!r} is brute and carries `proceeds:`: a brute verb opens no proceeding")
        for what, present in (("governing", row.governing), ("opposed_attribute", row.opposed_attribute)):
            if present:
                bad.append(f"{verb!r} carries `proceeds:` and `{what}:`: a verb that proceeds pools nothing, its dice are the proceeding's own (B24p.19)")
        for when, rid, form, move, item in row.proceeds:
            if rid != PROCEEDS_DOCKET and rid not in ARRANGEMENTS:
                bad.append(f"{verb!r}: `proceeds` row {rid!r} is no arrangement id and not `{PROCEEDS_DOCKET}`")
            if form not in _PROCEEDS_FORMS:
                bad.append(f"{verb!r}: `proceeds` form {form!r} is none of {list(_PROCEEDS_FORMS)}")
            if not (PROCEEDING_MOVES.get(move) or {}).get("draw"):
                bad.append(f"{verb!r}: `proceeds` move {move!r} is no `proceeding_moves` member that draws")
            if item not in _PROCEEDS_ITEMS:
                bad.append(f"{verb!r}: `proceeds` item {item!r} is none of {list(_PROCEEDS_ITEMS)}")
            for key, value in (when if isinstance(when, tuple) else ()):
                if key not in _PROCEEDS_WHEN or value not in _PROCEEDS_WHEN[key]:
                    bad.append(f"{verb!r}: `proceeds` when {key!r}: {value!r} is outside {_PROCEEDS_WHEN}")
        if row.proceeds[-1][0] != ():
            bad.append(f"{verb!r}: the last `proceeds` entry has a `when`; the list ends in an entry that holds for any act")
    if bad:
        raise Unspecified(
            "verb_table.yaml: " + "; ".join(bad), "verb_table.yaml: proceeds",
            needs="`proceeds:` on a non-brute row only: each entry an arrangement id (or `docket`), a form of full | abridged | auto, a drawing move, an item of "
                  "any | false, a `when` of hearer: cohort | docketed: true, the last entry with no `when`",
            law="B24p.16, RD §D.1 to §D.4 (R3, R6, R7): a verb that influences a person by words names the proceeding it opens, and whether in full or abridged")


def _load_verb_table() -> dict:
    if not VERB_TABLE_YAML.exists():
        raise SystemExit(f"verb_table.yaml not found at {VERB_TABLE_YAML}")
    doc = load_yaml(VERB_TABLE_YAML.read_text())
    out = {}
    _release_domain: frozenset = frozenset()
    _closer_domains: dict = {}             # v9 IN-12 step 5: every OTHER row's declared `domain:`
    for r in doc["verbs"]:
        name = r["verb"]
        if name in out:
            raise SystemExit(f"verb_table.yaml: {name!r} appears more than once")
        # LOADER INVARIANT 10, VERB HALF (`04 §B.13 #10`, `04:470`): UNKNOWN KEYS ARE REJECTED.
        # A column is either one this loader reads or an annotation spelled `*_note`; anything else
        # is a column that silently does nothing.
        # #10's OTHER CLAUSE -- *"a `scale:` key fails the load"* -- IS ENFORCED BY THIS SAME RULE: `scale` is
        # no `VerbRow` field (B21.84 cut the stored column; a scale is the scope of the seat exercised,
        # `Act.via`'s seat), so a `scale:` key is an unknown key and refuses the load naming the row.
        unknown = sorted(k for k in r if k not in _VERB_ROW_KEYS and not str(k).endswith("_note"))
        if unknown:
            raise SystemExit(
                f"verb_table.yaml: {name!r} carries unknown key(s) {unknown}. 04 §B.13 #10 -- a "
                f"row's keys are the ones this loader reads ({sorted(_VERB_ROW_KEYS)}) or an "
                "annotation spelled `*_note`; any other column is read by nothing.")
        # B11.65: THE `public:` COLUMN, REQUIRED ON EVERY ROW AND A BOOLEAN (`18_DETERMINISM_notice_is_a_draw` edit 1; as `capability:` below, no
        # default by omission). `isinstance(..., bool)` and nothing looser: `1`, `"yes"` and a null are not booleans.
        if "public" not in r:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares no `public:`. Every row says whether its deed is done to be seen "
                "(`public: true` or `public: false`); a row that omits it would leave the notice draw to guess from the verb's name.")
        if not isinstance(r["public"], bool):
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `public: {r['public']!r}`, which is not a boolean. Write `true` or `false`.")
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
        # ⚠ `emits_on_refusal:` TAKES TWO SHAPES TOO (invariant 4's per-conjunct half). A mapping is keyed by FAILABLE CLAUSE; a sequence is the flat form. The union is the
        # flat column either way, so every reader of *is this a refusal* sees the same kinds.
        raw_refusals = r["emits_on_refusal"]
        by_clause: dict = {}
        if isinstance(raw_refusals, dict):
            by_clause = {str(k): tuple(v or ()) for k, v in raw_refusals.items()}
            # B07.01: the `draw` clause's kinds are a lost draw, not a refusal (`VerbRow.draw_kinds`), so not in the union.
            flat_refusals = tuple(dict.fromkeys(k for c, v in by_clause.items() if c != DRAW_CLAUSE for k in v))
        else:
            flat_refusals = tuple(raw_refusals)
        row = VerbRow(name, r["stratum"], tuple(r["eligibility"]), r["requires"],
                      flat, flat_emits,
                      flat_refusals, r["grade"],
                      str(r.get("contests") or "").strip(),
                      by_degree, emits_by_degree,
                      build_typed_requires(name, r.get("requires_typed")),
                      str(r.get("requires_typed_note") or "").strip(),
                      str(r.get("beneficiary") or "").strip(),
                      str(r.get("counterparty") or "").strip(),
                      refusals_by_clause=by_clause,
                      effect_decline_note=str(r.get("effect_decline_note") or "").strip(),
                      requires_decline_note=str(r.get("requires_decline_note") or "").strip(),
                      referent_class=str(r.get("referent_class") or "").strip(),
                      counterparty_may_be_self=r.get("counterparty_may_be_self", False),
                      referent_named=r.get("referent_named", False),
                      subject_may_be_self=r.get("subject_may_be_self", False),
                      operation=str(r.get("operation") or "").strip(),
                      capability=str(r.get("capability") or "").strip(),
                      governing=tuple(r.get("governing") or ()),
                      opposed_attribute=str(r["opposed_attribute"]).strip() if r.get("opposed_attribute") else None,
                      brute=str(r["brute"]).strip() if r.get("brute") else None,
                      brute_note=str(r.get("brute_note") or "").strip(),
                      difficulty=str(r["difficulty"]).strip() if r.get("difficulty") else None,
                      regard_sign=r.get("regard_sign"),
                      public=r["public"],
                      proceeds=_proceeds_entries(name, r.get("proceeds")),
                      domain=tuple(r.get("domain") or ()))
        row = replace(row, observes=_build_looks(name, r.get("observes"), row))
        # B10.11: THE `regard_sign:` COLUMN, A `regard_signs` MEMBER OR THE LOAD REFUSES (a `True` is no sign: it equals 1 in a set). An absent
        # cell is the declared default -- `-1` on a row done against its subject (`opposed_to_subject`), else `+1` -- the sign `_stance_arm` read before the column.
        if row.regard_sign is None:
            row = replace(row, regard_sign=-1 if row.opposed_to_subject(roster("opposed_without_prize")) else 1)
        elif isinstance(row.regard_sign, bool) or row.regard_sign not in REGARD_SIGNS:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `regard_sign: {row.regard_sign!r}`, which is not a member of "
                f"`rosters.yaml: regard_signs` ({sorted(REGARD_SIGNS)}).")
        # THE COUNTERPARTY IS AN OPERAND THE ACT CARRIES, OR IT IS NOTHING. `opening_set` compares
        # it with the person; a name the typed cell does not BIND is absent from every Candidate,
        # so the comparison would pass silently and the rule would be a column nothing enforced.
        # ⚠ AN UNTYPED ROW MAY NAME ONE (`oblige`), AND IT MEANS SOMETHING ELSE
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
        # IN-53: A REFERENT CLASS IS A DECLARED ONE, OR THE LOAD REFUSES. A class the roster does not
        # name (a typo) would make the verb unformable from every question, silently -- the
        # always-false membership test `rosters.yaml`'s header refuses.
        if row.referent_class and row.referent_class not in REFERENT_CLASSES:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares referent_class {row.referent_class!r}, which "
                f"is not a declared class (the classes are {sorted(REFERENT_CLASSES)}, from "
                "`rosters.yaml: referent_classes`). `opening_set` forms the verb only on a "
                "referent carried as that class, so an undeclared one never forms.")
        # IN-09: A `Record` ROW NAMES THE RECORD KINDS IT
        # ANSWERS, OR THE LOAD REFUSES. `writs_held` stamps a held Record only if its kind is one a
        # `Record` row's typed cell asks `existence` of on `subject` (`RECORD_REFERENT_KINDS`, read
        # off `_record_kinds_answered`; v10 REM-25: a row whose cell also asks `held_by` is stamped by
        # `records_held_for_holding_rows` off `HOLDING_RECORD_KINDS` instead); a row naming none, or
        # naming a kind `rosters.yaml: record_kinds` does not hold, would be stamped nothing and never
        # form -- a declared row read by nothing, which `04` §A.1's ID-13 row binds `data/` to raise on.
        # v10 REM-2C (AM-A-11): THE CLASS ITSELF IS THE ONE OTHER KIND A CLAUSE MAY NAME (`research`:
        # any Record), which no sub-kind stamp answers and the own-referent term does
        # (`_record_subkinds_answered`); a typo, or another collection, is still refused.
        _kinds = _record_kinds_answered(row)
        if _kinds is not None and (not _kinds or not _kinds <= RECORD_KINDS | {row.referent_class}):
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares referent_class 'Record' and its "
                f"`requires_typed:` cell names {sorted(_kinds) or 'no'} `existence` kind(s) of "
                f"`subject` (the record kinds are {sorted(RECORD_KINDS)}, or the class itself). "
                "`writs_held` and `records_held_for_holding_rows` stamp a held Record only of a kind "
                "such a clause names, and the own-referent term a Record of any kind only for a clause "
                "naming the class, so this row would never form.")
        # IN-10 (a) / IN-53 D2 / CP-T05-02 (iii): `referent_named`, `counterparty_may_be_self` and
        # `subject_may_be_self` ARE BOOLEANS -- a string `"false"` would read truthy.
        for col in (f.name for f in fields(VerbRow) if f.type == "bool"):
            if not isinstance(getattr(row, col), bool):
                raise SystemExit(
                    f"verb_table.yaml: {name!r} declares {col} {getattr(row, col)!r}; it is "
                    "`true` or `false`")
        # AN `operation:` IS A `thread_operations` MEMBER, OR THE LOAD REFUSES -- `SystemExit`, the load-time
        # kind (`H-115`'s split, as `beneficiary:` above). The roster is `rosters.yaml`'s and is read through
        # `THREAD_OPERATIONS`; a name the threadwork module has no working for would be a verb nothing performs.
        if row.operation and row.operation not in THREAD_OPERATIONS:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `operation: {row.operation!r}`, which is not in "
                f"`thread_operations` ({sorted(THREAD_OPERATIONS)}). A thread operation is one named working a "
                "practitioner attempts on the thread; add a new one to rosters.yaml and argue for it there, "
                "never here.")
        # IN-10 (a): `referent_named` ONLY BESIDE A `referent_class:` -- on a row forming on plain
        # referents it would decline nothing the class partition offered, a column read by nothing.
        if row.referent_named and not row.referent_class:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares referent_named without a referent_class; the "
                "column narrows a CLASSED referent to one the person's own ledger names "
                "(`decision/options.py::opening_set`), and this row forms on plain referents.")
        # IN-53 D2: `counterparty_may_be_self` ONLY ON A ROW THE FAN REACHES. On a row whose
        # counterparty no known person fills (`oblige`'s `subject`, `petition`'s bound `to`) the
        # person is never added to any bag, so the column would waive the fold's self-exclusion for
        # hand-built acts alone -- a fiat admitted through the back door, which ED-IN-0210 ruling 1
        # refuses. (An empty counterparty is no operand a known person fills.)
        if row.counterparty_may_be_self and (
                row.counterparty not in row.known_person_operands()):
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares counterparty_may_be_self, but its counterparty "
                f"{row.counterparty!r} is not an operand a known person fills "
                f"({list(row.known_person_operands())}). The column adds the person to that fan "
                "(`decision/options.py::operand_bags`); on any other row it would only waive the "
                "fold's self-exclusion.")
        # CP-T05-02 (iii): `subject_may_be_self` ONLY ON A ROW CONTESTED AGAINST ITS SUBJECT. On any other
        # row `opening_set` makes no self-subject decline (`decision/options.py::subject_is_opponent`:
        # `tell`'s subject is a topic), so the column would waive nothing -- a column read by nothing.
        if row.subject_may_be_self and not row.contested_against_subject():
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares subject_may_be_self, but its act is not contested "
                f"against its subject (contests {row.contests!r}, opponent operand "
                f"{row.opponent_operand()!r}). The column waives `opening_set`'s decline of a person as "
                "his own adversary, which only such a row makes.")
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
        #     Candidate holds; a BLANK would say the same thing to `beneficiary_of` and nothing at
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
        #     ⚠⚠ IT RAISES `SystemExit`, NOT `Unspecified` (`require_member` raises
        #     `Unspecified`): load-time refusals are fatal `SystemExit`, while `Unspecified`/
        #     `ShapeGap`/`Forbidden`/`NoProducer` are the PER-ACT gap taxonomy
        #     `corpus_run.run_case` catches, so a broken TABLE would be reported as ONE CASE's
        #     `status="DESIGN-GAP"` (`H-115`). `test_h115_...` counts `raise SystemExit` only.
        if row.beneficiary not in BENEFICIARY_KINDS:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `beneficiary: {row.beneficiary!r}`, which is "
                f"not in `beneficiary_kinds` ({sorted(BENEFICIARY_KINDS)}). CAT-2 -- the "
                "beneficiary resolves to a carrier a Candidate ALREADY holds (the actor, "
                "`subject`, or a named operand); a name outside the roster is a carrier nothing "
                "can resolve. Add it to rosters.yaml and argue for it there, never here.")
        # (3) AN OPERAND BENEFICIARY MUST BE CARRIABLE BY THIS ROW'S OWN CELL, AND THIS IS THE
        #     CHECK THAT KEEPS THE COLUMN HONEST. A static column escapes the dead reference only
        #     while it declares carriers the row can actually hold: `beneficiary: to` on a verb
        #     whose cell never binds `to` would resolve to `None` forever in silence.
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
        elif "domain" in r:
            _closer_domains[name] = frozenset(r.get("domain") or ())
        # The two keyed columns must agree on their band set, or a band writes with nothing to
        # report or reports with nothing written.
        if by_degree and emits_by_degree and set(by_degree) != set(emits_by_degree):
            raise SystemExit(
                f"verb_table.yaml: {name!r} keys `writes` on {sorted(by_degree)} and `emits` on "
                f"{sorted(emits_by_degree)}. A band in one and not the other is an outcome that "
                "either changes the world silently or reports a change it did not make.")
        # v9 FI-01: a `graded_tasks` route beside a `contests:` is refused FIRST, before the
        # shape checks below would refuse it for a reason that is not the defect (see the emits arm).
        _graded = name in GRADED_TASKS
        # B07.01 (18-A item 2): the route's `form:` (validated after the loop, with the route's other fields).
        _form = (GRADED_TASKS.get(name) or {}).get("form") if _graded else None
        if _graded and row.contests:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `contests: {row.contests}` and has a "
                "`graded_tasks` route. The route is NOT a prize (`rosters.yaml`: giving an "
                "inquiry or a task a prize is scripting drift); one degree has one source.")
        # B04.03 (U1-A step 2): THE `capability:` COLUMN, REQUIRED ON A ROW THAT CONTESTS OR IS GRADED AND ON NO OTHER --
        # as `beneficiary:` is required below. "No default by omission; `none` is spelled": a missing key, a value that
        # is neither a `CAPABILITIES` id nor `none`, `none` with no `capability_note:`, and a column on a row nothing
        # rolls for (a column nothing reads) are each refused here, naming the row.
        if row.contests or _graded:
            if "capability" not in r:
                raise SystemExit(
                    f"verb_table.yaml: {name!r} {'contests' if row.contests else 'is graded'} and declares no "
                    f"`capability:`. Name the skill it tests ({sorted(CAPABILITIES)}) or spell `none` with a "
                    "`capability_note:`; a contested row that omits it would roll every person at the untrained "
                    "default without saying so.")
            if row.capability != "none" and row.capability not in CAPABILITIES:
                raise SystemExit(
                    f"verb_table.yaml: {name!r} declares `capability: {row.capability!r}`, which is neither a "
                    f"skill defined in `descriptor_registry.yaml: capabilities` ({sorted(CAPABILITIES)}) nor `none`.")
            if row.capability == "none" and not str(r.get("capability_note") or "").strip():
                raise SystemExit(
                    f"verb_table.yaml: {name!r} declares `capability: none` and no `capability_note:`. `none` is a "
                    "declaration, and a declaration with no reason is indistinguishable from a skill nobody named.")
        elif "capability" in r:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `capability: {row.capability!r}` and neither contests nor is "
                "graded. Nothing rolls dice from a skill for it, so the column would be read by nothing.")
        # B05.14 (SC-B Edit A; D-U1-04): THE `difficulty:` COLUMN, REQUIRED ON A ROW THE SOCIAL ROLL DEALS AND ON NO OTHER -- the shape of
        # `capability:` above. A rolled row with no level (the roll would have no difficulty to compose), a level outside
        # `rosters.yaml: difficulty_levels`, and a level on a row nothing rolls (a column nothing reads) are each refused, naming the row.
        if social_rolled(name, row, _PRIZES):
            if row.difficulty is None:
                raise SystemExit(
                    f"verb_table.yaml: {name!r} is dealt by the social roll and declares no `difficulty:`. Name the level of the act "
                    f"itself ({list(DIFFICULTY_LEVELS)}); a rolled row with none would have no difficulty to compose.")
            if row.difficulty not in DIFFICULTY_LEVELS:
                raise SystemExit(
                    f"verb_table.yaml: {name!r} declares `difficulty: {row.difficulty!r}`, which is not a member of "
                    f"`rosters.yaml: difficulty_levels` ({list(DIFFICULTY_LEVELS)}).")
        elif "difficulty" in r:
            raise SystemExit(
                f"verb_table.yaml: {name!r} declares `difficulty: {r['difficulty']!r}` and the social roll does not deal it. "
                "Nothing composes an obstacle for it, so the column would be read by nothing.")
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
        # ⚠ **INVARIANT 12 HAS A SECOND SIDE.** A row with a FLAT `writes:` (`[]` included), a
        # DEGREE-KEYED `emits:` and no `contests:` would load clean and then raise `Unspecified` at
        # the first act that folded it -- `emits_at(None)` has nowhere to look. The investigation
        # acts (ED-FI-0009) have `writes: []` by design -- a finding is a Claim minted at WITNESS,
        # not a typed write -- and ship with a FLAT `emits:` because nothing grades them yet; this
        # check is what makes that a decision rather than a habit.
        # ⚠ v9 FI-01 (J-22 option (A)): THE ARM ACCEPTS A SECOND SOURCE OF A DEGREE, a `graded_tasks`
        # ROUTE (`rosters.yaml`; `loop/resolve.py::_grade` rolls it). A routed row keys `emits:` by degree
        # and writes nothing (both refused below), so its roll has no band-blind write to apply.
        if emits_by_degree and not (row.contests or _graded):
            raise SystemExit(
                f"verb_table.yaml: {name!r} has a degree-keyed `emits:` and no `contests:` or "
                "`graded_tasks` route. Nothing resolves a degree for it, so no branch could "
                "ever be reported -- and unlike the `writes:` case this used to load clean and "
                "raise at the first fold.")
        # B07.01 (18-A item 2): THE ROUTE REFUSAL, BY `form:`. An `inquiry` keys `emits:` by Degree and writes nothing, as
        # before. B07.05: an ARMED inquiry (`reconstruct`) too, whatever its arm's value -- with the arm `off` the fold reads its
        # keyed `emits:` at `UNROUTED_BAND` (`loop/resolve.py::_fold`), so the load no longer reads a fixture's shipped value.
        if _form == FORM_INQUIRY and (row.writes or not emits_by_degree):
            raise SystemExit(
                f"verb_table.yaml: {name!r} has a `graded_tasks` route of `form: inquiry` and "
                f"{'a non-empty `writes:`' if row.writes else 'a FLAT `emits:`'}. "
                "A graded inquiry keys its emissions by Degree and writes nothing (a flat write applies on every band), "
                "or the roll decides nothing it reports.")
        # A `task` carries a FLAT `writes:` and `emits:` (04 §B.13 invariant 12: a degree-keyed column belongs to a
        # `contests:` row) and keys `emits_on_refusal:` with the clause `draw`, its lost draw (the keyed half below checks it).
        if _form == FORM_TASK and (by_degree or emits_by_degree or DRAW_CLAUSE not in by_clause):
            raise SystemExit(
                f"verb_table.yaml: {name!r} has a `graded_tasks` route of `form: task` and "
                f"{'a degree-keyed `writes:` or `emits:`' if by_degree or emits_by_degree else 'no `emits_on_refusal:` clause `draw`'}. "
                "A task row keeps its flat `writes:` and `emits:` and reports a lost draw under `emits_on_refusal:` clause "
                "`draw` (18-A item 4); a verb whose bands write different cells declares `contests:` (shape (b)).")

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
        # The stratum must be one of the five, and the roster owns which five.
        if row.stratum not in STRATA:
            raise SystemExit(f"verb_table.yaml: {name!r} has stratum {row.stratum!r}, which is "
                             f"not one of rosters.yaml's {list(STRATA)}")
        # LOADER INVARIANT 9 (`04 §B.13 #9`, `04:469`): CONTEST PRIZES ⊆ THE SUBSYSTEM ROSTER. A
        # misspelled prize would otherwise reach the seam's generic refusal at first call naming no
        # row (`manifest.registry.unclaimed_contest_prizes`'s docstring). The roster,
        # `contest_subsystems.prizes`, owns which prizes exist.
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
        # ⚠ THE PER-CONJUNCT HALF OF F7 IS ENFORCED BELOW, FOR A KEYED ROW. A FLAT row is checked at
        # row grain only (the block directly below): `restore`, `examine` and `surveil` carry an
        # `AllOf` of two and one flat kind, which is lawful -- a flat row DECLARES that all its
        # conjuncts refuse alike.
        _failable = (row.has_precondition
                     or any(k != "own" for k in row.eligibility_kinds()))
        if _failable and not row.emits_on_refusal:
            raise SystemExit(
                f"verb_table.yaml: {name!r} has a failable clause (a `requires` cell, or an "
                f"eligibility other than `own`: {list(row.eligibility)}) and an empty "
                "`emits_on_refusal:`. 04 §B.13 #4 (F7) -- every failable clause has a refusal "
                "kind; a refusal with no declared kind is a fabricated emission.")
        # LOADER INVARIANT 4, PER-CONJUNCT HALF (`04:465-468`, F7): A KEYED ROW
        # KEYS EXACTLY ITS FAILABLE CLAUSES. The clause set is DERIVED from the row, never listed:
        #   * `ELIGIBILITY_CLAUSE`  iff an eligibility alternative can decline (anything but `own`);
        #   * every NAMED top-level conjunct of its typed cell (`conjunct:`, `data/requires.py`) --
        #     and a keyed row with a precondition must be TYPED and name EVERY conjunct, OR be an untyped PREDICATE row
        #     (B09.19): a predicate's clauses (`REQUIRES_PREDICATES`) live in `loop/`, which this loader may not
        #     import, so it lets the keys beyond the fold's own four through and requires at least one; that they are
        #     exactly the predicate's declared clauses is `VerbRow.precondition_evaluable`'s, asked of the predicate table;
        #   * `WRITE_CLAUSE`         iff the row writes (an effect can decline, F9's `NoOpReceipt`);
        #   * `COUNTERPARTY_CLAUSE`  iff the row names a `counterparty:`.
        # MISSING is a failable clause with no kind -- the fold would reach `refusal_for` and raise;
        # EXTRA is a kind for a clause that cannot fail, read by nothing (`ID-13`). A name on a FLAT
        # row is refused for the same reason: nothing keys it. A CONTESTED row may key its refusals
        # only to ONE kind, unless it keys `COUNTERPARTY_CLAUSE` (below): the seam's party gap
        # (`loop/resolve.py::_refuse_party_gap`) is a refusal point this schema has no clause for
        # and emits the union, except where the row keys the counterparty clause, whose kinds it emits. ONE refusal names every
        # defect found, so a table edit that breaks three things is told all three.
        _names = row.requires_typed.conjuncts() if row.requires_typed is not None else ()
        _predicate_keys = (row.predicate_keys() if row.requires_typed is None and row.has_precondition
                           else frozenset())
        if by_clause or _names:
            _expected, _defects = set(_names), []
            if any(k != "own" for k in row.eligibility_kinds()):
                _expected.add(ELIGIBILITY_CLAUSE)
            if row.writes:
                _expected.add(WRITE_CLAUSE)
            if row.counterparty:
                _expected.add(COUNTERPARTY_CLAUSE)
            if _form == FORM_TASK:
                _expected.add(DRAW_CLAUSE)      # B07.01: a `task` row's lost draw (18-A item 4)
            if not by_clause:
                _defects.append(f"names conjuncts {list(_names)} and keys no refusal to them")
            # B07.01 (UNDECIDED (11) (ii)): a precondition may stay UNNAMED where the row declares ONE refusal kind -- its
            # refusal is then that kind whichever conjunct failed (`VerbRow.refusal_for(None)`), as on a flat row. The case is
            # a `task` row keyed only for its `draw` clause whose cell is an own-ledger conjunct (`forge`, `survey`): naming
            # it would make it carry `said` (`requires.TypedRequires.named_own_ledger_operands`), moving its formation.
            if row.has_precondition and len(row.emits_on_refusal) != 1 and (
                    (not _predicate_keys) if row.requires_typed is None
                    else (not row.requires_typed.names or None in row.requires_typed.names)):
                _defects.append("keys its refusals, so its precondition must be a typed cell with "
                                "EVERY top-level conjunct named")
            # ⚠ The party-gap refusal emits the UNION, which is `ID-9` only if the union holds more
            # than one kind -- a kind published for a conjunct that did not fail. A contested row
            # whose every key emits ONE kind (`tell`: `tell.refused` for `holds` and `hearer`) emits
            # exactly that kind at the party gap too.
            # ⚠ v9 IN-12 step 5 (#453 K-02, the party-gap fold edit): THE SEAM'S
            # PARTY GAP IS THE COUNTERPARTY CLAUSE FAILING, so a row that KEYS `COUNTERPARTY_CLAUSE`
            # emits that key's kinds there (`loop/resolve.py::_refuse_party_gap`) and not the union,
            # and may key two kinds (`arrest`: `arrest.unauthorized` / `arrest.refused`). The rule
            # still binds a contested or graded row that keys no counterparty. ⚠ S27.4's refusal (a
            # pool under 1D) reaches the same point and takes the counterparty kind too [ASSUMPTION;
            # medium; Jordan to correct; revert: this line without the `COUNTERPARTY_CLAUSE` test].
            # B07.01 (UNDECIDED (11) (i)): the count is of REFUSAL kinds (`emits_on_refusal`, which holds no `draw` kind), and a
            # `form: task` row -- nobody opposite, so no counterparty clause -- names the kind its refused roll emits by keying
            # `write`: its party gap emits that key's kinds (`loop/resolve.py::_refuse_party_gap`), as an act that did not take.
            # B21.81: THE SAME HOLDS FOR A CONTESTED ROW THAT NAMES NO `counterparty:` (`establish`, `revoke`): nobody is opposite
            # on the act's own face, so its party gap is likewise an act that did not take, and emits the `write` key's kinds.
            if ((row.contests or _graded) and len(row.emits_on_refusal) > 1
                    and COUNTERPARTY_CLAUSE not in by_clause
                    and not row.party_gap_at_write):
                _defects.append("declares `contests:` or a `graded_tasks` route, whose "
                                "party-gap refusal no clause names, keys no `counterparty` "
                                "refusal for it (nor, as a task, a `write` one), "
                                "and keys more than one refusal kind, so that refusal would emit "
                                "kinds for conjuncts that did not fail")
            _after_fold = set(_names) & FOLD_CLAUSES
            if _after_fold:
                _defects.append(f"names a conjunct after a fold clause ({sorted(_after_fold)})")
            _missing = sorted(_expected - set(by_clause)) if by_clause else []
            _extra = sorted(set(by_clause) - _expected - _predicate_keys)
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
        # LOADER INVARIANT 4, THE FLAT HALF (SC-02 `23`; S-8's residue: a row that still uses the flat
        # form where a conjunct is failable). A FLAT row's `emits_on_refusal:` is emitted WHOLE at every
        # refusal (`VerbRow.refusal_for`), so a flat row with two or more failable clauses -- eligibility,
        # each top-level conjunct of its cell (named or not: a flat row cannot name them), the write, the
        # counterparty -- and two or more refusal kinds publishes a kind for a clause that did not fail,
        # which is `ID-9` in the scarcity channel. The same holds of a contested or graded flat row at the
        # party gap (`loop/resolve.py::_refuse_party_gap`), a refusal point no clause names. The kinds the
        # fold FILTERS (`data/rosters.py::PERSON_DEMANDED`) do not count: the act earns them or they are
        # dropped. Such a row keys its refusals by clause (the keyed form above) or declares one kind.
        if not by_clause and not _names:
            _n_clauses = (int(any(k != "own" for k in row.eligibility_kinds()))
                          + (len(row.requires_typed.names) if row.requires_typed is not None
                             else int(row.has_precondition))
                          + int(bool(row.writes)) + int(bool(row.counterparty)))
            _unearned = [k for k in row.emits_on_refusal if k != PERSON_DEMANDED]
            if len(_unearned) > 1 and (_n_clauses >= 2 or row.contests or _graded):
                raise SystemExit(
                    f"verb_table.yaml: {name!r} is a FLAT row with {_n_clauses} failable clause(s)"
                    f"{' and a contest/graded party gap' if row.contests or _graded else ''} and "
                    f"declares {len(_unearned)} refusal kinds {_unearned}: a flat list is emitted "
                    "whole at every refusal, so a kind would be published for a clause that did not "
                    "fail. 04 §B.13 #4 (F7), the flat half -- key `emits_on_refusal:` by clause, "
                    "declare ONE kind (`data/rosters.py::PERSON_DEMANDED` is the one the fold keeps only when earned).")
        out[name] = row
    # -----------------------------------------------------------------------
    # LOADER INVARIANT 6 (`04_CODE_ARCHITECTURE.md` PART D row 15, MECHANICAL at load):
    # *"`release` generic; the loader asserts its domain equals `tenure_kinds \ {contain}`"*.
    #
    # ⚠⚠ **IT RUNS AFTER THE LOOP, SO IT CAN OBSERVE ITS OWN SUBJECT'S ABSENCE.** Inside the row
    # loop behind `if name == "release"`, deleting or renaming the row would mean the check never
    # executed: the load would succeed and the vocabulary be open-without-close again, which is the
    # state row 15 grades MECHANICAL at load (§0.1 pt 2).
    #
    # ⚠ THE ASSERTION IS AGAINST THE ROSTER, WHICH IS WHY THE COLUMN IS DECLARED AND NOT DERIVED.
    # `contain` is excluded because it is the one Tenure kind whose subject may be a Rung (PART D
    # row 13) and whose end is a MOVE, not a release -- `_eff_move` closes the old leg and opens
    # the new one, so a releasable `contain` would let a person leave a place for nowhere. Every
    # other kind in RELEASABLE_KINDS is an edge a person opened and must be able to end (T-m); a kind
    # outside it (`contain`, `reside`, `detain`, `ban`) is NOT checked here for a closer.
    #
    # This is the check `open-without-close in the vocabulary` names, for the releasable kinds: add an eighth tenure kind to
    # `rosters.yaml` and forget its closer, and the load fails HERE rather than shipping a relation
    # nothing can end.
    #
    # ⚠ ROW 15's SECOND HALF -- `04:466-467`, *"every kind's OPENER set is declared too"* -- IS
    # BELOW, after this check: `_derive_openers_from_effects()`, an AST walk over
    # `loop/effects.py`'s own `Tenure(...)` construction sites (`OPENERS-DERIVE`).
    # Declared-and-empty is REPORTED (`tenure_kinds_without_an_opener`), not refused.
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
    # stale when the exclusion grows (`contain`, `reside`).
    if _release_domain != RELEASABLE_KINDS:
        raise SystemExit(
            f"verb_table.yaml: `release` declares domain {sorted(_release_domain)}, and "
            f"`tenure_kinds \\ {sorted(frozenset(TENURE_KINDS) - RELEASABLE_KINDS)}` is "
            f"{sorted(RELEASABLE_KINDS)}. Loader invariant 6 "
            "(04 PART D row 15) requires them equal: a kind in the roster and not in this "
            "domain is an edge that can be opened and never closed, and a kind here and "
            "not in the roster is a closer for a relation that does not exist.")
    # LOADER INVARIANT 6, THE CLOSER CLAUSE (v9 IN-12 step 5, #453 §8.2 `:1518-1520`): *"every kind
    # outside `RELEASABLE_KINDS ∪ {contain, reside}` must sit in some row's declared `domain:`, read on
    # every row"*. The check above compares `release`'s domain with `RELEASABLE_KINDS` and EXEMPTS every
    # excluded kind, so a kind its holder may not release (`detain`, `ban`, `data/rosters.py::
    # RESTRAINT_KINDS`) could be opened and closed by nobody and load clean. The kinds that end by a relocation stay exempt
    # (`contain`, `reside`: `_eff_move`/`_eff_migrate` close the old edge as they open the new). The set
    # that needs a declared closer is READ off `data/rosters.py`, never spelt: `RESTRAINT_KINDS`, the
    # kinds excluded from `RELEASABLE_KINDS` because an AUTHORITY ends them -- today exactly the kinds
    # outside `RELEASABLE_KINDS ∪ {contain, reside}`; no third excluded set can exist, because
    # `RELEASABLE_KINDS` is DEFINED in `data/rosters.py` as `TENURE_KINDS` less that pair less
    # `RESTRAINT_KINDS`. A declared closer naming a kind that needs none (a releasable kind -- `release`'s,
    # a second closer of an edge whose holder ends it himself, T-m -- or no kind at all) is refused too:
    # [ASSUMPTION; medium; Jordan to correct] an addition beyond #453 `:1518-1520`, which asks only that
    # every restraint have a closer; revert: drop `_stray_domain` and its refusal.
    _needs_closer = frozenset(RESTRAINT_KINDS)
    _stray_domain = sorted((v, sorted(d - _needs_closer)) for v, d in _closer_domains.items()
                           if d - _needs_closer)
    if _stray_domain:
        raise SystemExit(
            f"verb_table.yaml: declared `domain:` member(s) {_stray_domain} name no kind that needs a "
            f"declared closer ({sorted(_needs_closer)}). A `domain:` outside `release` closes a kind "
            "its holder cannot release; a releasable kind is `release`'s, and a non-kind closes nothing.")
    _unclosed = sorted(_needs_closer - frozenset().union(*_closer_domains.values()))
    if _unclosed:
        raise SystemExit(
            f"verb_table.yaml: Tenure kind(s) {_unclosed} are restraints (`RESTRAINT_KINDS`: their "
            "holder may not release them) and no row declares them in its `domain:`. #453 §8.2's "
            "closer clause (loader invariant 6) -- a kind no act can close is an edge opened forever; "
            "declare its closer's `domain:` (`pardon`: `[detain, ban]`).")
    # LOADER INVARIANT 6, SECOND HALF (`04 §B.13 #6`, `04:466-467`, `ID-14`): EVERY KIND'S OPENER
    # SET IS DECLARED. `_derive_openers_from_effects()` seeds every `TENURE_KINDS` member with an
    # empty list before it reads anything, so "a kind with no entry" is impossible BY
    # CONSTRUCTION rather than checked (`CLAUDE.md` §0.1 pt 2 -- "an assertion must be able to
    # observe the failure it excludes"). What is checked is what a derivation cannot rule out by
    # construction: an opener naming a verb `verb_table.yaml` does not have -- a typo or an
    # orphaned `@effect_for` registration in `loop/effects.py`.
    _openers = _OPENERS_FROM_EFFECTS
    _stray = sorted((k, v) for k, vs in _openers.items() for v in (vs or []) if v not in out)
    if _stray:
        raise SystemExit(
            f"loop/effects.py: a `Tenure(...)` construction names opener(s) that are no verb: "
            f"{_stray}. 04 §B.13 #6 -- an opener is a row of verb_table.yaml.")
    # v9 FI-01 (`ED-FI-0009`): THE TWO INQUIRY ROSTERS, AGAINST THE TABLE THEY KEY ON. A route on no
    # verb row, a route carrying anything but its two fields (a `module:` would make it read as a
    # prize row), or a skipped kind no row declares is refused naming it: a misspelled skip would
    # skip nothing and report the deposit half built.
    # B07.01: the route carries `form:` (one of `ROUTE_FORMS`) and may carry `armed_by:`, a `Fixtures` member shipped
    # `on` or `off` (UNDECIDED (11) (iii)); nothing else.
    _declared_kinds = {k for v in out.values() for k in (*v.emits, *v.emits_on_refusal)}
    _bad = sorted(
        [f"route {v!r}: no verb row" for v in GRADED_TASKS if v not in out]
        + [f"route {v!r}: fields {sorted(r) if isinstance(r, dict) else r!r}"
           for v, r in GRADED_TASKS.items()
           if not isinstance(r, dict) or "form" not in r or not {"provider", "module_entry"} <= set(r)
           or not set(r) - {"provider", "module_entry"} <= {"form", "armed_by"}]
        + [f"route {v!r}: `form: {r.get('form')!r}` is none of {list(ROUTE_FORMS)}"
           for v, r in GRADED_TASKS.items() if isinstance(r, dict) and r.get("form") not in ROUTE_FORMS]
        + [f"route {v!r}: `armed_by: {r['armed_by']!r}` names no `Fixtures` member shipped `on` or `off`"
           for v, r in GRADED_TASKS.items()
           if isinstance(r, dict) and "armed_by" in r and _arm_default(str(r["armed_by"])) not in ("on", "off")]
        + [f"undeposited kind {k!r}: no verb row declares it"
           for k in UNDEPOSITED_KINDS if k not in _declared_kinds])
    if _bad:
        raise SystemExit(f"rosters.yaml: `graded_tasks` / `undeposited_kinds`: {_bad}. A route is "
                         "a verb row's `{provider, module_entry, form[, armed_by]}` and nothing else; a skipped "
                         "kind is one some row emits.")
    _check_resolution_classes(out)
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
    # B05.25: EVERY ROW IS ONE OF FOUR KINDS (`_check_governing_attributes`; B24p.16 added `proceeds`), and a `proceeds:` cell is routing the load checks.
    _check_governing_attributes(out, _PRIZES)
    _check_proceeds(out)
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
    (computed, not read off the roster)."""
    return sorted(k for k, vs in _OPENERS_FROM_EFFECTS.items() if not vs)


def arrangements_without_a_disposal_opener() -> list[str]:
    """C-1, AS A REPORT (see module docstring for why refusing is wrong today). Every arrangement
    id whose `disposes` kind has no opener naming `determine` -- or, for `close: consent` (was `disposal: mutual`), whose
    `oblige` has no opener at all -- in `data/verbs.py::_derive_openers_from_effects()`'s map.

    ⚠ A `disposal: mutual` row passes this check, because `oblige` has an opener (`_eff_oblige`, the
    joiner's own act). It reports only the seeded rows this check actually ASKS: a row disposing
    `Record` or `none` is excluded below (`continue`, "C-1 is about a TENURE kind's opener; neither
    is one"), so it is the seeded rows disposing a real Tenure kind or `mutual` that report today,
    not every seeded row -- `test_arrangements.py` pins this exactly (`["arbitration"]`, the one
    seeded row disposing a Tenure kind, against two `Record`-disposing rows that are correctly
    absent). That is the disclosed gap this function exists to make checkable rather than silent --
    the same shape `tenure_kinds_without_an_opener()` already reports one file over.

    ⚠ AND THE GAP CLOSED AT PLAN POSITION `19`: `_eff_determine` opens the disposal `oblige`, so
    `arbitration` is no longer reported and the pinned report is `[]` (see the module docstring's
    `19` paragraph for why it stays a report)."""
    openers = _OPENERS_FROM_EFFECTS
    out = []
    for name, row in ARRANGEMENTS.items():
        if row["close"] == "consent":
            if not openers.get("oblige"):
                out.append(name)
            continue
        kind = row["disposes"]
        if kind in _DISPOSES_LITERALS:
            continue                      # C-1 is about a TENURE kind's opener; `Record`, `none` and `yield` are none
        if "determine" not in (openers.get(kind) or ()):
            out.append(name)
    return out

# B24p close: this report lived in `data/arrangements.py` and read this module's opener map by a deferred import; once `_check_proceeds` here
# read `ARRANGEMENTS` the two modules were an import cycle (`tests/valoria/test_import_cycle_game_state_npe.py`). It sits beside
# `tenure_kinds_without_an_opener`, the same shape, and `arrangements.py` imports nothing from this file.

VERB_TABLE = _load_verb_table()


def _quantity_stems(table: dict) -> frozenset:
    """THE STEMS OF AN AMOUNT (v12 B11.51, `16_PESSIMIST_FI_A` edit 1): the stems of every `scalar_threshold` clause any row's `requires_typed`
    carries -- whatever the table compares against a threshold -- kept to the ones a cell holds (`data/requires.py: CELL_STEMS`). Derived,
    never spelt, on `CELL_STEMS`' own precedent. A rumour may garble an amount (`loop/witness.py::_told_value`; the liar's number,
    `queries/person_q.py::lie_said_of`); a numeric value on any other stem is an existence reading stored as 0/1 and is passed whole."""
    out = set()

    def walk(req) -> None:
        if isinstance(req, AllOf):
            for c in req.clauses:
                walk(c)
        elif isinstance(req, ScalarThreshold):
            out.update(req.stems())
    for row in table.values():
        if row.requires_typed is not None:
            walk(row.requires_typed.requirement)
    return frozenset(out) & CELL_STEMS


QUANTITY_STEMS = _quantity_stems(VERB_TABLE)

# B04.04 (U1-A steps 2-3): WHICH SKILL A VERB TESTS, DERIVED FROM THE ROW THAT HOLDS IT -- the `capability:` column on this table
# (`descriptors.CAPABILITIES` defines the skill, `descriptor_registry.yaml: capabilities`). The `rosters.yaml: verb_capability`
# roster it replaces is deleted; `data/rosters.py` re-exports nothing of it (it loads BEFORE this table and may not import it,
# which is why the derivation lives here). `none` is spelled on a row that contests with no skill (`lie`, `march`) and is in no map.
# B05.25: WHICH ATTRIBUTES A VERB READS is the verb row's own `governing:` and `opposed_attribute:` -- the attribute lives on the
# verb, not the skill (`inquiry` serves `examine`, `surveil` and `research`, which rely on different attributes). The skill row's
# `base:` and `opposed_by:` columns, and `VOCATION_ATTRIBUTE` and `VOCATION_OPPOSED_BY` read off them, are deleted.
VERB_CAPABILITY = {row.verb: row.capability for row in VERB_TABLE.values() if row.capability not in ("", "none")}
VOCATIONS = frozenset(VERB_CAPABILITY.values())


def skills_without_a_verb() -> list:
    """The defined skills (`descriptors.CAPABILITIES`) no verb row's `capability:` names -- REPORTED, not refused, as
    `tenure_kinds_without_an_opener` reports an unopened kind: a lifepath template may grant a skill no verb yet tests
    (B04.04), and which of them are holes is a judgement, not a load failure."""
    return sorted(set(CAPABILITIES) - VOCATIONS)

# v9 IN-12 step 6: `{verb: record kind}` -- the verbs whose `subject` a HELD record of that kind names
# (`rosters.yaml: warrant_sourced`). REFUSED AT IMPORT, so a stale line cannot read as "no verb needs a
# warrant" (`data/requires.py::_check_record_sourced`'s reason): a verb the table does not carry would
# narrow nothing, and a kind `record_sourced_operands` gives no `subject` key would answer nothing, so
# the verb would form for nobody. Read here, with the table it is checked against, so the person side
# (`decision/options.py`) and the world side (`loop/effects_information.py`) import one cross-validated
# map (Layer 1 §A.1, one loader per roster) and neither owns it.
WARRANT_SOURCED = dict(roster_map("warrant_sourced", "values"))
for _v, _k in WARRANT_SOURCED.items():
    if _v not in VERB_TABLE or "subject" not in RECORD_SOURCED_OPERANDS.get(_k, {}):
        raise Forbidden(
            f"`rosters.yaml: warrant_sourced` names {_v!r}: {_k!r}, and either the verb table carries no "
            f"such verb or `record_sourced_operands.{_k}` maps no `subject`", "rosters.yaml",
            needs="a `verb_table.yaml` verb, and a record kind whose `subject` a held Record answers",
            law="IN-12 step 6 -- a warrant-sourced verb forms only on what a held warrant names")

def _derive_minted_record_kinds() -> dict:
    """`{verb: {record kind}}` -- WHICH `record_kinds` MEMBER EACH VERB'S EFFECT MINTS (B21.17), derived as `OPENERS-DERIVE` derives
    openers: from `_mint_document(w, a, <kind>, ...)`, the one mint, inside the function `@effect_for` registers for the verb or a
    helper it reaches (`_effect_calls`). The kind is read where it is a string literal or a name `data/rosters.py` binds to one
    (`CHALLENGE_KIND`); a kind passed through a variable (`create_record`'s) or from another module's attribute is not read, so a
    verb minting only those has no entry. `covenant` reaches `issue`'s body, so it mints `dispensation`."""
    minted: dict = {}
    for verb, call in _effect_calls():
        if not (isinstance(call.func, ast.Name) and call.func.id == "_mint_document"):
            continue
        arg = call.args[2] if len(call.args) > 2 else next((kw.value for kw in call.keywords if kw.arg == "kind"), None)
        kind = (arg.value if isinstance(arg, ast.Constant) else
                getattr(_rosters, arg.id, None) if isinstance(arg, ast.Name) else None)
        if isinstance(kind, str):
            minted.setdefault(verb, set()).add(kind)
    return {v: frozenset(ks) for v, ks in minted.items()}


def _check_record_verb_minting(name: str, mapping: dict, table: dict, minted: dict) -> None:
    """REFUSAL (c) OF `rosters.yaml: read_to_addressee` AND `proclaimed` (`data/rosters.py::check_record_verb_rosters` has (a), (b)
    and (d)): every verb a kind lists is a `verb_table.yaml` row whose effect mints that kind. A function, so a test can plant a
    bad line and watch it refuse. ⚠ IT CANNOT TELL `covenant` FROM `issue` ON `dispensation`: both mint one, which is why the
    verb list, and not the kind, is the roster's content."""
    for kind, verbs in mapping.items():
        for verb in sorted(verbs):
            if verb not in table or kind not in minted.get(verb, ()):
                raise Forbidden(
                    f"`rosters.yaml: {name}` lists {verb!r} for {kind!r}, and either the verb table carries no such verb or "
                    f"its effect does not mint a {kind!r} Record", "rosters.yaml",
                    needs=f"a `verb_table.yaml` verb whose effect mints a {kind!r} document (`_mint_document`)",
                    law="B21.17 (c) -- the verb qualifier names the mint the roster covers, so a verb that mints something "
                        "else would be covered by a line that reads as covering it")


_MINTED_RECORD_KINDS = _derive_minted_record_kinds()
for _n, _m in (("read_to_addressee", READ_TO_ADDRESSEE), ("proclaimed", PROCLAIMED)):
    _check_record_verb_minting(_n, _m, VERB_TABLE, _MINTED_RECORD_KINDS)

# CP-T03-09: `{verb: term}` -- the terms a verb's personal-combat scene is fought under (`rosters.yaml:
# duel_terms`), read by `seam/wrappers/combat.py::combat_input`. REFUSED AT IMPORT for a verb the table lacks or
# a term that is not a non-empty string. THE TERM'S MEMBERSHIP IN THE ENGINE'S CLOSED SET (`modules/combat/
# wrapper.py::DUEL_TERMS`) IS NOT CHECKED HERE: `engine/season/data` imports no module, so the seam, which may
# reach the engine, refuses a value outside that tuple (`combat.py::duel_terms_of`) -- checked against it, never
# re-declared in this tree.
def _check_duel_terms(values: dict, table: dict) -> dict:
    """`rosters.yaml: duel_terms` held to the verb table, or import refuses naming the line. A function, so a test
    can plant a bad line and watch it refuse."""
    for verb, term in values.items():
        if verb not in table or not isinstance(term, str) or not term:
            raise Forbidden(
                f"`rosters.yaml: duel_terms` names {verb!r}: {term!r}, and either the verb table carries no such "
                f"verb or the term is not a non-empty string", "rosters.yaml",
                needs="a `verb_table.yaml` verb and a term the engine names (`modules/combat/wrapper.py::DUEL_TERMS`)",
                law="CP-T03-09 -- a verb's duel terms are a term of the engine's closed set, read from one roster")
    return dict(values)


DUEL_TERMS_BY_VERB = _check_duel_terms(dict(roster_map("duel_terms", "values")), VERB_TABLE)


# B15.08 (PHY_A A3): `{context: term}` -- the terms a `fight` is fought under by the context of violence that formed it
# (`rosters.yaml: context_terms`, `duel_terms`' shape), read by `seam/wrappers/combat.py::combat_input` when `duel_terms`
# names no line for the verb. REFUSED AT IMPORT for a key or a term that is not a non-empty string; THAT A KEY IS A CONTEXT
# READER is `decision/options.py::_check_context_terms`'s (the readers are `options.py`'s, `violence_contexts`' split), and
# THAT A TERM IS THE ENGINE'S is `combat.py::duel_terms_of`'s, `duel_terms`' own: checked against the tuple, never re-declared.
def _load_context_terms(values: dict) -> dict:
    """`rosters.yaml: context_terms`' `values`, checked and frozen. A function, so a test can plant a bad line."""
    for context, term in (values or {}).items():
        if not isinstance(context, str) or not context or not isinstance(term, str) or not term:
            raise Forbidden(
                f"`rosters.yaml: context_terms` names {context!r}: {term!r}, and either the context or the term is not a "
                "non-empty string", "rosters.yaml",
                needs="a context `decision/options.py` reads and a term the engine names (`modules/combat/wrapper.py::DUEL_TERMS`)",
                law="PHY_A A3 -- a fight's terms follow the context that formed it, read from one roster")
    return dict(values or {})


CONTEXT_TERMS = _load_context_terms(roster_map("context_terms", "values"))


def derive_event_kinds(table: dict, matrix: dict, fold_kinds: dict, logged_kinds: dict) -> frozenset:
    """LOADER INVARIANT 7 (`04 §B.13 #7`, `F.20b`): THE EVENT-KIND ROSTER IS DERIVED FROM EVERY EMISSION
    COLUMN. The columns are: each verb row's `emits` (every Degree branch), its `emits_on_refusal`
    (every clause) and `write_matrix.yaml`'s `emits:` (the kinds a gate write may emit), plus the
    fold's own `fold_kinds` (`rosters.yaml`) and `logged_kinds` (the
    kinds `loop/matter.py` logs with no write behind them). Nothing else adds a
    member, and the derivation is a function of its arguments so a test can plant a malformed column.

    ⚠ A KIND IS `<noun>.<verb>`: two non-empty dotted parts. A column holding anything else (a typo
    that lost the dot, an empty string from a stray comma) is refused at load NAMING ITS ROW, because
    an Event of that kind would be emitted, fanned and read by a predicate spelled the same wrong way
    and nothing would ever say the roster never held it. `loop/resolve.py::_act_events` refuses a kind
    outside this roster when the fold builds the Event (the F.20b defect, observed at execution)."""
    out: set = set()
    for name, row in table.items():
        cols = {"emits": row.emits, "emits_on_refusal": row.emits_on_refusal,
                **{f"emits[{d}]": ks for d, ks in row.emits_by_degree.items()},
                **{f"emits_on_refusal[{c}]": ks for c, ks in row.refusals_by_clause.items()}}
        for col, kinds in cols.items():
            for k in kinds:
                if not is_event_kind(k):
                    raise SystemExit(
                        f"verb_table.yaml: {name!r} declares Event kind {k!r} in `{col}:`, which is "
                        "not `<noun>.<verb>`. 04 §B.13 #7 -- the Event-kind roster is derived from "
                        "every emission column, so a column holding a malformed kind admits a kind "
                        "no reader spells the same.")
                out.add(k)
    for (kind, fld), mrow in matrix.items():
        for k in mrow.emits:
            if not is_event_kind(k):
                raise SystemExit(
                    f"write_matrix.yaml ({kind}, {fld}) declares Event kind {k!r} in `emits:`, which "
                    "is not `<noun>.<verb>`. 04 §B.13 #7 -- the Event-kind roster is derived from "
                    "every emission column.")
            out.add(k)
    out.update(fold_kinds.values())
    out.update(logged_kinds.values())
    return frozenset(out)


EVENT_KINDS = derive_event_kinds(VERB_TABLE, MATRIX, FOLD_KINDS, LOGGED_KINDS)


def act_key(verb: str, subject, operands) -> str:
    """WHAT AN ACT'S ID IS OF, AFTER ITS VERB: `H(seed, tick, actor, f"act:{verb}:{act_key}")`.
    The subject, and -- for a row whose cell binds a known-person operand beside `subject`
    (`VerbRow.known_person_operands`: `tell`'s and `give`'s `to`, the untyped `confer`'s, and
    `issue`'s, whose `terms` conjunct binds `subject` beside its executor) -- that operand too, as
    `subject>to`. A bag a HELD Record forms (`decision/options.py::operand_bags`, IN-10) names its
    addressee there the same way, so it keys exactly as the known-person bag for that person would
    and the fan drops it as a duplicate.

    ⚠ ONE TOPIC FORMS ONE `tell` PER PERSON THE TELLER KNOWS, so two acts in one deliberation would
    share `(actor, verb, subject)` and therefore one id, and `state/acts.py` would refuse the
    second (`act id ... is already in the store`). Every row that binds no such operand answers its
    subject alone.

    ⚠ `H-134`: AND THE SEAT, WHEN THE CANDIDATE WAS FORMED AMONG SEVERAL. A person holding two seats
    that grant the same act forms one Candidate per seat (`decision/options.py::opening_set`), the
    seat riding in the operands under `VIA`; two of them share `(actor, verb, subject)`, so without it
    they would share an id and `state/acts.py` would refuse the second. Present only for such a
    Candidate -- a person with one seat carries no `VIA`.
    ⚠ AND THE VOCATION, FOR A ROW THAT CARRIES ONE (`VOCATION_SOURCED`, v10 REM-30's vocation rows, now
    the verb table's `capability:` column). A `train` Candidate is formed once per vocation in `VOCATIONS` on the same subject, the
    vocation riding on the `kind` operand (`decision/options.py::opening_set`); two chosen in one
    deliberation share `(actor, verb, subject)` and `state/acts.py` refuses the second. Present only on
    a row `vocation_sourced` names.
    ONE OWNER for both minting sites: `decision/choose.py::pack_scenes` and
    `loop/deliberate.py::_qualify_by_lap` (`04 PART D row 35`: purpose uniqueness is a
    convention, and this is where it is kept)."""
    key = "" if subject is None else str(subject)
    row = VERB_TABLE.get(verb)
    ops = operands if isinstance(operands, dict) else {}
    voc = VOCATION_SOURCED.get(verb)
    if voc is not None and ops.get(voc) is not None:
        key += f"#{ops[voc]}"
    if row is not None:
        for n in row.known_person_operands():
            if ops.get(n) is not None:
                key += f">{ops[n]}"
    # CP-T04-02: AND THE CHOICE, FOR A ROW THAT CARRIES ONE (`CHOICE_SOURCED`, `marshal`'s `role` and `retreat_at`). A
    # Candidate is formed once per combination on the same subject, so two chosen in one deliberation would share
    # `(actor, verb, subject)` and `state/acts.py` would refuse the second. Present only on a row the roster names.
    for _, v in choice_values(verb, ops):
        key += f"#{v}"
    if ops.get(VIA) is not None:
        key += f"@{ops[VIA]}"
    return key


def opportunity_key(verb: str, subject, operands) -> Optional[tuple]:
    """WHAT MAKES TWO ACTS ONE OPPORTUNITY, FOR THE ONCE-PER-SEASON FILTER: `(verb, subject)`, plus
    the counterparty where the row names one -- `(verb, subject, <the operand its `counterparty:`
    column names>)`. `None` for an act that names no subject: it has no opportunity to be the same as,
    so it is never recorded and never filtered (`loop/deliberate.py::_drop_what_was_already_done`).

    ⚠ A PERSON CAN TELL SEVERAL HEARERS, so a `(verb, subject)` key would bar telling a topic told
    to B to D that season. The key is the GENERAL rule for a row that names a `counterparty:`, read
    off the ROW'S COLUMN and never a verb name; `tell`, `give` (typed and formable, its subject the
    Record and its counterparty `to` the receiver, one Candidate per person the giver knows:
    `decision/options.py::operand_bags`) and `issue` (one writ about a referent per executor the
    issuer knows) are the rows where it changes anything. `petition` always has `to` == `subject`
    (a computed Candidate's one referent), so its key is unchanged. Where the counterparty IS the
    subject (`determine`, `oblige`) it adds nothing and is left out.

    ONE OWNER, BOTH SITES: `loop/driver.py` (writes a realised act) and `loop/deliberate.py`
    (reads it) both call this, so the key cannot be spelled two ways (`CLAUDE.md` §8). It sits beside
    `act_key`, which reads the same operands for the act's id, and needs no `World` or carrier."""
    if not subject:
        return None
    row = VERB_TABLE.get(verb)
    ops = operands if isinstance(operands, dict) else {}
    other = ops.get(row.counterparty) if row is not None and row.counterparty else None
    # ⚠ `H-134`: THE SEAT IS NOT IN THIS KEY, and that is chosen, not forgotten. `act_key` carries it
    # (ids must stay distinct), but an opportunity is the verb on the subject (and counterparty) for
    # the ACTOR, however many seats could have done it: the key's shape must not depend on how many
    # seats the person holds at the moment, or a seat gained or lost mid-season would let one
    # realised act be realised again. A refused act through the wrong seat is never recorded (the
    # driver records REALISED acts only), so it does not bar the same act through the right seat.
    # Two seat-acts formed in ONE deliberation share this key and BOTH survive: `loop/deliberate.py`
    # filters only against what EARLIER laps realised (`_drop_what_was_already_done`, one call
    # site) and a queued scene is released without re-filtering, so the key bars a twin only across
    # a re-deliberation.
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

    ⚠⚠ THE LOADERS SHARE THESE CHECKS HERE: §8 says the rule lives once, so a fourth check or a
    change to the all-zero test is made once. The LAW STRINGS stay per-caller, because what a
    violation means differs by table."""
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

    ⚠⚠ **THIS TABLE MAPS CONVICTIONS TO AXES, WHICH ARE TWO ROSTERS.** Jordan, 2026-09-02:
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
# declared `sweep:` on its row and NO `projection_at()`, so a frozen copy here would be a
# second 15x7 in memory that a reader assumes is wired to something because its sibling is.
PROJECTION_DEFAULT_CELL = float(table_meta("pursuit_projection").get("default_cell", 0.0))


def _load_role_template_pursuits(rows: Optional[dict] = None) -> dict:
    """`tables.role_template_pursuits`, CHECKED AT LOAD, because its one read path cannot refuse.

    ⚠ `data/cast.py::loyalty` reads this table through
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

    `EMITTED_KINDS` is every event kind some verb row can emit, success, lost draw (`VerbRow.draw_kinds`) or refusal. `KIND_VERB`
    maps a kind to its verb ONLY where exactly one row emits it: a kind several rows emit names no
    single verb, so it maps to nothing rather than to whichever row happened to sort first. Both
    are read off the table once at load -- no kind or verb is listed here."""
    emitters: dict = {}
    for verb, row in VERB_TABLE.items():
        for kind in set(row.emits) | set(row.emits_on_refusal) | set(row.draw_kinds):   # B07.01: a lost draw is emitted too
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


def _check_deed_kinds(kinds, deed_kinds, message, where, law) -> frozenset:
    """A roster of event kinds a closed set may name is held to `DEED_KINDS` (a kind some verb row emits,
    on no row's refusal), or import refuses naming the members: a kind no act emits partitions nothing
    and leaves nothing, and what it feeds would read as built. A function, so a test can plant a bad
    member and watch it refuse. `message` takes `{bad}`. Returns the members."""
    bad = sorted(k for k in kinds if k not in deed_kinds)
    if bad:
        raise Unspecified(
            message.format(bad=bad), where,
            needs="name kinds in `data/verbs.py::DEED_KINDS` (emitted by some row, on no row's refusal)",
            law=law)
    return frozenset(kinds)


def _check_covert_kinds(kinds, deed_kinds) -> frozenset:
    """v9 FI-03 (`ED-FI-0002`): every `rosters.yaml: covert_kinds` member is a DEED kind the verb table
    emits -- a misspelled or refusal kind would be a trail nothing leaves."""
    return _check_deed_kinds(
        kinds, deed_kinds, "`covert_kinds` {bad} are not deed kinds the verb table emits",
        "rosters.yaml -- covert_kinds",
        "ED-FI-0002 -- a trail is an Event some act leaves; a kind no row emits, or a refusal "
        "kind, leaves none, and the trail would read as built")


def _check_dominance_kinds(kinds, deed_kinds) -> frozenset:
    """v9 SC-02 `22a` (step 20, route erosion): every `rosters.yaml: standing_routes` `dominance` member
    is a DEED kind -- the partition is of the kinds of act a hearer's claims record."""
    return _check_deed_kinds(
        kinds, deed_kinds, "`standing_routes.kinds.dominance` names {bad}, which are not deed kinds",
        "rosters.yaml -- standing_routes",
        "19_PLAN.md step 20 -- the partition is of the KINDS OF ACT a hearer's claims record; a "
        "kind no act emits partitions nothing, and erodes nothing, forever")


def _check_strife_kinds(lists, event_kinds) -> dict:
    """CR-75 (`rosters.yaml: strife_kinds`): the four strife kind lists are held to the Event-kind roster
    (`04` §B.13 invariant 7, which derives it from every emission column and lets the log accept no other),
    or import refuses naming the members. Three refusals: a kind in any list absent from `event_kinds`;
    a kind in more than one of `opens`, `joins`, `never` (a decision per kind, not two); a `concludes`
    kind outside `opens` and `joins` (a `never` kind is no move, so it cannot conclude a strand). A function,
    so a test can plant each and watch it refuse. `lists` is `{name: iterable of kinds}`. Returns it."""
    unknown = sorted({k for ks in lists.values() for k in ks if k not in event_kinds})
    if unknown:
        raise Unspecified(
            f"`strife_kinds` names {unknown}, which are not Event kinds the loop declares", "rosters.yaml -- strife_kinds",
            needs="name kinds in `data/verbs.py::EVENT_KINDS`",
            law="04 §B.13 invariant 7 -- the Event-kind roster is derived from every emission column; a kind "
                "outside it is one the log accepts from no one, and the list would read as built")
    placed = {}
    for n in (n for n in lists if n != "concludes"):    # the three decisions; `concludes` is derived from them
        for k in lists[n]:
            placed.setdefault(k, []).append(n)
    twice = sorted((k, ns) for k, ns in placed.items() if len(ns) > 1)
    if twice:
        raise Unspecified(
            f"`strife_kinds` places {twice} in more than one of opens, joins and never", "rosters.yaml -- strife_kinds",
            needs="move each kind to the one list it belongs in",
            law="CR-75 -- the lists are a decision per kind; two lists is two decisions with a read-order tiebreak")
    stray = sorted(k for k in lists["concludes"] if k not in lists["opens"] and k not in lists["joins"])
    if stray:
        raise Unspecified(
            f"`strife_kinds.concludes` names {stray}, which are in neither opens nor joins", "rosters.yaml -- strife_kinds",
            needs="a kind in `opens` or `joins`, or drop it from `concludes`",
            law="CR-75 -- a strand is made of moves; a kind that is no move (`never`, or in no list) concludes nothing")
    return lists


def _check_standing_occasion_opened_by(by_class, event_kinds) -> dict:
    """B09.12 (`rosters.yaml: standing_occasion_opened_by`): every listed kind is an Event kind the loop declares
    (`EVENT_KINDS`: a verb row's `emits`, the fold's kinds, and the MATTER and CALENDAR kinds), by the same test
    `_check_strife_kinds` makes, or import refuses naming the members -- a kind no one emits would be an opening Event
    `World.last_emission_of` never finds, and the roster would read as built. The class keys and shape are
    `data/rosters.py::_load_standing_occasion_opened_by`'s. A function, so a test can plant a bad kind. Returns it."""
    unknown = sorted({k for ks in by_class.values() for k in ks if k not in event_kinds})
    if unknown:
        raise Unspecified(
            f"`standing_occasion_opened_by` names {unknown}, which are not Event kinds the loop declares",
            "rosters.yaml -- standing_occasion_opened_by",
            needs="name kinds in `data/verbs.py::EVENT_KINDS`",
            law="04 §B.13 invariant 7 -- the Event-kind roster is derived from every emission column; a kind "
                "outside it is one the log accepts from no one, and no opening Event would ever be found")
    return by_class


_check_covert_kinds(COVERT_KINDS, DEED_KINDS)
_check_strife_kinds(STRIFE_KINDS, EVENT_KINDS)
_check_standing_occasion_opened_by(STANDING_OCCASION_OPENED_BY, EVENT_KINDS)
_check_dominance_kinds(DOMINANCE_KINDS, DEED_KINDS)

# B11.73 (`08_FI_03` §3 act 1; FRES §7 (1)-(2)): A CONCLUSION IS WHAT A PERSON DECIDES HAPPENED AND WHO DID IT, FROM WHAT HE HOLDS. The kind a row reports a winning
# `reconstruct` as (`conclusion.reached`), the payload key his conclusion rides the act under (`concluded`: `(the one the deed was done to, <deed kind>,
# doer)`, read off his OWN ledger at CHOOSE by `queries/person_q.py::_concluded`, with `conclusion_cites` for what each rests on) and the predicate stem WITNESS deposits it under to the maker
# (`concluded:<deed kind>`, `loop/witness.py`). `CONCLUDING_VERBS` is read off the table, no verb listed: the rows that report the kind. Refused at import when
# no row does, so a deposit nothing forms an act for cannot read as built.
CONCLUSION_KIND, CONCLUDED_KEY, CONCLUDED_STEM = "conclusion.reached", "concluded", "concluded"
# B11.75 (`19_LACUNA` R-19-04): WHICH SUSPECT IS A CHOICE. Where his ledger names several doers of a deed on one subject, `opening_set` forms one `reconstruct` Candidate per
# `(deed kind, doer)`, each carrying its own `concluded` triple, the claims that name him (`CITES_KEY`) and this key -- its place among them -- so the acts' ids differ
# (`choice_values`: `concluded` is a choice only where fanned, as `said` is); `decision/choose.py::settle_conclusions` keeps one, drawn by support.
CONCLUDED_RANK_KEY = "concluded_rank"
CONCLUDING_VERBS = frozenset(v for v, r in VERB_TABLE.items() if CONCLUSION_KIND in r.emits)
if not CONCLUDING_VERBS:
    raise Unspecified(
        f"no verb row emits {CONCLUSION_KIND!r}", "verb_table.yaml -- B11.73",
        needs=f"a row whose `emits:` reports {CONCLUSION_KIND!r}, or the conclusion's constants removed",
        law="FRES §7 -- a conclusion is deposited to the maker of the act that reaches it; a kind no row emits deposits to no one")


def _asks_subject_held(row: "VerbRow") -> bool:
    """WHETHER THE ROW'S TYPED CELL ASKS THE ACTOR TO HOLD ITS `subject` -- a `relation` conjunct of
    `subject`, `held_by`. The ONE reader of that conjunct: the two derivations of the Record kinds a held
    document is an occasion for (`RECORD_REFERENT_KINDS`, `HOLDING_RECORD_KINDS`) are told apart by it. (The person's own
    reading of the conjunct at formation is `OwnStateReader`'s `held_by`, B10.59.)"""
    if row.requires_typed is None:
        return False
    req = row.requires_typed.requirement
    return any(isinstance(c, Relation) and c.of == "subject" and c.relation == "held_by"
               for c in (req.clauses if isinstance(req, AllOf) else (req,)))


def _derive_record_referent_kinds() -> frozenset:
    """IN-09 (H-203, DECISION 2026-10-13 [ASSUMPTION; medium; Jordan to correct]): THE RECORD KINDS
    A HELD WRIT IS AN OCCASION FOR -- the `kind` of every `existence` clause of `subject` on a row
    declaring `referent_class: Record` whose cell asks no `held_by` of `subject` (`comply`:
    `dispensation`). Read off the rows that answer a held Record, so the stamp
    (`queries/world_q.py::writs_held`) and the cell the fold asks cannot name different kinds, and no
    kind literal lives at the stamp site. THE ROWS WHOSE CELL DOES ASK `held_by` are the other term
    (`HOLDING_RECORD_KINDS`, below): `writs_held` keeps its addressee test, which a row that needs
    only the person to HOLD the Record (`carry`'s petition) does not want. Empty when no row declares
    the class: then nothing is stamped. A row declaring it and naming no record kind is refused at
    load (`_load_verb_table`), so the union of both sets is empty only when no row declares `Record`.
    v10 REM-2C: SUB-KINDS ONLY (`_record_subkinds_answered`) -- `research` asks `existence` of the class
    itself and adds no kind here."""
    return frozenset(k for row in VERB_TABLE.values() if not _asks_subject_held(row)
                     for k in _record_subkinds_answered(row))


RECORD_REFERENT_KINDS = _derive_record_referent_kinds()


def _derive_holding_record_kinds() -> frozenset:
    """v10 REM-25 (B10-05, AM-A-10; M19 taken, [ASSUMPTION; medium; Jordan to correct]): THE RECORD
    KINDS A PERSON'S HOLDING IS AN OCCASION FOR -- the `kind` of every `existence` clause of `subject` on
    a row declaring `referent_class: Record` whose cell ALSO asks `held_by` of `subject` (`carry`:
    `petition`; `found` and `build`: `works`). Read off the rows, `RECORD_REFERENT_KINDS`' shape, so the
    stamp (`queries/world_q.py::records_held_for_holding_rows`) and the cell the fold asks cannot name
    different kinds, and no verb or kind literal lives at the stamp site. A row's kinds are in exactly
    one of the two sets (the `held_by` test splits them), so `comply`'s dispensation is stamped by its
    addressee test alone and a held petition by the person's holding alone. Empty when no Record row
    asks `held_by`: then the term stamps nothing. Sub-kinds only, as above (v10 REM-2C,
    `_record_subkinds_answered`)."""
    return frozenset(k for row in VERB_TABLE.values() if _asks_subject_held(row)
                     for k in _record_subkinds_answered(row))


HOLDING_RECORD_KINDS = _derive_holding_record_kinds()

# B11 lane A (the duel chain's reach): `{verb: record sub-kinds}` -- per `Record`-classed row, the sub-kinds its own
# cell asks `existence` of on `subject` (`_record_subkinds_answered`, the one owner both derivations above read).
# `decision/options.py::opening_set` keeps a Record referent of such a row only where the person's own content claim
# says it is of one of them: `accept` forms on a challenge, `comply` on a dispensation, never on another kind the
# shared class carries. A row asking only the class (`research`) is absent and forms as before.
RECORD_SUBKINDS_BY_VERB = {v: k for v, row in VERB_TABLE.items() if (k := _record_subkinds_answered(row))}
# ...and of them, the rows whose cell asks the actor to HOLD the document (`carry`, `found`, `build`): a document he holds
# and holds no reading of may be of the kind (clause 4: unknown forms), where a writ row (`accept`, `comply`) asks a
# document addressed to him, which he knows only by reading it.
RECORD_SUBKINDS_HELD = frozenset(v for v in RECORD_SUBKINDS_BY_VERB if _asks_subject_held(VERB_TABLE[v]))


def _derive_declared_classes() -> frozenset:
    """v10 REM-21 (AM-A-06): THE REFERENT CLASSES SOME ROW DECLARES -- every `referent_class:` value in
    the table, read off the rows as `RECORD_REFERENT_KINDS` is, so the own-referent term
    (`queries/world_q.py::own_referents_of_class`) stamps only a class a row forms on and no class
    literal lives at the stamp site. A subset of `rosters.yaml: referent_classes` (the load refuses any
    other); `questions_for` holds back `rosters.yaml: occasion_only_classes` from it."""
    return frozenset(row.referent_class for row in VERB_TABLE.values() if row.referent_class)


DECLARED_CLASSES = _derive_declared_classes()

# v9 IN-12 step 7: `{verb: (record kinds)}` -- the verbs that may ALSO form on what a held writ of one of
# those kinds says (`rosters.yaml: terms_sourced`; `commit` on a covenant dispensation's Proposition).
# REFUSED AT IMPORT, `WARRANT_SOURCED`'s reason: a verb the table lacks, a kind no record term stamps
# (neither `writs_held`'s `RECORD_REFERENT_KINDS` nor a holding row's `HOLDING_RECORD_KINDS`, v10 IN-12 step 5a),
# or a kind whose `subject` no held Record answers would each form for
# nobody, and a stale line must not read as a live route. Read here, beside the set it is checked against.
def _load_terms_sourced(values: dict) -> dict:
    """`rosters.yaml: terms_sourced`'s `values`, checked and frozen -- refused per line (above).

    v10 IN-12 step 5a (H-227 [ASSUMPTION; medium; Jordan to correct; revert: `RECORD_REFERENT_KINDS`
    alone, and `commit: [dispensation]`]): A KIND IS LIVE WHERE EITHER RECORD TERM STAMPS A HELD ONE --
    `RECORD_REFERENT_KINDS` (`writs_held`, the addressee's writ) OR `HOLDING_RECORD_KINDS`
    (`records_held_for_holding_rows`, a document he holds, a petition among them) -- both read off the
    rows, so the union is derived and names no verb. `opening_set`'s reader reads a held document's `terms` only where it is ADDRESSED to the holder
    (`person_q.addressed_to`, `writs_held`'s rule), so a petitioner holding his own petition forms nothing."""
    out = {v: tuple(ks or ()) for v, ks in values.items()}
    live = RECORD_REFERENT_KINDS | HOLDING_RECORD_KINDS
    for v, ks in out.items():
        dead = [k for k in ks if k not in live
                or "subject" not in RECORD_SOURCED_OPERANDS.get(k, {})]
        if v not in VERB_TABLE or not ks or dead:
            raise Forbidden(
                f"`rosters.yaml: terms_sourced` names {v!r}: {list(ks)}, and the verb table carries no "
                f"such verb, the line names no kind, or {dead} is no record kind a term stamps "
                f"(`RECORD_REFERENT_KINDS` or `HOLDING_RECORD_KINDS`) whose `subject` a held Record answers",
                "rosters.yaml",
                needs="a `verb_table.yaml` verb, and record kinds `writs_held` or a holding row stamps and "
                      "`record_sourced_operands` maps `subject` for",
                law="IN-12 step 7 -- a terms-sourced verb forms on what a held writ says, or on nothing new")
    return out


TERMS_SOURCED = _load_terms_sourced(roster_map("terms_sourced", "values"))

# v9 IN-12 step 9: `{verb: operand}` -- the verbs that carry a VOCATION (a skill of `descriptors.CAPABILITIES` the
# actor holds) on the named operand, one Candidate per vocation (`rosters.yaml: vocation_sourced`, read
# in `opening_set`; `train`'s `kind`). REFUSED AT IMPORT, `TERMS_SOURCED`'s reason: a verb the table
# lacks, a verb whose row writes no `Person.capability` (it would carry a vocation nothing raises), or
# an operand outside the closed `requires_operands` would each form a Candidate nobody reads right.
_CAPABILITY_PAIR = "Person.capability"


def _load_vocation_sourced(values: dict) -> dict:
    """`rosters.yaml: vocation_sourced`'s `values`, checked and frozen -- refused per line (above)."""
    out = {v: str(op or "") for v, op in values.items()}
    for v, op in out.items():
        row = VERB_TABLE.get(v)
        if row is None or _CAPABILITY_PAIR not in row.writes or op not in REQUIRES_OPERANDS:
            raise Forbidden(
                f"`rosters.yaml: vocation_sourced` names {v!r}: {op!r}, and the verb table carries no "
                f"such verb, its row writes no `{_CAPABILITY_PAIR}`, or {op!r} is no `requires_operands` "
                "member", "rosters.yaml",
                needs="a `verb_table.yaml` verb that writes `Person.capability`, and a closed operand",
                law="IN-12 step 9 -- a vocation rides an act that raises it, on an operand the grammar names")
    return out


VOCATION_SOURCED = _load_vocation_sourced(roster_map("vocation_sourced", "values"))
# THE VOCATIONS (`VOCATIONS`, derived above): the values of `VERB_CAPABILITY`, the skills a verb's `capability:` names.


# v11 CP-T04-02: `{verb: (key, ...)}` -- the verbs whose Candidate is formed once per COMBINATION of the closed sets the
# named payload keys range over (`rosters.yaml: choice_sourced`, read in `decision/options.py::operand_bags`; `marshal`'s
# `role` and `retreat_at`; CP-T04-06's `march` `posture`), and `CHOICE_RANGES`, each key's closed set. The ranges are pointers
# at the rosters (`order_roles`, `order_retreat_at` -- the mass-battle module's vocabulary -- and `march_postures`), never
# lists spelt here. REFUSED AT IMPORT, `VOCATION_SOURCED`'s reason: a verb the table lacks, a key with no range, or a verb whose
# row writes no `CHOICE_CARRIER` of the key (the order is a minted document, `Record.exists`; a besieged posture's wear is
# written on `Site.condition`) would each carry a choice nothing reads.
SAID_KEY, SAID_RANK_KEY, IN_CONFIDENCE_KEY = "said", "said_rank", "in_confidence"
CHOICE_RANGES = {ORDER_ROLE_KEY: tuple(ORDER_ROLES), ORDER_RETREAT_KEY: tuple(ORDER_RETREAT_AT),
                 MARCH_POSTURE_KEY: tuple(MARCH_POSTURES), IN_CONFIDENCE_KEY: (False, True)}
SITE_KEY = "site"
# v12 B11.74 (R-19-03, FRES §7 (3)): `CITES_KEY` IS A CHOICE WHOSE RANGE IS NOT A ROSTER -- the claim ids and Record ids the utterer HOLDS and cites for what he
# asserts, a pick of held ids (`11_GO_player_surface_contract_B.md` §5), carried on the act's payload under its own name and stored by `_eff_utter` as
# `Proposition.support`. It has no `CHOICE_RANGES` entry (`SAID_KEY`'s shape) and is NOT in `LEDGER_RANGES`: that roster adds referents for a verb to form on
# (`opening_set`), and the held ids are what a CONCLUSION cites, not what `utter` forms on, so no Candidate carries `cites` until typed `utter` (B25,
# `14_VERBS_SOCIAL2_B` §1) forms one from a held claim; `_fanned_choices` never fans it (no closed range), so the shipped season forms what it formed.
CITES_KEY = "cites"
# B24.24 (FI_05_B E-3): `CITED_KEY` IS WHAT THE CITED CLAIMS SAID, `{claim id: Said}`, carried on the act beside `cites` for the told deposit alone -- WITNESS opens no
# citer's ledger (`F8`), so the `Said` of each cited claim is copied out of his own at CHOOSE as `said` is (`person_q.said_of`). A cited Record needs none: its content is
# read off `w.records`. Read by `loop/witness.py::_told_items`; bound by no cell, dropped by `binding_of`, and not a choice (no `CHOICE_RANGES`/`CHOICE_CARRIER` entry).
CITED_KEY = "cited"
# B24.25 (EVID_B rules 1-2): `ANSWERS_KEY` IS THE FILED STAGES AN ACT ANSWERS, a tuple of their places on the case file (`Record.stages` indexes, the number an exhibit's id ends in), carried beside
# `cites`. The act's own band is the `answered_band` of each (`queries/inputs.py::ANSWERED_STAGE`). Read by `queries/world_q.py::filings`; bound by no cell and not a choice (as `CITED_KEY`).
ANSWERS_KEY = "answers"
CHOICE_CARRIER = {ORDER_ROLE_KEY: "Record.exists", ORDER_RETREAT_KEY: "Record.exists", MARCH_POSTURE_KEY: "Site.condition",
                  SAID_KEY: "news.told", IN_CONFIDENCE_KEY: "news.told", SITE_KEY: "finding.made", CITES_KEY: "Proposition.exists",
                  CONCLUDED_KEY: CONCLUSION_KIND}
# v12 B11.72 (`08_FI_07` §2 (a)): `SITE_KEY` IS A CHOICE WHOSE RANGE IS THE ACTOR'S OWN LEDGER -- the ids his claims present as a Site
# (`rosters.yaml: choice_sourced`'s `ledger_ranges`, read by `queries/person_q.py::ledger_range`), so it has no `CHOICE_RANGES` entry (`SAID_KEY`'s
# shape). The carrier is the kind the look emits (`finding.made`), as a telling's is its deposit.
def _check_ledger_ranges(ranges: dict, event_kinds, look_reads, classes) -> dict:
    """`rosters.yaml: choice_sourced`'s `ledger_ranges`, checked and frozen: each KEY is a choice carrier (`CHOICE_CARRIER`) and each PREDICATE is a form a
    held claim can carry -- an Event kind (`EVENT_KINDS`), a `look_reads` member (the observation a look deposits), or `exists:<class>` over a class the write
    matrix declares. A key no verb carries, or a predicate no claim is ever held under, would range over an empty ledger forever and read as built; a function,
    so a test can plant each refusal."""
    out = {k: tuple(ps or ()) for k, ps in ranges.items()}
    bad = {k: [x for x in ps if not (x in event_kinds or x in look_reads or (x.startswith("exists:") and x[len("exists:"):] in classes))]
           for k, ps in out.items()}
    bad = {k: v for k, v in bad.items() if v or not out[k]}
    nokey = sorted(k for k in out if k not in CHOICE_CARRIER)
    if nokey or bad:
        raise Forbidden(
            f"`rosters.yaml: choice_sourced` `ledger_ranges` names keys {nokey} outside `CHOICE_CARRIER`, or predicates {bad} that are no Event kind, `look_reads` "
            f"member or `exists:<class>` (an empty list is refused too)",
            "rosters.yaml -- choice_sourced.ledger_ranges",
            needs="a key `CHOICE_CARRIER` carries, over predicates a held claim can carry",
            law="v12 B11.72 -- a ledger-sourced range is the subjects of the actor's own claims under these predicates; one no claim carries ranges over nothing")
    return out


LEDGER_RANGES = _check_ledger_ranges(roster_map("choice_sourced", "ledger_ranges"), EVENT_KINDS, LOOK_READS, {c for c, _ in MATRIX})
# v12 B11.10 (`08_FI_02` edits 7-8): `SAID_KEY` IS A CHOICE WHOSE RANGE IS NOT A ROSTER -- the top `Fixtures.said_choices` claims `said_of`'s slant ranks for the
# subject (`queries/person_q.py::said_set`), so it has no `CHOICE_RANGES` entry; it rides the payload as it always did, and counts as chosen only where the
# fan held several (`SAID_RANK_KEY`, `choice_values`). A telling writes nothing, so the carrier of its two keys is the kind its deposit is (`loop/witness.py`'s
# `news.told` branch reads `said`, `_circle_of` reads `in_confidence`): the row must emit it.


def _load_choice_sourced(values: dict) -> dict:
    """`rosters.yaml: choice_sourced`'s `values`, checked and frozen -- refused per line (above)."""
    out = {v: tuple(ks or ()) for v, ks in values.items()}
    for v, ks in out.items():
        row = VERB_TABLE.get(v)
        if row is None or not ks or any(k not in CHOICE_CARRIER or (k not in CHOICE_RANGES and k not in (SAID_KEY, CITES_KEY, CONCLUDED_KEY) and k not in LEDGER_RANGES)
                                        or CHOICE_CARRIER[k] not in (*row.writes, *row.emits) for k in ks):
            raise Forbidden(
                f"`rosters.yaml: choice_sourced` names {v!r}: {list(ks)}, and the verb table carries no such verb, "
                f"its row writes or emits no carrier of a key (`CHOICE_CARRIER`), or the line names a key outside {sorted(CHOICE_CARRIER)}",
                "rosters.yaml",
                needs="a `verb_table.yaml` verb that writes or emits each key's carrier, and keys `CHOICE_CARRIER` carries",
                law="CP-T04-02 -- a choice rides an act that writes what the choice is read from, over a closed set")
    return out


CHOICE_SOURCED = _load_choice_sourced(roster_map("choice_sourced", "values"))


def choice_values(verb: str, ops) -> tuple:
    """`(key, value)` for each CHOICE VALUE the operands `ops` carry for `verb` (`rosters.yaml: choice_sourced`, in its order): the one reader, for `act_key`'s
    suffix and the chooser's score (`decision/choose.py::chosen_values`). `said` is a choice only where `opening_set` fanned it over several claims, and
    its value is then the claim's RANK (`SAID_RANK_KEY`, 0 for the claim `said_of` ranks first), never the `Said`: with one claim to say there is nothing
    to choose among, and riding the lone claim on every act would rename every telling (`_fanned_choices`'s reason for a one-member range).
    `concluded` (B11.75) is a choice the same way: its value is the variant's place among the doers his ledger names (`CONCLUDED_RANK_KEY`), absent for one doer."""
    ops = ops if isinstance(ops, dict) else {}
    out = []
    for k in CHOICE_SOURCED.get(verb, ()):
        v = ops.get(SAID_RANK_KEY) if k == SAID_KEY else ops.get(CONCLUDED_RANK_KEY) if k == CONCLUDED_KEY else ops.get(k)
        if v is not None:
            out.append((k, v))
    return tuple(out)


# B24p.24: THE VERBS THAT CARRY A `rig` (`rosters.yaml: rigged_verbs`, read in `decision/options.py::opening_set`). REFUSED AT IMPORT for a verb the
# table lacks: an offer on a verb nothing performs would be a rig no effect writes.
RIGGED_VERBS = frozenset(roster("rigged_verbs"))
if not RIGGED_VERBS <= VERB_TABLE.keys():
    raise Forbidden(
        f"`rosters.yaml: rigged_verbs` names {sorted(RIGGED_VERBS - VERB_TABLE.keys())}, which the verb table lacks", "rosters.yaml",
        needs="`verb_table.yaml` verbs whose effects read `rig`", law="B24p.24 -- a rig rides an act that writes the arrangement it sets")


# v9 IN-12 step 10: `{verb: record kind}` -- the verbs a person does not form while he holds a document
# of that kind whose content names him (`rosters.yaml: held_document_declines`, read in `opening_set`;
# `conceal` while a cover is held). REFUSED AT IMPORT, `TERMS_SOURCED`'s reason: a verb the table lacks
# or a kind `record_kinds` does not carry would decline for nobody, and a stale line must not read as a
# live decline.
def _load_held_document_declines(values: dict) -> dict:
    """`rosters.yaml: held_document_declines`' `values`, checked and frozen -- refused per line (above)."""
    out = {v: str(k or "") for v, k in values.items()}
    for v, k in out.items():
        if v not in VERB_TABLE or k not in RECORD_KINDS:
            raise Forbidden(
                f"`rosters.yaml: held_document_declines` names {v!r}: {k!r}, and the verb table carries no "
                f"such verb, or {k!r} is no `record_kinds` member ({sorted(RECORD_KINDS)})", "rosters.yaml",
                needs="a `verb_table.yaml` verb, and a record kind a held document can be",
                law="IN-12 step 10 -- a person-side decline reads a document he holds, of a kind that exists")
    return out


HELD_DOCUMENT_DECLINES = _load_held_document_declines(roster_map("held_document_declines", "values"))


# B21.55 (`14_VERBS_BINDING_D` commit D2, A-22): the UNTYPED verbs whose `subject` is a person the seat must command
# (`rosters.yaml: command_declines`, read in `decision/options.py::operand_bags` through `VerbRow.commanded_operand`;
# `dispatch`). REFUSED AT IMPORT when a member names a verb the table lacks, one whose row is TYPED (its cell's `basis`
# conjunct is the one owner of whom it orders) or one whose referent class is not `Person` (the subject is the man ordered).
def _load_command_declines(values) -> frozenset:
    """`rosters.yaml: command_declines`' `values`, checked and frozen -- refused per member (above)."""
    out = frozenset(str(v or "") for v in (values or ()))
    for v in sorted(out):
        row = VERB_TABLE.get(v)
        if row is None or row.requires_typed is not None or row.referent_class != "Person":
            raise Forbidden(
                f"`rosters.yaml: command_declines` names {v!r}, and the verb table carries no such verb, or its row is typed "
                "or forms on no `Person` referent", "rosters.yaml",
                needs="an untyped `verb_table.yaml` verb with `referent_class: Person`, whose subject is the man it orders",
                law="B21.55 -- a typed row's `basis: command` conjunct says whom it orders; an untyped row's subject is the person")
    return out


COMMAND_DECLINES = _load_command_declines(roster("command_declines"))


# B21.57 (`IS-B3-FA-05`, A-24): the verbs whose WRITING ROW MAY LAWFULLY WRITE NOTHING, and the kinds each emits when it does
# (`rosters.yaml: write_optional`, read in `loop/resolve.py::_fold`'s `NoOpReceipt` branch; `comply`). REFUSED AT IMPORT when a
# member names a verb the table lacks, a row that writes nothing (no write to decline) or a kind the row does not emit.
def _load_write_optional(values: dict) -> dict:
    """`rosters.yaml: write_optional`'s `values`, checked and frozen -- refused per member (above). A function, so a test can plant
    a bad line and watch it refuse."""
    out: dict = {}
    for verb, kinds in (values or {}).items():
        row = VERB_TABLE.get(verb)
        kinds = tuple(kinds) if isinstance(kinds, (list, tuple)) else ()
        if row is None or not row.writes or not kinds or not set(kinds) <= set(row.emits):
            raise Forbidden(
                f"`rosters.yaml: write_optional` names {verb!r}: {list(kinds)}, and the verb table carries no such verb, its row "
                "writes nothing, or it lists a kind the row does not emit", "rosters.yaml",
                needs="a writing `verb_table.yaml` verb and a non-empty list of kinds its `emits:` declares",
                law="B21.57 -- a decline is the row's refusal (F9) unless the roster says the verb is also answered without a write")
        out[verb] = kinds
    return out


WRITE_OPTIONAL = _load_write_optional(roster_map("write_optional", "values"))


# B24.25 (EVID_B edit 4, ADM edit 3): THE VERBS THAT FILE WHAT THEY CITE (`rosters.yaml: filing_verbs`, read in `loop/resolve.py::_admits`; `speak`). REFUSED AT IMPORT when a member
# names a verb the table lacks or one whose row writes no `Record.stages`: a refusal for cites that no stage the verb writes could carry would guard nothing.
def _load_filing_verbs(values) -> frozenset:
    """`rosters.yaml: filing_verbs`' `values`, checked and frozen -- refused per member (above). A function, so a test can plant a bad line and watch it refuse."""
    out = frozenset(str(v or "") for v in (values or ()))
    for v in sorted(out):
        row = VERB_TABLE.get(v)
        if row is None or "Record.stages" not in row.writes:
            raise Forbidden(
                f"`rosters.yaml: filing_verbs` names {v!r}, and the verb table carries no such verb or its row writes no `Record.stages`", "rosters.yaml",
                needs="a `verb_table.yaml` verb whose row writes `Record.stages` (the case file a filing is written on)",
                law="B24.25 -- an item is filed on the case file by the speech that cites it; a row that writes no stage files nothing")
    return out


FILING_VERBS = _load_filing_verbs(roster("filing_verbs"))


# v9 IN-12 step 13: the verbs a person forms only on a referent he holds a row against -- his own
# `Person.stance` rows naming it with a valence below zero (`rosters.yaml: own_stance_declines`, read in
# `opening_set`; `forgive`). Keyed on the row's `writes:`: REFUSED AT IMPORT when a member names a verb the
# table lacks or one whose row writes no `Person.stance` -- a decline on a field the act does not end would
# narrow its formation by a fact its effect never reads.
_STANCE_PAIR = "Person.stance"


def _load_own_stance_declines(values) -> frozenset:
    """`rosters.yaml: own_stance_declines`' `values`, checked and frozen -- refused per member (above)."""
    out = frozenset(str(v or "") for v in (values or ()))
    for v in sorted(out):
        row = VERB_TABLE.get(v)
        if row is None or _STANCE_PAIR not in row.writes:
            raise Forbidden(
                f"`rosters.yaml: own_stance_declines` names {v!r}, and the verb table carries no such verb "
                f"or its row writes no `{_STANCE_PAIR}`", "rosters.yaml",
                needs="a `verb_table.yaml` verb whose row writes `Person.stance`",
                law="IN-12 step 13 -- an own-state decline reads the field the act ends")
    return out


OWN_STANCE_DECLINES = _load_own_stance_declines(roster("own_stance_declines"))


# v11 CR-27 (M9 taken (a)): the verbs that say a FALSE value of a claim the speaker holds
# (`rosters.yaml: lie_verbs`, read in `opening_set`; `lie`). Refused at import when a member names a verb the
# table lacks or one whose typed cell names no `own_ledger` conjunct -- `opening_set` carries `said` only off
# that conjunct, so a listed row without one would be a roster line nothing reads.
def _load_lie_verbs(values) -> frozenset:
    """`rosters.yaml: lie_verbs`' `values`, checked and frozen -- refused per member (above)."""
    out = frozenset(str(v or "") for v in (values or ()))
    for v in sorted(out):
        row = VERB_TABLE.get(v)
        if row is None or row.requires_typed is None or not row.requires_typed.named_own_ledger_operands():
            raise Forbidden(
                f"`rosters.yaml: lie_verbs` names {v!r}, and the verb table carries no such verb or its typed "
                "cell names no `own_ledger` conjunct", "rosters.yaml",
                needs="a `verb_table.yaml` verb whose cell names an `own_ledger` conjunct (`tell`'s `holds`)",
                law="CR-27 -- a lie is a said claim made false; a row that says nothing has none")
    return out


LIE_VERBS = _load_lie_verbs(roster("lie_verbs"))


# v10 IN-61 (RS-27): the verbs a person forms only on a seat whose `successions` title he himself holds
# (`rosters.yaml: own_title_declines`, read in `opening_set`; `succeed`). `own_stance_declines`' shape one read
# over, REFUSED AT IMPORT when a member names a verb the table lacks or one whose row declares no
# `referent_class: Office` -- a title is a seat's, so a row forming on anything but a seat has no title.
_TITLE_CLASS = "Office"


def _load_own_title_declines(values) -> frozenset:
    """`rosters.yaml: own_title_declines`' `values`, checked and frozen -- refused per member (above)."""
    out = frozenset(str(v or "") for v in (values or ()))
    for v in sorted(out):
        row = VERB_TABLE.get(v)
        if row is None or row.referent_class != _TITLE_CLASS:
            raise Forbidden(
                f"`rosters.yaml: own_title_declines` names {v!r}, and the verb table carries no such verb "
                f"or its row declares no `referent_class: {_TITLE_CLASS}`", "rosters.yaml",
                needs=f"a `verb_table.yaml` verb formed on `{_TITLE_CLASS}` referents",
                law="IN-61 -- an own-title decline reads the title a seat passes to")
    return out


OWN_TITLE_DECLINES = _load_own_title_declines(roster("own_title_declines"))


# VB-A commit A1 (B21.07): `{verb: the Tenure kinds its row's `domain:` names}` -- the verbs a person forms only on a referent
# he is tied to by a live edge of such a kind (`rosters.yaml: own_edge_declines`, read in `opening_set`; `release`).
# `own_title_declines`' shape one carrier over. REFUSED AT IMPORT when a member names a verb the table lacks, one that is
# not `own`-eligible (an edge a person ends is his own act's), or one with no `domain:` (no kind to read the edges against).
def _load_own_edge_declines(values) -> dict:
    """`rosters.yaml: own_edge_declines`' `values`, as `{verb: frozenset(row.domain)}` -- refused per member (above)."""
    out: dict = {}
    for v in sorted(str(v or "") for v in (values or ())):
        row = VERB_TABLE.get(v)
        if row is None or "own" not in row.eligibility or not row.domain:
            raise Forbidden(
                f"`rosters.yaml: own_edge_declines` names {v!r}, and the verb table carries no such verb, or its row is "
                "not `own`-eligible, or it declares no `domain:`", "rosters.yaml",
                needs="a `verb_table.yaml` verb with `eligibility: [own]` and a `domain:` of Tenure kinds",
                law="VB-A -- an own-edge decline reads the kinds the row's own `domain:` names")
        out[v] = frozenset(row.domain)
    return out


OWN_EDGE_DECLINES = _load_own_edge_declines(roster("own_edge_declines"))


# VRES §4 (A-37): `{verb: the Event kind its disposal edge earns}` -- the verbs whose edge a party does not release
# (`rosters.yaml: own_edge_declines: disposal`; `determine` -> `matter.determined`). The fold's half
# (`loop/predicates.py::_req_release`) reads the VERB through `causing_act`, the formation half (`opening_set`) reads the KIND off
# the person's own ledger. REFUSED AT IMPORT for a verb the table lacks or a kind its row does not emit: a stale pair would
# decline for nobody, and must not read as a live decline.
def _load_disposal_events(values: dict) -> dict:
    """`rosters.yaml: own_edge_declines: disposal`, checked and frozen -- refused per line (above)."""
    out = {str(v): str(k or "") for v, k in (values or {}).items()}
    for v, k in out.items():
        row = VERB_TABLE.get(v)
        if row is None or k not in row.emits:
            raise Forbidden(
                f"`rosters.yaml: own_edge_declines: disposal` names {v!r}: {k!r}, and the verb table carries no such verb, "
                f"or its row does not emit {k!r}", "rosters.yaml",
                needs="a `verb_table.yaml` verb, and an Event kind its `emits:` declares",
                law="A-37 -- a party does not release an edge a bench imposed; the kind is the claim the bench's finding earns")
    return out


DISPOSAL_EVENTS = _load_disposal_events(roster_map("own_edge_declines", "disposal"))


# B10-09 close one, D3: `{verb: tenure kind}` -- the verbs a person does not form on an object he already
# holds a LIVE Tenure of that kind on (`rosters.yaml: held_edge_declines`, read in `opening_set`; `commit` on a
# Proposition he commits to). `held_document_declines`' shape, one carrier over. REFUSED AT IMPORT, its reason:
# a verb the table lacks or a kind `tenure_kinds` does not carry would decline for nobody, and a stale line
# must not read as a live decline.
def _load_held_edge_declines(values: dict) -> dict:
    """`rosters.yaml: held_edge_declines`' `values`, checked and frozen -- refused per line (above)."""
    out = {v: str(k or "") for v, k in (values or {}).items()}
    for v, k in out.items():
        if v not in VERB_TABLE or k not in TENURE_KINDS:
            raise Forbidden(
                f"`rosters.yaml: held_edge_declines` names {v!r}: {k!r}, and the verb table carries no "
                f"such verb, or {k!r} is no `tenure_kinds` member ({sorted(TENURE_KINDS)})", "rosters.yaml",
                needs="a `verb_table.yaml` verb, and a Tenure kind an edge can be",
                law="B10-09 -- a person-side decline reads a live edge he holds, of a kind that exists")
    return out


HELD_EDGE_DECLINES = _load_held_edge_declines(roster_map("held_edge_declines", "values"))


# B10.72: `{verb: tenure kind}` -- the verbs that ALSO form on the object of a live Tenure of that kind the person holds
# (`rosters.yaml: held_edge_sourced`, read in `opening_set`; `release` on a `commit` he holds). `held_edge_declines`' shape
# and loader rule, its mirror. REFUSED AT IMPORT for a verb the table lacks or a kind `tenure_kinds` does not carry: either
# would form for nobody, and a stale line must not read as a live route.
def _load_held_edge_sourced(values: dict) -> dict:
    """`rosters.yaml: held_edge_sourced`' `values`, checked and frozen -- refused per line (above)."""
    out = {v: str(k or "") for v, k in (values or {}).items()}
    for v, k in out.items():
        if v not in VERB_TABLE or k not in TENURE_KINDS:
            raise Forbidden(
                f"`rosters.yaml: held_edge_sourced` names {v!r}: {k!r}, and the verb table carries no "
                f"such verb, or {k!r} is no `tenure_kinds` member ({sorted(TENURE_KINDS)})", "rosters.yaml",
                needs="a `verb_table.yaml` verb, and a Tenure kind an edge can be",
                law="B10.72 -- a verb sourced from a held edge forms on the object of an edge of a kind that exists")
    return out


HELD_EDGE_SOURCED = _load_held_edge_sourced(roster_map("held_edge_sourced", "values"))


# v11 CR-87 (ED-IN-0337): `{verb: (context, ...)}` -- the verbs a person forms only on a subject he holds a context
# of violence against (`rosters.yaml: violence_contexts`, read in `opening_set`; `fight`). `held_edge_declines`'
# shape, a list of contexts per verb. REFUSED AT IMPORT for a verb the table lacks or a context list that is not a
# non-empty list of names; WHICH names are contexts is the readers' (`decision/options.py::VIOLENCE_CONTEXT_READERS`,
# which refuses a name it cannot read, and a row whose subject is not its opponent, at its own import).
def _load_violence_contexts(values: dict) -> dict:
    """`rosters.yaml: violence_contexts`' `values`, checked and frozen -- refused per line (above)."""
    out = {}
    for v, ctx in (values or {}).items():
        if (v not in VERB_TABLE or not isinstance(ctx, list) or not ctx
                or not all(isinstance(c, str) and c for c in ctx)):
            raise Forbidden(
                f"`rosters.yaml: violence_contexts` names {v!r}: {ctx!r}, and either the verb table carries no "
                "such verb or the contexts are not a non-empty list of names", "rosters.yaml",
                needs="a `verb_table.yaml` verb and a list of context names",
                law="CR-87 -- a violence decline reads a context the actor holds against the subject")
        out[v] = tuple(dict.fromkeys(ctx))
    return out


VIOLENCE_CONTEXTS = _load_violence_contexts(roster_map("violence_contexts", "values"))


# v11 CR-87: THE VIOLENT ROWS -- every row whose `contests:` prize `rosters.yaml: violent_prizes` lists (`the body`:
# `fight`, `capture`, `accept`), derived off the table, no verb named. `decision/choose.py::stance_term` bounds a
# grudge's pull on them (`Fixtures hostile_stance_gain`). Refused at import for a member that is no prize.
def _derive_violent_verbs(prizes) -> frozenset:
    """The rows contesting a listed prize; refused at import if a member is no `contest_subsystems` prize."""
    prizes = frozenset(prizes or ())
    if not prizes <= _CONTEST_PRIZES:
        raise Forbidden(
            f"`rosters.yaml: violent_prizes` names {sorted(prizes - _CONTEST_PRIZES)}, no `contest_subsystems` "
            "prize", "rosters.yaml", needs=f"a prize of {sorted(_CONTEST_PRIZES)}",
            law="CR-87 -- a violent row is one contesting a listed prize")
    return frozenset(v for v, r in VERB_TABLE.items() if r.contests in prizes)


VIOLENT_VERBS = _derive_violent_verbs(roster("violent_prizes"))


# B10.31: THE PRIZES THE ACTOR HIMSELF STAKES IN BODY OR FIELD (`rosters.yaml: bodily_prizes`); `decision/choose.py::score_terms`' `risk` prices a
# candidate whose row's `contests:` is one of them. Closed against the `contests:` values the verb table declares, so a prize no row contests
# (a renamed one) refuses here and cannot leave the term reading nobody.
def _load_bodily_prizes(prizes) -> frozenset:
    """The `bodily_prizes` roster, refused at import if a member is no prize any verb row contests."""
    prizes = frozenset(prizes or ())
    declared = frozenset(r.contests for r in VERB_TABLE.values() if r.contests)
    if not prizes or not prizes <= declared:
        raise Forbidden(
            f"`rosters.yaml: bodily_prizes` names {sorted(prizes - declared)}, no `contests:` value a verb row declares"
            if prizes else "`rosters.yaml: bodily_prizes` is empty", "rosters.yaml",
            needs=f"a prize of {sorted(declared)}",
            law="B10.31 -- an exposed candidate is one whose row contests a listed prize")
    return prizes


BODILY_PRIZES = _load_bodily_prizes(roster("bodily_prizes"))


def _load_opposed_without_prize(values) -> frozenset:
    """`rosters.yaml: opposed_without_prize` (B11 lane A): verbs naming no prize whose second side is their subject,
    read as done against him. Refused at import for a verb the table lacks or whose second side is not `subject`."""
    out = frozenset(values or ())
    bad = sorted(v for v in out if v not in VERB_TABLE or VERB_TABLE[v].opponent_operand() != "subject")
    if bad:
        raise Forbidden(f"`rosters.yaml: opposed_without_prize` names {bad}: no such verb, or its second side is not "
                        "its subject", "rosters.yaml", needs="a verb whose `counterparty:` is `subject`",
                        law="B11 lane A -- an act against its subject names him as its second side")
    return out


OPPOSED_WITHOUT_PRIZE = _load_opposed_without_prize(roster("opposed_without_prize"))

def social_roll_verbs() -> frozenset:
    """THE VERBS THE SOCIAL ROLL DEALS: the rows `social_rolled` says it deals (a `contests:` prize the `social_contest`
    provider resolves, a `graded_tasks` route to it). Read off the rows and the two rosters, no verb named."""
    prizes = _PRIZES
    return frozenset(v for v, r in VERB_TABLE.items() if social_rolled(v, r, prizes))


def _derive_rung_remit_acts() -> frozenset:
    """v9 IN-49 `requisition` (H-163 limit 3, [ASSUMPTION; medium; Jordan to correct]): THE REMIT ACTS A
    SEAT EXERCISES ON A `Rung`-CLASSED REFERENT -- the act of every `remit:` eligibility alternative
    on a row declaring `referent_class: Rung` (`requisition`: `issue`, `H-52`'s substitution, carried and not
    decided here). Read off the rows, `RECORD_REFERENT_KINDS`' shape one class over, so the stamp
    (`queries/world_q.py::larders_in_purview`, which offers a larder only to a holder of a seat
    granting one of these) and the fold's eligibility cannot name different acts, and no act literal
    lives at the stamp site. Empty when no `Rung` row is exercised through a seat (`migrate` is
    `own`): then nothing is stamped.
    THE DERIVED WIDENING, NAMED (v10 REM-27, REM-28; B10-06): the set is the UNION over every `Rung`-classed
    row, so a row that gains `referent_class: Rung` (`march`, `convene`) widens it and `larders_in_purview` is
    asked of that row's remit holders too, whatever `requisition` itself is eligible on. Its current value is
    pinned in `tests/test_referent_class_stamps.py`; each widening's measurement is in that row's
    `referent_class_note:`."""
    return _remit_acts_of_class("Rung")


def _remit_acts_of_class(cls: str) -> frozenset:
    """The act of every `remit:` eligibility alternative on a row declaring `referent_class: <cls>` --
    the ONE reading `RUNG_REMIT_ACTS` and `DETAINEE_REMIT_ACTS` are both taken by (v10 IN-12)."""
    return frozenset(act for row in VERB_TABLE.values() if row.referent_class == cls
                     for act in _remit_acts_of(row))


def _remit_acts_of(row: "VerbRow") -> frozenset:
    """The act of every `remit:` eligibility alternative on ONE row -- `_remit_acts_of_class`'s per-row read,
    which `FOUNDING_REMIT_ACTS` (below) takes too, never a second parse."""
    return frozenset(raw.strip() for kind, _, raw in (alt.partition(":") for alt in row.eligibility)
                     if kind.strip() == "remit" and raw.strip())


RUNG_REMIT_ACTS = _derive_rung_remit_acts()

# v10 IN-12 step 5 (H-226 route (a), the decline by H-232's shape [ASSUMPTION; medium; Jordan to correct;
# revert: `interrogate` back to `referent_class: Person`, which forms on every person a question names]):
# THE RESTRAINED-PERSONS CLASS. Not a collection, so `World.class_of` never answers it and only the
# standing occasion `queries/world_q.py::detainees_held` stamps it, naming it explicitly; refused at import
# off `rosters.yaml: referent_classes`, so a stamp of it can never be a class nobody declared.
DETAINEE_CLASS = "Detainee"
if DETAINEE_CLASS not in REFERENT_CLASSES:
    raise Forbidden(f"{DETAINEE_CLASS!r} is not a `rosters.yaml: referent_classes` value", "rosters.yaml",
                    needs="the restrained-persons class in the closed roster",
                    law="v10 IN-12 -- a class stamped by name must be one the roster declares")
# The remit acts a seat exercises on a `Detainee`: the union over the rows declaring the class
# (`interrogate`: `determine`), so the stamp offers a prisoner only to a holder of a seat granting one.
DETAINEE_REMIT_ACTS = _remit_acts_of_class(DETAINEE_CLASS)

# v11 CR-87 (the WAR context of `rosters.yaml: violence_contexts`): A PERSON OF A FACTION AT WAR WITH THE ASKER'S,
# `Detainee`'s shape -- no collection, stamped by name by the standing occasion `queries/world_q.py::enemies_heard`,
# and refused at import off `rosters.yaml: referent_classes`. No row declares it; the `fight` decline reads it.
ENEMY_CLASS = "Enemy"
if ENEMY_CLASS not in REFERENT_CLASSES:
    raise Forbidden(f"{ENEMY_CLASS!r} is not a `rosters.yaml: referent_classes` value", "rosters.yaml",
                    needs="the war-context class in the closed roster",
                    law="v11 CR-87 -- a class stamped by name must be one the roster declares")

# v11 CR-56 (reasons-to-convene RL1 [ASSUMPTION; medium; Jordan to correct; revert: drop with
# `queries/world_q.py::matters_awaiting`]): THE REMIT ACTS A SEAT CONVENES A SITTING THROUGH -- the `remit:`
# alternatives of every row that writes a Date's `due_at` (`convene`'s, today `convene`), read off the rows'
# `writes:` as `DOCKETING_KINDS` is, so `matters_awaiting` offers a tier only to a holder of a seat the fold's
# eligibility would admit, and no act literal lives at the stamp site. Refused at import if empty: the stamp would
# otherwise offer nothing for ever and read as an honest absence.
CONVENING_REMIT_ACTS = frozenset(act for row in VERB_TABLE.values() if "Date.due_at" in row.writes
                                 for act in _remit_acts_of(row))
if not CONVENING_REMIT_ACTS:
    raise Forbidden("no verb-table row granted by a remit act writes `Date.due_at`", "verb_table.yaml",
                    needs="the convening row's `writes:` and `remit:` eligibility, or `matters_awaiting` retired",
                    law="v11 CR-56 -- a stamp keyed on an act no row grants offers nothing in every world")

# B11 lane A (the duel chain's second link, [ASSUMPTION; medium; Jordan to correct; revert: drop the value and the
# stamp, `challenge` declares `Person`]): A PERSON BESIDE THE ASKER WHOM HE HOLDS A DISPUTE WITH, `Enemy`'s shape -- no
# collection, stamped by name by the standing occasion `queries/world_q.py::disputes_held`, refused at import off
# `rosters.yaml: referent_classes`. `challenge` declares it.
DISPUTANT_CLASS = "Disputant"
if DISPUTANT_CLASS not in REFERENT_CLASSES:
    raise Forbidden(f"{DISPUTANT_CLASS!r} is not a `rosters.yaml: referent_classes` value", "rosters.yaml",
                    needs="the dispute-context class in the closed roster",
                    law="B11 lane A -- a class stamped by name must be one the roster declares")

# B21.08 (VB-A commit A2 [ASSUMPTION; medium; Jordan to correct; revert: `establish`'s `referent_class: Rung`, drop the
# value and the `Holding` term in `queries/world_q.py::questions_for`]): THE UNFOUNDED HOLDING, `Detainee`'s shape -- no
# collection, stamped by name by the standing occasion `queries/world_q.py::holdings_to_found` (through `questions_for`), and
# refused at import off `rosters.yaml: referent_classes`. `establish` declares it.
HOLDING_CLASS = "Holding"
if HOLDING_CLASS not in REFERENT_CLASSES:
    raise Forbidden(f"{HOLDING_CLASS!r} is not a `rosters.yaml: referent_classes` value", "rosters.yaml",
                    needs="the founding-holding class in the closed roster",
                    law="B21.08 -- a class stamped by name must be one the roster declares")

# v11 CR-25 ([ASSUMPTION; medium; Jordan to correct; revert: drop `holdings_to_found` and the derivation]): THE
# REMIT ACTS A SEAT FOUNDS AN OFFICE THROUGH -- `establish`'s own `remit:` alternatives (`confer` today), read off
# the row, so the founding stamp (`queries/world_q.py::holdings_to_found`) offers a holding only to a holder of a
# seat the fold's eligibility would admit, and no act literal lives at the stamp site. `RUNG_REMIT_ACTS` (the
# union over the `Rung` rows) is NOT this set: it carries `issue` and `convene`, through which no `establish` is
# eligible.
FOUNDING_REMIT_ACTS = _remit_acts_of(VERB_TABLE["establish"])

# An authored alignment cell for an EVENT KIND rather than a verb is keyed `deed:<kind>` in the same
# axis row. Admitted only where `<kind>` is in `EMITTED_KINDS` (`_load_alignment`): a deed key for a
# kind no verb emits is a weight on an event nobody can see. The authored ones are the `deed:` keys of
# `rosters.yaml: tables.alignment` (a list here would be a second copy).
DEED_PREFIX = "deed:"
# B10.56 (`02_CHAR_choice_alignment` edits 1-2): an authored alignment cell for a CHOICE VALUE (`retreat_at` `early`, not the verb
# `marshal`) is keyed `choice:<key>=<value>` in the same axis row, so `ALIGNMENT` stays the ONE binding the `H-66` sweep rebinds and
# `align_choice` reads it where `align` does. The authored ones are `rosters.yaml: tables.alignment`'s optional `choices:` block (absent is
# the shipped state; the cells are content for `BA1-cast-content`), read by `_load_alignment` and refused by `_check_choice_cells`.
CHOICE_PREFIX = "choice:"


_DENSITY_LAW = ("IN-08 (`workplans/valoria_master_workplan_v9_part5.md`) -- every table verb carries "
                "a cell on each axis, or is listed in the declared `uncelled:` set with its reason; "
                "a verb nobody considered is not the same claim as a verb considered and left at "
                "zero, and only the first is refused")


def _check_alignment_density(cells: dict, uncelled: dict) -> None:
    """IN-08's DENSITY RULE, at load: each `VERB_TABLE` verb is either keyed on EVERY axis row
    (a number, or an explicit `null` -- "considered; no source, no lean") or named in `uncelled:`
    with a reason, and then keyed on NO axis.

    ⚠ `_check_sparse_table` does not check that all cells are present, which is right for the
    VALUES -- sparse is lawful. What it would let through silently is a NEW VERB ROW that nobody
    celled: it scores 0.0 on every axis, which reads exactly like a verb considered and judged
    neutral. Every verb row lands its cells or its `uncelled:` line, or this refuses, naming the
    verb and the axes it is missing."""
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


def _check_choice_cells(choices: Optional[dict]) -> dict:
    """`tables.alignment.choices`, `{key: {value: {axis: cell}}}`, checked and returned as axis rows `{axis: {choice:<key>=<value>: cell}}`.
    Refused at load, each for a cell nothing would read: a key no verb's `choice_sourced` line carries (no candidate holds it in its
    operands), a value outside that key's `CHOICE_RANGES` (no candidate holds it), an axis off the roster (`axis_weight` never reaches it)
    and a cell that is not a number. No value is required to carry a cell: a value the block does not name scores as the table's default.
    A value is spelt as `CHOICE_RANGES` spells it (`retreat_at`'s `0.5` is quoted in the YAML, and compared as the string it is)."""
    sourced = {k for ks in CHOICE_SOURCED.values() for k in ks if k in CHOICE_RANGES}   # `said` ranges over no roster: it is scored by the claim's own valence
    law = ("B10.56 / `02_CHAR_choice_alignment` -- a choice cell scores a value a candidate's operands can carry, on a rostered axis; "
           "a cell nothing reads is never reported")
    out: dict = {}
    for key, values in (choices or {}).items():
        if key not in sourced or not isinstance(values, dict):
            raise Forbidden(f"alignment `choices:` names {key!r}, which no `choice_sourced` line carries (keys: {sorted(sourced)})",
                            "rosters.yaml", needs="a key a verb's `choice_sourced` line names, with `{value: {axis: cell}}` under it", law=law)
        for value, row in values.items():
            if str(value) not in {str(v) for v in CHOICE_RANGES[key]}:
                raise Forbidden(f"alignment `choices:` {key!r} names value {value!r}, outside its range {list(CHOICE_RANGES[key])}",
                                "rosters.yaml", needs="a value of the key's closed set (`data/verbs.py::CHOICE_RANGES`)", law=law)
            for ax, cell in (row or {}).items():
                if ax not in PURSUIT_AXES or isinstance(cell, bool) or not isinstance(cell, (int, float)):
                    raise Forbidden(f"alignment `choices:` {key!r}={value!r} cells {ax!r}: {cell!r}, not a number on a rostered axis",
                                    "rosters.yaml", needs=f"a number on one of {sorted(PURSUIT_AXES)}", law=law)
                out.setdefault(ax, {})[f"{CHOICE_PREFIX}{key}={value}"] = cell
    return out


def _load_alignment(cells: Optional[dict] = None, uncelled: Optional[dict] = None, choices: Optional[dict] = None) -> dict:
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
    table it always saw and reads `default_cell` for it.

    `choices` is the table's optional `choices:` block (B10.56; `_check_choice_cells`), read from the roster when `cells` is, and merged
    into the returned axis rows under `choice:<key>=<value>`: absent or empty, the table is what it was."""
    if cells is None:
        cells = table("alignment")
        if uncelled is None:
            uncelled = table_meta("alignment").get("uncelled") or {}
        if choices is None:
            choices = table_meta("alignment").get("choices")
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
    out = {ax: {k: v for k, v in row.items() if v is not None} for ax, row in checked.items()}
    for ax, row in _check_choice_cells(choices).items():
        out.setdefault(ax, {}).update(row)
    return out

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


def align_choice(key: str, value, axis: str) -> float:
    """B10.56: the alignment of a CHOICE VALUE on an axis -- `align`'s reading for a `choice_sourced` payload key (`marshal`'s `retreat_at`
    `0.5`), the `choice:<key>=<value>` cell of `rosters.yaml: tables.alignment.choices`, else the table's `default_cell`. ⚠ IT READS
    `ALIGNMENT`, THE ONE BINDING (`align`'s warning): an `H-66` sweep point rebinds it, and a point built from the verb and deed cells alone
    (`uniform`) carries no choice cell, so a choice value scores `default_cell` there -- no value preferred, which is that control's claim."""
    return float(ALIGNMENT.get(axis, {}).get(f"{CHOICE_PREFIX}{key}={value}", ALIGNMENT_DEFAULT_CELL))


def celled_verbs() -> frozenset:
    """The verbs with AT LEAST ONE CELLED AXIS: a non-zero cell in the live `ALIGNMENT` binding.

    ⚠ G-1 (2026-10-06, [medium; Jordan to correct]) IS ITS FIRST READER: R-06 and R-08 count only
    candidates whose verb has a celled axis, because a verb with none -- an `uncelled:` verb such as
    `tell`, or one whose every cell is a considered `null` -- scores 0.0 for every person by
    construction, and its candidates can neither discriminate nor be a tie the ranking failed to
    break. Read off `ALIGNMENT`, the binding the sweep rebinds, so under `uniform` every verb is
    celled -- the control arm's own answer."""
    return frozenset(v for row in ALIGNMENT.values() for v, val in row.items()
                     if val and not str(v).startswith((DEED_PREFIX, CHOICE_PREFIX)))


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

    ⚠ IT IS A FLAG AND NOT A DELETE INSTRUCTION. Applied literally the rule condemns
    `(Person, pursuits)`, which #353 §9.3 REQUIRES ("moved by argument and consequence"). So a
    producerless row is one of two different things and the report cannot tell them apart:

      * A HOLE — the verb is missing (`determine` writes `(Person, pursuits)`; `argue`/`train`
        are IN-12 step 9), a gap in Part E, not a reason to delete a row #353 mandates.
      * DEAD — nothing in the design produces it.

    Distinguishing them is a judgement, so this reports and a human decides; it MUST NOT delete
    on sight."""
    produced = _produced_pairs(VERB_TABLE)
    out = {}
    for (kind, fld), row in MATRIX.items():
        if row.social is not True:
            continue                      # the world may write it; a verb is not required
        if f"{kind}.{fld}" not in produced:
            out[(kind, fld)] = row.emits
    return out

# From `rosters.yaml`, not a literal: the three points ARE a definition -- each names a claim
# the sweep compares -- so Jordan's no-hardcoding ruling reaches them.
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
    # point left (`sign_only` after `uniform` would be uniform again). The baseline is captured at
    # import and never rebound, which is what makes the three points independent.
    if point == "declared":
        return {ax: dict(row) for ax, row in ALIGNMENT_DECLARED.items()}
    if point == "uniform":
        # ⚠ EVERY (verb, axis) PAIR, NOT EVERY LISTED CELL, and the difference is the whole
        # control: UNLISTED pairs would fall through `align()` to `default_cell = 0.0`, a verb
        # absent from an axis would still score differently from one present on it, and
        # convictions could still discriminate. A control that the probe survives is not a
        # control (§0.1 point 2).
        # The deed keys too: `align_kind` reads a `deed:<kind>` cell first, so under the control a
        # kind several rows emit (no `KIND_VERB`) reads 1.0 like every verb, not 0.0. Since v9
        # IN-58, though, `person_q.deed_valence` returns 0 for those `PAIRED_KINDS`, so under this
        # control they are no longer scored on their claim's subject -- only for a paired doer.
        return {ax: {**{v: 1.0 for v in VERB_TABLE},
                     **{DEED_PREFIX + k: 1.0 for k in EMITTED_KINDS}} for ax in PURSUIT_AXES}
    return {ax: {v: (1.0 if w > 0 else -1.0 if w < 0 else 0.0) for v, w in row.items()}
            for ax, row in ALIGNMENT_DECLARED.items()}


def check_refusable(rows: Optional[dict] = None) -> dict:
    """`rosters.yaml: pursuit_axes.refusable`, CHECKED AT LOAD (B10.21), returned as `{axis: frozenset(verb)}`. `rows` is the
    table under test (default: the shipped one).

    Five refusals: a key off the axis roster or with no refusing pole (a list nobody can arm); a list that is not a list of
    distinct strings; a verb off `VERB_TABLE` (an act nobody can do); a verb with a ZERO cell on its axis (`data.verbs.align`
    is `0` -- the act the axis does not engage, which `refuses` could never refuse, so the listing would be a claim the gate
    cannot keep; the sparse default cell reads `0` too); a verb whose row emits no `scruple.overridden` in any band (B10.24: the kind is declared
    on every refusable row, or giving way on that verb leaves no Event).

    ⚠ IT LIVES HERE, NOT IN `data/rosters.py`, and is called from the foot of this module: `VERB_TABLE` and `align` live here, and
    `rosters` imports no `verbs` (this module imports it)."""
    out = {}
    for axis, verbs in (roster_map("pursuit_axes", "refusable") if rows is None else rows).items():
        require_member(axis, PURSUIT_AXES, f"pursuit_axes.refusable names {axis!r}, which is not on the roster",
                       "rosters.yaml", "ED-IN-0261 -- the refusable set is about a ROSTERED axis")
        refusing_pole(axis)
        if (not isinstance(verbs, (list, tuple)) or any(not isinstance(v, str) for v in verbs)
                or len(set(verbs)) != len(verbs)):
            raise Unspecified(f"pursuit_axes.refusable[{axis!r}] is {verbs!r}", "rosters.yaml",
                              needs="a list of distinct verb names", law="ED-IN-0261 -- the refusable set is a closed list of acts")
        for v in verbs:
            require_member(v, VERB_TABLE, f"pursuit_axes.refusable[{axis!r}] names {v!r}, which is not a verb",
                           "rosters.yaml", "a scruple forbids an act somebody can do",
                           needs="a `verb_table.yaml` key, spelled as it spells it")
            if not align(v, axis):
                raise Unspecified(f"pursuit_axes.refusable[{axis!r}] names {v!r}, which has no cell on {axis!r}", "rosters.yaml",
                                  needs=f"a non-zero `tables.alignment` cell for {v!r} on {axis!r}, or drop the verb",
                                  law="ED-IN-0261 -- only a verb the axis engages is one of the certain actions; a zero cell is never refused")
            row = VERB_TABLE[v]
            if not any(SCRUPLE_OVERRIDDEN in kinds for kinds in (row.emits, *row.emits_by_degree.values())):
                raise Unspecified(f"pursuit_axes.refusable[{axis!r}] names {v!r}, whose row emits no `{SCRUPLE_OVERRIDDEN}`", "rosters.yaml",
                                  needs=f"`{SCRUPLE_OVERRIDDEN}` in {v!r}'s `emits:` (a band of it, where it is band-keyed), or drop the verb",
                                  law="B10.24 -- a refusable verb done against his scruple is told: a row that cannot emit the kind leaves the giving way untold")
        out[axis] = frozenset(verbs)
    return out


check_refusable()      # B10.21: refuse a refusable verb off the table, or with no cell on its axis, at load (its owner imports this module)

