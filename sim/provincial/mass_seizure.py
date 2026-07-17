"""
sim/provincial/mass_seizure.py — Church Mass Seizure (PP-411 + supersession 250715f)

Canon source: designs/provincial/victory_v30.md §3.2; designs/architecture/campaign_architecture_v30.md §1.3
Supersession: registers/supersession_register.yaml 250715f — threshold remains CI ≥ 60
              but declaration is probabilistic P(declare) = ((CI-60)/40)^3.3.

Implements:
  - attempt_mass_seizure_declaration: probabilistic gate per victory §3.2
    declaration formula. One-shot lifetime event tracked on World.
  - resolve_mass_seizure: per-territory resolution against all territories
    with Church building (Chapel+). Pool = Influence + floor(CI/15);
    Ob = 10 − PT − infrastructure modifiers, floor 1.

GD-1 enforced: Mass Seizure does NOT directly produce victory. It produces
territorial conversions; Church must still meet Peninsular Sovereignty
(11+ territories Accord ≥ 2, Political Stability ≤ 6, sustained 2 seasons)
to win — same as any other faction.

[ASSUMPTION: declaration_used flag stored on World — basis: one-shot
 lifetime event needs durable state. World currently lacks this field.
 Module uses world.clocks['MASS_SEIZURE_USED'] (0=available, 1=spent).
 Aligns with existing clocks pattern; full schema migration to a typed
 field deferred to next migration batch.]

[ASSUMPTION: pool roll uses Church.L as Influence proxy — basis: World
 has Faction.L (Mandate/Legitimacy), Sta, W (Influence proxy), I, Mil.
 victory_v30 §3.2 says "Pool = Influence + floor(CI/15)". Church.W aligns
 with "Influence" semantically. The 7-stat lineup canon (faction_canon_v30
 §5.1) has an Influence stat (I), but game_state currently uses .W for
 Wealth and .I for what was Investments. Reading the doc closer the
 "Influence" used in §3.2 is the Church-specific faction action stat;
 in game_state that's faction.I.]

Dependencies:
  - sim/autoload/dice_engine
  - sim/peninsular/ci_track
  - systems/settlements/sim/infrastructure

Entry points:
  - attempt_mass_seizure_declaration(world, force_declare=False) -> SeizureDeclaration
  - resolve_mass_seizure(world) -> list[SeizureResult]
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional

from engine.autoload.dice_engine import roll_pool
from engine.autoload.game_state import canonical_pt
from systems.settlements.sim.infrastructure import (
    count_infrastructure, seizure_ob_modifier, BUILDING_CHAPEL,
    BUILDING_CHURCH, BUILDING_CATHEDRAL,
)


# §3.2 declaration thresholds
# [canonical: victory_v30 §3.2 — "CI ≥ 60 required" + supersession_register 250715f
#  "P(declare) = ((CI-60)/40)^3.3"]
MASS_SEIZURE_AVAILABILITY_CI = 60
MASS_SEIZURE_PROBABILISTIC_DIVISOR = 40   # (CI - 60) / 40
MASS_SEIZURE_PROBABILISTIC_EXPONENT = 3.3
MASS_SEIZURE_FORCED_CI = 100              # P=1 at CI=100

# §3.2 prerequisites
# [canonical: §3.2 — "Church Mandate ≥ 4 required to initiate any seizure"]
MASS_SEIZURE_MIN_MANDATE = 4

# §3.2 pool + Ob formulas
# [canonical: §3.2 — "Pool = Influence + floor(CI/15)"]
POOL_CI_DIVISOR = 15
# [canonical: §3.2 — "Ob = 10 − PT − infrastructure modifiers (floor 1)"]
OB_BASE = 10
OB_FLOOR = 1

# §3.2 Seizure Accord on success
# [canonical: §3.2 — "Success → max(floor(PT/2)+1, 2). Overwhelming → floor(PT/2)+2, max 3"]
SEIZURE_ACCORD_FLOOR = 2

# World flag for one-shot lifetime tracking
MASS_SEIZURE_FLAG_CLOCK = 'MASS_SEIZURE_USED'


@dataclass
class SeizureDeclaration:
    declared: bool
    probability: float
    ci_at_declaration: int
    forced: bool                # CI = 100 forces declaration
    voluntary: bool             # Player Church manually triggered
    reason: str


@dataclass
class SeizureResult:
    """Per-territory result of Mass Seizure resolution."""
    territory_id: str
    seized: bool
    degree: str                  # Overwhelming / Success / Partial / Failure
    pool: int
    ob: int
    net_successes: int
    starting_accord: int         # Accord assigned to seized territory
    notes: list[str] = field(default_factory=list)


def _church_influence(world) -> int:
    """Return Church faction Influence value per victory §3.2.

    [ASSUMPTION: game_state uses faction.I (Investments-renamed-Influence
     pre-canonical-stat-reform). faction.W is Wealth. Per §3.2's
     'Influence + floor(CI/15)' the I field maps. If a future stat-lineup
     migration shifts, the mapping updates here.]
    """
    if 'Church' not in world.factions:
        return 0
    return int(world.factions['Church'].I)


def _church_is_prominent_for_seizure(world, territory_id: str) -> bool:
    """Per §3.2 + PP-534 Self-Control Rule:
     - Church is auto-Prominent in territories it controls.
     - In rival-controlled territories: Church Mandate > controlling Mandate.
    """
    if territory_id not in world.territories:
        return False
    t = world.territories[territory_id]
    if 'Church' not in world.factions:
        return False
    # PP-534: auto-prominent if controlled
    if t.owner == 'Church':
        return True
    if t.owner is None:
        return False
    church_mandate = world.factions['Church'].L
    rival_mandate = world.factions[t.owner].L if t.owner in world.factions else 0
    return church_mandate > rival_mandate


def _declaration_probability(ci: float) -> float:
    """Compute P(declare) per supersession_register 250715f formula.

    P = ((CI - 60) / 40)^3.3, clamped [0, 1].
    """
    if ci < MASS_SEIZURE_AVAILABILITY_CI:
        return 0.0
    if ci >= MASS_SEIZURE_FORCED_CI:
        return 1.0
    base = (ci - MASS_SEIZURE_AVAILABILITY_CI) / MASS_SEIZURE_PROBABILISTIC_DIVISOR
    p = base ** MASS_SEIZURE_PROBABILISTIC_EXPONENT
    return max(0.0, min(1.0, p))


def _has_church_building(world, territory_id: str) -> bool:
    """Per §3.2: 'every territory with at least one settlement containing
    a Church building (Chapel+)'. Checked via infrastructure.count_infrastructure
    for the Religious Building axis."""
    return count_infrastructure(territory_id, 'Religious Building', world) > 0


def attempt_mass_seizure_declaration(world,
                                     force_declare: bool = False,
                                     rng=None) -> SeizureDeclaration:
    """Apply §3.2 + supersession 250715f declaration logic.

    Gate sequence:
      (0) Lifetime one-shot check: if already used, declined.
      (1) CI ≥ 60 required.
      (2) Church Mandate ≥ 4 required.
      (3) Probabilistic check unless force_declare=True or CI=100.
    """
    ci = world.clocks.get('CI', 0)
    already_used = world.clocks.get(MASS_SEIZURE_FLAG_CLOCK, 0) >= 1

    if already_used:
        return SeizureDeclaration(
            declared=False, probability=0.0,
            ci_at_declaration=int(ci), forced=False, voluntary=False,
            reason="one-shot Mass Seizure already declared (§3.2 'no second attempt')",
        )

    if ci < MASS_SEIZURE_AVAILABILITY_CI:
        return SeizureDeclaration(
            declared=False, probability=0.0,
            ci_at_declaration=int(ci), forced=False, voluntary=False,
            reason=f"CI={ci} below availability threshold {MASS_SEIZURE_AVAILABILITY_CI}",
        )

    if 'Church' not in world.factions or world.factions['Church'].L < MASS_SEIZURE_MIN_MANDATE:
        return SeizureDeclaration(
            declared=False, probability=0.0,
            ci_at_declaration=int(ci), forced=False, voluntary=False,
            reason=f"Church Mandate < {MASS_SEIZURE_MIN_MANDATE} (§3.2 prerequisite)",
        )

    prob = _declaration_probability(ci)
    forced = ci >= MASS_SEIZURE_FORCED_CI

    rng = rng if rng is not None else (world.rng if hasattr(world, 'rng') else None)
    if rng is None:
        import random
        rng = random.Random()

    if force_declare or forced:
        declared = True
        reason = "forced (CI=100)" if forced else "voluntary declaration"
    else:
        roll = rng.random()
        declared = roll < prob
        reason = f"probabilistic: rolled {roll:.3f} vs P={prob:.3f}"

    if declared:
        world.clocks[MASS_SEIZURE_FLAG_CLOCK] = 1

    return SeizureDeclaration(
        declared=declared, probability=prob,
        ci_at_declaration=int(ci), forced=forced, voluntary=force_declare,
        reason=reason,
    )


def resolve_mass_seizure(world, rng=None) -> list[SeizureResult]:
    """Per §3.2 + campaign_architecture §1.3: resolve Mass Seizure against
    every territory with at least one Church building (Chapel+).

    Per-territory:
      Pool = Influence + floor(CI / 15)
      Ob = 10 − PT − sum(infrastructure modifiers per settlement), floor 1
      Seized if net_successes >= Ob
      Overwhelming if net_successes >= Ob + 3
      Accord on success: max(floor(PT/2)+1, 2)
      Accord on Overwhelming: min(floor(PT/2)+2, 3)
    """
    rng = rng if rng is not None else (world.rng if hasattr(world, 'rng') else None)
    if rng is None:
        import random
        rng = random.Random()

    ci = world.clocks.get('CI', 0)
    influence = _church_influence(world)
    pool = influence + (int(ci) // POOL_CI_DIVISOR)

    results = []
    # Iterate all territories with Church building present
    for tid, t in world.territories.items():
        if not _has_church_building(world, tid):
            continue
        if not _church_is_prominent_for_seizure(world, tid):
            results.append(SeizureResult(
                territory_id=tid, seized=False, degree='Failure',
                pool=pool, ob=0, net_successes=0, starting_accord=0,
                notes=['not Church-prominent (§3.2 Prominence prerequisite)'],
            ))
            continue

        pt = canonical_pt(t.pt)  # bucket continuous Territory.pt → canon int 0-5
        # Ob: 10 − PT − |infrastructure_modifier|; seizure_ob_modifier returns negative
        infra_mod = seizure_ob_modifier(tid, world)  # already negative or 0, capped at -4
        ob = max(OB_FLOOR, OB_BASE - pt + infra_mod)  # adding negative = subtracting magnitude

        roll = roll_pool(pool, tn=7, rng=rng)
        net = roll.net

        if net >= ob + 3:
            degree, seized = 'Overwhelming', True
        elif net >= ob:
            degree, seized = 'Success', True
        elif net >= 1:
            degree, seized = 'Partial', False
        else:
            degree, seized = 'Failure', False

        # Accord on seizure per §3.2
        if seized:
            base_accord = max(pt // 2 + 1, SEIZURE_ACCORD_FLOOR)
            if degree == 'Overwhelming':
                starting_accord = min(pt // 2 + 2, 3)
            else:
                starting_accord = base_accord
        else:
            starting_accord = 0

        results.append(SeizureResult(
            territory_id=tid, seized=seized, degree=degree,
            pool=pool, ob=ob, net_successes=net,
            starting_accord=starting_accord,
            notes=[f"PT={pt} infra_mod={infra_mod} pool={pool} ob={ob} net={net}"],
        ))

        # Apply ownership transfer + accord on success
        if seized:
            t.owner = 'Church'
            # Convert int accord to ACCORD_MAP-style continuous if needed; for now,
            # set directly using same continuous scale game_state uses
            t.accord = float(starting_accord)

    return results


def is_available(world) -> bool:
    """Helper — True if Mass Seizure has not yet been declared and prerequisites met."""
    return (
        world.clocks.get(MASS_SEIZURE_FLAG_CLOCK, 0) == 0 and
        world.clocks.get('CI', 0) >= MASS_SEIZURE_AVAILABILITY_CI and
        'Church' in world.factions and
        world.factions['Church'].L >= MASS_SEIZURE_MIN_MANDATE
    )
