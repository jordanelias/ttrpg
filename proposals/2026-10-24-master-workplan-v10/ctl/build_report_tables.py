"""Render the code report's tables from the census JSON files in this directory (no season is run).

usage: python build_report_tables.py DIR OUT.json
DIR holds census2_s{0,1,2}.json, census_s0_nohooks.json, static_inventory.json, acquaintance_s0.json.
OUT.json maps a table key to a markdown string; build_report.py substitutes {{T:key}} placeholders."""
import sys, json, collections, os
D, OUT = sys.argv[1], sys.argv[2]
J = lambda f: json.load(open(os.path.join(D, f)))
R = [J(f"census2_s{i}.json") for i in (0, 1, 2)]
NH = J("census_s0_nohooks.json"); ST = J("static_inventory.json"); AQ = J("acquaintance_s0.json")
T = {}
def md(head, rows):
    return "\n".join(["| " + " | ".join(head) + " |", "|" + "|".join("---" for _ in head) + "|"] + ["| " + " | ".join(str(x) for x in r) + " |" for r in rows])

# per-seed identity and control
rows = [[r["seed"], r["content_hash"][:12], f'{r["log_events"]:,}', f'{r["acts_resolved"]:,}', r["persons_end"]] for r in R]
T["seeds"] = md(["seed", "World.content_hash (4 seasons)", "events", "acts resolved", "persons at end"], rows)
T["control"] = f'seed 0, 4 seasons: hooked `{R[0]["content_hash"][:12]}`, unhooked `{NH["content_hash"][:12]}`, equal = {R[0]["content_hash"] == NH["content_hash"]}'

# funnel per verb
F = collections.defaultdict(collections.Counter)
for r in R:
    for v, c in r["funnel"].items(): F[v].update(c)
rows = []
for v, c in sorted(F.items(), key=lambda kv: -sum(kv[1].values())):
    n = sum(c.values()); rows.append([f"`{v}`", n, c["made"], c["refused"], c["both"], f'{100*(c["made"]+c["both"])/n:.1f}%'])
tot = collections.Counter()
for c in F.values(): tot.update(c)
T["funnel"] = md(["verb", "acts resolved", "made only", "refused only", "made+refused", "executed share"], rows)
n = sum(tot.values())
T["funnel_total"] = f'{n:,} resolved acts: {tot["made"]:,} made ({100*tot["made"]/n:.1f}%), {tot["refused"]:,} refused ({100*tot["refused"]/n:.1f}%), {tot["both"]:,} both ({100*tot["both"]/n:.1f}%)'
T["zero_exec_verbs"] = ", ".join(f"`{v}`" for v, c in sorted(F.items()) if c["made"] + c["both"] == 0)

# admission classes
tot = collections.Counter()
for r in R: tot.update(r["admission"])
n = sum(tot.values())
T["admission"] = md(["admission outcome at the fold and the contest branch", "count", "share"],
                    [[k, f"{v:,}", f"{100*v/n:.1f}%"] for k, v in tot.most_common()]) + f"\n\nTotal {n:,} admission decisions over 3 seeds × 4 seasons."
A = collections.defaultdict(collections.Counter)
for r in R:
    for v, c in r["admission_by_verb"].items(): A[v].update(c)
rows = []
for v, c in sorted(A.items(), key=lambda kv: -(sum(kv[1].values()) - kv[1]["ADMITTED"])):
    ref = sum(c.values()) - c["ADMITTED"]
    if ref: rows.append([f"`{v}`", c["ADMITTED"], c["PRECONDITION_FALSE"], c["UNKNOWN_READ"], c["UNKNOWN_READ(no read recorded)"], ref])
T["admission_by_verb"] = md(["verb", "admitted", "precondition False", "UNKNOWN (read recorded)", "UNKNOWN (no read recorded)", "refused at admission"], rows)
inv = collections.Counter()
for r in R: inv.update(r["admission_refusals_not_in_resolved"])
refs = sum(v for k, v in tot.items() if k != "ADMITTED")
T["invisible"] = f'{sum(inv.values()):,} of {refs:,} admission refusals ({100*sum(inv.values())/refs:.1f}%) belong to acts that never enter `driver.resolved`, so `corpus_run.attribute` and `aperture` do not count them: ' + ", ".join(f"`{v}` {n}" for v, n in inv.most_common())

