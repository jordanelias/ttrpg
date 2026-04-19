"""
Valoria — Emergent Arc Test (Provisional Mechanics)
Tests: settlement_adjacency_v30, fractional_province_ownership_v30, faction_succession_split_v30
These three are PROVISIONAL (PP-666) and have never been smoke-tested.

Goal: run targeted scenario seeds to surface emergent arcs,
mechanical breakdowns, and design gaps.
Not a full engine rebuild — implements only the mechanics needed for interaction testing.
"""

import random
from dataclasses import dataclass, field
from typing import Optional
from copy import deepcopy

# ─── SUBSTRATE ───────────────────────────────────────────────────────────────

SETTLEMENTS = {
    # S#: (name, province, type, controller, prosperity, discipline, order, is_seat)
    "S001": dict(name="Valorsplatz Palace",    prov="T1",  stype="Seat",     ctrl="Crown",      P=4, D=3, O=4, seat=True),
    "S002": dict(name="Valorsplatz Riverside", prov="T1",  stype="Port",     ctrl="Crown",      P=4, D=1, O=3, seat=False),
    "S003": dict(name="Valorsplatz Cathedral", prov="T1",  stype="Cathedral",ctrl="Church",     P=2, D=1, O=4, seat=False),
    "S004": dict(name="Kronmark",              prov="T2",  stype="Town",     ctrl="Crown",      P=3, D=1, O=3, seat=True),
    "S005": dict(name="Kronmark Watchtower",   prov="T2",  stype="Fortress", ctrl="Crown",      P=1, D=3, O=3, seat=False),
    "S006": dict(name="Lowenskyst Fortress",   prov="T3",  stype="Fortress", ctrl="Crown",      P=1, D=4, O=4, seat=True),
    "S007": dict(name="Lowenskyst Garrison",   prov="T3",  stype="Town",     ctrl="Crown",      P=2, D=1, O=3, seat=False),
    "S008": dict(name="Feldmark",              prov="T5",  stype="Town",     ctrl="Crown",      P=4, D=0, O=3, seat=True),
    "S009": dict(name="Feldmark Storehouse",   prov="T5",  stype="Mine",     ctrl="Crown",      P=3, D=0, O=2, seat=False),
    "S010": dict(name="Stillhelm",             prov="T6",  stype="Town",     ctrl="Crown",      P=2, D=0, O=2, seat=True),
    "S011": dict(name="Stillhelm Watch",       prov="T6",  stype="Outpost",  ctrl="Crown",      P=0, D=2, O=2, seat=False),
    "S012": dict(name="Ehrenfeld Citadel",     prov="T14", stype="Fortress", ctrl="Crown",      P=1, D=4, O=4, seat=True),
    "S013": dict(name="Ehrenfeld Market",      prov="T14", stype="City",     ctrl="Crown",      P=3, D=1, O=3, seat=False),
    "S014": dict(name="Ehrenfeld Barracks",    prov="T14", stype="Fortress", ctrl="Löwenritter",P=1, D=3, O=4, seat=False),
    "S015": dict(name="Gransol Parliament",    prov="T8",  stype="Seat",     ctrl="Hafenmark",  P=4, D=2, O=4, seat=True),
    "S016": dict(name="Gransol Harbor",        prov="T8",  stype="Port",     ctrl="Hafenmark",  P=4, D=1, O=3, seat=False),
    "S017": dict(name="Gransol Market Quarter",prov="T8",  stype="City",     ctrl="Guilds",     P=5, D=0, O=3, seat=False),
    "S018": dict(name="Rendstad",              prov="T7",  stype="Town",     ctrl="Hafenmark",  P=2, D=0, O=2, seat=True),
    "S019": dict(name="Spartfell Fortress",    prov="T10", stype="Fortress", ctrl="Hafenmark",  P=1, D=3, O=3, seat=True),
    "S020": dict(name="Spartfell Village",     prov="T10", stype="Town",     ctrl="Hafenmark",  P=2, D=1, O=2, seat=False),
    "S021": dict(name="Halvarshelm Mines",     prov="T17", stype="Mine",     ctrl="Hafenmark",  P=3, D=0, O=2, seat=True),
    "S022": dict(name="Halvarshelm Town",      prov="T17", stype="Town",     ctrl="Hafenmark",  P=2, D=0, O=3, seat=False),
    "S023": dict(name="Himmelenger Cathedral", prov="T9",  stype="Cathedral",ctrl="Church",     P=3, D=2, O=5, seat=True),
    "S024": dict(name="Himmelenger City",      prov="T9",  stype="City",     ctrl="Church",     P=3, D=1, O=4, seat=False),
    "S025": dict(name="Himmelenger Seminary",  prov="T9",  stype="Cathedral",ctrl="Church",     P=1, D=1, O=5, seat=False),
    "S026": dict(name="Sigurdshelm Keep",      prov="T12", stype="Seat",     ctrl="Varfell",    P=3, D=2, O=3, seat=True),
    "S027": dict(name="Sigurdshelm Cove",      prov="T12", stype="Port",     ctrl="Varfell",    P=2, D=1, O=2, seat=False),
    "S028": dict(name="Grauwald",              prov="T4",  stype="Town",     ctrl="Varfell",    P=2, D=0, O=2, seat=True),
    "S029": dict(name="Grauwald Lodge",        prov="T4",  stype="Outpost",  ctrl="RM",         P=1, D=0, O=2, seat=False),
    "S030": dict(name="Halvardshelm",          prov="T11", stype="Town",     ctrl="Varfell",    P=2, D=0, O=2, seat=True),
    "S031": dict(name="Oastad",                prov="T13", stype="Town",     ctrl="Varfell",    P=2, D=0, O=2, seat=True),
    "S032": dict(name="Oastad Shrine",         prov="T13", stype="Outpost",  ctrl="RM",         P=0, D=0, O=1, seat=False),
    "S033": dict(name="Askeheim Ruins",        prov="T15", stype="Outpost",  ctrl="Wardens",    P=0, D=1, O=1, seat=False),
    "S034": dict(name="Askeheim Gate",         prov="T15", stype="Outpost",  ctrl="None",       P=0, D=0, O=0, seat=False),
    "S035": dict(name="Schoenland City",       prov="T16", stype="City",     ctrl="Schoenland", P=4, D=2, O=4, seat=True),
    "S036": dict(name="Schoenland Harbor",     prov="T16", stype="Port",     ctrl="Schoenland", P=3, D=3, O=4, seat=False),
}

