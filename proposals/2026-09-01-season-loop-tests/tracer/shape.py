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

import contextlib
import enum
import hashlib
from dataclasses import dataclass, field, fields as dc_fields
from pathlib import Path
from typing import Any, Callable, Optional

from trace_log import TRACE


# ===========================================================================
# GAP SIGNALS
# ===========================================================================

class InstrumentDefect(Exception):
    """THE INSTRUMENT WAS CALLED WRONG. Deliberately NOT a `ShapeGap`.

    ⚠ THIS EXISTS BECAUSE THE DISTINCTION WAS LOST ONCE AND COST THREE FALSE FINDINGS. `W5` moved
    the Tenure store onto its subject; three probes still wrote `w.tenures += [...]`; the
    read-only view refused them; `run_cases` catches EVERY `ShapeGap` and files it as a GAP --
    so `F1`, `F20` and `P40` flipped PASS -> GAP and the gap count rose 73 -> 76. Every one of
    those was A BUG IN THE PROBE, reported as a hole in the design.

    That is the worst failure this instrument can have. Its entire output is the claim *"here is
    what #353 does not specify"*, and a call-site bug that lands in that column corrupts the
    measurement in the direction that flatters it -- more holes found. `CLAUDE.md` §0.1 point 4:
    a number without a control is not a measurement, in EITHER direction.

    So: a refusal that means *"the design forbids this"* is a `Forbidden` and is a finding. A
    refusal that means *"you called me wrong"* is this, and is an INSTRUMENT-ERROR -- a bucket
    `run_cases` already had. The separation is by CLASS, so no probe can absorb one as the other,
    and `test_w5_no_gap_is_an_instrument_defect` is the falsifier."""


class ShapeGap(Exception):
    kind = "GAP"

    def __init__(self, what: str, where: str, needs: str = "", law: str = ""):
        self.what, self.where, self.needs, self.law = what, where, needs, law
        # REV 2 fix (antagonist obs. C-5 recurrence): a refusal a probe DELIBERATELY provokes
        # to verify it fires is not a gap in the case-blocking sense. `expect_refusal()` marks
        # the window so a passing probe no longer deposits a blocking gap row.
        TRACE.gap(self.kind, what, where, needs, law)
        super().__init__(f"[{self.kind}] {what}  @{where}" + (f"  needs: {needs}" if needs else ""))


class Unspecified(ShapeGap):
    """ARCHITECTURE.md NAMES this and does not specify it. Part IX S61-S62 is its own list.
    REV 2: this is also the kind for EVERY unmarked cell -- matrix or Partition -- because
    S30/S30.1 are one doctrinal condition and splitting them across two counters made the kind
    histogram a measurement of the transcription rather than of the design."""
    kind = "UNSPECIFIED"


class Forbidden(ShapeGap):
    """A law forbids what the case requires."""
    kind = "FORBIDDEN"


class NoProducer(ShapeGap):
    """Something the case needs -- a state change, or an INPUT -- that no step of the loop
    produces. REV 2 widened the docstring: the question `q` is an input, not a state change,
    and it was the category's only member under the narrower wording."""
    kind = "NO-PRODUCER"


class Collision(ShapeGap):
    """Two in-chain documents specify incompatible things. Part IX S62 is its own list."""
    kind = "COLLISION"


class Unowned(ShapeGap):
    """A value the case must change that the ownership table (S22) assigns to nobody. S22.3
    names four itself. Distinct from UNSPECIFIED: a specified mechanism with no writer."""
    kind = "UNOWNED"


class Ungraded(ShapeGap):
    """S42.2's polarity rule: zero evidence maps to the verdict AGAINST the thing measured. A
    row with no grade FAILS the export; it does not default to `assumption`. REV 2: this fires
    on an unregistered harness fixture, which is the same polarity applied to a number."""
    kind = "UNGRADED"


@contextlib.contextmanager
def expect_refusal():
    """Mark a window in which a refusal is EXPECTED -- the probe is verifying the law fires.
    Gap rows raised inside are tagged `expected` and excluded from blocking counts."""
    TRACE.expecting += 1
    try:
        yield
    finally:
        TRACE.expecting -= 1


# ===========================================================================
# S48 -- FIXED POINT.  S42.2.1 -- INJECT, GRADE, SWEEP. NO LITERAL IN ANY BODY.
# ===========================================================================

class Fixtures:
    """S42.2.1: never invent a constant. Inject it, declare it a harness fixture at
    `grade: assumption`, name the injection site, run a 3-point sweep, and treat A VERDICT
    THAT FLIPS ACROSS THE SWEEP AS ITSELF A FINDING.

    REV 2 added `wear_per_season` (per SITE KIND, with NO SILENT DEFAULT -- S42.2.1 names a
    wear table with a silent default as the exact prior sin), `confidence_default`, and
    `entrenchment_seasons`. It REMOVED `caller_supplied_max_depth`: S39.3 says the depth cap
    has NO DEFAULT, and a default relocated into a default-argument object is still a default."""

    def __init__(self, **vals: Any):
        self._v = dict(vals)
        self.reads: dict[str, int] = {}

    def get(self, name: str) -> Any:
        if name not in self._v:
            raise Ungraded(
                f"harness fixture '{name}' is not registered",
                "S42.2.1",
                needs="inject it, grade it assumption, name the injection site, sweep it",
                law="S42.2.1 -- a silent default does not fail; it answers, plausibly and wrongly, forever",
            )
        self.reads[name] = self.reads.get(name, 0) + 1
        return self._v[name]

    def wear(self, site_kind: str) -> int:
        """NO SILENT DEFAULT. An unregistered site kind RAISES rather than answering 20."""
        table = self.get("wear_per_season")
        if site_kind not in table:
            raise Ungraded(
                f"wear for site kind '{site_kind}' is not registered",
                "S42.2.1",
                needs="a per-kind wear row; S22 assigns `wear per site kind` to params",
                law="S42.2.1 -- 'a wear table that returns 20 for an unregistered site kind does not fail -- it answers, plausibly and wrongly, forever'",
            )
        return table[site_kind]

    def claim_decay(self) -> int:
        """`W4` / `H-40`. Confidence lost per season by a claim nobody refreshed — the THIRD
        licensed clock (#353 `:864`).

        ⚠ ON `wear`'s PRECEDENT, DELIBERATELY, INCLUDING THE REFUSAL. #353 licenses the clock and
        gives NO RATE, so this is an INJECTED DEFAULT with a site and a sweep (`H-40`, re-graded
        `assumption`), not a value the design states. It is registered rather than literal for the
        same reason `wear` is: *"a wear table that returns 20 for an unregistered site kind does
        not fail — it answers, plausibly and wrongly, forever."*"""
        table = self._v
        if "claim_decay_per_season" not in table:
            raise Ungraded(
                "claim confidence decay is not registered", "S42.2.1",
                needs="a `claim_decay_per_season` fixture row",
                law="S42.2.1 -- an unregistered rate must REFUSE, never answer plausibly")
        return table["claim_decay_per_season"]

    def sweep(self, name: str, value: Any) -> "Fixtures":
        f = Fixtures(**self._v)
        f._v[name] = value
        return f


# ⚠ `DEFAULT_FIXTURES` USED TO BE DEFINED HERE, AND `W8` MOVED IT BELOW THE ROSTER READERS.
# Three of its values are now READ FROM `rosters.yaml` rather than written as literals, and a
# reader that runs before `roster()` / `table()` / `roster_map()` exist cannot read anything.
# The move is mechanical: nothing between here and there referenced it except lazily.



# ===========================================================================
# S23 -- THE SIX STEPS; S30 -- THE FOUR WRITE CLASSES
# ===========================================================================

class Step(enum.Enum):
    CALENDAR = "CALENDAR"
    MATTER = "MATTER"
    DELIBERATE = "DELIBERATE"
    RESOLVE = "RESOLVE"
    WITNESS = "WITNESS"
    CENSUS = "CENSUS"


class WriteClass(enum.Enum):
    CALENDAR = "CALENDAR"
    MATTER = "MATTER"
    ACTS = "ACTS"
    INTERIOR = "INTERIOR"


# THE STEP -> WRITE CLASS MAP, and it is the single owner of that relation. CENSUS writes in the
# MATTER class (§30's reconciliation is a world write), DELIBERATE in ACTS -- it returns an act
# array and writes nothing else.
# roster-exempt: MECHANISM, and the distinction is the one rosters.yaml states. The STEP NAMES
# are `Step`'s own members — the six-step loop is the engine's shape, not the game's vocabulary —
# and this maps each to its write class, which is a RELATION the code owns. Moving it would invite
# someone to edit how the engine works while believing they were editing the game.
_STEP_CLASS = {
    "CALENDAR": WriteClass.CALENDAR,
    "MATTER": WriteClass.MATTER,
    "DELIBERATE": WriteClass.ACTS,
    "RESOLVE": WriteClass.ACTS,
    "WITNESS": WriteClass.INTERIOR,
    "CENSUS": WriteClass.MATTER,
}


# ===========================================================================
# PART D, LOADED FROM DATA -- W2.
#
# WHAT WAS HERE, AND WHY IT WENT. Six hand-maintained structures -- `WRITE_MATRIX`,
# `WRITE_CLASS_OF`, `PARTITION`, `PARTITION_ASSUMED`, `MATRIX_FIELD_OF` and `PARTITION_MISSING`
# -- plus a derivation loop that reconstructed the Partition from the matrix at import time.
# Every one of them was keyed on a THING (`stance`, `condition`, `Tenure`) because #353 §30's
# matrix is, and that keying IS defect `D1`: `(Person, convictions)` rode on `stance`'s row, so a
# real gap silently became a PASS. `MATRIX_FIELD_OF` existed only to paper over the mismatch, and
# it was a hand-written map of which fields were allowed to ride on which rows -- i.e. the defect,
# written down.
#
# `write_matrix.yaml` is keyed on `(kind, field)`, which is how §30's own rule is stated. The
# rule -- ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION -- is applicable now rather than
# aspirational, and there is nothing left to ride on.
#
# THE THREE `PARTITION_ASSUMED` ROWS ARE GONE AS ASSUMPTIONS. `(Person, claim_ledger)`,
# `(Date, fired)` and `(DocketItem, matter)` were instrument assumptions because the old
# two-clause derivation could not reach them. §D2's `DR-3` states them, so they are rows with a
# provenance now and `ASSUMPTIONS.md` regenerates with ZERO assumed Partition rows -- which is
# W2's own proof, and it is a REDUCTION in what the instrument supplies, not an addition.
# ===========================================================================

_HERE = Path(__file__).resolve().parent
WRITE_MATRIX_YAML = (_HERE.parent.parent / "2026-09-02-executable-architecture"
                     / "write_matrix.yaml")

# A step determines its write class exactly. ONE OWNER: the YAML's `class:` column carries V2's
# own string and the loader CHECKS it against this map rather than trusting either alone.
STEP_CLASS: dict = {Step[k]: v for k, v in _STEP_CLASS.items()}

# roster-exempt: MECHANISM. The abbreviations `write_matrix.yaml`'s `steps:` column uses, mapped
# to `Step`'s names. This is the FILE FORMAT, not a definition the game resolves from.
_STEP_OF = {"CAL": "CALENDAR", "MAT": "MATTER", "DEL": "DELIBERATE",
            "RES": "RESOLVE", "WIT": "WITNESS", "CEN": "CENSUS"}


@dataclass(frozen=True)
class MatrixRow:
    kind: str
    field: str
    steps: frozenset
    social: Optional[bool]      # None == `n/a`
    by: str
    emits: tuple

    def write_class(self, step: "Step") -> "WriteClass":
        return STEP_CLASS[step]



# ---------------------------------------------------------------------------
# ONE YAML READER FOR EVERY DATA FILE THIS INSTRUMENT OWNS, AND IT REFUSES A DUPLICATE KEY.
#
# ⚠ `yaml.safe_load` SILENTLY KEEPS THE LAST OF TWO IDENTICAL KEYS. `verb_table.yaml` declared
# `writes_note` TWICE on `issue` and twice on `petition` -- once with Part E's transcribed cell
# (*"a Dispensation is not a state write -- §37.3"*, *"a Petition is created, not written"*) and
# once with the `W3` audit's correction of it. The transcription was discarded at load, in the one
# file whose whole purpose is to be a faithful capture of Part E, and nothing said so. Both cells
# are merged in the data now; this is the guard that fails on recurrence.
#
# ⚠ SEVERITY, STATED ACCURATELY: `writes_note` is not a field of `VerbRow`, so nothing in the fold
# read either cell -- THAT instance lost transcribed text in a capture whose purpose is fidelity to
# Part E, and changed no behaviour. What earns the guard under `CLAUDE.md` §0.1 pt 5 is the same
# class at the ROW level, which DID change behaviour: two `(Office, exists)` rows where the loader
# took the last, so gate behaviour depended on file order. That fix guarded rows only; this guards
# every mapping in every file.
# ---------------------------------------------------------------------------

def load_yaml(text: str):
    """The instrument's only YAML entry point. Raises on a duplicate mapping key.

    Built per call rather than at module scope because this file imports `yaml` inside the
    functions that need it, and a class body cannot wait for that."""
    import yaml as _y

    class _NoDuplicateKeys(_y.SafeLoader):
        pass

    def _no_dup(loader, node, deep=False):
        seen, out = set(), {}
        for k, v in node.value:
            key = loader.construct_object(k, deep=deep)
            if key in seen:
                raise ValueError(
                    f"duplicate key {key!r} at line {k.start_mark.line + 1} -- `safe_load` would "
                    f"silently keep the last, which is how two `writes_note` cells became one")
            seen.add(key)
            out[key] = loader.construct_object(v, deep=deep)
        return out

    _NoDuplicateKeys.add_constructor(
        _y.resolver.BaseResolver.DEFAULT_MAPPING_TAG, _no_dup)
    return _y.load(text, _NoDuplicateKeys)


def _load_write_matrix() -> dict:
    import yaml as _yaml
    if not WRITE_MATRIX_YAML.exists():
        raise SystemExit(f"write_matrix.yaml not found at {WRITE_MATRIX_YAML}")
    doc = load_yaml(WRITE_MATRIX_YAML.read_text())
    out = {}
    for r in doc["rows"]:
        steps = frozenset(Step[_STEP_OF[s]] for s in r["steps"])
        # roster-exempt: MECHANISM. This parses §G4's three `social:` values into Python; it
        # is the file format, not a definition the game resolves from.
        social = {"true": True, "false": False, "n/a": None}[r["social"].strip()]
        # THE CROSS-CHECK. `class:` is V2's prose; the derivation is this file's. If they
        # disagree, one of them is wrong and neither may be trusted silently.
        derived = "/".join(sorted({STEP_CLASS[st].value for st in steps},
                                  key=lambda v: [s.value for s in Step].index(v)
                                  if v in [s.value for s in Step] else 99))
        stated = r["class"].strip()
        if steps and stated != "—":
            want = set(stated.split("/"))
            got = {STEP_CLASS[st].value for st in steps}
            if want != got:
                raise SystemExit(
                    f"write_matrix.yaml ({r['kind']}, {r['field']}): `class:` says {stated!r} and "
                    f"the step->class derivation gives {sorted(got)}. One is wrong; fix the row "
                    "or fix STEP_CLASS -- do not let them disagree.")
        emits = tuple(e.strip(" `") for e in r["emits"].split("·") if e.strip(" `—"))
        key = (r["kind"], r["field"])
        if key in out:
            # A DUPLICATE ROW SILENTLY OVERWROTE ITS TWIN and the only symptom was two counts
            # disagreeing -- 41 rows in the file, 40 in the map. Which of the two survives is
            # dict-insertion order, so the gate's behaviour would depend on where in the file
            # someone happened to add a row. That is precisely the class of defect this register
            # exists to end.
            raise SystemExit(
                f"write_matrix.yaml: ({r['kind']}, {r['field']}) appears more than once. "
                "One row per (kind, field) -- a duplicate makes the gate's behaviour depend on "
                "file order.")
        out[key] = MatrixRow(
            r["kind"], r["field"], steps, social, r["by"], emits)
    return out


# Filled at the bottom of this block, once Step/WriteClass exist.
MATRIX: dict[tuple[str, str], MatrixRow] = _load_write_matrix()

# Rows W2 RETIRED, kept so a write to one gets its own diagnosis rather than the generic
# "no row" -- a retired row and a row that never existed are different facts about the design.
import yaml as _yaml_boot
MATRIX_RETIRED: dict = {
    tuple(x.split(".", 1)): "retired by W2 -- its `emits:` kind is produced by no Part E verb "
                            "and written at no MATTER site"
    for x in (_yaml_boot.safe_load(WRITE_MATRIX_YAML.read_text()).get("retired") or [])
}

# S320's disclosure hook. W2 empties it BY CONSTRUCTION -- the three rows it used to carry were
# instrument assumptions only because the old two-clause derivation could not reach them, and
# S D2's DR-3 states all three. `report.py` still reads it, and it now reports zero.
PARTITION_ASSUMED: dict[tuple[str, str], tuple[bool, str]] = {}


