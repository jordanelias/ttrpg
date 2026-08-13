#!/usr/bin/env python3
"""Report modules that read a registry directly when a single owner already exists for it.

WHAT "SINGLE OWNER" MEANS HERE, defined at the point of use because the next session will meet
this word in a job name before it meets any prose (CLAUDE.md §4): a registry file has ONE module
responsible for reading and interpreting it. Everyone else calls that module. CLAUDE.md §8 states
the rule ("every rule lives once ... never re-implement a rule"); this reports where the tree does
not match it.

WHY IT KEYS ON THE FILE AND NOT ON THE WORDS "SINGLE OWNER".

The obvious build is to grep for modules that claim ownership and check whether others honour it.
That fails the same way three earlier scans in this repo failed, and it would be this programme's
signature defect one level up: a phrase in a comment is not the property. `tools/pathres.py`
declared itself "THE path-reference owner" for months while four other modules parsed the same
file, and the declaration is precisely what stopped readers from checking.

So the question asked here is factual: **does this module build a path to the registry itself?**
That has an answer independent of what anyone wrote about it.

AND WHY IT PARSES RATHER THAN GREPS. A first version of this check used regex over file text and
reported `build_engine_atlas.py` as a parser of the alias ledger. It is not — it *mentions* the
filename in a comment. Comments and docstrings discuss registries constantly in this repo, so a
text scan measures prose density. This walks the AST and looks only at **string constants outside
docstrings**, i.e. values the code actually computes with. Same lesson as `tools/pathres.py`'s
module header, arrived at again from a different direction.

REPORT-ONLY, AND IT REDS ON DAY ONE BY DESIGN. There are known bypasses right now — that is the
finding, not a regression. Blocking on them would refuse unrelated commits for a pre-existing
condition, which ED-IN-0112 already paid for. `--check` compares against the recorded baseline and
fails only if the count GROWS.

    python3 tools/single_owner_check.py
    python3 tools/single_owner_check.py --check
"""
from __future__ import annotations

import argparse
import ast
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import ci_common  # noqa: E402

REPO = ci_common.REPO

# Registry -> the module responsible for reading it. `match` is tested against string constants
# the code computes with, so a filename is enough; `owner_import` is the module name a caller
# imports to go through the owner instead.
OWNED = {
    'references/restructure_ledger.md': {
        'owner': 'tools/pathres.py',
        'owner_import': 'pathres',
        'match': ('restructure_ledger.md',),
        'what': 'the old-path -> new-path alias map',
    },
    'registers/editorial_ledger*.jsonl': {
        'owner': 'tools/observability/obs_core.py',
        'owner_import': 'obs_core',
        'match': ('editorial_ledger.jsonl', 'editorial_ledger_'),
        'what': 'the editorial ledger and its per-lane files',
    },
    'references/id_reservations.yaml': {
        'owner': 'tools/registry.py',
        'owner_import': 'registry',
        'match': ('id_reservations.yaml',),
        'what': 'the ID allocation register',
    },
}

# MEASURED 2026-08-13 (ED-IN-0180) AFTER excluding this file — see find_bypasses(). The first run
# reported 17 because the instrument matched its own OWNED table. The honest number is 14.
# Shrink it as Phase A2 and the obs_core migration land — never grow it to make a run pass.
BASELINE = 14


def _docstring_nodes(tree):
    """Constant nodes that are docstrings — excluded, they are prose about registries."""
    out = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.ClassDef, ast.FunctionDef, ast.AsyncFunctionDef)):
            body = getattr(node, 'body', None)
            if body and isinstance(body[0], ast.Expr) and isinstance(body[0].value, ast.Constant) \
                    and isinstance(body[0].value.value, str):
                out.add(id(body[0].value))
    return out


def module_reads(path: str) -> tuple[set[str], set[str]]:
    """(string constants the code computes with, imported module names)."""
    try:
        src = open(path, encoding='utf-8', errors='ignore').read()
        tree = ast.parse(src)
    except (SyntaxError, ValueError):
        return set(), set()
    skip = _docstring_nodes(tree)
    consts, imports = set(), set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, str) and id(node) not in skip:
            consts.add(node.value)
        elif isinstance(node, ast.Import):
            imports.update(a.name.split('.')[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom):
            if node.module:
                imports.add(node.module.split('.')[0])
            imports.update(a.name for a in node.names)
    return consts, imports


def _modules():
    for base in ('tools', '.githooks', 'skills'):
        root = os.path.join(REPO, base)
        if not os.path.isdir(root):
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d != '__pycache__']
            for fn in filenames:
                if fn.endswith('.py'):
                    p = os.path.join(dirpath, fn)
                    yield os.path.relpath(p, REPO).replace(os.sep, '/'), p


def find_bypasses():
    """{registry: [modules that build a path to it without going through the owner]}"""
    out = {}
    for registry, spec in OWNED.items():
        hits = []
        for rel, abspath in _modules():
            if rel == spec['owner']:
                continue
            # THE INSTRUMENT COUNTS ITSELF UNLESS TOLD NOT TO, and it did on its first run —
            # reporting itself as a bypass of all three registries, because its OWNED table names
            # them as string constants. That is ED-IN-0159 §2.4 ("the instrument counted itself")
            # recurring verbatim in a new instrument, which is worth more than the fix: a census
            # whose configuration mentions its own subject is self-matching BY CONSTRUCTION, and
            # the only reliable defence is to check the raw output for the tool's own name before
            # believing a number. Excluded explicitly rather than by a path heuristic, so the
            # exclusion is one named file and cannot quietly widen.
            if rel == 'tools/single_owner_check.py':
                continue
            consts, imports = module_reads(abspath)
            touches = any(any(m in c for m in spec['match']) for c in consts)
            if touches and spec['owner_import'] not in imports:
                hits.append(rel)
        out[registry] = sorted(hits)
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument('--check', action='store_true', help='exit 1 if the bypass count grew')
    args = ap.parse_args(argv)

    found = find_bypasses()
    total = sum(len(v) for v in found.values())

    for registry, hits in found.items():
        spec = OWNED[registry]
        print(f'\n{registry}  —  {spec["what"]}')
        print(f'  owner: {spec["owner"]}')
        if not hits:
            print('  no bypasses')
        for h in hits:
            print(f'  BYPASS  {h}')

    print(f'\n{"=" * 70}\n{total} module(s) read an owned registry directly (baseline {BASELINE}).')
    print('Report-only: these are known, and each needs its own migration with an expected-delta')
    print('test (CLAUDE.md §8). The number may shrink, never grow.')

    if args.check:
        if total > BASELINE:
            print(f'\n[single-owner FAIL] bypasses grew {BASELINE} -> {total}. A new module started '
                  f'reading an owned registry directly; route it through the owner instead.')
            return 1
        if total < BASELINE:
            print(f'\n[single-owner] bypasses SHRANK {BASELINE} -> {total} — lower BASELINE to '
                  f'{total} in this same commit so the ratchet holds.')
        print('\n[single-owner OK] no new direct readers.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
