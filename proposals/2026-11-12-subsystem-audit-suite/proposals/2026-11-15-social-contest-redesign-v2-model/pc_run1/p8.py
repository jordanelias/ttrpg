"""P8: the abridged tell / lie / speak. Own probes."""
import copy, random, sys
from collections import Counter
from common import *
from sc2.engine import Item
from scmodel.dice import roll_net_continuous, even_line, opposed_ob, p_at_least, MU_PER_DIE

N = int(sys.argv[1]) if len(sys.argv) > 1 else 600
G = 4


def tell_world(a_attrs=None, b_attrs=None, a_layers=None, b_layers=None, items=(), bears=None, believes=None, floor=False):
    pp = {"a": F.P("a", items=items, layers=a_layers or {}, **(a_attrs or {})),
          "b": F.P("b", layers=b_layers or {}, **(b_attrs or {})), "crowd": F.P("crowd", weight=30)}
    if believes is not None:
        pp["a"]["believes"] = {"m": believes}
    return pp, dict(id="m", parties={"for": "a", "against": "b"}, bears=bears or {})


def sit_ab(pp, m, key, D=None, dec=None, rite="conversation", **kw):
    inp, card = host.build(pp, rite, m, form="abridged", D=D, **kw)
    out = proceed(inp, draw(key, "act", rite), None, {"a": dec} if dec else None)
    return inp, card, out, host.act_band(inp, out)


# ---------------------------------------------------------------- 1. equality with the plain single roll under controls
C = host.controls()
ok = bad = 0
rr = random.Random(5)
for i in range(200):
    aa = {k: rr.randint(1, 7) for k in ("focus", "reason", "attunement", "presence", "grace", "will")}
    bb = {k: rr.randint(1, 7) for k in ("focus", "reason", "attunement", "presence", "grace", "will")}
    pp, m = tell_world(aa, bb, a_layers=dict(pursuits={"t": 0.9}), b_layers=dict(pursuits={"t": 0.6}), bears={"t": rr.choice((-1, 1))})
    inp, card, out, band = sit_ab(pp, m, ("eq", i), D=C)
    a = next(p for p in inp.room if p.id == "a"); b = next(p for p in inp.room if p.id == "b")
    from sc2.engine import case_pool
    pool = case_pool(inp, a, out.beats[0].ground)
    rng = draw(("eq", i), "act", "conversation")
    for _ in range(4 * G + 10):
        rng.normal()
    plain = roll_net_continuous(pool, rng=rng) - (even_line(C["pool_add"]) + opposed_ob(b.will + b.rank, C["opposition_rate"])
                                                   + inp.rite.difficulty + inp.rite.stakes)
    got = out.verdicts[0][1].net - out.verdicts[0][1].ob
    ok += abs(plain - got) < 1e-9; bad += abs(plain - got) >= 1e-9
print(f"[P8.5] under controls(), random attributes both sides, stakes on: margin == plain one roll on {ok}/200 keys (mismatch {bad})")
# distribution: shipped all-mid vs controls vs closed form
for nm, D in (("controls", C), ("shipped", host.dials())):
    car = 0; land = 0
    for i in range(N * 4):
        pp, m = tell_world()
        inp, card, out, band = sit_ab(pp, m, ("dist", i), D=D)
        car += band[0] in CARRIED; land += band[1] >= 0
    print(f"   {nm}: all-mid P(carried) {car/(N*4):.3f} P(lands, m>=0) {land/(N*4):.3f} (n={N*4}, se {se(car/(N*4), N*4):.3f})")
pp, m = tell_world(); inp, _ = host.build(pp, "conversation", m, form="abridged", D=C)
a = inp.room[0]; b = inp.room[1]
from sc2.engine import case_pool
pool = case_pool(inp, a, "evidence"); ob = even_line(6) + opposed_ob(b.will + b.rank, MU_PER_DIE) + inp.rite.difficulty
print(f"   closed form of the plain roll: P(m>=1) {p_at_least(pool, ob + 1):.3f} P(m>=0) {p_at_least(pool, ob):.3f}")

# ---------------------------------------------------------------- 2. the lie: detection by the hearer's Attunement
D = host.dials()
lie = Item("claim", "record", 0.8, source="a", about="b", sincere=False)
true_ = Item("claim", "record", 0.8, source="a", about="b", sincere=True)
print("\n[P8.4] abridged conversation, speaker argues on a record item (weight .8); hearer Attunement 1..7; n=%d each" % N)
print("   att | lie: carried  lands | true item: carried lands | 'hypocrite' ledger rows when the lie CARRIED")
for att in range(1, 8):
    row = []
    for it in (lie, true_):
        car = land = hyp = 0
        for i in range(N):
            pp, m = tell_world(b_attrs={"attunement": att}, items=(it,))
            inp, card, out, band = sit_ab(pp, m, ("lie", i), dec=ground("evidence"))
            assert out.beats[0].ground == "evidence" and out.beats[0].item == "claim", out.beats[0]
            car += band[0] in CARRIED; land += band[1] >= 0
            if it is lie and band[0] in CARRIED:
                w = host.new_world(); host.fold(w, pp, inp, card, out, m)
                hyp += any(r[0] == "hypocrite" for r in w["ledgers"].get("b", []))
        row.append((car / N, land / N, hyp))
    print(f"    {att}  | {row[0][0]:.3f} {row[0][1]:.3f}      | {row[1][0]:.3f} {row[1][1]:.3f}            | {row[0][2]} of {int(row[0][0]*N)}")

