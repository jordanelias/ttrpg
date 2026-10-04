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

A row may also declare a MODULE ENTRY KIND on a second key, `entry:` (`verb_call` with its `verb:`,
`step_call` or `query`), which `engine/season/manifest/registrar.py` reads at driver construction.
See `_ENTRIES`; it is validated here beside `kind:` (plan position `30`, A-25).

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

#: A row's MODULE ENTRY KIND (plan position `30`; A-25, `ED-IN-0284` revised by `ED-IN-0285`) --
#: HOW the season loop calls the target, on a SECOND key, `entry:`, because `kind:` already means
#: callable-or-value (`CLAUDE.md` §4: one key, one meaning). Defined here, the one owner of the
#: closed set, and in `engine/season/manifest/registrar.py`, where the registrar reads it:
#:   `verb_call`  -- a verb's loop-side adapter calls it; the row names that verb in `verb:`.
#:   `step_call`  -- a loop step calls it (MATTER, for instance).
#:   `query`      -- a projection consumer calls it.
#: A row with no `entry:` is not a module entry and keeps whatever caller already `require()`s it
#: (`mass_battle.resolve_field` today, re-keyed at `31c`). Validated here, at export, beside `kind:`;
#: `entry:` and `verb:` are cooked into every row, `None` where absent, so the artifact has one shape.
_ENTRIES = ('verb_call', 'step_call', 'query')
_VERB_ENTRY = _ENTRIES[0]


def _check_entry(role, row):
    """Refuse a malformed `entry:`/`verb:` pair, naming the role. Returns `(entry, verb)`."""
    entry = row.get('entry') if isinstance(row, dict) else None
    verb = row.get('verb') if isinstance(row, dict) else None
    if entry is None:
        if verb is not None:
            raise SystemExit(f'composition_roles {role!r}: `verb: {verb!r}` with no `entry:` -- only '
                             f'an `entry: {_VERB_ENTRY}` row names a verb.')
        return None, None
    if entry not in _ENTRIES:
        raise SystemExit(f'composition_roles {role!r}: entry {entry!r} must be one of {_ENTRIES}.')
    kind = (row.get('kind') or 'callable')
    if kind != 'callable':
        raise SystemExit(f'composition_roles {role!r}: `entry: {entry}` on a `kind: {kind}` row -- a '
                         f'module entry is something the loop CALLS, so its row is `kind: callable`.')
    # one predicate for "names a verb" in both branches: a `verb_call` row carries a non-empty string,
    # and every other entry kind carries none (`verb is None`, as the no-entry branch above reads it)
    named = isinstance(verb, str) and bool(verb.strip())
    if (entry == _VERB_ENTRY and not named) or (entry != _VERB_ENTRY and verb is not None):
        raise SystemExit(f'composition_roles {role!r}: `entry: {entry}` with `verb: {verb!r}` -- a '
                         f'`{_VERB_ENTRY}` row names its verb, and no other entry kind names one.')
    return entry, verb


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


