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
    wear_per_season={"harbour": 10, "seam": 10, "body": 10},
    # S20: Claim.confidence. Rev 1 hardcoded 1, which degenerated the eviction comparator.
    confidence_default=100,
    # S15.2: entrenchment(h,H) = min(1, seasons_held / 60). The 60 IS in-chain; it is a fixture
    # only so no literal sits in a body.
    entrenchment_seasons=60,
    # S27.4: "an attempt at Ob > 2 x Pool is refused, and the season is spent."
    obstacle_refusal_multiple=2,
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


# S30's matrix, transcribed cell by cell. ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION.
WRITE_MATRIX: dict[str, set[Step]] = {
    "Date":               {Step.CALENDAR, Step.RESOLVE},
    "DocketItem":         {Step.CALENDAR, Step.RESOLVE},
    "ConveningCondition": {Step.CALENDAR, Step.RESOLVE},
    "stores":             {Step.MATTER, Step.RESOLVE},
    "body":               {Step.MATTER, Step.RESOLVE},
    "travel_leg":         {Step.MATTER, Step.RESOLVE},
    "yield":              {Step.MATTER},
    "envelope":           {Step.MATTER, Step.CENSUS},
    "condition":          {Step.MATTER, Step.RESOLVE},
    "Tenure":             {Step.MATTER, Step.RESOLVE},
    "carrier_exists":     {Step.MATTER, Step.RESOLVE, Step.CENSUS},
    "stance":             {Step.RESOLVE},
    "claim_ledger":       {Step.WITNESS},
    "acts_returned":      {Step.DELIBERATE},
}

WRITE_CLASS_OF: dict[tuple[str, Step], WriteClass] = {
    ("Date", Step.CALENDAR): WriteClass.CALENDAR,
    ("Date", Step.RESOLVE): WriteClass.ACTS,
    ("DocketItem", Step.CALENDAR): WriteClass.CALENDAR,
    ("DocketItem", Step.RESOLVE): WriteClass.ACTS,
    ("ConveningCondition", Step.CALENDAR): WriteClass.CALENDAR,
    ("ConveningCondition", Step.RESOLVE): WriteClass.ACTS,
    ("stores", Step.MATTER): WriteClass.MATTER,
    ("stores", Step.RESOLVE): WriteClass.ACTS,
    ("body", Step.MATTER): WriteClass.MATTER,
    ("body", Step.RESOLVE): WriteClass.ACTS,
    ("travel_leg", Step.MATTER): WriteClass.MATTER,
    ("travel_leg", Step.RESOLVE): WriteClass.ACTS,
    ("yield", Step.MATTER): WriteClass.MATTER,
    ("envelope", Step.MATTER): WriteClass.MATTER,
    ("envelope", Step.CENSUS): WriteClass.MATTER,
    ("condition", Step.MATTER): WriteClass.MATTER,
    ("condition", Step.RESOLVE): WriteClass.ACTS,
    ("Tenure", Step.MATTER): WriteClass.MATTER,
    ("Tenure", Step.RESOLVE): WriteClass.ACTS,
    ("carrier_exists", Step.MATTER): WriteClass.MATTER,
    ("carrier_exists", Step.RESOLVE): WriteClass.ACTS,
    ("carrier_exists", Step.CENSUS): WriteClass.MATTER,
    ("stance", Step.RESOLVE): WriteClass.ACTS,
    ("claim_ledger", Step.WITNESS): WriteClass.INTERIOR,
    ("acts_returned", Step.DELIBERATE): WriteClass.ACTS,
}

# ---------------------------------------------------------------------------
# THE PARTITION (L4). REV 2: every row carries its PROVENANCE, and there are only two
# admissible provenances. Nothing here is transcribed from intuition.
#
#   "chain"   -- ARCHITECTURE.md states the row. There is exactly ONE (S15.3).
#   "matrix"  -- S30's matrix DETERMINES it by construction: a thing the matrix admits at
#                MATTER is one the world may write, hence social:false; a thing the matrix
#                admits ONLY at RESOLVE (where the write class is ACTS) is act-only, hence
#                social:true. This derives the row rather than inventing it.
#
# EVERYTHING ELSE IS MISSING and raises. In particular `(Person, convictions)` and
# `(Person, beliefs)` are NOT in S30's matrix and are NOT stated, so they are MISSING --
# restoring a gap rev 1 had turned into a PASS.
# ---------------------------------------------------------------------------
PARTITION: dict[tuple[str, str], tuple[bool, str]] = {
    ("Tenure", "until"): (False, "chain S15.3 -- THE PARTITION'S ONE DECLARED SEAM"),
}
for _thing, _steps in WRITE_MATRIX.items():
    if _thing in ("acts_returned",):
        continue
    _social = _steps == {Step.RESOLVE}
    PARTITION[("*matrix*", _thing)] = (_social, f"matrix S30 -- writable at {sorted(s.value for s in _steps)}")

