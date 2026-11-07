"""CR-85 (ED-IN-0330/0331) -- COMBAT'S POOL AND OB READ `faculty`, NOT `history`.

The season computes each party's `faculty(w, person, verb)` (`seam/wrappers/sigma.py`, THE ONE POOL READER) in
`seam/wrappers/combat.py::combat_input`, it crosses the seam as `PersonalCombatInput.faculties`, and the module
(`modules/combat/fight.py`) constructs each `Combatant` with it. Inside the module it is read in exactly two places,
the pool (`core.resolution_pool`, `max(5, faculty + 6)`) and the Ob the opponent rolls against
(`core.ob_from_defender`, `faculty / 2`); the five sigma reads of `history` are deleted.
[ASSUMPTION; medium; Jordan to correct; revert: delete the design file; history stays] -- built on
`proposals/2026-11-05-cr85-histories-hooks-and-combat-input.md` as written, which is UNRATIFIED (ED-IN-0349 was
withdrawn by ED-IN-0351).

  FALSIFIER: every roll a seeded season's fights make reads (8, 1.0) -- no verb names a combat key, so `faculty` is
  `pool_default` 2 and the module reads pool `max(5, 2 + 6)` against Ob `2 / 2`.
  PLANTED: a party holding the combat key at 5 (a test-local `VERB_CAPABILITY` row, no roster row) rolls pool 11 and
  his opponent rolls against Ob 2.5.
  MUTATION (executed, not by hand): the seam's read dropped (`faculties` left empty, the module default 3) reproduces
  (9, 1.5), and the falsifier's check goes red.
  CONTROL: the seam's value replaced by 3 for every party reproduces the pre-item one-season hash exactly -- the five
  deleted sigma terms were exactly 0.0 in every season fight (both parties at history 3, empty `skills`).
  ⚠ `build_realm(0)` forms no fight in one season since CR-87, so the falsifier reads seeds 1 and 2; seed 0's hash
  does not move, and neither does seed 2's: its fights roll at (8, 1.0) and land where they landed at (9, 1.5).
"""
from __future__ import annotations

import dataclasses
import importlib
import random
from collections import Counter

import pytest

from engine.substrate import pc_engine

from ..harness.populated import build_realm, run
from ..seam.wrappers import combat as C
from ..seam.wrappers import sigma
from ._fresh_process import entry_target
from .test_cp_t03_04_arms import revert_cp_t03_04
from .test_cp_t03_07_body_ceiling import revert_cp_t03_07


# ⚠ A FIXTURE, NOT A MODULE-LEVEL `skipif(C.engine() is None)` (`test_combat_band_edges.py`'s precedent):
# `test_importing_every_engine_module_pulls_in_no_subsystem` imports this module, and `C.engine()` at import loads
# the combat engine. The engine is loaded when a test RUNS.
@pytest.fixture(autouse=True)
def _engine_available():
    if C.engine() is None:
        pytest.skip(f"personal_combat engine unavailable: {C.load_error()}")

#: The one-season realm hashes BEFORE this item (93662b9a). `build_realm(seed)` itself does not move (7266f56b...).
PRE_ITEM = {0: "20accb03c3d32f80a9fab00d80a70b21",
            1: "f89ea45dd050cdf2329fde8885a1a110",
            2: "fe9032eda9b7701241dcbd766c96fd1a"}
#: The same, AFTER: only seed 1 moves (seed 0 fights nothing; seed 2's fights land where they did).
POST_ITEM = {0: "20accb03c3d32f80a9fab00d80a70b21",
             1: "6e25b047b1fb42e2d50014f100770053",
             2: "fe9032eda9b7701241dcbd766c96fd1a"}

_KEY = "cr85_test_arms"   # a test-local capability key: no roster row is added


def revert_cr85(monkeypatch):
    """The item at its control, in process: the seam's faculty replaced by 3 for every party, which is the value
    `history` held in every season fight before this item. Other tests that pin a pre-item hash call it."""
    real = C.combat_input
    monkeypatch.setattr(C, "combat_input",
                        lambda *a, **k: dataclasses.replace(real(*a, **k), faculties=(3, 3)))