# deciding reads
l = collections.Counter()
for r in R:
    for k, p, v, n in r["refusal_last_read"]: l[(k, p, v)] += n
T["last_read"] = md(["refusal event", "last read the verdict recorded", "value", "count"], [[f"`{k}`", f"`{p}`", v, n] for (k, p, v), n in l.most_common(22)])
tot_ev = sum(r["refusal_events_total"] for r in R); no_read = sum(r["refusal_events_with_no_read"] for r in R)
T["refusal_events"] = f"{tot_ev:,} refusal Events over the three runs; {no_read:,} ({100*no_read/tot_ev:.1f}%) carry no recorded read, so the Event cannot say why it refused."
wk = collections.Counter()
for r in R:
    for k, n in r["trace"]["exists_kind"] if "exists_kind" in r["trace"] else []: wk[k] += n
kinds = collections.Counter()
for (k, p, v), n in l.items():
    if p.startswith("exists:") and v == "0": kinds[p] += n
T["exists_zero"] = ", ".join(f"`{p}` {n}" for p, n in kinds.most_common())
T["exists_zero_total"] = sum(kinds.values())
cond_nonsite = sum(n for (k, p, v), n in l.items() if p == "condition" and v == "UNKNOWN")
T["condition_nonsite"] = str(cond_nonsite)
T["wrong_referent_total"] = f"{T['exists_zero_total'] + cond_nonsite:,}"
T["wrong_referent_pct"] = f"{100 * (T['exists_zero_total'] + cond_nonsite) / tot_ev:.1f}%"
T["docket_empty"] = str(kinds.get("exists:DocketItem", 0))
T["graded_loss_n"] = str(sum(r["funnel"].get(v, {}).get("both", 0) for r in R for v in ("tell", "research", "surveil")))
T["exists_zero_total"] = f"{T['exists_zero_total']:,}"

# write failures
wr = collections.Counter(); gp = collections.Counter(); dc = collections.Counter(); nt = collections.Counter(); wc = collections.Counter()
for r in R:
    for k, n in r["trace"]["write_refused"]: wr[tuple(k)] += n
    for k, n in r["trace"]["gap"]: gp[k] += n
    for k, n in r["trace"]["decision"]: dc[k] += n
    for k, n in r["trace"]["note"]: nt[k] += n
    for k, n in r["trace"]["write_classes"]: wc[tuple(k)] += n
T["write_classes"] = md(["write class", "admitted", "count"], [[k[0], k[1], f"{n:,}"] for k, n in sorted(wc.items(), key=lambda kv: -kv[1])])
T["write_refused"] = md(["write class", "field", "refused writes (no-op or no subject)"], [[k[0], f"`{k[1]}`", n] for k, n in wr.most_common()])
T["gap"] = md(["GAP row (ids normalised)", "count"], [[g, n] for g, n in gp.most_common(10)])
wn = [(k, n) for k, n in dc.items() if "wrote nothing" in k]
T["wrote_nothing"] = md(["effect that produced no delta", "count"], [[k.replace(" wrote nothing", ""), n] for k, n in sorted(wn, key=lambda x: -x[1])])
T["wrote_nothing_total"] = sum(n for k, n in wn)
cap = [(k, n) for k, n in dc.items() if k.startswith("a migration into a rung at capacity")]
T["capacity_total"] = sum(n for k, n in cap)
rem = [(k, n) for k, n in nt.items() if "not granted" in k]
nob = [(k, n) for k, n in nt.items() if "know nobody" in k]
T["note_remit_total"] = sum(n for k, n in rem); T["note_nobody"] = md(["formation-time decline", "count"], [[k, n] for k, n in sorted(nob, key=lambda x: -x[1])])
T["note_presence"] = sum(n for k, n in nt.items() if k.startswith("`presence:`"))

# NULL content
tot_n = collections.defaultdict(lambda: [0, 0, 0])
allnp = collections.Counter()
for r in R:
    for f in r["never_populated"]: allnp[f[0]] += 1
