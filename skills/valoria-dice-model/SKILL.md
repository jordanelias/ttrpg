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

**Model:** Haiku 4.5 for all execution (simulation is arithmetic, not reasoning).
**Sonnet** may call this skill and interpret results; it never reruns the math inline.

---

## Input Validation (MANDATORY BEFORE ANY TASK)

Fetch the following from GitHub before running any calculation:

```python
required = [
    'references/params_core.md',   # canonical die rule, TN values, Ob definitions
    'references/glossary.md',      # term definitions
]
files = g.read_files_graphql(required)
for path, content in files.items():
    if content is None:
        raise RuntimeError(f"GitHub fetch failed: {path} — cannot proceed")
```

**Version check:** Confirm `<!-- version: -->` tag in `references/params_core.md` matches current ruleset version in `compilation/README.md`. If mismatch: flag `[STALE PARAMS]` and stop.

**The die rule and TN values are read from `references/params_core.md`.** The module source below encodes the current standard rule; if `params_core.md` differs, the module source is stale and must be updated before proceeding.

## Term Reference

Use `references/glossary.md` (fetched above) for all term definitions and permitted abbreviations.

---

## Canonical Die Rule

Read from `references/params_core.md`. Current standard:

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

The canonical Python module lives at `valoria_dice.py`. On every invocation:

1. Check whether `/home/claude/valoria_dice.py` exists.
2. If not, write it from the **Module Source** section below before running anything.
3. All computations use `TRIALS = 200_000` unless the task specifies fewer.

---

## Module Source

Write this verbatim to `/home/claude/valoria_dice.py`:

```python
import random
from typing import List, Dict

TRIALS = 200_000

def die_ev(tn: int) -> float:
    p_minus = 0.1
    p_plus1 = max(0, (9 - tn + 1) / 10)
    p_zero  = (tn - 2) / 10
    return p_minus * -1 + p_plus1 * 1 + 0.1 * 2

def pool_ev(n: int, tn: int) -> float:
    return n * die_ev(tn)

def _roll_die(tn: int) -> int:
    r = random.randint(1, 10)
    if r == 1:  return -1
    if r == 10: return 2
    if r >= tn: return 1
    return 0

def _roll_pool(n: int, tn: int) -> int:
    return sum(_roll_die(tn) for _ in range(n))

def simulate_pool(n: int, tn: int, trials: int = TRIALS) -> List[int]:
    return [_roll_pool(n, tn) for _ in range(trials)]

def outcome_probs(n: int, tn: int, ob: int, trials: int = TRIALS) -> Dict[str, float]:
    results = simulate_pool(n, tn, trials)
    overwhelming = success = partial = failure = 0
    for r in results:
        if ob == 10:
            if r >= ob:   success += 1
            elif r >= 5:  partial += 1
            else:         failure += 1
        else:
            if r >= 2*ob: overwhelming += 1
            elif r >= ob: success += 1
            elif r > 0:   partial += 1
            else:         failure += 1
    t = trials
    return {
        "overwhelming": overwhelming/t, "success": success/t,
        "partial": partial/t, "failure": failure/t,
        "p_full": (overwhelming+success)/t,
    }

def opposing_roll(ap: int, atn: int, dp: int, dtn: int, trials: int = TRIALS) -> Dict[str, float]:
    atk_wins = def_wins = ties = margin_sum = 0
    for _ in range(trials):
        a = _roll_pool(ap, atn); d = _roll_pool(dp, dtn)
        margin_sum += (a - d)
        if a > d:   atk_wins += 1
        elif d > a: def_wins += 1
        else:       ties += 1
    return {
        "p_attacker_wins": atk_wins/trials, "p_defender_wins": def_wins/trials,
        "p_tie": ties/trials, "ev_margin": margin_sum/trials,
    }

def optimal_split(total: int, atk_tn: int, opp: int, opp_tn: int = 7,
                  def_tn: int = 7, trials: int = 50_000) -> List[Dict]:
    rows = []
    for off in range(1, total):
        dfn = total - off
        hit   = opposing_roll(off, atk_tn, opp, opp_tn, trials)
        avoid = opposing_roll(opp, opp_tn, dfn, def_tn, trials)
        rows.append({"offence": off, "defence": dfn,
                     "p_hit": hit["p_attacker_wins"], "p_avoid": avoid["p_defender_wins"],
                     "combined": hit["p_attacker_wins"] * avoid["p_defender_wins"]})
    return sorted(rows, key=lambda x: -x["combined"])

def fibonacci_marginal(base_pool: int, tn: int, ob: int,
                       max_attackers: int = 8, trials: int = 100_000) -> List[Dict]:
    """Expected Value gain from Fibonacci group bonus dice. Bonus: 2→+1, 3→+2, 5→+3, 8→+5."""
    bonus_map = {1: 0, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3, 7: 3, 8: 5}
    rows = []
    base = outcome_probs(base_pool, tn, ob, trials)
    for n in range(1, max_attackers+1):
        bonus = bonus_map.get(n, 5)
        p = outcome_probs(base_pool + bonus, tn, ob, trials)
        rows.append({"attackers": n, "bonus_dice": bonus,
                     "p_full": p["p_full"], "delta_vs_solo": p["p_full"] - base["p_full"]})
    return rows

def momentum_value(tn: int, ob: int, pool: int, trials: int = TRIALS) -> Dict:
    """Compare: spending 1 Momentum (auto-success) vs rolling 1 extra die."""
    base   = outcome_probs(pool,   tn, ob, trials)
    extra  = outcome_probs(pool+1, tn, ob, trials)
    results = simulate_pool(pool, tn, trials)
    mom_full = partial = 0
    for r in results:
        net = r + 1
        if ob == 10:
            if net >= ob:  mom_full += 1
            elif net >= 5: partial += 1
        else:
            if net >= ob:  mom_full += 1
    return {
        "base_p_full":       base["p_full"],
        "extra_die_p_full":  extra["p_full"],
        "momentum_p_full":   mom_full / trials,
        "momentum_vs_die":   (mom_full/trials) - extra["p_full"],
    }

def quick_check(n: int, tn: int, ob: int) -> str:
    p = outcome_probs(n, tn, ob, 100_000)
    return (f"Pool {n} TN{tn} Ob{ob}: "
            f"Overwhelm {p['overwhelming']:.1%} | Success {p['success']:.1%} | "
            f"Partial {p['partial']:.1%} | Fail {p['failure']:.1%} | Expected Value {pool_ev(n,tn):.2f}")
```

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

**Standard reference output** (generate once, cache to `references/tn_full_tables.md` via `g.atomic_commit()`):
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
| `references/params_core.md` | All skills (dice engine baseline) |
| `references/params_combat.md` | simulator Mode G1, combat-simulator |
| `references/params_mass_combat.md` | simulator Mode G1 |
| `references/params_debate.md` | simulator Mode G2 |
| `references/params_threadwork.md` | simulator Mode G3 |
| `references/params_factions.md` | simulator Mode G4, mechanic-audit |
| `references/params_board_game.md` | simulator Mode G5 |
| `references/params_scale_transitions.md` | simulator Mode G (cross-mode), mechanic-audit Mode G |