def assume_partition_row(record_kind: str, fieldname: str, social: bool, why: str) -> None:
    """THE CHANNEL, kept live so its emptiness means something.

    ⚠ W2 emptied `PARTITION_ASSUMED` and reported "ZERO exercised assumptions" as its proof. An
    adversarial pass observed that the dict had become a LITERAL NO CODE PATH COULD POPULATE, so
    the claim was satisfiable BY DELETION and `ASSUMPTIONS.md` read "0 of 0" rather than "0 of 3".
    That is §0.1 point 2 in its purest form: an assertion that cannot observe the failure it
    excludes. This function is the path, so zero is now a measurement rather than an absence.

    An instrument that must assume a schema row calls this. It should never need to — §D2's DR-3
    states the three rows that used to be assumed — and if it ever does, `report.py` says so."""
    PARTITION_ASSUMED[(record_kind, fieldname)] = (social, why)
    ASSUMPTIONS_USED.add((record_kind, fieldname))

# ===========================================================================
# THE ROSTERS, LOADED FROM DATA.
#
# ⚠ RULED BY JORDAN, 2026-09-02: *"I do not want definitions etc to be hardcoded"* … *"these must
# be easy to modify"* … *"that goes for all"*. Six rosters — 35 definitions — were literals in
# this file. They are `rosters.yaml` now, and changing one is a data edit.
#
# `roster()` RAISES on a name the file does not carry. That is §42.2's polarity rule applied to
# definitions: an absent roster is a REFUSAL, never an empty set, because an empty set silently
# makes every membership test false and every closed-set guard vacuous.
# ===========================================================================

ROSTERS_YAML = (_HERE.parent.parent / "2026-09-02-executable-architecture" / "rosters.yaml")


def _load_rosters() -> tuple:
    import yaml as _y
    if not ROSTERS_YAML.exists():
        raise SystemExit(f"rosters.yaml not found at {ROSTERS_YAML}")
    doc = load_yaml(ROSTERS_YAML.read_text()) or {}
    return (doc.get("rosters") or {}), (doc.get("tables") or {})


_ROSTERS, _TABLES = _load_rosters()


def roster(name: str, ordered: bool = False):
    """A closed set, from `rosters.yaml`. `ordered=True` returns a tuple because the order is
    semantic (the strata resolve in sequence); otherwise a frozenset, so a caller cannot depend
    on an order the data does not promise."""
    r = _ROSTERS.get(name)
    if r is None:
        raise Unspecified(
            f"roster {name!r} is not in rosters.yaml", "rosters.yaml",
            needs="add the roster to the data file; do not inline it here",
            law="Jordan 2026-09-02 -- definitions are not hardcoded. An absent roster REFUSES; "
                "returning an empty set would make every membership test silently false")
    if "values" not in r:
        raise Unspecified(
            f"{name!r} is not a roster -- it has no `values:`", "rosters.yaml",
            needs="read a MAPPING with table(), a SET with roster()",
            law="rosters.yaml -- a roster is a SET and a table is a MAPPING. Reading one with the "
                "other's function raises, so the two shapes cannot be confused at a call site")
    vals = r["values"]
    # A roster may FORBID a member by name. `conviction_axes` forbids `exposure` bare, because
    # #353 `:1897` names it as three senses of one word; a data edit that added it would
    # otherwise reintroduce the collision silently, which is the whole failure mode this file
    # exists to prevent. The check is on the DATA, so it survives every route into the roster.
    for bad in (r.get("forbidden") or []):
        if bad in vals:
            raise Forbidden(
                f"roster {name!r} carries the forbidden member {bad!r}", "rosters.yaml",
                needs=f"spell the sense meant; {bad!r} is named as a collision, not a value",
                law=f"rosters.yaml -- {name}'s `forbidden:` list. A roster may bar a member by "
                    "name, and the bar is DATA so no code path can route around it")
    return tuple(vals) if (ordered or r.get("ordered")) else frozenset(vals)


def roster_map(name: str, key: str) -> dict:
    """A MAPPING that lives inside a roster row -- `titles.domains`, `contest_subsystems.prizes`.

    ⚠ THIS EXISTS BECAUSE TWO CALL SITES HAD ALREADY WRITTEN IT AS `_ROSTERS.get(x) or {}`, WHICH
    SILENTLY DEFAULTS. `rosters.yaml`'s own header states the polarity: *"a name the code asks for
    that is not here RAISES rather than defaulting, which is §42.2's polarity rule applied to
    definitions -- an absent roster is a refusal, never an empty set."* The bare-dict reads broke
    exactly that rule, and the consequence was not cosmetic: delete the `titles` key and
    `title_domain` returns `None` for every post, `target_is_title` becomes universally false, and
    `_req_revoke` SILENTLY REVERTS TO PURVIEW-FOR-EVERYTHING -- the reading Jordan's fourth
    message exists to forbid. A guard that fails open into the ruled-against behaviour.

    One owner, so a third mapping inherits the refusal by existing (§8). Found by the
    governance-canon adversarial pass."""
    r = _ROSTERS.get(name)
    if r is None:
        raise Unspecified(
            f"roster {name!r} is not in rosters.yaml", "rosters.yaml",
            needs="add the roster to the data file; do not inline it here",
            law="Jordan 2026-09-02 -- definitions are not hardcoded. An absent roster REFUSES; "
                "returning an empty mapping would make every lookup silently answer `None`")
    m = r.get(key)
    if not isinstance(m, dict):
        raise Unspecified(
            f"roster {name!r} has no mapping `{key}:`", "rosters.yaml",
            needs=f"give {name!r} a `{key}:` mapping, or read it with roster()/table()",
            law="rosters.yaml -- the mapping is the DEFINITION. An absent one cannot be "
                "substituted by an empty dict without inverting the answer it gives")
    return dict(m)


def table(name: str) -> dict:
    """A MAPPING from `rosters.yaml`'s `tables:`, returned as `{outer: {inner: float}}`.

    Sparse: a pair the data does not list reads as `default_cell`, which is NOT the same claim as
    an all-zero table -- `alignment` may be sparse and may not be uniformly zero, and the two are
    checked separately below."""
    t = _TABLES.get(name)
    if t is None:
        if name in _ROSTERS:
            raise Unspecified(
                f"{name!r} is a roster, not a table", "rosters.yaml",
                needs="read a SET with roster(), a MAPPING with table()",
                law="rosters.yaml -- a roster is a SET and a table is a MAPPING")
        raise Unspecified(
            f"table {name!r} is not in rosters.yaml", "rosters.yaml",
            needs="add the table to the data file; do not inline it here",
            law="Jordan 2026-09-02 -- definitions are not hardcoded. An absent table REFUSES")
    return {outer: dict(inner) for outer, inner in (t.get("cells") or {}).items()}


def table_meta(name: str) -> dict:
    """The table's own declarations -- `default_cell`, `row`, `keys`. Read rather than assumed, so
    a data edit that changes the sparse default cannot leave a stale constant in a body."""
    return {k: v for k, v in (_TABLES.get(name) or {}).items() if k != "cells"}


TENURE_KINDS = roster("tenure_kinds")
RUNG_KINDS = roster("rung_kinds", ordered=True)
REMIT_ACTS = roster("remit_acts")
WITNESS_CHANNELS = roster("witness_channels", ordered=True)
CLAIM_SOURCES = roster("claim_sources")
STRATA = roster("strata", ordered=True)
CONVICTION_AXES = roster("conviction_axes")
QUESTION_SOURCES = roster("question_sources", ordered=True)
PERSON_PREDICATES = roster("person_predicates")
VIEW_BUILDER_RULES = roster("view_builder_rules")
QUESTION_AGGREGATION = roster("question_aggregation", ordered=True)
SCENE_PACKING_RULES = roster("scene_packing_rules")
CLAIM_SUBJECT_RULES = roster("claim_subject_rules")
# ⚠ BOUND AT IMPORT LIKE THE OTHERS, AND THAT IS THE POINT. `titles` was the ONE roster read
# lazily through a bare `_ROSTERS.get(...) or {}`, so it alone got no existence refusal -- and
# because `_req_revoke` fails OPEN into purview-for-everything when the mapping is empty, the one
# unbound roster was the one whose absence silently restores a ruled-against behaviour.
TITLE_DOMAINS = roster_map("titles", "domains")

# ===========================================================================
# PART E, LOADED FROM DATA -- W3. THE RESOLVER'S BODY.
#
# #353 types `resolve : (Act[], World) -> Event[]` and never says what any verb DOES. That is
# defect `D20`, and it is why the tested instrument could only GRADE cases: with no table, every
# act needed a hand-written `effect` lambda, and A LAMBDA PER ACT IS A SECOND RESOLVER -- the
# thing §27.2 forbids, arriving as a parameter rather than as a function.
#
# `verb_table.yaml` is the body. One `resolve` reads it.
# ===========================================================================

VERB_TABLE_YAML = (_HERE.parent.parent / "2026-09-02-executable-architecture" / "verb_table.yaml")

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

    def eligibility_kinds(self) -> tuple:
        return tuple(a.split(":")[0].strip() for a in self.eligibility)


def _load_verb_table() -> dict:
    import yaml as _y
    if not VERB_TABLE_YAML.exists():
        raise SystemExit(f"verb_table.yaml not found at {VERB_TABLE_YAML}")
    doc = load_yaml(VERB_TABLE_YAML.read_text())
    out = {}
    for r in doc["verbs"]:
        name = r["verb"]
        if name in out:
            raise SystemExit(f"verb_table.yaml: {name!r} appears more than once")
        row = VerbRow(name, r["stratum"], tuple(r["eligibility"]), r["requires"],
                      tuple(r["writes"]), tuple(r["emits"]),
                      tuple(r["emits_on_refusal"]), r["grade"],
                      str(r.get("scale") or "person").strip(),
                      str(r.get("contests") or "").strip())
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
    return out


VERB_TABLE: dict = {}          # filled after STRATA loads, at the bottom of the roster block


VERB_TABLE = _load_verb_table()


def _load_alignment() -> dict:
    """§F2's `alignment(c.verb, axis)`, from `rosters.yaml`, with THREE load-time checks.

    Each check exists because the corresponding failure would be SILENT. A cell naming a verb the
    table no longer carries is dead weight nothing reports; an axis outside the roster makes
    `conviction[axis]` unreachable; and an all-zero matrix -- PLAN §W5's named guardrail -- "would
    pass every test while meaning nothing", which is the dead-carrier defect #353 `:739-744`
    describes. All three raise HERE rather than producing a plausible score later."""
    cells = table("alignment")
    verbs = set(VERB_TABLE)
    for axis, row in cells.items():
        if axis not in CONVICTION_AXES:
            raise Forbidden(
                f"alignment names axis {axis!r}, which is not in the conviction_axes roster",
                "rosters.yaml",
                needs="add the axis to conviction_axes, or drop the row",
                law="§F2 -- `conviction[axis] * alignment(verb, axis)` sums over the ROSTER. A "
                    "cell on an unrostered axis is never read and never reported")
        unknown = sorted(set(row) - verbs)
        if unknown:
            raise Forbidden(
                f"alignment[{axis}] names {len(unknown)} verb(s) no verb table row carries: {unknown}",
                "rosters.yaml",
                needs="spell the verb exactly as verb_table.yaml spells it, or drop the cell",
                law="§E2 -- the verb table is the roster of verbs. A cell keyed on a verb that "
                    "does not exist is a weight on an option nobody can ever form")
    if not any(v for row in cells.values() for v in row.values()):
        raise Forbidden(
            "the alignment table is all zeroes", "rosters.yaml",
            needs="a default with at least one non-zero weight",
            law="PLAN §W5 -- 'a zero matrix makes convictions inert, which is the dead-carrier "
                "defect #353 `:739-744` names, and it would pass every test while meaning nothing'")
    return cells


ALIGNMENT = _load_alignment()


def _load_matter_tables() -> tuple:
    """`W8`. The matter economy's three tables, from `rosters.yaml`, with load-time checks.

    ⚠ THESE WERE LITERALS IN `DEFAULT_FIXTURES` AND PLAN `W8` ASKS FOR THEM AS REGISTRY ROWS. The
    comment that stood beside them objected, reasonably, that *"splitting them into rosters.yaml
    would put one declaration in two files"* — and the answer is that the fixture READS the data
    rather than restating it, so there is still exactly one declaration and it is the data.

    ⚠ THE CHECKS ARE THE POINT, not the relocation. A wear or weight table whose keys drift from
    the roster is §42.2.1's worked sin arriving through a data edit instead of through a literal:
    an unregistered kind that ANSWERS. Both directions are checked — a rate for a kind no roster
    carries, and a site kind with no rate."""
    kinds = set(roster("site_kinds"))
    rates = roster_map("wear_per_season", "rates")
    floors = table("band_floors")
    weights = roster_map("subsistence_weight", "weights")
    for name, got in (("wear_per_season", set(rates)), ("band_floors", set(floors))):
        if got - kinds:
            raise Forbidden(
                f"{name} names site kind(s) no roster carries: {sorted(got - kinds)}",
                "rosters.yaml",
                needs="add the kind to `site_kinds`, or drop the row",
                law="S42.2.1 -- an unregistered kind must RAISE, and a table keyed past its own "
                    "roster is that same silent answer arriving through the data file")
        if kinds - got:
            raise Ungraded(
                f"{name} has no row for site kind(s): {sorted(kinds - got)}", "rosters.yaml",
                needs=f"a {name} row per site kind",
                law="S42.2.1 -- 'a wear table that returns 20 for an unregistered site kind does "
                    "not fail -- it answers, plausibly and wrongly, forever'")
    yields = table("site_yield")
    if set(yields) - kinds:
        raise Forbidden(
            f"site_yield names site kind(s) no roster carries: {sorted(set(yields) - kinds)}",
            "rosters.yaml", needs="add the kind to `site_kinds`, or drop the row",
            law="S42.2.1 -- a table keyed past its own roster answers for a kind nobody declared")
    mk = set(roster("matter_kinds"))
    for sk, produced in yields.items():
        if set(produced) - mk:
            raise Forbidden(
                f"site_yield[{sk}] produces matter kind(s) no registry row carries: "
                f"{sorted(set(produced) - mk)}", "rosters.yaml",
                needs="add the kind to `matter_kinds`, or drop the cell",
                law="#353 §10.4 -- MatterKind is a REGISTRY. Open means addable, not unchecked")
    if not any(produced for produced in yields.values()):
        raise Ungraded(
            "site_yield is empty for every site kind", "rosters.yaml",
            needs="at least one producing kind, or delete the economy",
            law="PLAN W8 -- `yield` is the matter economy's ONLY source; an all-empty table is "
                "the `none` CONTROL ARM, and shipping the control as the default would make "
                "every store deplete monotonically while the proof clause claims otherwise")
    unknown = set(weights) - mk
    if unknown:
        raise Forbidden(
            f"subsistence_weight names matter kind(s) no registry row carries: {sorted(unknown)}",
            "rosters.yaml",
            needs="add the kind to `matter_kinds`, or drop the weight",
            law="#353 §10.4 -- MatterKind is a REGISTRY. Open means addable, not unchecked")
    return rates, floors, weights, yields


WEAR_RATES, BAND_FLOORS, SUBSISTENCE_WEIGHTS, SITE_YIELD = _load_matter_tables()


