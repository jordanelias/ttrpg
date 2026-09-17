"""engine.substrate — the engine's leaf readers.

Status: [live] — the package holds the single-owner leaves `engine/` resolves through:
`descriptors` (the axis and conviction rosters, cooked from `references/descriptor_registry.yaml`),
`names` (cooked from `references/names_index.yaml`), `composition` (the role -> module registry),
`canon_buckets`, `stubwire` and `world_initial_state`.

⚠ THIS FILE USED TO BE NOTHING BUT A KEY RE-EXPORT, AND THAT IS WHY IT NOW HOLDS NO CODE.
Until 2026-09-16 it imported thirteen names from `engine/substrate/keys.py` and re-exported them,
with one consequence worth recording: `import engine.substrate.descriptors` executed this file, so
the Key substrate loaded on an import of ANY leaf here. `engine/season/` — the RULED head —
constructed zero Keys and still paid that import on every run. The substrate retired under
ED-IN-0232 (Jordan, 2026-09-16: *"anything key-based gets retired"*) and the re-export went with it.

Import the leaf you want: `from engine.substrate import descriptors`. Nothing is re-exported here,
deliberately — a package __init__ that re-exports is how that accidental dependency formed.
"""
