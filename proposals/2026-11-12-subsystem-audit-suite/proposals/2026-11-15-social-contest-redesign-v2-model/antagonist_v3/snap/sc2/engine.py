"""sc2.engine -- the v2 proceeding MODULE, reconciled (2026-11-15, after the two antagonists and A-136..A-140).

World-free: reads only `inp`. Keeps no state. Returns margins and a record; grades nothing; writes nothing.
Compares no rite id, move id or person id: it reads cells. Draw discipline: every exchange takes exactly 2G+8
normals [reading acc, G fit blurs, G aim blurs, strain, mood, their point, own point, intent, hold, speech], each
believed number its own; every drawn decider exactly one. Asserted.
"""
from __future__ import annotations

import math
from dataclasses import dataclass, replace
from typing import Callable, Mapping, Optional

import scmodel  # noqa: F401
from scmodel.dice import (MU_PER_DIE, SD_PER_DIE, Margin, SocialContestInput, even_line, level, net_boost, obstacle,
                          opposed_ob, pool_of, roll_net_continuous, weighted_tenth)

SIGN = {"for": 1.0, "against": -1.0}
CHANNEL = {"consequence": 0, "authority": 1, "solidarity": 2}      # want, hold, bond; `evidence` reads the item


@dataclass(frozen=True)
class Item:
    id: str
    kind: str
    weight: float
    source: Optional[str] = None
    about: Optional[str] = None
    sincere: bool = True           # False: its holder knows it false (a lie's claim, a forgery)


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
    stakes: float = 0.0
    quorum: Optional[int] = None
    unrest: float = 0.0
    bears: str = "for"


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
    pressed: bool = False
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
    frame: Optional[str] = None    # what of the listener's the speech is framed on (chosen from his believed reading)


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
    visible: tuple
    mood: float
    odds: float                    # believed P(carried) as he reads the room; an ordinary bench assumed
    intent: float                  # believed stake of the man opposite, -1..1 toward `for`
    turns_left: int
    acc: float


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
    evaded: bool
    insincere: float
    rattled: Optional[str]
    frame: Optional[str]           # Attunement: what it was framed on
    relevance: float               # Reason: how to the point its content was
    heard: float                   # Presence: the share of him the room listened to
    esteem: float                  # Grace: his standing in the room as he spoke
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
        """One invariant (A-139): a sitting has at least two distinct characters. The rest are structural: a
        cohort has weight; a drawn close has someone whose verdict is drawn; somebody speaks."""
        if len({p.id for p in self.room}) < 2:
            raise ValueError("a sitting with one character is refused (A-139)")
        if any(p.weight <= 0 for p in self.room):
            raise ValueError("a person or cohort of no weight")
        if self.rite.close != "consent" and not any(p.decides for p in self.room):
            raise ValueError(f"close `{self.rite.close}` with nobody to adjudicate")
        if not any(p.side for p in self.room):
            raise ValueError("nobody speaks")
        if self.state is not None and self.state.ended == "yielded":
            raise ValueError("a sitting that ended `yielded` is not resumed (an adjourned one is)")


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


def _hearers(inp, voice: Present, side):
    """whose track a speech moves: everyone not on the speaking side."""
    return [p for p in inp.room if p.id != voice.id and p.side != side]


def _crowd(inp):
    w = sum(p.weight for p in inp.room if p.side is None)          # how many are listening, by head
    return min(1.0, w / inp.dials["crowd_at"])


def mood(inp, st, viewer: Optional[Present] = None):
    T = _d(st.tracks)
    hs = [p for p in inp.room if p.side is None]
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
    those who decide: 0..2, 1 at the middle of the scale. It scales what in a speech depends on being to the point:
    how far the matter's bearing on the listener is brought home, and the worth of an answer."""
    return 1.0 if not D["relevance"] else 2.0 * (v.reason - D["floor"]) / (D["ceiling"] - D["floor"])


