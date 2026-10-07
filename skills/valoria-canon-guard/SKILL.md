---
name: valoria-canon-guard
description: >
  Validate any Valoria mechanical proposal, existing mechanic, or content element against the
  Philosophical Foundations document. ALWAYS use this skill when checking philosophy compliance,
  evaluating new mechanic proposals, auditing existing mechanics for philosophical fidelity,
  or when any Valoria skill produces a finding that needs canon verification. Trigger on:
  "check philosophy", "canon check", "does this violate the foundations", "philosophy compliance",
  "is this consistent with the philosophy", any new mechanic proposal, any audit finding requiring
  philosophical validation, or whenever the orchestrator routes a compliance check. This skill NEVER
  approves content that contradicts the Foundations.
---

## Input Validation (MANDATORY BEFORE ANY COMPLIANCE CHECK)

Read from the working tree, never memory; cite Foundations text and values (P-15 especially) from them:

- `canon/00_philosophical_foundations_rules.md` — primary authority
- `canon/02_canon_constraints.md` — constraints P-01–P-15; each row's Violation Test column is the test
- any `canon/01_*.md` amendment relevant to the target system

## Process
1. Load the relevant Foundations section (chunk reference or direct read).
2. Score each applicable constraint. Philosophy governs mechanics: soundness never rescues a violation.
   - **PASS** — satisfied.
   - **PARTIAL** — state what is missing and its severity (cosmetic / structural). If unsure, PARTIAL.
   - **FAIL** — cite the Foundations section, give the philosophical reasoning, propose a repair.

## Output Format
```markdown
# Canon Guard Report — [Mechanic/Section Name]
## Source: [chunk reference or design doc path]
## Verdict: PASS / PARTIAL / FAIL

| Constraint | Status | Note |
|-----------|--------|------|
| P-01 | ✓ / ⚠ / ✗ | [brief] |
...

## Violations (if any)
### [ID]: [Brief description]
**Foundations ref:** §[N], key concept [cite from the working-tree file]
**Current implementation:** [what the mechanic does]
**Why this violates:** [philosophical reasoning]
**Proposed repair:** [mechanical suggestion]
**Editorial flag:** [yes/no — is this a content decision?]

## Summary
[1–3 sentences: overall compliance status, critical issues count]
```

## Critical Rules
- A repair touching setting, narrative or character content: flag `[EDITORIAL: requires user approval]`.
- Output is edits plus at most one commit paragraph (`CLAUDE.md` §0); nothing is recorded in a registry.
