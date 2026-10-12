"""THE IN-SIDE OF THE PERSONAL-COMBAT SEAM — the seam CALLS the engine that owns the prize.

This module is the HOST (plan position `31b`, A-25): the input builder `combat_input` (`World` ->
`queries/inputs.py::PersonalCombatInput`: the two parties, each one's derived `end`, the wound
quantities to lift) and the adapter `resolve`, which keeps the PARTY-GAP refusals and the seed, calls
the module entry the prize row names (`module_entry:`, registered in `manifest.MODULE_ENTRIES` from its
composition row) and interprets what comes back -- the winner, the surrender, the bouts, the wound-state
refusal -- and returns the scene's trace beside them (PC-06 M-1). The fight itself is
`modules/combat/fight.py`, reached by string; it, not this module, constructs the `Combatant`s and calls
`wrapper.fight`. Below, "this module constructs" and "the seam holds the Combatants" mean THE ENTRY's.

⚠ JORDAN, 2026-09-02: *"kill / wound points towards a seam that should be calling in the personal
combat system."* That is a ruling, and it overrides the scope note that stood in `contest()` —
*"wiring those engines is out of this chain's scope"* — which made the seam resolve the subsystem
by name and then refuse. Resolving and refusing is a pointer; this is the call.

WHAT THIS IS, AND WHAT IT DELIBERATELY IS NOT
---------------------------------------------
`references/module_contracts.yaml` declares `combat` (plan position `30`; the PROVIDER this module
registers keeps the name `personal_combat`) with `sim_module: modules/combat/` and `resolver: d_sigma`. Its public entry point is
`wrapper.fight(A, B, cfg=None, rng=None, max_bouts=12, yield_decl=None) -> int` — `+1` A wins, `-1` B wins, and
**`0` UNRESOLVED, which is a RULING and not a failure**: *"NO automatic tiebreak (Jordan
2026-06-02): if neither fighter is felled, the round ends UNRESOLVED... an undecided fight is a
legitimate outcome."*

This module does not decide anything about combat. It derives two parties, hands them to that
engine with a deterministic RNG, and returns what the engine says. Every combat rule stays in
the engine (`modules/combat/` since `31b`), which this chain may read and may not edit.

⚠ THE LOADER: `engine/substrate/pc_engine.py`, the one path seam into the engine, which the module
entry calls. This module reads it only for `engine()`, the availability probe its tests skip on, and
`load_error()`, the leaf's raise translated into a named reason. The adapter's typed refusal
`ENGINE-UNAVAILABLE` is the unregistered entry's (no driver constructed in the process), as in `sigma.py`.
⚠ THE PARTY DISCIPLINE FOLLOWS `combat_bridge.py` AS PRECEDENT RATHER THAN REINVENTING IT (§0:
*answered by precedent — the tree has already decided this shape somewhere else*). Its discipline is the part worth copying:
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
two terminal states — DECIDED (`result != 0`; `wrapper.fight` sets a result when a fighter is
felled, or when an unrefused §11.4 yield ends the scene, which `surrender` on the result carries) and UNRESOLVED (`result == 0`, *"an undecided fight is a legitimate outcome"*, Jordan
2026-06-02) — and the wound counts grade the second. What the DATA does not carry is any
separation of a decisive win from a narrow one beyond wound count on the victor. So the bands
below the felled/unresolved split are the remaining decision, and they are edges over a quantity
that exists rather than a mapping between types that do not meet.
"""
from __future__ import annotations

import random
from typing import Any, Optional

from ...data.rosters import WOUND_QUANTITIES
from ...decision import body_band_penalty
from ...gaps import Unspecified
# ⚠ THE LEAF, NOT THE PACKAGE'S RE-EXPORT. `manifest/providers.py` imports nothing, so no import
# here closes a loop back into this package (`_entry.py` says the same of the entry lookup).
from ...manifest.providers import provider
from ...queries.inputs import PersonalCombatInput
from ...state.ids import H
from ._entry import entry_for

_PROVIDER = "personal_combat"


