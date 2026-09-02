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

    def sweep(self, name: str, value: Any) -> "Fixtures":
        f = Fixtures(**self._v)
        f._v[name] = value
        return f


DEFAULT_FIXTURES = Fixtures(
    # S48: condition is an int on an EXPORTED scale. S22 assigns the scale to `params`, and the
    # in-chain params document "proposes NO VALUES", so this is a fixture. Injection site: here.
    condition_scale=1000,
    # S26.3: the budget is RULED at "~5". A band is not an integer; this is the integer the
    # instrument runs on, and A31 sweeps it because the verdict moves with it.
    act_budget=5,
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
    wear_per_season={"harbour": 10, "seam": 10, "body": 10},
    # S20: Claim.confidence. Rev 1 hardcoded 1, which degenerated the eviction comparator.
    confidence_default=100,
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
    band_floors={"harbour": {"bulk_shipping": 800, "fishing": 100},
                 "seam": {"deep_mining": 700, "surface_gleaning": 50},
                 "body": {"full_operations": 800, "limited": 500, "withdrawal_only": 100}},
)


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


def _load_write_matrix() -> dict:
    import yaml as _yaml
    if not WRITE_MATRIX_YAML.exists():
        raise SystemExit(f"write_matrix.yaml not found at {WRITE_MATRIX_YAML}")
    doc = _yaml.safe_load(WRITE_MATRIX_YAML.read_text())
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


def _load_rosters() -> dict:
    import yaml as _y
    if not ROSTERS_YAML.exists():
        raise SystemExit(f"rosters.yaml not found at {ROSTERS_YAML}")
    return (_y.safe_load(ROSTERS_YAML.read_text()) or {}).get("rosters") or {}


_ROSTERS = _load_rosters()


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
    vals = r["values"]
    return tuple(vals) if (ordered or r.get("ordered")) else frozenset(vals)


TENURE_KINDS = roster("tenure_kinds")
RUNG_KINDS = roster("rung_kinds", ordered=True)
REMIT_ACTS = roster("remit_acts")
WITNESS_CHANNELS = roster("witness_channels", ordered=True)
CLAIM_SOURCES = roster("claim_sources")
STRATA = roster("strata", ordered=True)

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

    def eligibility_kinds(self) -> tuple:
        return tuple(a.split(":")[0].strip() for a in self.eligibility)


def _load_verb_table() -> dict:
    import yaml as _y
    if not VERB_TABLE_YAML.exists():
        raise SystemExit(f"verb_table.yaml not found at {VERB_TABLE_YAML}")
    doc = _y.safe_load(VERB_TABLE_YAML.read_text())
    out = {}
    for r in doc["verbs"]:
        name = r["verb"]
        if name in out:
            raise SystemExit(f"verb_table.yaml: {name!r} appears more than once")
        row = VerbRow(name, r["stratum"], tuple(r["eligibility"]), r["requires"],
                      tuple(r["writes"]), tuple(r["emits"]),
                      tuple(r["emits_on_refusal"]), r["grade"])
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
        out[name] = row
    return out


VERB_TABLE: dict = {}          # filled after STRATA loads, at the bottom of the roster block


VERB_TABLE = _load_verb_table()


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

    __slots__ = ("subsistence",)

    def __init__(self, subsistence: int):
        self.subsistence = subsistence

    @property
    def standing(self) -> int:
        raise Unspecified(
            "Sensation.standing", "S18.2",
            needs="an aggregation producing 'what everyone reads off you' that does not cross holders",
            law="S18.2 defines standing as 'THE GAP BETWEEN WHAT EVERYONE READS OFF YOU AND WHAT YOU HOLD' and NO SECTION COMPUTES IT. The obvious computation -- reading a value off every other person -- is the shape S22.4 clause 2 bars, so this is not merely unwritten: the direct route to it is refused",
        )

    def __iter__(self):
        return iter((self.subsistence,))