# Province base PV (from geography_v30 — approximated from settlement count + political importance)
PROVINCE_BASE_PV = {
    "T1": 5, "T2": 3, "T3": 3, "T4": 2, "T5": 3, "T6": 2,
    "T7": 1, "T8": 4, "T9": 4, "T10": 2, "T11": 1, "T12": 3,
    "T13": 2, "T14": 4, "T15": 1, "T16": 2, "T17": 2,
}

# Province adjacency (from geography_v30)
# Key: province → adjacent provinces
PROVINCE_ADJ = {
    "T1":  ["T2", "T3", "T5", "T14"],
    "T2":  ["T1", "T3", "T4", "T5"],
    "T3":  ["T1", "T2"],
    "T4":  ["T2", "T11", "T12"],
    "T5":  ["T1", "T2", "T6", "T8"],
    "T6":  ["T5", "T15"],
    "T7":  ["T8", "T10"],
    "T8":  ["T5", "T7", "T9", "T10", "T14"],
    "T9":  ["T8", "T10", "T11", "T14"],
    "T10": ["T7", "T8", "T9"],
    "T11": ["T4", "T9", "T12", "T13"],
    "T12": ["T4", "T11", "T13"],
    "T13": ["T11", "T12", "T15"],
    "T14": ["T1", "T8", "T9"],
    "T15": ["T6", "T13"],
    "T16": [],  # island — naval only
    "T17": ["T7"],
}

# Settlement adjacency (intra-province: all same-province settlements adjacent by default;
# inter-province: one key edge per province-pair — Seat to Seat as primary)
# Edge format: (s1, s2, edge_type)
SETTLEMENT_EDGES = []
def build_settlement_adjacency():
    # Intra-province: all settlements in same province fully connected
    by_prov = {}
    for sid, sd in SETTLEMENTS.items():
        by_prov.setdefault(sd['prov'], []).append(sid)
    for prov, sids in by_prov.items():
        for i in range(len(sids)):
            for j in range(i+1, len(sids)):
                SETTLEMENT_EDGES.append((sids[i], sids[j], "road"))
    # Inter-province: Seat-to-Seat edges using province adjacency
    seats = {sd['prov']: sid for sid, sd in SETTLEMENTS.items() if sd['seat']}
    seen = set()
    for p1, adj in PROVINCE_ADJ.items():
        for p2 in adj:
            key = tuple(sorted([p1, p2]))
            if key in seen:
                continue
            seen.add(key)
            s1 = seats.get(p1)
            s2 = seats.get(p2)
            if s1 and s2:
                # Classify edge type
                etype = "road"
                mountain_pairs = {("T3","T1"),("T10","T7"),("T15","T6"),("T15","T13")}
                if tuple(sorted([p1,p2])) in mountain_pairs:
                    etype = "mountain_pass"
                SETTLEMENT_EDGES.append((s1, s2, etype))

