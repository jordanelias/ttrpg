"""The idealized code shape of PR #350, implemented faithfully enough to RUN.

This is a TRACER, not an engine. Its job is to execute the shape's season loop over real
cases and record, mechanically, every place the shape cannot express what a case requires.

FIDELITY RULES — these are what make a gap a finding rather than an artifact of this file:

  1. Where the suite specifies a mechanism, implement it as specified.
  2. Where the suite names a mechanism and does NOT specify it, raise `Unspecified`.
     Do not invent a plausible implementation. An `Unspecified` raised during a case IS the
     finding; papering over it destroys the measurement.
  3. Where the shape structurally forbids something a case needs, raise `Forbidden`.
  4. The four laws are enforced by construction, not by convention. `choose` cannot see a
     World because it is not passed one; a write outside its class raises.

Source: proposals/2026-08-31-unified-code-shape/{01,02,03,04,05,06,07,08}.md
"""

from __future__ import annotations

import enum
from dataclasses import dataclass, field
from typing import Any, Callable, Optional

from trace_log import TRACE


# ---------------------------------------------------------------------------
# GAP SIGNALS — the instrument's actual output
# ---------------------------------------------------------------------------

class ShapeGap(Exception):
    """Base: the shape could not carry this case."""
    kind = "GAP"

    def __init__(self, what: str, where: str, needs: str = ""):
        self.what, self.where, self.needs = what, where, needs
        TRACE.gap(self.kind, what, where, needs)
        super().__init__(f"[{self.kind}] {what}  @{where}" + (f"  needs: {needs}" if needs else ""))


class Unspecified(ShapeGap):
    """The suite NAMES this mechanism and does not specify it. `02` §5.5's scar is the type case."""
    kind = "UNSPECIFIED"


class Forbidden(ShapeGap):
    """A law forbids what the case requires. Records the law and the cost."""
    kind = "FORBIDDEN"


class NoProducer(ShapeGap):
    """A state change the case needs, that no step in the loop produces."""
    kind = "NO-PRODUCER"


class Collision(ShapeGap):
    """Two documents of the suite specify incompatible things."""
    kind = "COLLISION"


# ---------------------------------------------------------------------------
# §04 — THE SIX STEPS AND THE FOUR WRITE CLASSES
# ---------------------------------------------------------------------------

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


# `04` §4: which write classes may fire in which step. A class is not a phase; one class may
# appear in two steps. What is forbidden is a write OUTSIDE its class.
LEGAL_WRITES: dict[Step, set[WriteClass]] = {
    Step.CALENDAR:   {WriteClass.CALENDAR},
    Step.MATTER:     {WriteClass.MATTER},
    Step.DELIBERATE: set(),                    # a map, not a barrier: NO writes
    Step.RESOLVE:    {WriteClass.ACTS},
    Step.WITNESS:    {WriteClass.INTERIOR},
    Step.CENSUS:     {WriteClass.MATTER},
}

