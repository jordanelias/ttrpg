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
# REPINNED 2026-08-14 (ED-IN-0187 — Jordan's degree-ladder + strategic-dice ruling). Three ruled
# mechanisms move every seeded campaign at once: faction actions roll the continuous d10 through
# sigma_leverage instead of `d6, 4+` (different distribution AND different RNG draw count), the
# degree bands moved to the ruled margin ladder (Partial is now met-but-not-exceeded, so many former
# Partials are Failures), and `CONQUEST_MIN_MIL` was deleted (low-Military factions now reach the
# battle engine). The cause is a RULING, not drift; the deltas are published rather than buried
# (CLAUDE.md 0.1 point 4). OLD values, preserved:
#   _OFF_WIN_SHARE = {'Crown': 50.0, 'Church': 0.0, 'Hafenmark': 25.0, 'Varfell': 25.0}
#   _ON_WIN_SHARE  = {'Crown': 62.5, 'Church': 0.0, 'Hafenmark': 0.0, 'Varfell': 37.5}
# The ON/OFF arms still DIVERGE from each other, which is the property this file exists to pin —
# the spine changes outcomes. Both arms simply moved to new positions under the ruled dice.
_OFF_WIN_SHARE = {'Crown': 25.0, 'Church': 0.0, 'Hafenmark': 12.5, 'Varfell': 62.5}
# RE-PINNED 2026-08-21, M1 juncture 1: fractional dice pools (ED-IN-0187). `sigma_leverage.roll_net_continuous` no longer rounds its pool, so every sampled value changes and the RNG stream diverges. NOT a balance signal at this n — the control is `tools/balance_oracle.py` at 120 campaigns per arm, where no faction shifts significantly (all |z| < 0.53); see the RE-PINNED block in test_f7_smoke_oracle.py for the table.
# NOTE _OFF_WIN_SHARE did NOT move: the flag-OFF path does not reach a fractional pool on
# this batch, which is itself a useful signal about where fractional pools are produced.

# RE-PINNED 2026-08-22, plan S5d — ED-IN-0029's PER-STAT FLOORS. `Faction.adjust` now reads
# `descriptors.faction_bounds()` instead of a blanket 0.5/7.0, so Influence floors at 1 and
# Wealth/Military/Stability at 0. Unlike the 2026-07-29 re-record, this one moves BOTH the
# 8-campaign batch AND the single-campaign seed-42 pins, because the clamp is on the faction stats
# every path reads — 160 of 1,969 `.adjust()` calls now land differently over the 8-campaign batch.
# The full n=240-per-arm control table (two seed batches plus the pooled figures) is in
# test_f7_smoke_oracle.py's RE-PINNED block; read it before re-recording these again.
# PREVIOUS: _ON_WIN_SHARE = {'Crown': 50.0, 'Church': 12.5, 'Hafenmark': 0.0, 'Varfell': 37.5};
#   _ON_SCENES_RESOLVED = 125; _ON_KEYS_EMITTED = 186;
#   _ON_KEYS_BY_TYPE = {'scene.battle_concluded': 83, 'scene.contest_resolved': 89,
#                       'da.public_governance': 1};
#   _ON_KEYLOG_HASH = '1378f082210393c0a1a536f4d63d0fcdef5d6b9114753778131356cac8a52b73'
# ⚠ `da.public_governance` went 1 -> 2: the Parliamentary Transfer emitter fires TWICE on seed 42
# now. That is the emitter test_public_governance_transfer_key.py covers, and its count moving is
# expected here rather than a new emitter appearing — the composition map gains no new key type.
_ON_WIN_SHARE = {'Crown': 25.0, 'Church': 25.0, 'Hafenmark': 0.0, 'Varfell': 50.0}
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
# REPINNED 2026-08-14 (ED-IN-0187). The seed-42 single-campaign pins move for the same three ruled
# mechanisms as the batch shares above. The KeyLog hash necessarily changes with them: it is a
# content hash over an append-only log whose contents are the campaign. OLD values, preserved:
#   _ON_KEYLOG_HASH     = '2fd2c2dc1eb7996f738f7dedec185633999d72ebf4304b5289000b9b630174c1'
#   _ON_SCENES_RESOLVED = 50
#   _ON_KEYS_EMITTED    = 75
# ── RE-PINNED 2026-08-21 — fractional dice pools, AND A NEW KEY TYPE APPEARS ────────────────────
# `da.public_governance: 1` is now in the composition map, and that is the interesting part of this
# re-record rather than the shifted counts. `tests/valoria/test_public_governance_transfer_key.py`
# was written to pin that seed 42 fired the Parliamentary Transfer emitter ZERO times, and said in
# its own docstring: "If seed 42 ever DOES start transferring, this fails and the golden's
# composition map needs a da.public_governance row." It fired, it failed, and it named the remedy.
# That is a guard doing precisely its job, so the row is added rather than the guard relaxed.
#
# MECHANISM: fractional pools change every sampled value, so the RNG stream diverges and a transfer
# motion that previously missed its window now qualifies on this seed. Not a balance change — see
# the control table in test_f7_smoke_oracle.py (120 campaigns per arm, all |z| < 0.53).
_ON_KEYLOG_HASH = '1378f082210393c0a1a536f4d63d0fcdef5d6b9114753778131356cac8a52b73'
_ON_SCENES_RESOLVED = 125
_ON_KEYS_EMITTED = 186
# The composition behind that total — the diagnostic half of the pin.
_ON_KEYS_BY_TYPE = {'scene.battle_concluded': 80, 'scene.contest_resolved': 104, 'da.public_governance': 2}
# 2026-08-14 (ED-IN-0187): contest_resolved 13 -> 79 and battle_concluded 62 -> 76. The
# contest jump is the larger and has a mechanism worth naming — more faction actions now land
# in bands that open a scene, and the deleted Mil gate opens more conquests, so both emitters
# fire more often. No new emitter was added in this change.


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


