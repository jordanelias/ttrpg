#!/usr/bin/env python3
"""
export_engine_params.py — typed engine-params export: the Godot-ingestible seed (ED-1052).

Serializes the CANONICAL personal-combat Class-C oracle
(modules/combat/config.py + core.py — ratified ED-900/904; systems/combat/combat_engine_v1/ until plan
position `31b`; the live parameter
source per references/canonical_sources.yaml `resolution_engine`) to a typed JSON artifact:

    engine/engine_params/combat_engine_v1.json

and, since B03.68 (`09_WR_threadwork_module` edit 3), a second typed output of the same shape from the threadwork
oracle's one owner of its tables, systems/threadwork/sim/params.py:

    engine/engine_params/threadwork_params.json

The `cfg` section mirrors config.CFG; the `core` section (added under OPT-AV-17 / ED-PC-0013,
widening ED-1052's typed-export slice) carries core.py's ~20 canonical resolution/damage/armour
constants — POOL_FLOOR, BASE_POOL, TN, the QUAL/DELIVERY/RESIST/GAP_EXPOSURE model
tables, etc. — that a Godot port previously had to hand-transcribe (the RESIST/GAP_EXPOSURE
never-carried gap, C6-M2/OPT-AV-15). Constants are AUTO-COLLECTED (every uppercase JSON-typeable
module constant), not hand-listed, so a new canonical constant in the oracle cannot be silently
left unexported. The `attributes` section (PC-14) carries modules/combat/attributes.py's spec, a dict keyed
by attribute (default, neutral, registry_key, status); its Godot fields stay unbound (CLAUDE.md §5).
Since B14.12 (schema 8) the export also carries the weapons a port applies those coefficients to: `weapons` (each
record's authored fields; the baked fields are derived, not inputs), `derived` (per startable weapon, the quantities
`workbench/catalogue.py::QUANTITIES` enumerates, computed by the oracle: the parity oracle, never an input; the probe
`workbench/export_parity_probe.py` recomputes it from `weapons` alone) and one section per module of
weapon_physics / combat_systems / combatant / ability_primitives / traditions holding the constants DEFINED there
(found by the syntax tree, not `dir()`).

WHY (CLAUDE.md §5): mechanical parameters live as prose tables a Godot importer cannot
ingest; every value crossing into Godot has been hand-transcribed (the ED-1050 failure
class: the port hand-"corrected" its oracle). This exporter starts the successor
discipline — oracle → typed export → port regenerates from the export, never hand-edits
(godot_conversion_strategy re-export rule; archived wrapper doctrine ED-1083: convertibility =
round-trip morphisms). Scope guard: exports the ALREADY-TYPED Python oracle only; it does
NOT parse engine/params/*.md prose (that prose-formula-drift pipeline is the A18 detector,
tools/ci_formula_prose_check.py — the other half of the ED-1052 slice).

MODES:
    python tools/export_engine_params.py            # (re)generate the JSON artifact
    python tools/export_engine_params.py --check    # re-derive and diff vs the committed
                                                    # files (BOTH outputs); exit 1 on ANY drift
                                                    # (value or shape). Blocking in CI: deterministic,
                                                    # self-consistent — if config.py or params.py
                                                    # changes, regenerate and commit with the JSON.

The artifact is GENERATED — never hand-edit. Tuples become arrays; nested dicts pass
through; values are evaluated at import (computed expressions export their results).
`schema_version` bumps only on SHAPE changes (new or removed sections, removed or renamed keys
inside a section, type changes), not on retuned values.
"""
import ast
import inspect
import json
import math
import os
import sys

# Primitives (repo root, lane roster, token estimate, ids, Status reader) are
# owned by tools/ci_common.py — plan G7, ED-IN-0159 §8.3. See its module docstring;
# the two lines below are the bootstrap, anchored on THIS file's directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO_ROOT = ci_common.REPO
if REPO_ROOT not in sys.path:
    sys.path.insert(0, REPO_ROOT)   # `modules.combat` is a package: derive() imports it by that name
OUT_PATH = os.path.join(REPO_ROOT, 'engine', 'engine_params', 'combat_engine_v1.json')
THREADWORK_PARAMS = os.path.join(REPO_ROOT, 'systems', 'threadwork', 'sim', 'params.py')
THREADWORK_OUT_PATH = os.path.join(REPO_ROOT, 'engine', 'engine_params', 'threadwork_params.json')
THREADWORK_SCHEMA_VERSION = 1  # v1 (B03.68): the `params` section (params.py's uppercase constants).

