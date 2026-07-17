"""
sim/provincial/crown_initiative.py — Crown Initiative — three modes

Canon source: designs/audit/2026-05-14-balance-audit/part10_crown_initiative_design_2026-05-14.md
              (Royal Progress Ob ED-840 closure, Pass 2h, 2026-05-17)
Game Design constraints applicable: GD-2 (Crown faction-unique action)
Status: [PROVISIONAL — Phase 5/9 integration 2026-05-17. Three modes implemented
         (Royal Progress, Great Work, Coronation Renewal). Royal Progress uses
         POST-ED-840 closure formula: max(2, floor((sum_max - sum_current) / 2)).
         Great Work simplified to instant-resolution (multi-season Open Pledge
         tracking deferred to PP-515 personal/pledge module, canonical Phase 5+).
         Coronation Renewal lifts Excommunication state on success per §6.4
         (Q-11 resolution).]
[PRE-LPS-1 / PORT-BLOCKING — ED-FA-0004, 2026-07-07: Great Work's int(crown.L) Mandate-as-pool
 convention is the pre-LPS-1 SUPERSEDED scalar; the ratified per-settlement Mandate aggregate is
 UNIMPLEMENTED. Do NOT port as canon-conformant until ED-FA-0004 (Stratum B).]

Dependencies:
  - sim/autoload/dice_engine — d10 pool resolution
  - sim/autoload/game_state — Faction.adjust granular convention
"""
from __future__ import annotations

import math
from dataclasses import dataclass, field

from engine.autoload import dice_engine
from engine.autoload.dice_engine import Degree


# ── Granular conversion (matches v17 mc_v17.py:477-479 convention) ───────────
_MULTS_W = 100  # [canonical: params/factions.md §Stat multipliers — W=100]
_MULTS_L = 20   # [canonical: params/factions.md §Stat multipliers — L=20]
_MULTS_ACCORD = 10  # [canonical: game_state.py MULTS — accord=10]
_TN = 7  # [canonical: params/core.md §TN Values — TN 7 default]


# ── Mode I — Royal Progress (part10 §3.2 — POST-ED-840 closure formula) ──────

ROYAL_PROGRESS_WEALTH_COST = -2  # canonical "W -2" [part10 §3.2]
ROYAL_PROGRESS_OB_FLOOR = 2  # canonical "Floor at 2" [part10 §3.2 ED-840]
ROYAL_PROGRESS_MAX_ACCORD_PER_TERR = 7  # canonical "sum_max = 7 * num_owned" [part10 §3.2 ED-840]


def royal_progress_ob(world, faction) -> int:
    """ED-840 closure: max(2, floor((sum_max - sum_current) / 2)).

    Discontent-driven: easier when Accord is high (gap small), harder when realm
    is in turmoil. Floor 2 prevents trivial auto-success at peak Accord.
    """
    owned = [tid for tid in faction.territories if tid in world.territories]
    n = len(owned)
    if n == 0:
        return ROYAL_PROGRESS_OB_FLOOR
    sum_max = ROYAL_PROGRESS_MAX_ACCORD_PER_TERR * n
    sum_current = sum(world.territories[tid].accord for tid in owned)
    gap = sum_max - sum_current
    return max(ROYAL_PROGRESS_OB_FLOOR, math.floor(gap / 2))


