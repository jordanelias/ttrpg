# valoria-compiler

Assemble approved patches, editorial decisions, and structural changes into clean ruleset exports.

**Model:** Sonnet 4.6.
**Input:** `designs/` working documents (source of truth) + `canon/editorial_ledger.yaml` + session log.
**Note:** Compilation is the lowest-priority task. Compile only when a system is stable and explicitly requested. `designs/` is always more current than `compilation/`.

## Term Reference

Read `references/glossary.md` for all term definitions and permitted abbreviations before using any game-specific term or abbreviation.

## Process

### 1. Load Current State
- Read `canon/editorial_ledger.yaml` — check P1-BLOCKER and P1 count.
  - **P1-BLOCKER > 0: BLOCK export.** List blockers. Override: `[COMPILER GATE OVERRIDE: user accepted — date]`
  - **P1 > 0: WARN.** List P1 items. Compilation may proceed with explicit user acknowledgment.
- Identify pending vs. approved patches from session logs and gap register.

### 2. Apply Changes
- Apply in sequential order. Preserve section numbering unless restructuring approved.

### 3. Verify Editorial Cuts
**New — prevents ghost mechanics.** Scan compiled output for any mechanic or subsystem that has been editorially cut. Current cut list:
- Maxims (cut → Beliefs subsume)
- Push (cut → Momentum retained)
- Thread Harvest (struck entirely)
- Virtues & Vices (cut entirely)

If found: remove. Log removal in compilation report.

### 4. Verify Editorial Pending
- Scan for `[EDITORIAL: pending user approval]` flags.
- Do NOT include unapproved editorial content.

### 5. Canonical Header (Mandatory)
Every compiled ruleset begins with:
> *All mechanics derive from the Philosophical Foundations. Where this document conflicts with the Foundations, the Foundations govern.*

### 6. Export
- Output: `compilation/v[N]/valoria_ruleset_v[N].md` — match existing checkpoint naming convention (e.g. compilation/v0.15/)
- Appendix: changes since previous checkpoint
- Appendix: open P1/P2 items from gap register

### 7. Final Canon Guard Pass
- Run canon-guard on compiled output (Sonnet).
- FAIL → revert causing change, flag for review.
- PARTIAL → note in report.

## Compilation Report
```
# Compilation Report — Checkpoint [N]
Date: · Base: Checkpoint [N-1]
Patches applied: [count] · Pending: [count] · Editorial pending: [count]
Cut mechanics verified removed: [list]
Canon Guard: PASS / PARTIAL / FAIL
P1 items: [count]
## Changes Applied
## Pending Editorial
## Canon Guard Notes
```

## Rules
- Never include unapproved editorial content.
- Never alter canonical header or Foundations supremacy clause.
- All output to md.
