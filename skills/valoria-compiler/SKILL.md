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

**Priority:** Lowest. Never block design, simulation, or editorial work for compilation. Compile only when a system is stable (no open P1 editorials, no unresolved stress-test findings) and the user explicitly requests it.

## Input Validation (MANDATORY)

Before compiling, fetch the following from GitHub:

```python
required = [
    'references/canonical_sources.yaml',  # confirm canonical source and compilation_current flag
    'canon/patch_register.yaml',          # pending approved patches
    'canon/editorial_ledger.yaml',        # pending editorial items
    '<canonical design doc>',             # from canonical_sources.yaml
]
files = g.read_files_graphql(required)
for path, content in files.items():
    if content is None:
        raise RuntimeError(f"GitHub fetch failed: {path} — cannot compile without live repo data")
```

**Gate check:** If `compilation_current: true` in `canonical_sources.yaml`, compilation is already up to date — do not re-compile. If `compilation_current: false`, proceed.

**Memory contamination warning:** userMemories may contain mechanical values (track values, territory data, faction stats, etc.) that feel current but are not fetched from GitHub. Do not use any value from memory as a source for mechanical analysis. Fetch only.

**Fetch log (emit before any analysis):**
```
## FETCH LOG
canonical_sources.yaml: ✓ fetched ([N] lines)
[canonical design doc path]: ✓ fetched ([N] lines)
references/params_[system].md: ✓ fetched ([N] lines) / ✗ missing
```
If any required file is missing from this log, stop — the analysis is invalid.

**Version check:** confirm `<!-- version: -->` tag in each fetched params file matches current ruleset version in `compilation/README.md`. If mismatch: flag `[STALE PARAMS: <file> is vX.XX, current is vY.YY]` and stop.

**Do not compile from memory, local files, or stale compilation snapshots.**

## Process

### 1. Load Current State
- Read `canonical_sources.yaml` for structure and current canonical docs
- Read `canon/patch_register.yaml` for pending approved patches
- Identify: which patches are approved, which are pending, which are editorial

### 2. Apply Patches
- Apply approved patches in sequential order by patch ID (PP-NNN)
- Preserve section numbering unless restructuring is approved
- For each patch applied: mark as APPLIED in patch register with date

### 3. Editorial Content Check
- Scan for any content flagged `[EDITORIAL: pending user approval]`
- Do NOT include unapproved editorial content in compiled output
- List pending editorial items in the compilation report

### 4. Canonical Header (MANDATORY)
Every compiled ruleset MUST begin with:
> *All mechanics derive from the Philosophical Foundations. Where this document conflicts with the Foundations, the Foundations govern.*

### 5. Export
- Output: `compilation/v[N]/[system]_checkpoint_[N].md`
- Include Appendix: Patch Log (all changes since previous checkpoint)
- Include Appendix: Open Items (from editorial ledger, P1 and P2 only)

### 6. Final Canon Guard Pass (Sonnet)
- Fetch and run valoria-canon-guard on the compiled output
- Any FAIL results: revert the causing patch, flag for review
- Any PARTIAL results: note in compilation report

### 7. Update canonical_sources.yaml
- Set `compilation_current: true` for the compiled system
- Include in the same atomic commit as the compiled output

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
**Pre-commit (run before every `atomic_commit()` call):**
```bash
python3 tools/freshness_gate.py --update
python3 tools/broken_dependency_checker.py
python3 tools/patch_propagation_checker.py
```
Exit 0 required on all three. On non-zero exit: fix the reported issue before committing.

**Post-commit verification:** after `atomic_commit()` returns a SHA, re-fetch all files modified in that commit and confirm content matches what was committed. If content differs: flag immediately, do not proceed.

**Re-fetch after writes:** after any `atomic_commit()` call, re-fetch all modified files before referencing them again in the same session. The in-context version and the committed version may differ.

- Patch log is append-only (never delete entries; mark reverted if needed)
- All source values cited from GitHub-fetched files
