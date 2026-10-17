"""THE CLOSURE SCAN -- the one AST walk that finds game code branching on a literal id (scripting drift).

SC-01 step 16 wrote it for arrangement ids (`test_sc01_the_bar.py`); v9 FI-03 (`ED-FI-0002`) runs it for
entity ids (`test_fi03_trail.py`). This is the one copy; each caller passes its own id set and keeps its
own floor, membership assert and planted falsifier. Nothing here asserts anything.

WHAT IT READS: an `ast.Compare` or a `match` value case is reported when an operand is a string LITERAL
(or a tuple, list or set of them) in `ids`. NOT SEEN: an id reached without a literal comparison (a dict
keyed by the id, `.get("<id>")`, a named constant, an id built at runtime) -- a lookup is not a branch.
"""
from __future__ import annotations

import ast

from ..data import files


def branches_on_ids(tree: ast.AST, ids) -> list:
    """`(line, id)` for every comparison or `match` case in `tree` whose operand is a literal in `ids`."""
    ids, hits = set(ids), []

    def consts(node):
        if isinstance(node, ast.Constant):
            return [node.value]
        if isinstance(node, (ast.Tuple, ast.List, ast.Set)):
            return [e.value for e in node.elts if isinstance(e, ast.Constant)]
        return []
    for node in ast.walk(tree):
        if isinstance(node, ast.Compare):
            vals = consts(node.left) + [v for c in node.comparators for v in consts(c)]
        elif isinstance(node, ast.MatchValue):
            vals = consts(node.value)
        else:
            continue
        hits += [(node.lineno, v) for v in vals if isinstance(v, str) and v in ids]
    return hits


def game_code() -> list:
    """THE SCOPE: every `.py` under `engine/season/` outside `engine/season/tests/` (the harness included),
    plus every `.py` under `modules/`. `engine/` outside `season/`, and any other tree, is not scanned."""
    paths = [f for f in files.package_modules() if files.TESTS_DIR not in f.parents]
    return paths + sorted((files.REPO_ROOT / "modules").rglob("*.py"))
