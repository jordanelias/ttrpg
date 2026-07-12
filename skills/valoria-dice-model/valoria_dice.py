import math
import random
from typing import List, Dict

TRIALS = 200_000

# Continuous engine (Decision E, params/core.md "Continuous Engine") — canonical for the
# Godot videogame implementation. net ~ Normal(mu*N, sigma*sqrt(N)) per die at the active TN;
# statistically equivalent to the discrete d10 rule below (validated to within 0.03 in mean/std,
# pool sizes 5-17, Phase 5 sim 2026-05-15). The discrete rule stays canonical for TTRPG-mode play.
_CONTINUOUS_MU = {6: 0.50, 7: 0.40, 8: 0.30}
_CONTINUOUS_SIGMA = {6: 0.806, 7: 0.800, 8: 0.781}

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

def _norm_cdf(x: float) -> float:
    return 0.5 * (1 + math.erf(x / math.sqrt(2)))

def continuous_outcome_probs(n: int, tn: int, ob: float) -> Dict[str, float]:
    """Canonical videogame-mode (Godot) resolver — net ~ Normal(mu*N, sigma*sqrt(N)) per
    params/core.md's Continuous Engine. Continuity-corrected (resolve against x - 0.5, per
    the ER-2 fix landed in params/core.md, commit a3d3888) so odds track the discrete model
    even at small pools, per params/core.md's own equivalence note. Ob may be fractional
    (fractional Ob is canonical in videogame mode); clamped to the canonical [1, 20] range.
    Degree thresholds match params/core.md's Degrees of Success table: Overwhelming
    net >= max(2*Ob, 3), Success net >= Ob, Partial 0 < net < Ob, Failure net <= 0 —
    EXCEPT the documented Ob-20 exception (params/core.md "Degrees of Success"): at Ob 20,
    Overwhelming is unavailable (folds into Success) and Partial requires net >= 10 instead
    of net > 0."""
    if tn not in _CONTINUOUS_MU:
        raise ValueError(f"No continuous-engine mu/sigma for TN {tn} — only 6/7/8 defined")
    mu = _CONTINUOUS_MU[tn] * n
    sigma = _CONTINUOUS_SIGMA[tn] * math.sqrt(n)
    ob = max(1.0, min(20.0, ob))

    def p_at_least(x: float) -> float:
        return 1 - _norm_cdf((x - 0.5 - mu) / sigma)

    p_success_or_better = p_at_least(ob)
    if ob >= 20:
        # Ob-20 exception: Overwhelming unavailable, Partial requires net >= 10.
        p_partial_or_better = p_at_least(10)
        return {
            "overwhelming": 0.0,
            "success": p_success_or_better,
            "partial": p_partial_or_better - p_success_or_better,
            "failure": 1 - p_partial_or_better,
            "p_full": p_success_or_better,
        }
    p_overwhelming = p_at_least(max(2 * ob, 3))
    p_partial_or_better = p_at_least(1e-9)  # net > 0
    return {
        "overwhelming": p_overwhelming,
        "success": p_success_or_better - p_overwhelming,
        "partial": p_partial_or_better - p_success_or_better,
        "failure": 1 - p_partial_or_better,
        "p_full": p_success_or_better,
    }

def continuous_quick_check(n: int, tn: int, ob: float) -> str:
    p = continuous_outcome_probs(n, tn, ob)
    return (f"[continuous/Godot-canonical] Pool {n} TN{tn} Ob{ob}: "
            f"Overwhelm {p['overwhelming']:.1%} | Success {p['success']:.1%} | "
            f"Partial {p['partial']:.1%} | Fail {p['failure']:.1%}")

def quick_check(n: int, tn: int, ob: int) -> str:
    p = outcome_probs(n, tn, ob, 100_000)
    return (f"Pool {n} TN{tn} Ob{ob}: "
            f"Overwhelm {p['overwhelming']:.1%} | Success {p['success']:.1%} | "
            f"Partial {p['partial']:.1%} | Fail {p['failure']:.1%} | Expected Value {pool_ev(n,tn):.2f}")