build_settlement_adjacency()

# ─── DICE ENGINE ─────────────────────────────────────────────────────────────

def roll(pool: int, ob: int, rng) -> str:
    """d10 dice pool vs Ob (TN 7). Returns: Overwhelming/Success/Partial/Failure."""
    pool = max(1, pool)
    hits = sum(1 for _ in range(pool) if rng.randint(1, 10) >= 7)
    margin = hits - ob
    if margin >= 2:
        return "Overwhelming"
    elif margin >= 0:
        return "Success"
    elif margin >= -1:
        return "Partial"
    else:
        return "Failure"

# ─── FRACTIONAL PROVINCE OWNERSHIP ───────────────────────────────────────────

def compute_pv_shares(settlements: dict, province: str) -> dict:
    """Returns {controller: pv_share} for a province, weighted by Prosperity."""
    prov_settlements = {sid: sd for sid, sd in settlements.items() if sd['prov'] == province}
    total_p = sum(sd['P'] for sd in prov_settlements.values()) or 1
    base_pv = PROVINCE_BASE_PV.get(province, 1)
    shares = {}
    for sid, sd in prov_settlements.items():
        ctrl = sd['ctrl']
        share = (sd['P'] / total_p) * base_pv
        shares[ctrl] = shares.get(ctrl, 0) + share
    return shares

def is_fractional(settlements: dict, province: str) -> bool:
    """Province is fractional if non-Seat settlements have different controllers than Seat."""
    prov_s = {sid: sd for sid, sd in settlements.items() if sd['prov'] == province}
    seat = next((sd for sd in prov_s.values() if sd['seat']), None)
    if not seat:
        return False
    seat_ctrl = seat['ctrl']
    return any(sd['ctrl'] != seat_ctrl for sd in prov_s.values())

def fragmentation_check(settlements: dict, province: str, faction_influence: dict, rng) -> str:
    """Ob = 2 + (non-Seat-held settlements count). Pool = Seat-holder Influence."""
    prov_s = {sid: sd for sid, sd in settlements.items() if sd['prov'] == province}
    seat = next((sd for sd in prov_s.values() if sd['seat']), None)
    if not seat:
        return "N/A"
    seat_ctrl = seat['ctrl']
    non_seat_alien = sum(1 for sd in prov_s.values()
                         if not sd['seat'] and sd['ctrl'] != seat_ctrl)
    ob = 2 + non_seat_alien
    pool = faction_influence.get(seat_ctrl, 2)
    return roll(pool, ob, rng)

def consolidation_available(settlements: dict, province: str, faction: str) -> bool:
    """Returns True if faction holds ≥ 75% of province PV."""
    shares = compute_pv_shares(settlements, province)
    total = sum(shares.values()) or 1
    return (shares.get(faction, 0) / total) >= 0.75

# ─── SUCCESSION CONTEST ───────────────────────────────────────────────────────

@dataclass
class Contender:
    name: str
    claim_type: str  # blood / institutional / external
    pool: int
    disposition: int  # toward faction apparatus

def succession_contest(contenders: list, rng) -> tuple:
    """
    Returns (winner_name, runner_up_name, margin, outcome_type).
    outcome_type: 'clear' / 'narrow' / 'none'
    """
    results = {}
    for c in contenders:
        outcome = roll(c.pool, 3, rng)
        net = {"Overwhelming": 3, "Success": 2, "Partial": 1, "Failure": 0}[outcome]
        results[c.name] = (net, c)
    ranked = sorted(results.items(), key=lambda x: -x[1][0])
    if len(ranked) < 2:
        winner = ranked[0]
        return (winner[0], None, winner[1][0], 'clear')
    first_name, (first_net, first_c) = ranked[0]
    second_name, (second_net, _) = ranked[1]
    margin = first_net - second_net
    if first_net == 0 and second_net == 0:
        return (None, None, 0, 'none')
    if margin >= 2:
        return (first_name, second_name, margin, 'clear')
    else:
        return (first_name, second_name, margin, 'narrow')

