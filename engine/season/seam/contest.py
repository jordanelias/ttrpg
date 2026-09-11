"""`seam/contest.py` -- `04_CODE_ARCHITECTURE.md` §A.2's `seam/contest` row: *"Dispatches;
enforces `max_depth`; returns Events + degree, or a typed refusal."*

`contest()` itself, the manifest-shaped provider lookup `contest_subsystem()`, the typed
`ContestError`, and `Resolution` -- what the seam returned as the fold sees it.

The degree side lives in `seam/ladder.py` and this module calls into it; the dependency is
one-directional by construction, because §A.2 gives the ladder its own row (*"nothing.
`degree(margin, veto?) -> Degree`"*) and a seam that graded its own result would be the second
resolver `S27.2` names as its highest-value refusal.

Moved whole from the flat `seam.py` by unit L2 of
`workplans/2026-09-09-layer1-conformance-plan.md`; `seam/` is a directory on §A.2's nine-module
list (`04:135`) and was shipped as a file at step 8 (ED-IN-0206).
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Optional
from ..gaps import Forbidden, Unspecified
from ..manifest import resolve as manifest_resolve
from ..state.world import World
from ..trace_log import TRACE


class ContestError:
    """S39.3/S53 -- GDScript HAS NO EXCEPTIONS and exceeding recursion depth is a CRASH, so the
    cap must produce a TYPED ERROR RESULT, CHECKED BY THE CALLER. Rev 1 returned `[]`, which is
    indistinguishable from a lawful no-event contest. This type is distinguishable."""

    def __init__(self, reason: str, depth: int, max_depth: int):
        self.reason, self.depth, self.max_depth = reason, depth, max_depth

    def __repr__(self) -> str:
        return f"ContestError({self.reason!r}, depth={self.depth}, max_depth={self.max_depth})"




# ===========================================================================
# S39 -- THE SEAM
# ===========================================================================

def contest_subsystem(prize: Any) -> Optional[dict]:
    """Which subsystem owns a contest for this prize.

    ⚠ **THE CROSSING MOVED TO `manifest/` AT UNIT L4 (ED-IN-0206) AND THIS IS NOW THE SEAM ASKING
    IT.** `04 §C.5`'s pseudocode spells the call the seam makes as
    `provider = manifest.resolve("contest", prizes[prize])`, and §A.2:136 gives role->provider rows
    their own module; the `rosters.yaml` x `module_contracts.yaml` crossing sat here, resolved at
    FIRST CALL rather than at boot. Behaviour is unchanged for every caller: `None` for a prize no
    roster row claims -- a real answer, not a failure, leaving the generic refusal below intact --
    and a raise for a row naming a module no contract declares.

    The wrapper is kept rather than inlined at the call sites because the seam's own vocabulary is
    *"which subsystem owns a contest for this prize"*, and `resolve`'s is *"role, key"*."""
    return manifest_resolve("contest", prize)


@dataclass
class Resolution:
    """WHAT THE SEAM RETURNED, AS THE FOLD SEES IT. `None` for an uncontested verb, and that is
    the whole of the uncontested path's change: `writes_at(None)`/`emits_at(None)` on a verb with
    no degree map return the flat tuples they always did.

    Two fields and no third. `degree` is the token `verb_table.yaml` keys on; `result` is the
    subsystem's own return, kept whole so an effect can read a quantity the SCENE computed rather
    than one this file made up."""
    degree: str
    result: dict


