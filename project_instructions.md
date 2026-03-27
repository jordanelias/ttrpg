# VALORIA PROJECT INSTRUCTIONS

## What This Is
Valoria is a TTRPG / board game / hybrid playable in all three modes. This project develops the complete ruleset, audits it against philosophical canon, stress-tests mechanics, and compiles checkpoint editions.

---

## Document Hierarchy (Immutable)
1. `Valoria_Philosophical_Foundations.docx` — metaphysical canon; governs everything
2. `Mechanics.docx` — core mechanical principles and design intent
3. Current ruleset checkpoint — working document; audited against 1–2

Conflicts: higher-ranked document always wins.

---

## GitHub
**Repo:** `jordanelias/ttrpg` · branch `main`
**PAT:** `github_pat_11ACSEXDA0K9O7BaTfn` + `qSe_IvZhgAEv2oUytdU3VaBIoSRqTnKPkTAxy3DtxBQUI0VTCBEO6HLHfWkPNzB` (concatenate both parts)

**Read:**
```
GET https://api.github.com/repos/jordanelias/ttrpg/contents/{path}
Authorization: token {PAT}
```
content field is base64-encoded. Decode before use. Capture `sha` for writes.

**Write:**
```
PUT https://api.github.com/repos/jordanelias/ttrpg/contents/{path}
Authorization: token {PAT}
Body: {"message": "{msg}", "content": "{base64}", "sha": "{sha}"}
```
Always GET before PUT. SHA not required for new files. On 409: re-GET, retry once. On failure: output fenced block with manual paste instructions. Never silently drop state.

**Discipline:** Finalize before pushing. One push per file per session. No revision commits. Read/write files on an as-needed basis only — never bulk-load GitHub at session start or speculatively.

---

## Session Start Protocol
On every session start, read these three files from GitHub and nothing else:

1. `session_log_current.md` — report status in ≤3 lines
2. `valoria_gap_register_consolidated.md` — report P1 count only
3. `valoria_comprehensive_workplan.md` — report current phase and active stage only

Then: confirm task with user. Produce model routing table. Render the router artifact (see below).

All other files (compilation stages, canon constraints, test files, editorial register, NPC details, faction data) are fetched only when a specific task requires them.

---

## Model Routing

| Task Type | Model |
|-----------|-------|
| Document chunking, indexing, header extraction, cross-reference listing | Haiku 4.5 |
| Format fixes, formula transcription, consistency repair (pattern matching) | Haiku 4.5 |
| Mechanical gap-fill, canon compliance, stress testing, simulation | Sonnet 4.6 |
| Mechanical audit, interaction analysis, gap register updates | Sonnet 4.6 |
| Compilation assembly (merging sources, resolving integration conflicts) | Sonnet 4.6 |
| Editorial content, NPC/faction/setting authorship, design ambiguity resolution | Opus 4.6 |
| Philosophy-heavy new mechanic design, worldbuilding, tone/voice work | Opus 4.6 |

**Routing protocol:**
- Assess task tier BEFORE executing anything.
- For tasks in the current session's model tier: execute directly.
- For tasks requiring a different tier: use the inline router artifact — do not defer, do not request a new session.
- When multiple sub-tasks exist: produce a routing table, then execute in-tier tasks directly and route off-tier tasks through the artifact.

---

## Inline Model Router Artifact
Render at every session start using `visualize:show_widget`. The artifact lets Haiku and Opus tasks run inline without branching sessions.

**Models:**
- Haiku: `claude-haiku-4-5-20251001`
- Sonnet: `claude-sonnet-4-20250514`
- Opus: `claude-opus-4-6`

**Artifact code** is stored at `tools/model_router.html` on GitHub. Read and render it at session start.

---

## Editorial Gate
User approves all: setting, worldbuilding, character content, narrative, tone, faction behavior, design intent resolution, ambiguous calls.

Claude executes without approval: formula fixes, consistency repairs, format changes, audits, simulations, gap register updates.

Flag format: `[EDITORIAL: requires user approval — description]`

---

## Session Close Protocol
1. Replace `session_log_current.md` with session-close YAML (completed stages, gap register delta, commits, next action).
2. Append previous current block to `session_log_archive.md`.
3. Update `valoria_gap_register_consolidated.md` if changed.
4. Push all changed files. One commit per file.

---

## Token Efficiency
- Never re-read already-fetched documents within a session.
- Never re-run completed stages.
- Intermediate work: tables, not prose. Final outputs as documents.
- Chunk inputs >500 lines before analyzing (use valoria-chunker skill).
- Session log: read ONLY `session_log_current.md` on resume. Never the archive.
- Fetch files on demand. Never speculatively load GitHub content.
