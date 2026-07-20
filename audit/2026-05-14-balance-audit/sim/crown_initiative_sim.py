"""
Crown Initiative — prototype card for canonical Mandate-increase mechanic.

Historical precedent → mechanical translation:
- Royal Progress (Henry I, Elizabeth I): king tours own realm, +L from direct
  contact + dispensed justice. Cost: treasury for entertainment & gifts.
- Codification (Justinian, Napoleon, Edward I): great legal project. Cost: time
  + treasury. Benefit: institutional permanent +L.
- Coronation/Anointing (Charlemagne by Leo III): Church renews monarch's sacred
  mandate. Cost: concessions to Church + treasury. Benefit: lift Excommunication
  + sacred +L. Recovery mode.
- Patronage of public works (Versailles, Suleiman's mosques, Hadrian's Wall):
  W expenditure → +L through grandeur + popular favor.
- Marriage alliance (Habsburgs): dynastic +L through union. (Not modeled here —
  fits faction-treaty surface already.)

Design choice: ONE card "Crown Initiative" with three modes player chooses at
play. Each maps to a historical pattern. Modes have different cost/risk/payoff
profiles. Slot: new "Senator Inward" 1×/season (separate from "Senator Outward"
used for Crown Treaty).

For sim test, implement Mode I (Royal Progress) — the simplest mode — and
measure impact on canon-v5 results.
"""
import sys, json, random
sys.path.insert(0, '/home/claude')
from collections import defaultdict, Counter
from mc_v4 import (ALL_PLAYABLE_15, Faction, Territory, World, init_world,
                   roll_pool, resolve_degree)
from mc_v5 import select_actions_v5, prereqs_met_v5, pool_and_ob_v5
from mc_v6 import apply_outcome_v6, end_of_season_v6, PARAMS


def crown_initiative_prereqs(action, world):
    """Crown Initiative prereqs."""
    actor = action['actor']
    if actor.name != 'Crown': return False
    # New slot: senator_inward_used (separate from senator_card_used for Crown Treaty)
    if getattr(actor, 'senator_inward_used', False): return False
    mode = action.get('mode', 'progress')
    if mode == 'progress':
        # Cost: W -2
        if actor.stats['W'] < 2: return False
        return True
    elif mode == 'coronation':
        # Recovery mode: requires Crown-Church Treaty OR Truce; cost W -2
        if actor.stats['W'] < 2: return False
        treaty = actor.treaties.get('Church', '')
        if treaty not in ('CrownTreaty', 'Peace', 'Truce', 'Alliance'): return False
        return True
    return False


def crown_initiative_pool_ob(action, world):
    """Crown Initiative pool + Ob calculation."""
    actor = action['actor']
    mode = action.get('mode', 'progress')
    if mode == 'progress':
        # Pool: Influence. Ob: floor(sum own territories Accord / 2)
        sum_accord = sum(world.territories[tid].accord
                         for tid in actor.territories
                         if tid in world.territories)
        ob = max(1, sum_accord // 2)
        return actor.stats['I'], ob
    elif mode == 'coronation':
        # Pool: I. Ob: Church L / 2 + 1
        church = world.factions.get('Church')
        ob = (church.stats['L'] // 2) + 1 if church else 3
        return actor.stats['I'], ob
    return 3, 3


def crown_initiative_apply(action, degree, world):
    """Apply Crown Initiative effects."""
    actor = action['actor']
    mode = action.get('mode', 'progress')
    actor.senator_inward_used = True

    if mode == 'progress':
        actor.stats['W'] = max(0, actor.stats['W'] - 2)  # treasury cost
        if degree == 'Overwhelming':
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
            # All Crown territories at Accord 1 → Accord 2
            for tid in actor.territories:
                t = world.territories[tid]
                if t.accord == 1: t.accord = 2
        elif degree == 'Success':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            # One territory of choice (lowest Accord) → +1 Accord
            if actor.territories:
                worst = min((world.territories[tid] for tid in actor.territories),
                            key=lambda t: t.accord)
                worst.accord = min(3, worst.accord + 1)
        elif degree == 'Partial':
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)  # at least good optics
        # Failure: cost paid, no L gain
    elif mode == 'coronation':
        actor.stats['W'] = max(0, actor.stats['W'] - 2)
        if degree in ('Success', 'Overwhelming'):
            actor.stats['L'] = min(7, actor.stats['L'] + (2 if degree == 'Overwhelming' else 1))
            # Lift Excommunication-equivalent state (lost L from Excommunication = mandate scar)
            # For sim purposes: if L was recently dropped, recover further
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        elif degree == 'Partial':
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)


