"""P3 builds: single-attribute dump/mandatory test, profiles AR-49/50, P6R2 vs R6P2 by venue, all-7 vs all-1.
Auto policy both sides. carry = P(`for` carried: Success+ on act_margin).
    PYTHONHASHSEED=0 python lane3/p3_builds.py [n] [part ...]   parts: attr profiles venue extremes"""
import sys
from dataclasses import replace

from harness import run, person, ATTRS, dialmod

n = int(sys.argv[1]) if len(sys.argv) > 1 else 3000
parts = sys.argv[2:] or ["attr", "profiles", "venue", "extremes"]
D = dialmod.shipped()
MOV = dict(pursuits={"x": 0.6}, convictions={"c": 3})


def crowd_extra():
    return [person("crowd", weight=30, proofs=0, regard={}), person("onl", weight=20, proofs=0)]


def R(row, A, B, label, **kw):
    extra = None
    if row == "rally":
        extra = crowd_extra()
    return run(row, A, B, n=n, label=label, extra=extra, **kw)


ROWS = ["conversation", "negotiation", "questioning", "arbitration", "legal_trial", "rally"]

if "attr" in parts:
    print("== single-attribute: `for` speaker attr at 1 / 4 / 7 (others 4) vs mid opponent; and the same on the `against` side")
    mid = person("x", **MOV)
    for row in ROWS:
        base = R(row, mid, mid, f"attr:{row}:base")
        line = [f"{row:13} base={base['carry']:.3f}±{base['se']:.3f} |"]
        for a in ATTRS:
            lo = R(row, person("x", {a: 1}, **MOV), mid, f"attr:{row}:{a}:1:for")
            hi = R(row, person("x", {a: 7}, **MOV), mid, f"attr:{row}:{a}:7:for")
            line.append(f" {a[:4]} {lo['carry']:.3f}/{hi['carry']:.3f}")
        print("".join(line))
        if row == "rally":
            continue
        line = [f"{'  as against':13} base={base['carry']:.3f}         |"]
        for a in ATTRS:
            lo = R(row, mid, person("x", {a: 1}, **MOV), f"attr:{row}:{a}:1:ag")
            hi = R(row, mid, person("x", {a: 7}, **MOV), f"attr:{row}:{a}:7:ag")
            line.append(f" {a[:4]} {lo['carry']:.3f}/{hi['carry']:.3f}")
        print("".join(line))

if "profiles" in parts:
    print("\n== AR-49/50: P6/G2 vs P2/G6 as `for` vs mid opponent; routine standard; gallery room (patched)")
    from scmodel.records import Room
    for row in ("conversation", "negotiation", "arbitration", "legal_trial"):
        for room in ("gallery", "native"):
            def patch(t, row=row):
                return replace(t, standard=D["standard_demand"]["routine"])
            res = {}
            for nm, at in (("P6G2", {"presence": 6, "grace": 2}), ("P2G6", {"presence": 2, "grace": 6})):
                r = run(row, person("x", at, **MOV), person("y", **MOV), n=n, label=f"prof:{row}:{room}:{nm}",
                        typ_patch=patch if room == "gallery" else None,
                        extra=[person("g1", proofs=0), person("g2", proofs=0)] if room == "gallery" else None)
                res[nm] = r
            print(f"  {row:13} {room:8} carry P6G2={res['P6G2']['carry']:.3f}±{res['P6G2']['se']:.3f} "
                  f"P2G6={res['P2G6']['carry']:.3f}±{res['P2G6']['se']:.3f}  room={res['P6G2']['inp'].room.audience}")

if "venue" in parts:
    print("\n== P6/R2 (orator) vs R6/P2 (scholar), head to head, both seatings; and each vs mid")
    O = person("o", {"presence": 6, "reason": 2}, **MOV)
    Sc = person("s", {"presence": 2, "reason": 6}, proofs=2.0, **MOV)
    O2 = person("o", {"presence": 6, "reason": 2}, proofs=2.0, **MOV)
    mid = person("m", **MOV)
    for row in ROWS:
        a = R(row, O2, Sc, f"ven:{row}:OS")
        b = R(row, Sc, O2, f"ven:{row}:SO")
        c = R(row, O2, mid, f"ven:{row}:OM")
        d = R(row, Sc, mid, f"ven:{row}:SM")
        print(f"  {row:13} orator-for vs scholar {a['carry']:.3f} | scholar-for vs orator {b['carry']:.3f} | "
              f"orator vs mid {c['carry']:.3f} | scholar vs mid {d['carry']:.3f}  (se<={max(x['se'] for x in (a,b,c,d)):.3f}) room={c['inp'].room.audience}")

if "extremes" in parts:
    print("\n== all-7 (rank 3, proofs 3) vs all-1 (rank 0, proofs 0), and all-7 vs all-1 attributes only")
    for row in ROWS:
        s7 = person("s", {k: 7 for k in ATTRS}, rank=3, proofs=3, **MOV)
        s1 = person("w", {k: 1 for k in ATTRS}, rank=0, proofs=0, **MOV)
        a7 = person("s", {k: 7 for k in ATTRS}, **MOV)
        a1 = person("w", {k: 1 for k in ATTRS}, **MOV)
        r1 = R(row, s7, s1, f"ext:{row}:71")
        r2 = R(row, s1, s7, f"ext:{row}:17")
        r3 = R(row, a7, a1, f"ext:{row}:a71")
        r4 = R(row, a1, a7, f"ext:{row}:a17")
        print(f"  {row:13} full7-for {r1['carry']:.3f} ends={dict(r1['ends'])} | full1-for {r2['carry']:.3f} | "
              f"attr7-for {r3['carry']:.3f} | attr1-for {r4['carry']:.3f}")
