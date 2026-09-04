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
        # ⚠ ROUTED THROUGH `get()`, AND THE BYPASS WAS LOAD-BEARING ON A GREEN CHECK. This read
        # `self._v` directly, so `self.reads` was never incremented and `claim_decay_per_season`
        # was INVISIBLE to R5 and to `W9`'s check 3 -- the two guards whose whole job is "no fill
        # off the register". Check 3 was green BECAUSE of the bypass: route the read properly and
        # it fails with `missing == ["claim_decay_per_season"]` unless the fixture is named in a
        # register row's `site:`. A guard that cannot see the thing it guards is not a weak guard,
        # it is an absent one (§0.1 point 2). Found by the adversarial pass.
        if "claim_decay_per_season" not in self._v:
            raise Ungraded(
                "claim confidence decay is not registered", "S42.2.1",
                needs="a `claim_decay_per_season` fixture row",
                law="S42.2.1 -- an unregistered rate must REFUSE, never answer plausibly")
        return self.get("claim_decay_per_season")

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
# `W-B` / `H-122`. WHO RECEIVES A CLAIM MINTED FROM WHAT THE FOLD READ. Bound at import
# like every other roster, and for the reason `TITLE_DOMAINS` records below: an unbound
# roster is the one whose absence goes unnoticed.
OBSERVATION_DEPOSIT_MODES = roster("observation_deposit_modes")
# ⚠ BOUND AT IMPORT LIKE THE OTHERS, AND THAT IS THE POINT. `titles` was the ONE roster read
# lazily through a bare `_ROSTERS.get(...) or {}`, so it alone got no existence refusal -- and
# because `_req_revoke` fails OPEN into purview-for-everything when the mapping is empty, the one
# unbound roster was the one whose absence silently restores a ruled-against behaviour.
TITLE_DOMAINS = roster_map("titles", "domains")

# ⚠ THE OFFICE'S THREE CANON AXES -- `H-99`, and they are BOUND AT IMPORT for the reason the
# comment above gives: an unbound roster is the one whose absence goes unnoticed. Jordan asked
# *"does the office schema include faction belonging, scale of office, type of office, etc?"* and
# it did not. `FACTIONS` is the belonging, `BODY_FACTION`/`BODY_FUNCTION` the type. SCALE is
# deliberately not here -- an office's scale is the RUNG it is seated at, which `Office.seat`
# already carries; a body does not fix a rung.
#
# ⚠ SOURCED UNDER THE 2026-09-02 PRECEDENCE RULING, WHICH `rosters.yaml`'s header states in full:
# `systems/world/` is CANON for identity/names/organizations, `systems/factions/` near-canon only
# where it concerns a faction's identity AND world is silent, `research/` reference. The first
# version of these rosters was sourced from the near-canon tier and carried a name that tier
# itself calls *"institutional infrastructure, not a faction"*.
FACTIONS = roster("factions")
BODY_FACTION = roster_map("office_bodies", "faction")
BODY_FUNCTION = roster_map("office_bodies", "function")
ROLE_TEMPLATE_OF = roster_map("role_templates", "by_faction")


def office_faction(body: str | None, declared: str | None) -> str:
    """The faction an office belongs to: DERIVED from its canonical body where it has one,
    authored where canon gives its faction no organ.

    ⚠ ONE AUTHORED FIELD, TWO DERIVED, AND A DISAGREEMENT REFUSES. `office_bodies` already binds
    every body to its faction, so an overlay that names a `body` need not -- and may not -- name a
    different faction. A `Cardinal of Justice` seated in the Crown is a mis-seating, and it is
    exactly the kind of error a re-scaling pass makes at volume; without this it would be silent
    and would then read as canon.

    ⚠ AN ABSENT BODY IS NOT AN ERROR. The Restoration Movement's authority is *"informal"*
    (`worldbuilding_v30.md` §8) and canon gives it no organ, so such a case authors `faction`
    directly. That is a real gap in canon, carried as one rather than filled."""
    if body is not None:
        if body not in BODY_FACTION:
            raise Unspecified(
                f"{body!r} is not a canonical body", "rosters.yaml -- office_bodies",
                needs="name a body from `systems/world/`, or drop `body` and author `faction`",
                law="Jordan 2026-09-02 -- systems/world is canon for organizations. Inventing a "
                    "body here would be indistinguishable from canon to the next session")
        derived = BODY_FACTION[body]
        if declared is not None and declared != derived:
            raise Forbidden(
                f"office body {body!r} belongs to {derived!r}, not {declared!r}",
                "rosters.yaml -- office_bodies",
                needs="drop the `faction:` field; it derives from `body:`",
                law="H-99 -- one authored field, two derived. A body's faction is canon's, and a "
                    "disagreement is a mis-seating rather than a second opinion")
        return derived
    if declared is None:
        raise Unspecified(
            "an office names neither a `body` nor a `faction`", "the case overlay",
            needs="name a canonical body, or the faction directly where canon gives it no organ",
            law="H-99 -- an office belongs to something. §42.2's polarity rule: no evidence of "
                "belonging is a refusal, never a default faction")
    if declared not in FACTIONS:
        raise Unspecified(
            f"{declared!r} is not a canonical faction", "rosters.yaml -- factions",
            needs="use a faction named in `systems/world/`",
            law="Jordan 2026-09-02 -- systems/world is canon for identity and names")
    return declared

# ===========================================================================
# THE `requires` GRAMMAR -- W-A. ONE DECLARATION, THREE READERS.
#
# `04_CODE_ARCHITECTURE.md` §F.24a: *"`F.24` said 'assumed: a small typed predicate grammar' and
# supplied none, which is the shape of handing a property forward. The 32 `requires` cells in the
# executable chain are the specification, and reading them yields SEVEN forms."* This block is
# those seven forms as code, and `rosters.yaml: requires_forms` is the closed roster of their
# names -- a cell naming an eighth REFUSES AT LOAD.
#
# WHY A GRAMMAR RATHER THAN ANOTHER PREDICATE. `H-65` records the defect: Part E states every
# precondition in PROSE, so each verb needed its own hand-written `_req_*`, and `D20 -- the
# resolver has no body` came back as *the resolver has thirty*. Eight were written. Each was a
# SECOND reading of a cell that already exists in the table, and two of the eight were found to
# have dropped a conjunct or a disjunct (`_req_confer`, `_req_revoke`) -- which is the failure
# mode a per-verb body has and a typed cell does not.
#
# THE THREE READERS, and the reason this is worth doing at all:
#   1. THE FOLD (`SeasonDriver._fold`), through `WorldReader` -- §E2's `requires` against the
#      world the predecessors left.
#   2. THE PERSON (`belief_contradicts`), through `LedgerReader` -- §F1 clause 4, the SAME cell
#      asked of one person's OWN claims and of nothing else. Before this, the person's reading was
#      a `person_predicates` membership test that shared NO vocabulary with anything the fold
#      wrote (`H-116`), so clause 4 could not fire in any run.
#   3. `resolvable_verbs()` -- *can the fold carry this verb through RESOLVE at all*. It asked
#      `v in REQUIRES_PREDICATES`; a typed cell is evaluable too, and one owner means that
#      question has one answer.
#
# ⚠ THE HAZARD THIS BLOCK IS MOST LIKELY TO CARRY, stated so the next reader hunts for it: a cell
# that OVER-refuses (a conjunct the prose does not have) or UNDER-refuses (a dropped disjunct).
# `G4` weighs the two equally, and `_req_confer`'s own history in this file is the precedent for
# the second. Every cell names the §E3 line it was transcribed from, in `verb_table.yaml`.
# ===========================================================================

