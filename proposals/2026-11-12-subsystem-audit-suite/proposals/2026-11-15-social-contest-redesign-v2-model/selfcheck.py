"""selfcheck -- every number the spec itself asserts as a falsifier, run against the model.

    cd <sc_model> && PYTHONHASHSEED=0 python selfcheck.py [--n 5000]

Each check prints PASS / FAIL / READ (a reading the spec gives as approximate, reported with its value). A FAIL is a
spec assertion the model, built as written, does not reproduce: a finding (see SPEC_GAPS.md, "Self-check findings").
Exit code: the number of FAILs.
"""
from __future__ import annotations

import argparse
import math
import sys
from dataclasses import replace

import scmodel  # noqa: F401
from scmodel import data, dials as dialmod, proceeding as P
from scmodel.demo import default_people
from scmodel.dice import Margin, SocialContestInput, band_odds, level, obstacle, p_at_least, pool_of, roll
from scmodel.host import abridged, audience_kind, build_input
from scmodel.records import Choice
from scmodel.rng import draw

RESULTS = []


def check(name, ok, detail=""):
    RESULTS.append((name, "PASS" if ok else "FAIL", detail))


def read(name, detail):
    RESULTS.append((name, "READ", detail))


# ---------------------------------------------------------------- helpers
def person(pid, **attrs):
    base = {k: 4 for k in ("focus", "reason", "attunement", "presence", "grace", "will")}
    base.update(attrs)
    return {"id": pid, "attributes": base}


def tell_input(D, a=None, b=None, row="conversation", move="argue", bias=None, standard=None, attention=None,
               present=(), extra=None, order=None):
    """an abridged speech by `a` to `b` under `row`, with the type/room patched as a falsifier plants it."""
    people = {"a": a or person("a"), "b": b or person("b")}
    for p in (extra or ()):
        people[p["id"]] = p
    inp = build_input(people, row, "abridged", move, actor="a", addressed="b", dials=D, present=present, order=order)
    typ = inp.type
    if bias is not None:
        typ = replace(typ, reason_bias=bias)
    if standard is not None:
        typ = replace(typ, standard=D["standard_demand"][standard])
    inp = replace(inp, type=typ)
    if attention is not None:
        inp = replace(inp, room=replace(inp.room, attention=attention))
    return inp


def speech(inp, ground, move="argue", on_topic=True, i=0, state=None):
    st = state or P._start(inp)
    T, _ = P._target(inp, i)
    return P._speech_input(inp, i, st.sides[i], T, P._move_by_id(inp, move), ground, on_topic)


def lv(levels, name):
    for s, f, a in levels:
        if s == name:
            return (f, a)
    return None


def tm(terms, name):
    return dict(terms).get(name)


def se_diff(p1, p2, n):
    return math.sqrt(p1 * (1 - p1) / n + p2 * (1 - p2) / n)


