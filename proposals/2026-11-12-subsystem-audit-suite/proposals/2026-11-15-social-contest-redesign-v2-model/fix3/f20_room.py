"""F20 the room that stops registering: which change is smaller? (a) the record names the room in five bands and only
when a beat turns it (the renderer; the engine untouched); (b) the engine's clamp of the mood replaced by a smooth
saturation (tanh). The outcome bands over 200 seeds a rite under each, against the model as it is.
python -B f20_room.py"""
import hashlib, math
from common import *
cast, T = F.cast(), F.TOLLS
FL = ("guildsmen", "toll_men", "clerk")
SPEC = {"trial": dict(bench=("judge", "judge2", "judge3"), floor=FL), "negotiation": {}, "rally": dict(floor=("guildsmen", "toll_men", "townsfolk")),
        "debate": dict(bench=("judge", "judge2", "judge3"), floor=("guildsmen",)), "questioning": {}, "inquisition": dict(bench=("bishop", "prior")), "audience": dict(bench=("judge",))}
def bands():
    out = {}
    for rite, kw in SPEC.items():
        m = dict(T, parties={"for": "orator" if rite == "rally" else "scholar"}) if rite in ("rally", "audience") else dict(T, parties={"for": "scholar", "against": "bully"})
        out[rite] = tuple(sit(cast, rite, m, ("rm", rite, i), effort=3, **kw)[3][0] for i in range(200))
    return out
base = bands()
H("F20 outcome bands, 200 seeds a rite")
print("  (a) the record's bands: the engine is untouched, so every band equals the model's by construction:",
      {r: hashlib.sha256(repr(v).encode()).hexdigest()[:10] for r, v in base.items()})
clamp = E.mood
def smooth(inp, st, viewer=None):
    T_ = E._d(st.tracks)
    hs = [p for p in inp.room if p.side is None] or [p for p in inp.room if p.decides]
    if not hs:
        o = E._lead(inp, E._other(viewer.side)) if viewer else None
        hs = [o] if o else [p for p in inp.room if p.side]
    W = sum(p.weight * (1.0 + p.power) for p in hs)
    return math.tanh(sum(p.weight * (1.0 + p.power) * T_.get(p.id, 0.0) for p in hs) / W / inp.dials["mood_scale"])
E.mood = smooth; host.mood = smooth
alt = bands()
E.mood = clamp; host.mood = clamp
print("  (b) a smooth saturation in the engine: seeds whose band changes, by rite:", {r: sum(x != y for x, y in zip(base[r], alt[r])) for r in base})
