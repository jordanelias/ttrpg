"""`season.seam` -- S39, THE DISPATCH: which subsystem owns a contest, and what degree its answer
grades to. Extracted, step 8 of the decomposition (a PURE MOVE, ED-IN-0203).

WHAT MOVED HERE, as a pure line-slice of `shape.py` at HEAD `3e273d3d`: `ContestError`,
`contest_subsystem`, the S39.4 comment block that records why the degree has two sources and
neither is re-derived here, `_LADDER` / `_LADDER_ERROR`, `degree_ladder`, `ladder_error`,
`Resolution`, `combat_degree`, `degree_of`, and `contest` itself -- everything from
`contest_subsystem` to end-of-file was one contiguous span, so it moves as one slice rather than
several.

⚠ ONE LINE MOVED THAT THE DECOMPOSITION BRIEF DID NOT ENUMERATE, AND IT IS RECORDED HERE RATHER
THAN LEFT SILENT: the "`# S39 -- THE SEAM`" section-header comment immediately above
`contest_subsystem` moved with it. The brief's table starts at `contest_subsystem` itself; the
header describes exactly the block that follows it and nothing that stays in `shape.py`, and
leaving it behind would have orphaned a section title over the file's own closing blank lines. A
comment carries no runtime behaviour, so this does not touch the pure-move claim the AST/hash
falsifiers check -- it is a judgment call about where a piece of prose belongs, made explicit
rather than buried in a diff.

WHY THIS MODULE MAY NAME `World`, UNLIKE `decision.py`. `decision.py`'s AX-2 island forbids it --
a person-side function may not read other people's state. `contest()` is not person-side: it is
the SeasonDriver's own dispatch, called from inside `resolve()` with the World `resolve` already
holds, and S39 has always typed it that way. Moving it out of `shape.py` changes which file states
the rule; it does not change who may call it or what it may read.

THE REBIND HAZARD THIS MOVE MUST NOT TRIP, CLOSED HERE RATHER THAN DISCOVERED LATER. `global
_LADDER, _LADDER_ERROR` in `degree_ladder()` creates BOTH module bindings on first assignment --
`global` does not require them to pre-exist. A carve that moved `_LADDER` (and `degree_ladder`,
its only writer) here while leaving `_LADDER_ERROR` behind in `shape.py`'s facade would raise
NOTHING: `seam._LADDER_ERROR` would spring into existence as a second, silent home the moment a
real import failure ran `degree_ladder()`, while `shape._LADDER_ERROR` stayed the re-exported
`""` forever, read by anyone still asking the old name. `registers/handoffs/HANDOFF_IN.md`
demonstrates the shape of this on two throwaway modules before this step ever touched the real
one; the fix is not a second check, it is moving both names in the SAME commit, which is what the
facade below refuses to paper over by re-exporting either.

**THE FACADE RE-EXPORTS EVERY NAME ABOVE EXCEPT `_LADDER` AND `_LADDER_ERROR`.** A rebound module
global cannot be re-exported correctly through a `from .seam import _LADDER` binding in
`shape.py` -- that binding is a snapshot taken once, at import, and every later `global _LADDER =
...` inside `degree_ladder()` rebinds `seam`'s own namespace, never `shape`'s copy. The two
non-rebinding readers, `ladder_error()` and `degree_of()`, ARE re-exported and still work
correctly from `shape.py`, because a function is a single object regardless of which module holds
the name pointing at it: calling `shape.ladder_error()` still runs the same code, reading
`seam`'s own `_LADDER_ERROR` from inside `seam`'s own module globals. Only a caller that reads or
writes the raw module attribute -- `S._LADDER`, `S._LADDER_ERROR` -- needs to be re-pointed at
`seam._LADDER` / `seam._LADDER_ERROR` directly; `engine/season/tests/test_season_shape.py`'s
follow-the-owner arm is the one caller in this tree that does, and is re-pointed in this same
change.

`combat_seam.py` -- the IN-side of the personal-combat call this module's `contest()` dispatches
to -- does NOT move here and is not renamed; it stays at `engine/season/combat_seam.py`, unchanged
in location, per `PATH_SEAM_ALLOWED` in `tests/valoria/test_engine_does_not_import_systems.py`.
Two of its deferred `from . import shape as S` imports move to module level in this same change,
because their only reason for existing was the `combat_seam <-> shape` import cycle this move
dissolves: `body_band_penalty` now resolves from `.decision` directly (it moved there at step 7)
and `H` from `.state.ids` directly, so `combat_seam.py` no longer imports `shape` -- or, after this
step, `seam` -- at all.

Imported at the top of `shape.py` (`from . import seam` + a re-export block, everything but the
two excluded names) so every bare use further down that file keeps resolving, and so `S.<name>`
keeps resolving for the harness and tests -- a re-export, not a second definition, the same
convention every prior step in this decomposition follows.
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from typing import Any, Callable, Optional

from .data import files
from .data.rosters import FELLED, UNTOUCHED, WOUNDED, roster_map
from .gaps import Forbidden, Unspecified
from .state.world import World
from .trace_log import TRACE


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
    """Which subsystem owns a contest for this prize, from `rosters.yaml` crossed with
    `references/module_contracts.yaml`.

    Neither half is invented here: the PRIZE is what Part E's `contests:` column carries, and the
    SUBSYSTEM is a module the contracts file already declares with a doc and a resolver. Returns
    `None` for a prize no roster row claims -- which is a real answer, not a failure, and leaves
    the generic refusal below it intact."""
    name = roster_map("contest_subsystems", "prizes").get(str(prize))
    if name is None:
        return None
    import yaml as _y
    contracts = files.MODULE_CONTRACTS_YAML
    if not contracts.exists():
        return dict(module=name, resolver="unknown", doc="module_contracts.yaml not found")
    for m in (_y.safe_load(contracts.read_text()) or {}).get("modules") or []:
        if m.get("module") == name:
            # ⚠ THE PYTHON, NOT THE MARKDOWN. Jordan, 2026-09-02: *"we aren't using the .md or
            # anything for those systems. those are super outdated."* The contracts file carries
            # both a `doc:` (markdown) and a `sim_module:` (the live Python) for these three, and
            # the first version of this refusal printed the `doc:` — so it pointed a reader at a
            # file its owner calls superseded, which is the stale-pointer defect this chain keeps
            # finding in other people's work. `sim_module` first, and where the contract has none
            # the tree is asked directly rather than falling back to the markdown.
            where = m.get("sim_module") or ""
            if not where:
                guess = files.subsystem_sim_dir(name)
                where = (f"systems/{name}/sim/" if guess.is_dir()
                         else f"(no `sim_module:` in module_contracts.yaml; "
                              f"`doc:` is {m.get('doc')!r} and is out of date)")
            return dict(module=name, resolver=m.get("resolver") or "undeclared", doc=where)
    raise Unspecified(
        f"`contest_subsystems` maps {prize!r} to {name!r}, which is in no module contract", "S39",
        needs="a module named in references/module_contracts.yaml",
        law="the roster may only name a subsystem the contracts file declares -- otherwise the "
            "dispatch target is invented")


# ---------------------------------------------------------------------------
# S39.4 -- THE DEGREE. TWO SOURCES, BOTH ALREADY RULED, NEITHER RE-DERIVED HERE.
#
# ⚠ THIS BLOCK IS `W-E`, AND IT EXISTS BECAUSE A PARTIAL SUCCESS AND AN OVERWHELMING ONE WERE
# THE SAME EVENT. Three links were broken at once and each hid the next: `_fold` hardcoded
# `_degree_for_writes = None`; `emits_at` had ZERO callers anywhere in the tracer (`H-113`), so a
# contested verb reported the FLAT UNION of every band; and `Event.degree` was a field nothing
# ever assigned. Closing any one alone changes nothing observable.
#
# THE TWO SOURCES, AND WHY THIS FILE MAY NOT CHOOSE BETWEEN THEM:
#
#   1. THE LADDER, for a contest whose subsystem returns a MARGIN. `S39.4` -- one ladder for
#      every scale, four bands read off the margin -- and the tree OWNS it:
#      `engine/autoload/dice_engine.py::degree_from_net`, whose docstring reads *"THE degree
#      ladder. Single owner for every scale of the game (Jordan ruling, 2026-08-14)"*.
#      ⚠ IT IS IMPORTED AND CALLED, NOT MIRRORED. `S27.2` names a second resolver as its
#      highest-value refusal, and a band table copied into this file WOULD BE ONE -- it would go
#      on answering after the owner changed its mind, which is exactly what happened to
#      `params_tables.yaml`'s captured ladder (`CLAUDE.md` §5: the capture still shows the
#      PRE-RULING bands). The falsifier that this is a call and not a copy is
#      `test_we_the_ladder_is_the_trees_and_not_a_copy_of_it`, which monkeypatches
#      `degree_from_net` and requires every margin here to follow it.
#      ⚠ AND ITS OPERAND DOES NOT EXIST YET, WHICH IS SAID HERE RATHER THAN DISCOVERED LATER.
#      `degree_from_net` reads `net - ob`. NOTHING IN THIS TRACER PRODUCES A `net`: there is no
#      roll anywhere in `shape.py`, `Act.pool` / `Act.obstacle` are read only by `S27.4`'s
#      refusal gate, and no subsystem the seam can call returns one. So this branch is a READER
#      WITH NO PRODUCER today. It is written anyway, and recorded on `H-98` -- whose own `cite:` lists
#      *give the ladder a margin the subsystem can supply* as one of its three options -- because the
#      alternative is worse in a specific way: without it the shape of the missing thing is a
#      guess, and with it the gap is exactly *"no subsystem returns a margin"* -- which is one of
#      the three options `H-98`'s own `cite:` lists.
#
#   2. THE SCENE, for a contest that routes to personal combat. JORDAN, 2026-09-03, VERBATIM:
#      *"kill/wound degrees should be directly taken from scene combat, which is what actually
#      needs to be called when kill/wound is considered."* And again, 2026-09-04: *"the combat
#      engine determines the result there. your code just has to accept the result."*
#      So combat is EXEMPT from the ladder by ruling, and its bands are a READ of the
#      `WoundTracker` the engine computed -- `combat_seam.resolve`'s `wound_state`.
#
# ⚠ THE BAND IS READ OFF **THE ACT'S SUBJECT**, NOT OFF "THE LOSER", AND THAT CORRECTS THE TABLE.
# `verb_table.yaml`'s `writes_source:` cell says `wound_state[loser]`. `kill / wound` writes on
# `payload["subject"]` (`_eff_kill`), so reading the LOSER kills the wrong person whenever the
# ACTOR is the one felled: A attacks B, B fells A, `wound_state[A].felled` is True, and the fold
# would delete B. The subject is the person the writes land on, so the subject is the person
# whose state decides which branch of the writes applies. The table's cell is corrected there.
# ---------------------------------------------------------------------------

# ⚠ THE THREE BANDS AND THE HARM MODEL ARE DATA, NOT LITERALS HERE — `rosters.yaml:
# combat_degree_bands` / `wound_harm_models`, bound at import beside every other roster (Jordan
# 2026-09-02: definitions are not hardcoded). `verb_table.yaml` keys `writes:`/`emits:` on the
# same three strings, and `writes_at`'s own refusal prints BOTH SETS when they disagree, so drift
# between the reading and the table is loud at the first act that folds.
# ⚠ A FOURTH BAND (decisive vs narrow) HAS NO SOURCE IN THE DATA and is NOT invented -- that is
# the whole of what survives in `H-98` after the 2026-09-03 ruling.

_LADDER: Optional[tuple] = None
_LADDER_ERROR: str = ""


def degree_ladder() -> Optional[tuple]:
    """`(degree_from_net, DEGREE_LABEL)` from the tree's owner, or `None` with a NAMED reason.

    Deferred and by path, which is `combat_seam.engine()`'s shape and for its reason: the tracer
    still runs where the engine tree is absent, degrading to a named gap rather than an
    ImportError at import. The repo root carries no top-level modules, so putting it on
    `sys.path` shadows none of this directory's bare-name imports."""
    global _LADDER, _LADDER_ERROR
    if _LADDER is not None or _LADDER_ERROR:
        return _LADDER
    root = files.REPO_ROOT
    try:
        if str(root) not in sys.path:
            sys.path.insert(0, str(root))
        from engine.autoload.dice_engine import (  # noqa: E402
            DEGREE_LABEL as _L, degree_from_net as _d)
        _LADDER = (_d, _L)
        return _LADDER
    except Exception as e:                        # a real import failure is a NAMED gap
        _LADDER_ERROR = f"{type(e).__name__}: {e}"
        return None


