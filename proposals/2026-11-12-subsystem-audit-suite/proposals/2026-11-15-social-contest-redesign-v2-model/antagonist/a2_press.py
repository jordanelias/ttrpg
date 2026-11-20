"""Antagonist F-E: an independent, simplified `questioning` sitting (scripted, 4 exchanges, hearers disposal: the one
questioned ballots for himself), written from RD A.4-A.6, B.1-B.6, B.9 and PLAN B24p.10-.12, NOT from scmodel.
Simplifications (stated): no proofs, no host levels, no regard, every speech heard in full (room `none`), ground chosen
on a blurred reading of the target's moved_by, opposition = skill score 2, difficulty routine .5, reason_bias 0.
Policies at the behind side's turn: ARGUE (always argue), PRESS (press whenever behind), AUTO (A.6 threshold)."""
import sys, math, random
sys.path.insert(0, "/home/user/ttrpg")
from engine.dice_engine import sigma_leverage as SL
MU, SD = SL.MU_PER_DIE, SL.SD_PER_DIE
Phi = lambda z: 0.5 * (1 + math.erf(z / math.sqrt(2)))
EVEN, DIFF, OPP = 0.4 * 6, 0.5, 0.4 * 2
W = {"evidence": .8, "consequence": .7, "authority": .4, "solidarity": .2}
G = list(W)
pool_of = lambda s: max(5, s + 6)
def tenth(r, p, k): return (2 * (k * round(10 * r) + (10 - k) * round(10 * p)) + 10) // 20 / 10
def mv(P): return [(P["R"] - 1) / 6, P["pur"], P["conv"] / 5, (P["A"] - 1) / 6]
def fit(v, i):
    m = sum(v) / 4
    if max(v) == min(v): return 0.0
    return (v[i] - m) / (max(v) - m) if v[i] >= m else (v[i] - m) / (m - min(v))
def p_ge(pool, ob, sig, k=0.0):
    b = SL.net_boost(sig, pool); return 1 - Phi((ob + k - MU * pool - b) / (SD * math.sqrt(pool)))
def person(rnd, mid):
    if mid: return dict(R=4, P=4, A=4, F=4, Gr=4, Wi=4, pur=0.0, conv=0)
    return dict(R=rnd.randint(1, 7), P=rnd.randint(1, 7), A=rnd.randint(1, 7), F=rnd.randint(1, 7),
                Gr=rnd.randint(1, 7), Wi=rnd.randint(1, 7), pur=round(rnd.uniform(0, .8), 2), conv=rnd.randint(0, 5))
