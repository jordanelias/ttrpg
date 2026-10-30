"""PRESET ORDERS OF BATTLE FOR THE FACTIONS NOBODY PLAYS (ED-IN-0306 phase 5c).

    from engine.season.harness.army_presets import install
    kinds = install(w, ["fac_crown", "fac_hafenmark"])         # {faction: the event kinds the fold produced}

A faction with no player still needs an army when the battle looks for one. `install` gives it the one the module's
doctrine builds from what it can raise (`modules/mass_battle/troop_types/presets.py`, reached by the `mass_battle.army_preset`
row): the faction's leader mints the army, then gives the same six commands a player would -- `recruit`, `form_unit`,
`assign_troops` -- through the real fold, so every limit (the cohort's cap, the Site, who governs the cohort)
is the verbs' own and a refusal is a refusal. The plan is deterministic: it draws nothing.

⚠ SHIPPED OFF BY CONSTRUCTION. Nothing in the season loop, the harness `run` functions or the corpus calls this; a caller
has to. So no seeded run moves, and no `Fixtures` flag is needed (the `field_provisioning` precedent needs a flag only
because that arm sits INSIDE the loop). Turning it on for a run is the caller's one line, before the first season; a
sweep arm that did so would be a declared hash-moving commit of its own.

⚠ IT SPENDS NO PERSON'S BUDGET. The commands are folded directly, between seasons, as the hand-built acts the army verbs
are (`loop/effects_army.py`), not offered through DELIBERATE. That is the difference from the menu's `callback`, which a
client uses within a season. NAMED LIMITS: who marches where is MB-08's, so the army exists and does not yet move itself;
a realm with no barracks, range or stable raises levy alone, which holds a line and cannot press an attack.
"""
from __future__ import annotations

from typing import Iterable, Optional

from engine.substrate import composition

from ..data.matrix import WriteClass
from ..data.rosters import FACTION_BY_PROP
from ..loop.driver import SeasonDriver, mint_token
from ..loop.effects_information import _army_mintable
from ..queries import world_q
from ..queries.inputs import ArmyPresetQuery
from ..state.carriers import Act
from . import military_menu

__all__ = ["install", "plan_for"]


def _fold(w, driver: SeasonDriver, act: Act) -> list:
    """One hand-built act through RESOLVE, its Events appended to the log as the season loop appends a round's. The world's
    step and freeze are put back, since this runs between seasons and not inside one."""
    step, frozen = w.step, w.frozen
    try:
        ev = driver.resolve(mint_token(w, WriteClass.ACTS), [act], 2)
        w.log.extend(ev)
    finally:
        w.step, w.frozen = step, frozen
    return [e.kind for e in ev]


def _commander(w, faction: str) -> Optional[str]:
    """The first leader of `faction` (id order) who may mint its army, or None."""
    empty = military_menu._empty_army(faction)
    return next((p for p in world_q.leaders(w, faction) if _army_mintable(w, p, empty)), None)


def plan_for(w, faction: str) -> tuple:
    """The commands the doctrine gives `faction` now, `((verb, payload), ...)`, without folding any. Every army already in
    the world counts against the cohorts: the plan is for an army that does not exist yet."""
    return composition.require(world_q.ARMY_PRESET)(ArmyPresetQuery(
        faction, military_menu.cohorts_raisable(w, faction), w.fixtures.get("condition_scale"),
        world_q.other_army_records(w, "")))


def install(w, factions: Optional[Iterable[str]] = None, strategy: str = "line") -> dict:
    """Mint and organise an army for each faction in `factions` (default: every faction the world holds a Proposition for)
    that has none and has a leader who may mint one. Returns `{faction: (event kind, ...)}` for the factions it acted for,
    in the order the commands were folded; a faction with no army, no leader or nothing it can raise is absent. Mutates
    `w` through the fold only."""
    driver = SeasonDriver(w)
    out: dict = {}
    for faction in (list(factions) if factions is not None else sorted(f for f in FACTION_BY_PROP if f in w.propositions)):
        if faction not in FACTION_BY_PROP or world_q.army_of(w, faction) is not None:
            continue
        who = _commander(w, faction)
        if who is None:
            continue
        commands = plan_for(w, faction)
        if not commands:
            continue                                     # nothing to raise: no empty army is minted for nothing
        kinds = _fold(w, driver, military_menu.act_for(w, who, "create_record", strategy=strategy))
        rid = world_q.army_of(w, faction)
        if rid is None:                                  # the mint was refused; the kinds say why
            out[faction] = tuple(kinds)
            continue
        for verb, payload in commands:
            kinds += _fold(w, driver, military_menu.act_for(w, who, verb, **payload))
        out[faction] = tuple(kinds)
    return out
