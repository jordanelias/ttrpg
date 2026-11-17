"""F8 (adapted, fix3): lane C's seasons.py run on the model SC2 names; adds the most appeals one matter had in one
season, and the sittings skipped by a keyed refusal.
FAMILY 4: SEASON DRIVER (sc2/acts.py).  python -B seasons.py SEASONS SEEDS
Cast: 10 persons, 4 factions (Crown, Church, Guild, Parliament), offices at rungs 2..5 mixed, two cohorts.
Schedule: 9 recurring matters across trial, inquisition, debate, tribunal, audience, negotiation, questioning,
conversation, rally; one rigged trial. Every seed is a distinct `key`.
PREDICTIONS: every bounded quantity stays in [-1,1] (strife [0,1]); nothing pinned at a bound at the end; the
docket stays bounded (each entry convened or lapsing within two seasons); no faction's legitimacy or standing drifts
monotonically to a bound (the fade restores); a judge who rules rightly at Grace >= 4 does not lose legitimacy on
average; the same seed gives the same final hash; every scheduled party gets hearings; a vacated office or a
removed person mid-run is either handled or refused with a keyed reason, never an uncaught crash.
"""
import sys, copy, hashlib, math
from collections import Counter, defaultdict
from common import *
import hashlib
from inv import world_bounds
S = int(sys.argv[1]) if len(sys.argv) > 1 else 16
K = int(sys.argv[2]) if len(sys.argv) > 2 else 6
P, seat, Item = F.P, F.seat, E.Item


def cast():
    pp = {
        "king_j": P("king_j", reason=6, grace=6, office=seat(5, "Crown", "moderate"), faction="Crown", layers=dict(convictions={"law": 4})),
        "reeve": P("reeve", reason=4, grace=2, will=6, office=seat(3, "Crown"), faction="Crown", layers=dict(pursuits={"tolls": 0.8}, relationships={"merchant": -0.5})),
        "bishop": P("bishop", presence=6, will=6, grace=5, office=seat(4, "Church", "moderate"), faction="Church", layers=dict(convictions={"faith": 5})),
        "prior": P("prior", grace=3, office=seat(2, "Church"), faction="Church", layers=dict(convictions={"faith": 4}, patron="bishop")),
        "speaker": P("speaker", reason=5, grace=5, office=seat(4, "Parliament"), faction="Parliament", layers=dict(convictions={"commons": 4})),
        "member": P("member", presence=6, office=seat(2, "Parliament"), faction="Parliament", layers=dict(pursuits={"trade": 0.6})),
        "merchant": P("merchant", reason=6, attunement=6, faction="Guild", items=(Item("ledger", "record", 0.9, about="reeve"),), layers=dict(pursuits={"trade": 0.9}, relationships={"reeve": -0.6})),
        "master": P("master", grace=6, office=seat(3, "Guild"), faction="Guild", layers=dict(pursuits={"trade": 0.7})),
        "heretic": P("heretic", will=7, grace=2, presence=5, layers=dict(convictions={"faith": 0}, pursuits={"commons": 0.6})),
        "commons": P("commons", weight=30, layers=dict(needs={"grain": 0.7}, convictions={"commons": 3})),
        "guilds": P("guilds", weight=20, faction="Guild", layers=dict(pursuits={"trade": 0.8})),
    }
    return pp


def M(mid, f, a, **bears):
    return dict(id=mid, parties={"for": f, "against": a}, bears=bears)


SCHED = [
    ("trial", M("tolls", "merchant", "reeve", tolls=-1.0, trade=1.0, law=0.5), dict(bench=("king_j", "reeve"), floor=("guilds", "commons"), effort=3)),
    ("trial", M("rigged", "reeve", "merchant", tolls=1.0, trade=-1.0), dict(bench=("king_j",), arranger="reeve", rig=1.0, effort=3)),
    ("inquisition", M("heresy", "prior", "heretic", faith=1.0, commons=-0.5), dict(bench=("bishop", "prior"), effort=3)),
    ("debate", dict(M("grain_act", "speaker", "member", grain=1.0, trade=-0.5), strife="famine"), dict(bench=("speaker", "member", "king_j"), floor=("commons",), effort=3)),
    ("tribunal", M("charter", "master", "reeve", trade=1.0, tolls=-0.5), dict(bench=("king_j", "speaker", "reeve"), effort=3)),
    ("audience", M("plea", "heretic", None, commons=1.0), dict(bench=("king_j",), effort=2)),
    ("negotiation", M("guild_deal", "master", "merchant", trade=0.5), dict(effort=2)),
    ("questioning", M("whereabouts", "bishop", "heretic", faith=0.5), dict(effort=2)),
    ("rally", M("muster", "member", None, commons=1.0, grain=0.5), dict(floor=("commons", "guilds"), effort=2)),
]
FAC = ("Crown", "Church", "Guild", "Parliament")