# The matrix names THINGS, not (record-kind, field) pairs. A derivation is valid ONLY where the
# matrix row IS the field -- otherwise `(Person, convictions)` rides on `stance`'s row and a real
# gap silently becomes a PASS, which is the invented-row defect in a different guise.
MATRIX_FIELD_OF: dict[tuple[str, str], str] = {
    ("Rung", "stores"): "stores",
    ("Rung", "envelope"): "envelope",
    ("Rung", "yield"): "yield",
    ("Site", "condition"): "condition",
    ("Person", "body"): "body",
    ("Person", "stance"): "stance",
    ("Person", "claim_ledger"): "claim_ledger",
    ("Person", "travel_leg"): "travel_leg",
    ("Tenure", "since"): "Tenure",
    ("Tenure", "until"): "Tenure",
    ("Date", "fired"): "Date",
    ("DocketItem", "matter"): "DocketItem",
    ("ConveningCondition", "attached"): "ConveningCondition",
}

PARTITION_MISSING: dict[tuple[str, str], str] = {
    ("Record", "*"): "S30.1 -- the design has NONE, so every Record write is an unmarked cell",
    ("Person", "exists"): "S30.1 -- without it a death write raises under the matrix's own rule",
}


def partition_lookup(record_kind: str, fieldname: str, thing: str) -> tuple[bool, str]:
    if (record_kind, "*") in PARTITION_MISSING:
        raise Unspecified(f"({record_kind}, *) has no Partition row", "S30.1",
                          needs="rule the row before adding it",
                          law=PARTITION_MISSING[(record_kind, "*")])
    if (record_kind, fieldname) in PARTITION_MISSING:
        raise Unspecified(f"({record_kind}, {fieldname}) has no Partition row", "S30.1",
                          needs="rule the row before adding it; the reverse order invents the thing the rule prevents",
                          law=PARTITION_MISSING[(record_kind, fieldname)])
    if (record_kind, fieldname) in PARTITION:
        return PARTITION[(record_kind, fieldname)]
    named = MATRIX_FIELD_OF.get((record_kind, fieldname))
    if named is not None and ("*matrix*", named) in PARTITION:
        return PARTITION[("*matrix*", named)]
    raise Unspecified(
        f"({record_kind}, {fieldname}) is on no Partition row and no matrix row determines it",
        "S30.1",
        needs="a `social:` column entry, ruled",
        law="L4 -- the membership test is a STATIC SCHEMA COLUMN, not a judgement; S42.3 -- configuring an unspecified thing invents it",
    )


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


TENURE_KINDS = {"hold", "contain", "commit", "oblige", "succeed", "tie", "knot"}


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


CLAIM_SOURCES = {"firsthand", "told_by", "inferred", "firsthand_via_knot"}
WITNESS_CHANNELS = ("post_remit", "co_located", "witness_key", "document_key", "chronicle")


class Sensation:
    """S18.2 -- EXACTLY TWO SCALARS.

    REV 2 HONESTY NOTE. S34's own enforcement column rates this `convention -- the named
    residual risk`, and rev 1 claimed the two-slot shape made widening structural. In Python
    it does not, any more than a GDScript convention does; S46.1's `Vector2` argument is a
    GODOT property this instrument cannot reproduce. `__slots__` is the nearest available
    approximation and it is still a convention a determined author can spell around."""
    __slots__ = ("subsistence", "standing")

    def __init__(self, subsistence: int, standing: int):
        self.subsistence = subsistence
        self.standing = standing

    def __iter__(self):
        return iter((self.subsistence, self.standing))


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
    stratum: int = 4
    obstacle: int = 0
    pool: int = 0


# S27: FIVE STRATA. movement / binding decisions / contested physical / uncontested material / social
STRATA = ("movement", "binding_decision", "contested_physical", "uncontested_material", "social")


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


REMIT_ACTS = {"issue", "determine", "confer", "revoke", "dispatch", "convene"}
RUNG_KINDS = ["person", "hearth", "community", "settlement",
              "territory", "province", "duchy", "realm"]


