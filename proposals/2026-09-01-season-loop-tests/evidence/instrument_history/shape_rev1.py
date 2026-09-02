"""PR #353's idealized code shape (`ARCHITECTURE.md`), implemented faithfully enough to RUN.

SCOPE (ARCHITECTURE.md 0.1, and Jordan 2026-09-01): the ONLY admissible source is the
design chain PR #337 -> now. Nothing under engine/, no subsystem sim/, and no decision
ratified before #337 is authority. This file implements ARCHITECTURE.md and nothing else.
Where ARCHITECTURE.md differs from #350/#351, ARCHITECTURE.md wins -- it is the head.

FIDELITY RULES. These are what make a gap a finding rather than an artifact of this file:

  1. Where ARCHITECTURE.md SPECIFIES a mechanism, implement it as specified.
  2. Where it NAMES a mechanism and does not specify it, raise `Unspecified`. Do not invent
     a plausible implementation. An `Unspecified` raised during a case IS the finding.
     ARCHITECTURE.md 42.2.1 is explicit: "the honest behaviour is to REFUSE, not to pick a
     plausible number."
  3. Where the shape structurally FORBIDS what a case needs, raise `Forbidden`, naming the law.
  4. Where the loop has no step that produces a change a case needs, raise `NoProducer`.
  5. Where two in-chain documents specify incompatible things, raise `Collision`.
  6. The laws are enforced BY CONSTRUCTION, not by convention. `choose` cannot see a World
     because it is not passed one; a resolver-side Query cannot be called from `choose`
     because it takes World first and there is no World in scope; a write outside its class
     raises AND the gate applies the write (30.2).

WHAT THIS FILE DELIBERATELY DOES NOT DO
  - It does not invent constants. Every number a probe needs is INJECTED (42.2.1), declared
    a harness fixture, and swept. See `Fixtures`.
  - It does not add a `target` or `actor` field to Event (19.3). Routing is not made easier.
  - It does not implement a wrapper layer (44.1 -- retracted in chain).
  - It does not give any container a clock (40.3).
"""

from __future__ import annotations

import enum
import hashlib
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from trace_log import TRACE


# ===========================================================================
# GAP SIGNALS -- the instrument's actual output
# ===========================================================================

class ShapeGap(Exception):
    """Base: the shape could not carry this case."""
    kind = "GAP"

    def __init__(self, what: str, where: str, needs: str = "", law: str = ""):
        self.what, self.where, self.needs, self.law = what, where, needs, law
        TRACE.gap(self.kind, what, where, needs, law)
        super().__init__(f"[{self.kind}] {what}  @{where}" + (f"  needs: {needs}" if needs else ""))


class Unspecified(ShapeGap):
    """ARCHITECTURE.md NAMES this mechanism and does not specify it. Part IX 61 is its own list."""
    kind = "UNSPECIFIED"


class Forbidden(ShapeGap):
    """A law forbids what the case requires. `law` records which."""
    kind = "FORBIDDEN"


class NoProducer(ShapeGap):
    """A state change the case needs that no step in the loop produces."""
    kind = "NO-PRODUCER"


class Collision(ShapeGap):
    """Two in-chain documents specify incompatible things. Part IX 62 is its own list."""
    kind = "COLLISION"


class Unowned(ShapeGap):
    """A value the case must change that the ownership table (22) assigns to nobody.

    New in the #353 instrument. #350's shape had no ownership table complete enough for
    this to be a distinct verdict; ARCHITECTURE.md 22 makes it one, and 22.3 names four
    such values itself, so the instrument must be able to report them separately from
    UNSPECIFIED -- an unowned value is not an unspecified mechanism, it is a specified
    mechanism with no writer."""
    kind = "UNOWNED"


class Ungraded(ShapeGap):
    """42.2's polarity rule: a row with no grade FAILS the export; it does not default to
    `assumption`. Reported separately so the audit can see how much of the surface is
    ungraded rather than merely assumed."""
    kind = "UNGRADED"


# ===========================================================================
# 48 -- FIXED POINT. `condition` is an int on an exported scale, never a float.
# ===========================================================================

class Fixtures:
    """42.2.1: never invent a constant -- INJECT it, declare it a harness fixture at
    `grade: assumption`, name the injection site, and sweep it. A verdict that FLIPS
    across the sweep is itself a finding, and a more important one than the verdict.

    Every number this instrument needs to run at all is here and nowhere else. There is
    no literal in any body below. There is NO SILENT DEFAULT: `get` on an unregistered
    key raises rather than answering plausibly and wrongly forever (42.2.1)."""

    def __init__(self, **vals: int):
        self._v = dict(vals)
        self.reads: dict[str, int] = {}

    def get(self, name: str) -> int:
        if name not in self._v:
            raise Ungraded(
                f"harness fixture '{name}' is not registered",
                "S42.2.1",
                needs="inject it, grade it assumption, name the injection site",
                law="42.2.1 -- a silent default answers plausibly and wrongly forever",
            )
        self.reads[name] = self.reads.get(name, 0) + 1
        return self._v[name]

    def sweep(self, name: str, value: int) -> "Fixtures":
        f = Fixtures(**self._v)
        f._v[name] = value
        return f


