"""`loop/deliberate.py` -- DELIBERATE -- a MAP, not a barrier. `04 §A.2`: owns **nothing**; calls `sense()`, builds a `View`, calls `choose` per person; reads a frozen `World`, **for `sense` only**; **token: none**.

⚠ **THE BODY IS THE DRIVER'S OWN, BOUND BACK ONTO THE CLASS -- NOT A DELEGATING STUB.**
`loop/driver.py` ends with `SeasonDriver.deliberate = deliberate`, so `SeasonDriver.deliberate` IS this
function and `inspect.getsource(SeasonDriver.deliberate)` returns THIS SOURCE. Eight tests read a
step's body that way -- three of them `witness`'s, one of those a pure NEGATIVE assertion --
and a stub would fail two and silently vacate the third, which is why step 9 of the
decomposition (ED-IN-0203) refused to delegate. Step 5 established the technique when
`class Query` bound module functions as staticmethods.

⚠ **THE TOKEN IS STILL A `WriteClass` PARAMETER AND THAT IS G2's, NOT THIS UNIT's.** `04 §A.3`
row 3 replaces the parameter with an unforgeable token type minted only by the driver; until
that lands, this step passes `WriteClass` exactly as it did inside the class. Unit L5
delivers the MODULE boundary `04 §A.2:134` requires; the write discipline is Arc 2.

⚠ **THE §A.2 ROW QUOTED ABOVE IS NOT WHAT THIS BODY DOES, AND SAYING SO IS THE POINT.** The row reads
*"owns nothing; calls `sense()`, builds a `View`, calls `choose` per person; reads a frozen `World`,
**for `sense` only**; token: none."* Measured against the body:

- it calls `w._rehome()`, which MUTATES the tenure store, during DELIBERATE -- a barrier that owns
  nothing and holds no token;
- it reads `w.fixtures` and calls `questions_for(w, p)`, a `world_q` read that is not `sense`;
- it sets `w.step` and `w._in_parallel_map`, and writes `self.scenes` and `a.scene`.

None of that is L5's doing -- the body is unchanged from when it was a method on `SeasonDriver` --
but the module boundary is what makes the divergence checkable, so it is recorded here rather than
left for a reader to find under a header that reads like conformance. **The `_rehome()` call is the
one that matters**: either it moves to the MATTER barrier or the row is amended. That is a Layer-1
question, not this unit's. Found by the Fable gate on Arc 1 and filed under `ED-IN-0206`.
"""

from __future__ import annotations
from ..decision import standing_of
from ..gaps import InstrumentDefect
from ..state.carriers import Scene, Sensation
from ..state.ids import H

