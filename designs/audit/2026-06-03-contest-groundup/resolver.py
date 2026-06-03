"""
resolver.py — the composite resolver. Deterministic wrapper (turn order, stasis ground, merits
clock, defeat-condition checklist, standing/reserve ledgers) around a small stochastic core
(per-move reception via the engine). A contest ends two ways: a deterministic CLINCH when a side
incurs a defeat-condition, or MERITS accumulation crossing the threshold. This is the resolver the
diagnostic concluded and the corpus independently grounds.
"""
from dataclasses import dataclass, field
from engine import roll_net, effective_ob, degree
from primitives import Stasis, Appeal, Standing, Reserve, SelfGating, Leverage, Merits, DefeatConditions

POOL_BASE = 3  # [SEED] pool = faculty·2 + base, kept in the healthy band where dice is appropriate

def pool_of(faculty): return max(5, faculty * 2 + POOL_BASE)

@dataclass
class Move:
    kind: str            # 'advance' | 'hard' | 'shift' | 'support' | 'pass'
    appeal: str = Appeal.LOGOS
    ground: str = Stasis.QUALITY

class Contestant:
    def __init__(self, faculty, standing_start=Standing.START, reserve_max=Reserve.MAX):
        self.faculty = faculty
        self.standing = Standing(standing_start)
        self.reserve = Reserve(reserve_max)
        self.committed = None
        self.state = {"evasion": 0, "yields": 0, "contradicted": False, "barred": False}

@dataclass
class Config:
    start_ground: str = Stasis.QUALITY
    threshold: float = 4.0      # [SEED] merits to win
    budget: int = 6             # [SEED] exchanges
    base_ob: float = 2.0        # [SEED]
    audience_learned: bool = True
    audience_hostile: bool = False

def _reception(c, on_ground, base_ob):
    lev = Leverage().net(c.faculty, c.standing.dsigma(), on_ground)
    net = roll_net(pool_of(c.faculty))
    ob = max(1, round(effective_ob(base_ob, lev, pool_of(c.faculty))))
    return degree(net, ob)

def _process(side, c, cfg, live_ground, merits, mv):
    """Apply one move; mutate c.state / standing / merits; return possibly-new live_ground."""
    if c.committed is None:
        c.committed = live_ground
    if mv.kind == "pass" or not c.reserve.can(mv.kind):
        c.state["yields"] += 1; c.reserve.regroup(); return live_ground
    c.reserve.spend(mv.kind)
    if mv.kind == "support":
        c.reserve.regroup(); c.standing.build(1); return live_ground
    if mv.kind == "shift":
        # legitimate fallback only if the target ground is stronger (further down the ladder)
        if Stasis.stronger_than(mv.ground, live_ground):
            c.committed = mv.ground; return mv.ground
        c.state["contradicted"] = True; return live_ground   # illegitimate ground-switch = self-contradiction
    # 'advance' or 'hard'
    if mv.kind == "hard" and not SelfGating.hard_device_licensed(
            c.standing.v, getattr(c, "_opp_standing", 5.0), cfg.audience_learned, cfg.audience_hostile):
        c.state["barred"] = True; return live_ground          # unlicensed hard device = barred-device clinch
    on_ground = Stasis.relevant(mv.ground, live_ground)
    if not on_ground:
        c.state["evasion"] += 1; return live_ground            # off-ground = evasion strike, no merits
    deg = _reception(c, on_ground, cfg.base_ob)
    if deg >= 2:
        merits.advance(side, deg); c.standing.build(deg)
    return live_ground

def run(A, B, cfg, polA, polB):
    from policy import ContestView
    live = cfg.start_ground
    A.committed = B.committed = live
    merits = Merits(cfg.threshold)
    state = {"a": A.state, "b": B.state}
    for i in range(cfg.budget):
        for side, c, opp, pol in (("a", A, B, polA), ("b", B, A, polB)):
            c._opp_standing = opp.standing.v
            leading = getattr(merits, side) > getattr(merits, "b" if side == "a" else "a")
            view = ContestView(live_ground=live, committed=c.committed, appeal_axis=Appeal.ALL,
                               my_standing=c.standing.v, opp_standing=opp.standing.v,
                               can_hard=c.reserve.can("hard"), reserve_frac=c.reserve.cur / c.reserve.max,
                               i=i, n=cfg.budget, leading=leading,
                               audience_learned=cfg.audience_learned, audience_hostile=cfg.audience_hostile)
            mv = pol(view)
            live = _process(side, c, cfg, live, merits, mv)
            loser = DefeatConditions.check(state)
            if loser:                       return ("b" if loser == "a" else "a", f"clinch:{_why(state[loser])}")
            win = merits.leader()
            if win:                         return (win, "merits")
    win = merits.leader()
    return (win, "merits") if win else ("draw", "budget")

def _why(s):
    if s["barred"]: return "barred-device"
    if s["contradicted"]: return "self-contradiction"
    if s["evasion"] >= DefeatConditions.EVASION_STRIKES: return "evasion"
    if s["yields"] >= DefeatConditions.YIELD_STRIKES: return "silence"
    return "?"