def landing(h, side, channel, tag, rel=1.0):
    """how a speech FRAMED on `tag` lands with this listener, on his TRUE interior: he must hold the tag (its weight)
    and the matter must bear on it his way; a frame on something he does not hold misses and misfits."""
    for c, t, w, bear in h.holds:
        if c == channel and t == tag:
            return max(-1.0, min(1.0, rel * SIGN[side] * w * bear + 0.5 * (2.0 * w - 1.0)))
    return -0.5


def fit(h, voice, side, ground, it, tag=None, rel=1.0):
    """the ground against how the MATTER (or the item, or the speaker) bears on this listener: -1..1."""
    if ground == "evidence":
        return credit(h, it) if it else -1.0
    if ground == "solidarity":
        return max(-1.0, min(1.0, _bond(h, voice.id) + 0.5 * (2.0 * h.care[2] - 1.0)))
    c = CHANNEL[ground]
    if tag is not None:
        return landing(h, side, c, tag, rel)
    return max(-1.0, min(1.0, rel * SIGN[side] * h.stake[c] + 0.5 * (2.0 * h.care[c] - 1.0)))


def frame(inp, hs, side, ground, acc=1.0, xa=0.0, xb=0.0):
    """ATTUNEMENT (A-142): the frame he picks for a ground, from what he BELIEVES these listeners hold: each tag's
    weight as he reads it (true, blurred by his accuracy), the body's weighted mean. A body has one frame."""
    if ground not in CHANNEL:
        return None
    c = CHANNEL[ground]
    tags = [t for ch, t in inp.frames if ch == c]
    if not tags:
        return None
    W = sum(h.weight for h in hs) or 1.0
    best, bv = None, -1e9
    for k, t in enumerate(tags):
        noise = xa * math.cos(1.7 * k) + xb * math.sin(1.7 * k)          # his own two normals, mixed per tag
        v = sum(h.weight * landing(h, side, c, t) for h in hs) / W + (1.0 - acc) * 0.5 * inp.dials["read_blur"] * noise
        if v > bv:
            best, bv = t, v
    return best


def aim(t, ground, it):
    if ground == "evidence":
        if not it:
            return -1.0
        return max(-1.0, min(1.0, it.weight * (1.0 if it.about == t.id else max(0.0, _bond(t, it.about))) * 2.0 - 1.0))
    return 2.0 * t.care[CHANNEL[ground]] - 1.0


def insincerity(voice, side, ground, it):
    """sincerity is agreement between what he says and what he KNOWS and holds."""
    x = max(0.0, -SIGN[side] * voice.believes)
    if it is not None and not it.sincere:
        x = 1.0
    if ground in CHANNEL:
        x = max(x, -SIGN[side] * voice.stake[CHANNEL[ground]])
    return max(0.0, min(1.0, x))


def _cg(inp, g):
    return {a: b for a, b, _ in inp.grounds}[g]


def _era(inp, g):
    return {a: w for a, _, w in inp.grounds}[g]


def validation(h, inp):
    """ADJUDICATOR'S REASON (A-144): how well he can dissect a speech and tell whether it is coherent, sound and
    good: 0 (he cannot tell; he goes by manner and standing) .. 1. The able and the involved validate; a crowd less."""
    return elab(h, inp)


def swayed(h, D):
    """ADJUDICATOR'S FOCUS (A-144), the other half of `wF`: how far what proves nothing about the merits (a rattle's
    theatre, a failed attack's embarrassment) sways him: 2 at the floor, 1 at the middle, 0 at the top."""
    return 2.0 - _wF(h, D)


def awe(inp, v):
    """ADJUDICATOR'S PRESENCE AND STATION (A-144): how far those who decide intimidate this participant: their
    Presence and their station over his, less his own Will. It acts on HIM, on his confidence and composure: he
    tires sooner (his staying power is less by it) and is easier to rattle (a press on him meets less). It is NOT an
    obstacle on his speeches: a cowed man's speech does not move the room toward the other side."""
    D = inp.dials
    ds = [d for d in inp.room if d.decides and d.id != v.id]
    if not ds:
        return 0.0
    W = sum(d.weight for d in ds)
    return D["awe_step"] * sum(d.weight * max(0.0, (d.presence - D["mid"]) / 3.0 + (d.power - v.power) / D["power_scale"]
                                              - (v.will - D["mid"]) / 3.0) for d in ds) / W


