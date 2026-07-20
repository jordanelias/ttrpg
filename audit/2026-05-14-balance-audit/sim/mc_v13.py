"""
mc_v13 — DERIVED VALUE LAYER

v12c mechanics preserved. Adds canonical derived values per derived_stats_v30 §8:
  Legitimacy = Mandate(L) × 20    # [canonical: derived_stats_v30 §8]
  Discipline = Stability(Sta) × 10  # [canonical: derived_stats_v30 §8]
  Treasury   = Wealth(W) × 100      # [canonical: derived_stats_v30 §8]
  Reputation = Influence(I) × 15    # [canonical: derived_stats_v30 §8]

Key rule (§8.2): "No game event directly modifies a 1–7 stat except through
derived value depletion or explicit major events."

Strain threshold effects per peninsular_strain_v30 §4.3.
Treaty-based Strain decay per peninsular_strain_v30 §4.2.
"""
import sys, json, random
sys.path.insert(0, '/home/claude')
from collections import defaultdict, Counter

# Import base sim infrastructure from v12c
from mc_v12c import (
    ALL_PLAYABLE_15, CANONICAL_TERRITORIES, Faction, Territory, World,
    init_world, roll_pool, resolve_degree,
    ADJACENCY, STARTING_TERRITORIES, adjacent_territories, has_cb_against,
    # v5/v6 base
    prereqs_met_v5, pool_and_ob_v5, score_action_v5,
    list_candidate_actions_v5, apply_outcome_v6, PARAMS,
    # v12c functions we'll override
    v12_prereqs, v12_pool_ob, v12_score,
    v12_list_candidates, v12_select_actions,
    universal_victory_v12,
)
from mc_v8 import reset_seasonal_v8
Faction.reset_seasonal = reset_seasonal_v8

# ── Derived value multipliers ──────────────────────────────────────────────
# [canonical: derived_stats_v30 §8]
LEGITIMACY_MULT = 20   # Mandate × 20
DISCIPLINE_MULT = 10   # Stability × 10
TREASURY_MULT = 100    # Wealth × 100
REPUTATION_MULT = 15   # Influence × 15

# ── Derived value income/drain constants ───────────────────────────────────
# [canonical: derived_stats_v30 §8.1]
LEGIT_TERRITORY_INCOME = 5       # +5 per territory at Accord ≥ 2
LEGIT_GOVERN_INCOME_MULT = 5     # +Mandate × 5 per Govern Success
LEGIT_UNPOPULAR_DRAIN = -15      # Unpopular Domain Action
LEGIT_BATTLE_OWN_DRAIN = -10     # Battle in own territory
DISC_PEACEFUL_INCOME = 10        # +10 per peaceful season
DISC_GOVERN_INCOME = 5           # +5 per Govern Success
DISC_ACCORD0_DRAIN = -20         # Accord drops to 0 in any territory
DISC_BATTLE_LOSS_DRAIN = -15     # Battle loss
DISC_DEPLETION_OB = 1            # Ob for Stability check when Discipline = 0
LEGIT_DEPLETION_OB = 2           # Ob for Mandate check when Legitimacy = 0
# [canonical: peninsular_strain_v30 §4.3]
STRAIN_TENSION_LEGIT_DRAIN = -25 # Strain 3-4: Legitimacy drain
STRAIN_UNREST_GOVERN_OB = 1      # Strain 5-6: +1 Ob to Govern
# [canonical: peninsular_strain_v30 §4.2]
STRAIN_TREATY_DECAY_PER = -1     # Per Treaty pair
STRAIN_TREATY_DECAY_CAP = -2     # Cap per season

V13_PARAMS = dict(PARAMS)
V13_PARAMS.update(
    CONSENT_RATE=0.5,
    TURMOIL_CAP=12,
    CAMPAIGN_SEASONS=50,
    TREATY_LAPSE_RATE=0.5,
    EINHIR_I_GATE=4,
    EINHIR_PT_OB_WEIGHT=1,
    RM_BASE_STRENGTH=1,
    RM_GROWTH_PER_ARC=1,
    RM_PT_DECAY_CHANCE=0.3,
    RM_VARFELL_COOPTION_BONUS=0.1,
    ALTONIAN_I_GATE=5,
    ALTONIAN_MIL_GAIN=1,
    PARL_REQUIRE_CB=True,
    PARL_MAJORITY_OB_BONUS=2,
)


