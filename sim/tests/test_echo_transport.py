"""
sim/tests/test_echo_transport.py — echo-transport plumbing oracle (ED-IN-0028, PR-2a)

Guards the flag-gated Key & Echo transport wired in this slice (key_echo_armature_v1.md §6.2):
  1. FLAG-OFF byte-exactness: ECHO_TRANSPORT off leaves the seed-42 F7 win-share golden and
     the seed-0-adjacent campaign untouched, and attaches no substrate (empty key_log_hash).
  2. FLAG-ON in the live loop is currently INERT: every scene still defers (the context-
     derivation bridge is SC-lane, ED-SC-0006/0007), so win-share is byte-identical to OFF
     and the campaign's KeyLog is born empty-but-deterministic (sha256 of "").
  3. The transport PATH itself (exercised directly, the way the SC bridge will drive it):
     a resolved scene carrying an `echo` block routes through domain_echo -> a valid
     scene.*_resolved Key -> an OF-7-deferred faction apply that lands at the accounting
     boundary. Deterministic on replay.

When the SC derivation bridge lands and scenes resolve, assertions (2) flip to feature
assertions (keys_emitted > 0, a non-empty log hash) — that tripping is the SUCCESS signal.
"""
import hashlib

import pytest

from sim.mc_v18 import run_batch, run_campaign
from sim.autoload import game_state
from sim.cross_scale import echo_transport


# The seed-42 n=8 F7 golden (test_f7_smoke_oracle.py) — the transport flag must not move it.
_GOLDEN_WIN_SHARE = {'Crown': 12.5, 'Church': 0.0, 'Hafenmark': 0.0, 'Varfell': 87.5}
_EMPTY_LOG_SHA256 = hashlib.sha256(b"").hexdigest()  # sha256("") — the born-empty KeyLog


# ── 1. Flag OFF: byte-exact, no substrate ────────────────────────────────────

def test_flag_off_is_byte_exact_and_attaches_no_substrate():
    """Default (flag off) matches the F7 golden and attaches no KeyLog."""
    off = run_batch(n=8, base_seed=42, params={'ECHO_TRANSPORT': 0})
    assert off.win_share == _GOLDEN_WIN_SHARE, f"OFF win-share drifted: {off.win_share}"
    r = run_campaign(seed=42, params={'ECHO_TRANSPORT': 0})
    assert r.key_log_hash == "" and r.keys_emitted == 0


# ── 2. Flag ON in the live loop: inert (all scenes defer), deterministic ──────

def test_flag_on_live_loop_is_inert_and_deterministic():
    """With ECHO_TRANSPORT on, the substrate is attached but nothing resolves yet
    (SC bridge pending), so win-share is unchanged and the KeyLog is empty-deterministic.
    These assertions FLIP to feature assertions when the derivation bridge lands."""
    on = run_batch(n=8, base_seed=42, params={'ECHO_TRANSPORT': 1})
    assert on.win_share == _GOLDEN_WIN_SHARE, (
        f"ON win-share moved ({on.win_share}) — the SC derivation bridge may have landed; "
        "echoes now fire in the live loop. Update this golden and say so in the commit.")
    r = run_campaign(seed=42, params={'ECHO_TRANSPORT': 1})
    assert r.keys_emitted == 0, (
        f"keys_emitted is no longer 0 ({r.keys_emitted}) — scenes resolve now; "
        "the transport path is live. Update the golden.")
    assert r.key_log_hash == _EMPTY_LOG_SHA256


def test_flag_on_off_win_share_identical():
    """Belt-and-suspenders: ON and OFF produce identical strategic outcomes while inert."""
    off = run_batch(n=8, base_seed=42, params={'ECHO_TRANSPORT': 0}).win_share
    on = run_batch(n=8, base_seed=42, params={'ECHO_TRANSPORT': 1}).win_share
    assert off == on


# ── 3. The transport path (driven directly, as the SC bridge will) ────────────

def _world_with_scheduler(seed=42):
    world = game_state.create_world(seed=seed)
    world.echo_scheduler = echo_transport.make_scheduler()
    world.key_log = world.echo_scheduler.log
    world._echo_key_seq = 0
    return world


def test_resolved_scene_with_echo_block_emits_valid_key():
    world = _world_with_scheduler()
    fid = next(iter(world.factions))
    ctx = {'echo': {'actor_faction': fid, 'target_faction': fid,
                    'most_relevant_stat': 'L', 'degree': 'Overwhelming'}}
    out = echo_transport.emit_scene_echo('contest', {'winner': 'A', 'total_victory': True}, ctx, world)
    assert out.get('other_echoes'), "an Overwhelming Domain Echo should fire"
    assert len(world.key_log) == 1
    k = world.key_log.lookup('scene.contest.s0.n0')
    assert k.type == 'scene.contest_resolved'
    assert k.targets[0].actor_id == fid and k.targets[0].stat_deltas == {'L': 2}
    assert set(k.payload) == {'scene_id', 'outcome', 'participants'}


def test_echo_apply_is_deferred_to_accounting_boundary():
    """OF-7: the faction stat is untouched until accounting_boundary() runs the applies."""
    world = _world_with_scheduler()
    fid = next(iter(world.factions))
    before = getattr(world.factions[fid], 'L')
    ctx = {'echo': {'actor_faction': fid, 'most_relevant_stat': 'L', 'degree': 'Overwhelming'}}
    echo_transport.emit_scene_echo('contest', {'total_victory': True}, ctx, world)
    assert getattr(world.factions[fid], 'L') == before, "apply must be deferred, not live"
    ran = world.echo_scheduler.accounting_boundary()
    assert ran == 1
    assert getattr(world.factions[fid], 'L') > before, "delta lands at the boundary"


def test_transport_path_is_deterministic_on_replay():
    ctx = {'echo': {'actor_faction': None, 'most_relevant_stat': 'L', 'degree': 'Overwhelming'}}
    hashes = []
    for _ in range(2):
        world = _world_with_scheduler()
        fid = next(iter(world.factions))
        c = {'echo': dict(ctx['echo'], actor_faction=fid, target_faction=fid)}
        echo_transport.emit_scene_echo('contest', {'total_victory': True}, c, world)
        hashes.append(world.key_log.content_hash())
    assert hashes[0] == hashes[1]


def test_no_echo_block_is_inert_fallback():
    """A resolved scene without an `echo` block emits nothing (the byte-exact fallback)."""
    world = _world_with_scheduler()
    out = echo_transport.emit_scene_echo('contest', {'total_victory': True}, {}, world)
    assert out == {} and len(world.key_log) == 0


def test_no_scheduler_is_inert():
    """With no scheduler attached (flag off), the bridge is a no-op even with an echo block."""
    world = game_state.create_world(seed=42)
    fid = next(iter(world.factions))
    ctx = {'echo': {'actor_faction': fid, 'most_relevant_stat': 'L', 'degree': 'Overwhelming'}}
    out = echo_transport.emit_scene_echo('contest', {'total_victory': True}, ctx, world)
    assert out == {}


def test_partial_degree_does_not_fire():
    """§5.2: Partial is narrative-only (delta 0) — no Key, no apply."""
    world = _world_with_scheduler()
    fid = next(iter(world.factions))
    ctx = {'echo': {'actor_faction': fid, 'most_relevant_stat': 'L', 'degree': 'Partial'}}
    out = echo_transport.emit_scene_echo('contest', {}, ctx, world)
    assert out == {} and len(world.key_log) == 0