REQUIRES_FORMS = roster("requires_forms")
REQUIRES_OPERANDS = roster("requires_operands")
REQUIRES_FORM_NEEDS = roster_map("requires_forms", "needs")


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

    `observed` is kept HERE and attached to NO Event: an Event carrying its reads is `W-B`, and
    building the carrier before its reader exists is the dead-carrier defect `ID-13` refuses."""
    value: Any
    observed: tuple = ()


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


# `>=` is the only comparator both live cells use (§E3 `:418`, `:420`). `<=` is admitted because a
# threshold has a DIRECTION and a cell that cannot state the other one cannot be shown to have
# stated this one. MEASURED 2026-09-04: flipping `transfer`'s cell to `<=` reddens THREE tests --
# `test_wa_a_planted_claim_removes_transfer_and_a_larger_one_leaves_it`, `test_no_probe_errors`
# (probe `F10`, where both claimants on a one-unit larder are then GRANTED, so §27.1's scarcity
# stops happening) and the artifact round-trip. A strict `<`/`>` is NOT admitted: §12.1's floor is
# inclusive, and a fourth comparator would be a change to what a precondition can say.
COMPARATORS = {">=": lambda a, b: a >= b, "<=": lambda a, b: a <= b}

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
        unknown = False
        for c in self.clauses:
            r = c.check(reader, binding, observed)
            if r is False:
                return False
            if r is UNKNOWN:
                unknown = True
        return UNKNOWN if unknown else True


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
    person derives them and the act CARRIES them."""
    requirement: Requirement

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
    return Verdict(req.check(reader, b, observed), tuple(observed))


def binding_of(actor: str, operands: dict) -> dict:
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
    `venue` and `harm` ride, and the grammar's vocabulary is closed."""
    return {"actor": actor,
            **{k: v for k, v in (operands or {}).items() if k in REQUIRES_OPERANDS}}


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
                      a.payload if isinstance(getattr(a, "payload", None), dict) else {})


class WorldReader:
    """§F.24a's questions asked OF THE WORLD, with every read recorded as an `Observation`.

    ⚠ THE ACTOR'S OWN LEDGER AND NO OTHER, STRUCTURALLY. `04_CODE_ARCHITECTURE.md` §B.2's
    corrected row (`F8`): *"the carve-out is exact and it is not a widening: the fold may ask the
    ACTOR'S OWN ledger ... and no other. A Query taking a ledger and an asker who is not its
    holder still does not exist."* This reader is constructed with ONE actor id, so there is no
    argument by which a caller could name somebody else's claims -- the same move the
    `valoria-critic` agent definition makes against a read-only promise written in a prompt.

    ⚠ THE `if stem ==` CHAIN IS NOT THE ROUTER `G2` FORBIDS. It enumerates the GRAMMAR'S OWN
    predicates -- the strings `Observation` derives from the seven forms -- not verbs, entities or
    outcomes. A predicate it does not know is UNKNOWN, so an unanswerable question refuses."""

    def __init__(self, w, actor: str):
        self._w, self._actor = w, actor

    def _ancestry(self, start: str) -> list:
        seen, cur = [], start
        while cur is not None and cur not in seen:
            seen.append(cur)
            cur = Query.parent_of(self._w, cur)
        return seen

    def read(self, subject, predicate: str):
        w = self._w
        stem, _, arg = str(predicate).partition(":")
        if stem == "exists":
            # An EDGE kind is a `tenure_kinds` member and an OBJECT class is one of `World`'s own
            # collections. Both are DATA -- neither is a list written here.
            if arg in TENURE_KINDS:
                return sum(1 for t in w.tenures
                           if t.kind == arg and t.object == subject and t.live)
            attr = arg.lower() + "s"
            if attr in World._STATE_COLLECTIONS:
                return 1 if subject in getattr(w, attr) else 0
            return UNKNOWN
        if stem == "stores":
            r = w.rungs.get(subject)
            return UNKNOWN if r is None else (r.stores or {}).get(arg, 0)
        if stem == "condition":
            s = w.sites.get(subject)
            return UNKNOWN if s is None else s.condition
        if stem == "floor":
            s = w.sites.get(subject)
            if s is None:
                return UNKNOWN
            floors = w.fixtures.get("band_floors").get(s.kind)
            if floors is None:
                # `_req_work`'s refusal, carried unchanged: `H-08` owns the per-kind floors and
                # §42.2.1 forbids picking a plausible number for a kind nobody registered.
                raise Unspecified(
                    f"no band floors for site kind {s.kind!r}", "S12.1",
                    needs="a per-kind floor table -- register row H-08",
                    law="§12.1 gates verbs on `condition` against per-kind FLOORS, and §42.2.1 "
                        "forbids picking a plausible number for a kind nobody registered")
            # ⚠ THE LOOSEST FLOOR, AND AN ADVERSARIAL PASS CALLED THIS AN UNDER-REFUSAL.
            # The objection was exact and is answered rather than dismissed. It said: the prose is
            # `condition >= floor(verb)`, `band_floors`' inner keys are SITE-USE verbs
            # (bulk_shipping, fishing, deep_mining …) which its roster note says are "NOT
            # verb-table rows", so `work` is not among them and `min` silently substitutes the
            # loosest floor for the one the prose names — admitting, on a harbour, every condition
            # in 100..800 where `floor(bulk_shipping)` is 800.
            #
            # WHAT THE OBJECTION GETS RIGHT: this is not `floor(verb)`, and the site-USE is an
            # operand neither the act nor `requires_operands` carries (`H-94`).
            # WHAT IT GETS WRONG, AND WHY `min` STAYS: `work` is the GENERIC labour verb, so the
            # question its precondition asks is *can this site be worked at all* — and a site is
            # workable if it clears the floor of its LEAST demanding use. A seam at condition 100
            # cannot be deep-mined and CAN be surface-gleaned (`surface_gleaning: 50`); a harbour
            # at 150 cannot take bulk shipping and can be fished. So `min` is the READING of
            # `floor(verb)` for a verb that names no use, not a substitute for it.
            #
            # BOTH ALTERNATIVES WERE BUILT AND MEASURED BEFORE SETTLING HERE, which is why this
            # comment is long: `max` refuses a seam at 100 that surface-gleaning supports, and
            # turned `test_w8_...` red for exactly that site; `UNKNOWN` destroys the gate outright
            # — `work`'s precondition could then never return False, so §12.1's condition gate
            # could not observe the failure it exists to exclude (§0.1 point 2), and it turned
            # `test_w3_...` red. `min` is the only one of the three that both refuses an unworkable
            # site and admits a workable one.
            #
            # WHAT REMAINS OPEN AND IS NOT PAPERED OVER: a `work` that MEANS deep-mining is
            # admitted on a seam only surface-gleaning could support, because nothing on the act
            # says which use is intended. That is `H-94`'s operand, and when it exists this line
            # reads `floors[use]` and the reading collapses to the prose.
            return min(floors.values())
        if stem == "contain.path":
            if subject not in w.rungs or arg not in w.rungs:
                return UNKNOWN
            if subject == arg:
                return False           # a node is not a path to itself
            return bool(set(self._ancestry(subject)) & set(self._ancestry(arg)))
        if stem == "held_by":
            return any(t.kind == "hold" and t.subject == arg and t.object == subject and t.live
                       for t in w.tenures)
        if stem == "present_at":
            s = w.sites.get(subject)
            place = s.rung if s is not None else (subject if subject in w.rungs else None)
            return UNKNOWN if place is None else (arg in Query.presence(w, place))
        if stem == "claim.held":
            p = w.persons.get(self._actor)
            return UNKNOWN if p is None else any(c.subject == subject for c in p.ledger)
        return UNKNOWN


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
REQUIRES_STEMS = frozenset({
    "exists", "stores", "condition", "floor", "contain.path", "held_by", "present_at",
    "claim.held",
})


