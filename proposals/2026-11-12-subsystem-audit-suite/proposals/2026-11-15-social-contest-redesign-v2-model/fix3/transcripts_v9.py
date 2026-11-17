import os, sys; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
"""Rendered transcripts after the second fix pass: SEED 0 of each rite (not selected), with the card.
PYTHONHASHSEED=0 python transcripts_v8.py  (output transcripts_v8_out.txt; after the stress-test fixes, fix3/transcripts_v9_out.txt)"""
from sc2 import host, fixtures as F
from sc2.lab import *
cast, T = F.cast(), F.TOLLS
FL = ("guildsmen", "toll_men", "clerk")
def show(rite, m, **kw):
    inp, card, out, b = sit(cast, rite, m, ("tr", 0), effort=kw.pop("effort", 3), **kw)
    print(f"CARD {card.kind} | {card.genre} | {'an' if card.live[0] in 'aeiou' else 'a'} {card.live} borne by `{card.bears}` | reply {dict(card.reply)} | issues {card.issues} | silence: {card.silence} | unargued: {card.unargued} | standard {card.standard}")
    print(f"     arranged by {card.arranged_by or 'custom'} (tilt {card.tilt}) | stake {card.stake} | room {card.room} | barred {card.barred} | close {card.close} by {card.decided_by or 'accept'} | {card.turns} turns | ends {card.ends} | odds if nobody speaks {card.odds}")
    print(host.render(inp, card, out))
    w = host.new_world(); band, wr = host.fold(w, cast, inp, card, out, m)
    lab = lambda x: "for" if x >= 1 else "half" if x >= 0 else "against"
    wt = {p.id: p.weight for p in inp.room}
    moot = out.ended == "yielded" and host.act_band(inp, out)[1] is None
    vs = "; ".join(f"{i} {lab(v.net - v.ob)} ({v.net - v.ob:+.1f}{', weight ' + str(wt[i]) if wt[i] > 1 else ''})" for i, v in out.verdicts)
    print(f"  => band {band}; the close: {vs or 'no draw'}{' (moot: the yield decided)' if moot and vs else ''}; rattles {[(i, c.rattles) for i, c in out.state.cond if c.rattles]}")
    print(f"  => the world: {sorted({x[0] for x in wr})}; legitimacy {({f: round(v, 2) for f, v in w['legitimacy'].items()})}" + "".join(f"; {j}'s ruling received {r:.2f} ({'a brute\'s' if r < 1 else 'gracefully'}, {'wrong by the merits' if wr_ else 'right by the merits'})" for j, r, wr_ in w["reception"]) + "".join(f"; partial: {x[1]} ruled his own way and pays" for x in wr if x[0] == "partial_paid") + "\n")
show("trial", dict(T, parties={"for": "scholar", "against": "diplomat"}), bench=CB, floor=FL)
show("negotiation", dict(id="grain", parties={"for": "orator", "against": "diplomat"}, bears={"grain": 1.0, "trade": 0.5}))
show("rally", dict(T, parties={"for": "orator"}), floor=("guildsmen", "toll_men", "townsfolk"))
show("debate", dict(T, id="remit", parties={"for": "orator", "against": "diplomat"}), bench=CB, floor=("guildsmen",))
show("questioning", dict(T, id="who_took_the_tolls", parties={"for": "fox", "against": "bully"}))
show("inquisition", dict(T, id="heresy", parties={"for": "bishop", "against": "scholar"}), bench=("bishop", "prior"))
show("audience", dict(T, id="plea", parties={"for": "scholar"}), bench=("judge",))
show("trial", dict(T, id="rigged", parties={"for": "scholar", "against": "bully"}), bench=CB, floor=FL, arranger="bully", rig=1.0)
show("conversation", dict(T, id="word", parties={"for": "orator", "against": "diplomat"}), form="abridged", effort=0)
