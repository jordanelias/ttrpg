"""modules.mass_battle.resolution — sigma-leverage head: pool roll (the one sampler's draw), morale/charge-shock
sigma, the sigma dust snap. The degree ladder, the soft cap and the net boost are the dice engine's, called from
the orchestration. Depends on config + percell."""
import contextlib, contextvars
from engine.dice_engine.sigma_leverage import net_boost, roll_net_continuous  # the one sampler (A-5); the module's first `engine` import
from modules.mass_battle import rngsource  # single owner of engine randomness (see rngsource.py)
from modules.mass_battle.config import *
from modules.mass_battle.percell import *

__all__ = ['roll_pool', '_morale_sigma', '_charge_shock_sigma', '_snap_sigma', '_net_boost', '_unit_braced', '_subunit_braced', '_wall_prep', '_disc_prep', '_depth_prep', 'trace_event', 'tracing', 'tracing_on']

# ─── passive mechanical-trace collector ─────────────────────────────────────
# Observe-only. Records per-mechanic internals (melee contest, volley, per-tick markers) inside a
# `tracing()` block. Outside one, trace_event is a no-op -> ENGINE BYTE-EXACT. The trace never feeds
# back into any mechanic, so ON and OFF produce identical outcomes. PER-CALL STATE (plan position `31c`,
# AX-4): the buffer is the list a `tracing()` block opens and yields, held in a context variable for
# the block's extent only.
_SCOPED_TRACE = contextvars.ContextVar('mass_battle_trace', default=None)
@contextlib.contextmanager
def tracing():
    """Record mechanical events for the extent of the block; yields the list they land in."""
    token = _SCOPED_TRACE.set([])
    try:
        yield _SCOPED_TRACE.get()
    finally:
        _SCOPED_TRACE.reset(token)
def trace_event(cat, **kw):
    """Append one mechanical event. No-op outside a `tracing()` block (byte-exact when off)."""
    events = _SCOPED_TRACE.get()
    if events is not None:
        kw['cat'] = cat
        events.append(kw)
def tracing_on():
    """True iff a `tracing()` block is open. Lets a caller (e.g. an expensive per-tick snapshot
    builder in orchestration.py) skip its work entirely when tracing is off. Query-only; no engine effect."""
    return _SCOPED_TRACE.get() is not None

# [canonical: Jordan ruling 2026-08-25 "TN7 always. Never change TN anywhere ever." — ED-IN-0196]
def roll_pool(n, tn=7):
    """One pool roll: the ONE sampler's draw (`sigma_leverage.roll_net_continuous`, A-5; the bell curve every
    provider draws from), on the generator `rngsource` scopes to the battle. The pool is taken as it is above the
    module's one-die minimum (PP-273) -- a fractional pool rolls as the fraction it is, with no second rule below
    one die: that is the owner's. `tn` is retained for call-signature compatibility and ASSERTED, not honoured."""
    # [canonical: Jordan ruling 2026-08-25 "TN7 always. Never change TN anywhere ever." — ED-IN-0196]
    assert tn == 7, f"TN is 7. Always. (Jordan, 2026-08-25) — got {tn}; a varying difficulty is an Ob."
    return roll_net_continuous(max(1, n), rng=rngsource.get())

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
    time to set up before the battle began). MB_RECOIL_FRONTAL-style safety net: t=None -> caller
    didn't pass a tick -> treat as instantaneous (True) so old call sites stay byte-exact."""
    if t is None or not MB_BRACE_SETUP_DELAY:
        return True
    since = getattr(atom, '_brace_since_tick', 0)
    return since >= 0 and (t - since) >= 1

def _unit_braced(unit, t=None):
    """True if any subunit carries the 'brace' instruction (the FM brace tactic). Gates the brace
    benefit (charge-resistance) and the reciprocal charge-recoil; INERT for instruction-less units
    (the historical gauge + signature scenarios) -> byte-exact.
    t=None (default) preserves the old instantaneous check. t given + MB_BRACE_SETUP_DELAY on ->
    also requires >=1 full tick since the brace instruction was set (see _brace_setup_ok)."""
    return any('brace' in getattr(su, 'instructions', ()) and _brace_setup_ok(su, t)
               for su in getattr(unit, 'units', ()))

def _subunit_braced(atom, t=None):
    """Per-subunit brace (Jordan directive): THIS subunit carries 'brace'. For a single-subunit
    unit this equals _unit_braced(unit) -> byte-exact; for a mixed unit only the braced subunit resists.
    t=None (default) preserves the old instantaneous check. t given + MB_BRACE_SETUP_DELAY on ->
    also requires >=1 full tick since the brace instruction was set (see _brace_setup_ok)."""
    return 'brace' in getattr(atom, 'instructions', ()) and _brace_setup_ok(atom, t)

