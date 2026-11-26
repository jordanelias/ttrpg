"""THE PROCEEDING'S EXCHANGE (B24p.07; V2 p2 §C, §E): the view a chooser is shown, one speech, one margin per listener.

A MODULE (A-25): it reads the typed `Input` and a keyed `Draw`, returns values, keeps no state, writes nothing and reads no `World`.
It imports the dice engine, `fmath`, the record leaf (`engine/season/queries/inputs.py`), `.roll` and `.evidence`, nothing else. EVERY BRANCH READS A
CELL: a rite's (`Rite.*`), a move's `effect` and `draw`, a ground's `reads`; no rite, move, ground or person id is compared.

THE HOST HANDS THE TWO ROSTERS IN, `Input.dials` BEING THE ONE MAPPING THE RECORD HAS FOR THEM (a module holds no data, `FieldworkInput.terms`'s
precedent): `dials["moves"]` is `{move id: (effect, draw)}` (`rosters.yaml: proceeding_moves`) and `dials["reads"]` is `{ground id: reads}`
(`rosters.yaml: grounds`, `reads` in `item | want | hold | bond`). `want | hold | bond` are also the channel names of `Present.holds` and
`Input.frames`, and the order of `Present.care` and `.stake`. [ASSUMPTION: `proceeding_dials` does not name them (B24p.04 landed 61 names); B24p.13's
builder adds the two keys -- basis: the record has no field for a roster and this item may not edit it.]
`dials["fault_levels"]` is `{fault id: levels}` (`rosters.yaml: proceeding_faults.levels`): what a recorded fault costs the side at fault on the closing draw, in `fault_step` levels; `proceeding_dials` carries it.

DRAWS: every exchange takes `DRAWS_PER_EXCHANGE(G)` normals however it goes, in this order: `view` takes all but the last two, `exchange`
takes the hold and then the speech. `exchange` asserts its two and, given `mark` (`rng.n` before the view), the whole count; the sitting
(B24p.11's `proceed`) passes it.

THE SITTING (B24p.11; V2 p2 §C.1, §C.5, §F): `proceed` runs rounds of exchanges: each round, every speaker with a turn left and the fewest spoken
speaks once, the side that bears the live thing first and then by precedence (`_mover`); one callback per person (`deciders[id]`, else `decide`,
else the automatic policy: played and automatic meet in one sitting; an abridged act asks none). It ends `yielded` (a final concession), `rested`
(a whole round with nothing to say) or `budget` (every speaker's turns spent): the forum's time is the measure of readiness, no second rule reads
the deciders' state, and an end is never a verdict. Then the close.

THE CLOSE (B24p.12; V2 p2 §D): `_close` is each adjudicator's own draw on his own track (a `Margin`, never a band or a side), or under `consent` a
party's accept (an act, nothing drawn), or under `exchange` the one speech's margin with the one addressed; `p_carried`, `view_odds` and
`card_odds` are its closed form, the chooser's believed odds and the card's. The host reads the verdicts (B24p.13).

THE BOARD (B24.06; HEAR_B): `Sitting.board` holds the `Item`s entered (`exhibit`), the band drawn against each (`answer`: filed on the item, never decided here), halved
or turned on (`impugn`); which of them count, at what weight, and what the sitting owes for them is `evidence.standing`'s alone (B24.19), re-read at every change.
`Sitting.faults`/`.levels` hold what the sitting owes. A `rule` or an `adjourn` is the bench's. The board reaches the close as LEVERAGE ONLY (`_lever`: one
`proof_level` per whole unit of net standing weight, `fault_step` levels per level owed): nothing favourable lowers an obstacle (A-25), and a fault is
a cost on the draw, never a verdict. THE MATTER'S FILED EXHIBITS (`Input.exhibits`, B24.20) count with the board's standing items on that leverage (`_counted`) and are never
on the board; an abridged speech, which is its own close, carries the same leverage toward its speaker. With no item on the board and none filed the close is what it was.
"""
from __future__ import annotations

import math
from dataclasses import replace
from typing import Callable, Mapping, Optional

from engine.dice_engine import dice_engine, fmath
from engine.dice_engine.sigma_leverage import (M_MAX, MU_PER_DIE, SD_PER_DIE, band_odds, even_line, level, net_boost, pool_of,
                                               phi, roll_net_continuous, weighted_tenth)
from engine.season.queries.inputs import (SIDE_SIGN, Beat, Choice, Cond, Input, JudgeView, Margin, Option, Outcome, Point, Sitting,
                                          SocialContestInput, View, other_side as _other)
from .evidence import CONTRADICTS, FAILURE, band_of, newly_owed, pair_of, standing
from .roll import obstacle, standing_levels


def DRAWS_PER_EXCHANGE(G: int) -> int:
    """THE ONE STATEMENT OF THE EXCHANGE'S DRAW COUNT, in normals, for `G` grounds; every move takes it, `rest` and `concede` included.
    In order: his accuracy; the worth of arguing on each ground, then of pressing on each; conceding, the mood, their point, his own
    point, the other's intent, his esteem, resting, his awe; then, per ground, two for the frame and two for the press's object; then the
    hold and the speech."""
    return 6 * G + 11   # [canonical: V2 p2 §C.2 -- 6G + 11 normals an exchange]


# ------------------------------------------------------------------ small readers
def _d(t) -> dict:
    return dict(t)


def _put(t, k, v) -> tuple:
    d = dict(t)
    d[k] = v
    return tuple(d.items())


def _sg(side) -> float:
    return SIDE_SIGN.get(side, -1.0)   # a side that is not `for` reads as `against`, as the flip does


def _clip(x, lo=-1.0, hi=1.0) -> float:
    return max(lo, min(hi, x))


def _wsum(xs) -> float:
    return fmath.ltr_sum(xs)


def _sd(pool) -> float:
    return SD_PER_DIE * math.sqrt(max(0.0, pool))


def _epos(mu, sd) -> float:
    """E[max(0, X)] for X ~ Normal(mu, sd)."""
    if sd <= 0:
        return max(0.0, mu)
    z = mu / sd
    return mu * phi(z) + sd * fmath.exp(-0.5 * z * z) / math.sqrt(2.0 * math.pi)   # [canonical: V2 p2 §E -- the menu's expected gain, a normal's positive part]


def _p_up(mu, sd) -> float:
    return (1.0 if mu > 0 else 0.0) if sd <= 0 else 1 - phi(-mu / sd)


def _z(rng) -> float:
    return rng.normal(0.0, 1.0)


class _Taken:
    """A normal already drawn, handed to the one sampler (`roll_net_continuous`) so the draw is taken whatever the pool: the sampler draws
    nothing for an empty pool and the exchange's count must not vary."""
    __slots__ = ("z",)

    def __init__(self, z):
        self.z = z

    def normal(self, mu, sigma):
        return mu + sigma * self.z


def _roll(pool, z) -> float:
    return roll_net_continuous(pool, rng=_Taken(z))


def _need(inp, key):
    if key not in inp.dials:
        raise ValueError(f"refused[dials]: `dials[{key!r}]` -- the host hands the roster in (see proceeding.py's head)")
    return inp.dials[key]


def _move(inp, mid) -> tuple:
    rows = _need(inp, "moves")
    if mid not in rows:
        raise ValueError(f"refused[move]: {mid!r} is not a move row the host handed in")
    return rows[mid]


def _reads(inp, ground) -> str:
    return _need(inp, "reads")[ground]


def _ix(reads) -> int:
    return ("want", "hold", "bond").index(reads)


def _bond(p, other) -> float:
    return _d(p.bonds).get(other, 0.0) if other else 0.0


def who(inp, pid):
    return next(p for p in inp.room if p.id == pid)


def lead(inp, side):
    c = [p for p in inp.room if p.side == side]
    return max(c, key=lambda p: (p.precedence, p.id)) if c else None


def _stands(P) -> float:
    """how far a point stands with those who heard it."""
    return _sg(P.side) * _wsum(v for _, v in P.held)


def _point(st, pid):
    return next((p for p in st.points if p.id == pid), None) if pid is not None else None


def _reply(inp, side) -> str:
    return _d(inp.rite.reply).get(side, "may")


def _issue(inp, st) -> str:
    return inp.rite.issues[st.issue] if inp.rite.issues else inp.matter


def _ground(inp, g) -> tuple:
    return next((r, e) for a, r, e in inp.grounds if a == g)


def _weight(inp, st, g) -> float:
    """what a ground is worth here and now: the era's weight on it times the live rung's (stasis, A-134)."""
    return _ground(inp, g)[1] * _d(_d(inp.rite.weighs).get(_issue(inp, st), ())).get(g, 1.0)


def crowd(inp) -> float:
    return min(1.0, _wsum(p.weight for p in inp.room if p.side is None) / inp.dials["crowd_at"])


def _hearers(inp, voice, side) -> list:
    return [p for p in inp.room if p.id != voice.id and p.side != side]


def _deciders_for(inp, mover) -> list:
    """whom a speaker must move: those who decide and are not on his side, and himself if he decides (C2: a party who decides is moved by
    his own case as he hears it); with nobody deciding, everyone not on his side."""
    return [p for p in inp.room if p.decides and (p.side != mover.side or p.id == mover.id)] or _hearers(inp, mover, mover.side)


def _foe(inp, mover):
    """whose circumstances he must account for: the other side's lead; in an abridged act, the one he addresses; else nobody (no gap)."""
    o = lead(inp, _other(mover.side))
    if o is None and inp.rite.close == "exchange":
        o = next((p for p in inp.room if p.decides and not p.side and p.id != mover.id), None)
    return o


def _sole(inp, p) -> bool:
    return p.decides and not any(q.decides for q in inp.room if q.id != p.id)


def _items(inp, mover) -> list:
    return [it for it in mover.items if it.kind in inp.rite.admits]


def _find_item(inp, iid):
    return next((it for p in inp.room for it in p.items if it.id == iid), None)


def _voice(inp, mover, it):
    """a cited testimony whose source sits in the room with no side and no seat is spoken by its source (V2 p2 §A.1)."""
    if it is not None and it.kind == "testimony" and it.source and it.source != mover.id:
        for p in inp.room:
            if p.id == it.source and p.side is None and not p.decides:
                return p
    return mover


