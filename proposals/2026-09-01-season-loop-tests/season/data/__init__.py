"""`season.data` — where the package's inputs are resolved.

THE ONE ENTRY. `files` is the single path anchor for the whole package (see `files.py`). `rosters`
and `matrix` are the loaders that read those paths, joined here in DEPENDENCY ORDER: `matrix`'s
loader shares `rosters.load_yaml` rather than owning a second duplicate-key-refusing YAML reader,
so `rosters` imports before `matrix`. Importing `season.data` once therefore loads every registry
this package owns, in the order each needs its predecessor. Nothing outside `data/` may import a
`data.*` module's private `_load_*` -- each module's own loader is called once, at its own import,
and its result is the public name (`rosters.roster`/`.table`, `matrix.MATRIX`) a caller reads.
"""

from . import files    # noqa: F401  -- the anchor, and its import-time self-check
from . import rosters  # noqa: F401  -- the roster/table layer, loaded from rosters.yaml
from . import matrix   # noqa: F401  -- the write matrix, loaded from write_matrix.yaml
