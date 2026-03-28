"""
Valoria Dice Engine — canonical statistical model.
Die faces (d10):
  1        → -1 success
  2 to TN-1 → 0 successes
  TN to 9   → +1 success
  10        → +2 successes (flat bonus, no extra die)

Net successes = sum of all die contributions (can be negative).
"""

import random
from typing import List, Dict, Tuple
from collections import defaultdict

TRIALS = 200_000

# ── Analytic per-die EV ──────────────────────────────────────────────────────

def die_ev(tn: int) -> float:
    """Expected net successes from one d10 at given TN."""
    p_minus = 0.1          # result = 1
    p_zero  = (tn - 2) / 10  # results 2 .. TN-1
    p_plus1 = (10 - tn) / 10  # results TN .. 9  (0 when TN=10)
    p_plus2 = 0.1          # result = 10
    # clamp: when TN=6, p_plus1 = 4/10; when TN=10, p_plus1 = 0
    p_plus1 = max(0, (9 - tn + 1) / 10)  # TN..9 inclusive
    p_zero  = (tn - 2) / 10               # 2..TN-1 inclusive
    return p_minus * -1 + p_zero * 0 + p_plus1 * 1 + p_plus2 * 2

def pool_ev(n: int, tn: int) -> float:
    return n * die_ev(tn)

# ── Monte Carlo ──────────────────────────────────────────────────────────────

def _roll_die(tn: int) -> int:
    r = random.randint(1, 10)
    if r == 1:   return -1
    if r == 10:  return 2
    if r >= tn:  return 1
    return 0

def _roll_pool(n: int, tn: int) -> int:
    return sum(_roll_die(tn) for _ in range(n))

def simulate_pool(n: int, tn: int, trials: int = TRIALS) -> List[int]:
    return [_roll_pool(n, tn) for _ in range(trials)]

# ── Outcome probabilities ────────────────────────────────────────────────────

def outcome_probs(n: int, tn: int, ob: int, trials: int = TRIALS) -> Dict[str, float]:
    """
    Returns P(overwhelming), P(success), P(partial), P(failure) for a pool/TN/Ob.
    Ob10 special: overwhelming unavailable, partial requires net>=5.
    """
    results = simulate_pool(n, tn, trials)
    overwhelming = success = partial = failure = 0
    for r in results:
        if ob == 10:
            if r >= ob:      success += 1
            elif r >= 5:     partial += 1
            else:            failure += 1
        else:
            if r >= 2 * ob:  overwhelming += 1
            elif r >= ob:    success += 1
            elif r > 0:      partial += 1
            else:            failure += 1
    t = trials
    return {
        "overwhelming": overwhelming / t,
        "success":      success / t,
        "partial":      partial / t,
        "failure":      failure / t,
        "p_hit":        (overwhelming + success + partial) / t,  # net > 0
        "p_full":       (overwhelming + success) / t,            # net >= ob
    }

# ── Opposing roll ────────────────────────────────────────────────────────────

def opposing_roll(
    atk_pool: int, atk_tn: int,
    def_pool: int, def_tn: int,
    trials: int = TRIALS
) -> Dict[str, float]:
    """
    P(attacker net > defender net) — used for combat offence vs defence.
    Returns: p_attacker_wins, p_defender_wins, p_tie, ev_margin.
    """
    atk_wins = def_wins = ties = 0
    margin_sum = 0
    for _ in range(trials):
        a = _roll_pool(atk_pool, atk_tn)
        d = _roll_pool(def_pool, def_tn)
        margin_sum += (a - d)
        if a > d:   atk_wins += 1
        elif d > a: def_wins += 1
        else:       ties += 1
    t = trials
    return {
        "p_attacker_wins": atk_wins / t,
        "p_defender_wins": def_wins / t,
        "p_tie":           ties / t,
        "ev_margin":       margin_sum / t,
    }

# ── Pool split optimizer (combat) ────────────────────────────────────────────

