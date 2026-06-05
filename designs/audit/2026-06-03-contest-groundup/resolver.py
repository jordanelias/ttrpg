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
                        Resonance, Readiness, DefeatCatalogue, EvidenceItem, Dossier,
                        RhetoricalWeights)
from engine import roll_net, effective_ob, degree

VALID_KINDS = ("advance", "hard", "shift", "support", "pass", "evidence", "rebut")
REBUT_CAP = 3.0   # Fork 3 (PROTOTYPE): max advantage a single rebuttal can erase — bounds the one
                  # attrition channel so a rebuttal war cannot death-spiral (diagnostic Lesson 5).
MERIT_SCALE = 2.6   # [SEED]
JITTER = 0.08       # [SEED] irreducible variability in how persuasion lands
PUBLIC_LEAK = 0.5   # [SEED] public pressure → adjudicator susceptibility
INST_BIAS = 0.6     # [SEED] institutional thumb on the scale
PUB_BIAS = 0.3      # [SEED] public favour tilt
EVIDENCE_CAP = 3.0  # [SEED] ceiling on one evidence item's magnitude (audit R1/R4: bound the readiness-free channel)

class ContestState:
    """Live tally the win-condition reads. Only `adv` is authoritative here; standing/room/live
       live on the Contestant / Bout (single source of truth) — no mirror to keep in sync."""
    def __init__(self):
        self.adv = {A: 0.0, B: 0.0}

class WinCondition:
    def resolve(self, s, closing, adj=None): raise NotImplementedError
class ThresholdRace(WinCondition):
    def __init__(self, T): self.T = T
    def resolve(self, s, closing, adj=None):
        a, b = s.adv[A], s.adv[B]
        if a >= self.T and a > b: return A
        if b >= self.T and b > a: return B
        if closing: return A if a > b else B if b > a else "draw"
        return None
class TallyAtClose(WinCondition):
    def resolve(self, s, closing, adj=None):
        if not closing: return None
        a, b = s.adv[A], s.adv[B]
        return A if a > b else B if b > a else "draw"
class ProofBar(WinCondition):
    def __init__(self, bar, challenger=A): self.bar = bar; self.ch = challenger
    def resolve(self, s, closing, adj=None):
        df = other(self.ch); net = s.adv[self.ch] - s.adv[df]
        if net >= self.bar: return self.ch
        if closing: return df
        return None
class GraceThreshold(WinCondition):
    def __init__(self, bar, petitioner=A): self.bar = bar; self.pet = petitioner
    def resolve(self, s, closing, adj=None):
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
    def resolve(self, s, closing, adj=None):
        if not closing: return None
        t = self.track(s)
        if t >= 9: return "A_total"
        if t >= 7: return "A_decisive"
        if t > 3:  return "committee"
        if t > 1:  return "B_decisive"
        return "B_total"


class VoteAtClose(WinCondition):
    """Fork 1 (PROTOTYPE, opt-in via venue.win): un-fuse momentum from verdict. The running `adv` is the
       room's MOMENTUM (drama); the VERDICT is a separate terminal secret ballot. Each juror votes A iff
       (sharpness*gap + per-juror noise) > 0 — the vote tracks momentum on average, but a juror can cross
       AGAINST it, so a close room is near a coin-flip while a lopsided room is near-certain. Majority
       decides. Models the secret-ballot court that deliberately severs the room from the outcome
       (Athenian dikasteria; thorubos vs the counted vote — research 2026-06-04). `noise` = how independent
       the jury is (low: tracks the room; high: can upset it). Default venues do NOT use this; the fused
       ThresholdRace/TallyAtClose remain the baseline."""
    def __init__(self, jurors=7, sharpness=0.6, noise=0.8):
        self.jurors = jurors; self.k = sharpness; self.noise = noise
    def resolve(self, s, closing, adj=None):
        if not closing: return None
        gap = s.adv[A] - s.adv[B]
        members = getattr(adj, "members", None)
        n = len(members) if members else self.jurors
        votesA = sum(1 for _ in range(n) if self.k * gap + random.gauss(0, self.noise) > 0)
        if votesA * 2 > n: return A
        if votesA * 2 < n: return B
        return "draw"


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
    proof_past: float = 1.0       # temporal-register weights; tense_weight() normalizes to a tilt (equal -> neutral)
    proof_present: float = 1.0
    proof_future: float = 1.0
    split_standing: bool = False   # PROTOTYPE: split fused Standing into ascribed Rank + earned Credit (default off)
    allow_rebuttal: bool = False   # PROTOTYPE (Fork 3): permit the rebut move (attrition on opponent adv); default off
    rhetorical: RhetoricalWeights = field(default_factory=RhetoricalWeights)  # 3×3 combinatorial matrix
    def role(self): return {"ethos": self.proof_ethos, "pathos": self.proof_pathos, "logos": self.proof_logos}
    def tense_weight(self):
        w = {"past": self.proof_past, "present": self.proof_present, "future": self.proof_future}
        s = sum(w.values()) or 1.0
        return {k: 3.0 * v / s for k, v in w.items()}   # equal weights -> 1.0 each (zero regression)
    def joint_weight(self, appeal: str, tense: str) -> float:
        """Combinatorial venue weight for (appeal, tense): venue_role × R[appeal][tense] × tfit.
        Replaces the independent res × tfit product in _advance with a single value that
        captures the Aristotelian cross-term (e.g. logos is stronger in past/forensic;
        pathos stronger in future/deliberative). Row sums of R ≈ 3.0 → neutral temporal
        weights leave gain scale unchanged."""
        return self.role()[appeal] * self.rhetorical.weight(appeal, tense) * self.tense_weight()[tense]

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
    """Per-bout MUTABLE runtime for one contestant, instantiated from a Contestant spec.
       Accessors (cred_frac / rank_v / build_ethos) are pure pass-throughs when split=False, so the
       fused path is bit-identical to the un-split engine. split=True (opt-in per venue) routes
       readiness+leak through earned Credit and the hard-tactic gate through ascribed Rank."""
    def __init__(self, spec, split=False):
        self.faculty  = spec.faculty
        self.split    = split
        if split:
            self.rank   = Standing(spec.standing_start)   # ascribed station: gates the hard-tactic gradient; not built by ethos
            self.credit = Standing(Standing.START)        # earned credibility: built by ethos/support; drives readiness + leak
        else:
            self.standing = Standing(spec.standing_start) # fused (current engine)
        self.reserve  = Reserve(spec.reserve_max)
        self.fault    = FaultState()
        self.dossier  = Dossier(list(spec.evidence))
    def cred_frac(self):      return (self.credit if self.split else self.standing).frac()
    def rank_v(self):         return (self.rank   if self.split else self.standing).v
    def build_ethos(self, m): (self.credit if self.split else self.standing).build(m)

