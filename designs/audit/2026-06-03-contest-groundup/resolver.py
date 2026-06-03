"""
resolver.py — the WRAPPER. A thin orchestrator (Bout) that owns contest state and composes the
primitive modules; it adds no mechanics of its own beyond sequencing. Key corrections:
  - resolution at the EXCHANGE BOUNDARY (both sides move, then the merits race is judged) — removes
    the turn-order bias; a defeat-condition clinch still ends immediately (faults are self-inflicted).
  - the opponent is passed explicitly (no hidden _opp_standing attribute / magic default).
  - move dispatch is split from scoring; appeals are routed to their targets (logos→merits,
    ethos→standing, pathos→room); bad input is rejected at the boundary.
Outcomes: a deterministic clinch, or merits accumulation crossing the threshold.
"""
from dataclasses import dataclass
from contract import A, B, other, Move, ContestView, FaultState, Adjudicator
from primitives import (Stasis, Appeal, Standing, Reserve, Pool, SelfGating,
                        Leverage, Room, Merits, DefeatConditions)
from engine import roll_net, effective_ob, degree

VALID_KINDS = ("advance", "hard", "shift", "support", "pass")

@dataclass
class Config:
    start_ground: str = Stasis.QUALITY
    threshold: float = 4.0   # [SEED] merits to win
    budget: int = 6          # [SEED] exchanges
    base_ob: float = 2.0     # [SEED]

class Contestant:
    def __init__(self, faculty, standing_start=Standing.START, reserve_max=Reserve.MAX):
        self.faculty = faculty
        self.standing = Standing(standing_start)
        self.reserve = Reserve(reserve_max)
        self.committed = None
        self.fault = FaultState()

class Bout:
    """Owns (contestants, live ground, merits, room, adjudicator); sequences exchanges."""
    def __init__(self, ca, cb, cfg, adjudicator=None):
        self.c = {A: ca, B: cb}
        self.cfg = cfg
        self.adj = adjudicator or Adjudicator()
        self.live = cfg.start_ground
        self.merits = Merits(cfg.threshold)
        self.room = Room()
        ca.committed = cb.committed = self.live

    # ----- read-only view for the policy -----
    def _view(self, side, i):
        c, opp = self.c[side], self.c[other(side)]
        return ContestView(
            live_ground=self.live, committed=c.committed, appeal_axis=Appeal.ALL,
            my_standing=c.standing.v, opp_standing=opp.standing.v,
            can_hard=c.reserve.can("hard"), reserve_frac=c.reserve.cur / (c.reserve.max or 1),
            i=i, n=self.cfg.budget,
            leading=self.merits.m[side] > self.merits.m[other(side)],
            audience_learned=self.adj.learned, audience_hostile=self.adj.hostile)

    # ----- stochastic core: one reception roll for an on-ground move -----
    def _reception(self, side):
        c = self.c[side]
        lev = Leverage.net(c.faculty, c.standing.dsigma(), True, self.room.dsigma(side))
        ob = max(1, round(effective_ob(self.cfg.base_ob, lev, Pool.size(c.faculty))))
        return degree(roll_net(Pool.size(c.faculty)), ob)

    # ----- score a successful on-ground move by its appeal -----
    def _score(self, side, deg, appeal):
        appeal = appeal or Appeal.LOGOS
        if appeal == Appeal.ETHOS:    self.c[side].standing.build(deg)
        elif appeal == Appeal.PATHOS: self.room.build(side, deg)
        else:                         self.merits.advance(side, deg)   # logos (and default)

    # ----- dispatch one move (legality + effects); mutates only the acting side's state -----
    def _apply(self, side, mv):
        if mv.kind not in VALID_KINDS:
            raise ValueError(f"unknown Move.kind {mv.kind!r}; valid: {VALID_KINDS}")
        c = self.c[side]; opp = self.c[other(side)]
        if mv.kind == "pass" or not c.reserve.can(mv.kind):     # forced/elective silence
            c.fault.yields += 1; c.reserve.regroup(); return
        c.reserve.spend(mv.kind)
        if mv.kind == "support":
            c.reserve.regroup(); c.standing.build(1); return
        if mv.kind == "shift":
            g = mv.ground
            if g is None:                 c.fault.contradicted = True; return
            if not Stasis.is_ground(g):   raise ValueError(f"unknown stasis ground {g!r}")
            if Stasis.stronger_than(g, self.live):  c.committed = g; self.live = g
            else:                                   c.fault.contradicted = True
            return
        # advance / hard
        if not SelfGating.licit(mv.kind, c.standing.v, opp.standing.v, self.adj.learned, self.adj.hostile):
            c.fault.barred = True; return
        if mv.ground is None or not Stasis.is_ground(mv.ground):
            raise ValueError(f"advance/hard requires a valid ground, got {mv.ground!r}")
        if not Stasis.relevant(mv.ground, self.live):
            c.fault.evasion += 1; return
        deg = self._reception(side)
        if deg >= 2:
            self._score(side, deg, mv.appeal)

    # ----- run the bout; merits judged at the exchange boundary -----
    def resolve(self, polA, polB):
        pol = {A: polA, B: polB}
        for i in range(self.cfg.budget):
            for side in (A, B):
                self._apply(side, pol[side](self._view(side, i)))
                hit = DefeatConditions.check({A: self.c[A].fault, B: self.c[B].fault})
                if hit:
                    loser, reason = hit
                    return (other(loser), f"clinch:{reason}")
            win = self.merits.leader()                 # boundary judgment, both having moved
            if win:
                return (win, "merits")
        win = self.merits.leader()
        return (win, "merits") if win else ("draw", "budget")

def run(ca, cb, cfg, adjudicator, polA, polB):
    return Bout(ca, cb, cfg, adjudicator).resolve(polA, polB)