class LedgerReader:
    """THE SAME QUESTIONS ASKED OF ONE PERSON'S OWN CLAIMS, AND OF NOTHING ELSE.

    ⚠ IT TAKES CLAIMS, NOT A WORLD, AND NOT A PERSON. `#353 :634` permits `sense()` exactly one
    World among the non-decision functions, and §F1 clause 4 runs person-side; handing this a
    World would make `belief_contradicts` read the world, which is the filter §F1 spends two
    paragraphs forbidding (*"a filter on world truth would be `choose` reading the world"*).

    THE MOST RECENT, THEN THE MOST CONFIDENT. A ledger may hold two claims about one
    `(subject, predicate)` -- that is what a ledger IS -- and answering with the first found would
    make the verdict depend on append order. No matching claim is UNKNOWN, never False: §F1's
    asymmetry is that absence of a belief is not a belief in the negative."""

    def __init__(self, claims):
        self._claims = list(claims or [])

    def read(self, subject, predicate: str):
        best = None
        for c in self._claims:
            if c.subject == subject and c.predicate == predicate:
                if best is None or (c.when, c.confidence) > (best.when, best.confidence):
                    best = c
        return UNKNOWN if best is None else best.value


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
    return TypedRequires(_build_clause(verb, cell))


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
        `shape.py` OUTSIDE THE TYPED GAP TAXONOMY. `SystemExit` derives from `BaseException`, so
        `corpus_run.run_case`'s `except (S.ShapeGap, S.Unspecified, S.Forbidden, S.NoProducer)`
        clause never catches it -- a one-case design gap escaped as a whole-corpus run
        termination, with no DESIGN-GAP row and no section citation. The 14 load-time raises
        beside these (missing/malformed YAML, at shape.py:365/383/395/454/743/749/776/785/791/
        800/808/813/821/825) are CORRECTLY fatal and are UNCHANGED -- this file loads once, and a
        broken table should end the process. These four are not load-time; they fire per-act,
        mid-corpus, and belong in the taxonomy every other per-case refusal in this file uses."""
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
    # `W-B` / `H-122`. WHO RECEIVES A CLAIM MINTED FROM WHAT THE FOLD READ. #353 §28 says WITNESS
    # deposits and never says whether the deposit may carry the reads, or to whom; the arms are
    # `rosters.yaml: observation_deposit_modes` and the row is `H-122`. `none` is the CONTROL --
    # the behaviour before `W-B` exactly -- and the default below is argued on the row rather than
    # assumed here. Injection site: this line, read by `SeasonDriver.witness`.
    observation_deposit_mode="actor",  # `H-122`, swept none / actor / total
    # `H-80`. #353 §13.1 says the ACT declares a Record's stages and their terms. §F1's Candidate
    # is `(verb, subject, why)` and carries no operands, so NO COMPUTED ACT CAN DECLARE ANY --
    # `(Record, stages)` is a Part D row unreachable from the person's own decision. These are
    # the instrument's declared stand-in, swept, and the row says plainly that they are.
    record_stages_default=3,
    record_stage_term=1,
    budget_office_bonus=1,
    budget_leg_penalty=1,
    # `H-94`, `W-C`. THE TWO OPERANDS §54 ITEM 7'S FORMULA NAMES AND THE DESIGN NEVER SUPPLIES.
    # `stores(hearth(giver), kind) >= amount`: `hearth(giver)` is the actor's own live `contain`
    # Tenure and `to` is the question's referent, so both are DERIVED person-side -- but `kind`
    # and `amount` are values nobody states, which is `H-80`'s shape exactly (a declared stand-in
    # for operands the person cannot supply). Declare, default, sweep.
    #
    # ⚠ THESE ARE A MOVE, NOT AN INVENTION, AND THE OLD HOME IS DELETED. They were
    # `transfer`'s `operand_defaults: {kind: grain, amount: 1}` in `verb_table.yaml` -- the
    # relocated form of `_req_transfer`'s two literals -- and that cell filled them AT THE FOLD,
    # under the person, for an act whose payload carried neither. Two owners of one value, and
    # the fold's copy would have admitted a `transfer` whose effect then raised on the operands
    # the precondition had invented for it. The values are carried across unchanged.
    # ⚠ THE COMMENT HERE READ *"`H-94`, swept with the amount below"* AND NOTHING SWEPT IT. Struck
    # by the `W-C` adversarial pass: every `.sweep(...)` in the instrument named
    # `default_transfer_amount`, and `H-94`'s `sweep: [0, 1, 3]` are INTEGERS, which cannot be
    # arms for a matter kind -- one `sweep:` field was carrying two declared fixtures and
    # `register.rule_R2` cannot see that, so R2 was green on an unswept default. It has its own
    # row now (`H-121`) and its own three arms, RUN: `grain` (stocked) · `salt` (a second stocked
    # kind, which proves the fixture reaches the effect -- the store that moves is the one it
    # names) · `coin` (registered in `rosters.yaml: matter_kinds`, produced by no site and held by
    # no rung: THE CONTROL, and the only arm that can flip the verdict, because
    # `WorldReader.read` returns 0 rather than UNKNOWN for a kind a rung does not hold, so
    # `0 >= amount` is False and the transfer REFUSES).
    # ⚠ AND THE POLARITY WAS INVERTED: the SWEPT fixture was the decision-inert one and this
    # UNSWEPT one is decision-live. Measured over all 89 corpus worlds -- `transfer` executes
    # 702 / refuses 21 at both `grain` and `salt`, and 0 / 723 at `coin`, where it leaves the
    # executed set entirely (6 verbs -> 5). The 702-execution headline does rest on this value.
    default_store_kind="grain",        # `H-121`, swept grain / salt / coin
    # ⚠ `0` IS THE CONTROL AND IT IS SWEPT FIRST. Nothing is spent, so scarcity never binds and
    # `stores >= 0` admits every giver: a run at this point shows how much of the transfer
    # behaviour rests on the default rather than on the world.
    default_transfer_amount=1,         # `H-94`, swept 0 / 1 / 3
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
    # ⚠ `conferrer: Optional[str]` WAS DECLARED HERE AND IS DELETED (2026-09-03). It occurred
    # EXACTLY ONCE in the whole tracer — this line — and reached no reader, which by `ID-13` is
    # not a weak field but one that does not exist, wearing a schema's clothes. The same field
    # was deleted from the meta-architecture's own `Tenure` on the same grounds and the same day;
    # this is that ruling applied where the type actually runs.
    #
    # ⚠ AND THE DELETION OPENS NOTHING, which is the half worth stating. WHO MAY REVOKE is the
    # Seat's declared `revocation` basis (`T-o`), not the identity of whoever conferred; WHAT
    # CONFERRED a Tenure is the opening Act, in an append-only log with `causes[]`. A field here
    # would be a second home for a fact the act already holds — `ID-2`.
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
    # `W-B`. WHAT THE FOLD READ TO REACH THIS EVENT -- a tuple of `Observation`, the same triple a
    # `Claim` carries, which is what `Observation`'s own docstring says it is: *"an Observation is
    # what a Claim would be if the reader wrote one."*
    #
    # ⚠ IT IS NOT A FOURTH ABSENT FIELD. S19.3 names three fields deliberately NOT on an Event --
    # actor, target, stat_deltas -- and each absence is a design decision about ATTRIBUTION or
    # RECIPIENCY. This is neither: it is the record of what the fold read, and §27.1 already makes
    # reading the precondition the fold's business. `PLAN.md` §8.1's ban is on `target`/`actor`,
    # and `H-79` spent its own argument on reading `changes[]` rather than adding a field, so the
    # bar for adding one is stated here: this carries something NO existing field holds. `changes[]`
    # is what the act WROTE; `observed` is what it READ, and a refusal writes nothing and reads
    # everything.
    #
    # ⚠ EMPTY IS HONEST AND IS THE COMMON CASE. An untyped verb, a `NO_PRECONDITION` verb, and
    # every Event `matter()` or `calendar()` emits carry `()`: no read went through the
    # `Observation` channel. A verb on `REQUIRES_PREDICATES` reads the world through a hand-written
    # predicate that records nothing, so it too carries `()` -- that is a gap in the OLD channel,
    # not a claim that nothing was read, and it closes when the verb is typed.
    observed: tuple = ()

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
    """S17 -- `opening_set` RETURNS Candidate[], NOT Act[].

    ⚠ `operands` IS THE STRUCTURAL HALF OF `H-94`, AND IT IS NOT A FOURTH FIELD BOLTED ON. S17
    types the Candidate `(verb, subject, why)`, and `H-94` measured what that costs: `transfer`'s
    `stores(hearth(giver), kind) >= amount` has no `kind` and no `amount` that any part of the
    deliberation-to-resolution pipeline can carry, so the verb was attempted and refused in every
    world in the corpus. The row asked WHERE OPERANDS LIVE. They live here, on the Candidate,
    because the person is who derives them -- `hearth(giver)` is the giver's own Tenure and the
    referent is the person's own question -- and a channel anywhere further down (the Act, the
    Scene, the payload) would have to be filled by something that is not the person, which is L2.

    ⚠ AND THE FIELD IS NEVER PARTIAL. A form whose operands cannot all be bound forms NO
    Candidate (`operands_for` returns `None`), because an act minted with a hole is refused by the
    fold for a reason that is about the INSTRUMENT, and once `W-B` deposits observations that
    refusal becomes a FALSE BELIEF held by everyone who witnessed it."""
    verb: str
    subject: Optional[str] = None
    why: str = ""
    operands: dict = field(default_factory=dict)


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
    # ⚠ `occasion` IS THE QUESTION THE SCENE IS ABOUT, and it is the field that binds DELIBERATE
    # into the causal graph. `N3` (PR #357) measured the absence: *60 act-Events, 0 resolving to
    # a question* — an act never cited what made it, so `causes[]` could not walk from one
    # person's act back to another's, and `R3` scored 0 of 30 while every other check passed.
    # The meta-architecture types it here rather than on the Act: `Scene := (id, person,
    # occasion : Question, place : RungId, interactions : Act[])`, because the occasion is what
    # the person is spending the scene ON and the interactions are what they do in it.
    # ⚠ `place` IS DELIBERATELY NOT ADDED. `ID-13` — a declared field must reach a reader — and
    # nothing here reads a scene's place; `place_of(w, event)` already answers that question from
    # the Event. Adding it to match a type signature would be the defect the idiom names.
    occasion: Optional["Question"] = None

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
    # ⚠ WHICH SCENE THIS INTERACTION BELONGS TO. The meta-architecture's `Act` carries `scene`,
    # and it is what lets the fold ask what occasioned an act without the Act itself carrying a
    # Question — the Scene owns the occasion, the Act names its Scene. Stamped by the driver as
    # it flattens scenes into the produced list, so a caller that returns bare Acts (the
    # pre-`W17` accounting, still lawful under `as_scenes`) simply has none.
    scene: Optional[str] = None


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
    # ⚠ `H-99`, AND THESE FIELDS EXIST BECAUSE THE FIRST VERSION VALIDATED THEM AND THREW THEM
    # AWAY. `corpus_run._check_office` called `office_faction(...)` at overlay load and DISCARDED
    # the return; `Office` had no faction and no body, so nothing downstream could read either.
    # That is exactly the criterion on which `governance_modes` and `power_bases` were deleted
    # from `rosters.yaml` in the same session -- an artifact nothing reads -- applied to two
    # rosters and not to the schema that motivated them. Found by the adversarial pass.
    body: Optional[str] = None
    faction: Optional[str] = None
    body_function: Optional[str] = None

    def __post_init__(self):
        # The remit is a fixture choice; its MEMBERS are not. A typo here would mint a remit act
        # and every `remit:<that act>` eligibility would silently never match -- a verb quietly
        # unavailable to everyone, which is the worst shape a failure can take.
        bad = [a for a in self.remit_acts if a not in REMIT_ACTS]
        if bad:
            raise Unowned(f"office {self.id!r} claims remit acts not on the roster: {bad}",
                          "S11", needs="an act from rosters.yaml: remit_acts",
                          law="#353 §11 -- the remit acts are a CLOSED set")
        # The three canon axes, resolved ONCE, at construction, on the object the world holds.
        # `office_faction` refuses an unknown body, an unknown faction, a body/faction mismatch
        # and an office that belongs to nothing.
        # ⚠ REQUIRED ON EVERY OFFICE, AND THE ARGUMENT FOR MAKING IT OPTIONAL WAS WRONG. Rev 1
        # made it optional on the reasoning that requiring it "would break every test fixture and
        # import canon into the substrate". Both halves fail on inspection. There are FOUR Office
        # construction sites in the whole chain, not "every fixture"; and `shape.py` already reads
        # the canon factions from `rosters.yaml` at import, so the substrate knew about them
        # either way. Jordan, 2026-09-02, put the real question: *"Why would requiring a faction on
        # every office break canon? Wouldn't it just imply that we don't have enough factions?"*
        #
        # ⚠ THAT IS §42.2's POLARITY RULE, AND IT CUTS THE RIGHT WAY. Optional turns an office
        # nobody can place into a silent `None`; required turns it into a REFUSAL that names the
        # gap -- either the roster is missing a faction, or the office is mis-conceived, and both
        # are findings worth having. An office belongs to something or we do not know what it is.
        self.faction = office_faction(self.body, self.faction)
        if self.body is not None:
            self.body_function = BODY_FUNCTION[self.body]
        # ⚠ A TITLE IS NOT AN OFFICE, AND CONFLATING THEM PUT A KING IN THE CHURCH. `titles`
        # carries the governance ladder Jordan ruled (`title_domain`, read by `_req_revoke`), so a
        # `post` that names a TITLE is a seat on that ladder and cannot also be an organ of a
        # faction. The overlay `{post: "King", body: "Cardinal of Justice"}` was ACCEPTED before
        # this check and produced a realm title whose Church affiliation existed nowhere in canon.
        if self.body is not None and title_domain(self.post) is not None:
            raise Forbidden(
                f"office {self.id!r} names the TITLE {self.post!r} and the body {self.body!r}",
                "rosters.yaml -- titles vs office_bodies",
                needs="a title is held at a rung on the governance ladder, not seated in an organ",
                law="Jordan 2026-09-02 -- the title ladder turns on holdings and purview; an "
                    "office belongs to a faction's body. A post is one or the other, never both")
        # A titled post must sit at the rung its title governs. Otherwise a Duke seated at the
        # realm has realm-wide purview (`under_purview` walks up to the SEAT), which is the
        # governance canon inverted by a data-entry slip.
        dom = title_domain(self.post)
        if dom is not None and self.scope_rung is None and self.rung is not None:
            self.scope_rung = self.rung




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


def _entity_digest(obj: Any) -> str:
    """`H-118`: a deterministic string for ONE entity's own state, for `World.content_hash`.
    `Person`, `Site` and `Tenure` are `@dataclass` -- their auto-generated `__repr__` lists every
    field in DECLARATION order, which is fixed by the class and not by insertion, so it is stable
    across two runs of the same seed (R4). `Rung` is not a dataclass (S10 -- it stores its fields
    via `object.__setattr__` behind a whitelist, `Rung._DECLARED`), so it is read off `vars()`;
    `Rung.__init__` always inserts the same fields in the same order, so that dict's own iteration
    order is already stable, and `sorted()` over its items makes the point structural rather than
    incidental."""
    if hasattr(obj, "__dataclass_fields__"):
        return repr(obj)
    if isinstance(obj, dict):
        # `dates`, `petitions`, `dispensations` and `docket` hold PLAIN DICTS, not entities.
        # `sorted` on the items makes the digest independent of insertion order (R4).
        return repr(sorted((str(k), repr(v)) for k, v in obj.items()))
    if hasattr(obj, "__dict__"):
        return repr(sorted(vars(obj).items()))
    return repr(obj)


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


    def contain_ascends(self, subject: str, object_: str) -> bool:
        """MAY `subject` BE CONTAINED IN `object_`? The §10 ladder, asked rather than raised.

        ⚠ ONE OWNER, TWO POLARITIES, AND `W-C` MADE THE SECOND ONE REACHABLE. The rule lived
        inside `add_tenure`, where its only expression was a `Forbidden`. That was survivable while
        no COMPUTED act ever named a destination: once `move` carries a real `to`, a person can
        name any rung their containment path reaches -- including a SIBLING, because
        `contain.path` asks for a shared ancestor and a sibling has one -- and the ladder then
        refused the write by RAISING, which kills the season. A person attempting a journey the
        world will not seat them in is not an instrument defect and not a design gap; it is a
        BLOCKED TRAVEL, which is the Event `move` already declares.

        So the question is asked here and answered twice: `add_tenure` raises on it, because a
        caller writing an illegal edge directly is a bug, and `_eff_move` declines on it, because a
        person is allowed to try. Two readings of one declaration -- the same shape `evaluate`
        gives a `requires` cell, and the reason neither site re-implements the ladder.

        Non-rungs pass: `add_tenure` never checked an edge whose ends are not both rungs (a
        `contain` onto a Record means something else), and narrowing that here would be a new
        rule wearing a refactor's clothes."""
        sub, obj = self.rungs.get(subject), self.rungs.get(object_)
        if sub is None or obj is None:
            return True
        order = list(RUNG_KINDS)
        return order.index(obj.kind) > order.index(sub.kind)

    def add_tenure(self, t: Tenure) -> Tenure:
        """The ONE writer. Routes to `t.subject`'s own list, or to `_unowned` when the subject is
        not a person (`contain : Rung -> Rung` is most of those).

        ⚠ IT NOW VALIDATES, AND REV 1 VALIDATED NOTHING -- so `rung_kinds` was a MEMBERSHIP SET
        WEARING THE NAME OF A HIERARCHY. Jordan, 2026-09-02: *settlements are nested inside
        territories inside provinces inside duchies inside realm? I think that is required too, or
        is that unnecessary to nest these and instead just explicitly define scale?* The nesting is
        required and it is the thing `under_purview` WALKS -- a scale label cannot be walked, so
        the two are not interchangeable. But no `contain` edge was direction-checked, so a
        settlement containing a duchy was accepted, and `probes` builds an outright cycle.
        Measured: `corpus_run.build_at` gives 37 person-scale cases a `person`-kind rung containing
        three person rungs, and nothing refused.

        ⚠ AND `Tenure.kind` WAS UNCHECKED, which made `TENURE_KINDS` a write-only roster.
        `Tenure(..., "holds", ...)` -- the plural typo -- was accepted, and `_eligible` tests
        `t.kind == "hold"`, so the office would be silently unheld by everybody. That is the same
        failure shape `Office.__post_init__` already refuses for remit acts (§8: one rule, applied
        at every constructor rather than at one)."""
        if t.kind not in TENURE_KINDS:
            raise Unowned(
                f"tenure {t.id!r} has kind {t.kind!r}, which is not on the roster",
                "S15", needs=f"a kind from rosters.yaml: tenure_kinds {sorted(TENURE_KINDS)}",
                law="#353 §15 -- the seven Tenure kinds are a CLOSED set. An unrostered kind is "
                    "not an error at write time and a silent never-match at read time")
        if t.kind == "contain" and not self.contain_ascends(t.subject, t.object):
            sub, obj = self.rungs[t.subject], self.rungs[t.object]
            raise Forbidden(
                f"`contain` from {sub.kind} {t.subject!r} to {obj.kind} {t.object!r} does "
                f"not go up the ladder", "S10",
                needs="a parent strictly above the child on `rung_kinds`",
                law="#353 §10 -- `contain : Rung -> Rung` is the containment LADDER. An "
                    "edge that does not ascend makes `under_purview` walk sideways or "
                    "loop, and Jordan's governance canon reads purview off that walk")
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

    # `H-118`: EVERY GAME-STATE COLLECTION ON `World`, DECLARED ONCE. A hash that enumerates
    # collections inline goes stale the day someone adds one, silently and in the direction that
    # flatters it -- which is the defect H-118 IS. Declared here so `content_hash` iterates a
    # list rather than a hand-written sequence, and so
    # `test_h118_content_hash_folds_every_game_state_collection` can assert this covers the
    # World's actual attributes rather than a copy of them (§8: the rule lives once).
    #
    # ⚠ THE FIRST VERSION OF THIS FIX FOLDED FOUR OF ELEVEN AND ITS DOCSTRING CLAIMED THE GAP
    # CLOSED. Found by the W-0 adversarial pass, which is the reason the set is derived and
    # tested rather than typed: `records` and `propositions` were among the omissions, and
    # `create_record` and `utter` -- two of the FIVE verbs that execute in the corpus -- write
    # exactly those (`_eff_create_record`, `_eff_destroy_record`, `_eff_utter`). So the same
    # blindness H-118 measured on `persons` was live on the collections the corpus actually
    # moves, behind a docstring saying otherwise.
    # roster-exempt: MECHANISM, on the same ground as `_STEP_CLASS` above. These are `World`'s
    # OWN PYTHON ATTRIBUTE NAMES -- what the object calls its own fields -- not the game's
    # vocabulary. `rosters.yaml` holds what the WORLD contains; this holds where THIS CLASS puts
    # it, and the test below derives the check from `vars(World)` rather than from this tuple, so
    # the tuple is a hash ORDER and not a definition. Moving it to data would invite someone to
    # edit how the hash works while believing they were editing the game.
    _STATE_COLLECTIONS = ("persons", "rungs", "offices", "sites", "records", "propositions",
                          "dates", "petitions", "dispensations")
    # roster-exempt: MECHANISM, as `_STATE_COLLECTIONS` directly above -- the one state field that
    # is a LIST rather than a mapping, split out because its order is semantic (S31's queue) and
    # it is therefore folded positionally rather than sorted.
    _STATE_SEQUENCES = ("docket",)

    def content_hash(self) -> str:
        """`H-118`: REV 1 hashed the log alone. Demonstrated there -- delete a person from one of
        two identical worlds with no Event appended, and the hashes still matched. It now folds
        EVERY game-state collection (`_STATE_COLLECTIONS` + `_STATE_SEQUENCES` + `tenures`) --
        IN ID ORDER -- ahead of the log, so a state divergence that never reaches the log is no
        longer invisible to it.

        ⚠ SORTED-KEY ORDER, NEVER INSERTION ORDER (R4). Every mapping is hashed via `sorted(...)`
        over its own keys, and `self.tenures` (the read-only owner-first VIEW, S15.1) is re-sorted
        by `t.id` rather than trusted -- its own order is owner-then-unowned, a CONSTRUCTION
        order, and R4 (the same seed replaying byte-identically) would break the moment two runs
        added tenures in a different sequence for the same eventual world. `docket` is a LIST and
        its order is semantic (S31's queue), so it is folded in place, positionally.

        `Event.observed` DOES NOT EXIST YET (W-B) -- `getattr` guards it so this hash is
        forward-compatible without a second edit the day that field lands."""
        h = hashlib.blake2b(digest_size=16)
        for name in self._STATE_COLLECTIONS:
            for k in sorted(getattr(self, name, {}) or {}):
                h.update(f"{name}|{k}|{_entity_digest(getattr(self, name)[k])}".encode())
        for name in self._STATE_SEQUENCES:
            for n, item in enumerate(getattr(self, name, ()) or ()):
                h.update(f"{name}|{n}|{_entity_digest(item)}".encode())
        for t in sorted(self.tenures, key=lambda t: t.id):
            h.update(f"T|{t.id}|{_entity_digest(t)}".encode())
        for e in self.log:
            h.update(f"{e.id}|{e.kind}|{e.subject}|{e.emitted_at}|{e.degree}|"
                     f"{','.join(e.causes)}".encode())
            for c in e.changes:
                h.update(f"~{c.subject}|{c.mode}|{c.driver}|{c.field}|{c.delta}".encode())
            # W-B forward-compatibility: `Event` carries no `observed` field today (getattr with
            # a default guards that), and once it does this folds it with no second edit here.
            for o in (getattr(e, "observed", None) or []):
                h.update(f"^{o}".encode())
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
    # ⚠ REV 1 COMPARED A SITE ID TO A PERSON ID, SO Q3 COULD NEVER FIRE. `matter()` appends
    # `(s.id, verb, before, after, ev.id)` where `s` is a SITE, and this read `if who == p.id`.
    # A site id never equals a person id, so `band_crossed` produced ZERO Questions in every run
    # while `rosters.yaml` declared four sources and three were live. The falsifier did not catch
    # it because the test hand-planted a PERSON-keyed 3-tuple that `matter()` never emits -- it
    # asserted the reader against a shape the writer does not produce, which is a test of itself.
    # Found by the adversarial pass.
    #
    # ⚠ THE FIX IS PRESENCE, NOT A RENAME, and it is the reading §F1 Q3 actually asks for: a
    # crossing is a fact about a PLACE, and it becomes a person's question when that person is
    # THERE to notice it. `Query.presence` is the existing owner of "who is at this rung" (§8), so
    # nothing new is invented here. A person elsewhere gets no question, which is L2 working.
    #
    # ⚠ AND THIS IS WHY `F1`'s MOVE BUG MATTERED BEYOND MOVE: while every actor left the world in
    # season 1, `presence` was empty for every rung, so this source would have stayed dead even
    # once keyed correctly. The two defects hid each other.
    for who, what, *_rest in w.crossings:
        site = w.sites.get(who)
        at = getattr(site, "rung", None) if site is not None else None
        if who == p.id or (at is not None and p.id in Query.presence(w, at)):
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


