# Commit Message Convention

## Format
```
[scope] description — ID(s)
```

## Scopes
| Scope | When |
|-------|------|
| editorial | Editorial decision applied or ledger updated |
| patch | Mechanical fix applied |
| compilation | Stage assembled or checkpoint exported |
| simulation | Simulation batch committed |
| infrastructure | Scripts, skills, tooling, registry |
| skill | On-demand skill built or updated |
| cleanup | Renaming, deprecation, dead files |

## ID Cross-References
- `E-NNN` — editorial ledger entry
- `PP-NNN` — patch register entry
- `G-NNN` — gap register item
- `SIM-NNN` — simulation finding

## Examples
```
[editorial] Territory names confirmed — E-05
[patch] TD recovery mechanic added — PP-001
[patch] Stability floor removed — PP-114
[compilation] Assemble CP15 — stages 1-17
[simulation] Thread batch 09 — SIM-009-F-01 through F-12
[infrastructure] Add verify_cuts.py — Phase 0 step 0.4
[skill] Build valoria-sim-combat — Phase 1 step 1.7
[cleanup] Rename test files to convention — Phase 0 step 0.18
```
