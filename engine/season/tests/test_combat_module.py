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


import pytest

from ._fresh_process import entry_target, probe
from engine.dice_engine import draw

_PRIZE = "the body"


_PROBE = """
import sys, os, importlib, random, dataclasses
sys.path.insert(0, {root!r})
before = set(sys.modules)
mod_name, attr = {target!r}.split(":", 1)
entry = getattr(importlib.import_module(mod_name), attr)
from engine.season.queries.inputs import PersonalCombatInput
from engine.dice_engine import draw
qs = ("felled", "wounds", "max_wounds", "health_remaining", "health_full")
out = []
for seed, ends in ((7, (4, 4)), (11, (4, 1)), (3, (2, 4))):
    inp = PersonalCombatInput(claimants=("p_a", "p_b"), ends=ends, wound_quantities=qs)
    got = entry(inp, draw.seeded(draw.H2("test_combat_module", seed)))
    again = entry(inp, draw.seeded(draw.H2("test_combat_module", seed)))
    # THE PLAYABLE BRANCH (REM-31): a decider that always engages is the automated fight, and taking that branch
    # must load nothing of the host either (a host import placed behind `decide` would otherwise never be seen)
    played = entry(inp, draw.seeded(draw.H2("test_combat_module", seed)), decide=lambda view: "engage")
    out.append((seed, ends, type(got).__name__, got.claimants, dataclasses.asdict(got),
                again == got and played.wounds == got.wounds and played.rounds == got.rounds))
loaded = sorted(os.path.relpath(m.__file__, {root!r}) for n, m in list(sys.modules.items())
                if n not in before and getattr(m, "__file__", None)
                and os.path.abspath(m.__file__).startswith({root!r} + os.sep))
# THE ORACLE: the engine called directly, the way the seam called it before `31b`.
pkg = mod_name.rsplit(".", 1)[0]
wrapper, combatant = (importlib.import_module(pkg + "." + n) for n in ("wrapper", "combatant"))
oracle = []
for seed, ends, *_ in out:
    A, B = combatant.Combatant("p_a", end=ends[0]), combatant.Combatant("p_b", end=ends[1])
    seen = []
    r = wrapper.fight(A, B, cfg=None, rng=draw.seeded(draw.H2("test_combat_module", seed)), trace=seen.append, keyed_rounds=True)
    oracle.append((r, {{c.label: {{q: getattr(c.wt, q) for q in qs}} for c in (A, B)}}, seen))
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
    for (seed, ends, kind, claimants, rec, deterministic), (r, wt, seen) in zip(out, oracle):
        assert kind == "CombatOutcome", (seed, kind)
        assert deterministic, f"{role}: seed {seed} gave two results in one process"
        assert claimants == ("p_a", "p_b"), claimants
        # THE ORACLE COMPARISON, re-pointed at the record's fields: the engine called directly, its trackers and its trace
        assert rec["wounds"] == wt, f"{role}: seed {seed} lifted {rec['wounds']}, the trackers read {wt}"
        assert list(rec["trace"]) == seen, f"{role}: seed {seed} returned a trace that is not the engine's own"
        assert rec["rounds"] == sum(1 for e in seen if e["kind"] == "round_start"), (seed, rec["rounds"])
        # the integer `wrapper.fight` returns is not lifted: the engine's own `fight_result` event names it
        assert [e["result"] for e in seen if e["kind"] == "fight_result"] == [r], (seed, r)
        assert len(rec["trace"]) > 0, f"{role}: seed {seed} recorded no trace -- `_TRACE` was not captured"
        checked += 1
    assert checked == 3, checked
    assert len({(repr(o[4]["wounds"]), o[4]["rounds"]) for o in out}) > 1, (
        "every hand-built fight read the same; the comparison cannot tell the parties apart")


_FLAT_PROBE = """
import sys, random
sys.path.insert(0, {root!r})
from engine.substrate import composition
fight = composition.require("combat.fight")
from engine.season.queries.inputs import PersonalCombatInput
from engine.dice_engine import draw
inp = PersonalCombatInput(claimants=("p_a", "p_b"), ends=(4, 4),
                          wound_quantities=("felled", "wounds", "max_wounds", "health_remaining", "health_full"))
