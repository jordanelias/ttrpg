"""`modules/social_contest/proceeding.py` as RD A.4-A.6, B.1-B.9 and PLAN B24p.07-.12/.14 state it.

The module holds no roster and no state; it reads only `inp` (records.py) and `inp.dials`. Every place a choice had
to be made cites its SPEC_GAPS id. Draw discipline (RD A.4 / B24p.10): each exchange takes EXACTLY G+5 normals in the
order [reading roll, xi per ground (G), xi_0 strain, hold, speech, steadiness]; each balloted decider EXACTLY three
[hold, detection, ballot]; both asserted.
"""
from __future__ import annotations

import math
from dataclasses import replace
from types import SimpleNamespace
from typing import Callable, Optional

from .dice import (Margin, SocialContestInput, band_odds, degree, even_line, level, net_boost, obstacle,
                   p_at_least, pool_of, roll, roll_net_continuous, weighted_tenth)
from .records import (Choice, Exchange, ExchangeView, ProceedingInput, ProceedingOutcome, ProceedingState,
                      SideState)

SIGN = {"for": 1.0, "against": -1.0}


def _clamp(x, lo, hi):
    return max(lo, min(hi, x))


def _pair(x):
    """a signed sigma as the (for, against) pair every source returns (B05.10's signed channel)."""
    return (max(x, 0.0), max(-x, 0.0))


def _net(levels, name):
    for src, f, a in levels:
        if src == name:
            return f - a
    return 0.0


def _rank(S, skill):
    return dict(S.ranks).get(skill, 0) if skill else 0


def _moves(inp, side):
    return dict(inp.type.moves).get(side, ())


def _move_by_id(inp, mid):
    for _, ms in inp.type.moves:
        for m in ms:
            if m.id == mid:
                return m
    raise KeyError(mid)


def _even(D):
    return even_line(D["pool_add"])


def _P(D, score):
    """a bare attribute pool: `pool_of(attr, 0, pool_add, pool_floor)` (B.1 hold, B.6 steadiness, B.9 draws)."""
    return pool_of(score, 0, D["pool_add"], D["pool_floor"])


# ---------------------------------------------------------------- targets (RD A.4 `_target`; B.3 the body)
_TFIELDS = ("score", "will", "grace", "attunement", "reason", "focus")


def _as_target(p, weight=1):
    return SimpleNamespace(id=p.id, weight=getattr(p, "weight", weight), moved_by=dict(p.moved_by),
                           **{f: getattr(p, f) for f in _TFIELDS})


def _mean_target(people):
    """RD A.4: "the weight-mean of `deciders`; else the weight-mean of `hearers`". Every numeric field and the
    moved_by vector weight-meaned (G20: the spec names the mean, not which fields)."""
    W = float(sum(p.weight for p in people))
    mb = {}
    for p in people:
        for g, v in p.moved_by:
            mb[g] = mb.get(g, 0.0) + p.weight * v / W
    return SimpleNamespace(id="+".join(p.id for p in people), weight=W, moved_by=mb,
                           **{f: sum(p.weight * getattr(p, f) for p in people) / W for f in _TFIELDS})


def _other(inp, i):
    for j in range(len(inp.speakers)):
        if j != i:
            return j
    return None


def _target(inp, i):
    """RD A.4: T is "the other side's lead, where the rite gives `against` a move; else the weight-mean of
    `deciders`; else the weight-mean of `hearers`". Returns (T, index of T among speakers or None)."""
    j = _other(inp, i)
    if j is not None and _moves(inp, "against"):
        return _as_target(inp.speakers[j]), j
    if inp.deciders:
        return _mean_target(inp.deciders), None
    return _mean_target(inp.hearers), None


def _body(inp, i):
    """B.3: `fit_body` is over "the deciders an argument addresses"; B24p.08: `target:` blurs "the weight-mean vector
    of the persons an argument addresses". G22: the mover is excluded when he is himself a decider (conversation,
    questioning: the `against` speaker is balloted); empty -> hearers; empty -> the other speaker (negotiation)."""
    me = inp.speakers[i].id
    ds = [d for d in inp.deciders if d.id != me]
    if ds:
        return ds
    hs = [h for h in inp.hearers if h.id != me]
    if hs:
        return hs
    j = _other(inp, i)
    return [_as_target(inp.speakers[j])] if j is not None else []


