"""THE FIGHT -- the `combat` module's entry (A-25; plan position `31b`).

`modules/combat/` is the personal-combat engine: the import closure of `wrapper` and `combatant`, moved
from `systems/combat/combat_engine_v1/` at `31b` with its FLAT names kept (the files bare-import each other;
`engine/substrate/pc_engine.py` is the one path seam that loads them, and this directory has no
`__init__.py` on purpose -- it is a scripts directory, not a package of dotted modules). This file is the one
module entry: the composition row whose target is `fight` below (`entry: verb_call`, `verb: fight`),
registered in `manifest.MODULE_ENTRIES` by the registrar at driver construction, and called by the host
adapter `seam/wrappers/combat.py::resolve` -- the `@provider("contest", "personal_combat")` the prize row
`the body` names, for every verb contesting that prize.

It takes the host's typed input record and a seeded `rng`, and imports the path seam and the record type,
nothing else of the host. It never reads or writes `World`, holds no token and keeps no state between
calls (A-25): the engine's `wrapper._TRACE` hook is set for the call and restored after it.

It reads the scene, it does not grade it. It returns what the engine computed before `wrapper.fight`
collapses it to an int -- the result, the trace, each party's `end` and the `WoundTracker` fields the record
names -- and the host interprets that: the winner, the surrender, the bout count and the wound-state
refusal are `seam/wrappers/combat.py`'s, and the degree is `seam/ladder.py::combat_degree`'s.
"""
from __future__ import annotations

import random
from typing import Optional

from engine.season.queries.inputs import PersonalCombatInput
from engine.substrate import pc_engine

_MISSING = object()   # `getattr`'s default for a tracker field the engine does not carry (None is a value)


def fight(inp: PersonalCombatInput, rng: Optional[random.Random] = None) -> dict:
    """Fight one bout scene between the record's two parties. RESOLVED -> dict(status, result, trace,
    ends, wound_state), where `wound_state[id]` is `None` when the Combatant carries no tracker and
    otherwise holds each `inp.wound_quantities` field the tracker carries (a field it lacks is absent,
    and the host refuses it by name).

    The `rng` is a parameter and is never constructed here (`04 §C.12` rejection 4): the host builds it
    from its own seed and passes it down. `pc_engine.load()` RAISES on a missing engine, by its own
    contract; a module whose directory is gone is refused earlier, at driver construction, by the
    registrar resolving this file."""
    wrapper, combatant = pc_engine.load()
    a_id, b_id = inp.claimants
    a_end, b_end = inp.ends
    A, B = combatant.Combatant(a_id, end=a_end), combatant.Combatant(b_id, end=b_end)
    trace: list = []
    prev = getattr(wrapper, "_TRACE", None)
    try:
        # The engine's own note: `_TRACE` adds no rng draw and no state mutation, so capturing it
        # CANNOT change the result. That is why the scene may be recorded without perturbing it.
        wrapper._TRACE = trace.append
        result = wrapper.fight(A, B, rng=rng)
    finally:
        wrapper._TRACE = prev

    def _lift(c) -> Optional[dict]:
        wt = getattr(c, "wt", None)
        if wt is None:
            return None
        out = {}
        for q in inp.wound_quantities:
            v = getattr(wt, q, _MISSING)
            if v is not _MISSING:
                out[q] = v
        return out

    return dict(status="RESOLVED", result=result, trace=trace,
                ends={a_id: A.end, b_id: B.end},
                wound_state={a_id: _lift(A), b_id: _lift(B)})
