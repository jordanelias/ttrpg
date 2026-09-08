"""`season.queries.world_q` — THE WORLD-FIRST HALF OF `Query`, AND THE TWO WORLD-FIRST
FUNCTIONS THAT WERE NEVER IN IT.

EXTRACTED, step 5 of the decomposition. `04_CODE_ARCHITECTURE.md` §A.3 row 2 is the ruling and it
is a MODULE ruling, not a signature one: *"one `Query` class holding both families -> two modules;
the second cannot import the first ... In one class, a person-side function calls a resolver-side
one with no import to scan."* The eleven functions here all take a `World` FIRST. The four
person-side statics stay on `Query` in `shape.py` until step 7 puts them in `decision`, which is
the module that may not name `World` at all.

⚠ THE ELEVEN ARE MODULE FUNCTIONS NOW, AND `shape.Query` BINDS THEM AS `staticmethod`s. That is a
re-export, not a copy — `Query.parent_of is world_q.parent_of` — so the 73 call sites reading
`Query.<world-first>` resolve to these bodies and there is exactly one owner of each rule. The
binding is what makes the class deletable at step 7 without a second migration.

⚠ THIS MODULE MUST NOT LEARN A PERSON. Its one-way rule is the same one `state/` states: nothing
here imports `shape`, `decision`, `loop` or `seam`. `questions_for` takes a `Person` as its SECOND
argument and asks the WORLD about them; that is a world-first function, not a person-side one, and
the AST guard (`test_w5_sense_is_still_the_only_world_taking_non_decision_function`) is what keeps
the distinction checkable by signature rather than by intention.
"""

from __future__ import annotations

from typing import Callable, Optional

from ..data.rosters import QUESTION_SOURCES
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
