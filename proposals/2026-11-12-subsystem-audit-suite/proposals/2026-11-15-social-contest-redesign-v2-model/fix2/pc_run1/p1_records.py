"""P1.8: continuity of the beat record, by my own invariants, over n sittings per type; and raw beats for play-back."""
import sys
from collections import Counter, defaultdict
from common import *

cast = F.cast()
N = int(sys.argv[1]) if len(sys.argv) > 1 else 200
SHOW = int(sys.argv[2]) if len(sys.argv) > 2 else 3


def check(inp, out):
    c = Counter()
    rite = inp.rite
    reply = dict(rite.reply)
    pts = {p.id: p for p in out.state.points}
    live = {"for": None, "against": None}
    held = {}            # pid -> {h: signed d}
    last_voice = {"for": None, "against": None}
    judge = next((p.id for p in sorted(inp.room, key=lambda p: (-p.precedence, p.id)) if p.decides), None)
    for b in out.beats:
        other = "against" if b.side == "for" else "for"
        lt = live[other]
        stands = lt is not None and SIGN[other] * sum(held[lt].values()) > 1e-9
        c["beats"] += 1
        c["move:" + b.move] += 1
        if b.move == "argue":
            if b.point is None:
                c["VIOL argue names no point"] += 1
            if b.relation == "answers":
                c["answers"] += 1
                if b.point != lt:
                    c["VIOL answer not to the other side's live point"] += 1
                if pts[b.point].side != other:
                    c["VIOL answer to own side's point"] += 1
                if not stands:
                    c["answer to a point that no longer stands"] += 1
                seen = set()
                for hid, d in b.moved:
                    if hid not in seen and b.point in held:
                        seen.add(hid); held[b.point][hid] = held[b.point].get(hid, 0.0) + d
            else:
                c["raises"] += 1
                if live[b.side] is not None and SIGN[b.side] * sum(held[live[b.side]].values()) > 1e-9:
                    c["raise buries own standing point (it can no longer be answered)"] += 1
                hd, seen = {}, set()
                for hid, d in b.moved:
                    if hid not in seen:
                        seen.add(hid); hd[hid] = d
                held[b.point] = hd
                live[b.side] = b.point
        if b.move == "press":
            if b.target != (last_voice[other] or b.target):
                c["VIOL press target not other's last voice"] += 1
        # a beat that leaves a standing opposing point unanswered
        if stands and b.relation not in ("answers", "concedes"):
            c["ignores a standing point"] += 1
            if b.evaded:
                c["  ...charged (evaded)"] += 1
            else:
                c["  ...NOT charged (reply %s, silence %s)" % (reply.get(b.side, "may"), rite.silence)] += 1
        if b.move == "concede":
            c["concede by " + b.side + (" (yield)" if out.ended == "yielded" and b is out.beats[-1] else " (descends)")] += 1
            if not (out.ended == "yielded" and b is out.beats[-1]):
                live = {"for": None, "against": None}
                if judge:
                    before = None
                    # track of the presiding judge before/after this beat, from moved
                    for hid, d in b.moved:
                        if hid == judge:
                            c["  concede shift at judge toward conceder (sum)"] += round(-SIGN[b.side] * d * -1, 3) * 0  # placeholder
                    c["  concede moves judge (n)"] += 1
        if b.move in ("argue", "press"):
            last_voice[b.side] = b.voice
    return c


def tracks_at(inp, out):
    T = {p.id: p.start for p in inp.room}
    seq = []
    for b in out.beats:
        for hid, d in b.moved:
            T[hid] += d
        seq.append(dict(T))
    return seq


if __name__ == "__main__":
    for rite, (m, kw) in scenes().items():
        tot = Counter(); ends = Counter(); bands = Counter(); concede_shift = []
        for i in range(N):
            inp, card, out, band = run(cast, rite, m, ("pc1", i), **kw)
            tot += check(inp, out); ends[out.ended] += 1; bands[band[0]] += 1
            # concession: the presiding judge's track just before and after a descending concession, signed toward the conceder
            judge = next((p.id for p in sorted(inp.room, key=lambda p: (-p.precedence, p.id)) if p.decides), None)
            seq = tracks_at(inp, out)
            for k, b in enumerate(out.beats):
                if b.move == "concede" and b.issue != inp.rite.issues[-1] and judge and inp.rite.concede == "descends":
                    pre = seq[k - 1][judge] if k else [p.start for p in inp.room if p.id == judge][0]
                    concede_shift.append((b.side, round(SIGN[b.side] * pre, 2), round(SIGN[b.side] * seq[k][judge], 2)))
        print(f"\n=== {rite}: n={N} ends={dict(ends)} bands={dict(bands)}")
        for k in sorted(tot):
            print(f"   {k}: {tot[k]}")
        if concede_shift:
            bys = Counter(s for s, _, _ in concede_shift)
            gain = [post - pre for _, pre, post in concede_shift]
            print(f"   descending concessions: by side {dict(bys)}; judge track toward conceder pre->post mean "
                  f"{sum(p for _, p, _ in concede_shift)/len(concede_shift):+.2f} -> {sum(q for _, _, q in concede_shift)/len(concede_shift):+.2f}; "
                  f"share where conceding IMPROVED conceder's standing {sum(g > 0 for g in gain)/len(gain):.2f}")
    if SHOW:
        for rite, (m, kw) in scenes().items():
            for i in range(SHOW):
                inp, card, out, band = run(cast, rite, m, ("pc1", i), **kw)
                print(f"\n--- {rite} seed {i}: room {[(p.id, p.side, p.decides) for p in inp.room]} turns {inp.rite.turns} issues {inp.rite.issues}")
                for b in out.beats:
                    print(f"  {b.n}. {b.mover}{'' if b.voice == b.mover else '(voice ' + b.voice + ')'} [{b.side}] {b.move}/{b.relation} issue={b.issue} "
                          f"ground={b.ground} item={b.item} point={b.point} target={b.target} m={b.margin} drift={b.drift} "
                          f"evaded={b.evaded} insinc={b.insincere} rattled={b.rattled} broke={b.broke} closed={b.closed} mood={b.mood}")
                print(f"  -> ended {out.ended} by {out.ended_by}; band {band[0]} margin {None if band[1] is None else round(band[1], 2)}; "
                      f"verdicts {[(i_, round(v.net - v.ob, 2)) for i_, v in out.verdicts]}; points {[(p.id, p.side, p.ground, p.by) for p in out.state.points]}")