def _probe() -> tuple:
    """`(PCEngine, "")` or `(None, reason)`: the substrate leaf's RAISE, translated to a named reason.
    `pc_engine.load()` caches a success itself; the import is deferred so the tracer still imports
    where the engine tree is absent."""
    try:
        from engine.substrate import pc_engine
        return pc_engine.load(), ""         # a PCEngine: (wrapper, combatant) BY NAME
    except Exception as e:                  # a real load failure is a NAMED gap
        return None, f"{type(e).__name__}: {e}"


def engine() -> Optional[tuple]:
    """`(wrapper, combatant)` or `None` when the engine cannot load (`load_error()` says why). An
    AVAILABILITY PROBE only -- the adapter below never calls the engine through it."""
    return _probe()[0]


def load_error() -> str:
    """Why `engine()` is `None`, as `ExceptionType: message`; `""` when it loads."""
    return _probe()[1]


def surrender_of(trace: list) -> Optional[dict]:
    """§11.4 YIELD, LIFTED OFF THE SCENE'S TRACE (PC-01, `ED-PC-0056`) -- `wrapper.fight`'s `yield` event,
    or `None` when nobody yielded. A declaration the engine REFUSED (the yielder's objective still
    contested in the zone) is not a surrender and reads `None`: the fight it left behind is the record.

    ⚠ THE SURRENDER RIDES ON THE RESULT, NOT IN THE BAND. A yielder is standing, so `combat_degree`'s
    shipped walk reads him `Untouched`/`Wounded` off his own `WoundTracker`; `combat_degree_bands` gains
    no value, because a yield sets no new quantity the band roster could be an edge over."""
    for e in trace:
        if e.get("kind") == "yield" and e.get("refused") is None:
            return dict(by=e["by"], turn=e["turn"], accepted=e["accepted"])
    return None


def party_end(person: Any, fx: Any) -> int:
    """A tracer `Person`'s ONE derived `Combatant` field, `end` (`H-97`); every other field is the
    class's own. Was `derive_party`, which built the `Combatant` too; since `31b` the module entry
    builds it from this number (`modules/combat/fight.py`)."""
    bands = body_band_penalty(person, fx)
    # `end`'s class default is 4 (combatant.py). One band = one point, floored at 1: a dying
    # person still fights, which is the same floor `decision.budget` applies for the same reason.
    default_end = 4
    return max(1, default_end - bands)


def combat_input(w: Any, claimants: list) -> PersonalCombatInput:
    """THE HOST INPUT BUILDER (plan position `31b`, A-25): `World` -> the frozen record the fight reads.

    Reads `w.persons` (the two claimants) and `w.fixtures`, and nothing else; the module that consumes
    the record never sees `World`. Its precondition is the adapter's PARTY-GAP checks (`resolve`,
    below): two claimants, both persons."""
    a_id, b_id = claimants[0], claimants[1]
    return PersonalCombatInput(
        claimants=(a_id, b_id),
        ends=(party_end(w.persons[a_id], w.fixtures), party_end(w.persons[b_id], w.fixtures)),
        wound_quantities=tuple(WOUND_QUANTITIES))


# ⚠ THE OUTCOME'S SEVERITY, READ OFF THE COMBATANTS THE SCENE JUST FOUGHT WITH (Jordan
# 2026-09-03). No number is invented and no rule is re-implemented: every field below is a
# property the engine's own `WoundTracker` computes, on the objects the module entry constructed
# and lifted before `fight()` collapsed the scene to an int (`modules/combat/fight.py`).
def _wound_state(lifted: Optional[dict]) -> dict:
    if lifted is None:                  # ID-5 polarity: absence REFUSES, it does not default
        return dict(available=False)
    # ⚠ THE FIELD LIST IS `rosters.yaml: wound_quantities`, NOT A LITERAL HERE (`H-98`, plan
    # position `8`) -- the same list `combat_band_edges` is validated against at load, so an
    # edge cannot name a quantity this does not lift. A member the tracker does not carry
    # REFUSES by name; skipping it would hand `combat_degree` a dict that lacks it.
    out = dict(available=True)
    for q in WOUND_QUANTITIES:
        if q not in lifted:
            raise Unspecified(
                f"`wound_quantities` lists {q!r} and the engine's WoundTracker has no such "
                f"field", "S39.4/H-98", needs=f"a `WoundTracker.{q}`, or delete it from "
                "rosters.yaml: wound_quantities and from every edge that reads it",
                law="Jordan 2026-09-03 -- the degree is READ OFF THE SCENE; a quantity the "
                    "scene does not carry cannot be lifted")
        v = lifted[q]
        out[q] = v if isinstance(v, bool) else int(v)
    return out


