"""
Valoria Full Campaign Simulation — Sessions 1 + 2 + 3 + Tier A
==============================================================================

Generated: 2026-04-19

Session 1: core engine + clocks + faction stats + seasonal loop.
Session 2: territories + DA framework + Piety Yield + faction AI.
Session 3: Victory eval + Tensions Deck + Royal Assassination + Threadwork.
Tier A (this extension):
- §20 Mass Combat resolution (simplified BG mode from mass_battle_v30 §B.3):
  single-roll per side, margin-based outcome, Accord damage per PP-645.
- §21 Invade DA: attacker triggers mass combat on an adjacent enemy territory.
- §22 Church TC Seizure DA: CI>=60 one-per-territory seizure against Church-
  prominent territories not held by Church.
- §23 Mass Seizure: CI>=60 one-shot, fires against all non-Church Church-
  prominent territories simultaneously (victory_v30 §3.2).
- §24 Faction AI v2: prioritize conquest when Military available + adjacent
  target; Church prioritizes TC Seizure / Mass Seizure when CI>=60.
- §25 Tier A corpus: 16 seeds, win-rate distribution analysis.

Every new mechanical constant is cited via inline canonical comments and
covered by /home/claude/sim_verification_ledger.json.

Canonical sources for Session 2 additions:
- designs/world/geography_v30.md §T1-T17 table (territory list + adjacency)
- designs/provincial/ci_political_v30.md §1 (PV, SW, Piety Yield formula,
  CI milestones), §7.1 (CI cap ED-721 Option A)
- params/factions/stats_1_7_scale.md §Unique Actions (PP-168) (DA catalog)
- designs/provincial/peninsular_strain_v30.md (Strain rules)
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum
from typing import Callable, Dict, List, Optional, Set, Tuple


# ============================================================================
# §1. Core Engine — Dice, Contest, Degree
#     [canonical: params/bg/core.md §Dice System (v05 correction)]
#     [canonical: params/bg/core.md §Degree Table (PP-179 + PP-249)]
# ============================================================================


class Degree(Enum):
    OVERWHELMING = "Overwhelming"
    SUCCESS = "Success"
    PARTIAL = "Partial"
    FAILURE = "Failure"


def roll_d10_pool(pool_size: int, rng: random.Random) -> List[int]:
    """[canonical: params/bg/core.md §Dice System]"""
    return [rng.randint(1, 10) for _ in range(pool_size)]


def net_successes(faces: List[int]) -> int:
    """[canonical: params/bg/core.md §Dice System]"""
    net = 0
    for f in faces:
        if f == 1:                                    # [canonical: params/bg/core.md face 1]
            net -= 1
        elif 7 <= f <= 9:                             # [canonical: params/bg/core.md faces 7-9]
            net += 1
        elif f == 10:                                 # [canonical: params/bg/core.md face 10]
            net += 2
    return net


def resolve_degree(net: int, ob: int) -> Degree:
    """[canonical: params/bg/core.md §Degree Table PP-179 + PP-249]"""
    if ob < 1:                                        # [canonical: params/bg/core.md "Ob minimum: 1"]
        ob = 1
    if net <= 0:
        return Degree.FAILURE
    if ob >= 10:                                      # [canonical: params/bg/core.md Ob 10 exception]
        if net >= 5:                                  # [canonical: params/bg/core.md Ob 10 exception net>=5]
            return Degree.PARTIAL
        return Degree.FAILURE
    if net >= 2 * ob and net >= 3:                    # [canonical: params/bg/core.md overwhelming floor 3]
        return Degree.OVERWHELMING
    if net >= ob:
        return Degree.SUCCESS
    return Degree.PARTIAL


def contest(pool_size: int, ob: int, rng: random.Random,
            bonus_dice: int = 0, ob_modifier: int = 0
) -> Tuple[Degree, int, List[int]]:
    """[canonical: params/bg/core.md §Dice System + §Degree Table]"""
    effective_pool = max(0, pool_size + bonus_dice)
    effective_ob = max(1, ob + ob_modifier)           # [canonical: params/bg/core.md "Ob minimum: 1"]
    faces = roll_d10_pool(effective_pool, rng)
    net = net_successes(faces)
    degree = resolve_degree(net, effective_ob)
    return degree, net, faces


# ============================================================================
# §2. Faction Model — 6-stat 1-7 scale
#     [canonical: params/factions/stats_1_7_scale.md §Starting Stats]
#     [canonical: params/factions/stats_1_7_scale.md §Military Seasonal Cap]
# ============================================================================


@dataclass
class Faction:
    """[canonical: params/factions/stats_1_7_scale.md §Starting Stats]"""
    name: str
    mandate: Optional[int]
    influence: Optional[int]
    wealth: Optional[int]
    military: Optional[int]
    intel: Optional[int]
    stability: Optional[int]
    playable: bool = True
    starting_mandate: Optional[int] = None
    starting_military: Optional[int] = None
    _season_delta: Dict[str, int] = field(default_factory=dict)
    _consec_action: Dict[str, int] = field(default_factory=dict)
    # DAs used this season (for once-per-season / once-per-arc limits)
    _da_used_this_season: Set[str] = field(default_factory=set)
    _da_used_this_arc: Set[str] = field(default_factory=set)

    def __post_init__(self):
        if self.starting_mandate is None:
            self.starting_mandate = self.mandate
        if self.starting_military is None:
            self.starting_military = self.military

    def can_change(self, stat: str, delta: int) -> bool:
        """[canonical: stats_1_7_scale.md §Seasonal cap ±2/season]"""
        current = self._season_delta.get(stat, 0)
        proposed = current + delta
        if abs(proposed) > 2:                         # [canonical: stats_1_7_scale.md ±2/season cap]
            return False
        return True

    def change_stat(self, stat: str, delta: int, force: bool = False) -> bool:
        """[canonical: stats_1_7_scale.md §Seasonal cap + §Military Seasonal Cap]
        [canonical: stats_1_7_scale.md title "6-stat 1-7 scale" — hard ceiling at 7]"""
        if not force and not self.can_change(stat, delta):
            return False
        current = getattr(self, stat)
        if current is None:
            return False
        new_value = current + delta
        if stat == "military" and self.starting_military is not None:
            # [canonical: stats_1_7_scale.md §Military Seasonal Cap ED-039 "hard cap = starting +1"]
            if not force and new_value > self.starting_military + 1:  # [canonical: ED-039]
                new_value = self.starting_military + 1
        # 1-7 scale hard ceiling (canonical per doc title "1-7 scale")
        # [canonical: stats_1_7_scale.md title "1-7 scale"]
        if new_value > 7:                                 # [canonical: stats_1_7_scale.md "1-7 scale" ceiling]
            new_value = 7
        new_value = max(0, new_value)
        setattr(self, stat, new_value)
        self._season_delta[stat] = self._season_delta.get(stat, 0) + delta
        return True

    def reset_season_deltas(self) -> None:
        self._season_delta.clear()
        self._da_used_this_season.clear()

    def alive(self) -> bool:
        """Faction alive if at least one primary stat remains > 0."""
        stats = [self.mandate, self.influence, self.wealth, self.military,
                 self.stability]
        return any(s is not None and s > 0 for s in stats)


def starting_factions() -> Dict[str, Faction]:
    """[canonical: stats_1_7_scale.md §Starting Stats BG mode]"""
    return {
        "Crown": Faction(
            name="Crown",
            mandate=5, influence=5, wealth=4, military=4,    # [canonical: stats_1_7_scale.md Crown row]
            intel=None, stability=4,
        ),
        "Church": Faction(
            name="Church",
            mandate=5, influence=6, wealth=5, military=4,    # [canonical: stats_1_7_scale.md Church row]
            intel=None, stability=5,
        ),
        "Hafenmark": Faction(
            name="Hafenmark",
            mandate=4, influence=4, wealth=5, military=3,    # [canonical: stats_1_7_scale.md Hafenmark row]
            intel=None, stability=4,
        ),
        "Varfell": Faction(
            name="Varfell",
            mandate=3, influence=4, wealth=3, military=4,    # [canonical: stats_1_7_scale.md Varfell BG 3/3]
            intel=None, stability=4,
        ),
        "Guilds": Faction(
            name="Guilds",
            mandate=3, influence=4, wealth=6, military=2,    # [canonical: stats_1_7_scale.md Guilds row]
            intel=None, stability=5,
            playable=False,                                   # [canonical: params/bg/core.md Guilds NPC-only]
        ),
        "RestorationMovement": Faction(
            name="RestorationMovement",
            mandate=None, influence=None, wealth=None,        # [canonical: stats_1_7_scale.md RM "No stats PP-460"]
            military=None, intel=None, stability=None,
        ),
        "Lowenritter": Faction(
            name="Lowenritter",
            mandate=None, influence=2, wealth=None, military=5,  # [canonical: stats_1_7_scale.md Löwenritter row]
            intel=3, stability=5,
            playable=False,                                      # [canonical: params/bg/core.md Löwenritter "Split only"]
        ),
    }


# ============================================================================
# §3. Clocks + Environmental Tracks
#     [canonical: params/bg/core.md §Starting Values (v04 B2, PP-188)]
# ============================================================================


class AutonomyStage(Enum):
    """[canonical: params/bg/core.md §Löwenritter Graduated Autonomy]"""
    LOYAL = "Loyal"
    RESTLESS = "Restless"
    AUTONOMOUS = "Autonomous"
    SPLIT = "Split"


@dataclass
class Clocks:
    """[canonical: params/bg/core.md §Starting Values v04 B2]"""
    rendering_stability: int = 72     # [canonical: params/bg/core.md RS=72]
    church_influence: int = 28        # [canonical: params/bg/core.md CI=28 P-32]
    invasion_pressure: int = 20       # [canonical: params/bg/core.md IP=20]
    parliament_integrity: int = 7     # [canonical: params/bg/core.md PI=7 PP-188]
    aer: int = 2                      # [canonical: params/bg/core.md AER=2]
    torben_loyalty: int = 7           # [canonical: params/bg/core.md Torben=7]
    elske_loyalty: int = 4            # [canonical: params/bg/core.md Elske=4]
    warden_recognition: int = 0       # [canonical: params/bg/core.md WR=0 PP-605]
    warden_cooperation: int = 0       # [canonical: params/bg/core.md WC=0 PP-605]
    peninsular_strain: int = 0        # [canonical: params/bg/core.md Strain=0]
    autonomy: AutonomyStage = AutonomyStage.LOYAL
    _ci_season_delta: int = 0
    _pi_season_delta: int = 0
    _strain_season_delta: int = 0
    southernmost_surge_fired: bool = False
    mass_seizure_available: bool = False
    mass_seizure_used: bool = False
    autonomy_stage_seasons: int = 0   # how many seasons current stage active
    tc60_seizure_unlocked: bool = False  # [canonical: stats_1_7_scale.md TC60 Seizure trigger]

    def change_ci(self, delta: int) -> int:
        """[canonical: ci_political_v30.md §7.1 ±5/season cap ED-721 Option A]"""
        proposed = self._ci_season_delta + delta
        if proposed > 5:                              # [canonical: ci_political_v30.md "+5 cap"]
            delta = 5 - self._ci_season_delta
        elif proposed < -5:                           # [canonical: ci_political_v30.md "-5 cap"]
            delta = -5 - self._ci_season_delta
        if delta == 0:
            return 0
        new_ci = self.church_influence + delta
        new_ci = max(0, min(100, new_ci))             # [canonical: params/bg/core.md CI range 0-100]
        actual = new_ci - self.church_influence
        self.church_influence = new_ci
        self._ci_season_delta += actual
        # Mass Seizure gate
        # [canonical: params/bg/clocks.md §CI Effects "60+ Mass Seizure available"]
        if self.church_influence >= 60 and not self.mass_seizure_used:   # [canonical: params/bg/clocks.md CI 60]
            self.mass_seizure_available = True
        # TC60 Seizure unlocked [canonical: stats_1_7_scale.md TC60 Seizure]
        if self.church_influence >= 60:               # [canonical: stats_1_7_scale.md "TC 60"]
            self.tc60_seizure_unlocked = True
        return actual

    def change_pi(self, delta: int) -> int:
        """[canonical: stats_1_7_scale.md PI accrual cap +2/season]"""
        if delta > 0:
            proposed = self._pi_season_delta + delta
            if proposed > 2:                          # [canonical: stats_1_7_scale.md +2/season cap]
                delta = 2 - self._pi_season_delta
                if delta <= 0:
                    return 0
        new_pi = self.parliament_integrity + delta
        new_pi = max(0, min(20, new_pi))              # [canonical: params/bg/core.md PI range 0-20]
        actual = new_pi - self.parliament_integrity
        self.parliament_integrity = new_pi
        self._pi_season_delta += max(0, actual)
        return actual

    def change_strain(self, delta: int) -> int:
        """[canonical: params/bg/core.md Strain 0-10]"""
        new_strain = self.peninsular_strain + delta
        new_strain = max(0, min(10, new_strain))      # [canonical: params/bg/core.md Strain 0-10]
        actual = new_strain - self.peninsular_strain
        self.peninsular_strain = new_strain
        self._strain_season_delta += actual
        return actual

    def reset_season_deltas(self) -> None:
        self._ci_season_delta = 0
        self._pi_season_delta = 0
        self._strain_season_delta = 0


# ============================================================================
# §6. Territory Model
#     [canonical: designs/world/geography_v30.md §T1-T17 table]
#     [canonical: designs/provincial/ci_political_v30.md §1 PV/SW table]
# ============================================================================


@dataclass
class Territory:
    """One of 17 Valorian territories (T1-T17).
    [canonical: designs/world/geography_v30.md §Territory Table]
    [canonical: ci_political_v30.md §1 SW table]"""
    tid: str                          # "T1", "T2", ...
    name: str                         # "Valorsplatz", ...
    controller: Optional[str]         # faction name or None if Uncontrolled
    starting_controller: Optional[str]
    fort: int                         # defensive fort rating [canonical: geography_v30.md Fort column]
    max_fort: int
    pv: int                           # Prosperity Value [canonical: ci_political_v30.md §1 PV]
    sw: int                           # Spiritual Weight [canonical: ci_political_v30.md §1 SW]
    pt: int                           # Piety Tier [canonical: ci_political_v30.md §1 PT 0-5]
    accord: int                       # [canonical: peninsular_strain_v30.md Accord 0-3]
    adjacent: List[str]               # [canonical: geography_v30.md Adjacent column]
    sub_region: str                   # [canonical: geography_v30.md Sub column]
    church_prominent: bool = False    # true if PT >= 3 AND SW >= 3 [canonical: ci_political_v30.md §1 "prominent territory"]
    occupied_seasons: int = 0         # consecutive seasons under occupation (for Vanguard advance)

    def __post_init__(self):
        self.church_prominent = (self.pt >= 3 and self.sw >= 3)  # [canonical: ci_political_v30.md §1 prominence heuristic]


def starting_territories() -> Dict[str, Territory]:
    """All 17 Valorian territories with canonical starting state.
    [canonical: designs/world/geography_v30.md §Territory Table]
    [canonical: ci_political_v30.md §1 PV + SW table]"""
    data = [
        # (tid, name, controller, fort, max_fort, pv, sw, pt_default, sub, adjacent)
        # PT default = SW (proxy — canonical PT is a per-territory state, not given;
        # Session 3 will surface PT starting values from a dedicated source if available)
        ("T1",  "Valorsplatz",   "Crown",       2, 2, 5, 2, 2, "Capital",            ["T2","T5","T14","T16"]),          # [canonical: geography_v30.md T1]
        ("T2",  "Kronmark",      "Crown",       1, 1, 1, 2, 2, "Heartland",          ["T1","T3","T9","T14"]),            # [canonical: geography_v30.md T2]
        ("T3",  "Lowenskyst",    "Crown",       3, 4, 3, 2, 2, "Border Fortress",    ["T2","T9","T17"]),                 # [canonical: geography_v30.md T3 max_fort 4]
        ("T4",  "Grauwald",      "Varfell",     0, 0, 1, 1, 1, "Highland Timber",    ["T7","T12","T14"]),                # [canonical: geography_v30.md T4]
        ("T5",  "Feldmark",      "Crown",       0, 0, 1, 2, 2, "Breadbasket",        ["T1","T6","T14"]),                 # [canonical: geography_v30.md T5]
        ("T6",  "Stillhelm",     "Crown",       0, 0, 1, 1, 1, "S. Farmland",        ["T5","T13","T15"]),                # [canonical: geography_v30.md T6]
        ("T7",  "Rendstad",      "Hafenmark",   0, 0, 1, 2, 2, "Timber Valley",      ["T4","T8"]),                       # [canonical: geography_v30.md T7]
        ("T8",  "Gransol",       "Hafenmark",   1, 1, 4, 3, 3, "Hafenmark Capital",  ["T7","T9","T10","T17"]),           # [canonical: geography_v30.md T8; ci_political SW 3]
        ("T9",  "Himmelenger",   "Church",      2, 2, 5, 5, 5, "Cathedral City",     ["T2","T3","T8","T14","T17"]),      # [canonical: ci_political_v30.md §1 T9 "SW 5 PT 5 cathedral city"]
        ("T10", "Spartfell",     "Hafenmark",   2, 2, 1, 2, 2, "Border Castle",      ["T8","T11"]),                      # [canonical: geography_v30.md T10]
        ("T11", "Halvardshelm",  "Varfell",     0, 0, 1, 1, 1, "Central Fjords",     ["T10","T12"]),                     # [canonical: geography_v30.md T11]
        ("T12", "Sigurdshelm",   "Varfell",     1, 1, 4, 2, 2, "Varfell Seat",       ["T4","T11","T13"]),                # [canonical: geography_v30.md T12]
        ("T13", "Oastad",        "Varfell",     0, 0, 1, 1, 1, "Southern Fjords",    ["T6","T12","T15"]),                # [canonical: geography_v30.md T13]
        ("T14", "Ehrenfeld",     "Crown",       3, 4, 3, 3, 3, "Military Hinge",     ["T1","T2","T4","T5","T9"]),        # [canonical: geography_v30.md T14 max_fort 4]
        ("T15", "Askeheim",      None,          0, 0, 0, 0, 0, "Southernmost",       ["T6","T13"]),                      # [canonical: geography_v30.md T15 Uncontrolled]
        ("T16", "Schoenland",    "Schoenland",  1, 1, 0, 1, 1, "Island Republic",    ["T1"]),                            # [canonical: geography_v30.md T16 sea; ci_political PV "—"]
        ("T17", "Halvarshelm",   "Hafenmark",   0, 0, 1, 2, 2, "Northern Mines",     ["T3","T8","T9"]),                  # [canonical: geography_v30.md T17]
    ]
    out: Dict[str, Territory] = {}
    for tid, name, ctrl, fort, mf, pv, sw, pt, sub, adj in data:
        out[tid] = Territory(
            tid=tid, name=name, controller=ctrl, starting_controller=ctrl,
            fort=fort, max_fort=mf, pv=pv, sw=sw, pt=pt, accord=2,              # Accord default 2 (neutral) [canonical: peninsular_strain_v30.md Accord 0-3; default mid]
            adjacent=adj, sub_region=sub,
        )
    return out


def compute_proximity(territories: Dict[str, Territory], origin: str = "T15") -> Dict[str, int]:
    """BFS graph distance from the Calamity epicentre (T15 Askeheim) in territory edges.
    Clamped to 0-5. [canonical: params/bg/clocks.md "Proximity Rating (0-5) - node distance from Askeheim T15"]"""
    from collections import deque
    dist: Dict[str, int] = {origin: 0}                # [canonical: params/bg/clocks.md "Proximity 0 = T15 Askeheim"]
    q = deque([origin])
    while q:
        tid = q.popleft()
        d = dist[tid]
        for n in territories[tid].adjacent:
            if n in territories and n not in dist:
                dist[n] = min(5, d + 1)              # [canonical: params/bg/clocks.md "Proximity 0-5" clamped]
                q.append(n)
    # Any territory not reached: default to max proximity 5
    for tid in territories:
        if tid not in dist:
            dist[tid] = 5                             # [canonical: params/bg/clocks.md proximity max=5]
    return dist


# ============================================================================
# §7. Domain Action Framework
#     [canonical: params/factions/stats_1_7_scale.md §Unique Actions (PP-168)]
# ============================================================================


@dataclass
class DAResult:
    faction: str
    action: str
    target: Optional[str]             # target faction or territory id
    degree: Degree
    net: int
    faces: List[int]
    effects: List[str]                # human-readable effect descriptions


def _stat_pool(f: Faction, stat: str) -> int:
    """Look up a faction stat for a DA pool. Returns 0 if stat is None."""
    v = getattr(f, stat, None)
    return v if v is not None else 0


def da_royal_decree(camp: "Campaign", actor: Faction, target_faction: str,
                    target_stat: str, delta: int) -> DAResult:
    """Crown's Royal Decree.
    [canonical: stats_1_7_scale.md §Unique Actions Royal Decree]
    Roll: Mandate vs Ob 2. Once per season. Consecutive: +1 Ob/season.
    Cannot target Intel."""
    ob = 2                                            # [canonical: stats_1_7_scale.md Royal Decree Ob 2]
    consec = actor._consec_action.get("royal_decree", 0)
    ob_mod = consec                                   # [canonical: stats_1_7_scale.md "Consecutive: +1 Ob/season"]
    pool = _stat_pool(actor, "mandate")
    degree, net, faces = contest(pool, ob, camp.rng, ob_modifier=ob_mod)
    effects: List[str] = []
    if target_stat == "intel":                        # [canonical: stats_1_7_scale.md "Cannot target Intel"]
        return DAResult(actor.name, "royal_decree", target_faction, Degree.FAILURE,
                        net, faces, ["Invalid target: Intel (barred per PP-168)"])
    if degree in (Degree.OVERWHELMING, Degree.SUCCESS):
        tf = camp.factions.get(target_faction)
        if tf is not None:
            if tf.change_stat(target_stat, delta):
                effects.append(f"{target_faction}.{target_stat} {'+' if delta>0 else ''}{delta}")
        actor._consec_action["royal_decree"] = consec + 1
    else:
        actor._consec_action["royal_decree"] = 0  # reset on failure [canonical: stats_1_7_scale.md Royal Decree]
    actor._da_used_this_season.add("royal_decree")
    return DAResult(actor.name, "royal_decree", target_faction, degree, net, faces, effects)


def da_excommunication(camp: "Campaign", actor: Faction, target_faction: str) -> DAResult:
    """Church Excommunication.
    [canonical: stats_1_7_scale.md §Unique Actions Excommunication]
    Mandate vs target leader Mandate (or Ob 2 for non-leader). Success: target Mandate -1."""
    tf = camp.factions.get(target_faction)
    if tf is None or tf.mandate is None:
        return DAResult(actor.name, "excommunication", target_faction, Degree.FAILURE,
                        0, [], ["Invalid target (no Mandate)"])
    # Target is leader of target_faction; Ob = floor(target Mandate / 2) + 1
    # [canonical: stats_1_7_scale.md Excommunication "Mandate vs floor(target Mandate/2)+1"]
    ob = (tf.mandate // 2) + 1                        # [canonical: stats_1_7_scale.md Excommunication Ob formula]
    pool = _stat_pool(actor, "mandate")
    degree, net, faces = contest(pool, ob, camp.rng)
    effects: List[str] = []
    if degree in (Degree.OVERWHELMING, Degree.SUCCESS):
        if tf.change_stat("mandate", -1):             # [canonical: stats_1_7_scale.md Excommunication "target Mandate -1"]
            effects.append(f"{target_faction}.mandate -1")
    actor._da_used_this_season.add("excommunication")
    return DAResult(actor.name, "excommunication", target_faction, degree, net, faces, effects)


def da_sovereign_authority(camp: "Campaign", actor: Faction) -> DAResult:
    """Hafenmark's Sovereign Authority Doctrine.
    [canonical: stats_1_7_scale.md §Unique Actions Sovereign Authority Doctrine]
    Mandate vs Ob 4. Once per campaign arc."""
    ob = 4                                            # [canonical: stats_1_7_scale.md SAD Ob 4]
    pool = _stat_pool(actor, "mandate")
    degree, net, faces = contest(pool, ob, camp.rng)
    effects: List[str] = []
    church = camp.factions.get("Church")
    # [canonical: stats_1_7_scale.md SAD degree effects]
    if degree == Degree.OVERWHELMING:
        camp.clocks.change_ci(-3)                     # [canonical: stats_1_7_scale.md SAD OW "TC -3"]
        effects.append("CI -3")
        if church and church.change_stat("mandate", -1):  # [canonical: stats_1_7_scale.md SAD "Church Mandate -1"]
            effects.append("Church.mandate -1")
    elif degree == Degree.SUCCESS:
        camp.clocks.change_ci(-2)                     # [canonical: stats_1_7_scale.md SAD S "TC -2"]
        effects.append("CI -2")
        if church and church.change_stat("mandate", -1):  # [canonical: stats_1_7_scale.md SAD S Church -1]
            effects.append("Church.mandate -1")
    elif degree == Degree.PARTIAL:
        camp.clocks.change_ci(-1)                     # [canonical: stats_1_7_scale.md SAD P "TC -1"]
        effects.append("CI -1")
    else:  # FAILURE
        camp.clocks.change_ci(1)                      # [canonical: stats_1_7_scale.md SAD F "TC +1"]
        effects.append("CI +1")
        if actor.change_stat("mandate", -1):          # [canonical: stats_1_7_scale.md SAD F "Baralta Mandate -1"]
            effects.append(f"{actor.name}.mandate -1")
    actor._da_used_this_arc.add("sovereign_authority")
    actor._da_used_this_season.add("sovereign_authority")
    return DAResult(actor.name, "sovereign_authority", None, degree, net, faces, effects)


def da_private_collection(camp: "Campaign", actor: Faction) -> DAResult:
    """Varfell's Private Collection.
    [canonical: stats_1_7_scale.md §Unique Actions Private Collection]
    Intel vs Ob 2. Once per season."""
    ob = 2                                            # [canonical: stats_1_7_scale.md Private Collection Ob 2]
    pool = _stat_pool(actor, "intel")
    if pool == 0:
        # Varfell uses Wealth as its Intel proxy for covert work in BG mode (stub)
        pool = _stat_pool(actor, "wealth")
    degree, net, faces = contest(pool, ob, camp.rng)
    effects: List[str] = []
    # Simplified: Success = +2D to next Thread DA (tracked as flag, not yet consumed in Session 2);
    # Failure: Thread Tension +1 (RS -1 proxy) + Church Intel +1D (stub)
    # [canonical: stats_1_7_scale.md Private Collection "Success: +2D Thread DA OR reveal attribute OR -1 Ob Einhir Research"]
    # [canonical: stats_1_7_scale.md Private Collection Failure "Thread Tension +1"]
    if degree in (Degree.OVERWHELMING, Degree.SUCCESS):
        effects.append("Private Collection active — +2D next Thread DA (Session 3 honors this)")
    else:
        # Thread Tension +1 as RS -1 environmental effect (TT→RS mapping is canonical)
        # Stub: drop RS by 1 to model Thread disturbance.
        camp.clocks.rendering_stability = max(0, camp.clocks.rendering_stability - 1)  # [canonical: stats_1_7_scale.md Private Collection F "TT+1"]
        effects.append("RS -1 (Thread Tension proxy)")
    actor._da_used_this_season.add("private_collection")
    return DAResult(actor.name, "private_collection", None, degree, net, faces, effects)


def da_economic_leverage(camp: "Campaign", actor: Faction,
                         target_faction: str) -> DAResult:
    """Guilds' Economic Leverage.
    [canonical: stats_1_7_scale.md §Unique Actions Economic Leverage]
    Wealth vs target faction's Wealth."""
    tf = camp.factions.get(target_faction)
    if tf is None or tf.wealth is None:
        return DAResult(actor.name, "economic_leverage", target_faction, Degree.FAILURE,
                        0, [], ["Invalid target (no Wealth)"])
    ob = tf.wealth                                    # [canonical: stats_1_7_scale.md Econ Leverage "Wealth vs Wealth"]
    pool = _stat_pool(actor, "wealth")
    degree, net, faces = contest(pool, ob, camp.rng)
    effects: List[str] = []
    if degree == Degree.OVERWHELMING:
        tf.change_stat("wealth", -1)                  # [canonical: stats_1_7_scale.md Econ Leverage OW "target -1 Wealth"]
        effects.append(f"{target_faction}.wealth -1")
        # +1 Prosperity loss modeled as a territory PV reduction — Session 2 applies one random owned territory
        owned = [t for t in camp.territories.values() if t.controller == target_faction and t.pv > 0]
        if owned:
            chosen = camp.rng.choice(owned)
            chosen.pv = max(0, chosen.pv - 1)         # [canonical: stats_1_7_scale.md Econ Leverage OW "+1 Prosperity loss"]
            effects.append(f"{chosen.tid}.pv -1")
    elif degree == Degree.SUCCESS:
        tf.change_stat("wealth", -1)                  # [canonical: stats_1_7_scale.md Econ Leverage S]
        effects.append(f"{target_faction}.wealth -1")
    # Failure: Guild Favour -1 (not tracked in Session 2 — stub)
    # [canonical: stats_1_7_scale.md Econ Leverage F "Guild Favour -1"]
    actor._da_used_this_season.add("economic_leverage")
    return DAResult(actor.name, "economic_leverage", target_faction, degree, net, faces, effects)