np0 = R[0]["never_populated"]
T["never_populated"] = md(["carrier.field", "instances", "None", "empty"], [[f"`{f[0]}`", f[1], f[2], f[3]] for f in np0]) + f"\n\nFields 100% None/empty in every one of the 3 seeds: {sum(1 for k,v in allnp.items() if v==3)} of {len(allnp)} seen in any seed."
hi = [r for r in R[0]["null_scan"] if r[1] >= 50 and 0.9 <= r[4] < 1.0]
T["high_null"] = md(["carrier.field", "instances", "None", "empty", "null share"], [[f"`{r[0]}`", r[1], r[2], r[3], f"{100*r[4]:.1f}%"] for r in hi])
ev = R[0]
T["event_fields"] = f'Event.degree is None on {ev["events_degree_none"]:,} of {ev["log_events"]:,} Events ({100*ev["events_degree_none"]/ev["log_events"]:.1f}%); Event.observed is empty on {ev["events_observed_empty"]:,} ({100*ev["events_observed_empty"]/ev["log_events"]:.1f}%); Event.changes is empty on {ev["events_changes_empty"]:,} ({100*ev["events_changes_empty"]/ev["log_events"]:.1f}%); Event.causes is empty on {ev["events_causes_empty"]}.'
decl = set(R[0]["event_kinds"]) | set(R[0]["declared_never_emitted"]); em = set()
for r in R: em |= set(r["event_kinds"])
nev = sorted(decl - em)
T["never_emitted"] = f"{len(nev)} of {len(decl)} declared Event kinds were emitted in none of the three 4-season runs: " + ", ".join(f"`{k}`" for k in nev)
T["undeclared"] = "undeclared Event kinds seen: " + (", ".join(sorted(set(sum([r["undeclared_event_kinds"] for r in R], [])))) or "none")

# claims and ledger
T["acq"] = md(["point in the run (seed 0)", "persons", "know no one", "median known", "max known", "ledger min/median/max", "ledgers at cap (200)", "claims with a told chain"],
              [[a["at"], a["persons"], a["know_nobody"], a["known_median"], a["known_max"], f'{a["ledger_min"]}/{a["ledger_median"]}/{a["ledger_max"]}', a["ledger_at_cap"], a["claims_with_chain"]] for a in AQ])
kd = collections.Counter()
for r in R:
    for k in ("claim.deposited", "claim.decayed", "news.told", "news.untold"): kd[k] += r["event_kinds"].get(k, 0)
T["claims_events"] = ", ".join(f"`{k}` {v:,}" for k, v in kd.items())

# static
vs = ST["verb_static"]
T["verb_static"] = md(["property of the 56 verb-table rows", "rows", "verbs"],
    [["no effect function in `EFFECTS`", sum(1 for x in vs if not x["has_effect"]), ", ".join(f"`{x['verb']}`" for x in vs if not x["has_effect"])],
     ["writes: empty", sum(1 for x in vs if not x["writes"]), ", ".join(f"`{x['verb']}`" for x in vs if not x["writes"])],
     ["precondition present, neither typed nor predicate", sum(1 for x in vs if x["has_precondition"] and not x["typed_requires"] and not x["predicate"]), ", ".join(f"`{x['verb']}`" for x in vs if x["has_precondition"] and not x["typed_requires"] and not x["predicate"])],
     ["no `emits_on_refusal`", sum(1 for x in vs if not x["emits_on_refusal"]), ", ".join(f"`{x['verb']}`" for x in vs if not x["emits_on_refusal"])]])
ys = ST["yaml_null_scan"]
T["yaml_nulls"] = md(["registry", "values", "null or empty", "largest null paths"], [[f"`{f}`", d["values"], d["null_or_empty"], "; ".join(f"{p} ×{n}" for p, n in d["top_paths"][:3])] for f, d in ys.items() if "values" in d and d["null_or_empty"]])
mk = ST["markers"]
T["markers"] = md(["suite", "marker", "count"], [[m[0][0], m[0][1], m[1]] for m in mk])

