"""
primitives.py — the contest primitives, one module each, derived from the corpus.
Structure is corpus-grounded; every numeric value is a tunable [SEED] (history validates
structure, never numbers). Modules are independent; the resolver composes them.
"""
from dataclasses import dataclass, field
from engine import level

# ── Stasis: the terrain. Four grounds + the strongest-tenable-rung fallback ladder. ──
class Stasis:
    FACT, DEFINITION, QUALITY, JURISDICTION = "fact", "definition", "quality", "jurisdiction"
    LADDER = [FACT, DEFINITION, QUALITY, JURISDICTION]   # deny act → contest label → justify → challenge venue
    @staticmethod
    def relevant(move_ground, live_ground):
        return move_ground == live_ground               # arguing off the live ground = evasion risk
    @staticmethod
    def stronger_than(a, b):
        return Stasis.LADDER.index(a) > Stasis.LADDER.index(b)

# ── Appeal: the three modes of proof (per-move axis). ──
class Appeal:
    ETHOS, PATHOS, LOGOS = "ethos", "pathos", "logos"
    ALL = (ETHOS, PATHOS, LOGOS)

# ── Standing: the spendable standing/ethos resource. ──
class Standing:
    LO, HI, START = 0.0, 10.0, 5.0
    DSIGMA_COEFF = 0.13   # [SEED] standing → leverage in σ-space
    BUILD, STRIP = 0.8, 0.8  # [SEED] per success
    def __init__(self, start=START): self.v = start
    def build(self, deg): self.v = min(self.HI, self.v + self.BUILD * deg)
    def strip(self, deg): self.v = max(self.LO, self.v - self.STRIP * deg)
    def dsigma(self):     return (self.v - self.START) * self.DSIGMA_COEFF

# ── Reserve: the action-economy resource. Exhaustion forces a pass (→ silence condition). ──
class Reserve:
    MAX = 12       # [SEED] flat baseline; a real build would derive from an attribute
    COST = {"advance": 3, "hard": 5, "shift": 4, "support": 2, "pass": 0}  # [SEED]
    REGAIN = 4     # [SEED] on a forfeited "support/regroup" beat
    def __init__(self, mx=MAX): self.max = mx; self.cur = mx
    def can(self, kind): return self.cur >= self.COST[kind]
    def spend(self, kind): self.cur = max(0, self.cur - self.COST[kind])
    def regroup(self): self.cur = min(self.max, self.cur + self.REGAIN)

# ── SelfGating: which tactics are licit, by relative standing × audience composition. ──
class SelfGating:
    """Caraka triage: honest argument is owed against an equal before a learned/fair audience;
       harder devices are licensed only against a weaker opponent before an ignorant/hostile crowd.
       Using an unlicensed hard device is itself a defeat-trigger (see DefeatConditions.barred)."""
    @staticmethod
    def hard_device_licensed(my_standing, opp_standing, audience_learned, audience_hostile):
        weaker_opponent = opp_standing < my_standing - 1.0   # [SEED] margin
        return weaker_opponent and (not audience_learned or audience_hostile)

# ── Leverage: accumulates live δσ into the engine (standing + on-ground fit + reading edge). ──
class Leverage:
    ONGROUND = level("moderate")  # arguing on the live stasis ground is a real edge
    READING_COEFF = 0.167         # [SEED] (faculty − 4)·coeff
    def net(self, faculty, standing_dsigma, on_ground, reading_edge=0.0):
        d = (faculty - 4) * self.READING_COEFF + standing_dsigma + reading_edge
        if on_ground: d += self.ONGROUND
        return d

# ── Merits: the accumulation clock, used only where no defeat-condition clinches. ──
class Merits:
    VSCALE = 0.9   # [SEED] reception → merits movement
    def __init__(self, threshold): self.a = 0.0; self.b = 0.0; self.T = threshold
    def advance(self, side, deg): setattr(self, side, getattr(self, side) + self.VSCALE * deg)
    def leader(self):
        if self.a >= self.T and self.a > self.b: return "a"
        if self.b >= self.T and self.b > self.a: return "b"
        return None

# ── DefeatConditions: the enumerable loss catalogue (deterministic clinch). ──
class DefeatConditions:
    """Named faults that end the contest against the side that incurs one — adjudicated against a
       checklist, not a roll. Mirrors the nigrahasthāna clinch the diagnostic prefers over fragile rolls."""
    EVASION_STRIKES = 2  # [SEED] off-ground moves tolerated before evasion clinches
    YIELD_STRIKES   = 2  # [SEED] forced passes tolerated before silence clinches
    @staticmethod
    def check(state):
        """state: per-side dict with keys evasion, yields, contradicted, barred. Returns losing side or None."""
        for side in ("a", "b"):
            s = state[side]
            if s["barred"]:                              return side  # used an unlicensed hard device
            if s["contradicted"]:                        return side  # reversed a committed ground illegitimately
            if s["evasion"] >= DefeatConditions.EVASION_STRIKES: return side
            if s["yields"]  >= DefeatConditions.YIELD_STRIKES:   return side
        return None
