"""TN is 7. Always. Everywhere. (ED-IN-0196)

    Jordan, 2026-08-25, verbatim: "TN7 always. Never change TN anywhere ever."

WHY THIS GUARD EXISTS, AND WHY IT IS NOT APPARATUS-GUARDING-APPARATUS.
CLAUDE.md §0.1 point 5 admits a guard only when the defective artifact class is
load-bearing on the game, on a Jordan decision, on the exported params, or on the port.
This one is load-bearing on three of the four:

  * the game — TN is an input to every resolution in six subsystems;
  * a Jordan decision — the ruling above is the whole subject;
  * the exported params — `WEAPON_TN_BASE` crosses to Godot via
    `tools/export_game_constants.py`, so a re-introduced TN axis would ship to the port.

THE TRAP IT CLOSES, which is the real reason it is here.
Before the ruling, four independent mechanisms made TN vary. THREE OF THEM WERE INERT,
because `dice_engine.roll_pool` never read its `tn` argument:

    systems/combat/sim/combat.py        WEAPON_TN_MOD, shifting TN across 5-8
    systems/threadwork/sim/operations.py TN_BINDING=8, TN_POP=8, TN_POP_BINDING=9
    engine/autoload/sigma_leverage.py    a "Controlled 6 / Standard 7 / Desperate 8" scale

Those constants READ AS BUGS: named, plausible, and provably doing nothing. The natural
"fix" a future session would reach for is to make `dice_engine` honour `tn` — and that one
edit would silently re-activate a weapon matrix and three threadwork mechanics across six
subsystems in a single commit, violating the ruling everywhere at once while every targeted
test stayed green.

So the guard's job is not to check that a value is 7 today. It is to make that specific
"fix" impossible to land quietly. `test_the_die_rule_is_pinned_face_by_face` is the load
-bearing one: it pins all ten faces, so a change letting 6 score cannot pass.

The fourth mechanism, `VOLLEY_TN = 6`, was LIVE — it hand-rolled its own d10 loop and
bypassed the owner entirely (ED-MB-0066). A repeat of THAT shape is caught by
`test_no_tn_constant_is_anything_but_7` (a named non-7 TN) and by
`test_no_hand_rolled_d10_uses_a_non_canonical_face_boundary` (a bare literal); §5 below
explains why neither alone is sufficient.
"""
from __future__ import annotations

import pathlib
import random
import re

import pytest

from engine.autoload import dice_engine as de
from engine.autoload import sigma_leverage as sl
from systems.mass_battle.sim import resolution as mb


REPO = pathlib.Path(__file__).resolve().parents[2]

# The canonical face rule, pinned face by face. 1 fumbles, 2-6 score nothing,
# 7-9 each score one success, 10 scores two. No TN moves any of these boundaries.
CANONICAL_FACES = {1: -1, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 1, 8: 1, 9: 1, 10: 2}


# ── 1. The owner refuses ──────────────────────────────────────────────────────────────

@pytest.mark.parametrize("bad_tn", [5, 6, 8, 9, 0, -1])
def test_the_owner_refuses_a_non_7_tn(bad_tn):
    with pytest.raises(ValueError, match="TN is 7"):
        de.roll_pool(5, tn=bad_tn, rng=random.Random(0))
    with pytest.raises(ValueError, match="TN is 7"):
        de.continuous_engine_sample(5.0, tn=bad_tn, rng=random.Random(0))


def test_tn_7_is_accepted():
    """The refusal must not be so broad it breaks the one legal value."""
    assert de.roll_pool(5, tn=7, rng=random.Random(0)).net is not None
    assert isinstance(de.continuous_engine_sample(5.0, tn=7, rng=random.Random(0)), float)


# ── 2. THE LOAD-BEARING ONE: the die rule cannot be quietly widened ────────────────────

