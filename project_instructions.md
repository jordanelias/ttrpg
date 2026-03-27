# VALORIA PROJECT INSTRUCTIONS

Valoria is a TTRPG / board game / hybrid. This project develops, audits, stress-tests, and compiles the complete ruleset against philosophical canon.

## Architecture

**Persistent state:** GitHub repo `jordanelias/ttrpg`, branch `main`.
**Source documents:** Project Files (`/mnt/project/`) — read-only, may be stale.
**Skills:** GitHub `skills/` directory — read at session start via API. Do not use `/mnt/skills/user/` copies (may be stale).

**File precedence:** If a file exists in both Project Files and GitHub, compare sizes. Use whichever is larger (more recent). When in doubt, use GitHub.

## GitHub API

**PAT:** Provided in the Claude Project system prompt. Do not commit to GitHub.

**Read:** `GET https://api.github.com/repos/jordanelias/ttrpg/contents/{path}` — decode base64 `content` field. Capture `sha` for writes.
**Write:** `PUT` same endpoint — body: `{"message":"...","content":"{base64}","sha":"{current sha}"}`. Always GET immediately before PUT. No SHA for new files. On 409: re-GET, retry once. On failure: output as fenced code block.
**Commit discipline:** Finalize locally. One push per file per session. No revision commits.

## Document Hierarchy (Immutable)

1. `Valoria_Philosophical_Foundations.docx` — metaphysical canon; governs everything
2. `Mechanics.docx` — core mechanical principles; original edition
3. Current ruleset checkpoint — working document; subject to audit against 1–2

Higher-ranked document wins on conflict. Always.

## Editorial Control

**User approves:** setting, worldbuilding, characters, narrative, tone, faction behavior, ambiguous design intent.
**Claude executes without approval:** formula fixes, consistency repairs, formatting, audits, simulations.
**Flag:** `[EDITORIAL: requires user approval — description]`

## Model Routing — Non-Negotiable

Assess minimum-viable model BEFORE executing. Flag mismatches. Never run cheap work on expensive models.

| Tier | Tasks |
|------|-------|
| Haiku 4.5 | Chunking, indexing, format fixes, cross-refs, formula transcription, consistency repair |
| Sonnet 4.6 | Canon compliance, stress testing, mechanical audit, gap-fill, compilation assembly |
| Opus 4.6 | Editorial-adjacent design, ambiguous intent resolution, philosophy-heavy new mechanics |

## Session Protocol

1. **Start:** Read skills from GitHub `skills/`. Read `session_log_current.md` from GitHub. Report status ≤3 lines. Read `valoria_gap_register_consolidated.md` — P1 count only. Confirm task. Produce routing table.
2. **Work:** Execute via skill workflows. Checkpoint after each stage.
3. **End:** Archive previous `session_log_current.md` content to `session_log_archive.md`. Replace `session_log_current.md` with session-close YAML. Update gap register if changed.
4. **Context limit:** Complete current stage → session-close → instruct new chat.

## Token Rules

- Chunk before analyzing (>500 lines → chunker first)
- Never re-read already-chunked documents within a session
- Never re-run completed stages
- Intermediate work: tables, not prose
- Session log: read ONLY `session_log_current.md`. Never the archive.

## Key File Locations (GitHub)

| File | Path |
|------|------|
| Session state | `session_log_current.md` |
| Session archive | `session_log_archive.md` |
| Gap register | `valoria_gap_register_consolidated.md` |
| Workplan | `valoria_comprehensive_workplan.md` |
| Canon constraints | `canon/canon_constraints.md` |
| Timeline | `canon/valoria_canonical_timeline.md` |
| Design batches | `designs/` |
| Compilation stages | `compilation/` |
| Skills | `skills/` |
| Test results + coverage matrix | `tests/` |
| Coverage matrix (canonical) | `sim_coverage_matrix.md` (root) |
