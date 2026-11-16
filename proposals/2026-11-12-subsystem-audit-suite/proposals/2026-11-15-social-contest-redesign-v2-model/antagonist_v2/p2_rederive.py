"""Antagonist A probe 2: independent re-derivations (D1, D2, D8 analytic on the LIVE sigma_leverage), dominance over
real menus in every rite, pressing, speaking-hurts. PYTHONHASHSEED=0 python antagonist_v2/p2_rederive.py [n]"""
import sys, os, copy, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, "/home/user/ttrpg")
from collections import Counter
from engine.dice_engine import sigma_leverage as SL
from sc2 import host, fixtures as F
from sc2.engine import Choice
from sc2.lab import sit, rate, CB, BENCH, CARRIED, chooser, smart, se

N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
Phi = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))
def H(t): print("\n== " + t, flush=True)

# my own primitives, from the plan text (B04.24): pool_of = max(floor, score+addends+pool_add); even = 0.4 pool_add; opposed = 0.4 score
pool_of = lambda s, add=6, floor=5: max(floor, s + add)
even = 0.4 * 6
opp = lambda s: 0.4 * max(0.0, s)
def bands(mu, sd):
    f = Phi((0 - mu) / sd); p = Phi((1 - mu) / sd) - f
    return f, p, 1 - f - p

H("D2 independent: the abridged tell between equals (attr 4, rank 1, routine 0.5, flat interiors -> sigma 0)")
P = pool_of(4 + 1); mu = SL.MU_PER_DIE * P - (even + opp(4 + 1) + 0.5); sd = SL.SD_PER_DIE * math.sqrt(P)
f, p, c = bands(mu, sd)
print(f"  closed form: pool {P}, ob {even + opp(5) + 0.5:.2f}, mean {mu:+.2f}, sd {sd:.3f} -> fail {f:.3f} partial {p:.3f} carried {c:.3f}  [producer MC n=4000: .565/.153/.282; A-79 .59/.16/.25]")
P0 = pool_of(4); mu0 = 0.4 * P0 - (even + opp(4) + 0.5); f0, p0, c0 = bands(mu0, 0.8 * math.sqrt(P0))
print(f"  rank 0 (pool 10): fail {f0:.3f} partial {p0:.3f} carried {c0:.3f}")
# the plan's present plain roll (skill score only opposing, per part 4 Q2) for comparison
mu1 = 0.4 * P - (even + opp(1) + 0.5); f1, p1, c1 = bands(mu1, sd)
print(f"  the plan's current plain roll (opposition = rank only): fail {f1:.3f} carried {c1:.3f}  -> V2's 'control equality' is equality to V2's own redefined roll")

H("D1 / D8 independent: the close as a function of the decider's track (pool_of(mid), ob even+opp(mid)+0.5)")
Pc = pool_of(4); obc = even + opp(4) + 0.5; sdc = 0.8 * math.sqrt(Pc)
for t in (-12, -6, -3, 0, 3, 6, 9, 12, 30, 1e6):
    m = 0.4 * Pc + SL.net_boost(0.2 * t, Pc) - obc
    print(f"  track {t:>8}: P(carried) {1 - Phi((1 - m) / sdc):.3f}  P(fail) {Phi(-m / sdc):.3f}")
print("  -> lean never enters the close except as the track's start: D8 'equal track, equal verdict' holds by construction")

mp, M = F.mid_people(), F.matter()
H("D1 by simulation (own seeds): trial carried by the presiding track bin; excommunication")
bins = Counter(); hit = Counter(); big = 0; tot = 0
for i in range(N * 2):
    inp, card, out, b = sit(mp, "trial", M, ("A1", i), bench=BENCH, effort=3)
    t = dict(out.state.tracks)["j1"]; k = "<=-3" if t <= -3 else "(-3,0)" if t < 0 else "[0,3)" if t < 3 else ">=3"
    bins[k] += 1; hit[k] += b[0] in CARRIED; big += abs(t) >= 12; tot += b[0] in CARRIED
print("  " + "  ".join(f"{k} n={bins[k]} {hit[k]/bins[k]:.3f}" for k in ("<=-3", "(-3,0)", "[0,3)", ">=3")) + f"  overall {tot/(2*N):.3f}; |track|>=12 (past ~95% of the soft cap) {big/(2*N):.3f}")
ex = rate(mp, "excommunication_deliberation", M, N * 2, "A1x", bench=("c1", "c2", "c3"), effort=2)
print(f"  excommunication carried {ex:.3f} +- {2*se(ex, 2*N):.3f}  [producer .206]")
for lev in (1, 4, 7):
    pp = copy.deepcopy(mp); pp["a"]["attributes"]["reason"] = lev
    print(f"  trial, speaker Reason {lev}: carried {rate(pp, 'trial', M, N*2, 'A1r', bench=BENCH, effort=3):.3f}")
