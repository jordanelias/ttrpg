"""P6.7: repeated sittings. sc2/ has NO season driver; this is a LABELLED PROXY driver written for this run:
a fixed schedule per season; the fold's world carried; regard folded back into each person's relationships
(baseline + accumulated, clamped -1..1) and rattles into rattled_ago, so the next sitting can read them.
Arm 'carry' vs null arm 'no carry' (each season starts from the fixed cast)."""
import sys, statistics as stt
from collections import Counter
from common import *

SEEDS = int(sys.argv[1]) if len(sys.argv) > 1 else 40
SEASONS = int(sys.argv[2]) if len(sys.argv) > 2 else 12
cast0 = F.cast(); T = F.TOLLS
CB = ("judge", "judge2", "judge3"); FL = ("guildsmen", "toll_men", "clerk")


def run(seed, carry=True):
    people = copy.deepcopy(cast0); world = host.new_world(); world["strife"]["famine"] = 1.0; per = []

    def hold(rite, m, **kw):
        strife = "famine" if world["strife"].get("famine", 0) > 0.6 else "peace"
        inp, card = host.build(people, rite, m, effort=3, strife=strife, **kw)
        out = proceed(inp, draw((seed, len(world["events"])), "act", rite))
        band, wr = host.fold(world, people, inp, card, out, m)
        if carry:
            for (x, y), v in world["regard"].items():
                if x in people:
                    base = cast0[x]["layers"].get("relationships", {}).get(y, 0.0)
                    people[x]["layers"].setdefault("relationships", {})[y] = max(-1, min(1, base + v))
            for pid, rs in world["rattled"].items():
                people[pid]["rattled_ago"] = tuple(rs)
        return band, wr
    for s in range(SEASONS):
        if not carry:
            people = copy.deepcopy(cast0)
        for pid in world["rattled"]:
            world["rattled"][pid] = [x + 1 for x in world["rattled"][pid]]
        ups = downs = 0; bands = {}
        sched = [("trial", dict(T, id=f"tolls_{s}", strife=None), dict(bench=CB, floor=FL, arranger="bully", rig=1.0 if s == 0 else 0.0)),
                 ("negotiation", dict(id=f"grain_{s}", parties={"for": "diplomat", "against": "bully"}, bears={"grain": 1.0, "tolls": -0.5}, strife="famine"), {}),
                 ("conversation", dict(T, id=f"talk_{s}", parties={"for": "orator", "against": "diplomat"}), {}),
                 ("rally", dict(T, id=f"rally_{s}", parties={"for": "orator", "against": None}), dict(floor=("guildsmen", "townsfolk", "toll_men")))]
        if world["strife"].get("famine", 0) > 0.6:
            sched.insert(0, ("debate", dict(T, id=f"remit_{s}", parties={"for": "orator", "against": "bully"}), dict(bench=CB, floor=("guildsmen", "townsfolk"))))
        for rite, m, kw in sched:
            band, wr = hold(rite, m, **kw)
            bands[rite] = band
            ups += sum(1 for x in wr if x[0] == "regard+"); downs += sum(1 for x in wr if x[0] == "regard-")
        R = world["regard"]
        rel = {(x, y): people[x]["layers"].get("relationships", {}).get(y, 0.0) for x in people for y in people if x != y}
        dead = sum(1 for (x, y), v in rel.items() if x < y and v <= -0.95 and rel[(y, x)] <= -0.95)
        per.append(dict(ups=ups, downs=downs, Rsum=sum(R.values()), Rmin=min(R.values()), Rmax=max(R.values()),
                        npairs=len(R), dead=dead, griev=sum(1 for d in world["docket"] if d[1] == "grievance"),
                        docket=len(world["docket"]), famine=world["strife"].get("famine", 0.0),
                        legit=dict(world["legitimacy"]), trial=bands["trial"] in CARRIED,
                        sb=R.get(("scholar", "bully"), 0.0), bs=R.get(("bully", "scholar"), 0.0),
                        dip_bully=R.get(("diplomat", "bully"), 0.0), sd=R.get(("scholar", "diplomat"), 0.0),
                        g_od=R.get(("guildsmen", "orator"), 0.0)))
    return world, per


m = lambda xs: sum(xs) / len(xs)
for carry in (True, False):
    res = [run(sd, carry)[1] for sd in range(500, 500 + SEEDS)]
    print(f"\n== PROXY season driver, carry={carry}; {SEEDS} seeds x {SEASONS} seasons (season 1 trial rigged by the bully)")
    print(" season | regard+ writes | regard- writes | world regard sum | min | max | dead pairs (both <= -0.95) | grievances on docket | docket | famine (min..max) | trial carried | regard scholar->bully | bully->scholar | guildsmen->orator | scholar->diplomat")
    for s in range(SEASONS):
        if s > 3 and s not in (5, 8, SEASONS - 1): continue
        col = lambda k: [r[s][k] for r in res]
        fam = col("famine")
        print(f"  {s+1:3} | {m(col('ups')):5.1f} | {m(col('downs')):5.1f} | {m(col('Rsum')):+7.2f} | {m(col('Rmin')):+.2f} | {m(col('Rmax')):+.2f} | {m(col('dead')):.2f} | {m(col('griev')):5.1f} | {m(col('docket')):5.1f} | {m(fam):+.2f} ({min(fam):+.2f}..{max(fam):+.2f}) | {m(col('trial')):.2f} | {m(col('sb')):+.2f} | {m(col('bs')):+.2f} | {m(col('g_od')):+.2f} | {m(col('sd')):+.2f}")
    leg = Counter()
    for r in res:
        for k, v in r[-1]["legit"].items(): leg[k] += v / SEEDS
    print(f"   legitimacy after {SEASONS} seasons (mean): {dict((k, round(v, 2)) for k, v in leg.items())}")

w1, _ = run(777, True); w2, _ = run(777, True)
print(f"\n== determinism: same seed twice -> world hash {world_hash(w1)} == {world_hash(w2)}: {world_hash(w1) == world_hash(w2)}; different seed {world_hash(run(778, True)[0])}")