# ---------------------------------------------------------------- the roles' scalars (B24p.07 item 2)
def _heard(S, room, typ, D):
    # RD B.4: 1.0 if written_only, else clamp(1 - heard_step * max(0, attention - presence), heard_floor, 1)
    if typ.order == "written_only":
        return 1.0
    return _clamp(1.0 - D["heard_step"] * max(0.0, room.attention - S.presence), D["heard_floor"], 1.0)


def _shield(S, D):
    # RD B.6 c: min(shield_max, shield_step * (will - FLOOR))
    return min(D["shield_max"], D["shield_step"] * (S.will - D["attribute_floor"]))


def _account(S, D):
    # RD B.2 c: min(account_max, account_step * (reason - FLOOR))
    return min(D["account_max"], D["account_step"] * (S.reason - D["attribute_floor"]))


def _cover(P, D):
    # RD B.5 c: min(cover_max, cover_step * (grace - FLOOR))
    return min(D["cover_max"], D["cover_step"] * (P.grace - D["attribute_floor"]))


def _k(inp, move, ground):
    """B24p.07 item 3: c = ground_reason[ground] for a move with `ground: true`, else move.reason_weight;
    k = min(10, max(0, round(10 c) + round(10 reason_bias)))."""
    c = dict(inp.ground_reason)[ground] if move.ground else move.reason_weight
    return min(10, max(0, round(10 * c) + round(10 * inp.type.reason_bias)))


def _blend(inp, S, move, ground):
    k = _k(inp, move, ground)
    return weighted_tenth((S.reason, S.presence), (k, 10 - k))


# ---------------------------------------------------------------- fit (RD B.3; B24p.08 item 1)
def _fit(v: dict, g: str) -> float:
    vals = list(v.values())
    if not vals:
        return 0.0
    mean = sum(vals) / len(vals)
    mx, mn = max(vals), min(vals)
    if mx == mn:
        return 0.0                                  # "0 if v is flat"
    if v.get(g, 0.0) >= mean:
        return (v[g] - mean) / (mx - mean)
    return (v[g] - mean) / (mean - mn)


def _fit_body(targets, g):
    W = sum(t.weight for t in targets)
    if W == 0:
        return 0.0
    return sum(t.weight * _fit(dict(t.moved_by), g) for t in targets) / W


# ---------------------------------------------------------------- LEVERAGE / TERMS (B24p.07 item 1)
# signature: fn(S, s, T, room, typ, move, ground, D, inp, i) -> (for, against)
def _lev_delivery(S, s, T, room, typ, move, ground, D, inp, i):
    # RD B.4: delivery_step * (presence - mid) * 2 * (1 - proof_weight); 0 if written_only
    if typ.order == "written_only":
        return (0.0, 0.0)
    return _pair(D["delivery_step"] * (S.presence - D["attribute_mid"]) * 2.0 * (1.0 - room.proof_weight))


def _lev_fit(S, s, T, room, typ, move, ground, D, inp, i):
    # RD B.3 fit source on the TRUE vectors, for a move with fit: true (B24p.08 item 3)
    if not move.fit or ground is None:
        return (0.0, 0.0)
    fb = _fit_body(_body(inp, i), ground)
    return (level(D["fit_level"]) * max(fb, 0.0), level(D["misfit_level"]) * max(-fb, 0.0))


def _lev_respect(S, s, T, room, typ, move, ground, D, inp, i):
    # RD B.5 b: (max(esteem, 0), max(-esteem, 0))
    return _pair(s.esteem)


def _lev_marks(S, s, T, room, typ, move, ground, D, inp, i):
    # RD B.5 c: (0, marks * level(mark_level) * (1 - cover))
    return (0.0, s.marks * level(D["mark_level"]) * (1.0 - _cover(S, D)))


def _lev_resist(S, s, T, room, typ, move, ground, D, inp, i):
    # RD B.6 d: r = resist_step * (target.<resisted_by> - mid); (max(-r,0), max(r,0))
    attr = getattr(T, move.resisted_by or "will")
    r = D["resist_step"] * (attr - D["attribute_mid"])
    return (max(-r, 0.0), max(r, 0.0))


LEVERAGE = {"delivery": _lev_delivery, "fit": _lev_fit, "respect": _lev_respect, "marks": _lev_marks,
            "resist": _lev_resist}


def _term_off_topic(S, typ, D, on_topic):
    return (0.0 if on_topic else 1.0, D["off_topic_step"])