from typing import Any, Callable
from .. import decision
from ..data.matrix import Step
from ..data.requires import REQUIRES_STEMS
from ..decision import aggregate_questions
from ..gaps import Forbidden, Ungraded
from ..queries.world_q import questions_for
from ..state.carriers import Act, Person
from ..state.world import World
from ..trace_log import TRACE



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
    per_round = w.fixtures.get("scenes_per_round")
    w._in_parallel_map = True       # S51: WorkerThreadPool over persons. The one that pays.
    ext = w.fixtures.get("extended_scene_cost")
    for p in list(w.persons.values()):
        s = sense(p, w, subsistence)            # a Sensation, per S26's signature
        # §F1 / `H-04`. `q` HAS A PRODUCER NOW. Rev 3 took the question as an injected
        # parameter because §61 recorded that DELIBERATE HAD NO DECLARED ENTRY POINT; the
        # four sources are computed here, at the barrier, from the loop's own output.
        # An explicit `question` still overrides, so a probe can name the q it is testing.
        # ⚠ `U2`: SINCE THIS PERSON LAST DELIBERATED, not since last season. `None` on their first
        # deliberation of the season means `(tick - 1, 0)`, which is the pre-tick reading exactly.
        qs = questions_for(w, p, self._deliberated_at.get(p.id))
        # `H-54`, DECLARED. This was `qs[0] if qs else None` — an `absent` hole filled inside
        # a subscript, with no row and no alternative (`G1`). `question_sources` is ORDERED,
        # so taking the first silently ruled that A DATE ALWAYS BEATS A NEED, which decides
        # what every NPC does first. The rule is data now; `first` is the incumbent kept as
        # the sweep's control.
        q_p = question if question is not None else aggregate_questions(qs, q_rule)
        v = decision.assemble(p, q_p, k_view)
        # S26.3: the PERSON asks their own budget. `choose` receives the QUERY, not the
        # answer -- rev 2 computed it in the engine and handed the number down, which is
        # the half of retraction 5 that never landed.
        # ⚠ `U2`: THE REMAINDER, NOT THE WHOLE. The budget is the SEASON's and the season is now
        # several rounds, so what a person has left to spend is what they were given minus what
        # they have already spent. At `R = 1` nothing has been spent and this is the old value.
        ask_budget = lambda p=p, v=v: max(
            0, decision.budget(p, v, k_budget, w.fixtures) - self._spent.get(p.id, 0))
        b = ask_budget()
        # -------------------------------------------------------------------
        # `U2`: RE-DELIBERATE, OR RELEASE THE NEXT OF WHAT THEY ALREADY CHOSE.
        #
        # ⚠ **RE-ASKING EVERY ROUND IS THE DEFECT, NOT THE DESIGN.** `opening_set` is a pure
        # function of the person's own inputs, so a person for whom nothing moved re-derives THE
        # IDENTICAL RANKING and takes their top candidate again — and again, five times. Under the
        # one-pass loop `pack_scenes` sliced five DIFFERENT scenes off one ranking; a naive rounds
        # loop turns that into one scene done five times. So what the driver holds is the person's
        # OWN triage, and what it does each round is release the next of it.
        # ⚠ NOTHING IS DISCARDED, WHICH IS WHY THIS IS NOT THE ENGINE TRUNCATING (S26.3 / L1). A
        # queued scene is deferred, not dropped; and the moment anything the person reads moves,
        # they are asked again and may replace everything still queued.
        # ⚠ THE FINGERPRINT IS WHAT "NOTHING MOVED" MEANS, AND IT IS ENUMERATED RATHER THAN
        # ASSUMED — see `_inputs_fingerprint`, which lists every input `questions_for`,
        # `person_side_eligible`, `belief_contradicts` and `budget` read, and says which one each
        # term covers. If that list is incomplete the skip is wrong, which is what U2's falsifier
        # (b) tests.
        # -------------------------------------------------------------------
        fp = _inputs_fingerprint(p, qs, s)
        queue = self._queued.get(p.id) or []
        if b > 0 and (self._inputs.get(p.id) != fp or not queue):
            produced = choose(p, v, s, ask_budget)
            # `W17`. THE BUDGETED UNIT IS THE SCENE (Jordan, 2026-09-02), so the bound below
            # counts scenes and the interaction bound is a SEPARATE check. A bare `Act` is one
            # scene carrying one interaction -- which is exactly the pre-ruling semantics, so
            # every caller that returns Acts keeps its meaning and the change is additive.
            queue = _drop_what_was_already_done(
                as_scenes(produced, p.id, w), self._taken.get(p.id) or set())
            _qualify_by_round(queue, w, self.round)
            self._inputs[p.id] = fp
            self._deliberated_at[p.id] = (w.tick, self.round)
            # ⚠⚠ **BOTH CALLER-CONTRACT CHECKS MOVED INSIDE THIS BRANCH, AND THAT IS A SCOPE
            # CORRECTION RATHER THAN A RELAXATION.** They ask *did `choose` return more than it was
            # given*, which is a question about a RETURN VALUE — so they belong where the return
            # happens. Left outside, they re-examined the QUEUE every round against a remainder
            # that had since shrunk, and a person holding one unreleased scene with a remainder of
            # 0 was reported as having "returned 1 scene against a budget of 0" — an accusation
            # about a call that was made three rounds earlier and was lawful when it was made.
            # Measured: it fired on `p_b` in the NPC lane on the first corpus run under the tick.
            # The release loop below is what enforces the remainder, and it does so by DEFERRING
            # rather than refusing, which is the only reading that leaves the person's triage intact.
            spent = sum(sc.cost(ext) for sc in queue)
            # S26.3: the engine does NOT truncate. Any cap applied here would be AN ENGINE
            # DECIDING A PERSON'S OPTIONS, which is L1. Over-budget is the CALLER'S defect.
            if spent > b:
                raise Forbidden(
                    f"{p.id} returned {len(queue)} scenes costing {spent} against a budget of "
                    f"{b} scene actions", "S26.3",
                    needs="`choose` is bounded by budget(person, view) -- the PERSON chooses what to leave undone",
                    law="S26.3, re-stated in scenes per Jordan's 2026-09-02 ruling -- at one scene NOBODY EVER CHOOSES WHAT TO LEAVE UNDONE; the budget exists to create triage. An engine that silently discards the tail has made the choice instead of the person, which is L1. ⚠ THE UNIT MATTERS: eight INTERACTIONS across five scenes is LAWFUL and was refused before the ruling")
            # ⚠ A SEPARATE FAILURE, DELIBERATELY. `PLAN.md` `W17` item 3: the two propositions are
            # "a person returned more SCENES than `budget` allows" and "a scene carried more
            # interactions than the swept bound". Folding them into one check would make the
            # ruling's whole distinction unobservable.
            cap = w.fixtures.get("interactions_per_scene")
            for sc in (queue if cap is not None else ()):
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
        scenes = queue
        # ⚠ THE TRACE IS PER-SCENE, AND THE UNITS MUST NOT BE MIXED. It read
        # `TRACE.act(p.id, a.verb, b - i - 1)` where `b` is a SCENE budget and `i` enumerated
        # the FLATTENED interactions, so a lawful season published `budget_left=-10` — the
        # artifact stating that the engine had just accepted an overspend it did not. That is
        # the same defect the `act_budget` -> `scene_budget` rename was made to prevent, one
        # field along: a name is where the next reader learns what a number counts, and so is
        # a unit. `scene_left` is scenes; `interaction` is the position inside the scene.
        # -------------------------------------------------------------------
        # `U2`: THE RELEASE. At most `scenes_per_round` (`H-124`) of what the person chose runs
        # this round, and only while their season remainder covers the cost. The rest stays
        # queued for the next round; a scene they cannot afford stays queued rather than being
        # trimmed, because the affordability is a fact about the season and not about the scene.
        # ⚠ AT `scenes_per_round = 5` (the sweep's control arm) a person's whole season is
        # released in round 0 and every later round finds `queue` empty and `b` zero, which IS
        # the one-pass loop — reproduced through this code rather than around it.
        # -------------------------------------------------------------------
        produced = []
        left = b
        released = 0
        while scenes and released < per_round:
            cost = scenes[0].cost(ext)
            if cost > left:
                break
            sc = scenes.pop(0)
            left -= cost
            released += 1
            self._spent[p.id] = self._spent.get(p.id, 0) + cost
            self._taken.setdefault(p.id, set()).update(
                (a.verb, _subject_of(a)) for a in sc.acts if _subject_of(a))
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
        self._queued[p.id] = scenes
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


