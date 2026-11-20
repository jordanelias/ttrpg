"""Antagonist A probe 3: termination, refusals, NaN/inf, extremes, weight-0, hash-seed digest.
PYTHONHASHSEED=<k> python antagonist_v2/p3_extremes.py [digest]"""
import sys, os, copy, math, hashlib, itertools, traceback
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from collections import Counter
from sc2 import host, fixtures as F
from sc2 import engine as E
from sc2.lab import sit, rate, CB, BENCH, CARRIED, chooser, smart

mp, M = F.mid_people(), F.matter()
cast = F.cast()
if len(sys.argv) > 1 and sys.argv[1] == "digest":
    h = hashlib.sha256()
    for rite, kw in (("trial", dict(bench=CB, floor=("guildsmen", "toll_men", "clerk"))), ("debate", dict(bench=CB, floor=("guildsmen",))),
                     ("conversation", {}), ("negotiation", {}), ("questioning", {}), ("inquisition", dict(bench=("bishop", "prior")))):
        for i in range(60):
            inp, card, out, b = sit(cast, rite, F.TOLLS, ("hs", i), effort=3, **kw)
            h.update(repr((out.beats, out.verdicts, b)).encode())
    print(h.hexdigest()); sys.exit()

def H(t): print("\n== " + t, flush=True)
H("TERMINATION / REFUSALS / NaN over rite x effort x room x extreme attributes")
ROWS = (("conversation", {}), ("negotiation", {}), ("questioning", {}), ("inquisition", dict(bench=("c1", "c2"))),
        ("trial", dict(bench=BENCH)), ("debate", dict(bench=BENCH)), ("rally", {}), ("audience", dict(bench=("j1",))),
        ("tribunal", dict(bench=BENCH)), ("arbitration", dict(bench=BENCH)), ("excommunication_deliberation", dict(bench=("c1", "c2", "c3"))),
        ("interrogation", dict(bench=BENCH)), ("council_of_state", dict(bench=BENCH)))
errs = Counter(); bad = Counter(); runs = 0; ex_kinds = {}
attr_sets = {"all1": 1, "all7": 7, "all4": 4}
for (rite, kw), eff, (an, av), (bn, bv), fl, form in itertools.product(ROWS, (0, 1, 3, 9), attr_sets.items(), attr_sets.items(),
                                                                         ((), ("crowd",)), ("full", "abridged")):
    pp = copy.deepcopy(mp)
    for q, v in (("a", av), ("b", bv)):
        pp[q]["attributes"] = {k: v for k in host.ATTRS}
    m = M if rite not in ("rally", "audience") else dict(id="m", parties={"for": "a"}, bears={})
    for i in range(3):
        runs += 1
        try:
            inp, card, out, b = sit(pp, rite, m, ("ex", rite, eff, an, bn, i), effort=eff, floor=fl, form=form, **kw)
            vals = [x.margin for x in out.beats] + [v.net for _, v in out.verdicts] + [t for _, t in out.state.tracks]
            if any(not math.isfinite(v) for v in vals): bad["non-finite"] += 1
            if out.ended not in ("budget", "rested", "yielded"): bad["bad end"] += 1
            if b[0] is None and inp.rite.close != "consent": bad[f"no band {rite} {form} fl={bool(fl)}"] += 1
            if len(out.beats) > card.turns * len([p for p in inp.room if p.side]): bad["overlong"] += 1
        except Exception as e:
            key = f"{rite}/{form}/floor={bool(fl)}: {type(e).__name__}: {str(e)[:70]}"
            errs[key] += 1
print(f"  runs {runs}; non-exception defects {dict(bad)}")
for k, v in sorted(errs.items()): print(f"  EXC x{v}: {k}")

H("weight-0 / single listener / empty floor cohort")
cases = []
pp = copy.deepcopy(mp); pp["crowd"]["weight"] = 0
for rite, kw, m in (("rally", dict(floor=("crowd",)), dict(id="m", parties={"for": "a"}, bears={})),
                    ("rally", dict(floor=(), form="abridged"), dict(id="m", parties={"for": "a"}, bears={})),
                    ("conversation", dict(floor=("crowd",)), M), ("trial", dict(bench=("j1",), floor=("crowd",)), M),
                    ("trial", dict(bench=()), M), ("debate", dict(bench=("j1",)), M)):
    try:
        inp, card, out, b = sit(pp, rite, m, ("w0", 0), effort=2, **kw)
        print(f"  {rite:12} {kw}: band {b[0]} verdicts {[(i, round(v.net - v.ob, 2)) for i, v in out.verdicts]}")
    except Exception as e:
        print(f"  {rite:12} {kw}: {type(e).__name__}: {str(e)[:90]}")