def attempt_royal_progress(crown, world, rng) -> InitiativeResult:
    """Resolve one Royal Progress attempt for Crown.

    Pool = Influence + Standing modifier. Ob per ED-840 closure formula.
    Costs Wealth -2 regardless of outcome (part10 §3.2 outcome table).
    """
    # Historical grounding (annotation only, ED-FA-0017 CP-5, 2026-07-08): itinerant kingship —
    # Ottonian/Angevin iteration and Elizabeth I's royal progresses — presence-as-governance, the
    # court "eating the countryside" as simultaneous extraction and theater. Grounds why this mode
    # exists (Accord/Mandate paid for by physically moving the court through owned territory), not
    # the Ob/cost constants above, which are unchanged (ED-840 closure). See
    # designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md CP-5.
    if crown.name != 'Crown':
        return InitiativeResult(status='invalid_not_crown', mode='royal_progress')
    if crown.senator_inward_used:
        return InitiativeResult(status='invalid_slot_used', mode='royal_progress')

    crown.senator_inward_used = True
    ob = royal_progress_ob(world, crown)
    pool = int(crown.I) + crown.standing  # [canonical: part10 §3.2 — "Influence + Standing modifier"]

    res = dice_engine.roll_pool(pool_size=pool, tn=_TN, ob=ob, rng=rng)
    result = InitiativeResult(
        status='resolved', mode='royal_progress',
        degree=res.degree, pool_size=res.pool_size, ob=float(ob), net=res.net,
        rolls=res.rolls,
    )

    # Cost paid regardless of outcome [part10 §3.2 — "cost paid" on all rows]
    crown.adjust('W', ROYAL_PROGRESS_WEALTH_COST * _MULTS_W)
    result.effects_applied.append(f"Crown.W -2.0 stat-tier [§3.2 cost]")

    # Outcome [part10 §3.2 table]
    deg = res.degree
    if deg == Degree.OVERWHELMING:
        crown.adjust('L', 2 * _MULTS_L)  # Mandate +2
        crown.standing += 1
        # All own territories at Accord 1 -> Accord 2 (canonical-tier comparison: <=2.5 in v17)
        for tid in crown.territories:
            t = world.territories.get(tid)
            if t and t.accord <= 2.5:
                t.adjust_accord(15)  # +1.5 stat-tier (canonical "1 -> 2") per v17 mc_v17:483
        result.effects_applied.append("Crown.L +2.0 stat-tier; Crown.standing +1; low-accord territories +1.5")
    elif deg == Degree.SUCCESS:
        crown.adjust('L', 1 * _MULTS_L)  # Mandate +1
        # +1 Accord (canonical) to lowest-Accord owned territory
        owned = [(tid, world.territories[tid]) for tid in crown.territories if tid in world.territories]
        if owned:
            target_tid, target_t = min(owned, key=lambda kv: kv[1].accord)
            target_t.adjust_accord(_MULTS_ACCORD)  # +1.0 stat-tier
            result.effects_applied.append(f"Crown.L +1.0; {target_tid}.accord +1.0")
        else:
            result.effects_applied.append("Crown.L +1.0; no owned territory for accord boost")
    elif deg == Degree.PARTIAL:
        crown.standing += 1
        result.effects_applied.append("Crown.standing +1 [§3.2 partial]")
    else:  # FAILURE
        crown.standing -= 1
        result.effects_applied.append("Crown.standing -1 [§3.2 failure]")

    return result


# ── Mode II — Great Work (part10 §3.3 — instant-resolution simplification) ────

GREAT_WORK_WEALTH_COST_PER_SEASON = -1  # canonical "W -1 per season" [part10 §3.3]
GREAT_WORK_SEASONS = 3  # canonical "3 seasons" [part10 §3.3]
GREAT_WORK_FINAL_OB = 4  # canonical "Ob 4" [part10 §3.3]