# --- extra scalars used in prose
T["control1"] = None
c1 = J("census2_s0_1season.json")
T["control1"] = f'`{c1["content_hash"][:12]}`, equal to the first 12 digits of `BASE_HASHES[1]` in `engine/season/tests/test_season_weather.py` (`b2464a6c87dd9d2da9e3b3cbc8143fdf`): {c1["content_hash"][:12] == "b2464a6c87dd"}'
T["refusal_events_n"] = f"{tot_ev:,}"
nn = sum(n for k, n in nt.items() if "know nobody" in k)
T["note_nobody_total"] = f"{nn:,}"
refs = sum(v for k, v in collections.Counter({k: v for r in R for k, v in r['admission'].items()}.items()) if False) if False else None
adm_tot = collections.Counter()
for r in R: adm_tot.update(r["admission"])
refs = sum(v for k, v in adm_tot.items() if k != "ADMITTED")
T["admission_refusals_n"] = f"{refs:,}"
T["invisible_n"] = f"{sum(inv.values()):,}"
T["invisible_pct"] = f"{100*sum(inv.values())/refs:.1f}%"
T["know_nobody_end"] = str(AQ[-1]["know_nobody"]); T["acq_persons_end"] = str(AQ[-1]["persons"])
T["told_claims_max"] = str(max(a["claims_with_chain"] for a in AQ))
T["claim_dep"] = f'{kd["claim.deposited"]:,}'; T["claim_dec"] = f'{kd["claim.decayed"]:,}'
q = collections.Counter()
for r in R:
    for k, n in r["trace"]["query"]: q[k] += n
T["q_home"] = f'{q["home_of"]:,}'; T["q_presence"] = f'{q["presence"]:,}'; T["q_questions"] = f'{q["questions_for"]:,}'
r0 = R[0]["trace"]
T["write_rows_seed0"] = f'{sum(n for k, n in r0["write_classes"]):,}' if False else f'{sum(n for _, n in r0["write_classes"]):,}'
T["write_refused_seed0"] = f'{sum(n for k, n in r0["write_classes"] if not k[1]):,}'
# chain outcomes (text produced by chain_outcomes_probe.py)
import re
txt = open(os.path.join(D, "chain_outcomes_seed0_4seasons.txt")).read()
m_edges = re.search(r"cross-person edges (\d+)", txt); m_succ = re.search(r"succeeded \(made or both\): (\d+) ([0-9.]+)%", txt)
m_chain = re.search(r"deepest chain len (\d+) (\[.*?\])", txt); m_out = re.search(r"outcome (\{.*?\})", txt)
edges = {}
for m in re.finditer(r"antecedent=(\w+)\s+consequent=(\w+)\s+(\d+)", txt): edges[(m.group(1), m.group(2))] = int(m.group(3))
n_e = int(m_edges.group(1)); rr = edges.get(("refused", "refused"), 0)
chain = eval(m_chain.group(2)); cc = collections.Counter(chain)
T["chain_outcomes"] = (f"of {n_e:,} cross-person edges, {m_succ.group(1)} ({m_succ.group(2)}%) have an antecedent act that succeeded (made or both); {rr} ({100*rr/n_e:.1f}%) join two refusals. "
    f"Act outcomes at seed 0 (acts with Events in the log): {m_out.group(1)}; `unk` is an act that `corpus_run.attribute` does not return (not diagnosed). "
    f"The deepest chain has {m_chain.group(1)} steps: {cc['refused']} refused, {cc['made']} made, {cc['both']} both, {cc['unk']} unclassified.")


# --- §14: content and the choice surface (content_inventory.json, probe/out_*.json)
INV = J("content_inventory.json")
T["strata"] = md(["verb stratum", "verbs executed at least once / total", "attempts", "executed", "executed share"],
    [[k, f'{c["verbs_executed"]} / {c["verbs"]}', f'{c["attempts"]:,}', f'{c["executed"]:,}', f'{100*c["executed"]/c["attempts"]:.0f}%']
     for k, c in sorted(INV["strata"].items(), key=lambda x: -x[1]["attempts"])])
T["surface_scalars"] = (f'{INV["executed_acts"]:,} executed acts; {INV["executed_verbs"]} of 56 verbs execute at least once; the inverse Herfindahl over executed verbs '
    f'is {INV["effective_verbs"]} ("effective verbs"); the top three, {", ".join(f"`{v}` {n}" for v, n in INV["top3"])}, are {100*INV["top3_share"]:.0f}% of executions')
