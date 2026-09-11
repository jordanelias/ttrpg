"""`decision/` -- the `choose` member of `04_CODE_ARCHITECTURE.md` §A.2:133.

`make_chooser` and everything it resolves by BARE NAME: `align` (which reads `ALIGNMENT`),
`stance_toward`, `urgency`, and `pack_scenes` (with `_payload_of`).

⚠ **THE BARE-NAME CLUSTER IS WHY THESE FOUR ARE ONE FILE, AND IT IS NOT A STYLE CHOICE.** Three
names in the old `decision.py` are read bare inside a body and rebound from OUTSIDE as module
attributes -- `ALIGNMENT` (by `align`), `pack_scenes` (by `make_chooser`) and `belief_contradicts`
(by `opening_set`, which is why that one lives in `options.py`). A bare name resolves in ITS OWN
module's globals, so a rebind reaches it only if it targets the module the reader lives in. Split
`align` from `make_chooser` and `PS.pack_scenes = spy` in the degree-sweep arms becomes a NO-OP
that reports every branch identical -- a fabricated null, which `CLAUDE.md` §0.1 pt 4 calls the
worse of the two directions. The rebind sites name `decision.choose` and `decision.options`
directly for this reason; see `__init__.py`.

⚠ **`ALIGNMENT` AND `belief_contradicts` ARE NOT RE-EXPORTED FROM `__init__.py`** -- step 8's
`_LADDER` lesson: a rebound value re-exported is a stale snapshot, and a reader who rebinds the
package attribute would silently miss the reader.

AX-2 binds every file under `decision/`: no `World`, as an import, a name, an attribute or a
string. Enforced BY PATH over this directory (`04:1046`).
"""

from __future__ import annotations

import math as _math
from typing import Any, Callable, Optional
from ..data.rosters import CONVICTION_AXES, SCENE_PACKING_RULES
from ..data.verbs import (ALIGNMENT, ALIGNMENT_DEFAULT_CELL, CONVICTION_PROJECTION,
                         PROJECTION_DEFAULT_CELL)
from ..gaps import Unspecified
from ..state.carriers import Act, Candidate, Person, Question, Scene, Sensation, View
from .options import opening_set


def align(verb: str, axis: str) -> float:
    """§F2's `alignment(c.verb, axis)`. Sparse: an unlisted pair reads the table's own declared
    `default_cell`, never a literal here."""
    return float(ALIGNMENT.get(axis, {}).get(verb, ALIGNMENT_DEFAULT_CELL))


def project(p: Person) -> dict:
    """A person's thirteen conviction weights, in the four-axis basis. `U3` / R-06a.

    ⚠⚠ **§F2's `conviction[axis]` IS COMPUTED NOW, NOT LOOKED UP, AND THE FORMULA IS UNCHANGED IN
    SHAPE.** V2 §F2 spells `score(c) = Σ_axis conviction[axis] · alignment(c.verb, axis)` and that
    indexing only works if a person's convictions are KEYED BY AXIS — which is what
    `conviction_axes` used to be forced to be, holding `Precedent` (a conviction) beside
    `self_preservation`, `suspicion` and `harm_borne` (three ad-hoc scalars) so the lookup had
    something to hit. `conviction_axes`'s own note named the conflation and predicted the repair.
    So:

        conviction[axis]  :=  Σ_conv  p.convictions[conv] · projection[conv][axis]

    and `Σ_axis` above is untouched. A person holds weights over the THIRTEEN; the projection is
    the only thing that knows about axes.

    ⚠ **THE MATRIX IS READ, NOT INVENTED** — `conviction_axis_matrix_v30.md` §2, with a per-cell
    rationale in its §3. That is the difference between this table and `alignment`, whose own note
    says of its cells *"a reason is not a citation"*. They multiply together, so which of the two
    is argued and which is cited is worth being able to see.

    ⚠ **A CONVICTION THE MATRIX DOES NOT LIST PROJECTS TO NOTHING, AND THAT IS THE SPARSE DEFAULT
    RATHER THAN A SILENT DROP.** `PROJECTION_DEFAULT_CELL` is the declared 0.0; the loader has
    already refused any conviction name outside the roster, so an unlisted pair here is a cell the
    data chose to leave sparse, not a typo that got through."""
    out = {ax: 0.0 for ax in CONVICTION_AXES}
    for conv, w in (p.convictions or {}).items():
        row = CONVICTION_PROJECTION.get(conv)
        if row is None:
            continue
        for ax in CONVICTION_AXES:
            out[ax] += float(w) * float(row.get(ax, PROJECTION_DEFAULT_CELL))
    return out