def _term_venue_standard(S, typ, D, on_topic):
    return (max(0.0, typ.standard - S.grace), D["standard_step"])


TERMS = {"off_topic": _term_off_topic, "venue_standard": _term_venue_standard}   # B24p.05 appends in this order


def _proofs_source(S, room, D):
    """B24p.07 item 4: (level(proof_level) * min(S.proofs, cap) * 2 * proof_weight, 0.0), cap = proofs_per_reason *
    reason or none when None; at None S.proofs is read through B05.17's whole-unit rule int(proofs + 0.5)."""
    if D["proofs_per_reason"] is None:
        usable = int(S.proofs + 0.5)
    else:
        usable = min(S.proofs, D["proofs_per_reason"] * S.reason)
    return (level(D["proof_level"]) * usable * 2.0 * room.proof_weight, 0.0)


# ---------------------------------------------------------------- the speech (B24p.07 items 4-6; RD B.7)
def _speech_input(inp, i, s, T, move, ground, on_topic):
    """Returns (SocialContestInput, levels, pool_before_heard, heard)."""
    D, S, typ, room = inp.dials, inp.speakers[i], inp.type, inp.room
    case = _blend(inp, S, move, ground) + _rank(S, move.capability)
    pre = pool_of(case, S.addends, D["pool_add"], D["pool_floor"])
    h = _heard(S, room, typ, D)
    pool = pre * h
    shield, account = _shield(S, D), _account(S, D)
    ops = []
    for name, raw, step, eased_by in S.operands:
        if eased_by == "reason" and name in S.accounts:
            step = step * (1.0 - account)
        elif eased_by == "will":
            step = step * (1.0 - shield)
        ops.append((name, raw, step))
    for name, fn in TERMS.items():
        raw, step = fn(S, typ, D, on_topic)
        ops.append((name, raw, step))
    levels = list(S.levels)
    levels.append(("proofs",) + _proofs_source(S, room, D))
    for name, fn in LEVERAGE.items():
        levels.append((name,) + fn(S, s, T, room, typ, move, ground, D, inp, i))
    sig = sum(f for _, f, _ in levels) - sum(a for _, _, a in levels) * (1.0 - shield)
    x = SocialContestInput(pool=pool, opposition=T.score, leverage=sig, difficulty=typ.difficulty + move.difficulty,
                           obstacle_operands=tuple(ops), pool_default=D["pool_default"], pool_add=D["pool_add"],
                           opposition_rate=D["opposition_rate"], obstacle_ceiling=D["obstacle_ceiling"],
                           ceiling_per_pool=D["ceiling_per_pool"],
                           obstacle_refusal_multiple=D["obstacle_refusal_multiple"])
    return x, tuple(levels), pre, h


def exchange_odds(inp, state, mover_i, choice) -> tuple:
    """B24p.07 item 6 (pure): band_odds(x.pool, obstacle(x)[0], net_boost(x.leverage, x.pool)), on_topic=True."""
    s = state.sides[mover_i]
    T, _ = _target(inp, mover_i)
    move = _move_by_id(inp, choice.move)
    x, _, _, _ = _speech_input(inp, mover_i, s, T, move, choice.ground, True)
    return band_odds(x.pool, obstacle(x)[0], net_boost(x.leverage, x.pool))


# ---------------------------------------------------------------- the reading (RD B.3; B24p.08 item 2)
def _read(inp, i, state, rng) -> tuple:
    """Draws 1 + G + 1 normals: the reading's roll, one xi per ground, one xi_0 for the other side's strain."""
    D, S = inp.dials, inp.speakers[i]
    j = _other(inp, i)
    Pa = _P(D, S.attunement + _rank(S, "insight"))
    if j is not None:
        guard = inp.speakers[j].grace
    else:                                    # B24p.08: "the weight-mean `grace` of the deciders for a one-speaker type"
        pool = list(inp.deciders) or list(inp.hearers)
        guard = sum(p.weight * p.grace for p in pool) / sum(p.weight for p in pool)
    net = roll_net_continuous(Pa, rng=rng)
    read = net + net_boost(-D["guard_step"] * (guard - D["attribute_mid"]), Pa) - (_even(D) + D["read_ob"])
    acc = (1.0 + math.tanh(read / D["read_scale"])) / 2.0        # fmath.tanh (B06.02) -> math.tanh (G16)
    blur = D["read_blur"] * (1.0 - acc)
    xis = [rng.normal(0.0, 1.0) for _ in inp.grounds]
    xi0 = rng.normal(0.0, 1.0)
    body = _body(inp, i)
    W = sum(t.weight for t in body) or 1.0
    tv = {g: sum(t.weight * dict(t.moved_by).get(g, 0.0) for t in body) / W for g in inp.grounds}
    out = [("acc", acc)]
    for g, xi in zip(inp.grounds, xis):
        out.append(("target:" + g, _clamp(tv[g] + blur * xi, 0.0, 1.0)))
    if j is not None:
        ov = dict(inp.speakers[j].moved_by)
        for g, xi in zip(inp.grounds, xis):          # "both use the same xi per ground"
            out.append(("other:" + g, _clamp(ov.get(g, 0.0) + blur * xi, 0.0, 1.0)))
    t_strain = state.sides[j].strain if j is not None else 0.0
    out.append(("strain", max(0.0, t_strain + blur * xi0)))
    return tuple(out)


