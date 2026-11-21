"""Shared builder for a hand-planted `FieldOutcome` (B17.03): what a test that folds a `march` on a CONSTRUCTED field puts under
a `Resolution`'s `result["result"]`, where the provider's real one stands. Each side is given as its survivors' fraction (the
float the planted tests used to write as `attacker_size_pct`), quantised onto the body scale the one way the module does
(`round(scale x fraction)`), so a planted `1.0` is exactly the scale and a planted `0.8` is `0.8 x scale`. Nothing here asserts.
"""
from __future__ import annotations

from ..data.fixtures import DEFAULT_FIXTURES
from ..queries.inputs import FieldOutcome, PartOutcome, SideOutcome

SCALE = DEFAULT_FIXTURES.get("condition_scale")


def side(fraction: float, *, routed: bool = False, conceded: bool = False, parts: tuple = (), broke_first=None,
         scale: int = SCALE) -> SideOutcome:
    """One side, `fraction` of it left, its `parts` given as `(id, fraction, routed)` triples."""
    return SideOutcome(share=round(scale * fraction), routed=routed, conceded=conceded,
                       parts=tuple(PartOutcome(i, round(scale * f), r) for i, f, r in parts), broke_first=broke_first)


def field_outcome(attacker: float = 1.0, defender: float = 1.0, *, attacker_out: bool = False, defender_out: bool = False,
                  attacker_parts: tuple = (), defender_parts: tuple = (), attacker_broke=None, defender_broke=None,
                  ended: str = "time", ticks: int = 18, scale: int = SCALE) -> FieldOutcome:
    """A field whose attacker has `attacker` of its troops left and whose defender has `defender`; a side that is `*_out`
    routed. The band is `field_degree`'s read of the two flags, never passed in."""
    return FieldOutcome(
        ended=ended, ticks=ticks,
        attacker=side(attacker, routed=attacker_out, parts=attacker_parts, broke_first=attacker_broke, scale=scale),
        defender=side(defender, routed=defender_out, parts=defender_parts, broke_first=defender_broke, scale=scale))