# `01` Law 4 / `02` §5.1 — the Partition, keyed on (record-kind, field), ASYMMETRIC:
#   social: True  => ACT-DRIVEN ONLY. An Event may never write this row.
#   social: False => EITHER driver.
SOCIAL: dict[tuple[str, str], bool] = {
    ("Rung", "exists"): True,
    ("Rung", "matter.stores"): False,
    ("Rung", "envelope"): False,
    ("Site", "condition"): False,
    ("Office", "post"): True,
    ("Office", "establishment"): True,
    ("Tenure", "hold"): True,
    # ⚠ ADDED 2026-08-31 after a read-only audit found it MISSING, which is instrument defect
    # five and the first to point the DAMNING way — an omitted ruled row makes the shape look
    # WORSE than it is, and the guard at test_tracer_is_honest.py only covered invented rows.
    # `02` §5.1 RULES this outright: "(Tenure, until) is social: false. Otherwise death cannot
    # end a tenure and the entire succession mechanism has no producer." It is called "the
    # Partition's one declared seam" and it is bounded by a causation rule, enforced below.
    ("Tenure", "until"): False,
    ("Tenure", "contain"): False,     # a body may be moved by a landslide
    ("Tenure", "commit"): True,
    ("Tenure", "oblige"): True,
    ("Tenure", "succeed"): True,
    ("Person", "ledger"): False,      # claims arrive by witnessing an Event
    ("Person", "stance"): True,
    ("Person", "weight"): False,      # ADVERSARIAL row 13: only CENSUS writes it, and CENSUS is
                                      # not a person acting — flagged there, kept here as ruled
}
# DELIBERATELY ABSENT, because the suite does not have them. `ADVERSARIAL.md` rows 14/15/16 find:
#   ("Person", "capability")   -- "no row in the `04` §4 write matrix, so every advancement is an
#                                 unmarked cell"
#   ("Person", "convictions")  -- "no rows in the write matrix at all"
#   ("Person", "beliefs")      -- idem
#   ("Site",   "drawers")      -- "Site owns it; no write-matrix row"
# Adding them here would be an infidelity that HIDES a real gap: `04` §4 states that "any unmarked
# cell is a write-class violation", so a write to one of these must raise. It does — via the
# `key not in SOCIAL` branch above, which is the correct behaviour, not a tracer bug.


class World:
    """Primary state. `resolve` takes it; `choose` NEVER does (Law 2)."""

    def __init__(self, seed: int = 0):
        self.seed = seed
        self.tick = 0
        self.persons: dict[str, "Person"] = {}
        self.rungs: dict[str, "Rung"] = {}
        self.offices: dict[str, "Office"] = {}
        self.sites: dict[str, "Site"] = {}
        self.propositions: dict[str, "Proposition"] = {}
        self.tenures: dict[str, "Tenure"] = {}
        self.log: list["Event"] = []
        self.records: dict[str, "Record"] = {}
        self._step: Optional[Step] = None
        # the set of persons whose (Person, exists) the CURRENT actorless row changed.
        # `02` §5.1's causation rule reads this and nothing else.
        self._died_this_row: set[str] = set()

    # -- the write gate -----------------------------------------------------
    def write(self, record_kind: str, field_name: str, subject: str,
              value: Any, wclass: WriteClass, driver: str):
        """Every mutation goes through here. Two laws are enforced mechanically."""
        if self._step is None:
            raise Forbidden("a write outside the loop", f"{record_kind}.{field_name}")

        legal = LEGAL_WRITES[self._step]
        if wclass not in legal:
            raise Forbidden(
                f"write class {wclass.value} in step {self._step.value}",
                f"{record_kind}.{field_name}",
                needs=f"legal here: {sorted(c.value for c in legal) or 'NONE (DELIBERATE is a map)'}",
            )

        key = (record_kind, field_name)
        if key not in SOCIAL:
            # `04` §4: "any unmarked cell is a write-class violation."
            raise Unspecified(
                f"({record_kind}, {field_name}) has no row in the Partition schema",
                f"{record_kind}.{field_name}",
                needs="a social: bool column entry",
            )
        if SOCIAL[key] and driver == "Event":
            raise Forbidden(
                f"an Event writing social row ({record_kind}, {field_name})",
                f"{record_kind}.{field_name}",
                needs="an Act by a person",
            )

        # `02` §5.1's causation rule, which is what actually stops a storm vacating a
        # praefecture — NOT the column. "An actorless row's effects may write `until` ONLY on a
        # (Person, exists) change the same row also caused." Without this the seam is a hole:
        # social:false would let any Event end any tenure.
        if key == ("Tenure", "until") and driver == "Event" and subject not in self._died_this_row:
            raise Forbidden(
                "an actorless row writing `until` on a tenure whose holder it did not kill",
                "Tenure.until",
                needs="the same row must also have caused a (Person, exists) change on the "
                      "holder — a plague that kills the praefect ends his tenure; a storm may not",
            )

        TRACE.write(self._step, wclass, record_kind, field_name, subject, driver, value)
        return True

    def emit(self, ev: "Event"):
        self.log.append(ev)
        TRACE.event(ev)
        return ev


