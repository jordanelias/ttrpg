"""Shared runner for the three module-entry tests (`test_social_contest_module.py`,
`test_combat_module.py`, `test_mass_battle_module.py`): each asserts WHICH repository files an entry's
import loaded, which only a fresh interpreter can observe. Each test keeps its own probe script and its
own allowlist; this holds the two steps they share."""
from __future__ import annotations

import subprocess
import sys

from ..data import files
from ..manifest.registry import resolve
from engine.substrate import composition


def entry_target(prize: str) -> tuple:
    """`(role, target)` for the composition row the contest prize row `prize` names in `module_entry:`."""
    role = (resolve("contest", prize) or {}).get("module_entry")
    assert role, f"the prize row {prize!r} names no `module_entry:`; the entry this test is about is gone"
    return role, composition.ROLES[role]["target"]


def probe(script: str, target: str, timeout: int):
    """Run `script` (formatted with `root` and `target`) in a fresh interpreter at the repo root and
    return the `eval` of the last line it printed."""
    root = str(files.REPO_ROOT)
    proc = subprocess.run([sys.executable, "-c", script.format(root=root, target=target)],
                          capture_output=True, text=True, timeout=timeout, cwd=root)
    assert proc.returncode == 0, proc.stderr[-3000:]
    return eval(proc.stdout.strip().splitlines()[-1])     # our own probe's repr
