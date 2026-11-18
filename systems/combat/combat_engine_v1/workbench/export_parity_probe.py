#!/usr/bin/env python3
"""export_parity_probe.py -- can the typed export alone rebuild every weapon and reproduce its derived quantities?

The round trip a port has to pass (B14.12, `03_PC_weapon_records_in_the_export`): read ONLY
`engine/engine_params/combat_engine_v1.json`, rebuild every weapon record from its `weapons` entry (the authored
fields) by the bake the oracle applies at import, recompute the `derived` section with the catalogue's own quantity
registry (`catalogue.QUANTITIES`, the one owner), and compare it with the exported one. The authored data
`modules/combat/weapons.py` is never read: a bar on that module's name stops its import, and after the run
`modules.combat.weapons` is asserted absent from `sys.modules`.

HOW THE ORACLE'S FUNCTIONS RUN WITHOUT THAT FILE. `combatant.py` and `catalogue.py` bind `modules.combat.weapons` by
name (`WEAPONS`, `GEOMETRY`, `HALFSWORD_FORM`, `HALFSWORD_BASE`). The probe registers a stand-in module of that name,
built from the export (`weapons`, `kit.forms`), lets them bind it, then removes it. The stand-in holds the rebuilt
records and nothing else; the real file is barred by the import finder below, so a stray import of it is an
ImportError and not a silent read. The scalar constants of the export (`cfg`, `weapon_physics`, `combatant`) are
written over the oracle's own, so a drifted value cannot hide behind an identical module copy.

    python systems/combat/combat_engine_v1/workbench/export_parity_probe.py            # exit 0 and the 50-weapons line
    python systems/combat/combat_engine_v1/workbench/export_parity_probe.py --plant [WEAPON]
        # the planted control: one exported mass edited in an in-memory COPY (default `longsword`); prints the weapon
        # and exits 1. The file on disk is never written.

Parity is stated against the float contract (A-29): numbers agree to 1e-9 absolute; everything else (strings, flags,
lists) agrees exactly. Not a CI row (CLAUDE.md section 0.1 pt 5): a one-off run of the round trip.
"""
import copy
import importlib.abc
import importlib.util
import json
import os
import sys
import types

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
EXPORT = os.path.join(REPO, 'engine', 'engine_params', 'combat_engine_v1.json')
AUTHORED_DATA = 'modules.combat.weapons'
TOLERANCE = 1e-9


class _BarAuthoredData(importlib.abc.MetaPathFinder):
    """Refuses to import the authored weapons module. Consulted only for a name NOT already in `sys.modules`, so
    the stand-in registered under that name passes and the real file cannot."""
    def find_spec(self, name, path=None, target=None):
        if name == AUTHORED_DATA:
            raise ImportError(f"{AUTHORED_DATA} is barred: the probe reads the export alone")
        return None


def _is_number(x):
    return isinstance(x, (int, float)) and not isinstance(x, bool)


def _gap(a, b):
    """(largest numeric difference found, a description of the first non-numeric disagreement or None)."""
    if _is_number(a) and _is_number(b):
        return abs(a - b), None
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return 0.0, f"length {len(a)} vs {len(b)}"
        worst, why = 0.0, None
        for x, y in zip(a, b):
            w, d = _gap(x, y)
            worst, why = max(worst, w), why or d
        return worst, why
    if isinstance(a, dict) and isinstance(b, dict):
        if set(a) != set(b):
            return 0.0, f"keys {sorted(set(a) ^ set(b))}"
        worst, why = 0.0, None
        for k in a:
            w, d = _gap(a[k], b[k])
            worst, why = max(worst, w), why or d
        return worst, why
    return (0.0, None) if a == b else (0.0, f"{a!r} vs {b!r}")


def _rebuild(authored, geometry, weapon_physics):
    """One record from its exported authored fields, by the bake `weapons.py` applies at import (the same order:
    geo and gap, each mode element's geo, `_derived`, then the two guard sums)."""
    rec = copy.deepcopy(authored)
    baked = geometry.bake(rec['geometry'])
    rec['gap'], rec['geo'] = baked['gap'], baked
    for mode in rec.get('mode_elements', ()):
        mode['geo'] = geometry.bake(mode.pop('geometry'))
    rec['_derived'] = weapon_physics.derive(rec)
    rec['hand_guard'] = round(weapon_physics.hand_guard(rec), 4)
    rec['blade_guard'] = round(weapon_physics.blade_guard(rec), 4)
    return rec