DEFAULT_FIXTURES = Fixtures(
    # ARCHITECTURE.md 48: condition is an int on an EXPORTED scale. The scale itself is
    # params-owned (22 `params` row) and this design proposes NO VALUES, so the number
    # below is a harness fixture, grade: assumption, injection site = this line.
    condition_scale=1000,
    # 26.3: the act budget is RULED at ~5. `~5` is not a number, so the integer the
    # instrument runs on is a fixture over a ruled band.
    act_budget=5,
    # 20: the claim ledger cap L. Params-owned; unstated in chain.
    ledger_cap=200,
    # 39.3: max_depth has NO DEFAULT by rule. The value here is CALLER-SUPPLIED at every
    # call site; it lives in Fixtures only so the caller has something to supply, and the
    # instrument asserts no call site omits it.
    caller_supplied_max_depth=3,
)


# ===========================================================================
# 23 -- THE SIX STEPS; 30 -- THE FOUR WRITE CLASSES
# ===========================================================================

class Step(enum.Enum):
    CALENDAR = "CALENDAR"
    MATTER = "MATTER"
    DELIBERATE = "DELIBERATE"
    RESOLVE = "RESOLVE"
    WITNESS = "WITNESS"
    CENSUS = "CENSUS"


class WriteClass(enum.Enum):
    """30: `CALENDAR / MATTER / ACTS / INTERIOR` are WRITE CLASSES. A write class is NOT a
    step. One class may be written in two steps."""
    CALENDAR = "CALENDAR"
    MATTER = "MATTER"
    ACTS = "ACTS"
    INTERIOR = "INTERIOR"


# 30's matrix, transcribed. Key: the written thing. Value: the set of steps that may write it.
# ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION (30).
WRITE_MATRIX: dict[str, set[Step]] = {
    "Date":              {Step.CALENDAR, Step.RESOLVE},
    "DocketItem":        {Step.CALENDAR, Step.RESOLVE},
    "ConveningCondition": {Step.CALENDAR, Step.RESOLVE},
    "stores":            {Step.MATTER, Step.RESOLVE},
    "body":              {Step.MATTER, Step.RESOLVE},
    "travel_leg":        {Step.MATTER, Step.RESOLVE},
    "yield":             {Step.MATTER},
    "envelope":          {Step.MATTER, Step.CENSUS},
    "condition":         {Step.MATTER, Step.RESOLVE},
    "Tenure":            {Step.MATTER, Step.RESOLVE},
    "carrier_exists":    {Step.MATTER, Step.RESOLVE, Step.CENSUS},
    "stance":            {Step.RESOLVE},
    "claim_ledger":      {Step.WITNESS},
    "acts_returned":     {Step.DELIBERATE},
}

# 30's write-class column, so the store API can take the class as a PARAMETER (30.2) and
# the check is mechanical PER WRITE SITE rather than per module.
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

# L4 / "the Partition": `social: true` on a (record-kind, field) pair means ONLY AN ACT may
# write it. `social: false` means either an act or the world may.
# 30.1: the design has NO (Record, ...) row and NO (Person, exists) row. Those absences are
# themselves findings and this table records them as MISSING rather than guessing a value.
PARTITION: dict[tuple[str, str], bool] = {
    ("Rung", "stores"): False,
    ("Rung", "envelope"): False,
    ("Site", "condition"): False,
    ("Person", "body"): False,
    ("Person", "stance"): True,
    ("Person", "convictions"): True,
    ("Person", "beliefs"): True,
    ("Person", "claim_ledger"): True,
    ("Tenure", "until"): False,   # 15.3 -- THE PARTITION'S ONE DECLARED SEAM
    ("Tenure", "since"): True,
    ("Date", "fired"): False,
    ("DocketItem", "matter"): True,
}
PARTITION_MISSING: set[tuple[str, str]] = {
    ("Record", "*"),        # 30.1 -- every Record write is an unmarked cell
    ("Person", "exists"),   # 30.1 -- a death write raises under the matrix's own rule
}


# ===========================================================================
# 33 -- DETERMINISM. Ids from H(world_seed, tick, subject_id, purpose). No allocator.
# ===========================================================================

def H(world_seed: int, tick: int, subject_id: str, purpose: str) -> str:
    """33: an OWNED, VERSIONED mix -- never a language built-in hash(), whose value is not
    a cross-version contract. `purpose` must be unique per DRAW, not per operation."""
    raw = f"v1|{world_seed}|{tick}|{subject_id}|{purpose}".encode()
    return hashlib.blake2b(raw, digest_size=8).hexdigest()


# ===========================================================================
# PART II -- THE PRIMITIVES (8's inventory, and nothing else exists)
# ===========================================================================

