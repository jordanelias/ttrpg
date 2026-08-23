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

IT ALSO VALIDATES THE `wiring:` FACTS, and that is a second rule in one tool, so here is why.
Plan S5c folded `references/wiring_manifest.yaml` — a second registry keyed by the same 27 module
names — into this file. Three of that manifest's gate's rules survive the fold; two die because a
join makes them unfailable (see `validate_wiring`). The survivors needed a home that CI actually
runs, and this is the ONLY blocking CI gate whose subject is `references/module_contracts.yaml`:
`build_contract_index.py`, the earlier candidate and the natural home on subject grounds, is wired
into no workflow at all, so retiring the rules there would have deleted them while appearing to
move them. The rule count over this registry goes 3 -> 2, in a tool that already parses it.

Usage:
    python3 tools/export_composition.py           # write engine/engine_params/composition.json
    python3 tools/export_composition.py --check   # re-derive and diff vs committed (exit 1 on drift)

Both modes also run `validate_wiring`; it is cheap and a broken wiring row is broken either way.
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


#: The directory the `adapters:` tags name. The retired manifest declared this as a `registries:`
#: map entry alongside `key:` and `quantity:` rows that its own validator never read; only the
#: adapter path was ever consumed, so it is a constant here rather than authored indirection.
ADAPTER_DIR = os.path.join(REPO, 'engine', 'cross_scale')


def validate_wiring(contracts):
    """Return a list of failures in the `wiring:` facts (empty == green).

    TWO OF THE FIVE RULES `tools/wiring_map_check.py --check` ENFORCED ARE GONE, AND NOT BECAUSE
    THEY WERE DROPPED. It checked that every wiring tag resolved to a module contract, and that
    module coverage was 27/27, against a SEPARATE registry keyed by the same module names. Folding
    those facts onto the row they describe makes both unfailable: there is no longer a second key
    space that can disagree. What replaces them is cheaper and stricter — rule 1 below asserts the
    key is PRESENT, which is the only way the fold can now be undone by accident. The other three
    (adapter resolution, adapter coverage, vocabulary) are ported verbatim below.

    The adapter rules do NOT become structural, because adapter tags name FILES on disk rather than
    rows in this registry, so they are ported as-is.
    """
    fails = []
    vocab = contracts.get('wiring_vocabularies') or {}
    builds, godots = set(vocab.get('build_states') or ()), set(vocab.get('godot_states') or ())
    if not builds or not godots:
        return ['module_contracts.yaml: wiring_vocabularies is missing build_states/godot_states — '
                'every wiring row below is unvalidatable without it.']

    # 1) every module row carries wiring facts (the fold's 27/27 coverage, re-expressed)
    entries = []
    for row in contracts.get('modules') or []:
        w = row.get('wiring')
        if not isinstance(w, dict):
            fails.append(f"module:{row.get('module')} has no `wiring:` block — a module contract "
                         f"without a build state is invisible to the port work-list. Add one, or "
                         f"say in the row why this module has no build state.")
            continue
        entries.append((f"module:{row.get('module')}", w))

    # 2) every adapter tag resolves to engine/cross_scale/<name>.py, and coverage is total
    declared = contracts.get('adapters') or {}
    try:
        on_disk = {f[:-3] for f in os.listdir(ADAPTER_DIR)
                   if f.endswith('.py') and not f.startswith('__')}
    except OSError as exc:
        return fails + [f'cannot read {os.path.relpath(ADAPTER_DIR, REPO)}: {exc}']
    for name in sorted(set(declared) - on_disk):
        fails.append(f'adapter:{name} does not resolve in engine/cross_scale/ — renamed or moved?')
    # Coverage counts tags that RESOLVE, not tags that exist: a renamed row keeps len(declared)
    # at 8 and would otherwise print "8/8" on the same run that reports the rename as a failure.
    resolving = len(set(declared) & on_disk)
    for name in sorted(on_disk - set(declared)):
        fails.append(f'adapter coverage {resolving}/{len(on_disk)} — engine/cross_scale/{name}.py '
                     f'is undeclared. Every cross-scale seam is a conversion unit; add its row.')
    entries += [(f'adapter:{n}', e) for n, e in declared.items()]

    # 3) valid vocabulary on every entry
    for tag, e in entries:
        if e.get('build') not in builds:
            fails.append(f'{tag} bad build state {e.get("build")!r} — not in wiring_vocabularies.build_states')
        if e.get('godot') not in godots:
            fails.append(f'{tag} bad godot state {e.get("godot")!r} — not in wiring_vocabularies.godot_states')
    return fails


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
    contracts = ci_common.load_yaml(SRC, default=None) or {}
    wiring_fails = validate_wiring(contracts)
    if wiring_fails:
        print('[composition] wiring FAILED validation in references/module_contracts.yaml:')
        for f in wiring_fails:
            print('   -', f)
        return 1

    text = json.dumps(build(), indent=2, sort_keys=False) + '\n'
    if '--check' in argv:
        if not os.path.exists(OUT):
            print(f'[composition] MISSING {os.path.relpath(OUT, REPO)} — run without --check.')
            return 1
        if open(OUT).read() != text:
            print(f'[composition] DRIFT — {os.path.relpath(OUT, REPO)} is stale. '
                  f'Run: python3 tools/export_composition.py')
            return 1
        print(f'[composition] OK — {len(json.loads(text)["roles"])} role(s), every target resolved; '
              f'wiring valid for {len(contracts.get("modules") or [])} module(s) + '
              f'{len(contracts.get("adapters") or {})} adapter(s).')
        return 0
    with open(OUT, 'w') as fh:
        fh.write(text)
    print(f'[composition] wrote {os.path.relpath(OUT, REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