def ladder_error() -> str:
    degree_ladder()
    return _LADDER_ERROR


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


def combat_degree(result: dict, subject: Optional[str]) -> str:
    """The band, READ off the scene the engine just fought (Jordan, 2026-09-03). Invents nothing:
    every quantity below is a field of the engine's own `WoundTracker`, on the Combatants
    `combat_seam` constructed and still holds after `wrapper.fight` collapsed them to an int.

    `felled` and `result == 0` are the SAME event from the engine's side -- `wrapper.fight` sets a
    non-zero result only on a felling -- so the three bands are: the subject went down; the
    subject is standing and bled; the subject is standing and untouched."""
    states = result.get("wound_state") or {}
    st = states.get(subject)
    if not subject or st is None or not st.get("available"):
        raise Unspecified(
            f"personal combat resolved and the scene carries no wound state for the act's "
            f"subject ({subject!r}); it has {sorted(states)}", "S39.4/H-98",
            needs="a `wound_state` entry for the person the act writes on",
            law="Jordan 2026-09-03 -- the degree is READ OFF THE SCENE. A subject the scene never "
                "fought has no band, and picking one would be the mapping that ruling removed")
    if st["felled"]:
        return FELLED
    return WOUNDED if st["wounds"] > 0 else UNTOUCHED


