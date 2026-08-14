"""mass_battle.resolution — sigma-leverage head: pool roll, degree, morale/charge-shock
sigma, softcap, net-boost. Behaviour-frozen P-A extract. Depends on config + percell."""
import math, random
from mass_battle.config import *
from mass_battle.percell import *

__all__ = ['roll_pool', 'roll_pool_fractional', 'compute_degree', '_morale_sigma', '_charge_shock_sigma', '_sigma_softcap', '_sigma_net_boost', '_unit_braced', '_subunit_braced', '_wall_prep', '_disc_prep', '_depth_prep', 'trace_event', 'start_trace', 'get_trace', 'tracing_on']

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
def tracing_on():
    """True iff mechanical tracing is currently enabled. Lets a caller (e.g. an expensive per-tick
    snapshot builder in orchestration.py) skip its work entirely when tracing is off, instead of
    computing-then-discarding via trace_event's own no-op branch. Query-only; no engine effect."""
    return _trace_on

def roll_pool(n, tn=7):  # [canonical: params/core.md §TN Values — TN 7 standard]
    net = 0
    for _ in range(max(1, n)):
        f = random.randint(1, 10)
        if f == 1:         net -= 1
        elif tn <= f <= 9: net += 1  # [canonical: params/core.md — canonical face rule 1=-1, 2-6=0, 7-9=+1, 10=+2]
        elif f == 10:      net += 2
    return net

def roll_pool_fractional(pool, tn=7):  # [canonical: params/core.md §TN Values — TN 7 standard]
    """[ED-MB-0032, Jordan: "pool must be fractional."] Roll a CONTINUOUS combat pool without flooring it
    to an integer die count. The integer part rolls real d10s (the discrete stochastic base); the
    fractional remainder is realised as ONE extra real die rolled with probability `frac`.

    [Fable-audit A3 fix, 2026-07-24] The prior version added a DETERMINISTIC `frac*PER_DIE_NET_EV` mu-shift.
    Because `compute_degree` thresholds at `net<=0` (Failure), that constant EV crossed the boundary
    discontinuously — P(Failure) jumped ~31.8%->10% between pool 3.0 and 3.000001, and a sub-1 pool could
    NEVER Fail (a near-dead sliver became a guaranteed chip-damage machine). Realising the die stochastically
    preserves the EV EXACTLY (E[extra die] = PER_DIE_NET_EV = frac contribution when drawn w.p. frac), AND
    restores the die's own variance, AND keeps the Failure boundary intact (an all-fractional sub-1 pool can
    now roll a 1 -> net<0 -> Failure). [canonical: params/core.md continuous engine — the discrete dice carry
    all variance; no deterministic mu-shift.]"""
    lo = math.floor(max(0.0, pool))
    frac = max(0.0, pool - lo)
    net = roll_pool(lo, tn) if lo >= 1 else 0
    if frac > 0.0 and random.random() < frac:
        net += roll_pool(1, tn)
    return net

# [ED-MB-0051 / plan-v2 A2] Absolute epsilon for the degree boundaries.
#
# THE DEFECT. `net` is continuous (fractional pools, the sigma mu-shift), so a value that is
# MATHEMATICALLY on a boundary can arrive one ulp to the wrong side of it — and every boundary here
# is a hard step in `DAMAGE_BY_DEGREE`. The documented repro: `3 + _sigma_net_boost(-1e-16, 9)`
# evaluates to just under 3 and returned "Partial" -> 0 damage at the universal `dr=1`, where the
# intended answer is "Success" -> 3. A 1-ulp error erasing an entire exchange.
#
# ALL THREE COMPARISONS ARE GUARDED, not just `Success`. Guarding one would institutionalise an
# asymmetric, attacker-favouring correction: `net <= 0` lets a mathematically-ZERO net escape
# `Failure` whenever its ulp error happens to be positive, while an equally-zero net with negative
# error is correctly failed. Fixing only the boundary that was noticed is how a rounding repair
# becomes a balance change.
#
# WHY ABSOLUTE, AND WHY 1e-9. Measured over the four shipped batteries, |net| is bounded by pool
# scale (single digits to low tens), so accumulated float error across the pool sum + softcap +
# sqrt chain is ~1e-13 at worst — four orders below this epsilon. In the other direction, the
# epsilon can only alter a verdict for a `net` within 1e-9 of a boundary; for such a net the
# INTENDED degree IS the boundary value, because no designed quantity in this engine resolves at
# 1e-9 (the smallest designed sigma decrement is a morale step, ~1e-1 through `_morale_sigma`).
# So the epsilon cannot promote a designed decrement: it can only recover a boundary the arithmetic
# lost. A relative epsilon would scale with `ob` and re-introduce the asymmetry at ob=0.
_DEGREE_EPS = 1e-9   # [JUSTIFIED: ulp-recovery tolerance, 4 orders above measured accumulated error and 8 below the smallest designed sigma decrement; not a mechanical magnitude]


