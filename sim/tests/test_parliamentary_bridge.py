"""
sim/tests/test_parliamentary_bridge.py — live-loop consequence-spine oracle
                                         (ED-SC-0006 / ED-SC-0007 / ED-SC-0002)

Pins the behaviour Jordan's rulings activated: with ECHO_TRANSPORT on, the campaign loop resolves
a canonical §10 Parliamentary vote each season (faction-scale, on aggregate state), applies the §10
loser Mandate penalty, and composes a WINNER Domain Echo (ED-SC-0002 COMPOSED keying: band gates
magnitude, genre selects stat/channel) through the substrate. This is the SUCCESS SIGNAL the F7
named-zero-assertions were built to trip: scenes now resolve and Keys now emit.

The flag-OFF path stays byte-exact (guarded in test_echo_transport.py + test_f7_smoke_oracle.py).
"""
from dataclasses import replace

from sim.mc_v18 import run_batch, run_campaign
from sim.autoload import game_state
from sim.cross_scale import parliamentary_bridge as pb
from sim.personal.parliamentary_vote import VoteResult


# ── Flag-ON campaign golden (seed 42) — the consequence spine is live ─────────
# REPINNED 2026-07-08: merge of ED-SC-0002/0006/0007 auto-resolve (parliamentary_bridge.py, this
# file's subject, origin/main) with the other session's ED-SC-0007 play-out echo (scene_dispatch.py)
# + ED-FA-0009/0012/0013 faction-action mechanics + ED-SC-0007-item-2 Censure fallback. All consume
# campaign RNG, so origin/main's own goldens are stale in the merged tree. NOTE: the flag-OFF baseline
# is NO LONGER the degenerate {Varfell 87.5} artifact — this branch's FA mechanics already erode the
# Varfell lockout at flag-OFF ({Crown 50, Hafenmark 25, Varfell 25}); the spine then redistributes
# further (Church/Hafenmark pick up wins under the flag). See the diverges-from-off test below.
_OFF_WIN_SHARE = {'Crown': 50.0, 'Church': 0.0, 'Hafenmark': 25.0, 'Varfell': 25.0}
_ON_WIN_SHARE = {'Crown': 37.5, 'Church': 12.5, 'Hafenmark': 12.5, 'Varfell': 37.5}
_ON_KEYLOG_HASH = '43c9f319953f2d0ed46e5f1c2dc198ea07f527b8bfb16b227fc8e5af89c42c9e'
_ON_SCENES_RESOLVED = 50
_ON_KEYS_EMITTED = 13


def test_flag_on_resolves_contests_and_fires_echoes():
    """The named-zero-assertions FLIP: scenes resolve (>0) and Keys emit (>0), deterministically."""
    r = run_campaign(seed=42, params={'ECHO_TRANSPORT': 1})
    assert r.scenes_resolved == _ON_SCENES_RESOLVED and r.scenes_resolved > 0
    assert r.keys_emitted == _ON_KEYS_EMITTED and r.keys_emitted > 0
    assert r.key_log_hash == _ON_KEYLOG_HASH, f"KeyLog hash drifted: {r.key_log_hash}"


def test_flag_on_win_share_golden_and_diverges_from_off():
    """The spine measurably moves balance and REDISTRIBUTES wins. (Post-merge 2026-07-08: the
    flag-OFF baseline is no longer the degenerate {Varfell 87.5} — this branch's FA mechanics already
    broke the lockout at flag-OFF — so the guard is now 'the spine brings a shut-out faction into the
    winners', not 'reduces Varfell'.)"""
    on = run_batch(n=8, base_seed=42, params={'ECHO_TRANSPORT': 1}).win_share
    off = run_batch(n=8, base_seed=42, params={'ECHO_TRANSPORT': 0}).win_share
    assert on == _ON_WIN_SHARE, f"flag-ON win-share drifted: {on}"
    assert off == _OFF_WIN_SHARE, f"flag-OFF win-share drifted: {off}"
    assert on != off, "the consequence spine must change strategic outcomes when active"
    assert off['Church'] == 0.0 and on['Church'] > 0.0, (
        "the spine should bring Church (shut out at flag-OFF) into the winners")


def test_flag_on_is_deterministic():
    a = run_campaign(seed=42, params={'ECHO_TRANSPORT': 1}).key_log_hash
    b = run_campaign(seed=42, params={'ECHO_TRANSPORT': 1}).key_log_hash
    assert a == b


# ── Bridge unit tests ────────────────────────────────────────────────────────

def test_derive_vote_picks_crisis_proposer_and_mandate_establishment():
    w = game_state.create_world(seed=42)
    motion, decls, proposer, establishment = pb._derive_vote(w)
    # proposer = lowest Stability; establishment = highest Mandate (L), different faction
    assert proposer == min((n for n in w.factions if w.factions[n].parliamentary and w.factions[n].territories),
                           key=lambda n: w.factions[n].Sta)
    assert establishment != proposer
    assert [(d.side, d.genre) for d in decls] == [('A', 'Projection'), ('B', 'Memory')]
    assert motion.primary_genre == 'Projection'


def test_composed_keying_genre_to_stat():
    """ED-SC-0002 composed: Memory→L (Mandate), Projection→I (outward channel)."""
    assert pb.COMPOSED_GENRE_STAT == {'Memory': 'L', 'Projection': 'I'}


def _vr(status, track, total=False):
    return VoteResult(status=status, final_track=track, total_victory=total)


def test_winner_and_degree_band_mapping():
    # band gates magnitude (Total→Overwhelming, Decisive→Success, Committee→Partial/no-echo)
    assert pb._winner_and_degree(_vr('passed', 10, total=True)) == ('A', 'Overwhelming')
    assert pb._winner_and_degree(_vr('failed', 1, total=True)) == ('B', 'Overwhelming')
    assert pb._winner_and_degree(_vr('passed', 8)) == ('A', 'Success')
    assert pb._winner_and_degree(_vr('failed', 2)) == ('B', 'Success')
    assert pb._winner_and_degree(_vr('committee', 5)) == (None, 'Partial')  # compromise fires nothing


def test_bridge_is_inert_without_scheduler():
    """No ECHO_TRANSPORT scheduler → the bridge is a no-op (byte-exact default)."""
    w = game_state.create_world(seed=42)
    assert pb.run_parliamentary_scene(w, w.rng) == {"resolved": False, "reason": "ECHO_TRANSPORT off"}


def test_bridge_resolves_and_may_echo_with_scheduler():
    from sim.cross_scale import echo_transport
    w = game_state.create_world(seed=42)
    w.echo_scheduler = echo_transport.make_scheduler()
    w.key_log = w.echo_scheduler.log
    w._echo_key_seq = 0
    out = pb.run_parliamentary_scene(w, w.rng)
    assert out['resolved'] is True
    assert out['status'] in ('passed', 'failed', 'committee')
    assert out['degree'] in ('Overwhelming', 'Success', 'Partial')