got = fight(inp, draw.seeded(draw.H2("test_combat_module", 7)))
import os
pkg = os.path.join({root!r}, "modules", "combat") + os.sep
flat = sorted(n for n, m in list(sys.modules.items()) if str(getattr(m, "__file__", "") or "").startswith(pkg) and not n.startswith("modules.combat"))
print(repr((type(got).__name__, flat, "modules.combat.core" in sys.modules)))
"""


def test_resolve_returns_no_winner_key():
    """B14.01: the seam's `resolve` returns only what the fold and the viewer read -- `wound_state`, `surrender`,
    `beat`, `rounds`, `trace` -- and the six keys no reader asked for are gone (`winner`, `result`, `unresolved`,
    `bouts`, `parties`, `seed`). The module entry returns a `CombatOutcome`, not a dict. FALSIFIER: a deleted key
    returning, or an entry that hands back a dict."""
    from ..data.matrix import Step
    from ..harness import probes as P
    from ..loop.driver import SeasonDriver
    from ..queries.inputs import CombatOutcome, PartyWounds
    from ..seam.wrappers import combat as C
    from ..seam.wrappers._entry import entry_for
    if C.engine() is None:
        pytest.fail(f"personal_combat engine unavailable: {C.load_error()}")
    w = P.tiny_world()
    w.step = Step.RESOLVE
    SeasonDriver(P.tiny_world())                       # registers the module entries a direct `resolve` calls
    got = C.resolve(w, ["p_low", "p_mid"], ["a"], "the body")
    assert got["status"] == "RESOLVED", got
    deleted = {"winner", "result", "unresolved", "bouts", "parties", "seed"}
    assert not deleted & set(got), sorted(deleted & set(got))
    assert {"wound_state", "surrender", "beat", "rounds", "trace"} <= set(got), sorted(got)
    # the entry's own return is the record (a frozen dataclass), with one `PartyWounds` per claimant
    entry, refusal = entry_for(C._PRIZE, C._PROVIDER)
    assert entry is not None, refusal
    out = entry.fn(C.combat_input(w, ["p_low", "p_mid"], "fight"), draw.seeded(draw.H2("test_combat_module", 0)))
    assert isinstance(out, CombatOutcome) and not isinstance(out, dict), type(out)
    assert out.claimants == ("p_low", "p_mid") and set(out.wounds) == {"p_low", "p_mid"}, out.claimants
    assert all(isinstance(v, PartyWounds) for v in out.wounds.values()), out.wounds
    assert out.rounds >= 1 and len(out.trace) > 0, (out.rounds, len(out.trace))
    # a felling carries a beat; a fight nobody was felled in carries none
    felled = [pid for pid, pw in out.wounds.items() if pw.felled]
    assert (out.beat is not None) == bool(felled), (out.beat, felled)


def test_a_self_fight_is_refused_party_gap(monkeypatch):
    """B14.20: one id as both claimants is refused before the engine is called -- `fight_estimate`'s own `PARTY-GAP` line
    (`actor == target`), now `resolve`'s too. FALSIFIER: a person fighting himself returns `RESOLVED`, or reaches the engine
    (the host's input builder, `combat_input`, is spied on and the test fails if it is reached)."""
    from ..data.matrix import Step
    from ..harness import probes as P
    from ..loop.driver import SeasonDriver
    from ..seam.wrappers import combat as C
    if C.engine() is None:
        pytest.fail(f"personal_combat engine unavailable: {C.load_error()}")
    w = P.tiny_world()
    w.step = Step.RESOLVE
    SeasonDriver(P.tiny_world())
    real, built = C.combat_input, []
    monkeypatch.setattr(C, "combat_input", lambda *a, **k: built.append(a) or real(*a, **k))
    got = C.resolve(w, ["p_low", "p_low"], ["a"], "the body")
    assert got["status"] == "PARTY-GAP", got
    assert "p_low" in got["why"], got
    assert not built, "the self-fight reached the input builder, so the engine"
    # the control: two distinct persons still resolve
    assert C.resolve(w, ["p_low", "p_mid"], ["a"], "the body")["status"] == "RESOLVED"
    assert len(built) == 1, "the control never built an input: the spy cannot observe the failure it excludes"


def test_wrapper_fight_has_no_default_stream():
    """B14.20: `wrapper.fight(A, B, cfg, rng, ...)` takes neither `cfg` nor `rng` by default, and no fallback builds an unseeded
    `random.Random()`: a missing stream is a signature error at the call site, not a branch. A caller may still PASS `cfg=None`
    (the engine's own `CFG`). FALSIFIER: a combat call that passes with no stream supplied."""
    import importlib
    import inspect
    Combatant = importlib.import_module("modules.combat.combatant").Combatant
    wrapper = importlib.import_module("modules.combat.wrapper")
    params = inspect.signature(wrapper.fight).parameters
    assert params["rng"].default is inspect._empty, params["rng"]
    assert params["cfg"].default is inspect._empty, params["cfg"]
    with pytest.raises(TypeError):
        wrapper.fight(Combatant("a"), Combatant("b"))
    with pytest.raises(TypeError):
        wrapper.fight(Combatant("a"), Combatant("b"), cfg=None)
    assert wrapper.fight(Combatant("a"), Combatant("b"), None, draw.seeded(draw.H2("test_combat_module", 1))) in (-1, 0, 1)
    assert "random.Random()" not in inspect.getsource(wrapper)


def test_a_fight_leaves_no_flat_module_behind():
    """CI-09: the engine is the package `modules.combat`; no sibling is also loaded under its flat name (two
    identities for one file). A fresh interpreter resolves `combat.fight`, runs one fight on the input the tests
    above build, and lists every module in `sys.modules` whose file is under `modules/combat/` and whose name is not `modules.combat.*`
    (by path, so no roster of names can miss a sibling)."""
    kind, flat, packaged = probe(_FLAT_PROBE, "", 300)
    assert kind == "CombatOutcome", kind
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
    (`MU_PER_DIE x score`, A-71): a party with three addends rolls three dice more and is attacked at the same Ob (A-79: practice raises a pool,
    never an opposition). The record's `pool_add` and `pool_floor` are the pair every roll reads (here 3 and 0, not the module's 6
    and 5); a record naming neither rolls at the module's own."""
    import importlib
    import random
    from collections import Counter
    from ..queries.inputs import PersonalCombatInput
    from engine.dice_engine.dice_engine import MU_PER_DIE
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
        ob = MU_PER_DIE * 2                    # score 2, opposed at the rate the module opposes at (B15.03; was the half-score, 1.0)
        for kw, want in ((dict(pool_add=6, pool_floor=5), {(11, ob), (8, ob)}),
                         (dict(pool_add=3, pool_floor=0), {(8, ob), (5, ob)}),
                         (dict(), {(11, ob), (8, ob)})):
            seen.clear()
            for seed in range(5):
                entry(PersonalCombatInput(claimants=("a", "b"), ends=(4, 4), wound_quantities=qs, scores=(2, 2),
                                          addends=(3, 0), **kw), draw.seeded(draw.H2("test_combat_module", seed)))
                checked += 1
            # B15.10: a wounded party's yield roll is the fight's other roll through `core.resolve`; it is at the `death` obstacle and takes the
            # pool WITHOUT the party's addends (the verb's, not the roll's), so it is told apart by its obstacle and read separately
            yob = importlib.import_module("modules.combat.config").CFG["YIELD_OB"]["death"]   # by name: a function-local `from modules` import raises the ratchet
            assert {k for k in seen if k[1] != yob} == want, (kw, dict(seen))
            assert {p for p, o in seen if o == yob} <= {min(p for p, _ in want)}, (kw, dict(seen))
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
            hit += bool(entry(inp, draw.seeded(draw.H2("test_combat_module", seed))).wounds["op"].felled)
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
    return dict(inp=inp, got=entry.fn(inp, draw.seeded(draw.H2("test_combat_module", seed))))


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
            return {q: getattr(r["got"].wounds[_A], q) for q in ("max_wounds", "health_full")}
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
            whole = _fight(_wounded_world("level", 0), seed)["got"].trace
            hurt_res = _fight(_wounded_world("level", lost_steps), seed)
            assert hurt_res["inp"].carried == (-lost_steps * unit, 0.0), hurt_res["inp"].carried       # one level per step, signed against him
            roll_whole = next(e for e in whole if e["kind"] == "roll")
            roll_hurt = next(e for e in hurt_res["got"].trace if e["kind"] == "roll")
            assert (roll_hurt["aggressor"], roll_hurt["pool"], roll_hurt["ob"]) == (roll_whole["aggressor"], roll_whole["pool"], roll_whole["ob"])
            want = -lost_steps * unit if roll_hurt["aggressor"] == _A else lost_steps * unit      # his own attack lower, or the roller's net higher
            assert abs((roll_hurt["net_sigma"] - roll_whole["net_sigma"]) - want) < 1e-9, (lost_steps, seed, roll_hurt, roll_whole)
            seen_aggressor.add(roll_hurt["aggressor"])
    assert seen_aggressor == {_A, _B}, f"the sweep read only {seen_aggressor}: both directions of the term must be observed"


