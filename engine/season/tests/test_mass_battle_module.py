"""THE `mass_battle` MODULE ENTRY, CALLED ON A HAND-BUILT RECORD -- plan position `31c` (IN-05), as
`test_combat_module.py` is `31b`'s and `test_social_contest_module.py` is `31a`'s.

A-25: a module takes the host's typed input record and a seeded `rng`, imports what it runs and the record
type and nothing else of the host, and never reads `World`. This test builds a `MassBattleInput` by hand --
no `World`, no driver, no registrar -- and calls the entry the way the host finds it: the prize row
`a field` names a composition role in `module_entry:` (`references/module_contracts.yaml`), whose `target:`
is the module's dotted path. Nothing here imports the module by name -- `engine/` never imports module code.

IN A FRESH SUBPROCESS, because what is asserted includes WHICH repository files the import loaded, and
inside a pytest process another test's imports have loaded the whole host already.

FALSIFIER (2) of `31c` -- nothing observed it before this file. ONE constructed `march` record resolved
twice in ONE process with one seed gives one result, WITH A DIFFERENT FIELD FOUGHT BETWEEN THE TWO CALLS:
module-level state surviving between calls (the engine's draw source, the geography cache, the trace
buffer -- the three `31c` shed) makes the second differ. Three more observations close the gaps that
determinism alone leaves open: the stdlib `random` stream is untouched by every call (the battle draws
only from the seeded `rng` its call scoped), no draw source is still scoped after a call returns, and the
seeds do not all give one result (else the comparison could not tell two calls apart).

AND THE MODULE OPENS NO FILE: `builtins.open`, `io.open` and `os.open` are watched from before the import
to the last call, and the set they saw must be empty -- the geography arrives on the record
(`MassBattleInput.geography`), read once per process by the host (`data/geography.py`); until it did,
`terrain.py` parsed the file on every fought field. The record's geography must also come back unwritten:
the host shares one mapping across every field.
"""
from __future__ import annotations

from ..data import files
from ._fresh_process import entry_target, probe
from engine.dice_engine import draw

_PRIZE = "a field"

_PROBE = """
import sys, os, io, builtins, copy, importlib, random, yaml
sys.path.insert(0, {root!r})
# The geography the host hands the module on the record, read HERE, before anything is watched: the
# module takes it on `MassBattleInput.geography` and opens no file of its own.
with open(__GEOGRAPHY_YAML__, encoding="utf-8") as f:
    GEO = yaml.safe_load(f)
GEO_BEFORE = copy.deepcopy(GEO)
opened = []
def _watching(real):
    def watched(file, *a, **k):
        opened.append(str(file))
        return real(file, *a, **k)
    return watched
builtins.open, io.open, os.open = _watching(builtins.open), _watching(io.open), _watching(os.open)
before = set(sys.modules)
mod_name, attr = {target!r}.split(":", 1)
entry = getattr(importlib.import_module(mod_name), attr)
source = importlib.import_module(mod_name.rsplit(".", 1)[0] + ".rngsource")
from engine.season.queries.inputs import MassBattleInput
from engine.dice_engine import draw

# Sides large enough that the field is fought for ticks rather than routing on contact, on an UPHILL
# territory (T9) with a fortification (so the WALLS row and its DR are inside the replayed battle) and
# morale moved off the base by the stances.
FIELD = MassBattleInput(weights=((180.0, 120.0), (240.0,)), territory="T9", fort_level=1.0,
                        stances=(-1.0, 0.5), walls_dr=None, origin=None,
                        loyalties=(1.5, -0.5), loyalty_gain=0.4, geography=GEO)
# A RIVER_CROSSING field (MB-05r): a march from T9 onto T3's open ground crosses the Valoris.
OTHER = MassBattleInput(weights=((90.0,), (60.0, 30.0)), territory="T3", fort_level=0.0,
                        stances=(0.0, 0.0), walls_dr=1, origin="T9",
                        loyalties=(0.0, 0.0), loyalty_gain=0, geography=GEO)
stdlib_before = random.getstate()
out = []
for seed in (1, 2, 3, 4, 5, 6):
    got = entry(FIELD, draw.seeded(draw.H2("test_mass_battle_module", seed)))
    between = entry(OTHER, draw.seeded(draw.H2("test_mass_battle_module", seed + 100)))
    again = entry(FIELD, draw.seeded(draw.H2("test_mass_battle_module", seed)))
    out.append((seed, got, again == got, source.get() is random))
stdlib_untouched = random.getstate() == stdlib_before
loaded = sorted(os.path.relpath(m.__file__, {root!r}) for n, m in list(sys.modules.items())
                if n not in before and getattr(m, "__file__", None)
                and os.path.abspath(m.__file__).startswith({root!r} + os.sep))
print(repr((loaded, out, stdlib_untouched, opened, GEO == GEO_BEFORE)))
"""