# ---------------------------------------------------------------- the hold (RD B.1; B24p.09)
def _hold(inp, i, s, move, rng) -> bool:
    """One normal, always taken, before any comparison. pull = s.pull + distraction + (deceive_pull if move.holds)."""
    D, S = inp.dials, inp.speakers[i]
    pull = s.pull + inp.room.distraction + (D["deceive_pull"] if move.holds else 0.0)
    net = roll_net_continuous(_P(D, S.focus), rng=rng)
    return pull <= 0 or net - (_even(D) + pull) >= 0


# ---------------------------------------------------------------- one exchange (RD A.4; B24p.10)
def _exchange(inp, state, i, choice, rng):
    """Returns (state', Exchange, Margin or None, track delta). The reading was drawn by the caller (B24p.10)."""
    D, S, typ = inp.dials, inp.speakers[i], inp.type
    move = _move_by_id(inp, choice.move)
    sides = list(state.sides)
    s = sides[i]
    T, j = _target(inp, i)
    t = sides[j] if j is not None else None
    on_topic = _hold(inp, i, s, move, rng)                                  # normal G+3
    m = None
    levels, terms, margin = (), (), 0.0
    if move.draw:
        x, levels, _, _ = _speech_input(inp, i, s, T, move, choice.ground, on_topic)
        m = roll(x, rng)                                                    # normal G+4
        margin, terms = m.net - m.ob, m.terms
    else:
        rng.normal()                                                        # normal G+4, taken, unused
    sign = SIGN[S.side]
    track = state.track
    clip = D["track_clip"]
    blow, marked = 0.0, False
    steady_taken = False
    if move.effect == "track" and m is not None:
        track = _clamp(track + sign * _clamp(margin, -clip, clip), -clip, clip)
    elif move.effect == "strike" and m is not None:
        if margin >= 0 and t is not None:
            Tsp = inp.speakers[j]
            aim = 1.0 + D["sore_gain"] * dict(Tsp.moved_by).get(choice.ground, 0.0)
            blow = D["blow_gain"] * (D["press_base"] + margin) * aim
            steady = roll_net_continuous(_P(D, Tsp.will), rng=rng) - (_even(D) + t.strain + blow)   # normal G+5
            steady_taken = True
            if steady < 0:
                marked = True
                t = replace(t, marks=t.marks + 1, strain=0.0, resolve=t.resolve - D["mark_resolve"],
                            pull=t.pull + D["rattle_pull"],
                            esteem=t.esteem - D["mark_shame"] * (1.0 - _cover(Tsp, D)))
            else:
                t = replace(t, strain=t.strain + D["strain_carry"] * blow)
        elif margin < 0:
            s = replace(s, esteem=s.esteem - D["press_rebound"])
    elif move.effect == "pull" and m is not None:
        if margin >= 0 and t is not None:
            t = replace(t, pull=t.pull + D["divert_pull"] + D["divert_gain"] * margin)
    elif move.effect == "yield":
        track = _clamp(track - sign * D["concede_step"], -clip, clip)     # clamp: G23
        s = replace(s, resolve=s.resolve + 1.0)
    if not steady_taken:
        rng.normal()                                                        # normal G+5, taken, unused
    s = replace(s, resolve=s.resolve - (1.0 if move.draw else 0.0), pull=0.0,
                strikes=s.strikes + (0 if on_topic else 1))                # off-topic rest counts: G24
    sides[i] = s
    if t is not None:
        sides[j] = t
    ex = Exchange(n=state.n + 1, mover=S.id, move=move.id, ground=choice.ground, on_topic=on_topic,
                  margin=margin, terms=terms, levels=levels, strain=blow, marked=marked)
    new = replace(state, n=state.n + 1, track=track, sides=tuple(sides))
    return new, ex, m, track - state.track


