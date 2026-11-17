"""fix3 invariants: the stress test's fuzz (lane C, `fuzz.py`) and its violation checks (lane C `common.py`, ported
from checks_v8_core's TYPES block), run on whichever model `SC2` names, plus the held properties the fix brief lists.
python -B inv.py COUNT  ->  a summary: crashes (any exception that is not a keyed refusal), refusals by key,
violations, world bounds, determinism; the abridged form against the plain roll; A-139; monotone office power."""
import json, random, hashlib, traceback
from common import *
from sc2.lab import smart
BANDS = ("failure", "partial", "success", "overwhelming", None)


def force(pred):
    def f(v, me):
        os_ = [o for o in v.options if pred(o)] or list(v.options)
        o = max(os_, key=lambda o: o.ev)
        return Choice(o.move, o.ground, o.item, o.relation)
    return f


def only(mv):
    return force(lambda o: o.move == mv)


def rnd(seed):
    def f(v, me):
        o = random.Random(repr((seed, v.n, v.mover))).choice(v.options)   # hash-free: deterministic across processes
        return Choice(o.move, o.ground, o.item, o.relation)
    return f


def policy(name, seed=0):
    if name == "auto":
        return None
    if name == "best":
        return smart
    if name == "random":
        return rnd(seed)
    return only(name)                                   # press / rest / concede / argue (falls back to argue/any)


def violations(inp, card, out, band):
    """ported from checks_v8_core TYPES block, plus probability / band sanity."""
    v = Counter()
    held = {p.id: {it.id for it in p.items} for p in inp.room}
    kinds = {it.id: it.kind for p in inp.room for it in p.items}
    closed, spoke = set(), Counter()
    base = inp.state.n if inp.state is not None else 0
    for k, x in enumerate(out.beats):
        v["chain"] += x.n != base + k + 1
        v["no point"] += x.move == "argue" and x.point is None
        v["answers nothing"] += x.relation == "answers" and not any(p.id == x.point and p.side != x.side for p in out.state.points)
        v["item not held"] += bool(x.item) and x.item not in held[x.mover]
        v["item not admitted"] += bool(x.item) and kinds.get(x.item) not in card.admits
        v["closed issue re-argued"] += x.issue in closed
        v["move not on the card"] += x.move not in dict(card.moves).get(x.side, ())
        v["evasion unpriced"] += x.evaded and not x.rattled and not any(d != 0 for _, d in x.moved) and any(p.focus > 1 for p in inp.room if p.side != x.side)
        v["non-deciding speaker moved own track"] += any(q == x.voice and not next(p for p in inp.room if p.id == q).decides for q, _ in x.moved)
        if x.closed and not (out.ended == "yielded" and k == len(out.beats) - 1):
            closed.add(x.closed)
        spoke[x.mover] += 1
        v["nan in beat"] += any(isinstance(a, float) and not math.isfinite(a) for a in (x.margin, x.drift, x.mood, x.esteem, x.heard, x.relevance))
    # spoken counts across a resumed sitting are in state.cond
    v["over the card's turns"] += any(c.spoken > card.turns for _, c in out.state.cond)
    if card.close != "consent":
        v["verdicts != the card's adjudicators"] += set(i_ for i_, _ in out.verdicts) != set(card.decided_by)
    if inp.state is None:
        v["track != start + beats"] += any(abs(dict(out.state.tracks)[p.id] - p.start - sum(d for x in out.beats for q, d in x.moved if q == p.id)) > 1e-6 for p in inp.room)
    v["consent with a verdict"] += card.close == "consent" and bool(out.verdicts)
    v["nan track"] += any(not math.isfinite(t) for _, t in out.state.tracks)
    v["band unknown"] += band[0] not in BANDS
    v["odds out of [0,1]"] += card.odds is not None and not (0.0 <= card.odds <= 1.0)
    v["card turns != rite turns"] += card.turns != inp.rite.turns
    v["decided_by != deciding room"] += tuple(p.id for p in inp.room if p.decides) != card.decided_by
    return v


def world_bounds(world):
    v = Counter()
    for k in ("regard", "legitimacy", "standing", "pursuits"):
        for a, x in world[k].items():
            v[f"{k} out of [-1,1]"] += not (-1.0 - 1e-9 <= x <= 1.0 + 1e-9) or not math.isfinite(x)
    for k, x in world["strife"].items():
        v["strife out of [0,1]"] += not (0.0 <= x <= 1.0)
    for k, x in world["compliance"].items():
        v["compliance out of [0,1]"] += not (0.0 <= x <= 1.0)
    return v


def band2(b):
    return 2.0 * math.sqrt(max(b * (1 - b), 1e-12))


RITE_IDS = tuple(host.RITES) + tuple(host.ALIASES)
FACS = ("Crown", "Parliament", "Church", "Guild")
TAGS = ("tolls", "trade", "faith", "law", "grain", "office", "commons", "war")
KINDS = tuple(host.MATTERS)
POLS = ("auto", "auto", "best", "random", "press", "rest", "concede", "argue")