def compute_degree(net, ob):
    """The ruled margin ladder (Jordan, 2026-08-14). Owner: engine.autoload.dice_engine.

    Spelled out here rather than imported ON PURPOSE: this tree is the self-contained canon
    engine (J2) and deliberately takes no `engine.*` dependency — that coupling is a porting
    -architecture call nobody has made. Equivalence is held by a guard instead of by an import:
    `tests/valoria/test_degree_ladder_single_owner.py` evaluates every ladder in the tree over
    the integer AND quarter-step domains and fails unless they collapse to ONE behavioural
    class, so a divergence here is loud rather than silent.

    The epsilon is unchanged in role — ulp recovery at a band boundary, justified above.
    """
    margin = net - ob
    if margin < -_DEGREE_EPS:      return "Failure"
    if margin < 1 - _DEGREE_EPS:   return "Partial"
    if margin >= 3 - _DEGREE_EPS:  return "Overwhelming"
    return "Success"

def _morale_sigma(u, atom=None):
    # Graded morale effectiveness as a delta-sigma: 0 at full morale, down to -MORALE_SIGMA_SCALE near rout.
    # [historical anchor: Ardant du Picq / Clausewitz — effectiveness degrades progressively before the rout]
    # atom (Jordan directive): per-subunit morale; None -> unit. Single-subunit eff_morale==u.morale -> byte-exact.
    if not MORALE_FIX: return 0.0
    morale = atom.eff_morale if atom is not None else u.morale
    morale_start = atom.eff_morale_start if atom is not None else getattr(u, 'morale_start', 0)
    if not morale_start: return 0.0
    frac = max(0.0, min(1.0, morale / morale_start))
    return MORALE_SIGMA_SCALE * (frac - 1.0)
def _brace_setup_ok(atom, t):
    """[ED-1095, Jordan-ruled 2026-07-02] True iff `atom`'s brace has been held continuously since
    a tick strictly before `t` (>=1 full tick of setup). -1 means not currently braced (never true).
    A subunit deployed already braced is stamped 0 at construction (exempt from the delay -- it had
    time to set up before the battle began). PC_RECOIL_FRONTAL-style safety net: t=None -> caller
    didn't pass a tick -> treat as instantaneous (True) so old call sites stay byte-exact."""
    if t is None or not PC_BRACE_SETUP_DELAY:
        return True
    since = getattr(atom, '_brace_since_tick', 0)
    return since >= 0 and (t - since) >= 1

def _unit_braced(unit, t=None):
    """True if any subunit carries the 'brace' instruction (the FM brace tactic). Gates the brace
    benefit (charge-resistance) and the reciprocal charge-recoil; INERT for instruction-less units
    (the historical gauge + signature scenarios) -> byte-exact.
    t=None (default) preserves the old instantaneous check. t given + PC_BRACE_SETUP_DELAY on ->
    also requires >=1 full tick since the brace instruction was set (see _brace_setup_ok)."""
    return any('brace' in getattr(su, 'instructions', ()) and _brace_setup_ok(su, t)
               for su in getattr(unit, 'subunits', ()))

def _subunit_braced(atom, t=None):
    """Per-subunit brace (Jordan directive): THIS subunit carries 'brace'. For a single-subunit
    unit this equals _unit_braced(unit) -> byte-exact; for a mixed unit only the braced subunit resists.
    t=None (default) preserves the old instantaneous check. t given + PC_BRACE_SETUP_DELAY on ->
    also requires >=1 full tick since the brace instruction was set (see _brace_setup_ok)."""
    return 'brace' in getattr(atom, 'instructions', ()) and _brace_setup_ok(atom, t)

