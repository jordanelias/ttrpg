"""Read-only validation of the CR-106 / CR-107 content drafts (revision 2) against build_realm(0).

Run, from the repository root: python proposals/2026-11-08-flow-conditioning/content_validate.py   (writes nothing)
Checks the structure the loaders will require AND re-derives every cohort row and every Church-site
condition from the stated rules, diffing the result against the drafts (so a hand-transcription error shows).
"""
import collections
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[1]
sys.path.insert(0, str(REPO))

from engine.season.harness import populated as P                     # noqa: E402
from engine.season.harness.populated import build_realm               # noqa: E402
from engine.season.queries import world_q                             # noqa: E402
from engine.season.data import cast                                   # noqa: E402
from engine.season.data.affiliations import conviction_map            # noqa: E402
from engine.season.data.rosters import FACTIONS, roster               # noqa: E402
from engine.substrate import descriptors                              # noqa: E402

fails = 0


def check(ok, msg):
    global fails
    print(("PASS " if ok else "FAIL ") + msg)
    if not ok:
        fails += 1


w = build_realm(0)
geo = yaml.safe_load((REPO / "systems/settlements/valoria_geography_v30.yaml").read_text())
ven = yaml.safe_load((REPO / "engine/season/venues.yaml").read_text())
sites = yaml.safe_load((HERE / "content_church_sites.yaml").read_text())
rows = yaml.safe_load((HERE / "content_cohorts.yaml").read_text())["cohorts"]
desc = yaml.safe_load((REPO / "references/descriptor_registry.yaml").read_text())

settle = {f"set_{s.lower().replace('-', '_')}": (s, d) for s, d in geo["settlements"].items()}
territories = sorted(r for r, g in w.rungs.items() if g.kind == "territory")
realm = next(r for r, g in w.rungs.items() if g.kind == "realm")
under_realm = {t for t in territories if t in world_q.descendants(w, realm)} if hasattr(world_q, "descendants") \
    else {t for t in territories if t in P.descendants(w, realm)}
settles_in = collections.Counter(P.territory_id_of(P.enclosing_territory(w, r))
                                 for r, g in w.rungs.items() if g.kind == "settlement")

# ---------------------------------------------------------------- A. Church sites
print("== A. Church-owned Sites")
kinds = set(roster("site_kinds"))
new = sites["site_kinds_append"]
check(not (set(new) & kinds), f"new kinds {new} collide with no existing site_kinds member")
for tbl in ("wear_per_season_rates", "capacity_floor_floors", "works_cost_costs", "band_floors_cells"):
    check(set(sites[tbl]) == set(new), f"{tbl} keyed on exactly the three new kinds")
for k, owner in sites["site_owner"]["cells"].items():
    check(owner in FACTIONS, f"site_owner[{k}] = {owner!r} is a factions member")
scale = w.fixtures.get("condition_scale")


def band(kind, cond):
    floors = sites["band_floors_cells"][kind]
    got = [b for b, f in floors.items() if cond >= f]
    return max(got, key=lambda b: floors[b]) if got else None


church_seat = ven["seats"]["Church"]
type_cap = {}
for r, (sid, d) in settle.items():
    type_cap.setdefault(d["type"], set()).add(world_q.capacity(w, r))
check(all(len(v) == 1 for v in type_cap.values()), f"capacity is uniform per settlement type: {type_cap}")
church_seat_type = geo["settlements"][church_seat]["type"]
check(sum(1 for s in geo["settlements"].values() if s["type"] == church_seat_type) == 1,
      f"the Church's seat type {church_seat_type} has exactly one settlement (per-type row = per-settlement)")


def expected_condition(kind, stype):
    if stype == church_seat_type:
        return scale
    fl = sorted(sites["band_floors_cells"][kind].values())          # [bottom, middle, top]
    cap = next(iter(type_cap[stype]))
    tiers = sorted({next(iter(v)) for t, v in type_cap.items() if t != church_seat_type})
    idx = 0 if cap == tiers[0] else (2 if cap == tiers[-1] else 1)
    hi = fl[idx + 1] if idx + 1 < len(fl) else scale
    return (fl[idx] + hi) // 2


minted = []      # (territory, settlement, slug, kind, condition)
for stype, srows in sites["venue_site_rows"].items():
    slugs = {b["slug"] for b in ven["buildings"][stype]}
    for row in srows:
        st = row["site"]
        check(isinstance(st, dict) and set(st) == {"kind", "condition"},
              f"{stype}:{row['slug']} uses the adopted nested shape site: {{kind, condition}}")
        check(row["slug"] in slugs, f"{stype}:{row['slug']} is an existing venues.yaml row")
        exp = expected_condition(st["kind"], stype)
        check(st["condition"] == exp, f"{stype}:{row['slug']} condition {st['condition']} == rule {exp}")
    for r, (sid, d) in settle.items():
        if d["type"] == stype:
            for row in srows:
                minted.append((P.territory_id_of(P.enclosing_territory(w, r)), sid, row["slug"],
                               row["site"]["kind"], row["site"]["condition"]))
