"""sc2.engine -- the v2 proceeding MODULE (2026-11-16, second fix pass: the premise-check's causes C1..C5 and items B, C, D).

World-free: reads only `inp`. Keeps no state. Returns margins and a record; grades nothing; writes nothing.
Compares no rite id, move id or person id: it reads cells. Draw discipline (stated once, here, and asserted in
`proceed`): every exchange takes exactly DRAWS_PER_EXCHANGE(G) = 6G + 11 normals [the view: his accuracy; per
ground one for what arguing on it is worth, one for pressing on it, two for the speech's frame, two for the press's
object; conceding, resting, the mood, their point, his own point, the other's intent, his esteem, his awe; the
exchange: the hold, the speech], each believed number its own; every drawn decider exactly one.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, replace
from typing import Callable, Mapping, Optional

import scmodel  # noqa: F401
from engine.dice_engine.sigma_leverage import M_MAX
from scmodel.dice import (MU_PER_DIE, SD_PER_DIE, Margin, SocialContestInput, even_line, level, net_boost, obstacle,
                          pool_of, roll_net_continuous, weighted_tenth)

SIGN = {"for": 1.0, "against": -1.0}
CHANNEL = {"consequence": 0, "authority": 1, "solidarity": 2}      # want, hold, bond; `evidence` reads the item


def DRAWS_PER_EXCHANGE(G: int) -> int:
    """the one statement of the exchange's draw count (asserted in `proceed`)."""
    return 6 * G + 11


@dataclass(frozen=True)
class Item:
    id: str
    kind: str
    weight: float
    source: Optional[str] = None
    about: Optional[str] = None
    sincere: bool = True           # False: its holder knows it false (his own false word, a forgery: host `false_items`)


@dataclass(frozen=True)
class Present:
    id: str
    weight: int = 1
    side: Optional[str] = None     # "for" | "against" | None
    decides: bool = False          # he adjudicates; independent of `side`: a noble may speak with you and then decide
    focus: float = 4.0
    reason: float = 4.0
    attunement: float = 4.0
    presence: float = 4.0
    grace: float = 4.0
    will: float = 4.0
    rank: float = 0.0
    care: tuple = (0.5, 0.5, 0.5)
    stake: tuple = (0.0, 0.0, 0.0)  # bearing of the matter on him, signed toward `for`
    bonds: tuple = ()
    start: float = 0.0             # where his track starts (host: bearing + arrangement)
    believes: float = 0.0          # what he KNOWS of the matter, -1..1 toward `for` (own ledger)
    holds: tuple = ()              # ((channel, tag, weight 0..1, how the matter bears on it -1..1), ...): what he
                                   # wants (pursuits, needs, goals) and holds (convictions, duties), tag by tag
    bias: float = 0.0              # his stable misjudgement, -1 pessimist .. +1 optimist (host: his character)
    power: float = 0.0             # his circumstances: seat, office, wealth, influence, faction (host)
    precedence: int = 0
    items: tuple = ()
    strain: float = 0.0


@dataclass(frozen=True)
class Rite:
    id: str
    live: str
    reply: tuple
    issues: tuple
    concede: str                   # descends | accepts
    moves: tuple
    close: str                     # bench | declared | hearers | consent | exchange
    turns: int
    standard: float
    reason_lean: float
    admits: tuple
    difficulty: float = 0.5
    gravity: float = 0.0           # how grave the times make a change: an obstacle on the bearer at the close (strife)
    quorum: Optional[int] = None
    silence: str = "refusal"       # what not answering a standing point means here: admits | refusal | free (A-145)
    unrest: float = 0.0
    bears: str = "for"
    weighs: tuple = ()             # stasis: ((issue, ((ground, weight), ...)), ...): what each rung is argued from


@dataclass(frozen=True)
class MoveRow:
    id: str
    effect: str
    draw: bool


MOVES = {m.id: m for m in (MoveRow("argue", "track", True), MoveRow("press", "strike", True),
                           MoveRow("concede", "yield", False), MoveRow("rest", "none", False))}


@dataclass(frozen=True)
class Cond:
    rattles: int = 0
    strain: float = 0.0
    heat: float = 0.0              # this sitting's provocation: a rattle adds one; it cools at each beat he makes
    spoken: int = 0
    spent: float = 0.0             # staying power used: one a speech, one a rattle (Will)


@dataclass(frozen=True)
class Point:
    id: int
    side: str
    issue: str
    ground: str
    item: Optional[str]
    by: str
    held: tuple


@dataclass(frozen=True)
class Sitting:
    n: int = 0
    issue: int = 0
    points: tuple = ()
    live: tuple = (("for", None), ("against", None))
    tracks: tuple = ()             # the running value of `start + the beats' moves` (asserted equal); kept for resume
    cond: tuple = ()
    used: tuple = ()
    last_voice: tuple = (("for", None), ("against", None))
    ended: Optional[str] = None


@dataclass(frozen=True)
class Option:
    move: str
    ground: Optional[str]
    item: Optional[str]
    relation: str
    ev: float
    p: Optional[float]
    frame: Optional[str] = None    # argue: what of the listeners' it is framed on; press: the held thing it hits


@dataclass(frozen=True)
class View:
    n: int
    mover: str
    side: str
    issue: str
    live_theirs: Optional[tuple]
    live_own: Optional[tuple]
    options: tuple
    own: Cond
    esteem: float                  # his standing in the room this sitting (derived)
    weary: float
    awe: float                     # how far those who decide intimidate him (his own; he feels it)
    broke: bool                    # his temper has broken: he cannot hold his tongue, and `rest` is not on his menu
    visible: tuple
    mood: float
    odds: float                    # believed P(carried) as he reads the room; an ordinary bench assumed
    intent: float                  # believed stake of the man opposite, -1..1 toward `for`
    turns_left: int
    acc: float
    burden: bool = False           # he bears the matter and no point of his stands: resting is a charge not pressed


class Choice(tuple):
    def __new__(cls, move, ground=None, item=None, relation=None):
        return tuple.__new__(cls, (move, ground, item, relation))
    move = property(lambda s: s[0]); ground = property(lambda s: s[1])
    item = property(lambda s: s[2]); relation = property(lambda s: s[3])


@dataclass(frozen=True)
class Beat:
    n: int
    mover: str
    voice: str
    side: str
    move: str
    relation: str
    issue: str
    ground: Optional[str]
    item: Optional[str]
    point: Optional[int]
    target: Optional[str]
    margin: float
    drift: float
    evaded: bool                   # priced: he left a point he must answer standing, or rested on a charge he bears
    left: Optional[int]            # the other side's point that stood against him and that he did not answer (any rite)
    insincere: float
    caught: tuple                  # those whose reading of him turned a speech he did not hold (A-144 Attunement)
    rattled: Optional[str]
    frame: Optional[str]           # argue: what it was framed on (Attunement); press: the held thing it hit
    relevance: float               # Reason: how to the point its content was
    heard: float                   # Presence: the share of him the room listened to
    esteem: float                  # Grace: his standing in the room as he spoke
    broke: bool                    # he spoke with his temper broken (he could hold his tongue no longer)
    moved: tuple
    closed: Optional[str]
    mood: float
    terms: tuple = ()