def run(seed, seasons, vacate_at=None, remove_at=None, ab=("speaker", "bishop")):
    people = cast(); world = host.new_world()
    traj = []
    hearings = Counter(); appeals = 0; reversed_ = 0; errs = []
    rulings_right = Counter(); per = Counter()
    for s in range(seasons):
        if vacate_at is not None and s == vacate_at:
            people["king_j"]["office"] = None                        # the high seat falls vacant
        if remove_at is not None and s == remove_at:
            people.pop("reeve", None)                                 # a party/seat dies
        try:
            ran = acts.season(world, people, SCHED, s, appeal_bench=ab, key=("seas", seed))
        except Exception as e:
            errs.append((s, type(e).__name__, str(e)[:100])); break
        for r in ran:
            m = r["inp"].matter
            for p in r["inp"].room:
                if p.side: hearings[p.id] += 1
            appeals += "appeal" in r; reversed_ += bool(r.get("reversed"))
            if "appeal" in r: per[(s, r["matter"])] += 1
        for rec in world["reception"][-len(ran):]:
            rulings_right["wrong" if rec[2] else "right"] += 1
        reg = list(world["regard"].values())
        traj.append(dict(s=s, regmin=min(reg, default=0), regmax=max(reg, default=0),
                         legit={f: round(world["legitimacy"].get(f, 0.0), 3) for f in FAC},
                         stand={f: round(world["standing"].get(f, 0.0), 3) for f in FAC},
                         strife=dict(world["strife"]), docket=len(world["docket"]), viol=+world_bounds(world),
                         nsit=len(ran)))
    h = hashlib.sha256(repr((sorted((k, round(v, 9)) for k, v in world["regard"].items()),
                             sorted(world["legitimacy"].items()), len(world["tenures"]), len(world["events"]))).encode()).hexdigest()[:16]
    world["_per"] = per
    return traj, h, hearings, appeals, reversed_, errs, world, rulings_right


if __name__ == "__main__":
    allv = Counter(); final = defaultdict(list); hs = []
    for seed in range(K):
        traj, h, hear, ap, rv, errs, world, rr = run(seed, S)
        h2 = run(seed, S)[1]
        hs.append((seed, h, h == h2))
        for t in traj:
            allv.update(t["viol"])
        if not traj:
            continue
        last = traj[-1]
        for f in FAC:
            final[("legit", f)].append(last["legit"][f]); final[("stand", f)].append(last["stand"][f])
        print(f"seed {seed}: hash {h} deterministic {h == h2}; errs {errs}; sittings/season {[t['nsit'] for t in traj]}; docket {[t['docket'] for t in traj]}; appeals {ap} reversed {rv}; most appeals of one matter in a season {max(world['_per'].values(), default=0)}; skipped by a refusal {len(world.get('refused', []))}; rulings {dict(rr)}", flush=True)
        print(f"   regard range by season {[(round(t['regmin'],2), round(t['regmax'],2)) for t in traj[::3]]}", flush=True)
        print(f"   legitimacy by season (every 3rd) {[t['legit'] for t in traj[::3]]}", flush=True)
        print(f"   standing at end {last['stand']} strife {last['strife']}", flush=True)
        print(f"   hearings as a party/speaker {dict(hear)}; never heard among the parties scheduled: {[p for p in {x for _, m, _ in SCHED for x in m['parties'].values() if x} if hear[p] == 0]}", flush=True)
        led = Counter(x[0] for v in world["ledgers"].values() for x in v)
        print(f"   ledger kinds at end {dict(led.most_common(12))}; tenures {len(world['tenures'])} precedents {len(world['precedents'])} offices {world['offices']}", flush=True)
    print(f"\nbounds violations over all seasons/seeds: {dict(allv)}")
    print("final legitimacy/standing by faction (mean over seeds): " + ", ".join(f"{k[0]} {k[1]} {sum(v)/len(v):+.3f}" for k, v in final.items()))
    print("\n== vacated office at season 4 / a party-seat removed at season 4")
    for lab, kw in (("vacate king_j", dict(vacate_at=4)), ("remove reeve", dict(remove_at=4))):
        traj, h, hear, ap, rv, errs, world, rr = run(0, 8, **kw)
        print(f"  {lab}: seasons completed {len(traj)}; errors {errs}; skipped {sorted(set((k, m, r) for _, k, m, r in world.get('refused', [])))}")
    print("\n== a single polity appeal bench for every rite (the inquisition's appeal cannot sit)")
    for seed in range(3):
        traj, h, hear, ap, rv, errs, world, rr = run(seed, 4, ab=("speaker",))
        print(f"  seed {seed}: seasons completed {len(traj)}; errors {errs}; skipped {sorted(set((k, m, r) for _, k, m, r in world.get('refused', [])))}")