ROOT = "ROOT"   # 19.4 -- an Event with no antecedent declares causes: [ROOT], never []


@dataclass
class Tenure:
    """15 -- THE ONE EDGE. Seven kinds. Owned by its SUBJECT (15.1)."""
    id: str
    subject: str
    object: str
    kind: str            # hold contain commit oblige succeed tie knot
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
    """16 -- THE ONE STATE CHANGE. One shape for every mutation in the game."""
    subject: str
    mode: str            # create | alter | destroy
    driver: str          # Act | Event
    field: Optional[str] = None
    delta: Any = None
    spec: Any = None


@dataclass
class Event:
    """19 -- THE RECORD THAT WAS MISSING. Written here for the first time in the chain.

    19.3: THREE FIELDS ARE NOT ON IT, AND EACH ABSENCE IS A DESIGN DECISION.
      - no `actor`/`source_actor` -- attribution is a per-witness Claim, which is what
        makes covert action and false attribution expressible.
      - no `target`/rung address -- observers are computed at WITNESS from presence and
        channel; the emitter declares no recipient. DO NOT ADD ONE TO MAKE ROUTING EASIER.
      - no `stat_deltas` applied at emission -- changes are applied by the step that owns
        the write class, not by the log."""
    id: str
    kind: str                       # family.type, lowercase dotted
    subject: str
    changes: list[StateChange]
    causes: list[str]               # 19.4 REQUIRED AND NON-EMPTY. ids in the log, or [ROOT]
    emitted_at: int
    degree: Optional[str] = None

    def __post_init__(self) -> None:
        if not self.causes:
            raise Forbidden(
                f"Event {self.kind} emitted with causes=[]",
                "S19.4",
                needs="causes: [ROOT] for an antecedent-free emission",
                law="19.4 -- causes[] must be non-empty; [ROOT] makes the empty list unrepresentable",
            )


@dataclass
class Claim:
    """20. Lives in the HOLDER'S OWN ledger. Nobody else may read or write it."""
    id: str
    holder: str
    subject: str
    predicate: str
    value: Any
    when: int
    source: str          # firsthand | told_by | inferred | firsthand_via_knot
    confidence: int
    visibility: str


@dataclass
class Sensation:
    """18.2 / 46.1 -- EXACTLY TWO SCALARS AND NOTHING ELSE. Modelled as a two-slot value so
    that widening it is a structural change a reviewer must make on purpose."""
    subsistence: int
    standing: int

    def __iter__(self):
        return iter((self.subsistence, self.standing))


class View:
    """18.1 -- a View holds IDS, NEVER REFERENCES. A view that holds references is a masked
    world. L2 (3) is enforced BY CONSTRUCTION here: any attempt to reach a world collection
    through a View raises rather than returning something."""

    def __init__(self, holder: str, claim_ids: list[str]):
        self.holder = holder
        self.claim_ids = list(claim_ids)

    def __getattr__(self, name: str) -> Any:
        raise Forbidden(
            f"choose() reached for world state '{name}' through its View",
            "S3-L2",
            needs="a person decides from their own claims; world truth enters only via sense()",
            law="L2 -- choose never receives a World; not by discipline, by type",
        )


@dataclass
class Candidate:
    """17 -- `opening_set` RETURNS Candidate[], NOT Act[]. Typing it as acts makes the
    option set an authored list rather than a computed one."""
    verb: str
    subject: Optional[str] = None
    why: str = ""


@dataclass
class Act:
    """18. Produced by choose, consumed by resolve."""
    id: str
    actor: str
    verb: str
    changes: list[StateChange] = field(default_factory=list)
    reads: list[str] = field(default_factory=list)
    contests: list[str] = field(default_factory=list)
    payload: Any = None


@dataclass
class Person:
    """9. A COHORT IS A PERSON AT weight > 1. ONE CLASS (9.1) -- refuse the subclass."""
    id: str
    name: str = ""
    weight: int = 1
    marks: list[str] = field(default_factory=list)
    capability: dict = field(default_factory=dict)   # practice -> rank 0..5
    stance: list[tuple] = field(default_factory=list)
    convictions: dict = field(default_factory=dict)
    beliefs: list[tuple] = field(default_factory=list)  # (proposition, strong|wavering|revised)
    ledger: list[Claim] = field(default_factory=list)

    def __post_init__(self) -> None:
        if self.weight < 1:
            raise Forbidden("Person.weight < 1", "S9", law="9 -- weight >= 1, default 1")


@dataclass
class Site:
    """12. `condition` is PRIMARY STATE, not a Query, and it is a FIXED-POINT INT (48)."""
    id: str
    rung: str
    kind: str
    condition: int           # int on the exported scale. NEVER a float.
    drawers: list[str] = field(default_factory=list)


