"""`engine.season.tests` — the instrument's own adversarial test suite.

⚠ THIS FILE IS LOAD-BEARING AND IS NOT AN EMPTY PACKAGE MARKER. Without it pytest imports
`test_season_shape.py` as a TOP-LEVEL module and inserts `engine/season/tests/` on `sys.path`, so
every relative import in it (`from ..data import files`, `from ..harness import probes`) raises
`ImportError: attempted relative import with no known parent package`. With it, pytest walks up
through `tests/` -> `season/` -> `engine/`, all of which carry an `__init__.py`, stops at the
repository root, and imports the suite as `engine.season.tests.test_season_shape` — which is also
the name the engine import probe reaches it under.
"""