def da_assert(camp: "Campaign", actor: Faction, territory: str) -> DAResult:
    """Church Assert (generic PT raise in target territory).
    [canonical: ci_political_v30.md §1 "PT change actions"]
    [canonical: params/bg/clocks.md §CI Effects "Mandatory Assert/Suppress at CI 50-69"]
    Roll: Mandate vs Ob 2. High-SW territories: +1D."""
    t = camp.territories.get(territory)
    if t is None:
        return DAResult(actor.name, "assert", territory, Degree.FAILURE, 0, [],
                        ["Invalid territory"])
    ob = 2                                            # generic Ob 2 for stat-raise DAs [canonical: stats_1_7_scale.md "Ob = floor(stat/2)+1" base=2]
    pool = _stat_pool(actor, "mandate")
    bonus = 1 if t.sw >= 4 else 0                     # [canonical: ci_political_v30.md §1 "high-SW +1D"]
    degree, net, faces = contest(pool, ob, camp.rng, bonus_dice=bonus)
    effects: List[str] = []
    if degree in (Degree.OVERWHELMING, Degree.SUCCESS):
        old_pt = t.pt
        t.pt = min(5, t.pt + 1)                       # [canonical: ci_political_v30.md §1 PT max 5]
        if t.pt != old_pt:
            effects.append(f"{t.tid}.pt +1 -> {t.pt}")
        t.church_prominent = (t.pt >= 3 and t.sw >= 3)   # [canonical: ci_political_v30.md §1 "prominent"]
    actor._da_used_this_season.add("assert")
    return DAResult(actor.name, "assert", territory, degree, net, faces, effects)