SCHEMA_VERSION = 8  # v2 (OPT-AV-17): added the `core` section (core.py canonical constants).
                    # v3 (B-D1 PC-07): core.COVERAGE_GAP dict -> scalar (a type change); DECISIVE_OB removed (PC-03).
                    # v4 (PC-14): added the `attributes` section (attributes.py's spec; its entries carry null).
                    # v5 (CP-T03-03): added the `kit` section (the weapon keys, the armour tiers and the Combatant's
                    # default kit; read by `engine/substrate/combat_kit.py`).
                    # v6 (CR-85, ED-IN-0330): READ_HISTORY_K, INIT_HISTORY_K and COUNTER_TRAIN_K removed with their
                    # only readers; the `attributes` entry `history` renamed `faculty` (no `neutral`).
                    # v7 (B10-11b, PC-18 (1) and PC-20 (4)): the `attributes` entry `cog` removed (Reason has no combat
                    # read); the `strength` entry's `neutral` null -> 4 (a type change).
                    # v8 (B14.12, `03_PC_weapon_records_in_the_export`): added `weapons` (the 54 records' authored
                    # fields), `derived` (per startable weapon, catalogue.QUANTITIES by the oracle) and the sections
                    # `weapon_physics`, `combat_systems`, `combatant`, `ability_primitives`, `traditions` (the
                    # constants DEFINED in each module); `kit.weapons` now lists the 50 records without a `base`
                    # (it listed all 54) and `kit.forms` (form -> base) is new.


def _typed(value, defined=False):
    """JSON-typed copy of a config value; tuples -> arrays, dicts recurse. Rejects types the
    schema doesn't declare (a new type is a shape change: bump SCHEMA_VERSION deliberately).
    `defined=True` (the five defined-constant modules only, B14.12) also takes None (null) and a set or frozenset,
    as a sorted array: JSON has no set, and the order is the one a diff can hold (`traditions.ADJACENT` is a set of
    frozensets; a tradition row holds None)."""
    if isinstance(value, bool) or isinstance(value, (int, float, str)):
        return value
    if defined and value is None:
        return None
    if isinstance(value, (list, tuple)):
        return [_typed(v, defined) for v in value]
    if defined and isinstance(value, (set, frozenset)):
        return sorted((_typed(v, defined) for v in value), key=lambda v: json.dumps(v, sort_keys=True))
    if isinstance(value, dict):
        return {str(k): _typed(v, defined) for k, v in value.items()}
    raise TypeError(f"config value of unexported type {type(value).__name__}: {value!r}")


def _module_constants(mod):
    """Every module-level UPPERCASE constant that is JSON-typeable, as {name: typed_value}.
    AUTO-collected (not hand-listed) so a new canonical constant in the oracle cannot be
    silently left unexported; imported modules and other non-JSON objects (e.g. SL, WP) raise
    TypeError in _typed() and are skipped. Deterministic: dir() is sorted, output re-sorted at
    render."""
    out = {}
    for name in dir(mod):
        if not name.isupper() or name.startswith('_'):
            continue
        try:
            out[name] = _typed(getattr(mod, name))
        except TypeError:
            continue  # imported module / non-JSON object — not a param constant
    return out


def _attributes_section(spec):
    """The `attributes` section (PC-14): `attributes.SPEC` as a dict keyed by attribute key, each entry its combat
    facts (`default`, `neutral`, `registry_key`, `status`); `neutral` and `registry_key` may be null. Read from the
    spec, never hand-listed, so a new spec entry is a new key here with no edit to this exporter. Godot fields stay
    UNBOUND (CLAUDE.md §5: the registry's roster is IN FLUX); the registry's names and bounds are not exported here
    -- `registry_key` points at them."""
    out = {}
    for s in spec:
        out[s.key] = {f: None if getattr(s, f) is None else _typed(getattr(s, f)) for f in s._fields if f != 'key'}
    return out