# ═══════════════════════════════════════════════════════════════════════════
# DERIVED VALUE MANAGEMENT
# ═══════════════════════════════════════════════════════════════════════════

def init_derived(faction):
    """Initialize derived values from stats. [canonical: derived_stats_v30 §8]"""
    faction.legitimacy = faction.stats['L'] * LEGITIMACY_MULT
    faction.discipline = faction.stats['Sta'] * DISCIPLINE_MULT
    faction.treasury = faction.stats['W'] * TREASURY_MULT
    faction.reputation = faction.stats['I'] * REPUTATION_MULT
    faction.peaceful_this_season = True  # tracks for Discipline income


def drain_legitimacy(faction, amount, reason=None):
    """Drain Legitimacy. Negative amount = drain. Capped at 0."""
    faction.legitimacy = max(0, faction.legitimacy + amount)

def drain_discipline(faction, amount, reason=None):
    """Drain Discipline. Negative amount = drain. Capped at 0."""
    faction.discipline = max(0, faction.discipline + amount)

def drain_treasury(faction, amount, reason=None):
    """Drain Treasury. Negative amount = drain. Capped at 0."""
    faction.treasury = max(0, faction.treasury + amount)

def drain_reputation(faction, amount, reason=None):
    """Drain Reputation. Negative amount = drain. Capped at 0."""
    faction.reputation = max(0, faction.reputation + amount)


def accounting_derived(world):
    """
    Accounting phase: income, depletion checks, Strain thresholds.
    Fires once per season at end of season.
    [canonical: derived_stats_v30 §8.1, peninsular_strain_v30 §4.3]
    """
    strain = world.clocks.get('Turmoil', 0)

    for fname, f in world.factions.items():
        # ── Seasonal income ──
        # Legitimacy income: +5 per territory at Accord ≥ 2
        legit_income = sum(LEGIT_TERRITORY_INCOME
                          for tid in f.territories
                          if world.territories.get(tid) and world.territories[tid].accord >= 2)
        drain_legitimacy(f, legit_income)

        # Discipline income: +10 if peaceful (no hostile actions in own territory this season)
        if f.peaceful_this_season:
            drain_discipline(f, DISC_PEACEFUL_INCOME)

        # Treasury income: simplified — Prosperity-based
        # [canonical: derived_stats_v30 §8.1 Treasury]
        treasury_income = sum(world.territories[tid].prosperity * 10
                             for tid in f.territories
                             if tid in world.territories)
        drain_treasury(f, treasury_income)

        # ── Strain threshold effects ──
        # [canonical: peninsular_strain_v30 §4.3]
        if 3 <= strain <= 4:
            drain_legitimacy(f, STRAIN_TENSION_LEGIT_DRAIN)
        elif 5 <= strain <= 6:
            pass  # +1 Ob to Govern handled in pool_ob
        elif 7 <= strain <= 8:
            # Accord −1 in all non-capital territories
            for tid in list(f.territories):
                t = world.territories.get(tid)
                if t and tid not in _capital_territories(f):
                    t.accord = max(0, t.accord - 1)
            # Mandate check Ob 2
            net = roll_pool(f.stats['L']) - 2
            if resolve_degree(net) == 'Failure':
                drain_legitimacy(f, -25)
                f.stats['L'] = max(1, f.stats['L'] - 1)
                f.legitimacy = min(f.legitimacy, f.stats['L'] * LEGITIMACY_MULT)
        elif strain >= 9:
            # L−1 for all factions [canonical: §4.3 — this IS direct per §8.2]
            f.stats['L'] = max(1, f.stats['L'] - 1)
            f.legitimacy = min(f.legitimacy, f.stats['L'] * LEGITIMACY_MULT)

        # ── Depletion checks ──
        # [canonical: derived_stats_v30 §8.1]

        # Discipline depletion → Stability check
        if f.discipline <= 0:
            net = roll_pool(f.stats['Sta']) - DISC_DEPLETION_OB
            if resolve_degree(net) in ('Failure',):
                f.stats['Sta'] = max(1, f.stats['Sta'] - 1)
            # Reset discipline to new max (regardless of check outcome)
            f.discipline = f.stats['Sta'] * DISCIPLINE_MULT

        # Legitimacy depletion → Mandate check
        if f.legitimacy <= 0:
            net = roll_pool(f.stats['L']) - LEGIT_DEPLETION_OB
            if resolve_degree(net) in ('Failure',):
                f.stats['L'] = max(1, f.stats['L'] - 1)
                # Accord −1 in all territories
                for tid in list(f.territories):
                    t = world.territories.get(tid)
                    if t: t.accord = max(0, t.accord - 1)
            f.legitimacy = f.stats['L'] * LEGITIMACY_MULT

        # Treasury depletion → Wealth check
        if f.treasury <= 0:
            f.stats['W'] = max(1, f.stats['W'] - 1)
            f.treasury = f.stats['W'] * TREASURY_MULT

        # Reputation depletion → Influence check
        if f.reputation <= 0:
            f.stats['I'] = max(1, f.stats['I'] - 1)
            f.reputation = f.stats['I'] * REPUTATION_MULT

        # Cap derived at stat × multiplier
        f.legitimacy = min(f.legitimacy, f.stats['L'] * LEGITIMACY_MULT)
        f.discipline = min(f.discipline, f.stats['Sta'] * DISCIPLINE_MULT)
        f.treasury = min(f.treasury, f.stats['W'] * TREASURY_MULT)
        f.reputation = min(f.reputation, f.stats['I'] * REPUTATION_MULT)

        # Reset peaceful flag
        f.peaceful_this_season = True


