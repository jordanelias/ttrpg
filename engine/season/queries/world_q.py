"""`season.queries.world_q` — THE WORLD-FIRST HALF OF `Query`, AND THE TWO WORLD-FIRST
FUNCTIONS THAT WERE NEVER IN IT.

EXTRACTED, step 5 of the decomposition. `04_CODE_ARCHITECTURE.md` §A.3 row 2 is the ruling and it
is a MODULE ruling, not a signature one: *"one `Query` class holding both families -> two modules;
the second cannot import the first ... In one class, a person-side function calls a resolver-side
one with no import to scan."* The eleven functions here all take a `World` FIRST. The four
person-side statics stay on `Query` in `shape.py` until step 7 puts them in `decision`, which is
the module that may not name `World` at all.

⚠ THE ELEVEN ARE MODULE FUNCTIONS NOW, AND `shape.Query` BINDS THEM AS `staticmethod`s. That is a
re-export, not a copy — `Query.parent_of is parent_of` — so every call site reading
`Query.<world-first>` resolves to these bodies and there is exactly one owner of each rule. The
binding is what makes the class deletable at step 7 without a second migration.

⚠ THIS MODULE MUST NOT LEARN A PERSON. Its one-way rule is the same one `state/` states: nothing
here imports `shape`, `decision`, `loop` or `seam`. `questions_for` takes a `Person` as its SECOND
argument and asks the WORLD about them; that is a world-first function, not a person-side one, and
the AST guard (`test_w5_sense_is_still_the_only_world_taking_non_decision_function`) is what keeps
the distinction checkable by signature rather than by intention.

⚠ THAT SENTENCE WAS FALSE WHEN FIRST WRITTEN AND IS MADE TRUE RATHER THAN SOFTENED. The guard
parsed `files.SHAPE_PY` alone, so it could not see this module at all — a claim of enforcement
naming a gate that does not read the file it is written in, which is the §47 defect the package
records twice already. Caught by a read-only critic; the guard now parses the model set, and
`_model_modules()` derives that set from a recursive glob, so it will read the module a later
step adds without anyone remembering to say so.
"""

from __future__ import annotations

from typing import Callable, Optional

from ..data.requires import UNKNOWN
from ..data.rosters import (
    FACTION_BY_PROP, QUESTION_SOURCES, RECORD_CONTENT, RECORD_KINDS, RUNG_KINDS, TENURE_KINDS,
)
from ..gaps import Forbidden, Unspecified
from ..state.carriers import Person, Question, Site, Tenure
# ⚠ `parent_of` AND `descendants` ARE RE-EXPORTED, NOT DEFINED HERE (G3, plan position 6). The
# write gate's F3 clause needs both -- ruling (3)'s parent rung and ruling (4)'s purview subtree --
# and the gate is in `state/`, which may not import this module. The bodies moved down unchanged;
# these names are the same function objects, so every `world_q.parent_of(...)` call is unaffected.
from ..state.containment import descendants, parent_of  # noqa: F401 -- re-exported
from ..state.ids import ROOT
from ..state.world import World
from ..trace_log import TRACE


# ===========================================================================
# S17 -- QUERY. THE SIDE COLUMN IS THE ENFORCEMENT.
# ===========================================================================

# ---- resolver-side: World FIRST, always -----------------------------
# `parent_of(w, rung_id)` and `descendants(w, rung_id)` -- see the import above and
# `state/containment.py`.

def r1_aggregate(w: World, rung_id: str, over: Callable[[str], int]) -> int:
    """R-1: COMPUTE ON DEMAND over DESCENDANTS. Never received, never stored. S22.4 cl.3:
    LIVE EDGES ONLY. S6.2: this is a claim about the CONTAINMENT TREE."""
    TRACE.query("r1_aggregate", "resolver")
    return sum(over(d) for d in descendants(w, rung_id))

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

def commit_count_guard(w: World, edges: list[Tenure], name: str) -> int:
    """The DETECTING half of clause 3: it looks at the rows, not at a flag."""
    ended = [t for t in edges if not t.live]
    if ended:
        raise Forbidden(
            f"aggregate '{name}' composed over {len(ended)} ENDED edge(s)", "S22.4",
            needs="filter to until == null before summing",
            law="L3 clause 3 -- ended Tenures PERSIST as historical claim subjects (S15.2), so a count over live AND ended rows is monotone non-decreasing. That is a ratchet built entirely out of 'structural' edges")
    return len(edges)

def lateral(w: World, name: str, kind: str) -> list[Tenure]:
    """S6.2/S38 -- THE LATERAL GRAPH. Not governed by R-1/R-2. Resolver-side, World first,
    therefore unreachable from choose() BY CONSTRUCTION."""
    TRACE.query(f"lateral:{name}", "resolver")
    return [t for t in w.tenures if t.kind == kind and t.live]

def verbs(w: World, site: Site, floors: dict[str, int]) -> set[str]:
    """S12.1 -- condition GATES VERBS. The comparison is on a SUMMED FIXED-POINT INT."""
    TRACE.query("verbs", "resolver")
    return {v for v, floor in floors.items() if site.condition >= floor}

def hold_force(w: World, obj: str) -> Optional[Tenure]:
    """S15 -- `hold` is 1 PER OBJECT. S54 item 20's lawful form rests on this cardinality."""
    live = [t for t in w.tenures if t.kind == "hold" and t.object == obj and t.live]
    if len(live) > 1:
        raise Forbidden(f"{len(live)} live `hold` Tenures on {obj}", "S15",
                        law="S15 -- `hold` cardinality is 1 PER OBJECT")
    return live[0] if live else None

def judging_set(w: World, venue: str, matter: Optional[str] = None) -> list[str]:
    """`H-32`, BUILT -- plan position `18` (PROC-A), `21_RECONCILIATION.md` PHASE 2 step 7 /
    `03_PARAMETERS.md` §D's `bench_basis`. Live holders of a `hold` Tenure GRANTED the bench's
    basis AND whose Office's `scope_rung` CONTAINS `venue` -- the containment walk
    `ancestry(w, venue)` already owns (§8: the walk is a rule, lives once), not a bare equality,
    which is the "a purview walk one rung up still finds it" falsifier: a seat scoped one rung
    above `venue` still governs it. EMPTY SET -> the date fires and lapses; no forced decision
    (S61 -- *"nothing is decided at a sitting"* by fiat of this Query, only by who is actually
    seated).

    ⚠ THE GRANT, NOT THE OFFICE'S OWN FIELD -- plan position `13e`'s consolidation
    (`Tenure.granted_acts`, `H-71` arm 2). *"An office whose remit changes does so by an ACT ...
    a hand-mutation reaches nobody."* Reading `off.remit_acts` here would be a SIXTH reader of the
    field `13e` moved every consumer off of, and would let a bare attribute edit change who may
    judge without a `confer`/`establish` ever running -- exactly the drift that consolidation
    exists to stop. `test_13e_no_remit_acts_attribute_read_outside_the_three_allow_listed_sites`
    is the AST guard that catches a new reader of the retired field; this one reads the Tenure's
    own snapshot instead, the same as `person_side_eligible`.

    ⚠ `matter` IS ACCEPTED, NOT YET LOAD-BEARING. The design's signature is
    `judging_set(w, venue, matter)` because a per-arrangement `bench_basis` (`engine/season/arrangements.yaml`,
    part 3 of this same position) is meant to select the remit act a matter's disposal reads --
    but nothing yet maps a docketed matter to its governing arrangement row (that is PHASE 2 step
    10's docketing, explicitly weighed and left OPEN by this position's own record rather than
    built here). Until that mapping exists, `matter` is carried on the signature the design
    specifies and the basis is `H-32`'s own swept default, `"determine"` -- the one remit act any
    live matter in the corpus currently asks a bench to exercise. Wiring `matter` through is one
    line here (`basis = bench_basis_of(w, matter) or "determine"`) once that mapping exists, and
    is deliberately NOT invented now (§0.05: a mapping this position does not own is not smuggled
    in to make the signature look busier).

    ⚠ A SEAT WITH NO `scope_rung` REACHES NOTHING -- the office-cluster case (S6.2, `Office.rung
    is None`) has no ground to be contained on, exactly as `purview_reaches` treats it. It is a
    CONTENT fact about such a seat, not a bug here.

    ⚠ CORRECTED (methodology close, terminal critique, 2026-09-29): THE PARAGRAPH ABOVE OVERSTATES
    THE EQUIVALENCE. `off.scope_rung is None` does NOT only happen in the office-cluster case
    (`off.rung is None`) -- `carriers.py::Office.__post_init__` auto-sets `scope_rung` ONLY for a
    TITLED post (`title_domain(self.post)` non-`None`); a seated, RANKED, non-titled office
    (`off.rung` set, no title) gets no `scope_rung` unless one is authored for it by hand in
    `offices.yaml`, and this function excludes such a seat from EVERY bench, silently, the same way
    it excludes a true cluster seat -- a different content fact than the one this docstring claimed,
    not the same one restated. `state/gate.py::purview_reaches` asks the same containment question of
    `off.rung` (always set for a seated office) and would not exclude it. This function reads
    `scope_rung` rather than `rung`/`purview_reaches` by `H-32`'s own ruled default
    (`hole_register.yaml`, H-32), which is precedent this correction does not reopen -- it corrects
    only the FALSE claim that the two fields' `None` cases coincide, not the choice of field."""
    TRACE.query("judging_set", "resolver")
    basis = "determine"
    reach = set(ancestry(w, venue))
    seats: list[str] = []
    for t in w.tenures:
        if t.kind != "hold" or not t.live or basis not in t.granted_acts:
            continue
        off = w.offices.get(t.object)
        if off is None or off.scope_rung is None or off.scope_rung not in reach:
            continue
        seats.append(t.subject)
    return seats

