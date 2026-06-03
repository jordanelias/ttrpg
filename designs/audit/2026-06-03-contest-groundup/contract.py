"""
contract.py — the shared data types exchanged between the wrapper (resolver) and policies.
Depends on nothing else in the package, which is what breaks the former resolver<->policy
import cycle. Side identity (A/B) is defined ONCE here and imported everywhere.
"""
from dataclasses import dataclass

A, B = "a", "b"
def other(side): return B if side == A else A

@dataclass
class Move:
    kind: str                 # 'advance' | 'hard' | 'shift' | 'support' | 'pass'
    appeal: str = None        # ethos | pathos | logos  (advance/hard only)
    ground: str = None        # a stasis ground          (advance/hard/shift only)

@dataclass
class FaultState:
    """The single definition of a contestant's defeat-condition tallies."""
    evasion: int = 0
    yields: int = 0
    contradicted: bool = False
    barred: bool = False

@dataclass(frozen=True)
class Adjudicator:
    """Who judges — its own entity, not folded into the contest config."""
    learned: bool = True
    hostile: bool = False

@dataclass(frozen=True)
class ContestView:
    """Read-only snapshot a policy sees. Policies depend on this, never on resolver internals."""
    live_ground: str
    committed: str
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
