"""
primitives.py — the contest primitives, one module each, from the corpus. Structure is
corpus-grounded; numbers are tunable [SEED]s. Resources (Standing, Reserve) are stateful
instances; everything else is static, matching its siblings. Side identity comes from contract.
"""
from contract import A, B, FaultState
from engine import level

# ── Stasis: terrain — four grounds + strongest-tenable-rung fallback ladder. ──
class Stasis:
    FACT, DEFINITION, QUALITY, JURISDICTION = "fact", "definition", "quality", "jurisdiction"
    LADDER = [FACT, DEFINITION, QUALITY, JURISDICTION]
    @staticmethod
    def is_ground(g):                       return g in Stasis.LADDER
    @staticmethod
    def relevant(move_ground, live_ground): return move_ground == live_ground
    @staticmethod
    def stronger_than(a, b):                return Stasis.LADDER.index(a) > Stasis.LADDER.index(b)

# ── Appeal: the three modes of proof (the per-move axis; routed to a target in the wrapper). ──
class Appeal:
    ETHOS, PATHOS, LOGOS = "ethos", "pathos", "logos"
    ALL = (ETHOS, PATHOS, LOGOS)

# ── Standing: spendable ethos resource (stateful). ──
class Standing:
    LO, HI, START = 0.0, 10.0, 5.0
    DSIGMA_COEFF = 0.13   # [SEED] standing → σ-leverage
    BUILD, STRIP = 0.8, 0.8  # [SEED]
    def __init__(self, start=START): self.v = start
    def build(self, deg): self.v = min(self.HI, self.v + self.BUILD * deg)
    def strip(self, deg): self.v = max(self.LO, self.v - self.STRIP * deg)
    def dsigma(self):     return (self.v - self.START) * self.DSIGMA_COEFF

# ── Reserve: action-economy resource (stateful); exhaustion forces a pass → silence. ──
class Reserve:
    MAX = 12  # [SEED]
    COST = {"advance": 3, "hard": 5, "shift": 4, "support": 2, "pass": 0}  # [SEED]
    REGAIN = 4  # [SEED]
    def __init__(self, mx=MAX): self.max = mx; self.cur = mx
    def can(self, kind):   return self.cur >= self.COST[kind]
    def spend(self, kind): self.cur = max(0, self.cur - self.COST[kind])
    def regroup(self):     self.cur = min(self.max, self.cur + self.REGAIN)

# ── Pool: the dice-pool model (a primitive, no longer an orphan in the resolver). ──
class Pool:
    BASE = 3  # [SEED] pool = faculty·2 + base, floor 5 (healthy band where dice is appropriate)
    @staticmethod
    def size(faculty): return max(5, faculty * 2 + Pool.BASE)

# ── SelfGating: which tactics are licit (Caraka triage). 'hard' is the only gated tactic today. ──
class SelfGating:
    MARGIN = 1.0  # [SEED]
    @staticmethod
    def _hard_licensed(my, opp, learned, hostile):
        return (opp < my - SelfGating.MARGIN) and (not learned or hostile)
    @staticmethod
    def licit(kind, my, opp, learned, hostile):
        return SelfGating._hard_licensed(my, opp, learned, hostile) if kind == "hard" else True

# ── Leverage: live δσ into the engine (static; stateless like its siblings). ──
class Leverage:
    ONGROUND = level("moderate")
    READING_COEFF = 0.167  # [SEED]
    @staticmethod
    def net(faculty, standing_dsigma, on_ground, room_dsigma=0.0):
        d = (faculty - 4) * Leverage.READING_COEFF + standing_dsigma + room_dsigma
        return d + Leverage.ONGROUND if on_ground else d

# ── Room: per-side momentum built by successful PATHOS — pathos's mechanical target. ──
class Room:
    CAP = 3.0    # [SEED]
    COEFF = 0.12 # [SEED] room → δσ
    def __init__(self):        self.r = {A: 0.0, B: 0.0}
    def build(self, side, deg): self.r[side] = min(self.CAP, self.r[side] + 0.5 * deg)
    def dsigma(self, side):     return self.r[side] * self.COEFF

# ── Merits: the verdict accumulation clock (LOGOS's target). ──
class Merits:
    VSCALE = 0.9  # [SEED]
    def __init__(self, threshold): self.m = {A: 0.0, B: 0.0}; self.T = threshold
    def advance(self, side, deg):  self.m[side] += self.VSCALE * deg
    def leader(self):
        if self.m[A] >= self.T and self.m[A] > self.m[B]: return A
        if self.m[B] >= self.T and self.m[B] > self.m[A]: return B
        return None

# ── DefeatConditions: the enumerable loss catalogue; returns (side, reason) in ONE pass. ──
class DefeatConditions:
    EVASION_STRIKES = 2  # [SEED]
    YIELD_STRIKES   = 2  # [SEED]
    @staticmethod
    def check(faults):
        """faults: {A: FaultState, B: FaultState} → (losing_side, reason) | None."""
        for side in (A, B):
            f = faults[side]
            if f.barred:                                      return (side, "barred-device")
            if f.contradicted:                                return (side, "self-contradiction")
            if f.evasion >= DefeatConditions.EVASION_STRIKES: return (side, "evasion")
            if f.yields  >= DefeatConditions.YIELD_STRIKES:   return (side, "silence")
        return None