def home_of(w: World) -> dict:
    """`{person id: containing rung id}` for every person with a live `contain` edge.

    ⚠ **THE INVERSE OF `presence`, AND IT EXISTS BECAUSE FOUR SITES HAD ROLLED IT BY HAND.**
    `presence(w, rung)` answers *who is here*; this answers *where is everyone*, which is the
    question `harness/populated.py` (twice — the `by_home`/`home_of` index and `census`),
    `tools/export_npc_roster.py` and `engine/season/tests/test_season_shape.py` were each
    computing with their own copy of `t.kind == "contain" and t.live and t.subject in w.persons`.
    That is load-bearing rather than cosmetic: `export_npc_roster.py --check` detects drift by
    comparing ITS notion of home against the builder's, so the two agreeing by coincidence is the
    whole point of the check, and `census`'s `largest_building` is asserted in the suite. A change
    to what counts as home — a dead tenure, a person with two contain edges — had to land in four
    places with nothing to catch a miss (§8, and the §0.1 pt 5 pattern-defect signature).

    ⚠ LAST WRITE WINS on a person with more than one live `contain`, which `World.add_tenure`
    does not forbid. That is the incumbent behaviour of every site this replaces, preserved
    deliberately rather than quietly tightened here."""
    TRACE.query("home_of", "resolver")
    return {t.subject: t.object for t in w.tenures
            if t.kind == "contain" and t.live and t.subject in w.persons}


def place_of(w: World, x: Optional[str]) -> Optional[str]:
    """`ARCH §F.14`'s OWN NAME, PROMOTED (position `11a`, r2 `01_ATTENTION_AND_REACH.md` §A.3).
    The rung a THING is at, for ANY id -- moved in from `epistemic._event_place`, which took only
    an Event. That caller becomes `place_of(w, anchor_of(w, e))` (`epistemic.py`'s two sites).

    ⚠ PERSON BEFORE RUNG, AND THE ORDER IS THE WHOLE OF THIS FUNCTION'S CORRECTNESS -- carried
    over from `_event_place`'s own docstring rather than restated: testing `x in w.rungs` FIRST
    would answer a person's own same-id `person`-kind Rung, and `Query.presence` on THAT answers
    "who is contained in themselves" -- nobody. A channel BROKEN CLOSED, not merely narrow, and
    `P15`'s history is the worked case (`epistemic.py`, `_ch_co_located`'s docstring). THIS IS A
    REPEAT of a conflation `witness` had already retracted once; the order is what prevents it a
    third time.

    Two limbs promoted `_event_place` did not have, plus the NO SILENT DEFAULT floor (`ID-5`):
      * person  -> `home_of(w)[x]` -- the single owner, not a hand-rolled `contain` scan.
      * site    -> `Site.rung`, the maintained side (S12).
      * record  -> its live holder's place (`hold_force` -- S15's cardinality-1 guard makes this
                   total), else the record's own `Record.rung` (non-optional).
      * date    -> `venue` -- `_eff_convene` always sets one, and `_req_convene` requires
                   `venue in w.rungs`, so this limb is total for every date the engine can mint.
      * rung    -> itself.
      * anything else, including `None` -> `None`. Absence maps to the refusal, never to a
                   plausible guess.

    ⚠ MAY NOT READ A LEDGER (`AX-2`) and MAY NOT BE CALLED FROM `decision/` -- world-first,
    `queries/world_q` only (`ARCH §A.2`: reads *any store, via `World`*). It answers ONE place; a
    multi-rung actorless Event (a plague spanning many rungs) is a named LIMIT this does not
    solve (`01` §A.3.1) -- `_ch_co_located`'s membership test stays exactly that, not an
    intersection, and widening the signature is `ARCH §F.14`'s own ruling text to amend, not an
    edit to make here."""
    if x in w.persons:
        return home_of(w).get(x)
    if x in w.sites:
        return getattr(w.sites[x], "rung", None)
    if x in w.records:
        h = hold_force(w, x)
        return place_of(w, h.subject) if h is not None else w.records[x].rung
    if x in w.dates:
        return w.dates[x].get("venue")
    if x in w.rungs:
        return x
    return None


def reach(w: World, p: Person) -> set[str]:
    """`01_ATTENTION_AND_REACH.md` §A.4 -- the ids a question may be ABOUT for this person. A
    FILTER over what a WITNESS channel already deposited, and never a fan (§A.4.4, LB-2b): it is
    not called from `witness`, `observers_for` is untouched, and `questions_for`'s Q2 still reads
    only `p.ledger` -- so a claim not already in this person's own ledger cannot become a question
    no matter how wide `reach` is. World-first, owns nothing, stored nowhere, recomputable at any
    barrier (`ARCH §A.2`).

    FOUR LIMBS, none of them a new rule -- each composes on an existing owner (§A.4.2):
      1. me                  -- `{p.id}`, today's first Q2 disjunct.
      2. mine                -- every live Tenure's object -- `questions_for`'s own `mine`, read
                                 the same way.
      3. the ladder above me -- `ancestors-or-self` of `home_of(w)[p.id]`, via `parent_of` -- the
                                 identical walk `predicates.under_purview` and `conferral_path`
                                 already make (a fourth hand copy is what `CLAUDE.md` §8 forbids).
      4. purview             -- `{seat.rung} | descendants(seat.rung)` over every live `hold` on
                                 an Office with a rung. `descendants` EXCLUDES its own rung
                                 (`state/containment.py`), so the seat's own rung must be unioned
                                 in explicitly, or a Duke seated at his own duchy would never be
                                 reached by a claim about the duchy itself -- LB-2e, the
                                 inclusive-walk falsifier.

    ⚠ MAY NOT READ A LEDGER, NOT EVEN `p`'S OWN (`AX-2`): a reach computed from beliefs would make
    "what I may be asked about" a function of what I believe, and a false belief would silently
    widen the world I can act on (`01` §A.4.3). MAY NOT read another person's tenures -- it answers
    for `p` alone."""
    TRACE.query("reach", "resolver")
    R = {p.id}
    R |= {t.object for t in p.tenures if t.live}
    cur, seen = home_of(w).get(p.id), set()
    while cur is not None and cur not in seen:
        R.add(cur); seen.add(cur); cur = parent_of(w, cur)
    for t in p.tenures:
        if t.kind == "hold" and t.live and t.object in w.offices:
            rg = w.offices[t.object].rung
            if rg is not None:
                R.add(rg); R.update(descendants(w, rg))
    return R


