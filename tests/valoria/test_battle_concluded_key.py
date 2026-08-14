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
increments INSIDE `if battle['attacker_wins']:` (faction_action.py:509), so the field named
"battle_count" counts attacker VICTORIES. Seed 42: **76 battles resolved, 33 reported** (was
62/29 before the 2026-08-14 degree-ladder and strategic-dice ruling moved the campaign,
ED-IN-0187 — the UNDERCOUNT is the point here, and it survived the reband). The Key
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

from . import _campaign  # noqa: E402  the single owner of the seeded-campaign runner (CLAUDE.md §8)
SEED = 42


@pytest.fixture(scope='module')
def seeded_battle_campaign():
    """One seeded campaign under STRICT key validation, with emissions counted by type.

    The runner (tests/valoria/_campaign.py) owns the VALORIA_STRICT_KEYS handling and the
    create_world spy; both were duplicated here and in test_public_governance_transfer_key.py
    until the duplicated-helper ratchet caught the second copy.
    """
    result, _world, seen = _campaign.run(SEED)
    return result, seen


def test_the_key_is_actually_emitted(seeded_battle_campaign):
    """The load-bearing assertion: real traffic, not a declaration."""
    _result, seen = seeded_battle_campaign
    assert seen['scene.battle_concluded'] > 0, (
        'scene.battle_concluded was never emitted — the substrate is back to one live type. '
        'Either the emit site was removed or no battle occurred on this seed.')


def test_payload_validates_under_strict_mode(seeded_battle_campaign):
    """If the payload were malformed the fixture would have raised, not reached here.

    Stated explicitly because a test that merely *runs* a campaign and passes proves nothing about
    payload correctness; it is the strict flag in the fixture that makes this assertion mean
    something (CLAUDE.md §0.1 point 2 — an assertion must be able to observe the failure it
    excludes).
    """
    result, _seen = seeded_battle_campaign
    assert result.keys_emitted > 0


def test_emission_is_additive_and_changes_no_outcome(seeded_battle_campaign):
    """The emitter changes no outcome — asserted by SUPPRESSING it and comparing, not by pinning.

    ⚠ THIS TEST USED TO PIN ABSOLUTE CAMPAIGN VALUES (winner Crown, 50 seasons, battle_count 29),
    captured on seed 42 immediately before the emit site was added. That is a proxy for the claim,
    not the claim, and it fails whenever ANYTHING else in the campaign moves — which it did on
    2026-08-14, when Jordan's degree-ladder and strategic-dice ruling changed how faction actions
    resolve (ED-IN-0187). The pinned values then read as "the emitter broke something", which is
    precisely backwards: the emitter was the one thing that had not changed.

    So the claim is now tested directly. The campaign runs twice on the same seed, once with
    `_emit_battle_concluded` replaced by a no-op, and the two outcomes must be identical. This is
    immune to any future rebalancing — it can only fail if the emission actually writes state,
    which is the property the design relies on.
    """
    result, _seen = seeded_battle_campaign

    from systems.factions.sim import faction_action
    real = faction_action._emit_battle_concluded
    faction_action._emit_battle_concluded = lambda *a, **k: None
    try:
        silent, _world, silent_seen = _campaign.run(SEED)
    finally:
        faction_action._emit_battle_concluded = real

    assert silent_seen['scene.battle_concluded'] == 0, (
        'the suppression did not take — the control arm still emitted, so the comparison below '
        'would be one campaign against itself and could not fail (CLAUDE.md §0.1 point 2)')
    assert (silent.winner, silent.season, silent.battle_count) == \
           (result.winner, result.season, result.battle_count), (
        f'emitting scene.battle_concluded MOVED the campaign: '
        f'{(result.winner, result.season, result.battle_count)} with the emitter, '
        f'{(silent.winner, silent.season, silent.battle_count)} without it. The emission is '
        f'supposed to be additive (`emit()` with no `apply=`); if it now writes state, that is the '
        f'bug, not this test.')


def test_battle_count_undercounts_battles(seeded_battle_campaign):
    """Pins the telemetry defect this emission exposed, so it cannot be silently 'fixed' either way.

    `world.battle_count += 1` lives inside `if battle['attacker_wins']:`, so it is a victory count
    wearing a battle count's name. If someone moves the increment out of the branch, the two numbers
    converge and this test fails — which is the correct prompt to rename the field or update this
    expectation deliberately, rather than letting a metric quietly change meaning.
    """
    result, seen = seeded_battle_campaign
    battles = seen['scene.battle_concluded']
    assert battles > result.battle_count, (
        f'battles emitted ({battles}) should exceed battle_count ({result.battle_count}) — '
        f'battle_count only increments on attacker victories. If they now match, the increment '
        f'moved: rename the field or update this test on purpose.')
