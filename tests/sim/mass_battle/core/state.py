"""mass_battle.core.state — morale / discipline / rout state transitions.
Stage-1 behaviour-frozen extract from orchestration.py. The SOLE site (with the exchange pool)
of the resolver layer that MUTATES unit/subunit morale, discipline, and rout. Pure w.r.t.
modules: depends on config + duck-typed unit/atom methods (erode_morale, derive_rout,
degrade_discipline, ...) only; imports nothing from orchestration (no cycle). Re-imported by
orchestration via star-import so phase_boundary and every caller are unchanged.
[canonical: mass_battle_v30.md §A.4 morale/discipline, §A.12 rout]"""
import math
import random  # [ED-MB-0031] stochastic-rout draw — the SAME seeded global stream roll_pool uses (reproducible per seed)
from mass_battle.config import *
from mass_battle.core.exchange import D_YIELD  # [ED-MB-0024] DG-2 yield discipline gate (single owner: core.exchange)

__all__ = ['morale_check_phase', 'rout_resolution', 'discipline_check_phase']


def _rout_resilience(atom):
    """[ED-MB-0031] A subunit's inherent resistance to a morale break, 0..1, from its stable quality:
    Discipline (2->0, 5->1, saturating) blended with starting Morale (eff_morale_start on the 1-7 scale
    normalized by 7). A steady, disciplined, high-morale body (resilience -> 1) skews its break-point toward
    the ROUT_CAP (holds to ~30% losses); a loose, shaken one (resilience -> 0) breaks toward ROUT_ONSET
    (~15%). Uses starting morale (not live) so the break-point reflects inherent quality; live morale
    erosion still routs a unit independently via the canonical §A.4 path."""
    disc = max(0.0, min(1.0, (atom.eff_discipline - 2.0) / 3.0))
    ms = getattr(atom, 'eff_morale_start', 0) or 0
    # [canonical: params/factions/stats_1_7_scale.md — attributes on the 1-7 scale] normalize starting morale to 0..1
    mor = max(0.0, min(1.0, ms / 7.0)) if ms else 0.5
    return 0.5 * disc + 0.5 * mor


