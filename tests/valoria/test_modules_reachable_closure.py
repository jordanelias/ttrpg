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

TWO SHAPES, TOLD APART BY SHAPE AND NOT BY NAME. A module directory WITH an `__init__.py` is a package
whose files import each other by dotted name, which this walk follows (`social_contest`, `mass_battle`).
A directory WITHOUT one is a FLAT script set loaded through a declared path seam (`modules/combat/`,
loaded by `engine/substrate/pc_engine.py`, which puts the directory on `sys.path` and imports its
`PCEngine._fields` by bare name): its entry reaches the engine by strings, so its roots are the entry
PLUS the names the seam itself declares, and a dot-free import resolves to `<directory>/<name>.py` first,
as it does at load. A flat directory with no seam declaring its names fails rather than going unchecked.
In a flat set one more failure is observable: a bare name that resolves to no file in the directory and
to no standard-library or installed module is a file the set needs and does not hold (it would load
from wherever `sys.path` happens to find it, or raise) -- reported beside the files left behind. The
directories checked, of each shape, are printed (`-s`).

NOT CHECKED, RECORDED: DATA a module reads by path. `modules/mass_battle/terrain.py` (`_GEOGRAPHY_YAML`)
reads `systems/settlements/valoria_geography_v30.yaml` -- an input outside `modules/**` the port would
need and this import walk cannot see. Recorded here, not fixed.
"""
from __future__ import annotations

import ast
import importlib.util
import os
import sys

import pytest

from engine.substrate import composition

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
MODULES = "modules"


def _file_of(dotted: str, flat_dir: str | None = None):
    """The repository file a dotted module name loads from, or None (stdlib, third-party, absent). In a
    flat set (`flat_dir`) a dot-free name is the directory's own `<name>.py` first, as at load."""
    if flat_dir and "." not in dotted and os.path.isfile(os.path.join(flat_dir, dotted + ".py")):
        return os.path.join(flat_dir, dotted + ".py")
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


def _external(name: str) -> bool:
    """A dot-free name the standard library or an installed distribution provides (not this repo)."""
    if name in sys.stdlib_module_names:
        return True
    spec = importlib.util.find_spec(name)
    origin = getattr(spec, "origin", None) or ""
    return spec is not None and not os.path.abspath(origin).startswith(ROOT + os.sep)


def closure(roots: list, flat_dir: str | None = None, unresolved: set | None = None) -> set:
    """Repository files reached from `roots` (dotted module names), walking only module code: a file
    under `engine/` is recorded as reached and not walked further (the host is not module code). With
    `flat_dir`, every dot-free name that resolves nowhere and is not `_external` goes into `unresolved`."""
    seen, stack = set(), list(roots)
    while stack:
        dotted = stack.pop()
        path = _file_of(dotted, flat_dir)
        if path is None:
            if flat_dir and unresolved is not None and "." not in dotted and not _external(dotted):
                unresolved.add(dotted)
            continue
        if path in seen:
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


def _seam_roots() -> dict:
    """{flat directory: [bare name, ...]} as each path seam declares them -- `pc_engine` puts
    `PC_ENGINE_DIR` on `sys.path` and loads `PCEngine._fields` by name. Importing it mutates nothing."""
    from engine.substrate import pc_engine
    return {os.path.normpath(pc_engine.PC_ENGINE_DIR): list(pc_engine.PCEngine._fields)}


def check(module_dir: str, roots: list, flat: bool = False) -> tuple:
    """`(unreached, left_behind, unresolved)` for one module: files under `module_dir` the walk from
    `roots` does not reach, files the walk reaches under `systems/`, and (flat sets only) bare names the
    set imports and does not hold."""
    unresolved: set = set()
    reached = closure(roots, module_dir if flat else None, unresolved)
    unreached = _module_files(module_dir) - reached
    left_behind = {p for p in reached if os.path.relpath(p, ROOT).split(os.sep)[0] == "systems"}
    return unreached, left_behind, unresolved