def _disc_prep(disc):
    """Discipline -> preparedness 0..1. SHARED by the charge-shock brace gate (independent retention)
    and the recoil (conjunctive) so the disc curve has one source. disc 2 -> 0, disc 5 -> 1 (saturates)."""
    return max(0.0, min(1.0, (disc - 2) / 3.0))                    # [class-B] shared disc prep curve

def _depth_prep(depth):
    """Engaged depth -> preparedness 0..1. SHARED (one source for the depth curve).
    depth 1 -> 0, depth >= PC_SHOCK_DEPTH_REF -> 1."""
    ref = PC_SHOCK_DEPTH_REF if PC_SHOCK_DEPTH_REF > 1.0 else 2.0   # [class-B] depth-ref guard
    return max(0.0, min(1.0, (depth - 1.0) / (ref - 1.0)))

def _wall_prep(unit, contact_cells, atom=None):
    """Conjunctive wall-preparedness for the reciprocal charge-recoil: high only when disciplined
    AND deep. atom (Jordan directive): per-subunit discipline; None -> unit (byte-exact single-subunit)."""
    disc = atom.eff_discipline if atom is not None else getattr(unit, 'discipline', 5)
    return _disc_prep(disc) * _depth_prep(_defender_depth(unit, contact_cells))

def _charge_shock_sigma(defender, def_cells, zone, atom=None, t=None):
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
    # atom (Jordan directive): per-subunit defender stats; None -> unit. Single-subunit: atom.stance==unit.stance,
    # eff_discipline/eff_morale inherit -> byte-exact. brace gate (multiplicative): hold-stance x discipline x depth.
    _stance = atom.stance if atom is not None else getattr(defender, 'stance', 'balanced')
    _braced = _subunit_braced(atom, t) if atom is not None else _unit_braced(defender, t)
    b_stance = PC_SHOCK_HOLD_BRACE if (_stance == 'hold' or _braced) else 1.0
    disc = atom.eff_discipline if atom is not None else getattr(defender, 'discipline', 5)
    b_disc = 1.0 - _disc_prep(disc) * (1.0 - PC_SHOCK_DISC_FULL)        # independent disc retention (shared prep curve)
    depth = _defender_depth(defender, def_cells)
    b_depth = 1.0 - _depth_prep(depth) * (1.0 - PC_SHOCK_DEPTH_FULL)    # independent depth retention (shared prep curve)
    g_brace = max(PC_SHOCK_BRACE_FLOOR, min(1.0, b_stance * b_disc * b_depth))
    # shaken amplifier: a wavering defender takes more
    ms = (atom.eff_morale_start if atom is not None else getattr(defender, 'morale_start', 0)) or 0
    _morale = atom.eff_morale if atom is not None else defender.morale
    frac = max(0.0, min(1.0, _morale / ms)) if ms else 1.0
    a_shaken = 1.0 + PC_SHOCK_SHAKEN_GAIN * (1.0 - frac)
    return -PC_CHARGE_SIGMA * g_face * g_brace * a_shaken

def _sigma_softcap(x, m=1.5):                 # [canonical: modifier_system_spec.md §3.1 saturating]
    return m * math.tanh(x / m)
# [ED-MB-0051 / plan-v2 A2] Snap a numerically-zero sigma to exactly zero at the CHOKEPOINT.
# This is the semantically correct statement — "no modifier applies" — made once, where every
# producer's value passes through, rather than patched into each producer in turn. It covers the
# three cited producers at a stroke and any future one for free. The threshold is three orders
# TIGHTER than `_DEGREE_EPS`: this snap is for values that are zero and merely rendered as dust by
# float arithmetic, not for absorbing a small real modifier. Deliberately distinct constants — one
# tolerance doing two jobs is how the next confound gets built.
_SIGMA_ZERO_SNAP = 1e-12   # [JUSTIFIED: "this value is arithmetically zero" threshold; sized well below any designed sigma and below _DEGREE_EPS so the two never interact]


def _sigma_net_boost(net_sigma, pool, tn=7):  # [canonical: params/core.md continuous engine; modifier_system_spec §2.1] mu-shift
    _SIG = {6: 0.806, 7: 0.800, 8: 0.781}     # [canonical: params/core.md EV table] sigma per die at TN
    if abs(net_sigma) < _SIGMA_ZERO_SNAP:
        return 0.0
    return _sigma_softcap(net_sigma) * _SIG.get(tn, 0.800) * math.sqrt(max(1, pool))  # [canonical: params/core.md EV table — sigma per die at TN, default TN 7 = 0.800]