# ---------------------------------------------------------------------------------------------------------------------
# B14.02 (A-81, D-U1-11a, C3-C11): THE PARTY LEFT STANDING `prevailed`; AN UNDECIDED FIGHT STILL WRITES.
# The scenes are hand-built through the real fold and WITNESS (`test_cp_t03_02_band_ending_and_body._fight`).
# ---------------------------------------------------------------------------------------------------------------------
def test_the_party_left_standing_is_prevailed():
    """`fight_ending` names `prevailed` for the party who is neither felled nor the yielder while the other party is, and
    `undecided` only where neither is. FALSIFIER: a felled or yielding party named `prevailed`, or a scene with nobody down
    naming one (every row below reads the word on the Event the real fold stamped)."""
    from .test_cp_t03_02_band_ending_and_body import (ACTOR, SUBJECT, FELLED, UNTOUCHED, WOUNDED, _fight as scene)
    checked = 0
    for (a, s, yielder), want in {
            (WOUNDED, FELLED, None): {ACTOR: "prevailed", SUBJECT: "felled"},
            (FELLED, WOUNDED, None): {ACTOR: "felled", SUBJECT: "prevailed"},
            (UNTOUCHED, FELLED, None): {ACTOR: "prevailed", SUBJECT: "felled"},
            (UNTOUCHED, WOUNDED, SUBJECT): {ACTOR: "prevailed", SUBJECT: "yielded"},
            (WOUNDED, UNTOUCHED, ACTOR): {ACTOR: "yielded", SUBJECT: "prevailed"},
            (FELLED, FELLED, None): {ACTOR: "felled", SUBJECT: "felled"},                       # nobody is left standing
            (UNTOUCHED, WOUNDED, None): {ACTOR: "undecided", SUBJECT: "undecided"}}.items():    # nobody is down
        _w, out, _b = scene(a, s, yielder=yielder, aid=f"b1402_{checked}")
        assert out, (a, s, yielder)
        for e in out:
            assert dict(e.ending) == want, (a, s, yielder, e.kind, e.ending)
            checked += 1
    assert checked >= 7


def test_an_undecided_fight_is_witnessed_by_those_present():
    """A-81, C3-C11: a fight with no victor still writes. Its Event is witnessed and WITNESS deposits it to those present
    (`co_located`, `firsthand`), and each party holds his own claim of it. Read on two undecided scenes: one party
    wounded and nobody down (an `undecided` ending on each party), and both untouched (`contest.undecided`, which
    carries no ending). A person the channels do not admit holds nothing, so the assertion can see the deposit it excludes."""
    from .test_cp_t03_02_band_ending_and_body import (ACTOR, SUBJECT, UNTOUCHED, WOUNDED, _fight as scene)
    from ..data.rosters import ENDING_UNDECIDED
    checked = 0
    for a, s, kind in ((UNTOUCHED, WOUNDED, "body.changed"), (UNTOUCHED, UNTOUCHED, "contest.undecided")):
        w, out, _b = scene(a, s, aid=f"b1402_u{checked}")
        assert kind in [e.kind for e in out], (a, s, [e.kind for e in out])
        assert all(e.ending == () or set(dict(e.ending).values()) == {ENDING_UNDECIDED} for e in out), [e.ending for e in out]
        held = {p.id: [c for c in p.ledger if c.predicate == kind] for p in w.persons.values()}
        for pid in (ACTOR, SUBJECT):                                              # each party holds his own claim
            assert held[pid], (kind, pid, "a party holds no claim of his own fight")
        # v12 B11.04: the `reach` channel TELLS the Event onward, so a non-party may also hold it `told_by`; those PRESENT hold it firsthand.
        present = [pid for pid in w.persons if pid not in (ACTOR, SUBJECT) and any(c.source == "firsthand" for c in held[pid])]
        assert present, (kind, "nobody present witnessed the undecided fight")
        assert all(c.source in ("firsthand", "told_by") for pid in w.persons for c in held[pid]), (kind, held)
        assert [pid for pid in w.persons if not held[pid]], (kind, "everyone witnessed: the non-witness clause is vacuous")
        checked += 1
    assert checked == 2


# ---------------------------------------------------------------------------------------------------------------------
# B14.03 (D-U1-06, C3-L5, F-PC-08 (a)): A FELLING RECORDS ITS SOURCE AND WEAPON, NEVER A DOER.
# ---------------------------------------------------------------------------------------------------------------------
def test_a_felling_deposits_fell_to_on_the_death_event():
    """The felled party's Subject carries `(victim, "fell_to", "<source>:<weapon>")` on the Event it earns
    (`person.died`), as `broke_observed` carries `broke`; WITNESS deposits it to the act's actor (the shipped
    `observation_deposit_mode`). FALSIFIER: a felling whose Event has no `fell_to`; a value that names a person (either
    party, or anyone in the world); a `fell_to` on a party the beat did not fell, or on a scene with no beat (the seam
    lifts `None` for an unfelled fight), or on a wound that did not kill. Read on the real fold and WITNESS."""
    from .test_cp_t03_02_band_ending_and_body import (ACTOR, SUBJECT, FELLED, UNTOUCHED, WOUNDED, _fight as scene)
    beat = {"by": ACTOR, "victim": SUBJECT, "source": "stophit", "weapon": "longsword", "round": 2}
    want = "stophit:longsword"
    checked = 0
    # (a) the beat's victim is felled: his Event carries it, and nobody else's does
    for a, s in ((WOUNDED, FELLED), (UNTOUCHED, FELLED)):
        w, out, _b = scene(a, s, aid=f"b1403_{checked}", beat=beat)
        fell = [(e.kind, o) for e in out for o in e.observed if o.predicate == "fell_to"]
        assert fell, (a, s, "a felling's Event carries no fell_to", [(e.kind, e.observed) for e in out])
        for kind, o in fell:
            assert kind == "person.died" and o.subject == SUBJECT and o.value == want, (kind, o)
            assert not any(pid in str(o.value) for pid in w.persons), o
            assert ACTOR not in o.value and SUBJECT not in o.value, o
            checked += 1
        # WITNESS: the act's actor (the shipped mode) holds the claim; a non-witness holds none
        held = {p.id: [c.value for c in p.ledger if c.subject == SUBJECT and c.predicate == "fell_to"]
                for p in w.persons.values()}
        assert held[ACTOR] == [want], (a, s, held)
        assert [pid for pid in w.persons if pid != ACTOR and not held[pid]], (a, s, "everyone holds it: the clause is vacuous")
        assert all(h == [] for pid, h in held.items() if pid != ACTOR), held
        checked += 1
    # (b) the beat names the other party: the actor's own felling carries it, the standing subject's does not
    flipped = {**beat, "by": SUBJECT, "victim": ACTOR}
    _w, out, _b = scene(FELLED, WOUNDED, aid="b1403_flip", beat=flipped)
    assert [o.subject for e in out for o in e.observed if o.predicate == "fell_to"] == [ACTOR], [e.observed for e in out]
    checked += 1
    # (c) controls: no beat, no `fell_to`; a wound that did not fell carries none even where a beat is on the result
    for a, s, b in ((WOUNDED, FELLED, None), (UNTOUCHED, WOUNDED, beat), (UNTOUCHED, UNTOUCHED, beat)):
        _w, out, _b = scene(a, s, aid=f"b1403_c{checked}", beat=b)
        assert out, (a, s)
        assert not [o for e in out for o in e.observed if o.predicate == "fell_to"], (a, s, b, [e.observed for e in out])
        checked += 1
    assert checked >= 8


