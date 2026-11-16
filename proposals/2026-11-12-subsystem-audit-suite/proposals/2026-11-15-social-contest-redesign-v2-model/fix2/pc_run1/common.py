"""premise-check runner 1: shared helpers (own probes; does not import checks_v7*)."""
import copy, hashlib, math, os, sys
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))  # fix2 copy: two levels up
from sc2 import host, fixtures as F
from sc2.engine import proceed, Choice, SIGN
from scmodel.rng import draw

CARRIED = ("success", "overwhelming")
CB = ("judge", "judge2", "judge3")
FL = ("guildsmen", "toll_men", "clerk")


def se(p, n):
    return math.sqrt(max(p * (1 - p), 1e-12) / n)


def run(people, rite, matter, key, deciders=None, decide=None, **kw):
    inp, card = host.build(people, rite, matter, **kw)
    rng = draw(key, "act", rite)
    out = proceed(inp, rng, decide, deciders)
    return inp, card, out, host.act_band(inp, out)


def h(out):
    return hashlib.sha256(repr((out.beats, out.verdicts, out.state)).encode()).hexdigest()[:16]


def forced(kind):
    """choose the best-believed option of a move kind (rest: rest); falls back to rest if absent."""
    def f(view, me):
        pick = [o for o in view.options if o.move == kind] or [o for o in view.options if o.move == "rest"] or list(view.options)
        o = max(pick, key=lambda o: o.ev)
        return Choice(o.move, o.ground, o.item, o.relation)
    return f


def ground(g, rel=None):
    def f(view, me):
        pick = [o for o in view.options if o.move == "argue" and o.ground == g and (rel is None or o.relation == rel)]
        pick = pick or [o for o in view.options if o.move == "argue"] or list(view.options)
        o = max(pick, key=lambda o: o.ev)
        return Choice(o.move, o.ground, o.item, o.relation)
    return f


# the five sittings the task names, on the producer's characterful cast (a fixture, not canon)
def scenes():
    T = F.TOLLS
    return {
        "trial": (dict(T, parties={"for": "scholar", "against": "diplomat"}), dict(bench=CB, floor=FL, effort=3)),
        "negotiation": (dict(id="grain", parties={"for": "orator", "against": "diplomat"}, bears={"grain": 1.0, "trade": 0.5}), dict(effort=3)),
        "rally": (dict(T, parties={"for": "orator"}), dict(floor=("guildsmen", "toll_men", "townsfolk"), effort=3)),
        "questioning": (dict(T, id="who_took_the_tolls", parties={"for": "fox", "against": "bully"}), dict(effort=3)),
        "debate": (dict(T, id="remit", parties={"for": "orator", "against": "diplomat"}), dict(bench=CB, floor=("guildsmen",), effort=3)),
    }
