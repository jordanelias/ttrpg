# VALORIA PROJECT INSTRUCTIONS
## For All Sessions — Read First
## Version: 2026-04-02

---

## BOOTSTRAP (Run First — Every Session)

```python
# Step 1: Set PAT (from Claude Project Instructions — never commit this)
import os
os.environ['GITHUB_PAT'] = '<PAT from Claude Project Instructions>'

# Step 2: Bootstrap github_ops.py via REST (one-time per session)
import urllib.request, json, base64
PAT = os.environ['GITHUB_PAT']
req = urllib.request.Request(
    'https://api.github.com/repos/jordanelias/ttrpg/contents/skills/valoria-orchestrator/scripts/github_ops.py?ref=main',
    headers={'Authorization': f'token {PAT}', 'Accept': 'application/vnd.github.v3+json'}
)
with urllib.request.urlopen(req) as r:
    d = json.loads(r.read())
    open('/home/claude/github_ops.py', 'w').write(base64.b64decode(d['content']).decode())

# Step 3: All subsequent reads via GraphQL (token-efficient batch reads)
import sys; sys.path.insert(0, '/home/claude')
import github_ops as g  # now available
# g.read_files_graphql([list of paths]) — one API call for N files
# g.atomic_commit(additions, deletions, message) — one API call for N file writes
```

**PAT location:** Claude Project Instructions (not in any committed file). Copy from there.
**GraphQL:** Use `g.read_files_graphql()` for ALL file reads after bootstrap. Never use individual REST calls for batch reads.
**Writes:** Use `g.atomic_commit()` exclusively — never individual file PUTs.

---

## What This Project Is

Valoria is a tabletop roleplaying game / board game / hybrid playable in all three modes. All three modes are mechanically grounded in the TTRPG baseline — Hybrid bridges them, Board Game abstracts to strategic scale.

Frame: **TTRPG ← Hybrid → Board Game**

---

## State and Authority

**All persistent state lives on GitHub** (`jordanelias/ttrpg`, branch `main`). Project Files are deprecated — do not use them.

**Document authority (immutable hierarchy):**
1. `canon/00_philosophical_foundations.md` — governs everything
2. `canon/01_*.md` amendments — extend the Foundations
3. `canon/02_canon_constraints.md` — mechanical constraints derived from Foundations (P-01 to P-15)
4. `designs/` working documents — source of truth for all active mechanics
5. `compilation/` — periodic snapshots; use only when `compilation_current: true` in `references/canonical_sources.yaml`

**Critical rule:** When `references/canonical_sources.yaml` lists a design doc as `canonical:` for a system, use that design doc. If `compilation_current: false`, the compilation stage is stale — never use it as a source of mechanical values.

---

## Session Start Protocol (Mandatory)

1. Bootstrap `github_ops.py` from `skills/valoria-orchestrator/scripts/github_ops.py`. Use `read_files_graphql()` for all batch reads.
2. Read `session_log_current.md` from GitHub. Report last stage + next action in ≤3 lines.
3. Read `canon/editorial_ledger.yaml`. Report P1-BLOCKER count only.
4. Read `references/file_index.md` KNOWN STALE SYNC GAPS section. Report count.
5. Confirm task with user before proceeding.

---

## Simulation Commands

| Command | What runs |
|---------|-----------|
| `stress test [specific mechanic]` | Simulator Modes A + D + J + L (isolation, edge cases, cognitive load, precedent) |
| `stress test [subsystem]` | Simulator Mode G-submode + D + J + K + L (full subsystem + cross-mode) |
| `stress test [mode]` | All G-submodes for that mode — multi-session, orchestrator stages it |
| `simulate [scenario]` | Simulator Modes C + M (full scenario + branching flowchart) |
| `simulate [ttrpg/hybrid/boardgame]` | Modes C + G-suite + M — multi-session |
| `audit [subsystem]` | Mechanic-audit Modes A–G |

**Every simulation run commits findings immediately** (Mode I protocol). Nothing accumulates between sessions.

