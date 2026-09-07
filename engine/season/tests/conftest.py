"""The season package uses BARE-NAME imports between its own modules (`import shape`,
`import probes`), a convention it carried in from the tracer and which `systems/combat/
combat_engine_v1/` also uses. The suite sits one level below them, so the package directory
goes on `sys.path` here rather than in 7,461 lines of test file — which keeps every
`test_season_shape.py:NNN` citation in `hole_register.yaml` pointing at the line it named.
"""
import sys
from pathlib import Path

_PKG = Path(__file__).resolve().parent.parent
if str(_PKG) not in sys.path:
    sys.path.insert(0, str(_PKG))
