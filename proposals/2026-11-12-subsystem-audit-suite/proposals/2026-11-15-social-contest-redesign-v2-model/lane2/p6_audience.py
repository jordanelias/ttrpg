"""P6: audience. (a) which audience kinds each row can reach (full/abridged) over present = (), h1, crowd12, 20 onlookers;
(b) bench rows: are hearers/floor inert (same key, signatures with and without onlookers);
(c) rally to a lone cohort (room none) vs the cohort with one onlooker (gallery) vs a 12-weight crowd present: Presence
    2 vs 6 effect on the act's Success+ share (C.8: "Presence carries it").
    PYTHONHASHSEED=0 python lane2/p6_audience.py [n]
"""
import sys, random
from collections import Counter, defaultdict
from common import *

N = int(sys.argv[1]) if len(sys.argv) > 1 else 2000
D = dials.shipped()
SUC = ("success", "overwhelming")
P = people()
for k in range(20):
    P[f"o{k}"] = person(f"o{k}", 4)
PRESENT = {"none": (), "h1": ("h1",), "crowd12": ("crowd12",), "20 onlookers": tuple(f"o{k}" for k in range(20))}
kinds = defaultdict(set)
for row in data.ROW_IDS:
    pre = AUTH_PREFIX[data.ROWS[row]["authority"]]
    addressed = "cohort" if row == "rally" else ("b" if data.RITES[data.ROWS[row]["rite"]]["against"] else None)
    for form in ("full", "abridged"):
        for pk, pr in PRESENT.items():
            inp = build_input(P, row, form, actor="a", addressed=addressed, bench=(f"{pre}0",), present=pr, dials=D)
            kinds[(row, form)].add(inp.room.audience)
print("(a) audience kinds reachable:")
for k, v in kinds.items():
    print(f"    {k}: {sorted(v)}")

# (b)
diff = defaultdict(int)
tot = 0
for row in data.ROW_IDS:
    if data.ROWS[row]["disposal"] not in ("bench", "declared"):
        continue
    pre = AUTH_PREFIX[data.ROWS[row]["authority"]]
    addressed = "b" if data.RITES[data.ROWS[row]["rite"]]["against"] else None
    for s in range(200):
        sig = []
        for pr in PRESENT.values():
            inp = build_input(P, row, "full", actor="a", addressed=addressed, bench=(f"{pre}0", f"{pre}1"), present=pr,
                              effort=3, dials=D)
            o = proceed(inp, draw(("b", row, s), "a", "b"), None)
            sig.append((tuple((x.move, round(x.margin, 9)) for x in o.exchanges),
                        tuple((i, round(m.net, 9)) for i, m in o.verdicts)))
        tot += 1
        diff[row] += any(x != sig[0] for x in sig[1:])
print(f"(b) bench/declared rows: sittings whose outcome changes with onlookers present: {dict(diff)} of 200 each")

# (c) rally presence slope
def share(pres_val, present):
    c = 0
    for i in range(N):
        r = random.Random(i)
        Pp = people()
        for pid in Pp:
            Pp[pid]["attributes"] = {k: r.randint(1, 7) for k in ATTRS}
        Pp["a"]["attributes"]["presence"] = pres_val
        inp = build_input(Pp, "rally", "full", actor="a", addressed="cohort", present=present, effort=2, dials=D)
        o = proceed(inp, draw(("c", i), "a", "c"), None)
        m, _ = act_margin(o, inp.type, inp)
        c += degree(m) in SUC
    return c / N, inp.room.audience

for label, pr in (("lone cohort", ()), ("cohort + h1", ("h1",)), ("cohort + crowd12", ("crowd12",))):
    lo, k = share(2, pr)
    hi, _ = share(6, pr)
    print(f"(c) rally, {label:17s} room={k:8s}: Success+ Presence 2 {lo:.3f}, Presence 6 {hi:.3f}, diff {hi - lo:+.3f}")
