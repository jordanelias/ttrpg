"""THE `social_contest` MODULE ENTRY, CALLED ON A HAND-BUILT RECORD -- plan position `31a` (IN-03),
falsifier (2).

A-25: a module takes the host's typed input record and a seeded `rng`, imports the dice engine and the
record types and nothing else, and never reads `World`. This test builds a `SocialContestInput` by hand
-- no `World`, no driver, no registrar -- calls the entry and asserts the result: a `Margin` with `net`
and `ob` (v9 SC-01 step 15 typed the module -> host boundary; it was a `status: RESOLVED` dict).

IN A FRESH SUBPROCESS, because what is asserted includes WHICH repository files the import loaded,
and inside a pytest process another test's imports have loaded the whole host already.

The entry is found the way the host finds it: the prize rows' `module_entry:` names a composition role
(`references/module_contracts.yaml`), whose `target:` is the module's dotted path. Nothing here
imports the module by name -- `engine/` never imports module code
(`tests/valoria/test_engine_does_not_import_systems.py`, which imports this file too).
"""
from __future__ import annotations

from ..manifest.registry import roster_map
from engine.substrate import composition
from ._fresh_process import probe


def _entry_targets() -> list:
    """`(role, target)` for each composition row a `social_contest` prize row names in `module_entry:`
    (since `31b` another module's prize names one too; `test_combat_module.py` probes that one)."""
    roles = sorted({row["module_entry"] for row in roster_map("contest_subsystems", "prizes").values()
                    if isinstance(row, dict) and row.get("module_entry")
                    and row.get("module") == "social_contest"})
    return [(r, composition.ROLES[r]["target"]) for r in roles]


_PROBE = """
import sys, os, importlib, random
sys.path.insert(0, {root!r})
before = set(sys.modules)
mod_name, attr = {target!r}.split(":", 1)
entry = getattr(importlib.import_module(mod_name), attr)
loaded = sorted(os.path.relpath(m.__file__, {root!r}) for n, m in list(sys.modules.items())
                if n not in before and getattr(m, "__file__", None)
                and os.path.abspath(m.__file__).startswith({root!r} + os.sep))
from engine.season.queries.inputs import Margin, SocialContestInput
from engine.dice_engine.sigma_leverage import net_boost, roll_net
out = []
for lev in (0.0, 1.5):
    inp = SocialContestInput(pool=4, opposition=None, obstacle_default=2.0, obstacle_ceiling=3.0,
                             obstacle_refusal_multiple=3.0, leverage=lev)
    got = entry(inp, random.Random(7))
    again = entry(inp, random.Random(7))
    want = roll_net(4, rng=random.Random(7)) + net_boost(lev, 4)
    out.append((type(got) is Margin, dict(net=got.net, ob=got.ob), again == got, want))
print(repr((loaded, out)))
"""


def test_the_social_contest_entry_resolves_a_hand_built_record_importing_only_the_dice_engine_and_the_record():
    targets = _entry_targets()
    assert targets, "no prize row names a `module_entry:`; the module entry this test is about is gone"
    checked = 0
    for role, target in targets:
        loaded, out = probe(_PROBE, target, 300)
        module_dir = target.split(":", 1)[0].rsplit(".", 1)[0].replace(".", "/")
        allowed_files = {"engine/__init__.py", "engine/season/__init__.py",
                         "engine/season/queries/__init__.py", "engine/season/queries/inputs.py"}
        stray = [f for f in loaded
                 if f not in allowed_files
                 and not f.startswith("engine/dice_engine/")
                 and not f.startswith(module_dir + "/")
                 and f != module_dir.split("/", 1)[0] + "/__init__.py"]
        assert not stray, (
            f"{role} ({target}) loaded repository code beyond the dice engine and the record type: "
            f"{stray}. A-25: a module imports the dice engine and the record types, nothing else")
        assert any(f.startswith("engine/dice_engine/") for f in loaded), loaded
        assert "engine/season/queries/inputs.py" in loaded, loaded
        for is_margin, got, deterministic, want in out:
            assert is_margin, f"{role} returned something other than a `Margin`: {got}"
            assert got["ob"] == 2.0, got
            assert got["net"] == want, (
                f"{role}: net {got['net']} is not the tree's composition roll_net(pool) + "
                f"net_boost(lev, pool) = {want} (ED-SC-0037)")
            assert deterministic, f"{role}: the same seed gave two results"
            checked += 1
    assert checked >= 2, checked


def test_s27_4_refuses_on_the_derived_pair_strictly_above_the_multiple():
    """S27.4 at the host adapter (`seam/wrappers/sigma.py::resolve`): a derived obstacle EQUAL to the
    multiple times the pool is not refused; one strictly above it is, with the refusal's whole return.
    ⚠ SINCE v9 SC-01 STEP 14 THE PAIR IS THE ENTRY'S (the module composes the obstacle), so the call
    names a real prize and a driver registers the entry first; the ceiling is the uncapped control
    (`None`), since the shipped ceiling (2) keeps every obstacle at or under 2 x a 1D pool. A `>=` in
    the rule fails the first assertion; with the ceiling at 2 the second call is NOT refused (third)."""
    import random
    from types import SimpleNamespace
    from engine.season.data.fixtures import DEFAULT_FIXTURES
    from engine.season.harness import probes as P
    from engine.season.loop.driver import SeasonDriver
    from engine.season.seam.wrappers import sigma
    SeasonDriver(P.tiny_world(DEFAULT_FIXTURES))      # the registrar fills MODULE_ENTRIES
    fx = {"pool_default": 2, "obstacle_default": 4, "obstacle_ceiling": None,
          "obstacle_refusal_multiple": 2,
          "practice_cap": 0}       # `faculty` reads the practice addend (CP-T01-02), which reads this key
    w = SimpleNamespace(persons={"p": SimpleNamespace(capability={})}, fixtures=fx)
    at = sigma.resolve(w, ["p"], ["c"], "a standing", rng=random.Random(0))
    assert at["status"] == "RESOLVED", f"ob 4 == 2 x pool 2 was refused: {at}"
    fx["obstacle_default"] = 4.5
    assert sigma.resolve(w, ["p"], ["c"], "a standing", rng=random.Random(0)) == dict(
        status="REFUSED", why="S27.4", module="social_contest", resolver="d10_sigma", pool=2, ob=4.5)
    fx["obstacle_ceiling"] = 2
    capped = sigma.resolve(w, ["p"], ["c"], "a standing", rng=random.Random(0))
    assert capped["status"] == "RESOLVED" and capped["ob"] == 2.0, capped
