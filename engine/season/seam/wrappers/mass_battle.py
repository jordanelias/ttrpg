"""THE MASS-BATTLE PROVIDER -- the seam's wrapper around `systems/mass_battle/sim/massbattle.py`'s
season-facing entry point, `resolve_field`. Wired M3 of the `mc_v18`-retirement plan
(`ED-IN-0279`); `rosters.yaml`'s "a field" row previously had a `module:` and NO `provider:`,
whose own comment said the absence WAS the row -- *"sides need `faction_q.resolve` (04 §C.5.1)"*.
M2 built `faction_q.resolve`; this is the call that reads it.

⚠ **THE `claimants`/`subject`/`rung` SPLIT BELOW IS SETTLED, AND WHAT STILL SUPPLIES IT IS NOT.**
`seam/contest.py`'s S39.1 is unconditional: *"claimant[] is PERSONS, ALWAYS. Not factions, not
units, not sides"*, and `seam/wrappers/sigma.py` already types `subject` as sometimes naming
something that is NOT a person, so this module's shape needed no new seam-level concept: it reuses
`subject` for the other side's faction Proposition id (as always) and, new at M4 (`ED-IN-0279`
clause (a)), reads `rung` -- ALREADY a parameter of `contest()`, already passed at every call site,
unused until now -- to scope that faction's `members` down to who is actually PRESENT at the
target, via `world_q.mustered` (`04 §C.5.1`'s own *"squad combat: the squad is
`members ∩ present-at-rung`"*). `claimants` stays one side's already-resolved `PersonId[]` per
§C.5.1's *"sides = (faction_q.resolve(proj,A), faction_q.resolve(proj,B)) -- ONCE, before
provider.run"*.
**M4 BUILD STEP 5 CLOSED THIS.** `loop/sides.py::sides_of`, dispatched on the PRIZE's own manifest
`module` (never on `a.verb`, and never on what the target looks like -- see that module's own
docstring for the corpus case that made a shape-based dispatch unsafe), now builds the REAL
`claimants`/`subject`/`rung` for this prize: the actor's own muster at the origin, the target
rung's holder faction (`queries/world_q.holder_faction_of`), and the target rung itself. `kill /
wound` and `tell` keep their pre-M4 two-claimant shape unchanged, through `sides_of`'s other
branch, which is what "generalizing without changing their behaviour" meant.

⚠ **WHO ATTACKS, WHO DEFENDS, AND WHAT AN EMPTY DEFENDING SIDE MEANS ARE `march`'s OWN eligibility
and effects, RULED AND BUILT (M4, `ED-IN-0279` clause (b), 2026-09-28)** -- an empty defending side
is `Unopposed` (the branch at line ~99 below), never an auto-win manufactured here.

⚠⚠ **WHAT A GARRISON DOES TO THIS FIGHT IS NOW READ, AND THE READ IS ALL THIS MODULE ADDS (plan
position `20-iv`, `H-150`).** Jordan's ruling (planning round 2) fixed garrison STRENGTH as a Site's
`condition` field, and `queries/world_q.py::fortification_of` reads it. Until `20-iv` nothing called
that function: this module passed `terrain=None` unconditionally, so a garrisoned settlement fought
exactly like an undefended one. `resolve()` now reads three facts about the fight off the world and
hands them on as plain values -- it decides none of what they do:
  * the TERRITORY the target sits in, `_territory_of` below: the nearest `territory`-kind rung up
    the target's ancestry, turned back into its geography row by `data/rosters.territory_id_of`
    (the one owner of that id relation, which `harness/populated.py` mints through);
  * its FORTIFICATION, `world_q.fortification_of` at the target;
  * each side's MORALE source, `_side_stance` below;
and, since plan position `20-v`, one injected value: the `field_walls_dr` fixture (`H-150`).
What a fortification DOES is `massbattle.resolve_field`'s and `terrain.py`'s: any positive value
makes the field A.9's `WALLS` row, whose one number (defender +3 DR) the engine applies to `Unit.dr`
1:1 (an ASSUMPTION about the unit, `H-150`). The number is canon's, not invented here -- `None` in the
fixture leaves it where `terrain.py` authors it, and an int sweeps it -- which is why this
module may carry the read without deciding anything -- `seam/wrappers/combat.py` derives a party the same way and calls the
engine without deciding who picked the fight.

⚠ **`degree_of` (`seam/ladder.py`) NOW GRADES THIS RESULT, THROUGH A THIRD BRANCH RATHER THAN BY
MANUFACTURING A MARGIN (M4, `ED-IN-0279` clause (a)).** It does NOT grade `massbattle.py`'s own
survivor-ratio classification, which is still disclosed as *"NOT the canonical degree ladder ... a
bespoke post-hoc classification"* by that module's own header -- reconciling the two stays open
MB-lane work. What it grades is the top-level `attacker_wins`/`unopposed` this function lifts,
onto the three bands `march` writes on (`seam/ladder.py::field_degree`). Manufacturing a `net`/`ob`
from the survivor-ratio classification would have been the second resolver S27.2 refuses; reading
a marker this function already derives is not that.

⚠ **NO NEW `sys.path` SEAM.** `resolve_field` is reached through `composition.require`
(`references/module_contracts.yaml`'s `mass_battle.resolve_field` role), not a direct
`systems.mass_battle...` import -- `tests/valoria/test_engine_does_not_import_systems.py`'s
`BASELINE_TOTAL` ratchet is zero dotted `systems.*` imports anywhere under `engine/`, and
`PATH_SEAM_ALLOWED` is one entry (`substrate/pc_engine.py`, needed only because
`combat_engine_v1/` bare-imports its own siblings). `massbattle.py`'s own imports are already
proper dotted `systems.mass_battle.sim.*`, so it has no such problem and needs no second entry --
the composition-role indirection is the correct-fit channel, not a workaround.
"""
from __future__ import annotations

