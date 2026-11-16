"""`seam/ladder.py` -- `04_CODE_ARCHITECTURE.md` §A.2's `seam/ladder` row: *"nothing.
`degree(margin, veto?) -> Degree"*, reading *"the exported band edges"*.

Everything that turns a subsystem's return into the token `writes_at` / `emits_at` key on:
`degree_of` (the dispatcher, which decides nothing), `combat_degree` (the fight's band read off the
scene, the worst over its parties) and `party_degree` (one party's band, the walk both read),
and the tree's single-owner ladder -- `_LADDER`, `degree_ladder()`, `ladder_error()`.

⚠ **`_LADDER` IS NOT RE-EXPORTED FROM `seam/__init__.py`, AND THAT IS DELIBERATE.** `degree_ladder()` reads
it as this module's global, so a re-export would bind a snapshot in the package namespace that goes stale
the moment a test swaps the ladder: a test that swaps the ladder must name `seam.ladder._LADDER`, not
`seam._LADDER`.

⚠ **`04`'s T-k IS READ NARROWLY HERE (ED-IN-0206).**
T-k (`04:122`) says *"the ladder lives once, in the seam"*. Read narrowly: `degree_from_net`
(`engine/dice_engine/dice_engine.py`) is the ONE margin ladder and `degree_of` (below) its ONE dispatcher.
`combat_degree` and `field_degree` are not ladders in that sense: each grades a
provider's own result against roster edges (`combat_band_edges` over `wound_quantities`;
`field_degree_bands`) and holds no band table of its own, so they stay in the seam when the
personal-combat and mass-battle engines live in `modules/`.
"""

from __future__ import annotations

from typing import Any, Optional
from engine.dice_engine.dice_engine import DEGREE_LABEL, degree_from_net
from ..data.rosters import (
    COMBAT_BANDS, COMBAT_EDGES, INVESTED, LOST, UNOPPOSED, WON, WOUND_QUANTITIES, WOUNDED,
    check_edge_above)
from ..gaps import Unspecified


# ---------------------------------------------------------------------------
# S39.4 -- THE DEGREE. TWO SOURCES, BOTH ALREADY RULED, NEITHER RE-DERIVED HERE.
#
# THE TWO SOURCES, AND WHY THIS FILE MAY NOT CHOOSE BETWEEN THEM:
#
#   1. THE LADDER, for a contest whose subsystem returns a MARGIN. `S39.4` -- one ladder for
#      every scale, four bands read off the margin -- and the tree OWNS it:
#      `engine/dice_engine/dice_engine.py::degree_from_net`, whose docstring reads *"THE degree
#      ladder. Single owner for every scale of the game (Jordan ruling, 2026-08-14)"*.
#      ⚠ IT IS IMPORTED AND CALLED, NOT MIRRORED. `S27.2` names a second resolver as its
#      highest-value refusal, and a band table copied into this file WOULD BE ONE -- it would go
#      on answering after the owner changed its mind. The falsifier that this is a call and not a
#      copy is `test_we_the_ladder_is_the_trees_and_not_a_copy_of_it`, which monkeypatches
#      `degree_from_net` and requires every margin here to follow it.
#      A `net` is produced by the MODULES (`modules/social_contest/roll.py`), not by
#      `seam/wrappers/sigma.py`, which only builds the record and calls the entry.
#
#   2. THE SCENE, for a contest that routes to personal combat. JORDAN, 2026-09-03, VERBATIM:
#      *"kill/wound degrees should be directly taken from scene combat, which is what actually
#      needs to be called when kill/wound is considered."* And again, 2026-09-04: *"the combat
#      engine determines the result there. your code just has to accept the result."*
#      So combat is EXEMPT from the ladder by ruling, and its bands are a READ of the
#      `WoundTracker` the engine computed -- `combat_seam.resolve`'s `wound_state`.
#
# ⚠ EACH PARTY IS WRITTEN BY HIS OWN BAND, NOT BY "THE LOSER"'S. `kill / wound` writes on
# `payload["subject"]` (`_eff_kill`), so reading the LOSER would kill the wrong person whenever the
# ACTOR is the one felled: A attacks B, B fells A, `wound_state[A].felled` is True, and the fold
# would delete B. Each party is written by HIS OWN band (`party_degree`, read in `_eff_kill`), so B
# is never deleted for A's felling, and the act's band, which the cells key on, is the WORST over
# both (`combat_degree`; CP-T03-00, `-08` AM-C-01).
# ---------------------------------------------------------------------------

