# valoria-orchestrator

## Description
Route ALL Valoria project tasks. ALWAYS invoke for ANY request involving:
simulation, combat, threadweaving, social mechanics, mass battle, board game,
hybrid mode, compilation, assembly, checkpoint, audit, consistency, canon,
philosophy, editorial decisions, gap register, patches, stress testing, dice,
probability, coverage, session management, NPC mechanics, faction mechanics,
territory, clocks, or any reference to the Valoria ruleset. This is the
single entry point for all Valoria work — no other skill triggers directly.

## Interface
- Accepts: any user request involving Valoria
- Produces: routed task output, committed to GitHub
- Does NOT delegate commits — all GitHub writes go through orchestrator only
- On-demand skills write to /home/claude/ only; orchestrator commits

---

## Session Start Protocol

Execute in order on every session start:

1. **Bootstrap github_ops.py**
   - Check if `/home/claude/github_ops.py` exists
   - If not: copy from `scripts/github_ops.py` (bundled with this skill)
   - Set `GITHUB_PAT` env var from `references/github_pat.md`

2. **Read session log**
   - `github_ops.read_file("session_log_current.md")`
   - Report status in ≤3 lines: current phase, last action, what's next

3. **Load skill registry**
   - Read `references/skill_registry.md` (local — bundled)
   - Do NOT fetch from GitHub; this is the installed copy

4. **Freshness check**
   - Compare `len(open('scripts/github_ops.py').read())` vs `github_ops.file_size("tools/github_ops.py")`
   - If mismatch: warn "[STALE: bundled github_ops.py differs from GitHub tools/github_ops.py — update skill before next session]"

5. **Confirm task** with user before proceeding

---

## Task Routing

1. Match user request against trigger keywords in `references/skill_registry.md`
2. Declare: skill name · model tier · rationale (one line)
3. Fetch skill SKILL.md from GitHub path in registry:
   ```python
   skill_md = github_ops.read_file("skills/{skill-name}/SKILL.md")
   ```
4. Execute per skill instructions
5. Collect output from `/home/claude/`
6. Commit output + session log update atomically (see Session Close)

**If no skill matches:** handle inline if mechanical/deterministic. Flag [EDITORIAL] if creative.

---

## Canon Gate

**Mandatory before committing any new or changed mechanical content.**

```
1. skill_md = github_ops.read_file("skills/valoria-canon-guard/SKILL.md")
2. Run Mechanical mode on proposed content
3. FAIL   → do not commit; report violation; stop
4. PARTIAL → commit with [CANON-PARTIAL] warning; log in gap register
5. PASS   → proceed to commit
```

---

## Editorial Decision Protocol

When user makes a setting, lore, or design decision:

```
1. skill_md = github_ops.read_file("skills/valoria-editorial-ledger/SKILL.md")
2. Create YAML entry: id, date, category, decision, affects list
3. Run tools/find_references.py to verify affects list completeness
   - Any "found_not_declared" paths must be added to affects before proceeding
4. Run tools/propagator.py for each affected compiled stage
5. Atomic commit: modified stages + updated ledger + session log
6. Confirm: "Decision E-NNN applied to N files. Zero NOT_APPLIED."
```

---

## Patch Protocol

When a mechanical fix is identified (not an editorial decision):

```
1. Create entry in canon/patch_register.yaml (id: PP-NNN, status: approved)
2. If patch changes a value in compiled stages:
   a. Run tools/find_references.py to locate all occurrences
   b. Run tools/propagator.py to apply
3. Run Canon Gate on patched content
4. Atomic commit: patched files + updated register + session log
```

---

## Compiler Pre-flight

Before any compilation run, verify:
- `canon/editorial_ledger.yaml`: zero `NOT_APPLIED` entries → BLOCK if any found
- `canon/patch_register.yaml`: zero `approved` (unapplied) entries → BLOCK if any found
- `valoria_gap_register_consolidated.md`: zero open P1 items → BLOCK (or get user override)

---

## Session Close Protocol

At session end or context limit warning:

```python
import github_ops, datetime

new_current = f"""session_id: {datetime.date.today()}T_{SESSION_LABEL}
phase: {CURRENT_PHASE}
status: CLOSED

## SESSION SUMMARY
### Completed
{BULLET_LIST_OF_COMPLETED_TASKS}

### GitHub state (committed)
{FILES_COMMITTED}

### Resume instruction
{NEXT_ACTION_FOR_NEXT_SESSION}
"""

old_current = github_ops.read_file("session_log_current.md")
old_archive = github_ops.read_file("session_log_archive.md")

github_ops.atomic_commit(
    additions=[
        ("session_log_current.md", new_current),
        ("session_log_archive.md", old_archive + "\n---\n\n" + old_current),
    ],
    deletions=[],
    message="[infrastructure] Session close — {SUMMARY}",
)
```

**Context limit warning:** If approaching context limit mid-session, run Session Close immediately with all completed work, then tell user to start new chat.

---

## Commit Message Convention

```
[scope] description — ID(s)
```

Scopes: `editorial` · `patch` · `compilation` · `simulation` · `infrastructure` · `skill` · `cleanup`
IDs: `E-NNN` (editorial) · `PP-NNN` (patch) · `G-NNN` (gap) · `SIM-NNN` (simulation finding)

Examples:
- `[editorial] Territory names confirmed — E-05`
- `[patch] TD recovery mechanic — PP-001`
- `[compilation] Assemble CP15 — stages 1-17`
- `[simulation] Combat batch 12 — SIM-012-F-01 through F-08`

---

## Error Handling

| Error | Action |
|-------|--------|
| GitHub 401 | Check `references/github_pat.md`. PAT expired — tell user to regenerate. |
| OID mismatch | `github_ops.atomic_commit` retries once automatically. If second fail: report conflict, do not commit partial state. |
| Skill not found on GitHub | Report path, ask user to confirm skill has been built and committed. |
| Canon gate FAIL | Never commit. Report violation with P-0N reference. Wait for user decision. |
| Context limit approaching | Run Session Close immediately. |