per_kind = collections.Counter(m[3] for m in minted)
print("Church Sites by kind:", dict(sorted(per_kind.items())), "total", len(minted))
per_terr = collections.Counter(m[0] for m in minted)
print("Church Sites by territory:", {t: per_terr.get(P.territory_id_of(t), 0) for t in territories})
covered = 0
scope = [t for t in territories if t in under_realm and settles_in.get(P.territory_id_of(t), 0)]
for t in scope:
    n = per_terr.get(P.territory_id_of(t), 0)
    covered += n >= 1
    check(n >= 1, f"{t} (under {realm}, holds a settlement) holds >= 1 Church-owned Site ({n})")
print(f"coverage: {covered} of {len(scope)} territories under {realm} that hold a settlement")
for t in territories:
    if t in scope:
        continue
    tid = P.territory_id_of(t)
    n_set, n_sites = settles_in.get(tid, 0), per_terr.get(tid, 0)
    why = ("holds no settlement" if not n_set else
           f"foreign root (not under {realm}); {n_set} settlement(s)"
           + ("" if n_sites else ", no venue rows"))
    print(f"EXCEPTION {t}: {why}; Church Sites {n_sites}")
wor = [m for m in minted if m[3] == "worship"]
top = max(wor, key=lambda m: m[4])
check(top[1] == church_seat and sum(1 for m in wor if m[4] == top[4]) == 1,
      f"the single highest worship Site is at the Church's seat {church_seat} ({top[4]})")
order = {}
for m in wor:
    order.setdefault(geo["settlements"][m[1]]["type"], set()).add(band("worship", m[4]))
print("worship band by type:", {k: sorted(v) for k, v in sorted(order.items())})
check(order["Village"] == {"chapel"} and order["Town"] == {"church"} and order["Seat"] == {"cathedral"}
      and order["Cathedral-City"] == {"cathedral"}, "village chapel < town church < cathedral")
check(len(set(m[1:4] for m in minted)) == len(minted), "no duplicate minted Site (settlement, slug, kind)")

# ---------------------------------------------------------------- B. cohorts
print("== B. cohorts")
keys = {"rung", "weight", "label", "heritage", "conviction"}
check(all(set(r) <= keys for r in rows), "every row uses only rung/weight/label/heritage/conviction")
check(not any("faction" in r for r in rows), "NO row carries `faction:` (B1: commitment HELD behind a reader audit)")
check({r["rung"] for r in rows} == set(settle), f"every one of the {len(settle)} geography settlements has a cohort")
check(all(r["rung"] in w.rungs and w.rungs[r["rung"]].kind == "settlement" for r in rows),
      "every rung exists and is a settlement")
check(all(isinstance(r["weight"], int) and not isinstance(r["weight"], bool) and r["weight"] >= 2 for r in rows),
      "every weight is an int >= 2")
tot = collections.Counter()
for r in rows:
    tot[r["rung"]] += r["weight"]
over = {k: (v, world_q.capacity(w, k)) for k, v in tot.items() if v > world_q.capacity(w, k)}
check(not over, f"summed weight <= capacity at every rung (over: {over})")
check(all(r["heritage"] in descriptors.HERITAGES for r in rows), "every heritage is a heritage_roster member")
bad = []
for r in rows:
    try:
        conviction_map(r["conviction"], where=f"cohort {r['rung']}")
    except Exception as e:  # noqa: BLE001
        bad.append((r["rung"], str(e)[:80]))
check(not bad, f"every conviction passes conviction_map ({bad})")
ids = [(r["rung"], r.get("label")) for r in rows]
check(len(ids) == len(set(ids)), "no two cohorts share (rung, label)")
person_like = [r for r in rows for v in map(str, [r.get("label"), r["heritage"]])
               if v.startswith(("p_", "off_", "fac_", "NPC-", "cohort_")) or v in w.persons]
check(not person_like, "no row names a person or keys on a faction/office id")

# rule re-derivation (rules H, C, V of content_cohorts.yaml)
bands = {t: b["band"] for b in geo["radiation_bands"] for t in b["territories"]}
holder = {}
for t in territories:
    tid = P.territory_id_of(t)
    if tid in geo["provinces"]:
        holder[tid] = cast.resolve_faction(geo["provinces"][tid].get("faction"))
