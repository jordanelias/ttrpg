"""Read-only stress test of the return routes in 2026-11-01-social-contest-matters-standpoints-and-fold.md section 5.5,
on the hand-built bench world that engine/season/tests/test_u7_remit.py uses (a Duke judges the party `p_mid`).
Usage: python probe_routes_hand_built.py > out.json   (about two minutes). Writes nothing in the tree.
Part A (first Partial determination found): who holds the determination claim, who is handed a Question, the
disposal edge, the judge's pursuits, a second determine on the same party, and a non-person matter.
Part B (first determination found at each band): the judge's pursuits and every other person's regard and
legitimacy estimate of the judge, before and after the round is witnessed."""
import sys, json
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[2]))  # repo root
from engine.season.tests.test_u7_remit import _world, _fold, _open, _determine, _kinds, PARTY, DUKE
from engine.season.data.matrix import WriteClass
from engine.season.loop.driver import mint_token
from engine.season.queries import world_q, person_q
from engine.season.data.pursuits import pursuit

def estimates(w):
    win = w.fixtures.get("estimate_window_seasons")
    return {p: (person_q.regard(w.persons[p], DUKE, w.fixtures), person_q.legitimacy(w.persons[p], DUKE, win))
            for p in w.persons if p != DUKE}

out = {}
# Part A
for n in range(80):
    w, d = _world()
    before = estimates(w); bp = dict(w.persons[DUKE].pursuits)
    o1 = _fold(w, d, _open("oc")); o2 = _fold(w, d, _determine(f"dt{n}"))
    if o2 and o2[0].kind == "matter.determined" and o2[0].degree == "Partial":
        break
out["A_act_id"] = n
out["A_events"] = {"open": _kinds(o1), "determine": _kinds(o2), "band": o2[0].degree}
out["A_disposal_edges_on_party"] = [(t.kind, t.subject, t.object) for t in w.tenures
                                    if t.live and t.subject == PARTY and t.kind in ("oblige", "detain", "ban")]
out["A_judge_pursuits_moved"] = w.persons[DUKE].pursuits != bp
d.witness(mint_token(w, WriteClass.INTERIOR), o1 + o2)
out["A_holders_of_determination_claim"] = {pid: sorted({c.source for c in p.ledger if "matter.determined" in str(c.predicate)})
                                           for pid, p in w.persons.items()
                                           if any("matter.determined" in str(c.predicate) for c in p.ledger)}
w.tick += 1
out["A_next_round_questions"] = {pid: [x.source + ":" + ",".join(x.referents)[:40] for x in world_q.questions_for(w, p)][:3]
                                 for pid, p in w.persons.items()}
out["A_estimates_changed"] = {p: [before[p], v] for p, v in estimates(w).items() if v != before[p]}
out["A_second_determine_same_party"] = _kinds(_fold(w, d, _determine("dt_again")))
w3, d3 = _world()
out["A_nonperson_matter"] = {"open": _kinds(_fold(w3, d3, _open("ocS", subject="S"))),
                             "determine": _kinds(_fold(w3, d3, _determine("dtS", subject="S"))),
                             "docket": [x.get("matter") for x in w3.docket]}
# Part B
seen = {}
for n in range(80):
    w, d = _world()
    w.persons[DUKE].pursuits = {pursuit("honour"): 0.5, pursuit("liberty"): 0.3, pursuit("stability"): 0.2}
    for pid, p in w.persons.items():
        if pid != DUKE and not p.pursuits:
            p.pursuits = {pursuit("justice"): 0.5, pursuit("honour"): 0.3, pursuit("liberty"): 0.2}
    before = estimates(w); bp = dict(w.persons[DUKE].pursuits)
    o1 = _fold(w, d, _open("oc")); o2 = _fold(w, d, _determine(f"dt{n}"))
    if not o2 or o2[0].kind != "matter.determined" or o2[0].degree in seen: continue
    d.witness(mint_token(w, WriteClass.INTERIOR), o1 + o2)
    after = estimates(w)
    seen[o2[0].degree] = {"act_id": n, "kinds": _kinds(o2), "judge_pursuits_moved": w.persons[DUKE].pursuits != bp,
                          "regard_and_legitimacy_changed": {p: [before[p], after[p]] for p in after if after[p] != before[p]}}
    if len(seen) == 3: break
out["B_by_band"] = seen
print(json.dumps(out, indent=1, default=str))
