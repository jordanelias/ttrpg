"""
contract.py — shared types between the wrapper (resolver) and policies. Depends on nothing else in
the package (breaks the resolver<->policy cycle). Side identity is defined once here.
"""
from dataclasses import dataclass

A, B = "a", "b"
def other(side): return B if side == A else A

@dataclass
class Move:
    kind: str
    appeal: str = None
    ground: str = None

@dataclass
class FaultState:
    evasion: int = 0
    yields: int = 0
    contradicted: bool = False
    barred: bool = False
    reason: str = None   # specific (Nyaya-named) descriptor of the most recent fault — legibility only; check() ignores it

@dataclass(frozen=True)
class Adjudicator:
    """One judge. learned/hostile feed self-gating; discipline + character feed resonance.
       Specific characters are authored; defaults are a neutral [SEED]."""
    learned: bool = True
    hostile: bool = False
    discipline: float = 0.6
    char_ethos: float = 0.34
    char_pathos: float = 0.33
    char_logos: float = 0.33
    def character(self):
        return {"ethos": self.char_ethos, "pathos": self.char_pathos, "logos": self.char_logos}

@dataclass(frozen=True)
class Panel:
    """Adjudicator(s) — a jury / bench / council. Exposes the same interface as a single
       Adjudicator by aggregating its members, so the wrapper treats one-or-many uniformly."""
    members: tuple
    @property
    def learned(self):  return sum(m.learned for m in self.members) * 2 > len(self.members)
    @property
    def hostile(self):  return sum(m.hostile for m in self.members) * 2 > len(self.members)
    @property
    def discipline(self): return sum(m.discipline for m in self.members) / len(self.members)
    def character(self):
        ks = ("ethos", "pathos", "logos")
        n = len(self.members)
        return {k: sum(m.character()[k] for m in self.members) / n for k in ks}

@dataclass(frozen=True)
class ContestView:
    live_ground: str
    appeal_axis: tuple
    my_standing: float
    opp_standing: float
    can_hard: bool
    reserve_frac: float
    i: int
    n: int
    leading: bool
    audience_learned: bool
    audience_hostile: bool
    evidence_available: int = 0   # count of unpresented relevant items the player HOLDS (value hidden)


@dataclass(frozen=True)
class Pressure:
    """External force on the adjudicator, beyond role and character. `toward` names the favoured
       side; `institutional` is a thumb on the scale (Crown/Church/party leaning on the verdict);
       `public` is the crowd/mob pressure that makes the adjudicator more swayable (raises leak)
       and tilts toward the publicly favoured side. Default = none."""
    toward: str = None          # A | B | None
    institutional: float = 0.0  # [0,1]
    public: float = 0.0         # [0,1]
