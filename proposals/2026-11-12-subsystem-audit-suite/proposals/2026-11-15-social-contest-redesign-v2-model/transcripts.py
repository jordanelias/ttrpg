"""Rendered transcripts: SEED 0 of each rite (not selected), with the card.  PYTHONHASHSEED=0 python transcripts.py"""
from sc2 import host, fixtures as F
from sc2.lab import *
cast, T = F.cast(), F.TOLLS
FL = ("guildsmen", "toll_men", "clerk")
def show(rite, m, **kw):
    inp, card, out, b = sit(cast, rite, m, ("tr", 0), effort=3, **kw)
    print(f"CARD {card.kind} | {card.genre} | a {card.live} borne by `{card.bears}` | reply {dict(card.reply)} | issues {card.issues} | silence: {card.silence} | standard {card.standard} | Reason's share by ground {dict(card.reason_weight)}")
    print(f"     arranged by {card.arranged_by} (tilt {card.tilt}) | stake {card.stake} | room {card.room} | barred {card.barred} | admits {card.admits} | close {card.close} by {card.decided_by or 'accept'} | {card.turns} turns | odds before an unmoved bench {card.odds}")
    print(host.render(inp, card, out))
    print(f"  => band {b[0]}; verdicts {[(i, round(v.net - v.ob, 2)) for i, v in out.verdicts]}; rattles {[(i, c.rattles) for i, c in out.state.cond if c.rattles]}\n")
show("trial", dict(T, parties={"for": "scholar", "against": "diplomat"}), bench=CB, floor=FL)
show("negotiation", dict(id="grain", parties={"for": "orator", "against": "diplomat"}, bears={"grain": 1.0, "trade": 0.5}))
show("rally", dict(T, parties={"for": "orator"}), floor=("guildsmen", "toll_men", "townsfolk"))
show("debate", dict(T, id="remit", parties={"for": "orator", "against": "diplomat"}), bench=CB, floor=("guildsmen",))
show("questioning", dict(T, id="who_took_the_tolls", parties={"for": "fox", "against": "bully"}))