@dataclass(frozen=True)
class Input:
    rite: Rite
    matter: str
    room: tuple
    grounds: tuple                 # ((ground, reason weight, era weight), ...)
    dials: Mapping
    state: Optional[Sitting] = None
    frames: tuple = ()             # ((channel, tag), ...): the wants and convictions a speech here can be framed on

    def __post_init__(self):
        """One invariant (A-139): a sitting has at least two distinct characters. The rest are structural, each
        refused with a keyed reason: a cohort has weight; a drawn close has someone whose verdict is drawn; somebody
        speaks; an abridged act is addressed to someone other than the speaker."""
        if len({p.id for p in self.room}) < 2:
            raise ValueError("refused[one_character]: a sitting with one character (A-139)")
        if self.rite.close == "exchange" and not any(p.decides and not p.side for p in self.room):
            raise ValueError("refused[abridged_self]: an abridged act needs someone addressed other than the speaker")
        if any(p.weight <= 0 for p in self.room):
            raise ValueError("refused[no_weight]: a person or cohort of no weight")
        if self.rite.close != "consent" and not any(p.decides for p in self.room):
            raise ValueError(f"refused[no_adjudicator]: close `{self.rite.close}` with nobody to adjudicate")
        if not any(p.side for p in self.room):
            raise ValueError("refused[nobody_speaks]: nobody speaks")
        if self.state is not None and self.state.ended == "yielded":
            raise ValueError("refused[resume_yielded]: a sitting that ended `yielded` is not resumed (an adjourned one is)")
        if self.state is not None:                # a resume continues THIS sitting: the same people, with turns left
            if self.rite.close == "exchange":
                raise ValueError("refused[abridged_resume]: an abridged act is one speech; it is not resumed")
            if {p.id for p in self.room} != {i for i, _ in self.state.tracks}:
                raise ValueError("refused[room_changed]: a resumed sitting has the same people; a changed room is a new sitting")
            sp = _d(self.state.cond)
            if not any(p.side and _d(self.rite.moves).get(p.side) and sp[p.id].spoken < self.rite.turns for p in self.room):
                raise ValueError("refused[spent]: no speaker has a turn left; a close once drawn is not drawn again")


@dataclass(frozen=True)
class Outcome:
    beats: tuple
    state: Sitting
    ended: str
    ended_by: Optional[str]
    verdicts: tuple
    ruled: tuple = ()              # ((decider, how far his ruling departed from his own track), ...) for a played judge


# ------------------------------------------------------------------ readers
def _d(t):
    return dict(t)


def _put(t, k, v):
    d = dict(t); d[k] = v
    return tuple(d.items())


def _bond(p, other):
    return _d(p.bonds).get(other, 0.0) if other else 0.0


def _who(inp, pid):
    return next(p for p in inp.room if p.id == pid)


def _lead(inp, side):
    c = [p for p in inp.room if p.side == side]
    return max(c, key=lambda p: (p.precedence, p.id)) if c else None


def _other(side):
    return "against" if side == "for" else "for"


def _stands(P) -> float:
    """how far a point stands with those who HEARD it (the other side included, and a party who also decides)."""
    return SIGN[P.side] * sum(v for _, v in P.held)


def _point(st, pid):
    return next((p for p in st.points if p.id == pid), None) if pid is not None else None


def _reply(inp, side):
    return _d(inp.rite.reply).get(side, "may")


def silence_cost(inp, h, P, mover):
    """A-145: SILENCE IS NEVER FREE where the rite says a point must be answered (or a matter borne must be put).
    Each listener reads it as REFUSAL to engage: a disrespect growing with how formal the occasion is and with the
    station of one who decides; and, where the rite's `silence` cell is `admits`, as TACIT ADMISSION: the unanswered
    point counts with him again by a share of how far it stands. A man is not contemptuous of himself: a party who
    decides pays only the admission on his own track."""
    D, r = inp.dials, inp.rite
    if r.silence == "free":
        return 0.0
    c = 0.0 if h.id == mover.id else D["contempt_step"] * (r.standard / D["mid"]) * (1.0 + (h.power / 4.0 if h.decides else 0.0))
    if r.silence == "admits" and P is not None:
        c += D["admit_step"] * max(0.0, SIGN[P.side] * _d(P.held).get(h.id, 0.0))
    return c


def burden(inp, st, mover) -> bool:
    """THE BURDEN (one rule with A-145): the bearer of a matter that the other side MUST answer has to put it. While
    no point of his stands, his rest, or a press in place of a point, is a charge not pressed (a question not asked)
    and is priced as silence is. So an unargued charge lapses: a sitting where nobody speaks goes against the bearer."""
    r = inp.rite
    if mover.side != r.bears or _reply(inp, _other(mover.side)) != "must":
        return False
    Po = _point(st, _d(st.live).get(mover.side))
    return Po is None or _stands(Po) <= 0


def _hearers(inp, voice: Present, side):
    """whose track a speech moves from outside: everyone not on the speaking side."""
    return [p for p in inp.room if p.id != voice.id and p.side != side]


def _crowd(inp):
    w = sum(p.weight for p in inp.room if p.side is None)          # how many are listening, by head
    return min(1.0, w / inp.dials["crowd_at"])


def mood(inp, st, viewer: Optional[Present] = None):
    T = _d(st.tracks)
    hs = [p for p in inp.room if p.side is None] or [p for p in inp.room if p.decides]     # the tracks that decide
    if not hs:
        o = _lead(inp, _other(viewer.side)) if viewer else None
        hs = [o] if o else [p for p in inp.room if p.side]
    W = sum(p.weight * (1.0 + p.power) for p in hs)
    m = sum(p.weight * (1.0 + p.power) * T.get(p.id, 0.0) for p in hs) / W
    return max(-1.0, min(1.0, m / inp.dials["mood_scale"]))


def _wF(h, D):
    return (h.focus - D["floor"]) / (D["mid"] - D["floor"])


def _wA(h, D):
    return (h.attunement - D["floor"]) / (D["mid"] - D["floor"])


def elab(h, inp):
    """R12 Reason, ELM: the able (Reason) and involved (stake) weigh the case; a crowd lowers it. 0..1."""
    D = inp.dials
    return max(0.0, min(1.0, 0.5 + D["sense_step"] * (h.reason - D["mid"]) + D["involve"] * max(abs(x) for x in h.stake)
                        - D["crowd_lean"] * _crowd(inp)))


def credit(h, it):
    return max(-1.0, min(1.0, 2.0 * it.weight - 1.0 + _bond(h, it.source) - max(0.0, _bond(h, it.about))))


def relevance(v, D):
    """REASON (A-143): how relevant the content of his speech is to the live point and to the stakes that bear on
    those who decide: 0..2, 1 at the middle of the scale."""
    return 1.0 if not D["relevance"] else 2.0 * (v.reason - D["floor"]) / (D["ceiling"] - D["floor"])


def landing(h, side, channel, tag):
    """how a speech FRAMED on `tag` lands with this listener, on his TRUE interior: he must hold the tag (its weight)
    and the matter must bear on it his way; a frame on something he does not hold misses and misfits."""
    for c, t, w, bear in h.holds:
        if c == channel and t == tag:
            return max(-1.0, min(1.0, SIGN[side] * w * bear + 0.5 * (2.0 * w - 1.0)))
    return -0.5


def fit(h, voice, side, ground, it, tag=None):
    """the ground against how the MATTER (or the item, or the speaker) bears on this listener: -1..1."""
    if ground == "evidence":
        return credit(h, it) if it else -1.0
    if ground == "solidarity":
        return max(-1.0, min(1.0, _bond(h, voice.id) + 0.5 * (2.0 * h.care[2] - 1.0)))
    c = CHANNEL[ground]
    if tag is not None:
        return landing(h, side, c, tag)
    return max(-1.0, min(1.0, SIGN[side] * h.stake[c] + 0.5 * (2.0 * h.care[c] - 1.0)))