def stance_toward(p: Person, referent: str) -> float:
    """§F2's second term, from `p`'s OWN stance rows. #353 `:333`: `(referent, valence -5..+5,
    weight 0..5)`. Valence times weight, summed over the rows naming this referent -- weight is
    what `:333` supplies it for, and dropping it would make a 5-weight conviction and a 0-weight
    one count alike."""
    total = 0.0
    for row in p.stance:
        if len(row) >= 3 and row[0] == referent:
            total += float(row[1]) * float(row[2])
    return total


def urgency(subsistence: int, fx: "Fixtures") -> float:
    """§F2's third term. NO IN-CHAIN FORMULA -- `H-73`, `assumption`, swept.

    ⚠ AND IT CANNOT CHANGE ANY DECISION, WHICH IS A DEFECT IN §F2 RATHER THAN IN THIS FUNCTION.
    §F2's score is

        score(c) = SIGMA_axis conviction[axis] * alignment(c.verb, axis)
                 + stance_toward(c.subject)
                 + urgency(sensation.subsistence)

    and the third term HAS NO `c` IN IT. It is added identically to every candidate, so it cannot
    move the ranking, cannot change which candidates survive `ask_budget()`, and cannot change the
    order they are returned in. `choose` returns "the top ask_budget() candidates, ORDERED by
    score", so a term constant across candidates is INERT BY CONSTRUCTION -- it is the dead-carrier
    shape #353 `:739-744` names, arriving in the scoring function instead of in a field.

    Kept and computed anyway, faithfully, because deleting it would hide the finding: the sweep
    (`H-73`) reports that NO verdict moves across three urgency scales, and that null result IS
    the measurement. `test_w5_f2_third_term_is_inert` is the falsifier."""
    return float(subsistence) / float(fx.get("condition_scale"))