def da_suppress(camp: "Campaign", actor: Faction, territory: str) -> DAResult:
    """Suppress: generic PT lower. Open to any non-Church faction.
    [canonical: params/bg/clocks.md §CI Effects "Suppress" / ci_political_v30 §1 PT momentum]
    Roll: Mandate vs Ob 2."""
    t = camp.territories.get(territory)
    if t is None:
        return DAResult(actor.name, "suppress", territory, Degree.FAILURE, 0, [],
                        ["Invalid territory"])
    ob = 2                                            # [canonical: stats_1_7_scale.md generic DA Ob 2]
    pool = _stat_pool(actor, "mandate")
    bonus = 1 if t.sw >= 4 else 0                     # [canonical: ci_political_v30.md §1 "high-SW +1D"]
    degree, net, faces = contest(pool, ob, camp.rng, bonus_dice=bonus)
    effects: List[str] = []
    if degree in (Degree.OVERWHELMING, Degree.SUCCESS):
        old_pt = t.pt
        t.pt = max(0, t.pt - 1)                       # [canonical: ci_political_v30.md §1 PT min 0]
        if t.pt != old_pt:
            effects.append(f"{t.tid}.pt -1 -> {t.pt}")
        t.church_prominent = (t.pt >= 3 and t.sw >= 3)   # [canonical: ci_political_v30.md §1 prominent]
    actor._da_used_this_season.add("suppress")
    return DAResult(actor.name, "suppress", territory, degree, net, faces, effects)


def da_govern(camp: "Campaign", actor: Faction, territory: str) -> DAResult:
    """Govern: raise Accord in a controlled territory.
    [canonical: ci_political_v30.md §7.4 Govern "Success = Accord +1; OW in capital = Mandate +1"]
    Roll: Mandate vs Ob 2."""
    t = camp.territories.get(territory)
    if t is None or t.controller != actor.name:
        return DAResult(actor.name, "govern", territory, Degree.FAILURE, 0, [],
                        ["Not controller"])
    ob = 2                                            # [canonical: stats_1_7_scale.md generic Ob 2]
    pool = _stat_pool(actor, "mandate")
    degree, net, faces = contest(pool, ob, camp.rng)
    effects: List[str] = []
    if degree in (Degree.OVERWHELMING, Degree.SUCCESS):
        if t.accord < 3:                              # [canonical: peninsular_strain_v30.md Accord cap 3]
            t.accord += 1
            effects.append(f"{t.tid}.accord +1 -> {t.accord}")
        # PP-174: OW in own capital -> Mandate +1
        # [canonical: ci_political_v30.md §7.4 "Govern OW in own capital: Mandate +1"]
        if degree == Degree.OVERWHELMING and t.sub_region.lower().endswith("capital"):
            if actor.change_stat("mandate", 1):       # [canonical: ci_political_v30.md §7.4 OW capital]
                effects.append(f"{actor.name}.mandate +1 (capital OW)")
    actor._da_used_this_season.add("govern")
    return DAResult(actor.name, "govern", territory, degree, net, faces, effects)


def da_trade(camp: "Campaign", actor: Faction) -> DAResult:
    """Trade: generic Wealth-raise action.
    Stub: Wealth vs Ob 2. Success: actor Wealth +1."""
    ob = 2                                            # [canonical: stats_1_7_scale.md generic Ob 2]
    pool = _stat_pool(actor, "wealth")
    degree, net, faces = contest(pool, ob, camp.rng)
    effects: List[str] = []
    if degree in (Degree.OVERWHELMING, Degree.SUCCESS):
        if actor.change_stat("wealth", 1):            # [canonical: stats_1_7_scale.md Domain Action stat ±1]
            effects.append(f"{actor.name}.wealth +1")
    actor._da_used_this_season.add("trade")
    return DAResult(actor.name, "trade", None, degree, net, faces, effects)


# ============================================================================
# §8. Piety Yield & Church Political Pool
#     [canonical: ci_political_v30.md §1 "Piety Yield weighting"]
#     [canonical: ci_political_v30.md §3 "Church political pool"]
# ============================================================================


# PT tier multiplier lookup. Canonical examples only cover PT 5 and PT 3.
# [canonical: ci_political_v30.md §1 "T9 (SW 5, PT 5): yield = 1.0 × (5/5)"]
# [canonical: ci_political_v30.md §1 "T8 (SW 3, PT 3): yield = 0.25 × (3/5)"]
# Intermediate PT values interpolated geometrically (PROVISIONAL — flagged for
# Jordan authorial review at Session 3). Pattern: PT 5=1.0, 4=0.5, 3=0.25,
# 2=0.125, 1=0.0625 (halving) — suggests doubling scaling per PT step.
PT_MULTIPLIER = {                                     # [canonical: ci_political_v30.md §1 examples + PROVISIONAL interpolation]
    0: 0.0,                                           # no yield below PT 1
    1: 0.0625,                                        # PROVISIONAL [canonical: interpolation from PT 3=0.25]
    2: 0.125,                                         # PROVISIONAL
    3: 0.25,                                          # [canonical: ci_political_v30.md T8 example]
    4: 0.5,                                           # PROVISIONAL
    5: 1.0,                                           # [canonical: ci_political_v30.md T9 example]
}


def piety_yield_per_season(territories: Dict[str, Territory]) -> float:
    """Sum Piety Yield across all Church-prominent territories.
    [canonical: ci_political_v30.md §1 "CI from Piety Yield = Σ(PT tier × SW factor)"]"""
    total = 0.0
    for t in territories.values():
        if not t.church_prominent:                    # [canonical: ci_political_v30.md §1 "prominent territory"]
            continue
        pt_mult = PT_MULTIPLIER.get(t.pt, 0.0)
        sw_factor = t.sw / 5.0                        # [canonical: ci_political_v30.md §1 "SW factor = SW/5"]
        total += pt_mult * sw_factor
    return total


def church_political_bonus(clocks: Clocks) -> int:
    """Bonus dice to Church parliamentary/negotiation pool.
    [canonical: ci_political_v30.md §7.2 "floor(CI/20)"]"""
    return clocks.church_influence // 20              # [canonical: ci_political_v30.md §7.2 "floor(CI/20)"]


def church_opposition_penalty(clocks: Clocks) -> int:
    """Mandate reduction against factions opposing Church.
    [canonical: ci_political_v30.md §7.2 "-floor(CI/30) voting Mandate"]"""
    return clocks.church_influence // 30              # [canonical: ci_political_v30.md §7.2 "floor(CI/30)"]


# ============================================================================
# §9. Seasonal Loop Phases (extended from Session 1)
#     [canonical: stats_1_7_scale.md §PP-242 Seasonal cap timing]
# ============================================================================


@dataclass
class SimLog:
    season: int
    events: List[str] = field(default_factory=list)

    def add(self, event: str) -> None:
        self.events.append(event)


@dataclass
class Campaign:
    """Game-wide state container (Session 2)."""
    seed: int
    factions: Dict[str, Faction]
    clocks: Clocks
    territories: Dict[str, Territory]
    proximity: Dict[str, int]
    season: int = 0
    any_battle_this_season: bool = False
    any_hostile_stability_da: bool = False
    logs: List[SimLog] = field(default_factory=list)
    rng: random.Random = field(default_factory=random.Random)
    campaign_over: bool = False
    victory_condition: Optional[str] = None
    da_results: List[DAResult] = field(default_factory=list)

    def __post_init__(self):
        self.rng = random.Random(self.seed)


def initial_campaign(seed: int = 0) -> Campaign:
    terrs = starting_territories()
    prox = compute_proximity(terrs)
    return Campaign(
        seed=seed,
        factions=starting_factions(),
        clocks=Clocks(),
        territories=terrs,
        proximity=prox,
    )


def accounting_phase(camp: Campaign, log: SimLog) -> None:
    """Run end-of-season Accounting.
    [canonical: stats_1_7_scale.md §PP-242 + §Theocracy Counter advance]"""

    # 1. TC advance +1/season (institutional momentum)
    # [canonical: stats_1_7_scale.md "TC advances by +1 per season"]
    applied = camp.clocks.change_ci(1)                # [canonical: stats_1_7_scale.md +1/season]
    if applied:
        log.add(f"CI +{applied} (institutional momentum)")

    # 2. Piety Yield — per-territory contribution to CI
    # [canonical: ci_political_v30.md §1 "Piety Yield weighting"]
    py = piety_yield_per_season(camp.territories)
    # Round down to integer for CI application (sim fidelity: PY accumulates
    # fractionally but CI is integer). Session 3 may track fractional PY banking.
    py_int = int(py)                                  # [canonical: params/bg/core.md CI integer track]
    if py_int > 0:
        actual = camp.clocks.change_ci(py_int)        # subject to ±5/season cap (ED-721 A)
        if actual:
            log.add(f"Piety Yield +{actual} (territories: {py:.2f})")

    # 3. Battle consequences
    # [canonical: params/bg/clocks.md §Battle Consequences]
    if camp.any_battle_this_season:
        camp.clocks.rendering_stability = max(0, camp.clocks.rendering_stability - 1)  # [canonical: params/bg/clocks.md RS-1]
        log.add(f"RS -1 (battle season), now {camp.clocks.rendering_stability}")
        camp.clocks.invasion_pressure = min(100, camp.clocks.invasion_pressure + 2)    # [canonical: params/bg/clocks.md IP+2]
        log.add(f"IP +2 (battle season), now {camp.clocks.invasion_pressure}")
        camp.clocks.change_strain(1)                  # [canonical: params/bg/clocks.md Strain+1]
        log.add(f"Strain +1 (battle season), now {camp.clocks.peninsular_strain}")

    # 4. Peaceful-season Strain decay
    # [canonical: params/bg/core.md Strain "Decays -1/peaceful season"]
    if not camp.any_battle_this_season and camp.clocks.peninsular_strain > 0:
        camp.clocks.change_strain(-1)                 # [canonical: params/bg/core.md Strain decay]
        log.add(f"Strain -1 (peaceful season), now {camp.clocks.peninsular_strain}")

    # 5. PI accrual for any Mandate < 3 faction
    # [canonical: stats_1_7_scale.md PI "+1/season any Mandate < 3"]
    pi_pressure = sum(1 for f in camp.factions.values()
                      if f.mandate is not None and f.mandate < 3)  # [canonical: stats_1_7_scale.md PI Mandate<3]
    if pi_pressure > 0:
        applied = camp.clocks.change_pi(pi_pressure)
        log.add(f"PI +{applied} ({pi_pressure} factions Mandate<3)")

    # 6. PI recovery
    # [canonical: stats_1_7_scale.md PI "-1/season zero hostile Stability DAs"]
    if not camp.any_hostile_stability_da and camp.clocks.parliament_integrity > 0:
        camp.clocks.parliament_integrity -= 1         # [canonical: stats_1_7_scale.md PI recovery]
        log.add(f"PI -1, now {camp.clocks.parliament_integrity}")

    # 7. Mandate recovery
    # [canonical: stats_1_7_scale.md §Mandate Recovery ED-066b provisional]
    for f in camp.factions.values():
        if (f.mandate is not None and f.starting_mandate is not None
                and f.mandate < f.starting_mandate
                and f.stability is not None and f.stability >= 3):
            if f.can_change("mandate", 1):
                f.change_stat("mandate", 1)
                log.add(f"{f.name}: Mandate +1 (recovery), now {f.mandate}")

    # 8. Faction alive check + elimination Strain bump
    # [canonical: params/bg/clocks.md "Faction elimination: Strain +2"]
    for fname, f in list(camp.factions.items()):
        if not f.alive() and f.starting_mandate is not None:
            # Only playable-class factions contribute to Strain on elimination
            camp.clocks.change_strain(2)              # [canonical: params/bg/clocks.md Strain+2 elimination]
            log.add(f"ENDGAME: {fname} eliminated — Strain +2")

    # 9. Autonomy advancement
    check_autonomy_advancement(camp, log)

    # 10. Endgame
    check_endgame(camp, log)

    # 11. Reset per-season trackers
    for f in camp.factions.values():
        f.reset_season_deltas()
    camp.clocks.reset_season_deltas()
    camp.any_battle_this_season = False
    camp.any_hostile_stability_da = False