def tell(inp, st, voice, insinc):
    """what an attuned adjudicator perceives of a participant (A-144): his insincerity and his discomfort."""
    c = _d(st.cond)[voice.id]
    return min(1.0, insinc + inp.dials["comfort_step"] * min(1.0, c.strain + 0.5 * c.rattles))


def heard(inp, v):
    """Presence: the share of him that is listened to; a quiet room hears everyone."""
    D = inp.dials
    need = 1.0 + (D["ceiling"] - 1.0) * _crowd(inp)
    return max(D["heard_floor"], 1.0 - D["heard_step"] * max(0.0, need - v.presence))


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
    return (D["press_pull"] if c.pressed else 0.0) + D["rattle_pull"] * c.rattles + inp.rite.unrest \
        + D["heckle"] * max(0.0, heat(inp, st, v))


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
    """whose circumstances he must account for: the other side's lead, else the weightiest of those who decide."""
    o = _lead(inp, _other(mover.side))
    if o:
        return o
    ds = [p for p in inp.room if p.decides]
    return max(ds, key=lambda p: p.power) if ds else None


# ------------------------------------------------------------------ the one speech composer
def speech(inp, st, mover, voice, h, ground, it, relation, *, press_on=None, abridged=False, tag=None):
    D, r = inp.dials, inp.rite
    c = _d(st.cond)[voice.id]
    pool = case_pool(inp, voice, ground)
    foe = _foe(inp, mover)
    ops = [("weary", weary(inp, voice, c), 1.0), ("standing", standing_gap(inp, voice, foe) if foe else 0.0, 1.0)]
    if press_on is not None:
        T = press_on
        ct = _d(st.cond)[T.id]
        sig = level(D["fit_level"]) * _era(inp, ground) * aim(T, ground, it) + D["room_level"] * heat(inp, st, T) \
            + D["esteem_step"] * esteem(inp, st, voice)
        ops.append(("press", D["press_ob"], 1.0))
        opp = max(0.0, T.will + T.rank - (ct.strain + awe(inp, T)) / MU_PER_DIE)
        return pool, sig, SocialContestInput(pool, opp, sig, 0.0, tuple(ops), D["pool_default"], D["pool_add"],
                                             D["opposition_rate"], None, False)
    v = validation(h, inp)
    rl = 1.0 + 2.0 * v * (relevance(voice, D) - 1.0)        # how sound the speech is, as far as HE can validate it
    f = fit(h, voice, mover.side, ground, it, tag, rl) - D["repeat_step"] * _uses(st, mover.side, it.id if it else ground)
    sig = level(D["fit_level"]) * _era(inp, ground) * f \
        + D["esteem_step"] * esteem(inp, st, voice) * 2.0 * (1.0 - v) \
        + (rl * level(D["answer_level"]) if relation == "answers" else 0.0)
    return pool, sig, SocialContestInput(pool, h.will + h.rank, sig, (r.difficulty + r.stakes) if abridged else 0.0,
                                         tuple(ops), D["pool_default"], D["pool_add"], D["opposition_rate"], None, False)


def _phi(z):
    return 0.5 * (1.0 + math.erf(z / math.sqrt(2.0)))


def _epos(mu, sd):
    z = mu / sd
    return mu * _phi(z) + sd * math.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi)


def close_input(inp, track):
    D, r = inp.dials, inp.rite
    pool = pool_of(D["mid"], 0, D["pool_add"], D["pool_floor"])
    return SocialContestInput(pool, D["mid"], D["track_step"] * track, r.difficulty, (("stakes", r.stakes, 1.0),),
                              D["pool_default"], D["pool_add"], D["opposition_rate"], None, False)


def p_carried(inp, track):
    x = close_input(inp, track)
    ob, _ = obstacle(x)
    mu = MU_PER_DIE * x.pool + net_boost(x.leverage, x.pool) - ob
    return 1 - _phi((1.0 - mu) / (SD_PER_DIE * math.sqrt(x.pool)))


