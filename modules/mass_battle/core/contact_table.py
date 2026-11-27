"""modules.mass_battle.core.contact_table -- the measured felling chances the contact draw reads, by log-odds interpolation.

The head is the measured duel table `references/mb_contact/duel_grid.json` (written by `tools/calibrate_mb_contact.py`, which runs the
duel engine); `tools/export_mb_contact.py` cooks it, with the troop file, into `engine/engine_params/mb_contact.json` (the port's) and
`contact_table_data.py` beside this module (the same document as a Python literal). This module reads the second, once, on first use.
It imports no `engine` code and nothing from `modules.combat`: a registered module opens no file (A-25) and names no other
subsystem, so the duel engine reaches the game only through the table. A stale table is refused where a file may be opened, by the
exporter's `--check` (its fingerprint arm), never here.

A FELLING CHANCE `h` is the chance a defender's man is taken out of the fight (felled, or yielding) in one duel round, given that
round was fought. A FIGHTER TYPE is `(arm, armour, skill)`, `arm` a duel weapon key (the troop file's `arms.<key>.duel_key`, or a
missile arm's `sidearm`), `armour` one of the troop file's tiers, `skill` the men's martial skill. The table's grid holds skill 1, 3
and 5 and round index 1..K; every other skill and round is read by interpolation, LINEAR IN LOG-ODDS: on the attacker's skill, then
the defender's, then the round. A skill outside [1, 5] and a round outside [1, K] are refused (the table holds nothing to
interpolate toward; an extrapolation would be a guess).

[ASSUMPTION: the signature is `felling_chance(arm_a, armour_d, skill_a, skill_d, rounds_d, *, arm_d, armour_a)`, the two keyword-only
arguments REQUIRED -- basis: the table is keyed on the whole ordered pair of fighter types, `(arm_a, armour_a, skill_a)` against
`(arm_d, armour_d, skill_d)`; the plan's five names omit the defender's arm and the attacker's armour, and a chance marginalised over
either is undefined (it would need a distribution over what the other side carries, which this module does not hold). Every other
argument is as the plan names it (MBA §2.2). A caller (B19's vector builder) carries all seven. Reversible: this signature.]

[ASSUMPTION: `beta` is read per step of the ATTACKER's skill, at the pair, and interpolated linearly across skills -- basis: the
exporter's docstring; the contact draw's levels (in skill steps) move `logit(h)` by `beta` each, one ladder.]
"""
from __future__ import annotations

import functools
import math

__all__ = ['felling_chance', 'beta', 'flags', 'status', 'rounds_k', 'GRID_SKILLS']

GRID_SKILLS = (1, 3, 5)
_EPS = 1e-6        # logit's clamp: a chance of 0 or 1 is read as _EPS or 1 - _EPS


@functools.lru_cache(maxsize=None)
def _data() -> dict:
    """The exported document, imported once, on first use. The exporter's `--check` pins it equal to the JSON."""
    from modules.mass_battle.core.contact_table_data import DATA
    return DATA


def rounds_k() -> int:
    """`K`, the last round index the table holds."""
    return _data()['K']


def _logit(p: float) -> float:
    p = min(max(p, _EPS), 1 - _EPS)
    return math.log(p / (1 - p))


def _expit(x: float) -> float:
    return 1 / (1 + math.exp(-x))


def _bracket(x: float, what: str) -> tuple:
    """`(i, j, t)`: the grid skills either side of `x` and its place between them (`t` in [0, 1]); refuses `x` outside the grid's span."""
    if not GRID_SKILLS[0] <= x <= GRID_SKILLS[-1]:
        raise ValueError(f'{what} {x!r} is outside the table\'s [{GRID_SKILLS[0]}, {GRID_SKILLS[-1]}]')
    i = max(g for g in GRID_SKILLS if g <= x)
    j = min(g for g in GRID_SKILLS if g >= x)
    return i, j, 0.0 if i == j else (x - i) / (j - i)


