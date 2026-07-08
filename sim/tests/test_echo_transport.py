"""
sim/tests/test_echo_transport.py — echo-transport plumbing oracle (ED-IN-0028, PR-2a)

Guards the flag-gated Key & Echo TRANSPORT (ED-IN-0028, key_echo_armature_v1.md §6.2) at the
unit level. The LIVE-LOOP behaviour (the campaign now resolves parliamentary votes and fires
echoes once ECHO_TRANSPORT is on — ED-SC-0006/0007) is pinned in test_parliamentary_bridge.py.

  1. FLAG-OFF byte-exactness: ECHO_TRANSPORT off leaves the seed-42 F7 win-share golden untouched
     and attaches no substrate (empty key_log_hash).
  2. The transport PATH itself, exercised directly: a resolved scene carrying an `echo` block
     routes through domain_echo -> a valid scene.*_resolved Key -> an OF-7-deferred faction apply
     (in STAT POINTS via MULTS) that lands at the accounting boundary. Deterministic on replay.
"""
from sim.mc_v18 import run_batch, run_campaign
from sim.autoload import game_state
from sim.cross_scale import echo_transport


# The seed-42 n=8 F7 golden (test_f7_smoke_oracle.py) — the transport flag OFF must not move it.
_GOLDEN_WIN_SHARE = {'Crown': 12.5, 'Church': 0.0, 'Hafenmark': 0.0, 'Varfell': 87.5}


# ── 1. Flag OFF: byte-exact, no substrate ────────────────────────────────────

def test_flag_off_is_byte_exact_and_attaches_no_substrate():
    """Default (flag off) matches the F7 golden and attaches no KeyLog."""
    off = run_batch(n=8, base_seed=42, params={'ECHO_TRANSPORT': 0})
    assert off.win_share == _GOLDEN_WIN_SHARE, f"OFF win-share drifted: {off.win_share}"
    r = run_campaign(seed=42, params={'ECHO_TRANSPORT': 0})
    assert r.key_log_hash == "" and r.keys_emitted == 0


# ── 2. The transport path (driven directly) ──────────────────────────────────

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
    # Overwhelming = +2 STAT POINTS (via MULTS), clamped to ceiling 7.0 — mirrors the §10 scale.
    assert getattr(world.factions[fid], 'L') == min(7.0, before + 2), "full band delta lands at the boundary"


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