DEFAULT_FIXTURES = Fixtures(
    # S48: condition is an int on an EXPORTED scale. S22 assigns the scale to `params`, and the
    # in-chain params document "proposes NO VALUES", so this is a fixture. Injection site: here.
    condition_scale=1000,
    # RULED TWICE. #353 §26.3 puts the budget at "~5"; Jordan ruled 2026-09-02 that the UNIT is
    # the SCENE and the number is 5 -- *"5 scenes for a character to play per season"*. A band is
    # not an integer; this is the integer the instrument runs on, and A31 sweeps it because the
    # verdict moves with it.
    # ⚠ `W17` RENAMED THIS FROM `act_budget`. #353 §26.3's prose counts ACTS throughout and the
    # ruling re-states it in scenes: "a wounded duke gets fewer SCENES than a healthy one". The
    # spray argument survives the noun change unaltered -- five scenes each spent petitioning is
    # exactly the triage the budget exists to create -- but the key must not keep saying `act`,
    # because a name is where the next reader learns what the number counts.
    scene_budget=5,
    # S20: the ledger cap L. Params-owned; no in-chain value.
    ledger_cap=200,
    # S18: "at most K claim ids from the holder's OWN ledger -- BUILT, NOT FILTERED".
    view_k=12,
    # S22 assigns `wear per site kind` to params. NO in-chain table exists, so every kind the
    # instrument touches is declared here and an unregistered kind RAISES (see Fixtures.wear).
    # roster-exempt: Fixtures keys. `Fixtures` IS the registry for numbers and raises on an
    # unregistered kind, so the kinds are already declared data; splitting them into
    # rosters.yaml would put one declaration in two files. ⚠ `site_kinds` belongs in
    # rosters.yaml when W8 builds H-07's per-kind table, and not before.
    # ⚠ `W8` MOVED THE TABLE TO `rosters.yaml` AND THIS READS IT. The literal that stood here
    # carried an objection to splitting it out ("one declaration in two files"); the fixture
    # reading the data answers it, because the declaration is now in exactly one place and this
    # is not a copy of it. `Fixtures.wear` still refuses an unregistered kind.
    wear_per_season=WEAR_RATES,
    # S20: Claim.confidence. Rev 1 hardcoded 1, which degenerated the eviction comparator.
    confidence_default=100,
    # `W4` / `H-40`, THE THIRD LICENSED CLOCK (#353 `:864`). #353 licenses confidence decay at
    # MATTER and gives NO RATE, so this is an INJECTED DEFAULT with a `site:` and a three-point
    # sweep on the register, exactly as `H-09` treats the confidence default beside it. It is a
    # fixture rather than a literal so `Fixtures.claim_decay` can REFUSE when it is unregistered
    # — `wear`'s precedent, and S42.2.1's rule.
    claim_decay_per_season=5,
    # `W6` / `H-33`. WHICH WITNESS CHANNELS ARE LIVE. `total` is the DEFAULT AND THE CONTROL --
    # it is #353's specified behaviour (S61: *"WITNESS AS SPECIFIED FANS EVERY EVENT TO EVERY
    # PERSON"*), so the sweep's control arm is the design as written rather than a baseline
    # somebody invented. The three points are `H-33`'s own declared sweep.
    fan_out_mode="total",
    # `H-87`. S39.3 REFUSES a default for the contest depth cap -- *"a default is a number
    # somebody made up and it will be cited later as though it were measured"* -- so `contest()`
    # takes it from the CALLER. This is the caller's number, injected and swept, and it lives here
    # rather than in a body so that it is one.
    contest_max_depth=2,
    # S15.2: entrenchment(h,H) = min(1, seasons_held / 60). The 60 IS in-chain; it is a fixture
    # only so no literal sits in a body.
    entrenchment_seasons=60,
    # S27.4: "an attempt at Ob > 2 x Pool is refused, and the season is spent."
    obstacle_refusal_multiple=2,
    # S12.1 gates verbs on `condition` against per-kind band FLOORS. S22 assigns "band
    # coefficients" and "the obstacle floor" to params; the params document proposes NO
    # VALUES, so these are harness fixtures and A31c sweeps them. S42.2.1 names "three band
    # edges" as one of the four constants a prior instrument in the chain invented -- rev 2
    # fixed the other three and left these hardcoded in probe bodies, unswept.
    # roster-exempt: Fixtures keys, as `wear_per_season` above. These are H-08 and are swept.
    band_floors=BAND_FLOORS,          # `W8` -- `rosters.yaml: tables.band_floors`, `H-08`
    # ⚠ `W8` / `H-26`. #353 §22.3 names *"`season_factor`'s distribution"* as a value with NO
    # OWNER, and §25 says `yield` is *"blocked on"* it -- so the SHAPE ruled is a DISTRIBUTION and
    # what is injected here is a degenerate one. The sweep is on its value, which is the only axis
    # a constant has; a real distribution is a different hole and is not invented here.
    season_factor=1.0,                # `H-26`, swept 0.5 / 1 / 2
    # ⚠ `W8` / `H-11`. #353 §10.4 makes `MatterKind` open and V2 gives the draw's SHAPE -- *from
    # the containing rung's stores, scaled by weight* -- and no weights. Registry row, not literal.
    subsistence_weight=SUBSISTENCE_WEIGHTS,
    # W5 / `H-28`. §F3's `budget` has three modifier terms and #353 gives a value for NONE of
    # them -- `:912-913` says only that "a wounded duke gets fewer acts than a healthy one".
    # So the DIRECTION is ruled and the MAGNITUDE is not, which is exactly a fixture. Injection
    # site: here. Row: `H-70`, swept. ⚠ The BAND TABLE they read is NOT invented -- `band_floors`
    # above already carries a `"body"` row, so `condition_penalty(p's body band)` counts bands
    # against the table the site gate already uses. `H-38` closed with "`Site.condition` is the
    # model"; this is that closure spent rather than restated.
    # `H-54`, swept. The rule was `qs[0]` in a subscript; see `aggregate_questions`.
    question_aggregation_rule="first",
    # `W17` / Jordan 2026-09-02. The unit is the scene and the number is 5; NEITHER of these two
    # was ruled, so both are fixtures with register rows and a sweep. Source for both defaults:
    # `player_agency_v30.md` §6.3 -- "One scene action = one scene opportunity pursued. A scene
    # contains 1-3 mechanical interactions" -- which is `## Status: CANONICAL` but pre-#337 and,
    # under `CLAUDE.md` §0.05, REFERENCE rather than mechanism. `None` means unbounded.
    interactions_per_scene=3,          # `H-76`, swept 1 / 3 / unbounded
    extended_scene_cost=2,             # `H-77`, swept 1 / 2 / 3
    scene_packing_rule="greedy",       # `H-78`, swept greedy / one_per_scene / by_subject
    claim_subject_rule="both",         # `H-79`, swept actor / per_change / both
    # `H-80`. #353 §13.1 says the ACT declares a Record's stages and their terms. §F1's Candidate
    # is `(verb, subject, why)` and carries no operands, so NO COMPUTED ACT CAN DECLARE ANY --
    # `(Record, stages)` is a Part D row unreachable from the person's own decision. These are
    # the instrument's declared stand-in, swept, and the row says plainly that they are.
    record_stages_default=3,
    record_stage_term=1,
    budget_office_bonus=1,
    budget_leg_penalty=1,
)
# The immutable baseline. `ALIGNMENT` is REBOUND by a sweep; this is not, so every sweep point is
# built from the declared table rather than from the previous point (see `alignment_at`).
ALIGNMENT_DECLARED = {ax: dict(row) for ax, row in ALIGNMENT.items()}
ALIGNMENT_DEFAULT_CELL = float(table_meta("alignment").get("default_cell", 0.0))


def matrix_rows_without_a_field() -> dict:
    """Every matrix row whose `(kind, field)` names no field of that kind's model.

    ⚠ THE W2 ADVERSARIAL PASS NAMED THIS GAP: *"nothing checks that a matrix row's `fieldname` is
    a real field of its `record_kind` — which is exactly how `(Record, held_by)` survived four
    revisions."* It reports rather than raising, because a row can legitimately outrun the model:
    Part D is the SPECIFICATION and this file is one implementation of it, so a row naming a field
    the instrument has not built yet is a TODO for the instrument, not a defect in Part D.

    Kinds the instrument models as DICTS rather than classes — `Date`, `DocketItem`, `Petition`,
    `Dispensation`, `ConveningCondition` — cannot be checked at all and are reported separately,
    so the number is never mistaken for a clean bill.

    ⚠ `Rung` WAS IN THAT SECOND BUCKET AND DOES NOT BELONG THERE. The test was `is_dataclass`, and
    `Rung` is a plain class with an explicit `_DECLARED` field set — the whitelist S10 gives it, so
    that an undeclared attribute raises. Five rows, `(Rung, yield)` among them, were reported as
    *uncheckable* while the class carries the exact declaration needed to check them; and
    `(Rung, yield)` is the row `W8` exists to build, so the one instrument that could have said
    *the field does not exist yet* was excusing itself from the answer. A declared field set is a
    field set whatever shape it is stored in. Found while opening `W8`."""
    import dataclasses as _dc
    out = {"absent": [], "unmodelled": []}
    for (kind, fld) in sorted(MATRIX):
        cls = globals().get(kind)
        declared = (set(getattr(cls, "_DECLARED", ()) or ()) or
                    ({f.name for f in _dc.fields(cls)} if _dc.is_dataclass(cls) else set()))
        if cls is None or not declared:
            out["unmodelled"].append((kind, fld))
            continue
        if fld == "exists":
            continue                     # existence is the collection's membership, not a field
        if fld not in declared:
            out["absent"].append((kind, fld))
    return out


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




# Where S30's matrix says "no", the refusal belongs to the LAW THE CELL ENFORCES, not to the
# matrix's bookkeeping rule. These are the cells whose "no" is a named law refusing.
MATRIX_REFUSAL_LAW: dict[tuple[tuple[str, str], Step], tuple[str, str]] = {
    (("Person", "stance"), Step.MATTER): (
        "S3-L4",
        "L4 / S25 -- NO SOCIAL QUANTITY MOVES AT MATTER. 'The world may silt a harbour; IT MAY "
        "NOT SOUR A TOWN'S MOOD.' This is the design refusing, not the design failing to say"),
    (("Person", "stance"), Step.CALENDAR): (
        "S24", "S24 -- CALENDAR DECIDES NOTHING; it fires occasions"),
    (("Person", "stance"), Step.WITNESS): (
        "S9.3",
        "S9.3 -- WITNESS NEVER TOUCHES A BELIEF. If evidence can move a conviction the moral "
        "layer has become a second epistemic layer and T2 is gone"),
    (("Rung", "yield"), Step.RESOLVE): (
        "S30", "S30 -- `yield` is written at MATTER ONLY; it is the matrix's one single-cell row"),
    (("Person", "claim_ledger"), Step.RESOLVE): (
        "S20", "S20 -- `witness` is THE ONLY MINTER of a root token, and it runs at WITNESS"),
}

# ⚠ W2 AUDIT. Rekeying the table on `(kind, field)` NARROWED IT FOUR-FOLD without anyone noticing.
# Under the old thing-keying, every field written with `thing="stance"` INHERITED stance's laws --
# so `(Person, convictions)`, `(Person, beliefs)`, `(Person, scar)` and `(Person, axis_count)` got
# L4/§25 and §9.3 for free, and after the rekey they fell through to the generic "ANY UNMARKED
# CELL" branch. Four of the design's proudest refusals began logging as bookkeeping, which is
# exactly what REV 4's comment in `write()` exists to prevent.
#
# THE FIX IS NOT TO RESTORE THE RIDE-ON -- that inheritance WAS defect D1, and getting the law by
# riding on a neighbour's row is how `(Person, convictions)` became a PASS in the first place.
# Each row states its own law, which is what keying on the pair is for.
# roster-exempt: MECHANISM. The four rows that lost their law to the rekey, listed so each gets
# its own entry. Which rows these are is derivable from the matrix (`social: true`, Person);
# the list is a loop over a fix, not a definition.
for _pk_field in ("convictions", "beliefs", "scar", "axis_count"):
    MATRIX_REFUSAL_LAW[(("Person", _pk_field), Step.MATTER)] = (
        "S3-L4",
        "L4 / S25 -- NO SOCIAL QUANTITY MOVES AT MATTER. 'The world may silt a harbour; IT MAY "
        "NOT SOUR A TOWN'S MOOD.' This is the design refusing, not the design failing to say")
    MATRIX_REFUSAL_LAW[(("Person", _pk_field), Step.CALENDAR)] = (
        "S24", "S24 -- CALENDAR DECIDES NOTHING; it fires occasions")
    MATRIX_REFUSAL_LAW[(("Person", _pk_field), Step.WITNESS)] = (
        "S9.3",
        "S9.3 -- WITNESS NEVER TOUCHES A BELIEF. If evidence can move a conviction the moral "
        "layer has become a second epistemic layer and T2 is gone")

# ⚠ REV 5. This set was WRITTEN AND NEVER READ for two revisions, while S320's comment promised
# the assumed rows were "REPORTED IN THE OUTPUT, so a reader can see exactly how much of L4's
# enforcement rests on the instrument". Under this file's own fidelity rule 6 that was a false
# claim of a disclosure mechanism. `report.py` now reads it.
ASSUMPTIONS_USED: set[tuple[str, str]] = set()


def matrix_row(record_kind: str, fieldname: str) -> MatrixRow:
    """THE ONE LOOKUP. Six structures and a derivation loop collapsed into this, because they
    were six answers to one question that #353 §30 asks once: is `(kind, field)` on the table?"""
    row = MATRIX.get((record_kind, fieldname))
    if row is not None:
        return row
    if (record_kind, fieldname) in MATRIX_RETIRED:
        raise Unspecified(
            f"({record_kind}, {fieldname}) was RETIRED from the write matrix", "S30.1",
            needs="a Part E verb that produces its `emits:` kind, added in the same commit as "
                  "the row",
            law=MATRIX_RETIRED[(record_kind, fieldname)])
    raise Unspecified(
        f"({record_kind}, {fieldname}) is on no row of the write matrix", "S30.1",
        needs="rule the row first, then add it; the reverse order invents the thing the rule prevents",
        law="S30 -- ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION. L4's membership test is a "
            "STATIC SCHEMA COLUMN, not a judgement; S42.3 -- configuring an unspecified thing "
            "invents it")


def partition_lookup(record_kind: str, fieldname: str, thing: str = "") -> tuple[bool, str]:
    """L4's `social:` for a pair. Kept as a name because probes call it; it is a thin read of
    `matrix_row` now, and `thing` is ignored -- IT IS THE PARAMETER THAT CARRIED THE DEFECT."""
    row = matrix_row(record_kind, fieldname)
    if row.social is None:
        raise Unspecified(
            f"({record_kind}, {fieldname}) is `social: n/a` -- the row admits no write of this "
            "kind", "S30.1", needs="a `social:` column entry, ruled", law=row.by)
    return row.social, row.by


# ===========================================================================
# S33 -- DETERMINISM
# ===========================================================================

def H(world_seed: int, tick: int, subject_id: str, purpose: str) -> str:
    """S33/S49: an OWNED, VERSIONED mix -- never a language built-in hash(), whose value is not
    a cross-version contract. `purpose` must be unique per DRAW, not per operation."""
    return hashlib.blake2b(f"v1|{world_seed}|{tick}|{subject_id}|{purpose}".encode(),
                           digest_size=8).hexdigest()


ROOT = "ROOT"


# ===========================================================================
# PART II -- THE PRIMITIVES
# ===========================================================================

@dataclass
class Tenure:
    """S15 -- THE ONE EDGE. Owned by its SUBJECT (S15.1)."""
    id: str
    subject: str
    object: str
    kind: str
    since: int
    until: Optional[int] = None
    conferrer: Optional[str] = None
    degree: Optional[str] = None
    payload: Any = None

    @property
    def live(self) -> bool:
        return self.until is None




@dataclass
class StateChange:
    """S16 -- THE ONE STATE CHANGE."""
    subject: str
    mode: str
    driver: str
    field: Optional[str] = None
    delta: Any = None
    spec: Any = None


@dataclass
class Event:
    """S19 -- THE RECORD THAT WAS MISSING. S19.3: three fields are NOT on it and each absence
    is a design decision -- no actor (attribution is a per-witness Claim), no target (observers
    are computed at WITNESS from presence; THE EMITTER DECLARES NO RECIPIENT), no stat_deltas."""
    id: str
    kind: str
    subject: str
    changes: list[StateChange]
    causes: list[str]
    emitted_at: int
    degree: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.causes:
            raise Forbidden(
                f"Event {self.kind} emitted with causes=[]", "S19.4",
                needs="causes: [ROOT] for an antecedent-free emission",
                law="S19.4 -- causes[] is REQUIRED AND NON-EMPTY; [ROOT] makes the empty list unrepresentable rather than merely discouraged",
            )


@dataclass
class Claim:
    """S20. Lives in the HOLDER'S OWN ledger."""
    id: str
    holder: str
    subject: str
    predicate: str
    value: Any
    when: int
    source: str
    confidence: int
    visibility: str




class Sensation:
    """S18.2 -- EXACTLY TWO SCALARS, and it is the ONLY bridge from world truth into `choose`.

    REV 3. Rev 2 made `sense()` raise outright, which was right about `standing` and wrong
    about everything else: the driver then routed AROUND `Sensation` entirely and fed
    DELIBERATE a bare int, so the type S26 puts in `choose`'s signature was NEVER CONSTRUCTED
    IN ANY RUN and a regression test pinned the deviated 4-ary call as the invariant.

    The honest shape is to keep the type and RAISE AT THE POINT OF USE. `subsistence` is
    computable from an injected formula; `standing` is not computable at all, so reading it
    raises. A `choose` that never consults standing runs; one that does gets the gap exactly
    where the design fails to supply it.

    S34's enforcement column rates the two-scalar rule `convention -- the named residual
    risk`. `__slots__` is the nearest Python approximation to S46.1's `Vector2` argument and
    is still a convention a determined author can spell around."""

    # roster-exempt: MECHANISM -- `__slots__` is a Python language construct naming this
    # class's own attributes, as on `View`.
    __slots__ = ("subsistence", "_standing")

    def __init__(self, subsistence: int, standing: Optional[int] = None):
        self.subsistence = subsistence
        self._standing = standing

    @property
    def standing(self) -> int:
        """S18.2's second scalar. COMPUTED as of `W5`; see `standing_of`.

        Rev 3 raised `Unspecified` here and its reason was half right. It said the direct route --
        reading a value off every other person -- is barred by S22.4 clause 2. V2 §F4 corrected
        that: clause 2 governs RESOLVER-SIDE Queries and `sense()` is explicitly not one, so the
        real bar is §20, "Claims live in the holder's own ledger... Nobody else may read or write
        it." Same conclusion, right law, and it points at the answer rather than at a wall."""
        if self._standing is None:
            raise Unspecified(
                "Sensation.standing", "S18.2",
                needs="construct the Sensation through `sense()`, which computes both scalars",
                law="S18.2 -- Sensation is EXACTLY TWO SCALARS. A Sensation built with only "
                    "`subsistence` is half a Sensation, and reading the missing half must refuse "
                    "rather than answer 0 -- §42.2's polarity rule applied to a constructor")
        return self._standing

    def __iter__(self):
        return iter((self.subsistence, self._standing))