def aim(t, ground, it, tag=None):
    """how hard a press BITES on him (B7): it names its object, the held thing it hits, and bites by how much he
    holds it AND how far THIS matter bears on it (either way: a threat to what he holds unsettles him whichever side
    it helps). Unsigned, so it is never the same number as the fit. A press on what he does not hold misses."""
    if ground == "evidence":
        if not it:
            return -1.0
        return max(-1.0, min(1.0, it.weight * (1.0 if it.about == t.id else max(0.0, _bond(t, it.about))) * 2.0 - 1.0))
    c = CHANNEL[ground]
    w, bear = t.care[c], t.stake[c]
    if tag is not None:
        hit = next(((ww, b) for ch, tg, ww, b in t.holds if ch == c and tg == tag), None)
        if hit is None:
            return -1.0
        w, bear = hit
    return max(-1.0, min(1.0, w * (1.0 + abs(bear)) - 1.0))


def frame(inp, hs, side, ground, acc=1.0, xa=0.0, xb=0.0, score=None):
    """ATTUNEMENT (A-142): the frame he picks for a ground, from what he BELIEVES these listeners hold: each tag's
    worth as he reads it (true, blurred by his accuracy), the body's weighted mean. A body has one frame. With
    `score` = aim (one listener: the man pressed) it picks the press's object the same way."""
    if ground not in CHANNEL:
        return None
    c = CHANNEL[ground]
    tags = [t for ch, t in inp.frames if ch == c]
    if not tags:
        return None
    score = score or (lambda h, t: landing(h, side, c, t))
    W = sum(h.weight for h in hs) or 1.0
    best, bv = None, -1e9
    for k, t in enumerate(tags):
        noise = xa * math.cos(1.7 * k) + xb * math.sin(1.7 * k)          # his own two normals, mixed per tag
        v = sum(h.weight * score(h, t) for h in hs) / W + (1.0 - acc) * 0.5 * inp.dials["read_blur"] * noise
        if v > bv:
            best, bv = t, v
    return best


def press_object(inp, T, ground, acc=1.0, xa=0.0, xb=0.0):
    return frame(inp, [T], T.side, ground, acc, xa, xb, score=lambda h, t: aim(h, ground, None, t))


def insincerity(voice, side, ground, it):
    """sincerity is agreement between what he says and what he KNOWS (`believes`, a false item) and, on the ground of
    what is owed, what he HOLDS (preaching a duty or conviction he holds the other way). Arguing against his own
    interest is not insincere (B2: word against behaviour is not a lie)."""
    x = max(0.0, -SIGN[side] * voice.believes)
    if it is not None and not it.sincere:
        x = 1.0
    if ground == "authority":
        x = max(x, -SIGN[side] * voice.stake[1])
    return max(0.0, min(1.0, x))


def _cg(inp, g):
    return {a: b for a, b, _ in inp.grounds}[g]


def _era(inp, g):
    return {a: w for a, _, w in inp.grounds}[g]


def _weight(inp, st, g):
    """what a ground is worth here and now: the era's weight on it times the live rung's (stasis, A-134: fact is argued
    from the proof, definition from what is owed, justification from what it brings and who stands with whom)."""
    r = inp.rite
    return _era(inp, g) * _d(_d(r.weighs).get(r.issues[st.issue], ())).get(g, 1.0)


def validation(h, inp):
    """ADJUDICATOR'S REASON (A-144): how well he can dissect a speech and tell whether it is coherent, sound and
    good: 0 (he cannot tell; he goes by manner and standing) .. 1. The able and the involved validate; a crowd less."""
    return elab(h, inp)


def discern(inp, h, T):
    """ADJUDICATOR'S ATTUNEMENT on a rattle (A-144: he perceives "comfort/discomfort and sincerity/insincerity"): the
    rattled man's discomfort read for what it is. An attuned listener discounts an honest man's nerves and reads a
    false man's as guilt; a dull one the other way; 1 at the middle of the scale (B10: discomfort is never deducted
    as insincerity; this is its own signed rule, `comfort_step`)."""
    D = inp.dials
    false = max(0.0, -SIGN[T.side] * T.believes) if T.side else 0.0
    return max(0.0, 1.0 + D["comfort_step"] * (_wA(h, D) - 1.0) * (2.0 * false - 1.0))


def theatre(h, D):
    """ADJUDICATOR'S FOCUS, its second half (A-144: "not swayed by irrelevant things"): a rattle proves nothing
    about the merits; how far its theatre reaches him: 2 at Focus 1, 1 at the middle of the scale, 0 at the top."""
    return max(0.0, 2.0 - _wF(h, D))


def awe(inp, v):
    """ADJUDICATOR'S PRESENCE AND STATION (A-144): how far those who decide intimidate this participant: their
    Presence and their station over his, less his own Will. It acts on HIM, on his confidence and composure: he
    tires sooner (his staying power is less by it) and is easier to rattle (a press on him meets less). It is NOT an
    obstacle on his speeches."""
    D = inp.dials
    ds = [d for d in inp.room if d.decides and d.id != v.id]
    if not ds:
        return 0.0
    W = sum(d.weight for d in ds)
    return D["awe_step"] * sum(d.weight * max(0.0, (d.presence - D["mid"]) / 3.0 + (d.power - v.power) / D["power_scale"]
                                              - (v.will - D["mid"]) / 3.0) for d in ds) / W


def tell(inp, st, voice, insinc):
    """what an attuned adjudicator deducts as a ploy (A-144, R12): the participant's insincerity, nothing else. His
    discomfort is perceived too (`discomfort`; `discern` on a rattle; a played judge is shown it), never as a lie."""
    return min(1.0, insinc)


def discomfort(st, voice):
    c = _d(st.cond)[voice.id]
    return min(1.0, c.strain + 0.5 * c.rattles)


def _heard_abs(inp, v):
    D = inp.dials
    need = 1.0 + (D["ceiling"] - 1.0) * _crowd(inp)
    return max(D["heard_floor"], 1.0 - D["heard_step"] * max(0.0, need - v.presence))


def heard(inp, v):
    """PRESENCE: the share of him the room listens to, against the man opposite: the better heard of the two is
    heard whole and the other by his share; with nobody opposite (a rally, a witness), against what an ordinary man
    of the middle Presence would get from this room. So a room does not tilt against whoever speaks (C1), and
    Presence still decides who is heard (and, through its share of the dice, how far)."""
    own = _heard_abs(inp, v)
    o = _lead(inp, _other(v.side)) if v.side else None
    if o is None:
        return min(1.0, own / _heard_abs(inp, replace(v, presence=inp.dials["mid"])))
    return own / max(own, _heard_abs(inp, o))


def case_pool(inp, v, ground):
    D = inp.dials
    k = min(10, max(0, round(10 * (_cg(inp, ground) + inp.rite.reason_lean - D["crowd_lean"] * _crowd(inp)))))
    return heard(inp, v) * pool_of(weighted_tenth((v.reason, v.presence), (k, 10 - k)) + v.rank, 0, D["pool_add"],
                                   D["pool_floor"])


def _short(inp, p, c):
    return max(0.0, inp.rite.standard + inp.dials["show"] * c.rattles - p.grace)


