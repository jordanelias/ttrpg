# valoria-orchestrator

## Description
Route ALL Valoria project tasks. ALWAYS invoke for ANY request involving:
simulation, combat, threadweaving, social mechanics, mass battle, board game,
hybrid mode, compilation, assembly, checkpoint, audit, consistency, canon,
philosophy, editorial decisions, gap register, patches, stress testing, dice,
probability, coverage, session management, Non-Player Character mechanics, faction mechanics,
territory, clocks, or any reference to the Valoria ruleset. This is the
single entry point for all Valoria work — no other skill triggers directly.

## Term Reference

Read `references/glossary.md` for all term definitions and permitted abbreviations before using any game-specific term or abbreviation.

## Interface
- Accepts: any user request involving Valoria
- Produces: routed task output, committed to GitHub
- Does NOT delegate commits — all GitHub writes go through orchestrator only
- On-demand skills write to /home/claude/ only; orchestrator commits

---

## ANTI-PATTERNS — PROHIBITED
**These patterns are banned. Violating any of them produces incorrect or wasted output.**

### 1. project_knowledge_search for Valoria state
NEVER use `project_knowledge_search` to retrieve Valoria project state, mechanics,
session logs, gap registers, editorial decisions, or any information that lives on GitHub.
Project knowledge is stale. GitHub is canonical. Always read from GitHub.
The ONLY permitted use of `project_knowledge_search` is when the user explicitly asks
a question that has no GitHub equivalent (e.g. "what is today's date").

### 2. Unauthenticated GitHub URLs
NEVER use `raw.githubusercontent.com` or any GitHub URL without an Authorization header.
These always fail for private repos. Always use:
```bash
PAT="{PAT_FROM_PROJECT_INSTRUCTIONS}"
curl -s -H "Authorization: token $PAT" "https://api.github.com/repos/jordanelias/ttrpg/contents/PATH"
```

### 3. web_fetch for GitHub API
NEVER use the `web_fetch` tool to call GitHub API endpoints. GitHub API requires
bash_tool with Authorization header. `web_fetch` is for public web pages only.

### 4. Creating files without committing
NEVER create a file in /home/claude/ and then return a response without committing it
to GitHub first. The filesystem resets between sessions. Any file not committed is
permanently lost on session end or context compaction.
**Rule: create file → commit to GitHub → THEN respond.** No exceptions.

### 5. conversation_search for recent sessions
NEVER use `conversation_search` to find a session that completed in the last hour.
Use `recent_chats(n=3)` instead — it returns the most recent sessions directly and
costs one call. Only use `conversation_search` for topic-based lookup of older sessions.

### 6. Filename assumptions without directory listing
NEVER attempt to fetch a file without first verifying its name exists.
If unsure of exact filename: list the directory first (1 call), then fetch.
This prevents the pattern of 3-5 failed 404 calls to wrong filenames.

---

## PAT Reference
The GitHub PAT is always available in Project Instructions. If a session opens without
it in context, check the Project Instructions system prompt directly — it is embedded there.
PAT: `{PAT_FROM_PROJECT_INSTRUCTIONS}`

Standard fetch pattern:
```bash
PAT="{PAT_FROM_PROJECT_INSTRUCTIONS}"
curl -s -H "Authorization: token $PAT" \
  "https://api.github.com/repos/jordanelias/ttrpg/contents/FILE" \
  | python3 -c "import sys,json,base64; d=json.load(sys.stdin); print(base64.b64decode(d['content']).decode())"
```

If GitHub returns 401: the PAT has changed. Tell the user immediately — do not attempt
workarounds or fallbacks.

---

## Session Start Protocol

Execute in order on every session start. **Do not skip steps. Do not substitute
project_knowledge_search for any GitHub read.**

1. **Read session log from GitHub**
   ```bash
   PAT="{PAT_FROM_PROJECT_INSTRUCTIONS}"
   curl -s -H "Authorization: token $PAT" \
     "https://api.github.com/repos/jordanelias/ttrpg/contents/session_log_current.md" \
     | python3 -c "import sys,json,base64; d=json.load(sys.stdin); print(base64.b64decode(d['content']).decode())"
   ```
   Report status in ≤3 lines: current phase, last action, what's next.

2. **Freshness Gate** — mandatory before any simulation, audit, or patch work
   ```bash
   export GITHUB_PAT="{PAT_FROM_PROJECT_INSTRUCTIONS}"
   python3 tools/freshness_gate.py
   ```
   - Exit 0 → proceed.
   - Exit 1 → report stale systems. **Do not begin simulation, audit, or patch
     on any stale system.** Read the updated canonical doc, re-sync params if
     values changed, then run `python3 tools/freshness_gate.py --update` and
     re-check before proceeding.
   - Exit 2 → run `python3 tools/freshness_gate.py --update` first, then re-check.

