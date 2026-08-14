"""Wires tests/sim/mass_battle/bat.py's byte-exact golden-digest gate (G5) into CI.

Before Stage A (2026-07-01), bat.py existed but nothing ever invoked it automatically — only
`tests/valoria` runs in CI (per CLAUDE.md), and bat.py was not among its tests. A future default-flip
of a toggle like FIELD_MOVEMENT would have gone unnoticed: bat.py's own `--check` would still fail
loud on a real digest mismatch, but nobody would ever run it to see the failure. This test closes that
gap for the two toggle-OFF (grid) modes.

[2026-07-02 correction] The "well under a second" claim this docstring originally made was wrong —
confirmed wrong even at the commit that first hardcoded EXPECTED['unit']/['cell'] (12488dd7), i.e. it
predates every later mass-battle Stage A-D change and is not a regression from any of them. The battery
is 10 matchups x 24 seeds x up to 20 battle-turns of real engine work: 'unit' mode alone runs ~75-85s
end-to-end (subprocess spawn + compute) on ordinary dev hardware, and 'cell' mode (PER_CELL=1, finer
subunit-level granularity) runs noticeably longer than that — comfortably over the previous 90s
subprocess timeout, which is why both tests intermittently (or reliably, on slower boxes) failed with
subprocess.TimeoutExpired rather than a digest mismatch. See _run_bat's timeout for the corrected budget.

The FIELD_MOVEMENT=1 golden digests (bat.py EXPECTED['unit_field']/['cell_field']) are NOT checked
here — a full battery run under FIELD_MOVEMENT=1 takes ~80-110s per PER_CELL mode (nested float
distance checks are costlier than the grid's integer Chebyshev test), and this suite's CI job has a
5-minute overall budget shared with every other tests/valoria file. Run them manually instead — since
the ED-1089 default flip, a bare invocation IS the field path (the explicit env below is optional
belt-and-braces):

    PER_CELL=0 python3 tests/sim/mass_battle/bat.py --check
    PER_CELL=1 python3 tests/sim/mass_battle/bat.py --check

Each mode is run as an isolated subprocess with an explicit, controlled environment (not the ambient
one) — bat.py's toggles are read at import time, so a clean env per mode is the only way to test both
in one process without cross-contamination.

[2026-07-02] test_byte_exact_cell_mode hard-asserts only in the reference CI environment
(GITHUB_ACTIONS=='true', i.e. the ubuntu-latest/Python-3.11 runner valoria-ci.yml pins) and otherwise
skips (loudly, printing both digests) rather than silently passing OR permanently blocking local dev.
This is a REAL, narrow, non-portable engine bug, not test flakiness: bisected (throwaway PR #60, closed)
to the 'mirror' (Line-vs-Line, perfectly symmetric) battery entry, only 4/24 seeds (2, 5, 18, 23) --
confirmed present since the very first commit that hardcoded EXPECTED (12488dd7), so it is not a Stage
A-D regression. Turn 1 (18 ticks/3 phases) is BIT-IDENTICAL between a Windows/Python-3.14 dev box and
CI's Linux/Python-3.11; turn 2 onward diverges substantially and immediately -- not gradual ULP drift.
That signature (identical visible state, then a real behavioural fork) points to an RNG-stream desync:
some comparison unique to a perfectly-symmetric matchup lands on a platform/version-dependent tie,
consuming a different number of random() draws on one side without changing that turn's own numbers,
which then desyncs every later draw. orchestration.py:534-536 shows the author already hardened one
such symmetric-tie spot ("Use attacker CENTROID rather than nearest-cell to avoid non-determinism...");
this is most likely an unhardened sibling. Ruled out: `x**0.5` vs math.sqrt/hypot (patched locally,
digest didn't move) and PYTHONHASHSEED-driven set-ordering (repeated local runs are self-consistent).
Not yet found: the exact call site -- needs bisection inside turn 2's resolve_engagements_cascading /
find_contacts / assign_targets, most efficiently via more turn/tick-level DUMP instrumentation over
another throwaway CI branch (see the closed #60 for the harness pattern). Flagged as a follow-up, not
fixed here, since a real fix touches the canonical 'cell' golden digest -- Jordan-gated.
"""
import os
import platform
import subprocess
import sys