def validate_wiring(contracts):
    """Return a list of failures in the `wiring:` facts (empty == green).

    TWO OF THE FIVE RULES `tools/wiring_map_check.py --check` ENFORCED ARE GONE, AND NOT BECAUSE
    THEY WERE DROPPED. It checked that every wiring tag resolved to a module contract, and that
    module coverage was 27/27, against a SEPARATE registry keyed by the same module names. Folding
    those facts onto the row they describe removes the second key space that could disagree.

    ⚠ THAT IS TRUE ONLY BECAUSE RULE 1 BELOW ENFORCES THE KEYING, AND THE FIRST VERSION OF THIS
    FUNCTION DID NOT. "The registry cannot disagree with itself" holds for a YAML MAP, which is
    what the manifest was; `modules:` here is a LIST, where two rows may claim one name and a row
    may claim none. Shipped that way, a duplicated row validated as 28 modules and an unnamed row
    as 27 — both silent, and both fatal to consumers that re-key the list by name. So rule 1 is
    three assertions, not one: named, uniquely named, and carrying wiring. Structural is a claim
    about a data shape, and a list is not the shape that earns it for free.

    The adapter rules (resolution, coverage) that were ported verbatim from it retired at plan
    position `28-iii` (2026-10-01) with `engine/cross_scale/` and the `adapters:` block; vocabulary
    is the one that remains below.

    FALSIFIER: `tests/valoria/test_wiring_validation.py`. It replaces the falsifier S5c deleted
    with `wiring_map_check.py`, and it is not optional bookkeeping — for one commit these rules
    lived in a tool with no test at all while the checks registry claimed they were verified.

    """
    fails = []
    vocab = contracts.get('wiring_vocabularies') or {}
    builds, godots = set(vocab.get('build_states') or ()), set(vocab.get('godot_states') or ())
    if not builds or not godots:
        return ['module_contracts.yaml: wiring_vocabularies is missing build_states/godot_states — '
                'every wiring row below is unvalidatable without it.']

    # 1) every module row is NAMED, named UNIQUELY, and carries wiring facts.
    #
    # THE NAME RULES ARE NOT DECORATION, AND THEY ARE THE HALF THIS TOOL FIRST SHIPPED WITHOUT.
    # The retired manifest stored wiring under a YAML MAP (`modules: {victory: {...}}`), so
    # duplicate and missing keys were impossible by construction. `modules:` here is a LIST of
    # rows, which has no such guarantee — and every consumer of the fold re-keys that list by
    # `module` (build_contract_index's `wmods`, build_execution_map's `by_name`, build_fork's
    # `states`), where a duplicate silently keeps the LAST row and an unnamed row silently
    # becomes `None`. The commit that landed the fold claimed coverage was now "structural";
    # an adversarial pass showed a duplicated row validating as 28 modules and an unnamed row
    # validating as 27. Both are caught here, so the claim is true rather than nearly true.
    entries = []
    seen = {}
    for i, row in enumerate(contracts.get('modules') or []):
        name = row.get('module')
        if not name:
            fails.append(f'modules[{i}] has no `module:` name. An unnamed row cannot be joined to '
                         f'anything and disappears into every consumer that keys this list by name.')
            continue
        if name in seen:
            fails.append(f'module:{name} is declared twice (rows {seen[name]} and {i}). Consumers '
                         f're-key this list by name and silently keep the last row, so the earlier '
                         f"contract's Key edges and wiring facts would vanish without an error.")
            continue
        seen[name] = i
        w = row.get('wiring')
        if not isinstance(w, dict):
            fails.append(f"module:{name} has no `wiring:` block — a module contract without a "
                         f"build state is invisible to the port work-list. Add one, or say in the "
                         f"row why this module has no build state.")
            continue
        entries.append((f'module:{name}', w))

    # 2) valid vocabulary on every entry
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
                         'block was removed, nothing resolves through engine/substrate/composition.py '
                         '— restore it rather than deleting this exporter.')
    out = {}
    for role in sorted(roles):
        row = roles[role]
        target = row['target'] if isinstance(row, dict) else row
        kind = (row.get('kind') if isinstance(row, dict) else None) or 'callable'
        _resolve(target, kind)   # fail HERE, in CI, not at first call during a campaign
        entry, verb = _check_entry(role, row)
        out[role] = {
            'target': target,
            'kind': kind,
            'entry': entry,
            'verb': verb,
            'needed_by': (row.get('needed_by') if isinstance(row, dict) else None),
        }
    return {
        '_generated': (
            'GENERATED by tools/export_composition.py from references/module_contracts.yaml '
            "(composition_roles). NEVER hand-edit: regenerate and commit together. Read at runtime by "
            'engine/substrate/composition.py. Every target is imported and resolved at export time, '
            'so a broken row fails a blocking CI gate rather than a campaign run.'
        ),
        # 2: rows carry `kind` (callable | value), added at plan S5a. 3: rows carry `entry`
        # (verb_call | step_call | query | None) and `verb`, added at plan position `30`.
        'schema_version': 3,
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
              f'wiring valid for {len(contracts.get("modules") or [])} module(s).')
        return 0
    with open(OUT, 'w') as fh:
        fh.write(text)
    print(f'[composition] wrote {os.path.relpath(OUT, REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
