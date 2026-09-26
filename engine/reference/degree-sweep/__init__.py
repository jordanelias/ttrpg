"""Frozen degree-sweep probes EXECUTED by the blocking engine/season/tests suite (the W-D
acceptance region, `test_season_shape.py`'s `_WD_SWEEP`). Moved out of
`proposals/2026-09-04-degree-sweep` so the blocking tier depends on no unratified tree
(precedent ED-IN-0231: `engine/reference/` holds frozen reference instruments beside the code
they validate). The measurement record (`runs/`, `README.md`, `EXECUTION_PLAN.md`, the other
arms) stays in the proposal: it is a record, not an instrument, and
`tools/ci_design_prose_quarantine.py` forbids `.md` here regardless.

The three modules bare-import each other (their frozen convention: `sweep_core.py` builds a
compatibility shim over `engine.season`'s owner modules; `arm9_forking.py`/`arm9_subj.py` do
`from sweep_core import S`). This package puts its own directory on `sys.path` so the
engine-wide dotted-import walk in `tests/valoria/test_engine_does_not_import_systems.py`
resolves them exactly as `test_season_shape.py` does.
"""
import os
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
if _HERE not in sys.path:
    sys.path.insert(0, _HERE)
