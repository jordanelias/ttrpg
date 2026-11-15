"""`engine/season/boot/` imports no instrument -- executed (`04` §A.2's `boot/` row, PART D row 53).

THE CLAIM. The World a game runs is constructed by `boot/`, and `boot/` imports nothing under
`harness/`: the instruments import the builder, never the reverse, so "new game" is game code the
port can port. The boundary is a directory, so it is checkable by path.

  * `test_importing_boot_pulls_in_no_instrument` -- the claim itself. A fresh interpreter imports
    both `boot/` modules and reads `sys.modules`; only a fresh process shows that nothing else
    loaded the instrument first. The floor on the loaded `engine.season` modules means an import
    that loaded nothing cannot pass (`CLAUDE.md` §0.1 pt 2).
  * `test_no_harness_import_line_in_boot` -- the same boundary read from the source by `ast`: no
    `Import`/`ImportFrom` in a `boot/` file names a `harness` module. FALSIFIER of both: a
    `from ..harness import probes` planted in a `boot/` file turns the first one red (its import
    loads `engine.season.harness`) and the second one red by name.
"""
import ast
import subprocess
import sys

from engine.season.data import files

_PROBE = (
    "import sys\n"
    "import engine.season.boot.realm, engine.season.boot.chooser\n"
    "loaded = sorted(m for m in sys.modules if m.startswith('engine.season'))\n"
    "print(len(loaded))\n"
    "print('|'.join(m for m in loaded if m.startswith('engine.season.harness')))\n"
)


def test_importing_boot_pulls_in_no_instrument():
    proc = subprocess.run([sys.executable, "-c", _PROBE], cwd=str(files.REPO_ROOT),
                          capture_output=True, text=True)
    assert proc.returncode == 0, f"the probe did not run:\n{proc.stderr}"
    count, leaked = proc.stdout.splitlines()[0], proc.stdout.splitlines()[1]
    assert int(count) > 20, f"only {count} engine.season modules loaded -- the import loaded nothing"
    assert not leaked, "importing boot/ loaded the instrument: " + leaked.replace("|", ", ")


def _names(node):
    if isinstance(node, ast.Import):
        return [a.name for a in node.names]
    # `from ..harness import x` has module "harness" at level 2; `from .. import harness` has the name in `names`.
    return [node.module or ""] + [a.name for a in node.names]


def test_no_harness_import_line_in_boot():
    checked = 0
    for path in sorted(files.BOOT_DIR.rglob("*.py")):
        checked += 1
        for node in ast.walk(ast.parse(path.read_text(encoding="utf-8"))):
            if isinstance(node, (ast.Import, ast.ImportFrom)):
                for name in _names(node):
                    assert "harness" not in name.split("."), f"{path.name}:{node.lineno} imports {name}"
    assert checked >= 3, f"only {checked} files under boot/ -- the walk is broken"
