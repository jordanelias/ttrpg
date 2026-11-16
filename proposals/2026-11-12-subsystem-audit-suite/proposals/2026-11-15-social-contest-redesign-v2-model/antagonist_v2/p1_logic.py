"""Antagonist A probe 1: leaks, yield coherence, card odds, fold drops, resume. PYTHONHASHSEED=0 python antagonist_v2/p1_logic.py"""
import sys, os, copy, math
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from collections import Counter
from sc2 import host, fixtures as F
from sc2 import engine as E
from sc2.lab import sit, CB, BENCH, CARRIED, chooser
from scmodel.rng import draw

mp, M = F.mid_people(), F.matter()
cast = F.cast()

def H(t): print("\n== " + t)

# ---------------------------------------------------------------- 1 shared-noise leak in the View
H("LEAK: live_own - live_theirs vs the truth (shared xm)")
# wrap build_view to capture the views and compute truths
cap = []
orig = E.build_view
def spy(inp, st, mover, rng, turns_left):
    v = orig(inp, st, mover, rng, turns_left)
    if v.live_theirs and v.live_own:
        hs = [p for p in inp.room if p.decides and p.id != mover.id] or [E._lead(inp, E._other(mover.side))]
        W = sum(h.weight for h in hs) or 1.0
        pts = {p.id: p for p in st.points}
        def tru(pid, tw):
            return E.SIGN[tw] * sum(h.weight * dict(pts[pid].held).get(h.id, 0.0) for h in hs) / W
        t_th = tru(v.live_theirs[0], E._other(mover.side)); t_own = tru(v.live_own[0], mover.side)
        # also the mood term: m_seen = SIGN*mood + 0.5 blur xm (unclipped case)
        true_mood = E.SIGN[mover.side] * E.mood(inp, st)
        cap.append((v.live_own[3] - v.live_theirs[3], t_own - t_th, v.acc, v.live_theirs[3] - t_th,
                    v.live_theirs[3] - 2 * v.mood, t_th - 2 * true_mood, abs(v.mood) < 0.999))
    return v
E.build_view = spy
for i in range(400):
    sit(cast, "trial", F.TOLLS, ("lk", i), bench=CB, floor=("guildsmen", "toll_men", "clerk"), effort=3)
E.build_view = orig
n = len(cap)
err_diff = [abs(a - b) for a, b, *_ in cap]
err_each = [abs(d) for _, _, _, d, *_ in cap]
lowacc = [c for c in cap if c[2] < 0.3]
mix = [abs(c[4] - c[5]) for c in cap if c[6]]
print(f"  views with both live points: {n}; |believed(own-theirs) - true(own-theirs)| max {max(err_diff):.3f} mean {sum(err_diff)/n:.3f} (rounding to 0.1 bounds it at 0.1)")
print(f"  for comparison |believed theirs - true theirs| mean {sum(err_each)/n:.3f}; low-accuracy readers (acc<0.3): n={len(lowacc)}, mean abs error on 'theirs' {sum(abs(c[3]) for c in lowacc)/max(1,len(lowacc)):.3f}, on the difference {sum(abs(c[0]-c[1]) for c in lowacc)/max(1,len(lowacc)):.3f}")
print(f"  live_theirs - 2*mood_seen vs truth (mood unclipped, n={len(mix)}): mean abs err {sum(mix)/max(1,len(mix)):.3f}")

# ---------------------------------------------------------------- 2 a yield that still wins
H("YIELD COHERENCE: the side that concedes the last rung / accepts, and the verdict")
for rite, kw, who in (("questioning", {}, "b"), ("conversation", {}, "a"), ("conversation", {}, "b"),
                      ("trial", dict(bench=BENCH), "b"), ("trial", dict(bench=BENCH), "a"), ("debate", dict(bench=BENCH), "a")):
    cnt = Counter(); N = 2000
    for i in range(N):
        inp, card, out, b = sit(mp, rite, M, ("yc", rite, who, i), effort=3, deciders={who: chooser("concede")}, **kw)
        if out.ended == "yielded" and out.ended_by == who:
            yside = E._who(inp, who).side
            good_for_yielder = (b[0] in CARRIED) == (yside == "for")
            cnt["yielded"] += 1; cnt["yielder prevails"] += good_for_yielder
    y = cnt["yielded"]
    print(f"  {rite:12} '{who}' concedes at every chance: yielded {y}/{N}; of those, the verdict goes TO the yielder {cnt['yielder prevails']} ({cnt['yielder prevails']/max(1,y):.3f})")

