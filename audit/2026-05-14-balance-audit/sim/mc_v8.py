"""
v8 simulator — closes stalled trajectories.

Adds four faction Mandate-recovery cards from Part 10 §5:
- Crown Initiative (Mode I — Royal Progress)
- Varfell Vaynard's Hall
- Hafenmark Charter of Liberties
- Church Council of Solmund

Verifies whether 4-way balance closes when all 4 factions have flagship
L-recovery mechanics. Target: ≤ 15pp spread in win-share at canonical params.
"""
import sys, json, random
sys.path.insert(0, '/home/claude')
from collections import defaultdict, Counter
from mc_v4 import (ALL_PLAYABLE_15, Faction, Territory, World, init_world,
                   roll_pool, resolve_degree, make_action)
from mc_v5 import (prereqs_met_v5, pool_and_ob_v5, score_action_v5,
                   list_candidate_actions_v5)
from mc_v6 import apply_outcome_v6, end_of_season_v6, PARAMS

# ============================================================
# Reset hook — add slots for new cards
# ============================================================

def reset_seasonal_v8(self):
    self.royal_guard_available = True
    self.cardinal_focus_used_this_season = False
    self.diplomat_card_used = False
    self.senator_card_used = False
    self.senator_inward_used = False        # Crown Initiative slot
    self.tribune_card_used = False          # Varfell Vaynard's Hall (new tribune card)
    self.legacy_card_used = False           # Hafenmark Charter of Liberties (limited)

def reset_arc_v8(self):
    self.pa_session_arc_used = False
    self.influence_surge_arc_used = False
    self.council_used_this_arc = False      # Church Council 1×/arc

Faction.reset_seasonal = reset_seasonal_v8
_orig_reset_arc = Faction.reset_arc
Faction.reset_arc = reset_arc_v8


# ============================================================
# New cards: prereqs + pool/ob + apply
# ============================================================

def v8_prereqs(action, world):
    actor = action['actor']
    name = action['name']

    if name == 'Crown Initiative':
        if actor.name != 'Crown': return False
        if getattr(actor, 'senator_inward_used', False): return False
        if actor.stats['W'] < 2: return False
        return True

    if name == "Vaynard's Hall":
        if actor.name != 'Varfell': return False
        if getattr(actor, 'tribune_card_used', False): return False
        if actor.stats['Mil'] < 2 or actor.stats['W'] < 1: return False
        return True

    if name == 'Charter of Liberties':
        if actor.name != 'Hafenmark': return False
        if getattr(actor, 'legacy_card_used', False): return False
        if sum(actor.tokens_held.values()) < 1: return False  # need at least 1 Token to spend
        if actor.stats['W'] < 1: return False
        return True

    if name == 'Council of Solmund':
        if actor.name != 'Church': return False
        if getattr(actor, 'council_used_this_arc', False): return False
        if actor.cardinal_focus is None: return False  # require active CF to consume
        return True

    return prereqs_met_v5(action, world)


