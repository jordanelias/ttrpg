"""P8: (i) ground choice beyond argmax fit (the blend); (ii) the automatic `against`'s press share by his Reason;
(iii) R12 steering of the decider: divert before low/high Focus, a planted deceive before low/high Attunement, an orator
vs a scholar before low/high Reason (moved_by held fixed); (iv) negotiation: does the `against` speaker's play matter;
(v) the actor's effort choice.
    PYTHONHASHSEED=0 python lane3/p8_misc.py [n]"""
import sys
from collections import Counter
from dataclasses import replace

import harness
from harness import run, person, dialmod, P, STRATS, s_argue_fixed

n = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
PARTS = sys.argv[2:] or ["i", "ii", "iii", "iv", "v"]
D = dialmod.shipped()
MOV = dict(pursuits={"x": 0.6}, convictions={"c": 3})
mid = person("m", **MOV)
G = ("evidence", "consequence", "authority", "solidarity")

if "i" in PARTS:
  print("(i) `for` argue on each fixed ground vs argue_true (argmax true fit), vs mid opponent, conversation & rally")
  for row in ("conversation", "rally"):
    for nm, at, pr in (("orator P6R2", {"presence": 6, "reason": 2}, 0), ("scholar R6P2", {"presence": 2, "reason": 6}, 2)):
        A = person("a", at, proofs=pr, **MOV)
        extra = [person("crowd", weight=30, proofs=0), person("onl", weight=20, proofs=0)] if row == "rally" else None
        cells = []
        for s in ["argue_true"] + [s_argue_fixed(g) for g in G]:
            r = run(row, A, mid, s, "auto", n=n, label=f"p8i:{row}:{nm}", extra=extra)
            cells.append(f"{s if isinstance(s, str) else s.__name__}={r['carry']:.3f}")
        print(f"  {row:12} {nm:13} " + " ".join(cells) + f" se~{r['se']:.3f}")

print("\n(ii) automatic `against` in conversation: share of his speeches that are presses, by his Reason")
for v in (1, 4, 7):
    r = run("conversation", mid, person("b", {"reason": v}, **MOV), n=n, label="p8ii")
    mv = Counter({k[1]: c for k, c in r["moves"].items() if k[0] == "b"})
    print(f"  Reason {v}: press share {mv['press'] / sum(mv.values()):.3f}  carry {r['carry']:.3f}")


def fix_mb(inp):
    """hold every person's moved_by at one peaked vector so the decider's attribute moves only his ballot."""
    mb = (("evidence", 0.5), ("consequence", 0.6), ("authority", 0.5), ("solidarity", 0.5))
    sp = tuple(replace(S, moved_by=mb) for S in inp.speakers)
    ds = tuple(replace(d, moved_by=mb) for d in inp.deciders)
    return replace(inp, speakers=sp, deciders=ds)


orig_run_build = harness.build_input


def run_patched(row, A, B, sf, sa, label, typ_patch=None, inp_patch=None):
    def bi(*a, **k):
        inp = orig_run_build(*a, **k)
        return inp_patch(inp) if inp_patch else inp
    harness.build_input = bi
    try:
        return run(row, A, B, sf, sa, n=n, label=label, typ_patch=typ_patch)
    finally:
        harness.build_input = orig_run_build


print("\n(iii) R12 steering in conversation (the decider is the one addressed); moved_by held fixed")
for f in (1, 4, 7):
    B = person("b", {"focus": f}, **MOV)
    cells = [f"{s}={run_patched('conversation', mid, B, s, 'auto', f'p8iii:f{f}', inp_patch=fix_mb)['carry']:.3f}"
             for s in ("argue_best", "divert_alt", "divert")]
    print(f"  decider Focus {f}: " + " ".join(cells))


def add_deceive(t):
    from scmodel.host import _move_record
    mv = dict(t.moves)
    mv["for"] = tuple(mv["for"]) + (_move_record("deceive", D),)
    return replace(t, moves=tuple(mv.items()))


A = person("a", ranks=None, **MOV)
A["ranks"] = {"argue": 1, "deception": 1}
for at in (1, 4, 7):
    B = person("b", {"attunement": at}, **MOV)
    cells = [f"{s}={run_patched('conversation', A, B, s, 'auto', f'p8iii:a{at}', typ_patch=add_deceive, inp_patch=fix_mb)['carry']:.3f}"
             for s in ("argue_best", "deceive")]
    print(f"  decider Attunement {at} (deceive planted, deception rank 1): " + " ".join(cells))
O = person("o", {"presence": 6, "reason": 2}, proofs=0, **MOV)
Sc = person("s", {"presence": 2, "reason": 6}, proofs=3, **MOV)
for rs in (1, 4, 7):
    B = person("b", {"reason": rs}, **MOV)
    o = run_patched("conversation", O, B, "auto", "auto", f"p8iii:r{rs}", inp_patch=fix_mb)
    s = run_patched("conversation", Sc, B, "auto", "auto", f"p8iii:r{rs}", inp_patch=fix_mb)
    print(f"  decider Reason {rs}: orator(P6R2, no proofs) {o['carry']:.3f}  scholar(R6P2, 3 proofs) {s['carry']:.3f}")

print("\n(iv) negotiation (mutual): `against` auto vs rest vs press_always vs argue_true; `for` auto")
for sa in ("auto", "rest", "press_always", "argue_true", "concede_early"):
    r = run("negotiation", mid, mid, "auto", sa, n=n, label="p8iv")
    print(f"  against={sa:13} P(for's act Success+)={r['carry']:.3f}  mean final track {r['track']:+.2f}")

print("\n(v) the actor's effort (both sides get effort+1): P(for carried), mid people")
for row in ("conversation", "negotiation", "questioning", "legal_trial"):
    cells = []
    for e in (0, 1, 2, 4):
        r = run(row, mid, mid, n=n, effort=e, label=f"p8v:{row}:{e}")
        cells.append(f"e{e}={r['carry']:.3f}(nx {r['nx']:.1f}, ends {dict(r['ends'])})")
    print(f"  {row:12} " + " ".join(cells))
