"""modules.mass_battle.armyrecord -- the CONTENT of a faction's army record, as pure functions (ED-IN-0304, phase 2).

Jordan ruled on 2026-10-28 that a faction's army is a record of its own (an order of battle), not only
`PersonId[] at weight`. The season carries it as a `Record` of kind `army`; THIS module owns what that record's
`subject_matter` says and every operation on it, so the season verbs (`recruit`, `form`, `assign`, `order`) are thin:
they read the world for the facts a rule needs, call one function here, and write the result. Nothing here reads
a `World`.

THE SHAPE (`subject_matter`'s exact key set, which `rosters.yaml: record_kinds` mirrors):

    faction       the faction Proposition id the army belongs to
    strategy      an `orderofbattle.STRATEGIES` key
    trained       ((cohort person id, troop type, count), ...)   troops raised and not yet in a subformation
    subformations ({name, troop_type, role, stance, target, fall_back_at, assigned}, ...)
                  where `assigned` is ((cohort person id, count), ...)

A TROOP IS A HEADCOUNT OF A COHORT: `trained` and `assigned` name the cohort `Person` the people are drawn from and how
many, so the season can check the army never holds more of a cohort than its weight allows (this module checks the
arithmetic of its own record). Every function returns a NEW record and never mutates its argument; a rule broken
raises ValueError, which the verb turns into its refusal.

`to_order_of_battle` is the one reader the battle uses: it turns the record into `orderofbattle.OrderOfBattle`,
scaling each cohort's count by how much of that cohort is still fit to fight.
"""
from __future__ import annotations

from typing import Callable, Optional

from modules.mass_battle.armies import SUBUNIT_CAP
from modules.mass_battle.orderofbattle import STANCES, STRATEGIES, TARGETINGS, OrderOfBattle, Subformation
from modules.mass_battle.troop_types.registry import roles_for, stats_for

__all__ = ['KEYS', 'new', 'raised', 'by_type', 'unassigned', 'form', 'assign', 'order', 'set_strategy', 'validate',
           'to_order_of_battle']

#: `subject_matter`'s exact key set. `engine/season/rosters.yaml: record_kinds.values.army` mirrors it and a test pins
#: the two equal.
KEYS = ('faction', 'strategy', 'trained', 'subformations')


def new(faction: str, strategy: str = 'line') -> dict:
    """An empty army record for `faction`."""
    if strategy not in STRATEGIES:
        raise ValueError(f"unknown strategy {strategy!r} (known: {sorted(STRATEGIES)})")
    return {'faction': faction, 'strategy': strategy, 'trained': (), 'subformations': ()}


def _type(troop_type: str) -> str:
    t = str(troop_type).strip().lower()
    if stats_for(t) is None:
        raise ValueError(f"unknown troop type {troop_type!r}")
    return t


def _pos(count) -> int:
    if int(count) != count or count <= 0:
        raise ValueError(f"a count must be a positive whole number, got {count!r}")
    return int(count)


def _merge(rows, key, delta):
    """`rows` as ((*key, n), ...) with `delta` added to the row for `key`, dropping a row that reaches 0."""
    out, hit = [], False
    for r in rows:
        if tuple(r[:-1]) == tuple(key):
            hit = True
            n = r[-1] + delta
            if n < 0:
                raise ValueError(f"{key!r} would go below zero")
            if n:
                out.append((*key, n))
        else:
            out.append(tuple(r))
    if not hit:
        if delta < 0:
            raise ValueError(f"{key!r} is not held")
        if delta:
            out.append((*key, delta))
    return tuple(out)


def by_type(record: dict) -> dict:
    """Troops under arms by type, trained and assigned together: the figure the population cap counts."""
    out: dict = {}
    for _cohort, t, n in record['trained']:
        out[t] = out.get(t, 0) + n
    for sf in record['subformations']:
        for _cohort, n in sf['assigned']:
            out[sf['troop_type']] = out.get(sf['troop_type'], 0) + n
    return out


def raised(record: dict, cohort: str, troop_type: str, count) -> dict:
    """The record with `count` more troops of `troop_type` drawn from `cohort`, trained and unassigned. The caller
    has already checked the population and training limits (`troop_types.recruitment.recruit_limit`)."""
    t, n = _type(troop_type), _pos(count)
    return {**record, 'trained': _merge(record['trained'], (cohort, t), n)}


def unassigned(record: dict, cohort: str, troop_type: str) -> int:
    """Trained troops of `troop_type` from `cohort` not yet in any subformation."""
    t = _type(troop_type)
    return sum(n for c, tt, n in record['trained'] if c == cohort and tt == t)


def _sf_index(record: dict, name: str) -> int:
    for i, sf in enumerate(record['subformations']):
        if sf['name'] == name:
            return i
    raise ValueError(f"no subformation named {name!r}")


def _replace_sf(record: dict, i: int, sf: dict) -> dict:
    sfs = list(record['subformations'])
    sfs[i] = sf
    return {**record, 'subformations': tuple(sfs)}


def form(record: dict, name: str, troop_type: str, role: Optional[str] = None) -> dict:
    """The record with a new, empty subformation `name` of `troop_type`. Fields beyond name, type and role start
    unset; `order` sets them. Refuses a duplicate name, an unknown type, a role outside the type's menu, and a
    twelfth subformation (`armies.SUBUNIT_CAP`)."""
    t = _type(troop_type)
    if not str(name).strip():
        raise ValueError("a subformation needs a name")
    if any(sf['name'] == name for sf in record['subformations']):
        raise ValueError(f"duplicate subformation name {name!r}")
    if len(record['subformations']) >= SUBUNIT_CAP:
        raise ValueError(f"an army holds at most {SUBUNIT_CAP} subformations")
    if role is not None and role not in roles_for(t):
        raise ValueError(f"role {role!r} is not in {t!r}'s menu {roles_for(t)}")
    sf = {'name': name, 'troop_type': t, 'role': role, 'stance': None, 'target': None, 'fall_back_at': None,
          'assigned': ()}
    return {**record, 'subformations': (*record['subformations'], sf)}


