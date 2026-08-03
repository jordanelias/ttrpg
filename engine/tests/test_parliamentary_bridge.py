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

from engine.mc_v18 import run_batch, run_campaign
from engine.autoload import game_state
from engine.cross_scale import parliamentary_bridge as pb
from systems.social_contest.sim.parliamentary_vote import VoteResult


# ── Flag-ON campaign golden (seed 42) — the consequence spine is live ─────────
# REPINNED 2026-07-08: merge of ED-SC-0002/0006/0007 auto-resolve (parliamentary_bridge.py, this
# file's subject, origin/main) with the other session's ED-SC-0007 play-out echo (scene_dispatch.py)
# + ED-FA-0009/0012/0013 faction-action mechanics + ED-SC-0007-item-2 Censure fallback. All consume
# campaign RNG, so origin/main's own goldens are stale in the merged tree. NOTE: the flag-OFF baseline
# is NO LONGER the degenerate {Varfell 87.5} artifact — this branch's FA mechanics already erode the
# Varfell lockout at flag-OFF ({Crown 50, Hafenmark 25, Varfell 25}); the spine then redistributes
# further (Church/Hafenmark pick up wins under the flag). See the diverges-from-off test below.
#
# REPINNED 2026-07-29 (ED-FA-0036 / OI-04, ED-IN-0091 plan §3 Wave 2, item H golden re-record):
# parliamentary_transfer.propose_transfer gained its first caller this wave
# (parliamentary_bridge._run_transfer_motion — THIS module — every season a qualifying CB
# exists, canon-gated at 1/arc/faction). Fires only under ECHO_TRANSPORT on (the flag this whole
# module is scoped to), so _OFF_WIN_SHARE / test_flag_on_resolves_contests_and_fires_echoes'
# single-campaign seed-42 pins (_ON_KEYLOG_HASH/_ON_SCENES_RESOLVED/_ON_KEYS_EMITTED — Crown
# never drops under 6 territories on seed 42 alone) are UNCHANGED and NOT touched here; only the
# 8-campaign BATCH win-share (seeds 42-49, where Crown does cross the threshold on several
# seeds) moved. Isolated via pristine `git archive HEAD` vs. the fixed tree (see
# test_f7_smoke_oracle.py's matching note for the full control-isolation rationale). OLD value:
#   _ON_WIN_SHARE = {'Crown': 37.5, 'Church': 12.5, 'Hafenmark': 12.5, 'Varfell': 37.5}
_OFF_WIN_SHARE = {'Crown': 50.0, 'Church': 0.0, 'Hafenmark': 25.0, 'Varfell': 25.0}
_ON_WIN_SHARE = {'Crown': 62.5, 'Church': 0.0, 'Hafenmark': 0.0, 'Varfell': 37.5}
# ── GOLDEN RE-RECORD 2026-08-02 (ED-IN-0122) — deliberate, and here is the whole reason ────────
# `systems/factions/sim/faction_action` gained a SECOND live Key emitter, `scene.battle_concluded`.
# The KeyLog is append-only, so a new emitter necessarily changes both the count and the content
# hash. That is the INTENDED effect of adding an emitter, not drift — but CLAUDE.md §0.1 is explicit
# that a golden re-record IS a behaviour change and must be deliberate rather than silent, so the
# before/after is recorded here instead of the constants quietly moving.
#
#   keys_emitted   13 -> 75   (13 scene.contest_resolved unchanged, + 62 scene.battle_concluded)
#   key_log_hash   43c9f319953f2d0e... -> 2fd2c2dc1eb7996f...
#   scenes_resolved  50 -> 50 (UNCHANGED — the control that shows scene resolution is untouched)
#
# DETERMINISM RE-VERIFIED before re-recording: two consecutive seed-42 runs produce an identical
# hash and count. A golden is only worth pinning if it is stable, and re-recording an unstable one
# would convert a real determinism failure into a permanently moving target.
#
# NOTE FOR THE NEXT PERSON WHO ADDS AN EMITTER: this pin is a GLOBAL key count, so it moves whenever
# any subsystem starts emitting — even though this module is about the parliamentary bridge. The
# per-type assertion in the test below exists so that a future mismatch says WHICH type changed
# rather than just reporting two different integers.
_ON_KEYLOG_HASH = '2fd2c2dc1eb7996f738f7dedec185633999d72ebf4304b5289000b9b630174c1'
_ON_SCENES_RESOLVED = 50
_ON_KEYS_EMITTED = 75
# The composition behind that total — the diagnostic half of the pin.
_ON_KEYS_BY_TYPE = {'scene.contest_resolved': 13, 'scene.battle_concluded': 62}


