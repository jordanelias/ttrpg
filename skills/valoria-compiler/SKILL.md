---
name: valoria-compiler
description: >
  Assemble approved mechanical patches, editorial decisions, and structural changes into a clean,
  complete Valoria ruleset export. ALWAYS use this skill when compiling the ruleset, assembling
  changes, exporting a checkpoint, building a new version, applying patches, or producing a
  clean document. Trigger on: "compile the ruleset", "assemble changes", "export", "build checkpoint",
  "apply patches", "produce clean version", "write it up", or when the orchestrator routes assembly.
---

**Priority:** Lowest. Never block design, simulation, or editorial work for compilation. Compile only when a system is stable (no open P1 editorials, no unresolved stress-test findings) and the user explicitly requests it.

## Input Validation (MANDATORY)

Before compiling, read the following from the working tree:

- `references/canonical_sources.yaml` — confirm canonical source path
- `canon/patch_register_active.yaml` — pending approved patches
- `canon/editorial_ledger.jsonl` (pre-cutover flat-ID items) plus every existing
  `canon/editorial_ledger_<lane>.jsonl` relevant to the target system (see
  `valoria-editorial-register`'s ID Law section for the lane roster) — **not**
  `canon/editorial_ledger.yaml`, which does not exist
- the canonical design doc named in `canonical_sources.yaml`, and its `## Status:` line

If any of these paths is missing, stop — cannot compile without the repo data.

**Gate check:** `references/canonical_sources.yaml` has no `compilation_current` field (that
schema was never migrated into the live file — do not look for it). Currency is read from the
target doc's own `## Status:` line instead (CLAUDE.md §4): if it already reads `CANONICAL` and
no approved patches/editorial items are pending against it, compilation is already up to date —
report that and stop. Otherwise proceed.

## Process

### 1. Load Current State
- Read `canonical_sources.yaml` for structure and current canonical docs
- Read `canon/patch_register_active.yaml` for pending approved patches
- Identify: which patches are approved, which are pending, which are editorial

### 2. Apply Patches
- Apply approved patches in sequential order by patch ID (PP-NNN)
- Preserve section numbering unless restructuring is approved
- For each patch applied: mark as APPLIED in patch register with date
- If this compilation pass itself needs to allocate a new `PP-NNN` (e.g. to record a
  restructuring patch), follow `valoria-editorial-register`'s PP Number Collision Guard —
  re-read `references/id_reservations.yaml`'s live `next_free` immediately before assigning,
  never reuse a cached value

### 3. Editorial Content Check
- Scan for any content flagged `[EDITORIAL: pending user approval]`
- Do NOT include unapproved editorial content in compiled output
- List pending editorial items in the compilation report

### 4. Canonical Header (MANDATORY)
Every compiled ruleset MUST begin with:
> *All mechanics derive from the Philosophical Foundations. Where this document conflicts with the Foundations, the Foundations govern.*

### 5. Export

There is no live `compilation/` directory in this repo — nothing reads or writes one; do not
create it. Two supported output modes instead, chosen by what the user actually asked for:

- **In-place ratification (the common case, per CLAUDE.md §2's ED-1094 convention):** edit the
  canonical design doc directly with the applied patches, flip its `## Status:` line
  `PROPOSED`/`provisional` → `CANONICAL` (or leave it as-is if it was already canonical and this
  pass only applied incremental patches), flip the corresponding ED ledger entry/entries'
  `status` field, and update `CURRENT.md`'s row for that subsystem — all in the same commit. Do
  not leave a doc's contents ratified while its `## Status:` line still says otherwise; that
  silent-mismatch failure mode is exactly what ED-1094 exists to close.
- **Full clean export (only when explicitly requested — a standalone flattened artifact
  separate from the live canonical doc):** output to
  `designs/audit/<date>-compilation-export/<system>_export.md`, matching the dated-folder
  convention every other audit-producing skill uses (`designs/audit/<date>-<topic>/`).
- Both modes: include Appendix: Patch Log (all changes since the previous compilation of this
  system) and Appendix: Open Items (from the editorial ledger, P1 and P2 only).

### 6. Final Canon Guard Pass (Sonnet)
- Run valoria-canon-guard on the compiled output
- Any FAIL results: revert the causing patch, flag for review
- Any PARTIAL results: note in compilation report

### 7. Ratification Bookkeeping
- For in-place ratification: confirm the doc's `## Status:` line, the ED ledger entry/entries,
  and `CURRENT.md` were all updated in the same commit as the compiled content (step 5) — this
  is the loud, non-silent form ED-1094 requires; do not bundle a held-back item into this commit
  without flagging it prominently in the commit/PR body as *not* ratified.
- For a full clean export: no `## Status:` or `CURRENT.md` change is implied by the export
  itself (the live canonical doc is unchanged) — only note the export's existence and location.

## Patch Format (standardized)
```markdown
## PATCH [NNN] — [Date]
**Source:** [audit report / simulation finding / user direction]
**Section:** [Part.Section]
**Type:** mechanical / editorial / structural
**Description:** [what changes]
**Old text:** [exact text being replaced]
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

**Post-commit verification:** after committing, re-read all modified files from the working tree and confirm content matches what was committed. If content differs: flag immediately, do not proceed.

- Patch log is append-only (never delete entries; mark reverted if needed)
- All source values cited from working-tree files
