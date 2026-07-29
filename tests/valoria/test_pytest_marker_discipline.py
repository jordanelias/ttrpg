"""Guard the `slow` marker against the one way it can go wrong: silently shrinking the gate.

WHY (2026-07-29). `pytest.ini` adds a `slow` marker so the inner loop can run
`-m "not slow"`. The marker itself is harmless. The DANGER is that someone later adds
`addopts = -m "not slow"` to `pytest.ini`, or slips a `-m` filter into the CI invocation —
at which point `python -m pytest tests/valoria -q` (the command
`.github/workflows/valoria-ci.yml`'s `unit-tests` job runs) quietly stops executing the
expensive guards, the shipping gate shrinks, and NOTHING reports it. The suite would go green
faster and mean less.

That is a coverage cut, and per CLAUDE.md §0.1 a coverage cut is Jordan's call made loudly,
never a side effect of a speed change. This file is the falsifier for that claim
(§0.1 point 3) and the guard that fails on recurrence (§0.1 point 5).

RED STATE, verified at authoring time: adding `addopts = -m "not slow"` to `pytest.ini` turns
`test_pytest_ini_declares_no_addopts` red; adding `-m "not slow"` to the workflow's pytest
invocation turns `test_ci_invocation_is_unfiltered` red. Neither is hypothetical — both are the
literal one-line edit that would cause the failure.
"""
import configparser
import os
import re
import subprocess
import sys

HERE = os.path.dirname(__file__)
REPO = os.path.abspath(os.path.join(HERE, "..", ".."))
PYTEST_INI = os.path.join(REPO, "pytest.ini")
WORKFLOW = os.path.join(REPO, ".github", "workflows", "valoria-ci.yml")


def _collect_count(*args):
    """Number of tests pytest collects under the given selector."""
    out = subprocess.run(
        [sys.executable, "-m", "pytest", "tests/valoria", "--collect-only", "-q", *args],
        cwd=REPO, capture_output=True, text=True,
    ).stdout
    # ORDER MATTERS. With a -m filter pytest prints "974/999 tests collected (25 deselected)";
    # the unfiltered pattern `(\d+) tests collected` matches the "999 tests collected" SUBSTRING of
    # that line, so testing it first reports the total for both partitions and the sum check below
    # silently passes 999+999 != 999 into a confusing failure. Match the N/M form first.
    m = re.search(r"(\d+)/(\d+)\s+tests? collected", out)
    if m:
        return int(m.group(1))
    m = re.search(r"(\d+)\s+tests? collected", out)
    assert m, f"could not parse collection count from:\n{out[-2000:]}"
    return int(m.group(1))


def test_pytest_ini_declares_no_addopts():
    """`addopts` must not exist. It is the one line that can silently shrink the shipping gate."""
    cp = configparser.ConfigParser()
    cp.read(PYTEST_INI)
    assert cp.has_section("pytest"), "pytest.ini lost its [pytest] section"
    assert not cp.has_option("pytest", "addopts"), (
        "pytest.ini declares `addopts`. If it carries a -m filter, `pytest tests/valoria -q` — "
        "the command CI runs — silently stops executing the expensive guards and the shipping "
        "gate shrinks with nothing reporting it. Removing coverage is a Jordan decision made "
        "loudly (CLAUDE.md §0.1), never a side effect of a speed change."
    )


def test_slow_marker_is_registered():
    """An unregistered marker is a typo waiting to happen — a misspelt mark silently marks nothing."""
    cp = configparser.ConfigParser()
    cp.read(PYTEST_INI)
    assert "slow:" in cp.get("pytest", "markers", fallback=""), \
        "the `slow` marker must stay registered in pytest.ini"


def test_ci_invocation_is_unfiltered():
    """CI's pytest command must carry no -m selector."""
    with open(WORKFLOW, encoding="utf-8") as fh:
        lines = fh.read().split("\n")
    invocations = [
        ln for ln in lines
        if "pytest" in ln and "tests/valoria" in ln and not ln.lstrip().startswith("#")
    ]
    assert invocations, "no live pytest invocation found in valoria-ci.yml — did the job move?"
    for ln in invocations:
        # Only a -m AFTER the `pytest` token is a marker filter. The `-m` in `python -m pytest` is
        # the interpreter's module flag; matching it would fire on every CORRECT invocation, which
        # is a guard that cries wolf rather than one that guards.
        tail = ln.split("pytest", 1)[1]
        assert not re.search(r"(?:^|\s)-m(?:\s|=)", tail), (
            f"CI's pytest invocation carries a -m marker filter, which cuts the shipping "
            f"gate:\n  {ln}"
        )


def test_marked_and_unmarked_partition_the_full_suite():
    """`slow` + `not slow` must sum to the whole collection.

    This is what makes marking incapable of dropping a test: if a mark is ever applied in a way
    that removes a test from BOTH partitions, the arithmetic breaks here rather than silently in
    the gate.
    """
    full = _collect_count()
    slow = _collect_count("-m", "slow")
    fast = _collect_count("-m", "not slow")
    assert slow + fast == full, (
        f"partition broken: {slow} slow + {fast} not-slow != {full} total. "
        "A test has escaped both partitions."
    )
    assert slow > 0, "no test carries @pytest.mark.slow — the marker is unreachable, so the "
    "fast lane is a no-op and this guard is decoration"