def esteem(inp, st, v):
    """Grace: his standing in the room THIS sitting: how much better he meets what the occasion and his own
    rattles demand than the man opposite does. Derived; never stored on a person (S-7)."""
    cd = _d(st.cond)
    o = _lead(inp, _other(v.side)) if v.side else None
    return (_short(inp, o, cd[o.id]) if o else 0.0) - _short(inp, v, cd[v.id])


def weary(inp, v, c):
    """Will: staying power. Past it every speech is made uphill."""
    D = inp.dials
    return D["weary_step"] * max(0.0, c.spent - (D["stay_base"] + D["stay_per_will"] * v.will - awe(inp, v)))


def standing_gap(inp, v, T):
    """Reason: the other side's circumstances (seat, office, wealth, influence, faction: host `power`) stand
    against him unless he can account for them."""
    D = inp.dials
    account = (v.reason - D["floor"]) / (D["ceiling"] - D["floor"])
    return D["gap_step"] * max(0.0, T.power - v.power) * (1.0 - account)


def heat(inp, st, v):
    return -SIGN[v.side] * mood(inp, st) * _crowd(inp) if v.side else 0.0


def _pull(inp, st, v, c):
    D = inp.dials
    return D["press_pull"] * c.heat + D["rattle_pull"] * c.rattles + inp.rite.unrest \
        + D["heckle"] * max(0.0, heat(inp, st, v))


def _hold_pool(v, D):
    return pool_of(v.focus, 0, D["pool_add"], D["pool_floor"])


def drift_of(pull, hold):
    """FOCUS (R1, B14): how far he is pulled off the point: the pull less what his Focus holds, never below 0 and
    continuous in the pull (at no pull, no drift; a weak hold is a hold of 0, not a push)."""
    return max(0.0, pull - max(0.0, hold))


def _uses(st, side, key):
    return _d(st.used).get((side, key), 0)


def _items(inp, mover):
    return [it for it in mover.items if it.kind in inp.rite.admits]


def _find_item(inp, iid):
    return next((it for p in inp.room for it in p.items if it.id == iid), None)


def _voice(inp, mover, it):
    if it is not None and it.kind == "testimony" and it.source and it.source != mover.id:
        for p in inp.room:
            if p.id == it.source and p.side is None and not p.decides:
                return p
    return mover


def _foe(inp, mover):
    """whose circumstances he must account for: the other side's lead; in an abridged act (`close: exchange`), the
    one he addresses, who is the man opposite there though the act gives him no move. With nobody opposite there is
    no foe and no gap (A9, A-144: the station of those who decide is awe on him, never an obstacle on his speech)."""
    o = _lead(inp, _other(mover.side))
    if o is None and inp.rite.close == "exchange":
        o = next((p for p in inp.room if p.decides and not p.side and p.id != mover.id), None)
    return o


def pressable(inp, side, P, S) -> bool:
    """a press is cross-examination: it lies only where something stands against the man pressed, a live point of his
    own that stands, or a charge laid on him (his side is not the bearer's and must answer). A man who has said nothing
    and is charged with nothing is not pressed (finding 18: debates and negotiations opened by pressing a silence)."""
    return (P is not None and S > 0) or (side != inp.rite.bears and _reply(inp, side) == "must")


def _sole(inp, p) -> bool:
    """his verdict alone is the close: he decides and nobody else does (one seat, one vote)."""
    return p.decides and not any(q.decides for q in inp.room if q.id != p.id)


def _deciders_for(inp, mover):
    """whom a speaker must move: those who decide and are not on his side, AND HIMSELF if he decides (C2: a party
    who decides is moved by his own case as he hears it); with nobody deciding, everyone not on his side."""
    hs = [p for p in inp.room if p.decides and (p.side != mover.side or p.id == mover.id)]
    return hs or _hearers(inp, mover, mover.side)


# ------------------------------------------------------------------ the one speech composer
def speech(inp, st, mover, voice, h, ground, it, relation, *, press_on=None, abridged=False, tag=None):
    """one speech heard by `h`. `h` may be the speaker himself, where he decides (C2): then it is his own Reason that
    validates it and his own Will that resists it, as for any listener."""
    D, r = inp.dials, inp.rite
    c = _d(st.cond)[voice.id]
    pool = case_pool(inp, voice, ground)
    foe = _foe(inp, mover)
    ops = [("weary", weary(inp, voice, c), 1.0), ("standing", standing_gap(inp, voice, foe) if foe else 0.0, 1.0)]
    if press_on is not None:
        T = press_on
        ct = _d(st.cond)[T.id]
        sig = level(D["fit_level"]) * _weight(inp, st, ground) * aim(T, ground, it, tag) + D["room_level"] * heat(inp, st, T) \
            + D["esteem_step"] * esteem(inp, st, voice)
        ops.append(("press", D["press_ob"], 1.0))
        opp = max(0.0, T.will + T.rank - ct.strain / MU_PER_DIE - awe(inp, T))      # awe: as so many points of Will
        return pool, sig, SocialContestInput(pool, opp, sig, 0.0, tuple(ops), D["pool_default"], D["pool_add"],
                                             D["opposition_rate"], None, False)
    v = validation(h, inp)
    rl = 1.0 + 2.0 * v * (relevance(voice, D) - 1.0)        # how sound the speech is, as far as HE can validate it
    f = fit(h, voice, mover.side, ground, it, tag) + D["rel_gain"] * (rl - 1.0) - D["repeat_step"] * _uses(st, mover.side, it.id if it else ground)
    sig = level(D["fit_level"]) * _weight(inp, st, ground) * f \
        + D["esteem_step"] * esteem(inp, st, voice) * 2.0 * (1.0 - v) \
        + (rl * level(D["answer_level"]) if relation == "answers" else 0.0)
    return pool, sig, SocialContestInput(pool, h.will + h.rank, sig, (r.difficulty + r.gravity) if abridged else 0.0,
                                         tuple(ops), D["pool_default"], D["pool_add"], D["opposition_rate"], None, False)


def _phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def _epos(mu, sd):
    z = mu / sd
    return mu * _phi(z) + sd * math.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi)


def close_input(inp, track):
    D, r = inp.dials, inp.rite
    pool = pool_of(D["mid"], 0, D["pool_add"], D["pool_floor"])
    return SocialContestInput(pool, D["mid"], D["track_step"] * track, r.difficulty, (("gravity", r.gravity, 1.0),),
                              D["pool_default"], D["pool_add"], D["opposition_rate"], None, False)


def p_carried(inp, track):
    x = close_input(inp, track)
    ob, _ = obstacle(x)
    mu = MU_PER_DIE * x.pool + net_boost(x.leverage, x.pool) - ob
    return 1 - _phi((1.0 - mu) / (SD_PER_DIE * math.sqrt(x.pool)))