# ⚠ THE THREE BANDS AND THE HARM MODEL ARE DATA, NOT LITERALS HERE — `rosters.yaml:
# combat_degree_bands` / `wound_harm_models`, bound at import beside every other roster (Jordan
# 2026-09-02: definitions are not hardcoded). `verb_table.yaml` keys `writes:`/`emits:` on the
# same three strings, and `writes_at`'s own refusal prints BOTH SETS when they disagree, so drift
# between the reading and the table is loud at the first act that folds.
# ⚠ AND SO IS WHERE THE BANDS FALL: `rosters.yaml: combat_band_edges` (plan position `8`), over the
# quantities `wound_quantities` lists, with the `Wounded` threshold the one swept fixture
# (`Fixtures.combat_wounded_above`, `H-184`).
# ⚠ A FOURTH BAND (decisive vs narrow) HAS NO SOURCE IN THE DATA and is NOT invented (`H-98`).

# The owner's ladder is imported at module scope: `seam/wrappers/sigma.py` imports the same dice engine at module
# scope, so a tree without it already fails `import seam`, and a named-gap path here would never run.
_LADDER: tuple = (degree_from_net, DEGREE_LABEL)


def degree_ladder() -> tuple:
    """`(degree_from_net, DEGREE_LABEL)` from the tree's owner (read at call time, so a test may swap `_LADDER`)."""
    return _LADDER


def ladder_error() -> str:
    """Why the ladder is unavailable: `""`, always (the owner is imported above). Kept for the callers that import it."""
    return ""


def party_degree(st: Optional[dict], wounded_above=None) -> str:
    """ONE PARTY'S band, READ off the scene the engine just fought (Jordan, 2026-09-03). Invents
    nothing: every quantity below is a field of the engine's own `WoundTracker`, on the Combatants
    `combat_seam` constructed and still holds after `wrapper.fight` collapsed them to an int. `st` is
    that party's `wound_state` entry.

    The bands read `felled`, never `result`: `wrapper.fight` sets a non-zero result on a felling AND
    on any §11.4 yield the engine did not refuse, accepted or not (PC-01), so the three bands are: the
    party went down; the party is standing and bled; the party is standing and untouched. ⚠ A YIELDER
    IS STANDING, so this walk reads him `Untouched`/`Wounded` and the surrender rides on
    `result["surrender"]` -- NO FOURTH BAND: a yield sets no quantity in `wound_quantities` that a
    fourth edge could be drawn over.

    ⚠ WHERE THE BANDS FALL IS DATA, NOT TWO LITERALS (`H-98`, plan position `8`; Jordan 2026-09-02:
    definitions are not hardcoded). `rosters.yaml: combat_band_edges` carries one `{quantity, above}`
    per band but the last; the bands are walked in `combat_degree_bands`' order (SEVERITY, worst
    first), the first whose quantity is strictly above its threshold is the answer, and the last
    band is what is left. The shipped edges reproduce `if felled: Felled; elif wounds > 0: Wounded;
    else: Untouched` exactly. `wounded_above` is `Fixtures.combat_wounded_above` -- the ONE swept
    edge, on the `Wounded` band; `None` is the roster's own value. The `Felled` edge is the engine's
    verdict accepted, never swept (`combat_band_edges`' note).

    CP-T03-00 (`-08` AM-C-01): the walk lives once and both
    readers ask it: `combat_degree` (the act's band, the worst over every party) and
    `loop/effects_combat.py::_eff_kill` (each party written by his own band)."""
    if st is None or not st.get("available"):
        raise Unspecified(
            f"personal combat resolved and a party's wound state is unavailable ({st!r})",
            "S39.4/H-98",
            needs="a `wound_state` entry, lifted off the party's own WoundTracker",
            law="Jordan 2026-09-03 -- the degree is READ OFF THE SCENE. A party the scene carries no "
                "tracker for has no band, and picking one would be the mapping that ruling removed")
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
                    f"the scene's wound state for a party carries no {q!r} "
                    f"(it has {sorted(st)})", "S39.4/H-98",
                    needs=f"`wound_state` to lift {q!r}, which `combat_band_edges` reads",
                    law="Jordan 2026-09-03 -- the degree is READ OFF THE SCENE; an edge over a "
                        "quantity the scene does not carry has nothing to read")
        if int(st[quantity]) > (int(st[above]) if isinstance(above, str) else above):
            return band
    return COMBAT_BANDS[-1]