def v8_pool_ob(action, world):
    actor = action['actor']
    name = action['name']

    if name == 'Crown Initiative':
        sum_accord = sum(world.territories[tid].accord
                         for tid in actor.territories if tid in world.territories)
        return actor.stats['I'], max(1, sum_accord // 2)

    if name == "Vaynard's Hall":
        return actor.stats['Mil'] + (1 if actor.revelation_tokens >= 1 else 0), 3

    if name == 'Charter of Liberties':
        return actor.stats['I'] + sum(actor.tokens_held.values()), 4

    if name == 'Council of Solmund':
        return actor.stats['L'], (world.clocks['CI'] // 30) + 2

    return pool_and_ob_v5(action, world)


def v8_apply(action, degree, world):
    actor = action['actor']
    name = action['name']
    success = degree in ('Success', 'Overwhelming')
    overwhelming = degree == 'Overwhelming'

    if name == 'Crown Initiative':
        actor.senator_inward_used = True
        actor.stats['W'] = max(0, actor.stats['W'] - 2)
        if overwhelming:
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
            for tid in actor.territories:
                t = world.territories[tid]
                if t.accord == 1: t.accord = 2
        elif degree == 'Success':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            if actor.territories:
                worst = min((world.territories[tid] for tid in actor.territories),
                            key=lambda t: t.accord)
                worst.accord = min(3, worst.accord + 1)
        elif degree == 'Partial':
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        return

    if name == "Vaynard's Hall":
        actor.tribune_card_used = True
        actor.stats['Mil'] = max(1, actor.stats['Mil'] - 1)
        actor.stats['W'] = max(0, actor.stats['W'] - 1)
        if overwhelming:
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            # Public insult: choose strongest rival, L -1
            rivals = [(f, f.stats['L']) for f in world.factions.values()
                      if f.name != actor.name]
            if rivals:
                victim = max(rivals, key=lambda x: x[1])[0]
                victim.stats['L'] = max(1, victim.stats['L'] - 1)
        elif degree == 'Success':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            if actor.revelation_tokens >= 1:
                actor.revelation_tokens -= 1  # sacrifice token
                # +1 Standing — model as +1 Sta
                actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        elif degree == 'Partial':
            actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)  # rally pays off
        # Failure: cost paid, no gain
        return

    if name == 'Charter of Liberties':
        actor.legacy_card_used = True
        # Consume one Token (any held)
        for k in list(actor.tokens_held.keys()):
            if actor.tokens_held[k] > 0:
                actor.tokens_held[k] -= 1
                if actor.tokens_held[k] == 0:
                    del actor.tokens_held[k]
                break
        actor.stats['W'] = max(0, actor.stats['W'] - 1)
        if overwhelming:
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            world.clocks['PI'] = max(0, world.clocks['PI'] - 2)
            # Excomm protection: flag — simplification, just bump Sta
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        elif degree == 'Success':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            world.clocks['PI'] = max(0, world.clocks['PI'] - 1)
        elif degree == 'Partial':
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        return

    if name == 'Council of Solmund':
        actor.council_used_this_arc = True
        actor.cardinal_focus = None  # consume CF
        if overwhelming:
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            # Formal censure: strongest rival L -1
            rivals = [(f, f.stats['L']) for f in world.factions.values()
                      if f.name != actor.name]
            if rivals:
                victim = max(rivals, key=lambda x: x[1])[0]
                victim.stats['L'] = max(1, victim.stats['L'] - 1)
        elif degree == 'Success':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
        elif degree == 'Partial':
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        return

    apply_outcome_v6(action, degree, world)


# ============================================================
# Score + list_candidates extensions
# ============================================================

def v8_score(action, world):
    name = action['name']
    actor = action['actor']
    if name == 'Crown Initiative':
        return 5 + max(0, 6 - actor.stats['L']) + (4 if actor.stats['L'] <= 3 else 0)
    if name == "Vaynard's Hall":
        return 6 + max(0, 6 - actor.stats['L']) + (3 if actor.stats['L'] <= 3 else 0)
    if name == 'Charter of Liberties':
        # Higher priority when at Crisis or when L is low
        s = 4 + max(0, 6 - actor.stats['L'])
        if world.clocks['PI'] >= 7: s += 4
        return s
    if name == 'Council of Solmund':
        return 8 + max(0, 6 - actor.stats['L'])
    return score_action_v5(action, world)


def v8_list_candidates(faction, world):
    cands = list_candidate_actions_v5(faction, world)
    # Add the new flagship cards
    if faction.name == 'Crown':
        a = dict(name='Crown Initiative', actor=faction, target=None)
        if v8_prereqs(a, world): cands.append(a)
    elif faction.name == 'Varfell':
        a = dict(name="Vaynard's Hall", actor=faction, target=None)
        if v8_prereqs(a, world): cands.append(a)
    elif faction.name == 'Hafenmark':
        a = dict(name='Charter of Liberties', actor=faction, target=None)
        if v8_prereqs(a, world): cands.append(a)
    elif faction.name == 'Church':
        a = dict(name='Council of Solmund', actor=faction, target=None)
        if v8_prereqs(a, world): cands.append(a)
    return cands


def v8_select_actions(faction, world, n_actions=3):
    selected = []
    used = set()
    for _ in range(n_actions):
        cands = v8_list_candidates(faction, world)
        cands = [a for a in cands if (a['name'], a.get('target')) not in used]
        if not cands: break
        scored = [(v8_score(a, world), a) for a in cands]
        scored.sort(key=lambda x: -x[0])
        top = scored[:4]
        weights = [4, 3, 2, 1][:len(top)]
        chosen = random.choices([a for _, a in top], weights=weights, k=1)[0]
        selected.append(chosen)
        used.add((chosen['name'], chosen.get('target')))
    return selected


# ============================================================
# Run pipeline
# ============================================================

def run_season_v8(world):
    if world.winner: return
    for f in world.factions.values(): f.reset_seasonal()
    acts = []
    for f in world.factions.values():
        acts.extend(v8_select_actions(f, world, n_actions=3))
    for action in acts:
        if not v8_prereqs(action, world): continue
        pool, ob = v8_pool_ob(action, world)
        net = roll_pool(pool) - ob
        degree = resolve_degree(net)
        v8_apply(action, degree, world)
    end_of_season_v6(world, world.params['TURMOIL_CAP'])
    world.season += 1
    if world.season % 4 == 0:
        for f in world.factions.values():
            f.reset_arc()
        world.arc += 1


def run_campaign_v8(params=None, seed=None, enable=True):
    if seed is not None: random.seed(seed)
    p = dict(PARAMS); p.update(params or {})
    world = init_world(tweaks=set())
    world.params = p

    # Track Almud state
    almud_history = []

    for _ in range(p['CAMPAIGN_SEASONS']):
        if world.winner: break
        if enable:
            run_season_v8(world)
        else:
            # Fall back to v5/v6 behavior
            from mc_v6 import run_season_v6 as run_season_v6
            # Actually we need v6's run_season; recreate inline
            for f in world.factions.values(): f.reset_seasonal()
            acts = []
            for f in world.factions.values():
                acts.extend(v8_select_actions(f, world, n_actions=3) if False
                            else __import__('mc_v5').select_actions_v5(f, world, n_actions=3))
            for action in acts:
                if not prereqs_met_v5(action, world): continue
                pool, ob = pool_and_ob_v5(action, world)
                net = roll_pool(pool) - ob
                degree = resolve_degree(net)
                apply_outcome_v6(action, degree, world)
            end_of_season_v6(world, p['TURMOIL_CAP'])
            world.season += 1
            if world.season % 4 == 0:
                for f in world.factions.values(): f.reset_arc()
                world.arc += 1
        crown = world.factions['Crown']
        almud_history.append(dict(Sta=crown.stats['Sta'], L=crown.stats['L']))

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

    # Almud state
    almud_state = 'stable'
    if any(h['Sta'] == 0 for h in almud_history): almud_state = 'deposed-submission'
    elif sum(1 for h in almud_history[-6:] if h['L'] <= 1) >= 2:
        almud_state = 'deposed-mandate-collapse'
    elif almud_history and almud_history[-1]['Sta'] >= 4 and almud_history[-1]['L'] >= 5:
        almud_state = 'strong'
    elif almud_history and (almud_history[-1]['Sta'] <= 2 or almud_history[-1]['L'] <= 2):
        almud_state = 'weak'

    return dict(winner=winner, almud_state=almud_state, world=world)


def run_mc_v8(n, params=None, enable=True):
    wins = Counter()
    final_L = defaultdict(list)
    state_count = Counter()
    for i in range(n):
        r = run_campaign_v8(params=params, seed=i, enable=enable)
        wins[r['winner']] += 1
        state_count[r['almud_state']] += 1
        for fname, f in r['world'].factions.items():
            final_L[fname].append(f.stats['L'])
    total = sum(wins.values())
    return dict(
        win_share={k: round(wins.get(k, 0)/total*100, 1) for k in
                   ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        final_L_mean={k: round(sum(v)/len(v), 2) for k, v in final_L.items()},
        almud_states=dict(state_count),
    )


if __name__ == '__main__':
    N = 500
    print("=" * 80)
    print("v8 — 4-faction analog cards (all four L-recovery mechanics)")
    print("=" * 80)

    configs = [
        ('canon (no new cards)', dict(), False),
        ('canon + 4 analog cards (all)', dict(), True),
        ('consent=0.75 + 4 analog cards', dict(CONSENT_RATE=0.75), True),
        ('consent=0.5 + 4 analogs + 50s', dict(CONSENT_RATE=0.5, CAMPAIGN_SEASONS=50), True),
        ('consent=0.5 + 4 analogs + 24s', dict(CONSENT_RATE=0.5, CAMPAIGN_SEASONS=24), True),
    ]
    results = {}
    for label, params, enable in configs:
        r = run_mc_v8(N, params=params, enable=enable)
        results[label] = r
        ws = r['win_share']
        spread = max(ws.values()) - min(ws.values())
        print(f"\n{label}")
        print(f"  Cr={ws['Crown']:5.1f}% Ch={ws['Church']:5.1f}% "
              f"Ha={ws['Hafenmark']:5.1f}% Va={ws['Varfell']:5.1f}%   "
              f"(spread {spread:.1f}pp)")
        print(f"  Final L: {r['final_L_mean']}")
        print(f"  Almud states: {r['almud_states']}")

    # Check 4-way balance closure
    print("\n" + "=" * 80)
    print("4-way balance closure check (target: spread ≤ 15pp)")
    print("=" * 80)
    for label, r in results.items():
        ws = r['win_share']
        spread = max(ws.values()) - min(ws.values())
        status = '✓ CLOSED' if spread <= 15 else ('~ partial' if spread <= 25 else '✗ open')
        print(f"  {label}: spread {spread:.1f}pp  {status}")

    open('/home/claude/mc_v8_4analogs.json', 'w').write(json.dumps(results, indent=2))