def close_odds(inp, tracks: Mapping) -> float:
    """P(carried) of THE CLOSE ITSELF with each who decides at his own track (A-133: the card's odds are the
    proceeding's own): `bench` the presiding seat's; `declared` at least the quorum of the seats carrying, each his
    own draw (the quorum-th best margin); `hearers` the weight-mean margin, one normal per hearer. No draw."""
    r = inp.rite
    ds = sorted((p for p in inp.room if p.decides), key=lambda p: (-p.precedence, p.id))
    if not ds or r.close in ("consent", "exchange"):
        return 0.0
    if r.close == "bench":
        return p_carried(inp, tracks[ds[0].id])
    if r.close == "declared":
        q = min(len(ds), r.quorum or 1)
        dist = [1.0]                                     # P(k seats carry), seat by seat
        for d in ds:
            p = p_carried(inp, tracks[d.id])
            dist = [(dist[k] if k < len(dist) else 0.0) * (1 - p) + (dist[k - 1] * p if k > 0 else 0.0) for k in range(len(dist) + 1)]
        return sum(dist[q:])
    W = sum(d.weight for d in ds)
    xs = [close_input(inp, tracks[d.id]) for d in ds]
    pool, ob = xs[0].pool, obstacle(xs[0])[0]
    mu = MU_PER_DIE * pool - ob + sum(d.weight * net_boost(x.leverage, pool) for d, x in zip(ds, xs)) / W
    sd = SD_PER_DIE * math.sqrt(pool) * math.sqrt(sum(d.weight ** 2 for d in ds)) / W
    return 1 - _phi((1.0 - mu) / sd)


def believed_odds(inp, mood_seen):
    """what a chooser may be shown: the close as the room SEEMS to stand to him (his believed mood), an ordinary
    bench assumed (B05.62). No true attribute and no true start enters it. Under consent there are no odds."""
    if inp.rite.close == "consent":
        return 0.0
    return p_carried(inp, mood_seen * inp.dials["mood_scale"])


# ------------------------------------------------------------------ the view
def temper_of(p, c, D):
    """A-136, A-146: how far THIS sitting's provocation has run past what his Will and Grace carry: 0 composed .. 1
    lost. The provocation is his `heat` (a rattle adds one; it cools as he speaks); what he carries is his Will and
    Grace against twice the middle of the scale. Nobody is born broken: with no rattle there is no temper (C4)."""
    return max(0.0, min(1.0, D["temper_step"] * c.heat * 2.0 * D["mid"] / max(1.0, p.will + p.grace)))


def _yield_to(D):
    """how far a given-up matter puts the room: as far as the close's leverage can carry it (M_MAX / track_step)."""
    return M_MAX / D["track_step"] if D["track_step"] else D["mood_scale"]


def _broken(p, c, D):
    return temper_of(p, c, D) >= D["temper_break"]


def _legal(inp, mover, turns_left, c=None):
    """A-146: a man whose temper has broken cannot hold his tongue: `rest` leaves his menu (player or NPC alike).
    A legality rule on the one existing quantity; nothing is resolved by it."""
    if turns_left <= 0:
        return ("rest",)
    ms = _d(inp.rite.moves).get(mover.side, ())
    if c is not None and _broken(mover, c, inp.dials) and len(ms) > 1:
        ms = tuple(m for m in ms if MOVES[m].effect != "none")
    return ms


def _believed(h, acc, D):
    """B11, A-141: a chooser reads each listener's judging operands and resisting Will as he BELIEVES them: the truth
    as far as his accuracy reaches, the middle of the scale for the rest (a stranger is an ordinary man, B05.62)."""
    if acc >= 1.0:
        return h
    b = lambda x: D["mid"] + acc * (x - D["mid"])
    return replace(h, attunement=b(h.attunement), focus=b(h.focus), reason=b(h.reason), will=b(h.will))


def menu(inp, st, mover, turns_left, frames=None, objects=None, acc=1.0):
    """The worth of every option on his menu, from the engine's own values with each listener read as he believes
    him (`_believed`): [(move, ground, item, relation, ev, p, frame)]. No draw. Nobody is shown this: a View shows
    `perceived` of it."""
    D = inp.dials
    G = [g for g, _, _ in inp.grounds]
    c = _d(st.cond)[mover.id]
    hs = [h if h.id == mover.id else _believed(h, acc, D) for h in _deciders_for(inp, mover)]
    W = sum(h.weight for h in hs) or 1.0
    mean = lambda f: sum(h.weight * f(h) for h in hs) / W
    other_side = _other(mover.side)
    tid = _d(st.last_voice).get(other_side)
    T = _who(inp, tid) if tid else _lead(inp, other_side)
    items = _items(inp, mover)
    pull = _pull(inp, st, mover, c)
    Pf = _hold_pool(mover, D)
    e_drift = min(pull, _epos(pull - (MU_PER_DIE * Pf - even_line(D["pool_add"])), SD_PER_DIE * math.sqrt(Pf))) if pull > 0 else 0.0
    rep_ = _reply(inp, mover.side)
    P = _point(st, _d(st.live).get(other_side))
    S = _stands(P) / max(1, len(P.held)) if P else 0.0
    must_answer = P is not None and S > 0 and rep_ == "must"
    bur = burden(inp, st, mover)
    sc_a = mean(lambda h: silence_cost(inp, h, P, mover)) if must_answer else 0.0           # a point left standing
    sc_b = mean(lambda h: silence_cost(inp, h, None, mover)) if (bur and not must_answer) else 0.0   # a matter not put
    m_true = SIGN[mover.side] * mood(inp, st, mover)
    cands = [(g, None) for g in G if g != "evidence"] + [("evidence", it) for it in items]
    if frames is None:                                   # with no reading given: the frames a perfect reader would pick
        frames = {g: frame(inp, hs, mover.side, g) for g in G}
    if objects is None and T is not None:
        objects = {g: press_object(inp, T, g) for g in G}
    def best_raise(stx):
        best = -9.0
        for g, it in cands:
            pool = case_pool(inp, mover, g)
            ins = insincerity(mover, mover.side, g, it)
            mu = mean(lambda h: (lambda x: MU_PER_DIE * pool + net_boost(x.leverage, pool) - obstacle(x)[0])(
                speech(inp, stx, mover, mover, h, g, it, "raises", tag=frames.get(g))[2]) - D["ploy_step"] * _wA(h, D) * ins)
            sd = SD_PER_DIE * math.sqrt(pool)
            best = max(best, _epos(mu, sd) - D["flop"] * _epos(-mu, sd))
        return best

    out = []
    for mid in _legal(inp, mover, turns_left, c):
        row = MOVES[mid]
        if row.effect == "track":
            for g, it in cands:
                pool = case_pool(inp, mover, g)
                ins = insincerity(mover, mover.side, g, it)
                sd = SD_PER_DIE * math.sqrt(pool)
                for rel in (["answers"] if (rep_ != "raise" and P is not None and S > 0) else []) + ["raises"]:
                    def mu_h(h, rel=rel):
                        x = speech(inp, st, mover, mover, h, g, it, rel, abridged=inp.rite.close == "exchange", tag=frames.get(g))[2]
                        ob, _ = obstacle(x)
                        return MU_PER_DIE * pool + net_boost(x.leverage, pool) - ob - D["off_step"] * _wF(h, D) * e_drift \
                            - D["ploy_step"] * _wA(h, D) * tell(inp, st, mover, ins)
                    mu = mean(mu_h)
                    if rel == "answers":         # bounded both ways by how far the point stands (C1)
                        ev = min(S, _epos(mu, sd)) - D["flop"] * min(S, _epos(-mu, sd))
                    else:
                        up, dn = _epos(mu, sd), _epos(-mu, sd)
                        invited = D["invite"] if (_d(inp.rite.moves).get(other_side) and _reply(inp, other_side) != "raise"
                                                  and T is not None) else 0.0
                        ev = (1.0 - invited) * up - D["flop"] * dn - sc_a
                    out.append((mid, g, it.id if it else None, rel, ev, 1 - _phi(-mu / sd), frames.get(g)))
        elif row.effect == "strike":
            if T is None or not pressable(inp, other_side, P, S):
                continue
            ct = _d(st.cond)[T.id]
            for g, it in cands:
                tag = (objects or {}).get(g) if it is None else None
                pool, sig, x = speech(inp, st, mover, mover, T, g, it, "presses", press_on=T, tag=tag)
                ob, _ = obstacle(x)
                mu = MU_PER_DIE * pool + net_boost(sig, pool) - ob
                p = 1 - _phi(-mu / (SD_PER_DIE * math.sqrt(pool)))
                gain = D["rattle_gain"] * (1.0 - D["reactance"] * ct.rattles) * mean(lambda h: (1.0 - max(0.0, _bond(h, T.id))) * discern(inp, h, T) * theatre(h, D))
                lasting = _lasting(inp, st, T, ct, hs, mean, turns_left)
                ins = 1.0 if (it is not None and not it.sincere) else 0.0
                ev = p * (gain + lasting) - (1 - p) * D["rebound"] - D["off_step"] * e_drift - D["ploy_step"] * ins \
                    - sc_a - sc_b
                out.append((mid, g, it.id if it else None, "presses", ev, p, tag))
        elif row.effect == "yield":
            own = _d(st.tracks).get(mover.id, 0.0)
            last = st.issue >= len(inp.rite.issues) - 1
            if (inp.rite.concede == "accepts" or last) and (inp.rite.close == "consent" or _sole(inp, mover)):
                ev = -SIGN[mover.side] * own - D["consent_at"]       # his accept IS the close: his own consent
            elif inp.rite.concede == "accepts" or last:              # one seat, one vote: on a close others share,
                ev = -_yield_to(D) * (1.0 + m_true)                  # his yield gives the matter up like any party's
            else:                                 # C1, C5: what descending buys: the next rung's better ground, fresh
                st2 = replace(st, issue=st.issue + 1, live=(("for", None), ("against", None)),
                              used=tuple((k, v) for k, v in st.used if k[0] != mover.side))
                gain = max(0.0, best_raise(st2) - best_raise(st)) * max(0, turns_left - 1)
                ev = gain - D["concede_step"] * (1.0 + max(abs(x) for x in mover.stake))
            out.append((mid, None, None, "concedes", ev, None, None))
        else:
            out.append((mid, None, None, "rests", -sc_a - sc_b, None, None))
    return out, T, P, S


