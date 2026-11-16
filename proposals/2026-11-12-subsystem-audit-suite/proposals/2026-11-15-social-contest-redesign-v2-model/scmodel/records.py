"""The records, RD A.3 (`2026-11-14-social-contest-redesign.md:127-277`) + PLAN B24p.02 (`part22_b24p.md:108`) +
B24p.03 (`base_disposal`). Frozen, stdlib only. Field comments abridged; see RD A.3.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Mapping, NamedTuple, Optional


@dataclass(frozen=True)
class Speaker:
    id: str
    side: str                  # "for" | "against"
    focus: float
    reason: float
    attunement: float
    presence: float
    grace: float
    will: float
    ranks: tuple               # ((skill id, rank), ...)
    addends: int
    score: float               # his skill score: what an opponent's draw is opposed by (A-79)
    proofs: float
    accounts: tuple            # names of the other side's circumstance terms he holds a claim about (B.2)
    precedence: int
    effort: int                # exchanges he is prepared to spend: act effort + 1
    levels: tuple              # ((source, sigma for, sigma against), ...) host sources
    operands: tuple            # ((name, raw, step, eased_by), ...) host obstacle operands (B24p.05 four-tuples)
    moved_by: tuple            # ((ground, weight in [0, 1]), ...) true values
    strain: float              # strain carried in


@dataclass(frozen=True)
class Decider:
    id: str
    weight: int
    pool: float
    score: float
    grace: float
    attunement: float
    reason: float
    focus: float
    will: float
    lean: float
    modifier: Optional[str]
    moved_by: tuple


@dataclass(frozen=True)
class Room:
    audience: str
    attention: float
    distraction: float
    proof_weight: float
    reception: tuple           # ((speaker id, signed regard), ...)


@dataclass(frozen=True)
class Move:
    id: str
    draw: bool
    capability: Optional[str]
    resisted_by: Optional[str]
    ground: bool
    fit: bool
    holds: bool
    effect: str                # "track" | "strike" | "pull" | "yield" | "none"
    reason_weight: Optional[float]
    ploy: bool = False
    difficulty: float = 0.0


@dataclass(frozen=True)
class ProceedingType:
    id: str
    disposal: str              # bench | declared | mutual | hearers | exchange | none
    order: str                 # free | written_only | alternating | rank | scripted   (G01: RD:194 says "single")
    exchanges: tuple
    moves: tuple               # ((side, (Move, ...)), ...)
    standard: float
    difficulty: float
    stakes: float
    presumes: str
    reason_bias: float
    quorum: Optional[int]
    break_at: Optional[int]
    strikes: int
    struck_ends: bool
    base_disposal: str = ""    # B24p.03 item 2: NEW cell, read by audience_kind (host side); carried for the record


@dataclass(frozen=True)
class SideState:
    id: str
    strain: float
    marks: int
    resolve: float
    pull: float
    strikes: int
    esteem: float
    read: tuple


@dataclass(frozen=True)
class ProceedingState:
    n: int
    track: float
    issue: Optional[str]
    sides: tuple


@dataclass(frozen=True)
class ProceedingInput:
    type: ProceedingType
    topic: str
    issue: Optional[str]
    speakers: tuple
    deciders: tuple
    hearers: tuple
    room: Room
    grounds: tuple
    ground_reason: tuple
    dials: Mapping
    state: Optional[ProceedingState] = None

    def __post_init__(self):
        # B24p.02: "raises `ValueError` when it has one speaker and neither a decider nor a hearer"
        if len(self.speakers) == 1 and not self.deciders and not self.hearers:
            raise ValueError("a one-speaker proceeding needs someone addressed (RD A.4)")


@dataclass(frozen=True)
class ExchangeView:
    n: int
    mover: str
    legal: tuple
    own: SideState
    read: tuple
    track_sign: int
    issue: Optional[str]


class Choice(NamedTuple):
    move: str
    ground: Optional[str]


@dataclass(frozen=True)
class Exchange:
    n: int
    mover: str
    move: str
    ground: Optional[str]
    on_topic: bool
    margin: float              # net + boost - ob; 0.0 for a non-drawing move (G29)
    terms: tuple
    levels: tuple
    strain: float
    marked: bool


@dataclass(frozen=True)
class ProceedingOutcome:
    exchanges: tuple
    state: ProceedingState
    ended: str
    verdicts: tuple            # ((id, Margin), ...)
    # NOT in RD A.3: the per-ballot levels, kept so the B.9 falsifiers can read `levels["sense"]` etc. (B24p.18 item 2
    # asserts "on the ballot record"; A.3 gives the outcome no field for it: G30)
    ballot_levels: tuple = ()
