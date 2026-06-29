# Shim: expose the modular mass_battle engine as a flat namespace, so gauge_mb.py's
# `exec(open(argv[1]).read())` monolith model runs against the CURRENT modular engine.
# Mirrors mass_battle/engine.py's import order. Env toggles (PER_CELL etc.) must be set
# in the environment BEFORE this is imported (config reads them at import time).
from mass_battle.config import *        # noqa: F401,F403
from mass_battle.geometry import *      # noqa: F401,F403
from mass_battle.percell import *       # noqa: F401,F403
from mass_battle.resolution import *    # noqa: F401,F403
from mass_battle.orchestration import * # noqa: F401,F403