for lev in (1, 4, 7):
    pp = copy.deepcopy(mp); pp["a"]["attributes"].update(reason=lev); pp["a"]["items"] = (F.Item("deed", "record", 0.8),)
    print(f"  trial, speaker Reason {lev} holding a 0.8 record: carried {rate(pp, 'trial', M, N*2, 'A1ri', bench=BENCH, effort=3):.3f}")

H("SPEAKING HURTS: mean margin of a raise between equals is -manner (standard - grace) x 0.5")
for rite, std in (("conversation", 4), ("trial", 5), ("inquisition", 6)):
    print(f"  {rite:12} standard {std}: a mid-Grace speaker's expected raise margin {-0.5*max(0, std-4):+.2f}; the raise adds the full signed margin to every track")
for rite, kw in (("trial", dict(bench=BENCH)), ("debate", dict(bench=BENCH)), ("audience", dict(bench=("j1",)))):
    m = M if rite != "audience" else dict(id="m", parties={"for": "a"}, bears={})
    r = {k: rate(mp, rite, m, N * 2, "A2", effort=3, deciders={"a": chooser(k)} if k != "auto" else None, **kw) for k in ("auto", "argue", "rest")}
    print(f"  {rite:9} all-mid, `for` vs automatic: " + "  ".join(f"{k} {v:.3f}" for k, v in r.items()) + f"   (2 s.e. {2*se(0.3, 2*N):.3f})")

H("PRESSING A WEAK MAN (Will 2, Grace 2): does reactance bound it? controls show=0; and with the victim automatic")
wk = copy.deepcopy(mp); wk["b"]["attributes"].update(will=2, grace=2)
def pol(kind):
    def f(view, me):
        k = "press" if (kind == "press" or (kind == "p1" and view.own.spoken == 0)) else "argue"
        return chooser(k)(view, me)
    return f
for lab, DD in (("shipped", host.dials()), ("show=0 (a rattle does not raise his manner cost)", host.dials(show=0.0)),
                ("reactance=1.33 (2nd rattle already turns the room)", host.dials(reactance=1.33))):
    for vic in ("argue", "auto"):
        dec = lambda k: {"a": pol(k)} | ({"b": chooser("argue")} if vic == "argue" else {})
        r = {k: rate(wk, "trial", M, N * 2, "A3", bench=BENCH, effort=3, deciders=dec(k), D=DD) for k in ("p1", "press", "argue")}
        print(f"  {lab:50} victim {vic:5}: one press then argue {r['p1']:.3f}  press always {r['press']:.3f}  argue {r['argue']:.3f}")

H("DOMINANCE over the real menus, every rite (cast, effort 3): P(for carried) by `for` policy vs automatic `against`, and by `against` policy vs automatic `for`")
cast = F.cast()
ROWS = (("conversation", {}), ("negotiation", {}), ("questioning", {}), ("inquisition", dict(bench=("bishop", "prior"))),
        ("trial", dict(bench=CB, floor=("guildsmen", "toll_men", "clerk"))), ("debate", dict(bench=CB, floor=("guildsmen",))),
        ("rally", dict(floor=("guildsmen", "toll_men", "townsfolk"))), ("audience", dict(bench=("judge",))))
pols = ("auto", "smart", "argue", "press", "rest", "concede", "random")
for rite, kw in ROWS:
    m = dict(F.TOLLS) if rite not in ("rally", "audience") else dict(F.TOLLS, parties={"for": "orator" if rite == "rally" else "scholar"})
    fid, aid = m["parties"]["for"], m["parties"].get("against")
    for side, who in (("for", fid), ("against", aid)):
        if who is None or (rite in ("rally", "audience") and side == "against"):
            continue
        res = {}
        for k in pols:
            dec = {} if k == "auto" else {who: smart if k == "smart" else chooser(k, 7)}
            res[k] = rate(cast, rite, m, N, ("A4", rite, side), effort=3, deciders=dec, **kw)
        better = (lambda x, y: x > y) if side == "for" else (lambda x, y: x < y)
        best = max(pols, key=lambda k: res[k] if side == "for" else -res[k])
        print(f"  {rite:12} {side:7} " + " ".join(f"{k} {res[k]:.3f}" for k in pols) + f"  | best: {best} (vs auto {abs(res[best]-res['auto']):+.3f}; 2se {2*se(0.4, N):.3f})", flush=True)