def named(c) -> tuple:
    """CLAUSE 3's `named(c)` -- position `15c`, r2 `01_ATTENTION_AND_REACH.md` §A.5.3/§A.5.4 and
    `02_THE_WRIT_AND_THE_WORD.md` §A.9.1. The id set inside a `content:<kind>` claim's value, so
    that a writ can name someone into a question WITHOUT a place query -- `holonic §37.3`'s
    *"scope enumerates EXECUTORS, not places."*

    ⚠ **RULED: read from `record_kinds`, never from the value's strings.** `RECORD_CONTENT`'s
    `addressee` key (`rosters.yaml: record_kinds.content`) names the ONE key, shared by every
    kind that has one, under which an addressee id list sits -- `to`, for `dispensation` and
    `petition` alike. A generic *"every id anywhere in the value"* would make a `works` plan's
    site ids into addressees and a petition's `from` into a summons; this reads the roster that
    types the schema, which is one owner for both facts. A kind with no such key (`works`,
    `text`) simply has no `to` entry, so this returns `()` for it without a second branch.

    `()` -- never `None`, so a bare caller need not guard -- for a claim whose `predicate` does
    not start `content:`, or whose `value` names nobody. Takes a `Claim`, not a `World`: it reads
    one object already in hand, the same shape as `place_of(w, c.subject)` beside it in `Q2`, and
    is not a second read of `p.ledger` (`AX-2` stays satisfied by the caller's own loop)."""
    stem, sep, _ = str(c.predicate).partition(":")
    if not sep or stem != RECORD_CONTENT.get("predicate") or c.value is None:
        return ()
    ids = dict(c.value).get(RECORD_CONTENT.get("addressee"))
    return tuple(ids) if ids else ()


def nearest_store(w: World, rung_id: Optional[str], kind: str,
                  available: Optional[dict] = None) -> Optional[str]:
    """THE LARDER LADDER: the nearest rung AT OR ABOVE `rung_id` holding any `kind`, or `None`.

    ⚠⚠ IT EXISTS BECAUSE THE SUBSISTENCE ECONOMY IS TWO HALVES THAT NEVER MEET. MEASURED on
    `build_realm(0)` after one season, before this Query: **4,810 units, every one of them at the
    37 SETTLEMENT rungs and none at the 211 hearths**, while all 46 persons live in **26 hearths**
    — so `matter`'s per-rung draw counted **zero eaters at every rung that had stores** and the
    whole subsistence step was INERT on a world that runs. The walk is the join, and it moves no
    matter and creates no store: a person reaches UP the ladder they already live on.

    ⚠ IT RETURNS THE RUNG ITSELF WHERE THE RUNG HAS STOCK, which is what makes this a
    GENERALISATION rather than a replacement. A hearth with its own larder feeds its own people
    exactly as before; the walk is a no-op wherever the old per-rung code was already right. That
    is the control `LB-3a` pairs with, and if it ever moves, the walk is not a generalisation.

    ⚠ `None` AT THE ROOT IS A SHORTFALL, NEVER AN ERROR. A person under a realm that holds nothing
    goes hungry, and hunger is a fact about the world; raising here would make an empty larder an
    instrument defect. What the caller does with it is the caller's — today MATTER records it and
    acts on nothing (L5: a threshold crossing MAY NEVER PRODUCE AN OUTCOME).

    ⚠ `available` IS THE CALLER'S RUNNING VIEW DURING ONE DRAW, and it is the reason two eaters
    cannot spend the same unit. `{(rung_id, kind): units_left}`; absent, the world's own stores
    answer. Without it a caller that defers its writes — as MATTER must, because the gate applies
    the write — would show every eater the FULL larder and scarcity would never bind, which is the
    exact defect `loop/effects.py`'s own header names for `transfer` (*"`transfer` twice from a
    one-unit larder succeeds twice: the scarcity §27.1 rests on never happens"*).

    ⚠ ITERATIVE WITH A VISITED SET, on `descendants`'s precedent (S38.1). `contain_ascends` makes
    the ladder strictly ascending at `add_tenure`, so a cycle should be unreachable — but a walk
    that hangs on a malformed fixture is a worse failure than one that stops, and the guard costs
    one set."""
    TRACE.query("nearest_store", "resolver")
    seen: set = set()
    cur = rung_id
    while cur is not None and cur in w.rungs and cur not in seen:
        seen.add(cur)
        if available is not None:
            held = available.get((cur, kind))
            if held is None:
                held = (w.rungs[cur].stores or {}).get(kind, 0)
        else:
            held = (w.rungs[cur].stores or {}).get(kind, 0)
        if held > 0:
            return cur
        cur = parent_of(w, cur)
    return None


def presence(w: World, rung_id: str) -> list[str]:
    """S28 -- the PRESENCE INDEX the global fan-out reads."""
    TRACE.query("presence", "resolver")
    return [t.subject for t in w.tenures
            if t.kind == "contain" and t.object == rung_id and t.live
            and t.subject in w.persons]


# ===========================================================================
# §14.2 -- THE POLITY QUERIES. "A faction IS a Proposition plus its `commit` edges."
#
# §22's `Nobody` row assigns FACTION, LEADERS, PRESENCE, DENSITY and FOOTPRINT to nobody, as
# Queries stored nowhere, and §17 names each in the resolver-side list. Four of the five had no
# body. They are written here rather than in a new module because `04 §A.2` types `queries/` as
# `world_q · person_q · cache` -- a `polity_q.py` for THESE functions would be a fourth member and
# a conformance defect, and these are world-first reads like every other function in this file.
#
# ⚠ `faction_q.py` IS NOT A COUNTEREXAMPLE TO THIS RULE; IT IS A DIFFERENT CASE, DISTINGUISHED AT
# ITS OWN SITE. This paragraph's "no fourth module" holds for functions §A.2 does not name outside
# this file -- exactly the case for `members`/`leaders`/`footprint` below, and for `WorldReader`
# before unit L3 folded it in. `faction_q.resolve` is named by its OWN dotted path in §B.6.1 and
# §C.5.1, both ratified, neither touched by this docstring's reasoning; see `faction_q.py`'s and
# `queries/__init__.py`'s own docstrings for why that is a genuinely different ambiguity, named
# rather than resolved the same way.
#
# ⚠ THE SEMANTICS ARE NOT TRANSCRIBED, BECAUSE §17 GIVES ONLY `name(w, ...)`. What IS transcribed
# is the definition each rests on -- §14.2 for membership, §15's cardinality table for the edge
# kinds, §22.4's three L3 clauses for what an aggregate may compose over. Where the argument list
# or the denominator is this module's choice, the docstring says so in those words.
#
# ⚠ EVERY ONE READS LIVE EDGES ONLY. §22.4 clause 3 REFUSES any aggregate monotone in the ENDED
# edge set -- `count{commit}` over live AND ended rows is "members ever", which is a ratchet built
# out of structural edges. `t.live` is not a filter for tidiness; dropping it changes the kind of
# thing the function is.
# ===========================================================================

def members(w: World, faction: str) -> list[str]:
    """Everyone with a LIVE `commit` to this Proposition. §14.2: *"Membership is `commit`."*

    ⚠ THIS IS THE WHOLE OF MEMBERSHIP AND THERE IS NO SECOND ROUTE. Before this, the only way a
    person belonged to a faction was to hold an Office whose `body` resolved to one -- so a
    faction had no laity, no rank-and-file and no congregation, and `role_templates` keyed on
    faction described a population that could not exist. `commit` was already the ruled edge and
    was carrying only a person's private want."""
    TRACE.query("members", "resolver")
    return sorted(t.subject for t in w.tenures
                  if t.kind == "commit" and t.object == faction and t.live
                  and t.subject in w.persons)


def leaders(w: World, faction: str) -> list[str]:
    """The members who hold an Office belonging to this faction. §17 · §22's `Nobody` row.

    ⚠ IT IS THE INTERSECTION AND NOT EITHER HALF, which is the claim worth stating: an
    office-holder who has not committed is staff, not a leader, and a committed member holding no
    office is a member. Both readings were available and this one is what §14.2 leaves room for --
    the faction is the Proposition plus its commits, so leadership has to be read THROUGH
    membership rather than beside it.

    ⚠ `Office.faction` IS DERIVED AT CONSTRUCTION from `body` (`Office.__post_init__`), so this
    never re-derives it and cannot disagree with the constructor.

    ⚠⚠ TWO IDENTIFIERS NAME ONE FACTION, AND THIS FUNCTION HAS NOW RETURNED `[]` FOR A WORLD WITH
    LEADERS IN IT TWICE, FOR TWO DIFFERENT REASONS. `members` keys on the PROPOSITION ID
    (`fac_hafenmark`) because that is what a `commit` edge points at; `Office.faction` carries the
    FACTION NAME (`Hafenmark`) because that is what `rosters.yaml: factions` holds and what
    `office_faction` validates against. So a translation is needed, and WHERE IT READS THE NAME
    FROM is the whole question.

    The first writing compared the two identifiers directly. The second read `Proposition.subject`,
    which was the faction's name -- until the creed commit made `subject` the LEADER'S PERSON ID
    for every faction that has a creed and moved the name to `value`, leaving this reader pointed
    at a field whose meaning had changed underneath it. MEASURED at `build_realm(0)`: `[]` for
    Crown, Church of Solmund, Hafenmark and Varfell -- all four factions that hold seats -- hiding
    19 of 19 occupied offices.

    It now reads `FACTION_BY_PROP`, which `data/rosters.py` DERIVES from the roster, so there is no
    field to guess and no mood to dispatch on. ⚠ BOTH FAILURES WERE INVISIBLE FOR ONE REASON: `[]`
    is a plausible answer for a faction with no office-holders -- four of the eight genuinely have
    none -- so nothing raised, and a test asserting `leaders <= members` is satisfied by the empty
    set. `test_leaders_are_found_for_every_faction_that_holds_a_seat` asserts the non-empty case."""
    TRACE.query("leaders", "resolver")
    name = FACTION_BY_PROP.get(faction, faction)
    held = {t.object: t.subject for t in w.tenures if t.kind == "hold" and t.live}
    inside = set(members(w, faction))
    return sorted(who for oid, who in held.items()
                  if who in inside
                  and oid in w.offices and w.offices[oid].faction == name)


