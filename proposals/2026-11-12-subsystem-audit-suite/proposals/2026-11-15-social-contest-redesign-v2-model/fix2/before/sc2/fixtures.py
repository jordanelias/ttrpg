"""Toy persons and matters for the v2 checks."""
import copy
from .engine import Item

def P(pid, rank=1, weight=1, office=None, faction=None, items=(), layers=None, **attrs):
    a = {k: 4 for k in ("focus", "reason", "attunement", "presence", "grace", "will")}
    a.update(attrs)
    return dict(id=pid, attributes=a, rank=rank, weight=weight, office=office, faction=faction, items=tuple(items),
                layers=layers or {})

def seat(rung, faction, modifier=None, duty=None):
    return dict(rung=rung, faction=faction, modifier=modifier, duty=duty or {})

def mid_people():
    """all-mid, flat interiors: the control cast (the stress test's base_people)."""
    pp = {"a": P("a"), "b": P("b"), "crowd": P("crowd", weight=30)}
    for j in ("j1", "j2", "j3"):
        pp[j] = P(j, office=seat(3, "Crown"))
    for j in ("c1", "c2", "c3"):
        pp[j] = P(j, office=seat(2, "Church"))
    return pp

def matter(mid="m", f="a", ag="b", **kw):
    d = dict(id=mid, parties={"for": f, "against": ag}, bears={})
    d.update(kw)
    return d

def cast():
    """a characterful cast: an orator, a scholar, a bully, a diplomat, a fox; a partial judge; a split floor."""
    rec = Item("ledger_of_tolls", "record", 0.9, source="clerk", about="bully")
    tes = Item("clerk_saw_it", "testimony", 0.7, source="clerk", about="bully")
    forged = Item("forged_writ", "record", 0.8, source="fox", about="scholar", sincere=False)
    pp = {
        "orator": P("orator", presence=7, reason=3, grace=5, faction="Guild",
                    layers=dict(pursuits={"trade": 0.8}, convictions={"commons": 3}, relationships={"bully": -0.6})),
        "scholar": P("scholar", reason=7, presence=3, focus=6, faction="Church", items=(rec, tes),
                     layers=dict(pursuits={"learning": 0.6}, convictions={"faith": 5}, patron="bishop")),
        "bully": P("bully", will=7, presence=5, grace=2, attunement=3, office=seat(2, "Crown", "minor"), faction="Crown",
                   layers=dict(pursuits={"tolls": 0.9}, ambitions=("office",), relationships={"scholar": -0.7, "orator": -0.3})),
        "diplomat": P("diplomat", grace=7, attunement=6, will=3, faction="Guild",
                      layers=dict(pursuits={"trade": 0.5}, needs={"grain": 0.0}, relationships={"bully": 0.2, "orator": 0.4})),
        "fox": P("fox", attunement=7, reason=5, grace=5, will=5, items=(forged,),
                 layers=dict(pursuits={"tolls": 0.7}, convictions={"faith": 1})),
        "judge": P("judge", reason=6, focus=6, attunement=5, office=seat(4, "Crown", "moderate"), faction="Crown",
                   layers=dict(convictions={"law": 4})),
        "judge2": P("judge2", reason=4, focus=3, attunement=3, office=seat(3, "Crown"), faction="Crown",
                    layers=dict(patron="bully", convictions={"law": 2})),
        "judge3": P("judge3", reason=5, office=seat(3, "Crown"), faction="Crown", layers=dict(convictions={"law": 3})),
        "bishop": P("bishop", presence=6, will=6, office=seat(4, "Church", "moderate"), faction="Church",
                    layers=dict(convictions={"faith": 5}, clients=("scholar",))),
        "prior": P("prior", office=seat(2, "Church"), faction="Church", layers=dict(convictions={"faith": 4})),
        "clerk": P("clerk", will=3, grace=3, layers=dict(relationships={"bully": -0.2})),
        "guildsmen": P("guildsmen", weight=20, faction="Guild", layers=dict(pursuits={"trade": 0.8}, convictions={"commons": 3})),
        "toll_men": P("toll_men", weight=10, faction="Crown", layers=dict(pursuits={"tolls": 0.8}, relationships={"bully": 0.5})),
        "townsfolk": P("townsfolk", weight=20, layers=dict(needs={"grain": 0.3}, convictions={"faith": 3})),
    }
    return pp

TOLLS = dict(id="tolls", parties={"for": "scholar", "against": "bully"},
             bears={"tolls": -1.0, "trade": 1.0, "law": 0.5, "commons": 0.5, "office": -0.5, "grain": 0.5},
             strife="famine")