def attempt_great_work(crown, world, rng) -> InitiativeResult:
    """Multi-season Open Pledge simplified to instant resolution at full cost.

    Real PP-515 pledge tracking (Phase 1 declare, breach penalties, Standing on
    declare) is deferred. Current form: pays all 3 seasons of Wealth, rolls at
    Ob 4 with Mandate pool, applies outcome.
    """
    # Historical grounding (annotation only, ED-FA-0017 CP-5, 2026-07-08): cathedral/civic-works
    # legitimacy — great construction projects (and their fiscal shadow, e.g. Beauvais) as a
    # standing mechanism for converting sustained Wealth expenditure into durable Mandate/Standing.
    # Grounds why this mode exists as a Wealth-for-Mandate exchange, not the specific cost/Ob
    # constants above (canonical, part10 §3.3, unchanged). See
    # designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md CP-5.
    if crown.name != 'Crown':
        return InitiativeResult(status='invalid_not_crown', mode='great_work')
    if crown.senator_inward_used:
        return InitiativeResult(status='invalid_slot_used', mode='great_work')

    crown.senator_inward_used = True
    pool = int(crown.L)  # [canonical: §3.3 — "Pool (final season) | Mandate"]

    res = dice_engine.roll_pool(pool_size=pool, tn=_TN, ob=GREAT_WORK_FINAL_OB, rng=rng)
    result = InitiativeResult(
        status='resolved', mode='great_work',
        degree=res.degree, pool_size=res.pool_size, ob=float(GREAT_WORK_FINAL_OB), net=res.net,
        rolls=res.rolls,
    )

    # Full 3-season Wealth cost upfront (simplification per v17 mc_v17:491)
    crown.adjust('W', GREAT_WORK_WEALTH_COST_PER_SEASON * _MULTS_W * GREAT_WORK_SEASONS)
    result.effects_applied.append(f"Crown.W -3.0 stat-tier [§3.3 3-season cost upfront]")

    deg = res.degree
    if deg == Degree.OVERWHELMING:
        crown.adjust('L', 2 * _MULTS_L)
        crown.standing += 2
        result.effects_applied.append("Crown.L +2.0 (permanent); Crown.standing +2")
        result.notes.append("[PROVISIONAL] §3.3 OW 'Charters Govern -1 Ob (permanent)' not modeled — Charters not in v18 schema")
    elif deg == Degree.SUCCESS:
        crown.adjust('L', 2 * _MULTS_L)
        result.effects_applied.append("Crown.L +2.0 (permanent)")
    elif deg == Degree.PARTIAL:
        crown.adjust('L', 1 * _MULTS_L)
        result.effects_applied.append("Crown.L +1.0; sunk W partial loss [§3.3 partial]")
    else:  # FAILURE
        crown.standing -= 2
        result.effects_applied.append("Crown.standing -2 [§3.3 failure]")
        result.notes.append("[PROVISIONAL] §3.3 Failure 'Cohesion -20 (PP-515)' not modeled — Cohesion track not in v18 schema")

    return result


# ── Mode III — Coronation Renewal (part10 §3.4 — Excomm recovery, §6.4 Q-11) ──

CORONATION_WEALTH_COST = -2  # canonical "W -2" [part10 §3.4]


def coronation_renewal_ob(church_l: float) -> int:
    """Ob = floor(Church Mandate / 2) + 1 [part10 §3.4]."""
    return math.floor(church_l / 2) + 1


def coronation_renewal_prereq(crown, church, world) -> tuple[bool, str]:
    """Truce/Peace/Alliance/Crown Treaty with Church AND Church not actively
    prosecuting an Excommunication against Crown this season.

    v18 schema lacks Crown-Church relation tracking; we use a permissive default
    (peace assumed unless Crown is currently excommunicated, in which case
    Coronation is the canonical recovery path — distinct from Church *actively
    prosecuting*, which is a same-season event).
    """
    # Permissive prereq — Crown can attempt Coronation while excommunicated
    # (this IS the canonical recovery path per §6.4 Q-11).
    # We do block when Crown is BOTH excommunicated AND the Church just attempted
    # to excommunicate this same season (faction_action would need to flag, deferred).
    if church is None or not getattr(church, 'parliamentary', True):
        return False, "Church not available"
    return True, "ok"


