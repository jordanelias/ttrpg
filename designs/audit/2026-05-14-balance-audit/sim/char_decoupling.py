"""
Character-scale instrumentation on v5 simulator.

Question (Jordan): "is it really a win for Valorsmark re Almud if he gets deposed?"

Faction-scale wins (what v5 currently measures) are not the same as
character-scale outcomes. This instrumentation tracks both, and reports the
emergent decoupling rate.

CHARACTER STATES per faction:
- STRONG: faction Sta ≥ 4, Mandate ≥ 5, no recent submission, no recent Excomm
- WEAK: faction Sta ≤ 2 OR Mandate ≤ 2 in any recent season
- DEPOSED: faction Sta hit 0 (submission, ED-318) OR Mandate ≤ 1 sustained 2+ seasons,
  OR Excommunication landed and Mandate didn't recover within 4 seasons,
  OR territory loss to Hafenmark DP > 50% of starting territories

Per-leader semantic mapping:
- Crown:    'Almud'    (named target of Jordan's question)
- Church:   'Cardinal' (anonymous holder; Excomm by Church inverts: Church Excomming
                       others is Cardinal-strong)
- Hafenmark: 'Baralta'  (per §5.3 canonical text)
- Varfell:  'Vaynard'  (per §5.4 STRUCK canonical text)
"""
import sys, json, random
sys.path.insert(0, '/home/claude')
from collections import defaultdict, Counter
from mc_v4 import (CANONICAL_TERRITORIES, ALL_PLAYABLE_15, Faction, Territory,
                   World, init_world, roll_pool, resolve_degree)
from mc_v5 import select_actions_v5, prereqs_met_v5, pool_and_ob_v5
from mc_v6 import apply_outcome_v6, end_of_season_v6, PARAMS


LEADER_NAMES = {'Crown': 'Almud', 'Church': 'Cardinal',
                'Hafenmark': 'Baralta', 'Varfell': 'Vaynard'}


