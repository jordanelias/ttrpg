"""
primitives.py — the general, emergent substrate. Same across venues; the venue (top-down) shapes
how they resolve. Numbers are [SEED]s. N-collapse applied: standing/room feed ONLY readiness (and
standing feeds leak); the inert standing/room → reception-leverage coupling is removed (the audit
toggle showed readiness carries the build payoff). DefeatCatalogue is venue-configured.
"""
from dataclasses import dataclass
from contract import A, B
from engine import level

class Stasis:
    FACT, DEFINITION, QUALITY, JURISDICTION = "fact", "definition", "quality", "jurisdiction"
    LADDER = [FACT, DEFINITION, QUALITY, JURISDICTION]
    @staticmethod
    def is_ground(g):                       return g in Stasis.LADDER
    @staticmethod
    def relevant(move_ground, live_ground): return move_ground == live_ground
    @staticmethod
    def stronger_than(a, b):                return Stasis.LADDER.index(a) > Stasis.LADDER.index(b)

class Appeal:
    ETHOS, PATHOS, LOGOS = "ethos", "pathos", "logos"
    ALL = (ETHOS, PATHOS, LOGOS)

class Standing:
    LO, HI, START = 0.0, 10.0, 5.0
    BUILD, STRIP = 0.8, 0.8  # [SEED]
    def __init__(self, start=START): self.v = start
    def build(self, deg): self.v = min(self.HI, self.v + self.BUILD * deg)
    def strip(self, deg): self.v = max(self.LO, self.v - self.STRIP * deg)
    def frac(self):       return min(1.0, max(0.0, (self.v - self.START) / (self.HI - self.START)))

class Reserve:
    MAX = 12  # [SEED]
    COST = {"advance": 3, "hard": 5, "shift": 4, "support": 2, "pass": 0, "evidence": 3}
    REGAIN = 4
    def __init__(self, mx=MAX): self.max = mx; self.cur = mx
    def can(self, kind):   return self.cur >= self.COST[kind]
    def spend(self, kind): self.cur = max(0, self.cur - self.COST[kind])
    def regroup(self):     self.cur = min(self.max, self.cur + self.REGAIN)

class Pool:
    BASE = 3  # [SEED]
    @staticmethod
    def size(faculty): return max(5, faculty * 2 + Pool.BASE)

class SelfGating:
    MARGIN = 1.0  # [SEED]
    @staticmethod
    def _hard_licensed(my, opp, learned, hostile):
        return (opp < my - SelfGating.MARGIN) and (not learned or hostile)
    @staticmethod
    def licit(kind, my, opp, learned, hostile):
        return SelfGating._hard_licensed(my, opp, learned, hostile) if kind == "hard" else True

class Leverage:
    """δσ into the reception roll. N-collapsed: faculty (skill) + on-ground (terrain) only.
       Standing/room no longer feed the roll — they feed readiness (their one role)."""
    ONGROUND = level("moderate")
    READING_COEFF = 0.167  # [SEED]
    @staticmethod
    def net(faculty, on_ground):
        d = (faculty - 4) * Leverage.READING_COEFF
        return d + Leverage.ONGROUND if on_ground else d

class Room:
    CAP = 3.0  # [SEED] pathos's target; feeds readiness
    def __init__(self):         self.r = {A: 0.0, B: 0.0}
    def build(self, side, deg): self.r[side] = min(self.CAP, self.r[side] + 0.5 * deg)
    def frac(self, side):       return self.r[side] / self.CAP

class Resonance:
    """How much a proof moves THIS adjudicator HERE = blend(role, character) by leak.
       leak rises as discipline is low and as built ethos draws the judge toward character."""
    ETHOS_UNLOCK = 0.5  # [SEED]
    LEAK_CAP = 0.9      # [SEED]
    @staticmethod
    def leak(discipline, standing_frac):
        return min(Resonance.LEAK_CAP, max(0.0, (1.0 - discipline) + Resonance.ETHOS_UNLOCK * standing_frac))
    @staticmethod
    def effective(appeal, role_w, char_w, leak):
        return (1 - leak) * role_w.get(appeal, 0.0) + leak * char_w.get(appeal, 0.0)
    @staticmethod
    def tension(role_w, char_w):
        return sum(abs(role_w.get(a, 0.0) - char_w.get(a, 0.0)) for a in Appeal.ALL)

class Readiness:
    """Built support that makes appeals land; floor < 1 so unsupported still moves something."""
    FLOOR = 0.35  # [SEED]
    W_STANDING, W_ROOM = 0.5, 0.5
    @staticmethod
    def of(standing_frac, room_frac):
        r = Readiness.W_STANDING * standing_frac + Readiness.W_ROOM * room_frac
        return Readiness.FLOOR + (1 - Readiness.FLOOR) * min(1.0, max(0.0, r))

class DefeatCatalogue:
    """Venue-configured fault→clinch rules. WHICH faults are fatal, and at what count, is a
       top-down property of the institution: a disputation clinches on the nigrahasthāna (all four);
       a vote disables the rhetorical-device bar; a ceremony has no defeat-conditions at all.
       The general fault *detection* lives in the wrapper; this decides which are *fatal*."""
    def __init__(self, barred=True, contradiction=True, evasion_strikes=2, yield_strikes=2):
        self.barred = barred
        self.contradiction = contradiction
        self.evasion_strikes = evasion_strikes   # 0/None disables
        self.yield_strikes = yield_strikes
    def check(self, faults):
        for side in (A, B):
            f = faults[side]
            if self.barred and f.barred:                                       return (side, "barred-device")
            if self.contradiction and f.contradicted:                          return (side, "self-contradiction")
            if self.evasion_strikes and f.evasion >= self.evasion_strikes:      return (side, "evasion")
            if self.yield_strikes and f.yields >= self.yield_strikes:           return (side, "silence")
        return None


@dataclass
class EvidenceItem:
    """A piece of evidence/testimony. `weight` is the engine's HIDDEN true value (relevance×quality);
       the player never sees it. `appeal` is the proof it bolsters (documentary→logos, a credible
       witness→ethos, a victim's testimony→pathos)."""
    ground: str
    weight: float
    appeal: str = Appeal.LOGOS

class Dossier:
    """A side's evidence. Presenting a RELEVANT item (ground == live stasis) adds its hidden value;
       presenting more relevant evidence is good but with diminishing returns (corroboration
       saturates). Irrelevant evidence has nothing to present. Weights are hidden from the player."""
    CORROB = (1.0, 0.7, 0.5, 0.35)  # [SEED] diminishing returns; beyond → 0.25
    def __init__(self, items=None):
        self.items = list(items or [])
        self.presented = set()
        self.count_on = {}
    def available(self, ground):
        return [i for i, it in enumerate(self.items) if it.ground == ground and i not in self.presented]
    def best(self, ground):
        av = self.available(ground)
        return max(av, key=lambda i: self.items[i].weight) if av else None
    def present(self, idx):
        self.presented.add(idx)
        g = self.items[idx].ground
        k = self.count_on.get(g, 0); self.count_on[g] = k + 1
        factor = Dossier.CORROB[k] if k < len(Dossier.CORROB) else 0.25
        return self.items[idx], factor