H("EXTREMES: all-7 against all-1 (and the reverse); saturation")
for rite, kw in (("conversation", {}), ("trial", dict(bench=BENCH)), ("debate", dict(bench=BENCH)), ("negotiation", {})):
    out_ = []
    for av, bv in ((7, 1), (1, 7), (7, 7), (1, 1)):
        pp = copy.deepcopy(mp)
        pp["a"]["attributes"] = {k: av for k in host.ATTRS}; pp["b"]["attributes"] = {k: bv for k in host.ATTRS}
        out_.append(f"{av}v{bv} {rate(pp, rite, M, 600, ('xt', rite), effort=3, **kw):.3f}")
    print(f"  {rite:12} P(for carried): " + "  ".join(out_))
# the judge: all-1 vs all-7 decider with an insincere, wandering speaker
pp = copy.deepcopy(mp); pp["a"]["layers"] = dict(convictions={"x": 5}); pp["a"]["attributes"].update(focus=1)
mm = dict(M, bears={"x": -1.0})
for jv in (1, 7):
    q = copy.deepcopy(pp); q["j1"]["attributes"] = {k: jv for k in host.ATTRS}
    print(f"  trial, insincere wandering accuser, presiding judge all-{jv}: carried {rate(q, 'trial', mm, 1200, 'jx', bench=('j1',), effort=3, strife='famine'):.3f}")

H("R2 at the quiet tell: the zero slopes, with a control that gives each attribute an object")
for attr, lab, kw in (("focus", "quiet room", {}), ("focus", "famine (unrest 0.75)", dict(strife="famine")),
                      ("will", "quiet room", {}), ("attunement", "flat hearer", {})):
    r = {}
    for lev in (1, 7):
        pp = copy.deepcopy(mp); pp["a"]["attributes"][attr] = lev
        r[lev] = rate(pp, "conversation", M, 3000, ("r2", attr), form="abridged", **kw)
    print(f"  tell, speaker {attr:10} 1 vs 7, {lab:22}: {r[1]:.3f} vs {r[7]:.3f} (diff {r[7]-r[1]:+.3f})")
pk = copy.deepcopy(mp); pk["b"]["layers"] = dict(pursuits={"p": 0.95}, convictions={"c": 0}, relationships={"a": -0.5})
r = {}
for lev in (1, 7):
    pp = copy.deepcopy(pk); pp["a"]["attributes"]["attunement"] = lev
    r[lev] = rate(pp, "conversation", M, 3000, ("r2a",), form="abridged")
print(f"  tell, speaker attunement 1 vs 7, sharply peaked hearer: {r[1]:.3f} vs {r[7]:.3f} (diff {r[7]-r[1]:+.3f}); perfect-reading ceiling:", end=" ")
r0 = rate(pk, "conversation", M, 3000, ("r2a",), form="abridged", D=host.dials(read_blur=0.0))
print(f"{r0:.3f}")

H("Why the trial expresses Reason weakly: the presiding track by speaker Reason, and the share of a's raised track undone by answers")
for lev in (1, 7):
    pp = copy.deepcopy(mp); pp["a"]["attributes"]["reason"] = lev
    raised = undone = trk = 0.0; n = 800
    for i in range(n):
        inp, card, out, b = sit(pp, "trial", M, ("why", i), bench=BENCH, effort=3)
        trk += dict(out.state.tracks)["j1"]
        for x in out.beats:
            d = dict(x.moved).get("j1", 0.0)
            if x.mover == "a" and x.relation == "raises": raised += d
            if x.mover == "b" and x.relation == "answers": undone += d
    print(f"  Reason {lev}: mean presiding track {trk/n:+.2f}; a's raises put {raised/n:+.2f} on it, b's answers {undone/n:+.2f}")
