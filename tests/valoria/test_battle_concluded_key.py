"""The second live Key emitter — `scene.battle_concluded` (ED-IN-0122).

WHY THIS EXISTS. The Key substrate is the architecture's inter-subsystem transport: subsystems are
supposed to announce state changes as typed Keys rather than reach into each other. MEASURED before
this landed: **55 declared key types, ONE live emitter** — 13 `scene.contest_resolved` per seeded
campaign — while the real traffic ran over 16 direct Python imports. A transport with one call site
is a prototype, and nothing could tell the difference because nothing counted.

`systems/factions/sim/faction_action._emit_battle_concluded` is the second. It is deliberately
ADDITIVE: `sched.emit(key)` with no `apply=`, so the log grows and no state moves.

THE DISTINCTION THIS ENCODES, which is the reusable part: the obvious migration target was the
`faction_action -> massbattle` direct import that CLAUDE.md flags as a lane-boundary hack. That
would have been WRONG. `resolve_mass_battle()` is a RESOLVER INVOCATION — the caller needs
`attacker_wins` synchronously to decide the territory transfer — and Keys are deferred to the
accounting boundary. Replacing it with a Key breaks it. A request for a computed answer stays a
call; an announcement that something HAPPENED becomes a Key. Not every cross-subsystem import is a
Key candidate, and a migration that ignores the difference is cargo-culting.

WHAT THE EMISSION IMMEDIATELY FOUND, which is the argument for doing it at all: `world.battle_count`
increments INSIDE `if battle['attacker_wins']:` (faction_action.py:488), so the field named
"battle_count" counts attacker VICTORIES. Seed 42: **62 battles resolved, 29 reported.** The Key
fires on every battle regardless of outcome, so adding it produced a measurement the existing
telemetry did not have.
"""
import os
import sys
import collections

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

pytest.importorskip('yaml')
SEED = 42


@pytest.fixture(scope='module')
def campaign():
    """Run one seeded campaign under STRICT key validation, counting emissions by type.

    `VALORIA_STRICT_KEYS` matters: the emitter swallows exceptions so telemetry can never break a
    turn, and a swallowed exception is exactly where a broken payload would hide. Under the flag a
    `KeyValidationError` propagates, so a green run here is evidence the payload really validates
    against the registry — not evidence that nothing was checked.
    """
    from engine.substrate import keys as ks
    seen = collections.Counter()
    real = ks.TickScheduler.emit

    def spy(self, key, apply=None):
        seen[key.type] += 1
        return real(self, key, apply)

    ks.TickScheduler.emit = spy
    os.environ['VALORIA_STRICT_KEYS'] = '1'
    try:
        from engine import mc_v18
        result = mc_v18.run_campaign(seed=SEED)
    finally:
        ks.TickScheduler.emit = real
        os.environ.pop('VALORIA_STRICT_KEYS', None)
    return result, seen


def test_the_key_is_actually_emitted(campaign):
    """The load-bearing assertion: real traffic, not a declaration."""
    _result, seen = campaign
    assert seen['scene.battle_concluded'] > 0, (
        'scene.battle_concluded was never emitted — the substrate is back to one live type. '
        'Either the emit site was removed or no battle occurred on this seed.')


def test_payload_validates_under_strict_mode(campaign):
    """If the payload were malformed the fixture would have raised, not reached here.

    Stated explicitly because a test that merely *runs* a campaign and passes proves nothing about
    payload correctness; it is the strict flag in the fixture that makes this assertion mean
    something (CLAUDE.md §0.1 point 2 — an assertion must be able to observe the failure it
    excludes).
    """
    result, _seen = campaign
    assert result.keys_emitted > 0


def test_emission_is_additive_and_changes_no_outcome(campaign):
    """Byte-exact safety: the campaign lands where it landed before the emitter existed.

    Baseline captured on seed 42 immediately BEFORE the emit site was added: winner Crown, 50
    seasons, battle_count 29. `emit()` is called with no `apply=`, so there is no write path at
    all — this asserts the property the design relies on rather than trusting the argument.
    """
    result, _seen = campaign
    assert result.winner == 'Crown'
    assert result.season == 50
    assert result.battle_count == 29


def test_battle_count_undercounts_battles(campaign):
    """Pins the telemetry defect this emission exposed, so it cannot be silently 'fixed' either way.

    `world.battle_count += 1` lives inside `if battle['attacker_wins']:`, so it is a victory count
    wearing a battle count's name. If someone moves the increment out of the branch, the two numbers
    converge and this test fails — which is the correct prompt to rename the field or update this
    expectation deliberately, rather than letting a metric quietly change meaning.
    """
    result, seen = campaign
    battles = seen['scene.battle_concluded']
    assert battles > result.battle_count, (
        f'battles emitted ({battles}) should exceed battle_count ({result.battle_count}) — '
        f'battle_count only increments on attacker victories. If they now match, the increment '
        f'moved: rename the field or update this test on purpose.')
