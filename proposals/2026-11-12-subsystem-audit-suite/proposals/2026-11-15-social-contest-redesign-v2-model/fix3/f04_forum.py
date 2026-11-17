"""F4 who pays legitimacy (stress lane C repro_acquit, lane A det P7, lane B probe_fold's free rig, check_faction).
PREDICTION after: the forum is its seat's faction; an office-holder with no faction of his own pays for a rig as his
seat; a decree's `faction+` reaches a seated mover; a right acquittal under `ban` costs the court nothing and the
accuser's faction pays the failed charge.  python -B f04_forum.py N"""
from common import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 400
mp, M = F.mid_people(), F.matter()
H("F4a a fair Grace-7 bench that acquits: mean legitimacy after one sitting, by (band, ruled right) and faction")
pp = copy.deepcopy(mp)
for j in BENCH + ("c1", "c2", "c3"):
    pp[j]["attributes"]["grace"] = 7
pp["a"]["faction"] = "Church"; pp["b"]["faction"] = "Guild"
for rite, bench in (("tribunal", BENCH), ("trial", BENCH), ("excommunication_deliberation", ("c1", "c2", "c3"))):
    agg = defaultdict(list)
    for i in range(N):
        inp, card, out, b = sit(pp, rite, M, ("aq", i), bench=bench, effort=3)
        w = host.new_world(); band, wr = host.fold(w, pp, inp, card, out, M)
        right = not w["reception"][-1][2] if w["reception"] else None
        if band == "failure" and right:
            for f in ("Crown", "Church", "Guild"):
                agg[f].append(w["legitimacy"].get(f, 0.0))
    print(f"  {rite:29} ({card.stake}) a right acquittal (n={len(agg['Crown'])}): " + ", ".join(f"{f} {sum(v)/max(1,len(v)):+.3f}" for f, v in agg.items()))
H("F4b a Church man in a Crown seat rules a trial (detain; success writes legitimacy+): whose legitimacy moves")
for pf in ("Crown", "Church", None):
    q = copy.deepcopy(mp); q["j1"]["faction"] = pf
    c = Counter()
    for i in range(80):
        inp, card, out, b = sit(q, "trial", M, ("p7", i), bench=("j1",), effort=3)
        w = host.new_world(); host.fold(w, q, inp, card, out, M); c.update(f for f, v in w["legitimacy"].items() if v)
    print(f"  judge's own faction {pf}: factions written {dict(c)}")
H("F4c an arranger with a seat and no faction of his own (rig 1, trial): is the rig paid?")
q = castB(pa="r5M", pb="r2", fac_person=False, seat_fac="Parliament")
paid = rig = 0
for i in range(N // 2):
    inp, card, out, b = sit(q, "trial", mat(), ("fr", i), bench=BENCH, arranger="a", rig=1.0, effort=2)
    w = host.new_world(); band, wr = host.fold(w, q, inp, card, out, mat())
    if card.tilt > 0 and band is not None:
        rig += 1; paid += w["legitimacy"].get("Parliament", 0.0) < -0.2
print(f"  rigged sittings with a band {rig}; Parliament charged the price in {paid}")
H("F4d a decree carried by a seated mover with no faction of his own: standing raised?")
q = castB(pa="r3", fac_person=False, seat_fac="Parliament")
up = car = 0
for i in range(N // 2):
    inp, card, out, b = sit(q, "debate", mat(), ("cf", i), bench=BENCH, effort=3)
    w = host.new_world(); band, wr = host.fold(w, q, inp, card, out, mat())
    if band in CARRIED:
        car += 1; up += w["standing"].get("Parliament", 0.0) > 0
print(f"  carried {car}; Parliament standing raised {up}")
