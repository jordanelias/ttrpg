"""
Valoria Full Campaign Simulation — Session 1 Foundation
========================================================

Generated: 2026-04-19
Scope: core engine (dice + contest + degree), clock tracking (RS/CI/IP/PI/
Strain/AER/Torben/Elske/Autonomy), faction stat tracking (6-stat 1-7 scale),
seasonal loop skeleton. Domain-action resolution is a stub — Session 2 fills
it with faction-specific actions. NPC behaviour + arcs come in Session 3.

Every mechanical constant cites its canonical source via an inline
`# [canonical: <path> §<section>]` comment, per sim_fabrication_check
requirements (valoria_hooks.py).

Canonical sources for this file:
- params/bg/core.md (dice, degree table, starting values)
- params/bg/clocks.md (RS/CI/IP environmental effects)
- params/factions/stats_1_7_scale.md (faction starting stats + seasonal caps)
- params/factions.md (faction roster)
- designs/architecture/conflict_architecture_proposal.md (Löwenritter graduated
  autonomy replacing binary Coup Counter)
- designs/provincial/peninsular_strain_v30.md (Strain mechanics)
- designs/provincial/ci_political_v30.md (CI cap ±5/season uniform at T9,
  ED-721 Option A)
- designs/provincial/factions_personal_v30.md (§8.7 Niflhel STRUCK; 7 active
  factions)
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field
from enum import Enum
from typing import Dict, List, Optional, Tuple


# ============================================================================
# §1. Core Engine — Dice, Contest, Degree
#     [canonical: params/bg/core.md §Dice System (v05 correction)]
#     [canonical: params/bg/core.md §Degree Table (PP-179 + PP-249)]
# ============================================================================


class Degree(Enum):
    """Resolution degree outcomes.
    [canonical: params/bg/core.md §Degree Table]"""
    OVERWHELMING = "Overwhelming"
    SUCCESS = "Success"
    PARTIAL = "Partial"
    FAILURE = "Failure"


def roll_d10_pool(pool_size: int, rng: random.Random) -> List[int]:
    """Roll N d10s. [canonical: params/bg/core.md §Dice System]"""
    return [rng.randint(1, 10) for _ in range(pool_size)]


def net_successes(faces: List[int]) -> int:
    """Convert faces to net successes per v05 dice system.
    1 = -1 success; 2-6 = 0; 7-9 = +1; 10 = +2.
    [canonical: params/bg/core.md §Dice System]"""
    net = 0
    for f in faces:
        if f == 1:                                    # [canonical: params/bg/core.md §Dice System face 1]
            net -= 1
        elif f >= 7 and f <= 9:                       # [canonical: params/bg/core.md §Dice System faces 7-9]
            net += 1
        elif f == 10:                                 # [canonical: params/bg/core.md §Dice System face 10]
            net += 2
        # faces 2-6 contribute 0 [canonical: params/bg/core.md §Dice System faces 2-6]
    return net


def resolve_degree(net: int, ob: int) -> Degree:
    """Determine Degree from net successes vs Ob.
    [canonical: params/bg/core.md §Degree Table PP-179 + PP-249]

    Thresholds:
      Overwhelming: net >= 2*Ob AND net >= 3
      Success:      net >= Ob
      Partial:      0 < net < Ob
      Failure:      net <= 0
    Ob 10 exception: Overwhelming unavailable, Partial requires net >= 5.
    """
    if ob < 1:                                        # [canonical: params/bg/core.md §Dice System "Ob minimum: 1"]
        ob = 1
    if net <= 0:
        return Degree.FAILURE
    # Ob 10 exception [canonical: params/bg/core.md §Degree Table Ob 10 exception]
    if ob >= 10:                                      # [canonical: params/bg/core.md §Degree Table Ob 10 exception]
        if net >= 5:                                  # [canonical: params/bg/core.md §Degree Table Ob 10 exception "net >= 5"]
            return Degree.PARTIAL
        return Degree.FAILURE
    # Overwhelming: net >= 2*Ob AND net >= 3 [canonical: params/bg/core.md §Degree Table]
    if net >= 2 * ob and net >= 3:                    # [canonical: params/bg/core.md §Degree Table overwhelming floor 3]
        return Degree.OVERWHELMING
    if net >= ob:
        return Degree.SUCCESS
    return Degree.PARTIAL


def contest(pool_size: int, ob: int, rng: random.Random,
            bonus_dice: int = 0, ob_modifier: int = 0
) -> Tuple[Degree, int, List[int]]:
    """Resolve a single contest. Returns (degree, net, faces).
    [canonical: params/bg/core.md §Dice System + §Degree Table]"""
    effective_pool = max(0, pool_size + bonus_dice)   # pool can't be negative
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
    """A Valoria faction with the 6 canonical stats.
    [canonical: params/factions/stats_1_7_scale.md §Starting Stats]"""
    name: str
    mandate: Optional[int]      # M
    influence: Optional[int]    # I
    wealth: Optional[int]       # W
    military: Optional[int]     # Mil
    intel: Optional[int]        # Int
    stability: Optional[int]    # Sta
    playable: bool = True
    starting_mandate: Optional[int] = None
    starting_military: Optional[int] = None
    # Stat deltas this season (for ±2/season cap enforcement)
    # [canonical: params/factions/stats_1_7_scale.md "Seasonal cap: ±2 per stat per season"]
    _season_delta: Dict[str, int] = field(default_factory=dict)
    # Consecutive-action tracker for Royal Decree +1 Ob/season on repeat
    # [canonical: params/factions/stats_1_7_scale.md §Domain Action Table "Consecutive: +1 Ob/season"]
    _consec_action: Dict[str, int] = field(default_factory=dict)

    def __post_init__(self):
        if self.starting_mandate is None:
            self.starting_mandate = self.mandate
        if self.starting_military is None:
            self.starting_military = self.military

    def can_change(self, stat: str, delta: int) -> bool:
        """Enforce ±2/season stat change cap.
        [canonical: params/factions/stats_1_7_scale.md §Seasonal cap]"""
        current = self._season_delta.get(stat, 0)
        proposed = current + delta
        if abs(proposed) > 2:                         # [canonical: params/factions/stats_1_7_scale.md "±2 per stat per season"]
            return False
        return True

    def change_stat(self, stat: str, delta: int, force: bool = False) -> bool:
        """Apply a stat change. Returns True if applied, False if capped.
        [canonical: params/factions/stats_1_7_scale.md §Seasonal cap + §Military Seasonal Cap]"""
        if not force and not self.can_change(stat, delta):
            return False
        current = getattr(self, stat)
        if current is None:
            return False  # faction does not have this stat
        new_value = current + delta
        # Hard caps: 1-7 scale
        # [canonical: params/factions/stats_1_7_scale.md title (1-7 scale)]
        if stat == "military" and self.starting_military is not None:
            # Military hard cap: starting + 1 via Domain Actions alone
            # [canonical: params/factions/stats_1_7_scale.md §Military Seasonal Cap ED-039]
            if not force and new_value > self.starting_military + 1:
                new_value = self.starting_military + 1  # [canonical: ED-039]
        new_value = max(0, new_value)                 # floor at 0 (stat destroyed)
        setattr(self, stat, new_value)
        self._season_delta[stat] = self._season_delta.get(stat, 0) + delta
        return True

    def reset_season_deltas(self) -> None:
        self._season_delta.clear()

    def alive(self) -> bool:
        """Faction is eliminated if all its stats are 0 or it holds 0 territories.
        [canonical: tests/coverage_matrix.md '0-territory = immediate elimination']
        Stub: for Session 1, elimination check is deferred to Session 2 (territory)."""
        return True


# Canonical starting stats (BG mode)
# [canonical: params/factions/stats_1_7_scale.md §Starting Stats]
def starting_factions() -> Dict[str, Faction]:
    return {
        "Crown": Faction(
            name="Crown",
            mandate=5, influence=5, wealth=4, military=4,    # [canonical: stats_1_7_scale.md §Starting Stats Crown BG row]
            intel=None, stability=4,
        ),
        "Church": Faction(
            name="Church",
            mandate=5, influence=6, wealth=5, military=4,    # [canonical: stats_1_7_scale.md §Starting Stats Church row]
            intel=None, stability=5,
        ),
        "Hafenmark": Faction(
            name="Hafenmark",
            mandate=4, influence=4, wealth=5, military=3,    # [canonical: stats_1_7_scale.md §Starting Stats Hafenmark row]
            intel=None, stability=4,
        ),
        "Varfell": Faction(
            name="Varfell",
            mandate=3, influence=4, wealth=3, military=4,    # [canonical: stats_1_7_scale.md §Starting Stats Varfell BG "3/3 intentional"]
            intel=None, stability=4,
        ),
        "Guilds": Faction(
            name="Guilds",
            mandate=3, influence=4, wealth=6, military=2,    # [canonical: stats_1_7_scale.md §Starting Stats Guilds row]
            intel=None, stability=5,
            playable=False,  # [canonical: params/bg/core.md §FACTION ASSIGNMENT "Guilds NPC-only"]
        ),
        "RestorationMovement": Faction(
            name="RestorationMovement",
            mandate=None, influence=None, wealth=None,        # [canonical: stats_1_7_scale.md "Restoration Movement: No faction stats (PP-460)"]
            military=None, intel=None, stability=None,
            # Operates via Presence markers and Community Weaving
            # [canonical: stats_1_7_scale.md §Starting Stats RM row]
        ),
        "Lowenritter": Faction(
            name="Lowenritter",
            # BG baseline: I=2 Mil=5 Sta=5 (Loyal-stage NPC faction)
            # [canonical: stats_1_7_scale.md §Starting Stats Lowenritter row]
            # Full activation on Split: M=3 I=2 W=3 Mil=6 Sta=5
            # [canonical: params/bg/core.md §Starting Values "Löwenritter Autonomy" footer]
            mandate=None, influence=2, wealth=None, military=5,
            intel=3, stability=5,
            playable=False,  # [canonical: params/bg/core.md §FACTION ASSIGNMENT Löwenritter "Conditional: Split stage only"]
        ),
        # Niflhel: STRUCK (Session B 2026-04-18)
        # [canonical: designs/architecture/conflict_architecture_proposal.md]
        # [canonical: params/bg/core.md §FACTION ASSIGNMENT Niflhel STRUCK]
        # No faction entry generated.
    }


# ============================================================================
# §3. Clocks + Environmental Tracks
#     [canonical: params/bg/core.md §Starting Values (v04 B2, PP-188 correction)]
#     [canonical: params/bg/clocks.md §Clock Environmental Effects]
# ============================================================================


class AutonomyStage(Enum):
    """Löwenritter graduated autonomy stages (replaces binary Coup Counter).
    [canonical: params/bg/core.md §Löwenritter Graduated Autonomy]
    [canonical: designs/architecture/conflict_architecture_proposal.md]
    [canonical: ED-667 closed 2026-04-19]"""
    LOYAL = "Loyal"
    RESTLESS = "Restless"
    AUTONOMOUS = "Autonomous"
    SPLIT = "Split"


@dataclass
class Clocks:
    """All world-level clocks and progressive counters.
    [canonical: params/bg/core.md §Starting Values v04 B2]"""
    rendering_stability: int = 72     # RS  [canonical: params/bg/core.md §Starting Values RS row]
    church_influence: int = 28        # CI  [canonical: params/bg/core.md §Starting Values CI row "P-32"]
    invasion_pressure: int = 20       # IP  [canonical: params/bg/core.md §Starting Values IP row]
    parliament_integrity: int = 7     # PI  [canonical: params/bg/core.md §Starting Values PI row PP-188]
    aer: int = 2                      # AER [canonical: params/bg/core.md §Starting Values AER row]
    torben_loyalty: int = 7           # [canonical: params/bg/core.md §Starting Values Torben Loyalty row]
    elske_loyalty: int = 4            # [canonical: params/bg/core.md §Starting Values Elske Loyalty row]
    warden_recognition: int = 0       # WR  [canonical: params/bg/core.md §Starting Values WR row PP-605]
    warden_cooperation: int = 0       # WC  [canonical: params/bg/core.md §Starting Values WC row PP-605]
    peninsular_strain: int = 0        # [canonical: params/bg/core.md §Starting Values Peninsular Strain row]
    autonomy: AutonomyStage = AutonomyStage.LOYAL  # [canonical: params/bg/core.md §Löwenritter Graduated Autonomy "Start = Loyal"]

    # Per-season CI delta tracker — enforces ±5/season cap
    # [canonical: designs/provincial/ci_political_v30.md §7.1 "Old cap: ±5/season (PP-504)"]
    # [canonical: ED-721 Option A — T9 counts against cap uniformly]
    _ci_season_delta: int = 0
    # Per-season PI delta tracker — enforces +2/season accrual cap
    # [canonical: params/factions/stats_1_7_scale.md "PI increase rate cap: +2/season"]
    _pi_season_delta: int = 0
    # Per-season Strain delta tracker
    _strain_season_delta: int = 0

    # Has the one-time Southernmost Surge fired? [canonical: params/bg/clocks.md §RS Effects]
    southernmost_surge_fired: bool = False
    # Has Mass Seizure been used? (one-shot at CI >= 60) [canonical: params/bg/clocks.md §CI Effects]
    mass_seizure_available: bool = False
    mass_seizure_used: bool = False

    def change_ci(self, delta: int) -> int:
        """Apply a CI change subject to ±5/season cap (ED-721 Option A: uniform).
        [canonical: designs/provincial/ci_political_v30.md §7.1]
        Returns actual applied delta (may be clipped)."""
        proposed = self._ci_season_delta + delta
        # Clip to ±5 window [canonical: ci_political_v30.md §7.1 "±5/season (PP-504)"]
        if proposed > 5:                              # [canonical: ci_political_v30.md §7.1 "+5 cap"]
            delta = 5 - self._ci_season_delta
        elif proposed < -5:                           # [canonical: ci_political_v30.md §7.1 "-5 cap"]
            delta = -5 - self._ci_season_delta
        if delta == 0:
            return 0
        new_ci = self.church_influence + delta
        # Clamp to [0, 100] [canonical: params/bg/core.md §Starting Values CI range 0-100]
        new_ci = max(0, min(100, new_ci))             # [canonical: params/bg/core.md §Starting Values]
        actual = new_ci - self.church_influence
        self.church_influence = new_ci
        self._ci_season_delta += actual
        # Mass Seizure gate at CI >= 60 [canonical: params/bg/clocks.md §CI Effects "60+ Mass Seizure available one-shot"]
        if self.church_influence >= 60 and not self.mass_seizure_used:   # [canonical: params/bg/clocks.md §CI Effects]
            self.mass_seizure_available = True
        return actual

    def change_pi(self, delta: int) -> int:
        """Apply a PI change subject to +2/season accrual cap.
        [canonical: params/factions/stats_1_7_scale.md 'PI increase rate cap: +2/season']"""
        if delta > 0:
            proposed = self._pi_season_delta + delta
            if proposed > 2:                          # [canonical: stats_1_7_scale.md PI "+2/season cap"]
                delta = 2 - self._pi_season_delta     # [canonical: stats_1_7_scale.md PI cap]
                if delta <= 0:
                    return 0
        new_pi = self.parliament_integrity + delta
        # PI range 0-20 [canonical: params/bg/core.md §Starting Values PI row]
        new_pi = max(0, min(20, new_pi))              # [canonical: params/bg/core.md PI range]
        actual = new_pi - self.parliament_integrity
        self.parliament_integrity = new_pi
        self._pi_season_delta += max(0, actual)
        return actual

    def change_strain(self, delta: int) -> int:
        """Apply Peninsular Strain change.
        [canonical: designs/provincial/peninsular_strain_v30.md]
        [canonical: params/bg/core.md §Starting Values 'Peninsular Strain 0-10']"""
        new_strain = self.peninsular_strain + delta
        new_strain = max(0, min(10, new_strain))      # [canonical: params/bg/core.md Strain range 0-10]
        actual = new_strain - self.peninsular_strain
        self.peninsular_strain = new_strain
        self._strain_season_delta += actual
        return actual

    def reset_season_deltas(self) -> None:
        self._ci_season_delta = 0
        self._pi_season_delta = 0
        self._strain_season_delta = 0


# ============================================================================
# §4. Seasonal Loop — Accounting Phase
#     [canonical: params/factions/stats_1_7_scale.md §Seasonal cap timing PP-242]
#     [canonical: params/factions/stats_1_7_scale.md §Theocracy Counter]
# ============================================================================


@dataclass
class SimLog:
    """Event log for one season."""
    season: int
    events: List[str] = field(default_factory=list)

    def add(self, event: str) -> None:
        self.events.append(event)


@dataclass
class Campaign:
    """Game-wide state container."""
    seed: int
    factions: Dict[str, Faction]
    clocks: Clocks
    season: int = 0
    any_battle_this_season: bool = False
    any_hostile_stability_da: bool = False  # for PI recovery rule
    logs: List[SimLog] = field(default_factory=list)
    rng: random.Random = field(default_factory=random.Random)
    campaign_over: bool = False
    victory_condition: Optional[str] = None

    def __post_init__(self):
        self.rng = random.Random(self.seed)


def initial_campaign(seed: int = 0) -> Campaign:
    """Set up Season 0 starting state."""
    return Campaign(seed=seed, factions=starting_factions(), clocks=Clocks())


def accounting_phase(camp: Campaign, log: SimLog) -> None:
    """Run end-of-season Accounting.
    [canonical: params/factions/stats_1_7_scale.md §Theocracy Counter]
    [canonical: params/factions/stats_1_7_scale.md §PP-242 Seasonal cap timing]
    [canonical: params/bg/clocks.md §Battle Consequences]"""

    # 1. TC advance +1/season (institutional momentum), BEFORE Assert/Suppress
    # [canonical: stats_1_7_scale.md "TC advances by +1 per season from institutional momentum"]
    # NB: "TC" in older docs = "CI" in current terminology (ci_political_v30 renamed)
    # CI auto-advance still subject to ±5/season cap (ED-721 Option A uniform).
    applied = camp.clocks.change_ci(1)                # [canonical: stats_1_7_scale.md "+1 per season"]
    if applied:
        log.add(f"CI +{applied} (institutional momentum, PP-504 cap applies)")

    # 2. Battle consequences [canonical: params/bg/clocks.md §Battle Consequences]
    if camp.any_battle_this_season:
        # RS -1 per battle season (or -2 for Campaign/War scale — Session 2 adds scale)
        # [canonical: params/bg/clocks.md §Battle Consequences "RS -1"]
        camp.clocks.rendering_stability = max(0, camp.clocks.rendering_stability - 1)  # [canonical: params/bg/clocks.md "RS -1"]
        log.add(f"RS -1 (battle season), now {camp.clocks.rendering_stability}")
        # IP +2 per battle season [canonical: params/bg/clocks.md "IP +2"]
        camp.clocks.invasion_pressure = min(100, camp.clocks.invasion_pressure + 2)   # [canonical: params/bg/clocks.md "IP +2"]
        log.add(f"IP +2 (battle season), now {camp.clocks.invasion_pressure}")
        # Strain +1 per battle season [canonical: params/bg/clocks.md "Peninsular Strain +1"]
        camp.clocks.change_strain(1)                  # [canonical: params/bg/clocks.md "Strain +1"]
        log.add(f"Strain +1 (battle season), now {camp.clocks.peninsular_strain}")

    # 3. Peninsular Strain decay -1/peaceful season
    # [canonical: params/bg/core.md §Starting Values Strain "Decays -1/peaceful season"]
    if not camp.any_battle_this_season and camp.clocks.peninsular_strain > 0:
        camp.clocks.change_strain(-1)                 # [canonical: params/bg/core.md Strain decay]
        log.add(f"Strain -1 (peaceful season), now {camp.clocks.peninsular_strain}")

    # 4. PI accrual: +1/season per faction with Mandate < 3
    # [canonical: stats_1_7_scale.md "PI +1/season any faction Mandate < 3 at accounting"]
    pi_pressure = 0
    for f in camp.factions.values():
        if f.mandate is not None and f.mandate < 3:   # [canonical: stats_1_7_scale.md PI "Mandate < 3"]
            pi_pressure += 1
    if pi_pressure > 0:
        applied = camp.clocks.change_pi(pi_pressure)  # subject to +2/season cap
        log.add(f"PI +{applied} ({pi_pressure} factions Mandate<3)")

    # 5. PI recovery: -1/season if zero hostile Stability-targeting DAs
    # [canonical: stats_1_7_scale.md "PI -1/season zero hostile Stability-targeting DAs"]
    if not camp.any_hostile_stability_da and camp.clocks.parliament_integrity > 0:
        camp.clocks.parliament_integrity -= 1         # [canonical: stats_1_7_scale.md PI recovery]
        log.add(f"PI -1 (no hostile Stability DAs), now {camp.clocks.parliament_integrity}")

    # 6. Mandate recovery for factions with Mandate < starting value
    # [canonical: stats_1_7_scale.md §Mandate Recovery ED-066b provisional]
    # Conditions listed in doc but not fully canonical; stub = +1/season unconditional
    # when Mandate below starting value AND faction Stability is >=3 (proxy for stability).
    for f in camp.factions.values():
        if (f.mandate is not None and f.starting_mandate is not None              # [canonical: stats_1_7_scale.md §Mandate Recovery]
                and f.mandate < f.starting_mandate                                # [canonical: stats_1_7_scale.md "Mandate < starting value"]
                and f.stability is not None and f.stability >= 3):                # stub condition (ED-066b provisional)
            if f.can_change("mandate", 1):
                f.change_stat("mandate", 1)
                log.add(f"{f.name}: Mandate +1 (recovery), now {f.mandate}")

    # 7. Löwenritter Autonomy advancement check
    # [canonical: params/bg/core.md §Löwenritter Graduated Autonomy table]
    check_autonomy_advancement(camp, log)

    # 8. Victory / loss checks
    check_endgame(camp, log)

    # 9. Reset per-season delta trackers
    for f in camp.factions.values():
        f.reset_season_deltas()
    camp.clocks.reset_season_deltas()
    camp.any_battle_this_season = False
    camp.any_hostile_stability_da = False


def check_autonomy_advancement(camp: Campaign, log: SimLog) -> None:
    """Advance Löwenritter Autonomy per graduated-autonomy triggers.
    [canonical: params/bg/core.md §Löwenritter Graduated Autonomy]"""
    crown = camp.factions.get("Crown")
    if crown is None or crown.mandate is None:
        return
    stage = camp.clocks.autonomy
    new_stage = stage
    # Loyal -> Restless: Crown Stability <= 3 (simplified; full trigger set in Session 2)
    # [canonical: params/bg/core.md §Löwenritter Graduated Autonomy "Restless" trigger]
    if stage == AutonomyStage.LOYAL:
        if crown.stability is not None and crown.stability <= 3:   # [canonical: params/bg/core.md "Crown Stability ≤ 3"]
            new_stage = AutonomyStage.RESTLESS
    # Restless -> Autonomous: Crown Stability <= 2
    # [canonical: params/bg/core.md "Crown Stability ≤ 2"]
    elif stage == AutonomyStage.RESTLESS:
        if crown.stability is not None and crown.stability <= 2:   # [canonical: params/bg/core.md "Crown Stability ≤ 2"]
            new_stage = AutonomyStage.AUTONOMOUS
    # Autonomous -> Split: Crown eliminated or sustained Autonomous (Session 2 tracks duration)
    # [canonical: params/bg/core.md "Crown eliminated OR 4+ seasons Autonomous"]

    if new_stage != stage:
        camp.clocks.autonomy = new_stage
        log.add(f"Löwenritter Autonomy: {stage.value} -> {new_stage.value}")


def check_endgame(camp: Campaign, log: SimLog) -> None:
    """Check shared-loss and victory conditions.
    [canonical: params/bg/core.md §Starting Values RS "Rupture = shared loss"]
    [canonical: params/bg/clocks.md "RS 0 = Rupture (campaign ends, all factions lose)"]"""
    if camp.clocks.rendering_stability <= 0:          # [canonical: params/bg/clocks.md "RS 0 = Rupture"]
        camp.campaign_over = True
        camp.victory_condition = "SHARED_LOSS: RS Rupture"
        log.add("ENDGAME: RS Rupture — all factions lose")
        return
    # PI 20 = Crown eliminated (auto-resolve)
    # [canonical: params/bg/core.md §Starting Values PI "Auto-resolves at PI >= 20"]
    if camp.clocks.parliament_integrity >= 20:        # [canonical: params/bg/core.md "PI >= 20 Crown elimination"]
        camp.campaign_over = True
        camp.victory_condition = "CROWN_ELIMINATED: PI >= 20"
        log.add("ENDGAME: PI 20 — Crown eliminated")
        return


def run_season(camp: Campaign, domain_actions_phase=None) -> SimLog:
    """Advance the campaign one season.

    domain_actions_phase: callable(camp, log) -> None — Session 2 will provide
    real faction action logic. For Session 1 this is an optional no-op stub.
    """
    camp.season += 1
    log = SimLog(season=camp.season)
    log.add(f"--- Season {camp.season} begin ---")
    # Domain Actions phase (stub for Session 1)
    if domain_actions_phase is not None:
        domain_actions_phase(camp, log)
    # Accounting
    log.add(f"--- Season {camp.season} Accounting ---")
    accounting_phase(camp, log)
    log.add(f"End of season state: RS={camp.clocks.rendering_stability} "
            f"CI={camp.clocks.church_influence} IP={camp.clocks.invasion_pressure} "
            f"PI={camp.clocks.parliament_integrity} Strain={camp.clocks.peninsular_strain} "
            f"Autonomy={camp.clocks.autonomy.value}")
    camp.logs.append(log)
    return log


def run_campaign(max_seasons: int = 40, seed: int = 0,
                 domain_actions_phase=None) -> Campaign:
    """Run until endgame or max_seasons reached.
    Default max_seasons=40 is a smoke-test ceiling, not a canonical campaign
    length. Real campaigns end on Endgame trigger per canon."""
    camp = initial_campaign(seed=seed)
    while not camp.campaign_over and camp.season < max_seasons:
        run_season(camp, domain_actions_phase=domain_actions_phase)
    return camp


# ============================================================================
# §5. Smoke test (Session 1 acceptance)
# ============================================================================


def smoke_test_10_seasons() -> None:
    """Smoke test: run 10 seasons with no Domain Actions, verify state is
    consistent and the seasonal loop drives TC upward and PI gently while
    RS holds."""
    camp = run_campaign(max_seasons=10, seed=42)     # seed 42 for determinism
    # With no DAs, we expect: CI auto-advance +1/season capped at +5/season max,
    # so after 10 seasons CI should be starting 28 + 10 = 38
    # [canonical: stats_1_7_scale.md "TC advances by +1 per season"]
    # [canonical: params/bg/core.md §Starting Values CI 28]
    expected_ci = 28 + 10                             # [canonical: stats_1_7_scale.md TC +1/season]
    assert camp.clocks.church_influence == expected_ci, (
        f"CI drift: expected {expected_ci}, got {camp.clocks.church_influence}"
    )
    # No battles => RS should remain at starting 72
    # [canonical: params/bg/core.md §Starting Values RS 72]
    assert camp.clocks.rendering_stability == 72, (                       # [canonical: params/bg/core.md RS 72]
        f"RS drift: expected 72, got {camp.clocks.rendering_stability}"
    )
    # No battles, no Mandate<3 factions => PI should decay or hold
    # Starting PI = 7, decays -1/peaceful season when no hostile Stability DAs
    # So after 10 peaceful seasons: PI should be 0 (floor)
    # [canonical: params/bg/core.md §Starting Values PI 7]
    # [canonical: stats_1_7_scale.md "PI -1/season zero hostile Stability DAs"]
    assert camp.clocks.parliament_integrity == 0, (                       # [canonical: stats_1_7_scale.md PI recovery]
        f"PI drift: expected 0, got {camp.clocks.parliament_integrity}"
    )
    # Autonomy should still be Loyal (Crown Stability holds at 4)
    # [canonical: params/bg/core.md §Löwenritter Graduated Autonomy Start=Loyal]
    assert camp.clocks.autonomy == AutonomyStage.LOYAL, (                  # [canonical: params/bg/core.md Autonomy Loyal]
        f"Autonomy drift: expected Loyal, got {camp.clocks.autonomy}"
    )
    print("SMOKE TEST PASSED (10 seasons, no DAs)")
    print(f"Final state: season={camp.season}")
    print(f"  RS={camp.clocks.rendering_stability}")
    print(f"  CI={camp.clocks.church_influence}")
    print(f"  IP={camp.clocks.invasion_pressure}")
    print(f"  PI={camp.clocks.parliament_integrity}")
    print(f"  Strain={camp.clocks.peninsular_strain}")
    print(f"  Autonomy={camp.clocks.autonomy.value}")
    for fname, f in camp.factions.items():
        if f.mandate is not None:
            print(f"  {fname}: M={f.mandate} I={f.influence} W={f.wealth} "
                  f"Mil={f.military} Sta={f.stability}")


def smoke_test_dice() -> None:
    """Test dice engine against canonical face values.
    [canonical: params/bg/core.md §Dice System]"""
    # Known: 10 successes + 1 dud -> net=20-0=20
    # 10 = +2 successes [canonical: params/bg/core.md face 10]
    assert net_successes([10]) == 2                   # [canonical: params/bg/core.md face 10 "+2 successes"]
    # 1 = -1 success [canonical: params/bg/core.md face 1]
    assert net_successes([1]) == -1                   # [canonical: params/bg/core.md face 1]
    # 7 = +1 [canonical: params/bg/core.md faces 7-9]
    assert net_successes([7]) == 1                    # [canonical: params/bg/core.md face 7 "+1"]
    # 6 = 0 [canonical: params/bg/core.md faces 2-6]
    assert net_successes([6]) == 0                    # [canonical: params/bg/core.md face 6 "0"]
    # Mixed: [10, 7, 6, 1] = 2 + 1 + 0 + (-1) = 2
    assert net_successes([10, 7, 6, 1]) == 2          # [canonical: params/bg/core.md Dice System sum]
    # Degree table
    # [canonical: params/bg/core.md §Degree Table]
    assert resolve_degree(4, 2) == Degree.OVERWHELMING  # net >= 2*Ob AND >= 3
    assert resolve_degree(2, 2) == Degree.SUCCESS       # net >= Ob
    assert resolve_degree(1, 2) == Degree.PARTIAL       # 0 < net < Ob
    assert resolve_degree(0, 2) == Degree.FAILURE
    assert resolve_degree(-1, 2) == Degree.FAILURE
    # Ob 10 exception [canonical: params/bg/core.md §Degree Table Ob 10 exception]
    assert resolve_degree(4, 10) == Degree.FAILURE      # net < 5 on Ob 10 = Failure
    assert resolve_degree(5, 10) == Degree.PARTIAL      # net >= 5 on Ob 10 = Partial
    print("DICE ENGINE TEST PASSED")


if __name__ == "__main__":
    smoke_test_dice()
    smoke_test_10_seasons()
