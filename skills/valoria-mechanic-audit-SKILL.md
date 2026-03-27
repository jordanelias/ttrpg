# valoria-mechanic-audit

Mechanical consistency checking: formulas, number systems, interaction chains, gap detection, core principles.

**Model:** Sonnet 4.6.
**Input:** Chunked sections or `mechanics_index.md`. Never full document.

## Modes

### A — Formula Validation
Per formula in `mechanics_index.md`: verify variable definitions, calculate at min/avg/max, check for division-by-zero, negative pools, impossible states, boundary behavior.
**Output:** `formula_audit.md` — `| ID | Formula | Min | Max | Issues | Status |`

### B — Number System Coherence
Inventory all scales (attributes, derived scores, faction stats, tracks). Flag inconsistent ranges, redundant difficulty levers, unintuitive derivations. Propose unification where possible.
**Output:** `number_systems_audit.md` — `| System | Range | Scale Basis | Analogous Systems | Inconsistency |`

### C — Interaction Chain Analysis
Per mechanic: map upstream inputs, downstream outputs, chain intersections. Flag: circular dependencies, dead-end mechanics, unconnected systems, missing interaction rules, amplification loops.
**Output:** `mechanic_dependency_graph.md` — `| Mechanic | Upstream | Downstream | Chain Length | Flags |`

### D — Gap Detection
Check: referenced-but-undefined mechanics, placeholders/TBD, orphaned rules, missing edge cases (0/max/threshold/simultaneous), missing resolution procedures, missing tables.
**Output:** appends to `valoria_gap_register_consolidated.md` — `| ID | Type | Description | Location | Severity | Status |`
Severity: P1 (blocks play) / P2 (ambiguity) / P3 (polish)

### E — Core Principles Compliance
Cross-reference against Mechanics.docx principles:

| # | Principle | Test |
|---|-----------|------|
| 1 | Roll only when meaningful | "When to roll" gate present? |
| 2 | Let It Ride | Re-roll prohibition stated? |
| 3 | Fail Forward | Failure advances narrative? |
| 4 | Histories, not Skills | Lived experience, not categories? |
| 5 | Pool = Attribute + History bonus | Base formula preserved? |
| 6 | Wound system with escalating Ob | +1 Ob per wound? |
| 7 | Inspiration/Spirit economy | Emotional resource system present? |
| 8 | Beliefs as moral character | Moral dimension expressed through Beliefs + faction ethical tendencies? (Virtues/Vices and Maxims cut; Beliefs subsume) |
| 9 | Social combat via Rhetoric | Appeals, Debates, Negotiation distinct? |
| 10 | Reach/Speed priority | Weapon geometry determines combat flow? |
| 11 | Phase-based combat | Collaborative action within phases? |
| 12 | Beginner's Luck | Untrained attempt accessibility? |
| 13 | Circles and Resources | Social/economic resolution present? |

Per principle: PRESENT / ALTERED (with justification) / ABSENT

## Rules
- Each mode produces standalone md. Modes run independently or as suite.
- All findings: P1/P2/P3 severity. P1 → auto-append to gap register.
- No editorial judgment — mechanical analysis only.
