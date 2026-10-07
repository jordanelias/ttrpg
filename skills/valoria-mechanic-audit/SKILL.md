---
name: valoria-mechanic-audit
description: >
  Systematic mechanical consistency checking for the Valoria ruleset — formulas, number systems,
  interaction chains, gap detection, redundancy detection, and core principles compliance.
  ALWAYS use this skill when checking mechanical consistency, finding gaps, reviewing
  number systems, checking formulas, or evaluating mechanical interactions. Trigger on:
  "mechanical audit", "audit for mechanics", "check consistency", "find gaps", "number systems",
  "formula check", "interaction analysis", "what's broken", "what's missing", any specific
  mechanical question, or when the orchestrator routes a mechanical-consistency check. The bare
  word "audit" routes to nothing; the audit-word phrases that route here are "mechanical audit"
  and "audit for mechanics".
---

## Input Validation (MANDATORY BEFORE ANY AUDIT)

Read from the working tree, never from memory:

- `references/canonical_sources.yaml` — which design doc is canonical
- the target — any working-tree work or files; it need not be canon (D2). Canon is the baseline;
  where the target has a canonical version, the latest work supersedes it — note which supersedes which.
- mechanical values from their owner: a typed artifact under `engine/engine_params/` or the single
  Python owner (`CLAUDE.md` §0.05, §5)
- `canon/02_canon_constraints.md` — P-01–P-15
- `references/propagation_map.md` — dependency map

## Audit Modes

### Mode A — Formula Validation
For each formula in the design doc: confirm every variable is defined elsewhere in the ruleset;
compute output at minimum, average and maximum inputs; check for division by zero, negative pools,
impossible states, results outside the stated range, and boundary behaviour (attribute = 1 or max).

**Output table:** `| ID | Formula | Min Output | Max Output | Issues | Status |`

### Mode B — Number System Coherence
Inventory every numerical scale: attributes (range), derived scores (range + formula), faction
stats, tracks (Thread Tension (TT), Thread Charge (TC), Influence Points (IP), Thread Sensitivity
(TS), Thread Debt (TD), Taint, Certainty, Deniability Debt). Flag inconsistent ranges across
systems, different scales for analogous concepts, redundant difficulty levers (TN × Ob) and
unintuitive derived values. Propose unification where it does not violate the Foundations.

**Output table:** `| System | Range | Scale Basis | Analogous Systems | Inconsistency |`

### Mode C — Interaction Chain Analysis
Map each mechanic's upstream (what feeds it), downstream (what it feeds) and where chains
intersect. Flag:
- circular dependencies (A → B → A) and amplification loops (output feeds back to raise input)
- dead ends (calculated, never consumed) and unconnected systems (no links either way)
- interacting mechanics with no interaction rule

**Output table:** `| Mechanic | Upstream | Downstream | Chain Length | Flags |`

### Mode D — Gap Detection
Find:
- referenced but undefined mechanics; defined but never-referenced (orphaned) rules
- placeholders ("[Content as per prior ruleset]", "[TBD]")
- missing edge-case rules (value reaches 0, exceeds max, threshold crossed, simultaneous triggers)
- missing resolution procedures (X and Y conflict) and missing tables

**Output:** ED-disposition rows only (Output Rules); no gap-register file.

### Mode E — Core Principles Compliance
Rate each of the 13 core principles from the Foundations PRESENT / ALTERED (justification checked) /
ABSENT:

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

## Output Rules
- Output is edits plus at most one commit paragraph (`CLAUDE.md` §0); nothing is recorded in a
  registry and no audit directory is created. Modes run singly or as the full suite (A–E).
- Exception (`CLAUDE.md` §0, terminal pass): findings may go in a section of the audited artifact or
  a sibling file in its directory only if that record creates no work for a future session; if it
  does, drop it.
- Every finding carries a severity: P1 blocks play, P2 causes ambiguity, P3 polish.
- Every finding resolves to a row of an **ED-disposition table** citing either its filed
  `ED-<LANE>-NNNN` or an explicit no-action line ("no action — working as intended", "no action —
  superseded by PP-NNN"). P1 findings are filed, not merely noted: an entry in
  `registers/editorial_ledger_<lane>.jsonl`, id allocated per `references/id_reservations.yaml`
  (`valoria-editorial-register`'s ID Law section).
- Mechanical analysis only; no editorial judgment.
- Cite every mechanical value with its source file and section.