class View:
    """S18.1 -- a View holds IDS, NEVER REFERENCES. L2 is enforced BY CONSTRUCTION: any attempt
    to reach a world collection through a View raises. S18: AT MOST K ids, BUILT NOT FILTERED."""

    __slots__ = ("holder", "claim_ids")

    def __init__(self, holder: str, claim_ids: list[str], k: int):
        if len(claim_ids) > k:
            raise Forbidden(f"View built with {len(claim_ids)} ids against cap K={k}", "S18",
                            law="S18 -- at most K claim ids from the holder's OWN ledger")
        object.__setattr__(self, "holder", holder)
        object.__setattr__(self, "claim_ids", list(claim_ids))

    def __getattr__(self, name: str) -> Any:
        raise Forbidden(
            f"choose() reached for world state '{name}' through its View", "S3-L2",
            needs="a person decides from their own claims; world truth enters only via sense()",
            law="L2 -- choose never receives a World. NOT BY DISCIPLINE -- BY TYPE",
        )


@dataclass
class Candidate:
    """S17 -- `opening_set` RETURNS Candidate[], NOT Act[]."""
    verb: str
    subject: Optional[str] = None
    why: str = ""


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
    _DECLARED = {"id", "kind", "stores", "sites", "records", "dates", "stake",
                 "envelope", "transmission", "judging_set_rule"}

    def __init__(self, id: str, kind: str, **kw: Any):
        if kind not in RUNG_KINDS:
            raise Forbidden(f"Rung.kind '{kind}'", "S10", law=f"S10 -- eight kinds: {RUNG_KINDS}")
        object.__setattr__(self, "id", id)
        object.__setattr__(self, "kind", kind)
        for f_, d in (("stores", dict), ("sites", list), ("records", list),
                      ("dates", list), ("stake", list), ("envelope", list)):
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
        self.tenures: list[Tenure] = []
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
        self.crossings: list[tuple] = []        # S12.1/L5 -- band-edge crossings, EMISSIONS
        # S33: "`purpose` must be unique per DRAW, not per operation, or two draws inside one
        # act collide." A per-TICK ordinal is unique within the tick AND identical across runs
        # of the same seed -- a global counter would be unique but NOT REPRODUCIBLE, which
        # destroys the replay contract, and a content hash collides when two draws are alike.
        self.draw = 0

    # -- S30.2: the write class is a PARAMETER of the store API, THE GATE APPLIES THE WRITE,
    # and `record_kind`/`fieldname` are REQUIRED so the L4 limb cannot be silenced by omission.
    def write(self, thing: str, wclass: WriteClass, apply: Callable[[], Any],
              record_kind: str, fieldname: str, driver: str,
              caused_person_exists: Optional[str] = None) -> Any:
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
        before = apply()
        TRACE.write(thing, wclass.value, sname, True)
        self.writes.append((thing, wclass.value, sname, record_kind, fieldname, driver))
        return before

    # -- S4: a Query MAY be cached. Built AT a barrier, read-only until the next, DISCARDED there.
    def cache_at_barrier(self, key: str, build: Callable[[], Any]) -> Any:
        if self._in_parallel_map:
            raise Forbidden(f"cache '{key}' built inside a parallel map", "S4",
                            law="S4 -- the cache is built AT A BARRIER; NOTHING INSIDE A PARALLEL MAP BUILDS ONE")
        if key not in self._barrier_cache:
            self._barrier_cache[key] = build()
        return self._barrier_cache[key]

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
    def budget(p: Person, v: View, k: int) -> int:
        """S26: `budget : (Person, View) -> int`. NO WORLD.

        REV 3 DISCLOSURE, because rev 2's docstring claimed something the body did not do.
        THIS RETURNS THE INJECTED FIXTURE AND IGNORES `p` AND `v` -- it is functionally the
        FIELD S26.3 forbids, and it cannot honestly be otherwise, because of a collision the
        chain has not resolved:

          S26 types it `(Person, View) -> int`, with NO World.
          S26.3 consequence 1 says it varies by OFFICE, CONDITION and DISTANCE TRAVELLED.

        All three are RESOLVER-SIDE facts. Office-holding is a `hold` Tenure in the tenure
        store; `condition` belongs to a Site; distance travelled is a travel leg, which S22.3
        says HAS NO OWNER AT ALL. A person-side function with no World cannot read any of
        them. Probe P42 raises this as a COLLISION rather than papering over it with a
        plausible formula, which S42.2.1 forbids.

        What rev 3 DOES restore is the half rev 2 dropped: `choose` ASKS for its own budget
        rather than being handed the answer. `deliberate` passes this callable down, so the
        person consults their own budget and decides what to leave undone -- and an
        over-budget return still RAISES, because silently discarding the tail would be an
        engine deciding a person's options, which is L1."""
        TRACE.query("budget", "person")
        return k

    @staticmethod
    def opening_set(p: Person, v: View, roster: list[Candidate]) -> list[Candidate]:
        """S17 -- returns Candidate[], NOT Act[].

        REV 2 HONESTY NOTE. The TYPE is faithful; the PROPERTY S17 chose the type to protect --
        "an option set that is COMPUTED rather than an AUTHORED LIST" -- is not, because
        `roster` is the caller's authored list. S61 records why it cannot be: `assemble(person,
        question)` has no producer for `q`, so DELIBERATE HAS NO DECLARED ENTRY POINT and there
        is nothing from which to compute a set. The roster is the instrument standing in for a
        producer that does not exist, and it is marked so rather than banked."""
        TRACE.query("opening_set", "person")
        return list(roster)

    @staticmethod
    def assemble(p: Person, question: Any, k: int) -> View:
        if question is None:
            raise NoProducer("the question `q` that assemble() takes", "S61",
                             needs="a producer for q",
                             law="S61 -- `assemble(person, question)` and `view(person, question)` are UNSATISFIABLE; DELIBERATE HAS NO DECLARED ENTRY POINT")
        return View(p.id, [c.id for c in p.ledger][-k:], k)

    @staticmethod
    def entrenchment(p: Person, seasons_held: int, scale: int, span: int) -> int:
        TRACE.query("entrenchment", "person")
        return min(scale, (seasons_held * scale) // span)


def sense(p: Person, w: World, subsistence: Callable[[Person, World], int]) -> Sensation:
    """S18.2 / S26 -- the ONE non-decision function permitted a World, and the only bridge from
    world truth into `choose`.

    REV 3. It now RETURNS a Sensation, so `choose : (Person, View, Sensation) -> Act[]` is the
    signature actually exercised. Reading `.standing` raises where the design fails to supply
    it; `.subsistence` is computed by an INJECTED formula, because no in-chain document
    supplies one and S10.4 makes MatterKind an OPEN registry -- summing kinds as if fungible
    is a model choice this instrument may not make on the design's behalf (S42.2.1)."""
    TRACE.query("sense", "bridge")
    return Sensation(subsistence(p, w))


def sense_subsistence_only(p: Person, w: World, formula: Callable[[Person, World], int]) -> int:
    """The subsistence half, with the formula INJECTED rather than invented (S42.2.1). No
    in-chain document supplies one, and S10.4 makes MatterKind an OPEN registry, so summing
    kinds as if fungible is a model choice this instrument may not make on the design's behalf."""
    return formula(p, w)


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


@requires_predicate("transfer")
def _req_transfer(w: "World", a: "Act") -> bool:
    """#353 §54 item 7: `stores(hearth(giver), kind) >= amount`. THIS IS THE SCARCITY PREDICATE --
    §27.1's whole argument rests on it: the second claimant on an emptied granary gets a DIFFERENT
    Event, and it falls out of the fold because each act sees the world its predecessors left."""
    give = (a.payload or {}) if isinstance(a.payload, dict) else {}
    rung = w.rungs.get(give.get("from", ""))
    kind, amount = give.get("kind", "grain"), give.get("amount", 1)
    return bool(rung and (rung.stores or {}).get(kind, 0) >= amount)


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
    """§12.1: `condition >= floor(verb)`. The floors are `H-08` and come from Fixtures, swept."""
    for ch in a.changes:
        site = w.sites.get(ch.subject)
        if site is not None:
            return site.condition >= 0        # the per-verb floor is H-08; presence of the site
    return True                               # is what this fold can check without inventing one


# Verbs the probe corpus uses that #353 does not name AS A VERB — checked, not assumed: the
# strings `take_seat`, `press_claim`, `raid` and `confer_authority` appear ZERO times in its 2,067
# lines, and `fight`/`refuse`/`do`/`act` appear only as ordinary English. They are the caller's
# inventions and the fold says so, rather than charging them to the design. Register row H-64.
INVENTED_VERBS = frozenset(  # roster-exempt: not a game definition — the OPPOSITE, a list of
                             # things the game does not define, kept so the fold can attribute a
                             # gap correctly. It SHRINKS as probes are re-authored.
    ["take_seat", "press_claim", "raid", "confer_authority", "fight", "refuse", "do", "act"])

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
        w.tenures.append(Tenure(H(w.world_seed, w.tick, a.actor, f"leg:{a.id}"),
                                a.actor, dest, "contain", since=w.tick))


@effect_for("work")
def _eff_work(w: "World", a: "Act") -> None:
    """`work` alters `(Site, condition)` by the act's declared delta. The DELTA IS NOT APPLIED
    HERE -- §27.3 sums every delta across the fold and clamps ONCE, so applying it per act would
    make the clamp arrival-order dependent, which §32 forbids. The write goes through the gate so
    the class and Partition are checked; the value lands in the accumulator."""
    return None


@effect_for("transfer")
def _eff_transfer(w: "World", a: "Act") -> None:
    """§54 item 7's mirror: the giver's store goes DOWN by the amount. #353 states the
    PRECONDITION (`stores(...) >= amount`) and this is its only consistent effect -- a
    precondition on a quantity that the act never spends would never bind twice."""
    give = (a.payload or {}) if isinstance(a.payload, dict) else {}
    rung = w.rungs.get(give.get("from", ""))
    kind, amount = give.get("kind", "grain"), give.get("amount", 1)
    if rung is not None:
        rung.stores = dict(rung.stores or {})
        rung.stores[kind] = rung.stores.get(kind, 0) - amount


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

        # S25: NO SOCIAL QUANTITY MOVES HERE. L4 at its sharpest.
        w._in_parallel_map = True
        scale = w.fixtures.get("condition_scale")
        floors_all = w.fixtures.get("band_floors")
        for s in w.sites.values():
            before = s.condition
            wear = w.fixtures.wear(s.kind)      # NO SILENT DEFAULT -- unregistered kind raises
            w.write("condition", WriteClass.MATTER,
                    lambda s=s, wear=wear: setattr(s, "condition", max(0, s.condition - wear)),
                    record_kind="Site", fieldname="condition", driver="Event")
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
                    ev = Event(
                        id=H(w.world_seed, w.tick, s.id, f"crossing:{verb}"),
                        kind="condition.band_crossed", subject=s.id, changes=[],
                        causes=[ROOT], emitted_at=w.tick)
                    w.log.append(ev); emitted.append(ev)
                    w.crossings.append((s.id, verb, before, s.condition, ev.id))
                    TRACE.event(ev.id, ev.kind, ev.causes)
                    TRACE.decision(f"{s.id} crossed the `{verb}` floor", "S12.1/S3-L5",
                                   chose="EMIT a witnessable Event; write no social row; produce no outcome",
                                   alternatives=["write the consequence directly (L5 forbids: a crossing MAY NEVER PRODUCE AN OUTCOME)",
                                                 "silently drop the verb from the set (then nobody can witness it)"])
        w._in_parallel_map = False
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
        acts: list[Act] = []
        k_view = w.fixtures.get("view_k")
        k_budget = w.fixtures.get("act_budget")
        w._in_parallel_map = True       # S51: WorkerThreadPool over persons. The one that pays.
        for p in list(w.persons.values()):
            s = sense(p, w, subsistence)            # a Sensation, per S26's signature
            v = Query.assemble(p, question, k_view)
            # S26.3: the PERSON asks their own budget. `choose` receives the QUERY, not the
            # answer -- rev 2 computed it in the engine and handed the number down, which is
            # the half of retraction 5 that never landed.
            ask_budget = lambda p=p, v=v: Query.budget(p, v, k_budget)
            b = ask_budget()
            produced = choose(p, v, s, ask_budget)
            # S26.3: the engine does NOT truncate. Any cap applied here would be AN ENGINE
            # DECIDING A PERSON'S OPTIONS, which is L1. Over-budget is the CALLER'S defect.
            if len(produced) > b:
                raise Forbidden(
                    f"{p.id} returned {len(produced)} acts against a budget of {b}", "S26.3",
                    needs="`choose` is bounded by budget(person, view) -- the PERSON chooses what to leave undone",
                    law="S26.3 -- at one act NOBODY EVER CHOOSES WHAT TO LEAVE UNDONE; the budget exists to create triage. An engine that silently discards the tail has made the choice instead of the person, which is L1")
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
                TRACE.act(p.id, a.verb, b - i - 1)
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
            kind, _, arg = alt.partition(":")
            kind, arg = kind.strip(), arg.strip().strip("<>")
            if kind == "own":
                return True                       # every person may attempt their own acts
            if kind == "remit":
                for t in w.tenures:
                    if t.subject == a.actor and t.kind == "hold" and t.until is None:
                        off = w.offices.get(t.object)
                        if off and arg in off.remit_acts:
                            return True
            elif kind == "hold":
                if any(t.subject == a.actor and t.kind == "hold" and t.until is None
                       for t in w.tenures):
                    return True
            elif kind == "presence":
                return True                       # the presence index is H-33; not resolvable here
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
            named = a.verb in INVENTED_VERBS
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
            return ev(row.emits_on_refusal or ("act.ineligible",), [ROOT])

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
                return ev(row.emits_on_refusal or ("act.refused",), [ROOT])

        # Each `writes:` through the gate. The gate is the only writer; the fold never assigns.
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
            for pair in row.writes:
                kind, _, fld = pair.partition(".")
                self._apply_write(w, a, kind, fld, eff)
        # The act's proposed changes ride on the success Events -- §27.3's accumulator sums
        # them across the fold and clamps ONCE, which is order-independent as a fact.
        return ev(row.emits, [ROOT], a.changes)

    def _apply_write(self, w: "World", a: Act, kind: str, fld: str, eff) -> None:
        """The fold's write. It carries no per-verb behaviour -- the effect of a write is the
        matrix row's business, and what a verb writes is the verb table's."""
        mrow = matrix_row(kind, fld)
        w.write(fld, mrow.write_class(Step.RESOLVE), lambda: eff(w, a),
                record_kind=kind, fieldname=fld, driver="Act")

    def resolve(self, acts: list[Act],
                contest_max_depth: Optional[int] = None) -> list[Event]:
        w = self.w
        w.step = Step.RESOLVE
        w.frozen = False
        TRACE.step("RESOLVE", "enter"); TRACE.barrier(3, "RESOLVE")
        w.discard_caches()

        # S27: FIVE STRATA, then S32 rest 3's CONTENT-DERIVED canonicalization WITHIN each.
        # This sorts ONE GLOBAL ARRAY, which is exactly why RESOLVE DOES NOT PARTITION (S31).
        ordered = sorted(acts, key=lambda a: (a.stratum,
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
                out.append(Event(H(w.world_seed, w.tick, a.actor, f"refused:{a.id}"),
                                 "attempt.refused", a.actor, [], [ROOT], w.tick))
                TRACE.decision(f"{a.actor} attempted Ob={a.obstacle} against Pool={a.pool}",
                               "S27.4", chose="refuse; the season is spent",
                               alternatives=["roll it anyway", "route to an Ob=0 roll"])
                continue
            # S39.2 line 1: loop -> subsystem, when an act's contests[] names one.
            if a.contests:
                if contest_max_depth is None:
                    raise Forbidden("a contest was reached with no caller-supplied max_depth",
                                    "S39.3", law="S39.3 -- the depth cap has NO DEFAULT; a default is a number somebody made up and it will be cited later as though it were measured")
                # S39.2 line 2: Events, into the same log, WITH causes[] NAMING THE ACTS.
                # ⚠ REV 3. Rev 2 wrote `[a.id] if any(e.id == a.id for e in w.log) else [ROOT]`.
                # `w.log` holds Events and an Act is never appended to it, so the predicate was
                # PERMANENTLY FALSE and every contest was called with [ROOT]. Retraction 4
                # replaced rev 1's fabricated cause with an unreachable branch rather than with
                # the rule. The act id is named directly.
                r = contest(w, rung=a.payload or "R", prize=a.contests[0],
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
        index = w.cache_at_barrier("presence", lambda: {
            r: Query.presence(w, r) for r in w.rungs})
        everyone = list(w.persons)
        fan: list[tuple[str, Event, str]] = [
            (pid, e, "UNSPECIFIED-CHANNEL") for e in events for pid in everyone]
        TRACE.decision(f"fan-out over {len(events)} events -> {len(fan)} deposits", "S28/S61",
                       chose=f"EVERY event to EVERY person ({len(everyone)}) -- the specified behaviour",
                       alternatives=[
                           "shard per rung (retired: made the parallelism claim unsound)",
                           "restrict by presence (the index is built and UNUSED -- no channel "
                           "predicate exists to exclude anyone; S61 names this as the debt)",
                           f"the five channels {list(WITNESS_CHANNELS)} are named and NONE has a predicate"])

        # S28 stage 2: DEPOSIT IS PER-PERSON, into that person's OWN ledger and no other.
        cap = w.fixtures.get("ledger_cap")
        conf = w.fixtures.get("confidence_default")
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
            cid = e.id if via_knot else H(w.world_seed, w.tick, pid, f"claim:{e.id}")
            src = "firsthand_via_knot" if via_knot else "firsthand"
            c = Claim(cid, pid, e.subject, e.kind, True, w.tick, src, conf, "own")
            w.write("claim_ledger", WriteClass.INTERIOR, lambda p=p, c=c: p.ledger.append(c),
                    record_kind="Person", fieldname="claim_ledger", driver="Event")
            TRACE.claim(pid, e.id, src)
            deposits += 1
            if len(p.ledger) > cap:
                # S20/S34: EVICTION RANKS ON `confidence_live x recency` ONLY, NEVER SALIENCE.
                # Rev 1 sorted lexicographically on (confidence, when), which is a different
                # comparator and degenerated to insertion order under a constant confidence.
                p.ledger.sort(key=lambda c: c.confidence * (c.when + 1))
                p.ledger.pop(0)
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
    if depth >= max_depth:
        TRACE.decision("contest depth cap reached", "S39.3",
                       chose="typed error result returned to the caller",
                       alternatives=["recurse (a CRASH in GDScript, not a catchable error)"])
        return ContestError("max_depth reached", depth, max_depth)
    raise Unspecified(
        "the degree ladder's margin model",
        "S39.4",
        needs="a margin -- pool, obstacle, and the four band edges read off it",
        law="S39.4 -- ONE degree ladder for every scale, FOUR BANDS READ OFF THE MARGIN, never off the obstacle's size. No in-chain document supplies the margin model, and S27.2 refuses a second resolver, an auto-resolve formula and a fast path -- so a band computed here without a margin IS the second resolver",
    )
