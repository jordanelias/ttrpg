"""
v10 simulator — REFINED INTEGRATED BALANCE

v9 over-corrected: Crown 69% (too high), Hafenmark 12% (under), Varfell 2% (way under).
v10 tunes:

- Q-21 SOFTER: Ecclesiastical Appointment every-other-arc (effectively per ~8 seasons)
  vs v9's every arc. Church recovers some power.
- Q-1 SOFTER: consent=0.6 (middle of 0.5/0.75). Crown win-rate drops back toward band.
- Charter of Liberties EFFECTS BOOSTED: L+1 even on Partial; tokens-on-rivals add +1 L on Success
- Varfell adds Vaynard's Hall (per Part 10 §5.3): Tribune card, Mil+1 pool vs Ob 3, L+1 on
  Success, L+2 on OW. Sacrifices a Revelation Token for +1 Standing/Sta.
- Vaynard's Settlement retained (post-conquest consolidation)
- Crown Initiative cost up to W -3 (was -2) — slows Crown's recovery momentum slightly
"""
import sys, json, random
sys.path.insert(0, '/home/claude')
from collections import defaultdict, Counter
from mc_v4 import (ALL_PLAYABLE_15, Faction, Territory, World, init_world,
                   roll_pool, resolve_degree)
from mc_v5 import (prereqs_met_v5, pool_and_ob_v5, score_action_v5,
                   list_candidate_actions_v5)
from mc_v6 import apply_outcome_v6, PARAMS
from mc_v8 import reset_seasonal_v8

Faction.reset_seasonal = reset_seasonal_v8


def v10_prereqs(action, world):
    actor = action['actor']
    name = action['name']

    # Q-21 SOFTER: EA fires every-other-arc (2 per 36s campaign vs 3 in v9, 12 in canon)
    if name == 'Ecclesiastical Appointment':
        if actor.name != 'Church': return False
        if actor.stats['L'] >= 7: return False
        if getattr(actor, 'ecclesiastical_appointment_arc_used', False): return False
        if getattr(actor, 'ea_last_arc', -10) >= world.arc - 1:  # 2-arc cooldown
            return False
        return True

    if name == 'Crown Initiative':
        if actor.name != 'Crown': return False
        if getattr(actor, 'senator_inward_used', False): return False
        if actor.stats['W'] < 3: return False  # COST UP from 2 to 3
        return True

    if name == "Vaynard's Settlement":
        if actor.name != 'Varfell': return False
        if getattr(actor, 'tribune_card_used', False): return False
        target = action.get('target')
        if target not in world.territories: return False
        t = world.territories[target]
        if t.owner != 'Varfell' or t.accord >= 2: return False
        if actor.stats['Mil'] < 3 or actor.stats['W'] < 1: return False
        return True

    if name == "Vaynard's Hall":
        # NEW per Part 10 §5.3 — gives Varfell an L-gain card
        if actor.name != 'Varfell': return False
        if getattr(actor, 'hall_card_used', False): return False
        if actor.stats['Mil'] < 3 or actor.stats['W'] < 1: return False
        return True

    if name == 'Charter of Liberties':
        if actor.name != 'Hafenmark': return False
        if getattr(actor, 'legacy_card_used', False): return False
        if actor.stats['W'] < 1: return False
        return True

    return prereqs_met_v5(action, world)


def v10_pool_ob(action, world):
    actor = action['actor']
    name = action['name']
    if name == 'Crown Initiative':
        sum_accord = sum(world.territories[tid].accord
                         for tid in actor.territories if tid in world.territories)
        return actor.stats['I'], max(1, sum_accord // 2)
    if name == "Vaynard's Settlement":
        return actor.stats['Mil'] + (actor.stats['W'] // 2), 3
    if name == "Vaynard's Hall":
        return actor.stats['Mil'] + (1 if actor.revelation_tokens >= 1 else 0), 3
    if name == 'Charter of Liberties':
        # +1 pool per active Token on rival (synergy with Diplomat Card)
        token_bonus = sum(1 for v in actor.tokens_held.values() if v > 0)
        return actor.stats['I'] + token_bonus, 4  # Ob 4 down from 5 (less harsh)
    return pool_and_ob_v5(action, world)


def v10_apply(action, degree, world):
    actor = action['actor']
    name = action['name']
    success = degree in ('Success', 'Overwhelming')
    overwhelming = degree == 'Overwhelming'

    if name == 'Ecclesiastical Appointment':
        actor.ecclesiastical_appointment_arc_used = True
        actor.ea_last_arc = world.arc  # mark for cooldown
        if success:
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
        return

    if name == 'Crown Initiative':
        actor.senator_inward_used = True
        actor.stats['W'] = max(0, actor.stats['W'] - 3)  # COST UP
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
            t.accord = min(3, t.accord + 2)
            t.order = min(5, t.order + 1)
            actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)
        elif degree == 'Success':
            t.accord = min(3, t.accord + 1)
            t.order = min(5, t.order + 1)
        elif degree == 'Partial':
            t.order = min(5, t.order + 1)
        return

    if name == "Vaynard's Hall":
        actor.hall_card_used = True
        actor.stats['Mil'] = max(1, actor.stats['Mil'] - 1)  # warband leaves front
        actor.stats['W'] = max(0, actor.stats['W'] - 1)
        if overwhelming:
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            # Public insult: strongest rival L -1
            rivals = [(f, f.stats['L']) for f in world.factions.values() if f.name != actor.name]
            if rivals:
                victim = max(rivals, key=lambda x: x[1])[0]
                victim.stats['L'] = max(1, victim.stats['L'] - 1)
        elif degree == 'Success':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            if actor.revelation_tokens >= 1:
                actor.revelation_tokens -= 1
                actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        elif degree == 'Partial':
            actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)  # rally recovers
        return

    if name == 'Charter of Liberties':
        actor.legacy_card_used = True
        actor.stats['W'] = max(0, actor.stats['W'] - 1)
        # BOOSTED EFFECTS
        if overwhelming:
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            world.clocks['PI'] = max(0, world.clocks['PI'] - 2)
            actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
        elif degree == 'Success':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            world.clocks['PI'] = max(0, world.clocks['PI'] - 1)
            # NEW: bonus L per Token on rival (Token-leverage synergy)
            token_count = sum(1 for v in actor.tokens_held.values() if v > 0)
            if token_count >= 2:
                actor.stats['L'] = min(7, actor.stats['L'] + 1)  # extra L
        elif degree == 'Partial':
            actor.stats['L'] = min(7, actor.stats['L'] + 1)  # NEW: even Partial gives L+1
        return

    apply_outcome_v6(action, degree, world)


