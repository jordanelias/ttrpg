"""The third live Key emitter — `da.public_governance` on a Parliamentary Transfer (ED-IN-0123).

WHY THIS EXISTS. `references/wiring_manifest.yaml` records `save_replay_premise: violated`:
"the live strategic loop mutates World DIRECTLY (Faction.L, Territory.owner) with no Key trace,
so the Key log cannot reconstruct strategic state." The conversion strategy's Stage 1 specifies
`save = serialize-the-log` and its Stage 2 makes Key-log equality the master parity check, so
save, replay and Godot parity are one mechanism resting on that premise.

MEASURED 2026-08-03, and the note turned out to be mostly out of date. Reconstructing a seeded
campaign's final state from initial conditions + the Key log:

  * `Faction.L` rebuilds from `Target.stat_deltas` (echo_transport already carries them).
  * Territory conquest rebuilds from `scene.battle_concluded` (`victor` + `territorial_outcome`).
  * **7 of 8** ownership changes rebuilt. The miss was always the same one, and it was always a
    Parliamentary Transfer.

Attributed by instrumenting `Territory.__setattr__` across a seeded campaign rather than by
grepping for assignments — the grep would have missed it, because `Faction.adjust()` writes via
`setattr(self, stat, val)` and an AST scan for `Attribute` targets cannot see that. Owner writes
by module: `faction_action` 8, `parliamentary_transfer` 1, `mass_seizure` 0. **`mass_seizure` did
not fire on this seed — it is untested here, not proven clean.**

WHAT THIS TEST PINS, and what it deliberately does not:

The reconstruction test below is the falsifier for the fix. It rebuilds ownership from the log
alone and requires EVERY change to be recoverable, so deleting the emitter fails it.

It also records a coverage fact the suite would otherwise hide. `engine/tests/test_parliamentary_bridge.py`
pins the Key-log composition on **seed 42**, and seed 42 produces **zero** Parliamentary Transfers —
verified by counting emitter calls, not inferred. That golden therefore passed unchanged when this
emitter landed, which looks like "no regression" and is really "the golden cannot see this path".
The seed used here is chosen because it DOES exercise it.
"""
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

pytest.importorskip('yaml')

from . import _campaign  # noqa: E402  the single owner of the seeded-campaign runner (CLAUDE.md §8)

SEED = 20260803          # exercises Parliamentary Transfer; seed 42 does not
SEASONS = 24
GOLDEN_SEED = 42         # the seed engine/tests/test_parliamentary_bridge.py pins


def _rebuild_owners(initial, log):
    """Reconstruct Territory.owner from initial conditions + the Key log alone.

    Two rules, both keyed on REGISTERED payload fields:
      * scene.battle_concluded with territorial_outcome == 'transfer' -> owner := victor
      * da.public_governance with outcome == 'success' and a target_territory_id
        -> owner := faction_id
    """
    owners = dict(initial)
    for key in log:
        payload = getattr(key, 'payload', None) or {}
        if payload.get('territorial_outcome') == 'transfer' and payload.get('victor'):
            tid = next((t.actor_id for t in (key.targets or []) if t.role == 'subject'), None)
            if tid in owners:
                owners[tid] = payload['victor']
        elif (key.type == 'da.public_governance'
              and payload.get('outcome') == 'success'
              and payload.get('target_territory_id')
              and payload.get('faction_id')):
            tid = payload['target_territory_id']
            if tid in owners:
                owners[tid] = payload['faction_id']
    return owners


@pytest.fixture(scope='module')
def seeded_transfer_campaign():
    initial = _campaign.initial_owners(SEED)
    res, world, _seen = _campaign.run(SEED, seasons=SEASONS)
    return initial, res, world, list(getattr(world, 'key_log', []) or [])


def test_territory_ownership_reconstructs_from_the_key_log(seeded_transfer_campaign):
    """THE FALSIFIER for save_replay_premise on the Territory.owner half.

    Delete the emitter and this fails: before it landed, reconstruction scored 7/8 and the
    missing one was the Parliamentary Transfer.
    """
    initial, _res, world, log = seeded_transfer_campaign
    final = _campaign.owners_of(world)
    changed = [t for t in final if initial.get(t) != final[t]]
    assert changed, ("no territory changed hands in this campaign — the test proves nothing. "
                     "Pick a seed/horizon that exercises transfers.")
    rebuilt = _rebuild_owners(initial, log)
    missing = {t: (initial.get(t), final[t], rebuilt.get(t)) for t in changed
               if rebuilt.get(t) != final[t]}
    assert not missing, (
        f"{len(missing)} of {len(changed)} ownership changes are unreconstructable from the Key "
        f"log: {missing}. save = initial conditions + Key log is the strategy's Stage-1 premise.")


def test_the_transfer_emitter_actually_fired(seeded_transfer_campaign):
    """Anti-vacuity for the test above: if no da.public_governance key exists, the
    reconstruction passed on the battle rule alone and says nothing about this emitter."""
    _initial, _res, _world, log = seeded_transfer_campaign
    n = sum(1 for k in log if k.type == 'da.public_governance')
    assert n >= 1, "no da.public_governance key in the log — the transfer emitter never fired"


def test_emission_is_log_only(seeded_transfer_campaign):
    """The Key carries no `apply=`, so it must not move any state.

    Measured directly rather than asserted from the source: run the same seed with the emitter
    monkeypatched out and compare outcomes. Winner, Faction.L and Territory.owner must be
    identical; only the log length may differ.
    """
    _initial, res_on, world_on, log_on = seeded_transfer_campaign
    import systems.factions.sim.parliamentary_transfer as PT
    original = PT._emit_public_governance_transfer
    PT._emit_public_governance_transfer = lambda *a, **k: None
    try:
        res_off, world_off, _ = _campaign.run(SEED, seasons=SEASONS)
    finally:
        PT._emit_public_governance_transfer = original

    assert getattr(res_on, 'winner', None) == getattr(res_off, 'winner', None)
    assert ({n: f.L for n, f in world_on.factions.items()}
            == {n: f.L for n, f in world_off.factions.items()}), "emitter moved Faction.L"
    assert _campaign.owners_of(world_on) == _campaign.owners_of(world_off), "emitter moved Territory.owner"
    assert res_on.keys_emitted > res_off.keys_emitted, (
        "the log did not grow — the emitter is not firing, so 'log-only' is untested")


def test_the_pinned_golden_seed_cannot_see_this_path():
    """RECORDS A BLIND SPOT rather than asserting a behaviour.

    engine/tests/test_parliamentary_bridge.py pins the Key-log composition on seed 42. That
    golden stayed green when this emitter landed — not because nothing changed, but because seed
    42 produces zero Parliamentary Transfers. Left green-and-silent, that reads as coverage.
    If seed 42 ever DOES start transferring, this fails and the golden's composition map needs a
    da.public_governance row.
    """
    from engine import mc_v18
    import systems.factions.sim.parliamentary_transfer as PT
    calls = []
    original = PT._emit_public_governance_transfer

    def counting(*a, **k):
        calls.append(1)
        return original(*a, **k)

    PT._emit_public_governance_transfer = counting
    try:
        mc_v18.run_campaign(seed=GOLDEN_SEED, params={'ECHO_TRANSPORT': True})
    finally:
        PT._emit_public_governance_transfer = original
    assert not calls, (
        f"seed {GOLDEN_SEED} now fires the transfer emitter {len(calls)}x. "
        f"engine/tests/test_parliamentary_bridge.py's _ON_KEYS_BY_TYPE and _ON_KEYLOG_HASH must "
        f"be re-recorded to include da.public_governance.")
