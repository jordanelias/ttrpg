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
               'PC_FACING_MODEL': '0', 'CONTACT_REACH': '0.0'}


def _run_bat(per_cell):
    """Run bat.py --check for one PER_CELL mode, toggles pinned OFF (see _PINNED_OFF), in a subprocess.

    Deliberately invokes 'python3' on PATH, NOT sys.executable — under some pytest install layouts
    (e.g. a uv tool-installed pytest running from its own isolated interpreter) sys.executable resolves
    to an interpreter/environment that is dramatically slower for this workload for unrelated reasons
    (matching this repo's own documented invocation, `python3 tests/sim/mass_battle/bat.py`)."""
    env = dict(os.environ)
    env.update(_PINNED_OFF)
    env['PER_CELL'] = '1' if per_cell else '0'
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


def test_byte_exact_unit_mode():
    r = _run_bat(per_cell=False)
    assert '[BYTE-EXACT OK]' in r.stdout, f"unit-mode digest drifted:\n{r.stdout}\n{r.stderr}"


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
