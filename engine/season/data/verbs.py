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

⚠ CORRECTED, step 7 of the decomposition: this paragraph used to say `align()` ITSELF DOES NOT
MOVE, present tense, true when written (step 3) and false now. `align()` moved to
`season.decision` at step 7, together with the rest of `decision/`'s person-side surface, and
THIS module is still the table it reads -- `decision.py` imports `ALIGNMENT`/
`ALIGNMENT_DEFAULT_CELL` from here, the same names `shape.py` re-exports back from `decision.py`
so `S.ALIGNMENT` keeps resolving. THE SWEEP STILL WORKS, BUT THE NAMESPACE THAT MAKES IT WORK
MOVED WITH THE READER: `test_season_shape.py`'s
`test_w5_the_alignment_table_is_swept_at_three_points_and_every_flip_is_printed` now rebinds
`decision.ALIGNMENT` (not `S.ALIGNMENT`, which would be a no-op on it since step 7), and
`align()` -- defined in `decision.py` now -- reads the global `ALIGNMENT` of the module it is
DEFINED IN, which is `decision.py`'s own, populated by the `from .data.verbs import ALIGNMENT`
in THAT file. The rule this paragraph exists to state is unchanged even though the address moved:
the rebind and the read still share a namespace, because that namespace is wherever `align` is
DEFINED, not wherever it happens to have been defined last (§4's "write the rule, not the
address" — the exact correction `shape.py`'s own S23/S30 breadcrumb records making twice already).
⚠ THE ORIGINAL SENTENCE ALSO NAMED THE WRONG TEST FILE (`test_tracer_is_honest.py`, under
`proposals/2026-08-31-shape-tracer/`, which does not mention `ALIGNMENT` at all) -- a
pre-existing inaccuracy this correction does not repeat, found while fixing the move claim rather
than by a separate pass, and left as a `not this step's declared scope` note rather than chased
further: nothing else in this docstring depended on it.

⚠ `VERB_TABLE` IS ASSIGNED TWICE, VERBATIM, AND ONLY THE SECOND ASSIGNMENT EVER RUNS. The
forward declaration below (`VERB_TABLE: dict = {}`) carries a comment from a PRIOR layout of
`shape.py`, from before steps 1-2 extracted the write matrix and roster readers: at that time
real loading code sat physically between the forward declaration and the fill. It does not any
more -- the two lines are adjacent -- and nothing at IMPORT TIME reads `VERB_TABLE` in the gap:
checked directly, `_load_alignment`'s own read of it (`verbs = set(VERB_TABLE)`) is inside a
function BODY, defined a few lines after the real fill but not CALLED (`ALIGNMENT =
_load_alignment()`) until further still -- by which point the real fill has long since run.
Preserved unchanged because this is a PURE MOVE and the forward declaration is otherwise
harmless -- a `dict` type hint on a name the next line immediately rebinds.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from . import files
from ..gaps import Forbidden, Unspecified
from .matrix import MATRIX
from .requires import TypedRequires, build_typed_requires
from .rosters import (
    CONVICTION_AXES, CONVICTIONS, RELEASABLE_KINDS, RUNG_KINDS, STRATA, load_yaml, roster,
    table,
    table_meta,
)

VERB_TABLE_YAML = files.VERB_TABLE_YAML

ELIGIBILITY_KINDS = roster("eligibility_kinds")

@dataclass(frozen=True)
class VerbRow:
    verb: str
    stratum: str
    eligibility: tuple        # a DISJUNCTION -- `transfer` is eligible by `own` OR `hold:<store>`
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
        row = VerbRow(name, r["stratum"], tuple(r["eligibility"]), r["requires"],
                      flat, flat_emits,
                      tuple(r["emits_on_refusal"]), r["grade"],
                      str(r.get("scale") or "person").strip(),
                      str(r.get("contests") or "").strip(),
                      by_degree, emits_by_degree,
                      build_typed_requires(name, r.get("requires_typed")),
                      str(r.get("requires_typed_note") or "").strip())
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
    # ⚠ ROW 15 HAS A SECOND HALF THIS DOES NOT IMPLEMENT, NAMED SO NOBODY READS THE CHECK'S NAME
    # AS COVERING IT: `04:464-465` states invariant 6 as two conjuncts, the domain AND *"every
    # kind's OPENER set is declared too"*. Only the first is here. The second is
    # `architecture/meta/HANDOFF_NEXT.md` item 1e and is open.
    if "release" not in out:
        raise SystemExit(
            "verb_table.yaml: no `release` row. Loader invariant 6 (04 PART D row 15) is the "
            "check that `tenure_kinds \\ {contain}` all have a closer, and without the verb "
            "every one of them is an edge that can be opened and never ended -- the "
            "open-without-close state T-m refuses. Removing the verb is a design change and "
            "`architecture/meta/HANDOFF_NEXT.md` §2a rules against re-opening it.")
    # ⚠ `RELEASABLE_KINDS` AND NOT A SECOND `frozenset(TENURE_KINDS) - {"contain"}`. The
    # derivation lives once, in `data/rosters.py` beside the roster it reads; this is the
    # comparison against the verb table's DECLARED column, which is the whole point of the column.
    if _release_domain != RELEASABLE_KINDS:
        raise SystemExit(
            f"verb_table.yaml: `release` declares domain {sorted(_release_domain)}, and "
            f"`tenure_kinds \\ {{contain}}` is {sorted(RELEASABLE_KINDS)}. Loader invariant 6 "
            "(04 PART D row 15) requires them equal: a kind in the roster and not in this "
            "domain is an edge that can be opened and never closed, and a kind here and "
            "not in the roster is a closer for a relation that does not exist.")
    return out

VERB_TABLE: dict = {}          # filled after STRATA loads, at the bottom of the roster block

VERB_TABLE = _load_verb_table()

def _check_sparse_table(name: str, cells: dict, rows: "set|tuple", row_what: str,
                        cols: "set|tuple", col_what: str, row_law: str, col_law: str) -> dict:
    """THE THREE CHECKS A ROSTER-KEYED SPARSE TABLE NEEDS, IN ONE PLACE.

    `alignment` (axis x verb) and `conviction_projection` (conviction x axis) are the same KIND of
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
    """`tables.conviction_projection`, the 13x4 that maps a person's convictions into axis space.

    ⚠⚠ **THIS TABLE EXISTS BECAUSE `conviction_axes` USED TO DO TWO JOBS AND COULD DO NEITHER
    WELL.** Before `U3` the roster held four names -- `Precedent`, `self_preservation`,
    `suspicion`, `harm_borne` -- one of which is a CONVICTION and three of which are ad-hoc
    scalars, and §F2's `conviction[axis]` looked a person's weight up in that one index set.
    `conviction_axes`'s own note called the conflation out and predicted this repair: *"THIRTEEN
    convictions projecting onto FOUR axes through a 13x4 matrix ... It is the likeliest thing to
    change when `H-46` closes."* It changed here, and `H-46` did NOT close -- Jordan, 2026-09-02:
    *"convictions roster and axes etc may be modified in future."*

    THREE CHECKS, each for a failure that would otherwise be SILENT, and each the exact shape
    `_load_alignment` uses one table over -- the rule lives once in kind, not in copy:
      * a conviction outside the roster is a row nobody projects FROM;
      * an axis outside the roster is a column nobody scores WITH;
      * an all-zero matrix makes every person's convictions project to the zero vector, which is
        `uniform`'s control arm shipped as the default -- the dead-carrier defect, one table along.

    ⚠ IT DOES NOT CHECK THAT ALL 13 x 4 CELLS ARE PRESENT. Sparse is lawful here exactly as it is
    for `alignment`: an unlisted pair reads `default_cell`. What is checked is that every cell
    NAMED is nameable."""
    cells = table("conviction_projection")
    return _check_sparse_table(
        "conviction_projection", cells, CONVICTIONS, "conviction", CONVICTION_AXES, "axis",
        row_law=("§F2 -- a person's convictions are weights over the roster. A projection row for a "
                 "conviction nobody can hold is read by nothing"),
        col_law=("engine/substrate/keys.py::AXES single-owns the four names; a fifth is one edit "
                 "there and a refusal here, never two rosters drifting apart"))


CONVICTION_PROJECTION = _load_projection()
# ⚠ NO `PROJECTION_DECLARED` HERE, AND ITS ABSENCE IS DELIBERATE. `ALIGNMENT_DECLARED` below
# exists because `ALIGNMENT` is REBOUND by `alignment_at()`'s sweep, so every arm must be
# built from an immutable baseline rather than from the previous arm. The projection has a
# declared `sweep:` on its row and NO `projection_at()` yet, so a frozen copy here would be a
# second 13x4 in memory that a reader assumes is wired to something because its sibling is.
# It comes back in the commit that adds the sweep, the way `ALIGNMENT_DECLARED` arrived with
# `ALIGNMENT_SWEEP`.
PROJECTION_DEFAULT_CELL = float(table_meta("conviction_projection").get("default_cell", 0.0))


def _load_alignment() -> dict:
    """§F2's `alignment(c.verb, axis)`, from `rosters.yaml`, with THREE load-time checks.

    Each check exists because the corresponding failure would be SILENT. A cell naming a verb the
    table no longer carries is dead weight nothing reports; an axis outside the roster makes
    `conviction[axis]` unreachable; and an all-zero matrix -- PLAN §W5's named guardrail -- "would
    pass every test while meaning nothing", which is the dead-carrier defect #353 `:739-744`
    describes. All three raise HERE rather than producing a plausible score later."""
    cells = table("alignment")
    verbs = set(VERB_TABLE)
    return _check_sparse_table(
        "alignment", cells, CONVICTION_AXES, "axis", verbs, "verb",
        row_law=("§F2 -- `conviction[axis] * alignment(verb, axis)` sums over the ROSTER. A cell on "
                 "an unrostered axis is never read and never reported"),
        col_law=("§E2 -- the verb table is the roster of verbs. A cell keyed on a verb that does "
                 "not exist is a weight on an option nobody can ever form"))

ALIGNMENT = _load_alignment()

# The immutable baseline. `ALIGNMENT` is REBOUND by a sweep; this is not, so every sweep point is
# built from the declared table rather than from the previous point (see `alignment_at`).
ALIGNMENT_DECLARED = {ax: dict(row) for ax, row in ALIGNMENT.items()}
ALIGNMENT_DEFAULT_CELL = float(table_meta("alignment").get("default_cell", 0.0))

def rows_without_a_producer() -> dict:
    """Every `social: true` row that no verb writes — §7.2's rule for W2, as a REPORT.

    ⚠ IT IS A FLAG AND NOT A DELETE INSTRUCTION, and the W2 audit is why. W2 retired six rows on
    this rule; applied literally the same rule condemns `(Person, convictions)`, which #353 §9.3
    REQUIRES ("moved by argument and consequence"). So a producerless row is one of two different
    things and the report cannot tell them apart:

      * A HOLE — the verb is missing. `(Person, convictions)` has no verb because Part E carries
        no argument verb, which is a gap in Part E, not a reason to delete a row #353 mandates.
      * DEAD — nothing in the design produces it. That was the six.

    Distinguishing them is a judgement, so this reports and a human decides. What it MUST NOT do
    is what the first reading of the rule did: delete on sight. `emits:` was parsed and never read
    by anything until this function, so the column the retirement rested on was inert data."""
    produced = {w for v in VERB_TABLE.values() for w in v.writes}
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
    if point not in ALIGNMENT_SWEEP:
        raise Unspecified(
            f"{point!r} is not an alignment sweep point", "H-66",
            needs=f"one of {list(ALIGNMENT_SWEEP)}",
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
        return {ax: {v: 1.0 for v in VERB_TABLE} for ax in CONVICTION_AXES}
    return {ax: {v: (1.0 if w > 0 else -1.0 if w < 0 else 0.0) for v, w in row.items()}
            for ax, row in ALIGNMENT_DECLARED.items()}

NO_PRECONDITION = ("—", "-", "")