def believed_odds(inp, mood_seen):
    """what a chooser may be shown: the close as the room SEEMS to stand to him (his believed mood), an ordinary
    bench assumed (B05.62). No true attribute and no true start enters it. Under consent there are no odds."""
    if inp.rite.close == "consent":
        return 0.0
    return p_carried(inp, mood_seen * inp.dials["mood_scale"])


# ------------------------------------------------------------------ the view
def _legal(inp, mover, turns_left):
    return ("rest",) if turns_left <= 0 else _d(inp.rite.moves).get(mover.side, ())


def _reply(inp, side):
    return _d(inp.rite.reply).get(side, "may")


def menu(inp, st, mover, turns_left, frames=None):
    """The TRUE expected worth of every option on his menu, from the engine's own values: [(move, ground, item,
    relation, ev, p)]. No draw. Nobody is shown this: a View shows `perceived` of it."""
    D = inp.dials
    G = [g for g, _, _ in inp.grounds]
    c = _d(st.cond)[mover.id]
    hs = [p for p in inp.room if p.decides and p.side != mover.side] or _hearers(inp, mover, mover.side)
    W = sum(h.weight for h in hs) or 1.0
    mean = lambda f: sum(h.weight * f(h) for h in hs) / W
    other_side = _other(mover.side)
    tid = _d(st.last_voice).get(other_side)
    T = _who(inp, tid) if tid else _lead(inp, other_side)
    items = _items(inp, mover)
    est, wry = esteem(inp, st, mover), weary(inp, mover, c)
    foe = _foe(inp, mover)
    gap = standing_gap(inp, mover, foe) if foe else 0.0
    pull = _pull(inp, st, mover, c)
    Pf = pool_of(mover.focus, 0, D["pool_add"], D["pool_floor"])
    e_drift = _epos(pull - MU_PER_DIE * mover.focus, SD_PER_DIE * math.sqrt(Pf)) if pull > 0 else 0.0
    rep_ = _reply(inp, mover.side)
    lt = _d(st.live).get(other_side)
    P = next((p for p in st.points if p.id == lt), None)
    S = _stands(P) / max(1, len(P.held)) if P else 0.0
    stands = S > 0
    m_true = SIGN[mover.side] * mood(inp, st, mover)
    cands = [(g, None) for g in G if g != "evidence"] + [("evidence", it) for it in items]
    if frames is None:                                   # with no reading given: the frames a perfect reader would pick
        frames = {g: frame(inp, hs, mover.side, g) for g in G}
    out = []
    for mid in _legal(inp, mover, turns_left):
        row = MOVES[mid]
        if row.effect == "track":
            for g, it in cands:
                pool = case_pool(inp, mover, g)
                ins = insincerity(mover, mover.side, g, it)
                sd = SD_PER_DIE * math.sqrt(pool)
                for rel in (["answers"] if (rep_ != "raise" and P is not None) else []) + ["raises"]:
                    def mu_h(h, rel=rel):
                        x = speech(inp, st, mover, mover, h, g, it, rel, abridged=inp.rite.close == "exchange", tag=frames.get(g))[2]
                        ob, _ = obstacle(x)
                        return MU_PER_DIE * pool + net_boost(x.leverage, pool) - ob - D["off_step"] * _wF(h, D) * e_drift \
                            - D["ploy_step"] * _wA(h, D) * tell(inp, st, mover, ins)
                    mu = mean(mu_h)
                    if rel == "answers":
                        ev = min(max(S, 0.0), mu) if mu > 0 else mu
                    else:
                        ev = mu - (D["off_step"] * D["evade"] * mean(lambda h: _wF(h, D)) if (rep_ == "must" and stands) else 0.0)
                    out.append((mid, g, it.id if it else None, rel, ev, 1 - _phi(-mu / sd), frames.get(g)))
        elif row.effect == "strike" and T is not None:
            ct = _d(st.cond)[T.id]
            for g, it in cands:
                pool, sig, x = speech(inp, st, mover, mover, T, g, it, "presses", press_on=T)
                ob, _ = obstacle(x)
                mu = MU_PER_DIE * pool + net_boost(sig, pool) - ob
                p = 1 - _phi(-mu / (SD_PER_DIE * math.sqrt(pool)))
                gain = D["rattle_gain"] * (1.0 - D["reactance"] * ct.rattles)
                lasting = (D["esteem_step"] * 2.0 * D["show"] + D["weary_step"] * 0.5) * max(0, turns_left - 1) \
                    + D["off_step"] * 0.6 * (D["press_pull"] + D["rattle_pull"])
                ins = 1.0 if (it is not None and not it.sincere) else 0.0
                ev = p * (gain + lasting) - (1 - p) * D["rebound"] - D["off_step"] * e_drift - D["ploy_step"] * ins \
                    - (D["off_step"] * D["evade"] if (rep_ == "must" and stands) else 0.0)
                out.append((mid, g, it.id if it else None, "presses", ev, p, None))
        elif row.effect == "yield":
            own = _d(st.tracks).get(mover.id, 0.0)
            last = st.issue >= len(inp.rite.issues) - 1
            if inp.rite.concede == "accepts" or last:
                ev = (-SIGN[mover.side] * own - D["consent_at"]) if (inp.rite.close == "consent" or mover.decides) \
                    else (-m_true * D["mood_scale"] - D["yield_track"])
            else:
                ev = (-m_true * D["mood_scale"] - D["concede_step"] * (1.0 + max(abs(x) for x in mover.stake))) if turns_left > 1 else -9.0
            out.append((mid, None, None, "concedes", ev, None, None))
        else:
            out.append((mid, None, None, "rests", -D["off_step"] * D["evade"] if (rep_ == "must" and stands) else 0.0, None, None))
    return out, T, P, S


