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
    # Church infrastructure starting state
    # [canonical: Jordan — most settlements have a chapel at minimum]
    for tid, t in gs.territories.items():
        if tid == 'T9':
            t.church_building = 3  # [canonical: Cathedral City]
            t.templar = True       # Cathedral garrison
        elif tid in ('T1', 'T3', 'T8', 'T14'):
            t.church_building = 2  # Church building in major territories
        elif tid in ('T4', 'T11', 'T12', 'T13', 'T15'):
            t.church_building = 0  # Varfell/remote territories — no Church presence
        elif tid in ('T6',):
            t.church_building = 0  # Remote southern — minimal Church reach
        else:
            t.church_building = 1  # Chapel in standard territories
    # Factions
    # [canonical: params/bg/core.md §Batch Card Hand + §Domain Expertise]
    STARTING_HANDS = {
        'Crown':     (['Legionary','Legionary','Consul','Senator','Prefect','Recess'], 'Legionary'),
        'Church':    (['Senator','Senator','Pontifex','Consul','Legionary','Recess'], 'Senator'),
        'Hafenmark': (['Consul','Consul','Senator','Legionary','Diplomat','Recess'], 'Consul'),
        'Varfell':   (['Tribune','Tribune','Legionary','Legionary','Consul','Recess'], 'Tribune'),
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

    # Step 2: Piety Yield — TC += Σ(PT_tier × SW/5) per prominent territory, floored
    # [canonical: ci_political_v30 §1, ED-721 resolved 2026-04-20]
    # PT_tier is non-linear (NOT literal PT): see canonical table.
    PT_TIER = {5: 1.0, 4: 0.5, 3: 0.25, 2: 0.10, 1: 0.0, 0: 0.0}
    piety_yield = 0.0
    for tid, t in gs.territories.items():
        ctrl_faction = gs.factions.get(t.controller)
        is_prominent = (t.controller == 'Church') or (ctrl_faction and church.mandate > ctrl_faction.mandate)
        if is_prominent:
            piety_yield += PT_TIER.get(t.pt, 0.0) * (t.sw / 5.0)
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

    # P2: Heresy Investigation — target Thread-active faction leaders
    # [canonical: Jordan — Vaynard faces heresy charges for Thread work]
    # [canonical: params/bg/npc_priority_trees.md Church P2]
    if has_card(f, 'Pontifex'):
        # Target Varfell first (Thread-active), then any faction with low PT in their capital
        varfell = gs.factions.get('Varfell')
        if varfell and varfell.active and not varfell.submitted:
            play_card(f, 'Pontifex')
            # Heresy Investigation: Church Influence vs target Stability
            net, deg = check(f.influence, max(1, varfell.stability // 2 + 1))
            if deg == 'Overwhelming':
                varfell.mandate = max(0, varfell.mandate - 1)
                varfell.stability = max(0, varfell.stability - 1)
                gs.log.append(f"S{gs.season}: Church HERESY charges against Varfell (OW) — Mandate-1, Stability-1")
            elif deg == 'Success':
                varfell.mandate = max(0, varfell.mandate - 1)
                gs.log.append(f"S{gs.season}: Church heresy investigation of Varfell — Mandate-1")

    # P3: Church infrastructure investment — upgrade buildings, deploy Templars/Inquisitors
    # [canonical: Jordan — Church regularly invests in chapel→church→cathedral, Templars, Inquisitors]
    if has_card(f, 'Consul'):
        play_card(f, 'Consul')
        # Upgrade priority: highest-PT non-maxed territory (bias toward existing Church presence)
        upgrade_targets = sorted(
            [t for t in gs.territories.values()
             if t.church_building < 3 and t.controller != 'Varfell'
             and not (t.controller == 'Hafenmark' and gs.factions.get('Hafenmark') and gs.factions['Hafenmark'].mandate >= 4)  # Baralta blocks Church building
             and t.id != 'T15'],
            key=lambda t: (-t.pt, -t.church_building)  # favor high PT, then upgrade existing
        )
        if upgrade_targets:
            target = upgrade_targets[0]
            # Upgrade building: Influence vs Ob = current_level + 1
            net, deg = check(f.influence, target.church_building + 1)
            if deg in ('Success', 'Overwhelming'):
                target.church_building = min(3, target.church_building + 1)
                bnames = {1: 'Chapel', 2: 'Church', 3: 'Cathedral'}
                gs.log.append(f"S{gs.season}: Church builds {bnames[target.church_building]} in {target.name}")
                # PT boost from building
                if target.church_building >= 2 and target.pt < 5:
                    target.pt = min(5, target.pt + 1)

    # P3b: Deploy Templar — military presence biased toward Cathedrals > Churches
    # [canonical: Jordan — increasing Templar presence biased toward cathedrals]
    if has_card(f, 'Legionary') and f.military >= 2:
        templar_targets = sorted(
            [t for t in gs.territories.values()
             if not t.templar and t.church_building >= 2 and t.id != 'T15'],
            key=lambda t: -t.church_building  # Cathedral first
        )
        if templar_targets:
            play_card(f, 'Legionary')
            target = templar_targets[0]
            target.templar = True
            gs.log.append(f"S{gs.season}: Church deploys Templar Station in {target.name}")
        else:
            # No Templar targets — use for military defense/reclaim
            lost = [t for t in gs.territories.values() if t.controller in ('Uncontrolled', 'LocalMilitia') and t.id != 'T15']
            if lost:
                play_card(f, 'Legionary')
                attempt_conquest(gs, f, lost[0])

    # P3c: Deploy Inquisitor — suppresses RM, raises Seizure Ob for rivals
    # [canonical: Jordan — Inquisitors suppress RM and target faction leadership]
    if has_card(f, 'Senator'):
        play_card(f, 'Senator')
        inq_targets = sorted(
            [t for t in gs.territories.values()
             if not t.inquisitor and t.church_building >= 1 and t.id != 'T15'
             and t.controller != 'Varfell'],  # can't operate in hostile territory
            key=lambda t: (-t.church_building, t.pt)
        )
        if inq_targets:
            target = inq_targets[0]
            target.inquisitor = True
            gs.log.append(f"S{gs.season}: Church deploys Inquisitor in {target.name}")

    # Church Mass Seizure declaration (probabilistic, fires earlier)
    # [canonical: victory_v30 §3.2 — shifted curve for earlier declaration]
    # P = ((CI-40)/60)^2.5: CI 50→2%, CI 60→8%, CI 70→19%, CI 80→35%, CI 90→57%, CI 100→100%
    if gs.ci >= 40 and not gs.church_seizure_fired:
        p_declare = min(1.0, max(0.0, ((gs.ci - 40) / 60.0) ** 2.5))
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
        # [canonical: Jordan — Baralta suppresses Church in Hafenmark territory]
        haf = gs.factions.get('Hafenmark')
        if haf and haf.active and target.controller == 'Hafenmark' and haf.mandate >= 4:
            ob += 3  # constitutional resistance to Church seizure
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
    # [canonical: Jordan — Hafenmark discipline + equipment defensive advantage]
    if defender.name == 'Hafenmark':
        battle_ob += 1  # fortified positions + better equipment
    atk_pool = attacker.military
    # [canonical: Jordan — Hafenmark smithing/equipment advantage]
    if attacker.name == 'Hafenmark':
        atk_pool += 1  # equipment bonus from mines
    net, deg = check(atk_pool, battle_ob)
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
    # Crown aggressively pursues treaties when it has military/territorial advantage
    if has_card(f, 'Senator'):
        rivals = sorted(
            [r for r in gs.factions.values() if r.active and not r.submitted
             and r.name != 'Crown' and (r.mandate < f.mandate or len(r.territories) < len(f.territories) // 2)],
            key=lambda r: len(r.territories)  # target weakest first
        )
        if rivals:
            target_r = rivals[0]
            play_card(f, 'Senator')
            treaty_ob = max(1, target_r.mandate // 2 + 1)
            # +1D if Crown has 2× territories
            pool = f.mandate
            if len(f.territories) >= 2 * max(1, len(target_r.territories)):
                pool += 1
            net, deg = check(pool, treaty_ob)
            if deg in ('Success', 'Overwhelming'):
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

    # Hafenmark Wealth advantage — mine income
    # [canonical: Jordan — fantastic material wealth from mines]
    # +1 Wealth per 2 territories held (mine network), capped at 7
    mine_bonus = min(2, len(f.territories) // 3)
    if mine_bonus > 0 and f.wealth < 7:
        f.wealth = min(7, f.wealth + mine_bonus)

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
                # [canonical: Jordan — Hafenmark wealth backs diplomatic claims]
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

    # Legionary: military expansion — Hafenmark uses wealth-backed professional army
    # [canonical: Jordan — better troops/equipment from mines, discipline from Baralta]
    if has_card(f, 'Legionary') and f.stability >= 3 and f.military >= 2:
        target = pick_conquest_target(gs, f)
        if target:
            ctrl = gs.factions.get(target.controller)
            effective_mil = f.military + f.wealth // 3  # wealth funds better equipment
            if not ctrl or not ctrl.active or effective_mil >= ctrl.military:
                play_card(f, 'Legionary')
                # Temporarily boost military for the conquest roll
                saved_mil = f.military
                f.military = effective_mil
                attempt_conquest(gs, f, target)
                f.military = saved_mil

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


    # Second Tribune if available
    if has_card(f, 'Tribune'):
        play_card(f, 'Tribune')
        pool = f.influence + 1
        net, deg = check(pool, 2)
        if deg in ('Success', 'Overwhelming'):
            intel_bonus += 1

    # P5: March to T15 — Varfell's Thread investigation path
    # [canonical: npc_behavior §8.5 P2b — VTM struck; march gates on faction stability + military]
    if gs.territories['T15'].controller != 'Varfell' and has_card(f, 'Legionary') and f.military >= 3 and f.stability >= 3:
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

    # Varfell expansion is purely military — Vaynard is a conqueror
    # [canonical: Jordan — Vaynard is Reinhardt. Militaristic, opportunistic. Thread is a force multiplier.]
    # Colonist card repurposed: strategic positioning / supply lines (+1 Military next conquest)
    if has_card(f, 'Colonist'):
        play_card(f, 'Colonist')
        # Colonist = forward staging — temporary military boost for next engagement
        # (absorbed into the Legionary action below via intel_bonus)
        intel_bonus += 1

    # Legionary: military expansion — Vaynard is relentlessly aggressive
    # [canonical: Jordan — extremely militaristic and opportunistic]
    # Intel advantage: knows enemy stats, picks weakest target, +1D per successful Tribune
    if has_card(f, 'Legionary') and f.military >= 2:
        target = pick_conquest_target(gs, f)
        if target:
            play_card(f, 'Legionary')
            saved_mil = f.military
            f.military += intel_bonus  # Tribune intel + Colonist staging bonus
            attempt_conquest(gs, f, target)
            f.military = saved_mil

    # Second Legionary if available — Vaynard presses advantage
    if has_card(f, 'Legionary') and f.military >= 2:
        target = pick_conquest_target(gs, f)
        if target:
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

    # RS baseline: -1/season (EVERY season, not just Year-End)
    # [canonical: params/bg/clocks.md — "seasonal baseline -1"]
    is_year_end = (gs.season % 4 == 0)
    rs_delta = -1  # baseline decay per season

    # [canonical: params/bg/core.md §Warden Cooperation Effects]
    # WC ≥ 2: RS decay rate halved (baseline -1 becomes -0.5, rounded down)
    if gs.wc >= 2:
        rs_delta = 0  # halved: floor(-0.5) = 0 baseline

    # WC = 3: RS +2/season at Accounting
    # [canonical: params/bg/core.md — WC 3: RS +2/season]
    # Net effect at WC 3: 0 baseline + 2 = +2/season (stabilization, not immunity)
    if gs.wc >= 3:
        rs_delta += 2

    # [canonical: params/bg/clocks.md — Strain 9-10 Collapse: RS -1/season additional]
    if gs.strain >= 9:
        rs_delta -= 1

    gs.rs = max(0, min(100, gs.rs + rs_delta))

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

    # Territory pressure — factions losing ground destabilize
    # [canonical: Jordan — increase elimination cascade speed]
    for f in gs.factions.values():
        if f.active and not f.submitted:
            home_count = len([tid for tid in FACTION_TERRITORIES.get(f.name, [])
                             if gs.territories[tid].controller == f.name])
            starting = len(FACTION_TERRITORIES.get(f.name, []))
            if starting > 0:
                lost_ratio = 1.0 - (home_count / starting)
                # Lost >50% of home territories: -1 Stability/season
                if lost_ratio > 0.5:
                    f.stability = max(0, f.stability - 1)
                    f.clamp()
            # Forced submission: ≤ 2 territories vs dominant faction with ≥ 10
            if len(f.territories) <= 2:
                dominant = max(
                    [r for r in gs.factions.values() if r.active and not r.submitted and r.name != f.name],
                    key=lambda r: len(r.territories), default=None
                )
                if dominant and len(dominant.territories) >= 10:
                    f.submitted = True
                    for tid in list(f.territories):
                        gs.territories[tid].controller = dominant.name
                        dominant.territories.append(tid)
                        gs.territories[tid].accord = 1
                    f.territories.clear()
                    gs.log.append(f"S{gs.season}: {f.name} SUBMITS to {dominant.name} ({dominant.name} holds {len(dominant.territories)} territories)")

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
        # WR advances: Varfell present in T15 → WR +1/year at Year-End
        if is_year_end and gs.wr < 3:
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
