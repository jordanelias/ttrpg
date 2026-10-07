---
name: valoria-compiler
description: >
  Assemble approved mechanical patches, editorial decisions, and structural changes into a clean,
  complete Valoria ruleset export. ALWAYS use this skill when compiling the ruleset, assembling
  changes, exporting a checkpoint, building a new version, applying patches, or producing a
  clean document. Trigger on: "compile the ruleset", "assemble changes", "export", "build checkpoint",
  "apply patches", "produce clean version", "write it up", or when the orchestrator routes assembly.
---

**Priority:** lowest; never block design, simulation or editorial work for it. Compile only when
the user asks and the system is stable (no open P1 editorials, no unresolved stress-test findings).

## Input Validation (MANDATORY)

Read from the working tree; if any is missing, stop:

- `references/canonical_sources.yaml` — the canonical source path
- `registers/patch_register_active.yaml` — pending approved patches
- `registers/editorial_ledger.jsonl` (flat-ID items) and each `registers/editorial_ledger_<lane>.jsonl`
  relevant to the target (lane roster: `valoria-editorial-register`'s ID Law section)
- the canonical design doc and its `## Status:` line

**Gate check:** currency is the target doc's `## Status:` line (CLAUDE.md §4), not a
`canonical_sources.yaml` field. If it reads `CANONICAL` and no approved patches or editorial items
are pending against it, report it up to date and stop.

## Process

1. **Load current state.** Classify each item from the files above: approved patch, pending patch,
   editorial.
2. **Apply patches** in PP-NNN order; mark each APPLIED, with date, in the patch register. Preserve
   section numbering unless restructuring is approved. If this pass must allocate a new `PP-NNN`
   (e.g. to record a restructuring patch), follow `valoria-editorial-register`'s PP Number
   Collision Guard: re-read `references/id_reservations.yaml`'s live `next_free` immediately before
   assigning, never a cached value.
3. **Editorial check.** Never include unapproved editorial content. Scan for content flagged
   `[EDITORIAL: pending user approval]`; list pending items in the compilation report.
4. **Canonical header (MANDATORY).** Every compiled ruleset begins with, unaltered:
   > *All mechanics derive from the Philosophical Foundations. Where this document conflicts with the Foundations, the Foundations govern.*
5. **Export**, in the mode the user asked for. Never create a `compilation/` or standing export directory.
   - **In-place ratification (default; CLAUDE.md §2, ED-1094):** in one commit, edit the canonical
     doc with the applied patches, flip its `## Status:` `PROPOSED`/`provisional` → `CANONICAL`
     (already canonical: leave it), flip the ED ledger entries' `status`, and update `CURRENT.md`'s
     row. Never leave contents ratified under a `## Status:` line that says otherwise.
   - **Full clean export (explicit request only):** a standalone flattened `<system>_export.md` at
     the path the user names.
   - Both: append Appendix: Patch Log (all changes since this system's previous compilation) and
     Appendix: Open Items (editorial ledger, P1 and P2 only).
6. **Final canon-guard pass (Sonnet).** Run `valoria-canon-guard` on the output. FAIL: revert the
   causing patch and flag for review. PARTIAL: note in the compilation report.
7. **Ratification check.** In-place: confirm the `## Status:` line, ED ledger entries and
   `CURRENT.md` changed in the commit carrying the content. Do not bundle a held-back item into it
   unless flagged prominently in the commit/PR body as *not* ratified. Full export: no `## Status:`
   or `CURRENT.md` change; note the export's existence and location in the compilation report.

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
- Output is markdown.
- The patch log is append-only: mark entries reverted, never delete them.
- Cite every source value from working-tree files.
- After committing, re-read every modified file from the working tree; if it differs from what was
  committed, flag it and stop.
