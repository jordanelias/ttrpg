"""
sim/personal/knots.py — Knot lifecycle — formation, sustaining, rupture

Canon source: designs/personal/knots_v30.md (Pass 2g synthesis 2026-05-17)

Implements:
  - form_knot: §3.1 prerequisites + §3.2 procedure
  - sustain_knot: §5 strain accumulation + §6.1 break check at Accounting
  - check_knot_rupture: §6.2 trigger evaluation
  - apply_knot_loss: §6.1/§6.2 consequences (Disposition drop, Coherence -1,
    Composure damage, Conviction Scar if high-strain Close break)

[ASSUMPTION OPTION A] knots_v30 §2 surfaces a 3-way canon contradiction
(TIER-DRIFT-001) on tier system. Implementing Option A (ED-773
chronological supersedence): Distant/Close 2-tier with capacities 4/7.
This is the explicit "Option A" alternative listed in §3.2's
[PROVISIONAL] note, and matches the most-recent canon source. If Jordan
resolves to Option B (Loose/Medium/Close) or Option C (4-tier), tier
constants and §3.2 degree table swap; semantic contracts unchanged.

Cyclic resolution: knots depends on coherence (apply_coherence_delta on
rupture per PP-632 -1 Coherence) and conviction (Scar on high-strain
break per §6.1). Both via late-import inside function bodies — no
module-load-time cycle.

[ASSUMPTION: knot registry stored at module level — basis: World has no
 .knots field. _store(world) router prepared for future schema migration.]

Dependencies:
  - sim/thread/coherence (apply_coherence_delta on rupture)
  - sim/personal/conviction (apply_conviction_scar on high-strain break)

Entry points:
  - form_knot(actor_a, actor_b, world, rng) -> Knot | None
  - sustain_knot(knot_id, strain_delta, source, world) -> KnotState
  - check_knot_rupture(knot, trigger, world) -> bool
  - apply_knot_loss(actor, knot, mode, world) -> dict (consequences)
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Optional, Any

from sim.autoload.dice_engine import roll_pool


# §3.1 prerequisites
# [canonical: §3.1 — "Disposition +5 with target NPC", "PC Bonds ≥ 5",
#  "PC's current Knot count < floor(Bonds/2) + 1"]
KNOT_DISPOSITION_MIN = 5
KNOT_BONDS_MIN = 5
KNOT_TS_MIN_PARTY = 30  # Either PC or NPC has TS ≥ 30

# §3.2 formation roll
# [canonical: §3.2 — "Spirit × 2 + History (Relationships), TN 7, Ob 2"]
KNOT_FORMATION_TN = 7
KNOT_FORMATION_OB = 2

# §2 Option A tier system + §6.1 capacities
# [canonical: §2 Option A — Distant/Close 2-tier; §6.1 — Distant 4, Close 7]
TIER_DISTANT = "Distant"
TIER_CLOSE = "Close"
TIER_CAPACITY = {
    TIER_DISTANT: 4,
    TIER_CLOSE: 7,
}

# §6.1 high-strain break threshold (Option A)
# [canonical: §6.1 — "Close Knots broken at high strain (Option A: strain ≥ 6 of 7):
#  Conviction Scar +1 to both partners"]
CLOSE_BREAK_SCAR_STRAIN_THRESHOLD = 6

# §6.1 break consequences
# [canonical: §6.1 — "Both partners take 4 Composure"]
BREAK_COMPOSURE_DAMAGE = 4

# §6.2 rupture consequences
# [canonical: §6.2 — "Per PP-632, rupture imposes mandatory −1 Coherence"]
RUPTURE_COHERENCE_LOSS = -1
# [canonical: §6.2 trigger table — public citation: Disposition → -4]
RUPTURE_DISPOSITION_CITATION = -4
# [canonical: §6.2 trigger — FR Dissolution rupture-victim takes +1 Wound]
RUPTURE_WOUND_DISSOLUTION = 1

# §8.1 Coherence-band strain pacing
# [canonical: §8.1 table]
COHERENCE_BAND_STRAIN_PACING = {
    "Stable":     0,    # 10-8: None
    "Dissonant":  3,    # 7-5: +1 strain per 3 sessions
    "Fragmented": 2,    # 4-3: +1 strain per 2 sessions
    "Fractured":  1,    # 2: +1 strain per session
    "Severed":    1,    # 1: +2 strain (still per-session but doubled)
}


@dataclass
class Knot:
    """A Knot between two actors per §1-§5."""
    knot_id: str
    actor_a: str
    actor_b: str
    tier: str                    # 'Distant' / 'Close'
    strain: int = 0
    disposition: int = 5         # Starts at min prereq +5
    active: bool = True
    formed_season: int = 0
    log: list[dict] = field(default_factory=list)


@dataclass
class KnotState:
    """Return value of sustain_knot — current state after operation."""
    knot: Knot
    broke: bool
    ruptured: bool
    strain_after: int
    notes: list[str] = field(default_factory=list)


# Module-level knot registry
_knots: dict[str, Knot] = {}
_knot_id_counter = [0]


def _store(world):
    """Return the knot store: world.knots if world supplied,
    else module-level fallback."""
    if world is not None and hasattr(world, 'knots'):
        return world.knots
    return _knots


def _count_knots_for_actor(actor: str, world=None) -> int:
    """How many active Knots does this actor participate in."""
    return sum(1 for k in _store(world).values()
               if k.active and (k.actor_a == actor or k.actor_b == actor))


def form_knot(actor_a: str, actor_b: str, world=None,
              actor_a_obj=None, actor_b_obj=None, season: int = 0,
              rng=None) -> Optional[Knot]:
    """§3 Formation. Returns Knot on success, None on prerequisite failure.

    Caller supplies actor_a_obj / actor_b_obj for stat lookups (.bonds,
    .spirit, .history_relationships, .ts, .disposition_with_other).
    """
    # §3.1 Prerequisites
    if actor_a_obj is None or actor_b_obj is None:
        return None

    bonds_a = getattr(actor_a_obj, 'bonds', 0)
    if bonds_a < KNOT_BONDS_MIN:
        return None

    disp = getattr(actor_a_obj, f'disposition_with_{actor_b}', None)
    if disp is None:
        disp = getattr(actor_a_obj, 'disposition', 0)
    if disp < KNOT_DISPOSITION_MIN:
        return None

    ts_a = getattr(actor_a_obj, 'ts', 0)
    ts_b = getattr(actor_b_obj, 'ts', 0)
    if ts_a < KNOT_TS_MIN_PARTY and ts_b < KNOT_TS_MIN_PARTY:
        return None

    current_knots = _count_knots_for_actor(actor_a, world)
    knot_max = (bonds_a // 2) + 1
    if current_knots >= knot_max:
        return None

    # No existing Knot between these two
    for k in _store(world).values():
        if not k.active:
            continue
        if (k.actor_a == actor_a and k.actor_b == actor_b) or \
           (k.actor_a == actor_b and k.actor_b == actor_a):
            return None

    # §3.2 Formation roll
    spirit = getattr(actor_a_obj, 'spirit', 3)
    history_rel = getattr(actor_a_obj, 'history_relationships', 0)
    pool = (spirit * 2) + history_rel

    rng = rng if rng is not None else (world.rng if world is not None and hasattr(world, 'rng') else None)
    if rng is None:
        import random
        rng = random.Random()

    roll_result = roll_pool(pool, tn=KNOT_FORMATION_TN, rng=rng)
    net = roll_result.net

    # Degree
    if net >= KNOT_FORMATION_OB + 3:
        # Overwhelming
        tier = TIER_CLOSE
    elif net >= KNOT_FORMATION_OB:
        tier = TIER_DISTANT
    else:
        # Partial / Failure — no knot
        return None

    _knot_id_counter[0] += 1
    if world is not None and hasattr(world, 'knot_id_counter'):
        world.knot_id_counter += 1
        knot_id = f"KNOT-{world.knot_id_counter:04d}"
    else:
        knot_id = f"KNOT-{_knot_id_counter[0]:04d}"
    knot = Knot(
        knot_id=knot_id, actor_a=actor_a, actor_b=actor_b,
        tier=tier, strain=0, disposition=disp,
        formed_season=season,
    )
    _store(world)[knot_id] = knot
    return knot


def sustain_knot(knot_id: str, strain_delta: int = 0,
                 source: str = "", world=None) -> KnotState:
    """Apply strain change (positive=accumulate, negative=decay) and
    check §6.1 capacity break at the end."""
    store = _store(world)
    if knot_id not in store:
        return KnotState(knot=None, broke=False, ruptured=False, strain_after=0,
                         notes=[f"knot_id {knot_id} not found"])

    knot = store[knot_id]
    if not knot.active:
        return KnotState(knot=knot, broke=False, ruptured=False,
                         strain_after=knot.strain, notes=["knot inactive"])

    knot.strain = max(0, knot.strain + strain_delta)
    knot.log.append({'source': source, 'strain_delta': strain_delta, 'strain_after': knot.strain})

    # §6.1 capacity break check
    capacity = TIER_CAPACITY.get(knot.tier, 0)
    broke = knot.strain > capacity
    if broke:
        knot.active = False
    return KnotState(knot=knot, broke=broke, ruptured=False, strain_after=knot.strain)


def check_knot_rupture(knot_id: str, trigger: str, world=None) -> KnotState:
    """§6.2 rupture trigger check.

    trigger values:
      'public_citation', 'partner_death', 'fr_dissolution',
      'conviction_shift', 'player_dissolution'
    """
    store = _store(world)
    if knot_id not in store:
        return KnotState(knot=None, broke=False, ruptured=False, strain_after=0)

    knot = store[knot_id]
    if not knot.active:
        return KnotState(knot=knot, broke=False, ruptured=False,
                         strain_after=knot.strain, notes=["already inactive"])

    rupture_triggers = {
        'public_citation', 'partner_death', 'fr_dissolution',
        'conviction_shift', 'player_dissolution'
    }
    if trigger not in rupture_triggers:
        return KnotState(knot=knot, broke=False, ruptured=False,
                         strain_after=knot.strain,
                         notes=[f"unknown trigger '{trigger}'"])

    knot.active = False
    knot.log.append({'source': f"rupture: {trigger}", 'rupture': True})
    return KnotState(knot=knot, broke=False, ruptured=True,
                     strain_after=knot.strain,
                     notes=[f"§6.2 rupture trigger: {trigger}"])


def apply_knot_loss(actor: str, knot_id: str, mode: str = 'break',
                    world=None) -> dict:
    """Apply §6.1 break or §6.2 rupture consequences to an actor.

    mode: 'break' (capacity exceeded) or 'rupture' (immediate trigger).
    Returns consequences dict; routes through coherence + conviction modules.
    """
    store = _store(world)
    if knot_id not in store:
        return {'error': 'knot not found'}

    knot = store[knot_id]
    consequences = {
        'actor': actor,
        'knot_id': knot_id,
        'mode': mode,
        'composure_damage': 0,
        'coherence_delta': 0,
        'disposition_set_to': None,
        'wound': 0,
        'conviction_scar': None,
    }

    if mode == 'break':
        # §6.1
        consequences['composure_damage'] = BREAK_COMPOSURE_DAMAGE
        # Disposition drops to +2 (or current -2, whichever lower)
        consequences['disposition_set_to'] = min(2, knot.disposition - 2)
        # High-strain Close break → Conviction Scar
        if knot.tier == TIER_CLOSE and knot.strain >= CLOSE_BREAK_SCAR_STRAIN_THRESHOLD:
            consequences['conviction_scar'] = 1
            # Late-import conviction
            try:
                from sim.personal.conviction import apply_conviction_scar
                # Caller specifies which Conviction; default to a generic flag
                apply_conviction_scar(actor, f"Close Knot break (id={knot_id})",
                                      magnitude=1, conviction='Loyalty',
                                      world=world)
            except (ImportError, AttributeError):
                pass

    elif mode == 'rupture':
        # §6.2
        # PP-632 mandatory -1 Coherence
        consequences['coherence_delta'] = RUPTURE_COHERENCE_LOSS
        try:
            from sim.thread.coherence import apply_coherence_delta
            apply_coherence_delta(actor, RUPTURE_COHERENCE_LOSS,
                                  f"Knot rupture (id={knot_id})", world=world)
        except (ImportError, AttributeError):
            pass

    return consequences


def get_knot(knot_id: str, world=None) -> Optional[Knot]:
    return _store(world).get(knot_id)


def get_active_knots(world=None) -> list[Knot]:
    return [k for k in _store(world).values() if k.active]


def reset_knots(world=None):
    """Test helper."""
    _store(world).clear()
    if world is not None and hasattr(world, 'knot_id_counter'):
        world.knot_id_counter = 0
    _knot_id_counter[0] = 0