def sitting(rnd, Pq, Pa, pol_q, pol_a):
    S = {"for": Pq, "against": Pa}; other = {"for": "against", "against": "for"}
    st = {s: dict(marks=0, strain=0.0, res=2 + .5 * S[s]["Wi"], pull=0.0, est=.08 * (S[s]["Gr"] - 4), left=2) for s in S}
    track, argues, ended = 0.0, [], "budget"
    for s in ("for", "against", "for", "against"):
        me, T, ts = S[s], S[other[s]], st[other[s]]
        if st[s]["res"] <= 0 or st[s]["left"] <= 0: continue
        sign = 1 if s == "for" else -1
        # reading (Attunement), blurred view of the target (here the other speaker; for `for` also the decider)
        read = rnd.gauss(MU * pool_of(me["A"]), SD * math.sqrt(pool_of(me["A"]))) - 0.15 * (T["Gr"] - 4) * 0 - (EVEN + 1.4)
        blur = 1 - (1 + math.tanh(read)) / 2
        bel = [min(1, max(0, v + blur * rnd.gauss(0, 1))) for v in mv(T)]
        g = max(range(4), key=lambda i: (bel[i], -i))
        behind = sign * track < 0
        pol = pol_q if s == "for" else pol_a
        cover = min(.9, .15 * (me["Gr"] - 1)); shield = min(.6, .1 * (me["Wi"] - 1))
        k = round(10 * W[G[g]]); pool = pool_of(tenth(me["R"], me["P"], k) + 1)
        r = .15 * (T["Wi"] - 4)
        f_for = [.25 * (me["P"] - 4) if me["P"] > 4 else 0, max(st[s]["est"], 0), max(-r, 0)]
        f_ag = [.25 * (4 - me["P"]) if me["P"] < 4 else 0, max(-st[s]["est"], 0), st[s]["marks"] * .5 * (1 - cover), max(r, 0)]
        press = False
        if behind and pol == "press": press = True
        if behind and pol == "auto":
            sig0 = sum(f_for) - sum(f_ag) * (1 - shield)
            p_land = p_ge(pool, EVEN + DIFF + OPP, sig0)
            blow = .5 * 2 * (1 + max(bel)); steady = p_ge(10, EVEN + blow, 0.0)   # believed strain 0, Will at mid
            press = p_land * (1 - steady) >= 0.4
        fitsig = 0.0 if press else (.75 * max(fit(mv(T), g), 0), .5 * max(-fit(mv(T), g), 0))
        sig = sum(f_for) - sum(f_ag) * (1 - shield)
        if not press: sig += fitsig[0] - fitsig[1] * (1 - shield)
        pull = st[s]["pull"] + 0.5
        on = rnd.gauss(MU * pool_of(me["F"]), SD * math.sqrt(pool_of(me["F"]))) - (EVEN + pull) >= 0
        ob = EVEN + DIFF + OPP + (0 if on else 1.5)
        m = rnd.gauss(MU * pool, SD * math.sqrt(pool)) + SL.net_boost(sig, pool) - ob
        stdy = rnd.gauss(MU * pool_of(T["Wi"]), SD * math.sqrt(pool_of(T["Wi"])))
        if press:
            if m >= 0:
                blow = .5 * (1 + m) * (1 + mv(T)[max(range(4), key=lambda i: (bel[i], -i))])
                if stdy - (EVEN + ts["strain"] + blow) < 0:
                    ts["marks"] += 1; ts["strain"] = 0; ts["res"] -= 1; ts["pull"] += .5
                    ts["est"] -= .25 * (1 - min(.9, .15 * (T["Gr"] - 1)))
                else: ts["strain"] += .5 * blow
            else: st[s]["est"] -= .25
        else:
            track = max(-3, min(3, track + sign * max(-3, min(3, m)))); argues.append((sign, me, k))
        st[s]["res"] -= 1; st[s]["left"] -= 1; st[s]["pull"] = 0.0
        if any(st[x]["marks"] >= 2 for x in st): ended = "broken"; break
        y = [x for x in st if st[x]["res"] <= 0 and st[other[x]]["res"] > 0 and st[other[x]]["left"] > 0]
        if y: ended = ("yielded", y[0]); break
    # the questioned's own ballot (hearers disposal), pool_of(untrained 2) = 8, ob even+diff+stakes 0+opposed_ob(2)
    d = Pa; pw = .5; pwd = min(1, max(0, pw + .05 * (d["R"] - 4))); delta = pwd - pw
    sense = 0.0
    if argues:
        sense = 2 * delta * sum(sg * (.25 * (kk / 10) * (sp["R"] - 4) - (.25 * (sp["P"] - 4)) / (2 * (1 - pw))) for sg, sp, kk in argues) / len(argues)
    ends = 0.0
    if isinstance(ended, tuple): ends = .5 if ended[1] == "against" else -.5
    if ended == "broken": ends = .75 if st["against"]["marks"] >= 2 else -.75
    sig = .3 * track + sense + ends - .15 * (d["Wi"] - 4)
    return p_ge(8, EVEN + DIFF + OPP, sig, k=1.0), ended, st["for"]["marks"] + st["against"]["marks"]
N = 60000
for mid in (True, False):
    print(f"== {'all-mid people' if mid else 'random people (attributes 1..7)'} n={N} paired keys; P(questioner carried = S+)")
    for lab, pq, pa in (("questioned: Q auto, A argue-only", "auto", "argue"), ("contest: Q auto, A auto", "auto", "auto"),
                        ("no press: both argue", "argue", "argue"), ("Q press-when-behind, A argue", "press", "argue"),
                        ("Q argue, A press-when-behind", "argue", "press")):
        tot, marks, br = 0.0, 0, 0
        for i in range(N):
            rnd = random.Random(i); Pq, Pa = person(rnd, mid), person(rnd, mid)
            p, e, mk = sitting(rnd, Pq, Pa, pq, pa); tot += p; marks += mk; br += e == "broken"
        print(f"  {lab:34s} {tot/N:.4f}   marks/sitting {marks/N:.3f}  broken {br}")
