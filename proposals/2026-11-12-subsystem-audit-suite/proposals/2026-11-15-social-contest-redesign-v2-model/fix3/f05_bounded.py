"""F5 `bounded` leaves [-1, 1] for a step over 1 (stress lane A2, C8; lane C K5's first regard overshoot).
PREDICTION after: every result in [-1, 1]; a step inside (-1, 1) unchanged from before.  python -B f05_bounded.py"""
from common import *
H("F5 bounded")
print("  bounded(0, -1.2) =", host.bounded(0.0, -1.2), "; bounded(0.5, 2.0) =", host.bounded(0.5, 2.0), "; bounded(-1, -0.5) =", host.bounded(-1.0, -0.5))
import random
r = random.Random(5); out = same = 0
for _ in range(20000):
    x, d = r.uniform(-1, 1), r.uniform(-3, 3); y = host.bounded(x, d)
    out += not (-1 <= y <= 1)
for _ in range(20000):
    x, d = r.uniform(-1, 1), r.uniform(-0.999, 0.999)
    same += abs(host.bounded(x, d) - (x + d * (1 - x) if d > 0 else x + d * (1 + x))) < 1e-12
print(f"  20,000 random steps in (-3, 3): results outside [-1, 1] {out}; 20,000 steps inside (-1, 1) equal to the old rule {same}")
