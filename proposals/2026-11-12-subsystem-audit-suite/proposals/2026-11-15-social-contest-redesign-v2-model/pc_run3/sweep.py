"""STEP 4 speaker sweep: attribute of `a` (the `for` speaker) 1..7, all else mid; auto NPC choosers both sides.
usage: python sweep.py N [dialset]   dialset: shipped | ctl_<attr> (that attribute's carrying setting removed)"""
import sys, json, copy
from multiprocessing import Pool
from common import *
from dataclasses import replace

def ctl_dials(attr):
    D = dict(host.SHIPPED)
    if attr == "focus": D.update(press_pull=0.0, rattle_pull=0.0, heckle=0.0, off_step=0.0)
    if attr == "reason": D.update(relevance=0, gap_step=0.0)
    if attr == "attunement": D.update(read_blur=0.0, bias_step=0.0)
    if attr == "presence": D.update(heard_step=0.0)
    if attr == "grace": D.update(esteem_step=0.0, temper_break=99.0)
    if attr == "will": D.update(weary_step=0.0, temper_break=99.0, awe_step=0.0)
    return host.MappingProxyType(D)

def run_cell(args):
    fx, ctx, attr, n, dialset = args
    pp0 = blank() if fx == "blank" else rich(); m = mat(fx)
    kw = {}
    if dialset != "shipped":
        kw["D"] = ctl_dials(attr)
    res = {}
    for x in range(1, 8):
        pp = copy.deepcopy(pp0); pp["a"]["attributes"][attr] = x
        car = 0; mm = 0.0; st = dict(drift=0, rel=0, heard=0, est=0, broke=0, nb=0, rattled=0, rests=0, yielded=0, presses=0, argues=0)
        for i in range(n):
            if dialset != "shipped" and attr == "reason":
                rite, base = CTX[ctx]; k = dict(base); k.update(kw)
                inp, card = host.build(pp, rite, m, **k)
                inp = replace(inp, grounds=tuple((g, -1.0, e) for g, _, e in inp.grounds))  # Reason's dice share 0
                out = proceed(inp, draw(("sw", i), "act", rite)); b = host.act_band(inp, out)
            else:
                inp, card, out, b = sit(pp, ctx, m, ("sw", i), **kw)
            car += b[0] in CARRIED
            mm += (b[1] or 0.0)
            for bt in out.beats:
                if bt.rattled == "a": st["rattled"] += 1
                if bt.mover != "a": continue
                st["nb"] += 1; st["drift"] += bt.drift; st["rel"] += bt.relevance; st["heard"] += bt.heard
                st["est"] += bt.esteem; st["broke"] += bt.broke; st["rests"] += bt.move == "rest"
                st["presses"] += bt.move == "press"; st["argues"] += bt.move == "argue"
            st["yielded"] += (out.ended == "yielded" and out.ended_by == "a")
        nb = max(1, st["nb"])
        res[x] = dict(car=car / n, m=mm / n, drift=st["drift"] / nb, rel=st["rel"] / nb, heard=st["heard"] / nb,
                      est=st["est"] / nb, broke=st["broke"] / nb, rests=st["rests"] / nb, presses=st["presses"] / nb,
                      argues=st["argues"] / nb, rattled=st["rattled"] / n, yielded=st["yielded"] / n, beats=st["nb"] / n)
    return (fx, ctx, attr, dialset, res)

if __name__ == "__main__":
    n = int(sys.argv[1]); dialset = sys.argv[2] if len(sys.argv) > 2 else "shipped"
    fxs = sys.argv[3].split(",") if len(sys.argv) > 3 else ["blank", "rich"]
    jobs = [(fx, ctx, a, n, dialset) for fx in fxs for ctx in CTX for a in ATTRS]
    with Pool(4) as P:
        out = P.map(run_cell, jobs)
    json.dump(out, open(f"sweep_{dialset}_{n}.json", "w"))
    print("done", len(out))
