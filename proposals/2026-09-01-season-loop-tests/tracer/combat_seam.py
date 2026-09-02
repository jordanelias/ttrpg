"""THE IN-SIDE OF THE PERSONAL-COMBAT SEAM — the seam CALLS the engine that owns the prize.

⚠ JORDAN, 2026-09-02: *"kill / wound points towards a seam that should be calling in the personal
combat system."* That is a ruling, and it overrides the scope note that stood in `contest()` —
*"wiring those engines is out of this chain's scope"* — which made the seam resolve the subsystem
by name and then refuse. Resolving and refusing is a pointer; this is the call.

WHAT THIS IS, AND WHAT IT DELIBERATELY IS NOT
---------------------------------------------
`references/module_contracts.yaml` declares `personal_combat` with `sim_module:
systems/combat/combat_engine_v1/` and `resolver: d_sigma`. Its public entry point is
`wrapper.fight(A, B, cfg=None, rng=None, max_bouts=12) -> int` — `+1` A wins, `-1` B wins, and
**`0` UNRESOLVED, which is a RULING and not a failure**: *"NO automatic tiebreak (Jordan
2026-06-02): if neither fighter is felled, the round ends UNRESOLVED... an undecided fight is a
legitimate outcome."*

This module does not decide anything about combat. It derives two parties, hands them to that
engine with a deterministic RNG, and returns what the engine says. Every combat rule stays in
`systems/combat/`, which this chain may read and may not edit.

⚠ THE PRECEDENT IS `engine/cross_scale/combat_bridge.py`, AND IT IS FOLLOWED RATHER THAN
REINVENTED (§0: *answered by precedent — the tree has already decided this shape somewhere else*).
That module is the same seam from the campaign side, and its discipline is the part worth copying:
derive EXACTLY ONE field from something the actor genuinely has, leave every other field at the
class's own constructor default, and return a typed gap rather than fabricate a party. The
`Combatant` defaults it names — strength 4, agi 4, end 4, cog 3, att 3, spirit 3, focus 3, disp 4,
weapon `arming`, armor `light`, tradition `none` — are the class's, not this module's.

⚠ THE ONE DERIVED FIELD IS `end`, FROM `body_band_penalty`, AND IT INVENTS NO NUMBER. A tracer
`Person` carries nothing combat-shaped except `body`, an int on the condition scale. The tree
already owns the body → bands reading: `body_band_penalty` counts how many `band_floors["body"]`
floors a person has fallen below (0 at full operations, +1 per band), and `H-38` closed with
*"`Site.condition` is the model"* so that table is the registered one. `end` is the Combatant
field that reading belongs to — it drives `wound_interval`, `max_wounds` and `health_full`, i.e.
how much punishment the body takes. A healthy person gets the class default; each band costs one.
Which field the penalty lands on is the injected part and is registered (`H-97`); the magnitude is
not invented, because the bands already exist.

⚠ AND THE SEAM DOES NOT MINT A DEGREE. `contest()`'s contract (S39.4) reads a band off a MARGIN;
the subsystem returns a WINNER. Those are different types and no mapping between them exists in
any document. Inventing one here would be the second resolver §27.2 forbids, arriving in the seam
for the second time. The outcome is returned as the engine gave it, and the mismatch is registered
(`H-98`) rather than papered over.
"""
from __future__ import annotations

import random
import sys
from pathlib import Path
from typing import Any, Optional

_REPO = Path(__file__).resolve().parents[3]
_PC = _REPO / "systems" / "combat" / "combat_engine_v1"

_LOADED: Optional[tuple] = None
_LOAD_ERROR: str = ""