def footprint(w: World, faction: str) -> list[str]:
    """Every rung the faction REACHES: the rungs it holds, plus the rungs its members sit in.

    ⚠ THE UNION IS THIS MODULE'S CHOICE AND THE TWO HALVES ARE DIFFERENT CLAIMS. Holding is
    title; presence is reach. A faction with members in a city it does not hold has a footprint
    there and no claim to it, which is the distinction the strategic layer turns on, so collapsing
    to either half alone would answer a different question. §14.2 names `footprint` beside
    `presence` and `density` without defining any of the three.

    ⚠ A FACTION HOLDS A RUNG AS THE `hold` SUBJECT, WHICH §15's TABLE TYPES AS `Person -> ...`.
    §14.2's own closing note is the licence and the warning: *"A Proposition may be a `hold`
    subject and is never destroyed, so a memberless faction leaves territory held by a banner
    nobody carries."* That defect is declared there and is not repaired here."""
    TRACE.query("footprint", "resolver")
    out = {t.object for t in w.tenures
           if t.kind == "hold" and t.subject == faction and t.live and t.object in w.rungs}
    inside = set(members(w, faction))
    out |= {t.object for t in w.tenures
            if t.kind == "contain" and t.live and t.subject in inside and t.object in w.rungs}
    return sorted(out)


def _subtree(w: World, rung_id: str) -> set:
    """`rung_id` plus everything under it, by containment (`descendants`). Extracted (M4 review
    pass, `/simplify` reuse finding): `density`, `mustered` and `fortification_of` each wrote
    `{rung_id, *descendants(w, rung_id)}` independently -- `mustered`'s own docstring already
    named the duplication ("density's own composition, one line above") rather than ending it."""
    return {rung_id, *descendants(w, rung_id)}


def density(w: World, rung_id: str, faction: str) -> tuple[int, int]:
    """`(members of this faction present, persons present)` over the containment subtree.

    An R-1 aggregate: computed on demand over descendants, never received and never stored
    (§22.4 clause 1's licensed shape). It counts PEOPLE, never anything a person holds inside
    them -- clause 2 bars a Query that sums a per-person tally across holders, and a headcount is
    not one.

    ⚠ THE DENOMINATOR IS PERSONS PRESENT, NOT THE FACTION'S TOTAL MEMBERSHIP, so this reads as
    *"how much of this place is theirs"* rather than *"how much of them is in this place"*. The
    other denominator is the other question; both are one line, and the caller should say which
    it means rather than this returning a bare ratio."""
    TRACE.query("density", "resolver")
    here = _subtree(w, rung_id)
    inside = set(members(w, faction))
    present = [t.subject for t in w.tenures
               if t.kind == "contain" and t.live
               and t.object in here and t.subject in w.persons]
    return sum(1 for p in present if p in inside), len(present)


def mustered(w: World, rung_id: str, faction: str) -> list[str]:
    """M4 (`ED-IN-0279` clause (a)). This faction's members present in `rung_id`'s subtree --
    settlement plus everything under it, Jordan's ruling on what "present at the target" means
    for a march (planning round 2). `density`'s own composition, one line above, minus the count:
    person containment never terminates AT a settlement rung -- every person's `contain` targets a
    `home` building beneath one (`harness/populated.py`) -- so a literal exact-rung read finds
    nobody home, ever, and the subtree is the only reading that finds anyone at all.

    Who a march may draw on at its origin, and who a field battle's defending side draws from at
    its target -- both the same query, the faction and the rung simply swapped. `04 §C.5.1`'s own
    pseudocode: *"squad combat: the squad is `members ∩ present-at-rung`"*."""
    TRACE.query("mustered", "resolver")
    here = _subtree(w, rung_id)
    inside = set(members(w, faction))
    return sorted(t.subject for t in w.tenures
                  if t.kind == "contain" and t.live
                  and t.object in here and t.subject in inside)


def fortification_of(w: World, rung_id: str) -> float:
    """M4 (`ED-IN-0279` clause (a)). A settlement's defensive strength, `0.0` to `1.0`, read off
    the `garrison` Site(s) in `rung_id`'s subtree -- `H-38`'s *"`Site.condition` is the model"*
    applied to fortification, Jordan's choice over a cohort-Person alternative (planning round 2).
    `0.0` with no garrison in the subtree: an unfortified settlement, not a refusal -- absence of
    a garrison Site is a legitimate world state (`harness/populated.py`'s M4 build step 11 seeds
    one per settlement, but nothing enforces that it must).

    ⚠ MULTIPLE GARRISONS AVERAGE RATHER THAN SUM: one per settlement is what step 11 ships, and an
    average keeps the return in `[0.0, 1.0]` regardless, which summing would not.

    ⚠⚠ **NOTHING CALLS THIS FUNCTION.** `seam/wrappers/mass_battle.py::resolve()` passes
    `terrain=None` unconditionally and has no other parameter to carry a fortification bonus
    through -- `systems/mass_battle/sim/massbattle.py::resolve_field`'s only knobs are `terrain`
    and `rng`. Seeding a garrison Site (step 11) changes no fight's outcome until something reads
    this return AND the provider is given somewhere to put it. `H-150` (`hole_register.yaml`) is
    this gap's row: HOW MUCH a fortification level should shift a field battle is an invented
    magnitude no ruling states, on `H-148`'s own shape."""
    TRACE.query("fortification_of", "resolver")
    here = _subtree(w, rung_id)
    garrisons = [s for s in w.sites.values() if s.kind == "garrison" and s.rung in here]
    if not garrisons:
        return 0.0
    scale = w.fixtures.get("condition_scale")
    return sum(s.condition for s in garrisons) / (scale * len(garrisons))