def _stochastic_break(atom, loss_frac):
    """[ED-MB-0031, Jordan 2026-07-23: routs at 15% (early) to 30% (upper).] du Picq will-to-fight collapse:
    each subunit draws ONE fractional break-point in the [ROUT_ONSET, ROUT_CAP] casualty band, skewed by
    its resilience, and routs once its casualty fraction (`loss_frac`, passed in by the caller = 1 - survival
    fraction) crosses it. Returns True if the subunit breaks this check. Fractional throughout (random draw +
    fractional band + fractional loss). Reproducible under the seeded RNG; only consumed when
    PC_STOCHASTIC_ROUT is on (else never called -> byte-exact)."""
    bp = getattr(atom, '_rout_breakpoint', None)
    if bp is None:
        resil = _rout_resilience(atom)
        # skew the uniform draw toward the CAP (later break) as resilience rises: exponent < 1 pushes high.
        skewed = random.random() ** (1.0 / (0.5 + resil))
        bp = ROUT_ONSET_FRAC + (ROUT_CAP_FRAC - ROUT_ONSET_FRAC) * skewed
        atom._rout_breakpoint = bp
    return loss_frac >= bp


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
        # [DG-4, ED-MB-0002, 2026-07-04 Jordan ruling: "Subunit morale combination of own morale and
        # overall morale; more likely to wilt if other subunits losing, more likely to rally if other
        # subunits winning."] Phase-start snapshot of every living subunit's morale, taken BEFORE any
        # mutation this phase. [2026-07-04 adversarial-review fix, two findings]: (1) siblings pull
        # toward this FIXED snapshot, not toward siblings' already-updated values later in this same
        # loop -- the original per-atom-live-read version was a Gauss-Seidel order-dependency that
        # systematically favored whichever subunit happened to iterate first. (2) the pull is applied
        # BEFORE this atom's own casualty/exhaustion erosion below (reordered from after), so a
        # subunit's own bad phase always has the final say on whether IT routs this phase -- the
        # original after-erosion ordering let a healthy sibling's pull retroactively rescue a subunit
        # from a same-phase rout its own casualties would otherwise have caused, before
        # rout_resolution ever saw the value. A sibling's state can soften/harden the morale a
        # subunit ENTERS this phase's own erosion with; it can no longer erase that erosion's result.
        snapshot = {id(s): s.eff_morale for s in u.subunits if not s.routed}
        # step 3 (Jordan directive 2026-06-03): canonical Size-fraction morale triggers (§A.4),
        # replacing the per-tick absolute-damage erosion. Routs occur at meaningful casualty levels,
        # not ~98% intact. No general-floor in the unit duel (units rout from their own casualties).
        for atom in u.subunits:
            if atom.routed:
                continue
            siblings = [s for s in u.subunits if s is not atom and not s.routed]
            if siblings:
                sib_troops = sum(s.troop_count for s in siblings)
                if sib_troops > 0:
                    sib_agg = sum(snapshot[id(s)] * s.troop_count for s in siblings) / sib_troops
                    pull = MORALE_SIBLING_PULL * (sib_agg - snapshot[id(atom)])
                    if pull:
                        atom.pull_morale(pull)
            frac = atom.cohesion           # single-subunit: == u.hp/u.hp_max (byte-exact); else this subunit's own
            loss = 0.0
            if frac < 0.50: loss += 1.0    # [canonical: mass_battle_v30.md §A.4 — Size<50% morale trigger] Size < 50% max -> -1
            if frac < 0.25: loss += 1.0    # Size < 25% max -> -1 additional
            if u.broken: loss += 1.0       # unit formation-broken pressure (kept unit-scoped for byte-exactness)
            if atom.eff_stamina <= 0 and atom.eff_discipline > 0 and u.command > 0:
                loss += 1.0 / (atom.eff_discipline * u.command)   # per-subunit exhaustion pressure
            # [ED-MB-0024, DG-2 §2.2 EMERGENT auto-entry] When the casualty-fraction trigger pushes a
            # disciplined subunit (eff_discipline >= D_YIELD, parent command > 0) toward the rout cliff, it
            # ENTERS `yielding` -- it starts giving ground in good order rather than only eroding. Sets the
            # state; the already-built yield consumption sites (give-ground movement, facing-lock, pool
            # malus) do the rest. A sub-D_YIELD subunit is unaffected (routs as today). Gated OFF by default
            # (highest blast radius per §4.3) -> inert/byte-exact. The erosion-BRAKE calibration (whether
            # yielding should also reduce `loss`) stays deferred (needs_jordan) -- state entry only here.
            if (PC_YIELD_EMERGENT and not atom.yielding and frac < 0.50  # [canonical: mass_battle_v30.md §A.4 — Size<50% trigger, same threshold as the loss line above]
                    and atom.eff_discipline >= D_YIELD and u.command > 0 and atom.unit_type != 'ranged'):
                atom.yielding = True
            if loss:
                atom.erode_morale(min(loss, 3.0))   # cap -3 per Cascade Phase (§A.4); routes own-else-Unit
            # [ED-MB-0031] Stochastic morale break at the historical 15-30% casualty band (du Picq): the
            # canonical §A.4 steps above don't fire until 50% losses, so units grind to ~58% before breaking.
            # When gated on, a subunit whose casualties cross its own drawn break-point routs NOW (drive its
            # morale <=0 -> rout_resolution breaks it this phase). Fires AFTER the §A.4 erosion so a unit
            # already collapsing by canon still routs; this only pulls the break EARLIER, into the band.
            if PC_STOCHASTIC_ROUT and not atom.routed and _stochastic_break(atom, 1.0 - frac):
                atom.erode_morale(atom.eff_morale + 1.0)   # will breaks -> morale <=0 -> routs


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
