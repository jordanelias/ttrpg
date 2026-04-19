"""
Valoria Campaign Simulation Engine v3
Rebuilt 2026-04-18 for canonical fidelity.
Single-file engine. All constants cited to canonical source.
"""
import random, math
from dataclasses import dataclass, field
from typing import Dict, List, Set

# ═══════════════════════════════════════════════════════════════
# DICE SYSTEM
# [canonical: params/core.md §Die Rule d10]
# ═══════════════════════════════════════════════════════════════

def roll_pool(pool: int, tn: int = 7) -> int:  # [canonical: params/core.md §TN Values — 7 standard]
    pool = max(1, pool)  # [canonical: params/core.md §Pool Minimum — floor 1D]
    total = 0
    for _ in range(pool):
        face = random.randint(1, 10)
        if face == 1:       total -= 1  # [canonical: params/core.md — face 1 = -1 success]
        elif face == 10:    total += 2  # [canonical: params/core.md — face 10 = +2 successes]
        elif face >= tn:    total += 1  # [canonical: params/core.md — face 7-9 = +1 at TN7]
    return total

def degree(net: int, ob: int) -> str:
    # [canonical: params/core.md §Degrees of Success]
    ob = max(1, ob)  # [canonical: params/core.md — Ob minimum 1]
    if net >= 2 * ob and net >= 3:  # [canonical: params/core.md — Overwhelming floor 3]
        return 'Overwhelming'
    if net >= ob:
        return 'Success'
    if net > 0:
        return 'Partial'
    return 'Failure'

def check(pool: int, ob: int, tn: int = 7):
    net = roll_pool(pool, tn)
    return net, degree(net, ob)

# ═══════════════════════════════════════════════════════════════
# TERRITORY DATA
# [canonical: designs/provincial/victory_v30.md §1 + params/bg/geography.md]
# PV = Provincial Value (political power; NOT used in victory)
# SW = Spiritual Weight (CI generation input)
# PR = Proximity Rating (RS effect graduation)
# ═══════════════════════════════════════════════════════════════

# [canonical: editorial_decisions_ci_pv_2026-04-18.md §5 — PV by settlement type]
# Cathedral City=5, National capital=5, Duchy capitals=4, Fortresses/strategic=3, others=1
# Remaining territories TBD — using 1 as placeholder
TERRITORIES = {
    #  id: (name,            PV, SW, PR, start_controller, start_accord, start_PT)
    'T1':  ('Valorsplatz',    5,  2,  5, 'Crown',      3, 3),  # [canonical: National capital PV=5]
    'T2':  ('Kronmark',       1,  2,  5, 'Crown',      2, 3),
    'T3':  ('Lowenskyst',     3,  2,  4, 'Crown',      2, 3),  # [canonical: Fortress/strategic PV=3]
    'T4':  ('Grauwald',       1,  1,  3, 'Varfell',    2, 2),  # [canonical: params/bg/core.md PT=2]
    'T5':  ('Feldmark',       1,  2,  4, 'Crown',      2, 3),
    'T6':  ('Stillhelm',      1,  1,  3, 'Crown',      2, 1),  # [canonical: params/bg/core.md PT=1]
    'T7':  ('Rendstad',       1,  2,  4, 'Hafenmark',  2, 3),
    'T8':  ('Gransol',        4,  3,  4, 'Hafenmark',  3, 3),  # [canonical: Duchy capital PV=4]
    'T9':  ('Himmelenger',    5,  5,  4, 'Church',     3, 5),  # [canonical: Cathedral City PV=5, PT=5]
    'T10': ('Spartfell',      1,  2,  3, 'Hafenmark',  2, 3),
    'T11': ('Halvardshelm',   1,  1,  2, 'Varfell',    2, 2),  # [canonical: PT=2]
    'T12': ('Sigurdshelm',    4,  1,  2, 'Varfell',    3, 2),  # [canonical: Duchy capital PV=4, PT=2]
    'T13': ('Oastad',         1,  1,  2, 'Varfell',    2, 1),  # [canonical: PT=1]
    'T14': ('Ehrenfeld',      3,  2,  3, 'Crown',      2, 3),  # [canonical: Fortress/strategic PV=3]
    'T15': ('Askeheim',       0,  0,  0, 'Uncontrolled', 0, 0), # [canonical: hard-fixed]
    'T17': ('Halvarshelm',    1,  2,  4, 'Hafenmark',  2, 3),
}

# ═══════════════════════════════════════════════════════════════
# FACTION STARTING STATS
# [canonical: params/bg/core.md §Faction Starting Stats v04 B5]
# Order: Mandate, Influence, Wealth, Military, Stability
# ═══════════════════════════════════════════════════════════════

FACTION_STATS = {
    'Crown':     {'mandate':5, 'influence':5, 'wealth':4, 'military':4, 'stability':4},
    'Church':    {'mandate':5, 'influence':6, 'wealth':5, 'military':4, 'stability':5},
    'Hafenmark': {'mandate':4, 'influence':4, 'wealth':5, 'military':3, 'stability':4},
    'Varfell':   {'mandate':4, 'influence':4, 'wealth':4, 'military':4, 'stability':4},
}

FACTION_TERRITORIES = {  # [canonical: params/bg/geography.md]
    'Crown':     ['T1','T2','T3','T5','T6','T14'],
    'Church':    ['T9'],
    'Hafenmark': ['T7','T8','T10','T17'],
    'Varfell':   ['T4','T11','T12','T13'],
}

# ═══════════════════════════════════════════════════════════════
# GAME STATE
# ═══════════════════════════════════════════════════════════════

