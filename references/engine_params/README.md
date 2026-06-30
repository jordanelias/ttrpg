# `references/engine_params/` — typed engine parameters (ED-1052)

## Status: CURRENT

The **typed, Godot-ingestible** layer for Valoria's mechanical numbers. Each `*.json` here holds
numeric operands, structured formulas (operator expression + declared inputs), and explicit clamps —
the form a Godot 4.6 importer can load directly, which the prose `params/*.md` tables (unicode `×`,
en-dashes, parenthetical caveats) are not.

This is the **ingestion source for the values it covers**. The prose `params/*.md` heads remain the
human canon; these files are derived from them and held honest by a CI round-trip check. Do **not**
lift Godot numbers from `references/values_master.yaml` — it is auto-extracted, partly stale, and
indexes a nonexistent `params/combat.md` (see its header banner).

## Coverage (incremental)

| File | Subsystem | Source head |
|---|---|---|
| `core_resolution.json` | d10 engine + derived character scores | `params/core.md` (+ `designs/scene/derived_stats_v30.md` for Health) |

Other subsystems (contest, mass_combat, threadwork, board_game, factions) are **not yet typed** —
follow-on work under ED-1052. Add one by dropping a new `*.json` here in the same schema; the gate
picks it up automatically.

## Schema (v1)

```jsonc
{
  "schema_version": 1,
  "subsystem": "core_resolution",
  "scalars": {
    "tn_standard": { "value": 7, "type": "int", "unit": "target_number",
      "clamp": { "min": 0, "max": 20 },                 // optional
      "source": { "doc": "params/core.md", "section": "TN Values",
                  "patch": "PP-…",                       // optional
                  "quote": "| Standard | 7 |" } }        // must appear verbatim in `doc`
  },
  "formulas": {
    "combat_pool": { "expr": "(agility * 2) + (weapon_history_points + 3)",
      "inputs": ["agility", "weapon_history_points"],    // identifiers in expr beyond inputs
      "clamp": { "min": 5 },                             //   must be other param keys or math fns
      "result_type": "int",
      "source": { "doc": "params/core.md", "patch": "PP-615", "quote": "(Agility × 2) + …" } }
  },
  "tables": {
    "ev_per_die": { "rows": { "7": { "mu": 0.40, "sigma": 0.800 } },
      "source": { "doc": "params/core.md", "quote": "| 7 | 0.40 | 0.64 | 0.800 |" } }
  }
}
```

## The CI gate

`tools/engine_params_check.py` (CI job **Engine Params Round-Trip**) validates every file:
schema well-formedness, `clamp.min ≤ clamp.max`, formula identifiers resolve to declared inputs /
other param keys / a math allowlist, and — the core guarantee — **every entry's `source.quote`
still appears (whitespace-normalized) in its `source.doc`**. If you change a prose value, the quote
stops matching and CI fails until the typed file is updated to agree. Run locally:

```
python3 tools/engine_params_check.py
python -m pytest tests/valoria/test_engine_params_check.py -q
```

## Provenance discipline

When a typed value crosses from prose, cite the establishing `PP-NNN`/`ED-NNN` in `source.patch` and
pick a `quote` that is a distinctive verbatim substring of the current canonical head (resolve the head
via `CURRENT.md`). Never type a value the prose does not back.