def _sample_order(ranked: list, score, p: Person, fx: "Fixtures", draw) -> list:
    """`U4` / `H-96`: the triage stops being decided by the SPELLING of a verb.

    THE DEFECT, MEASURED WITH A CONTROL (2026-09-10). `H-96` records that only a handful of
    candidates carry a nonzero conviction score and that the triage is *"decided, for most
    candidates, BY ALPHABETICAL ORDER OF THE VERB'S NAME"* (`hole_register.yaml`, H-96's `hole:`).
    ⚠ THE SHORTER PHRASING *"the rest TIE and are ordered alphabetically by verb name"* IS NOT
    H-96's and was attributed to it in the first writing of this docstring — it is
    `requirements.yaml`'s R-08 and this plan's own §6. A paraphrase inside quotation marks, pointed
    at the wrong row; corrected rather than dropped, because mis-sourcing a quote is the recurring
    defect this lane's §14 names.

    WHAT THE DEFECT COST, measured by adding one ruled verb (`release`, `04 §A.3` row 14) and then
    running the SAME verb, predicate and effect again under a name that sorts last: the
    early-sorting name executed in **18** corpus cases and displaced 71 acts (`utter` ×56); the
    late-sorting one executed in **5** and displaced **2**. Same mechanism, same world, same seed —
    only the letters differed. ⚠ **THAT PAIR WAS MEASURED IN-SESSION AND IS NOT REPRODUCIBLE FROM
    THIS TREE**, because `release` is not in `verb_table.yaml`: it is a separate unit, held behind
    this one. To re-run it, add the verb and diff the corpus's executed sets against a rename of it.
    Said plainly rather than left to read as a standing artifact (§0.1 pt 3). A design in which adding a correct verb makes the world
    do LESS, because of where its name falls in the alphabet, has its triage in the wrong place.

    THE FIX IS PLACKETT-LUCE VIA GUMBEL, and it is one line of arithmetic for a reason. Adding
    `-log(-log(u))` to `score/tau` and sorting descending samples an ORDER without replacement
    whose probabilities are `softmax(score/tau)` — so this generalises the old ranking rather than
    replacing it: as `tau -> 0` the score term dominates and the order converges on the score
    order, with the residual ties broken by the DRAW instead of by the alphabet. An ORDER is what
    is needed, not a pick: `pack_scenes` takes the ranked list and slices it by budget, so a
    chooser that sampled a single winner would leave the rest of the triage alphabetical.

    ⚠ `tau == 0` SHORT-CIRCUITS TO THE OLD PATH, AND THE ARM VALIDATES THE PLUMBING RATHER THAN
    THE SAMPLER. The zero-temperature limit of a softmax over TIED scores is uniform over the tied
    set, not the alphabetical order — so byte-identity at `tau = 0` needs this discontinuous case,
    and that case then exercises the OLD code. Stated plainly because both prior plans named the
    `tau = 0` arm as the sampler's control and neither noticed: it controls that the draw is
    threaded, the signature is unchanged and nothing else moved. The sampler's own falsifier is
    the rename control above, re-run.

    ⚠ NO SILENT FALLBACK. A missing `draw` at `tau > 0` RAISES rather than quietly returning the
    alphabetical order: that would be S42.2.1's *"a silent default does not fail; it answers,
    plausibly and wrongly, forever"* — and it would answer with the exact defect this exists to
    remove, while every instrument reported the sampler as live.

    ⚠⚠ **A SECOND CLAUSE IS NOT MET: THE DRAW IS NOT CONSTRUCTED BY THE DRIVER.** `U4` lists
    `loop/driver.py` as the file that *"constructs and passes `draw`"*, and `04:861-862` says of an
    RNG *"its generator must be constructed by the driver from the run seed and passed down exactly
    as `World` is"*. It is instead built at every CALL SITE (`harness/headless.py`,
    `harness/corpus_run.py` x2, `harness/probes.py` x2, the degree-sweep arms, and the tests).
    **The structural reason: the driver never constructs the chooser.** `SeasonDriver.season(choose,
    ...)` RECEIVES an already-built one, so the only way the driver could own the draw is to hand it
    to `choose` — and `choose`'s four-parameter signature is pinned as a source string by
    `test_choose_receives_no_world`, which `U4` itself insists must not change. The two clauses of
    the spec are in tension and this took the one that a test enforces.
    ⚠ SCOPE, STATED SO IT IS NOT OVERREAD: `04:858-860` scopes that sentence to **R-09's** producer
    (*"chains of events within a scene are probabilistic"*), which is unbuilt; this is R-08's
    chooser. But `04:862-863` gives its reason as *"so the roll is not built the idiomatic way first
    and retrofitted after"*, which is exactly the hazard here, and `U4`'s file list asked for the
    driver independently of `04`. **Whether a driver-owned generator is required before R-09's roll
    lands is the one question in this unit a ruling could change.**

    ⚠ **ONE CLAUSE OF THE UNIT'S SPEC IS NOT MET, AND IT IS DECLARED RATHER THAN QUIETLY DROPPED.**
    `U4` says *"the draw `purpose` includes the round (U2)"*. The purpose is instead
    `choice:<verb>:<subject>`, seeded per `(world_seed, tick, person)` by the factory.
    ⚠⚠ **THE REASON THIS PARAGRAPH GIVES FOR THAT IS NOT THE ONE IT GAVE FIRST, AND THE FIRST ONE
    IS NOW FALSE.** It read *"U2 is unbuilt — `SeasonDriver.season` still runs DELIBERATE once per
    season, so there is no round index to include"*, and closed by requiring `U2` to add the round
    *"in the same commit that adds rounds, or the second round is a replay of the first"*. `U2`
    landed 2026-09-11: `season()` runs DELIBERATE `scene_budget` times, `SeasonDriver.round` is the
    index, and `_qualify_by_round` already re-derives act and scene ids through it. The clause is
    still unmet, for two reasons that replace the stale one, and NEITHER is "there is no round".

    **(1) STRUCTURAL — THE ROUND CANNOT REACH THIS FUNCTION, AND IT IS THE SAME TENSION AS CLAUSE
    2 ABOVE.** The round is state on the DRIVER; the chooser is built by the CALLER (clause 2's
    finding), so the driver cannot key a draw it never constructs. The only other route is to hand
    `choose` the round, and `choose`'s four-parameter signature is pinned as a source string by
    `test_choose_receives_no_world`, which `U4` insists must not change. A caller holding both CAN
    close over `d.round` when it builds the draw, which is exactly how the arm below was measured —
    but that is a harness reaching past the engine, not the engine meeting the clause.

    **(2) DESIGN — IT CONTRADICTS THE KEYED-NOISE PROPERTY THIS FUNCTION IS BUILT ON**, one axis
    along from the defect the `⚠⚠` block below records recovering from. The round makes a
    candidate's noise a property of WHEN IT WAS REACHED; the whole argument for keying on
    `(verb, subject)` is that it must be a property OF THAT CANDIDATE, so that two arms of an
    experiment differ by what differed and not by a reshuffle. Under a scene tick a candidate that
    lost round 0 keeps its margin in rounds 1..4, which is a person whose TASTE is stable across a
    season while their OPTIONS move — and the options do move: what they have already realised is
    removed by `_drop_what_was_already_done`, so the later rounds are them continuing down the list,
    never repeating it. MEASURED, `build_world(0)`, 2 seasons, tick 1: `p_carin`'s round-2 ranking
    is `research · reconstruct · create_record · move · work · release · examine`, round 3 is the
    same order minus `research`, round 4 the same minus `release · examine`. The "replay" the stale
    sentence feared does not occur; what occurs is continuation, which is what R-03 asked for.

    ⚠ **AND THE CLAUSE IS NOT INERT, WHICH IS WHY THIS IS A DECISION AND NOT A SHRUG.** Arm: wrap
    the caller's draw as `orig(pid, f"{purpose}:r{d.round}")`. `build_world(0)`, 2 seasons, against
    the shipped arm: events 113 -> 114, `release.refused` 0 -> 1, `finding.none` 3 -> 4,
    `claim.deposited` 62 -> 63, `travel.blocked` 3 -> 1, content hash `7d64c569..` -> `8886d0aa..`;
    acts 20 in both. So a reader may not conclude from "unmet" that it would change nothing.
    TAKEN UNDER `CLAUDE.md` §0's fifth step — 1..4 are silent, one option is clearly right for the
    code — rather than escalated: reasons (1) and (2) point the same way and no ruling overwrites a
    design call whose two defensible options are "unreachable" and "self-contradicting".
    ⚠ AND THE ADJACENT PRIMITIVE IS NAMED RATHER THAN IGNORED: the tree already owns a per-tick
    draw ordinal, `state/world.py::World.new_draw` (*"`S33`'s draw ordinal. Reset at the start of
    every tick by `season()`"*), and `harness/probes.py`'s own header argues the general case — *"A
    CONTENT-DERIVED draw was the second attempt and it collides whenever two draws in one tick are
    alike."* It is NOT used here for two reasons, both structural: it is a method on `World`, which
    `AX-2` bars from `decision/` by path (`04:1046`), and an ORDINAL would destroy the
    candidate-keyed replay this function depends on — the noise must be a property of the candidate,
    not of the order it was reached in. Recorded here because a declaration that a mechanism is
    missing, made without naming the adjacent one, is the defect this lane keeps finding."""
    tau = float(fx.get("choice_temperature"))
    if tau == 0 or len(ranked) < 2:
        return ranked
    if draw is None:
        raise Unspecified(
            "the choice draw", "H-96",
            needs=f"`make_chooser(fx, mint, verbs, draw)` with a draw at choice_temperature={tau}",
            law="U4/H-96 -- at a nonzero temperature the order is SAMPLED, and a chooser built "
                "without a draw would silently fall back to the alphabetical tie-break this "
                "replaces, reporting a sampler that is not running")
    keyed = []
    for c in ranked:
        # ⚠⚠ THE NOISE IS KEYED BY THE CANDIDATE, NOT DRAWN IN LIST ORDER, AND THE DIFFERENCE IS
        # WHAT MAKES A FORK ATTRIBUTABLE. The first version took ONE stream per person and consumed
        # it down `ranked` — so adding, removing or reordering a single candidate shifted the
        # noise-to-candidate assignment WHOLESALE, and every downstream difference between two arms
        # of an experiment was the reshuffle rather than the thing under test. `W-D` measures
        # exactly that: whether a forked decision changes a LATER one. With a positional stream the
        # fork's own signal is swamped by its side effect on the draw, and the control arm's
        # residual channel read 0 where it had read 2. Keying on `(verb, subject)` makes a
        # candidate's noise a property OF THAT CANDIDATE: identical candidates get identical draws
        # in both arms, so what differs between them is what actually differed.
        # ⚠ It is also the only form in which the `tau = 0` control means anything, because it is
        # the only form where a candidate's treatment does not depend on its neighbours.
        # ⚠ ONE STREAM PER CANDIDATE, AND THE RETRY ADVANCES IT. The first version re-called
        # `draw(...)` inside the loop with a CONSTANT purpose, which re-seeds an identical
        # `Random` and returns the identical value — an infinite loop wearing a retry's clothes,
        # on the one input (`u == 0.0`) the loop exists to handle. Found by this unit's own
        # adversarial pass rather than in play, because `random()` returns exactly 0.0 about
        # once in 2^53 draws: a guard that cannot do its job is not a weak guard but an absent
        # one (`CLAUDE.md` §0.1 pt 2), and a hang is the worst shape for one.
        rng = draw(p.id, f"choice:{c.verb}:{c.subject or '-'}")
        u = rng.random()
        while u <= 0.0:                   # `random()` is [0,1); log(0) is the one unusable draw
            u = rng.random()              # SAME stream, so it advances and can terminate
        g = -_math.log(-_math.log(u))
        # the trailing two terms are a STABLE TOTAL ORDER for exact float ties, which continuous
        # noise makes measure-zero; they are not the tie-break -- `g` is.
        keyed.append((-(score(c) / tau + g), c.verb, c.subject or "", c))
    keyed.sort(key=lambda t: t[:3])
    return [t[3] for t in keyed]


