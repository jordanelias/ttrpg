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
**STILL OPEN: the shared fold code that actually constructs every `contest()` call --
`loop/resolve.py`'s `_target = payload.get("subject")` / `_parties = [a.actor] + ([_target] if
...)`, and its `rung=(a.payload if isinstance(a.payload, str) else None) or "R"` placeholder --
builds EXACTLY TWO claimants and no real `rung` for ANY contested verb today.** Generalizing that,
without changing `kill / wound`'s or `tell`'s existing behaviour, is M4 build step 5; this module's
half of the contract is complete and callable, the caller that would actually satisfy it is not.

⚠ **THIS DOES NOT DECIDE WHO ATTACKS, WHO DEFENDS, WHAT A GARRISON IS, OR WHAT AN EMPTY DEFENDING
SIDE MEANS.** Those are `march`'s own eligibility and effects (M4, still gated on Jordan's ruling,
`ED-IN-0279` clause (b)) -- the open half of that same row. This module's job is narrower and does
not need M4 answered first: given a claimant side and a named opposing faction, resolve the field
battle and return what the engine says, exactly as `seam/wrappers/combat.py` derives a party and
calls the engine without deciding who picked the fight.

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
from ...queries import world_q


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
    result = engine_resolve_field(w, claimants, other, terrain=None, rng=rng)
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