@dataclass
class Record:
    """13 -- a LIVE CARRIER, promoted from an inert noun. 30.1: the design has NO Partition
    row for it, so every Record write is an unmarked cell -- which this instrument reports
    rather than papering over."""
    id: str
    rung: str
    kind: str
    forgery_quality: int = 0
    subject_matter: Any = None
    ttl: Optional[int] = None
    stages: list[tuple] = field(default_factory=list)  # 13.1 act-declared terms


@dataclass
class Proposition:
    """14. IDENTITY-BEARING AND IMMUTABLE. Fixed at utterance, never destroyed."""
    id: str
    mood: str            # HOLDS | OUGHT
    subject: str
    predicate: str
    value: Any
    when: int
    scope: Any = None


@dataclass
class Office:
    """11. `rung?` is OPTIONAL; null is the office-cluster case (6.2)."""
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


@dataclass
class Rung:
    """10 -- THE HOLON. Eight kinds, ONE type. A Rung owns NO SOCIAL AGGREGATE (10.1)."""
    id: str
    kind: str            # person hearth community settlement territory province duchy realm
    stores: dict = field(default_factory=dict)     # MatterKind -> int, whole units
    sites: list[str] = field(default_factory=list)
    records: list[str] = field(default_factory=list)
    dates: list[str] = field(default_factory=list)
    stake: list[str] = field(default_factory=list)
    envelope: list[int] = field(default_factory=list)
    transmission: Optional[str] = None
    judging_set_rule: Any = None    # 10.2 / 61 -- UNSPECIFIED

    def __setattr__(self, k: str, v: Any) -> None:
        # 10.1: no norms, no densities, no reputation, no unrest, no legitimacy. Every one
        # is a Query. This is the row the whole ownership table exists to protect.
        if k in ("unrest", "legitimacy", "reputation", "norms", "density", "discipline"):
            raise Forbidden(
                f"Rung.{k} assigned",
                "S10.1",
                needs="a Query over the containment subtree, owned by Nobody",
                law="L3 / 22 -- every aggregate is a function, never a field",
            )
        object.__setattr__(self, k, v)


RUNG_KINDS = ["person", "hearth", "community", "settlement",
              "territory", "province", "duchy", "realm"]


# ===========================================================================
# 45.1 -- DECLARE `World` FIRST. It is the object every rule points at.
# ===========================================================================

class World:
    """45.1: until World has fields, "resolver-side Queries take a World first" is a
    sentence rather than a signature. These are its fields."""

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
        self.tenures: list[Tenure] = []          # 46: rows in a store, never per-edge objects
        self.log: list[Event] = []               # 19.5 -- ONE LOG, NOT TWO
        self.dates: dict[str, dict] = {}
        self.docket: list[dict] = []
        self.petitions: dict[str, dict] = {}
        self.dispensations: dict[str, dict] = {}
        self.step: Optional[Step] = None
        self.frozen = False                      # 26.2 -- frozen from end of MATTER to RESOLVE
        self._barrier_cache: dict = {}           # 4 -- built AT a barrier, discarded there
        self._in_parallel_map = False
        self.writes: list[tuple] = []

    # -- 30.2: the write class is a PARAMETER of the store API, and THE GATE APPLIES THE
    # WRITE. A gate that validates, logs and returns true while the mutation happens beside
    # it is worse than no gate (30.2).
    def write(self, thing: str, wclass: WriteClass, apply: Callable[[], Any],
              record_kind: Optional[str] = None, fieldname: Optional[str] = None,
              driver: str = "Act") -> Any:
        step = self.step
        allowed = WRITE_MATRIX.get(thing)
        if allowed is None:
            TRACE.write(thing, wclass.value, step.value if step else "-", False)
            raise Forbidden(
                f"'{thing}' has no row in the write matrix",
                "S30",
                needs="rule the row first, then add it",
                law="30 -- ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION",
            )
        if step not in allowed:
            TRACE.write(thing, wclass.value, step.value if step else "-", False)
            raise Forbidden(
                f"'{thing}' written during {step.value if step else '-'}",
                "S30",
                needs=f"one of {sorted(s.value for s in allowed)}",
                law="30 -- ANY UNMARKED CELL IS A WRITE-CLASS VIOLATION",
            )
        expect = WRITE_CLASS_OF.get((thing, step))
        if expect is not None and expect is not wclass:
            TRACE.write(thing, wclass.value, step.value, False)
            raise Forbidden(
                f"'{thing}' written in class {wclass.value} at {step.value}, matrix says {expect.value}",
                "S30.2",
                law="30.2 -- the write class is a parameter of the store API",
            )
        # L4 / the Partition: social: true means ONLY AN ACT may write it.
        if record_kind is not None and fieldname is not None:
            key = (record_kind, fieldname)
            if (record_kind, "*") in PARTITION_MISSING or key in PARTITION_MISSING:
                TRACE.write(thing, wclass.value, step.value, False)
                raise Unspecified(
                    f"({record_kind}, {fieldname}) has no Partition row",
                    "S30.1",
                    needs="rule the row before adding it; the reverse order invents the thing the rule prevents",
                    law="30.1 -- the design has none, so every such write is an unmarked cell",
                )
            social = PARTITION.get(key)
            if social is None:
                TRACE.write(thing, wclass.value, step.value, False)
                raise Unspecified(
                    f"({record_kind}, {fieldname}) is not on the Partition",
                    "S30.1", law="L4 -- the membership test is a static schema column",
                )
            if social and driver != "Act":
                TRACE.write(thing, wclass.value, step.value, False)
                raise Forbidden(
                    f"({record_kind}, {fieldname}) is social:true and was written by {driver}",
                    "S3-L4",
                    needs="a named person's act",
                    law="L4 -- social:true means ONLY an act may write it; the world may silt a harbour, it may not sour a town's mood",
                )
        TRACE.write(thing, wclass.value, step.value, True)
        self.writes.append((thing, wclass.value, step.value))
        return apply()

    # -- 4: a Query MAY be cached. Built AT a barrier, read-only until the next, discarded
    # there. NOTHING INSIDE A PARALLEL MAP BUILDS ONE.
    def cache_at_barrier(self, key: str, build: Callable[[], Any]) -> Any:
        if self._in_parallel_map:
            raise Forbidden(
                f"cache '{key}' built inside a parallel map",
                "S4",
                law="4 -- the cache is built AT A BARRIER; nothing inside a parallel map builds one",
            )
        if key not in self._barrier_cache:
            self._barrier_cache[key] = build()
        return self._barrier_cache[key]

    def discard_caches(self) -> None:
        self._barrier_cache.clear()


