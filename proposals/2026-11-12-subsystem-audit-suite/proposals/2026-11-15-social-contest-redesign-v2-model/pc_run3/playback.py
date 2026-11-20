"""STEP 6: a Grace-1 and a Grace-7 accuser make the same argument at a formal trial (standard 5); same seed; both sides
scripted (a argues on consequence; b argues on consequence). Print the beat records only."""
from common import *
from sc2 import engine as E
def argcons(v, me):
    os_ = [o for o in v.options if o.move == "argue" and o.ground == "consequence"] or [o for o in v.options if o.move == "argue"] or list(v.options)
    o = sorted(os_, key=lambda o: (o.relation != "answers",))[0]
    return Choice(o.move, o.ground, o.item, o.relation)
for seed in (3,):
    for g in (1, 7):
        pp = blank(); pp["a"]["attributes"]["grace"] = g
        inp, card, out, b = sit(pp, "trial", mat("blank"), ("pb", seed), deciders={"a": argcons, "b": argcons}, effort=2)
        print(f"== Grace {g}  card: {card.kind}, standard {card.standard}, decided by {card.decided_by}, turns {card.turns}")
        for bt in out.beats:
            print(f"  {bt.n} {bt.mover} {bt.move} {bt.relation} ground={bt.ground} pt={bt.point} margin={bt.margin:+.2f} esteem={bt.esteem:+.1f} rel={bt.relevance} heard={bt.heard} drift={bt.drift} evaded={bt.evaded} broke={bt.broke} rattled={bt.rattled} moved={[(h, round(x,2)) for h, x in bt.moved]} mood={bt.mood:+.2f}")
        print(f"  ended {out.ended}; verdicts {[(d, round(v.net - v.ob, 2)) for d, v in out.verdicts]}; band {b[0]}; j1 track {dict(out.state.tracks)['j1']:+.2f}")
        print(host.render(inp, card, out))
