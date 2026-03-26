---
name: valoria-compiler
description: >
  Assemble approved mechanical patches, editorial decisions, and structural changes into a clean,
  complete Valoria ruleset export. ALWAYS use this skill when compiling the ruleset, assembling
  changes, exporting a checkpoint, building a new version, applying patches, or producing a
  clean document. Trigger on: "compile the ruleset", "assemble changes", "export", "build checkpoint",
  "apply patches", "produce clean version", "write it up", or when the orchestrator routes assembly.
---

**Model:** Haiku 4.5 for structural assembly. Sonnet 4.6 for final canon-guard pass.
**Input:** Current ruleset (chunked) + `valoria_patch_log.md`.

## Process

### 1. Load Current State
- Read `valoria_section_map.md` for structure
- Read `valoria_patch_log.md` for pending approved patches
- Read `valoria_gap_register_consolidated.md` — check P1 count
  - **If P1 > 0: BLOCK export.** List open P1 items in compilation report. Do not proceed until user explicitly overrides or P1 count reaches 0.
  - Override format: `[COMPILER GATE OVERRIDE: user accepted P1 export with N open P1 items — date]`
- Identify: which patches are approved, which are pending, which are editorial

### 2. Apply Patches
- Apply approved patches in sequential order
- Preserve section numbering unless restructuring is approved
- For each patch applied: mark as APPLIED in patch log with date

### 3. Editorial Content Check
- Scan for any content flagged `[EDITORIAL: pending user approval]`
- Do NOT include unapproved editorial content in compiled output
- List pending editorial items in the compilation report

### 4. Canonical Header (MANDATORY)
Every compiled ruleset MUST begin with:
> *All mechanics derive from the Philosophical Foundations. Where this document conflicts with the Foundations, the Foundations govern.*

### 5. Export
- Output: `valoria_ruleset_checkpoint_[N].md`
- Include Appendix: Patch Log (all changes since previous checkpoint)
- Include Appendix: Open Items (from gap register, P1 and P2 only)

### 6. Final Canon Guard Pass (Sonnet)
- Run valoria-canon-guard on the compiled output
- Any FAIL results: revert the causing patch, flag for review
- Any PARTIAL results: note in compilation report

## Patch Format (standardized)
```markdown
## PATCH [NNN] — [Date]
**Source:** [audit report / simulation finding / user direction]
**Section:** [Part.Section]
**Type:** mechanical / editorial / structural
**Description:** [what changes]
**Old text:** [exact text being replaced — for reversion]
**New text:** [replacement text]
**Canon Guard:** PASS / PARTIAL — [constraint IDs checked]
**Core Principles:** [any affected principle IDs]
**User Approval:** required / not required / approved [date]
**Status:** pending / approved / applied [date] / reverted [date]
```

## Compilation Report Format
```markdown
# Compilation Report — Checkpoint [N]
**Date:** [date]
**Base:** Checkpoint [N-1]
**Patches applied:** [count]
**Patches pending:** [count]
**Editorial items pending:** [count]
**Canon Guard result:** PASS / PARTIAL / FAIL
**Gap register P1 items:** [count]

## Applied Patches
[list with IDs]

## Pending Editorial Decisions
[list with descriptions]

## Canon Guard Notes
[any PARTIAL findings from final pass]
```

## Rules
- Never include unapproved editorial content
- Never alter the canonical header
- Never remove the Foundations supremacy clause
- Preserve section numbering unless explicitly approved for restructuring
- All output to md format
- Keep the patch log append-only (never delete entries; mark reverted if needed)
