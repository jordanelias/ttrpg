"""Lane 1 harness: clean all-mid people, scenarios, one-attribute sweeps with common random numbers.
Slope = mean over keys of the per-key OLS slope of `carried` on the attribute (x=1..7); SE = sd/sqrt(n)."""
import copy, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import scmodel  # noqa
from scmodel import dials
from scmodel.dice import degree
from scmodel.host import build_input
from scmodel.proceeding import act_margin, proceed
from scmodel.rng import draw

ATTRS = ("focus", "reason", "attunement", "presence", "grace", "will")
CARRIED = ("success", "overwhelming")


def mid(**kw):
    a = {k: 4 for k in ATTRS}; a.update(kw); return a


def base_people(rank=1, proofs=2.0, known=True):
    P = {
        "a": dict(id="a", attributes=mid(), ranks={"argue": rank} if rank else {}, proofs=proofs,
                  knows=["b"] if known else [], operands=[("rank_gap", 1.0, 0.5, "reason")] if known else []),
        "b": dict(id="b", attributes=mid(), ranks={"argue": rank} if rank else {}, proofs=proofs / 2),
        "crowd": dict(id="crowd", attributes=mid(), weight=30),
    }
    for j in ("j1", "j2", "j3"):
        P[j] = dict(id=j, attributes=mid(), ranks={"argue": 1}, seat={"rung": "duchy", "faction": "Crown", "modifier": None})
    return P

# scenario -> (row, form, scene kwargs, decider ids)
SCEN = {
    "private_abr":  ("conversation", "abridged", dict(addressed="b"), ("b",)),
    "private_full": ("conversation", "full", dict(addressed="b"), ("b",)),
    "bench_abr":    ("legal_trial", "abridged", dict(addressed=None, bench=("j1", "j2", "j3")), ("j1",)),
    "bench_full":   ("legal_trial", "full", dict(addressed="b", bench=("j1", "j2", "j3")), ("j1", "j2", "j3")),
    "crowd_full":   ("rally", "full", dict(addressed=None, present=("crowd",)), ("crowd",)),
    "question_full": ("questioning", "full", dict(addressed="b"), ("b",)),
}


def sitting(scen, people, D, key, effort=2, difficulty_level="routine", decide=None):
    row, form, sc, _ = SCEN[scen]
    inp = build_input(people, row, form, "argue", actor="a", dials=D, effort=effort,
                      difficulty_level=difficulty_level, **sc)
    out = proceed(inp, draw(key, "a", f"roll:proceeding:{row}:{form}"), decide)
    m, veto = act_margin(out, inp.type, inp)
    band = None if m is None else degree(m)
    if veto and band in CARRIED:
        band = "failure"
    return inp, out, band


def set_attr(people, who, attr, v, scen):
    P = copy.deepcopy(people)
    ids = SCEN[scen][3] if who == "dec" else (who,)
    for i in ids:
        P[i]["attributes"][attr] = v
    return P


def sweep(scen, who, attr, n=2000, D=None, seed="L1", people=None, levels=range(1, 8), outcome=None, **kw):
    """returns dict(level -> share), slope, se, per-level se, and extra tallies."""
    D = D or dials.shipped()
    people = people or base_people()
    levels = list(levels)
    xm = sum(levels) / len(levels); sxx = sum((x - xm) ** 2 for x in levels)
    outcome = outcome or (lambda inp, out, band: 1.0 if band in CARRIED else 0.0)
    ys = {x: [] for x in levels}
    Ps = {x: set_attr(people, who, attr, x, scen) for x in levels}
    slopes = []
    for i in range(n):
        row = []
        for x in levels:
            inp, out, band = sitting(scen, Ps[x], D, (seed, i), **kw)
            y = outcome(inp, out, band)
            ys[x].append(y); row.append(y)
        slopes.append(sum((x - xm) * y for x, y in zip(levels, row)) / sxx)
    mean = sum(slopes) / n
    sd = math.sqrt(sum((s - mean) ** 2 for s in slopes) / (n - 1))
    share = {x: sum(v) / n for x, v in ys.items()}
    sse = {x: math.sqrt(max(share[x] * (1 - share[x]), 1e-12) / n) if all(y in (0.0, 1.0) for y in ys[x]) else
           math.sqrt(sum((y - share[x]) ** 2 for y in ys[x]) / (n - 1) / n) for x in levels}
    return dict(share=share, slope=mean, se=sd / math.sqrt(n), sse=sse, n=n)


def monotone(r, sign):
    """count adjacent steps that go against `sign` by more than 2 SE of the paired difference (approx: unpaired)."""
    xs = sorted(r["share"]); bad = []
    for a, b in zip(xs, xs[1:]):
        d = r["share"][b] - r["share"][a]
        se = math.hypot(r["sse"][a], r["sse"][b])
        if sign * d < -2 * se:
            bad.append((a, b, round(d, 3)))
    return bad