def classify_leader_state(faction, history):
    """Classify character-scale state. history = list of per-season records for this
    faction: dicts with 'Sta', 'L', 'excommunicated', 'territories_lost_to_dp'."""
    if not history:
        return 'unknown'
    final = history[-1]
    n = len(history)

    # Look at last ~6 seasons for trends
    recent = history[max(0, n - 6):]

    # Submission check (Sta hit 0 anywhere)
    if any(h['Sta'] == 0 for h in history):
        return 'deposed-submission'
    # Mandate collapse — L≤1 sustained 2+ seasons
    low_l = [h['L'] <= 1 for h in recent]
    if sum(low_l) >= 2:
        return 'deposed-mandate-collapse'
    # Excommunication landed and not recovered
    excomm_any = any(h.get('excommunicated', False) for h in history)
    if excomm_any and final['L'] < 4:
        return 'deposed-excommunicated'
    # Hafenmark DP territorial loss (≥ 50% starting territories lost to DP specifically)
    starting = {'Crown': 6, 'Hafenmark': 4, 'Church': 1, 'Varfell': 4}.get(
        history[-1].get('faction'), 4)
    if final.get('territories_lost_to_dp', 0) >= max(2, starting // 2):
        return 'deposed-proclaimed-against'

    # Strong: Sta ≥ 4 AND L ≥ 5 currently
    if final['Sta'] >= 4 and final['L'] >= 5:
        return 'strong'
    # Weak: Sta ≤ 2 or L ≤ 2 currently
    if final['Sta'] <= 2 or final['L'] <= 2:
        return 'weak'
    return 'stable'


def run_campaign_char(params=None, tweaks=None, seed=None):
    """Run with per-season character tracking."""
    if seed is not None: random.seed(seed)
    p = dict(PARAMS); p.update(params or {})
    world = init_world(tweaks=tweaks or set())
    world.params = p

    # Per-faction history
    history = {n: [] for n in world.factions}
    # Track territory transfers (specifically losses to Hafenmark DP)
    dp_losses = defaultdict(int)
    excomm_active = {n: False for n in world.factions}
    last_owner = {tid: t.owner for tid, t in world.territories.items()}

    for _ in range(p['CAMPAIGN_SEASONS']):
        if world.winner: break
        for f in world.factions.values(): f.reset_seasonal()
        acts = []
        for f in world.factions.values():
            acts.extend(select_actions_v5(f, world, n_actions=3))
        for action in acts:
            if not prereqs_met_v5(action, world): continue
            pool, ob = pool_and_ob_v5(action, world)
            net = roll_pool(pool) - ob
            degree = resolve_degree(net)
            # Detect Excommunication landing
            if (action['name'] == 'Excommunication' and
                degree in ('Success', 'Overwhelming')):
                excomm_active[action.get('target')] = True
            apply_outcome_v6(action, degree, world)
        # Detect territory transfers to Hafenmark via DP
        for tid, t in world.territories.items():
            prior = last_owner.get(tid)
            if prior and prior != t.owner and t.owner == 'Hafenmark':
                dp_losses[prior] += 1
            last_owner[tid] = t.owner
        # End-of-season accounting
        end_of_season_v6(world, p['TURMOIL_CAP'])
        # Record state
        for fname, f in world.factions.items():
            history[fname].append(dict(
                faction=fname,
                Sta=f.stats['Sta'],
                L=f.stats['L'],
                territories=len(f.territories),
                excommunicated=excomm_active[fname],
                territories_lost_to_dp=dp_losses[fname],
            ))
        world.season += 1
        if world.season % 4 == 0:
            for f in world.factions.values():
                f.reset_arc(); f.reset_annual()
            world.arc += 1

    # Fallback winner
    winner = world.winner
    if winner is None:
        scores = {}
        for fname, f in world.factions.items():
            h = 0
            for tid in ALL_PLAYABLE_15:
                t = world.territories.get(tid)
                if t and t.owner == fname: h += 1
                elif t and t.owner in world.factions:
                    if f.treaties.get(t.owner, '') in ('CrownTreaty', 'Peace', 'Alliance', 'Capitulation', 'Tributary'):
                        h += 0.5
            scores[fname] = h * 10 + f.stats['L'] + len(f.territories)
        winner = max(scores, key=scores.get)

    leader_states = {fname: classify_leader_state(history[fname], history[fname])
                     for fname in world.factions}
    return dict(winner=winner, leader_states=leader_states, world=world)


def run_mc_char(n, params=None, tweaks=None):
    """MC with character-scale decoupling reporting."""
    wins = Counter()
    leader_state_by_winner = defaultdict(Counter)  # winner → state of winner's leader
    leader_state_global = defaultdict(Counter)     # faction → state distribution
    crown_wins_almud_strong = 0
    crown_wins_almud_deposed = 0
    almud_strong_overall = 0
    almud_deposed_overall = 0
    for i in range(n):
        r = run_campaign_char(params=params, tweaks=tweaks, seed=i)
        w = r['winner']
        wins[w] += 1
        winner_leader_state = r['leader_states'][w]
        leader_state_by_winner[w][winner_leader_state] += 1
        for fname, state in r['leader_states'].items():
            leader_state_global[fname][state] += 1
        # Crown / Almud specific tracking
        almud_state = r['leader_states']['Crown']
        if almud_state == 'strong': almud_strong_overall += 1
        if almud_state.startswith('deposed'): almud_deposed_overall += 1
        if w == 'Crown':
            if almud_state == 'strong': crown_wins_almud_strong += 1
            if almud_state.startswith('deposed'): crown_wins_almud_deposed += 1
    total = sum(wins.values())
    return dict(
        n=n,
        win_share={k: round(wins.get(k, 0)/total*100, 1) for k in
                   ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        leader_state_global={f: dict(d) for f, d in leader_state_global.items()},
        leader_state_by_winner={f: dict(d) for f, d in leader_state_by_winner.items()},
        almud_strong_pct=round(almud_strong_overall / n * 100, 1),
        almud_deposed_pct=round(almud_deposed_overall / n * 100, 1),
        crown_wins_almud_strong_pct=round(crown_wins_almud_strong / max(1, wins.get('Crown', 1)) * 100, 1),
        crown_wins_almud_deposed_pct=round(crown_wins_almud_deposed / max(1, wins.get('Crown', 1)) * 100, 1),
    )


if __name__ == '__main__':
    N = 500
    print("=" * 80)
    print("CHARACTER-SCALE DECOUPLING ANALYSIS — Almud vs Crown")
    print("=" * 80)

    configs = [
        ('canon-v5 (consent=0.5, cap=6, 36s)', dict()),
        ('high consent (Q-1=1.0)', dict(CONSENT_RATE=1.0)),
        ('short campaign (24s)', dict(CAMPAIGN_SEASONS=24)),
        ('long campaign (60s)', dict(CAMPAIGN_SEASONS=60)),
    ]
    all_results = {}
    for label, p in configs:
        r = run_mc_char(N, params=p)
        all_results[label] = r
        ws = r['win_share']
        print(f"\n{label}")
        print(f"  Win share: Cr={ws['Crown']:5.1f}% Ch={ws['Church']:5.1f}% "
              f"Ha={ws['Hafenmark']:5.1f}% Va={ws['Varfell']:5.1f}%")
        print(f"  Almud's fate (across ALL campaigns):")
        print(f"    Strong   {r['almud_strong_pct']:5.1f}%")
        print(f"    Deposed  {r['almud_deposed_pct']:5.1f}%")
        print(f"  Crown 'wins' (faction-scale) but Almud personally:")
        print(f"    Strong   {r['crown_wins_almud_strong_pct']:5.1f}% of Crown's wins")
        print(f"    Deposed  {r['crown_wins_almud_deposed_pct']:5.1f}% of Crown's wins")
        print(f"  Almud state distribution: {r['leader_state_global']['Crown']}")
    open('/home/claude/char_decoupling.json', 'w').write(json.dumps(all_results, indent=2))
    print("\n[saved /home/claude/char_decoupling.json]")
