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

⚠ THE SEAM STILL DOES NOT MINT A DEGREE — IT NOW READS ONE. ⚠ SUPERSEDED IN PART 2026-09-03 BY A
JORDAN RULING: *"kill/wound degrees should be directly taken from scene combat, which is what
actually needs to be called when kill/wound is considered."*

The paragraph that stood here said the subsystem returns a WINNER, that `contest()` wants a band
off a MARGIN, and that **no mapping between them exists in any document**. The first two are still
true. The third was true of the DOCUMENTS and false of the DATA, and that is the correction:

  `wrapper.fight` returns `+1 / -1 / 0` and THROWS AWAY WHAT IT COMPUTED. But the seam constructs
  `A` and `B` and still holds them after the call, and each carries a `WoundTracker` (`.wt`) with
  `felled`, `wounds`, `max_wounds`, `health_remaining` and `health_full`. The severity of the
  outcome was computed by scene combat and is sitting on objects this module owns.

**So the degree is READ OFF THE SCENE, not mapped from a winner.** That is the ruling made
mechanical, and it invents nothing: this module already returns `parties={id: A.end}` by reading
the Combatants after the fight, and the wound state is the same read one field deeper.

⚠ WHAT IS STILL REGISTERED, NARROWED RATHER THAN CLOSED (`H-98`). The engine distinguishes exactly
two terminal states — FELLED (`result != 0`; `wrapper.fight` sets a result only when a fighter is
felled) and UNRESOLVED (`result == 0`, *"an undecided fight is a legitimate outcome"*, Jordan
2026-06-02) — and the wound counts grade the second. What the DATA does not carry is any
separation of a decisive win from a narrow one beyond wound count on the victor. So the bands
below the felled/unresolved split are the remaining decision, and they are edges over a quantity
that exists rather than a mapping between types that do not meet.
"""
from __future__ import annotations

import random
import sys
from typing import Any, Optional

from ...data import files
from ...decision import body_band_penalty
# ⚠ THE LEAF, NOT THE PACKAGE. `...manifest` re-exports from `registry.py`, which imports
# THIS module to register it — importing the package here closes that loop and the cycle
# guard counts it. `manifest/providers.py` imports nothing and is safe to reach from here.
from ...manifest.providers import provider
from ...state.ids import H

# ⚠ THE SILENT ONE, AND IT IS NAMED HERE BECAUSE ITS FAILURE IS GREEN. This used to climb four
# `parents[...]` levels from this module's own location -- a depth that is a fact about where this
# file sits rather than about the tree. Move the file one directory and `_PC` names something that
# does not exist, `engine()` returns `None`, `resolve()` answers `ENGINE-UNAVAILABLE`, the six seam
# tests SKIP, and the run reports success. The anchor is asserted at import in `season.data.files`.
_PC = files.PC_ENGINE_DIR

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
    bands = body_band_penalty(person, fx)
    # `end`'s class default is 4 (combatant.py). One band = one point, floored at 1: a dying
    # person still fights, which is the same floor `decision.budget` applies for the same reason.
    default_end = 4
    return combatant.Combatant(label, end=max(1, default_end - bands))


@provider("contest", "personal_combat")
def resolve(w: Any, claimants: list, causes: list, prize: Any, *,
            verb: str = "", subject: Optional[str] = None,
            rng: Optional[random.Random] = None) -> dict:
    """CALL the personal-combat engine. Returns what it said; decides nothing itself.

    The RNG is seeded from the WORLD's own clock and the causing act, so a contest is reproducible
    exactly as every other draw in this instrument is (`S33`: *unique per DRAW, not per
    operation*). `wrapper.fight`'s own note says to pass `random.Random(seed)` for determinism.

    ⚠ **`U1` ADDED `@provider` AND THREE KEYWORD PARAMETERS, AND THE SEED IS DELIBERATELY UNCHANGED.**
    ED-SC-0033 clause (1) rules that *"the seam dispatches by manifest ROW rather than the hardcoded
    personal_combat literal"*, so this function is now reached by lookup rather than by an `if`; the
    keywords are the second provider's signature, which the seam calls uniformly.
    ⚠ **AND `rng` IS ACCEPTED AND NOT USED HERE, WHICH IS A DELIBERATE NON-CHANGE.** `04 §C.12`'s
    rejection 4 wants the generator constructed by the driver, and `seam/wrappers/sigma.py` is built
    that way. This module already derives its own seed from `H(world_seed, tick, a_id,
    f"contest:{prize}:{causes[0]}")` — a DIFFERENT string from the driver's, with a different third
    argument — so consuming the driver's `rng` here would re-seed every existing `kill / wound`
    result and silently re-record the goldens under cover of a refactor. `04 PART D row 35` needs
    `purpose` UNIQUENESS, not one spelling across providers, and forcing one costs a golden re-record
    for nothing. The parameter is in the signature because the SEAM's call is uniform; whose seed a
    provider uses is the provider's.
    """
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
    # `H` returns a blake2b hexdigest (`state/ids.py`), so 16 is the RADIX that parses it back to
    # an int for the RNG -- structural, not a game value. Pre-existing; surfaced because step 8's
    # `S.H(...)` -> `H(...)` lift rewrote the line and the gate scores added lines.
    # [JUSTIFIED: radix for parsing H()'s hex digest, not a mechanical constant]
    seed = int(H(w.world_seed, w.tick, a_id, f"contest:{prize}:{causes[0] if causes else ''}"), 16)
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

    # ⚠ THE OUTCOME'S SEVERITY, READ OFF THE COMBATANTS THE SCENE JUST FOUGHT WITH (Jordan
    # 2026-09-03). No number is invented and no rule is re-implemented: every field below is a
    # property the engine's own `WoundTracker` computes, on objects this module constructed.
    # `fight()` collapses all of it to an int at the return; this reads it before it is lost.
    def _state(c) -> dict:
        wt = getattr(c, "wt", None)
        if wt is None:                      # ID-5 polarity: absence REFUSES, it does not default
            return dict(available=False)
        return dict(available=True, felled=bool(wt.felled), wounds=int(wt.wounds),
                    max_wounds=int(wt.max_wounds),
                    health_remaining=int(wt.health_remaining), health_full=int(wt.health_full))
    _wounds = {a_id: _state(A), b_id: _state(B)}

    return dict(status="RESOLVED", module="personal_combat", resolver="d_sigma",
                result=result, winner=winner,
                # THE DEGREE SOURCE. A caller reads severity from here; it does not map it from
                # `winner`, which carries none. `H-98`'s remaining half is which wound counts sit
                # in which band -- an edge over a real quantity, not an invented correspondence.
                wound_state=_wounds,
                # ⚠ `0` IS A RULED OUTCOME, NOT A FAILURE — Jordan, 2026-06-02, in the engine:
                # *"an undecided fight is a legitimate outcome."* The seam must not retry it into
                # a decision, which is what a caller expecting a winner would be tempted to do.
                unresolved=(result == 0),
                bouts=sum(1 for e in trace if e.get("kind") == "turn_start"),
                parties={a_id: A.end, b_id: B.end}, seed=seed)
