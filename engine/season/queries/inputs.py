"""`queries/inputs.py` -- THE TYPED INPUT RECORDS the host builds for a module entry (A-25).

A-25 (`ED-IN-0284`, revised by `ED-IN-0285`): a verb is a loop-side ADAPTER. The host builds a typed
INPUT record from what `World` holds, calls the module ENTRY (a composition row carrying `entry:`,
registered in `manifest.MODULE_ENTRIES`) and interprets what comes back. A module never reads or
writes `World`; it reads the record. The record types live HOST-side, here, where projections are
built, and a module imports them -- it depends upward on `engine/`, and the host reaches the module
only by string.

⚠ THIS FILE IS A LEAF: stdlib only, and it imports nothing from the season package. A module that
imports a record type must pull in nothing else of the host
(`engine/season/tests/test_social_contest_module.py` observes it in a fresh process); a record type
placed beside a builder that reads `data/` would drag the registries into every module.

ONE RECORD TODAY (plan position `31a`). No OUTPUT type is minted: the providers return a `dict`,
and typing a `Margin` for one provider while the others return a dict would give the seam two
return shapes (`seam/wrappers/sigma.py`'s docstring, the placement question).
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class SocialContestInput:
    """What the `social_contest` module's σ-leverage roll reads, and nothing else.

    Built by `seam/wrappers/sigma.py::contest_input` (the host input builder) from `World`:
      * `claimants` -- the contest's claimant ids, the first the actor (S39.1: persons, always);
      * `pool`      -- dice, from what the actor genuinely has (`sigma.py::_pool_of`);
      * `ob`        -- what stands against it (`sigma.py::_obstacle_of`);
      * `obstacle_refusal_multiple` -- S27.4's multiple, the fixture the host adapter refuses on
                       before the entry is called (the module never sees a refused pair);
      * `leverage`  -- the σ-layer μ-shift. Zero until something supplies leverage: an `assumption`
                       reading with no producer, stated as zero rather than fabricated."""
    claimants: tuple
    pool: int
    ob: float
    obstacle_refusal_multiple: float
    leverage: float