def _kit_section(weapons, vocabulary, combatant):
    """The `kit` section (CP-T03-03): what a person can be armed with, read from the oracle and hand-listed nowhere.
    `weapons` is the sorted keys of the records WITHOUT a `base` (a form is a grip the engine switches into, never a
    kit), `forms` maps each form to its base, `armour_tiers` is the sorted `vocabulary.ARMOUR_TIERS`, and
    `defaults` the `weapon` and `armor` defaults of `Combatant.__init__`'s own signature (the kit of a Combatant
    given none), so the season's `rosters.yaml: arms_kinds` is validated at load against the engine that fights, and
    a person who holds no arms is handed the engine's own default rather than a copy of it."""
    params = inspect.signature(combatant.Combatant.__init__).parameters
    forms = {n: r['base'] for n, r in sorted(weapons.WEAPONS.items()) if 'base' in r}
    if forms != dict(sorted(weapons.HALFSWORD_BASE.items())):
        raise ValueError(f"the records' `base` fields {forms} disagree with weapons.HALFSWORD_BASE "
                         f"{weapons.HALFSWORD_BASE}: one mapping of form to base, or none")
    return {
        "weapons": sorted(set(weapons.WEAPONS) - set(forms)),
        "forms": forms,
        "armour_tiers": sorted(vocabulary.ARMOUR_TIERS),
        "defaults": {"weapon": params["weapon"].default, "armor": params["armor"].default},
    }


# The AUTHORED fields of a weapon record, taken from the schema header of modules/combat/weapons.py (a field the code
# reads that the header leaves out is marked): a record or part holding any other field is REFUSED, so a new field is a
# deliberate schema bump here and not a silent omission from the port.
_RECORD_FIELDS = ('mass', 'head_len', 'grip_len', 'hands', 'head', 'reach_adj', 'wclass', 'hilt', 'elements', 'guards',
                  'haft', 'pommel', 'butt', 'geometry', 'mode_elements', 'adornments',
                  'base')           # `base` (not in the header's list): a form's base weapon, which `kit.forms` reads
# What the bake at the foot of weapons.py ADDS to a record: derived, so not exported as an input.
_BAKED_FIELDS = ('geo', 'gap', '_derived', 'hand_guard', 'blade_guard')
_GEOMETRY_FIELDS = ('curvature', 'point_concentration', 'cross_section', 'edge_keenness', 'strike_concentration')
_PART_FIELDS = {
    'elements': ('x_m', 'mass_kg', 'extent_m', 'orient_deg', 'material', 'edge_undulation',
                 'grippable', 'edges'),     # `grippable` and `edges` (not in the header): the half-sword zone, the edge count
    'guards': ('x_m', 'mass_kg', 'extent_m', 'type', 'orient_deg', 'material', 'dual_role_element'),
    'haft': ('x_m', 'mass_kg', 'extent_m'),
    'pommel': ('x_m', 'mass_kg'),
    'butt': ('x_m', 'mass_kg'),
    'geometry': _GEOMETRY_FIELDS,
    'adornments': ('count', 'extent_m'),
    'edges': ('sides', 'false_edge_frac'),
    'edge_undulation': ('amplitude_mm', 'period_mm'),
}
_MODE_FIELDS = ('head', 'element_ref')   # a mode element's third field, `geometry`, is baked into `geo` and recovered below


def _part(label, part, kind):
    unknown = sorted(set(part) - set(_PART_FIELDS[kind]))
    if unknown:
        raise ValueError(f"{label}: field(s) {unknown} are not in the weapon record schema "
                         f"(weapons.py header); add them to _PART_FIELDS['{kind}'] with a SCHEMA_VERSION bump")
    return {k: _part(f"{label}.{k}", v, k) if k in _PART_FIELDS else _typed(v) for k, v in part.items()}


def _weapons_section(weapons, geometry):
    """The `weapons` section: each of the records (forms included) as its AUTHORED fields, so a port can rebuild a
    weapon and apply the coefficients to it. Baked fields (`geo`, `gap`, `_derived`, `hand_guard`, `blade_guard`) are
    derived from these, not inputs. A mode element's authored `geometry` is popped by the bake and survives only inside
    its `geo`, whose five raw passthrough keys are exactly it; `geometry.bake` is re-run on each recovered geometry
    and must reproduce `geo`, or the record is refused."""
    out = {}
    for name in sorted(weapons):
        rec = weapons[name]
        unknown = sorted(set(rec) - set(_RECORD_FIELDS) - set(_BAKED_FIELDS))
        if unknown:
            raise ValueError(f"weapon {name}: field(s) {unknown} are not in the record schema "
                             f"(weapons.py header); add them to _RECORD_FIELDS with a SCHEMA_VERSION bump")
        if geometry.bake(rec['geometry']) != rec['geo']:
            raise ValueError(f"weapon {name}: `geo` is not the bake of its `geometry`")
        row = {}
        for field in _RECORD_FIELDS:
            if field not in rec:
                continue
            value = rec[field]
            if field in ('elements', 'guards', 'adornments'):
                row[field] = [_part(f"{name}.{field}[{i}]", p, field) for i, p in enumerate(value)]
            elif field in ('haft', 'pommel', 'butt', 'geometry'):
                row[field] = _part(f"{name}.{field}", value, field)
            elif field == 'mode_elements':
                row[field] = []
                for i, mode in enumerate(value):
                    extra = sorted(set(mode) - set(_MODE_FIELDS) - {'geo'})
                    if extra:
                        raise ValueError(f"weapon {name}.mode_elements[{i}]: field(s) {extra} are not in the schema")
                    authored = {k: mode['geo'][k] for k in _GEOMETRY_FIELDS}
                    if geometry.bake(authored) != mode['geo']:
                        raise ValueError(f"weapon {name}.mode_elements[{i}]: `geo` is not the bake of its raw keys")
                    row[field].append({**{k: _typed(mode[k]) for k in _MODE_FIELDS}, 'geometry': _typed(authored)})
            else:
                row[field] = _typed(value)
        out[name] = row
    return out


