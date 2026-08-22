#!/usr/bin/env python3
"""Cook the composition-role map so `engine/` can stop naming `systems/`.

WHY THIS EXISTS. `systems/` stems from `engine/` and `references/` (Jordan, 2026-08-20). The
campaign driver contradicted that: `engine/mc_v18.py:37-38` imported two subsystem callables by
name, so the root named its own dependents and the package graph carried a cycle
(`systems/factions/sim/faction_action.py` -> `engine.autoload.game_state` -> `systems.factions.sim.treaty`).

`references/module_contracts.yaml`'s `composition_roles:` block now declares WHICH module provides
each role; `engine/` states only WHAT role it needs. This tool cooks that block into
`engine/engine_params/composition.json`, which `engine/substrate/composition.py` reads — the same
generate + blocking `--check` pattern as its four siblings, and the same discipline as `keys.py`
vs `key_types.json`: the authored YAML stays reviewable, runtime reads the cooked artifact.

IT VALIDATES AT EXPORT TIME, NOT AT FIRST CALL. Every declared target is imported and its attribute
resolved here, so a typo or a moved module fails a blocking CI gate rather than a campaign run
hours later. That is the whole reason this is worth a gate: an indirection that fails late is worse
than the direct import it replaced.

A row may declare `kind: value` for a module CONSTANT; the default `kind: callable` keeps the
original assertion. See `_KINDS` for why that widening exists and why it is per-row.

Usage:
    python3 tools/export_composition.py           # write engine/engine_params/composition.json
    python3 tools/export_composition.py --check   # re-derive and diff vs committed (exit 1 on drift)
"""
from __future__ import annotations

import importlib
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO = ci_common.REPO
sys.path.insert(0, REPO)

SRC = os.path.join(REPO, 'references', 'module_contracts.yaml')
OUT = os.path.join(REPO, 'engine', 'engine_params', 'composition.json')


_MISSING = object()

#: A role resolves to a named module attribute. `callable` (the default) is the overwhelming
#: majority and keeps the original assertion; `value` admits a module CONSTANT and is declared per
#: row so the callable check is never lost silently. Added 2026-08-22 (plan S5a) for
#: `systems.social_contest.sim.contest`'s side labels, which `engine/cross_scale/scene_dispatch.py`
#: compares a verdict against — a constant, so no callable role could carry it, and no authored
#: surface declares it either (the two EARLIER constant seams each had one: settlements' STAT_MIN/
#: MAX are `set.order` in descriptor_registry.yaml, and the persuasion thresholds turned out to be
#: re-derivation of a verdict the callee already returned). This is a widening of the ONE mechanism,
#: not a second registry: same authored surface, same exporter, same artifact, same leaf.
_KINDS = ('callable', 'value')


def _resolve(target, kind):
    """Import `dotted.module:attribute` and return it. Raises with the role's own words on failure."""
    if kind not in _KINDS:
        raise SystemExit(f'composition_roles target {target!r}: kind {kind!r} must be one of {_KINDS}.')
    if ':' not in target:
        raise SystemExit(f'composition_roles target {target!r} must be "dotted.module:attribute".')
    mod_name, attr = target.split(':', 1)
    mod = importlib.import_module(mod_name)
    fn = getattr(mod, attr, _MISSING)
    if fn is _MISSING:
        raise SystemExit(f'composition_roles target {target!r}: module imported but has no {attr!r}.')
    if kind == 'callable' and not callable(fn):
        raise SystemExit(
            f'composition_roles target {target!r} resolved to a non-callable. If that is '
            f'deliberate — a module constant rather than a function — declare `kind: value` on the '
            f'row so the widening is visible in the registry rather than assumed at the call site.')
    return fn


def build():
    contracts = ci_common.load_yaml(SRC, default=None)
    if not contracts:
        raise SystemExit(f'cannot read {os.path.relpath(SRC, REPO)}')
    roles = contracts.get('composition_roles') or {}
    if not roles:
        raise SystemExit('references/module_contracts.yaml declares no composition_roles. If the '
                         'block was removed, engine/mc_v18.py has nothing to resolve — restore it '
                         'rather than deleting this exporter.')
    out = {}
    for role in sorted(roles):
        row = roles[role]
        target = row['target'] if isinstance(row, dict) else row
        kind = (row.get('kind') if isinstance(row, dict) else None) or 'callable'
        _resolve(target, kind)   # fail HERE, in CI, not at first call during a campaign
        out[role] = {
            'target': target,
            'kind': kind,
            'needed_by': (row.get('needed_by') if isinstance(row, dict) else None),
        }
    return {
        '_generated': (
            'GENERATED by tools/export_composition.py from references/module_contracts.yaml '
            "(composition_roles). NEVER hand-edit: regenerate and commit together. Read at runtime by "
            'engine/substrate/composition.py. Every target is imported and resolved at export time, '
            'so a broken row fails a blocking CI gate rather than a campaign run.'
        ),
        'schema_version': 2,   # 2: rows carry `kind` (callable | value), added at plan S5a
        'source': 'references/module_contracts.yaml#composition_roles',
        'roles': out,
    }


def main(argv):
    text = json.dumps(build(), indent=2, sort_keys=False) + '\n'
    if '--check' in argv:
        if not os.path.exists(OUT):
            print(f'[composition] MISSING {os.path.relpath(OUT, REPO)} — run without --check.')
            return 1
        if open(OUT).read() != text:
            print(f'[composition] DRIFT — {os.path.relpath(OUT, REPO)} is stale. '
                  f'Run: python3 tools/export_composition.py')
            return 1
        print(f'[composition] OK — {len(json.loads(text)["roles"])} role(s), every target resolved.')
        return 0
    with open(OUT, 'w') as fh:
        fh.write(text)
    print(f'[composition] wrote {os.path.relpath(OUT, REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
