"""P1 controls: P, N (refusals), C (speak vs silent, with a both-silent null), M (mirror/swap), determinism, sweeps."""
import copy, sys
from collections import Counter
from common import *
from sc2.engine import Input, p_carried

N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
mp = F.mid_people()
M = F.matter()
BENCH = ("j1", "j2", "j3")
TR = dict(bench=BENCH, effort=3, floor=("crowd",))


def stats(people, rite, m, n, seed, deciders=None, **kw):
    car = 0; tr = 0.0; pos = 0; ends = Counter(); beats = 0; moved_any = 0
    for i in range(n):
        inp, card, out, b = run(people, rite, m, (seed, i), deciders=deciders, **kw)
        car += b[0] in CARRIED
        j = next(p.id for p in sorted(inp.room, key=lambda p: (-p.precedence, p.id)) if p.decides)
        t = dict(out.state.tracks)[j]; tr += t; pos += t > 0
        ends[out.ended] += 1; beats += len(out.beats)
        moved_any += any(b.moved for b in out.beats)
    return dict(carried=round(car / n, 3), se=round(se(car / n, n), 3), judge_track=round(tr / n, 2), track_pos=round(pos / n, 3),
                beats=round(beats / n, 1), ends=dict(ends), moved=moved_any)


def refused(name, f):
    try:
        f(); print(f"  N {name}: NOT REFUSED")
    except Exception as e:
        print(f"  N {name}: refused -> {type(e).__name__}: {e}")


print("== P positive: trial, all-mid, bench of 3, both automatic")
print("  ", stats(mp, "trial", M, N, "P", **TR))
print("== N one-condition negatives")
refused("one character (both parties one)", lambda: host.build(mp, "trial", F.matter(f="a", ag="a"), **TR))
inp, _ = host.build(mp, "trial", M, **TR)
refused("one character in the room", lambda: Input(inp.rite, "m", (inp.room[0],), inp.grounds, inp.dials))
refused("trial with no seat (nobody decides)", lambda: host.build(mp, "trial", M, effort=3))
refused("drawn close, deciders removed", lambda: Input(inp.rite, "m", tuple(p for p in inp.room if not p.decides), inp.grounds, inp.dials))
refused("nobody speaks", lambda: Input(inp.rite, "m", tuple(p for p in inp.room if not p.side), inp.grounds, inp.dials))
print("  N trial with no opposing party (against=None):")
try:
    print("    ", stats(mp, "trial", dict(id="m", parties={"for": "a"}, bears={}), 100, "Nopp", **TR))
except Exception as e:
    print("    refused ->", e)

print("== C counterfactual: who speaks (same seeds); null = both rest")
arms = {"both auto": None, "against silent (rests)": {"b": forced("rest")}, "for silent (rests)": {"a": forced("rest")},
        "both silent (null)": {"a": forced("rest"), "b": forced("rest")},
        "for argues only": {"a": forced("argue")}, "both argue only": {"a": forced("argue"), "b": forced("argue")}}
for rite, kw in (("trial", TR), ("debate", dict(bench=BENCH, effort=3, floor=("crowd",))), ("conversation", dict(effort=3))):
    print(f"  -- {rite}")
    for k, d in arms.items():
        print(f"    {k:26s}", stats(mp, rite, M, N, "C", deciders=d, **kw))

print("== M mirror/swap (n=%d; band at p=.5 about +-%.3f)" % (N, 2 * (0.25 / N) ** 0.5))
for rite, kw in (("trial", TR), ("debate", dict(bench=BENCH, effort=3, floor=("crowd",))), ("conversation", dict(effort=3))):
    s0 = stats(mp, rite, M, N, "M", **kw)
    strong_for = copy.deepcopy(mp); strong_for["a"]["attributes"]["reason"] = 7
    strong_ag = copy.deepcopy(mp); strong_ag["b"]["attributes"]["reason"] = 7
    s1 = stats(strong_for, rite, M, N, "M", **kw); s2 = stats(strong_ag, rite, M, N, "M", **kw)
    print(f"  {rite}: identical sides: P(judge track>0) {s0['track_pos']} mean {s0['judge_track']} carried {s0['carried']}")
    print(f"     A=Reason7 as for: track>0 {s1['track_pos']} mean {s1['judge_track']} carried {s1['carried']} | as against: track>0 {s2['track_pos']} mean {s2['judge_track']} carried {s2['carried']}")

print("== determinism (same seed twice) and spread")
hs = [h(run(mp, "trial", M, ("det", 7), **TR)[2]) for _ in range(2)]
print("  same seed:", hs, "equal" if hs[0] == hs[1] else "DIFFER")
print("  distinct hashes over 50 seeds:", len({h(run(mp, 'trial', M, ('det', i), **TR)[2]) for i in range(50)}))

print("== sweep turns via effort (trial row 2..5)")
for e in range(0, 7):
    inp, _ = host.build(mp, "trial", M, bench=BENCH, effort=e, floor=("crowd",))
    print(f"  effort {e}: turns {inp.rite.turns}", stats(mp, "trial", M, N // 2, "E", bench=BENCH, effort=e, floor=("crowd",)))
print("== close monotone in presiding track (closed form p_carried)")
inp, _ = host.build(mp, "trial", M, **TR)
print("  ", [(t, round(p_carried(inp, t), 3)) for t in (-10, -5, -3, 0, 3, 5, 10, 20)])
