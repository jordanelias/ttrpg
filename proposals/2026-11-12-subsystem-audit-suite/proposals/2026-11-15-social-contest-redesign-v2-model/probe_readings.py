"""Readings used in the receipt (not assertions): bands/ends per type at shipped and at controls."""
import sys
import scmodel  # noqa
from scmodel import data, dials
from scmodel.demo import run_many, default_people
n = int(sys.argv[1]) if len(sys.argv) > 1 else 400
for name, D in (("shipped", dials.shipped()), ("controls", dials.controls())):
    print("==", name)
    for row in data.ROW_IDS:
        r = run_many(n, row, D=D, people_fn=lambda i: default_people(i), effort=2)
        print(f"{row:30} bands={dict(sorted(r['band'].items(), key=str))} ends={dict(r['ended'])} "
              f"x={r['exchanges']:.2f} marks={r['marks']:.2f}")
    for row in ("conversation",):
        r = run_many(n, row, "abridged", D=D, people_fn=lambda i: default_people(i))
        print(f"{row+' abridged':30} bands={dict(r['band'])}")