# ------------------------------------------------------------------ the board (B24.06; HEAR_B "The six moves", "Faults")
STANDS, ANSWERED, STRUCK, WITHDRAWN = "stands", "answered", "struck", "withdrawn"
#: an `Item`'s status on `Sitting.board`: an answered item stands (its answer failed or halved it); `struck` is what `evidence.standing` struck; `withdrawn` is
#: what the sitting itself refused at entry (two items of one side disagreeing, the lighter) and `standing` is never shown.


def _at(board, iid) -> Optional[int]:
    return next((k for k, (it, _) in enumerate(board) if it.id == iid), None)


def _ruled(inp, board, filed=()) -> tuple:
    """THE ONE EVIDENCE RULE ON THIS BOARD (B24.19): `evidence.standing` over the items shown, at the weight each was entered at. Nothing else here decides which
    item counts, at what weight, or what is struck or owed for it; a filed finding is the item's own `forged_found`, `evidence_cap` a dial. `filed` is the matter's filed
    exhibits (`_counted`), counted with the board's items in the same call."""
    shown = (*filed, *(it for it, s in board if s != WITHDRAWN))
    return standing(shown, tuple(it.id for it in shown if it.forged_found), inp.dials.get("evidence_cap"))


def _standing(inp, board, side=None) -> list:
    """the items that count, at the weight they now carry, of one side or of both."""
    return [it for it in _ruled(inp, board)[0] if side is None or it.side == side]


def _settle(inp, board) -> list:
    """the board with each item's status as the rule leaves it: struck, answered (an answering act has been drawn against it) or standing."""
    struck = set(_ruled(inp, board)[1])
    return [(it, s if s == WITHDRAWN else STRUCK if it.id in struck else ANSWERED if it.answered_band is not None else STANDS) for it, s in board]


def _on_rung(it, issue) -> bool:
    return it.rung is None or it.rung == issue


def _entry_weight(it, issue) -> float:
    """the weight `it` enters a sitting at: its own on the rung tried, half off it (the `irrelevance` fault counts it)."""
    return it.weight if _on_rung(it, issue) else it.weight / 2.0


def _hand(inp, st, mover) -> list:
    """his own admitted items not yet shown."""
    return [it for it in _items(inp, mover) if _at(st.board, it.id) is None]


def _answer_of(held, side, target):
    """the heaviest of `held`, of `side`, that the host filed as contradicting `target`, or `None`."""
    mine = [it for it in held if it.side == side and pair_of(target, it) == CONTRADICTS]
    return max(mine, key=lambda it: (it.weight, it.id)) if mine else None


def _answerable(inp, st, mover, effect) -> list:
    """`[(the item answered or impugned, his answer to it or None, over)]` over the other side's standing items: an `answer` needs an item of his own that
    clashes with the target, or the target's `forged_found` (a filed finding); an `impugn` needs an origin to impugn. `over` is the weight the target holds
    over its answer, the roll's added obstacle."""
    out, held = [], _standing(inp, st.board)
    for tg in (i for i in held if i.side == _other(mover.side)):
        if effect == "answer":
            ans = _answer_of(held, mover.side, tg)
            if ans is not None or tg.forged_found:
                out.append((tg, ans, max(0.0, tg.weight - (ans.weight if ans else 0.0))))
        elif tg.origin is not None:
            out.append((tg, None, 0.0))
    return out


def _track(inp, dial, n) -> float:
    """`n` levels of the `dial` (`proof_level`, `fault_step`) in TRACK units, read through the close's own slope (`track_step`); `0.0` where there is none."""
    D = inp.dials
    return n * _lv(D[dial]) / D["track_step"] if D["track_step"] else 0.0


def _worth(inp, w) -> float:
    """`w` of standing weight as the closing draw's leverage, read in TRACK units through the close's own slope (`track_step`): what the menu prices an
    exhibit at. [ASSUMPTION; Jordan to correct: this price is the menu's only -- the NPC decider's cost terms are B24.12's, which replaces it]"""
    return _track(inp, "proof_level", w)


def _cost(inp, n) -> float:
    """`n` levels owed, in track units, the same way (`fault_step`)."""
    return _track(inp, "fault_step", n)


def _counted(inp, board) -> tuple:
    """WHAT COUNTS ON THE CLOSE (B24's close, R1; B24.20): `evidence.standing` over the matter's filed exhibits (`Input.exhibits`) AND the board's items shown, in one call, so an item
    filed and shown again is one item (the same cell and origin corroborate once, the other side's same cell counts for neither) and one quantity has one rule. Never the board's
    own reading (`_ruled`): a filed exhibit is never entered, answered, struck or owed for in a sitting. With nothing filed it is `_ruled`'s standing, to the call."""
    return _ruled(inp, board, inp.exhibits)[0]


def _lever(inp, st) -> float:
    """THE BOARD ON THE CLOSING DRAW'S LEVERAGE CHANNEL (HEAR_B "How a sitting runs" 4; A-25): one `proof_level` per whole unit of the standing weight toward
    `for` (rounded half up) less one per whole unit toward `against` -- `roll.standing_levels`, the same counter the roll's own exhibits are read with (B24.21: the net was once truncated here, two ladders for one quantity) -- less `fault_step` levels per level owed against `for` (toward it, per level
    owed against `against`). The standing weight is the board's items and the matter's filed exhibits together (`_counted`; B24.20: the exhibits' `proofs` levels reach a sitting's
    close, as they reach the single roll). It reaches the leverage and never the obstacle: nothing favourable is subtracted. `0.0` for an empty board and an empty case file, whatever the settings."""
    D = inp.dials
    n_for, n_against = standing_levels(_counted(inp, st.board), "for")      # the roll's own counter (B24.21): one rounding for one quantity
    owed = _wsum(_sg(side) * n for side, n in st.levels)
    return _lv(D["proof_level"]) * (n_for - n_against) - _lv(D["fault_step"]) * owed


def mood(inp, st, viewer=None) -> float:
    """the room's lean toward `for`, -1..1: the weighted mean of the tracks that decide."""
    T = _d(st.tracks)
    hs = [p for p in inp.room if p.side is None] or [p for p in inp.room if p.decides]
    if not hs:
        o = lead(inp, _other(viewer.side)) if viewer else None
        hs = [o] if o else [p for p in inp.room if p.side]
    W = _wsum(p.weight * (1.0 + p.power) for p in hs)
    return _clip(_wsum(p.weight * (1.0 + p.power) * T.get(p.id, 0.0) for p in hs) / W / inp.dials["mood_scale"])


# ------------------------------------------------------------------ the six attributes' operands
def _wF(h, D) -> float:
    return (h.focus - D["attribute_floor"]) / (D["attribute_mid"] - D["attribute_floor"])


def _wA(h, D) -> float:
    return (h.attunement - D["attribute_floor"]) / (D["attribute_mid"] - D["attribute_floor"])


def validation(inp, h) -> float:
    """ADJUDICATOR'S REASON (A-144): how well he can dissect a speech and tell whether it is sound, 0..1. The able and the involved
    validate; a crowd less."""
    D = inp.dials
    return _clip(0.5 + D["sense_step"] * (h.reason - D["attribute_mid"])    # [canonical: V2 p2 §C.3 -- 0.5 at the middle of the scale]
                 + D["involve"] * max(abs(x) for x in h.stake) - D["crowd_lean"] * crowd(inp), 0.0, 1.0)


def relevance(inp, v) -> float:
    """REASON (A-143): how relevant the content of his speech is, 0..2, 1 at the middle of the scale."""
    D = inp.dials
    return 1.0 if not D["relevance"] else 2.0 * (v.reason - D["attribute_floor"]) / (D["attribute_ceiling"] - D["attribute_floor"])


def discern(inp, h, T) -> float:
    """ADJUDICATOR'S ATTUNEMENT on a rattle (A-144): the rattled man's discomfort read for what it is; 1 at the middle of the scale
    (B10: discomfort is never deducted as insincerity)."""
    D = inp.dials
    false = max(0.0, -_sg(T.side) * T.believes) if T.side else 0.0
    return max(0.0, 1.0 + D["comfort_step"] * (_wA(h, D) - 1.0) * (2.0 * false - 1.0))


def theatre(inp, h) -> float:
    """ADJUDICATOR'S FOCUS, its second half (A-140): how far a rattle's theatre reaches him; 2 at Focus 1, 1 at the middle, 0 at the top."""
    return max(0.0, 2.0 - _wF(h, inp.dials))


def awe(inp, v) -> float:
    """how far those who decide intimidate a participant: their Presence and station over his, less his own Will. It shortens his staying
    power and lowers what a press on him meets; it is never an obstacle on his speeches."""
    D = inp.dials
    ds = [d for d in inp.room if d.decides and d.id != v.id]
    if not ds:
        return 0.0
    mid = D["attribute_mid"]
    return D["awe_step"] * _wsum(d.weight * max(0.0, (d.presence - mid) / 3.0 + (d.power - v.power) / D["power_scale"]    # [canonical: V2 p2 §C.2 -- awe, three points of attribute a step]
                                                - (v.will - mid) / 3.0) for d in ds) / _wsum(d.weight for d in ds)


def _heard_abs(inp, presence) -> float:
    D = inp.dials
    need = 1.0 + (D["attribute_ceiling"] - 1.0) * crowd(inp)
    return max(D["heard_floor"], 1.0 - D["heard_step"] * max(0.0, need - presence))


def heard(inp, v) -> float:
    """PRESENCE: the share of him the room listens to, against the man opposite: the better heard of the two is heard whole and the other by
    his share; with nobody opposite, against what an ordinary man of the middle Presence would get from this room (C1)."""
    own = _heard_abs(inp, v.presence)
    o = lead(inp, _other(v.side)) if v.side else None    # the man opposite, as esteem reads him (V2 p4 §F 16); `_foe`'s abridged addressee is for the gap only
    if o is None:
        return min(1.0, own / _heard_abs(inp, inp.dials["attribute_mid"]))
    return own / max(own, _heard_abs(inp, o.presence))