foreign_roots = {P.territory_id_of(t) for t in territories if t not in under_realm}
CON = desc["affiliation_roster"]["concerns"]
S, E, C = CON["church"][0], CON["einhir"][0], CON["altonia"][0]
engages = desc["heritage_roster"]["engages"]
church_seat_tid = geo["settlements"][church_seat]["territory"]
valorsmark_seat_tid = geo["settlements"][ven["seats"]["Crown"]]["territory"]
T11_SET = {"T11"}            # rule H2: the Varfell territory north of the lake (geography :152, :161)


def majority(tid):
    if tid in foreign_roots:
        return "schoenlander"                                   # H6 (T16's people)
    if holder[tid] == "Varfell":
        return "northern_einhir" if tid in T11_SET else "southern_einhir"   # H2 / H1
    b = bands[tid]
    return "southern_einhir" if b <= 1 else ("central_einhir" if b <= 3 else "northern_einhir")


reg = yaml.safe_load((REPO / "references/npc_registry.yaml").read_text())
import statistics  # noqa: E402
people_fac = collections.defaultdict(set)
fac_rows = collections.defaultdict(list)
for c in reg["characters"]:
    f = cast.faction_of(c)[0]
    fac_rows[f].append(c.get("affiliations") or {})
    if c.get("heritage"):
        people_fac[c["heritage"]].add(f)


def has_band_data(her):          # V's branch: the heritage holds a majority cohort in a territory under the realm
    return any(majority(geo["settlements"][sid]["territory"]) == her
               for r, (sid, d) in settle.items() if d["territory"] not in foreign_roots)


def conviction(her, tid):
    out = {S: 1, E: 1, C: 1}
    b = bands.get(tid)
    if not has_band_data(her):                                  # V2
        con = engages.get(her)
        if con:
            m = CON[con][0]
            (fac,) = people_fac[her]
            out[m] = statistics.median_low([a[m] for a in fac_rows[fac] if m in a])
        return out
    if her == "southern_einhir":
        out[CON[engages[her]][0]] = 6 - b
    elif her in ("northern_einhir", "central_einhir"):
        out[S] = 5 if tid == church_seat_tid else min(5, 1 + b)
    return out


heritage_people = {h.split("_")[0] for h in descriptors.HERITAGES}
expected = []
for r, (sid, d) in sorted(settle.items()):
    tid = d["territory"]
    cap = world_q.capacity(w, r)
    maj = majority(tid)
    here = [dict(rung=r, weight=2, heritage=maj)]
    extra = []
    if holder.get(tid) != "Varfell" and tid not in foreign_roots and bands[tid] <= 2:          # C1
        extra.append("southern_einhir" if maj != "southern_einhir" else majority(valorsmark_seat_tid))
    if tid in T11_SET:                                                                          # C2
        extra.append("southern_einhir")
    if holder.get(tid) == "Varfell" and maj == "southern_einhir" and cap >= 6:                 # C3
        extra.append("northern_einhir")
    for tag, s in ven["seats"].items():                                                         # C4
        if s == sid and tag.lower() in heritage_people and tag.lower() in descriptors.HERITAGES:
            extra.append(tag.lower())
    for h in extra:
        if 2 * (len(here) + 1) <= cap:
            here.append(dict(rung=r, weight=2, label=h.split("_")[0], heritage=h))
    for x in here:
        x["conviction"] = conviction(x["heritage"], tid)
    expected += here


def norm(x):
    return (x["rung"], x.get("label") or "", x["heritage"], x["weight"], tuple(sorted(x["conviction"].items())))


exp_s, got_s = sorted(map(norm, expected)), sorted(map(norm, rows))
check(exp_s == got_s, f"drafted rows == rows re-derived from rules H/C/V "
      f"(missing {sorted(set(exp_s) - set(got_s))[:3]}, extra {sorted(set(got_s) - set(exp_s))[:3]})")

by_rung = collections.defaultdict(set)
for r in rows:
    by_rung[r["rung"]].add(r["heritage"])
multi = sorted(k for k, v in collections.Counter(r["rung"] for r in rows).items() if v > 1)
ns = sorted(k for k, v in by_rung.items() if {"northern_einhir", "southern_einhir"} <= v)
print("cohort rows:", len(rows), "| settlements:", len(by_rung), "| settlements with >1 cohort:", len(multi), multi)
print("settlements with a northern AND a southern cohort:", len(ns), ns)
print("rows by label:", dict(collections.Counter(r.get("label") or "(majority)" for r in rows)))
print("band-data heritages:", sorted(h for h in descriptors.HERITAGES if has_band_data(h)))
print("rows by heritage:", dict(collections.Counter(r["heritage"] for r in rows)))
print("room left for migrate (capacity - cohorts), min:", min(world_q.capacity(w, k) - v for k, v in tot.items()))
print(f"== {fails} FAIL line(s)")
sys.exit(1 if fails else 0)
