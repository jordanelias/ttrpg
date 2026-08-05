"""
Unit tests for `tools/build_fork.py`'s empty-scan guard (ED-IN-0126).

THE DEFECT THIS PINS. `--verify-only` skips `assemble()`, so pointed at a fresh `--out` the tree
never existed. `os.walk` on a nonexistent path yields nothing rather than raising, so the escape
scan printed

    [FORK] no path literal reaches an uncarried tree

over **zero files** — textually identical to the clean result — and the run then died at the
`FORK_MANIFEST.json` write with a bare `FileNotFoundError`. Both halves were wrong: a green line
that meant nothing, followed by an illegible failure. That is the gate-reporting-clean-over-nothing
class (#283/#284) reproduced inside the tool the fork plan names as its step 1, and the plan's own
§11-item-4 settling measurement — "`--verify-only` on a clean checkout" — could never have run.

WHY THESE TESTS AND NOT AN INTEGRATION TEST. `tests/valoria` is a BLOCKING CI job, so nothing here
may call `assemble()` (copies the tree) or `verify_runs()` (spawns a seeded campaign subprocess).
Every test below exercises the guard directly, or `main()` on a path that returns before either.

CLAUDE.md §0.1 point 2 — an assertion must be able to observe the failure it excludes — is why
`test_the_guard_itself_can_fail` exists: without it, a guard that raised unconditionally would make
every other test in this file pass while protecting nothing.
"""
import os
import sys

import pytest

HERE = os.path.dirname(__file__)
TOOLS = os.path.join(HERE, '..', '..', 'tools')
sys.path.insert(0, TOOLS)
import build_fork as bf  # noqa: E402


# --------------------------------------------------------------------------------------
# The guard itself
# --------------------------------------------------------------------------------------

def test_guard_rejects_a_missing_directory(tmp_path):
    """The exact --verify-only-on-a-fresh-dir case."""
    missing = tmp_path / "never-assembled"
    with pytest.raises(bf.EmptyScanError) as e:
        bf._scanned_py(str(missing))
    # The message must say what to do, not merely that something is wrong.
    assert "does not exist" in str(e.value)
    assert "--verify-only" in str(e.value)


def test_guard_rejects_a_directory_with_no_python(tmp_path):
    """An EXISTING but empty tree is the subtler half: it also scans vacuously clean."""
    (tmp_path / "docs").mkdir()
    (tmp_path / "docs" / "readme.md").write_text("prose, not code\n", encoding="utf-8")
    with pytest.raises(bf.EmptyScanError) as e:
        bf._scanned_py(str(tmp_path))
    assert "no .py files" in str(e.value)


def test_the_guard_itself_can_fail(tmp_path):
    """POSITIVE CONTROL (CLAUDE.md §0.1 point 2).

    A guard that raised unconditionally would satisfy every other test here while protecting
    nothing. Plant one real .py file and assert the guard PASSES and returns it. If this test ever
    fails, the guard has become unconditional and the rest of this file is vacuous.
    """
    pkg = tmp_path / "engine"
    pkg.mkdir()
    planted = pkg / "mc_v18.py"
    planted.write_text("X = 1\n", encoding="utf-8")
    (tmp_path / "notes.md").write_text("ignored\n", encoding="utf-8")

    found = bf._scanned_py(str(tmp_path))

    assert found == [str(planted)], "the guard must return exactly the .py files it saw"


def test_guard_ignores_pycache(tmp_path):
    """__pycache__ must not be able to satisfy the guard — it would make an empty tree pass."""
    cache = tmp_path / "__pycache__"
    cache.mkdir()
    (cache / "stale.py").write_text("X = 1\n", encoding="utf-8")
    with pytest.raises(bf.EmptyScanError):
        bf._scanned_py(str(tmp_path))


# --------------------------------------------------------------------------------------
# The scanners route through it — the guard is not merely available, it is on the path
# --------------------------------------------------------------------------------------

@pytest.mark.parametrize("scanner", ["escapes", "classify"])
def test_scanners_refuse_an_empty_tree(tmp_path, scanner):
    """Both scanners previously returned a clean empty result here."""
    with pytest.raises(bf.EmptyScanError):
        getattr(bf, scanner)(str(tmp_path / "never-assembled"))


# --------------------------------------------------------------------------------------
# main() — fails before printing anything green
# --------------------------------------------------------------------------------------

def test_verify_only_on_a_missing_tree_exits_nonzero(tmp_path, capsys):
    """Returns 2 and — the point of the fix — prints NO clean-scan line on the way out."""
    rc = bf.main(["--out", str(tmp_path / "never-assembled"), "--verify-only"])
    out = capsys.readouterr().out

    assert rc == 2, "a tree that cannot be scanned must not exit 0"
    assert "CANNOT VERIFY" in out
    # The regression this file exists for: these lines were printed over zero files.
    assert "no path literal reaches an uncarried tree" not in out
    assert "every contract unit" not in out
