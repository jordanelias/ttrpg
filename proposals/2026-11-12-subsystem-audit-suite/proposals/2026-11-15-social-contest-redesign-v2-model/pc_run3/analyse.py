import json, sys, math
from common import ols
f = sys.argv[1]
data = json.load(open(f)); n = int(f.split("_")[-1].split(".")[0])
print(f"file {f}  n={n}/level; slope = OLS of carried on level 1..7 per seat-sitting (SE from OLS); d71 = P7-P1")
for fx, ctx, attr, ds, res in sorted(data, key=lambda r: (r[0], r[2], r[1])):
    xs, ys = [], []
    for x in range(1, 8):
        p = res[str(x)]["car"]; k = round(p * n)
        xs += [x] * n; ys += [1] * k + [0] * (n - k)
    b, se = ols(xs, ys)
    ps = [res[str(x)]["car"] for x in range(1, 8)]
    inv = sum(1 for i in range(6) if ps[i+1] < ps[i] - 2 * math.sqrt(0.5 / n))
    r1, r7 = res["1"], res["7"]
    extra = " ".join(f"{k}:{r1[k]:.2f}>{r7[k]:.2f}" for k in ("drift","rel","heard","est","broke","rests","presses","rattled","yielded","beats"))
    print(f"{fx:5} {attr:10} {ctx:12} slope {b*100:+6.2f}±{se*100:4.2f}pp/lvl z{b/se:+6.1f} P1..7 " + " ".join(f"{p:.3f}" for p in ps) + f" nonmono{inv} | {extra}")
