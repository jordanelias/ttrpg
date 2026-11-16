"""P6.1-3: Jordan's seven -> band -> typed writes, through the toy fold, against a not-held null arm;
hidden writes (world changes no write names); net regard per sitting; determinism."""
import sys
from collections import Counter, defaultdict
from common import *

N = int(sys.argv[1]) if len(sys.argv) > 1 else 300
cast = F.cast()
T = dict(F.TOLLS)
FL = ("guildsmen", "toll_men", "clerk")
CB = ("judge", "judge2", "judge3", "bishop", "prior")
SEVEN = [  # (Jordan's example, row, matter, build kwargs)
    ("heresy trial", "inquisition_hearing", dict(T, id="heresy", parties={"for": "bishop", "against": "scholar"}), dict(bench=CB)),
    ("parliamentary debate", "debate", dict(T, id="remit", parties={"for": "orator", "against": "bully"}), dict(bench=CB, floor=("guildsmen", "townsfolk"))),
    ("private negotiation", "negotiation", dict(id="grain", parties={"for": "diplomat", "against": "bully"}, bears={"grain": 1.0, "tolls": -0.5}, strife="famine"), {}),
    ("rallying a crowd", "rally", dict(T, id="rally", parties={"for": "orator", "against": None}), dict(floor=("guildsmen", "townsfolk", "toll_men"))),
    ("interrogation for information", "questioning", dict(T, id="q", parties={"for": "scholar", "against": "clerk"}), {}),
    ("a trial", "trial", dict(T, id="tolls"), dict(bench=CB, floor=FL)),
    ("abridged (a tell)", "conversation", dict(T, id="tell", parties={"for": "orator", "against": "diplomat"}), dict(form="abridged")),
]
NAMED = {  # world key -> write kinds that name a change there
    "tenures": ("tenure:",), "offices": ("office:stripped",), "case_files": ("case_file:stage", "record:"),
    "regard": ("regard+", "regard-"), "pursuits": ("pursuits+",), "standing": ("faction+", "faction-"),
    "legitimacy": ("legitimacy+", "legitimacy-"), "strife": ("strife",), "precedents": ("precedent",),
    "docket": ("docket:", "grievance"), "rattled": ("strain_carried",), "ledgers": ("claim:converted",),
}
null = host.new_world(); h_null = world_hash(null)
print(f"null arm (not held): world hash {h_null}; n={N} sittings per example; the toy fold of sc2/host.py")
for lab, row, m, kw in SEVEN:
    bands = Counter(); kinds = defaultdict(Counter); empty = Counter(); hidden = Counter(); netreg = defaultdict(list)
    same_band_diff_world = 0; dets = 0
    for i in range(N):
        inp, card, out, b = sit(cast, row, m, ("seven", lab, i), effort=3, **kw)
        w = host.new_world(); band, wr = host.fold(w, cast, inp, card, out, m)
        bands[band] += 1
        k = Counter(x[0] for x in wr)
        kinds[band].update(k.keys())
        substantive = [x for x in wr if x[0] != "case_file:stage"]
        if not substantive: empty[band] += 1
        for key, pref in NAMED.items():
            if w[key] != null[key] and not any(x[0].startswith(p) for x in wr for p in pref):
                hidden[key] += 1
        for key in ("compliance", "reception", "appeal_weight"):
            if key in w: hidden[key + "(no reader)"] += 1
        netreg[band].append(sum(w["regard"].values()))
        if i < 20:   # determinism: same key twice -> same world hash
            inp2, card2, out2, b2 = sit(cast, row, m, ("seven", lab, i), effort=3, **kw)
            w2 = host.new_world(); host.fold(w2, cast, inp2, card2, out2, m)
            dets += world_hash(w2) == world_hash(w)
    print(f"\n== {lab} = `{row}` disposes `{card.stake}`; bands {dict(bands)}; determinism {dets}/20 same-hash")
    for band in sorted(bands, key=lambda x: str(x)):
        nr = netreg[band]
        print(f"   {str(band):12} n={bands[band]:3} | sittings writing nothing but the case-file stage: {empty[band]} | "
              f"net regard/sitting {sum(nr)/len(nr):+.2f} | write kinds: {dict(kinds[band])}")
    print(f"   world changes with NO write naming them (sittings of {N}): {dict(hidden)}")

print("\n== the same Success under each strife: does what is 'at stake' change any write? (trial, the fold's writes for band 'success')")
for strife in host.STRIFE:
    got = None
    for i in range(400):
        inp, card, out, b = sit(cast, "trial", dict(T, id="tolls", strife=None), ("stk", strife, i), effort=3, bench=CB, floor=FL, strife=strife)
        if b[0] == "success":
            w = host.new_world(); band, wr = host.fold(w, cast, inp, card, out, dict(T, id="tolls", strife=None))
            got = sorted({x[0] for x in wr if not x[0].startswith("regard") and x[0] not in ("strain_carried",)}); break
    print(f"   {strife:7} stakes {host.STRIFE[strife]['stakes']}: non-regard write kinds on a success {got}")

print("\n== matter with no strife in the world yet: a famine is created at 1.0 by the first sitting that names it")
w = host.new_world(); inp, card, out, b = sit(cast, "conversation", dict(T, id="c0", parties={"for": "orator", "against": "diplomat"}), ("cr", 0), effort=3)
host.fold(w, cast, inp, card, out, T); print(f"   empty world -> after one conversation on the tolls (matter strife=famine): strife {w['strife']} band {b[0]}")
pp = F.mid_people(); M = F.matter()
inp, card, out, b = sit(pp, "trial", M, ("nofac", 0), bench=("j1",), floor=("crowd",), effort=3, arranger="a", rig=1.0)
pp2 = F.mid_people(); pp2["a"]["office"] = F.seat(4, "Crown")
inp, card, out, b = sit(pp2, "trial", M, ("nofac", 1), bench=("j1", "j2"), floor=("crowd",), effort=3, arranger="a", rig=1.0)
w = host.new_world(); host.fold(w, pp2, inp, card, out, M)
print(f"   an arranger with an office but no faction rigs (tilt {card.tilt}): legitimacy written to {list(w['legitimacy'])}")