def perceived(true_worth, acc, x, lean, D):
    """ATTUNEMENT (A-141): the one gauge. What a contestant takes an option to be worth is its true worth plus an
    error that shrinks as his reading sharpens: his own noise `x`, and his stable bias `lean` (an optimist
    overrates acting, a pessimist underrates it). At acc 1 perceived is true."""
    return true_worth + (1.0 - acc) * (D["read_blur"] * x + D["bias_step"] * lean)


def build_view(inp, st, mover, rng, turns_left) -> View:
    """2G+6 normals, each perceived number its own: accuracy; one per ground for what arguing on it is worth; one
    per ground for what pressing on it is worth; conceding; the mood; their point; his own point; the other's intent."""
    D = inp.dials
    G = [g for g, _, _ in inp.grounds]
    c = _d(st.cond)[mover.id]
    # his accuracy is his Attunement, with a little luck: 0.5 at the middle of the scale; nothing opposes it
    acc = (1.0 + math.tanh((MU_PER_DIE * (mover.attunement - D["mid"]) + D["read_noise"] * rng.normal()) / D["read_scale"])) / 2.0
    xarg = dict(zip(G, (rng.normal() for _ in G)))
    xprs = dict(zip(G, (rng.normal() for _ in G)))
    xc, xm, xt, xo, xi = (rng.normal() for _ in range(5))
    hs = [p for p in inp.room if p.decides and p.side != mover.side] or _hearers(inp, mover, mover.side)
    frames = {g: frame(inp, hs, mover.side, g, acc, xarg[g], xprs[g]) for g in G}     # framed from his believed reading
    true, T, P, S = menu(inp, st, mover, turns_left, frames)
    opts = []
    for mv, g, it, rel, ev, p, fr in true:
        acting = MOVES[mv].draw
        x = xarg[g] if mv == "argue" else xprs[g] if mv == "press" else xc if mv == "concede" else 0.0
        pe = perceived(ev, acc, x, mover.bias if acting else 0.0, D) if (acting or mv == "concede") else ev
        pp = None if p is None else max(0.0, min(1.0, perceived(p, acc, 0.1 * x, 0.1 * mover.bias, D)))
        opts.append(Option(mv, g, it, rel, round(pe, 2), None if pp is None else round(pp, 2), fr))
    m_seen = max(-1.0, min(1.0, perceived(SIGN[mover.side] * mood(inp, st, mover), acc, 0.25 * xm, 0.0, D)))
    intent = max(-1.0, min(1.0, perceived(sum(T.stake) / 3.0 if T else 0.0, acc, 0.25 * xi, 0.0, D)))
    lo = _d(st.live).get(mover.side)
    Po = next((p for p in st.points if p.id == lo), None)
    live_theirs = (P.id, P.ground, P.item, round(perceived(S, acc, 0.5 * xt, 0.0, D), 1)) if P else None
    live_own = (Po.id, Po.ground, Po.item, round(perceived(_stands(Po) / max(1, len(Po.held)), acc, 0.5 * xo, 0.0, D), 1)) if Po else None
    vis = tuple((p.id, _d(st.cond)[p.id].rattles) for p in inp.room if p.side)
    return View(st.n, mover.id, mover.side, inp.rite.issues[st.issue], live_theirs, live_own, tuple(opts), c,
                round(esteem(inp, st, mover), 2), round(weary(inp, mover, c), 2), round(awe(inp, mover), 2), vis, m_seen, believed_odds(inp, m_seen),
                intent, turns_left, acc)