def main(n):
    S = dialmod.shipped()
    C = dialmod.controls()
    mid = S["attribute_mid"]

    # ---------------- B.2 a: k values and pool differences (RD:608-617; B24p.07; B24p.18)
    for g, bias, k_exp in (("evidence", 0.2, 10), ("solidarity", -0.3, 0), ("authority", 0.0, 4)):
        inp = tell_input(S, bias=bias)
        k = P._k(inp, P._move_by_id(inp, "argue"), g)
        check(f"B.2a k({g}, bias {bias:+.1f}) == {k_exp}", k == k_exp, f"k={k}")
    for g, bias, attr, exp, label in (
            ("evidence", 0.2, "reason", 4.0, "B.2(i) judicial: Reason 2->6 pool diff = 4 x heard"),
            ("solidarity", -0.3, "reason", 0.0, "B.2(i') crowd: Reason 2->6 equal pools"),
            ("authority", 0.0, "reason", 1.6, "B.2(i') balanced: Reason 2->6 pool diff = 1.6 x heard"),
            ("solidarity", -0.3, "presence", 4.0, "B.4(o) crowd k=0: Presence 2->6 pool diff = 4"),
            ("evidence", 0.2, "presence", 0.0, "B.4(o) judicial k=10: Presence 2->6 equal pools"),
            ("authority", 0.0, "presence", 2.4, "B24p.18: k=4 Presence 2->6 pool-before-heard diff = 2.4")):
        for att in (0.0, 5.0):
            lo = tell_input(S, a=person("a", **{attr: 2}), bias=bias, attention=att)
            hi = tell_input(S, a=person("a", **{attr: 6}), bias=bias, attention=att)
            xl, _, pl, hl = speech(lo, g)
            xh, _, ph, hh = speech(hi, g)
            if label.startswith("B24p.18") or "Presence" in label:
                d, want = ph - pl, exp                       # pool before heard (Presence also moves heard)
            else:
                d, want = xh.pool - xl.pool, exp * hl        # recorded pool; heard equal across Reason
            check(f"{label} [attention {att:g}] (spec: 'exactly', float ==)", d == want,
                  f"diff={d!r} want={want!r} (heard {hl}, {hh})")
            check(f"{label} [attention {att:g}] (within 1e-9)", abs(d - want) < 1e-9, f"diff={d!r}")
    # ---------------- B.2 (ii), (iii)
    for r, want in ((2, 1.0), (6, 3.0)):
        inp = tell_input(S, a={**person("a", reason=r), "proofs": 5.0})
        _, levs, _, _ = speech(inp, "evidence")
        usable = lv(levs, "proofs")[0] / (level(S["proof_level"]) * 2 * inp.room.proof_weight)
        check(f"B.2(ii) five proofs, Reason {r}: usable {want}", abs(usable - want) < 1e-12, f"usable={usable}")
    inp0 = tell_input(S, a={**person("a"), "proofs": 0.0})
    check("B.2(ii) no proofs: source 0", lv(speech(inp0, "evidence")[1], "proofs") == (0.0, 0.0))
    rg = []
    for r in (2, 4, 6):
        a = {**person("a", reason=r), "operands": [("rank_gap", 2.0, 0.5, "reason")], "knows": ["b"]}
        rg.append(tm(obstacle(speech(tell_input(S, a=a), "evidence")[0])[1], "rank_gap"))
    check("B.2(iii) rank_gap term falls strictly with Reason when known", rg[0] > rg[1] > rg[2], f"{rg}")
    rg2 = []
    for r in (2, 6):
        a = {**person("a", reason=r), "operands": [("rank_gap", 2.0, 0.5, "reason")]}
        rg2.append(tm(obstacle(speech(tell_input(S, a=a), "evidence")[0])[1], "rank_gap"))
    check("B.2(iii) rank_gap equal across Reason when unknown", rg2[0] == rg2[1], f"{rg2}")
    check("B.2 table: Reason 7 discounts a known circumstance by 0.9",
          abs(P._account(tell_input(S, a=person("a", reason=7)).speakers[0], S) - 0.9) < 1e-12)

    # ---------------- B.4 (i)-(iii)
    for p_, want in ((2, (0.0, 0.5)), (6, (0.5, 0.0))):
        inp = tell_input(S, a=person("a", presence=p_), bias=0.2, attention=0.0)
        got = lv(speech(inp, "evidence")[1], "delivery")
        check(f"B.4(i) delivery at Presence {p_} = {'-' if p_ < 4 else '+'}0.5", got == want, f"{got}")
    lo = speech(tell_input(S, a=person("a", presence=2), bias=0.2, attention=5.0), "evidence")[0].pool
    hi = speech(tell_input(S, a=person("a", presence=6), bias=0.2, attention=5.0), "evidence")[0].pool
    check("B.4(ii) attention 5: pool(P2) == pool(P6) x 0.7 exactly", lo == hi * 0.7, f"{lo!r} vs {hi * 0.7!r}")
    check("B.4(ii) ... within 1e-12", abs(lo - hi * 0.7) < 1e-12, f"{lo!r} vs {hi * 0.7!r}")
    w2 = speech(tell_input(S, a=person("a", presence=2), bias=0.2, attention=5.0, order="written_only"), "evidence")
    w6 = speech(tell_input(S, a=person("a", presence=6), bias=0.2, attention=5.0, order="written_only"), "evidence")
    check("B.4(iii) written_only: heard and delivery equal across Presence",
          w2[3] == w6[3] and lv(w2[1], "delivery") == lv(w6[1], "delivery"))

    # ---------------- B.5 (i), (ii)
    vs = {g: tm(obstacle(speech(tell_input(S, a=person("a", grace=g), standard="hard"), "evidence")[0])[1],
                "venue_standard") for g in (2, 5, 6, 7)}
    check("B.5(i) hard: venue_standard 1.5 at Grace 2, 0 at 5/6/7", vs == {2: 1.5, 5: 0.0, 6: 0.0, 7: 0.0}, f"{vs}")
    pl = [obstacle(speech(tell_input(S, a=person("a", grace=g), standard="plain"), "evidence")[0])[0] for g in (2, 6)]
    check("B.5(i) plain: obstacle equal at Grace 2 and 6", pl[0] == pl[1], f"{pl}")
    e = [P._start(tell_input(S, a=person("a", grace=g))).sides[0].esteem for g in (2, 6)]
    check("B.5(ii) esteem starts -0.16 / +0.16", abs(e[0] + 0.16) < 1e-12 and abs(e[1] - 0.16) < 1e-12, f"{e}")

    # ---------------- B.6 (ii), (iii), (iv); table
    r0 = [P._start(tell_input(S, a=person("a", will=w))).sides[0].resolve for w in (2, 6)]
    check("B.6(ii) resolve_0 = 3.0 / 5.0", r0 == [3.0, 5.0], f"{r0}")
    r1 = [P._start(tell_input(S, a=person("a", will=w))).sides[0].resolve for w in (1, 6)]
    check("B.6 table: Will 1 speaks 2.5 exchanges, Will 6 five", r1 == [2.5, 5.0], f"{r1}")
    flat = {"traits": []}
    for w, want in ((2, -0.9), (6, -0.5)):
        a = person("a", will=w)
        b = person("b")
        inp = tell_input(S, a=a, b=b, bias=0.2)
        sp = replace(inp.speakers[0], levels=(("planted", 0.0, 1.0),), moved_by=inp.speakers[0].moved_by)
        # flat target vector so fit is 0; everything else at mid
        inp = replace(inp, speakers=(sp,), deciders=(replace(inp.deciders[0], moved_by=tuple(
            (g, 0.5) for g in data.GROUND_IDS)),))
        x = speech(inp, "evidence")[0]
        check(f"B.6(iii) 1.0 sigma against at Will {w}: net sigma {want}", abs(x.leverage - want) < 1e-12,
              f"leverage={x.leverage!r}")
    for w, side in ((6, "against"), (2, "for")):
        inp = tell_input(S, b=person("b", will=w))
        got = lv(speech(inp, "evidence")[1], "resist")
        ok = (got[1] > 0 and got[0] == 0) if side == "against" else (got[0] > 0 and got[1] == 0)
        check(f"B.6(iv) hearer Will {w}: resist {side}", ok, f"{got}")
    hostile = {**person("a"), "operands": []}
    rec = []
    for w in (2, 6):
        a = person("a", will=w)
        b = {**person("b"), "regard": {"a": -1.0}}
        inp = tell_input(S, a=a, b=b)
        rec.append(tm(obstacle(speech(inp, "evidence")[0])[1], "regard"))
    check("B.6(iii) hostile hearer term (regard, eased_by will) lower at Will 6", rec[1] < rec[0], f"{rec}")
    check("B.6 table: Will 7 discounts what is against him by 0.6",
          abs(P._shield(tell_input(S, a=person("a", will=7)).speakers[0], S) - 0.6) < 1e-12)

    # ---------------- B.9: the zero, f_d, pw_d, relevance exact
    D9 = dialmod.shipped(strike_level="minor")
    full = build_input({"a": person("a"), "b": person("b"), "j": {**person("j"), "seat": {"rung": "duchy",
                        "faction": "Crown"}}}, "legal_trial", "full", actor="a", addressed="b", bench=("j",),
                       dials=D9, effort=3)
    out = P.proceed(full, draw(1, "a", "t"))
    d_mid = replace(full.deciders[0], reason=mid)
    check("B.9 zero: sense == 0 exactly at a decider of Reason mid (pw_d = pw)",
          P._ballot_sense(full, d_mid, out.exchanges) == 0.0)
    full0 = replace(full, dials=dialmod.shipped(sense_step=0.0))
    check("B.9 zero: sense == 0 exactly at sense_step 0",
          P._ballot_sense(full0, replace(full.deciders[0], reason=7), out.exchanges) == 0.0)
    pwd = full.room.proof_weight + D9["sense_step"] * (7 - mid)
    check("B.9 table: Reason 7 before a bench: 0.75 -> 0.90", abs(pwd - 0.90) < 1e-12 and full.room.proof_weight
          == 0.75, f"pw={full.room.proof_weight} pw_d={pwd}")
    fd = [max(0, min(2, 1 + D9["relevance_step"] * (f - mid))) for f in (1, 7)]
    check("B.9 table: f_d Focus 1 -> 0.25, Focus 7 -> 1.75", fd == [0.25, 1.75], f"{fd}")
    # two strikes planted on `for`, k = 1
    t1 = replace(full.type, strikes=1)
    full1 = replace(full, type=t1)
    st = replace(out.state, sides=(replace(out.state.sides[0], strikes=2), replace(out.state.sides[1], strikes=0)))
    for f in (2, 6):
        d = replace(full1.deciders[0], focus=f)
        f_d = max(0, min(2, 1 + D9["relevance_step"] * (f - mid)))
        rel = P._ballot_relevance(full1, st, d, (), [], [], 1.0)
        check(f"B.9(ii) relevance vs `for` = f_d x level x 2 at Focus {f}", rel == -(f_d * level("minor") * 2),
              f"rel={rel!r} want={-(f_d * 0.25 * 2)!r}")

    # ---------------- draw counts
    inp = tell_input(S)
    rng = draw(3, "a", "x")
    st0 = P._start(inp)
    rd = P._read(inp, 0, st0, rng)
    check("B24p.08: a reading takes len(grounds) + 2 normals", rng.count == len(inp.grounds) + 2, f"{rng.count}")
    for mv in ("argue", "press", "divert", "concede", "rest"):
        inp = build_input({"a": person("a"), "b": person("b")}, "conversation", "full", actor="a", addressed="b",
                          dials=S, effort=3)
        rng = draw(4, "a", mv)
        o = P.proceed(inp, rng, decide=lambda v, mv=mv: Choice(mv if mv in v.legal else "rest",
                                                               "evidence" if mv in ("argue", "press") else None))
        nb = 3 * len(inp.deciders)
        check(f"A.4: G+5 = 9 normals per exchange, 3 per decider ({mv})",
              rng.count == 9 * len(o.exchanges) + nb, f"count={rng.count} exchanges={len(o.exchanges)} ballots={nb}")
    # ballots in id order (deciders handed in reverse)
    ppl = default_people()
    rinp = build_input(ppl, "rally", "full", actor="a", addressed="crowd", present=("h2", "h1"), dials=S, effort=1)
    rinp = replace(rinp, deciders=tuple(reversed(rinp.deciders)))
    o = P.proceed(rinp, draw(5, "a", "r"))
    ids = [i for i, _ in o.verdicts]
    check("A.5/B.9: ballots drawn in decider id order", ids == sorted(ids), f"{ids}")

    # ---------------- track clamp
    big = {"a": {**person("a", reason=7), "ranks": {"argue": 6}, "addends": 6}, "b": person("b", reason=1),
           "j": {**person("j"), "seat": {"rung": "duchy", "faction": "Crown"}}}
    inp = build_input(big, "legal_trial", "full", actor="a", addressed="b", bench=("j",), dials=S, effort=9)
    worst = 0.0
    for k in range(300):
        o = P.proceed(inp, draw(("clip", k)))
        tr = 0.0
        for x in o.exchanges:
            worst = max(worst, abs(tr))
        worst = max(worst, abs(o.state.track))
    check("A.4: the track stays within +/- track_clip", worst <= S["track_clip"] + 1e-12, f"max |track| {worst}")

    # ---------------- B.7 control equality, model-internal (B24p.07 test)
    inp = tell_input(C)
    bad = 0
    for k in range(200):
        a = {**person("a", reason=1 + k % 7, presence=1 + (k * 3) % 7), "proofs": (k % 9) * 0.37,
             "ranks": {"argue": k % 3}}
        inp = tell_input(C, a=a)
        x, _, _, _ = speech(inp, "evidence")
        T = P._target(inp, 0)[0]
        rec = SocialContestInput(pool=pool_of(a["attributes"]["reason"] + k % 3, 0, C["pool_add"], C["pool_floor"]),
                                 opposition=T.score, leverage=level(C["proof_level"]) * int(a["proofs"] + 0.5),
                                 difficulty=inp.type.difficulty,
                                 obstacle_operands=tuple((o[0], o[1], o[2]) for o in inp.speakers[0].operands)
                                 + (("off_topic", 0.0, 0.0), ("venue_standard", max(0, inp.type.standard - 4), 0.0)),
                                 pool_default=C["pool_default"], pool_add=C["pool_add"],
                                 opposition_rate=C["opposition_rate"], obstacle_ceiling=C["obstacle_ceiling"],
                                 ceiling_per_pool=C["ceiling_per_pool"])
        o1 = P.exchange_odds(inp, P._start(inp), 0, Choice("argue", "evidence"))
        o2 = band_odds(rec.pool, obstacle(rec)[0], P.net_boost(rec.leverage, rec.pool))
        m1 = roll(x, draw(k))
        m2 = roll(rec, draw(k))
        if not (o1 == o2 and m1 == m2):
            bad += 1
    check("B.7/B24p.07 control (model-internal): at control a speech == the single roll on contest_input's record",
          bad == 0, f"{bad}/200 differ")

    # ---------------- B.7 control equality against the LIVE roll.py::roll (the task's assertion)
    try:
        from modules.social_contest import roll as LIVE
        from engine.season.queries.inputs import SocialContestInput as LiveSCI
        diffs, odds_diffs, nonce = [], [], 0
        for k in range(200):
            a = {**person("a", reason=1 + k % 7), "ranks": {"argue": k % 3}}
            inp = tell_input(C, a=a)
            G = len(inp.grounds)
            rng = draw(("live", k), "a", "roll")
            out = P.proceed(inp, rng)
            mm = out.verdicts[0][1]
            x, _, _, _ = speech(inp, out.exchanges[0].ground)
            live_in = LiveSCI(pool=x.pool, opposition=x.opposition, obstacle_default=2.0,
                              obstacle_ceiling=C["obstacle_ceiling"], obstacle_refusal_multiple=2.0,
                              leverage=x.leverage, ceiling_per_pool=True, difficulty=x.difficulty)
            r2 = draw(("live", k), "a", "roll")
            for _ in range(G + 3):          # advance the same key to the speech's slot
                r2.normal()
            c0 = r2.count
            lm = LIVE.roll(live_in, r2)
            nonce = max(nonce, r2.count - c0)
            diffs.append(((mm.net - mm.ob) - (lm.net - lm.ob), mm.ob - lm.ob))
            lo = LIVE.band_odds(x.pool, LIVE.obstacle(live_in), P.net_boost(x.leverage, x.pool))
            mo = P.exchange_odds(inp, P._start(inp), 0, Choice("argue", out.exchanges[0].ground))
            odds_diffs.append(max(abs(u - v) for u, v in zip(lo, mo)))
        eq = sum(1 for dm, dob in diffs if dm == 0.0)
        mob = sum(dob for _, dob in diffs) / len(diffs)
        check("B.7 control vs LIVE modules/social_contest/roll.py::roll (same key, same record)", eq == len(diffs),
              f"{eq}/200 equal margins; mean ob(model) - ob(live) = {mob:+.3f}; live roll consumed up to {nonce} "
              f"rng calls per speech (d10 faces) vs the model's 1 normal; max |band_odds diff| = "
              f"{max(odds_diffs):.3f}")
    except Exception as exc:  # pragma: no cover
        check("B.7 control vs LIVE roll.py::roll", False, f"could not call: {exc!r}")

    # ---------------- B24p.11 control; B24p.12 control
    inp = tell_input(S)
    rng = draw(9, "a", "c")
    o = P.proceed(inp, rng, decide=None)
    r2 = draw(9, "a", "c")
    st0 = P._start(inp)
    rd = P._read(inp, 0, st0, r2)
    ch = P._auto(inp, st0, 0, rd, [0])
    on = P._hold(inp, 0, st0.sides[0], P._move_by_id(inp, ch.move), r2)
    x, _, _, _ = speech(inp, ch.ground, on_topic=on)
    m2 = roll(x, r2)
    check("B24p.11 control: one speaker, one exchange, decide=None: verdict == _speech's margin",
          o.verdicts[0][1] == m2 and len(o.verdicts) == 1, f"{o.verdicts[0][1]} vs {m2}")
    calls = []
    o = P.proceed(inp, draw(10), decide=lambda v: calls.append(1) or Choice("argue", "evidence"))
    check("B24p.11: abridged form never asks `decide`... (the plan passes decide=None; with a callable it IS asked)",
          len(calls) == 1, f"asked {len(calls)}x; the module asks any `decide` it is handed; the 'never asked' test holds only because the host passes"
                " None (G40)")
    D0 = dialmod.controls()
    full = build_input(default_people(), "legal_trial", "full", actor="a", addressed="b", bench=("j1", "j2", "j3"),
                       present=(), dials=D0, effort=2)
    o = P.proceed(full, draw(11))
    d = sorted(full.deciders, key=lambda d: d.id)[0]
    x, _ = P._ballot_input(full, o.state, d, o.ended, None, o.exchanges, [None] * len(o.exchanges),
                           [0.0] * len(o.exchanges), 1.0, False)
    rec = replace(x, leverage=d.lean + level(d.modifier) - D0["resist_step"] * (d.will - mid))
    check("B24p.12 control: track_step 0, end levels None: ballot record == the decider's own record",
          x == rec, f"{x.leverage} vs {rec.leverage}")

    # ---------------- room kinds (RD C.5 / B24p.13)
    ppl = {"a": person("a"), "b": person("b"), "j": {**person("j"), "seat": {"rung": "duchy", "faction": "Crown"}}}
    k1 = build_input(ppl, "conversation", "full", actor="a", addressed="b", dials=S).room.audience
    k2 = build_input(ppl, "conversation", "abridged", actor="a", addressed="b", dials=S).room.audience
    k3 = build_input(ppl, "legal_trial", "abridged", actor="a", addressed=None, bench=("j",), dials=S)
    check("C.5: full conversation and abridged tell read `none`; abridged speak under legal_trial `bench`",
          (k1, k2, k3.room.audience) == ("none", "none", "bench") and k3.deciders[0].id == "j",
          f"{k1}, {k2}, {k3.room.audience}, addressed {k3.deciders[0].id}")

    # ---------------- B.1 controls; B.3 (i); press_at basis (B24p.11)
    Dz = dialmod.shipped(audience_room={k: {"attention": 0.0, "distraction": 0.0, "proof_weight": 0.5}
                                        for k in data.AUDIENCE_KINDS_SHIPPED})
    same = True
    for k in range(200):
        m = [P.proceed(tell_input(Dz, a=person("a", focus=f)), draw(("b1", k))).exchanges[0].margin for f in (2, 6)]
        same &= m[0] == m[1]
    check("B.1 control: pull 0, distraction 0: Focus 2 and 6 give identical margins", same)
    same = True
    for k in range(200):
        xs = [P.proceed(tell_input(S, a=person("a", attunement=t)), draw(("b3", k)),
                        decide=lambda v: Choice("argue", "evidence")).exchanges[0].margin for t in (2, 6)]
        same &= xs[0] == xs[1]
    check("B.3(i) ground forced: Attunement 2 and 6 give identical margins", same)
    pool_mid = pool_of(mid, 0, S["pool_add"], S["pool_floor"])
    q = 1 - p_at_least(pool_mid, 0.4 * S["pool_add"] + 0.0 + S["blow_gain"] * (S["press_base"] + 1) * 1.0)
    check("B24p.11: '1 - steady_odds at least 0.406 at zero strain'", abs(q - 0.406) < 5e-4, f"{q:.4f}")
    read("B.3 read_ob: 'an Attunement at the population's middle reads at even odds'",
         f"P(read >= 0) at Attunement 4, guard at mid = {p_at_least(pool_mid, 0.4 * 6 + 1.4):.3f}")
    read("B.9 ploy_ob: 'a mid Attunement sees at about even odds'",
         f"P(seen) = {p_at_least(pool_mid, 0.4 * 6 + 1.4):.3f}")
    read("A.5 track_step: 'a fully carried track reads 0.9 sigma'", f"{S['track_step'] * S['track_clip']:.2f}")

    # ---------------- every end reachable; never a verdict
    planted_end = {}
    for k in range(400):
        for row, kw in (("conversation", {}), ("legal_trial", {"bench": ("j1", "j2", "j3")})):
            inp = build_input(default_people(k), row, "full", actor="a", addressed="b", dials=S, effort=4, **kw)
            o = P.proceed(inp, draw(("end", k, row)))
            planted_end.setdefault(o.ended, 0)
            planted_end[o.ended] += 1
    inp = build_input({"a": person("a", focus=1), "b": person("b")}, "conversation", "full", actor="a",
                      addressed="b", dials=S, effort=4)
    inp = replace(inp, type=replace(inp.type, strikes=1, struck_ends=True),
                  room=replace(inp.room, distraction=6.0))
    o = P.proceed(inp, draw(12))
    planted_end["struck(planted)"] = int(o.ended == "struck")
    read("A.5 ends reached by automatic sittings (400 keys x conversation + legal_trial, effort 4)",
         f"{planted_end}")
    check("A.5 struck end reachable with struck_ends=True, strikes=1", o.ended == "struck", o.ended)

    # ---------------- statistical falsifiers (n keys)
    def share(fn, n):
        return sum(1 for k in range(n) if fn(k)) / n
    pull = dialmod.shipped(audience_room={k: {"attention": 0.0, "distraction": 1.0, "proof_weight": 0.5}
                                          for k in data.AUDIENCE_KINDS_SHIPPED})
    s2 = share(lambda k: P.proceed(tell_input(pull, a=person("a", focus=2)), draw(("f", k))).exchanges[0].on_topic, n)
    s6 = share(lambda k: P.proceed(tell_input(pull, a=person("a", focus=6)), draw(("f", k))).exchanges[0].on_topic, n)
    check(f"B.1 share on topic higher at Focus 6 by >= 4 SE (pull 1.0, n={n})", s6 - s2 >= 4 * se_diff(s2, s6, n),
          f"{s2:.3f} -> {s6:.3f}")
    peaked = {**person("b", reason=7, attunement=1), "pursuits": {}, "convictions": {}}

    def chose_ev(att, grace=4):
        def f(k):
            b = {**peaked, "attributes": {**peaked["attributes"], "grace": grace}}
            return P.proceed(tell_input(S, a=person("a", attunement=att), b=b), draw(("a", k))).exchanges[0].ground \
                == "evidence"
        return f
    a2, a6 = share(chose_ev(2), n), share(chose_ev(6), n)
    check(f"B.3(ii) share choosing the peaked ground higher at Attunement 6 by >= 4 SE (n={n})",
          a6 - a2 >= 4 * se_diff(a2, a6, n), f"{a2:.3f} -> {a6:.3f}")
    g2, g6 = share(chose_ev(6, 2), n), share(chose_ev(6, 6), n)
    check(f"B.3(iii) target Grace 2 -> 6: the share is lower at 6 (n={n})", g6 < g2, f"{g2:.3f} -> {g6:.3f}")

    def marked(will):
        def f(k):
            inp = build_input({"a": person("a"), "b": person("b", will=will)}, "questioning", "full", actor="a",
                              addressed="b", dials=S, effort=1)
            rng = draw(("w", k))
            st = P._start(inp)
            P._read(inp, 0, st, rng)
            T, j = P._target(inp, 0)
            # a scripted presser landing a blow of 1.5 (B.6(i)): steadiness draw against strain 0 + blow 1.5
            stdy = P.roll_net_continuous(P._P(S, inp.speakers[j].will), rng=rng) - (P._even(S) + 0.0 + 1.5)
            return stdy < 0
        return f
    m2_, m6_ = share(marked(2), n), share(marked(6), n)
    check(f"B.6(i) share marked lower at Will 6 by >= 4 SE (blow 1.5, n={n})", m2_ - m6_ >= 4 * se_diff(m2_, m6_, n),
          f"{m2_:.3f} -> {m6_:.3f}")
    # B.6(ii) second half: under a decider that always argues the Will 2 side rests (spends resolve) first
    first_w2 = 0
    for k in range(200):
        inp = build_input({"a": person("a", will=2), "b": person("b", will=6)}, "conversation", "full", actor="a",
                          addressed="b", dials=S, effort=20)
        inp = replace(inp, type=replace(inp.type, exchanges=(1, 20)))
        o = P.proceed(inp, draw(("r", k)), decide=lambda v: Choice("argue", "evidence") if "argue" in v.legal
                      else Choice("rest", None))
        first_w2 += int(o.state.sides[0].resolve <= 0 < o.state.sides[1].resolve)
    check("B.6(ii) a decider that always argues: the Will 2 side's resolve is spent first in every sitting",
          first_w2 == 200, f"{first_w2}/200")
    # automatic sittings: relevance/sincerity read 0 (B.9 'by construction'); _auto never diverts
    nz, div = 0, 0
    for k in range(300):
        inp = build_input(default_people(k), "arbitration", "full", actor="a", addressed="b",
                          bench=("j1", "j2", "j3"), dials=S, effort=3)
        o = P.proceed(inp, draw(("auto", k)))
        div += sum(1 for x in o.exchanges if x.move == "divert")
        for _, levs in o.ballot_levels:
            dl = dict(levs)
            nz += int(dl["relevance"] != 0.0 or dl["sincerity"] != 0.0)
    check("B.9: in automatic sittings relevance and sincerity read 0 and _auto never diverts", nz == 0 and div == 0,
          f"nonzero ballots {nz}, diverts {div}")

    # ---------------- C.6 item 3: every case row nameable?
    from scmodel.host import row_for_case
    named = {row_for_case({"faction": f, "rung": r}, m, b) for f in ("Crown", "Church", "Guild", "Other")
             for r in data.RUNG_KINDS for m in ("person", "proposition", "record") for b in (1, 3)}
    dead = [rid for _, rid in data.CASE_ROWS if rid not in named]
    check("C.6: every case_rows row can be named by row_for_case", not dead,
          f"never named: {dead} (named: {sorted(named)})")
    q = build_input(default_people(), "excommunication_deliberation", "full", actor="a", addressed="b",
                    bench=("j1", "j2", "j3"), dials=S)
    check("C.3/B24p.14: a declared row's quorum can be met by its filtered bench",
          len(q.deciders) >= (q.type.quorum or 0), f"quorum {q.type.quorum}, church seats {len(q.deciders)}")

    # ---------------- report
    w = max(len(r[0]) for r in RESULTS)
    fails = 0
    for name, verdict, detail in RESULTS:
        fails += verdict == "FAIL"
        print(f"{verdict:4}  {name:<{w}}  {detail}")
    print(f"\n{sum(1 for r in RESULTS if r[1] == 'PASS')} PASS, {fails} FAIL, "
          f"{sum(1 for r in RESULTS if r[1] == 'READ')} READ")
    return fails


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--n", type=int, default=4000)
    sys.exit(main(ap.parse_args().n))
