"""`modules/**` EQUALS THE REACHABLE CLOSURE, IN BOTH DIRECTIONS -- `SM-7`, built at plan position `31c`
(IN-05).

A-25 places in `modules/` the running code the season loop reaches, and nothing else: `31a`-`31c` moved a
module's reachable closure out of `systems/` and left the unreached files (workbenches, harnesses) behind.
`modules/` is the port's input set (GO-05's manifest resource lists `modules/**`), so a file there that
nothing reaches is dead weight the port would carry, and a file the closure reaches that stayed in
`systems/` is a module the port would get half of. Licensed by `CLAUDE.md` §0.1 pt 5: the artifact is
load-bearing on the port.

THE WALK. Roots: every composition row (`references/module_contracts.yaml`, read through
`engine.substrate.composition`) that carries `entry:` and targets a package under `modules/`. From each
root, every `import`/`from ... import` in the file -- module scope and function-local alike, so a lazy
import counts -- that resolves to a repository `.py` file is followed; the package `__init__.py` of every
reached module is reached too. The two directions:
  1. EVERY `.py` file under the module's directory is reached (a planted unreached file is red);
  2. NOTHING the closure reaches lies under `systems/` (the closure moved whole). The host (`engine/`) is
     not module code and is not walked: a module imports its record type and the dice engine from there.

SCOPE, AND THE ONE EXCLUSION, BY SHAPE AND NOT BY NAME. A module directory WITH an `__init__.py` is a
package whose files import each other by dotted name, which this walk follows (`social_contest`,
`mass_battle`). A directory WITHOUT one is a FLAT script set loaded through a declared path seam
(`modules/combat/`, loaded by `engine/substrate/pc_engine.py` with `importlib.import_module('wrapper')`):
its entry reaches the engine by a string this walk cannot follow, so the walk would report the whole engine
unreached. Such a directory is listed in the test's output, not checked; checking it is a walk that follows
the path seam, which is not this position's.
"""
from __future__ import annotations

import ast
import os
import sys

import pytest

from engine.substrate import composition

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULES = "modules"


def _file_of(dotted: str):
    """The repository file a dotted module name loads from, or None (stdlib, third-party, absent)."""
    base = os.path.join(ROOT, *dotted.split("."))
    for cand in (base + ".py", os.path.join(base, "__init__.py")):
        if os.path.isfile(cand):
            return cand
    return None


def _imports(path: str, dotted: str) -> list:
    """Every dotted name `path` imports, at any depth of the file, relative imports resolved."""
    tree = ast.parse(open(path, encoding="utf-8").read(), filename=path)
    package = dotted if path.endswith("__init__.py") else dotted.rsplit(".", 1)[0]
    names = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            names += [a.name for a in node.names]
        elif isinstance(node, ast.ImportFrom):
            if node.level:
                parts = package.split(".")
                stem = ".".join(parts[:len(parts) - node.level + 1])
                base = f"{stem}.{node.module}" if node.module else stem
            else:
                base = node.module
            names.append(base)
            names += [f"{base}.{a.name}" for a in node.names if a.name != "*"]   # `from pkg import submodule`
    return names


def closure(roots: list) -> set:
    """Repository files reached from `roots` (dotted module names), walking only module code: a file
    under `engine/` is recorded as reached and not walked further (the host is not module code)."""
    seen, stack = set(), list(roots)
    while stack:
        dotted = stack.pop()
        path = _file_of(dotted)
        if path is None or path in seen:
            continue
        seen.add(path)
        parts = dotted.split(".")
        stack += [".".join(parts[:i]) for i in range(1, len(parts))]   # the parent packages
        if os.path.relpath(path, ROOT).split(os.sep)[0] == "engine":
            continue
        stack += _imports(path, dotted)
    return seen


def _module_files(directory: str) -> set:
    out = set()
    for dirpath, dirs, files in os.walk(directory):
        dirs[:] = [d for d in dirs if d != "__pycache__"]
        out |= {os.path.join(dirpath, f) for f in files if f.endswith(".py")}
    return out


def _entry_roots() -> dict:
    """{module directory: [entry module, ...]} for every composition entry row targeting `modules/`."""
    roots = {}
    for role, row in composition.ROLES.items():
        mod = str(row.get("target", "")).split(":", 1)[0]
        if row.get("entry") and mod.split(".")[0] == MODULES:
            roots.setdefault(os.path.join(ROOT, *mod.split(".")[:2]), []).append(mod)
    return roots


def _rel(paths) -> list:
    return sorted(os.path.relpath(p, ROOT) for p in paths)


def check(module_dir: str, roots: list) -> tuple:
    """`(unreached, left_behind)` for one package module: files under `module_dir` the walk from `roots`
    does not reach, and files the walk reaches under `systems/`."""
    reached = closure(roots)
    unreached = _module_files(module_dir) - reached
    left_behind = {p for p in reached if os.path.relpath(p, ROOT).split(os.sep)[0] == "systems"}
    return unreached, left_behind


def test_every_package_module_is_exactly_its_entries_reachable_closure():
    roots = _entry_roots()
    packages = {d: r for d, r in roots.items() if os.path.isfile(os.path.join(d, "__init__.py"))}
    flat = sorted(set(roots) - set(packages))
    checked = []
    for module_dir, entry_modules in sorted(packages.items()):
        unreached, left_behind = check(module_dir, entry_modules)
        assert not unreached, (
            f"{os.path.relpath(module_dir, ROOT)}: files no entry reaches ({entry_modules}): "
            f"{_rel(unreached)}. `modules/` holds the reachable closure only (A-25); an unreached file goes "
            "back to `systems/` or is deleted")
        assert not left_behind, (
            f"{os.path.relpath(module_dir, ROOT)}: its closure reaches files left in `systems/`: "
            f"{_rel(left_behind)}. The closure moves whole")
        checked.append(os.path.relpath(module_dir, ROOT))
    assert os.path.join(MODULES, "mass_battle") in checked, (
        f"the walk checked {checked} and not `modules/mass_battle`, the package `31c` moved; the roots "
        f"are read from the composition rows -- has its entry row lost `entry:`? (flat, not walked: {flat})")


def test_the_walk_sees_a_planted_unreached_file_and_a_closure_left_behind(tmp_path, monkeypatch):
    """The check can observe both failures it excludes (`CLAUDE.md` §0.1 pt 2), on a planted tree: a
    package whose entry imports a sibling and, lazily, a `systems/` file, beside a file nothing imports."""
    def write(rel, text=""):
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(text)
    write("modules/__init__.py")
    write("modules/m/__init__.py")
    write("modules/m/entry.py", "from modules.m import used\n\ndef run():\n    import systems.s.sim.old\n")
    write("modules/m/used.py")
    write("modules/m/orphan.py")
    write("systems/__init__.py")
    write("systems/s/__init__.py")
    write("systems/s/sim/__init__.py")
    write("systems/s/sim/old.py")
    monkeypatch.setattr(sys.modules[__name__], "ROOT", str(tmp_path))
    unreached, left_behind = check(str(tmp_path / "modules" / "m"), ["modules.m.entry"])
    assert _rel(unreached) == [os.path.join("modules", "m", "orphan.py")], _rel(unreached)
    assert os.path.join("systems", "s", "sim", "old.py") in _rel(left_behind), _rel(left_behind)


if __name__ == "__main__":   # pragma: no cover
    pytest.main([__file__, "-q"])
