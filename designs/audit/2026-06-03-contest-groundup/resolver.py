"""
resolver.py — the WRAPPER + the top-down VENUE spec. No privileged "merits": primitives accumulate a
per-side advancement; the venue's win-condition decides what winning is, and the venue's defeat-
catalogue which faults are fatal. Adds (this pass):
  - a small persuasion JITTER (no two arguments land identically) — removes high-faculty exact-tie draws;
  - EVIDENCE: presenting a relevant item adds its HIDDEN value (deterministic, not a roll), with
    corroboration (diminishing returns); irrelevant evidence has nothing to present;
  - PRESSURE on the adjudicator: institutional pressure tilts advancement toward a side; public
    pressure raises the adjudicator's leak (more swayable) and tilts toward the publicly favoured side.
Resolution at the exchange boundary; clinch immediate.
"""
import random
from dataclasses import dataclass, field
from contract import A, B, other, Move, ContestView, FaultState, Adjudicator, Pressure
from primitives import (Stasis, Appeal, Standing, Reserve, Pool, SelfGating, Leverage, Room,
                        Resonance, Readiness, DefeatCatalogue, EvidenceItem, Dossier)
from engine import roll_net, effective_ob, degree

VALID_KINDS = ("advance", "hard", "shift", "support", "pass", "evidence")
MERIT_SCALE = 2.6   # [SEED]
JITTER = 0.08       # [SEED] irreducible variability in how persuasion lands
PUBLIC_LEAK = 0.5   # [SEED] public pressure → adjudicator susceptibility
INST_BIAS = 0.6     # [SEED] institutional thumb on the scale
PUB_BIAS = 0.3      # [SEED] public favour tilt

class ContestState:
    """Live tally the win-condition reads. Only `adv` is authoritative here; standing/room/live
       live on the Contestant / Bout (single source of truth) — no mirror to keep in sync."""
    def __init__(self):
        self.adv = {A: 0.0, B: 0.0}

class WinCondition:
    def resolve(self, s, closing): raise NotImplementedError
class ThresholdRace(WinCondition):
    def __init__(self, T): self.T = T
    def resolve(self, s, closing):
        a, b = s.adv[A], s.adv[B]
        if a >= self.T and a > b: return A
        if b >= self.T and b > a: return B
        if closing: return A if a > b else B if b > a else "draw"
        return None
class TallyAtClose(WinCondition):
    def resolve(self, s, closing):
        if not closing: return None
        a, b = s.adv[A], s.adv[B]
        return A if a > b else B if b > a else "draw"
class ProofBar(WinCondition):
    def __init__(self, bar, challenger=A): self.bar = bar; self.ch = challenger
    def resolve(self, s, closing):
        df = other(self.ch); net = s.adv[self.ch] - s.adv[df]
        if net >= self.bar: return self.ch
        if closing: return df
        return None
class GraceThreshold(WinCondition):
    def __init__(self, bar, petitioner=A): self.bar = bar; self.pet = petitioner
    def resolve(self, s, closing):
        if s.adv[self.pet] >= self.bar: return self.pet
        if closing: return other(self.pet)
        return None

class PersuasionTrack(WinCondition):
    """Canon's two-pole Persuasion Track (social_contest §10 BG vote, §7.2 succession): a 0-10 axis,
       neutral start 5, pushed up by Side A and down by Side B, READ AT CLOSE into bands. Supplies the
       committee/compromise outcome the binary win-conditions lack:
         >=9 A_total · >=7 A_decisive · 4-6 committee · <=3 B_decisive · <=1 B_total."""
    def __init__(self, scale=1.5, start=5.0): self.scale = scale; self.start = start
    def track(self, s): return max(0.0, min(10.0, self.start + self.scale * (s.adv[A] - s.adv[B])))
    def resolve(self, s, closing):
        if not closing: return None
        t = self.track(s)
        if t >= 9: return "A_total"
        if t >= 7: return "A_decisive"
        if t > 3:  return "committee"
        if t > 1:  return "B_decisive"
        return "B_total"

@dataclass
class Venue:
    proof_ethos: float = 0.30
    proof_pathos: float = 0.30
    proof_logos: float = 0.40
    start_ground: str = Stasis.QUALITY
    budget: int = 8
    base_ob: float = 2.0
    win: WinCondition = field(default_factory=lambda: ThresholdRace(5.0))
    faults: DefeatCatalogue = field(default_factory=DefeatCatalogue)
    pressure: Pressure = field(default_factory=Pressure)
    def role(self): return {"ethos": self.proof_ethos, "pathos": self.proof_pathos, "logos": self.proof_logos}

class Contestant:
    """Immutable SPEC: faculty, starting standing, reserve cap, evidence items. The Bout builds a fresh
       per-bout runtime (`_Side`) from this and never mutates the spec, so a Contestant is safely reusable
       across bouts. Accepts `dossier=` (its items become the spec) or `evidence=[items]`."""
    def __init__(self, faculty, standing_start=Standing.START, reserve_max=Reserve.MAX, dossier=None, evidence=None):
        self.faculty = faculty
        self.standing_start = standing_start
        self.reserve_max = reserve_max
        items = evidence if evidence is not None else (dossier.items if dossier is not None else [])
        self.evidence = tuple(items)

class _Side:
    """Per-bout MUTABLE runtime for one contestant, instantiated from a Contestant spec."""
    def __init__(self, spec):
        self.faculty  = spec.faculty
        self.standing = Standing(spec.standing_start)
        self.reserve  = Reserve(spec.reserve_max)
        self.fault    = FaultState()
        self.dossier  = Dossier(list(spec.evidence))