CATALOGUE_PATH = os.path.join(REPO_ROOT, 'systems', 'combat', 'combat_engine_v1', 'workbench', 'catalogue.py')


def _derived_section(catalogue):
    """The `derived` section: per startable weapon (a record without a `base`), the quantities
    `catalogue.QUANTITIES` enumerates, evaluated by the oracle for a neutral fighter. It is the parity oracle a
    port checks its own derivation against, NEVER an input (`workbench/export_parity_probe.py` recomputes it from
    the exported `weapons` alone). A value must be finite; a derivation that raised is exported as its `ERR:` token,
    as the catalogue reports it, never as 0."""
    values = catalogue.values(as_json=True)
    columns = [col for col, _group, _fn, _src in catalogue.QUANTITIES]
    out = {}
    for name in sorted(catalogue.roster()):
        row = {}
        for col in columns:
            value = _typed(values[name][col])
            if isinstance(value, float) and not math.isfinite(value):
                raise ValueError(f"derived {name}.{col} is {value}: not exportable")
            row[col] = value
        out[name] = row
    return out


def _defined_constants(path, module):
    """The constants DEFINED in `path`: every public UPPERCASE name bound by an assignment in the module's OWN body,
    found by the syntax tree and not by `dir()` (which would sweep in what the module merely imports, as
    `combat_systems` imports `WEAPONS`), valued from the imported `module` so a computed expression exports its
    result. A defined constant of an unexportable type RAISES, naming it: it is never silently left out."""
    with open(path, encoding='utf-8') as fh:
        tree = ast.parse(fh.read(), filename=path)
    names = set()
    for node in tree.body:
        targets = node.targets if isinstance(node, ast.Assign) else [node.target] if isinstance(node, ast.AnnAssign) else []
        for target in targets:
            names |= {n.id for n in ast.walk(target) if isinstance(n, ast.Name)}
    out = {}
    for name in sorted(n for n in names if n.isupper() and not n.startswith('_')):
        try:
            out[name] = _typed(getattr(module, name), defined=True)
        except TypeError as exc:
            raise TypeError(f"{os.path.basename(path)}: constant {name} is defined but cannot be exported ({exc})") from exc
    return out


def _load_catalogue():
    """The workbench's catalogue, loaded BY PATH (its directory is no package): its `QUANTITIES` registry is the one
    list of per-weapon derived quantities, so the `derived` section holds no list of its own."""
    import importlib.util
    spec = importlib.util.spec_from_file_location('combat_catalogue', CATALOGUE_PATH)
    catalogue = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(catalogue)
    return catalogue