class View:
    """S18.1 -- a View holds IDS, NEVER REFERENCES. L2 is enforced BY CONSTRUCTION: any attempt
    to reach a world collection through a View raises. S18: AT MOST K ids, BUILT NOT FILTERED."""

    # roster-exempt: MECHANISM. `__slots__` is a PYTHON LANGUAGE CONSTRUCT — it names this
    # class's own attributes and the interpreter reads it, so changing it changes how the code
    # works, never what the game is. It crossed the guard's three-element threshold only when W5
    # added `question`, which is the guard behaving correctly on a shape it cannot distinguish.
    __slots__ = ("holder", "claim_ids", "question")

    def __init__(self, holder: str, claim_ids: list[str], k: int, question: Any = None):
        if len(claim_ids) > k:
            raise Forbidden(f"View built with {len(claim_ids)} ids against cap K={k}", "S18",
                            law="S18 -- at most K claim ids from the holder's OWN ledger")
        object.__setattr__(self, "holder", holder)
        object.__setattr__(self, "claim_ids", list(claim_ids))
        # ⚠ W5: THE VIEW CARRIES ITS QUESTION, and this is a defect found in §F2 rather than a
        # convenience. §F2 types `choose(p, view, sensation, ask_budget)` -- FOUR parameters --
        # and its body then reads `candidates = opening_set(p, view, q)`, where `q` IS FREE: the
        # pseudocode uses a variable its own signature does not bind. Widening `choose` to five
        # would break the signature §26 states, so the binding goes where §F1 already put it --
        # `assemble(person, question) -> View` builds the View FROM the question, so the View is
        # the thing that knows which question it was built for. No signature changes.
        object.__setattr__(self, "question", question)

    def __getattr__(self, name: str) -> Any:
        raise Forbidden(
            f"choose() reached for world state '{name}' through its View", "S3-L2",
            needs="a person decides from their own claims; world truth enters only via sense()",
            law="L2 -- choose never receives a World. NOT BY DISCIPLINE -- BY TYPE",
        )


@dataclass(frozen=True)
class Question:
    """§F1's `q` -- the thing a person is deliberating ABOUT, and the input `opening_set` derives
    its subjects from. `H-04` / §61's `NoProducer` is closed by `questions_for()` below.

    `source` is one of `question_sources` in `rosters.yaml`. `referents` are the ids the question
    is ABOUT -- §F1 clause 3: "subject in referents(q)". `about` is the originating object's id,
    kept so a Candidate can say WHY it exists without the resolver re-deriving it."""
    id: str
    source: str
    referents: tuple
    about: str = ""

    def __post_init__(self) -> None:
        if self.source not in QUESTION_SOURCES:
            raise Forbidden(
                f"question source {self.source!r} is not in the question_sources roster",
                "§F1", needs="add it to rosters.yaml, or use one of the four",
                law="§F1 -- a question is produced by these sources and by nothing else. V2 said "
                    "THREE and was wrong by one; the roster is where a fifth would be argued for")


@dataclass
class Candidate:
    """S17 -- `opening_set` RETURNS Candidate[], NOT Act[]."""
    verb: str
    subject: Optional[str] = None
    why: str = ""


@dataclass
class Scene:
    """THE BUDGETED UNIT. Ruled by Jordan, 2026-09-02: *"5 scenes for a character to play per
    season"*.

    ⚠ IT IS A LEVEL ABOVE THE VERB TABLE AND CHANGES NOTHING BENEATH IT. Parts D and E stand
    unaltered: the table's rows are the INTERACTIONS, and a Scene carries 1-3 of them. `PLAN.md`
    `W17` says so and it is worth restating -- this is the cheapest shape the ruling could have
    taken, and nothing about the write matrix or the resolver moves.

    #353 §26.3's prose counts ACTS throughout. Re-stated in scenes, its argument is unaltered:
    "a wounded duke gets fewer SCENES than a healthy one", and five scenes each spent petitioning
    is exactly the triage the budget exists to create. The noun changes; the spray argument does
    not.

    `extended` costs more than one scene action (`H-77`, swept). Both that cost and the
    interactions bound are FIXTURES and register rows -- Jordan ruled the UNIT and the NUMBER and
    ruled neither of these."""
    id: str
    actor: str
    acts: list = field(default_factory=list)
    extended: bool = False

    # roster-exempt: MECHANISM. `PLAIN_COST` is the DEFINITION OF THE UNIT -- one ordinary scene
    # is one scene action -- not a tunable value. `H-77` tunes what an EXTENDED scene costs
    # relative to it, and a "cost" whose base was itself variable would make the budget's units
    # undefined. Named rather than inlined because §42.2.1's rule is that no bare literal sits in
    # a body, and because naming it is what makes the distinction from `extended_cost` visible.
    PLAIN_COST = 1

    def cost(self, extended_cost: int) -> int:
        return extended_cost if self.extended else self.PLAIN_COST


@dataclass
class Act:
    id: str
    actor: str
    verb: str
    changes: list[StateChange] = field(default_factory=list)
    reads: list[str] = field(default_factory=list)
    contests: list[str] = field(default_factory=list)
    payload: Any = None
    # S27's five strata. 4 == "social", the stratum most acts in this corpus belong to; the
    # value is declared rather than silent, and A37 exercises the ordering.
    stratum: int = 4
    # ⚠ S27.4 refuses an attempt at Ob > 2 x Pool and routes an UNCONTESTED attempt to A GATE,
    # "never to an Ob = 0 roll". `None` means UNCONTESTED (no obstacle was declared); 0 would
    # be the Ob=0 roll the section names, which is why it is not the default.
    obstacle: Optional[int] = None
    pool: Optional[int] = None


# S27: FIVE STRATA. movement / binding decisions / contested physical / uncontested material / social


@dataclass
class Person:
    """S9. A COHORT IS A PERSON AT weight > 1. ONE CLASS (S9.1)."""
    id: str
    name: str = ""
    weight: int = 1
    marks: list[str] = field(default_factory=list)
    capability: dict = field(default_factory=dict)
    stance: list[tuple] = field(default_factory=list)
    convictions: dict = field(default_factory=dict)
    beliefs: list[tuple] = field(default_factory=list)
    ledger: list[Claim] = field(default_factory=list)
    # W5. Part D carries `(Person, body)` and `(Person, travel_leg)` and this class had NEITHER,
    # so both rows named a field that did not exist — the `(Record, held_by)` defect, at scale
    # (see `matrix_rows_without_a_field`). `budget` reads both, person-side, which is PLAN §3.3's
    # smaller amendment: a Person owns every Tenure whose subject they are, so office-holding,
    # body and travel are all the person's own state and `sense()` keeps §18.2's "the ONE".
    # `condition_scale`, not a literal 1000: a person at full body is at the top of the same
    # fixed-point scale `Site.condition` uses, which is what `H-38` closing on "`Site.condition`
    # is the model" MEANS. A bare 1000 here would be a second, silent copy of that scale — the
    # defect `G1` names — and it would drift the moment the fixture moved.
    body: int = field(default_factory=lambda: DEFAULT_FIXTURES.get("condition_scale"))
    travel_leg: list[str] = field(default_factory=list)
    # ⚠ W5 MOVED THE TENURE STORE HERE, and `Tenure`'s OWN DOCSTRING already said this: "S15 --
    # THE ONE EDGE. Owned by its SUBJECT (S15.1)." The class asserted the ownership and the
    # storage contradicted it -- every Tenure lived in one flat `World.tenures` list. That was
    # survivable until `budget : (Person, View) -> int` had to read "own `hold` Tenures" WITH NO
    # WORLD (#353 `:877`, `:912-913`; `H-28`). With a flat world list that signature is
    # UNSATISFIABLE, which is why V2 §F3 gave `budget` a `World` and became a SECOND non-decision
    # function taking one -- breaking `:634`'s "the ONE non-decision function permitted a World".
    # PLAN §3.3 takes the smaller amendment instead: #353 `:730` gives Person "every Tenure whose
    # subject they are", so the store was in the wrong place all along and no signature had to
    # change. `World.tenures` is now a READ-ONLY VIEW over these; see `_TenureView`.
    tenures: list = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.weight < 1:
            raise Forbidden("Person.weight < 1", "S9", law="S9 -- weight >= 1, default 1")


@dataclass
class Site:
    """S12. `condition` is PRIMARY STATE, a FIXED-POINT INT (S48), and it GATES VERBS (S12.1)."""
    id: str
    rung: str
    kind: str
    condition: int
    drawers: list[str] = field(default_factory=list)


@dataclass
class Record:
    """S13 -- a LIVE CARRIER. S30.1: it has NO Partition row, so every Record write is an
    unmarked cell -- which this instrument reports rather than papering over."""
    id: str
    rung: str
    kind: str
    forgery_quality: int = 0
    subject_matter: Any = None
    ttl: Optional[int] = None
    stages: list[tuple] = field(default_factory=list)


@dataclass(frozen=True)
class Proposition:
    """S14. IDENTITY-BEARING AND IMMUTABLE. Fixed at utterance, never destroyed.
    REV 2: `frozen=True` makes the immutability structural rather than asserted."""
    id: str
    mood: str
    subject: str
    predicate: str
    value: Any
    when: int
    scope: Any = None


@dataclass
class Office:
    """S11. `rung?` is OPTIONAL; null is the office-cluster case (S6.2)."""
    id: str
    post: str
    rung: Optional[str]
    remit_acts: list[str]
    scope_rung: Optional[str] = None
    binds: str = "members_by_admission"
    conferral: Optional[str] = None
    revocation: Optional[str] = None
    establishment: list[str] = field(default_factory=list)
    dates: list[str] = field(default_factory=list)
    upkeep: Any = None

    def __post_init__(self):
        # The remit is a fixture choice; its MEMBERS are not. A typo here would mint a remit act
        # and every `remit:<that act>` eligibility would silently never match -- a verb quietly
        # unavailable to everyone, which is the worst shape a failure can take.
        bad = [a for a in self.remit_acts if a not in REMIT_ACTS]
        if bad:
            raise Unowned(f"office {self.id!r} claims remit acts not on the roster: {bad}",
                          "S11", needs="an act from rosters.yaml: remit_acts",
                          law="#353 §11 -- the remit acts are a CLOSED set")




class Rung:
    """S10 -- THE HOLON. Eight kinds, ONE type. A Rung owns NO SOCIAL AGGREGATE (S10.1).

    REV 2: rev 1 blacklisted six spellings, so `r.morale` and `r.stability` passed. This is a
    WHITELIST over S10's declared field set -- a concept check rather than a term check.
    Any attribute not in S10's record raises, whatever it is called."""

    # roster-exempt: MECHANISM. These are the FIELD NAMES of this dataclass, checked so an
    # undeclared attribute raises. They are the code's own shape, not the game's vocabulary.
    # ⚠ `yield` IS PART D's FIELD NAME AND IT IS A PYTHON KEYWORD, so it is reached with
    # `getattr`/`setattr` rather than dotted access. Renaming it here would break the
    # `(record_kind, fieldname)` key the write gate, the write class and the emission all share
    # (§8) — the key is the same string Part D uses, and Part D says `yield`. `W8` added it: the
    # row existed in the matrix from the start and named a field the class did not have, which
    # `matrix_rows_without_a_field` now reports because it reads `_DECLARED` (see that function).
    _DECLARED = {"id", "kind", "stores", "sites", "records", "dates", "stake",
                 "envelope", "transmission", "judging_set_rule", "yield"}

    def __init__(self, id: str, kind: str, **kw: Any):
        if kind not in RUNG_KINDS:
            raise Forbidden(f"Rung.kind '{kind}'", "S10", law=f"S10 -- eight kinds: {RUNG_KINDS}")
        object.__setattr__(self, "id", id)
        object.__setattr__(self, "kind", kind)
        # `yield` is #353 §25's *"only here"* row: what this rung PRODUCED this season, per
        # matter kind. Empty for a rung that produces nothing, which is most of them.
        for f_, d in (("stores", dict), ("sites", list), ("records", list),
                      ("dates", list), ("stake", list), ("envelope", list), ("yield", dict)):
            object.__setattr__(self, f_, kw.pop(f_, None) or d())
        object.__setattr__(self, "transmission", kw.pop("transmission", None))
        # S10.2 caveat: `judging_set_rule` is UNSPECIFIED (S61). It is carried as a field so the
        # record matches S10, and reading it raises -- see Query.judging_set.
        object.__setattr__(self, "judging_set_rule", kw.pop("judging_set_rule", None))
        if kw:
            raise Forbidden(f"Rung given undeclared fields {sorted(kw)}", "S10.1",
                            law="S10.1 -- a Rung owns NO social aggregate: no norms, no densities, no reputation, no unrest, no legitimacy. EVERY ONE IS A QUERY")

    def __setattr__(self, k: str, v: Any) -> None:
        if k not in self._DECLARED:
            raise Forbidden(
                f"Rung.{k} assigned -- not a declared field of S10's record", "S10.1",
                needs="a Query over the containment subtree, owned by Nobody",
                law="L3 -- every aggregate is a function, never a field. S22.1 -- if the aggregate is a function it CANNOT go stale and CANNOT be initialised and then forgotten, because there is nothing to initialise",
            )
        object.__setattr__(self, k, v)


# ===========================================================================
# S45.1 -- DECLARE `World` FIRST
# ===========================================================================


class _TenureView(list):
    """`World.tenures` -- a READ-ONLY concatenation over the owners (S15.1).

    ⚠ IT RAISES ON EVERY MUTATOR, and that is the whole reason it is a class rather than a plain
    `list(...)`. `CLAUDE.md` §0.1 point 1 names this exact hazard: *"when a getter starts computing
    from a new source while setters still write the old one, EVERY WRITER SILENTLY BECOMES A
    NO-OP."* Moving the store onto `Person` did precisely that to nine `w.add_tenure(...)`
    sites. Returning a plain list would have let all nine keep running, keep appending to a
    throwaway, and keep passing -- the Tenure would simply never exist. Every one of them now
    fails at the call, and the fix is `w.add_tenure(t)`, which routes by subject."""

    # roster-exempt: MECHANISM. These are PYTHON'S mutator method names, not a game definition
    # — rosters.yaml's own test is "would changing this change the GAME, or change how the code
    # works?", and editing this list changes only which call raises. It is also not a set anyone
    # may edit: it is fixed by the language. The guard flagging it is the guard working; a
    # declared exemption is the answer, and a name-based whitelist would not be (G2).
    _MUTATORS = ("append", "extend", "insert", "remove", "pop", "clear", "sort", "reverse",
                 "__setitem__", "__delitem__", "__iadd__", "__imul__")

    def _refuse(self, *_a, **_k):
        # `InstrumentDefect`, NOT `Forbidden`: this is a call-site bug, not a law of the design,
        # and filing it as a GAP is what put three false holes in the count. See the class.
        raise InstrumentDefect(
            "w.tenures is a READ-ONLY VIEW over the subjects that own the Tenures (S15.1). "
            "Use w.add_tenure(t) -- it routes by subject to the owner. Mutating the "
            "concatenation would write to a temporary and silently lose the Tenure.")


for _n in _TenureView._MUTATORS:
    setattr(_TenureView, _n, _TenureView._refuse)


