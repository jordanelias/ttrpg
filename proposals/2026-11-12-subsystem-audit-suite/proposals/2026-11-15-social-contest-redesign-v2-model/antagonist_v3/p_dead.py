"""Each of the 47 settings flipped (to its control / zero, and doubled) over two batteries: the producer's (checks_v3 digest) and an enriched one."""
import sys, os, copy, hashlib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)) + "/..")
from sc2 import host, fixtures as F
from sc2.lab import sit, chooser
cast, T = F.cast(), F.TOLLS
CB = ("judge", "judge2", "judge3"); FL = ("guildsmen", "toll_men", "clerk")
ROWS = (("conversation", {}), ("negotiation", {}), ("questioning", {}), ("inquisition", dict(bench=("bishop", "prior"))), ("trial", dict(bench=CB, floor=FL)), ("debate", dict(bench=CB, floor=("guildsmen",))), ("rally", dict(floor=("guildsmen", "toll_men", "townsfolk"))), ("audience", dict(bench=("judge",))))
def battery(enriched):
    c2 = copy.deepcopy(cast); c2["bully"]["rattled_ago"] = (0, 1); c2["scholar"]["believes"] = {"tolls": -0.5}
    if enriched:
        c2["scholar"]["attributes"]["reason"] = 3; c2["fox"]["bias"] = 0.8; c2["diplomat"]["bias"] = -0.8; c2["orator"]["attributes"]["focus"] = 1
    return c2
def digest(DD, enriched):
    h = hashlib.sha256(); c2 = battery(enriched)
    rows = ROWS if not enriched else ROWS + (("trial_famine", dict(bench=CB, floor=FL, strife="famine")), ("conv_abr", dict(form="abridged")))
    for rite, kw in rows:
        r = {"trial_famine": "trial", "conv_abr": "conversation"}.get(rite, rite)
        m = dict(T) if r not in ("rally", "audience") else dict(T, parties={"for": "orator" if r == "rally" else "scholar"})
        for i in range(20 if not enriched else 30):
            dec = {} if (not enriched or i % 2 == 0) else {p: chooser("random", i) for p in c2}
            inp, card, out, b = sit(c2, r, m, ("abl", i), effort=4, D=DD, deciders=dec, arranger="bully" if r == "trial" else None, rig=0.5 if r == "trial" else 0.0, **kw)
            h.update(repr((b[0], round(b[1] or 0, 6), len(out.beats), out.ended, tuple((x.move, x.margin) for x in out.beats))).encode())
    return h.hexdigest()
own = [k for k in host.SHIPPED if k not in ("pool_add", "pool_floor", "pool_default", "opposition_rate", "mid", "floor", "ceiling")]
NOZERO = {"crowd_at", "mood_scale", "read_scale", "power_scale"}
for enriched in (False, True):
    base = digest(host.dials(), enriched); dead = []
    for k in own:
        v = host.SHIPPED[k]
        flips = []
        if isinstance(v, str): flips = [None]
        elif k == "relevance": flips = [0]
        else:
            if k not in NOZERO: flips.append(0.0)
            flips.append(v * 2 if v else 1.0)
        if all(digest(host.dials(**{k: f}), enriched) == base for f in flips):
            dead.append(k)
    print(f"{'enriched' if enriched else 'producer'} battery: {len(own)} settings; moving nothing when zeroed AND doubled: {dead}")