def _disc_prep(disc):
    """Discipline -> preparedness 0..1. SHARED by the charge-shock brace gate (independent retention)
    and the recoil (conjunctive) so the disc curve has one source. disc 2 -> 0, disc 5 -> 1 (saturates)."""
    return max(0.0, min(1.0, (disc - 2) / 3.0))                    # [class-B] shared disc prep curve

def _depth_prep(depth):
    """Engaged depth -> preparedness 0..1. SHARED (one source for the depth curve).
    depth 1 -> 0, depth >= MB_SHOCK_DEPTH_REF -> 1."""
    ref = MB_SHOCK_DEPTH_REF if MB_SHOCK_DEPTH_REF > 1.0 else 2.0   # [class-B] depth-ref guard
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
    fights worse that exchange. Composes with _morale_sigma (one morale channel; role-conflation, diagnostic Phase 3d).
    [historical anchor: du Picq Battle Studies; Waterloo/Albuera; precedents_warfare §1.1.
     bottom-up: stance/discipline/_defender_depth/octagon zone/morale_start — all engine state.]
    """
    if not PER_CELL:
        return 0.0
    # facing gate: can the defender face the charge?
    if zone == "GREEN":   g_face = MB_SHOCK_FRONT      # faced charge mostly absorbed
    elif zone == "RED":   g_face = MB_SHOCK_REAR       # rear bypass (cannot face it)
    else:                 g_face = 1.0                 # YELLOW flank
    # atom (Jordan directive): per-subunit defender stats; None -> unit. Single-subunit: atom.stance==unit.stance,
    # eff_discipline/eff_morale inherit -> byte-exact. brace gate (multiplicative): hold-stance x discipline x depth.
    _stance = atom.eff_stance if atom is not None else getattr(defender, 'stance', 'balanced')  # [MB-04] role keyword via eff_stance
    _braced = _subunit_braced(atom, t) if atom is not None else _unit_braced(defender, t)
    b_stance = MB_SHOCK_HOLD_BRACE if (_stance == 'hold' or _braced) else 1.0
    disc = atom.eff_discipline if atom is not None else getattr(defender, 'discipline', 5)
    b_disc = 1.0 - _disc_prep(disc) * (1.0 - MB_SHOCK_DISC_FULL)        # independent disc retention (shared prep curve)
    depth = _defender_depth(defender, def_cells)
    b_depth = 1.0 - _depth_prep(depth) * (1.0 - MB_SHOCK_DEPTH_FULL)    # independent depth retention (shared prep curve)
    g_brace = max(MB_SHOCK_BRACE_FLOOR, min(1.0, b_stance * b_disc * b_depth))
    # shaken amplifier: a wavering defender takes more
    ms = (atom.eff_morale_start if atom is not None else getattr(defender, 'morale_start', 0)) or 0
    _morale = atom.eff_morale if atom is not None else defender.morale
    frac = max(0.0, min(1.0, _morale / ms)) if ms else 1.0
    a_shaken = 1.0 + MB_SHOCK_SHAKEN_GAIN * (1.0 - frac)
    return -MB_CHARGE_SIGMA * g_face * g_brace * a_shaken

# [ED-MB-0051 / plan-v2 A2] Snap a numerically-zero sigma to exactly zero at the CHOKEPOINT.
# This is the semantically correct statement — "no modifier applies" — made once, where every
# producer's value passes through, rather than patched into each producer in turn. It covers the
# three cited producers at a stroke and any future one for free. The degree boundaries' own ulp recovery
# is the owner's (the margin is quantised once at the ladder, `dice_engine.MARGIN_SCALE`); this snap is for
# values that are zero and merely rendered as dust by float arithmetic, not for absorbing a small real modifier.
_SIGMA_ZERO_SNAP = 1e-12   # [JUSTIFIED: "this value is arithmetically zero" threshold; sized well below any designed sigma (the smallest, a morale step, is ~1e-1) and far below the ladder's half milli-unit]


def _snap_sigma(net_sigma):
    """`net_sigma`, or exactly 0.0 where it is arithmetic dust (`_SIGMA_ZERO_SNAP`): the field's producers' value as it
    reaches `sigma_leverage.net_boost`."""
    return 0.0 if abs(net_sigma) < _SIGMA_ZERO_SNAP else net_sigma


def _net_boost(net_sigma, pool):
    """THE CHOKEPOINT the snap above is made at (B05 close): `sigma_leverage.net_boost` of `_snap_sigma(net_sigma)`, so a caller cannot reach the
    boost without the snap. A sigma that snaps to zero is no boost at all and skips the `tanh` and `sqrt` (what the deleted `_sigma_net_boost`
    short-circuited): `net_boost(0.0, pool)` is `0.0` for any finite pool."""
    snapped = _snap_sigma(net_sigma)
    return 0.0 if snapped == 0.0 else net_boost(snapped, pool)