def test_the_die_rule_is_pinned_face_by_face():
    """Make "teach dice_engine to honour tn" impossible to land silently.

    A bounds/property test (does net stay within +-2 per die) would pass happily if faces
    6-9 started scoring. This does not: every face is pinned to its exact contribution.
    """
    for face, expected in CANONICAL_FACES.items():
        assert de._die_result(face) == expected, (
            f"face {face} scores {de._die_result(face)}, canon says {expected} — if this "
            "changed because dice_engine now honours `tn`, that violates the ruling in this "
            "file's docstring across six subsystems at once"
        )


def test_the_mass_battle_roller_uses_the_same_face_window():
    """The second roller in the tree must not drift from the first.

    `resolution.roll_pool` scores its own faces (it takes no engine dependency by design),
    so equivalence is held by this test rather than by an import — the same pattern
    test_degree_ladder_single_owner.py uses for the degree ladder.
    """
    for face, expected in CANONICAL_FACES.items():
        class _FixedRng:
            def randint(self, _a, _b):
                return face

        import contextlib
        from systems.mass_battle.sim import rngsource
        with contextlib.ExitStack() as stack:
            stack.enter_context(rngsource.using(_FixedRng()))
            got = mb.roll_pool(1)
        assert got == expected, f"mass_battle face {face} -> {got}, canon says {expected}"


@pytest.mark.parametrize("bad_tn", [6, 8])
def test_the_mass_battle_roller_also_refuses_non_7(bad_tn):
    with pytest.raises(AssertionError, match="TN is 7"):
        mb.roll_pool(3, bad_tn)
    with pytest.raises(AssertionError, match="TN is 7"):
        mb.roll_pool_fractional(3.5, bad_tn)


# ── 3. No constant may name a TN that is not 7 ────────────────────────────────────────

_TN_CONST = re.compile(r'^\s*([A-Z_]*TN[A-Z_]*)\s*=\s*(\d+)\s*(?:#.*)?$', re.M)
_SCAN_ROOTS = ("engine", "systems")


def _tn_constants():
    found = []
    for root in _SCAN_ROOTS:
        for path in sorted((REPO / root).rglob("*.py")):
            if "/tests/" in str(path).replace("\\", "/"):
                continue
            for name, value in _TN_CONST.findall(path.read_text(encoding="utf-8")):
                found.append((path.relative_to(REPO).as_posix(), name, int(value)))
    return found


def test_no_tn_constant_is_anything_but_7():
    offenders = [f for f in _tn_constants() if f[2] != 7]
    assert not offenders, (
        "TN constants that are not 7 — the ruling forbids these; express a varying "
        f"difficulty as an Ob: {offenders}"
    )


def test_the_tn_constant_sweep_actually_found_constants():
    """Assert that it asserted (§0.1 point 2).

    Without this, a regex that silently stopped matching would make the test above pass
    over a tree full of violations. The roster measured at ED-MB-0066 is 11.
    """
    found = _tn_constants()
    assert len(found) >= 8, (
        f"the TN-constant sweep found only {len(found)} constants — the pattern has probably "
        "stopped matching, and the test above is now vacuous"
    )


# ── 4. The per-die EV tables carry only TN 7 ──────────────────────────────────────────

def test_only_tn7_survives_in_the_ev_tables():
    assert de._MU_PER_DIE == 0.40
    assert de._SIGMA_PER_DIE == 0.800
    assert set(sl.PER_DIE) == {7}, (
        f"sigma_leverage.PER_DIE carries {sorted(sl.PER_DIE)} — TN 6 and TN 8 are superseded "
        "canon and a live row is a way back to them"
    )
    assert sl.PER_DIE[7] == (0.40, 0.800)


def test_sigma_leverage_raises_on_a_superseded_tn():
    """PER_DIE stays a dict precisely so this is loud rather than silent."""
    with pytest.raises(KeyError):
        sl.net_boost(1.0, 10, tn=6)