# ------------------------------------------------------------------ the automatic policy (A-136)
def temper(view: View, me: Present, D) -> float:
    """0 composed .. 1 lost: how far he is rattled past what his Will and Grace carry."""
    return max(0.0, min(1.0, D["temper_step"] * view.own.rattles + (2.0 * D["mid"] - me.will - me.grace) / 6.0))


def auto(view: View, me: Present, D) -> Choice:
    """While he keeps his temper he takes the option his own reading says is worth most. As his temper goes, the
    man shows: he argues from what he himself holds, the proud press and will not give way, the timid give way,
    the orator plays to the room, a grudge goes after its object."""
    t = temper(view, me, D)
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
    hold = roll_net_continuous(pool_of(voice.focus, 0, D["pool_add"], D["pool_floor"]), rng=rng) - even_line(D["pool_add"])
    drift = max(0.0, pull - hold) if pull > 0 else 0.0
    z = rng.normal()
    tracks, live, points, used = _d(st.tracks), _d(st.live), list(st.points), _d(st.used)
    hearers = _hearers(inp, voice, side)
    judges = [h for h in hearers if h.decides] or hearers
    lt = live.get(other)
    rep = _reply(inp, side)
    stands = False
    if lt is not None:
        stands = _stands(next(p for p in points if p.id == lt)) > 0
    relation = ch.relation or {"track": "raises", "strike": "presses", "yield": "concedes", "none": "rests"}[row.effect]
    if relation == "answers" and lt is None:
        relation = "raises"
    evaded = bool(rep == "must" and stands and relation != "answers" and row.effect != "yield")
    off = drift + (D["evade"] if evaded else 0.0)
    moved, margins, margin, rattled, target, closed, pid, insinc, terms, ended = [], [], 0.0, None, None, None, None, 0.0, (), None
    issue = r.issues[st.issue]

    def move(h, d):
        moved.append((h.id, d)); tracks[h.id] += d

    if row.effect == "track":
        insinc = insincerity(voice, side, ch.ground, it)
        held, tot, W = {}, 0.0, 0.0
        for h in hearers:
            pool, sig, x = speech(inp, st, mover, voice, h, ch.ground, it, relation, abridged=abridged, tag=tag)
            ob, terms = obstacle(x)
            m = MU_PER_DIE * pool + SD_PER_DIE * math.sqrt(pool) * z + net_boost(sig, pool) - ob \
                - D["off_step"] * _wF(h, D) * off - D["ploy_step"] * _wA(h, D) * tell(inp, st, voice, insinc)
            if h in judges:
                tot += h.weight * m; W += h.weight
            margins.append((h.id, Margin(net=m + ob, ob=ob, terms=terms)))
            d = sg * m
            if relation == "answers":
                P = next(p for p in points if p.id == lt)
                s = SIGN[other] * _d(P.held).get(h.id, 0.0)
                d = sg * (min(max(s, 0.0), m) if m > 0 else m)
                points[points.index(P)] = replace(P, held=_put(P.held, h.id, _d(P.held).get(h.id, 0.0) + d))
            else:
                held[h.id] = d
            move(h, d)
        margin = tot / W if W else 0.0
        if relation == "answers":
            pid = lt
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
        pool, sig, x = speech(inp, st, mover, voice, T, ch.ground, it, relation, press_on=T)
        ob, terms = obstacle(x)
        margin = MU_PER_DIE * pool + SD_PER_DIE * math.sqrt(pool) * z + net_boost(sig, pool) - ob
        ct = cond[T.id]
        if margin >= 0:
            rattled = T.id
            gain = D["rattle_gain"] * (1.0 - D["reactance"] * ct.rattles)
            cond[T.id] = replace(ct, rattles=ct.rattles + 1, strain=0.0, pressed=True, spent=ct.spent + 1.0)
        else:
            gain = -D["rebound"]
            cond[T.id] = replace(ct, strain=ct.strain + D["wear"])
        for h in hearers:
            move(h, sg * (gain * swayed(h, D) * (1.0 - max(0.0, _bond(h, T.id))) - D["off_step"] * _wF(h, D) * off
                          - D["ploy_step"] * _wA(h, D) * insinc))
        pid = lt
    elif row.effect == "yield":
        last = st.issue >= len(r.issues) - 1
        closed = issue
        if r.concede == "accepts" or last:
            ended = "yielded"                           # he gives up the matter: the room goes to the other side,
            for h in hearers + ([mover] if mover.decides else []):      # and so does he, if it is his to decide
                move(h, -sg * D["yield_track"] - tracks[h.id])
        else:
            cost = D["concede_step"] * (1.0 + max(abs(x) for x in mover.stake))
            for h in hearers:
                move(h, (h.start - sg * cost) - tracks[h.id])
            live = {"for": None, "against": None}
            used = {k: v for k, v in used.items() if k[0] != side}
    elif evaded:                                        # silence under a charge is turning away
        for h in hearers:
            move(h, -sg * D["off_step"] * D["evade"] * _wF(h, D))
    cv2 = cond[voice.id]
    cond[voice.id] = replace(cv2, pressed=False if row.draw else cv2.pressed, spoken=cv2.spoken + 1,
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
                round(margin, 3), round(drift, 3), evaded, round(insinc, 3), rattled, tag if row.effect == "track" else None,
                round(relevance(voice, D), 2), round(heard(inp, voice), 2), round(esteem(inp, st, voice), 2), tuple(moved), closed,
                round(mood(inp, new), 3), terms)
    return new, beat, margins, ended


