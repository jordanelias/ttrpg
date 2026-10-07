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

Read from the working tree; if either is missing, stop:

- `engine/dice_engine/dice_engine.py` — owner of the die rule, the TN and `degree_from_net`
- `references/glossary.md` — term definitions and permitted abbreviations
- `skills/valoria-dice-model/valoria_dice.py` — the module every task runs; if it differs from the
  owner, update it first. Computations use `TRIALS = 200_000` unless the task specifies fewer.

## Two Resolver Modes (both canonical, different contexts)

Statistically equivalent; choose by the question, not by recency:

| Mode | Governs | Tasks |
|---|---|---|
| Discrete (legacy / TTRPG-mode) | tabletop play | 1, 3–8 |
| Continuous (videogame-mode, Godot-canonical) | what the Godot build actually rolls | 9 |

**Degrees** are the same for both modes, owned by `degree_from_net`, with margin = net − Ob:
Overwhelming `margin ≥ 3`, Success `margin ≥ 1`, Partial `0 ≤ margin < 1`, Failure `margin < 0`.

### Discrete — Canonical Die Rule (TTRPG-mode)

```
d10 face → net successes
  1       → -1
  2 to 6  → 0
  7 to 9  → +1
  10      → +2  (flat bonus; no extra die rolled)

Net successes = sum of all dice contributions (may be negative).
```

**TN is 7, always** (ED-IN-0196): a varying difficulty is an Ob, not a TN. The script raises
`ValueError` on any other TN.

### Continuous — Godot-canonical Resolver (videogame-mode)

- `net ~ Normal(μ·N, σ·√N)`, μ = 0.40 and σ = 0.800 per die at TN 7 (`_CONTINUOUS_MU`,
  `_CONTINUOUS_SIGMA`).
- Continuity-corrected: resolves against `x − 0.5`, so odds track the discrete model at small pools.
- Ob may be fractional (weapon condition, cover, terrain).
- `continuous_outcome_probs(n, tn, ob)` and `continuous_quick_check(n, tn, ob)`: same call shape as
  the discrete functions, closed-form via the normal CDF, no sampling.

## Task Procedures

### Task 1 — Single-Pool Outcome Table
**Input:** pool sizes, TN, Ob values. Run `outcome_probs(n, tn, ob)` per (pool, Ob); output
`Pool | Overwhelm | Success | Partial | Failure`.

### Task 2 — TN Comparison (superseded)
There is no TN to compare. For a difficulty comparison, sweep Ob at TN 7 with Task 1.

### Task 3 — Opposing Roll Analysis
**Input:** attacker pool + TN, defender pool + TN.
1. Run `opposing_roll(ap, atn, dp, dtn)`, sweeping one pool over 3–12 with the other fixed.
2. Output per configuration: P(attacker wins), P(defender wins), P(tie), expected margin.
3. Identify the crossover where P(attacker wins) drops below 50%.

### Task 4 — Pool Split Optimizer
**Input:** total combat pool, attacker TN, opponent pool, opponent TN. Run `optimal_split`; output
the top 5 splits by P(hit) × P(avoid); flag an asymmetric split beating the equal split by >5%.

### Task 5 — Fibonacci Marginal Value
**Input:** base pool, TN, Ob. Run `fibonacci_marginal`; output
`Attackers | Bonus Dice | P(full) | Delta vs Solo`; flag where another attacker gains <2% P(full).

### Task 6 — Momentum Value Analysis
**Input:** pool, TN, Ob sweep. Run `momentum_value` over Ob 1–8; output
`P(full) base | extra die | Momentum spend | Momentum advantage over extra die`; flag each Ob where
Momentum is strictly worse than an extra die.

### Task 7 — Quick Check (Inline)
**Input:** single pool, TN, Ob. One-line summary via `quick_check(n, tn, ob)`.

### Task 8 — Full Probability Table
**Input:** pool range (e.g. 3–15), Ob range (e.g. 1–8). Run `outcome_probs(n, 7, ob)` at every
pair; output P(full success). Standard reference, generated once and cached to
`references/tn_full_tables.md`: pool 3–12, Ob 1–6.

### Task 9 — Continuous-Mode Table (Godot-canonical)
**Input:** pool sizes, TN, Ob values (fractional allowed). Run `continuous_outcome_probs(n, tn, ob)`
per pair; output `Pool | Overwhelm | Success | Partial | Failure` labelled
"[continuous/Godot-canonical]". Use for the videogame's resolver, e.g. balance that lands in
`engine/engine_params/*.json` or `systems/combat/combat_engine_v1/`.

## Output Format

- Markdown tables, inline unless >40 lines (then a `.md` committed to `references/`).
- Caption states sample size: `(n=200,000 trials)`.
- Probabilities: 3 decimals in tables, 1 in prose.

## Integration Points

| Calling Skill | Typical Request | Task # |
|---|---|---|
| valoria-mechanic-audit | "What's P(success) at these pool sizes?" | 1 |
| valoria-mechanic-audit | "Is Fibonacci bonus well-calibrated?" | 5 |
| Any skill | "Opposing roll odds for this combat?" | 3, 4 |
| Any skill | "When is Momentum worth spending?" | 6 |
| Any skill | Spot-check a specific pool/TN/Ob | 7 |
| Any skill | "What will the Godot build actually roll?" | 9 |
