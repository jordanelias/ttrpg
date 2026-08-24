#!/usr/bin/env python3
"""Cook references/module_contracts.yaml's INTERFACE into an artifact code reads at runtime.

WHY THIS EXISTS (Jordan, 2026-08-24 — the hub-and-bus directive)
---------------------------------------------------------------
    "anything that gets emitted by a subsystem must be returned to a centralized location,
     and anything that gets inputted must come from a centralized location"

`references/module_contracts.yaml` already declares that interface — 27 modules with `emits:` and
`consumes:` blocks. What it did NOT have was a cooked form, so the declared interface was reachable
only by parsing the YAML, and TEN tools did exactly that (`test_engine_params_bridge.py`'s
`AUTHORED_PARSERS`). Every one of them re-derives the same three facts.

WHO READS IT TODAY, stated plainly rather than implied. `tools/contract_runtime_conformance.py`,
and nothing under `engine/` or `systems/`. That is an honest difference from its four siblings —
`descriptors.json`, `composition.json`, `key_types.json` and `world_initial_state.json` are all read
at import by the engine, and this one is not. It is the cooked form of the DECLARED interface, which
is what a conformance verdict has to be measured against and what the Godot port needs in order to
know which module owns which Key; it does not yet feed a runtime path, and this paragraph should be
rewritten the day it does rather than left to imply that it already has.

This is the writer half. It emits the INTERFACE ONLY — module name, its implementation path, what it
emits, what it consumes — not the registry's prose (`gap_notes`, `sources`, `loops` narrative). Those
are reference under §0.05 and stay in the YAML, which remains the authored, reviewable surface.

THE `sim_module` BINDING IS THE POINT, and it is why this artifact is more than a convenience. A
contract module name is LOGICAL (`domain_actions`, `social_contest`); the tree is organised by
DIRECTORY (`systems/factions/`, `systems/social_contest/`). Nothing in the tree owned the map
between them, so any instrument trying to attribute a runtime event to a contract had to invent one
— and inventing it is how you get a measurement that reads "0 of 60 declared emissions happen" when
the truth is "my attribution scheme and the registry disagree about what a module is called". That
was measured on 2026-08-24 and is the reason this file exists rather than a private dict inside the
conformance tool.

WHAT IT DELIBERATELY RECORDS RATHER THAN FIXES. Several modules have `sim_module: none` or no
`sim_module` at all (`domain_actions` is the load-bearing case: its home doc is `null` too). Those
are UNATTRIBUTABLE by path, and the artifact says so in `unattributable` instead of guessing a
directory. A guessed binding would make a conformance verdict unfalsifiable.

Usage:
    python3 tools/export_module_contracts.py           # write the artifact
    python3 tools/export_module_contracts.py --check   # re-derive and diff (exit 1 on drift)
"""
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

# `ci_common` owns both of these: the repo root (plan G7 / ED-IN-0159 §8.1 — a module that
# re-derives an ancestor directory is a second owner of the same fact) and the YAML register load.
# Two ratchets in tests/valoria/test_ci_common_primitives.py caught this file doing both by hand.
REPO = ci_common.REPO
SRC = os.path.join(REPO, 'references', 'module_contracts.yaml')
OUT = os.path.join(REPO, 'engine', 'engine_params', 'module_contracts.json')


def _types(entry, side):
    """The Key type_ids on one side of a contract. A `type` may be a bare string or a mapping."""
    out = []
    for x in (entry.get(side) or []):
        t = x.get('type') if isinstance(x, dict) else x
        if isinstance(t, str) and '.' in t and t not in out:
            out.append(t)
    return sorted(out)


def _impl_path(entry):
    """The module's implementation path, or None when the registry does not bind one.

    `sim_module: none` is a DECLARATION that there is no implementation, not a missing field, and it
    is normalised to None here so a consumer cannot accidentally treat the string 'none' as a path.
    """
    p = entry.get('sim_module')
    if not isinstance(p, str) or p.strip().lower() in ('', 'none', 'null'):
        return None
    return p.strip().rstrip('/')


def build():
    doc = ci_common.load_yaml(SRC, default={}) or {}
    modules, unattributable = {}, []
    for entry in doc.get('modules', []):
        name = entry.get('module')
        if not name:
            continue
        path = _impl_path(entry)
        if path is None:
            unattributable.append(name)
        modules[name] = {
            'impl_path': path,
            'doc': entry.get('doc'),
            'emits': _types(entry, 'emits'),
            'consumes': _types(entry, 'consumes'),
        }
    # Longest-prefix-first, so `systems/social_contest/sim/contest/` wins over a shorter sibling.
    by_path = sorted(((v['impl_path'], k) for k, v in modules.items() if v['impl_path']),
                     key=lambda kv: (-len(kv[0]), kv[0]))
    return {
        '_generated': ('GENERATED by tools/export_module_contracts.py from '
                       'references/module_contracts.yaml — the DECLARED Key interface, cooked so '
                       'code reads one artifact instead of ten tools re-parsing the YAML. '
                       'Regenerate with no args; drift-gated by --check.'),
        'schema_version': 1,
        'source': 'references/module_contracts.yaml',
        'module_count': len(modules),
        'emit_edge_count': sum(len(v['emits']) for v in modules.values()),
        'consume_edge_count': sum(len(v['consumes']) for v in modules.values()),
        # module -> {impl_path, doc, emits, consumes}
        'modules': dict(sorted(modules.items())),
        # (impl_path, module) longest-prefix-first: the ONLY owner of directory -> contract module.
        'path_to_module': [list(x) for x in by_path],
        # Modules the registry binds to no implementation path. Recorded, never guessed.
        'unattributable': sorted(unattributable),
    }


def main(argv):
    text = json.dumps(build(), indent=2, sort_keys=False) + '\n'
    if '--check' in argv:
        if not os.path.exists(OUT):
            print(f'[module_contracts] MISSING {os.path.relpath(OUT, REPO)} — run without --check.')
            return 1
        if open(OUT).read() != text:
            print(f'[module_contracts] DRIFT — {os.path.relpath(OUT, REPO)} is stale. '
                  f'Run: python3 tools/export_module_contracts.py')
            return 1
        d = json.loads(text)
        print(f'[module_contracts] OK — {d["module_count"]} module(s), '
              f'{d["emit_edge_count"]} emit edge(s), {d["consume_edge_count"]} consume edge(s), '
              f'{len(d["unattributable"])} unattributable.')
        return 0
    with open(OUT, 'w') as fh:
        fh.write(text)
    print(f'[module_contracts] wrote {os.path.relpath(OUT, REPO)}')
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
