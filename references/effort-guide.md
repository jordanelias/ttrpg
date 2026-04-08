# Valoria Skill Effort Guide

Effort levels govern how much work a skill expends on a given task.
Valid values: 150 · 125 · 100 · 75 · 50.

Inline instruction from the user overrides this table. If the user specifies effort for a task, that governs.

## Per-Skill Default Effort

| Skill | Default Effort |
|-------|---------------|
| valoria-orchestrator | 100 |
| valoria-simulator | 125 |
| valoria-mechanic-audit | 125 |
| valoria-canon-guard | 100 |
| valoria-editorial-register | 100 |
| valoria-compiler | 75 |
| valoria-chunker | 75 |
| valoria-arc-generator | 125 |
| valoria-combat-simulator | 125 |
| valoria-dice-model | 75 |

## Effort Level Definitions

| Level | Meaning |
|-------|---------|
| 150 | Maximum depth. Exhaustive coverage. Use for P1-BLOCKER resolution, final pre-playtest audits. |
| 125 | High depth. Full mode coverage, complete edge-case search. Default for simulation and audit skills. |
| 100 | Standard. All required modes, representative edge cases. Default for orchestration and canon work. |
| 75 | Reduced. Core modes only, no extended edge-case sweep. Default for compilation and chunking. |
| 50 | Minimal. Single-pass, primary output only. Use when speed matters more than coverage. |