# ---------------------------------------------------------------------------------------------------------------------
# B14.13 (F-PC-16): A ROUND OPENS WITH THE WEAPON AS ISSUED -- THE HALF-SWORD FORM DOES NOT CROSS THE ROUND BOUNDARY.
# ---------------------------------------------------------------------------------------------------------------------
def test_no_engagement_opens_in_a_halfsword_form(monkeypatch):
    """A longsword against plate at three seeds: every `engagement_start` weapon key, on either side, is a base key
    (`HALFSWORD_BASE` has no entry for it), and so is the first of each fight. FALSIFIER: an `engagement_start` that
    names a `_halfsword` record as either fighter's weapon. The control inside it: the fights reach later engagements (`later >= 1`), the only
    place a carried form could show; the red reading before the reset is the form reaching one."""
    import importlib
    import random
    wrapper = importlib.import_module("modules.combat.wrapper")
    Combatant = importlib.import_module("modules.combat.combatant").Combatant
    HALFSWORD_BASE = importlib.import_module("modules.combat.weapons").HALFSWORD_BASE
    S = importlib.import_module("modules.combat.combat_systems")
    real, carried = S.base_form, []
    monkeypatch.setattr(S, "base_form", lambda c: (carried.append(c.weapon in HALFSWORD_BASE), real(c))[1])   # the reset, seen
    checked = later = 0
    for seed in (0, 1, 2):
        A, B = Combatant("A", weapon="longsword", armor="heavy"), Combatant("B", weapon="arming", armor="heavy")
        events = []
        wrapper.fight(A, B, None, draw.seeded(draw.H2("test_combat_module", seed)), trace=events.append)
        starts = [e for e in events if e["kind"] == "engagement_start"]
        for i, e in enumerate(starts):
            for key in (e["weapon_A"], e["weapon_B"]):
                assert key not in HALFSWORD_BASE, (seed, i, key, "an engagement opened in a half-sword form")
                checked += 1
        later += max(0, len(starts) - 1)
    assert checked >= 1
    assert later >= 1, "no fight reached a second engagement: the carried form was never at issue"
    assert any(carried), "no engagement reset found a half-sword form to carry: the reset was never at issue"

# B14.24 (`U5b_PC_residue` §8, F-DICE-14 Edit C; A-1, A-30): A FIGHT IS PRICED BY THE BELIEVER'S OWN PICTURE OF IT.
# `sigma.believed_chance` answers a row whose prize binds `personal_combat` with the fight sampled on a private stream, read over
# the bands asked, with the OPPONENT'S kit and wounds as the believer's ledger gives them (the world's where he has seen him).
# ---------------------------------------------------------------------------------------------------------------------
_FIGHT_AXIS = "grandiose_humble"      # a pursuit axis the equal pursuits project onto (asserted below)
_FIGHT_RIVAL = "carry"                # an uncontested verb, whose pursuit term a believed chance never weights


def _believing_world(seed: int, body: int = 1000):
    """`tiny_world` at world seed `seed` with `odds_weighting` `believed`, a driver built (the module entry registered), and `_A`'s body at `body`.
    `_B` is the unhurt opponent he holds no claim about."""
    from ..harness import probes as P
    from ..loop.driver import SeasonDriver
    w = P.tiny_world()
    SeasonDriver(w)
    w.world_seed = seed
    w.fixtures = w.fixtures.sweep("odds_weighting", "believed").sweep("choice_temperature", 0)
    w.persons[_A].body = body
    return w


def _forms_fight(w, monkeypatch) -> bool:
    """`make_chooser`'s real ranking of a `fight` on `_B` and an uncontested rival for `_A`, the View carrying the real believed-odds query
    (`sigma.believed_odds_query`, closed over `w` and bound to him); the option set is planted and `pack_scenes` is a spy
    (`test_cr17_odds_weighting._ranked`'s shape). The alignment cells are planted on the rebound table: `fight` 1.0 and the rival 0.7 on one
    axis (the shipped table's own `fight` cells, all negative, are struck so the term is the planted one), so the fight outranks the rival exactly
    where the believed chance of its bands exceeds 0.7, a line the unhurt man's figures (0.68 to 0.85) mostly clear and the hurt man's (0.55 to
    0.77) mostly do not."""
    from types import SimpleNamespace
    from engine.substrate.descriptors import PURSUITS
    from ..data import verbs as V
    from ..decision import choose as CH
    from ..seam.wrappers import sigma
    from ..state.carriers import Candidate, Person
    table = {ax: {v: a for v, a in row.items() if v != "fight"} for ax, row in V.ALIGNMENT.items()}
    table.setdefault(_FIGHT_AXIS, {}).update({"fight": 1.0, _FIGHT_RIVAL: 0.7})
    monkeypatch.setattr(V, "ALIGNMENT", table)
    person = Person(id=_A, name=_A)
    person.pursuits = {n: 1.0 for n in PURSUITS}                  # roster-exempt: TEST FIXTURE, one vector for both worlds
    assert CH.deliberation_memo(person, w.fixtures)[CH._AXIS_W][_FIGHT_AXIS] > 0, "the equal pursuits project to nothing"
    seen = {}
    monkeypatch.setattr(CH, "opening_set", lambda p, view, q, fx: [Candidate("fight", _B), Candidate(_FIGHT_RIVAL, "prop_x")])

    def spy(p, ranked, budget, fx, mint, occasion=None):
        seen["ranked"] = [c.verb for c in ranked]
        return []
    monkeypatch.setattr(CH, "pack_scenes", spy)
    odds = sigma.believed_odds_query(w, w.persons[_A])
    CH.make_chooser(w.fixtures, lambda *a: "act")(person, SimpleNamespace(question=object(), odds=odds), SimpleNamespace(), lambda: 1)
    assert "ranked" in seen, "the chooser never ranked: the falsifier did not run"
    return seen["ranked"][0] == "fight"