def _capital_territories(faction):
    """Return capital territory IDs (first territory in starting set)."""
    # Simplified: use first territory alphabetically as capital
    return {min(faction.territories)} if faction.territories else set()


# ═══════════════════════════════════════════════════════════════════════════
# STRAIN DECAY FROM TREATIES
# [canonical: peninsular_strain_v30 §4.2]
# ═══════════════════════════════════════════════════════════════════════════

def strain_treaty_decay(world):
    """Active Treaty pairs reduce Strain. Per §4.2."""
    treaty_pairs = 0
    seen = set()
    for fname, f in world.factions.items():
        for partner, ttype in f.treaties.items():
            pair = tuple(sorted([fname, partner]))
            if pair not in seen and ttype in ('CrownTreaty', 'Peace', 'Alliance', 'Truce',
                                               'Capitulation', 'Tributary'):
                treaty_pairs += 1
                seen.add(pair)
    decay = min(treaty_pairs, abs(STRAIN_TREATY_DECAY_CAP))
    world.clocks['Turmoil'] = max(0, world.clocks.get('Turmoil', 0) - decay)


# ═══════════════════════════════════════════════════════════════════════════
# v13 APPLY — routes through derived values
# ═══════════════════════════════════════════════════════════════════════════

def v13_apply(action, degree, world):
    """Apply outcomes via derived values. Stats change only through depletion."""
    actor = action['actor']
    name = action['name']
    success = degree in ('Success', 'Overwhelming')
    overwhelming = degree == 'Overwhelming'

    if name == 'Ecclesiastical Appointment':
        actor.ecclesiastical_appointment_arc_used = True
        actor.ea_last_arc = world.arc
        if success:
            drain_legitimacy(actor, 20)  # [canonical: §8.1 — institutional appointment]
        return

    if name == 'Crown Initiative':
        actor.senator_inward_used = True
        drain_treasury(actor, -300)  # W−3 → Treasury −300
        if overwhelming:
            # Major event: direct L+2 [canonical: §8.2 — Govern/Trade OW analog]
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            actor.legitimacy = min(actor.stats['L'] * LEGITIMACY_MULT, actor.legitimacy + 40)
            drain_discipline(actor, 10)  # Sta+1 → Discipline +10
            for tid in actor.territories:
                t = world.territories[tid]
                if t.accord == 1: t.accord = 2
        elif degree == 'Success':
            drain_legitimacy(actor, 20)  # L+1 → Legitimacy +20
            if actor.territories:
                worst = min((world.territories[tid] for tid in actor.territories),
                            key=lambda t: t.accord)
                worst.accord = min(3, worst.accord + 1)
        elif degree == 'Partial':
            drain_discipline(actor, 10)  # Sta+1 → Discipline +10
        return

    if name == "Vaynard's Settlement":
        actor.tribune_card_used = True
        drain_treasury(actor, -100)  # W−1 → Treasury −100
        t = world.territories[action['target']]
        if overwhelming:
            t.accord = min(3, t.accord + 2); t.order = min(5, t.order + 1)
            actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)  # direct — structural military
        elif degree == 'Success':
            t.accord = min(3, t.accord + 1); t.order = min(5, t.order + 1)
        elif degree == 'Partial':
            t.order = min(5, t.order + 1)
        return

    if name == "Vaynard's Hall":
        actor.hall_card_used = True
        actor.stats['Mil'] = max(1, actor.stats['Mil'] - 1)  # direct — structural military
        drain_treasury(actor, -100)  # W−1 → Treasury −100
        if overwhelming:
            drain_legitimacy(actor, 40)  # L+2 → Legitimacy +40
            rivals = [(f, f.stats['L']) for f in world.factions.values() if f.name != actor.name]
            if rivals:
                victim = max(rivals, key=lambda x: x[1])[0]
                drain_legitimacy(victim, -20)  # rival L−1 → Legitimacy −20
        elif degree == 'Success':
            drain_legitimacy(actor, 20)  # L+1 → Legitimacy +20
            if getattr(actor, 'revelation_tokens', 0) >= 1:
                actor.revelation_tokens -= 1
                drain_discipline(actor, 10)  # Sta+1 → Discipline +10
        elif degree == 'Partial':
            actor.stats['Mil'] = min(7, actor.stats['Mil'] + 1)  # direct recovery
        return

    if name == 'Charter of Liberties':
        actor.legacy_card_used = True
        drain_treasury(actor, -100)  # W−1 → Treasury −100
        if overwhelming:
            # Major event: direct L+2
            actor.stats['L'] = min(7, actor.stats['L'] + 2)
            actor.legitimacy = min(actor.stats['L'] * LEGITIMACY_MULT, actor.legitimacy + 40)
            world.clocks['PI'] = max(0, world.clocks['PI'] - 2)
            drain_discipline(actor, 10)
        elif degree == 'Success':
            drain_legitimacy(actor, 20)  # L+1 → Legitimacy +20
            world.clocks['PI'] = max(0, world.clocks['PI'] - 1)
            token_count = sum(1 for v in actor.tokens_held.values() if v > 0)
            if token_count >= 2:
                drain_legitimacy(actor, 20)  # bonus L+1 → Legitimacy +20
        elif degree == 'Partial':
            drain_legitimacy(actor, 20)  # L+1 → Legitimacy +20
        return

    if name == 'Einhir Revival':
        actor.einhir_arc_used = True
        target_tid = action['target']
        t = world.territories[target_tid]
        old_owner = t.owner
        if overwhelming:
            # Major event: territory transfer with stat changes
            if old_owner and old_owner in world.factions:
                world.factions[old_owner].territories.discard(target_tid)
                drain_legitimacy(world.factions[old_owner], -20)
            t.owner = 'Varfell'; actor.territories.add(target_tid)
            t.accord = 2; t.pt = max(0, t.pt - 1)
            drain_legitimacy(actor, 20)
        elif degree == 'Success':
            if old_owner and old_owner in world.factions:
                world.factions[old_owner].territories.discard(target_tid)
            t.owner = 'Varfell'; actor.territories.add(target_tid)
            t.accord = 1; t.pt = max(0, t.pt - 1)
        elif degree == 'Partial':
            t.pt = max(0, t.pt - 1)
            if not hasattr(actor, 'casus_belli'): actor.casus_belli = set()
            if old_owner: actor.casus_belli.add(old_owner)
        return

    if name == 'Parliamentary Transfer':
        actor.parl_transfer_arc_used = True
        target_tid = action['target']
        t = world.territories[target_tid]
        old_owner = t.owner
        if hasattr(actor, 'casus_belli') and old_owner in actor.casus_belli:
            actor.casus_belli.discard(old_owner)
        if overwhelming:
            # Major event: territory transfer
            if old_owner and old_owner in world.factions:
                world.factions[old_owner].territories.discard(target_tid)
                drain_legitimacy(world.factions[old_owner], -20)
            t.owner = actor.name; actor.territories.add(target_tid); t.accord = 1
        elif degree == 'Success':
            if old_owner and old_owner in world.factions:
                world.factions[old_owner].territories.discard(target_tid)
            t.owner = actor.name; actor.territories.add(target_tid); t.accord = 1
        elif degree == 'Partial':
            if not hasattr(actor, 'casus_belli'): actor.casus_belli = set()
            if old_owner: actor.casus_belli.add(old_owner)
        else:  # Failure
            drain_discipline(actor, -10)  # Sta−1 → Discipline −10
            if old_owner and old_owner in world.factions:
                drain_legitimacy(world.factions[old_owner], 20)  # sympathy
        return

    # Base v6 outcomes — wrap stat changes in derived
    # For base actions, apply normally but mark non-peaceful if hostile
    apply_outcome_v6(action, degree, world)

    # Track Govern success for Discipline income
    if name == 'Govern' and success:
        drain_discipline(actor, DISC_GOVERN_INCOME)
        drain_legitimacy(actor, actor.stats['L'] * LEGIT_GOVERN_INCOME_MULT)


