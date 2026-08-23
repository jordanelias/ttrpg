"""
F7 smoke oracle — the "born guarded" campaign regression (ED-IN-0021 / OPT-3).

WHY THIS EXISTS (unaddressed-areas audit U-4 / C-EMERGE)
-------------------------------------------------------
The "~87% win-share degeneracy" that five docs cited as a balance fact was a SMALL-N
ARTIFACT: it traces to a single un-guarded `run_batch(8, base_seed=42)` that propagated
unchallenged. The lesson the audit drew: *no balance claim without an oracle + n >= 100.*
This is the second pinned golden (`base_seed=42`), complementing the seed-0 golden in
`test_mc_v18_regression.py`. It exists to guard the CURRENT (pre-transport) state so that
when the Key/echo transport layer and the LPS-1 oracle land, the change is LOUD here rather
than silent.

WHAT IT PINS — and why each assertion is a *guard*, not a target
----------------------------------------------------------------
1. The n=8 seed-42 golden win-share {Crown 37.5, Church 12.5, Hafenmark 12.5, Varfell 37.5}.
   This is now the DEFAULT campaign with ECHO_TRANSPORT ratified ON (Jordan 2026-07-08) — the
   consequence spine is live (REPINNED 2026-07-08 for the merge of origin/main's parliamentary_bridge
   auto-resolve with this branch's FA-lane mechanics + play-out echo). Still small-n (NOT balance
   signal), but note the spine already ERODED the pre-spine {Varfell 87.5} artifact (retained under
   ECHO_TRANSPORT=0 in test_echo_transport.py). Do not tune to it.
2. scenes_resolved now FIRES (the spine is live — the named-zero flipped, the success signal
   the earlier revision predicted). insurgencies_formed / npcs_generated are STILL 0 — the
   insurgency pipeline and NPE remain built-but-unreachable islands (C-EMERGE-5/6) with no
   bridge yet; when they land these MUST become non-zero (the next success signal).
3. Hafenmark elimination lockout: the one-way 0-territory lockout MECHANISM is intact (0-territory
   factions never act again; the only restoration path, parliamentary_transfer, is never called).
   Hafenmark wins 1/8 here as a TRAJECTORY artifact of the merged RNG, not a comeback. KNOWN-TRACKED
   via ED-FA-0005 (comeback path ruled to be authored). Trips when a comeback path lands.
4. VICTORY_THRESHOLD dead-param regression: the param moves NO outcome (C-EMERGE-8 / C-FA-9).
   Trips when the victory threshold is actually wired to a live gate.
5. Wall-time ceiling: keeps the reference fast and non-degrading.

REGENERATING THE GOLDEN (only when a change is *intended* to move output)
-------------------------------------------------------------------------
    python -c "from engine.mc_v18 import run_batch; print(run_batch(n=8, base_seed=42).win_share)"
A surprise failure means simulation output moved — investigate BEFORE regenerating. If the
move is the transport layer / oracle finally reaching a subsystem, that is the intended win;
update the pins and note it.
"""
import os
import sys
import time

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if _REPO_ROOT not in sys.path:
    sys.path.insert(0, _REPO_ROOT)

from engine.mc_v18 import run_campaign, run_batch  # noqa: E402

_SEED = 42
_N = 8
_FACTIONS = ['Crown', 'Church', 'Hafenmark', 'Varfell']

