"""Wires tests/sim/mass_battle/bat.py's byte-exact golden-digest gate (G5) into CI.

Before Stage A (2026-07-01), bat.py existed but nothing ever invoked it automatically — only
`tests/valoria` runs in CI (per CLAUDE.md), and bat.py was not among its tests. A future default-flip
of a toggle like FIELD_MOVEMENT would have gone unnoticed: bat.py's own `--check` would still fail
loud on a real digest mismatch, but nobody would ever run it to see the failure. This test closes that
gap for the two toggle-OFF (grid) modes, which are fast (well under a second each) and so safe to run
unconditionally as a blocking CI gate.

The FIELD_MOVEMENT=1 golden digests (bat.py EXPECTED['unit_field']/['cell_field']) are NOT checked
here — a full battery run under FIELD_MOVEMENT=1 takes ~80-110s per PER_CELL mode (nested float
distance checks are costlier than the grid's integer Chebyshev test), and this suite's CI job has a
5-minute overall budget shared with every other tests/valoria file. Run them manually instead:

    FIELD_MOVEMENT=1 PC_NODE_COHESION=1 PER_CELL=0 python3 tests/sim/mass_battle/bat.py --check
    FIELD_MOVEMENT=1 PC_NODE_COHESION=1 PER_CELL=1 python3 tests/sim/mass_battle/bat.py --check

Each mode is run as an isolated subprocess with an explicit, controlled environment (not the ambient
one) — bat.py's toggles are read at import time, so a clean env per mode is the only way to test both
in one process without cross-contamination.
"""
import os
import subprocess

REPO_ROOT = os.path.join(os.path.dirname(__file__), '..', '..')
BAT_PY = os.path.join(REPO_ROOT, 'tests', 'sim', 'mass_battle', 'bat.py')


# Every toggle this test needs pinned OFF, explicitly — inherit the rest of the ambient environment
# (a from-scratch minimal env, e.g. just PATH, was measured to make an UNRELATED, otherwise sub-second
# run take 20s+ -- some ambient var this process needs for unrelated reasons, e.g. HOME, was clearly
# load-bearing for performance; stripping it is not worth the risk). Explicit pins are what actually
# make this test mean anything: without them, an ambient FIELD_MOVEMENT=1 in the CI runner's own
# environment would silently make this "OFF-mode" check exercise the field path instead.
_PINNED_OFF = ('FIELD_MOVEMENT', 'PC_NODE_COHESION', 'FIELD_CONTACT', 'PC_FACING_MODEL', 'CONTACT_REACH')


def _run_bat(per_cell):
    """Run bat.py --check for one PER_CELL mode, toggles pinned OFF (see _PINNED_OFF), in a subprocess.

    Deliberately invokes 'python3' on PATH, NOT sys.executable — under some pytest install layouts
    (e.g. a uv tool-installed pytest running from its own isolated interpreter) sys.executable resolves
    to an interpreter/environment that is dramatically slower for this workload for unrelated reasons,
    timing out a check that completes in well under a second on the interpreter a human or CI would
    actually use to run bat.py (matching this repo's own documented invocation,
    `python3 tests/sim/mass_battle/bat.py`)."""
    env = dict(os.environ)
    for k in _PINNED_OFF:
        env.pop(k, None)
    env['PER_CELL'] = '1' if per_cell else '0'
    # The underlying compute() finishes in well under a second (confirmed by direct invocation); the
    # generous timeout absorbs nested-subprocess-spawn overhead observed in some sandboxed dev shells
    # (a python parent shelling out to a python child), not slowness in bat.py itself.
    return subprocess.run(['python3', BAT_PY, '--check'], cwd=REPO_ROOT, env=env,
                          capture_output=True, text=True, timeout=90)


def test_byte_exact_unit_mode():
    r = _run_bat(per_cell=False)
    assert '[BYTE-EXACT OK]' in r.stdout, f"unit-mode digest drifted:\n{r.stdout}\n{r.stderr}"


def test_byte_exact_cell_mode():
    r = _run_bat(per_cell=True)
    assert '[BYTE-EXACT OK]' in r.stdout, f"cell-mode digest drifted:\n{r.stdout}\n{r.stderr}"
