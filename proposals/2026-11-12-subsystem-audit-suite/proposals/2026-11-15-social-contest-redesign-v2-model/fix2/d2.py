"""D2, B9: the season driver on the cast: regard, grudges, legitimacy, strife, the docket, over 3 and 12 seasons."""
from common import *
from sc2 import acts
N = int(sys.argv[1]) if len(sys.argv) > 1 else 100
S = int(sys.argv[2]) if len(sys.argv) > 2 else 3
cast = F.cast()
T = F.TOLLS
SCHED = [("trial", dict(T, parties={"for": "scholar", "against": "bully"}), dict(bench=CB, floor=FL, effort=3, arranger="bully", rig=1.0)),
         ("negotiation", dict(id="grain", parties={"for": "orator", "against": "diplomat"}, bears={"grain": 1.0, "trade": 0.5}), dict(effort=3)),
         ("questioning", dict(T, id="who", parties={"for": "fox", "against": "bully"}), dict(effort=3)),
         ("rally", dict(T, id="rally", parties={"for": "orator"}), dict(floor=("guildsmen", "toll_men", "townsfolk"), effort=3))]
H(f"D2 {N} runs x {S} seasons: the recurring trial (bully rigs), a negotiation, a questioning, a rally, and the docket")
traj = defaultdict(list); acts_c = Counter(); kinds = Counter(); rev = Counter(); snow = defaultdict(list)
lo = hi = 0.0; dead = recovered = 0; legit = []; famine = []; griev_left = []
for run in range(N):
    w = host.new_world(); first = None; pinned = set()
    for s in range(S):
        ran = acts.season(w, cast, SCHED, s, appeal_bench=("judge3", "judge"), key=("d2", run))
        for r in ran:
            acts_c[r["act"]] += 1
            k = "appeal" if "appeal" in r else r["rite"]
            kinds[k] += 1
            if "appeal" in r: rev[r["reversed"]] += 1
            if r["matter"] == "tolls" and "appeal" not in r and r["rite"] == "trial":
                won = r["band"] in CARRIED
                if s == 0: first = won
                if s == S - 1 and first is not None: snow[first].append(won)
        for (x, y), v in w["regard"].items():
            lo, hi = min(lo, v), max(hi, v)
            if v <= -0.9: pinned.add((x, y))
        for p in list(pinned):
            if w["regard"].get(p, 0.0) > -0.5: recovered += 1; pinned.discard(p)
        traj[s].append(w["regard"].get(("scholar", "bully"), 0.0))
    dead += len(pinned)
    legit.append(dict(w["legitimacy"])); famine.append(w["strife"].get("famine", 0.0))
    griev_left.append(sum(1 for d in w["docket"] if d["kind"] == "grievance"))
print(f"  sittings by kind {dict(kinds)}; the losers' acts {dict(acts_c)}; appeals reversed {rev[True]} of {rev[True] + rev[False]}")
print(f"  regard: least {lo:+.2f}, greatest {hi:+.2f} (bounded in -1..1); pairs pinned at <= -0.9 at the end {dead / N:.2f} a run; pairs that came back above -0.5 {recovered}")
print("  the scholar's regard for the bully by season: " + ", ".join(f"s{s} {sum(v)/len(v):+.2f} ({min(v):+.2f}..{max(v):+.2f})" for s, v in traj.items()))
fac = sorted({f for l in legit for f in l})
print("  legitimacy at the end: " + "; ".join(f"{f} {min(l.get(f, 0) for l in legit):+.2f}..{max(l.get(f, 0) for l in legit):+.2f}" for f in fac))
print(f"  famine at the end: {min(famine):.2f}..{max(famine):.2f} (mean {sum(famine)/N:.2f}); grievances still docketed at the end {sum(griev_left)/N:.2f} a run")
if snow[True] and snow[False]:
    print(f"  no snowball: the recurring trial in the last season carried {sum(snow[True])/len(snow[True]):.2f} after a first-season win (n={len(snow[True])}), {sum(snow[False])/len(snow[False]):.2f} after a loss (n={len(snow[False])})")
w = host.new_world(); ups = downs = 0
for s in range(S):
    for r in acts.season(w, cast, SCHED, s, appeal_bench=("judge3", "judge"), key=("d2w", 0)):
        pass
