#!/usr/bin/env python3
"""ci_vacuous_assertion_check.py — find assertions that cannot fail.

ED-IN-0098, 2026-07-30. REPORT-ONLY.

WHY THIS EXISTS
---------------
CLAUDE.md §0.1 #2 says: "An assertion must be able to observe the failure it excludes." Until now
that was enforced by vigilance alone, and vigilance measurably failed — twice, in the same wave:

  * `assert sa.ci_common.has_main_guard is not None  # single-owner delegation, not a re-copy`
    A module-level function is never None. The comment claimed coverage the line did not provide.
  * `assert st['drift'] >= 0  # the scope may be resolving to nothing again`
    `drift` is an integer file COUNT. This was written *by the session that had just fixed the
    first one*, citing §0.1 #2 in its own commit message.

Two instances, one session, one of them introduced while fixing the other. That is a pattern
defect by §0.1 #5's own signature, and the remedy §0.1 #5 prescribes is a guard — "if you cannot
write the guard you have not understood the pattern".

WHAT IT DETECTS, AND HOW CONFIDENT EACH RULE IS
----------------------------------------------
Two tiers, because precision matters more than reach for a tool people are meant to trust:

PROVABLE — the expression is unfalsifiable by construction. Zero false positives by design.
  V1  `assert <truthy literal>`            e.g. assert True / assert 1 / assert "x" / assert [1]
  V2  `assert len(...) >= 0` / `> -1`      len() is non-negative for every object
  V3  `assert <name> is not None` where `<name>` is a `def`/`class`/`import` in the SAME module —
      a function, class or module object is never None
  V4  `assert isinstance(x, object)`       true for every value
  V5  `assert <lit> == <same lit>`         a literal compared with itself

SUSPICIOUS — heuristic, needs a human. Reported separately and never counted as a violation.
  S1  `assert <expr> >= 0` where the expression names a count-ish thing (count/drift/total/
      len/size/n_/num/idx) — the `drift >= 0` shape. Cannot be proven statically without types,
      which is exactly why it is advisory.
  S2  `assert <attribute chain> is not None` with no call anywhere in it — often a legitimate
      optional check, sometimes the `has_main_guard` shape. Reported so a reviewer can judge.

HONEST LIMITS
-------------
Static and single-file. It cannot resolve imported names through modules (S2 exists because of
that), cannot see types, and says nothing about assertions that are *weak* rather than vacuous
(`assertAlmostEqual` on an exactness claim — §0.1 #2's other example — is out of scope here).
REPORT-ONLY: promoting PROVABLE to blocking is a reasonable next step and Jordan's call.

USAGE
    python3 tools/ci_vacuous_assertion_check.py                 # scan tests/valoria + engine/tests
    python3 tools/ci_vacuous_assertion_check.py --path tests/valoria/test_foo.py
    python3 tools/ci_vacuous_assertion_check.py --suspicious    # also list the heuristic tier
    python3 tools/ci_vacuous_assertion_check.py --json
"""
from __future__ import annotations

import argparse
import ast
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_ROOTS = ('tests/valoria', 'engine/tests')

COUNTISH = ('count', 'drift', 'total', 'len', 'size', 'num', 'n_', 'idx', 'index', 'depth')


def _is_truthy_literal(node: ast.AST) -> bool:
    """A constant/collection literal that is always truthy."""
    if isinstance(node, ast.Constant):
        return bool(node.value)
    if isinstance(node, (ast.List, ast.Tuple, ast.Set)):
        return len(node.elts) > 0
    if isinstance(node, ast.Dict):
        return len(node.keys) > 0
    return False


def _const_num(node: ast.AST):
    """Numeric value of a constant, handling unary minus.

    `-1` is NOT `Constant(-1)` in the AST — it is `UnaryOp(USub, Constant(1))`. Comparing
    `node.value == -1` therefore silently never matches, which is how `len(x) > -1` slipped past
    the first version of this tool (caught by its own test — see
    tests/valoria/test_vacuous_assertion_check.py).
    """
    if isinstance(node, ast.Constant) and isinstance(node.value, (int, float)) \
            and not isinstance(node.value, bool):
        return node.value
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        inner = _const_num(node.operand)
        return None if inner is None else -inner
    return None