# ── 5. The dangerous class: a hand-rolled d10 whose face boundaries are not canonical ──
#
# HOW THE TWO HALVES OF THIS DIVIDE, stated plainly because neither is sufficient alone:
#
#   * `VOLLEY_TN = 6` was scored as `roll >= VOLLEY_TN` — a NAME, not a literal. The scan
#     below cannot see that, and does not pretend to. `test_no_tn_constant_is_anything_but_7`
#     is what catches that shape, and it would have caught VOLLEY_TN on the day it landed.
#   * A future hand-roller could instead write `roll >= 6` with no named constant at all,
#     which the constant sweep cannot see. That is this scan's job.
#
# Together they cover both spellings. An earlier version of this scan was a bare regex for
# `>= N` and flagged seven false positives — discipline tiers, orbit directions, pool sizes —
# because it had no idea which variables hold a die face. It was deleted rather than tuned: a
# guard that cries wolf gets ignored, which is worse than not having it.

import ast

CANONICAL_FACE_BOUNDS = {1, 7, 9, 10}   # the only literals the canonical rule compares a face to


def _die_face_comparisons(tree):
    """Yield (lineno, literal) for comparisons of a d10-face variable against an int literal.

    A "d10-face variable" is one bound to a `randint(1, 10)` call inside the same function —
    real dataflow, not a text match, which is what keeps this off the false positives.
    """
    for fn in ast.walk(tree):
        if not isinstance(fn, (ast.FunctionDef, ast.AsyncFunctionDef)):
            continue
        faces = set()
        for node in ast.walk(fn):
            if not isinstance(node, ast.Assign) or not isinstance(node.value, ast.Call):
                continue
            call = node.value
            args = call.args
            if (getattr(call.func, "attr", None) == "randint" and len(args) == 2
                    and all(isinstance(a, ast.Constant) for a in args)
                    and (args[0].value, args[1].value) == (1, 10)):
                for tgt in node.targets:
                    if isinstance(tgt, ast.Name):
                        faces.add(tgt.id)
        if not faces:
            continue
        for node in ast.walk(fn):
            if not isinstance(node, ast.Compare):
                continue
            operands = [node.left, *node.comparators]
            names = {o.id for o in operands if isinstance(o, ast.Name)}
            if not (names & faces):
                continue
            for o in operands:
                if isinstance(o, ast.Constant) and isinstance(o.value, int):
                    if o.value not in CANONICAL_FACE_BOUNDS:
                        yield node.lineno, o.value


def _files_that_roll_their_own_d10s():
    out = []
    for root in _SCAN_ROOTS:
        for path in sorted((REPO / root).rglob("*.py")):
            p = path.relative_to(REPO).as_posix()
            if "/tests/" in p:
                continue
            text = path.read_text(encoding="utf-8")
            if "randint(1, 10)" in text or "randint(1,10)" in text:
                out.append((p, text))
    return out


def test_no_hand_rolled_d10_uses_a_non_canonical_face_boundary():
    offenders = []
    for p, text in _files_that_roll_their_own_d10s():
        for lineno, literal in _die_face_comparisons(ast.parse(text)):
            offenders.append(f"{p}:{lineno} compares a d10 face against {literal}")
    assert not offenders, (
        "a hand-rolled d10 compares a face against a non-canonical boundary. The canonical "
        f"rule only ever compares against {sorted(CANONICAL_FACE_BOUNDS)}:\n  "
        + "\n  ".join(offenders)
    )


def test_the_hand_rolled_scan_actually_reaches_a_hand_roller():
    """Assert that it asserted (§0.1 point 2).

    If every hand-rolled d10 were refactored away the scan would go vacuously green, so it
    must keep finding at least one file to inspect. `units.py` still rolls its own — the
    discipline check at units.py:2106 — which is the live example that keeps this honest.
    Note orchestration.py is deliberately NOT the anchor any more: ED-MB-0066 removed its
    hand-rolled volley loop, which is exactly the outcome this guard wants.
    """
    files = dict(_files_that_roll_their_own_d10s())
    assert files, "no file rolls its own d10 any more — this scan is now vacuous"
    assert "systems/mass_battle/sim/hierarchy/units.py" in files, sorted(files)
    parsed = sum(1 for _p, t in files.items() for _ in [ast.parse(t)])
    assert parsed >= 2, f"only {parsed} hand-rolling file(s) parsed"
