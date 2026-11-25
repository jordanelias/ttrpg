"""`seam/wrappers/edge.py` -- THE `capability` SOURCE AND THE ONE READER OF A SITE'S NET SIGMA (B05.10, ADV Edit A, MAP §G edit 6; B10.15; B11.66).

A LEAF: it imports `data/`, `gaps`, `substrate` and the dice engine, and nothing of `epistemic` or `queries/`, which is why it is a file of its own. `sigma.py` (the
social roll's provider) imports `epistemic`, and `queries/cache.py` (which `epistemic` imports) builds the notice maps from a site's `edge` rows: the reader both
`loop/resolve.py::_crisis_net_sigma` and `cache.notice_edges` call lives here, so neither closes a loop through `sigma.py`. `sigma.py` re-binds the names it and its
importers (`combat.py`, `resolve.py`) read.
"""
from __future__ import annotations

import math
from typing import Any

from engine.dice_engine.sigma_leverage import levels_to_net_sigma
from engine.substrate import descriptors

from ...data.rosters import capability_rows, when_holds
from ...gaps import Unspecified

EDGE = "edge"                      # the operand key of the selected `edge` rows, beside `EFFORT`
CAPABILITY = "capability"          # the roster member (`rosters.yaml: advantage_sources`)


def _edge_scale(key: str) -> tuple:
    """`(floor, ceiling)` of the scale `key`'s value lives on: an attribute's or a practitioner stat's (`descriptors.scale_of`), a skill's own."""
    if key in descriptors.CAPABILITIES:
        row = descriptors.CAPABILITIES[key]
        return row.floor, row.ceiling
    return descriptors.scale_of(key)


def _edge_levels(row: Any, key: str, value: Any) -> tuple:
    """`(levels for the roller, levels against him)` of one selected row. The count is `per: held` 1 if held, `per: rank` the held rank,
    `per: mid` the signed WHOLE steps of the value from its scale's mid-point (an unauthored value IS the mid-point: zero steps; a
    half step is no step); `against: true` negates it; a positive count is that many copies of the row's `level` FOR the roller, a
    negative one that many AGAINST him."""
    if row.per == "held":
        n = 1 if value else 0
    elif row.per == "rank":
        n = int(value or 0)
    elif row.per == "mid":
        floor, ceiling = _edge_scale(key)
        mid = (floor + ceiling) / 2
        n = math.trunc((mid if value is None else value) - mid)
    else:
        raise Unspecified(f"an `edge` row at the social roll ({row.key!r}) has per {row.per!r}", "rosters.yaml -- tables: capability_uses",
                          needs="`per: held`, `per: rank` or `per: mid`", law="U1 §3 item 2 -- an edge row counts its held value one of three ways")
    n = -n if row.against else n
    return ([row.level] * n, []) if n > 0 else ([], [row.level] * -n)


def _capability_levels(fx: Any, operands: dict) -> tuple:
    """THE `capability` SOURCE: `(levels for the roller, levels against him)` summed over the act's selected `edge` rows
    (`operands[EDGE]`, chosen and read by the input builders). `([], [])` where the act brings none -- the shipped case."""
    for_, against = [], []
    for row, key, value in operands.get(EDGE, ()):
        f, a = _edge_levels(row, key, value)
        for_.extend(f)
        against.extend(a)
    return for_, against


def site_net_sigma(w: Any, p: Any, site: str) -> float:
    """THE NET SIGMA PERSON `p` BRINGS TO A ROLL AT THE `capability_use_sites` SITE `site` (B10.15 `crisis`; B11.66 `notice`): the site's `edge` rows (the shipped ones key
    a Spirit or a Perception, `per: mid`) are selected as the social roll's are (`when_holds`) and each read at the value `p` holds, summed by the ONE `edge` reader
    (`_capability_levels`, which `sigma.ADVANTAGE_SOURCES["capability"]` is) into named levels for or against him, and turned into a sigma by `levels_to_net_sigma`. A person who
    holds no value reads the scale's mid-point: no step. `0.0` where the site has no `edge` row. One body for every site: the site NAME is the only thing a caller varies."""
    reads = tuple((r, r.key, (p.attributes or {}).get(r.key)) for r in capability_rows(site) if r.role == "edge" and when_holds(r, p))
    return levels_to_net_sigma(*_capability_levels(w.fixtures, {EDGE: reads}))
