import sys, os, traceback
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/snap")
from sc2 import host, fixtures as F
from sc2.engine import proceed
from scmodel.rng import draw
mp, M = F.mid_people(), F.matter()
cases = [
 ("trial: accused by himself (for=a, against=a)", "trial", dict(M, parties={"for": "a", "against": "a"}), dict(bench=("j1",))),
 ("abridged rally: the speaker is the only one who decides, a crowd overhears", "rally", dict(M, parties={"for": "a"}), dict(form="abridged", bench=("a",), floor=("crowd",))),
 ("rally: the speaker also on the bench", "rally", dict(M, parties={"for": "a"}), dict(bench=("a",), floor=("crowd",))),
 ("negotiation between a and a", "negotiation", dict(M, parties={"for": "a", "against": "a"}), {}),
 ("debate: both movers are seats and vote", "debate", dict(M, parties={"for": "j1", "against": "j2"}), dict(bench=("j1", "j2", "j3"))),
 ("audience: petitioner is the seat", "audience", dict(M, parties={"for": "j1", "against": "b"}), dict(bench=("j1",))),
 ("questioning with no one questioned", "questioning", dict(M, parties={"for": "a"}), {}),
]
for lab, rite, m, kw in cases:
    try:
        inp, card = host.build(mp, rite, m, effort=2, **kw)
        out = proceed(inp, draw(1, "e", "e"))
        print(f"  RAN   {lab}: room {[(p.id, p.side, p.decides) for p in inp.room]}; band {host.act_band(inp, out)[0]}; beats {len(out.beats)}")
    except ValueError as e:
        print(f"  REFUSED {lab}: {e}")
    except Exception as e:
        print(f"  CRASH {lab}: {type(e).__name__}: {e}")
