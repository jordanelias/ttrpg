"""(fix3 copy of the transcript audit's scratch script; SC2=before runs the model as the stress test found it.) Narrative-logic audit of machine transcripts at scale. Run from model dir: PYTHONHASHSEED=0 python -B ../sc_audit/corpus.py [n]"""
import sys, os, random, collections
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if os.environ.get("SC2") == "before":
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "before"))
from sc2 import host, fixtures as F
from sc2.lab import *
N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
cast, T = F.cast(), F.TOLLS
SP = ["orator", "scholar", "bully", "diplomat", "fox", "bishop"]
FL = ("guildsmen", "toll_men", "clerk")
SPEC = {   # rite -> kwargs (as transcripts_v8)
 "trial": dict(bench=CB, floor=FL), "negotiation": dict(), "rally": dict(floor=("guildsmen","toll_men","townsfolk")),
 "debate": dict(bench=CB, floor=("guildsmen",)), "questioning": dict(), "inquisition": dict(bench=("bishop","prior")),
 "audience": dict(bench=("judge",)), "conversation": dict(form="abridged", effort=0)}
ONE = {"rally": 1, "audience": 1, "conversation": 2}
M = collections.defaultdict(collections.Counter)
def pairs(rng, rite):
    a, b = rng.sample(SP, 2)
    return {"for": a} if rite in ("rally", "audience") else {"for": a, "against": b}
