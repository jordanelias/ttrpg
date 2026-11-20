"""NERS cut test on the rig's levers (2026-11-17, Jordan: distil or cut where it makes sense). Arms: `all` (presumption,
sympathy, packing), `nosym` (sympathy_step 0), `presume` (sympathy 0 and no packing: the presumption alone). For each:
does the rig move every row toward the arranger whichever side arranges (monotone in rig), and is every rig level
best somewhere on the arranger's reckoning 2 x stake x P - rig_price x tilt^2 (fix2/c3_grid's cast and cases)?
python -B f18_levers.py ARM N"""
from common import *
ARM_ = sys.argv[1]; N = int(sys.argv[2]) if len(sys.argv) > 2 else 400
D = host.dials(sympathy_step=0.0) if ARM_ in ("nosym", "presume") else host.dials()
if ARM_ == "presume":
    host._pack = lambda cands, arr_id, t, people, keep=1: list(cands)
H(f"F18 arm `{ARM_}`: P(for) by rig 0 / 0.5 / 1, arranger r5M vs r2, Parliament parties, n={N}")
bad = 0
for row, kw in (("trial", dict(bench=BENCH, floor=("crowd", "o1"))), ("tribunal", dict(bench=BENCH)), ("debate", dict(bench=BENCH, floor=("crowd",))),
                ("audience", dict(bench=BENCH)), ("rally", dict(floor=("crowd", "o1", "t")))):
    for who in ("a", "b"):
        pp = castB(pa="r5M", pb="r2", seat_fac="Parliament") if who == "a" else castB(pa="r2", pb="r5M", seat_fac="Parliament")
        ps = [sum(sit(pp, row, mat(), ("lv", row, who, i), arranger=who, rig=rig, effort=2, D=D, **kw)[3][0] in CARRIED for i in range(N)) / N for rig in (0.0, 0.5, 1.0)]
        sg = 1 if who == "a" else -1
        mono = sg * (ps[2] - ps[0]) > 0 and sg * (ps[1] - ps[0]) > -2 * se(.3, N)
        bad += not mono
        print(f"  {row:9} arranger {who}: " + " / ".join(f"{p:.3f}" for p in ps) + ("" if mono else "   <-- not toward the arranger"), flush=True)
print(f"  rows where the rig does not move toward its arranger: {bad} of 10")
def cast_with(a_rung):
    pp = F.mid_people(); pp["a"]["faction"] = pp["b"]["faction"] = "Crown"; pp["a"]["office"] = F.seat(a_rung, "Crown")
    pp["j2"]["layers"] = dict(relationships={"a": 0.6}); pp["j3"]["layers"] = dict(relationships={"b": 0.6}); return pp
tab = {}
for rung in (1, 2, 4):
    for ra in (1, 4, 7):
        pp = cast_with(rung); pp["a"]["attributes"]["reason"] = ra
        ps = {r: sum(sit(pp, "trial", F.matter(), ("g", i), bench=BENCH, floor=("crowd",), effort=3, arranger="a", rig=r, D=D)[3][0] in CARRIED for i in range(N)) / N for r in (0, 0.5, 1)}
        ts = {r: host.build(pp, "trial", F.matter(), bench=BENCH, floor=("crowd",), effort=3, arranger="a", rig=r, D=D)[1].tilt for r in ps}
        tab[(rung, ra)] = (ps, ts)
cnt = Counter()
for (ps, ts) in tab.values():
    for st in (0.25, 0.5, 1.0):
        cnt[max(ps, key=lambda r: 2 * st * ps[r] - host.FOLD["rig_price"] * ts[r] ** 2)] += 1
print(f"  C3: the best rig over 9 cases x stakes 0.25 / 0.5 / 1 at rig_price {host.FOLD['rig_price']}: {dict(sorted(cnt.items()))}")