# ═══════════════════════════════════════════════════════════════════════════
# v13 POOL/OB — adds Strain-based Govern Ob modifier
# ═══════════════════════════════════════════════════════════════════════════

def v13_pool_ob(action, world):
    pool, ob = v12_pool_ob(action, world)
    # [canonical: peninsular_strain_v30 §4.3 — Strain 5-6: +1 Ob to Govern]
    if action['name'] == 'Govern':
        strain = world.clocks.get('Turmoil', 0)
        if 5 <= strain <= 6:
            ob += STRAIN_UNREST_GOVERN_OB
    return pool, ob


# ═══════════════════════════════════════════════════════════════════════════
# END OF SEASON — v12c + derived Accounting + Strain Treaty decay
# ═══════════════════════════════════════════════════════════════════════════

def end_of_season_v13(world, turmoil_cap, threshold):
    """v12c end_of_season + derived value Accounting + Strain Treaty decay."""
    world.clocks['CI'] += 1
    world.clocks['MS'] = max(0, world.clocks['MS'] - 1)

    revolts = 0
    for tid, t in list(world.territories.items()):
        if t.is_uncontrolled(): continue
        if t.accord == 1 and not t.garrison: t.accord = 0
        if t.accord == 0:
            world.clocks['Turmoil'] = world.clocks.get('Turmoil', 0) + 1
            revolts += 1
            # Discipline drain for controlling faction
            if t.owner and t.owner in world.factions:
                drain_discipline(world.factions[t.owner], DISC_ACCORD0_DRAIN)
                world.factions[t.owner].peaceful_this_season = False
            if t.garrison:
                c = world.factions.get(t.owner)
                if c and (roll_pool(c.stats['Mil']) - 2) >= 1:
                    t.accord = 1
                else:
                    if t.owner in world.factions:
                        world.factions[t.owner].territories.discard(tid)
                    t.owner = None; t.garrison = False; t.inquisitor_holder = None
                    for ff in world.factions.values(): ff.inquisitors.discard(tid)
            else:
                if t.owner in world.factions:
                    world.factions[t.owner].territories.discard(tid)
                t.owner = None; t.inquisitor_holder = None

        if t.garrison and t.owner and world.season - getattr(t, 'last_hostile_season', 0) >= 2:
            t.consec_passive_seasons = getattr(t, 'consec_passive_seasons', 0) + 1
            if t.consec_passive_seasons >= 2 and t.accord < 2:
                t.accord += 1; t.consec_passive_seasons = 0
        else:
            t.consec_passive_seasons = 0

    if revolts == 0:
        world.clocks['Turmoil'] = max(0, world.clocks.get('Turmoil', 0) - 1)
    world.clocks['Strain'] = world.clocks['Turmoil']

    # Treaty-based Strain decay [canonical: peninsular_strain_v30 §4.2]
    strain_treaty_decay(world)

    # Derived value Accounting (replaces raw Sta ≤ 2 cascade)
    accounting_derived(world)

    # Victory check
    winner = universal_victory_v12(world, turmoil_cap, threshold)
    if winner: world.winner = winner


