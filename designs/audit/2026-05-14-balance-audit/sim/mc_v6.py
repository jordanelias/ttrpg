"""
Simulator v6 — Sensitivity analysis on the highest-leverage open canonical questions.

Inherits v5's canonical rules. Adds tunable parameters:
- CONSENT_RATE (Q-1 GAP-05): probability target accepts Crown Treaty after Success roll
- TURMOIL_CAP (Q-3): max Turmoil for Peninsular Sovereignty victory condition
- APPEASE_RATE: probability target Appeases when Mandate ≥ 4
- CAMPAIGN_SEASONS (Q-4): how many seasons before campaign times out

Per Jordan's directive: bottom-up granular emergent — perturb each rule
independently, observe what emerges.
"""
import sys, json, random
sys.path.insert(0, '/home/claude')
from collections import defaultdict, Counter
from mc_v4 import (CANONICAL_TERRITORIES, ALL_PLAYABLE_15, Faction, Territory,
                   World, make_action, init_world, roll_pool, resolve_degree)
from mc_v5 import (reset_seasonal_v5, prereqs_met_v5, pool_and_ob_v5,
                   score_action_v5, list_candidate_actions_v5, select_actions_v5)

# Apply v5 monkey-patches
Faction.reset_seasonal = reset_seasonal_v5

# Parameters (default = v5 canonical interpretation)
PARAMS = dict(
    CONSENT_RATE=0.5,         # Q-1: 50% baseline assumption
    APPEASE_RATE=0.7,         # Defensive Appease likelihood
    TURMOIL_CAP=6,            # Q-3: canonical §6.1
    CAMPAIGN_SEASONS=36,      # Q-4
    VARFELL_HAS_ACQUISITION=False,  # SB-1: post-CR-STRIKE, Varfell has no canonical acquisition
)


def universal_victory_check_param(world, turmoil_cap):
    """Peninsular Sovereignty check with tunable Turmoil threshold."""
    for fname, f in world.factions.items():
        territories_controlled = set()
        for tid in ALL_PLAYABLE_15:
            t = world.territories.get(tid)
            if t is None: continue
            if t.owner == fname:
                territories_controlled.add(tid)
            elif t.owner in world.factions:
                rival = world.factions[t.owner]
                treaty_type = f.treaties.get(rival.name, '')
                if treaty_type in ('CrownTreaty', 'Peace', 'Alliance', 'Capitulation', 'Tributary'):
                    territories_controlled.add(tid)
                elif rival.submitted:
                    territories_controlled.add(tid)
                elif rival.stats['L'] <= 1 and f.stats['L'] >= 5:
                    territories_controlled.add(tid)
        if len(territories_controlled) < len(ALL_PLAYABLE_15):
            f.sovereignty_history = 0; continue
        directly = world.territories_owned_by(fname)
        accord_ok = all(world.territories[tid].accord >= 2 for tid in directly)
        if not accord_ok:
            f.sovereignty_history = 0; continue
        if world.turmoil() > turmoil_cap:
            f.sovereignty_history = 0; continue
        f.sovereignty_history += 1
        if f.sovereignty_history >= 2: return fname
    return None


