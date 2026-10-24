"""Static inventory of open rows and null content, read from the tree (no season is run).

usage: PYTHONPATH=<repo> python static_inventory.py OUT.json"""
import sys, re, json, glob, collections, yaml, subprocess
out = sys.argv[1]
res = {}
# 1. hole-register rows produced in the v9 period
hr = yaml.safe_load(open("engine/season/hole_register.yaml"))["rows"]
hn = lambda i: int(i.split("-")[1])
CLOSEISH = re.compile(r"\b(CLOSED|DISCHARGED|LANDED|FALSIFIED|REVERTED|SUPERSEDED|RETIRED)\b")
scope = [r for r in hr if hn(r["id"]) >= 186 or "v9" in str(r.get("source", ""))]
res["hole_rows_total"] = len(hr)
res["hole_grade_total"] = dict(collections.Counter(r["grade"] for r in hr))
res["hole_scope"] = [{
    "id": r["id"], "grade": r["grade"], "kind": r["kind"], "tier": r["tier"],
    "hole": str(r["hole"])[:300], "owner": str(r["owner"])[:200], "unblocks": str(r["unblocks"])[:300],
    "source": str(r["source"])[:240], "closeish_tokens": sorted(set(CLOSEISH.findall(str(r["cite"]) + str(r["hole"])))),
    "cite_head": str(r["cite"])[:500]} for r in scope]
# 2. editorial ledger: last row per id, dated >= 2026-10-06, open-ish
last = {}
for f in sorted(glob.glob("registers/editorial_ledger*.jsonl")):
    if "archive" in f: continue
    for ln in open(f):
        ln = ln.strip()
        if not ln: continue
        try: r = json.loads(ln)
        except Exception: continue
        last[r.get("id")] = (f, r)
res["ed_open_since_v9"] = [{"id": i, "date": r.get("date"), "status": r.get("status"), "needs_jordan": r.get("needs_jordan"),
                            "file": f.split("/")[-1], "description": str(r.get("description"))[:700]}
                           for i, (f, r) in last.items()
                           if str(r.get("date", "0")) >= "2026-10-06" and (r.get("status") in ("open", "partial", "provisional", "deferred") or r.get("needs_jordan"))]
res["ed_needs_jordan_any_date"] = [i for i, (f, r) in last.items() if r.get("needs_jordan") is True]
# 3. state index table of the v9 plan
txt = open("workplans/valoria_master_workplan_v9.md").read()
sec = txt.split("## 3. THE STATE INDEX")[1].split("## 4. CROSSWALK")[0]
rows = []
for ln in sec.splitlines():
    if ln.startswith("| ") and not ln.startswith("| handle") and not ln.startswith("|---"):
        c = [x.strip() for x in ln.strip("|").split("|")]
        if len(c) >= 8: rows.append(dict(zip(["handle", "alias", "lane", "state", "gate", "R", "batch", "home"], c[:8])))
res["state_index"] = rows
# 4. verb table vs code
from engine.season.data.verbs import VERB_TABLE
from engine.season.loop.effects import EFFECTS
from engine.season.loop.predicates import REQUIRES_PREDICATES
vt = []
for v, row in VERB_TABLE.items():
    vt.append({"verb": v, "has_effect": v in EFFECTS, "typed_requires": row.requires_typed is not None,
               "predicate": v in REQUIRES_PREDICATES, "has_precondition": bool(row.has_precondition),
               "emits": bool(row.emits), "emits_on_refusal": bool(row.emits_on_refusal), "writes": bool(row.writes),
               "grade": getattr(row, "grade", None)})
res["verb_static"] = vt
# 5. YAML null scan of engine/season registries
def walk(o, path, acc):
    if isinstance(o, dict):
        for k, v in o.items(): walk(v, path + [str(k)], acc)
    elif isinstance(o, list):
        for i, v in enumerate(o): walk(v, path + ["[]"], acc)
    else:
        acc["n"] += 1
        if o is None or o == "": acc["null"] += 1; acc["paths"][".".join(p for p in path[-3:])] += 1
ys = {}
for f in sorted(glob.glob("engine/season/*.yaml")) + sorted(glob.glob("engine/season/data/*.yaml")) + ["references/npc_registry.yaml"]:
    try: d = yaml.safe_load(open(f))
    except Exception as e: ys[f] = {"error": str(e)[:80]}; continue
    acc = {"n": 0, "null": 0, "paths": collections.Counter()}
    walk(d, [], acc)
    ys[f] = {"values": acc["n"], "null_or_empty": acc["null"], "top_paths": acc["paths"].most_common(6)}
res["yaml_null_scan"] = ys
# 6. skip / xfail markers in the three suites
mk = collections.Counter(); ex = []
pat = re.compile(r"(pytest\.mark\.(xfail|skip|skipif)|pytest\.(skip|xfail)\()")
for root in ("tests/valoria", "engine/season/tests", "engine/tests"):
    for f in glob.glob(root + "/**/*.py", recursive=True):
        for i, ln in enumerate(open(f, errors="replace"), 1):
            m = pat.search(ln)
            if m:
                mk[(root, m.group(2) or m.group(3))] += 1
                if len(ex) < 400: ex.append([f, i, ln.strip()[:170]])
res["markers"] = [[list(k), n] for k, n in mk.items()]
res["marker_lines"] = ex
json.dump(res, open(out, "w"), indent=1, default=str)
print("ok", {k: (len(v) if hasattr(v, "__len__") else v) for k, v in res.items()})
