---
name: valoria-mechanic-audit
description: >
  Systematic mechanical consistency checking for the Valoria ruleset — formulas, number systems,
  interaction chains, gap detection, redundancy detection, and core principles compliance.
  ALWAYS use this skill when auditing mechanics, checking consistency, finding gaps, reviewing
  number systems, checking formulas, or evaluating mechanical interactions. Trigger on:
  "audit mechanics", "check consistency", "find gaps", "number systems", "formula check",
  "interaction analysis", "what's broken", "what's missing", any specific mechanical question,
  or when the orchestrator routes a mechanical audit.
---

**Model:** Sonnet 4.6. Requires cross-referencing complex interacting systems.

## Input Validation (MANDATORY BEFORE ANY AUDIT)

Before running any audit mode, verify the following have been fetched from GitHub this session:

```python
# Required files — fetch via g.read_files_graphql() if not already in context
required = [
    'references/canonical_sources.yaml',       # confirm which design doc is canonical
    '<canonical design doc for target system>', # from canonical_sources.yaml lookup
    'references/params_<system>.md',           # extracted mechanical values
    'canon/02_canon_constraints.md',           # P-01–P-15
]
```

**If any required file was not fetched from GitHub this session:** STOP. Fetch it. Do not substitute memory or local file content.

**Never audit from memory or project-file versions of design docs. The canonical source is always on GitHub.**

## Audit Modes

### Mode A — Formula Validation
For each formula in the fetched design doc:
- Verify all variables are defined elsewhere in the ruleset
- Calculate output at minimum, average, and maximum input values
- Check for: division by zero, negative pools, impossible states, results outside stated range
- Check for: undefined behavior at boundary values (attribute = 1 or max)

**Output:** `formula_audit.md`
```
| ID | Formula | Min Output | Max Output | Issues | Status |
```

### Mode B — Number System Coherence
Inventory all numerical scales:
- Character attributes (range), derived scores (range + formula), faction stats, tracks (Thread Tension (TT), Thread Charge (TC), Influence Points (IP), Thread Sensitivity (TS), Thread Debt (TD), Taint, Certainty, Deniability Debt)
- Flag: inconsistent ranges across systems, redundant difficulty levers (TN × Ob interaction), unintuitive derived values
- Flag: different scales for analogous concepts
- Propose unification where possible without violating Foundations

**Output:** `number_systems_audit.md`
```
| System | Range | Scale Basis | Analogous Systems | Inconsistency |
```

### Mode C — Interaction Chain Analysis
For each mechanic in the fetched design doc: map inputs and outputs.
Build dependency chains:
- What feeds this mechanic? (upstream)
- What does this mechanic feed? (downstream)
- Where do chains intersect?

**Flag:**
- Circular dependencies (A → B → A)
- Dead-end mechanics (calculated but never consumed)
- Unconnected systems (no upstream or downstream links)
- Mechanics that interact but lack an interaction rule
- Amplification loops (output feeds back to increase input)

**Output:** `mechanic_dependency_graph.md`
```
| Mechanic | Upstream | Downstream | Chain Length | Flags |
```

### Mode D — Gap Detection
Systematic check:
- Referenced but undefined mechanics
- Placeholder sections ("[Content as per prior ruleset]", "[TBD]")
- Defined but never-referenced mechanics (orphaned rules)
- Missing edge case rules (value reaches 0, exceeds max, threshold crossed, simultaneous triggers)
- Missing resolution procedures (what happens when X and Y conflict?)
- Missing tables

**Output:** `gap_register_update.md` — appends to `canon/editorial_ledger.yaml`
```
| ID | Type | Description | Location | Severity | Status |
```
Severity: P1 (blocks play), P2 (causes ambiguity), P3 (polish)

### Mode E — Core Principles Compliance
Cross-reference against the 13 core principles from the fetched Foundations:

| # | Principle | Test |
|---|-----------|------|
| 1 | Roll only when meaningful | Is there a "when to roll" gate? |
| 2 | Let It Ride | Is re-roll prohibition stated? |
| 3 | Fail Forward | Does failure advance narrative? |
| 4 | Histories, not Skills | Are Histories lived experience, not categories? |
| 5 | Pool = Attribute + History bonus | Is the base formula preserved? |
| 6 | Wound system with escalating Ob | Is +1 Ob per wound implemented? |
| 7 | Inspiration/Spirit economy | Is the emotional resource system present? |
| 8 | Virtues & Vices | Is moral character mechanical? |
| 9 | Social combat via Rhetoric | Are Appeals, Debates, Negotiation distinct? |
| 10 | Reach/Speed priority | Does weapon geometry determine combat flow? |
| 11 | Phase-based combat | Is collaborative action within phases supported? |
| 12 | Beginner's Luck | Is accessibility for untrained attempts present? |
| 13 | Circles and Resources | Are social/economic resolution systems present? |

For each: PRESENT / ALTERED (with justification check) / ABSENT

**Output:** `core_principles_audit.md`

## Output Rules
- Each mode produces a standalone md file
- Modes can run independently or as full suite (A–E)
- All findings assigned severity (P1/P2/P3)
- P1 findings automatically appended to `canon/editorial_ledger.yaml`
- No editorial judgment — mechanical analysis only
- All mechanical values cited with source file and section from GitHub fetch