def reason_tenths(inp, ground) -> int:
    """Reason's share of the speech's dice on `ground`, in whole tenths (R11): the ground's `reason` weight, by the venue's lean and the crowd's."""
    D = inp.dials
    return min(10, max(0, round(10 * (_ground(inp, ground)[0] + inp.rite.reason_lean - D["crowd_lean"] * crowd(inp)))))


def case_pool(inp, v, ground) -> float:
    """the speech's dice: Presence's share of them (the ground's `reason` weight is Reason's, by the venue's lean and the crowd's), then
    `heard`. `k` is Reason's share in whole tenths (R11); at control it is 10 and the dice are Reason's."""
    D = inp.dials
    k = reason_tenths(inp, ground)
    return heard(inp, v) * pool_of(weighted_tenth((v.reason, v.presence), (k, 10 - k)) + v.rank, 0, D["pool_add"], D["pool_floor"])


def _short(inp, p, c) -> float:
    return max(0.0, inp.rite.standard + inp.dials["show"] * c.rattles - p.grace)


def esteem(inp, st, v) -> float:
    """GRACE: his standing in the room this sitting: how much better he meets the venue's standard, and his own rattles, than the man opposite."""
    cd = _d(st.cond)
    o = lead(inp, _other(v.side)) if v.side else None
    return (_short(inp, o, cd[o.id]) if o else 0.0) - _short(inp, v, cd[v.id])


def _weary_term(inp, v, c, foe, pressed=False, abridged=False, over=None, first=False) -> tuple:
    D = inp.dials
    return max(0.0, c.spent - (D["stay_base"] + D["stay_per_will"] * v.will - awe(inp, v))), D["weary_step"]


def _standing_term(inp, v, c, foe, pressed=False, abridged=False, over=None, first=False) -> tuple:
    D = inp.dials
    account = (v.reason - D["attribute_floor"]) / (D["attribute_ceiling"] - D["attribute_floor"])
    return (max(0.0, foe.power - v.power) * (1.0 - account) if foe else 0.0), D["gap_step"]


def _press_term(inp, v, c, foe, pressed=False, abridged=False, over=None, first=False) -> Optional[tuple]:
    return (1.0, inp.dials["press_ob"]) if pressed else None


def _gravity_term(inp, v, c, foe, pressed=False, abridged=False, over=None, first=False) -> Optional[tuple]:
    return (inp.rite.gravity, 1.0) if abridged and not pressed else None


def _answer_term(inp, v, c, foe, pressed=False, abridged=False, over=None, first=False) -> Optional[tuple]:
    """B24.06 (HEAR_B's `answer`): an answer to an exhibit meets `answer_step` a unit of the weight the answered exhibit holds over its answer (`over`),
    a hostile term and never a subtraction (A-25: a heavier answer is the closing draw's `proof_level`)."""
    return (over, inp.dials["answer_step"]) if over else None


def _first_heard_term(inp, v, c, foe, pressed=False, abridged=False, over=None, first=False) -> Optional[tuple]:
    """B24.26 (ADM edit 4; OBS §2 member 11): an answer to an item the room heard FIRST (`first`: the answered `Item.first` inside a sitting, `Input.first_heard` for the answering
    `speak`) meets `first_heard_ob` more. A hostile term only, listed where it weighs (at `first_heard_ob` 0, the control, no roll names it)."""
    return (1.0, inp.dials["first_heard_ob"]) if first and inp.dials["first_heard_ob"] > 0 else None


#: The proceeding's own obstacle terms, the `rosters.yaml: obstacle_terms` members `bound: module`, in the roster's order:
#: `fn(inp, voice, cond, foe, pressed, abridged, over, first) -> (raw, step)`, or `None` where the term does not weigh on this speech. `roll.obstacle` composes
#: each as `raw x step` and names it in `Margin.terms`. Will: `weary`; Reason: `standing`; `press` is a press's and `gravity` the abridged form's;
#: `answer` is an exhibit answer's (`over`, B24.06); `first_heard` is an answer's to an item first heard (`first`, B24.26).
TERMS = {"weary": _weary_term, "standing": _standing_term, "press": _press_term, "gravity": _gravity_term, "answer": _answer_term, "first_heard": _first_heard_term}


def _operands(inp, voice, c, foe, pressed=False, abridged=False, over=None, first=False) -> tuple:
    got = ((name, fn(inp, voice, c, foe, pressed, abridged, over, first)) for name, fn in TERMS.items())
    return tuple((name,) + row for name, row in got if row is not None)


def weary(inp, v, c) -> float:
    raw, step = _weary_term(inp, v, c, None)
    return raw * step


def temper_of(inp, p, c) -> float:
    """A-136, A-146: how far this sitting's provocation (`heat`) has run past what his Will and Grace carry: 0 composed .. 1 lost."""
    D = inp.dials
    return _clip(D["temper_step"] * c.heat * 2.0 * D["attribute_mid"] / max(1.0, p.will + p.grace), 0.0, 1.0)


def _broken(inp, p, c) -> bool:
    return temper_of(inp, p, c) >= inp.dials["temper_break"]


def _legal(inp, st, mover) -> tuple:
    """his moves: the rite's for his side; a man whose temper has broken cannot hold his tongue (A-146), so the moves that do nothing leave
    his menu; with his turns spent, only those."""
    c = _d(st.cond)[mover.id]
    rows = _need(inp, "moves")
    ms = _d(inp.rite.moves).get(mover.side, ())
    if inp.rite.turns - c.spoken <= 0:
        return tuple(m for m, (effect, _) in rows.items() if effect == "none")
    if _broken(inp, mover, c) and len(ms) > 1:
        ms = tuple(m for m in ms if _move(inp, m)[0] != "none")
    return ms


def heat(inp, st, v) -> float:
    return -_sg(v.side) * mood(inp, st) * crowd(inp) if v.side else 0.0


def _pull(inp, st, v, c) -> float:
    D = inp.dials
    return D["press_pull"] * c.heat + D["rattle_pull"] * c.rattles + inp.rite.unrest + D["heckle"] * max(0.0, heat(inp, st, v))


def _hold_pool(v, D) -> float:
    return pool_of(v.focus, 0, D["pool_add"], D["pool_floor"])


def drift_of(pull, hold) -> float:
    """FOCUS (R1, B14): how far he is pulled off the point: the pull less what his hold carries, never below 0 and continuous in the pull."""
    return max(0.0, pull - max(0.0, hold))


def pressable(inp, side, P, S) -> bool:
    """a press lies only where something stands against the man pressed: a live point of his own that stands, or a charge laid on him."""
    return (P is not None and S > 0) or (side != inp.rite.bears and _reply(inp, side) == "must")


def silence_cost(inp, h, P, mover) -> float:
    """A-145: silence is never free where the rite says a point must be answered: a disrespect growing with the occasion and the listener's
    station, plus, where `silence` is `admits`, the unanswered point counting with him again by a share of how far it stands."""
    D, r = inp.dials, inp.rite
    if r.silence == "free":
        return 0.0
    floor_ = D["contempt_step"] * (r.standard / D["attribute_mid"])
    c = (floor_ if P is not None else 0.0) if h.id == mover.id else floor_ * (1.0 + (h.power / 4.0 if h.decides else 0.0))   # [canonical: V2 p2 §C.2 -- 1 + his station / 4]
    if r.silence == "admits" and P is not None:
        c += D["admit_step"] * max(0.0, _sg(P.side) * _d(P.held).get(h.id, 0.0))
    return c


def burden(inp, st, mover) -> bool:
    """THE BURDEN: the bearer of a matter the other side must answer has to put it; while no point of his stands, his rest is a charge not pressed."""
    if mover.side != inp.rite.bears or _reply(inp, _other(mover.side)) != "must":
        return False
    Po = _point(st, _d(st.live).get(mover.side))
    return Po is None or _stands(Po) <= 0


def insincerity(inp, voice, side, ground, it) -> float:
    """agreement between what he says and what he KNOWS (`believes`, a false item) and, on a ground that reads what he holds, what he HOLDS."""
    x = max(0.0, -_sg(side) * voice.believes)
    if it is not None and not it.sincere:
        x = 1.0
    if _reads(inp, ground) == "hold":
        x = max(x, -_sg(side) * voice.stake[_ix("hold")])
    return _clip(x, 0.0, 1.0)


# ------------------------------------------------------------------ what a speech lands on
def credit(h, it) -> float:
    return _clip(2.0 * it.weight - 1.0 + _bond(h, it.source) - max(0.0, _bond(h, it.about)))


def landing(h, side, channel, tag) -> float:
    """how a speech framed on `tag` lands on this listener's true interior: he must hold the tag and the matter must bear on it his way."""
    for c, t, w, bear in h.holds:
        if c == channel and t == tag:
            return _clip(_sg(side) * w * bear + 0.5 * (2.0 * w - 1.0))   # [canonical: V2 p2 §A.2 -- care's half-weight about the middle]
    return -0.5   # [canonical: V2 p2 §C.6 -- a frame on something he does not hold misses and misfits]


def fit(inp, h, voice, side, ground, it, tag=None) -> float:
    """the ground against how the matter (or the item, or the speaker) bears on this listener: -1..1."""
    reads = _reads(inp, ground)
    if reads == "item":
        return credit(h, it) if it else -1.0
    if reads == "bond":
        return _clip(_bond(h, voice.id) + 0.5 * (2.0 * h.care[_ix(reads)] - 1.0))   # [canonical: V2 p2 §A.2]
    if tag is not None:
        return landing(h, side, reads, tag)
    c = _ix(reads)
    return _clip(_sg(side) * h.stake[c] + 0.5 * (2.0 * h.care[c] - 1.0))   # [canonical: V2 p2 §A.2]