def occasioned_by(w: "World", q: Optional["Question"]) -> list:
    """What EVENT occasioned a question — the antecedent an act formed from it must cite.

    ⚠ THIS IS `N3`'s MISSING EDGE, AND `N3` WAS MEASURED, NOT INFERRED: *60 act-Events, 0
    resolving to a question*. An act emitted `causes=[a.id]` and nothing else, so the graph knew
    which act made an Event and never which Event made the act — and `R3` (an act by one person
    caused by an act of another) scored **0 of 30** while `R1`, `R4` and `R5` all passed. The
    chain Reading 07 §4 calls *"the one that is actually the game"* — a claim lands in a ledger,
    raises a question, forms a candidate, becomes an act, emits an Event, is witnessed, deposits
    in SOMEONE ELSE'S ledger — was built end to end except for this one edge.

    **One route per question source, and `need` is a deliberate empty rather than a guess:**

      * `claim_landed` — the deposit Event names the claim in its `changes[]`; its `causes[]`
        name the Event the claim is ABOUT. **The originating Event is returned, not the deposit.**
        The claim IS a belief about that Event — `Claim.predicate` is literally `e.kind` at the
        deposit — so citing the transport instead would put the postman in the arc. The deposit
        stays in the graph on its own `causes[]`; nothing is lost by not naming it twice.
      * `date_due` — ⚠ **ALSO DEAD, AND FOR A DIFFERENT CAUSE THAN `band_crossed`.** `calendar()`
        writes `Date.fired` through the gate with **no `emits=`**, and the gate builds an Event
        only when one is passed (it is *required* only at MATTER), so **no Event in any log
        carries a date id** and the search below cannot match. `write_matrix.yaml` declares
        `date.fired` for `(Date, fired)` and nothing emits it — a CALENDAR-class silent write of
        exactly the shape the gate refuses at MATTER. Doubly latent today, because `N1` means Q1
        never forms at all; when `W20` closes `N1` the question will form and walk to nothing.
        **Making CALENDAR emit is `W20`'s and is not done here** — it would put a new Event in
        every log and move every hash.
      * `band_crossed` — ⚠ **THIS ROUTE IS DEAD, AND IT IS NAMED DEAD RATHER THAN LEFT TO LOOK
        LIVE.** `questions_for` builds the question as `Question(f"q:band:{what}", "band_crossed",
        (what,), what)` where `what` is the crossing's **verb** — `"work"` — not an id, so the
        search below can never match: nothing in the log has id `"work"` or a change whose
        subject is `"work"`. The crossing Event's id EXISTS, as element 4 of the `w.crossings`
        tuple `(s.id, verb, before, after, ev.id)`, and `questions_for` discards it. Carrying it
        onto the Question is a one-line change to a surface this function does not own, so it is
        registered (`H-110`) rather than taken here. **A route that returns nothing is honest; a
        docstring saying it walks is not, and the first writing of this one said it walks.**
      * `need` — **empty, on purpose.** A standing commitment to an OUGHT is interior; no Event
        caused it this season, and `ID-5`'s polarity says absence maps to the refusal rather than
        to a plausible default. An act taken out of a standing ambition genuinely has no
        antecedent but the actor, and `[ROOT]` is what the design already has for that.

    ⚠ **SO ONE OF FOUR ROUTES IS LIVE** — `claim_landed`, which is the one propagation runs on.
    One is empty by design (`need`) and **two are dead**, each for a cause it does not own:
    `band_crossed` because the question carries a verb name where an id is needed, `date_due`
    because CALENDAR emits nothing. ⚠ **This count has been wrong twice**: *"one route per
    question source"* first, then *"two of four"* after a critic found `band_crossed`. Both were
    written by looking at this function rather than at what feeds it. **The lesson is in the
    count, not in the routes: a route's liveness is a property of its PRODUCER, and this function
    cannot see its producers.**

    ⚠ **IT RETURNS IDS AND WRITES NOTHING.** Resolver-side, read-only over `w.log`, callable from
    a test without a driver — which is `ID-10`: a check that cannot observe the failure it
    excludes is absent, and this one can be asked directly what it found."""
    if q is None:
        return []
    about = str(getattr(q, "about", "") or "")
    if not about or q.source == "need":
        return []
    if q.source == "claim_landed":
        for e in reversed(w.log):
            if e.kind == "claim.deposited" and any(c.subject == about for c in e.changes):
                return [x for x in (e.causes or []) if x != ROOT]
        return []
    if q.source not in ("date_due", "band_crossed"):
        # ⚠ NOT A BARE `else`. An undeclared source added to the roster would otherwise fall into
        # the id search below and answer plausibly forever, which is the polarity `ID-5` refuses:
        # zero evidence maps to the verdict AGAINST the thing measured, never to a quiet default.
        # ⚠ AND IT IS DEFENCE IN DEPTH, NOT THE FIRST GATE: `Question.__post_init__` already
        # refuses a source outside `question_sources`, so this is unreachable from a rostered
        # question and would fire only if that constructor were bypassed or the roster grew
        # without this function being taught the new route.
        raise Unspecified(
            f"no occasion route for question source {q.source!r}", "ID-16",
            needs=f"a route here, or one of {sorted(QUESTION_SOURCES)}",
            law="ID-5 -- refuse, don't default. A new question source silently taking the id "
                "search would answer plausibly and wrongly for every question it raised")
    for e in reversed(w.log):
        if e.id == about or any(c.subject == about for c in e.changes):
            return [e.id]
    return []


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