def _pair(arm_a, armour_a, skill_a, arm_d, armour_d, skill_d) -> dict:
    key = f'{arm_a}/{armour_a}/{skill_a}>{arm_d}/{armour_d}/{skill_d}'
    try:
        return _data()['pairs'][key]
    except KeyError:
        raise ValueError(f'the table has no pair {key!r} (arms {sorted({k.split("/")[0] for k in _data()["pairs"]})}, '
                         f'skills {GRID_SKILLS})') from None


def _over_skills(arm_a, armour_a, skill_a, arm_d, armour_d, skill_d, read) -> float:
    """`read(pair)` (a logit) interpolated linearly over the attacker's skill and then the defender's."""
    a0, a1, ta = _bracket(skill_a, 'skill_a')
    d0, d1, td = _bracket(skill_d, 'skill_d')

    def along_a(sd):
        x0 = read(_pair(arm_a, armour_a, a0, arm_d, armour_d, sd))
        x1 = x0 if a1 == a0 else read(_pair(arm_a, armour_a, a1, arm_d, armour_d, sd))
        return x0 + ta * (x1 - x0)

    y0 = along_a(d0)
    y1 = y0 if d1 == d0 else along_a(d1)
    return y0 + td * (y1 - y0)


def felling_chance(arm_a: str, armour_d: str, skill_a: float, skill_d: float, rounds_d: float, *, arm_d: str, armour_a: str) -> float:
    """The chance the defender's man is felled in a duel round, `rounds_d` in `[1, K]` rounds since he was fresh, by log-odds
    interpolation on both skills and on the round. The grid's points are returned as stored."""
    K = rounds_k()
    if not 1 <= rounds_d <= K:
        raise ValueError(f'rounds_d {rounds_d!r} is outside the table\'s [1, {K}]')
    r0 = min(int(rounds_d), K - 1) if K > 1 else 1      # the round index below `rounds_d` (the last pair's lower one at K)
    r1 = min(r0 + 1, K)
    tr = rounds_d - r0 if r1 > r0 else 0.0
    x0 = _over_skills(arm_a, armour_a, skill_a, arm_d, armour_d, skill_d, lambda p: _logit(p['h'][r0 - 1]))
    x1 = x0 if r1 == r0 else _over_skills(arm_a, armour_a, skill_a, arm_d, armour_d, skill_d, lambda p: _logit(p['h'][r1 - 1]))
    return _expit(x0 + tr * (x1 - x0))


def beta(arm_a: str, armour_d: str, skill_a: float, skill_d: float, *, arm_d: str, armour_a: str) -> float:
    """The change in `logit(h_1)` per skill step at the pair (the exporter's docstring says how it is measured), interpolated
    linearly across the grid's skills."""
    return _over_skills(arm_a, armour_a, skill_a, arm_d, armour_d, skill_d, lambda p: p['beta'])


def flags(arm_a: str, armour_d: str, skill_a: float, skill_d: float, *, arm_d: str, armour_a: str) -> tuple:
    """The measurement flags (`precision:absolute`, `below_resolution:<k>`, `carried:<k>`) of the grid pairs this read interpolates
    between, united and sorted; empty for a clean read."""
    a0, a1, _ = _bracket(skill_a, 'skill_a')
    d0, d1, _ = _bracket(skill_d, 'skill_d')
    out = set()
    for sa in {a0, a1}:
        for sd in {d0, d1}:
            out.update(_pair(arm_a, armour_a, sa, arm_d, armour_d, sd)['flags'])
    return tuple(sorted(out))


def status(path: str) -> str:
    """The status tag (`seed`, `calibrated` or `derived`) of the contact value at a dotted path, e.g. `contact.exposure.posture_k`,
    `contact.levels.intent_offense`, `missile.hit.bow.close`, `missile.bands`. Refuses a path that names no tagged value."""
    node = _data()
    for part in path.split('.'):
        if not isinstance(node, dict) or part not in node:
            raise ValueError(f'no contact value at {path!r}')
        node = node[part]
    if not isinstance(node, dict) or 'status' not in node:
        raise ValueError(f'{path!r} is a block, not a tagged value')
    return node['status']