def derive():
    """Import the oracle and derive the export payload (deterministic)."""
    from modules.combat import config  # the Class-C oracle
    from modules.combat import core    # canonical resolution/damage/armour constants (OPT-AV-17 / ED-PC-0013)
    from modules.combat import combatant   # the Combatant's default kit (CP-T03-03)
    from modules.combat import vocabulary  # the armour tiers (CP-T03-03)
    from modules.combat import weapons     # the weapon keys (CP-T03-03)
    from modules.combat import attributes  # the combat attribute spec (PC-14)
    from modules.combat import geometry    # the bake a weapon record's `geo` is derived by (B14.12)
    from modules.combat import weapon_physics, combat_systems, ability_primitives, traditions  # defined constants (B14.12)
    catalogue = _load_catalogue()          # the per-weapon quantity registry (B14.12)
    sources = ("modules/combat/config.py + core.py + attributes.py + weapons.py + vocabulary.py + combatant.py + "
               "weapon_physics.py + combat_systems.py + ability_primitives.py + traditions.py "
               "(+ workbench/catalogue.py for `derived`)")
    payload = {
        "_generated": ("GENERATED by tools/export_engine_params.py from " + sources + " — the CANONICAL "
                       "Class-C combat oracle (ED-900/904; ED-1050 re-export discipline). NEVER "
                       "hand-edit: regenerate via the exporter and commit both together. "
                       "Class-C = calibrated against the harness, not canon prose."),
        "schema_version": SCHEMA_VERSION,
        "source": sources,
        "canonical_status": "CANONICAL combat_engine_v1 (ED-900; re-ratified ED-904)",
        "sections": {
            "cfg": _typed(config.CFG),
            # handle_rank RETIRED (morphology-rearch Phase B6, 2026-07-02): config.HANDLE_RANK is gone —
            # systems.str_demand reads weapon_physics.handling() (real per-part data) instead.
            "core": _module_constants(core),
            "attributes": _attributes_section(attributes.SPEC),
            "kit": _kit_section(weapons, vocabulary, combatant),
            # B14.12: the weapons a port applies the coefficients to, what the oracle derives from them (the parity
            # oracle, never an input), and the constants DEFINED in the physics, tradition and wound modules.
            "weapons": _weapons_section(weapons.WEAPONS, geometry),
            "derived": _derived_section(catalogue),
            **{m.__name__.rsplit('.', 1)[-1]: _defined_constants(m.__file__, m)
               for m in (weapon_physics, combat_systems, combatant, ability_primitives, traditions)},
        },
    }
    return payload


def derive_threadwork():
    """The threadwork payload: every uppercase JSON-typeable constant of `systems/threadwork/sim/params.py`, the one
    owner of the oracle's tables, collected the way `_module_constants` collects `modules/combat/config.py` (so a
    new table in the owner is exported with no edit here). The module is loaded BY PATH: it imports nothing, and
    the `systems.threadwork.sim` package is not needed to read it."""
    import importlib.util
    spec = importlib.util.spec_from_file_location('threadwork_params_owner', THREADWORK_PARAMS)
    params = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(params)
    return {
        "_generated": ("GENERATED by tools/export_engine_params.py from systems/threadwork/sim/params.py — the one "
                       "owner of the threadwork oracle's tables and magnitudes. NEVER hand-edit: change the "
                       "constant in params.py, regenerate via the exporter and commit both together."),
        "schema_version": THREADWORK_SCHEMA_VERSION,
        "source": "systems/threadwork/sim/params.py",
        "sections": {
            "params": _module_constants(params),
        },
    }


def render(payload):
    return json.dumps(payload, indent=1, sort_keys=True, ensure_ascii=False) + "\n"


def main(argv):
    outputs = ((OUT_PATH, render(derive())), (THREADWORK_OUT_PATH, render(derive_threadwork())))
    if '--check' in argv:
        for path, payload in outputs:
            rel = os.path.relpath(path, REPO_ROOT)
            try:
                with open(path, encoding='utf-8') as f:
                    committed = f.read()
            except OSError:
                print(f"[DRIFT] {rel} missing — run the exporter and commit it.")
                return 1
            if committed != payload:
                print(f"[DRIFT] committed {rel} does not match its oracle.")
                print("        The oracle (modules/combat/config.py or systems/threadwork/sim/params.py) changed")
                print("        without re-export (or the JSON was hand-edited).")
                print("        Fix: python tools/export_engine_params.py  && commit both files together.")
                return 1
        print("Engine-params round-trip: committed JSON matches config.py and threadwork params.py "
              "(oracle -> export verified, both outputs).")
        return 0
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    for path, payload in outputs:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(payload)
    sections = json.loads(outputs[0][1])['sections']
    print(f"Wrote {os.path.relpath(OUT_PATH, REPO_ROOT)} "
          f"(schema v{SCHEMA_VERSION}; {len(sections['cfg'])} cfg keys, {len(sections['core'])} core keys, "
          f"{len(sections['attributes'])} attributes, {len(sections['kit']['weapons'])} weapons).")
    tw = json.loads(outputs[1][1])
    print(f"Wrote {os.path.relpath(THREADWORK_OUT_PATH, REPO_ROOT)} "
          f"(schema v{THREADWORK_SCHEMA_VERSION}; {len(tw['sections']['params'])} params).")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