def _call_name(node: ast.AST) -> str | None:
    if isinstance(node, ast.Call):
        f = node.func
        if isinstance(f, ast.Name):
            return f.id
        if isinstance(f, ast.Attribute):
            return f.attr
    return None


def _dotted(node: ast.AST) -> str | None:
    """'a.b.c' for a pure Name/Attribute chain; None if any call/subscript is involved."""
    parts = []
    cur = node
    while isinstance(cur, ast.Attribute):
        parts.append(cur.attr)
        cur = cur.value
    if isinstance(cur, ast.Name):
        parts.append(cur.id)
        return '.'.join(reversed(parts))
    return None


def _module_level_defs(tree: ast.Module) -> set[str]:
    """Names bound to a def/class/import at module level — objects that are never None."""
    names: set[str] = set()
    for node in tree.body:
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            names.add(node.name)
        elif isinstance(node, ast.Import):
            for a in node.names:
                names.add(a.asname or a.name.split('.')[0])
        elif isinstance(node, ast.ImportFrom):
            for a in node.names:
                if a.name != '*':
                    names.add(a.asname or a.name)
    return names


def _src(node: ast.AST, lines: list[str]) -> str:
    try:
        return lines[node.lineno - 1].strip()
    except Exception:
        return ''


def scan_file(path: str) -> tuple[list[dict], list[dict]]:
    """Return (provable, suspicious) findings for one file."""
    try:
        text = open(path, encoding='utf-8', errors='replace').read()
        tree = ast.parse(text)
    except (SyntaxError, OSError):
        return [], []
    lines = text.splitlines()
    defs = _module_level_defs(tree)
    provable: list[dict] = []
    suspicious: list[dict] = []

    for node in ast.walk(tree):
        if not isinstance(node, ast.Assert):
            continue
        t = node.test
        rel = os.path.relpath(path, ROOT)
        base = {'file': rel, 'line': node.lineno, 'source': _src(node, lines)}

        # V1 — truthy literal
        if _is_truthy_literal(t):
            provable.append({**base, 'rule': 'V1', 'why': 'asserts a literal that is always truthy'})
            continue

        # V4 — isinstance(x, object)
        if _call_name(t) == 'isinstance' and isinstance(t, ast.Call) and len(t.args) == 2:
            second = t.args[1]
            if isinstance(second, ast.Name) and second.id == 'object':
                provable.append({**base, 'rule': 'V4', 'why': 'isinstance(x, object) is true for every value'})
                continue

        if isinstance(t, ast.Compare) and len(t.ops) == 1 and len(t.comparators) == 1:
            op, left, right = t.ops[0], t.left, t.comparators[0]

            # V2 — len(...) >= 0  /  len(...) > -1
            if _call_name(left) == 'len':
                if isinstance(op, ast.GtE) and _const_num(right) == 0:
                    provable.append({**base, 'rule': 'V2', 'why': 'len() is never negative'})
                    continue
                if isinstance(op, ast.Gt) and _const_num(right) == -1:
                    provable.append({**base, 'rule': 'V2', 'why': 'len() > -1 is always true'})
                    continue

            # V5 — literal compared with itself
            if isinstance(op, ast.Eq) and isinstance(left, ast.Constant) and isinstance(right, ast.Constant) \
                    and left.value == right.value:
                provable.append({**base, 'rule': 'V5', 'why': 'a literal compared with itself'})
                continue

            # V6 — `0 * anything == 0`: an arithmetic identity, not a claim about the system.
            #
            # Added on FIELD EVIDENCE, not speculation: the PC lane independently hit this exact
            # shape (`assert 0.0 * edge == 0.0`) and recorded it as "a property of floating-point
            # multiplication, not of the engine ... third instance of this defect class in this
            # arc". Two lanes reaching the same defect class in one week is the §0.1 #5 signature.
            # Caveat stated rather than hidden: it is vacuous for FINITE operands — `0.0 * nan`
            # and `0.0 * inf` are nan, so a test deliberately probing non-finite values is a real
            # claim. That case is vanishingly rare next to the zero-gain idiom, and this tier is
            # report-only, so a human reads it either way.
            if isinstance(op, ast.Eq) and isinstance(left, ast.BinOp) and isinstance(left.op, ast.Mult) \
                    and _const_num(right) == 0:
                if _const_num(left.left) == 0 or _const_num(left.right) == 0:
                    provable.append({**base, 'rule': 'V6',
                                     'why': 'zero times anything equals zero — an arithmetic '
                                            'identity, not a property of the system under test'})
                    continue

            # V3 / S2 — `is not None`
            if isinstance(op, ast.IsNot) and isinstance(right, ast.Constant) and right.value is None:
                dotted = _dotted(left)
                if dotted and dotted.split('.')[0] in defs and '.' not in dotted:
                    provable.append({**base, 'rule': 'V3',
                                     'why': f'{dotted!r} is a def/class/import in this module — never None'})
                    continue
                if dotted:
                    suspicious.append({**base, 'rule': 'S2',
                                       'why': f'{dotted!r} is a plain attribute chain; confirm it can be None'})
                    continue

            # S1 — count-ish >= 0
            if isinstance(op, ast.GtE) and _const_num(right) == 0:
                blob = ast.dump(left).lower()
                if any(k in blob for k in COUNTISH):
                    suspicious.append({**base, 'rule': 'S1',
                                       'why': 'looks like a non-negative count compared >= 0'})
                    continue
    return provable, suspicious


