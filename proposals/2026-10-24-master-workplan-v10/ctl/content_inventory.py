"""Content inventory and realised choice surface (observation only).

usage: PYTHONPATH=<repo> python content_inventory.py CTL_DIR OUT.json
Reads `census2_s{0,1,2}.json` in CTL_DIR (the funnel and contested admission refusals) and the tree; writes
what is authored, what reaches `build_realm(0)`, and what the realised choice surface is. No number is typed."""
import sys, os, json, collections
import yaml
from engine.season.harness.populated import build_realm
from engine.season.data import verbs as V
from engine.season.data.verbs import VERB_TABLE
CTL, OUT = sys.argv[1:3]
res = {}

# --- realised choice surface, pooled over the three census runs
tot = collections.defaultdict(collections.Counter); inv = collections.Counter()
for s in ("s0", "s1", "s2"):
    d = json.load(open(os.path.join(CTL, f"census2_{s}.json")))
    for v, c in d["funnel"].items():
        for k, x in c.items():
            if isinstance(x, (int, float)): tot[v][k] += x
    inv.update(d["admission_refusals_not_in_resolved"])
by = collections.defaultdict(collections.Counter)
for v, row in VERB_TABLE.items():
    t = tot.get(v, collections.Counter()); n = sum(t.values()) + inv.get(v, 0); ex = t["made"] + t["both"]
    c = by[str(row.stratum)]
    c["verbs"] += 1; c["verbs_attempted"] += n > 0; c["verbs_executed"] += ex > 0; c["attempts"] += n; c["executed"] += ex
res["strata"] = {k: dict(c) for k, c in by.items()}
ex = collections.Counter({v: t["made"] + t["both"] for v, t in tot.items() if t["made"] + t["both"]})
T = sum(ex.values()); hh = sum((n / T) ** 2 for n in ex.values())
res["executed_acts"] = T; res["executed_verbs"] = len(ex); res["effective_verbs"] = round(1 / hh, 1)
res["top3"] = [[v, n] for v, n in ex.most_common(3)]; res["top3_share"] = round(sum(n for _, n in ex.most_common(3)) / T, 3)

# --- content that reaches build_realm(0)
w = build_realm(0, None); P = list(w.persons.values())
def empty(v): return v is None or (hasattr(v, "__len__") and len(v) == 0) or v == 0
res["persons"] = len(P); res["cohorts"] = sum(1 for p in P if p.weight > 1)
res["person_fields"] = {f: {"non_empty": sum(1 for p in P if not empty(getattr(p, f))),
                            "distinct": len({repr(getattr(p, f)) for p in P if not empty(getattr(p, f))})}
                        for f in ("capability", "pursuits", "conviction", "stance", "scar", "thread_sensitivity")}
res["tenure_kinds_at_build"] = dict(collections.Counter(t.kind for t in (w.tenures.values() if isinstance(w.tenures, dict) else w.tenures)))
res["offices"] = len(w.offices); res["offices_with_upkeep"] = sum(1 for o in w.offices.values() if o.upkeep)
res["office_factions"] = dict(collections.Counter(o.faction for o in w.offices.values()))
res["site_kinds"] = dict(collections.Counter(s.kind for s in w.sites.values()))
res["vocations"] = sorted(V.VOCATIONS); res["verb_capability"] = dict(V.VERB_CAPABILITY)
nz = 0
for ax, row in V.ALIGNMENT.items():
    nz += sum(1 for v, x in row.items() if not v.startswith("deed:") and x not in (None, 0, 0.0))
celled = V.celled_verbs() if callable(V.celled_verbs) else V.celled_verbs
res["alignment"] = {"non_zero_cells": nz, "possible": len(celled) * 7, "celled_verbs": len(celled), "verbs": len(VERB_TABLE),
                    "uncelled": sorted(v for v in VERB_TABLE if v not in celled)}
res["fixtures_shipped_off"] = {"season_factor_draw": repr(w.fixtures.get("season_factor_draw"))}
res["carriers_absent"] = {n: not hasattr(__import__("engine.season.state.carriers", fromlist=["x"]), n) for n in ("Faction", "Troop", "Cohort")}
res["person_has_kit_or_tradition"] = any(f in {x.name for x in __import__("dataclasses").fields(type(P[0]))} for f in ("kit", "equipment", "tradition", "weapon"))
npcs = yaml.safe_load(open("engine/season/npcs.yaml"))
res["npc_roster"] = {"rows": len(npcs["npcs"]), "with_concerns": sum(1 for n in npcs["npcs"] if n.get("concerns")), "ties": dict(collections.Counter(n.get("tie") for n in npcs["npcs"]))}
res["goals_rows"] = len(yaml.safe_load(open("engine/season/goals.yaml"))["goals"])
import importlib
sys.path.insert(0, "modules/combat")
wp = importlib.import_module("weapons"); tr = importlib.import_module("traditions")
res["oracle_content"] = {"weapons": len(wp.WEAPONS), "traditions": len(tr.TRADITIONS)}
from modules.mass_battle import config as MBC
res["oracle_content"]["mass_battle_troop_type_roles"] = len(MBC.TROOP_TYPE_ROLES)
res["oracle_content"]["mass_battle_role_spec"] = len(MBC.ROLE_SPEC)
json.dump(res, open(OUT, "w"), indent=1)
print(json.dumps({k: res[k] for k in ("persons", "cohorts", "effective_verbs", "executed_verbs", "alignment")}, indent=1)[:600])