# --- Patch the prereqs / apply / score functions to recognize Crown Initiative ---

_orig_prereqs = prereqs_met_v5
_orig_pool_ob = pool_and_ob_v5
_orig_apply = apply_outcome_v6

def prereqs_met_v7(action, world):
    if action['name'] == 'Crown Initiative':
        return crown_initiative_prereqs(action, world)
    return _orig_prereqs(action, world)

def pool_and_ob_v7(action, world):
    if action['name'] == 'Crown Initiative':
        return crown_initiative_pool_ob(action, world)
    return _orig_pool_ob(action, world)

def apply_outcome_v7(action, degree, world):
    if action['name'] == 'Crown Initiative':
        return crown_initiative_apply(action, degree, world)
    return _orig_apply(action, degree, world)


def score_initiative(action, world):
    actor = action['actor']
    mode = action.get('mode', 'progress')
    s = 0
    if mode == 'progress':
        # Score high if L is below max (recovery)
        s = 4 + max(0, 6 - actor.stats['L'])  # higher score when L is lower
        if actor.stats['W'] >= 4: s += 2  # plenty of treasury
        if actor.stats['L'] <= 3: s += 6  # urgent recovery
    elif mode == 'coronation':
        s = 3 + max(0, 6 - actor.stats['L'])
        if actor.stats['L'] <= 3: s += 8  # high priority recovery
    return s


def select_actions_v7(faction, world, n_actions=3):
    """Extends v5 selection to consider Crown Initiative for Crown."""
    selected = []
    used_targets = set()
    for _ in range(n_actions):
        cands = []
        # Generate base candidates from v5 logic
        from mc_v5 import list_candidate_actions_v5
        cands.extend(list_candidate_actions_v5(faction, world))
        # Add Crown Initiative for Crown
        if faction.name == 'Crown':
            for mode in ('progress', 'coronation'):
                act = dict(name='Crown Initiative', actor=faction, target=None, mode=mode)
                if crown_initiative_prereqs(act, world):
                    cands.append(act)
        cands = [a for a in cands if (a['name'], a.get('target'), a.get('mode'))
                 not in used_targets]
        if not cands: break
        # Score
        scored = []
        for a in cands:
            if a['name'] == 'Crown Initiative':
                scored.append((score_initiative(a, world), a))
            else:
                from mc_v5 import score_action_v5
                scored.append((score_action_v5(a, world), a))
        scored.sort(key=lambda x: -x[0])
        top = scored[:4]
        weights = [4, 3, 2, 1][:len(top)]
        chosen = random.choices([a for _, a in top], weights=weights, k=1)[0]
        selected.append(chosen)
        used_targets.add((chosen['name'], chosen.get('target'), chosen.get('mode')))
    return selected


def reset_seasonal_v7(self):
    """Extend reset to clear new slot."""
    self.royal_guard_available = True
    self.cardinal_focus_used_this_season = False
    self.diplomat_card_used = False
    self.senator_card_used = False
    self.senator_inward_used = False  # NEW
Faction.reset_seasonal = reset_seasonal_v7


