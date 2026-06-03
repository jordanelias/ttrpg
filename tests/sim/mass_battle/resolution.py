"""mass_battle.resolution — sigma-leverage head: pool roll, degree, morale/charge-shock
sigma, softcap, net-boost. Behaviour-frozen P-A extract. Depends on config + percell."""
import math, random
from mass_battle.config import *
from mass_battle.percell import *

__all__ = ['roll_pool', 'compute_degree', '_morale_sigma', '_charge_shock_sigma', '_sigma_softcap', '_sigma_net_boost', '_unit_braced', '_wall_prep', '_disc_prep', '_depth_prep', 'trace_event', 'start_trace', 'get_trace']

# ─── passive mechanical-trace collector ─────────────────────────────────────
# Observe-only. Records per-mechanic internals (melee contest, volley, per-tick markers) when ON.
# Default OFF -> trace_event is a no-op -> ENGINE BYTE-EXACT. The trace never feeds back into any
# mechanic, so ON and OFF produce identical outcomes; it only makes a run auditable down to the
# mechanic that produced each value.
_battle_trace = []
_trace_on = False
def start_trace(on=True):
    """Clear the buffer and enable/disable mechanical tracing for the next run."""
    global _battle_trace, _trace_on
    _battle_trace = []
    _trace_on = bool(on)
def trace_event(cat, **kw):
    """Append one mechanical event. No-op unless tracing is ON (byte-exact when off)."""
    if _trace_on:
        kw['cat'] = cat
        _battle_trace.append(kw)
def get_trace():
    """Return a copy of the recorded events."""
    return list(_battle_trace)

def roll_pool(n, tn=7):
    net = 0
    for _ in range(max(1, n)):
        f = random.randint(1, 10)
        if f == 1:         net -= 1
        elif tn <= f <= 9: net += 1
        elif f == 10:      net += 2
    return net

def compute_degree(net, ob):
    if net <= 0:                    return "Failure"
    if net >= 2 * ob and net >= 3:  return "Overwhelming"
    if net >= ob:                   return "Success"
    return "Partial"

def _morale_sigma(u):
    # Graded morale effectiveness as a delta-sigma: 0 at full morale, down to -MORALE_SIGMA_SCALE near rout.
    # A breaking unit wins fewer exchanges and deals less -> it cannot out-damage the winner pre-rout.
    # [historical anchor: Ardant du Picq / Clausewitz — combat effectiveness degrades progressively as
    #  cohesion erodes, BEFORE the rout; most casualties fall in the pursuit, not the stand]
    if not MORALE_FIX or not getattr(u, 'morale_start', 0): return 0.0
    frac = max(0.0, min(1.0, u.morale / u.morale_start))
    return MORALE_SIGMA_SCALE * (frac - 1.0)
def _unit_braced(unit):
    """True if any subunit carries the 'brace' instruction (the FM brace tactic). Gates the brace
    benefit (charge-resistance) and the reciprocal charge-recoil; INERT for instruction-less units
    (the historical gauge + signature scenarios) -> byte-exact."""
    return any('brace' in getattr(su, 'instructions', ()) for su in getattr(unit, 'subunits', ()))

def _disc_prep(disc):
    """Discipline -> preparedness 0..1. SHARED by the charge-shock brace gate (independent retention)
    and the recoil (conjunctive) so the disc curve has one source. disc 2 -> 0, disc 5 -> 1 (saturates)."""
    return max(0.0, min(1.0, (disc - 2) / 3.0))                    # [class-B] shared disc prep curve

def _depth_prep(depth):
    """Engaged depth -> preparedness 0..1. SHARED (one source for the depth curve).
    depth 1 -> 0, depth >= PC_SHOCK_DEPTH_REF -> 1."""
    ref = PC_SHOCK_DEPTH_REF if PC_SHOCK_DEPTH_REF > 1.0 else 2.0   # [class-B] depth-ref guard
    return max(0.0, min(1.0, (depth - 1.0) / (ref - 1.0)))

def _wall_prep(unit, contact_cells):
    """Conjunctive wall-preparedness for the reciprocal charge-recoil: high only when disciplined
    AND deep (a true prepared pike block, not a deep mob or a thin elite line). Uses the shared
    _disc_prep/_depth_prep curves. [bottom-up: discipline x _defender_depth -- the wall that breaks a charge.]"""
    disc = getattr(unit, 'discipline', 5)                          # [class-B] default disc mirrors _charge_shock_sigma
    return _disc_prep(disc) * _depth_prep(_defender_depth(unit, contact_cells))

def _charge_shock_sigma(defender, def_cells, zone):
    """Phase 3: DEFENDER moral-shock delta-sigma (<=0) on a charge impact.
    Cavalry's weapon is the MORAL impulse (du Picq), gated by the defender's preparedness:
    near-zero vs a braced+disciplined+deep defender facing the charge (Waterloo squares),
    catastrophic vs an in-line / shallow / rear-charged / already-shaken defender (Albuera,
    Cannae, Hastings-post-feint). Applied to the defender's offensive net successes -> it
    fights worse that exchange. Composes with _morale_sigma (one morale channel, Lesson 1).
    [historical anchor: du Picq Battle Studies; Waterloo/Albuera; precedents_warfare §1.1.
     bottom-up: stance/discipline/_defender_depth/octagon zone/morale_start — all engine state.]
    """
    if not PER_CELL:
        return 0.0
    # facing gate: can the defender face the charge?
    if zone == "GREEN":   g_face = PC_SHOCK_FRONT      # faced charge mostly absorbed
    elif zone == "RED":   g_face = PC_SHOCK_REAR       # rear bypass (cannot face it)
    else:                 g_face = 1.0                 # YELLOW flank
    # brace gate (multiplicative): hold-stance x discipline x depth, floored
    b_stance = PC_SHOCK_HOLD_BRACE if (getattr(defender, 'stance', 'balanced') == 'hold' or _unit_braced(defender)) else 1.0
    disc = getattr(defender, 'discipline', 5)
    b_disc = 1.0 - _disc_prep(disc) * (1.0 - PC_SHOCK_DISC_FULL)        # independent disc retention (shared prep curve)
    depth = _defender_depth(defender, def_cells)
    b_depth = 1.0 - _depth_prep(depth) * (1.0 - PC_SHOCK_DEPTH_FULL)    # independent depth retention (shared prep curve)
    g_brace = max(PC_SHOCK_BRACE_FLOOR, min(1.0, b_stance * b_disc * b_depth))
    # shaken amplifier: a wavering defender takes more
    ms = getattr(defender, 'morale_start', 0) or 0
    frac = max(0.0, min(1.0, defender.morale / ms)) if ms else 1.0
    a_shaken = 1.0 + PC_SHOCK_SHAKEN_GAIN * (1.0 - frac)
    return -PC_CHARGE_SIGMA * g_face * g_brace * a_shaken

def _sigma_softcap(x, m=1.5):                 # [canonical: modifier_system_spec.md §3.1 saturating]
    return m * math.tanh(x / m)
def _sigma_net_boost(net_sigma, pool, tn=7):  # mu-shift; [canonical: params/core.md continuous engine; modifier_system_spec §2.1]
    _SIG = {6: 0.806, 7: 0.800, 8: 0.781}     # [canonical: params/core.md EV table] sigma per die at TN
    return _sigma_softcap(net_sigma) * _SIG.get(tn, 0.800) * math.sqrt(max(1, pool))