def sovereign_fraction(w: World, rung_id: str) -> tuple[float, int]:
    """§17's one Query with a DECLARED return type: `-> (fraction, undetermined_count)`.

    Over the rungs of the subtree: the share held by the single largest holder, and how many are
    held by nobody. The signature is the architecture's; the denominator -- DETERMINED rungs only,
    so an unheld rung lowers nothing and is reported separately -- is this module's reading of why
    §17 bothered to return the second number at all. A fraction over all rungs would make
    `undetermined_count` derivable and therefore pointless.

    ⚠ `0.0, 0` FOR A SUBTREE OF ONE UNHELD RUNG IS THE HONEST ANSWER AND NOT A FAILURE. Nobody
    holds anything, so no fraction is sovereign; the caller distinguishes that from a contested
    subtree by the second number, which is what it is for.

    ⚠ PERSON-KIND RUNGS ARE EXCLUDED, AND THE FIRST WRITING COUNTED THEM. `descendants` walks
    `contain`, and a person's own rung is contained like everything else, so a realm with four
    inhabitants reported four more `undetermined` places than it has. Counting heads in the
    denominator makes a populous duchy look less determined than an empty one. The exclusion is
    this module's reading and is stated rather than silent -- §10's ladder does put `person` on it,
    and `own` eligibility is "a person governing themselves", so the other reading exists and is
    simply not what this Query answers.

    ⚠⚠ `undetermined_count` IS NOT "UNHELD TERRITORY", AND THIS DOCSTRING USED TO SAY *"sovereignty
    is over TERRITORY"*, WHICH INVITED EXACTLY THAT READING -- a reviewer made it. EVERY OTHER rung
    kind in the denominator is GOVERNABLE: `offices.yaml: titles: domains:` declares a title for
    each (moved from `rosters.yaml: titles`, position `8a`, 2026-09-29 -- `TITLE_DOMAINS`/
    `title_domain` in `data/rosters.py` read the survivor), and `Family Head` governs
    `community`, `Mayor` governs `settlement`, `Lord` territory, `Duke`/`Duchess` duchy,
    `King`/`Queen` realm. So an unheld hearth is a governable seat nobody holds, not noise.

    MEASURED at `build_realm(0)`, `r_valoria`: `(0.4, 304)`, and those 304 are
    `hearth 205 · community 58 · settlement 36 · duchy 3 · territory 1 · realm 1`. That shape is
    the WORLD's, not this Query's -- the populated world seats 19 offices and none below
    territory. A caller wanting unheld TERRITORY filters `w.rungs[r].kind` itself; this number is
    every governable rung in the subtree that nobody holds, which is what §17 asked for."""
    TRACE.query("sovereign_fraction", "resolver")
    here = [r for r in [rung_id, *descendants(w, rung_id)]
            if r in w.rungs and w.rungs[r].kind != "person"]
    holder_of: dict[str, str] = {}
    for t in w.tenures:
        if t.kind == "hold" and t.live and t.object in w.rungs:
            holder_of[t.object] = t.subject
    held = [holder_of[r] for r in here if r in holder_of]
    undetermined = len(here) - len(held)
    if not held:
        return 0.0, undetermined
    top = max(held.count(h) for h in set(held))
    return top / len(held), undetermined


def provinces_of(w: World, rung_id: str) -> dict:
    """`{faction Proposition id: [territory ids]}` — the provinces that EXIST right now.

    ⭐ `systems/settlements/reference/scale_hierarchy_v1.md` §2, **RATIFIED, direct Jordan ruling
    2026-07-13**: *"Provinces are only formed if the same faction holds the constituent
    territories … territories are the fixed geographic units; a province is an emergent aggregation
    that exists only while its constituent territories share a common faction holder."* It replaces
    PP-726 §2.3's fracturing state-machine: *"A province isn't a container that sometimes breaks —
    it's a name for 'these territories, right now, cohering under one faction.'"*

    ⚠⚠ SO A PROVINCE IS A QUERY AND NOT A RUNG, AND THAT IS THE RULING ARRIVING AT THE SAME PLACE
    §22 DOES FROM THE OTHER SIDE. §22.1's reason for giving every aggregate to Nobody — *"if the
    aggregate is a function it cannot go stale, and it cannot be initialised and then forgotten"* —
    is exactly what an existence-conditional province needs: the moment a territory changes hands
    the province it was part of stops existing, and nothing has to be told. `province` stays a
    declared `rung_kind` (the ladder names it, and `contain_ascends` permits `territory -> duchy`
    directly), and `build_realm` builds none.

    ⚠ NO MINIMUM SIZE IS IMPOSED, BECAUSE CANON STATES NONE. A single territory held alone comes
    back as a group of one. Jordan's title note — a Count governs ONE province, a Lord may govern
    several territories *"that have not been assembled into a province"* — implies a threshold
    exists without giving it, so the caller decides and this does not invent one.

    ⚠ LIVE `hold` EDGES ONLY, like every aggregate here (§22.4 clause 3).

    ⚠⚠ THE ROOT RUNG IS NOT IN ITS OWN SUBTREE HERE, AND IT IS IN `sovereign_fraction`'s. Both
    docstrings say "the subtree" and they mean different sets -- `descendants(w, rung_id)` versus
    `[rung_id, *descendants(...)]` -- so `provinces_of(w, 'terr_T1')` is `{}` while
    `sovereign_fraction(w, 'terr_T1')` is `(1.0, 33)` for the same held territory.

    THE REASON IS WHAT EACH QUESTION IS ABOUT. Sovereignty is a property OF the rung asked about,
    so its own holder belongs in its own answer. A province is an aggregation of the territories
    BENEATH one, so the rung asked about is the container and not a member.

    ⚠ AN EARLIER DRAFT OF THIS PARAGRAPH JUSTIFIED IT BY SAYING THE ROOT WOULD OTHERWISE "report a
    lone territory as a province of one, which the ruling refuses" -- AND THAT IS FLATLY
    CONTRADICTED EIGHT LINES ABOVE, where this same docstring says *"NO MINIMUM SIZE IS IMPOSED,
    BECAUSE CANON STATES NONE. A single territory held alone comes back as a group of one."* The
    code agrees with the older paragraph: the grouping below applies no cardinality filter. Written
    down because two incompatible readings of one ratified sentence, both in one docstring, is the
    §4 idempotence trap -- and it was a fresh adversarial read that caught it, not this author."""
    TRACE.query("provinces_of", "resolver")
    here = {r for r in descendants(w, rung_id)
            if r in w.rungs and w.rungs[r].kind == "territory"}
    holder_of: dict[str, str] = {}
    for t in w.tenures:
        if t.kind != "hold" or not t.live or t.object not in here:
            continue
        fac = faction_holding(w, t.subject)
        if fac is not None:
            holder_of[t.object] = fac
    out: dict = {}
    for terr, holder in sorted(holder_of.items()):
        out.setdefault(holder, []).append(terr)
    return out


def faction_holding(w: World, subject: str) -> "str | None":
    """WHICH FACTION A `hold`'s SUBJECT COHERES UNDER — the faction Proposition id, or `None`.

    ⚠⚠ THIS EXISTS BECAUSE ITEM 16 RE-HOMED EVERY RUNG `hold` FROM A FACTION TO A PERSON AND
    `provinces_of` READ THE SUBJECT DIRECTLY. `holonic §15` makes `hold` a PERSON's edge, and
    `01_BUILD_ORDER` item 16 enforced it -- so the subject stopped being a faction Proposition and
    `provinces_of`'s `t.subject in w.propositions` filter matched nothing. MEASURED: the Query went
    from grouping 16 territories to returning `{}`, silently, and the only thing that caught it was
    a test asserting the OLD shape. The plan that scheduled item 16 did not price this.

    ⚠ **THE RATIFIED SENTENCE IS PRESERVED RATHER THAN AMENDED, AND THAT IS THE WHOLE POINT.**
    `scale_hierarchy_v1.md` §2 (RATIFIED, direct Jordan ruling 2026-07-13) says a province exists
    *"only while its constituent territories share a common FACTION holder."* A person holding land
    is a member of a faction, so "the same faction holds these territories" is still exactly the
    question -- it is now answered through the holder rather than read off the edge. Grouping by
    the PERSON instead would have quietly replaced a ratified rule with a different game (a
    magnate's demesne, not a faction's province) by way of a data change.

    ⚠ MEMBERSHIP HAS ONE OWNER AND THIS DOES NOT MINT A SECOND. §14.2: *"Membership is `commit`"*,
    and `members()` above reads exactly this edge from the other end. A subject that is itself a
    faction Proposition still answers for itself, so a world built the old way reads the same.

    ⚠ NONE AND MANY BOTH RETURN `None`, AND NEITHER IS A DEFAULT. A holder committed to no faction
    holds land that coheres into no province -- which is the same reading `Uncontrolled` already
    gets, and a thing to play for. A holder committed to two is a genuine question this Query does
    not get to answer by picking one: canon states no precedence between a magnate's two
    allegiances, so inventing one here would put a ruling in a Query."""
    if subject in w.propositions and subject in FACTION_BY_PROP:
        return subject
    if subject not in w.persons:
        return None
    facs = {t.object for t in w.persons[subject].tenures
            if t.kind == "commit" and t.live and t.object in FACTION_BY_PROP}
    return next(iter(facs)) if len(facs) == 1 else None


