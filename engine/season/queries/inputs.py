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

THREE RECORDS (plan positions `31a`, `31b`, `31c`). No OUTPUT type is minted: the providers return a `dict`,
and typing a `Margin` for one provider while the others return a dict would give the seam two
return shapes (`seam/wrappers/sigma.py`'s docstring, the placement question).
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class SocialContestInput:
    """What the `social_contest` module's σ-leverage roll reads, and nothing else.

    Built by `seam/wrappers/sigma.py::contest_input` (the host input builder) from `World`:
      * `pool`      -- dice, from what the actor genuinely has (`sigma.py::_pool_of`);
      * `ob`        -- what stands against it (`sigma.py::_obstacle_of`);
      * `obstacle_refusal_multiple` -- S27.4's multiple, the fixture the host adapter refuses on
                       before the entry is called (the module never sees a refused pair);
      * `leverage`  -- the σ-layer μ-shift. Zero until something supplies leverage: an `assumption`
                       reading with no producer, stated as zero rather than fabricated."""
    pool: int
    ob: float
    obstacle_refusal_multiple: float
    leverage: float


@dataclass(frozen=True)
class PersonalCombatInput:
    """What the `combat` module's fight reads, and nothing else (plan position `31b`).

    Built by `seam/wrappers/combat.py::combat_input` (the host input builder) from `World`:
      * `claimants` -- the two parties' ids, `(A, B)`: each is a `Combatant` label, and the engine's
                       result is `+1` when A wins, `-1` when B does, `0` UNRESOLVED (a ruled outcome);
      * `ends`      -- each party's one derived field, `end`, in `claimants` order
                       (`combat.py::party_end`, `H-97`); every other field is the class's own default;
      * `wound_quantities` -- the `WoundTracker` fields the host lifts per party after the fight
                       (`rosters.yaml: wound_quantities`, in roster order). The module reads them off the
                       trackers and returns what it found; the refusal for one the tracker does not carry
                       is the host's (`combat.py::_wound_state`)."""
    claimants: tuple
    ends: tuple
    wound_quantities: tuple


@dataclass(frozen=True)
class MassBattleInput:
    """What the `mass_battle` module's field reads, and nothing else (plan position `31c`).

    Built by `seam/wrappers/mass_battle.py::field_input` (the host input builder) from `World`, after
    the adapter's PARTY-GAP checks and its `Unopposed` branch (an empty defending side is never fought):
      * `weights`   -- `(attacker, defender)`, each a tuple of `Person.weight`, one per side member
                       `World` holds, in side order: the claimants, then the subject's members mustered
                       at the rung. The module sums each into its side's troops;
      * `territory` -- the geography territory id of the place fought over, or `None`
                       (`mass_battle.py::_territory_of`);
      * `fort_level` -- its fortification, `world_q.fortification_of`, in `[0.0, 1.0]`;
      * `stances`   -- `(attacker, defender)`: each side's weight-mean stance toward its own faction
                       (`mass_battle.py::_side_stance`), which the module turns into a morale-start;
      * `walls_dr`  -- the `field_walls_dr` fixture (`H-150`); `None` is A.9's own number, which the
                       module reads from its terrain table;
      * `origin`    -- the geography territory id the attacking side marched from, or `None` where it
                       has no one origin (`mass_battle.py::_origin_of`, MB-05r). The module decides from
                       it and `territory` whether the march crossed a river (`terrain.py::river_crossed`);
      * `loyalties` -- `(attacker, defender)`: each side's weight-mean build-time loyalty row, the
                       stance toward its faction creed's utterer (`mass_battle.py::_side_stance` with
                       `_creed_referent`, MB-03), which the module adds to the morale-start at
                       `loyalty_gain`;
      * `loyalty_gain` -- the `field_morale_loyalty_gain` fixture (`H-148`'s site); `0` is the control,
                       battle history only."""
    weights: tuple
    territory: Optional[str]
    fort_level: float
    stances: tuple
    walls_dr: Optional[int]
    origin: Optional[str]
    loyalties: tuple
    loyalty_gain: float
