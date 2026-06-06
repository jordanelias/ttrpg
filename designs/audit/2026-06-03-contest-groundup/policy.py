"""policy.py — decoupled policies (read-only ContestView → Move via contract; no resolver internals)."""
from contract import Move, ContestView
from primitives import Stasis, Appeal

def _low(v): return v.reserve_frac < 0.3
def logos_spammer(v):
    if _low(v): return Move("support")
    return Move("advance", Appeal.LOGOS, v.live_ground)
def demagogue(v):
    if _low(v): return Move("support")
    return Move("advance", Appeal.PATHOS, v.live_ground)
def courtier(v):
    if _low(v): return Move("support")
    return Move("advance", Appeal.ETHOS, v.live_ground)
def build_then_close(v):
    if _low(v): return Move("support")
    if v.i < v.n // 2:
        return Move("advance", Appeal.ETHOS if v.i % 2 == 0 else Appeal.PATHOS, v.live_ground)
    return Move("advance", Appeal.LOGOS, v.live_ground)
def exploiter(v):
    if _low(v): return Move("support")
    if v.i < v.n // 2:
        return Move("advance", Appeal.ETHOS, v.live_ground)
    return Move("advance", Appeal.PATHOS, v.live_ground)
def fallback_ladder(v):
    if _low(v): return Move("support")
    if not v.leading:
        idx = Stasis.LADDER.index(v.live_ground)
        if idx + 1 < len(Stasis.LADDER):
            return Move("shift", Appeal.LOGOS, Stasis.LADDER[idx + 1])
    return Move("advance", Appeal.LOGOS, v.live_ground)
def off_ground_chancer(v):
    if v.i % 2 == 1:
        g = next(x for x in Stasis.LADDER if x != v.live_ground)
        return Move("advance", Appeal.LOGOS, g)
    return Move("advance", Appeal.LOGOS, v.live_ground)
def advocate(v):
    """Lead with evidence while you hold relevant items (value hidden), then argue logos."""
    if v.evidence_available > 0:
        return Move("evidence")
    if _low(v): return Move("support")
    return Move("advance", Appeal.LOGOS, v.live_ground)
def overreacher(v): return Move("hard", Appeal.PATHOS, v.live_ground)
def staller(v):     return Move("pass")
def counterpuncher(v):
    """Reactive rebuttal posture grounded in the classical partes orationis: confirmatio before
       refutatio (Quintilian — prove your own case, THEN rebut the opponent). Builds a position in the
       first half; in the back half, if not ahead, attacks the opponent's standing advantage instead of
       adding to its own. Banks reserve when low. Lands rebuttals only where venue.allow_rebuttal is set;
       elsewhere a back-half rebut scores as an off-issue evasion (so it self-limits there)."""
    if _low(v): return Move("support")
    if v.i >= v.n // 2 and not v.leading:
        return Move("rebut", ground=v.live_ground)
    return Move("advance", Appeal.LOGOS, v.live_ground)

POLICIES = {"logos": logos_spammer, "demagogue": demagogue, "courtier": courtier,
            "build_then_close": build_then_close, "exploiter": exploiter,
            "fallback": fallback_ladder, "off_ground": off_ground_chancer,
            "advocate": advocate, "overreacher": overreacher, "staller": staller,
            "counterpuncher": counterpuncher}