def holder_faction_of(w: World, rung_id: str) -> Optional[str]:
    """M4 (`ED-IN-0279` clause (a)). Which faction holds `rung_id` -- the faction Proposition id,
    or `None` -- read up its own ancestry, since a SETTLEMENT is never itself the object of a
    `hold` Tenure in this corpus (`hold_force` on one returns `None` always; every live `hold`
    targets a `territory` or an `Office`). `nearest_store`'s own walk, applied to holding rather
    than to a larder: the nearest rung AT OR ABOVE `rung_id` that IS held, then `faction_holding`
    on ITS holder (a person) -- never on `rung_id` itself, which `faction_holding` cannot answer
    for at all (`subject not in w.persons` returns `None` immediately; it takes the HOLDER, not
    the held object -- confirmed against the live fixture before this was written, not assumed
    from the name).

    ⚠ `None` FOR "NOBODY HOLDS ANY RUNG UP THIS CHAIN" IS A SHORTFALL, NOT AN ERROR --
    `nearest_store`'s own reading of an empty root. What a `march` targeting an unheld
    (`Uncontrolled`) settlement means is `march`'s own eligibility to decide, not this Query's.

    ⚠ THE WALK IS `ancestry`, NOT A FOURTH HAND-ROLLED COPY (M4 review pass, `/simplify` reuse
    finding). A first writing repeated `ancestry`'s own visited-set-guarded parent walk inline,
    one screen away from `ancestry` itself in this same file -- exactly the duplication that
    function's own docstring exists to end."""
    TRACE.query("holder_faction_of", "resolver")
    for cur in ancestry(w, rung_id):
        t = hold_force(w, cur)
        if t is not None:
            return faction_holding(w, t.subject)
    return None


def establishment_of(w: World, office_id: str) -> list[str]:
    """§11 -- *"the named persons the office employs. Finite, contested, durable."* -- AS A QUERY
    OVER LIVE `oblige` TENURES, the persons obliged to this seat, in `w.tenures` order.

    ⚠ REWRITTEN AT PLAN POSITION `17a` (r2 item 9, `03_SEATS_AND_CONTENT.md` §A.9): the body is
    §A.9's own, verbatim, and the name and signature did not move. It read `Office.establishment`,
    a field `[]` on every office in every world (nothing wrote it), and `ARCH §B.7` call 2 deletes
    it: *"`establishment` is a Query over `oblige`, not a field. A set of persons on a seat is two
    homes for one fact. A person joins by `oblige : Person -> Seat` and leaves by `release`."* The
    field is gone; this is the one home. A council is one seat whose members oblige (`AX §E.2.5`).

    ⚠ WITH A CALLER, OR NOT AT ALL (r2 `05` §A.1.5 RULED (d)). It had ZERO callers for as long as
    it read the field, and a Query with no consumer is a false N-line. Its consumer is
    `epistemic._ch_post_remit`, the obligee channel, which asks it rather than re-deriving the set --
    so the witness layer and anything else that asks *who serves this seat* get one answer.

    It is NOT the holder: §22 is explicit that an Office never owns *who holds it* -- that is a
    `hold` Tenure -- so this returns those who serve and `hold_force` returns the seat's occupant.
    `_req_oblige` refuses the holder obliging to his own seat, so the two do not overlap by an act.

    ⚠ `H-34`'s *"establishment size per office kind"* is no longer a number anybody must supply:
    the size is however many have obliged. `ARCH §B.7` call 2 rejected that number by name (*"a
    number nobody can source"*); closed in `hole_register.yaml` at `17a`."""
    TRACE.query("establishment_of", "resolver")
    return [t.subject for t in w.tenures
            if t.kind == "oblige" and t.object == office_id and t.live and t.subject in w.persons]


def upkeep_of(w: World, office_id: str) -> int:
    """`Office.upkeep`'S READER -- plan position `17b`, and the field's first since the ratified `04
    §B.7` `Seat := ( …, upkeep, dates[], exists )` declared it. WHAT THIS SEAT PAYS EACH PERSON
    OBLIGED TO IT, PER TERM: the seat's own declared amount, or the fixture `default_upkeep`
    (`H-158`) when it declares none. The ONE place that fallback is read, so no caller carries a
    number of its own -- `_eff_transfer` asks it to count how many obligees a payment covers.

    `F.18` is the gap it answers: *"upkeep's source -- 'out of the office's stake', and `stake` was
    retired ... no economic pressure on any office. A MATTER payment would be a fourth clock, so the
    repair is a verb."* The verb is the existing `transfer` (the plan's Contradiction-1 box, and the
    retirement plan's G2: *"treasury = `Rung.stores` at the office's own rung; payment = the
    existing `transfer` verb"*), so this Query supplies the amount and nothing moves on its own.

    ⚠ UNITS OF WHATEVER MATTER THE PAYING `transfer` CARRIES -- A LIMIT, STATED. `04 §B.7` names the
    field and no document names its matter kind, so a grain payment and a salt payment count alike
    here. Keying upkeep by kind (`{grain: 2}`) would need a kind nobody has ruled and a second
    schema for one Seat field; the int is the smallest type that makes a payment countable, and
    `H-158`'s row carries the kind question rather than this body deciding it."""
    TRACE.query("upkeep_of", "resolver")
    off = w.offices[office_id]
    if off.upkeep is not None:
        return off.upkeep                 # `Office.__post_init__` already refused a bad declaration
    v = w.fixtures.get("default_upkeep")
    # THE FIXTURE GETS THE SAME REFUSAL THE FIELD DOES, here at its one reader: a sweep arm of `0.5`
    # or `-1` would otherwise count fractional or negative obligees and renew a number nobody set.
    if isinstance(v, bool) or not isinstance(v, int) or v < 0:
        raise Forbidden(
            f"fixture default_upkeep is {v!r}", "ARCH §B.7",
            needs="a whole, non-negative amount per obligee per term (H-158's sweep is 0 / 1 / 3)",
            law="ARCH §B.7 / F.18 -- upkeep counts how many obligees a payment covers; "
                "`Office.__post_init__` refuses the same value on the field")
    return v


def ancestry(w: World, rung_id: str) -> list[str]:
    """`[rung_id, its parent, ..., the root]` — the containment walk up from a rung.

    ⚠ **IT EXISTS BECAUSE THREE SITES HAD ROLLED IT BY HAND**, which is the same reason and the
    same remedy as `home_of` above. `parent_of` owns ONE EDGE; every caller that wants the CHAIN
    was repeating the identical loop — step, guard with a visited set, stop at the root or on a
    revisit — in `WorldReader._ancestry`, in `conferral_path`, and most recently in
    `harness/governance_spine.census`. §8: the walk is a rule, and a rule lives once.

    ⚠ **THE VISITED SET IS LOAD-BEARING, NOT DEFENSIVE.** `World.add_tenure` enforces strict
    ascent on a `contain` edge, so a well-formed world presents no cycle — but `contain_ascends`
    passes any edge whose endpoints are not both resolvable rungs, so a half-built world can. The
    three hand copies each carried their own guard and agreed; consolidating keeps that agreement
    a property of one function rather than a coincidence of three.

    The start rung is INCLUDED, so `len(ancestry(w, r)) - 1` is its depth and a root returns
    `[root]`. An unknown id returns `[id]` — this reports the containment edges that exist and
    does not assert the rung does.

    ⚠ **IT DOES NOT `TRACE`, AND THAT IS THE EXTRACTION BEING CORRECT RATHER THAN AN OMISSION.**
    The first writing called `TRACE.query("ancestry", "resolver")` like its neighbours, and
    `test_w15_report_py_reproduces_every_committed_artifact_byte_for_byte` went red on `TRACE.txt`
    and `results.json`: `conferral_path` traces its own name and would now have traced twice, and
    `WorldReader._ancestry` traced nothing and would have started. A helper extracted to remove
    duplication must be INVISIBLE to its callers -- the moment it emits, consolidating three copies
    becomes a behaviour change, and the callers own their query names."""
    out: list[str] = []
    seen: set[str] = set()
    cur: str | None = rung_id
    while cur is not None and cur not in seen:
        out.append(cur); seen.add(cur)
        cur = parent_of(w, cur)
    return out


def conferral_path(w: World, office_id: str) -> list[str]:
    """The chain of seats from this office UP to the rung that confers it, by containment.

    §11 gives an Office a `conferral` basis and a `rung?`; §10 gives the ladder. The path is the
    walk from the office's own rung to the root, which is the same walk `under_purview` makes and
    is why a Duke seated at the realm would have realm-wide purview.

    ⚠ IT RETURNS RUNGS, NOT OFFICES, AND THAT IS A LIMIT RATHER THAN A CHOICE. `H-101` is graded
    `absent` and says so in terms: *"NOTHING CAN BE UNDER ANYTHING, AT EITHER INSTITUTIONAL
    SCALE. `factions` is a flat set of eight names and `Office` has no superior."* Until an
    Office can name a superior office, the only real chain is the place ladder, and returning
    rungs says that out loud instead of implying an institutional one exists."""
    TRACE.query("conferral_path", "resolver")
    off = w.offices.get(office_id)
    if off is None or off.rung is None:
        return []
    return ancestry(w, off.rung)