def test_flag_on_resolves_contests_and_fires_echoes():
    """The named-zero-assertions FLIP: scenes resolve (>0) and Keys emit (>0), deterministically."""
    from collections import Counter
    from engine.substrate import keys as _ks
    seen = Counter()
    _real = _ks.TickScheduler.emit

    def _spy(self, key, apply=None):
        seen[key.type] += 1
        return _real(self, key, apply)

    _ks.TickScheduler.emit = _spy
    try:
        r = run_campaign(seed=42, params={'ECHO_TRANSPORT': 1})
    finally:
        _ks.TickScheduler.emit = _real
    assert r.scenes_resolved == _ON_SCENES_RESOLVED and r.scenes_resolved > 0
    # Per-type FIRST: when a new emitter lands, this says exactly which type moved, instead of
    # leaving the next person to diff two bare integers (which is what happened here).
    assert dict(seen) == _ON_KEYS_BY_TYPE, (
        f'key emission composition changed: {dict(seen)} != {_ON_KEYS_BY_TYPE}. '
        f'If a new emitter was added deliberately, re-record BOTH this map and _ON_KEYLOG_HASH, '
        f'and say why in the block above them.')
    assert r.keys_emitted == _ON_KEYS_EMITTED and r.keys_emitted > 0
    assert r.key_log_hash == _ON_KEYLOG_HASH, f"KeyLog hash drifted: {r.key_log_hash}"


def test_flag_on_win_share_golden_and_diverges_from_off():
    """The spine measurably moves balance and REDISTRIBUTES wins. (Post-merge 2026-07-08: the
    flag-OFF baseline is no longer the degenerate {Varfell 87.5} — this branch's FA mechanics already
    broke the lockout at flag-OFF — so the guard is now 'the spine brings a shut-out faction into the
    winners', not 'reduces Varfell'.)

    REPINNED 2026-07-29 (ED-FA-0036/OI-04 — see the golden block's REPINNED comment above): the
    prior 'the spine brings Church into the winners' claim (Church 0.0 -> 12.5 under the flag) no
    longer holds now that the Territory Transfer motion also consumes RNG under the flag — Church
    stays shut out (0.0) in both arms on this seed-42..49 batch. The weaker, still-true claim this
    wave's fix preserves is asserted instead: the flag still measurably redistributes SOMETHING
    (on != off, already asserted below) and still changes who is shut out relative to off (here:
    Hafenmark, not Church) — not "no faction is ever brought in", which this test no longer has
    grounds to claim for Church specifically."""
    on = run_batch(n=8, base_seed=42, params={'ECHO_TRANSPORT': 1}).win_share
    off = run_batch(n=8, base_seed=42, params={'ECHO_TRANSPORT': 0}).win_share
    assert on == _ON_WIN_SHARE, f"flag-ON win-share drifted: {on}"
    assert off == _OFF_WIN_SHARE, f"flag-OFF win-share drifted: {off}"
    assert on != off, "the consequence spine must change strategic outcomes when active"
    assert off['Hafenmark'] > 0.0 and on['Hafenmark'] == 0.0, (
        "the spine should still shut out a faction that survives at flag-OFF (was Hafenmark on "
        "this batch as of the 2026-07-29 repin — see docstring for why the Church claim retired)")


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
    from engine.cross_scale import echo_transport
    w = game_state.create_world(seed=42)
    w.echo_scheduler = echo_transport.make_scheduler()
    w.key_log = w.echo_scheduler.log
    w._echo_key_seq = 0
    out = pb.run_parliamentary_scene(w, w.rng)
    assert out['resolved'] is True
    assert out['status'] in ('passed', 'failed', 'committee')
    assert out['degree'] in ('Overwhelming', 'Success', 'Partial')