def contest(w: World, rung: str, prize: Any, claimants: list[str],
            depth: int, max_depth: int, causes: list[str],
            extension: Optional[Callable[[str], bool]] = None,
            *, verb: str = "", subject: Optional[str] = None,
            rng: Optional[Any] = None):
    """S39. EVERY ARGUMENT IS LOAD-BEARING. Attaches at EXACTLY ONE PLACE -- RESOLVE.

    ⚠ `U1` ADDED THREE KEYWORD-ONLY PARAMETERS AND CHANGED NO EXISTING CALL. `verb` and `subject`
    are what a provider needs to derive a pool and an obstacle from the act rather than from the
    prize; `rng` is the generator `04 §C.12`'s rejection 4 requires the DRIVER to construct — *"its
    generator must be constructed by the driver from the run seed and passed down exactly as
    `World` is"* — which that rejection records as *"the one rejection that is not yet
    load-bearing, because no roll exists yet."* It exists now. All three default, so a caller that
    does not contest passes nothing and reads as it always did.

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
    # ⚠ A CONTEST IS A DISPATCH TO A SUBSYSTEM, NOT A GENERIC ROLL. Jordan, 2026-09-02: *"a
    # contest seems like it can be a call for a different subsystem like personal combat, mass
    # battle or social contest."* All three ARE BUILT -- `references/module_contracts.yaml` gives
    # each a doc, a sim module and a declared resolver (`d_sigma` for personal combat, `dice_pool`
    # for the other two). So this seam was never missing a degree ladder it had to invent; it was
    # failing to CALL the engine that owns the prize.
    #
    # Wiring those engines is out of this chain's scope (Jordan ruled only this proposal chain is
    # in scope), so the refusal below NAMES the subsystem and its resolver instead of reporting one
    # undifferentiated hole. That turns "the degree ladder's margin model is absent" -- which reads
    # as a missing design -- into "this act belongs to `personal_combat`, whose resolver is
    # `d_sigma`, and nothing connects them", which is a wiring statement somebody can act on.
    if depth >= max_depth:
        TRACE.decision("contest depth cap reached", "S39.3",
                       chose="typed error result returned to the caller",
                       alternatives=["recurse (a CRASH in GDScript, not a catchable error)"])
        return ContestError("max_depth reached", depth, max_depth)
    # ⚠ THE DISPATCH RUNS **AFTER** THE DEPTH CHECK, AND IT DID NOT. Raising here first made
    # `ContestError("max_depth reached")` UNREACHABLE for every prize the roster claims — so
    # `H-87`'s registered cap was a number no branch could read and its three-point sweep was a
    # set of arms identical by construction. Found by the governance-slice adversarial pass.
    # ⚠ AND THE FIX IS A MOVE, NOT A SECOND CHECK. My first attempt added a duplicate cap test
    # twelve lines above this one — §8 broken in the act of fixing an ordering bug.
    _sub = contest_subsystem(prize)
    if _sub is not None:
        # ⚠ THE SEAM CALLS NOW. Jordan, 2026-09-02: *"kill / wound points towards a seam that
        # should be calling in the personal combat system."* This block used to resolve the
        # subsystem by name and then REFUSE — a pointer, not a call — on a scope note that ruling
        # overrides. The wrappers are the IN-side, built on `engine/cross_scale/combat_bridge.py`'s
        # precedent rather than a new pattern.
        #
        # ⚠⚠ **`U1` DELETED `if _sub["module"] == "personal_combat":` AND ED-SC-0033 RULES EXACTLY
        # THAT**, in these words: *"(1) the seam dispatches by manifest ROW rather than the
        # hardcoded personal_combat literal"*. A literal here is a SECOND REGISTRY, and it disagrees
        # with the first the day a row moves — the failure `04:1031`'s *"a misspelled manifest row
        # fails at boot naming the row"* exists to make impossible, surviving in the half that was
        # still a branch. `manifest.call` returns the provider a module registered with
        # `@provider(role, module)`, or `None`.
        # ⚠ **`None` IS A REAL ANSWER AND IS WHY THIS IS BYTE-INVARIANT TODAY.** `mass_battle` and
        # `social_contest` name modules nothing has registered, so they fall through to the refusal
        # below exactly as they did under the literal — the seam names the subsystem and its
        # resolver rather than reporting one undifferentiated hole. `proposals/…/08_SEAM.md` PART B
        # is titled *THE MANIFEST ROW, AND WHY THIS DESIGN REFUSES THE `if`-BRANCH* and registers
        # the `if` as a shim; this is the shim coming out.
        from ..manifest import call as _provider_for
        # ⚠ THE `provider:` FIELD, NOT THE `module:`. A prize names WHOSE contest it is and,
        # separately, WHAT RUNS IT — `a standing` belongs to `social_contest` and is rolled by
        # `sigma_leverage` until the proceedings subsystem lands (ED-SC-0033 clause 2,
        # `interim: true`). Looking the callable up by `module:` would make the interim resolver
        # unreachable and the repoint a code change.
        _run = _provider_for("contest", _sub.get("provider"))
        if _run is not None:
            out = _run(w, claimants, causes, prize, verb=verb, subject=subject, rng=rng)
            if out.get("status") == "RESOLVED":
                TRACE.decision(f"contest for {prize!r} dispatched", "S39",
                               chose=f"called {out['module']} (resolver {out['resolver']})",
                               alternatives=["invent a degree ladder in the seam (S27.2: the "
                                             "second resolver)"])
                return out
            # A gap in the CALL is named as a gap in the call, never as a missing design.
            raise Unspecified(
                f"a contest for {prize!r} routes to `{out['module']}` and the call did not "
                f"complete: {out.get('why')}", "S39",
                needs=out.get("status"),
                law="the seam DISPATCHES (Jordan 2026-09-02). A party the seam cannot derive is "
                    "a gap in the derivation, not a hole in the subsystem, and `combat_bridge` "
                    "sets the rule: return the gap, never fabricate a side")
        raise Unspecified(
            f"a contest for {prize!r} belongs to the `{_sub['module']}` subsystem "
            f"(resolver: {_sub['resolver']}), and nothing connects the seam to it", "S39",
            needs=f"the seam to call {_sub['module']} ({_sub['doc']})",
            law="Jordan 2026-09-02 -- a contest is a call for a different subsystem. The three "
                "are declared in references/module_contracts.yaml WITH resolvers, so the seam's "
                "job is to DISPATCH; inventing a degree ladder here would be a second resolver, "
                "which S27.2 names as its highest-value refusal. `personal_combat` is CALLED "
                "above; mass_battle and social_contest still resolve to a name only")
    raise Unspecified(
        "the degree ladder's margin model",
        "S39.4",
        needs="a margin -- pool, obstacle, and the four band edges read off it",
        law="S39.4 -- ONE degree ladder for every scale, FOUR BANDS READ OFF THE MARGIN, never off the obstacle's size. No in-chain document supplies the margin model, and S27.2 refuses a second resolver, an auto-resolve formula and a fast path -- so a band computed here without a margin IS the second resolver",
    )
