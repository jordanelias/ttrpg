"""STEP 6: the record of a rigged trial and of a rally (seed 0), as a player would see it: card, beats, writes."""
from common import *
cast = F.cast(); T = F.TOLLS
for lab, rite, m, kw in (("RIGGED TRIAL", "trial", T, dict(bench=("judge", "judge2", "judge3"), floor=("guildsmen", "toll_men", "clerk"), arranger="bully", rig=1.0)),
                         ("RALLY", "rally", dict(T, id="rally", parties={"for": "orator", "against": None}), dict(floor=("guildsmen", "townsfolk", "toll_men")))):
    inp, card, out, b = sit(cast, rite, m, ("play", 0), effort=3, **kw)
    w = host.new_world(); band, wr = host.fold(w, cast, inp, card, out, m)
    print(f"===== {lab}: card kind={card.kind} arranged_by={card.arranged_by} tilt={card.tilt} decided_by={card.decided_by} room={card.room} turns={card.turns} silence={card.silence} odds={card.odds}")
    print(host.render(inp, card, out))
    print(f"  band {band} margin {b[1]}")
    print("  writes:", wr)
    print("  ledgers:", {k: v for k, v in w['ledgers'].items() if v})
    print("  legitimacy", w["legitimacy"], "standing", w["standing"], "docket", w["docket"], "strife", w["strife"])