# ---------------------------------------------------------------- the sitting (RD A.5, A.6; B24p.11)
def _start(inp) -> ProceedingState:
    if inp.state is not None:
        return inp.state
    D = inp.dials
    sides = []
    for S in inp.speakers:
        r0 = (inp.type.exchanges[1] if D["resolve_base"] is None
              else D["resolve_base"] + D["resolve_per_will"] * S.will)
        sides.append(SideState(id=S.id, strain=S.strain, marks=0, resolve=r0, pull=0.0, strikes=0,
                               esteem=D["respect_step"] * (S.grace - D["attribute_mid"]), read=()))
    return ProceedingState(n=0, track=0.0, issue=inp.issue, sides=tuple(sides))


def _legal(inp, state, i, spoken) -> tuple:
    """B24p.11 item 3: rest ALONE when resolve <= 0 or effort spent; else the rite's moves for his side."""
    S, s = inp.speakers[i], state.sides[i]
    if s.resolve <= 0 or S.effort - spoken[i] <= 0:
        return ("rest",)
    return tuple(m.id for m in _moves(inp, S.side))


def _can_move(inp, state, i, spoken):
    return _legal(inp, state, i, spoken) != ("rest",)


def _mover(inp, state, spoken, last) -> Optional[int]:
    """B24p.11 item 2. G01: `single` read as `free`. G25: "in turn" = the next speaker after the last mover in the
    order's cycle, skipping one who can only rest."""
    n = len(inp.speakers)
    able = [i for i in range(n) if _can_move(inp, state, i, spoken)]
    if not able:
        return None
    order = inp.type.order
    if order in ("free", "written_only", "single"):
        return min(able, key=lambda i: (-(inp.speakers[i].effort - spoken[i]),
                                        0 if inp.speakers[i].side == "for" else 1, i))
    if order in ("alternating", "scripted"):
        cyc = sorted(range(n), key=lambda i: (0 if inp.speakers[i].side == "for" else 1, i))
    elif order == "rank":
        cyc = sorted(range(n), key=lambda i: (-inp.speakers[i].precedence, inp.speakers[i].id))
    else:
        raise ValueError(f"order {order!r}")
    start = 0 if last is None else (cyc.index(last) + 1)
    for k in range(n):
        i = cyc[(start + k) % n]
        if i in able:
            return i
    return None


def _argmax(reading, prefix, grounds):
    r = dict(reading)
    keys = [g for g in grounds if prefix + g in r]
    if not keys:
        return None
    return max(keys, key=lambda g: (r[prefix + g], -grounds.index(g)))   # ties to roster order


def _auto(inp, state, i, reading, spoken) -> Choice:
    """B24p.11 item 4 (RD A.6). Reads effects, never ids."""
    D, S = inp.dials, inp.speakers[i]
    legal = [_move_by_id(inp, mid) for mid in _legal(inp, state, i, spoken)]
    grounds = list(inp.grounds)
    g_t = _argmax(reading, "target:", grounds)
    tracks = [m for m in legal if m.effect == "track"]
    strikes = [m for m in legal if m.effect == "strike"]
    behind = SIGN[S.side] * state.track < 0
    if tracks and behind and strikes:
        mv = strikes[0]
        g_o = _argmax(reading, "other:", grounds) or g_t
        p_land = 1.0 - exchange_odds(inp, state, i, Choice(mv.id, g_o))[0]   # true record: G26
        r = dict(reading)
        blow = D["blow_gain"] * (D["press_base"] + 1.0) * (1.0 + D["sore_gain"] * r.get("other:" + g_o, 0.0))
        steady_odds = p_at_least(_P(D, D["attribute_mid"]), _even(D) + r["strain"] + blow)
        if p_land * (1.0 - steady_odds) >= D["press_at"]:
            return Choice(mv.id, g_o)
    if tracks:
        return Choice(tracks[0].id, g_t if tracks[0].ground else None)
    mv = legal[0]
    return Choice(mv.id, g_t if mv.ground else None)