def engine() -> Optional[tuple]:
    """`(wrapper, combatant)` or `None`, loaded on FIRST USE and by PATH.

    ⚠ DEFERRED AND BY PATH, WHICH IS THE PRECEDENT'S SHAPE AND NOT LAZINESS. `combat_engine_v1/`
    is a flat module set with its own bare-import convention (`combat_bridge.py` says so, and the
    balance workbench depends on it), so it cannot be imported as `systems.combat...` without
    giving those modules a second identity. Deferring also means the tracer still runs when the
    engine is absent — this seam degrades to a named gap rather than an ImportError at load."""
    global _LOADED, _LOAD_ERROR
    if _LOADED is not None or _LOAD_ERROR:
        return _LOADED
    if not _PC.is_dir():
        _LOAD_ERROR = f"{_PC} does not exist"
        return None
    try:
        if str(_PC) not in sys.path:
            sys.path.insert(0, str(_PC))
        import wrapper as _w                      # noqa: E402  (flat module set, bare name)
        import combatant as _c                    # noqa: E402
        _LOADED = (_w, _c)
        return _LOADED
    except Exception as e:                        # a real import failure is a NAMED gap
        _LOAD_ERROR = f"{type(e).__name__}: {e}"
        return None


def load_error() -> str:
    engine()
    return _LOAD_ERROR


def derive_party(person: Any, fx: Any, label: str) -> Any:
    """One `Combatant` from one tracer `Person`. ONE derived field; the rest are the class's.

    Returns `None` when the engine is unavailable, never a stand-in."""
    eng = engine()
    if eng is None:
        return None
    _, combatant = eng
    import shape as S
    bands = S.body_band_penalty(person, fx)
    # `end`'s class default is 4 (combatant.py). One band = one point, floored at 1: a dying
    # person still fights, which is the same floor `Query.budget` applies for the same reason.
    default_end = 4
    return combatant.Combatant(label, end=max(1, default_end - bands))


def resolve(w: Any, claimants: list, causes: list, prize: Any) -> dict:
    """CALL the personal-combat engine. Returns what it said; decides nothing itself.

    The RNG is seeded from the WORLD's own clock and the causing act, so a contest is reproducible
    exactly as every other draw in this instrument is (`S33`: *unique per DRAW, not per
    operation*). `wrapper.fight`'s own note says to pass `random.Random(seed)` for determinism.
    """
    import shape as S
    eng = engine()
    if eng is None:
        return dict(status="ENGINE-UNAVAILABLE", why=load_error(), module="personal_combat")
    wrapper, _ = eng
    if len(claimants) < 2:
        # `combat_bridge.derive_parties` returns None on a derivation gap rather than faking a
        # side; the same rule, stated once more because the shape of the gap is different here.
        return dict(status="PARTY-GAP", why=f"personal combat needs two parties; got {len(claimants)}",
                    module="personal_combat")
    a_id, b_id = claimants[0], claimants[1]
    pa, pb = w.persons.get(a_id), w.persons.get(b_id)
    if pa is None or pb is None:
        return dict(status="PARTY-GAP", why=f"claimant not a person: {a_id!r} / {b_id!r}",
                    module="personal_combat")
    A, B = derive_party(pa, w.fixtures, a_id), derive_party(pb, w.fixtures, b_id)
    seed = int(S.H(w.world_seed, w.tick, a_id, f"contest:{prize}:{causes[0] if causes else ''}"), 16)
    trace: list = []
    prev = getattr(wrapper, "_TRACE", None)
    try:
        # The engine's own note: `_TRACE` adds no rng draw and no state mutation, so capturing it
        # CANNOT change the result. That is why the seam may record without perturbing.
        wrapper._TRACE = trace.append
        result = wrapper.fight(A, B, rng=random.Random(seed))
    finally:
        wrapper._TRACE = prev
    winner = a_id if result == 1 else (b_id if result == -1 else None)
    return dict(status="RESOLVED", module="personal_combat", resolver="d_sigma",
                result=result, winner=winner,
                # ⚠ `0` IS A RULED OUTCOME, NOT A FAILURE — Jordan, 2026-06-02, in the engine:
                # *"an undecided fight is a legitimate outcome."* The seam must not retry it into
                # a decision, which is what a caller expecting a winner would be tempted to do.
                unresolved=(result == 0),
                bouts=sum(1 for e in trace if e.get("kind") == "turn_start"),
                parties={a_id: A.end, b_id: B.end}, seed=seed)
