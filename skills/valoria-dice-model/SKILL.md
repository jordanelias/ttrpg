---
name: valoria-dice-model
description: >
  Statistical modeling of Valoria dice mechanics: single-pool success probabilities,
  outcome distributions, opposing rolls (combat offence vs defence), pool split
  optimization, Fibonacci bonus marginal value, TN shift impact, and Momentum Expected Value.
  ALWAYS use this skill when any Valoria task requires probability tables, expected
  values, P(success/partial/failure), combat odds, or balance analysis of pool sizes.
  Trigger on: "probability", "expected value", "odds", "how often does X succeed",
  "pool size", "TN comparison", "combat split", "Fibonacci value", "balance check",
  "dice math", or whenever mechanic-audit or simulator needs quantitative support.
---

## Input Validation (MANDATORY BEFORE ANY TASK)

Read the following from the working tree before running any calculation:

- `params/core.md` — canonical die rule, TN values, Ob definitions
- `references/glossary.md` — term definitions

If either path is missing, stop — cannot proceed.

**The die rule and TN values are read from `params/core.md`.** The module source below encodes the current standard rule; if `params_core.md` differs, the module source is stale and must be updated before proceeding.

## Term Reference

Use `references/glossary.md` (read above) for all term definitions and permitted abbreviations.

---

## Canonical Die Rule

Read from `params/core.md`. Current standard:

```
d10 face → net successes
  1         → -1
  2 to TN-1 → 0
  TN to 9   → +1
  10        → +2  (flat bonus; no extra die rolled)

Net successes = sum of all dice contributions (may be negative).
```

TN values in Valoria: **6** (Controlled), **7** (Standard), **8** (Desperate).

If `params_core.md` specifies different values, those govern over the above.

---

## Setup

The canonical Python module lives at `skills/valoria-dice-model/valoria_dice.py` in the working tree. On every invocation:

1. Use the module at `skills/valoria-dice-model/valoria_dice.py`.
2. All computations use `TRIALS = 200_000` unless the task specifies fewer.

---

## Module Source

The module is `skills/valoria-dice-model/valoria_dice.py` in the working tree. Read it before running any calculation.

---

## Task Procedures

### Task 1 — Single-Pool Outcome Table
**Input:** pool sizes (list), TN, Ob values (list)
**Procedure:**
1. Ensure module exists.
2. Run `outcome_probs(n, tn, ob)` for each (pool, ob) combination.
3. Output markdown table: Pool | Overwhelm | Success | Partial | Failure

### Task 2 — TN Comparison (Controlled / Standard / Desperate)
**Input:** pool sizes, Ob
**Procedure:**
1. Run `outcome_probs` at TN 6, 7, 8 for each pool size.
2. Output three side-by-side tables + delta row (TN6−TN8 gap).
3. Flag any Ob where the TN shift causes a >20% swing in P(full success).

### Task 3 — Opposing Roll Analysis
**Input:** attacker pool + TN, defender pool + TN
**Procedure:**
1. Run `opposing_roll(ap, atn, dp, dtn)`.
2. Sweep: vary one pool from 3–12 while holding the other fixed.
3. Output: P(attacker wins), P(defender wins), P(tie), Expected Value margin per configuration.
4. Identify crossover point where attacker win probability drops below 50%.

### Task 4 — Pool Split Optimizer
**Input:** total combat pool, attacker TN, opponent pool size, opponent TN
**Procedure:**
1. Run `optimal_split`.
2. Output top 5 splits ranked by combined P(hit) × P(avoid).
3. Flag if asymmetric split dominates equal split by >5%.

### Task 5 — Fibonacci Marginal Value
**Input:** base pool, TN, Ob
**Procedure:**
1. Run `fibonacci_marginal`.
2. Output table: Attackers | Bonus Dice | P(full) | Delta vs Solo.
3. Flag diminishing returns: where adding more attackers gains <2% P(full).

### Task 6 — Momentum Value Analysis
**Input:** pool size, TN, Ob values (sweep)
**Procedure:**
1. Run `momentum_value` across Ob 1–8.
2. Output: P(full) base | extra die | Momentum spend | Momentum advantage over extra die.
3. Flag Ob values where Momentum is strictly worse than an extra die.

### Task 7 — Quick Check (Inline)
**Input:** pool, TN, Ob (single values)
**Output:** one-line summary via `quick_check(n, tn, ob)`.
Use when mechanic-audit or simulator needs a spot probability without a full table.

### Task 8 — Full Multi-TN Probability Tables
**Input:** pool range (e.g. 3–15), Ob range (e.g. 1–8)
**Procedure:**
1. Run `outcome_probs(n, tn, ob)` for TN 6, 7, 8 at every (pool, ob) combination.
2. Output three tables (one per TN) showing P(full success).
3. Add a delta table: TN6 minus TN8 at each cell.
4. Flag cells where TN6→TN8 shift causes >25% swing in P(full).

**Standard reference output** (generate once, cache to `references/tn_full_tables.md`):
Pool 3–12, Ob 1–6, all three TNs.

---

## Output Format

All outputs are **markdown tables**, inline unless >40 lines (then `.md` file committed to `references/`).
Always state sample size: `(n=200,000 trials)` in table caption.
Round probabilities to 3 decimal places in tables; 1 decimal in prose.

---

## Integration Points

| Calling Skill | Typical Request | Task # |
|---|---|---|
| valoria-mechanic-audit | "What's P(success) at these pool sizes?" | 1, 2 |
| valoria-simulator | "Opposing roll odds for this combat?" | 3, 4 |
| valoria-mechanic-audit | "Is Fibonacci bonus well-calibrated?" | 5 |
| valoria-simulator | "When is Momentum worth spending?" | 6 |
| Any skill | Spot-check a specific pool/TN/Ob | 7 |

---

## Params File Reference

| Params file | Used by |
|-------------|---------|
| `params/core.md` | All skills (dice engine baseline) |
| `params/combat.md` | simulator Mode G1, combat-simulator |
| `params/mass_combat.md` | simulator Mode G1 |
| `params/contest.md` | simulator Mode G2 |
| `params/threadwork.md` | simulator Mode G3 |
| `params/factions.md` | simulator Mode G4, mechanic-audit |
| `params/board_game.md` | simulator Mode G5 |
| `params/scale_transitions.md` | simulator Mode G (cross-mode), mechanic-audit Mode G |