def iter_py(roots: list[str]):
    for r in roots:
        full = os.path.join(ROOT, r)
        if os.path.isfile(full):
            yield full
            continue
        for dirpath, dirnames, filenames in os.walk(full):
            dirnames[:] = [d for d in dirnames if d not in ('__pycache__', 'deprecated')]
            for fn in filenames:
                if fn.endswith('.py'):
                    yield os.path.join(dirpath, fn)


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--path', action='append', default=None, help='file or dir (repeatable)')
    ap.add_argument('--suspicious', action='store_true', help='also print the heuristic tier')
    ap.add_argument('--json', action='store_true', dest='as_json')
    args = ap.parse_args(argv)

    roots = args.path or list(DEFAULT_ROOTS)
    provable: list[dict] = []
    suspicious: list[dict] = []
    n_files = 0
    for f in iter_py(roots):
        n_files += 1
        p, s = scan_file(f)
        provable += p
        suspicious += s

    if args.as_json:
        print(json.dumps({'files_scanned': n_files, 'provable': provable,
                          'suspicious': suspicious}, indent=2))
        return 0

    print(f'[vacuous-assert] scanned {n_files} file(s) under {", ".join(roots)}')
    if provable:
        print(f'\n[vacuous-assert ✗] {len(provable)} PROVABLY VACUOUS assertion(s) — cannot fail:')
        for f in provable:
            print(f"  {f['file']}:{f['line']}  [{f['rule']}] {f['why']}")
            print(f"      {f['source']}")
    else:
        print('[vacuous-assert ✓] no provably-vacuous assertions found')

    if suspicious:
        if args.suspicious:
            print(f'\n[vacuous-assert ~] {len(suspicious)} suspicious (heuristic — judge each):')
            for f in suspicious:
                print(f"  {f['file']}:{f['line']}  [{f['rule']}] {f['why']}")
                print(f"      {f['source']}")
        else:
            print(f'[vacuous-assert ~] {len(suspicious)} suspicious finding(s) — re-run with '
                  f'--suspicious to list them')
    # REPORT-ONLY: see the module docstring. Promoting PROVABLE to blocking is Jordan's call.
    return 0


if __name__ == '__main__':
    sys.exit(main())