@dataclass
class Territory:
    id: str
    name: str
    pv: int
    sw: int
    pr: int
    controller: str
    accord: int
    pt: int
    fort: int = 0
    garrison: bool = False
    # Church infrastructure per settlement_layer/campaign_architecture
    church_building: int = 0   # 0=none, 1=chapel, 2=church, 3=cathedral
    templar: bool = False
    inquisitor: bool = False
    church_governor: bool = False

    @property
    def church_infra_modifier(self) -> int:
        # [canonical: editorial_decisions §4 — Chapel -1, Church -2, Cathedral -3, Inquisitor -1, Templar -1]
        mod = 0
        mod -= self.church_building  # 0/1/2/3
        if self.templar: mod -= 1
        if self.inquisitor: mod -= 1
        return mod

@dataclass
class Faction:
    name: str
    mandate: int
    influence: int
    wealth: int
    military: int
    stability: int
    territories: List[str] = field(default_factory=list)
    active: bool = True
    submitted: bool = False
    seizure_used: bool = False  # [canonical: editorial_decisions §6 — one-time]
    # Card-hand economy [canonical: params/bg/core.md §Batch Card Hand]
    hand: List[str] = field(default_factory=list)      # available cards
    cooldown: List[str] = field(default_factory=list)   # cards on 1-season cooldown
    expertise: str = ''  # Domain Expertise card type (+1D)

    def clamp(self):
        # [canonical: params/bg/core.md §Stat Ceilings and Floors]
        self.mandate   = max(0, min(7, self.mandate))
        self.influence = max(1, min(7, self.influence))
        self.wealth    = max(0, min(7, self.wealth))
        self.military  = max(0, min(7, self.military))
        self.stability = max(0, min(7, self.stability))

@dataclass
class GameState:
    season: int = 0
    # [canonical: params/bg/core.md §Starting Values]
    ci: int = 28    # Church Influence (was TC) [canonical: editorial_decisions §1,2]
    rs: int = 72    # Rendering Stability
    ip: int = 20    # Invasion Pressure [canonical: params/bg/core.md — IP start 20]
    pi: int = 7     # Parliament Integrity
    strain: int = 0 # Peninsular Strain [canonical: params/bg/core.md]
    coup_counter: int = 0  # Löwenritter
    torben_loyalty: int = 7  # [canonical: params/bg/core.md — start 7]
    elske_loyalty: int = 4   # [canonical: params/bg/core.md — start 4]
    aer: int = 2    # Altonian Ecclesiastical Relationship
    wc: int = 0     # Warden Cooperation
    wr: int = 0     # Warden Recognition
    vtm: int = 0    # Vaynard Thread Mastery [canonical: params/bg/core.md]
    warden_emerged: bool = False  # Edeyja/Wardens active
    factions: Dict[str, Faction] = field(default_factory=dict)
    territories: Dict[str, Territory] = field(default_factory=dict)
    log: List[str] = field(default_factory=list)
    winner: str = ''
    church_seizure_fired: bool = False

def init_state(seed: int = 42) -> GameState:
    random.seed(seed)
    gs = GameState()
    # Territories
    for tid, (name, pv, sw, pr, ctrl, accord, pt) in TERRITORIES.items():
        gs.territories[tid] = Territory(tid, name, pv, sw, pr, ctrl, accord, pt)
    # T9 starts with Cathedral
    gs.territories['T9'].church_building = 3  # [canonical: Cathedral City]
    # Factions
    # [canonical: params/bg/core.md §Batch Card Hand + §Domain Expertise]
    STARTING_HANDS = {
        'Crown':     (['Legionary','Legionary','Consul','Senator','Prefect','Recess'], 'Legionary'),
        'Church':    (['Senator','Senator','Pontifex','Consul','Legionary','Recess'], 'Senator'),
        'Hafenmark': (['Consul','Consul','Senator','Legionary','Diplomat','Recess'], 'Consul'),
        'Varfell':   (['Tribune','Tribune','Legionary','Consul','Colonist','Recess'], 'Tribune'),
    }
    for fname, stats in FACTION_STATS.items():
        hand, expertise = STARTING_HANDS[fname]
        gs.factions[fname] = Faction(fname, **stats, territories=list(FACTION_TERRITORIES[fname]),
                                     hand=list(hand), expertise=expertise)
    return gs

# ═══════════════════════════════════════════════════════════════
# CI GENERATION (per season)
# [canonical: params/bg/tc_seizure.md — TC Generation; editorial_decisions §1,2]
# ═══════════════════════════════════════════════════════════════