for rite, kw in SPEC.items():
    rng = random.Random(rite)
    for i in range(N):
        pr = pairs(rng, rite)
        m = dict(T, id=f"{rite}{i}", parties=pr)
        kk = dict(kw); eff = kk.pop("effort", 3)
        try:
            inp, card, out, band = sit(cast, rite, m, ("au", rite, i), effort=eff, **kk)
        except Exception as e:
            M[rite]["refused/crash:" + type(e).__name__] += 1; continue
        c = M[rite]; c["n"] += 1
        beats = out.beats; c["beats"] += len(beats)
        pts = {p.id: p for p in out.state.points}
        # A press before any point stands
        seen = 0; first = next((b for b in beats if b.move != "rest"), None)
        raised = set()
        for b in beats:
            if b.move == "argue" and b.relation != "answers": raised.add(b.point)
            if b.move == "press" and not raised and card.live != "charge":
                c["press_nothing_said"] += 1; break
        if first and first.move == "press" and card.live != "charge": c["opens_with_press"] += 1
        # same point answered >=3
        ans = collections.Counter(b.point for b in beats if b.move == "argue" and b.relation == "answers")
        if any(v >= 3 for v in ans.values()): c["point_answered_3x"] += 1
        # dead beats: no change in room
        prev = 0.0; dead = 0
        for b in beats:
            if abs(b.mood - prev) < 0.005 and abs(b.mood) >= 0.995: dead += 1
            prev = b.mood
        c["dead_beats"] += dead
        if any(abs(b.mood) >= 0.995 for b in beats[:max(1, len(beats)//2)]): c["room_saturated_by_half"] += 1
        # referentless: ground with no frame, no item
        sp = [b for b in beats if b.move in ("argue", "press")]
        c["speech_beats"] += len(sp)
        c["referentless"] += sum(1 for b in sp if not b.frame and not b.item)
        c["solidarity_ref0"] += sum(1 for b in sp if b.ground == "solidarity" and not b.frame and not b.item)
        c["proof_no_item"] += sum(1 for b in sp if b.ground == "evidence" and not b.item)
        # mismatched answer that lands
        for b in beats:
            if b.move == "argue" and b.relation == "answers" and b.point in pts:
                pg = pts[b.point].ground; c["answers"] += 1
                if b.ground != pg:
                    c["answer_ground_mismatch"] += 1
                    if b.margin >= 1: c["mismatch_lands"] += 1
                    if pg == "evidence" and b.ground == "solidarity" and b.margin >= 1: c["proof_beaten_by_solidarity"] += 1
        # endings
        c["end:" + str(out.ended)] += 1
        if beats and beats[-1].move == "press": c["ends_on_press"] += 1
        # verdict vs band
        vs = [v.net - v.ob for _, v in out.verdicts]
        if len(vs) >= 2 and out.ended != "yielded":
            maj = sum(1 for x in vs if x > 0) > len(vs) / 2
            carried = band[0] in CARRIED
            c["multi_verdict"] += 1
            if maj != carried: c["verdict_band_contradiction"] += 1
        if len(vs) >= 2 and out.ended == "yielded": c["yield_decides_multi"] += 1
        # fold
        w = host.new_world(); band2, wr = host.fold(w, cast, inp, card, out, m)
        kinds = {x[0] for x in wr}
        pj = [x[1] for x in wr if x[0] == "partial_paid"]
        if pj:
            c["partial_paid"] += 1
            for j in pj:
                p = cast[j]; f, g = pr.get("for"), pr.get("against")
                ties = [abs(host.tie(p, q, cast)) for q in (f, g) if q]
                fac = any(cast[q].get("faction") and cast[q].get("faction") == p.get("faction") for q in (f, g) if q)
                if max(ties or [0]) == 0 and not fac: c["partial_by_conviction_only"] += 1
        if band[0] in ("failure",) and ("legitimacy-" in kinds): c["failure_costs_legitimacy"] += 1
        if band[0] in ("failure",) and ("record:acquittal" in kinds or "record:defeated" in kinds): c["failure_record"] += 1
        # abridged / negotiation terms
        if rite == "negotiation" and not any(b.terms for b in beats): c["negotiation_no_terms"] += 1
print(f"n per rite = {N}")
for rite, c in M.items():
    n = c["n"] or 1; sb = c["speech_beats"] or 1
    print(f"\n== {rite}: sittings {c['n']}, beats/sitting {c['beats']/n:.1f}, refused/crash {sum(v for k,v in c.items() if k.startswith('refused'))}")
    print(f"   opens with a press on a standing nothing: {c['opens_with_press']/n:.0%}; a press before any point was raised: {c['press_nothing_said']/n:.0%}")
    print(f"   one point answered 3+ times: {c['point_answered_3x']/n:.0%}; ends on a press: {c['ends_on_press']/n:.0%}; endings { {k[4:]:v for k,v in c.items() if k.startswith('end:')} }")
    print(f"   room pinned at +-1 by half-time: {c['room_saturated_by_half']/n:.0%}; dead beats (no visible effect) per sitting: {c['dead_beats']/n:.2f}")
    print(f"   speech beats with NO referent (no frame, no item): {c['referentless']/sb:.0%}; of which 'as one of their own' with no referent: {c['solidarity_ref0']/sb:.0%}; 'on the proof' with nothing cited: {c['proof_no_item']/sb:.0%}")
    a = c["answers"] or 1
    print(f"   answers: {c['answers']}; answered from a different ground than the point: {c['answer_ground_mismatch']/a:.0%}; such an answer LANDS: {c['mismatch_lands']/a:.0%}; a proof beaten by solidarity: {c['proof_beaten_by_solidarity']/a:.0%}")
    if c["multi_verdict"] or c["yield_decides_multi"]:
        print(f"   multi-seat verdict contradicts band: {c['verdict_band_contradiction']}/{c['multi_verdict']}; sittings a yield decided over the seats' own verdicts: {c['yield_decides_multi']}")
    print(f"   judge 'partial' paid: {c['partial_paid']/n:.0%}; of those, with no tie and no shared faction (conviction only): {c['partial_by_conviction_only']}; failure that costs legitimacy: {c['failure_costs_legitimacy']}/{c['failure_record']}")
    if rite == "negotiation": print(f"   negotiation sittings in which no beat carries any term: {c['negotiation_no_terms']/n:.0%}")