# ─── RM EMERGENCE ─────────────────────────────────────────────────────────────

def check_rm_settlement_emergence(settlements: dict, rm_presence: dict, rng) -> list:
    """
    Per faction_succession_split §4: if settlement Order=0, PT≤1, Disposition≥+3 toward Yrsa Vossen.
    Simplified: PT proxied by (3 - settlement O) for Varfell/fractional settlements.
    Disposition toward RM proxied by Varfell settlements with O≤1.
    Returns list of settlements where RM emerges.
    """
    emerged = []
    prov_cooldown = rm_presence.get('_cooldown', {})
    for sid, sd in settlements.items():
        if sd['ctrl'] in ('Varfell', 'Eastern Varfell') and sd['O'] <= 1:
            prov = sd['prov']
            if prov_cooldown.get(prov, 0) > 0:
                continue
            # Simulated: if Order is 0 and province is not Church-held, RM can emerge
            if sd['O'] == 0 or (sd['O'] <= 1 and sd['stype'] in ('Outpost', 'Town')):
                emerged.append(sid)
                prov_cooldown[prov] = 4  # 4-season cooldown
    rm_presence['_cooldown'] = prov_cooldown
    return emerged

# ─── SCENARIO ENGINE ──────────────────────────────────────────────────────────

class ArcLog:
    def __init__(self):
        self.events = []

    def log(self, season: int, actor: str, event: str, detail: str = ""):
        self.events.append({"season": season, "actor": actor, "event": event, "detail": detail})

    def print_arc(self):
        for e in self.events:
            detail = f" — {e['detail']}" if e['detail'] else ""
            print(f"  S{e['season']:02d} [{e['actor']}] {e['event']}{detail}")