def _lasting(inp, st, T, ct, hs, mean, turns_left):
    """what a rattle goes on doing after it lands, honestly reckoned (C1): his standing falls only as far as his Grace
    lacks headroom (`show`), which tells on both men's later speeches (esteem is relative); he tires sooner only if it
    takes him past his staying power; his next speech is pulled. In track units, through one speech's slope, the
    later speeches' share discounted by `invite` exactly as a raise's worth is (an answer undoes part of it)."""
    D, r = inp.dials, inp.rite
    slope = 0.75 * SD_PER_DIE * math.sqrt(pool_of(D["mid"] + 1.0, 0, D["pool_add"], D["pool_floor"]))
    dshort = max(0.0, r.standard + D["show"] * (ct.rattles + 1) - T.grace) - max(0.0, r.standard + D["show"] * ct.rattles - T.grace)
    v = mean(lambda h: validation(h, inp))
    stay = D["stay_base"] + D["stay_per_will"] * T.will - awe(inp, T)
    k = max(0, turns_left - 1)
    return k * (2.0 * D["esteem_step"] * dshort * 2.0 * (1.0 - v) * slope * (1.0 - D["invite"])
                + D["weary_step"] * (1.0 if ct.spent + 1.0 > stay else 0.0) * 0.75) \
        + D["off_step"] * mean(lambda h: _wF(h, D)) * 0.6 * (D["press_pull"] + D["rattle_pull"]) * 0.75


def perceived(true_worth, acc, x, lean, D):
    """ATTUNEMENT (A-141): the one gauge. What a contestant takes an option to be worth is its worth plus an error
    that shrinks as his reading sharpens: his own noise `x`, and his stable bias `lean` (an optimist overrates
    acting, a pessimist underrates it). At acc 1 perceived is true."""
    return true_worth + (1.0 - acc) * (D["read_blur"] * x + D["bias_step"] * lean)


def build_view(inp, st, mover, rng, turns_left) -> View:
    """the view's share of the exchange's draws (DRAWS_PER_EXCHANGE): his accuracy; per ground what arguing on it
    is worth, what pressing on it is worth, two for the frame, two for the press's object; conceding; resting; the
    mood; their point; his own point; the other's intent; his esteem; his awe."""
    D = inp.dials
    G = [g for g, _, _ in inp.grounds]
    c = _d(st.cond)[mover.id]
    # his accuracy is his Attunement, with a little luck: 0.5 at the middle of the scale; nothing opposes it
    acc = (1.0 + math.tanh((MU_PER_DIE * (mover.attunement - D["mid"]) + D["read_noise"] * rng.normal()) / D["read_scale"])) / 2.0
    xarg = dict(zip(G, (rng.normal() for _ in G)))
    xprs = dict(zip(G, (rng.normal() for _ in G)))
    xc, xm, xt, xo, xi, xe, xr, xw = (rng.normal() for _ in range(8))
    xfa = dict(zip(G, (rng.normal() for _ in G)))
    xfb = dict(zip(G, (rng.normal() for _ in G)))
    xoa = dict(zip(G, (rng.normal() for _ in G)))
    xob = dict(zip(G, (rng.normal() for _ in G)))
    hs = [h if h.id == mover.id else _believed(h, acc, D) for h in _deciders_for(inp, mover)]
    frames = {g: frame(inp, hs, mover.side, g, acc, xfa[g], xfb[g]) for g in G}       # framed from his believed reading
    other_side = _other(mover.side)
    tid = _d(st.last_voice).get(other_side)
    T0 = _who(inp, tid) if tid else _lead(inp, other_side)
    objects = {g: press_object(inp, T0, g, acc, xoa[g], xob[g]) for g in G} if T0 is not None else {}
    true, T, P, S = menu(inp, st, mover, turns_left, frames, objects, acc)
    opts = []
    for mv, g, it, rel, ev, p, fr in true:
        acting = MOVES[mv].draw
        x = xarg[g] if mv == "argue" else xprs[g] if mv == "press" else xc if mv == "concede" else xr
        pe = perceived(ev, acc, x, mover.bias if acting else 0.0, D)
        pp = None if p is None else max(0.0, min(1.0, perceived(p, acc, 0.1 * x, 0.1 * mover.bias, D)))
        opts.append(Option(mv, g, it, rel, round(pe, 2), None if pp is None else round(pp, 2), fr))
    m_seen = max(-1.0, min(1.0, perceived(SIGN[mover.side] * mood(inp, st, mover), acc, 0.25 * xm, 0.0, D)))
    intent = max(-1.0, min(1.0, perceived(sum(T.stake) / 3.0 if T else 0.0, acc, 0.25 * xi, 0.0, D)))
    Po = _point(st, _d(st.live).get(mover.side))
    live_theirs = (P.id, P.ground, P.item, round(perceived(S, acc, 0.5 * xt, 0.0, D), 1)) if P else None
    live_own = (Po.id, Po.ground, Po.item, round(perceived(_stands(Po) / max(1, len(Po.held)), acc, 0.5 * xo, 0.0, D), 1)) if Po else None
    vis = tuple((p.id, _d(st.cond)[p.id].rattles) for p in inp.room if p.side)
    return View(st.n, mover.id, mover.side, inp.rite.issues[st.issue], live_theirs, live_own, tuple(opts), c,
                round(perceived(esteem(inp, st, mover), acc, 0.25 * xe, 0.0, D), 2), round(weary(inp, mover, c), 2),
                round(max(0.0, perceived(awe(inp, mover), acc, 0.25 * xw, 0.0, D)), 2),
                _broken(mover, c, D), vis, m_seen, believed_odds(inp, m_seen),
                intent, turns_left, acc, burden(inp, st, mover))


