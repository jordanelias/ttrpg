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
    for fname, stats in FACTION_STATS.items():
        gs.factions[fname] = Faction(fname, **stats, territories=list(FACTION_TERRITORIES[fname]))
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
        if t.controller != 'Church' and t.controller != 'Uncontrolled':
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

    # Step 5: Assert (optional) — Church AI decides; simplified as: attempt if CI < 100
    # [canonical: params/bg/tc_seizure.md §3.6 — Influence vs Ob 2]
    if gs.ci < 100:
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
    for fname, f in gs.factions.items():
        if not f.active or f.submitted:
            continue
        # Check if this faction controls or dominates all others
        all_controlled = True
        for rival_name, rival in gs.factions.items():
            if rival_name == fname:
                continue
            if rival.active and not rival.submitted:
                all_controlled = False
                break
        if all_controlled:
            gs.winner = fname
            gs.log.append(f"S{gs.season}: VICTORY — {fname} controls peninsula")
            return

    # [canonical: params/bg/core.md — RS 0 = Rupture, shared loss]
    if gs.rs <= 0:
        gs.winner = 'SHARED_LOSS'
        gs.log.append(f"S{gs.season}: SHARED LOSS — Rupture (RS=0)")

# ═══════════════════════════════════════════════════════════════
# FACTION AI — 7-PRIORITY TREES
# [canonical: params/bg/npc_priority_trees.md]
# ═══════════════════════════════════════════════════════════════