def make_chooser(fx: "Fixtures", mint: Callable[[str, str, str], str],
                 verbs: Optional[frozenset] = None,
                 draw: Optional[Callable[[str, str], Any]] = None) -> Callable[..., list[Act]]:
    """§F2's decision policy as a FACTORY, so `choose(p, view, sensation, ask_budget)` keeps the
    FOUR-parameter signature §26 states while still reaching its params.

    `H-03` is the row: "grade: assumption. THE SHAPE IS RULED (§3 L1, §9, §26); only the weighting
    is open", so §G's discipline applies to the weights and not to this structure.

    Four properties, and each is checked by a test rather than asserted here:
      1. EVERY INPUT IS PERSON-SIDE -- `convictions`, `stance`, the View, the two Sensation
         scalars. No World, no resolver-side Query. L2 by parameter list.
      2. It CONSUMES `convictions` and `stance`, which #353 declares as fields and no formula in
         the chain reads -- a carrier nothing consumes is dead state (§22.1's own complaint).
      3. THE PERSON TRIAGES. `ask_budget()` is asked, not imposed; the engine never truncates.
      4. A lookup on one's own interior is indistinguishable from a deliberation at this
         boundary, and the design does not claim otherwise (§F2 property 4).

    ⚠ `mint` IS HERE BECAUSE §F2 TYPES `choose -> Act[]` AND GIVES THE PERSON NO WAY TO MINT ONE.
    An `Act` needs an id, and §33 derives every id from the world seed and the tick -- "unique per
    DRAW, not per operation" -- so a person-side function cannot produce one. That is a real gap
    between §F1's `-> Candidate[]` and §F2's `-> Act[]` and it is registered (`H-74`), not filled:
    the barrier passes a minter closed over the seed and tick, which are the CLOCK, not anybody's
    interior. Same shape as `fx`, and the AST proof still sees no `World`."""
    def choose(p: Person, v: View, s: Sensation, ask_budget) -> list[Act]:
        q = getattr(v, "question", None)
        if q is None:
            return []
        cands = opening_set(p, v, q, fx)
        if verbs is not None:
            cands = [c for c in cands if c.verb in verbs]
        u = urgency(s.subsistence, fx)
        # `U3`: the person's convictions are weights over the THIRTEEN, so they are projected
        # into the four-axis basis once per deliberation rather than looked up per candidate.
        # Hoisted out of `score` deliberately: it does not depend on `c`, and computing it inside
        # would run it once per candidate for an identical answer.
        axis_w = project(p)
        def score(c: Candidate) -> float:
            return (sum(axis_w[ax] * align(c.verb, ax) for ax in CONVICTION_AXES)
                    + stance_toward(p, c.subject or "")
                    + u)
        # ⚠ SCORED ONCE, NOT TWICE. `score` was passed to `_sample_order` and re-invoked there for
        # every candidate it had just been invoked for in this sort key — measured by a `/simplify`
        # profile as `align()` running 637,324 times for 78,858 candidates across a 143-case corpus
        # run, almost exactly 2x one pass. The scores are IDENTICAL either way (`score` is pure in
        # `c` given the closure), so this is the same ranking computed half as often, not a
        # different one.
        _scores = {id(c): score(c) for c in cands}
        ranked = sorted(cands, key=lambda c: (-_scores[id(c)], c.verb, c.subject or ""))
        # ⚠ KEYED ON `id(c)` AND THAT IS SAFE HERE, NARROWLY: `cands` holds every Candidate alive
        # for the whole of this call, so no id can be recycled underneath the dict. A Candidate is
        # not guaranteed hashable and `(verb, subject)` is not guaranteed unique, so neither is a
        # key this can use.
        ranked = _sample_order(ranked, lambda c: _scores[id(c)], p, fx, draw)
        # §26.3: the PERSON triages. The slice is the person's own choice of what to leave
        # undone, taken against a budget they ASKED for -- not an engine truncating a tail.
        # `W17`: the budgeted unit is the SCENE, so the slice is over scenes and each carries up
        # to `interactions_per_scene` of the ranked candidates. The default policy fills scenes
        # greedily in score order -- a person spends a scene on their best option and whatever
        # else it can carry, which is what "1-3 mechanical interactions" describes.
        # `U2`: `ask_budget()` is the person's SEASON REMAINDER, not one round's allowance. The
        # person chooses the whole of what they will do with the season they have left; the driver
        # releases `scenes_per_round` of it per round (`H-124`). Nothing is discarded, so S26.3's
        # *the engine never truncates* is untouched -- what the round bounds is WHEN a chosen scene
        # runs, not WHETHER.
        return pack_scenes(p, ranked, ask_budget(), fx, mint, occasion=q)
    return choose