# REPINNED 2026-07-08: merge of ED-SC-0002/0006/0007 auto-resolve (parliamentary_bridge.py,
# origin/main) with this branch's ED-SC-0007 play-out echo addition (scene_dispatch.py) +
# ED-FA-0009/0012/0013 faction-action mechanics + ED-SC-0007-item-2 Censure fallback — all of these
# consume campaign RNG, so goldens from either session alone are stale. This is the DEFAULT campaign
# with the consequence spine ON (ECHO_TRANSPORT ratified ON, Jordan 2026-07-08): the faction-scale §10
# vote (parliamentary_bridge, every season) + the personal emergency-council contest with its play-out
# echo (ED-SC-0006/0007 #96 + this branch). Still small-n (NOT balance signal) — a guard against silent
# drift, not a target. The pre-spine byte-exact oracle is retained under ECHO_TRANSPORT=0 in
# test_echo_transport.py. (deterministic; reproduced stable across repeat runs.)
#
# REPINNED 2026-07-29 (ED-FA-0036 / OI-04, ED-IN-0091 plan §3 Wave 2, item H golden re-record —
# orchestrator-adjudicated fix batch): `systems.factions.sim.parliamentary_transfer.propose_transfer`
# gained its first caller this wave (`engine.cross_scale.parliamentary_bridge._run_transfer_motion`,
# every season, independent of the §10 vote above) — a faction whose territories drop under 6 now
# attempts a CB-gated Territory Transfer (canon-gated at 1/arc/faction, §1.1), consuming extra
# `world.rng` draws whenever Crown qualifies. Isolated via a pristine `git archive HEAD` vs. this
# fixed-tree comparison (git HEAD predates this wave's session entirely, so the comparison covers
# both landing the motion AND this wave's frequency-gate refinement as ONE OI-04-attributed move,
# per the adjudicator's control-isolation instruction — not split into two separate re-records).
# OLD (pre-OI-04, pre-transfer-motion) values, preserved for the before/after record:
#   GOLDEN_WIN_SHARE  = {'Crown': 37.5, 'Church': 12.5, 'Hafenmark': 12.5, 'Varfell': 37.5}
#   GOLDEN_WINNERS    = {'Crown': 3, 'Church': 1, 'Hafenmark': 1, 'Varfell': 3}
#   GOLDEN_BATTLES_MEAN    = 30.2
#   GOLDEN_SCENES_RESOLVED = 383
# REPINNED 2026-08-14 (ED-IN-0187 — Jordan's degree-ladder + strategic-dice ruling). Three ruled
# mechanisms move every seeded campaign at once: faction actions roll the continuous d10 through
# sigma_leverage instead of `d6, 4+` (different distribution AND different RNG draw count), the
# degree bands moved to the ruled margin ladder (Partial is now met-but-not-exceeded, so many former
# Partials are Failures), and `CONQUEST_MIN_MIL` was deleted (low-Military factions now reach the
# battle engine). The cause is a RULING, not drift; the deltas are published rather than buried
# (CLAUDE.md 0.1 point 4). OLD values, preserved:
#   GOLDEN_WIN_SHARE       = {'Crown': 62.5, 'Church': 0.0, 'Hafenmark': 0.0, 'Varfell': 37.5}
#   GOLDEN_WINNERS         = {'Crown': 5, 'Varfell': 3}
#   GOLDEN_BATTLES_MEAN    = 35.5
#   GOLDEN_SCENES_RESOLVED = 463
# Note SCENES_RESOLVED nearly doubles (463 -> 862). That is the largest single delta here and it
# has a mechanism: more faction actions now resolve to a band that opens a scene, and the deleted
# Mil gate lets more conquests start. Recorded explicitly because 'the spine output moved,
# investigate before regenerating' is what this assertion says, and this IS the investigation.
# ── RE-PINNED 2026-08-21 — M1 juncture 1, fractional dice pools (ED-IN-0187) ────────────────────
# `sigma_leverage.roll_net_continuous` stopped rounding its pool: it did `max(1, int(round(pool)))`
# so a 3.5-die pool sampled as 4 dice, and Jordan's 2026-08-14 "fractional dice" ruling was only
# half-implemented. MEASURED before the change: a 4-season seeded campaign made 40 calls and 20
# already passed a fractional pool, every one silently rounded.
#
# WHY THESE NUMBERS MOVED, AND WHY THAT IS NOT A BALANCE SIGNAL. Every sampled value changes, so
# the RNG stream diverges and campaign outcomes reshuffle. At n=8 ONE campaign flipping is 12.5pp,
# so the deltas below carry no balance information whatsoever — which is exactly the gap line 8 of
# this file has been demanding an n>=100 oracle to close.
#
# THAT ORACLE WAS RUN BEFORE RE-RECORDING, and it is the control this re-pin rests on
# (`tools/balance_oracle.py`, 120 campaigns per arm, both arms in one process so the ONLY
# difference is the mechanic):
#
#     faction      rounded   fractional   delta pp        z
#     Church        10.8%       10.0%       -0.8       -0.21
#     Crown         36.7%       39.2%       +2.5       +0.40
#     Hafenmark      8.3%       10.0%       +1.7       +0.45
#     Varfell       44.2%       40.8%       -3.3       -0.52
#
# No faction shifts significantly (all |z| < 0.53 against a 1.96 threshold). So: the mechanic did
# what it was meant to and did NOT move balance measurably. Re-run `python3 tools/balance_oracle.py`
# before any future re-record — an uncontrolled re-pin is the second open gap CLAUDE.md §7 names.
#
# THE CONTROL IN THE OTHER DIRECTION: personal combat shares this entry point via
# `systems/combat/combat_engine_v1/core.py:56`. Measured 749 combat calls through
# `workbench.balance.winrate`, ALL INTEGRAL — so combat is value-identical and its byte-exact
# goldens did not move. They are what says this change touched only what it was aimed at.
# ══════════════════════════════════════════════════════════════════════════════════════════════
# RE-PINNED 2026-08-22, plan S5d — ED-IN-0029's PER-STAT FLOORS, AND THIS ONE MOVED BALANCE-ADJACENT
# OUTPUT, NOT ONLY THE RNG STREAM. Read this before re-recording again.
#
# WHAT CHANGED. `Faction.adjust` applied a blanket floor 0.5 / ceiling 7.0 to every faction stat.
# It now reads `descriptors.faction_bounds()`, so the floors ratified 2026-07-08 (ED-IN-0029,
# OPT-AV-14/D14 + OPT-AV-18) finally apply: Influence floors at 1, Wealth/Military/Stability at 0.
# `L` keeps 0.5/7.0 — the registry declares no bounds for it and Q1 is Jordan's open ruling.
#
# BLAST RADIUS, measured rather than assumed (§0.1 pt 4). Over these 8 seeded campaigns there are
# 1,969 `.adjust()` calls; 160 of them now clamp to a different value than before — 107 on Wealth
# and 53 on Stability, both of which gained room BELOW the old floor. Zero on Influence and zero on
# L at these seeds. So the change is real and it is concentrated in two stats.
#
# THE CONTROL, `tools/balance_oracle.py`, run at n=120 per arm TWICE before any golden was touched:
#
#   seed 20260819          blanket    per_stat   delta pp       z
#   Church                   10.0%      15.8%      +5.8     +1.35
#   Crown                    39.2%      43.3%      +4.2     +0.66
#   Hafenmark                10.0%       3.3%      -6.7     -2.07   SIGNIFICANT
#   Varfell                  40.8%      37.5%      -3.3     -0.53
#
#   seed 424242 (replication)
#   Church                   12.5%      10.0%      -2.5     -0.61
#   Crown                    45.0%      50.8%      +5.8     +0.90
#   Hafenmark                 9.2%       9.2%      +0.0     +0.00
#   Varfell                  33.3%      30.0%      -3.3     -0.56
#
#   POOLED, n=240 per arm (480 campaigns)
#   Church                   11.2%      12.9%      +1.7     +0.56
#   Crown                    42.1%      47.1%      +5.0     +1.10
#   Hafenmark                 9.6%       6.2%      -3.3     -1.35
#   Varfell                  37.1%      33.8%      -3.3     -0.76
#
# HOW TO READ THAT, honestly and in both directions (§0.1 pt 4 forbids asymmetric skepticism):
#   * The first batch flagged Hafenmark SIGNIFICANT. It did NOT replicate — the second batch shows
#     exactly zero effect on Hafenmark — and pooled over 480 campaigns nothing is significant. With
#     four comparisons per batch, one |z| just past 1.96 is close to the expected false-positive
#     rate; that is why it was replicated instead of banked.
#   * Do NOT therefore record "no balance effect". The pooled Crown +5.0pp and Hafenmark -3.3pp
#     point the same way in both batches. The control BOUNDS the effect; it does not exclude one.
#   * The statistic itself under-detects here: both arms run the same seeds (deliberately — that is
#     what makes the mechanic the only difference), and a two-proportion z assumes independence, so
#     it overstates the standard error on paired arms. The bias runs toward the null.
#
# `scenes_resolved` moved 858 -> 947 (+10.4%), which is an AGGREGATE, not a win-share. It is left
# unexplained rather than given a plausible story: the obvious candidate — more factions crossing
# the `Sta <= 2` Stability-Crisis trigger — is NOT the mechanism, because a faction clamped at the
# old 0.5 floor was already below 2 and already firing. What changed is what happens after: the
# emergency-council contest's own `faculty = round(7 - Faction.Sta)` sees 7 where it used to see 6,
# and Influence-derived pools floor at 1 rather than 0.5. Tracing which of those dominates was not
# done, and saying so is better than a confident guess in a golden block.
# ══════════════════════════════════════════════════════════════════════════════════════════════
# PREVIOUS (pre-S5d, verified against 62ce837 rather than retyped):
#   GOLDEN_WIN_SHARE = {'Crown': 50.0, 'Church': 12.5, 'Hafenmark': 0.0, 'Varfell': 37.5};
#   GOLDEN_WINNERS = {'Varfell': 3, 'Crown': 4, 'Church': 1};
#   GOLDEN_BATTLES_MEAN = 32.9; GOLDEN_SCENES_RESOLVED = 858
# ══════════════════════════════════════════════════════════════════════════════════════════════
# RE-PINNED 2026-08-23 — TWO JORDAN RULINGS ON THE FACTION-STAT ROSTER. Read before re-recording.
#
# WHAT CHANGED.
#   1. "Legitimacy is a base." `fac.legitimacy` is now declared in references/descriptor_registry.yaml
#      and bound to the `L` field, so `L` clamps from the REGISTRY (0-7). It previously fell back to
#      the blanket 0.5/7.0 because the registry declared nothing for it — the "5-vs-6" gap this
#      repository carried as `unimplemented.faction_L` for six weeks. That register is now EMPTY.
#   2. "Influence can be 0." Supersedes ED-IN-0029's Influence floor of 1 (OPT-AV-14/D14), which
#      plan S5d had wired ONE DAY EARLIER. All six faction stats floor at 0 and ceiling at 7.
#
# Jordan's rationale, recorded because it is what makes ruling 1 coherent rather than a reversal:
# "now that we're using continuous, we don't have to worry near as much either as we can just
# aggregate these stats as opposed to weird derivations."
#
# BLAST RADIUS, MEASURED (§0.1 pt 4), over these 8 seeded campaigns: 1,979 `.adjust()` calls, of
# which 605 now clamp to a different value. ALL 605 are on `L`. ZERO are on Influence — Influence
# never sinks below 1 at these seeds, so ruling 2 is DECLARED BUT INERT here. Saying "both rulings
# moved the goldens" would be false; ruling 1 moved them.
# ⚠ THE PER-STAT SPLIT, MEASURED rather than estimated (an earlier draft of this block said
# "roughly 1,277 L-adjustments", derived from the 20-of-31 call-SITE ratio; call sites are not
# executed uniformly, so it was replaced with a count):
#     L 1,235 · W 339 · Sta 182 · Mil 172 · I 51   (total 1,979)
# 605 of the 1,235 L-adjustments now clamp differently — 49% of them. `L` sat ON the old 0.5 floor
# for about half its writes and can now reach 0. That is a change in how Legitimacy behaves over a
# campaign, not a rounding nudge, and it is why the win-shares below moved as much as they did.
# ⚠ RULING 2's INERTNESS IS MEASURED ON BOTH ARMS, and the first version of this block was not.
# "Influence never sinks below 1 at these seeds" was originally established by a counterfactual on
# the RULED trajectory alone — but the arms provably diverge (the win-shares below move, and
# scenes_resolved 947 -> 967), so the pre-ruling campaign is a different campaign and a property of
# one says nothing about the other. That is the setup-vs-statistics gap §0.1's preamble was written
# about. Re-measured on each arm separately:
#     pre_ruling arm: 49 Influence adjustments, 0 with a raw value below 1
#     ruled arm:      51 Influence adjustments, 0 with a raw value below 1
# The call counts differ, which is the divergence being real; the floor is reached on NEITHER. So
# ruling 2 changes what the registry declares and changes no clamp that executes at these seeds —
# now as a two-arm measurement rather than an inference from the absence of a diff.
#
# THE CONTROL, tools/balance_oracle.py, run at n=120 per arm TWICE before any golden was touched.
# Arms patch `faction_bounds` back to its pre-ruling answers (I floors at 1, L undeclared), so both
# arms read ONE cooked artifact and the only difference is the answer `adjust` gets:
#
#   seed 20260819        pre_ruling     ruled   delta pp       z
#   Church                   15.8%     11.7%       -4.2   -0.94
#   Crown                    43.3%     38.3%       -5.0   -0.79
#   Hafenmark                 3.3%      7.5%       +4.2   +1.43
#   Varfell                  37.5%     42.5%       +5.0   +0.79
#
#   seed 424242 (replication)
#   Church                   10.0%      7.5%       -2.5   -0.69
#   Crown                    50.8%     47.5%       -3.3   -0.52
#   Hafenmark                 9.2%      9.2%       +0.0   +0.00
#   Varfell                  30.0%     35.8%       +5.8   +0.96
#
#   POOLED, n=240 per arm (480 campaigns)
#   Church                   12.9%      9.6%       -3.3   -1.16
#   Crown                    47.1%     42.9%       -4.2   -0.92
#   Hafenmark                 6.2%      8.3%       +2.1   +0.88
#   Varfell                  33.8%     39.2%       +5.4   +1.23
#
# HOW TO READ IT, in both directions (§0.1 pt 4 forbids asymmetric skepticism):
#   * Nothing is significant at |z| > 1.96, in either batch or pooled. Unlike the S5d measurement,
#     no batch flagged a false positive that then failed to replicate.
#   * That is NOT "no balance effect". Crown is down and Varfell is up in BOTH batches and pooled,
#     which is the pattern a real small effect makes; the control bounds it, it does not exclude it.
#   * The statistic UNDER-detects here: both arms run the same seeds by design (so the mechanic is
#     the only difference), while a two-proportion z assumes independence. The bias is toward the
#     null, which is the safe direction for a control and the unsafe one for concluding "no effect".
#
# `scenes_resolved` moved 947 -> 967. Left unexplained rather than given a story: the `Sta <= 2`
# crisis trigger is untouched by these rulings, and tracing which downstream path dominates was not
# done.
# ══════════════════════════════════════════════════════════════════════════════════════════════
# PREVIOUS (2026-08-22, per-stat floors — verified against 556449a rather than retyped):
#   GOLDEN_WIN_SHARE = {'Crown': 25.0, 'Church': 25.0, 'Hafenmark': 0.0, 'Varfell': 50.0};
#   GOLDEN_WINNERS = {'Varfell': 4, 'Church': 2, 'Crown': 2};
#   GOLDEN_BATTLES_MEAN = 32.6; GOLDEN_SCENES_RESOLVED = 947
#
# ⚠ BOTH "PREVIOUS" BLOCKS IN THIS FILE WERE WRONG UNTIL 2026-08-23, IN A WAY NO TEST CAN SEE.
# Each re-record copied the LIVE winners/battles values into the PREVIOUS line instead of reading
# the superseded ones, so the historical record was internally impossible: `_win_share` derives
# share from wins over n=8, and {Varfell 3, Church 2, Crown 3} yields {37.5, 25.0, 0.0, 37.5}, not
# the {25.0, 25.0, 0.0, 50.0} recorded beside it. A golden test pins the LIVE constants; nothing
# pins the prose, so a fabricated history stays green forever and the next re-recorder reasons from
# it. Restored from git. Rule: a PREVIOUS line is read out of `git show <ref>:<file>`, never
# copied from the constant you are about to overwrite.
GOLDEN_WIN_SHARE = {'Crown': 37.5, 'Church': 25.0, 'Hafenmark': 0.0, 'Varfell': 37.5}
# GOLDEN_WINNERS mirrors _win_share's raw `wins` dict shape: only factions with >=1 win get a key.
# ⚠ The sentence here used to say "Church/Hafenmark win 0/8 now". That was true of the PREVIOUS
# pin and false of this one — under the 2026-08-14 reband Church wins 2 of 8 and Hafenmark 0, so
# Hafenmark alone is absent. Corrected rather than left: a comment explaining the shape of numbers
# it no longer describes is how the next re-record gets reasoned about wrongly.
GOLDEN_WINNERS = {'Varfell': 3, 'Church': 2, 'Crown': 3}
GOLDEN_BATTLES_MEAN = 30.1
GOLDEN_SCENES_RESOLVED = 967  # 862 -> 858 (fractional pools, 08-21) -> 947 (per-stat floors, 08-22) -> 967 (roster rulings, 08-23)
WALL_TIME_CEILING_S = 90.0  # n=8 runs ~16s; generous headroom for CI variance