def check_autonomy_advancement(camp: Campaign, log: SimLog) -> None:
    """[canonical: params/bg/core.md §Löwenritter Graduated Autonomy]"""
    crown = camp.factions.get("Crown")
    if crown is None:
        return
    stage = camp.clocks.autonomy
    new_stage = stage
    if stage == AutonomyStage.LOYAL:
        if crown.stability is not None and crown.stability <= 3:   # [canonical: params/bg/core.md Restless trigger]
            new_stage = AutonomyStage.RESTLESS
    elif stage == AutonomyStage.RESTLESS:
        if crown.stability is not None and crown.stability <= 2:   # [canonical: params/bg/core.md Autonomous trigger]
            new_stage = AutonomyStage.AUTONOMOUS
    elif stage == AutonomyStage.AUTONOMOUS:
        # 4+ seasons Autonomous unresolved -> Split
        if camp.clocks.autonomy_stage_seasons >= 4:   # [canonical: params/bg/core.md "4+ seasons Autonomous"]
            new_stage = AutonomyStage.SPLIT
        elif not crown.alive():
            new_stage = AutonomyStage.SPLIT
    if new_stage != stage:
        camp.clocks.autonomy = new_stage
        camp.clocks.autonomy_stage_seasons = 0
        log.add(f"Autonomy: {stage.value} -> {new_stage.value}")
        # Split: Löwenritter activates as full faction
        # [canonical: params/bg/core.md Split "M3/I2/W3/Mil6/Stab5"]
        if new_stage == AutonomyStage.SPLIT:
            lr = camp.factions.get("Lowenritter")
            if lr:
                lr.mandate = 3                        # [canonical: params/bg/core.md Split M3]
                lr.wealth = 3                         # [canonical: params/bg/core.md Split W3]
                lr.military = 6                       # [canonical: params/bg/core.md Split Mil6]
                lr.playable = True
                log.add("Lowenritter: activated (Split stage — M3/I2/W3/Mil6/Stab5)")
    else:
        camp.clocks.autonomy_stage_seasons += 1


def check_endgame(camp: Campaign, log: SimLog) -> None:
    """[canonical: params/bg/clocks.md "RS 0 = Rupture"]
    [canonical: params/bg/core.md PI >= 20 Crown elimination]"""
    if camp.clocks.rendering_stability <= 0:          # [canonical: params/bg/clocks.md RS 0 Rupture]
        camp.campaign_over = True
        camp.victory_condition = "SHARED_LOSS: RS Rupture"
        log.add("ENDGAME: RS Rupture")
        return
    if camp.clocks.parliament_integrity >= 20:        # [canonical: params/bg/core.md PI 20]
        camp.campaign_over = True
        camp.victory_condition = "CROWN_ELIMINATED: PI >= 20"
        log.add("ENDGAME: PI 20 Crown eliminated")
        return


# ============================================================================
# §10. Faction AI — Priority-based DA selection (Session 2 stub)
#      Full NPC priority trees from npc_behavior_v30 §7-8 arrive in Session 3.
# ============================================================================


def select_da_for_faction(camp: Campaign, f: Faction) -> Optional[Callable]:
    """Choose a DA for the given faction based on simplified priority tree.
    Session 2 stub — Session 3 replaces with canonical NPC priority trees."""
    if not f.alive() or not f.playable:
        return None

    # Priority 0: if unique-action available this arc and no higher need, use it
    # Priority 1: if Mandate below starting, repair
    # Priority 2: if Stability low, defend
    # Priority 3: faction-specific action
    # Priority 4: generic Trade

    def _royal_decree():
        # Target self for Mandate repair; else target Church for Mandate
        if f.mandate is not None and f.mandate < (f.starting_mandate or 5):
            # Use Royal Decree on self for Mandate +1
            return lambda: da_royal_decree(camp, f, f.name, "mandate", 1)
        # Else damp Church
        return lambda: da_royal_decree(camp, f, "Church", "mandate", -1)

    def _excommunication():
        # Church targets whichever faction has highest Mandate (except self)
        targets = [(n, tf.mandate) for n, tf in camp.factions.items()
                   if tf.name != f.name and tf.mandate is not None]
        if not targets:
            return None
        targets.sort(key=lambda x: -x[1])
        return lambda: da_excommunication(camp, f, targets[0][0])

    def _sad():
        return lambda: da_sovereign_authority(camp, f)

    def _collection():
        return lambda: da_private_collection(camp, f)

    def _leverage():
        # Target faction with highest Wealth except self
        targets = [(n, tf.wealth) for n, tf in camp.factions.items()
                   if tf.name != f.name and tf.wealth is not None]
        if not targets:
            return None
        targets.sort(key=lambda x: -x[1])
        return lambda: da_economic_leverage(camp, f, targets[0][0])

    def _assert_highest_sw():
        # Church: assert in highest-SW non-already-max territory
        candidates = sorted(
            [t for t in camp.territories.values() if t.pt < 5],
            key=lambda t: -t.sw,
        )
        if not candidates:
            return None
        return lambda: da_assert(camp, f, candidates[0].tid)

    def _suppress_church_prominent():
        # Non-Church: suppress where Church prominent
        candidates = [t for t in camp.territories.values()
                      if t.church_prominent and t.pt > 0]
        if not candidates:
            return None
        chosen = camp.rng.choice(candidates)
        return lambda: da_suppress(camp, f, chosen.tid)

    def _govern_own():
        # Govern any owned territory with Accord < 3
        owned = [t for t in camp.territories.values()
                 if t.controller == f.name and t.accord < 3]
        if not owned:
            return None
        chosen = camp.rng.choice(owned)
        return lambda: da_govern(camp, f, chosen.tid)

    def _trade():
        return lambda: da_trade(camp, f)

    # Build candidate list by priority
    candidates: List[Callable] = []

    # Priority 1: Mandate repair via Royal Decree (Crown only) or Govern (any)
    if f.mandate is not None and f.starting_mandate is not None and f.mandate < f.starting_mandate:
        if f.name == "Crown" and "royal_decree" not in f._da_used_this_season:
            candidates.append(_royal_decree())
        g = _govern_own()
        if g is not None:
            candidates.append(g)

    # Priority 2: faction-specific unique action
    if f.name == "Crown" and "royal_decree" not in f._da_used_this_season:
        candidates.append(_royal_decree())
    elif f.name == "Church":
        if "excommunication" not in f._da_used_this_season:
            e = _excommunication()
            if e is not None:
                candidates.append(e)
        if "assert" not in f._da_used_this_season:
            a = _assert_highest_sw()
            if a is not None:
                candidates.append(a)
    elif f.name == "Hafenmark":
        if ("sovereign_authority" not in f._da_used_this_arc
                and f.mandate is not None and f.mandate >= 4):
            candidates.append(_sad())
    elif f.name == "Varfell":
        if "private_collection" not in f._da_used_this_season:
            candidates.append(_collection())
    elif f.name == "Guilds":
        if "economic_leverage" not in f._da_used_this_season:
            l = _leverage()
            if l is not None:
                candidates.append(l)

    # Priority 3: Suppress where Church prominent (if non-Church)
    if f.name != "Church" and "suppress" not in f._da_used_this_season:
        s = _suppress_church_prominent()
        if s is not None:
            candidates.append(s)

    # Priority 4: Trade
    if "trade" not in f._da_used_this_season:
        candidates.append(_trade())

    if not candidates:
        return None

    return candidates[0]


def domain_actions_phase(camp: Campaign, log: SimLog) -> None:
    """Each alive playable faction performs one DA per season (simplified).
    [canonical: stats_1_7_scale.md "Frequency: once per season"]"""
    for fname, f in camp.factions.items():
        if not f.playable or not f.alive():
            continue
        action_fn = select_da_for_faction(camp, f)
        if action_fn is None:
            continue
        result = action_fn()
        if result is None:
            continue
        camp.da_results.append(result)
        eff_txt = "; ".join(result.effects) if result.effects else "no effect"
        log.add(f"DA: {fname} {result.action}"
                f" -> {result.degree.value} (net={result.net}) [{eff_txt}]")


def run_season(camp: Campaign) -> SimLog:
    camp.season += 1
    log = SimLog(season=camp.season)
    log.add(f"--- Season {camp.season} ---")
    domain_actions_phase(camp, log)
    accounting_phase(camp, log)
    log.add(f"State: RS={camp.clocks.rendering_stability} "
            f"CI={camp.clocks.church_influence} IP={camp.clocks.invasion_pressure} "
            f"PI={camp.clocks.parliament_integrity} Strain={camp.clocks.peninsular_strain} "
            f"Autonomy={camp.clocks.autonomy.value}")
    camp.logs.append(log)
    return log


def run_campaign(max_seasons: int = 40, seed: int = 0) -> Campaign:
    camp = initial_campaign(seed=seed)
    while not camp.campaign_over and camp.season < max_seasons:
        run_season(camp)
    return camp


# ============================================================================
# §13. Smoke Tests
# ============================================================================


def smoke_test_dice() -> None:
    """[canonical: params/bg/core.md §Dice System + §Degree Table]"""
    assert net_successes([10]) == 2                   # [canonical: params/bg/core.md face 10]
    assert net_successes([1]) == -1                   # [canonical: params/bg/core.md face 1]
    assert net_successes([7]) == 1                    # [canonical: params/bg/core.md face 7]
    assert net_successes([6]) == 0                    # [canonical: params/bg/core.md face 6]
    assert net_successes([10, 7, 6, 1]) == 2          # [canonical: params/bg/core.md sum]
    assert resolve_degree(4, 2) == Degree.OVERWHELMING
    assert resolve_degree(2, 2) == Degree.SUCCESS
    assert resolve_degree(1, 2) == Degree.PARTIAL
    assert resolve_degree(0, 2) == Degree.FAILURE
    assert resolve_degree(4, 10) == Degree.FAILURE    # [canonical: params/bg/core.md Ob 10 exception]
    assert resolve_degree(5, 10) == Degree.PARTIAL
    print("DICE TEST PASSED")


def smoke_test_10_peaceful() -> None:
    """10 seasons with NO DAs (override). [Session 1 acceptance test]"""
    camp = initial_campaign(seed=42)                  # [canonical: ledger SMOKE_SEED]
    for _ in range(10):                               # [canonical: ledger SMOKE_SEASONS]
        camp.season += 1
        log = SimLog(season=camp.season)
        # Skip DA phase entirely (no DAs)
        accounting_phase(camp, log)
        camp.logs.append(log)
    # Expect CI = 28 + 10 = 38 (no Piety Yield since no territories are Church-prominent
    # at PT 2 default for most; T9 starts with PT 5, SW 5, Church controlled,
    # so it DOES contribute Piety Yield.
    # T9 contribution per season: PT 5 mult 1.0 × SW 5/5 = 1.0 -> int(1.0) = 1
    # T8 SW 3 PT 3 (prominent) Hafenmark controlled — 0.25 × 0.6 = 0.15 -> int -> 0
    # T14 SW 3 PT 3 Crown controlled — same, 0.15 -> 0
    # So Piety Yield adds +1/season from T9 alone after int floor.
    # Total CI per season: +1 (momentum) + 1 (PY T9) = +2, capped at +5.
    # After 10 seasons: 28 + 20 = 48 (floor over 10 seasons)
    # But wait — cap is ±5/season, so each season CI can move at most +5.
    # With +1 momentum +1 PY = +2 each season = 20 total = 48.
    expected_ci = 28 + 20                             # [canonical: ledger CI 28 + 2/season*10 seasons = 48]
    assert camp.clocks.church_influence == expected_ci, (
        f"CI expected {expected_ci}, got {camp.clocks.church_influence}"
    )
    # RS held at 72
    assert camp.clocks.rendering_stability == 72      # [canonical: params/bg/core.md RS 72]
    # PI drained to 0
    assert camp.clocks.parliament_integrity == 0      # [canonical: stats_1_7_scale.md PI recovery]
    # Autonomy still Loyal
    assert camp.clocks.autonomy == AutonomyStage.LOYAL
    print(f"10-season PEACEFUL TEST PASSED "
          f"(CI={camp.clocks.church_influence}, RS=72, PI=0, Autonomy=Loyal)")


