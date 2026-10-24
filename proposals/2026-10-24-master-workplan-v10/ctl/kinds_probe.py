import collections, json
from engine.season.harness import storybar as SB
w,d,b = SB.drive(0, 4, "off")
k = collections.Counter(e.kind for e in w.log)
persons0 = None
print(json.dumps(k.most_common()))
print("persons", len(w.persons) if hasattr(w,'persons') else '?')
print("tick", w.tick)