def test_a_hurt_man_forms_fight_less_often_on_believed_odds(monkeypatch):
    """B14.24 (the gate's reading): with `odds_weighting` `believed`, a person at `body` 400 forms `fight` on an unhurt opponent less often than
    the same person unhurt, over seeds 0 to 29 (before the item nothing read his body: `believed_chance` was `None` for a fight, the weight
    1.0, and both formed it every time). FALSIFIER: the two counts equal, or the unhurt man forming it on no seed (nothing to lose)."""
    formed = {400: 0, 1000: 0}
    checked = 0
    for seed in range(30):
        for body in formed:
            formed[body] += _forms_fight(_believing_world(seed, body), monkeypatch)
            checked += 1
    assert checked >= 30, checked
    assert formed[1000] > 0, f"the unhurt man formed no fight on any seed: {formed}"
    assert formed[400] < formed[1000], f"a hurt man formed fight no less often than an unhurt one: {formed}"


class _Sighting:
    """A `seen` deposit's value: only `who` is read here (`person_q.heritage_regard` reads the same field)."""
    def __init__(self, who):
        self.who, self.marks = who, ()


def test_an_estimate_reads_no_kit_the_believer_has_no_claim_about(monkeypatch):
    """B14.24's falsifier: the believer's estimate of a fight reads the OPPONENT'S kit and wounds as the believer's ledger gives them. The world
    arms `_B` with a longsword and heavy armour and wounds him to `body` 400; `_A` holds NO claim about him and has not seen him. The input the
    sampler deals is built on the DEFAULT kit and an UNHURT body, not the true ones. Then the same world with a sighting (the world's, `seen`)
    reads the true kit and the true wound, and with a claim reads the claim's kit: the assertion can see the leak it excludes. `_A`'s OWN kit is
    his own."""
    from engine.substrate import combat_kit
    from ..data.rosters import SEEN_PREDICATE
    from ..queries import person_q
    from ..seam.wrappers import combat as C, sigma
    from ..state.carriers import Act, Claim
    default = (combat_kit.DEFAULTS["weapon"], combat_kit.DEFAULTS["armor"])
    true_kit, claimed, own = ("longsword", "heavy"), ("dagger", "none"), ("poleaxe", "medium")
    assert len({default, true_kit, claimed, own}) == 4
    monkeypatch.setattr(C, "kit_of", lambda w, pid: own if pid == _A else true_kit)
    real, built = C.combat_input, []
    monkeypatch.setattr(C, "combat_input", lambda *a, **k: built.append(real(*a, **k)) or built[-1])

    def read(*claims):
        w = _believing_world(3)
        w.persons[_B].body = 400
        w.persons[_A].ledger.extend(claims)
        built.clear()
        got = sigma.believed_chance(w, w.persons[_A], Act("a", _A, "fight", payload={"subject": _B}), ("Felled", "Wounded"))
        assert got is not None and 0.0 <= got <= 1.0, got
        assert len(built) == 1, built
        return built[0], w

    blind, w = read()
    unhurt = _believing_world(3)
    def wound_of(inp):
        """How the wound reaches the fight under the shipped arm: his `end` (the cut, `endurance_cut`), his carried level (`level`), and the levels
        against him the mortal roll charges (`mortal[1][3]`, B15.07: his body band, read off the same picture as the other two)."""
        return inp.ends[1], inp.carried[1], inp.mortal[1][3]
    def mortal_levels(world):
        """The mortal roll's levels against `_B` as the WORLD'S body gives them (the dealt fight's, no believer)."""
        return C._mortal_operands(world, _B, (_A, _B), blind.terms, False)[3]
    true_wound = (C.party_end(w.persons[_B], w.fixtures), C._carried_of(w.persons[_B], w.fixtures), mortal_levels(w))
    unhurt_wound = (C.party_end(unhurt.persons[_B], unhurt.fixtures), C._carried_of(unhurt.persons[_B], unhurt.fixtures), mortal_levels(unhurt))
    assert true_wound != unhurt_wound, "the world's wound reaches the fight by neither arm: the control cannot see the leak"
    assert true_wound[2] != unhurt_wound[2], "the world's wound reaches the mortal roll's levels by no band: the control cannot see that leak"
    assert blind.kits == (own, default), blind.kits                            # his own kit is his own; the stranger's is the DEFAULT, not the true one
    assert wound_of(blind) == unhurt_wound, (wound_of(blind), "the opponent's wound leaked into the believer's picture")
    sighting = Claim("c_seen", _A, "R", SEEN_PREDICATE, _Sighting(_B), 0, "firsthand", 5, "own")
    seen_it = read(sighting)[0]
    assert seen_it.kits == (own, true_kit) and wound_of(seen_it) == true_wound, (seen_it.kits, wound_of(seen_it), true_wound)   # where he has seen him: the world's
    said = read(Claim("c_w", _A, _B, person_q.KIT_CLAIM + "weapon", claimed[0], 0, "told", 5, "own"),
                Claim("c_a", _A, _B, person_q.KIT_CLAIM + "armor", claimed[1], 0, "told", 5, "own"))[0]
    assert said.kits == (own, claimed), said.kits                              # a claim of his: the claim's, over the default
    wounded = read(Claim("c_b", _A, _B, person_q.BODY_CLAIM, 400, 0, "told", 5, "own"))[0]
    assert wound_of(wounded) == true_wound and wounded.kits == (own, default), (wound_of(wounded), wounded.kits)   # a claim of his wound: the wound, the kit still the default