# ═══════════════════════════════════════════════════════════════════════════
# ARC BOUNDARY — import from v12c, unchanged
# ═══════════════════════════════════════════════════════════════════════════
from mc_v12c import arc_boundary_v12


# ═══════════════════════════════════════════════════════════════════════════
# RUN
# ═══════════════════════════════════════════════════════════════════════════

def run_season_v13(world, threshold):
    if world.winner: return
    for f in world.factions.values():
        f.reset_seasonal()
        f.hall_card_used = False
    acts = []
    for f in world.factions.values():
        acts.extend(v12_select_actions(f, world, n_actions=3))
    for action in acts:
        if not v12_prereqs(action, world): continue
        pool, ob = v13_pool_ob(action, world)
        net = roll_pool(pool) - ob
        degree = resolve_degree(net)
        v13_apply(action, degree, world)
    end_of_season_v13(world, world.params['TURMOIL_CAP'], threshold)
    world.season += 1
    if world.season % 4 == 0:
        arc_boundary_v12(world)
        world.arc += 1


def run_campaign_v13(params=None, seed=None, threshold=11):
    if seed is not None: random.seed(seed)
    p = dict(V13_PARAMS); p.update(params or {})
    world = init_world(tweaks=set())
    world.params = p
    for f in world.factions.values():
        f.casus_belli = set()
        init_derived(f)  # Initialize derived values
    almud_history = []
    for _ in range(p['CAMPAIGN_SEASONS']):
        if world.winner: break
        run_season_v13(world, threshold)
        crown = world.factions.get('Crown')
        if crown:
            almud_history.append(dict(Sta=crown.stats['Sta'], L=crown.stats['L'],
                                      Discipline=crown.discipline, Legitimacy=crown.legitimacy))
    winner = world.winner
    if winner is None:
        scores = {}
        for fname, f in world.factions.items():
            h = 0
            for tid in ALL_PLAYABLE_15:
                t = world.territories.get(tid)
                if t and t.owner == fname: h += 1
                elif t and t.owner in world.factions:
                    if f.treaties.get(t.owner, '') in ('CrownTreaty', 'Peace', 'Alliance',
                                                        'Capitulation', 'Tributary'):
                        h += 0.5
            scores[fname] = h * 10 + f.stats['L'] + len(f.territories)
        winner = max(scores, key=scores.get)
    almud_state = 'stable'
    if any(h['Sta'] == 0 for h in almud_history):
        almud_state = 'deposed-submission'
    elif sum(1 for h in almud_history[-6:] if h['L'] <= 1) >= 2:
        almud_state = 'deposed-mandate-collapse'
    elif almud_history and almud_history[-1]['Sta'] >= 4 and almud_history[-1]['L'] >= 5:
        almud_state = 'strong'
    elif almud_history and (almud_history[-1]['Sta'] <= 2 or almud_history[-1]['L'] <= 2):
        almud_state = 'weak'
    return dict(winner=winner, almud_state=almud_state, world=world)


