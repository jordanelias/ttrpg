---
name: valoria-orchestrator
description: >
  Orchestrate multi-skill workflows for the Valoria videogame project (Godot 4.6).
  ALWAYS use this skill at the start of any Valoria task, to decompose it into the correct
  skill sequence, manage inter-skill handoffs, enforce the editorial gate, track the gap register,
  and ensure outputs feed forward correctly. Trigger on: "start work", "resume",
  "run a simulation", "stress test", "where did we leave off", "what's the plan", "compile",
  "build checkpoint", any multi-step Valoria task, or resuming work after a session gap.
  Also trigger whenever another Valoria skill needs routing or sequencing.
---

## COMPLIANCE IS AUTOMATIC

You do NOT manually run atomization, index generation, register splitting,
or archive chunking. These are enforced by `compliance_check.py` via hooks.

If bootstrap reports `[COMPLIANCE]` activity, it is handling rule violations.
Wait for it to complete. Then proceed with Jordan's task.

If bootstrap raises `[COMPLIANCE VIOLATION]` with manual items, those require
specific content decisions. Report to Jordan — do not guess.

**Never run these tasks manually:**
- "Atomize X" → compliance auto-splits at threshold
- "Split this register" → auto-archive on commit
- "Generate index for Y" → auto-generated when design doc committed
- "Regenerate the index" → auto-regenerated on any register change

---

## PROJECT CONTEXT — VIDEOGAME ONLY

**As of 2026-04-17, Valoria is a videogame project.** TTRPG, board game, and hybrid modes are abandoned. All design work targets the Godot 4.6 implementation in `jordanelias/valoria-game`.

**Implications for all skills:**
- Design docs containing TTRPG/BG/Hybrid mode-branching tables: extract the videogame-relevant rules only. Do not design for tabletop play.
- Mode applicability sections in design docs (`Three-mode: TTRPG/Hybrid/BG`) are historical. The videogame uses a unified ruleset that combines personal-scale mechanics (formerly "TTRPG") with strategic-scale mechanics (formerly "BG") in a single continuous experience.
- "Board game" mechanical abstractions (card-hand economy, phase-locked resolution, territory-level orders) remain valid as strategic-scale videogame mechanics. They are not board game mechanics — they are the videogame's strategic layer.
- "TTRPG" mechanical detail (dice pools, degree tables, skill checks, social contests, fieldwork procedures) remains valid as personal-scale videogame mechanics. There is no GM — the engine handles all resolution.
- Scale transitions between personal and strategic are the videogame's core architectural challenge. The zoom system (personal ↔ settlement ↔ territory ↔ peninsula) is the game's primary UX flow.
- All simulation, audit, and design work should evaluate mechanics through the lens of: "Can this be implemented in Godot? Does the player experience this through UI, or is it invisible engine logic?"

**Two repos:**
- `jordanelias/ttrpg` — design source of truth (mechanics, params, registers, skills)
- `jordanelias/valoria-game` — Godot implementation (GDScript, scenes, assets)

---

## STEP 0 — GitHub Bootstrap (MANDATORY, BLOCKING)

**This step executes before anything else. No memory substitution. No skipping.**