def attr(r):
    return r.choice((1, 7)) if r.random() < 0.3 else r.randint(1, 7)


def person(r, pid, ids, i):
    a = {k: attr(r) for k in host.ATTRS}
    off = None
    if r.random() < 0.5:
        off = F.seat(r.randint(1, 5), r.choice(FACS + (None,)) if r.random() < 0.95 else "Nobody",
                     r.choice((None, None, "minor", "moderate", "strong", "major")),
                     {t: r.uniform(-1, 1) for t in r.sample(TAGS, r.randint(0, 2))})
    others = [q for q in ids if q != pid]
    L = {}
    if r.random() < 0.7:
        L["pursuits"] = {t: r.uniform(0, 1) for t in r.sample(TAGS, r.randint(0, 3))}
    if r.random() < 0.3:
        L["needs"] = {t: r.uniform(0, 1) for t in r.sample(TAGS, r.randint(1, 2))}
    if r.random() < 0.3:
        L["goals"] = tuple(r.sample(TAGS, r.randint(1, 2)))
    if r.random() < 0.3:
        L["ambitions"] = tuple(r.sample(TAGS, 1))
    if r.random() < 0.6:
        L["convictions"] = {t: r.randint(0, 5) for t in r.sample(TAGS, r.randint(1, 3))}
    if others and r.random() < 0.6:
        L["relationships"] = {q: r.uniform(-1, 1) for q in r.sample(others, r.randint(1, min(3, len(others))))}
    if others and r.random() < 0.2:
        L["kin"] = tuple(r.sample(others, 1))
    if others and r.random() < 0.2:
        L["patron"] = r.choice(others)
    if others and r.random() < 0.2:
        L["clients"] = tuple(r.sample(others, 1))
    if others and r.random() < 0.2:
        L["debts"] = {r.choice(others): r.uniform(-1, 1)}
    items = []
    for k in range(r.randint(0, 3)):
        items.append(E.Item(f"it{i}_{pid}_{k}", r.choice(KINDS), round(r.uniform(0, 1), 2),
                            source=r.choice(ids + [None]), about=r.choice(ids + [None]), sincere=r.random() > 0.2))
    w = r.choice((1, 1, 1, 1, 3, 30, 200)) if r.random() > 0.02 else 0
    p = F.P(pid, rank=r.choice((0, 0, 1, 1, 2, 3)), weight=w, office=off,
            faction=r.choice(FACS + (None, None)), items=items, layers=L, **a)
    if r.random() < 0.3:
        p["believes"] = {"m": r.uniform(-1, 1)}
    if r.random() < 0.3:
        p["bias"] = r.uniform(-1, 1)
    if r.random() < 0.2:
        p["rattled_ago"] = tuple(r.randint(0, 3) for _ in range(r.randint(1, 3)))
    return p


def config(i):
    r = random.Random(f"fuzz{i}")
    n = r.randint(2, 9)
    ids = [f"p{k}" for k in range(n)]
    people = {pid: person(r, pid, ids, i) for pid in ids}
    rite = r.choice(RITE_IDS)
    u = r.random()
    against = None if u < 0.12 else ("p0" if u < 0.14 else "p1")
    m = dict(id="m", parties={"for": "p0", "against": against},
             bears={t: round(r.uniform(-1, 1), 2) for t in r.sample(TAGS, r.randint(0, 4))})
    if r.random() < 0.3:
        m["factions"] = {f: r.choice((-0.5, 0.5)) for f in r.sample(FACS, r.randint(1, 2))}
    if r.random() < 0.2:
        m["strife"] = "famine"
    if r.random() < 0.1:
        m["disposes"] = r.choice(tuple(host.DISPOSAL))
    bench = tuple(r.sample(ids, r.randint(0, n)))
    floor = tuple(r.sample(ids, r.randint(0, n)))
    kw = dict(bench=bench, floor=floor, form=r.choice(("full", "full", "full", "abridged", "auto")),
              era=r.choice(tuple(host.ERAS)), regime=r.choice(tuple(host.REGIMES)), strife=r.choice(tuple(host.STRIFE)),
              arranger=r.choice((None, None, "p0", "p1", r.choice(ids))), rig=r.choice((0.0, 0.0, 0.5, 1.0)),
              effort=r.choice((None, 0, 1, 2, 3, 4)), difficulty=r.choice(tuple(host.DIFFICULTY)))
    if kw["arranger"] not in people:
        kw["arranger"] = None
    if r.random() < 0.05:
        kw["grounds_for"] = (r.choice(("for", "against")), r.uniform(0, 1))
    pols = {pid: r.choice(POLS) for pid in ids}
    resume = r.random() < 0.08
    return people, rite, m, kw, pols, resume