def run_scenario(name: str, setup_fn, seasons: int = 20, seed: int = 42) -> dict:
    """Run a scenario and return arc events + outcome."""
    rng = random.Random(seed)
    settlements = deepcopy(SETTLEMENTS)
    faction_influence = {"Crown": 5, "Hafenmark": 5, "Varfell": 4, "Church": 4,
                         "RM": 2, "Eastern Varfell": 2}
    faction_mandate = {"Crown": 4, "Hafenmark": 4, "Varfell": 4, "Church": 3}
    leaders = {"Varfell": "Vaynard", "Crown": "Almud", "Hafenmark": "Baralta",
               "Church": "Confessor"}
    rm_presence = {"settlements": [], "_cooldown": {}}
    splinters = {}  # faction_name: dict with leader, mandate, etc.
    log = ArcLog()

    # Setup function modifies initial state
    setup_fn(settlements, faction_influence, faction_mandate, leaders, log)

    for season in range(1, seasons + 1):
        # ── FRAGMENTATION CHECKS for all fractional provinces ──
        provinces_checked = set()
        for sid, sd in settlements.items():
            prov = sd['prov']
            if prov in provinces_checked:
                continue
            if is_fractional(settlements, prov):
                provinces_checked.add(prov)
                result = fragmentation_check(settlements, prov, faction_influence, rng)
                shares = compute_pv_shares(settlements, prov)
                prov_s = {s: d for s, d in settlements.items() if d['prov'] == prov}
                seat_ctrl = next(d['ctrl'] for d in prov_s.values() if d['seat'])
                if result == "Failure":
                    # Secession: pick a non-Seat-held settlement for secession
                    secession_candidates = [s for s, d in prov_s.items()
                                            if not d['seat'] and d['ctrl'] != seat_ctrl]
                    if secession_candidates:
                        target = rng.choice(secession_candidates)
                        old_ctrl = settlements[target]['ctrl']
                        settlements[target]['ctrl'] = "RM"  # Secession → RM or subnational
                        rm_presence['settlements'].append(target)
                        log.log(season, "Fragmentation", "Secession",
                                f"{settlements[target]['name']} ({prov}) → RM (from {old_ctrl})")
                elif result == "Partial":
                    # Order drop in non-Seat-held settlement
                    alien = [s for s, d in prov_s.items()
                             if not d['seat'] and d['ctrl'] != seat_ctrl]
                    if alien:
                        target = rng.choice(alien)
                        settlements[target]['O'] = max(0, settlements[target]['O'] - 1)
                        log.log(season, "Fragmentation", "Order drop",
                                f"{settlements[target]['name']} O→{settlements[target]['O']}")

        # ── CONSOLIDATION CHECKS ──
        for prov in PROVINCE_BASE_PV:
            prov_s = {s: d for s, d in settlements.items() if d['prov'] == prov}
            if not prov_s:
                continue
            seat_ctrl = next((d['ctrl'] for d in prov_s.values() if d['seat']), None)
            if seat_ctrl and consolidation_available(settlements, prov, seat_ctrl):
                alien = [s for s, d in prov_s.items()
                         if not d['seat'] and d['ctrl'] != seat_ctrl]
                if alien:
                    # Resolve consolidation: each alien settlement chooses Submit/Resist
                    for asid in alien:
                        # Simplified: resist if alien faction's mandate is high
                        alien_ctrl = settlements[asid]['ctrl']
                        resist_pool = faction_mandate.get(alien_ctrl, 1)
                        resist = rng.randint(1, 6) <= resist_pool  # higher mandate = more likely resist
                        if not resist:
                            old_ctrl = settlements[asid]['ctrl']
                            settlements[asid]['ctrl'] = seat_ctrl
                            settlements[asid]['O'] = max(0, settlements[asid]['O'] - 2)
                            log.log(season, "Consolidation", "Submit",
                                    f"{settlements[asid]['name']} → {seat_ctrl} (O−2)")
                        else:
                            log.log(season, "Consolidation", "Resist — siege next season",
                                    f"{settlements[asid]['name']} resists {seat_ctrl}")

        # ── RM EMERGENCE ──
        if season % 2 == 0:  # check every 2 seasons
            emerged = check_rm_settlement_emergence(settlements, rm_presence, rng)
            for esid in emerged:
                if settlements[esid]['ctrl'] != 'RM':
                    old = settlements[esid]['ctrl']
                    settlements[esid]['ctrl'] = 'RM'
                    rm_presence['settlements'].append(esid)
                    faction_influence['RM'] = faction_influence.get('RM', 0) + 1
                    log.log(season, "RM", "Settlement Emergence",
                            f"{settlements[esid]['name']} (was {old}) — RM Influence→{faction_influence['RM']}")

        # ── SUCCESSION CHECK (fires on season-specific trigger from setup) ──
        for faction, trigger_season in getattr(run_scenario, '_triggers', {}).get(name, {}).items():
            if season == trigger_season and leaders.get(faction):
                log.log(season, faction, "Leader eliminated", f"{leaders[faction]} falls")
                leaders[faction] = None
                # Build contenders based on faction
                if faction == "Varfell":
                    contenders = [
                        Contender("Maret Uln",       "blood",         pool=7,  disposition=2),
                        Contender("Tribune Captain",  "institutional", pool=9,  disposition=4),
                        Contender("RM-candidate",     "external",      pool=max(3, faction_influence.get('RM', 2) + 2), disposition=0),
                    ]
                elif faction == "Crown":
                    contenders = [
                        Contender("Baralta's Claim",  "external",      pool=7,  disposition=-1),
                        Contender("Regency Council",  "institutional", pool=5,  disposition=2),
                    ]
                else:
                    contenders = [
                        Contender("Heir A", "blood",         pool=6, disposition=2),
                        Contender("Heir B", "institutional", pool=5, disposition=1),
                    ]
                winner, runner_up, margin, outcome_type = succession_contest(contenders, rng)
                if outcome_type == 'none':
                    log.log(season, faction, "Succession: Regency",
                            "No contender succeeded — regency opens")
                    leaders[faction] = "Regency"
                elif outcome_type == 'clear':
                    log.log(season, faction, f"Succession: Clear → {winner}",
                            f"margin {margin} over {runner_up}")
                    leaders[faction] = winner
                    faction_mandate[faction] = max(1, faction_mandate.get(faction, 3) - 1)
                else:
                    # FACTION SPLIT
                    log.log(season, faction, f"Succession: SPLIT — {winner} vs {runner_up}",
                            f"margin {margin} — faction fractures")
                    leaders[faction] = winner
                    splinter_name = f"Eastern {faction}" if faction == "Varfell" else f"{runner_up}'s {faction}"
                    # Asset split: geographic (simplified — runner-up takes non-capital provinces)
                    faction_provinces = list(set(sd['prov'] for sd in settlements.values()
                                                 if sd['ctrl'] == faction))
                    # Capital province (province of the Seat)
                    cap_prov = next((sd['prov'] for sd in settlements.values()
                                     if sd['ctrl'] == faction and sd['seat'] and
                                     sd['prov'] in faction_provinces), None)
                    splinter_provs = [p for p in faction_provinces if p != cap_prov]
                    # Transfer splinter provinces
                    for sprov in splinter_provs:
                        for sid2 in settlements:
                            if settlements[sid2]['prov'] == sprov and settlements[sid2]['ctrl'] == faction:
                                settlements[sid2]['ctrl'] = splinter_name
                    # Stat split
                    old_m = faction_mandate.get(faction, 3)
                    splinters[splinter_name] = {
                        'leader': runner_up,
                        'mandate': int(old_m * 0.4),
                        'influence': faction_influence.get(faction, 3),
                        'provinces': splinter_provs,
                    }
                    faction_mandate[faction] = int(old_m * 0.6)
                    faction_influence[splinter_name] = faction_influence.get(faction, 3)
                    log.log(season, splinter_name, "Splinter established",
                            f"provinces: {splinter_provs}, mandate: {splinters[splinter_name]['mandate']}")
                    # RM gets partial advantage from RM-candidate partial success (if applicable)
                    rm_candidate = next((c for c in contenders if 'RM' in c.name), None)
                    if rm_candidate:
                        faction_influence['RM'] = faction_influence.get('RM', 0) + 1
                        log.log(season, "RM", "Political momentum from succession",
                                f"Influence→{faction_influence['RM']}")

    # ── FINAL STATE ──
    pv_totals = {}
    for prov in PROVINCE_BASE_PV:
        shares = compute_pv_shares(settlements, prov)
        for ctrl, pv in shares.items():
            pv_totals[ctrl] = round(pv_totals.get(ctrl, 0) + pv, 2)

    rm_settlement_count = sum(1 for sd in settlements.values() if sd['ctrl'] == 'RM')

    return {
        "scenario": name,
        "log": log,
        "pv_totals": pv_totals,
        "rm_settlements": rm_settlement_count,
        "rm_influence": faction_influence.get('RM', 0),
        "splinters": splinters,
        "leaders": leaders,
        "faction_mandate": faction_mandate,
    }