# ---------------------------------------------------------------------------
# §02 — THE CARRIERS, THE FIFTH KIND, THE ONE EDGE
# ---------------------------------------------------------------------------

RUNG_KINDS = ("person", "hearth", "community", "settlement",
              "territory", "province", "duchy", "realm")

# `02` §2.3: remit acts are a CLOSED FIVE. An office adds no verb.
REMIT_ACTS = ("issue", "determine", "confer_revoke", "dispatch", "convene")

# `02` §4.1: the seven Tenure kinds.
TENURE_KINDS = ("hold", "contain", "commit", "oblige", "succeed", "tie", "knot")


@dataclass
class Person:
    id: str
    weight: int = 1                      # a cohort IS a person at weight > 1
    marks: list[str] = field(default_factory=list)
    capability: dict[str, int] = field(default_factory=dict)
    stance: list[tuple[str, int, int]] = field(default_factory=list)   # (referent, valence, weight)
    convictions: dict[str, float] = field(default_factory=dict)
    beliefs: list[str] = field(default_factory=list)
    ledger: list["Claim"] = field(default_factory=list)
    name: str = ""

    # --- the mechanism `02` §5.5 NAMES and does not specify -----------------
    def scar(self, conviction: str, world: World):
        raise Unspecified(
            "Conviction motion: `02` §5.5 says convictions move 'slowly, by scar and crisis'",
            f"Person[{self.id}].convictions[{conviction}]",
            needs="a scar object, an owner, a write class, and a crisis rule",
        )

    def conviction_weighted_ranking(self, options: list["Act"]):
        raise Unspecified(
            "`02`:877 'Convictions weight the option ranking' — unformalized, in no signature in `08`",
            f"Person[{self.id}].choose",
            needs="a formula consuming Person.convictions",
        )


@dataclass
class Rung:
    id: str
    kind: str
    stake: list[str] = field(default_factory=list)
    judging_set_rule: Optional[str] = None
    dates: list["Date"] = field(default_factory=list)
    stores: dict[str, int] = field(default_factory=dict)
    sites: list[str] = field(default_factory=list)
    records: list[str] = field(default_factory=list)
    envelope: list[int] = field(default_factory=list)
    exists: bool = True

    def __post_init__(self):
        if self.kind not in RUNG_KINDS:
            raise Collision(f"Rung.kind {self.kind!r} not in the ruled eight", f"Rung[{self.id}]")


@dataclass
class Office:
    id: str
    post: str
    rung: Optional[str] = None           # `02` §2.3: optional; null is the office-cluster case
    remit_acts: tuple = REMIT_ACTS
    remit_scope: Optional[str] = None
    binds: str = "persons_by_presence"
    conferral: Optional[str] = None
    revocation: Optional[str] = None
    establishment: list[str] = field(default_factory=list)
    dates: list["Date"] = field(default_factory=list)
    upkeep: int = 0


@dataclass
class Site:
    id: str
    rung: str
    kind: str
    condition: int = 1000                # fixed point on COND_SCALE
    drawers: list[str] = field(default_factory=list)


@dataclass(frozen=True)
class Proposition:
    """`02` §3 — the fifth identity-bearing kind. IMMUTABLE, never destroyed.
    Mood OUGHT is an uttered Belief; a faction is this plus its commit edges."""
    id: str
    mood: str                            # HOLDS | OUGHT
    subject: str
    predicate: str
    value: Any
    when: tuple                          # MANDATORY interval — what makes collision free
    scope: str
    utterer: str = ""