```python
import os, sys, json, base64, urllib.request

# PAT: read from env, fallback to file written by bootstrap
_pat_file = '/home/claude/.valoria_pat'
PAT = os.environ.get('GITHUB_PAT') or (open(_pat_file).read().strip() if __import__('os').path.exists(_pat_file) else '')
if not PAT:
    raise RuntimeError('GITHUB_PAT not set and .valoria_pat not found — re-run bootstrap')
os.environ['GITHUB_PAT'] = PAT
open(_pat_file, 'w').write(PAT)  # ensure file is always written
REPO = 'jordanelias/ttrpg'

# Bootstrap github_ops.py from repo
req = urllib.request.Request(
    f'https://api.github.com/repos/{REPO}/contents/skills/valoria-orchestrator/scripts/github_ops.py?ref=main',
    headers={'Authorization': f'token {PAT}', 'Accept': 'application/vnd.github.v3+json'}
)
with urllib.request.urlopen(req) as r:
    d = json.loads(r.read())
    open('/home/claude/github_ops.py', 'w').write(base64.b64decode(d['content']).decode())

sys.path.insert(0, '/home/claude')
import github_ops as g

# Step 1: fetch hooks (alongside github_ops — same REST call pattern)
import urllib.request as _ur, base64 as _b64, json as _j
for _src, _dst in [
    ('skills/valoria-orchestrator/scripts/valoria_hooks.py', '/home/claude/valoria_hooks.py'),
    ('tools/ci_register_size_check.py', '/home/claude/ci_register_size_check.py'),
]:
    _rq = _ur.Request(
        f'https://api.github.com/repos/jordanelias/ttrpg/contents/{_src}?ref=main',
        headers={'Authorization': f'token {PAT}', 'Accept': 'application/vnd.github.v3+json'}
    )
    with _ur.urlopen(_rq) as _r:
        open(_dst, 'w').write(_b64.b64decode(_j.loads(_r.read())['content']).decode())
import valoria_hooks as h

# Step 2: batch-read session-critical files (triggers register health check automatically)
files = g.read_files_graphql([
    'session_log_current.md',
    'session_logs/index.md',
    'canon/editorial_ledger_summary.yaml',
    'references/canonical_sources.yaml',
])
# Full registers — load only when needed:
# canon/editorial_ledger.yaml           → adding new editorials
# canon/patch_register_active.yaml      → patch work
# tests/coverage_matrix.md             → open SIM-DEBT
# *_archive.yaml / *_archive.md        → audit/reference only

# Step 3: confirm bootstrap and run all session-start hooks
h.assert_bootstrap()
h.context_gate()
token = g.assert_fetched(
    'session_log_current.md',
    'session_logs/index.md',
    'canon/editorial_ledger_summary.yaml',
    'references/canonical_sources.yaml',
)
print(f'Session token: {token}')
print('Bootstrap complete. All hooks active.')
```

**Execution requirement:** All GitHub operations must be executed via `bash_tool`, not written as passive code blocks. A code block that is not executed is not a fetch. Every `read_files_graphql()` and `atomic_commit()` call must appear as a `bash_tool` execution with visible output in context.

**Memory contamination warning:** userMemories may contain mechanical values (track values, territory data, faction stats, etc.) that feel current but are not fetched from GitHub. Do not use any value from memory as a source for mechanical analysis. Fetch only.

**Failure behavior:** If PAT is missing, GitHub is unreachable, or any critical file returns None — STOP. Report the error. State: "GitHub bootstrap failed — cannot proceed without live repo data." Do not continue using memory.

**After bootstrap:** Hold fetched contents in working context. Do not re-fetch within the same session unless a write has occurred since last fetch.


## Hook Quick Reference (valoria_hooks.py)

All hooks imported as `h` at bootstrap. All raise `RuntimeError` — no warnings.

| Hook | When to call | Blocks |
|------|-------------|--------|
| `h.assert_bootstrap()` | Immediately after bootstrap | Work before GitHub fetch |
| `h.task_gate(type)` | Before starting any task | Missing canonical sources |
| `h.task_gate_with_system(type, system, sources)` | Simulation/audit with specific system | Missing design doc |
| `h.editorial_gate(path, content)` | Called automatically by safe_commit | Unflagged editorial commits |
| `h.propose_mechanic_gate(system)` | Before any mechanic proposal | Proposing without sources |
| `h.pre_commit_gate(additions, deletions)` | Before every commit | Size, co-files, tools |
| `h.commit_message_gate(message)` | Before every commit | Bad message format |
| `h.context_gate()` | Every ~10 bash_tool calls | Context limit violations |
| `h.memory_contamination_guard(path, content)` | When reusing fetched content | Stale/injected content |
| `h.safe_commit(additions, deletions, message)` | **Always** — replaces g.atomic_commit() | All of the above |