def aim(inp, t, ground, it, tag=None) -> float:
    """how hard a press BITES on him (B7): by how much he holds the thing it names AND how far this matter bears on it, either way. Unsigned."""
    reads = _reads(inp, ground)
    if reads == "item":
        if not it:
            return -1.0
        return _clip(it.weight * (1.0 if it.about == t.id else max(0.0, _bond(t, it.about))) * 2.0 - 1.0)
    c = _ix(reads)
    w, bear = t.care[c], t.stake[c]
    if tag is not None:
        hit = next(((ww, b) for ch, tg, ww, b in t.holds if ch == reads and tg == tag), None)
        if hit is None:
            return -1.0
        w, bear = hit
    return _clip(w * (1.0 + abs(bear)) - 1.0)


def frame(inp, hs, side, ground, acc=1.0, xa=0.0, xb=0.0, score=None) -> Optional[str]:
    """ATTUNEMENT (A-142): the frame he picks for a ground, from what he BELIEVES these listeners hold: each tag's worth as he reads it (true,
    blurred by his accuracy), the body's weighted mean. With `score` = aim it picks the press's object the same way. None for an item ground."""
    reads = _reads(inp, ground)
    tags = [t for ch, t in inp.frames if ch == reads]
    if reads == "item" or not tags:
        return None
    score = score or (lambda h, t: landing(h, side, reads, t))
    W = _wsum(h.weight for h in hs) or 1.0
    best, bv = None, -1e9
    for k, t in enumerate(tags):
        noise = xa * fmath.cos(1.7 * k) + xb * fmath.sin(1.7 * k)   # [canonical: V2 p2 §C.6 -- his own two normals, mixed per tag]
        v = _wsum(h.weight * score(h, t) for h in hs) / W + (1.0 - acc) * 0.5 * inp.dials["read_blur"] * noise   # [canonical: V2 p2 §E -- half the blur]
        if v > bv:
            best, bv = t, v
    return best


def press_object(inp, T, ground, acc=1.0, xa=0.0, xb=0.0) -> Optional[str]:
    return frame(inp, [T], T.side, ground, acc, xa, xb, score=lambda h, t: aim(inp, h, ground, None, t))


# ------------------------------------------------------------------ the one speech composer
def _record(inp, pool, opposition, leverage, difficulty, operands) -> SocialContestInput:
    D = inp.dials
    return SocialContestInput(pool=pool, opposition=opposition, obstacle_ceiling=None, obstacle_refusal_multiple=math.inf, leverage=leverage,
                              difficulty=difficulty, pool_default=D["pool_default"], pool_add=D["pool_add"],
                              opposition_rate=D["opposition_rate"], obstacle_operands=operands)


def speech(inp, st, mover, voice, h, ground, it, relation, *, press_on=None, abridged=False, tag=None, over=None, first=False) -> tuple:
    """one speech heard by `h` (who may be the speaker himself, where he decides: his own Reason validates it, his own Will resists it, C2).
    Returns `(pool, leverage, record)`; the record's obstacle is composed by `roll.obstacle`, so `Margin.terms` names each term. `over` (B24.06) is
    given for a board move's roll (`answer`, `impugn`): its difficulty is `answer_ob`, and `over` the weight the answered item holds over its answer
    (`TERMS["answer"]`); `None` for every other speech. `first` (B24.26) is given for an `answer` to an item first heard (`TERMS["first_heard"]`); an abridged speech
    meets it too where the host built the input for an act that answers one (`Input.first_heard`), and no other speech does. So does `over` (B24.43, `Input.answered_over`)."""
    D, r = inp.dials, inp.rite
    c, foe = _d(st.cond)[voice.id], _foe(inp, mover)
    pool = case_pool(inp, voice, ground)
    if over is None and abridged:
        over = inp.answered_over    # B24.43: the abridged speech of an act that answers an item is the sitting's `answer` (`Input.answered_over`): difficulty `answer_ob`, the `answer` term on this weight
    if press_on is not None:
        T = press_on
        sig = _lv(D["fit_level"]) * _weight(inp, st, ground) * aim(inp, T, ground, it, tag) + D["room_level"] * heat(inp, st, T) \
            + D["esteem_step"] * esteem(inp, st, voice)
        # [ASSUMPTION; Jordan to correct: awe is subtracted as so many points of Will, as the running model does (`sc2/engine.py:642`); V2 p2 §C.4's
        # text divides it by `MU_PER_DIE` as it does the strain -- basis: the shipped `awe_step` was tuned on the model; no effect while it is 0]
        opp = max(0.0, T.will + T.rank - _d(st.cond)[T.id].strain / MU_PER_DIE - awe(inp, T))
        return pool, sig, _record(inp, pool, opp, sig, 0.0, _operands(inp, voice, c, foe, pressed=True))
    v = validation(inp, h)
    rl = 1.0 + 2.0 * v * (relevance(inp, voice) - 1.0)    # how sound the speech is, as far as HE can validate it
    fitted = fit(inp, h, voice, mover.side, ground, it, tag)
    if h.backed is not None and ground not in h.backed:
        fitted = min(fitted, 0.0)      # B24.35 (WGM edits 2-3): a ground that does not back this act with him counts none of its fit in his favour; a misfit still counts
    f = fitted + D["rel_gain"] * (rl - 1.0) \
        - D["repeat_step"] * _d(st.used).get((mover.side, it.id if it else ground), 0)
    sig = _lv(D["fit_level"]) * _weight(inp, st, ground) * f + D["esteem_step"] * esteem(inp, st, voice) * 2.0 * (1.0 - v) \
        + (rl * _lv(D["answer_level"]) if relation == "answers" else 0.0) \
        + (_sg(mover.side) * _lever(inp, st) if abridged else 0.0)    # B24's close (R1): the abridged speech IS the close, so what counts on it (`_lever`) is its leverage, toward the speaker
    return pool, sig, _record(inp, pool, h.will + h.rank, sig, D["answer_ob"] if over is not None else r.difficulty if abridged else 0.0,
                              _operands(inp, voice, c, foe, abridged=abridged, over=over, first=first or (abridged and inp.first_heard)))


def _lv(name) -> float:
    """a setting naming a level; `None` is the control, no leverage."""
    return 0.0 if name is None else level(name)


def _margin(inp, pool, z, x, off, h, ded):
    """`(net, ob, terms, m)`: the speech's roll and boost less what is off the point (Focus) and a ploy (Attunement); `m = net - ob`."""
    D = inp.dials
    ob, terms = obstacle(x)
    net = _roll(pool, z) + net_boost(x.leverage, pool) - D["off_step"] * _wF(h, D) * off - ded
    return net, ob, terms, net - ob


# ------------------------------------------------------------------ the view
def perceived(true_worth, acc, x, lean, D) -> float:
    """ATTUNEMENT (A-141): the one gauge every worth reaches a view through: the worth plus an error that shrinks as his reading sharpens
    (his own noise `x`, and his stable bias `lean`). At `acc` 1 perceived is true."""
    return true_worth + (1.0 - acc) * (D["read_blur"] * x + D["bias_step"] * lean)


def _believed(inp, h, acc):
    """B11, A-141: a listener's judging operands and Will as he BELIEVES them: the truth as far as his accuracy reaches, the middle of the
    scale for the rest (a stranger is an ordinary man, B05.62)."""
    if acc >= 1.0:
        return h
    D = inp.dials

    def b(x):
        return D["attribute_mid"] + acc * (x - D["attribute_mid"])
    return replace(h, attunement=b(h.attunement), focus=b(h.focus), reason=b(h.reason), will=b(h.will))


def _yield_to(D) -> float:
    """how far a given-up matter puts the room: as far as the close's leverage can carry it."""
    return M_MAX / D["track_step"] if D["track_step"] else D["mood_scale"]


def _lasting(inp, T, ct, mean, turns_left) -> float:
    """what a rattle goes on doing after it lands (C1): his standing falls only as far as his Grace lacks headroom, he tires only past his
    staying power, his next speech is pulled; in track units through one speech's slope, the later speeches discounted by `invite`."""
    D, r = inp.dials, inp.rite
    slope = 0.75 * _sd(pool_of(D["attribute_mid"] + 1.0, 0, D["pool_add"], D["pool_floor"]))   # [canonical: V2 p2 §E -- three quarters of one speech's slope]
    dshort = max(0.0, r.standard + D["show"] * (ct.rattles + 1) - T.grace) - max(0.0, r.standard + D["show"] * ct.rattles - T.grace)
    v = mean(lambda h: validation(inp, h))
    stay = D["stay_base"] + D["stay_per_will"] * T.will - awe(inp, T)
    k = max(0, turns_left - 1)
    return k * (2.0 * D["esteem_step"] * dshort * 2.0 * (1.0 - v) * slope * (1.0 - D["invite"])   # [canonical: V2 p2 §E -- _lasting's weights]
                + D["weary_step"] * (1.0 if ct.spent + 1.0 > stay else 0.0) * 0.75) \
        + D["off_step"] * mean(lambda h: _wF(h, D)) * 0.6 * (D["press_pull"] + D["rattle_pull"]) * 0.75   # [canonical: V2 p2 §E -- _lasting's weights]


