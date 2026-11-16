"""C2: a party who also decides. His argue vs rest must differ; no speaker-attribute slope changes sign with who decides."""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
A, R = only("argue"), only("rest")

def cases(pp):
    """(label, rite, matter, kw, the party who decides)"""
    return [("questioning: the questioned man b decides", "questioning", M, dict(effort=3), "b"),
            ("conversation: the man addressed b decides", "conversation", M, dict(effort=3), "b"),
            ("audience: the noble j1 is the other party and decides", "audience", F.matter(ag="j1"), dict(bench=("j1",), effort=3), "j1"),
            ("inquisition: the inquisitor c1 accuses and judges", "inquisition", F.matter(f="c1", ag="b"), dict(bench=("c1",), effort=3), "c1")]

H(f"C2.1 the party who decides: `for` carried when HE argues every turn / rests every turn / plays automatically (n={N})")
for lab, rite, m, kw, who in cases(mp):
    r = {k: carried(mp, rite, m, N, "c2a", deciders={who: pol} if pol else None, **kw) for k, pol in (("argue", A), ("rest", R), ("auto", None))}
    good = "argue - rest toward HIS side"
    s = SIGN["for"] if who == m["parties"]["for"] else -1.0
    dlt = s * (r["argue"] - r["rest"])
    print(f"  {lab:58s} argue {r['argue']:.3f} rest {r['rest']:.3f} auto {r['auto']:.3f} | {good} {dlt:+.3f} (z {z(r['argue'], r['rest'], N) * s:+.1f})")

H(f"C2.2 speaker Reason 1 -> 7 (`a`, arguing every turn) by WHO decides: the slope's sign must not change (n={N})")
for lab, rite, m, kw, other in (("a third-party bench (trial, j1 decides)", "trial", M, dict(bench=BENCH, effort=3), "b"),
                                ("the other party decides (conversation)", "conversation", M, dict(effort=3), "b"),
                                ("the other party decides (questioning)", "questioning", M, dict(effort=3), "b"),
                                ("a noble who is the other party (audience)", "audience", F.matter(ag="j1"), dict(bench=("j1",), effort=3), "j1")):
    for oset in ({}, dict(reason=7, grace=2)):
        r = {}
        for x in (1, 7):
            pp = copy.deepcopy(mp); pp["a"]["attributes"]["reason"] = x; pp[other]["attributes"].update(oset)
            r[x] = carried(pp, rite, m, N, "c2b", deciders={"a": A}, **kw)
        print(f"  {lab:44s} other {str(oset or 'mid'):28s} a Reason 1/7: {r[1]:.3f} -> {r[7]:.3f} ({r[7]-r[1]:+.3f}, z {z(r[7], r[1], N):+.1f})")

H(f"C2.2b the other speaker attributes 1 -> 7 (`a` arguing every turn) by who decides: no sign change (n={N})")
for attr in ("presence", "grace", "will", "attunement"):
    row = []
    for lab, rite, m, kw in (("bench", "trial", M, dict(bench=BENCH, effort=3)), ("the other party", "questioning", M, dict(effort=3)),
                             ("a noble", "audience", F.matter(ag="j1"), dict(bench=("j1",), effort=3))):
        r = {}
        for x in (1, 7):
            pp = copy.deepcopy(mp); pp["a"]["attributes"][attr] = x
            r[x] = carried(pp, rite, m, N, "c2s", deciders={"a": A}, **kw)
        row.append(f"{lab} {r[7]-r[1]:+.3f}")
    print(f"  {attr:10s} " + "; ".join(row))

H(f"C2.3 a man who says NOTHING (a rests every turn): does his own attribute move the deciding party b's verdict? (b argues; n={N})")
for rite in ("conversation", "questioning"):
    for attr, bset in (("reason", dict(reason=7, grace=1)), ("will", {}), ("presence", {})):
        r = {}
        for x in (1, 7):
            pp = copy.deepcopy(mp); pp["a"]["attributes"][attr] = x; pp["b"]["attributes"].update(bset)
            r[x] = carried(pp, rite, M, N, "c2c", effort=3, deciders={"a": R, "b": A})
        print(f"  {rite:12s} silent a's {attr:9s} 1 -> 7 (b {bset or 'mid'}): {r[1]:.3f} -> {r[7]:.3f} ({r[7]-r[1]:+.3f})")