def run(i):
    people, rite, m, kw, pols, resume = config(i)
    dec = {pid: policy(p, i) for pid, p in pols.items() if p != "auto"}
    inp, card = host.build(people, rite, m, **kw)
    out = proceed(inp, draw(("fz", i), "act", rite), None, dec)
    band = host.act_band(inp, out)
    viol = violations(inp, card, out, band)
    if resume and out.ended != "yielded":
        inp2, card2 = host.build(people, rite, m, state=out.state, **dict(kw, effort=4))
        out2 = proceed(inp2, draw(("fz2", i), "act", rite), None, dec)
        b2 = host.act_band(inp2, out2)
        viol.update(violations(inp2, card2, out2, b2))
        inp, card, out, band = inp2, card2, out2, b2
    world = host.new_world()
    if m.get("strife"):
        world["strife"][m["strife"]] = 1.0
    b, writes = host.fold(world, people, inp, card, out, m)
    viol["fold band != act_band"] += b != band[0]
    act, opts = acts.after(world, people, inp, card, out, m, b)
    viol.update(world_bounds(world))
    h = hashlib.sha256(repr((band[0], round(band[1] or 0, 9), out.ended, len(out.beats),
                             tuple(sorted((k, round(v, 9)) for k, v in world["regard"].items())))).encode()).hexdigest()[:16]
    return dict(i=i, rite=rite, regime=kw["regime"], close=card.close, band=band[0], ended=out.ended, beats=len(out.beats),
                tilt=card.tilt, moves=[x.move for x in out.beats], act=act, viol={k: v for k, v in viol.items() if v}, hash=h,
                n=len(people), resume=resume)


def sig_of(e):
    tb = traceback.extract_tb(e.__traceback__)
    fr = [f for f in tb if "/model/" in f.filename][-1:] or tb[-1:]
    import re
    msg = re.sub(r"p\d+", "pX", str(e))[:120]
    return f"{type(e).__name__}: {msg} @ {fr[0].filename.split('/')[-1]}:{fr[0].lineno}" if fr else f"{type(e).__name__}: {msg}"



def summary(count):
    crash, refused, viol, det, ran = Counter(), Counter(), Counter(), Counter(), 0
    for i in range(count):
        try:
            rec = run(i); ran += 1
            viol.update(rec["viol"])
            if i % 25 == 0:
                det[run(i)["hash"] == rec["hash"]] += 1
        except ValueError as e:
            s = str(e)
            if s.startswith("refused["):
                refused[s.split("]")[0] + "]"] += 1
            else:
                crash[sig_of(e)] += 1
        except Exception as e:                            # noqa: BLE001
            crash[sig_of(e)] += 1
    H(f"fuzz {count} configs: ran {ran}; crashes {sum(crash.values())} {dict(crash)}")
    print(f"  refusals {dict(sorted(refused.items()))}")
    print(f"  violations {dict(viol) or 0}; determinism (every 25th re-run) {dict(det)}")


def abridged_plain():
    from scmodel import dice
    mp, M, C = F.mid_people(), F.matter(), host.controls()
    ok = 0
    for i in range(200):
        inp, card = host.build(mp, "conversation", M, form="abridged", D=C); out = proceed(inp, draw(("eq", i), "act", "conversation"))
        rng = draw(("eq", i), "act", "conversation"); [rng.normal() for _ in range(E.DRAWS_PER_EXCHANGE(4) - 1)]
        x = dice.SocialContestInput(pool=11.0, opposition=5.0, leverage=0.0, difficulty=0.5, obstacle_operands=(), pool_default=2,
                                    pool_add=6, opposition_rate=0.4, obstacle_ceiling=None, ceiling_per_pool=False)
        m = dice.roll(x, rng); v = out.verdicts[0][1]; ok += abs((v.net - v.ob) - (m.net - m.ob)) < 1e-9
    print(f"  abridged == the plain roll at control: {ok}/200")


def a139_power(n):
    mp, M = F.mid_people(), F.matter()
    print("  A-139 one party twice:", attempt(lambda: host.build(mp, "trial", F.matter(ag="a"), bench=BENCH)))
    pj = castB(pa="r3")
    print("  A-139 a party who also judges (the accuser holds the one seat):", attempt(lambda: host.build(pj, "trial", mat(), bench=("a",))[1].decided_by))
    row = []
    for lv in ("none", "r2", "r3", "r4m", "r5M"):
        pp = castB(pa=lv, seat_fac="Parliament")
        k = sum(sit(pp, "trial", mat(), ("pw", i), bench=BENCH, effort=3)[3][0] in CARRIED for i in range(n))
        row.append(f"{lv} {k/n:.3f}")
    print(f"  office power of the accuser (trial, n={n} each; monotone expected within 2 s.e. {2*se(.3,n):.3f}): " + " | ".join(row))


if __name__ == "__main__":
    import sys
    count = int(sys.argv[1]) if len(sys.argv) > 1 else 1500
    summary(count)
    abridged_plain()
    a139_power(int(sys.argv[2]) if len(sys.argv) > 2 else 400)