def menu(inp, st, mover, turns_left, frames=None, objects=None, acc=1.0) -> tuple:
    """The worth of every legal option from the engine's own values, each listener read as he believes him: `([(move, ground, item, relation,
    ev, p, frame)], T, P, S)`. No draw. Nobody is shown this: a `View` shows `perceived` of it."""
    D = inp.dials
    G = [g for g, _, _ in inp.grounds]
    c = _d(st.cond)[mover.id]
    hs = [h if h.id == mover.id else _believed(inp, h, acc) for h in _deciders_for(inp, mover)]
    W = _wsum(h.weight for h in hs) or 1.0
    mean = lambda f: _wsum(h.weight * f(h) for h in hs) / W
    other_side = _other(mover.side)
    tid = _d(st.last_voice).get(other_side)
    T = who(inp, tid) if tid else lead(inp, other_side)
    items = _items(inp, mover)
    pull = _pull(inp, st, mover, c)
    Pf = _hold_pool(mover, D)
    e_drift = min(pull, _epos(pull - (MU_PER_DIE * Pf - even_line(D["pool_add"])), _sd(Pf))) if pull > 0 else 0.0
    rep_ = _reply(inp, mover.side)
    P = _point(st, _d(st.live).get(other_side))
    S = _stands(P) / max(1, len(P.held)) if P else 0.0
    must_answer = P is not None and S > 0 and rep_ == "must"
    bur = burden(inp, st, mover)
    sc_a = mean(lambda h: silence_cost(inp, h, P, mover)) if must_answer else 0.0           # a point left standing
    sc_b = mean(lambda h: silence_cost(inp, h, None, mover)) if (bur and not must_answer) else 0.0   # a matter not put
    m_true = _sg(mover.side) * mood(inp, st, mover)
    cands = [(g, None) for g in G if _reads(inp, g) != "item"] + [(g, it) for g in G if _reads(inp, g) == "item" for it in items]
    if frames is None:                                   # with no reading given: the frames a perfect reader would pick
        frames = {g: frame(inp, hs, mover.side, g) for g in G}
    if objects is None and T is not None:
        objects = {g: press_object(inp, T, g) for g in G}

    def mu_of(stx, h, g, it, rel, pool, ins, abridged=False, drift=0.0, over=None, first=False):
        x = speech(inp, stx, mover, mover, h, g, it, rel, abridged=abridged, tag=frames.get(g), over=over, first=first)[2]
        return MU_PER_DIE * pool + net_boost(x.leverage, pool) - obstacle(x)[0] - D["off_step"] * _wF(h, D) * drift \
            - D["ploy_step"] * _wA(h, D) * ins

    def best_raise(stx):
        best = -math.inf
        for g, it in cands:
            pool, ins = case_pool(inp, mover, g), insincerity(inp, mover, mover.side, g, it)
            mu = mean(lambda h: mu_of(stx, h, g, it, "raises", pool, ins))
            best = max(best, _epos(mu, _sd(pool)) - D["flop"] * _epos(-mu, _sd(pool)))
        return best

    out = []
    for mid in _legal(inp, st, mover):
        effect, _ = _move(inp, mid)
        if effect == "track":
            for g, it in cands:
                pool, ins = case_pool(inp, mover, g), insincerity(inp, mover, mover.side, g, it)
                sd = _sd(pool)
                for rel in (["answers"] if (rep_ != "raise" and P is not None and S > 0) else []) + ["raises"]:
                    mu = mean(lambda h: mu_of(st, h, g, it, rel, pool, ins, inp.rite.close == "exchange", e_drift))
                    if rel == "answers":         # bounded both ways by how far the point stands (C1)
                        ev = min(S, _epos(mu, sd)) - D["flop"] * min(S, _epos(-mu, sd))
                    else:
                        invited = D["invite"] if (_d(inp.rite.moves).get(other_side) and _reply(inp, other_side) != "raise"
                                                  and T is not None) else 0.0
                        ev = (1.0 - invited) * _epos(mu, sd) - D["flop"] * _epos(-mu, sd) - sc_a
                    out.append((mid, g, it.id if it else None, rel, ev, _p_up(mu, sd), frames.get(g)))
        elif effect == "strike":
            if T is None or not pressable(inp, other_side, P, S):
                continue
            ct = _d(st.cond)[T.id]
            for g, it in cands:
                tag = (objects or {}).get(g) if it is None else None
                pool, sig, x = speech(inp, st, mover, mover, T, g, it, "presses", press_on=T, tag=tag)
                mu = MU_PER_DIE * pool + net_boost(sig, pool) - obstacle(x)[0]
                p = _p_up(mu, _sd(pool))
                gain = D["rattle_gain"] * (1.0 - D["reactance"] * ct.rattles) * mean(
                    lambda h: (1.0 - max(0.0, _bond(h, T.id))) * discern(inp, h, T) * theatre(inp, h))
                ins = 1.0 if (it is not None and not it.sincere) else 0.0
                ev = p * (gain + _lasting(inp, T, ct, mean, turns_left)) - (1 - p) * D["rebound"] - D["off_step"] * e_drift \
                    - D["ploy_step"] * ins - sc_a - sc_b
                out.append((mid, g, it.id if it else None, "presses", ev, p, tag))
        elif effect == "yield":
            own = _d(st.tracks).get(mover.id, 0.0)
            last = st.issue >= len(inp.rite.issues) - 1
            if (inp.rite.concede == "accepts" or last) and (inp.rite.close == "consent" or _sole(inp, mover)):
                ev = -_sg(mover.side) * own - D["consent_at"]       # his accept IS the close: his own consent
            elif inp.rite.concede == "accepts" or last:              # one seat, one vote: on a close others share, his yield gives the matter up
                ev = -_yield_to(D) * (1.0 + m_true)
            else:                                 # C1, C5: what descending buys: the next rung's better ground, fresh
                st2 = replace(st, issue=st.issue + 1, live=(("for", None), ("against", None)),
                              used=tuple((k, v) for k, v in st.used if k[0] != mover.side))
                ev = max(0.0, best_raise(st2) - best_raise(st)) * max(0, turns_left - 1) \
                    - D["concede_step"] * (1.0 + max(abs(x) for x in mover.stake))
            out.append((mid, None, None, "concedes", ev, None, None))
        elif effect == "exhibit":                    # B24.06: each admitted item of his hand not yet shown, at what it would weigh on this rung
            for x_it in _hand(inp, st, mover):
                out.append((mid, None, x_it.id, "presents", _worth(inp, _entry_weight(x_it, _issue(inp, st))), None, None))
        elif effect in ("answer", "impugn"):         # B24.06: each standing item of the other side he may answer, or whose origin he may impugn, on each ground
            for tg, ans, over in _answerable(inp, st, mover, effect):
                for g in G:
                    if effect == "impugn" and _reads(inp, g) == "item":
                        continue
                    a, rel = (ans if _reads(inp, g) == "item" else None), ("answers" if effect == "answer" else "impugns")
                    pool = case_pool(inp, mover, g)
                    sd = _sd(pool)
                    mu = mean(lambda h: mu_of(st, h, g, a, rel, pool, 0.0, False, e_drift, over, effect == "answer" and tg.first))
                    if effect == "answer":           # bounded both ways by how far the answered item stands (C1)
                        ev = min(tg.weight, _epos(mu, sd)) - D["flop"] * min(tg.weight, _epos(-mu, sd))
                    else:                            # a win halves the origin's items, a failure costs a level (HEAR_B's table)
                        p = _p_up(mu, sd)
                        ev = p * _worth(inp, _wsum(i.weight for i in _standing(inp, st.board) if i.origin == tg.origin) / 2.0) - (1.0 - p) * _cost(inp, 1)
                    out.append((mid, g, tg.id, rel, ev, _p_up(mu, sd), frames.get(g)))
        elif effect in ("rule", "adjourn"):
            continue                                 # the bench's moves: a seat that decides without a side takes no turn in `proceed` (the order is the host's, B24.10)
        else:
            out.append((mid, None, None, "rests", -sc_a - sc_b, None, None))
    return out, T, P, S


def accuracy(D, attunement, z) -> float:
    """HIS ACCURACY (V2 p2 §C.6): his Attunement alone, with a little luck `z` (a standard normal), opposed by nothing: 0.5 at the middle of the scale. THE ONE LADDER OF A
    READING: `view` reads it for the exchange's view, and the host reads it for a reading of the bench (B24.29) with its own keyed `z`."""
    return (1.0 + fmath.tanh((MU_PER_DIE * (attunement - D["attribute_mid"]) + D["read_noise"] * z) / D["read_scale"])) / 2.0


def read_sign(D, attunement, sign, rng) -> int:
    """THE SIGN OF A LEAN AS A READER TAKES IT (B24.29, V2 p2 §C.6): `sign` (+1 or -1) is the true sign, and the reader holds it with chance `(1 + acc) / 2`, `acc` his `accuracy` at the
    first normal of `rng` (the host's one keyed stream of this reading), the share of the truth `acc` reaches, the rest a guess: the stream's next uniform. A wrong sign is possible at every
    Attunement, a truer one likelier at a higher. The module owns the outcome and the host keeps the stream and the Attunement. Pure over `rng`."""
    acc = accuracy(D, attunement, rng.normal(0.0, 1.0))
    return sign if rng.random() < (1.0 + acc) / 2.0 else -sign


