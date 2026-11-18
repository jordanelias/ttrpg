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
    inp = SocialContestInput(pool=4, opposition=None, difficulty=0.0, pool_default=4, pool_add=0, opposition_rate=0.5, obstacle_ceiling=3.0,
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
    from engine.season.data.rosters import roster
    from engine.season.harness import probes as P
    from engine.season.loop.driver import SeasonDriver
    from engine.season.seam.wrappers import sigma
    SeasonDriver(P.tiny_world(DEFAULT_FIXTURES))      # the registrar fills MODULE_ENTRIES
    # B05.14: the act's obstacle is the level's size plus `opposed_ob(pool_default)` (1.0 here: nobody is opposite): `tell` is `routine`,
    # sized 3 here, so the obstacle is 4 == 2 x the pool of 2 (`pool_default` 2: no attribute, no rank), and sized 3.5 it is over it.
    # B05.99 rewrite: the fixtures are the shipped ones swept (the host reads keys B05.21, B05.53, B05.60 and B05.62 added: a
    # hand-written dict of the old keys raised before the roll), and the hand-built person carries the body the `wounds` source reads
    sized = lambda routine: (DEFAULT_FIXTURES.sweep("pool_default", 2).sweep("obstacle_ceiling", None)
                             .sweep("ceiling_per_pool", False)  # the fixed arm, as the hand-written dict (no such key) read
                             .sweep("obstacle_refusal_multiple", 2)
                             .sweep("difficulty_ob", dict(zip(roster("difficulty_levels", ordered=True), (0, routine, 2, 3))))
                             .sweep("opposition_rate", 0.5)
                             .sweep("practice_cap", 0)          # `faculty` reads the practice addend (CP-T01-02), which reads this key
                             .sweep("pool_add", 0).sweep("pool_floor", 0))   # and (B05.09) `pool_of`'s two operands, at control
    person = SimpleNamespace(id="p", capability={}, attributes={}, traits=(), body=1000, body_ceiling=1000)
    w = SimpleNamespace(persons={"p": person}, fixtures=sized(3.0))
    at = sigma.resolve(w, ["p"], ["c"], "a standing", verb="tell", rng=random.Random(0))
    assert at["status"] == "RESOLVED" and at["ob"] == 4.0, f"ob 4 == 2 x pool 2 was refused: {at}"
    w.fixtures = sized(3.5)
    refused = sigma.resolve(w, ["p"], ["c"], "a standing", verb="tell", rng=random.Random(0))
    fed_by = refused.pop("fed_by")           # B04.08: the rows that fed the roll ride the record, a refusal's too (D-U1-06)
    assert tuple((f[0], f[1], f[4], f[5]) for f in fed_by) == (("social_roll", "dice", 2, 2), ("social_roll", "opposes", None, 0.0))
    levels = refused.pop("levels")           # B05.17: each advantage source's levels ride the record too, all zero here
    assert all(n_for == n_against == 0 for _src, n_for, n_against in levels) and len(levels) >= 2, levels
    assert refused == dict(
        status="REFUSED", why="S27.4", module="social_contest", resolver="d_sigma", pool=2, ob=4.5,
        # B05.14: the obstacle's terms ride the record, a refusal's too; B05.15/B05.17 add the two standing members at 0.0
        terms=(("even", 0.0), ("difficulty", 3.5), ("opposition", 1.0), ("reception", 0.0), ("capability", 0.0)))
    w.fixtures = w.fixtures.sweep("obstacle_ceiling", 2)
    capped = sigma.resolve(w, ["p"], ["c"], "a standing", verb="tell", rng=random.Random(0))
    assert capped["status"] == "RESOLVED" and capped["ob"] == 2.0, capped


def test_the_obstacle_is_reached_by_its_own_composition_row(monkeypatch):
    """`seam/wrappers/sigma.py::_composed_obstacle` reaches the obstacle by the `social_contest.obstacle` row
    and by no other: with that role's resolved callable replaced (and restored) by a stub returning 7.0, the
    host returns 7.0 for any record. A missing row is `composition.require`'s refusal, not a reflective import."""
    from engine.season.queries.inputs import SocialContestInput
    from engine.season.seam.wrappers import sigma
    role = "social_contest.obstacle"
    monkeypatch.setitem(composition._CACHE, role, lambda inp: (7.0, ()))
    for pool, opposition in ((1, None), (4, 3.0)):
        inp = SocialContestInput(pool=pool, opposition=opposition, difficulty=0.0, pool_default=4, pool_add=0, opposition_rate=0.5, obstacle_ceiling=3.0,
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
        inp = SocialContestInput(pool=pool, opposition=None, difficulty=0.0, pool_default=4, pool_add=0, opposition_rate=0.5, obstacle_ceiling=3.0,
                                 obstacle_refusal_multiple=3.0, leverage=lev)
        got = _module().roll(inp, _NoFaces(7))
        assert got.net == roll_net_continuous(pool, rng=random.Random(7)) + net_boost(lev, pool), (pool, lev, got)


# ---------------------------------------------------------------------------------------------------------------------
# B05.56 -- WHERE NOBODY OPPOSES, THE UNTRAINED SCORE DOES (`16_PESSIMIST_DICE_task_difficulty_and_throughput`, (a)-(c), gates 1, 2, 4).
# `roll.py::obstacle` (B05.14) reads `opposition=None` as `opposed_ob(pool_default, opposition_rate)`; these four read that term from the
# composed record. The calibrated sizes are READ from `DEFAULT_FIXTURES` (never copied here); the control arm is pinned, as `test_obstacle_form.py`
# pins its own. The falsifier of all four: the stand-in replaced by `0.0` (a row with no person opposite then composes no opposition at all).
# ---------------------------------------------------------------------------------------------------------------------

def _unopposed(**kw):
    """A hand-built record with NO person opposite (`opposition=None`), the ceiling off (the uncapped control, so no bound hides a term)."""
    from engine.season.queries.inputs import SocialContestInput
    base = dict(pool=5, opposition=None, difficulty=0.0, pool_default=2, pool_add=0, opposition_rate=0.5, obstacle_ceiling=None,
                obstacle_refusal_multiple=3.0, leverage=0.0, ceiling_form="hard")
    base.update(kw)
    return SocialContestInput(**base)


def test_unopposed_row_term_list_has_an_opposition_entry():
    """PES-DICE (a): a rolled act with nobody opposite lists an `opposition` term equal to `opposed_ob(pool_default, opposition_rate)`."""
    from engine.dice_engine.sigma_leverage import opposed_ob
    from .test_sc01_obstacle_ceiling import _module
    from ..data.fixtures import DEFAULT_FIXTURES as FX
    checked = 0
    for pool_default, rate in ((2, 0.5), (3, 0.5), (FX.get("pool_default"), FX.get("opposition_rate")), (0, FX.get("opposition_rate"))):
        _, terms = _module().obstacle(_unopposed(pool_default=pool_default, opposition_rate=rate))
        named = [value for name, value in terms if name == "opposition"]
        assert len(named) == 1, terms
        assert named[0] == opposed_ob(pool_default, rate), (pool_default, rate, terms)
        checked += 1
    assert checked == 4
    assert dict(_module().obstacle(_unopposed(pool_default=2, opposition_rate=0.5))[1])["opposition"] > 0.0   # not vacuously 0 (it fails on a stand-in of 0)


def test_four_levels_compose_four_strictly_increasing_obstacles_on_an_unopposed_row():
    """The four levels of ONE unopposed row (a `research` on a site) at the shipped sizes compose four strictly increasing obstacles; no figure
    is asserted. TWO ARMS, because at the shipped `pool_add` the even line alone (2.4) keeps every level over the `OB_MIN` floor and the stand-in
    could not be seen to matter: (shipped) every number read off `DEFAULT_FIXTURES`; (floor-visible) the same ladder and rate with `pool_add` 0,
    where without the stand-in the first two levels both lift to the floor and compose ONE obstacle -- the failure the source names."""
    from engine.dice_engine.sigma_leverage import OB_MIN
    from engine.season.data.fixtures import DEFAULT_FIXTURES as FX
    from engine.season.data.rosters import roster
    from .test_sc01_obstacle_ceiling import _module
    levels = tuple(roster("difficulty_levels", ordered=True))
    sizes = FX.get("difficulty_ob")
    assert len(levels) == 4 and all(level in sizes for level in levels), (levels, sizes)
    for arm, pool_add in (("shipped", FX.get("pool_add")), ("floor-visible", 0)):
        obs = []
        for level in levels:
            ob, terms = _module().obstacle(_unopposed(pool=FX.get("pool_floor"), pool_add=pool_add, difficulty=float(sizes[level]),
                                                      pool_default=FX.get("pool_default"), opposition_rate=FX.get("opposition_rate")))
            assert "opposition" in dict(terms), (arm, level, terms)
            obs.append(ob)
        assert len(obs) == 4 and all(a < b for a, b in zip(obs, obs[1:])), (arm, dict(zip(levels, obs)))     # strictly increasing: three adjacent pairs
        assert obs[0] >= OB_MIN


def test_routine_plus_stand_in_reproduces_the_control_obstacle():
    """At the control arm (`difficulty_ob` 0/1/2/3, `pool_add` 0, `opposition_rate` 0.5, `pool_default` 2, the `hard` form) `routine` plus the stand-in
    composes 2.0, the obstacle an inquiry carried before the ladder existed (OBS §4 step 1a)."""
    from engine.season.data.fixtures import DIFFICULTY_OB_CONTROL
    from .test_sc01_obstacle_ceiling import _module
    assert tuple(DIFFICULTY_OB_CONTROL.values()) == (0, 1, 2, 3), DIFFICULTY_OB_CONTROL
    ob, terms = _module().obstacle(_unopposed(pool=2, pool_add=0, pool_default=2, opposition_rate=0.5, ceiling_form="hard",
                                              difficulty=float(DIFFICULTY_OB_CONTROL["routine"])))
    assert ob == 2.0, (ob, terms)
    assert terms == (("even", 0.0), ("difficulty", 1.0), ("opposition", 1.0)), terms


def test_the_floor_pool_can_succeed_on_a_plain_task():
    """Gate 4: at the shipped fixtures the pool at its floor (`pool_floor` dice) meets a `plain` unopposed task at an obstacle that INCLUDES the stand-in
    (even line + `opposed_ob(pool_default)`), and the closed form's Success-or-better share there is above zero (`band_odds` bands: F, P, S, O)."""
    from engine.dice_engine.sigma_leverage import band_odds, even_line, opposed_ob
    from engine.season.data.fixtures import DEFAULT_FIXTURES as FX
    from .test_sc01_obstacle_ceiling import _module
    pool = float(FX.get("pool_floor"))
    ob, terms = _module().obstacle(_unopposed(
        pool=pool, pool_add=FX.get("pool_add"), pool_default=FX.get("pool_default"), opposition_rate=FX.get("opposition_rate"),
        difficulty=float(FX.get("difficulty_ob")["plain"]), obstacle_ceiling=FX.get("obstacle_ceiling"),
        ceiling_per_pool=FX.get("ceiling_per_pool"), ceiling_form=FX.get("ceiling_form")))
    assert ob == even_line(FX.get("pool_add")) + opposed_ob(FX.get("pool_default"), FX.get("opposition_rate")), (ob, terms)   # the stand-in is IN the obstacle
    bands = band_odds(pool, ob)
    assert bands[2] + bands[3] > 0.0, (pool, ob, bands)


# ---------------------------------------------------------------------------------------------------------------------
# B05.59 -- THE ARGUMENT READS THE OWNER ON THE EVEN LINE (`29_DICE` item 29-4 step 6; gate 8's first half). The record is built by hand, so the
# composer alone is read: no host operand reader stands between the numbers below and the obstacle.
# ---------------------------------------------------------------------------------------------------------------------

def test_the_obstacle_is_even_line_plus_difficulty_plus_opposed_ob():
    """A hand-built record at `pool_add` 6, `plain` (difficulty 0), a person opposite bringing 2, the rate `MU_PER_DIE`, the ceiling off (so no bound
    hides a term): `obstacle == even_line(6) + opposed_ob(2, MU_PER_DIE)`, which is 3.2 (2.4 + 0.0 + 0.8), and the `terms` sum to it, folded left to
    right from 0.0 as the module folds them (the built-in `sum` of floats is compensated on Python 3.12+ and differs by an ulp). The even line is the
    FIRST term (29_DICE's falsifier: "absent from an argument's `terms`")."""
    from engine.dice_engine.sigma_leverage import MU_PER_DIE, even_line, opposed_ob
    from engine.season.queries.inputs import SocialContestInput
    from .test_sc01_obstacle_ceiling import _module
    inp = SocialContestInput(pool=11, opposition=2.0, difficulty=0.0, pool_default=2, pool_add=6, opposition_rate=MU_PER_DIE, obstacle_ceiling=None,
                             obstacle_refusal_multiple=3.0, leverage=0.0, ceiling_form="hard")
    ob, terms = _module().obstacle(inp)
    assert ob == even_line(6) + 0.0 + opposed_ob(2.0, MU_PER_DIE), (ob, terms)
    assert abs(ob - 3.2) < 1e-12, ob                                           # the entry's stated figure, read off the owner and not retyped into it
    assert [name for name, _ in terms][:3] == ["even", "difficulty", "opposition"], terms
    assert dict(terms)["even"] == even_line(6) and dict(terms)["opposition"] == opposed_ob(2.0, MU_PER_DIE), terms
    folded = 0.0
    for _, value in terms:
        folded += value
    assert folded == ob, (folded, ob, terms)
    # the falsifier: the same record at `pool_add` 0 composes no even line, and its obstacle is the lower one (here the Ob floor, `OB_MIN`, lifts it)
    bare, bare_terms = _module().obstacle(SocialContestInput(pool=11, opposition=2.0, difficulty=0.0, pool_default=2, pool_add=0, opposition_rate=MU_PER_DIE,
                                                             obstacle_ceiling=None, obstacle_refusal_multiple=3.0, leverage=0.0, ceiling_form="hard"))
    assert dict(bare_terms)["even"] == 0.0 and bare < ob, (bare, bare_terms, ob)