def generate_ci(gs: GameState) -> int:
    """Calculate CI change this season. Returns delta (capped ±5)."""
    delta = 0
    church = gs.factions['Church']
    if not church.active: return 0

    # Step 1: Conditional Passive (+1 if Church Mandate > controller Mandate in ≥2 territories)
    # [canonical: params/bg/tc_seizure.md §3.2]
    prominent_count = 0
    for tid, t in gs.territories.items():
        if t.controller != 'Church' and t.controller not in ('Uncontrolled', 'LocalMilitia'):
            ctrl_faction = gs.factions.get(t.controller)
            if ctrl_faction and church.mandate > ctrl_faction.mandate:
                prominent_count += 1
    if prominent_count >= 2:
        delta += 1

    # Step 2: Piety Yield — TC += Σ(PT tier × SW/5) per prominent territory, floored
    # [canonical: params/bg/tc_seizure.md §3.3]
    piety_yield = 0.0
    for tid, t in gs.territories.items():
        ctrl_faction = gs.factions.get(t.controller)
        is_prominent = (t.controller == 'Church') or (ctrl_faction and church.mandate > ctrl_faction.mandate)
        if is_prominent and t.pt >= 4:
            piety_yield += t.pt * t.sw / 5.0
    delta += math.floor(piety_yield)

    # Step 3: Charity Advantage — Church Wealth spent → CI +1 per 2 Wealth, cap 2/season
    # [canonical: params/bg/tc_seizure.md §3.4]
    if church.wealth >= 2:
        charity = min(2, church.wealth // 2)
        delta += charity

    # Step 4: Templar Presence — +1 per territory with Church military + prominence
    # [canonical: params/bg/tc_seizure.md §3.5]
    for tid, t in gs.territories.items():
        if t.templar and t.controller == 'Church':
            delta += 1

    # Step 5: Assert (optional) — only when stability safe
    # [canonical: params/bg/tc_seizure.md §3.6 — Influence vs Ob 2]
    # [canonical: params/bg/npc_priority_trees.md Church P1 — suspend Assert if Stability=1]
    if gs.ci < 100 and church.stability >= 3:
        net, deg = check(church.influence, 2)
        if deg in ('Success', 'Overwhelming'):
            delta += 1
        else:
            church.stability -= 1
            church.clamp()

    # Step 6: Suppress — opponent with highest Mandate attempts
    # [canonical: params/bg/tc_seizure.md §3.7]
    suppressors = [(f.mandate, f) for f in gs.factions.values()
                   if f.active and f.name != 'Church' and f.mandate >= 2]
    if suppressors:
        _, suppressor = max(suppressors, key=lambda x: x[0])
        suppress_ob = max(1, church.mandate // 2 + 1)
        net, deg = check(suppressor.mandate, suppress_ob)
        if deg in ('Success', 'Overwhelming'):
            delta -= 1  # negate conditional passive
        elif deg == 'Failure':
            suppressor.stability -= 1
            suppressor.clamp()

    # Step 7: Hafenmark Structural Suppression — while Baralta Mandate ≥ 4
    # [canonical: params/bg/tc_seizure.md §3.8]
    haf = gs.factions.get('Hafenmark')
    if haf and haf.active and haf.mandate >= 4:
        delta -= 1

    # [canonical: params/bg/tc_seizure.md — seasonal cap ±5 all sources]
    delta = max(-5, min(5, delta))
    return delta

# ═══════════════════════════════════════════════════════════════
# VICTORY CHECK
# [canonical: editorial_decisions §7 — control peninsula, all factions eliminated or submitted]
# ═══════════════════════════════════════════════════════════════

def check_victory(gs: GameState):
    # [canonical: victory_v30 §0 — Universal Victory: all 15 playable territories controlled,
    #  Accord ≥ 2, all rivals eliminated or submitted. Held 2 consecutive Accountings.]
    # [canonical: editorial_decisions §7 — victory = control peninsula]
    playable = [tid for tid in gs.territories if tid not in ('T15',)]  # T15 Askeheim, T16 not in play

    for fname, f in gs.factions.items():
        if not f.active or f.submitted:
            continue

        # Check 1: all rival factions eliminated or submitted
        rivals_clear = True
        for rival_name, rival in gs.factions.items():
            if rival_name == fname:
                continue
            if rival.active and not rival.submitted:
                rivals_clear = False
                break
        if not rivals_clear:
            continue

        # Check 2: all playable territories controlled by winner (directly or via submitted factions)
        controlled = set(f.territories)
        for sub_name, sub in gs.factions.items():
            if sub.submitted and sub_name != fname:
                controlled.update(sub.territories)
        uncontrolled = [tid for tid in playable if tid not in controlled]
        if uncontrolled:
            continue

        # Check 3: Accord ≥ 2 in all directly controlled territories
        low_accord = [tid for tid in f.territories if gs.territories[tid].accord < 2]
        if low_accord:
            continue

        gs.winner = fname
        gs.log.append(f"S{gs.season}: VICTORY — {fname} controls peninsula ({len(f.territories)} territories)")
        return

    # [canonical: params/bg/core.md — RS 0 = Rupture, shared loss]
    if gs.rs <= 0:
        gs.winner = 'SHARED_LOSS'
        gs.log.append(f"S{gs.season}: SHARED LOSS — Rupture (RS=0)")

# ═══════════════════════════════════════════════════════════════
# CARD ECONOMY
# [canonical: params/bg/core.md §Batch Card Hand, params/bg/phases.md Step 3]
# Each card: play → cooldown 1 season → return to hand
# ═══════════════════════════════════════════════════════════════

def play_card(faction: Faction, card_type: str) -> bool:
    """Attempt to play a card. Returns True if card was available."""
    if card_type in faction.hand:
        faction.hand.remove(card_type)
        faction.cooldown.append(card_type)
        return True
    return False

def has_card(faction: Faction, card_type: str) -> bool:
    return card_type in faction.hand

def advance_cooldowns(gs: GameState):
    """Phase 5 Step 3: all cooldown items return to hand."""
    # [canonical: params/bg/phases.md Step 3 — Cooldown Track -1; at 0: return]
    # Simplified: 1-season cooldown, so all cooldown cards return each season
    for f in gs.factions.values():
        if f.active:
            f.hand.extend(f.cooldown)
            f.cooldown.clear()

# ═══════════════════════════════════════════════════════════════

def faction_ai_church(gs: GameState):
    f = gs.factions['Church']
    if not f.active: return

    # P1: Survival — Consul card
    # [canonical: params/bg/npc_priority_trees.md Church P1]
    if f.stability <= 2 and has_card(f, 'Consul'):
        best = max((t for t in gs.territories.values() if t.controller == 'Church'), key=lambda t: t.pt, default=None)
        if best:
            play_card(f, 'Consul')
            net, deg = check(f.influence, max(1, best.pt // 2 + 1))
            if deg in ('Success', 'Overwhelming'):
                f.stability = min(7, f.stability + 1)
            return

    # P4: Expand Piety — Consul card
    if has_card(f, 'Consul'):
        targets = [t for t in gs.territories.values() if t.controller == 'Church' and t.pt < 5]
        if targets:
            play_card(f, 'Consul')
            target = min(targets, key=lambda t: t.pt)
            net, deg = check(f.influence, max(1, target.pt // 2 + 1))
            if deg == 'Overwhelming':
                target.pt = min(5, target.pt + 1)
            elif deg == 'Success':
                target.accord = min(3, target.accord + 1)

    # Senator: diplomacy (abstract)
    if has_card(f, 'Senator'):
        play_card(f, 'Senator')

    # Legionary: reclaim uncontrolled or defend
    if has_card(f, 'Legionary') and f.military >= 2:
        lost = [t for t in gs.territories.values() if t.controller in ('Uncontrolled', 'LocalMilitia') and t.id != 'T15']
        if lost:
            play_card(f, 'Legionary')
            attempt_conquest(gs, f, lost[0])

    # Church Mass Seizure declaration (probabilistic)
    # [canonical: victory_v30 §3.2 — P(declare) = ((CI-60)/40)^3.3, CI ≥ 60]
    # Exponential curve: 1% at CI 70, 10% at CI 80, 39% at CI 90, 100% at CI 100
    if gs.ci >= 60 and not gs.church_seizure_fired:
        p_declare = min(1.0, max(0.0, ((gs.ci - 60) / 40.0) ** 3.3))
        if random.random() < p_declare:
            attempt_mass_seizure(gs)

def attempt_mass_seizure(gs: GameState):
    """One-time Mass Seizure — ALL prominent territories targeted simultaneously.
    [canonical: victory_v30 §3.2 — Mass Seizure, one-shot, Ob = 10 - PT - infrastructure (floor 1)]"""
    gs.church_seizure_fired = True
    church = gs.factions['Church']
    pool = church.influence + gs.ci // 15  # [canonical: victory_v30 §3.2]

    # Target: all non-Church territories where Church is prominent
    # [canonical: victory_v30 §3.2 — every territory with Church building]
    targets = []
    for tid, t in gs.territories.items():
        if t.controller == 'Church' or t.controller in ('Uncontrolled', 'LocalMilitia'):
            continue
        ctrl = gs.factions.get(t.controller)
        if ctrl and church.mandate > ctrl.mandate:
            targets.append(t)

    if not targets:
        gs.log.append(f"S{gs.season}: Church Mass Seizure declared — no prominent targets!")
        return

    seized = 0
    failed = 0
    for target in targets:
        # [canonical: victory_v30 §3.2 — Ob = 10 - PT + church_infra_modifier (modifier is negative)]
        ob = max(1, 10 - target.pt + target.church_infra_modifier)
        net, deg = check(pool, ob)

        if deg in ('Overwhelming', 'Success'):
            old_ctrl = target.controller
            if target.id in gs.factions[old_ctrl].territories:
                gs.factions[old_ctrl].territories.remove(target.id)
            target.controller = 'Church'
            church.territories.append(target.id)
            if deg == 'Overwhelming':
                target.accord = max(2, target.pt // 2 + 1)
                target.pt = min(5, target.pt + 1)
            else:
                target.accord = max(2, target.pt // 2 + 1)
            seized += 1
            gs.log.append(f"S{gs.season}: Church SEIZES {target.name} from {old_ctrl} ({deg})")
        elif deg == 'Partial':
            target.accord = 1
            failed += 1
        else:
            failed += 1

    # Political cost: Mass Seizure is civil war
    # [canonical: victory_v30 §3.2 — Strain +2, failed seizures generate Church Attention]
    gs.strain = min(10, gs.strain + 3)
    if failed > 0:
        church.stability = max(0, church.stability - (failed // 2))
        church.clamp()
    gs.log.append(f"S{gs.season}: Church MASS SEIZURE — {seized} seized, {failed} failed. Strain={gs.strain}")

def attempt_conquest(gs: GameState, attacker: Faction, target: Territory):
    """Universal territory conquest mechanic. Returns True if successful."""
    defender = gs.factions.get(target.controller)
    if not defender or not defender.active:
        # Uncontrolled / local militia — free claim
        target.controller = attacker.name
        if target.id not in attacker.territories:
            attacker.territories.append(target.id)
        target.accord = 1
        return True
    # [canonical: params/bg/tc_seizure.md — Battle Ob = floor(defender Military / 2) + 1]
    battle_ob = max(1, defender.military // 2 + 1)
    net, deg = check(attacker.military, battle_ob)
    if deg in ('Success', 'Overwhelming'):
        if target.id in defender.territories:
            defender.territories.remove(target.id)
        target.controller = attacker.name
        attacker.territories.append(target.id)
        target.accord = 1
        # [canonical: peninsular_strain_v30 §3 — battle consequences]
        gs.rs = max(0, gs.rs - 1)
        gs.strain = min(10, gs.strain + 1)
        gs.ip = min(100, gs.ip + 2)
        gs.log.append(f"S{gs.season}: {attacker.name} conquers {target.name} from {defender.name} ({deg})")
        if deg == 'Overwhelming':
            defender.stability = max(0, defender.stability - 1)
        # [canonical: Jordan — territory inheritance on elimination]
        # If defender has no territories left, attacker absorbs all (faction collapses)
        if len(defender.territories) == 0 and defender.active:
            defender.active = False
            defender.stability = 0
            gs.strain = min(10, gs.strain + 2)
            gs.log.append(f"S{gs.season}: {defender.name} ELIMINATED by {attacker.name} — territories absorbed")
        return True
    else:
        # Battle still happened — RS/strain cost
        gs.rs = max(0, gs.rs - 1)
        gs.strain = min(10, gs.strain + 1)
        gs.ip = min(100, gs.ip + 2)
        if deg == 'Failure':
            attacker.stability = max(0, attacker.stability - 1)
        return False

def pick_conquest_target(gs: GameState, attacker: Faction) -> Territory:
    """Pick highest-PV non-owned territory where attacker has military advantage."""
    targets = [t for t in gs.territories.values()
               if t.controller != attacker.name and t.controller not in ('Uncontrolled', 'LocalMilitia') and t.id != 'T15']
    if not targets:
        # Try uncontrolled
        targets = [t for t in gs.territories.values() if t.controller in ('Uncontrolled', 'LocalMilitia') and t.id != 'T15']
    if not targets:
        return None
    # Prefer targets where we have military advantage
    def score(t):
        ctrl = gs.factions.get(t.controller)
        if not ctrl or not ctrl.active:
            return t.pv + 10  # easy target
        advantage = attacker.military - ctrl.military
        return t.pv + advantage
    return max(targets, key=score)

def faction_ai_crown(gs: GameState):
    f = gs.factions['Crown']
    if not f.active: return

    # P1: Survival — Consul card
    # [canonical: params/bg/npc_priority_trees.md Crown P1]
    if f.stability <= 2 and has_card(f, 'Consul'):
        play_card(f, 'Consul')
        net, deg = check(f.influence, 2)
        if deg in ('Success', 'Overwhelming'):
            f.stability = min(7, f.stability + 1)
        return

    # P2: Military response — Legionary card, reclaim lost territories
    # [canonical: params/bg/npc_priority_trees.md Crown P2]
    lost = [tid for tid in FACTION_TERRITORIES['Crown'] if gs.territories[tid].controller != 'Crown']
    if lost and has_card(f, 'Legionary') and f.military >= 2:
        play_card(f, 'Legionary')
        attempt_conquest(gs, f, gs.territories[lost[0]])
        return

    # P3: Royal Decree — Prefect card (Special/Unique Priority 6)
    # [canonical: params/bg/faction_actions.md Crown Royal Decree Enhancement PP-435 — Ob 2, once/season]
    if f.mandate >= 4 and has_card(f, 'Prefect'):
        play_card(f, 'Prefect')
        net, deg = check(f.mandate, 2)  # [canonical: Mandate pool vs Ob 2]
        if deg in ('Success', 'Overwhelming'):
            weakest = min(['mandate','influence','wealth','military','stability'], key=lambda a: getattr(f, a))
            setattr(f, weakest, min(7, getattr(f, weakest) + 1))
            if deg == 'Overwhelming':
                # [canonical: PP-435 Enhancement — OW: ±2 to one faction or ±1 to two]
                setattr(f, weakest, min(7, getattr(f, weakest) + 1))

    # P4: Govern — Consul card
    # [canonical: params/bg/core.md — Govern Ob = floor(Prosperity/2)+1, -1 own capital]
    if has_card(f, 'Consul'):
        home = [gs.territories[tid] for tid in f.territories if gs.territories[tid].accord < 3]
        if home:
            play_card(f, 'Consul')
            t = min(home, key=lambda t: t.accord)
            gov_ob = max(1, t.pv // 2 + 1)  # using PV as Prosperity proxy
            if t.id == 'T1': gov_ob = max(1, gov_ob - 1)  # [canonical: -1 own capital]
            net, deg = check(f.influence, gov_ob)
            if deg in ('Success', 'Overwhelming'):
                t.accord = min(3, t.accord + 1)

    # Senator: Crown Treaty — diplomatic submission of weaker faction
    # [canonical: params/bg/core.md — Formal Crown Treaty Ob = floor(target Mandate/2)+1]
    if has_card(f, 'Senator'):
        rivals = [r for r in gs.factions.values() if r.active and not r.submitted
                  and r.name != 'Crown' and r.mandate < f.mandate]
        if rivals:
            target_r = min(rivals, key=lambda r: r.mandate)
            play_card(f, 'Senator')
            treaty_ob = max(1, target_r.mandate // 2 + 1)
            net, deg = check(f.mandate, treaty_ob)
            if deg in ('Success', 'Overwhelming'):
                # Crown Treaty: target submits (territories transfer conceptually)
                for tid in list(target_r.territories):
                    gs.territories[tid].controller = 'Crown'
                    f.territories.append(tid)
                    gs.territories[tid].accord = 2
                target_r.territories.clear()
                target_r.submitted = True
                gs.log.append(f"S{gs.season}: {target_r.name} submits to Crown via Treaty")
        else:
            play_card(f, 'Senator')

    # Legionary: expansion when stable (if still available)
    if has_card(f, 'Legionary') and f.stability >= 2 and f.military >= 2:
        target = pick_conquest_target(gs, f)
        if target:
            ctrl = gs.factions.get(target.controller)
            if not ctrl or not ctrl.active or f.military > ctrl.military:
                play_card(f, 'Legionary')
                attempt_conquest(gs, f, target)

def faction_ai_hafenmark(gs: GameState):
    f = gs.factions['Hafenmark']
    if not f.active: return

    # P1: Survival — Consul card
    if f.stability <= 2 and has_card(f, 'Consul'):
        play_card(f, 'Consul')
        net, deg = check(f.influence, 2)
        if deg in ('Success', 'Overwhelming'):
            f.stability = min(7, f.stability + 1)
        return

    # P2: Respond to Church seizure — Senator card
    # [canonical: params/bg/npc_priority_trees.md Hafenmark P2]
    if gs.church_seizure_fired and has_card(f, 'Senator'):
        if f.mandate >= 4:
            play_card(f, 'Senator')
            net, deg = check(f.mandate, max(1, gs.factions['Church'].mandate // 2 + 1))
            if deg in ('Success', 'Overwhelming'):
                gs.ci = max(0, gs.ci - 2)

    # P4: Govern — Consul card
    # [canonical: params/bg/core.md — Govern Ob = floor(Prosperity/2)+1]
    if has_card(f, 'Consul'):
        home = [gs.territories[tid] for tid in f.territories if gs.territories[tid].accord < 3]
        if home:
            play_card(f, 'Consul')
            t = min(home, key=lambda t: t.accord)
            gov_ob = max(1, t.pv // 2 + 1)
            if t.id == 'T8': gov_ob = max(1, gov_ob - 1)  # [canonical: -1 own capital]
            net, deg = check(f.influence, gov_ob)
            if deg in ('Success', 'Overwhelming'):
                t.accord = min(3, t.accord + 1)

    # P5: Dynastic Proclamation — Diplomat card
    # [canonical: params/bg/faction_actions.md PP-649 — Pool: Influence, Ob: floor(target Stability/2)+1]
    if f.mandate >= 4 and has_card(f, 'Diplomat'):
        targets = [t for t in gs.territories.values()
                   if t.controller not in ('Hafenmark', 'Uncontrolled', 'Church') and t.id != 'T15']
        if targets:
            target = max(targets, key=lambda t: t.pv)
            ctrl = gs.factions.get(target.controller)
            if ctrl and f.mandate > ctrl.mandate:
                play_card(f, 'Diplomat')
                dip_ob = max(1, ctrl.stability // 2 + 1)
                # [canonical: PP-649 — Pool: Influence. +1 Ob if PT ≤ 1]
                if target.pt <= 1: dip_ob += 1
                net, deg = check(f.influence, dip_ob)
                if deg in ('Success', 'Overwhelming'):
                    ctrl.territories.remove(target.id)
                    target.controller = 'Hafenmark'
                    f.territories.append(target.id)
                    target.accord = 2
                    ctrl.mandate = max(0, ctrl.mandate - 1)  # [canonical: PP-649 Success]
                    gs.log.append(f"S{gs.season}: Hafenmark claims {target.name} via Dynastic Proclamation")

    # Legionary: military expansion
    if has_card(f, 'Legionary') and f.stability >= 3 and f.military >= 2:
        target = pick_conquest_target(gs, f)
        if target:
            ctrl = gs.factions.get(target.controller)
            if not ctrl or not ctrl.active or f.military >= ctrl.military:
                play_card(f, 'Legionary')
                attempt_conquest(gs, f, target)

def faction_ai_varfell(gs: GameState):
    f = gs.factions['Varfell']
    if not f.active: return

    # P1: Survival — Consul card
    if f.stability <= 2 and has_card(f, 'Consul'):
        play_card(f, 'Consul')
        net, deg = check(f.influence, 2)
        if deg in ('Success', 'Overwhelming'):
            f.stability = min(7, f.stability + 1)
        return

    # P2/P3: Intel — Tribune card (+1D Domain Expertise)
    # [canonical: params/bg/npc_priority_trees.md Varfell P2/P3]
    intel_bonus = 0
    if has_card(f, 'Tribune'):
        play_card(f, 'Tribune')
        pool = f.influence + 1  # [canonical: Domain Expertise +1D for Tribune]
        net, deg = check(pool, 2)
        if deg in ('Success', 'Overwhelming'):
            intel_bonus = 1
            # [canonical: params/bg/core.md — VTM advances via intel/Thread contact]
            if random.random() < 0.3:  # ~30% chance per successful intel op
                gs.vtm = min(5, gs.vtm + 1)
                gs.log.append(f"S{gs.season}: Varfell VTM advances to {gs.vtm}")

    # Second Tribune if available
    if has_card(f, 'Tribune'):
        play_card(f, 'Tribune')
        pool = f.influence + 1
        net, deg = check(pool, 2)
        if deg in ('Success', 'Overwhelming'):
            intel_bonus += 1

    # P5: March to T15 when VTM ≥ 2 AND no unit in T15
    # [canonical: npc_behavior §8.5 P2b / params/bg/npc_priority_trees.md Varfell P5]
    if gs.vtm >= 2 and gs.territories['T15'].controller != 'Varfell' and has_card(f, 'Legionary') and f.military >= 3:
        play_card(f, 'Legionary')
        gs.territories['T15'].controller = 'Varfell'
        f.territories.append('T15')
        gs.territories['T15'].accord = 1
        gs.log.append(f"S{gs.season}: Varfell marches to T15 (Askeheim) — Warden contact imminent")

    # P4: Govern — Consul card
    # [canonical: params/bg/core.md — Govern Ob = floor(Prosperity/2)+1]
    if has_card(f, 'Consul'):
        home = [gs.territories[tid] for tid in f.territories if gs.territories[tid].accord < 3]
        if home:
            play_card(f, 'Consul')
            t = min(home, key=lambda t: t.accord)
            gov_ob = max(1, t.pv // 2 + 1)
            if t.id == 'T12': gov_ob = max(1, gov_ob - 1)  # [canonical: -1 own capital]
            net, deg = check(f.influence, gov_ob)
            if deg in ('Success', 'Overwhelming'):
                t.accord = min(3, t.accord + 1)

    # Colonist: Cultural Reformation — transfers territory on Success/OW
    # [canonical: params/bg/faction_actions.md PP-650 — Pool: Influence+floor(VTM/2), Ob: PT+1]
    # [canonical: Prerequisites: VTM ≥ 2, target PT ≤ 3, adjacent to Varfell territory]
    if has_card(f, 'Colonist'):
        # Target: non-Varfell territory with PT ≤ 3
        targets = [t for t in gs.territories.values()
                   if t.controller not in ('Varfell', 'Uncontrolled') and t.pt <= 3 and t.id != 'T15']
        if targets:
            play_card(f, 'Colonist')
            target = min(targets, key=lambda t: t.pt)  # easiest first (lowest PT)
            reform_ob = max(1, target.pt + 1)
            pool = f.influence + intel_bonus  # VTM not tracked yet; using intel_bonus as proxy
            net, deg = check(pool, reform_ob)
            if deg in ('Success', 'Overwhelming'):
                # [canonical: PP-650 — territory transfers, Accord 2, PT -1, TC -1]
                ctrl = gs.factions.get(target.controller)
                if ctrl and target.id in ctrl.territories:
                    ctrl.territories.remove(target.id)
                target.controller = 'Varfell'
                f.territories.append(target.id)
                target.accord = 2
                target.pt = max(0, target.pt - 1)
                gs.ci = max(0, gs.ci - 1)
                gs.log.append(f"S{gs.season}: Varfell claims {target.name} via Cultural Reformation ({deg})")
            elif deg == 'Partial':
                # [canonical: PP-650 Partial — no transfer, PT -1, intel presence]
                target.pt = max(0, target.pt - 1)
            else:
                # [canonical: PP-650 Failure — Stability -1, TC +1]
                f.stability = max(0, f.stability - 1)
                gs.ci = min(100, gs.ci + 1)

    # Legionary: military expansion with intel advantage
    if has_card(f, 'Legionary') and f.stability >= 2 and f.military >= 2:
        target = pick_conquest_target(gs, f)
        if target:
            ctrl = gs.factions.get(target.controller)
            if not ctrl or not ctrl.active or f.military + intel_bonus > ctrl.military:
                play_card(f, 'Legionary')
                saved_mil = f.military
                f.military += intel_bonus
                attempt_conquest(gs, f, target)
                f.military = saved_mil

# ═══════════════════════════════════════════════════════════════
# SEASON LOOP
# [canonical: params/bg/phases.md — Phase 4 + Phase 5 Accounting]
# ═══════════════════════════════════════════════════════════════

def run_season(gs: GameState):
    gs.season += 1

    # Phase 4: Faction actions (priority order)
    # [canonical: params/bg/phases.md — descending Stability order within tier]
    factions_by_stab = sorted(
        [f for f in gs.factions.values() if f.active and not f.submitted],
        key=lambda f: -f.stability
    )

    for f in factions_by_stab:
        # P0: Reclaim LocalMilitia territories — free conquest, top priority
        # [canonical: Jordan — provinces should never sit unclaimed]
        if has_card(f, 'Legionary'):
            militia_targets = [t for t in gs.territories.values()
                              if t.controller == 'LocalMilitia' and t.id != 'T15']
            if militia_targets:
                play_card(f, 'Legionary')
                target = max(militia_targets, key=lambda t: t.pv)
                target.controller = f.name
                if target.id not in f.territories:
                    f.territories.append(target.id)
                target.accord = 1
                gs.log.append(f"S{gs.season}: {f.name} reclaims {target.name} from local militia")

        if f.name == 'Church':   faction_ai_church(gs)
        elif f.name == 'Crown':  faction_ai_crown(gs)
        elif f.name == 'Hafenmark': faction_ai_hafenmark(gs)
        elif f.name == 'Varfell':   faction_ai_varfell(gs)

    # Phase 5: Accounting
    # Step 1: Apply pending changes (implicit in action resolution above)

    # Step 3: Advance Cooldown Track
    # [canonical: params/bg/phases.md Step 3]
    advance_cooldowns(gs)

    # Step 2: Stability checks — any faction with ≥2 attr loss
    # [canonical: params/bg/phases.md Step 2]
    # (simplified — full attr tracking would require per-season deltas)

    # Step 4: Clock advances
    ci_delta = generate_ci(gs)
    gs.ci = max(0, min(100, gs.ci + ci_delta))

    # RS baseline: -1/year at Year-End only
    # [canonical: params/core.md §RS Baseline Decay — -1 per in-game year at Year-End]
    is_year_end = (gs.season % 4 == 0)
    if is_year_end:
        # [canonical: params/bg/core.md §Warden Cooperation Effects]
        # WC ≥ 2: RS decay rate halved (baseline -1 becomes -0.5, rounded down)
        # WC = 3: RS +2/season at Accounting
        if gs.wc >= 2:
            pass  # halved: -0.5 rounds to 0 at Year-End
        else:
            gs.rs = max(0, gs.rs - 1)

    # WC = 3: RS +2/season (every season, not just Year-End)
    # [canonical: params/bg/core.md — WC 3: RS +2/season at Accounting]
    if gs.wc >= 3:
        gs.rs = min(100, gs.rs + 2)

    # Step 4c: Accord checks
    # [canonical: params/bg/phases.md Step 4c]
    for tid, t in gs.territories.items():
        if t.accord == 1 and not t.garrison:
            t.accord = 0  # [canonical: Accord 1 without garrison → 0]
        if t.accord == 0 and t.controller not in ('Uncontrolled', 'LocalMilitia'):
            # Revolt — territory forms local militia governance
            # [canonical: Jordan — settlements form ad-hoc faction rather than sit vacant]
            old_ctrl = t.controller
            if old_ctrl in gs.factions and tid in gs.factions[old_ctrl].territories:
                gs.factions[old_ctrl].territories.remove(tid)
            t.controller = 'LocalMilitia'
            t.accord = 1  # local governance provides minimum stability
            gs.strain = min(10, gs.strain + 1)
            gs.log.append(f"S{gs.season}: {t.name} revolts — local militia forms")

    # Step 4d: Strain update
    # [canonical: params/bg/phases.md Step 4d]
    # Peaceful season (no battles): Strain -1
    battles_this_season = any('SEIZES' in e or 'Battle' in e for e in gs.log if f'S{gs.season}' in e)
    if not battles_this_season and gs.strain > 0:
        gs.strain -= 1

    # Strain threshold effects
    # [canonical: params/bg/core.md §Peninsular Strain Threshold Effects]
    if gs.strain >= 3:
        for f in gs.factions.values():
            if f.active and not f.submitted:
                strain_ob = 1 if gs.strain <= 4 else (2 if gs.strain <= 8 else 3)
                net, deg = check(f.mandate, strain_ob)
                if deg == 'Failure':
                    f.mandate = max(0, f.mandate - 1)

    # Warden emergence + WR/WC advancement
    # [canonical: params/bg/core.md — WR gates WC; WR advances via Varfell T15 presence]
    # [canonical: npc_behavior §8.5 P2b — T15 presence prerequisite for Warden emergence]
    varfell = gs.factions.get('Varfell')
    if varfell and varfell.active and 'T15' in varfell.territories:
        # WR advances: Varfell in T15 with VTM ≥ 2 → WR +1/year at Year-End
        if is_year_end and gs.vtm >= 2 and gs.wr < 3:
            gs.wr = min(3, gs.wr + 1)
            gs.log.append(f"S{gs.season}: Warden Recognition advances to {gs.wr}")

    # WC advances when WR ≥ 2 (per-year at Year-End)
    # [canonical: params/bg/core.md — WC: WR ≥ 2 required to advance]
    if is_year_end and gs.wr >= 2 and gs.wc < 3:
        gs.wc = min(3, gs.wc + 1)
        gs.log.append(f"S{gs.season}: Warden Cooperation advances to {gs.wc}")

    # Warden emergence at WC ≥ 1
    if gs.wc >= 1 and not gs.warden_emerged:
        gs.warden_emerged = True
        gs.log.append(f"S{gs.season}: WARDEN EMERGENCE — Edeyja and Wardens active")

    # Warden active: RS stabilization
    # [canonical: params/bg/npc_priority_trees.md Edeyja P3 — RS ≤ 40: RS +1/Warden, max +2/season]
    if gs.warden_emerged and gs.rs <= 40:
        warden_rs = min(2, 1 + (1 if gs.wc >= 2 else 0))
        gs.rs = min(100, gs.rs + warden_rs)

    # Step 12: Victory check
    check_victory(gs)

    # Faction elimination check
    for f in gs.factions.values():
        if f.active:
            # [canonical: Jordan — a faction with no territories is no faction at all]
            if len(f.territories) == 0:
                f.stability = 0
        if f.active and f.stability <= 0:
            f.active = False
            # Remaining territories go to the strongest active neighbor, not Uncontrolled
            # [canonical: Jordan — provinces should never sit unclaimed]
            absorber = max(
                [r for r in gs.factions.values() if r.active and not r.submitted and r.name != f.name],
                key=lambda r: len(r.territories),
                default=None
            )
            for tid in list(f.territories):
                if absorber:
                    gs.territories[tid].controller = absorber.name
                    absorber.territories.append(tid)
                    gs.territories[tid].accord = 1  # imposed rule, not accepted
                else:
                    # No absorber — genuine collapse, local militia forms
                    gs.territories[tid].controller = 'LocalMilitia'
                    gs.territories[tid].accord = 1
            f.territories.clear()
            gs.strain = min(10, gs.strain + 2)
            gs.log.append(f"S{gs.season}: {f.name} ELIMINATED (Stability 0) — territories to {absorber.name if absorber else 'LocalMilitia'}")

def run_campaign(seed: int = 42, max_seasons: int = 120) -> GameState:
    gs = init_state(seed)
    for _ in range(max_seasons):
        run_season(gs)
        if gs.winner:
            break
    return gs

# ═══════════════════════════════════════════════════════════════
# SMOKE TEST
# ═══════════════════════════════════════════════════════════════

if __name__ == '__main__':
    print("Engine v3.1 — smoke test (5 seeds × 120 seasons)")
    results = []
    for seed in range(5):
        gs = run_campaign(seed=seed*100+42, max_seasons=120)
        results.append({
            'seed': seed,
            'winner': gs.winner or 'None',
            'season': gs.season,
            'ci': gs.ci,
            'rs': gs.rs,
            'strain': gs.strain,
            'factions': {f.name: (f.stability, len(f.territories), f.active)
                        for f in gs.factions.values()},
        })
        print(f"  seed={seed}: winner={gs.winner or 'None'} S{gs.season} CI={gs.ci} RS={gs.rs} Strain={gs.strain}")
        for f in gs.factions.values():
            print(f"    {f.name}: stab={f.stability} terr={len(f.territories)} active={f.active}")
    
    winners = [r['winner'] for r in results if r['winner'] != 'None' and r['winner'] != 'SHARED_LOSS']
    print(f"\nVictories: {len(winners)}/5")
    if winners:
        from collections import Counter
        print(f"  By faction: {dict(Counter(winners))}")