def view(inp, st, mover, rng) -> View:
    """what a chooser is shown (V2 p2 §E): own values true, everything else perceived, each number with its own normal. Takes all of the
    exchange's draws but the hold and the speech."""
    D, n0 = inp.dials, rng.n
    G = [g for g, _, _ in inp.grounds]
    c = _d(st.cond)[mover.id]
    turns_left = inp.rite.turns - c.spoken
    # his accuracy is his Attunement, with a little luck: 0.5 at the middle of the scale; nothing opposes it
    acc = accuracy(D, mover.attunement, _z(rng))
    xarg, xprs = {g: _z(rng) for g in G}, {g: _z(rng) for g in G}
    xc, xm, xt, xo, xi, xe, xr, xw = (_z(rng) for _ in range(8))
    xfa, xfb, xoa, xob = ({g: _z(rng) for g in G} for _ in range(4))
    hs = [h if h.id == mover.id else _believed(inp, h, acc) for h in _deciders_for(inp, mover)]
    frames = {g: frame(inp, hs, mover.side, g, acc, xfa[g], xfb[g]) for g in G}       # framed from his believed reading
    other_side = _other(mover.side)
    tid = _d(st.last_voice).get(other_side)
    T0 = who(inp, tid) if tid else lead(inp, other_side)
    objects = {g: press_object(inp, T0, g, acc, xoa[g], xob[g]) for g in G} if T0 is not None else {}
    true, T, P, S = menu(inp, st, mover, turns_left, frames, objects, acc)
    opts = []
    for mv, g, it, rel, ev, p, fr in true:
        effect, draws = _move(inp, mv)
        x = xarg[g] if effect in ("track", "answer", "impugn") else xprs[g] if effect == "strike" else xc if effect == "yield" else xr
        pe = perceived(ev, acc, x, mover.bias if draws else 0.0, D)
        pp = None if p is None else _clip(perceived(p, acc, 0.1 * x, 0.1 * mover.bias, D), 0.0, 1.0)   # [canonical: V2 p2 §E -- a chance's tenth of the worth's error]
        opts.append(Option(mv, g, it, rel, round(pe, 2), None if pp is None else round(pp, 2), fr))
    m_seen = _clip(perceived(_sg(mover.side) * mood(inp, st, mover), acc, 0.25 * xm, 0.0, D))   # [canonical: V2 p2 §E -- a quarter of the blur on a 0..1 reading]
    intent = _clip(perceived(_wsum(T.stake) / 3.0 if T else 0.0, acc, 0.25 * xi, 0.0, D))   # [canonical: V2 p2 §E -- the mean of three channels]
    Po = _point(st, _d(st.live).get(mover.side))
    live_theirs = (P.id, P.ground, P.item, round(perceived(S, acc, 0.5 * xt, 0.0, D), 1)) if P else None   # [canonical: V2 p2 §E -- half the blur on a strength]
    live_own = (Po.id, Po.ground, Po.item, round(perceived(_stands(Po) / max(1, len(Po.held)), acc, 0.5 * xo, 0.0, D), 1)) if Po else None
    vis = tuple((p.id, _d(st.cond)[p.id].rattles) for p in inp.room if p.side)
    out = View(st.n, mover.id, mover.side, _issue(inp, st), turns_left, live_theirs, live_own, tuple(opts), c,
               round(perceived(esteem(inp, st, mover), acc, 0.25 * xe, 0.0, D), 2), round(weary(inp, mover, c), 2),   # [canonical: V2 p2 §E -- a quarter of the blur]
               round(max(0.0, perceived(awe(inp, mover), acc, 0.25 * xw, 0.0, D)), 2), _broken(inp, mover, c), vis, m_seen,
               0.0, intent, acc, burden(inp, st, mover), board=tuple(st.board), hand=tuple(_hand(inp, st, mover)),     # B24.06: the rite discloses the whole board
               lever=_lever(inp, st))                                                                                   # the close's own board term, which `odds` reads (R12)
    assert rng.n - n0 == 2 * (DRAWS_PER_EXCHANGE(len(G)) - 2), (rng.n - n0)    # normals are two uniforms each (`Draw.normal`)
    return replace(out, odds=view_odds(inp, out))


# ------------------------------------------------------------------ one exchange
def exchange(inp, st, mover, choice, rng, framed=None, mark=None) -> tuple:
    """one exchange: `(Sitting, Beat)`. The view's draws are already taken (`view`, the choice made on it, `framed` the picked option's frame);
    this takes the hold and then the speech, whatever the move. Pure but for `rng`; new values by `replace`. `mark` is `rng.n` before the
    view: where given, the whole exchange (view and speech) is asserted to have taken `DRAWS_PER_EXCHANGE` normals."""
    new, beat, _ = _exchange(inp, st, mover, choice, rng, framed)
    _took(inp, rng, mark)
    return new, beat


def _took(inp, rng, mark) -> None:
    if mark is not None:
        assert rng.n - mark == 2 * DRAWS_PER_EXCHANGE(len(inp.grounds)), (rng.n - mark)    # normals are two uniforms each


def _exchange(inp, st, mover, ch, rng, tag) -> tuple:
    """`exchange` and, third, each listener's `Margin` (what an abridged close reads)."""
    D, r, n0 = inp.dials, inp.rite, rng.n
    effect, draws = _move(inp, ch.move)
    abridged = r.close == "exchange"
    it = _find_item(inp, ch.item) if ch.item else None
    voice = _voice(inp, mover, it) if effect == "track" else mover
    cond = _d(st.cond)
    cv = cond[voice.id]
    side, sg = mover.side, _sg(mover.side)
    other = _other(side)
    hold = _roll(_hold_pool(voice, D), _z(rng)) - even_line(D["pool_add"])
    drift = drift_of(_pull(inp, st, voice, cv), hold)
    z = _z(rng)
    tracks, live, points, used = _d(st.tracks), _d(st.live), list(st.points), _d(st.used)
    hearers = _hearers(inp, voice, side)
    own = [mover] if (mover.decides and voice.id == mover.id) else []        # C2: he is moved by his own case
    judges = [h for h in hearers + own if h.decides] or hearers
    lt = live.get(other)
    P_lt = _point(st, lt)
    rep = _reply(inp, side)
    stands = P_lt is not None and _stands(P_lt) > 0
    relation = ch.relation or {"track": "raises", "strike": "presses", "yield": "concedes", "none": "rests", "exhibit": "presents", "answer": "answers",
                               "impugn": "impugns", "rule": "rules", "adjourn": "adjourns"}[effect]
    if relation == "answers" and not stands and effect == "track":
        relation = "raises"                               # an answer is to a point that stands; else it raises (an `answer` move's is to an item)
    unanswered = stands and relation != "answers" and effect not in ("yield", "exhibit", "impugn", "rule", "adjourn")
    evade_a = rep == "must" and unanswered
    evade_b = burden(inp, st, mover) and effect in ("none", "strike") and not evade_a
    evaded = (evade_a or evade_b) and r.silence != "free"
    moved, margins, margin, rattled, target, closed, pid, insinc, terms, ended, caught = [], [], 0.0, None, None, None, None, 0.0, (), None, []
    issue, obj = _issue(inp, st), tag
    board, faults, levels, entered, struck, flagged = list(st.board), list(st.faults), list(st.levels), [], [], []

    def move(h, d):
        moved.append((h.id, d))
        tracks[h.id] += d

    def fault(name, who):                                 # a condition on the board, and a cost on the closing draw (`Input.dials["fault_levels"]`, `rosters.yaml: proceeding_faults`), never a verdict
        if name not in inp.rite.faults:                   # B24.32: a rite lists the faults that apply (`Rite.faults`); one it does not list is not recorded and costs no level
            return
        faults.append((name, who))
        flagged.append(name)
        if inp.dials["fault_levels"][name]:               # a fault that costs no level (`0`) writes none
            levels.append((who, inp.dials["fault_levels"][name]))

    def put(iid, how=None, w=None, band=None):            # one item's row on the board: a status, a weight where it changes, the best band drawn against it
        k = _at(board, iid)
        it, s = board[k]
        if band is not None and (it.answered_band is None or band_of(band) > band_of(it.answered_band)):
            it = replace(it, answered_band=band)
        board[k] = (replace(it, weight=it.weight if w is None else w), how or s)

    if effect == "track":
        insinc = insincerity(inp, voice, side, ch.ground, it)
        held, tot, W = {}, 0.0, 0.0
        for h in hearers + own:
            pool, sig, x = speech(inp, st, mover, voice, h, ch.ground, it, relation, abridged=abridged, tag=tag)
            ded = D["ploy_step"] * _wA(h, D) * insinc
            net, ob, terms, m = _margin(inp, pool, z, x, drift, h, ded)
            if insinc > 0 and m < 0 <= m + ded:
                caught.append(h.id)                       # his reading of the speaker turned it (B2)
            if h in judges:
                tot += h.weight * m
                W += h.weight
            margins.append((h.id, Margin(net=net, ob=ob, terms=terms)))
            if relation == "answers":                     # bounded both ways by how far the point stands with him (C1)
                s = max(0.0, _sg(other) * _d(P_lt.held).get(h.id, 0.0))
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
    elif effect == "strike":
        lv = _d(st.last_voice).get(other)
        T = who(inp, lv) if lv else lead(inp, other)
        target = T.id
        insinc = 1.0 if (it is not None and not it.sincere) else 0.0          # a press made with a forged item
        obj = None if it is not None else tag
        pool, sig, x = speech(inp, st, mover, voice, T, ch.ground, it, relation, press_on=T, tag=obj)
        net, ob, terms, margin = _margin(inp, pool, z, x, 0.0, T, 0.0)
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
            seen = gain * (1.0 - max(0.0, _bond(h, T.id))) * discern(inp, h, T) * theatre(inp, h) if landed else gain
            ded = D["ploy_step"] * _wA(h, D) * insinc
            d = sg * (seen - D["off_step"] * _wF(h, D) * drift - ded)
            if insinc > 0 and sg * d < 0 <= sg * d + ded:
                caught.append(h.id)
            move(h, d)
        pid = lt
    elif effect == "yield":
        last = st.issue >= len(r.issues) - 1
        closed = issue
        if r.concede == "accepts" or last:
            ended = "yielded"                           # he gives up the matter: the room goes to the other side as far as the close can carry it
            for h in hearers + ([mover] if mover.decides else []):
                move(h, -sg * _yield_to(D) - tracks[h.id])
        else:                                           # C5: a conceded issue STAYS conceded and costs, from where he stands
            cost = D["concede_step"] * (1.0 + max(abs(x) for x in mover.stake))
            for h in hearers + ([mover] if mover.decides else []):
                move(h, -sg * cost)
            live = {"for": None, "against": None}
            used = {k: v for k, v in used.items() if k[0] != side}
    elif effect == "exhibit":                           # B24.06: an item of his hand enters the board; nothing is drawn but the exchange's own two
        if it is None or it not in mover.items or it.kind not in r.admits or _at(board, it.id) is not None:
            raise ValueError(f"refused[exhibit]: {ch.item!r} is not an admitted item of {mover.id}'s hand not yet shown")
        w = _entry_weight(it, issue)                    # off the rung tried it enters at half, and the `irrelevance` fault counts it
        if w != it.weight:
            fault("irrelevance", side)
        board.append((replace(it, side=side, weight=w), STANDS))
        entered.append(it.id)
        clash = [o for o in _standing(inp, board, side) if o.id != it.id and pair_of(it, o) == CONTRADICTS]
        if clash:                                       # two standing items of one side disagree: the lighter is withdrawn (the newcomer on a tie)
            if max(i.weight for i in clash) < w:        # the newcomer outweighs every item it clashes with: all of them are withdrawn, not only the heaviest
                for o in clash:
                    put(o.id, WITHDRAWN)
            else:
                put(it.id, WITHDRAWN)
            fault("self_contradiction", side)
    elif effect in ("answer", "impugn"):                # B24.06: a rolled move on the board; each listener's margin is read as a speech's is
        tg, ans, over = next(((t, a, o) for t, a, o in _answerable(inp, replace(st, board=tuple(board)), mover, effect) if t.id == ch.item), (None, None, None))
        if tg is None:
            raise ValueError(f"refused[{effect}]: {ch.item!r} is not a standing item of the other side that {mover.id} may {effect}")
        tot, W = 0.0, 0.0
        for h in hearers + own:
            pool, sig, x = speech(inp, st, mover, voice, h, ch.ground, (ans if _reads(inp, ch.ground) == "item" else None), relation, abridged=abridged, tag=tag,
                                  over=over, first=effect == "answer" and tg.first)      # the answer item is spoken only on a ground that reads an item, as `menu` prices it
            net, ob, terms, m = _margin(inp, pool, z, x, drift, h, 0.0)
            if h in judges:
                tot += h.weight * m
                W += h.weight
            margins.append((h.id, Margin(net=net, ob=ob, terms=terms)))
            if effect == "answer":                      # bounded both ways by how far the answered item stands (C1)
                move(h, sg * (min(tg.weight, m) if m > 0 else -D["flop"] * min(tg.weight, -m)))
        margin = tot / W if W else 0.0
        degree = dice_engine.degree_from_net(margin, 0.0)           # graded on the one ladder owner, in the module (HEAR_B)
        if effect == "impugn":                          # Success or better halves every item of that origin; Failure is a level against the mover
            if dice_engine.DEGREE_ORDINAL[degree] >= CARRIED:
                for o, s_ in list(board):
                    if s_ not in (STRUCK, WITHDRAWN) and o.origin == tg.origin:
                        put(o.id, None, o.weight / 2.0)
            elif dice_engine.DEGREE_ORDINAL[degree] == FAILURE:
                levels.append((side, 1))                # the `impugn` row's own level (a failed impugnment costs its mover one); a fault's levels are `fault_levels`, this one is a move's and no roster column carries it
        else:                                           # the answering act's band is the item's own, and `evidence.standing` reads it: nothing is decided here
            put(tg.id, None, None, dice_engine.DEGREE_LABEL[degree])
    elif effect in ("rule", "adjourn"):                 # the bench's: close on what was said now, or hold the stage to the next sitting (resumable)
        if not mover.decides:
            raise ValueError(f"refused[{effect}]: {mover.id} does not decide, and only the bench rules or adjourns")
        ended = "rested" if effect == "rule" else "budget"
    if board:                                           # B24.19: what the board owes and what it strikes is `evidence.standing`'s, read once the exchange has changed it
        before, board = _ruled(inp, st.board), _settle(inp, board)
        for name, by in newly_owed(before[2], _ruled(inp, board)[2]):
            fault(name, by)
        gone = {i.id for i, s_ in st.board if s_ in (STRUCK, WITHDRAWN)}
        struck = [i.id for i, s_ in board if s_ in (STRUCK, WITHDRAWN) and i.id not in gone]
    if effect == "none" and any(p.items for p in inp.room):       # SILENCE as a fault: the bearer rests with nothing standing on the rung, or the other rests unanswered
        if (side == r.bears and not [i for i in _standing(inp, board, side) if _on_rung(i, issue)]) or \
                (side != r.bears and [i for i, s in board if s == STANDS and i.side == other and _on_rung(i, issue)]):
            fault("silence", side)
    if evaded:                                          # silence, or turning away, where he must speak (A-145)
        for h in hearers + ([mover] if mover.decides else []):
            move(h, -sg * silence_cost(inp, h, P_lt if evade_a else None, mover))
    cv2 = cond[voice.id]
    cond[voice.id] = replace(cv2, heat=cv2.heat * (1.0 - D["temper_cool"]), spoken=cv2.spoken + 1, spent=cv2.spent + (1.0 if draws else 0.0))
    if voice.id != mover.id:
        cm = cond[mover.id]
        cond[mover.id] = replace(cm, spoken=cm.spoken + 1)
    lv = _d(st.last_voice)
    if draws:
        lv[side] = voice.id
    new = replace(st, n=st.n + 1, issue=st.issue + (1 if (closed and ended is None) else 0), points=tuple(points), live=tuple(live.items()),
                  tracks=tuple(tracks.items()), cond=tuple(cond.items()), used=tuple(used.items()), last_voice=tuple(lv.items()), ended=ended,
                  board=tuple(board), faults=tuple(faults), levels=tuple(levels))
    beat = Beat(st.n + 1, mover.id, voice.id, side, ch.move, relation, issue, ch.ground, ch.item, pid, target, margin, drift, evaded,
                lt if unanswered else None, insinc, tuple(caught), rattled,
                (tag if effect == "track" else obj if effect == "strike" else None), relevance(inp, voice), heard(inp, voice),
                esteem(inp, st, voice), _broken(inp, mover, _d(st.cond)[mover.id]), tuple(moved), closed, mood(inp, new), terms,
                tuple(entered), tuple(struck), flagged[0] if flagged else None)
    assert rng.n - n0 == 2 * 2, (rng.n - n0)    # the hold and the speech, a normal each (two uniforms: `Draw.normal`)
    return new, beat, tuple(margins)