def apply_outcome_v6(action, degree, world):
    """v6 apply with parameterized consent + appease + acquisition gating."""
    name = action['name']; actor = action['actor']; target = action.get('target')
    success = degree in ('Success', 'Overwhelming')
    overwhelming = degree == 'Overwhelming'

    if name == 'Royal Decree':
        actor.consec_decree += 1
        if success: actor.stats['Sta'] = min(5, actor.stats['Sta'] + 1)
    elif name == 'Royal Charter':
        if success: actor.charters.add(target)
    elif name == 'Crown Treaty':
        actor.senator_card_used = True
        if success and target in world.factions:
            tf = world.factions[target]
            # Appease check
            if tf.stats['L'] >= 4 and random.random() < world.params['APPEASE_RATE']:
                tf.stats['L'] -= 1
                return
            # Consent check (parameterized Q-1)
            if random.random() < world.params['CONSENT_RATE']:
                actor.treaties[target] = 'CrownTreaty'
                tf.treaties[actor.name] = 'CrownTreaty'
                actor.stats['L'] = min(7, actor.stats['L'] + 1)
    elif name == 'Outreach to Schoenland':
        if success: world.clocks['IP'] = max(0, world.clocks['IP'] - 2)
    elif name == 'Cardinal Focus':
        actor.cardinal_focus = random.choice(['Justice', 'Prudence', 'Temperance', 'Fortitude'])
        actor.cardinal_focus_used_this_season = True
    elif name == 'Piety Spread':
        if overwhelming: world.territories[target].ap += 3
        elif degree == 'Success': world.territories[target].ap += 2
        elif degree == 'Partial': world.territories[target].ap += 1
    elif name == 'Active Inquisition':
        if success:
            t = world.territories[target]
            t.inquisitor_holder = 'Church'; actor.inquisitors.add(target); t.ap = 0
            t.last_hostile_season = world.season
            t.order = max(0, t.order - 1)
        elif degree == 'Partial':
            world.territories[target].ap += 1
    elif name == 'Church Seizure':
        t = world.territories[target]
        controller = world.factions.get(t.owner)
        if controller and controller.stats['L'] >= 4 and random.random() < world.params['APPEASE_RATE']:
            controller.stats['L'] -= 1; return
        if overwhelming:
            new_accord = min(3, (t.pt // 2) + 2)
            old = t.owner
            if old in world.factions: world.factions[old].territories.discard(target)
            t.owner = 'Church'; actor.territories.add(target); t.accord = new_accord
        elif degree == 'Success':
            new_accord = max((t.pt // 2) + 1, 2)
            old = t.owner
            if old in world.factions: world.factions[old].territories.discard(target)
            t.owner = 'Church'; actor.territories.add(target); t.accord = new_accord
        elif degree == 'Partial':
            t.accord = 1
    elif name == 'Excommunication':
        if success: world.factions[target].stats['L'] = max(1, world.factions[target].stats['L'] - 1)
        else: actor.stats['Sta'] = max(0, actor.stats['Sta'] - 1)
    elif name == 'Ecclesiastical Appointment':
        if success: actor.stats['L'] = min(7, actor.stats['L'] + 1)
    elif name == 'Diplomat Card':
        actor.diplomat_card_used = True
        if success:
            actor.tokens_held[target] += 1
            world.factions[target].tokens_received[actor.name] += 1
            world.clocks['PI'] += 1
    elif name == 'Parliamentary Session':
        actor.pa_session_arc_used = True
        support = 1
        for f in world.factions.values():
            if f.name == actor.name: continue
            if actor.tokens_held.get(f.name, 0) > 0:
                if random.random() < 0.6: support += 1
            elif f.name == 'Church': pass
            else:
                if random.random() < 0.4: support += 1
        if support >= 3:
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
            world.clocks['PI'] += 2
    elif name == 'Dynastic Proclamation':
        actor.diplomat_card_used = True
        t = world.territories[target]
        target_faction = world.factions.get(t.owner)
        if target_faction is None: return
        if target_faction.stats['L'] >= 4 and random.random() < world.params['APPEASE_RATE']:
            target_faction.stats['L'] -= 1; return
        if overwhelming:
            target_faction.territories.discard(target)
            t.owner = 'Hafenmark'; actor.territories.add(target); t.accord = 2
            target_faction.stats['L'] = max(1, target_faction.stats['L'] - 1)
            actor.stats['L'] = min(7, actor.stats['L'] + 1)
        elif degree == 'Success':
            target_faction.territories.discard(target)
            t.owner = 'Hafenmark'; actor.territories.add(target); t.accord = 2
            target_faction.stats['L'] = max(1, target_faction.stats['L'] - 1)
        elif degree == 'Partial':
            t.accord = max(0, t.accord - 1)
    elif name == 'Counter-Narrative':
        t = world.territories[target]
        if overwhelming:
            t.ap = max(0, t.ap - 3)
            actor.revelation_tokens += 1
        elif degree == 'Success': t.ap = max(0, t.ap - 2)
        elif degree == 'Partial': t.ap = max(0, t.ap - 1)
    elif name == 'Spy':
        if target == 'Crown':
            v = world.factions['Crown']
            if v.royal_guard_available:
                v.royal_guard_available = False; return
        if success:
            world.factions[target].stats['Sta'] = max(0, world.factions[target].stats['Sta'] - 1)
            if actor.name == 'Varfell': actor.revelation_tokens += 1
    elif name == 'Trade':
        if success: actor.stats['W'] = min(8, actor.stats['W'] + 1)
    elif name == 'Govern':
        t = world.territories[target]
        t.last_govern_season = world.season
        if overwhelming:
            t.prosperity = min(5, t.prosperity + 1)
            actor.stats['W'] = min(8, actor.stats['W'] + 1)
            t.order = min(5, t.order + 2); t.accord = min(3, t.accord + 1)
        elif degree == 'Success':
            t.prosperity = min(5, t.prosperity + 1)
            actor.stats['W'] = min(8, actor.stats['W'] + 1)
            t.order = min(5, t.order + 1); t.accord = min(3, t.accord + 1)
    elif name == 'Muster':
        if success:
            t = world.territories[target]
            t.garrison = True; actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)
    elif name == 'Tribune Network':
        if success: actor.revelation_tokens += 1
    elif name == 'Military Conquest':
        if success:
            t = world.territories[target]
            old = t.owner
            if old in world.factions: world.factions[old].territories.discard(target)
            t.owner = actor.name; actor.territories.add(target); t.accord = 1
            world.clocks['MS'] = max(0, world.clocks['MS'] - 2)
            world.clocks['IP'] += 2


def end_of_season_v6(world, turmoil_cap):
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
                controller = world.factions[t.owner]
                if (roll_pool(controller.stats['Mil']) - 2) >= 1: t.accord = 1
                else:
                    if t.owner in world.factions:
                        world.factions[t.owner].territories.discard(tid)
                    t.owner = None; t.garrison = False; t.inquisitor_holder = None
                    for f in world.factions.values(): f.inquisitors.discard(tid)
            else:
                if t.owner in world.factions:
                    world.factions[t.owner].territories.discard(tid)
                t.owner = None; t.inquisitor_holder = None
                for f in world.factions.values(): f.inquisitors.discard(tid)
        if (t.garrison and world.season - t.last_hostile_season >= 2):
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
    winner = universal_victory_check_param(world, turmoil_cap)
    if winner: world.winner = winner


def run_season_v6(world):
    if world.winner: return
    for f in world.factions.values(): f.reset_seasonal()
    all_acts = []
    for f in world.factions.values():
        all_acts.extend(select_actions_v5(f, world, n_actions=3))
    for action in all_acts:
        if not prereqs_met_v5(action, world): continue
        pool, ob = pool_and_ob_v5(action, world)
        net = roll_pool(pool) - ob
        degree = resolve_degree(net)
        apply_outcome_v6(action, degree, world)
    end_of_season_v6(world, world.params['TURMOIL_CAP'])
    world.season += 1
    if world.season % 4 == 0:
        for f in world.factions.values():
            f.reset_arc(); f.reset_annual()
        world.arc += 1


def run_campaign_v6(params=None, tweaks=None, seed=None, instrument=False):
    if seed is not None: random.seed(seed)
    p = dict(PARAMS); p.update(params or {})
    world = init_world(tweaks=tweaks or set())
    world.params = p
    trace = [] if instrument else None
    for _ in range(p['CAMPAIGN_SEASONS']):
        run_season_v6(world)
        if instrument:
            trace.append(dict(
                season=world.season,
                turmoil=world.clocks['Turmoil'],
                CI=world.clocks['CI'],
                PI=world.clocks['PI'],
                territories={n: len(f.territories) for n, f in world.factions.items()},
                L={n: f.stats['L'] for n, f in world.factions.items()},
                Sta={n: f.stats['Sta'] for n, f in world.factions.items()},
                inquisitors=len(world.factions['Church'].inquisitors),
                treaties={n: dict(f.treaties) for n, f in world.factions.items()},
                rev_tok=world.factions['Varfell'].revelation_tokens,
            ))
        if world.winner: break
    # Fallback winner
    winner = world.winner
    if winner is None:
        scores = {}
        for fname, f in world.factions.items():
            hegemony = 0
            for tid in ALL_PLAYABLE_15:
                t = world.territories.get(tid)
                if t and t.owner == fname: hegemony += 1
                elif t and t.owner in world.factions:
                    if f.treaties.get(t.owner, '') in ('CrownTreaty', 'Peace', 'Alliance', 'Capitulation', 'Tributary'):
                        hegemony += 0.5
            scores[fname] = hegemony * 10 + f.stats['L'] + len(f.territories)
        winner = max(scores, key=scores.get)
    return dict(winner=winner, world=world, trace=trace)


def run_mc_v6(n, params=None, tweaks=None):
    wins = Counter(); terr = defaultdict(list); treaties = defaultdict(list)
    inq = []; turmoil = 0; direct = 0; lengths = []; rev_tok = []
    for i in range(n):
        r = run_campaign_v6(params=params, tweaks=tweaks, seed=i)
        wins[r['winner']] += 1
        for fname in r['world'].factions:
            terr[fname].append(len(r['world'].factions[fname].territories))
            treaties[fname].append(len(r['world'].factions[fname].treaties))
        inq.append(len(r['world'].factions['Church'].inquisitors))
        turmoil += r['world'].clocks['Turmoil']
        if r['world'].winner: direct += 1
        lengths.append(r['world'].season)
        rev_tok.append(r['world'].factions['Varfell'].revelation_tokens)
    total = sum(wins.values())
    return dict(
        win_share={k: round(wins.get(k, 0)/total * 100, 1) for k in
                   ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        terr_mean={k: round(sum(v)/len(v), 2) for k, v in terr.items()},
        treaty_mean={k: round(sum(v)/len(v), 2) for k, v in treaties.items()},
        inq_mean=round(sum(inq)/len(inq), 2),
        turmoil_mean=round(turmoil/n, 2),
        direct_rate=round(direct/n * 100, 1),
        avg_length=round(sum(lengths)/len(lengths), 1),
        rev_tok_mean=round(sum(rev_tok)/len(rev_tok), 2),
    )


if __name__ == '__main__':
    N = 300  # smaller per-config for sensitivity sweep
    print("=" * 80)
    print("v6 SENSITIVITY ANALYSIS — Q-1, Q-3, Q-4 perturbations")
    print(f"  Baseline: {N} campaigns/config, v5 canonical rules")
    print("=" * 80)

    # ---------- Q-1: Treaty consent rate sensitivity ----------
    print("\n>>> Q-1 SENSITIVITY: Crown Treaty consent rate")
    q1_results = {}
    for consent in [0.0, 0.25, 0.5, 0.75, 1.0]:
        r = run_mc_v6(N, params=dict(CONSENT_RATE=consent))
        q1_results[f'consent_{consent}'] = r
        ws = r['win_share']
        print(f"  consent={consent:.2f}  Cr={ws['Crown']:5.1f}% Ch={ws['Church']:5.1f}% "
              f"Ha={ws['Hafenmark']:5.1f}% Va={ws['Varfell']:5.1f}%  "
              f"direct={r['direct_rate']:.1f}%  "
              f"crown_treaties={r['treaty_mean']['Crown']:.2f}")

    # ---------- Q-3: Turmoil cap sensitivity ----------
    print("\n>>> Q-3 SENSITIVITY: Turmoil ≤ N victory cap")
    q3_results = {}
    for cap in [6, 10, 15, 20, 30, 100]:
        r = run_mc_v6(N, params=dict(TURMOIL_CAP=cap))
        q3_results[f'cap_{cap}'] = r
        ws = r['win_share']
        print(f"  cap≤{cap:3d}  Cr={ws['Crown']:5.1f}% Ch={ws['Church']:5.1f}% "
              f"Ha={ws['Hafenmark']:5.1f}% Va={ws['Varfell']:5.1f}%  "
              f"direct={r['direct_rate']:.1f}%  "
              f"turmoil_mean={r['turmoil_mean']:.1f}")

    # ---------- Q-4: Campaign length sensitivity ----------
    print("\n>>> Q-4 SENSITIVITY: Campaign length (seasons)")
    q4_results = {}
    for seasons in [24, 36, 50, 75, 100]:
        r = run_mc_v6(N, params=dict(CAMPAIGN_SEASONS=seasons))
        q4_results[f'seasons_{seasons}'] = r
        ws = r['win_share']
        print(f"  seasons={seasons:3d}  Cr={ws['Crown']:5.1f}% Ch={ws['Church']:5.1f}% "
              f"Ha={ws['Hafenmark']:5.1f}% Va={ws['Varfell']:5.1f}%  "
              f"direct={r['direct_rate']:.1f}%  "
              f"avg_actual_length={r['avg_length']}")

    # ---------- Combined: Q-1 + Q-3 best-case ----------
    print("\n>>> COMBINED: Q-1=1.0 + Q-3=12 (best-of-both editorial resolution)")
    r = run_mc_v6(N, params=dict(CONSENT_RATE=1.0, TURMOIL_CAP=12, CAMPAIGN_SEASONS=60))
    ws = r['win_share']
    print(f"  Cr={ws['Crown']:5.1f}% Ch={ws['Church']:5.1f}% "
          f"Ha={ws['Hafenmark']:5.1f}% Va={ws['Varfell']:5.1f}%  "
          f"direct={r['direct_rate']:.1f}%  treaties_Cr={r['treaty_mean']['Crown']:.2f}")

    # Save
    all_results = dict(q1=q1_results, q3=q3_results, q4=q4_results, combined=r)
    open('/home/claude/mc_v6_sensitivity.json', 'w').write(json.dumps(all_results, indent=2))
    print("\n[saved /home/claude/mc_v6_sensitivity.json]")