def test_one_march_resolved_twice_in_one_process_gives_one_result_and_loads_nothing_of_the_host():
    role, target = entry_target(_PRIZE)
    loaded, out, stdlib_untouched, opened, geo_untouched = probe(
        _PROBE.replace("__GEOGRAPHY_YAML__", repr(str(files.GEOGRAPHY_YAML))), target, 600)
    module_dir = target.split(":", 1)[0].rsplit(".", 1)[0].replace(".", "/")
    allowed = {"engine/__init__.py", "engine/season/__init__.py", "engine/season/queries/__init__.py",
               "engine/season/queries/inputs.py", module_dir.split("/", 1)[0] + "/__init__.py"}
    # The dice engine is the one leaf the module imports besides the record type (B05.03, U5b §1 row 1): the
    # sampler and the ladder it draws from and grades on, as the other two registered modules already do.
    stray = [f for f in loaded if f not in allowed and not f.startswith("engine/dice_engine/")
             and not f.startswith(module_dir + "/")]
    assert not stray, (
        f"{role} ({target}) loaded repository code beyond the module it runs, the dice engine and the record type: {stray}. "
        "A-25: a module imports what it runs and the record types, nothing else of the host")
    assert f"{module_dir}/massbattle.py" in loaded and f"{module_dir}/orchestration.py" in loaded, loaded
    checked = 0
    for seed, got, deterministic, unscoped in out:
        assert set(got) == {"attacker_wins", "degree", "attacker_size_pct", "defender_size_pct"}, got
        assert deterministic, f"{role}: seed {seed} gave two results in one process with a field between"
        assert unscoped, f"{role}: seed {seed} left a draw source scoped after the call returned"
        checked += 1
    assert checked == 6, checked
    assert stdlib_untouched, f"{role}: a call drew from the stdlib `random` stream, not its seeded rng"
    assert len({repr(got) for _, got, _, _ in out}) > 1, (
        "every seed fought the same field to the same result; the twice-in-one-process comparison cannot "
        "tell two calls apart")
    assert not opened, (
        f"{role} ({target}) opened {opened} while importing or fighting: the geography (and any other "
        "data) arrives on the record (`MassBattleInput.geography`, the host's one read), never by path")
    assert geo_untouched, f"{role} wrote into the record's geography, a mapping the host shares across fields"


def _fought(entry, seeds, rng_for):
    """Fight the two hand-built fields of the probe above, in this process, once per seed with `rng_for(seed)`."""
    import yaml
    from engine.season.queries.inputs import MassBattleInput
    with open(files.GEOGRAPHY_YAML, encoding="utf-8") as f:
        geo = yaml.safe_load(f)
    field = MassBattleInput(weights=((180.0, 120.0), (240.0,)), territory="T9", fort_level=1.0,
                            stances=(-1.0, 0.5), walls_dr=None, origin=None,
                            loyalties=(1.5, -0.5), loyalty_gain=0.4, geography=geo)
    other = MassBattleInput(weights=((90.0,), (60.0, 30.0)), territory="T3", fort_level=0.0,
                            stances=(0.0, 0.0), walls_dr=1, origin="T9",
                            loyalties=(0.0, 0.0), loyalty_gain=0, geography=geo)
    return [entry(inp, rng_for(seed)) for seed in seeds for inp in (field, other)]


def _entry():
    import importlib
    _role, target = entry_target(_PRIZE)
    mod_name, attr = target.split(":", 1)
    return getattr(importlib.import_module(mod_name), attr)


def test_no_d10_face_in_mass_battle():
    """DOE §1 gate (1), for the field: a graded act draws no d10 face. Two arms, each able to observe the failure it
    excludes: (a) the source of `modules/mass_battle` holds no d10-face draw (a `randint` over 1..10); (b) whole fields
    fought with a generator whose every d10-face `randint` over 1..10 RAISES come back, so the roll the field makes is the one
    sampler's `gauss` draw (a roll that still dealt faces would raise)."""
    import random
    import re
    from pathlib import Path

    root = Path(files.REPO_ROOT)
    scanned = 0
    for path in (root / "modules" / "mass_battle").rglob("*.py"):
        scanned += 1
        assert not re.search(r"(randint|die)\(\s*1\s*,\s*10\s*\)", path.read_text(encoding="utf-8")), path
    assert scanned >= 20, scanned

    class _NoFaces(draw.Draw):
        def __init__(self, seed):
            super().__init__(draw.H2("test_mass_battle_module", seed))

        def die(self, lo, hi):
            if (lo, hi) == (1, 10):
                raise AssertionError("a d10 face was drawn on the field")
            return super().die(lo, hi)

    fought = _fought(_entry(), range(1, 5), _NoFaces)
    assert len(fought) == 8 and all("degree" in got for got in fought), fought
    assert len({repr(got) for got in fought}) > 1, "every field gave one result; the arm cannot tell fields apart"


def test_one_ladder_for_the_field(monkeypatch):
    """DOE §1 gate (2): the field grades on the owner's ladder and has none of its own. Two arms: (a) the module holds
    no ladder of its own (`compute_degree` and its epsilon are gone, nothing under `modules/mass_battle` spells the
    `net - ob` bands); (b) fought fields grade THROUGH `dice_engine.degree_from_net`, the one function a call to it
    is counted on, and every grade the field acted on is the owner's grade for that (net, ob)."""
    import importlib
    import re
    from pathlib import Path
    import random
    from engine.dice_engine import dice_engine

    _role, target = entry_target(_PRIZE)
    pkg = target.split(":", 1)[0].rsplit(".", 1)[0]
    entry = _entry()
    resolution = importlib.import_module(pkg + ".resolution")
    assert not hasattr(resolution, "compute_degree"), "the field still has a ladder of its own"
    assert not hasattr(resolution, "_DEGREE_EPS"), "the field still carries its own band epsilon"
    root = Path(files.REPO_ROOT)
    for path in (root / "modules" / "mass_battle").rglob("*.py"):
        assert not re.search(r"return\s+[\'\"](?:Overwhelming|Partial)[\'\"]", path.read_text(encoding="utf-8")), path

    seen = []
    real = dice_engine.degree_from_net

    def counting(net, ob, *a, **k):
        got = real(net, ob, *a, **k)
        seen.append((net, ob, got))
        return got

    monkeypatch.setattr(dice_engine, "degree_from_net", counting)
    _fought(entry, range(1, 4), lambda s: draw.seeded(draw.H2("test_mass_battle_module", s)))
    assert len(seen) >= 50, f"only {len(seen)} grade(s) went through the owner: the field grades elsewhere"
    assert all(got == real(net, ob) for net, ob, got in seen)
