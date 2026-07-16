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

Before running any audit mode, read the following from the working tree:

- `references/canonical_sources.yaml` — confirm which design doc is canonical
- the target system doc — session-local work OR canonical; need NOT be canon (D2); canon is the baseline
- `params/<system>.md` — extracted mechanical values (e.g. `params/core.md`, `params/contest.md`, `params/mass_combat.md`)
- `canon/02_canon_constraints.md` — P-01–P-15
- `references/propagation_map.md` — dependency map

**The audit target may be whatever work/files exist in the working tree — it need NOT be canon (D2).** Read canon as the *baseline/yardstick*; where a canonical version of the target exists, the latest working-tree work *supersedes the stale canon* (note which artifact supersedes which source). The standing prohibition is narrower than before: **never audit from *memory* — read the actual artifact from the working tree, never a remembered or hallucinated version.**

## Audit Modes

### Mode A — Formula Validation
For each formula in the design doc (read from the working tree):
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
For each mechanic in the design doc (read from the working tree): map inputs and outputs.
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

**Output:** `gap_register_update.md` — findings feed the ED-disposition table (Output Rules
below); there is no `canon/editorial_ledger.yaml` file. P1 gaps get filed as
`ED-<LANE>-NNNN` entries in the relevant `registers/editorial_ledger_<lane>.jsonl`, per
`references/id_reservations.yaml`'s allocation protocol (see `valoria-editorial-register`'s
ID Law section) — not appended to a YAML file.
```
| ID | Type | Description | Location | Severity | Status |
```
Severity: P1 (blocks play), P2 (causes ambiguity), P3 (polish)

### Mode E — Core Principles Compliance
Cross-reference against the 13 core principles from the Foundations (read from the working tree):

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
- Findings land in a dated `designs/audit/<date>-<topic>/` folder (matching the naming
  pattern used throughout `designs/audit/`) — not standalone files at unspecified locations.
  (`archives/audit/` holds older runs that have since been superseded/archived — it is
  history only, never a target for new output; CLAUDE.md §1.)
- Modes can run independently or as full suite (A–E); when multiple modes run in one session, their
  findings can share one dated folder (one file per mode, e.g. `formula_audit.md`,
  `number_systems_audit.md`, `mechanic_dependency_graph.md`, `gap_register_update.md`,
  `core_principles_audit.md`), or be combined into a single report — either is fine as long as the
  folder is dated and topic-named.
- All findings assigned severity (P1/P2/P3)
- Every finding must resolve to an **ED-disposition table**: one row per finding, each row citing
  either the `ED-<LANE>-NNNN` id filed for it (per `references/id_reservations.yaml`'s allocation
  protocol) or an explicit no-action line (e.g. "no action — working as intended", "no action —
  superseded by PP-NNN"). P1 findings must be filed as ED entries, not merely noted.
- No editorial judgment — mechanical analysis only
- All mechanical values cited with source file and section from the working tree

## Dashboard registry logging (MANDATORY on completion)

When this skill's run concludes — pass, fail, or partial — append one record to the
Valoria audit/simulation-run registry (`references/audit_registry.jsonl`) so the
GitHub Pages dashboard and `tools/ci_audit_registry_check.py` can see it. Do this
every time, not only on request — a skipped append is what makes the dashboard's
verdict table go stale.

```bash
python tools/audit_registry.py append \
  --audit-type mechanic_audit \
  --subsystem <personal_combat|mass_battle|social_contest|faction_political|settlement_territory|threadwork|fieldwork_investigation|architecture|cross_cutting|corpus_wide> \
  --skill valoria-mechanic-audit \
  --date <YYYY-MM-DD> \
  --folder "<designs/audit/... path this run's output actually lives at>" \
  --scope "<one-line: what was audited>" \
  --verdict <this skill's own verdict, mapped to PASS|FAIL|PARTIAL|CONFORMANT|NON_CONFORMANT|OPEN|MIXED|CLOSED> \
  --verdict-detail "<one-line context, e.g. a PR number or ratification note>"
```

Pick `--subsystem` from what the run actually targeted (`cross_cutting` if it
genuinely spans several, `corpus_wide` only for a whole-corpus pass). See
`tools/audit_registry.py`'s module docstring for the full field/vocabulary
reference — this is the single source of truth for the schema, not this note.