class Rung:
    """S10 -- THE HOLON. Eight kinds, ONE type. A Rung owns NO SOCIAL AGGREGATE (S10.1).

    REV 2: rev 1 blacklisted six spellings, so `r.morale` and `r.stability` passed. This is a
    WHITELIST over S10's declared field set -- a concept check rather than a term check.
    Any attribute not in S10's record raises, whatever it is called."""

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

    # -- S30.2: the write class is a PARAMETER of the store API, THE GATE APPLIES THE WRITE,
    # and `record_kind`/`fieldname` are REQUIRED so the L4 limb cannot be silenced by omission.
    def write(self, thing: str, wclass: WriteClass, apply: Callable[[], Any],
              record_kind: str, fieldname: str, driver: str,
              caused_person_exists: Optional[str] = None) -> Any:
        step = self.step
        sname = step.value if step else "-"
        allowed = WRITE_MATRIX.get(thing)
        if allowed is None:
            TRACE.write(thing, wclass.value, sname, False)
            raise Unspecified(f"'{thing}' has no row in the write matrix", "S30",
                              needs="rule the row first, then add it",
                              law="S30 -- ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION")
        if step not in allowed:
            TRACE.write(thing, wclass.value, sname, False)
            raise Forbidden(f"'{thing}' written during {sname}", "S30",
                            needs=f"one of {sorted(s.value for s in allowed)}",
                            law="S30 -- ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION")
        expect = WRITE_CLASS_OF.get((thing, step))
        if expect is not None and expect is not wclass:
            TRACE.write(thing, wclass.value, sname, False)
            raise Forbidden(
                f"'{thing}' written in class {wclass.value} at {sname}; matrix says {expect.value}",
                "S30.2", law="S30.2 -- the write class is a PARAMETER of the store API, checked PER WRITE SITE")
        social, prov = partition_lookup(record_kind, fieldname, thing)
        if social and driver != "Act":
            TRACE.write(thing, wclass.value, sname, False)
            raise Forbidden(
                f"({record_kind}, {fieldname}) is social:true and was written by {driver}", "S3-L4",
                needs="a named person's act",
                law=f"L4 -- social:true means ONLY AN ACT may write it. The world may silt a harbour; IT MAY NOT SOUR A TOWN'S MOOD. [row provenance: {prov}]")
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
                f"resolver-side Query '{name}' aggregates per-person tallies across holders",
                "S22.4", law="L3 clause 2 -- THAT IS STORED, MONOTONE, NEVER-DECAYING UNREST IN ALL BUT NAME -- worse than the field L3 banned, because the banned field could at least go down")
        if over_ended_edges:
            raise Forbidden(
                f"Query '{name}' composes over ENDED edges and is monotone", "S22.4",
                law="L3 clause 3 -- any Query monotone in the ENDED-edge set is a ratchet and is REFUSED. `count{commit}` over live AND ended rows is monotone; `count{hold: until != null}` is revocations-ever; each is built only from 'structural' edges and each EVADES clause 2")

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

        REV 2 fix. Rev 1 gave this a World first, so `choose` -- which correctly has none --
        could not ask its own budget, and `deliberate` silently truncated the tail. That is
        AN ENGINE DECIDING A PERSON'S OPTIONS, which is L1. It is person-side, `choose` asks
        it, and exceeding it RAISES rather than being trimmed."""
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


def sense(p: Person, w: World) -> Sensation:
    """S18.2 -- the ONE non-decision function permitted a World. EXACTLY TWO SCALARS.

    REV 2 fix: rev 1 returned `standing = 0` unconditionally -- the silent default S42.2.1
    names by name. S18.2 defines standing as "the gap between what everyone reads off you and
    what you hold" and NO SECTION COMPUTES IT; worse, "what everyone reads off you" is an
    aggregation ACROSS HOLDERS, which S22.4 clause 2 forbids outright. It raises."""
    TRACE.query("sense", "bridge")
    raise Unspecified(
        "Sensation.standing",
        "S18.2",
        needs="an aggregation producing 'what everyone reads off you' that does not cross holders",
        law="S18.2 names it; NO SECTION COMPUTES IT -- and the obvious computation is refused by S22.4 clause 2, which bars any resolver-side Query aggregating per-person values across holders",
    )


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


class SeasonDriver:
    """S23. Six steps, four barriers. DELIBERATE is a MAP, not a barrier; CENSUS SHARES
    WITNESS'S JOIN. S40.3/S44.3: NO CONTAINER GETS A CLOCK -- there is exactly one `season()`."""

    def __init__(self, w: World):
        self.w = w

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
        TRACE.decision("MATTER's three cross-owner operations", "S31.1",
                       chose="serial: event channel, then death cascade; then parallel over Sites and bodies",
                       alternatives=["shard the event channel per rung (breaks causes[])"])
        for e in (actorless or []):
            w.log.append(e); emitted.append(e)
            TRACE.event(e.id, e.kind, e.causes)

        # S25: NO SOCIAL QUANTITY MOVES HERE. L4 at its sharpest.
        w._in_parallel_map = True
        scale = w.fixtures.get("condition_scale")
        for s in w.sites.values():
            before = s.condition
            wear = w.fixtures.wear(s.kind)      # NO SILENT DEFAULT -- unregistered kind raises
            w.write("condition", WriteClass.MATTER,
                    lambda s=s, wear=wear: setattr(s, "condition", max(0, s.condition - wear)),
                    record_kind="Site", fieldname="condition", driver="Event")
            # S12.1/L5: A BAND EDGE CROSSING IS AN EMISSION, NOT A WRITE, and it is the L5
            # mechanism in its commonest form. Rev 1 had no crossing channel at all.
            w.crossings.append((s.id, before, s.condition))
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
            s = sense_subsistence_only(p, w, subsistence)
            v = Query.assemble(p, question, k_view)
            b = Query.budget(p, v, k_budget)        # person-side; `choose` asks its own budget
            produced = choose(p, v, s, b)
            # S26.3: the engine does NOT truncate. Any cap applied here would be AN ENGINE
            # DECIDING A PERSON'S OPTIONS, which is L1. Over-budget is the CALLER'S defect.
            if len(produced) > b:
                raise Forbidden(
                    f"{p.id} returned {len(produced)} acts against a budget of {b}", "S26.3",
                    needs="`choose` is bounded by budget(person, view) -- the PERSON chooses what to leave undone",
                    law="S26.3 -- at one act NOBODY EVER CHOOSES WHAT TO LEAVE UNDONE; the budget exists to create triage. An engine that silently discards the tail has made the choice instead of the person, which is L1")
            for i, a in enumerate(produced):
                TRACE.act(p.id, a.verb, b - i - 1)
                acts.append(a)
        w._in_parallel_map = False
        TRACE.step("DELIBERATE", "leave")
        return acts

    # -- RESOLVE -- barrier 3 -- the ONLY writing step for acts (S27) -------
    def resolve(self, acts: list[Act], effect: Callable[[World, Act], list[Event]],
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
            if a.obstacle and a.obstacle > mult * max(a.pool, 0):
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
                r = contest(w, rung=a.payload or "R", prize=a.contests[0],
                            claimants=[a.actor], depth=0, max_depth=contest_max_depth,
                            causes=[a.id] if any(e.id == a.id for e in w.log) else [ROOT])
                if isinstance(r, ContestError):
                    TRACE.note(f"contest returned {r}", "S39.3")
                else:
                    out.extend(r)
                continue
            # S27.1: CONTENTION IS AN ORDERED FOLD. Each act sees the world its predecessors
            # left. SEQUENCE, NOT SIMULTANEITY -- and NO ACT NEEDS TO KNOW ANOTHER EXISTED.
            produced = effect(w, a)
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
        index = w.cache_at_barrier("presence", lambda: {
            r: Query.presence(w, r) for r in w.rungs})
        fan: list[tuple[str, Event, str]] = []
        for e in events:
            observers = index.get(e.subject) or []
            if not observers and e.subject in w.persons:
                observers = [e.subject]
            for pid in observers:
                fan.append((pid, e, "co_located"))
            # S61: WITNESS AS SPECIFIED FANS EVERY EVENT TO EVERY PERSON. The five channels are
            # NAMED and their predicates are not given, so `co_located` above is the only one
            # this instrument can evaluate; the other four have no predicate to run.
        TRACE.decision(f"fan-out over {len(events)} events -> {len(fan)} deposits", "S28",
                       chose="one global pass over the presence index; channel `co_located` only",
                       alternatives=["shard per rung (retired: made the parallelism claim unsound)",
                                     f"the other four channels {WITNESS_CHANNELS[0::2]} have no predicate in chain"])

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
    def season(self, choose, effect, question, subsistence,
               actorless: Optional[list[Event]] = None,
               contest_max_depth: Optional[int] = None) -> dict:
        w = self.w
        self.calendar()
        matter_events = self.matter(actorless)
        acts = self.deliberate(choose, question, subsistence)
        events = self.resolve(acts, effect, contest_max_depth)
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