def test_the_believed_estimate_is_private_and_moves_no_hash():
    """B14.24's control: `believed_chance` on a fight reads `World` and writes nothing -- `content_hash` and the season draw are the same with
    the call and without it, the figure is the same on every ask (a private stream keyed `estimate.fight`, not a season draw), the sample
    count is `believed_fight_samples`' (not the display's `estimate_samples`), another's act and a band the combat ladder does not carry are
    `None`."""
    from ..seam.wrappers import sigma
    from ..state.carriers import Act
    act = Act("a", _A, "fight", payload={"subject": _B})
    control, called = _believing_world(2), _believing_world(2)
    assert control.content_hash() == called.content_hash() and control.draw == called.draw
    first = sigma.believed_chance(called, called.persons[_A], act, ("Felled", "Wounded"))
    again = sigma.believed_chance(called, called.persons[_A], act, ("Felled", "Wounded"))
    assert first is not None and first == again, (first, again)
    assert called.content_hash() == control.content_hash(), "the believed estimate moved the world's content hash"
    assert called.draw == control.draw and called.new_draw() == control.new_draw(), "the believed estimate took a season draw"
    n = called.fixtures.get("believed_fight_samples")
    assert n == 60 and n != called.fixtures.get("estimate_samples"), n
    assert abs(first * n - round(first * n)) < 1e-9, (first, n)              # a share of `n` scenes, not of the display's 400
    assert sigma.believed_chance(called, called.persons[_A], act, ("Won",)) is None
    assert sigma.believed_chance(called, called.persons[_B], act, ("Felled",)) is None
    assert sigma.believed_chance(called, called.persons[_A], act, ()) is None


# ---------------------------------------------------------------------------------------------------------------------
# B14.23 (`U5b_PC_residue` §7; A-30, A-5 to A-8): THE LASTING MARK MAY BE DRAWN, AND SHIPS AT TODAY'S ARM.
# ---------------------------------------------------------------------------------------------------------------------
def test_drawn_marks_yield_all_three_outcomes_over_200_seeds():
    """200 seeded fights, each leaving a survivor at his limit (`wounds == max_wounds`, one gate short of felling), folded through the real
    gate at `body_mark_model` `drawn`: Failure leaves ceiling 499 (`marked_ceiling` applied twice), Partial 799 (as today), Success and better
    1000 (no mark); one `marked` Observation on the survivor's Event exactly where a mark fell, carrying the ceiling written. FALSIFIER: under
    `drawn`, a mark on every such survivor (the 1000 outcome absent), or a `marked` Observation beside no mark. CONTROL: `deepest_gate` marks
    every one of the same fights at 799 and records no `marked`, so the assertions can see what `drawn` changed. The draw is keyed by the victim
    and its own purpose (`fight.mark`): the same seed and victim give the same outcome whatever the act's id."""
    from ..harness import probes as P
    from ._scar_helpers import party_state
    from .test_cp_t03_07_body_ceiling import DEEPEST, SUBJECT, _fight as fold

    def one(seed: int, model: str, aid: str = "b1423"):
        w = P.tiny_world()
        w.world_seed = seed
        w.fixtures = w.fixtures.sweep("body_mark_model", model)
        _res, out = fold(w, party_state(**DEEPEST), aid=aid)
        marked = [o for e in out for o in e.observed if o.predicate == "marked"]
        return w.persons[SUBJECT].body_ceiling, marked

    ceilings, checked = {}, 0
    for seed in range(200):
        ceiling, marked = one(seed, "drawn")
        assert (len(marked) == 1 and marked[0].subject == SUBJECT and marked[0].value == ceiling) if ceiling < 1000 else not marked, (seed, ceiling, marked)
        assert not marked or ceiling in (799, 499), (seed, ceiling)
        ceilings[ceiling] = ceilings.get(ceiling, 0) + 1
        checked += 1
        held, held_marked = one(seed, "deepest_gate")                    # the control, the same fight
        assert (held, held_marked) == (799, []), (seed, held, held_marked)
    assert checked >= 200
    assert set(ceilings) == {1000, 799, 499}, f"the three outcomes each occur over {checked} seeds: {ceilings}"
    assert ceilings[1000] < checked, "a mark on every survivor is the certainty the draw replaces"
    for seed in range(8):                                                # keyed by victim and purpose, not by the act or a stream position
        assert one(seed, "drawn", aid="x")[0] == one(seed, "drawn", aid="y")[0]


# ---------------------------------------------------------------------------------------------------------------------
# B15.07 (PHY_A A3; A-5 to A-8, A-30, A-81): A FELLING IS FOLLOWED BY THE MORTAL-WOUND DRAW, IN THE MODULE.
# ---------------------------------------------------------------------------------------------------------------------
def _module_of_entry():
    """The combat module the host's entry resolves to (reached by the composition row, never imported by name here)."""
    import sys
    from ..loop.driver import SeasonDriver
    from ..harness import probes as P
    from ..seam.wrappers import combat
    SeasonDriver(P.tiny_world())
    entry, refusal = combat.entry_for(combat._PRIZE, combat._PROVIDER)
    assert entry is not None, refusal
    return sys.modules[entry.fn.__module__], entry


def test_mortal_wound_every_band_writes():
    """A-81: every band of the mortal draw writes. Over 400 keyed draws for one felled party (pool 8, the season's untrained default; obstacle 3):
    Failure keeps him felled at the scene's wounds (he dies: the host's band `Felled`); Partial stands him up at `max_wounds` or the scene's wounds,
    the more (left for dead; on an engine-produced tracker, `max_wounds + 1`, the same as Success: H-576); Success and Overwhelming stand him up at
    the scene's wounds. Through the host's map (`_wound_state`) and the one grader (`party_degree`)
    no band is `Untouched`, the band that writes nothing. FALSIFIER: a band missing over 400 draws, a Partial below `max_wounds`, a survivor
    still felled, or a band the host grades `Untouched`. The draw is keyed: the same key gives the same result."""
    import dataclasses
    from ..data.rosters import FELLED
    from ..queries.inputs import PartyWounds
    from ..seam.ladder import party_degree
    from ..seam.wrappers import combat
    mod, _entry = _module_of_entry()
    # THE STATES THE ENGINE PRODUCES: a felled tracker carries `wounds == max_wounds + 1` (`combatant.py`: `wounds` is capped at `max_wounds + 1`
    # and a felling is `cumulative_damage >= health_full`), for each fighter's own `max_wounds`; none holds fewer. ⚠ So Partial's
    # `max(wounds, max_wounds)` equals Success's `wounds` on every state the engine produces: the two survivor bands write the SAME `wounds` (hole row
    # H-576, held for a ruling). `want` asserts what each band writes today, `partial` included; it is not a claim that the two should agree.
    seen, checked = {}, 0
    for max_wounds in (5, 4):
        pw = PartyWounds(felled=True, wounds=max_wounds + 1, max_wounds=max_wounds, health_remaining=0, health_full=12)
        scene_wounds = pw.wounds
        for seed in range(400):
            m = mod.mortal_wound(pw, draw.seeded(draw.H2("test_mortal_wound", seed)), (8.0, 3.0, (), ()))
            assert m == mod.mortal_wound(pw, draw.seeded(draw.H2("test_mortal_wound", seed)), (8.0, 3.0, (), ())), seed
            want = {"fail": (True, scene_wounds), "partial": (False, max(max_wounds, scene_wounds))}.get(m.degree, (False, scene_wounds))
            assert (m.mortal, m.wounds) == want, (seed, m)
            band = party_degree(combat._wound_state(pw, m))
            assert (band == FELLED) == m.mortal and band in ("Felled", "Wounded"), (seed, m, band)
            seen[m.degree] = seen.get(m.degree, 0) + 1
            checked += 1
    assert checked >= 800
    pw = dataclasses.replace(pw, wounds=5 + 1, max_wounds=5)
    assert set(seen) == {"fail", "partial", "success", "overwhelming"}, f"each band occurs over {checked} draws: {seen}"
    # levels move it: a level for raises the survivors, a level against lowers them, on the same keys
    def survivors(f, a):
        return sum(not mod.mortal_wound(pw, draw.seeded(draw.H2("test_mortal_wound", s)), (8.0, 3.0, f, a)).mortal for s in range(400))
    assert survivors(("major",), ()) > survivors((), ()) > survivors((), ("major",)), "a level is not applied to the mortal roll"


