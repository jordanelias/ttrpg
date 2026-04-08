---
name: valoria-canon-guard
description: >
  Validate any Valoria mechanical proposal, existing mechanic, or content element against the
  Philosophical Foundations document. ALWAYS use this skill when checking philosophy compliance,
  evaluating new mechanic proposals, auditing existing mechanics for philosophical fidelity,
  or when any Valoria skill produces a finding that needs canon verification. Trigger on:
  "check philosophy", "canon check", "does this violate the foundations", "philosophy compliance",
  "is this consistent with the philosophy", any new mechanic proposal, any audit finding requiring
  philosophical validation, or whenever the orchestrator routes a compliance check.
  This skill NEVER approves content that contradicts the Foundations.
---

**Model:** Sonnet 4.6. Requires deep philosophical reasoning.

## Input Validation (MANDATORY BEFORE ANY COMPLIANCE CHECK)

Before running any compliance check, verify the following have been fetched from GitHub this session:

```python
# Required files — fetch via g.read_files_graphql() if not already in context
required = [
    'canon/00_philosophical_foundations.md',  # primary authority
    'canon/02_canon_constraints.md',          # P-01–P-15 derived constraints
    # fetch any canon/01_*.md amendments relevant to the target system
]
```

**Memory contamination warning:** userMemories may contain mechanical values (track values, territory data, faction stats, etc.) that feel current but are not fetched from GitHub. Do not use any value from memory as a source for mechanical analysis. Fetch only.

**If any required file was not fetched from GitHub this session:** STOP. Fetch it. Do not use remembered Foundations content — the file on GitHub is authoritative.

## Canon Constraints Reference (P-01 through P-15)

| ID | Constraint | Key Test |
|----|-----------|----------|
| P-01 | Inseparability: all three dimensions co-move | Does every thread op produce mandatory secondary consequences? |
| P-02 | Ein Sof = infinite positive being | Is the unintelligible ground framed as fullness, not void/chaos? |
| P-03 | Rendering = consciousness-performed | Is GM positioned as rendering engine? Is information asymmetry mechanical? |
| P-04 | Monstrosity = ontological, not moral | Are monstrous entities framed as rendering failures, not evil? |
| P-05 | Three emergence modes mechanically distinct | Do Modes 1/2/3 have distinct stat blocks and behaviors? |
| P-06 | Threadcut = radically is without becoming | Do threadcut beings maintain via Thread work? Past-Pull → auto-Gap? No Taint? |
| P-07 | Calamity = rendered-side mechanism | Does TT system imply over-drawing, not ground responsiveness? |
| P-08 | Epistemological barrier = inaccessibility, not suppression | Is knowledge transmission framed as "religious poetry"? Church reinforces, doesn't cause? |
| P-09 | Memory pulling = messy, costly, detectable | Not a clean eraser? Produces orphaned configurations? |
| P-10 | Epistemic seduction = perceptual shift | Is transformation framed as dissolving categories, not corruption? |
| P-11 | Temporal Disjunction (TD) is universal | Do ALL thread ops produce some TD? Not just Past-Pulls? |
| P-12 | Relational contagion via knotting | Does a transforming practitioner's shift propagate through Knots? |
| P-13 | Forgetting = rendering failure | Is Southernmost knowledge mechanically untransmittable to non-sensitives? |
| P-14 | Board/VG modes must express inseparability | Is co-movement mechanically implemented in all play modes? |
| P-15 | [Fetch from canon/02_canon_constraints.md — do not use memory] | |

**Fetch log (emit before any analysis):**
```
## FETCH LOG
canonical_sources.yaml: ✓ fetched ([N] lines)
[canonical design doc path]: ✓ fetched ([N] lines)
references/params_[system].md: ✓ fetched ([N] lines) / ✗ missing
```
If any required file is missing from this log, stop — the analysis is invalid.

## Process
1. Fetch and load `canon/00_philosophical_foundations.md` and `canon/02_canon_constraints.md` from GitHub
2. Load relevant Foundations section by chunk reference or direct read
3. For each applicable constraint:
   - **PASS**: mechanic satisfies the constraint
   - **PARTIAL**: mechanic partially satisfies — identify what's missing
   - **FAIL**: mechanic violates the constraint
4. For FAIL: cite specific Foundations text (by section, from fetched file), explain philosophical reasoning, propose repair
5. For PARTIAL: flag what's missing and assess severity (cosmetic vs. structural)

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
**Foundations ref:** §[N], key concept [cite from fetched file]
**Current implementation:** [what the mechanic does]
**Why this violates:** [philosophical reasoning]
**Proposed repair:** [mechanical suggestion]
**Editorial flag:** [yes/no — is this a content decision?]

## Summary
[1–3 sentences: overall compliance status, critical issues count]
```

## Critical Rules
- This skill NEVER approves content that contradicts the Foundations, regardless of mechanical elegance.
- Philosophy governs mechanics. Never the reverse.
- If a mechanic is mechanically sound but philosophically incoherent, it fails.
- If a repair proposal involves setting/narrative/character content: flag `[EDITORIAL: requires user approval]`.
- When uncertain whether something violates: flag as PARTIAL with reasoning, not PASS.
- All Foundations citations must reference the fetched file, not memory.
- Do not use remembered constraint values — P-15 in particular must be read from `canon/02_canon_constraints.md` on GitHub.
