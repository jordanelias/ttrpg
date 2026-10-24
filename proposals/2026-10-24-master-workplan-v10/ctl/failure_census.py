"""Failure census over a seeded multi-season run of engine/season (observation only).

usage: PYTHONPATH=<repo> python failure_census.py SEED SEASONS OUT.json [--no-hooks]

Counts, per run: the act funnel and every refusal (by kind, by deciding clause, by observed read),
UNKNOWN reads vs False preconditions at the fold's `_admits`, no-op and refused writes and GAPs from
the TRACE channel, undeclared Event kinds, and NULL / empty content across the World's carriers.
`--no-hooks` runs the same season with the `_admits` wrapper off, so a caller can compare
`World.content_hash()` with and without the instrument (the control)."""
import sys, re, json, collections, dataclasses
from engine.season.harness import storybar as SB, corpus_run as CR
from engine.season.trace_log import TRACE
from engine.season.loop.driver import SeasonDriver
from engine.season.data.verbs import VERB_TABLE, EVENT_KINDS

seed, seasons, out = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
hooks = "--no-hooks" not in sys.argv

NORM = re.compile(r"\b(p_npc_\d+|cohort_set_s_\d+|cohort_\w+|set_s_\d+\w*|s_s_\d+\w*|rec:[\w:.\-]+|[0-9a-f]{16}|off_\w+|terr_\w+|prop_\w+)\b")
def norm(s, n=120):
    return re.sub(r"\d+", "N", NORM.sub("#", str(s)))[:n]

adm = []
_elig = {}
if hooks:
    _oe = SeasonDriver._eligible
    def _eligible(self, w, a, row):
        r = _oe(self, w, a, row)
        _elig[a.id] = bool(r)
        return r
    SeasonDriver._eligible = _eligible
    _orig = SeasonDriver._admits
    def _admits(self, w, a, row):
        r = _orig(self, w, a, row)
        try:
            ok, kinds, v = r
            adm.append((a.verb, bool(ok), repr(v.value), v.failed, tuple(kinds or ()), a.id, w.tick,
                        _elig.get(a.id), len(v.observed or ())))
        except Exception:
            adm.append((a.verb, None, "?", None, (), a.id, w.tick, None, 0))
        return r
    SeasonDriver._admits = _admits

T = {"channels": collections.Counter(), "write_refused": collections.Counter(),
     "write_classes": collections.Counter(), "gap": collections.Counter(),
     "note": collections.Counter(), "decision": collections.Counter(), "query": collections.Counter()}
def tally(w, summary, n):
    for r in TRACE.rows:
        T["channels"][r.channel] += 1
        if r.channel == "WRITE":
            T["write_classes"][(r.detail.get("write_class"), bool(r.detail.get("admitted")))] += 1
            if not r.detail.get("admitted"):
                T["write_refused"][(r.detail.get("write_class"), norm(r.what, 80))] += 1
        elif r.channel == "GAP": T["gap"][norm(r.what)] += 1
        elif r.channel == "NOTE": T["note"][norm(r.what)] += 1
        elif r.channel == "DECISION": T["decision"][norm(r.what)] += 1
        elif r.channel == "QUERY": T["query"][r.what] += 1
    TRACE.rows.clear()

TRACE.rows.clear()
w, d, bounds = SB.drive(seed, seasons, "off", None, on_season=tally)
res = {"seed": seed, "seasons": seasons, "hooks": hooks, "content_hash": w.content_hash(),
       "persons_end": len(w.persons), "log_events": len(w.log), "acts_resolved": len(d.resolved)}

# --- admission verdicts (fold branch AND contest branch of resolve)
cls = collections.Counter(); by_verb = collections.defaultdict(collections.Counter)
failed = collections.Counter(); per_tick = collections.defaultdict(collections.Counter)
invisible = collections.Counter()
rids = d._resolved_ids
for verb, ok, val, fl, kinds, aid, tick, elig, nobs in adm:
    if ok: c = "ADMITTED"
    elif elig is False: c = "INELIGIBLE"
    elif val == "UNKNOWN": c = "UNKNOWN_READ" + ("" if nobs else "(no read recorded)")
    elif val == "False": c = "PRECONDITION_FALSE"
    else: c = "REFUSED_OTHER(counterparty)"
    cls[c] += 1; by_verb[verb][c] += 1; per_tick[tick][c] += 1
    if not ok and aid not in rids: invisible[verb] += 1
    if c.startswith(("UNKNOWN_READ", "PRECONDITION_FALSE")): failed[(verb, c, fl)] += 1