import random
from typing import Any, Optional

# ⚠ THE LEAF, NOT THE PACKAGE. See combat.py/sigma.py's own note: importing `...manifest` (which
# re-exports from `registry.py`, which imports `seam/wrappers/*` to register them) would close the
# import cycle `manifest/providers.py` exists to break.
from ...manifest.providers import provider
from ...data.rosters import territory_id_of
from ...queries.person_q import stance_toward
from ...queries import world_q


def _territory_of(w: Any, rung: str) -> Optional[str]:
    """The geography territory id of the territory `rung` sits in, or `None`.

    The nearest `territory`-kind rung at or above `rung` (`world_q.ancestry`, the walk
    `holder_faction_of` and `loop/sides.py`'s origin both use), read back to its geography row by
    `territory_id_of`. `None` -- no territory above, or one no geography row minted (a corpus
    fixture's) -- is `terrain_row_for_territory`'s no-modifier case, not a refusal."""
    for cur in world_q.ancestry(w, rung):
        r = w.rungs.get(cur)
        if r is not None and r.kind == "territory":
            return territory_id_of(cur)
    return None


def _side_stance(w: Any, pids: list) -> float:
    """A side's weight-mean stance toward each member's OWN faction -- the season's morale carrier
    (`massbattle._morale_start`'s docstring says why it is this one).

    Each member's faction is `world_q.faction_holding`, the one owner of *which faction a person
    coheres under*, and the stance is `queries.person_q.stance_toward`, the one reader of a stance row
    (valence x weight, summed over the rows naming that referent). A member committed to no faction
    or to two reads `None` there and contributes zero -- `faction_holding`'s own *"NONE AND MANY BOTH
    RETURN None, AND NEITHER IS A DEFAULT"*. Weighted by `Person.weight` because `resolve_field` sizes
    the side by the same weights: a cohort of ten carries ten men's morale. An empty side reads 0."""
    total = 0
    acc = 0.0
    for pid in pids:
        p = w.persons.get(pid)
        if p is None:
            continue
        fac = world_q.faction_holding(w, pid)
        acc += p.weight * (stance_toward(p, fac) if fac is not None else 0.0)
        total += p.weight
    return acc / total if total else 0.0


def _resolver():
    """`resolve_field`, by composition role. Deferred: a module-level import here would put
    `engine.substrate.composition` — and, transitively, `systems.mass_battle...` — on every
    caller's import path merely for importing this wrapper, not for calling it."""
    from engine.substrate import composition
    return composition.require("mass_battle.resolve_field")