# ---------------------------------------------------------------------------
# ⚠ `sense` AND `as_scenes` LIVE HERE, NOT IN `driver.py`, AND THE REASON IS A REAL IMPORT CYCLE.
# L5's first cut left them in the driver, so `deliberate.py` did `from .driver import as_scenes,
# sense` while `driver.py` imported this module to bind the step -- a genuine
# `driver <-> deliberate <-> resolve` cycle that `tests/valoria/test_import_cycle_game_state_npe.py`
# caught immediately (4 cycles where the tree declares 3). It WORKED at runtime, only because the
# driver's bindings sit at the bottom of the file and these two are defined above them: ordering,
# not structure. DELIBERATE is their only caller, so they belong beside it -- and `04:116`'s
# *"`sense()` called by the loop, never by the decision"* and `04:158`'s grant of the frozen World
# to `loop/deliberate` *"for `sense` only"* both name THIS step by name.
# ---------------------------------------------------------------------------

def _subject_of(a) -> str:
    """The act's subject, or `""`. ⚠ `isinstance(..., dict)` AND NOT `a.payload or {}`, because a
    hand-built probe Act may carry a STRING payload — `_operand` in `loop/effects.py` guards it the
    same way and for the same reason. Caught by `test_no_probe_errors`, which ran fourteen probes
    through this line and reported `'str' object has no attribute 'get'` from six of them."""
    d = a.payload if isinstance(getattr(a, "payload", None), dict) else {}
    return d.get("subject") or ""