_CACHE = {}


def _campaigns42():
    """Run the 8 seed-42 campaigns once; cache for reuse across assertions."""
    if 'c' not in _CACHE:
        t0 = time.time()
        _CACHE['c'] = [run_campaign(seed=_SEED + i) for i in range(_N)]
        _CACHE['wall'] = time.time() - t0
    return _CACHE['c']


def _win_share(campaigns):
    wins = {}
    for r in campaigns:
        if r.winner:
            wins[r.winner] = wins.get(r.winner, 0) + 1
    total = sum(wins.values()) or 1
    return {fn: round(wins.get(fn, 0) / total * 100, 1) for fn in _FACTIONS}, wins


def test_f7_determinism():
    """Same seed -> identical output. A non-deterministic reference cannot be an oracle."""
    a = run_batch(n=2, base_seed=_SEED)
    b = run_batch(n=2, base_seed=_SEED)
    assert a.win_share == b.win_share
    assert a.all_winners == b.all_winners
    assert a.battles_mean == b.battles_mean


def test_f7_golden_win_share():
    """The n=8 seed-42 artifact, pinned. NOT balance signal — a guard against silent drift."""
    share, winners = _win_share(_campaigns42())
    assert share == GOLDEN_WIN_SHARE, f"win_share drifted: {share}"
    assert winners == GOLDEN_WINNERS, f"winners drifted: {winners}"
    b = run_batch(n=_N, base_seed=_SEED)
    assert b.battles_mean == GOLDEN_BATTLES_MEAN, f"battles_mean drifted: {b.battles_mean}"


