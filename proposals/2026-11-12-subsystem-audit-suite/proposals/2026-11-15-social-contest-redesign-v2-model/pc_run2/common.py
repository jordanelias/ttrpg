"""premise-check runner 2: shared helpers (probe code, not part of the model)."""
import sys, os, copy, math, hashlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.dirname(HERE))
from sc2 import host, fixtures as F, engine as E          # noqa: E402
from sc2.engine import proceed                            # noqa: E402
from scmodel.rng import draw                              # noqa: E402

CARRIED = ("success", "overwhelming")


def se(p, n):
    return math.sqrt(max(p * (1 - p), 1e-12) / n)


def sit(people, rite, matter, key, decide=None, deciders=None, **kw):
    inp, card = host.build(people, rite, matter, **kw)
    out = proceed(inp, draw(key, "act", rite), decide, deciders)
    return inp, card, out, host.act_band(inp, out)


def whash(obj):
    return hashlib.sha256(repr(obj).encode()).hexdigest()[:16]


def world_hash(w):
    return whash(sorted((k, repr(v)) for k, v in w.items()))


def people_mid(**office):
    pp = F.mid_people()
    for pid, o in office.items():
        pp[pid]["office"] = o
    return pp
