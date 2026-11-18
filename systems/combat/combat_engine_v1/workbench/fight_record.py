"""The workbench's one way to a fight: a fighter spec (or a Combatant) becomes a `PersonalCombatInput`, and the record
is fought by `modules.combat.fight:fight`, the entry the season loop calls (B14.11; `03_PC_typed_outcome_one_door`
Part B). `fight_trace.py`, `balance.py` and `server.py` read it; none of them calls `wrapper.fight` on a Combatant or touches
`wrapper._TRACE`.

A PARTY is a plain dict, one fighter's share of the record:
  label, end, attributes ({registry key: value}), kit ((weapon, armor)), score (`Combatant.faculty`), disp,
  tradition, techniques ({name: level}, or a list), axes ({axis: bonus}).
It comes from a spec (`party_of_spec`: the keys `attributes.KEYS` names, plus weapon, armor, tradition, equipped, skills, label)
or from a built Combatant (`party_of_combatant`). `record_of` zips two parties into the record, `claimants` order.

NOT CARRIED, and said so: state a Combatant holds that the record has no field for (`known_traditions`, a hand-set
grip or facing) does not cross the door; a declared `Yield` has no field either (`fight_trace.py` keeps its one fallback).

This file is a leaf: it imports the record type, the entry and the attribute spec, and nothing of the workbench."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..', '..')))  # the repository root: `modules.combat` is a package
from engine.season.queries.inputs import PersonalCombatInput
from modules.combat import attributes   # the combat attribute spec (PC-14): the one owner of which attributes exist
from modules.combat import fight as entry   # `entry.fight` is read at call time, so a spy on the entry sees every call


def party_of_spec(spec, default_label):
    given = {k: spec[k] for k in attributes.KEYS if k in spec}   # an absent attribute takes the spec's default in the Combatant
    return dict(label=spec.get('label', default_label),
                end=given.get('end', attributes.DEFAULT['end']),
                attributes={s.registry_key: given[s.key] for s in attributes.SPEC
                            if s.key in given and s.key != 'end' and s.registry_key is not None},
                kit=(spec.get('weapon', 'arming'), spec.get('armor', 'light')),
                score=given.get('faculty'), disp=given.get('disp'),
                tradition=spec.get('tradition', 'none'), techniques=spec.get('equipped'), axes=spec.get('skills'))


def party_of_combatant(c):
    return dict(label=c.label, end=c.attrs['end'],
                attributes={s.registry_key: c.attrs[s.key] for s in attributes.SPEC
                            if s.key != 'end' and s.registry_key is not None},
                kit=(c.weapon, c.armor), score=c.attrs['faculty'], disp=c.attrs['disp'],
                tradition=c.tradition, techniques=c.equipped, axes=c.skills)


def record_of(pa, pb, terms='death'):
    """The record for parties `pa` (claimant A) and `pb` (B). `wound_quantities` is `()`: it names the fields the
    host's per-turn decider view reads, and the workbench's decider takes only the turn number."""
    both = lambda k: (pa[k], pb[k])
    return PersonalCombatInput(
        claimants=both('label'), ends=both('end'), wound_quantities=(), terms=terms, kits=both('kit'),
        scores=both('score'), attributes=both('attributes'), traditions=both('tradition'),
        techniques=both('techniques'), axes=both('axes'), dispositions=both('disp'))


def result_of(outcome):
    """+1 / -1 / 0 (A won / B won / unresolved): the engine's own `fight_result` event, the last event of every scene. The
    record lifts no integer (B14.01), and the trackers cannot give it: the upset flip turns a felling's winner over."""
    return [e for e in outcome.trace if e['kind'] == 'fight_result'][-1]['result']


def fight_result(rec, rng, cfg=None):
    """One fight of `rec` through the entry, as the integer `wrapper.fight` returns."""
    return result_of(entry.fight(rec, rng, cfg=cfg))
