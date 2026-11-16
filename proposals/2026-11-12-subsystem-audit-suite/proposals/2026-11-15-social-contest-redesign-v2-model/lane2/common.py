"""Lane 2 shared fixtures: a people factory with seats of every authority, a cohort, a 12-weight crowd."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import scmodel  # noqa: F401
from scmodel import dials, data
from scmodel.host import build_input
from scmodel.proceeding import proceed, act_margin, _moves
from scmodel.rng import draw
from scmodel.dice import degree, Margin

ATTRS = ("focus", "reason", "attunement", "presence", "grace", "will")
PROFILES = {"lo": 1, "mid": 4, "hi": 7}


def person(pid, v=4, **kw):
    p = dict(id=pid, attributes={k: v for k in ATTRS}, ranks={"argue": 1}, proofs=1.0,
             pursuits={"x": 0.5}, convictions={"c": 2}, regard={})
    p.update(kw)
    return p


def people(pa="mid", pb="mid", pd="mid"):
    a, b, d = PROFILES[pa], PROFILES[pb], PROFILES[pd]
    P = {"a": person("a", a, regard={"b": -0.2}), "b": person("b", b, regard={"a": -0.2})}
    for fac, auth in (("Crown", "pol"), ("Church", "ch"), ("Guild", "gu")):
        for k in range(5):
            pid = f"{auth}{k}"
            P[pid] = person(pid, d, seat={"rung": "duchy", "faction": fac, "modifier": None})
    P["cohort"] = person("cohort", d, weight=30, regard={"a": 0.1})
    P["seatcohort"] = person("seatcohort", d, weight=30, seat={"rung": "duchy", "faction": "Crown"})
    P["crowd12"] = person("crowd12", d, weight=12, regard={"a": 0.1})
    P["h1"] = person("h1", d, regard={"a": 0.2}, seat={"rung": "hearth", "faction": "Guild"})
    return P


AUTH_PREFIX = {"polity": "pol", "church": "ch", "guild": "gu", "parties": "pol", "none": "pol"}


def bench_for(row, kind):
    """kind: 0,1,2,5 seats of the row's authority; 'cohort' a weight-30 seat; 'short' 1 seat (< quorum when declared);
    'filtered' 3 seats of a wrong authority."""
    auth = data.ROWS[row]["authority"]
    pre = AUTH_PREFIX[auth]
    if kind == "cohort":
        return ("seatcohort",)
    if kind == "short":
        return (f"{pre}0",)
    if kind == "filtered":
        wrong = "gu" if pre != "gu" else "pol"
        return tuple(f"{wrong}{k}" for k in range(3))
    return tuple(f"{pre}{k}" for k in range(kind))


HEARERS = {0: (), 1: ("h1",), 12: ("crowd12",)}


def legal_move(inp, x):
    side = next(S.side for S in inp.speakers if S.id == x.mover)
    return x.move in {m.id for m in _moves(inp, side)} or x.move == "rest"
