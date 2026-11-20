"""P1c: is pressing ever worth it? `for` strategies vs an automatic `against` of Will/Grace 1, 4, 7; common seeds per
cell (the label omits the for-strategy), so differences are paired. Also: the policy with press_at 0.0 / 0.4 / 1.0.
Also conditional carry given the opponent was broken.
    PYTHONHASHSEED=0 python lane3/p1c_press_value.py [n]"""
import math
import sys

from harness import run, person, dialmod, CARRIED

n = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
MOV = dict(pursuits={"x": 0.6}, convictions={"c": 3})
for row in ("conversation", "questioning", "negotiation"):
    for w in (1, 4, 7):
        A = person("a", **MOV)
        B = person("b", {"will": w, "grace": w}, **MOV)
        out = []
        for s in ("argue_best", "auto", "press_behind", "press_first", "press_always"):
            r = run(row, A, B, s, "auto", n=n, label=f"p1c:{row}:{w}")
            out.append(f"{s}={r['carry']:.3f}(brk {r['ends'].get('broken', 0) / n:.2f})")
        print(f"{row:12} opp Will/Grace={w}: " + "  ".join(out) + f"  se~{r['se']:.3f}")
    for pa in (0.0, 0.4, 1.0):
        r = run(row, person("a", **MOV), person("b", **MOV), "auto", "auto", n=n, D=dialmod.shipped(press_at=pa),
                label=f"p1c:{row}:pa")
        print(f"{row:12} both auto, press_at={pa}: carry={r['carry']:.3f}±{r['se']:.3f} ends={dict(r['ends'])} "
              f"marks={ {k: round(v, 3) for k, v in r['marks'].items()} }")