import pytest

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
BAT_PY = os.path.join(REPO_ROOT, 'tests', 'sim', 'mass_battle', 'bat.py')


# Every toggle this test needs pinned OFF, explicitly — inherit the rest of the ambient environment
# (a from-scratch minimal env, e.g. just PATH, was measured to make an UNRELATED, otherwise sub-second
# run take 20s+ -- some ambient var this process needs for unrelated reasons, e.g. HOME, was clearly
# load-bearing for performance; stripping it is not worth the risk). Explicit pins are what actually
# make this test mean anything: without them, an ambient FIELD_MOVEMENT=1 in the CI runner's own
# environment would silently make this "OFF-mode" check exercise the field path instead.
#
# [ED-1089, 2026-07-02] FIELD_MOVEMENT/PC_NODE_COHESION now DEFAULT ON (Jordan-ratified flip), so
# pinning OFF must SET each toggle's byte-exact-OFF value explicitly — the previous env.pop() approach
# would now leave the flipped ON default in force and silently run this grid-oracle check on the field
# path against grid digests (exactly the failure mode this test exists to prevent). CONTACT_REACH is a
# float env; its OFF value is '0.0'.
_PINNED_OFF = {'FIELD_MOVEMENT': '0', 'PC_NODE_COHESION': '0', 'FIELD_CONTACT': '0',
               'PC_FACING_MODEL': '0', 'CONTACT_REACH': '0.0',
               # [ED-MB-0018] PC_OCTAGON_DMG defaults ON and the grid goldens are recorded ON -- pin it
               # explicitly so an ambient PC_OCTAGON_DMG=0 can't silently check the ON golden against the
               # legacy path (same defense-in-depth as the other toggles here).
               'PC_OCTAGON_DMG': '1',
               # [ED-MB-0042, 2026-07-25] Pinned OFF because the DEFAULT is off — the flip to ON was
               # retracted the same day (its measurement was confounded; see config.py at the flag).
               # Pinned explicitly rather than left ambient so that when the flip is re-attempted, the
               # pin has to be changed deliberately and the goldens re-recorded with it.
               'PC_CELL_MORALE': '0',
               # [ED-MB-0045 A1b, 2026-07-29] Determinism pin, per the A1a critic pass. The digests
               # are empirically hash-order-independent (A1a's bisect ran every process with a fresh
               # random hash seed and all runs agreed, including reproducing goldens authored on a
               # different box) — pinned anyway so that can never silently stop being true.
               'PYTHONHASHSEED': '0'}


def _run_bat(per_cell, cell_morale=False):
    """Run bat.py --check for one PER_CELL mode, toggles pinned OFF (see _PINNED_OFF), in a subprocess.

    Deliberately invokes 'python3' on PATH, NOT sys.executable — under some pytest install layouts
    (e.g. a uv tool-installed pytest running from its own isolated interpreter) sys.executable resolves
    to an interpreter/environment that is dramatically slower for this workload for unrelated reasons
    (matching this repo's own documented invocation, `python3 tests/sim/mass_battle/bat.py`)."""
    env = dict(os.environ)
    env.update(_PINNED_OFF)
    env['PER_CELL'] = '1' if per_cell else '0'
    # [ED-MB-0053 / §4a] _PINNED_OFF pins PC_CELL_MORALE=0; the fifth mode overrides it deliberately.
    if cell_morale:
        env['PC_CELL_MORALE'] = '1'
    # compute() genuinely takes tens of seconds to ~2 minutes (10 matchups x 24 seeds x up to 20
    # battle-turns of real engine work; 'cell' mode's finer per-subunit granularity runs longest) --
    # this is NOT startup/spawn overhead, it is the battery itself. 300s gives real headroom above the
    # slowest observed run (~150s for 'cell' mode on ordinary dev hardware) without masking an actual
    # hang; a true infinite loop would still fail loud, just later.
    return subprocess.run(['python3', BAT_PY, '--check'], cwd=REPO_ROOT, env=env,
                          capture_output=True, text=True, timeout=300)


