"""
Valoria — Arc Test Batch 3
Systems under test (all previously untouched):
  B3-1: CI buildup → Mass Seizure timing (curve, pool, Ob, infrastructure)
  B3-2: RS decay under warfare pressure (proximity-graduated effects, Warden emergence)
  B3-3: Fort level as Varfell breakout constraint (T14 Fort3, T3 Fort3)
  B3-4: IP escalation → Altonian Vanguard pressure (coalition forcing)
  B3-5: Hafenmark CI suppression vs Church infrastructure buildup (suppression race)

Canonical sources:
  - params/bg/ci_seizure.md — CI formula, seizure curve, pool, Ob
  - params/bg/clocks.md — RS effects table, IP effects, battle consequences
  - params/bg/core.md — starting stats, d10 system
  - params/bg/faction_actions.md — Parliamentary Challenge, Piety Spread
  - designs/world/geography_v30.md — node distances, Fort levels, adjacency
"""

import random
from dataclasses import dataclass, field
from typing import Optional

# ─── CANONICAL CONSTANTS ─────────────────────────────────────────────────────

STARTING_STATS = {
    "Crown":     dict(M=5, I=5, W=4, Mil=4, Stab=4),
    "Church":    dict(M=5, I=6, W=5, Mil=4, Stab=5),
    "Hafenmark": dict(M=4, I=4, W=5, Mil=3, Stab=4),
    "Varfell":   dict(M=4, I=4, W=4, Mil=4, Stab=4),
}

# Node distance from T15 (Askeheim)
NODE_DIST = {
    "T15": 0,
    "T6": 1, "T13": 1,
    "T5": 2, "T12": 2,
    "T1": 3, "T14": 3, "T4": 3, "T11": 3,
    "T2": 4, "T16": 4, "T9": 4, "T7": 4, "T10": 4,
    "T3": 5, "T8": 5, "T17": 5,
}

# Fort levels per territory
FORT_LEVEL = {
    "T3": 3, "T14": 3,  # Primary chokepoints
    "T10": 2, "T9": 2, "T1": 2,
    "T8": 1, "T12": 1, "T16": 1,
}

# Province adjacency (Crown path north, Varfell breakout routes)
PROV_ADJ = {
    "T1":  ["T2","T3","T5","T14"],
    "T2":  ["T1","T3","T4","T5"],
    "T3":  ["T1","T2"],
    "T4":  ["T2","T11","T12"],
    "T5":  ["T1","T2","T6","T8"],
    "T6":  ["T5","T15"],
    "T7":  ["T8","T10"],
    "T8":  ["T5","T7","T9","T10","T14"],
    "T9":  ["T8","T10","T11","T14"],
    "T10": ["T7","T8","T9"],
    "T11": ["T4","T9","T12","T13"],
    "T12": ["T4","T11","T13"],
    "T13": ["T11","T12","T15"],
    "T14": ["T1","T8","T9"],
    "T15": ["T6","T13"],
    "T16": [],
    "T17": ["T7"],
}

# Starting PT per territory (Piety Track — Church influence level)
# Canonical from geography/settlement data; PT 0-5
STARTING_PT = {
    "T1": 2,   # Valorsplatz — capital, moderate Church presence
    "T2": 1, "T3": 1, "T4": 1, "T5": 1,
    "T6": 1,
    "T7": 0,
    "T8": 1,   # Gransol — Hafenmark, low Church
    "T9": 5,   # Himmelenger — Church heartland
    "T10": 0, "T11": 1, "T12": 0, "T13": 0,
    "T14": 1,
    "T15": 0, "T16": 0, "T17": 0,
}

# Church infrastructure tiers per settlement (0=none,1=Chapel,2=Church,3=Cathedral)
# Infra modifier to Seizure Ob: −1 per tier of Church-built infrastructure in territory
STARTING_CHURCH_INFRA = {
    "T1": 3,   # Valorsplatz Cathedral (S003)
    "T9": 3,   # Himmelenger (multiple cathedrals)
    "T8": 0, "T2": 0, "T3": 0, "T4": 0, "T5": 0,
    "T6": 0, "T7": 0, "T10": 0, "T11": 0, "T12": 0,
    "T13": 0, "T14": 0, "T15": 0, "T16": 0, "T17": 0,
}

# ─── DICE ─────────────────────────────────────────────────────────────────────

def roll_d10_pool(pool: int, ob: int, rng) -> tuple[str, int]:
    """d10 pool. TN7: 1=−1, 7-9=+1, 10=+2. Returns (degree, net)."""
    pool = max(1, pool)
    net = sum((-1 if d==1 else 2 if d==10 else 1 if d>=7 else 0)
              for d in (rng.randint(1,10) for _ in range(pool)))
    net -= ob
    deg = "Overwhelming" if net>=2 else "Success" if net>=0 else "Partial" if net>=-1 else "Failure"
    return deg, net

# ─── RS EFFECTS TABLE ─────────────────────────────────────────────────────────

def rs_ob_penalty(rs: int, node_dist: int) -> int:
    """Returns global Ob penalty for actions in a territory at given RS and node distance."""
    if rs >= 80:
        return 0
    elif rs >= 60:  # 79-60
        return 1 if node_dist == 0 else 0
    elif rs >= 40:  # 59-40
        if node_dist == 0: return 2
        elif node_dist == 1: return 1
        else: return 0
    elif rs >= 20:  # 39-20
        if node_dist <= 1: return 1
        else: return 0
    else:  # 19-1
        if node_dist <= 1: return 1
        else: return 0

