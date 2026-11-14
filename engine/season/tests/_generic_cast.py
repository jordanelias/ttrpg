"""THE GENERIC TEST CAST (B01a.03; Jordan 2026-11-13/14: no tuning to everyone scoring 2). A realm test needs
nothing from here: `build_realm(seed)` seats the drawn sheets, and a test at another seed draws others. A test
that BUILDS ITS OWN PERSONS (`probes.tiny_world`, a hand-built world) and whose subject reads an attribute in any
form seats this cast, so it runs against generated attributes, not an empty sheet. A test that needs a FIXED
value (a planted edge, a mirror, an authored row's comparison) asks for it here, by `fixed`, and says why in
its own docstring: the fixed value is the test's subject, the rest of the sheet stays drawn.

Test support only: nothing but tests reads it. Nothing here asserts anything.
"""
from __future__ import annotations

from engine.substrate.descriptors import ATTRIBUTES

from ..gaps import Forbidden
from ..state.carriers import generated_attributes


def seat_generic_cast(w, *, seed: int | None = None, fixed: dict | None = None):
    """Every person of `w` with an empty sheet gets `generated_attributes(seed if seed is not None else
    w.world_seed, pid, w.fixtures.get("generated_attribute_range"))`; then `fixed`, `{pid: {registry key:
    value}}`, over it, key by key. Returns `w`. Refuses a key outside `ATTRIBUTES`."""
    for pid, keys in (fixed or {}).items():
        for key in keys:
            if key not in ATTRIBUTES:
                raise Forbidden(f"`seat_generic_cast` fixed value for {pid!r}: {key!r} is none of the ten attributes",
                                "engine/season/tests/_generic_cast.py",
                                needs="a key of engine.substrate.descriptors.ATTRIBUTES",
                                law="B01a.03 -- a fixed value replaces its own key of the drawn sheet")
    span = w.fixtures.get("generated_attribute_range")
    s = w.world_seed if seed is None else seed
    for pid, p in w.persons.items():
        if not p.attributes:
            p.attributes = generated_attributes(s, pid, span)
        if pid in (fixed or {}):
            p.attributes = {**p.attributes, **fixed[pid]}
    return w
