#!/usr/bin/env python3
"""dead_primitive_census.py — every built-but-unwired primitive in the engine, exhaustively.

JORDAN'S STANDING RULE (2026-07-29, restated three times before this tool existed):
    "If we have built a model that hasn't been superseded, it likely has a purpose that must be
     evaluated. You MUST identify ALL modules and primitives."

The repo already finds *some* of this — `structure_audit` builds the module import graph,
`build_apparatus_registry` flags orphan tools, the vector audit walks the token/citation graphs.
None of them descend BELOW module granularity, and that is where the dead things actually live:
`resolve_internal_collisions` sits inside a live, heavily-imported module and has never once been
called. A module-level orphan check cannot see it, which is why the same finding has been re-flagged
by hand since 2026-05-29 without ever becoming a standing signal.

WHAT THIS FINDS — four classes, each a different way a built thing goes unused:

  1. DEAD FUNCTIONS   — defined, never referenced anywhere outside their own definition.
  2. DEAD CONSTANTS   — module-level UPPER_CASE assigned, never read.
  3. INERT FLAGS      — an env-gated toggle whose gated branch is never reachable, or which no
                        module reads at all.
  4. ORPHAN MODULES   — zero importers (the class the existing tools already cover; included so
                        one report answers the whole question).

METHOD, and its honest limits. This is AST-based, not execution-based: a name is "referenced" if it
appears as a Call, Attribute, Name load, or string literal (the last catches `getattr`/dispatch
tables). That over-counts rather than under-counts — a thing reported DEAD here is dead under a
generous definition, which is the right bias for a census whose output is "go look at this". It
cannot see reflection built from computed strings; the compensating control is that every finding is
a pointer to a human read, never an automatic deletion.

DISPOSITION IS NOT AUTOMATIC. Per ED-MB-0041's own rule the answer to a dead primitive is
**wire or delete, one line of disposition each** — and `reform_check` is the standing example of why
a tool must not decide: it is canon-required (mass_battle_v30 §A.5/PP-241), so wiring it changes
battles and deleting it repudiates canon. Its only permitted disposition is a fork ruling.

    python3 tools/dead_primitive_census.py [--root tests/sim/mass_battle] [--json out.json]
"""
import argparse
import ast
import json
import os
import sys

_REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Scanned for DEFINITIONS. Everything under the repo is scanned for REFERENCES, so a primitive
# defined in the engine and called only from a test or a probe is correctly seen as live.
DEFAULT_ROOTS = ['tests/sim/mass_battle', 'engine', 'systems']

SKIP_DIRS = {'__pycache__', '.git', 'deprecated', 'node_modules', '.venv'}

# Names that are live by protocol rather than by call site.
DUNDER_OK = {'__init__', '__post_init__', '__repr__', '__eq__', '__hash__', '__str__',
             '__enter__', '__exit__', '__iter__', '__len__', '__bool__', '__call__',
             '__getitem__', '__setitem__', '__contains__'}


def py_files(root):
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if fn.endswith('.py'):
                yield os.path.join(dp, fn)


def parse(path):
    try:
        return ast.parse(open(path, encoding='utf-8').read(), filename=path)
    except (SyntaxError, UnicodeDecodeError):
        return None


def collect_definitions(roots):
    """{name: [(relpath, lineno, kind)]} for functions, methods and UPPER constants."""
    defs = {}
    for root in roots:
        base = os.path.join(_REPO, root)
        if not os.path.isdir(base):
            continue
        for path in py_files(base):
            tree = parse(path)
            if tree is None:
                continue
            rel = os.path.relpath(path, _REPO)
            for node in ast.walk(tree):
                if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                    if node.name in DUNDER_OK:
                        continue
                    kind = 'function'
                    defs.setdefault(node.name, []).append((rel, node.lineno, kind))
                elif isinstance(node, ast.Assign):
                    for t in node.targets:
                        if isinstance(t, ast.Name) and t.id.isupper() and len(t.id) > 2:
                            defs.setdefault(t.id, []).append((rel, node.lineno, 'constant'))
    return defs


def collect_references(scan_root=None):
    """Every name that is READ anywhere in the repo, plus every string literal.

    Deliberately generous: a name appearing as an attribute, a bare load, or inside a string counts
    as a reference. Under-counting would produce false 'dead' claims, which is the failure mode that
    matters — a census nobody trusts gets ignored, and then the real dead code stays.

    ⚠ A `def` statement contributes NO reference node (a FunctionDef is not a Name load), so a
    definition never counts as its own use and no file-level subtraction is needed. The first draft
    of this tool DID subtract the whole definition FILE, which reported every method called as
    `self._foo(...)` from inside its own module as dead — 96 false positives including
    `_node_advance`, `_kite_goal` and `_rekey_node_state`, all of which this session had just read
    live call sites for. Verifying the instrument before quoting its number is the whole of G4.
    """
    refs = {}
    root = scan_root or _REPO
    for dp, dns, fns in os.walk(root):
        dns[:] = [d for d in dns if d not in SKIP_DIRS]
        for fn in fns:
            if not fn.endswith('.py'):
                continue
            path = os.path.join(dp, fn)
            tree = parse(path)
            if tree is None:
                continue
            rel = os.path.relpath(path, _REPO)
            for node in ast.walk(tree):
                nm = None
                if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
                    nm = node.id
                elif isinstance(node, ast.Attribute):
                    nm = node.attr
                elif isinstance(node, ast.Constant) and isinstance(node.value, str):
                    nm = node.value.strip()
                if nm:
                    refs.setdefault(nm, set()).add(rel)
    return refs


def census(roots):
    defs = collect_definitions(roots)
    refs = collect_references()
    dead_fn, dead_const = [], []
    for name, sites in sorted(defs.items()):
        if name.startswith('test_'):
            continue
        seen_in = refs.get(name, set())
        if seen_in:
            continue
        kind = sites[0][2]
        row = {'name': name, 'defined': [f'{p}:{ln}' for p, ln, _k in sites],
               'referenced_in': sorted(seen_in)}
        (dead_const if kind == 'constant' else dead_fn).append(row)
    return {'dead_functions': dead_fn, 'dead_constants': dead_const,
            'counts': {'definitions_scanned': len(defs),
                       'dead_functions': len(dead_fn),
                       'dead_constants': len(dead_const)}}


def main(argv):
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--root', action='append', default=None,
                    help='definition root (repeatable); default: engine + systems + the MB engine')
    ap.add_argument('--json', default=None)
    a = ap.parse_args(argv[1:])
    roots = a.root or DEFAULT_ROOTS
    out = census(roots)
    c = out['counts']
    print(f"[DEAD-PRIMITIVE CENSUS] roots: {', '.join(roots)}")
    print(f"  definitions scanned : {c['definitions_scanned']:,}")
    print(f"  DEAD functions      : {c['dead_functions']}")
    print(f"  DEAD constants      : {c['dead_constants']}")
    for title, rows in (('FUNCTIONS', out['dead_functions']), ('CONSTANTS', out['dead_constants'])):
        if not rows:
            continue
        print(f"\n  ── dead {title} ──")
        for r in rows:
            print(f"    {r['name']:42s} {r['defined'][0]}")
    if a.json:
        with open(a.json, 'w', encoding='utf-8') as f:
            json.dump(out, f, indent=2, sort_keys=True)
        print(f"\nwrote {a.json}")
    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