def attempt_coronation_renewal(crown, world, rng) -> InitiativeResult:
    """Coronation Renewal — recovery from Excommunication, Mandate boost.

    Pool = Crown.I. Ob = floor(Church.L / 2) + 1.
    On Success/Overwhelming: lifts Excommunication if active. (§6.4 Q-11)
    """
    # Historical grounding (annotation only, ED-FA-0017 CP-5, 2026-07-08): Festkronungen — ritual
    # crown-wearings at Christmas/Easter/Whitsun — and the Laudes Regiae, ritual reaffirmations of
    # sacral kingship distinct from a first coronation. Grounds why a *renewal* rite (not a new
    # coronation) is the canonical Excommunication-recovery path here; the Ob/pool formula above
    # (part10 §3.4) is unchanged. See
    # designs/audit/2026-07-08-fa-se-historical-precedent-research/fa_se_historical_precedent_research_v1.md CP-5.
    if crown.name != 'Crown':
        return InitiativeResult(status='invalid_not_crown', mode='coronation_renewal')
    if crown.senator_inward_used:
        return InitiativeResult(status='invalid_slot_used', mode='coronation_renewal')

    church = world.factions.get('Church')
    ok, msg = coronation_renewal_prereq(crown, church, world)
    if not ok:
        return InitiativeResult(status='invalid_prereq', mode='coronation_renewal',
                                notes=[msg])

    crown.senator_inward_used = True
    ob = coronation_renewal_ob(church.L)
    pool = int(crown.I)

    res = dice_engine.roll_pool(pool_size=pool, tn=_TN, ob=ob, rng=rng)
    result = InitiativeResult(
        status='resolved', mode='coronation_renewal',
        degree=res.degree, pool_size=res.pool_size, ob=float(ob), net=res.net,
        rolls=res.rolls,
    )

    crown.adjust('W', CORONATION_WEALTH_COST * _MULTS_W)
    result.effects_applied.append("Crown.W -2.0 stat-tier [§3.4 cost]")

    deg = res.degree
    was_excommunicated = getattr(crown, 'excommunicated', False)

    if deg == Degree.OVERWHELMING:
        crown.adjust('L', 2 * _MULTS_L)
        crown.standing += 1
        if was_excommunicated:
            crown.excommunicated = False
            result.effects_applied.append("Crown.excommunicated = False [§3.4 OW lifts Excomm]")
        result.effects_applied.append("Crown.L +2.0; Crown.standing +1")
        result.notes.append("[PROVISIONAL] §3.4 OW 'Crown-Church Standing +1' not modeled (cross-faction Standing not in v18 schema)")
    elif deg == Degree.SUCCESS:
        crown.adjust('L', 1 * _MULTS_L)
        if was_excommunicated:
            crown.excommunicated = False
            result.effects_applied.append("Crown.excommunicated = False [§3.4 Success lifts Excomm]")
        result.effects_applied.append("Crown.L +1.0")
    elif deg == Degree.PARTIAL:
        crown.standing += 1
        result.effects_applied.append("Crown.standing +1 [§3.4 partial]")
    else:  # FAILURE
        crown.standing -= 1
        result.effects_applied.append("Crown.standing -1 [§3.4 failure]")

    return result


# ── Result type ───────────────────────────────────────────────────────────────

@dataclass
class InitiativeResult:
    """Outcome of one Crown Initiative attempt (any mode)."""
    status: str  # 'invalid_not_crown' | 'invalid_slot_used' | 'invalid_prereq' | 'resolved'
    mode: str    # 'royal_progress' | 'great_work' | 'coronation_renewal'
    degree: Degree | None = None
    pool_size: int = 0
    ob: float = 0.0
    net: int = 0
    rolls: list[int] = field(default_factory=list)
    effects_applied: list[str] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)


# ── Mode selection (mirrors mc_v17:582-588 heuristic) ────────────────────────

def select_initiative_mode(crown, world, rng) -> str | None:
    """Mode selection heuristic.

    Coronation Renewal is ONLY for Excommunication recovery — never selected
    when Crown is not excommunicated (it burns Wealth without strategic gain
    against Ob = floor(Church.L/2)+1, which is non-trivial).

    Royal Progress when Ob viable (Ob ≤ Pool + reasonable margin).
    Great Work when Wealth sufficient (3 stat-tier cost).
    """
    if crown.senator_inward_used:
        return None
    if getattr(crown, 'excommunicated', False):
        return 'coronation_renewal'
    ob = royal_progress_ob(world, crown)
    pool = int(crown.I) + crown.standing
    # RP viable when Ob ≤ Pool + 1 (≥50% chance of Partial-or-better)
    if ob <= pool + 1:
        return 'royal_progress'
    # Great Work: requires Wealth ≥ 3.0 (3-season cost paid upfront)
    if crown.W >= 3.0:
        return 'great_work'
    # No viable mode this season
    return None