**Audit criteria covered:** crunch cascade, edge cases, regressions, failures, ambiguities, overlap, incoherence, philosophy compliance, cognitive load, time consumed, meaningful actions, emergent gameplay, precedent comparison, cross-mode interdependency, transition/zoom fidelity, narrative branching flowcharts.

---

## Mandatory Model Routing

| Task | Model |
|------|-------|
| Chunking, indexing, section extraction, dice math, format fixes | Haiku 4.5 |
| Simulation, audit, canon compliance, mechanical gap-fill, compilation | Sonnet 4.6 |
| Editorial-adjacent design, ambiguous intent, philosophy-heavy design | Opus 4.6 |

Assess tier BEFORE starting. If the current model is wrong: flag `[MODEL MISMATCH: this is <tier>-tier work]` and stop.

---

## Editorial Gate

**User approves:** setting, worldbuilding, characters, narrative, faction behaviour, ambiguous design intent, all `[EDITORIAL: ...]` items.

**Claude executes without approval:** formula fixes, consistency repairs, formatting, simulations, mechanical patches derived from simulation findings.

**Provisional decisions:** When a blocker prevents simulation, Claude makes the most mechanically defensible choice, marks it `[PROVISIONAL: ...]`, adds it to the editorial ledger with `status: provisional`, and surfaces it for user review. Provisional decisions unblock simulation — they are not final.

**Flag format:** `[EDITORIAL: ED-NNN — brief description]`

---

## Commit Protocol (Mandatory on Every Commit)

Every commit must be atomic and contain:
1. The changed design doc(s)
2. The corresponding params file(s) if mechanical values changed
3. `references/canonical_sources.yaml` if a source authority changed
4. `references/propagation_map.md` (updated with any new cross-references)
5. `canon/patch_register.yaml` if patches were applied
6. `canon/editorial_ledger.yaml` if editorial items were added/resolved
7. `tests/coverage_matrix.md` if a simulation was run
8. The test output file in `tests/` if a simulation was run

**Commit message format:** `[scope] description — PP-NNN / ED-NNN if applicable`

Scopes: `editorial` / `patch` / `simulation` / `compilation` / `infrastructure` / `skill` / `cleanup`

Never commit a design file without updating `canonical_sources.yaml` if the commit changes which document is canonical for a system.

---

## Key Reference Files

| File | Purpose |
|------|---------|
| `references/canonical_sources.yaml` | Which document is canonical for each system |
| `references/propagation_map.md` | Cross-reference dependencies; auto-updated on every commit |
| `references/file_index.md` | All files, status, stale gaps |
| `references/params_*.md` | Extracted mechanical values for each system |
| `canon/editorial_ledger.yaml` | All editorial decisions (49 items: 40 open, 3 provisional, 3 resolved, 4 struck) |
| `canon/patch_register.yaml` | All patches PP-001–PP-096 |
| `tests/coverage_matrix.md` | Simulation coverage; P1 findings; SIM-DEBT register |
| `skills/valoria-orchestrator/references/state_transfer_spec.md` | State variables at every mode boundary |
| `skills/valoria-orchestrator/references/skill_registry.md` | All skills, paths, triggers, command routing |
| `session_log_current.md` | Current session state |

---

## Skills

All skills live in `skills/` on GitHub. Read from GitHub — never from local or Project File copies.

| Skill | Path | Tier | Use When |
|-------|------|------|----------|
| valoria-orchestrator | `skills/valoria-orchestrator/SKILL.md` | Sonnet | Session start, routing, any multi-step task |
| valoria-simulator | `skills/valoria-simulator-SKILL.md` | Sonnet | Stress test, simulate, Modes A–M |
| valoria-mechanic-audit | `skills/valoria-mechanic-audit-SKILL.md` | Sonnet | Audit, consistency check, gap detection |
| valoria-canon-guard | `skills/valoria-canon-guard-SKILL.md` | Sonnet | Canon compliance (P-01–P-15) |
| valoria-editorial-register | `skills/valoria-editorial-register/SKILL.md` | Sonnet | Resolve editorials, harvest flags, dedup |
| valoria-compiler | `skills/valoria-compiler-SKILL.md` | Sonnet | Compile (lowest priority — only on request) |
| valoria-chunker | `skills/valoria-chunker-SKILL.md` | Haiku | Pre-process docs >500 lines |
| valoria-arc-generator | `skills/valoria-arc-generator/SKILL.md` | Sonnet | Generate arcs, campaign scenarios |
| valoria-combat-simulator | `skills/valoria-combat-simulator/SKILL.md` | Sonnet | Statistical/probabilistic combat analysis |
| valoria-dice-model | `skills/valoria-dice-model/SKILL.md` | Haiku | Dice math, probability tables |

