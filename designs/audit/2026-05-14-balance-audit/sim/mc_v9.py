"""
v9 simulator — INTEGRATED BALANCE SOLUTION

Comprehensive package addressing all structural findings from Parts 7-12:

Q-1 (consent rate): set to 0.75 (Part 8 sweet spot — Crown viable, not dominant)
Q-21 (Church L-compounding): Ecclesiastical Appointment throttled to 1×/arc
Q-22 (Hafenmark cannibalization): Charter of Liberties pure W cost, Ob 5
Q-23 (Varfell acquisition): NEW Vaynard's Settlement action (post-conquest)
Crown Initiative: per Part 10 — character-scale recovery, not faction amplifier
Territorial threshold: 11/15 (Co-Victory analog primary endpoint per Part 8)
Turmoil cap: 12 (relaxed from canonical 6; sensitivity showed it didn't gate)

Goal: 4-way balance spread ≤ 15pp; positive direct sovereignty rate
"""
import sys, json, random
sys.path.insert(0, '/home/claude')
from collections import defaultdict, Counter
from mc_v4 import (ALL_PLAYABLE_15, Faction, Territory, World, init_world,
                   roll_pool, resolve_degree)
from mc_v5 import (prereqs_met_v5, pool_and_ob_v5, score_action_v5,
                   list_candidate_actions_v5)
from mc_v6 import apply_outcome_v6, end_of_season_v6, PARAMS
from mc_v8 import reset_seasonal_v8, reset_arc_v8

# Apply v8 monkey-patches for slot tracking
Faction.reset_seasonal = reset_seasonal_v8
Faction.reset_arc = reset_arc_v8


# ============================================================
# v9 prereqs — implements Q-21/22/23 fixes
# ============================================================

def v9_prereqs(action, world):
    actor = action['actor']
    name = action['name']

    # Q-21: Throttle Ecclesiastical Appointment to 1×/arc
    if name == 'Ecclesiastical Appointment':
        if actor.name != 'Church': return False
        if actor.stats['L'] >= 7: return False
        if getattr(actor, 'ecclesiastical_appointment_arc_used', False): return False
        return True

    if name == 'Crown Initiative':
        if actor.name != 'Crown': return False
        if getattr(actor, 'senator_inward_used', False): return False
        if actor.stats['W'] < 2: return False
        return True

    # Q-23: NEW Vaynard's Settlement action
    if name == "Vaynard's Settlement":
        if actor.name != 'Varfell': return False
        if getattr(actor, 'tribune_card_used', False): return False
        # Target: a territory Varfell acquired by Military Conquest (low Accord)
        target = action.get('target')
        if target not in world.territories: return False
        t = world.territories[target]
        if t.owner != 'Varfell': return False
        if t.accord >= 2: return False  # already secure
        if actor.stats['Mil'] < 3 or actor.stats['W'] < 1: return False
        return True

    # Q-22: Charter of Liberties revised — pure W cost
    if name == 'Charter of Liberties':
        if actor.name != 'Hafenmark': return False
        if getattr(actor, 'legacy_card_used', False): return False
        if actor.stats['W'] < 1: return False
        return True

    return prereqs_met_v5(action, world)


