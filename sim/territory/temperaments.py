"""
sim/territory/temperaments.py — Per-territory Public Temperament (PP-686 v2 Phase B Stage 6)

Canon source: designs/territory/territory_temperaments_v30.md

Implements §2 per-territory temperament authoring (17 provinces, T1-T17) +
§3 per-faction aggregation + §4 drift dynamics under peninsular_strain_shock.

5-typology: pragmatic / traditional / balanced / principled / outcomes-only,
each with α (outcomes weight) and β (conduct weight) coefficients.

[ASSUMPTION: temperament data stored as module-level constants — basis:
 canon §2 authors initial values; drift state would belong on World per
 schema migration pattern, but no consumer currently mutates drift.
 World schema migration for drift state deferred until first consumer
 lands.]

Dependencies:
  - sim/autoload/game_state
  - sim/territory/settlement

Entry points:
  - temperament_of(territory_id) -> str
  - temperament_modifiers(territory_id, action_type) -> dict
"""
from __future__ import annotations

from dataclasses import dataclass


# §1 5-temperament typology with α/β weights
# [canonical: territory_temperaments_v30 §1 Purpose table]
TEMPERAMENT_WEIGHTS = {
    "pragmatic":     {"alpha": 0.7, "beta": 0.3},
    "traditional":   {"alpha": 0.3, "beta": 0.7},
    "balanced":      {"alpha": 0.5, "beta": 0.5},
    "principled":    {"alpha": 0.2, "beta": 0.8},
    "outcomes-only": {"alpha": 0.9, "beta": 0.1},
}

# §2 Per-territory authoring — canonical table values
# [canonical: territory_temperaments_v30 §2 Per-Territory Temperament Table]
TERRITORY_TEMPERAMENTS = {
    "T1":  "pragmatic",       # Valorsplatz, Crown capital, river-sea trade
    "T2":  "traditional",     # Kronmark, Crown farmland heartland
    "T3":  "balanced",        # Lowenskyst, NE Altonian-pass garrison
    "T4":  "traditional",     # Grauwald, Varfell highland Einhir heritage
    "T5":  "traditional",     # Feldmark, Crown breadbasket
    "T6":  "outcomes-only",   # Stillhelm, Calamity-adjacent (south Crown gate)
    "T7":  "traditional",     # Rendstad, Hafenmark timber valley
    "T8":  "pragmatic",       # Gransol, Hafenmark constitutional capital
    "T9":  "principled",      # Himmelenger, Church cathedral city
    "T10": "balanced",        # Spartfell, NW Altonian-pass garrison
    "T11": "traditional",     # Halvardshelm, Varfell fjord communities
    "T12": "balanced",        # Sigurdshelm, Varfell seat
    "T13": "outcomes-only",   # Oastad, Calamity-adjacent (south Varfell gate)
    "T14": "balanced",        # Ehrenfeld, Crown military hinge
    "T15": "outcomes-only",   # Askeheim, Calamity epicenter
    "T16": "pragmatic",       # Schoenland, independent island republic
    "T17": "balanced",        # Halvarshelm, Hafenmark mining + Guild
}

# §4 Drift dynamics
# [canonical: §4 — "territory.temperament_drift = clamp(
#  territory.temperament_drift + 0.1 × strain_delta, -1, +1)"]
DRIFT_PER_STRAIN_UNIT = 0.1
DRIFT_MIN = -1.0
DRIFT_MAX = +1.0

# Per-faction aggregate temperaments (§3 uniform-weighted approximation)
# [canonical: §3 table]
FACTION_AGGREGATE_TEMPERAMENTS = {
    "Crown":     {"alpha_approx": 0.50, "beta_approx": 0.50,
                  "description": "balanced-leaning"},
    "Church":    {"alpha_approx": 0.20, "beta_approx": 0.80,
                  "description": "strongly principled"},
    "Hafenmark": {"alpha_approx": 0.55, "beta_approx": 0.45,
                  "description": "mildly pragmatic"},
    "Varfell":   {"alpha_approx": 0.50, "beta_approx": 0.50,
                  "description": "balanced (skewed by traditional)"},
}


# Module-level drift state (per-territory cumulative drift)
# Keyed by territory_id; updated by env.peninsular_strain_shock callers.
_drift_state: dict[str, float] = {}


def _drift_store(world=None):
    """Drift store — module-level for now."""
    return _drift_state


def temperament_of(territory_id: str) -> str:
    """Return the canonical temperament label for a territory.

    Returns 'balanced' as a safe default for unknown territory_ids.
    """
    return TERRITORY_TEMPERAMENTS.get(territory_id, "balanced")


def temperament_modifiers(territory_id: str, action_type: str) -> dict:
    """Return α/β coefficients + any action-specific modifier dict for a territory.

    action_type is preserved in signature for callers (faction_action,
    contest, etc) that may extend with action-specific logic. Currently
    returns the canonical α/β pair regardless of action_type, since canon
    does not yet specify per-action-type α/β shifts.

    Returns dict with keys: alpha, beta, temperament, drift, drift_applied.
    """
    temp = temperament_of(territory_id)
    weights = TEMPERAMENT_WEIGHTS[temp]
    drift = _drift_store().get(territory_id, 0.0)
    # Drift biases toward outcomes-only per §4
    # [canonical: §4 — "Drift bias applies to faction effective-temperament
    #  recomputation each Accounting."]
    # Apply drift as α shift toward outcomes-only (α=0.9, β=0.1)
    # Drift +1 = full shift to outcomes-only; -1 = no shift (canon doesn't
    # spec negative-drift semantics).
    alpha = weights["alpha"]
    beta = weights["beta"]
    if drift > 0:
        # Linear interp toward outcomes-only weights
        outcomes_alpha = TEMPERAMENT_WEIGHTS["outcomes-only"]["alpha"]
        outcomes_beta = TEMPERAMENT_WEIGHTS["outcomes-only"]["beta"]
        alpha = alpha + drift * (outcomes_alpha - alpha)
        beta = beta + drift * (outcomes_beta - beta)
    return {
        "alpha": alpha,
        "beta": beta,
        "temperament": temp,
        "drift": drift,
        "drift_applied": drift > 0,
        "action_type": action_type,
    }


def apply_strain_shock(strain_delta: float, affected_territories: list,
                       world=None) -> dict:
    """Apply §4 drift dynamics under env.peninsular_strain_shock.

    For each affected territory, increment its drift_state by
    0.1 × strain_delta, clamped to [-1, +1]. Returns a dict mapping
    territory_id → new drift value.
    """
    # [canonical: §4 drift dynamics pseudocode]
    if strain_delta <= 0:
        return {}
    store = _drift_store(world)
    updated = {}
    for tid in affected_territories:
        new_drift = store.get(tid, 0.0) + DRIFT_PER_STRAIN_UNIT * strain_delta
        new_drift = max(DRIFT_MIN, min(DRIFT_MAX, new_drift))
        store[tid] = new_drift
        updated[tid] = new_drift
    return updated


def get_faction_aggregate(faction_name: str) -> dict:
    """Return the §3 per-faction aggregate temperament (uniform-weighted approximation)."""
    return FACTION_AGGREGATE_TEMPERAMENTS.get(faction_name, {})


def reset_drift(world=None):
    """Test helper."""
    _drift_store(world).clear()
