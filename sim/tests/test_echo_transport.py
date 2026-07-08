"""
sim/tests/test_echo_transport.py — echo-transport plumbing oracle (ED-IN-0028, PR-2a)

Guards the flag-gated Key & Echo TRANSPORT (ED-IN-0028, key_echo_armature_v1.md §6.2) at the
unit level, plus one live-loop smoke that the flag now fires end-to-end.

REPINNED / MERGED 2026-07-08 (two concurrent sessions): ECHO_TRANSPORT is now DEFAULT ON (Jordan:
"Yes echo transport on"). Two mechanisms emit under it — origin/main's faction-scale §10 Parliamentary
vote every season (sim/cross_scale/parliamentary_bridge.py) and this branch's personal-scale
emergency-council play-out echo (sim/cross_scale/scene_dispatch.py). The full flag-ON campaign golden
lives in test_parliamentary_bridge.py + test_f7_smoke_oracle.py; this file pins the flag-OFF byte-exact
oracle, one live-loop smoke, and the transport path in isolation.

  1. FLAG-OFF byte-exactness: ECHO_TRANSPORT off leaves the seed-42 F7 win-share golden untouched
     and attaches no substrate (empty key_log_hash).
  2. FLAG-ON live loop: for a seed that crosses Stability Crisis (seed=1) the campaign now emits real
     echo Keys through the composed-keying (ED-SC-0002) path — no longer architecturally inert
     (ED-SC-0006/0007). As of the merge the default-ON per-season Parliamentary vote also emits on
     essentially every seed.
  3. The transport PATH itself, exercised directly: a resolved scene carrying an `echo` block
     routes through domain_echo -> a valid scene.*_resolved Key -> an OF-7-deferred faction apply
     (in STAT POINTS via MULTS) that lands at the accounting boundary. Deterministic on replay.
"""
from sim.mc_v18 import run_batch, run_campaign
from sim.autoload import game_state
from sim.cross_scale import echo_transport


# The seed-42 n=8 F7 FLAG-OFF golden — the transport flag OFF must not move it. REPINNED 2026-07-08
# for the two-session merge: with the flag OFF, only this branch's FA-lane mechanics
# (ED-FA-0008/0011/0012) move seed-42 RNG — parliamentary_bridge and the play-out echo are inert.
# The flag-ON default is a DIFFERENT distribution now (test_f7_smoke_oracle.GOLDEN_WIN_SHARE).
_GOLDEN_WIN_SHARE = {'Crown': 50.0, 'Church': 0.0, 'Hafenmark': 25.0, 'Varfell': 25.0}


# ── 1. Flag OFF: byte-exact, no substrate ────────────────────────────────────

def test_flag_off_is_byte_exact_and_attaches_no_substrate():
    """Default (flag off) matches the F7 golden and attaches no KeyLog."""
    off = run_batch(n=8, base_seed=42, params={'ECHO_TRANSPORT': 0})
    assert off.win_share == _GOLDEN_WIN_SHARE, f"OFF win-share drifted: {off.win_share}"
    r = run_campaign(seed=42, params={'ECHO_TRANSPORT': 0})
    assert r.key_log_hash == "" and r.keys_emitted == 0


# ── 2. Flag ON: the live loop now fires (default ON) ─────────────────────────

def test_flag_on_live_loop_fires_for_a_seed_that_crosses_stability_crisis():
    """ED-SC-0006/0007 + the merged parliamentary_bridge: with ECHO_TRANSPORT on the campaign emits
    real echo Keys. seed=1 is the historically-motivated case (Stability Crisis fires and the
    Emergency Council contest resolves — test_mc_v18_regression.py); as of the merge the per-season
    §10 Parliamentary vote (parliamentary_bridge.py) ALSO emits every season, so the flag is live on
    essentially every seed. Flag OFF stays byte-exact (no substrate)."""
    off = run_campaign(seed=1, params={'ECHO_TRANSPORT': 0})
    assert off.keys_emitted == 0 and off.key_log_hash == ""
    on = run_campaign(seed=1, params={'ECHO_TRANSPORT': 1})
    assert on.keys_emitted > 0, "expected the consequence spine to emit at least one echo Key"
    assert on.key_log_hash != "" and on.key_log_hash != off.key_log_hash
    # NOT asserting win-share equality here: the deferred Mandate applies are now a real strategic-
    # state mutation — the intended effect of ED-SC-0007, not a regression to guard against.
    # Byte-exactness is guarded where it still holds: flag-OFF (above) and the flag-OFF F7 batch
    # (_GOLDEN_WIN_SHARE / test_flag_off_is_byte_exact_and_attaches_no_substrate).
    #
    # MERGE NOTE (2026-07-08): two prior HEAD tests here — test_flag_on_f7_batch_is_still_empirically_zero
    # and test_flag_on_off_win_share_identical — were DROPPED. Both asserted the flag is INERT (zero
    # keys at seed-42 / on==off win-share), which the merged default-ON parliamentary_bridge falsifies
    # (seed-42 flag-ON now emits 13 keys and the flag moves the batch win-share). The flag-ON campaign
    # golden is pinned in test_f7_smoke_oracle.py + test_parliamentary_bridge.py instead.


# ── 3. The transport path (driven directly, as the SC bridge drives it) ───────

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