def _yielded_side(inp, state, spoken):
    """B24p.11 item 5: "a side with `resolve <= 0` whose opposite still has resolve and effort" (the concede-the-last-
    issue clause is inert while `issue` is None)."""
    if len(inp.speakers) < 2:
        return None
    for i, s in enumerate(state.sides):
        j = _other(inp, i)
        o = state.sides[j]
        if s.resolve <= 0 and o.resolve > 0 and inp.speakers[j].effort - spoken[j] > 0:
            return i
    return None


def proceed(inp: ProceedingInput, rng, decide: Optional[Callable] = None) -> ProceedingOutcome:
    D, typ = inp.dials, inp.type
    G = len(inp.grounds)
    state = _start(inp)
    exchanges, margins, deltas = [], [], []
    spoken = [0] * len(inp.speakers)
    last, ended, ended_side = None, None, None
    rests_in_a_row = 0
    while state.n < typ.exchanges[1]:
        i = _mover(inp, state, spoken, last)
        if i is None:
            ended = "rested"
            break
        c0 = rng.count
        reading = _read(inp, i, state, rng)                                 # normals 1 .. G+2
        sides = list(state.sides)
        sides[i] = replace(sides[i], read=reading)
        state = replace(state, sides=tuple(sides))
        legal = _legal(inp, state, i, spoken)
        if decide is not None:
            view = ExchangeView(n=state.n, mover=inp.speakers[i].id, legal=legal, own=state.sides[i], read=reading,
                                track_sign=(state.track > 0) - (state.track < 0), issue=state.issue)
            choice = decide(view)
        else:
            choice = _auto(inp, state, i, reading, spoken)
        if choice.move not in legal:
            raise ValueError(f"{inp.speakers[i].id}: move {choice.move!r} not legal ({legal})")
        state, ex, m, delta = _exchange(inp, state, i, choice, rng)
        assert rng.count - c0 == G + 5, (rng.count - c0, G + 5)            # RD A.4: G + 5 normals, used or not
        exchanges.append(ex)
        margins.append(m)
        deltas.append(delta)
        spoken[i] += 1                                                      # every exchange spends effort: G28
        last = i
        rests_in_a_row = rests_in_a_row + 1 if choice.move == "rest" else 0
        # the ends, in the plan's order (B24p.11 item 5): broken, struck, yielded, budget
        if D["break_at"] is not None and any(s.marks >= D["break_at"] for s in state.sides):
            ended = "broken"
            ended_side = next(k for k, s in enumerate(state.sides) if s.marks >= D["break_at"])
            break
        if typ.struck_ends and typ.strikes >= 1 and any(s.strikes >= typ.strikes for s in state.sides):
            ended = "struck"
            break
        y = _yielded_side(inp, state, spoken)
        if y is not None:
            ended, ended_side = "yielded", y
            break
        if rests_in_a_row >= len(inp.speakers):    # RD A.5 "every side rests in turn" (G21; the plan omits it)
            ended = "rested"
            break
    if ended is None:
        ended = "budget"
    verdicts, blv = _close(inp, state, ended, ended_side, tuple(exchanges), margins, deltas, rng)
    return ProceedingOutcome(exchanges=tuple(exchanges), state=state, ended=ended, verdicts=verdicts,
                             ballot_levels=blv)


# ---------------------------------------------------------------- the close (RD A.5, B.9; B24p.12)
def _side_of(inp, pid):
    for S in inp.speakers:
        if S.id == pid:
            return S.side
    raise KeyError(pid)


def _last_divert(inp, exchanges, margins):
    for k in range(len(exchanges) - 1, -1, -1):
        mv = _move_by_id(inp, exchanges[k].move)
        if mv.effect == "pull" and margins[k] is not None and exchanges[k].margin >= 0:
            return k
    return None


def _p_div(inp, exchanges, margins):
    D = inp.dials
    k = _last_divert(inp, exchanges, margins)
    if k is None:
        return 0.0, None
    return D["divert_pull"] + D["divert_gain"] * exchanges[k].margin, k