# Attach scenario-specific succession triggers to function
run_scenario._triggers = {}

# ─── SCENARIOS ────────────────────────────────────────────────────────────────

def scenario_1_setup(settlements, faction_influence, faction_mandate, leaders, log):
    """
    Arc 1: Varfell partial capture of Hafenmark (Gransol) via settlement-granular invasion.
    Varfell army moves from T12 → T11 → T8 (three edges: Sigurdshelm → Halvardshelm → Gransol Seat).
    Captures S017 Gransol Market Quarter from Guilds but cannot take Seat S015.
    Province fractionalizes.
    """
    # Varfell seizes S017 at season 0 (setup)
    settlements['S017']['ctrl'] = 'Varfell'
    log.log(0, "Varfell", "Captures S017 Gransol Market Quarter (via road edge T12→T11→T8)",
            "province T8 now fractional")

def scenario_2_setup(settlements, faction_influence, faction_mandate, leaders, log):
    """
    Arc 2: Varfell succession crisis while holding fractional T8.
    Vaynard dies season 8. Varfell already holds S017 (Market Quarter) in Hafenmark T8.
    Tests succession split compounding with already-fractional province.
    """
    settlements['S017']['ctrl'] = 'Varfell'
    log.log(0, "Varfell", "Captures S017 Gransol Market Quarter", "T8 fractional from start")
    run_scenario._triggers.setdefault("Arc 2: Succession during fractional hold", {})
    run_scenario._triggers["Arc 2: Succession during fractional hold"]["Varfell"] = 8

def scenario_3_setup(settlements, faction_influence, faction_mandate, leaders, log):
    """
    Arc 3: RM emergence cascade.
    Varfell succession split happens S5, leaving Eastern Varfell with T11+T13.
    RM already has footholds (S029, S032). Low-Order Eastern Varfell settlements
    create emergence windows.
    """
    # Degrade Eastern Varfell settlement Order to create RM emergence windows
    settlements['S030']['O'] = 1  # Halvardshelm low Order
    settlements['S031']['O'] = 1  # Oastad low Order
    run_scenario._triggers.setdefault("Arc 3: RM cascade from Eastern Varfell collapse", {})
    run_scenario._triggers["Arc 3: RM cascade from Eastern Varfell collapse"]["Varfell"] = 5