class Bout:
    def __init__(self, ca, cb, venue, adjudicator=None):
        self.c = {A: _Side(ca), B: _Side(cb)}
        self.v = venue
        self.adj = adjudicator or Adjudicator()
        self.pr = venue.pressure
        self.live = venue.start_ground
        self.room = Room()
        self.state = ContestState()

    def _view(self, side, i):
        c, opp = self.c[side], self.c[other(side)]
        return ContestView(
            live_ground=self.live, appeal_axis=Appeal.ALL,
            my_standing=c.standing.v, opp_standing=opp.standing.v,
            can_hard=c.reserve.can("hard"), reserve_frac=c.reserve.cur / (c.reserve.max or 1),
            i=i, n=self.v.budget,
            leading=self.state.adv[side] > self.state.adv[other(side)],
            audience_learned=self.adj.learned, audience_hostile=self.adj.hostile,
            evidence_available=len(c.dossier.available(self.live)))

    def _reception(self, side):
        c = self.c[side]
        lev = Leverage.net(c.faculty, on_ground=True)
        ob = max(1, round(effective_ob(self.v.base_ob, lev, Pool.size(c.faculty))))
        return degree(roll_net(Pool.size(c.faculty)), ob)

    def _bias(self, side):
        if self.pr.toward != side: return 1.0
        return 1.0 + self.pr.institutional * INST_BIAS + self.pr.public * PUB_BIAS

    def _advance(self, side, magnitude, appeal, readiness=True, build=True):
        """Shared scorer. Argument (magnitude=deg): readiness-gated and builds its resource. Evidence
           (magnitude=weight·corroboration): HARD proof — readiness-independent, builds nothing; its
           value is the hidden weight weighted by how much this adjudicator credits that proof."""
        appeal = appeal or Appeal.LOGOS
        if appeal not in Appeal.ALL:
            raise ValueError(f"unknown appeal {appeal!r}; valid: {Appeal.ALL}")
        c = self.c[side]
        leak = min(Resonance.LEAK_CAP, Resonance.leak(self.adj.discipline, c.standing.frac())
                   + self.pr.public * PUBLIC_LEAK)
        res = Resonance.effective(appeal, self.v.role(), self.adj.character(), leak)
        rdy = Readiness.of(c.standing.frac(), self.room.frac(side)) if readiness else 1.0
        gain = MERIT_SCALE * magnitude * res * rdy * random.uniform(1 - JITTER, 1 + JITTER) * self._bias(side)
        self.state.adv[side] += gain
        if build and appeal == Appeal.ETHOS:
            c.standing.build(magnitude)
        elif build and appeal == Appeal.PATHOS:
            self.room.build(side, magnitude)

    def _apply(self, side, mv):
        if mv.kind not in VALID_KINDS:
            raise ValueError(f"unknown Move.kind {mv.kind!r}; valid: {VALID_KINDS}")
        c = self.c[side]; opp = self.c[other(side)]
        if mv.kind == "pass" or not c.reserve.can(mv.kind):
            c.fault.yields += 1; c.reserve.regroup(); return
        c.reserve.spend(mv.kind)
        if mv.kind == "support":
            c.reserve.regroup(); c.standing.build(1); return
        if mv.kind == "shift":
            g = mv.ground
            if g is None:               c.fault.contradicted = True; return
            if not Stasis.is_ground(g): raise ValueError(f"unknown stasis ground {g!r}")
            if Stasis.stronger_than(g, self.live): self.live = g
            else:                                  c.fault.contradicted = True
            return
        if mv.kind == "evidence":
            idx = c.dossier.best(self.live)          # best unpresented RELEVANT item (hidden value)
            if idx is None:                          # nothing relevant to present — refund the spend, no gain
                c.reserve.cur = min(c.reserve.max, c.reserve.cur + Reserve.COST["evidence"]); return
            item, factor = c.dossier.present(idx)
            self._advance(side, item.weight * factor, item.appeal, readiness=False, build=False)   # hard proof; value hidden
            return
        # advance / hard (argument — stochastic reception)
        if not SelfGating.licit(mv.kind, c.standing.v, opp.standing.v, self.adj.learned, self.adj.hostile):
            c.fault.barred = True; return
        if mv.ground is None or not Stasis.is_ground(mv.ground):
            raise ValueError(f"advance/hard requires a valid ground, got {mv.ground!r}")
        if not Stasis.relevant(mv.ground, self.live):
            c.fault.evasion += 1; return
        deg = self._reception(side)
        if deg >= 2:
            self._advance(side, deg, mv.appeal)

    def resolve(self, polA, polB):
        pol = {A: polA, B: polB}
        for i in range(self.v.budget):
            for side in (A, B):
                self._apply(side, pol[side](self._view(side, i)))
                hit = self.v.faults.check({A: self.c[A].fault, B: self.c[B].fault})
                if hit:
                    loser, reason = hit
                    return (other(loser), f"clinch:{reason}")
            w = self.v.win.resolve(self.state, closing=False)
            if w:
                return (w, "win")
        w = self.v.win.resolve(self.state, closing=True)
        return (w, "draw" if w == "draw" else "win")

def run(ca, cb, venue, adjudicator, polA, polB):
    return Bout(ca, cb, venue, adjudicator).resolve(polA, polB)