# ------------------------------------------------------------------ the sitting (B24p.11)
def _speakers(inp) -> list:
    """who speaks, in the order of a round: the side that bears the live thing opens, then each by precedence (V2 p2 §C.1)."""
    moves = _d(inp.rite.moves)
    sp = [p for p in inp.room if p.side and moves.get(p.side)]
    return sorted(sp, key=lambda p: (0 if p.side == inp.rite.bears else 1, -p.precedence, p.id))


def _able(inp, st) -> list:
    return [p for p in _speakers(inp) if _d(st.cond)[p.id].spoken < inp.rite.turns]


def start(inp) -> Sitting:
    """the sitting's opening value: a given `Input.state` (refused at `Input` if it cannot be resumed) opened again, else each person at his
    `start` carrying in his `strain`, the first rung (or the one undivided issue) reached."""
    if inp.state is not None:
        return replace(inp.state, ended=None)
    return Sitting(tracks=tuple((p.id, p.start) for p in inp.room), cond=tuple((p.id, Cond(strain=p.strain)) for p in inp.room))


def _mover(inp, st) -> Optional[str]:
    """who speaks next: of those with a turn left (the rite's `turns` less `cond.spoken`) the one who has spoken least, the bearer's side first
    and then by precedence; `None` when nobody can move."""
    able = _able(inp, st)
    c = _d(st.cond)
    return min(able, key=lambda p: c[p.id].spoken).id if able else None


def policy(inp, view, me) -> Choice:
    """THE AUTOMATIC POLICY (A-136; V2 p2 §F): below `temper_break` a man takes the option his own reading says is worth most, the same menu and
    view a player has and no other information; at or past it the man shows: he argues from what he himself holds (and the orator plays to the
    room), the proud press and will not give way, the timid give way, a grudge goes after its object. The earlier of equal options wins."""
    D = inp.dials
    t = temper_of(inp, me, view.own)
    t = t if t >= D["temper_break"] else 0.0
    foe = max((i for i, _ in view.visible if i != me.id), key=lambda i: abs(_bond(me, i)), default=None)
    nerve = (me.will - D["attribute_mid"]) / 3.0    # [canonical: V2 p2 §F -- the temperament, three points of attribute a step]
    best, bv = None, -math.inf
    for o in view.options:
        effect, v = _move(inp, o.move)[0], o.ev
        if effect == "track" and o.ground is not None and _reads(inp, o.ground) != "item":
            c = _ix(_reads(inp, o.ground))
            v += t * D["grain"] * ((2.0 * me.care[c] - 1.0) + ((me.presence - D["attribute_mid"]) / 3.0 if _reads(inp, o.ground) == "bond" else 0.0))   # [canonical: V2 p2 §F]
        elif effect == "strike":
            v += t * (D["grudge"] * (-_bond(me, foe)) + D["pride"] * nerve)
        elif effect == "yield":
            v -= t * D["pride"] * nerve
        if v > bv + 1e-12:    # [canonical: sc2/engine.py:931 -- a lead inside float noise is a tie, and the earlier option keeps it]
            best, bv = o, v
    if best is None:
        raise ValueError(f"refused[menu]: {me.id} has nothing legal to do")
    return Choice(best.move, best.ground, best.item, best.relation)


def _taken(inp, st, view, me, ch) -> tuple:
    """a chooser's pick, checked: his move must be in `_legal` and the pick must be on the menu he was shown; `(Choice, the option's frame)`,
    the choice with the option's own relation (an answer is offered only to a point that stands)."""
    legal = _legal(inp, st, me)
    if ch.move not in legal:
        raise ValueError(f"refused[choice]: {me.id} may not {ch.move!r} here (legal: {legal})")
    o = next((o for o in view.options if (o.move, o.ground, o.item) == (ch.move, ch.ground, ch.item) and ch.relation in (None, o.relation)), None)
    if o is None:
        raise ValueError(f"refused[choice]: {me.id}: {tuple(ch)} is not on his menu")
    return Choice(o.move, o.ground, o.item, o.relation), o.frame


# ------------------------------------------------------------------ the close (B24p.12; V2 p2 §D)
#: A ruling's margin: the middle of the ladder's Success band, so a ruling carries and is never an Overwhelming; against is its mirror.
_RULING = (dice_engine.BAND_FLOORS["success"] + dice_engine.BAND_FLOORS["overwhelming"]) / 2.0 / dice_engine.MARGIN_SCALE    # [canonical: the ladder, BAND_FLOORS in MARGIN_SCALE milli-units; the running model's 2.0 (sc2/engine.py:1152)]
CARRIED = dice_engine.DEGREE_ORDINAL[dice_engine.Degree.SUCCESS]      # carried is Success or better: the ladder's third band (V2 p3 §B.1 D2: carried = success + overwhelming)


def _seats(inp) -> list:
    """those who decide, the presiding seat first (highest precedence, then id): the close draws in this order and `bench` is the first's."""
    return sorted((p for p in inp.room if p.decides), key=lambda p: (-p.precedence, p.id))


