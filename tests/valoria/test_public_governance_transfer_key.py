"""The third live Key emitter — `da.public_governance` on a Parliamentary Transfer (ED-IN-0123).

WHY THIS EXISTS. `references/module_contracts.yaml` records `save_replay_premise: violated`
under `foundation_gaps:` (it was `wiring_manifest.yaml`'s until plan S5c folded that file in):
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
import ast
import os
import sys

import pytest

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

pytest.importorskip('yaml')

from . import _campaign  # noqa: E402  the single owner of the seeded-campaign runner (CLAUDE.md §8)

# RE-SEEDED 2026-08-24 — the mass-battle engine was swapped (`systems/mass_battle/sim/` replaced by
# the 11,342-line engine ported from `tests/sim/mass_battle/`). A different resolution model draws a
# different number of RNG values per battle, so every downstream faction-action roll shifts and the
# set of seeds that qualify a Parliamentary Transfer motion is not preserved. 20260803 fired the
# emitter before the swap and fires it ZERO times after, which is a re-seed, not a regression: the
# path is still reachable. Measured over 14 seeds at 24 seasons, counting emitter CALLS rather than
# inferring from the log:
#
#   fires:      0 -> 1 · 99 -> 2 · 2024 -> 1 · 555 -> 1 · 777 -> 1
#   silent:     20260803, 42, 1, 7, 13, 123, 20260824, 1000, 31337
#
# 99 is chosen because it fires TWICE. A one-call seed proves reachability; a two-call seed also
# survives a single qualification flipping, which is the fragility that put this test here.
SEED = 99                # exercises Parliamentary Transfer twice; 20260803 no longer does
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


def _golden_keys_by_type():
    """Read `_ON_KEYS_BY_TYPE` out of the pinned golden by AST, not by import.

    Importing that module would execute a test file; parsing it reads the same literal without
    side effects, and it fails loudly if the constant is renamed rather than silently returning {}.
    """
    src = open(os.path.join(ROOT, 'engine', 'tests', 'test_parliamentary_bridge.py'),
               encoding='utf-8').read()
    tree = ast.parse(src)
    for node in tree.body:
        if (isinstance(node, ast.Assign) and len(node.targets) == 1
                and isinstance(node.targets[0], ast.Name)
                and node.targets[0].id == '_ON_KEYS_BY_TYPE'):
            return ast.literal_eval(node.value)
    raise AssertionError(
        "engine/tests/test_parliamentary_bridge.py no longer defines a module-level "
        "_ON_KEYS_BY_TYPE. This test polices what that map claims; if the map moved, point this at "
        "its new home rather than deleting the check.")


def test_the_golden_map_and_the_golden_seed_agree_about_this_emitter():
    """The map must claim this emitter's coverage IF AND ONLY IF the seed actually fires it.

    HISTORY, because this assertion has now flipped twice and the next session should not read a
    flip as a defect. It began (2026-08-03) RECORDING A BLIND SPOT: seed 42 produced zero
    Parliamentary Transfers, so `engine/tests/test_parliamentary_bridge.py`'s composition pin stayed
    green when this emitter landed — which looks like "no regression" and is really "the golden
    cannot see this path". Fractional dice pools (2026-08-21) shifted the RNG stream, seed 42 began
    firing it, and the assertion INVERTED to demand coverage; the map gained a
    `'da.public_governance': 1` row. The mass-battle engine swap (2026-08-24) shifted the stream
    again, seed 42 went back to zero, and the map's row was correctly dropped in the same commit.

    So it is re-stated as the INVARIANT the two flips were both instances of, instead of as
    whichever side happens to hold today. Either state is legitimate; a MISMATCH is not, and a
    mismatch in the dangerous direction — the map claiming a row the seed cannot produce — is the
    original "green over nothing" defect. Both directions fail here, so no future stream shift can
    leave this quietly wrong again.
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

    fired = len(calls)
    claimed = _golden_keys_by_type().get('da.public_governance', 0)
    assert fired == claimed, (
        f"seed {GOLDEN_SEED} fires the transfer emitter {fired} time(s), but "
        f"engine/tests/test_parliamentary_bridge.py's _ON_KEYS_BY_TYPE claims {claimed}. "
        + ("The map claims coverage it does not have — it is green over a path it cannot see. Drop "
           "the row and re-record the hash." if claimed > fired else
           "The seed now exercises a path the map does not pin — add the row and re-record the "
           "hash, or the golden will not observe this emitter changing.")
    )