def _payload_of(c: "Candidate") -> Optional[dict]:
    """WHAT A COMPUTED ACT CARRIES: its subject, and the operands its verb's cell names.

    ⚠ `subject` STAYS EVEN WHEN NO CELL BINDS IT, because it is not only an operand. `act_refs`
    reads it to say what an act NAMES, `claim_subjects` reads it to say what a deposit is ABOUT,
    and `tell` -- whose `writes:` is empty by design -- has nothing else that knows what was told.
    Dropping it for a verb whose requirement happens not to mention `subject` would break the
    causal graph for the one verb the corpus most relies on."""
    d = dict(c.operands or {})
    if c.subject:
        d.setdefault("subject", c.subject)
    return d or None


def pack_scenes(p: Person, ranked: list, n_scenes: int, fx: "Fixtures", mint,
                occasion: Optional["Question"] = None) -> list:
    """`H-78`: WHICH interactions share one scene. `H-76` says how many; this says which.

    ⚠ THIS WAS A COMMENT IN `make_chooser` UNTIL THE `W17` ADVERSARIAL PASS READ IT -- "the
    default policy fills scenes greedily in score order", with no row, no alternative and no
    sweep. That is `H-53`'s defect one level up, and `H-53`'s own row names the shape: the
    instrument answering a WHICH question the specification left open, inside a slice.

    `greedy` is that behaviour declared and kept as the control. `one_per_scene` is the pre-ruling
    accounting. `by_subject` groups the interactions that share a subject, which is what
    `player_agency_v30.md` §6.3's "one scene opportunity pursued" describes -- an opportunity is
    an opportunity to do something ABOUT something.

    ⚠ `n_scenes` IS A COST BUDGET AND NOT A SCENE COUNT, WHICH IS WHY `U2`'s ROUND BOUND IS NOT
    HERE. `take()` spends it, and an extended scene costs `extended_scene_cost` (2) against a
    plain one's 1. The scene tick bounds how many of a person's chosen scenes RUN in one round,
    and that is a scheduling fact the driver owns (`SeasonDriver.deliberate`, `H-124`) -- not a
    second bound on the person's triage. Putting it here as a count of 1 would make every extended
    chunk cost 2 > 1 and be trimmed to a single interaction, so no extended scene could form,
    `Scene.cost` would return 1 unconditionally, and `H-77`'s three-point sweep would go INERT --
    the exact shape that row records itself recovering from."""
    rule = fx.get("scene_packing_rule")
    if rule not in SCENE_PACKING_RULES:
        raise Unspecified(
            f"scene-packing rule {rule!r} is not in the roster", "H-78",
            needs=f"one of {sorted(SCENE_PACKING_RULES)}",
            law="H-78 -- nothing in the chain says WHICH interactions share a scene, so a rule "
                "outside the roster is a fourth answer nobody declared")
    per = fx.get("interactions_per_scene")
    width = 1 if rule == "one_per_scene" else (len(ranked) if per is None else per)

    def scene(n: int, chunk: list) -> "Scene":
        # ⚠ `occasion=` IS NOT DECORATION. `choose` already holds the question — it refuses to
        # produce anything without one — and dropping it here is what left the act with no route
        # back to what raised it (`N3`).
        return Scene(mint(p.id, "scene", str(n)), p.id,
                     # ⚠ THE CANDIDATE'S SUBJECT REACHES THE ACT, AND IT USED NOT TO. This read
                     # `Act(mint(...), p.id, c.verb)` — three arguments — so `opening_set`
                     # computed a subject from the question's referents, `mint` folded it into the
                     # act's ID, and the act itself carried NOTHING. `_req_tell` reads
                     # `payload["subject"]` and got `None`, so `tell` was attempted and refused in
                     # every world in the corpus; `_eff_tell` had no target either.
                     #
                     # ⚠ THAT WAS HALF OF `H-94` AND `W-C` CLOSED THE OTHER HALF. The
                     # Candidate carries `operands` now, derived person-side from the actor's own
                     # Tenures, the question's referent and two fixtures, so
                     # `stores(hearth(giver), kind) >= amount` has a `from`, a `kind` and an
                     # `amount` -- and the act CARRIES them, which is what makes the fold bind
                     # what the person bound. The subject is written first and the operands over
                     # it, so a cell that binds the referent under its own name (`to`, `site`)
                     # cannot disagree with `subject` about which thing that is.
                     [Act(mint(p.id, c.verb, c.subject or ""), p.id, c.verb,
                          payload=_payload_of(c)) for c in chunk],
                     # `H-77`: a scene carrying more than one interaction is the EXTENDED one.
                     # This is what `extended` MEANS, and until W17's adversarial pass nothing
                     # ever set it -- so `Scene.cost` returned 1 unconditionally, H-77's sweep
                     # could not move any verdict, and the row passed R2 while being
                     # unexecutable. That is the laundering R2 exists to stop, in the row that
                     # was added the same day the rule was written.
                     extended=len(chunk) > 1, occasion=occasion)

    # ⚠ THE BOUND IS THE COST, NOT THE SCENE COUNT, and getting that wrong made the DEFAULT
    # chooser overspend by construction: once `extended` was actually set, five greedy scenes
    # cost ten against a budget of five and every season using `make_chooser` refused itself.
    # Found by running the corpus after `H-77` stopped being inert -- the row and the packer are
    # the same mechanism seen from two sides, and fixing one without the other is what broke it.
    ext = fx.get("extended_scene_cost")

    def take(chunks) -> list:
        out, left = [], n_scenes
        for chunk in chunks:
            if left <= 0:
                break
            # An extension the person cannot afford is taken as a PLAIN scene rather than
            # skipped: they still pursue the opportunity, with less in it. Skipping would be the
            # engine deciding what they leave undone, which is L1.
            if len(chunk) > 1 and ext > left:
                chunk = chunk[:1]
            cost = ext if len(chunk) > 1 else 1
            out.append(scene(len(out), chunk))
            left -= cost
        return out

    if rule == "by_subject":
        seen: dict = {}
        for c in ranked:
            seen.setdefault(c.subject or "", []).append(c)
        chunks = [seen[subj][start:start + width]
                  for subj in sorted(seen)
                  for start in range(0, len(seen[subj]), width)]
    else:
        chunks = [ranked[i:i + width] for i in range(0, len(ranked), width)]
    return take(chunks)
