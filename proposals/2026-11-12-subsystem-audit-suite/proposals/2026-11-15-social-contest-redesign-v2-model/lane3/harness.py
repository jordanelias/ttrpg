"""Lane 3 harness: a copy of scmodel.proceeding.proceed's loop that calls a per-side POLICY with full access
(inp, state, i, reading, spoken, legal) instead of decide(view), so a fixed strategy can face the automatic policy.
Verified identical to proceed(decide=None) when both policies are `auto` (control, see check_identity)."""
from __future__ import annotations

import math
import random
import sys
from collections import Counter
from dataclasses import replace

sys.path.insert(0, __file__.rsplit("/lane3/", 1)[0])
import scmodel  # noqa: F401,E402
from scmodel import dials as dialmod, proceeding as P  # noqa: E402
from scmodel.dice import degree  # noqa: E402
from scmodel.host import build_input  # noqa: E402
from scmodel.records import Choice, ProceedingOutcome  # noqa: E402
from scmodel.rng import draw  # noqa: E402

ATTRS = ("focus", "reason", "attunement", "presence", "grace", "will")


def proceed2(inp, rng, policies):
    """policies: {speaker index: fn(inp, state, i, reading, spoken, legal) -> Choice}; missing -> auto."""
    D, typ = inp.dials, inp.type
    G = len(inp.grounds)
    state = P._start(inp)
    exchanges, margins, deltas = [], [], []
    spoken = [0] * len(inp.speakers)
    last, ended, ended_side = None, None, None
    rests = 0
    while state.n < typ.exchanges[1]:
        i = P._mover(inp, state, spoken, last)
        if i is None:
            ended = "rested"
            break
        c0 = rng.count
        reading = P._read(inp, i, state, rng)
        sides = list(state.sides)
        sides[i] = replace(sides[i], read=reading)
        state = replace(state, sides=tuple(sides))
        legal = P._legal(inp, state, i, spoken)
        pol = policies.get(i)
        choice = P._auto(inp, state, i, reading, spoken) if pol is None else pol(inp, state, i, reading, spoken, legal)
        if choice.move not in legal:
            choice = Choice("rest", None) if "rest" in legal else P._auto(inp, state, i, reading, spoken)
        state, ex, m, delta = P._exchange(inp, state, i, choice, rng)
        assert rng.count - c0 == G + 5
        exchanges.append(ex)
        margins.append(m)
        deltas.append(delta)
        spoken[i] += 1
        last = i
        rests = rests + 1 if choice.move == "rest" else 0
        if D["break_at"] is not None and any(s.marks >= D["break_at"] for s in state.sides):
            ended = "broken"
            ended_side = next(k for k, s in enumerate(state.sides) if s.marks >= D["break_at"])
            break
        if typ.struck_ends and typ.strikes >= 1 and any(s.strikes >= typ.strikes for s in state.sides):
            ended = "struck"
            break
        y = P._yielded_side(inp, state, spoken)
        if y is not None:
            ended, ended_side = "yielded", y
            break
        if rests >= len(inp.speakers):
            ended = "rested"
            break
    if ended is None:
        ended = "budget"
    verdicts, blv = P._close(inp, state, ended, ended_side, tuple(exchanges), margins, deltas, rng)
    return ProceedingOutcome(exchanges=tuple(exchanges), state=state, ended=ended, verdicts=verdicts,
                             ballot_levels=blv), ended_side


# ------------------------------------------------------------------ strategies
def _best(reading, prefix, grounds):
    return P._argmax(reading, prefix, list(grounds))


def _pick(legal, *pref):
    for m in pref:
        if m in legal:
            return m
    return legal[0]


def s_auto(inp, state, i, reading, spoken, legal):
    return P._auto(inp, state, i, reading, spoken)


def s_argue_best(inp, state, i, reading, spoken, legal):
    if "argue" in legal:
        return Choice("argue", _best(reading, "target:", inp.grounds))
    return Choice(legal[0], None)


def s_argue_fixed(g):
    def f(inp, state, i, reading, spoken, legal):
        if "argue" in legal:
            return Choice("argue", g)
        return Choice(legal[0], None)
    f.__name__ = "argue_" + g
    return f


def s_argue_true_best(inp, state, i, reading, spoken, legal):
    """oracle: argue on the ground of the TRUE highest fit to the body (what a perfect reader would choose)."""
    if "argue" not in legal:
        return Choice(legal[0], None)
    body = P._body(inp, i)
    g = max(inp.grounds, key=lambda g: P._fit_body(body, g))
    return Choice("argue", g)


def s_press_always(inp, state, i, reading, spoken, legal):
    if "press" in legal:
        return Choice("press", _best(reading, "other:", inp.grounds) or _best(reading, "target:", inp.grounds))
    return s_argue_best(inp, state, i, reading, spoken, legal)


def s_press_behind(inp, state, i, reading, spoken, legal):
    behind = P.SIGN[inp.speakers[i].side] * state.track < 0
    if behind and "press" in legal:
        return s_press_always(inp, state, i, reading, spoken, legal)
    return s_argue_best(inp, state, i, reading, spoken, legal)


def s_press_first(inp, state, i, reading, spoken, legal):
    """press on the first own exchange, then argue."""
    if spoken[i] == 0 and "press" in legal:
        return s_press_always(inp, state, i, reading, spoken, legal)
    return s_argue_best(inp, state, i, reading, spoken, legal)


def s_divert(inp, state, i, reading, spoken, legal):
    if "divert" in legal:
        return Choice("divert", None)
    return s_argue_best(inp, state, i, reading, spoken, legal)


def s_divert_then_argue(inp, state, i, reading, spoken, legal):
    if spoken[i] % 2 == 0 and "divert" in legal:
        return Choice("divert", None)
    return s_argue_best(inp, state, i, reading, spoken, legal)


