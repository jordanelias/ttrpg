"""Acquaintance and ledger saturation by season: persons who know no one, ledger fill, told share.
usage: PYTHONPATH=<repo> python acquaintance_probe.py SEED SEASONS OUT.json"""
import sys, json, statistics, collections
from engine.season.harness import storybar as SB
from engine.season.state.ids import H  # noqa: F401 (import check only)
from engine.season.queries.person_q import known_persons
from engine.season.harness.populated import build_realm
seed, seasons, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
rows = []
def snap(label, w):
    ks = [len(known_persons(p.ledger, p.id)) for p in w.persons.values()]
    led = [len(p.ledger) for p in w.persons.values()]
    told = sum(1 for p in w.persons.values() for c in p.ledger if getattr(c, "chain", None))
    rows.append({"at": label, "persons": len(ks), "know_nobody": sum(1 for k in ks if k == 0),
                 "known_median": statistics.median(ks), "known_max": max(ks),
                 "ledger_min": min(led), "ledger_median": statistics.median(led), "ledger_max": max(led),
                 "ledger_at_cap": sum(1 for x in led if x >= 200), "claims_with_chain": told})
w0 = build_realm(seed, None); snap("build", w0)
w, d, b = SB.drive(seed, seasons, "off", None, on_season=lambda w, s, n: snap(f"season_end_{len(rows)}", w))
json.dump(rows, open(out, "w"), indent=1)
for r in rows: print(r)
