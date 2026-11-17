import os, sys; sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
"""Rendered transcripts after the second fix pass: SEED 0 of each rite (not selected), with the card.
PYTHONHASHSEED=0 python transcripts_v8.py  (output transcripts_v8_out.txt; after the stress-test fixes, fix3/transcripts_v9_out.txt)"""
from sc2 import host, fixtures as F
from sc2.lab import *
cast, T = F.cast(), F.TOLLS
FL = ("guildsmen", "toll_men", "clerk")
def show(rite, m, **kw):
    inp, card, out, b = sit(cast, rite, m, ("tr", 0), effort=kw.pop("effort", 3), **kw)
    print(f"CARD {card.kind} | {card.genre} | a {card.live} borne by `{card.bears}` | reply {dict(card.reply)} | issues {card.issues} | silence: {card.silence} | unargued: {card.unargued} | standard {card.standard}")
    print(f"     arranged by {card.arranged_by or 'custom'} (tilt {card.tilt}) | stake {card.stake} | room {card.room} | barred {card.barred} | close {card.close} by {card.decided_by or 'accept'} | {card.turns} turns | ends {card.ends} | odds if nobody speaks {card.odds}")
    print(host.render(inp, card, out))
    w = host.new_world(); band, wr = host.fold(w, cast, inp, card, out, m)
    print(f"  => band {band}; verdicts {[(i, round(v.net - v.ob, 2)) for i, v in out.verdicts]}; rattles {[(i, c.rattles) for i, c in out.state.cond if c.rattles]}")
    print(f"  => the world: {sorted({x[0] for x in wr})}\n")
show("trial", dict(T, parties={"for": "scholar", "against": "diplomat"}), bench=CB, floor=FL)
show("negotiation", dict(id="grain", parties={"for": "orator", "against": "diplomat"}, bears={"grain": 1.0, "trade": 0.5}))
show("rally", dict(T, parties={"for": "orator"}), floor=("guildsmen", "toll_men", "townsfolk"))
show("debate", dict(T, id="remit", parties={"for": "orator", "against": "diplomat"}), bench=CB, floor=("guildsmen",))
show("questioning", dict(T, id="who_took_the_tolls", parties={"for": "fox", "against": "bully"}))
show("inquisition", dict(T, id="heresy", parties={"for": "bishop", "against": "scholar"}), bench=("bishop", "prior"))
show("audience", dict(T, id="plea", parties={"for": "scholar"}), bench=("judge",))
show("trial", dict(T, id="rigged", parties={"for": "scholar", "against": "bully"}), bench=CB, floor=FL, arranger="bully", rig=1.0)
show("conversation", dict(T, id="word", parties={"for": "orator", "against": "diplomat"}), form="abridged", effort=0)