def s_deceive(inp, state, i, reading, spoken, legal):
    if "deceive" in legal:
        return Choice("deceive", _best(reading, "target:", inp.grounds))
    return s_argue_best(inp, state, i, reading, spoken, legal)


def s_concede_early(inp, state, i, reading, spoken, legal):
    if spoken[i] == 0 and "concede" in legal:
        return Choice("concede", None)
    return s_argue_best(inp, state, i, reading, spoken, legal)


def s_rest(inp, state, i, reading, spoken, legal):
    return Choice("rest", None)


def s_argue_once_rest(inp, state, i, reading, spoken, legal):
    if spoken[i] == 0:
        return s_argue_best(inp, state, i, reading, spoken, legal)
    return Choice("rest", None)


def s_mixed(inp, state, i, reading, spoken, legal):
    r = random.Random(hash((state.n, state.track, i, round(reading[0][1], 6))))
    opts = [m for m in ("argue", "press", "divert") if m in legal] or list(legal)
    m = r.choice(opts)
    g = _best(reading, "target:" if m == "argue" else "other:", inp.grounds) if m in ("argue", "press") else None
    return Choice(m, g)


STRATS = {
    "auto": s_auto, "argue_best": s_argue_best, "argue_true": s_argue_true_best,
    "argue_evidence": s_argue_fixed("evidence"), "argue_solidarity": s_argue_fixed("solidarity"),
    "press_always": s_press_always, "press_behind": s_press_behind, "press_first": s_press_first,
    "divert": s_divert, "divert_alt": s_divert_then_argue, "concede_early": s_concede_early,
    "rest": s_rest, "argue_once_rest": s_argue_once_rest, "mixed": s_mixed, "deceive": s_deceive,
}


# ------------------------------------------------------------------ people / scenes
def person(pid, attrs=None, rank=1, proofs=1.0, **kw):
    a = {k: 4 for k in ATTRS}
    a.update(attrs or {})
    p = {"id": pid, "attributes": a, "ranks": {"argue": rank}, "proofs": proofs}
    p.update(kw)
    return p


def bench_people(attrs=None):
    """three polity seats (one church kept out by the filter in polity rows)."""
    out = {}
    for k, (rung, fac) in enumerate((("duchy", "Crown"), ("settlement", "Parliament"), ("settlement", "Crown"))):
        out[f"j{k + 1}"] = person(f"j{k + 1}", attrs, rank=1, proofs=0.0,
                                  seat={"rung": rung, "faction": fac, "modifier": None})
    return out


def scene_kw(row, extra_ids=()):
    if row in ("conversation", "questioning", "negotiation"):
        return dict(addressed="b", bench=(), present=tuple(extra_ids))
    if row == "rally":
        return dict(addressed="crowd", bench=(), present=tuple(extra_ids))
    return dict(addressed="b", bench=("j1", "j2", "j3"), present=tuple(extra_ids))


CARRIED = ("success", "overwhelming")


def run(row, A, B, pol_for="auto", pol_against="auto", n=1000, D=None, effort=2, seed0="l3", extra=None,
        bench_attrs=None, label=None, typ_patch=None):
    """A is the `for` speaker (id 'a'), B the `against` (id 'b'). Returns dict of rates."""
    D = D or dialmod.shipped()
    people = {"a": dict(A, id="a"), "b": dict(B, id="b")}
    people.update(bench_people(bench_attrs))
    for p in (extra or ()):
        people[p["id"]] = p
    inp = build_input(people, row, "full", "argue", actor="a", dials=D, effort=effort,
                      **scene_kw(row, [p["id"] for p in (extra or ())]))
    if typ_patch:
        inp = replace(inp, type=typ_patch(inp.type))
    pols = {}
    for k, S in enumerate(inp.speakers):
        nm = pol_for if S.side == "for" else pol_against
        pols[k] = STRATS[nm] if isinstance(nm, str) else nm
    bands, ends, endside = Counter(), Counter(), Counter()
    marks = Counter()
    moves = Counter()
    nx = 0
    track = 0.0
    for t in range(n):
        rng = draw((seed0, label or row, t), "a", f"roll:proceeding:{row}")
        out, es = proceed2(inp, rng, pols)
        m, veto = P.act_margin(out, inp.type, inp)
        b = None if m is None else degree(m)
        if veto and b in CARRIED:
            b = "failure"
        bands[b] += 1
        ends[out.ended] += 1
        if es is not None:
            endside[(out.ended, inp.speakers[es].side)] += 1
        for S, s in zip(inp.speakers, out.state.sides):
            marks[S.side] += s.marks
        for x in out.exchanges:
            moves[(x.mover, x.move)] += 1
        nx += len(out.exchanges)
        track += out.state.track
    c = (bands["success"] + bands["overwhelming"]) / n
    return dict(carry=c, se=math.sqrt(max(c * (1 - c), 1e-9) / n), bands=bands, ends=ends, endside=endside,
                marks={k: v / n for k, v in marks.items()}, moves=moves, nx=nx / n, track=track / n, n=n, inp=inp)


def check_identity(n=200):
    """control: proceed2 with both auto == proceed(decide=None), field for field."""
    D = dialmod.shipped()
    from scmodel.demo import default_people, scene
    bad = 0
    for row in ("conversation", "legal_trial", "negotiation", "questioning"):
        for t in range(n):
            people = default_people(t)
            inp = build_input(people, row, "full", "argue", actor="a", dials=D, effort=2, **scene(row))
            o1 = P.proceed(inp, draw(t, "a", "x"), None)
            o2, _ = proceed2(inp, draw(t, "a", "x"), {})
            bad += (o1 != o2)
    return bad


if __name__ == "__main__":
    print("identity mismatches:", check_identity())
