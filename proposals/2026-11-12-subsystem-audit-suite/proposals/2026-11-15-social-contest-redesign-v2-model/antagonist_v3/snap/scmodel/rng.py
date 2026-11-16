"""The keyed draw (stand-in for B06.03's `engine/dice_engine/draw.py::Draw`, which the tree does not have).

PLAN B24p.08: "`rng.normal(0.0, 1.0)` for the `xi`"; RD A.2: the rng is "the act's own keyed `Draw` ...
`draw_factory(world_seed, tick)(actor, "roll:<prize>:<act id>")`". Not in the tree: derived here as
random.Random(sha256((seed, actor, label))) producing standard normals, with a counter so the fixed draw counts
(G+5 per exchange, three per balloted decider) can be ASSERTED. `gauss(mu, sd)` is provided because the LIVE
`sigma_leverage.roll_net_continuous` -> `dice_engine.continuous_engine_sample` calls `rng.gauss(mean, std)`;
each gauss is one normal and is counted.
"""
from __future__ import annotations

import hashlib
import random


class Draw:
    def __init__(self, seed, actor="actor", label="roll"):
        h = hashlib.sha256(repr((seed, actor, label)).encode()).digest()
        self._r = random.Random(int.from_bytes(h[:8], "big"))
        self.count = 0
        self.key = (seed, actor, label)

    def normal(self, mu: float = 0.0, sd: float = 1.0) -> float:
        self.count += 1
        return mu + sd * self._r.gauss(0.0, 1.0)

    # the live sampler's interface (dice_engine.continuous_engine_sample -> rng.gauss(mean, std))
    def gauss(self, mu: float, sd: float) -> float:
        return self.normal(mu, sd)

    # B05.02 deletes the fraction rule's uniform; nothing in the proceeding calls it. Refused so a stray use shows.
    def random(self):  # pragma: no cover
        raise AssertionError("the proceeding draws normals only (G02); a uniform was requested")

    def randint(self, a, b):  # the LIVE discrete roll_net calls this: counted separately so the control shows it
        self.count += 1
        return self._r.randint(a, b)


def draw(seed, actor="actor", label="roll") -> Draw:
    return Draw(seed, actor, label)
