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

## MANDATORY MODEL ROUTING — READ BEFORE ANY WORK

Every task MUST be assessed for minimum-viable model BEFORE execution. This is non-negotiable.

### Model Assignment Table

| Task Type | Model | Rationale |
|-----------|-------|-----------|
| Document chunking, indexing, section extraction | Haiku 4.5 | Structural; no reasoning required |
| Format fixes, cross-reference insertion, table formatting | Haiku 4.5 | Mechanical transcription |
| Formula transcription from design docs to ruleset | Haiku 4.5 | Copy + format |
| Consistency repair (wrong numbers, broken refs) | Haiku 4.5 | Pattern matching |
| Mechanical gap-fill (known constraints, no ambiguity) | Sonnet 4.6 | Structured reasoning within bounds |
| Canon compliance checking | Sonnet 4.6 | Requires philosophical judgment |
| Stress testing / simulation | Sonnet 4.6 | Requires scenario reasoning |
| Mechanical audit (interaction analysis, gap detection) | Sonnet 4.6 | Requires system-level reasoning |
| Editorial-adjacent design (faction cards, NPCs, setting) | Opus 4.6 | Requires creative + philosophical judgment |
| Ambiguous design intent resolution | Opus 4.6 | Requires deep contextual reasoning |
| Philosophy-heavy new mechanic design | Opus 4.6 | Requires Foundations interpretation |

### Routing Protocol
1. Assess task complexity BEFORE starting.
2. If task can be done by Haiku: say so. Suggest user switch model or flag for batch.
3. If task can be done by Sonnet: say so. Suggest user switch model.
4. If task requires Opus: proceed, but note why.
5. **NEVER run Haiku-tier work on Opus.** Flag it and refuse to execute inline.
6. When multiple sub-tasks exist, produce a routing table showing each sub-task's assigned model.

### Skill Delegation Protocol
Skills exist to be used. Every multi-step task MUST be decomposed into skill calls:

| Skill | Model | Trigger |
|-------|-------|---------|
| valoria-chunker | Haiku 4.5 | Any input >500 lines |
| valoria-canon-guard | Sonnet 4.6 | Any new mechanic, any audit finding, any compilation stage |
| valoria-mechanic-audit | Sonnet 4.6 | Any consistency question, gap detection, formula check |
| valoria-simulator | Sonnet 4.6 | Any "does this work" question, stress test, edge case |
| valoria-compiler | Haiku 4.5 / Sonnet 4.6 | Any assembly, patching, checkpoint export |

**Anti-pattern: doing skill work inline on Opus.** If the orchestrator catches itself about to do chunking, formula checking, or structural assembly inline, STOP and route to the appropriate skill + model.

## Session Start Protocol
1. Read `session_log_current.md` (NOT the full log — that's the archive).
2. Read `valoria_gap_register_consolidated.md` — P1 count only.
3. Report status in ≤3 lines. Confirm task.
4. Produce routing table for the session's work before executing anything.

## Canonical Hierarchy (immutable)
1. `Valoria_Philosophical_Foundations.docx` — governs everything
2. `Mechanics.docx` — governs mechanical design intent
3. Current ruleset checkpoint — working document; subject to audit against 1–2

If conflict: higher-ranked document wins. Always.

## Editorial Gate (MANDATORY)
**User retains exclusive authority over:**
- Setting, context, worldbuilding decisions
- Character names, personalities, motivations, backstories
- Narrative events, faction behaviors, plot directions
- Tone, theme, aesthetic decisions
- Resolution of ambiguous design intent from Mechanics.docx

**Flag format:** `[EDITORIAL: requires user approval — brief description]`

**Claude may execute without approval:**
- Mechanical formula corrections (verified against Foundations + core principles)
- Internal consistency fixes (math errors, wrong cross-references)
- Formatting, structural reorganization
- Simulation and audit reports

No editorial content proceeds without explicit user sign-off.

## Workflows

**Full Mechanical Audit**
chunker (A, C, E) → canon-guard → mechanic-audit (A–E) → gap register update → findings report

**Philosophy Compliance Check**
chunker (target section) → canon-guard

**Stress Test Suite**
chunker (target mechanics + dependencies) → simulator (Mode A then D) → findings report

**Comprehensive Simulation**
chunker (A–E) → simulator (E: coverage matrix) → simulator (A: isolation) → simulator (B: interactions) → simulator (C: scenarios) → simulator (D: edge cases) → coverage update → report

**Targeted Repair**
canon-guard → mechanic-audit → [EDITORIAL GATE if content] → compiler

**New Mechanic Development**
canon-guard (pre-check) → mechanic-audit (integration) → simulator (stress test) → [EDITORIAL GATE] → compiler

**Ruleset Assembly (Phase 2)**
chunker → compiler → canon-guard (final pass) → export checkpoint

**Board/VG Mode Development**
chunker (Foundations §21–23) → canon-guard (constraints) → [EDITORIAL GATE: user designs] → mechanic-audit → simulator → compiler

## Session Close Protocol
Write YAML block to `session_log_current.md` (replace, not append).
Append previous current block to `session_log_archive.md`.

```yaml
session_close: YYYY-MM-DD
checkpoint: [N]
completed_stages: []
next_action:
  skill: name
  model: [required model]
  input_file: filename
  parameters: {}
open_gaps_added: []
editorial_decisions_pending: []
blockers: []
model_routing_notes: "summary of model assignments used this session"
```

## Token Rules
- Never re-read a document already chunked this session. Consume chunk outputs.
- Never re-run a completed stage. Consume prior results.
- Intermediate work: tables, not prose.
- Context limit approaching → complete current stage → session-close → instruct new chat.
- Chunk all inputs >500 lines before passing to any analysis skill.
- **Finalize files locally before pushing to GitHub. One push per file per session.**
- **Session log: read only `session_log_current.md`. Never read the archive on resume.**

## GitHub Protocol
- GET before PUT (capture SHA).
- Finalize content before committing. No revision commits.
- New files: no SHA needed.
- On 409: re-GET, retry once. On failure: output as fenced code block.
- One commit per file per session unless content genuinely changes between stages.
