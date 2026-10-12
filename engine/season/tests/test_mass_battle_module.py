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
"""
from __future__ import annotations

import subprocess
import sys

from ..data import files
from ..manifest.registry import resolve
from engine.substrate import composition

_PRIZE = "a field"

_PROBE = """
import sys, os, importlib, random
sys.path.insert(0, {root!r})
before = set(sys.modules)
mod_name, attr = {target!r}.split(":", 1)
entry = getattr(importlib.import_module(mod_name), attr)
source = importlib.import_module(mod_name.rsplit(".", 1)[0] + ".rngsource")
from engine.season.queries.inputs import MassBattleInput

# Sides large enough that the field is fought for ticks rather than routing on contact, on an UPHILL
# territory (T9) with a fortification (so the WALLS row and its DR are inside the replayed battle) and
# morale moved off the base by the stances.
FIELD = MassBattleInput(weights=((180.0, 120.0), (240.0,)), territory="T9", fort_level=1.0,
                        stances=(-1.0, 0.5), walls_dr=None, origin=None,
                        loyalties=(1.5, -0.5), loyalty_gain=0.4)
# A RIVER_CROSSING field (MB-05r): a march from T9 onto T3's open ground crosses the Valoris.
OTHER = MassBattleInput(weights=((90.0,), (60.0, 30.0)), territory="T3", fort_level=0.0,
                        stances=(0.0, 0.0), walls_dr=1, origin="T9",
                        loyalties=(0.0, 0.0), loyalty_gain=0)
stdlib_before = random.getstate()
out = []
for seed in (1, 2, 3, 4, 5, 6):
    got = entry(FIELD, random.Random(seed))
    between = entry(OTHER, random.Random(seed + 100))
    again = entry(FIELD, random.Random(seed))
    out.append((seed, got, again == got, source.get() is random))
stdlib_untouched = random.getstate() == stdlib_before
loaded = sorted(os.path.relpath(m.__file__, {root!r}) for n, m in list(sys.modules.items())
                if n not in before and getattr(m, "__file__", None)
                and os.path.abspath(m.__file__).startswith({root!r} + os.sep))
print(repr((loaded, out, stdlib_untouched)))
"""


def _entry_target() -> tuple:
    role = (resolve("contest", _PRIZE) or {}).get("module_entry")
    assert role, f"the prize row {_PRIZE!r} names no `module_entry:`; the entry this test is about is gone"
    return role, composition.ROLES[role]["target"]


def _probe(target: str):
    root = str(files.REPO_ROOT)
    proc = subprocess.run([sys.executable, "-c", _PROBE.format(root=root, target=target)],
                          capture_output=True, text=True, timeout=600, cwd=root)
    assert proc.returncode == 0, proc.stderr[-3000:]
    return eval(proc.stdout.strip().splitlines()[-1])     # our own probe's repr


def test_one_march_resolved_twice_in_one_process_gives_one_result_and_loads_nothing_of_the_host():
    role, target = _entry_target()
    loaded, out, stdlib_untouched = _probe(target)
    module_dir = target.split(":", 1)[0].rsplit(".", 1)[0].replace(".", "/")
    allowed = {"engine/__init__.py", "engine/season/__init__.py", "engine/season/queries/__init__.py",
               "engine/season/queries/inputs.py", module_dir.split("/", 1)[0] + "/__init__.py"}
    stray = [f for f in loaded if f not in allowed and not f.startswith(module_dir + "/")]
    assert not stray, (
        f"{role} ({target}) loaded repository code beyond the module it runs and the record type: {stray}. "
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