def _in_reference_env():
    """The exact environment the golden digests were authored/validated against: the ubuntu-latest +
    Python-3.11 runner valoria-ci.yml pins for every job. GITHUB_ACTIONS is GitHub's own always-'true'
    marker, so this is precise without hardcoding a runner image name that could drift independently of
    this file."""
    return os.environ.get('GITHUB_ACTIONS') == 'true' and platform.system() == 'Linux'


@pytest.mark.slow
def test_byte_exact_unit_mode():
    r = _run_bat(per_cell=False)
    assert '[BYTE-EXACT OK]' in r.stdout, f"unit-mode digest drifted:\n{r.stdout}\n{r.stderr}"


@pytest.mark.slow
def test_byte_exact_cell_mode():
    r = _run_bat(per_cell=True)
    if '[BYTE-EXACT OK]' in r.stdout:
        return
    if _in_reference_env():
        assert False, f"cell-mode digest drifted:\n{r.stdout}\n{r.stderr}"
    # Known non-portable divergence outside the reference env (see module docstring) -- skip loudly
    # rather than silently pass or permanently block local dev on a platform/version this gate was
    # never actually validated against.
    pytest.skip(
        "cell-mode digest doesn't match the golden value on this platform/Python version -- a known, "
        "narrow, pre-existing engine non-portability (not a regression), only verified byte-exact on "
        f"the reference CI environment (see module docstring). Got:\n{r.stdout}\n{r.stderr}")


# ── [ED-MB-0053 / plan v2 §4a] THE FIFTH DIGEST MODE — key guard only, by design ────────────────
#
# The fifth mode's actual `--check` runs in the DEDICATED golden job (tools/ci_golden_modes_check.py,
# CI job `golden-modes`), not here. Reason, stated because the first draft got it wrong: running it
# in this suite meant three more full batteries (~7 min locally, more on a hosted runner) inside a
# job already measured at ~9-11m43s against a 16-minute cap. That is how a suite acquires a
# mysterious cancellation instead of a finding. What belongs HERE is the part that is cheap and
# catches the actual trap: that the mode KEY discriminates the flag.

def test_mode_key_discriminates_every_digest_toggle():
    """The key must separate all three digest-selecting toggles, or a run checks the wrong golden.

    Until 2026-07-29 the key read only PER_CELL and FIELD_MOVEMENT, so a PC_CELL_MORALE=1 run
    reported 'cell' and compared itself against the flag-OFF golden — the ED-1089 shape, one flag
    later. This asserts the key is INJECTIVE over the toggle cube: eight configurations, eight
    distinct names. A weaker test (checking one example) would pass with any two toggles conflated.

    MUTATION: drop the `_cm` clause in bat._mode_key and this fails on the collision.
    """
    sys.path.insert(0, os.path.join(REPO_ROOT, 'tests', 'sim'))
    import mass_battle.bat as bat
    cube = {(pc, fm, cm): bat._mode_key(pc, fm, cm)
            for pc in (0, 1) for fm in (0, 1) for cm in (0, 1)}
    assert len(set(cube.values())) == 8, f"mode key is not injective over the toggles: {cube}"
    assert cube[(1, 0, 1)] == 'cell_legacy_mor1'
    assert cube[(1, 0, 0)] == 'cell_legacy_mor0'
    # ED-MB-0062: every axis must appear WITH ITS VALUE. Injectivity alone was already true
    # of the old suffix-on-true scheme and did not stop `cell` silently re-pointing when a
    # default flips — absence encoded "off" only relative to the default at recording time.
    for (pc, fm, cm), key in cube.items():
        assert key.startswith('cell_' if pc else 'unit_'), key
        assert ('_field_' if fm else '_legacy_') in key, key
        assert key.endswith('_mor1' if cm else '_mor0'), key
    # every recorded golden must be a key this function can actually produce
    for recorded in bat.EXPECTED:
        assert recorded in cube.values(), (
            f"EXPECTED holds {recorded!r}, which _mode_key can never emit — the table and the key "
            f"have drifted apart")
