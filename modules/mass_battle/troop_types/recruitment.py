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

from modules.mass_battle.troop_types import table as _table
from modules.mass_battle.troop_types.registry import stats_for

__all__ = ['TROOPS_PER_WEIGHT', 'MUSTER_FRACTION', 'TRAINING_SITE', 'training_site_for', 'under_arms_cap',
           'recruit_limit']

#: People per unit of `Person.weight`. One weight is ten thousand people, so a tenth under arms (`MUSTER_FRACTION`) is a
#: thousand troops a weight: `config.MIN_ARMY_TROOPS`, the least an army is (ED-MB-0101, Jordan, 2026-11-20: "i expect
#: armies to be a minimum of 1000 troops"; "typically ... 5000 to 10000"). The weight is the floor and a heavier side is
#: a multiple of it; `massbattle` splits what a side raises into units of at most `config.MAX_TROOPS_PER_UNIT`. A weight
#: under one is a place that cannot raise an army: it fields fewer than the floor and the form-time warning says so.
#: [ASSUMPTION; medium; Jordan to correct; revert: 300 (the 100-troop unit floor's scale, ED-IN-0306).] The ruling fixes the floor, not this constant.
TROOPS_PER_WEIGHT = 10_000  # [ASSUMPTION: sized so one weight at MUSTER_FRACTION raises ED-MB-0101's 1,000-troop floor; whether the floor or the typical battle sets it is Jordan's open question, ED-MB-0101's last row]

#: The share of a place's people that can be under arms at once. A tenth is the usual ceiling of pre-industrial
#: mobilisation (the able-bodied men of military age are about a fifth of a population, and half of those is a hard
#: draw on it), and at `TROOPS_PER_WEIGHT` it lands a weight-12 cohort at 12,000 troops, clear of `config.UNIT_ROUT_FLOOR` and over one unit's ceiling, so it is several units.
MUSTER_FRACTION = 0.10  # [canonical: ED-IN-0306 -- ASSUMPTION, pre-industrial mobilisation ceiling; Jordan to correct]

#: troop type -> (the Site kind it is trained at, the least condition fraction at which that Site trains it at all).
#: Drawn from the unit classes Romance of the Three Kingdoms and Total War share: foot soldiers drill at a barracks,
#: missile troops at a range, horse at a stable, engines at a workshop. The elite entries need a Site at least half
#: built. A type absent from this table (levy) needs no Site. [B17.10] The pairing is the troop file's `training_site` and
#: `min_site_condition` columns (`references/troops.yaml`, read by `troop_types/table.py`); this table is that file read as one.
#: [canonical: ED-IN-0306 -- ASSUMPTION: the type -> site pairing and the 0.5 elite floor are the troop file's, from the RTK / Total War unit classes; Jordan to correct]
TRAINING_SITE = _table.training_sites()


def training_site_for(troop_type: str) -> Optional[tuple]:
    """`(site_kind, min_condition_fraction)` the type is trained at, or `None` for a type needing no Site (levy).
    Case-insensitive, as `stats_for`."""
    return _table.training_site_for(troop_type)


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