def _drop_what_was_already_done(scenes: list, taken: set) -> list:
    """`U2` / `R-03`: A SCENE-ACTION IS SPENT ON A DISTINCT OPPORTUNITY, ONCE PER SEASON.

    ⚠⚠ **THIS IS NOT A NEW RULE — IT IS THE ONE THE ONE-PASS LOOP HAD BY CONSTRUCTION, MADE
    EXPLICIT BECAUSE THE TICK REMOVED THE CONSTRUCTION.** `pack_scenes` consumes a ranking
    POSITIONALLY: chunk 1 is the top three candidates, chunk 2 the next three, chunk 3 the next.
    One call, three scenes, nine distinct opportunities. Re-deliberating every round restarts at
    the top of a freshly-derived ranking, so the person takes their best three again, and again.

    ⚠ **MEASURED, BEFORE THIS EXISTED**, at `build_world(0)`, 2 seasons: `create_record` x10,
    `reconstruct` x9, `research` x7, `move` x2 — **all by `p_carin`**, with `examine`, `interview`,
    `speak`, `tell`, `transfer`, `work` and `release` gone from the world entirely. One person
    doing their top three, five times a season.

    ⚠ **AND S26.3 IS WHY IT IS A DEFECT RATHER THAN A CURIOSITY.** The budget exists to create
    TRIAGE — *"at one scene NOBODY EVER CHOOSES WHAT TO LEAVE UNDONE"*. A person who may spend
    every scene on their single favourite option has nothing to leave undone either, so the triage
    the ruling asks for is gone in the other direction. `player_agency_v30.md` §6.3's unit is *one
    scene opportunity pursued*, and pursuing the same one five times is one opportunity, not five.

    ⚠ **WHAT IT IS NOT: THE ENGINE TRUNCATING A TAIL (S26.3 / L1).** It removes nothing the person
    has not ALREADY DONE. Their ranking is untouched, their triage is their own, and every
    candidate they have not yet spent a scene on survives — including the ones this season's
    events have just made attractive, which is the whole of what the tick buys. What it refuses is
    a second scene spent on an identical `(verb, subject)`, which the pre-tick loop could not
    express at all.

    ⚠ AND THE KEY IS `(verb, subject)`, NOT `verb`. A person may write two records about two
    different things in one season; what they may not do is write the same record twice.

    ⚠⚠ **AN ACT THAT NAMES NOTHING IS NEVER FILTERED, AND THE PROBES ARE WHY.** A subject-less act
    has no opportunity to be the same as — `(verb, "")` is an absence, not an identity, and two
    acts sharing it share only the absence. `probes.py::Act_` builds acts whose discriminator is in
    the ID and not in the payload, so `P2y` returned four scenes of `speak` with no subject and the
    first version of this filter dropped three of them, taking a probe about *several interactions
    inside one budgeted scene* from 12 acts to 3. `test_no_probe_errors` is what found it. Every
    COMPUTED act carries a subject when its Candidate has one (`_payload_of`'s unconditional
    `setdefault`), so the corpus is unaffected by the carve-out; what it protects is the honest
    reading of the key."""
    if not taken:
        return scenes
    out = []
    for sc in scenes:
        keep = [a for a in sc.acts
                if not _subject_of(a) or (a.verb, _subject_of(a)) not in taken]
        if keep:
            sc.acts = keep
            sc.extended = len(keep) > 1
            out.append(sc)
    return out