def faction_ai_church(gs: GameState):
    f = gs.factions['Church']
    if not f.active: return

    # P1: Survival
    if f.stability <= 2:
        # Consul Inward highest-PT territory
        best = max((t for t in gs.territories.values() if t.controller == 'Church'), key=lambda t: t.pt, default=None)
        if best:
            net, deg = check(f.influence, max(1, best.pt // 2 + 1))
            if deg in ('Success', 'Overwhelming'):
                f.stability = min(7, f.stability + 1)
        return

    # P2: Heresy response — simplified: if any territory lost PT this season, investigate
    # (tracked implicitly; skip for now)

    # P3: CI advancement — handled in generate_ci (Assert)

    # P4: Expand Piety — Consul Inward lowest-PT territory with Church presence
    targets = [t for t in gs.territories.values() if t.controller == 'Church' and t.pt < 5]
    if targets:
        target = min(targets, key=lambda t: t.pt)
        net, deg = check(f.influence, max(1, target.pt // 2 + 1))
        if deg == 'Overwhelming':
            target.pt = min(5, target.pt + 1)
        elif deg == 'Success':
            target.accord = min(3, target.accord + 1)

    # Church seizure attempt (one-time, CI ≥ 60)
    # [canonical: Jordan correction 2026-04-18 — CI ≥ 75, one-time seizure]
    if gs.ci >= 75 and not gs.church_seizure_fired:  # [canonical: Jordan correction — CI ≥ 75, one-time]
        attempt_church_seizure(gs)

def attempt_church_seizure(gs: GameState):
    """One-time Church seizure attempt. [canonical: editorial_decisions §4,6]"""
    gs.church_seizure_fired = True
    church = gs.factions['Church']
    # Target: highest-PV non-Church territory where Church is prominent
    targets = []
    for tid, t in gs.territories.items():
        if t.controller == 'Church' or t.controller == 'Uncontrolled':
            continue
        ctrl = gs.factions.get(t.controller)
        if ctrl and church.mandate > ctrl.mandate:
            targets.append(t)
    if not targets:
        gs.log.append(f"S{gs.season}: Church seizure — no prominent targets available")
        return

    target = max(targets, key=lambda t: t.pv)
    # [canonical: editorial_decisions §4 — Ob = 10 - PT - infrastructure]
    ob = max(1, 10 - target.pt + target.church_infra_modifier)
    pool = church.influence + gs.ci // 15  # [canonical: victory_v30 §3.2 — Pool = Influence + floor(CI/15)]
    net, deg = check(pool, ob)

    if deg == 'Overwhelming':
        old_ctrl = target.controller
        gs.factions[old_ctrl].territories.remove(target.id)
        target.controller = 'Church'
        church.territories.append(target.id)
        target.accord = max(2, target.pt // 2 + 1)
        target.pt = min(5, target.pt + 1)
        gs.log.append(f"S{gs.season}: Church SEIZES {target.name} from {old_ctrl} (OW). Accord={target.accord}")
    elif deg == 'Success':
        old_ctrl = target.controller
        gs.factions[old_ctrl].territories.remove(target.id)
        target.controller = 'Church'
        church.territories.append(target.id)
        target.accord = max(2, target.pt // 2 + 1)
        gs.log.append(f"S{gs.season}: Church SEIZES {target.name} from {old_ctrl}. Accord={target.accord}")
    elif deg == 'Partial':
        target.accord = 1
        gs.log.append(f"S{gs.season}: Church seizure of {target.name} — PARTIAL. Accord→1")
    else:
        church.stability -= 1
        church.clamp()
        gs.log.append(f"S{gs.season}: Church seizure of {target.name} — FAILURE. Stability-1")

    # Political cost: Casus Belli
    gs.strain = min(10, gs.strain + 2)
    gs.log.append(f"S{gs.season}: Church seizure attempt → Strain+2 ({gs.strain})")

def faction_ai_crown(gs: GameState):
    f = gs.factions['Crown']
    if not f.active: return

    # P1: Survival
    if f.stability <= 2:
        net, deg = check(f.influence, max(1, 2))
        if deg in ('Success', 'Overwhelming'):
            f.stability = min(7, f.stability + 1)
        return

    # P2: Military response if territories lost
    lost = [tid for tid in FACTION_TERRITORIES['Crown'] if gs.territories[tid].controller != 'Crown']
    if len(lost) >= 2 or gs.coup_counter >= 2 or gs.pi >= 8:
        # Legionary action — attempt to reclaim one territory
        if lost and f.military >= 2:
            target = gs.territories[lost[0]]
            defender = gs.factions.get(target.controller)
            if defender and defender.active:
                battle_ob = max(1, defender.military // 2 + 1)
                net, deg = check(f.military, battle_ob)
                if deg in ('Success', 'Overwhelming'):
                    defender.territories.remove(target.id)
                    target.controller = 'Crown'
                    f.territories.append(target.id)
                    target.accord = 1
                    gs.rs = max(0, gs.rs - 1)
                    gs.strain = min(10, gs.strain + 1)
                    gs.ip = min(100, gs.ip + 2)
        return

    # P3: Royal Decree — boost weakest stat
    if f.mandate >= 4:
        weakest = min(['mandate','influence','wealth','military','stability'], key=lambda a: getattr(f, a))
        setattr(f, weakest, min(7, getattr(f, weakest) + 1))

    # P4: Default — Govern
    home = [gs.territories[tid] for tid in f.territories if gs.territories[tid].accord < 3]
    if home:
        t = min(home, key=lambda t: t.accord)
        gov_ob = max(1, t.accord)
        net, deg = check(f.influence, gov_ob)
        if deg in ('Success', 'Overwhelming'):
            t.accord = min(3, t.accord + 1)

def faction_ai_hafenmark(gs: GameState):
    f = gs.factions['Hafenmark']
    if not f.active: return

    # P1: Survival
    if f.stability <= 2:
        net, deg = check(f.influence, 2)
        if deg in ('Success', 'Overwhelming'):
            f.stability = min(7, f.stability + 1)
        return

    # P2: Respond to Church seizure
    if gs.church_seizure_fired:
        # Parliamentary objection
        if f.mandate >= 4:
            net, deg = check(f.mandate, max(1, gs.factions['Church'].mandate // 2 + 1))
            if deg in ('Success', 'Overwhelming'):
                gs.ci = max(0, gs.ci - 2)

    # P3: Suppress CI (handled in generate_ci)

    # P4: Govern + trade
    home = [gs.territories[tid] for tid in f.territories if gs.territories[tid].accord < 3]
    if home:
        t = min(home, key=lambda t: t.accord)
        net, deg = check(f.influence, max(1, t.accord))
        if deg in ('Success', 'Overwhelming'):
            t.accord = min(3, t.accord + 1)

    # P5: Diplomatic expansion — attempt to gain territory via Dynastic Proclamation
    if f.mandate >= 4:
        adjacent_non_haf = [t for t in gs.territories.values()
                           if t.controller not in ('Hafenmark', 'Uncontrolled', 'Church')]
        if adjacent_non_haf and random.random() < 0.15:
            target = random.choice(adjacent_non_haf)
            ctrl = gs.factions.get(target.controller)
            if ctrl:
                dip_ob = max(1, ctrl.stability // 2 + 1)
                net, deg = check(f.mandate, dip_ob)
                if deg == 'Overwhelming':
                    ctrl.territories.remove(target.id)
                    target.controller = 'Hafenmark'
                    f.territories.append(target.id)
                    target.accord = 2

def faction_ai_varfell(gs: GameState):
    f = gs.factions['Varfell']
    if not f.active: return

    # P1: Survival
    if f.stability <= 2:
        net, deg = check(f.influence, 2)
        if deg in ('Success', 'Overwhelming'):
            f.stability = min(7, f.stability + 1)
        return

    # P2: Intel — Tribune investigate
    # Reveal hidden stat of richest rival
    rivals = [r for r in gs.factions.values() if r.active and r.name != 'Varfell']
    if rivals:
        target_rival = max(rivals, key=lambda r: r.wealth)
        net, deg = check(f.influence, 2)
        if deg in ('Success', 'Overwhelming'):
            pass  # Intel gathered (abstract — no hidden stat tracking yet)

    # P3: Military expansion into adjacent territories
    if f.military >= 3 and random.random() < 0.1:
        targets = [t for t in gs.territories.values()
                  if t.controller not in ('Varfell', 'Uncontrolled')]
        if targets:
            target = random.choice(targets)
            ctrl = gs.factions.get(target.controller)
            if ctrl:
                battle_ob = max(1, ctrl.military // 2 + 1)
                net, deg = check(f.military, battle_ob)
                if deg in ('Success', 'Overwhelming'):
                    ctrl.territories.remove(target.id)
                    target.controller = 'Varfell'
                    f.territories.append(target.id)
                    target.accord = 1
                    gs.rs = max(0, gs.rs - 1)
                    gs.strain = min(10, gs.strain + 1)
                    gs.ip = min(100, gs.ip + 2)

    # P4: Govern
    home = [gs.territories[tid] for tid in f.territories if gs.territories[tid].accord < 3]
    if home:
        t = min(home, key=lambda t: t.accord)
        net, deg = check(f.influence, max(1, t.accord))
        if deg in ('Success', 'Overwhelming'):
            t.accord = min(3, t.accord + 1)

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
        if f.name == 'Church':   faction_ai_church(gs)
        elif f.name == 'Crown':  faction_ai_crown(gs)
        elif f.name == 'Hafenmark': faction_ai_hafenmark(gs)
        elif f.name == 'Varfell':   faction_ai_varfell(gs)

    # Phase 5: Accounting
    # Step 1: Apply pending changes (implicit in action resolution above)

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
        gs.rs = max(0, gs.rs - 1)

    # Step 4c: Accord checks
    # [canonical: params/bg/phases.md Step 4c]
    for tid, t in gs.territories.items():
        if t.accord == 1 and not t.garrison:
            t.accord = 0  # [canonical: Accord 1 without garrison → 0]
        if t.accord == 0 and t.controller != 'Uncontrolled':
            # Revolt — territory becomes Uncontrolled
            old_ctrl = t.controller
            if old_ctrl in gs.factions and tid in gs.factions[old_ctrl].territories:
                gs.factions[old_ctrl].territories.remove(tid)
            t.controller = 'Uncontrolled'
            gs.strain = min(10, gs.strain + 1)

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

    # Step 12: Victory check
    check_victory(gs)

    # Faction elimination check
    for f in gs.factions.values():
        if f.active and f.stability <= 0:
            f.active = False
            # Release territories
            for tid in list(f.territories):
                gs.territories[tid].controller = 'Uncontrolled'
                gs.territories[tid].accord = 0
            f.territories.clear()
            gs.strain = min(10, gs.strain + 2)
            gs.log.append(f"S{gs.season}: {f.name} ELIMINATED (Stability 0)")

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
    print("Engine v3 — smoke test (5 seeds × 120 seasons)")
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
