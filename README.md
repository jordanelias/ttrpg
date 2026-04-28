# Valoria — Design Canon

Design source of truth for **Valoria**, a Godot 4.6 videogame combining personal-scale resolution (dice pools, skill checks, social contests) with strategic-layer board game mechanics (territory control, faction politics, domain actions).

## Two-Repo Structure

| Repo | Purpose |
|---|---|
| `jordanelias/ttrpg` (this repo) | Design documents, parameters, simulation outputs, editorial tracking |
| `jordanelias/valoria-game` | Godot 4.6 implementation |

Design docs retain mechanical detail from TTRPG/board game origins — these abstractions **are** the videogame's strategic and personal layers. There is no GM; the engine handles all resolution.

## Project State

Current workplan: `designs/workplans/valoria_workplan_v3_consolidated.md`

Phase 0 (Foundation) in progress. See workplan for full 7-phase plan through First Playable.

## Key Directories

| Directory | Contents |
|---|---|
| `canon/` | Philosophical foundations, editorial ledger, patch register, timeline |
| `designs/` | System design docs (architecture, NPCs, provincial, scene, threadwork, world) |
| `params/` | Extracted mechanical parameters (combat, threadwork, factions, board game) |
| `references/` | Canonical sources registry, propagation map, glossary, throughlines |
| `tests/` | Simulation outputs, stress tests, coverage matrix |
| `tools/` | CI checks, collator, freshness gate, compliance |
| `archives/` | Session logs, resolved editorials, archived patches |

## Bootstrap

Claude sessions begin with a bootstrap block that downloads orchestration scripts and loads register files. See system prompt for protocol.

## CI

7-job CI pipeline validates: co-file compliance, editorial markers, register sizes, hook verification, naming consistency.