def test_unreachable_mortal_ob_reproduces_the_shipped_deaths():
    """THE CONTROL (PHY_A's falsifier): at the unreachable `mortal_wound_ob` (99.0 for every cause) the season's fight, under `death` terms, deals
    exactly the deaths it dealt with no draw: over 300 seeds, the host's `wound_state` with the draw equals the one built on the same record with
    `mortal=()` (no draw), party by party, and the scene (rounds, beat, trace) is the same scene -- the draw is keyed apart from the scene's
    stream (`fight.mortal`) and moves nothing at control. Every felled party is drawn for and dies. FALSIFIER: a survivor at the control, a scene
    that differs with the draw, or a felled party not drawn for."""
    import dataclasses
    from ..seam.wrappers import combat
    from ..harness import probes as P
    _mod, entry = _module_of_entry()
    w = P.tiny_world()
    w.fixtures = w.fixtures.sweep("mortal_wound_ob", {c: 99.0 for c in w.fixtures.get("mortal_wound_ob")})
    deaths = checked = 0
    for seed in range(300):     # was 200: a failed yield roll (B15.10) ends about a third of lethal scenes with both alive, so fewer parties are felled
        w.world_seed = seed
        inp = combat.combat_input(w, ["p_low", "p_mid"], "fight")
        assert inp.terms == "death" and len(inp.mortal) == 2, (inp.terms, inp.mortal)
        key = draw.H2("test_unreachable_mortal_ob", seed)
        drawn, bare = entry.fn(inp, draw.seeded(key)), entry.fn(dataclasses.replace(inp, mortal=()), draw.seeded(key))
        assert (drawn.rounds, drawn.beat, drawn.trace, drawn.wounds) == (bare.rounds, bare.beat, bare.trace, bare.wounds), seed
        assert set(drawn.mortal) == {p for p, pw in drawn.wounds.items() if pw.felled} and not bare.mortal, (seed, drawn.mortal)
        for pid in drawn.wounds:
            assert combat._wound_state(drawn.wounds[pid], drawn.mortal.get(pid)) == combat._wound_state(bare.wounds[pid]), (seed, pid)
        deaths += sum(m.mortal for m in drawn.mortal.values())
        checked += 1
    assert checked == 300 and deaths >= 150, (checked, deaths)


def _round_inp(seed, ends=(4, 4), kits=(), terms="death"):
    from ..queries.inputs import PersonalCombatInput
    return PersonalCombatInput(claimants=("p_a", "p_b"), ends=ends, kits=kits, terms=terms,
                               wound_quantities=("felled", "wounds", "max_wounds", "health_remaining", "health_full"))


def _fight_by_rounds(inp, rng, fight_round, limit=12):
    """The rounds of one fight called by hand, the `DuelState`s and the measure threaded in this frame: yields each round's outcome."""
    from ..queries.inputs import DuelRoundInput, DuelState
    from modules.combat import wrapper
    states, prev_closed = (DuelState(), DuelState()), False
    fkey = wrapper.fight_draw(draw.seeded(rng.key))
    for r in range(1, limit + 1):
        out = fight_round(DuelRoundInput(fighters=inp, states=states, plans=({}, {}), round=r, prev_closed=prev_closed), wrapper.round_draw(fkey, r))
        yield out
        states, prev_closed = out.states, out.closed
        if out.felled or out.yielded or any(e["kind"] == "fight_result" for e in out.trace):
            return


def test_round_keeps_no_state_between_calls():
    """B16.01 (PB step 1): `fight_round` keeps nothing. One round input and one key give one outcome, however many other fights and rounds were called
    in between, and the engine's trace hook is not left bound; what a round takes from another is the `DuelState` it is handed and nothing else (the same
    input with a hurt `DuelState` is another round). FALSIFIER: a second call that differs from the first, a bound `_TRACE`, or a state that moves nothing."""
    import dataclasses
    import importlib
    from engine.substrate import composition
    from ..queries.inputs import DuelRoundInput, DuelState
    fight, fight_round = composition.require("combat.fight"), composition.require("combat.round")
    wrapper = importlib.import_module("modules.combat.wrapper")
    inp = _round_inp(5, kits=(("longsword", "heavy"), ("arming", "light")))
    rin = DuelRoundInput(fighters=inp, states=(DuelState(), DuelState()), plans=({}, {}), round=1)
    first = fight_round(rin, draw.seeded(draw.H2("test_round_state", 1)))
    for s in range(5):    # other fights, and other rounds, called between the two
        fight(_round_inp(s, ends=(2, 5)), draw.seeded(draw.H2("test_round_state_other", s)))
        fight_round(dataclasses.replace(rin, round=3), draw.seeded(draw.H2("test_round_state_other", s)))
    again = fight_round(rin, draw.seeded(draw.H2("test_round_state", 1)))
    assert again == first, "a second call of the same round, on the same key, differs: the module kept something"
    assert wrapper._TRACE is None, "the round left the engine's trace hook bound"
    hurt = dataclasses.replace(rin, states=(DuelState(cumulative_damage=first.states[0].cumulative_damage + 6, stamina=5.0, conc=2.0, poise=0.4), DuelState()))
    other = fight_round(hurt, draw.seeded(draw.H2("test_round_state", 1)))
    assert other.states != first.states and other.trace != first.trace, "a carried state moved nothing in the round"