@provider("contest", "mass_battle")
def resolve(w: Any, claimants: list, causes: list, prize: Any, *,
            verb: str = "", subject: Optional[str] = None,
            rng: Optional[random.Random] = None, rung: str = "") -> dict:
    """CALL the mass-battle engine. Returns what it said; decides nothing itself.

    `claimants`: one side's `PersonId[]`, expected already resolved (§C.5.1) by whoever called
    `contest()` -- see this module's docstring for why nothing does that yet.
    `subject`: the OTHER side's faction Proposition id.
    `rung`: where the defence is scoped (M4, `ED-IN-0279` clause (a)) -- `subject`'s faction is
    resolved to its `members` (`faction_q.resolve`, the same function M2 built) and THEN
    INTERSECTED with presence at `rung`'s subtree (`queries/world_q.mustered`), per `04 §C.5.1`'s
    own pseudocode: *"squad combat: the squad is `members ∩ present-at-rung`"*. Without the
    intersection a field battle would defend with a faction's ENTIRE membership wherever it
    stands -- the M4 planning pass's F6, closed here. REQUIRED: a caller with no rung has no
    place to defend, which is a PARTY-GAP exactly like a caller with no claimants.

    `result` carries `massbattle.py`'s own non-canonical survivor-ratio classification under
    `result['degree']`, kept for introspection; it is NOT the token `degree_of` grades with (see
    this module's docstring) and callers should not read it as one."""
    if not claimants:
        return dict(status="PARTY-GAP", why="a field battle needs at least one claimant",
                    module="mass_battle")
    if subject is None:
        return dict(status="PARTY-GAP", why="a field battle needs a named opposing faction "
                    "(subject); none given", module="mass_battle")
    if not rung:
        return dict(status="PARTY-GAP", why="a field battle needs a place to scope the "
                    "defending side to (rung); none given", module="mass_battle")
    other = world_q.mustered(w, rung, subject)
    if not other:
        # ⚠ AN EMPTY DEFENDING SIDE IS `Unopposed`, NOT A CALL TO `resolve_field` (M4,
        # `ED-IN-0279` clause (a)). `resolve_field`'s own docstring: *"AN EMPTY `side_b` gets
        # `_MIN_TROOPS`' crash-avoidance floor, not an invented auto-win... what an empty
        # defending force MEANS is eligibility policy for whichever verb calls this."* This
        # wrapper is that caller's derivation half: it does not decide what an unopposed march
        # means for the game, but it does not launder "nobody mustered" into a fabricated fight
        # against a floor-sized phantom unit either. `attacker_wins`/`unopposed` are top-level so
        # `seam/ladder.py::field_degree` can grade this without opening `result`.
        return dict(status="RESOLVED", module="mass_battle", resolver="dice_pool",
                    attacker_wins=True, unopposed=True,
                    result=dict(attacker_wins=True, degree="Unopposed",
                                attacker_size_pct=1.0, defender_size_pct=0.0),
                    winner=claimants,
                    parties={"claimants": claimants, "subject_members": other})
    try:
        engine_resolve_field = _resolver()
    except Exception as e:
        return dict(status="ENGINE-UNAVAILABLE", why=f"{type(e).__name__}: {e}", module="mass_battle")
    # PLAN POSITION `20-iv`: the place and the two sides' morale, read here and decided there
    # (`H-150` -- `fortification_of`'s caller on the battle path).
    # PLAN POSITION `20-v`: the walls' DR is the `field_walls_dr` fixture (`H-150`), `None` = A.9's
    # own number, which `massbattle` reads from `terrain.py` -- this wrapper decides none of it.
    result = engine_resolve_field(w, claimants, other,
                                  territory=_territory_of(w, rung),
                                  fort_level=world_q.fortification_of(w, rung),
                                  stance_a=_side_stance(w, claimants),
                                  stance_b=_side_stance(w, other),
                                  walls_dr=w.fixtures.get("field_walls_dr"), rng=rng)
    return dict(status="RESOLVED", module="mass_battle", resolver="dice_pool",
                # ⚠ LIFTED TO TOP LEVEL, NOT LEFT NESTED UNDER `result` (M4). `degree_of`
                # (`seam/ladder.py`) reads a provider's return directly -- `wound_state` and
                # `net`/`ob` are already top-level for the other two providers -- so a third,
                # nested-only shape would be the one branch `degree_of` could not reach without
                # a special case. `result['degree']` stays as `massbattle.py`'s own
                # non-canonical classification, kept for introspection only; it is NOT this.
                attacker_wins=result.get("attacker_wins"), unopposed=False,
                result=result,
                winner=(claimants if result.get("attacker_wins") else other),
                parties={"claimants": claimants, "subject_members": other})