def test_f7_scenes_live_insurgency_and_npe_still_islands():
    """The consequence spine is LIVE: scenes_resolved now FIRES.

    REPINNED 2026-07-08 (merge of both sessions): scenes_resolved is no longer 0 on seed-42. The
    faction-scale §10 Parliamentary vote (parliamentary_bridge, origin/main) resolves EVERY season,
    and the personal-scale Emergency Council contest resolves when the FA-lane action-mix/Muster/
    conquest-fork/Parliamentary changes (this branch) shift seed-42 RNG across Stability Crisis
    (383 scenes across the n=8 batch). Pinned here as the new golden — NOT re-asserted to 0.
    insurgencies_formed and npcs_generated remain built-but-unreachable islands (C-EMERGE-4/5),
    still guarded at 0; when the insurgency pipeline / NPE seeding land, those pins trip next and
    get updated the same way.
    """
    campaigns = _campaigns42()
    scenes = sum(r.scenes_resolved for r in campaigns)
    insurgencies = sum(r.insurgencies_formed for r in campaigns)
    npcs = sum(r.npcs_generated for r in campaigns)
    assert scenes == GOLDEN_SCENES_RESOLVED, f"scenes_resolved drifted ({scenes} vs {GOLDEN_SCENES_RESOLVED}) — the spine output moved; investigate before regenerating"
    assert insurgencies == 0, f"insurgencies_formed is no longer 0 ({insurgencies}) — the insurgency pipeline may be reachable; update the golden"
    assert npcs == 0, f"npcs_generated is no longer 0 ({npcs}) — generate_npc may have live call sites; update the golden"