def optimal_split(
    total_pool: int, atk_tn: int,
    opp_pool: int,   def_tn_opp: int = 7,
    def_tn_self: int = 7,
    trials: int = 50_000
) -> List[Dict]:
    """
    For each (offence, defence) split of total_pool, compute:
      - P(land hit on opponent)
      - P(avoid hit from opponent)
    Returns list sorted by combined score.
    """
    rows = []
    for off in range(1, total_pool):  # min 1 each side
        dfn = total_pool - off
        hit = opposing_roll(off, atk_tn, opp_pool, def_tn_opp, trials)
        avoid = opposing_roll(opp_pool, def_tn_opp, dfn, def_tn_self, trials)
        rows.append({
            "offence": off,
            "defence": dfn,
            "p_hit":   hit["p_attacker_wins"],
            "p_avoid": avoid["p_defender_wins"],
            "combined": hit["p_attacker_wins"] * avoid["p_defender_wins"],
        })
    rows.sort(key=lambda x: -x["combined"])
    return rows

# ── Standard table printers ──────────────────────────────────────────────────

def print_success_table(pool_sizes, tn, ob_values, trials=TRIALS):
    print(f"\n### TN {tn} — P(full success: net ≥ Ob)")
    header = "| Pool |" + "".join(f" Ob{ob:2d} |" for ob in ob_values)
    sep    = "|------|" + "-------|" * len(ob_values)
    print(header)
    print(sep)
    for n in pool_sizes:
        results = simulate_pool(n, tn, trials)
        row = f"|  {n:3d} |"
        for ob in ob_values:
            p = sum(1 for r in results if r >= ob) / trials
            row += f" {p:.3f} |"
        print(row)

def print_outcome_table(pool_sizes, tn, ob, trials=TRIALS):
    print(f"\n### TN {tn} Ob {ob} — Outcome Distribution")
    print("| Pool | Overwhelm | Success | Partial | Failure |")
    print("|------|-----------|---------|---------|---------|")
    for n in pool_sizes:
        p = outcome_probs(n, tn, ob, trials)
        print(f"|  {n:3d} |   {p['overwhelming']:.3f}   |  {p['success']:.3f}  |  {p['partial']:.3f}  |  {p['failure']:.3f}  |")

def print_ev_table(pool_sizes, tns=(6, 7, 8)):
    print("\n### Analytic EV per pool (net successes)")
    header = "| Pool |" + "".join(f"  TN{t}  |" for t in tns)
    print(header)
    print("|------|" + "--------|" * len(tns))
    for n in pool_sizes:
        row = f"|  {n:3d} |"
        for t in tns:
            row += f"  {pool_ev(n, t):5.2f}  |"
        print(row)

# ── Quick-reference function (used by skills) ────────────────────────────────

def quick_check(n: int, tn: int, ob: int) -> str:
    """One-line summary for inline use."""
    p = outcome_probs(n, tn, ob)
    ev = pool_ev(n, tn)
    return (
        f"Pool {n} TN{tn} Ob{ob}: "
        f"Overwhelm {p['overwhelming']:.1%} | "
        f"Success {p['success']:.1%} | "
        f"Partial {p['partial']:.1%} | "
        f"Fail {p['failure']:.1%} | "
        f"EV {ev:.2f}"
    )

if __name__ == "__main__":
    import sys
    random.seed(42)
    print("=== VALORIA DICE ENGINE — SELF-TEST ===\n")

    print("Analytic EV per die:")
    for tn in (6, 7, 8):
        print(f"  TN{tn}: {die_ev(tn):.4f}")

    print_ev_table(range(3, 12), (6, 7, 8))
    print_success_table([3,4,5,6,7,8,10,12], 7, [1,2,3,4,5,8,10])
    print_success_table([3,4,5,6,7,8,10,12], 6, [1,2,3,4,5])
    print_success_table([3,4,5,6,7,8,10,12], 8, [1,2,3,4,5])
    print_outcome_table([4,6,8,10], 7, 3)
    print_outcome_table([4,6,8,10], 7, 5)

    print("\n### Opposing rolls — 6-die pool vs 6-die pool at TN7")
    r = opposing_roll(6, 7, 6, 7)
    for k, v in r.items():
        print(f"  {k}: {v:.3f}")

    print("\n### Pool split — 10 dice total vs 6-die opponent at TN7")
    splits = optimal_split(10, 7, 6, 7, 7, trials=30_000)
    print("| Off | Def | P(hit) | P(avoid) | Combined |")
    print("|-----|-----|--------|----------|----------|")
    for row in splits[:5]:
        print(f"|  {row['offence']:2d} |  {row['defence']:2d} | {row['p_hit']:.3f}  |  {row['p_avoid']:.3f}   |  {row['combined']:.3f}   |")

    print(f"\nQuick check: {quick_check(6, 7, 3)}")