class Bout:
    def __init__(self, ca, cb, venue, adjudicator=None, record=False):
        self.c = {A: _Side(ca, venue.split_standing), B: _Side(cb, venue.split_standing)}
        self.v = venue
        self.adj = adjudicator or Adjudicator()
        self.pr = venue.pressure
        self.live = venue.start_ground
        self.room = Room()
        self.state = ContestState()
        self.log = [] if record else None   # opt-in beat trace for narrative.summarize; None => no recording

    def _view(self, side, i):
        c, opp = self.c[side], self.c[other(side)]
        return ContestView(
            live_ground=self.live, appeal_axis=Appeal.ALL,
            my_standing=c.rank_v(), opp_standing=opp.rank_v(),
            can_hard=c.reserve.can("hard"), reserve_frac=c.reserve.cur / (c.reserve.max or 1),
            i=i, n=self.v.budget,
            leading=self.state.adv[side] > self.state.adv[other(side)],
            audience_learned=self.adj.learned, audience_hostile=self.adj.hostile,
            evidence_available=len(c.dossier.available(self.live)))

    def _reception(self, side):
        c = self.c[side]
        lev = Leverage.net(c.faculty, on_ground=True)
        ob = max(1.0, effective_ob(self.v.base_ob, lev, Pool.size(c.faculty)))  # σ-leverage: float OB, no rounding
        return degree(roll_net(Pool.size(c.faculty)), ob)

    def _bias(self, side):
        if self.pr.toward != side: return 1.0
        return 1.0 + self.pr.institutional * INST_BIAS + self.pr.public * PUB_BIAS

    def _advance(self, side, magnitude, appeal, ground, readiness=True, build=True):
        """Shared scorer. Argument (magnitude=deg): readiness-gated and builds its resource. Evidence
           (magnitude=weight·corroboration): HARD proof — readiness-independent, builds nothing; its
           value is the hidden weight weighted by how much this adjudicator credits that proof."""
        appeal = appeal or Appeal.LOGOS
        if appeal not in Appeal.ALL:
            raise ValueError(f"unknown appeal {appeal!r}; valid: {Appeal.ALL}")
        c = self.c[side]
        tense = Stasis.tense(ground)
        leak = min(Resonance.LEAK_CAP, Resonance.leak(self.adj.discipline, c.cred_frac())
                   + self.pr.public * PUBLIC_LEAK)
        venue_w = self.v.joint_weight(appeal, tense)          # rhetorical × temporal × venue-role — combined
        res = (1 - leak) * venue_w + leak * self.adj.character().get(appeal, 0.0)
        rdy = Readiness.of(c.cred_frac(), self.room.frac(side)) if readiness else 1.0
        gain = MERIT_SCALE * magnitude * res * rdy * random.uniform(1 - JITTER, 1 + JITTER) * self._bias(side)
        self.state.adv[side] += gain
        if build and appeal == Appeal.ETHOS:
            c.build_ethos(magnitude)
        elif build and appeal == Appeal.PATHOS:
            self.room.build(side, magnitude)

    def _apply(self, side, mv):
        if mv.kind not in VALID_KINDS:
            raise ValueError(f"unknown Move.kind {mv.kind!r}; valid: {VALID_KINDS}")
        c = self.c[side]; opp = self.c[other(side)]
        if mv.kind == "pass" or not c.reserve.can(mv.kind):
            c.fault.yields += 1
            c.fault.reason = "declined to answer (ananubhasana)" if mv.kind == "pass" else "no reply left, reserve spent (apratibha)"
            c.reserve.regroup(); return
        c.reserve.spend(mv.kind)
        if mv.kind == "support":
            c.reserve.regroup(); c.build_ethos(1); return
        if mv.kind == "shift":
            g = mv.ground
            if g is None:               c.fault.contradicted = True; c.fault.reason = "abandoned the question (pratijna-hani)"; return
            if not Stasis.is_ground(g): raise ValueError(f"unknown stasis ground {g!r}")
            if Stasis.stronger_than(g, self.live): self.live = g
            else:                                  c.fault.contradicted = True; c.fault.reason = "incoherent reframe (apasiddhanta)"
            return
        if mv.kind == "evidence":
            idx = c.dossier.best(self.live)          # best unpresented RELEVANT item (hidden value)
            if idx is None:                          # nothing relevant to present — refund the spend, no gain
                c.reserve.cur = min(c.reserve.max, c.reserve.cur + Reserve.COST["evidence"]); return
            item, factor = c.dossier.present(idx)
            mag = min(item.weight * factor, EVIDENCE_CAP)   # audit R4: cap the one readiness-free channel
            self._advance(side, mag, item.appeal, item.ground, readiness=False, build=False)   # hard proof; value hidden
            return
        if mv.kind == "rebut":                               # Fork 3 (PROTOTYPE): contest the opponent's case
            if not self.v.allow_rebuttal:                    # off-limits here -> treated as arguing off the live issue
                c.fault.evasion += 1; c.fault.reason = "rebuttal not permitted in this venue (arthantara)"; return
            deg = self._reception(side)                      # reception-gated like an argument
            if deg >= 2:                                     # a landed rebuttal erases up to REBUT_CAP of opp adv, floored at 0
                tgt = other(side)
                self.state.adv[tgt] = max(0.0, self.state.adv[tgt] - min(REBUT_CAP, float(deg)))
            return
        # advance / hard (argument — stochastic reception)
        if not SelfGating.licit(mv.kind, c.rank_v(), opp.rank_v(), self.adj.learned, self.adj.hostile):
            c.fault.barred = True; c.fault.reason = "overreach not licensed by standing (chala/jati)"; return
        if mv.ground is None or not Stasis.is_ground(mv.ground):
            raise ValueError(f"advance/hard requires a valid ground, got {mv.ground!r}")
        if not Stasis.relevant(mv.ground, self.live):
            c.fault.evasion += 1; c.fault.reason = "argued off the live issue (arthantara)"; return
        deg = self._reception(side)
        if deg >= 1:                                         # partial (1) gives a small gain; 0=failure still nothing
            self._advance(side, deg, mv.appeal, mv.ground)

    def resolve(self, polA, polB):
        pol = {A: polA, B: polB}
        for i in range(self.v.budget):
            for side in (A, B):
                mv = pol[side](self._view(side, i))
                if self.log is not None:
                    before = self.state.adv[side]
                    f0 = (self.c[side].fault.evasion, self.c[side].fault.yields,
                          self.c[side].fault.contradicted, self.c[side].fault.barred)
                self._apply(side, mv)
                if self.log is not None:
                    f1 = (self.c[side].fault.evasion, self.c[side].fault.yields,
                          self.c[side].fault.contradicted, self.c[side].fault.barred)
                    self.log.append(dict(i=i, side=side, kind=mv.kind, appeal=mv.appeal, ground=mv.ground,
                                         gain=self.state.adv[side] - before, live=self.live,
                                         advA=self.state.adv[A], advB=self.state.adv[B],
                                         fault=(self.c[side].fault.reason if f1 != f0 else None)))
                hit = self.v.faults.check({A: self.c[A].fault, B: self.c[B].fault})
                if hit:
                    loser, reason = hit
                    detail = self.c[loser].fault.reason
                    return (other(loser), f"clinch:{reason}" + (f" - {detail}" if detail else ""))
            w = self.v.win.resolve(self.state, closing=False, adj=self.adj)
            if w:
                return (w, "win")
        w = self.v.win.resolve(self.state, closing=True, adj=self.adj)
        return (w, "draw" if w == "draw" else "win")

def run(ca, cb, venue, adjudicator, polA, polB):
    return Bout(ca, cb, venue, adjudicator).resolve(polA, polB)
