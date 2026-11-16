"""P7 'with nobody playing it is a simulation by the same rules': a multi-season run of the same few people.
LABELLED PROXY: sc2/ has no season driver (N: P6.7 ASSERTED); this loop is the runner's, built only from host.build,
engine.proceed and host.fold, carrying regard into relationships and rattles into strain, as the fold's own writes allow."""
from common import *
NS = int(sys.argv[1]) if len(sys.argv) > 1 else 200
SEASONS = int(sys.argv[2]) if len(sys.argv) > 2 else 3
cast0, T = F.cast(), F.TOLLS
FL = ("guildsmen", "toll_men", "clerk")
WHO = ("scholar", "bully", "diplomat", "orator", "judge", "clerk")


def run(seed, seasons=SEASONS, played=None):
    people = copy.deepcopy(cast0); world = host.new_world(); world["strife"]["famine"] = 1.0; log = []
    presses = Counter()
    def hold(rite, m, **kw):
        strife = "famine" if world["strife"].get("famine", 0) > 0.6 else "peace"
        inp, card = host.build(people, rite, m, effort=3, strife=strife, **kw)
        out = proceed(inp, draw((seed, len(world["events"])), "act", rite), None, played)
        band, wr = host.fold(world, people, inp, card, out, m)
        for x in out.beats:
            if x.move == "press" and x.target: presses[(x.mover, x.target)] += 1
        for (x, y), v in world["regard"].items():
            if x in people:
                people[x]["layers"].setdefault("relationships", {})[y] = max(-1, min(1, cast0[x]["layers"].get("relationships", {}).get(y, 0.0) + v))
        for pid, rs in world["rattled"].items(): people[pid]["rattled_ago"] = tuple(rs)
        log.append((rite, m["id"], band, out.ended)); return band
    for s in range(seasons):
        for pid in world["rattled"]: world["rattled"][pid] = [x + 1 for x in world["rattled"][pid]]
        hold("trial", dict(T, id=f"tolls_{s}", strife=None), bench=CB, floor=FL)
        for d in list(world["docket"]):
            if d[1] == "appeal": world["docket"].remove(d); hold("audience", dict(T, id=d[0], parties={"for": "scholar", "against": "bully"}, strife=None), bench=("judge",))
        hold("negotiation", dict(id=f"grain_{s}", parties={"for": "diplomat", "against": "bully"}, bears={"grain": 1.0, "tolls": -0.5}, strife="famine"))
        hold("conversation", dict(id=f"remit_{s}", parties={"for": "orator", "against": "bully"}, bears={"trade": 1.0, "tolls": -1.0}))
    return world, people, log, presses


def rel(people, x, y):
    return people[x]["layers"].get("relationships", {}).get(y, 0.0)


print(f"== {SEASONS} seasons x {NS} seeds; each season: the tolls trial (scholar v bully), the grain negotiation (diplomat v bully), a conversation (orator v bully); appeals heard")
car = defaultdict(list); after = {True: [], False: []}; pins = Counter(); pairs = 0; ups = downs = 0; stn = []
meet = []; nomeet = []; pr_vs_reg = []
for sd in range(NS):
    w, pe, log, pr = run(sd)
    tr = [l for l in log if l[0] == "trial"]
    for k, l in enumerate(tr): car[k].append(l[2] in CARRIED)
    after[car[0][-1]].append(car[SEASONS - 1][-1])
    for x in WHO:
        for y in WHO:
            if x != y:
                r = rel(pe, x, y); pairs += 1; pins[("-1" if r <= -1 else "+1" if r >= 1 else "mid")] += 1
                (meet if y == "bully" or x == "bully" else nomeet).append(r - cast0[x]["layers"].get("relationships", {}).get(y, 0.0))
                pr_vs_reg.append((pr[(y, x)], r))
    stn.append(max(host.strain_carried(p, D) for p in pe.values()))
    ups += sum(1 for (x, y), v in w["regard"].items() if v > 0); downs += sum(1 for (x, y), v in w["regard"].items() if v < 0)
m_ = lambda xs: sum(xs) / max(1, len(xs))
print("  the trial carried by season: " + ", ".join(f"s{k+1} {m_(v):.3f}" for k, v in sorted(car.items())))
print(f"  snowball: season {SEASONS} after a season-1 win {m_(after[True]):.3f} (n={len(after[True])}), after a loss {m_(after[False]):.3f} (n={len(after[False])})")
print(f"  regard change from the start: pairs involving the bully (they met) mean {m_(meet):+.3f}; pairs that never sat against each other {m_(nomeet):+.3f}")
for lo, hi in ((0, 1), (1, 2), (2, 4), (4, 99)):
    rs = [r for p, r in pr_vs_reg if lo <= p < hi]
    if rs: print(f"    pressed by him {lo}..{hi-1} times: n={len(rs)} mean regard toward him {m_(rs):+.3f}")
print(f"  pinned at the clip: {dict(pins)} of {pairs} directed pairs; pair-level regard entries up {ups}, down {downs}; greatest strain carried {max(stn):.2f}")

print("\n== recovery from a pin: pairs at -1 after 3 seasons that are above -1 after 6 (same seeds, 6-season runs), first 100 seeds")
rec = tot = 0
for sd in range(min(100, NS)):
    w3, p3, _, _ = run(sd, 3); w6, p6, _, _ = run(sd, 6)
    for x in WHO:
        for y in WHO:
            if x != y and rel(p3, x, y) <= -1:
                tot += 1; rec += rel(p6, x, y) > -1
print(f"  pinned at -1 after 3: {tot}; above -1 after 6: {rec}")

print("\n== determinism: the same seed twice")
hs = set()
for _ in range(2):
    w, pe, log, pr = run(7)
    hs.add(hashlib.sha256(repr((sorted(w["regard"].items()), w["docket"], w["events"], log)).encode()).hexdigest()[:16])
print(f"  distinct world hashes over 2 runs of seed 7: {len(hs)} {hs}")