def v9_pool_ob(action, world):
    actor = action['actor']
    name = action['name']

    if name == 'Crown Initiative':
        sum_accord = sum(world.territories[tid].accord
                         for tid in actor.territories if tid in world.territories)
        return actor.stats['I'], max(1, sum_accord // 2)

    if name == "Vaynard's Settlement":
        # Pool: Mil + W (spoils consolidate); Ob 3
        return actor.stats['Mil'] + (actor.stats['W'] // 2), 3

    if name == 'Charter of Liberties':
        # Q-22: Pure W cost, harder Ob (canonical legislative — institutional weight)
        return actor.stats['I'], 5

    return pool_and_ob_v5(action, world)


def v9_apply(action, degree, world):
    actor = action['actor']
    name = action['name']
    success = degree in ('Success', 'Overwhelming')
    overwhelming = degree == 'Overwhelming'

    if name == 'Ecclesiastical Appointment':
        actor.ecclesiastical_appointment_arc_used = True  # throttle marker
        if success:
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
        return

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

    if name == "Vaynard's Settlement":
        actor.tribune_card_used = True
        actor.stats['W'] = max(0, actor.stats['W'] - 1)
        t = world.territories[action['target']]
        if overwhelming:
            t.accord = min(3, t.accord + 2)  # Accord 1 → 3 (full secured)
            t.order = min(5, t.order + 1)
            actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)
        elif degree == 'Success':
            t.accord = min(3, t.accord + 1)  # Accord 1 → 2 (secured)
            t.order = min(5, t.order + 1)
        elif degree == 'Partial':
            t.order = min(5, t.order + 1)  # Settlement progress at least
        # Failure: cost paid, no progress
        return

    if name == 'Charter of Liberties':
        actor.legacy_card_used = True
        # Q-22: Pure W cost (no Token consume)
        actor.stats['W'] = max(0, actor.stats['W'] - 1)
        if overwhelming:
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            world.clocks['PI'] = max(0, world.clocks['PI'] - 2)
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        elif degree == 'Success':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            world.clocks['PI'] = max(0, world.clocks['PI'] - 1)
        elif degree == 'Partial':
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        return

    apply_outcome_v6(action, degree, world)


# ============================================================
# Scoring + candidate enumeration
# ============================================================

def v9_score(action, world):
    name = action['name']
    actor = action['actor']
    if name == 'Crown Initiative':
        return 5 + max(0, 6 - actor.stats['L']) + (4 if actor.stats['L'] <= 3 else 0)
    if name == "Vaynard's Settlement":
        # High priority — secures newly conquered territory
        return 12  # higher than most Varfell options
    if name == 'Charter of Liberties':
        s = 6 + max(0, 6 - actor.stats['L'])
        if world.clocks['PI'] >= 7: s += 3
        return s
    return score_action_v5(action, world)


def v9_list_candidates(faction, world):
    cands = list_candidate_actions_v5(faction, world)
    # Add new flagship cards per faction
    if faction.name == 'Crown':
        a = dict(name='Crown Initiative', actor=faction, target=None)
        if v9_prereqs(a, world): cands.append(a)
    elif faction.name == 'Varfell':
        # Add Vaynard's Settlement for each conquered Varfell territory at Accord<2
        for tid, t in world.territories.items():
            if t.owner == 'Varfell' and t.accord < 2:
                a = dict(name="Vaynard's Settlement", actor=faction, target=tid)
                if v9_prereqs(a, world): cands.append(a)
    elif faction.name == 'Hafenmark':
        a = dict(name='Charter of Liberties', actor=faction, target=None)
        if v9_prereqs(a, world): cands.append(a)
    return cands


def v9_select_actions(faction, world, n_actions=3):
    selected = []
    used = set()
    for _ in range(n_actions):
        cands = v9_list_candidates(faction, world)
        cands = [a for a in cands if (a['name'], a.get('target')) not in used]
        if not cands: break
        scored = [(v9_score(a, world), a) for a in cands]
        scored.sort(key=lambda x: -x[0])
        top = scored[:4]
        weights = [4, 3, 2, 1][:len(top)]
        chosen = random.choices([a for _, a in top], weights=weights, k=1)[0]
        selected.append(chosen)
        used.add((chosen['name'], chosen.get('target')))
    return selected


# ============================================================
# Victory check with adjustable threshold (Co-Victory @ 11/15)
# ============================================================

def universal_victory_v9(world, turmoil_cap, threshold):
    for fname, f in world.factions.items():
        territories_controlled = set()
        for tid in ALL_PLAYABLE_15:
            t = world.territories.get(tid)
            if t is None: continue
            if t.owner == fname:
                territories_controlled.add(tid)
            elif t.owner in world.factions:
                rival = world.factions[t.owner]
                tt = f.treaties.get(rival.name, '')
                if tt in ('CrownTreaty', 'Peace', 'Alliance', 'Capitulation', 'Tributary'):
                    territories_controlled.add(tid)
                elif rival.submitted:
                    territories_controlled.add(tid)
                elif rival.stats['L'] <= 1 and f.stats['L'] >= 5:
                    territories_controlled.add(tid)
        if len(territories_controlled) < threshold:
            f.sovereignty_history = 0; continue
        if not all(world.territories[tid].accord >= 2 for tid in world.territories_owned_by(fname)):
            f.sovereignty_history = 0; continue
        if world.turmoil() > turmoil_cap:
            f.sovereignty_history = 0; continue
        f.sovereignty_history += 1
        if f.sovereignty_history >= 2: return fname
    return None


def end_of_season_v9(world, turmoil_cap, threshold):
    world.clocks['CI'] += 1
    world.clocks['MS'] = max(0, world.clocks['MS'] - 1)
    revolts = 0
    for tid, t in list(world.territories.items()):
        if t.is_uncontrolled(): continue
        if t.accord == 1 and not t.garrison: t.accord = 0
        if t.accord == 0:
            world.clocks['Turmoil'] = world.clocks.get('Turmoil', 0) + 1
            revolts += 1
            if t.garrison:
                c = world.factions[t.owner]
                if (roll_pool(c.stats['Mil']) - 2) >= 1: t.accord = 1
                else:
                    if t.owner in world.factions:
                        world.factions[t.owner].territories.discard(tid)
                    t.owner = None; t.garrison = False; t.inquisitor_holder = None
                    for ff in world.factions.values(): ff.inquisitors.discard(tid)
            else:
                if t.owner in world.factions:
                    world.factions[t.owner].territories.discard(tid)
                t.owner = None; t.inquisitor_holder = None
        if t.garrison and world.season - t.last_hostile_season >= 2:
            t.consec_passive_seasons += 1
            if t.consec_passive_seasons >= 2 and t.accord < 2:
                t.accord += 1; t.consec_passive_seasons = 0
        else: t.consec_passive_seasons = 0
    if revolts == 0:
        world.clocks['Turmoil'] = max(0, world.clocks.get('Turmoil', 0) - 1)
    world.clocks['Strain'] = world.clocks['Turmoil']
    for fname, f in world.factions.items():
        if f.stats['Sta'] <= 2:
            for tid in list(f.territories):
                world.territories[tid].accord = max(0, world.territories[tid].accord - 1)
    winner = universal_victory_v9(world, turmoil_cap, threshold)
    if winner: world.winner = winner


def run_season_v9(world, threshold):
    if world.winner: return
    for f in world.factions.values(): f.reset_seasonal()
    acts = []
    for f in world.factions.values():
        acts.extend(v9_select_actions(f, world, n_actions=3))
    for action in acts:
        if not v9_prereqs(action, world): continue
        pool, ob = v9_pool_ob(action, world)
        net = roll_pool(pool) - ob
        degree = resolve_degree(net)
        v9_apply(action, degree, world)
    end_of_season_v9(world, world.params['TURMOIL_CAP'], threshold)
    world.season += 1
    if world.season % 4 == 0:
        for f in world.factions.values():
            # Reset arc-level slots
            f.pa_session_arc_used = False
            f.influence_surge_arc_used = False
            f.ecclesiastical_appointment_arc_used = False  # Q-21
        world.arc += 1


def run_campaign_v9(params=None, seed=None, threshold=11):
    if seed is not None: random.seed(seed)
    p = dict(PARAMS); p.update(params or {})
    world = init_world(tweaks=set())
    world.params = p
    almud_history = []
    for _ in range(p['CAMPAIGN_SEASONS']):
        if world.winner: break
        run_season_v9(world, threshold)
        crown = world.factions['Crown']
        almud_history.append(dict(Sta=crown.stats['Sta'], L=crown.stats['L']))
    # Fallback
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
    almud_state = 'stable'
    if any(h['Sta'] == 0 for h in almud_history): almud_state = 'deposed-submission'
    elif sum(1 for h in almud_history[-6:] if h['L'] <= 1) >= 2:
        almud_state = 'deposed-mandate-collapse'
    elif almud_history and almud_history[-1]['Sta'] >= 4 and almud_history[-1]['L'] >= 5:
        almud_state = 'strong'
    elif almud_history and (almud_history[-1]['Sta'] <= 2 or almud_history[-1]['L'] <= 2):
        almud_state = 'weak'
    return dict(winner=winner, almud_state=almud_state, world=world)


def run_mc_v9(n, params=None, threshold=11):
    wins = Counter()
    states = Counter()
    L_final = defaultdict(list)
    territories_final = defaultdict(list)
    direct = 0
    turmoil = []
    for i in range(n):
        r = run_campaign_v9(params=params, seed=i, threshold=threshold)
        wins[r['winner']] += 1
        states[r['almud_state']] += 1
        for fname, f in r['world'].factions.items():
            L_final[fname].append(f.stats['L'])
            territories_final[fname].append(len(f.territories))
        if r['world'].winner: direct += 1
        turmoil.append(r['world'].clocks['Turmoil'])
    total = sum(wins.values())
    return dict(
        n=n,
        win_share={k: round(wins.get(k, 0)/total*100, 1) for k in ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        L_mean={k: round(sum(v)/len(v), 2) for k, v in L_final.items()},
        terr_mean={k: round(sum(v)/len(v), 2) for k, v in territories_final.items()},
        direct_rate=round(direct/n*100, 1),
        turmoil_mean=round(sum(turmoil)/len(turmoil), 2),
        almud_strong=round(states.get('strong', 0)/n*100, 1),
        almud_deposed=round(sum(v for k, v in states.items() if k.startswith('deposed'))/n*100, 1),
    )


if __name__ == '__main__':
    N = 500
    print("=" * 80)
    print("v9 — INTEGRATED BALANCE SOLUTION")
    print("Q-21: EA throttled to 1×/arc | Q-22: Charter pure W cost | Q-23: Vaynard's Settlement")
    print("Q-1: consent=0.75 | Co-Victory threshold 11/15 | Turmoil cap 12")
    print("=" * 80)

    # ABLATION SWEEP: which fix matters most?
    configs = [
        ('canon-v5 baseline (no fixes)',
         dict(CONSENT_RATE=0.5, TURMOIL_CAP=6), 15),
        ('Q-1 only (consent=0.75)',
         dict(CONSENT_RATE=0.75, TURMOIL_CAP=6), 15),
        ('Q-1 + threshold 11/15',
         dict(CONSENT_RATE=0.75, TURMOIL_CAP=12), 11),
        ('v9 INTEGRATED (all fixes)',
         dict(CONSENT_RATE=0.75, TURMOIL_CAP=12), 11),
        ('v9 + short campaign (24s)',
         dict(CONSENT_RATE=0.75, TURMOIL_CAP=12, CAMPAIGN_SEASONS=24), 11),
        ('v9 + 50-season campaign',
         dict(CONSENT_RATE=0.75, TURMOIL_CAP=12, CAMPAIGN_SEASONS=50), 11),
    ]
    all_results = {}
    for label, params, threshold in configs:
        r = run_mc_v9(N, params=params, threshold=threshold)
        all_results[label] = r
        ws = r['win_share']
        spread = max(ws.values()) - min(ws.values())
        status = '✓ CLOSED' if spread <= 15 else ('~ partial' if spread <= 25 else '✗ open')
        print(f"\n{label}")
        print(f"  Cr={ws['Crown']:5.1f}% Ch={ws['Church']:5.1f}% "
              f"Ha={ws['Hafenmark']:5.1f}% Va={ws['Varfell']:5.1f}%   "
              f"spread {spread:.1f}pp {status}")
        print(f"  L_mean: Cr={r['L_mean']['Crown']:.2f} Ch={r['L_mean']['Church']:.2f} "
              f"Ha={r['L_mean']['Hafenmark']:.2f} Va={r['L_mean']['Varfell']:.2f}")
        print(f"  Territories: {r['terr_mean']}")
        print(f"  Direct sovereignty: {r['direct_rate']:.1f}% | "
              f"Almud strong: {r['almud_strong']:.1f}% | deposed: {r['almud_deposed']:.1f}%")
        print(f"  Turmoil mean: {r['turmoil_mean']}")

    # Final summary
    print("\n" + "=" * 80)
    print("BALANCE CLOSURE CHECK")
    print("=" * 80)
    for label, r in all_results.items():
        ws = r['win_share']
        spread = max(ws.values()) - min(ws.values())
        status = '✓ CLOSED (≤15pp)' if spread <= 15 else ('~ partial (≤25pp)' if spread <= 25 else '✗ open')
        print(f"  {label[:40]:40s}: spread {spread:5.1f}pp  direct {r['direct_rate']:5.1f}%  {status}")
    open('/home/claude/mc_v9_integrated.json', 'w').write(json.dumps(all_results, indent=2))
