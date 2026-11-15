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
    "engine.season.boot.realm.build_realm(0)\n"   # a harness import deferred into a function runs here, not at import
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


class _Logged(dict):
    """A dict that appends `(label, key)` to a shared log on each item assignment -- how the test sees the ORDER of writes across stores."""
    def __init__(self, label, log):
        super().__init__()
        self._label, self._log = label, log

    def __setitem__(self, key, value):
        self._log.append((self._label, key))
        super().__setitem__(key, value)


def test_place_person_writes_the_four_records():
    """ONE call writes the `Person`, its person `Rung`, the `contain` Tenure `t_<pid>_in` and the `reside` Tenure `t_<pid>_home`, in that order -- and `home` defaults to `rung`."""
    from engine.season.boot.realm import place_person
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    from engine.season.queries.world_q import RESIDE_KIND
    from engine.season.state.carriers import Person, Rung
    from engine.season.state.world import World

    log = []
    w = World(0, DEFAULT_FIXTURES)
    w.persons, w.rungs = _Logged("person", log), _Logged("rung", log)
    w.rungs["hearth_a"] = Rung("hearth_a", "hearth")
    w.rungs["hearth_b"] = Rung("hearth_b", "hearth")
    log.clear()
    real_add = w.add_tenure
    w.add_tenure = lambda t: (log.append(("tenure", t.id)), real_add(t))[1]

    p = place_person(w, "p_x", "Xan", "hearth_a")
    assert isinstance(p, Person) and p is w.persons["p_x"] and (p.name, p.weight) == ("Xan", 1)
    assert w.rungs["p_x"].kind == "person"
    assert log == [("person", "p_x"), ("rung", "p_x"), ("tenure", "t_p_x_in"), ("tenure", "t_p_x_home")]
    tenures = {t.id: t for t in w.persons["p_x"].tenures}
    assert list(tenures) == ["t_p_x_in", "t_p_x_home"]
    assert (tenures["t_p_x_in"].kind, tenures["t_p_x_in"].object) == ("contain", "hearth_a")
    assert (tenures["t_p_x_home"].kind, tenures["t_p_x_home"].object) == (RESIDE_KIND, "hearth_a")
    assert RESIDE_KIND == "reside"

    # `home` set apart from `rung`, `weight` and a `Person` field pass through.
    q = place_person(w, "p_y", "Yan", "hearth_a", home="hearth_b", weight=3, pursuits={"a": 1})
    assert (q.weight, q.pursuits) == (3, {"a": 1})
    got = {t.id: t.object for t in q.tenures}
    assert got == {"t_p_y_in": "hearth_a", "t_p_y_home": "hearth_b"}
