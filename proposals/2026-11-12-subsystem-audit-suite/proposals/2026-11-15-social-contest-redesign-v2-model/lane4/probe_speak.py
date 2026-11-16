"""Lane 4 probe: for each contested act the five proceeds verbs deal, record who would be addressed
under the plan's builder rules; speak: is the actor the first (id-order) seat of judging_set at his place?"""
import sys, collections
from engine.season.harness.populated import build_realm, run
from engine.season.seam.wrappers import sigma
from engine.season.queries import world_q
from engine.season.state.gate import seat_faction
calls = []
real = sigma.resolve.__wrapped__ if hasattr(sigma.resolve, "__wrapped__") else None
import engine.season.manifest.providers as P
orig = None
def rec(w, claimants, causes, prize, **kw):
    v = kw.get("verb"); s = kw.get("subject"); r = kw.get("rung")
    if v in ("speak", "tell", "lie", "argue", "interrogate", "determine"):
        js = sorted(world_q.judging_set(w, r, s)) if r else []
        items = world_q.docketed(w, s)
        calls.append((v, claimants[0], s, r, js, [i.get("arrangement") for i in items],
                      [seat_faction(w, o) for o in js]))
    return orig(w, claimants, causes, prize, **kw)
# patch the registry entry for the contest provider
from engine.season.manifest import providers as prov
for k, f in list(prov.__dict__.items()):
    pass
seed = int(sys.argv[1]) if len(sys.argv) > 1 else 0
import engine.season.manifest.registry as reg
# find the provider table
tbl = None
for name in dir(prov):
    obj = getattr(prov, name)
    if isinstance(obj, dict) and any(isinstance(k, tuple) and k and k[0] == "contest" for k in obj):
        tbl = obj; break
key = [k for k in tbl if k == ("contest", "social_contest")][0]
orig = tbl[key]
import functools
rec = functools.wraps(orig)(rec)
tbl[key] = rec
w = build_realm(seed)
run(2, seed, w=w)
c = collections.Counter(x[0] for x in calls)
print("calls by verb", dict(c))
sp = [x for x in calls if x[0] == "speak"]
self_addr = sum(1 for x in sp if x[4] and x[4][0] == x[1])
in_bench = sum(1 for x in sp if x[1] in x[4])
empty = sum(1 for x in sp if not x[4])
print(f"speak: n={len(sp)} actor-is-first-seat={self_addr} actor-in-bench={in_bench} empty-bench={empty}")
print("speak docket arrangements", collections.Counter(tuple(x[5]) for x in sp))
print("speak bench factions sample", [x[6] for x in sp[:5]])
it = [x for x in calls if x[0] == "interrogate"]
print("interrogate subjects docketed:", collections.Counter(bool(x[5]) for x in it))
allf = [f for x in sp for f in x[6]]
print("speak bench members:", len(allf), "seat_faction None:", sum(f is None for f in allf))
from engine.season.queries.world_q import judging_set
offs = [o for o in w.offices]
print("seat_faction on office ids (sample):", sorted({seat_faction(w, o) for o in offs})[:4])