def _ballot_sense(inp, d, exchanges):
    """RD B.9 (i)."""
    D, room = inp.dials, inp.room
    mid, pw = D["attribute_mid"], room.proof_weight
    pw_d = _clamp(pw + D["sense_step"] * (d.reason - mid), 0.0, 1.0)
    delta = pw_d - pw
    T = [x for x in exchanges if _move_by_id(inp, x.move).effect == "track" and x.levels]
    if not T or delta == 0.0:
        return 0.0
    acc = 0.0
    for x in T:
        S = next(sp for sp in inp.speakers if sp.id == x.mover)
        mv = _move_by_id(inp, x.move)
        q = _net(x.levels, "proofs") / (2.0 * pw)
        mm = _net(x.levels, "delivery") / (2.0 * (1.0 - pw)) + _net(x.levels, "respect")
        r = D["delivery_step"] * (_k(inp, mv, x.ground) / 10.0) * (S.reason - mid)
        acc += SIGN[S.side] * (q + r - mm)
    return 2.0 * delta * acc / len(T)


def _ballot_relevance(inp, state, d, exchanges, margins, deltas, hold_d):
    """RD B.9 (ii); n(side) = max(0, strikes - k + 1) with k >= 1."""
    D, typ = inp.dials, inp.type
    f_d = _clamp(1.0 + D["relevance_step"] * (d.focus - D["attribute_mid"]), 0.0, 2.0)
    k = typ.strikes
    n = {"for": 0, "against": 0}
    if k >= 1:
        for S, s in zip(inp.speakers, state.sides):
            n[S.side] += max(0, s.strikes - k + 1)
    base = f_d * level(D["strike_level"]) * (n["against"] - n["for"])
    p_div, kd = _p_div(inp, exchanges, margins)
    lost = 0.0
    if hold_d < 0 and p_div > 0 and kd is not None:
        diverted = _side_of(inp, exchanges[kd].mover)
        diverted = "against" if diverted == "for" else "for"
        for q in range(kd + 1, len(exchanges)):
            if _side_of(inp, exchanges[q].mover) == diverted:
                lost = deltas[q]
                break
    return base - D["track_step"] * lost


def _ballot_sincerity(inp, exchanges, seen):
    """RD B.9 (iii)."""
    if not seen:
        return 0.0
    ployed = {"for": 0, "against": 0}
    for x in exchanges:
        if _move_by_id(inp, x.move).ploy:
            ployed[_side_of(inp, x.mover)] = 1
    return level(inp.dials["ploy_level"]) * (ployed["against"] - ployed["for"])


BALLOT = {"sense": _ballot_sense, "relevance": _ballot_relevance, "sincerity": _ballot_sincerity}


def _end_levels(inp, ended, ended_side):
    """toward `for`: a yield or a break by `for` counts against `for` (RD A.5: - end_levels(for) + end_levels(against))."""
    D = inp.dials
    if ended == "yielded" and ended_side is not None:
        lv = level(D["yield_level"])
    elif ended == "broken" and ended_side is not None:
        lv = level(D["break_level"])
    else:
        return 0.0
    return -lv if inp.speakers[ended_side].side == "for" else lv


def _ballot_input(inp, state, d, ended, ended_side, exchanges, margins, deltas, hold_d, seen):
    """B24p.12 item 1. Returns (SocialContestInput, levels)."""
    D, typ = inp.dials, inp.type
    sense = BALLOT["sense"](inp, d, exchanges)
    relevance = BALLOT["relevance"](inp, state, d, exchanges, margins, deltas, hold_d)
    sincerity = BALLOT["sincerity"](inp, exchanges, seen)
    pres = {"for": 1.0, "against": -1.0, "none": 0.0}[typ.presumes] * level(D["presumption_level"])
    ends = _end_levels(inp, ended, ended_side)
    resist = D["resist_step"] * (d.will - D["attribute_mid"])          # scalar subtraction: G04
    track_term = D["track_step"] * state.track
    lev = track_term + sense + relevance + sincerity + d.lean + level(d.modifier) + pres + ends - resist
    levels = (("track", track_term), ("sense", sense), ("relevance", relevance), ("sincerity", sincerity),
              ("lean", d.lean), ("modifier", level(d.modifier)), ("presumption", pres), ("ends", ends),
              ("resist", -resist))
    x = SocialContestInput(pool=d.pool, opposition=d.score, leverage=lev, difficulty=typ.difficulty,
                           obstacle_operands=(("stakes", typ.stakes, 1.0),), pool_default=D["pool_default"],
                           pool_add=D["pool_add"], opposition_rate=D["opposition_rate"],
                           obstacle_ceiling=D["obstacle_ceiling"], ceiling_per_pool=D["ceiling_per_pool"])
    return x, levels


