"""`seam/ladder.py` -- `04_CODE_ARCHITECTURE.md` §A.2's `seam/ladder` row: *"nothing.
`degree(margin, veto?) -> Degree"*, reading *"the exported band edges"*.

Everything that turns a subsystem's return into the token `writes_at` / `emits_at` key on:
`degree_of` (the dispatcher, which decides nothing), `combat_degree` (the band read off the scene),
and the deferred import of the tree's single-owner ladder -- `_LADDER`, `_LADDER_ERROR`,
`degree_ladder()`, `ladder_error()`.

⚠ **`_LADDER` AND `_LADDER_ERROR` ARE NOT RE-EXPORTED FROM `seam/__init__.py`, AND THAT IS
DELIBERATE.** `degree_ladder()` rebinds both through `global`, so a re-export would bind a snapshot
in the package namespace that is permanently stale the moment the first call fires. Step 8
established this and it holds one directory down: a test that swaps the ladder must name
`seam.ladder._LADDER`, not `seam._LADDER`.

Moved whole from the flat `seam.py` by unit L2 of
`workplans/2026-09-09-layer1-conformance-plan.md` (ED-IN-0206).
"""

from __future__ import annotations

import sys

from typing import Any, Optional
from ..data import files
from ..data.rosters import (
    COMBAT_BANDS, COMBAT_EDGES, LOST, UNOPPOSED, WON, WOUND_QUANTITIES, WOUNDED,
    check_edge_above)
from ..gaps import Unspecified


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
#      ⚠ SUPERSEDED (plan position `8`'s record sweep): `seam/wrappers/sigma.py` now produces a `net`
#      for `fight`, `tell` and `march` (`test_we_only_a_verb_that_declares_contests_can_be_graded_today`
#      pins the producer set to {sigma.py}); what follows is the original rationale.
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
# `verb_table.yaml`'s `writes_source_note:` cell (`writes_source:` until 2026-09-25) said `wound_state[loser]`. `kill / wound` writes on
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
# ⚠ AND SO IS WHERE THE BANDS FALL: `rosters.yaml: combat_band_edges` (plan position `8`), over the
# quantities `wound_quantities` lists, with the `Wounded` threshold the one swept fixture
# (`Fixtures.combat_wounded_above`, `H-98`).
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


def combat_degree(result: dict, subject: Optional[str], wounded_above=None) -> str:
    """The band, READ off the scene the engine just fought (Jordan, 2026-09-03). Invents nothing:
    every quantity below is a field of the engine's own `WoundTracker`, on the Combatants
    `combat_seam` constructed and still holds after `wrapper.fight` collapsed them to an int.

    `felled` and `result == 0` are the SAME event from the engine's side -- `wrapper.fight` sets a
    non-zero result only on a felling -- so the three bands are: the subject went down; the
    subject is standing and bled; the subject is standing and untouched.

    ⚠ WHERE THE BANDS FALL IS DATA, NOT TWO LITERALS (`H-98`, plan position `8`; Jordan 2026-09-02:
    definitions are not hardcoded). `rosters.yaml: combat_band_edges` carries one `{quantity, above}`
    per band but the last; the bands are walked in `combat_degree_bands`' order (SEVERITY, worst
    first), the first whose quantity is strictly above its threshold is the answer, and the last
    band is what is left. The shipped edges reproduce `if felled: Felled; elif wounds > 0: Wounded;
    else: Untouched` exactly. `wounded_above` is `Fixtures.combat_wounded_above` -- the ONE swept
    edge, on the `Wounded` band; `None` is the roster's own value. The `Felled` edge is the engine's
    verdict accepted, never swept (`combat_band_edges`' note)."""
    states = result.get("wound_state") or {}
    st = states.get(subject)
    if not subject or st is None or not st.get("available"):
        raise Unspecified(
            f"personal combat resolved and the scene carries no wound state for the act's "
            f"subject ({subject!r}); it has {sorted(states)}", "S39.4/H-98",
            needs="a `wound_state` entry for the person the act writes on",
            law="Jordan 2026-09-03 -- the degree is READ OFF THE SCENE. A subject the scene never "
                "fought has no band, and picking one would be the mapping that ruling removed")
    if wounded_above is not None:
        # An injected threshold is held to the grammar the authored one is, so a bad arm REFUSES
        # rather than reading off a name the tracker never returned (§42.2.1 polarity).
        check_edge_above(wounded_above, WOUND_QUANTITIES, "Fixtures.combat_wounded_above",
                         "H-98")
    for band, quantity, above in COMBAT_EDGES:
        if band == WOUNDED and wounded_above is not None:
            above = wounded_above
        for q in (quantity, above):
            if isinstance(q, str) and q not in st:
                raise Unspecified(
                    f"the scene's wound state for {subject!r} carries no {q!r} "
                    f"(it has {sorted(st)})", "S39.4/H-98",
                    needs=f"`wound_state` to lift {q!r}, which `combat_band_edges` reads",
                    law="Jordan 2026-09-03 -- the degree is READ OFF THE SCENE; an edge over a "
                        "quantity the scene does not carry has nothing to read")
        if int(st[quantity]) > (int(st[above]) if isinstance(above, str) else above):
            return band
    return COMBAT_BANDS[-1]


