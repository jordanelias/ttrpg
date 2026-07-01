"""
sim/tests/test_contest_kernel.py — pytest gate for the promoted groundup contest kernel.

Stage 1b (designs/audit/2026-06-30-contest-stage0-reconciliation): the 9-module groundup
kernel was relocated into sim/personal/contest/ and unified onto the ONE canonical σ-kernel
(sim.autoload.sigma_leverage / dice_engine), replacing the groundup local engine.py. This
stage is BEHAVIOR-PRESERVING: the seeded 151-check kernel suite must stay green.

The kernel suite (sim/personal/contest/_kernel_tests.py) is the groundup tests.py
(random.seed(20260603), gates via sys.exit, prints "RESULT: N passed, 0 failed"). It runs
as a script, not a pytest module, so this wrapper executes it as a subprocess and asserts
both the exit code (0) and the ">= 151 passed, 0 failed" line — the master parity guard for
the promotion + rewiring.

Stage 1c (2026-06-30): the v30 surface re-skin (8 canonical proceedings + 4 adjudicator types)
+ the build_contest/resolve_contest wrapper ADD checks on top of the behavior-preserved 151.
The 151 original checks stay verbatim and green; the count is now 222 (rev1: +5 judge-upheld
fixes — F1 odd-base halved-resistance round-up regression x2, F10 metadata-only/PARTIAL x2, and the
F4/F7 pinned-literal golden-trace assertion; rev2: +8 canon-boundary guard — the adjudicator
discipline/character profiles are LIVE but NON-canonical, so they are [SEED]-tagged and the re-skin
header no longer claims "NO number is invented", both source-enforced; rev3: +13 tracker tri-state —
social_contest_v30 §2:87 'no tracker' (Casual Dispute) vs :88-89 'tracker optional' (Private
Negotiation / Personal Appeal) is no longer flattened to a bare 'no tracker'; the optional state
DEFAULTS to TallyAtClose (behavior-preserving) and opts in via use_tracker=). The gate asserts the
count is AT LEAST 151 (the behavior-preserving floor) and exactly the current expected total.

Stage 1d (2026-07-01, Gate A): CR3 three-tracker model (RATIFIED_2026-06-01.md) — Concentration
(stamina) + Face (contest-local ethos) + Persuasion Track (merits, preserved); Composure RETIRED.
+12 checks assert the canonical CR3 names are wired over the existing groundup primitives
(Face=Standing, Concentration=Reserve) with NO behaviour change (all 222 above stay green) and that
Composure is absent as a kernel primitive. Subtotal 234.

Gate A closure (2026-07-01): the Face scale-binding resolution (ED-1056) — Face_max = Charisma x 3
(unchanged v30 ceiling formula), Face_current = round(Standing / 10 x Face_max) (Standing, unchanged,
sets position within that ceiling) — adds +10 checks covering FaceScale.face_max/face_current and the
_Side.face_max()/face_current() accessors, including the two boundary cases (Standing=0 -> 0,
Standing=Standing.HI -> Face_max), the pinned rounding rule, non-mutation of the underlying Standing,
and live tracking through an ethos-building move. Total 244.
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


# The behavior-preserving floor: the original groundup kernel had 151 checks; the Stage-1c
# re-skin + wrapper ADD checks on top. All 151 stay green — the count only grows.
_KERNEL_FLOOR = 151
_KERNEL_EXPECTED = 244   # 151 preserved + 45 Stage-1c re-skin/wrapper/golden-trace + 5 rev1 (F1/F10/F4-F7) + 8 rev2 canon-boundary guard + 13 rev3 tracker tri-state + 12 Stage-1d CR3 three-tracker model + 10 Gate-A Face scale-binding (ED-1056)


def test_contest_kernel_green():
    """The promoted kernel suite runs green (N passed, 0 failed), gates exit 0, and never drops
    below the behavior-preserving 151-check floor."""
    proc = _run_kernel_suite()
    combined = proc.stdout + "\n" + proc.stderr
    m = re.search(r"RESULT:\s*(\d+)\s+passed,\s*(\d+)\s+failed", combined)
    assert m is not None, f"no RESULT line in kernel output:\n{combined}"
    passed, failed = int(m.group(1)), int(m.group(2))
    assert failed == 0, f"{failed} kernel checks failed:\n{combined}"
    assert passed >= _KERNEL_FLOOR, (
        f"kernel check count {passed} dropped below the behavior-preserving floor "
        f"{_KERNEL_FLOOR} (the 151 groundup checks must all remain):\n{combined}")
    assert passed == _KERNEL_EXPECTED, (
        f"expected {_KERNEL_EXPECTED} kernel checks, got {passed}:\n{combined}")
    assert proc.returncode == 0, f"kernel suite exited {proc.returncode}:\n{combined}"