def v10_score(action, world):
    name = action['name']
    actor = action['actor']
    if name == 'Crown Initiative':
        return 4 + max(0, 6 - actor.stats['L']) + (3 if actor.stats['L'] <= 3 else 0)
    if name == "Vaynard's Settlement":
        return 12
    if name == "Vaynard's Hall":
        return 9 + max(0, 6 - actor.stats['L'])
    if name == 'Charter of Liberties':
        return 8 + max(0, 6 - actor.stats['L'])
    return score_action_v5(action, world)


def v10_list_candidates(faction, world):
    cands = list_candidate_actions_v5(faction, world)
    if faction.name == 'Crown':
        a = dict(name='Crown Initiative', actor=faction, target=None)
        if v10_prereqs(a, world): cands.append(a)
    elif faction.name == 'Varfell':
        for tid, t in world.territories.items():
            if t.owner == 'Varfell' and t.accord < 2:
                a = dict(name="Vaynard's Settlement", actor=faction, target=tid)
                if v10_prereqs(a, world): cands.append(a)
        a2 = dict(name="Vaynard's Hall", actor=faction, target=None)
        if v10_prereqs(a2, world): cands.append(a2)
    elif faction.name == 'Hafenmark':
        a = dict(name='Charter of Liberties', actor=faction, target=None)
        if v10_prereqs(a, world): cands.append(a)
    return cands


def v10_select_actions(faction, world, n_actions=3):
    selected = []; used = set()
    for _ in range(n_actions):
        cands = v10_list_candidates(faction, world)
        cands = [a for a in cands if (a['name'], a.get('target')) not in used]
        if not cands: break
        scored = [(v10_score(a, world), a) for a in cands]
        scored.sort(key=lambda x: -x[0])
        top = scored[:4]
        weights = [4, 3, 2, 1][:len(top)]
        chosen = random.choices([a for _, a in top], weights=weights, k=1)[0]
        selected.append(chosen)
        used.add((chosen['name'], chosen.get('target')))
    return selected


def universal_victory_v10(world, turmoil_cap, threshold):
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
                elif rival.submitted: territories_controlled.add(tid)
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


def end_of_season_v10(world, turmoil_cap, threshold):
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
                    if t.owner in world.factions: world.factions[t.owner].territories.discard(tid)
                    t.owner = None; t.garrison = False; t.inquisitor_holder = None
                    for ff in world.factions.values(): ff.inquisitors.discard(tid)
            else:
                if t.owner in world.factions: world.factions[t.owner].territories.discard(tid)
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
    winner = universal_victory_v10(world, turmoil_cap, threshold)
    if winner: world.winner = winner


def run_season_v10(world, threshold):
    if world.winner: return
    for f in world.factions.values():
        f.reset_seasonal()
        # Reset new per-season slots
        f.hall_card_used = False
    acts = []
    for f in world.factions.values():
        acts.extend(v10_select_actions(f, world, n_actions=3))
    for action in acts:
        if not v10_prereqs(action, world): continue
        pool, ob = v10_pool_ob(action, world)
        net = roll_pool(pool) - ob
        degree = resolve_degree(net)
        v10_apply(action, degree, world)
    end_of_season_v10(world, world.params['TURMOIL_CAP'], threshold)
    world.season += 1
    if world.season % 4 == 0:
        for f in world.factions.values():
            f.pa_session_arc_used = False
            f.influence_surge_arc_used = False
            f.ecclesiastical_appointment_arc_used = False
        world.arc += 1


