"""
systems/fieldwork/sim/knots.py — Knot lifecycle — formation, sustaining, rupture

Canon source: systems/fieldwork/knots_v30.md (Pass 2g synthesis 2026-05-17)

Implements:
  - form_knot: §3.1 prerequisites + §3.2 procedure
  - sustain_knot: §5 strain accumulation + §6.1 break check at Accounting
  - check_knot_rupture: §6.2 trigger evaluation
  - apply_knot_loss: §6.1/§6.2 consequences (Disposition drop, Coherence -1,
    Composure damage, Conviction Scar if high-strain Close break)

[RESOLVED — ED-912, 2026-06-28] knots_v30 §2's TIER-DRIFT-001 contradiction
was ruled: the 2-tier Distant/Close model was reframed onto a bidirectional
−5..+5 bond-strain gauge (Distant −2..+5 start 0; Close −5..+5 start −2;
rupture at +5 both tiers; −5 = Tempered, Close-only, absorbs the next rupture
trigger once). The pre-ED-912 one-way 0→capacity accumulator (Distant 4 /
Close 7, PP-632) is struck. This module was rebuilt onto the gauge 2026-07-08
(C-TW-12), matching the doc side that landed in knots_v30 §6 / fieldwork_v30 §5.6b.

Cyclic resolution: knots depends on coherence (apply_coherence_delta on
rupture — the −1 Coherence loss is [UNVERIFIED post-ED-912], see the
RUPTURE_COHERENCE_LOSS note) and conviction (Scar on a positive-strain Close
break per §6.1). Both via late-import inside function bodies — no
module-load-time cycle.

[ASSUMPTION: knot registry stored at module level — basis: World has no
 .knots field. _store(world) router prepared for future schema migration.]

Dependencies:
  - systems/threadwork/sim/coherence (apply_coherence_delta on rupture)
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

from engine.autoload.dice_engine import roll_pool


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

# §2/§3.1 tier system — ED-912 bidirectional −5..+5 bond-strain gauge (RESOLVED 2026-06-28;
# sim rebuilt 2026-07-08, C-TW-12). [canonical: knots_v30 §2/§3.1/§6.1 + fieldwork_v30 §5.6b —
# supersedes the pre-ED-912 one-way 0→capacity accumulator (TIER_CAPACITY {Distant:4, Close:7};
# PP-632 struck).]
TIER_DISTANT = "Distant"
TIER_CLOSE = "Close"
# per-tier (min, max) strain range on the shared −5..+5 gauge
TIER_RANGE = {
    TIER_DISTANT: (-2, 5),
    TIER_CLOSE:   (-5, 5),
}
# formation start value per tier
TIER_START = {
    TIER_DISTANT: 0,
    TIER_CLOSE:   -2,
}
# §6.1 break/rupture at the +5 wear-direction ceiling (both tiers)
RUPTURE_STRAIN = 5
# −5 = Tempered (Close only): absorbs the next rupture trigger once, resetting strain to 0
TEMPERED_STRAIN = -5

# §6.1 break consequences
# [canonical: §6.1 — "Both partners take 4 Composure"]
BREAK_COMPOSURE_DAMAGE = 4
# ED-912 break/rupture Disposition: −3 (Antagonistic), floor −5 (was the pre-ED-912 min(2, disp−2))
BREAK_DISPOSITION = -3
DISPOSITION_FLOOR = -5

# §6.2 rupture consequences
# ED-912 betrayal-rupture (public citation of private counsel): Disposition → −3 (revised from −4)
RUPTURE_DISPOSITION_CITATION = -3
# [UNVERIFIED post-ED-912] mandatory −1 Coherence on rupture — originally PP-632 (struck); ED-912
# did not restate it and knots_v30 §6.2 flags it [UNVERIFIED]. Retained provisionally to match the
# doc; not a settled value.
RUPTURE_COHERENCE_LOSS = -1
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

    def to_dict(self) -> dict:
        return {
            'knot_id': self.knot_id, 'actor_a': self.actor_a, 'actor_b': self.actor_b,
            'tier': self.tier, 'strain': self.strain,
            'disposition': self.disposition, 'active': self.active,
            'formed_season': self.formed_season,
            'log': list(self.log),
        }

    @classmethod
    def from_dict(cls, d: dict) -> "Knot":
        return cls(
            knot_id=d['knot_id'], actor_a=d['actor_a'], actor_b=d['actor_b'],
            tier=d['tier'], strain=d.get('strain', 0),
            disposition=d.get('disposition', 5),
            active=d.get('active', True),
            formed_season=d.get('formed_season', 0),
            log=list(d.get('log', [])),
        )


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
        tier=tier, strain=TIER_START[tier], disposition=disp,
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

    lo, hi = TIER_RANGE.get(knot.tier, (TEMPERED_STRAIN, RUPTURE_STRAIN))
    knot.strain = max(lo, min(hi, knot.strain + strain_delta))
    knot.log.append({'source': source, 'strain_delta': strain_delta, 'strain_after': knot.strain})

    # §6.1 break at the +5 wear-direction ceiling (ED-912 gauge; both tiers share it)
    broke = knot.strain >= RUPTURE_STRAIN
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

    # ED-912 Tempered (§6.1): a Close knot at −5 absorbs the next rupture trigger ONCE,
    # resetting strain to 0 instead of rupturing.
    if knot.tier == TIER_CLOSE and knot.strain <= TEMPERED_STRAIN:
        knot.strain = 0
        knot.log.append({'source': f"tempered_absorb: {trigger}", 'tempered': True, 'strain_after': 0})
        return KnotState(knot=knot, broke=False, ruptured=False, strain_after=0,
                         notes=[f"§6.1 Tempered (−5, Close): absorbed rupture trigger '{trigger}', strain reset to 0"])

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
        # §6.1 (ED-912)
        consequences['composure_damage'] = BREAK_COMPOSURE_DAMAGE
        # Disposition → −3 (Antagonistic), floor −5
        consequences['disposition_set_to'] = max(DISPOSITION_FLOOR, BREAK_DISPOSITION)
        # ED-912: a Close Knot that broke from POSITIVE strain (reached +5) → Conviction Scar +1
        if knot.tier == TIER_CLOSE and knot.strain > 0:
            consequences['conviction_scar'] = 1
            # Late-import conviction
            try:
                from systems.characters.sim.conviction import apply_conviction_scar
                # Caller specifies which Conviction; default to a generic flag
                apply_conviction_scar(actor, f"Close Knot break (id={knot_id})",
                                      magnitude=1, conviction='Loyalty',
                                      world=world)
            except (ImportError, AttributeError):
                pass

    elif mode == 'rupture':
        # §6.2 (ED-912)
        # Disposition → −3 (betrayal-rupture value, revised from −4), floor −5
        consequences['disposition_set_to'] = max(DISPOSITION_FLOOR, RUPTURE_DISPOSITION_CITATION)
        # [UNVERIFIED post-ED-912] mandatory −1 Coherence (see RUPTURE_COHERENCE_LOSS note)
        consequences['coherence_delta'] = RUPTURE_COHERENCE_LOSS
        try:
            from systems.threadwork.sim.coherence import apply_coherence_delta
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
