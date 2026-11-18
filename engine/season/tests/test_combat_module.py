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
    # THE PLAYABLE BRANCH (REM-31): a decider that always engages is the automated fight, and taking that branch
    # must load nothing of the host either (a host import placed behind `decide` would otherwise never be seen)
    played = entry(inp, random.Random(seed), decide=lambda view: "engage")
    out.append((seed, ends, got["status"], got["result"], got["ends"], got["wound_state"],
                len(got["trace"]), again == got and played["result"] == got["result"]
                and played["ends"] == got["ends"] and played["wound_state"] == got["wound_state"]))
loaded = sorted(os.path.relpath(m.__file__, {root!r}) for n, m in list(sys.modules.items())
                if n not in before and getattr(m, "__file__", None)
                and os.path.abspath(m.__file__).startswith({root!r} + os.sep))
# THE ORACLE: the engine called directly, the way the seam called it before `31b`.
pkg = mod_name.rsplit(".", 1)[0]
wrapper, combatant = (importlib.import_module(pkg + "." + n) for n in ("wrapper", "combatant"))
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
               "engine/season/queries/inputs.py", module_dir.split("/", 1)[0] + "/__init__.py"}
    stray = [f for f in loaded
             if f not in allowed and not f.startswith("engine/dice_engine/")
             and not f.startswith(module_dir + "/")]
    assert not stray, (
        f"{role} ({target}) loaded repository code beyond the engine it runs and the record "
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


_FLAT_PROBE = """
import sys, random
sys.path.insert(0, {root!r})
from engine.substrate import composition
fight = composition.require("combat.fight")
from engine.season.queries.inputs import PersonalCombatInput
inp = PersonalCombatInput(claimants=("p_a", "p_b"), ends=(4, 4),
                          wound_quantities=("felled", "wounds", "max_wounds", "health_remaining", "health_full"))
got = fight(inp, random.Random(7))
import os
pkg = os.path.join({root!r}, "modules", "combat") + os.sep
flat = sorted(n for n, m in list(sys.modules.items()) if str(getattr(m, "__file__", "") or "").startswith(pkg) and not n.startswith("modules.combat"))
print(repr((got["status"], flat, "modules.combat.core" in sys.modules)))
"""


def test_a_fight_leaves_no_flat_module_behind():
    """CI-09: the engine is the package `modules.combat`; no sibling is also loaded under its flat name (two
    identities for one file). A fresh interpreter resolves `combat.fight`, runs one fight on the input the tests
    above build, and lists every module in `sys.modules` whose file is under `modules/combat/` and whose name is not `modules.combat.*`
    (by path, so no roster of names can miss a sibling)."""
    status, flat, packaged = probe(_FLAT_PROBE, "", 300)
    assert status == "RESOLVED", status
    assert not flat, f"flat module names loaded beside the package: {flat}"
    assert packaged, "`modules.combat.core` was not loaded: the fight did not run through the package"


# ---------------------------------------------------------------------------------------------------------------------
# B05.57 (`UPR` §2 edits 1-3; CAP B7; D-U1-08, F-PC-08 (d)): THE FIGHT'S TWO INPUTS AND THE ONE POOL RULE.
# A fight's pool is `pool_of(score, addends, add, floor)`, UNROUNDED; the skill score and the attribute are two numbers.
# ---------------------------------------------------------------------------------------------------------------------
def test_resolution_pool_is_unrounded_and_floored():
    """`resolution_pool(2.5)` is 8.5 and `resolution_pool(-3)` is 5 (addends 0, the module's own base and floor): the pool is
    the owner's `pool_of`, with no `int(round(.))` (a fractional pool is canonical, F-PC-08 (d)) and a negative score meets the
    floor. The addends and the row's two operands are the owner's too: `max(floor, score + addends + add)`."""
    import importlib
    core = importlib.import_module("modules.combat.core")
    sl = importlib.import_module("engine.dice_engine.sigma_leverage")
    assert core.resolution_pool(2.5, 0) == 8.5
    assert core.resolution_pool(-3, 0) == 5
    checked = 0
    for score, addends, add, floor in ((2, 3, 1, 0), (2.5, 1, 0, 9), (0, 0, 6, 5), (-3, 0, 6, 5), (4, 2, 3.5, 5)):
        assert core.resolution_pool(score, addends, add, floor) == sl.pool_of(score, addends, add, floor)
        checked += 1
    assert core.resolution_pool(2, 3, 1, 0) == 6          # the addends are summed into the pool, not into the Ob
    assert checked == 5


def test_an_addend_raises_the_pool_and_never_the_ob_and_the_records_pair_is_the_engines():
    """The fight's pool is `pool_of(score, addends, pool_add, pool_floor)` and its Ob is the defender's skill score alone
    (`faculty / 2`): a party with three addends rolls three dice more and is attacked at the same Ob (A-79: practice raises a pool,
    never an opposition). The record's `pool_add` and `pool_floor` are the pair every roll reads (here 3 and 0, not the module's 6
    and 5); a record naming neither rolls at the module's own."""
    import importlib
    import random
    from collections import Counter
    from ..queries.inputs import PersonalCombatInput
    core = importlib.import_module("modules.combat.core")
    mod, attr = entry_target(_PRIZE)[1].split(":", 1)
    entry = getattr(importlib.import_module(mod), attr)
    seen, real = Counter(), core.resolve
    from ..data.rosters import roster
    qs = tuple(roster("wound_quantities", ordered=True))

    def spy(pool, net_sigma, rng, ob):
        seen[(pool, ob)] += 1
        return real(pool, net_sigma, rng, ob)
    core.resolve = spy
    try:
        checked = 0
        for kw, want in ((dict(pool_add=6, pool_floor=5), {(11, 1.0), (8, 1.0)}),
                         (dict(pool_add=3, pool_floor=0), {(8, 1.0), (5, 1.0)}),
                         (dict(), {(11, 1.0), (8, 1.0)})):
            seen.clear()
            for seed in range(5):
                entry(PersonalCombatInput(claimants=("a", "b"), ends=(4, 4), wound_quantities=qs, scores=(2, 2),
                                          addends=(3, 0), **kw), random.Random(seed))
                checked += 1
            assert set(seen) == want, (kw, dict(seen))
    finally:
        core.resolve = real
    assert checked == 15


def test_skill_score_and_attribute_move_the_fight_separately():
    """A-7: the skill score and the attribute reach a fight as two numbers. A hand-built pair, one of skill score 5 and
    Strength 2, one of skill score 2 and Strength 5, each fights one opponent (score 3, Strength 4) over seeds 0 to 399:
    the opponent's felled share differs between the two by more than the disjoint-seed band (three binomial standard errors
    of a difference of two shares, at the widest p = 1/2). And each input moves the share alone: score 5 against 2 at one
    Strength, Strength 5 against 2 at one score."""
    import importlib
    import random
    from ..queries.inputs import PersonalCombatInput
    mod, attr = entry_target(_PRIZE)[1].split(":", 1)
    entry = getattr(importlib.import_module(mod), attr)
    from ..data.rosters import roster
    qs = tuple(roster("wound_quantities", ordered=True))
    n = 400
    band = 3 * (2 * 0.25 / n) ** 0.5

    def felled_share(score: int, strength: int) -> float:
        hit = 0
        for seed in range(n):
            inp = PersonalCombatInput(claimants=("me", "op"), ends=(4, 4), wound_quantities=qs, scores=(score, 3),
                                      addends=(0, 0), attributes=({"attr.body.strength": strength}, {}))
            hit += bool(entry(inp, random.Random(seed))["wound_state"]["op"]["felled"])
        return hit / n

    checked = 0
    for (s1, a1), (s2, a2) in (((5, 2), (2, 5)), ((5, 4), (2, 4)), ((3, 5), (3, 2))):
        d = abs(felled_share(s1, a1) - felled_share(s2, a2))
        assert d > band, f"score {s1} / Strength {a1} and score {s2} / Strength {a2} fell within {band:.3f} of each other: {d:.3f}"
        checked += 1
    assert checked >= 2


# ---------------------------------------------------------------------------------------------------------------------
# B05.61 (`UPR` §3 edits 1-4; A-8): A WOUND CARRIED INTO A FIGHT IS A LEVEL, NOT A SHORTER HEALTH TRACK.
# Under `carried_wound_model` `level` the authored Endurance arrives whole and the wound rides on `PersonalCombatInput.carried`, once.
# ---------------------------------------------------------------------------------------------------------------------
_A, _B = "p_low", "p_mid"                      # `tiny_world`'s two persons


def _wounded_world(model: str, lost_steps: int = 0, who: str = _A):
    """`tiny_world` with `carried_wound_model` swept to `model` and `who` having lost `lost_steps` of `wound_step` below his ceiling.
    Builds a driver too, which registers the combat module entry the host resolves."""
    from ..harness import probes as P
    from ..loop.driver import SeasonDriver
    w = P.tiny_world()
    SeasonDriver(w)
    w.fixtures = w.fixtures.sweep("carried_wound_model", model)
    w.persons[who].body = w.persons[who].body_ceiling - lost_steps * w.fixtures.get("wound_step")
    return w


def _fight(w, seed: int = 5) -> dict:
    """The record the host builds for `_A` fighting `_B` and the module entry's result on it, one seeded fight (the entry the seam resolves)."""
    import random
    from ..seam.wrappers import combat
    entry, refusal = combat.entry_for(combat._PRIZE, combat._PROVIDER)
    assert entry is not None, refusal
    inp = combat.combat_input(w, [_A, _B], "fight")
    return dict(inp=inp, got=entry.fn(inp, random.Random(seed)))


def test_a_carried_wound_leaves_health_and_max_wounds_whole():
    """UNDER `level` a party one band down, and one at the bottom band, has the Health and Max Wounds of an unwounded man: `party_end` cuts no
    band. The same worlds under the control `endurance_cut` read lower on every one, so the assertion can see the cut it excludes."""
    from ..decision import body_band_penalty
    checked = 0
    for lost_steps in (1, 2, 3):                 # a third, two thirds and the whole of the body lost: down a band, deeper, the bottom
        whole = _fight(_wounded_world("level", 0))
        hurt_w = _wounded_world("level", lost_steps)
        assert body_band_penalty(hurt_w.persons[_A], hurt_w.fixtures) >= 1, "the planted wound is below the first body band"
        hurt = _fight(hurt_w)
        assert hurt["inp"].ends == whole["inp"].ends, (lost_steps, hurt["inp"].ends, whole["inp"].ends)

        def full(r):
            return {q: r["got"]["wound_state"][_A][q] for q in ("max_wounds", "health_full")}
        assert full(hurt) == full(whole), (lost_steps, full(hurt), full(whole))
        assert hurt["inp"].carried[0] < 0.0 and hurt["inp"].carried[1] == 0.0 and whole["inp"].carried == (0.0, 0.0), hurt["inp"].carried
        cut = _fight(_wounded_world("endurance_cut", lost_steps))
        assert cut["inp"].ends[0] < whole["inp"].ends[0] and cut["inp"].carried == (0.0, 0.0), cut["inp"]
        assert full(cut) != full(whole), "under the control the same wound shrinks Health and Max Wounds: the falsifier's reading"
        checked += 1
    assert checked == 3


def test_the_carried_level_is_applied_once():
    """The trace's first roll's net sigma for a carried party differs from the unwounded mirror's by EXACTLY one `wound_step` level
    (`LEVEL_SIGMA[wound_level]`, 0.25 at `minor`) per band lost, not two: the host sizes it once (`combat._carried_of`) and the module adds it once
    (`assemble_net_sigma`), the party's own, against his attack when he strikes and against his defence when he is struck. The direction is read off
    the roll's aggressor. Seeds 0 to 7 fight the wounded and the whole world at one seed each, so the draws agree up to the first roll."""
    from engine.dice_engine.sigma_leverage import LEVEL_SIGMA
    unit = LEVEL_SIGMA["minor"]
    seen_aggressor = set()
    for lost_steps in (1, 2):
        for seed in range(8):
            whole = _fight(_wounded_world("level", 0), seed)["got"]["trace"]
            hurt_res = _fight(_wounded_world("level", lost_steps), seed)
            assert hurt_res["inp"].carried == (-lost_steps * unit, 0.0), hurt_res["inp"].carried       # one level per step, signed against him
            roll_whole = next(e for e in whole if e["kind"] == "roll")
            roll_hurt = next(e for e in hurt_res["got"]["trace"] if e["kind"] == "roll")
            assert (roll_hurt["aggressor"], roll_hurt["pool"], roll_hurt["ob"]) == (roll_whole["aggressor"], roll_whole["pool"], roll_whole["ob"])
            want = -lost_steps * unit if roll_hurt["aggressor"] == _A else lost_steps * unit      # his own attack lower, or the roller's net higher
            assert abs((roll_hurt["net_sigma"] - roll_whole["net_sigma"]) - want) < 1e-9, (lost_steps, seed, roll_hurt, roll_whole)
            seen_aggressor.add(roll_hurt["aggressor"])
    assert seen_aggressor == {_A, _B}, f"the sweep read only {seen_aggressor}: both directions of the term must be observed"
