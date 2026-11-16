"""engine.substrate — the engine's leaf readers.

Status: [live] — the package holds the single-owner leaves `engine/` resolves through:
`descriptors` (the axis and pursuit rosters, cooked from `references/descriptor_registry.yaml`),
`names` (cooked from `references/names_index.yaml`), `composition` (the role -> module registry),
`stubwire` and `pc_engine`.

⚠ THIS FILE HOLDS NO CODE, DELIBERATELY. The Key substrate is retired (ED-IN-0232, Jordan,
2026-09-16: *"anything key-based gets retired"*); build nothing on it.

Import the leaf you want: `from engine.substrate import descriptors`. Nothing is re-exported here,
deliberately — a package __init__ that re-exports makes `import engine.substrate.descriptors`
execute every re-exported leaf, an accidental dependency.
"""
