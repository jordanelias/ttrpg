"""`season.state.carriers` -- THE PRIMITIVES. The sixteen things the model is made of.

Extracted from `shape.py` at step 4 of the decomposition (ED-IN-0203), a PURE MOVE: `Tenure`,
`StateChange`, `Event`, `Claim`, `Sensation`, `View`, `Question`, `Candidate`, `Scene`, `Act`,
`Person`, `Site`, `Record`, `Proposition`, `Office`, `Rung` -- and `matrix_rows_without_a_field`,
which is not a carrier and is here for a reason given below. `shape.py` re-exports every name, so
`from ..shape import Person` and `S.Person` keep resolving exactly as before.

⚠ WHY `matrix_rows_without_a_field` IS IN THIS MODULE AND NOT IN `data/`. It answers *does this
matrix row's `fieldname` name a real field of its `record_kind`* by looking the KIND UP AS A NAME
(`globals().get(kind)`) and reading the class's declared fields. That lookup resolves in the
module it is written in, so it has to be written where the classes are -- and `season.data` cannot
import this module, because the carriers read `data.rosters` and `data.fixtures` and the arrow
would reverse. Put it in `data/matrix.py` and it silently reports every kind `unmodelled`: no
exception, no red test, just a clean bill over a check that stopped looking. Recorded because that
is the same shape as the two instrument failures step 0b hit -- a reflective lookup and a glob both
answer about the FILE THEY RUN IN, and moving the file moves the answer without moving the code.

⚠ THIS MODULE IMPORTS NOTHING FROM `world` OR ABOVE, AND THE DIRECTION IS THE POINT. A carrier is
a thing the world holds; it may not know about the store that holds it. `state/world.py` imports
these nine classes and this module imports nothing back, so the two files together carry no cycle
-- which is checkable in one grep (`grep -n 'import' state/carriers.py`) rather than asserted here.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any, Optional

from ..data.fixtures import DEFAULT_FIXTURES
from ..data.matrix import MATRIX
from ..data.rosters import (
    BODY_FUNCTION, QUESTION_SOURCES, REMIT_ACTS, RUNG_KINDS, office_faction, title_domain,
)
from ..gaps import Forbidden, Unowned, Unspecified


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
    # ⚠ THIS DEFAULT IS ALSO THE SENTINEL, AND THE TWO JOBS CONTRADICT EACH OTHER. `stratum_of`
    # decides "did the caller declare a stratum?" by comparing against THIS VALUE
    # (`a.stratum != Act.__dataclass_fields__["stratum"].default`), so an act that deliberately
    # declares `stratum=4` is indistinguishable from one that declared nothing and is routed to
    # the verb table instead -- against `stratum_of`'s own promise that "a caller that sets it
    # explicitly is taken at its word". MEASURED: 19 of the 32 verb-table rows carry a stratum
    # other than `social`, so a declared 4 would be silently overridden on 19 of 32 verbs.
    # LATENT, NOT LIVE, and only by coincidence: the sole explicit call site is
    # `probes.py:2339`, verb `speak`, whose row is `social` -- so the override lands on the same
    # value and the A37 arm cannot tell "set" from "unset". Found by the step-4 adversarial pass.
    # NOT fixed here: step 4 is a pure move, and the fix changes `Act`'s schema.
    # [JUSTIFIED: an INDEX into the `strata` roster (#353 §27), inherited -- `social` is index 4 and `stratum_of` returns `STRATA.index(row.stratum)`. NOT `[canonical:]`: this 4 is also the "caller declared nothing" sentinel `stratum_of` tests against, so it is a fitted default doing two jobs, not a ratified value -- see the ⚠ below]
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