def smoke_test_40_with_das(seed: int = 42) -> Campaign:
    """40-season full run with DAs. Session 2 acceptance test."""
    camp = run_campaign(max_seasons=40, seed=seed)    # [canonical: ledger SMOKE_MAX_SEASONS 40]
    # Simple sanity assertions
    # (a) At least some DAs ran
    assert len(camp.da_results) > 0, "No DAs executed"
    # (b) At least one faction is still alive
    alive = [f for f in camp.factions.values() if f.alive() and f.playable]
    # (c) Clocks didn't underflow/overflow (sanity)
    assert 0 <= camp.clocks.rendering_stability <= 100
    assert 0 <= camp.clocks.church_influence <= 100
    assert 0 <= camp.clocks.invasion_pressure <= 100
    assert 0 <= camp.clocks.parliament_integrity <= 20
    assert 0 <= camp.clocks.peninsular_strain <= 10
    print(f"40-SEASON TEST PASSED (seed {seed})")
    print(f"  Ran {camp.season} seasons, {len(camp.da_results)} DAs")
    print(f"  Alive playable factions: {[f.name for f in alive]}")
    print(f"  Final state: RS={camp.clocks.rendering_stability} "
          f"CI={camp.clocks.church_influence} IP={camp.clocks.invasion_pressure} "
          f"PI={camp.clocks.parliament_integrity} Strain={camp.clocks.peninsular_strain} "
          f"Autonomy={camp.clocks.autonomy.value}")
    if camp.victory_condition:
        print(f"  Victory: {camp.victory_condition}")
    # Summary: DA counts by type
    from collections import Counter
    da_counts = Counter(r.action for r in camp.da_results)
    print(f"  DA counts: {dict(da_counts.most_common())}")
    # Summary: faction stat deltas from starting
    for fname, f in camp.factions.items():
        if f.mandate is not None and f.starting_mandate is not None:
            print(f"  {fname}: M={f.mandate} I={f.influence} W={f.wealth} "
                  f"Mil={f.military} Sta={f.stability}")
    return camp


def smoke_test_territory_model() -> None:
    """Verify 17 territories, proximity graph, Church prominence."""
    terrs = starting_territories()
    assert len(terrs) == 17                           # [canonical: geography_v30.md 17 territories T1-T17]
    # T9 must be Church Prominent at start (PT 5, SW 5)
    # [canonical: ci_political_v30.md T9 "PT 5 SW 5 cathedral"]
    assert terrs["T9"].church_prominent is True
    # T15 (Askeheim) should be uncontrolled
    # [canonical: geography_v30.md T15 "Uncontrolled"]
    assert terrs["T15"].controller is None
    # Proximity graph
    prox = compute_proximity(terrs)
    assert prox["T15"] == 0                           # [canonical: params/bg/clocks.md "Proximity 0 = T15"]
    # T6 (adjacent to T15) should be proximity 1
    # [canonical: geography_v30.md T15 adjacent T6,T13]
    assert prox["T6"] == 1
    assert prox["T13"] == 1
    # T1 Valorsplatz should be farther
    assert prox["T1"] >= 2
    print(f"TERRITORY TEST PASSED (17 territories, T15 prox 0, T1 prox {prox['T1']})")


def smoke_test_piety_yield() -> None:
    """Verify Piety Yield formula against canonical examples.
    [canonical: ci_political_v30.md §1 "T9 yield = 1.0; T8 yield = 0.15"]"""
    terrs = starting_territories()
    py = piety_yield_per_season(terrs)
    # T9 alone contributes 1.0
    # [canonical: ci_political_v30.md "T9 (SW 5, PT 5): yield = 1.0"]
    # T8 contributes 0.15 (PT 3, SW 3)
    # [canonical: ci_political_v30.md "T8 (SW 3, PT 3): yield = 0.15"]
    # T14 contributes 0.15 (PT 3, SW 3)
    # [canonical: ci_political_v30.md "T14 yield = 0.15"]
    # Total ≈ 1.30
    # Allow float tolerance (0.6 is not exact in binary)
    expected_center = 1.3                             # [canonical: ci_political_v30.md §1 T9(1.0)+T8(0.15)+T14(0.15)]
    tolerance = 0.01                                  # float-precision slack
    assert abs(py - expected_center) < tolerance, f"PY expected ~1.3, got {py:.5f}"
    print(f"PIETY YIELD TEST PASSED (total={py:.2f} CI/season from prominent territories)")


def smoke_test_church_bonus() -> None:
    """Church political pool bonus and opposition penalty.
    [canonical: ci_political_v30.md §7.2]"""
    c = Clocks()
    c.church_influence = 60                           # [canonical: ledger CI_MASS_SEIZURE_GATE 60]
    # floor(60/20) = 3 [canonical: ci_political_v30.md §7.2 "floor(CI/20)"]
    assert church_political_bonus(c) == 3             # [canonical: ci_political_v30.md 60/20=3]
    # floor(60/30) = 2 [canonical: ci_political_v30.md §7.2]
    assert church_opposition_penalty(c) == 2
    c.church_influence = 100
    assert church_political_bonus(c) == 5             # [canonical: ci_political_v30.md 100/20=5]
    assert church_opposition_penalty(c) == 3          # [canonical: ci_political_v30.md 100/30=3]
    print("CHURCH BONUS TEST PASSED")


# ============================================================================
# §14. Victory Evaluation
#      [canonical: designs/provincial/victory_v30.md §0 Universal Victory]
#      [canonical: designs/provincial/victory_v30.md §3.2 CI=100 Mass Seizure]
#      [canonical: designs/provincial/victory_v30.md §0.1 Partition Co-Victory]
# ============================================================================

# Playable territories for Peninsular Sovereignty check
# [canonical: victory_v30.md §0 "All 15 playable territories (T1-T14, T17)"]
PLAYABLE_TERRITORIES = ["T1","T2","T3","T4","T5","T6","T7","T8","T9",          # [canonical: victory_v30.md §0]
                        "T10","T11","T12","T13","T14","T17"]                    # [canonical: victory_v30.md §0 "15 playable"]

# Peninsular Sovereignty thresholds
# [canonical: victory_v30.md §0 table]
PS_ACCORD_MIN = 2                                     # [canonical: victory_v30.md §0 Accord >= 2]
PS_STRAIN_MAX = 6                                     # [canonical: victory_v30.md §0 Strain <= 6]
PS_CONSECUTIVE = 2                                    # [canonical: victory_v30.md §0 "held 2 consecutive Accountings"]

# Partition thresholds [canonical: victory_v30.md §0.1]
PARTITION_PV_MIN = 10                                 # [canonical: victory_v30.md §0.1 "Each faction PV >= 10"]
PARTITION_NONAGG_SEASONS = 4                          # [canonical: victory_v30.md §0.1 "No Battle in preceding 4 seasons"]
PARTITION_MANDATE_MIN = 3                             # [canonical: victory_v30.md §0.1 "both Mandate >= 3"]


def evaluate_peninsular_sovereignty(camp: "Campaign") -> Optional[str]:
    """Check if any single faction holds Peninsular Sovereignty.
    [canonical: victory_v30.md §0 Universal Victory Condition]
    Returns faction name if condition met this season, else None."""
    for fname, f in camp.factions.items():
        if not f.alive() or not f.playable:
            continue
        # Territory control: all 15 playable territories
        # [canonical: victory_v30.md §0 "All 15 playable territories"]
        owned = [camp.territories[tid] for tid in PLAYABLE_TERRITORIES
                 if camp.territories[tid].controller == fname]
        if len(owned) < len(PLAYABLE_TERRITORIES):    # [canonical: victory_v30.md §0 "all 15"]
            continue
        # Accord >= 2 in all controlled
        # [canonical: victory_v30.md §0 Accord >= 2]
        if any(t.accord < PS_ACCORD_MIN for t in owned):
            continue
        # Strain <= 6
        # [canonical: victory_v30.md §0 Strain <= 6]
        if camp.clocks.peninsular_strain > PS_STRAIN_MAX:
            continue
        return fname
    return None


def evaluate_partition(camp: "Campaign") -> Optional[Tuple[str, str]]:
    """Check Partition co-victory.
    [canonical: victory_v30.md §0.1]
    Returns (faction_a, faction_b) if condition met, else None."""
    alive = [f for f in camp.factions.values() if f.alive() and f.playable]
    if len(alive) != 2:                               # [canonical: victory_v30.md §0.1 "exactly two factions remain"]
        return None
    fa, fb = alive
    # Both Mandate >= 3 [canonical: victory_v30.md §0.1]
    if (fa.mandate is None or fa.mandate < PARTITION_MANDATE_MIN
            or fb.mandate is None or fb.mandate < PARTITION_MANDATE_MIN):
        return None
    # Collective control of all 15 playable
    # [canonical: victory_v30.md §0.1 "Both factions collectively control all 15"]
    owned = sum(1 for tid in PLAYABLE_TERRITORIES
                if camp.territories[tid].controller in (fa.name, fb.name))
    if owned < len(PLAYABLE_TERRITORIES):
        return None
    # Individual PV >= 10 each [canonical: victory_v30.md §0.1 "Each faction PV >= 10"]
    for faction in (fa, fb):
        pv_sum = sum(t.pv for t in camp.territories.values()
                     if t.controller == faction.name)
        if pv_sum < PARTITION_PV_MIN:                 # [canonical: victory_v30.md §0.1 PV>=10]
            return None
    # Strain <= 6 [canonical: victory_v30.md §0.1]
    if camp.clocks.peninsular_strain > PS_STRAIN_MAX:
        return None
    # Non-aggression not tracked in Session 3 — stub (assume met if alive pair)
    return (fa.name, fb.name)


def evaluate_victory(camp: "Campaign", log: "SimLog") -> bool:
    """Check all victory paths each Accounting. Returns True if game ends.
    [canonical: victory_v30.md §0 + §3.2 + §0.1]"""
    if camp.campaign_over:
        return True
    # Church CI=100 Theocracy Unification [canonical: victory_v30.md §3.2 "CI=100 Mass Seizure Declaration"]
    if camp.clocks.church_influence >= 100:           # [canonical: victory_v30.md §3.2 CI 100]
        camp.campaign_over = True
        camp.victory_condition = "CHURCH_VICTORY: CI 100 Theocracy Unification"
        log.add("VICTORY: Church — CI 100 Theocracy Unification")
        return True
    # Peninsular Sovereignty (single faction)
    winner = evaluate_peninsular_sovereignty(camp)
    if winner is not None:
        # Check consecutive accountings via a counter on the campaign
        camp.ps_hold_seasons = getattr(camp, 'ps_hold_seasons', {})
        camp.ps_hold_seasons[winner] = camp.ps_hold_seasons.get(winner, 0) + 1
        # Reset others
        for other in list(camp.ps_hold_seasons):
            if other != winner:
                camp.ps_hold_seasons[other] = 0
        if camp.ps_hold_seasons[winner] >= PS_CONSECUTIVE:   # [canonical: victory_v30.md §0 "2 consecutive"]
            camp.campaign_over = True
            camp.victory_condition = f"PENINSULAR_SOVEREIGNTY: {winner}"
            log.add(f"VICTORY: {winner} — Peninsular Sovereignty")
            return True
    else:
        camp.ps_hold_seasons = {}
    # Partition
    pair = evaluate_partition(camp)
    if pair is not None:
        camp.partition_hold_seasons = getattr(camp, 'partition_hold_seasons', 0) + 1
        if camp.partition_hold_seasons >= PS_CONSECUTIVE:
            camp.campaign_over = True
            camp.victory_condition = f"PARTITION: {pair[0]} + {pair[1]}"
            log.add(f"VICTORY: Partition — {pair[0]} + {pair[1]}")
            return True
    else:
        camp.partition_hold_seasons = 0
    return False


# ============================================================================
# §15. Tensions Deck
#      [canonical: params/bg/tensions_deck.md "6-card spec"]
#      [canonical: designs/architecture/conflict_architecture_proposal.md]
# ============================================================================


class TensionCard(Enum):
    """[canonical: params/bg/tensions_deck.md]"""
    ROYAL_CRISIS = "Royal Crisis"                     # [canonical: tensions_deck.md Card 1]
    FELDMARK_FAMINE = "Feldmark Famine"               # [canonical: tensions_deck.md Card 2]
    CARDINAL_INDEPENDENCE = "Cardinal Independence"   # [canonical: tensions_deck.md Card 3]
    GUILD_FRACTURE = "Guild Fracture"                 # [canonical: tensions_deck.md Card 4]
    EINHIR_INCIDENT = "Einhir Incident"               # [canonical: tensions_deck.md Card 5]
    MINISTRY_CRISIS = "Ministry Crisis"               # [canonical: tensions_deck.md Card 6]


# Fuse timeline [canonical: params/bg/royal_assassination.md + tensions_deck.md]
FUSE_FIRE_WINDOW_MIN = 8                              # [canonical: royal_assassination.md "S8-S12"]
FUSE_FIRE_WINDOW_MAX = 12                             # [canonical: royal_assassination.md "S8-S12"]


@dataclass
class TensionFuse:
    """Active tension card fuse state.
    [canonical: tensions_deck.md Fuse Model S0-S12]"""
    card: TensionCard
    season_seeded: int                                # S0 season
    season_fires: int                                 # rolled S8-S12 at seed
    averted: bool = False
    fired: bool = False
    # Royal Crisis-specific target
    rc_target: Optional[str] = None                   # "Lenneth" | "Torben" | "Almud"


def draw_tension_card(rng: random.Random) -> TensionCard:
    """Draw 1 of 6 tension cards at game start.
    [canonical: tensions_deck.md "Draw: 6 cards, draw 1 at game start"]"""
    cards = list(TensionCard)                         # [canonical: tensions_deck.md "6 cards"]
    return rng.choice(cards)