@dataclass
class Tenure:
    id: str
    subject: str
    object: str
    kind: str
    since: int
    until: Optional[int] = None
    conferrer: Optional[str] = None
    degree: Optional[int] = None
    payload: Any = None

    def __post_init__(self):
        if self.kind not in TENURE_KINDS:
            raise Collision(f"Tenure.kind {self.kind!r} not in the seven", f"Tenure[{self.id}]")


@dataclass
class Claim:
    """`02` §5.3 — what a person holds TRUE. Moved by evidence, at WITNESS."""
    proposition: str
    source_event: str
    confidence: int
    holder: str


@dataclass
class Record:
    id: str
    rung: str
    kind: str
    ttl: Optional[int] = None


@dataclass
class Date:
    id: str
    holder: str
    season: int
    convening_conditions: list = field(default_factory=list)
    fired: bool = False


@dataclass
class Act:
    actor: str                           # a PERSON id — Law 1, mechanical
    verb: str
    target: Optional[str] = None
    payload: Any = None


@dataclass
class Event:
    id: str
    family: str
    scope: str
    causes: list[str] = field(default_factory=list)
    origin: str = "act"                  # act | exogenous
    subject: Optional[str] = None
    payload: Any = None


@dataclass
class View:
    """`01` Law 2 — a DISTINCT TYPE from World, BUILT not filtered.
    Absence produces absence, never a widened interval."""
    holder: str
    claims: list[Claim] = field(default_factory=list)

    def __getattr__(self, item):
        if item in ("persons", "rungs", "sites", "offices", "log", "tenures"):
            raise Forbidden(
                f"View.{item} — a View is not a World and holds no field of one",
                f"View[{self.holder}]",
                needs="assemble(person, question) over the ledger",
            )
        raise AttributeError(item)


@dataclass
class Sensation:
    """`07` §3.1 — the two scalars."""
    need: float = 0.0
    standing: float = 0.0


# ---------------------------------------------------------------------------
# §08 — THE THREE SIGNATURES. They work by what they OMIT.
# ---------------------------------------------------------------------------

def choose(person: Person, view: View, sensation: Sensation) -> Optional[Act]:
    """NO World, ever. A resolver-side Query called from here fails for want of an argument."""
    TRACE.call("choose", person.id, omitted="World")
    return None      # each case supplies its own decider


def resolve(acts: list[Act], world: World) -> list[Event]:
    """NO Person. The resolver cannot acquire a per-actor special case."""
    TRACE.call("resolve", f"{len(acts)} acts", omitted="Person")
    out = []
    for a in acts:
        ev = Event(id=f"E{world.tick}.{len(world.log)}", family=a.verb,
                   scope="place", subject=a.target, causes=[])
        world.emit(ev)
        out.append(ev)
    return out


def witness(person: Person, event: Event) -> list[Claim]:
    """Per person. A collection is NOT SPELLABLE — there is no (list[Person], Event) signature."""
    TRACE.call("witness", f"{person.id}<-{event.id}")
    return [Claim(proposition=f"{event.family}@{event.subject}",
                  source_event=event.id, confidence=3, holder=person.id)]


# ---------------------------------------------------------------------------
# QUERIES — never stored, always recomputed. `03`: Nobody owns an aggregate.
# ---------------------------------------------------------------------------

def leaders(world: World, prop_id: str, rung: str) -> list[str]:
    """`06` row 13: deposition IS this returning somebody else.
    `02` §10 item 2 carries the comparator as OPEN."""
    members = [t.subject for t in world.tenures.values()
               if t.kind == "commit" and t.object == prop_id and t.until is None]
    if not members:
        return []
    raise Unspecified(
        "`leaders()` comparator — `02` §10 item 2 proposes 'commitment degree x backing raisable', unadopted",
        f"leaders({prop_id},{rung})",
        needs="a comparator; and it must read `succeed` edges before it (see FINDINGS §2.8)",
    )


def condition_band(site: Site) -> str:
    """`05` §5.2 — a band edge changes an OPTION SET, never a roll term, never an outcome."""
    c = site.condition
    if c >= 750: return "sound"
    if c >= 500: return "worn"
    if c >= 250: return "failing"
    return "derelict"


