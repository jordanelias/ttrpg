"""
sim/thread/co_movement.py — Co-Movement Version C with 15 cards (ED-577)

Canon source: designs/threadwork/threadwork_v30.md Part 4 (Co-Movement)

Implements the 15-card canonical deck (CM-01 through CM-15) per §4.3
ED-577. CM-16/17/18 are Mending-specific additions per §7.1; not
implemented here (will land with Mending sim integration). Deck is global
(not per-territory), shuffled when exhausted per ED-577-02.

[ASSUMPTION: deck state stored at module level — basis: World has no
 .comovement_deck field. Module owns deck shuffle state; world parameter
 reserved for future schema migration.]

Dependencies:
  - sim/thread/operations (target of Co-Movement firing)
  - sim/autoload/dice_engine (rng)

Entry points:
  - draw_comovement_card(op_type, depth, world) -> CoMovementCard
  - apply_comovement_effects(card, op_result, world) -> dict
"""
from __future__ import annotations

import random
from dataclasses import dataclass, field
from typing import Optional


# §4.3 ED-577 — 15 canonical cards (CM-16/17/18 Mending-specific deferred)
# Each card has (id, name, actualized_effect_dict, unactualized_effect_dict)
# Effects dicts: 'ms_delta', plus any side-effect markers.
# [canonical: §4.3 ED-577 Co-Movement Cards 1-15 table]

CO_MOVEMENT_CARDS = [
    # (id, name, actualized_ms_delta, actualized_notes, unactualized_ms_delta, unactualized_notes)
    ("CM-01", "Temporal Drift", -1, "One clock advances 1 tick", 0, "Clock advance still applies"),
    ("CM-02", "Substrate Ripple", -2, "All Thread ops in territory +1 Ob next season", -1, "No Ob change"),
    ("CM-03", "Echo Cascade", -1, "One resolved Thread op re-manifests minor", 0, "No effect"),
    ("CM-04", "Coherence Bleed", -1, "Lowest-Coherence entity: Coherence -1", 0, "Coherence loss still applies"),
    ("CM-05", "Anchor Settling", +1, "One Thread Witness Node stabilises", +1, "No Node effect"),
    ("CM-06", "Resonance Bloom", -2, "Each Practitioner: +1D next Thread op", -1, "No bonus"),
    ("CM-07", "Scar Memory", 0, "One Dissolution residue visible to non-Sensitives 1 scene", 0, "No effect"),
    ("CM-08", "Temporal Fold", -1, "One POP +1 season free depth", 0, "No depth extension"),
    ("CM-09", "Rendering Surge", -3, "All Thread entities: forced Coherence check Ob 1", -2, "No Coherence check"),
    ("CM-10", "Ground Harmony", +2, "Mending in territory: -1 Ob this season", +1, "No Ob change"),
    ("CM-11", "Witness Flare", 0, "Church Attention Pool +1; all Nodes activate", 0, "Church Attention Pool +1"),
    ("CM-12", "Ground Stability", +1, "Territory Thread Debt cleared", +1, "Debt not cleared"),
    ("CM-13", "Epistemic Breach", -1, "One non-Sensitive NPC: TS=15 for 1 scene; Certainty pressure; Church Attention +1", 0, "Church Attention +1"),
    ("CM-14", "Substrate Assertion", -3, "One Locked entity: Lock strength +1", -1, "No Lock change"),
    ("CM-15", "Dissolution Wake", -2, "Dissolution residue gains intensity", -1, "Residue intensity +1 if exists"),
]


@dataclass
class CoMovementCard:
    """A drawn Co-Movement card with its effect profile."""
    card_id: str
    name: str
    actualized: bool                # Whether actual effect fires (Object/Personal scale → unactualized)
    ms_delta: int
    notes: str


# Module-level deck state
_deck_state: dict = {'remaining': [], 'discard': []}


def _store(world):
    """Co-Movement deck state: world.comovement_deck if world supplied,
    else module-level fallback."""
    if world is not None and hasattr(world, 'comovement_deck'):
        return world.comovement_deck
    return _deck_state


def _shuffle_deck(rng=None):
    """Shuffle full 15-card deck back into _remaining."""
    cards = list(CO_MOVEMENT_CARDS)
    if rng is not None:
        rng.shuffle(cards)
    else:
        random.shuffle(cards)
    return cards


def draw_comovement_card(op_type: str, depth: str = "Object", world=None,
                         rng=None) -> CoMovementCard:
    """§4.3 Draw 1 card per Thread operation.

    op_type: 'Weaving' / 'Pulling' / 'Locking' / 'Dissolution' / 'POP' /
             'Mending' / 'Leap' (Mending uses 18-card deck per §7.1; here
             we use 15-card deck and flag if Mending requested).
    depth: scale label per Three-Axis Ob (Object/Personal/Relational/Field/
           Structural/Foundational). Determines actualized vs unactualized
           per §4 — "Object or Personal scale operation | 0 (co-movement
           fires but practitioner's rendering absorbs negligibly)".
    """
    # [canonical: §4 — "Object or Personal scale operation | 0
    #  (co-movement fires but practitioner's rendering absorbs negligibly)"]
    actualized = depth not in ("Object", "Personal")

    rng = rng if rng is not None else (world.rng if world is not None and hasattr(world, 'rng') else None)
    if rng is None:
        rng = random.Random()

    state = _store(world)
    if not state['remaining']:
        # [canonical: §4.3 — "Reshuffle when all 18 cards drawn (global deck,
        #  not per-territory)". Using 15-card subset until §7.1 lands.]
        state['remaining'] = _shuffle_deck(rng=rng)
        state['discard'] = []

    raw = state['remaining'].pop(0)
    state['discard'].append(raw)

    card_id, name, act_ms, act_notes, unact_ms, unact_notes = raw

    if actualized:
        return CoMovementCard(
            card_id=card_id, name=name, actualized=True,
            ms_delta=act_ms, notes=act_notes,
        )
    return CoMovementCard(
        card_id=card_id, name=name, actualized=False,
        ms_delta=unact_ms, notes=unact_notes,
    )


def apply_comovement_effects(card: CoMovementCard, op_result, world) -> dict:
    """Apply the card's MS delta + side effects.

    op_result: the OperationResult from sim/thread/operations (for chaining
               MS effects). Not currently mutated; included for future
               territory-specific side-effect routing.

    Returns dict with applied effects.
    """
    ms_before = world.clocks.get('MS', 80.0)
    # [2026-05-20 migration] route through ms_track.apply_ms_delta — single
    # canonical surface for MS arithmetic per PP-255. Was: inline clamp.
    from sim.peninsular.ms_track import apply_ms_delta
    new_ms = apply_ms_delta(card.ms_delta, source=f"co_movement {card.card_id}", world=world)
    return {
        'card_id': card.card_id,
        'card_name': card.name,
        'ms_before': ms_before,
        'ms_after': new_ms,
        'ms_delta': card.ms_delta,
        'actualized': card.actualized,
        'notes': card.notes,
    }


def reset_deck(world=None):
    """Test helper."""
    state = _store(world)
    state['remaining'] = []
    state['discard'] = []