def test_f7_hafenmark_elimination_lockout():
    """Hafenmark wins 0/8 on seed-42 (REPINNED 2026-07-29, ED-FA-0036/OI-04 — see the golden
    block's REPINNED comment above).

    CORRECTED CLAIM (the prior docstring's premise went stale, not just its number):
    `parliamentary_transfer.propose_transfer` is NO LONGER "never called" — OI-04 wired it into
    `parliamentary_bridge._run_transfer_motion`, attempted every season a qualifying CB exists.
    But the ONLY auto-populated CB is `crown_constitutional_restoration` (Crown < 6 territories,
    parliamentary_transfer.py §3) — this is CROWN's OWN restoration path, not a mechanism that
    targets a 0-territory faction for rescue. ED-FA-0005 (a dedicated comeback path FOR an
    eliminated faction) is therefore STILL open; the one-way 0-territory lockout MECHANISM
    itself (0-territory factions never act again) is untouched by this wave. Verified directly
    (2026-07-29, monkey-patched `propose_transfer` across the seed-42..49 batch): Crown's
    restoration motion fires 0-10 times per campaign depending on seed, and its [SEED]
    largest-non-Crown-holder targeting (parliamentary_transfer.derive_transfer_candidate, moved
    out of parliamentary_bridge at plan S5a) sometimes selects
    Hafenmark as the target holder (e.g. seed 49: `('Crown', 'T10', 'Hafenmark', 'transferred')`)
    — Crown reclaiming territory FROM Hafenmark, working against Hafenmark's trajectory rather
    than for it, on top of the general RNG-stream shift from every attempt (success or failure)
    consuming `world.rng`. Hafenmark's 0/8 here is therefore still a TRAJECTORY artifact of the
    (now further-)shifted RNG, not evidence one way or the other about ED-FA-0005. Pinned as the
    new golden; a move here again means the RNG shifted further — investigate before
    regenerating."""
    campaigns = _campaigns42()
    hafenmark_wins = sum(1 for r in campaigns if r.winner == 'Hafenmark')
    assert hafenmark_wins == 0, f"Hafenmark won {hafenmark_wins} != 0 — trajectory moved (or an ED-FA-0005 comeback path landed); investigate before regenerating"


def test_f7_victory_threshold_is_a_dead_param():
    """VICTORY_THRESHOLD moves no outcome (C-EMERGE-8 / C-FA-9). Trips when wired to a live gate."""
    base = run_batch(n=3, base_seed=_SEED, params={'VICTORY_THRESHOLD': 11}).win_share
    hi = run_batch(n=3, base_seed=_SEED, params={'VICTORY_THRESHOLD': 999}).win_share
    lo = run_batch(n=3, base_seed=_SEED, params={'VICTORY_THRESHOLD': 1}).win_share
    assert base == hi == lo, (
        f"VICTORY_THRESHOLD now moves outcomes (11->{base}, 999->{hi}, 1->{lo}) — "
        "the dead param may have been wired to a live victory gate; update this test"
    )


def test_f7_wall_time_ceiling():
    """The reference stays fast; guards against an accidental complexity blow-up."""
    _campaigns42()  # populates _CACHE['wall']
    assert _CACHE['wall'] < WALL_TIME_CEILING_S, (
        f"the {_N}-campaign seed-42 batch took {_CACHE['wall']:.1f}s "
        f"(> {WALL_TIME_CEILING_S}s ceiling)"
    )
