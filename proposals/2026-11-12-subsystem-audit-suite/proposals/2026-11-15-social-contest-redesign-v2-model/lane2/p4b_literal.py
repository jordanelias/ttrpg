"""P4b: A.2's recompute read literally (every recorded margin, clipped, running sum clamped) vs the module's track,
automatic sittings (presses occur, no concede).  PYTHONHASHSEED=0 python lane2/p4b_literal.py"""
from common import *
D = dials.shipped()
for row in ("conversation", "legal_trial"):
    inp = build_input(people("hi", "lo"), row, "full", actor="a", addressed="b", bench=("pol0",), effort=7, dials=D)
    mism = tot = haspress = 0
    for s in range(1000):
        o = proceed(inp, draw(("l", s), "a", "l"), None)
        side = {S.id: (1.0 if S.side == "for" else -1.0) for S in inp.speakers}
        t = 0.0
        for x in o.exchanges:
            if x.terms:
                t = max(-3, min(3, t + side[x.mover] * max(-3, min(3, x.margin))))
        tot += 1; mism += abs(t - o.state.track) > 1e-9; haspress += any(x.move == "press" for x in o.exchanges)
    print(f"{row}: literal recompute != track in {mism}/{tot}; sittings with a press {haspress}")