def _overwrite_scalars(module_or_dict, exported):
    """Write the export's int/float constants over the oracle's own (a name the oracle does not hold is skipped)."""
    for name, value in exported.items():
        if not _is_number(value):
            continue
        if isinstance(module_or_dict, dict):
            if name in module_or_dict:
                module_or_dict[name] = value
        elif hasattr(module_or_dict, name):
            setattr(module_or_dict, name, value)


def run(plant=None):
    with open(EXPORT, encoding='utf-8') as fh:
        sections = json.load(fh)['sections']
    weapons = copy.deepcopy(sections['weapons'])
    if plant is not None:
        weapons[plant]['mass'] = weapons[plant]['mass'] * 1.5   # the control: ONE mass, in the copy

    sys.path.insert(0, REPO)
    sys.path.insert(0, HERE)
    sys.meta_path.insert(0, _BarAuthoredData())
    from modules.combat import geometry, weapon_physics, config
    _overwrite_scalars(weapon_physics, sections['weapon_physics'])
    _overwrite_scalars(config.CFG, sections['cfg'])

    records = {name: _rebuild(rec, geometry, weapon_physics) for name, rec in weapons.items()}
    forms = sections['kit']['forms']
    stand_in = types.ModuleType(AUTHORED_DATA)
    stand_in.__package__ = 'modules.combat'
    stand_in.WEAPONS = records
    stand_in.GEOMETRY = {n: r['geometry'] for n, r in records.items()}
    stand_in.HALFSWORD_BASE = dict(forms)
    stand_in.HALFSWORD_FORM = {base: form for form, base in forms.items()}
    sys.modules[AUTHORED_DATA] = stand_in
    try:
        from modules.combat import combatant
        _overwrite_scalars(combatant, sections['combatant'])
        spec = importlib.util.spec_from_file_location('catalogue_for_parity', os.path.join(HERE, 'catalogue.py'))
        catalogue = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(catalogue)
        recomputed = json.loads(json.dumps(catalogue.values(as_json=True), default=str))
        columns = [col for col, _g, _f, _s in catalogue.QUANTITIES]
    finally:
        sys.modules.pop(AUTHORED_DATA, None)
    assert AUTHORED_DATA not in sys.modules, f"{AUTHORED_DATA} is in sys.modules after the run"

    derived = sections['derived']
    startable = sections['kit']['weapons']
    problems, worst = [], 0.0
    if sorted(derived) != sorted(startable) or sorted(recomputed) != sorted(startable):
        problems.append(f"roster: derived {len(derived)}, recomputed {len(recomputed)}, kit.weapons {len(startable)}")
    for name in sorted(set(derived) & set(recomputed)):
        if sorted(derived[name]) != sorted(columns):
            problems.append(f"{name}: derived columns differ from catalogue.QUANTITIES")
        for col in columns:
            w, why = _gap(derived[name].get(col), recomputed[name].get(col))
            worst = max(worst, w)
            if why or w > TOLERANCE:
                problems.append(f"{name}: {col} derived={derived[name].get(col)!r} "
                                f"recomputed={recomputed[name].get(col)!r}" + (f" ({why})" if why else ""))
    return len(startable), worst, problems


def main(argv):
    try:
        sys.stdout.reconfigure(encoding='utf-8', errors='replace')
    except Exception:
        pass
    plant = None
    if '--plant' in argv:
        i = argv.index('--plant')
        plant = argv[i + 1] if i + 1 < len(argv) and not argv[i + 1].startswith('-') else 'longsword'
    count, worst, problems = run(plant)
    if problems:
        print(f"PARITY FAILS: {len(problems)} disagreement(s)" + (f" (planted: {plant}.mass x 1.5, in a copy)" if plant else ""))
        for p in problems:
            print(f"  {p}")
        return 1
    print(f"{count} weapons; max |derived − recomputed| <= 1e-9")
    print(f"  measured max {worst:.3e}; {AUTHORED_DATA} not in sys.modules")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