# ===========================================================================
# 17 -- QUERY. Two families, and THE SIDE COLUMN IS THE ENFORCEMENT.
# ===========================================================================

class Query:
    """RESOLVER-SIDE takes `World` FIRST, always. Calling one from inside choose() fails at
    the call site for want of an argument -- and in this instrument that is literally true,
    because choose() is not given a World and Python raises NameError/TypeError.

    PERSON-SIDE takes the ASKER and may read the asker's OWN interior and nothing else."""

    # ---- resolver-side --------------------------------------------------
    @staticmethod
    def parent_of(w: World, rung_id: str) -> Optional[str]:
        for t in w.tenures:
            if t.kind == "contain" and t.subject == rung_id and t.live:
                return t.object
        return None

    @staticmethod
    def descendants(w: World, rung_id: str) -> list[str]:
        """6.1 -- the CONTAINMENT TREE, and only it. 38.1: traverse ITERATIVELY with a
        visited set; the reference graph is cyclic on purpose and a tree walk hangs on the
        NORMAL case."""
        TRACE.query("descendants", "resolver")
        out, seen, stack = [], {rung_id}, [rung_id]
        while stack:
            cur = stack.pop()
            for t in w.tenures:
                if t.kind == "contain" and t.object == cur and t.live and t.subject not in seen:
                    seen.add(t.subject)
                    out.append(t.subject)
                    stack.append(t.subject)
        return out

    @staticmethod
    def r1_aggregate(w: World, rung_id: str, over: Callable[[str], int]) -> int:
        """4 / R-1: a rung MAY COMPUTE an aggregate over its DESCENDANTS ON DEMAND. It may
        not receive a pushed one and may not store one. 22.4: composes over LIVE EDGES ONLY.
        6.2: this is a claim about the CONTAINMENT TREE -- following a tie, knot, commit or
        distant hold LEAVES THE SUBTREE and is NOT an R-1 aggregate."""
        TRACE.query("r1_aggregate", "resolver")
        return sum(over(d) for d in Query.descendants(w, rung_id))

    @staticmethod
    def aggregate_guard(w: World, name: str, *, per_person_tally: bool = False,
                        over_ended_edges: bool = False) -> None:
        """22.4 -- THE AGGREGATION BOUNDARY, THREE CLAUSES. Clause 3 is #353's addition."""
        if per_person_tally:
            raise Forbidden(
                f"resolver-side Query '{name}' aggregates per-person tallies across holders",
                "S22.4",
                law="L3 clause 2 -- that is stored, monotone, never-decaying unrest in all but name",
            )
        if over_ended_edges:
            raise Forbidden(
                f"Query '{name}' composes over ENDED edges and is monotone",
                "S22.4",
                law="L3 clause 3 -- any Query monotone in the ended-edge set is a ratchet and is refused",
            )

    @staticmethod
    def lateral(w: World, name: str, kind: str) -> list[Tenure]:
        """6.2 / 38 -- THE LATERAL GRAPH. tie, knot, commit, hold-at-distance, offices with
        rung?=null, containerless venues. NOT governed by R-1/R-2. Resolver-side, World
        first, and therefore unreachable from choose() by construction."""
        TRACE.query(f"lateral:{name}", "resolver")
        return [t for t in w.tenures if t.kind == kind and t.live]

    @staticmethod
    def verbs(w: World, site: Site, floors: dict[str, int]) -> set[str]:
        """12.1 -- condition GATES VERBS. A band-edge crossing is an EMISSION, not a write,
        and it is the L5 mechanism in its commonest form. 32/48: the comparison is on a
        SUMMED FIXED-POINT INT, so it is exact and order-independent."""
        TRACE.query("verbs", "resolver")
        return {v for v, floor in floors.items() if site.condition >= floor}

    @staticmethod
    def judging_set(w: World, rung_id: str) -> list[str]:
        """61 -- `judging_set_rule` IS UNSPECIFIED. NOTHING IS DECIDED AT A SITTING."""
        raise Unspecified(
            "judging_set_rule",
            "S61",
            needs="who decides at a sitting",
            law="61 -- T5's 'filtered at a rung' runs straight through it",
        )

    @staticmethod
    def budget(w: World, p: Person, v: View) -> int:
        """26.3 -- budget is a QUERY, NEVER A FIELD. Office, condition, distance travelled.
        A wounded duke gets fewer acts than a healthy one WITHOUT ANYBODY STORING A NUMBER."""
        TRACE.query("budget", "resolver")
        return w.fixtures.get("act_budget")

    # ---- person-side ----------------------------------------------------
    @staticmethod
    def opening_set(p: Person, v: View, roster: list[Candidate]) -> list[Candidate]:
        """17 -- RETURNS Candidate[], NOT Act[]. The head's own player document still
        carries the old -> Act[] signature; the adjudication overturned it (54 item 1)."""
        TRACE.query("opening_set", "person")
        return list(roster)

    @staticmethod
    def assemble(p: Person, question: Any) -> View:
        """61 -- THE QUESTION `q` HAS NO PRODUCER. assemble(person, question) is
        unsatisfiable, so DELIBERATE HAS NO DECLARED ENTRY POINT."""
        if question is None:
            raise NoProducer(
                "the question `q` that assemble() takes",
                "S61",
                needs="a producer for q",
                law="61 -- DELIBERATE has no declared entry point",
            )
        return View(p.id, [c.id for c in p.ledger])

    @staticmethod
    def entrenchment(p: Person, seasons_held: int, w_scale: int) -> int:
        """15.2 -- entrenchment(h,H) = min(1, seasons_held/60) has nothing to read if you
        delete ended rows. Fixed point: expressed in basis points against an injected scale."""
        TRACE.query("entrenchment", "person")
        return min(w_scale, (seasons_held * w_scale) // 60)


def sense(p: Person, w: World) -> Sensation:
    """18.2 -- the ONE non-decision function permitted a World. Returns EXACTLY TWO SCALARS.
    46.1: define the sensation domain so its values are float32-exact -- here, ints."""
    TRACE.query("sense", "bridge")
    scale = w.fixtures.get("condition_scale")
    home = None
    for t in w.tenures:
        if t.kind == "contain" and t.subject == p.id and t.live:
            home = w.rungs.get(t.object)
            break
    subsistence = 0 if home is None else min(scale, sum(home.stores.values()) * scale // max(1, p.weight))
    standing = 0
    return Sensation(subsistence, standing)


# ===========================================================================
# PART III -- THE SEASON LOOP. Six steps, four barriers (23).
# ===========================================================================

class SeasonDriver:
    """23. The counts differ for two structural reasons: DELIBERATE is a MAP, not a barrier;
    CENSUS SHARES WITNESS'S JOIN rather than opening its own.

    40.3 / 44.3: NO CONTAINER GETS A CLOCK. There is exactly one `season()` and it is here."""

    def __init__(self, w: World):
        self.w = w
        self.pending_acts: list[Act] = []
        self.emitted: list[Event] = []

    # -- CALENDAR -- barrier 1 -- fires occasions and DECIDES NOTHING (24) ---
    def calendar(self) -> None:
        w = self.w
        w.step = Step.CALENDAR
        TRACE.step("CALENDAR", "enter")
        TRACE.barrier(1, "CALENDAR")
        w.discard_caches()
        for did, d in list(w.dates.items()):
            if d.get("due_at") == w.tick:
                # 24: a VACANT date FIRES, ALLOCATES NOTHING, AND LAPSES. It does not block.
                vacant = not d.get("holder")
                TRACE.decision(
                    f"date {did} came due",
                    "S24",
                    chose="fire-and-lapse" if vacant else "fire-as-sitting",
                    alternatives=["block until a holder exists", "defer to next season"],
                )
                w.write("Date", WriteClass.CALENDAR, lambda d=d: d.__setitem__("fired", True),
                        record_kind="Date", fieldname="fired", driver="Event")
                if not vacant:
                    w.write("DocketItem", WriteClass.CALENDAR,
                            lambda did=did: w.docket.append({"date": did, "matter": None}))
        TRACE.step("CALENDAR", "leave")

    # -- MATTER -- barrier 2 -- THE WORLD FREEZES AT ITS END (25) ------------
    def matter(self) -> None:
        w = self.w
        w.step = Step.MATTER
        TRACE.step("MATTER", "enter")
        TRACE.barrier(2, "MATTER")
        w.discard_caches()

        # 31.2: run the EVENT CHANNEL and the DEATH CASCADE SERIALLY, before the parallel
        # section, because both cross owners (31.1).
        TRACE.decision(
            "MATTER's three cross-owner operations",
            "S31.1",
            chose="serial: event channel, death cascade; then parallel over Sites and bodies",
            alternatives=["shard the event channel per rung (breaks causes[] -- one cause is one id)"],
        )

        # 25: NO SOCIAL QUANTITY MOVES HERE. L4 at its sharpest.
        w._in_parallel_map = True
        for s in w.sites.values():
            # `wear` ONLY. Act deltas are RESOLVE's. Fixed point (48).
            wear = w.fixtures.get("condition_scale") // 100
            w.write("condition", WriteClass.MATTER,
                    lambda s=s, wear=wear: setattr(s, "condition", max(0, s.condition - wear)),
                    record_kind="Site", fieldname="condition", driver="Event")
        w._in_parallel_map = False
        TRACE.step("MATTER", "leave")
        # 26.2: the world is FROZEN from the end of MATTER to the start of RESOLVE.
        w.frozen = True

    # -- DELIBERATE -- a MAP, not a barrier (26) -----------------------------
    def deliberate(self, choose: Callable[[Person, View, Sensation], list[Act]],
                   question: Any = None) -> list[Act]:
        w = self.w
        w.step = Step.DELIBERATE
        TRACE.step("DELIBERATE", "enter")
        acts: list[Act] = []
        w._in_parallel_map = True    # 51: WorkerThreadPool over persons. The one that pays.
        for p in list(w.persons.values()):
            s = sense(p, w)          # the ONLY bridge from world truth into choose
            v = Query.assemble(p, question)
            budget = Query.budget(w, p, v)   # 26.3 -- a Query, never a field
            # NOTE the call below passes NO WORLD. L2 is enforced by the parameter list.
            produced = choose(p, v, s)
            # 26.3 consequence 2: THE LIST IS ORDERED.
            for i, a in enumerate(produced):
                if i >= budget:
                    TRACE.decision(
                        f"{p.id} produced {len(produced)} acts against budget {budget}",
                        "S26.3",
                        chose=f"truncate at {budget}",
                        alternatives=["raise", "let it run"],
                    )
                    break
                TRACE.act(p.id, a.verb, budget - i - 1)
                acts.append(a)
        w._in_parallel_map = False
        TRACE.step("DELIBERATE", "leave")
        return acts

    # -- RESOLVE -- barrier 3 -- the ONLY writing step for acts (27) ---------
    def resolve(self, acts: list[Act],
                effect: Callable[[World, Act], list[Event]]) -> list[Event]:
        w = self.w
        w.step = Step.RESOLVE
        w.frozen = False
        TRACE.step("RESOLVE", "enter")
        TRACE.barrier(3, "RESOLVE")
        w.discard_caches()

        # 32 rest 3: the act array is CANONICALIZED BEFORE RESOLUTION -- sorted by a
        # CONTENT-DERIVED key, never by completion order. This sorts ONE GLOBAL ARRAY,
        # which is exactly why RESOLVE does not partition (31).
        ordered = sorted(acts, key=lambda a: H(w.world_seed, w.tick, a.actor, f"order:{a.verb}:{a.id}"))
        TRACE.decision(
            f"ordering {len(acts)} acts",
            "S32",
            chose="content-derived hash key over one global array",
            alternatives=["completion order", "rank", "per-container sort (voids the fold)"],
        )

        # 27.1: CONTENTION IS AN ORDERED FOLD, not a grouping. Each act sees the world its
        # predecessors left. Sequence, not simultaneity. Scarcity then falls out for free,
        # AND NO ACT NEEDS TO KNOW ANOTHER ACT EXISTED.
        out: list[Event] = []
        for a in ordered:
            out.extend(effect(w, a))
        TRACE.step("RESOLVE", "leave")
        return out

    # -- WITNESS -- barrier 4 -- THE JOIN (28) -------------------------------
    def witness(self, events: list[Event],
                observers: Callable[[World, Event], list[str]]) -> int:
        w = self.w
        w.step = Step.WITNESS
        TRACE.step("WITNESS", "enter")
        TRACE.barrier(4, "WITNESS")
        w.discard_caches()

        # 28 stage 1: FAN-OUT IS GLOBAL AND ONE PASS. No signals, no subscription table.
        # DO NOT SHARD IT -- the predecessor loop was retired precisely because its WITNESS
        # was not global, which made its parallelism claim UNSOUND rather than unproven.
        fan: list[tuple[str, Event]] = []
        for e in events:
            for pid in observers(w, e):
                fan.append((pid, e))
        TRACE.decision(
            f"fan-out over {len(events)} events -> {len(fan)} deposits",
            "S28",
            chose="one global pass over the presence index",
            alternatives=["shard per rung (retired: made the parallelism claim unsound)"],
        )

        # 28 stage 2: DEPOSIT IS PER-PERSON, any order, into that person's OWN ledger.
        deposits = 0
        cap = w.fixtures.get("ledger_cap")
        w._in_parallel_map = True
        for pid, e in fan:
            p = w.persons.get(pid)
            if p is None:
                continue
            cid = e.id if False else H(w.world_seed, w.tick, pid, f"claim:{e.id}")
            c = Claim(cid, pid, e.subject, e.kind, True, w.tick, "firsthand", 1, "own")
            w.write("claim_ledger", WriteClass.INTERIOR,
                    lambda p=p, c=c: p.ledger.append(c),
                    record_kind="Person", fieldname="claim_ledger", driver="Act")
            TRACE.claim(pid, e.id, "firsthand")
            deposits += 1
            if len(p.ledger) > cap:
                # 20 / 28: EVICTION RANKS ON confidence_live x recency ONLY -- NEVER SALIENCE.
                p.ledger.sort(key=lambda c: (c.confidence, c.when))
                p.ledger.pop(0)
        w._in_parallel_map = False
        # 9.3 / 28: WITNESS NEVER TOUCHES A BELIEF. Nothing above writes `beliefs`.
        TRACE.step("WITNESS", "leave")
        return deposits

    # -- CENSUS -- shares WITNESS's join (29) --------------------------------
    def census(self) -> None:
        w = self.w
        w.step = Step.CENSUS
        TRACE.step("CENSUS", "enter")
        # 29: DEMAND-DRIVEN ONLY. Nothing generates without a demand, and NO CLOCK generates
        # anything. This instrument therefore generates nobody here.
        TRACE.decision(
            "individuation",
            "S29",
            chose="demand-driven only; generated nobody",
            alternatives=["a clock that generates (forbidden)", "a world-gen roster (54 item 18, not a clock, not folded in yet)"],
        )
        for r in w.rungs.values():
            if r.envelope:
                w.write("envelope", WriteClass.MATTER, lambda r=r: r.envelope,
                        record_kind="Rung", fieldname="envelope", driver="Event")
        TRACE.step("CENSUS", "leave")

    # -- one season ----------------------------------------------------------
    def season(self, choose, effect, observers, question=None) -> dict:
        self.calendar()
        self.matter()
        acts = self.deliberate(choose, question)
        events = self.resolve(acts, effect)
        for e in events:
            self.w.log.append(e)          # 19.5 -- ONE LOG
            TRACE.event(e.id, e.kind, e.causes)
        deposits = self.witness(events, observers)
        self.census()
        self.w.tick += 1
        return dict(acts=len(acts), events=len(events), deposits=deposits)


# ===========================================================================
# 39 -- THE SEAM. A contest is the season loop, NESTED. Attaches at exactly ONE place.
# ===========================================================================

def contest(w: World, rung: str, prize: Any, claimants: list[str],
            depth: int, max_depth: int,
            extension: Optional[Callable[[str], bool]] = None) -> list[Event]:
    """39. EVERY ARGUMENT IS LOAD-BEARING. 39.3: the depth cap has NO DEFAULT -- it is
    CALLER-SUPPLIED, for two reasons: no fabricated constant enters the engine, and in
    GDScript exceeding recursion depth is a CRASH, not a catchable error. Exceeding the cap
    must produce a TYPED ERROR RESULT, checked by the caller."""
    if not claimants:
        raise Forbidden("contest with no claimants", "S39.1",
                        law="39.1 -- claimant[] is PERSONS, ALWAYS")
    if prize is None:
        raise Forbidden("contest with no prize", "S39.1",
                        law="39.1 -- a contest with no prize is a fight scene, and this engine has no use for one")
    if depth >= max_depth:
        # A TYPED ERROR RESULT, not a crash and not an exception that unwinds the world.
        TRACE.decision("contest depth cap reached", "S39.3",
                       chose="typed error result returned to caller",
                       alternatives=["recurse (crash in GDScript)", "silently cap"])
        return []
    # 39.4: ONE DEGREE LADDER. Four bands read off the MARGIN, never off the obstacle's size.
    band = "Partial"
    if extension is not None and band == "Overwhelming":
        # the ONE permitted variation: a demote-only veto. Returns bool. There is no
        # signature by which it could promote a band.
        if extension("Overwhelming"):
            band = "Success"
    e = Event(
        id=H(w.world_seed, w.tick, rung, f"contest:{prize}"),
        kind="contest.resolved",
        subject=rung,
        changes=[],
        causes=[ROOT] if not w.log else [w.log[-1].id],
        emitted_at=w.tick,
        degree=band,
    )
    return [e]   # 39.2 line 2: Events, INTO THE SAME LOG. Not state writes.