# ------------------------------------------------------------------ the automatic policy (A-136)
def auto(view: View, me: Present, D) -> Choice:
    """While he keeps his temper (below `temper_break`) he takes the option his own reading says is worth most.
    Once it breaks, the man shows: he argues from what he himself holds, the proud press and will not give way, the
    timid give way, the orator plays to the room, a grudge goes after its object."""
    t = temper_of(me, view.own, D)
    t = t if t >= D["temper_break"] else 0.0
    foe = max((i for i, _ in view.visible if i != me.id), key=lambda i: abs(_bond(me, i)), default=None)
    nerve = (me.will - D["mid"]) / 3.0
    best, bv = None, -1e9
    for o in view.options:
        v = o.ev
        if o.move == "argue" and o.ground in CHANNEL:
            v += t * D["grain"] * ((2.0 * me.care[CHANNEL[o.ground]] - 1.0)
                                   + ((me.presence - D["mid"]) / 3.0 if o.ground == "solidarity" else 0.0))
        elif o.move == "press":
            v += t * (D["grudge"] * (-_bond(me, foe)) + D["pride"] * nerve)
        elif o.move == "concede":
            v -= t * D["pride"] * nerve
        if v > bv + 1e-12:
            best, bv = o, v
    return Choice(best.move, best.ground, best.item, best.relation)


# ------------------------------------------------------------------ one exchange
def _start(inp) -> Sitting:
    if inp.state is not None:
        return inp.state
    return Sitting(tracks=tuple((p.id, p.start) for p in inp.room),
                   cond=tuple((p.id, Cond(strain=p.strain)) for p in inp.room))


def exchange(inp, st, mover, ch, rng, abridged=False, tag=None):
    D, r = inp.dials, inp.rite
    row = MOVES[ch.move]
    it = _find_item(inp, ch.item) if ch.item else None
    voice = _voice(inp, mover, it) if row.effect == "track" else mover
    cond = _d(st.cond)
    cv = cond[voice.id]
    side, sg = mover.side, SIGN[mover.side]
    other = _other(side)
    pull = _pull(inp, st, voice, cv)
    hold = roll_net_continuous(_hold_pool(voice, D), rng=rng) - even_line(D["pool_add"])
    drift = drift_of(pull, hold)
    z = rng.normal()
    tracks, live, points, used = _d(st.tracks), _d(st.live), list(st.points), _d(st.used)
    hearers = _hearers(inp, voice, side)
    own = [mover] if (mover.decides and voice.id == mover.id) else []        # C2: he is moved by his own case
    judges = [h for h in hearers + own if h.decides] or hearers
    lt = live.get(other)
    P_lt = _point(st, lt)
    rep = _reply(inp, side)
    stands = P_lt is not None and _stands(P_lt) > 0
    relation = ch.relation or {"track": "raises", "strike": "presses", "yield": "concedes", "none": "rests"}[row.effect]
    if relation == "answers" and not stands:
        relation = "raises"                               # an answer is to a point that stands; else it raises
    unanswered = stands and relation != "answers" and row.effect != "yield"
    evade_a = rep == "must" and unanswered
    evade_b = burden(inp, st, mover) and row.effect in ("none", "strike") and not evade_a
    evaded = (evade_a or evade_b) and r.silence != "free"
    left = lt if unanswered else None
    off = drift
    moved, margins, margin, rattled, target, closed, pid, insinc, terms, ended = [], [], 0.0, None, None, None, None, 0.0, (), None
    caught = []
    issue = r.issues[st.issue]
    obj = tag

    def move(h, d):
        moved.append((h.id, d)); tracks[h.id] += d

    if row.effect == "track":
        insinc = insincerity(voice, side, ch.ground, it)
        held, tot, W = {}, 0.0, 0.0
        for h in hearers + own:
            pool, sig, x = speech(inp, st, mover, voice, h, ch.ground, it, relation, abridged=abridged, tag=tag)
            ob, terms = obstacle(x)
            ded = D["ploy_step"] * _wA(h, D) * tell(inp, st, voice, insinc)
            m = MU_PER_DIE * pool + SD_PER_DIE * math.sqrt(pool) * z + net_boost(sig, pool) - ob \
                - D["off_step"] * _wF(h, D) * off - ded
            if insinc > 0 and m < 0 <= m + ded:
                caught.append(h.id)                       # his reading of the speaker turned it (B2)
            if h in judges:
                tot += h.weight * m; W += h.weight
            margins.append((h.id, Margin(net=m + ob, ob=ob, terms=terms)))
            if relation == "answers":                     # bounded both ways by how far the point stands with him (C1)
                s = max(0.0, SIGN[other] * _d(P_lt.held).get(h.id, 0.0))
                d = sg * (min(s, m) if m > 0 else -D["flop"] * min(s, -m))
                P_lt = replace(P_lt, held=_put(P_lt.held, h.id, _d(P_lt.held).get(h.id, 0.0) + d))
            else:
                d = sg * (m if m > 0 else D["flop"] * m)  # a speech that falls flat costs a part of its shortfall
                held[h.id] = d
            move(h, d)
        margin = tot / W if W else 0.0
        if relation == "answers":
            pid = lt
            points[[p.id for p in points].index(lt)] = P_lt
        else:
            pid = len(points)
            points.append(Point(pid, side, issue, ch.ground, ch.item, voice.id, tuple(held.items())))
            live[side] = pid
        key = it.id if it else ch.ground
        used[(side, key)] = used.get((side, key), 0) + 1
        cond[voice.id] = replace(cv, strain=cv.strain + D["grain_strain"] * insinc)
    elif row.effect == "strike":
        lv = _d(st.last_voice).get(other)
        T = _who(inp, lv) if lv else _lead(inp, other)
        target = T.id
        insinc = 1.0 if (it is not None and not it.sincere) else 0.0          # a press made with a forged item
        if it is not None:
            obj = None
        pool, sig, x = speech(inp, st, mover, voice, T, ch.ground, it, relation, press_on=T, tag=obj)
        ob, terms = obstacle(x)
        margin = MU_PER_DIE * pool + SD_PER_DIE * math.sqrt(pool) * z + net_boost(sig, pool) - ob
        ct = cond[T.id]
        landed = margin >= 0
        if landed:
            rattled = T.id
            gain = D["rattle_gain"] * (1.0 - D["reactance"] * ct.rattles)
            cond[T.id] = replace(ct, rattles=ct.rattles + 1, strain=0.0, heat=ct.heat + 1.0, spent=ct.spent + 1.0)
        else:
            gain = -D["rebound"]
            cond[T.id] = replace(ct, strain=ct.strain + D["wear"])
        for h in hearers + ([mover] if mover.decides else []):
            seen = gain * (1.0 - max(0.0, _bond(h, T.id))) * discern(inp, h, T) * theatre(h, D) if landed else gain
            ded = D["ploy_step"] * _wA(h, D) * insinc
            d = sg * (seen - D["off_step"] * _wF(h, D) * off - ded)
            if insinc > 0 and sg * d < 0 <= sg * d + ded:
                caught.append(h.id)
            move(h, d)
        pid = lt
    elif row.effect == "yield":
        last = st.issue >= len(r.issues) - 1
        closed = issue
        if r.concede == "accepts" or last:
            ended = "yielded"                           # he gives up the matter: the room goes to the other side as far
            for h in hearers + ([mover] if mover.decides else []):      # as the close can carry it (M_MAX / track_step),
                move(h, -sg * _yield_to(D) - tracks[h.id])              # and so does he, if it is his to decide
        else:                                           # C5: a conceded issue STAYS conceded and costs, from where he stands
            cost = D["concede_step"] * (1.0 + max(abs(x) for x in mover.stake))
            for h in hearers + ([mover] if mover.decides else []):
                move(h, -sg * cost)
            live = {"for": None, "against": None}
            used = {k: v for k, v in used.items() if k[0] != side}
    if evaded:                                          # silence, or turning away, where he must speak (A-145)
        for h in hearers + ([mover] if mover.decides else []):
            move(h, -sg * silence_cost(inp, h, P_lt if evade_a else None, mover))
    cv2 = cond[voice.id]
    cond[voice.id] = replace(cv2, heat=cv2.heat * (1.0 - D["temper_cool"]), spoken=cv2.spoken + 1,
                             spent=cv2.spent + (1.0 if row.draw else 0.0))
    if voice.id != mover.id:
        cm = cond[mover.id]
        cond[mover.id] = replace(cm, spoken=cm.spoken + 1)
    lv = _d(st.last_voice)
    if row.draw:
        lv[side] = voice.id
    new = Sitting(n=st.n + 1, issue=st.issue + (1 if (closed and ended is None) else 0), points=tuple(points),
                  live=tuple(live.items()), tracks=tuple(tracks.items()), cond=tuple(cond.items()),
                  used=tuple(used.items()), last_voice=tuple(lv.items()), ended=ended)
    beat = Beat(st.n + 1, mover.id, voice.id, side, ch.move, relation, issue, ch.ground, ch.item, pid, target,
                round(margin, 3), round(drift, 3), evaded, left, round(insinc, 3), tuple(caught), rattled,
                (tag if row.effect == "track" else obj if row.effect == "strike" else None),
                round(relevance(voice, D), 2), round(heard(inp, voice), 2), round(esteem(inp, st, voice), 2),
                _broken(mover, _d(st.cond)[mover.id], D), tuple(moved), closed,
                round(mood(inp, new), 3), terms)
    return new, beat, margins, ended