@provider("contest", _PROVIDER)
def resolve(w: Any, claimants: list, causes: list, prize: Any, *,
            verb: str = "", subject: Optional[str] = None,
            rng: Optional[random.Random] = None, rung: str = "") -> dict:
    """CALL the personal-combat engine. Returns what it said; decides nothing itself.

    ⚠ `rung` IS ACCEPTED AND NOT USED HERE, THE SAME DELIBERATE NON-CHANGE AS `rng` BELOW (M4,
    `ED-IN-0279` clause (a)). The seam's call is uniform; two duellists need no place to scope
    a derivation over.

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
    if len(claimants) < 2:
        # `combat_bridge.derive_parties` returns None on a derivation gap rather than faking a
        # side; the same rule, stated once more because the shape of the gap is different here.
        return dict(status="PARTY-GAP", why=f"personal combat needs two parties; got {len(claimants)}",
                    module=_PROVIDER)
    a_id, b_id = claimants[0], claimants[1]
    pa, pb = w.persons.get(a_id), w.persons.get(b_id)
    if pa is None or pb is None:
        return dict(status="PARTY-GAP", why=f"claimant not a person: {a_id!r} / {b_id!r}",
                    module=_PROVIDER)
    inp = combat_input(w, claimants)
    # `H` returns a blake2b hexdigest (`state/ids.py`), so 16 is the RADIX that parses it back to
    # an int for the RNG -- structural, not a game value. Pre-existing; surfaced because step 8's
    # `S.H(...)` -> `H(...)` lift rewrote the line and the gate scores added lines.
    # [JUSTIFIED: radix for parsing H()'s hex digest, not a mechanical constant]
    seed = int(H(w.world_seed, w.tick, a_id, f"contest:{prize}:{causes[0] if causes else ''}"), 16)
    entry, refusal = entry_for(prize, _PROVIDER)
    if entry is None:
        return refusal
    got = entry.fn(inp, random.Random(seed))
    result, trace = got["result"], got["trace"]
    winner = a_id if result == 1 else (b_id if result == -1 else None)

    _wounds = {a_id: _wound_state(got["wound_state"][a_id]), b_id: _wound_state(got["wound_state"][b_id])}

    return dict(status="RESOLVED", module=_PROVIDER, resolver="d_sigma",
                result=result, winner=winner,
                # THE DEGREE SOURCE. A caller reads severity from here; it does not map it from
                # `winner`, which carries none. `H-98`'s remaining half is which wound counts sit
                # in which band -- an edge over a real quantity, not an invented correspondence.
                wound_state=_wounds,
                # ⚠ `0` IS A RULED OUTCOME, NOT A FAILURE — Jordan, 2026-06-02, in the engine:
                # *"an undecided fight is a legitimate outcome."* The seam must not retry it into
                # a decision, which is what a caller expecting a winner would be tempted to do.
                unresolved=(result == 0),
                # §11.4: `None` unless a yield ended the scene; then a non-zero `result` with nobody felled.
                surrender=surrender_of(trace),
                bouts=sum(1 for e in trace if e.get("kind") == "turn_start"),
                # v9 PC-06 M-1 (#445 `05` M-1 / `03` S-4): THE SCENE'S OWN TRACE, AS THE MODULE ENTRY
                # CAPTURED IT, returned rather than reduced to `bouts` alone -- the read a grid display
                # or B-3's per-event measure plays the bout from. `bouts` above is its `turn_start`
                # count. Nothing here or downstream folds it into `World`: `contest()` hands this dict
                # to `_fold` as `Resolution.result`, whose effects read `result`/`wound_state`/
                # `parties` only, so `content_hash()` is unchanged
                # (`engine/season/tests/test_combat_trace_returned.py`).
                trace=trace,
                parties=got["ends"], seed=seed)
