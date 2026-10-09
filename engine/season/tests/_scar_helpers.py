"""Shared builders for the IN-08 scar tests (H3, H11, H13) and their neighbours (G4, 6f).

Each was copied verbatim between test files; this is the one copy. A test's own planted world stays
in its own file -- the three `_world`s differ in what they plant, which is the point of each test.
Nothing here asserts anything.
"""
from __future__ import annotations

import itertools

from ..data import affiliations as A
from ..data.matrix import WriteClass
from ..data.rosters import AFFILIATIONS, WOUNDED
from ..loop.driver import SeasonDriver, mint_token
from ..seam import Resolution
from ..state.carriers import Act


def wounded(victim="p_mid", full=10, left=5) -> Resolution:
    """A `WOUNDED` scene result leaving `victim` at `left` of `full` health."""
    return Resolution(WOUNDED, {"wound_state": {victim: {"health_full": full,
                                                         "health_remaining": left}}})


def fight(w, aid: str):
    """`p_low` fights `p_mid` and is `wounded()`: the Act folded through the real driver's `_fold`
    with an ACTS token. Returns the Events the fold emits."""
    return SeasonDriver(w)._fold(w, mint_token(w, WriteClass.ACTS),
                                 Act(id=aid, actor="p_low", verb="fight",
                                     payload={"subject": "p_mid"}),
                                 wounded())


def scars(w) -> dict:
    """`{pid: scar}` for every person holding a scar count."""
    return {pid: dict(p.scar) for pid, p in w.persons.items() if p.scar}


def rebound(**cells) -> dict:
    """The loaded engagement table with `cells` laid over it: `{column: {verb: value}}`."""
    out = {col: dict(row) for col, row in A.ENGAGEMENT.items()}
    for col, row in cells.items():
        out.setdefault(col, {}).update(row)
    return out


def incompatible_pairs() -> list:
    """Every loaded `incompatible` pair, each as a name-sorted tuple, in name order."""
    return sorted(tuple(sorted(pair)) for pair in A.INCOMPATIBLE)


def compatible_pairs() -> list:
    """Every rostered pair NOT in `incompatible`, as name-sorted tuples, in name order."""
    return [pr for pr in itertools.combinations(sorted(AFFILIATIONS), 2)
            if frozenset(pr) not in A.INCOMPATIBLE]