def _qualify_by_round(scenes: list, w: World, r: int) -> None:
    """`U2` / `R-03`: A RE-DELIBERATION MINTS INSIDE THE SAME TICK, SO ITS IDS NEED THE ROUND.

    ⚠ **THIS IS A MEASURED NECESSITY, NOT A PRECAUTION.** `mint(pid, verb, subj)` derives
    `H(seed, tick, pid, f"act:{verb}:{subj}")`, and `tick` advances once per SEASON. A person
    re-deliberated in a later round who chooses the same verb on the same subject therefore mints
    THE SAME ACT ID as the one already resolved, and the fold derives each Event id from the act's,
    so the duplication reaches the log. Measured over the 27 NPC rung cases at seed 0, 3 seasons,
    before this function existed: **27 of 27 cases carried duplicate act ids** (13-22 apiece) and
    every one of them duplicate Event ids. U2's design note calls this out as decision 6 and it is
    load-bearing exactly as stated.

    ⚠ **THE DRIVER DOES IT, AND THE ARGUMENT IS `make_chooser`'s OWN.** That docstring explains why
    a person is handed a minter rather than minting for themselves: *"§33 derives every id from the
    world seed and the tick … the barrier passes a minter closed over the seed and tick, which are
    THE CLOCK, NOT ANYBODY'S INTERIOR."* The round is part of that clock — a person cannot know
    which round it is and has no business knowing — so the term that names it is added at the
    barrier, by the one object that does know. The alternative, threading the round through
    thirty-one caller-built minters, would put a fact about the loop into every harness and test
    that builds one.

    ⚠ **ROUND 0 IS UNTOUCHED, WHICH IS WHAT KEEPS THE CONTROL A CONTROL.** `r == 0` returns
    immediately, so a one-round season mints byte-identical ids to the pre-tick loop and the
    `scene_budget = 1` arm reproduces its Event multiset exactly. Only a re-deliberation — the case
    that could not arise before — is qualified.

    ⚠ **RE-DERIVED, NOT RE-HASHED.** The new purpose is the original purpose plus `:r{n}`, so a
    reader can see what the id is of; hashing the previous id would have made it opaque.
    `04 PART D row 35` allows exactly this: `H(seed, tick, subject, purpose)`, *no counter, no
    service*, with `purpose` uniqueness a CONVENTION — and the round is what makes this one
    unique."""
    if r == 0:
        return
    for sc in scenes:
        for a in sc.acts:
            a.id = H(w.world_seed, w.tick, a.actor,
                     f"act:{a.verb}:{_subject_of(a)}:r{r}")
        sc.id = H(w.world_seed, w.tick, sc.actor, f"scene:{sc.id}:r{r}")


