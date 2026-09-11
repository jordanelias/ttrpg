"""One conviction name, checked against the single owner. `U3`.

⚠⚠ **THIS LIVES HERE AND NOT IN THE HARNESS THAT NEEDS IT, BECAUSE TWO GUARDS PULL OPPOSITE WAYS
AND ONLY ONE OF THEM IS WRONG ABOUT THIS CASE.**

  * `tests/valoria/test_conviction_roster_single_owner.py` fails on any literal holding two or more
    canonical conviction names, and demands they be READ from
    `references/descriptor_registry.yaml:conviction_roster` rather than retyped. It is right, and
    it is mutation-verified: three incompatible rosters once shipped at once and silently disabled
    ED-912 §6.1's Conviction Scar.
  * `test_w9_check4_no_effect_lambda_and_no_roster` asserts the substring `"roster"` never appears
    in `harness/headless.py`'s CODE, standing in for *artifact 2 must not author a roster*.

READING a roster is not AUTHORING one, and a substring scan cannot tell them apart. Rather than
spell around the second guard or widen it, the validator moves to the package that owns the
definition surface — which is where a "is this a real conviction?" question belonged anyway. The
harness calls `conviction("Precedent")` and names no roster at all, which is TRUE of it in the
sense that guard means.

⚠ IT VALIDATES AND DOES NOT TRANSLATE. `resolve_conviction`'s rule is that no legacy name is
silently migrated; this holds the same line one layer down. A name that is not canonical is a typo
or a rename, and both should stop the run rather than seed a person with a conviction
`CONVICTION_PROJECTION` has no row for.
"""
from __future__ import annotations

from ..gaps import Unspecified
from .rosters import CONVICTIONS


def conviction(name: str) -> str:
    """Return `name` if it is one of the thirteen; raise naming the roster if it is not."""
    if name not in CONVICTIONS:
        raise Unspecified(
            f"{name!r} is not a canonical Conviction", "descriptor_registry.yaml",
            needs=f"one of {sorted(CONVICTIONS)}",
            law="references/descriptor_registry.yaml:conviction_roster owns the thirteen; a "
                "harness chooses among them and may not mint one")
    return name
