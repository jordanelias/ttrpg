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
from engine.dice_engine.sigma_leverage import net_boost, roll_net_continuous
out = []
for lev in (0.0, 1.5):
    inp = SocialContestInput(pool=4, opposition=None, obstacle_default=2.0, obstacle_ceiling=3.0,
                             obstacle_refusal_multiple=3.0, leverage=lev)
    got = entry(inp, random.Random(7))
    again = entry(inp, random.Random(7))
    want = roll_net_continuous(4, rng=random.Random(7)) + net_boost(lev, 4)
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
                f"{role}: net {got['net']} is not the tree's composition roll_net_continuous(pool) + "
                f"net_boost(lev, pool) = {want} (ED-SC-0037, B05.02)")
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
    refused = sigma.resolve(w, ["p"], ["c"], "a standing", rng=random.Random(0))
    fed_by = refused.pop("fed_by")           # B04.08: the rows that fed the roll ride the record, a refusal's too (D-U1-06)
    assert tuple((f[0], f[1], f[4], f[5]) for f in fed_by) == (("social_roll", "dice", 2, 2), ("social_roll", "opposes", None, 0.0))
    assert refused == dict(
        status="REFUSED", why="S27.4", module="social_contest", resolver="d10_sigma", pool=2, ob=4.5,
        ob_terms={"stand_in": 4.5})          # B11 lane A: the obstacle's terms ride the record, a refusal's too
    fx["obstacle_ceiling"] = 2
    capped = sigma.resolve(w, ["p"], ["c"], "a standing", rng=random.Random(0))
    assert capped["status"] == "RESOLVED" and capped["ob"] == 2.0, capped


def test_the_obstacle_is_reached_by_its_own_composition_row(monkeypatch):
    """`seam/wrappers/sigma.py::_composed_obstacle` reaches the obstacle by the `social_contest.obstacle` row
    and by no other: with that role's resolved callable replaced (and restored) by a stub returning 7.0, the
    host returns 7.0 for any record. A missing row is `composition.require`'s refusal, not a reflective import."""
    from engine.season.queries.inputs import SocialContestInput
    from engine.season.seam.wrappers import sigma
    role = "social_contest.obstacle"
    monkeypatch.setitem(composition._CACHE, role, lambda inp: 7.0)
    for pool, opposition in ((1, None), (4, 3.0)):
        inp = SocialContestInput(pool=pool, opposition=opposition, obstacle_default=2.0, obstacle_ceiling=3.0,
                                 obstacle_refusal_multiple=3.0, leverage=0.0)
        assert sigma._composed_obstacle(inp) == 7.0


def test_no_d10_face_in_social_contest():
    """DOE §1 gate (1), for `modules/social_contest` and the season loop: a graded act outside combat draws no d10 face.
    Two arms, each able to observe the failure it excludes: (a) the source of the module and of `engine/season/`
    (tests excepted) holds no d10-face draw (a `randint` over 1..10); (b) the entry run with a generator whose every integer draw RAISES
    still returns the sampler's margin -- only `gauss` is drawn, and the draw is the one sampler's."""
    import random
    import re
    from pathlib import Path
    from engine.dice_engine.sigma_leverage import net_boost, roll_net_continuous
    from engine.season.data import files
    from engine.season.queries.inputs import SocialContestInput
    from .test_sc01_obstacle_ceiling import _module

    root = Path(files.REPO_ROOT)
    scanned = 0
    for base in (root / "modules" / "social_contest", root / "engine" / "season"):
        for path in base.rglob("*.py"):
            if "tests" in path.relative_to(root).parts:
                continue
            scanned += 1
            assert not re.search(r"randint\(\s*1\s*,\s*10\s*\)", path.read_text(encoding="utf-8")), path
    assert scanned >= 20, scanned

    class _NoFaces(random.Random):
        def randint(self, a, b):
            raise AssertionError("a d10 face was drawn in the social roll")
        randrange = randint

    for pool, lev in ((4, 0.0), (8, 1.5), (0.5, 0.0)):
        inp = SocialContestInput(pool=pool, opposition=None, obstacle_default=2.0, obstacle_ceiling=3.0,
                                 obstacle_refusal_multiple=3.0, leverage=lev)
        got = _module().roll(inp, _NoFaces(7))
        assert got.net == roll_net_continuous(pool, rng=random.Random(7)) + net_boost(lev, pool), (pool, lev, got)