## Register Health (Auto-enforced by github_ops.py)

`check_register_health()` runs automatically on first `read_files_graphql()` call each session.
**Hard stop on violation — no manual override.**

Thresholds (tokens = chars // 4):
| File | Limit |
|------|-------|
| session_log_current.md | 2,000 |
| canon/editorial_ledger.yaml (active) | 2,000 |
| canon/editorial_ledger_summary.yaml | 1,000 |
| references/canonical_sources.yaml | 5,000 |
| canon/patch_register_active.yaml | 20,000 |
| tests/coverage_matrix.md (active) | 5,000 |

**On violation:** archive resolved/applied/struck content to `_archive` file before any other work.
`append_to_register(path, new_entries, message)` enforces threshold before every register write.
`atomic_commit()` enforces threshold on every file in the commit additions list.

Archive size warning fires at 100,000 tokens — signals need for year-split.


**Fetch log (emit before any analysis):**
```
## FETCH LOG
session token: [16-char hex from g.assert_fetched()]
canonical_sources.yaml: ✓ fetched ([N] lines)
[canonical design doc path]: ✓ fetched ([N] lines)
params/[system].md: ✓ fetched ([N] lines) / ✗ missing
```
If any required file is missing from this log, or session token is absent, stop — the analysis is invalid. Jordan: verify the token is present and line counts are plausible before accepting any output.

**Version check:** confirm `<!-- version: -->` tag in each fetched params file matches current ruleset version in `deprecated/compilation/README.md`. If mismatch: flag `[STALE PARAMS: <file> is vX.XX, current is vY.YY]` and stop.

**Additional reads:** Any task referencing a specific design doc, params file, or register must fetch that file from GitHub before use. Do not read from memory, local copies, or project files.

## Session Start Protocol (MANDATORY)

Run Step 0 via `bash_tool`. Output Session Status Block.

- **If a task follows in the same message:** proceed to it immediately after the Status Block.
- **If no task follows:** stop and wait for Jordan to verify before sending the task.

If any fetch returns None or the token is missing, do not proceed regardless.

### Session Status Block — Contents
1. From fetched `session_log_current.md`: extract active resumption block.
   - If found: report last stage + next action in ≤3 lines; confirm before proceeding.
   - If not found: new session. Confirm task with user.
2. From fetched `canon/editorial_ledger_summary.yaml`: read p1_blocker_count and open_count. Report counts only.
3. **Roadmap position.** `quick_bootstrap` calls `report_roadmap()`, which reads `references/roadmap_state.yaml` and prints a `ROADMAP POSITION` block: current phase + item progress, next actions, completed phases, phases ahead, and pending decisions. Update `roadmap_state.yaml` (bump `updated` + counts) whenever a phase/item completes or a decision resolves — stale roadmap state is a defect of the same class as a stale session log.
4. Confirm task with user before proceeding.

## Canonical Hierarchy (immutable)
1. `canon/00_philosophical_foundations_rules.md` — governs everything
2. `canon/01_*.md` amendments — extend the Foundations
3. `canon/02_canon_constraints.md` — mechanical constraints P-01 to P-15
4. `designs/` working documents — canonical for active mechanics
5. `compilation/` — snapshots; use only when `compilation_current: true` in `canonical_sources.yaml`

If conflict: higher-ranked document wins. Always.
When `canonical_sources.yaml` lists a design doc as `canonical:` for a system, use that doc.
If `compilation_current: false`, never use the compilation as a source of mechanical values.

## Editorial Gate (MANDATORY)
**User retains exclusive authority over:**
- Setting, worldbuilding, character, narrative, faction behaviour decisions
- Ambiguous design intent
- All `[EDITORIAL: ...]` flagged items

**Flag format:** `[EDITORIAL: ED-NNN — brief description]`

**Claude executes without approval:**
- Formula fixes, consistency repairs, formatting
- Simulations and audit reports
- Mechanical patches derived from simulation findings

**Provisional decisions:** Make the most mechanically defensible choice. Mark `[PROVISIONAL: ...]`, add to editorial ledger with `status: provisional`. Unblocks simulation — not final.

## Skill Registry
| Skill | Path (on GitHub) | Model | Use When |
|-------|-----------------|-------|----------|
| valoria-orchestrator | `skills/valoria-orchestrator/SKILL.md` | Sonnet | Session start, routing, multi-step |
| valoria-simulator | `skills/valoria-simulator/SKILL.md` | Sonnet | Stress test, simulate |
| valoria-mechanic-audit | `skills/valoria-mechanic-audit/SKILL.md` | Sonnet | Mechanical consistency, gap detection (NOT bare "audit") |
| valoria-resolution-diagnostic | `skills/valoria-resolution-diagnostic/SKILL.md` | Opus | "engine / resolution audit" — rolling-engine resolution under stress |
| valoria-canon-guard | `skills/valoria-canon-guard/SKILL.md` | Sonnet | Canon compliance P-01–P-15 |
| valoria-editorial-register | `skills/valoria-editorial-register/SKILL.md` | Sonnet | Resolve editorials, harvest flags |
| valoria-compiler | `skills/valoria-compiler/SKILL.md` | Sonnet | Compile (lowest priority) |
| valoria-chunker | `skills/valoria-chunker/SKILL.md` | Haiku | Pre-process docs >500 lines |

**Audit routing.** The bare word "audit" routes to **nothing** — it is a free English word, not a trigger. Qualified audit phrases route to their specific skill: "mechanical audit" / "audit for mechanics" → `valoria-mechanic-audit`; "engine audit" / "resolution diagnostic audit" / "resolution audit" → `valoria-resolution-diagnostic`; "canon check" → `valoria-canon-guard`; "vector/topographic/corpus audit" → `valoria-vector-audit`; "interface audit" → `valoria-module-adjudicator`. **"NERS audit" is currently unassigned (routes to nothing)** — NERS (Necessary/Robust/Smooth/Elegant) is the project-wide verdict framework, not a single skill. **All audits run on whatever work/files exist local to the session — the target need not be canon (D2);** canon is the baseline, the latest local session work supersedes stale canon.

**Skills load from `/mnt/skills/user/` at runtime.** GitHub (`skills/*/SKILL.md`) is the version-controlled source. Do not fetch skills from GitHub during a session.


## Collision Prevention (MANDATORY — run before every `atomic_commit()` call)

A session collision occurs when another session writes a file between your fetch and your commit.
This causes silent overwrites. Prevent it:

```python
import os, sys
os.environ['GITHUB_PAT'] = '<PAT>'
sys.path.insert(0, '/home/claude')
import github_ops as g

# Before committing: re-fetch the specific files you are about to modify
# and compare content against what you fetched at session start.
files_to_write = ['path/to/file1.md', 'path/to/file2.md']
fresh = g.read_files_graphql(files_to_write)

for path in files_to_write:
    fresh_content = fresh.get(path)
    session_content = session_fetched[path]   # your original fetch
    if fresh_content != session_content:
        print(f"[COLLISION: {path} was modified since session fetch — DO NOT OVERWRITE]")
        print("Stop commit. Review changes before proceeding.")
        raise SystemExit(1)

# Only if all match: proceed with atomic_commit()
```

**On collision detected:** STOP. Do not commit. Surface the conflict to the user. Show a diff summary if possible.

## ED Number Collision Guard

The editorial ledger `# next_id:` counter must be read from a FRESH fetch immediately before assigning new ED numbers — not from the session-start fetch. Two concurrent sessions can otherwise assign the same IDs.

```python
# Right before assigning any new ED-NNN:
fresh_ledger = g.read_files_graphql(['canon/editorial_ledger.yaml'])
import re
raw = fresh_ledger['canon/editorial_ledger.yaml']
nid_match = re.search(r'# next_id:\s*(\d+)', raw)
if not nid_match:
    raise RuntimeError("next_id not found in ledger — cannot safely assign ED numbers")
next_id = int(nid_match.group(1))
# Assign: next_id, next_id+1, ... for this batch
# After committing: confirm the committed file has next_id incremented correctly
```

**Known issue (2026-04-13):** Ledger header says `# next_id: 486` but items ED-486 through ED-489 exist. Actual safe next_id is **490**. The collision guard will catch this correctly if you re-fetch.

## Design Registry

`references/design_registry.yaml` is the single source of truth for v30 design doc paths and atomization state.

**Fetch on any session that touches design doc paths:**
```python
files = g.read_files_graphql(['references/design_registry.yaml'])
```

**Before renaming or creating index/infill files:** read the registry, update `canonical_v30`, `index`, `infill`, `atomized` fields atomically.

**After any rename, atomization, or deprecation:** include `references/design_registry.yaml` in the same atomic commit.

## v30 Naming Convention (from 2026-04-13)

All active canonical design docs use the `_v30.md` suffix. Pre-v30 filenames are deprecated.

| File type | Pattern |
|-----------|---------|
| Canonical design doc | `designs/{system}/{name}_v30.md` |
| Index (mechanical spec only) | `designs/{system}/{name}_v30_index.md` |
| Content infill (prose, rationale) | `designs/{system}/{name}_v30_infill.md` |
| Mode-split variant | DEPRECATED — videogame is the sole target. Existing mode-split files are historical. |

If any skill, params file, or cross-reference still uses a pre-v30 path, flag it:
`[STALE REF: <file> references <old-path> — update to <v30-path>]`

## v30 Propagation Protocol

After any v30 rename commit, run a propagation pass to update all cross-references:

1. Fetch `references/propagation_map.md` and `references/design_registry.yaml`
2. For each renamed doc: grep all repo files that reference the old path
3. Update all references to the new v30 path
4. Include `references/propagation_map.md` + all updated files in one atomic commit
5. Run freshness_gate after: `python3 tools/freshness_gate.py --update`

Tools: `tools/find_references.py` can assist with step 2.



## Two-Repo Architecture

Valoria has two repositories:

| Repo | Purpose | Enforcement |
|------|---------|-------------|
| `jordanelias/ttrpg` | Design: mechanics, params, registers, skills | Full — register health, editorial gate, co-files, CI |
| `jordanelias/valoria-game` | Godot implementation: GDScript, scenes, assets | Commit format only — no register/editorial checks |

**Default is `ttrpg`.** Switch repos with `g.use_repo('valoria-game')` or pass `repo=` per-call.

### Working on valoria-game

```python
# Fetch Godot files
files = g.read_files_graphql(['autoload/Meta.gd', 'systems/combat/CombatLogic.gd'],
                              repo='valoria-game')

# Commit Godot files — same safe_commit, different repo
oid = h.safe_commit(
    additions=[('autoload/Meta.gd', new_content)],
    deletions=[],
    message='[godot] Meta: add faction stat tracker — PP-644',
    repo='valoria-game',
)
```

**Commit message scopes for valoria-game:** `[godot]` · `[phase]` · `[fix]` · `[bugfix]` · `[infrastructure]`

### Cross-repo work (design change → implementation)

When a design change in ttrpg requires a corresponding change in valoria-game, commit both atomically in sequence:

```python
# 1. Commit design change to ttrpg
oid1 = h.safe_commit(design_additions, [], '[patch] PP-NNN: mechanic change', repo='ttrpg')

# 2. Commit implementation to valoria-game
oid2 = h.safe_commit(godot_additions, [], '[godot] implement PP-NNN: mechanic change', repo='valoria-game')
```

### What GitHub sources for valoria-game

Read from ttrpg params files to implement. Never invent mechanical values:
```python
params = g.read_files_graphql(['params/combat.md'], repo='ttrpg')
# Use params content to derive constants for GDScript
```



## Fetch Depth Routing (Token Efficiency)

**Default: index-first.** Always load the canonical v30 index file, NOT the infill, unless prose rationale is specifically needed.

| Task | Depth | Function |
|---|---|---|
| Mechanic proposal | `index` | `g.fetch_system('combat', cs_content)` |
| Simulation | `params_only` | `g.fetch_system('combat', cs_content, depth='params_only')` |
| Deep editorial review | `full` | `g.fetch_system('combat', cs_content, depth='full')` |
| Canon check | Use `canon/00_philosophical_foundations_rules.md` (1,943t) NOT full prose (17,554t) |
| Audit | `index` + params separately if values needed |

**Infill files exist for rationale/prose.** They are NOT needed for: simulation, audit, mechanic proposal, patch work, compilation. Only load infill when Jordan asks for philosophical justification or narrative context.

## Workflows

**Full Mechanical Audit**
GitHub fetch relevant docs → chunker (A, C, E) → canon-guard → mechanic-audit (A–E) → gap register update → findings report

**Philosophy Compliance Check**
GitHub fetch relevant docs → chunker (target section) → canon-guard

**Stress Test Suite**
GitHub fetch relevant docs → chunker (target mechanics + dependencies) → simulator (Mode A then D) → findings report

**Targeted Repair**
GitHub fetch relevant docs → canon-guard → mechanic-audit → [EDITORIAL GATE if content] → compiler

**New Mechanic Development**
GitHub fetch all relevant design docs → canon-guard (pre-check) → mechanic-audit (integration) → simulator (stress test) → [EDITORIAL GATE] → compiler

## Commit Protocol (Every Commit)
Every commit must be atomic and include:
1. Changed design doc(s)
2. Corresponding params file(s) if mechanical values changed
3. `references/canonical_sources.yaml` if source authority changed
4. `references/propagation_map.md`
5. `canon/patch_register_active.yaml` if patches applied
6. `canon/editorial_ledger.yaml` if editorial items added/resolved
7. `tests/coverage_matrix.md` if simulation run
8. Test output in `tests/` if simulation run
9. Run `python3 tools/freshness_gate.py --update` after any canonical doc change; include result in same commit

**Pre-commit — use `h.safe_commit()` instead of `g.atomic_commit()` directly:**
```python
oid = h.safe_commit(additions, deletions, message)
# Automatically runs: commit_message_gate + editorial_gate + pre_commit_gate
# (which includes freshness_gate, broken_dependency_checker, patch_propagation_checker)
# Raises RuntimeError on any violation — no bypass.
```

**Post-commit verification (WS-BU-1, ED-837 — 2026-05-15):** every `safe_commit` MUST be followed by a read-back of each file in the `additions` list, with grep for at least one required content marker per file. Hook chain catches violations pre-commit; post-commit read-back catches the rare cases where the local change does not match what landed on remote (network failure mid-write, content-encoding drift, etc.).

```python
# After safe_commit returns the SHA, verify:
for path, expected_content in expected_markers.items():
    landed = g.read_files_graphql([path])[path]
    assert expected_content in landed, f"Post-commit verify failed: {path}"
```

Treat this as a standing practice. Workstream audit 2026-05-15 (`tests/audit/workstream_meta_audit_2026-05-15.md`) found post-commit verification was applied to 4 of 10 commits in the same-day chain; asymmetric verification weakens the audit trail.
Direct `g.atomic_commit()` is permitted only in infrastructure commits where hooks are being updated.

**Post-commit verification:** after `atomic_commit()` returns a SHA, re-fetch all files modified in that commit and confirm content matches what was committed. If content differs: flag immediately, do not proceed.

**Commit message format:** `[scope] description — PP-NNN / ED-NNN if applicable`
Scopes: `editorial` / `patch` / `simulation` / `compilation` / `infrastructure` / `skill` / `cleanup`


---

## Standard Work Block Template

Every bash_tool block after bootstrap uses this preamble. Copy-paste verbatim:

```python
import sys; sys.path.insert(0, '/home/claude')
from github_ops import quick_bootstrap
g, h, files, token = quick_bootstrap()
# For task-specific extra files:
# g, h, files, token = quick_bootstrap(['canon/patch_register_active.yaml'])

h.context_gate()
h.task_gate('design')  # replace with actual task type
# ... work ...
```

`quick_bootstrap()` handles: PAT load from `.valoria_pat`, env set, session-start fetch,
`assert_bootstrap()`, module reload. No manual boilerplate required.

Valid task types: `audit` · `canon_check` · `compilation` · `design` · `editorial` · `patch` · `propose_mechanic` · `simulation`

Each type pre-fetches its required files — see `TASK_REQUIRED_FILES` in `valoria_hooks.py`.

---
## Session Close Protocol
**Re-fetch after writes:** after any `atomic_commit()` call, re-fetch all modified files before referencing them again in the same session. The in-context version and the committed version may differ.

**All commits go to GitHub via `h.safe_commit()`, `g.close_session_log()`, or `g.safe_session_close()` (legacy). Direct `g.atomic_commit()` raises RuntimeError without authorization from safe_commit().**

**Per-session logs (current protocol):** Each session writes to `session_logs/<scope>_<token>.md`. The file `session_log_current.md` is auto-generated — direct writes are blocked by `pre_commit_gate`. Use `g.start_session_log(scope, token)` at session open and `g.close_session_log(scope, token, final_content)` at close. `g.safe_session_close()` is legacy (single-file, no per-session index) — use only if per-session logging is not yet active.

**Concurrent sessions:** Each session has its own `session_logs/<scope>_<token>.md`. Bootstrap reports all active sessions from `session_logs/index.md`. Conflict detection runs through handoff `owns` declarations — see handoff workflow below.

**Session close sequence** — follow in order:

**Step 1 — Write handoff** (required if work continues in a future session):
```python
g.write_handoff({
    'id': '<scope>_<slug>',           # e.g. 'simulation_battery_bands'
    'scope': '<scope>',               # simulation | editorial | design | infrastructure | godot
    'task': {
        'skill': '<skill-name>',
        'description': '<one-line summary of the continuing task>',
    },
    'context_files': [
        {'path': '<repo-relative-path>', 'depth': 'skeleton|full',
         'repo': 'ttrpg',             # or 'valoria-game' for Godot files
         'reason': '<why this file is needed on resume>'},
    ],
    'working_state': {
        'completed': ['<item>', ...],
        'in_progress': [],
        'next': ['<first thing to do on resume>', ...],  # non-empty required
    },
    'owns': ['<glob>', ...],           # files this workstream modifies — required for conflict detection
    'key_values': ['<decision or value to carry forward>', ...],
    'blockers': ['<blocking issue>', ...],
    'last_commit': '<short-sha>',
})
# → prints resumption block — copy it, give it to Jordan for the next session
```

**Step 2 — Require handoff on close** (validates the file was written correctly):
```python
h.require_handoff_on_close('<handoff_id>')
```

**Step 3 — Close session log:**
```yaml
session_id: <scope>_<token>
session_close: YYYY-MM-DD HH:mm
scope: <scope>
status: CLOSED
last_stage: <stage name>
next_action:
  skill: <skill-name>
  description: <what to do on resume>
blockers: []
```
```python
g.close_session_log(scope, token, final_content, handoff_id='<handoff_id>')
```

This archives the session log to `archives/session/`, removes the session from `session_logs/index.md`, updates the auto-generated pointer, and validates the handoff reference.

**If work is complete** (no continuation): omit `g.write_handoff()` and `h.require_handoff_on_close()`. Call `g.close_session_log()` without `handoff_id`.

## Token Rules
- Never re-read a document already fetched this session. Consume fetched content.
- Never re-run a completed stage. Consume prior results.
- Intermediate work: tables, not prose.
- Context limit approaching → complete current stage → session-close → commit → instruct new chat.
- Chunk all inputs >500 lines before passing to any analysis skill.
