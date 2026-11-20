"""Probe 6: what triggers a press. Among exchanges where the mover is behind and holds a strike move, the share pressed,
by speaker Attunement, with the TRUE strain of the target, the believed strain and p_land. Control: read_blur 0
(a perfect reading). usage: PYTHONHASHSEED=0 python lane1/press_driver.py [n]"""
import sys, os, math
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from harness import sitting, base_people
from scmodel import dials, proceeding as P
N = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
LOG = []
_orig = P._auto
def spy(inp, state, i, reading, spoken):
    c = _orig(inp, state, i, reading, spoken)
    S = inp.speakers[i]
    behind = P.SIGN[S.side] * state.track < 0
    legal = P._legal(inp, state, i, spoken)
    if behind and "press" in legal and i == 0:
        j = P._other(inp, i)
        LOG.append((c.move == "press", state.sides[j].strain, dict(reading)["strain"]))
    return c
P._auto = spy
for blur_lab, over in (("shipped", {}), ("read_blur 0 (perfect reading)", dict(read_blur=0.0))):
    D = dials.shipped(**over)
    for att in (1, 4, 7):
        LOG.clear()
        pp = base_people(); pp["a"]["attributes"]["attunement"] = att
        for i in range(N):
            sitting("bench_full", pp, D, ("press", i))
        n = len(LOG); pr = sum(l[0] for l in LOG)
        pz = [l for l in LOG if l[1] == 0.0]
        prz = sum(l[0] for l in pz)
        prz_bel0 = sum(1 for l in pz if l[0] and l[2] == 0.0)
        print(f"{blur_lab:30} Attunement {att}: behind-with-press {n}, pressed {pr/n:.3f}±{math.sqrt(pr/n*(1-pr/n)/n):.3f}; "
              f"of those with TRUE strain 0 ({len(pz)}): pressed {prz/max(1,len(pz)):.3f}, pressed with believed strain 0: {prz_bel0}")
