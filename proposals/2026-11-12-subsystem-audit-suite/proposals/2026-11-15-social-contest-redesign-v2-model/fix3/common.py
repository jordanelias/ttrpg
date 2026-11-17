"""fix3 helpers: the stress-test fix pass's probes (2026-11-17). `SC2=before` runs a probe on the model as the
stress test found it (`fix3/before/sc2`, the control: the same probe, the cause still present); anything else runs
it on the fixed model (`../sc2`). Adapted from the stress test's lanes A, B, C, which ran on a scratch copy."""
import sys, os, copy, math
HERE = os.path.dirname(os.path.abspath(__file__))
MODEL = os.path.dirname(HERE)
sys.path.insert(0, MODEL)
if os.environ.get("SC2") == "before":
    sys.path.insert(0, os.path.join(HERE, "before"))
from collections import Counter, defaultdict          # noqa: E402
from sc2 import host, fixtures as F, engine as E, acts  # noqa: E402
from sc2.engine import proceed, Choice                 # noqa: E402
from sc2.lab import sit, se, CARRIED, BENCH            # noqa: E402
from scmodel.rng import draw                           # noqa: E402

ARM = "before" if os.environ.get("SC2") == "before" else "after"
LEVELS = {"none": None, "r2": (2, None), "r3": (3, None), "r4m": (4, "moderate"), "r5M": (5, "major")}


def office(lv, fac="Crown"):
    v = LEVELS[lv]
    return None if v is None else F.seat(v[0], fac, v[1])


def castB(pa="none", pb="none", pt="none", fac_person=True, seat_fac="Crown"):
    """lane B's cast: a (for), b (against), t (a third), j1..j3 Crown r3, c1..c3 Church r2, a crowd of 30, o1 a Guild officer."""
    pp = {}
    for pid, lv in (("a", pa), ("b", pb), ("t", pt)):
        o = office(lv, seat_fac)
        pp[pid] = F.P(pid, office=o, faction=(seat_fac if (o and fac_person) else None))
    for j in ("j1", "j2", "j3"):
        pp[j] = F.P(j, office=F.seat(3, "Crown"), faction="Crown")
    for c in ("c1", "c2", "c3"):
        pp[c] = F.P(c, office=F.seat(2, "Church"), faction="Church")
    pp["crowd"] = F.P("crowd", weight=30)
    pp["o1"] = F.P("o1", office=F.seat(2, "Guild"), faction="Guild")
    return pp


def mat(mid="m", **kw):
    d = dict(id=mid, parties={"for": "a", "against": "b"}, bears={})
    d.update(kw)
    return d


def only(mv):
    def f(v, me):
        os_ = [o for o in v.options if o.move == mv] or list(v.options)
        o = max(os_, key=lambda o: o.ev)
        return Choice(o.move, o.ground, o.item, o.relation)
    return f


def attempt(fn):
    """'ok: <result>' | 'refused[...]' | 'CRASH <type>' -- a keyed refusal is a ValueError whose text opens `refused[`."""
    try:
        return f"ok: {fn()}"
    except ValueError as e:
        s = str(e)
        return s[:s.index("]") + 1] if s.startswith("refused[") else f"ValueError (unkeyed): {s[:60]}"
    except Exception as e:                                # noqa: BLE001 -- the probe counts crashes
        return f"CRASH {type(e).__name__}: {str(e)[:50]}"


def pc(k, n):
    p = k / n
    return f"{p:.3f} +-{2 * se(p, n):.3f}"


def H(t):
    print(f"\n== [{ARM}] {t}", flush=True)