class World:
    def __init__(self, world_seed: int, fixtures: Fixtures = DEFAULT_FIXTURES):
        self.world_seed = world_seed
        self.tick = 0
        self.fixtures = fixtures
        self.persons: dict[str, Person] = {}
        self.rungs: dict[str, Rung] = {}
        self.offices: dict[str, Office] = {}
        self.sites: dict[str, Site] = {}
        self.records: dict[str, Record] = {}
        self.propositions: dict[str, Proposition] = {}
        # S15.1 -- the store is the SUBJECT'S. `_unowned` holds only the Tenures whose subject
        # is not a person (`contain : Rung -> Rung` is the bulk of them). See the `tenures` view.
        self._unowned: list[Tenure] = []
        self.log: list[Event] = []
        self.dates: dict[str, dict] = {}
        self.docket: list[dict] = []

        self.petitions: dict[str, dict] = {}
        self.dispensations: dict[str, dict] = {}
        self.manifest: dict[str, str] = {}      # S43 -- role -> provider, resolved AT BOOT
        self.step: Optional[Step] = None
        self.frozen = False
        self._barrier_cache: dict = {}
        self._in_parallel_map = False
        self.writes: list[tuple] = []
        # `W4`. The Events `write()` emitted during the current barrier, so a caller that needs an
        # ANTECEDENT can name the emission its own write just produced -- which is how a band
        # crossing's `causes[]` reaches the wear that crossed the floor.
        self._emitted_by_write: list[Event] = []
        self.crossings: list[tuple] = []        # S12.1/L5 -- band-edge crossings, EMISSIONS
        # S33: "`purpose` must be unique per DRAW, not per operation, or two draws inside one
        # act collide." A per-TICK ordinal is unique within the tick AND identical across runs
        # of the same seed -- a global counter would be unique but NOT REPRODUCIBLE, which
        # destroys the replay contract, and a content hash collides when two draws are alike.
        self.draw = 0

    # -- S30.2: the write class is a PARAMETER of the store API, THE GATE APPLIES THE WRITE,
    # and `record_kind`/`fieldname` are REQUIRED so the L4 limb cannot be silenced by omission.
    # -- THE TENURE STORE, ROUTED BY SUBJECT (S15.1) -----------------------
    @property
    def tenures(self) -> "_TenureView":
        """Every live-or-dead Tenure, owner-first. Read-only -- see `_TenureView`."""
        self._rehome()
        out: list[Tenure] = []
        for pid in sorted(self.persons):
            out.extend(self.persons[pid].tenures)
        out.extend(self._unowned)
        return _TenureView(out)

    def add_tenure(self, t: Tenure) -> Tenure:
        """The ONE writer. Routes to `t.subject`'s own list, or to `_unowned` when the subject is
        not a person (`contain : Rung -> Rung` is most of those)."""
        (self.persons[t.subject].tenures if t.subject in self.persons else self._unowned).append(t)
        return t

    def _rehome(self) -> None:
        """A Tenure added BEFORE its subject existed landed in `_unowned`; move it now.

        Without this, ordering decides ownership: a fixture that appends the Tenure and then
        creates the Person leaves `p.tenures` empty while `w.tenures` still shows it -- so
        `budget` would read zero offices for a duke the world agrees is a duke. That is a
        read/write asymmetry of exactly the shape §0.1 point 1 describes, and it would be
        invisible because both surfaces are individually correct."""
        if not self._unowned:
            return
        keep = []
        for t in self._unowned:
            (self.persons[t.subject].tenures if t.subject in self.persons else keep).append(t)
        self._unowned = keep

    def _refuse_undeclared_kind(self, thing, wclass, sname, record_kind, fieldname,
                                emits, declared) -> None:
        """A kind no Part D row declares is a FABRICATED kind, and the `emits:` column is the only
        thing that may name one.

        ⚠ ONE RULE, ONE MESSAGE. This lived twice — once on the must-name-a-kind path and once on
        the exempt path — and the two copies said *"which Part D does not declare for it"* and
        *"undeclared"*, so a test matching one passed and the other did not. §8 broken inside a
        single function, which is the smallest scale this repo has yet found it at. Found by the
        `W4` adversarial pass."""
        if emits is None or emits in declared:
            return
        TRACE.write(thing, wclass.value, sname, False)
        raise Forbidden(
            f"({record_kind}, {fieldname}) tried to emit {emits!r}, which Part D does not "
            f"declare for it: {list(declared)}", "D22",
            needs=f"one of {list(declared)}",
            law="a kind no row declares is a FABRICATED kind, and the `emits:` column is the "
                "only thing that may name one")

    def write(self, thing: str, wclass: WriteClass, apply: Callable[[], Any],
              record_kind: str, fieldname: str, driver: str,
              caused_person_exists: Optional[str] = None,
              emits: Optional[str] = None,
              causes: Optional[list[str]] = None,
              subject: Optional[str] = None) -> Any:
        """`W4`. THE GATE IS ALSO THE EMITTER, because `H-12` is `ruled` that way: *"MATTER emits
        an Event per write so crossings have an antecedent"*, default *"Part D's `emits:` column"*.

        A MATTER write on a row that declares an `emits:` kind MUST name one, and naming one the
        row does not declare is refused. That pairing is `D22` made mechanical: a MATTER write with
        a declared emission that emits nothing is the SILENT WRITE the design forbids, and an
        emission the matrix never declared is a fabricated kind. Both directions matter — §42.2's
        polarity rule is that absence maps to the verdict against the thing measured, so the
        absence of an emission has to be a refusal rather than a quiet success.

        Emission lives HERE rather than at each call site because §8's invariant is that every rule
        lives once: keyed on `(record_kind, fieldname)`, which is the same key the write class and
        the social partition are already read from, so a new MATTER write inherits its emission by
        existing rather than by remembering."""
        step = self.step
        sname = step.value if step else "-"
        # W2: THE GATE IS KEYED ON `(kind, field)`, which is how S30's own rule is stated. It was
        # keyed on `thing`, and that is defect D1 in one line: `(Person, convictions)` rode on
        # `stance`'s row, so a real gap became a PASS. `thing` survives as a TRACE label only.
        try:
            row = matrix_row(record_kind, fieldname)
        except Unspecified:
            TRACE.write(thing, wclass.value, sname, False)
            raise
        allowed = row.steps
        if step not in allowed:
            TRACE.write(thing, wclass.value, sname, False)
            # ⚠ REV 4. Rev 3 raised Unspecified here on the argument that S30 and S30.1 are
            # one doctrinal condition. THEY ARE NOT, and the over-correction reported THREE OF
            # THE DESIGN'S PROUDEST REFUSALS AS DEBTS: W3 ("the world sours a mood"), A3 ("an
            # arc ends at a counter"), P19 ("a threshold produces an outcome") all showed as
            # UNSPECIFIED at S30 -- L4 and L5 tallied as things the design failed to say.
            #
            #   a cell marked "no"  = the design REFUSING          -> Forbidden, at ITS law
            #   a row that is absent = the design NOT SAYING       -> Unspecified, at S30.1
            #
            law = MATRIX_REFUSAL_LAW.get(((record_kind, fieldname), step))
            if law is not None:
                raise Forbidden(f"({record_kind}, {fieldname}) written during {sname}", law[0],
                                needs=f"one of {sorted(s.value for s in allowed)}", law=law[1])
            raise Forbidden(f"({record_kind}, {fieldname}) written during {sname}", "S30",
                            needs=f"one of {sorted(s.value for s in allowed)}",
                            law="S30 -- ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION")
        expect = row.write_class(step)
        if expect is not wclass:
            TRACE.write(thing, wclass.value, sname, False)
            raise Forbidden(
                f"({record_kind}, {fieldname}) written in class {wclass.value} at {sname}; "
                f"the matrix says {expect.value}",
                "S30.2", law="S30.2 -- the write class is a PARAMETER of the store API, checked PER WRITE SITE")
        social, prov = partition_lookup(record_kind, fieldname)
        if social and driver != "Act":
            TRACE.write(thing, wclass.value, sname, False)
            raise Forbidden(
                f"({record_kind}, {fieldname}) is social:true and was written by {driver}", "S3-L4",
                needs="a named person's act",
                law=f"L4 -- social:true means ONLY AN ACT may write it. The world may silt a harbour; IT MAY NOT SOUR A TOWN'S MOOD. [row provenance: {prov}]")
        # W2 AUDIT: `(Person, coherence)` is written ONLY through seam Events (#353 :1904), and
        # the seam is RESOLVE via `contest` (:98). The row said so IN A COMMENT, which constrains
        # nothing -- this file's own fidelity rule 6: a false claim of enforcement is worse than
        # none. Bounded here, on `(Tenure, until)`'s precedent one block below.
        if (record_kind, fieldname) == ("Person", "coherence") and driver != "Seam":
            TRACE.write(thing, wclass.value, sname, False)
            raise Forbidden(
                f"(Person, coherence) written by {driver}", "S54 item 15",
                needs="driver='Seam' -- a contest Event at RESOLVE",
                law="#353 :1904 -- Coherence is 'written only through SEAM Events', and :98 puts "
                    "the seam at RESOLVE via `contest`. Any other writer makes it a FOURTH "
                    "licensed clock, and §25.1 says the three are exhaustive")

        # S15.3 -- THE SEAM IS BOUNDED BY A CAUSATION RULE, NOT BY THE COLUMN. An actorless row
        # may write Tenure.until ONLY on a (Person, exists) change THE SAME ROW ALSO CAUSED.
        if (record_kind, fieldname) == ("Tenure", "until") and driver != "Act":
            if caused_person_exists is None:
                TRACE.write(thing, wclass.value, sname, False)
                raise Forbidden(
                    "an actorless row wrote Tenure.until with no (Person, exists) change of its own",
                    "S15.3", needs="the same row must cause the death it ends a tenure through",
                    law="S15.3 -- a plague that kills the praefect ends his tenure THROUGH THE DEATH; A STORM CANNOT TOUCH IT. A second such seam means the column is the wrong mechanism")
        # S30.2: "AND THE GATE MUST APPLY THE WRITE." A gate that validates, logs and returns
        # true while the mutation happens beside it is worse than no gate.
        # -- W4: THE EMISSION, GATED ON THE SAME ROW AS THE WRITE ------------------------
        declared = tuple(row.emits or ())
        # `H-86`. A row whose declared emissions are ALL CONDITIONAL is exempt from the
        # must-name-a-kind rule -- `(Record, ttl)` declares only `record.expired`, and emitting
        # that on a non-terminal decrement asserts an expiry that has not happened. The exempt
        # rows are DATA (`rosters.yaml: conditional_emission_rows`), never a literal here, and the
        # ambiguity in Part D's column that makes the roster necessary is registered rather than
        # decided. The exemption is narrow: an UNDECLARED kind is still refused below.
        conditional = roster("conditional_emission_rows")
        if (wclass is WriteClass.MATTER and declared
                and f"{record_kind}.{fieldname}" not in conditional):
            if emits is None:
                TRACE.write(thing, wclass.value, sname, False)
                raise Forbidden(
                    f"({record_kind}, {fieldname}) written at MATTER and emitted nothing, while "
                    f"Part D declares {list(declared)}", "D22",
                    needs="emits=<one of the row's declared kinds>",
                    law="`H-12`, RULED: MATTER emits an Event PER WRITE so crossings have an "
                        "antecedent, and the kind is Part D's `emits:` column. A MATTER write "
                        "that emits nothing is the silent write `D22` names")
            self._refuse_undeclared_kind(thing, wclass, sname, record_kind, fieldname,
                                         emits, declared)
        else:
            self._refuse_undeclared_kind(thing, wclass, sname, record_kind, fieldname,
                                         emits, declared)

        before = apply()
        TRACE.write(thing, wclass.value, sname, True)
        self.writes.append((thing, wclass.value, sname, record_kind, fieldname, driver))
        if emits is not None:
            # ⚠ THE SUBJECT IS THE RECORD, NOT THE TRACE LABEL. `thing` is a human label for the
            # trace line (`"condition"`); the Event's subject has to be the RECORD ID or nothing
            # can find the emission again. The first version used `thing`, so every site's wear
            # emitted under the subject `"condition"` — and `last_emission_of` therefore never
            # matched, so season 1's wear re-rooted at `[ROOT]` and the clock did not chain. That
            # is exactly the failure `W4`'s ROOT-count proof exists to catch, and it caught it.
            if subject is None:
                raise Forbidden(
                    f"({record_kind}, {fieldname}) emits {emits!r} with no `subject=`", "S33",
                    needs="subject=<the record id>",
                    law="THE SUBJECT IS THE RECORD, NOT THE TRACE LABEL. The fallback was "
                        "`subject or thing`, and `thing` is a human label for the trace line -- "
                        "which is exactly the value that made every site's wear emit under the "
                        "subject `\"condition\"`, so `last_emission_of` never matched and the clock "
                        "re-rooted every season. Leaving the fallback in place meant emission was "
                        "inherited by existing while the half that makes a clock CHAIN still had "
                        "to be remembered -- and a one-shot emission with a forgotten `subject=` "
                        "is silent. Found by the `W4` adversarial pass")
            subj = subject
            # ⚠ THE DRAW ORDINAL IS PART OF THE ID, AND IT WAS NOT. Without it the id is
            # `(seed, tick, subject, kind)`, so TWO EMISSIONS OF ONE KIND ON ONE SUBJECT IN ONE
            # TICK GET THE SAME ID — and `W8` produces exactly that: MATTER's larder draw and its
            # yield credit both write `(Rung, stores)` and both emit `stores.changed` for the same
            # rung in the same season. The `W4` adversarial pass named this months of work ago in
            # the abstract (*"the emission id carries no draw ordinal; `new_draw()` has zero
            # callers"*) and nothing could reach it until there were two same-kind writes; the
            # uniqueness guard caught it the moment there were. S33's ordinal is the mechanism the
            # design already carries, reset per tick by `season()`, so ids stay reproducible: the
            # write order is deterministic (every loop here is sorted) and the counter follows it.
            ev = Event(
                # ⚠ IN `purpose`, NOT AS A FIFTH ARGUMENT. `H`'s own docstring states the
                # contract — *"`purpose` must be unique per DRAW, not per operation"* — so the
                # ordinal belongs inside the string the design already reserves for it, and
                # widening `H`'s signature would have been a second way to say the same thing.
                id=H(self.world_seed, self.tick, subj, f"emit:{emits}#{self.new_draw()}"),
                kind=emits, subject=subj,
                changes=[StateChange(subj, "set", wclass.value, fieldname, None)],
                # ⚠ `causes` IS REQUIRED IN SUBSTANCE AND THE DEFAULT IS NOT `[ROOT]`. Handing an
                # un-caused emission the root is how every Event in the `W9` artifact came to
                # carry `causes=[ROOT]` — #353 §19.4 calls that field "the substrate of the entire
                # emergent-narrative claim", and a default root populates it with nothing. A
                # caller with no antecedent must say so by passing `[ROOT]` itself.
                causes=list(causes if causes is not None else []),
                emitted_at=self.tick)
            # ⚠ NO EMPTY-`causes[]` CHECK HERE. `Event.__post_init__` already refuses one at
            # S19.4, and re-implementing it would be `CLAUDE.md` §8's violation one constructor
            # apart — the first version of this block did exactly that and shipped two messages
            # for one rule. The Event constructor raises before this line is reached.
            self.log.append(ev)
            TRACE.event(ev.id, ev.kind, ev.causes)
            # ⚠ BUFFERED ONLY AT MATTER, AND THE SCOPE IS THE POINT. `matter()` drains this to
            # decide what WITNESS fans out. A WITNESS-step emission (`claim.deposited`) left in
            # the buffer survives into the NEXT season's MATTER and is fanned there, which closes
            # a loop: a deposit emits, the emission is witnessed, that deposit emits. Measured
            # before this guard: `claim.deposited` reached 249 in a two-season run and was
            # accelerating. The buffer is MATTER's, so only MATTER fills it.
            if step is Step.MATTER:
                self._emitted_by_write.append(ev)
        return before

    # -- S4: a Query MAY be cached. Built AT a barrier, read-only until the next, DISCARDED there.
    def cache_at_barrier(self, key: str, build: Callable[[], Any]) -> Any:
        if self._in_parallel_map:
            raise Forbidden(f"cache '{key}' built inside a parallel map", "S4",
                            law="S4 -- the cache is built AT A BARRIER; NOTHING INSIDE A PARALLEL MAP BUILDS ONE")
        if key not in self._barrier_cache:
            self._barrier_cache[key] = build()
        return self._barrier_cache[key]

    def last_emission_of(self, kind: str, subject: str) -> Optional[str]:
        """The id of the most recent Event of `kind` about `subject`, or None.

        `W4`'s chaining primitive: a licensed clock's next tick names its previous one, so
        `[ROOT]` stops appearing after the clock's genuine first emission."""
        for e in reversed(self.log):
            if e.kind == kind and e.subject == subject:
                return e.id
        return None

    def discard_caches(self) -> None:
        self._barrier_cache.clear()

    # -- S33/S45.2/S66: THE ARTIFACT IS A CONTENT HASH OVER THE LOG. Rev 1 had none, and it is
    # the one execution artifact the architecture names as its done-condition.
    def new_draw(self) -> int:
        """S33's draw ordinal. Reset at the start of every tick by `season()`."""
        self.draw += 1
        return self.draw

    def content_hash(self) -> str:
        h = hashlib.blake2b(digest_size=16)
        for e in self.log:
            h.update(f"{e.id}|{e.kind}|{e.subject}|{e.emitted_at}|{e.degree}|"
                     f"{','.join(e.causes)}".encode())
            for c in e.changes:
                h.update(f"~{c.subject}|{c.mode}|{c.driver}|{c.field}|{c.delta}".encode())
        return h.hexdigest()

    # -- S43: resolution AT BOOT, by string. A missing provider is a STARTUP FAILURE WITH A
    # NAME IN IT, not a null three seasons into a campaign.
    def boot(self, required_roles: tuple[str, ...]) -> None:
        missing = [r for r in required_roles if r not in self.manifest]
        if missing:
            raise NoProducer(
                f"role(s) {missing} have no provider in the manifest", "S43",
                needs="a registry row naming a role and its provider",
                law="S43 -- the engine names the ROLE; the registry names the MODULE; RESOLUTION HAPPENS BY STRING AT BOOT. A missing provider is a startup failure with a name in it. THE MANIFEST IS THE SEAM; A PATH LITERAL IN A BODY IS NOT")


