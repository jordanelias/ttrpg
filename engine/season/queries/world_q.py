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

from ..data.rosters import QUESTION_SOURCES
from ..data.requires import UNKNOWN
from ..data.rosters import TENURE_KINDS
from ..gaps import Forbidden, Unspecified
from ..state.carriers import Person, Question, Site, Tenure
from ..state.ids import ROOT
from ..state.world import World
from ..trace_log import TRACE


# ===========================================================================
# S17 -- QUERY. THE SIDE COLUMN IS THE ENFORCEMENT.
# ===========================================================================

# ---- resolver-side: World FIRST, always -----------------------------
def parent_of(w: World, rung_id: str) -> Optional[str]:
    for t in w.tenures:
        if t.kind == "contain" and t.subject == rung_id and t.live:
            return t.object
    return None

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

def judging_set(w: World, rung_id: str) -> list[str]:
    raise Unspecified("judging_set_rule", "S61", needs="who decides at a sitting",
                      law="S61 -- NOTHING IS DECIDED AT A SITTING. T5's 'filtered at a rung' runs straight through it, and S10.2's 'arrangements, not choices' cannot be confirmed until it is")

def presence(w: World, rung_id: str) -> list[str]:
    """S28 -- the PRESENCE INDEX the global fan-out reads."""
    TRACE.query("presence", "resolver")
    return [t.subject for t in w.tenures
            if t.kind == "contain" and t.object == rung_id and t.live
            and t.subject in w.persons]


def questions_for(w: World, p: Person, since: Optional[tuple] = None) -> list[Question]:
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
    the loop" -- no new step, no new carrier, no clock -- and that is what this reads.

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
    mine = {t.object for t in p.tenures if t.live}

    # Q1 -- a Date coming due whose DocketItem names a matter, for every person in its judging set.
    for did, d in sorted(w.dates.items()):
        # [JUSTIFIED: a SENTINEL, not a game value -- a Date with no `due_at` is never due]
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
    # `U2`: the boundary is *since this person last deliberated*, which is the season boundary
    # when nothing else is supplied. See the docstring for why the two readings coincide at R = 1.
    floor = since if since is not None else (w.tick - 1, 0)
    for c in p.ledger:
        if (c.when, c.round) >= floor and (c.subject == p.id or c.subject in mine):
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
        if who == p.id or (at is not None and p.id in presence(w, at)):
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
        seen, cur = [], start
        while cur is not None and cur not in seen:
            seen.append(cur)
            cur = parent_of(self._w, cur)
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
            return UNKNOWN if place is None else (arg in presence(w, place))
        if stem == "claim.held":
            p = w.persons.get(self._actor)
            return UNKNOWN if p is None else any(c.subject == subject for c in p.ledger)
        return UNKNOWN