def test_winner_and_degree_is_identical_to_the_threshold_derivation_it_replaced():
    """The falsifier for S5a's one behavioural-looking edit (§0.1 pts 2-3).

    `_winner_and_degree` used to import `PERSUASION_TOTAL_VICTORY` / `PERSUASION_TOTAL_DEFEAT` from
    `systems.social_contest` and re-derive, from the raw persuasion track, which side had won and
    whether totally — a classification `run_parliamentary_vote` had ALREADY made and recorded on
    the result it returned. S5a made it read `vr.status` + `vr.total_victory` instead, which is what
    removed the last of `engine/`'s three top-level `systems` imports.

    "Value-identical" is an argument, and an argument is not a measurement. This runs BOTH
    implementations over every reachable (status, total_victory, track) triple and asserts they
    never disagree. It reads the real canon constants rather than hardcoding 9/1/7/3, so if a
    retune ever inverts the ordering the new form depends on — TOTAL_VICTORY >= WIN_THRESHOLD and
    TOTAL_DEFEAT <= LOSS_THRESHOLD, i.e. "a total victory always also passes or fails" — this fails
    here rather than silently changing which faction gets a Domain Echo.
    """
    from systems.social_contest.sim.contest import (
        PERSUASION_TOTAL_VICTORY, PERSUASION_TOTAL_DEFEAT,
        PERSUASION_WIN_THRESHOLD, PERSUASION_LOSS_THRESHOLD,
    )

    def old(vr):
        """Verbatim the pre-S5a body."""
        if vr.total_victory and vr.final_track >= PERSUASION_TOTAL_VICTORY:
            return "A", "Overwhelming"
        if vr.total_victory and vr.final_track <= PERSUASION_TOTAL_DEFEAT:
            return "B", "Overwhelming"
        if vr.status == "passed":
            return "A", "Success"
        if vr.status == "failed":
            return "B", "Success"
        return None, "Partial"

    checked = 0
    # The track is clamped to [_TRACK_FLOOR, _TRACK_CEIL] = [0, 10] in parliamentary_vote.py; the
    # status and total_victory flags are derived from it there, so only these triples are reachable
    # by a real vote. The zero-zero early return is the extra case: committee + not-total at ANY
    # track, since it keeps the STARTING track rather than a computed one.
    for track in range(0, 11):
        if track >= PERSUASION_WIN_THRESHOLD:
            status = 'passed'
        elif track <= PERSUASION_LOSS_THRESHOLD:
            status = 'failed'
        else:
            status = 'committee'
        total = track >= PERSUASION_TOTAL_VICTORY or track <= PERSUASION_TOTAL_DEFEAT
        for reachable in ((status, total), ('committee', False)):   # normal, then zero-zero
            vr = _vr(reachable[0], track, total=reachable[1])
            assert pb._winner_and_degree(vr) == old(vr), (
                f'S5a changed behaviour at status={reachable[0]!r} track={track} '
                f'total_victory={reachable[1]}: now {pb._winner_and_degree(vr)}, was {old(vr)}'
            )
            checked += 1
    assert checked == 22, f'the sweep did not run over every reachable triple (checked {checked})'


def test_the_equivalence_sweep_can_observe_a_divergence():
    """§0.1 pt 2 — the sweep above must be able to FAIL. A comparison of a function against a copy
    of itself is not evidence; this plants the divergence the sweep is meant to catch and asserts
    the two forms really do differ there, so the sweep is comparing two distinct implementations.
    """
    from systems.social_contest.sim.contest import PERSUASION_TOTAL_VICTORY

    # A total victory that did NOT pass — unreachable under canon's ordering (9 >= 7), which is
    # precisely the assumption the new form rests on. The old threshold form calls it a Side-A
    # overwhelming win; the new status-reading form calls it a compromise.
    impossible = _vr('committee', PERSUASION_TOTAL_VICTORY, total=True)
    assert pb._winner_and_degree(impossible) == (None, 'Partial')
    assert impossible.total_victory and impossible.final_track >= PERSUASION_TOTAL_VICTORY, (
        'the planted triple no longer trips the OLD form, so the sweep proves nothing'
    )


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
