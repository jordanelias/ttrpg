"""modules.mass_battle.troop_types.recruitment -- how many troops of a type a place can raise (ED-IN-0306, phase 2).

Jordan, 2026-10-28, on the gap between a season cohort (a weight of single or double digits) and the battle engine
(calibrated for hundreds of troops): *"you can invent one that makes sense. basically the more population the more
troops possible, but you also need to have infrastructure built to train troops and specific infrastructure for
specific kinds of troops."* This module is that rule, as pure functions over plain values. It reads no `World`; the
season host passes in a rung's population and its training Sites' conditions.

THE RULE.
  * POPULATION BOUNDS THE ARMY. A place of weight `w` holds `w * TROOPS_PER_WEIGHT` people, and at most
    `MUSTER_FRACTION` of them can be under arms at once (`under_arms_cap`).
  * INFRASTRUCTURE BOUNDS EACH KIND. A troop type is trained at one KIND of Site (`TRAINING_SITE`); the Site's
    condition, as a fraction of full, is the share of the under-arms cap that type may reach, so a half-built
    archery range trains half the archers a full one does. A type listed with a minimum condition is not trained
    at all below it. Levy is the exception that proves the rule: the call-up of ordinary people needs no training
    ground, so it has no entry and is bounded by population alone.
  * THE TWO BOUNDS COMPOSE: a type's room is the smaller of its own site share and what the whole under-arms cap
    leaves after every troop already raised there.

`recruit_limit` is the whole answer for one type at one place. The verb that spends it (`recruit`) and the Site kinds
it reads (`rosters.yaml: site_kinds`) are `engine/season/`'s; the numbers and the type -> site table are here, beside
the troop stats, so a troop type is defined once.

[canonical: none -- every number below is an ASSUMPTION of ED-IN-0306 (Jordan: "you can invent one that makes
sense"), medium confidence, Jordan to correct; revert: set MUSTER_FRACTION to 1.0 and TRAINING_SITE to {} and a place
raises any type up to its whole population.]
"""
from __future__ import annotations

import math
from typing import Mapping, Optional

from modules.mass_battle.troop_types.registry import stats_for

__all__ = ['TROOPS_PER_WEIGHT', 'MUSTER_FRACTION', 'TRAINING_SITE', 'training_site_for', 'under_arms_cap',
           'recruit_limit']

#: People per unit of `Person.weight`. One weight is a hamlet of three hundred. It is set by what the engine can fight
#: with, not by a census: a unit under `Unit.recalc_size`'s 100-troop block routs at once, `config.TROOPS_PER_TIER` runs
#: 100..800 for a field army, and the shipped realm holds 120 weight in all (the Crown 30, Hafenmark and Varfell 20 each,
#: the Church 2). At 300 and a tenth under arms the Crown can raise 900, a middling faction 600, and the Church 60 --
#: a garrison, which routs in the open and should. At the first writing's 100 the Crown's best was 300 and a town's
#: cohort (weight 2) 20, which no field could use. [ASSUMPTION; medium; Jordan to correct; revert: 100.]
TROOPS_PER_WEIGHT = 300  # [canonical: ED-IN-0306 -- ASSUMPTION, Jordan: "you can invent one"; sized to the engine's 100-troop unit floor and 100..800 field armies, ED-IN-0306 phase 5]

#: The share of a place's people that can be under arms at once. A tenth is the usual ceiling of pre-industrial
#: mobilisation (the able-bodied men of military age are about a fifth of a population, and half of those is a hard
#: draw on it), and at `TROOPS_PER_WEIGHT` it lands a weight-12 cohort at 360 troops, well clear of `config.SUBUNIT_ROUT_FLOOR`.
MUSTER_FRACTION = 0.10  # [canonical: ED-IN-0306 -- ASSUMPTION, pre-industrial mobilisation ceiling; Jordan to correct]

#: troop type -> (the Site kind it is trained at, the least condition fraction at which that Site trains it at all).
#: Drawn from the unit classes Romance of the Three Kingdoms and Total War share: foot soldiers drill at a barracks,
#: missile troops at a range, horse at a stable, engines at a workshop. The elite entries need a Site at least half
#: built. A type absent from this table (levy) needs no Site.
TRAINING_SITE = {
    'light_infantry':  ('barracks',       0.0),
    'spearmen':        ('barracks',       0.0),
    'heavy_infantry':  ('barracks',       0.0),
    'pike':            ('barracks',       0.0),
    'archers':         ('archery_range',  0.0),
    'crossbow':        ('archery_range',  0.0),
    'sling':           ('archery_range',  0.0),
    'skirmishers':     ('archery_range',  0.0),
    'cavalry':         ('stable',         0.0),
    'light_cavalry':   ('stable',         0.0),
    'mounted_archers': ('stable',         0.0),
    'knights_templar': ('stable',         0.5),
    'artillery':       ('siege_workshop', 0.5),
}  # [canonical: ED-IN-0306 -- ASSUMPTION: the type -> site pairing and the 0.5 elite floor are this module's, from the RTK / Total War unit classes; Jordan to correct]


def training_site_for(troop_type: str) -> Optional[tuple]:
    """`(site_kind, min_condition_fraction)` the type is trained at, or `None` for a type needing no Site (levy).
    Case-insensitive, as `stats_for`."""
    return TRAINING_SITE.get(str(troop_type).strip().lower())


def under_arms_cap(weight: float) -> int:
    """Most people a place of population `weight` can hold under arms at once."""
    return int(math.floor(max(0.0, weight) * TROOPS_PER_WEIGHT * MUSTER_FRACTION))


def recruit_limit(troop_type: str, weight: float, site_conditions: Mapping[str, float], raised: Mapping[str, int],
                  full: float) -> int:
    """How many MORE troops of `troop_type` the place can raise now.

    `weight` -- the place's population (`world_q.population`). `site_conditions` -- the best Site condition the
    place has for each kind (`{site_kind: condition}`, a kind it has none of absent or 0). `raised` -- troops
    already under arms there, by type (every type counts against the population cap; only `troop_type` against its
    own site share). `full` -- the condition scale (`condition_scale`); a Site at `full` is a complete one.
    Never negative. An unknown type raises ValueError, so a typo is not read as "needs no Site"."""
    if stats_for(troop_type) is None:
        raise ValueError(f"unknown troop type {troop_type!r}")
    if not full > 0:
        raise ValueError(f"full must be positive, got {full!r}")
    cap = under_arms_cap(weight)
    room_total = cap - sum(int(n) for n in raised.values())
    site = training_site_for(troop_type)
    if site is None:
        # Levy has no Site, so its own count is the whole of what it shares.
        share, kind_types = cap, {str(troop_type).strip().lower()}
    else:
        kind, floor = site
        frac = max(0.0, min(1.0, float(site_conditions.get(kind, 0.0)) / float(full)))
        share = 0 if frac <= 0.0 or frac < floor else int(math.floor(cap * frac))
        # The Site is shared by every type trained at its kind: a quarter-built barracks trains a quarter of the cap
        # BETWEEN its types, not a quarter each.
        kind_types = {t for t, (k, _f) in TRAINING_SITE.items() if k == kind}
    room_type = share - sum(int(n) for t, n in raised.items() if str(t).strip().lower() in kind_types)
    return max(0, min(room_total, room_type))
