"""Demo: each of the thirteen types once with default people; and `run_many`.

    cd <sc_model> && PYTHONHASHSEED=0 python -m scmodel.demo [--controls] [--n N]
"""
from __future__ import annotations

import argparse
import random
from collections import Counter

from . import data, dials as dialmod
from .dice import degree
from .host import build_input
from .proceeding import act_margin, proceed
from .rng import draw


def default_people(rng_seed=None):
    """A, B the parties; three seats (polity, church, polity) at a settlement; two onlookers; a cohort of 30."""
    rnd = random.Random(rng_seed) if rng_seed is not None else None

    def att(**kw):
        base = {k: 4 for k in ("focus", "reason", "attunement", "presence", "grace", "will")}
        if rnd is not None:
            base = {k: rnd.randint(1, 7) for k in base}
        base.update(kw)
        return base

    P = {
        "a": dict(id="a", attributes=att(reason=5, presence=4), ranks={"argue": 1}, proofs=2.0,
                  pursuits={"x": 0.6}, convictions={"faith": 2}, regard={"b": -0.2}, knows=["b"],
                  operands=[("rank_gap", 1.0, 0.5, "reason")]),
        "b": dict(id="b", attributes=att(reason=4, presence=5), ranks={"argue": 1}, proofs=1.0,
                  pursuits={"y": 0.3}, convictions={"crown": 4}, regard={"a": -0.3}),
        "j1": dict(id="j1", attributes=att(reason=6), ranks={"argue": 2}, addends=1,
                   seat={"rung": "duchy", "faction": "Crown", "modifier": "minor"}, regard={"a": 0.1}),
        "j2": dict(id="j2", attributes=att(attunement=6), ranks={"argue": 1},
                   seat={"rung": "settlement", "faction": "Church", "modifier": "minor"}),
        "j3": dict(id="j3", attributes=att(focus=3), seat={"rung": "settlement", "faction": "Parliament",
                                                           "modifier": None}),
        "h1": dict(id="h1", attributes=att(), regard={"a": 0.5}, seat={"rung": "hearth", "faction": "Guild"}),
        "h2": dict(id="h2", attributes=att(will=6), regard={"a": -0.5}),
        "crowd": dict(id="crowd", attributes=att(), weight=30, regard={"a": 0.2}),
    }
    return P


def scene(row):
    """who is addressed, who sits, who is present, per row (a plausible default; C.8)."""
    bench = ("j1", "j2", "j3")
    if row == "rally":
        return dict(addressed="crowd", bench=(), present=("h1", "h2"))
    if row in ("conversation", "questioning", "negotiation"):
        return dict(addressed="b", bench=(), present=("h1", "h2"))
    if row == "audience":
        return dict(addressed=None, bench=bench, present=("h1", "h2", "crowd"))
    return dict(addressed="b", bench=bench, present=("h1", "h2", "crowd"))


def run_one(row, form="full", move="argue", seed=0, D=None, people=None, effort=2, decide=None, **kw):
    D = D or dialmod.shipped()
    people = people or default_people()
    sc = scene(row)
    sc.update(kw)
    inp = build_input(people, row, form, move, actor="a", dials=D, effort=effort, **sc)
    rng = draw(seed, "a", f"roll:proceeding:{row}:{form}")
    out = proceed(inp, rng, decide)
    m, veto = act_margin(out, inp.type, inp)
    band = None if m is None else degree(m)
    if veto and band in ("success", "overwhelming"):
        band = "failure"    # "the ladder takes the minimum on a veto" (B24p.19 item 4)
    return inp, out, m, band


def run_many(n, row, form="full", move="argue", D=None, people_fn=None, effort=2, seed0=0, **kw):
    """n keyed sittings. Returns {'band': Counter, 'ended': Counter, 'exchanges': mean, 'marks': mean,
    'moves': Counter}. people_fn(i) -> people dict (default: fixed default_people)."""
    bands, ends, moves = Counter(), Counter(), Counter()
    nx = marks = 0
    for i in range(n):
        people = people_fn(i) if people_fn else None
        inp, out, m, band = run_one(row, form, move, seed=(seed0, i), D=D, people=people, effort=effort, **kw)
        bands[band] += 1
        ends[out.ended] += 1
        nx += len(out.exchanges)
        marks += sum(s.marks for s in out.state.sides)
        for x in out.exchanges:
            moves[x.move] += 1
    return {"band": bands, "ended": ends, "exchanges": nx / n, "marks": marks / n, "moves": moves}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--controls", action="store_true")
    ap.add_argument("--n", type=int, default=0, help="also run_many(n) per type")
    a = ap.parse_args()
    D = dialmod.controls() if a.controls else dialmod.shipped()
    print(f"dials: {'controls' if a.controls else 'shipped'}")
    for row in data.ROW_IDS:
        inp, out, m, band = run_one(row, D=D)
        print(f"\n== {row}: disposal={inp.type.disposal} order={inp.type.order} room={inp.room.audience} "
              f"speakers={[s.id for s in inp.speakers]} deciders={[d.id for d in inp.deciders]}")
        for x in out.exchanges:
            print(f"   #{x.n} {x.mover:>5} {x.move:<7} {str(x.ground):<11} on_topic={x.on_topic!s:<5} "
                  f"margin={x.margin:+.3f} strain={x.strain:.2f} marked={x.marked}")
        print(f"   ended={out.ended} track={out.state.track:+.3f} "
              f"sides={[(s.id, s.marks, s.strikes, round(s.resolve, 2), round(s.esteem, 3)) for s in out.state.sides]}")
        for did, mm in out.verdicts:
            print(f"   verdict {did}: net={mm.net:+.3f} ob={mm.ob:.3f} -> {degree(mm)}")
        print(f"   act margin: {None if m is None else round(m.net - m.ob, 3)} band={band}")
        if a.n:
            r = run_many(a.n, row, D=D)
            print(f"   run_many({a.n}): bands={dict(r['band'])} ends={dict(r['ended'])} "
                  f"exchanges={r['exchanges']:.2f} marks={r['marks']:.2f}")
    print("\n== abridged: tell (conversation), lie (conversation, deceive), speak (legal_trial)")
    for row, move, addressed in (("conversation", "argue", "b"), ("conversation", "deceive", "b"),
                                 ("legal_trial", "argue", None)):
        inp, out, m, band = run_one(row, "abridged", move, D=D, addressed=addressed)
        x = out.exchanges[0]
        print(f"   {row}/{move}: room={inp.room.audience} addressed={inp.deciders[0].id} margin={x.margin:+.3f} "
              f"band={band} verdicts={len(out.verdicts)}")


if __name__ == "__main__":
    main()