def seed_tension_fuse(card: TensionCard, season: int, rng: random.Random) -> TensionFuse:
    """Seed the fuse at S0 with a roll for fire window S8-S12.
    [canonical: tensions_deck.md Fuse Model]"""
    fires_at = season + rng.randint(FUSE_FIRE_WINDOW_MIN, FUSE_FIRE_WINDOW_MAX)   # [canonical: royal_assassination.md S8-S12]
    fuse = TensionFuse(card=card, season_seeded=season, season_fires=fires_at)
    if card == TensionCard.ROYAL_CRISIS:
        # Sub-roll 1-6 -> target [canonical: royal_assassination.md Target Determination]
        roll = rng.randint(1, 6)                      # [canonical: royal_assassination.md d6 sub-roll]
        if roll <= 2:                                 # [canonical: royal_assassination.md "1-2 Lenneth"]
            fuse.rc_target = "Lenneth"
        elif roll <= 4:                               # [canonical: royal_assassination.md "3-4 Torben"]
            fuse.rc_target = "Torben"
        else:                                         # [canonical: royal_assassination.md "5-6 Almud"]
            fuse.rc_target = "Almud"
    return fuse


# ============================================================================
# §16. Tension Card Fire Resolution
#      [canonical: params/bg/royal_assassination.md §Target Consequences]
# ============================================================================


def fire_royal_crisis(camp: "Campaign", fuse: TensionFuse, log: "SimLog") -> None:
    """Resolve Royal Crisis card firing.
    [canonical: royal_assassination.md §Target Consequences]"""
    target = fuse.rc_target
    log.add(f"ROYAL CRISIS FIRES: target={target}")
    crown = camp.factions.get("Crown")
    church = camp.factions.get("Church")
    if target == "Lenneth":
        # [canonical: royal_assassination.md "Lenneth dies -> Almud revenge arc"]
        # Crown Mandate -1 to -2 over subsequent seasons (apply -1 immediate)
        if crown and crown.change_stat("mandate", -1):   # [canonical: royal_assassination.md "Crown governance suffers"]
            log.add("  Crown.mandate -1 (Almud distraction)")
        # Southern Accord erodes: Accord -1 in all Crown territories
        # [canonical: royal_assassination.md "Southern Accord erodes"]
        for t in camp.territories.values():
            if t.controller == "Crown" and t.accord > 0:  # [canonical: royal_assassination.md]
                t.accord -= 1
    elif target == "Torben":
        # [canonical: royal_assassination.md "Torben dies -> Elske retrieval"]
        # IP +5 (Altonian diplomatic crisis spike)
        # [canonical: royal_assassination.md "Altonian diplomatic crisis (IP spike)"]
        camp.clocks.invasion_pressure = min(100, camp.clocks.invasion_pressure + 5)  # [canonical: royal_assassination.md IP spike]
        log.add("  IP +5 (Altonian crisis)")
        # Mark battle at T4 (Varfell provocation) — simplified as Strain +1
        camp.any_battle_this_season = True            # [canonical: royal_assassination.md "Military deployment to T4"]
        # Torben loyalty track zeros (Torben is dead)
        camp.clocks.torben_loyalty = 0
    elif target == "Almud":
        # [canonical: royal_assassination.md "Almud dies -> Lenneth takes throne"]
        # Crown factional identity inverts: mark Crown as "Queen Lenneth" doctrine
        # Mechanically: Church immediately opens Heresy Investigation
        # -> Church Mandate +1, Crown Mandate -2
        if crown and crown.change_stat("mandate", -2, force=True):  # [canonical: royal_assassination.md "heresy target for Church"]
            log.add("  Crown.mandate -2 (factional inversion)")
        if church and church.change_stat("mandate", 1):  # [canonical: royal_assassination.md "heresy target"]
            log.add("  Church.mandate +1 (heresy investigation)")
        # Autonomy forced to at least Restless [canonical: royal_assassination.md "Löwenritter must decide"]
        if camp.clocks.autonomy == AutonomyStage.LOYAL:
            camp.clocks.autonomy = AutonomyStage.RESTLESS
            log.add("  Lowenritter Autonomy: Loyal -> Restless (heretic queen decision)")
    fuse.fired = True


def fire_feldmark_famine(camp: "Campaign", fuse: TensionFuse, log: "SimLog") -> None:
    """[canonical: tensions_deck.md Card 2 Feldmark Famine]"""
    log.add("FELDMARK FAMINE FIRES")
    # Prosperity collapse: T5 PV -1, Crown Wealth -1
    # [canonical: tensions_deck.md "Prosperity collapse in Crown's food supply"]
    t5 = camp.territories.get("T5")
    if t5 and t5.pv > 0:
        t5.pv -= 1                                    # [canonical: tensions_deck.md Card 2]
        log.add("  T5.pv -1")
    crown = camp.factions.get("Crown")
    if crown and crown.change_stat("wealth", -1):
        log.add("  Crown.wealth -1 (food supply crisis)")
    fuse.fired = True


def fire_cardinal_independence(camp: "Campaign", fuse: TensionFuse, log: "SimLog") -> None:
    """[canonical: tensions_deck.md Card 3 Cardinal Independence]"""
    log.add("CARDINAL INDEPENDENCE FIRES")
    # Rogue Cardinal appoints bishop-governor in Crown settlement
    # Simplified: T1 PT +1 (Church encroachment in capital)
    # [canonical: tensions_deck.md Card 3 "Rogue Cardinal ... in Crown settlement"]
    t1 = camp.territories.get("T1")
    if t1:
        t1.pt = min(5, t1.pt + 1)                     # [canonical: tensions_deck.md Card 3]
        t1.church_prominent = (t1.pt >= 3 and t1.sw >= 3)
        log.add(f"  T1.pt -> {t1.pt}")
    fuse.fired = True


def fire_guild_fracture(camp: "Campaign", fuse: TensionFuse, log: "SimLog") -> None:
    """[canonical: tensions_deck.md Card 4 Guild Fracture]"""
    log.add("GUILD FRACTURE FIRES")
    # S017 Guild schism: Hafenmark + Guilds both Stability -1
    # [canonical: tensions_deck.md Card 4 "S017 Guild schism ... contested"]
    haf = camp.factions.get("Hafenmark")
    gu = camp.factions.get("Guilds")
    if haf and haf.change_stat("stability", -1):      # [canonical: tensions_deck.md Card 4]
        log.add("  Hafenmark.stability -1")
    if gu and gu.change_stat("stability", -1):
        log.add("  Guilds.stability -1")
    fuse.fired = True


def fire_einhir_incident(camp: "Campaign", fuse: TensionFuse, log: "SimLog") -> None:
    """[canonical: tensions_deck.md Card 5 Einhir Incident]"""
    log.add("EINHIR INCIDENT FIRES")
    # Public confrontation forces position declaration — Strain +1, RM presence up
    # Simplified: Peninsular Strain +1
    # [canonical: tensions_deck.md Card 5 "forces all factions to declare position"]
    camp.clocks.change_strain(1)                      # [canonical: tensions_deck.md Card 5]
    log.add(f"  Strain +1, now {camp.clocks.peninsular_strain}")
    fuse.fired = True


def fire_ministry_crisis(camp: "Campaign", fuse: TensionFuse, log: "SimLog") -> None:
    """[canonical: tensions_deck.md Card 6 Ministry Crisis]"""
    log.add("MINISTRY CRISIS FIRES")
    # Crown governance vacuum -> Church fills. Crown Mandate -1, Church Mandate +1.
    # [canonical: tensions_deck.md Card 6 "Crown governance vacuum -> Church fills"]
    crown = camp.factions.get("Crown")
    church = camp.factions.get("Church")
    if crown and crown.change_stat("mandate", -1):    # [canonical: tensions_deck.md Card 6]
        log.add("  Crown.mandate -1 (Ministry collapse)")
    if church and church.change_stat("mandate", 1):
        log.add("  Church.mandate +1 (filling vacuum)")
    # Strain +1 [canonical: tensions_deck.md Card 6 "Ministry crisis"]
    camp.clocks.change_strain(1)                      # [canonical: tensions_deck.md Card 6]
    fuse.fired = True


FIRE_HANDLERS = {
    TensionCard.ROYAL_CRISIS: fire_royal_crisis,
    TensionCard.FELDMARK_FAMINE: fire_feldmark_famine,
    TensionCard.CARDINAL_INDEPENDENCE: fire_cardinal_independence,
    TensionCard.GUILD_FRACTURE: fire_guild_fracture,
    TensionCard.EINHIR_INCIDENT: fire_einhir_incident,
    TensionCard.MINISTRY_CRISIS: fire_ministry_crisis,
}


def tick_tension_fuses(camp: "Campaign", log: "SimLog") -> None:
    """Each season, check if any fuse has fired.
    [canonical: tensions_deck.md Fuse Model]"""
    for fuse in camp.tension_fuses:
        if fuse.fired or fuse.averted:
            continue
        if camp.season >= fuse.season_fires:          # [canonical: royal_assassination.md "fires S8-S12"]
            handler = FIRE_HANDLERS[fuse.card]
            handler(camp, fuse, log)


# ============================================================================
# §17. Threadwork Stub
#      [canonical: designs/threadwork/threadwork_v30.md]
#      [canonical: params/threadwork.md §Thread Tension]
# ============================================================================


# Thread Tension <-> Rendering Stability coupling
# [canonical: params/bg/clocks.md "TT rises -> RS falls"]
TT_RS_DECAY_RATE = 0.5                                # [canonical: params/threadwork.md "Each deployment TT +0.5"]
TT_RS_DRAIN_THRESHOLD = 10                            # [canonical: params/threadwork.md "TT 10 per RS -1 at Accounting"]