def field_degree(result: dict) -> str:
    """M4 (`ED-IN-0279` clause (a)). THE BAND `march` FOLDS ON, READ OFF THE MASS-BATTLE
    PROVIDER'S OWN RESULT -- the shape `combat_degree` reads off a scene's `wound_state`, one
    function above. `seam/wrappers/mass_battle.py` lifts `attacker_wins`/`unopposed` to the TOP
    level of what it returns for exactly this read.

    ⚠ NO `subject` PARAMETER, UNLIKE `combat_degree`. `kill / wound` grades one duellist; `march`
    grades a SIDE, and there is no single person the band is read off of -- `Won`/`Lost` is the
    attacker's own outcome, and every person on the losing side takes the same band's writes
    (`04 §C.4`'s `writes_at(degree)`, unconditional on which person the write lands on). This
    matches `degree_of`'s margin branch, which also carries no `subject` (`degree_from_net` reads
    only `net`/`ob`).

    ⚠ DOES NOT GRADE `massbattle.py`'s OWN NON-CANONICAL `result['degree']`
    (Overwhelming/Success/Partial/Failure) -- that classification is disclosed as *"NOT the
    canonical degree ladder... a bespoke post-hoc classification"* by its own module header, and
    reconciling the two remains open MB-lane work, not M4's. `march` writes on THREE bands
    (Won/Lost/Unopposed); the engine's finer four-way split is available under
    `result['result']['degree']` for introspection and stays there."""
    if result.get("unopposed"):
        return UNOPPOSED
    return WON if result.get("attacker_wins") else LOST


def degree_of(result: Any, subject: Optional[str] = None, fixtures: Any = None) -> str:
    """THE ONE PLACE A SUBSYSTEM'S RESULT BECOMES THE TOKEN `writes_at` / `emits_at` KEY ON.

    `fixtures` is the world's `Fixtures`, read ONLY on the scene branch for `combat_wounded_above`
    (`H-98`) -- so a mass-battle or margin result never touches a combat fixture, and a caller with
    no world (a unit test grading a hand-built result) gets the roster's own edges.

    ⚠ IT DECIDES NOTHING. Each branch hands the question to whoever already owns it -- the scene
    for combat, `field_degree` for a mass battle, `degree_from_net` for a margin -- and a result
    carrying NONE OF THE THREE refuses by name.
    ⚠ `mass_battle` WAS THE UNGRADABLE THIRD SHAPE UNTIL M4 (`ED-IN-0279` clause (a)); it is not
    any more. Its provider's result is still a survivor-ratio classification, not a margin -- see
    `seam/wrappers/mass_battle.py`'s own docstring -- and `field_degree` does not grade THAT
    classification either; it reads the top-level `attacker_wins`/`unopposed` markers the provider
    lifts for exactly this purpose, onto the three bands `march` actually writes on
    (Won/Lost/Unopposed). Reconciling the engine's own finer four-way split with the canonical
    ladder stays open MB-lane work, unrelated to this."""
    if not isinstance(result, dict):
        raise Unspecified(
            f"a contest returned {type(result).__name__}, which carries no outcome to grade",
            "S39.4", needs="a subsystem result",
            law="S39.4 -- the degree is the SUBSYSTEM's, read off what it returned")
    if "wound_state" in result:
        return combat_degree(
            result, subject,
            None if fixtures is None else fixtures.get("combat_wounded_above"))
    # M4 (`ED-IN-0279` clause (a)). `attacker_wins` is `mass_battle`'s own top-level marker,
    # present on every RESOLVED result including the `unopposed` bypass -- neither a `wound_state`
    # nor a `net`/`ob` pair, so it needed a third branch rather than fitting either existing one.
    if "attacker_wins" in result:
        return field_degree(result)
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