def run_campaign_v7(params=None, tweaks=None, seed=None, enable_initiative=True):
    """Run with Crown Initiative enabled or disabled."""
    if seed is not None: random.seed(seed)
    p = dict(PARAMS); p.update(params or {})
    world = init_world(tweaks=tweaks or set())
    world.params = p

    # Track Almud-state for decoupling analysis
    almud_history = []

    for _ in range(p['CAMPAIGN_SEASONS']):
        if world.winner: break
        for f in world.factions.values(): f.reset_seasonal()
        acts = []
        for f in world.factions.values():
            if f.name == 'Crown' and enable_initiative:
                acts.extend(select_actions_v7(f, world, n_actions=3))
            else:
                acts.extend(select_actions_v5(f, world, n_actions=3))
        for action in acts:
            if not prereqs_met_v7(action, world): continue
            pool, ob = pool_and_ob_v7(action, world)
            net = roll_pool(pool) - ob
            degree = resolve_degree(net)
            apply_outcome_v7(action, degree, world)
        end_of_season_v6(world, p['TURMOIL_CAP'])
        crown = world.factions['Crown']
        almud_history.append(dict(Sta=crown.stats['Sta'], L=crown.stats['L']))
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

    # Classify Almud state
    almud_state = 'stable'
    if any(h['Sta'] == 0 for h in almud_history): almud_state = 'deposed-submission'
    elif sum(1 for h in almud_history[-6:] if h['L'] <= 1) >= 2:
        almud_state = 'deposed-mandate-collapse'
    elif almud_history and almud_history[-1]['Sta'] >= 4 and almud_history[-1]['L'] >= 5:
        almud_state = 'strong'
    elif almud_history and (almud_history[-1]['Sta'] <= 2 or almud_history[-1]['L'] <= 2):
        almud_state = 'weak'
    return dict(winner=winner, almud_state=almud_state, world=world)


def run_mc_v7(n, params=None, tweaks=None, enable=True):
    wins = Counter()
    states = Counter()
    crown_wins_almud_deposed = 0
    almud_strong_count = 0
    almud_deposed_count = 0
    for i in range(n):
        r = run_campaign_v7(params=params, tweaks=tweaks, seed=i, enable_initiative=enable)
        wins[r['winner']] += 1
        states[r['almud_state']] += 1
        if r['almud_state'] == 'strong': almud_strong_count += 1
        if r['almud_state'].startswith('deposed'): almud_deposed_count += 1
        if r['winner'] == 'Crown' and r['almud_state'].startswith('deposed'):
            crown_wins_almud_deposed += 1
    total = sum(wins.values())
    return dict(
        win_share={k: round(wins.get(k, 0)/total*100, 1) for k in ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        almud_strong_pct=round(almud_strong_count / n * 100, 1),
        almud_deposed_pct=round(almud_deposed_count / n * 100, 1),
        crown_pyrrhic_pct=round(crown_wins_almud_deposed / max(1, wins.get('Crown', 1)) * 100, 1),
        states={k: v for k, v in states.most_common()},
    )


if __name__ == '__main__':
    N = 500
    print("=" * 80)
    print("CROWN INITIATIVE SIMULATION TEST — does it move the needle?")
    print("=" * 80)

    configs = [
        ('canon-v5 (no Crown Initiative)', dict(), False),
        ('canon + Crown Initiative ENABLED', dict(), True),
        ('long campaign (60s) WITHOUT Initiative', dict(CAMPAIGN_SEASONS=60), False),
        ('long campaign (60s) WITH Initiative', dict(CAMPAIGN_SEASONS=60), True),
        ('high consent (Q-1=1.0) WITHOUT Initiative', dict(CONSENT_RATE=1.0), False),
        ('high consent (Q-1=1.0) WITH Initiative', dict(CONSENT_RATE=1.0), True),
    ]
    results = {}
    for label, params, enable in configs:
        r = run_mc_v7(N, params=params, enable=enable)
        results[label] = r
        ws = r['win_share']
        print(f"\n{label}")
        print(f"  Crown win-share: {ws['Crown']:5.1f}%  "
              f"Church: {ws['Church']:5.1f}%  Hafenmark: {ws['Hafenmark']:5.1f}%  "
              f"Varfell: {ws['Varfell']:5.1f}%")
        print(f"  Almud Strong: {r['almud_strong_pct']:5.1f}%  "
              f"Almud Deposed: {r['almud_deposed_pct']:5.1f}%  "
              f"Pyrrhic wins: {r['crown_pyrrhic_pct']:5.1f}%")
    open('/home/claude/crown_initiative_test.json', 'w').write(json.dumps(results, indent=2))
    print("\n[saved /home/claude/crown_initiative_test.json]")
