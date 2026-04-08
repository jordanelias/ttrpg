---
name: valoria-orchestrator
description: >
  Orchestrate multi-skill workflows for the Valoria TTRPG/board game/hybrid project.
  ALWAYS use this skill at the start of any Valoria task, to decompose it into the correct
  skill sequence, manage inter-skill handoffs, enforce the editorial gate, track the gap register,
  and ensure outputs feed forward correctly. Trigger on: "start work", "resume", "audit the ruleset",
  "run a simulation", "stress test", "where did we leave off", "what's the plan", "compile",
  "build checkpoint", any multi-step Valoria task, or resuming work after a session gap.
  Also trigger whenever another Valoria skill needs routing or sequencing.
---

## STEP 0 — GitHub Bootstrap (MANDATORY, BLOCKING)

**This step executes before anything else. No memory substitution. No skipping.**

```python
import os, sys, json, base64, urllib.request

PAT = os.environ['GITHUB_PAT']  # must be set — abort if missing
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

# Batch-read all session-critical files
files = g.read_files_graphql([
    'session_log_current.md',
    'canon/editorial_ledger.yaml',
    'references/file_index.md',
    'references/canonical_sources.yaml',
    'references/propagation_map.md',
])
token = g.assert_fetched(
    'session_log_current.md',
    'canon/editorial_ledger.yaml',
    'references/canonical_sources.yaml',
)
print(f'Session token: {token}')
```

**Execution requirement:** All GitHub operations must be executed via `bash_tool`, not written as passive code blocks. A code block that is not executed is not a fetch. Every `read_files_graphql()` and `atomic_commit()` call must appear as a `bash_tool` execution with visible output in context.

**Memory contamination warning:** userMemories may contain mechanical values (track values, territory data, faction stats, etc.) that feel current but are not fetched from GitHub. Do not use any value from memory as a source for mechanical analysis. Fetch only.

**Failure behavior:** If PAT is missing, GitHub is unreachable, or any critical file returns None — STOP. Report the error. State: "GitHub bootstrap failed — cannot proceed without live repo data." Do not continue using memory.

**After bootstrap:** Hold fetched contents in working context. Do not re-fetch within the same session unless a write has occurred since last fetch.

**Fetch log (emit before any analysis):**
```
## FETCH LOG
session token: [16-char hex from g.assert_fetched()]
canonical_sources.yaml: ✓ fetched ([N] lines)
[canonical design doc path]: ✓ fetched ([N] lines)
references/params_[system].md: ✓ fetched ([N] lines) / ✗ missing
```
If any required file is missing from this log, or session token is absent, stop — the analysis is invalid. Jordan: verify the token is present and line counts are plausible before accepting any output.

**Version check:** confirm `<!-- version: -->` tag in each fetched params file matches current ruleset version in `compilation/README.md`. If mismatch: flag `[STALE PARAMS: <file> is vX.XX, current is vY.YY]` and stop.

**Additional reads:** Any task referencing a specific design doc, params file, or register must fetch that file from GitHub before use. Do not read from memory, local copies, or project files.

## Two-Message Session Start (MANDATORY)

**Message 1 — Bootstrap only:** Run Step 0 via `bash_tool`. Output Session Status Block only. Stop.
**Message 2 — Task:** Jordan verifies the Session Status Block is present and all fetches succeeded, then sends the task.

If any fetch in Message 1 returns None or the token is missing, do not proceed to Message 2.

## Session Start Protocol
1. From fetched `session_log_current.md`: extract active resumption block.
   - If found: report last stage + next action in ≤3 lines; confirm before proceeding.
   - If not found: new session. Confirm task with user.
2. From fetched `canon/editorial_ledger.yaml`: count P1-BLOCKER items. Report count only.
3. From fetched `references/file_index.md`: report KNOWN STALE SYNC GAPS count only.
4. Confirm task with user before proceeding.

## Canonical Hierarchy (immutable)
1. `canon/00_philosophical_foundations.md` — governs everything
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
| valoria-mechanic-audit | `skills/valoria-mechanic-audit/SKILL.md` | Sonnet | Audit, consistency, gap detection |
| valoria-canon-guard | `skills/valoria-canon-guard/SKILL.md` | Sonnet | Canon compliance P-01–P-15 |
| valoria-editorial-register | `skills/valoria-editorial-register/SKILL.md` | Sonnet | Resolve editorials, harvest flags |
| valoria-compiler | `skills/valoria-compiler/SKILL.md` | Sonnet | Compile (lowest priority) |
| valoria-chunker | `skills/valoria-chunker/SKILL.md` | Haiku | Pre-process docs >500 lines |

**Skills load from `/mnt/skills/user/` at runtime.** GitHub (`skills/*/SKILL.md`) is the version-controlled source. Do not fetch skills from GitHub during a session.

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
5. `canon/patch_register.yaml` if patches applied
6. `canon/editorial_ledger.yaml` if editorial items added/resolved
7. `tests/coverage_matrix.md` if simulation run
8. Test output in `tests/` if simulation run
9. Run `python3 tools/freshness_gate.py --update` after any canonical doc change; include result in same commit

**Pre-commit (run before every `atomic_commit()` call):**
```bash
python3 tools/freshness_gate.py --update
python3 tools/broken_dependency_checker.py
python3 tools/patch_propagation_checker.py
```
Exit 0 required on all three. On non-zero exit: fix the reported issue before committing.

**Post-commit verification:** after `atomic_commit()` returns a SHA, re-fetch all files modified in that commit and confirm content matches what was committed. If content differs: flag immediately, do not proceed.

**Commit message format:** `[scope] description — PP-NNN / ED-NNN if applicable`
Scopes: `editorial` / `patch` / `simulation` / `compilation` / `infrastructure` / `skill` / `cleanup`

## Session Close Protocol
**Re-fetch after writes:** after any `atomic_commit()` call, re-fetch all modified files before referencing them again in the same session. The in-context version and the committed version may differ.

**All commits go to GitHub via `g.atomic_commit()`. Local-only writes are not a valid session close.**

Write YAML resumption block to `session_log_current.md`:
```yaml
session_close: YYYY-MM-DD
last_stage: [stage name]
next_action:
  skill: name
  input_file: filename
  parameters: {}
open_gaps_added: []
editorial_decisions_pending: []
blockers: []
```

## Token Rules
- Never re-read a document already fetched this session. Consume fetched content.
- Never re-run a completed stage. Consume prior results.
- Intermediate work: tables, not prose.
- Context limit approaching → complete current stage → session-close → commit → instruct new chat.
- Chunk all inputs >500 lines before passing to any analysis skill.