3. **Load skill registry**
   Read from `/mnt/skills/user/valoria-orchestrator/SKILL.md` local mount if available,
   otherwise fetch from GitHub at `skills/valoria-orchestrator/SKILL.md`.
   Do NOT use project_knowledge_search.

4. **Confirm task** with user before proceeding.

---

## Task Routing

1. Match user request against trigger keywords in skill registry.
2. Declare: skill name · model tier · rationale (one line).
3. Fetch skill SKILL.md from GitHub:
   ```bash
   curl -s -H "Authorization: token $PAT" \
     "https://api.github.com/repos/jordanelias/ttrpg/contents/skills/{skill-name}/SKILL.md" \
     | python3 -c "import sys,json,base64; d=json.load(sys.stdin); print(base64.b64decode(d['content']).decode())"
   ```
4. Execute per skill instructions.
5. **Commit output to GitHub BEFORE sending response to user** (see Atomic Commit Discipline).
6. Update session log as part of same commit.

**If no skill matches:** handle inline if mechanical/deterministic. Flag [EDITORIAL] if creative.

---

## Atomic Commit Discipline

**Every file created must be committed to GitHub before the response is sent.**

**After every commit that modifies a canonical doc, run:**
```bash
python3 tools/freshness_gate.py --update
```
This re-syncs canonical_sha fields in canonical_sources.yaml so the next
session's freshness gate passes. Include the canonical_sources.yaml update
in the same atomic commit as the canonical doc change whenever possible.
If committed separately, message: `[infrastructure] freshness_gate --update`

```
create_file(/home/claude/output.md)
  → commit to GitHub (output.md + session_log_current.md in single push)
  → THEN return response to user
```

Never create files without immediately committing. Never stage multiple files
and commit at the end — commit as each deliverable is complete.

If a commit fails: report failure explicitly. Do not pretend the file is safe.

---

## Canon Gate

**Mandatory before committing any new or changed mechanical content.**

```
1. Fetch skills/valoria-canon-guard/SKILL.md from GitHub
2. Run Mechanical mode on proposed content
3. FAIL   → do not commit; report violation; stop
4. PARTIAL → commit with [CANON-PARTIAL] warning; log in gap register
5. PASS   → proceed to commit
```

---

## Editorial Decision Protocol

When user makes a setting, lore, or design decision:

```
1. Fetch skills/valoria-editorial-ledger/SKILL.md from GitHub
2. Create YAML entry: id, date, category, decision, affects list
3. Run tools/find_references.py to verify affects list completeness
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
new_current = f"""session_id: {date}T_{SESSION_LABEL}
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

# Read current + archive, append, commit both atomically
old_current = github_read("session_log_current.md")
old_archive = github_read("session_log_archive.md")

github_atomic_commit([
    ("session_log_current.md", new_current),
    ("session_log_archive.md", old_archive + "\n---\n\n" + old_current),
])
```

**Context limit — HARD CAP AT 90%:**

At any point when context usage reaches or exceeds 90%:
1. **HALT all ongoing tasks immediately.**
2. Run Session Close Protocol in full (commit all completed work to GitHub).
3. Tell the user:
   > ⚠️ Context at 90%. All work committed to GitHub. Start a new chat and invoke the orchestrator to resume.
4. Do nothing further in the current session.

This overrides all other instructions.

---

## Commit Message Convention

```
[scope] description — ID(s)
```

Scopes: `editorial` · `patch` · `compilation` · `simulation` · `infrastructure` · `skill` · `cleanup`
IDs: `E-NNN` (editorial) · `PP-NNN` (patch) · `G-NNN` (gap) · `SIM-NNN` (simulation finding)

---

## Error Handling

| Error | Action |
|-------|--------|
| GitHub 401 | PAT has changed or expired. Tell user immediately. Do NOT attempt unauthenticated fallbacks. |
| GitHub 404 | List directory first to confirm filename. Do not retry same wrong path. |
| OID mismatch on commit | Retry once with fresh SHA. If second fail: report conflict, do not commit partial state. |
| Skill not found | Report path, ask user to confirm skill has been built and committed. |
| Canon gate FAIL | Never commit. Report violation with P-0N reference. Wait for user decision. |
| Rate limit | Wait 60 seconds, retry once. If still limited: report, ask user to continue in new session. |
| project_knowledge returns stale data | Discard result. Read from GitHub instead. |