# ---------------------------------------------------------------- 3 the card's odds vs the sitting
H("CARD ODDS vs actual (all-mid; odds = card.odds of the first decider)")
for rite, kw, lab in (("negotiation", {}, "consent, no one concedes"), ("conversation", dict(form="abridged"), "abridged tell"),
                      ("trial", dict(bench=BENCH), "bench")):
    car = 0; N = 2000; odds = None
    for i in range(N):
        dec = {"a": chooser("rest"), "b": chooser("rest")} if rite == "negotiation" else None
        inp, card, out, b = sit(mp, rite, M, ("co", rite, i), effort=3, deciders=dec, **kw)
        odds = card.odds[0][1]; car += b[0] in CARRIED
    print(f"  {lab:28} card promises P(carried) {odds:.2f}; sitting delivers {car/N:.3f}")
# strong speaker in the abridged tell: card ignores him
pp = copy.deepcopy(mp); pp["a"]["attributes"].update(reason=7, presence=7, grace=7)
car = 0
for i in range(2000):
    inp, card, out, b = sit(pp, "conversation", M, ("co2", i), form="abridged")
    car += b[0] in CARRIED
print(f"  abridged tell, speaker R/P/G 7: card promises {card.odds[0][1]:.2f}; delivers {car/2000:.3f}")

# ---------------------------------------------------------------- 4 the fold performs the disposal row?
H("FOLD: disposal ops the toy fold performs vs drops")
handled = ("tenure:", "office:stripped", "record:", "precedent", "docket:", "grievance", "faction+", "faction-", "legitimacy-arranger")
for disp, row in host.DISPOSAL.items():
    for band, ops in row.items():
        dropped = [op for op in ops if not any(op.startswith(h) if h.endswith(":") else op == h for h in handled)]
        if dropped:
            print(f"  {disp:7} {band:12} dropped silently: {dropped}")
# a conversation success vs failure: the typed writes the disposal row produces
seen = {}
for i in range(300):
    inp, card, out, b = sit(mp, "conversation", M, ("fd", i), effort=3)
    if b[0] in seen: continue
    w = host.new_world()
    band, writes = host.fold(w, mp, inp, card, out, M)
    seen[b[0]] = (sorted(set(x[0] for x in writes)), w["regard"].get(("b", "a")), w["regard"].get(("a", "b")))
for k, v in seen.items():
    print(f"  conversation {k:12} write kinds {v[0]}; regard b->a {v[1]}, a->b {v[2]}")
# sign of regard writes between parties over many sittings
w = host.new_world(); pos = neg = 0
for i in range(300):
    inp, card, out, b = sit(mp, "conversation", M, ("rg", i), effort=3)
    before = dict(w["regard"])
    host.fold(w, mp, inp, card, out, M)
    for k in (("a", "b"), ("b", "a")):
        d = w["regard"].get(k, 0.0) - before.get(k, 0.0)
        pos += d > 1e-12; neg += d < -1e-12
print(f"  300 conversations between a and b: party-to-party regard writes up {pos}, down {neg}; final a->b {w['regard'].get(('a','b'),0):.2f}, b->a {w['regard'].get(('b','a'),0):.2f}")
print(f"  legitimacy writes anywhere in host.fold that can be positive: {'legitimacy' in open(host.__file__).read() and ' + ' in ''}  (see source: only '- 0.5' and '- card.tilt')")

# ---------------------------------------------------------------- 5 resume
H("RESUME: a sitting resumed from its own end state")
for rite, kw in (("trial", dict(bench=BENCH)), ("conversation", {})):
    over = 0; extra = Counter(); yres = 0; reargued = 0; N = 200
    for i in range(N):
        inp, card, out, b = sit(mp, rite, M, ("rs", i), effort=3, **kw)
        inp2, card2 = host.build(mp, rite, M, effort=3, state=out.state, **kw)
        out2 = E.proceed(inp2, draw(("rs2", i), "act", rite))
        spoke = Counter(x.mover for x in out.beats) + Counter(x.mover for x in out2.beats)
        over += any(v > card.turns for v in spoke.values())
        extra[len(out2.beats)] += 1
        if out.ended == "yielded":
            yres += len(out2.beats) > 0
        conceded = {x.closed for x in out.beats if x.closed}
        reargued += any(x.issue in conceded for x in out2.beats)
    print(f"  {rite:12} card turns {card.turns}: resumed-after-finish sittings that ran more beats {sum(v for k, v in extra.items() if k > 0)}/{N} (beats {dict(extra)}); total speeches exceed the card's turns in {over}/{N}; a yielded sitting resumed and spoke again {yres}; a conceded issue re-argued {reargued}")
# mid-sitting split: run 1 turn, then resume with 2 more expected
inp, card = host.build(mp, "trial", M, bench=BENCH, effort=1)
print(f"  (a 1-turn trial's card says {card.turns} turns; resuming its end state with effort 3 card {host.build(mp, 'trial', M, bench=BENCH, effort=3)[1].turns} runs a fresh full budget, ignoring Cond.spoken)")
