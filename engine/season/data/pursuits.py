"""One conviction name, checked against the single owner. `U3`.

⚠⚠ **THIS LIVES HERE AND NOT IN THE HARNESS THAT NEEDS IT, BECAUSE TWO GUARDS PULL OPPOSITE WAYS
AND ONLY ONE OF THEM IS WRONG ABOUT THIS CASE.**

  * `tests/valoria/test_conviction_roster_single_owner.py` fails on any literal holding two or more
    canonical pursuit names, and demands they be READ from
    `references/descriptor_registry.yaml:pursuit_roster` rather than retyped. It is right, and
    it is mutation-verified: three incompatible rosters once shipped at once and silently disabled
    ED-912 §6.1's Conviction Scar.
  * `test_w9_check4_no_effect_lambda_and_no_roster` asserts the substring `"roster"` never appears
    in `harness/headless.py`'s CODE, standing in for *artifact 2 must not author a roster*.

READING a roster is not AUTHORING one, and a substring scan cannot tell them apart. Rather than
spell around the second guard or widen it, the validator moves to the package that owns the
definition surface — which is where a "is this a real pursuit?" question belonged anyway. The
harness calls `pursuit("stability")` and names no roster at all, which is TRUE of it in the
sense that guard means.

⚠ IT VALIDATES AND DOES NOT TRANSLATE. `resolve_pursuit`'s rule is that no legacy name is
silently migrated; this holds the same line one layer down. A name that is not canonical is a typo
or a rename, and both should stop the run rather than seed a person with a pursuit
`PURSUIT_PROJECTION` has no row for.

⚠ IN-08's CELLS COMMIT (`ED-IN-0261`): it validates against the substrate's fifteen-name leaf
(`engine.substrate.descriptors.PURSUITS`/`resolve_pursuit`), projected through the 15×7
`tables.pursuit_projection`.
"""
from __future__ import annotations

import math
from typing import Optional

from ..gaps import Unspecified
from engine.substrate.descriptors import resolve_pursuit

from .rosters import PURSUITS


def pursuit(name: str) -> str:
    """Return `name` if it is one of the fifteen; raise naming the roster if it is not.

    ⚠ IT DELEGATES. `engine.substrate.descriptors.resolve_pursuit` already IS this check, against
    the same tuple, with a fuller message that names the canonical fifteen and explains what a
    LEGACY tag should do instead. A first writing of this function re-did the membership test with a
    shorter message — a second "is this a real pursuit?" in the tree, which is the exact shape
    `test_conviction_roster_single_owner.py` exists to prevent one level up. What is season-specific
    is the EXCEPTION TYPE, not the rule: this package refuses with `Unspecified` so a caller catching
    the season's own gap type sees it, and `resolve_pursuit` raises `ValueError`. So the check is
    borrowed and only the wrapper is local."""
    try:
        return resolve_pursuit(name)
    except ValueError as exc:
        raise Unspecified(
            f"{name!r} is not a canonical pursuit", "descriptor_registry.yaml",
            needs=f"one of {sorted(PURSUITS)}",
            law=str(exc)) from exc


def to_axes(weights: dict) -> dict:
    """A weighted pursuit map, projected into the seven bipolar axes. THE ONE OWNER.

    `Σ_p weight[p] · projection[p][axis]`, over `references/descriptor_registry.yaml`'s
    fifteen and `rosters.yaml: tables.pursuit_projection`'s 15×7.

    ⚠ IT TAKES A DICT, NOT A `Person`, AND THAT IS WHY IT IS HERE RATHER THAN IN `decision/`.
    `decision.choose.project` was the only projector and its signature is `Person -> dict`, so a
    caller wanting to project anything ELSE — a role template's EXPECTED conviction vector, say —
    had to re-derive the loop. Two owners of *convictions → axes* is `§8` exactly. `project` now
    calls this, so the rule lives once and the Person-shaped convenience stays where it was.

    ⚠ IT LIVES IN `data/`, NOT `decision/`, BECAUSE OF THE IMPORT ARROW. `decision/` already imports
    `data/`; the reverse would be a cycle, and `data.cast` needs this to weigh a person against
    their faction's expectations.

    ⚠ A CONVICTION THE MATRIX DOES NOT LIST PROJECTS TO NOTHING — the sparse default, not a silent
    drop: the roster check has already refused any name outside the canonical fifteen.
    `role_template_pursuits` is the one caller whose names `pursuit()` never sees, so its cells are
    checked against the roster at load (`data/verbs.py::ROLE_TEMPLATE_PURSUITS`)."""
    from .rosters import PURSUIT_AXES
    from .verbs import PURSUIT_PROJECTION, PROJECTION_DEFAULT_CELL
    out = {ax: 0.0 for ax in PURSUIT_AXES}
    for conv, w in (weights or {}).items():
        row = PURSUIT_PROJECTION.get(conv)
        if row is None:
            continue
        for ax in PURSUIT_AXES:
            out[ax] += float(w) * float(row.get(ax, PROJECTION_DEFAULT_CELL))
    return out


def alignment(weights_a: dict, weights_b: dict) -> Optional[float]:
    """HOW FAR TWO WEIGHTED PURSUIT MAPS POINT THE SAME WAY, `[-1, +1]`: the cosine of their `to_axes`
    projections. THE ONE OWNER (v9 IN-69, `CLAUDE.md` §8) -- `cast.loyalty` (a person against his
    faction's role template, mapped onto `0..100`) and `world_q.attention_key` (a person against an
    organization's expected vector, ordering the ambition he answers first) both call it: the FORMULA has
    one owner. The INPUTS differ by design -- `loyalty` reads the registry row's raw pursuits at
    world-gen, salience reads `person_q.crisis_weights` (scars, IN-71's doctrine scaling) at read time.

    `+1` is the same direction, `0` is orthogonal (neither is about anything the other holds), `-1` is
    opposed. `None` when either side projects to the zero vector: a map with no ethics has no direction
    to compare, and `None` is the refusal rather than a default of `0`, which would be a claim of
    indifference. Each caller decides what an absent reading means for it.

    ⚠ IT PROJECTS FIRST (`data/cast.py::loyalty` records why): two maps can share no pursuit name and
    still point the same way ethically, and the cosine over the fifteen names would score them `0`.
    ⚠ IT LIVES HERE, NOT IN `person_q`, BECAUSE IT TAKES WEIGHTS: `data/` imports no `queries/`
    module and `cast.loyalty` holds a registry row, not a Person.
    (Unrelated: `decision/` has a verb-axis table named `alignment`; that is a different quantity.)"""
    mine, theirs = to_axes(weights_a), to_axes(weights_b)
    # SORTED: `PURSUIT_AXES` is a frozenset, so a sum in set order would give a float whose low bits move
    # with PYTHONHASHSEED, and this value is a sort key (`world_q.attention_key`); `person_q._lean` sorts
    # its axes for the same reason.
    axes = sorted(set(mine) | set(theirs))
    dot = sum(mine.get(a, 0.0) * theirs.get(a, 0.0) for a in axes)
    na = math.sqrt(sum(mine.get(a, 0.0) ** 2 for a in axes))
    nb = math.sqrt(sum(theirs.get(a, 0.0) ** 2 for a in axes))
    if not na or not nb:
        return None
    return max(-1.0, min(1.0, dot / (na * nb)))