---

## Context Limit

At 90% context: halt all tasks, run Session Close Protocol, commit everything, tell the user to start a new chat. This rule overrides everything else.

---

## GitHub

**Repository:** `jordanelias/ttrpg` branch `main`
**PAT:** stored in Claude Project Instructions only — never in any committed file
**Operations:** use `github_ops.py` exclusively. GraphQL for batch reads (`read_files_graphql`). GraphQL mutation for atomic commits (`atomic_commit`). REST only for operations not covered by the script.

---

## Compilation

Compilation is the **lowest-priority task**. Never block design, simulation, or editorial work waiting for compilation. Compile only when:
- A system is stable (no open P1 editorials, no unresolved stress-test findings)
- The user explicitly requests it
- `canonical_sources.yaml` shows `compilation_current: false` for that system and a compilation pass is due

Compilation reads FROM `canonical:` docs in `canonical_sources.yaml` and writes TO `compilation/v[N]/`.

---

## Open Blockers (as of 2026-04-02)

| ID | Description | Blocks |
|----|-------------|--------|
| ED-001 | Card-Hand system for BG | BG compilation sync |
| ED-036 | Altonian unit stats (provisional placeholder active) | Hybrid Altonian engagement |
| ED-048 | 'Ceiral' is not a canon name | NPC/arc work referencing this character |

All other editorial items are non-blocking for simulation.
**SIM-DEBT-01:** Debate stress tests calibrated with Cognition+History pool; now (Presence×2)+History. Re-simulation needed before calibration values are treated as final.
---

## Skeleton Ruleset Principle

**Design documents (`designs/`) must be mechanical specifications only.** No explanatory prose, no historical context, no "why we designed it this way." Those belong in compilation or separate reference documents.

A skeleton ruleset contains:
- Tables (weapon stats, armour DR, degree table, phase structure)
- Formulas (pool = X, damage = Y)
- Procedures (numbered steps)
- Edge case rulings (one sentence each)
- Cross-references to other files

A skeleton ruleset does NOT contain:
- Historical precedent (Scholastic disputatio, etc.) → reference doc or compilation
- Philosophical motivation → compilation or canon
- Design rationale prose → compilation
- Patch history → `references/params_[system]_history.md`

**Flag for splitting:** Any design doc over 400 lines likely has non-skeleton content. Flag it as `[SKELETON-DEBT: file — contains explanatory content at lines N-M]` when encountered.

---

## Container Pattern

Every file in the pipeline is a **container** — it contains values and points to related containers:

```
Skill
  └─ references params file (mechanical values only)
       ├─ patch_history: references/params_[system]_history.md
       ├─ canonical_sources: references/canonical_sources.yaml
       └─ (if value missing) → canonical source document
```

**params files** contain: headers, formula tables, key value tables, stale flags. Nothing else.
**params_history files** contain: all patches applied, pending editorials, SIM-DEBT items.
**canonical_sources.yaml** contains: which document is canonical per system.
**propagation_map.md** contains: cross-reference relationships between files.

This means simulations stay fast (params are compact), history is preserved (history files), and canonical authority is unambiguous (canonical_sources.yaml).

**Commit protocol for params:** When a patch changes mechanical values:
1. Update `references/params_[system].md` (values only)
2. Append the patch summary to `references/params_[system]_history.md`
3. Include both in the same atomic commit

---

## Broken Dependency Check

Before closing any commit, run:
```bash
export GITHUB_PAT=<pat>
python3 tools/broken_dependency_checker.py
```

Exit 0 = clean. Exit 1 = broken references. Fix before committing.