def test_every_module_is_exactly_its_entries_reachable_closure():
    roots = _entry_roots()
    seams = _seam_roots()
    checked = {"package": [], "flat": []}
    # What the walk below cannot see on its own: an entry row aimed outside `modules/`, a directory under
    # `modules/` that no entry row names, and a loose top-level file. Each would sit outside every closure.
    stray_targets = sorted(r for r, row in composition.ROLES.items() if row.get("entry")
                           and str(row.get("target", "")).split(".")[0] != MODULES)
    assert not stray_targets, f"entry rows whose target is not under `{MODULES}/`: {stray_targets}"
    top = os.path.join(ROOT, MODULES)
    unnamed = sorted(d for d in os.listdir(top) if d != "__pycache__"
                     and os.path.isdir(os.path.join(top, d))
                     and os.path.join(top, d) not in roots)
    loose = sorted(f for f in os.listdir(top) if f.endswith(".py") and f != "__init__.py")
    assert not unnamed and not loose, (
        f"`{MODULES}/` holds directories no entry row names {unnamed} or loose files {loose}; "
        "it holds the reachable closure of the entries only")
    for module_dir, entry_modules in sorted(roots.items()):
        flat = not os.path.isfile(os.path.join(module_dir, "__init__.py"))
        rel = os.path.relpath(module_dir, ROOT)
        if flat:
            assert os.path.normpath(module_dir) in seams, (
                f"{rel} is a flat module set and no path seam this walk knows declares its names: "
                f"{sorted(seams)}")
            entry_modules = entry_modules + seams[os.path.normpath(module_dir)]
        unreached, left_behind, unresolved = check(module_dir, entry_modules, flat)
        assert not unreached, (
            f"{rel}: files no entry reaches ({entry_modules}): "
            f"{_rel(unreached)}. `modules/` holds the reachable closure only (A-25); an unreached file goes "
            "back to `systems/` or is deleted")
        assert not left_behind, (
            f"{rel}: its closure reaches files left in `systems/`: "
            f"{_rel(left_behind)}. The closure moves whole")
        assert not unresolved, (
            f"{rel}: the flat set imports {sorted(unresolved)}, which it does not hold and nothing "
            "installed provides. The closure moves whole")
        checked["flat" if flat else "package"].append(rel)
    print(f"SM-7 checked: {checked}")
    assert os.path.join(MODULES, "mass_battle") in checked["package"], (
        f"the walk checked {checked} and not `modules/mass_battle`, the package `31c` moved; the roots "
        f"are read from the composition rows -- has its entry row lost `entry:`?")
    assert os.path.join(MODULES, "combat") in checked["flat"], (
        f"the walk checked {checked} and not `modules/combat`, the flat set `31b` moved")


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
    unreached, left_behind, _ = check(str(tmp_path / "modules" / "m"), ["modules.m.entry"])
    assert _rel(unreached) == [os.path.join("modules", "m", "orphan.py")], _rel(unreached)
    assert os.path.join("systems", "s", "sim", "old.py") in _rel(left_behind), _rel(left_behind)
    # A FLAT set (no `__init__.py`): roots by bare name, a sibling found in the directory first, a bare
    # name the set does not hold reported, an unimported file unreached; stdlib names pass.
    write("modules/f/entry.py", "import os, used\n\ndef run():\n    import zz_not_in_the_set\n")
    write("modules/f/used.py", "from math import tanh\n")
    write("modules/f/orphan.py")
    unreached, left_behind, unresolved = check(str(tmp_path / "modules" / "f"), ["entry"], flat=True)
    assert _rel(unreached) == [os.path.join("modules", "f", "orphan.py")], _rel(unreached)
    assert unresolved == {"zz_not_in_the_set"} and not left_behind, (unresolved, _rel(left_behind))


if __name__ == "__main__":   # pragma: no cover
    pytest.main([__file__, "-q"])
