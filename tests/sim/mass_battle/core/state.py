"""mass_battle.core.state — morale / discipline / rout state transitions.
Stage-1 behaviour-frozen extract from orchestration.py. The SOLE site (with the exchange pool)
of the resolver layer that MUTATES unit/subunit morale, discipline, and rout. Pure w.r.t.
modules: depends on config + duck-typed unit/atom methods (erode_morale, derive_rout,
degrade_discipline, ...) only; imports nothing from orchestration (no cycle). Re-imported by
orchestration via star-import so phase_boundary and every caller are unchanged.
[canonical: mass_battle_v30.md §A.4 morale/discipline, §A.12 rout]"""
import math
from mass_battle.config import *

__all__ = ['morale_check_phase', 'rout_resolution', 'discipline_check_phase']


def morale_check_phase(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """v17: phase-boundary morale = exhaustion pressure ONLY (D-7 fix).
    Per-tick morale handles casualty-based triggers separately.
    Exhausted units lose -1 morale at phase boundary (within cap).
    Floor is NOT overridden here — that's the per-tick trigger's job.
    [canonical: designs/provincial/mass_battle_v30.md §A.4 — morale floor 1 while general present;
     §A.4 — cap −3 non-general morale loss per Cascade Phase]"""
    for u in [unit_a, unit_b]:
        if u.routed:
            continue
        # step 3 (Jordan directive 2026-06-03): canonical Size-fraction morale triggers (§A.4),
        # replacing the per-tick absolute-damage erosion. Routs occur at meaningful casualty levels,
        # not ~98% intact. No general-floor in the unit duel (units rout from their own casualties).
        for atom in u.subunits:
            if atom.routed:
                continue
            frac = atom.cohesion           # single-subunit: == u.hp/u.hp_max (byte-exact); else this subunit's own
            loss = 0.0
            if frac < 0.50: loss += 1.0    # [canonical: mass_battle_v30.md §A.4 — Size<50% morale trigger] Size < 50% max -> -1
            if frac < 0.25: loss += 1.0    # Size < 25% max -> -1 additional
            if u.broken: loss += 1.0       # unit formation-broken pressure (kept unit-scoped for byte-exactness)
            if atom.eff_stamina <= 0 and atom.eff_discipline > 0 and u.command > 0:
                loss += 1.0 / (atom.eff_discipline * u.command)   # per-subunit exhaustion pressure
            if loss:
                atom.erode_morale(min(loss, 3.0))   # cap -3 per Cascade Phase (§A.4); routes own-else-Unit


def rout_resolution(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """Units with morale ≤ 0 rout.
    [canonical: designs/provincial/mass_battle_v30.md §A.12 —
     "Routing: Slow/Standard cannot fight back."
     "Pursuit: Fast units only. Routing unit loses Size equal to pursuer net
      Offence successes (no Defence) each turn. Recall: Command Ob 2."]
    v19: Standard infantry cannot pursue. Pursuit is a level-2 mechanic
    that fires at the battle-map level when a Fast unit is adjacent.
    Morale Cascade (§A.12): friendly units in same engagement make
    Discipline check Ob 1 on rout — modeled when multi-unit engagements exist."""
    for u, opponent in [(unit_a, unit_b), (unit_b, unit_a)]:
        if u.routed or u.broken:
            continue
        for atom in u.subunits:
            if not atom.routed and atom.eff_morale <= 0:
                atom.routed = True   # this subunit's eroding morale reached 0 -> it breaks ("a section of the line")
        u.derive_rout()              # unit routs iff agg morale <= 0 / all subunits routed / general gone (byte-exact single-subunit)
            # No pursuit damage from Standard infantry (canonical: Fast only).
            # Pursuit damage will be handled at the battle-map level (level 2)
            # when cavalry (G-11) and multi-unit engagements (D-3) are implemented.


def discipline_check_phase(unit_a, unit_b, phase_idx):  # noqa: ARG001
    """v18 (D-6): discipline degradation at phase boundary using cumulative loss.
    [canonical: params/mass_combat.md §Discipline Degradation —
     deterministic, fires when effective_size loss > threshold AND asymmetric]
    Roll-input fidelity: each subunit's Discipline degrades from ITS OWN cumulative
    Size loss, not the whole unit's -- so a fresh reserve subunit does not crack from casualties
    its engaged siblings took. This makes Discipline consistent with morale_check_phase, which
    already reads the per-subunit cohesion. A single-subunit unit uses the exact unit-loss
    expression (mirrors cohesion's byte-exact fast-path) so the homogeneous gauge is unchanged.
    The loss-asymmetry baseline stays the opposing UNIT's loss (the 1v1 engine has no per-subunit
    opponent mapping); for a single-subunit unit this reduces to the exact old `my_loss > their_loss`.
    """
    a_loss = (unit_a.hp_max - unit_a.hp) / BLOCK_SIZE if BLOCK_SIZE else 0
    b_loss = (unit_b.hp_max - unit_b.hp) / BLOCK_SIZE if BLOCK_SIZE else 0
    for u, their_loss in [(unit_a, b_loss), (unit_b, a_loss)]:
        if u.routed or u.broken:
            continue
        single = len(u.subunits) == 1
        for atom in u.subunits:
            if atom.routed or atom.broken:
                continue
            # per-subunit own Size loss drives THIS subunit's degradation
            if single:
                my_loss = (u.hp_max - u.hp) / BLOCK_SIZE if BLOCK_SIZE else 0   # exact old value -> byte-exact
            else:
                my_loss = (atom._start_troops - atom.cur_troops) / BLOCK_SIZE if BLOCK_SIZE else 0
            disc_hits = int(my_loss / DISCIPLINE_LOSS_THRESHOLD)
            # already applied for THIS subunit (single-subunit: == u.discipline_start - u.discipline)
            already_applied = atom.eff_discipline_start - atom.eff_discipline
            if disc_hits > already_applied and my_loss > their_loss:
                atom.degrade_discipline()   # -1 toward 0, routes own-else-Unit
        u.check_drift()
