"""modules.mass_battle.armyrecord -- the CONTENT of a faction's army record, as pure functions (ED-IN-0305, phase 2).

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
from modules.mass_battle.config import BLOCK_SIZE, SUBUNIT_ROUT_FLOOR
from modules.mass_battle.orderofbattle import STANCES, STRATEGIES, TARGETINGS, OrderOfBattle, Subformation
from modules.mass_battle.troop_types.recruitment import TRAINING_SITE, recruit_limit
from modules.mass_battle.troop_types.registry import TROOP_TYPE_STATS, roles_for, stats_for

__all__ = ['KEYS', 'new', 'raised', 'by_type', 'unassigned', 'form', 'assign', 'release', 'order', 'set_strategy',
           'validate', 'to_order_of_battle', 'apply', 'OPS', 'fielded', 'disband', 'discharge', 'cohort_claims', 'options']

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


def by_type(record: dict, cohort: Optional[str] = None) -> dict:
    """Troops under arms by type, trained and assigned together: the figure the population cap counts. With
    `cohort`, only the troops drawn from that cohort (the cap is per cohort: a cohort is the population)."""
    out: dict = {}
    for c, t, n in record['trained']:
        if cohort is None or c == cohort:
            out[t] = out.get(t, 0) + n
    for sf in record['subformations']:
        for c, n in sf['assigned']:
            if cohort is None or c == cohort:
                out[sf['troop_type']] = out.get(sf['troop_type'], 0) + n
    return out


def cohort_claims(record: Optional[dict], others, cohort: str) -> dict:
    """Troops already under arms from `cohort`, by type, across `record` (None for no army yet) and every record in
    `others`: the figure `recruit_limit` reads as `raised`. The cap is the cohort's population, whichever army it is
    raised into."""
    given: dict = dict(by_type(record, cohort)) if record is not None else {}
    for other in others:
        for t, k in by_type(other, cohort).items():
            given[t] = given.get(t, 0) + k
    return given


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
    if not isinstance(name, str) or not name.strip():
        raise ValueError(f"a subformation needs a name (a non-empty string), got {name!r}")
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


def disband(record: dict, name: str) -> dict:
    """The record without subformation `name`; every trooper in it returns to the trained, unassigned pool, so no one is
    lost. (A wrong type or a spare slot is no longer permanent.)"""
    i = _sf_index(record, name)
    sf = record['subformations'][i]
    trained = record['trained']
    for cohort, n in sf['assigned']:
        trained = _merge(trained, (cohort, sf['troop_type']), n)
    sfs = tuple(s for j, s in enumerate(record['subformations']) if j != i)
    return {**record, 'trained': trained, 'subformations': sfs}


def discharge(record: dict, cohort: str, troop_type: str, count) -> dict:
    """The record with `count` trained, UNASSIGNED troops of `troop_type` from `cohort` sent home: they leave the army
    and stop counting against the cohort's cap. Troops in a subformation are released (`assign` with a negative count,
    or `disband`) before they can be discharged."""
    t, n = _type(troop_type), _pos(count)
    have = unassigned(record, cohort, t)
    if n > have:
        raise ValueError(f"{cohort!r} has only {have} trained {t} unassigned, asked to discharge {n}")
    return {**record, 'trained': _merge(record['trained'], (cohort, t), -n)}


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
    parts, drawn = [], []
    for sf in record['subformations']:
        strength = sum(n * max(0.0, min(1.0, float(fit(c)))) for c, n in sf['assigned'])
        if strength > 0:
            drawn += [c for c, n in sf['assigned'] if n > 0 and float(fit(c)) > 0 and c not in drawn]
            parts.append(Subformation(sf['name'], sf['troop_type'], strength, role=sf['role'], stance=sf['stance'],
                                      target=sf['target'], fall_back_at=sf['fall_back_at']))
    if not parts:
        raise ValueError("no subformation has any troops assigned")
    return OrderOfBattle(tuple(parts), record['strategy'], tuple(drawn))


#: The commands `apply` runs: one per season verb (`recruit`, `form_unit`, `assign_troops`, `order_unit`) and
#: `validate`, which `create_record` asks of an army it mints.
OPS = ('recruit', 'form', 'assign', 'order', 'disband', 'discharge', 'validate')


def apply(cmd) -> dict:
    """THE ONE ENTRY THE SEASON CALLS (`mass_battle.army`, a `query` composition row): run `cmd.op` on `cmd.record`
    with `cmd.args` and return the new record, or raise ValueError with the rule broken. `cmd` is
    `engine/season/queries/inputs.py::ArmyCommand` (`record`, `op`, `args`); the host builds it from the act and the
    world and writes the result back, so nothing here reads a `World`.

      recruit  args cohort, troop_type, count, weight, sites ({site kind: condition}), full -- raise `count` troops
               from `cohort`, no more than `recruit_limit` allows for that cohort's `weight` and `sites`
      form     args name, troop_type, role (optional)
      assign   args name, cohort, count -- a negative count releases troops back to the trained pool
      order    args name and any of role, stance, target, fall_back_at; or strategy alone, for the army
      validate no args -- the record unchanged if well formed
    """
    try:
        return _apply(cmd)
    except (KeyError, TypeError, OverflowError) as e:    # a missing or mistyped payload field is a refusal, not a crash
        raise ValueError(f"bad {cmd.op!r} command: {type(e).__name__} {e}") from e


def _apply(cmd) -> dict:
    r, a = cmd.record, cmd.args
    validate(r)
    if cmd.op == 'validate':
        return r
    if cmd.op == 'recruit':
        n = _pos(a['count'])
        # The cap is the cohort's population, whichever army it is raised into: what it has already given to any
        # other army (`others`, the host's: the other armies' records) counts against it.
        given = cohort_claims(r, a.get('others', ()), a['cohort'])
        room = recruit_limit(a['troop_type'], a['weight'], a['sites'], given, a['full'])
        if n > room:
            raise ValueError(f"{a['cohort']!r} can raise {room} more {a['troop_type']}, asked for {n}")
        return raised(r, a['cohort'], a['troop_type'], n)
    if cmd.op == 'form':
        return form(r, a['name'], a['troop_type'], a.get('role'))
    if cmd.op == 'assign':
        n = a['count']
        if n == 0 or int(n) != n:
            raise ValueError(f"a count must be a non-zero whole number, got {n!r}")
        return assign(r, a['name'], a['cohort'], n) if n > 0 else release(r, a['name'], a['cohort'], -n)
    if cmd.op == 'disband':
        return disband(r, a['name'])
    if cmd.op == 'discharge':
        return discharge(r, a['cohort'], a['troop_type'], a['count'])
    if cmd.op == 'order':
        if 'strategy' in a:
            if set(a) != {'strategy'}:
                raise ValueError("an order names a strategy or a subformation's tactics, not both")
            return set_strategy(r, a['strategy'])
        fields = {k: a[k] for k in ('role', 'stance', 'target', 'fall_back_at') if k in a}
        if not fields:
            raise ValueError("an order sets at least one of role, stance, target, fall_back_at, or a strategy")
        return order(r, a['name'], **fields)
    raise ValueError(f"unknown army command {cmd.op!r} (known: {OPS})")


def options(q) -> dict:
    """THE THIRD ENTRY THE SEASON CALLS (`mass_battle.army_options`, a `query` composition row): what a player may ask of
    this army, as plain data, and what is wrong with it as it stands. Read-only, and it decides nothing: a command listed
    here is one `apply` would accept and a command not listed is one it would refuse for the reason given, because the
    bounds are the same functions (`recruit_limit`, the registry's menus). `q` is
    `engine/season/queries/inputs.py::ArmyOptionsQuery`: `record`, `cohorts` (`((cohort id, weight, {site kind:
    condition}), ...)`, those the faction may raise), `full` (the condition scale), `others` (the other armies'
    records, whose claims on a cohort count against it).

      strategies, stances, targets  the vocabulary `order` accepts
      troop_types   ((type, roles, site kind or None), ...), the types `recruit` and `form` accept
      raise         ((cohort, type, room), ...), for each cohort and type with room above 0
      advisories    ((kind, subject, have, floor), ...) -- a subformation under `SUBUNIT_ROUT_FLOOR` routs at the first
                    check (`subformation_routs`), a record fielding under one `BLOCK_SIZE` block routs at once
                    (`army_routs`), trained troops in no subformation do not fight (`unassigned`), and a levy
                    subformation never closes to contact (`levy_never_closes`, HANDOFF_MB)."""
    r = q.record
    validate(r)
    rows = []
    for cohort, weight, sites in sorted(q.cohorts):
        given = cohort_claims(r, q.others, cohort)
        for t in sorted(TROOP_TYPE_STATS):
            room = recruit_limit(t, weight, sites, given, q.full)
            if room > 0:
                rows.append((cohort, t, room))
    notes, fielded_total = [], 0
    for sf in r['subformations']:
        n = sum(k for _c, k in sf['assigned'])
        fielded_total += n
        if n < SUBUNIT_ROUT_FLOOR:
            notes.append(('subformation_routs', sf['name'], n, SUBUNIT_ROUT_FLOOR))
        if sf['troop_type'] == 'levy':
            notes.append(('levy_never_closes', sf['name'], n, 0))
    if r['subformations'] and fielded_total < BLOCK_SIZE:
        notes.append(('army_routs', None, fielded_total, BLOCK_SIZE))
    idle = sum(n for _c, _t, n in r['trained'])
    if idle:
        notes.append(('unassigned', None, idle, 0))
    return {'strategies': tuple(sorted(STRATEGIES)), 'stances': STANCES, 'targets': TARGETINGS,
            'troop_types': tuple((t, tuple(roles_for(t)), (TRAINING_SITE.get(t) or (None,))[0])
                                 for t in sorted(TROOP_TYPE_STATS)),
            'raise': tuple(rows), 'advisories': tuple(notes)}


def fielded(muster) -> Optional[OrderOfBattle]:
    """THE SECOND ENTRY THE SEASON CALLS (`mass_battle.army_order`, a `query` composition row): the order of battle an
    army record fights with on one field, or None when none of its troops are there to fight.
    `muster` is `engine/season/queries/inputs.py::ArmyMuster` (`record`, `fit`); `fit` is `((cohort, fraction), ...)`
    for every cohort the host knows of (not only those near this field: an army is where its commander is, and the
    host has already decided the commander is here), the fraction being the share of each still fit to fight. A cohort
    the record names that is not in `fit` has no body left to give, and fights with nobody. A malformed record raises
    ValueError (`validate`); an army with nobody present is not malformed, it is absent, and reads None so the host
    fights that side as it always did."""
    validate(muster.record)
    here = dict(muster.fit)
    try:
        return to_order_of_battle(muster.record, lambda c: here.get(c, 0.0))
    except ValueError:                  # `validate` passed, so the only refusal left is 'nobody has any strength here'
        return None
