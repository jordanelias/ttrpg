"""Antagonist F-K: the decider's Reason reaches the speaker's `fit` (RD B.3 fit_body over deciders; B24p.06 moved_by
evidence = (Reason-1)/6) with sense_step 0. Mean fit sigma (strong .75 / moderate .5, shield .3) of a mid reader."""
import math, random
def fit(v, i):
    m = sum(v) / 4
    if max(v) == min(v): return 0.0
    return (v[i] - m) / (max(v) - m) if v[i] >= m else (v[i] - m) / (m - min(v))
rnd = random.Random(1); N = 100000
for R in range(1, 8):
    v = [(R - 1) / 6, 0.0, 0.0, 0.5]; tot = 0.0
    for _ in range(N):
        read = rnd.gauss(4.0, 0.8 * math.sqrt(10)) - 3.8; blur = 1 - (1 + math.tanh(read)) / 2
        bel = [min(1, max(0, x + blur * rnd.gauss(0, 1))) for x in v]
        g = max(range(4), key=lambda i: (bel[i], -i)); f = fit(v, g)
        tot += .75 * max(f, 0) - .5 * 0.7 * max(-f, 0)
    print(f"  decider Reason {R}: moved_by={[round(x,2) for x in v]}  mean fit sigma to the speaker {tot/N:+.3f}")