res["admission"] = dict(cls)
res["admission_by_verb"] = {v: dict(c) for v, c in sorted(by_verb.items())}
res["admission_by_tick"] = {str(t): dict(c) for t, c in sorted(per_tick.items())}
res["failed_conjunct"] = [[v, c, f, n] for (v, c, f), n in failed.most_common()]
res["admission_refusals_not_in_resolved"] = dict(invisible)

# --- act funnel (execution attributed to the act)
fun = collections.defaultdict(lambda: collections.Counter())
for a, made, refused in CR.attribute(w, d, seasons):
    k = ("made" if made and not refused else "refused" if refused and not made else "both" if made and refused else "neither")
    fun[a.verb][k] += 1
res["funnel"] = {v: dict(c) for v, c in sorted(fun.items())}
res["unrowed_acts"] = sum(1 for a in d.resolved if VERB_TABLE.get(a.verb) is None)
res["resolved_by_verb"] = dict(collections.Counter(a.verb for a in d.resolved))

# --- events
kinds = collections.Counter(e.kind for e in w.log)
refkinds = set()
for row in VERB_TABLE.values():
    em = row.emits_on_refusal
    for k in (em.values() if isinstance(em, dict) else (em or ())):
        refkinds.update(k if isinstance(k, (list, tuple)) else [k])
refkinds.add("act.ineligible")
res["event_kinds"] = dict(kinds)
res["undeclared_event_kinds"] = sorted(k for k in kinds if k not in EVENT_KINDS)
res["declared_never_emitted"] = sorted(k for k in EVENT_KINDS if k not in kinds)
res["events_degree_none"] = sum(1 for e in w.log if e.degree is None)
res["events_observed_empty"] = sum(1 for e in w.log if not e.observed)
res["events_changes_empty"] = sum(1 for e in w.log if not e.changes)
res["events_causes_empty"] = sum(1 for e in w.log if not e.causes)
obs = collections.Counter()
for e in w.log:
    if e.kind in refkinds and e.observed:
        o = e.observed[-1]
        o = o if isinstance(o, dict) else dataclasses.asdict(o) if dataclasses.is_dataclass(o) else {"predicate": str(o)}
        obs[(e.kind, norm(o.get("predicate"), 40), str(o.get("value"))[:20])] += 1
res["refusal_last_read"] = [[*k, n] for k, n in obs.most_common(60)]
res["refusal_events_total"] = sum(n for k, n in kinds.items() if k in refkinds)
res["refusal_events_with_no_read"] = sum(1 for e in w.log if e.kind in refkinds and not e.observed)

# --- TRACE tallies
res["trace"] = {k: ([[list(kk) if isinstance(kk, tuple) else kk, n] for kk, n in v.most_common(60)] if k != "channels" else dict(v))
                for k, v in T.items()}

# --- NULL / empty content across carriers
def fields_of(o):
    if dataclasses.is_dataclass(o): return [(f.name, getattr(o, f.name, None)) for f in dataclasses.fields(o)]
    if hasattr(o, "__slots__"): return [(s, getattr(o, s, None)) for s in o.__slots__]
    return list(vars(o).items()) if hasattr(o, "__dict__") else []
def empty(v):
    if v is None: return "none"
    if isinstance(v, (str, list, dict, tuple, set, frozenset)) and len(v) == 0: return "empty"
    return None
stat = collections.defaultdict(lambda: collections.Counter())
def scan(o, depth=0):
    cn = type(o).__name__
    for name, v in fields_of(o):
        key = f"{cn}.{name}"
        stat[key]["n"] += 1
        e = empty(v)
        if e: stat[key][e] += 1
        if depth < 1 and isinstance(v, (list, tuple)):
            for it in v:
                if dataclasses.is_dataclass(it): scan(it, depth + 1)
for coll in ("persons", "offices", "propositions", "records", "rungs", "sites"):
    for o in getattr(w, coll).values(): scan(o)
for e in w.log: scan(e, 1)
rows = []
for k, c in sorted(stat.items()):
    n = c["n"]; nul = c["none"] + c["empty"]
    rows.append([k, n, c["none"], c["empty"], round(nul / n, 3) if n else 0])
res["null_scan"] = rows
res["never_populated"] = [r for r in rows if r[1] >= 10 and r[4] == 1.0]
led = sorted(len(p.ledger) for p in w.persons.values())
res["ledger_sizes"] = {"min": led[0], "median": led[len(led) // 2], "max": led[-1], "empty": sum(1 for x in led if x == 0), "total_held": sum(led)}
json.dump(res, open(out, "w"), indent=1, default=str)
print("ok", out, res["content_hash"][:12], "events", res["log_events"])
