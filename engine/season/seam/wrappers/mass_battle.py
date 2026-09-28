"""THE MASS-BATTLE PROVIDER -- the seam's wrapper around `systems/mass_battle/sim/massbattle.py`'s
season-facing entry point, `resolve_field`. Wired M3 of the `mc_v18`-retirement plan
(`ED-IN-0279`); `rosters.yaml`'s "a field" row previously had a `module:` and NO `provider:`,
whose own comment said the absence WAS the row -- *"sides need `faction_q.resolve` (04 §C.5.1)"*.
M2 built `faction_q.resolve`; this is the call that reads it.

⚠ **THE `claimants`/`subject` SPLIT BELOW IS THIS MODULE'S OWN PROPOSAL FOR WHAT `march` (M4) MUST
SUPPLY, NOT AN ALREADY-AGREED CONVENTION -- CHECKED AGAINST THE ONLY REAL CALLER AND FOUND NOT YET
SATISFIABLE BY IT.** `seam/contest.py`'s S39.1 is unconditional: *"claimant[] is PERSONS, ALWAYS.
Not factions, not units, not sides"*, and `seam/wrappers/sigma.py` already types `subject` as
sometimes naming something that is NOT a person. But the shared fold code that actually
constructs every `contest()` call today -- `loop/resolve.py`'s `_target = payload.get("subject")`
/ `_parties = [a.actor] + ([_target] if ...)` -- builds EXACTLY TWO claimants for ANY contested
verb, and passes `subject` as that SAME second person, read by `sigma.py::_obstacle_of` to look up
ONE entity's own capability. Reading `subject` as a whole FACTION whose members[] are pulled in as
the opposing side is an EXPANSION this seam has never done before, not the sigma precedent
extended -- named here rather than overclaimed. So: `claimants` = one side's already-resolved
`PersonId[]` (per §C.5.1's "sides = (faction_q.resolve(proj,A), faction_q.resolve(proj,B)) --
ONCE, before provider.run"), `subject` = the other side's faction Proposition id, resolved HERE.
**Wiring `march` to call this provider will need to ALSO change `loop/resolve.py`'s shared
`_parties`/`_target` construction** -- itself a change to code every OTHER contested verb runs
through, so it is not a narrow addition. That is M4's work, gated on Jordan's ruling
(`ED-IN-0279`); this module states the contract it would need, not a working integration.

⚠ **THIS DOES NOT DECIDE WHO ATTACKS, WHO DEFENDS, WHAT A GARRISON IS, OR WHAT AN EMPTY DEFENDING
SIDE MEANS.** Those are `march`'s own eligibility and effects (M4, still gated on Jordan's ruling,
`ED-IN-0279` clause (b)) -- the open half of that same row. This module's job is narrower and does
not need M4 answered first: given a claimant side and a named opposing faction, resolve the field
battle and return what the engine says, exactly as `seam/wrappers/combat.py` derives a party and
calls the engine without deciding who picked the fight.

⚠ **`degree_of` (`seam/ladder.py`) CANNOT GRADE THIS RESULT YET, AND THAT IS DISCLOSED, NOT
HIDDEN.** It recognizes exactly two shapes: a `wound_state` (combat's scene) or a `net`/`ob` pair
(the margin ladder). This provider's `result` carries neither -- `massbattle.py`'s own header
already discloses that its survivor-ratio bands "are NOT the canonical degree ladder ... a
bespoke post-hoc classification", and "reconciling the two is open MB-lane work, not a port
concern". Manufacturing a `net`/`ob` from that classification without a real derivation would be
the second resolver S27.2 refuses, so this does not attempt one. Consequence, stated plainly: if
`loop/resolve.py:662` ever calls `degree_of` on this dict (which needs a verb declaring `contests:
"a field"` -- M4, not built), it will raise `Unspecified("... neither a scene to read nor a margin
to grade")`. Nothing calls this integration today, so the raise is a named forward gap, not a live
defect; M4 inherits it alongside the `claimants`/`subject` gap above.

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
from ...queries import faction_q


def _resolver():
    """`resolve_field`, by composition role. Deferred: a module-level import here would put
    `engine.substrate.composition` — and, transitively, `systems.mass_battle...` — on every
    caller's import path merely for importing this wrapper, not for calling it."""
    from engine.substrate import composition
    return composition.require("mass_battle.resolve_field")


@provider("contest", "mass_battle")
def resolve(w: Any, claimants: list, causes: list, prize: Any, *,
            verb: str = "", subject: Optional[str] = None,
            rng: Optional[random.Random] = None) -> dict:
    """CALL the mass-battle engine. Returns what it said; decides nothing itself.

    `claimants`: one side's `PersonId[]`, expected already resolved (§C.5.1) by whoever called
    `contest()` -- see this module's docstring for why nothing does that yet.
    `subject`: the OTHER side's faction Proposition id -- resolved here, via `faction_q.resolve`,
    to that faction's `members` (the same function M2 built, single-owned: this does not
    re-implement membership).

    `result` carries `massbattle.py`'s own non-canonical survivor-ratio classification under
    `result['degree']`, kept for introspection; it is NOT the token `degree_of` grades with (see
    this module's docstring) and callers should not read it as one."""
    if not claimants:
        return dict(status="PARTY-GAP", why="a field battle needs at least one claimant",
                    module="mass_battle")
    if subject is None:
        return dict(status="PARTY-GAP", why="a field battle needs a named opposing faction "
                    "(subject); none given", module="mass_battle")
    other = faction_q.resolve(w, subject).members
    try:
        engine_resolve_field = _resolver()
    except Exception as e:
        return dict(status="ENGINE-UNAVAILABLE", why=f"{type(e).__name__}: {e}", module="mass_battle")
    result = engine_resolve_field(w, claimants, other, terrain=None, rng=rng)
    return dict(status="RESOLVED", module="mass_battle", resolver="dice_pool",
                result=result,
                winner=(claimants if result.get("attacker_wins") else other),
                parties={"claimants": claimants, "subject_members": other})