# lie through what he knows (no item): believes -1 vs +1, arguing consequence
print("\n[P8.2] lie without an item: speaker KNOWS the matter cuts against his side (believes -1) vs believes +1; hearer Att 7 / 1")
for att in (1, 7):
    for bel in (-1.0, 0.0, 1.0):
        car = 0; ins = []
        for i in range(N):
            pp, m = tell_world(b_attrs={"attunement": att}, believes=bel, b_layers=dict(pursuits={"t": 0.8}), bears={"t": 1.0})
            inp, card, out, band = sit_ab(pp, m, ("bel", i), dec=ground("consequence"))
            car += band[0] in CARRIED; ins.append(out.beats[0].insincere)
        print(f"   hearer att {att}, believes {bel:+.0f}: carried {car/N:.3f}  insincerity on the beat {sum(ins)/len(ins):.2f}")

# against own interest: the matter HURTS the speaker (his pursuit loses), he argues for it; he believes it (believes +1)
print("\n[P8.2 word] speaker argues FOR a matter that costs him (his pursuit bears -1), believing it right; hearer Att 7 / 1")
for att in (1, 7):
    for sb in (+1.0, -1.0):
        car = 0; ins = []
        for i in range(N):
            pp, m = tell_world(b_attrs={"attunement": att}, believes=1.0, a_layers=dict(pursuits={"own": 0.9}),
                               b_layers=dict(pursuits={"t": 0.8}), bears={"t": 1.0, "own": sb})
            inp, card, out, band = sit_ab(pp, m, ("int", i), dec=ground("consequence"))
            car += band[0] in CARRIED; ins.append(out.beats[0].insincere)
        print(f"   hearer att {att}, matter {'serves' if sb > 0 else 'COSTS'} the speaker: carried {car/N:.3f} insincerity {sum(ins)/len(ins):.2f}")

# ---------------------------------------------------------------- 3. hostile vs friendly hearer; the hearer's own mind
print("\n[P8.3] hearer disposition (n=%d)" % N)
cases = {
    "neutral": dict(),
    "friend (tie +0.8 to speaker)": dict(b_layers=dict(relationships={"a": 0.8})),
    "foe (tie -0.8 to speaker)": dict(b_layers=dict(relationships={"a": -0.8})),
    "matter serves hearer (pursuit +)": dict(b_layers=dict(pursuits={"t": 0.8}), bears={"t": 1.0}),
    "matter hurts hearer (pursuit -)": dict(b_layers=dict(pursuits={"t": 0.8}), bears={"t": -1.0}),
}
for nm, kw in cases.items():
    res = []
    for g in ("solidarity", "consequence", None):
        car = 0
        for i in range(N):
            pp, m = tell_world(**kw)
            inp, card, out, band = sit_ab(pp, m, ("hf", i), dec=ground(g) if g else None)
            car += band[0] in CARRIED
        res.append(f"{g or 'auto'} {car/N:.3f}")
    print(f"   {nm:34s} " + " | ".join(res))
for attr in ("will", "reason", "attunement", "focus"):
    r = []
    for x in (1, 4, 7):
        car = 0
        for i in range(N):
            pp, m = tell_world(b_attrs={attr: x}, b_layers=dict(pursuits={"t": 0.8}), bears={"t": 1.0})
            inp, card, out, band = sit_ab(pp, m, ("hm", i), dec=ground("consequence"))
            car += band[0] in CARRIED
        r.append(f"{x}:{car/N:.3f}")
    print(f"   hearer {attr:10s} " + " ".join(r))

# ---------------------------------------------------------------- 4. one speech to one person; bystanders; refusal; determinism
print("\n[P8.1] scope")
pp, m = tell_world(); pp["j1"] = F.P("j1", office=F.seat(3, "Crown"))
inp, card, out, band = sit_ab(pp, m, ("sc", 0), rite="trial", floor=("crowd",), bench=("j1",))
print(f"   abridged trial with an open floor: room {[(p.id, p.side, p.decides) for p in inp.room]}; beats {len(out.beats)}; "
      f"moved {out.beats[0].moved}; verdicts {[v[0] for v in out.verdicts]}")
w = host.new_world(); host.fold(w, pp, inp, card, out, m)
print(f"   fold regard rows for the bystander crowd: {[(k, round(v, 3)) for k, v in w['regard'].items() if k[0] == 'crowd']}")
try:
    host.build({"a": F.P("a"), "crowd": F.P("crowd", weight=30)}, "rally", dict(id="m", parties={"for": "a"}, bears={}), floor=("crowd",), form="abridged")
    print("   abridged rally with nobody addressed: NOT refused")
except Exception as e:
    print(f"   abridged rally with nobody addressed: refused -> {e}")
hs = [h(sit_ab(*tell_world(), ("det", 3))[2]) for _ in range(2)]
print(f"   same seed twice: {hs} {'equal' if hs[0] == hs[1] else 'DIFFER'}")

print("\n[P8.3b] speaker Reason x hearer Reason (consequence; matter serves hearer)")
for sr in (1, 7):
    r = []
    for hr in (1, 4, 7):
        car = 0
        for i in range(N):
            pp, m = tell_world(a_attrs={"reason": sr}, b_attrs={"reason": hr}, b_layers=dict(pursuits={"t": 0.8}), bears={"t": 1.0})
            inp, card, out, band = sit_ab(pp, m, ("rr", i), dec=ground("consequence"))
            car += band[0] in CARRIED
        r.append(f"hearer {hr}:{car/N:.3f}")
    print(f"   speaker reason {sr}: " + " ".join(r))
