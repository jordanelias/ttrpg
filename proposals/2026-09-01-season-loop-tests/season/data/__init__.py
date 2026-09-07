"""`season.data` — where the package's inputs are resolved.

`files` is the single path anchor for the whole package; the loaders that read those paths (the
rosters, the verb table, the write matrix) join it here in a later step.
"""

from . import files  # noqa: F401  -- the anchor, and its import-time self-check
