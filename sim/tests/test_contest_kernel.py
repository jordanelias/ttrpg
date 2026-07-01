"""
sim/tests/test_contest_kernel.py — pytest gate for the promoted groundup contest kernel.

Stage 1b (designs/audit/2026-06-30-contest-stage0-reconciliation): the 9-module groundup
kernel was relocated into sim/personal/contest/ and unified onto the ONE canonical σ-kernel
(sim.autoload.sigma_leverage / dice_engine), replacing the groundup local engine.py. This
stage is BEHAVIOR-PRESERVING: the seeded 151-check kernel suite must stay green.

The kernel suite (sim/personal/contest/_kernel_tests.py) is the groundup tests.py verbatim
(random.seed(20260603), gates via sys.exit, prints "RESULT: 151 passed, 0 failed"). It runs
as a script, not a pytest module, so this wrapper executes it as a subprocess and asserts
both the exit code (0) and the "151 passed, 0 failed" line — the master parity guard for the
promotion + rewiring.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

import pytest

_REPO_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))


def _run_kernel_suite() -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, "-m", "sim.personal.contest._kernel_tests"],
        cwd=_REPO_ROOT,
        capture_output=True,
        text=True,
    )


def test_contest_kernel_151_green():
    """The promoted kernel suite runs green (151 passed, 0 failed) and gates exit 0."""
    proc = _run_kernel_suite()
    combined = proc.stdout + "\n" + proc.stderr
    m = re.search(r"RESULT:\s*(\d+)\s+passed,\s*(\d+)\s+failed", combined)
    assert m is not None, f"no RESULT line in kernel output:\n{combined}"
    passed, failed = int(m.group(1)), int(m.group(2))
    assert failed == 0, f"{failed} kernel checks failed:\n{combined}"
    assert passed == 151, f"expected 151 kernel checks, got {passed}:\n{combined}"
    assert proc.returncode == 0, f"kernel suite exited {proc.returncode}:\n{combined}"
