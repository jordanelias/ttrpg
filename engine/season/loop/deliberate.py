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
        v = decision.assemble(p, q_p, k_view)
        # S26.3: the PERSON asks their own budget. `choose` receives the QUERY, not the
        # answer -- rev 2 computed it in the engine and handed the number down, which is
        # the half of retraction 5 that never landed.
        ask_budget = lambda p=p, v=v: decision.budget(p, v, k_budget, w.fixtures)
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
