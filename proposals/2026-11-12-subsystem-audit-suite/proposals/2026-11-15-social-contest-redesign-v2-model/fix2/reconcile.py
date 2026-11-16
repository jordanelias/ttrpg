"""The reconcile pass: B12's Focus carrier restored; the regime's gravity; the arms isolated; the claims measured."""
from common import *
from dataclasses import replace as rp
from sc2 import acts
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
L = dict(pursuits={"grain": 0.9}, convictions={"law": 4}); MM = dict(id="m", parties={"for": "a", "against": "b"}, bears={"grain": 1.0, "law": 0.5})
def base():
    pp = copy.deepcopy(mp); pp["j1"]["layers"] = dict(L); pp["a"]["attributes"]["will"] = 2; return pp

H(f"R1 the adjudicator's Focus as the theatre filter: `for` (Will 2) argues, the other side presses him every turn; `for` carried by the judge's Focus (n={N})")
for lab, DD in (("shipped", host.dials(bias_step=0.0, off_step=0.0)), ("control: a rattle moves nobody (rattle_gain 0)", host.dials(bias_step=0.0, off_step=0.0, rattle_gain=0.0))):
    r = {}
    for x in (1, 4, 7):
        pp = base(); pp["j1"]["attributes"]["focus"] = x
        r[x] = carried(pp, "trial", MM, N, "r1", bench=("j1",), effort=3, D=DD, deciders={"a": only("argue"), "b": only("press")})
    print(f"  [{lab}] judge's Focus 1 / 4 / 7: {r[1]:.3f} / {r[4]:.3f} / {r[7]:.3f} ({r[7]-r[1]:+.3f}, z {z(r[7], r[1], N):+.1f})")
pp = base()
for x in (1, 7):
    pp["j1"]["attributes"]["focus"] = x
    inp, card = host.build(pp, "trial", MM, bench=("j1",), effort=3)
    print(f"  the theatre weight at judge's Focus {x}: {E.theatre([p for p in inp.room if p.id == 'j1'][0], D):.2f}")

H(f"R2 the regime's gravity (one method with strife): the same case, crown against theocracy, standard held at the crown's; `for` carried (n={N})")
def run_reg(reg, gdelta, n=N):
    k = 0
    for i in range(n):
        inp, card = host.build(mp, "trial", M, bench=BENCH, effort=3, regime=reg)
        inp = rp(inp, rite=rp(inp.rite, standard=host.RITES["trial"]["standard"], silence="refusal", admits=host.RITES["trial"]["admits"],
                              reason_lean=host.RITES["trial"]["reason_lean"], gravity=inp.rite.gravity if gdelta else 0.0))
        out = proceed(inp, draw(("r2", i), "act", "trial")); k += host.act_band(inp, out)[0] in CARRIED
    return k / n, inp.rite.gravity
for lab, reg, g in (("crown", "crown", True), ("theocracy (gravity 0.5)", "theocracy", True), ("theocracy, the delta at 0 (control)", "theocracy", False)):
    p, gv = run_reg(reg, g); print(f"  {lab:38s} gravity {gv:.2f}: carried {p:.3f}")

H(f"R3 `admit_step` isolated: the crown's trial, the standard fixed at 5, only the `silence` cell changed; the accused rests every turn (n={N})")
def sil(cell, DD):
    k = 0
    for i in range(N):
        inp, card = host.build(mp, "trial", M, bench=BENCH, effort=3, D=DD)
        inp = rp(inp, rite=rp(inp.rite, silence=cell))
        out = proceed(inp, draw(("r3", i), "act", "trial"), deciders={"b": only("rest")}); k += host.act_band(inp, out)[0] in CARRIED
    return k / N
for lab, DD in (("shipped", D), ("admit_step 0", host.dials(admit_step=0.0))):
    a_, r_ = sil("admits", DD), sil("refusal", DD)
    print(f"  [{lab}] `admits` {a_:.3f} against `refusal` {r_:.3f} ({a_ - r_:+.3f}, z {z(a_, r_, N):+.1f})")

