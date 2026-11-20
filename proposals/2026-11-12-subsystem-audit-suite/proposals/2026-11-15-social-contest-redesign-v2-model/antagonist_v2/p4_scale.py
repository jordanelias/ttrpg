"""Antagonist A probe 4: the judge's three with Will held; abridged vs full for a strong speaker; D5; the view's
`acc` and the auto==smart identity. PYTHONHASHSEED=0 python antagonist_v2/p4_scale.py"""
import sys, os, copy, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sc2 import host, fixtures as F
from sc2.lab import sit, rate, BENCH, CARRIED, chooser, smart, se
mp, M = F.mid_people(), F.matter()
def H(t): print("\n== " + t, flush=True)
N = 1500

H("the presiding judge's Reason/Focus/Attunement 1 vs 7 (Will held at 4), trial, an insincere accuser who wanders (famine)")
pp = copy.deepcopy(mp); pp["a"]["layers"] = dict(convictions={"x": 5}); pp["a"]["attributes"].update(focus=1)
mm = dict(M, bears={"x": -1.0})
for attr in ("reason", "focus", "attunement"):
    r = {}
    for lev in (1, 7):
        q = copy.deepcopy(pp); q["j1"]["attributes"][attr] = lev
        r[lev] = rate(q, "trial", mm, N, ("jd", attr), bench=("j1",), effort=3, strife="famine")
    print(f"  judge {attr:10} 1 vs 7: {r[1]:.3f} vs {r[7]:.3f}  diff {r[7]-r[1]:+.3f} (2se {2*math.hypot(se(r[1],N), se(r[7],N)):.3f})")
# insincerity actually occurring?
ins = 0; nb = 0
for i in range(300):
    inp, card, out, b = sit(pp, "trial", mm, ("jd2", i), bench=("j1",), effort=3, strife="famine")
    for x in out.beats:
        if x.mover == "a" and x.move == "argue": nb += 1; ins += x.insincere > 0
print(f"  (the automatic accuser argues insincerely in {ins}/{nb} of his speeches: his grain steers him off the ploy)")

H("the same strong speaker, abridged tell vs played-out sitting (vs all-mid)")
for lab, upd in (("Reason 7", dict(reason=7)), ("Presence 7", dict(presence=7)), ("Grace 7", dict(grace=7)), ("all 7", {k: 7 for k in host.ATTRS})):
    q = copy.deepcopy(mp); q["a"]["attributes"].update(upd)
    t = rate(q, "conversation", M, N, ("ab", lab), form="abridged")
    f = rate(q, "conversation", M, N, ("ab", lab), effort=3)
    t0 = rate(mp, "conversation", M, N, ("ab", lab), form="abridged"); f0 = rate(mp, "conversation", M, N, ("ab", lab), effort=3)
    print(f"  {lab:10}: tell {t:.3f} (equals {t0:.3f}, gain {t-t0:+.3f}) | full conversation {f:.3f} (equals {f0:.3f}, gain {f-f0:+.3f})")

H("auto == smart for flat people (the T20 test is an identity there)")
same = tot = 0
from sc2 import engine as E
orig = E.auto
def spy(view, me, D):
    global same, tot
    a = orig(view, me, D); s = smart(view, me); tot += 1; same += tuple(a) == tuple(s); return a
E.auto = spy
for i in range(300): sit(mp, "trial", M, ("id", i), bench=BENCH, effort=3)
E.auto = orig
print(f"  all-mid trial: automatic choice == view-only max-ev choice in {same}/{tot} decisions")