# ------------------------------------------------------------------ the sitting
def order(inp):
    sp = [p for p in inp.room if p.side and _d(inp.rite.moves).get(p.side)]
    return sorted(sp, key=lambda p: (0 if p.side == inp.rite.bears else 1, -p.precedence, p.id))


def proceed(inp: Input, rng, decide: Optional[Callable] = None, deciders: Optional[Mapping] = None,
            rulings: Optional[Mapping] = None) -> Outcome:
    """`deciders[person]` (or `decide`) chooses for a speaker; `rulings[person]` rules for a played adjudicator.
    A resumed sitting (`inp.state`) continues: each speaker has the rite's turns less what he has already spoken.
    The sitting closes when the turns the forum gives are spent, when a whole round rests, or when a side yields:
    the forum's time is the measure of when those who decide are ready (D5, decided by the ladder)."""
    D, r = inp.dials, inp.rite
    G = len(inp.grounds)
    st = _start(inp)
    abridged = r.close == "exchange"
    beats, ended, ended_by, last_m = [], None, None, None
    sp = order(inp)
    while ended is None:
        able = [me for me in sp if _d(st.cond)[me.id].spoken < r.turns]
        if not able:
            break
        rests = 0
        for me in able:
            c0 = rng.count
            view = build_view(inp, st, me, rng, r.turns - _d(st.cond)[me.id].spoken)
            fn = (deciders or {}).get(me.id, decide)
            ch = fn(view, me) if fn else auto(view, me, D)
            pick = next((o for o in view.options if (o.move, o.ground, o.item, o.relation) == tuple(ch)), None)
            if pick is None:
                raise ValueError(f"{me.id}: {tuple(ch)} is not on his menu")
            st, beat, margins, end = exchange(inp, st, me, ch, rng, abridged, pick.frame)
            assert rng.count - c0 == DRAWS_PER_EXCHANGE(G), rng.count - c0
            beats.append(beat)
            if margins:
                last_m = margins
            rests += ch.move == "rest"
            if end:
                ended, ended_by = end, me.id
                break
        if ended is None and rests == len(able):
            ended = "rested"
    ended = ended or "budget"
    st = replace(st, ended=ended)
    verdicts, ruled = _close(inp, st, rng, last_m, rulings or {})
    return Outcome(tuple(beats), st, ended, ended_by, verdicts, ruled)


def _close(inp, st, rng, last_m, rulings):
    """ONE close. A drawn decider's verdict is his own draw with his own track as leverage. Under `consent` nobody
    adjudicates: the outcome is whether a party accepted (his act). The abridged verdict is the speech's margin with
    the one addressed. A played adjudicator rules; how far he departs from his own track is returned."""
    r = inp.rite
    T = _d(st.tracks)
    ds = sorted((p for p in inp.room if p.decides), key=lambda p: (-p.precedence, p.id))
    if r.close == "consent":
        return (), ()
    if r.close == "exchange":
        m = _d(last_m)[ds[0].id]
        return ((ds[0].id, Margin(net=m.net + ds[0].start, ob=m.ob, terms=m.terms)),), ()
    out, ruled = [], []
    for d in ds:
        x = close_input(inp, T[d.id])
        ob, terms = obstacle(x)
        c0 = rng.count
        net = roll_net_continuous(x.pool, rng=rng) + net_boost(x.leverage, x.pool)
        assert rng.count - c0 == 1
        if d.id in rulings:                     # the draw is still taken (fixed count) and set aside
            a_ = (d.attunement - inp.dials["floor"]) / (inp.dials["ceiling"] - inp.dials["floor"])
            tl = tuple((p.id, round(a_ * max(0.0, -SIGN[p.side] * p.believes), 2), round(a_ * discomfort(st, p), 2))
                       for p in inp.room if p.side and p.id != d.id)
            how = rulings[d.id](JudgeView(d.id, T[d.id], p_carried(inp, T[d.id]), tuple(st.points), tl))
            if how in ("for", "against"):
                net = ob + (2.0 if how == "for" else -2.0)
                ruled.append((d.id, round(max(0.0, -(1.0 if how == "for" else -1.0) * T[d.id]), 2)))
        out.append((d.id, Margin(net=net, ob=ob, terms=terms)))
    return tuple(out), tuple(ruled)


@dataclass(frozen=True)
class JudgeView:
    """what a played adjudicator has at the close: his OWN mind (he knows it), and the points as they stood. He
    rules at the close only; he asks nothing during the sitting (D7, decided by the ladder)."""
    id: str
    track: float
    odds: float
    points: tuple
    tells: tuple = ()              # ((participant, perceived insincerity, perceived discomfort), ...) by his Attunement