def scenario_4_setup(settlements, faction_influence, faction_mandate, leaders, log):
    """
    Arc 4: All three mechanics interacting.
    - Varfell captures S017 (adjacency mechanic → partial capture → fractionalization)
    - Vaynard dies S10 → succession contest → narrow win → faction split
    - Eastern Varfell inherits fractional T8 stake (asset split compounds fractionalization)
    - RM emerges in deteriorated Eastern Varfell settlements
    """
    settlements['S017']['ctrl'] = 'Varfell'
    settlements['S030']['O'] = 1
    settlements['S031']['O'] = 1
    log.log(0, "Varfell", "Captures S017 Gransol Market Quarter", "T8 fractional")
    run_scenario._triggers.setdefault("Arc 4: Full interaction test", {})
    run_scenario._triggers["Arc 4: Full interaction test"]["Varfell"] = 10

SCENARIOS = [
    ("Arc 1: Partial capture → fractionalization", scenario_1_setup),
    ("Arc 2: Succession during fractional hold", scenario_2_setup),
    ("Arc 3: RM cascade from Eastern Varfell collapse", scenario_3_setup),
    ("Arc 4: Full interaction test", scenario_4_setup),
]

# ─── RUN & REPORT ─────────────────────────────────────────────────────────────

if __name__ == "__main__":
    results = []
    for name, setup in SCENARIOS:
        # Each scenario runs 3 seeds
        for seed in [42, 99, 137]:
            r = run_scenario(name, setup, seasons=16, seed=seed)
            results.append((name, seed, r))

    print("=" * 70)
    print("VALORIA — PROVISIONAL MECHANICS ARC TEST")
    print("Systems under test: settlement_adjacency_v30, fractional_province_ownership_v30,")
    print("                    faction_succession_split_v30")
    print("=" * 70)

    arc_summaries = {}
    for name, seed, r in results:
        arc_summaries.setdefault(name, []).append((seed, r))

    for arc_name, runs in arc_summaries.items():
        print(f"\n{'─'*70}")
        print(f"SCENARIO: {arc_name}")
        print(f"{'─'*70}")

        # Representative run (seed 42) — full event log
        rep_seed, rep = next((s, r) for s, r in runs if s == 42)
        print(f"\nEvent Log (seed 42, 16 seasons):")
        rep['log'].print_arc()

        print(f"\nOutcomes across 3 seeds (42, 99, 137):")
        for seed, r in runs:
            splinter_str = f", splinters: {list(r['splinters'].keys())}" if r['splinters'] else ""
            print(f"  seed={seed:3d} | PV: {dict((k,v) for k,v in sorted(r['pv_totals'].items(), key=lambda x:-x[1]) if v > 0.1)} | RM settlements: {r['rm_settlements']} RM inf: {r['rm_influence']}{splinter_str}")

    print("\n" + "=" * 70)
    print("GAP FLAGS SURFACED BY SIMULATION")
    print("=" * 70)
    gaps = [
        "[GAP: settlement_adjacency — inter-province edge classification not in canonical map file yet (settlement_adjacency_map.yaml not authored); mountain/river edges approximated from geography_v30 notes]",
        "[GAP: fractional_province_ownership — PV base values for provinces not in canonical source; approximated from settlement count + political importance; needs geography_v30 explicit PV table]",
        "[GAP: faction_succession_split — Varfell contender pools (Maret Uln, Tribune Captain) have no canonical stat values in npc_character_analyses_v30; pools estimated from workplan §3 example]",
        "[GAP: RM settlement emergence — Disposition toward Yrsa Vossen not tracked at settlement level in current state; proxied by Order ≤ 1 in Varfell-controlled settlements]",
        "[GAP: consolidation action — Ob formula uses (remaining non-faction PV share × 2) but Influence pool source per faction not specified in fractional_province_ownership_v30]",
        "[GAP: splinter province assignment — 'proximity through settlement adjacency graph' rule in §2.4 requires settlement adjacency map to be canonical; currently approximated as 'non-capital provinces to runner-up']",
    ]
    for g in gaps:
        print(f"  {g}")
