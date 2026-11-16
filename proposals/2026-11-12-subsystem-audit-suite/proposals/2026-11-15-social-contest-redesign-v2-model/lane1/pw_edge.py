"""proof_weight 0 / 1 with a non-mid decider Reason: B.9 sense divides by 2*pw and 2*(1-pw)."""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import sitting, base_people
from scmodel import dials
S = dials.shipped()
for pw in (0.0, 1.0, 0.01, 0.99):
    for r in (2, 6):
        ar = {k: dict(v) for k, v in S['audience_room'].items()}
        for k in ar: ar[k]['proof_weight'] = pw
        D = dials.shipped(audience_room=ar)
        pp = base_people()
        for j in ("j1", "j2", "j3"): pp[j]["attributes"]["reason"] = r
        res = []
        for i in range(200):
            try:
                inp, out, band = sitting("bench_full", pp, D, ("pw", i)); res.append("ok")
            except Exception as e:
                res.append(type(e).__name__)
        from collections import Counter
        print(f"pw={pw} decider Reason {r}: {dict(Counter(res))}")