def assign(record: dict, name: str, cohort: str, count) -> dict:
    """Move `count` trained troops of the subformation's type, from `cohort`, into subformation `name`. A negative
    `count` is not accepted: to move troops out, assign them to the other subformation after `release`."""
    n = _pos(count)
    i = _sf_index(record, name)
    sf = record['subformations'][i]
    have = unassigned(record, cohort, sf['troop_type'])
    if n > have:
        raise ValueError(f"{cohort!r} has only {have} trained {sf['troop_type']} unassigned, asked for {n}")
    trained = _merge(record['trained'], (cohort, sf['troop_type']), -n)
    sf2 = {**sf, 'assigned': _merge(sf['assigned'], (cohort,), n)}
    return _replace_sf({**record, 'trained': trained}, i, sf2)


def release(record: dict, name: str, cohort: str, count) -> dict:
    """The reverse of `assign`: return `count` troops from subformation `name` to the trained, unassigned pool."""
    n = _pos(count)
    i = _sf_index(record, name)
    sf = record['subformations'][i]
    sf2 = {**sf, 'assigned': _merge(sf['assigned'], (cohort,), -n)}
    trained = _merge(record['trained'], (cohort, sf['troop_type']), n)
    return _replace_sf({**record, 'trained': trained}, i, sf2)


_UNSET = object()


def order(record: dict, name: str, *, role=_UNSET, stance=_UNSET, target=_UNSET, fall_back_at=_UNSET) -> dict:
    """Set subformation `name`'s tactics: its role (from its type's menu), stance, targeting preference and
    fall-back point. A field left out is unchanged; passing None clears it. Validated as `orderofbattle.validate`
    validates a subformation."""
    i = _sf_index(record, name)
    sf = dict(record['subformations'][i])
    if role is not _UNSET:
        if role is not None and role not in roles_for(sf['troop_type']):
            raise ValueError(f"role {role!r} is not in {sf['troop_type']!r}'s menu {roles_for(sf['troop_type'])}")
        sf['role'] = role
    if stance is not _UNSET:
        if stance is not None and stance not in STANCES:
            raise ValueError(f"stance {stance!r} not in {STANCES}")
        sf['stance'] = stance
    if target is not _UNSET:
        if target not in TARGETINGS:
            raise ValueError(f"target {target!r} not in {TARGETINGS}")
        sf['target'] = target
    if fall_back_at is not _UNSET:
        if fall_back_at is not None and not 0.0 < fall_back_at < 1.0:
            raise ValueError(f"fall_back_at must be strictly between 0 and 1, got {fall_back_at!r}")
        sf['fall_back_at'] = fall_back_at
    return _replace_sf(record, i, sf)


def set_strategy(record: dict, strategy: str) -> dict:
    """The record under a different `orderofbattle.STRATEGIES` strategy."""
    if strategy not in STRATEGIES:
        raise ValueError(f"unknown strategy {strategy!r} (known: {sorted(STRATEGIES)})")
    return {**record, 'strategy': strategy}


def validate(record: dict) -> None:
    """Refuse a record that is not well formed: wrong key set, an unknown strategy or troop type, a non-positive
    count, a duplicate subformation name, or more than `SUBUNIT_CAP` subformations. Raises ValueError."""
    if tuple(sorted(record)) != tuple(sorted(KEYS)):
        raise ValueError(f"army record keys {sorted(record)} are not {sorted(KEYS)}")
    if record['strategy'] not in STRATEGIES:
        raise ValueError(f"unknown strategy {record['strategy']!r}")
    for c, t, n in record['trained']:
        _type(t)
        _pos(n)
    names = [sf['name'] for sf in record['subformations']]
    if len(set(names)) != len(names):
        raise ValueError("duplicate subformation name")
    if len(names) > SUBUNIT_CAP:
        raise ValueError(f"more than {SUBUNIT_CAP} subformations")
    for sf in record['subformations']:
        _type(sf['troop_type'])
        for _c, n in sf['assigned']:
            _pos(n)


def to_order_of_battle(record: dict, fitness: Optional[Callable[[str], float]] = None) -> OrderOfBattle:
    """The `OrderOfBattle` the battle fights with. Each subformation's strength is the sum over its assigned cohorts
    of `count * fitness(cohort)`; `fitness` is the share of a cohort still fit to fight (1.0 for a whole one; the
    season passes its body fraction). A subformation left with no strength is dropped; an army with none left
    raises ValueError, since there is nothing to field."""
    fit = fitness or (lambda _c: 1.0)
    parts = []
    for sf in record['subformations']:
        strength = sum(n * max(0.0, min(1.0, float(fit(c)))) for c, n in sf['assigned'])
        if strength > 0:
            parts.append(Subformation(sf['name'], sf['troop_type'], strength, role=sf['role'], stance=sf['stance'],
                                      target=sf['target'], fall_back_at=sf['fall_back_at']))
    if not parts:
        raise ValueError("no subformation has any troops assigned")
    return OrderOfBattle(tuple(parts), record['strategy'])