pf = INV["person_fields"]
T["inventory"] = md(["content", "what the tree holds", "what reaches `build_realm(0)`"], [
    ["Capability", f'`VOCATIONS` = {INV["vocations"]}, from `VERB_CAPABILITY` = {INV["verb_capability"]}', f'{pf["capability"]["non_empty"]} of {INV["persons"]} persons'],
    ["Ambitions (pursuit vectors)", f'15 axes; 46 named persons from NPC test cases (`npcs.yaml`: names and wants are the corpus\'s, not authored)', f'{pf["pursuits"]["non_empty"]} of {INV["persons"]} persons ({pf["pursuits"]["distinct"]} distinct); the {INV["cohorts"]} cohorts carry none'],
    ["Convictions", "creed weights", f'{pf["conviction"]["non_empty"]} persons ({pf["conviction"]["distinct"]} distinct); scar {pf["scar"]["non_empty"]}'],
    ["Decision making (verb × axis cells)", f'{INV["alignment"]["non_zero_cells"]} non-zero cells of {INV["alignment"]["possible"]} possible on {INV["alignment"]["celled_verbs"]} celled verbs', f'{len(INV["alignment"]["uncelled"])} of {INV["alignment"]["verbs"]} verbs uncelled: a conviction cannot rank them'],
    ["Relationships, knots, bonds", f'`npcs.yaml` gives each of {INV["npc_roster"]["rows"]} named persons a `concerns` subject and a `tie` ({INV["npc_roster"]["ties"]})', f'tenures at build {INV["tenure_kinds_at_build"]}; no acquaintance, kin or spouse edge'],
    ["Faction affiliations, subfactions", f'{len(INV["office_factions"])} faction names, held as a string on {INV["offices"]} offices', f'no Faction carrier {INV["carriers_absent"]["Faction"]}; no subfaction'],
    ["Offices", f'{INV["offices"]} seated offices (+2 foreign seats, shipped off)', f'upkeep declared by {INV["offices_with_upkeep"]} of {INV["offices"]}'],
    ["Equipment, martial traditions", f'`modules/combat`: {INV["oracle_content"]["weapons"]} weapons, {INV["oracle_content"]["traditions"]} traditions', f'a `Person` carries no kit, tradition or weapon field ({not INV["person_has_kit_or_tradition"]}); the season duel uses the class defaults (weapon `arming`, armour `light`, tradition `none`; only `end` is derived)'],
    ["Troop types, army variations", f'`modules/mass_battle`: {INV["oracle_content"]["mass_battle_troop_type_roles"]} troop-type roles, {INV["oracle_content"]["mass_battle_role_spec"]} role specs', f'no Troop carrier {INV["carriers_absent"]["Troop"]}; the engine feeds coarse infantry/cavalry; a cohort is a Person of weight 2'],
    ["Event decks, exogenous events", "designs only (`proposals/2026-08-31-unified-code-shape/05_WORLD_CHURN.md`)", f'none in `engine/season`; `season_factor_draw` ships {INV["fixtures_shipped_off"]["season_factor_draw"]}; no birth event'],
])
import glob as _g
order = ["baseline", "foreign", "guards", "foreign_guards", "capability", "exogenous", "all"]
label = {"baseline": "baseline", "foreign": "external empire on", "guards": "guards on", "foreign_guards": "empire + guards", "capability": "capability seeded (`copying` 1 to 3)", "exogenous": "weather draw on", "all": "all four on"}
rows = []
for f in sorted(_g.glob(os.path.join(D, "probe", "out_*.json"))):
    d = json.load(open(f)); m = d["march"]
    rows.append((d["seed"], order.index(d["arm"]), [d["seed"], label[d["arm"]], f'{d["events"]:,}', d["executed"], d["executed_verbs"], d["effective_verbs"], f'{m["march.declared"]}/{m["march.refused"]}/{m["army.arrived"]}', sum(d["field_events"].values())]))
T["probe"] = md(["seed", "arm (four seasons)", "events", "executed acts", "executed verbs", "effective verbs", "marches declared / refused / arrived", "field events"], [r[2] for r in sorted(rows)])
e8 = {json.load(open(f))["arm"]: json.load(open(f)) for f in _g.glob(os.path.join(D, "probe", "out8_*.json"))}
T["probe8"] = (f'Eight seasons at seed 0, baseline against the weather draw: {e8["baseline"]["events"]:,} events and {e8["baseline"]["executed"]:,} executed acts in both; '
    f'hashes {e8["baseline"]["hash"]} and {e8["exogenous"]["hash"]}.')

json.dump(T, open(OUT, "w"), indent=1)
print("tables:", len(T))
