"""THE `combat` MODULE ENTRY, CALLED ON A HAND-BUILT RECORD -- plan position `31b` (IN-04), as
`test_social_contest_module.py` is `31a`'s.

A-25: a module takes the host's typed input record and a seeded `rng`, imports what it runs and the record
type and nothing else of the host, and never reads `World`. This test builds a `PersonalCombatInput` by hand
-- no `World`, no driver, no registrar -- calls the entry and asserts the result dict against the engine
called directly with the same parties and seed (the independent oracle: `wrapper.fight` on two
`Combatant`s, which is what the seam did before the split).

IN A FRESH SUBPROCESS, because what is asserted includes WHICH repository files the import loaded, and
inside a pytest process another test's imports have loaded the whole host already.

The entry is found the way the host finds it: the prize row `the body` names a composition role in
`module_entry:` (`references/module_contracts.yaml`), whose `target:` is the module's dotted path. Nothing
here imports the module by name -- `engine/` never imports module code.

FALSIFIER (2) of `31b`, at the module's grain: the same record and the same seed, called twice in ONE
process, give one result (module-level state surviving between calls makes the second differ).
"""
from __future__ import annotations

from ._fresh_process import entry_target, probe

_PRIZE = "the body"


_PROBE = """
import sys, os, importlib, random
sys.path.insert(0, {root!r})
before = set(sys.modules)
mod_name, attr = {target!r}.split(":", 1)
entry = getattr(importlib.import_module(mod_name), attr)
from engine.season.queries.inputs import PersonalCombatInput
qs = ("felled", "wounds", "max_wounds", "health_remaining", "health_full")
out = []
for seed, ends in ((7, (4, 4)), (11, (4, 1)), (3, (2, 4))):
    inp = PersonalCombatInput(claimants=("p_a", "p_b"), ends=ends, wound_quantities=qs)
    got = entry(inp, random.Random(seed))
    again = entry(inp, random.Random(seed))
    out.append((seed, ends, got["status"], got["result"], got["ends"], got["wound_state"],
                len(got["trace"]), again == got))
loaded = sorted(os.path.relpath(m.__file__, {root!r}) for n, m in list(sys.modules.items())
                if n not in before and getattr(m, "__file__", None)
                and os.path.abspath(m.__file__).startswith({root!r} + os.sep))
# THE ORACLE: the engine called directly, the way the seam called it before `31b`.
import wrapper, combatant
oracle = []
for seed, ends, *_ in out:
    A, B = combatant.Combatant("p_a", end=ends[0]), combatant.Combatant("p_b", end=ends[1])
    r = wrapper.fight(A, B, rng=random.Random(seed))
    oracle.append((r, {{c.label: {{q: getattr(c.wt, q) for q in qs}} for c in (A, B)}}))
print(repr((loaded, out, oracle)))
"""


def test_the_combat_entry_fights_a_hand_built_record_as_the_engine_does_and_loads_nothing_of_the_host():
    role, target = entry_target(_PRIZE)
    loaded, out, oracle = probe(_PROBE, target, 300)
    module_dir = target.split(":", 1)[0].rsplit(".", 1)[0].replace(".", "/")
    allowed = {"engine/__init__.py", "engine/season/__init__.py", "engine/season/queries/__init__.py",
               "engine/season/queries/inputs.py", "engine/substrate/__init__.py",
               "engine/substrate/pc_engine.py", module_dir.split("/", 1)[0] + "/__init__.py"}
    stray = [f for f in loaded
             if f not in allowed and not f.startswith("engine/dice_engine/")
             and not f.startswith(module_dir + "/")]
    assert not stray, (
        f"{role} ({target}) loaded repository code beyond the engine it runs, the path seam and the record "
        f"type: {stray}. A-25: a module imports what it runs and the record types, nothing else of the host")
    assert "engine/season/queries/inputs.py" in loaded and f"{module_dir}/wrapper.py" in loaded, loaded
    checked = 0
    for (seed, ends, status, result, got_ends, wound_state, n_trace, deterministic), (r, wt) in zip(out, oracle):
        assert status == "RESOLVED", (seed, status)
        assert deterministic, f"{role}: seed {seed} gave two results in one process"
        assert result == r, f"{role}: seed {seed} result {result} != the engine's own {r}"
        assert got_ends == {"p_a": ends[0], "p_b": ends[1]}, got_ends
        assert wound_state == wt, f"{role}: seed {seed} lifted {wound_state}, the trackers read {wt}"
        assert n_trace > 0, f"{role}: seed {seed} recorded no trace -- `_TRACE` was not captured"
        checked += 1
    assert checked == 3, checked
    assert len({(o[3], repr(o[5])) for o in out}) > 1, (
        "every hand-built fight read the same; the comparison cannot tell the parties apart")