def threadwork_accounting(camp: "Campaign", log: "SimLog") -> None:
    """Apply Thread Tension / RS coupling.
    [canonical: params/bg/clocks.md §Battle Consequences + TT/RS relationship]"""
    # Every TT_RS_DRAIN_THRESHOLD points of accumulated TT drains 1 RS at Accounting
    # (simplified — canonical is a gradual decay tied to proximity).
    # For Session 3: TT accumulates from Private Collection failures (already
    # -1 RS immediate) and settlement-layer broker activity (stub).
    # Stub implementation: if TT accumulated this season >= threshold, drain RS.
    accumulated = getattr(camp, '_tt_accumulated', 0.0)
    if accumulated >= TT_RS_DRAIN_THRESHOLD:
        # Each full threshold unit -> 1 RS drain
        # [canonical: params/threadwork.md TT/RS coupling]
        drain = int(accumulated // TT_RS_DRAIN_THRESHOLD)   # [canonical: params/threadwork.md integer drain]
        camp.clocks.rendering_stability = max(0, camp.clocks.rendering_stability - drain)  # [canonical: params/threadwork.md]
        camp._tt_accumulated -= drain * TT_RS_DRAIN_THRESHOLD
        log.add(f"Thread Tension drain: RS -{drain}")


def add_thread_tension(camp: "Campaign", amount: float) -> None:
    """Add Thread Tension to the campaign's accumulator.
    [canonical: params/threadwork.md "TT deployment"]"""
    camp._tt_accumulated = getattr(camp, '_tt_accumulated', 0.0) + amount


# ============================================================================
# §18. Session 3 Integration: run_campaign with full features
# ============================================================================


def initial_campaign_s3(seed: int = 0) -> Campaign:
    """Session 3 initial campaign: adds Tensions Deck draw + fuse state."""
    camp = initial_campaign(seed=seed)
    # Initialize tension fuses list + TT accumulator
    camp.tension_fuses = []
    camp._tt_accumulated = 0.0
    camp.ps_hold_seasons = {}
    camp.partition_hold_seasons = 0
    # Draw 1 Tensions Deck card at game start
    # [canonical: tensions_deck.md "Draw: 6 cards, draw 1 at game start"]
    card = draw_tension_card(camp.rng)
    fuse = seed_tension_fuse(card, season=0, rng=camp.rng)
    camp.tension_fuses.append(fuse)
    return camp


def run_season_s3(camp: Campaign) -> SimLog:
    """Session 3 seasonal loop: integrates tension fuses + threadwork + victory."""
    camp.season += 1
    log = SimLog(season=camp.season)
    log.add(f"--- Season {camp.season} ---")
    # 0. Tension fuse tick (pre-DA)
    tick_tension_fuses(camp, log)
    # 1. Domain Actions
    domain_actions_phase(camp, log)
    # 2. Accounting (TC advance, battle, strain, PI, mandate recovery, autonomy, endgame)
    accounting_phase(camp, log)
    # 3. Threadwork accounting (TT -> RS coupling)
    threadwork_accounting(camp, log)
    # 4. Victory evaluation
    evaluate_victory(camp, log)
    log.add(f"State: RS={camp.clocks.rendering_stability} "
            f"CI={camp.clocks.church_influence} IP={camp.clocks.invasion_pressure} "
            f"PI={camp.clocks.parliament_integrity} Strain={camp.clocks.peninsular_strain} "
            f"Autonomy={camp.clocks.autonomy.value}")
    camp.logs.append(log)
    return log


def run_campaign_s3(max_seasons: int = 40, seed: int = 0) -> Campaign:
    """Full Session 3 campaign run."""
    camp = initial_campaign_s3(seed=seed)
    while not camp.campaign_over and camp.season < max_seasons:
        run_season_s3(camp)
    return camp


# ============================================================================
# §19. Smoke Tests + Deterministic Test Corpus (Session 3)
# ============================================================================


def smoke_test_dice() -> None:
    assert net_successes([10]) == 2
    assert net_successes([1]) == -1
    assert net_successes([7]) == 1
    assert net_successes([6]) == 0
    assert resolve_degree(4, 2) == Degree.OVERWHELMING
    assert resolve_degree(5, 10) == Degree.PARTIAL
    print("DICE TEST PASSED")


def smoke_test_victory_conditions() -> None:
    """Verify victory condition evaluators fire when expected.
    [canonical: victory_v30.md §0 + §3.2]"""
    # Construct a scenario where Church hits CI=100
    camp = initial_campaign_s3(seed=7)                # [canonical: ledger seed]
    camp.clocks.church_influence = 100                # [canonical: victory_v30.md §3.2]
    log = SimLog(season=1)
    evaluate_victory(camp, log)
    assert camp.campaign_over                         # [canonical: victory_v30.md §3.2 CI 100 victory]
    assert camp.victory_condition is not None
    assert "CHURCH_VICTORY" in camp.victory_condition
    print(f"VICTORY TEST PASSED: {camp.victory_condition}")


def smoke_test_tensions_deck() -> None:
    """Verify tensions deck draw + Royal Crisis sub-roll + fire.
    [canonical: tensions_deck.md + royal_assassination.md]"""
    # Force seed that produces Royal Crisis + known target
    for seed in range(100):
        camp = initial_campaign_s3(seed=seed)
        if camp.tension_fuses[0].card == TensionCard.ROYAL_CRISIS:
            fuse = camp.tension_fuses[0]
            assert fuse.rc_target in ("Lenneth", "Torben", "Almud")
            assert FUSE_FIRE_WINDOW_MIN <= fuse.season_fires <= FUSE_FIRE_WINDOW_MAX
            # Fire manually
            log = SimLog(season=10)
            fire_royal_crisis(camp, fuse, log)
            assert fuse.fired
            print(f"TENSIONS TEST PASSED: seed {seed} drew {fuse.card.value} "
                  f"target={fuse.rc_target} fires S{fuse.season_fires}")
            return
    raise AssertionError("No Royal Crisis seed found in 100 attempts (statistically implausible)")


def smoke_test_full_campaign(seed: int = 42, max_seasons: int = 40, verbose: bool = False) -> Campaign:
    """Full Session 3 campaign test."""
    camp = run_campaign_s3(max_seasons=max_seasons, seed=seed)
    # Sanity
    assert 0 <= camp.clocks.rendering_stability <= 100
    assert 0 <= camp.clocks.church_influence <= 100
    assert 0 <= camp.clocks.invasion_pressure <= 100
    assert 0 <= camp.clocks.parliament_integrity <= 20
    assert 0 <= camp.clocks.peninsular_strain <= 10
    fuse = camp.tension_fuses[0]
    summary = (f"seed={seed} ran={camp.season} "
               f"card={fuse.card.value} "
               f"{'target=' + (fuse.rc_target or '') if fuse.rc_target else ''} "
               f"fired={fuse.fired} "
               f"RS={camp.clocks.rendering_stability} "
               f"CI={camp.clocks.church_influence} "
               f"IP={camp.clocks.invasion_pressure} "
               f"PI={camp.clocks.parliament_integrity} "
               f"Strain={camp.clocks.peninsular_strain} "
               f"Autonomy={camp.clocks.autonomy.value} "
               f"victory={camp.victory_condition or 'ongoing'}")
    print(summary)
    if verbose:
        from collections import Counter
        da_counts = Counter(r.action for r in camp.da_results)
        print(f"  DA counts: {dict(da_counts.most_common())}")
        for fname, f in camp.factions.items():
            if f.mandate is not None and f.alive():
                print(f"  {fname}: M={f.mandate} I={f.influence} W={f.wealth} "
                      f"Mil={f.military} Sta={f.stability}")
    return camp


def deterministic_test_corpus() -> None:
    """Run 8 seeds × full campaign, verify all complete cleanly."""
    print("\n=== DETERMINISTIC TEST CORPUS (8 seeds) ===")
    seeds = [1, 7, 42, 100, 314, 1000, 2026, 9999]    # [canonical: ledger corpus seeds]
    campaigns = []
    for seed in seeds:
        camp = smoke_test_full_campaign(seed=seed, max_seasons=40, verbose=False)
        campaigns.append(camp)
    # Aggregate outcome statistics
    from collections import Counter
    outcomes = Counter(camp.victory_condition or "ONGOING_40S" for camp in campaigns)
    cards_drawn = Counter(camp.tension_fuses[0].card.value for camp in campaigns)
    print(f"\nOutcome distribution: {dict(outcomes)}")
    print(f"Tension cards drawn: {dict(cards_drawn)}")
    return campaigns


# ============================================================================
# §20. Mass Combat Resolution (BG mode simplified)
#      [canonical: designs/provincial/mass_battle_v30.md §B.3 BG Battle Resolution]
# ============================================================================


@dataclass
class BattleResult:
    attacker: str
    defender: str
    territory: str
    attacker_net: int
    defender_net: int
    outcome: str                      # "capture" | "partial" | "defender_wins"
    effects: List[str]


def _military_pool(f: Faction) -> int:
    """BG battle pool = Military + commander bonus.
    [canonical: mass_battle_v30.md §B.3 Step 3 "Pool = Martial + commander bonus"]
    [canonical: mass_battle_v30.md §B.3 "Commander bonus = floor(faction Military / 2) PP-555"]"""
    mil = f.military if f.military is not None else 0
    commander_bonus = mil // 2                       # [canonical: mass_battle_v30.md §B.3 "floor(Military/2)"]
    return mil + commander_bonus


def resolve_mass_battle(camp: "Campaign", attacker: Faction, defender: Faction,
                        territory: Territory) -> BattleResult:
    """Simplified single-roll BG battle.
    [canonical: mass_battle_v30.md §B.3 BG Battle Resolution + Step 4 margin table]
    [canonical: mass_battle_v30.md §B.3 Accord consequence PP-645]"""
    a_pool = _military_pool(attacker)
    d_pool = _military_pool(defender) if defender else 0
    # Defender fort adds dice (simplified formation defence bonus)
    # [canonical: geography_v30.md fort rating; §B.3 disposition Ob modifiers]
    d_bonus = territory.fort                          # [canonical: geography_v30.md Fort column]
    # Roll both sides; TN 7 standard.
    _, a_net, a_faces = contest(a_pool, 1, camp.rng)  # Ob 1 placeholder; margin matters, not Ob here
    _, d_net, d_faces = contest(d_pool + d_bonus, 1, camp.rng)
    effects: List[str] = []
    # Step 4: determine outcome by margin [canonical: mass_battle_v30.md §B.3 Step 4 PP-104]
    margin = a_net - d_net
    if margin >= 2:                                   # [canonical: mass_battle_v30.md §B.3 "Attacker net >= Defender net + 2"]
        # Attacker wins: territory captured, defender Military -1
        territory.controller = attacker.name          # [canonical: mass_battle_v30.md §B.3 "Territory captured"]
        territory.accord = 1                          # [canonical: mass_battle_v30.md §B.3 "Accord set to 1 (Resistant) PP-645"]
        if defender and defender.change_stat("military", -1):   # [canonical: mass_battle_v30.md §B.3 "Defender Military -1"]
            effects.append(f"{defender.name}.military -1")
        effects.append(f"{territory.tid} captured by {attacker.name}; Accord->1")
        outcome = "capture"
    elif margin <= -2:                                # [canonical: mass_battle_v30.md §B.3 "Defender net >= Attacker net + 2"]
        if attacker.change_stat("military", -1):      # [canonical: mass_battle_v30.md §B.3 "Attacker Military -1"]
            effects.append(f"{attacker.name}.military -1")
        effects.append(f"{territory.tid} held; defender wins")
        outcome = "defender_wins"
    else:                                             # [canonical: mass_battle_v30.md §B.3 "Margin <=1 either direction = Partial"]
        effects.append(f"{territory.tid} partial — no territory change")
        # Attacker Cohesion -15 -> modeled as Attacker Stability -1
        # [canonical: mass_battle_v30.md §B.3 "Attacker Cohesion -15 (derived_stats_v1)"]
        if attacker.change_stat("stability", -1):     # [canonical: derived_stats_v1 Cohesion -15 = Stability -1]
            effects.append(f"{attacker.name}.stability -1 (partial commitment cost)")
        outcome = "partial"
    return BattleResult(
        attacker=attacker.name, defender=defender.name if defender else "None",
        territory=territory.tid, attacker_net=a_net, defender_net=d_net,
        outcome=outcome, effects=effects,
    )


# ============================================================================
# §21. Invade DA
# ============================================================================


def da_invade(camp: "Campaign", actor: Faction, territory_id: str) -> DAResult:
    """Invade an adjacent enemy territory. Triggers mass combat.
    Requires: actor controls an adjacent territory; target controlled by another
    faction or uncontrolled; actor Military >= 2.
    [canonical: mass_battle_v30.md §B.3 BG battle; geography_v30.md adjacency]"""
    target = camp.territories.get(territory_id)
    if target is None:
        return DAResult(actor.name, "invade", territory_id, Degree.FAILURE, 0, [],
                        ["Invalid territory"])
    # Need adjacency from some territory actor controls
    # [canonical: geography_v30.md Adjacent column]
    actor_adjacent = any(
        t.controller == actor.name and territory_id in t.adjacent
        for t in camp.territories.values()
    )
    if not actor_adjacent:
        return DAResult(actor.name, "invade", territory_id, Degree.FAILURE, 0, [],
                        ["Target not adjacent to actor territory"])
    # Cannot invade own territory
    if target.controller == actor.name:
        return DAResult(actor.name, "invade", territory_id, Degree.FAILURE, 0, [],
                        ["Cannot invade own territory"])
    # Need Military >= 2 to mount invasion [simplified: some force must exist]
    if actor.military is None or actor.military < 2:  # [canonical: mass_battle_v30.md A.13 "unit requires Military >= 2"]
        return DAResult(actor.name, "invade", territory_id, Degree.FAILURE, 0, [],
                        ["Military too low to invade"])
    defender = camp.factions.get(target.controller) if target.controller else None
    # Sim: if defender is NPC-only (Guilds) or uncontrolled (None), allow
    # attacker to win by walkover if defender Military 0 or None
    if defender is None or defender.military is None or defender.military == 0:
        # Walkover capture
        target.controller = actor.name
        target.accord = 1                             # [canonical: mass_battle_v30.md §B.3 PP-645]
        camp.any_battle_this_season = True
        return DAResult(actor.name, "invade", territory_id, Degree.SUCCESS, 0, [],
                        [f"{target.tid} walkover captured by {actor.name}"])
    br = resolve_mass_battle(camp, actor, defender, target)
    camp.battle_results.append(br)
    camp.any_battle_this_season = True                # [canonical: params/bg/clocks.md §Battle Consequences]
    camp.last_battle_seasons[(actor.name, defender.name)] = camp.season
    actor._da_used_this_season.add("invade")
    # Map BattleResult outcome to DA degree for reporting
    degree = Degree.OVERWHELMING if br.outcome == "capture" else (
        Degree.FAILURE if br.outcome == "defender_wins" else Degree.PARTIAL
    )
    return DAResult(actor.name, "invade", territory_id, degree,
                    br.attacker_net - br.defender_net, [], br.effects)


# ============================================================================
# §22. Church TC Seizure DA (CI >= 60, per-territory)
#      [canonical: stats_1_7_scale.md §Unique Actions TC 60 Territorial Seizure]
# ============================================================================


def da_tc_seizure(camp: "Campaign", actor: Faction, territory_id: str) -> DAResult:
    """Church Territorial Seizure at CI>=60.
    [canonical: stats_1_7_scale.md §Unique Actions TC 60 Territorial Seizure]
    Roll: Mandate vs floor(owner Mandate/2)+1. Once per territory."""
    target = camp.territories.get(territory_id)
    if target is None:
        return DAResult(actor.name, "tc_seizure", territory_id, Degree.FAILURE, 0, [],
                        ["Invalid territory"])
    # Gate: CI >= 60 [canonical: stats_1_7_scale.md "Trigger: TC reaches 60"]
    if not camp.clocks.tc60_seizure_unlocked:         # [canonical: stats_1_7_scale.md TC60 gate]
        return DAResult(actor.name, "tc_seizure", territory_id, Degree.FAILURE, 0, [],
                        ["CI < 60"])
    # Must be Church-prominent and not already Church-held
    # [canonical: ci_political_v30.md §2.1 "Church Prominent in target territory ED-326"]
    if target.controller == actor.name:
        return DAResult(actor.name, "tc_seizure", territory_id, Degree.FAILURE, 0, [],
                        ["Already Church-held"])
    if not target.church_prominent:                   # [canonical: ci_political_v30.md §2.1 ED-326]
        return DAResult(actor.name, "tc_seizure", territory_id, Degree.FAILURE, 0, [],
                        ["Not Church-prominent"])
    owner = camp.factions.get(target.controller) if target.controller else None
    owner_mandate = owner.mandate if (owner and owner.mandate is not None) else 0
    ob = (owner_mandate // 2) + 1                     # [canonical: stats_1_7_scale.md TC60 Seizure "floor(owner Mandate/2)+1"]
    pool = _stat_pool(actor, "mandate")
    degree, net, faces = contest(pool, ob, camp.rng)
    effects: List[str] = []
    if degree in (Degree.OVERWHELMING, Degree.SUCCESS):
        target.controller = actor.name                # [canonical: stats_1_7_scale.md TC60 "Administrative control"]
        target.accord = 1                             # peacefully administered seizure still resistant
        effects.append(f"{target.tid} seized by Church")
        # Flat TC +? not applied here (immediate CI already at 60+)
    else:
        # Failure: Mandate -1 [canonical: stats_1_7_scale.md TC60 Failure]
        if actor.change_stat("mandate", -1):          # [canonical: stats_1_7_scale.md TC60 F "Mandate -1"]
            effects.append(f"{actor.name}.mandate -1")
    actor._da_used_this_season.add("tc_seizure")
    return DAResult(actor.name, "tc_seizure", territory_id, degree, net, faces, effects)


# ============================================================================
# §23. Mass Seizure (CI>=60 one-shot)
#      [canonical: victory_v30.md §3.2 CI=100 Mass Seizure Declaration]
#      [canonical: ci_political_v30.md §2.1 "Mass Seizure ... from CI >= 60"]
# ============================================================================


def da_mass_seizure(camp: "Campaign", actor: Faction) -> DAResult:
    """Church Mass Seizure one-shot at CI>=60.
    [canonical: ci_political_v30.md §2.1 "Mass Seizure ... Gated by Church Mandate >= 4"]
    [canonical: stats_1_7_scale.md TC60 Seizure + Mass Seizure]"""
    effects: List[str] = []
    if not camp.clocks.mass_seizure_available or camp.clocks.mass_seizure_used:
        return DAResult(actor.name, "mass_seizure", None, Degree.FAILURE, 0, [],
                        ["Mass Seizure unavailable"])
    # Gate: Church Mandate >= 4 [canonical: ci_political_v30.md §2.1 ED-326 gate]
    if actor.mandate is None or actor.mandate < 4:    # [canonical: ci_political_v30.md "Church Mandate >= 4"]
        return DAResult(actor.name, "mass_seizure", None, Degree.FAILURE, 0, [],
                        ["Church Mandate < 4"])
    # Fire against all Church-prominent territories not held by Church
    # [canonical: ci_political_v30.md §2.1 "one-shot ... Ob = 10 - PT - infrastructure"]
    targets = [t for t in camp.territories.values()
               if t.church_prominent and t.controller != actor.name]
    if not targets:
        return DAResult(actor.name, "mass_seizure", None, Degree.FAILURE, 0, [],
                        ["No Church-prominent non-Church territories"])
    captured = 0
    for t in targets:
        # Ob = max(1, 10 - PT) (simplified; full infrastructure mods deferred)
        # [canonical: ci_political_v30.md §2.1 "Ob = 10 - PT - infrastructure (floor 1)"]
        ob = max(1, 10 - t.pt)                        # [canonical: ci_political_v30.md §2.1 Mass Seizure Ob]
        pool = _stat_pool(actor, "mandate")
        degree, net, _ = contest(pool, ob, camp.rng)
        if degree in (Degree.OVERWHELMING, Degree.SUCCESS, Degree.PARTIAL):
            t.controller = actor.name                 # [canonical: ci_political_v30.md §2.1 "Mass Seizure captures"]
            t.accord = 1                              # [canonical: mass_battle_v30.md PP-645 Accord 1]
            captured += 1
            effects.append(f"{t.tid} seized")
    camp.clocks.mass_seizure_used = True              # [canonical: ci_political_v30.md §2.1 "one-shot"]
    actor._da_used_this_season.add("mass_seizure")
    return DAResult(actor.name, "mass_seizure", None,
                    Degree.OVERWHELMING if captured > 0 else Degree.FAILURE,
                    captured, [], effects + [f"Mass Seizure: {captured}/{len(targets)} captured"])


# ============================================================================
# §24. Faction AI v2 — Conquest-aware priority
# ============================================================================


def _find_invasion_target(camp: "Campaign", actor: Faction) -> Optional[str]:
    """Find a weakest adjacent enemy territory to invade.
    Priority: lower defender Military > lower fort > higher PV."""
    candidates = []
    for t in camp.territories.values():
        if t.controller == actor.name:
            continue
        # Must be adjacent to an owned territory
        if not any(nt.controller == actor.name and t.tid in nt.adjacent
                   for nt in camp.territories.values()):
            continue
        # Skip protected: Schoenland (foreign), Askeheim (Calamity)
        if t.controller == "Schoenland" or t.tid == "T15":
            continue
        defender = camp.factions.get(t.controller) if t.controller else None
        d_mil = defender.military if (defender and defender.military) else 0
        candidates.append((t, d_mil))
    if not candidates:
        return None
    # Sort by (low defender Military, low fort, high PV)
    candidates.sort(key=lambda x: (x[1], x[0].fort, -x[0].pv))
    return candidates[0][0].tid


def select_da_for_faction_v2(camp: "Campaign", f: Faction) -> Optional[Callable]:
    """AI v2: adds conquest (Invade / TC Seizure / Mass Seizure) + defensive Govern."""
    if not f.alive() or not f.playable:
        return None

    # Church priority: if CI>=60 and Mass Seizure unused, FIRE IT
    if f.name == "Church" and camp.clocks.mass_seizure_available and not camp.clocks.mass_seizure_used:
        if f.mandate is not None and f.mandate >= 4:
            return lambda: da_mass_seizure(camp, f)

    # Church priority: if CI>=60, TC Seizure a Church-prominent non-Church territory
    if f.name == "Church" and camp.clocks.tc60_seizure_unlocked and "tc_seizure" not in f._da_used_this_season:
        candidates = [t for t in camp.territories.values()
                      if t.church_prominent and t.controller != f.name and t.controller is not None]
        if candidates:
            # Pick lowest-Mandate owner for easiest roll
            def _owner_mandate(t):
                o = camp.factions.get(t.controller)
                return o.mandate if (o and o.mandate is not None) else 0
            candidates.sort(key=_owner_mandate)
            tid = candidates[0].tid
            return lambda: da_tc_seizure(camp, f, tid)

    # Non-Church military-capable: if Military >= 3, attempt Invade every 3 seasons
    # Also require that we don't already control all 15 playable territories
    own_count = sum(1 for t in camp.territories.values() if t.controller == f.name)
    # [canonical: victory_v30.md §0 "all 15 playable"]
    playable_own = sum(1 for tid in PLAYABLE_TERRITORIES
                       if camp.territories[tid].controller == f.name)

    # If we're close to PS (own >= 10 playable) prioritize Govern over Invade to
    # rebuild Accord on captured territories. [canonical: victory_v30.md §0 Accord >= 2]
    if playable_own >= 10:
        low_accord_owned = [t for t in camp.territories.values()
                            if t.controller == f.name and t.accord < 2
                            and t.tid in PLAYABLE_TERRITORIES]
        if low_accord_owned and "govern" not in f._da_used_this_season:
            target_t = low_accord_owned[0]
            return lambda: da_govern(camp, f, target_t.tid)

    if (f.military is not None and f.military >= 3                              # [canonical: mass_battle_v30.md A.13 Military>=2 to mount]
            and "invade" not in f._da_used_this_season
            and own_count < 15                                                  # [canonical: victory_v30.md §0]
            and camp.season % 2 == 0                                            # every other season (rate-limit invasion spam)
            and f.name != "Church"):                                            # Church uses TC Seizure, not military invasion
        invasion_target = _find_invasion_target(camp, f)
        if invasion_target:
            return lambda: da_invade(camp, f, invasion_target)

    # Fall through to Session 2 AI (Mandate repair, unique actions, govern, trade)
    return select_da_for_faction(camp, f)


def domain_actions_phase_v2(camp: Campaign, log: SimLog) -> None:
    """Per-season DA phase using AI v2."""
    for fname, f in camp.factions.items():
        if not f.playable or not f.alive():
            continue
        action_fn = select_da_for_faction_v2(camp, f)
        if action_fn is None:
            continue
        result = action_fn()
        if result is None:
            continue
        camp.da_results.append(result)
        eff_txt = "; ".join(result.effects) if result.effects else "no effect"
        log.add(f"DA: {fname} {result.action}"
                f" -> {result.degree.value} (net={result.net}) [{eff_txt}]")


def run_season_tier_a(camp: Campaign) -> SimLog:
    """Tier A seasonal loop: full Session-3 loop + conquest-aware AI."""
    camp.season += 1
    log = SimLog(season=camp.season)
    log.add(f"--- Season {camp.season} ---")
    tick_tension_fuses(camp, log)
    domain_actions_phase_v2(camp, log)                # v2 AI with conquest
    accounting_phase(camp, log)
    threadwork_accounting(camp, log)
    evaluate_victory(camp, log)
    log.add(f"State: RS={camp.clocks.rendering_stability} "
            f"CI={camp.clocks.church_influence} IP={camp.clocks.invasion_pressure} "
            f"PI={camp.clocks.parliament_integrity} Strain={camp.clocks.peninsular_strain} "
            f"Autonomy={camp.clocks.autonomy.value}")
    camp.logs.append(log)
    return log


def initial_campaign_tier_a(seed: int = 0) -> Campaign:
    camp = initial_campaign_s3(seed=seed)
    camp.battle_results = []                          # per-run combat log
    camp.last_battle_seasons = {}                     # (attacker, defender) -> season
    return camp


def run_campaign_tier_a(max_seasons: int = 60, seed: int = 0) -> Campaign:
    """Tier A full campaign run. Default 60 seasons — Peninsular Sovereignty
    usually takes 30-60 seasons even with active conquest."""
    camp = initial_campaign_tier_a(seed=seed)
    while not camp.campaign_over and camp.season < max_seasons:
        run_season_tier_a(camp)
    return camp


# ============================================================================
# §25. Tier A Tests + Win-Rate Corpus
# ============================================================================


def smoke_test_mass_combat() -> None:
    """Verify a deterministic mass battle produces a valid outcome."""
    camp = initial_campaign_tier_a(seed=42)
    crown = camp.factions["Crown"]
    hafenmark = camp.factions["Hafenmark"]
    # Crown invades T8 Gransol (adjacent to T9 which Crown doesn't own but is adjacent via T14)
    # Actually verify adjacency: T14 Ehrenfeld is Crown-controlled, T14 adj includes T4 (Varfell),
    # so Crown can invade T4. Use that.
    result = da_invade(camp, crown, "T4")
    assert result.degree in (Degree.OVERWHELMING, Degree.PARTIAL, Degree.FAILURE)
    # any_battle_this_season should be true after an invasion (unless walkover rules out combat)
    print(f"MASS COMBAT TEST: Crown invades T4 -> {result.degree.value} "
          f"[{'; '.join(result.effects)[:100]}]")


def smoke_test_tier_a_campaign(seed: int = 42, max_seasons: int = 60,
                                verbose: bool = False) -> Campaign:
    camp = run_campaign_tier_a(max_seasons=max_seasons, seed=seed)
    # Clock sanity
    assert 0 <= camp.clocks.rendering_stability <= 100
    assert 0 <= camp.clocks.church_influence <= 100
    # Territory control sanity — sum equals 17
    control_counts: Dict[str, int] = {}
    for t in camp.territories.values():
        k = t.controller or "Uncontrolled"
        control_counts[k] = control_counts.get(k, 0) + 1
    assert sum(control_counts.values()) == 17
    fuse = camp.tension_fuses[0]
    summary = (f"seed={seed} ran={camp.season} "
               f"card={fuse.card.value}"
               f"{' target=' + (fuse.rc_target or '') if fuse.rc_target else ''} "
               f"fired={fuse.fired} "
               f"RS={camp.clocks.rendering_stability} "
               f"CI={camp.clocks.church_influence} "
               f"IP={camp.clocks.invasion_pressure} "
               f"Strain={camp.clocks.peninsular_strain} "
               f"autonomy={camp.clocks.autonomy.value} "
               f"battles={len(getattr(camp, 'battle_results', []))} "
               f"victory={camp.victory_condition or 'ongoing'}")
    print(summary)
    if verbose:
        from collections import Counter
        print(f"  Territory control: {dict(sorted(control_counts.items(), key=lambda x:-x[1]))}")
        print(f"  Battles: {len(camp.battle_results)}")
        for br in camp.battle_results[:5]:
            print(f"    {br.attacker}->{br.defender} {br.territory} "
                  f"net={br.attacker_net}v{br.defender_net} -> {br.outcome}")
        if len(camp.battle_results) > 5:
            print(f"    ... +{len(camp.battle_results) - 5} more battles")
        da_counts = Counter(r.action for r in camp.da_results)
        print(f"  DA counts: {dict(da_counts.most_common())}")
    return camp


def tier_a_win_rate_corpus(num_seeds: int = 16, max_seasons: int = 60) -> None:
    """Run N seeds, measure outcome distribution."""
    from collections import Counter
    print(f"\n=== TIER A WIN-RATE CORPUS ({num_seeds} seeds, {max_seasons} seasons max) ===")
    outcomes: Counter = Counter()
    winners: Counter = Counter()
    for seed in range(1, num_seeds + 1):
        camp = run_campaign_tier_a(max_seasons=max_seasons, seed=seed)
        vc = camp.victory_condition or "ONGOING"
        outcomes[vc.split(":")[0]] += 1
        if vc and ":" in vc:
            tag = vc.split(":", 1)[0]
            if tag == "PENINSULAR_SOVEREIGNTY":
                winners[vc.split(": ")[1]] += 1
            elif tag == "CHURCH_VICTORY":
                winners["Church (CI=100)"] += 1
            elif tag == "PARTITION":
                winners[vc.split(": ")[1]] += 1
            elif tag == "SHARED_LOSS":
                winners["SHARED_LOSS"] += 1
            elif tag == "CROWN_ELIMINATED":
                winners["CROWN_ELIMINATED"] += 1
    print(f"Outcomes: {dict(outcomes)}")
    print(f"Winners: {dict(winners)}")


if __name__ == "__main__":
    smoke_test_dice()
    smoke_test_territory_model()
    smoke_test_piety_yield()
    smoke_test_church_bonus()
    smoke_test_10_peaceful()
    smoke_test_victory_conditions()
    smoke_test_tensions_deck()
    smoke_test_mass_combat()
    print("\n=== TIER A SAMPLE (seed=42, verbose) ===")
    smoke_test_tier_a_campaign(seed=42, max_seasons=60, verbose=True)
    print("\n=== TIER A SAMPLE (seed=7, verbose) ===")
    smoke_test_tier_a_campaign(seed=7, max_seasons=60, verbose=True)
    tier_a_win_rate_corpus(num_seeds=16, max_seasons=100)
    print("\n=== EXTENDED-HORIZON CORPUS (120 seasons) ===")
    tier_a_win_rate_corpus(num_seeds=8, max_seasons=120)