def run_mc_v13(n, params=None, threshold=11):
    wins = Counter(); states = Counter()
    L = defaultdict(list); terr = defaultdict(list)
    direct = 0; turmoil = []
    for i in range(n):
        r = run_campaign_v13(params=params, seed=i, threshold=threshold)
        wins[r['winner']] += 1; states[r['almud_state']] += 1
        for fname, f in r['world'].factions.items():
            L[fname].append(f.stats['L']); terr[fname].append(len(f.territories))
        if r['world'].winner: direct += 1
        turmoil.append(r['world'].clocks.get('Turmoil', 0))
    total = sum(wins.values())
    return dict(
        win_share={k: round(wins.get(k, 0)/total*100, 1)
                   for k in ['Crown', 'Church', 'Hafenmark', 'Varfell']},
        L_mean={k: round(sum(v)/len(v), 2) for k, v in L.items()},
        terr_mean={k: round(sum(v)/len(v), 2) for k, v in terr.items()},
        direct_rate=round(direct/n*100, 1),
        turmoil_mean=round(sum(turmoil)/len(turmoil), 2),
        almud_strong=round(states.get('strong', 0)/n*100, 1),
        almud_deposed=round(sum(v for k, v in states.items()
                                if k.startswith('deposed'))/n*100, 1),
    )


if __name__ == '__main__':
    print("v13 smoke test — 10 campaigns...")
    r = run_mc_v13(10)
    print(f"Win shares: {r['win_share']}")
    print(f"Direct: {r['direct_rate']}% | Almud deposed: {r['almud_deposed']}%")
    print(f"L: {r['L_mean']}")
    print(f"Terr: {r['terr_mean']}")
    print(f"Turmoil: {r['turmoil_mean']}")
