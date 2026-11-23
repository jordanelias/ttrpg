"""CR-85 (ED-IN-0330/0331) -- COMBAT'S POOL AND OB READ `faculty`, NOT `history`.

The season computes each party's `faculty(w, person, verb)` (`seam/wrappers/sigma.py`, THE ONE POOL READER) in
`seam/wrappers/combat.py::combat_input`, it crosses the seam as `PersonalCombatInput.scores` and `.addends` (B05.57), and the module
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
  MUTATION (executed, not by hand): the seam's read dropped (`scores` and `addends` left empty, the module default 3) reproduces
  (9, 1.5), and the falsifier's check goes red.
  CONTROL: the realm hashes are `_realm_goldens.py`'s.
  ⚠ `build_realm(0)` forms no fight in one season since CR-87, so the falsifier reads seeds 1 and 2.
"""
from __future__ import annotations

import importlib
from engine.dice_engine import draw
from collections import Counter

import pytest


from ..boot.realm import build_realm
from ..harness.populated import run
from ..seam.wrappers import combat as C
from ..seam.wrappers import pool, sigma
from ._fresh_process import entry_target


# ⚠ A FIXTURE, NOT A MODULE-LEVEL `skipif(C.engine() is None)` (`test_combat_band_edges.py`'s precedent):
# `test_importing_every_engine_module_pulls_in_no_subsystem` imports this module, and `C.engine()` at import loads
# the combat engine. The engine is loaded when a test RUNS.
@pytest.fixture(autouse=True)
def _engine_available():
    if C.engine() is None:
        pytest.fail(f"personal_combat engine unavailable: {C.load_error()}")

_KEY = "cr85_test_arms"   # a test-local capability key: no roster row is added
_ARMS = "arms"             # the roster key BA1.01 authors scores on


def _spy(monkeypatch) -> Counter:
    """Count every `(pool, ob)` the engine's `core.resolve` is called with."""
    # by name, inside the function: `test_importing_every_engine_module_pulls_in_no_subsystem` fails on a module-scope import and the ratchet counts a written one
    core = importlib.import_module("modules.combat.core")
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


@pytest.mark.parametrize("seed", [1, 2])
def test_falsifier_every_season_roll_reads_pool_8_against_ob_1_unless_an_authored_holder_is_party(seed, monkeypatch):
    """BA1.99 re-point (was: every roll reads pool 8 against Ob 1.0). On the world with no attribute seated (B11 lane A's persons-hold-scores
    at its revert: a drawn sheet moves a pool and an Ob by itself, and the falsifier is about the seam's read, not the sheets), a roll reads
    pool 8 against Ob 1.0 unless a party holds a key above the untrained score; BA1.01 authors `arms` on 11 persons (3 or 5), so such rolls
    exist and each reads `pool_of(attacker's score)` against `opposed_ob(defender's score)` for a score the build seats or one `_grown` raises
    by one -- no other pool or Ob is read. Both halves are observed: the untrained reading (8, 1.0) still occurs for the persons who author
    nothing, and a pool above 8 occurs for an authored holder. The realm's hash is `_realm_goldens.py`'s."""
    from engine.dice_engine.sigma_leverage import opposed_ob, pool_of
    from ..seam.wrappers.pool import FIGHT_DICE_SITE, pool_pair, untrained
    from .test_b11a_scores_and_obstacle import revert_b11a_scores
    revert_b11a_scores(monkeypatch)
    w0 = build_realm(seed)
    authored = {p.capability[_ARMS] for p in w0.persons.values() if _ARMS in (p.capability or {})}
    assert authored == {3, 5}, authored                       # the BA1.01 `arms` scores, read off the build (setup: the world has holders)
    pool_add, pool_floor = pool_pair(w0.fixtures, FIGHT_DICE_SITE)
    scores = {untrained(w0.fixtures)} | authored | {v + 1 for v in authored}
    allowed = {(pool_of(a, 0, pool_add, pool_floor), opposed_ob(b, 0.5)) for a in scores for b in scores}    # 0.5: the module's own constant
    seen, _ = _season_rolls(monkeypatch, seed)
    assert set(seen) <= allowed, sorted(set(seen) - allowed)
    assert (8, 1.0) in seen and any(pool > 8 for pool, _ob in seen), dict(seen)


def test_planted_a_party_holding_the_combat_key_at_5_rolls_11_and_is_attacked_at_ob_2_5(monkeypatch):
    """A test-local `VERB_CAPABILITY` row names `fight`'s key; one party holds it at 5, the other none (the fallback,
    `pool_default` 2). His rolls are pool 11 against his opponent's Ob 1.0; his opponent's are pool 8 against 2.5."""
    monkeypatch.setattr(pool, "VERB_CAPABILITY", {**pool.VERB_CAPABILITY, "fight": _KEY})
    w = build_realm(1)
    a, b = sorted(w.persons)[:2]
    w.persons[a].capability = {**(w.persons[a].capability or {}), _KEY: 5}
    assert _KEY not in (w.persons[b].capability or {})
    inp = C.combat_input(w, [a, b], "fight")
    assert inp.scores == (5, 2) and inp.addends == (0, 0), (inp.scores, inp.addends)
    mod, attr = entry_target("the body")[1].split(":", 1)
    entry = getattr(importlib.import_module(mod), attr)
    seen = _spy(monkeypatch)
    checked = 0
    for s in range(6):
        entry(inp, draw.seeded(draw.H2("test_cr85_faculty_replaces_history", s)))
        checked += 1
    assert set(seen) == {(11, 1.0), (8, 2.5)}, dict(seen)
    assert checked == 6


def test_the_record_carries_the_opposition_rate_to_the_module():
    """B05.58 (29-2): a hand-built `PersonalCombatInput` with `opposition_rate=0.4` and skill scores (2, 3) is fought at Ob
    `0.4 x` the struck party's score, `{0.8, 1.2}`; with `None` (the module's own constant, 0.5) at `{1.0, 1.5}`."""
    from ..queries.inputs import PersonalCombatInput
    mod, attr = entry_target("the body")[1].split(":", 1)
    entry = getattr(importlib.import_module(mod), attr)

    def obs(rate) -> set:
        inp = PersonalCombatInput(claimants=("a", "b"), ends=(5, 5), wound_quantities=(), scores=(2, 3), opposition_rate=rate)
        seen, checked = set(), 0
        for s in range(8):
            for ev in entry(inp, draw.seeded(draw.H2("test_cr85_faculty_replaces_history", s))).trace:
                if "ob" in ev:
                    seen.add(round(ev["ob"], 9))
                    checked += 1
        assert checked >= 1, checked
        return seen

    assert obs(0.4) == {0.8, 1.2}
    assert obs(None) == {1.0, 1.5}