def close_record(inp, track, board=0.0) -> tuple:
    """`(pool, record)` of one adjudicator's draw at `track`: the ordinary bench (the middle of the scale for his dice and for what opposes
    him), his own track as the leverage, the rite's `difficulty` and `gravity` (named in `Margin.terms`) the obstacle. No speaker enters it.
    `board` (B24.06) is the board's leverage (`_lever`): added to the leverage and to nothing else, so no favourable term lowers the obstacle (A-25)."""
    D, r = inp.dials, inp.rite
    pool = pool_of(D["attribute_mid"], 0, D["pool_add"], D["pool_floor"])
    return pool, _record(inp, pool, D["attribute_mid"], D["track_step"] * track + board if board else D["track_step"] * track, r.difficulty,
                         (("gravity", r.gravity, 1.0),))


def p_carried(inp, track, board=0.0) -> float:
    """P(carried) of one adjudicator's draw at `track`: the closed form of the close at that track (`band_odds` on the same record the close
    rolls), Success or better. `board` is the standing board's leverage (`_lever`) where the close has one. Pure."""
    pool, x = close_record(inp, track, board)
    return _wsum(band_odds(pool, obstacle(x)[0], net_boost(x.leverage, pool))[CARRIED:])


def view_odds(inp, view) -> float:
    """what a chooser is shown (V2 p2 §E; B05.62): P(carried) before an ordinary bench at the track his believed mood implies, on the board's leverage as the close
    would read it (`View.lever`, `_lever`: one ladder with `_close` and `_judge_view`, R12); no true attribute and no true start of anyone enters it. A `consent` has no draw, so none."""
    # the mood is signed toward the mover's own side, the track toward `for`: so `_sg(side)` between them (a departure from the running model,
    # sc2/engine.py:899, which reads the mood as the track and so shows an `against` mover the odds of his own defeat)
    return 0.0 if inp.rite.close == "consent" else p_carried(inp, _sg(view.side) * view.mood * inp.dials["mood_scale"], view.lever)


def card_odds(inp) -> Optional[float]:
    """the card's odds (V2 p1 §E; A-133): P(carried) of THE CLOSE ITSELF in a sitting where nobody speaks, each who decides at his own `start`
    (bearing, the rig's presumption, an appeal's grounds, the bench as packed) less what the burden charges the bearer where he must put the
    matter and his rest is priced as silence. `bench`: the presiding seat's; `declared`: at least the quorum of the seats' own draws carry (the
    quorum-th best margin, no veto); `hearers`: the weight-mean margin. `None` where nothing is drawn (`consent`) or the verdict is the speech
    itself (`exchange`). Pure; the same closed form as `p_carried`, which a silent sitting's close samples, on the board that close reads (`_lever` of the opening
    sitting: the filed exhibits, and a resumed sitting's board)."""
    D, r = inp.dials, inp.rite
    if r.close in ("consent", "exchange"):
        return None
    ds, bearer = _seats(inp), lead(inp, r.bears)
    charged = bearer is not None and _reply(inp, _other(r.bears)) == "must"
    quiet = {d.id: d.start - (_sg(r.bears) * silence_cost(inp, d, None, bearer) if charged else 0.0) for d in ds}
    board = _lever(inp, start(inp))
    if r.close == "bench":
        return p_carried(inp, quiet[ds[0].id], board)
    if r.close == "declared":
        q = min(len(ds), r.quorum or 1)
        dist = [1.0]                                                    # P(k seats carry), seat by seat
        for d in ds:
            p = p_carried(inp, quiet[d.id], board)
            dist = [(dist[k] if k < len(dist) else 0.0) * (1.0 - p) + (dist[k - 1] * p if k > 0 else 0.0) for k in range(len(dist) + 1)]
        return _wsum(dist[q:])
    pool, x = close_record(inp, 0.0)
    W = _wsum(d.weight for d in ds)
    mu = MU_PER_DIE * pool - obstacle(x)[0] + _wsum(d.weight * net_boost(D["track_step"] * quiet[d.id] + board, pool) for d in ds) / W
    sd = SD_PER_DIE * math.sqrt(pool) * math.sqrt(_wsum(d.weight ** 2 for d in ds)) / W
    return 1.0 - phi(((dice_engine.BAND_FLOORS["success"] - 0.5) / dice_engine.MARGIN_SCALE - mu) / sd)    # the ladder's edge for Success, as `band_odds` reads it


def _judge_view(inp, st, d, track) -> JudgeView:
    """what a played adjudicator has at the close (V2 p2 §D): his own track and its odds, the points as they stood, and what his Attunement
    perceives of each participant: `(who, insincerity, discomfort)`, each scaled by how well he reads (0..1 across the attribute scale)."""
    D = inp.dials
    read = (d.attunement - D["attribute_floor"]) / (D["attribute_ceiling"] - D["attribute_floor"])
    cond = _d(st.cond)
    tells = tuple((p.id, round(read * max(0.0, -_sg(p.side) * p.believes), 2),
                   round(read * min(1.0, cond[p.id].strain + 0.5 * cond[p.id].rattles), 2))     # [ASSUMPTION; Jordan to correct: discomfort is strain plus half a rattle, as the running model reads it (sc2/engine.py:502)]
                  for p in inp.room if p.side and p.id != d.id)
    return JudgeView(d.id, track, p_carried(inp, track, _lever(inp, st)), tuple(st.points), tells)


def _abridged(inp, beats, margins=()) -> tuple:
    """the abridged act's one verdict: the one speech's margin with the one addressed, plus where he started (his net is his own `Margin` of
    that speech, its obstacle and terms his, his `start` added: a watcher seated after him never lends his). `margins` is the last exchange's,
    each hearer's; where the addressed man has none (the act was not a speech to him) the beat's margin and terms stand."""
    if not beats:
        raise ValueError("refused[close]: an abridged close reads the one speech's beat, and there is none")
    to = min((p for p in inp.room if p.decides and not p.side), key=lambda p: (-p.precedence, p.id))
    m = dict(margins).get(to.id)
    if m is not None:
        return ((to.id, Margin(net=m.net + to.start, ob=m.ob, terms=m.terms)),)
    b = beats[-1]
    ob = _wsum(v for _, v in b.terms)
    return ((to.id, Margin(net=b.margin + ob + to.start, ob=ob, terms=b.terms)),)


def _close(inp, st, rng, rulings=None, *, beats=(), margins=()) -> tuple:
    """THE CLOSE: `(verdicts, ruled)` (V2 p2 §D). `bench`, `declared` and `hearers` take ONE normal for each adjudicator, presiding seat first, and
    each verdict is `Margin(roll + the boost of his own track - the obstacle)`: a draw on his own track (A-14), never a band or a side. `bench`
    returns the presiding seat's alone, the other two every seat's; the host reads them (`declared` by the quorum-th best, `hearers` by the
    weight-mean). `consent` draws nothing and returns `()`: a party's accept is an act. `exchange` draws nothing: the one speech's margin
    with the one addressed plus his start (`beats`, and `margins`: the last exchange's, each hearer's). A played adjudicator (`rulings[id](JudgeView)`, called once, here) rules `"for"`, `"against"`
    or anything else to leave it to his draw, which is taken whatever he rules; `ruled` is how far each ruling departs from his own track."""
    r = inp.rite
    if r.close == "consent":
        return (), ()
    if r.close == "exchange":
        return _abridged(inp, beats, margins), ()
    T, seats, n0, out, ruled, board = _d(st.tracks), _seats(inp), rng.n, [], [], _lever(inp, st)
    for k, d in enumerate(seats):
        pool, x = close_record(inp, T[d.id], board)
        ob, terms = obstacle(x)
        net = _roll(pool, _z(rng)) + net_boost(x.leverage, pool)
        if (k == 0 or r.close != "bench") and rulings and d.id in rulings:
            how = rulings[d.id](_judge_view(inp, st, d, T[d.id]))
            if how in ("for", "against"):
                net = ob + _sg(how) * _RULING
                ruled.append((d.id, round(max(0.0, -_sg(how) * T[d.id]), 2)))
        out.append((d.id, Margin(net=net, ob=ob, terms=terms)))
    assert rng.n - n0 == 2 * len(seats), (rng.n - n0)    # a normal each (two uniforms: `Draw.normal`)
    return tuple(out[:1] if r.close == "bench" else out), tuple(ruled)


def proceed(inp: Input, rng, decide: Optional[Callable] = None, deciders: Optional[Mapping] = None, rulings: Optional[Mapping] = None) -> Outcome:
    """THE SITTING: `deciders[person]` (else `decide`) chooses for a speaker with `(view, person)`, and the automatic policy where there is
    none, so a played and an automatic man meet in one sitting; an abridged act (`close: exchange`) is one speech nobody watches and asks no
    callback. A resumed sitting (`inp.state`) continues the same sitting: the count of beats, the issue reached and the turns each has had.
    It ends `yielded`, `rested` or `budget` (see the head); `Outcome.ended_by` is who yielded."""
    r = inp.rite
    st, beats, ended_by, heard_by = start(inp), [], None, ()
    while st.ended is None:
        able = _able(inp, st)
        if not able:
            break
        lo = min(_d(st.cond)[p.id].spoken for p in able)
        round_, rests = [p for p in able if _d(st.cond)[p.id].spoken == lo], 0
        for _ in round_:
            me = who(inp, _mover(inp, st))
            n0 = rng.n
            v = view(inp, st, me, rng)
            fn = None if r.close == "exchange" else (deciders or {}).get(me.id, decide)
            ch, frame = _taken(inp, st, v, me, fn(v, me) if fn else policy(inp, v, me))
            st, beat, heard_by = _exchange(inp, st, me, ch, rng, frame)
            _took(inp, rng, n0)
            beats.append(beat)
            rests += _move(inp, ch.move)[0] == "none"
            if st.ended:
                ended_by = me.id
                break
        if st.ended is None and rests == len(round_):
            st = replace(st, ended="rested")
    st = replace(st, ended=st.ended or "budget")
    verdicts, ruled = _close(inp, st, rng, rulings, beats=tuple(beats), margins=heard_by)
    return Outcome(tuple(beats), st, st.ended, ended_by, verdicts, ruled, tuple(_standing(inp, st.board)), tuple(f for f, _ in st.faults))