def test_round_outcome_names_how_it_ended():
    """B16.01 (PCR-2): over 100 fights (a different matchup per seed, the three duel terms among them), each round of each: `ended_by` is `felled` where
    the round felled a party, else the reason of its one `separation` event, and a member of `ROUND_ENDS`; `exchanges` is its `outcome` events;
    `sum(attempts.values())` its `roll`, `stophit` and pursued `disengage` events. The between-round recovery is taken at the end of a round the fight
    goes on from and never after a felling or a yield (counted at `wrapper.recover`). There is no `winner` on the round. FALSIFIER: an `ended_by` that
    disagrees with the trace, a count that does not, a recovery after a felling, a `winner` field."""
    import dataclasses
    import importlib
    from engine.substrate import composition
    from ..queries.inputs import DuelRoundOutcome
    fight_round = composition.require("combat.round")
    wrapper = importlib.import_module("modules.combat.wrapper")
    vocabulary = importlib.import_module("modules.combat.vocabulary")
    assert "winner" not in {f.name for f in dataclasses.fields(DuelRoundOutcome)}
    recoveries = []
    real = wrapper.recover
    wrapper.recover = lambda A, B, cfg: (recoveries.append(1), real(A, B, cfg))[1]
    kit_sets = ((), (("longsword", "heavy"), ("arming", "light")), (("spear", "light"), ("mace", "medium")), (("rapier", "none"), ("longsword", "heavy")))
    checked, ends_seen, felled_rounds, recovered_rounds = 0, set(), 0, 0
    try:
        for seed in range(100):
            inp = _round_inp(seed, ends=((4, 4), (3, 5), (2, 4))[seed % 3], kits=kit_sets[seed % 4], terms=("death", "blood", "yield")[seed % 3])
            recoveries.clear()
            for out in _fight_by_rounds(inp, draw.seeded(draw.H2("test_round_ended_by", seed)), fight_round):
                seps = [e["reason"] for e in out.trace if e["kind"] == "separation"]
                assert out.ended_by == ("felled" if out.felled else seps[-1]), (seed, out.ended_by, out.felled, seps)
                assert out.ended_by in vocabulary.ROUND_ENDS, out.ended_by
                assert len(seps) == (0 if out.felled else 1), (seed, seps)
                assert out.exchanges == sum(e["kind"] == "outcome" for e in out.trace), seed
                assert sum(out.attempts.values()) == sum(bool(e["kind"] in ("roll", "stophit") or (e["kind"] == "disengage" and e.get("pursued")))
                                                         for e in out.trace), seed
                assert set(out.attempts) == {"p_a", "p_b"}
                goes_on = out.felled is None and out.yielded is None and not any(e["kind"] == "fight_result" for e in out.trace)
                assert len(recoveries) == goes_on, (seed, "the recovery is taken exactly where the fight goes on", out.ended_by, out.felled, out.yielded)
                recoveries.clear()
                recovered_rounds += goes_on
                ends_seen.add(out.ended_by)
                felled_rounds += out.felled is not None
                checked += 1
    finally:
        wrapper.recover = real
    assert checked >= 100, checked
    assert felled_rounds > 0 and recovered_rounds > 0 and len(ends_seen) >= 4, (
        f"the fights ended rounds by {sorted(ends_seen)} only ({felled_rounds} felled, {recovered_rounds} recovered): the comparison cannot tell endings apart")


# What each fight below drew and traced at B16.03 (c11b2a91f, before the lean was read): the round's `Draw.n` after each round, and the head of the md5 of
# the rounds' traces' reprs. Read off the tree before B16.05's edit; an all-`normal` fight that draws one more or one fewer number moves a count.
_AS_AT_B1603 = {("duel", 3): ((29, 21), "945b5f19e931"), ("duel", 11): ((33, 32, 22, 33), "7d81b312451d"),
                ("reach", 3): ((69, 12), "0d0ccb9b7d8d"), ("reach", 11): ((57, 49), "bb5e527c1a3f"),
                ("fast", 3): ((27, 14, 15), "d9ffc6e3d8b3"), ("fast", 11): ((25, 19, 15, 44), "8f39c7a671b9")}
_KIT_SETS = {"duel": (("longsword", "heavy"), ("arming", "light")), "reach": (("spear", "light"), ("mace", "medium")),
             "fast": (("rapier", "none"), ("longsword", "heavy"))}


def test_all_normal_plans_draw_the_same_count_as_today():
    """B16.05 (PB step 3a, "all-`normal` byte-identical to step 2"): six fights, played round by round on the round's own `Draw`. Each is played twice, with
    `plans=({}, {})` and with every phase named `normal` for both parties, and the two are one fight event for event; each fight's per-round `Draw.n` and its
    traces' digest are the literals read at B16.03, before the lean was built. A `normal` lean draws nothing and reorders nothing. FALSIFIER: a draw taken (or
    skipped) by an all-`normal` round moves a count; a lean read where `normal` is lean 0 moves a trace."""
    import hashlib
    from engine.substrate import composition
    from ..queries.inputs import DuelRoundInput, DuelState
    from modules.combat import wrapper
    fight_round = composition.require("combat.round")
    normal = {ph: "normal" for ph in ("measure", "exchange", "bind")}

    def play(name, seed, plans):
        inp = _round_inp(seed, kits=_KIT_SETS[name])
        fkey = wrapper.fight_draw(draw.seeded(draw.H2("b16.05", f"{name}:{seed}")))
        states, closed, counts, digest, trace = (DuelState(), DuelState()), False, [], hashlib.md5(), []
        for r in range(1, 13):
            rng = wrapper.round_draw(fkey, r)
            out = fight_round(DuelRoundInput(fighters=inp, states=states, plans=plans, round=r, prev_closed=closed), rng)
            counts.append(rng.n); digest.update(repr(out.trace).encode()); trace.extend(out.trace)
            states, closed = out.states, out.closed
            if out.felled or out.yielded or any(e["kind"] == "fight_result" for e in out.trace):
                break
        return tuple(counts), digest.hexdigest()[:12], trace
    checked = 0
    for (name, seed), (counts, head) in _AS_AT_B1603.items():
        empty = play(name, seed, ({}, {}))
        named = play(name, seed, (dict(normal), dict(normal)))
        assert empty[:2] == (counts, head), f"{name}/{seed}: an all-normal fight draws or traces other than it did at B16.03: {empty[:2]} != {(counts, head)}"
        assert named == empty, f"{name}/{seed}: naming `normal` in every phase is not the same fight as naming nothing"
        checked += 1
    assert checked == len(_AS_AT_B1603) == 6