def questions_for(w: World, p: Person, since: Optional[tuple] = None) -> list[Question]:
    """§F1's `q` producer -- TWO sources, resolver-side, at the DELIBERATE barrier.

    ⚠ THIS CLOSES `H-04` AND §61's `NoProducer`, which between them blocked every NPC case: with
    no producer for `q`, `assemble(person, question)` was UNSATISFIABLE and DELIBERATE had no
    declared entry point, so `opening_set` had nothing to compute a set FROM. That is why the
    instrument needed an authored `roster` -- `D2`.

    ⚠ FOLDED TO TWO AT POSITION `11a` (r2 `01_ATTENTION_AND_REACH.md` §A.2, `05_LEDGER_AND_BUILD.md`
    §A.4.1 item 2). `date_due` and `band_crossed` MEASURED zero questions in every world the engine
    could build -- Q1's addressing clause was unsatisfiable and Q3 keyed a verb string where an id
    was needed (`H-110`) -- and `04 §B.13` `ID-13` treats a declared source that reaches no code as
    the defect, not as a source worth keeping. Both fold into `claim_landed` rather than vanish: a
    fired date and a band crossing are each already an Event that WITNESS already deposits as a
    claim, so the fold is entirely in what admits that claim as a question, not in what produces
    it. `date_due`'s half needs CALENDAR to emit `date.fired` first (position `11b`, BUILT
    2026-09-29 -- `loop/calendar.py`'s write now carries `emits="date.fired"`) AND needs that
    emission to actually reach WITNESS, which it still does not: `loop/driver.py`'s barrier-4
    dispatch (`:404,462`) passes only MATTER's and the fold's events into `witness()`, never
    CALENDAR's own (found at BATCH-CLOSE, methodology-close Phase 3 terminal critique, F4;
    `test_season_shape.py:4307-4316` already pins the resulting "0 of 0" claims). So `date_due`
    is unblocked by neither half yet -- 11b closed the emission gap and opened the routing one;
    `band_crossed`'s half needs nothing further, because `_crossings` (`loop/matter.py`) already
    emits a witnessable Event whose claim's subject is the site (`epistemic.claim_subjects`'s
    anchor fallback) -- `reach`/`place_of`, below, are what let a claim about a place reach someone
    who was never at that place: a seat's own purview, the ladder above their home.

    Q4 `need` (PLAN `W5`, #353 `:509`, `:605`, `:1297`) survives untouched: a live `commit` to an
    OUGHT Proposition generates a standing question every season, and without it "an NPC with a
    standing ambition and a quiet season forms no candidates at all", which is most of the NPC
    corpus. The sources are `rosters.yaml`'s `question_sources`, IN ORDER, because a budget-bounded
    person answers the earlier one first.

    Resolver-side by construction: it takes a `World`. §F1 says both are "already produced by the
    loop" -- no new step, no new carrier, no clock -- and that is what this reads.

    ⚠ `since` IS `U2`'s ONE ADDITION AND IT GENERALISES Q2 EXACTLY. §F1 Q2 is *a claim LANDING in
    the holder's ledger*, and while a season was ONE PASS "landing" could be read off `when` alone:
    the previous season's WITNESS stamped `when = tick - 1` and DELIBERATE read it at `tick`. Once
    a season is several rounds, a claim can land in round 1 and be new to a person deliberating in
    round 2 of the SAME tick, which `when` cannot express. `since` is the driver-owned
    `(tick, round)` of that person's LAST deliberation, and `Claim.round` is the field that makes
    the pair comparable.
    ⚠ THE DEFAULT REPRODUCES THE OLD READING BIT FOR BIT, WHICH IS WHY THIS IS A GENERALISATION
    AND NOT A CHANGE. `since=None` means `(w.tick - 1, 0)`; every claim carries `when <= tick - 1`
    at DELIBERATE, because WITNESS stamps `when = t` and the tick advances after it -- so
    `(c.when, c.round) >= (tick - 1, 0)` selects exactly the claims `c.when == w.tick - 1` did.
    The one-round arm of `H-124`'s sweep is the executed control for that claim."""
    TRACE.query("questions_for", "resolver")
    out: list[Question] = []

    # Q2 -- a claim landing in p's own ledger, ADMITTED THROUGH `reach` (`01` §A.4-§A.5): the
    # claim's own subject is something REACH covers (today's test, generalised -- `me`/`mine`
    # subsume `c.subject == p.id or c.subject in mine`), OR the claim's subject is AT a place
    # REACH covers. `since_tick` is the season boundary: "landing" is new.
    # ⚠ THE PREVIOUS SEASON'S WITNESS, NOT THIS ONE'S. §F1 Q2 is "a claim LANDING in the
    # holder's ledger AT WITNESS", and WITNESS runs at the END of a season: the deposit is
    # stamped `when = t` and DELIBERATE reads it at `t + 1`. Testing `c.when == w.tick` therefore
    # matched nothing, ever — Q2 was dead for every person in every season, which is half of why
    # nothing propagated. Found by running `headless.py` and reading the ledgers.
    # `U2`: the boundary is *since this person last deliberated*, which is the season boundary
    # when nothing else is supplied. See the docstring for why the two readings coincide at R = 1.
    #
    # ⚠ THE PLACE CLAUSE IS A FILTER, NOT A FAN (`01` §A.4.4, LB-2b): `reach(w, p)` is read-only
    # over `p`'s own tenures and the world's tenure/office/rung stores, `observers_for` is untouched
    # and unaware `reach` exists, and this loop still reads only `p.ledger`. Widening `R` changes
    # which of THIS PERSON'S ALREADY-LANDED claims become a question; it cannot put a claim in a
    # ledger it was never witnessed into. `place_of` may return `None` (a Proposition-subject claim
    # has no place), and `None in R` must be impossible -- the walrus binds it once so the `is not
    # None` guard is written rather than relied on by accident (`01` §A.5.2, `AR-6`).
    #
    # ⚠ CLAUSE 3 (`named(c)`, the id set inside a `content:`-predicate claim) SHIPS HERE, at
    # position `15c` (r2 `01` §A.5.3/§A.5.4, `02` §A.9.1): the deposit rule landed at positions
    # `15`/`16` (`loop/witness.py`'s content deposit), so a `content:<kind>` claim now carries the
    # Record's real `subject_matter` instead of `True` -- the producer §A.5.3 was waiting for.
    # ⚠ NOT A FOURTH SOURCE, NOT A WIDENED REFERENT (§A.5.4). One `Question` shape, one `source`
    # string ("claim_landed", unchanged), one `occasioned_by` route. The Question is still
    # `(c.subject,)` -- clause 3 only ADMITS the claim into `out`; it does not change what the
    # Question is ABOUT. `requires_operands` is untouched by this clause for exactly that reason.
    R = reach(w, p)
    floor = since if since is not None else (w.tick - 1, 0)
    for c in p.ledger:
        if (c.when, c.round) < floor:
            continue
        if (c.subject in R                                       # clause 1 -- the thing itself
                or ((pl := place_of(w, c.subject)) is not None and pl in R)   # clause 2 -- where it is
                or any(x in R for x in named(c))):                # clause 3 -- whom the CONTENT names
            out.append(Question(f"q:claim:{c.id}", "claim_landed", (c.subject,), c.id))

    # Q4 -- `need`. A live `commit` Tenure whose object is an OUGHT Proposition is a STANDING
    # question: it recurs every season until the commitment ends, which is what makes an NPC with
    # an ambition act in a quiet season.
    for t in p.tenures:
        if t.kind == "commit" and t.live:
            prop = w.propositions.get(t.object)
            if prop is not None and str(prop.mood).upper() == "OUGHT":
                out.append(Question(f"q:need:{t.object}", "need",
                                    (prop.subject,), t.object))

    # ⚠ TWO ORDERINGS LIVE IN THIS ONE LINE AND ONLY THE FIRST IS DECLARED ANYWHERE.
    # `order[q.source]` is `rosters.yaml: question_sources`, whose own note says ORDER IS SEMANTIC
    # and that editing it "changes which question a budget-bounded person answers first". That is
    # the ACROSS-source rule, declared, and `H-54` sweeps its consumer.
    # `q.id` is the WITHIN-source tiebreak and NOTHING DECLARES IT. For `claim_landed` -- the
    # source that supplies most questions in the corpus -- `q.id` is `f"q:claim:{c.id}"` and
    # `c.id` is a CONTENT HASH minted in `SeasonDriver.witness` off the depositing Event's own id,
    # so WHICH QUESTION A PERSON ANSWERS IS SETTLED BY LEXICOGRAPHIC ORDER OVER HASHES. It is not
    # cosmetic: MEASURED over 89 corpus baselines (`wd_extra.py`), the leading source is SHARED
    # with at least one other question in 801 of 1,068 deliberations, and a traced fork moved
    # `qs[0]` from a question about `p_c` to one about `r_hearth` purely because `0261...` sorts
    # before `219a...` -- changing every Candidate that person formed.
    # ⚠ THE SORT ALSO DESTROYS APPEND ORDER, so anything attributing this effect to "the ledger's
    # append order" is wrong; `W-D` did, and is corrected. Disposition (`CLAUDE.md` §0's five
    # tests) is recorded on `H-54`, which already owns "which question a budget-bounded person
    # answers": it closes at step 4 on `H-54`'s own precedent, `needs_jordan` is FALSE, and NO
    # RULE IS CHANGED HERE -- editing this sort is a design edit to a line three rows depend on,
    # not a repair, so it is declared and left alone.
    order = {src: i for i, src in enumerate(QUESTION_SOURCES)}
    out.sort(key=lambda q: (order[q.source], q.id))
    return out