def combat_degree(result: dict, subject: Optional[str], wounded_above=None) -> str:
    """THE FIGHT'S band: the WORST `party_degree` over every `wound_state` entry (CP-T03-00, `-08`
    AM-C-01), worst by `combat_degree_bands`' own order (SEVERITY, worst first). It is the token the
    fold keys `writes_at` / `emits_at` on, so the band's cells cover whatever any party took: a felled
    attacker makes the fight `Felled` though his target stands, and `contest.undecided` (`Untouched`'s
    kind) is reached only when every party is untouched. Who is written by which band is not this
    function's: `_eff_kill` reads `party_degree` per party.

    ⚠ THE SUBJECT IS REQUIRED TO BE A PARTY: the refusal for a subject the scene never fought
    stands, because the act's writes land on him and a scene without him is not the act's scene."""
    states = result.get("wound_state") or {}
    st = states.get(subject)
    if not subject or st is None or not st.get("available"):
        raise Unspecified(
            f"personal combat resolved and the scene carries no wound state for the act's "
            f"subject ({subject!r}); it has {sorted(states)}", "S39.4/H-98",
            needs="a `wound_state` entry for the person the act writes on",
            law="Jordan 2026-09-03 -- the degree is READ OFF THE SCENE. A subject the scene never "
                "fought has no band, and picking one would be the mapping that ruling removed")
    return min((party_degree(s, wounded_above) for s in states.values()), key=COMBAT_BANDS.index)


def field_degree(result: dict) -> str:
    """THE BAND `march` FOLDS ON (`ED-IN-0279` clause (a)), READ OFF THE MASS-BATTLE
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
    reconciling the two remains open MB-lane work. `march` writes on its graded bands (Won, Lost,
    Unopposed and, CP-T04-06, Invested); the engine's finer four-way split is available under
    `result['result']['degree']` for introspection and stays there."""
    if result.get("unopposed"):
        return UNOPPOSED
    # CP-T04-06: an opposed `besiege` fought no field -- the provider lifts `invested` and nobody won or lost.
    if result.get("invested"):
        return INVESTED
    return WON if result.get("attacker_wins") else LOST


def degree_of(result: Any, subject: Optional[str] = None, fixtures: Any = None) -> str:
    """THE ONE PLACE A SUBSYSTEM'S RESULT BECOMES THE TOKEN `writes_at` / `emits_at` KEY ON.

    `fixtures` is the world's `Fixtures`, read ONLY on the scene branch for `combat_wounded_above`
    (`H-98`) -- so a mass-battle or margin result never touches a combat fixture, and a caller with
    no world (a unit test grading a hand-built result) gets the roster's own edges.

    ⚠ IT DECIDES NOTHING. Each branch hands the question to whoever already owns it -- the scene
    for combat, `field_degree` for a mass battle, `degree_from_net` for a margin -- and a result
    carrying NONE OF THE THREE refuses by name.
    ⚠ `mass_battle` IS THE THIRD SHAPE (`ED-IN-0279` clause (a)). Its provider's result is a
    survivor-ratio classification, not a margin -- see
    `seam/wrappers/mass_battle.py`'s own docstring -- and `field_degree` does not grade THAT
    classification either; it reads the top-level `attacker_wins`/`unopposed` markers the provider
    lifts for exactly this purpose, onto the bands `march` writes on
    (Won/Lost/Unopposed, and Invested under a besiege). Reconciling the engine's own finer four-way split with the canonical
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
    # `attacker_wins` is `mass_battle`'s own top-level marker (`ED-IN-0279` clause (a)),
    # present on every RESOLVED result including the `unopposed` bypass -- neither a `wound_state`
    # nor a `net`/`ob` pair, so it takes a third branch rather than fitting either of the others.
    if "attacker_wins" in result:
        return field_degree(result)
    if "net" in result and "ob" in result:
        ladder, label = degree_ladder()
        # CP-T01-04: a record carrying `settled_margin` (the provider settled the margin's fraction by
        # the act's own draw) is graded on it, against a zero obstacle -- integers on both sides, so
        # the ladder's no-epsilon comparison is exact. A pair without one (a planted result, a caller
        # that never settled) is graded on `net` and `ob`.
        if "settled_margin" in result:
            return label[ladder(result["settled_margin"], 0)]
        return label[ladder(result["net"], result["ob"])]
    raise Unspecified(
        f"a contest for {result.get('prize', result.get('module'))!r} resolved and returned "
        f"neither a scene to read nor a margin to grade (keys: {sorted(result)})",
        "S39.4/H-98",
        needs="a `wound_state` (the scene), or a `net`/`ob` pair (the margin the one ladder reads)",
        law="S39.4 -- FOUR BANDS READ OFF THE MARGIN, and Jordan 2026-09-03 exempts combat by "
            "reading them off the scene instead. A subsystem returning neither cannot be graded, "
            "and grading it anyway is the second resolver S27.2 refuses")