def verbs(world: World, site: Site) -> set[str]:
    """World truth, as against opening_set's claim-derived account."""
    band = condition_band(site)
    return {"sound": {"ship", "levy", "mine"}, "worn": {"levy", "mine"},
            "failing": {"levy"}, "derelict": set()}[band]


def opening_set(person: Person, view: View):
    """`08` row 20 says Candidate[], NOT Act[]. `07` §3.2 still ships `-> Act[]`.
    The overturn is landed in `08`/`15` and NOT in `07`/`12`."""
    raise Collision(
        "opening_set return type: `08` row 20 + `15` row 13 say Candidate[]; `07` §3.2 ships Act[]",
        "opening_set",
        needs="the fold to reach `07` §3.2 and `12` T3",
    )


# ---------------------------------------------------------------------------
# THE LOOP
# ---------------------------------------------------------------------------

WEAR = {"harbour": 40, "mine": 30, "field": 20, "seam": 25, "hall": 15, "road": 20}


class SeasonLoop:
    """`04` — six steps, four barriers. Nested in SEASON_TICK -> ACTION -> ACCOUNTING_BOUNDARY."""

    def __init__(self, world: World):
        self.w = world

    def run(self, deciders: dict[str, Callable[[Person, View, Sensation], Optional[Act]]]):
        w = self.w
        w.tick += 1
        TRACE.season(w.tick)

        # ---- CALENDAR (barrier 1) -----------------------------------------
        w._step = Step.CALENDAR
        TRACE.step(Step.CALENDAR)
        for r in w.rungs.values():
            for d in r.dates:
                if d.season == w.tick:
                    d.fired = True
                    TRACE.note("date fires", f"{d.id}@{r.id}")

        # ---- MATTER (barrier 2; the world freezes at its end) --------------
        w._step = Step.MATTER
        TRACE.step(Step.MATTER)
        for s in w.sites.values():
            before = s.condition
            w.write("Site", "condition", s.id, before - WEAR.get(s.kind, 20),
                    WriteClass.MATTER, driver="Event")
            s.condition = max(0, before - WEAR.get(s.kind, 20))
            if condition_band(Site(s.id, s.rung, s.kind, before)) != condition_band(s):
                w.emit(Event(id=f"E{w.tick}.band.{s.id}", family="band_crossed",
                             scope="place", subject=s.id))

        # ---- DELIBERATE (a map, not a barrier: NO writes) -------------------
        w._step = Step.DELIBERATE
        TRACE.step(Step.DELIBERATE)
        acts: list[Act] = []
        for pid, p in w.persons.items():
            view = View(holder=pid, claims=[c for c in p.ledger])
            sens = Sensation(need=0.0, standing=0.0)
            d = deciders.get(pid)
            if d is None:
                continue
            TRACE.call("choose", pid, omitted="World")
            a = d(p, view, sens)
            if a is not None:
                if a.actor != pid:
                    raise Forbidden("an Act whose actor is not the chooser", f"Act[{a.verb}]")
                acts.append(a)
                TRACE.act(a)

        # ---- RESOLVE (barrier 3) -------------------------------------------
        w._step = Step.RESOLVE
        TRACE.step(Step.RESOLVE)
        events = resolve(acts, w)

        # ---- WITNESS (barrier 4, the join) ---------------------------------
        w._step = Step.WITNESS
        TRACE.step(Step.WITNESS)
        for ev in events:
            for pid, p in w.persons.items():
                for c in witness(p, ev):
                    w.write("Person", "ledger", pid, c.proposition,
                            WriteClass.INTERIOR, driver="Event")
                    p.ledger.append(c)

        # ---- CENSUS (shares WITNESS's join) --------------------------------
        w._step = Step.CENSUS
        TRACE.step(Step.CENSUS)
        w._step = None
        return events
