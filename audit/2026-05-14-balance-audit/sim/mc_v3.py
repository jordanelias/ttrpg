"""
Sim v3 — corrected victory formulas

v2 issue identified: Church victory_progress included `CI clock + 3×inquisitors`
as personal score. CI is a global pressure clock that triggers events; not a
personal scoreboard. Fixed below.

All factions now scored on territories × L baseline (fair across factions),
plus faction-specific bonuses for their canonical victory path.
"""

import sys, json, math, random
sys.path.insert(0, '/home/claude')
from collections import defaultdict, Counter
from mc_sim_v2 import (Faction, Territory, World, make_action, prereqs_met,
                       pool_and_ob, score_action, list_candidate_actions,
                       select_actions, init_world, roll_pool, resolve_degree)
from mc_sweep import apply_outcome_extended, end_of_season_extended


# Replace victory_progress with corrected version
def victory_progress_v3(self, world):
    """Faction-specific victory path; territories × L baseline + bonuses."""
    base = len(self.territories) * self.stats['L']

    if self.name == 'Valorsmark':
        # Sovereign/Mandate: territories × L + Charters × 3 + sum(L+PS+Sta)
        return (base + len(self.charters) * 3 +
                self.stats['L'] + self.stats['PS'] + self.stats['Sta'])

    elif self.name == 'Church':
        # Ecclesiastical: territories × L + Inquisitors × 4 + L + I
        return (base + len(self.inquisitors) * 4 +
                self.stats['L'] + self.stats['I'])

    elif self.name == 'Hafenmark':
        # Parliamentary: territories × L + tokens × 4 + W + L + PI/2
        return (base + sum(self.tokens_held.values()) * 4 +
                self.stats['W'] + self.stats['L'] +
                world.clocks['PI'] // 2)

    elif self.name == 'Varfell':
        # Revelation: territories × L + RT × 6 + Int × 2 + Mil
        return (base + self.revelation_tokens * 6 +
                self.stats['Int'] * 2 + self.stats['Mil'])

    return base


# Monkey-patch
Faction.victory_progress = victory_progress_v3


def run_campaign_v3(tweaks=None, seasons=12, seed=None):
    if seed is not None: random.seed(seed)
    world = init_world(tweaks=tweaks)
    # use extended season runner from mc_sweep
    from mc_sweep import run_season_extended
    for _ in range(seasons): run_season_extended(world)
    final = {f.name: f.victory_progress(world) for f in world.all_player_factions()}
    winner = max(final, key=final.get)
    return dict(winner=winner, scores=final, world=world)


def run_mc_v3(n, tweaks=None, seasons=12):
    wins = Counter(); finals = defaultdict(list)
    territs = defaultdict(list); rev_tok = defaultdict(list); tokens = defaultdict(list)
    inq = []; crisis = 0; revolts = 0
    for i in range(n):
        r = run_campaign_v3(tweaks=tweaks, seasons=seasons, seed=i)
        wins[r['winner']] += 1
        for fname, score in r['scores'].items():
            finals[fname].append(score)
            territs[fname].append(len(r['world'].factions[fname].territories))
            rev_tok[fname].append(r['world'].factions[fname].revelation_tokens)
            tokens[fname].append(sum(r['world'].factions[fname].tokens_held.values()))
        inq.append(len(r['world'].factions['Church'].inquisitors))
        if r['world'].crisis_active: crisis += 1
        revolts += r['world'].clocks['Strain']
    total = sum(wins.values())
    return dict(
        win_share={k: round(wins.get(k, 0)/total * 100, 1) for k in
                   ['Valorsmark', 'Church', 'Hafenmark', 'Varfell']},
        score_means={k: round(sum(v)/len(v), 1) for k, v in finals.items()},
        score_stds={k: round(math.sqrt(sum((x - sum(v)/len(v))**2 for x in v)/len(v)), 1)
                    for k, v in finals.items()},
        territory_means={k: round(sum(v)/len(v), 2) for k, v in territs.items()},
        rev_tok_means={k: round(sum(v)/len(v), 2) for k, v in rev_tok.items()},
        tokens_means={k: round(sum(v)/len(v), 2) for k, v in tokens.items()},
        inq_mean=round(sum(inq)/len(inq), 2),
        crisis_rate=round(crisis/n * 100, 1),
        revolts_mean=round(revolts/n, 2),
    )


if __name__ == '__main__':
    N = 500
    configs = [
        ('canon (no tweaks)', set()),
        ('top-down min-viable (T-09c+T-02a+T-09b)', {'T-09c', 'T-02a', 'T-09b'}),
        ('all top-down (Parts 3-5)', {'T-01a','T-02a','T-02c','T-03c','T-09a','T-09b','T-09c'}),
        ('T-X1 only (revolt → unaligned)', {'T-X1'}),
        ('T-X2 only (Charter blocks Inq)', {'T-X2'}),
        ('T-X3 only (Garrison blocks drain)', {'T-X3'}),
        ('T-X4 only (PA Session +2L+Token)', {'T-X4'}),
        ('T-X5 only (Varfell Govern→RT)', {'T-X5'}),
        ('emergent core (X1+X2+X4)', {'T-X1','T-X2','T-X4'}),
        ('emergent full (X1+X2+X3+X4+X5)', {'T-X1','T-X2','T-X3','T-X4','T-X5'}),
        ('union: top-down + emergent', {'T-01a','T-02a','T-09c','T-X1','T-X2','T-X3','T-X4','T-X5'}),
    ]
    results = {}
    print(f"Running sweep, {N} campaigns each, corrected victory_progress")
    print("=" * 80)
    for label, tw in configs:
        r = run_mc_v3(N, tweaks=tw)
        results[label] = r
        ws = r['win_share']
        print(f"\n{label}")
        print(f"  V={ws['Valorsmark']:5.1f}% C={ws['Church']:5.1f}% "
              f"H={ws['Hafenmark']:5.1f}% Va={ws['Varfell']:5.1f}%  "
              f"(spread {max(ws.values()) - min(ws.values()):.1f}pp)")
        print(f"  Scores  V={r['score_means']['Valorsmark']:6.1f}  "
              f"C={r['score_means']['Church']:6.1f}  "
              f"H={r['score_means']['Hafenmark']:6.1f}  "
              f"Va={r['score_means']['Varfell']:6.1f}")
        print(f"  Inq mean {r['inq_mean']} | Crisis {r['crisis_rate']}% | Revolts {r['revolts_mean']}")
    open('/home/claude/mc_v3.json', 'w').write(json.dumps(results, indent=2))
    print("\n[saved /home/claude/mc_v3.json]")

    # Identify in-band configs
    print("\n" + "=" * 80)
    print("CONFIGURATIONS WITHIN ±5pp BAND (20-30% per faction):")
    print("=" * 80)
    for label, r in results.items():
        ws = r['win_share']
        in_band = all(20 <= v <= 30 for v in ws.values())
        spread = max(ws.values()) - min(ws.values())
        if in_band or spread < 15:
            print(f"  {label}: spread {spread:.1f}pp; {ws}")
