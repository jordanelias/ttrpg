"""P5 information: what a `decide` callback can learn about the other side's TRUE values.
(1) the view's fields; (2) in a bench row the reading's `target:g` and `other:g` share one xi per ground, so their
difference is the true difference of the means, noise-free whenever neither is clamped; (3) the Exchange record's
levels/terms recover the target's true Will, score and body fit exactly.
    PYTHONHASHSEED=0 python lane3/p5_info.py"""
import dataclasses
import random

from harness import person, bench_people, scene_kw, P, dialmod, build_input, draw, ATTRS
from scmodel.records import Choice
from scmodel.proceeding import proceed

D = dialmod.shipped()
views = []


def spy(view):
    views.append(view)
    return Choice("argue", P._argmax(view.read, "target:", ["evidence", "consequence", "authority", "solidarity"])) \
        if "argue" in view.legal else Choice(view.legal[0], None)


print("ExchangeView fields:", [f.name for f in dataclasses.fields(views and views[0] or __import__('scmodel.records', fromlist=['ExchangeView']).ExchangeView)])
tot = exact = 0
worst = 0.0
will_err = score_err = fit_err = 0.0
nrec = 0
for t in range(300):
    rnd = random.Random(t)
    A = person("a", {k: rnd.randint(1, 7) for k in ATTRS}, pursuits={"x": rnd.random()}, convictions={"c": rnd.randint(0, 5)})
    B = person("b", {k: rnd.randint(1, 7) for k in ATTRS}, rank=rnd.randint(0, 3), pursuits={"x": rnd.random()},
               convictions={"c": rnd.randint(0, 5)})
    people = {"a": A, "b": B}
    people.update(bench_people({k: rnd.randint(1, 7) for k in ATTRS}))
    inp = build_input(people, "legal_trial", "full", "argue", actor="a", dials=D, effort=2, **scene_kw("legal_trial"))
    views.clear()
    out = proceed(inp, draw(("p5", t), "a", "r"), spy)
    for v in views:
        i = [S.id for S in inp.speakers].index(v.mover)
        j = 1 - i
        body = P._body(inp, i)
        W = sum(b.weight for b in body)
        r = dict(v.read)
        for g in inp.grounds:
            tv = sum(b.weight * dict(b.moved_by)[g] for b in body) / W
            ov = dict(inp.speakers[j].moved_by)[g]
            bt, bo = r["target:" + g], r["other:" + g]
            if 0 < bt < 1 and 0 < bo < 1:
                tot += 1
                e = abs((bt - bo) - (tv - ov))
                worst = max(worst, e)
                exact += e < 1e-9
    # (3) the record
    for x in out.exchanges:
        lv = {s: (f, a) for s, f, a in x.levels}
        if "resist" not in lv:
            continue
        i = [S.id for S in inp.speakers].index(x.mover)
        T = inp.speakers[1 - i]
        f, a = lv["resist"]
        will_hat = D["attribute_mid"] + (a - f) / D["resist_step"]
        will_err = max(will_err, abs(will_hat - T.will))
        opp = dict(x.terms).get("opposition")
        score_err = max(score_err, abs(opp / D["opposition_rate"] - T.score))
        if x.move == "argue" and x.ground:
            ff, fa = lv["fit"]
            fb_hat = ff / 0.75 - fa / 0.5
            fb = P._fit_body(P._body(inp, i), x.ground)
            fit_err = max(fit_err, abs(fb_hat - fb))
        nrec += 1
print(f"(2) unclamped (target:g - other:g) pairs: {tot}; equal to the TRUE difference within 1e-9: {exact}; max error {worst:.2e}")
print(f"(3) over {nrec} drawn exchanges: max |Will recovered from levels['resist'] - true| = {will_err:.2e}; "
      f"max |score from terms['opposition'] - true| = {score_err:.2e}; max |body fit from levels['fit'] - true| = {fit_err:.2e}")
print("(1) view.own is the mover's own SideState; view.read holds acc, target:g, other:g, strain; no exchange list, no "
      "opponent SideState, no track magnitude (track_sign only).")