def occasioned_by(w: "World", q: Optional["Question"]) -> list:
    """What EVENT occasioned a question — the antecedent an act formed from it must cite.

    ⚠ THIS IS `N3`'s MISSING EDGE, AND `N3` WAS MEASURED, NOT INFERRED: *60 act-Events, 0
    resolving to a question*. An act emitted `causes=[a.id]` and nothing else, so the graph knew
    which act made an Event and never which Event made the act — and `R3` (an act by one person
    caused by an act of another) scored **0 of 30** while `R1`, `R4` and `R5` all passed. The
    chain Reading 07 §4 calls *"the one that is actually the game"* — a claim lands in a ledger,
    raises a question, forms a candidate, becomes an act, emits an Event, is witnessed, deposits
    in SOMEONE ELSE'S ledger — was built end to end except for this one edge.

    **ONE ROUTE, since position `11a` folded `date_due` and `band_crossed` out of
    `question_sources` (`01_ATTENTION_AND_REACH.md` §A.2, `05_LEDGER_AND_BUILD.md` §A.3.1):**

      * `claim_landed` — the deposit Event names the claim in its `changes[]`; its `causes[]`
        name the Event the claim is ABOUT. **The originating Event is returned, not the deposit.**
        The claim IS a belief about that Event — `Claim.predicate` is literally `e.kind` at the
        deposit — so citing the transport instead would put the postman in the arc. The deposit
        stays in the graph on its own `causes[]`; nothing is lost by not naming it twice.
      * `need` — **empty, on purpose.** A standing commitment to an OUGHT is interior; no Event
        caused it this season, and `ID-5`'s polarity says absence maps to the refusal rather than
        to a plausible default. An act taken out of a standing ambition genuinely has no
        antecedent but the actor, and `[ROOT]` is what the design already has for that.

    ⚠ **WHAT THIS DELETES IS A GUARD AND AN UNREACHABLE SEARCH, NOT TWO BRANCHES.** `date_due` and
    `band_crossed` never had a branch of their own here — `05` §A.3.1's correction to an earlier
    draft of this same plan: *"there is no `date_due` branch and no `band_crossed` branch … a
    NEGATIVE membership guard … lets exactly those two fall through to the generic id search …
    which finds nothing."* `date_due` was dead because CALENDAR emitted no Event for a fired Date;
    `band_crossed` was dead because the Question it built carried the crossing's **verb** —
    `"work"` — where an id belongs, so the id search could never match (`H-110`). Deleting the two
    sources deletes the guard's tuple and leaves the id search with no caller, so the search goes
    with it rather than surviving as dead code with nothing left to reach it.

    ⚠ **This count has been wrong twice before landing here**: *"one route per question source"*
    first, then *"two of four"* after a critic found `band_crossed` still nominally rostered. **The
    lesson is in the count, not in the routes: a route's liveness is a property of its PRODUCER,
    and this function cannot see its producers** — which is why, now that both dead sources are
    gone from the roster, there is exactly one route left to get wrong.

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
    # ⚠ NOT A BARE `else`, AND STILL DEFENCE IN DEPTH RATHER THAN THE FIRST GATE. An undeclared
    # source reaching here would otherwise need a branch nobody wrote, which the polarity `ID-5`
    # refuses: zero evidence maps to the verdict AGAINST the thing measured, never to a quiet
    # default. `Question.__post_init__` already refuses a source outside `question_sources`, so
    # this raise is unreachable from a rostered question and fires only if that constructor is
    # bypassed, or the roster grows a source this function is not taught a route for.
    raise Unspecified(
        f"no occasion route for question source {q.source!r}", "ID-16",
        needs=f"a route here, or one of {sorted(QUESTION_SOURCES)}",
        law="ID-5 -- refuse, don't default. A new question source silently taking a plausible "
            "default would answer wrongly for every question it raised")


# ---------------------------------------------------------------------------
# `WorldReader` -- MOVED HERE FROM `queries/readers.py` AT UNIT L3 (ED-IN-0206), and the move ANSWERS
# a question `queries/__init__.py` had already framed and deferred: *"By source they would split
# `WorldReader` -> `world_q` and `LedgerReader` -> `person_q`; `person_q` does not exist until step 7
# ... whether §A.2's roster then absorbs them is a Layer-1 call for that step, not this one."*
# `person_q` exists now, so this is that call, taken the way that docstring predicted rather than
# left as a FOURTH module in a package `04 §A.2` enumerates with three. `WorldReader` asks THE WORLD
# -- it takes a `World` and reads the actor's own ledger through it -- so it belongs in the
# World-first module; `LedgerReader` takes claims and nothing else, and is in `person_q`.
# ---------------------------------------------------------------------------

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
        return ancestry(self._w, start)

    def read(self, subject, predicate: str):
        w = self._w
        stem, _, arg = str(predicate).partition(":")
        if stem == "exists":
            # An EDGE kind is a `tenure_kinds` member and an OBJECT class is one of `World`'s own
            # collections. Both are DATA -- neither is a list written here.
            if arg in TENURE_KINDS:
                return sum(1 for t in w.tenures
                           if t.kind == arg and t.object == subject and t.live)
            # A RECORD KIND is a `record_kinds` member, and asks for a Record OF THAT KIND -- plan
            # position `15`, where `Petition` stopped being a collection of its own and became a
            # kind of `Record` (`04 §B.5`). `carry`'s cell is the reader. The two vocabularies are
            # disjoint by a load-time refusal (`data/rosters.py`), so this order decides nothing.
            if arg in RECORD_KINDS:
                r = w.records.get(subject)
                return 1 if r is not None and r.kind == arg else 0
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
            if not floors:
                # `_req_work`'s refusal, carried unchanged: `H-08` owns the per-kind floors and
                # §42.2.1 forbids picking a plausible number for a kind nobody registered.
                # `not floors` catches BOTH a missing kind (`None`) and a kind registered with no
                # uses (`{}`, `dwelling`'s control-arm row, `24d-i`) -- `min({}.values())` is a bare
                # `ValueError`, not this typed refusal, and `is None` alone let it through.
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
            return UNKNOWN if place is None else (arg in presence(w, place))
        if stem == "claim.held":
            p = w.persons.get(self._actor)
            return UNKNOWN if p is None else any(c.subject == subject for c in p.ledger)
        if stem == "rank":
            # `21_RECONCILIATION.md` PHASE 2 step 9 / `03_PARAMETERS.md` §C.1 -- THE ORDINAL, NOT
            # A KIND CHECK. `rung_kinds` is an ORDERED roster (`person` first), so a rung's rank
            # is its own kind's position in it -- correct if a sub-settlement tier is ever added,
            # where an enumerated kind list would not be (§C.2's falsifier: change the roster's
            # membership and see what breaks). A Person's own rung carries kind `"person"`
            # (`tiny_world`'s `w.rungs[pid] = Rung(pid, "person")`), so this stem answers for a
            # person address exactly as for any other rung, at rank 0.
            r = w.rungs.get(subject)
            return UNKNOWN if r is None else RUNG_KINDS.index(r.kind)
        return UNKNOWN
