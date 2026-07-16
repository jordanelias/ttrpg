# Valoria — Design Canon

Design source of truth for **Valoria**, a Godot 4.6 videogame that fuses personal-scale resolution
(dice pools, skill checks, social contests) with a strategic layer (territory control, faction
politics, domain actions). There is no GM — the engine resolves everything.

| Repo | Purpose |
|---|---|
| `jordanelias/ttrpg` (this repo) | Design docs, parameters, simulation outputs, editorial tracking |
| `jordanelias/valoria-game` | Godot 4.6 implementation |

## Start here

This README intentionally carries **no live state** (the old version drifted — stale workplan, retired
bootstrap, wrong CI job count). For anything current, defer to:

- **`CLAUDE.md`** — how this repo is worked: conventions, repository map, the data→Godot pipeline, the
  port state, enforcement, and task routing. **Read this first if you are an agent.**
- **`CURRENT.md`** — the single human-readable index of the live canonical head per subsystem
  (Generation v40). The authority on what is current.
- **`HANDOFF.md`** — the single live continuity surface: pending work and next actions.
- **`references/canonical_sources.yaml`** + **`registers/mechanics_index.yaml`** — machine-readable indices.

Superseded exploration lives under `archives/` and `deprecated/` — history, not canon.

## License

See `LICENSE`.
