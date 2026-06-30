"""mass_battle.core.attrition — Lanchester attrition LAW application.
Stage-1 behaviour-frozen extract from orchestration.py. Applies the linear-law contact-frontage
term (the square-law volley term still lives in volley_phase pending a later increment). Pure:
config + duck-typed unit.hp/ncells only; the COEFFICIENTS (K_LINEAR/REF/DENSITY_REF) are config
tunables injected here, not authored — the resolver APPLIES the law. No up-DAG import (no cycle).
[spec designs/audit/2026-06-01-massbattle-stub-wiring/mb_lanchester_design.md §3a; Lanchester Linear Law]"""
from mass_battle.config import *

__all__ = ['_lanchester_strength']


def _lanchester_strength(contact_cells, unit=None):
    """P-L Linear Law: enemy effective strength IN CONTACT, expressed as engaged
    contact-frontage (distinct contact columns) normalized to ~1 at LANCHESTER_STRENGTH_REF
    so K_LINEAR composes with the canonical exchange scale (PP-233 successes×(1+Power)).
    Frontage-capped BY CONSTRUCTION: contact columns can never exceed the meeting frontage,
    so numerical superiority is a LINEAR edge (via overlap/envelopment), never square.
    Mode-agnostic: contact cells exist under PER_CELL 0 and 1; depletion enters via the
    pool (effective_size→degree) and, under PER_CELL=1, via dead columns leaving contact.
    [spec mb_lanchester_design.md §3a; Lanchester Linear Law = frontage-capped ancient melee.]
    """
    if not contact_cells:
        return 0.0
    n_eng_cols = len(set(c for r, c in contact_cells))
    if unit is not None and getattr(unit, 'ncells', 0):
        tpc = unit.hp / unit.ncells   # all-fight: current per-cell troops (thins as casualties mount)
        return n_eng_cols * (min(tpc, CELL_CAP) / LANCHESTER_DENSITY_REF) / LANCHESTER_STRENGTH_REF
    return n_eng_cols / LANCHESTER_STRENGTH_REF