def _drop_the_read(monkeypatch):
    """THE MUTATION: the seam's read dropped -- the record carries no faculties, so the module's default stands."""
    real = C.combat_input
    monkeypatch.setattr(C, "combat_input",
                        lambda *a, **k: dataclasses.replace(real(*a, **k), faculties=()))


def _spy(monkeypatch) -> Counter:
    """Count every `(pool, ob)` the engine's `core.resolve` is called with."""
    core = pc_engine.load()[0].core
    seen, real = Counter(), core.resolve

    def spy(pool, net_sigma, rng, ob):
        seen[(pool, ob)] += 1
        return real(pool, net_sigma, rng, ob)
    monkeypatch.setattr(core, "resolve", spy)
    return seen


def _season_rolls(monkeypatch, seed) -> tuple:
    seen = _spy(monkeypatch)
    w = build_realm(seed)
    run(1, seed, w=w)
    return seen, w.content_hash()


def _off_the_reading(seen: Counter, want=(8, 1.0)) -> list:
    """The falsifier's check: every roll at `want`, and at least one roll seen (an empty count asserts nothing)."""
    bad = [k for k in seen if k != want]
    if not seen:
        bad.append("setup: no roll was made")
    return bad


@pytest.mark.parametrize("seed", [1, 2])
def test_falsifier_every_season_roll_reads_pool_8_against_ob_1(seed, monkeypatch):
    # v11 CP-T03-04 (`arms` in the vocation range, a formation mover of every season) is reverted so `POST_ITEM` stands;
    # its own file reads the live tree's rolls (`test_cp_t03_04_arms.py`, every season roll still at (8, 1.0)).
    revert_cp_t03_04(monkeypatch)
    revert_cp_t03_07(monkeypatch)        # v11 CP-T03-07 (`body_ceiling`, a schema mover of every realm), the same way
    seen, got = _season_rolls(monkeypatch, seed)
    assert _off_the_reading(seen) == [], dict(seen)
    assert got == POST_ITEM[seed]


def test_mutation_the_seam_read_dropped_reproduces_9_against_1_5_and_reddens(monkeypatch):
    _drop_the_read(monkeypatch)
    seen, _ = _season_rolls(monkeypatch, 1)
    assert set(seen) == {(9, 1.5)}, dict(seen)
    assert _off_the_reading(seen) != []


@pytest.mark.parametrize("seed", [0, 1, 2])
def test_control_faculty_3_for_every_party_reproduces_the_pre_item_hash(seed, monkeypatch):
    revert_cr85(monkeypatch)
    revert_cp_t03_04(monkeypatch)        # v11 CP-T03-04, a later formation mover of every season: so `PRE_ITEM` stands
    revert_cp_t03_07(monkeypatch)        # v11 CP-T03-07 (`body_ceiling`, a schema mover of every realm), the same way
    seen, got = _season_rolls(monkeypatch, seed)
    assert got == PRE_ITEM[seed]
    assert set(seen) <= {(9, 1.5)}, dict(seen)
    assert (POST_ITEM[seed] != PRE_ITEM[seed]) == (seed == 1)


def test_planted_a_party_holding_the_combat_key_at_5_rolls_11_and_is_attacked_at_ob_2_5(monkeypatch):
    """A test-local `VERB_CAPABILITY` row names `fight`'s key; one party holds it at 5, the other none (the fallback,
    `pool_default` 2). His rolls are pool 11 against his opponent's Ob 1.0; his opponent's are pool 8 against 2.5."""
    monkeypatch.setattr(sigma, "VERB_CAPABILITY", {**sigma.VERB_CAPABILITY, "fight": _KEY})
    w = build_realm(1)
    a, b = sorted(w.persons)[:2]
    w.persons[a].capability = {**(w.persons[a].capability or {}), _KEY: 5}
    assert _KEY not in (w.persons[b].capability or {})
    inp = C.combat_input(w, [a, b], "fight")
    assert inp.faculties == (5, 2), inp.faculties
    mod, attr = entry_target("the body")[1].split(":", 1)
    entry = getattr(importlib.import_module(mod), attr)
    seen = _spy(monkeypatch)
    checked = 0
    for s in range(6):
        entry(inp, random.Random(s))
        checked += 1
    assert set(seen) == {(11, 1.0), (8, 2.5)}, dict(seen)
    assert checked == 6
