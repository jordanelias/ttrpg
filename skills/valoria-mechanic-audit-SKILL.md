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


### F — Playtest Burden Analysis
Per mechanic or procedure: measure cost imposed on players and Game Master at the table.

**Per mechanic, produce:**

| Field | Content |
|-------|---------|
| Estimated resolve time | Human time in seconds for a typical instance (roll + interpret + apply) |
| Mandatory lookups | Tables/rules player must consult to resolve (count) |
| Parallel tracking burden | How many values must be held in working memory simultaneously |
| Decision points | Number of choices player makes per instance |
| Cognitive load rating | Low / Medium / High (formula: lookups + tracking + decisions; ≥5 = High) |

**Flag:** Any mechanic with High cognitive load or >90s resolve time → P2 finding. Any that require >2 parallel lookups → P1 if they occur every round.

**Output:** `playtest_burden.md` — `| Mechanic | Time(s) | Lookups | Tracking | Decisions | Load | Flag |`

### G — Cross-Mode Consistency
Test that each mechanic behaves correctly when the session switches mode (TTRPG → BG → Hybrid).

**Per mechanic with mode tags:**
1. Identify which modes it appears in.
2. For each mode pairing (TTRPG↔BG, TTRPG↔Hybrid, BG↔Hybrid): does the mechanic change? If yes — is the change documented? Is the transition procedure defined?
3. Check transition point mechanics specifically: what triggers a mode switch, what state is preserved, what resets.

**Flag:** Mechanic present in 2+ modes with no documented transition procedure → P1. Mechanic behaves differently across modes with no explanation → P2.

**Output:** `cross_mode_audit.md` — `| Mechanic | Modes | Transition Defined? | State Preserved? | Flag |`

### H — Flowchart Generation
Produce a text-based branching flowchart for a mechanic or procedure.

**Format (Mermaid):**
```
flowchart TD
  A[Trigger condition] --> B{Decision point}
  B -->|Yes| C[Outcome A]
  B -->|No| D[Outcome B]
  C --> E{Another gate?}
  ...
```

Include: all decision points, all dice roll branches (succeed/partial/fail), all state changes per branch, all exit conditions. Every leaf node must be a terminal state or loop-back label.

**Flag inline:** Any branch with no defined resolution (dead branch → P1), any loop with no exit condition (regression → P1).

**Output:** Mermaid block, inline unless >60 nodes (then `.md` file).

### I — Precedent Comparison
Compare a mechanic against named reference games. Read `designs/` for any prior game analysis already done (bg_improvement_* files contain 33-game analysis).

**Per mechanic under review:**
1. Identify closest analogue in 1–3 reference games.
2. State: how reference game resolves the same problem, what they get right, what Valoria's version does differently.
3. Flag: if Valoria's version is strictly worse on cognitive load OR outcome variance without a philosophical justification → P2.

**Reference pool (priority):** Burning Wheel, Blades in the Dark, Root, Pax Pamir, Twilight Imperium, Mage Knight, Spirit Island, Arcs, Anachrony, Oath, Barrage, Concordia, Nemesis, The Quiet Year, HoMM3, Crisis.

**Output:** inline table `| Mechanic | Closest Analogue | Game | Valoria Difference | Flag |`


## Read Protocol — Mandatory Before Any Mode
Load params files, not stage files. Stage files are verbose source documents; params files are extracted mechanical values.

1. Always read `references/params_core.md` first (dice engine, TN, Ob, degrees).
2. Then read only the params files relevant to the subsystem being simulated/audited:

| Subsystem | Params File |
|-----------|-------------|
| Core dice/TN/Ob | `references/params_core.md` |
| Personal combat | `references/params_combat.md` |
| Mass combat | `references/params_mass_combat.md` |
| Debate | `references/params_debate.md` |
| Threadwork | `references/params_threadwork.md` |
| Factions (TTRPG or BG) | `references/params_factions.md` |
| Board game mode | `references/params_board_game.md` |
| Scale/mode transitions | `references/params_scale_transitions.md` |

3. For each params file loaded, check the `<!-- version: -->` tag. If it does not match the current ruleset version (see `compilation/README.md`), halt and flag: `[STALE PARAMS: <file> is <version>, current ruleset is <version> — update params before proceeding]`.
4. Do NOT read stage files or design files to get mechanical values. If a value is missing from params, flag it as a gap and request a params update rather than reading the source document mid-simulation.
5. Exception: when specifically auditing a new design document (not yet parameterised), read that document directly and note that params are incomplete for that subsystem.

## Version Check Protocol (Mandatory)
Before running any mode that uses mechanical values:
1. Read the relevant `references/params_*.md` file(s) for this task.
2. Check the `<!-- version: -->` tag at the top of each params file.
3. Compare against the current ruleset version (stated in `compilation/README.md`).
4. If params version ≠ current ruleset version: **halt, flag as `[STALE PARAMS: <file> is v0.XX, current ruleset is vX.XX — update params before proceeding]`**, and do not proceed until the user confirms or params are updated.
5. If params version matches: proceed. Cost: ~200 tokens per params file read. No GitHub API call required.

Params files and their skill usage:
| Params file | Used by |
|-------------|---------|
| `references/params_core.md` | All skills (dice engine baseline) |
| `references/params_combat.md` | simulator Mode G1, combat-simulator |
| `references/params_mass_combat.md` | simulator Mode G1 |
| `references/params_debate.md` | simulator Mode G2 |
| `references/params_threadwork.md` | simulator Mode G3 |
| `references/params_factions.md` | simulator Mode G4, mechanic-audit |
| `references/params_board_game.md` | simulator Mode G5 |
| `references/params_scale_transitions.md` | simulator Mode G (cross-mode), mechanic-audit Mode G |
## Mode G — Cross-Mode Consistency Audit

**Run this after any Mode C/D that touches a mechanic existing in multiple game modes.**

For each mechanic audited:
1. Identify which modes it appears in (TTRPG / Hybrid / BG)
2. Load the relevant params file for each mode
3. Check: does the mechanic produce equivalent strategic incentives across modes?
4. Check: does the mechanic's resolution complexity scale appropriately (simpler in BG, fuller in TTRPG)?
5. Check: is every mode-specific variant documented with its rationale?

Flag: any undocumented mode-specific behaviour (P2), any mode where the mechanic is absent without explanation (P1 if the mechanic is referenced cross-mode).

**Transition points (always audit these):**
- Zoom In / Zoom Out: verify against `skills/valoria-orchestrator/references/state_transfer_spec.md`
- Register Shift: verify state persistence at each scale crossing
- Domain Echo: verify that faction-level consequences are correctly derived from personal-level outcomes

If `skills/valoria-orchestrator/references/state_transfer_spec.md` does not exist or is stale: halt, flag `[STATE-TRANSFER-SPEC MISSING OR STALE]`, do not proceed with transition audit.