def _close(inp, state, ended, ended_side, exchanges, margins, deltas, rng):
    D, disp = inp.dials, inp.type.disposal
    if disp == "exchange":
        last = next((m for m in reversed(margins) if m is not None), None)
        return ((inp.deciders[0].id, last),), ()
    if disp in ("none", "mutual") or ended == "adjourned":
        return (), ()
    p_div, _ = _p_div(inp, exchanges, margins)
    out, blv = [], []
    for d in sorted(inp.deciders, key=lambda d: d.id):                      # id order (G31)
        c0 = rng.count
        hold_d = roll_net_continuous(_P(D, d.focus), rng=rng) - (_even(D) + inp.room.distraction + p_div)
        seen = roll_net_continuous(_P(D, d.attunement), rng=rng) - (_even(D) + D["ploy_ob"]) >= 0
        x, lv = _ballot_input(inp, state, d, ended, ended_side, exchanges, margins, deltas, hold_d, seen)
        m = roll(x, rng)
        assert rng.count - c0 == 3, rng.count - c0                         # RD B.9: three normals per decider
        out.append((d.id, m))
        blv.append((d.id, lv))
    return tuple(out), tuple(blv)


def closing_odds(inp, state, exchanges=(), margins=None, deltas=None) -> tuple:
    """B24p.12 item 2 (pure). G32: the plan's signature (inp, state) cannot see the exchanges `sense` and `lost`
    read (ProceedingState holds none), so they are passed optionally; `ended="budget"`."""
    D = inp.dials
    margins = margins if margins is not None else [None if not x.levels else Margin(0, 0) for x in exchanges]
    deltas = deltas if deltas is not None else [0.0] * len(exchanges)
    p_div, _ = _p_div(inp, exchanges, margins)
    out = []
    for d in sorted(inp.deciders, key=lambda d: d.id):
        p_fail = 1.0 - p_at_least(_P(D, d.focus), _even(D) + inp.room.distraction + p_div)
        p_seen = p_at_least(_P(D, d.attunement), _even(D) + D["ploy_ob"])
        shares = [0.0] * 4
        for hold_fails, ph in ((True, p_fail), (False, 1.0 - p_fail)):
            for seen, ps in ((True, p_seen), (False, 1.0 - p_seen)):
                x, _ = _ballot_input(inp, state, d, "budget", None, exchanges, margins, deltas,
                                     -1.0 if hold_fails else 1.0, seen)
                bo = band_odds(x.pool, obstacle(x)[0], net_boost(x.leverage, x.pool))
                for b in range(4):
                    shares[b] += ph * ps * bo[b]
        out.append((d.id, tuple(shares)))
    return tuple(out)


# ---------------------------------------------------------------- the host's read (PLAN B24p.14 item 2)
_RANK = {"failure": 0, "partial": 1, "success": 2, "overwhelming": 3}


def act_margin(outcome, typ, inp=None):
    """B24p.14 item 2. G33: `hearers` needs the deciders' weights and `none`/`mutual` need the `for` speaker's id,
    neither of which `(outcome, type)` carries, so `inp` is passed."""
    if outcome.ended == "adjourned":
        return None, False
    disp = typ.disposal
    if disp in ("exchange", "bench"):
        return (outcome.verdicts[0][1] if outcome.verdicts else None), False
    if disp == "declared":
        if not outcome.verdicts:
            return None, False
        n_ok = sum(1 for _, m in outcome.verdicts if _RANK[degree(m)] >= 2)
        return outcome.verdicts[0][1], (typ.quorum is not None and n_ok < typ.quorum)
    if disp == "hearers":
        w = {d.id: d.weight for d in inp.deciders}
        W = sum(w[i] for i, _ in outcome.verdicts)
        return Margin(net=sum(w[i] * m.net for i, m in outcome.verdicts) / W,
                      ob=sum(w[i] * m.ob for i, m in outcome.verdicts) / W), False
    # none, mutual: the last exchange drawn by the act's actor (the `for` speaker)
    for_id = next(S.id for S in inp.speakers if S.side == "for")
    for x in reversed(outcome.exchanges):
        if x.mover == for_id and x.terms:
            ob = sum(v for _, v in x.terms)
            return Margin(net=x.margin + ob, ob=ob, terms=x.terms), False
    return None, False