H(f"R4 `grain` and `grudge` isolated: a broken man's beats (trial, `a` presses every turn), each setting at 0 against full (n={N // 2})")
def broken_moves(b, DD, rel=None):
    pp = copy.deepcopy(mp); pp["b"]["attributes"].update(b)
    if rel: pp["b"]["layers"] = dict(relationships={"a": rel}, pursuits={"p": 0.9}, convictions={"c": 1})
    c = Counter(); g = Counter()
    for i in range(N // 2):
        inp, card, out, bb = sit(pp, "trial", M, ("r4", i), bench=BENCH, effort=3, D=DD, deciders={"a": only("press")})
        for x in out.beats:
            if x.mover == "b" and x.broke:
                c[x.move] += 1
                if x.move == "argue": g[x.ground] += 1
    t = sum(c.values()) or 1; tg = sum(g.values()) or 1
    return f"broken beats {sum(c.values())}: press {c['press']/t:.2f} argue {c['argue']/t:.2f} (consequence {g['consequence']/tg:.2f}) concede {c['concede']/t:.2f}"
for lab, DD in (("full", D), ("grain 0", host.dials(grain=0.0)), ("grudge 0", host.dials(grudge=0.0))):
    print(f"  W2 G2 who wants much and holds a grudge against `a` [{lab:8s}] {broken_moves(dict(will=2, grace=2), DD, rel=-0.9)}")

H(f"R5 contumacy on the same n: the accused rests every turn in a crown trial; per sitting, over {N} sittings")
cl = rg = 0.0
for i in range(N):
    inp, card, out, b = sit(mp, "trial", M, ("r5", i), bench=BENCH, effort=3, deciders={"b": only("rest")})
    w = host.new_world(); host.fold(w, mp, inp, card, out, M)
    cl += sum(1 for e in w["ledgers"].get("j1", []) if e[0] == "contumacy"); rg += w["regard"].get(("j1", "b"), 0.0)
print(f"  contumacy claims in the judge's ledger {cl / N:.2f} a sitting; the judge's regard for the silent man {rg / N:+.3f}")

H(f"R6 appeals by the side a third party rigged FOR: the tilt is never among his grounds (gap 5, a lord rigs for `a`, rig 1; n={N // 2})")
def cast_with():
    pp = F.mid_people(); pp["a"]["faction"] = pp["b"]["faction"] = "Crown"
    pp["lord"] = F.P("lord", office=F.seat(6, "Crown"), layers=dict(relationships={"a": 0.8})); return pp
pp = cast_with(); los = tilt_in = app = 0
for i in range(N // 2):
    inp, card, out, b = sit(pp, "trial", M, ("r6", i), bench=BENCH, floor=("crowd",), effort=3, arranger="lord", rig=1.0)
    if b[0] in CARRIED or b[0] == "partial": continue
    w = host.new_world(); band, _ = host.fold(w, pp, inp, card, out, M)
    j = sorted((p for p in inp.room if p.decides), key=lambda p: (-p.precedence, p.id))[0]
    brute, rec = host.reception(inp, j)
    los += 1; aw = w["appeal_weight"].get("m", 0.0); tilt_in += aw > brute + 0.5 + 1e-9
    act, _ = acts.after(w, pp, inp, card, out, M, band); app += act == "appeal"
print(f"  `a` lost {los}; appeal weights holding more than brute + wrong (i.e. any tilt): {tilt_in}; he appealed {app}")

H("R7 a pinned pair: the scholar's regard for the bully set at -0.95 before the first season; 30 runs x 12 seasons of the driver")
cast, T = F.cast(), F.TOLLS
SCHED = [("trial", dict(T, parties={"for": "scholar", "against": "bully"}), dict(bench=CB, floor=FL, effort=3, arranger="bully", rig=1.0)),
         ("negotiation", dict(id="grain", parties={"for": "orator", "against": "diplomat"}, bears={"grain": 1.0, "trade": 0.5}), dict(effort=3)),
         ("questioning", dict(T, id="who", parties={"for": "fox", "against": "bully"}), dict(effort=3))]
traj = defaultdict(list)
for run in range(30):
    w = host.new_world(); w["regard"][("scholar", "bully")] = -0.95
    for s_ in range(12):
        acts.season(w, cast, SCHED, s_, appeal_bench=("judge3", "judge"), key=("r7", run))
        traj[s_].append(w["regard"].get(("scholar", "bully"), 0.0))
print("  by season: " + ", ".join(f"s{s_} {sum(v)/len(v):+.2f}" for s_, v in traj.items() if s_ in (0, 1, 2, 3, 5, 8, 11)))
print(f"  share of runs back above -0.5 by season 3 / 11: {sum(x > -0.5 for x in traj[3]) / 30:.2f} / {sum(x > -0.5 for x in traj[11]) / 30:.2f}")
