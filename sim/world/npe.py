"""
sim/world/npe.py — NPC Population Engine

Canon source: designs/scene/investigation_systems_v30.md SYSTEM 1 (NPE)

Implements §Territory Social Ecology weights + §NPC Genome 5-axis structure
+ §Two-Tier Generation (archetype seed + deviation roll) + §Persistence
(generated NPCs persist per territory).

[ASSUMPTION: NPC registry stored at module level keyed by territory —
 basis: investigation_systems_v30 §Persistence specifies "Generated NPCs
 persist across scenes in the same territory". game_state.World has no
 NPC registry. Schema migration when other higher-tier modules also need
 World-level NPC state. Generated NPCs survive process restart only if
 persisted by caller; tests/Godot save-loads are out of scope here.]

Dependencies:
  - sim/autoload/game_state

Entry points:
  - generate_npc(faction: str | None, role: str | None, world: GameState) -> NPC
  - simulate_npc_actions(world: GameState) -> list[NPCAction]
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional


# §Two-Tier Generation thresholds
# [canonical: §Two-Tier Generation — "Each NPC receives a d6 deviation score
#  at generation. On 5–6: one axis is rolled against the opposite extreme"]
DEVIATION_DIE_THRESHOLD = 5
DEVIATION_DIE_MAX = 6
DEVIATION_ARC_VECTOR_THRESHOLD = 5  # "Deviation ≥ 5 also makes the NPC eligible to become an arc vector"

# §Territory Social Ecology — stat thresholds for ecology weight shifts
# [canonical: §Territory Social Ecology table]
PIETY_HIGH = 4   # 4-5 = Church-aligned weights
PIETY_LOW = 1    # 0-1 = Thread-aware / RM-sympathetic
ACCORD_HIGH = 4  # 4-5 = institutional-trust
ACCORD_LOW = 1   # 0-1 = resentment / survival-first
PROSPERITY_HIGH = 4
PROSPERITY_LOW = 1

# §NPC Genome Record axis bounds
# [canonical: §NPC Genome Record — "1–5 rating" for Stance + Volatility]
STANCE_MIN = 1
STANCE_MAX = 5
VOLATILITY_MIN = 1
VOLATILITY_MAX = 5
LOYALTY_MIN = 0
LOYALTY_MAX = 3

# Faction-controlling-faction default weight
# [canonical: §Territory Social Ecology — "Controlling faction's ethical
#  framework is the default for 60% of generated NPCs"]
FACTION_DEFAULT_WEIGHT_PCT = 60

# Conviction taxonomy (from canon reference)
# [canonical: §NPC Genome Record axis 2 — "drawn from the existing conviction
#  taxonomy (Faith, Order, Reason, Justice, Survival, Loyalty, Truth, Power)"]
CONVICTIONS = ("Faith", "Order", "Reason", "Justice", "Survival", "Loyalty", "Truth", "Power")

# Compromise profile categories
# [canonical: §NPC Genome Record axis 4 — "Economic / Informational /
#  Political / Personal / Nothing"]
COMPROMISE_CATEGORIES = ("Economic", "Informational", "Political", "Personal", "Nothing")

# Active political/metaphysical issues per §NPC Genome axis 1
ACTIVE_ISSUES = ("Thread reality", "Church authority", "Altonian threat",
                 "RM legitimacy", "Varfell autonomy")


# Module-level NPC store — fallback when world is None
# Post-2026-05-19 schema migration: when world is supplied, NPCs live on
# world.npcs (dict[territory_id, list[NPC]]) and counter on world.npc_counter.
_npcs_by_territory: dict[str, list["NPC"]] = {}
_npc_counter = [0]


def _npc_store(world):
    if world is not None and hasattr(world, 'npcs'):
        return world.npcs
    return _npcs_by_territory


def _next_npc_id(world):
    """Increment and return the next NPC id counter (world-keyed or module-level)."""
    if world is not None and hasattr(world, 'npc_counter'):
        world.npc_counter += 1
        return world.npc_counter
    _npc_counter[0] += 1
    return _npc_counter[0]


@dataclass
class NPC:
    """Generated NPC matching §NPC Genome Record 5-axis structure."""
    npc_id: str
    territory_id: str
    # Axis 1: Stance (per active issue, 1-5)
    stance: dict[str, int] = field(default_factory=dict)
    # Axis 2: Worldview (1-2 convictions from taxonomy)
    worldview: list[str] = field(default_factory=list)
    # Axis 3: Affiliation
    affiliation_faction: Optional[str] = None
    affiliation_loyalty: int = 1   # 0-3
    hidden_allegiance: Optional[str] = None
    # Axis 4: Compromise Profile
    compromise_category: str = "Economic"
    # Axis 5: Volatility (1-5)
    volatility: int = 3
    # Generation provenance
    deviation_roll: int = 0
    is_arc_vector: bool = False
    persistent_state: dict = field(default_factory=dict)


@dataclass
class NPCAction:
    npc_id: str
    action_type: str
    season: int
    details: dict = field(default_factory=dict)


def _ecology_weights(world, territory_id: str) -> dict:
    """Compute §Territory Social Ecology weights for one territory.

    Returns a dict of weight modifiers applied to the generation roll.
    """
    if territory_id not in world.territories:
        return {}
    t = world.territories[territory_id]

    # Map Territory.accord (continuous 0.5-7.0 via ACCORD_MAP) → canonical
    # integer 0-4 via canonical_accord. Direct int() drifts: t.accord=5.5
    # (canon Accord 3) → int=5 → falsely triggers ACCORD_HIGH=4.
    # [BUG FIX 2026-05-19 — see game_state.canonical_accord helper.]
    from sim.autoload.game_state import canonical_accord
    accord_int = canonical_accord(t.accord)

    weights = {
        'piety_high': 0, 'piety_low': 0,
        'accord_high': 0, 'accord_low': 0,
        'prosperity_high': 0, 'prosperity_low': 0,
        'volatility_offset': 0,
        'controlling_faction': t.owner,
    }
    # Note: Territory currently has no piety field; use prosperity as proxy
    # for ecology, flagged as approximation
    if t.prosperity >= PROSPERITY_HIGH:
        weights['prosperity_high'] = +2
    elif t.prosperity <= PROSPERITY_LOW:
        weights['prosperity_low'] = +1

    if accord_int >= ACCORD_HIGH:
        weights['accord_high'] = +1
        weights['volatility_offset'] = -1
    elif accord_int <= ACCORD_LOW:
        weights['accord_low'] = +2
        weights['volatility_offset'] = +1

    return weights


def generate_npc(faction: Optional[str], role: Optional[str], world,
                 territory_id: Optional[str] = None,
                 rng=None) -> NPC:
    """Generate an NPC per §Two-Tier Generation.

    Tier 1: Archetype seed — ecology weights for the territory populate the
            5 axes with locally-typical values.
    Tier 2: Deviation roll — d6; on 5-6 one axis flips to ecology's opposite
            extreme.

    faction: optional override (forces affiliation)
    role: optional archetype label (not used in mechanical weights here;
          reserved for future scene-specific generation)
    territory_id: optional; if None, world.rng picks one
    rng: optional random.Random; default world.rng
    """
    rng = rng if rng is not None else (world.rng if hasattr(world, 'rng') else None)
    if rng is None:
        import random
        rng = random.Random()

    if territory_id is None:
        territory_id = rng.choice(list(world.territories.keys()))

    weights = _ecology_weights(world, territory_id)
    controlling = weights.get('controlling_faction')

    # Tier 1 — archetype
    npc_faction = faction if faction is not None else (
        controlling if rng.randint(1, 100) <= FACTION_DEFAULT_WEIGHT_PCT
        else rng.choice([f for f in ('Crown', 'Church', 'Hafenmark', 'Varfell') if f != controlling])
    )

    # Stance per active issue — base 3 (neutral) plus ecology nudges
    stance = {}
    for issue in ACTIVE_ISSUES:
        base = 3
        # Ecology nudges: only apply where directionally meaningful
        if issue == "Church authority":
            if weights['prosperity_high']:
                base += 1   # high prosperity → more institutional trust → more Church authority
        if issue == "Thread reality":
            if weights['prosperity_low'] or weights['accord_low']:
                base += 1   # desperation increases Thread-awareness per §Ecology table
        stance[issue] = max(STANCE_MIN, min(STANCE_MAX, base))

    # Worldview — 1-2 convictions weighted by faction
    primary = rng.choice(CONVICTIONS)
    worldview = [primary]
    if rng.randint(1, 100) <= 40:
        secondary = rng.choice([c for c in CONVICTIONS if c != primary])
        worldview.append(secondary)

    # Compromise
    compromise = rng.choice(COMPROMISE_CATEGORIES[:-1])  # 'Nothing' is rare

    # Volatility
    base_vol = 3 + weights['volatility_offset']
    volatility = max(VOLATILITY_MIN, min(VOLATILITY_MAX, base_vol))

    # Loyalty 0-3
    loyalty = 1 if controlling != npc_faction else rng.randint(1, 3)

    # Tier 2 — deviation roll
    dev_roll = rng.randint(1, DEVIATION_DIE_MAX)
    is_arc_vector = dev_roll >= DEVIATION_ARC_VECTOR_THRESHOLD
    if dev_roll >= DEVIATION_DIE_THRESHOLD:
        # Flip one axis to opposite extreme
        flip_choice = rng.randint(0, 4)
        if flip_choice == 0:
            # Flip a Stance to opposite extreme
            issue = rng.choice(list(stance.keys()))
            stance[issue] = STANCE_MAX if stance[issue] <= 2 else STANCE_MIN
        elif flip_choice == 1:
            # Replace worldview with opposite-leaning conviction
            opposites = {"Faith": "Reason", "Reason": "Faith",
                         "Order": "Survival", "Survival": "Order",
                         "Justice": "Power", "Power": "Justice",
                         "Loyalty": "Truth", "Truth": "Loyalty"}
            if worldview[0] in opposites:
                worldview[0] = opposites[worldview[0]]
        elif flip_choice == 2:
            # Hidden allegiance != affiliation
            other = [f for f in ('Crown', 'Church', 'Hafenmark', 'Varfell', 'RM') if f != npc_faction]
            hidden_allegiance = rng.choice(other) if other else None
        elif flip_choice == 3:
            # Compromise becomes 'Nothing'
            compromise = "Nothing"
        else:
            # Volatility extreme
            volatility = VOLATILITY_MIN if volatility >= 3 else VOLATILITY_MAX

    _next_npc_id_val = _next_npc_id(world)
    npc = NPC(
        npc_id=f"NPC-{_next_npc_id_val:05d}",
        territory_id=territory_id,
        stance=stance,
        worldview=worldview,
        affiliation_faction=npc_faction,
        affiliation_loyalty=loyalty,
        compromise_category=compromise,
        volatility=volatility,
        deviation_roll=dev_roll,
        is_arc_vector=is_arc_vector,
    )
    store = _npc_store(world)
    store.setdefault(territory_id, []).append(npc)
    return npc


def simulate_npc_actions(world) -> list[NPCAction]:
    """End-of-season NPC actions per §Persistence "NPCs with shared worldview
    and adjacent Stance positions make a Volatility check. On pass: both
    shift toward each other's Stance by 1."

    Returns list of NPCAction descriptors (mutation already applied).
    """
    actions = []
    rng = world.rng if hasattr(world, 'rng') else None
    if rng is None:
        import random
        rng = random.Random()

    store = _npc_store(world)
    for tid, npcs in store.items():
        # All pairs in same territory; same worldview overlap; adjacent stance
        for i, a in enumerate(npcs):
            for b in npcs[i+1:]:
                # Shared worldview = at least one common conviction
                if not set(a.worldview) & set(b.worldview):
                    continue
                # Adjacent stance on shared issues
                adj_pairs = []
                for issue in ACTIVE_ISSUES:
                    av = a.stance.get(issue, 3)
                    bv = b.stance.get(issue, 3)
                    if abs(av - bv) == 1:
                        adj_pairs.append((issue, av, bv))
                if not adj_pairs:
                    continue
                # Volatility check — average of both NPCs' volatility, roll d6
                avg_vol = (a.volatility + b.volatility) / 2
                if rng.randint(1, 6) <= avg_vol:
                    # Pass — shift toward each other by 1 on one shared issue
                    issue, av, bv = adj_pairs[0]
                    if av < bv:
                        a.stance[issue] = av + 1
                        b.stance[issue] = bv - 1
                    else:
                        a.stance[issue] = av - 1
                        b.stance[issue] = bv + 1
                    actions.append(NPCAction(
                        npc_id=f"{a.npc_id}+{b.npc_id}",
                        action_type='stance_drift',
                        season=world.season,
                        details={'issue': issue},
                    ))
    return actions


def get_npcs_in_territory(territory_id: str, world=None) -> list[NPC]:
    store = _npc_store(world)
    return list(store.get(territory_id, []))


def reset_npcs(world=None):
    """Test helper."""
    _npc_store(world).clear()
    if world is not None and hasattr(world, 'npc_counter'):
        world.npc_counter = 0
    else:
        _npc_counter[0] = 0
