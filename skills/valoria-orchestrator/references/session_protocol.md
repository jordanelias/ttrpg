# Session Protocol

## Start
1. Bootstrap github_ops.py (copy from scripts/ if absent, set GITHUB_PAT)
2. Read session_log_current.md from GitHub
3. Load references/skill_registry.md (local)
4. Freshness check: compare bundled vs GitHub github_ops.py size
5. Report status ≤3 lines. Confirm task.

## During Session
- Scope → Plan → Execute → Verify on every task
- Checkpoint after each skill execution (commit output before starting next task)
- If context window is filling: run Session Close immediately, tell user to start new chat
- Never hold uncommitted output across a context reset

## Close
1. Write YAML block to session_log_current.md
2. Append old current to session_log_archive.md
3. Atomic commit: both log files + any pending output

## YAML Block Schema
```yaml
session_id: YYYY-MM-DDT_LABEL
phase: Phase N (description)
status: CLOSED

## SESSION SUMMARY
### Completed
- item 1
- item 2

### GitHub state (committed)
- file: description

### Resume instruction
{one paragraph: what to do next session, which skill, which task}
```