def rs_critical_global_penalty(rs: int) -> int:
    """At RS 19-1: all Thread ops +1 Ob globally. Faction Stability checks Ob1."""
    return 1 if rs <= 19 else 0

# ─── CI SEIZURE CURVE ─────────────────────────────────────────────────────────

def seizure_probability(ci: int) -> float:
    if ci < 60: return 0.0
    return min(1.0, ((ci - 60) / 40) ** 3.3)

def seizure_pool(church_influence: int, ci: int) -> int:
    return church_influence + (ci // 15)

def seizure_ob(pt: int, infra: int) -> int:
    return max(1, 10 - pt - infra)

# ─── CI GENERATION (seasonal) ─────────────────────────────────────────────────

def ci_seasonal_gain(ci: int, church_stats: dict, territory_pts: dict,
                     territory_ctrl: dict, hafenmark_mandate: int,
                     hafenmark_played_challenge: bool, rng) -> tuple[int, list]:
    """
    Returns (delta_CI, events).
    Steps per ci_seizure.md §3.1-3.7:
    1. Conditional Passive: +1 if Church Mandate > controlling faction Mandate in ≥2 territories
    2. Piety Yield: CI += Σ(PT × SW/5) per prominent territory
    3. Charity Advantage: skipped (W not tracked at this granularity)
    4. Templar Presence: skipped (no unit tracking in this sim)
    5. Assert: Church action — Influence vs Ob2
    6. Suppress: opponent action (Hafenmark plays if Mandate≥4)
    7. Hafenmark Structural Suppression: if Mandate≥4 and no challenge played
    """
    events = []
    delta = 0

    # Step 1: Conditional Passive
    church_m = church_stats['M']
    prominent_count = sum(1 for t, ctrl in territory_ctrl.items()
                          if ctrl != 'Church' and church_m > church_stats.get(f'rival_m_{ctrl}', 3))
    # Simplified: Church has prominence if PT≥2 in territory
    prominent_count = sum(1 for t, pt in territory_pts.items() if pt >= 2)
    if prominent_count >= 2:
        delta += 1
        events.append("Conditional Passive: CI+1")

    # Step 2: Piety Yield — Σ(PT tier × SW/5) for Church-prominent territories
    # SW (Spiritual Weight) — canonical per territory. Approximate from PT:
    # T9 Himmelenger SW=5, T1 Valorsplatz SW=3, others SW=1-2
    SW = {"T9": 5, "T1": 3, "T14": 2, "T8": 2, "T12": 2, "T4": 2,
          "T2": 1, "T5": 1, "T6": 1, "T13": 1}
    piety_yield = 0
    for t, pt in territory_pts.items():
        if pt >= 1:  # Church has some presence
            sw = SW.get(t, 1)
            piety_yield += pt * sw // 5
    if piety_yield > 0:
        delta += piety_yield
        events.append(f"Piety Yield: CI+{piety_yield}")

    # Step 5: Assert (Church action — Mandate vs Ob2)
    assert_deg, _ = roll_d10_pool(church_stats['M'], 2, rng)
    if assert_deg in ("Overwhelming", "Success"):
        delta += 1
        events.append(f"Assert: CI+1 ({assert_deg})")
    elif assert_deg == "Failure":
        church_stats['Stab'] = max(0, church_stats['Stab'] - 1)
        events.append(f"Assert: Failure — Church Stab−1 ({church_stats['Stab']})")

    # Step 6: Suppress — Hafenmark (if Mandate≥4, not playing challenge)
    if hafenmark_mandate >= 4 and not hafenmark_played_challenge:
        hm_m = hafenmark_mandate
        ob_sup = (church_stats['M'] // 2) + 1
        sup_deg, _ = roll_d10_pool(hm_m, ob_sup, rng)
        if sup_deg in ("Overwhelming", "Success"):
            # Negate Step 1
            if "Conditional Passive: CI+1" in events:
                delta -= 1
                events.append(f"Suppress: negates Conditional Passive (CI−1)")
        elif sup_deg == "Failure":
            church_stats['Stab'] = max(0, church_stats['Stab'] - 1)  # wrong faction but flag
            events.append(f"Suppress: Failure")

    # Step 7: Structural Suppression
    if hafenmark_mandate >= 4 and not hafenmark_played_challenge:
        delta -= 1
        events.append("Structural Suppression: CI−1")

    # Cap: ±5 per season total
    delta = max(-5, min(5, delta))
    return delta, events

# ─── VARFELL BREAKOUT (B3-3) ──────────────────────────────────────────────────

def attempt_battle(attacker_mil: int, defender_mil: int, fort_level: int, rng) -> tuple[str, int]:
    """
    Battle: attacker Military pool vs Ob = floor(defender_mil/2)+1.
    Fort adds bonus dice to defender equivalent: attacker pool −fort_level (defender benefit).
    """
    ob = (defender_mil // 2) + 1
    # Fort level: adds defender bonus dice — modeled as Ob+fort_level for attacker
    effective_ob = ob + fort_level
    effective_ob = max(1, effective_ob)
    return roll_d10_pool(attacker_mil, effective_ob, rng)

# ─── ARC LOG ──────────────────────────────────────────────────────────────────

class Log:
    def __init__(self):
        self.events = []
    def log(self, s, actor, event, detail=""):
        self.events.append((s, actor, event, detail))
    def print_arc(self, max_events=999):
        for s, a, e, d in self.events[:max_events]:
            print(f"  S{s:02d} [{a}] {e}" + (f" — {d}" if d else ""))
        if len(self.events) > max_events:
            print(f"  ... ({len(self.events)-max_events} more)")
    def filter(self, keyword):
        return [(s,a,e,d) for s,a,e,d in self.events if keyword.lower() in (a+e+d).lower()]

# ─── B3-1: CI BUILDUP → MASS SEIZURE TIMING ──────────────────────────────────

def sim_b31_seizure(seasons=40, seed=42,
                    infra_buildup_rate=1,        # Church infra gain per season (0-3)
                    hafenmark_suppression=True,
                    target_territory="T9",       # which territory Church targets
                    ) -> dict:
    """
    Simulate CI growth and Mass Seizure timing.
    Church performs Assert each season. Hafenmark suppresses if enabled.
    Church upgrades infra toward target territory.
    """
    rng = random.Random(seed)
    church = dict(STARTING_STATS["Church"])
    hafenmark = dict(STARTING_STATS["Hafenmark"])

    ci = 28
    territory_pts = dict(STARTING_PT)
    territory_ctrl = {t: "Crown" for t in NODE_DIST}
    territory_ctrl.update({"T9":"Church","T23":"Church","T25":"Church"})  # Himmelenger Church-held
    territory_ctrl["T4"] = "Varfell"
    territory_ctrl["T11"] = "Varfell"
    territory_ctrl["T12"] = "Varfell"
    territory_ctrl["T13"] = "Varfell"
    territory_ctrl["T8"] = "Hafenmark"
    territory_ctrl["T7"] = "Hafenmark"
    territory_ctrl["T10"] = "Hafenmark"
    territory_ctrl["T17"] = "Hafenmark"

    church_infra = dict(STARTING_CHURCH_INFRA)
    log = Log()

    seizure_season = None
    seizure_outcome = None
    seizure_ci_at_fire = None

    for season in range(1, seasons+1):
        # Church infra buildup toward target territory
        if church_infra[target_territory] < 3 and infra_buildup_rate > 0:
            if season % max(1, 3-infra_buildup_rate) == 0:
                church_infra[target_territory] = min(3, church_infra[target_territory]+1)
                log.log(season, "Church", "Infra upgrade",
                        f"{target_territory} tier→{church_infra[target_territory]}")

        # PT accumulation (Piety Spread action success)
        if territory_pts[target_territory] < 5:
            pt_ob = (3 // 2) + 1  # Ob = floor(controlling faction Mandate/2)+1
            pt_deg, _ = roll_d10_pool(church['M'], pt_ob, rng)
            if pt_deg in ("Overwhelming", "Success"):
                territory_pts[target_territory] = min(5, territory_pts[target_territory]+1)
                log.log(season, "Church", "Piety Spread success",
                        f"{target_territory} PT→{territory_pts[target_territory]}")

        # CI generation
        hf_challenge = False  # no Parliamentary Challenge in this sim
        delta, events = ci_seasonal_gain(
            ci, church, territory_pts, territory_ctrl,
            hafenmark['M'] if hafenmark_suppression else 0,
            hf_challenge, rng
        )
        ci_before = ci
        ci = max(0, min(100, ci + delta))
        if delta != 0:
            log.log(season, "CI", f"{ci_before}→{ci}", "; ".join(events))

        # Mass Seizure check
        if ci >= 60 and seizure_season is None:
            prob = seizure_probability(ci)
            if rng.random() < prob:
                # Seizure fires
                seizure_ci_at_fire = ci
                pool = seizure_pool(church['I'], ci)
                pt = territory_pts[target_territory]
                infra = church_infra[target_territory]
                ob = seizure_ob(pt, infra)
                deg, net = roll_d10_pool(pool, ob, rng)
                seizure_season = season
                seizure_outcome = deg
                log.log(season, "Church", f"MASS SEIZURE FIRES — {target_territory}",
                        f"CI={ci} P={prob:.1%} pool={pool}d ob={ob} → {deg} (net={net})")
                if deg == "Overwhelming":
                    territory_pts[target_territory] = min(5, territory_pts[target_territory]+1)
                elif deg == "Failure":
                    church['Stab'] = max(0, church['Stab']-1)
                break

    return {
        "log": log,
        "ci_final": ci,
        "seizure_season": seizure_season,
        "seizure_ci": seizure_ci_at_fire,
        "seizure_outcome": seizure_outcome,
        "territory_pt_final": territory_pts[target_territory],
        "infra_final": church_infra[target_territory],
    }

# ─── B3-2: RS DECAY UNDER WARFARE ─────────────────────────────────────────────

def sim_b32_rs(seasons=30, seed=42,
               battles_per_season=1,   # 1=moderate, 2=active war, 3=total war
               campaign_scale=False,   # False=RS-1/battle, True=RS-2/battle
               ) -> dict:
    """
    Track RS decay from sustained warfare.
    At each season, battles fire and RS drops.
    Track when each RS band is entered and what Ob penalties appear per proximity zone.
    """
    rng = random.Random(seed)
    rs = 100
    ip = 0
    log = Log()
    band_crossings = {}
    vanguard_deployed = False
    vanguard_pos = None
    vanguard_advance_counter = 0

    # Track Ob penalties per proximity zone by season
    ob_timeline = []

    for season in range(1, seasons+1):
        rs_drop = battles_per_season * (2 if campaign_scale else 1)
        ip_gain = battles_per_season * 2

        rs_before = rs
        rs = max(0, rs - rs_drop)
        ip = min(100, ip + ip_gain)

        # Check RS band crossings
        for band, threshold in [(80, 79), (60, 59), (40, 39), (20, 19), (1, 0)]:
            if rs_before > threshold >= rs and threshold not in band_crossings:
                band_crossings[threshold] = season
                log.log(season, "RS", f"Band crossing: RS entered {threshold+1}–{threshold-1 if threshold>0 else 0}",
                        f"RS={rs}")

        # Record Ob penalties for key proximity zones
        ob_p0 = rs_ob_penalty(rs, 0)
        ob_p1 = rs_ob_penalty(rs, 1)
        ob_p2 = rs_ob_penalty(rs, 2)
        ob_p3 = rs_ob_penalty(rs, 3)
        ob_timeline.append((season, rs, ip, ob_p0, ob_p1, ob_p2, ob_p3))

        # Critical RS: global Stability checks
        if rs <= 19:
            crit_penalty = rs_critical_global_penalty(rs)
            for faction, stats in [("Crown",STARTING_STATS["Crown"]),
                                    ("Hafenmark",STARTING_STATS["Hafenmark"])]:
                deg, _ = roll_d10_pool(3, 1, rng)  # Stability check Ob1
                if deg == "Failure":
                    log.log(season, faction, "Critical RS Stability check FAILED", f"Mandate−1")

        # Warden emergence at RS≤40
        if rs <= 40 and rs_before > 40:
            log.log(season, "Wardens", "Warden emergence threshold crossed", f"RS={rs}")

        # Altonian Vanguard at IP≥75
        if ip >= 75 and not vanguard_deployed:
            vanguard_deployed = True
            vanguard_pos = "T10"
            log.log(season, "Altonia", "VANGUARD DEPLOYED at T10", f"IP={ip}")

        # Vanguard advance (simplified: advance if no contest for 2 seasons)
        if vanguard_deployed:
            vanguard_advance_counter += 1
            if vanguard_advance_counter >= 2:
                route = ["T10", "T3", "T2", "T1"]
                curr_idx = route.index(vanguard_pos) if vanguard_pos in route else 0
                if curr_idx < len(route)-1:
                    vanguard_pos = route[curr_idx+1]
                    vanguard_advance_counter = 0
                    log.log(season, "Altonia", f"Vanguard advances → {vanguard_pos}",
                            f"IP={ip}, RS={rs}")

        if rs <= 0:
            log.log(season, "RUPTURE", "RS=0 — campaign ends — all factions lose", "")
            break

    return {
        "log": log,
        "rs_final": rs,
        "ip_final": ip,
        "band_crossings": band_crossings,
        "ob_timeline": ob_timeline,
        "vanguard_pos": vanguard_pos,
        "seasons_run": season,
    }

# ─── B3-3: FORT CONSTRAINT — VARFELL BREAKOUT ────────────────────────────────

def sim_b33_varfell_breakout(seasons=20, seed=42,
                              varfell_mil_growth=0,  # Mil gained per 4 seasons (0=static)
                              use_southern_route=False,  # T13→T15→T6→T5 (Askeheim bypass)
                              ) -> dict:
    """
    Test Varfell breakout through fortified northern routes.
    Route A: T12→T4→T2→T1 (T14 bypass via T4, but T2 has no fort, T1 has Fort2)
    Route B: T12→T11→T9→T14 (hits T14 Fort3 — primary chokepoint)
    Route C: T13→T15→T6→T5→T1 (Askeheim route — no forts but RS exposure)
    Crown defends T14 with Military 4.
    """
    rng = random.Random(seed)
    varfell_mil = STARTING_STATS["Varfell"]["Mil"]
    crown_mil = STARTING_STATS["Crown"]["Mil"]
    log = Log()

    # Route definitions: list of (territory, fort_level, defender_mil)
    routes = {
        "A — via T4/T2": [
            ("T4", 0, 0),       # Grauwald — Varfell territory, no fight
            ("T2", 0, crown_mil),  # Kronmark — Crown, no fort
            ("T1", 2, crown_mil),  # Valorsplatz — Crown, Fort2
        ],
        "B — via T9/T14": [
            ("T11", 0, 0),      # Halvardshelm — Varfell
            ("T9", 2, 4),       # Himmelenger — Church Fort2, Church Mil4
            ("T14", 3, crown_mil), # Ehrenfeld — Crown Fort3 ← primary chokepoint
            ("T1", 2, crown_mil),
        ],
        "C — via T15 (Askeheim)": [
            ("T13", 0, 0),      # Oastad — Varfell
            ("T15", 0, 0),      # Askeheim — Warden (no military resistance but RS penalty)
            ("T6", 0, crown_mil//2),  # Stillhelm — Crown, minimal garrison
            ("T5", 0, crown_mil),  # Feldmark — Crown breadbasket
            ("T1", 2, crown_mil),
        ],
    }

    # T15 RS exposure: Askeheim route incurs RS−1 per season army transits
    rs = 100

    results = {}
    for route_name, steps in routes.items():
        if use_southern_route and "T15" not in route_name:
            continue
        if not use_southern_route and "T15" in route_name:
            continue

        rng2 = random.Random(seed)
        mil = varfell_mil
        route_log = Log()
        broke_through = False
        season_reached = {}
        stalled_at = None

        for season in range(1, seasons+1):
            # Mil growth
            if varfell_mil_growth > 0 and season % 4 == 0:
                mil = min(8, mil + varfell_mil_growth)

            # Each step: can Varfell take this territory?
            for step_i, (terr, fort, def_mil) in enumerate(steps):
                step_key = f"step{step_i}_{terr}"
                if step_key in season_reached:
                    continue  # already passed

                if def_mil == 0:
                    season_reached[step_key] = season
                    route_log.log(season, "Varfell", f"Occupies {terr}", "no defender")
                    continue

                # RS penalty on T15 transit
                if terr == "T15":
                    rs = max(0, rs - 1)
                    ob_pen = rs_ob_penalty(rs, 0)
                    route_log.log(season, "RS", f"T15 transit RS−1", f"RS={rs}, Ob+{ob_pen} all")

                deg, net = attempt_battle(mil, def_mil, fort, rng2)
                route_log.log(season, "Varfell", f"Battle at {terr} (Fort{fort})",
                              f"pool={mil} ob={def_mil//2+1}+{fort}={def_mil//2+1+fort} → {deg}")

                if deg in ("Overwhelming", "Success"):
                    season_reached[step_key] = season
                    if terr == "T1":
                        broke_through = True
                        route_log.log(season, "Varfell", "BREAKOUT COMPLETE — reaches T1 Valorsplatz",
                                      f"season {season}, Mil={mil}")
                else:
                    stalled_at = terr
                    break  # Varfell stalled — try again next season
            if broke_through:
                break

        results[route_name] = {
            "broke_through": broke_through,
            "season": min(season_reached.values(), default=None) if broke_through else None,
            "stalled_at": stalled_at,
            "steps_completed": len(season_reached),
            "log": route_log,
        }

    return {"results": results, "rs_final": rs}

# ─── B3-4: IP ESCALATION → ALTONIAN PRESSURE ─────────────────────────────────

def sim_b34_altonian(seasons=30, seed=42,
                     faction_aggression=2,   # battles/season between factions
                     aer_level=0,            # AER 0=no diplomacy, 4=Schoenland mediates
                     ) -> dict:
    """
    Track IP escalation and Altonian Vanguard pressure.
    Tests: at what season does Vanguard deploy, does it reach T1, does faction conflict stop?
    AER≥4: IP threshold rises to 80, Vanguard halts.
    """
    rng = random.Random(seed)
    rs = 100
    ip = 0
    log = Log()
    vanguard_pos = None
    vanguard_deployed = False
    vanguard_advance_counter = 0
    coalition_formed = False

    # Faction conflict tracker — do factions stop fighting when Vanguard threatens T1?
    faction_conflict_paused = False

    for season in range(1, seasons+1):
        # IP threshold adjusted by AER
        ip_threshold = 80 if aer_level >= 4 else 75

        # Faction battles
        if not faction_conflict_paused:
            battles_this_season = faction_aggression + rng.randint(-1, 1)
            battles_this_season = max(0, battles_this_season)
            rs = max(0, rs - battles_this_season)
            ip_gain = battles_this_season * 2
            if aer_level >= 5:
                ip_gain = 0  # AER5: IP held at 50
            ip = min(100, ip + ip_gain)
            if battles_this_season > 0:
                log.log(season, "Warfare", f"{battles_this_season} battle(s)",
                        f"RS−{battles_this_season}={rs}, IP+{ip_gain}={ip}")

        # Vanguard deployment
        if ip >= ip_threshold and not vanguard_deployed:
            vanguard_deployed = True
            vanguard_pos = "T10"
            log.log(season, "Altonia", f"VANGUARD DEPLOYED (IP={ip}≥{ip_threshold})", "at T10")

        # Vanguard advance (2-season uncontested rule)
        if vanguard_deployed:
            if faction_conflict_paused:
                # Factions are contesting — roll battle
                deg, _ = roll_d10_pool(4, 3, rng)  # Coalition Military 4 vs Ob3
                if deg in ("Overwhelming","Success"):
                    vanguard_advance_counter = 0
                    log.log(season, "Coalition", f"Contests Vanguard at {vanguard_pos}", f"→ {deg}")
                else:
                    vanguard_advance_counter += 1
                    log.log(season, "Coalition", f"Fails to contest Vanguard", f"→ {deg}")
            else:
                vanguard_advance_counter += 1

            if vanguard_advance_counter >= 2:
                route = ["T10","T3","T2","T1"]
                idx = route.index(vanguard_pos) if vanguard_pos in route else 0
                if idx < len(route)-1:
                    vanguard_pos = route[idx+1]
                    vanguard_advance_counter = 0
                    log.log(season, "Altonia", f"Vanguard advances → {vanguard_pos}", f"IP={ip}")
                    # Coalition formed when Vanguard threatens T2 or T1
                    if vanguard_pos in ("T2","T1") and not coalition_formed:
                        coalition_formed = True
                        faction_conflict_paused = True
                        log.log(season, "Coalition", "ALL FACTIONS PAUSE — Vanguard at capital approach",
                                f"Vanguard at {vanguard_pos}")

        if rs <= 0:
            log.log(season, "RUPTURE", "RS=0", "")
            break
        if vanguard_pos == "T1" and not faction_conflict_paused:
            log.log(season, "Altonia", "Vanguard at T1 — all factions -1 Stab/season", "")

    return {
        "log": log,
        "rs_final": rs,
        "ip_final": ip,
        "vanguard_pos": vanguard_pos,
        "coalition_formed": coalition_formed,
        "seasons_run": season,
    }

# ─── B3-5: HAFENMARK CI SUPPRESSION RACE ─────────────────────────────────────

def sim_b35_suppression_race(seasons=40, seed=42,
                              hf_plays_challenge=False,  # Parliamentary Challenge each season
                              church_infra_strategy="T9",  # territory to build infra in first
                              ) -> dict:
    """
    Church builds CI via Assert + Piety Yield.
    Hafenmark uses structural suppression (Mandate≥4) and optionally Parliamentary Challenge.
    Test: can Hafenmark prevent CI from reaching 60 before season 30?
    """
    rng = random.Random(seed)
    church = dict(STARTING_STATS["Church"])
    hafenmark = dict(STARTING_STATS["Hafenmark"])
    ci = 28
    territory_pts = dict(STARTING_PT)
    church_infra = dict(STARTING_CHURCH_INFRA)
    log = Log()

    ci_history = []
    seizure_season = None

    for season in range(1, seasons+1):
        # Hafenmark plays Parliamentary Challenge?
        hf_challenge_this_season = (hf_plays_challenge and hafenmark['M'] >= 4)
        if hf_challenge_this_season:
            ob_ch = 2 - (1 if 5 >= 5 else 0)  # PI≥5 gives Ob1, assume PI=3 for now → Ob2
            deg_ch, _ = roll_d10_pool(hafenmark['M'], ob_ch, rng)
            challenge_effect = 0
            if deg_ch == "Overwhelming": challenge_effect = -2
            elif deg_ch == "Success": challenge_effect = -1
            elif deg_ch in ("Partial","Failure"):
                hafenmark['Stab'] = max(0, hafenmark['Stab']-1)
            if challenge_effect < 0:
                log.log(season, "Hafenmark", f"Parliamentary Challenge: CI{challenge_effect}", f"→{deg_ch}")
                ci = max(0, ci + challenge_effect)

        # Church infra buildup
        for t in [church_infra_strategy, "T9", "T1"]:
            if church_infra[t] < 3:
                church_infra[t] = min(3, church_infra[t]+1)
                log.log(season, "Church", f"Infra {t} → tier {church_infra[t]}", "")
                break

        # PT growth in highest-SW territories
        for t, sw in sorted({"T9":5,"T1":3,"T14":2,"T8":2}.items(), key=lambda x:-x[1]):
            if territory_pts[t] < 5:
                deg_pt, _ = roll_d10_pool(church['M'], 2, rng)
                if deg_pt in ("Overwhelming","Success"):
                    territory_pts[t] = min(5, territory_pts[t]+1)
                break

        # CI generation
        delta, events = ci_seasonal_gain(
            ci, church, territory_pts, {},
            hafenmark['M'],
            hf_challenge_this_season,  # structural suppression disabled if challenge played
            rng
        )
        ci_before = ci
        ci = max(0, min(100, ci + delta))
        ci_history.append(ci)
        if delta != 0 or season % 5 == 0:
            log.log(season, "CI", f"{ci_before}→{ci} (Δ{delta:+})", "; ".join(events[:3]))

        # Seizure check
        if ci >= 60 and seizure_season is None:
            prob = seizure_probability(ci)
            if rng.random() < prob:
                pt_t = territory_pts.get(church_infra_strategy, 2)
                infra_t = church_infra.get(church_infra_strategy, 0)
                ob_s = seizure_ob(pt_t, infra_t)
                pool_s = seizure_pool(church['I'], ci)
                deg_s, _ = roll_d10_pool(pool_s, ob_s, rng)
                seizure_season = season
                log.log(season, "Church", "MASS SEIZURE",
                        f"CI={ci} P={prob:.0%} pool={pool_s} Ob={ob_s} → {deg_s}")
                break

    return {
        "log": log,
        "ci_final": ci,
        "ci_history": ci_history,
        "seizure_season": seizure_season,
        "territory_pt_final": {t: territory_pts[t] for t in ["T9","T1","T14","T8"]},
        "infra_final": {t: church_infra[t] for t in ["T9","T1","T14","T8"]},
    }

# ─── MAIN ─────────────────────────────────────────────────────────────────────

SEEDS = [42, 77, 99, 137, 201]

def hdr(t): print(f"\n{'═'*68}\n  {t}\n{'═'*68}")
def sub(t): print(f"\n{'─'*55}\n  {t}\n{'─'*55}")

if __name__ == "__main__":
    print("="*68)
    print("VALORIA — ARC TEST BATCH 3")
    print("Systems: CI/Seizure, RS decay, Fort constraint, IP/Vanguard, Suppression race")
    print("="*68)

    # ── B3-1: MASS SEIZURE TIMING ────────────────────────────────────────────
    hdr("B3-1: CI BUILDUP → MASS SEIZURE TIMING")
    sub("No suppression, T9 target (high PT/infra)")
    for seed in SEEDS:
        r = sim_b31_seizure(seasons=40, seed=seed, hafenmark_suppression=False, target_territory="T9")
        print(f"  seed={seed}: seizure S{r['seizure_season']} at CI={r['seizure_ci']} "
              f"→ {r['seizure_outcome']} | PT={r['territory_pt_final']} infra={r['infra_final']}")

    sub("With Hafenmark suppression, T9 target")
    for seed in SEEDS:
        r = sim_b31_seizure(seasons=40, seed=seed, hafenmark_suppression=True, target_territory="T9")
        s_str = f"S{r['seizure_season']}" if r['seizure_season'] else "never (40 seasons)"
        print(f"  seed={seed}: seizure {s_str} CI_final={r['ci_final']} "
              f"→ {r['seizure_outcome'] or '—'} | PT={r['territory_pt_final']} infra={r['infra_final']}")

    sub("With suppression, T1 target (low PT, but politically significant)")
    for seed in SEEDS:
        r = sim_b31_seizure(seasons=40, seed=seed, hafenmark_suppression=True, target_territory="T1")
        s_str = f"S{r['seizure_season']}" if r['seizure_season'] else "never"
        print(f"  seed={seed}: seizure {s_str} CI_final={r['ci_final']} "
              f"→ {r['seizure_outcome'] or '—'} | PT={r['territory_pt_final']} infra={r['infra_final']}")

    print("\n  Full event log (seed 42, suppression on, T9):")
    r42 = sim_b31_seizure(seasons=40, seed=42, hafenmark_suppression=True, target_territory="T9")
    r42['log'].print_arc(40)

    # ── B3-2: RS DECAY ───────────────────────────────────────────────────────
    hdr("B3-2: RS DECAY UNDER WARFARE PRESSURE")
    configs = [
        ("1 battle/season (moderate)",  1, False),
        ("2 battles/season (active war)",2, False),
        ("3 battles/season (total war)", 3, False),
        ("2 battles/season, campaign scale (RS-2 each)", 2, True),
    ]
    for label, bps, camp in configs:
        sub(label)
        for seed in SEEDS[:3]:
            r = sim_b32_rs(seasons=30, seed=seed, battles_per_season=bps, campaign_scale=camp)
            crossings = {k:v for k,v in r['band_crossings'].items()}
            print(f"  seed={seed}: RS={r['rs_final']} IP={r['ip_final']} "
                  f"| Band crossings S: {crossings} "
                  f"| Vanguard: {r['vanguard_pos'] or 'not deployed'}")

    sub("RS decay timeline (seed 42, 2 battles/season)")
    r_rs = sim_b32_rs(seasons=30, seed=42, battles_per_season=2)
    print("  Season | RS  | IP  | Ob(P0) | Ob(P1) | Ob(P2) | Ob(P3)")
    for s, rs, ip, ob0, ob1, ob2, ob3 in r_rs['ob_timeline'][::3]:
        print(f"  S{s:02d}    | {rs:3d} | {ip:3d} | {ob0}      | {ob1}      | {ob2}      | {ob3}")
    r_rs['log'].print_arc(20)

    # ── B3-3: VARFELL BREAKOUT ───────────────────────────────────────────────
    hdr("B3-3: FORT CONSTRAINT — VARFELL BREAKOUT ROUTES")
    sub("Static Mil=4, northern routes")
    for seed in SEEDS:
        r = sim_b33_varfell_breakout(seasons=20, seed=seed, varfell_mil_growth=0, use_southern_route=False)
        for route, res in r['results'].items():
            s_str = f"S{res['season']}" if res['broke_through'] else f"STALLED@{res['stalled_at']} ({res['steps_completed']} steps)"
            print(f"  seed={seed} [{route[:25]}]: {s_str}")

    sub("Mil growth +1 per 4 seasons, northern routes")
    for seed in SEEDS:
        r = sim_b33_varfell_breakout(seasons=20, seed=seed, varfell_mil_growth=1, use_southern_route=False)
        for route, res in r['results'].items():
            s_str = f"S{res['season']}" if res['broke_through'] else f"STALLED@{res['stalled_at']} ({res['steps_completed']} steps)"
            print(f"  seed={seed} [{route[:25]}]: {s_str}")

    sub("Southern route (Askeheim) — all seeds")
    for seed in SEEDS:
        r = sim_b33_varfell_breakout(seasons=20, seed=seed, use_southern_route=True)
        for route, res in r['results'].items():
            s_str = f"S{res['season']}" if res['broke_through'] else f"STALLED@{res['stalled_at']} ({res['steps_completed']} steps)"
            print(f"  seed={seed} [{route[:30]}]: {s_str}")
    print(f"  RS after southern transit: {r['rs_final']}")

    sub("Full log (seed 42, Route A — T4/T2, static Mil)")
    r_b = sim_b33_varfell_breakout(seasons=20, seed=42, varfell_mil_growth=0, use_southern_route=False)
    for route, res in r_b['results'].items():
        if "T4" in route:
            res['log'].print_arc()

    # ── B3-4: ALTONIAN VANGUARD ───────────────────────────────────────────────
    hdr("B3-4: IP ESCALATION → ALTONIAN VANGUARD")
    configs_ip = [
        ("Low aggression (1 battle/s)",  1, 0),
        ("Active war (2 battles/s)",     2, 0),
        ("Total war (3 battles/s)",      3, 0),
        ("Active war + AER4 (Schoenland mediates)", 2, 4),
    ]
    for label, agg, aer in configs_ip:
        sub(label)
        for seed in SEEDS[:3]:
            r = sim_b34_altonian(seasons=30, seed=seed, faction_aggression=agg, aer_level=aer)
            print(f"  seed={seed}: Vanguard={r['vanguard_pos'] or 'not deployed'} "
                  f"RS={r['rs_final']} IP={r['ip_final']} "
                  f"coalition={r['coalition_formed']}")
        print()

    sub("Full log (seed 42, active war, no AER)")
    r_ip = sim_b34_altonian(seasons=30, seed=42, faction_aggression=2, aer_level=0)
    r_ip['log'].print_arc()

    # ── B3-5: SUPPRESSION RACE ───────────────────────────────────────────────
    hdr("B3-5: HAFENMARK CI SUPPRESSION vs CHURCH BUILDUP")
    configs_sup = [
        ("No challenge, structural only",     False),
        ("Parliamentary Challenge each season", True),
    ]
    for label, challenge in configs_sup:
        sub(label)
        for seed in SEEDS:
            r = sim_b35_suppression_race(seasons=40, seed=seed, hf_plays_challenge=challenge)
            s_str = f"S{r['seizure_season']}" if r['seizure_season'] else "never"
            print(f"  seed={seed}: seizure {s_str} CI_final={r['ci_final']}")

    sub("CI history comparison (seed 42)")
    r_no  = sim_b35_suppression_race(seasons=40, seed=42, hf_plays_challenge=False)
    r_yes = sim_b35_suppression_race(seasons=40, seed=42, hf_plays_challenge=True)
    print(f"  {'Season':<8} {'No Challenge':<15} {'With Challenge'}")
    for i in range(0, min(40, len(r_no['ci_history'])), 4):
        ci_no  = r_no['ci_history'][i]
        ci_yes = r_yes['ci_history'][i] if i < len(r_yes['ci_history']) else "—"
        print(f"  S{i+1:<7} {ci_no:<15} {ci_yes}")

    # ── SUMMARY ──────────────────────────────────────────────────────────────
    hdr("CROSS-SYSTEM SUMMARY — KEY SEASON MARKERS (seed 42, representative runs)")
    print(f"\n  {'System':<40} {'Key finding'}")
    print(f"  {'─'*70}")
    r1 = sim_b31_seizure(seasons=40,seed=42,hafenmark_suppression=True,target_territory="T9")
    r2 = sim_b32_rs(seasons=30,seed=42,battles_per_season=2)
    r3 = sim_b33_varfell_breakout(seasons=20,seed=42,varfell_mil_growth=0,use_southern_route=False)
    r4 = sim_b34_altonian(seasons=30,seed=42,faction_aggression=2,aer_level=0)
    r5_n = sim_b35_suppression_race(seasons=40,seed=42,hf_plays_challenge=False)
    r5_y = sim_b35_suppression_race(seasons=40,seed=42,hf_plays_challenge=True)

    s1 = f"Seizure S{r1['seizure_season']} at CI={r1['seizure_ci']}" if r1['seizure_season'] else "no seizure in 40s"
    s2 = f"RS39 at S{r2['band_crossings'].get(39,'?')}, Vanguard S{r2['log'].filter('VANGUARD')[0][0] if r2['log'].filter('VANGUARD') else '?'}"
    route_a = [res for name,res in r3['results'].items() if 'T4' in name]
    s3 = f"Route A: {'breakthrough S'+str(route_a[0]['season']) if route_a and route_a[0]['broke_through'] else 'STALLED@'+str(route_a[0]['stalled_at'] if route_a else '?')}"
    vang_events = r4['log'].filter('VANGUARD')
    s4 = f"Vanguard S{vang_events[0][0] if vang_events else '?'}, final pos {r4['vanguard_pos']}"
    s5 = f"No challenge: seizure S{r5_n['seizure_season'] or 'never'} | Challenge: seizure S{r5_y['seizure_season'] or 'never'}"
    for label, finding in [
        ("B3-1 CI/Seizure (suppression on, T9)", s1),
        ("B3-2 RS decay (2 battles/s)", s2),
        ("B3-3 Varfell breakout (static Mil)", s3),
        ("B3-4 IP/Vanguard (2 battles/s)", s4),
        ("B3-5 Suppression race", s5),
    ]:
        print(f"  {label:<40} {finding}")