# ===========================================================================
# S17 -- QUERY. THE SIDE COLUMN IS THE ENFORCEMENT.
# ===========================================================================

class Query:
    # ---- resolver-side: World FIRST, always -----------------------------
    @staticmethod
    def parent_of(w: World, rung_id: str) -> Optional[str]:
        for t in w.tenures:
            if t.kind == "contain" and t.subject == rung_id and t.live:
                return t.object
        return None

    @staticmethod
    def descendants(w: World, rung_id: str) -> list[str]:
        """S6.1 -- the CONTAINMENT TREE and only it. S38.1: ITERATIVE, with a visited set --
        the reference graph is cyclic ON PURPOSE and a tree walk hangs on the NORMAL case."""
        TRACE.query("descendants", "resolver")
        out, seen, stack = [], {rung_id}, [rung_id]
        while stack:
            cur = stack.pop()
            for t in w.tenures:
                if t.kind == "contain" and t.object == cur and t.live and t.subject not in seen:
                    seen.add(t.subject); out.append(t.subject); stack.append(t.subject)
        return out

    @staticmethod
    def r1_aggregate(w: World, rung_id: str, over: Callable[[str], int]) -> int:
        """R-1: COMPUTE ON DEMAND over DESCENDANTS. Never received, never stored. S22.4 cl.3:
        LIVE EDGES ONLY. S6.2: this is a claim about the CONTAINMENT TREE."""
        TRACE.query("r1_aggregate", "resolver")
        return sum(over(d) for d in Query.descendants(w, rung_id))

    @staticmethod
    def aggregate_guard(w: World, name: str, *, per_person_tally: bool = False,
                        over_ended_edges: bool = False) -> None:
        """S22.4 -- THE AGGREGATION BOUNDARY.

        REV 2 HONESTY NOTE. S22.4 clause 2 is a READ-SIDE rule and is therefore checkable by
        GREPPING THE RESOLVER for a Query crossing holders -- a static check, not a runtime one.
        This function is the runtime half and THE CALLER VOLUNTEERS ITS OWN VIOLATION, which
        detects nothing on its own. `commit_count_guard` below is the part that actually
        detects, because it inspects the edge set rather than trusting a flag."""
        if per_person_tally:
            raise Forbidden(
                f"resolver-side Query '{name}' aggregates per-person tallies ACROSS HOLDERS",
                "S22.4", law="L3 clause 2 -- THAT IS STORED, MONOTONE, NEVER-DECAYING UNREST IN ALL BUT NAME -- worse than the field L3 banned, because the banned field could at least go down")
        if over_ended_edges:
            raise Forbidden(
                f"Query '{name}' composes over ENDED edges and is monotone", "S22.4",
                law="L3 clause 3 -- any Query monotone in the ENDED-edge set is a ratchet and is REFUSED. `count{commit}` over live AND ended rows is monotone; `count{hold: until != null}` is revocations-ever; each is built only from 'structural' edges and each EVADES clause 2")

    @staticmethod
    def single_holder_counter(w: World, person: str, axis: str, registry: set[str]) -> int:
        """L3 CLAUSE 1 -- and rev 4 exists because revisions 1-3 refused what this clause
        EXPLICITLY PERMITS.

        The head, verbatim: *"a monotone counter exists ONLY per `(Person, axis)` where `axis`
        is on a closed registry"*, and its own note calls such a counter **"legal, since every
        increment is in the holder's own ledger"**. Clause 2 bars only the CROSS-HOLDER SUM.

        Revisions 1-3 routed every "a character's risk builds up quietly" row to a probe that
        raised clause 2 -- on a need that never crosses a holder. It was THE LARGEST SINGLE
        BLOCKER IN THE CORPUS (18 cases), and it was the instrument measuring AGAINST the
        design, which S0.1 point 4 rules is no more acceptable than flattering it.

        What is genuinely missing is narrower and is what this raises: THE CLOSED REGISTRY."""
        TRACE.query("single_holder_counter", "resolver")
        if not registry:
            raise Unspecified(
                f"the closed `axis` registry L3 clause 1 requires (asked for '{axis}')",
                "S22.4",
                needs="a closed roster of axes, and a write-matrix row admitting the increment",
                law="L3 clause 1 permits a monotone counter PER (Person, axis) -- 'legal, since every increment is in the holder's own ledger' -- but ONLY where `axis` is ON A CLOSED REGISTRY. No such registry exists in the chain, and no S30 row admits the write. S54 item 6 adds that the axis must not be spelled `exposure` bare, or it collides with the need scalar",
            )
        if axis not in registry:
            raise Forbidden(f"axis '{axis}' is not on the closed registry", "S22.4",
                            law="L3 clause 1 -- ONLY where `axis` is on a closed registry")
        return sum(1 for c in w.persons[person].ledger if c.predicate == axis)

    @staticmethod
    def commit_count_guard(w: World, edges: list[Tenure], name: str) -> int:
        """The DETECTING half of clause 3: it looks at the rows, not at a flag."""
        ended = [t for t in edges if not t.live]
        if ended:
            raise Forbidden(
                f"aggregate '{name}' composed over {len(ended)} ENDED edge(s)", "S22.4",
                needs="filter to until == null before summing",
                law="L3 clause 3 -- ended Tenures PERSIST as historical claim subjects (S15.2), so a count over live AND ended rows is monotone non-decreasing. That is a ratchet built entirely out of 'structural' edges")
        return len(edges)

    @staticmethod
    def lateral(w: World, name: str, kind: str) -> list[Tenure]:
        """S6.2/S38 -- THE LATERAL GRAPH. Not governed by R-1/R-2. Resolver-side, World first,
        therefore unreachable from choose() BY CONSTRUCTION."""
        TRACE.query(f"lateral:{name}", "resolver")
        return [t for t in w.tenures if t.kind == kind and t.live]

    @staticmethod
    def verbs(w: World, site: Site, floors: dict[str, int]) -> set[str]:
        """S12.1 -- condition GATES VERBS. The comparison is on a SUMMED FIXED-POINT INT."""
        TRACE.query("verbs", "resolver")
        return {v for v, floor in floors.items() if site.condition >= floor}

    @staticmethod
    def hold_force(w: World, obj: str) -> Optional[Tenure]:
        """S15 -- `hold` is 1 PER OBJECT. S54 item 20's lawful form rests on this cardinality."""
        live = [t for t in w.tenures if t.kind == "hold" and t.object == obj and t.live]
        if len(live) > 1:
            raise Forbidden(f"{len(live)} live `hold` Tenures on {obj}", "S15",
                            law="S15 -- `hold` cardinality is 1 PER OBJECT")
        return live[0] if live else None

    @staticmethod
    def judging_set(w: World, rung_id: str) -> list[str]:
        raise Unspecified("judging_set_rule", "S61", needs="who decides at a sitting",
                          law="S61 -- NOTHING IS DECIDED AT A SITTING. T5's 'filtered at a rung' runs straight through it, and S10.2's 'arrangements, not choices' cannot be confirmed until it is")

    @staticmethod
    def presence(w: World, rung_id: str) -> list[str]:
        """S28 -- the PRESENCE INDEX the global fan-out reads."""
        TRACE.query("presence", "resolver")
        return [t.subject for t in w.tenures
                if t.kind == "contain" and t.object == rung_id and t.live
                and t.subject in w.persons]

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
    def opening_set(p: Person, v: View, q: Question) -> list[Candidate]:
        """§F1 -- COMPUTED FROM THE VERB TABLE. No `roster` parameter: that is `D2` entire.

        ⚠ WHAT CHANGED, AND WHY IT COULD NOT CHANGE BEFORE. Rev 2 took `roster: list[Candidate]`
        and returned it, and said so: "the PROPERTY S17 chose the type to protect -- an option set
        that is COMPUTED rather than an AUTHORED LIST -- is not [faithful], because `roster` is the
        caller's authored list." Its reason was real: §61 gave `q` no producer, so there was
        nothing to compute a set FROM. `questions_for()` is that producer, so the roster's excuse
        is gone and with it the roster.

            { Candidate(verb, subject, why) :
                verb    in the verb table                            -- clause 1
              , eligibility(verb, p) holds                           -- clause 2
              , subject in referents(q)                              -- clause 3
              , requires(verb) not KNOWN-FALSE from p's OWN claims }  -- clause 4

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
                if belief_contradicts(p, row, subject):
                    continue
                out.append(Candidate(verb, subject, why=q.source))
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
        gated = (row.requires or "").strip() in NO_PRECONDITION or v in REQUIRES_PREDICATES
        effected = not row.writes or v in EFFECTS
        # ⚠ AND A THIRD GATE: A VERB THAT CONTESTS DOES NOT TAKE THE EFFECT PATH AT ALL.
        # `ARCHITECTURE_V2.md:394` — *"`contests: <prize>` — if set, ROUTES TO THE SEAM at
        # RESOLVE (§39)"* — so such a verb is executable only if the SEAM can return, and today
        # `contest()` raises `Unspecified` at S39.4 (*"the degree ladder's margin model"*, `H-31`)
        # before it returns anything. So `kill / wound` is NOT executable, and it was counted as
        # executable only because the instrument read its own `EFFECTS` entry and never read the
        # column that says the effect is not the path. Jordan, 2026-09-02: *"you can't just kill
        # or wound imo."* Correct, and the design agreed at `:434` all along.
        # `W7` is the item that makes the seam return; this line is what will admit the verb again.
        contested = bool(row.contests)
        if gated and effected and not contested:
            out.add(v)
    return frozenset(out)


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
        cands = Query.opening_set(p, v, q)
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
        return pack_scenes(p, ranked, ask_budget(), fx, mint)
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


def belief_contradicts(p: Person, row: "VerbRow", subject: str) -> bool:
    """§F1 clause 4 -- is `requires(verb)` KNOWN-FALSE from `p`'s OWN claims?

    ⚠ THE ASYMMETRY IS THE WHOLE POINT AND MUST NOT BE SOFTENED TO "requires holds". This returns
    True only when the person HOLDS A CLAIM THAT CONTRADICTS the requirement. Having no belief
    either way is NOT a contradiction, so the Candidate forms, the person acts on a false premise,
    and the fold refuses them -- which is §F1's "a person who *wrongly* believes the granary full
    still forms the Candidate ... That is T3 and L2 working."

    Jordan, 2026-09-02: *"we can't control how others perceive and interpret our words or
    actions"* and *"our understanding of all other words and actions is subjective and singular."*
    A filter on world truth would be `choose` reading the world; this reads one person's ledger.

    The contradiction test is a claim about THIS subject whose value is falsy for the predicate
    the verb's `requires:` names. `H-72` registers the mapping from a `requires:` note to a
    predicate: the verb table states requirements as PROSE, so which predicate a requirement is
    about is not mechanically derivable, and inventing that mapping is what §42.2.1 forbids."""
    req = (row.requires or "").strip()
    if req in NO_PRECONDITION:
        return False
    for c in p.ledger:
        if c.subject == subject and c.predicate in PERSON_PREDICATES and c.value is False:
            return True
    return False


def questions_for(w: World, p: Person) -> list[Question]:
    """§F1's `q` producer -- FOUR sources, resolver-side, at the DELIBERATE barrier.

    ⚠ THIS CLOSES `H-04` AND §61's `NoProducer`, which between them blocked every NPC case: with
    no producer for `q`, `assemble(person, question)` was UNSATISFIABLE and DELIBERATE had no
    declared entry point, so `opening_set` had nothing to compute a set FROM. That is why the
    instrument needed an authored `roster` -- `D2`.

    ⚠ V2 §F1 SAYS "EXACTLY THREE SOURCES, AND BY NOTHING ELSE" AND IS WRONG BY ONE. PLAN `W5`
    adds **Q4 `need`** (#353 `:509`, `:605`, `:1297`): a live `commit` to an OUGHT Proposition
    generates a standing question every season. Without it "an NPC with a standing ambition and a
    quiet season forms no candidates at all", which is most of the NPC corpus -- a person with a
    goal and no inbox would simply not act. The sources are `rosters.yaml`'s `question_sources`,
    IN ORDER, because a budget-bounded person answers the earlier ones first.

    Resolver-side by construction: it takes a `World`. §F1 says all four are "already produced by
    the loop" -- no new step, no new carrier, no clock -- and that is what this reads."""
    TRACE.query("questions_for", "resolver")
    out: list[Question] = []
    mine = {t.object for t in p.tenures if t.live}

    # Q1 -- a Date coming due whose DocketItem names a matter, for every person in its judging set.
    for did, d in sorted(w.dates.items()):
        if d.get("due_at", 1 << 30) <= w.tick and not d.get("fired"):
            if d.get("holder") in (p.id, None) or d.get("holder") in mine:
                items = [it for it in w.docket if it.get("date") == did]
                refs = tuple(sorted({str(it.get("matter")) for it in items if it.get("matter")}))
                out.append(Question(f"q:date:{did}", "date_due", refs or (did,), did))

    # Q2 -- a claim landing in p's OWN ledger whose subject is p, something p holds, or a
    # Proposition p has committed to. `since_tick` is the season boundary: "landing" is new.
    # ⚠ THE PREVIOUS SEASON'S WITNESS, NOT THIS ONE'S. §F1 Q2 is "a claim LANDING in the
    # holder's ledger AT WITNESS", and WITNESS runs at the END of a season: the deposit is
    # stamped `when = t` and DELIBERATE reads it at `t + 1`. Testing `c.when == w.tick` therefore
    # matched nothing, ever — Q2 was dead for every person in every season, which is half of why
    # nothing propagated. Found by running `headless.py` and reading the ledgers.
    landed = w.tick - 1
    for c in p.ledger:
        if c.when == landed and (c.subject == p.id or c.subject in mine):
            out.append(Question(f"q:claim:{c.id}", "claim_landed", (c.subject,), c.id))

    # Q3 -- a Sensation band change: `subsistence` crossing a floor since last season. The
    # crossing is D22's emission, read person-side; the loop records them on `w.crossings`.
    for who, what, *_rest in w.crossings:
        if who == p.id:
            out.append(Question(f"q:band:{what}", "band_crossed", (what,), what))

    # Q4 -- `need`. A live `commit` Tenure whose object is an OUGHT Proposition is a STANDING
    # question: it recurs every season until the commitment ends, which is what makes an NPC with
    # an ambition act in a quiet season.
    for t in p.tenures:
        if t.kind == "commit" and t.live:
            prop = w.propositions.get(t.object)
            if prop is not None and str(prop.mood).upper() == "OUGHT":
                out.append(Question(f"q:need:{t.object}", "need",
                                    (prop.subject,), t.object))

    order = {src: i for i, src in enumerate(QUESTION_SOURCES)}
    out.sort(key=lambda q: (order[q.source], q.id))
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


def pack_scenes(p: Person, ranked: list, n_scenes: int, fx: "Fixtures", mint) -> list:
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
        return Scene(mint(p.id, "scene", str(n)), p.id,
                     [Act(mint(p.id, c.verb, c.subject or ""), p.id, c.verb) for c in chunk],
                     # `H-77`: a scene carrying more than one interaction is the EXTENDED one.
                     # This is what `extended` MEANS, and until W17's adversarial pass nothing
                     # ever set it -- so `Scene.cost` returned 1 unconditionally, H-77's sweep
                     # could not move any verdict, and the row passed R2 while being
                     # unexecutable. That is the laundering R2 exists to stop, in the row that
                     # was added the same day the rule was written.
                     extended=len(chunk) > 1)

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


def claim_subjects(e: "Event", rule: str) -> list:
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
    return out or [e.subject]


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
    return any(t.kind == "hold" and t.subject == pid and t.object == e.subject and t.live
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

class Ineligible(ShapeGap):
    """The actor is not eligible for this verb. Not a gap in the design -- a fact about the actor
    -- so it EMITS rather than raising, per §E2's 'failure emits, never raises'."""
    kind = "INELIGIBLE"


# A `requires:` predicate. The table states preconditions in PROSE, which the fold cannot read --
# the same defect `resolve` had, one column along. A verb with a prose precondition and no
# predicate here REFUSES, naming what is missing, rather than silently succeeding.
REQUIRES_PREDICATES: dict = {}


def requires_predicate(verb: str):
    def deco(fn):
        REQUIRES_PREDICATES[verb] = fn
        return fn
    return deco


# ---------------------------------------------------------------------------
# THE GOVERNANCE SLICE. Jordan, 2026-09-02, asked for governance and management across scales of
# governing bodies. The verbs for it ALREADY EXIST -- all eight `binding_decision` rows -- and not
# one of them executed, because each states its precondition in PROSE. So `post_remit` and
# `chronicle`, two of `W6`'s five witness channels, could never fire: both need a binding decision
# and no binding decision could happen.
#
# ⚠ A FACTION DOES NOT ACT. `ARCHITECTURE_V2.md:93` puts *"a faction acting as an actor"* in its
# REFUSAL table at `L1`, with three corpus cases that wanted it, and `H-21` completes it -- *"a
# faction's treasury is matter at the rung or office that holds it"*. Governance at a scale above
# the person is A PERSON HOLDING AN OFFICE acting at a rung, which is what these four do.
# ---------------------------------------------------------------------------

def title_domain(post: Optional[str]) -> Optional[str]:
    """The rung kind a title governs, from `rosters.yaml: titles`. `None` for a post that is not
    a title — a Dicastery is an office, not a rank."""
    return TITLE_DOMAINS.get(str(post or ""))


def title_rank(post: Optional[str]) -> int:
    """A title's rank as its domain's ordinal in `rung_kinds`. Higher governs wider.

    ⚠ RANK IS NOT A SECOND LADDER. `rung_kinds` is already ordered person → realm, and each title
    names the rung kind it governs, so the ordering falls out of a roster that exists rather than
    from a number somebody assigns. `-1` for a non-title."""
    dom = title_domain(post)
    return -1 if dom is None else (list(RUNG_KINDS).index(dom)
                                              if dom in RUNG_KINDS else -1)


def in_holdings(w: "World", actor: str, rung: Optional[str]) -> bool:
    """Is this rung one of the actor's HOLDINGS? A `hold` Tenure whose object is a RUNG.

    ⚠ HOLDINGS ARE NOT GOVERNING AUTHORITY, AND JORDAN RULED THE DIFFERENCE OPERATIONAL:
    *"King/Queen cannot revoke title of Duke/Duchess if they do not have duchy is in their
    holdings. King/Queen can revoke title of Duke/Duchess if the duchy is one of their
    holdings."* So a king with governing authority over the whole realm still cannot unmake a
    duke whose duchy he does not hold — which is the same ruling as *"they do not necessarily
    have all territories/provinces/duchies in their holdings"*, made mechanical.

    ⚠ NO NEW TENURE KIND, AND NOT EVEN A NEW OBJECT CLASS. `hold` is already polymorphic over an
    office and over a Record (§13) — and a `hold` WHOSE OBJECT IS A RUNG ALREADY EXISTED in the
    corpus before this function did: probe `F2` writes one at `probes.py:978` and `:985`, holding
    the settlement `S`. So this names a shape the tree was already using rather than adding one,
    and `tenure_kinds` does not move (§8).

    ⚠ THE ORIGINAL WORDING ALSO CITED *"a store"* AS AN EXISTING INSTANCE, AND THAT WAS
    UNSUPPORTED — no `hold` Tenure over a store is constructed anywhere in the instrument.
    Corrected rather than kept, because the sentence's whole job is to say what the tree already
    does. Found by the governance-canon adversarial pass.

    ⚠ AND THE NARROW CLAIM WAS THE WRONG THING TO CHECK. *`tenure_kinds` does not move* is true
    and proves nothing about the READERS: `Query.budget` counts every live `hold` as an office, so
    a landholding buys scene actions, and `_ch_document_key` makes a landholder a witness of every
    Event whose subject is their rung. Both pre-date this function; registered as `H-92`."""
    if rung is None or rung not in w.rungs:
        return False
    return any(t.kind == "hold" and t.subject == actor and t.object == rung and t.live
               for t in w.tenures)


def under_purview(w: "World", actor: str, holding: Optional[str]) -> bool:
    """Is `holding` under the governing authority of a title `actor` holds?

    ⚠ JORDAN, 2026-09-02: *"a Duke can revoke office from any individual in that office so long as
    that office is for a holding under their purview."* So authority over a governance act is
    **RANK + CONTAINMENT** — the actor holds a title whose domain contains the holding — and NOT
    `remit:<act>` on the particular office. That is a different eligibility model from the one
    Part E states, and the difference is registered rather than resolved here (`H-90`).

    ⚠ GOVERNING AUTHORITY, NOT SOVEREIGNTY AND NOT OWNERSHIP. Jordan, same ruling: a King *"may
    have governing authority over the country"* yet hold neither sovereign power over it nor all
    of it in their holdings. This function answers the FIRST question only; the tree models
    neither of the other two."""
    if holding is None:
        return False
    # ⚠ EVERY SEAT, NOT THE FIRST. This read `next((... for t in w.tenures ...), None)` and took
    # whichever title-hold appeared first in an INSERTION-ORDERED list, which was wrong twice
    # over. `Office.rung` is Optional (the office-cluster case, S6.2), and the generator YIELDED
    # `None` as a value -- so a title office with a null rung ended the scan and returned False,
    # and a Duke who was also made a King LOST PURVIEW OVER HIS OWN DUCHY. And a person holding
    # two titles got whichever the tenure list happened to hold first: a Count of P who is also
    # Duke of D was refused purview over D, or over P, depending on insertion order.
    #
    # It is a DISJUNCTION over the seats: authority over a holding is authority from ANY title the
    # actor holds. Taking the highest-ranked seat instead would be the same bug wearing a better
    # argument -- a Duke of D who is also Count of an unrelated P would lose P. Found by the
    # governance-canon adversarial pass.
    for seat in [rung for _, rung in titles_held(w, actor) if rung is not None]:
        # containment walks UP from the holding: a duchy's province is under the duke, a duchy's
        # neighbour is not.
        seen, cur = set(), holding
        while cur is not None and cur not in seen:
            if cur == seat:
                return True
            seen.add(cur)
            cur = Query.parent_of(w, cur)
    return False


def titles_held(w: "World", actor: str) -> list:
    """Every TITLE this person holds, as `(post, rung)`. THE SINGLE OWNER of the question *what
    does this person govern* -- `under_purview` reads it for containment and `highest_title_rank`
    for rank, so the two cannot drift into different answers about the same person (§8)."""
    out = []
    for t in w.tenures:
        if t.kind == "hold" and t.subject == actor and t.live and t.object in w.offices:
            o = w.offices[t.object]
            if title_domain(o.post) is not None:
                out.append((o.post, o.rung))
    return out


def highest_title_rank(w: "World", actor: str) -> int:
    """The best rank this person holds, or `-1` for someone holding no title at all.

    ⚠ THIS IS WHAT MAKES `title_rank` LOAD-BEARING. Until the governance-canon pass, `title_rank`
    had no caller outside its own test: the ladder was asserted and then decided nothing, which is
    §0.05's reference-wearing-mechanism's clothes. It decides a revocation now."""
    return max((title_rank(post) for post, _ in titles_held(w, actor)), default=-1)


@requires_predicate("confer")
def _req_confer(w: "World", a: "Act") -> bool:
    """Part E, IN FULL: *"the office's **conferral basis**, and 1-per-object: no live `hold` on the
    object, **or** the holder-Proposition has zero live `commit` (§54 it. 20)"*.

    ⚠ THE FIRST VERSION IMPLEMENTED HALF OF ONE OF TWO CLAUSES -- it dropped the conferral-basis
    conjunct entirely and the `or` disjunct with it, while its docstring claimed *"the cardinality
    rule stated structurally"*. Dropping a disjunct is an OVER-REFUSAL: an office whose
    holder-Proposition has no live commit was refused where Part E admits it. `G4` weighs that
    equally with an invention, and the docstring made it invisible. Found by the governance-slice
    adversarial pass."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    obj = d.get("office")
    if not obj or obj not in w.offices:
        return False
    if not (w.offices[obj].conferral or "").strip():
        return False                       # no conferral basis: the office cannot be conferred
    if not any(t.kind == "hold" and t.object == obj and t.live for t in w.tenures):
        return True                        # 1-per-object satisfied
    # THE `or` DISJUNCT: a held office is still conferrable when the holder-Proposition carries
    # no live `commit`. §54 item 20.
    holder = next((t.subject for t in w.tenures
                   if t.kind == "hold" and t.object == obj and t.live), None)
    return holder is not None and not any(
        t.kind == "commit" and t.subject == holder and t.live for t in w.tenures)


@requires_predicate("revoke")
def _req_revoke(w: "World", a: "Act") -> bool:
    """Part E: *"the office's **revocation basis**, and a live `hold` exists"*.

    ⚠ THE FIRST VERSION DROPPED THE OFFICE CLAUSE AND WAS AN OVER-ADMISSION -- it scanned for any
    live `hold` on the payload's object with no check that the object IS AN OFFICE, and §13 makes
    possession of a Record a `hold` Tenure. So a holder of `remit:revoke` could revoke a person's
    possession of a book, and `_eff_revoke` would close it. Asymmetric with `confer`, which did
    check. Found by the governance-slice adversarial pass."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    obj = d.get("office")
    if not obj or obj not in w.offices:
        return False
    if not (w.offices[obj].revocation or "").strip():
        return False
    # ⚠ TWO RULES, AND WHICH ONE APPLIES TURNS ON WHETHER THE TARGET IS A TITLE.
    #
    # An ORDINARY office — a governor, a council seat — is revocable by GOVERNING AUTHORITY.
    # Jordan, 2026-09-02: *"a Duke can revoke office from any individual in that office so long as
    # that office is for a holding UNDER THEIR PURVIEW."* Rank plus containment.
    #
    # A TITLE is revocable only from HOLDINGS. Jordan, same exchange: *"King/Queen cannot revoke
    # title of Duke/Duchess if they do not have duchy is in their holdings. King/Queen can revoke
    # title of Duke/Duchess if the duchy is one of their holdings."* So a king with governing
    # authority over the entire realm STILL CANNOT unmake a duke whose duchy he does not hold.
    # This is the distinction he drew at the start — governing authority, sovereign power and
    # holdings are three different things — arriving as a branch rather than as prose.
    #
    # ⚠ AND PURVIEW ALONE WOULD HAVE BEEN WRONG HERE. The first version applied `under_purview` to
    # every revocation, so a king could strip any duke in his realm. That is exactly the reading
    # the ruling exists to forbid.
    target_is_title = title_domain(w.offices[obj].post) is not None
    domain = w.offices[obj].rung
    if target_is_title:
        # ⚠ A CONJUNCTION, AND THE FIRST VERSION WAS A SINGLE TERM. It tested `in_holdings`
        # ALONE, which makes holdings SUFFICIENT — so a Dicastery clerk who happened to hold a
        # duchy could unmake its Duke, and a Duke holding the realm could unmake the King. That is
        # the MIRROR of the defect it was written to fix: the version before it conflated governing
        # authority with holdings in one direction, and this conflated them in the other. Jordan's
        # message states a NECESSARY condition on someone who already has the authority —
        # *"King/Queen CANNOT revoke title of Duke/Duchess IF they do not have duchy is in their
        # holdings"* — and message 1 separates the two concepts on purpose. Both terms,
        # therefore, plus rank: the whole point of *"they do not necessarily have sovereign power"*
        # is that holding the land is not the same as outranking the person who governs it. Found
        # by the governance-canon adversarial pass.
        if not under_purview(w, a.actor, domain):
            return False                       # governing authority over the domain
        if not in_holdings(w, a.actor, domain):
            return False                       # AND the domain is one of the actor's holdings
        if highest_title_rank(w, a.actor) <= title_rank(w.offices[obj].post):
            # AND strictly higher rank — which also forbids revoking YOUR OWN title, an
            # equal-rank case nothing else in the branch excluded, and which a Duke who holds his
            # own duchy (the ordinary case) otherwise satisfied.
            return False
    elif not under_purview(w, a.actor, domain):
        return False
    #
    # ⚠ THIS IS A DIFFERENT ELIGIBILITY MODEL FROM THE ONE PART E STATES, AND CALLING IT A
    # COMPATIBLE NARROWING WAS WRONG — that is what this comment said, and it is false of
    # Jordan's text. *"a Duke can revoke office from any individual in that office SO LONG AS that
    # office is for a holding under their purview"* states a SUFFICIENT condition, so keeping Part
    # E's `remit:revoke` as a necessary one on top means a Duke whose office lacks the `revoke`
    # remit cannot revoke a governor inside his own duchy — an OVER-REFUSAL, which `G4` weighs
    # equally with an invention. It is a narrowing relative to PART E, never relative to the
    # ruling. The transcribed `eligibility:` column is not this item's to rewrite, so the conflict
    # is REGISTERED (`H-91`) and named here rather than resolved by a quiet table edit.
    return any(t.kind == "hold" and t.object == obj and t.live for t in w.tenures)


@requires_predicate("dispatch")
def _req_dispatch(w: "World", a: "Act") -> bool:
    """Part E: *the named person exists*."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    return d.get("subject") in w.persons


@requires_predicate("convene")
def _req_convene(w: "World", a: "Act") -> bool:
    """Part E: *the venue's **container** resolves, or is NONE* (§6.2).

    ⚠ THE FIRST VERSION TESTED THE WRONG THING -- `venue in w.rungs` asks whether the venue IS a
    rung, not whether its CONTAINER resolves, so a top rung (which has no container) passed. And
    `Query.parent_of` already existed, so re-deriving a weaker test here was §8-adjacent. Found by
    the governance-slice adversarial pass."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    venue = d.get("venue")
    if venue is None:
        return True                        # §6.2's carve-out
    return venue in w.rungs and Query.parent_of(w, venue) is not None


@requires_predicate("transfer")
def _req_transfer(w: "World", a: "Act") -> bool:
    """#353 §54 item 7: `stores(hearth(giver), kind) >= amount`. THIS IS THE SCARCITY PREDICATE --
    §27.1's whole argument rests on it: the second claimant on an emptied granary gets a DIFFERENT
    Event, and it falls out of the fold because each act sees the world its predecessors left."""
    give = (a.payload or {}) if isinstance(a.payload, dict) else {}
    rung = w.rungs.get(give.get("from", ""))
    kind, amount = give.get("kind", "grain"), give.get("amount", 1)
    return bool(rung and (rung.stores or {}).get(kind, 0) >= amount)


@requires_predicate("tell")
def _req_tell(w: "World", a: "Act") -> bool:
    """§E3: *"the teller holds a claim on the subject"*.

    ⚠ IT READS THE TELLER'S OWN LEDGER, NOT THE WORLD'S TRUTH, and that is the whole of T3. A
    person may tell what they wrongly believe -- the precondition is that they HOLD a claim, not
    that the claim is true -- so a liar and a mistaken witness both pass it and the distortion
    lands at the receiver's WITNESS deposit. Jordan, 2026-09-02: *"we can't control how others
    perceive and interpret our words or actions"*, and `H-36` closed receiver-side for the same
    reason. A predicate that checked the world here would put the refusal on the wrong side."""
    d = a.payload if isinstance(a.payload, dict) else {}
    subj = d.get("subject")
    teller = w.persons.get(a.actor)
    if teller is None or subj is None:
        return False
    return any(c.subject == subj for c in teller.ledger)


@requires_predicate("move")
def _req_move(w: "World", a: "Act") -> bool:
    """§E3: *a `contain` path exists*. #353 §15 types `contain : Rung -> Rung` with ONE parent, so
    a path exists when the mover's own rung is on the containment ladder. The DESTINATION is the
    act's payload where it names one; where it does not, the ladder's existence is what the fold
    can check without inventing a route."""
    here = w.rungs.get(a.actor)
    if here is None:
        return False
    return any(t.subject == a.actor or t.subject == here.id
               for t in w.tenures if t.kind == "contain") or here.kind == "person"


@requires_predicate("work")
def _req_work(w: "World", a: "Act") -> bool:
    """§12.1: `condition >= floor(verb)`. The floors are `H-08` and come from Fixtures, swept.
    ⚠ THE FIRST VERSION CHECKED `condition >= 0`, WHICH IS EVERY POSSIBLE CONDITION. A predicate
    that cannot fail is not a predicate — it is a `return True` with a docstring, and §0.1 point 2
    calls that an assertion that cannot observe the failure it excludes. The floors come from
    `Fixtures`, which RAISES on an unregistered site kind rather than defaulting, so an unswept
    floor cannot slip in silently."""
    for ch in a.changes:
        site = w.sites.get(ch.subject)
        if site is None:
            continue
        floors = w.fixtures.get("band_floors").get(site.kind)
        if floors is None:
            raise Unspecified(
                f"no band floors for site kind {site.kind!r}", "S12.1",
                needs="a per-kind floor table -- register row H-08",
                law="§12.1 gates verbs on `condition` against per-kind FLOORS, and §42.2.1 "
                    "forbids picking a plausible number for a kind nobody registered")
        return site.condition >= min(floors.values())
    return True


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
        f = _HERE.parent.parent / "2026-09-01-holonic-architecture" / "ARCHITECTURE.md"
        _S353_CACHE.append(f.read_text() if f.exists() else "")
    return _S353_CACHE[0]

NO_PRECONDITION = ("—", "-", "")


# ---------------------------------------------------------------------------
# THE EFFECTS. One per verb, OWNED BY THE RESOLVER.
#
# ⚠ PART E's `writes:` COLUMN NAMES THE CELL AND NEVER THE VALUE. `transfer` writes
# `(Rung, stores)` -- it does not say BY HOW MUCH, or that the giver's store goes DOWN. Without
# that the fold checks a precondition, emits, and changes nothing, so `transfer` twice from a
# one-unit larder succeeds twice: the scarcity §27.1 rests on never happens.
#
# THE DISTINCTION FROM THE `effect` PARAMETER W3 REMOVED IS THE WHOLE POINT, and it is §27.2's.
# A CALLER-supplied lambda is a second resolver: every caller may disagree about what a verb does,
# and each probe did. A VERB-KEYED effect registered here is the resolver's BODY -- one
# implementation, the same for every caller, and a verb with a `writes:` and no effect REFUSES
# rather than silently writing nothing.
#
# This gap is register row H-63.
# ---------------------------------------------------------------------------
EFFECTS: dict = {}


def effect_for(verb: str):
    def deco(fn):
        EFFECTS[verb] = fn
        return fn
    return deco


# --- THE GOVERNANCE SLICE'S EFFECTS. `dispatch` needs none: Part E gives it `writes: []`, so an
# order is an EMISSION and nothing else, which is `L1` in one row -- a dispatch does not move a
# person, it tells one, and whether they go is their own act next season.

@effect_for("confer")
def _eff_confer(w: "World", a: "Act") -> list:
    """Seats an office: a new `hold` Tenure opens, and any prior holder's closes.

    ⚠ AN EFFECT MUTATES AND RETURNS THE IDS IT TOUCHED; IT DOES NOT CALL `w.write`. The fold
    calls it INSIDE the gate's `apply()`, once, for all of the row's `writes:` — so a nested
    `w.write` is a write inside a write, and returning `None` tells the fold nothing was touched,
    which makes it emit the REFUSAL. My first version did both, and the fold correctly refused an
    act whose state change had in fact happened. `_apply_write`'s docstring states the contract."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    obj, to = d.get("office"), d.get("to") or a.actor
    if not obj or obj not in w.offices:
        return []
    closed = []
    for t in w.tenures:
        if t.kind == "hold" and t.object == obj and t.live:
            t.until = w.tick
            closed.append(t.id)
    nt = Tenure(H(w.world_seed, w.tick, to, f"hold:{obj}"), to, obj, "hold", w.tick)
    w.add_tenure(nt)
    # ⚠ PER-KIND. Conferring onto an UNHELD office closes nothing, and returning a flat list made
    # the fold publish `tenure.closed` anyway -- a state change that did not happen, which is the
    # fabricated-`person.died` class committed inside the fix for it. The mapping's empty entry is
    # dropped by `_apply_write`.
    return {"tenure.opened": [nt.id], "tenure.closed": closed}


@effect_for("revoke")
def _eff_revoke(w: "World", a: "Act") -> list:
    """Unseats an office: the live `hold` closes. The mirror of `confer`, which is why the two are
    the pair that proves the slice — one opens what the other closes, on the same row."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    obj = d.get("office")
    touched = []
    for t in w.tenures:
        if t.kind == "hold" and t.object == obj and t.live:
            t.until = w.tick
            touched.append(t.id)
    return touched


@effect_for("convene")
def _eff_convene(w: "World", a: "Act") -> list:
    """Schedules a sitting: a Date comes due, with a ConveningCondition attached — Part E's two
    writes, both done by this one effect because the fold calls it once for the row.

    ⚠ A DATE IS A DICT HERE, not a class: `w.dates` is read as `d.get("due_at")` / `d.get("fired")`
    at CALENDAR. The first version built a `Date(...)` that does not exist.

    ⚠ WHAT THE SITTING THEN DECIDES IS `H-32` AND IS NOT HERE. `convene` puts a date on the
    calendar and stops, which is `L5`: a clock may not produce an outcome. `W7` is the item that
    makes the sitting decide."""
    d = (a.payload or {}) if isinstance(a.payload, dict) else {}
    when = int(d.get("when", w.tick + 1))
    did = H(w.world_seed, w.tick, a.actor, f"convene:{d.get('venue') or '-'}")
    date = w.dates.setdefault(did, {"id": did, "venue": d.get("venue")})
    date["due_at"] = when
    date["convening_attached"] = True
    return [did]


@effect_for("move")
def _eff_move(w: "World", a: "Act") -> None:
    """§D4 / #353 §15.1: travel is a TENURE ALTER, owned by the traveller as the Tenure's subject.
    The old leg closes and a new one opens; the destination rides on the payload where the act
    names one. ⚠ This is `H-63`: Part E's `writes:` names the three cells and never the values, so
    what a `move` DOES is stated here rather than in the table — one implementation owned by the
    resolver, which is the distinction §27.2 draws against a caller-supplied lambda."""
    dest = (a.payload or {}).get("to") if isinstance(a.payload, dict) else None
    for t in w.tenures:
        if t.subject == a.actor and t.kind == "contain" and t.until is None:
            t.until = w.tick
    if dest:
        w.add_tenure(Tenure(H(w.world_seed, w.tick, a.actor, f"leg:{a.id}"),
                                a.actor, dest, "contain", since=w.tick))
    return [a.actor]


@effect_for("work")
def _eff_work(w: "World", a: "Act") -> None:
    """`work` alters `(Site, condition)` by the act's declared delta. The DELTA IS NOT APPLIED
    HERE -- §27.3 sums every delta across the fold and clamps ONCE, so applying it per act would
    make the clamp arrival-order dependent, which §32 forbids. The write goes through the gate so
    the class and Partition are checked; the value lands in the accumulator.

    ⚠ IT REPORTS THE SITE ANYWAY. The fold now refuses an act whose effect touched nothing, and
    `work`'s DELTA is deferred while its SUBJECT is not: the act is about that site, and saying
    so is what keeps the deferral from reading as a no-op."""
    d = a.payload if isinstance(a.payload, dict) else {}
    site = d.get("site") or next((x for x in sorted(w.sites)), None)
    return [site] if site else []


@effect_for("create_record")
def _eff_create_record(w: "World", a: "Act") -> None:
    """§E3: `create_record` writes `(Record, exists)` and `(Record, stages)`. `H-63` is why the
    VALUES are here and not in the table.

    ⚠ THE STAGES COME FROM THE ACT, NOT FROM A DEFAULT. #353 `:1043` (§54 item 14) makes the
    stage list ACT-DECLARED -- "the act DECLARES the stages and their terms" -- so an act that
    names none creates a record with none, and the instrument does not invent a ladder. That is
    what makes Carin's season the case `PLAN.md` §6.1 chose: a Record with act-declared stages is
    the largest ruled row in the corpus and nothing about it needs a default."""
    d = a.payload if isinstance(a.payload, dict) else {}
    rid = d.get("record") or f"rec:{a.id}"
    stages = list(d.get("stages") or [])
    if not stages:
        # `H-80`, DECLARED AND SWEPT. The act SHOULD declare these (#353 §13.1) and a computed
        # act cannot: §F1's Candidate is `(verb, subject, why)` with no operand channel. Refusing
        # instead would make `(Record, stages)` -- a Part D row -- unreachable from any person's
        # decision, so the honest form is §G's declare-default-sweep rather than either an
        # invention or a blocker. Each stage is `(due_tick, label, the act that wound the clock)`.
        n = w.fixtures.get("record_stages_default")
        term = w.fixtures.get("record_stage_term")
        stages = [(w.tick + (i + 1) * term, f"stage{i + 1}", a.id) for i in range(n)]
    w.records[rid] = Record(rid, d.get("rung") or a.actor, d.get("kind") or "text",
                            subject_matter=d.get("subject_matter"), stages=stages)
    # S13: possession is a `hold` Tenure owned by the holder, never a field on the Record. The
    # maker holds what they made until they part with it.
    w.add_tenure(Tenure(H(w.world_seed, w.tick, a.actor, f"hold:{rid}"),
                        a.actor, rid, "hold", since=w.tick))
    return [rid]


@effect_for("destroy_record")
def _eff_destroy_record(w: "World", a: "Act") -> None:
    """§E3: writes `(Record, exists)`. The Record goes, and every `hold` on it ends -- S15.3's
    rule that a tenure dies THROUGH the death of what it is over, never beside it."""
    d = a.payload if isinstance(a.payload, dict) else {}
    rid = d.get("record")
    if rid is None or rid not in w.records:
        return None
    del w.records[rid]
    for t in w.tenures:
        if t.object == rid and t.live:
            t.until = w.tick
    return [rid]


@effect_for("kill / wound")
def _eff_kill(w: "World", a: "Act") -> None:
    """§E3: writes `(Person, body)`, `(Person, exists)` and `(Tenure, until)`.

    ⚠ THE TENURE ENDS THROUGH THE DEATH, which is §15.3's rule and the reason this is ONE effect
    rather than three writes a caller sequences: "a plague that kills the praefect ends his
    tenure THROUGH THE DEATH; A STORM CANNOT TOUCH IT." A wound that does not kill writes only
    the band, so the same verb covers both -- which is why the table's row is `kill / wound`."""
    d = a.payload if isinstance(a.payload, dict) else {}
    who = d.get("subject")
    p = w.persons.get(who)
    if p is None:
        return None
    p.body = max(0, p.body - int(d.get("harm", p.body)))
    if p.body > 0:
        return None
    for t in list(p.tenures) + list(w._unowned):
        if (t.subject == who or t.object == who) and t.live:
            t.until = w.tick
    del w.persons[who]
    return [who]


@effect_for("utter")
def _eff_utter(w: "World", a: "Act") -> None:
    """§E3: writes `(Proposition, exists)`. §14: a Proposition is IDENTITY-BEARING AND IMMUTABLE,
    fixed at utterance and never destroyed -- `Proposition` is a frozen dataclass, so that is
    structural here rather than asserted."""
    d = a.payload if isinstance(a.payload, dict) else {}
    pid = d.get("proposition") or f"prop:{a.id}"
    if pid in w.propositions:
        return None                       # immutable: an utterance never overwrites one
    w.propositions[pid] = Proposition(pid, d.get("mood") or "OUGHT",
                                      d.get("subject") or a.actor,
                                      d.get("predicate") or "", d.get("value"), w.tick)
    return [pid]


@effect_for("transfer")
def _eff_transfer(w: "World", a: "Act") -> None:
    """§54 item 7's mirror: the giver's store goes DOWN and the receiver's goes UP.

    ⚠ THE FIRST VERSION ONLY DECREMENTED, and §E3 says `transfer` writes `(Rung, stores)` **×2**,
    one per side. A one-sided transfer ANNIHILATES MATTER -- six grain left the world and arrived
    nowhere, in an economy where `yield` is the only source (#353 `:856`). The scarcity proof still
    passed, because it only watched the giver: a run can be right about the thing it looks at and
    wrong about the world."""
    give = (a.payload or {}) if isinstance(a.payload, dict) else {}
    src = w.rungs.get(give.get("from", ""))
    dst = w.rungs.get(give.get("to", ""))
    kind, amount = give.get("kind", "grain"), give.get("amount", 1)
    if src is not None:
        src.stores = dict(src.stores or {})
        src.stores[kind] = src.stores.get(kind, 0) - amount
    if dst is not None:
        dst.stores = dict(dst.stores or {})
        dst.stores[kind] = dst.stores.get(kind, 0) + amount
    # BOTH SIDES, because §E3 says `transfer` writes `(Rung, stores)` twice -- one per side -- and
    # a one-sided report would make the Event name half of what it did.
    return [r.id for r in (src, dst) if r is not None]


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
                for n, a in enumerate(sc.acts):
                    TRACE.scene_act(p.id, a.verb, left, n + 1, len(sc.acts))
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

    def _fold(self, w: "World", a: Act) -> list[Event]:
        """ONE act through the table. This is what `effect` used to be, and the difference is
        that it is the SAME code for every act and every caller."""
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

        def ev(kinds, causes, changes=None):
            return [Event(H(w.world_seed, w.tick, a.actor, f"{k}:{a.id}"),
                          k, a.actor, list(changes or []), list(causes), w.tick)
                    for k in kinds]

        if not self._eligible(w, a, row):
            TRACE.decision(f"{a.actor} is not eligible for {a.verb}", "E4",
                           chose="emit the refusal", alternatives=["raise", "silently drop"])
            return ev(row.emits_on_refusal or ("act.ineligible",), [a.id])

        # `requires`, AGAINST THE WORLD THE PREDECESSORS LEFT -- which is the whole of §27.1.
        if row.requires.strip() not in NO_PRECONDITION:
            pred = REQUIRES_PREDICATES.get(a.verb)
            if pred is None:
                raise Unspecified(
                    f"{a.verb!r} has a precondition the fold cannot evaluate: {row.requires!r}",
                    "E2",
                    needs="a predicate in REQUIRES_PREDICATES, or a `requires:` the table states "
                          "structurally rather than in prose",
                    law="§E2 -- `requires` is checked IN THE FOLD. Stated as prose it is the same "
                        "defect `resolve` had, one column along: a rule the code cannot read")
            if not pred(w, a):
                TRACE.decision(f"{a.verb} by {a.actor}: precondition unmet", "E2/S27.1",
                               chose="emit the refusal -- scarcity falls out of the fold",
                               alternatives=["raise (no Event, no witness, no arc)"])
                return ev(row.emits_on_refusal or ("act.refused",), [a.id])

        # Each `writes:` through the gate. The gate is the only writer; the fold never assigns.
        changed: list = []
        # Which of `emits:` the effect actually earned. Empty means "all of them", which is the
        # contract every effect returning a plain list keeps.
        earned: set = set()
        if row.writes:
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
            for n, pair in enumerate(row.writes):
                kind, _, fld = pair.partition(".")
                # The effect runs ONCE, on the first pair: a verb writing three cells is ONE
                # operation, and running it per pair minted three Tenures for one `move`.
                made = self._apply_write(w, a, kind, fld, eff if n == 0 else None,
                                         earned=earned)
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
        kinds = tuple(k for k in row.emits if k in earned) if earned else row.emits
        return ev(kinds, [a.id], list(a.changes) + changed)

    def _apply_write(self, w: "World", a: Act, kind: str, fld: str, eff=None,
                     earned: Optional[set] = None) -> list:
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
            got = eff(w, a) if eff is not None else None
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
                r = contest(w, rung=(a.payload if isinstance(a.payload, str) else None) or "R",
                            prize=_contests[0],
                            claimants=[a.actor], depth=0, max_depth=contest_max_depth,
                            causes=[a.id])
                if isinstance(r, ContestError):
                    TRACE.note(f"contest returned {r}", "S39.3")
                else:
                    out.extend(r)
                continue
            # S27.1: CONTENTION IS AN ORDERED FOLD. Each act sees the world its predecessors
            # left. SEQUENCE, NOT SIMULTANEITY -- and NO ACT NEEDS TO KNOW ANOTHER EXISTED.
            produced = self._fold(w, a)
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
                             f"({'the specified behaviour' if mode == 'total' else 'a swept arm of H-33'})",
                       alternatives=[
                           "shard per rung (retired: made the parallelism claim unsound)",
                           "total (S61's specified behaviour, and H-33's control arm)",
                           f"the five channels {list(WITNESS_CHANNELS)}, each with the predicate "
                           "`rosters.yaml: witness_channel_predicates` injects"])

        # S28 stage 2: DEPOSIT IS PER-PERSON, into that person's OWN ledger and no other.
        cap = w.fixtures.get("ledger_cap")
        conf = w.fixtures.get("confidence_default")
        claim_rule = w.fixtures.get("claim_subject_rule")
        deposits = 0
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
            for n, subj in enumerate(claim_subjects(e, claim_rule)):
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
    contracts = _HERE.parent.parent.parent / "references" / "module_contracts.yaml"
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
                guess = _HERE.parent.parent.parent / "systems" / name / "sim"
                where = (f"systems/{name}/sim/" if guess.is_dir()
                         else f"(no `sim_module:` in module_contracts.yaml; "
                              f"`doc:` is {m.get('doc')!r} and is out of date)")
            return dict(module=name, resolver=m.get("resolver") or "undeclared", doc=where)
    raise Unspecified(
        f"`contest_subsystems` maps {prize!r} to {name!r}, which is in no module contract", "S39",
        needs="a module named in references/module_contracts.yaml",
        law="the roster may only name a subsystem the contracts file declares -- otherwise the "
            "dispatch target is invented")


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
        raise Unspecified(
            f"a contest for {prize!r} belongs to the `{_sub['module']}` subsystem "
            f"(resolver: {_sub['resolver']}), and nothing connects the seam to it", "S39",
            needs=f"the seam to call {_sub['module']} ({_sub['doc']})",
            law="Jordan 2026-09-02 -- a contest is a call for a different subsystem. The three "
                "are declared in references/module_contracts.yaml WITH resolvers, so the seam's "
                "job is to DISPATCH; inventing a degree ladder here would be a second resolver, "
                "which S27.2 names as its highest-value refusal")
    raise Unspecified(
        "the degree ladder's margin model",
        "S39.4",
        needs="a margin -- pool, obstacle, and the four band edges read off it",
        law="S39.4 -- ONE degree ladder for every scale, FOUR BANDS READ OFF THE MARGIN, never off the obstacle's size. No in-chain document supplies the margin model, and S27.2 refuses a second resolver, an auto-resolve formula and a fast path -- so a band computed here without a margin IS the second resolver",
    )