# ------------------------------------------------------------------ the sitting
def order(inp):
    sp = [p for p in inp.room if p.side and _d(inp.rite.moves).get(p.side)]
    return sorted(sp, key=lambda p: (0 if p.side == inp.rite.bears else 1, -p.precedence, p.id))


def proceed(inp: Input, rng, decide: Optional[Callable] = None, deciders: Optional[Mapping] = None,
            rulings: Optional[Mapping] = None) -> Outcome:
    """`deciders[person]` (or `decide`) chooses for a speaker; `rulings[person]` rules for a played adjudicator.
    A resumed sitting (`inp.state`) continues: each speaker has the rite's turns less what he has already spoken."""
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
            assert rng.count - c0 == 2 * G + 8, rng.count - c0
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
            tl = tuple((p.id, round(a_ * tell(inp, st, p, max(0.0, -SIGN[p.side] * p.believes)), 2)) for p in inp.room if p.side and p.id != d.id)
            how = rulings[d.id](JudgeView(d.id, T[d.id], p_carried(inp, T[d.id]), tuple(st.points), tl))
            if how in ("for", "against"):
                net = ob + (2.0 if how == "for" else -2.0)
                ruled.append((d.id, round(max(0.0, -(1.0 if how == "for" else -1.0) * T[d.id]), 2)))
        out.append((d.id, Margin(net=net, ob=ob, terms=terms)))
    return tuple(out), tuple(ruled)


@dataclass(frozen=True)
class JudgeView:
    """what a played adjudicator has at the close: his OWN mind (he knows it), and the points as they stood."""
    id: str
    track: float
    odds: float
    points: tuple
    tells: tuple = ()              # ((participant, what he perceives of his discomfort and insincerity), ...) by his Attunement