def run_campaign_v10(params=None, seed=None, threshold=11):
    if seed is not None: random.seed(seed)
    p = dict(PARAMS); p.update(params or {})
    world = init_world(tweaks=set())
    world.params = p
    almud_history = []
    for _ in range(p['CAMPAIGN_SEASONS']):
        if world.winner: break
        run_season_v10(world, threshold)
        crown = world.factions['Crown']
        almud_history.append(dict(Sta=crown.stats['Sta'], L=crown.stats['L']))
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


def run_mc_v10(n, params=None, threshold=11):
    wins = Counter(); states = Counter()
    L = defaultdict(list); terr = defaultdict(list)
    direct = 0; turmoil = []
    for i in range(n):
        r = run_campaign_v10(params=params, seed=i, threshold=threshold)
        wins[r['winner']] += 1
        states[r['almud_state']] += 1
        for fname, f in r['world'].factions.items():
            L[fname].append(f.stats['L'])
            terr[fname].append(len(f.territories))
        if r['world'].winner: direct += 1
        turmoil.append(r['world'].clocks['Turmoil'])
    total = sum(wins.values())
    return dict(
        win_share={k: round(wins.get(k, 0)/total*100, 1) for k in ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        L_mean={k: round(sum(v)/len(v), 2) for k, v in L.items()},
        terr_mean={k: round(sum(v)/len(v), 2) for k, v in terr.items()},
        direct_rate=round(direct/n*100, 1),
        turmoil_mean=round(sum(turmoil)/len(turmoil), 2),
        almud_strong=round(states.get('strong', 0)/n*100, 1),
        almud_deposed=round(sum(v for k, v in states.items() if k.startswith('deposed'))/n*100, 1),
    )


if __name__ == '__main__':
    N = 500
    print("=" * 80)
    print("v10 — FINE-TUNED INTEGRATED BALANCE")
    print("EA softer (every-other-arc) | Charter boosted | Vaynard's Hall added")
    print("Crown Init cost↑ (W-3) | Vaynard's Settlement retained")
    print("=" * 80)

    configs = [
        ('v9 reference (consent=0.75, thresh=11)', dict(CONSENT_RATE=0.75, TURMOIL_CAP=12), 11),
        ('v10 consent=0.5', dict(CONSENT_RATE=0.5, TURMOIL_CAP=12), 11),
        ('v10 consent=0.6', dict(CONSENT_RATE=0.6, TURMOIL_CAP=12), 11),
        ('v10 consent=0.75', dict(CONSENT_RATE=0.75, TURMOIL_CAP=12), 11),
        ('v10 consent=0.6 + 24s', dict(CONSENT_RATE=0.6, TURMOIL_CAP=12, CAMPAIGN_SEASONS=24), 11),
        ('v10 consent=0.6 + 50s', dict(CONSENT_RATE=0.6, TURMOIL_CAP=12, CAMPAIGN_SEASONS=50), 11),
        ('v10 consent=0.5 + thresh=13', dict(CONSENT_RATE=0.5, TURMOIL_CAP=12), 13),
    ]
    all_results = {}
    for label, params, threshold in configs:
        r = run_mc_v10(N, params=params, threshold=threshold)
        all_results[label] = r
        ws = r['win_share']
        spread = max(ws.values()) - min(ws.values())
        status = '✓ CLOSED' if spread <= 15 else ('~ partial' if spread <= 25 else '✗ open')
        in_band = all(15 <= v <= 35 for v in ws.values())
        band_status = '★ IN BAND' if in_band else ''
        print(f"\n{label}")
        print(f"  Cr={ws['Crown']:5.1f}% Ch={ws['Church']:5.1f}% "
              f"Ha={ws['Hafenmark']:5.1f}% Va={ws['Varfell']:5.1f}%   "
              f"spread {spread:.1f}pp {status} {band_status}")
        print(f"  L: Cr={r['L_mean']['Crown']:.2f} Ch={r['L_mean']['Church']:.2f} "
              f"Ha={r['L_mean']['Hafenmark']:.2f} Va={r['L_mean']['Varfell']:.2f}")
        print(f"  Direct: {r['direct_rate']:.1f}% | Almud strong: {r['almud_strong']:.1f}% | "
              f"deposed: {r['almud_deposed']:.1f}% | Turmoil: {r['turmoil_mean']}")

    print("\n" + "=" * 80)
    print("BALANCE CLOSURE SUMMARY")
    print("=" * 80)
    for label, r in all_results.items():
        ws = r['win_share']
        spread = max(ws.values()) - min(ws.values())
        in_band = all(15 <= v <= 35 for v in ws.values())
        status = '★ BALANCED' if in_band else ('✓ ≤15pp' if spread <= 15 else
                                                ('~ ≤25pp' if spread <= 25 else '✗ open'))
        print(f"  {label[:40]:40s}: spread {spread:5.1f}pp  direct {r['direct_rate']:5.1f}%  {status}")
    open('/home/claude/mc_v10_integrated.json', 'w').write(json.dumps(all_results, indent=2))