# ---------------------------------------------------------------------------
# ⚠ FOUR PREDICATES WERE RETIRED HERE BY `W-A` (2026-09-04) -- `_req_transfer`, `_req_tell`,
# `_req_move` and `_req_work`. Each is now a TYPED CELL in `verb_table.yaml`'s `requires_typed:`
# column, read by `evaluate()`, and §8's rule is that the rule lives once: a verb with both would
# be two readings of one cell, which is exactly how `_req_confer` came to drop a disjunct and
# `_req_revoke` an entire clause.
# `test_wa_one_owner_a_verb_has_a_typed_cell_or_a_predicate_and_never_both` is the guard that
# fails on a recurrence.
#
# THE FOUR THAT REMAIN -- `confer`, `revoke`, `dispatch`, `convene` -- are `remit:`-eligible, not
# `own`-eligible, and `W-A`'s scope is the `own` rows. Two of them need grammar forms with no
# `own` cell (`cardinality`, `basis`) and `confer` needs a DISJUNCTION, which no `own` cell has
# and which is therefore not built (`ID-13`: a combinator nothing uses is a dead carrier).
# ---------------------------------------------------------------------------


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


def _operand(a: "Act", name: str):
    """THE FOLD'S ONE READ OF A CARRIED OPERAND. A missing one RAISES.

    ⚠ AN ABSENT OPERAND AT RESOLVE IS AN `InstrumentDefect`, NOT A REFUSAL, AND THE DISTINCTION
    IS THE WHOLE OF `W-C`'s SECOND HALF. A refusal says *the world would not permit this*; a
    caller minting a `transfer` that names no receiver is saying nothing about the world at all.
    Filing it as a refusal would emit `emits_on_refusal`, `W-B` would deposit that at WITNESS, and
    every witness would end the season holding a belief about a granary the act never named --
    the instrument's own gap, laundered into the game as evidence. `operands_for` is what makes
    this unreachable from a COMPUTED act: a Candidate whose operands cannot be derived is never
    formed, so an act arriving here without one came from a hand-written call site.

    ⚠ IT IS THE OWNER OF THE RULE, AND THREE EFFECTS HAD THEIR OWN COPY. `_eff_move` raised on a
    missing `to` and `_eff_work` on a missing `site` -- both correct, both written twice -- while
    `_eff_transfer` DEFAULTED four operands (`from`/`to` to `""`, `kind` to `"grain"`, `amount` to
    `1`) and `_eff_confer` defaulted `to` to the actor, i.e. conferred an office on whoever
    happened to be acting when the act named nobody. Same situation, four verbs, three answers.
    §8: the rule lives once."""
    d = a.payload if isinstance(getattr(a, "payload", None), dict) else {}
    if d.get(name) is None:
        raise InstrumentDefect(
            f"a {a.verb!r} reached its effect with no {name!r} operand. The fold binds operands "
            f"from the act's payload and `operands_for` forms NO Candidate whose operands it "
            f"cannot derive, so an act minted without one is a CALLER defect and not a design "
            f"gap -- and fabricating a value here would name a thing nobody chose. Payload: "
            f"{sorted(d)}")
    return d[name]


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
    # ⚠ `to` WAS `d.get("to") or a.actor` -- a silent default that seated the ACTOR whenever the
    # act named nobody, which is the same class as `_eff_transfer`'s four and is deleted with
    # them. A conferral onto nobody is a malformed act, not a self-conferral.
    # ⚠ THIS CHANGE IS A DELIBERATE EXTRA AND NOT A PATH `H-94` MADE REACHABLE; RECLASSIFIED BY
    # THE `W-C` ADVERSARIAL PASS, because filing it as a consequence overstates what closing the
    # operand channel did. NO COMPUTED ACT CAN REACH THIS EFFECT: `confer` is untyped, `office`
    # is not in `rosters.yaml: requires_operands` so `operands_for` can never derive one, and
    # `_req_confer` returns False when the payload names none -- `corpus_run`'s own output lists
    # `confer` among the verbs "foldable but never even attempted". The improvement is real (a
    # silent self-conferral becomes a loud `InstrumentDefect`) and nothing measurable moved.
    obj, to = d.get("office"), _operand(a, "to")
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
    dest = _operand(a, "to")
    # ⚠ THE GUARD MOVED TO `_operand` AND ITS HISTORY IS KEPT HERE, because the history is what
    # makes the guard's shape legible. Rev 1 fell through on a missing destination, closed every
    # live leg and STILL returned `[a.actor]`, so `_fold` saw a non-empty `changed` and published
    # `travel.moved` for a move that did not happen. Returning `[]` would be quieter and just as
    # wrong: the caller would report a no-op as a legitimate nothing. §42.2's polarity rule -- no
    # destination is a refusal, never a silent success. The version of this guard that lived here
    # was found to pass `needs=`/`law=` to `InstrumentDefect`, which takes no keywords, so it
    # would have raised `TypeError` if it had ever fired -- a guard that crashes instead of
    # reporting, unfired because the precondition refuses first. One owner is also one place for
    # that mistake to be made.
    # ⚠ A DESTINATION THE LADDER WILL NOT SEAT THE MOVER IN IS A BLOCKED TRAVEL, NOT A CRASH, and
    # this branch is `W-C`'s doing: once `move` carries a real `to`, a person can name any rung
    # their containment path reaches, and `contain.path` asks for a SHARED ANCESTOR -- which a
    # sibling has. So `move p_low -> p_mid` passed the precondition, `add_tenure` raised
    # `Forbidden` on the §10 ladder, and the season died. Declining here returns nothing changed,
    # so the fold emits `move`'s own `emits_on_refusal`. The rule itself is not re-implemented:
    # `World.contain_ascends` is the one owner and `add_tenure` still RAISES on it, because a
    # caller writing the edge directly is a bug where a person attempting the journey is not.
    if not w.contain_ascends(a.actor, dest):
        # ⚠ THE INSTANCE DETAIL SITS AFTER ` -> `, WHICH IS `report.py`'s CLUSTER KEY
        # (`d.what.split(" -> ")[0]`). Putting the actor and the destination in the prefix would
        # mint one register entry per pair and leave the label reading mid-sentence.
        TRACE.decision(f"a move's destination is not up the §10 ladder -> {a.actor} into {dest!r}",
                       "S10/E3", chose="change nothing, so the fold emits the refusal",
                       alternatives=["write the edge anyway (add_tenure raises and the season "
                                     "dies)", "let the precondition admit it and crash later"])
        return []
    for t in w.tenures:
        if t.subject == a.actor and t.kind == "contain" and t.until is None:
            t.until = w.tick
    w.add_tenure(Tenure(H(w.world_seed, w.tick, a.actor, f"leg:{a.id}"),
                        a.actor, dest, "contain", since=w.tick))
    # ⚠ THE DECLARED WRITE, NOW ACTUALLY WRITTEN. `verb_table.yaml`'s `move` row names
    # `(Person, travel_leg)` as its FIRST write and rev 1 never touched the field, so
    # `Query.budget`'s distance penalty read `len(p.travel_leg)` == 0 in every run and the only
    # test of it set the field by hand. A declared write that no effect performs is a lie the
    # write matrix cannot catch, because the matrix gates writes that HAPPEN.
    mover = w.persons.get(a.actor)
    if mover is not None:
        mover.travel_leg = list(mover.travel_leg) + [dest]
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
    # ⚠ NO FALLBACK. This read `or next((x for x in sorted(w.sites)), None)` -- the alphabetically
    # FIRST site in the world -- so a `work` with no site named one nobody chose. `_eff_move`
    # refused the identical situation and this did not; found by the W-A adversarial pass, which
    # noted the two are the same defect one verb along. `W-C` gave that answer ONE owner
    # (`_operand`) rather than two copies of it.
    return [_operand(a, "site")]


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
    # ⚠ `harm` KEEPS ITS DEFAULT AND `W-C` LEFT IT DELIBERATELY -- IT IS `W-E`. Every other
    # `.get(<operand>, <literal>)` in this block is deleted, and this one is not, because `harm`
    # is NOT in `rosters.yaml: requires_operands`: no cell can bind it, `operands_for` cannot
    # derive it, and there is no route by which a computed act could carry it. Deleting the
    # default here without that route would make `kill / wound` raise on every act the loop
    # produces, so the honest move is to name the item that supplies it rather than to break the
    # verb for tidiness. ⚠ AND THE DEFAULT IS NOT INNOCENT: `p.body` is FULL body, so an act that
    # names no harm KILLS. `W-E` owns both halves.
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
    # ⚠ FOUR SILENT DEFAULTS STOOD HERE AND `W-C` DELETED ALL FOUR: `from`/`to` defaulted to
    # `""`, `kind` to `"grain"` and `amount` to `1`. Each was §0.05's literal-in-a-body, and
    # together they made an operand-less `transfer` a WELL-FORMED act about a granary nobody
    # named. They are `_operand` reads now, and their two open values are fixtures with a register
    # row and a sweep (`H-94`).
    src = w.rungs.get(_operand(a, "from"))
    dst = w.rungs.get(_operand(a, "to"))
    kind, amount = _operand(a, "kind"), _operand(a, "amount")
    # ⚠ A SIDE THAT IS NOT A RUNG MEANS THE TRANSFER DID NOT HAPPEN, and returning nothing is what
    # makes the fold emit the refusal. This branch became reachable FROM A COMPUTED ACT the moment
    # operands became real: a person names a receiver from their question's referents and may name
    # something that is no rung at all. The old shape moved the giver's side anyway, which is the
    # matter ANNIHILATION this effect's own docstring records -- grain leaving the world and
    # arriving nowhere. §42.2's polarity: an unperformable transfer refuses; it does not
    # half-happen.
    # ⚠ *"IT SURVIVED ONLY BECAUSE NO COMPUTED ACT EVER BOUND `from` TO BEGIN WITH"* STOOD HERE
    # AND IS FALSE; STRUCK BY THE `W-C` ADVERSARIAL PASS. No COMPUTED act bound `from` -- but
    # probe `F10` did, in its payload, and omitted `to`, so the old effect decremented `Hh` and
    # delivered nowhere: `F10` DESTROYED 6 GRAIN ON EVERY PROBE RUN, in an economy where `yield`
    # is the only source. Measured by weighing every rung across the probe's own season: total
    # store mass ends at 107 on the pre-`W-C` tree (`45a537c`) and at 113 here, and the difference
    # is exactly the 6. The path was reachable AND REACHED; only the computed path was closed, and
    # `F10`'s payload edit is a BUG FIX in a live probe rather than a signature accommodation.
    # `F10` now asserts conservation, because its old assertion set could not observe the failure
    # it was sitting on (§0.1 point 2).
    if src is None or dst is None:
        TRACE.decision(f"transfer names a side that is no rung -> from "
                       f"{_operand(a, 'from')!r} to {_operand(a, 'to')!r}", "E3/S27.1",
                       chose="change nothing, so the fold emits the refusal",
                       alternatives=["move the giver's side anyway (matter leaves the world)"])
        return []
    src.stores = dict(src.stores or {})
    src.stores[kind] = src.stores.get(kind, 0) - amount
    dst.stores = dict(dst.stores or {})
    dst.stores[kind] = dst.stores.get(kind, 0) + amount
    # BOTH SIDES, because §E3 says `transfer` writes `(Rung, stores)` twice -- one per side -- and
    # a one-sided report would make the Event name half of what it did. The `if r is not None`
    # filter that stood here is gone with the branch above that made it necessary.
    return [src.id, dst.id]


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

        # `W-B`. THE READS THIS ACT'S PRECONDITION MADE, ON EVERY EVENT THE ACT EMITS.
        # ⚠ DECLARED BEFORE `ev` AND REBOUND BY THE `requires` BLOCK BELOW, DELIBERATELY. `ev`
        # closes over the NAME, so it reads whatever `verdict` is bound to AT CALL TIME -- which
        # is `UNKNOWN, ()` for the ineligibility return above (eligibility reads tenures, not the
        # requirement, so it observed nothing) and the evaluated Verdict for every return after
        # it. The alternative -- passing `observed` as a parameter to all four `ev(...)` call
        # sites -- puts the same fact in four places, which is `§8` one seam over.
        verdict = Verdict(UNKNOWN, ())

        def ev(kinds, causes, changes=None):
            return [Event(H(w.world_seed, w.tick, a.actor, f"{k}:{a.id}"),
                          k, a.actor, list(changes or []), list(causes), w.tick,
                          observed=verdict.observed)
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
        # ⚠ A CONTESTED VERB NEVER REACHES THIS LINE TODAY. The contest branch in `resolve()`
        # `continue`s before the fold, because the subsystem returns a WINNER and no mapping to a
        # degree exists (H-98, tier 0, absent). `writes_at(None)` on a contested verb RAISES
        # rather than falling back to the union -- so if that branch is ever wired to fall
        # through without minting a degree, it fails loudly here instead of silently writing the
        # full kill. That is the guard, and it is the reason the parameter is not optional.
        _degree_for_writes = None      # the seam mints this once H-98 rules the bands
        _pairs = row.writes_at(_degree_for_writes) if row.writes else ()
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
        # ⚠ `[a.id]` ALONE WAS `N3`. §39.2 line 2 says `causes[]` NAMES THE ACTS, and that is
        # necessary and was treated as sufficient: an Event named the act that emitted it and
        # nothing named what occasioned the act, so the walk stopped dead at every decision and
        # `R3` — the only check the corpus failed — could never fire from a real run. The
        # occasion is on the Scene the act belongs to; `occasioned_by` turns it into the
        # antecedent Event ids. Adding them here rather than at the twelve `ev(...)` call sites
        # is `§8`: the rule lives once, on the one path every act-emission takes.
        return ev(kinds, [a.id] + self._occasion_ids(w, a), list(a.changes) + changed)

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
                elif isinstance(r, dict):
                    # ⚠ THE SEAM RETURNS A SUBSYSTEM RESULT, NOT EVENTS, AND REV 1 EXTENDED THE
                    # EVENT LIST WITH ITS KEYS. `out.extend(r)` over a dict yields the STRINGS
                    # 'status', 'module', 'winner', ... so `resolve()` handed nine strings back to
                    # `season()` as if they were Events. Invisible until now only because the road
                    # to the seam was closed (the one-claimant bug above): the first act to reach
                    # the seam is the first act to hit this.
                    #
                    # ⚠ WHAT THE FOLD MAY WRITE HERE IS `H-98`, AND IT IS OPEN. The verb row
                    # declares `emits: [person.died]` and `writes: [Person.body, Person.exists,
                    # Tenure.until]`; the subsystem returns a WINNER and a legitimate UNDECIDED
                    # case. Turning "p_low won" into "p_mid died" is the mapping H-98 says nobody
                    # has made -- and S27.2 calls inventing it the second resolver. So the fold
                    # records THAT THE CONTEST RAN and who prevailed, with `changes=[]`: no state
                    # moves, no degree is minted, and `person.died` stays unemitted, which is the
                    # honest report that the outcome model is missing rather than empty.
                    #
                    # ⚠ WHAT CHANGED 2026-09-03, AND WHAT DID NOT (#358 rev.2 §C.4 / F6).
                    # THE PLACE THE MAPPING LANDS NOW EXISTS: `VerbRow.writes_at(degree)` is the
                    # reader, and `kill / wound` declares its four branches in `verb_table.yaml`
                    # at grade `assumption` with a sweep. So this is no longer "there is nowhere
                    # to put the answer" -- it is "the bands are not ruled".
                    # WHAT DID NOT CHANGE: `combat_seam.resolve` returns `winner` and
                    # `result in {1, -1, 0}`. A WINNER IS NOT A DEGREE. Turning one into the
                    # other is still H-98, still tier 0, still `absent`, and filling it here
                    # would be an instrument inventing off the register (G.4.8). The correct
                    # sequence is: the subsystem returns a MARGIN -> the one ladder mints a
                    # Degree -> `writes_at` selects the branch. Two of those three now exist.
                    _win = r.get("winner")
                    out.append(Event(
                        H(w.world_seed, w.tick, a.actor, f"contest:{_contests[0]}:{a.id}"),
                        "contest.resolved", a.actor, [], [a.id], w.tick))
                    TRACE.decision(
                        f"contest for {_contests[0]!r} resolved; winner={_win!r}", "S39/H-98",
                        chose="record that it ran; write nothing",
                        alternatives=["map winner -> person.died (H-98: the missing model)",
                                      "raise (E2: failure emits, never raises)"])
                else:
                    out.extend(r)
                continue
            # S27.1: CONTENTION IS AN ORDERED FOLD. Each act sees the world its predecessors
            # left. SEQUENCE, NOT SIMULTANEITY -- and NO ACT NEEDS TO KNOW ANOTHER EXISTED.
            produced = self._fold(w, a)
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
            # MATCHES ON. Two claims a reader cannot tell apart are one belief stored twice, and
            # `claim_subjects` gives the same reason for its own de-duplication: a person holding
            # two identical claims would double-count in every eviction comparison.
            if obs_mode != "none" and (obs_mode == "total" or pid == e.subject):
                seen_obs: set = set()
                for o in (getattr(e, "observed", ()) or ()):
                    if o.value is UNKNOWN or o.value is None:
                        continue
                    key = (o.subject, o.predicate)
                    if key in seen_obs:
                        continue
                    seen_obs.add(key)
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
        # ⚠ THE SEAM CALLS NOW. Jordan, 2026-09-02: *"kill / wound points towards a seam that
        # should be calling in the personal combat system."* This block used to resolve the
        # subsystem by name and then REFUSE — a pointer, not a call — on a scope note that ruling
        # overrides. `combat_seam` is the IN-side, built on `engine/cross_scale/combat_bridge.py`'s
        # precedent rather than a new pattern.
        if _sub["module"] == "personal_combat":
            import combat_seam
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