def degree_of(result: Any, subject: Optional[str] = None) -> str:
    """THE ONE PLACE A SUBSYSTEM'S RESULT BECOMES THE TOKEN `writes_at` / `emits_at` KEY ON.

    ⚠ IT DECIDES NOTHING. Each branch hands the question to whoever already owns it -- the scene
    for combat, `degree_from_net` for a margin -- and a result carrying NEITHER refuses by name.
    That refusal is the honest state of `mass_battle` and `social_contest`, which the seam
    resolves and does not call (Jordan, 2026-09-02: *"we don't NEED to worry about them at this
    point in time"*)."""
    if not isinstance(result, dict):
        raise Unspecified(
            f"a contest returned {type(result).__name__}, which carries no outcome to grade",
            "S39.4", needs="a subsystem result",
            law="S39.4 -- the degree is the SUBSYSTEM's, read off what it returned")
    if "wound_state" in result:
        return combat_degree(result, subject)
    if "net" in result and "ob" in result:
        lad = degree_ladder()
        if lad is None:
            raise Unspecified(
                f"a contest returned a margin and the tree's degree ladder is unavailable: "
                f"{ladder_error()}", "S39.4",
                needs="engine/autoload/dice_engine.py",
                law="S27.2 -- the ladder is imported from its single owner. A band table copied "
                    "into this file would be the second resolver, and would keep answering "
                    "after the owner changed its mind")
        degree_from_net, label = lad
        return label[degree_from_net(result["net"], result["ob"])]
    raise Unspecified(
        f"a contest for {result.get('prize', result.get('module'))!r} resolved and returned "
        f"neither a scene to read nor a margin to grade (keys: {sorted(result)})",
        "S39.4/H-98",
        needs="a `wound_state` (the scene), or a `net`/`ob` pair (the margin the one ladder reads)",
        law="S39.4 -- FOUR BANDS READ OFF THE MARGIN, and Jordan 2026-09-03 exempts combat by "
            "reading them off the scene instead. A subsystem returning neither cannot be graded, "
            "and grading it anyway is the second resolver S27.2 refuses")


def contest(w: World, rung: str, prize: Any, claimants: list[str],
            depth: int, max_depth: int, causes: list[str],
            extension: Optional[Callable[[str], bool]] = None):
    """S39. EVERY ARGUMENT IS LOAD-BEARING. Attaches at EXACTLY ONE PLACE -- RESOLVE.

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
        # overrides. `combat_seam` is the IN-side, built on `engine/cross_scale/combat_bridge.py`'s
        # precedent rather than a new pattern.
        if _sub["module"] == "personal_combat":
            from . import combat_seam
            out = combat_seam.resolve(w, claimants, causes, prize)
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