def _inputs_fingerprint(p: Person, qs: list, s: Sensation) -> tuple:
    """`U2` / `R-03`: EVERYTHING A PERSON'S DELIBERATION READS, AS ONE COMPARABLE VALUE.

    The scene tick re-enters DELIBERATE `scene_budget` times a season. A person whose inputs have
    not moved since their last deliberation would re-derive THE IDENTICAL candidate set — that is
    a property of `opening_set` being a pure function of these terms, not an optimisation — so the
    driver releases the next of what they already chose instead. This is the predicate for
    *"unmoved"*, and the unit is only as sound as this list is complete.

    ⚠ **ENUMERATED FROM THE READERS, NOT FROM MEMORY, AND EACH TERM NAMES THE ONE IT COVERS.**
    U2's design note calls the enumeration *a CONSTRUCTION, not a theorem*: what is provable is the
    converse — with these equal, `opening_set` is identical by construction. That the list is
    COMPLETE is a claim about the code as it stands, and U2's falsifier (b) is what tests it.

      * `q_ids`      — `questions_for`'s whole output. Covers Q1 (`w.dates` / `w.docket`), Q2 (a
                       claim LANDING, which is why it is computed with `since`), Q3 (`w.crossings`
                       and `Query.presence`) and Q4 (a live `commit` to an OUGHT). A world-level
                       change that cannot reach this person cannot move this term, which is what
                       keeps the skip from degenerating into "anything happened anywhere".
      * `subsistence` — `sense`'s first scalar, and `urgency(s.subsistence, fx)` is a term of the
                       chooser's score. ⚠ `standing` IS DELIBERATELY ABSENT: `Sensation.standing`
                       RAISES where the design fails to supply it (§18.2), and a fingerprint that
                       raises would make the skip a second failure mode rather than a decision.
      * `tenures`    — `person_side_eligible` reads them (eligibility `own`), `budget` counts the
                       live `hold`s, and `questions_for`'s `mine` set is built from them.
                       ⚠ `live` AND NOT `until`: a tenure CLOSING is the change that matters, and
                       `until` is `None` on every live edge — sorting a mixed `None`/`int` column
                       raises `TypeError`, which this first did. `live` is the property the three
                       readers actually test, and it is totally ordered.
      * `ledger`     — but ONLY the claims in the `requires` GRAMMAR VOCABULARY, which is the
                       whole of what `belief_contradicts` can read (§F1 clause 4; the same
                       `REQUIRES_STEMS` predicate `test_wb_the_control_arm_…` measures the channel
                       with). `(id, value, confidence)` because such a claim can arrive, be
                       overturned, or DECAY, and the third is what `claim.decayed` moves.
                       ⚠⚠ **THE WHOLE LEDGER WAS THE FIRST WRITING AND IT BROKE THE UNIT.** Every
                       WITNESS deposits into everyone's ledger, so a whole-ledger term moved every
                       round for everybody: every person's queue was invalidated every round, every
                       person re-deliberated from the top of a freshly-derived ranking, and a
                       season became ONE PERSON DOING THEIR TOP ACT FIVE TIMES. Measured at
                       `build_world(0)`, 2 seasons: `create_record` x10, `reconstruct` x9,
                       `research` x7, `move` x2, **all by `p_carin`**, with `examine`, `interview`,
                       `speak`, `tell`, `transfer`, `work` and `release` gone entirely. The
                       one-pass loop consumed a ranking POSITIONALLY, which did this work
                       implicitly; restarting at the top each round undoes it. Narrowing the term
                       to the vocabulary that can actually suppress a candidate is what makes the
                       queue survive a season, and it is narrower BECAUSE IT IS READ OFF THE
                       READER rather than guessed at.
      * `body` / `travel_leg` — `budget`'s condition and distance penalties. A person wounded in round 1
                       has fewer scenes in round 2, and that must re-open their triage rather than
                       silently shrink a queue they chose against a larger number.

    ⚠ WHAT IS NOT HERE, AND WHY THAT IS SAFE: `w.fixtures` is constant within a season (the sweep
    arms are chosen at `build_world`), and `self.round` is not an input to any of the five readers
    — a person's options do not depend on which round it is, only on what has happened."""
    return (
        tuple(q.id for q in qs),
        s.subsistence,
        tuple(sorted((t.id, t.kind, t.object, t.live) for t in p.tenures)),
        tuple((c.id, c.value, c.confidence) for c in p.ledger
              if str(c.predicate).partition(":")[0] in REQUIRES_STEMS),
        p.body,
        tuple(p.travel_leg),
    )


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
